import glob
import os
import re

TARGET_DOMAIN = "https://www.fitcalchub.co.uk"
TARGET_HOST = "www.fitcalchub.co.uk"
BRAND_NAME = "FitCalcHub"

print("=" * 60)
print(f"MIGRATING SITE TO {TARGET_DOMAIN} ({BRAND_NAME})")
print("=" * 60)

html_files = glob.glob("*.html")
print(f"Found {len(html_files)} HTML files to update.")

updated_html_count = 0

for hf in html_files:
    with open(hf, "r", encoding="utf-8") as f:
        content = f.read()

    orig_content = content
    slug = hf.replace(".html", "")

    # 1. Canonical tag
    if hf == "404.html":
        # Remove canonical in 404
        content = re.sub(r'<link[^>]*rel=[\"\']canonical[\"\'][^>]*>\s*', '', content, flags=re.I)
        content = re.sub(r'<link[^>]*href=[\"\'][^\"\']*[\"\'][^>]*rel=[\"\']canonical[\"\'][^>]*>\s*', '', content, flags=re.I)
    else:
        canonical_href = f"{TARGET_DOMAIN}/" if hf == "index.html" else f"{TARGET_DOMAIN}/{slug}"
        canonical_tag = f'<link rel="canonical" href="{canonical_href}">'
        if re.search(r'<link[^>]*rel=[\"\']canonical[\"\'][^>]*>', content, re.I):
            content = re.sub(r'<link[^>]*rel=[\"\']canonical[\"\'][^>]*>', canonical_tag, content, count=1, flags=re.I)
        elif re.search(r'<link[^>]*href=[\"\'][^\"\']*[\"\'][^>]*rel=[\"\']canonical[\"\'][^>]*>', content, re.I):
            content = re.sub(r'<link[^>]*href=[\"\'][^\"\']*[\"\'][^>]*rel=[\"\']canonical[\"\'][^>]*>', canonical_tag, content, count=1, flags=re.I)

    # 2. OpenGraph URL & Images
    if hf != "404.html":
        og_url_tag = f'<meta property="og:url" content="{canonical_href}">'
        if re.search(r'<meta[^>]*property=[\"\']og:url[\"\'][^>]*>', content, re.I):
            content = re.sub(r'<meta[^>]*property=[\"\']og:url[\"\'][^>]*>', og_url_tag, content, count=1, flags=re.I)

    content = re.sub(r'<meta\s+property=[\"\']og:image[\"\']\s+content=[\"\']https?://[^\"\']+[\"\']', f'<meta property="og:image" content="{TARGET_DOMAIN}/og-image.png"', content, flags=re.I)
    content = re.sub(r'<meta\s+name=[\"\']twitter:image[\"\']\s+content=[\"\']https?://[^\"\']+[\"\']', f'<meta name="twitter:image" content="{TARGET_DOMAIN}/og-image.png"', content, flags=re.I)
    content = re.sub(r'<meta\s+property=[\"\']og:image:alt[\"\']\s+content=[\"\'][^\"\']*CalcHub[^\"\']*[\"\']', f'<meta property="og:image:alt" content="{BRAND_NAME} — Precision Standards-Compliant Calculators"', content, flags=re.I)

    # 3. Domain URL replacements in Schema and metadata
    # Replace all calchub.org, calchub.com, vercel.app occurrences in URLs
    content = re.sub(r'https?://(?:www\.)?calchub\.org/?', f'{TARGET_DOMAIN}/', content)
    content = re.sub(r'https?://(?:www\.)?calchub\.com/?', f'{TARGET_DOMAIN}/', content)
    content = re.sub(r'https?://calculator-omega-three-33\.vercel\.app/?', f'{TARGET_DOMAIN}/', content)
    # Fix double slashes if any created like https://www.fitcalchub.co.uk//
    content = content.replace(f'{TARGET_DOMAIN}//', f'{TARGET_DOMAIN}/')

    # Schema WebSite & Org IDs
    content = content.replace(f'{TARGET_DOMAIN}/#website', f'{TARGET_DOMAIN}/#website')
    content = content.replace(f'{TARGET_DOMAIN}/#org', f'{TARGET_DOMAIN}/#org')

    # 4. Brand Name updates
    # Logo in header & footer: <span>Calc<span class="accent">Hub</span></span> -> <span>FitCalc<span class="accent">Hub</span></span>
    content = content.replace('<span>Calc<span class="accent">Hub</span></span>', '<span>FitCalc<span class="accent">Hub</span></span>')
    content = content.replace('<span>CalcHub</span>', f'<span>{BRAND_NAME}</span>')

    # Apple mobile title
    content = re.sub(r'<meta\s+name=[\"\']apple-mobile-web-app-title[\"\']\s+content=[\"\'][^\"\']*[\"\']', f'<meta name="apple-mobile-web-app-title" content="{BRAND_NAME}">', content, flags=re.I)

    # Author meta tag
    content = re.sub(r'<meta\s+name=[\"\']author[\"\']\s+content=[\"\'][^\"\']*CalcHub[^\"\']*[\"\']', f'<meta name="author" content="{BRAND_NAME} Global Editorial Board"', content, flags=re.I)

    # Title replacements: "CalcHub" -> "FitCalcHub"
    def fix_title(match):
        t_content = match.group(1)
        t_content = t_content.replace('CalcHub', BRAND_NAME)
        return f'<title>{t_content}</title>'
    content = re.sub(r'<title>(.*?)</title>', fix_title, content, flags=re.S)

    # Email addresses in contact/privacy/legal
    content = content.replace('editorial@calchub.org', f'editorial@{TARGET_HOST.replace("www.", "")}')
    content = content.replace('privacy@calchub.org', f'privacy@{TARGET_HOST.replace("www.", "")}')
    content = content.replace('contact@calchub.org', f'contact@{TARGET_HOST.replace("www.", "")}')
    content = content.replace('corrections@calchub.org', f'corrections@{TARGET_HOST.replace("www.", "")}')
    content = content.replace('support@calchub.org', f'support@{TARGET_HOST.replace("www.", "")}')

    if content != orig_content:
        with open(hf, "w", encoding="utf-8") as f:
            f.write(content)
        updated_html_count += 1

