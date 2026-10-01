import glob
import re

with open("styles.css", "r", encoding="utf-8") as f:
    css_content = f.read()

# Extract class selectors from CSS
css_classes = set(re.findall(r"\.([a-zA-Z0-9_-]+)", css_content))

# Extract all classes from HTML files
html_files = glob.glob("*.html")
used_classes = {}
for hf in html_files:
    with open(hf, "r", encoding="utf-8") as f:
        html = f.read()
    classes = re.findall(r'class=["\']([^"\']+)["\']', html)
    for c_str in classes:
        for c in c_str.split():
            used_classes.setdefault(c, []).append(hf)

missing_classes = {}
for c, files in used_classes.items():
    if c not in css_classes:
        missing_classes[c] = len(files)

print(f"Total unique classes in HTML: {len(used_classes)}")
print(f"Classes in styles.css: {len(css_classes)}")
print(f"Missing classes count: {len(missing_classes)}")
print("\nMissing classes and how many files use them:")
for c, count in sorted(missing_classes.items(), key=lambda x: -x[1]):
    print(f"  .{c:35} in {count} files")
