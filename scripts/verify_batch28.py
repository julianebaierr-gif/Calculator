import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BATCH_FILES = [
    'absolute-value-calculator.html',
    'area-calculator.html',
    'arithmetic-sequence-calculator.html',
    'circle-calculator.html',
    'cube-root-calculator.html',
    'decimal-to-fraction-calculator.html',
    'exponent-calculator.html',
    'factorial-calculator.html'
]

print("=== BATCH 28 WORD COUNT & INTEGRITY AUDIT ===")
all_pass = True

for fname in BATCH_FILES:
    fpath = os.path.join(BASE_DIR, fname)
    if not os.path.exists(fpath):
        print(f"[-] {fname}: NOT FOUND YET")
        all_pass = False
        continue
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'<article class="article-body">(.*?)</article>', content, re.DOTALL)
    if not match:
        print(f"[FAIL] {fname}: <article class=\"article-body\"> NOT FOUND!")
        all_pass = False
        continue
    
    body_text = match.group(1)
    text_only = re.sub(r'<[^>]+>', ' ', body_text)
    words = len(text_only.split())
    
    status = "PASS" if words >= 1000 else "FAIL (<1000)"
    if words < 1000:
        all_pass = False
    print(f"[{status}] {fname}: {words:,} words in article body")

if all_pass:
    print("\n>>> ALL TOOLS IN BATCH 28 MEET THE 1,000+ WORD REQUIREMENT! <<<")
else:
    print("\n>>> SOME TOOLS ARE MISSING OR DO NOT MEET THE 1,000+ WORD REQUIREMENT! <<<")
