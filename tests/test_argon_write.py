"""Exercise streaming failures and source provenance without model requests."""
import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('argon_write_test', ROOT / 'tools/scripts/argon_write.py')
writer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(writer)


def event(content='', model=writer.MODEL, finish=None, index=0):
    return {'model': model, 'choices': [{'index': index, 'delta': {'content': content}, 'finish_reason': finish}]}


class Stream:
    def __init__(self, events, error=None):
        self.events, self.error = events, error
        self.status_code = 429 if error else 200
        self.text = '{"error":{"message":"quota exceeded"}}' if error else ''

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def raise_for_status(self):
        if isinstance(self.error, writer.requests.HTTPError):
            raise self.error

    def iter_lines(self):
        yield b': heartbeat'
        yield b''
        for value in self.events:
            if isinstance(value, Exception):
                raise value
            if isinstance(value, dict):
                value = json.dumps(value, ensure_ascii=False).encode()
            yield b'data: ' + value
            yield b''


@pytest.fixture
def inputs(tmp_path):
    prompt = tmp_path / 'prompt.txt'
    prompt.write_text('按原文梳理：输入、推理与结论。', encoding='utf-8')
    return prompt, tmp_path / 'new' / 'chapter-01'


def stub(monkeypatch, events, error=None):
    calls = []

    def post(url, **kwargs):
        calls.append((url, kwargs))
        return Stream(events, error)

    monkeypatch.setattr(writer.requests, 'post', post)
    return calls


def receipt(prefix):
    return json.loads(Path(str(prefix) + '-receipt.json').read_text())


def test_full_prompt_and_source_hashes_are_separate(monkeypatch, tmp_path, inputs):
    prompt, prefix = inputs
    sources = tmp_path / 'sources'
    (sources / 'nested').mkdir(parents=True)
    original = sources / 'nested' / 'transcript.txt'
    original.write_text('SOURCE-ONLY-TEXT', encoding='utf-8')
    extra = tmp_path / 'official.txt'
    extra.write_text('原始资料', encoding='utf-8')
    calls = stub(monkeypatch, [event('{"标题":'), event('"学习"}', finish='stop'),
                               {'choices': [], 'usage': {'total_tokens': 90}}, b'[DONE]'])
    monkeypatch.setenv('ARGON_ENDPOINT', 'http://127.0.0.1:9999/v1/chat/completions')
    assert writer.request(prompt, prefix, [sources, extra, original], max_tokens=1234) == {'标题': '学习'}
    assert len(calls) == 1
    assert calls[0][0] == 'http://127.0.0.1:9999/v1/chat/completions'
    payload = calls[0][1]['json']
    assert payload['messages'][1]['content'] == prompt.read_text()
    assert 'SOURCE-ONLY-TEXT' not in json.dumps(payload)
    assert payload['max_tokens'] == 1234
    assert payload['model'] == writer.MODEL
    audit = receipt(prefix)
    assert audit['usage']['total_tokens'] == 90
    assert audit['stream_done'] and not audit['error']
    assert audit['source_mode'] == 'audit_only_not_appended_to_prompt'
    assert len(audit['source_snapshot']) == 2
    actual = {p['path']: p['sha256'] for p in audit['source_snapshot']}
    assert actual[str(original)] == hashlib.sha256(original.read_bytes()).hexdigest()
    assert audit['prompt_sha256'] == hashlib.sha256(prompt.read_bytes()).hexdigest()
    assert Path(str(prefix) + '-prompt.txt').read_bytes() == prompt.read_bytes()
    assert b': heartbeat' in Path(str(prefix) + '-events.sse').read_bytes()


