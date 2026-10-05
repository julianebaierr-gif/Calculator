# -*- coding: utf-8 -*-
"""
Generator for Batch 36 - Part 3
Tools:
5. lightning-protection-calculator.html
6. lumen-lux-calculator.html
"""

import os

HEADER_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="https://calchub.com/{slug}.html">
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
                <a href="math.html">Math &amp; Stats</a>
                <a href="converter.html">Converters</a>
                <a href="engineering.html">Engineering</a>
                <a href="finance.html">Finance</a>
            </nav>
        </div>
    </header>
    <div class="container">
        <div class="main-wrapper">
            <main class="content-area">
                <nav class="breadcrumb">
                    <a href="index.html">Home</a> &gt; <a href="engineering.html">Engineering</a> &gt; <span>{h1}</span>
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
                    <h3>Related Engineering Tools</h3>
                    <ul class="sidebar-links">
                        <li><a href="lightning-protection-calculator.html">Lightning Protection (NFPA 780)</a></li>
                        <li><a href="lumen-lux-calculator.html">Lumen to Lux Illuminance</a></li>
                        <li><a href="earth-pit-resistance-calculator.html">Earth Pit Resistance</a></li>
                        <li><a href="earthing-cable-size-calculator.html">Earthing Cable Sizing</a></li>
                        <li><a href="voltage-drop-calculator.html">Voltage Drop Calculator</a></li>
                        <li><a href="illuminance-converter.html">Illuminance Converter</a></li>
                        <li><a href="wire-ampacity-calculator.html">Wire Ampacity Sizing</a></li>
                        <li><a href="fault-current-calculator.html">Fault Current Sizing</a></li>
                        <li><a href="solar-panel-sizing-calculator.html">Solar Panel Sizing</a></li>
                        <li><a href="decibel-calculator.html">Decibel Calculator</a></li>
                    </ul>
                </div>
            </aside>
        </div>
    </div>
    <footer class="site-footer">
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>About CalcHub</h4>
                    <p>CalcHub provides free, engineering-grade calculators, physics simulation utilities, and facility safety models verified against NFPA 780, IEC 62305, and IESNA lighting codes.</p>
                </div>
                <div class="footer-col">
                    <h4>Calculator Hubs</h4>
                    <ul class="footer-links">
                        <li><a href="index.html">All Calculators</a></li>
                        <li><a href="math.html">Mathematics &amp; Statistics</a></li>
                        <li><a href="converter.html">Unit Converters</a></li>
                        <li><a href="engineering.html">Electrical &amp; Engineering</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Facility Safety &amp; Optics</h4>
                    <ul class="footer-links">
                        <li><a href="lightning-protection-calculator.html">Rolling Sphere Lightning</a></li>
                        <li><a href="lumen-lux-calculator.html">Lumen Lux Photometry</a></li>
                        <li><a href="earth-pit-resistance-calculator.html">Grounding Electrode Grid</a></li>
                        <li><a href="illuminance-converter.html">Lux to Foot-Candles</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 CalcHub. All rights reserved. Computational tools for electrical engineers, facility designers, and architects.</p>
            </div>
        </div>
    </footer>
    <script>
    {calc_js}
    </script>
</body>
</html>
"""

# ==============================================================================
# TOOL 5: lightning-protection-calculator.html
# ==============================================================================
TOOL5_SLUG = "lightning-protection-calculator"
TOOL5_TITLE = "Lightning Protection Calculator - Rolling Sphere Method (NFPA 780 & IEC 62305)"
TOOL5_DESC = "Calculate lightning protection zone radius, rolling sphere penetration, equivalent collection area (Ad), and annual strike frequency (Nd) per NFPA 780 and IEC 62305."
TOOL5_H1 = "Lightning Protection Rolling Sphere Calculator"
TOOL5_SHORT = "Determine air terminal protection radius, rolling sphere penetration depth, equivalent collection area, and annual flash risk per NFPA 780 and IEC 62305."

TOOL5_SCHEMA = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Lightning Protection Calculator",
      "url": "https://calchub.com/lightning-protection-calculator.html",
      "description": "Calculates lightning protection zone of protection, rolling sphere method parameters, collection area, and strike risk per NFPA 780 and IEC 62305.",
      "applicationCategory": "EngineeringApplication",
      "operatingSystem": "All",
      "offers": {
        "@type": "Offer",
        "price": "0.00",
        "priceCurrency": "USD"
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the Rolling Sphere Method (RSM) in lightning protection?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The Rolling Sphere Method is an electro-geometric modeling standard (NFPA 780, IEC 62305, IEEE 998) that visualizes an imaginary sphere rolled over a structure. All points touched by the sphere are susceptible to direct lightning strikes. Any surface beneath the sphere suspended between air terminals or above ground is inside the protected zone."
          }
        },
        {
          "@type": "Question",
          "name": "What are the rolling sphere radii for different Lightning Protection Levels (LPL)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "IEC 62305 and NFPA 780 define four levels: LPL I uses R = 20 m (99% interception efficiency, protects critical chemical/explosive plants); LPL II uses R = 30 m (97% efficiency); LPL III uses R = 45 m (91% efficiency, standard commercial structures); LPL IV uses R = 60 m (84% efficiency)."
          }
        },
        {
          "@type": "Question",
          "name": "How is the protection radius of a single vertical air terminal calculated?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "For a vertical rod of height h where h <= R, the horizontal protection radius rx at the reference ground plane is calculated as rx = sqrt(h * (2R - h)), where R is the rolling sphere radius."
          }
        },
        {
          "@type": "Question",
          "name": "How is the expected annual strike frequency (Nd) determined?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Annual strike frequency is calculated as Nd = Ng * Ad * Cd * 10^-6, where Ng is annual ground flash density (flashes/km2/yr), Ad is structure equivalent collection area (m2), and Cd is environmental location factor."
          }
        }
      ]
    }
  ]
}"""

