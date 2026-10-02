import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def update_finance():
    fpath = os.path.join(BASE_DIR, "finance.html")
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    # Update counts
    html = re.sub(r'<strong>\d+</strong> Certified Calculators', '<strong>7</strong> Certified Calculators', html)
    html = re.sub(r'Available Financial Calculators \(\d+\)', 'Available Financial Calculators (7)', html)

    new_cards = '''
      <!-- 6. Mortgage Calculator -->
      <a href="mortgage-calculator.html" class="silo-card" style="border-top:3px solid #2563EB;">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;">
          <div class="silo-card-icon">🏡</div>
          <span class="silo-card-badge">PITI &amp; Amortization</span>
        </div>
        <div class="silo-card-title">Mortgage &amp; PITI Calculator</div>
        <div class="silo-card-desc">Calculate total monthly housing payments with principal, interest, property taxes, hazard insurance, PMI, and HOA fees.</div>
        <div class="formula-badge-pill">PITI = P&amp;I + Taxes + Insurance + PMI</div>
        <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:#2563EB;margin-top:1rem;">
          Launch Calculator &rarr;
        </span>
      </a>

      <!-- 7. Tip & Bill Splitter -->
      <a href="tip-calculator.html" class="silo-card" style="border-top:3px solid #2563EB;">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;">
          <div class="silo-card-icon">🍽️</div>
          <span class="silo-card-badge">Bill Splitter</span>
        </div>
        <div class="silo-card-title">Tip &amp; Bill Split Calculator</div>
        <div class="silo-card-desc">Compute restaurant gratuities, split checks evenly across dining parties, compare pre-tax vs post-tax etiquette, and round to nearest dollar.</div>
        <div class="formula-badge-pill">Tip = Subtotal × (Tip% ÷ 100)</div>
        <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:#2563EB;margin-top:1rem;">
          Launch Calculator &rarr;
        </span>
      </a>
'''
    if 'mortgage-calculator.html' not in html:
        html = re.sub(r'(<div class="silo-card-grid"[^>]*>.*?)(</div>\s*<!-- Educational)', r'\1' + new_cards + r'\2', html, flags=re.DOTALL)

    new_bullets = '''        <li>
          <a href="mortgage-calculator.html"><strong>Mortgage &amp; PITI Amortization Calculator</strong></a> — Computes comprehensive monthly homeownership obligations including Principal, Interest, Property Taxes, Hazard Insurance (PITI), Private Mortgage Insurance (PMI), and HOA dues. Simulates early principal prepayments, compares 15-year vs 30-year fixed loans, and models statutory PMI cancellation thresholds under the federal Homeowners Protection Act.
        </li>
        <li>
          <a href="tip-calculator.html"><strong>Tip &amp; Bill Split Calculator</strong></a> — Determines fair restaurant gratuities on pre-tax subtotal versus post-tax totals, splits dining checks across parties of any size, and applies currency rounding rules aligned with FLSA hospitality wage standards.
        </li>
'''
    m = re.search(r'<h3>Calculators in This Financial &amp; Investment Suite</h3>.*?<ul>', html, re.DOTALL)
    if m and 'mortgage-calculator.html' not in html[m.start():m.start()+800]:
        html = re.sub(r'(<h3>Calculators in This Financial &amp; Investment Suite</h3>\s*<p>.*?</p>\s*<ul>)', r'\1\n' + new_bullets, html, flags=re.DOTALL)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print("finance.html updated with Mortgage & Tip calculators.")

