# -*- coding: utf-8 -*-
"""
Generator for Batch 35 - Part 4
Tools:
7. zener-diode-calculator.html
8. lm317-calculator.html
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
                    <a href="index.html">Home</a> &gt; <a href="engineering.html">Engineering &amp; Electronics</a> &gt; <span>{h1}</span>
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
                        <li><a href="voltage-divider-calculator.html">Voltage Divider Calculator</a></li>
                        <li><a href="parallel-resistance-calculator.html">Parallel Resistance Calculator</a></li>
                        <li><a href="capacitor-energy-calculator.html">Capacitor Energy Calculator</a></li>
                        <li><a href="resonant-frequency-calculator.html">Resonant Frequency Calculator</a></li>
                        <li><a href="rc-time-constant-calculator.html">RC Time Constant Calculator</a></li>
                        <li><a href="rl-time-constant-calculator.html">RL Time Constant Calculator</a></li>
                        <li><a href="zener-diode-calculator.html">Zener Diode Calculator</a></li>
                        <li><a href="lm317-calculator.html">LM317 Voltage Regulator</a></li>
                        <li><a href="ohms-law-calculator.html">Ohm's Law Calculator</a></li>
                        <li><a href="frequency-calculator.html">Frequency Calculator</a></li>
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
                    <p>CalcHub delivers rigorous, laboratory-verified computational tools for electrical engineers, physicists, and circuit designers.</p>
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
                    <h4>Voltage Regulators</h4>
                    <ul class="footer-links">
                        <li><a href="zener-diode-calculator.html">Zener Shunt Regulator</a></li>
                        <li><a href="lm317-calculator.html">LM317 Adjustable Linear IC</a></li>
                        <li><a href="voltage-divider-calculator.html">Resistive Divider</a></li>
                        <li><a href="parallel-resistance-calculator.html">Parallel Resistance Network</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 CalcHub. All rights reserved. Precise voltage regulation and thermal dissipation modeling engines.</p>
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
# TOOL 7: zener-diode-calculator.html
# ==============================================================================
TOOL7_SLUG = "zener-diode-calculator"
TOOL7_TITLE = "Zener Diode Calculator - Series Resistor Sizing, Power & Regulation"
TOOL7_DESC = "Calculate Zener diode series current-limiting resistor (Rs), maximum Zener power dissipation (Pz), resistor wattage, and line/load regulation limits."
TOOL7_H1 = "Zener Diode Voltage Regulator Calculator"
TOOL7_SHORT = "Size series current-limiting resistors, verify maximum diode power dissipation, and design robust shunt voltage regulation stages."

TOOL7_SCHEMA = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Zener Diode Calculator",
      "url": "https://calchub.com/zener-diode-calculator.html",
      "description": "Calculates Zener series current-limiting resistor Rs, maximum diode power dissipation Pz, resistor power rating, and regulation margins.",
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
          "name": "What is the difference between Zener breakdown and Avalanche breakdown?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "True Zener breakdown occurs in heavily doped p-n junctions at breakdown voltages below 5.6 V, where quantum mechanical tunneling across an ultra-narrow depletion region allows electrons to cross the forbidden band gap. Avalanche breakdown predominates at voltages above 5.6 V in moderately doped junctions, where high electric fields accelerate carriers to cause impact ionization. Around 5.6 V, both effects possess opposite temperature coefficients, producing near-zero temperature drift."
          }
        },
        {
          "@type": "Question",
          "name": "How do you size the series resistor (Rs) for a Zener diode regulator?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The series resistor must supply sufficient current under minimum input voltage (Vin,min) to feed maximum load current (IL,max) while maintaining the Zener diode above its knee current (Izk): Rs = (Vin,min - Vz) / (IL,max + Izk)."
          }
        },
        {
          "@type": "Question",
          "name": "When does a Zener diode dissipate maximum power?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The Zener diode experiences maximum power dissipation when input voltage reaches its peak (Vin,max) and load current drops to zero (IL = 0, no-load condition). In this case, all series current shunts entirely through the Zener: Pz,max = Vz * ((Vin,max - Vz) / Rs)."
          }
        },
        {
          "@type": "Question",
          "name": "What safety margin is recommended for resistor and Zener power ratings?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A standard engineering de-rating factor of 50% to 100% is strongly advised. For example, if calculated dissipation is 0.35 W, specify at least a 0.5 W or 1.0 W rated component to maintain acceptable operating temperatures."
          }
        }
      ]
    }
  ]
}"""

TOOL7_UI = """
<div class="calc-grid">
    <div class="calc-input-group">
        <label for="zd-vin-min">Minimum Input Voltage ($V_{\\text{in,min}}$):</label>
        <div class="input-with-select">
            <input type="number" id="zd-vin-min" value="10" min="0.1" step="any">
            <select id="zd-vin-min-unit">
                <option value="1" selected>V</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="zd-vin-max">Maximum Input Voltage ($V_{\\text{in,max}}$):</label>
        <div class="input-with-select">
            <input type="number" id="zd-vin-max" value="14" min="0.1" step="any">
            <select id="zd-vin-max-unit">
                <option value="1" selected>V</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="zd-vz">Zener Voltage ($V_Z$):</label>
        <div class="input-with-select">
            <input type="number" id="zd-vz" value="5.1" min="0.1" step="any">
            <select id="zd-vz-unit">
                <option value="1" selected>V</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="zd-il-max">Maximum Load Current ($I_{L,\\text{max}}$):</label>
        <div class="input-with-select">
            <input type="number" id="zd-il-max" value="20" min="0" step="any">
            <select id="zd-il-max-unit">
                <option value="0.001" selected>mA</option>
                <option value="1">A</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="zd-iz-min">Minimum Zener Knee Current ($I_{Z,\\text{min}}$):</label>
        <div class="input-with-select">
            <input type="number" id="zd-iz-min" value="5" min="0.1" step="any">
            <select id="zd-iz-min-unit">
                <option value="0.001" selected>mA</option>
                <option value="1">A</option>
            </select>
        </div>
    </div>
</div>
<button id="calc-zd-btn" class="calc-btn">Calculate Zener Circuit Parameters</button>
<div class="calc-results-card" id="zd-results">
    <h3>Zener Shunt Regulation Metrics</h3>
    <div class="result-row highlight-result">
        <span class="result-label">Recommended Series Resistor ($R_s$):</span>
        <span class="result-val" id="res-zd-rs">196.00 &Omega; (Standard E24: 180 &ndash; 200 &Omega;)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Resistor Power Dissipation ($P_{Rs,\\text{max}}$):</span>
        <span class="result-val" id="res-zd-prs">0.404 W (Specify &ge; 0.5 W or 1.0 W)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Worst-Case Zener Power ($P_{Z,\\text{max}}$ at no load):</span>
        <span class="result-val" id="res-zd-pz">0.232 W (Specify &ge; 0.5 W Zener diode)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Maximum Total Input Current ($I_{S,\\text{max}}$):</span>
        <span class="result-val" id="res-zd-ismax">45.41 mA</span>
    </div>
    <div class="result-row">
        <span class="result-label">Minimum Total Input Current ($I_{S,\\text{min}}$):</span>
        <span class="result-val" id="res-zd-ismin">25.00 mA</span>
    </div>
</div>
"""

