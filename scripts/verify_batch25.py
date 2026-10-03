import re
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BATCH_25_FILES = [
    "power-converter.html",
    "force-converter.html",
    "data-storage-converter.html",
    "data-transfer-rate-converter.html",
    "frequency-converter.html",
    "flow-rate-converter.html",
    "fuel-economy-converter.html",
    "angle-converter.html",
]

def check_article_words(filepath):
    if not os.path.exists(filepath):
        return None, "File does not exist"
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    m = re.search(r'<article class="article-body">(.*?)</article>', html, re.DOTALL)
    if not m:
        return 0, "No <article class='article-body'> found!"
    
    content = m.group(1)
    content = re.sub(r'<script.*?</script>', ' ', content, flags=re.DOTALL)
    content = re.sub(r'<style.*?</style>', ' ', content, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', content)
    text = re.sub(r'\\[a-zA-Z]+', ' ', text)
    words = text.split()
    return len(words), "OK"

print("=" * 60)
print("BATCH 25 ARTICLE WORD COUNT VERIFICATION")
print("=" * 60)

all_passed = True
for fname in BATCH_25_FILES:
    fpath = os.path.join(BASE_DIR, fname)
    wc, status = check_article_words(fpath)
    if wc is None:
        print(f"[MISSING] {fname}: {status}")
        all_passed = False
    elif wc < 1000:
        print(f"[FAIL] {fname}: {wc} words (FAILED < 1,000)")
        all_passed = False
    else:
        print(f"[PASS] {fname}: {wc} words (PASS > 1,000)")

print("=" * 60)
if all_passed:
    print("[SUCCESS] ALL 8 BATCH 25 TOOLS PASSED THE 1,000+ WORD COUNT STANDARD!")
else:
    print("[WAITING] Some tools are missing or under the 1,000 words requirement.")
print("=" * 60)
