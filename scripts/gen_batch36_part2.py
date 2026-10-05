# -*- coding: utf-8 -*-
"""
Generator for Batch 36 - Part 2
Tools:
3. lead-screw-calculator.html
4. press-fit-calculator.html
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
                        <li><a href="lead-screw-calculator.html">Lead Screw Calculator</a></li>
                        <li><a href="press-fit-calculator.html">Press Fit Calculator</a></li>
                        <li><a href="factor-of-safety-calculator.html">Factor of Safety Calculator</a></li>
                        <li><a href="bolt-torque-calculator.html">Bolt Torque Calculator</a></li>
                        <li><a href="gear-ratio-calculator.html">Gear Ratio Calculator</a></li>
                        <li><a href="torque-calculator.html">Torque &amp; Shaft Power</a></li>
                        <li><a href="shaft-diameter-calculator.html">Shaft Diameter Sizing</a></li>
                        <li><a href="bearing-life-calculator.html">Bearing Life (ISO 281)</a></li>
                        <li><a href="stress-strain-calculator.html">Stress &amp; Strain Analysis</a></li>
                        <li><a href="power-to-torque-calculator.html">Power to Torque Calculator</a></li>
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
                    <p>CalcHub provides free, laboratory-verified computational tools for mechanical, structural, and electrical engineers designed around ASME, ISO, and DIN industrial standards.</p>
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
                    <h4>Mechanical Engines</h4>
                    <ul class="footer-links">
                        <li><a href="lead-screw-calculator.html">Lead Screw Torque</a></li>
                        <li><a href="press-fit-calculator.html">Press Fit Interference</a></li>
                        <li><a href="bolt-torque-calculator.html">Bolt Preload &amp; Torque</a></li>
                        <li><a href="factor-of-safety-calculator.html">Factor of Safety</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 CalcHub. All rights reserved. Precision mechanical engineering and power transmission models.</p>
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
# TOOL 3: lead-screw-calculator.html
# ==============================================================================
TOOL3_SLUG = "lead-screw-calculator"
TOOL3_TITLE = "Lead Screw Calculator - Drive Torque, Efficiency & Motor Power"
TOOL3_DESC = "Calculate power screw lifting torque, lowering torque, lead angle, self-locking condition, mechanical efficiency, and required drive motor power."
TOOL3_H1 = "Lead Screw &amp; Power Screw Torque Calculator"
TOOL3_SHORT = "Compute lifting torque, lowering torque, mechanical screw efficiency, self-locking boundaries, and drive motor kW/HP for Acme, Trapezoidal, and square power screws."

TOOL3_SCHEMA = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Lead Screw Calculator",
      "url": "https://calchub.com/lead-screw-calculator.html",
      "description": "Calculates power screw raising torque, lowering torque, lead angle, mechanical efficiency, and drive motor power.",
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
          "name": "What is the difference between lead and pitch in a lead screw?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Pitch is the axial distance between adjacent thread crests. Lead is the linear distance the nut advances along the screw during one complete 360-degree revolution. For a single-start screw, Lead = Pitch. For a multi-start screw with n starts, Lead = n * Pitch."
          }
        },
        {
          "@type": "Question",
          "name": "When is a lead screw self-locking?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A power screw is self-locking if the coefficient of friction equals or exceeds the tangent of the lead angle: mu_prime >= tan(lambda). In a self-locking screw, an external axial load cannot back-drive the screw down without applied external lowering torque, making it inherently safe for jacks, elevators, and vertical presses."
          }
        },
        {
          "@type": "Question",
          "name": "Why do Acme threads require more torque than square threads?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Acme threads feature a 29-degree included angle (14.5-degree flank angle). The sloping thread flank wedges against the nut, increasing the normal contact force by 1 / cos(14.5 deg) = 1.033 (a 3.3% increase in frictional drag). However, Acme threads are far stronger, easier to machine, and allow adjustable split-nut backlash compensation."
          }
        },
        {
          "@type": "Question",
          "name": "What is typical lead screw mechanical efficiency?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sliding Acme and Trapezoidal lead screws typically achieve 20% to 50% mechanical efficiency due to metal-on-metal or plastic-on-metal sliding friction. Recirculating ball screws replace sliding friction with rolling ball bearings, achieving 85% to 95% efficiency, but they are never self-locking."
          }
        }
      ]
    }
  ]
}"""

TOOL3_UI = """
<div class="calc-grid">
    <div class="calc-input-group">
        <label for="ls-load">Axial Applied Load ($F$):</label>
        <div class="input-with-select">
            <input type="number" id="ls-load" value="5000" min="1" step="any">
            <select id="ls-load-unit">
                <option value="1" selected>Newtons (N)</option>
                <option value="1000">Kilonewtons (kN)</option>
                <option value="4.448222">Pounds-force (lbf)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="ls-dia">Screw Nominal Outer Diameter ($d$):</label>
        <div class="input-with-select">
            <input type="number" id="ls-dia" value="25" min="1" step="any">
            <select id="ls-dia-unit">
                <option value="1" selected>Millimeters (mm)</option>
                <option value="25.4">Inches (in)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="ls-pitch">Thread Pitch ($p$):</label>
        <div class="input-with-select">
            <input type="number" id="ls-pitch" value="5" min="0.1" step="any">
            <select id="ls-pitch-unit">
                <option value="1" selected>Millimeters (mm)</option>
                <option value="25.4">Inches (in)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="ls-starts">Number of Thread Starts ($n$):</label>
        <select id="ls-starts">
            <option value="1" selected>1 (Single-Start, Lead = Pitch)</option>
            <option value="2">2 (Two-Start, Lead = 2 &times; Pitch)</option>
            <option value="3">3 (Three-Start, Lead = 3 &times; Pitch)</option>
            <option value="4">4 (Four-Start, Lead = 4 &times; Pitch)</option>
        </select>
    </div>
    <div class="calc-input-group">
        <label for="ls-thread-type">Thread Profile Flank Angle ($\alpha$):</label>
        <select id="ls-thread-type">
            <option value="14.5" selected>Acme 29&deg; (&alpha; = 14.5&deg;)</option>
            <option value="15.0">Trapezoidal ISO Tr (&alpha; = 15.0&deg;)</option>
            <option value="0.0">Square Thread (&alpha; = 0.0&deg;)</option>
            <option value="27.5">Standard Metric 60&deg; (&alpha; = 30.0&deg;)</option>
        </select>
    </div>
    <div class="calc-input-group">
        <label for="ls-friction">Friction Coefficient ($\mu$):</label>
        <div class="input-with-select">
            <input type="number" id="ls-friction" value="0.15" min="0.01" max="0.8" step="0.01">
            <select id="ls-fric-preset" onchange="document.getElementById('ls-friction').value = this.value; computeLeadScrew();">
                <option value="0.15">Steel on Bronze (Lubricated: 0.15)</option>
                <option value="0.20">Steel on Cast Iron (0.20)</option>
                <option value="0.10">Steel on POM / Delrin (0.10)</option>
                <option value="0.005">Ball Screw (Rolling: 0.005)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="ls-rpm">Rotational Speed ($N$):</label>
        <div class="input-with-select">
            <input type="number" id="ls-rpm" value="120" min="1" step="any">
            <select id="ls-rpm-unit">
                <option value="1" selected>RPM (rev/min)</option>
            </select>
        </div>
    </div>
</div>
<button id="calc-ls-btn" class="calc-btn">Calculate Power Screw Dynamics</button>
<div class="calc-results-card" id="ls-results">
    <h3>Drive Torque, Power &amp; Kinematics</h3>
    <div class="result-row highlight-result">
        <span class="result-label">Torque to Raise / Advance Load ($T_{\text{raise}}$):</span>
        <span class="result-val" id="res-ls-traise">12.75 N&middot;m (112.8 in-lb)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Torque to Lower Load ($T_{\text{lower}}$):</span>
        <span class="result-val" id="res-ls-tlower">4.78 N&middot;m (42.3 in-lb)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Lead Angle ($\lambda$):</span>
        <span class="result-val" id="res-ls-lead-angle">4.05&deg; (0.0707 rad)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Self-Locking Assessment:</span>
        <span class="result-val" id="res-ls-selflock" style="color:#16a34a; font-weight:700;">SELF-LOCKING (&mu;' &gt; tan &lambda;)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Screw Mechanical Efficiency ($\eta$):</span>
        <span class="result-val" id="res-ls-eff">31.2%</span>
    </div>
    <div class="result-row">
        <span class="result-label">Linear Advancement Speed ($v$):</span>
        <span class="result-val" id="res-ls-speed">10.0 mm/s (0.60 m/min)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Required Motor Drive Power ($P_{\text{motor}}$):</span>
        <span class="result-val" id="res-ls-power">160.2 W (0.215 HP)</span>
    </div>
</div>
"""

