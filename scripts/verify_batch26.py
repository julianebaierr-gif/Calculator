import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BATCH_26_FILES = [
    "density-converter.html",
    "illuminance-converter.html",
    "thermal-conductivity-converter.html",
    "viscosity-converter.html",
    "cooking-converter.html",
    "number-base-converter.html",
    "roman-numeral-converter.html",
    "time-converter.html"
]

def count_article_words(filepath):
    if not os.path.exists(filepath):
        return None, "File does not exist"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    m = re.search(r'<article class="article-body">(.*?)</article>', content, re.DOTALL)
    if not m:
        return 0, "No <article class='article-body'> tag found"
    
    article_text = m.group(1)
    text_clean = re.sub(r'<[^>]+>', ' ', article_text)
    words = text_clean.split()
    return len(words), None

print("="*60)
print("BATCH 26 ARTICLE WORD COUNT VERIFICATION")
print("="*60)

all_pass = True
for fn in BATCH_26_FILES:
    fp = os.path.join(BASE_DIR, fn)
    wc, err = count_article_words(fp)
    if err:
        print(f"[MISSING] {fn}: {err}")
        all_pass = False
    elif wc < 1000:
        print(f"[FAIL] {fn}: {wc} words (MUST BE > 1,000)")
        all_pass = False
    else:
        print(f"[PASS] {fn}: {wc} words (PASS > 1,000)")

print("="*60)
if all_pass:
    print("[SUCCESS] ALL 8 BATCH 26 TOOLS PASSED THE 1,000+ WORD COUNT STANDARD!")
else:
    print("[WAITING] Some tools are missing or under the 1,000 words requirement.")
print("="*60)
