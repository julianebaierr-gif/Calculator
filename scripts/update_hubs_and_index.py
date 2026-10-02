"""
Updates all category hub pages, index.html, and runs apply_sidebars_all.py
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 1. Update civil.html
civil_path = os.path.join(BASE_DIR, "civil.html")
with open(civil_path, "r", encoding="utf-8") as f:
    civil_content = f.read()

civil_cards = """
        <a href="brick-calculator.html" class="silo-card" style="border-top:3px solid #B45309;">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;">
            <div class="silo-card-icon">🧱</div>
            <span class="silo-card-badge">ASTM C216 &amp; C90</span>
          </div>
          <div class="silo-card-title">Brick &amp; Block Masonry Calculator</div>
          <div class="silo-card-desc">Calculate standard modular brick counts, mortar bags, sand volume, and waste allowance for single and multi-wythe walls.</div>
          <div class="formula-badge-pill">Bricks = Wall Area × Multiplier × (1 + Waste)</div>
          <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:#B45309;margin-top:1rem;">
            Launch Calculator &rarr;
          </span>
        </a>

        <a href="asphalt-calculator.html" class="silo-card" style="border-top:3px solid #B45309;">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;">
            <div class="silo-card-icon">🛣️</div>
            <span class="silo-card-badge">Asphalt Institute MS-4</span>
          </div>
          <div class="silo-card-title">Asphalt Paving &amp; Tonnage Calculator</div>
          <div class="silo-card-desc">Determine hot mix asphalt (HMA) tonnage, volume, and crushed stone base aggregate based on 145 lbs/cu ft density and compaction factor.</div>
          <div class="formula-badge-pill">Tons = Volume × Density ÷ 2,000 lbs</div>
          <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:#B45309;margin-top:1rem;">
            Launch Calculator &rarr;
          </span>
        </a>
"""

if "brick-calculator.html" not in civil_content:
    civil_content = civil_content.replace('<strong>4</strong> Certified Calculators', '<strong>6</strong> Certified Calculators')
    civil_content = civil_content.replace('Available Tools (4)', 'Available Tools (6)')
    civil_content = civil_content.replace('</div>\n\n    <!-- Educational Guide -->', civil_cards + '\n</div>\n\n    <!-- Educational Guide -->')
    civil_content = civil_content.replace('</div>\n    <!-- Educational Guide -->', civil_cards + '\n</div>\n    <!-- Educational Guide -->')
    with open(civil_path, "w", encoding="utf-8") as f:
        f.write(civil_content)
    print("civil.html updated!")

# 2. Update health.html
health_path = os.path.join(BASE_DIR, "health.html")
with open(health_path, "r", encoding="utf-8") as f:
    health_content = f.read()

health_cards = """
      <!-- 6. BMR Calculator -->
      <a href="bmr-calculator.html" class="silo-card" style="border-top:3px solid #059669;">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;">
          <div class="silo-card-icon">🧬</div>
          <span class="silo-card-badge">Mifflin &amp; Katch</span>
        </div>
        <div class="silo-card-title">BMR Calculator (Basal Metabolism)</div>
        <div class="silo-card-desc">Determine baseline resting caloric burn using clinical Mifflin-St Jeor, Harris-Benedict, and lean mass Katch-McArdle equations.</div>
        <div class="formula-badge-pill">BMR = 10W + 6.25H - 5A + s</div>
        <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:#059669;margin-top:1rem;">
          Launch Calculator &rarr;
        </span>
      </a>

      <!-- 7. Macro Calculator -->
      <a href="macro-calculator.html" class="silo-card" style="border-top:3px solid #059669;">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;">
          <div class="silo-card-icon">🥗</div>
          <span class="silo-card-badge">AMDR &amp; ISSN</span>
        </div>
        <div class="silo-card-title">Macronutrient Split Calculator</div>
        <div class="silo-card-desc">Calculate daily protein, carbohydrate, and dietary fat gram targets based on training goals, body composition, and IIFYM splits.</div>
        <div class="formula-badge-pill">Atwater: 4C - 4P - 9F kcal/g</div>
        <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:#059669;margin-top:1rem;">
          Launch Calculator &rarr;
        </span>
      </a>