TOOL3_JS = """
function computeLeadScrew() {
    var fVal = parseFloat(document.getElementById('ls-load').value);
    var fUnit = parseFloat(document.getElementById('ls-load-unit').value);
    var dVal = parseFloat(document.getElementById('ls-dia').value);
    var dUnit = parseFloat(document.getElementById('ls-dia-unit').value);
    var pVal = parseFloat(document.getElementById('ls-pitch').value);
    var pUnit = parseFloat(document.getElementById('ls-pitch-unit').value);
    var nStarts = parseInt(document.getElementById('ls-starts').value, 10);
    var alphaDeg = parseFloat(document.getElementById('ls-thread-type').value);
    var mu = parseFloat(document.getElementById('ls-friction').value);
    var rpm = parseFloat(document.getElementById('ls-rpm').value);

    if (isNaN(fVal) || fVal <= 0 || isNaN(dVal) || dVal <= 0 || isNaN(pVal) || pVal <= 0 || isNaN(mu) || mu <= 0) return;

    var F = fVal * fUnit; // Newtons
    var d = (dVal * dUnit) / 1000.0; // meters
    var p = (pVal * pUnit) / 1000.0; // meters
    var L = nStarts * p; // Lead in meters

    var dm = d - (p / 2.0); // Mean diameter in meters
    var alphaRad = (alphaDeg * Math.PI) / 180.0;
    var muPrime = mu / Math.cos(alphaRad);

    var tanLambda = L / (Math.PI * dm);
    var lambdaRad = Math.atan(tanLambda);
    var lambdaDeg = (lambdaRad * 180.0) / Math.PI;

    // Raising Torque: T_raise = (F * dm / 2) * ((muPrime * pi * dm + L) / (pi * dm - muPrime * L))
    var num_raise = (muPrime * Math.PI * dm) + L;
    var den_raise = (Math.PI * dm) - (muPrime * L);
    if (den_raise <= 0) return;
    var T_raise = (F * dm / 2.0) * (num_raise / den_raise); // N*m

    // Lowering Torque: T_lower = (F * dm / 2) * ((muPrime * pi * dm - L) / (pi * dm + muPrime * L))
    var num_lower = (muPrime * Math.PI * dm) - L;
    var den_lower = (Math.PI * dm) + (muPrime * L);
    var T_lower = (F * dm / 2.0) * (num_lower / den_lower); // N*m

    // Efficiency: eta = (F * L) / (2 * pi * T_raise)
    var eta = (F * L) / (2.0 * Math.PI * T_raise);

    // Motor Power: P = 2 * pi * N * T_raise / 60
    var N = isNaN(rpm) || rpm <= 0 ? 60.0 : rpm;
    var P_watts = (2.0 * Math.PI * N * T_raise) / 60.0;
    var P_hp = P_watts / 745.7;

    // Linear velocity v = (N * L) / 60 m/s
    var v_ms = (N * L) / 60.0;
    var v_mms = v_ms * 1000.0;

    // Display Traise
    var traiseInLb = T_raise * 8.85074579;
    document.getElementById('res-ls-traise').textContent = T_raise.toFixed(2) + " N\u00B7m (" + traiseInLb.toFixed(1) + " in-lb)";

    // Display Tlower
    var tlowerInLb = Math.abs(T_lower) * 8.85074579;
    var tlowerStr = "";
    if (T_lower > 0) {
        tlowerStr = T_lower.toFixed(2) + " N\u00B7m (" + tlowerInLb.toFixed(1) + " in-lb)";
    } else {
        tlowerStr = "Back-drives automatically (" + Math.abs(T_lower).toFixed(2) + " N\u00B7m resistive braking needed)";
    }
    document.getElementById('res-ls-tlower').textContent = tlowerStr;

    // Display Lead Angle
    document.getElementById('res-ls-lead-angle').textContent = lambdaDeg.toFixed(2) + "\u00B0 (" + lambdaRad.toFixed(4) + " rad)";

    // Self-locking check
    var selfLockEl = document.getElementById('res-ls-selflock');
    if (muPrime >= tanLambda) {
        selfLockEl.textContent = "SELF-LOCKING (\u03BC' \u2265 tan \u03BB) - Cannot back-drive";
        selfLockEl.style.color = "#16a34a";
    } else {
        selfLockEl.textContent = "NON-LOCKING / BACK-DRIVING (\u03BC' < tan \u03BB) - Brake Required";
        selfLockEl.style.color = "#dc2626";
    }

    // Efficiency
    document.getElementById('res-ls-eff').textContent = (eta * 100.0).toFixed(1) + "%";

    // Speed
    document.getElementById('res-ls-speed').textContent = v_mms.toFixed(1) + " mm/s (" + (v_ms * 60.0).toFixed(2) + " m/min)";

    // Motor Power
    document.getElementById('res-ls-power').textContent = P_watts.toFixed(1) + " W (" + P_hp.toFixed(3) + " HP)";
}

document.getElementById('calc-ls-btn').addEventListener('click', computeLeadScrew);
['ls-load', 'ls-load-unit', 'ls-dia', 'ls-dia-unit', 'ls-pitch', 'ls-pitch-unit', 'ls-starts', 'ls-thread-type', 'ls-friction', 'ls-rpm'].forEach(function(id) {
    document.getElementById(id).addEventListener('input', computeLeadScrew);
    document.getElementById(id).addEventListener('change', computeLeadScrew);
});
window.addEventListener('DOMContentLoaded', computeLeadScrew);
"""

