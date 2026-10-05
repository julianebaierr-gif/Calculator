# -*- coding: utf-8 -*-
"""
Generator for Batch 36 - Part 4
Tools:
7. lumen-method-calculator.html
8. motor-parameters-calculator.html
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
                        <li><a href="lumen-method-calculator.html">Lumen Method Fixture Layout</a></li>
                        <li><a href="motor-parameters-calculator.html">Motor Parameters &amp; Slip</a></li>
                        <li><a href="lumen-lux-calculator.html">Lumen to Lux Illuminance</a></li>
                        <li><a href="motor-starting-current-calculator.html">Motor Starting Current</a></li>
                        <li><a href="power-factor-calculator.html">Power Factor Correction</a></li>
                        <li><a href="three-phase-power-calculator.html">Three-Phase AC Power</a></li>
                        <li><a href="cable-sizing-calculator.html">Cable Sizing (IEC/NEC)</a></li>
                        <li><a href="wire-ampacity-calculator.html">Wire Ampacity Sizing</a></li>
                        <li><a href="conduit-fill-calculator.html">Conduit Fill Sizing</a></li>
                        <li><a href="torque-calculator.html">Torque &amp; Shaft Power</a></li>
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
                    <p>CalcHub provides free, engineering-grade calculators, physics simulation utilities, and architectural layout models verified against IESNA, NEMA, and IEC standards.</p>
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
                        <li><a href="lumen-method-calculator.html">IESNA Zonal Cavity</a></li>
                        <li><a href="motor-parameters-calculator.html">AC Induction Motor Slip</a></li>
                        <li><a href="three-phase-power-calculator.html">Three-Phase Power</a></li>
                        <li><a href="motor-starting-current-calculator.html">Motor Inrush Amps</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 CalcHub. All rights reserved. Precision computational tools for facility engineers, electricians, and MEP designers.</p>
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
# TOOL 7: lumen-method-calculator.html
# ==============================================================================
TOOL7_SLUG = "lumen-method-calculator"
TOOL7_TITLE = "Lumen Method Calculator - IESNA Zonal Cavity Lighting Fixture Layout"
TOOL7_DESC = "Calculate required lighting luminaires using the IESNA Zonal Cavity Lumen Method. Compute Room Cavity Ratio (RCR), fixture spacing, and grid layout."
TOOL7_H1 = "Lumen Method Lighting Calculator (Zonal Cavity)"
TOOL7_SHORT = "Determine required luminaire fixture count, Room Cavity Ratio (RCR), spacing-to-mounting height ratios, and grid layout based on IESNA standards."

TOOL7_SCHEMA = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Lumen Method Lighting Calculator",
      "url": "https://calchub.com/lumen-method-calculator.html",
      "description": "Calculates required number of lighting fixtures, Room Cavity Ratio, total lumens, and grid spacing using the IESNA Zonal Cavity Lumen Method.",
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
          "name": "What is the Lumen Method in architectural lighting design?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The Lumen Method (or Zonal Cavity Method) is the standard IESNA mathematical procedure used to calculate the number of luminaires required to achieve a uniform target illuminance (Lux or Foot-Candles) across a designated horizontal workplane: N = (E * A) / (n * Lumens * CU * LLF)."
          }
        },
        {
          "@type": "Question",
          "name": "How is the Room Cavity Ratio (RCR) calculated?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "RCR measures room geometry proportion relative to lighting mounting height: RCR = (5 * h_rc * (L + W)) / (L * W), where h_rc is the cavity height between the luminaire mounting plane and the task workplane (typically 0.75 m to 0.85 m above the finished floor)."
          }
        },
        {
          "@type": "Question",
          "name": "What is the Coefficient of Utilization (CU)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "CU is the fraction of total initial lamp lumens that successfully reaches the workplane, accounting for room geometry (RCR) and inter-reflections off ceiling, wall, and floor surfaces (typical values range from 0.40 to 0.85)."
          }
        },
        {
          "@type": "Question",
          "name": "What factors comprise the Light Loss Factor (LLF)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "LLF (or Maintenance Factor MF) accounts for real-world environmental degradation over time: LLF = LLD (Lamp Lumen Depreciation) * LDD (Luminaire Dirt Depreciation) * BF (Ballast Factor) * RSDD (Room Surface Dirt Depreciation). Typical clean office values range from 0.75 to 0.85."
          }
        }
      ]
    }
  ]
}"""

