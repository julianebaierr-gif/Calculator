import glob
import re

html_files = glob.glob('*.html')
total_html_links = 0
for f in html_files:
    c = open(f, encoding='utf-8', errors='ignore').read()
    links = re.findall(r'href=[\"\']([a-zA-Z0-9_\-]+\.html)[\"\']', c)
    total_html_links += len(links)

print(f"Total href=xyz.html links across all {len(html_files)} files: {total_html_links}")
