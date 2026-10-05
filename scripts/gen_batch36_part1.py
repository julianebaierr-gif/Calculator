# -*- coding: utf-8 -*-
"""
Generator for Batch 36 - Part 1
Tools:
1. pcb-trace-width-calculator.html
2. factor-of-safety-calculator.html
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
                        <li><a href="pcb-trace-width-calculator.html">PCB Trace Width Calculator</a></li>
                        <li><a href="factor-of-safety-calculator.html">Factor of Safety Calculator</a></li>
                        <li><a href="stress-strain-calculator.html">Stress and Strain Calculator</a></li>
                        <li><a href="voltage-divider-calculator.html">Voltage Divider Calculator</a></li>
                        <li><a href="wire-ampacity-calculator.html">Wire Ampacity Calculator</a></li>
                        <li><a href="heatsink-calculator.html">Heatsink Thermal Calculator</a></li>
                        <li><a href="microstrip-impedance-calculator.html">Microstrip Impedance</a></li>
                        <li><a href="parallel-resistance-calculator.html">Parallel Resistance</a></li>
                        <li><a href="ohms-law-calculator.html">Ohm's Law Calculator</a></li>
                        <li><a href="bolt-torque-calculator.html">Bolt Torque Calculator</a></li>
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
                    <p>CalcHub provides free, rigorous, engineering-grade calculators, physics simulation utilities, and structural models verified against international standards (IPC, ASME, IEEE, ISO).</p>
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
                    <h4>Engineering Tools</h4>
                    <ul class="footer-links">
                        <li><a href="pcb-trace-width-calculator.html">PCB Trace Sizing (IPC-2152)</a></li>
                        <li><a href="factor-of-safety-calculator.html">Factor of Safety (ASME)</a></li>
                        <li><a href="microstrip-impedance-calculator.html">Microstrip Impedance</a></li>
                        <li><a href="stress-strain-calculator.html">Stress &amp; Strain Analysis</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 CalcHub. All rights reserved. Precision computational tools for design engineers and physical scientists.</p>
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
# TOOL 1: pcb-trace-width-calculator.html
# ==============================================================================
TOOL1_SLUG = "pcb-trace-width-calculator"
TOOL1_TITLE = "PCB Trace Width Calculator - IPC-2152 & IPC-2221 Current Capacity"
TOOL1_DESC = "Calculate PCB trace width, cross-sectional area, ampacity, voltage drop, and temperature rise using IPC-2221 and IPC-2152 thermal design standards."
TOOL1_H1 = "PCB Trace Width Calculator (IPC-2152 &amp; IPC-2221)"
TOOL1_SHORT = "Determine required printed circuit board copper trace width for target current, allowable temperature rise, copper weight, and trace length."

TOOL1_SCHEMA = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "PCB Trace Width Calculator",
      "url": "https://calchub.com/pcb-trace-width-calculator.html",
      "description": "Calculates PCB trace width, ampacity, cross-sectional area, voltage drop, and power loss based on IPC-2221 and IPC-2152 standards.",
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
          "name": "What is the difference between IPC-2221 and IPC-2152 trace sizing?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "IPC-2221 is based on legacy empirical charts dating back to 1954 National Bureau of Standards experiments on isolated traces in vacuum/air, which often overestimate required trace width. IPC-2152 is the modern comprehensive standard based on physical thermal measurements that account for board thickness, FR-4 substrate thermal conductivity, internal plane heat spreading, and convective cooling."
          }
        },
        {
          "@type": "Question",
          "name": "Why do internal PCB traces require greater width than external traces for the same current?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "External traces sit in contact with ambient air, facilitating natural convective and radiative heat dissipation. Internal traces are completely encapsulated by epoxy-glass FR-4 dielectric, which acts as a thermal insulator (low thermal conductivity ~0.25 W/mK). Consequently, internal layers retain heat and require approximately twice the cross-sectional area to maintain identical temperature rise."
          }
        },
        {
          "@type": "Question",
          "name": "What is standard 1 oz copper thickness?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "One ounce (1 oz) of copper represents 1 oz of copper rolled flat over one square foot of area, resulting in a nominal foil thickness of approximately 1.37 mils (0.00137 inches or 34.8 micrometers). Common PCB copper weights include 0.5 oz (17.5 um), 1 oz (35 um), 2 oz (70 um), and 3 oz (105 um)."
          }
        },
        {
          "@type": "Question",
          "name": "What allowable temperature rise (Delta T) is standard for PCB traces?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "For commercial electronics operating at 25 C to 40 C ambient, a 10 C temperature rise is common. For high-density power electronics or automotive under-hood applications, designers often allow 20 C to 30 C Delta T, provided total peak temperature remains below the FR-4 glass transition temperature (Tg, typically 130 C to 170 C)."
          }
        }
      ]
    }
  ]
}"""