TOOL7_UI = """
<div class="calc-grid">
    <div class="calc-input-group">
        <label for="lm-length">Room Length ($L$):</label>
        <div class="input-with-select">
            <input type="number" id="lm-length" value="12" min="1" step="any">
            <select id="lm-len-unit">
                <option value="1" selected>Meters (m)</option>
                <option value="0.3048">Feet (ft)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="lm-width">Room Width ($W$):</label>
        <div class="input-with-select">
            <input type="number" id="lm-width" value="8" min="1" step="any">
            <select id="lm-wid-unit">
                <option value="1" selected>Meters (m)</option>
                <option value="0.3048">Feet (ft)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="lm-ceil-h">Ceiling Mounting Height ($H$):</label>
        <div class="input-with-select">
            <input type="number" id="lm-ceil-h" value="3.0" min="1.5" step="any">
            <select id="lm-ceil-unit">
                <option value="1" selected>Meters (m)</option>
                <option value="0.3048">Feet (ft)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="lm-work-h">Workplane Height ($h_w$, standard desk: 0.75m / 2.5ft):</label>
        <div class="input-with-select">
            <input type="number" id="lm-work-h" value="0.75" min="0" step="any">
            <select id="lm-work-unit">
                <option value="1" selected>Meters (m)</option>
                <option value="0.3048">Feet (ft)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="lm-target-lux">Target Maintained Illuminance ($E$):</label>
        <div class="input-with-select">
            <input type="number" id="lm-target-lux" value="500" min="10" step="any">
            <select id="lm-target-unit">
                <option value="1" selected>Lux (lx)</option>
                <option value="10.7639">Foot-Candles (fc)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="lm-lumens-fix">Lumens per Fixture ($\Phi_{\text{luminaire}}$):</label>
        <div class="input-with-select">
            <input type="number" id="lm-lumens-fix" value="4000" min="100" step="any">
            <select id="lm-lumens-unit">
                <option value="1" selected>Lumens (lm)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="lm-cu">Coefficient of Utilization ($\text{CU}$):</label>
        <input type="number" id="lm-cu" value="0.65" min="0.1" max="1.0" step="0.05">
    </div>
    <div class="calc-input-group">
        <label for="lm-llf">Light Loss Factor ($\text{LLF} / \text{MF}$):</label>
        <input type="number" id="lm-llf" value="0.80" min="0.3" max="1.0" step="0.05">
    </div>
</div>
<button id="calc-lm-btn" class="calc-btn">Calculate Luminaire Layout</button>
<div class="calc-results-card" id="lm-results">
    <h3>Zonal Cavity Layout &amp; Fixture Grid</h3>
    <div class="result-row highlight-result">
        <span class="result-label">Required Number of Fixtures ($N$):</span>
        <span class="result-val" id="res-lm-n">23.07 &rarr; Round to 24 Fixtures</span>
    </div>
    <div class="result-row">
        <span class="result-label">Recommended Grid Configuration:</span>
        <span class="result-val" id="res-lm-grid">6 Rows &times; 4 Columns (24 Fixtures)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Room Cavity Ratio ($\text{RCR}$):</span>
        <span class="result-val" id="res-lm-rcr">2.34</span>
    </div>
    <div class="result-row">
        <span class="result-label">Total Floor Area ($A$):</span>
        <span class="result-val" id="res-lm-area">96.0 m&sup2; (1,033.3 sq ft)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Achieved Maintained Illuminance ($E_{\text{actual}}$):</span>
        <span class="result-val" id="res-lm-actual-lux">520.0 Lux (48.3 fc)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Longitudinal Fixture Spacing ($S_L$):</span>
        <span class="result-val" id="res-lm-spacing-l">2.00 m (Ratio to Cavity: 0.89 &le; 1.2 OK)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Transverse Fixture Spacing ($S_W$):</span>
        <span class="result-val" id="res-lm-spacing-w">2.00 m (Ratio to Cavity: 0.89 &le; 1.2 OK)</span>
    </div>
</div>
"""

TOOL7_JS = """
function computeLumenMethod() {
    var lVal = parseFloat(document.getElementById('lm-length').value);
    var lUnit = parseFloat(document.getElementById('lm-len-unit').value);
    var wVal = parseFloat(document.getElementById('lm-width').value);
    var wUnit = parseFloat(document.getElementById('lm-wid-unit').value);
    var hCeilVal = parseFloat(document.getElementById('lm-ceil-h').value);
    var hCeilUnit = parseFloat(document.getElementById('lm-ceil-unit').value);
    var hWorkVal = parseFloat(document.getElementById('lm-work-h').value);
    var hWorkUnit = parseFloat(document.getElementById('lm-work-unit').value);
    var eVal = parseFloat(document.getElementById('lm-target-lux').value);
    var eUnit = parseFloat(document.getElementById('lm-target-unit').value);
    var lumens = parseFloat(document.getElementById('lm-lumens-fix').value);
    var cu = parseFloat(document.getElementById('lm-cu').value);
    var llf = parseFloat(document.getElementById('lm-llf').value);

    if (isNaN(lVal) || lVal <= 0 || isNaN(wVal) || wVal <= 0 || isNaN(hCeilVal) || hCeilVal <= 0 || isNaN(lumens) || lumens <= 0 || isNaN(cu) || cu <= 0 || isNaN(llf) || llf <= 0) return;

    var L = lVal * lUnit; // meters
    var W = wVal * wUnit; // meters
    var H = hCeilVal * hCeilUnit; // meters
    var Hw = (isNaN(hWorkVal) || hWorkVal < 0) ? 0.75 : hWorkVal * hWorkUnit; // meters
    var E = eVal * eUnit; // Lux

    var area_m2 = L * W;
    var area_sqft = area_m2 * 10.7639104;

    // Room cavity height h_rc = H - Hw
    var h_rc = Math.max(0.5, H - Hw);

    // RCR = 5 * h_rc * (L + W) / (L * W)
    var rcr = (5.0 * h_rc * (L + W)) / area_m2;

    // N_exact = (E * Area) / (lumens * CU * LLF)
    var denom = lumens * cu * llf;
    if (denom <= 0) return;
    var N_exact = (E * area_m2) / denom;

    // Grid layout heuristic
    // Aspect ratio = L / W
    // N = N_rows * N_cols, N_rows / N_cols approx L / W
    var aspect = L / W;
    var N_round = Math.ceil(N_exact);

    // Find best integer rows and cols
    var bestRows = Math.round(Math.sqrt(N_round * aspect));
    bestRows = Math.max(1, bestRows);
    var bestCols = Math.ceil(N_round / bestRows);
    var totalFixtures = bestRows * bestCols;

    // Recalculate actual maintained lux
    var actualLux = (totalFixtures * lumens * cu * llf) / area_m2;
    var actualFc = actualLux / 10.7639104;

    // Spacings
    var s_L = L / bestRows;
    var s_W = W / bestCols;
    var ratio_L = s_L / h_rc;
    var ratio_W = s_W / h_rc;

    document.getElementById('res-lm-n').textContent = N_exact.toFixed(2) + " \u2192 Round to " + totalFixtures + " Fixtures";
    document.getElementById('res-lm-grid').textContent = bestRows + " Rows (length) \u00D7 " + bestCols + " Columns (width) = " + totalFixtures + " Units";
    document.getElementById('res-lm-rcr').textContent = rcr.toFixed(2);
    document.getElementById('res-lm-area').textContent = area_m2.toFixed(1) + " m\u00B2 (" + area_sqft.toFixed(1) + " sq ft)";
    document.getElementById('res-lm-actual-lux').textContent = actualLux.toFixed(1) + " Lux (" + actualFc.toFixed(1) + " fc)";

    var okStr_L = (ratio_L <= 1.5) ? "OK (\u2264 1.5)" : "Caution: > 1.5 Spacing";
    var okStr_W = (ratio_W <= 1.5) ? "OK (\u2264 1.5)" : "Caution: > 1.5 Spacing";
    document.getElementById('res-lm-spacing-l').textContent = s_L.toFixed(2) + " m (S/MH = " + ratio_L.toFixed(2) + " " + okStr_L + ")";
    document.getElementById('res-lm-spacing-w').textContent = s_W.toFixed(2) + " m (S/MH = " + ratio_W.toFixed(2) + " " + okStr_W + ")";
}

document.getElementById('calc-lm-btn').addEventListener('click', computeLumenMethod);
['lm-length', 'lm-len-unit', 'lm-width', 'lm-wid-unit', 'lm-ceil-h', 'lm-ceil-unit', 'lm-work-h', 'lm-work-unit', 'lm-target-lux', 'lm-target-unit', 'lm-lumens-fix', 'lm-cu', 'lm-llf'].forEach(function(id) {
    document.getElementById(id).addEventListener('input', computeLumenMethod);
    document.getElementById(id).addEventListener('change', computeLumenMethod);
});
window.addEventListener('DOMContentLoaded', computeLumenMethod);
"""

