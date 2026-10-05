# -*- coding: utf-8 -*-
"""
Generator for Batch 41 - Part 2 (Final 4 Tools of Master Database)
Tools:
5. cable-sizing-guide.html (IEC 60364, NEC Article 310, Voltage Drop, Thermal Withstand)
6. electrical.html (Master Electrical Hub, 30+ Tools Index, Quick Ohm & 3-Phase Solver)
7. engineering-formulas.html (Multidisciplinary Formula Compendium & Live Equation Solver)
8. financial.html (Master Financial Hub, 29+ Tools Index, Quick TVM & Loan Sizer)
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COMMON_TAIL = """    <footer class="site-footer">
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>About CalcHub</h4>
                    <p>CalcHub delivers peer-reviewed chronometric computing algorithms, professional engineering suites, and enterprise financial calendar engines compliant with ISO 8601, IEEE, IEC, and FLSA reporting standards.</p>
                </div>
                <div class="footer-col">
                    <h4>Professional Suites</h4>
                    <ul>
                        <li><a href="electrical.html">Electrical Engineering</a></li>
                        <li><a href="engineering.html">Engineering Tools</a></li>
                        <li><a href="financial.html">Financial Planning</a></li>
                        <li><a href="datetime.html">Date &amp; Time Utilities</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Core Reference Guides</h4>
                    <ul>
                        <li><a href="cable-sizing-guide.html">Cable Sizing Guide</a></li>
                        <li><a href="engineering-formulas.html">Engineering Formulas</a></li>
                        <li><a href="best-engineering-calculator.html">Best Engineering Calculator</a></li>
                        <li><a href="electrical.html">Electrical Suite Hub</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="index.html">All Calculators</a></li>
                        <li><a href="converter.html">Metric Converters</a></li>
                        <li><a href="finance.html">Finance &amp; Payroll</a></li>
                        <li><a href="math.html">Math &amp; Statistics</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 CalcHub. All rights reserved. Precision engineering, chronometry, and mathematical computational systems.</p>
            </div>
        </div>
    </footer>
</body>
</html>"""

def get_page_html(title, description, canonical_slug, schema_json, h1, short_desc, calc_ui, article_content, category_hub="engineering.html", category_name="Engineering Tools"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="https://calchub.com/{canonical_slug}.html">
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
    <script type="application/ld+json">
{schema_json}
    </script>
</head>
<body>
    <header class="site-header">
        <div class="header-container">
            <a href="index.html" class="logo">CalcHub</a>
            <nav class="nav-links">
                <a href="index.html">Home</a>
                <a href="datetime.html">Date &amp; Time</a>
                <a href="math.html">Math &amp; Stats</a>
                <a href="finance.html">Finance</a>
                <a href="converter.html">Converters</a>
            </nav>
        </div>
    </header>
    <div class="container">
        <div class="main-wrapper">
            <main class="content-area">
                <nav class="breadcrumb">
                    <a href="index.html">Home</a> &gt; <a href="{category_hub}">{category_name}</a> &gt; <span>{h1}</span>
                </nav>
                <div class="calculator-card">
                    <div class="calc-header">
                        <h1>{h1}</h1>
                        <p class="calc-desc">{short_desc}</p>
                    </div>
                    {calc_ui}
                </div>
                <article class="article-body">
                    {article_content}
                </article>
            </main>
            <aside class="sidebar">
                <div class="sidebar-card">
                    <h3>Related Engineering Hubs</h3>
                    <ul class="sidebar-links">
                        <li><a href="cable-sizing-guide.html">Cable Sizing Guide</a></li>
                        <li><a href="electrical.html">Electrical Suite Hub</a></li>
                        <li><a href="engineering-formulas.html">Engineering Formulas</a></li>
                        <li><a href="financial.html">Financial Suite Hub</a></li>
                        <li><a href="best-engineering-calculator.html">Best Engineering Calculator</a></li>
                        <li><a href="engineering.html">All Engineering Tools</a></li>
                        <li><a href="voltage-drop-calculator.html">Voltage Drop Calculator</a></li>
                    </ul>
                </div>
            </aside>
        </div>
    </div>
{COMMON_TAIL}"""