TOOL7_JS = """
function computeZener() {
    var vinMin = parseFloat(document.getElementById('zd-vin-min').value);
    var vinMax = parseFloat(document.getElementById('zd-vin-max').value);
    var vz = parseFloat(document.getElementById('zd-vz').value);
    var ilMaxVal = parseFloat(document.getElementById('zd-il-max').value);
    var ilMaxUnit = parseFloat(document.getElementById('zd-il-max-unit').value);
    var izMinVal = parseFloat(document.getElementById('zd-iz-min').value);
    var izMinUnit = parseFloat(document.getElementById('zd-iz-min-unit').value);

    if (isNaN(vinMin) || isNaN(vinMax) || isNaN(vz) || vinMin <= vz || vinMax < vinMin) {
        document.getElementById('res-zd-rs').textContent = "Invalid: Vin,min must exceed Vz";
        return;
    }

    var ilMax = (isNaN(ilMaxVal) || ilMaxVal < 0) ? 0 : ilMaxVal * ilMaxUnit; // Amperes
    var izMin = (isNaN(izMinVal) || izMinVal <= 0) ? 0.005 : izMinVal * izMinUnit; // Amperes

    // Sizing Rs: Rs = (Vin,min - Vz) / (IL,max + Iz,min)
    var isMinReq = ilMax + izMin;
    var Rs = (vinMin - vz) / isMinReq; // Ohms

    // Maximum current under Vin,max
    var isMax = (vinMax - vz) / Rs; // Amperes

    // Resistor power dissipation at Vin,max
    var prsMax = Math.pow(vinMax - vz, 2) / Rs; // Watts

    // Worst-case Zener dissipation (occurs when Vin = Vin,max and IL = 0, no-load)
    var pzMax = vz * isMax; // Watts

    // Output formatted results
    document.getElementById('res-zd-rs').textContent = Rs.toFixed(2) + " \u03A9";
    document.getElementById('res-zd-prs').textContent = prsMax.toFixed(3) + " W (Use \u2265 " + (prsMax * 1.5).toFixed(2) + " W rated)";
    document.getElementById('res-zd-pz').textContent = pzMax.toFixed(3) + " W (Use \u2265 " + (pzMax * 1.5).toFixed(2) + " W rated)";
    document.getElementById('res-zd-ismax').textContent = (isMax * 1000).toFixed(2) + " mA";
    document.getElementById('res-zd-ismin').textContent = (isMinReq * 1000).toFixed(2) + " mA";
}

document.getElementById('calc-zd-btn').addEventListener('click', computeZener);
['zd-vin-min', 'zd-vin-max', 'zd-vz', 'zd-il-max', 'zd-il-max-unit', 'zd-iz-min', 'zd-iz-min-unit'].forEach(function(id) {
    document.getElementById(id).addEventListener('input', computeZener);
    document.getElementById(id).addEventListener('change', computeZener);
});
window.addEventListener('DOMContentLoaded', computeZener);
"""

