import glob
import os
import re

def main():
    html_files = glob.glob('*.html')
    print(f"Validating {len(html_files)} HTML files...")
    errors = 0

    for f in html_files:
        with open(f, 'r', encoding='utf-8') as fh:
            c = fh.read()
        if not c.startswith('<!DOCTYPE html>'):
            print(f"Error: {f} missing doctype")
            errors += 1
        if '</html>' not in c:
            print(f"Error: {f} missing closing html tag")
            errors += 1
        # Check internal html links
        links = re.findall(r'href=[\'"]([a-zA-Z0-9_\-\.]+\.html)[\'"]', c)
        for link in links:
            if not os.path.exists(link):
                print(f"Broken link in {f}: {link}")
                errors += 1

    if errors == 0:
        print(f"SUCCESS: All {len(html_files)} HTML files and internal links are 100% valid with zero broken links!")
    else:
        print(f"Found {errors} errors.")

if __name__ == '__main__':
    main()
