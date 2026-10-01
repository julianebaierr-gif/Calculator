import os
import re
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from enrich_tools_data import TOOLS_DATA
from enrich_tools_data2 import ADDITIONAL_DATA
from enrich_tools_data3 import THIRD_BATCH_DATA

ALL_TOOLS = {}
ALL_TOOLS.update(TOOLS_DATA)
ALL_TOOLS.update(ADDITIONAL_DATA)
ALL_TOOLS.update(THIRD_BATCH_DATA)

print(f"Total tools to enrich: {len(ALL_TOOLS)}")

def build_standards_box(data):
    std_items_html = "".join([
        f'<div class="standards-item"><strong>{title}</strong><span>{desc}</span></div>'
        for title, desc in data["standards"]
    ])
    return f'''
      <div class="standards-verification-box">
        <div class="standards-verification-header">
          <span class="standards-badge-title">🛡️ Standards &amp; Methodology Verification</span>
          <span class="worked-example-badge">E-E-A-T Verified: {data["verification"]}</span>
        </div>
        <div class="standards-grid">
          {std_items_html}
        </div>
      </div>
    '''

def build_worked_example_card(data):
    steps_html = ""
    for title, formula, desc in data["steps"]:
        formula_render = f'\\[ {formula} \\]' if formula else ''
        steps_html += f'''
          <div class="calc-step-item">
            <div class="calc-step-title">{title}</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              {formula_render}
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">{desc}</p>
          </div>
        '''

    return f'''
      <div class="worked-example-card">
        <div class="worked-example-header">
          <h3 class="worked-example-title">📐 {data["example_title"]}</h3>
          <span class="worked-example-badge">{data["example_badge"]}</span>
        </div>
        <div class="step-calculation-list">
          {steps_html}
        </div>
        <div class="calc-final-result">
          ✅ <strong>Verified Engineering Outcome:</strong> {data["final_result"]}
        </div>
      </div>
    '''

def build_faqs_html(data):
    faqs_html = ""
    for q, a in data["faqs"]:
        faqs_html += f'''
        <div class="faq-item">
          <div class="faq-q">{q}</div>
          <div class="faq-a">{a}</div>
        </div>
        '''
    return f'''
      <div class="faq-container" style="margin-top:2.5rem;">
        <h3 style="margin-bottom:1.5rem;">Frequently Asked Questions</h3>
        {faqs_html}
      </div>
    '''

def update_tool_schema(html_content, faqs):
    main_entity = []
    for q, a in faqs:
        clean_a = re.sub(r'<[^>]+>', '', a)
        main_entity.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": clean_a
            }
        })
    
    faq_schema = {
        "@type": "FAQPage",
        "mainEntity": main_entity
    }

    script_pattern = re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)', re.DOTALL)
    match = script_pattern.search(html_content)
    if match:
        script_body = match.group(2)
        try:
            parsed = json.loads(script_body)
            if "@graph" in parsed:
                new_graph = []
                for item in parsed["@graph"]:
                    if item.get("@type") != "FAQPage":
                        new_graph.append(item)
                new_graph.append(faq_schema)
                parsed["@graph"] = new_graph
                new_json = json.dumps(parsed, indent=2)
                return script_pattern.sub(lambda m: f'{m.group(1)}\n{new_json}\n{m.group(3)}', html_content, count=1)
        except Exception as e:
            print(f"Error parsing JSON-LD: {e}")
    return html_content

def enrich_tool_file(filename, data):
    filepath = os.path.join(BASE_DIR, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filename}")
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    standards_box = build_standards_box(data)
    worked_example = build_worked_example_card(data)
    faqs_html = build_faqs_html(data)

    article_match = re.search(r'(<article class="article-section">)(.*?)(</article>)', content, re.DOTALL)
    if not article_match:
        print(f"Warning: Article tag not found in {filename}")
        return False

    article_start, article_body, article_end = article_match.group(1), article_match.group(2), article_match.group(3)

    # Check if this article has the 4 numbered sections format (newer 25 tools)
    if "<h3>4. Worked Real-World Engineering Example</h3>" in article_body or "<h3>4. Worked Real-World Practical Example</h3>" in article_body or "<h3>4. Worked Real-World Clinical Example</h3>" in article_body or "<h3>4. Worked Real-World Financial Example</h3>" in article_body or "<h3>4. Worked Real-World Mathematical Example</h3>" in article_body:
        # 1. Insert standards box right after article-summary-box
        summary_box_match = re.search(r'(<div class="article-summary-box">.*?</div>)', article_body, re.DOTALL)
        if summary_box_match:
            new_body = article_body.replace(summary_box_match.group(1), summary_box_match.group(1) + "\n" + standards_box, 1)
        else:
            header_match = re.search(r'(<div class="article-header">.*?</div>)', article_body, re.DOTALL)
            if header_match:
                new_body = article_body.replace(header_match.group(1), header_match.group(1) + "\n" + standards_box, 1)
            else:
                new_body = standards_box + "\n" + article_body

        # 2. Replace section 4 and everything up to faq-container with worked example card
        sec4_pattern = re.compile(r'<h3>4\.\s*Worked Real-World.*?</p>', re.DOTALL)
        if sec4_pattern.search(new_body):
            new_body = sec4_pattern.sub(lambda m: worked_example, new_body, count=1)

        # 3. Replace faq-container with new faqs_html
        faq_pattern = re.compile(r'<div class="faq-container".*?</div>\s*(?=$|\s*</article>)', re.DOTALL)
        if faq_pattern.search(new_body):
            new_body = faq_pattern.sub(lambda m: faqs_html, new_body, count=1)
        else:
            new_body = new_body + "\n" + faqs_html

    else:
        # Older 8 tools (cable-sizing, voltage-drop, ohms-law, etc.)
        # 1. Prepend standards box
        new_body = standards_box + "\n" + article_body

        # 2. Find where the worked example can be cleanly placed or replace/insert
        # Look for FAQs header: <h2 id=".*?-faq"> or <div class="faq-wrap">
        faq_match = re.search(r'(<h2 id="[a-z0-9_-]+faq".*?)(?=$|\s*</article>)', new_body, re.DOTALL)
        if faq_match:
            # Insert worked example right before FAQs
            new_body = new_body.replace(faq_match.group(1), worked_example + "\n" + faqs_html, 1)
        else:
            faq_wrap_match = re.search(r'(<div class="faq-wrap".*?</div>)', new_body, re.DOTALL)
            if faq_wrap_match:
                new_body = new_body.replace(faq_wrap_match.group(1), worked_example + "\n" + faqs_html, 1)
            else:
                new_body = new_body + "\n" + worked_example + "\n" + faqs_html

    updated_content = content[:article_match.start(2)] + new_body + content[article_match.end(2):]

    # Update schema
    updated_content = update_tool_schema(updated_content, data["faqs"])

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print(f"Successfully enriched tool: {filename}")
    return True

if __name__ == "__main__":
    count = 0
    for fname, d in ALL_TOOLS.items():
        if enrich_tool_file(fname, d):
            count += 1
    print(f"\nCompleted enrichment of {count} tools!")