TOOL7_ARTICLE = r"""
<h2>Zener Diode Fundamentals: Quantum Tunneling vs Avalanche Breakdown</h2>
<p>A Zener diode is a specialized silicon p-n junction diode engineered to operate stably in the reverse-bias breakdown breakdown regime. Under forward bias, it exhibits standard diode conduction with a forward threshold drop ($V_F \approx 0.7\text{ V}$). Under reverse bias below its critical threshold, only a tiny reverse leakage current flows ($I_R \sim \text{nA}$). However, once reverse potential surpasses the breakdown threshold ($V_Z$), the diode enters a highly conductive state characterized by an extremely steep current-voltage ($I\text{-}V$) curve, maintaining an almost invariant clamp voltage across wide ranges of reverse current.</p>

<p>Two distinct quantum and solid-state phenomena govern this breakdown behavior depending on junction doping concentration and physical barrier thickness:</p>

<ul>
    <li><strong>Quantum Mechanical Zener Tunneling ($V_Z < 5.6\text{ V}$):</strong> In heavily doped silicon junctions, the depletion region barrier width is extraordinarily narrow (often less than $10\text{ nm}$). The resulting electric field gradient exceeds $10^6\text{ V/m}$, allowing valence band electrons to quantum mechanically tunnel directly across the forbidden energy bandgap into empty conduction band states without kinetic collision. This true Zener mechanism possesses a <em>negative temperature coefficient</em> (as crystal lattice temperature rises, bandgap energy decreases, causing breakdown voltage to slightly decrease).</li>
    <li><strong>Avalanche Impact Ionization ($V_Z > 5.6\text{ V}$):</strong> In moderately doped silicon junctions with wider depletion regions, free thermally generated carriers accelerate to massive kinetic velocities under high reverse electric fields. When these energetic carriers collide with stationary crystal lattice atoms, they liberate secondary electron-hole pairs through impact ionization. These newly created carriers accelerate in turn, triggering an exponential multiplicative avalanche cascade. Avalanche breakdown exhibits a <em>positive temperature coefficient</em> (increased thermal lattice vibrations scatter electrons, shortening mean free path and requiring higher potential to trigger avalanche).</li>
    <li><strong>Zero-Temperature-Coefficient Crossover ($V_Z \approx 5.6\text{ V}$):</strong> Near nominal $5.6\text{ V}$, the negative temperature coefficient of quantum tunneling precisely cancels the positive temperature coefficient of avalanche multiplication. Precision voltage reference diodes (such as the 1N821 family) intentionally operate at $5.6\text{--}6.2\text{ V}$ to achieve sub-$5\text{ ppm/}^\circ\text{C}$ temperature stability.</li>
</ul>

<h2>Mathematical Design Equations for Shunt Zener Regulation</h2>
<p>A basic shunt regulator consists of an unregulated input voltage rail ($V_{\text{in}}$), a series current-limiting resistor ($R_s$), a Zener diode ($V_Z$), and a parallel load resistance ($R_L$) drawing load current ($I_L$). The circuit must maintain voltage regulation under extreme supply and load fluctuations.</p>

<h3>1. Sizing Series Resistor $R_s$ Under Worst-Case Minimum Rail</h3>
<p>To guarantee that the Zener diode does not fall out of regulation into high-impedance cutoff, the current through the diode must never drop below its minimum knee test current ($I_{Z,\text{min}}$ or $I_{ZK}$, typically $1\text{--}5\text{ mA}$). The worst-case condition for maintaining regulation occurs when the input voltage is at its lowest ($V_{\text{in,min}}$) and the external load current is at its maximum ($I_{L,\text{max}}$):</p>
$$I_{S,\text{min}} = I_{L,\text{max}} + I_{Z,\text{min}}$$
$$R_{s,\text{max}} = \frac{V_{\text{in,min}} - V_Z}{I_{L,\text{max}} + I_{Z,\text{min}}}$$

<p>If $R_s$ exceeds this value, supply voltage droop or heavy load transients will pull the output voltage below $V_Z$, extinguishing Zener conduction.</p>

<h3>2. Worst-Case Power Dissipation in the Zener Diode ($P_{Z,\text{max}}$)</h3>
<p>Conversely, maximum electrical stress occurs under maximum input voltage ($V_{\text{in,max}}$) when the load is suddenly disconnected ($I_L = 0$, open-circuit no-load condition). Under this scenario, the entire current flowing through $R_s$ is shunted through the Zener diode:</p>
$$I_{Z,\text{max}} = I_{S,\text{max}} = \frac{V_{\text{in,max}} - V_Z}{R_s}$$
$$P_{Z,\text{max}} = V_Z \cdot I_{Z,\text{max}} = V_Z \left( \frac{V_{\text{in,max}} - V_Z}{R_s} \right)$$

<p>The chosen Zener diode component must have a continuous power rating $P_{Z,\text{rated}} \ge 1.5 \times P_{Z,\text{max}}$ to ensure junction temperatures remain within safe semiconductor operating margins.</p>

<h3>3. Series Resistor Power Dissipation ($P_{Rs,\text{max}}$)</h3>
<p>The series resistor continuously dissipates ohmic heat:
$$P_{Rs,\text{max}} = I_{S,\text{max}}^2 \cdot R_s = \frac{(V_{\text{in,max}} - V_Z)^2}{R_s}$$
Engineers must select a power resistor (e.g., $1\text{ W}$, $2\text{ W}$, or $5\text{ W}$ wirewound/metal oxide) to prevent thermal degradation and solder joint fatigue.</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Standard Zener Family</th>
            <th>Power Rating ($P_D$)</th>
            <th>Typical Package</th>
            <th>Knee Current ($I_{ZK}$)</th>
            <th>Dynamic Impedance ($Z_Z$)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>BZX84C Series</strong></td>
            <td>$350\text{ mW}$</td>
            <td>SOT-23 Surface Mount</td>
            <td>$1.0\text{--}5.0\text{ mA}$</td>
            <td>$10\text{--}80\ \Omega$</td>
        </tr>
        <tr>
            <td><strong>BZX55C Series</strong></td>
            <td>$500\text{ mW}$</td>
            <td>DO-35 Glass Axial</td>
            <td>$1.0\text{--}5.0\text{ mA}$</td>
            <td>$7\text{--}50\ \Omega$</td>
        </tr>
        <tr>
            <td><strong>1N4728A &ndash; 1N4764A</strong></td>
            <td>$1.0\text{ W}$</td>
            <td>DO-41 Plastic Axial</td>
            <td>$0.25\text{--}1.0\text{ mA}$</td>
            <td>$2\text{--}30\ \Omega$</td>
        </tr>
        <tr>
            <td><strong>1N5333B &ndash; 1N5388B</strong></td>
            <td>$5.0\text{ W}$</td>
            <td>Axial Leaded Power Case</td>
            <td>$1.0\text{ mA}$</td>
            <td>$1\text{--}15\ \Omega$</td>
        </tr>
    </tbody>
</table>

<h2>Line Regulation, Load Regulation, and Dynamic Impedance ($Z_Z$)</h2>
<p>A real Zener diode is not an ideal zero-impedance battery; it possesses an incremental dynamic resistance $Z_Z = \frac{\Delta V_Z}{\Delta I_Z}$ (ranging from $2\ \Omega$ to $100\ \Omega$). Consequently, variations in input voltage and load current cause minor shifts in output voltage:</p>
<ul>
    <li><strong>Line Regulation (Input Ripple Rejection):</strong> The fraction of input voltage ripple $\Delta V_{\text{in}}$ that reaches the load is governed by the voltage divider formed by $R_s$ and $Z_Z$:
    $$\frac{\Delta V_{\text{out}}}{\Delta V_{\text{in}}} = \frac{Z_Z}{R_s + Z_Z}$$
    Because $R_s \gg Z_Z$, input ripple is typically attenuated by $20\text{--}40\text{ dB}$.</li>
    <li><strong>Load Regulation:</strong> When load current jumps by $\Delta I_L$, diode current drops by approximately the same amount, causing a change in output voltage $\Delta V_{\text{out}} \approx -\Delta I_L \cdot Z_Z$.</li>
</ul>

<div class="worked-example-card">
    <h4>Step-by-Step Engineering Case Study: 5.1V Microcontroller Auxiliary Rail</h4>
    <p><strong>Scenario:</strong> An industrial PLC auxiliary line delivers an unregulated DC supply varying between $V_{\text{in,min}} = 11.5\text{ V}$ and $V_{\text{in,max}} = 15.0\text{ V}$. An auxiliary microcontroller board requires a stabilized $V_Z = 5.1\text{ V}$ with a load current drawing between $I_{L,\text{min}} = 5\text{ mA}$ and $I_{L,\text{max}} = 25\text{ mA}$. A 1N4733A Zener diode ($5.1\text{ V}$, $1.0\text{ W}$) with a minimum knee current of $I_{Z,\text{min}} = 5.0\text{ mA}$ is selected.</p>
    <div class="step-solution">
        <p><strong>Step 1: Calculate Maximum Series Resistor ($R_s$):</strong></p>
        $$I_{S,\text{min}} = I_{L,\text{max}} + I_{Z,\text{min}} = 25\text{ mA} + 5.0\text{ mA} = 30.0\text{ mA} = 0.030\text{ A}$$
        $$R_s = \frac{V_{\text{in,min}} - V_Z}{I_{S,\text{min}}} = \frac{11.5\text{ V} - 5.1\text{ V}}{0.030\text{ A}} = \frac{6.4\text{ V}}{0.030\text{ A}} = 213.33\ \Omega$$
        <p>Selecting the nearest lower standard E24 resistor ensures adequate current: $R_s = 200\ \Omega$.</p>
        <p><strong>Step 2: Calculate Maximum Loop Current at $V_{\text{in,max}}$:</strong></p>
        $$I_{S,\text{max}} = \frac{V_{\text{in,max}} - V_Z}{R_s} = \frac{15.0\text{ V} - 5.1\text{ V}}{200\ \Omega} = \frac{9.9\text{ V}}{200\ \Omega} = 0.0495\text{ A} = 49.5\text{ mA}$$
        <p><strong>Step 3: Determine Worst-Case Zener Power Dissipation (No Load, $I_L = 0$):</strong></p>
        $$P_{Z,\text{max}} = V_Z \cdot I_{S,\text{max}} = 5.1\text{ V} \times 0.0495\text{ A} = 0.2525\text{ W} = 252.5\text{ mW}$$
        <p>The $1.0\text{ W}$ rated 1N4733A operates with a generous $75\%$ safety margin ($P_D / P_{\text{rated}} = 0.25$).</p>
        <p><strong>Step 4: Sizing Resistor Wattage:</strong></p>
        $$P_{Rs,\text{max}} = I_{S,\text{max}}^2 \cdot R_s = (0.0495\text{ A})^2 \times 200\ \Omega = 0.00245 \times 200 = 0.490\text{ W}$$
        <p><strong>Conclusion:</strong> A standard $0.25\text{ W}$ resistor would overheat and burn out. A $1.0\text{ W}$ metal oxide $200\ \Omega$ resistor must be installed.</p>
    </div>
</div>

<h2>Frequently Asked Questions (FAQ)</h2>
<div class="faq-section">
    <h3>What is the difference between Zener breakdown and Avalanche breakdown?</h3>
    <p>True Zener breakdown occurs in heavily doped p-n junctions at breakdown voltages below $5.6\text{ V}$, where quantum mechanical tunneling across an ultra-narrow depletion region allows electrons to cross the forbidden band gap. Avalanche breakdown predominates at voltages above $5.6\text{ V}$ in moderately doped junctions, where high electric fields accelerate carriers to cause impact ionization. Around $5.6\text{ V}$, both effects possess opposite temperature coefficients, producing near-zero temperature drift.</p>

    <h3>How do you size the series resistor ($R_s$) for a Zener diode regulator?</h3>
    <p>The series resistor must supply sufficient current under minimum input voltage ($V_{\text{in,min}}$) to feed maximum load current ($I_{L,\text{max}}$) while maintaining the Zener diode above its knee current ($I_{ZK}$): $R_s = \frac{V_{\text{in,min}} - V_Z}{I_{L,\text{max}} + I_{Z,\text{min}}}$.</p>

    <h3>When does a Zener diode dissipate maximum power?</h3>
    <p>The Zener diode experiences maximum power dissipation when input voltage reaches its peak ($V_{\text{in,max}}$) and load current drops to zero ($I_L = 0$, no-load condition). In this case, all series current shunts entirely through the Zener: $P_{Z,\text{max}} = V_Z \cdot \left(\frac{V_{\text{in,max}} - V_Z}{R_s}\right)$.</p>

    <h3>What safety margin is recommended for resistor and Zener power ratings?</h3>
    <p>A standard engineering de-rating factor of $50\%$ to $100\%$ is strongly advised. For example, if calculated dissipation is $0.35\text{ W}$, specify at least a $0.5\text{ W}$ or $1.0\text{ W}$ rated component to maintain acceptable operating temperatures.</p>
</div>
"""

