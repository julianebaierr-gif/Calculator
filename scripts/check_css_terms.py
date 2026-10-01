with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

terms = [
    'calc-card', 'card-header', 'calc-card-header', 'calc-form-grid', 'calc-field-group',
    'field-label', 'calc-input', 'calc-select', 'input-unit', 'results-card', 'results-header',
    'results-badge', 'primary-result-box', 'primary-result-label', 'primary-result-value',
    'primary-result-desc', 'result-breakdown-grid', 'breakdown-item', 'breakdown-label',
    'breakdown-value', 'results-footer-actions', 'article-section', 'article-header',
    'article-meta', 'article-summary-box', 'data-table-container', 'data-table',
    'faq-container', 'faq-item', 'faq-q', 'faq-a', 'category-breadcrumbs', 'cat-hub-hero'
]

for t in terms:
    is_found = ("." + t) in css
    status = "FOUND" if is_found else "MISSING"
    print(f"{t:25}: {status}")