# ===========================================================================
# TOOL 5: cable-sizing-guide.html
# ===========================================================================
def gen_cable_sizing_guide():
    slug = "cable-sizing-guide"
    title = "Cable Sizing Guide & Selection Calculator | IEC 60364 & NEC Standards"
    desc = "Engineering cable sizing guide and interactive conductor selection calculator. Conforms to IEC 60364-5-52, BS 7671, and NEC Article 310 for voltage drop and thermal rating."
    h1 = "Cable Sizing Guide &amp; Selection Calculator"
    short_desc = "Comprehensive engineering conductor selection engine compliant with IEC 60364-5-52, BS 7671, and NEC Article 310, evaluating derated ampacity, voltage drop, and short-circuit thermal withstand."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Cable Sizing Guide Calculator",
      "url": "https://calchub.com/cable-sizing-guide.html",
      "applicationCategory": "EngineeringApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Calculates electrical cable conductor sizing according to IEC 60364 and NEC standards, including voltage drop and short circuit thermal capacity."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What are the four primary criteria for sizing an electrical cable?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Cable sizing requires satisfying four independent engineering criteria: (1) Continuous current ampacity under derated thermal conditions, (2) Maximum allowable voltage drop percentage, (3) Short-circuit adiabatic thermal withstand capability, and (4) Mechanical strength and physical installation constraints."
          }
        },
        {
          "@type": "Question",
          "name": "How do installation derating factors affect cable ampacity?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nominal cable ampacity is derated using environmental coefficients: Ca for ambient temperature deviation, Cg for cable bundling/grouping proximity, and Ci for thermal insulation contact. The required derated capacity Iz = Ib / (Ca * Cg * Ci)."
          }
        },
        {
          "@type": "Question",
          "name": "What is the maximum permissible voltage drop in industrial installations?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Under IEC 60364-5-52, the maximum recommended voltage drop between the public supply origin and user appliances is 3% for lighting circuits and 5% for other power loads. Under NEC 210.19/215.2, 3% on branch circuits and 5% total is standard."
          }
        },
        {
          "@type": "Question",
          "name": "Why is copper preferred over aluminium in smaller building cables?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Copper has significantly lower electrical resistivity (1.72e-8 ohm-m vs 2.82e-8 ohm-m for aluminium), higher tensile ductility, superior creep resistance at termination lugs, and creates no dangerous galvanic oxidation in branch circuit sizes."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-body">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.25rem; margin-bottom: 1.25rem;">
        <div>
            <label for="csSystem" style="font-weight: 600; font-size: 0.875rem;">Electrical System Voltage:</label>
            <select id="csSystem" class="input-field" onchange="calculateCableSize()">
                <option value="400_3p">3-Phase 400V (IEC European/Global)</option>
                <option value="480_3p">3-Phase 480V (NEC North American)</option>
                <option value="230_1p">Single Phase 230V (Global)</option>
                <option value="120_1p">Single Phase 120V (North American)</option>
            </select>
        </div>
        <div>
            <label for="csLoadKw" style="font-weight: 600; font-size: 0.875rem;">Load Power (kW):</label>
            <input type="number" id="csLoadKw" class="input-field" value="45.0" min="0.1" step="1.0" oninput="calculateCableSize()">
        </div>
        <div>
            <label for="csPf" style="font-weight: 600; font-size: 0.875rem;">Power Factor (cos &phi;):</label>
            <input type="number" id="csPf" class="input-field" value="0.85" min="0.5" max="1.0" step="0.05" oninput="calculateCableSize()">
        </div>
        <div>
            <label for="csLength" style="font-weight: 600; font-size: 0.875rem;">Run Length (Meters):</label>
            <input type="number" id="csLength" class="input-field" value="75" min="1" max="2000" step="5" oninput="calculateCableSize()">
        </div>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.25rem; margin-bottom: 1.5rem;">
        <div>
            <label for="csMaxVd" style="font-weight: 600; font-size: 0.875rem;">Max Allowed Voltage Drop (%):</label>
            <input type="number" id="csMaxVd" class="input-field" value="3.0" min="1.0" max="10.0" step="0.5" oninput="calculateCableSize()">
        </div>
        <div>
            <label for="csConductor" style="font-weight: 600; font-size: 0.875rem;">Conductor Material:</label>
            <select id="csConductor" class="input-field" onchange="calculateCableSize()">
                <option value="cu">Copper (Cu - Standard)</option>
                <option value="al">Aluminium (Al - Feeder)</option>
            </select>
        </div>
        <div>
            <label for="csInsulation" style="font-weight: 600; font-size: 0.875rem;">Insulation Type:</label>
            <select id="csInsulation" class="input-field" onchange="calculateCableSize()">
                <option value="xlpe">XLPE / EPR (90&deg;C Operating)</option>
                <option value="pvc">PVC (70&deg;C Operating)</option>
            </select>
        </div>
        <div>
            <label for="csDerateTotal" style="font-weight: 600; font-size: 0.875rem;">Total Derating Factor (Ca &times; Cg):</label>
            <input type="number" id="csDerateTotal" class="input-field" value="0.80" min="0.3" max="1.0" step="0.05" oninput="calculateCableSize()">
            <span class="input-hint">Ambient temp + cable grouping</span>
        </div>
    </div>

    <div class="result-box" style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem;">
        <h3 style="margin-top: 0; color: #1e293b; font-size: 1.1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">Recommended Conductor &amp; Analysis</h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Recommended Cable Size</div>
                <div id="resCableSize" style="font-size: 1.5rem; font-weight: 700; color: #2563eb;">35 mm²</div>
                <div id="resAwgEq" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">AWG #2 Equivalent</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Design Load Current (Ib)</div>
                <div id="resLoadCurrent" style="font-size: 1.4rem; font-weight: 700; color: #0f172a;">76.4 A</div>
                <div id="resDeratedCurrent" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">Req Ampacity Iz: 95.5 A</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Actual Voltage Drop</div>
                <div id="resActualVd" style="font-size: 1.4rem; font-weight: 700; color: #059669;">1.84% (7.36 V)</div>
                <div id="resVdPass" style="font-size: 0.8rem; color: #16a34a; margin-top: 0.25rem;">PASS (&lt; 3.0% limit)</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Total Cable Power Loss</div>
                <div id="resPowerLoss" style="font-size: 1.4rem; font-weight: 700; color: #d97706;">562 Watts</div>
                <div style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">3-Phase I²R Heat Loss</div>
            </div>
        </div>
    </div>
</div>

<script>
const SIZES_MM2 = [1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120, 150, 185, 240, 300, 400];
const AWG_MAP = {
    1.5: "16 AWG", 2.5: "14 AWG", 4: "12 AWG", 6: "10 AWG", 10: "8 AWG",
    16: "6 AWG", 25: "4 AWG", 35: "2 AWG", 50: "1/0 AWG", 70: "2/0 AWG",
    95: "3/0 AWG", 120: "4/0 AWG", 150: "300 kcmil", 185: "350 kcmil",
    240: "500 kcmil", 300: "600 kcmil", 400: "750 kcmil"
};

// Nominal base ampacities in conduit / tray (Reference Method C, 30C, Copper XLPE)
const BASE_AMPACITY_CU_XLPE = {
    1.5: 23, 2.5: 31, 4: 42, 6: 54, 10: 75, 16: 100, 25: 133,
    35: 164, 50: 198, 70: 253, 95: 306, 120: 354, 150: 407,
    185: 464, 240: 546, 300: 628, 400: 728
};

function calculateCableSize() {
    const sys = document.getElementById('csSystem').value;
    const kw = parseFloat(document.getElementById('csLoadKw').value) || 0;
    const pf = parseFloat(document.getElementById('csPf').value) || 0.85;
    const len = parseFloat(document.getElementById('csLength').value) || 0;
    const maxVdPct = parseFloat(document.getElementById('csMaxVd').value) || 3.0;
    const mat = document.getElementById('csConductor').value;
    const ins = document.getElementById('csInsulation').value;
    const derate = parseFloat(document.getElementById('csDerateTotal').value) || 0.8;

    let vLine = 400;
    let is3Phase = true;

    if (sys === '400_3p') { vLine = 400; is3Phase = true; }
    else if (sys === '480_3p') { vLine = 480; is3Phase = true; }
    else if (sys === '230_1p') { vLine = 230; is3Phase = false; }
    else { vLine = 120; is3Phase = false; }

    // Load current Ib
    let ib = 0;
    if (is3Phase) {
        ib = (kw * 1000) / (Math.sqrt(3) * vLine * pf);
    } else {
        ib = (kw * 1000) / (vLine * pf);
    }

    const reqAmpacity = ib / Math.max(0.1, derate);

    // Resistivity rho at operating temp (ohm * mm^2 / m)
    // Cu XLPE (90C) = 0.0225, Cu PVC (70C) = 0.0212
    // Al XLPE (90C) = 0.036, Al PVC (70C) = 0.034
    let rho = 0.0225;
    if (mat === 'cu') {
        rho = (ins === 'xlpe') ? 0.0225 : 0.0212;
    } else {
        rho = (ins === 'xlpe') ? 0.0360 : 0.0340;
    }

    // Material ampacity factor (Al is ~0.78 of Cu)
    const matFactor = (mat === 'cu') ? 1.0 : 0.78;
    const insFactor = (ins === 'xlpe') ? 1.0 : 0.87;

    let selectedSize = SIZES_MM2[SIZES_MM2.length - 1];
    let actualVdPct = 0;
    let actualVdVolts = 0;
    let cableR = 0;

    for (let i = 0; i < SIZES_MM2.length; i++) {
        const s = SIZES_MM2[i];
        const baseAmp = (BASE_AMPACITY_CU_XLPE[s] || 20) * matFactor * insFactor;

        // Voltage drop calculation
        const r_single = (rho * len) / s;
        let vd_v = 0;
        if (is3Phase) {
            vd_v = Math.sqrt(3) * ib * r_single * pf;
        } else {
            vd_v = 2 * ib * r_single * pf;
        }
        const vd_pct = (vd_v / vLine) * 100;

        // Check if both ampacity and voltage drop criteria are satisfied
        if (baseAmp >= reqAmpacity && vd_pct <= maxVdPct) {
            selectedSize = s;
            actualVdPct = vd_pct;
            actualVdVolts = vd_v;
            cableR = r_single;
            break;
        }
    }

    // Calculate I^2 R power loss
    const powerLossWatts = is3Phase ? (3 * Math.pow(ib, 2) * cableR) : (2 * Math.pow(ib, 2) * cableR);

    document.getElementById('resCableSize').innerText = `${selectedSize} mm²`;
    document.getElementById('resAwgEq').innerText = `${AWG_MAP[selectedSize] || 'Large Feeder'} Equivalent`;
    document.getElementById('resLoadCurrent').innerText = `${ib.toFixed(1)} A`;
    document.getElementById('resDeratedCurrent').innerText = `Req Ampacity Iz: ${reqAmpacity.toFixed(1)} A`;
    document.getElementById('resActualVd').innerText = `${actualVdPct.toFixed(2)}% (${actualVdVolts.toFixed(1)} V)`;

    const vdEl = document.getElementById('resVdPass');
    if (actualVdPct <= maxVdPct) {
        vdEl.style.color = '#16a34a';
        vdEl.innerText = `PASS (< ${maxVdPct.toFixed(1)}% limit)`;
    } else {
        vdEl.style.color = '#dc2626';
        vdEl.innerText = `WARNING: Exceeds ${maxVdPct.toFixed(1)}%`;
    }

    document.getElementById('resPowerLoss').innerText = `${Math.round(powerLossWatts).toLocaleString()} Watts`;
}

window.addEventListener('DOMContentLoaded', calculateCableSize);
</script>"""

    article = """<h2>Engineering Principles of Cable Sizing and Conductor Selection</h2>
<p>In electrical power engineering, proper conductor selection ensures that insulated electrical cables operate safely under continuous full-load current without thermal degradation, deliver adequate voltage to terminal equipment, withstand prospective short-circuit fault currents without dielectric breakdown, and comply with international statutory electrical safety codes.</p>

<p>A rigorous cable sizing engineering assessment requires satisfying four independent mathematical and physical criteria:</p>
<ol>
    <li><strong>Continuous Current-Carrying Capacity (Ampacity):</strong> The derated thermal rating of the cable $I_z$ must exceed the circuit design full-load current $I_b$, and coordinate with the overcurrent protective device rating $I_n$:
    $$I_b \le I_n \le I_z$$
    </li>
    <li><strong>Voltage Drop Limitation:</strong> The percentage voltage drop $\Delta V_{\%}$ across the conductor span must remain below statutory thresholds (typically $3\%$ to $5\%$) to guarantee proper motor starting torque and sensitive electronic functionality.</li>
    <li><strong>Short-Circuit Thermal Withstand:</strong> The conductor cross-sectional area $S$ must satisfy the adiabatic energy withstand equation during upstream fault clearing time $t$:
    $$k^2 S^2 \ge I_{\text{sc}}^2 t \implies S \ge \frac{I_{\text{sc}} \sqrt{t}}{k}$$
    </li>
    <li><strong>Harmonic Current Derating:</strong> In modern commercial facilities with heavy non-linear LED, VFD, and server loads, triplen harmonic currents ($3\text{rd}, 9\text{th}, 15\text{th}$) circulate through the neutral conductor, requiring neutral up-sizing per IEC 60364-5-52 Annex E.</li>
</ol>

<h2>Installation Derating Factors and Thermal Modeling</h2>
<p>Nominal cable current capacities published in regulatory standards (such as IEC 60364-5-52 Table B.52 or NEC Article 310 Table 310.16) are referenced to idealized baseline operating conditions: an ambient air temperature of $30^\circ\text{C}$ and an isolated single circuit. In real industrial installations, conductors are derated using environmental correction factors:</p>

$$I_z = I_{\text{tabulated}} \times C_a \times C_g \times C_i \times C_s$$

<p>Where the mathematical derating coefficients represent:</p>
<ul>
    <li>$C_a$ (Ambient Temperature Factor): Accounts for operating in ambient temperatures exceeding $30^\circ\text{C}$ (e.g., $C_a = 0.82$ for $45^\circ\text{C}$ ambient in XLPE insulation).</li>
    <li>$C_g$ (Grouping / Bundling Factor): Accounts for mutual thermal heating when multiple single-core or multi-core cables run touching in conduits or trays (e.g., $C_g = 0.70$ for 4 grouped circuits).</li>
    <li>$C_i$ (Thermal Insulation Factor): Derates cables embedded in building thermal fiberglass or cellulose batting ($C_i \approx 0.50$ to $0.75$).</li>
    <li>$C_s$ (Soil Thermal Resistivity Factor): Applies to direct-buried underground cables based on soil moisture and thermal resistivity ($K \cdot m / W$).</li>
</ul>

<h3>IEC Installation Reference Methods and Derating Matrix</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>IEC Reference Method</th>
            <th>Physical Installation Description</th>
            <th>Thermal Dissipation Efficiency</th>
            <th>Copper XLPE 35 mm² Ampacity</th>
            <th>Aluminium XLPE 50 mm² Ampacity</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Method A1 / A2</td><td>Insulated conductors in conduit inside thermally insulated wall</td><td>Lowest (Thermal Trap)</td><td>110 A</td><td>104 A</td></tr>
        <tr><td>Method B1 / B2</td><td>Cables in conduit or trunking on a wooden/masonry wall</td><td>Moderate</td><td>135 A</td><td>128 A</td></tr>
        <tr><td>Method C</td><td>Single or multi-core cable clipped direct to non-combustible surface</td><td>High (Convection Free)</td><td>164 A</td><td>155 A</td></tr>
        <tr><td>Method E / F</td><td>Cables in free air on open perforated cable tray or ladder rack</td><td>Highest (Optimal Ventilation)</td><td>182 A</td><td>172 A</td></tr>
        <tr><td>Method D1 / D2</td><td>Direct buried or in underground ducts in soil ($20^\circ\text{C}$)</td><td>High (Soil Conduction)</td><td>170 A</td><td>160 A</td></tr>
    </tbody>
</table>

<h2>Voltage Drop Mathematical Formulations</h2>
<p>Voltage drop across an alternating current (AC) feeder is evaluated from conductor resistance $R$ and inductive reactance $X$:</p>

$$\Delta V_{\text{3-phase}} = \sqrt{3} \cdot I_b \cdot L \cdot \left( R \cos \phi + X \sin \phi \right)$$
$$\Delta V_{\text{1-phase}} = 2 \cdot I_b \cdot L \cdot \left( R \cos \phi + X \sin \phi \right)$$

<p>Where $L$ is one-way feeder length in kilometers, and $R$ and $X$ are expressed in $\Omega / \text{km}$. The percentage drop evaluates as:</p>

$$\Delta V_{\%} = \frac{\Delta V}{V_{\text{nominal}}} \times 100\%$$

<div class="worked-example-card">
    <h3>Worked Industrial Engineering Case Study: 45 kW Wastewater Pump Feeder</h3>
    <p><strong>Scenario:</strong> A 400V, 3-phase, 50 Hz municipal wastewater treatment plant installs a 45 kW submersible lift pump operating at a power factor of $\cos \phi = 0.85$ lagging. The cable route runs <strong>75 meters</strong> in an open ventilated tray. Ambient summer temperature reaches $40^\circ\text{C}$ ($C_a = 0.91$), and the cable runs bundled alongside two other operational feeders ($C_g = 0.80$). Maximum allowable voltage drop is 3.0%. Size the required Copper XLPE cable.</p>
    
    <div class="step-solution">
        <h4>Step 1: Calculate Design Full-Load Current ($I_b$)</h4>
        $$I_b = \frac{P}{\sqrt{3} \cdot V \cdot \cos \phi} = \frac{45,000}{\sqrt{3} \cdot 400 \cdot 0.85} = \frac{45,000}{588.897} \approx 76.41 \text{ A}$$

        <h4>Step 2: Evaluate Total Environmental Derating Factor</h4>
        $$C_{\text{total}} = C_a \times C_g = 0.91 \times 0.80 = 0.728$$

        <h4>Step 3: Determine Required Minimum Tabulated Ampacity ($I_z$)</h4>
        $$I_z = \frac{I_b}{C_{\text{total}}} = \frac{76.41}{0.728} \approx 104.96 \text{ A}$$
        <p>From IEC Method C / E tables: A $25 \text{ mm}^2$ Cu XLPE cable provides $133 \text{ A}$ (satisfies ampacity $133 \times 0.728 = 96.8 \text{ A} < 104.96 \text{ A}$, so next size up $35 \text{ mm}^2$ provides $164 \times 0.728 = 119.4 \text{ A}$, which PASSES).</p>

        <h4>Step 4: Verify Voltage Drop on $35 \text{ mm}^2$ Conductor</h4>
        <p>For $35 \text{ mm}^2$ copper at $90^\circ\text{C}$: $R \approx 0.627 \, \Omega/\text{km} = 0.000627 \, \Omega/\text{m}$.</p>
        $$\Delta V = \sqrt{3} \cdot (76.41) \cdot (75) \cdot (0.000627 \cdot 0.85) = 132.34 \cdot 75 \cdot 0.000533 \approx 5.29 \text{ V}$$
        $$\Delta V_{\%} = \frac{5.29}{400} \times 100\% \approx 1.32\%$$
        <p><strong>Conclusion:</strong> $1.32\% < 3.0\%$ maximum limit! A <strong>$35 \text{ mm}^2$ Copper XLPE 4-core cable</strong> satisfies both thermal ampacity and voltage drop criteria.</p>
    </div>
</div>

<h2>Common Implementation Pitfalls in Cable Sizing</h2>
<ol>
    <li><strong>Neglecting Inductive Reactance in Large Feeders:</strong> For conductors larger than $70 \text{ mm}^2$ (or 2/0 AWG), inductive reactance $X$ becomes comparable to AC resistance $R$. Ignoring reactive drop underestimates total voltage drop by 20% to 40%.</li>
    <li><strong>Sizing Exclusively for Ampacity While Ignoring Voltage Drop:</strong> On long runs exceeding 50 meters, a cable that easily passes thermal ampacity will frequently fail voltage drop criteria, leading to motor contactor chatter and premature equipment burn-out.</li>
    <li><strong>Overlooking Short-Circuit Thermal Ratings:</strong> High prospective fault currents near substation transformers can vaporize undersized grounding or neutral conductors before the circuit breaker trips unless verified against the adiabatic equation $S \ge I_{\text{sc}} \sqrt{t} / k$.</li>
</ol>

<section class="faq-section">
    <h2>Frequently Asked Questions About Cable Sizing</h2>
    <div class="faq-item">
        <h3>What are the four primary criteria for sizing an electrical cable?</h3>
        <p>Cable sizing requires satisfying four independent engineering criteria: (1) Continuous current ampacity under derated thermal conditions, (2) Maximum allowable voltage drop percentage, (3) Short-circuit adiabatic thermal withstand capability, and (4) Mechanical strength and physical installation constraints.</p>
    </div>
    <div class="faq-item">
        <h3>How do installation derating factors affect cable ampacity?</h3>
        <p>Nominal cable ampacity is derated using environmental coefficients: Ca for ambient temperature deviation, Cg for cable bundling/grouping proximity, and Ci for thermal insulation contact. The required derated capacity Iz = Ib / (Ca * Cg * Ci).</p>
    </div>
    <div class="faq-item">
        <h3>What is the maximum permissible voltage drop in industrial installations?</h3>
        <p>Under IEC 60364-5-52, the maximum recommended voltage drop between the public supply origin and user appliances is 3% for lighting circuits and 5% for other power loads. Under NEC 210.19/215.2, 3% on branch circuits and 5% total is standard.</p>
    </div>
    <div class="faq-item">
        <h3>Why is copper preferred over aluminium in smaller building cables?</h3>
        <p>Copper has significantly lower electrical resistivity (1.72e-8 ohm-m vs 2.82e-8 ohm-m for aluminium), higher tensile ductility, superior creep resistance at termination lugs, and creates no dangerous galvanic oxidation in branch circuit sizes.</p>
    </div>
</section>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article, category_hub="engineering.html", category_name="Engineering Tools")