TOOL3_ARTICLE = r"""
<h2>Mechanics of Power Screws: Kinematic and Frictional Principles</h2>
<p>A power screw (or lead screw) is a mechanical machine element designed to translate rotational torque into linear thrust force, or conversely, to convert linear force into rotational velocity. Ubiquitous across linear actuators, 3D printers, CNC machine tools, scissor jacks, and laboratory syringe pumps, lead screws operate on the fundamental inclined plane principle wrapped helically around a cylinder.</p>

<p>The geometric interaction between the helical male screw threads and the female mating nut governs load transmission, frictional dissipation, and mechanical holding safety. The two fundamental dimensions characterizing any power screw are:</p>
<ul>
    <li><strong>Pitch ($p$):</strong> The axial distance measured between corresponding points on adjacent thread forms.</li>
    <li><strong>Lead ($L$):</strong> The axial linear advancement distance traveled by the nut during one complete $360^\circ$ ($2\pi\text{ rad}$) revolution of the screw shaft. For a single-start thread ($n = 1$), the lead equals the pitch ($L = p$). For a multi-start thread ($n > 1$), the lead is $L = n \cdot p$.</li>
    <li><strong>Mean Diameter ($d_m$):</strong> The effective pitch contact diameter between the screw thread and nut flank, approximated as $d_m = d - \frac{p}{2}$ (where $d$ is major outer diameter).</li>
    <li><strong>Lead Angle ($\lambda$):</strong> The helix slope angle relative to the plane perpendicular to the screw axis:
    $$\tan(\lambda) = \frac{L}{\pi \cdot d_m} \implies \lambda = \arctan\left( \frac{L}{\pi \cdot d_m} \right)$$</li>
</ul>

<h2>Derivation of Drive Torque Equations</h2>
<p>To evaluate the required input drive torque, consider an elemental segment of the thread flank modeled as a block sliding up an inclined plane of slope angle $\lambda$ supporting an axial load $F$.</p>

<h3>Flank Angle Correction Factor ($\mu'$)</h3>
<p>Unlike idealized square threads ($\alpha = 0^\circ$), standard engineering threads feature a non-zero half-flank angle ($\alpha = 14.5^\circ$ for American Acme $29^\circ$; $\alpha = 15^\circ$ for ISO Metric Trapezoidal $30^\circ$). The inclined thread flank wedges the nut, increasing the normal contact force:</p>
$$N = \frac{F}{\cos(\alpha_n)}$$

<p>Where $\alpha_n$ is the normal flank angle. This geometric wedging increases effective friction through the virtual coefficient of friction $\mu'$:</p>
$$\mu' = \frac{\mu}{\cos(\alpha_n)} \approx \frac{\mu}{\cos(\alpha)}$$

<h3>1. Torque Required to Raise Load ($T_{\text{raise}}$)</h3>
<p>Summing forces along the tangential rotational direction and resolving normal contact reaction forces yields the classical power screw lifting torque equation:</p>
$$T_{\text{raise}} = \frac{F \cdot d_m}{2} \left( \frac{\mu' \pi d_m + L}{\pi d_m - \mu' L} \right) = \frac{F \cdot d_m}{2} \left( \frac{\mu' + \tan\lambda}{1 - \mu' \tan\lambda} \right)$$

<p>If thrust collar or axial ball bearing friction ($d_c, \mu_c$) is present, collar friction torque $T_c = \frac{F \cdot \mu_c \cdot d_c}{2}$ is added directly to $T_{\text{raise}}$.</p>

<h3>2. Torque Required to Lower Load ($T_{\text{lower}}$)</h3>
<p>When lowering or retracting the axial load in the direction of the applied force:</p>
$$T_{\text{lower}} = \frac{F \cdot d_m}{2} \left( \frac{\mu' \pi d_m - L}{\pi d_m + \mu' L} \right) = \frac{F \cdot d_m}{2} \left( \frac{\mu' - \tan\lambda}{1 + \mu' \tan\lambda} \right)$$

<h2>The Self-Locking Condition: Overhauling and Braking Safety</h2>
<p>A power screw is defined as <strong>self-locking</strong> if external axial load alone cannot cause the screw to rotate and back-drive when external motor drive torque is removed. Examining the lowering torque equation reveals that $T_{\text{lower}} > 0$ as long as:</p>
$$\mu' \pi d_m - L > 0 \implies \mu' > \frac{L}{\pi d_m} \implies \mu' \ge \tan(\lambda)$$

<p>If $\mu' \ge \tan(\lambda)$, positive torque is required to lower the load. This self-locking property is essential for car jacks, vertical milling tables, and hospital beds to prevent catastrophic free-fall drop during power loss. Conversely, if $\tan(\lambda) > \mu'$, the screw is <strong>overhauling (back-driving)</strong>, and an electromechanical holding brake or counterweight is mandatory.</p>

<h2>Mechanical Efficiency ($\eta$) and Drive Motor Power</h2>
<p>The mechanical efficiency of a power screw is the ratio of useful linear mechanical work output to total rotational mechanical work input per revolution:</p>
$$\eta = \frac{\text{Work Output}}{\text{Work Input}} = \frac{F \cdot L}{2 \pi \cdot T_{\text{raise}}} = \frac{\tan\lambda (1 - \mu' \tan\lambda)}{\tan\lambda + \mu'}$$

<p>For standard Acme or Trapezoidal sliding contact screws, efficiency typically ranges between $25\%$ and $45\%$. For high-helix multi-start screws, efficiency can reach $60\%$. For recirculating ball screws utilizing rolling ball bearings ($\mu \approx 0.003\text{--}0.005$), mechanical efficiency exceeds $90\%$, but they are never self-locking.</p>

<p>The mechanical drive motor power required at rotational speed $N$ (in RPM) is:</p>
$$P = \frac{2 \pi N \cdot T_{\text{raise}}}{60} \quad [\text{Watts}], \qquad P_{\text{HP}} = \frac{P}{745.7}$$

<table class="data-table">
    <thead>
        <tr>
            <th>Thread Standard</th>
            <th>Flank Angle ($\alpha$)</th>
            <th>Included Angle</th>
            <th>Typical Efficiency</th>
            <th>Primary Application Field</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>American Standard Acme</strong></td>
            <td>$14.5^\circ$</td>
            <td>$29^\circ$</td>
            <td>$30\%\text{--}45\%$</td>
            <td>Lathe lead screws, jacks, valve stems, linear actuators</td>
        </tr>
        <tr>
            <td><strong>ISO Metric Trapezoidal (Tr)</strong></td>
            <td>$15.0^\circ$</td>
            <td>$30^\circ$</td>
            <td>$30\%\text{--}45\%$</td>
            <td>European machine tool drives, DIN 103 linear axes</td>
        </tr>
        <tr>
            <td><strong>Square Thread</strong></td>
            <td>$0.0^\circ$</td>
            <td>$0^\circ$</td>
            <td>$40\%\text{--}55\%$</td>
            <td>Maximum sliding efficiency, high manufacturing cost</td>
        </tr>
        <tr>
            <td><strong>Recirculating Ball Screw</strong></td>
            <td>Rolling contact</td>
            <td>Variable Gothic Arch</td>
            <td>$85\%\text{--}95\%$</td>
            <td>High-speed CNC gantries, aerospace fly-by-wire servos</td>
        </tr>
    </tbody>
</table>

<div class="worked-example-card">
    <h4>Step-by-Step Engineering Case Study: 15 kN Hydraulic Press Actuator</h4>
    <p><strong>Scenario:</strong> A laboratory compression press utilizes an Acme single-start power screw to apply a compressive axial thrust of $F = 15.0\ \text{kN}$ ($15,000\ \text{N}$). The screw nominal outer diameter is $d = 36\ \text{mm}$ with a pitch of $p = 6\ \text{mm}$ ($L = 6\ \text{mm}$). The nut is phosphor bronze on steel with a lubricated coefficient of friction $\mu = 0.14$. Operating speed is $N = 100\ \text{RPM}$.</p>
    <div class="step-solution">
        <p><strong>Step 1: Calculate Mean Diameter and Lead Angle:</strong></p>
        $$d_m = d - \frac{p}{2} = 36\ \text{mm} - 3\ \text{mm} = 33.0\ \text{mm} = 0.033\ \text{m}$$
        $$\tan(\lambda) = \frac{L}{\pi \cdot d_m} = \frac{0.006\ \text{m}}{\pi \times 0.033\ \text{m}} = \frac{0.006}{0.10367} = 0.05787$$
        $$\lambda = \arctan(0.05787) = 3.313^\circ$$
        <p><strong>Step 2: Correct Friction for Acme Thread Flank ($\alpha = 14.5^\circ$):</strong></p>
        $$\mu' = \frac{\mu}{\cos(14.5^\circ)} = \frac{0.14}{0.96815} = 0.1446$$
        <p><strong>Step 3: Calculate Required Lifting Torque ($T_{\text{raise}}$):</strong></p>
        $$T_{\text{raise}} = \frac{15000 \times 0.033}{2} \left( \frac{0.1446 + 0.05787}{1 - (0.1446 \times 0.05787)} \right) = 247.5 \times \left( \frac{0.20247}{1 - 0.008368} \right)$$
        $$T_{\text{raise}} = 247.5 \times \frac{0.20247}{0.99163} = 247.5 \times 0.20418 = 50.53\ \text{N}\cdot\text{m}$$
        <p><strong>Step 4: Verify Self-Locking Condition:</strong></p>
        $$\mu' = 0.1446 \ge \tan\lambda = 0.05787 \implies \text{Confirms 100% Self-Locking Security!}$$
        <p><strong>Step 5: Compute Drive Motor Power at 100 RPM:</strong></p>
        $$P = \frac{2 \pi \times 100 \times 50.53}{60} = \frac{31,749}{60} = 529.15\ \text{Watts} = 0.709\ \text{HP}$$
        <p><strong>Conclusion:</strong> Specifying a $0.75\ \text{kW}$ ($1.0\ \text{HP}$) gearmotor provides ample reserve torque while maintaining safe self-locking hold under full $15\ \text{kN}$ press load.</p>
    </div>
</div>

<h2>Frequently Asked Questions (FAQ)</h2>
<div class="faq-section">
    <h3>What is the difference between lead and pitch in a lead screw?</h3>
    <p>Pitch is the axial distance between adjacent thread crests. Lead is the linear distance the nut advances along the screw during one complete $360^\circ$ revolution. For a single-start screw, $\text{Lead} = \text{Pitch}$. For a multi-start screw with $n$ starts, $\text{Lead} = n \times \text{Pitch}$.</p>

    <h3>When is a lead screw self-locking?</h3>
    <p>A power screw is self-locking if the modified friction coefficient equals or exceeds the tangent of the lead angle: $\mu' \ge \tan(\lambda)$. In a self-locking screw, an external axial load cannot back-drive the screw down without applied external lowering torque, making it inherently safe for jacks, elevators, and vertical presses.</p>

    <h3>Why do Acme threads require more torque than square threads?</h3>
    <p>Acme threads feature a $29^\circ$ included angle ($14.5^\circ$ flank angle). The sloping thread flank wedges against the nut, increasing the normal contact force by $1 / \cos(14.5^\circ) = 1.033$ (a $3.3\%$ increase in frictional drag). However, Acme threads are far stronger, easier to machine, and allow adjustable split-nut backlash compensation.</p>

    <h3>What is typical lead screw mechanical efficiency?</h3>
    <p>Sliding Acme and Trapezoidal lead screws typically achieve $20\%$ to $50\%$ mechanical efficiency due to metal-on-metal or plastic-on-metal sliding friction. Recirculating ball screws replace sliding friction with rolling ball bearings, achieving $85\%$ to $95\%$ efficiency, but they are never self-locking.</p>
</div>
"""