print(f"[+] Updated {updated_html_count} HTML files.")

# --- 5. Update sitemap.xml ---
if os.path.exists("sitemap.xml"):
    with open("sitemap.xml", "r", encoding="utf-8") as f:
        sitemap = f.read()
    sitemap = re.sub(r'https?://(?:www\.)?calchub\.org/?', f'{TARGET_DOMAIN}/', sitemap)
    sitemap = re.sub(r'https?://(?:www\.)?calchub\.com/?', f'{TARGET_DOMAIN}/', sitemap)
    sitemap = sitemap.replace(f'{TARGET_DOMAIN}//', f'{TARGET_DOMAIN}/')
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap)
    print(f"[+] Updated sitemap.xml to {TARGET_DOMAIN}")

# --- 6. Update robots.txt ---
if os.path.exists("robots.txt"):
    with open("robots.txt", "r", encoding="utf-8") as f:
        rbt = f.read()
    rbt = re.sub(r'CALCHUB', f'{BRAND_NAME.upper()}', rbt)
    rbt = re.sub(r'Sitemap:\s*https?://[^\s]+', f'Sitemap: {TARGET_DOMAIN}/sitemap.xml', rbt)
    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(rbt)
    print(f"[+] Updated robots.txt with Sitemap: {TARGET_DOMAIN}/sitemap.xml")

# --- 7. Update llms.txt ---
if os.path.exists("llms.txt"):
    with open("llms.txt", "r", encoding="utf-8") as f:
        llms = f.read()
    llms = re.sub(r'https?://(?:www\.)?calchub\.org/?', f'{TARGET_DOMAIN}/', llms)
    llms = re.sub(r'https?://(?:www\.)?calchub\.com/?', f'{TARGET_DOMAIN}/', llms)
    llms = llms.replace('CalcHub', BRAND_NAME)
    llms = llms.replace(f'{TARGET_DOMAIN}//', f'{TARGET_DOMAIN}/')
    with open("llms.txt", "w", encoding="utf-8") as f:
        f.write(llms)
    print(f"[+] Updated llms.txt with {TARGET_DOMAIN} and {BRAND_NAME}")

# --- 8. Update site.webmanifest ---
if os.path.exists("site.webmanifest"):
    with open("site.webmanifest", "r", encoding="utf-8") as f:
        manifest = f.read()
    manifest = manifest.replace('"CalcHub', f'"{BRAND_NAME}')
    manifest = manifest.replace('"short_name": "CalcHub"', f'"short_name": "{BRAND_NAME}"')
    with open("site.webmanifest", "w", encoding="utf-8") as f:
        f.write(manifest)
    print(f"[+] Updated site.webmanifest with {BRAND_NAME}")

# --- 9. Update app.js ---
if os.path.exists("app.js"):
    with open("app.js", "r", encoding="utf-8") as f:
        app_code = f.read()
    app_code = app_code.replace("CalcHub", BRAND_NAME)
    app_code = app_code.replace("calchub.org", TARGET_HOST)
    with open("app.js", "w", encoding="utf-8") as f:
        f.write(app_code)
    print(f"[+] Updated app.js with {BRAND_NAME}")

# --- 10. Update ping_indexnow.py & indexnow key ---
INDEXNOW_KEY = "fitcalchub2026indexnowkey"
with open(f"{INDEXNOW_KEY}.txt", "w", encoding="utf-8") as f:
    f.write(INDEXNOW_KEY + "\n")
print(f"[+] Created IndexNow key file: {INDEXNOW_KEY}.txt")

if os.path.exists("ping_indexnow.py"):
    with open("ping_indexnow.py", "r", encoding="utf-8") as f:
        pinger = f.read()
    pinger = re.sub(r'SITE_HOST = "[^"]+"', f'SITE_HOST = "{TARGET_HOST}"', pinger)
    pinger = re.sub(r'INDEXNOW_KEY = "[^"]+"', f'INDEXNOW_KEY = "{INDEXNOW_KEY}"', pinger)
    pinger = pinger.replace("CalcHub", BRAND_NAME)
    pinger = pinger.replace("CALCHUB", BRAND_NAME.upper())
    with open("ping_indexnow.py", "w", encoding="utf-8") as f:
        f.write(pinger)
    print(f"[+] Updated ping_indexnow.py with {TARGET_HOST} and key {INDEXNOW_KEY}")

print("[SUCCESS] All files successfully configured for " + TARGET_DOMAIN)
