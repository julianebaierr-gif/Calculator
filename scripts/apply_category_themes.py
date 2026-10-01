"""
Apply distinct category color themes across all 12 categories and 33 calculators.
"""

import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

THEMES = {
    "health": {
        "name": "Health & Fitness",
        "accent": "#059669",
        "subtle": "#ECFDF5",
        "border": "#A7F3D0",
        "hub": "health.html",
        "tools": [
            "bmi-calculator.html",
            "calorie-calculator.html",
            "body-fat-calculator.html",
            "ideal-weight-calculator.html",
            "water-intake-calculator.html"
        ]
    },
    "finance": {
        "name": "Finance & Investment",
        "accent": "#2563EB",
        "subtle": "#EFF6FF",
        "border": "#BFDBFE",
        "hub": "finance.html",
        "tools": [
            "loan-emi-calculator.html",
            "compound-interest-calculator.html",
            "simple-interest-calculator.html",
            "discount-calculator.html",
            "salary-calculator.html"
        ]
    },
    "math": {
        "name": "Mathematics & Utilities",
        "accent": "#7C3AED",
        "subtle": "#F5F3FF",
        "border": "#DDD6FE",
        "hub": "math.html",
        "tools": [
            "percentage-calculator.html",
            "age-calculator.html",
            "gpa-calculator.html",
            "fraction-calculator.html",
            "ratio-calculator.html"
        ]
    },
    "engineering": {
        "name": "Electrical Engineering",
        "accent": "#D97706",
        "subtle": "#FFFBEB",
        "border": "#FDE68A",
        "hub": "engineering.html",
        "tools": [
            "ohms-law-calculator.html",
            "voltage-drop-calculator.html",
            "cable-sizing-calculator.html",
            "resistor-color-code-calculator.html"
        ]
    },
    "solar": {
        "name": "Solar & Renewable Energy",
        "accent": "#EA580C",
        "subtle": "#FFF7ED",
        "border": "#FFEDD5",
        "hub": "solar-energy.html",
        "tools": [
            "solar-panel-sizing-calculator.html",
            "solar-battery-bank-calculator.html",
            "solar-inverter-sizing-calculator.html",
            "ev-charging-time-calculator.html"
        ]
    },
    "mechanical": {
        "name": "Mechanical & HVAC",
        "accent": "#0891B2",
        "subtle": "#ECFEFF",
        "border": "#A5F3FC",
        "hub": "mechanical.html",
        "tools": [
            "cooling-load-calculator.html",
            "pipe-sizing-calculator.html",
            "torque-calculator.html"
        ]
    },
    "civil": {
        "name": "Civil & Construction",
        "accent": "#B45309",
        "subtle": "#FEFCE8",
        "border": "#FEF08A",
        "hub": "civil.html",
        "tools": [
            "concrete-calculator.html",
            "rebar-calculator.html"
        ]
    },
    "chemical": {
        "name": "Chemical & Water Treatment",
        "accent": "#0D9488",
        "subtle": "#F0FDFA",
        "border": "#99F6E4",
        "hub": "chemical.html",
        "tools": [
            "chemical-dosing-calculator.html"
        ]
    },
    "fire": {
        "name": "Fire & Life Safety",
        "accent": "#DC2626",
        "subtle": "#FEF2F2",
        "border": "#FECACA",
        "hub": "fire-safety.html",
        "tools": [
            "smoke-detector-spacing-calculator.html"
        ]
    },
    "programmer": {
        "name": "Programmer & Networking",
        "accent": "#4F46E5",
        "subtle": "#EEF2FF",
        "border": "#C7D2FE",
        "hub": "programmer.html",
        "tools": [
            "subnet-calculator.html"
        ]
    },
    "datetime": {
        "name": "Date & Time Utilities",
        "accent": "#0284C7",
        "subtle": "#F0F9FF",
        "border": "#BAE6FD",
        "hub": "datetime.html",
        "tools": [
            "date-difference-calculator.html"
        ]
    },
    "converter": {
        "name": "Universal Converters",
        "accent": "#9333EA",
        "subtle": "#FAF5FF",
        "border": "#E9D5FF",
        "hub": "converter.html",
        "tools": [
            "unit-converter.html"
        ]
    }
}

def update_hub_page(filename, conf):
    with open(filename, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update body class
    html = re.sub(r'<body[^>]*>', f'<body class="cat-theme-{conf["key"]}">', html)

    # 2. Update category tag in hero
    hero_tag_pattern = re.compile(r'<span class="category-tag"[^>]*style="[^"]*"', re.DOTALL)
    new_tag_style = f'<span class="category-tag" style="background:{conf["subtle"]};color:{conf["accent"]};border-color:{conf["border"]};margin-bottom:1rem;"'
    html = hero_tag_pattern.sub(new_tag_style, html)

    # 3. Update silo cards border-top
    silo_pattern = re.compile(r'(<a href="[^"]+" class="silo-card"[^>]*style=")border-top:[^;"]+;(")', re.DOTALL)
    html = silo_pattern.sub(rf'\g<1>border-top:3px solid {conf["accent"]};\2', html)

    # 4. Update Launch Calculator link color in cards
    launch_pattern = re.compile(r'(<span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;)color:[^;"]+;(margin-top:1rem;">\s*Launch Calculator &rarr;\s*</span>)')
    html = launch_pattern.sub(rf'\g<1>color:{conf["accent"]};\2', html)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Hub updated: {filename} -> {conf['key']} ({conf['accent']})")

def update_calculator_page(filename, conf):
    with open(filename, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update body class
    html = re.sub(r'<body[^>]*>', f'<body class="cat-theme-{conf["key"]}">', html)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Calculator updated: {filename} -> {conf['key']} ({conf['accent']})")

def main():
    total_hubs = 0
    total_tools = 0

    for key, conf in THEMES.items():
        conf["key"] = key
        hub_file = conf["hub"]
        update_hub_page(hub_file, conf)
        total_hubs += 1

        for tool_file in conf["tools"]:
            update_calculator_page(tool_file, conf)
            total_tools += 1

    print(f"\nDone! Updated {total_hubs} hubs and {total_tools} calculator pages with distinct color themes.")

if __name__ == "__main__":
    main()