TOOL5_UI = """
<div class="calc-grid">
    <div class="calc-input-group">
        <label for="lp-level">Lightning Protection Level (LPL / Class):</label>
        <select id="lp-level">
            <option value="20">Level I: $R = 20\\text{ m}$ (Critical Infrastructure / Explosives, 99%)</option>
            <option value="30">Level II: $R = 30\\text{ m}$ (High Risk Commercial / Hospitals, 97%)</option>
            <option value="45" selected>Level III: $R = 45\\text{ m}$ (Standard Commercial &amp; Residential, 91%)</option>
            <option value="60">Level IV: $R = 60\\text{ m}$ (Open Farm / Non-Hazardous Storage, 84%)</option>
        </select>
    </div>
    <div class="calc-input-group">
        <label for="lp-rod-h">Air Terminal Tip Height ($h$ above roof/ground):</label>
        <div class="input-with-select">
            <input type="number" id="lp-rod-h" value="3.0" min="0.3" step="any">
            <select id="lp-rod-h-unit">
                <option value="1" selected>Meters (m)</option>
                <option value="0.3048">Feet (ft)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="lp-bldg-l">Structure Length ($L$):</label>
        <div class="input-with-select">
            <input type="number" id="lp-bldg-l" value="40" min="1" step="any">
            <select id="lp-bldg-l-unit">
                <option value="1" selected>Meters (m)</option>
                <option value="0.3048">Feet (ft)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="lp-bldg-w">Structure Width ($W$):</label>
        <div class="input-with-select">
            <input type="number" id="lp-bldg-w" value="25" min="1" step="any">
            <select id="lp-bldg-w-unit">
                <option value="1" selected>Meters (m)</option>
                <option value="0.3048">Feet (ft)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="lp-bldg-h">Structure Roof Height ($H$):</label>
        <div class="input-with-select">
            <input type="number" id="lp-bldg-h" value="15" min="1" step="any">
            <select id="lp-bldg-h-unit">
                <option value="1" selected>Meters (m)</option>
                <option value="0.3048">Feet (ft)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="lp-keraunic">Thunderstorm Days per Year ($T_d$ or isokeraunic):</label>
        <div class="input-with-select">
            <input type="number" id="lp-keraunic" value="30" min="1" max="250" step="any">
            <select id="lp-keraunic-unit">
                <option value="1" selected>Days/year</option>
            </select>
        </div>
    </div>
</div>
<button id="calc-lp-btn" class="calc-btn">Calculate Rolling Sphere Protection</button>
<div class="calc-results-card" id="lp-results">
    <h3>Rolling Sphere Protection &amp; Risk Metrics</h3>
    <div class="result-row highlight-result">
        <span class="result-label">Air Terminal Ground Protection Radius ($r_x$):</span>
        <span class="result-val" id="res-lp-rx">16.16 m (53.0 ft)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Rolling Sphere Radius ($R$):</span>
        <span class="result-val" id="res-lp-r">45.0 m (147.6 ft)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Structure Equivalent Collection Area ($A_d$):</span>
        <span class="result-val" id="res-lp-ad">3,656.9 m&sup2; (0.00366 km&sup2;)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Ground Flash Density ($N_g$):</span>
        <span class="result-val" id="res-lp-ng">2.82 flashes/km&sup2;/year</span>
    </div>
    <div class="result-row">
        <span class="result-label">Estimated Annual Direct Strikes ($N_d$):</span>
        <span class="result-val" id="res-lp-nd">0.0103 strikes/yr (1 strike every 97 years)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Minimum Down-Conductor Requirement:</span>
        <span class="result-val" id="res-lp-downcond">&ge; 2 Down-Conductors (Spacing &le; 15 m)</span>
    </div>
</div>
"""