"""

if "bmr-calculator.html" not in health_content:
    health_content = health_content.replace('<strong>5</strong> Precision Tools', '<strong>7</strong> Precision Tools')
    health_content = health_content.replace('Available Health Calculators (5)', 'Available Health Calculators (7)')
    health_content = health_content.replace('</div>\n\n    <!-- Educational Guide -->', health_cards + '\n</div>\n\n    <!-- Educational Guide -->')
    health_content = health_content.replace('</div>\n    <!-- Educational Guide -->', health_cards + '\n</div>\n    <!-- Educational Guide -->')
    with open(health_path, "w", encoding="utf-8") as f:
        f.write(health_content)
    print("health.html updated!")

# 3. Update chemical.html
chemical_path = os.path.join(BASE_DIR, "chemical.html")
with open(chemical_path, "r", encoding="utf-8") as f:
    chemical_content = f.read()

chemical_cards = """
        <a href="chlorine-dosing-calculator.html" class="silo-card" style="border-top:3px solid #0D9488;">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;">
            <div class="silo-card-icon">💧</div>
            <span class="silo-card-badge">AWWA C651 &amp; EPA CT</span>
          </div>
          <div class="silo-card-title">Chlorine Dosing Calculator</div>
          <div class="silo-card-desc">Calculate pure Cl₂ mass, sodium hypochlorite bleach volume (12.5% &amp; 6%), or continuous metering pump rates per AWWA C651.</div>
          <div class="formula-badge-pill">Feed (lbs) = Vol (MGal) × Dose (mg/L) × 8.34</div>
          <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:#0D9488;margin-top:1rem;">
            Launch Calculator &rarr;
          </span>
        </a>
"""

if "chlorine-dosing-calculator.html" not in chemical_content:
    chemical_content = chemical_content.replace('<strong>1</strong> Certified Calculators', '<strong>2</strong> Certified Calculators')
    chemical_content = chemical_content.replace('Available Tools (1)', 'Available Tools (2)')
    chemical_content = chemical_content.replace('</div>\n\n    <!-- Educational Guide -->', chemical_cards + '\n</div>\n\n    <!-- Educational Guide -->')
    chemical_content = chemical_content.replace('</div>\n    <!-- Educational Guide -->', chemical_cards + '\n</div>\n    <!-- Educational Guide -->')
    with open(chemical_path, "w", encoding="utf-8") as f:
        f.write(chemical_content)
    print("chemical.html updated!")

# 4. Update engineering.html
eng_path = os.path.join(BASE_DIR, "engineering.html")
with open(eng_path, "r", encoding="utf-8") as f:
    eng_content = f.read()

eng_cards = """
      <!-- 7. Conduit Fill -->
      <a href="conduit-fill-calculator.html" class="silo-card" style="border-top:3px solid #D97706;">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;">
          <div class="silo-card-icon">🪢</div>
          <span class="silo-card-badge">NEC Ch. 9 Table 1 &amp; 4</span>
        </div>
        <div class="silo-card-title">Conduit Fill &amp; Jam Ratio Calculator</div>
        <div class="silo-card-desc">Calculate raceway area fill percentage for EMT, PVC, RMC, and FMC under the NEC 40% fill rule and check critical cable jamming ratios.</div>
        <div class="formula-badge-pill">Fill % = ∑(A_conductors) ÷ A_conduit ≤ 40%</div>
        <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:#D97706;margin-top:1rem;">
          Launch Calculator &rarr;
        </span>
      </a>

      <!-- 8. Motor Starting Current -->
      <a href="motor-starting-current-calculator.html" class="silo-card" style="border-top:3px solid #D97706;">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;">
          <div class="silo-card-icon">⚙️</div>
          <span class="silo-card-badge">NEMA MG 1 Code A-M</span>
        </div>
        <div class="silo-card-title">Motor Starting Current Calculator</div>
        <div class="silo-card-desc">Determine 3-phase induction motor locked rotor inrush amperes (LRA) across NEMA letters and evaluate DOL vs Soft-Starter voltage dips.</div>
        <div class="formula-badge-pill">LRA = (HP × kVA/HP × 1000) ÷ (√3 × V)</div>
        <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:#D97706;margin-top:1rem;">
          Launch Calculator &rarr;
        </span>
      </a>

      <!-- 9. Wire Ampacity -->
      <a href="wire-ampacity-calculator.html" class="silo-card" style="border-top:3px solid #D97706;">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;">
          <div class="silo-card-icon">🔌</div>
          <span class="silo-card-badge">NEC Table 310.16</span>
        </div>
        <div class="silo-card-title">Wire Ampacity &amp; Sizing Calculator</div>
        <div class="silo-card-desc">Determine allowable conductor current capacity with ambient temperature derating, conduit bundling factors, and NEC 110.14(C) terminal limits.</div>
        <div class="formula-badge-pill">I_adj = I_base × K_temp × K_bundle</div>
        <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:#D97706;margin-top:1rem;">
          Launch Calculator &rarr;
        </span>
      </a>