TOOL7_ARTICLE = r"""
<h2>Theoretical Foundations of the IESNA Zonal Cavity (Lumen) Method</h2>
<p>The Lumen Method—formally designated as the <strong>Zonal Cavity Method</strong> by the Illuminating Engineering Society of North America (IESNA)—is the standard mathematical procedure utilized by electrical consulting engineers and lighting architects to determine the quantity and spatial placement of luminaires required to achieve uniform, maintained horizontal illuminance across an architectural space.</p>

<p>Rather than relying on isolated point-by-point ray tracing, the Lumen Method operates by partitioning an enclosed interior architectural room into three distinct virtual horizontal cavities:</p>
<ul>
    <li><strong>Ceiling Cavity ($h_{cc}$):</strong> The spatial volume located between the physical ceiling surface and the plane of suspended luminaire light centers (for recessed troffers or surface-mounted luminaires, $h_{cc} = 0$).</li>
    <li><strong>Room Cavity ($h_{rc}$):</strong> The vital working space located between the luminaire mounting plane and the horizontal task workplane.</li>
    <li><strong>Floor Cavity ($h_{fc}$):</strong> The volume situated below the task workplane down to the finished floor (typically standard desk height $h_{fc} = 0.75\text{--}0.85\ \text{meters}$ or $2.5\text{--}2.8\ \text{feet}$).</li>
</ul>

<h2>The Master Zonal Cavity Equation</h2>
<p>The fundamental equation of the Lumen Method balances the rate of total light flux delivered onto the task plane against spatial room absorption and long-term environmental degradation:</p>
$$E = \frac{N \cdot n \cdot \Phi_{\text{lamp}} \cdot \text{CU} \cdot \text{LLF}}{A}$$

<p>Rearranging to solve for the required total quantity of luminaires ($N$):</p>
$$N = \frac{E \cdot A}{n \cdot \Phi_{\text{lamp}} \cdot \text{CU} \cdot \text{LLF}}$$

<p>Where:</p>
<ul>
    <li><strong>$N$</strong>: Total number of luminaire fixtures required.</li>
    <li><strong>$E$</strong>: Target maintained horizontal illuminance on the task plane (in Lux, where $1\text{ lx} = 1\text{ lm/m}^2$, or Foot-Candles, where $1\text{ fc} = 10.764\text{ lx}$).</li>
    <li><strong>$A$</strong>: Total floor area of the interior space ($A = L \times W$ in $\text{m}^2$).</li>
    <li><strong>$n$</strong>: Number of individual lamps or LED light engines per luminaire fixture.</li>
    <li><strong>$\Phi_{\text{lamp}}$</strong>: Initial rated luminous flux emitted per lamp or LED module in Lumens ($\text{lm}$).</li>
    <li><strong>$\text{CU}$</strong>: <strong>Coefficient of Utilization</strong>, representing the percentage of initial luminaire lumens that successfully reach the workplane.</li>
    <li><strong>$\text{LLF}$</strong>: <strong>Light Loss Factor</strong> (also termed Maintenance Factor, $\text{MF}$), accounting for long-term luminous degradation.</li>
</ul>

<h2>Room Cavity Ratio (RCR) and Geometry Modeling</h2>
<p>The proportion of light that strikes the task surface versus being absorbed by surrounding walls depends directly on room geometry. The dimensionless <strong>Room Cavity Ratio ($\text{RCR}$)</strong> characterizes this volumetric relationship:</p>
$$\text{RCR} = \frac{5 \cdot h_{rc} \cdot (L + W)}{L \cdot W} = \frac{2.5 \cdot \text{Perimeter} \cdot h_{rc}}{\text{Area}}$$

<p>Where $h_{rc} = H_{\text{ceiling}} - h_{\text{workplane}} - h_{\text{suspension}}$ is the net room cavity height. Low, broad rooms (e.g., large open-plan trading floors or big-box stores) have low RCR values ($1\text{--}2$), maximizing wall inter-reflections and yielding high CU values ($0.70\text{--}0.85$). Conversely, tall, narrow corridors have high RCR values ($6\text{--}10$), causing substantial wall absorption and reducing CU ($0.30\text{--}0.45$).</p>

<h2>Deconstructing the Light Loss Factor ($\text{LLF}$)</h2>
<p>A lighting system designed solely around initial clean-room output will inevitably fail to deliver code-mandated illuminance as equipment ages. The total Light Loss Factor is the multiplicative product of recoverable and non-recoverable depreciation parameters:</p>
$$\text{LLF} = \text{LLD} \cdot \text{LDD} \cdot \text{BF} \cdot \text{RSDD}$$

<table class="data-table">
    <thead>
        <tr>
            <th>Depreciation Factor</th>
            <th>Acronym</th>
            <th>Typical Modern LED Range</th>
            <th>Physical Mechanism</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Lamp Lumen Depreciation</strong></td>
            <td>$\text{LLD}$</td>
            <td>$0.85\text{--}0.92$ (L80 / L90 ratings)</td>
            <td>Phosphor degradation and semiconductor junction thermal decay</td>
        </tr>
        <tr>
            <td><strong>Luminaire Dirt Depreciation</strong></td>
            <td>$\text{LDD}$</td>
            <td>$0.85\text{--}0.95$ (Clean office / dry)</td>
            <td>Airborne dust accumulation on lenses, diffusers, and louvers</td>
        </tr>
        <tr>
            <td><strong>Ballast / Driver Factor</strong></td>
            <td>$\text{BF}$</td>
            <td>$0.95\text{--}1.00$</td>
            <td>Electronic LED driver efficiency relative to standard bench rating</td>
        </tr>
        <tr>
            <td><strong>Room Surface Dirt Depreciation</strong></td>
            <td>$\text{RSDD}$</td>
            <td>$0.90\text{--}0.98$</td>
            <td>Gradual darkening of wall paint, acoustic ceiling tiles, and carpet</td>
        </tr>
    </tbody>
</table>

<h2>Spacing-to-Mounting Height Ratio ($S/MH$) and Grid Uniformity</h2>
<p>To prevent alternating dark shadows and intense bright spots, luminaires must be laid out in a symmetrical rectangular grid satisfying the manufacturer's photometric <strong>Spacing Criterion ($SC$ or $S/MH$)</strong>:</p>
$$\frac{S}{h_{rc}} \le SC_{\text{rated}} \quad (\text{Typically } 1.20\text{ to } 1.50)$$

<p>Where $S$ is the center-to-center distance between adjacent luminaires. To maintain uniform illuminance along room perimeters, the distance from the outer fixture row to the adjacent wall should equal half the internal spacing: $S_{\text{wall}} \approx \frac{1}{2} S$.</p>

<div class="worked-example-card">
    <h4>Step-by-Step Engineering Case Study: Corporate Open-Plan Office Lighting</h4>
    <p><strong>Scenario:</strong> Design a recessed LED troffer layout for an engineering consulting office measuring $L = 18.0\ \text{m}$ by $W = 12.0\ \text{m}$ with a finished ceiling height of $H = 2.85\ \text{m}$. Standard desk workplane height is $h_w = 0.75\ \text{m}$. Target maintained illuminance per IESNA standards is $E = 500\ \text{Lux}$. High-efficiency $2\times 2\ \text{ft}$ LED panel fixtures rated at $\Phi = 4,200\ \text{lumens}$ each are selected. Manufacturer photometric data indicates $\text{CU} = 0.68$ for this space, and clean-office maintenance factor is $\text{LLF} = 0.82$.</p>
    <div class="step-solution">
        <p><strong>Step 1: Calculate Room Cavity Height ($h_{rc}$) and RCR:</strong></p>
        $$h_{rc} = 2.85\ \text{m} - 0.75\ \text{m} = 2.10\ \text{meters}$$
        $$\text{Area} = 18.0 \times 12.0 = 216.0\ \text{m}^2$$
        $$\text{RCR} = \frac{5 \times 2.10 \times (18.0 + 12.0)}{216.0} = \frac{10.5 \times 30.0}{216.0} = \frac{315.0}{216.0} = 1.458$$
        <p><strong>Step 2: Calculate Exact Required Number of Fixtures ($N$):</strong></p>
        $$N = \frac{E \cdot A}{\Phi \cdot \text{CU} \cdot \text{LLF}} = \frac{500\ \text{lx} \times 216.0\ \text{m}^2}{4200\ \text{lm} \times 0.68 \times 0.82}$$
        $$N = \frac{108,000}{2341.92} = 46.12\ \text{fixtures}$$
        <p><strong>Step 3: Establish Symmetrical Rectangular Grid:</strong></p>
        <p>Room aspect ratio is $\frac{L}{W} = \frac{18}{12} = 1.5$. Selecting a $8 \times 6 = 48\ \text{fixture}$ grid:</p>
        <ul>
            <li>$N_{\text{rows}} = 8$ along the $18\text{ m}$ length ($S_L = \frac{18.0}{8} = 2.25\ \text{m}$).</li>
            <li>$N_{\text{cols}} = 6$ along the $12\text{ m}$ width ($S_W = \frac{12.0}{6} = 2.00\ \text{m}$).</li>
        </ul>
        <p><strong>Step 4: Verify Spacing-to-Mounting Height Ratio:</strong></p>
        $$\frac{S_L}{h_{rc}} = \frac{2.25}{2.10} = 1.071 \le 1.20 \quad (\text{Compliant!})$$
        $$\frac{S_W}{h_{rc}} = \frac{2.00}{2.10} = 0.952 \le 1.20 \quad (\text{Compliant!})$$
        <p><strong>Step 5: Verify Actual Maintained Illuminance:</strong></p>
        $$E_{\text{actual}} = \frac{48 \times 2341.92}{216.0} = 520.4\ \text{Lux} \quad (\text{Excellently within } 500\text{--}550\text{ lx target})$$
        <p><strong>Conclusion:</strong> Installing 48 LED troffers arranged in an $8 \times 6$ array provides $520\ \text{Lux}$ of uniform, glare-free task lighting satisfying all IESNA quality and energy criteria.</p>
    </div>
</div>

<h2>Frequently Asked Questions (FAQ)</h2>
<div class="faq-section">
    <h3>What is the Lumen Method in architectural lighting design?</h3>
    <p>The Lumen Method (or Zonal Cavity Method) is the standard IESNA mathematical procedure used to calculate the number of luminaires required to achieve a uniform target illuminance (Lux or Foot-Candles) across a designated horizontal workplane: $N = \frac{E \cdot A}{n \cdot \Phi_{\text{lamp}} \cdot \text{CU} \cdot \text{LLF}}$.</p>

    <h3>How is the Room Cavity Ratio (RCR) calculated?</h3>
    <p>RCR measures room geometry proportion relative to lighting mounting height: $\text{RCR} = \frac{5 \cdot h_{rc} \cdot (L + W)}{L \cdot W}$, where $h_{rc}$ is the cavity height between the luminaire mounting plane and the task workplane (typically $0.75\text{ m}$ to $0.85\text{ m}$ above the finished floor).</p>

    <h3>What is the Coefficient of Utilization (CU)?</h3>
    <p>CU is the fraction of total initial lamp lumens that successfully reaches the workplane, accounting for room geometry (RCR) and inter-reflections off ceiling, wall, and floor surfaces (typical values range from $0.40$ to $0.85$).</p>

    <h3>What factors comprise the Light Loss Factor (LLF)?</h3>
    <p>LLF (or Maintenance Factor MF) accounts for real-world environmental degradation over time: $\text{LLF} = \text{LLD} \times \text{LDD} \times \text{BF} \times \text{RSDD}$, where LLD is Lamp Lumen Depreciation, LDD is Luminaire Dirt Depreciation, BF is Ballast Factor, and RSDD is Room Surface Dirt Depreciation. Typical clean office values range from $0.75$ to $0.85$.</p>
</div>
"""