TOOL5_JS = """
function computeLightning() {
    var R = parseFloat(document.getElementById('lp-level').value);
    var hVal = parseFloat(document.getElementById('lp-rod-h').value);
    var hUnit = parseFloat(document.getElementById('lp-rod-h-unit').value);
    var lVal = parseFloat(document.getElementById('lp-bldg-l').value);
    var lUnit = parseFloat(document.getElementById('lp-bldg-l-unit').value);
    var wVal = parseFloat(document.getElementById('lp-bldg-w').value);
    var wUnit = parseFloat(document.getElementById('lp-bldg-w-unit').value);
    var bldgHVal = parseFloat(document.getElementById('lp-bldg-h').value);
    var bldgHUnit = parseFloat(document.getElementById('lp-bldg-h-unit').value);
    var Td = parseFloat(document.getElementById('lp-keraunic').value);

    if (isNaN(hVal) || hVal <= 0 || isNaN(lVal) || lVal <= 0 || isNaN(wVal) || wVal <= 0 || isNaN(bldgHVal) || bldgHVal <= 0 || isNaN(Td) || Td <= 0) return;

    var h = hVal * hUnit; // meters
    var L = lVal * lUnit; // meters
    var W = wVal * wUnit; // meters
    var H = bldgHVal * bldgHUnit; // meters

    // Protection radius rx = sqrt(h * (2R - h)) if h <= R, else R
    var rx = 0;
    if (h <= R) {
        rx = Math.sqrt(h * ((2.0 * R) - h));
    } else {
        rx = R;
    }
    var rx_ft = rx * 3.28084;
    var R_ft = R * 3.28084;

    // Equivalent collection area Ad per IEC 62305-2:
    // For an isolated rectangular structure: Ad = L*W + 2*L*H + 2*W*H + pi*H^2
    var Ad = (L * W) + (2.0 * L * H) + (2.0 * W * H) + (Math.PI * Math.pow(H, 2)); // m^2
    var Ad_km2 = Ad * 1e-6;

    // Ground Flash Density Ng per IEC 62305: Ng = 0.04 * (Td)^1.25 flashes/km^2/year
    var Ng = 0.04 * Math.pow(Td, 1.25);

    // Expected annual lightning flash frequency Nd = Ng * Ad * Cd * 1e-6 (assume Cd = 1.0 isolated)
    var Nd = Ng * Ad * 1e-6;
    var returnPeriod = (Nd > 0) ? (1.0 / Nd) : 999999;

    document.getElementById('res-lp-rx').textContent = rx.toFixed(2) + " m (" + rx_ft.toFixed(1) + " ft)";
    document.getElementById('res-lp-r').textContent = R.toFixed(1) + " m (" + R_ft.toFixed(1) + " ft)";
    document.getElementById('res-lp-ad').textContent = Ad.toFixed(1) + " m\u00B2 (" + Ad_km2.toFixed(5) + " km\u00B2)";
    document.getElementById('res-lp-ng').textContent = Ng.toFixed(2) + " flashes/km\u00B2/year";

    var ndStr = Nd.toFixed(4) + " strikes/yr (1 strike every " + Math.round(returnPeriod) + " years)";
    document.getElementById('res-lp-nd').textContent = ndStr;

    // Down conductor spacing per IEC 62305:
    // LPL I: 10m, LPL II: 10m, LPL III: 15m, LPL IV: 20m
    var spacing = (R === 20 || R === 30) ? 10 : ((R === 45) ? 15 : 20);
    var perimeter = 2.0 * (L + W);
    var reqDown = Math.max(2, Math.ceil(perimeter / spacing));
    document.getElementById('res-lp-downcond').textContent = "\u2265 " + reqDown + " Down-Conductors (Perimeter " + perimeter.toFixed(0) + "m, Max Spacing " + spacing + "m)";
}

document.getElementById('calc-lp-btn').addEventListener('click', computeLightning);
['lp-level', 'lp-rod-h', 'lp-rod-h-unit', 'lp-bldg-l', 'lp-bldg-l-unit', 'lp-bldg-w', 'lp-bldg-w-unit', 'lp-bldg-h', 'lp-bldg-h-unit', 'lp-keraunic'].forEach(function(id) {
    document.getElementById(id).addEventListener('input', computeLightning);
    document.getElementById(id).addEventListener('change', computeLightning);
});
window.addEventListener('DOMContentLoaded', computeLightning);
"""

