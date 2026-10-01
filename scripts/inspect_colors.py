import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("\n=== Silo Cards in category pages ===")
cat_list = ['health.html', 'finance.html', 'math.html', 'engineering.html', 'solar-energy.html', 'mechanical.html', 'civil.html', 'chemical.html', 'fire-safety.html', 'programmer.html', 'datetime.html', 'converter.html']
for cat_file in cat_list:
    with open(cat_file, 'r', encoding='utf-8') as f:
        content = f.read()
    silo_cards = re.findall(r'<a href="[^"]+" class="silo-card"[^>]*style="([^"]+)"', content)
    tag = re.findall(r'<span class="category-tag"[^>]*style="([^"]+)"', content)
    body_class = re.findall(r'<body[^>]*class="([^"]+)"', content)
    print(f"{cat_file:20}: body={body_class[:1]} cards={silo_cards[:1]} tag={tag[:1]}")

print("\n=== Calculator Pages Body Class ===")
for f in sorted(glob.glob('*.html')):
    if f in ['index.html', '404.html'] + cat_list:
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    body_class = re.findall(r'<body[^>]*class="([^"]+)"', c)
    print(f"{f:32}: body={body_class[:1]}")
