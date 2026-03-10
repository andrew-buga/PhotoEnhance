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
        if any(k in line for k in ["torch.compile(net", "f0f4ff", "BEFORE / AFTER", "suptitle", "torch.compile: CodeFormer", "_cmp_path = os.path.join"]):
            print(f"[{i}]: {repr(line[:120])}")