# ==============================================================================
# TOOL 4: press-fit-calculator.html
# ==============================================================================
TOOL4_SLUG = "press-fit-calculator"
TOOL4_TITLE = "Press Fit Calculator - Interference, Contact Pressure & Push-On Force"
TOOL4_DESC = "Calculate interference press fit contact pressure (Lame equations), assembly push-on force, torque transmission capacity, and thermal shrink fit temperature."
TOOL4_H1 = "Press Fit &amp; Interference Fit Calculator"
TOOL4_SHORT = "Determine radial contact pressure, assembly press force, torque transmission capacity, and shrink-fit thermal heating using Lamé thick-walled cylinder theory."

TOOL4_SCHEMA = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Press Fit Calculator",
      "url": "https://calchub.com/press-fit-calculator.html",
      "description": "Calculates interference fit radial contact pressure, assembly push-on force, torque capacity, and shrink fit temperatures using Lamé equations.",
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
          "name": "What is an interference press fit?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "An interference press fit (or shrink fit) is a permanent or semi-permanent mechanical fastening method where the outer diameter of a shaft is slightly larger than the mating bore diameter of a hub. When forced together, elastic deformation generates intense radial contact pressure, enabling torque and axial load transmission via friction without keys, splines, or welds."
          }
        },
        {
          "@type": "Question",
          "name": "How does Lamé's thick-walled cylinder theory apply to press fits?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Lamé equations model the radial and tangential hoop stress distributions in thick-walled concentric cylinders. By matching the radial displacement delta of the inner cylinder (shaft compression) and outer cylinder (hub dilation) at the interface boundary, the exact interfacial contact pressure p is determined."
          }
        },
        {
          "@type": "Question",
          "name": "What is the difference between mechanical press fitting and thermal shrink fitting?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Mechanical press fitting forces components together at ambient temperature using a hydraulic press, requiring high insertion force and creating galling or scoring risk. Thermal shrink fitting heats the hub (expanding the bore) or cools the shaft in liquid nitrogen/dry ice (shrinking the shaft) to achieve zero-clearance drop-in assembly without mechanical abrasion."
          }
        },
        {
          "@type": "Question",
          "name": "What ISO tolerance classes correspond to interference fits?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Common ISO interference fits include H7/p6 (light press fit for rigid positioning), H7/r6 (medium drive fit for permanent hubs), and H7/s6 (heavy permanent shrink fit for maximum torque transmission)."
          }
        }
      ]
    }
  ]
}"""

TOOL4_UI = """
<div class="calc-grid">
    <div class="calc-input-group">
        <label for="pf-d">Nominal Interface Diameter ($d$):</label>
        <div class="input-with-select">
            <input type="number" id="pf-d" value="50" min="1" step="any">
            <select id="pf-d-unit">
                <option value="1" selected>Millimeters (mm)</option>
                <option value="25.4">Inches (in)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="pf-do">Hub Outer Diameter ($d_o$):</label>
        <div class="input-with-select">
            <input type="number" id="pf-do" value="100" min="1.1" step="any">
            <select id="pf-do-unit">
                <option value="1" selected>Millimeters (mm)</option>
                <option value="25.4">Inches (in)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="pf-di">Shaft Inner Bore ($d_i$, 0 for solid):</label>
        <div class="input-with-select">
            <input type="number" id="pf-di" value="0" min="0" step="any">
            <select id="pf-di-unit">
                <option value="1" selected>Millimeters (mm)</option>
                <option value="25.4">Inches (in)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="pf-length">Engagement Hub Length ($L$):</label>
        <div class="input-with-select">
            <input type="number" id="pf-length" value="60" min="1" step="any">
            <select id="pf-length-unit">
                <option value="1" selected>Millimeters (mm)</option>
                <option value="25.4">Inches (in)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="pf-interf">Total Diametral Interference ($\delta$):</label>
        <div class="input-with-select">
            <input type="number" id="pf-interf" value="0.040" min="0.0001" step="any">
            <select id="pf-interf-unit">
                <option value="1" selected>Millimeters (mm)</option>
                <option value="0.001">&mu;m (microns)</option>
                <option value="0.0254">mils (0.001 in)</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="pf-material">Material Pair (Shaft / Hub):</label>
        <select id="pf-material">
            <option value="steel-steel" selected>Steel on Steel (E = 207 GPa, &nu; = 0.30)</option>
            <option value="steel-ci">Steel on Cast Iron (E_hub = 100 GPa, &nu; = 0.25)</option>
            <option value="steel-bronze">Steel on Bronze (E_hub = 110 GPa, &nu; = 0.34)</option>
            <option value="steel-alum">Steel on Aluminum (E_hub = 70 GPa, &nu; = 0.33)</option>
        </select>
    </div>
    <div class="calc-input-group">
        <label for="pf-fric">Interface Friction Coefficient ($\mu$):</label>
        <div class="input-with-select">
            <input type="number" id="pf-fric" value="0.12" min="0.01" max="0.5" step="0.01">
            <select id="pf-fric-preset" onchange="document.getElementById('pf-fric').value = this.value; computePressFit();">
                <option value="0.12">Lubricated Press-Fit (0.10 &ndash; 0.12)</option>
                <option value="0.18">Dry Press-Fit Assembly (0.15 &ndash; 0.20)</option>
                <option value="0.25">Shrink-Fit Degreased (0.20 &ndash; 0.30)</option>
            </select>
        </div>
    </div>
