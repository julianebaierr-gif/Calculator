"""
Verification script for Batch 22 tools.
Checks:
- File existence
- <article class="article-body"> presence
- Word count strictly > 1,000 words (excluding HTML tags and KaTeX math)
"""

import os
import re
import sys

# Ensure UTF-8 output encoding
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BATCH_22_TOOLS = [
    "due-date-calculator.html",
    "fat-intake-calculator.html",
    "heart-rate-zone-calculator.html",
    "lean-body-mass-calculator.html",
    "max-heart-rate-calculator.html",
    "met-calculator.html",
    "ovulation-calculator.html",
    "pregnancy-weight-gain-calculator.html"
]

def count_article_words(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.search(r'<article class="article-body">(.*?)</article>', content, re.DOTALL)
    if not match:
        return 0, "No <article class='article-body'> found!"

    article_text = match.group(1)

    # Strip script and style tags if any
    article_text = re.sub(r'<script.*?</script>', ' ', article_text, flags=re.DOTALL)
    article_text = re.sub(r'<style.*?</style>', ' ', article_text, flags=re.DOTALL)
    # Strip HTML tags
    article_text = re.sub(r'<[^>]+>', ' ', article_text)
    # Strip KaTeX display math $$ ... $$ and inline math $ ... $
    article_text = re.sub(r'\$\$.*?\$\$', ' ', article_text, flags=re.DOTALL)
    article_text = re.sub(r'\$.*?\$', ' ', article_text)

    # Normalize whitespace and count words
    words = article_text.split()
    return len(words), None

def main():
    print("=" * 60)
    print("BATCH 22 ARTICLE WORD COUNT VERIFICATION")
    print("=" * 60)

    all_passed = True
    for tool in BATCH_22_TOOLS:
        path = os.path.join(BASE_DIR, tool)
        if not os.path.exists(path):
            print(f"[MISSING] {tool}: FILE MISSING")
            all_passed = False
            continue

        words, err = count_article_words(path)
        if err:
            print(f"[FAIL] {tool}: {err}")
            all_passed = False
        elif words < 1000:
            print(f"[FAIL] {tool}: ONLY {words} WORDS (Required: >1000)")
            all_passed = False
        else:
            print(f"[PASS] {tool}: {words} words (PASS > 1,000)")

    print("=" * 60)
    if all_passed:
        print("[SUCCESS] ALL 8 BATCH 22 TOOLS PASSED THE 1,000+ WORD COUNT STANDARD!")
    else:
        print("[WARN] SOME TOOLS FAILED VERIFICATION. EXPANSION REQUIRED.")
    print("=" * 60)

if __name__ == "__main__":
    main()