def update_electrical():
    fpath = os.path.join(BASE_DIR, "engineering.html")
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    # Update counts
    html = re.sub(r'<strong>\d+</strong> Certified Calculators', '<strong>6</strong> Certified Calculators', html)
    html = re.sub(r'Available Electrical Calculators \(\d+\)', 'Available Electrical Calculators (6)', html)

    new_cards = '''
      <!-- 5. Short-Circuit Calculator -->
      <a href="short-circuit-calculator.html" class="silo-card" style="border-top:3px solid #2563EB;">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;">
          <div class="silo-card-icon">💥</div>
          <span class="silo-card-badge">IEC 60909 Symmetrical</span>
        </div>
        <div class="silo-card-title">Short-Circuit Current Calculator</div>
        <div class="silo-card-desc">Calculate initial symmetrical short-circuit current (Ik''), peak dynamic current (ip), and switchgear breaking capacity per IEC 60909.</div>
        <div class="formula-badge-pill">Ik'' = c·Un / (√3·|Zk|)</div>
        <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:#2563EB;margin-top:1rem;">
          Launch Calculator &rarr;
        </span>
      </a>

      <!-- 6. Transformer Sizing -->
      <a href="transformer-sizing-calculator.html" class="silo-card" style="border-top:3px solid #2563EB;">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;">
          <div class="silo-card-icon">⚡</div>
          <span class="silo-card-badge">NEC 450 &amp; IEC 60076</span>
        </div>
        <div class="silo-card-title">Transformer Sizing &amp; FLC Calculator</div>
        <div class="silo-card-desc">Determine required transformer kVA rating, primary and secondary full-load currents (FLC), and overcurrent protection breaker limits.</div>
        <div class="formula-badge-pill">FLC = (kVA × 1000) / (√3 × V)</div>
        <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:#2563EB;margin-top:1rem;">
          Launch Calculator &rarr;
        </span>
      </a>
'''
    if 'short-circuit-calculator.html' not in html:
        html = re.sub(r'(<div class="silo-card-grid"[^>]*>.*?)(</div>\s*<!-- Educational)', r'\1' + new_cards + r'\2', html, flags=re.DOTALL)

    new_bullets = r'''        <li>
          <a href="short-circuit-calculator.html"><strong>Three-Phase Short-Circuit Current Calculator (IEC 60909)</strong></a> — Computes prospective symmetrical initial short-circuit currents ($I_k''$), peak dynamic current ($i_p$), and total short-circuit apparent power ($S_k''$) using the equivalent voltage source method. Evaluates transformer internal impedance ($Z_T$), upstream utility fault MVA, and downstream conductor attenuation to specify circuit breaker breaking capacity ($I_{cu} / I_{cs}$) under IEC 60947-2.
        </li>
        <li>
          <a href="transformer-sizing-calculator.html"><strong>Transformer Sizing &amp; Full-Load Current Calculator (NEC 450)</strong></a> — Sizes commercial and industrial power distribution transformers in standard kVA increments. Computes primary and secondary Full-Load Currents (FLC), applies demand diversity factors and continuous operating margins, and verifies maximum allowable overcurrent protective device (OCPD) ratings per NEC Table 450.3.
        </li>
'''
    m = re.search(r'<h3>Calculators in This Electrical Engineering Suite</h3>.*?<ul>', html, re.DOTALL)
    if m and 'short-circuit-calculator.html' not in html[m.start():m.start()+800]:
        html = re.sub(r'(<h3>Calculators in This Electrical Engineering Suite</h3>\s*<p>.*?</p>\s*<ul>)', lambda m: m.group(1) + '\n' + new_bullets, html, flags=re.DOTALL)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print("engineering.html updated with Short-Circuit & Transformer calculators.")