TOOL5_ARTICLE = r"""
<h2>Electrophysics of Atmospheric Discharges and Leader Attachment</h2>
<p>Cloud-to-ground lightning is a transient, high-current atmospheric electric discharge initiated when electrostatic charge separation within cumulonimbus clouds establishes breakdown electric fields exceeding $3\text{ MV/m}$ in moist air. A stepped leader descends in discrete nanosecond steps of tens of meters, creating an ionized plasma channel carrying thousands of Coulombs of charge. As the stepped leader approaches within $50\text{--}100\text{ meters}$ of the Earth's surface, the intense ground-level electric field gradient launches upward connecting leaders from sharp, elevated ground structures (building corners, parapets, radio towers, air terminals).</p>

<p>The instant an upward connecting leader establishes electrical contact with the downward stepped leader, the final striking distance is bridged. A return stroke surges upward at roughly one-third the speed of light, discharging peak currents ranging from $10\text{ kA}$ to over $200\text{ kA}$ with di/dt wavefront gradients exceeding $100\text{ kA/}\mu\text{s}$, producing severe mechanical blast shockwaves, extreme ohmic Joule heating, and lethal side-flash potential differences.</p>

<h2>The Rolling Sphere Method (RSM) Electro-Geometric Model</h2>
<p>Modern lightning protection design (governed globally by <strong>NFPA 780</strong> in North America, <strong>IEC 62305</strong> internationally, and <strong>IEEE 998</strong> for electrical substations) is grounded in the <strong>Electro-Geometric Model (EGM)</strong>. The fundamental physical premise of EGM is that the striking distance ($r_s$) across which the downward leader attaches to a ground object is a function of the prospective peak return stroke current ($I$):</p>
$$r_s = A \cdot I^b$$

<p>Per IEC and Whitehead formulations, $r_s \approx 10 \cdot I^{0.65}$ (where $r_s$ is in meters and $I$ in kA). In the <strong>Rolling Sphere Method</strong>, an imaginary sphere of standardized radius $R = r_s$ is rolled across the terrain, over all buildings, towers, and parapets. Any physical point on the building or roof that touches the sphere's surface is exposed to direct lightning strikes. Conversely, all spatial volume enclosed underneath the sphere without touching its boundary resides within the <strong>Zone of Protection (LPZ 0B)</strong>.</p>

<h3>Lightning Protection Levels (LPL) and Rolling Sphere Radii</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Protection Level (LPL)</th>
            <th>Sphere Radius ($R$)</th>
            <th>Minimum Current ($I_{\text{min}}$)</th>
            <th>Interception Efficiency</th>
            <th>Typical Protected Structure</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>LPL I (Class I)</strong></td>
            <td>$20\text{ meters}$ ($65\text{ ft}$)</td>
            <td>$3\text{ kA}$</td>
            <td>$99\%$</td>
            <td>Chemical refineries, ammunition depots, nuclear plants</td>
        </tr>
        <tr>
            <td><strong>LPL II (Class II)</strong></td>
            <td>$30\text{ meters}$ ($100\text{ ft}$)</td>
            <td>$5\text{ kA}$</td>
            <td>$97\%$</td>
            <td>Hospitals, data centers, telecom central offices</td>
        </tr>
        <tr>
            <td><strong>LPL III (Class III)</strong></td>
            <td>$45\text{ meters}$ ($150\text{ ft}$)</td>
            <td>$10\text{ kA}$</td>
            <td>$91\%$</td>
            <td>Commercial offices, multi-family residences, retail</td>
        </tr>
        <tr>
            <td><strong>LPL IV (Class IV)</strong></td>
            <td>$60\text{ meters}$ ($200\text{ ft}$)</td>
            <td>$16\text{ kA}$</td>
            <td>$84\%$</td>
            <td>Agricultural warehouses, non-combustible open storage</td>
        </tr>
    </tbody>
</table>

<h2>Mathematical Formulations for Protection Radius ($r_x$) and Sag Depth ($p$)</h2>
<p>For an isolated vertical air terminal rod of height $h$ positioned on a flat horizontal plane (where $h \le R$), the horizontal circular protection radius $r_x$ at the reference plane is derived using the Pythagorean theorem on the right triangle formed by the sphere center:</p>
$$(R - h)^2 + r_x^2 = R^2$$
$$r_x^2 = R^2 - (R - h)^2 = R^2 - (R^2 - 2Rh + h^2) = 2Rh - h^2$$
$$r_x = \sqrt{h (2R - h)} \quad [\text{Meters}]$$

<p>When two air terminals of equal height $h$ are separated by horizontal distance $D$, the rolling sphere rolls between them and sags downward. The maximum penetration dip depth $p$ below the terminal tip level is:</p>
$$p = R - \sqrt{R^2 - \left( \frac{D}{2} \right)^2}$$

<p>To ensure intermediate roof equipment is not struck, the height of the protected equipment must not exceed $h_{\text{equip}} \le h - p$. If $D > 2R$, the sphere touches the roof surface between the terminals, creating an unprotected strike zone.</p>

<h2>Risk Assessment: Collection Area ($A_d$) and Annual Flash Expectancy ($N_d$)</h2>
<p>To assess whether a building requires an engineered lightning protection system, IEC 62305-2 defines the <strong>Equivalent Collection Area ($A_d$)</strong> of an isolated rectangular building of length $L$, width $W$, and roof height $H$ as:</p>
$$A_d = L \cdot W + 2 \cdot L \cdot H + 2 \cdot W \cdot H + \pi \cdot H^2 \quad [\text{m}^2]$$

<p>The annual ground flash density $N_g$ (lightning flashes per square kilometer per year) is calculated from local keraunic thunderstorm days $T_d$:</p>
$$N_g = 0.04 \cdot T_d^{1.25} \quad \left[ \frac{\text{flashes}}{\text{km}^2\cdot\text{year}} \right]$$

<p>The expected annual direct strike frequency $N_d$ to the structure is:</p>
$$N_d = N_g \cdot A_d \cdot C_d \times 10^{-6} \quad [\text{Strikes / Year}]$$

<p>Where $C_d$ is the environmental location factor ($C_d = 1.0$ for isolated flat terrain; $C_d = 2.0$ on a hilltop; $C_d = 0.5$ in dense urban centers surrounded by taller structures).</p>

<div class="worked-example-card">
    <h4>Step-by-Step Engineering Case Study: Commercial Data Center Facility</h4>
    <p><strong>Scenario:</strong> A tier-3 data center building measures $L = 60\ \text{m}$, $W = 35\ \text{m}$, and $H = 12\ \text{m}$. Due to financial mission-criticality, Level II protection ($R = 30\ \text{m}$) is specified. Parapet air terminals have a height of $h = 1.5\ \text{m}$ above the roof surface. The region experiences $T_d = 40$ thunderstorm days per year.</p>
    <div class="step-solution">
        <p><strong>Step 1: Calculate Air Terminal Protection Radius ($r_x$):</strong></p>
        $$r_x = \sqrt{h (2R - h)} = \sqrt{1.5 \times ((2 \times 30) - 1.5)} = \sqrt{1.5 \times 58.5} = \sqrt{87.75} = 9.367\ \text{meters}$$
        <p>Each terminal covers a horizontal radius of $9.37\ \text{m}$ ($30.7\ \text{ft}$) on the roof deck.</p>
        <p><strong>Step 2: Calculate Equivalent Collection Area ($A_d$):</strong></p>
        $$A_d = (60 \times 35) + 2(60 \times 12) + 2(35 \times 12) + \pi(12)^2$$
        $$A_d = 2100 + 1440 + 840 + 452.39 = 4,832.39\ \text{m}^2 \approx 0.00483\ \text{km}^2$$
        <p><strong>Step 3: Determine Ground Flash Density ($N_g$):</strong></p>
        $$N_g = 0.04 \times (40)^{1.25} = 0.04 \times 100.995 = 4.04\ \text{flashes/km}^2/\text{year}$$
        <p><strong>Step 4: Compute Annual Direct Strike Expectancy ($N_d$):</strong></p>
        $$N_d = 4.04 \times 4,832.39 \times 1.0 \times 10^{-6} = 0.01952\ \text{strikes/year}$$
        <p>The statistical return period between direct lightning strikes is $T_{\text{return}} = \frac{1}{0.01952} \approx 51.2\ \text{years}$.</p>
        <p><strong>Step 5: Determine Minimum Down-Conductor Network:</strong></p>
        <p>Total building perimeter $P = 2(60 + 35) = 190\ \text{m}$. For LPL II, maximum down-conductor spacing is $10\ \text{m}$:</p>
        $$N_{\text{down}} = \left\lceil \frac{190}{10} \right\rceil = 19\ \text{down-conductors}$$
        <p><strong>Conclusion:</strong> A complete LPZ 0B Faraday mesh with 19 perimeter down-conductors connected to an interconnected grounding ring electrode ($R_{\text{ground}} \le 10\ \Omega$) must be installed.</p>
    </div>
</div>

<h2>Frequently Asked Questions (FAQ)</h2>
<div class="faq-section">
    <h3>What is the Rolling Sphere Method (RSM) in lightning protection?</h3>
    <p>The Rolling Sphere Method is an electro-geometric modeling standard (NFPA 780, IEC 62305, IEEE 998) that visualizes an imaginary sphere rolled over a structure. All points touched by the sphere are susceptible to direct lightning strikes. Any surface beneath the sphere suspended between air terminals or above ground is inside the protected zone.</p>

    <h3>What are the rolling sphere radii for different Lightning Protection Levels (LPL)?</h3>
    <p>IEC 62305 and NFPA 780 define four levels: LPL I uses $R = 20\text{ m}$ ($99\%$ interception efficiency, protects critical chemical/explosive plants); LPL II uses $R = 30\text{ m}$ ($97\%$ efficiency); LPL III uses $R = 45\text{ m}$ ($91\%$ efficiency, standard commercial structures); LPL IV uses $R = 60\text{ m}$ ($84\%$ efficiency).</p>

    <h3>How is the protection radius of a single vertical air terminal calculated?</h3>
    <p>For a vertical rod of height $h$ where $h \le R$, the horizontal protection radius $r_x$ at the reference ground plane is calculated as $r_x = \sqrt{h (2R - h)}$, where $R$ is the rolling sphere radius.</p>

    <h3>How is the expected annual strike frequency ($N_d$) determined?</h3>
    <p>Annual strike frequency is calculated as $N_d = N_g \cdot A_d \cdot C_d \times 10^{-6}$, where $N_g$ is annual ground flash density (flashes/$\text{km}^2$/yr), $A_d$ is structure equivalent collection area ($\text{m}^2$), and $C_d$ is the environmental location factor.</p>
</div>
"""

