import os
import glob

def main():
    files = glob.glob('*.html')
    target_files = [f for f in files if f not in ['index.html', '404.html', 'health.html', 'finance.html', 'math.html', 'engineering.html']]
    print(f"Updating {len(target_files)} calculator files...")

    for f in target_files:
        with open(f, 'r', encoding='utf-8') as fh:
            content = fh.read()

        content = content.replace('href="index.html#health"', 'href="health.html"')
        content = content.replace('href="index.html#finance"', 'href="finance.html"')
        content = content.replace('href="index.html#math"', 'href="math.html"')
        content = content.replace('href="index.html#engineering"', 'href="engineering.html"')

        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(content)

    print("All calculator files updated successfully.")

if __name__ == '__main__':
    main()
