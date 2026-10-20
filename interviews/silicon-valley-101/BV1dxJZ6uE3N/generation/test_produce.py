"""Verify this episode uses the shared writer without changing its prompt."""
import importlib.util
from pathlib import Path


def test_episode_request_delegates_without_appending_sources(monkeypatch, tmp_path):
    spec = importlib.util.spec_from_file_location(
        'episode_produce_test', Path(__file__).with_name('produce.py'))
    episode = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(episode)
    (tmp_path / 'sources').mkdir()
    (tmp_path / 'audio.srt').write_text('字幕')
    monkeypatch.setattr(episode, 'EPISODE', tmp_path)
    calls = []
    monkeypatch.setattr(episode._writer, 'request', lambda *args, **kwargs: calls.append((args, kwargs)))
    episode.request(tmp_path / 'prompt.txt', tmp_path / 'result')
    assert calls == [((tmp_path / 'prompt.txt', tmp_path / 'result'),
                      {'sources': [tmp_path / 'sources', tmp_path / 'audio.srt']})]
