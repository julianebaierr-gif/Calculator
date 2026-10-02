# -*- coding: utf-8 -*-
import glob
import os

def check():
    with open(r'C:\Users\Admin\.gemini\antigravity\brain\3654d7fd-c2ee-4fea-81eb-c02b00dc2534\calculator_master_database.md', encoding='utf-8') as f:
        lines = f.readlines()

    live_files = set([os.path.basename(p) for p in glob.glob('*.html')])

    missing = []
    total_tools = 0
    for line in lines:
        line_clean = line.strip()
        if line_clean.startswith('|') and '`' in line_clean and ':---' not in line_clean and 'URL Slug' not in line_clean:
            parts = [p.strip() for p in line_clean.split('|') if p.strip()]
            if len(parts) >= 3:
                name = parts[0].replace('*', '').strip()
                slug = parts[1].replace('`', '').strip()
                kw = parts[2].replace('`', '').strip()
                html_file = slug if slug.endswith('.html') else slug + '.html'
                total_tools += 1
                if html_file not in live_files:
                    missing.append((name, html_file, kw))

    live_count = len([f for f in live_files if f not in [
        'index.html', '404.html', 'health.html', 'finance.html', 'math.html',
        'engineering.html', 'solar-energy.html', 'mechanical.html', 'civil.html',
        'chemical.html', 'fire-safety.html', 'programmer.html', 'datetime.html', 'converter.html'
    ]])
    print(f"Total Database Tools in Master Table: {total_tools}")
    print(f"Total Live Tool Calculators on Website: {live_count}")
    print(f"Database Tools Still Missing: {len(missing)}")
    print(f"\nNext 12 Missing Tools for Batch 7 & 8:")
    for i, (name, html_file, kw) in enumerate(missing[:12], 1):
        print(f"  {i}. {html_file} -> {name} (KW: \"{kw}\")")

if __name__ == '__main__':
    check()
