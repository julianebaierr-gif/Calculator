import glob
import re
from bs4 import BeautifulSoup

html_files = glob.glob('*.html')
h1_map = {}
for f in html_files:
    if f in ['index.html', '404.html', 'about.html', 'privacy-policy.html', 'terms.html', 'disclaimer.html', 'contact.html']:
        continue
    c = open(f, encoding='utf-8', errors='ignore').read()
    soup = BeautifulSoup(c, 'html.parser')
    h1 = soup.find('h1')
    h1_text = h1.get_text(strip=True).lower() if h1 else ''
    h1_clean = re.sub(r'[^a-z0-9]', '', h1_text)
    if h1_clean:
        h1_map.setdefault(h1_clean, []).append((f, h1_text))

duplicates = {k: v for k, v in h1_map.items() if len(v) > 1}
print(f"Duplicate H1 Headings count: {len(duplicates)}")
for k, v in duplicates.items():
    print(f"H1: {v[0][1]}")
    for item in v:
        print(f"   -> {item[0]}")
