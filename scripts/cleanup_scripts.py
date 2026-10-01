import glob
import re

files = glob.glob("*.html")
removed_polyfill = 0
added_mathjax = 0

polyfill_pattern = re.compile(r'\s*<script\s+src=["\']https://polyfill\.io/[^"\']+["\']></script>', re.IGNORECASE)
mathjax_tag = '  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>'

for f in files:
    with open(f, "r", encoding="utf-8") as fh:
        content = fh.read()

    modified = False
    if polyfill_pattern.search(content):
        content = polyfill_pattern.sub("", content)
        modified = True
        removed_polyfill += 1

    # Check if file has LaTeX formulas (\\[ or \\() but lacks MathJax
    if ("\\[" in content or "\\(" in content) and "mathjax" not in content.lower() and "katex" not in content.lower():
        if "</head>" in content:
            content = content.replace("</head>", f"{mathjax_tag}\n</head>")
            modified = True
            added_mathjax += 1

    if modified:
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(content)

print(f"Removed polyfill.io from {removed_polyfill} files.")
print(f"Added MathJax script to {added_mathjax} files.")
