import glob
import os
import re

html_files = glob.glob('*.html')
all_slugs = {f.replace('.html', '') for f in html_files}
print(f"Total HTML files to process: {len(html_files)}")

FAVICON_TAGS = '''  <link rel="icon" type="image/x-icon" href="/favicon.ico">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">'''

NEW_FOOTER_BOTTOM_LINKS = '''<div class="footer-bottom-links">
                    <a href="/sitemap.xml">Sitemap</a>
                    <a href="/about">About Us</a>
                    <a href="/privacy-policy">Privacy Policy</a>
                    <a href="/terms">Terms of Service</a>
                    <a href="/disclaimer">Disclaimers</a>
                    <a href="/contact">Contact Us</a>
                </div>'''

modified_count = 0

for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()

    orig_content = content
    slug = hf.replace('.html', '')

    # --- 1. Robots Meta Tag ---
    if hf == '404.html':
        robots_tag = '<meta name="robots" content="noindex, follow">'
    else:
        robots_tag = '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">'

    if re.search(r'<meta[^>]*name=[\"\']robots[\"\'][^>]*>', content, re.I):
        content = re.sub(r'<meta[^>]*name=[\"\']robots[\"\'][^>]*>', robots_tag, content, count=1, flags=re.I)
    else:
        # Insert after viewport or after <head>
        if re.search(r'(<meta[^>]*name=[\"\']viewport[\"\'][^>]*>)', content, re.I):
            content = re.sub(r'(<meta[^>]*name=[\"\']viewport[\"\'][^>]*>)', r'\1\n  ' + robots_tag, content, count=1, flags=re.I)
        elif '<head>' in content:
            content = content.replace('<head>', f'<head>\n  {robots_tag}', 1)

    # --- 2. Canonical Tag ---
    if hf == '404.html':
        # Remove any canonical in 404
        content = re.sub(r'<link[^>]*rel=[\"\']canonical[\"\'][^>]*>\s*', '', content, flags=re.I)
        content = re.sub(r'<link[^>]*href=[\"\'][^\"\']*[\"\'][^>]*rel=[\"\']canonical[\"\'][^>]*>\s*', '', content, flags=re.I)
    else:
        canonical_href = "https://calchub.org/" if hf == "index.html" else f"https://calchub.org/{slug}"
        canonical_tag = f'<link rel="canonical" href="{canonical_href}">'

        # Check if canonical tag exists
        if re.search(r'<link[^>]*rel=[\"\']canonical[\"\'][^>]*>', content, re.I) or re.search(r'<link[^>]*href=[\"\'][^\"\']*[\"\'][^>]*rel=[\"\']canonical[\"\'][^>]*>', content, re.I):
            content = re.sub(r'<link[^>]*rel=[\"\']canonical[\"\'][^>]*>', canonical_tag, content, count=1, flags=re.I)
            content = re.sub(r'<link[^>]*href=[\"\'][^\"\']*[\"\'][^>]*rel=[\"\']canonical[\"\'][^>]*>', canonical_tag, content, count=1, flags=re.I)
        else:
            # Insert after robots tag or before </head>
            if robots_tag in content:
                content = content.replace(robots_tag, f'{robots_tag}\n  {canonical_tag}', 1)
            elif '</head>' in content:
                content = content.replace('</head>', f'  {canonical_tag}\n</head>', 1)

    # --- 3. OpenGraph URL ---
    if hf != '404.html':
        og_url_tag = f'<meta property="og:url" content="{canonical_href}">'
        if re.search(r'<meta[^>]*property=[\"\']og:url[\"\'][^>]*>', content, re.I):
            content = re.sub(r'<meta[^>]*property=[\"\']og:url[\"\'][^>]*>', og_url_tag, content, count=1, flags=re.I)

    # --- 4. Favicon Tags ---
    # Check if favicon is in head
    if not re.search(r'<link[^>]*rel=[\"\'](?:shortcut )?icon[\"\']', content, re.I):
        if hf != '404.html' and canonical_tag in content:
            content = content.replace(canonical_tag, f'{canonical_tag}\n{FAVICON_TAGS}', 1)
        elif '</head>' in content:
            content = content.replace('</head>', f'{FAVICON_TAGS}\n</head>', 1)

    # --- 5. Footer Bottom Links ---
    if re.search(r'<div class=[\"\']footer-bottom-links[\"\']>.*?</div>', content, re.S):
        content = re.sub(r'<div class=[\"\']footer-bottom-links[\"\']>.*?</div>', NEW_FOOTER_BOTTOM_LINKS, content, count=1, flags=re.S)

    # --- 6. Footer and Header Internal Links Clean Up ---
    # In footer brand: href="index.html" -> href="/"
    content = re.sub(r'(<footer[^>]*>.*?<a\s+href=[\"\'])index\.html([\"\'#])', r'\1/\2', content, flags=re.S)
    # In header brand: href="index.html" -> href="/"
    content = re.sub(r'(<header[^>]*>.*?<a\s+href=[\"\'])index\.html([\"\'#])', r'\1/\2', content, flags=re.S)

    # Replace <a href="index.html"> throughout with <a href="/">
    content = re.sub(r'href=[\"\']index\.html([\"\'#])', r'href="/\1', content)

    # Clean internal tool links: href="slug.html" -> href="/slug"
    def replace_tool_href(match):
        target = match.group(1)
        suffix = match.group(2) or ''
        quote = match.group(0)[-1]  # closing quote
        if target in all_slugs:
            if target == 'index':
                return f'href="/{suffix}"'
            return f'href="/{target}{suffix}"'
        return match.group(0)

    content = re.sub(r'href=[\"\']([a-zA-Z0-9_\-]+)\.html([#\?][^\"\']*)?[\"\']', replace_tool_href, content)

    # In sidebar-pool-data: "slug": "slug.html" -> "slug": "/slug"
    def replace_pool_slug(match):
        slug_target = match.group(1)
        if slug_target in all_slugs:
            return f'"slug": "/{slug_target}"'
        return match.group(0)

    content = re.sub(r'\"slug\":\s*\"([a-zA-Z0-9_\-]+)\.html\"', replace_pool_slug, content)

    # Update rotateSidebarTools JS to handle clean URLs robustly if present
    old_sidebar_find = "const currentPath = window.location.pathname.split('/').pop() || '';"
    new_sidebar_find = "const currentPath = (window.location.pathname.split('/').pop() || '').replace(/\\.html$/, '');"
    if old_sidebar_find in content:
        content = content.replace(old_sidebar_find, new_sidebar_find)

    old_filter = "const available = pool.filter(item => item.slug !== currentPath);"
    new_filter = "const available = pool.filter(item => (item.slug || '').replace(/^\\//, '').replace(/\\.html$/, '') !== currentPath);"
    if old_filter in content:
        content = content.replace(old_filter, new_filter)

    if content != orig_content:
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(content)
        modified_count += 1

print(f"Standardized {modified_count} HTML files successfully.")
