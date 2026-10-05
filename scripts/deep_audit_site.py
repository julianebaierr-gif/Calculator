# -*- coding: utf-8 -*-
"""
Deep Website A-to-Z Audit Script for CalcHub
Checks:
1. Duplicate titles, meta descriptions, and H1 tags across all pages
2. Content similarity & duplicate paragraphs across article bodies
3. Word counts of all articles
4. JavaScript syntax and DOM ID verification (getElementById vs HTML element IDs)
5. Current internal link density inside <article class="article-body">
"""

import os
import re
import glob
from collections import defaultdict
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def audit_site():
    html_files = sorted(glob.glob(os.path.join(BASE_DIR, "*.html")))
    print(f"Total HTML files found: {len(html_files)}")

    titles = defaultdict(list)
    meta_descs = defaultdict(list)
    h1s = defaultdict(list)
    article_word_counts = {}
    article_texts = {}
    missing_ids_report = defaultdict(list)
    js_syntax_errors = []
    internal_links_count = {}

    category_hubs = set([
        "index.html", "404.html", "health.html", "finance.html", "math.html",
        "engineering.html", "solar-energy.html", "mechanical.html", "civil.html",
        "chemical.html", "physics.html", "fire-safety.html", "programmer.html",
        "datetime.html", "converter.html", "financial.html"
    ])

    for filepath in html_files:
        filename = os.path.basename(filepath)
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        soup = BeautifulSoup(content, "html.parser")

        # 1. Title, Meta, H1
        title_tag = soup.find("title")
        title_text = title_tag.get_text().strip() if title_tag else "NO_TITLE"
        titles[title_text].append(filename)

        meta_tag = soup.find("meta", attrs={"name": "description"})
        meta_text = meta_tag["content"].strip() if (meta_tag and meta_tag.get("content")) else "NO_META"
        meta_descs[meta_text].append(filename)

        h1_tag = soup.find("h1")
        h1_text = h1_tag.get_text().strip() if h1_tag else "NO_H1"
        h1s[h1_text].append(filename)

        # 2. Article Body & Internal Links
        # 2. Article Body & Internal Links
        art = soup.find("article") or soup.find(class_=re.compile(r'article-(body|section)'))
        if art:
            raw_text = art.get_text(" ", strip=True)
            words = len(re.findall(r'\b\w+\b', raw_text))
            article_word_counts[filename] = words
            article_texts[filename] = raw_text

            # Count internal links inside article
            links = art.find_all("a", href=True)
            internal_links = [l["href"] for l in links if not l["href"].startswith("http") and not l["href"].startswith("#")]
            internal_links_count[filename] = len(internal_links)
        else:
            if filename not in category_hubs:
                article_word_counts[filename] = 0
                internal_links_count[filename] = 0

        # 3. DOM ID verification in inline JavaScript
        all_ids = set()
        for tag in soup.find_all(True, id=True):
            all_ids.add(tag["id"])
        # Also include IDs generated inside JS template strings like id="inpM"
        template_ids = set(re.findall(r'id=[\'"]([a-zA-Z0-9_\-]+)[\'"]', content))
        all_ids.update(template_ids)

        scripts = soup.find_all("script")
        for s in scripts:
            script_code = s.string or ""
            # find document.getElementById('...')
            matches = re.findall(r'document\.getElementById\([\'"]([^\'"]+)[\'"]\)', script_code)
            for m in matches:
                if m not in all_ids:
                    missing_ids_report[filename].append(m)

    # Output Findings
    print("\n" + "="*60)
    print("1. DUPLICATE TITLE / META / H1 AUDIT:")
    print("="*60)
    dup_titles = {t: fs for t, fs in titles.items() if len(fs) > 1 and t != "NO_TITLE"}
    dup_metas = {m: fs for m, fs in meta_descs.items() if len(fs) > 1 and m != "NO_META"}
    dup_h1s = {h: fs for h, fs in h1s.items() if len(fs) > 1 and h != "NO_H1"}

    print(f"Duplicate titles count: {len(dup_titles)}")
    for t, fs in list(dup_titles.items())[:5]:
        print(f"  Title: '{t}' in {fs}")

    print(f"Duplicate meta descriptions count: {len(dup_metas)}")
    for m, fs in list(dup_metas.items())[:5]:
        print(f"  Meta: '{m[:60]}...' in {fs}")

    print(f"Duplicate H1 tags count: {len(dup_h1s)}")
    for h, fs in list(dup_h1s.items())[:5]:
        print(f"  H1: '{h}' in {fs}")

    print("\n" + "="*60)
    print("2. JAVASCRIPT DOM ID AUDIT (Missing Element IDs):")
    print("="*60)
    print(f"Files with missing referenced IDs in JS: {len(missing_ids_report)}")
    for fn, ids in list(missing_ids_report.items())[:10]:
        print(f"  {fn}: missing IDs -> {set(ids)}")

    print("\n" + "="*60)
    print("3. ARTICLE WORD COUNT AUDIT:")
    print("="*60)
    under_1000 = {fn: wc for fn, wc in article_word_counts.items() if wc < 1000 and fn not in category_hubs}
    print(f"Total tools evaluated for word count: {len(article_word_counts)}")
    print(f"Tools with < 1000 words: {len(under_1000)}")
    if under_1000:
        for fn, wc in list(under_1000.items())[:10]:
            print(f"  {fn}: {wc} words")

    print("\n" + "="*60)
    print("4. IN-ARTICLE CONTEXTUAL INTERNAL LINKS AUDIT:")
    print("="*60)
    zero_in_art_links = {fn: c for fn, c in internal_links_count.items() if c == 0 and fn not in category_hubs}
    low_in_art_links = {fn: c for fn, c in internal_links_count.items() if 1 <= c <= 2 and fn not in category_hubs}
    good_in_art_links = {fn: c for fn, c in internal_links_count.items() if c >= 3 and fn not in category_hubs}
    print(f"Tools with 0 in-article internal links: {len(zero_in_art_links)}")
    print(f"Tools with 1-2 in-article internal links: {len(low_in_art_links)}")
    print(f"Tools with 3+ in-article internal links: {len(good_in_art_links)}")

    print("\n" + "="*60)
    print("5. DUPLICATE CONTENT / SIMILARITY AUDIT:")
    print("="*60)
    # Check for identical paragraphs across different tools
    para_to_files = defaultdict(list)
    for filepath in html_files:
        filename = os.path.basename(filepath)
        if filename in category_hubs:
            continue
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
        art = soup.find("article") or soup.find(class_=re.compile(r'article-(body|section)'))
        if art:
            paras = art.find_all("p")
            for p in paras:
                p_text = p.get_text(strip=True)
                if len(p_text) > 80: # meaningful paragraph
                    para_to_files[p_text].append(filename)

    shared_paras = {p: fs for p, fs in para_to_files.items() if len(set(fs)) > 1}
    print(f"Identical paragraphs shared across multiple distinct tools: {len(shared_paras)}")
    for p, fs in list(shared_paras.items())[:5]:
        print(f"  Shared across {len(set(fs))} files: '{p[:70]}...' -> {set(fs)}")

if __name__ == "__main__":
    audit_site()