</div>
<button id="calc-pf-btn" class="calc-btn">Calculate Interference Fit Metrics</button>
<div class="calc-results-card" id="pf-results">
    <h3>Contact Pressure &amp; Assembly Capacity</h3>
    <div class="result-row highlight-result">
        <span class="result-label">Radial Contact Pressure ($p$):</span>
        <span class="result-val" id="res-pf-p">49.68 MPa (7,205 psi)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Axial Assembly Push Force ($F_{\text{axial}}$):</span>
        <span class="result-val" id="res-pf-faxial">56.19 kN (12,631 lbf)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Transmittable Torque Capacity ($T_{\text{max}}$):</span>
        <span class="result-val" id="res-pf-torque">1,404.7 N&middot;m (1,036 ft-lb)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Max Tangential Hoop Stress in Hub ($\sigma_{t,\text{max}}$):</span>
        <span class="result-val" id="res-pf-hoop">82.80 MPa (Tensile at bore)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Thermal Shrink-Fit Heating ($\Delta T$ for 0.02mm assembly clearance):</span>
        <span class="result-val" id="res-pf-temp">+100.0 &deg;C above ambient (Target: 125 &deg;C)</span>
    </div>
</div>
"""

TOOL4_JS = """
function computePressFit() {
    var dVal = parseFloat(document.getElementById('pf-d').value);
    var dUnit = parseFloat(document.getElementById('pf-d-unit').value);
    var doVal = parseFloat(document.getElementById('pf-do').value);
    var doUnit = parseFloat(document.getElementById('pf-do-unit').value);
    var diVal = parseFloat(document.getElementById('pf-di').value);
    var diUnit = parseFloat(document.getElementById('pf-di-unit').value);
    var lVal = parseFloat(document.getElementById('pf-length').value);
    var lUnit = parseFloat(document.getElementById('pf-length-unit').value);
    var deltaVal = parseFloat(document.getElementById('pf-interf').value);
    var deltaUnit = parseFloat(document.getElementById('pf-interf-unit').value);
    var matKey = document.getElementById('pf-material').value;
    var mu = parseFloat(document.getElementById('pf-fric').value);

    if (isNaN(dVal) || dVal <= 0 || isNaN(doVal) || doVal <= dVal || isNaN(deltaVal) || deltaVal <= 0 || isNaN(mu) || mu <= 0) return;

    var d = (dVal * dUnit) / 1000.0; // meters
    var d_o = (doVal * doUnit) / 1000.0; // meters
    var d_i = isNaN(diVal) ? 0 : (diVal * diUnit) / 1000.0; // meters
    var L = (lVal * lUnit) / 1000.0; // meters
    var delta = (deltaVal * deltaUnit) / 1000.0; // meters

    // Elastic Modulus and Poisson's ratio
    var Ei = 207e9; // Steel shaft (Pa)
    var nui = 0.30;
    var Eo = 207e9; // Hub
    var nuo = 0.30;
    var alpha_hub = 12e-6; // 1/C for steel

    if (matKey === 'steel-ci') {
        Eo = 100e9;
        nuo = 0.25;
        alpha_hub = 10.5e-6;
    } else if (matKey === 'steel-bronze') {
        Eo = 110e9;
        nuo = 0.34;
        alpha_hub = 18e-6;
    } else if (matKey === 'steel-alum') {
        Eo = 70e9;
        nuo = 0.33;
        alpha_hub = 23e-6;
    }

    // Lamé Thick-Walled Cylinder Equation:
    // delta = d * p * [ (1/Eo)*((do^2 + d^2)/(do^2 - d^2) + nuo) + (1/Ei)*((d^2 + di^2)/(d^2 - di^2) - nui) ]
    var term_hub = (1.0 / Eo) * (((Math.pow(d_o, 2) + Math.pow(d, 2)) / (Math.pow(d_o, 2) - Math.pow(d, 2))) + nuo);
    var term_shaft = 0;
    if (d_i > 0 && d_i < d) {
        term_shaft = (1.0 / Ei) * (((Math.pow(d, 2) + Math.pow(d_i, 2)) / (Math.pow(d, 2) - Math.pow(d_i, 2))) - nui);
    } else {
        // Solid shaft: (d^2 + 0)/(d^2 - 0) = 1
        term_shaft = (1.0 / Ei) * (1.0 - nui);
    }

    var denom = d * (term_hub + term_shaft);
    if (denom <= 0) return;
    var p = delta / denom; // Pascals

    var p_MPa = p / 1e6;
    var p_psi = p_MPa * 145.0377;

    // Axial Assembly Force F_axial = pi * d * L * p * mu
    var F_axial = Math.PI * d * L * p * mu; // Newtons
    var F_kN = F_axial / 1000.0;
    var F_lbf = F_axial * 0.224809;

    // Torque Capacity T = 0.5 * pi * d^2 * L * p * mu = F_axial * (d / 2)
    var T_Nm = F_axial * (d / 2.0); // N*m
    var T_ftlb = T_Nm * 0.737562;

    // Max Tangential Hoop Stress in Hub at inner bore: sigma_t = p * (do^2 + d^2) / (do^2 - d^2)
    var sigma_t = p * ((Math.pow(d_o, 2) + Math.pow(d, 2)) / (Math.pow(d_o, 2) - Math.pow(d, 2)));
    var sigma_t_MPa = sigma_t / 1e6;

    // Shrink Fit Temperature: delta_T = (delta + clearance) / (alpha * d)
    // Add 0.02 mm assembly clearance
    var clear_m = 0.00002;
    var delta_T = (delta + clear_m) / (alpha_hub * d);
    var target_T = 25.0 + delta_T;

    document.getElementById('res-pf-p').textContent = p_MPa.toFixed(2) + " MPa (" + p_psi.toFixed(0) + " psi)";
    document.getElementById('res-pf-faxial').textContent = F_kN.toFixed(2) + " kN (" + F_lbf.toFixed(0) + " lbf)";
    document.getElementById('res-pf-torque').textContent = T_Nm.toFixed(1) + " N\u00B7m (" + T_ftlb.toFixed(0) + " ft-lb)";
    document.getElementById('res-pf-hoop').textContent = sigma_t_MPa.toFixed(2) + " MPa (Tensile at bore)";
    document.getElementById('res-pf-temp').textContent = "+" + delta_T.toFixed(1) + " \u00B0C above ambient (Bore target: " + target_T.toFixed(0) + " \u00B0C)";
}