TOOL1_UI = """
<div class="calc-grid">
    <div class="calc-input-group">
        <label for="pcb-current">Design Current ($I$):</label>
        <div class="input-with-select">
            <input type="number" id="pcb-current" value="3.0" min="0.01" step="any">
            <select id="pcb-current-unit">
                <option value="1" selected>Amperes (A)</option>
                <option value="0.001">Milliamperes (mA)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="pcb-temp-rise">Allowable Temperature Rise ($\Delta T$):</label>
        <div class="input-with-select">
            <input type="number" id="pcb-temp-rise" value="10" min="1" max="100" step="any">
            <select id="pcb-temp-unit">
                <option value="1" selected>&deg;C</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="pcb-cu-weight">Copper Foil Weight / Thickness:</label>
        <select id="pcb-cu-weight">
            <option value="0.5">0.5 oz/ft&sup2; (17.5 &mu;m / 0.69 mil)</option>
            <option value="1.0" selected>1.0 oz/ft&sup2; (35.0 &mu;m / 1.37 mil)</option>
            <option value="2.0">2.0 oz/ft&sup2; (70.0 &mu;m / 2.74 mil)</option>
            <option value="3.0">3.0 oz/ft&sup2; (105.0 &mu;m / 4.11 mil)</option>
            <option value="4.0">4.0 oz/ft&sup2; (140.0 &mu;m / 5.48 mil)</option>
        </select>
    </div>
    <div class="calc-input-group">
        <label for="pcb-length">Trace Physical Length ($L$):</label>
        <div class="input-with-select">
            <input type="number" id="pcb-length" value="2.0" min="0.01" step="any">
            <select id="pcb-length-unit">
                <option value="1" selected>Inches (in)</option>
                <option value="0.03937">Millimeters (mm)</option>
                <option value="0.3937">Centimeters (cm)</option>
            </select>
        </div>
    </div>
</div>
<button id="calc-pcb-btn" class="calc-btn">Calculate PCB Trace Dimensions</button>
<div class="calc-results-card" id="pcb-results">
    <h3>Conductor Sizing &amp; Thermal Dissipation</h3>
    <div class="result-row highlight-result">
        <span class="result-label">External Layer Required Width:</span>
        <span class="result-val" id="res-pcb-w-ext">48.24 mils (1.225 mm)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Internal Layer Required Width:</span>
        <span class="result-val" id="res-pcb-w-int">125.43 mils (3.186 mm)</span>
    </div>
    <div class="result-row">
        <span class="result-label">External Cross-Sectional Area:</span>
        <span class="result-val" id="res-pcb-area-ext">66.08 mils&sup2; (0.0426 mm&sup2;)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Trace DC Resistance ($R_{\text{DC}}$ at 25&deg;C):</span>
        <span class="result-val" id="res-pcb-rdc">0.0205 &Omega; (20.5 m&Omega;)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Voltage Drop across Length ($\Delta V$):</span>
        <span class="result-val" id="res-pcb-vdrop">0.0616 V (61.6 mV)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Ohmic Power Loss ($P_{\text{loss}} = I^2 R$):</span>
        <span class="result-val" id="res-pcb-ploss">0.185 W (184.7 mW)</span>
    </div>
</div>
"""

TOOL1_JS = """
function computePcbTrace() {
    var iVal = parseFloat(document.getElementById('pcb-current').value);
    var iUnit = parseFloat(document.getElementById('pcb-current-unit').value);
    var dt = parseFloat(document.getElementById('pcb-temp-rise').value);
    var cuOz = parseFloat(document.getElementById('pcb-cu-weight').value);
    var lVal = parseFloat(document.getElementById('pcb-length').value);
    var lUnit = parseFloat(document.getElementById('pcb-length-unit').value);

    if (isNaN(iVal) || iVal <= 0 || isNaN(dt) || dt <= 0) return;

    var I = iVal * iUnit; // Amperes
    var L_in = lVal * lUnit; // Inches
    var thicknessMils = cuOz * 1.378; // mils (1 oz = 1.378 mils = 35 um)

    // IPC-2221 Formula: I = k * (dt)^0.44 * A^0.725
    // Area A = (I / (k * dt^0.44))^(1 / 0.725) mils^2
    // For external layers: k = 0.048
    // For internal layers: k = 0.024
    var k_ext = 0.048;
    var k_int = 0.024;
    var b = 0.44;
    var c = 0.725;

    var A_ext = Math.pow(I / (k_ext * Math.pow(dt, b)), 1.0 / c); // mils^2
    var A_int = Math.pow(I / (k_int * Math.pow(dt, b)), 1.0 / c); // mils^2

    var W_ext_mils = A_ext / thicknessMils;
    var W_int_mils = A_int / thicknessMils;

    var W_ext_mm = W_ext_mils * 0.0254;
    var W_int_mm = W_int_mils * 0.0254;

    var A_ext_mm2 = A_ext * 0.00064516;

    // Resistance calculation
    // Resistivity of annealed copper rho = 1.724e-6 ohm-cm = 6.787e-7 ohm-in
    // R = rho * L / A
    // In mils: R = (6.787e-7 ohm-in * L_in) / (A_ext * 1e-6 sq in) = 0.6787 * L_in / A_ext
    // Accounting for temperature: R_T = R_25 * (1 + 0.00393 * (dt))
    var R_dc = (6.787e-1 * L_in / A_ext) * (1.0 + 0.00393 * (dt / 2.0));
    var V_drop = I * R_dc;
    var P_loss = I * I * R_dc;

    document.getElementById('res-pcb-w-ext').textContent = W_ext_mils.toFixed(2) + " mils (" + W_ext_mm.toFixed(3) + " mm)";
    document.getElementById('res-pcb-w-int').textContent = W_int_mils.toFixed(2) + " mils (" + W_int_mm.toFixed(3) + " mm)";
    document.getElementById('res-pcb-area-ext').innerHTML = A_ext.toFixed(2) + " mils&sup2; (" + A_ext_mm2.toFixed(4) + " mm&sup2;)";

    if (R_dc >= 1) {
        document.getElementById('res-pcb-rdc').textContent = R_dc.toFixed(4) + " \u03A9";
    } else {
        document.getElementById('res-pcb-rdc').textContent = (R_dc * 1000).toFixed(2) + " m\u03A9 (" + R_dc.toFixed(4) + " \u03A9)";
    }

    if (V_drop >= 1) {
        document.getElementById('res-pcb-vdrop').textContent = V_drop.toFixed(4) + " V";
    } else {
        document.getElementById('res-pcb-vdrop').textContent = (V_drop * 1000).toFixed(2) + " mV (" + V_drop.toFixed(4) + " V)";
    }

    if (P_loss >= 1) {
        document.getElementById('res-pcb-ploss').textContent = P_loss.toFixed(3) + " W";
    } else {
        document.getElementById('res-pcb-ploss').textContent = (P_loss * 1000).toFixed(2) + " mW (" + P_loss.toFixed(4) + " W)";
    }
}

document.getElementById('calc-pcb-btn').addEventListener('click', computePcbTrace);
['pcb-current', 'pcb-current-unit', 'pcb-temp-rise', 'pcb-cu-weight', 'pcb-length', 'pcb-length-unit'].forEach(function(id) {
    document.getElementById(id).addEventListener('input', computePcbTrace);
    document.getElementById(id).addEventListener('change', computePcbTrace);
});
window.addEventListener('DOMContentLoaded', computePcbTrace);
"""

