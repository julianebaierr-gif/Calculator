import glob
import os
import re

def main():
    html_files = glob.glob('*.html')
    print(f"Validating {len(html_files)} HTML files...")
    errors = 0

    all_slugs = {f.replace('.html', '') for f in html_files}
    all_slugs.add('')  # root '/'

    for f in html_files:
        with open(f, 'r', encoding='utf-8') as fh:
            c = fh.read()
        if not c.startswith('<!DOCTYPE html>'):
            print(f"Error: {f} missing doctype")
            errors += 1
        if '</html>' not in c:
            print(f"Error: {f} missing closing html tag")
            errors += 1

        # Strip <script>...</script> before checking HTML href links
        html_only = re.sub(r'<script\b[^>]*>.*?</script>', '', c, flags=re.S)

        # Check internal links
        hrefs = re.findall(r'href=[\'"]([^\'":#\s]+)(?:#[^\'"]*)?[\'"]', html_only)
        for h in hrefs:
            if h.startswith('http') or h.startswith('mailto:') or h.startswith('tel:') or h.startswith('#') or h.startswith('javascript:'):
                continue
            if '${' in h:
                continue
            
            clean_target = h.strip('/')
            known_assets = {'sitemap.xml', 'styles.css', 'favicon.ico', 'favicon.svg', 'apple-touch-icon.png', 'site.webmanifest', 'logo.png', 'og-image.png'}
            if clean_target == '' or clean_target in known_assets:
                continue
            
            target_file = clean_target if clean_target.endswith('.html') else f"{clean_target}.html"
            if not os.path.exists(target_file):
                print(f"Broken link in {f}: {h} (Target not found: {target_file})")
                errors += 1

    if errors == 0:
        print(f"SUCCESS: All {len(html_files)} HTML files and internal links are 100% valid with ZERO broken links!")
    else:
        print(f"Found {errors} errors.")

if __name__ == '__main__':
    main()