# ==============================================================================
# TOOL 8: motor-parameters-calculator.html
# ==============================================================================
TOOL8_SLUG = "motor-parameters-calculator"
TOOL8_TITLE = "Motor Parameters Calculator - Slip, Synchronous Speed & Full Load Torque"
TOOL8_DESC = "Calculate induction motor synchronous speed (Ns = 120f/P), percentage rotor slip, full load torque (FLT), input electrical kW, and mechanical shaft power."
TOOL8_H1 = "Induction Motor Parameters &amp; Slip Calculator"
TOOL8_SHORT = "Compute synchronous speed, percentage slip, full load shaft torque, electrical input kW, full-load amps (FLA), and NEMA operating characteristics."

TOOL8_SCHEMA = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Motor Parameters Calculator",
      "url": "https://calchub.com/motor-parameters-calculator.html",
      "description": "Calculates induction motor synchronous speed, rotor slip, full load torque, input power, and full-load current.",
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
          "name": "What is synchronous speed in an AC induction motor?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Synchronous speed (Ns) is the rotational velocity of the stator magnetic field, determined by AC line frequency f and pole count P: Ns = (120 * f) / P RPM. For a 60 Hz system, synchronous speeds are 3600 RPM (2 poles), 1800 RPM (4 poles), and 1200 RPM (6 poles)."
          }
        },
        {
          "@type": "Question",
          "name": "Why must an induction motor have rotor slip?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "An induction motor relies on Faraday's law of induction. If the rotor spun at synchronous speed, there would be zero relative motion between the rotating stator flux and the rotor bars, inducing zero rotor voltage, zero rotor current, and producing zero mechanical torque. Therefore, an induction motor must always operate below synchronous speed: Slip s = (Ns - Nr) / Ns * 100%."
          }
        },
        {
          "@type": "Question",
          "name": "How is full-load torque calculated from shaft power and speed?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Full load torque is calculated as tau = (P_kW * 9548.8) / N_r (in Newton-meters) or tau = (5252 * HP) / N_r (in pound-feet), where N_r is the rated operating rotor speed in RPM."
          }
        },
        {
          "@type": "Question",
          "name": "What is the typical full-load slip for NEMA Design B motors?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Standard NEMA Design B industrial squirrel-cage induction motors operate with full-load slip between 1.5% and 4.0% (e.g., a 4-pole 1800 RPM motor typically runs at 1740 to 1765 RPM under full rated load)."
          }
        }
      ]
    }
  ]
}"""

TOOL8_UI = """
<div class="calc-grid">
    <div class="calc-input-group">
        <label for="mp-power">Rated Shaft Mechanical Power ($P_{\\text{shaft}}$):</label>
        <div class="input-with-select">
            <input type="number" id="mp-power" value="15" min="0.1" step="any">
            <select id="mp-pwr-unit">
                <option value="1" selected>Kilowatts (kW)</option>
                <option value="0.745699872">Horsepower (HP)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="mp-freq">AC Line Frequency ($f$):</label>
        <select id="mp-freq">
            <option value="60" selected>60 Hz (North America, Brazil, KSA)</option>
            <option value="50">50 Hz (Europe, Asia, Australia, Africa)</option>
        </select>
    </div>
    <div class="calc-input-group">
        <label for="mp-poles">Stator Pole Count ($P$):</label>
        <select id="mp-poles">
            <option value="2">2 Poles (3600 / 3000 RPM)</option>
            <option value="4" selected>4 Poles (1800 / 1500 RPM - Standard)</option>
            <option value="6">6 Poles (1200 / 1000 RPM)</option>
            <option value="8">8 Poles (900 / 750 RPM)</option>
            <option value="12">12 Poles (600 / 500 RPM)</option>
        </select>
    </div>
    <div class="calc-input-group">
        <label for="mp-rotor-rpm">Rotor Operating Speed ($N_r$):</label>
        <div class="input-with-select">
            <input type="number" id="mp-rotor-rpm" value="1750" min="1" step="any">
            <select id="mp-rotor-unit">
                <option value="1" selected>RPM (rev/min)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="mp-voltage">Line-to-Line Voltage ($V_{\\text{LL}}$):</label>
        <div class="input-with-select">
            <input type="number" id="mp-voltage" value="460" min="10" step="any">
            <select id="mp-volt-unit">
                <option value="1" selected>Volts (V AC)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="mp-pf">Operating Power Factor ($\cos\\theta$):</label>
        <input type="number" id="mp-pf" value="0.86" min="0.1" max="1.0" step="0.01">
    </div>
    <div class="calc-input-group">
        <label for="mp-eff">Nominal Efficiency ($\eta$):</label>
        <div class="input-with-select">
            <input type="number" id="mp-eff" value="92.4" min="50" max="99" step="0.1">
            <select id="mp-eff-unit">
                <option value="1" selected>% (NEMA Premium / IE3)</option>
            </select>
        </div>
    </div>