TOOL1_ARTICLE = r"""
<h2>Physics and Standards of Printed Circuit Board Conductor Sizing</h2>
<p>Printed circuit board (PCB) traces are rectangular copper conductors laminated onto dielectric substrates such as standard FR-4 (flame retardant woven glass-reinforced epoxy). When electric current flows through a conductive trace, electrical resistance converts energy into thermal dissipation via Joule heating ($P = I^2 R$). As thermal energy accumulates, the conductor temperature rises until the rate of internal heat generation equals the rate of convective, conductive, and radiative heat transfer to the ambient environment and neighboring PCB structural planes.</p>

<p>Accurate trace width determination is vital in high-reliability hardware engineering. Undersized conductors experience excessive thermal stress, leading to conductor delamination, dielectric blistering, solder mask discoloration, solder joint reflow fatigue, and catastrophic trace vaporization during surge events. Conversely, excessively wide traces consume critical PCB routing area, increase parasitic capacitance to adjacent planes, and limit component escape routing on high-density interconnect (HDI) multilayer boards.</p>

<h2>IPC-2221 Empirical Conductor Sizing Model</h2>
<p>The historical benchmark for printed circuit board current capacity is the IPC-2221 standard (formerly IPC-D-275), formulated from classic experiments conducted by the National Bureau of Standards (NBS) in 1954. The standard establishes an empirical power-law relationship correlating permissible continuous DC current ($I$), allowable conductor temperature rise ($\Delta T$), and cross-sectional area ($A$):</p>
$$I = k \cdot (\Delta T)^b \cdot A^c$$

<p>Where:</p>
<ul>
    <li><strong>$I$</strong>: Maximum allowable continuous current in Amperes ($\text{A}$).</li>
    <li><strong>$\Delta T$</strong>: Maximum allowable temperature rise above ambient in degrees Celsius ($^\circ\text{C}$).</li>
    <li><strong>$A$</strong>: Cross-sectional conductor area in square mils ($\text{mils}^2$, where $1\text{ mil} = 0.001\text{ inch} = 25.4\ \mu\text{m}$).</li>
    <li><strong>$k$</strong>: Layer-dependent empirical constant ($k = 0.048$ for external surface layers; $k = 0.024$ for internal buried layers).</li>
    <li><strong>$b$</strong>: Temperature exponent constant ($b = 0.44$).</li>
    <li><strong>$c$</strong>: Geometric area exponent constant ($c = 0.725$).</li>
</ul>

<p>Inverting the empirical power law to solve for the required cross-sectional conductor area $A$:</p>
$$A = \left( \frac{I}{k \cdot (\Delta T)^b} \right)^{\frac{1}{c}} = \left( \frac{I}{k \cdot (\Delta T)^{0.44}} \right)^{\frac{1}{0.725}} \quad [\text{mils}^2]$$

<p>Once cross-sectional area $A$ is determined, the physical required trace width $W$ is calculated by dividing by the nominal copper foil thickness $T_{\text{copper}}$:</p>
$$W = \frac{A}{T_{\text{copper}}} \quad [\text{mils}]$$

<h3>Copper Foil Thickness and Standard Ounce Weights</h3>
<p>In printed circuit manufacturing, copper thickness is designated in ounces per square foot ($\text{oz/ft}^2$). One ounce ($1\text{ oz}$) of copper corresponds to the thickness of one avoirdupois ounce of copper rolled flat across a surface area of exactly one square foot ($0.0929\ \text{m}^2$). The equivalent geometric thickness values are tabulated below:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Designation</th>
            <th>Nominal Weight</th>
            <th>Thickness (mils)</th>
            <th>Thickness ($\mu\text{m}$)</th>
            <th>Primary Application</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>0.5 oz (H oz)</strong></td>
            <td>$0.5\ \text{oz/ft}^2$</td>
            <td>$0.69\ \text{mils}$</td>
            <td>$17.5\ \mu\text{m}$</td>
            <td>Fine-pitch HDI, high-speed digital escape routing</td>
        </tr>
        <tr>
            <td><strong>1.0 oz (1 oz)</strong></td>
            <td>$1.0\ \text{oz/ft}^2$</td>
            <td>$1.38\ \text{mils}$</td>
            <td>$35.0\ \mu\text{m}$</td>
            <td>Standard commercial multilayer signals and low power</td>
        </tr>
        <tr>
            <td><strong>2.0 oz (2 oz)</strong></td>
            <td>$2.0\ \text{oz/ft}^2$</td>
            <td>$2.76\ \text{mils}$</td>
            <td>$70.0\ \mu\text{m}$</td>
            <td>Industrial DC-DC switch-mode converters, motor drivers</td>
        </tr>
        <tr>
            <td><strong>3.0 oz (3 oz)</strong></td>
            <td>$3.0\ \text{oz/ft}^2$</td>
            <td>$4.13\ \text{mils}$</td>
            <td>$105.0\ \mu\text{m}$</td>
            <td>Heavy copper automotive, solar inverters, high-current bus</td>
        </tr>
        <tr>
            <td><strong>4.0 oz (4 oz)</strong></td>
            <td>$4.0\ \text{oz/ft}^2$</td>
            <td>$5.51\ \text{mils}$</td>
            <td>$140.0\ \mu\text{m}$</td>
            <td>Extreme power distribution, aerospace power distribution</td>
        </tr>
    </tbody>
</table>

<h2>IPC-2152 Modern Standard and Thermal Spreading Improvements</h2>
<p>While IPC-2221 provided a safe conservative baseline for decades, modern multi-layer boards differ drastically from 1950s single-sided boards. The current industry standard, <strong>IPC-2152 (Standard for Determining Current-Carrying Capacity in Printed Board Design)</strong>, was developed through comprehensive empirical and finite element modeling (FEM). Key insights incorporated into IPC-2152 include:</p>
<ul>
    <li><strong>Internal Plane Thermal Sinking:</strong> Solid internal copper ground and power planes act as effective heat spreaders. An external trace routed over an unbroken ground plane runs substantially cooler than an isolated trace because heat conducts through the thin prepreg dielectric into the copper plane.</li>
    <li><strong>Substrate Thickness and Thermal Conductivity:</strong> Thicker core substrates offer higher thermal capacitance, but FR-4 has poor through-plane thermal conductivity ($k_z \approx 0.25\text{--}0.35\ \text{W/m}\cdot\text{K}$). High-temperature substrates like polyimide or ceramic-filled hydrocarbons exhibit improved thermal performance.</li>
    <li><strong>Solder Mask and Conformal Coating:</strong> A standard solder mask layer ($0.5\text{--}1.0\ \text{mil}$) increases the effective infrared emissivity of bare copper from $\sim 0.05$ to over $0.85$, significantly enhancing radiative cooling.</li>
</ul>

<h2>DC Resistance, Voltage Drop, and Joule Heating Calculations</h2>
<p>In addition to thermal rise limits, designers must verify that DC voltage drop ($\Delta V$) across long power traces does not breach supply tolerance thresholds for sensitive integrated circuits (e.g., modern microprocessors requiring $1.0\text{ V} \pm 3\%$).</p>

<p>The electrical resistance of a copper trace at room temperature ($25^\circ\text{C}$) is given by:</p>
$$R_{\text{DC}} = \rho_{25} \cdot \frac{L}{A} = \left( 1.724 \times 10^{-6}\ \Omega\cdot\text{cm} \right) \cdot \frac{L}{A}$$

<p>Accounting for the positive temperature coefficient of annealed copper ($\alpha = 0.00393\ /^\circ\text{C}$):</p>
$$R_T = R_{25} \cdot [1 + \alpha \cdot (\Delta T)]$$
$$\Delta V = I \cdot R_T, \qquad P_{\text{loss}} = I^2 \cdot R_T$$

<div class="worked-example-card">
    <h4>Step-by-Step Engineering Case Study: 12V 5A Buck Converter Power Stage Trace</h4>
    <p><strong>Scenario:</strong> A point-of-load synchronous buck converter delivers continuous $I = 5.0\ \text{A}$ across an external surface trace with a length of $L = 3.0\ \text{inches}$ ($76.2\ \text{mm}$). The board uses standard $1\ \text{oz}$ copper foil ($T = 1.378\ \text{mils}$). The allowable temperature rise is set to $\Delta T = 15^\circ\text{C}$.</p>
    <div class="step-solution">
        <p><strong>Step 1: Calculate Required Cross-Sectional Area ($A_{\text{ext}}$):</strong></p>
        $$A = \left( \frac{I}{0.048 \times (\Delta T)^{0.44}} \right)^{\frac{1}{0.725}} = \left( \frac{5.0}{0.048 \times 15^{0.44}} \right)^{\frac{1}{0.725}}$$
        $$\Delta T^{0.44} = 15^{0.44} \approx 3.303$$
        $$A = \left( \frac{5.0}{0.048 \times 3.303} \right)^{\frac{1}{0.725}} = \left( \frac{5.0}{0.15854} \right)^{1.3793} = (31.537)^{1.3793} \approx 117.82\ \text{mils}^2$$
        <p><strong>Step 2: Determine Required External Trace Width ($W$):</strong></p>
        $$W = \frac{A}{T_{\text{copper}}} = \frac{117.82\ \text{mils}^2}{1.378\ \text{mils}} = 85.50\ \text{mils} \approx 2.172\ \text{mm}$$
        <p><strong>Step 3: Calculate Conductor Resistance and Voltage Drop:</strong></p>
        $$R_{\text{DC}} = \frac{0.6787 \times 3.0\ \text{in}}{117.82\ \text{mils}^2} \times [1 + 0.00393 \times 7.5] = 0.01728 \times 1.0295 = 0.01779\ \Omega\ (17.79\ \text{m}\Omega)$$
        $$\Delta V = I \cdot R = 5.0\ \text{A} \times 0.01779\ \Omega = 0.0889\ \text{V} = 88.9\ \text{mV}$$
        <p><strong>Step 4: Determine Power Dissipation:</strong></p>
        $$P_{\text{loss}} = I^2 \cdot R = (5.0)^2 \times 0.01779 = 25 \times 0.01779 = 0.445\ \text{Watts} = 445\ \text{mW}$$
        <p><strong>Conclusion:</strong> A minimum trace width of $86\ \text{mils}$ ($2.2\ \text{mm}$) is required on the external layer to restrict temperature rise to $15^\circ\text{C}$ and hold voltage drop to under $90\ \text{mV}$.</p>
    </div>
</div>

<h2>Frequently Asked Questions (FAQ)</h2>
<div class="faq-section">
    <h3>What is the difference between IPC-2221 and IPC-2152 trace sizing?</h3>
    <p>IPC-2221 is based on legacy empirical charts dating back to 1954 National Bureau of Standards experiments on isolated traces in vacuum/air, which often overestimate required trace width. IPC-2152 is the modern comprehensive standard based on physical thermal measurements that account for board thickness, FR-4 substrate thermal conductivity, internal plane heat spreading, and convective cooling.</p>

    <h3>Why do internal PCB traces require greater width than external traces for the same current?</h3>
    <p>External traces sit in contact with ambient air, facilitating natural convective and radiative heat dissipation. Internal traces are completely encapsulated by epoxy-glass FR-4 dielectric, which acts as a thermal insulator (low thermal conductivity $\sim 0.25\ \text{W/m}\cdot\text{K}$). Consequently, internal layers retain heat and require approximately twice the cross-sectional area to maintain identical temperature rise.</p>

    <h3>What is standard 1 oz copper thickness?</h3>
    <p>One ounce ($1\ \text{oz}$) of copper represents $1\ \text{oz}$ of copper rolled flat over one square foot of area, resulting in a nominal foil thickness of approximately $1.378\ \text{mils}$ ($0.001378\ \text{inches}$ or $35.0\ \mu\text{m}$). Common PCB copper weights include $0.5\ \text{oz}$ ($17.5\ \mu\text{m}$), $1\ \text{oz}$ ($35\ \mu\text{m}$), $2\ \text{oz}$ ($70\ \mu\text{m}$), and $3\ \text{oz}$ ($105\ \mu\text{m}$).</p>

    <h3>What allowable temperature rise ($\Delta T$) is standard for PCB traces?</h3>
    <p>For commercial electronics operating at $25^\circ\text{C}$ to $40^\circ\text{C}$ ambient, a $10^\circ\text{C}$ temperature rise is common. For high-density power electronics or automotive under-hood applications, designers often allow $20^\circ\text{C}$ to $30^\circ\text{C}$ $\Delta T$, provided total peak temperature remains below the FR-4 glass transition temperature ($T_g$, typically $130^\circ\text{C}$ to $170^\circ\text{C}$).</p>
</div>
"""