# ==============================================================================
# TOOL 6: lumen-lux-calculator.html
# ==============================================================================
TOOL6_SLUG = "lumen-lux-calculator"
TOOL6_TITLE = "Lumen to Lux Calculator - Illuminance, Beam Angle & Candela"
TOOL6_DESC = "Convert Lumens to Lux and Foot-Candles based on beam angle and distance. Calculate center beam candlepower (CBCP), lighted spot area, and IESNA lighting levels."
TOOL6_H1 = "Lumen to Lux Illuminance Calculator"
TOOL6_SHORT = "Convert luminous flux (Lumens) to illuminance (Lux &amp; Foot-Candles) across distance, beam spread angle, luminous intensity (Candela), and coverage area."

TOOL6_SCHEMA = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Lumen to Lux Calculator",
      "url": "https://calchub.com/lumen-lux-calculator.html",
      "description": "Calculates illuminance in Lux and Foot-Candles from Lumens, beam angle, distance, and luminous intensity in Candelas.",
      "applicationCategory": "EngineeringApplication",
      "operatingSystem": "All",
      "offers": {
        "@type": "Offer",
        "price": "0.00",
        "priceCurrency": "USD"
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the difference between Lumens, Lux, and Candelas?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Lumens (lm) measure total luminous flux emitted by a light source in all directions. Candela (cd) measures luminous intensity emitted into a specific solid angle (1 cd = 1 lumen per steradian). Lux (lx) measures illuminance, which is the density of luminous flux incident on a surface (1 lux = 1 lumen per square meter). Foot-Candle (fc) is the imperial equivalent (1 fc = 1 lm/ft2 = 10.764 lux)."
          }
        },
        {
          "@type": "Question",
          "name": "How does the Inverse-Square Law affect illuminance?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Illuminance drops inversely with the square of throw distance: E = I / d^2. Doubling the distance between a light source and a task surface reduces illuminance to one-fourth (25%) of its original level."
          }
        },
        {
          "@type": "Question",
          "name": "How do you calculate peak center beam candela from lumens and beam angle?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "For a conical beam of angle theta, the solid angle is Omega = 2 * pi * (1 - cos(theta / 2)). The average luminous intensity is I = Lumens / Omega. In real optical reflectors, the peak center beam candela (CBCP) typically equals approximately CBCP = Lumens / Omega."
          }
        },
        {
          "@type": "Question",
          "name": "What are recommended IESNA / OSHA illuminance levels?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Hallways and corridors: 100 lux (10 fc); General office work and computer labs: 300 to 500 lux (30 to 50 fc); Detailed drafting, PCB soldering, and precision inspection: 1,000 to 2,000 lux (100 to 200 fc); Surgical suites: 10,000 to 50,000 lux."
          }
        }
      ]
    }
  ]
}"""

TOOL6_UI = """
<div class="calc-grid">
    <div class="calc-input-group">
        <label for="lx-lumens">Luminous Flux ($\Phi$ in Lumens):</label>
        <div class="input-with-select">
            <input type="number" id="lx-lumens" value="1200" min="1" step="any">
            <select id="lx-lumens-unit">
                <option value="1" selected>Lumens (lm)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="lx-angle">Optical Beam Angle ($\theta$):</label>
        <div class="input-with-select">
            <input type="number" id="lx-angle" value="38" min="1" max="180" step="any">
            <select id="lx-angle-unit">
                <option value="1" selected>Degrees (&deg;)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="lx-dist">Throw Distance to Task Surface ($d$):</label>
        <div class="input-with-select">
            <input type="number" id="lx-dist" value="2.5" min="0.1" step="any">
            <select id="lx-dist-unit">
                <option value="1" selected>Meters (m)</option>
                <option value="0.3048">Feet (ft)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="lx-preset">Common Fixture Beam Presets:</label>
        <select id="lx-preset" onchange="applyLxPreset(this.value)">
            <option value="custom" selected>Custom Selection</option>
            <option value="10">Narrow Spot (10&deg; Beam)</option>
            <option value="24">Spot Light (24&deg; Beam)</option>
            <option value="38">Flood Light (38&deg; Beam)</option>
            <option value="60">Wide Flood (60&deg; Beam)</option>
            <option value="120">Diffuse Downlight / Panel (120&deg; Beam)</option>
        </select>
    </div>