# ==============================================================================
# TOOL 8: lm317-calculator.html
# ==============================================================================
TOOL8_SLUG = "lm317-calculator"
TOOL8_TITLE = "LM317 Voltage Regulator Calculator - Resistors R1 & R2, Power & Heatsink"
TOOL8_DESC = "Calculate LM317 output voltage (Vout = 1.25*(1 + R2/R1) + Iadj*R2), feedback resistors, thermal dissipation (Pd), and required heatsink thermal resistance."
TOOL8_H1 = "LM317 Voltage Regulator Calculator"
TOOL8_SHORT = "Calculate output voltage, feedback divider resistors (R1, R2), internal power dissipation, and thermal heatsink requirements for the LM317 IC."

TOOL8_SCHEMA = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "LM317 Voltage Regulator Calculator",
      "url": "https://calchub.com/lm317-calculator.html",
      "description": "Calculates LM317 adjustable positive linear regulator output voltage, resistor divider network, thermal dissipation, and heatsink thermal resistance.",
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
          "name": "How does the LM317 regulate its output voltage?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The LM317 maintains an internal temperature-compensated 1.25 V bandgap reference voltage (Vref) between its OUT and ADJ terminals. By forcing this fixed 1.25 V across programming resistor R1, a constant reference current flows into resistor R2, developing an output voltage: Vout = Vref * (1 + R2 / R1) + Iadj * R2."
          }
        },
        {
          "@type": "Question",
          "name": "Why is R1 commonly chosen as 240 ohms or 120 ohms?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The LM317 requires a minimum operating load current (typically 3.5 mA to 10 mA) to maintain stable regulation under all temperature conditions. With Vref = 1.25 V, setting R1 = 120 ohms guarantees a baseline current of 10.4 mA, while R1 = 240 ohms guarantees 5.2 mA, satisfying the minimum load specification without requiring an external load."
          }
        },
        {
          "@type": "Question",
          "name": "What is the dropout voltage of the LM317?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The LM317 requires an input-to-output voltage differential (Vin - Vout) of at least 1.5 V to 2.5 V depending on load current and junction temperature to keep its internal Darlington pass transistor in active regulation."
          }
        },
        {
          "@type": "Question",
          "name": "Why are protection diodes recommended in LM317 circuits?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "If input power is abruptly grounded while large capacitors exist at the output or ADJ pin, reverse current flows into the regulator's internal transistors. Diode D1 across OUT-to-IN and diode D2 across ADJ-to-OUT safely divert discharge currents away from internal junctions."
          }
        }
      ]
    }
  ]
}"""

TOOL8_UI = """
<div class="calc-grid">
    <div class="calc-input-group">
        <label for="lm-mode">Calculation Mode:</label>
        <select id="lm-mode">
            <option value="vout" selected>Solve Output Voltage ($V_{\\text{out}}$) from Resistors</option>
            <option value="r2">Solve Required Resistor $R_2$ from Desired $V_{\\text{out}}$</option>
        </select>
    </div>
    <div class="calc-input-group">
        <label for="lm-vin">Input Voltage ($V_{\\text{in}}$):</label>
        <div class="input-with-select">
            <input type="number" id="lm-vin" value="12" min="1.5" step="any">
            <select id="lm-vin-unit">
                <option value="1" selected>V</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group" id="grp-lm-r1">
        <label for="lm-r1">Resistor $R_1$ (Standard 240 or 120 &Omega;):</label>
        <div class="input-with-select">
            <input type="number" id="lm-r1" value="240" min="1" step="any">
            <select id="lm-r1-unit">
                <option value="1" selected>&Omega;</option>
                <option value="1000">k&Omega;</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group" id="grp-lm-r2">
        <label for="lm-r2">Resistor $R_2$:</label>
        <div class="input-with-select">
            <input type="number" id="lm-r2" value="720" min="0" step="any">
            <select id="lm-r2-unit">
                <option value="1" selected>&Omega;</option>
                <option value="1000">k&Omega;</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group" id="grp-lm-target-vout" style="display:none;">
        <label for="lm-target-vout">Desired Output Voltage ($V_{\\text{out}}$):</label>
        <div class="input-with-select">
            <input type="number" id="lm-target-vout" value="5.0" min="1.25" step="any">
            <select id="lm-target-vout-unit">
                <option value="1" selected>V</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="lm-il">Load Current ($I_L$):</label>
        <div class="input-with-select">
            <input type="number" id="lm-il" value="500" min="0" step="any">
            <select id="lm-il-unit">
                <option value="0.001" selected>mA</option>
                <option value="1">A</option>
            </select>
        </div>
    </div>
