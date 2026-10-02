import os
import re

db_path = r"C:\Users\Admin\.gemini\antigravity\brain\3654d7fd-c2ee-4fea-81eb-c02b00dc2534\calculator_master_database.md"
base_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\calchub"

existing_files = set(f for f in os.listdir(base_dir) if f.endswith(".html"))

with open(db_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

categories = {}
current_cat = None

for line in lines:
    line_str = line.strip()
    # Check category header
    m_cat = re.match(r"^###\s+([^\n(]+)\s*\((\d+)\s*Tools?\)", line_str)
    if m_cat:
        current_cat = m_cat.group(1).strip()
        categories[current_cat] = []
        continue
    
    # Check table row
    if current_cat and line_str.startswith("|") and not line_str.startswith("| :---") and not "Tool Name" in line_str:
        cols = [c.strip() for c in line_str.split("|")]
        # cols[0] is empty (before first |)
        # cols[1] is Tool Name
        # cols[2] is URL Slug
        # cols[3] is Primary Keyword
        # cols[4] is Search Intent
        if len(cols) >= 3:
            slug = cols[2].replace("`", "").strip()
            name = cols[1].replace("*", "").strip()
            if slug and not slug.startswith("http") and not slug == "URL Slug":
                fname = slug + ".html" if not slug.endswith(".html") else slug
                categories[current_cat].append((fname, name))

print("=" * 72)
print("           CALCHUB MASTER DATABASE (373 TOOLS) REAL AUDIT")
print("=" * 72)

total_db_tools = 0
live_count = 0
missing_count = 0
all_missing = []

for cat_name, tools in categories.items():
    cat_live = [t for t in tools if t[0] in existing_files]
    cat_miss = [t for t in tools if t[0] not in existing_files]
    
    total_db_tools += len(tools)
    live_count += len(cat_live)
    missing_count += len(cat_miss)
    
    status = "[DONE]    " if len(cat_miss) == 0 else f"[PENDING: {len(cat_miss):>2}]"
    print(f"{status} {cat_name:<40} : {len(cat_live):>2} Live / {len(tools):>2} Total")
    
    for t in cat_miss:
        all_missing.append((cat_name, t[0], t[1]))

print("=" * 72)
print(f"TOTAL UNIQUE TOOLS IN DATABASE : {total_db_tools}")
print(f"TOTAL DATABASE TOOLS LIVE      : {live_count}")
print(f"TOTAL REMAINING (ABHI BACHY)   : {missing_count}")
print("=" * 72)

print("\n--- NEXT 25 REMAINING TOOLS ---")
for idx, (cat, fname, name) in enumerate(all_missing[:25], 1):
    print(f"{idx:>2}. [{cat}] {fname:<42} ({name})")
