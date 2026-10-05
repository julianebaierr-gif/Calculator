import os
import glob
import re

db_path = r"C:\Users\Admin\.gemini\antigravity\brain\3654d7fd-c2ee-4fea-81eb-c02b00dc2534\calculator_master_database.md"
with open(db_path, "r", encoding="utf-8") as f:
    text = f.read()

# Match lines like | **Tool** | `slug` | `keyword` | `intent` |
slugs = []
for line in text.splitlines():
    parts = line.split("|")
    if len(parts) >= 4:
        col2 = parts[2].strip()
        if col2.startswith("`") and col2.endswith("`"):
            slug = col2.strip("`").strip()
            if slug and slug != "URL Slug":
                slugs.append(slug)

slugs = list(dict.fromkeys(slugs))

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
existing = set(os.path.basename(p) for p in glob.glob(os.path.join(base_dir, "*.html")))

missing = []
for s in slugs:
    fname = s if s.endswith(".html") else s + ".html"
    if fname not in existing:
        missing.append((s, fname))

print(f"Total slugs extracted from master database: {len(slugs)}")
print(f"Total existing HTML files in root: {len(existing)}")
print(f"Total missing tools: {len(missing)}")
print("\n--- MISSING TOOLS ---")
for i, (slug, fname) in enumerate(missing, 1):
    print(f"{i}. {fname}")