</div>
<button id="calc-lx-btn" class="calc-btn">Calculate Illuminance &amp; Coverage</button>
<div class="calc-results-card" id="lx-results">
    <h3>Photometric Illuminance &amp; Beam Spread</h3>
    <div class="result-row highlight-result">
        <span class="result-label">Center Beam Illuminance ($E$ in Lux):</span>
        <span class="result-val" id="res-lx-lux">553.8 Lux (lx)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Illuminance in Foot-Candles ($E_{\text{fc}}$):</span>
        <span class="result-val" id="res-lx-fc">51.4 fc (lumens/ft&sup2;)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Luminous Intensity (Peak Candela, $I_0$):</span>
        <span class="result-val" id="res-lx-cd">3,461.3 cd (Candela)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Solid Beam Angle ($\Omega$):</span>
        <span class="result-val" id="res-lx-omega">0.3467 steradians (sr)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Light Spot Coverage Diameter ($D$):</span>
        <span class="result-val" id="res-lx-diam">1.72 m (5.65 ft)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Illuminated Surface Area ($A$):</span>
        <span class="result-val" id="res-lx-area">2.33 m&sup2; (25.1 sq ft)</span>
    </div>
    <div class="result-row">
        <span class="result-label">IESNA Recommended Application:</span>
        <span class="result-val" id="res-lx-app">Commercial Office &amp; Reading (300 &ndash; 500 lx)</span>
    </div>
</div>
"""

TOOL6_JS = """
function applyLxPreset(val) {
    if (val !== 'custom') {
        document.getElementById('lx-angle').value = val;
        computeLumenLux();
    }
}

function computeLumenLux() {
    var lumens = parseFloat(document.getElementById('lx-lumens').value);
    var angleDeg = parseFloat(document.getElementById('lx-angle').value);
    var distVal = parseFloat(document.getElementById('lx-dist').value);
    var distUnit = parseFloat(document.getElementById('lx-dist-unit').value);

    if (isNaN(lumens) || lumens <= 0 || isNaN(angleDeg) || angleDeg <= 0 || angleDeg >= 180 || isNaN(distVal) || distVal <= 0) return;

    var d_m = distVal * distUnit; // distance in meters
    var d_ft = d_m * 3.28084;
    var thetaRad = (angleDeg * Math.PI) / 180.0;
    var halfAngleRad = thetaRad / 2.0;

    // Solid angle Omega = 2 * pi * (1 - cos(theta / 2))
    var omega = 2.0 * Math.PI * (1.0 - Math.cos(halfAngleRad)); // steradians

    // Luminous intensity I0 = Lumens / Omega (candela)
    var I0 = lumens / omega;

    // Illuminance at center E = I0 / d^2 (Lux)
    var lux = I0 / Math.pow(d_m, 2);
    var fc = lux / 10.7639104; // Foot-candles

    // Beam spread diameter D = 2 * d * tan(theta / 2)
    var D_m = 2.0 * d_m * Math.tan(halfAngleRad);
    var D_ft = D_m * 3.28084;

    // Lighted area A = pi * (D/2)^2
    var area_m2 = Math.PI * Math.pow(D_m / 2.0, 2);
    var area_sqft = area_m2 * 10.7639104;

    document.getElementById('res-lx-lux').textContent = lux.toFixed(1) + " Lux (lx)";
    document.getElementById('res-lx-fc').textContent = fc.toFixed(1) + " fc (lumens/ft\u00B2)";
    document.getElementById('res-lx-cd').textContent = I0.toFixed(1) + " cd (Candela)";
    document.getElementById('res-lx-omega').textContent = omega.toFixed(4) + " steradians (sr)";
    document.getElementById('res-lx-diam').textContent = D_m.toFixed(2) + " m (" + D_ft.toFixed(2) + " ft)";
    document.getElementById('res-lx-area').textContent = area_m2.toFixed(2) + " m\u00B2 (" + area_sqft.toFixed(1) + " sq ft)";

    // Application benchmark
    var appEl = document.getElementById('res-lx-app');
    if (lux >= 1000) {
        appEl.textContent = "High Precision Inspection & Drafting (> 1000 lx)";
    } else if (lux >= 500) {
        appEl.textContent = "General Commercial Office & Lab Bench (500 \u2013 1000 lx)";
    } else if (lux >= 300) {
        appEl.textContent = "Classrooms & Retail Merchandising (300 \u2013 500 lx)";
    } else if (lux >= 150) {
        appEl.textContent = "Residential Living, Kitchen & Workshop (150 \u2013 300 lx)";
    } else if (lux >= 50) {
        appEl.textContent = "Corridors, Stairwells & Parking Garages (50 \u2013 150 lx)";
    } else {
        appEl.textContent = "Night Security & Ambient Pathway (< 50 lx)";
    }
}

document.getElementById('calc-lx-btn').addEventListener('click', computeLumenLux);
['lx-lumens', 'lx-lumens-unit', 'lx-angle', 'lx-dist', 'lx-dist-unit'].forEach(function(id) {
    document.getElementById(id).addEventListener('input', computeLumenLux);
    document.getElementById(id).addEventListener('change', computeLumenLux);
});
window.addEventListener('DOMContentLoaded', computeLumenLux);
"""

TOOL6_ARTICLE = r"""
<h2>Photometric Science: Differentiating Flux, Intensity, and Illuminance</h2>
<p>In optical and architectural lighting design, confusion frequently arises between radiometric radiant energy (measured in Watts) and photometric luminous energy perceived by the human visual system. The International Commission on Illumination (CIE) defines the standard <strong>Photopic Luminous Efficiency Function $V(\lambda)$</strong>, which models the spectral sensitivity of human retinal cone photoreceptors. Human visual sensitivity peaks sharply at a green wavelength of $\lambda = 555\ \text{nm}$, where radiant flux converts to luminous flux at an exact physical ratio of $683\ \text{lumens per Watt}$.</p>

