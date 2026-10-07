import glob
import re

html_files = glob.glob('*.html')
footer_bottom_patterns = set()

for f in html_files:
    content = open(f, encoding='utf-8', errors='ignore').read()
    m = re.findall(r'<div class=[\"\']footer-bottom-links[\"\']>(.*?)</div>', content, re.S)
    if m:
        # Normalize whitespace
        norm = " ".join(m[0].split())
        footer_bottom_patterns.add(norm)
    else:
        footer_bottom_patterns.add(f"NO_FOOTER_BOTTOM_LINKS_IN_{f}")

print(f"Unique footer-bottom-links patterns found: {len(footer_bottom_patterns)}")
for p in list(footer_bottom_patterns)[:5]:
    print("Pattern:", p)
