import re

files = [
    'mechanical.html', 'engineering.html', 'solar-energy.html', 'civil.html',
    'chemical.html', 'fire-safety.html', 'finance.html', 'health.html',
    'math.html', 'datetime.html', 'programmer.html', 'converter.html'
]

for f in files:
    content = open(f, encoding='utf-8').read()
    match = re.search(r'class=["\']article-section["\'][^>]*>(.*)', content, re.DOTALL)
    if match:
        text = re.sub(r'<[^>]+>', ' ', match.group(1))
        words = len(text.split())
        print(f'{f:20}: {words:5d} words in article section')
    else:
        print(f'{f:20}: not found')
