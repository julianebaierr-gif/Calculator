from bs4 import BeautifulSoup
import re

batch20 = [
    'down-payment-calculator.html',
    'emergency-fund-calculator.html',
    'inflation-calculator.html',
    'net-salary-calculator.html',
    'net-worth-calculator.html',
    'sales-tax-calculator.html',
    'savings-calculator.html',
    'savings-goal-calculator.html'
]

print("=== BATCH 20 WORD COUNT VERIFICATION ===")
for f in batch20:
    with open(f, 'r', encoding='utf-8') as fp:
        soup = BeautifulSoup(fp.read(), 'html.parser')
    art = soup.find('article', class_='article-body')
    text = art.get_text() if art else ''
    words = len(re.findall(r'\b\w+\b', text))
    status = "PASS (1000+)" if words >= 1000 else "FAIL (<1000)"
    print(f"{f:35} : {words:4} words -> {status}")