document.getElementById('calc-pf-btn').addEventListener('click', computePressFit);
['pf-d', 'pf-d-unit', 'pf-do', 'pf-do-unit', 'pf-di', 'pf-di-unit', 'pf-length', 'pf-length-unit', 'pf-interf', 'pf-interf-unit', 'pf-material', 'pf-fric'].forEach(function(id) {
    document.getElementById(id).addEventListener('input', computePressFit);
    document.getElementById(id).addEventListener('change', computePressFit);
});
window.addEventListener('DOMContentLoaded', computePressFit);
"""

TOOL4_ARTICLE = r"""
<h2>Principles of Interference Press Fits and Shrink Fits</h2>
<p>An interference fit (commonly called a press fit or shrink fit) is a semi-permanent or permanent mechanical assembly technique where a male cylindrical component (shaft or pin) has an outer diameter intentionally manufactured larger than the mating female bore of a hub, gear, pulley, or bearing ring. When assembled, the negative clearance (interference $\delta$) creates mutual elastic deformation: the shaft contracts radially under compression, while the surrounding hub expands outward under tension.</p>

<p>This elastic strain establishes a severe continuous <strong>radial interface contact pressure ($p$)</strong> across the mating boundary. Frictional adhesion between the pressurized micro-asperities of the two mating surfaces allows direct transmission of large torsional twisting moments ($T$) and bidirectional axial thrust loads ($F_{\text{axial}}$) without requiring failure-prone keyways, splines, set screws, or fusion welding.</p>