@pytest.mark.parametrize('events,expected', [
    ([event('{}', model='other', finish='stop'), b'[DONE]'], 'Unexpected returned models'),
    ([event('{', model=writer.MODEL), event('}', model='other', finish='stop'), b'[DONE]'], 'Unexpected returned models'),
    ([event('{}', model=None, finish='stop'), b'[DONE]'], 'Unexpected returned models'),
    ([event('{}', finish='length'), b'[DONE]'], 'Incomplete completion'),
    ([event('{}'), b'[DONE]'], 'Incomplete completion'),
    ([event('{}', finish='stop')], 'without [DONE]'),
    ([event('{', finish='stop'), b'[DONE]'], 'JSONDecodeError'),
    ([event('[]', finish='stop'), b'[DONE]'], 'Expected a JSON object'),
    ([event('{"value":NaN}', finish='stop'), b'[DONE]'], 'Invalid JSON constant'),
    ([event('{"value":Infinity}', finish='stop'), b'[DONE]'], 'Invalid JSON constant'),
    ([event('{"value":-Infinity}', finish='stop'), b'[DONE]'], 'Invalid JSON constant'),
    ([event('{}', finish='stop'), event('extra'), b'[DONE]'], 'after finish_reason'),
    ([event('{}', finish='stop', index=1), b'[DONE]'], 'Unexpected completion choice'),
    ([{'error': {'message': 'upstream unavailable'}}, b'[DONE]'], 'upstream unavailable'),
    ([b'not-json', b'[DONE]'], 'JSONDecodeError'),
    ([{'choices': [{'delta': {'content': ['bad']}}]}, b'[DONE]'], 'must be text'),
    ([event('{'), writer.requests.ReadTimeout('disconnected')], 'ReadTimeout'),
])
def test_failed_stream_keeps_evidence_and_does_not_retry(monkeypatch, inputs, events, expected):
    prompt, prefix = inputs
    calls = stub(monkeypatch, events)
    with pytest.raises(RuntimeError, match=expected.replace('[', r'\[').replace(']', r'\]')):
        writer.request(prompt, prefix)
    assert len(calls) == 1
    assert not Path(str(prefix) + '.json').exists()
    audit = receipt(prefix)
    assert audit['error']
    raw = Path(str(prefix) + '-raw.txt').read_bytes()
    assert audit['output_sha256'] == hashlib.sha256(raw).hexdigest()
    before = Path(str(prefix) + '-receipt.json').read_bytes()
    with pytest.raises(FileExistsError, match='fresh output prefix'):
        writer.request(prompt, prefix)
    assert len(calls) == 1
    assert Path(str(prefix) + '-receipt.json').read_bytes() == before


def test_http_failure_still_writes_receipt(monkeypatch, inputs):
    prompt, prefix = inputs
    stub(monkeypatch, [], error=writer.requests.HTTPError('429 Too Many Requests'))
    with pytest.raises(RuntimeError, match='429 Too Many Requests'):
        writer.request(prompt, prefix)
    assert receipt(prefix)['stream_done'] is False
    assert receipt(prefix)['http_error'] == {
        'status': 429, 'body': '{"error":{"message":"quota exceeded"}}'}
    assert Path(str(prefix) + '-raw.txt').read_text() == ''


def test_multiline_sse_and_done_at_eof(monkeypatch, inputs):
    prompt, prefix = inputs

    class Multiline(Stream):
        def iter_lines(self):
            yield b'event: message'
            yield b'data: {"model": "gemini-4-argon",'
            yield b'data: "choices": [{"delta": {"content": "{}"}, "finish_reason": "stop"}]}'
            yield b''
            yield b'data: [DONE]'

    monkeypatch.setattr(writer.requests, 'post', lambda *args, **kwargs: Multiline([]))
    assert writer.request(prompt, prefix) == {}


def test_cli_defaults_and_repeatable_source(monkeypatch, tmp_path, inputs):
    prompt, prefix = inputs
    first, second = tmp_path / 'first.txt', tmp_path / 'second.txt'
    first.write_text('first')
    second.write_text('second')
    calls = stub(monkeypatch, [event('{}', finish='stop'), b'[DONE]'])
    monkeypatch.delenv('ARGON_ENDPOINT', raising=False)
    monkeypatch.setattr('sys.argv', ['argon_write.py', '--prompt', str(prompt), '--output-prefix', str(prefix),
                                    '--source', str(first), '--source', str(second)])
    writer.main()
    assert calls[0][0] == writer.DEFAULT_ENDPOINT
    assert calls[0][1]['json']['max_tokens'] == 24000
    assert len(receipt(prefix)['source_snapshot']) == 2
