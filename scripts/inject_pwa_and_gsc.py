import glob
import re

html_files = glob.glob('*.html')
print(f"Injecting PWA manifest and mobile theme tags across {len(html_files)} HTML files...")

PWA_TAGS = '''  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#2563EB">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="default">
  <meta name="apple-mobile-web-app-title" content="CalcHub">'''

GSC_TAG = '  <meta name="google-site-verification" content="GSC_VERIFICATION_TOKEN_REPLACE_ME">'

modified_count = 0

for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content

    # 1. PWA Manifest & Theme Color
    if 'site.webmanifest' not in content:
        if '<link rel="apple-touch-icon"' in content:
            content = re.sub(r'(<link rel=[\"\']apple-touch-icon[\"\'][^>]*>)', r'\1\n' + PWA_TAGS, content, count=1)
        elif '</head>' in content:
            content = content.replace('</head>', f'{PWA_TAGS}\n</head>', 1)

    # 2. Google Site Verification Tag on index.html
    if hf == 'index.html':
        if 'google-site-verification' not in content:
            if '<meta name="robots"' in content:
                content = re.sub(r'(<meta name=[\"\']robots[\"\'][^>]*>)', r'\1\n' + GSC_TAG, content, count=1)
            elif '</head>' in content:
                content = content.replace('</head>', f'{GSC_TAG}\n</head>', 1)

    if content != orig:
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(content)
        modified_count += 1

print(f"Successfully updated {modified_count} HTML files with PWA and verification meta tags.")