# ==============================================================================
# TOOL 2: factor-of-safety-calculator.html
# ==============================================================================
TOOL2_SLUG = "factor-of-safety-calculator"
TOOL2_TITLE = "Factor of Safety Calculator - Structural, Yield & Fatigue Design (ASME)"
TOOL2_DESC = "Calculate mechanical Factor of Safety (FoS = Yield/Working Stress), Margin of Safety (MoS), Goodman fatigue limit, and structural compliance with ASME/AISC standards."
TOOL2_H1 = "Factor of Safety Calculator (FoS &amp; MoS)"
TOOL2_SHORT = "Compute mechanical Factor of Safety (FoS), Margin of Safety (MoS), von Mises yield ratios, and cyclic fatigue endurance limits."

TOOL2_SCHEMA = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Factor of Safety Calculator",
      "url": "https://calchub.com/factor-of-safety-calculator.html",
      "description": "Calculates Factor of Safety (FoS), Margin of Safety (MoS), and cyclic fatigue limits using static yield and modified Goodman criteria.",
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
          "name": "What is the difference between Factor of Safety (FoS) and Margin of Safety (MoS)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Factor of Safety is the ratio of structural capacity (yield or ultimate strength) to applied operational stress: FoS = S_material / sigma_working. Margin of Safety is defined as MoS = FoS - 1 = (S_material / sigma_working) - 1. An MoS > 0 indicates structural adequacy, MoS = 0 represents boundary capacity, and MoS < 0 denotes failure."
          }
        },
        {
          "@type": "Question",
          "name": "Should Factor of Safety be based on Yield Strength or Ultimate Tensile Strength?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "For ductile materials (structural steel, aluminum alloys) in machines and buildings, FoS is universally based on Yield Strength (S_y) to prevent permanent plastic deformation. For brittle materials (cast iron, ceramics, concrete) or catastrophic containment vessels, FoS is calculated against Ultimate Tensile Strength (S_ut) using higher safety margins."
          }
        },
        {
          "@type": "Question",
          "name": "What is the modified Goodman relation for fatigue loading?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Under fluctuating cyclic loading with alternating stress sigma_a and mean tensile stress sigma_m, the modified Goodman criterion determines safety against fatigue failure: (sigma_a / S_e) + (sigma_m / S_ut) = 1 / FoS, where S_e is the endurance limit and S_ut is the ultimate tensile strength."
          }
        },
        {
          "@type": "Question",
          "name": "What are typical engineering Factor of Safety values across industries?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Aerospace: 1.25 to 1.50 (mass critical); Automotive: 1.5 to 2.5; Civil structural steel (AISC): 1.67 to 2.0; Boilers and pressure vessels (ASME Section VIII): 3.5 to 4.0; Elevators and wire ropes: 8.0 to 12.0."
          }
        }
      ]
    }
  ]
}"""

TOOL2_UI = """
<div class="calc-grid">
    <div class="calc-input-group">
        <label for="fos-mode">Failure Criterion Mode:</label>
        <select id="fos-mode">
            <option value="yield" selected>Static Yield Strength ($S_y$ - Ductile Materials)</option>
            <option value="ultimate">Ultimate Tensile Strength ($S_{ut}$ - Brittle / Burst)</option>
            <option value="fatigue">Cyclic Fatigue (Modified Goodman Criterion)</option>
        </select>
    </div>
    <div class="calc-input-group" id="grp-fos-str">
        <label for="fos-strength">Material Strength ($S_y$ or $S_{ut}$):</label>
        <div class="input-with-select">
            <input type="number" id="fos-strength" value="250" min="0.1" step="any">
            <select id="fos-str-unit">
                <option value="1" selected>MPa (N/mm&sup2;)</option>
                <option value="0.001">GPa</option>
                <option value="6.894757">ksi</option>
                <option value="0.006894757">psi</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group" id="grp-fos-work">
        <label for="fos-working">Applied Working Stress ($\sigma_{\text{work}}$):</label>
        <div class="input-with-select">
            <input type="number" id="fos-working" value="125" min="0.1" step="any">
            <select id="fos-work-unit">
                <option value="1" selected>MPa (N/mm&sup2;)</option>
                <option value="0.001">GPa</option>
                <option value="6.894757">ksi</option>
                <option value="0.006894757">psi</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group" id="grp-fos-alt" style="display:none;">
        <label for="fos-sigma-a">Alternating Stress Amplitude ($\sigma_a$):</label>
        <div class="input-with-select">
            <input type="number" id="fos-sigma-a" value="50" min="0" step="any">
            <select id="fos-sigma-a-unit">
                <option value="1" selected>MPa</option>
                <option value="6.894757">ksi</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group" id="grp-fos-end" style="display:none;">
        <label for="fos-se">Endurance Limit ($S_e$):</label>
        <div class="input-with-select">
            <input type="number" id="fos-se" value="150" min="0.1" step="any">
            <select id="fos-se-unit">
                <option value="1" selected>MPa</option>
                <option value="6.894757">ksi</option>
            </select>
        </div>
    </div>
