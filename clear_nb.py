import json
import sys

path = r'c:\Users\bintu\Desktop\baitapai\day11\Day-11-Guardrails-HITL-Responsible-AI\notebooks\assignment11_defense_pipeline.ipynb'

with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb.get('cells', []):
    if 'outputs' in cell:
        cell['outputs'] = []
    if 'execution_count' in cell:
        cell['execution_count'] = None

with open(path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook outputs cleared successfully.")
