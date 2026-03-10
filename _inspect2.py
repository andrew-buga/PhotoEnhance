import json, sys
sys.stdout.reconfigure(encoding="utf-8")
NB = "PhotoEnhance_MVP.ipynb"
with open(NB, encoding="utf-8") as f:
    nb = json.load(f)
for cell in nb["cells"]:
    if cell["cell_type"] != "code":
        continue
    src = cell["source"]
    for i, line in enumerate(src):
        if 495 <= i <= 540 or 555 <= i <= 580 or 190 <= i <= 200:
            print(f"[{i}]: {repr(line[:100])}")
