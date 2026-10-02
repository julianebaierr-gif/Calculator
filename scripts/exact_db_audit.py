import os
import re

db_path = r"C:\Users\Admin\.gemini\antigravity\brain\3654d7fd-c2ee-4fea-81eb-c02b00dc2534\calculator_master_database.md"
base_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\calchub"

existing_files = set(f for f in os.listdir(base_dir) if f.endswith(".html"))

with open(db_path, "r", encoding="utf-8") as f:
    text = f.read()

# Split by category sections
sections = re.split(r"###\s+([^\n(]+)\s*\((\d+)\s*Tools?\)", text)

total_db_tools = 0
live_count = 0
missing_count = 0

print("=" * 70)
print("             CALCHUB MASTER DATABASE (373 TOOLS) AUDIT")
print("=" * 70)

category_missing = {}

for i in range(1, len(sections), 3):
    cat_name = sections[i].strip()
    cat_expected = int(sections[i+1])
    cat_body = sections[i+2]
    
    slugs = re.findall(r"\|\s*`([^`]+)`\s*\|", cat_body)
    cat_tools = []
    seen = set()
    for s in slugs:
        s_clean = s.strip()
        fname = s_clean + ".html" if not s_clean.endswith(".html") else s_clean
        if fname not in seen:
            seen.add(fname)
            cat_tools.append(fname)
            
    cat_live = [t for t in cat_tools if t in existing_files]
    cat_miss = [t for t in cat_tools if t not in existing_files]
    
    total_db_tools += len(cat_tools)
    live_count += len(cat_live)
    missing_count += len(cat_miss)
    
    category_missing[cat_name] = cat_miss
    
    status_icon = "[DONE]" if len(cat_miss) == 0 else "[PENDING]"
    print(f"{status_icon:<10} {cat_name:<40} : {len(cat_live):>2} Live / {len(cat_miss):>2} Bachy ({len(cat_tools)} Total)")

print("=" * 70)
print(f"TOTAL UNIQUE TOOLS IN DATABASE : {total_db_tools}")
print(f"CURRENTLY LIVE ON WEBSITE      : {live_count}")
print(f"TOTAL REMAINING (BACHI HUWI)   : {missing_count}")
print("=" * 70)

print("\n--- NEXT REMAINING TOOLS LIST (FIRST 25) ---")
all_missing = []
for cat, misses in category_missing.items():
    for m in misses:
        all_missing.append((cat, m))

for idx, (cat, m) in enumerate(all_missing[:25], 1):
    print(f"{idx:>2}. [{cat}] {m}")
