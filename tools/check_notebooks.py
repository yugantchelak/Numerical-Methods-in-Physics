"""Run every notebook top to bottom, headless, and report errors, warnings and runtimes.

usage (from anywhere):  python tools/check_notebooks.py

Each notebook runs in its own subprocess with matplotlib's Agg backend, a 300 s per-cell timeout and a
600 s per-notebook timeout. Nothing is saved: the notebooks on disk are never modified. The exit code is 0
only if every notebook passes with no warnings and every easter egg produces output.
"""
import glob, json, os, subprocess, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep
NB_TIMEOUT = 600

# Executed in a fresh subprocess for each notebook.
ONE = r'''
import os, sys, json, time
os.environ["MPLBACKEND"] = "Agg"
import nbformat
from nbformat.v4 import new_code_cell
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError, CellTimeoutError
p = sys.argv[1]
nb = nbformat.read(p, 4)
# Agg cannot show windows, so plt.show() warns "FigureCanvasAgg is non-interactive". That is caused by this
# headless runner, not by the notebooks, so silence exactly that message (every other warning is still reported).
# Also close all figures after every cell, exactly as Jupyter's inline backend does, so one cell's
# figure can't leak into the next (plain Agg keeps figures open across cells).
nb.cells.insert(0, new_code_cell("; ".join([
    "import warnings",
    "warnings.filterwarnings('ignore', message='FigureCanvasAgg is non-interactive')",
    "import matplotlib.pyplot as _plt",
    "get_ipython().events.register('post_run_cell', lambda *a: _plt.close('all'))"])))
res = {"status": "PASS", "detail": "", "warnings": [], "eggs": []}
t0 = time.time()
try:
    NotebookClient(nb, timeout=300, kernel_name="python3", resources={"metadata": {"path": os.path.dirname(p)}}).execute()
except CellTimeoutError as e:
    res["status"], res["detail"] = "TIMEOUT", str(e).splitlines()[0]
except CellExecutionError as e:
    res["status"], res["detail"] = "ERROR", [l for l in str(e).splitlines() if l.strip()][-1]
res["seconds"] = time.time() - t0
for i, c in enumerate(nb.cells[1:]):               # i is the cell's index in the original notebook
    for o in c.get("outputs", []):
        if o.get("name") == "stderr" or o.get("output_type") == "error":
            res["warnings"].append(f"cell {i}: " + (o.get("text") or o.get("ename", "")).strip()[:200])
    if "easter-egg" in c.metadata.get("tags", []) or "secret checker" in c.source:
        out = "".join(o.get("text", "") for o in c.get("outputs", [])).strip()
        res["eggs"].append(out.splitlines()[-1] if out else "(no output!)")
print("RESULT" + json.dumps(res))
'''

paths = sorted(p for p in glob.glob(ROOT + '**/*.ipynb', recursive=True) if '.ipynb_checkpoints' not in p)
all_ok, total = True, 0.0
for p in paths:
    rel = os.path.relpath(p, ROOT)
    t0 = time.time()
    try:
        r = subprocess.run([sys.executable, '-c', ONE, p], capture_output=True, text=True, timeout=NB_TIMEOUT,
                           encoding='utf-8', env={**os.environ, 'PYTHONIOENCODING': 'utf-8'})
        line = [l for l in r.stdout.splitlines() if l.startswith('RESULT')]
        res = json.loads(line[-1][6:]) if line else {'status': 'CRASH', 'detail': r.stderr[-300:], 'warnings': [],
                                                     'eggs': [], 'seconds': time.time() - t0}
    except subprocess.TimeoutExpired:
        res = {'status': 'NB-TIMEOUT', 'detail': f'> {NB_TIMEOUT}s', 'warnings': [], 'eggs': [], 'seconds': NB_TIMEOUT}
    total += res['seconds']
    ok = res['status'] == 'PASS' and not res['warnings'] and all(e != '(no output!)' for e in res['eggs'])
    all_ok &= ok
    print(f"{res['status']:<7} {res['seconds']:6.1f}s  warnings={len(res['warnings'])}  {rel}  {res['detail']}")
    for w in res['warnings']:
        print('            WARNING', w)
    for e in res['eggs']:
        print('            egg ->', e[:110])

print(f'\nTotal {total:.0f}s for {len(paths)} notebooks. ' + ('ALL PASS, no warnings.' if all_ok else 'PROBLEMS FOUND'))
sys.exit(0 if all_ok else 1)
