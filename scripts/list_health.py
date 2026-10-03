import os

db_path = r'C:\Users\Admin\.gemini\antigravity\brain\3654d7fd-c2ee-4fea-81eb-c02b00dc2534\calculator_master_database.md'
with open(db_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

existing = set(os.listdir('.'))

current_cat = ''
health_tools = []

for line in lines:
    if line.startswith('### '):
        current_cat = line.strip().replace('### ', '')
    elif '|' in line and not line.startswith('| Tool Name') and not ':---' in line:
        if 'Health, Fitness & Medical' in current_cat:
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 3:
                slug = parts[2].replace('`', '').strip()
                if slug:
                    fname = slug if slug.endswith('.html') else slug + '.html'
                    title = parts[1].replace('**', '').strip()
                    kw = parts[3].replace('`', '').strip() if len(parts) > 3 else ''
                    is_built = fname in existing
                    health_tools.append((title, fname, kw, is_built))

print(f"Total Health Tools: {len(health_tools)}")
for idx, (title, fname, kw, is_built) in enumerate(health_tools, 1):
    status = "[LIVE]" if is_built else "[UNBUILT]"
    print(f"{idx:02d}. {status} {title} -> {fname} (KW: {kw})")
