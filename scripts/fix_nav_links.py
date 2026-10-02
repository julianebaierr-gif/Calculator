import os

files = [
    'acceleration-calculator.html',
    'angular-velocity-calculator.html',
    'centripetal-force-calculator.html',
    'doppler-effect-calculator.html',
    'escape-velocity-calculator.html',
    'free-fall-calculator.html',
    'physics.html',
    os.path.join('scripts', 'gen_batch17_part2.py'),
    os.path.join('scripts', 'gen_batch17_part3.py'),
    os.path.join('scripts', 'gen_batch17_part4.py'),
    os.path.join('scripts', 'gen_physics_hub.py'),
]

for fn in files:
    if os.path.exists(fn):
        with open(fn, 'r', encoding='utf-8') as f:
            c = f.read()
        c = c.replace('href="electrical.html"', 'href="engineering.html"')
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Fixed {fn}")
