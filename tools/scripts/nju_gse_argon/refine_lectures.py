"""Resolve residual review findings with a small Argon edit request."""
import argparse
import concurrent.futures
import hashlib
import json

from argon_writer import ROOT, request, sources
from edit_lectures import leaves, apply_edits


def refine(i):
    folder = ROOT/f'lecture{i:02d}'/'generation'
    snapshot = folder/'refinement-draft.json'
    if not snapshot.exists():
        snapshot.write_bytes((folder/'prose.json').read_bytes())
    draft = json.loads(snapshot.read_text())
    findings = (folder/'residual-findings.md').read_text()
    prompt = '''下面是已经统一编辑过的教材。请只修正复核发现的残留问题，同时检查同一错误的其他出现位置。用自然具体的讲解替换错误，不要添加通用免责声明。主线、页码和完整教学内容都保持。返回JSON：
{"edits":[{"path":"/sections/0/units/0/reading","old":"字段内准确存在且唯一的原句或段落","new":"正确自然的新句或段落"}],"editor_note":"实际修正说明"}
old 必须逐字复制，不改原句字符；各替换互不重叠。可编辑代码和公式；不需要修的字段不返回。
'''+ '\n【残留发现】\n'+findings+'\n【全文】\n'+json.dumps(list(leaves(draft)),ensure_ascii=False)+'\n【来源】\n'+sources(i)
    response = request(i, 'refinement', prompt)
    final = apply_edits(draft, response['edits'])
    text = json.dumps(final,ensure_ascii=False,indent=2)+'\n'
    (folder/'prose.json').write_text(text)
    report={'edits':len(response['edits']), 'final_sha256':hashlib.sha256(text.encode()).hexdigest(), 'editor_note':response.get('editor_note','')}
    (folder/'refinement-applied.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(f'L{i:02d} refined {len(response["edits"])} passages',flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('lectures',nargs='+',type=int)
    args=parser.parse_args()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        list(pool.map(refine,args.lectures))
