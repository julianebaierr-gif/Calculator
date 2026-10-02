import os
import re

db_path = r'C:\Users\Admin\.gemini\antigravity\brain\3654d7fd-c2ee-4fea-81eb-c02b00dc2534\calculator_master_database.md'

with open(db_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern for markdown tables where slug is enclosed in backticks
slugs = re.findall(r'\|\s*`([^`]+)`\s*\|', text)
seen = set()
unique_slugs = []
for s in slugs:
    # only slugs that look like calculator slugs
    if s.endswith('-calculator') or '-calculator-' in s or s in ['date-difference-calculator', 'unit-converter', 'projectile-motion-calculator', 'torque-converter']:
        html_file = s + '.html' if not s.endswith('.html') else s
        if html_file not in seen:
            seen.add(html_file)
            unique_slugs.append(html_file)

print(f"Total unique tool files extracted from database: {len(unique_slugs)}")

existing = set(f for f in os.listdir('.') if f.endswith('.html'))
print(f"Total HTML files in repo root: {len(existing)}")

live_tools = [s for s in unique_slugs if s in existing]
missing = [s for s in unique_slugs if s not in existing]

print(f"Live tools in database: {len(live_tools)}")
print(f"Missing tools in database: {len(missing)}")

print("\n--- NEXT 20 MISSING CALCULATORS ---")
for i, m in enumerate(missing[:20], 1):
    print(f"{i}. {m}")
