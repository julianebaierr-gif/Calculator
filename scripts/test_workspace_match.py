import glob
import re

tools = [f for f in glob.glob('*.html') if f not in ['index.html', '404.html', 'health.html', 'finance.html', 'math.html', 'engineering.html', 'solar-energy.html', 'mechanical.html', 'civil.html', 'chemical.html', 'fire-safety.html', 'programmer.html', 'datetime.html', 'converter.html']]

unmatched = []
for t in tools:
    with open(t, 'r', encoding='utf-8') as f:
        c = f.read()
    # Find position of calculator-workspace
    idx = c.find('calculator-workspace')
    if idx == -1:
        unmatched.append((t, 'no calculator-workspace string'))
        continue
    # Find the tag start
    tag_start = c.rfind('<', 0, idx)
    tag_name = re.match(r'<(\w+)', c[tag_start:]).group(1)
    # Check if there is </main>
    main_idx = c.find('</main>')
    if main_idx == -1:
        unmatched.append((t, 'no </main>'))
        continue
    
print(f"Total tools checked: {len(tools)}, Unmatched: {len(unmatched)}")
if unmatched:
    print(unmatched)
else:
    print("ALL 33 tools contain 'calculator-workspace' and '</main>'!")
