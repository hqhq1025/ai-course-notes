"""Compile lecture sources twice and retain only canonical PDFs and QA logs."""
import argparse
import concurrent.futures
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3] / 'nju-generative-software-engineering-2026/argon-rewrite'
REPO = ROOT.parents[1]


def build(i):
    d = ROOT/f'lecture{i:02d}'
    stem = f'lecture{i:02d}-notes'
    temp = Path(tempfile.gettempdir())/'nju-gse-argon-build'/d.name
    temp.mkdir(parents=True, exist_ok=True)
    qa = d/'qa'; qa.mkdir(exist_ok=True)
    for n in [1,2]:
        result = subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error',
                                 f'-output-directory={temp}',stem+'.tex'],cwd=d,capture_output=True,text=True,timeout=180)
        (qa/f'compile-pass{n}.log').write_text(result.stdout+result.stderr)
        if result.returncode:
            print(i,'COMPILE FAILED',result.stdout[-2500:],flush=True)
            raise RuntimeError(f'L{i} compilation failed')
    shutil.copy2(temp/(stem+'.pdf'),d/(stem+'.pdf'))
    for name, cmd in [
        ('coverage', ['python3',str(REPO/'tools/scripts/check_note_coverage.py'),str(d/(stem+'.tex')),'--manifest',str(d/'lecture-manifest.md')]),
        ('quality', ['bash',str(REPO/'tools/scripts/check_quality.sh'),str(d/(stem+'.tex'))])]:
        r = subprocess.run(cmd,cwd=REPO,capture_output=True,text=True)
        (qa/f'{name}-report.txt').write_text(r.stdout+r.stderr)
        if name=='coverage' and r.returncode: raise RuntimeError(r.stdout+r.stderr)
    checker = Path.home()/'.agents/skills/speak-plainly/scripts/check.py'
    if checker.is_file():
        r = subprocess.run(['python3',str(checker),str(d/(stem+'.md')),'--lang','zh'],
                           cwd=REPO,capture_output=True,text=True)
        (qa/'language-report.txt').write_text(r.stdout+r.stderr)
    else:
        message = 'SKIP language check: optional speak-plainly checker is not installed.\n'
        (qa/'language-report.txt').write_text(message)
        print(i,message.strip(),flush=True)
    r = subprocess.run(['python3',str(REPO/'tools/scripts/render_pdf_qa.py'),str(d/(stem+'.pdf'))],cwd=REPO,capture_output=True,text=True,timeout=180)
    (qa/'render-command.log').write_text(r.stdout+r.stderr)
    if r.returncode:raise RuntimeError(r.stdout+r.stderr)
    print(i,'BUILT',subprocess.check_output(['pdfinfo',str(d/(stem+'.pdf'))],text=True).split('Pages:')[1].splitlines()[0].strip(),'pages',flush=True)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('lectures',nargs='+',type=int);args=ap.parse_args()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:list(pool.map(build,args.lectures))