"""

if "wire-ampacity-calculator.html" not in eng_content:
    eng_content = re.sub(r'<strong>\d+</strong> Engineering Tools', '<strong>9</strong> Engineering Tools', eng_content)
    eng_content = re.sub(r'Available Engineering Calculators \(\d+\)', 'Available Engineering Calculators (9)', eng_content)
    eng_content = eng_content.replace('</div>\n\n    <!-- Educational & Engineering Guide -->', eng_cards + '\n</div>\n\n    <!-- Educational & Engineering Guide -->')
    eng_content = eng_content.replace('</div>\n    <!-- Educational & Engineering Guide -->', eng_cards + '\n</div>\n    <!-- Educational & Engineering Guide -->')
    with open(eng_path, "w", encoding="utf-8") as f:
        f.write(eng_content)
    print("engineering.html updated!")

# 5. Update finance.html
fin_path = os.path.join(BASE_DIR, "finance.html")
with open(fin_path, "r", encoding="utf-8") as f:
    fin_content = f.read()

fin_cards = """
      <!-- 8. Car Loan Calculator -->
      <a href="car-loan-calculator.html" class="silo-card" style="border-top:3px solid #2563EB;">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;">
          <div class="silo-card-icon">🚗</div>
          <span class="silo-card-badge">TILA Reg Z</span>
        </div>
        <div class="silo-card-title">Car Loan &amp; Auto Financing Calculator</div>
        <div class="silo-card-desc">Calculate monthly auto loan payments, trade-in sales tax savings, dealer documentation fees, and total lifetime interest financing costs.</div>
        <div class="formula-badge-pill">Auto EMI = [P·r·(1+r)ⁿ] / [(1+r)ⁿ - 1]</div>
        <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:#2563EB;margin-top:1rem;">
          Launch Calculator &rarr;
        </span>
      </a>

      <!-- 9. ROI Calculator -->
      <a href="roi-calculator.html" class="silo-card" style="border-top:3px solid #2563EB;">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;">
          <div class="silo-card-icon">📈</div>
          <span class="silo-card-badge">CFA Institute</span>
        </div>
        <div class="silo-card-title">ROI &amp; Annualized CAGR Calculator</div>
        <div class="silo-card-desc">Compute net investment percentage return, compound annualized growth rate (CAGR), multiple on invested capital (MOIC), and real return.</div>
        <div class="formula-badge-pill">ROI = (Gain - Cost) ÷ Cost × 100%</div>
        <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:#2563EB;margin-top:1rem;">
          Launch Calculator &rarr;
        </span>
      </a>

      <!-- 10. Rule of 72 Calculator -->
      <a href="rule-of-72-calculator.html" class="silo-card" style="border-top:3px solid #2563EB;">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;">
          <div class="silo-card-icon">📈</div>
          <span class="silo-card-badge">Compound Doubling</span>
        </div>
        <div class="silo-card-title">Rule of 72 Doubling Time Calculator</div>
        <div class="silo-card-desc">Estimate the exact number of years required to double, triple (Rule of 115), or quadruple your investment portfolio at any annual return.</div>
        <div class="formula-badge-pill">Years to Double ≈ 72 ÷ Return %</div>
        <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:#2563EB;margin-top:1rem;">
          Launch Calculator &rarr;
        </span>
      </a>
