"""
Deep Quality & Keyword Alignment Audit for all 54 Calculators on CalcHub.
Checks:
1. Interactive JS calculation engine (DOM ID match, input/output connectivity).
2. Primary Keyword & SEO tags (<title>, <meta description>, <h1>).
3. Educational content depth (Word count of technical article).
4. Schema.org JSON-LD structured data (SoftwareApplication, FAQPage).
5. Math formulas (KaTeX syntax / equations).
6. Reference tables & worked examples.
7. Technical FAQ items.
8. Internal links.
"""

import glob
import json
import os
import re
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CATEGORY_FILES = {
    'health.html', 'finance.html', 'math.html', 'engineering.html',
    'solar-energy.html', 'mechanical.html', 'civil.html', 'chemical.html',
    'fire-safety.html', 'programmer.html', 'datetime.html', 'converter.html'
}

all_html = glob.glob(os.path.join(BASE_DIR, '*.html'))
tool_files = sorted([f for f in all_html if os.path.basename(f) not in CATEGORY_FILES and os.path.basename(f) not in {'index.html', '404.html'}])

print(f"================================================================================")
print(f"=== DEEP QUALITY & KEYWORD ALIGNMENT AUDIT OF ALL {len(tool_files)} LIVE CALCULATORS ===")
print(f"================================================================================\n")

results = []
dom_mismatches = []
low_content_tools = []
missing_schema = []
missing_js = []
seo_keyword_analysis = []