</div>
<button id="calc-fos-btn" class="calc-btn">Calculate Safety Margin</button>
<div class="calc-results-card" id="fos-results">
    <h3>Structural Adequacy &amp; Safety Factors</h3>
    <div class="result-row highlight-result">
        <span class="result-label">Factor of Safety ($\text{FoS}$):</span>
        <span class="result-val" id="res-fos-val">2.000</span>
    </div>
    <div class="result-row">
        <span class="result-label">Margin of Safety ($\text{MoS} = \text{FoS} - 1$):</span>
        <span class="result-val" id="res-fos-mos">+1.000 (+100.0%)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Structural Integrity Assessment:</span>
        <span class="result-val" id="res-fos-status" style="color:#16a34a; font-weight:700;">SAFE &amp; ADEQUATE</span>
    </div>
    <div class="result-row">
        <span class="result-label">Allowable Working Capacity Utilization:</span>
        <span class="result-val" id="res-fos-util">50.0%</span>
    </div>
    <div class="result-row">
        <span class="result-label">Industry Benchmark Comparison:</span>
        <span class="result-val" id="res-fos-benchmark">Meets Standard Machinery (1.5 &ndash; 2.5)</span>
    </div>
</div>
"""

TOOL2_JS = """
function updateFosMode() {
    var mode = document.getElementById('fos-mode').value;
    var isFatigue = (mode === 'fatigue');
    document.getElementById('grp-fos-alt').style.display = isFatigue ? 'block' : 'none';
    document.getElementById('grp-fos-end').style.display = isFatigue ? 'block' : 'none';
    if (isFatigue) {
        document.querySelector('#grp-fos-str label').textContent = "Ultimate Tensile Strength (S_ut):";
        document.querySelector('#grp-fos-work label').textContent = "Mean Static Stress (\u03C3_m):";
    } else if (mode === 'ultimate') {
        document.querySelector('#grp-fos-str label').textContent = "Ultimate Tensile Strength (S_ut):";
        document.querySelector('#grp-fos-work label').textContent = "Working Peak Stress (\u03C3_work):";
    } else {
        document.querySelector('#grp-fos-str label').textContent = "Material Yield Strength (S_y):";
        document.querySelector('#grp-fos-work label').textContent = "Applied Working Stress (\u03C3_work):";
    }
}