</div>
<button id="calc-mp-btn" class="calc-btn">Calculate Motor Characteristics</button>
<div class="calc-results-card" id="mp-results">
    <h3>Electromechanical Operating Characteristics</h3>
    <div class="result-row highlight-result">
        <span class="result-label">Synchronous Speed ($N_s$):</span>
        <span class="result-val" id="res-mp-ns">1,800 RPM (Stator Flux Speed)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Full-Load Rotor Slip ($s$):</span>
        <span class="result-val" id="res-mp-slip">2.78% (50.0 RPM slip speed)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Full-Load Shaft Torque ($\tau$):</span>
        <span class="result-val" id="res-mp-torque">81.85 N&middot;m (60.37 lb-ft)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Electrical Input Power ($P_{\text{in}}$):</span>
        <span class="result-val" id="res-mp-pin">16.23 kW (21.77 kVA Apparent)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Full-Load Line Current ($I_{\text{FLA}}$):</span>
        <span class="result-val" id="res-mp-fla">23.71 Amperes</span>
    </div>
    <div class="result-row">
        <span class="result-label">Rotor Induced Slip Frequency ($f_r$):</span>
        <span class="result-val" id="res-mp-fr">1.67 Hz</span>
    </div>
</div>
"""

TOOL8_JS = """
function computeMotorParams() {
    var pwrVal = parseFloat(document.getElementById('mp-power').value);
    var pwrUnit = parseFloat(document.getElementById('mp-pwr-unit').value);
    var f = parseFloat(document.getElementById('mp-freq').value);
    var P = parseInt(document.getElementById('mp-poles').value, 10);
    var nr = parseFloat(document.getElementById('mp-rotor-rpm').value);
    var V = parseFloat(document.getElementById('mp-voltage').value);
    var pf = parseFloat(document.getElementById('mp-pf').value);
    var effPct = parseFloat(document.getElementById('mp-eff').value);

    if (isNaN(pwrVal) || pwrVal <= 0 || isNaN(nr) || nr <= 0 || isNaN(V) || V <= 0 || isNaN(pf) || pf <= 0 || isNaN(effPct) || effPct <= 0) return;

    var P_shaft_kW = pwrVal * pwrUnit; // kW
    var P_shaft_HP = P_shaft_kW / 0.745699872;
    var eff = effPct / 100.0;

    // Synchronous speed Ns = 120 * f / P
    var Ns = (120.0 * f) / P;

    // Check rotor speed
    if (nr >= Ns) {
        document.getElementById('res-mp-slip').textContent = "Invalid: Induction motor rotor must run slower than Ns (" + Ns + " RPM)";
        return;
    }

    // Slip s = (Ns - Nr) / Ns * 100%
    var slipRpm = Ns - nr;
    var slipRatio = slipRpm / Ns;
    var slipPct = slipRatio * 100.0;

    // Induced rotor frequency fr = s * f
    var fr = slipRatio * f;

    // Full load torque tau = (P_kW * 9548.8) / nr (N*m)
    var torque_Nm = (P_shaft_kW * 9548.8) / nr;
    var torque_lbft = torque_Nm * 0.737562;

    // Electrical input power Pin = P_shaft / eff (kW)
    var P_in_kW = P_shaft_kW / eff;
    var S_kVA = P_in_kW / pf;

    // Full load current FLA for 3-phase: I = Pin / (sqrt(3) * V * pf)
    var I_fla = (P_in_kW * 1000.0) / (Math.sqrt(3.0) * V * pf);

    document.getElementById('res-mp-ns').textContent = Ns.toFixed(0) + " RPM (Stator Flux Speed)";
    document.getElementById('res-mp-slip').textContent = slipPct.toFixed(2) + "% (" + slipRpm.toFixed(1) + " RPM slip speed)";
    document.getElementById('res-mp-torque').textContent = torque_Nm.toFixed(2) + " N\u00B7m (" + torque_lbft.toFixed(2) + " lb-ft)";
    document.getElementById('res-mp-pin').textContent = P_in_kW.toFixed(2) + " kW (" + S_kVA.toFixed(2) + " kVA Apparent)";
    document.getElementById('res-mp-fla').textContent = I_fla.toFixed(2) + " Amperes";
    document.getElementById('res-mp-fr').textContent = fr.toFixed(2) + " Hz";
}