</div>
<button id="calc-lm-btn" class="calc-btn">Calculate LM317 Parameters</button>
<div class="calc-results-card" id="lm-results">
    <h3>LM317 Regulation &amp; Thermal Analysis</h3>
    <div class="result-row highlight-result">
        <span class="result-label">Output Voltage ($V_{\\text{out}}$):</span>
        <span class="result-val" id="res-lm-vout">5.04 V</span>
    </div>
    <div class="result-row">
        <span class="result-label">Resistor $R_2$ Value:</span>
        <span class="result-val" id="res-lm-r2-val">720.0 &Omega;</span>
    </div>
    <div class="result-row">
        <span class="result-label">Input-to-Output Voltage Headroom ($V_{\\text{in}} - V_{\\text{out}}$):</span>
        <span class="result-val" id="res-lm-vdiff">6.96 V (&ge; 2.0 V Dropout OK)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Regulator Internal Power Dissipation ($P_D$):</span>
        <span class="result-val" id="res-lm-pd">3.48 W</span>
    </div>
    <div class="result-row">
        <span class="result-label">Thermal Management Requirement:</span>
        <span class="result-val" id="res-lm-thermal">Heatsink Required (&theta;SA &le; 24.6 &deg;C/W)</span>
    </div>
</div>
"""

TOOL8_JS = """
function updateLmMode() {
    var mode = document.getElementById('lm-mode').value;
    document.getElementById('grp-lm-r2').style.display = (mode === 'r2') ? 'none' : 'block';
    document.getElementById('grp-lm-target-vout').style.display = (mode === 'vout') ? 'none' : 'block';
}

