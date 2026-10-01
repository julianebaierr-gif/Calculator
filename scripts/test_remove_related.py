import re

with open("loan-emi-calculator.html", "r", encoding="utf-8") as f:
    c = f.read()

# Pattern to remove the old related calculators at the bottom
old_related_pattern = re.compile(r'(?:<!--\s*Related Topic Silos\s*-->\s*)?<section>\s*<h2[^>]*>Related[^<]*</h2>\s*<div class="silo-card-grid">.*?</div>\s*</section>', re.DOTALL | re.IGNORECASE)

m = old_related_pattern.search(c)
if m:
    print(f"Matched old related section! Length = {len(m.group(0))}")
    print(f"Snippet:\n{m.group(0)[:150]}...")
else:
    print("NO MATCH for old related section!")