document.getElementById('calc-mp-btn').addEventListener('click', computeMotorParams);
['mp-power', 'mp-pwr-unit', 'mp-freq', 'mp-poles', 'mp-rotor-rpm', 'mp-voltage', 'mp-pf', 'mp-eff'].forEach(function(id) {
    document.getElementById(id).addEventListener('input', computeMotorParams);
    document.getElementById(id).addEventListener('change', computeMotorParams);
});
window.addEventListener('DOMContentLoaded', computeMotorParams);
"""

TOOL8_ARTICLE = r"""
<h2>Electromechanical Fundamentals of AC Induction Motors</h2>
<p>The three-phase alternating current (AC) squirrel-cage induction motor, patented by Nikola Tesla in 1888, is the undisputed workhorse of modern global industry, consuming over $60\%$ of all industrial electrical power worldwide. The induction motor operates on the principle of electromagnetic induction: three-phase sinusoidal voltages applied to distributed stator windings create a continuously rotating magnetic field (RMF) of constant magnitude rotating at <strong>Synchronous Speed ($N_s$)</strong>.</p>

<p>The speed of this rotating stator magnetic field is locked strictly to AC supply line frequency ($f$) and the geometric number of magnetic poles ($P$) per phase wound into the stator laminations:</p>
$$N_s = \frac{120 \cdot f}{P} \quad [\text{RPM}]$$