function computeLm317() {
    var mode = document.getElementById('lm-mode').value;
    var vin = parseFloat(document.getElementById('lm-vin').value);
    var r1Val = parseFloat(document.getElementById('lm-r1').value);
    var r1Unit = parseFloat(document.getElementById('lm-r1-unit').value);
    var r2Val = parseFloat(document.getElementById('lm-r2').value);
    var r2Unit = parseFloat(document.getElementById('lm-r2-unit').value);
    var targetVout = parseFloat(document.getElementById('lm-target-vout').value);
    var ilVal = parseFloat(document.getElementById('lm-il').value);
    var ilUnit = parseFloat(document.getElementById('lm-il-unit').value);

    var Vref = 1.25; // Volts
    var Iadj = 50e-6; // 50 microamperes

    if (isNaN(vin) || isNaN(r1Val) || r1Val <= 0) return;
    var R1 = r1Val * r1Unit;
    var IL = (isNaN(ilVal) || ilVal < 0) ? 0.1 : ilVal * ilUnit;

    var Vout = 0;
    var R2 = 0;

    if (mode === 'vout') {
        if (isNaN(r2Val) || r2Val < 0) return;
        R2 = r2Val * r2Unit;
        Vout = Vref * (1.0 + R2 / R1) + (Iadj * R2);
    } else {
        if (isNaN(targetVout) || targetVout < Vref) return;
        Vout = targetVout;
        // Target Vout = Vref * (1 + R2/R1) + Iadj * R2 = Vref + R2 * (Vref/R1 + Iadj)
        // R2 = (Vout - Vref) / (Vref / R1 + Iadj)
        R2 = (Vout - Vref) / ((Vref / R1) + Iadj);
        document.getElementById('lm-r2').value = R2.toFixed(1);
    }

    var vdiff = vin - Vout;

    // Display Vout
    document.getElementById('res-lm-vout').textContent = Vout.toFixed(2) + " V";
    document.getElementById('res-lm-r2-val').textContent = R2.toFixed(1) + " \u03A9";

    // Headroom check
    if (vdiff < 1.5) {
        document.getElementById('res-lm-vdiff').textContent = vdiff.toFixed(2) + " V (WARNING: Insufficient Headroom, Dropout < 1.5 V)";
    } else if (vdiff < 2.0) {
        document.getElementById('res-lm-vdiff').textContent = vdiff.toFixed(2) + " V (Marginal Headroom, near dropout limit)";
    } else {
        document.getElementById('res-lm-vdiff').textContent = vdiff.toFixed(2) + " V (Adequate Headroom, \u2265 2.0 V OK)";
    }

    // Power dissipation Pd = (Vin - Vout) * IL + Vin * Iadj
    var Pd = (vdiff * IL) + (vin * Iadj);
    document.getElementById('res-lm-pd').textContent = Pd.toFixed(3) + " W";

    // Heatsink estimation for TO-220 package (Rth_JC = 4 C/W, Rth_JA = 50 C/W, T_ambient = 25 C, T_jmax = 125 C)
    var Tj_noHeatsink = 25.0 + (Pd * 50.0);
    if (Pd <= 0.5) {
        document.getElementById('res-lm-thermal').textContent = "No Heatsink Needed (Free air Tj \u2248 " + Tj_noHeatsink.toFixed(0) + " \u00B0C)";
    } else if (Pd <= 1.0) {
        document.getElementById('res-lm-thermal').textContent = "Small PCB Copper Area or Clip-on Heatsink Recommended";
    } else {
        // Required theta_SA = (Tjmax - Tamb) / Pd - (Rth_JC + Rth_CS)
        // Let Tjmax = 100 C (conservative), Tamb = 35 C, Rth_JC = 4 C/W, Rth_CS = 1 C/W
        var theta_sa = ((100.0 - 35.0) / Pd) - 5.0;
        if (theta_sa > 0) {
            document.getElementById('res-lm-thermal').textContent = "Heatsink Required (\u03B8SA \u2264 " + theta_sa.toFixed(1) + " \u00B0C/W)";
        } else {
            document.getElementById('res-lm-thermal').textContent = "CRITICAL: Power Dissipation Excessive for Single TO-220 (" + Pd.toFixed(1) + " W)";
        }
    }
}

document.getElementById('lm-mode').addEventListener('change', function() {
    updateLmMode();
    computeLm317();
});
document.getElementById('calc-lm-btn').addEventListener('click', computeLm317);
['lm-vin', 'lm-r1', 'lm-r1-unit', 'lm-r2', 'lm-r2-unit', 'lm-target-vout', 'lm-il', 'lm-il-unit'].forEach(function(id) {
    document.getElementById(id).addEventListener('input', computeLm317);
    document.getElementById(id).addEventListener('change', computeLm317);
});
window.addEventListener('DOMContentLoaded', function() {
    updateLmMode();
    computeLm317();
});
"""

TOOL8_ARTICLE = r"""
<h2>Architecture of the LM317 Adjustable Linear Voltage Regulator</h2>
<p>The LM317 is a monolithic three-terminal adjustable positive linear voltage regulator designed by Robert C. Dobkin at National Semiconductor in 1976. Widely considered one of the most versatile analog integrated circuits in electronics history, it delivers over $1.5\text{ A}$ of load current across an adjustable output range spanning $1.25\text{ V}$ to $37\text{ V}$.</p>

<p>Unlike classic fixed-voltage linear regulators (e.g., the 7805 or 7812) that reference their control circuitry to an external chassis ground pin, the LM317 possesses no physical ground terminal. Instead, its internal error amplifier and temperature-compensated bandgap voltage reference float between the <strong>OUTPUT ($V_{\text{out}}$)</strong> terminal and the <strong>ADJUST ($\text{ADJ}$)</strong> terminal, maintaining a precision potential of:</p>
$$V_{\text{ref}} = 1.25\text{ V} \quad (\text{Nominal: } 1.20\text{--}1.30\text{ V})$$

<p>Because the regulator floats on the output voltage, the differential voltage experienced across the silicon pass transistor is simply $(V_{\text{in}} - V_{\text{out}})$. As long as this differential limit ($40\text{ V}$ standard, $60\text{ V}$ for the LM317HV) is not breached, the LM317 can regulate high-voltage supplies safely.</p>

<h2>Derivation of the Output Voltage Equation</h2>
<p>The programming network consists of two external resistors: $R_1$ placed between OUT and ADJ, and $R_2$ connected between ADJ and ground.</p>

<p>Because the IC strictly maintains $V_{\text{ref}} = 1.25\text{ V}$ across $R_1$, a constant reference current $I_1$ flows down through $R_1$:</p>
$$I_1 = \frac{V_{\text{ref}}}{R_1}$$

<p>At the ADJ terminal node, Kirchhoff's Current Law (KCL) dictates that the total current flowing through resistor $R_2$ to ground is the sum of reference current $I_1$ and internal bias adjustment current $I_{\text{adj}}$:</p>
$$I_2 = I_1 + I_{\text{adj}} = \frac{V_{\text{ref}}}{R_1} + I_{\text{adj}}$$