<p>Three core photometric quantities govern the design of luminaires, task planes, and architectural lighting layouts:</p>

<ul>
    <li><strong>Luminous Flux ($\Phi$, measured in Lumens, $\text{lm}$):</strong> The total rate of light energy emitted in all directions by a light source, weighted by the spectral sensitivity of the human eye. A bare $10\text{ W}$ modern LED emitter typically radiates between $800$ and $1,200\text{ lumens}$.</li>
    <li><strong>Luminous Intensity ($I$, measured in Candelas, $\text{cd}$):</strong> The concentration of luminous flux radiated into a specific directional solid angle ($\Omega$). One candela equals one lumen per steradian ($1\text{ cd} = 1\text{ lm/sr}$). Reflectors and optical lenses focus wide diffuse flux into concentrated beam angles, dramatically multiplying center beam intensity without changing total lumens.</li>
    <li><strong>Illuminance ($E$, measured in Lux, $\text{lx}$, or Foot-Candles, $\text{fc}$):</strong> The areal density of luminous flux incident upon a task surface. One lux equals one lumen per square meter ($1\text{ lx} = 1\text{ lm/m}^2$). The imperial unit is the foot-candle, representing one lumen per square foot ($1\text{ fc} = 1\text{ lm/ft}^2$). The exact conversion factor is:
    $$1\text{ Foot-Candle} = 10.7639\ \text{Lux}, \qquad 1\text{ Lux} = 0.0929\ \text{Foot-Candles}$$</li>
</ul>

<h2>Solid Angle Geometry and Peak Beam Intensity (Candela)</h2>
<p>When light from an LED or spotlight is constrained by a conical reflector of apex beam spread angle $\theta$ (in radians), the enclosed three-dimensional <strong>solid angle ($\Omega$)</strong> in steradians ($\text{sr}$) is evaluated by integrating over spherical coordinates:</p>
$$\Omega = \int_{0}^{2\pi} \int_{0}^{\theta/2} \sin\phi \, d\phi \, d\psi = 2\pi [-\cos\phi]_{0}^{\theta/2} = 2\pi \left( 1 - \cos\left( \frac{\theta}{2} \right) \right) \quad [\text{steradians}]$$

<p>Assuming a uniform intensity distribution across the optical beam, the luminous intensity $I_0$ (Center Beam Candlepower, CBCP) is:</p>
$$I_0 = \frac{\Phi}{\Omega} = \frac{\Phi}{2\pi \left( 1 - \cos\left( \frac{\theta}{2} \right) \right)} \quad [\text{Candelas}]$$

<p>This formulation explains why a narrow $10^\circ$ spot produces drastically higher peak surface illumination than a wide $120^\circ$ diffuse floodlight emitting the identical lumen package.</p>

<h2>The Inverse-Square Law of Illuminance</h2>
<p>For point sources and optical fixtures whose throw distance $d$ exceeds at least five times the luminaire aperture diameter ($d \ge 5D_{\text{aperture}}$), illuminance on a surface perpendicular to the beam axis follows the fundamental <strong>Inverse-Square Law</strong>:</p>
$$E = \frac{I_0}{d^2} \quad [\text{Lux}]$$

<p>Where $d$ is the throw distance measured in meters. If the task surface is inclined at an incident tilt angle $\beta$ relative to the beam axis, Lambert's Cosine Law applies:</p>
$$E_{\text{tilted}} = \frac{I_0 \cos(\beta)}{d^2}$$

<h3>Beam Spread Diameter and Illuminated Surface Area</h3>
<p>At throw distance $d$, the conical optical beam projects a circular light pool whose diameter $D$ and illuminated floor surface area $A$ are calculated geometrically via trigonometry:</p>
$$D = 2 \cdot d \cdot \tan\left( \frac{\theta}{2} \right) \quad [\text{Meters}]$$
$$A = \pi \left( \frac{D}{2} \right)^2 = \pi \left[ d \cdot \tan\left( \frac{\theta}{2} \right) \right]^2 \quad [\text{m}^2]$$

<table class="data-table">
    <thead>
        <tr>
            <th>Application Environment</th>
            <th>IESNA / EN 12464 Target Illuminance</th>
            <th>Foot-Candles (fc)</th>
            <th>Visual Task Complexity</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Emergency Corridors &amp; Stairwells</strong></td>
            <td>$50\text{--}100\ \text{lx}$</td>
            <td>$5\text{--}10\ \text{fc}$</td>
            <td>Orientation, safe egress, minimal reading</td>
        </tr>
        <tr>
            <td><strong>Warehouses &amp; Loading Docks</strong></td>
            <td>$150\text{--}200\ \text{lx}$</td>
            <td>$15\text{--}20\ \text{fc}$</td>
            <td>Material handling, rough inventory identification</td>
        </tr>
        <tr>
            <td><strong>General Commercial Office Work</strong></td>
            <td>$400\text{--}500\ \text{lx}$</td>
            <td>$40\text{--}50\ \text{fc}$</td>
            <td>Continuous VDT typing, data entry, reading paper</td>
        </tr>
        <tr>
            <td><strong>Classrooms &amp; Lecture Theatres</strong></td>
            <td>$300\text{--}500\ \text{lx}$</td>
            <td>$30\text{--}50\ \text{fc}$</td>
            <td>Whiteboard visibility, writing, active learning</td>
        </tr>
        <tr>
            <td><strong>Electronic Assembly &amp; SMD Soldering</strong></td>
            <td>$1,000\text{--}1,500\ \text{lx}$</td>
            <td>$100\text{--}150\ \text{fc}$</td>
            <td>Microscopic component inspection, manual soldering</td>
        </tr>
        <tr>
            <td><strong>Hospital Surgical Operating Theatres</strong></td>
            <td>$10,000\text{--}50,000\ \text{lx}$</td>
            <td>$1,000\text{--}5,000\ \text{fc}$</td>
            <td>Deep cavity surgical tissue differentiation</td>
        </tr>
    </tbody>
