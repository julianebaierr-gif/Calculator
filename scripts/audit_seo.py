import glob
import re
import os

html_files = glob.glob('*.html')
print(f"Total HTML files found: {len(html_files)}")

canonical_domains = {}
canonical_has_html = 0
missing_canonical = []
robots_meta_count = 0
missing_robots = []
favicon_in_head = 0

for f in html_files:
    content = open(f, encoding='utf-8', errors='ignore').read()
    
    # Canonical
    m = re.findall(r'<link[^>]*rel=[\"\']canonical[\"\'][^>]*href=[\"\']([^\"\']*)[\"\']', content, re.I)
    if not m:
        m = re.findall(r'<link[^>]*href=[\"\']([^\"\']*)[\"\'][^>]*rel=[\"\']canonical[\"\']', content, re.I)
    
    if m:
        c = m[0]
        d = re.findall(r'https?://[^/]+', c)
        dom = d[0] if d else 'RELATIVE'
        canonical_domains[dom] = canonical_domains.get(dom, 0) + 1
        if c.endswith('.html'):
            canonical_has_html += 1
    else:
        missing_canonical.append(f)
        
    # Robots
    if re.search(r'<meta[^>]*name=[\"\']robots[\"\']', content, re.I):
        robots_meta_count += 1
    else:
        missing_robots.append(f)

    # Favicon
    if re.search(r'<link[^>]*rel=[\"\'](?:shortcut )?icon[\"\']', content, re.I):
        favicon_in_head += 1

print("\n--- Canonical Domains ---")
for k, v in canonical_domains.items():
    print(f"  {k}: {v}")
print(f"Total with .html in canonical: {canonical_has_html}")
print(f"Missing canonical: {len(missing_canonical)}")

print("\n--- Robots Meta Tag ---")
print(f"Has robots tag: {robots_meta_count}")
print(f"Missing robots tag: {len(missing_robots)}")

print("\n--- Favicon Tag in <head> ---")
print(f"Has favicon tag: {favicon_in_head}")
print(f"Missing favicon tag: {len(html_files) - favicon_in_head}")