<p>The total output voltage $V_{\text{out}}$ is the sum of the potential across $R_1$ and the potential across $R_2$:</p>
$$V_{\text{out}} = V_{\text{ref}} + I_2 \cdot R_2 = V_{\text{ref}} + \left( \frac{V_{\text{ref}}}{R_1} + I_{\text{adj}} \right) R_2$$
$$V_{\text{out}} = V_{\text{ref}} \left( 1 + \frac{R_2}{R_1} \right) + I_{\text{adj}} \cdot R_2$$

<p>In typical components, $I_{\text{adj}}$ is held to a tightly controlled nominal value of $50\ \mu\text{A}$ ($100\ \mu\text{A}$ maximum). When $R_1$ is sized so that $I_1 \ge 5\text{ mA}$, the term $I_{\text{adj}} \cdot R_2$ represents an error smaller than $1\%$, allowing the simplified approximation:</p>
$$V_{\text{out}} \approx 1.25 \left( 1 + \frac{R_2}{R_1} \right)$$

<h3>Why is $R_1$ Standardized at $240\ \Omega$ or $120\ \Omega$?</h3>
<p>All linear regulators require a <strong>minimum load current ($I_{L,\text{min}}$)</strong> to sustain internal biasing and prevent the output voltage from floating up to the unregulated input rail under no-load conditions. The LM317 datasheet specifies a maximum required minimum load current of $3.5\text{ mA}$ (commercial grade) to $10\text{ mA}$ (military/extreme temperature grade).</p>
<ul>
    <li>With $R_1 = 240\ \Omega$: $I_1 = \frac{1.25\text{ V}}{240\ \Omega} = 5.21\text{ mA}$. This satisfies the $3.5\text{ mA}$ requirement for all standard operating temperatures.</li>
    <li>With $R_1 = 120\ \Omega$: $I_1 = \frac{1.25\text{ V}}{120\ \Omega} = 10.42\text{ mA}$. This satisfies the strictest $10\text{ mA}$ worst-case military specification.</li>
</ul>

<h2>Thermal Power Dissipation ($P_D$) and Heatsink Thermal Resistance Calculation</h2>
<p>Linear regulators operate by dropping excess voltage across an internal series Darlington pass transistor, converting the product of voltage differential and load current directly into waste heat. Total internal power dissipation $P_D$ is:</p>
$$P_D = (V_{\text{in}} - V_{\text{out}}) \cdot I_L + V_{\text{in}} \cdot I_{\text{adj}} \approx (V_{\text{in}} - V_{\text{out}}) \cdot I_L$$

<p>To prevent the silicon die from exceeding its maximum safe junction temperature ($T_{J,\text{max}} = 125^\circ\text{C}$ to $150^\circ\text{C}$), the thermal impedance chain from junction to ambient air must satisfy:</p>
$$T_J = T_A + P_D \cdot \theta_{JA}$$
$$\theta_{JA} = \theta_{JC} + \theta_{CS} + \theta_{SA}$$

<p>Where:</p>
<ul>
    <li><strong>$T_A$</strong>: Maximum expected ambient temperature ($^\circ\text{C}$).</li>
    <li><strong>$\theta_{JC}$</strong>: Junction-to-case thermal resistance (typically $4.0^\circ\text{C/W}$ for a standard TO-220 package).</li>
    <li><strong>$\theta_{CS}$</strong>: Case-to-heatsink mounting interface thermal resistance (typically $0.5\text{--}1.0^\circ\text{C/W}$ with silicone thermal grease and mica insulator).</li>
    <li><strong>$\theta_{SA}$</strong>: Required heatsink-to-ambient thermal resistance ($^\circ\text{C/W}$).</li>
</ul>

<p>Solving for the maximum permissible heatsink thermal resistance:</p>
$$\theta_{SA} \le \frac{T_{J,\text{max}} - T_A}{P_D} - (\theta_{JC} + \theta_{CS})$$

<table class="data-table">
    <thead>
        <tr>
            <th>Package Type</th>
            <th>Max Current ($I_{\text{max}}$)</th>
            <th>$\theta_{JC}$ (Junction-to-Case)</th>
            <th>$\theta_{JA}$ (Free Air, No Heatsink)</th>
            <th>Max Uncooled Dissipation ($25^\circ\text{C}$)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>TO-220 (LM317T)</strong></td>
            <td>$1.5\text{ A}$</td>
            <td>$4.0^\circ\text{C/W}$</td>
            <td>$50^\circ\text{C/W}$</td>
            <td>$1.5\text{--}2.0\text{ W}$</td>
        </tr>
        <tr>
            <td><strong>TO-3 (LM317K Metal Can)</strong></td>
            <td>$1.5\text{ A}$</td>
            <td>$2.3^\circ\text{C/W}$</td>
            <td>$35^\circ\text{C/W}$</td>
            <td>$2.5\text{--}3.0\text{ W}$</td>
        </tr>
        <tr>
            <td><strong>D2PAK / TO-263 (Surface Mount)</strong></td>
            <td>$1.5\text{ A}$</td>
            <td>$4.0^\circ\text{C/W}$</td>
            <td>$45^\circ\text{C/W}$ (On 1-inch copper pad)</td>
            <td>$1.8\text{ W}$</td>
        </tr>
        <tr>
            <td><strong>SOT-223 (LM317M, 500mA)</strong></td>
            <td>$0.5\text{ A}$</td>
            <td>$15^\circ\text{C/W}$</td>
            <td>$100^\circ\text{C/W}$</td>
            <td>$0.7\text{--}1.0\text{ W}$</td>
        </tr>
    </tbody>
</table>