<p>Where $120 = 2 \times 60$ accounts for seconds-to-minutes conversion and two electrical pole alternations per complete electrical cycle. In $60\text{ Hz}$ grids, standard synchronous speeds are $3,600\text{ RPM}$ ($2\text{ pole}$), $1,800\text{ RPM}$ ($4\text{ pole}$), and $1,200\text{ RPM}$ ($6\text{ pole}$). In $50\text{ Hz}$ grids, corresponding speeds are $3,000$, $1,500$, and $1,000\text{ RPM}$.</p>

<h2>The Physics of Rotor Slip ($s$) and Torque Generation</h2>
<p>An induction motor can never operate at synchronous speed ($N_r \ne N_s$) under steady mechanical drive conditions. If the conductive rotor turned at the identical speed as the stator flux, the magnetic lines of force would appear stationary relative to the rotor bars. By Faraday's Law of Electromagnetic Induction:</p>
$$e_{\text{induced}} = -\frac{d\Phi}{dt} = 0$$

<p>With zero relative velocity ($\Delta v = 0$), no voltage is induced, no circulating rotor current flows, and Lorentz magnetic force ($F = I L \times B$) vanishes to zero, extinguishing mechanical torque. To generate drive torque, the rotor must constantly fall behind the rotating stator field. This relative velocity lag is termed <strong>Rotor Slip ($s$)</strong>:</p>
$$s = \frac{N_s - N_r}{N_s} \times 100\% = \frac{\Delta N}{N_s} \times 100\%$$

<p>The electrical frequency of the alternating current induced within the rotor bars ($f_r$) is directly proportional to slip:</p>
$$f_r = s \cdot f \quad [\text{Hz}]$$

<p>Under normal full-load operating conditions in standard NEMA Design B or IEC IE3 motors, slip is small ($1.5\%\text{--}4.0\%$), causing rotor currents to cycle at a gentle $1\text{--}2.5\text{ Hz}$, which keeps rotor core hysteresis and eddy current losses negligibly low.</p>

<h2>Full-Load Shaft Torque ($\tau$) and Mechanical Power</h2>
<p>The mechanical power delivered at the rotating shaft output ($P_{\text{mech}}$) is related to rotational torque ($\tau$) and angular velocity ($\omega = \frac{2\pi N_r}{60}$) by:</p>
$$P_{\text{mech}} = \tau \cdot \omega = \tau \cdot \left( \frac{2\pi N_r}{60} \right)$$

<p>Rearranging in metric engineering units where power is in Kilowatts ($\text{kW}$) and torque is in Newton-meters ($\text{N}\cdot\text{m}$):</p>
$$\tau = \frac{60 \times 1000 \cdot P_{\text{kW}}}{2\pi \cdot N_r} = \frac{9548.8 \cdot P_{\text{kW}}}{N_r} \quad [\text{N}\cdot\text{m}]$$

<p>In North American imperial units (Horsepower and pound-feet):</p>
$$\tau = \frac{5252.1 \cdot \text{HP}}{N_r} \quad [\text{lb-ft}]$$

<h2>Electrical Input Power, Full Load Amps (FLA), and Efficiency</h2>
<p>Because induction motors draw lagging magnetizing reactive power to establish stator flux, their electrical characteristics depend on line-to-line RMS voltage ($V_{\text{LL}}$), power factor ($\cos\theta$), and electrical-to-mechanical conversion efficiency ($\eta$):</p>

<h3>1. Active and Apparent Power</h3>
$$P_{\text{in}} = \frac{P_{\text{shaft}}}{\eta} \quad [\text{kW}], \qquad S_{\text{in}} = \frac{P_{\text{in}}}{\cos\theta} \quad [\text{kVA}]$$

<h3>2. Full Load Current (FLA) in Three-Phase Balanced Systems</h3>
$$P_{\text{in}} = \sqrt{3} \cdot V_{\text{LL}} \cdot I_{\text{FLA}} \cdot \cos\theta \implies I_{\text{FLA}} = \frac{P_{\text{in}} \times 1000}{\sqrt{3} \cdot V_{\text{LL}} \cdot \cos\theta}$$

<table class="data-table">
    <thead>
        <tr>
            <th>NEMA Motor Design Class</th>
            <th>Locked Rotor Torque</th>
            <th>Starting Current (LRA)</th>
            <th>Full Load Slip</th>
            <th>Primary Industrial Applications</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>NEMA Design B (Standard)</strong></td>
            <td>Normal ($120\%\text{--}150\%$)</td>
            <td>Normal ($600\%\text{--}700\%$ FLA)</td>
            <td>Low ($1.5\%\text{--}3.5\%$)</td>
            <td>Centrifugal pumps, HVAC fans, blowers, machine tools</td>
        </tr>
        <tr>
            <td><strong>NEMA Design C (High Torque)</strong></td>
            <td>High ($200\%\text{--}250\%$)</td>
            <td>Normal ($600\%\text{--}700\%$ FLA)</td>
            <td>Low to Medium ($3\%\text{--}5\%$)</td>
            <td>Loaded conveyors, positive displacement pumps, crushers</td>
        </tr>
        <tr>
            <td><strong>NEMA Design D (High Slip)</strong></td>
            <td>Very High ($\ge 275\%$)</td>
            <td>Low ($300\%\text{--}500\%$ FLA)</td>
            <td>High ($5\%\text{--}13\%$)</td>
            <td>Punch presses, stamping flywheels, hoists, oil well jacks</td>
        </tr>
        <tr>
            <td><strong>NEMA Design A</strong></td>
            <td>Normal ($120\%\text{--}150\%$)</td>
            <td>High ($> 800\%$ FLA)</td>
            <td>Ultra-Low ($< 1.5\%$)</td>
            <td>Extremely high efficiency, requires oversized switchgear</td>
        </tr>
    </tbody>