function computeFos() {
    var mode = document.getElementById('fos-mode').value;
    var sVal = parseFloat(document.getElementById('fos-strength').value);
    var sUnit = parseFloat(document.getElementById('fos-str-unit').value);
    var wVal = parseFloat(document.getElementById('fos-working').value);
    var wUnit = parseFloat(document.getElementById('fos-work-unit').value);

    if (isNaN(sVal) || sVal <= 0 || isNaN(wVal) || wVal <= 0) return;

    var S = sVal * sUnit; // MPa
    var sigma_w = wVal * wUnit; // MPa
    var fos = 0;

    if (mode === 'fatigue') {
        var saVal = parseFloat(document.getElementById('fos-sigma-a').value);
        var saUnit = parseFloat(document.getElementById('fos-sigma-a-unit').value);
        var seVal = parseFloat(document.getElementById('fos-se').value);
        var seUnit = parseFloat(document.getElementById('fos-se-unit').value);

        var sigma_a = (isNaN(saVal) || saVal < 0) ? 0 : saVal * saUnit;
        var Se = (isNaN(seVal) || seVal <= 0) ? 100 : seVal * seUnit;

        // Modified Goodman: (sigma_a / Se) + (sigma_m / Sut) = 1 / FoS
        var goodmanSum = (sigma_a / Se) + (sigma_w / S);
        if (goodmanSum <= 0) return;
        fos = 1.0 / goodmanSum;
    } else {
        // Static Yield or Ultimate
        fos = S / sigma_w;
    }

    var mos = fos - 1.0;
    var util = (1.0 / fos) * 100.0;

    document.getElementById('res-fos-val').textContent = fos.toFixed(3);

    var mosStr = (mos >= 0 ? "+" : "") + mos.toFixed(3) + " (" + (mos >= 0 ? "+" : "") + (mos * 100).toFixed(1) + "%)";
    document.getElementById('res-fos-mos').textContent = mosStr;

    var statusEl = document.getElementById('res-fos-status');
    if (fos >= 1.5) {
        statusEl.textContent = "SAFE & ADEQUATE (FoS \u2265 1.5)";
        statusEl.style.color = "#16a34a";
    } else if (fos >= 1.0) {
        statusEl.textContent = "MARGINAL (1.0 \u2264 FoS < 1.5) - Verify Standards";
        statusEl.style.color = "#d97706";
    } else {
        statusEl.textContent = "CRITICAL: STRUCTURAL FAILURE PREDICTED (FoS < 1.0)";
        statusEl.style.color = "#dc2626";
    }

    document.getElementById('res-fos-util').textContent = util.toFixed(1) + "%";

    // Industry benchmark
    var benchEl = document.getElementById('res-fos-benchmark');
    if (fos >= 8.0) {
        benchEl.textContent = "Elevators & Overhead Rigging (8.0 \u2013 12.0)";
    } else if (fos >= 3.5) {
        benchEl.textContent = "ASME Boiler & Pressure Vessels (3.5 \u2013 4.0)";
    } else if (fos >= 2.0) {
        benchEl.textContent = "General Machinery & Heavy Equipment (2.0 \u2013 2.5)";
    } else if (fos >= 1.5) {
        benchEl.textContent = "AISC Structural & Civil Building Frame (1.67 \u2013 2.0)";
    } else if (fos >= 1.25) {
        benchEl.textContent = "Aerospace & Mass-Critical Structures (1.25 \u2013 1.5)";
    } else {
        benchEl.textContent = "Below Standard Engineering Minimums (< 1.25)";
    }
}

document.getElementById('fos-mode').addEventListener('change', function() {
    updateFosMode();
    computeFos();
});
document.getElementById('calc-fos-btn').addEventListener('click', computeFos);
['fos-strength', 'fos-str-unit', 'fos-working', 'fos-work-unit', 'fos-sigma-a', 'fos-sigma-a-unit', 'fos-se', 'fos-se-unit'].forEach(function(id) {
    document.getElementById(id).addEventListener('input', computeFos);
    document.getElementById(id).addEventListener('change', computeFos);
});
window.addEventListener('DOMContentLoaded', function() {
    updateFosMode();
    computeFos();
});
"""

TOOL2_ARTICLE = r"""
<h2>Foundations of Structural Reliability and Safety Margins in Mechanical Design</h2>
<p>In mechanical, structural, and aerospace engineering, physical structures are subjected to variable operational loads, environmental degradation, geometric manufacturing tolerances, and intrinsic material microscopic variances. The <strong>Factor of Safety ($\text{FoS}$)</strong>, frequently denoted as $N$ or $\text{SF}$, is the dimensionless ratio of a structural component's ultimate capacity or material resistance limit to the maximum anticipated working load or operational stress.</p>