<h2>Protection Diodes and Ripple Rejection Capacitor Optimization</h2>
<p>To achieve high power supply rejection ratio (PSRR) and ensure fail-safe operation, two external design practices are essential:</p>
<ul>
    <li><strong>ADJ Bypass Capacitor ($C_{\text{adj}}$):</strong> Placing a $10\ \mu\text{F}$ capacitor across resistor $R_2$ bypasses the feedback divider ripple at AC, boosting ripple rejection from $65\text{ dB}$ to an exceptional $80\text{ dB}$ (a $10\times$ improvement in 100/120 Hz mains hum attenuation).</li>
    <li><strong>Reverse Protection Diode $D_1$ (OUT to IN):</strong> When the input power supply is turned off, input capacitors discharge faster than large output filter capacitors ($C_{\text{out}}$). Without protection, current flows backwards from OUT into the internal collector, destroying the series pass transistor. Diode $D_1$ (1N4002 or 1N4007) clamps reverse voltage to $0.7\text{ V}$.</li>
    <li><strong>Discharge Protection Diode $D_2$ (ADJ to OUT):</strong> When bypass capacitor $C_{\text{adj}}$ is utilized, an abrupt output short-circuit will dump $C_{\text{adj}}$ energy back into the ADJ pin. Diode $D_2$ discharges $C_{\text{adj}}$ safely through the load.</li>
</ul>

<div class="worked-example-card">
    <h4>Step-by-Step Engineering Case Study: 9.0V Precision Benchtop Supply</h4>
    <p><strong>Scenario:</strong> Design a regulated $V_{\text{out}} = 9.0\text{ V}$ benchtop supply delivering up to $I_L = 800\text{ mA}$ from an unregulated DC rectified rail of $V_{\text{in}} = 15.0\text{ V}$. An LM317T in a TO-220 package ($\theta_{JC} = 4.0^\circ\text{C/W}$) is used. Ambient operating temperature is $T_A = 40^\circ\text{C}$ and junction limit is set conservatively to $T_{J,\text{max}} = 110^\circ\text{C}$.</p>
    <div class="step-solution">
        <p><strong>Step 1: Choose $R_1$ and Solve for $R_2$:</strong></p>
        <p>Select standard precision metal film resistor $R_1 = 240\ \Omega$.</p>
        $$R_2 = \frac{V_{\text{out}} - V_{\text{ref}}}{\frac{V_{\text{ref}}}{R_1} + I_{\text{adj}}} = \frac{9.0\text{ V} - 1.25\text{ V}}{\frac{1.25\text{ V}}{240\ \Omega} + 50 \times 10^{-6}\text{ A}} = \frac{7.75\text{ V}}{0.0052083 + 0.000050} = \frac{7.75}{0.0052583} = 1,473.8\ \Omega$$
        <p>Select standard E96 precision value $R_2 = 1.47\ \text{k}\Omega$ ($1470\ \Omega$) or trim with a multi-turn cermet potentiometer.</p>
        <p><strong>Step 2: Check Input-to-Output Voltage Headroom:</strong></p>
        $$V_{\text{diff}} = V_{\text{in}} - V_{\text{out}} = 15.0\text{ V} - 9.0\text{ V} = 6.0\text{ V}$$
        <p>This comfortably exceeds the $2.0\text{ V}$ worst-case dropout voltage requirement.</p>
        <p><strong>Step 3: Calculate Regulator Power Dissipation ($P_D$):</strong></p>
        $$P_D = (V_{\text{in}} - V_{\text{out}}) \cdot I_L = 6.0\text{ V} \times 0.800\text{ A} = 4.80\text{ Watts}$$
        <p><strong>Step 4: Compute Required Heatsink Thermal Resistance ($\theta_{SA}$):</strong></p>
        <p>Assuming silicone grease mounting thermal resistance $\theta_{CS} = 1.0^\circ\text{C/W}$:</p>
        $$\theta_{SA} \le \frac{T_{J,\text{max}} - T_A}{P_D} - (\theta_{JC} + \theta_{CS}) = \frac{110^\circ\text{C} - 40^\circ\text{C}}{4.80\text{ W}} - (4.0 + 1.0)$$
        $$\theta_{SA} \le \frac{70}{4.80} - 5.0 = 14.58 - 5.0 = 9.58^\circ\text{C/W}$$
        <p><strong>Conclusion:</strong> To prevent thermal shutdown, a stamped aluminum or extruded heatsink with thermal resistance rating $\theta_{SA} \le 9.5^\circ\text{C/W}$ must be mounted to the LM317T TO-220 tab.</p>
    </div>
</div>

<h2>Frequently Asked Questions (FAQ)</h2>
<div class="faq-section">
    <h3>How does the LM317 regulate its output voltage?</h3>
    <p>The LM317 maintains an internal temperature-compensated $1.25\text{ V}$ bandgap reference voltage ($V_{\text{ref}}$) between its OUT and ADJ terminals. By forcing this fixed $1.25\text{ V}$ across programming resistor $R_1$, a constant reference current flows into resistor $R_2$, developing an output voltage: $V_{\text{out}} = V_{\text{ref}} \left(1 + \frac{R_2}{R_1}\right) + I_{\text{adj}} R_2$.</p>

    <h3>Why is $R_1$ commonly chosen as $240\ \Omega$ or $120\ \Omega$?</h3>
    <p>The LM317 requires a minimum operating load current (typically $3.5\text{ mA}$ to $10\text{ mA}$) to maintain stable regulation under all temperature conditions. With $V_{\text{ref}} = 1.25\text{ V}$, setting $R_1 = 120\ \Omega$ guarantees a baseline current of $10.4\text{ mA}$, while $R_1 = 240\ \Omega$ guarantees $5.2\text{ mA}$, satisfying the minimum load specification without requiring an external load.</p>

    <h3>What is the dropout voltage of the LM317?</h3>
    <p>The LM317 requires an input-to-output voltage differential ($V_{\text{in}} - V_{\text{out}}$) of at least $1.5\text{ V}$ to $2.5\text{ V}$ depending on load current and junction temperature to keep its internal Darlington pass transistor in active regulation.</p>

    <h3>Why are protection diodes recommended in LM317 circuits?</h3>
    <p>If input power is abruptly grounded while large capacitors exist at the output or ADJ pin, reverse current flows into the regulator's internal transistors. Diode $D_1$ across OUT-to-IN and diode $D_2$ across ADJ-to-OUT safely divert discharge currents away from internal junctions.</p>
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