</table>

<div class="worked-example-card">
    <h4>Step-by-Step Engineering Case Study: Museum Art Gallery Track Lighting</h4>
    <p><strong>Scenario:</strong> A museum gallery requires accent lighting for an oil painting. The track fixture is mounted at a ceiling distance of $d = 3.0\ \text{meters}$ ($9.84\ \text{ft}$) from the artwork. Curatorial conservation guidelines mandate a maximum illuminance of $E = 200\ \text{Lux}$ to prevent photochemical pigment fading. An LED spot fixture with a narrow $\theta = 24^\circ$ beam angle is selected.</p>
    <div class="step-solution">
        <p><strong>Step 1: Calculate Solid Angle ($\Omega$) for $24^\circ$ Conical Beam:</strong></p>
        $$\frac{\theta}{2} = 12^\circ = 0.20944\ \text{radians}$$
        $$\Omega = 2\pi (1 - \cos(12^\circ)) = 2\pi (1 - 0.97815) = 2\pi \times 0.02185 = 0.1373\ \text{steradians}$$
        <p><strong>Step 2: Determine Required Luminous Intensity ($I_0$) for $200\ \text{Lux}$ at $3.0\ \text{m}$:</strong></p>
        $$I_0 = E \cdot d^2 = 200\ \text{lx} \times (3.0\ \text{m})^2 = 200 \times 9.0 = 1,800\ \text{Candelas (cd)}$$
        <p><strong>Step 3: Calculate Maximum Permissible Emitter Lumens ($\Phi$):</strong></p>
        $$\Phi = I_0 \cdot \Omega = 1,800\ \text{cd} \times 0.1373\ \text{sr} = 247.14\ \text{Lumens}$$
        <p><strong>Step 4: Determine Light Pool Coverage Diameter on the Painting:</strong></p>
        $$D = 2 \cdot d \cdot \tan(12^\circ) = 2 \times 3.0 \times 0.21256 = 1.275\ \text{meters} \approx 4.18\ \text{ft}$$
        <p><strong>Conclusion:</strong> To comply with conservation standards, the museum must install a dimmable LED fixture calibrated to exactly $250\ \text{lumens}$, projecting a $1.28\ \text{m}$ diameter spot delivering $200\ \text{lux}$.</p>
    </div>
</div>

<h2>Frequently Asked Questions (FAQ)</h2>
<div class="faq-section">
    <h3>What is the difference between Lumens, Lux, and Candelas?</h3>
    <p>Lumens ($\text{lm}$) measure total luminous flux emitted by a light source in all directions. Candela ($\text{cd}$) measures luminous intensity emitted into a specific directional solid angle ($1\text{ cd} = 1\text{ lm/sr}$). Lux ($\text{lx}$) measures illuminance, which is the density of luminous flux incident on a surface ($1\text{ lx} = 1\text{ lm/m}^2$). Foot-Candle ($\text{fc}$) is the imperial equivalent ($1\text{ fc} = 1\text{ lm/ft}^2 = 10.764\ \text{lux}$).</p>

    <h3>How does the Inverse-Square Law affect illuminance?</h3>
    <p>Illuminance drops inversely with the square of throw distance: $E = I / d^2$. Doubling the distance between a light source and a task surface reduces illuminance to one-fourth ($25\%$) of its original level.</p>

    <h3>How do you calculate peak center beam candela from lumens and beam angle?</h3>
    <p>For a conical beam of angle $\theta$, the solid angle is $\Omega = 2\pi (1 - \cos(\theta / 2))$. The average luminous intensity is $I = \text{Lumens} / \Omega$. In real optical reflectors, the peak center beam candela (CBCP) is directly governed by this geometric concentration.</p>

    <h3>What are recommended IESNA / OSHA illuminance levels?</h3>
    <p>Hallways and corridors: $100\text{ lux}$ ($10\text{ fc}$); General office work and computer labs: $300$ to $500\text{ lux}$ ($30$ to $50\text{ fc}$); Detailed drafting, PCB soldering, and precision inspection: $1,000$ to $2,000\text{ lux}$ ($100$ to $200\text{ fc}$); Surgical suites: $10,000$ to $50,000\text{ lux}$.</p>
</div>
"""

def generate_tool(slug, title, desc, h1, short_desc, schema_json, ui_html, js_code, article_html):
    full_html = HEADER_HTML.format(
        title=title,
        description=desc,
        slug=slug,
        h1=h1,
        short_desc=short_desc,
        schema_json=schema_json,
        calc_ui=ui_html,
        article_content=article_html,
        calc_js=js_code
    )
    filepath = os.path.join(r"C:\Users\Admin\.gemini\antigravity\scratch\calchub", f"{slug}.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Generated: {filepath}")

if __name__ == "__main__":
    generate_tool(TOOL5_SLUG, TOOL5_TITLE, TOOL5_DESC, TOOL5_H1, TOOL5_SHORT, TOOL5_SCHEMA, TOOL5_UI, TOOL5_JS, TOOL5_ARTICLE)
    generate_tool(TOOL6_SLUG, TOOL6_TITLE, TOOL6_DESC, TOOL6_H1, TOOL6_SHORT, TOOL6_SCHEMA, TOOL6_UI, TOOL6_JS, TOOL6_ARTICLE)
