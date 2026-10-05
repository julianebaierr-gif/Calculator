import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Check bracket matching
open_count = css.count("{")
close_count = css.count("}")
print(f"Open brackets: {open_count}, Close brackets: {close_count}")
if open_count != close_count:
    print("WARNING: Unmatched brackets in styles.css!")

# Check for empty rules or duplicate blocks
empty_rules = re.findall(r'([^{]+)\{\s*\}', css)
print(f"Empty rules count: {len(empty_rules)}")
for r in empty_rules[:5]:
    print(f"  Empty: {r.strip()}")

# Check for double semicolons or malformed properties
double_semi = len(re.findall(r';\s*;', css))
print(f"Double semicolons count: {double_semi}")

# Find all selectors
selectors = re.findall(r'([^{]+)\{', css)
print(f"Total selectors/blocks: {len(selectors)}")
