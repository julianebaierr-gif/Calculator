import glob
import json
import re

html_files = glob.glob('*.html')
errors = 0
empty = 0

for f in html_files:
    c = open(f, encoding='utf-8', errors='ignore').read()
    matches = re.findall(r'<script\b[^>]*type=[\"\']application/ld\+json[\"\'][^>]*>(.*?)</script>', c, re.S)
    for idx, s in enumerate(matches):
        s_clean = s.strip()
        if not s_clean:
            print(f"Empty JSON-LD in {f}")
            empty += 1
        else:
            try:
                json.loads(s_clean)
            except Exception as e:
                print(f"JSON-LD error in {f} (# {idx}): {e}")
                errors += 1

print(f"Audit finished. Total files: {len(html_files)}, Errors: {errors}, Empty: {empty}")