<h2>Thick-Walled Cylinder Mechanics: Lamé Elasticity Formulations</h2>
<p>To accurately calculate the interface contact pressure, both components are modeled as concentric thick-walled elastic cylinders using Gabriel Lamé's classical 1852 elastostatic boundary value equations.</p>

<p>For a thick-walled cylinder subjected to internal pressure $p_i$ and external pressure $p_o$, radial stress $\sigma_r(r)$ and tangential hoop stress $\sigma_t(r)$ at radius $r$ are:</p>
$$\sigma_r(r) = \frac{p_i r_i^2 - p_o r_o^2}{r_o^2 - r_i^2} - \frac{(p_i - p_o) r_i^2 r_o^2}{r^2 (r_o^2 - r_i^2)}$$
$$\sigma_t(r) = \frac{p_i r_i^2 - p_o r_o^2}{r_o^2 - r_i^2} + \frac{(p_i - p_o) r_i^2 r_o^2}{r^2 (r_o^2 - r_i^2)}$$

<h3>Derivation of Contact Pressure ($p$) from Total Interference ($\delta$)</h3>
<p>At the mating nominal diameter $d = 2r$, the total diametral interference $\delta = d_{\text{shaft}} - d_{\text{hole}}$ is the absolute sum of the radial dilation of the hub bore ($\Delta d_o$) and the radial contraction of the shaft surface ($\Delta d_i$):</p>
$$\delta = |\Delta d_o| + |\Delta d_i|$$

<p>Applying Hooke's generalized plane stress law ($\varepsilon_t = \frac{\Delta d}{d} = \frac{\sigma_t - \nu \sigma_r}{E}$) to both cylinders yields the master press-fit interference relationship:</p>
$$p = \frac{\delta}{d \left[ \frac{1}{E_o}\left( \frac{d_o^2 + d^2}{d_o^2 - d^2} + \nu_o \right) + \frac{1}{E_i}\left( \frac{d^2 + d_i^2}{d^2 - d_i^2} - \nu_i \right) \right]} \quad [\text{Pascals}]$$

<p>Where:</p>
<ul>
    <li><strong>$d$</strong>: Nominal mating contact diameter ($\text{m}$).</li>
    <li><strong>$d_o$</strong>: Outer diameter of the exterior hub ($\text{m}$).</li>
    <li><strong>$d_i$</strong>: Internal bore diameter of a hollow shaft ($d_i = 0$ for a solid solid shaft, simplifying the bracketed shaft term to $\frac{1 - \nu_i}{E_i}$).</li>
    <li><strong>$E_o, E_i$</strong>: Young's Modulus of elasticity of the hub and shaft materials ($\text{Pa}$).</li>
    <li><strong>$\nu_o, \nu_i$</strong>: Poisson's ratio of the hub and shaft materials.</li>
    <li><strong>$\delta$</strong>: Total diametral interference ($\text{m}$).</li>
</ul>

<h2>Load Transmission Capacities: Axial Force and Torque</h2>
<p>Once contact pressure $p$ is established across engagement length $L$, the assembly's frictional load-holding capacity is governed by Coulomb friction with coefficient $\mu$:</p>

<h3>1. Axial Holding Capacity and Insertion Push Force ($F_{\text{axial}}$)</h3>
<p>The total normal force acting across the cylindrical surface area $A_{\text{contact}} = \pi \cdot d \cdot L$ is $N_{\text{total}} = p \cdot \pi \cdot d \cdot L$. The maximum axial force the joint can sustain before slipping (and the required hydraulic ram push-on assembly force) is:</p>
$$F_{\text{axial}} = \mu \cdot p \cdot \pi \cdot d \cdot L \quad [\text{Newtons}]$$

<h3>2. Torsional Torque Capacity ($T_{\text{max}}$)</h3>
<p>Because frictional shear traction acts at radius $r = \frac{d}{2}$, the maximum transmittable torque before angular slippage is:</p>
$$T_{\text{max}} = F_{\text{axial}} \cdot \left( \frac{d}{2} \right) = \frac{1}{2} \mu \cdot p \cdot \pi \cdot d^2 \cdot L \quad [\text{N}\cdot\text{m}]$$

<h2>Peak Tangential Hoop Stress and Hub Rupture Safety</h2>
<p>The most vulnerable region in any interference assembly is the inner bore surface of the hub ($r = d/2$), where tensile tangential hoop stress reaches its maximum value:</p>
$$\sigma_{t,\text{max}} = p \left( \frac{d_o^2 + d^2}{d_o^2 - d^2} \right) \quad [\text{Tensile}]$$

<p>Combining tensile hoop stress with compressive radial stress ($\sigma_r = -p$), the equivalent von Mises stress at the hub bore is:</p>
$$\sigma_{\text{von Mises}} = \sqrt{\sigma_t^2 - \sigma_t \sigma_r + \sigma_r^2} = \sqrt{\sigma_t^2 + \sigma_t p + p^2}$$

<p>To avoid plastic yielding, cracking, or permanent loosening of the joint, the von Mises stress must satisfy $\sigma_{\text{von Mises}} \le \frac{S_{y,\text{hub}}}{\text{FoS}}$.</p>

<h2>Thermal Shrink-Fit Assembly Temperature ($\Delta T$)</h2>
<p>Mechanical press fitting at ambient temperature requires massive hydraulic rams and risks destructive surface galling, scoring, and metal transfer. Thermal shrink fitting bypasses mechanical abrasion by thermally expanding the hub or cryogenic shrinking the shaft.</p>

<p>To provide smooth drop-in assembly with a safe assembly diametral clearance (typically $c = 0.02\text{--}0.05\ \text{mm}$), the required temperature differential $\Delta T$ is:</p>
$$\Delta T = \frac{\delta + c}{\alpha_{\text{hub}} \cdot d} \quad [^\circ\text{C}]$$

<p>Where $\alpha_{\text{hub}}$ is the linear thermal expansion coefficient of the hub material (e.g., $12 \times 10^{-6}\ /^\circ\text{C}$ for carbon steel; $23 \times 10^{-6}\ /^\circ\text{C}$ for aluminum).</p>

