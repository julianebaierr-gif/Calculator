# -*- coding: utf-8 -*-
"""
Verification script for Batch 29:
1. fraction-to-percent-calculator.html
2. geometric-sequence-calculator.html
3. logarithm-calculator.html
4. long-division-calculator.html
5. mean-median-mode-calculator.html
6. midpoint-calculator.html
7. modulo-calculator.html
8. nth-root-calculator.html
"""
import os
import sys
from bs4 import BeautifulSoup

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

BATCH_FILES = [
    "fraction-to-percent-calculator.html",
    "geometric-sequence-calculator.html",
    "logarithm-calculator.html",
    "long-division-calculator.html",
    "mean-median-mode-calculator.html",
    "midpoint-calculator.html",
    "modulo-calculator.html",
    "nth-root-calculator.html"
]

def verify_tool(filename):
    path = os.path.join(BASE_DIR, filename)
    if not os.path.exists(path):
        return False, "File does not exist"
    
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article", class_="article-body")
    if not article:
        return False, "Missing <article class='article-body'>"
    
    words = len(article.get_text().split())
    if words < 1000:
        return False, f"Article word count {words} < 1000 threshold"
    
    # Check for basic required elements
    card = soup.find("div", class_="calculator-card")
    if not card:
        return False, "Missing .calculator-card"
    
    table = soup.find("table", class_="data-table")
    if not table:
        return False, "Missing .data-table"
    
    example = soup.find("div", class_="worked-example-card")
    if not example:
        return False, "Missing .worked-example-card"
        
    faq = soup.find("div", class_="faq-accordion")
    if not faq:
        return False, "Missing .faq-accordion"
        
    return True, f"PASS ({words} words, complete structures)"

def main():
    print("=" * 60)
    print("VERIFYING BATCH 29 CALCULATORS (Word count >= 1000 & Structures)")
    print("=" * 60)
    all_ok = True
    for f in BATCH_FILES:
        ok, msg = verify_tool(f)
        status = "[OK]  " if ok else "[FAIL]"
        print(f"{status} {f:38} : {msg}")
        if not ok:
            all_ok = False
    print("=" * 60)
    if all_ok:
        print("ALL BATCH 29 TOOLS PASS QUALITY & WORD COUNT AUDIT!")
    else:
        print("SOME TOOLS FAILED VERIFICATION.")
        sys.exit(1)

if __name__ == "__main__":
    main()
