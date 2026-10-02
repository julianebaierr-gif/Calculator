"""
Generates battery-life-calculator.html and pv-string-sizing-calculator.html
Each tool includes:
- 1,200+ words of deep engineering content
- Exact keyword matching in title, meta description, and H1
- KaTeX mathematical formulas
- Interactive JS calculation engine
- Reference engineering lookup tables
- Worked real-world case study example card
- Schema.org SoftwareApplication and FAQPage JSON-LD
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ==========================================
# 1. BATTERY LIFE CALCULATOR
# ==========================================
TOOL_BATTERY_LIFE = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Battery Life Calculator — Runtime Hours &amp; Peukert's Law Discharge</title>
  <meta name="description" content="Calculate battery runtime hours, discharge current C-rate, and Peukert capacity derating for Lithium-ion, LiFePO4, AGM, and lead-acid battery banks under DC load.">
  <meta name="keywords" content="battery life calculator, battery runtime calculator, battery discharge time, peukert's law calculator, mah to hours calculator, battery ah runtime, lithium vs lead acid discharge">
  <link rel="canonical" href="https://calchub.org/battery-life-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "Electrochemical Battery Runtime & Peukert Law Calculator",
        "operatingSystem": "All",
        "applicationCategory": "EngineeringApplication",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
        "description": "Calculates battery runtime hours, available discharge capacity, Peukert derating factor, and C-rate for portable electronics and energy storage systems."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "How is battery runtime calculated from capacity (Ah) and load (Amps)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Nominal battery runtime is standardly calculated using: T = (Capacity in Ah × Depth of Discharge × Efficiency) / Load Current in Amperes. For instance, a 100 Ah battery discharged to 80% DoD powering a 5 Amp DC load with 95% inverter efficiency delivers: (100 × 0.80 × 0.95) / 5 = 15.2 hours of continuous runtime."
            }
          },
          {
            "@type": "Question",
            "name": "What is Peukert's Law and why does it reduce lead-acid battery runtime at high currents?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Formulated by Wilhelm Peukert in 1897, Peukert's Law states that available battery capacity decreases non-linearly as discharge rate increases: C_p = I^k × t, where k is the Peukert exponent (typically 1.15 to 1.30 for lead-acid batteries, but nearly ideal 1.02 to 1.05 for Lithium Iron Phosphate). At heavy discharge rates, slow acid diffusion inside lead-acid plates starves the active material of sulfate ions, reducing delivered energy by over 40%."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between Depth of Discharge (DoD) for Lithium vs Lead-Acid?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Deep-cycle Lead-Acid (FLA/AGM/Gel) batteries should rarely be discharged beyond 50% Depth of Discharge (DoD) to avoid accelerating sulfation and slashing cycle life below 500 cycles. In contrast, modern Lithium Iron Phosphate (LiFePO4) and Lithium-ion chemistry can safely operate at 80% to 95% DoD while delivering 3,000 to 6,000 charge-discharge cycles."
            }
          },
          {
            "@type": "Question",
            "name": "How do you calculate battery runtime when load is specified in Watts instead of Amps?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Convert load power in Watts to DC current using Ohm's Law: Current (A) = Power (W) / Nominal Battery Voltage (V). For example, a 120 Watt DC load operating on a 12V battery bank draws: 120 W / 12 V = 10 Amperes. If an AC inverter is used, divide the current by inverter efficiency (typically 0.88 to 0.94) to account for DC-to-AC conversion losses."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body class="cat-theme-engineering">

  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="brand-logo">
        <span class="logo-badge">∑</span>
        <span>Calc<span class="accent">Hub</span></span>
      </a>
      <nav class="header-nav" aria-label="Main Navigation">
        <div class="nav-row">
          <a href="index.html" class="nav-link">🏠 Home</a>
          <a href="engineering.html" class="nav-link active">⚡ Electrical</a>
          <a href="mechanical.html" class="nav-link">⚙️ Mechanical</a>
          <a href="civil.html" class="nav-link">🏗️ Civil</a>
          <a href="finance.html" class="nav-link">🏦 Finance</a>
          <a href="math.html" class="nav-link">🔢 Math</a>
          <a href="chemical.html" class="nav-link">🧪 Chemical</a>
        </div>
        <div class="nav-row">
          <a href="health.html" class="nav-link">⚖️ Health</a>
          <a href="solar-energy.html" class="nav-link">☀️ Solar</a>
          <a href="fire-safety.html" class="nav-link">🚨 Fire &amp; Safety</a>
          <a href="programmer.html" class="nav-link">👨‍💻 Programmer</a>
          <a href="datetime.html" class="nav-link">📅 Date &amp; Time</a>
          <a href="converter.html" class="nav-link">🔄 Converter</a>
        </div>
      </nav>
    </div>
  </header>

  <div class="calc-page-header">
    <div class="calc-page-header-inner">
      <span class="category-tag">⚡ Electrochemical Energy Storage &amp; Electronics</span>
      <h1 class="calc-page-title">Battery Life Calculator</h1>
      <p class="calc-page-desc">Calculate battery runtime in hours and days, discharge C-rate, and available watt-hour capacity for Lithium LiFePO4, AGM, and lead-acid chemistries using Peukert's law.</p>
    </div>
  </div>

  <div class="layout-container" style="display:flex;gap:2rem;max-width:1200px;margin:2rem auto;padding:0 1.25rem;align-items:start;">
    
    <main style="flex:1;min-width:0;">
      <div class="calculator-workspace">
        <section class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title"><span>🔋</span> Battery &amp; Electrical Load Setup</h2>
            <span class="status-info">Electrochemical Modeling</span>
          </div>
          <form id="battery-form" onsubmit="return false;">
            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="batt-chemistry">Battery Chemistry &amp; Peukert Exponent</label>
                <select id="batt-chemistry" class="form-control" onchange="applyChemistryDefaults()">
                  <option value="lifepo4" data-k="1.04" data-dod="0.90" data-v="12.8" selected>Lithium Iron Phosphate (LiFePO4 / k = 1.04 / 90% DoD)</option>
                  <option value="li-ion" data-k="1.05" data-dod="0.80" data-v="3.7">Lithium-Ion / LiPo (Cell 3.7V / k = 1.05 / 80% DoD)</option>
                  <option value="agm" data-k="1.15" data-dod="0.50" data-v="12.0">AGM / Gel Deep Cycle (k = 1.15 / 50% DoD)</option>
                  <option value="fla" data-k="1.25" data-dod="0.50" data-v="12.0">Flooded Lead-Acid (Golf Cart / k = 1.25 / 50% DoD)</option>
                </select>
              </div>
              <div class="form-group">
                <label class="form-label" for="batt-capacity">Nominal Capacity (Ah)</label>
                <input type="number" id="batt-capacity" class="form-control" value="100" min="0.1" max="10000" step="1" oninput="runBatteryCalc()">
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="batt-voltage">Nominal Pack Voltage (V DC)</label>
                <input type="number" id="batt-voltage" class="form-control" value="12.8" min="1.2" max="1000" step="0.1" oninput="runBatteryCalc()">
              </div>
              <div class="form-group">
                <label class="form-label" for="load-type">Load Specification Method</label>
                <select id="load-type" class="form-control" onchange="runBatteryCalc()">
                  <option value="current" selected>Discharge Current (Amperes / A)</option>
                  <option value="power">Continuous Power (Watts / W)</option>
                  <option value="milliamps">Low Power Electronics (Milliamps / mA)</option>
                </select>
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="load-value">Load Value (Amps, Watts, or mA)</label>
                <input type="number" id="load-value" class="form-control" value="10" min="0.001" max="5000" step="0.5" oninput="runBatteryCalc()">
              </div>
              <div class="form-group">
                <label class="form-label" for="depth-of-discharge">Target Depth of Discharge (DoD %)</label>
                <input type="number" id="depth-of-discharge" class="form-control" value="90" min="10" max="100" step="5" oninput="runBatteryCalc()">
              </div>
            </div>

            <div class="calc-actions" style="margin-top:1.5rem;display:flex;gap:1rem;">
              <button type="button" class="btn btn-primary" onclick="runBatteryCalc()">Calculate Battery Runtime</button>
              <button type="button" class="btn btn-secondary" onclick="window.print()">🖨️ Print Discharge Analysis</button>
            </div>
          </form>
        </section>

        <section class="results-card">
          <h2 class="results-title">Discharge Runtime &amp; Energy Analysis</h2>
          
          <div class="primary-result-box" style="margin-bottom:1.5rem;text-align:center;padding:1.5rem;border-radius:12px;background:#F8FAFC;border:2px solid #E2E8F0;">
            <div class="primary-result-label" style="font-size:0.9rem;text-transform:uppercase;letter-spacing:0.05em;color:#64748B;">Estimated Battery Runtime</div>
            <div id="res-runtime-primary" class="primary-result-value" style="font-size:2.5rem;font-weight:800;color:#0F172A;margin:0.25rem 0;">8 Hours 41 Minutes</div>
            <div id="res-runtime-sub" style="font-size:1.05rem;color:#059669;font-weight:700;">8.68 Decimal Hours (0.36 Days Continuous)</div>
          </div>

          <div class="result-details-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;">
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Effective Delivered Capacity</span>
              <span id="res-eff-capacity" class="result-val" style="font-size:1.1rem;font-weight:700;color:#2563EB;">86.8 Ah (90% DoD)</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Total Usable Energy</span>
              <span id="res-usable-energy" class="result-val" style="font-size:1.1rem;font-weight:700;color:#0F172A;">1,111 Watt-hours (1.11 kWh)</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Discharge C-Rate</span>
              <span id="res-c-rate" class="result-val" style="font-size:1.1rem;font-weight:700;color:#0F172A;">0.10 C (10h Rate)</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Peukert Derating Loss</span>
              <span id="res-peukert-loss" class="result-val" style="font-size:1.1rem;font-weight:700;color:#475569;">3.2% Capacity Loss</span>
            </div>
          </div>

          <div style="margin-top:1.25rem;padding:0.85rem;border-radius:8px;background:#F0FDF4;border:1px solid #BBF7D0;font-size:0.85rem;color:#166534;">
            <strong>☀️ Renewable Integration:</strong> Sizing an off-grid solar system? Calculate your required array with our <a href="solar-panel-sizing-calculator.html" style="color:#166534;font-weight:700;">Solar Panel Sizing Calculator</a> and backup storage with the <a href="solar-battery-bank-calculator.html" style="color:#166534;font-weight:700;">Solar Battery Bank Calculator</a>.
          </div>
        </section>
      </div>

      <article class="educational-content" style="margin-top:3rem;line-height:1.7;color:#334155;">
        <h2>The Physics of Battery Discharge: Peukert's Law &amp; Chemistry Dynamics</h2>
        <p>In electrical engineering, estimating the operational autonomy of battery-powered systems requires more than simply dividing nominal Ampere-hour capacity by load amperage. An electrochemical battery is not an ideal bucket of coulombs that pours out energy at a 100% constant rate regardless of discharge velocity. Instead, chemical reaction kinetics, internal series resistance ($R_{int}$), and ion diffusion rates across the electrolyte fundamentally dictate how much usable energy can be extracted before cell voltage collapses below its minimum low-voltage cutoff threshold.</p>

        <p>In 1897, German scientist Wilhelm Peukert discovered that as the discharge current increases, the available capacity of a lead-acid battery diminishes exponentially. This phenomenon is modeled mathematically by <strong>Peukert's Law</strong>, and it explains why a 100 Ah deep-cycle battery can power a 5-Amp load for 20 hours (delivering 100 Ah), but will collapse in under 18 minutes if discharged at 200 Amps (delivering only 60 Ah of useful energy).</p>

        <h2>Mathematical Discharge &amp; Runtime Formulations</h2>

        <h3>1. The Classical Peukert Equation</h3>
        <p>Peukert's equation relates discharge current to discharge duration:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #2563EB;">
          $$C_p = I^k \cdot t$$
        </div>
        <p>Where:</p>
        <ul>
          <li><strong>$C_p$</strong> = Peukert capacity constant for the battery.</li>
          <li><strong>$I$</strong> = Discharge current in Amperes.</li>
          <li><strong>$t$</strong> = Time to full discharge in hours.</li>
          <li><strong>$k$</strong> = Peukert exponent (dimensionless parameter characterizing internal electrochemical resistance).</li>
        </ul>

        <p>When normalized against the standard manufacturer rating duration ($H$, typically the $20\text{-hour}$ rating for deep-cycle batteries or $1\text{-hour}$ for Lithium), the effective runtime $t$ under load current $I$ is calculated as:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #059669;">
          $$t = H \cdot \left( \frac{C_{\text{rated}}}{I \cdot H} \right)^k \cdot \text{DoD}$$
        </div>

        <h3>2. Conversion Between Electrical Load Units</h3>
        <p>When consumer devices specify continuous load in Watts ($P$) rather than Amps ($I$), current drawn from the DC bus is calculated via Ohm's Law:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #7C3AED;">
          $$I = \frac{P}{V_{\text{nominal}} \cdot \eta_{\text{inverter}}}$$
        </div>
        <p>Where $\eta_{\text{inverter}}$ represents DC-to-AC power inverter conversion efficiency (typically $0.88$ to $0.94$).</p>

        <h2>Electrochemical Battery Chemistry Comparison Table</h2>
        <p>Different rechargeable chemistries exhibit radically different Peukert exponents, usable depths of discharge, and thermal tolerances:</p>

        <div class="table-responsive" style="overflow-x:auto;margin:1.5rem 0;">
          <table class="table-custom" style="width:100%;border-collapse:collapse;border:1px solid #E2E8F0;">
            <thead style="background:#F8FAFC;">
              <tr style="border-bottom:2px solid #CBD5E1;text-align:left;">
                <th style="padding:0.75rem;">Battery Chemistry</th>
                <th style="padding:0.75rem;">Peukert Exponent ($k$)</th>
                <th style="padding:0.75rem;">Recommended DoD</th>
                <th style="padding:0.75rem;">Cycle Life</th>
                <th style="padding:0.75rem;">Round-Trip Efficiency</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>Lithium Iron Phosphate (LiFePO4)</strong></td>
                <td style="padding:0.75rem;">1.02 – 1.05</td>
                <td style="padding:0.75rem;">80% – 95%</td>
                <td style="padding:0.75rem;">3,500 – 6,000 cycles</td>
                <td style="padding:0.75rem;">95% – 98%</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>Lithium-Ion / Li-Polymer (NMC/LCO)</strong></td>
                <td style="padding:0.75rem;">1.04 – 1.08</td>
                <td style="padding:0.75rem;">80%</td>
                <td style="padding:0.75rem;">800 – 1,500 cycles</td>
                <td style="padding:0.75rem;">92% – 95%</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>AGM Deep-Cycle Sealed Lead-Acid</strong></td>
                <td style="padding:0.75rem;">1.12 – 1.18</td>
                <td style="padding:0.75rem;">50%</td>
                <td style="padding:0.75rem;">400 – 700 cycles</td>
                <td style="padding:0.75rem;">80% – 85%</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>Flooded Lead-Acid (Wet Cell)</strong></td>
                <td style="padding:0.75rem;">1.20 – 1.30</td>
                <td style="padding:0.75rem;">50%</td>
                <td style="padding:0.75rem;">300 – 500 cycles</td>
                <td style="padding:0.75rem;">75% – 80%</td>
              </tr>
              <tr>
                <td style="padding:0.75rem;"><strong>Nickel-Metal Hydride (NiMH)</strong></td>
                <td style="padding:0.75rem;">1.10 – 1.15</td>
                <td style="padding:0.75rem;">70%</td>
                <td style="padding:0.75rem;">500 – 1,000 cycles</td>
                <td style="padding:0.75rem;">65% – 70%</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="worked-example-card" style="background:#F8FAFC;border:2px solid #E2E8F0;border-radius:12px;padding:1.5rem;margin:2rem 0;">
          <h3 style="margin-top:0;color:#0F172A;display:flex;align-items:center;gap:0.5rem;">
            <span>📋</span> Real-World Engineering Worked Example: Marine Inverter System
          </h3>
          <p><strong>Scenario:</strong> A cruising sailboat installs a $12\text{V}$, $200\text{ Ah}$ AGM battery bank ($k = 1.15$, rated at the $20\text{-hr}$ rate). The boat operates a $360\text{ Watt}$ refrigeration compressor powered by an inverter ($\eta = 0.90$). The owner limits discharge to $50\%$ DoD to maximize battery bank longevity.</p>

          <ol style="padding-left:1.25rem;line-height:1.8;">
            <li><strong>Calculate DC Current Drawn from the Battery Bank:</strong>
              $$I = \frac{360\text{ W}}{12\text{ V} \times 0.90} = \frac{360}{10.8} = 33.33\text{ Amperes}$$
            </li>
            <li><strong>Determine the C-Rate:</strong>
              $$\text{C-Rate} = \frac{33.33\text{ A}}{200\text{ Ah}} \approx 0.167\text{ C} \quad (\approx 6\text{-hour discharge rate})$$
            </li>
            <li><strong>Apply Peukert's Formulation ($H = 20\text{ hrs}$):</strong>
              $$\text{Full Discharge Time } t_{\text{full}} = 20 \times \left( \frac{200}{33.33 \times 20} \right)^{1.15} = 20 \times \left( \frac{200}{666.6} \right)^{1.15} = 20 \times (0.300)^{1.15} \approx 5.01\text{ Hours}$$
            </li>
            <li><strong>Apply Depth of Discharge ($50\%$ DoD):</strong>
              $$\text{Usable Autonomy} = 5.01\text{ hrs} \times 0.50 \approx 2.50\text{ Hours } (2\text{h } 30\text{m})$$
            </li>
            <li><strong>Comparison with Lithium:</strong> If the owner replaces the AGM bank with a $200\text{ Ah}$ LiFePO4 battery ($k = 1.04$, usable at $90\%$ DoD), the usable runtime increases to $5.4\text{ hours}$—more than double the autonomy for the exact same nameplate Ah rating!</li>
          </ol>
        </div>

        <h2>Frequently Asked Technical Questions</h2>
        <div class="faq-accordion" style="margin-top:1.5rem;">
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">Why doesn't Lithium LiFePO4 suffer from Peukert's capacity loss?</h4>
            <p style="margin:0;color:#64748B;">Lithium Iron Phosphate cells utilize solid-state intercalation of lithium ions into olivine crystalline iron-phosphate cathode structures. Because lithium ions have exceptionally high mobility and the cells have near-negligible internal resistance compared to lead-acid liquid sulfuric acid dissociation, the Peukert exponent of LiFePO4 is nearly ideal (k ≈ 1.02 to 1.04), allowing the cell to deliver ~98% of its capacity even at a rapid 1C (1-hour) discharge rate.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">How does ambient cold temperature affect battery runtime?</h4>
            <p style="margin:0;color:#64748B;">Electrochemical reaction kinetics slow down significantly at low temperatures. At 0°C (32°F), a standard AGM or lead-acid battery delivers only about 75% to 80% of its rated capacity. At -20°C (-4°F), usable capacity falls below 50%. Furthermore, lithium batteries must never be recharged at temperatures below freezing (0°C) without internal heating blankets, as doing so causes permanent metallic lithium plating and internal short circuits.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">What is the relationship between C-rate and battery life expectancy?</h4>
            <p style="margin:0;color:#64748B;">The C-rate is the discharge current normalized to rated capacity (e.g., discharging a 100 Ah battery at 50 Amps is 0.5C). High continuous C-rates (&gt; 1C) generate internal ohmic I²R heating, which elevates internal cell temperatures, accelerates electrolyte breakdown, and degrades the solid-electrolyte interphase (SEI) layer, substantially reducing total cumulative lifetime cycles.</p>
          </div>
          <div class="faq-item" style="padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">How do you convert milliamp-hours (mAh) to Watt-hours (Wh)?</h4>
            <p style="margin:0;color:#64748B;">To convert milliamp-hours to Watt-hours, multiply the mAh by nominal cell voltage in Volts and divide by 1,000: Wh = (mAh × V) / 1000. For example, a 5,000 mAh smartphone battery operating at a nominal 3.85V contains: (5000 × 3.85) / 1000 = 19.25 Watt-hours of total electrochemical energy.</p>
          </div>
        </div>
      </article>
    </main>

    <aside class="sidebar" style="width:300px;flex-shrink:0;">
      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;margin-bottom:1.5rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">⚡ Electrical Energy Suite</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="battery-life-calculator.html" style="font-weight:700;color:#2563EB;">🔋 Battery Life &amp; Runtime</a></li>
          <li><a href="solar-battery-bank-calculator.html" style="color:#475569;">🔋 Solar Battery Bank Sizing</a></li>
          <li><a href="ohms-law-calculator.html" style="color:#475569;">⚡ Ohm's Law Calculator</a></li>
          <li><a href="voltage-drop-calculator.html" style="color:#475569;">📉 Voltage Drop Calculator</a></li>
          <li><a href="wire-ampacity-calculator.html" style="color:#475569;">🔌 Wire Ampacity (NEC)</a></li>
        </ul>
      </div>

      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">☀️ Solar &amp; Renewable Tools</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="solar-panel-sizing-calculator.html" style="color:#475569;">☀️ Solar Panel Sizing</a></li>
          <li><a href="solar-inverter-sizing-calculator.html" style="color:#475569;">⚡ Solar Inverter Sizing</a></li>
          <li><a href="ev-charging-time-calculator.html" style="color:#475569;">🔌 EV Charging Time &amp; Power</a></li>
        </ul>
      </div>
    </aside>

  </div>

  <footer class="site-footer" style="background:#0F172A;color:#94A3B8;padding:3rem 1.25rem;margin-top:4rem;">
    <div style="max-width:1200px;margin:0 auto;display:flex;justify-content:space-between;flex-wrap:wrap;gap:2rem;">
      <div>
        <div style="font-size:1.25rem;font-weight:800;color:#FFFFFF;margin-bottom:0.5rem;">CalcHub</div>
        <p style="font-size:0.88rem;max-width:320px;">Open-source engineering, financial, and scientific computational tools. 100% verified mathematics.</p>
      </div>
      <div>
        <div style="font-weight:700;color:#FFFFFF;margin-bottom:0.75rem;">Electrochemical Standards</div>
        <div style="font-size:0.85rem;line-height:2;">
          IEC 62619 Secondary Lithium Cells<br>
          IEEE 485 Stationary Battery Sizing<br>
          UL 1973 Energy Storage Systems
        </div>
      </div>
    </div>
    <div style="max-width:1200px;margin:2rem auto 0;padding-top:1.5rem;border-top:1px solid #1E293B;text-align:center;font-size:0.82rem;">
      &copy; 2026 CalcHub. Professional Electrochemical &amp; Power Storage Suite.
    </div>
  </footer>

  <script>
    function applyChemistryDefaults() {
      const chem = document.getElementById('batt-chemistry');
      const opt = chem.options[chem.selectedIndex];
      const dod = parseFloat(opt.dataset.dod) * 100;
      const v = parseFloat(opt.dataset.v);

      document.getElementById('depth-of-discharge').value = dod;
      document.getElementById('batt-voltage').value = v;
      runBatteryCalc();
    }

    function runBatteryCalc() {
      const chem = document.getElementById('batt-chemistry');
      const opt = chem.options[chem.selectedIndex];
      const k = parseFloat(opt.dataset.k) || 1.05;

      const cRated = Math.max(0.01, parseFloat(document.getElementById('batt-capacity').value) || 100);
      const vNom = Math.max(0.5, parseFloat(document.getElementById('batt-voltage').value) || 12.8);
      const loadType = document.getElementById('load-type').value;
      const loadVal = Math.max(0.0001, parseFloat(document.getElementById('load-value').value) || 10);
      const dodPct = Math.min(100, Math.max(5, parseFloat(document.getElementById('depth-of-discharge').value) || 90));
      const dodFrac = dodPct / 100.0;

      // Determine load current in Amperes
      let iLoad = 10;
      if (loadType === 'current') {
        iLoad = loadVal;
      } else if (loadType === 'power') {
        iLoad = loadVal / vNom;
      } else if (loadType === 'milliamps') {
        iLoad = loadVal / 1000.0;
      }

      const H = (opt.value === 'lifepo4' || opt.value === 'li-ion') ? 1.0 : 20.0;

      // Peukert calculation: t = H * (C_rated / (I * H))^k * DoD
      let hours = 0;
      if (Math.abs(k - 1.0) < 0.001) {
        hours = (cRated / iLoad) * dodFrac;
      } else {
        const ratio = cRated / (iLoad * H);
        hours = H * Math.pow(ratio, k) * dodFrac;
      }

      if (hours < 0 || isNaN(hours)) hours = 0;

      const totalMinutes = Math.round(hours * 60);
      const hPart = Math.floor(totalMinutes / 60);
      const mPart = totalMinutes % 60;
      const days = hours / 24.0;

      // Usable energy
      const usableWh = cRated * vNom * dodFrac;
      const cRate = iLoad / cRated;

      // Theoretical linear hours vs Peukert hours
      const linearHours = (cRated / iLoad) * dodFrac;
      const peukertLossPct = linearHours > 0 ? Math.max(0, ((linearHours - hours) / linearHours) * 100) : 0;

      let runtimeStr = '';
      if (hours < 1) {
        runtimeStr = totalMinutes + ' Minutes';
      } else if (hours < 48) {
        runtimeStr = hPart + ' Hours ' + mPart + ' Minutes';
      } else {
        runtimeStr = days.toFixed(1) + ' Days (' + Math.round(hours) + ' Hours)';
      }

      document.getElementById('res-runtime-primary').textContent = runtimeStr;
      document.getElementById('res-runtime-sub').textContent = hours.toFixed(2) + ' Decimal Hours (' + days.toFixed(2) + ' Days Continuous)';
      document.getElementById('res-eff-capacity').textContent = (cRated * dodFrac).toFixed(1) + ' Ah (' + dodPct + '% DoD)';
      document.getElementById('res-usable-energy').textContent = Math.round(usableWh).toLocaleString() + ' Wh (' + (usableWh / 1000).toFixed(2) + ' kWh)';
      document.getElementById('res-c-rate').textContent = cRate.toFixed(3) + ' C (' + (1/cRate).toFixed(1) + 'h Rate)';
      document.getElementById('res-peukert-loss').textContent = peukertLossPct.toFixed(1) + '% Peukert Loss';
    }

    window.addEventListener('DOMContentLoaded', runBatteryCalc);
  </script>
</body>
</html>
"""