<table class="data-table">
    <thead>
        <tr>
            <th>ISO Fit Class</th>
            <th>Type of Fit</th>
            <th>Typical Interference Range</th>
            <th>Primary Application Field</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>H7 / p6</strong></td>
            <td>Light Press Fit</td>
            <td>$0.015\text{--}0.035\ \text{mm}$</td>
            <td>Locating dowels, small gear hubs, non-slip bushings</td>
        </tr>
        <tr>
            <td><strong>H7 / r6</strong></td>
            <td>Medium Drive Fit</td>
            <td>$0.025\text{--}0.055\ \text{mm}$</td>
            <td>Couplings, machine tool pulleys, permanent bearing collars</td>
        </tr>
        <tr>
            <td><strong>H7 / s6</strong></td>
            <td>Heavy Permanent Shrink Fit</td>
            <td>$0.040\text{--}0.090\ \text{mm}$</td>
            <td>Locomotive wheel tires, heavy crane bull gears, turbines</td>
        </tr>
        <tr>
            <td><strong>H7 / u6</strong></td>
            <td>Extreme Force Fit</td>
            <td>$0.060\text{--}0.150\ \text{mm}$</td>
            <td>Maximum torque assemblies, stress relief heat treatment required</td>
        </tr>
    </tbody>
</table>

<div class="worked-example-card">
    <h4>Step-by-Step Engineering Case Study: Heavy Drive Gear on Solid Steel Shaft</h4>
    <p><strong>Scenario:</strong> A steel spur gear hub ($E_o = 207\ \text{GPa}$, $\nu_o = 0.30$, $S_y = 400\ \text{MPa}$) with outer diameter $d_o = 120\ \text{mm}$ and width $L = 75\ \text{mm}$ is shrink-fitted onto a solid steel shaft ($d_i = 0$, $E_i = 207\ \text{GPa}$, $\nu_i = 0.30$) of nominal diameter $d = 60\ \text{mm}$. The total diametral interference is ground to $\delta = 0.050\ \text{mm}$ ($50\ \mu\text{m}$). The interface coefficient of friction is $\mu = 0.15$.</p>
    <div class="step-solution">
        <p><strong>Step 1: Calculate Cylinder Geometric Compliances:</strong></p>
        $$\frac{d_o^2 + d^2}{d_o^2 - d^2} = \frac{120^2 + 60^2}{120^2 - 60^2} = \frac{14400 + 3600}{14400 - 3600} = \frac{18000}{10800} = 1.6667$$
        $$\text{Term}_{\text{hub}} = \frac{1}{207 \times 10^9} [1.6667 + 0.30] = \frac{1.9667}{207 \times 10^9} = 9.501 \times 10^{-12}\ \text{m}^2/\text{N}$$
        $$\text{Term}_{\text{shaft}} = \frac{1}{207 \times 10^9} [1.0 - 0.30] = \frac{0.70}{207 \times 10^9} = 3.382 \times 10^{-12}\ \text{m}^2/\text{N}$$
        <p><strong>Step 2: Determine Interface Contact Pressure ($p$):</strong></p>
        $$p = \frac{\delta}{d (\text{Term}_{\text{hub}} + \text{Term}_{\text{shaft}})} = \frac{0.000050\ \text{m}}{0.060 \times (9.501 + 3.382) \times 10^{-12}}$$
        $$p = \frac{5.0 \times 10^{-5}}{0.060 \times 12.883 \times 10^{-12}} = \frac{5.0 \times 10^{-5}}{7.7298 \times 10^{-13}} = 64.685 \times 10^6\ \text{Pa} = 64.69\ \text{MPa}$$
        <p><strong>Step 3: Calculate Transmittable Torque Capacity ($T_{\text{max}}$):</strong></p>
        $$T_{\text{max}} = \frac{1}{2} \mu \cdot p \cdot \pi \cdot d^2 \cdot L = 0.5 \times 0.15 \times 64.69 \times 10^6 \times \pi \times (0.060)^2 \times 0.075$$
        $$T_{\text{max}} = 4.85175 \times 10^6 \times 3.14159 \times 0.0036 \times 0.075 = 4,115.4\ \text{N}\cdot\text{m}$$
        <p><strong>Step 4: Check Hub Bore Tensile Hoop Stress and Yield Safety:</strong></p>
        $$\sigma_{t,\text{max}} = p \times 1.6667 = 64.69\ \text{MPa} \times 1.6667 = 107.82\ \text{MPa}$$
        $$\sigma_{\text{von Mises}} = \sqrt{107.82^2 + (107.82 \times 64.69) + 64.69^2} = \sqrt{11625 + 6975 + 4185} = \sqrt{22785} = 150.95\ \text{MPa}$$
        $$\text{FoS} = \frac{S_y}{\sigma_{\text{von Mises}}} = \frac{400\ \text{MPa}}{150.95\ \text{MPa}} = 2.65\ \text{(Safe)}$$
        <p><strong>Conclusion:</strong> The joint safely transmits over $4,115\ \text{N}\cdot\text{m}$ of continuous torque with a high safety factor of $2.65$ against hub yielding.</p>
    </div>
</div>

<h2>Frequently Asked Questions (FAQ)</h2>
<div class="faq-section">
    <h3>What is an interference press fit?</h3>
    <p>An interference press fit (or shrink fit) is a permanent or semi-permanent mechanical fastening method where the outer diameter of a shaft is slightly larger than the mating bore diameter of a hub. When forced together, elastic deformation generates intense radial contact pressure, enabling torque and axial load transmission via friction without keys, splines, or welds.</p>

    <h3>How does Lamé's thick-walled cylinder theory apply to press fits?</h3>
    <p>Lamé equations model the radial and tangential hoop stress distributions in thick-walled concentric cylinders. By matching the radial displacement $\delta$ of the inner cylinder (shaft compression) and outer cylinder (hub dilation) at the interface boundary, the exact interfacial contact pressure $p$ is determined.</p>

    <h3>What is the difference between mechanical press fitting and thermal shrink fitting?</h3>
    <p>Mechanical press fitting forces components together at ambient temperature using a hydraulic press, requiring high insertion force and creating galling or scoring risk. Thermal shrink fitting heats the hub (expanding the bore) or cools the shaft in liquid nitrogen/dry ice (shrinking the shaft) to achieve zero-clearance drop-in assembly without mechanical abrasion.</p>

    <h3>What ISO tolerance classes correspond to interference fits?</h3>
    <p>Common ISO interference fits include H7/p6 (light press fit for rigid positioning), H7/r6 (medium drive fit for permanent hubs), and H7/s6 (heavy permanent shrink fit for maximum torque transmission).</p>
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
    generate_tool(TOOL3_SLUG, TOOL3_TITLE, TOOL3_DESC, TOOL3_H1, TOOL3_SHORT, TOOL3_SCHEMA, TOOL3_UI, TOOL3_JS, TOOL3_ARTICLE)
    generate_tool(TOOL4_SLUG, TOOL4_TITLE, TOOL4_DESC, TOOL4_H1, TOOL4_SHORT, TOOL4_SCHEMA, TOOL4_UI, TOOL4_JS, TOOL4_ARTICLE)