<p>A properly evaluated Factor of Safety ensures that unexpected load surges, stress concentrations, dynamic vibration shocks, or minor metallurgical inclusions do not induce catastrophic rupture or permanent plastic deformation during the intended design service life. The fundamental mathematical expression is formulated as:</p>
$$\text{FoS} = \frac{\text{Failure Criterion Material Capacity}}{\text{Operational Working Stress}} = \frac{S_{\text{material}}}{\sigma_{\text{working}}}$$

<h2>Factor of Safety ($\text{FoS}$) vs Margin of Safety ($\text{MoS}$)</h2>
<p>While consumer engineering frequently references Factor of Safety, aerospace organizations (NASA, ESA, FAA, DoD) mandate the use of the <strong>Margin of Safety ($\text{MoS}$ or $\text{MS}$)</strong> to quantify excess load-bearing capacity above regulatory certification requirements:</p>
$$\text{MoS} = \frac{\text{Allowable Load / Stress}}{(\text{Design Load / Stress}) \times \text{FoS}_{\text{required}}} - 1 = \frac{\text{FoS}_{\text{actual}}}{\text{FoS}_{\text{required}}} - 1$$

<p>When the required factor of safety is standardized to unity ($\text{FoS}_{\text{req}} = 1.0$), the definition simplifies directly to:</p>
$$\text{MoS} = \text{FoS}_{\text{actual}} - 1$$

<p>The interpretation of Margin of Safety values across formal structural validation audits follows rigid criteria:</p>
<ul>
    <li><strong>$\text{MoS} > 0$ (Positive Margin):</strong> The structure possesses adequate excess strength. For example, an $\text{MoS} = +0.25$ indicates the component can carry $25\%$ more load than its regulatory maximum design limit.</li>
    <li><strong>$\text{MoS} = 0.0$ (Zero Margin):</strong> The component is operating exactly at its ultimate structural boundary. While theoretically compliant, zero margin offers zero tolerance for manufacturing anomalies.</li>
    <li><strong>$\text{MoS} < 0$ (Negative Margin):</strong> The structure is non-compliant, unsafe, and will experience yield deformation or catastrophic rupture under design conditions.</li>
</ul>

<h2>Failure Theories: Ductile vs Brittle Material Criteria</h2>
<p>Selecting the appropriate material strength parameter ($S_{\text{material}}$) depends on material ductility, crystalline microstructure, and operational failure mode:</p>

<h3>1. Ductile Materials (Elongation $\ge 5\%$): Static Yield Criterion ($S_y$)</h3>
<p>For ductile metals (mild structural steel, austenitic stainless steel, 6061-T6 aluminum, titanium alloys), failure is defined as the onset of irreversible plastic yielding. Designers evaluate safety against the material's <strong>Yield Strength ($S_y$)</strong> using multi-axial stress invariants:</p>
$$\text{FoS}_{\text{yield}} = \frac{S_y}{\sigma_{\text{von Mises}}}$$

