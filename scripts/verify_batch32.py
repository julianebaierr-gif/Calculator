# -*- coding: utf-8 -*-
"""
Verification Script for Batch 32:
8 Geometry, Physics, and Business Calculators
"""
import os
import sys
from bs4 import BeautifulSoup

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

BATCH_32_FILES = [
    "perimeter-calculator.html",
    "surface-area-calculator.html",
    "volume-calculator.html",
    "percentage-change-calculator.html",
    "markup-calculator.html",
    "density-calculator.html",
    "pressure-calculator.html",
    "speed-calculator.html"
]

def verify_tool(fname):
    fpath = os.path.join(BASE_DIR, fname)
    if not os.path.exists(fpath):
        return False, f"File {fname} does not exist!"
    
    with open(fpath, "r", encoding="utf-8") as fp:
        html = fp.read()
    
    soup = BeautifulSoup(html, "html.parser")
    
    # 1. Word count in article-body
    article = soup.find("article", class_="article-body")
    if not article:
        return False, "Missing <article class='article-body'>"
    
    words = article.get_text().split()
    word_count = len(words)
    if word_count < 1000:
        return False, f"Word count ({word_count}) is below 1,000 threshold!"
    
    # 2. Schema.org JSON-LD (FAQPage & WebApplication)
    scripts = soup.find_all("script", type="application/ld+json")
    has_faq = any("FAQPage" in s.get_text() for s in scripts)
    has_app = any("WebApplication" in s.get_text() for s in scripts)
    if not (has_faq and has_app):
        return False, f"Missing Schema.org JSON-LD (FAQ: {has_faq}, App: {has_app})"
    
    # 3. Canonical link
    canonical = soup.find("link", rel="canonical")
    if not canonical or fname not in canonical.get("href", ""):
        return False, f"Canonical tag missing or incorrect for {fname}"
    
    # 4. KaTeX integration
    has_katex = "katex" in html
    if not has_katex:
        return False, "KaTeX integration missing"
    
    # 5. Tables and worked examples
    has_table = bool(soup.find("table", class_="data-table"))
    has_examples = bool(soup.find("div", class_="worked-example-card"))
    if not has_table:
        return False, "Missing .data-table"
    if not has_examples:
        return False, "Missing .worked-example-card"

    return True, f"PASS ({word_count} words)"

def main():
    all_ok = True
    print("=" * 60)
    print("BATCH 32 VERIFICATION AUDIT")
    print("=" * 60)
    for f in BATCH_32_FILES:
        ok, msg = verify_tool(f)
        status = "✓ PASS" if ok else "✗ FAIL"
        print(f"[{status}] {f.ljust(35)} : {msg}")
        if not ok:
            all_ok = False
    print("=" * 60)
    if all_ok:
        print("ALL 8 TOOLS PASSED STRICT QUALITY CRITERIA!")
    else:
        print("SOME TOOLS FAILED VERIFICATION.")
        sys.exit(1)

if __name__ == "__main__":
    main()
