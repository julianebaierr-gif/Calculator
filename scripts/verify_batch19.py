from bs4 import BeautifulSoup
import re

batch19 = [
    'acceleration-converter.html',
    'amortization-schedule-calculator.html',
    'apr-apy-calculator.html',
    'break-even-calculator.html',
    'capital-gains-calculator.html',
    'cd-calculator.html',
    'credit-card-payoff-calculator.html',
    'debt-to-income-calculator.html'
]

print("=== BATCH 19 WORD COUNT VERIFICATION ===")
for f in batch19:
    with open(f, 'r', encoding='utf-8') as fp:
        soup = BeautifulSoup(fp.read(), 'html.parser')
    art = soup.find('article', class_='article-body')
    text = art.get_text() if art else ''
    words = len(re.findall(r'\b\w+\b', text))
    status = "PASS (1000+)" if words >= 1000 else "FAIL (<1000)"
    print(f"{f:38} : {words:4} words -> {status}")
