import glob
import re

category_files = [
    ('health.html', 'Health & Fitness', '⚖️'),
    ('finance.html', 'Finance & Investment', '🏦'),
    ('math.html', 'Mathematics & Utilities', '🔢'),
    ('engineering.html', 'Electrical & Power Systems', '⚡'),
    ('solar-energy.html', 'Solar & Renewable Energy', '☀️'),
    ('mechanical.html', 'Mechanical & HVAC', '⚙️'),
    ('civil.html', 'Civil & Construction', '🏗️'),
    ('chemical.html', 'Chemical & Water Treatment', '🧪'),
    ('fire-safety.html', 'Fire & Life Safety', '🚨'),
    ('programmer.html', 'Programmer & Networking', '👨‍💻'),
    ('datetime.html', 'Date & Time Utility', '📅'),
    ('converter.html', 'Universal Unit Converters', '🔄')
]

cat_tools = {}

for cat_file, cat_name, cat_icon in category_files:
    with open(cat_file, 'r', encoding='utf-8') as f:
        html = f.read()
    # Find all silo-card tool links or main cards
    matches = re.findall(r'<a href="([^"]+)" class="silo-card"[^>]*>.*?<div class="silo-card-title">([^<]+)</div>.*?<div class="silo-card-desc">([^<]+)</div>', html, re.DOTALL)
    cat_tools[cat_file] = {
        'name': cat_name,
        'icon': cat_icon,
        'tools': matches
    }
    print(f"\n=== {cat_name} ({cat_file}) - {len(matches)} Tools ===")
    for href, title, desc in matches:
        print(f"  * [{href}] {title.strip()} - {desc.strip()[:60]}...")