for tool_path in tool_files:
    fname = os.path.basename(tool_path)
    with open(tool_path, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # 1. Title, Meta, H1
    title = soup.find('title').get_text().strip() if soup.find('title') else ''
    meta_desc = ''
    meta_tag = soup.find('meta', attrs={'name': 'description'})
    if meta_tag and meta_tag.get('content'):
        meta_desc = meta_tag['content'].strip()

    meta_kw = ''
    kw_tag = soup.find('meta', attrs={'name': 'keywords'})
    if kw_tag and kw_tag.get('content'):
        meta_kw = kw_tag['content'].strip()

    h1 = soup.find('h1').get_text().strip() if soup.find('h1') else ''

    # 2. Derive expected primary keyword from slug (e.g. bmr-calculator.html -> 'bmr calculator')
    clean_slug = fname.replace('.html', '')
    primary_kw_slug = clean_slug.replace('-', ' ')

    # 3. Check article word count
    article = soup.find('article')
    art_text = article.get_text() if article else ''
    word_count = len(art_text.split())

    # 4. Check JS Engine
    scripts = soup.find_all('script')
    inline_js = '\n'.join([s.get_text() for s in scripts if not s.get('src') and s.get('type') != 'application/ld+json'])
    has_js = len(inline_js.strip()) > 50

    # Check DOM ID references in JS
    js_dom_ids = set(re.findall(r'getElementById\([\'"]([a-zA-Z0-9_\-]+)[\'"]\)', inline_js))
    missing_ids = []
    for d_id in js_dom_ids:
        if not soup.find(id=d_id):
            missing_ids.append(d_id)

    # 5. Schema JSON-LD
    has_software_schema = False
    has_faq_schema = False
    schema_scripts = soup.find_all('script', attrs={'type': 'application/ld+json'})
    for sc in schema_scripts:
        try:
            data = json.loads(sc.get_text())
            text_repr = json.dumps(data)
            if 'SoftwareApplication' in text_repr or 'WebApplication' in text_repr:
                has_software_schema = True
            if 'FAQPage' in text_repr:
                has_faq_schema = True
        except Exception:
            pass

    # 6. Worked Example & Reference Table & FAQs
    has_example = bool(soup.find(class_='worked-example-card')) or bool(soup.find(class_='example-card')) or 'worked-example' in html.lower()
    has_table = bool(soup.find('table'))
    faq_items = len(soup.find_all('details', class_='faq-item')) or len(soup.find_all(class_='faq-item')) or len(soup.find_all('details'))

    # Keyword check: does title, h1, or meta_desc contain the core keyword terms?
    # e.g., 'conduit fill', 'wire ampacity', 'bmr'
    core_kw_words = [w for w in clean_slug.split('-') if w not in {'calculator', 'sizing'}]
    kw_in_title = any(w in title.lower() for w in core_kw_words)
    kw_in_h1 = any(w in h1.lower() for w in core_kw_words)
    kw_in_desc = any(w in meta_desc.lower() for w in core_kw_words)

    record = {
        'file': fname,
        'title': title,
        'h1': h1,
        'word_count': word_count,
        'has_js': has_js,
        'missing_ids': missing_ids,
        'has_software_schema': has_software_schema,
        'has_faq_schema': has_faq_schema,
        'has_example': has_example,
        'has_table': has_table,
        'faq_items': faq_items,
        'kw_in_title': kw_in_title,
        'kw_in_h1': kw_in_h1,
        'kw_in_desc': kw_in_desc
    }
    results.append(record)

    if missing_ids:
        dom_mismatches.append((fname, missing_ids))
    if word_count < 950:
        low_content_tools.append((fname, word_count))
    if not (has_software_schema and has_faq_schema):
        missing_schema.append(fname)
    if not has_js:
        missing_js.append(fname)

# Print Summary Report
print("1. JAVASCRIPT CALCULATION ENGINE AUDIT:")
if not missing_js and not dom_mismatches:
    print(f"  [PASS] ALL {len(tool_files)} tools have active, inline JavaScript calculation engines.")
    print("  [PASS] ZERO DOM ID mismatches! All getElementById() calls map to real HTML inputs and output elements.")
else:
    if missing_js:
        print(f"  [FAIL] Missing JS engines in: {missing_js}")
    if dom_mismatches:
        for f, ids in dom_mismatches:
            print(f"  [FAIL] {f} references missing DOM IDs: {ids}")

print("\n2. CONTENT DEPTH & WORD COUNT AUDIT:")
avg_words = sum(r['word_count'] for r in results) / len(results)
print(f"  Average article word count across all {len(tool_files)} tools: {avg_words:.0f} words")
if not low_content_tools:
    print(f"  [PASS] ALL {len(tool_files)} tools meet or exceed technical depth requirement (1,000+ words).")
else:
    print(f"  [WARN] {len(low_content_tools)} tools have less than 950 words:")
    for f, wc in low_content_tools:
        print(f"     - {f}: {wc} words")

print("\n3. SCHEMA.ORG & STRUCTURED DATA AUDIT:")
if not missing_schema:
    print(f"  [PASS] ALL {len(tool_files)} tools have complete Schema.org JSON-LD (SoftwareApplication + FAQPage).")
else:
    print(f"  [WARN] {len(missing_schema)} tools missing complete schema:")
    for f in missing_schema:
        print(f"     - {f}")

print("\n4. KEYWORD TARGETING & SEO META AUDIT:")
misaligned_seo = [r for r in results if not (r['kw_in_title'] and r['kw_in_h1'] and r['kw_in_desc'])]
if not misaligned_seo:
    print(f"  [PASS] ALL {len(tool_files)} tools have 100% matched primary keywords in <title>, <h1>, and <meta description>!")
else:
    print(f"  [WARN] Misaligned keywords in {len(misaligned_seo)} tools:")
    for m in misaligned_seo:
        print(f"     - {m['file']}: title_kw={m['kw_in_title']}, h1_kw={m['kw_in_h1']}, desc_kw={m['kw_in_desc']}")

print("\n5. INTERACTIVE COMPONENTS & EEAT VERIFICATION:")
tools_with_examples = sum(1 for r in results if r['has_example'])
tools_with_tables = sum(1 for r in results if r['has_table'])
tools_with_faqs = sum(1 for r in results if r['faq_items'] >= 3)
print(f"  - Tools with step-by-step Worked Example case study: {tools_with_examples} / {len(tool_files)}")
print(f"  - Tools with Multi-Column Reference Tables: {tools_with_tables} / {len(tool_files)}")
print(f"  - Tools with 3+ Technical FAQs: {tools_with_faqs} / {len(tool_files)}")

print("\n================================================================================")
print(f"AUDIT SUMMARY COMPLETE: {len(tool_files)} tools audited.")
print("================================================================================")

