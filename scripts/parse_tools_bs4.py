import json
from bs4 import BeautifulSoup

with open('index.html', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

cards = soup.find_all('div', class_='directory-tool-card')
print(f"BeautifulSoup found {len(cards)} cards")

tools_data = []
for card in cards:
    cat_tag = card.find('span', style=lambda s: s and 'font-size:0.72rem' in s)
    cat = cat_tag.get_text(strip=True) if cat_tag else ''
    
    icon_tag = card.find('span', style=lambda s: s and 'font-size:1.5rem' in s)
    icon = icon_tag.get_text(strip=True) if icon_tag else '🧮'
    
    a_tag = card.find('h3').find('a') if card.find('h3') else None
    title = a_tag.get_text(strip=True) if a_tag else ''
    url = a_tag['href'] if a_tag and 'href' in a_tag.attrs else ''
    
    p_tag = card.find('p')
    desc = p_tag.get_text(strip=True) if p_tag else ''
    
    code_tag = card.find('code')
    formula = code_tag.get_text(strip=True) if code_tag else ''
    
    search_data = card.get('data-search', f"{title} {url} {desc}").lower()
    
    clean_url = url.replace('.html', '')
    
    tools_data.append({
        'c': cat,
        'i': icon,
        't': title,
        'u': clean_url,
        'd': desc,
        'f': formula,
        's': search_data
    })

print(f"Successfully processed {len(tools_data)} tools")

json_str = json.dumps(tools_data, ensure_ascii=False)
print(f"JSON size: {len(json_str.encode('utf-8')) / 1024:.1f} KB")

with open('tools-directory.json', 'w', encoding='utf-8') as f:
    f.write(json_str)

print("Saved to tools-directory.json")