"""

if "rule-of-72-calculator.html" not in fin_content:
    fin_content = re.sub(r'<strong>\d+</strong> Certified Calculators', '<strong>10</strong> Certified Calculators', fin_content)
    fin_content = re.sub(r'Available Finance Calculators \(\d+\)', 'Available Finance Calculators (10)', fin_content)
    fin_content = re.sub(r'Available Tools \(\d+\)', 'Available Tools (10)', fin_content)
    fin_content = fin_content.replace('</div>\n\n    <!-- Educational Guide -->', fin_cards + '\n</div>\n\n    <!-- Educational Guide -->')
    fin_content = fin_content.replace('</div>\n    <!-- Educational Guide -->', fin_cards + '\n</div>\n    <!-- Educational Guide -->')
    with open(fin_path, "w", encoding="utf-8") as f:
        f.write(fin_content)
    print("finance.html updated!")

# 6. Update mechanical.html
mech_path = os.path.join(BASE_DIR, "mechanical.html")
with open(mech_path, "r", encoding="utf-8") as f:
    mech_content = f.read()

mech_cards = """
        <a href="pump-head-calculator.html" class="silo-card" style="border-top:3px solid #0891B2;">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;">
            <div class="silo-card-icon">🌊</div>
            <span class="silo-card-badge">Hydraulic Institute &amp; Crane</span>
          </div>
          <div class="silo-card-title">Pump Head (TDH) &amp; Power Calculator</div>
          <div class="silo-card-desc">Calculate Total Dynamic Head (TDH), static elevation lift, piping friction head loss, pump water horsepower, and motor brake power (BHP).</div>
          <div class="formula-badge-pill">TDH = Static Head + Friction Head</div>
          <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:#0891B2;margin-top:1rem;">
            Launch Calculator &rarr;
          </span>
        </a>

        <a href="gear-ratio-calculator.html" class="silo-card" style="border-top:3px solid #0891B2;">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;">
            <div class="silo-card-icon">⚙️</div>
            <span class="silo-card-badge">AGMA 908-B89 &amp; ISO 6336</span>
          </div>
          <div class="silo-card-title">Gear Ratio &amp; Speed Calculator</div>
          <div class="silo-card-desc">Determine gear train speed reduction, mechanical advantage, driven shaft torque multiplication, and compound gear set ratios.</div>
          <div class="formula-badge-pill">Ratio = Driven Teeth ÷ Driving Teeth</div>
          <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:#0891B2;margin-top:1rem;">
            Launch Calculator &rarr;
          </span>
        </a>
"""

if "pump-head-calculator.html" not in mech_content:
    mech_content = re.sub(r'<strong>\d+</strong> Certified Calculators', '<strong>5</strong> Certified Calculators', mech_content)
    mech_content = re.sub(r'Available Tools \(\d+\)', 'Available Tools (5)', mech_content)
    mech_content = mech_content.replace('</div>\n\n    <!-- Educational Guide -->', mech_cards + '\n</div>\n\n    <!-- Educational Guide -->')
    mech_content = mech_content.replace('</div>\n    <!-- Educational Guide -->', mech_cards + '\n</div>\n    <!-- Educational Guide -->')
    with open(mech_path, "w", encoding="utf-8") as f:
        f.write(mech_content)
    print("mechanical.html updated!")

# 7. Update math.html
math_path = os.path.join(BASE_DIR, "math.html")
with open(math_path, "r", encoding="utf-8") as f:
    math_content = f.read()

math_cards = """
      <!-- 6. Standard Deviation -->
      <a href="standard-deviation-calculator.html" class="silo-card" style="border-top:3px solid #7C3AED;">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;">
          <div class="silo-card-icon">📊</div>
          <span class="silo-card-badge">Bessel n-1 &amp; ISO</span>
        </div>
        <div class="silo-card-title">Standard Deviation &amp; Variance Calculator</div>
        <div class="silo-card-desc">Calculate sample standard deviation with Bessel's correction, population variance, mean, SEM, and sum of squares with step breakdown.</div>
        <div class="formula-badge-pill">s = √[ ∑(x - x̄)² ÷ (n - 1) ]</div>
        <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:#7C3AED;margin-top:1rem;">
          Launch Calculator &rarr;
        </span>
      </a>