# ==========================================
# 2. PV STRING SIZING CALCULATOR
# ==========================================
TOOL_PV_STRING = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PV String Sizing Calculator — MPPT Voltage Window &amp; NEC 690 Limits</title>
  <meta name="description" content="Calculate minimum and maximum solar panels per series string based on inverter MPPT voltage windows, extreme site temperatures, and NEC 690 maximum DC voltage limits.">
  <meta name="keywords" content="pv string sizing calculator, solar string calculator, mppt voltage window calculator, nec 690 string sizing, solar panels per string, voc temperature coefficient, inverter mppt string sizing">
  <link rel="canonical" href="https://calchub.org/pv-string-sizing-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "Solar PV Inverter String Sizing Calculator",
        "operatingSystem": "All",
        "applicationCategory": "EngineeringApplication",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
        "description": "Calculates allowable series solar module counts per string to satisfy inverter MPPT operational limits and NEC 690.7 maximum voltage constraints."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "How does temperature affect solar panel voltage (Voc and Vmp)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Silicon photovoltaic cells have a negative temperature coefficient of voltage (typically -0.26% to -0.30% / °C for Voc). As cell temperature drops during cold winter mornings, open-circuit voltage rises sharply, risking inverter over-voltage damage. Conversely, on scorching summer afternoons, cell temperature can reach 65°C or higher, dropping maximum power voltage (Vmp) and potentially falling below the inverter's minimum MPPT tracking threshold."
            }
          },
          {
            "@type": "Question",
            "name": "What is the formula for calculating maximum series modules per string under NEC 690.7?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "First, calculate the temperature-adjusted maximum open-circuit voltage per module at record low winter ambient temperature: Voc_max = Voc_STC × [ 1 + (beta_Voc / 100) × (T_min - 25°C) ]. Then, determine maximum modules per string: N_max = floor( min(V_inverter_max, V_system_code) / Voc_max ). Under NEC 690.7, residential systems are limited to 600V DC, while commercial systems permit 1,000V or 1,500V DC."
            }
          },
          {
            "@type": "Question",
            "name": "What determines the minimum number of solar panels required in a string?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The minimum string length is governed by the inverter's lowest MPPT operating voltage (V_mppt_min) during extreme summer heat: Vmp_min = Vmp_STC × [ 1 + (beta_Vmp / 100) × (T_cell_max - 25°C) ], where T_cell_max is typically ambient summer temperature plus a 25°C to 30°C thermal offset. Then: N_min = ceil( V_mppt_min / Vmp_min ). If fewer modules are connected, the inverter drops out of MPPT tracking, severely clipping solar production."
            }
          },
          {
            "@type": "Question",
            "name": "What happens if a solar string exceeds the inverter's maximum input voltage?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Exceeding the inverter's maximum DC input voltage (e.g., 600V or 1000V) triggers catastrophic breakdown in the input DC-DC boost converter or input electrolytic filter capacitors, causing immediate permanent hardware destruction, internal electrical fires, and complete voiding of manufacturer equipment warranties."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body class="cat-theme-solar">

  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="brand-logo">
        <span class="logo-badge">∑</span>
        <span>Calc<span class="accent">Hub</span></span>
      </a>
      <nav class="header-nav" aria-label="Main Navigation">
        <div class="nav-row">
          <a href="index.html" class="nav-link">🏠 Home</a>
          <a href="engineering.html" class="nav-link">⚡ Electrical</a>
          <a href="mechanical.html" class="nav-link">⚙️ Mechanical</a>
          <a href="civil.html" class="nav-link">🏗️ Civil</a>
          <a href="finance.html" class="nav-link">🏦 Finance</a>
          <a href="math.html" class="nav-link">🔢 Math</a>
          <a href="chemical.html" class="nav-link">🧪 Chemical</a>
        </div>
        <div class="nav-row">
          <a href="health.html" class="nav-link">⚖️ Health</a>
          <a href="solar-energy.html" class="nav-link active">☀️ Solar</a>
          <a href="fire-safety.html" class="nav-link">🚨 Fire &amp; Safety</a>
          <a href="programmer.html" class="nav-link">👨‍💻 Programmer</a>
          <a href="datetime.html" class="nav-link">📅 Date &amp; Time</a>
          <a href="converter.html" class="nav-link">🔄 Converter</a>
        </div>
      </nav>
    </div>
  </header>

  <div class="calc-page-header">
    <div class="calc-page-header-inner">
      <span class="category-tag">☀️ Photovoltaic Engineering &amp; NEC 690</span>
      <h1 class="calc-page-title">PV String Sizing Calculator</h1>
      <p class="calc-page-desc">Calculate allowable series modules per string (minimum and maximum panels) based on inverter MPPT operating windows, extreme winter/summer ambient temperatures, and NEC 690.7 DC voltage limits.</p>
    </div>
  </div>

  <div class="layout-container" style="display:flex;gap:2rem;max-width:1200px;margin:2rem auto;padding:0 1.25rem;align-items:start;">
    
    <main style="flex:1;min-width:0;">
      <div class="calculator-workspace">
        <section class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title"><span>☀️</span> Module, Inverter &amp; Climate Parameters</h2>
            <span class="status-info">NEC 690.7 / IEC 62548</span>
          </div>
          <form id="pv-form" onsubmit="return false;">
            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="mod-voc">Module Open-Circuit Voltage Voc (V)</label>
                <input type="number" id="mod-voc" class="form-control" value="41.5" min="15.0" max="90.0" step="0.1" oninput="runPvCalc()">
              </div>
              <div class="form-group">
                <label class="form-label" for="mod-vmp">Module Max Power Voltage Vmp (V)</label>
                <input type="number" id="mod-vmp" class="form-control" value="34.2" min="12.0" max="80.0" step="0.1" oninput="runPvCalc()">
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="temp-coeff-voc">Voc Temp Coefficient (% / °C)</label>
                <input type="number" id="temp-coeff-voc" class="form-control" value="-0.28" min="-0.60" max="-0.10" step="0.01" oninput="runPvCalc()">
              </div>
              <div class="form-group">
                <label class="form-label" for="inv-max-v">Inverter Max DC Input Voltage (V)</label>
                <select id="inv-max-v" class="form-control" onchange="runPvCalc()">
                  <option value="600" selected>600 V DC (NEC Residential String Inverter)</option>
                  <option value="1000">1,000 V DC (Commercial / Industrial Standard)</option>
                  <option value="1500">1,500 V DC (Utility Scale Ground Mount)</option>
                  <option value="500">500 V DC (Off-Grid / Hybrid Inverter)</option>
                </select>
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="mppt-min-v">Inverter MPPT Min Voltage (V)</label>
                <input type="number" id="mppt-min-v" class="form-control" value="120" min="50" max="600" step="5" oninput="runPvCalc()">
              </div>
              <div class="form-group">
                <label class="form-label" for="mppt-max-v">Inverter MPPT Max Voltage (V)</label>
                <input type="number" id="mppt-max-v" class="form-control" value="480" min="100" max="1500" step="10" oninput="runPvCalc()">
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="site-min-temp">Record Low Winter Ambient Temp (°C)</label>
                <input type="number" id="site-min-temp" class="form-control" value="-10" min="-50" max="20" step="1" oninput="runPvCalc()">
              </div>
              <div class="form-group">
                <label class="form-label" for="site-max-cell-temp">Extreme Summer Cell Temp (°C)</label>
                <input type="number" id="site-max-cell-temp" class="form-control" value="65" min="30" max="95" step="1" oninput="runPvCalc()">
              </div>
            </div>

            <div class="calc-actions" style="margin-top:1.5rem;display:flex;gap:1rem;">
              <button type="button" class="btn btn-primary" onclick="runPvCalc()">Calculate String Sizing Limits</button>
              <button type="button" class="btn btn-secondary" onclick="window.print()">🖨️ Print PV Engineering Submittal</button>
            </div>
          </form>
        </section>

        <section class="results-card">
          <h2 class="results-title">String Sizing Design Recommendations</h2>
          
          <div class="primary-result-box" style="margin-bottom:1.5rem;text-align:center;padding:1.5rem;border-radius:12px;background:#F8FAFC;border:2px solid #E2E8F0;">
            <div class="primary-result-label" style="font-size:0.9rem;text-transform:uppercase;letter-spacing:0.05em;color:#64748B;">Allowable Panels Per Series String</div>
            <div id="res-allowable-range" class="primary-result-value" style="font-size:2.5rem;font-weight:800;color:#0F172A;margin:0.25rem 0;">5 to 13 Panels</div>
            <div id="res-optimal-rec" style="font-size:1.05rem;color:#059669;font-weight:700;">Optimal Design: 10 to 12 Panels per String</div>
          </div>

          <div class="result-details-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;">
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Max Winter Cold Voc / Module</span>
              <span id="res-cold-voc" class="result-val" style="font-size:1.1rem;font-weight:700;color:#DC2626;">45.57 V (at -10°C)</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Min Summer Hot Vmp / Module</span>
              <span id="res-hot-vmp" class="result-val" style="font-size:1.1rem;font-weight:700;color:#2563EB;">29.86 V (at 65°C)</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Max String Voc (13 Panels)</span>
              <span id="res-max-string-v" class="result-val" style="font-size:1.1rem;font-weight:700;color:#0F172A;">592.4 V (&lt; 600V Limit)</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Min String Vmp (5 Panels)</span>
              <span id="res-min-string-v" class="result-val" style="font-size:1.1rem;font-weight:700;color:#0F172A;">149.3 V (&gt; 120V MPPT Min)</span>
            </div>
          </div>

          <div style="margin-top:1.25rem;padding:0.85rem;border-radius:8px;background:#F0FDF4;border:1px solid #BBF7D0;font-size:0.85rem;color:#166534;">
            <strong>☀️ Complete System Sizing:</strong> Verify balance-of-system inverter capacity with our <a href="solar-inverter-sizing-calculator.html" style="color:#166534;font-weight:700;">Solar Inverter Sizing Calculator</a> and size energy autonomy with the <a href="solar-battery-bank-calculator.html" style="color:#166534;font-weight:700;">Solar Battery Bank Calculator</a>.
          </div>
        </section>
      </div>

      <article class="educational-content" style="margin-top:3rem;line-height:1.7;color:#334155;">
        <h2>The Engineering Behind Photovoltaic Series String Sizing</h2>
        <p>In modern grid-tied and commercial solar installations, photovoltaic (PV) modules are wired in series to create high-voltage "strings" that connect to Maximum Power Point Tracking (MPPT) inputs on central or string inverters. Wiring modules in series increases string voltage linearly while keeping current constant, which minimizes ohmic copper wire losses ($I^2R$) and allows the use of thinner conductors over long rooftop or ground-mount DC feeders.</p>

        <p>However, string length is bounded by strict physical and safety constraints. Under <strong>National Electrical Code (NEC) Article 690.7</strong> and international standard <strong>IEC 62548</strong>, the system designer must ensure that string voltage never exceeds the maximum permissible voltage rating of the inverter or code ceiling (typically 600V for US residential homes and 1,000V or 1,500V for commercial arrays). Simultaneously, the designer must verify that on the hottest summer days, the string voltage remains above the inverter's minimum MPPT window floor so the inverter can continue tracking maximum power.</p>

        <h2>Mathematical Temperature Correction Formulations</h2>

        <h3>1. Maximum Open-Circuit Voltage at Extreme Winter Lows</h3>
        <p>Photovoltaic semiconductors possess a negative temperature coefficient of voltage ($\beta_{Voc}$). As ambient temperatures plummet during clear, sunny winter mornings, the bandgap of the silicon solar cell widens, generating substantially higher open-circuit voltage:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #DC2626;">
          $$V_{oc,\text{cold}} = V_{oc,\text{STC}} \cdot \left[ 1 + \left( \frac{\beta_{Voc}}{100} \right) \cdot \left( T_{\text{min}} - 25^\circ\text{C} \right) \right]$$
        </div>
        <p>Where:</p>
        <ul>
          <li><strong>$V_{oc,\text{STC}}$</strong> = Nameplate open-circuit voltage under Standard Test Conditions ($25^\circ\text{C}$, $1,000\text{ W/m}^2$, AM 1.5).</li>
          <li><strong>$\beta_{Voc}$</strong> = Temperature coefficient of $V_{oc}$ in $\% / ^\circ\text{C}$ (negative value, typically $-0.26\% / ^\circ\text{C}$ to $-0.32\% / ^\circ\text{C}$).</li>
          <li><strong>$T_{\text{min}}$</strong> = Extreme recorded historical low winter ambient temperature at the installation site in $^\circ\text{C}$.</li>
        </ul>

        <p>The maximum number of series modules per string ($N_{\text{max}}$) is then calculated using the floor function:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #2563EB;">
          $$N_{\text{max}} = \left\lfloor \frac{V_{\text{inverter, max}}}{V_{oc,\text{cold}}} \right\rfloor$$
        </div>

        <h3>2. Minimum Maximum Power Voltage at Extreme Summer Heat</h3>
        <p>On hot summer afternoons with direct solar irradiation, dark photovoltaic modules absorb thermal energy and operate at cell temperatures $25^\circ\text{C}$ to $35^\circ\text{C}$ above ambient air temperature ($T_{\text{cell, max}} \approx T_{\text{ambient, max}} + 30^\circ\text{C}$). Elevated temperature degrades $V_{mp}$:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #059669;">
          $$V_{mp,\text{hot}} = V_{mp,\text{STC}} \cdot \left[ 1 + \left( \frac{\beta_{Vmp}}{100} \right) \cdot \left( T_{\text{cell, max}} - 25^\circ\text{C} \right) \right]$$
        </div>
        <p>The absolute minimum number of modules per series string ($N_{\text{min}}$) required to keep the inverter inside its active MPPT operating range is calculated using the ceiling function:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #7C3AED;">
          $$N_{\text{min}} = \left\lceil \frac{V_{\text{MPPT, min}}}{V_{mp,\text{hot}}} \right\rceil$$
        </div>

        <h2>Standard Inverter Voltage Ratings &amp; Code Ceilings</h2>
        <p>System designers must comply with both local electrical codes and manufacturer maximum DC input ratings:</p>

        <div class="table-responsive" style="overflow-x:auto;margin:1.5rem 0;">
          <table class="table-custom" style="width:100%;border-collapse:collapse;border:1px solid #E2E8F0;">
            <thead style="background:#F8FAFC;">
              <tr style="border-bottom:2px solid #CBD5E1;text-align:left;">
                <th style="padding:0.75rem;">System Classification</th>
                <th style="padding:0.75rem;">Max DC Voltage Ceiling</th>
                <th style="padding:0.75rem;">Typical MPPT Range</th>
                <th style="padding:0.75rem;">Applicable Codes &amp; Standards</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>Residential Rooftop (US)</strong></td>
                <td style="padding:0.75rem;">600 V DC</td>
                <td style="padding:0.75rem;">100 V – 480 V DC</td>
                <td style="padding:0.75rem;">NEC 690.7(A) Maximum Voltage</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>Commercial Rooftop / Industrial</strong></td>
                <td style="padding:0.75rem;">1,000 V DC</td>
                <td style="padding:0.75rem;">200 V – 850 V DC</td>
                <td style="padding:0.75rem;">NEC 690.7 / IEC 62548 Commercial</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>Utility-Scale Ground Mount</strong></td>
                <td style="padding:0.75rem;">1,500 V DC</td>
                <td style="padding:0.75rem;">550 V – 1,300 V DC</td>
                <td style="padding:0.75rem;">Utility Substation Interconnection</td>
              </tr>
              <tr>
                <td style="padding:0.75rem;"><strong>Off-Grid / Hybrid Battery Inverters</strong></td>
                <td style="padding:0.75rem;">450 V – 500 V DC</td>
                <td style="padding:0.75rem;">80 V – 420 V DC</td>
                <td style="padding:0.75rem;">UL 1741 Low-Voltage Standards</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="worked-example-card" style="background:#F8FAFC;border:2px solid #E2E8F0;border-radius:12px;padding:1.5rem;margin:2rem 0;">
          <h3 style="margin-top:0;color:#0F172A;display:flex;align-items:center;gap:0.5rem;">
            <span>📋</span> Real-World Engineering Worked Example: Residential 8 kW Solar Roof
          </h3>
          <p><strong>Scenario:</strong> A solar installer is sizing a residential string inverter for a project in Denver, Colorado. Equipment and climate specifications:</p>
          <ul>
            <li>Solar Module: $400\text{W}$ Monocrystalline ($V_{oc} = 41.2\text{ V}$, $V_{mp} = 34.0\text{ V}$, $\beta_{Voc} = -0.28\%/^\circ\text{C}$, $\beta_{Vmp} = -0.35\%/^\circ\text{C}$)</li>
            <li>Inverter: $7.6\text{ kW}$ Dual MPPT ($V_{\text{max}} = 600\text{ V}$, MPPT window: $120\text{ V}$ to $480\text{ V}$)</li>
            <li>Site Climate: Record low winter $T_{\text{min}} = -15^\circ\text{C}$; Summer maximum cell temperature $T_{\text{cell, max}} = 70^\circ\text{C}$</li>
          </ul>

          <ol style="padding-left:1.25rem;line-height:1.8;">
            <li><strong>Calculate Winter Cold Open-Circuit Voltage ($V_{oc,\text{cold}}$):</strong>
              $$\Delta T_{\text{cold}} = -15^\circ\text{C} - 25^\circ\text{C} = -40^\circ\text{C}$$
              $$V_{oc,\text{cold}} = 41.2 \times [ 1 + (-0.0028 \times -40) ] = 41.2 \times [ 1 + 0.112 ] = 41.2 \times 1.112 \approx 45.81\text{ V}$$
            </li>
            <li><strong>Determine Maximum Modules per String ($N_{\text{max}}$):</strong>
              $$N_{\text{max}} = \left\lfloor \frac{600\text{ V}}{45.81\text{ V}} \right\rfloor = \lfloor 13.097 \rfloor = 13\text{ Modules}$$
              <em>Check:</em> $13 \times 45.81\text{ V} = 595.5\text{ V} \le 600\text{ V}$ (Code compliant).
            </li>
            <li><strong>Calculate Summer Hot Max Power Voltage ($V_{mp,\text{hot}}$):</strong>
              $$\Delta T_{\text{hot}} = 70^\circ\text{C} - 25^\circ\text{C} = +45^\circ\text{C}$$
              $$V_{mp,\text{hot}} = 34.0 \times [ 1 + (-0.0035 \times 45) ] = 34.0 \times [ 1 - 0.1575 ] = 34.0 \times 0.8425 \approx 28.65\text{ V}$$
            </li>
            <li><strong>Determine Minimum Modules per String ($N_{\text{min}}$):</strong>
              $$N_{\text{min}} = \left\lceil \frac{120\text{ V}}{28.65\text{ V}} \right\rceil = \lceil 4.188 \rceil = 5\text{ Modules}$$
            </li>
            <li><strong>Engineering Conclusion:</strong> Any string between <strong>5 and 13 modules</strong> will operate safely. For a 20-module installation, the designer wires two identical parallel strings of <strong>10 modules each</strong>, providing optimal central MPPT voltage ($10 \times 34\text{ V} = 340\text{ V}$ at STC), maximizing inverter efficiency.</li>
          </ol>
        </div>

        <h2>Frequently Asked Technical Questions</h2>
        <div class="faq-accordion" style="margin-top:1.5rem;">
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">Can you connect strings with different numbers of modules into the same MPPT input?</h4>
            <p style="margin:0;color:#64748B;">No! Strings wired in parallel into the same MPPT channel must contain the exact same number of identical modules. Paralleling mismatched string lengths (e.g., 10 panels and 12 panels) causes heavy cross-conduction voltage mismatch losses, severe reverse current flow, hotspot development, and significant energy yield reduction.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">What is the difference between Inverter Max Input Voltage and Max MPPT Voltage?</h4>
            <p style="margin:0;color:#64748B;">Max Input Voltage (e.g., 600V) is the absolute destructive electrical breakdown limit of the inverter. If open-circuit voltage ever exceeds this value, hardware is destroyed. In contrast, Max MPPT Voltage (e.g., 480V) is the upper threshold where the inverter's MPPT tracking algorithm functions at peak efficiency. Between 480V and 600V, the inverter safely curtails or throttles power output without physical damage.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">How does rooftop mounting affect summer cell operating temperature?</h4>
            <p style="margin:0;color:#64748B;">Modules mounted flush against dark asphalt shingle roofs with minimal clearance (&lt; 2 inches) suffer poor convective ventilation and routinely reach cell temperatures of 65°C to 75°C (30°C to 35°C above ambient). Raising the racking standoff to 4 to 6 inches improves airflow, keeping operating cell temperatures 10°C cooler and increasing annual energy production by up to 4%.</p>
          </div>
          <div class="faq-item" style="padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">Are DC optimizers or microinverters subject to the same string sizing limits?</h4>
            <p style="margin:0;color:#64748B;">Microinverters attach directly to each module individually, completely eliminating series string calculations. DC optimizers (like SolarEdge) regulate their output voltage into the inverter string (holding a fixed bus voltage such as 380V or 400V), allowing longer strings (up to 25 modules) and enabling strings with varying lengths and orientations.</p>
          </div>
        </div>
      </article>
    </main>

    <aside class="sidebar" style="width:300px;flex-shrink:0;">
      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;margin-bottom:1.5rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">☀️ Solar Engineering Suite</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="pv-string-sizing-calculator.html" style="font-weight:700;color:#059669;">☀️ PV String Sizing (NEC 690)</a></li>
          <li><a href="solar-panel-sizing-calculator.html" style="color:#475569;">☀️ Solar Panel Sizing</a></li>
          <li><a href="solar-inverter-sizing-calculator.html" style="color:#475569;">⚡ Solar Inverter Sizing</a></li>
          <li><a href="solar-battery-bank-calculator.html" style="color:#475569;">🔋 Solar Battery Bank Sizing</a></li>
          <li><a href="ev-charging-time-calculator.html" style="color:#475569;">🔌 EV Charging Time &amp; Power</a></li>
        </ul>
      </div>

      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">⚡ Electrical Installation Suite</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="cable-sizing-calculator.html" style="color:#475569;">🔌 Cable Sizing Calculator</a></li>
          <li><a href="wire-ampacity-calculator.html" style="color:#475569;">🔌 Wire Ampacity (NEC)</a></li>
          <li><a href="voltage-drop-calculator.html" style="color:#475569;">📉 Voltage Drop Calculator</a></li>
          <li><a href="conduit-fill-calculator.html" style="color:#475569;">🪢 Conduit Fill Calculator</a></li>
        </ul>
      </div>
    </aside>

  </div>

  <footer class="site-footer" style="background:#0F172A;color:#94A3B8;padding:3rem 1.25rem;margin-top:4rem;">
    <div style="max-width:1200px;margin:0 auto;display:flex;justify-content:space-between;flex-wrap:wrap;gap:2rem;">
      <div>
        <div style="font-size:1.25rem;font-weight:800;color:#FFFFFF;margin-bottom:0.5rem;">CalcHub</div>
        <p style="font-size:0.88rem;max-width:320px;">Open-source engineering, financial, and scientific computational tools. 100% verified mathematics.</p>
      </div>
      <div>
        <div style="font-weight:700;color:#FFFFFF;margin-bottom:0.75rem;">Solar Engineering Standards</div>
        <div style="font-size:0.85rem;line-height:2;">
          NEC Article 690 Solar Photovoltaic Systems<br>
          IEC 62548 Design Requirements for PV Arrays<br>
          UL 1741 Inverters &amp; Interconnection
        </div>
      </div>
    </div>
    <div style="max-width:1200px;margin:2rem auto 0;padding-top:1.5rem;border-top:1px solid #1E293B;text-align:center;font-size:0.82rem;">
      &copy; 2026 CalcHub. Professional Photovoltaic &amp; Renewable Energy Suite.
    </div>
  </footer>

  <script>
    function runPvCalc() {
      const vocStc = Math.max(10, parseFloat(document.getElementById('mod-voc').value) || 41.5);
      const vmpStc = Math.max(10, parseFloat(document.getElementById('mod-vmp').value) || 34.2);
      const coeffVocPct = parseFloat(document.getElementById('temp-coeff-voc').value) || -0.28;
      const coeffVmpPct = coeffVocPct * 1.25; // typically slightly steeper negative coefficient

      const invMaxV = parseFloat(document.getElementById('inv-max-v').value) || 600;
      const mpptMinV = Math.max(20, parseFloat(document.getElementById('mppt-min-v').value) || 120);
      const mpptMaxV = Math.max(mpptMinV + 50, parseFloat(document.getElementById('mppt-max-v').value) || 480);

      const tMin = parseFloat(document.getElementById('site-min-temp').value) || -10;
      const tCellMax = parseFloat(document.getElementById('site-max-cell-temp').value) || 65;

      // 1. Extreme cold Voc per module: Voc_cold = Voc_STC * [1 + (beta/100) * (T_min - 25)]
      const deltaTCold = tMin - 25.0;
      const vocCold = vocStc * (1.0 + (coeffVocPct / 100.0) * deltaTCold);

      // 2. Extreme hot Vmp per module: Vmp_hot = Vmp_STC * [1 + (beta/100) * (T_cell_max - 25)]
      const deltaTHot = tCellMax - 25.0;
      const vmpHot = vmpStc * (1.0 + (coeffVmpPct / 100.0) * deltaTHot);

      // Max modules per string (limited by inverter max voltage)
      const nMax = Math.floor(invMaxV / vocCold);

      // Min modules per string (limited by MPPT min voltage)
      const nMin = Math.ceil(mpptMinV / vmpHot);

      // MPPT max ceiling check: nMaxMppt
      const nMaxMppt = Math.floor(mpptMaxV / vmpHot);

      const maxStringVoc = nMax * vocCold;
      const minStringVmp = nMin * vmpHot;

      let rangeStr = nMin + ' to ' + nMax + ' Panels';
      if (nMin > nMax) {
        rangeStr = 'Incompatible Setup (Min ' + nMin + ' > Max ' + nMax + ')';
      }

      document.getElementById('res-allowable-range').textContent = rangeStr;
      if (nMin <= nMax) {
        const optimalN = Math.min(nMax, Math.max(nMin, Math.round((nMin + nMax) / 2)));
        document.getElementById('res-optimal-rec').textContent = 'Recommended Target: ' + optimalN + ' Panels per String (Best MPPT Yield)';
      } else {
        document.getElementById('res-optimal-rec').textContent = 'Please choose an inverter with a broader MPPT window.';
      }

      document.getElementById('res-cold-voc').textContent = vocCold.toFixed(2) + ' V (at ' + tMin + '°C)';
      document.getElementById('res-hot-vmp').textContent = vmpHot.toFixed(2) + ' V (at ' + tCellMax + '°C)';
      document.getElementById('res-max-string-v').textContent = maxStringVoc.toFixed(1) + ' V (< ' + invMaxV + 'V Limit)';
      document.getElementById('res-min-string-v').textContent = minStringVmp.toFixed(1) + ' V (> ' + mpptMinV + 'V MPPT Min)';
    }

    window.addEventListener('DOMContentLoaded', runPvCalc);
  </script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "battery-life-calculator.html"), "w", encoding="utf-8") as f:
    f.write(TOOL_BATTERY_LIFE)
print("[PASS] battery-life-calculator.html generated successfully!")

with open(os.path.join(BASE_DIR, "pv-string-sizing-calculator.html"), "w", encoding="utf-8") as f:
    f.write(TOOL_PV_STRING)
print("[PASS] pv-string-sizing-calculator.html generated successfully!")
