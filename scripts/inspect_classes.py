import glob
import re

classes_to_check = [
    'calc-field-group', 'field-label', 'calc-input', 'input-unit',
    'calc-select', 'breakdown-value', 'faq-q', 'faq-a', 'card-header',
    'results-badge', 'primary-result-desc', 'article-header',
    'category-breadcrumbs', 'article-meta', 'faq-container',
    'results-footer-actions', 'article-summary-box', 'data-table-container',
    'category-block-section', 'gpa-grade', 'gpa-credits', 'formula-block'
]

html_files = glob.glob("*.html")

for c in classes_to_check:
    print(f"\n==================== .{c} ====================")
    found = 0
    for hf in html_files:
        with open(hf, "r", encoding="utf-8") as f:
            content = f.read()
        matches = re.findall(rf'(<[^>]*class=["\'][^"\']*{re.escape(c)}[^"\']*["\'][^>]*>)', content)
        if matches:
            found += 1
            if found <= 2:
                print(f"[{hf}] -> {matches[0]}")
    print(f"Total files using .{c}: {found}")