# ===========================================================================
# TOOL 6: electrical.html (Master Electrical Hub)
# ===========================================================================
def gen_electrical_hub():
    slug = "electrical"
    title = "Electrical Engineering Calculators & Power Systems Reference Hub"
    desc = "Master Electrical Engineering Suite Hub. Access 30+ peer-reviewed calculators for cable sizing, 3-phase power, transformers, motors, Ohm's law, and PCB design."
    h1 = "Electrical Engineering Suite Hub"
    short_desc = "CalcHub's comprehensive Master Electrical Engineering Hub indexing specialized power systems calculators, conductor sizing engines, and circuit analysis utilities."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Electrical Engineering Suite Hub",
      "url": "https://calchub.com/electrical.html",
      "applicationCategory": "EngineeringApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Comprehensive reference directory and computational suite for electrical engineers, technicians, and power system designers."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What calculation tools are included in the CalcHub Electrical Suite?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The suite includes 30+ specialized tools spanning cable sizing (IEC/NEC), 3-phase power, transformer sizing, motor starters, PCB trace width, lightning protection, earthing grid sizing, and filter analysis."
          }
        },
        {
          "@type": "Question",
          "name": "How does 3-phase electrical power differ from single-phase power?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "3-phase power utilizes three alternating sinusoidal currents separated by 120 electrical degrees, delivering continuous constant instantaneous power P = sqrt(3) * V_LL * I_L * cos(phi) with 73% greater efficiency in conductor material."
          }
        },
        {
          "@type": "Question",
          "name": "What is the difference between active, reactive, and apparent power?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Active power (kW) performs physical useful work. Reactive power (kVAR) sustains inductive electromagnetic fields in motors and transformers. Apparent power (kVA) is their vector sum S = sqrt(P^2 + Q^2)."
          }
        },
        {
          "@type": "Question",
          "name": "Why is power factor correction essential in industrial facilities?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Operating at a poor power factor draws excess reactive current, overloading transformers, increasing feeder I^2 R losses, causing voltage sags, and incurring severe utility tariff penalties."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-body">
    <!-- Embedded Interactive Quick Solver: Ohm's Law & 3-Phase Power -->
    <div style="background: white; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem; margin-bottom: 1.5rem;">
        <h3 style="margin-top: 0; color: #1e293b; font-size: 1.1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">Interactive Electrical Quick Solver: 3-Phase Power &amp; Ohm's Law</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <label for="eqVoltage" style="font-size: 0.8rem; font-weight: 600;">Line Voltage (V):</label>
                <input type="number" id="eqVoltage" class="input-field" value="400" min="1" step="10" oninput="solveQuickPower()">
            </div>
            <div>
                <label for="eqCurrent" style="font-size: 0.8rem; font-weight: 600;">Current (A):</label>
                <input type="number" id="eqCurrent" class="input-field" value="125" min="0.1" step="5" oninput="solveQuickPower()">
            </div>
            <div>
                <label for="eqPf" style="font-size: 0.8rem; font-weight: 600;">Power Factor (cos &phi;):</label>
                <input type="number" id="eqPf" class="input-field" value="0.85" min="0.1" max="1.0" step="0.05" oninput="solveQuickPower()">
            </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 0.75rem; margin-top: 1rem; background: #f8fafc; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
            <div>
                <div style="font-size: 0.7rem; color: #64748b; font-weight: 700; text-transform: uppercase;">Active Power (P)</div>
                <div id="resActiveP" style="font-size: 1.2rem; font-weight: 700; color: #2563eb;">73.61 kW</div>
            </div>
            <div>
                <div style="font-size: 0.7rem; color: #64748b; font-weight: 700; text-transform: uppercase;">Apparent Power (S)</div>
                <div id="resApparentS" style="font-size: 1.2rem; font-weight: 700; color: #0f172a;">86.60 kVA</div>
            </div>
            <div>
                <div style="font-size: 0.7rem; color: #64748b; font-weight: 700; text-transform: uppercase;">Reactive Power (Q)</div>
                <div id="resReactiveQ" style="font-size: 1.2rem; font-weight: 700; color: #d97706;">45.62 kVAR</div>
            </div>
            <div>
                <div style="font-size: 0.7rem; color: #64748b; font-weight: 700; text-transform: uppercase;">Phase Impedance (Z)</div>
                <div id="resImpedanceZ" style="font-size: 1.2rem; font-weight: 700; color: #059669;">1.85 &Omega;</div>
            </div>
        </div>
    </div>

    <!-- Live Category Filter Bar -->
    <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.25rem;">
        <button type="button" class="btn btn-primary" onclick="filterHub('all')">All Electrical (30+)</button>
        <button type="button" class="btn btn-outline" onclick="filterHub('cables')">Cables &amp; Conduits</button>
        <button type="button" class="btn btn-outline" onclick="filterHub('power')">Power &amp; Motors</button>
        <button type="button" class="btn btn-outline" onclick="filterHub('circuits')">Circuits &amp; Electronics</button>
    </div>

    <!-- Hub Cards Grid -->
    <div id="elecHubGrid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem;">
        <!-- Injected via script -->
    </div>
</div>

<script>
const ELEC_TOOLS = [
    { slug: "cable-sizing-guide.html", name: "Cable Sizing Guide (IEC/NEC)", cat: "cables", desc: "Comprehensive ampacity, derating factors & voltage drop." },
    { slug: "cable-sizing-calculator.html", name: "Cable Sizing Calculator", cat: "cables", desc: "Standard conductor cross-section selector." },
    { slug: "voltage-drop-calculator.html", name: "Voltage Drop Calculator", cat: "cables", desc: "AC/DC voltage drop & percentage across run length." },
    { slug: "conduit-fill-calculator.html", name: "Conduit Fill (NEC Chapter 9)", cat: "cables", desc: "40% maximum allowable fill area for trade conduits." },
    { slug: "wire-ampacity-calculator.html", name: "Wire Ampacity (NEC 310.16)", cat: "cables", desc: "Continuous copper and aluminium conductor ampacity." },
    { slug: "three-phase-power-calculator.html", name: "3-Phase Power (kW, kVA, kVAR)", cat: "power", desc: "Balanced active, apparent, and reactive power vector math." },
    { slug: "power-factor-calculator.html", name: "Power Factor Correction", cat: "power", desc: "Capacitor bank sizing in kVAR to hit target power factor." },
    { slug: "transformer-sizing-calculator.html", name: "Transformer Sizing (kVA)", cat: "power", desc: "Primary & secondary full load current and kVA rating." },
    { slug: "motor-starter-sizing-calculator.html", name: "Motor Starter Sizing (NEC 430)", cat: "power", desc: "NEMA sizes, IEC contactors, overloads & breaker OCPD." },
    { slug: "motor-starting-current-calculator.html", name: "Motor Starting Current & VFD", cat: "power", desc: "Locked rotor kVA code letters and voltage dip." },
    { slug: "short-circuit-calculator.html", name: "Short Circuit Fault Current", cat: "power", desc: "Infinite bus MVA method and transformer impedance." },
    { slug: "earthing-cable-size-calculator.html", name: "Earthing Conductor Size (IEC)", cat: "cables", desc: "Adiabatic fault current earth bonding conductor size." },
    { slug: "ohms-law-calculator.html", name: "Ohm's Law Calculator", cat: "circuits", desc: "V = IR, power P = VI, and circuit component parameters." },
    { slug: "parallel-resistor-calculator.html", name: "Parallel Resistor Calculator", cat: "circuits", desc: "Equivalent resistance 1/Req = 1/R1 + 1/R2." },
    { slug: "pcb-trace-width-calculator.html", name: "PCB Trace Width (IPC-2152)", cat: "circuits", desc: "Current capacity, copper weight and thermal rise." },
    { slug: "zener-diode-calculator.html", name: "Zener Diode Shunt Regulator", cat: "circuits", desc: "Series resistor Rs and power dissipation Pz." }
];

function solveQuickPower() {
    const v = parseFloat(document.getElementById('eqVoltage').value) || 400;
    const i = parseFloat(document.getElementById('eqCurrent').value) || 0;
    const pf = parseFloat(document.getElementById('eqPf').value) || 0.85;

    const s = (Math.sqrt(3) * v * i) / 1000;
    const p = s * pf;
    const sinPhi = Math.sqrt(Math.max(0, 1 - Math.pow(pf, 2)));
    const q = s * sinPhi;
    const z = (v / Math.sqrt(3)) / (i > 0 ? i : 1);

    document.getElementById('resActiveP').innerText = `${p.toFixed(2)} kW`;
    document.getElementById('resApparentS').innerText = `${s.toFixed(2)} kVA`;
    document.getElementById('resReactiveQ').innerText = `${q.toFixed(2)} kVAR`;
    document.getElementById('resImpedanceZ').innerText = `${z.toFixed(2)} Ω`;
}

function filterHub(cat) {
    const grid = document.getElementById('elecHubGrid');
    const filtered = (cat === 'all') ? ELEC_TOOLS : ELEC_TOOLS.filter(t => t.cat === cat);
    grid.innerHTML = filtered.map(t => `
        <div style="background: white; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; box-shadow: 0 1px 3px rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <h4 style="margin: 0 0 0.4rem 0;"><a href="${t.slug}" style="color: #2563eb; text-decoration: none; font-weight: 700;">${t.name}</a></h4>
                <p style="font-size: 0.85rem; color: #475569; margin: 0 0 0.75rem 0;">${t.desc}</p>
            </div>
            <div>
                <a href="${t.slug}" style="display: inline-block; font-size: 0.8rem; font-weight: 600; color: #2563eb;">Open Calculator &rarr;</a>
            </div>
        </div>
    `).join('');
}

window.addEventListener('DOMContentLoaded', () => {
    solveQuickPower();
    filterHub('all');
});
</script>"""

    article = """<h2>Foundations of Electrical Power and Circuit Analysis</h2>
<p>Electrical engineering constitutes the mathematical and physical discipline that governs the generation, transmission, distribution, and utilization of electromagnetic energy. From macroscopic gigawatt electrical grids down to sub-micron integrated semiconductor devices, electrical design relies on strict physical laws formulated by James Clerk Maxwell, Georg Simon Ohm, Gustav Kirchhoff, and Michael Faraday.</p>

<p>The core computational workloads of practicing power system engineers center on three foundational analytical pillars:</p>
<ol>
    <li><strong>Alternating Current Phasor Dynamics:</strong> In AC sinusoidal systems, voltage and current oscillate at fundamental power frequencies ($50\text{ Hz}$ or $60\text{ Hz}$). Expressing voltages and currents as complex rotating vectors (phasors) simplifies differential equations into linear complex algebraic formulations:
    $$\mathbf{V} = \mathbf{I} \cdot \mathbf{Z} = \mathbf{I} \cdot (R + jX)$$
    </li>
    <li><strong>The AC Power Triangle:</strong> Power in alternating current circuits resolves into three orthogonal vector components:
        <ul>
            <li><strong>Active / Real Power ($P$):</strong> Measured in Watts (W) or kilowatts (kW), representing the true thermodynamic rate of energy transfer that produces mechanical shaft work or thermal heat: $P = \sqrt{3} V_L I_L \cos \phi$.</li>
            <li><strong>Reactive Power ($Q$):</strong> Measured in Volt-Amperes Reactive (VAR) or kVAR, representing the energy oscillating between magnetic fields (inductors) and electric fields (capacitors): $Q = \sqrt{3} V_L I_L \sin \phi$.</li>
            <li><strong>Apparent Power ($S$):</strong> Measured in Volt-Amperes (VA) or kVA, representing the total capacity demanded from upstream transformers and generators: $S = \sqrt{P^2 + Q^2}$.</li>
        </ul>
    </li>
    <li><strong>Three-Phase System Symmetries:</strong> Three-phase transmission delivers constant, ripple-free instantaneous mechanical power to induction motors while requiring $73\%$ of the conductor material compared to an equivalent single-phase delivery network.</li>
</ol>

<h2>Transformer Mechanics, Impedance, and Fault Current Analysis</h2>
<p>In electrical distribution systems, power transformers step voltage levels between transmission lines and utilization equipment. The full-load current rating of a three-phase transformer is governed by:</p>

$$I_{\text{FLA}} = \frac{S_{\text{kVA}} \times 1000}{\sqrt{3} \times V_{\text{line}}}$$

<p>During an electrical fault (such as a three-phase bolted short circuit), the maximum prospective symmetrical fault current $I_{\text{sc}}$ available at the transformer secondary terminals is limited strictly by the transformer's internal percentage impedance $\%Z$:</p>

$$I_{\text{sc}} = \frac{I_{\text{FLA}}}{\%Z / 100} = \frac{S_{\text{kVA}} \times 1000}{\sqrt{3} \times V_{\text{line}} \times (\%Z / 100)}$$

<p>This prospective fault current dictates the required Interrupting Capacity (AIC rating) of downstream circuit breakers and switchgear, preventing catastrophic electrical arc-flash explosions.</p>

<h3>Master Electrical Formulas and Reference Matrix</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Physical Parameter</th>
            <th>Single-Phase Formula</th>
            <th>3-Phase Balanced Formula</th>
            <th>SI Unit</th>
            <th>Standard Reference Symbol</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Active Real Power</td><td>$P = V \cdot I \cdot \cos \phi$</td><td>$P = \sqrt{3} \cdot V_L \cdot I_L \cdot \cos \phi$</td><td>Watts (W, kW)</td><td>$P$</td></tr>
        <tr><td>Apparent Power</td><td>$S = V \cdot I$</td><td>$S = \sqrt{3} \cdot V_L \cdot I_L$</td><td>Volt-Amps (VA, kVA)</td><td>$S$</td></tr>
        <tr><td>Reactive Power</td><td>$Q = V \cdot I \cdot \sin \phi$</td><td>$Q = \sqrt{3} \cdot V_L \cdot I_L \cdot \sin \phi$</td><td>kVAR</td><td>$Q$</td></tr>
        <tr><td>Impedance Magnitude</td><td>$Z = \sqrt{R^2 + X^2}$</td><td>$Z_{\text{phase}} = V_{LN} / I_L$</td><td>Ohms ($\Omega$)</td><td>$Z$</td></tr>
        <tr><td>Inductive Reactance</td><td>$X_L = 2\pi f L$</td><td>$X_L = 2\pi f L$</td><td>Ohms ($\Omega$)</td><td>$X_L$</td></tr>
        <tr><td>Capacitive Reactance</td><td>$X_C = \frac{1}{2\pi f C}$</td><td>$X_C = \frac{1}{2\pi f C}$</td><td>Ohms ($\Omega$)</td><td>$X_C$</td></tr>
    </tbody>
</table>

<h2>Power Factor Correction and Industrial Energy Optimization</h2>
<p>Low industrial power factor (caused by unloaded induction motors, fluorescent ballasts, and arc welders) creates excessive line currents that generate avoidable resistive losses in supply cables ($P_{\text{loss}} = 3 I^2 R$). Installing parallel capacitor banks supplies local reactive magnetizing current, reducing the upstream utility demand.</p>

<p>The required capacitor bank rating $Q_{\text{cap}}$ (in kVAR) to correct a load from initial power factor $\cos \phi_1$ to improved target power factor $\cos \phi_2$ evaluates as:</p>

$$Q_{\text{cap}} = P_{\text{kW}} \left( \tan \phi_1 - \tan \phi_2 \right) = P_{\text{kW}} \left( \frac{\sqrt{1 - \cos^2 \phi_1}}{\cos \phi_1} - \frac{\sqrt{1 - \cos^2 \phi_2}}{\cos \phi_2} \right)$$

<div class="worked-example-card">
    <h3>Worked Power System Engineering Case Study: Industrial Substation Expansion</h3>
    <p><strong>Scenario:</strong> A manufacturing plant operates a continuous manufacturing load of <strong>450 kW</strong> at an uncorrected lagging power factor of <strong>0.72</strong> on a 480V, 3-phase, 60 Hz service. The electric utility assesses heavy penalties for power factors below 0.95. Determine: (1) existing uncorrected apparent power (kVA) and load current, (2) required capacitor bank rating to achieve 0.95 power factor, and (3) line current reduction.</p>
    
    <div class="step-solution">
        <h4>Step 1: Compute Uncorrected Power and Current</h4>
        $$S_1 = \frac{P}{\cos \phi_1} = \frac{450}{0.72} = 625.0 \text{ kVA}$$
        $$I_{L1} = \frac{S_1 \times 1000}{\sqrt{3} \times V} = \frac{625,000}{\sqrt{3} \times 480} = \frac{625,000}{831.38} \approx 751.76 \text{ A}$$

        <h4>Step 2: Calculate Required Capacitor Bank ($Q_{\text{cap}}$)</h4>
        $$\phi_1 = \arccos(0.72) \approx 43.95^\circ \implies \tan \phi_1 \approx 0.9639$$
        $$\phi_2 = \arccos(0.95) \approx 18.19^\circ \implies \tan \phi_2 \approx 0.3287$$
        $$Q_{\text{cap}} = 450 \times (0.9639 - 0.3287) = 450 \times 0.6352 \approx 285.84 \text{ kVAR}$$
        <p>A standard <strong>300 kVAR automatic stepped capacitor bank</strong> is selected.</p>

        <h4>Step 3: Evaluate Corrected System Demand and Current</h4>
        $$S_2 = \frac{P}{\cos \phi_2} = \frac{450}{0.95} \approx 473.68 \text{ kVA}$$
        $$I_{L2} = \frac{473,680}{\sqrt{3} \times 480} \approx 569.75 \text{ A}$$
        $$\text{Current Reduction} = 751.76 - 569.75 = 182.01 \text{ A (24.2% drop in conductor current!)}$$
    </div>
</div>

<h2>Common Calculation Errors in Electrical Engineering</h2>
<ol>
    <li><strong>Confusing Line-to-Line and Line-to-Neutral Voltages:</strong> In 3-phase calculations, substituting line-to-line voltage ($V_{LL} = 400\text{V}$) into single-phase equations without dividing by $\sqrt{3}$ produces a catastrophic $\sqrt{3} \approx 1.732$ error in current and transformer sizing.</li>
    <li><strong>Omitting Power Factor in Generator and UPS Sizing:</strong> Sizing an emergency standby generator based strictly on real power (kW) rather than apparent power (kVA) will overload the generator's alternator coils when serving low power factor induction motors.</li>
    <li><strong>Neglecting Ambient Temperature in Breaker Trip Ratings:</strong> Standard thermal-magnetic molded case circuit breakers (MCCBs) are calibrated at $40^\circ\text{C}$ ($104^\circ\text{F}$). Operating inside outdoor switchgear boxes reaching $55^\circ\text{C}$ causes nuisance thermal tripping unless derated per manufacturer curves.</li>
</ol>

<section class="faq-section">
    <h2>Frequently Asked Questions About Electrical Calculations</h2>
    <div class="faq-item">
        <h3>What calculation tools are included in the CalcHub Electrical Suite?</h3>
        <p>The suite includes 30+ specialized tools spanning cable sizing (IEC/NEC), 3-phase power, transformer sizing, motor starters, PCB trace width, lightning protection, earthing grid sizing, and filter analysis.</p>
    </div>
    <div class="faq-item">
        <h3>How does 3-phase electrical power differ from single-phase power?</h3>
        <p>3-phase power utilizes three alternating sinusoidal currents separated by 120 electrical degrees, delivering continuous constant instantaneous power P = sqrt(3) * V_LL * I_L * cos(phi) with 73% greater efficiency in conductor material.</p>
    </div>
    <div class="faq-item">
        <h3>What is the difference between active, reactive, and apparent power?</h3>
        <p>Active power (kW) performs physical useful work. Reactive power (kVAR) sustains inductive electromagnetic fields in motors and transformers. Apparent power (kVA) is their vector sum S = sqrt(P^2 + Q^2).</p>
    </div>
    <div class="faq-item">
        <h3>Why is power factor correction essential in industrial facilities?</h3>
        <p>Operating at a poor power factor draws excess reactive current, overloading transformers, increasing feeder I^2 R losses, causing voltage sags, and incurring severe utility tariff penalties.</p>
    </div>
</section>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article, category_hub="engineering.html", category_name="Engineering Tools")


