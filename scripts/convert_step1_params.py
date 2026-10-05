# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PARAM_GRIDS = {
    "bmi-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Sex:</strong> Male</span>
              <span class="step-param-pill"><strong>Age:</strong> 34</span>
              <span class="step-param-pill"><strong>Height:</strong> 180 cm (1.80 m)</span>
              <span class="step-param-pill"><strong>Weight:</strong> 88.0 kg</span>
            </div>""",

    "body-fat-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Sex:</strong> Male</span>
              <span class="step-param-pill"><strong>Height:</strong> 178 cm</span>
              <span class="step-param-pill"><strong>Neck:</strong> 39.0 cm</span>
              <span class="step-param-pill"><strong>Waist:</strong> 91.0 cm</span>
              <span class="step-param-pill"><strong>Weight:</strong> 85.0 kg</span>
            </div>""",

    "age-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Date of Birth:</strong> August 24, 1996</span>
              <span class="step-param-pill"><strong>Reference Date:</strong> October 1, 2026</span>
            </div>""",

    "date-difference-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Start Date:</strong> February 15, 2024</span>
              <span class="step-param-pill"><strong>Handover Date:</strong> November 20, 2025</span>
            </div>""",

    "datetime.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Commencement Date:</strong> March 15, 2024</span>
              <span class="step-param-pill"><strong>Practical Completion:</strong> November 20, 2025</span>
            </div>""",

    "ideal-weight-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Biological Sex:</strong> Male</span>
              <span class="step-param-pill"><strong>Height:</strong> 5 ft 10 in (70 in / 177.8 cm)</span>
            </div>""",

    "resistor-color-code-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>1st Band:</strong> Brown (1)</span>
              <span class="step-param-pill"><strong>2nd Band:</strong> Green (5)</span>
              <span class="step-param-pill"><strong>3rd Band:</strong> Black (0)</span>
              <span class="step-param-pill"><strong>Multiplier:</strong> Orange (1,000)</span>
              <span class="step-param-pill"><strong>Tolerance:</strong> Brown (±1%)</span>
            </div>""",

    "salary-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Gross Annual Salary:</strong> $85,000 / year</span>
              <span class="step-param-pill"><strong>Pay Frequency:</strong> Bi-Weekly (26 Paychecks/Year)</span>
            </div>""",

    "ratio-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Target Proportion:</strong> 1 : 2 : 4</span>
              <span class="step-param-pill"><strong>Total Parts:</strong> 1 + 2 + 4 = 7</span>
            </div>""",

    "gpa-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Calculus IV:</strong> 4 cr (Grade A = 4.0)</span>
              <span class="step-param-pill"><strong>Heat Transfer:</strong> 3 cr (Grade A- = 3.7)</span>
              <span class="step-param-pill"><strong>Circuit Analysis:</strong> 3 cr (Grade B+ = 3.3)</span>
              <span class="step-param-pill"><strong>Physics Lab:</strong> 1 cr (Grade A = 4.0)</span>
            </div>""",

    "smoke-detector-spacing-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Room Length (L):</strong> 36.0 m</span>
              <span class="step-param-pill"><strong>Room Width (W):</strong> 18.0 m</span>
              <span class="step-param-pill"><strong>Ceiling Profile:</strong> 3.5 m Smooth Concrete Slab</span>
            </div>""",

    "fire-safety.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Facility Length (L):</strong> 48.0 m (157.5 ft)</span>
              <span class="step-param-pill"><strong>Facility Width (W):</strong> 24.0 m (78.7 ft)</span>
              <span class="step-param-pill"><strong>Ceiling Profile:</strong> 3.6 m Flat Concrete Slab</span>
            </div>""",

    "rebar-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Slab Length (L):</strong> 12.0 m</span>
              <span class="step-param-pill"><strong>Slab Width (W):</strong> 8.0 m</span>
              <span class="step-param-pill"><strong>Bar Schedule:</strong> T12 (12 mm) @ 150 mm c/c</span>
            </div>""",

    "compound-interest-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Initial Principal (P):</strong> $50,000</span>
              <span class="step-param-pill"><strong>Annual Rate (r):</strong> 8.00% (0.08)</span>
              <span class="step-param-pill"><strong>Investment Horizon (t):</strong> 15 Years</span>
              <span class="step-param-pill"><strong>Compounding Frequency (n):</strong> 12 (Monthly)</span>
            </div>""",

    "loan-emi-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Borrowing Principal (P):</strong> $350,000</span>
              <span class="step-param-pill"><strong>Annual Rate (r):</strong> 6.75%</span>
              <span class="step-param-pill"><strong>Term (n):</strong> 25 Years (300 Monthly Payments)</span>
            </div>""",

    "simple-interest-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Loan Principal (P):</strong> $25,000</span>
              <span class="step-param-pill"><strong>Annual Rate (r):</strong> 7.50% (0.075)</span>
              <span class="step-param-pill"><strong>Term (t):</strong> 1.5 Years (18 Months)</span>
            </div>""",

    "mortgage-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Purchase Price:</strong> $500,000</span>
              <span class="step-param-pill"><strong>Down Payment (10%):</strong> $50,000</span>
              <span class="step-param-pill"><strong>Financed Loan (P):</strong> $450,000</span>
              <span class="step-param-pill"><strong>Loan-to-Value (LTV):</strong> 90.0%</span>
            </div>""",

    "discount-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Original Price:</strong> $240.00</span>
              <span class="step-param-pill"><strong>Store Sale Discount:</strong> 30% Off</span>
              <span class="step-param-pill"><strong>Member Loyalty Coupon:</strong> Extra 15% Off</span>
              <span class="step-param-pill"><strong>Sales Tax:</strong> 8.5%</span>
            </div>""",

    "tip-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Culinary Subtotal:</strong> $340.00</span>
              <span class="step-param-pill"><strong>Sales Tax (8.875%):</strong> $30.18</span>
            </div>""",

    "water-intake-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Body Weight:</strong> 80.0 kg</span>
              <span class="step-param-pill"><strong>Hydration Baseline:</strong> 35 mL / kg / day</span>
            </div>""",

    "ohms-law-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Heating Power (P):</strong> 4,500 W (4.5 kW)</span>
              <span class="step-param-pill"><strong>Supply Voltage (V):</strong> 230 V AC</span>
            </div>""",

    "percentage-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Q1 Baseline Revenue:</strong> $125,000</span>
              <span class="step-param-pill"><strong>Q2 Comparison Revenue:</strong> $165,000</span>
            </div>""",

    "pipe-sizing-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Flow Rate (Q):</strong> 120 m³/hr (0.0333 m³/s / 528.3 GPM)</span>
            </div>""",

    "torque-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Motor Power (P):</strong> 15.0 kW</span>
              <span class="step-param-pill"><strong>Shaft Speed (N):</strong> 1,450 RPM</span>
            </div>""",

    "solar-battery-bank-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Daily Energy Consumption:</strong> 12 kWh/day (12,000 Wh/day)</span>
            </div>""",

    "calorie-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Demographics:</strong> Male, 32 Years</span>
              <span class="step-param-pill"><strong>Weight (W):</strong> 84.0 kg</span>
              <span class="step-param-pill"><strong>Height (H):</strong> 180 cm</span>
              <span class="step-param-pill"><strong>Activity Level:</strong> Moderate (4 days/week, PAL 1.55)</span>
            </div>""",

    "programmer.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Base Network:</strong> 192.168.10.0/24</span>
              <span class="step-param-pill"><strong>Total Capacity:</strong> 256 Host IP Addresses</span>
            </div>""",

    "chemical-dosing-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Flow Rate (Q):</strong> 1,500 m³/day (62.5 m³/hr)</span>
              <span class="step-param-pill"><strong>Target Chlorine Dose:</strong> 4.0 mg/L (4.0 g/m³)</span>
            </div>""",

    "voltage-drop-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Supply Voltage:</strong> 400 V AC Line-to-Line</span>
              <span class="step-param-pill"><strong>Load Current (I):</strong> 55 A</span>
              <span class="step-param-pill"><strong>One-Way Length (L):</strong> 120 m</span>
              <span class="step-param-pill"><strong>Conductor:</strong> 25 mm² Copper</span>
            </div>""",

    "beam-deflection-calculator.html": """            <div class="step-param-grid">
              <span class="step-param-pill"><strong>Clear Span (L):</strong> 7.50 m</span>
              <span class="step-param-pill"><strong>Service Load (w):</strong> 18.0 kN/m</span>
              <span class="step-param-pill"><strong>Modulus (E):</strong> 200 GPa</span>
              <span class="step-param-pill"><strong>Moment of Inertia (Ix):</strong> 216 × 10⁶ mm⁴</span>
            </div>"""
}

def convert_step1():
    updated = 0
    for filename, replacement in PARAM_GRIDS.items():
        filepath = os.path.join(BASE_DIR, filename)
        if not os.path.exists(filepath):
            print(f"File not found: {filename}")
            continue

        with open(filepath, "r", encoding="utf-8", errors="ignore") as fp:
            content = fp.read()

        # Find the Step 1 calc-step-item
        step1_regex = re.compile(
            r'(<div class="calc-step-item">\s*<div class="calc-step-title">[^<]*Step 1:[^<]*</div>\s*)<div class="formula-block"[^>]*>[\s\S]*?</div>',
            re.IGNORECASE
        )

        match = step1_regex.search(content)
        if match:
            new_step1 = match.group(1) + replacement
            new_content = content[:match.start()] + new_step1 + content[match.end():]
            with open(filepath, "w", encoding="utf-8") as fp:
                fp.write(new_content)
            updated += 1
            print(f"Updated Step 1 in {filename}")
        else:
            print(f"Could not find regex match for Step 1 in {filename}")

    print(f"Total files updated with clean parameter grid: {updated} of {len(PARAM_GRIDS)}")

if __name__ == "__main__":
    convert_step1()
