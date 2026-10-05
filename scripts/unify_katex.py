import glob
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html_files = glob.glob(os.path.join(BASE_DIR, "*.html"))

CANONICAL_KATEX = """  <!-- KaTeX Math Rendering Support -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
"""

updated = 0
for f in html_files:
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        content = fp.read()

    if "</head>" not in content:
        continue

    head_idx = content.find("</head>")
    head_content = content[:head_idx]
    rest = content[head_idx:]

    # Remove any existing KaTeX links and scripts from head
    lines = head_content.splitlines()
    new_lines = []
    skip_comment = False
    for line in lines:
        if "KaTeX Math Rendering Support" in line:
            continue
        if "katex" in line.lower() or "auto-render" in line.lower():
            continue
        new_lines.append(line)

    clean_head = "\n".join(new_lines).rstrip() + "\n"
    new_content = clean_head + CANONICAL_KATEX + rest

    if new_content != content:
        with open(f, "w", encoding="utf-8") as fp:
            fp.write(new_content)
        updated += 1

print(f"Total HTML files updated with canonical KaTeX: {updated} of {len(html_files)}")
