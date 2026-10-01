"""
Update the sticky header in all HTML files to remove search and show all 12 categories.
"""

import glob
import re

CATEGORIES_ROW_1 = [
    ("health.html", "⚖️ Health", "health"),
    ("finance.html", "🏦 Finance", "finance"),
    ("math.html", "🔢 Math", "math"),
    ("engineering.html", "⚡ Electrical", "engineering"),
    ("solar-energy.html", "☀️ Solar", "solar"),
    ("mechanical.html", "⚙️ Mechanical", "mechanical")
]

CATEGORIES_ROW_2 = [
    ("civil.html", "🏗️ Civil", "civil"),
    ("chemical.html", "🧪 Chemical", "chemical"),
    ("fire-safety.html", "🚨 Fire &amp; Safety", "fire"),
    ("programmer.html", "👨‍💻 Programmer", "programmer"),
    ("datetime.html", "📅 Date &amp; Time", "datetime"),
    ("converter.html", "🔄 Converter", "converter")
]

def get_header_html(active_cat=None):
    r1_links = []
    for href, label, cat_key in CATEGORIES_ROW_1:
        is_active = ' active' if active_cat == cat_key else ''
        r1_links.append(f'          <a href="{href}" class="nav-link{is_active}">{label}</a>')
    r1_str = "\n".join(r1_links)

    r2_links = []
    for href, label, cat_key in CATEGORIES_ROW_2:
        is_active = ' active' if active_cat == cat_key else ''
        r2_links.append(f'          <a href="{href}" class="nav-link{is_active}">{label}</a>')
    r2_str = "\n".join(r2_links)

    return f"""  <!-- Sticky Header -->
  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="brand-logo">
        <span class="logo-badge">∑</span>
        <span>Calc<span class="accent">Hub</span></span>
      </a>
      <nav class="header-nav" aria-label="Main Navigation">
        <div class="nav-row">
{r1_str}
        </div>
        <div class="nav-row">
{r2_str}
        </div>
      </nav>
    </div>
  </header>"""

def determine_active_cat(filename):
    f = filename.lower()
    if "health" in f or "bmi" in f or "calorie" in f or "body-fat" in f or "ideal-weight" in f or "water-intake" in f:
        return "health"
    if "finance" in f or "loan" in f or "compound" in f or "interest" in f or "discount" in f or "salary" in f:
        return "finance"
    if "engineering" in f or "ohms" in f or "voltage" in f or "cable" in f or "resistor" in f:
        return "engineering"
    if "solar" in f or "charging" in f:
        return "solar"
    if "mechanical" in f or "cooling" in f or "pipe" in f or "torque" in f:
        return "mechanical"
    if "civil" in f or "concrete" in f or "rebar" in f or "brick" in f or "beam" in f:
        return "civil"
    if "chemical" in f:
        return "chemical"
    if "fire" in f or "smoke" in f:
        return "fire"
    if "programmer" in f or "subnet" in f:
        return "programmer"
    if "date" in f or "time" in f:
        return "datetime"
    if "converter" in f or "unit" in f:
        return "converter"
    if "math" in f or "percentage" in f or "age" in f or "gpa" in f or "fraction" in f or "ratio" in f:
        return "math"
    return None

def main():
    files = glob.glob("*.html")
    print(f"Updating headers across {len(files)} files...")
    
    header_pattern = re.compile(r'<!--\s*Sticky Header\s*-->\s*<header class="site-header">.*?</header>|<!--\s*Header\s*-->\s*<header class="site-header">.*?</header>|<header class="site-header">.*?</header>', re.DOTALL)

    updated_count = 0
    for f in files:
        with open(f, "r", encoding="utf-8") as fh:
            content = fh.read()

        active_cat = determine_active_cat(f)
        new_header = get_header_html(active_cat)

        if header_pattern.search(content):
            new_content = header_pattern.sub(new_header, content)
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(new_content)
            updated_count += 1
        else:
            print(f"Warning: header not matched in {f}")

    print(f"Successfully updated headers in {updated_count} files!")

if __name__ == "__main__":
    main()
