import re
import json

with open('index.html', encoding='utf-8') as f:
    content = f.read()

# Pattern for card
card_pattern = re.compile(
    r'<div class="directory-tool-card"[^>]*data-cat="([^"]*)"[^>]*data-search="([^"]*)"[^>]*>.*?'
    r'<span style="font-size:1\.5rem;">([^<]*)</span>.*?'
    r'<span [^>]*>([^<]*)</span>.*?'
    r'<h3 [^>]*><a href="([^"]*)"[^>]*>([^<]*)</a></h3>.*?'
    r'<p [^>]*>([^<]*)</p>.*?'
    r'<code [^>]*>([^<]*)</code>',
    re.S
)

matches = card_pattern.findall(content)
print(f"Regex matched: {len(matches)} cards out of 387")

tools_data = []
for m in matches:
    cat_data, search_data, icon, cat_label, url, title, desc, formula = m
    # Clean up url (strip .html)
    clean_url = url.replace('.html', '')
    tools_data.append({
        'c': cat_label.strip(),
        'i': icon.strip(),
        't': title.strip(),
        'u': clean_url.strip(),
        'd': desc.strip(),
        'f': formula.strip(),
        's': search_data.strip()
    })

print(f"Extracted {len(tools_data)} tools successfully.")
if tools_data:
    print("Sample tool 1:", tools_data[0])
    print("Sample tool 100:", tools_data[99] if len(tools_data) > 99 else None)

json_str = json.dumps(tools_data, ensure_ascii=False)
print(f"JSON size: {len(json_str.encode('utf-8')) / 1024:.1f} KB")
