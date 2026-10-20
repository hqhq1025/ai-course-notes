"""Formatting changes must preserve the saved Argon prose and executable examples."""
import importlib.util
from pathlib import Path

import pytest


SCRIPT = Path(__file__).resolve().parents[1] / 'tools/scripts/nju_gse_argon/render_notes.py'
spec = importlib.util.spec_from_file_location('nju_argon_render', SCRIPT)
render = importlib.util.module_from_spec(spec)
spec.loader.exec_module(render)


def test_inline_math_emphasis_and_code_keep_their_meanings():
    text = r'**复杂度为 $2^n - 1$**，检查 `a_b && $HOME`。'
    result = render.esc(text)
    assert r'\textbf{复杂度为 \(2^n - 1\)}' in result
    assert r'\texttt{a\_b \&\& \$HOME}' in result
    assert '**' not in result


def test_lists_keep_numbering_across_blank_lines_and_close_before_prose():
    result = render.prose('先检查输入。\n\n1. **读取**源码。\n\n2. 执行测试。\n\n然后核对输出。\n\n- 保留日志。')
    assert result.count(r'\begin{enumerate}') == 1
    assert result.count(r'\begin{itemize}') == 1
    assert result.count(r'\item ') == 3
    assert result.index(r'\end{enumerate}') < result.index('然后核对输出。')
    assert result.endswith(r'\end{itemize}')


def test_presentation_changes_structure_without_replacing_saved_prose():
    obj = {'sections': [{'summary': '检查输入。执行测试。'}]}
    edits = [{'path': ['sections', 0, 'summary'], 'before': '检查输入。执行测试。',
              'after': '- **检查输入。**\n- 执行测试。'}]
    assert render.apply_presentation(obj, edits)['sections'][0]['summary'] == edits[0]['after']


def test_existing_inline_step_numbers_can_be_reflowed_into_a_list():
    before = '1. 读取；2. 检查；3. 提交。'
    after = '1. **读取**；\n\n2. 检查；\n\n3. 提交。'
    assert render.apply_presentation({'lead': before}, [
        {'path': ['lead'], 'before': before, 'after': after},
    ])['lead'] == after


def test_exercise_heading_does_not_repeat_the_model_supplied_number():
    assert render.exercise_parts(2, '**练习二：检查协议。**\n\n先读取源码。') == (
        '练习 2：检查协议', '先读取源码。')
    assert render.exercise_parts(2, '先读取源码。') == ('练习 2', '先读取源码。')


def test_presentation_does_not_insert_markdown_inside_math():
    with pytest.raises(ValueError, match='formula'):
        render.apply_presentation({'lead': '$x=y$'}, [
            {'path': ['lead'], 'before': '$x=y$', 'after': '$x=**y**$'},
        ])


@pytest.mark.parametrize('before,after', [
    ('旧版本。', '**旧版本。**'),
    ('需要 3 次检查。', '需要 **2** 次检查。'),
])
def test_presentation_rejects_stale_sources_and_wording_changes(before, after):
    with pytest.raises(ValueError):
        render.apply_presentation({'lead': '需要 3 次检查。'}, [
            {'path': ['lead'], 'before': before, 'after': after},
        ])
