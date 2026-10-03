# -*- coding: utf-8 -*-
"""
Verification script for Batch 30 calculators.
Checks word counts, structural cards, tables, FAQs, schemas, and JS DOM IDs.
"""
import os
import sys
import re
from bs4 import BeautifulSoup

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

BATCH_30_FILES = [
    "square-root-calculator.html",
    "percent-to-fraction-calculator.html",
    "percent-error-calculator.html",
    "rounding-calculator.html",
    "factors-calculator.html",
    "sum-of-integers-calculator.html",
    "triangle-area-calculator.html",
    "variance-calculator.html",
]

def verify():
    all_pass = True
    print(f"=== Verifying Batch 30 ({len(BATCH_30_FILES)} files) ===")
    
    for fn in BATCH_30_FILES:
        fp = os.path.join(BASE_DIR, fn)
        if not os.path.exists(fp):
            print(f"[FAIL] Missing file: {fn}")
            all_pass = False
            continue
            
        with open(fp, "r", encoding="utf-8") as f:
            content = f.read()
            
        soup = BeautifulSoup(content, "html.parser")
        
        # 1. Word count in article
        article = soup.find("article", class_="article-body")
        if not article:
            print(f"[FAIL] {fn}: Missing <article class='article-body'>")
            all_pass = False
            continue
        text = article.get_text()
        words = len(re.findall(r"\b[A-Za-z0-9'-]+\b", text))
        
        # 2. Mathematical formulas
        has_math = "$$" in content or bool(soup.find(class_="formula-box"))
        
        # 3. Data table
        table = soup.find("table", class_="data-table")
        
        # 4. Worked examples
        examples = soup.find_all(class_="worked-example-card")
        
        # 5. FAQs
        faqs = soup.find_all(class_="faq-item")
        
        # 6. JSON-LD
        schemas = soup.find_all("script", type="application/ld+json")
        
        # Status checks
        status = "PASS"
        issues = []
        if words < 1000:
            status = "FAIL"
            issues.append(f"Words: {words} < 1000")
        if not has_math:
            status = "FAIL"
            issues.append("Missing KaTeX formulas")
        if not table:
            status = "FAIL"
            issues.append("Missing .data-table")
        if len(examples) < 2:
            status = "FAIL"
            issues.append(f"Worked examples: {len(examples)} < 2")
        if len(faqs) < 3:
            status = "FAIL"
            issues.append(f"FAQs: {len(faqs)} < 3")
        if len(schemas) < 2:
            status = "FAIL"
            issues.append(f"Schemas: {len(schemas)} < 2")
            
        if status == "PASS":
            print(f"[OK] {fn:35} | Words: {words:4} | Examples: {len(examples)} | FAQs: {len(faqs)} | Schemas: {len(schemas)}")
        else:
            print(f"[{status}] {fn:35} | Words: {words:4} | Issues: {', '.join(issues)}")
            all_pass = False

    if all_pass:
        print("\nAll 8 Batch 30 calculators PASSED all checks!")
    else:
        print("\nSome checks failed. Please fix before proceeding.")
    return all_pass

if __name__ == "__main__":
    if not verify():
        sys.exit(1)