<p>Where $\sigma_{\text{von Mises}}$ is the equivalent distortional energy stress combining triaxial principle stresses ($\sigma_1, \sigma_2, \sigma_3$):</p>
$$\sigma_{\text{von Mises}} = \sqrt{\frac{1}{2} [(\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2]}$$

<h3>2. Brittle Materials (Elongation $< 5\%$): Ultimate Strength ($S_{ut}$)</h3>
<p>Brittle materials (gray cast iron, structural ceramics, unreinforced concrete, tooling steels) do not yield plastically; instead, microcracks propagate catastrophically into cleavage fracture. For brittle elements, safety is calculated against <strong>Ultimate Tensile Strength ($S_{ut}$)</strong> or Ultimate Compressive Strength ($S_{uc}$) using the Maximum Normal Stress Theory (Rankine) or Modified Mohr criteria:</p>
$$\text{FoS}_{\text{ultimate}} = \frac{S_{ut}}{\sigma_1} \quad (\text{where } \sigma_1 \text{ is maximum principal tensile stress})$$

<h2>Cyclic Fatigue Failure: Modified Goodman and Soderberg Criteria</h2>
<p>Over $80\%$ of all real-world mechanical machine failures occur due to progressive cyclic fatigue at stress levels far below static yield strength. Fluctuating loads exhibit an alternating stress amplitude ($\sigma_a$) superimposed onto a non-zero mean static stress ($\sigma_m$):</p>
$$\sigma_a = \frac{\sigma_{\text{max}} - \sigma_{\text{min}}}{2}, \qquad \sigma_m = \frac{\sigma_{\text{max}} + \sigma_{\text{min}}}{2}$$

<p>The <strong>Modified Goodman Criterion</strong> provides the most reliable conservative estimate for infinite fatigue life across ductile engineering alloys:</p>
$$\frac{\sigma_a}{S_e} + \frac{\sigma_m}{S_{ut}} = \frac{1}{\text{FoS}}$$

<p>Where $S_e$ is the endurance limit (fatigue limit) of the material modified by Marin surface finish, size, and reliability factors. The stricter <strong>Soderberg Criterion</strong> substitutes yield strength $S_y$ for ultimate strength $S_{ut}$ to eliminate any local yielding under peak cycles:</p>
$$\frac{\sigma_a}{S_e} + \frac{\sigma_m}{S_y} = \frac{1}{\text{FoS}_{\text{Soderberg}}}$$

<table class="data-table">
    <thead>
        <tr>
            <th>Engineering Industry / Sector</th>
            <th>Governing Standard</th>
            <th>Typical Factor of Safety ($\text{FoS}$)</th>
            <th>Primary Engineering Rationale</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Aerospace Airframes &amp; Spacecraft</strong></td>
            <td>FAA FAR 25 / NASA-STD-5001</td>
            <td>$1.25\text{--}1.50$ (Yield: 1.1; Ult: 1.5)</td>
            <td>Extreme mass sensitivity; rigorous non-destructive inspection</td>
        </tr>
        <tr>
            <td><strong>Civil Structural Building Steel</strong></td>
            <td>AISC 360 / Eurocode 3</td>
            <td>$1.67\text{--}2.00$</td>
            <td>Wind gusts, live occupancy variances, seismic dampening</td>
        </tr>
        <tr>
            <td><strong>Automotive Powertrain &amp; Chassis</strong></td>
            <td>SAE J429 / ISO 26262</td>
            <td>$1.50\text{--}2.50$</td>
            <td>Road surface shock impacts, fatigue life over 150k miles</td>
        </tr>
        <tr>
            <td><strong>Pressure Vessels &amp; Boilers</strong></td>
            <td>ASME Section VIII Div 1</td>
            <td>$3.50\text{--}4.00$</td>
            <td>Lethal pneumatic/steam expansion hazards, corrosion thinning</td>
        </tr>
        <tr>
            <td><strong>Passenger Elevators &amp; Hoists</strong></td>
            <td>ASME A17.1 / EN 81</td>
            <td>$8.00\text{--}12.00$</td>
            <td>Direct life-safety critical cable bending fatigue and sudden stops</td>
        </tr>
    </tbody>
</table>

<div class="worked-example-card">
    <h4>Step-by-Step Engineering Case Study: Hydraulic Excavator Pin Sizing</h4>
    <p><strong>Scenario:</strong> A main boom joint on a hydraulic excavator utilizes a solid cylindrical pivot pin fabricated from quenched and tempered 4140 alloy steel ($S_y = 655\ \text{MPa}$, $S_{ut} = 850\ \text{MPa}$). Peak operating loads generate a maximum calculated von Mises bending plus shear stress of $\sigma_{\text{work}} = 260\ \text{MPa}$. The mining equipment design specification mandates a minimum Factor of Safety of $\text{FoS}_{\text{req}} = 2.0$.</p>
    <div class="step-solution">
        <p><strong>Step 1: Calculate Actual Factor of Safety against Yield ($\text{FoS}_{\text{actual}}$):</strong></p>
        $$\text{FoS}_{\text{actual}} = \frac{S_y}{\sigma_{\text{work}}} = \frac{655\ \text{MPa}}{260\ \text{MPa}} = 2.519$$
        <p><strong>Step 2: Calculate Margin of Safety ($\text{MoS}$) relative to Requirement:</strong></p>
        $$\text{MoS} = \frac{\text{FoS}_{\text{actual}}}{\text{FoS}_{\text{req}}} - 1 = \frac{2.519}{2.00} - 1 = 1.2595 - 1 = +0.2595\ (+26.0\%)$$
        <p><strong>Step 3: Evaluate Cyclic Fatigue under Fluctuating Load:</strong></p>
        <p>If cyclic digging loads induce alternating stress $\sigma_a = 90\ \text{MPa}$ with mean stress $\sigma_m = 170\ \text{MPa}$, and pin polished endurance limit is $S_e = 310\ \text{MPa}$:</p>
        $$\frac{1}{\text{FoS}_{\text{fatigue}}} = \frac{\sigma_a}{S_e} + \frac{\sigma_m}{S_{ut}} = \frac{90\ \text{MPa}}{310\ \text{MPa}} + \frac{170\ \text{MPa}}{850\ \text{MPa}} = 0.2903 + 0.2000 = 0.4903$$
        $$\text{FoS}_{\text{fatigue}} = \frac{1}{0.4903} = 2.039$$
        <p><strong>Conclusion:</strong> The design achieves a static $\text{FoS} = 2.52$ ($\text{MoS} = +26\%$) and a cyclic fatigue $\text{FoS} = 2.04$, comfortably satisfying the client requirement of $2.0$ across all operational states.</p>
    </div>
</div>

<h2>Frequently Asked Questions (FAQ)</h2>
<div class="faq-section">
    <h3>What is the difference between Factor of Safety ($\text{FoS}$) and Margin of Safety ($\text{MoS}$)?</h3>
    <p>Factor of Safety is the ratio of structural capacity (yield or ultimate strength) to applied operational stress: $\text{FoS} = S_{\text{material}} / \sigma_{\text{working}}$. Margin of Safety is defined as $\text{MoS} = \text{FoS} - 1 = (S_{\text{material}} / \sigma_{\text{working}}) - 1$. An $\text{MoS} > 0$ indicates structural adequacy, $\text{MoS} = 0$ represents boundary capacity, and $\text{MoS} < 0$ denotes failure.</p>

    <h3>Should Factor of Safety be based on Yield Strength or Ultimate Tensile Strength?</h3>
    <p>For ductile materials (structural steel, aluminum alloys) in machines and buildings, $\text{FoS}$ is universally based on Yield Strength ($S_y$) to prevent permanent plastic deformation. For brittle materials (cast iron, ceramics, concrete) or catastrophic containment vessels, $\text{FoS}$ is calculated against Ultimate Tensile Strength ($S_{ut}$) using higher safety margins.</p>

    <h3>What is the modified Goodman relation for fatigue loading?</h3>
    <p>Under fluctuating cyclic loading with alternating stress $\sigma_a$ and mean tensile stress $\sigma_m$, the modified Goodman criterion determines safety against fatigue failure: $\frac{\sigma_a}{S_e} + \frac{\sigma_m}{S_{ut}} = \frac{1}{\text{FoS}}$, where $S_e$ is the endurance limit and $S_{ut}$ is the ultimate tensile strength.</p>

    <h3>What are typical engineering Factor of Safety values across industries?</h3>
    <p>Aerospace: $1.25$ to $1.50$ (mass critical); Automotive: $1.5$ to $2.5$; Civil structural steel (AISC): $1.67$ to $2.0$; Boilers and pressure vessels (ASME Section VIII): $3.5$ to $4.0$; Elevators and wire ropes: $8.0$ to $12.0$.</p>
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
    generate_tool(TOOL1_SLUG, TOOL1_TITLE, TOOL1_DESC, TOOL1_H1, TOOL1_SHORT, TOOL1_SCHEMA, TOOL1_UI, TOOL1_JS, TOOL1_ARTICLE)
    generate_tool(TOOL2_SLUG, TOOL2_TITLE, TOOL2_DESC, TOOL2_H1, TOOL2_SHORT, TOOL2_SCHEMA, TOOL2_UI, TOOL2_JS, TOOL2_ARTICLE)
