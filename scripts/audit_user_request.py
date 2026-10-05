import glob
import os

user_keywords = [
    'treadmill calorie calculator',
    'stairmaster calorie calculator',
    'cycling calorie calculator',
    'pushup calorie calculator',
    'bench press calories calculator',
    'swimming calorie calculator',
    'stationary bike calorie calculator',
    'incline treadmill calorie calculator',
    'rucking calorie calculator',
    'Jack Daniels Running Calculator',
    'jumping jacks calories burned calculator',
    'squat calorie calculator',
    'Sit Up Calorie Calculator',
    'leg press to squat calculator',
    'Cycling Watt Calorie Calculator',
    'Running Calorie Calculator',
    'Rowing Machine Calorie Calculator',
    'peloton calorie burn calculator',
    'elliptical calorie calculator',
    'FTP Calculator',
    'elliptical to running conversion calculator',
    'BMI Calculator',
    'Body Fat Calculator',
    'BMR Calculator',
    'Lean Body Mass Calculator',
    'Army Body Fat Calculator',
    'TDEE Calculator',
    'starbucks calories calculator'
]

existing_files = set(os.path.basename(f) for f in glob.glob('*.html'))

slug_map = {
    'treadmill calorie calculator': 'treadmill-calorie-calculator.html',
    'stairmaster calorie calculator': 'stairmaster-calorie-calculator.html',
    'cycling calorie calculator': 'cycling-calorie-calculator.html',
    'pushup calorie calculator': 'pushup-calorie-calculator.html',
    'bench press calories calculator': 'bench-press-calories-calculator.html',
    'swimming calorie calculator': 'swimming-calorie-calculator.html',
    'stationary bike calorie calculator': 'stationary-bike-calorie-calculator.html',
    'incline treadmill calorie calculator': 'incline-treadmill-calorie-calculator.html',
    'rucking calorie calculator': 'rucking-calorie-calculator.html',
    'Jack Daniels Running Calculator': 'jack-daniels-running-calculator.html',
    'jumping jacks calories burned calculator': 'jumping-jacks-calories-burned-calculator.html',
    'squat calorie calculator': 'squat-calorie-calculator.html',
    'Sit Up Calorie Calculator': 'sit-up-calorie-calculator.html',
    'leg press to squat calculator': 'leg-press-to-squat-calculator.html',
    'Cycling Watt Calorie Calculator': 'cycling-watt-calorie-calculator.html',
    'Running Calorie Calculator': 'running-calorie-calculator.html',
    'Rowing Machine Calorie Calculator': 'rowing-machine-calorie-calculator.html',
    'peloton calorie burn calculator': 'peloton-calorie-burn-calculator.html',
    'elliptical calorie calculator': 'elliptical-calorie-calculator.html',
    'FTP Calculator': 'ftp-calculator.html',
    'elliptical to running conversion calculator': 'elliptical-to-running-conversion-calculator.html',
    'BMI Calculator': 'bmi-calculator.html',
    'Body Fat Calculator': 'body-fat-calculator.html',
    'BMR Calculator': 'bmr-calculator.html',
    'Lean Body Mass Calculator': 'lean-body-mass-calculator.html',
    'Army Body Fat Calculator': 'army-body-fat-calculator.html',
    'TDEE Calculator': 'tdee-calculator.html',
    'starbucks calories calculator': 'starbucks-calories-calculator.html'
}

exists = []
missing = []

for kw, slug in slug_map.items():
    if slug in existing_files:
        exists.append((kw, slug))
    else:
        missing.append((kw, slug))

print(f"Total requested: {len(user_keywords)}")
print(f"Already exists: {len(exists)}")
for kw, slug in exists:
    print(f"  [EXISTS] {kw} -> {slug}")

print(f"\nMissing to be built: {len(missing)}")
for i, (kw, slug) in enumerate(missing, 1):
    print(f"  {i}. [MISSING] {kw} -> {slug}")
