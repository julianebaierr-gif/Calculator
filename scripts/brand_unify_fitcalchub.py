import glob
import os
import re

print("=" * 60)
print("UNIFYING BRAND TO FitCalcHub & DOMAIN TO www.fitcalchub.co.uk")
print("=" * 60)

files_to_check = (
    glob.glob("*.html") +
    glob.glob("*.xml") +
    glob.glob("*.txt") +
    glob.glob("*.json") +
    glob.glob("*.js") +
    ["scripts/ping_indexnow.py", "scripts/validate_site.py"]
)

updated_files = 0

for file_path in files_to_check:
    if not os.path.isfile(file_path):
        continue

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    orig = content

    # 1. Clean domain URLs
    content = re.sub(r'https?://(?:www\.)?calchub\.org/?', 'https://www.fitcalchub.co.uk/', content)
    content = re.sub(r'https?://(?:www\.)?calchub\.com/?', 'https://www.fitcalchub.co.uk/', content)
    content = re.sub(r'https?://calculator-omega-three-33\.vercel\.app/?', 'https://www.fitcalchub.co.uk/', content)
    content = content.replace('https://www.fitcalchub.co.uk//', 'https://www.fitcalchub.co.uk/')

    # 2. Plain domain mentions
    content = re.sub(r'(?<!fit)calchub\.org', 'fitcalchub.co.uk', content)
    content = re.sub(r'(?<!fit)calchub\.com', 'fitcalchub.co.uk', content)

    # 3. Email addresses
    content = re.sub(r'[a-zA-Z0-9.-]+@calchub\.[a-z]+', lambda m: m.group(0).split('@')[0] + '@fitcalchub.co.uk', content)

    # 4. Brand Name: CalcHub -> FitCalcHub (avoiding double 'Fit')
    content = re.sub(r'(?<![Ff]it)CalcHub', 'FitCalcHub', content)
    content = re.sub(r'(?<![Ff]IT)CALCHUB', 'FITCALCHUB', content)

    # 5. Fix logo markup if double Fit occurred or needs clean markup
    content = content.replace('FitFitCalc<span class="accent">Hub</span>', 'FitCalc<span class="accent">Hub</span>')
    content = content.replace('<span>Calc<span class="accent">Hub</span></span>', '<span>FitCalc<span class="accent">Hub</span></span>')

    if content != orig:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        updated_files += 1

print(f"[SUCCESS] Updated {updated_files} files with 100% unified FitCalcHub branding.")
