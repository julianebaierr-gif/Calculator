import glob
import re
import os

def slugify(text):
    text = re.sub(r'<[^>]+>', '', text)
    # remove leading numbers like "1. ", "2. "
    text = re.sub(r'^\d+\.\s*', '', text)
    # clean symbols
    text = re.sub(r'[^a-zA-Z0-9\s-]', '', text).strip().lower()
    slug = re.sub(r'[\s_]+', '-', text)
    return slug[:50].strip('-')

files = glob.glob('*.html')
processed = 0

for f in files:
    if f in ['404.html', 'index.html', 'about.html', 'privacy.html', 'privacy-policy.html', 'terms.html', 'legal.html', 'contact.html', 'disclaimer.html']:
        continue
    
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
        
    if 'class="toc-container"' in content or "class='toc-container'" in content:
        continue
        
    # Find h2 headings in article / main content
    # Look for H2s
    h2_matches = list(re.finditer(r'<h2([^>]*)>(.*?)</h2>', content, re.I | re.S))
    if len(h2_matches) < 2:
        continue
        
    # Build list of items
    toc_items = []
    modified_content = content
    offset = 0
    
    # Process each H2 to ensure it has an id
    new_h2s = []
    used_slugs = set()
    
    for m in h2_matches:
        attrs = m.group(1)
        raw_title = m.group(2)
        clean_title = re.sub(r'<[^>]+>', '', raw_title).strip()
        
        # Check if already has id
        id_match = re.search(r'id=["\']([^"\']+)["\']', attrs)
        if id_match:
            slug = id_match.group(1)
        else:
            base_slug = slugify(clean_title) or 'section'
            slug = base_slug
            counter = 1
            while slug in used_slugs:
                slug = f"{base_slug}-{counter}"
                counter += 1
        used_slugs.add(slug)
        
        # Filter out footer/sidebar H2s like "Connected Solvers"
        if any(skip in clean_title.lower() for skip in ['connected', 'related tools', 'other calculators']):
            continue
            
        toc_items.append((slug, clean_title))
        
        # If H2 doesn't have an ID, inject it
        if not id_match:
            old_h2 = m.group(0)
            new_h2 = f'<h2 id="{slug}"{attrs}>{raw_title}</h2>'
            # Replace only this occurrence
            pos = modified_content.find(old_h2, offset)
            if pos != -1:
                modified_content = modified_content[:pos] + new_h2 + modified_content[pos + len(old_h2):]
                offset = pos + len(new_h2)
                
    if not toc_items:
        continue
        
    # Build the TOC HTML
    toc_html = '\n    <nav class="toc-container" aria-label="Table of Contents">\n'
    toc_html += '      <div class="toc-title">📑 Table of Contents</div>\n'
    toc_html += '      <ul class="toc-list">\n'
    for slug, title in toc_items:
        toc_html += f'        <li><a href="#{slug}">{title}</a></li>\n'
    toc_html += '      </ul>\n'
    toc_html += '    </nav>\n'
    
    # Find insertion point: right before the first H2 or right after geo-citation-box
    first_h2 = re.search(r'<h2[^>]*>', modified_content, re.I)
    if first_h2:
        idx = first_h2.start()
        # If there's an article-section before it, insert after <article...> or before first h2
        final_content = modified_content[:idx] + toc_html + '\n      ' + modified_content[idx:]
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(final_content)
        processed += 1

print(f"Successfully injected Table of Contents into {processed} calculator pages!")
