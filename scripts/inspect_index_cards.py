import re

with open('index.html', encoding='utf-8') as f:
    c = f.read()

# Match directory-tool-card
cards = re.findall(r'<div class="directory-tool-card"([^>]*)>(.*?)(?=<div class="directory-tool-card"|</div>\s*</div>\s*<div id="no-search-results")', c, re.S)
print(f"Total directory tool cards: {len(cards)}")

# Check cards before line 1168
before_1168 = c[:c.find('<section id="all-calculators-directory"')]
print(f"Size of index.html before all-calculators-directory: {len(before_1168.encode('utf-8')) / 1024:.1f} KB")

after_6626 = c[c.find('</section>\n  </main>'):]
print(f"Size of index.html after all-calculators-directory: {len(after_6626.encode('utf-8')) / 1024:.1f} KB")
