import glob
import re
import os

html_files = glob.glob('*.html')
print(f"Applying advanced fixes to {len(html_files)} HTML files...")

KATEX_HEAD = '''  <!-- KaTeX Math Rendering Support -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\\\[', right: '\\\\]', display: true}, {left: '\\\\(', right: '\\\\)', display: false}], throwOnError: false});"></script>'''

OG_IMAGE_TAGS = '''  <!-- Open Graph & Social Sharing Previews -->
  <meta property="og:image" content="https://calchub.org/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="CalcHub — Precision Standards-Compliant Calculators">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://calchub.org/og-image.png">'''

modified_files = 0
alerts_replaced = 0

for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()
    orig = content

    # 1. KaTeX check & normalization
    if 'katex.min.js' not in content:
        # Insert before </head>
        if '</head>' in content:
            content = content.replace('</head>', f'{KATEX_HEAD}\n</head>', 1)
    else:
        # Normalize the auto-render call to include delimiters and throwOnError: false
        old_katex = re.findall(r'<script[^>]*auto-render\.min\.js[^>]*>.*?</script>', content)
        if old_katex:
            new_auto_render = '<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body, {delimiters: [{left: \'$$\', right: \'$$\', display: true}, {left: \'\\\\[\', right: \'\\\\]\', display: true}, {left: \'\\\\(\', right: \'\\\\)\', display: false}], throwOnError: false});"></script>'
            content = content.replace(old_katex[0], new_auto_render)

    # 2. OpenGraph Image & Twitter Cards
    if 'og:image' not in content:
        # Insert right after og:url or og:type or before </head>
        if '<meta property="og:url"' in content:
            content = re.sub(r'(<meta property=[\"\']og:url[\"\'][^>]*>)', r'\1\n' + OG_IMAGE_TAGS, content, count=1)
        elif '</head>' in content:
            content = content.replace('</head>', f'{OG_IMAGE_TAGS}\n</head>', 1)

    # 3. Keyword Cannibalization: Canonical Consolidation for alias pages
    if hf == '3-phase-power-calculator.html':
        content = re.sub(r'<link[^>]*rel=[\"\']canonical[\"\'][^>]*>', '<link rel="canonical" href="https://calchub.org/three-phase-power-calculator">', content)
    elif hf == 'waist-to-height-ratio-calculator.html':
        content = re.sub(r'<link[^>]*rel=[\"\']canonical[\"\'][^>]*>', '<link rel="canonical" href="https://calchub.org/waist-to-height-calculator">', content)
    elif hf == 'fire-sprinkler-calculator.html':
        content = re.sub(r'<link[^>]*rel=[\"\']canonical[\"\'][^>]*>', '<link rel="canonical" href="https://calchub.org/fire-sprinkler-hydraulic-calculator">', content)
    elif hf == 'privacy.html':
        content = re.sub(r'<link[^>]*rel=[\"\']canonical[\"\'][^>]*>', '<link rel="canonical" href="https://calchub.org/privacy-policy">', content)
    elif hf == 'legal.html':
        content = re.sub(r'<link[^>]*rel=[\"\']canonical[\"\'][^>]*>', '<link rel="canonical" href="https://calchub.org/terms">', content)

    # 4. Standard differentiation for Cable Sizing NEC vs IEC
    if hf == 'cable-sizing-calculator-nec.html':
        content = re.sub(r'<title>.*?</title>', '<title>US NEC Cable Sizing Calculator — NFPA 70 Wire Ampacity | CalcHub</title>', content, count=1, flags=re.I)
    elif hf == 'cable-sizing-calculator.html':
        content = re.sub(r'<title>.*?</title>', '<title>IEC &amp; BS 7671 Cable Sizing Calculator — Conductor Ampacity | CalcHub</title>', content, count=1, flags=re.I)

    # 5. Replace native alert() calls in inline JS
    # Replace alert(...) with window.showToast(...)
    alert_matches = len(re.findall(r'(?<![a-zA-Z0-9_\.])alert\s*\(', content))
    if alert_matches > 0:
        content = re.sub(r'(?<![a-zA-Z0-9_\.])alert\s*\(', 'window.showToast(', content)
        alerts_replaced += alert_matches

    if content != orig:
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(content)
        modified_files += 1

print(f"Advanced fixes applied: {modified_files} files modified, {alerts_replaced} alert() calls replaced with non-blocking toast.")
