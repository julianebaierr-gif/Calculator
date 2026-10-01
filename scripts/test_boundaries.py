import glob
import re

tools = [f for f in glob.glob('*.html') if f not in ['index.html', '404.html', 'health.html', 'finance.html', 'math.html', 'engineering.html', 'solar-energy.html', 'mechanical.html', 'civil.html', 'chemical.html', 'fire-safety.html', 'programmer.html', 'datetime.html', 'converter.html']]

for t in tools:
    with open(t, 'r', encoding='utf-8') as f:
        c = f.read()

    # Find the start of calculator-workspace
    m_start = re.search(r'<([a-z0-9]+)[^>]*class=["\'][^"\']*calculator-workspace[^"\']*["\'][^>]*>', c, re.IGNORECASE)
    if not m_start:
        print(f"Error finding start in {t}")
        continue
    start_pos = m_start.start()
    tag_name = m_start.group(1)

    # Let's count matching tags from start_pos
    pos = start_pos
    open_count = 0
    end_pos = -1

    # Tokenize tags from start_pos
    tag_regex = re.compile(rf'</?{tag_name}\b[^>]*>', re.IGNORECASE)
    for tm in tag_regex.finditer(c, start_pos):
        tag_str = tm.group(0)
        if tag_str.startswith('</'):
            open_count -= 1
            if open_count == 0:
                end_pos = tm.end()
                break
        else:
            open_count += 1

    if end_pos != -1:
        after_workspace = c[end_pos:]
        main_end = after_workspace.find('</main>')
        between = after_workspace[:main_end]
        has_article = '<article' in between
        print(f"{t:35}: end found! Between length={len(between)}, has_article={has_article}")
    else:
        print(f"{t:35}: ERROR finding end!")
