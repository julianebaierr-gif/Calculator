import os
import re

base_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\calchub"
html_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]

system_pages = {
    "index.html", "about.html", "contact.html", "privacy.html", "terms.html",
    "chemical.html", "civil.html", "converter.html", "datetime.html",
    "engineering.html", "finance.html", "fire-safety.html", "health.html",
    "math.html", "mechanical.html", "programmer.html", "solar-energy.html"
}

live_calculators = [f for f in html_files if f not in system_pages]
print(f"Total HTML files on disk: {len(html_files)}")
print(f"System & Hub pages: {len([f for f in html_files if f in system_pages])}")
print(f"Total LIVE Calculators on website right now: {len(live_calculators)}")

# Check master database
db_path = r"C:\Users\Admin\.gemini\antigravity\brain\3654d7fd-c2ee-4fea-81eb-c02b00dc2534\calculator_master_database.md"
with open(db_path, "r", encoding="utf-8") as f:
    db_text = f.read()

# Match slugs in tables
raw_slugs = re.findall(r"\|\s*`([^`]+)`\s*\|", db_text)
db_tools = []
seen = set()
for s in raw_slugs:
    fname = s if s.endswith(".html") else s + ".html"
    if fname not in seen and fname not in system_pages:
        seen.add(fname)
        db_tools.append(fname)

print(f"\nTotal unique calculators in master database: {len(db_tools)}")

live_from_db = [t for t in db_tools if t in live_calculators]
missing_from_db = [t for t in db_tools if t not in live_calculators]

print(f"Database tools LIVE right now: {len(live_from_db)}")
print(f"Database tools REMAINING (Bachy huway): {len(missing_from_db)}")

# Check complete_site_hunt.txt
hunt_path = r"C:\Users\Admin\.gemini\antigravity\brain\3654d7fd-c2ee-4fea-81eb-c02b00dc2534\complete_site_hunt.txt"
if os.path.exists(hunt_path):
    with open(hunt_path, "r", encoding="utf-8") as f:
        hunt_text = f.read()
    # find lines with url slugs
    hunt_slugs = set(re.findall(r"aionlinecalculator\.com/([a-z0-9\-]+)", hunt_text))
    hunt_slugs = {s + ".html" for s in hunt_slugs if s not in ["category", "privacy", "terms", "about", "contact", ""]}
    print(f"\nTotal unique tools in complete_site_hunt.txt: {len(hunt_slugs)}")
    hunt_missing = [s for s in hunt_slugs if s not in live_calculators]
    print(f"Remaining from complete_site_hunt: {len(hunt_missing)}")

# Breakdown of remaining tools by category
cat_pattern = re.compile(r"### ([^\n]+)\s*\(\d+ Tools?\)\s*\n\s*\|[^\n]+\|\s*\n\s*\|[^\n]+\|\s*\n((?:\|[^\n]+\|\s*\n)+)")
matches = cat_pattern.findall(db_text)

print("\n--- REMAINING TOOLS BREAKDOWN BY CATEGORY ---")
total_categorized_missing = 0
for cat_name, table_block in matches:
    cat_slugs = re.findall(r"\|\s*`([^`]+)`\s*\|", table_block)
    cat_missing = [s + ".html" if not s.endswith(".html") else s for s in cat_slugs]
    cat_missing = [s for s in cat_missing if s not in live_calculators]
    if cat_missing:
        print(f"• {cat_name}: {len(cat_missing)} tools bachy hen")
        total_categorized_missing += len(cat_missing)
