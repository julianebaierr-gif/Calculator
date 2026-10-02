import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

batch5_files = [
    'adc-dac-calculator.html',
    'antenna-length-calculator.html',
    'battery-short-circuit-current-calculator.html',
    'bjt-transistor-calculator.html',
    'breaker-size-calculator.html',
    'decibel-calculator.html',
    'earth-pit-resistance-calculator.html',
    'electrical-power-calculator.html'
]

old_pattern = """        <div>
          <h4>Standards &amp; Trust</h4>
          <ul class="footer-links">
            <li><a href="engineering-formulas.html">Engineering Formulas</a></li>
            <li><a href="about.html">About Calchub</a></li>
            <li><a href="privacy.html">Privacy Policy</a></li>
            <li><a href="terms.html">Terms of Service</a></li>
          </ul>
        </div>"""

new_pattern = """        <div>
          <h4>Standards &amp; Trust</h4>
          <ul class="footer-links">
            <li><a href="ohms-law-calculator.html">Ohm's Law Suite</a></li>
            <li><a href="engineering.html">Electrical Systems Hub</a></li>
            <li><a href="sitemap.xml">XML Sitemap</a></li>
            <li><a href="index.html">All Calculators</a></li>
          </ul>
        </div>"""

for fn in batch5_files:
    fpath = os.path.join(BASE_DIR, fn)
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            c = f.read()
        if old_pattern in c:
            c = c.replace(old_pattern, new_pattern)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(c)
            print(f"Fixed footer in {fn}")
        else:
            print(f"Pattern not found in {fn}")

# Also update the generator scripts so re-running them never reintroduces the broken links
for script_fn in ["gen_batch5_part1.py", "gen_batch5_part2.py", "gen_batch5_part3.py", "gen_batch5_part4.py"]:
    sp = os.path.join(BASE_DIR, "scripts", script_fn)
    if os.path.exists(sp):
        with open(sp, "r", encoding="utf-8") as f:
            sc = f.read()
        if old_pattern in sc:
            sc = sc.replace(old_pattern, new_pattern)
            with open(sp, "w", encoding="utf-8") as f:
                f.write(sc)
            print(f"Updated template in scripts/{script_fn}")
