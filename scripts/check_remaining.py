import os
import sys

db_path = r'C:\Users\Admin\.gemini\antigravity\brain\3654d7fd-c2ee-4fea-81eb-c02b00dc2534\calculator_master_database.md'
with open(db_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

existing = set(os.listdir('.'))

current_cat = ''
unbuilt = {}
built = {}

for line in lines:
    if line.startswith('### '):
        current_cat = line.strip().replace('### ', '')
        unbuilt[current_cat] = []
        built[current_cat] = []
    elif '|' in line and not line.startswith('| Tool Name') and not ':---' in line:
        parts = [p.strip() for p in line.split('|')]
        if len(parts) >= 3:
            slug = parts[2].replace('`', '').strip()
            if slug:
                fname = slug if slug.endswith('.html') else slug + '.html'
                title = parts[1].replace('**', '').strip()
                kw = parts[3].replace('`', '').strip() if len(parts) > 3 else ''
                if fname in existing:
                    built[current_cat].append((title, fname))
                else:
                    unbuilt[current_cat].append((title, fname, kw))

total_built = sum(len(v) for v in built.values())
total_unbuilt = sum(len(v) for v in unbuilt.values())

print(f"Total Tools in Database: {total_built + total_unbuilt}")
print(f"Total Built & Live: {total_built}")
print(f"Total Remaining Unbuilt: {total_unbuilt}\n")

print("--- CATEGORY BREAKDOWN ---")
for cat in unbuilt:
    b_count = len(built.get(cat, []))
    u_count = len(unbuilt.get(cat, []))
    status = "COMPLETE" if u_count == 0 else f"{u_count} REMAINING"
    print(f"{cat}: {b_count}/{b_count + u_count} built ({status})")
    if u_count > 0:
        for t in unbuilt[cat]:
            print(f"   - {t[0]} -> {t[1]}")
