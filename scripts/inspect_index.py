with open('index.html', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
for idx, line in enumerate(lines):
    if '<section' in line or '</section>' in line or 'all-calculators' in line or 'id=' in line and '<h' in line:
        print(f"Line {idx+1}: {line.strip()[:100]}")