def update_civil():
    fpath = os.path.join(BASE_DIR, "civil.html")
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    html = re.sub(r'<strong>\d+</strong> Certified Calculators', '<strong>4</strong> Certified Calculators', html)
    html = re.sub(r'Available Tools \(\d+\)', 'Available Tools (4)', html)

    new_cards = '''
        <a href="beam-deflection-calculator.html" class="silo-card" style="border-top:3px solid #D97706;">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;">
            <div class="silo-card-icon">📐</div>
            <span class="silo-card-badge">AISC 360 &amp; Eurocode 3</span>
          </div>
          <div class="silo-card-title">Beam Deflection &amp; Bending Moments</div>
          <div class="silo-card-desc">Calculate maximum elastic deflection (δmax), bending moment (Mmax), and shear force across simply supported and cantilever beams.</div>
          <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:#D97706;margin-top:1rem;">
            Launch Calculator &rarr;
          </span>
        </a>

        <a href="retaining-wall-calculator.html" class="silo-card" style="border-top:3px solid #D97706;">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;">
            <div class="silo-card-icon">🧱</div>
            <span class="silo-card-badge">Rankine &amp; ACI 318</span>
          </div>
          <div class="silo-card-title">Cantilever Retaining Wall Stability</div>
          <div class="silo-card-desc">Analyze lateral active earth pressure, safety factors against overturning and sliding, and foundation soil bearing pressures.</div>
          <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:#D97706;margin-top:1rem;">
            Launch Calculator &rarr;
          </span>
        </a>
'''
    if 'beam-deflection-calculator.html' not in html:
        html = re.sub(r'(<div class="silo-card-grid"[^>]*>.*?)(</div>\s*<!-- Educational)', r'\1' + new_cards + r'\2', html, flags=re.DOTALL)

    new_bullets = r'''        <li>
          <a href="beam-deflection-calculator.html"><strong>Beam Deflection &amp; Flexural Moment Calculator</strong></a> — Implements classical Euler-Bernoulli fourth-order elastic bending theory to compute maximum deflections ($\delta_{\max}$), bending moments ($M_{\max}$), and shear reactions across simply supported and cantilever beams under point and uniformly distributed loads. Verifies Serviceability Limit State (SLS) span-to-deflection ratios ($L/250$ and $L/360$) under AISC 360 and Eurocode 3.
        </li>
        <li>
          <a href="retaining-wall-calculator.html"><strong>Cantilever Retaining Wall Stability Calculator</strong></a> — Resolves Rankine active earth pressure thrust ($P_a$) and verifies geotechnical equilibrium limit states for reinforced concrete cantilever walls. Computes factors of safety against overturning ($FS \ge 1.50$), base sliding, and eccentric soil bearing pressure distributions under ACI 318-19 and IBC Chapter 18.
        </li>
'''
    m = re.search(r'<h3>Calculators in This Civil &amp; Structural Engineering Suite</h3>.*?<ul>', html, re.DOTALL)
    if m and 'beam-deflection-calculator.html' not in html[m.start():m.start()+800]:
        html = re.sub(r'(<h3>Calculators in This Civil &amp; Structural Engineering Suite</h3>\s*<p>.*?</p>\s*<ul>)', lambda m: m.group(1) + '\n' + new_bullets, html, flags=re.DOTALL)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print("civil.html updated with Beam Deflection & Retaining Wall calculators.")

def update_fire_safety():
    fpath = os.path.join(BASE_DIR, "fire-safety.html")
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    html = re.sub(r'<strong>\d+</strong> Certified Calculators', '<strong>2</strong> Certified Calculators', html)
    html = re.sub(r'Available Tools \(\d+\)', 'Available Tools (2)', html)

    new_cards = '''
        <a href="fire-sprinkler-calculator.html" class="silo-card" style="border-top:3px solid #E11D48;">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;">
            <div class="silo-card-icon">💦</div>
            <span class="silo-card-badge">NFPA 13 Hydraulics</span>
          </div>
          <div class="silo-card-title">Fire Sprinkler Hydraulic &amp; Flow</div>
          <div class="silo-card-desc">Calculate individual sprinkler head discharge flow (Q = K√P), total system water demand, hose allowance, and storage tank volume.</div>
          <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:#E11D48;margin-top:1rem;">
            Launch Calculator &rarr;
          </span>
        </a>
'''
    if 'fire-sprinkler-calculator.html' not in html:
        html = re.sub(r'(<div class="silo-card-grid"[^>]*>.*?)(</div>\s*<!-- Educational)', r'\1' + new_cards + r'\2', html, flags=re.DOTALL)

    new_bullets = r'''        <li>
          <a href="fire-sprinkler-calculator.html"><strong>Fire Sprinkler Hydraulic &amp; Flow Rate Calculator (NFPA 13)</strong></a> — Computes individual head discharge flow rates ($Q = K\sqrt{P}$) across standard orifice K-factors ($K=5.6$ through $K=25.2$ ESFR). Sizes system water demand using the NFPA 13 Density/Area method, adds required fire hose stream allowances, and determines minimum fire protection water storage tank capacity under NFPA 22.
        </li>
'''
    m = re.search(r'<h3>Calculators in This Fire Protection &amp; Life Safety Suite</h3>.*?<ul>', html, re.DOTALL)
    if m and 'fire-sprinkler-calculator.html' not in html[m.start():m.start()+800]:
        html = re.sub(r'(<h3>Calculators in This Fire Protection &amp; Life Safety Suite</h3>\s*<p>.*?</p>\s*<ul>)', lambda m: m.group(1) + '\n' + new_bullets, html, flags=re.DOTALL)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print("fire-safety.html updated with Fire Sprinkler calculator.")

if __name__ == "__main__":
    update_finance()
    update_electrical()
    update_civil()
    update_fire_safety()
