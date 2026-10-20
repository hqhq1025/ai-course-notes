"""Bound requests to one chapter; resume only missing complete outputs."""
import argparse
import concurrent.futures
import json
from pathlib import Path
from argon_writer import ROOT, section, finish_lecture


def assemble(i):
    d=ROOT/f'lecture{i:02d}'
    p=json.loads((d/'generation/plan.json').read_text())
    paths=[d/f'generation/section-{n+1:02d}.json' for n in range(len(p['sections']))]
    ends=d/'generation/bookends.json'
    if not ends.exists() or not all(p.exists() for p in paths):return
    obj=json.loads(ends.read_text());obj['sections']=[json.loads(p.read_text()) for p in paths]
    expected=[x['id'] for x in json.loads((d/'sources/slides.json').read_text())]
    actual=[u['slide_id'] for s in obj['sections'] for u in s['units']]
    assert sorted(actual)==sorted(expected)
    target=d/'generation/prose.json'
    if not target.exists():
        target.write_text(json.dumps(obj,ensure_ascii=False,indent=2))
        print(f'L{i:02d} COMPLETE {len(obj["sections"])} chapters {len(actual)} slides',flush=True)


ap=argparse.ArgumentParser();ap.add_argument('lectures',nargs='+',type=int);ap.add_argument('--workers',type=int,default=4);args=ap.parse_args()
failures=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
    jobs={}
    for i in args.lectures:
        p=json.loads((ROOT/f'lecture{i:02d}/generation/plan.json').read_text())
        for n in range(len(p['sections'])):jobs[pool.submit(section,i,n)]=(i,f'section-{n+1:02d}')
        jobs[pool.submit(finish_lecture,i)]=(i,'bookends')
    for job in concurrent.futures.as_completed(jobs):
        i,name=jobs[job]
        try:job.result();assemble(i)
        except Exception as e:
            failures.append((i,name));print(f'L{i:02d} {name} FAILED {type(e).__name__}: {e}',flush=True)
if failures:
    print('Failed requests:',failures,flush=True)
    raise SystemExit(1)
