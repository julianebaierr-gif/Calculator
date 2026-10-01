import glob
import re

html_files = glob.glob("*.html")
katex_files = []
latex_syntax_files = []

for hf in html_files:
    with open(hf, "r", encoding="utf-8") as f:
        content = f.read()
    if "katex" in content.lower():
        katex_files.append(hf)
    if "\\[" in content or "\\(" in content:
        latex_syntax_files.append(hf)

print(f"Files loading KaTeX: {len(katex_files)}")
print(f"Files with \\[ or \\(: {len(latex_syntax_files)}")
if len(katex_files) < len(latex_syntax_files):
    print("Files with LaTeX but NO KaTeX:")
    for f in latex_syntax_files:
        if f not in katex_files:
            print(f"  - {f}")