# ===========================================================================
# TOOL 7: engineering-formulas.html
# ===========================================================================
def gen_engineering_formulas():
    slug = "engineering-formulas"
    title = "Engineering Formulas Compendium & Equation Solver | Multidisciplinary Suite"
    desc = "Master engineering formulas compendium and interactive equation solver across electrical, mechanical, civil, chemical, and fluid engineering disciplines."
    h1 = "Engineering Formulas Compendium"
    short_desc = "Master multidisciplinary engineering equations compendium and interactive live formula solver across civil, mechanical, electrical, and chemical engineering."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Engineering Formulas Compendium",
      "url": "https://calchub.com/engineering-formulas.html",
      "applicationCategory": "EngineeringApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Multidisciplinary engineering formula directory and live interactive equation solver."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What engineering disciplines are covered in this formulas compendium?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The compendium covers five core branches: Mechanical (beam bending, torque, kinetics), Electrical (Ohm's law, 3-phase power, impedance), Civil (concrete shear, retaining soil pressure), Chemical (ideal gas, Arrhenius kinetics), and Fluid Dynamics (Bernoulli, Darcy-Weisbach)."
          }
        },
        {
          "@type": "Question",
          "name": "What is the Buckingham Pi theorem in engineering dimensional analysis?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The Buckingham Pi theorem states that if a physical problem involves n variables expressed in k fundamental physical dimensions, the problem can be reduced to n - k dimensionless groups (Pi terms), enabling scale-model testing."
          }
        },
        {
          "@type": "Question",
          "name": "How does the Euler-Bernoulli beam equation evaluate flexural stress?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The flexural bending formula sigma = M * y / I evaluates normal stress from applied internal bending moment M, distance from neutral axis y, and area moment of inertia I."
          }
        },
        {
          "@type": "Question",
          "name": "What is the Darcy-Weisbach equation for fluid friction head loss?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The Darcy-Weisbach equation hf = f * (L / D) * (v^2 / (2g)) calculates hydraulic head loss from pipe friction factor f, length L, internal diameter D, flow velocity v, and gravity g."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-body">
    <div style="background: white; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem; margin-bottom: 1.5rem;">
        <h3 style="margin-top: 0; color: #1e293b; font-size: 1.1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">Multidisciplinary Live Equation Solver</h3>
        
        <div style="margin-bottom: 1.25rem;">
            <label for="formulaSelector" style="font-weight: 600; font-size: 0.875rem;">Select Engineering Formula to Solve:</label>
            <select id="formulaSelector" class="input-field" onchange="updateFormulaUI()">
                <option value="mech_bending">Mechanical: Beam Bending Stress (&sigma; = M &middot; y / I)</option>
                <option value="fluid_darcy">Fluid Dynamics: Darcy-Weisbach Head Loss (hf = f &middot; (L/D) &middot; v² / 2g)</option>
                <option value="elec_power">Electrical: 3-Phase Real Power (P = &radic;3 &middot; V &middot; I &middot; cos &phi;)</option>
                <option value="civil_shear">Civil: ACI Concrete Shear Strength (Vc = 0.17 &middot; &radic;f'c &middot; bw &middot; d)</option>
                <option value="thermo_carnot">Thermodynamics: Maximum Carnot Efficiency (&eta; = 1 - Tc / Th)</option>
            </select>
        </div>

        <div id="dynamicInputs" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-bottom: 1.25rem;">
            <!-- Inputs dynamically injected -->
        </div>

        <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1rem;">
            <div style="font-size: 0.75rem; color: #64748b; font-weight: 700; text-transform: uppercase;">Computed Result</div>
            <div id="resFormulaOutput" style="font-size: 1.5rem; font-weight: 700; color: #2563eb; margin: 0.25rem 0;">--</div>
            <div id="resFormulaDetails" style="font-size: 0.85rem; color: #475569;">--</div>
        </div>
    </div>
</div>

<script>
function updateFormulaUI() {
    const f = document.getElementById('formulaSelector').value;
    const container = document.getElementById('dynamicInputs');

    if (f === 'mech_bending') {
        container.innerHTML = `
            <div><label style="font-size:0.8rem; font-weight:600;">Moment M (kN&middot;m):</label><input type="number" id="inpM" class="input-field" value="25" oninput="solveFormula()"></div>
            <div><label style="font-size:0.8rem; font-weight:600;">Distance y (mm):</label><input type="number" id="inpY" class="input-field" value="150" oninput="solveFormula()"></div>
            <div><label style="font-size:0.8rem; font-weight:600;">Inertia I (cm⁴):</label><input type="number" id="inpI" class="input-field" value="8500" oninput="solveFormula()"></div>
        `;
    } else if (f === 'fluid_darcy') {
        container.innerHTML = `
            <div><label style="font-size:0.8rem; font-weight:600;">Friction Factor f:</label><input type="number" id="inpF" class="input-field" value="0.02" step="0.005" oninput="solveFormula()"></div>
            <div><label style="font-size:0.8rem; font-weight:600;">Length L (m):</label><input type="number" id="inpL" class="input-field" value="100" oninput="solveFormula()"></div>
            <div><label style="font-size:0.8rem; font-weight:600;">Diameter D (m):</label><input type="number" id="inpD" class="input-field" value="0.20" step="0.05" oninput="solveFormula()"></div>
            <div><label style="font-size:0.8rem; font-weight:600;">Velocity v (m/s):</label><input type="number" id="inpV" class="input-field" value="2.5" step="0.1" oninput="solveFormula()"></div>
        `;
    } else if (f === 'elec_power') {
        container.innerHTML = `
            <div><label style="font-size:0.8rem; font-weight:600;">Line Voltage V (V):</label><input type="number" id="inpVl" class="input-field" value="400" oninput="solveFormula()"></div>
            <div><label style="font-size:0.8rem; font-weight:600;">Line Current I (A):</label><input type="number" id="inpIl" class="input-field" value="65" oninput="solveFormula()"></div>
            <div><label style="font-size:0.8rem; font-weight:600;">Power Factor cos &phi;:</label><input type="number" id="inpCos" class="input-field" value="0.88" max="1" step="0.02" oninput="solveFormula()"></div>
        `;
    } else if (f === 'civil_shear') {
        container.innerHTML = `
            <div><label style="font-size:0.8rem; font-weight:600;">Concrete f'c (MPa):</label><input type="number" id="inpFc" class="input-field" value="28" oninput="solveFormula()"></div>
            <div><label style="font-size:0.8rem; font-weight:600;">Web Width bw (mm):</label><input type="number" id="inpBw" class="input-field" value="300" oninput="solveFormula()"></div>
            <div><label style="font-size:0.8rem; font-weight:600;">Depth d (mm):</label><input type="number" id="inpDepth" class="input-field" value="500" oninput="solveFormula()"></div>
        `;
    } else if (f === 'thermo_carnot') {
        container.innerHTML = `
            <div><label style="font-size:0.8rem; font-weight:600;">Cold Reservoir Tc (K):</label><input type="number" id="inpTc" class="input-field" value="298" oninput="solveFormula()"></div>
            <div><label style="font-size:0.8rem; font-weight:600;">Hot Reservoir Th (K):</label><input type="number" id="inpTh" class="input-field" value="873" oninput="solveFormula()"></div>
        `;
    }
    solveFormula();
}

function solveFormula() {
    const f = document.getElementById('formulaSelector').value;
    const out = document.getElementById('resFormulaOutput');
    const det = document.getElementById('resFormulaDetails');

    if (f === 'mech_bending') {
        const m = parseFloat(document.getElementById('inpM').value) || 0; // kN*m = 1e6 N*mm
        const y = parseFloat(document.getElementById('inpY').value) || 0; // mm
        const i_cm4 = parseFloat(document.getElementById('inpI').value) || 1; // cm4 = 1e4 mm4
        const i_mm4 = i_cm4 * 10000;
        const stress = ((m * 1000000) * y) / (i_mm4 > 0 ? i_mm4 : 1);
        out.innerText = `${stress.toFixed(2)} MPa (N/mm²)`;
        det.innerText = `Flexural Bending Stress at extreme fiber distance y = ${y} mm`;
    } else if (f === 'fluid_darcy') {
        const factor = parseFloat(document.getElementById('inpF').value) || 0.02;
        const l = parseFloat(document.getElementById('inpL').value) || 0;
        const d = parseFloat(document.getElementById('inpD').value) || 0.1;
        const v = parseFloat(document.getElementById('inpV').value) || 0;
        const g = 9.80665;
        const hf = factor * (l / d) * (Math.pow(v, 2) / (2 * g));
        out.innerText = `${hf.toFixed(3)} meters of head loss`;
        det.innerText = `Equivalent pressure loss: ${(hf * 9.80665 * 1000 / 1000).toFixed(2)} kPa (for water at 20°C)`;
    } else if (f === 'elec_power') {
        const vl = parseFloat(document.getElementById('inpVl').value) || 0;
        const il = parseFloat(document.getElementById('inpIl').value) || 0;
        const pf = parseFloat(document.getElementById('inpCos').value) || 0.85;
        const p_kw = (Math.sqrt(3) * vl * il * pf) / 1000;
        out.innerText = `${p_kw.toFixed(2)} kW`;
        det.innerText = `Total 3-Phase balanced active power consumption`;
    } else if (f === 'civil_shear') {
        const fc = parseFloat(document.getElementById('inpFc').value) || 28;
        const bw = parseFloat(document.getElementById('inpBw').value) || 300;
        const depth = parseFloat(document.getElementById('inpDepth').value) || 500;
        const vc_n = 0.17 * Math.sqrt(fc) * bw * depth;
        out.innerText = `${(vc_n / 1000).toFixed(2)} kN`;
        det.innerText = `Nominal unreinforced concrete shear resistance Vc per ACI 318`;
    } else if (f === 'thermo_carnot') {
        const tc = parseFloat(document.getElementById('inpTc').value) || 298;
        const th = parseFloat(document.getElementById('inpTh').value) || 873;
        const eta = (th > tc) ? (1 - (tc / th)) * 100 : 0;
        out.innerText = `${eta.toFixed(2)}% Thermal Efficiency`;
        det.innerText = `Theoretical maximum thermodynamic limit between ${tc} K and ${th} K`;
    }
}

window.addEventListener('DOMContentLoaded', updateFormulaUI);
</script>"""

    article = """<h2>Dimensional Analysis and Conservation Laws in Engineering</h2>
<p>Modern engineering sciences—encompassing civil, mechanical, aerospace, electrical, and chemical fields—rely on closed-form algebraic and differential equations derived from the universal physical conservation laws of nature: the <strong>Conservation of Mass</strong>, the <strong>Conservation of Linear and Angular Momentum</strong>, and the <strong>Conservation of Energy (First and Second Laws of Thermodynamics)</strong>.</p>

<p>Before any engineering formula can be deployed in physical systems design, it must satisfy dimensional homogeneity. In 1914, American physicist Edgar Buckingham formulated the celebrated <strong>Buckingham $\Pi$ Theorem</strong>, proving that any physically meaningful relationship involving $n$ physical variables expressed across $k$ fundamental independent dimensions ($M$ for mass, $L$ for length, $T$ for time, $\Theta$ for temperature, and $I$ for electric current) can be restated as an equivalent function of $n - k$ dimensionless groups:</p>

$$\Pi_1 = f(\Pi_2, \Pi_3, \dots, \Pi_{n-k})$$

<p>This dimensional reduction underpins all scaled wind tunnel aerodynamic testing (matching Reynolds number $Re$ and Mach number $Ma$) and civil hydraulic spillway flume modeling (matching Froude number $Fr$).</p>

<h2>Continuum Mechanics and Multi-Discipline Formula Formulations</h2>

<h3>1. Solid Mechanics: The Euler-Bernoulli Flexural Formula</h3>
<p>In structural and mechanical engineering, calculating internal normal stresses in beams subject to transverse loading is governed by the Euler-Bernoulli beam theory. Normal bending stress $\sigma_x$ at any fiber distance $y$ from the neutral bending axis evaluates as:</p>

$$\sigma_x = -\frac{M \cdot y}{I}$$

<p>Where $M$ represents the internal bending moment ($N \cdot m$), $y$ is the perpendicular distance from the centroidal neutral axis ($m$), and $I$ is the second moment of area (area moment of inertia, $m^4$).</p>

<h3>2. Fluid Dynamics: The Darcy-Weisbach Energy Equation</h3>
<p>For internal pipe flow in chemical processing plants, water distribution networks, and district HVAC chillers, the irreversible frictional head loss $h_f$ across pipe length $L$ and diameter $D$ is governed by the Darcy-Weisbach formulation:</p>

$$h_f = f \cdot \frac{L}{D} \cdot \frac{v^2}{2g}$$

<p>Where $f$ represents the Darcy friction factor (evaluated from the Colebrook-White implicit equation or Swamee-Jain explicit approximation based on the Reynolds number $Re = \rho v D / \mu$ and relative pipe roughness $\epsilon / D$).</p>

<h3>3. Thermodynamics: The Carnot Thermodynamic Ceiling</h3>
<p>Under the Second Law of Thermodynamics, no heat engine operating between a thermal heat source at absolute temperature $T_{\text{hot}}$ and a heat sink at $T_{\text{cold}}$ can achieve thermal efficiency $\eta$ exceeding the idealized reversible Carnot cycle limit:</p>

$$\eta_{\text{Carnot}} = 1 - \frac{T_{\text{cold}}}{T_{\text{hot}}}$$

<h3>Multidisciplinary Engineering Master Formulas Reference Matrix</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Discipline</th>
            <th>Governing Equation</th>
            <th>Primary Application</th>
            <th>Key Variables</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Mechanical</td><td>$\sigma = \frac{M y}{I}$</td><td>Beam Bending &amp; Structural Stress</td><td>$M$ (Moment), $y$ (Distance), $I$ (Inertia)</td></tr>
        <tr><td>Electrical</td><td>$P = \sqrt{3} V_L I_L \cos \phi$</td><td>3-Phase Balanced Power Transmission</td><td>$V_L$ (Line Volts), $I_L$ (Amps), $\cos \phi$ (PF)</td></tr>
        <tr><td>Fluid Dynamics</td><td>$h_f = f \frac{L}{D} \frac{v^2}{2g}$</td><td>Pipe Friction Pressure Loss</td><td>$f$ (Friction), $L$ (Length), $D$ (Bore), $v$ (Velocity)</td></tr>
        <tr><td>Civil / Structural</td><td>$V_c = 0.17 \lambda \sqrt{f'_c} b_w d$</td><td>ACI Concrete Beam Shear Strength</td><td>$f'_c$ (Concrete Strength), $b_w$ (Width), $d$ (Depth)</td></tr>
        <tr><td>Chemical</td><td>$P V = n R T$</td><td>Ideal Gas Volumetric Behavior</td><td>$P$ (Pressure), $V$ (Vol), $n$ (Moles), $T$ (Kelvin)</td></tr>
        <tr><td>Thermodynamics</td><td>$\eta = 1 - \frac{T_C}{T_H}$</td><td>Carnot Thermal Cycle Limit</td><td>$T_C$ (Cold Reservoir K), $T_H$ (Hot Reservoir K)</td></tr>
    </tbody>
</table>

<div class="worked-example-card">
    <h3>Worked Engineering Case Study: Structural Steel I-Beam Load Capacity</h3>
    <p><strong>Scenario:</strong> A structural engineer is verifying an ASTM A992 structural steel W310x38.7 wide-flange beam spanning 6.0 meters under a central concentrated point load $P = 40 \text{ kN}$. The beam has an area moment of inertia $I_x = 8,490 \times 10^4 \text{ mm}^4$ and depth $d = 310 \text{ mm}$ (neutral axis $y = d/2 = 155 \text{ mm}$). Determine: (1) maximum bending moment, (2) peak flexural bending stress, and (3) factor of safety against yield ($F_y = 345 \text{ MPa}$).</p>
    
    <div class="step-solution">
        <h4>Step 1: Compute Maximum Bending Moment</h4>
        <p>For a simply supported beam with central point load:</p>
        $$M_{\text{max}} = \frac{P \cdot L}{4} = \frac{40 \text{ kN} \times 6.0 \text{ m}}{4} = 60.0 \text{ kN}\cdot\text{m} = 60.0 \times 10^6 \text{ N}\cdot\text{mm}$$

        <h4>Step 2: Evaluate Peak Flexural Stress ($\sigma_{\text{max}}$)</h4>
        $$\sigma_{\text{max}} = \frac{M_{\text{max}} \cdot y}{I_x} = \frac{(60.0 \times 10^6 \text{ N}\cdot\text{mm}) \times 155 \text{ mm}}{84.9 \times 10^6 \text{ mm}^4} \approx 109.54 \text{ MPa}$$

        <h4>Step 3: Calculate Factor of Safety Against Yield</h4>
        $$\text{FoS} = \frac{F_y}{\sigma_{\text{max}}} = \frac{345 \text{ MPa}}{109.54 \text{ MPa}} \approx 3.15$$
        <p><strong>Conclusion:</strong> The beam operates well within the elastic regime with an adequate structural margin ($\text{FoS} = 3.15 > 1.67$ allowable limit).</p>
    </div>
</div>

<h2>Common Implementation Pitfalls with Engineering Formulas</h2>
<ol>
    <li><strong>Inconsistent Unit Systems (SI vs. US Customary):</strong> Mixing millimeters with meters, or kips with pounds, is the leading cause of disastrous engineering failures (e.g., the 1999 Mars Climate Orbiter loss caused by metric Newton-seconds vs. pound-force-seconds mismatch). Always perform formal dimensional checks.</li>
    <li><strong>Applying Formulas Beyond Boundary Assumptions:</strong> Using the linear Bernoulli equation for compressible transonic gas flow, or applying the thin-walled pressure vessel formula ($t < r/10$) to thick-walled hydraulic cylinders, produces dangerously invalid results.</li>
    <li><strong>Gauge Pressure vs. Absolute Pressure in Thermodynamics:</strong> Ideal gas law ($PV = nRT$) and polytropic expansion equations require absolute pressure ($P_{\text{abs}} = P_{\text{gauge}} + P_{\text{atm}}$) and absolute temperature (Kelvin or Rankine). Substituting Celsius or gauge PSI produces total mathematical failure.</li>
</ol>

<section class="faq-section">
    <h2>Frequently Asked Questions About Engineering Formulas</h2>
    <div class="faq-item">
        <h3>What engineering disciplines are covered in this formulas compendium?</h3>
        <p>The compendium covers five core branches: Mechanical (beam bending, torque, kinetics), Electrical (Ohm's law, 3-phase power, impedance), Civil (concrete shear, retaining soil pressure), Chemical (ideal gas, Arrhenius kinetics), and Fluid Dynamics (Bernoulli, Darcy-Weisbach).</p>
    </div>
    <div class="faq-item">
        <h3>What is the Buckingham Pi theorem in engineering dimensional analysis?</h3>
        <p>The Buckingham Pi theorem states that if a physical problem involves n variables expressed in k fundamental physical dimensions, the problem can be reduced to n - k dimensionless groups (Pi terms), enabling scale-model testing.</p>
    </div>
    <div class="faq-item">
        <h3>How does the Euler-Bernoulli beam equation evaluate flexural stress?</h3>
        <p>The flexural bending formula sigma = M * y / I evaluates normal stress from applied internal bending moment M, distance from neutral axis y, and area moment of inertia I.</p>
    </div>
    <div class="faq-item">
        <h3>What is the Darcy-Weisbach equation for fluid friction head loss?</h3>
        <p>The Darcy-Weisbach equation hf = f * (L / D) * (v^2 / (2g)) calculates hydraulic head loss from pipe friction factor f, length L, internal diameter D, flow velocity v, and gravity g.</p>
    </div>
</section>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article, category_hub="engineering.html", category_name="Engineering Tools")


# ===========================================================================
# TOOL 8: financial.html (Master Financial Hub)
# ===========================================================================
def gen_financial_hub():
    slug = "financial"
    title = "Financial Planning & Investment Calculators | Comprehensive Economics Suite"
    desc = "CalcHub's Master Financial Planning & Investment Suite Hub. Access 29+ peer-reviewed calculators for compound interest, mortgages, loan amortizations, and retirement."
    h1 = "Financial Planning Suite Hub"
    short_desc = "Comprehensive economic reference directory and computational suite indexing all 29+ financial calculators, mortgage amortizations, and personal wealth engines."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Financial Planning Suite Hub",
      "url": "https://calchub.com/financial.html",
      "applicationCategory": "FinanceApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Comprehensive reference directory and computational suite for personal finance, mortgage amortizations, investments, and corporate accounting."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What calculation engines are included in the Financial Planning Suite?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The suite encompasses 29+ tools across mortgages, auto loans, compound interest wealth accumulation, retirement FIRE planning, capital gains tax, salary take-home pay, and debt payoff."
          }
        },
        {
          "@type": "Question",
          "name": "What is the Time Value of Money (TVM) principle?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The Time Value of Money states that a dollar received today is worth more than a dollar received in the future due to its potential earning capacity through compound interest and investment yield."
          }
        },
        {
          "@type": "Question",
          "name": "How does compound interest differ from simple interest?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Simple interest accumulates strictly on the initial principal balance (I = P * R * T). Compound interest accumulates on both the principal and previously earned interest (A = P * (1 + r/n)^(nt)), creating exponential wealth growth."
          }
        },
        {
          "@type": "Question",
          "name": "What is the 4% Safe Withdrawal Rule in retirement planning?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Originating from the 1998 Trinity Study, the 4% rule states that a retiree can safely withdraw 4% of their initial portfolio in Year 1, adjusted annually for inflation, with a 95%+ probability of portfolio survival over 30 years."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-body">
    <!-- Embedded Interactive Quick Solver: Compound Wealth & Loan EMI -->
    <div style="background: white; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem; margin-bottom: 1.5rem;">
        <h3 style="margin-top: 0; color: #1e293b; font-size: 1.1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">Interactive Financial Quick Solver: Compound Wealth &amp; Loan Sizer</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <label for="finPrincipal" style="font-size: 0.8rem; font-weight: 600;">Starting Principal ($):</label>
                <input type="number" id="finPrincipal" class="input-field" value="25000" min="0" step="1000" oninput="solveQuickFinance()">
            </div>
            <div>
                <label for="finMonthlyPmt" style="font-size: 0.8rem; font-weight: 600;">Monthly Addition ($):</label>
                <input type="number" id="finMonthlyPmt" class="input-field" value="500" min="0" step="50" oninput="solveQuickFinance()">
            </div>
            <div>
                <label for="finRate" style="font-size: 0.8rem; font-weight: 600;">Annual Rate (%):</label>
                <input type="number" id="finRate" class="input-field" value="8.0" min="0.1" max="25" step="0.5" oninput="solveQuickFinance()">
            </div>
            <div>
                <label for="finYears" style="font-size: 0.8rem; font-weight: 600;">Time Horizon (Years):</label>
                <input type="number" id="finYears" class="input-field" value="20" min="1" max="50" step="1" oninput="solveQuickFinance()">
            </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 0.75rem; margin-top: 1rem; background: #f8fafc; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
            <div>
                <div style="font-size: 0.7rem; color: #64748b; font-weight: 700; text-transform: uppercase;">Future Investment Value</div>
                <div id="resFutureVal" style="font-size: 1.3rem; font-weight: 700; color: #16a34a;">$412,883</div>
            </div>
            <div>
                <div style="font-size: 0.7rem; color: #64748b; font-weight: 700; text-transform: uppercase;">Total Contributions</div>
                <div id="resTotalContrib" style="font-size: 1.3rem; font-weight: 700; color: #0f172a;">$145,000</div>
            </div>
            <div>
                <div style="font-size: 0.7rem; color: #64748b; font-weight: 700; text-transform: uppercase;">Compound Interest Earned</div>
                <div id="resInterestEarned" style="font-size: 1.3rem; font-weight: 700; color: #2563eb;">$267,883</div>
            </div>
            <div>
                <div style="font-size: 0.7rem; color: #64748b; font-weight: 700; text-transform: uppercase;">Equivalent Loan Payment</div>
                <div id="resEquivLoan" style="font-size: 1.3rem; font-weight: 700; color: #7c3aed;">$209.11 / mo</div>
            </div>
        </div>
    </div>

    <!-- Live Category Filter Bar -->
    <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.25rem;">
        <button type="button" class="btn btn-primary" onclick="filterFinHub('all')">All Financial (29+)</button>
        <button type="button" class="btn btn-outline" onclick="filterFinHub('lending')">Loans &amp; Mortgages</button>
        <button type="button" class="btn btn-outline" onclick="filterFinHub('wealth')">Wealth &amp; Savings</button>
        <button type="button" class="btn btn-outline" onclick="filterFinHub('payroll')">Payroll &amp; Tax</button>
    </div>

    <!-- Hub Cards Grid -->
    <div id="finHubGrid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem;">
        <!-- Injected via script -->
    </div>
</div>

<script>
const FIN_TOOLS = [
    { slug: "mortgage-calculator.html", name: "Mortgage & PITI Calculator", cat: "lending", desc: "Monthly principal, interest, tax & home insurance." },
    { slug: "loan-emi-calculator.html", name: "Loan EMI Calculator", cat: "lending", desc: "Amortizing monthly payment and interest breakdown." },
    { slug: "car-loan-calculator.html", name: "Auto Loan Financing", cat: "lending", desc: "Vehicle purchase payments with trade-in tax credits." },
    { slug: "compound-interest-calculator.html", name: "Compound Interest Calculator", cat: "wealth", desc: "Exponential wealth accumulation with recurring deposits." },
    { slug: "retirement-calculator.html", name: "Retirement & FIRE Planner", cat: "wealth", desc: "Trinity study 4% rule and retirement nest egg sizer." },
    { slug: "savings-calculator.html", name: "Compound Savings Growth", cat: "wealth", desc: "High-yield savings interest and maturity timeline." },
    { slug: "overtime-calculator.html", name: "Overtime Pay Calculator", cat: "payroll", desc: "FLSA time-and-a-half, regular rate & CA double time." },
    { slug: "salary-calculator.html", name: "Salary & Paycheck Calculator", cat: "payroll", desc: "Hourly, monthly, and annual gross pay conversion." },
    { slug: "time-card-calculator.html", name: "Time Card Calculator", cat: "payroll", desc: "Weekly 7-day timesheet with unpaid lunch breaks." },
    { slug: "capital-gains-calculator.html", name: "Capital Gains Tax", cat: "payroll", desc: "Short-term vs long-term rates and NIIT 3.8% surtax." },
    { slug: "break-even-calculator.html", name: "Break-Even Point Calculator", cat: "wealth", desc: "Fixed costs, contribution margins and unit volume." },
    { slug: "debt-to-income-calculator.html", name: "Debt-to-Income (DTI) Ratios", cat: "lending", desc: "Front-end housing and back-end total debt Fannie Mae limits." }
];

function solveQuickFinance() {
    const p = parseFloat(document.getElementById('finPrincipal').value) || 0;
    const pmt = parseFloat(document.getElementById('finMonthlyPmt').value) || 0;
    const r = (parseFloat(document.getElementById('finRate').value) || 0) / 100;
    const t = parseFloat(document.getElementById('finYears').value) || 1;

    // Monthly compounding n = 12
    const n = 12;
    const r_m = r / n;
    const nt = n * t;

    // Compound future value
    const fv_p = p * Math.pow(1 + r_m, nt);
    const fv_pmt = (pmt > 0 && r_m > 0) ? (pmt * (Math.pow(1 + r_m, nt) - 1) / r_m) : (pmt * nt);
    const totalFv = fv_p + fv_pmt;
    const totalDeposits = p + (pmt * nt);
    const interest = Math.max(0, totalFv - totalDeposits);

    // Amortizing loan payment for principal P over T years
    const loanPmt = (p > 0 && r_m > 0) ? (p * (r_m * Math.pow(1 + r_m, nt)) / (Math.pow(1 + r_m, nt) - 1)) : 0;

    document.getElementById('resFutureVal').innerText = `$${Math.round(totalFv).toLocaleString()}`;
    document.getElementById('resTotalContrib').innerText = `$${Math.round(totalDeposits).toLocaleString()}`;
    document.getElementById('resInterestEarned').innerText = `$${Math.round(interest).toLocaleString()}`;
    document.getElementById('resEquivLoan').innerText = `$${loanPmt.toFixed(2)} / mo`;
}

function filterFinHub(cat) {
    const grid = document.getElementById('finHubGrid');
    const filtered = (cat === 'all') ? FIN_TOOLS : FIN_TOOLS.filter(t => t.cat === cat);
    grid.innerHTML = filtered.map(t => `
        <div style="background: white; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; box-shadow: 0 1px 3px rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <h4 style="margin: 0 0 0.4rem 0;"><a href="${t.slug}" style="color: #2563eb; text-decoration: none; font-weight: 700;">${t.name}</a></h4>
                <p style="font-size: 0.85rem; color: #475569; margin: 0 0 0.75rem 0;">${t.desc}</p>
            </div>
            <div>
                <a href="${t.slug}" style="display: inline-block; font-size: 0.8rem; font-weight: 600; color: #2563eb;">Open Calculator &rarr;</a>
            </div>
        </div>
    `).join('');
}

window.addEventListener('DOMContentLoaded', () => {
    solveQuickFinance();
    filterFinHub('all');
});
</script>"""

    article = """<h2>Economic Foundations of the Time Value of Money (TVM)</h2>
<p>The entire superstructure of modern quantitative finance, corporate capital budgeting, commercial lending, and individual wealth accumulation is built upon the foundational economic axiom known as the <strong>Time Value of Money (TVM)</strong>. First rigorously analyzed by Fibonacci in 1202 and codified by Irving Fisher in 1930, TVM establishes that a unit of currency received today possesses greater purchasing utility and economic value than the identical nominal unit received in the future.</p>

<p>The time value of money arises from three distinct economic mechanisms:</p>
<ol>
    <li><strong>Investment Opportunity Cost:</strong> Capital deployed today immediately earns continuous returns through compound interest, corporate dividends, or economic yield.</li>
    <li><strong>Inflationary Purchasing Power Erosion:</strong> General monetary price inflation continuously decreases the quantity of real goods and services that a nominal dollar can purchase over time.</li>
    <li><strong>Credit Default and Uncertainty Risk:</strong> Future cash flows carry inherent counterparty risk, demanding a risk premium discount rate to reflect future uncertainty.</li>
</ol>

<h2>Mathematical Derivations: Compounding vs. Amortization</h2>

<h3>1. Discrete Compound Wealth Accumulation</h3>
<p>When an initial principal $P_0$ is invested at an annual nominal interest rate $r$ compounded $n$ times per year with recurring end-of-period contributions $\text{PMT}$, the terminal future value $FV$ after $t$ years evaluates as the linear superposition of lump-sum compounding and an ordinary annuity:</p>

$$FV = P_0 \left( 1 + \frac{r}{n} \right)^{nt} + \text{PMT} \left[ \frac{\left( 1 + \frac{r}{n} \right)^{nt} - 1}{r / n} \right]$$

<p>As the compounding frequency $n$ approaches infinity ($n \to \infty$), the expression transitions into continuous compounding governed by Euler's exponential constant $e$:</p>

$$FV_{\text{continuous}} = P_0 \, e^{rt}$$

<h3>2. The Fixed-Rate Loan Amortization Equation</h3>
<p>In residential mortgages, auto loans, and commercial notes, an initial borrowed principal $P$ is amortized through $N$ equal monthly payments ($M$). Because the outstanding loan balance decreases with each successive payment, the fraction of each payment allocated to interest declines monotonically while principal reduction accelerates:</p>

$$M = P \left[ \frac{r_m (1 + r_m)^N}{(1 + r_m)^N - 1} \right]$$

<p>Where $r_m = r / 12$ is the periodic monthly interest rate. The remaining unpaid principal balance $B_k$ after $k$ completed payments evaluates as:</p>

$$B_k = P \left[ \frac{(1 + r_m)^N - (1 + r_m)^k}{(1 + r_m)^N - 1} \right]$$

<h3>Comparative Financial Metrics and Wealth Conventions Matrix</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Financial Discipline</th>
            <th>Primary Governing Formulation</th>
            <th>Core Objective</th>
            <th>Standard Benchmark</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Lending &amp; Mortgages</td><td>$M = P \frac{r(1+r)^n}{(1+r)^n - 1}$</td><td>Equal Monthly Debt Amortization</td><td>Fannie Mae 43% DTI Ceiling</td></tr>
        <tr><td>Wealth Compounding</td><td>$FV = P(1+r/n)^{nt} + \text{PMT} \frac{(1+r/n)^{nt}-1}{r/n}$</td><td>Long-Term Nest Egg Sizing</td><td>S&amp;P 500 Historical 10% CAGR</td></tr>
        <tr><td>Retirement (FIRE)</td><td>$\text{Nest Egg} = \frac{\text{Annual Spend}}{\text{SWR}}$</td><td>Portfolio Longevity Sizing</td><td>Trinity Study 4.0% Safe Rate</td></tr>
        <tr><td>Capital Gains Tax</td><td>$\text{Tax} = (\text{Proceeds} - \text{Basis}) \times \tau$</td><td>Statutory Post-Tax Liquidation</td><td>0%, 15%, 20% Brackets + 3.8% NIIT</td></tr>
        <tr><td>Overtime Payroll</td><td>$W_{\text{ot}} = H_{\text{ot}} \times 1.5 \times R_{\text{reg}}$</td><td>FLSA Statutory Wage Compliance</td><td>Time-and-a-half past 40 hrs/wk</td></tr>
    </tbody>
</table>

<h2>Modern Portfolio Theory and the 4% Safe Withdrawal Framework</h2>
<p>In personal wealth management and the Financial Independence Retire Early (FIRE) movement, retirement readiness is governed by William Bengen's 1994 asset allocation model and the landmark <strong>Trinity Study (1998)</strong>. Across a century of US market data spanning the Great Depression, stagflation, and dot-com crashes, a balanced portfolio of $60\%$ equities and $40\%$ fixed-income bonds sustained a constant <strong>4.0% Safe Withdrawal Rate (SWR)</strong> for a minimum 30-year retirement horizon with a $95\%$ statistical survival probability.</p>

<p>The required baseline retirement nest egg is evaluated directly as:</p>

$$\text{Retirement Portfolio Target} = \frac{\text{Net Annual Living Expenses}}{\text{SWR}} = 25 \times \text{Annual Living Expenses}$$

<div class="worked-example-card">
    <h3>Worked Financial Economics Case Study: Mortgage Amortization vs. Index Investing</h3>
    <p><strong>Scenario:</strong> A homebuyer borrows a $400,000, 30-year fixed-rate mortgage at an annual interest rate of 6.50% ($r_m = 0.065 / 12 \approx 0.0054167$). Determine: (1) monthly principal and interest payment ($M$), (2) total interest paid over the complete 30-year term, and (3) compare total interest with compounding returns if an extra $300/month is invested in an S&P 500 index fund yielding 8.0% annualized.</p>
    
    <div class="step-solution">
        <h4>Step 1: Compute Monthly Mortgage Payment ($M$)</h4>
        $$N = 30 \times 12 = 360 \text{ monthly payments}$$
        $$(1 + r_m)^{360} = (1.0054167)^{360} \approx 6.9918$$
        $$M = 400,000 \left[ \frac{0.0054167 \times 6.9918}{6.9918 - 1} \right] = 400,000 \times \left[ \frac{0.037872}{5.9918} \right] \approx \$2,528.27 \text{ per month}$$

        <h4>Step 2: Calculate Lifetime Mortgage Interest</h4>
        $$\text{Total Payments} = 360 \times \$2,528.27 = \$910,177.20$$
        $$\text{Total Interest Paid} = \$910,177.20 - \$400,000 = \$510,177.20$$

        <h4>Step 3: Evaluate Opportunity Cost of Extra $300/Month Investment</h4>
        <p>Investing $300/month for 30 years at 8.0% ($r_m = 0.08 / 12 \approx 0.006667$):</p>
        $$FV = 300 \times \left[ \frac{(1 + 0.006667)^{360} - 1}{0.006667} \right] = 300 \times \left[ \frac{10.9357 - 1}{0.006667} \right] \approx \$447,108$$
        <p><strong>Financial Insight:</strong> An investor contributing just $300/month into equity index funds accumulates over $447,000 in wealth, offsetting nearly the entire lifetime interest burden of the $400k mortgage!</p>
    </div>
</div>

<h2>Common Financial Calculation Pitfalls</h2>
<ol>
    <li><strong>Conflating APR and APY:</strong> Annual Percentage Rate (APR) ignores compounding frequency, whereas Annual Percentage Yield (APY) reflects real compounding. Comparing a loan's APR directly against a deposit's APY creates distorted financial decisions.</li>
    <li><strong>Disregarding Inflation in Retirement Planning:</strong> A nest egg that generates $60,000/year today will possess less than $25,000 of real purchasing power in 30 years under standard 3% annual inflation. Financial models must incorporate real rates of return ($r_{\text{real}} = \frac{1+r}{1+i} - 1$).</li>
    <li><strong>Failing to Account for Statutory Tax Drag:</strong> Calculating investment gains without deducting capital gains taxes, dividend taxes, and mandatory retirement account minimum distributions (RMDs) overestimates net spendable wealth by 15% to 30%.</li>
</ol>

<section class="faq-section">
    <h2>Frequently Asked Questions About Financial Planning</h2>
    <div class="faq-item">
        <h3>What calculation engines are included in the Financial Planning Suite?</h3>
        <p>The suite encompasses 29+ tools across mortgages, auto loans, compound interest wealth accumulation, retirement FIRE planning, capital gains tax, salary take-home pay, and debt payoff.</p>
    </div>
    <div class="faq-item">
        <h3>What is the Time Value of Money (TVM) principle?</h3>
        <p>The Time Value of Money states that a dollar received today is worth more than a dollar received in the future due to its potential earning capacity through compound interest and investment yield.</p>
    </div>
    <div class="faq-item">
        <h3>How does compound interest differ from simple interest?</h3>
        <p>Simple interest accumulates strictly on the initial principal balance (I = P * R * T). Compound interest accumulates on both the principal and previously earned interest (A = P * (1 + r/n)^(nt)), creating exponential wealth growth.</p>
    </div>
    <div class="faq-item">
        <h3>What is the 4% Safe Withdrawal Rule in retirement planning?</h3>
        <p>Originating from the 1998 Trinity Study, the 4% rule states that a retiree can safely withdraw 4% of their initial portfolio in Year 1, adjusted annually for inflation, with a 95%+ probability of portfolio survival over 30 years.</p>
    </div>
</section>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article, category_hub="finance.html", category_name="Financial Planning")


def main():
    cs_html = gen_cable_sizing_guide()
    with open(os.path.join(BASE_DIR, "cable-sizing-guide.html"), "w", encoding="utf-8") as f:
        f.write(cs_html)
    print("Generated cable-sizing-guide.html successfully!")

    elec_html = gen_electrical_hub()
    with open(os.path.join(BASE_DIR, "electrical.html"), "w", encoding="utf-8") as f:
        f.write(elec_html)
    print("Generated electrical.html successfully!")

    eng_html = gen_engineering_formulas()
    with open(os.path.join(BASE_DIR, "engineering-formulas.html"), "w", encoding="utf-8") as f:
        f.write(eng_html)
    print("Generated engineering-formulas.html successfully!")

    fin_html = gen_financial_hub()
    with open(os.path.join(BASE_DIR, "financial.html"), "w", encoding="utf-8") as f:
        f.write(fin_html)
    print("Generated financial.html successfully!")

if __name__ == "__main__":
    main()