"""

if "standard-deviation-calculator.html" not in math_content:
    math_content = re.sub(r'<strong>\d+</strong> Certified Calculators', '<strong>6</strong> Certified Calculators', math_content)
    math_content = re.sub(r'Available Mathematics Calculators \(\d+\)', 'Available Mathematics Calculators (6)', math_content)
    math_content = re.sub(r'Available Tools \(\d+\)', 'Available Tools (6)', math_content)
    math_content = math_content.replace('</div>\n\n    <!-- Educational & Math Guide -->', math_cards + '\n</div>\n\n    <!-- Educational & Math Guide -->')
    math_content = math_content.replace('</div>\n    <!-- Educational & Math Guide -->', math_cards + '\n</div>\n    <!-- Educational & Math Guide -->')
    with open(math_path, "w", encoding="utf-8") as f:
        f.write(math_content)
    print("math.html updated!")

# 8. Update index.html chips and cards
idx_path = os.path.join(BASE_DIR, "index.html")
with open(idx_path, "r", encoding="utf-8") as f:
    idx_content = f.read()

# Update chips
idx_content = idx_content.replace('>⚖️ Health (5)<', '>⚖️ Health (7)<')
idx_content = idx_content.replace('>🏦 Finance (9)<', '>🏦 Finance (10)<')
idx_content = idx_content.replace('>🔢 Math (5)<', '>🔢 Math (6)<')
idx_content = idx_content.replace('>⚡ Electrical (8)<', '>⚡ Electrical (9)<')
idx_content = idx_content.replace('>⚙️ Mechanical (3)<', '>⚙️ Mechanical (5)<')
idx_content = idx_content.replace('>🏗️ Civil (4)<', '>🏗️ Civil (6)<')
idx_content = idx_content.replace('>🧪 Chemical (1)<', '>🧪 Chemical (2)<')

# Update badges in category overview cards
idx_content = idx_content.replace('>5 Tools</span>\n        </div>\n        <div class="cat-card-title">Health & Fitness</div>', '>7 Tools</span>\n        </div>\n        <div class="cat-card-title">Health & Fitness</div>')
idx_content = idx_content.replace('>9 Tools</span>\n        </div>\n        <div class="cat-card-title">Finance & Investment</div>', '>10 Tools</span>\n        </div>\n        <div class="cat-card-title">Finance & Investment</div>')
idx_content = idx_content.replace('>5 Tools</span>\n        </div>\n        <div class="cat-card-title">Mathematics & Utilities</div>', '>6 Tools</span>\n        </div>\n        <div class="cat-card-title">Mathematics & Utilities</div>')
idx_content = idx_content.replace('>8 Tools</span>\n        </div>\n        <div class="cat-card-title">Electrical Engineering</div>', '>9 Tools</span>\n        </div>\n        <div class="cat-card-title">Electrical Engineering</div>')
idx_content = idx_content.replace('>4 Tools</span>\n        </div>\n        <div class="cat-card-title">Civil & Construction</div>', '>6 Tools</span>\n        </div>\n        <div class="cat-card-title">Civil & Construction</div>')
idx_content = idx_content.replace('>1 Tool</span>\n        </div>\n        <div class="cat-card-title">Chemical & Water</div>', '>2 Tools</span>\n        </div>\n        <div class="cat-card-title">Chemical & Water</div>')

with open(idx_path, "w", encoding="utf-8") as f:
    f.write(idx_content)
print("index.html updated!")

print("All hubs and index updated successfully!")