</table>

<div class="worked-example-card">
    <h4>Step-by-Step Engineering Case Study: 30 kW Wastewater Centrifugal Pump Motor</h4>
    <p><strong>Scenario:</strong> A municipal wastewater pump is driven by a 4-pole 3-phase squirrel-cage induction motor rated at $P_{\text{shaft}} = 30.0\ \text{kW}$ ($40.23\ \text{HP}$) operating on a $400\ \text{V}$, $50\ \text{Hz}$ industrial grid. The manufacturer nameplate lists full-load rotor speed $N_r = 1,460\ \text{RPM}$, nominal efficiency $\eta = 93.6\%$ (IE3 Premium), and full-load power factor $\cos\theta = 0.85$.</p>
    <div class="step-solution">
        <p><strong>Step 1: Compute Synchronous Speed ($N_s$):</strong></p>
        $$N_s = \frac{120 \times 50\ \text{Hz}}{4\ \text{poles}} = \frac{6000}{4} = 1,500\ \text{RPM}$$
        <p><strong>Step 2: Determine Full-Load Slip ($s$):</strong></p>
        $$\Delta N = N_s - N_r = 1,500 - 1,460 = 40\ \text{RPM}$$
        $$s = \frac{40\ \text{RPM}}{1,500\ \text{RPM}} \times 100\% = 2.667\%$$
        <p><strong>Step 3: Calculate Full-Load Shaft Torque ($\tau$):</strong></p>
        $$\tau = \frac{9548.8 \times 30.0\ \text{kW}}{1,460\ \text{RPM}} = \frac{286,464}{1,460} = 196.21\ \text{N}\cdot\text{m} \approx 144.72\ \text{lb-ft}$$
        <p><strong>Step 4: Compute Electrical Input Power ($P_{\text{in}}$) and Apparent Power ($S$):</strong></p>
        $$P_{\text{in}} = \frac{P_{\text{shaft}}}{\eta} = \frac{30.0\ \text{kW}}{0.936} = 32.051\ \text{kW}$$
        $$S_{\text{in}} = \frac{32.051\ \text{kW}}{0.85} = 37.707\ \text{kVA}$$
        <p><strong>Step 5: Determine Full Load Rated Current ($I_{\text{FLA}}$):</strong></p>
        $$I_{\text{FLA}} = \frac{32.051 \times 1000}{\sqrt{3} \times 400\ \text{V} \times 0.85} = \frac{32,051}{1.73205 \times 340} = \frac{32,051}{588.9} = 54.43\ \text{Amperes}$$
        <p><strong>Step 6: Rotor Induced Slip Frequency ($f_r$):</strong></p>
        $$f_r = 0.02667 \times 50\ \text{Hz} = 1.333\ \text{Hz}$$
        <p><strong>Conclusion:</strong> The motor develops $196.2\ \text{N}\cdot\text{m}$ of shaft torque at $2.67\%$ slip, drawing $54.43\ \text{A}$ of line current with minimal rotor electrical losses ($1.33\ \text{Hz}$ rotor frequency).</p>
    </div>
</div>

<h2>Frequently Asked Questions (FAQ)</h2>
<div class="faq-section">
    <h3>What is synchronous speed in an AC induction motor?</h3>
    <p>Synchronous speed ($N_s$) is the rotational velocity of the stator magnetic field, determined by AC line frequency $f$ and pole count $P$: $N_s = \frac{120 \cdot f}{P}\ \text{RPM}$. For a $60\text{ Hz}$ system, synchronous speeds are $3,600\text{ RPM}$ ($2\text{ poles}$), $1,800\text{ RPM}$ ($4\text{ poles}$), and $1,200\text{ RPM}$ ($6\text{ poles}$).</p>

    <h3>Why must an induction motor have rotor slip?</h3>
    <p>An induction motor relies on Faraday's law of induction. If the rotor spun at synchronous speed, there would be zero relative motion between the rotating stator flux and the rotor bars, inducing zero rotor voltage, zero rotor current, and producing zero mechanical torque. Therefore, an induction motor must always operate below synchronous speed: $\text{Slip } s = \frac{N_s - N_r}{N_s} \times 100\%$.</p>

    <h3>How is full-load torque calculated from shaft power and speed?</h3>
    <p>Full load torque is calculated as $\tau = \frac{P_{\text{kW}} \times 9548.8}{N_r}$ (in Newton-meters) or $\tau = \frac{5252 \times \text{HP}}{N_r}$ (in pound-feet), where $N_r$ is the rated operating rotor speed in RPM.</p>

    <h3>What is the typical full-load slip for NEMA Design B motors?</h3>
    <p>Standard NEMA Design B industrial squirrel-cage induction motors operate with full-load slip between $1.5\%$ and $4.0\%$ (e.g., a 4-pole $1,800\text{ RPM}$ motor typically runs at $1,740$ to $1,765\text{ RPM}$ under full rated load).</p>
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
    generate_tool(TOOL7_SLUG, TOOL7_TITLE, TOOL7_DESC, TOOL7_H1, TOOL7_SHORT, TOOL7_SCHEMA, TOOL7_UI, TOOL7_JS, TOOL7_ARTICLE)
    generate_tool(TOOL8_SLUG, TOOL8_TITLE, TOOL8_DESC, TOOL8_H1, TOOL8_SHORT, TOOL8_SCHEMA, TOOL8_UI, TOOL8_JS, TOOL8_ARTICLE)
