import glob

all_html = glob.glob("*.html")
category_pages = set([
    "index.html", "404.html", "health.html", "finance.html", "math.html",
    "engineering.html", "solar-energy.html", "mechanical.html", "civil.html",
    "chemical.html", "physics.html", "fire-safety.html", "programmer.html",
    "datetime.html", "converter.html"
])
tool_pages = [f for f in all_html if f not in category_pages]

old_header = []
old_footer = []
no_sidebar = []

for f in tool_pages:
    c = open(f, encoding="utf-8", errors="ignore").read()
    if 'class="site-header"' not in c:
        old_header.append(f)
    if 'class="site-footer"' not in c or 'footer-inner' not in c:
        old_footer.append(f)
    if 'sidebar-widget' not in c:
        no_sidebar.append(f)

print(f"Total tool pages: {len(tool_pages)}")
print(f"Pages without standard site-header: {len(old_header)}")
print(f"Pages without standard site-footer (footer-inner): {len(old_footer)}")
print(f"Pages without sidebar-widget: {len(no_sidebar)}")

if old_header:
    print(f"\nPages without standard site-header ({len(old_header)}):")
    for f in old_header:
        print(f" - {f}")

if old_footer:
    print(f"\nPages without standard site-footer ({len(old_footer)}):")
    for f in old_footer:
        print(f" - {f}")

if no_sidebar:
    print(f"\nPages without sidebar-widget ({len(no_sidebar)}):")
    for f in no_sidebar:
        print(f" - {f}")
