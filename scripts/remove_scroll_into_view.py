import glob, re

files = sorted(glob.glob('*.html'))
fixed = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    if 'scrollIntoView' in c:
        # Remove lines calling scrollIntoView
        c_new = re.sub(r'[^\n]*\.scrollIntoView\([^)]*\);?\s*\n', '\n', c)
        if c_new != c:
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(c_new)
            fixed += 1

print(f"Removed scrollIntoView from {fixed} files!")
