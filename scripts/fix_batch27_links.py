import os
import glob

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BATCH_FILES = [
    'gcd-lcm-calculator.html',
    'quadratic-equation-calculator.html',
    'pythagorean-theorem-calculator.html',
    'scientific-notation-calculator.html',
    'significant-figures-calculator.html',
    'prime-number-calculator.html'
]

FOOTER_OLD = """      <div class="footer-col">
        <h4>Legal</h4>
        <ul>
          <li><a href="privacy.html">Privacy Policy</a></li>
          <li><a href="terms.html">Terms of Service</a></li>
        </ul>
      </div>"""

FOOTER_NEW = """      <div class="footer-col">
        <h4>Hub Categories</h4>
        <ul>
          <li><a href="converter.html">Unit Converters</a></li>
          <li><a href="engineering.html">Engineering Tools</a></li>
        </ul>
      </div>"""

for fname in BATCH_FILES:
    fpath = os.path.join(BASE_DIR, fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace broken links
    content = content.replace(FOOTER_OLD, FOOTER_NEW)
    content = content.replace('href="matrix-calculator.html"', 'href="ratio-calculator.html"')
    content = content.replace('Matrix Calculator', 'Ratio Calculator')
    content = content.replace('href="distance-converter.html"', 'href="length-converter.html"')
    content = content.replace('Distance Converter', 'Length & Distance Converter')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed links in {fname}")
