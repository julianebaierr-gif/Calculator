# -*- coding: utf-8 -*-
"""
Generator for Batch 37 - Part 1
Tools:
1. buck-boost-converter-calculator.html
2. 3-phase-power-calculator.html
"""

import os

COMMON_TAIL = """    <footer class="site-footer">
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>About CalcHub</h4>
                    <p>CalcHub provides free, high-precision engineering calculators, unit converters, and analytical tools designed for practicing engineers, technicians, and students worldwide.</p>
                </div>
                <div class="footer-col">
                    <h4>Engineering Categories</h4>
                    <ul>
                        <li><a href="engineering.html">Electrical &amp; Electronics</a></li>
                        <li><a href="mechanical.html">Mechanical &amp; HVAC</a></li>
                        <li><a href="civil.html">Civil &amp; Structural</a></li>
                        <li><a href="chemical.html">Chemical &amp; Process</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Popular Calculators</h4>
                    <ul>
                        <li><a href="pcb-trace-width-calculator.html">PCB Trace Width</a></li>
                        <li><a href="wire-ampacity-calculator.html">Wire Ampacity</a></li>
                        <li><a href="voltage-divider-calculator.html">Voltage Divider</a></li>
                        <li><a href="motor-parameters-calculator.html">Motor Parameters</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="index.html">All Calculators</a></li>
                        <li><a href="converter.html">Unit Converters</a></li>
                        <li><a href="math.html">Math Tools</a></li>
                        <li><a href="finance.html">Finance Tools</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 CalcHub. All rights reserved. Peer-reviewed analytical calculation models.</p>
            </div>
        </div>
    </footer>
</body>
</html>"""

def get_page_html(title, description, canonical_slug, schema_json, h1, short_desc, calc_ui, article_content, category_hub="engineering.html", category_name="Engineering"):
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
                    <h3>Related Engineering Tools</h3>
                    <ul class="sidebar-links">
                        <li><a href="buck-boost-converter-calculator.html">Buck-Boost Converter</a></li>
                        <li><a href="3-phase-power-calculator.html">3-Phase Power Calculator</a></li>
                        <li><a href="pcb-trace-width-calculator.html">PCB Trace Width</a></li>
                        <li><a href="voltage-divider-calculator.html">Voltage Divider</a></li>
                        <li><a href="parallel-resistance-calculator.html">Parallel Resistance</a></li>
                        <li><a href="rc-time-constant-calculator.html">RC Time Constant</a></li>
                        <li><a href="rl-time-constant-calculator.html">RL Time Constant</a></li>
                        <li><a href="zener-diode-calculator.html">Zener Diode Sizing</a></li>
                        <li><a href="lm317-calculator.html">LM317 Voltage Regulator</a></li>
                        <li><a href="wire-ampacity-calculator.html">Wire Ampacity</a></li>
                    </ul>
                </div>
            </aside>
        </div>
    </div>
{COMMON_TAIL}"""


# ---------------------------------------------------------------------------
# Tool 1: Buck-Boost Converter Calculator
# ---------------------------------------------------------------------------
def gen_buck_boost():
    slug = "buck-boost-converter-calculator"
    title = "Buck-Boost Converter Calculator | Inductance, Ripple, Duty Cycle & Capacitance"
    desc = "Calculate duty cycle, critical inductance, peak inductor current, switch voltage stress, and output filter capacitance for inverting and non-inverting buck-boost DC-DC power supplies."
    h1 = "Buck-Boost Converter Calculator"
    short_desc = "Compute duty cycle, minimum continuous conduction inductance, peak switch current, and filter capacitor values for switch-mode DC-DC buck-boost power converters."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Buck-Boost Converter Calculator",
      "url": "https://calchub.com/buck-boost-converter-calculator.html",
      "applicationCategory": "EngineeringApplication",
      "operatingSystem": "All",
      "description": "Calculate duty cycle, continuous conduction mode (CCM) critical inductance, ripple current, and output capacitance for buck-boost power stages.",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the primary difference between inverting and four-switch non-inverting buck-boost converters?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "An inverting buck-boost topology reverses output voltage polarity relative to the input using a single active switch, diode, and inductor. In contrast, a 4-switch synchronous buck-boost converter maintains identical polarity and features higher efficiency by dynamically transitioning between pure buck, buck-boost, and pure boost modes depending on whether Vin is higher, comparable to, or lower than Vout."
          }
        },
        {
          "@type": "Question",
          "name": "Why is the inductor ripple current ratio (r) typically chosen between 0.2 and 0.4?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A ripple ratio r between 0.2 and 0.4 (20% to 40% of average inductor current) balances magnetic core volume and dynamic loop response against conduction and AC winding losses. Setting r below 0.2 yields an excessively large inductor with sluggish transient response, while r above 0.4 induces high peak currents, increased core hysteresis loss, and severe output voltage ripple."
          }
        },
        {
          "@type": "Question",
          "name": "How does Right-Half-Plane (RHP) zero affect the compensation loop of a buck-boost converter in CCM?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In Continuous Conduction Mode (CCM), a buck-boost converter exhibits a Right-Half-Plane (RHP) zero in its control-to-output transfer function. The RHP zero adds 20 dB/decade gain while simultaneously introducing a 90-degree phase lag. To ensure closed-loop feedback stability, the loop crossover frequency must typically be limited to below one-third or one-fifth of the RHP zero frequency."
          }
        },
        {
          "@type": "Question",
          "name": "How is the minimum critical inductance (L_crit) calculated to maintain Continuous Conduction Mode (CCM)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Critical inductance is determined at minimum load current: L_crit = (Vin * D) / (2 * I_load_min * f_sw), or equivalently L_crit = ((1 - D)^2 * R_load_max) / (2 * f_sw). When actual inductance falls below L_crit, the inductor current collapses to zero before the end of the switching cycle, forcing the converter into Discontinuous Conduction Mode (DCM)."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calculator-form">
    <div class="calc-row">
        <div class="calc-field">
            <label for="bb_vin">Input Voltage \\(V_{in}\\) (V):</label>
            <input type="number" id="bb_vin" value="12" step="0.1" min="0.1">
            <small class="field-hint">Nominal DC power rail voltage</small>
        </div>
        <div class="calc-field">
            <label for="bb_vout">Desired Output Voltage \\(V_{out}\\) (V):</label>
            <input type="number" id="bb_vout" value="24" step="0.1" min="0.1">
            <small class="field-hint">Target regulated DC output voltage</small>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="bb_iout">Output Load Current \\(I_{out}\\) (A):</label>
            <input type="number" id="bb_iout" value="2.5" step="0.1" min="0.01">
            <small class="field-hint">Maximum continuous load current</small>
        </div>
        <div class="calc-field">
            <label for="bb_fsw">Switching Frequency \\(f_{sw}\\) (kHz):</label>
            <input type="number" id="bb_fsw" value="150" step="1" min="10">
            <small class="field-hint">PWM controller operating frequency</small>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="bb_ripple_ratio">Inductor Ripple Ratio \\(r\\) (\\(\\Delta I_L / I_L\\)):</label>
            <input type="number" id="bb_ripple_ratio" value="0.30" step="0.05" min="0.1" max="1.0">
            <small class="field-hint">Recommended design target: 0.20 to 0.40</small>
        </div>
        <div class="calc-field">
            <label for="bb_vripple">Max Output Voltage Ripple \\(\\Delta V_o\\) (mV):</label>
            <input type="number" id="bb_vripple" value="50" step="1" min="1">
            <small class="field-hint">Peak-to-peak output capacitor ripple specification</small>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="bb_vd">Diode / Sync Rectifier Drop \\(V_D\\) (V):</label>
            <input type="number" id="bb_vd" value="0.5" step="0.05" min="0.0">
            <small class="field-hint">Schottky forward drop (~0.4-0.6V) or sync FET drop (~0.05V)</small>
        </div>
        <div class="calc-field">
            <label for="bb_eff">Estimated Efficiency \\(\\eta\\) (%):</label>
            <input type="number" id="bb_eff" value="88" step="1" min="50" max="99">
            <small class="field-hint">Expected conversion efficiency (typical: 85% - 94%)</small>
        </div>
    </div>
    <button type="button" class="btn btn-primary" id="btn_calc_bb" style="width:100%; margin-top:1rem;">Calculate Power Stage Parameters</button>

    <div class="calc-results" id="bb_results" style="margin-top:1.5rem;">
        <h3>Power Stage Design Summary</h3>
        <div class="results-grid">
            <div class="result-item">
                <span class="result-label">Operating Duty Cycle \\(D\\):</span>
                <span class="result-value" id="res_bb_duty">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Recommended Inductance \\(L\\):</span>
                <span class="result-value" id="res_bb_l">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Critical Inductance \\(L_{crit}\\) (at 10% load):</span>
                <span class="result-value" id="res_bb_lcrit">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Inductor Peak Current \\(I_{L,pk}\\):</span>
                <span class="result-value" id="res_bb_ilpk">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Inductor RMS Current \\(I_{L,rms}\\):</span>
                <span class="result-value" id="res_bb_ilrms">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Minimum Output Filter \\(C_{out}\\):</span>
                <span class="result-value" id="res_bb_cout">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Switch Voltage Stress \\(V_{sw,max}\\):</span>
                <span class="result-value" id="res_bb_vsw">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Right-Half-Plane Zero \\(f_{RHPZ}\\):</span>
                <span class="result-value" id="res_bb_rhpz">--</span>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    function calculateBuckBoost() {
        const vin = parseFloat(document.getElementById('bb_vin').value) || 12;
        const vout = parseFloat(document.getElementById('bb_vout').value) || 24;
        const iout = parseFloat(document.getElementById('bb_iout').value) || 2.5;
        const fswKhz = parseFloat(document.getElementById('bb_fsw').value) || 150;
        const fsw = fswKhz * 1000;
        const r = parseFloat(document.getElementById('bb_ripple_ratio').value) || 0.3;
        const vrippleMv = parseFloat(document.getElementById('bb_vripple').value) || 50;
        const vripple = vrippleMv / 1000;
        const vd = parseFloat(document.getElementById('bb_vd').value) || 0.5;
        const eff = (parseFloat(document.getElementById('bb_eff').value) || 88) / 100;

        // Duty cycle accounting for diode drop and efficiency
        // Vout = (D * Vin * eff) / ((1 - D)) - Vd  => D = (Vout + Vd) / (Vin * eff + Vout + Vd)
        const d = (vout + vd) / (vin * eff + vout + vd);
        const dPercent = (d * 100).toFixed(1) + '%';

        // Average inductor current IL,avg = Iout / (1 - D)
        const ilAvg = iout / (1 - d);
        
        // Inductor ripple current Delta IL = r * IL,avg
        const deltaIl = r * ilAvg;

        // Inductance L = (Vin * D) / (deltaIl * fsw)
        const lH = (vin * d) / (deltaIl * fsw);
        const lMicroH = (lH * 1e6).toFixed(1) + ' µH';

        // Critical inductance at 10% load
        const ioutMin = 0.10 * iout;
        const ilAvgMin = ioutMin / (1 - d);
        const lCritH = (vin * d) / (2 * ilAvgMin * fsw);
        const lCritMicroH = (lCritH * 1e6).toFixed(1) + ' µH';

        // Peak and RMS inductor current
        const ilPk = ilAvg + (deltaIl / 2);
        const ilRms = Math.sqrt(Math.pow(ilAvg, 2) + Math.pow(deltaIl, 2) / 12);

        // Output filter capacitance Cout = (Iout * D) / (fsw * DeltaVo)
        const coutF = (iout * d) / (fsw * vripple);
        const coutMicroF = (coutF * 1e6).toFixed(1) + ' µF';

        // Switch maximum voltage stress
        const vswMax = vin + vout + vd;

        // Right Half Plane Zero: f_RHPZ = (R_load * (1 - D)^2) / (2 * pi * D * L)
        const rLoad = vout / iout;
        const rhpzHz = (rLoad * Math.pow(1 - d, 2)) / (2 * Math.PI * d * lH);
        const rhpzKhz = (rhpzHz / 1000).toFixed(1) + ' kHz';

        document.getElementById('res_bb_duty').textContent = dPercent;
        document.getElementById('res_bb_l').textContent = lMicroH;
        document.getElementById('res_bb_lcrit').textContent = lCritMicroH;
        document.getElementById('res_bb_ilpk').textContent = ilPk.toFixed(2) + ' A';
        document.getElementById('res_bb_ilrms').textContent = ilRms.toFixed(2) + ' A';
        document.getElementById('res_bb_cout').textContent = coutMicroF;
        document.getElementById('res_bb_vsw').textContent = vswMax.toFixed(1) + ' V';
        document.getElementById('res_bb_rhpz').textContent = rhpzKhz;
    }

    document.getElementById('btn_calc_bb').addEventListener('click', calculateBuckBoost);
    calculateBuckBoost();
});
</script>"""

    article_content = """<h2>1. Fundamental Theory of Buck-Boost DC-DC Conversion</h2>
<p>In power electronics design, the buck-boost converter represents a canonical switch-mode power supply (SMPS) topology capable of delivering an output voltage that can be higher, lower, or equal in absolute magnitude to the input supply voltage. Unlike classic step-down (buck) or step-up (boost) architectures, the buck-boost topology accommodates battery discharge curves where the chemical cell voltage begins above the required system rail and subsequently declines below it as capacity is depleted.</p>

<p>The standard classical topology is the <strong>inverting buck-boost converter</strong>, which produces a negative output voltage relative to circuit ground using a single controlled active switch (MOSFET), a passive freewheeling diode (or synchronous secondary MOSFET), an energy storage inductor, and an output filter capacitor. During the switch conduction phase (\(t_{on} = D \cdot T_{sw}\)), the inductor is connected directly across the DC input source. Energy accumulates in the inductor's magnetic core as the flux density ramps up linearly, while the diode is reverse-biased, isolating the output capacitor and load. During the switch turn-off interval (\(t_{off} = (1 - D) \cdot T_{sw}\)), the collapsing magnetic field reverses the inductor's terminal voltage, forward-biasing the freewheeling diode and discharging stored electromagnetic energy into the output filter capacitor and external load.</p>

<h2>2. Core Mathematical Derivations &amp; Governing Equations</h2>
<p>To design an efficient, thermally resilient switch-mode power converter, power stage magnetics and semiconductor components must be synthesized through rigorous volt-second balance and charge-balance relationships. Under steady-state Continuous Conduction Mode (CCM), the net volt-seconds applied across the inductor over one complete switching period \(T_{sw} = 1 / f_{sw}\) must equate to zero:</p>

$$\int_0^{T_{sw}} v_L(t) \, dt = (V_{in}) \cdot D \cdot T_{sw} + (-V_{out} - V_D) \cdot (1 - D) \cdot T_{sw} = 0$$

<p>Solving for the nominal duty ratio \(D\) while factoring in power stage efficiency \(\eta\) and diode forward drop \(V_D\) gives:</p>

$$D = \frac{V_{out} + V_D}{V_{in} \cdot \eta + V_{out} + V_D}$$

<p>The average inductor current \(I_{L,avg}\) exceeds the DC load current \(I_{out}\) because the inductor transfers energy to the output network only during the turn-off interval \((1 - D)\):</p>

$$I_{L,avg} = \frac{I_{out}}{1 - D}$$

<p>The peak-to-peak inductor current ripple \(\Delta I_L\) is specified as a fraction \(r\) (the inductor ripple ratio, typically selected between \(0.20\) and \(0.40\)) of the average inductor current:</p>

$$\Delta I_L = r \cdot I_{L,avg} = r \cdot \frac{I_{out}}{1 - D}$$

<p>Applying Faraday's Law during the switch ON-time yields the required power stage inductance \(L\):</p>

$$L = \frac{V_{in} \cdot D}{\Delta I_L \cdot f_{sw}} = \frac{V_{in} \cdot D \cdot (1 - D)}{r \cdot I_{out} \cdot f_{sw}}$$

<p>The peak inductor current \(I_{L,pk}\) and root-mean-square (RMS) current \(I_{L,rms}\), critical for core saturation checking and copper wire loss calculations, are expressed as:</p>

$$I_{L,pk} = I_{L,avg} + \frac{\Delta I_L}{2}$$

$$I_{L,rms} = \sqrt{I_{L,avg}^2 + \frac{\Delta I_L^2}{12}}$$

<p>Because the output filter capacitor must supply the full load current during the switch conduction time \(D \cdot T_{sw}\), output capacitance requirements are notably more stringent than those of a standard buck converter. The minimum capacitance \(C_{out}\) to guarantee an output voltage ripple no greater than \(\Delta V_o\) is:</p>

$$C_{out,min} = \frac{I_{out} \cdot D}{\Delta V_o \cdot f_{sw}}$$

<h2>3. Empirical Design Benchmark Table for SMPS Inductors</h2>
<p>The following engineering data table provides standard magnetic core material selections, permeability values, saturation flux densities, and recommended operational frequency bands for switch-mode converter design:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Core Material</th>
            <th>Composition</th>
            <th>Initial Permeability (\(\mu_i\))</th>
            <th>Saturation Flux \(B_{sat}\) (T)</th>
            <th>Core Loss at 100 kHz</th>
            <th>Optimal Frequency Range</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Sendust (Kool M\(\mu\))</strong></td>
            <td>Fe-Si-Al alloy powder</td>
            <td>60 – 125</td>
            <td>1.05 T</td>
            <td>Low</td>
            <td>50 kHz – 500 kHz</td>
        </tr>
        <tr>
            <td><strong>High Flux</strong></td>
            <td>50% Ni, 50% Fe alloy</td>
            <td>14 – 160</td>
            <td>1.50 T</td>
            <td>Moderate</td>
            <td>20 kHz – 300 kHz</td>
        </tr>
        <tr>
            <td><strong>MPP (Molypermalloy)</strong></td>
            <td>79% Ni, 17% Fe, 4% Mo</td>
            <td>14 – 300</td>
            <td>0.75 T</td>
            <td>Lowest</td>
            <td>100 kHz – 1.5 MHz</td>
        </tr>
        <tr>
            <td><strong>Iron Powder (-26 mix)</strong></td>
            <td>Pure distributed air gap Fe</td>
            <td>75</td>
            <td>1.40 T</td>
            <td>High</td>
            <td>10 kHz – 100 kHz</td>
        </tr>
        <tr>
            <td><strong>Power Ferrite (MnZn)</strong></td>
            <td>N87 / 3C90 sintered ceramic</td>
            <td>2000 – 3000 (gapped)</td>
            <td>0.38 – 0.49 T</td>
            <td>Very Low</td>
            <td>100 kHz – 2.0 MHz</td>
        </tr>
    </tbody>
</table>

<h2>4. Right-Half-Plane Zero (RHPZ) and Feedback Compensation</h2>
<p>A crucial dynamic characteristic of Continuous Conduction Mode (CCM) buck-boost and boost topologies is the presence of an inherent <strong>Right-Half-Plane (RHP) Zero</strong> in the power stage control-to-output transfer function \(G_{vd}(s)\). The frequency of this zero is calculated as:</p>

$$\omega_{RHPZ} = \frac{R_{load} \cdot (1 - D)^2}{D \cdot L} \quad \implies \quad f_{RHPZ} = \frac{R_{load} \cdot (1 - D)^2}{2\pi \cdot D \cdot L}$$

<p>In classical control theory, an ordinary left-half-plane zero contributes \(+20\text{ dB/decade}\) of gain slope and \(+90^\circ\) of phase lead, improving stability. Conversely, an RHP zero boosts loop gain by \(+20\text{ dB/decade}\) while introducing a severe <strong>\(-90^\circ\) phase lag</strong>. If the closed-loop crossover frequency \(f_c\) approaches \(f_{RHPZ}\), the system experiences uncontrollable regenerative oscillation. Consequently, power supply design guidelines enforce the rule that loop crossover frequency must be kept below:</p>

$$f_{cross} \le \frac{1}{3} \text{ to } \frac{1}{5} f_{RHPZ}$$

<h2>5. Worked Engineering Case Study: Automotive Step-Up/Down Supply</h2>
<div class="worked-example-card">
    <h3>Design Specification: 12V Nominal to 24V Auxiliary Rail</h3>
    <p>An automotive telemetry computer requires a regulated \(V_{out} = 24\text{ V}\) rail delivering \(I_{out} = 2.5\text{ A}\) (\(60\text{ W}\)). The automotive battery fluctuates between \(V_{in,min} = 9\text{ V}\) during cold cranking and \(V_{in,nom} = 13.8\text{ V}\). The controller operates at \(f_{sw} = 150\text{ kHz}\) with an estimated efficiency \(\eta = 88\%\), Schottky diode drop \(V_D = 0.5\text{ V}\), ripple current ratio \(r = 0.30\), and peak-to-peak output ripple limit \(\Delta V_o \le 50\text{ mV}\).</p>

    <div class="step-solution">
        <h4>Step 1: Compute Maximum Operating Duty Cycle (Worst-Case Low Input)</h4>
        <p>At \(V_{in} = 9\text{ V}\):</p>
        $$D = \frac{24 + 0.5}{(9 \times 0.88) + 24 + 0.5} = \frac{24.5}{7.92 + 24.5} = \frac{24.5}{32.42} \approx 0.7557 \text{ (75.6\%)}$$

        <h4>Step 2: Average Inductor Current and Target Current Ripple</h4>
        $$I_{L,avg} = \frac{I_{out}}{1 - D} = \frac{2.5}{1 - 0.7557} = \frac{2.5}{0.2443} = 10.233\text{ A}$$
        $$\Delta I_L = r \times I_{L,avg} = 0.30 \times 10.233\text{ A} = 3.07\text{ A}$$

        <h4>Step 3: Inductance Calculation</h4>
        $$L = \frac{V_{in} \cdot D}{\Delta I_L \cdot f_{sw}} = \frac{9 \times 0.7557}{3.07 \times 150{,}000} = \frac{6.8013}{460{,}500} \approx 14.77 \times 10^{-6}\text{ H} \approx 15\text{ }\mu\text{H}$$

        <h4>Step 4: Inductor Peak Current and Component Voltage Stress</h4>
        $$I_{L,pk} = 10.233 + \frac{3.07}{2} = 11.77\text{ A}$$
        $$V_{sw,max} = V_{in,max} + V_{out} + V_D = 16\text{ V} + 24\text{ V} + 0.5\text{ V} = 40.5\text{ V}$$
        <p>A power MOSFET rated for at least \(60\text{ V}\) breakdown with low \(R_{DS(on)}\) and an inductor with a saturation current rating \(I_{sat} \ge 14\text{ A}\) are selected to provide adequate operating margin.</p>

        <h4>Step 5: Minimum Output Filter Capacitance</h4>
        $$C_{out,min} = \frac{I_{out} \cdot D}{f_{sw} \cdot \Delta V_o} = \frac{2.5 \times 0.7557}{150{,}000 \times 0.050} = \frac{1.8893}{7500} \approx 251.9\text{ }\mu\text{F}$$
        <p>A parallel combination of three \(100\text{ }\mu\text{F}\), \(35\text{ V}\) low-ESR polymer aluminum electrolytic capacitors shunted by two \(10\text{ }\mu\text{F}\) X7R ceramic capacitors satisfies both the capacitive bulk requirement and high-frequency ESR ripple suppression.</p>
    </div>
</div>

<h2>6. Frequently Asked Questions</h2>
<div class="faq-accordion">
    <div class="faq-item">
        <h3>What is the primary difference between inverting and four-switch non-inverting buck-boost converters?</h3>
        <p>An inverting buck-boost converter reverses the polarity of the DC output with respect to ground and employs only two power switches (one active transistor and one diode). A four-switch synchronous non-inverting buck-boost converter utilizes four power MOSFETs (two half-bridges) and an inductor. It preserves positive voltage polarity and delivers superior efficiency (&gt;96%) by operating dynamically as a pure buck converter when \(V_{in} \gg V_{out}\), a pure boost converter when \(V_{in} \ll V_{out}\), and in 4-switch buck-boost mode only when input and output voltages are nearly identical.</p>
    </div>
    <div class="faq-item">
        <h3>Why is the inductor ripple current ratio (r) typically chosen between 0.2 and 0.4?</h3>
        <p>Selecting \(r\) between 0.20 and 0.40 provides an optimal trade-off between magnetic component volume and power losses. A lower ripple ratio (\(r &lt; 0.2\)) requires a large, bulky inductor with higher DCR (winding resistance), increasing copper losses and slowing closed-loop transient response. A higher ripple ratio (\(r &gt; 0.4\)) produces severe AC peak currents, excessive core hysteresis and eddy-current losses, and demands much larger output capacitors to attenuate voltage ripple.</p>
    </div>
    <div class="faq-item">
        <h3>How does Right-Half-Plane (RHP) zero affect the compensation loop of a buck-boost converter in CCM?</h3>
        <p>In Continuous Conduction Mode, when the control loop demands higher output voltage by suddenly increasing duty cycle \(D\), the immediate short-term effect is a reduction in the switch turn-off time \((1 - D)\), temporarily decreasing the energy delivered to the load until inductor current ramps up. This phenomenon creates a Right-Half-Plane zero that increases open-loop gain by \(+20\text{ dB/decade}\) while degrading loop phase by \(-90^\circ\). To prevent severe phase margin erosion and instability, loop bandwidth must be restricted to less than one-third to one-fifth of the RHP zero frequency.</p>
    </div>
    <div class="faq-item">
        <h3>How is the minimum critical inductance (L_crit) calculated to maintain Continuous Conduction Mode (CCM)?</h3>
        <p>Continuous Conduction Mode requires that the instantaneous inductor current does not drop to zero at any point during the cycle. At the CCM/DCM boundary, peak-to-peak ripple current \(\Delta I_L\) equals twice the average inductor current. For a minimum operating load current \(I_{out,min}\), critical inductance is calculated as:</p>
        $$L_{crit} = \frac{V_{in} \cdot D}{2 \cdot I_{L,avg,min} \cdot f_{sw}} = \frac{V_{in} \cdot D \cdot (1 - D)}{2 \cdot I_{out,min} \cdot f_{sw}}$$
    </div>
</div>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article_content)


# ---------------------------------------------------------------------------
# Tool 2: 3-Phase Power Calculator
# ---------------------------------------------------------------------------
def gen_three_phase():
    slug = "3-phase-power-calculator"
    title = "3-Phase Power Calculator | Real, Reactive & Apparent Power (kW, kVAR, kVA)"
    desc = "Calculate active, reactive, and apparent power, line and phase currents, power factor correction capacitance, and load impedance for balanced 3-phase Wye (Star) and Delta electrical systems."
    h1 = "3-Phase Power Calculator"
    short_desc = "Compute 3-phase real power (kW), reactive power (kVAR), apparent power (kVA), line-to-line vs line-to-neutral voltages, and power factor correction capacitors."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "3-Phase Power Calculator",
      "url": "https://calchub.com/3-phase-power-calculator.html",
      "applicationCategory": "EngineeringApplication",
      "operatingSystem": "All",
      "description": "Calculate 3-phase electrical power parameters including real power (kW), reactive power (kVAR), apparent power (kVA), phase currents, and power factor correction capacitance.",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Why is the square root of 3 (sqrt(3) ≈ 1.732) used in 3-phase power calculations?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The factor sqrt(3) arises geometrically from the 120-degree phase displacement between the three sinusoidal voltages. In a balanced Wye (Star) connection, vector addition of two 120-degree displaced phase voltages yields a line-to-line voltage magnitude equal to sqrt(3) times the phase-to-neutral voltage: V_LL = sqrt(3) * V_LN."
          }
        },
        {
          "@type": "Question",
          "name": "What is the difference between active (kW), reactive (kVAR), and apparent (kVA) power?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Active power (P in kW) represents the actual usable energy consumed by resistive loads to perform mechanical work or heat generation. Reactive power (Q in kVAR) is the non-working oscillating power required to sustain magnetic fields in inductive equipment such as motors and transformers. Apparent power (S in kVA) is the total vector sum of active and reactive power: S = sqrt(P^2 + Q^2)."
          }
        },
        {
          "@type": "Question",
          "name": "How does current and voltage differ between Wye (Star) and Delta configurations?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In a Wye (Star) system, line current equals phase current (I_line = I_phase), while line-to-line voltage is sqrt(3) times phase voltage (V_LL = sqrt(3) * V_phase). In a Delta system, line-to-line voltage equals phase voltage (V_LL = V_phase), while line current is sqrt(3) times phase current (I_line = sqrt(3) * I_phase)."
          }
        },
        {
          "@type": "Question",
          "name": "How is power factor correction capacitor rating (kVAR) calculated?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The required corrective reactive power Q_c is calculated using: Q_c = P * [tan(acos(PF_initial)) - tan(acos(PF_target))]. Installing shunt capacitors with rating Q_c cancels lagging inductive reactive current, reducing apparent kVA demand and eliminating utility power factor penalties."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calculator-form">
    <div class="calc-row">
        <div class="calc-field">
            <label for="p3_calc_mode">Calculation Target:</label>
            <select id="p3_calc_mode">
                <option value="from_vi">Calculate Power from Voltage &amp; Current</option>
                <option value="from_p">Calculate Current from Known Power (kW)</option>
            </select>
        </div>
        <div class="calc-field">
            <label for="p3_connection">Configuration:</label>
            <select id="p3_connection">
                <option value="wye">Wye / Star (Y) Connection</option>
                <option value="delta">Delta (Δ) Connection</option>
            </select>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="p3_vll">Line-to-Line Voltage \\(V_{L-L}\\) (V):</label>
            <input type="number" id="p3_vll" value="480" step="1" min="1">
            <small class="field-hint">e.g., 480V, 400V, 208V, 600V</small>
        </div>
        <div class="calc-field" id="box_p3_iline">
            <label for="p3_iline">Line Current \\(I_L\\) (A):</label>
            <input type="number" id="p3_iline" value="65" step="0.1" min="0.1">
            <small class="field-hint">Measured RMS line conductor current</small>
        </div>
        <div class="calc-field" id="box_p3_power_input" style="display:none;">
            <label for="p3_p_kw">Real Power \\(P\\) (kW):</label>
            <input type="number" id="p3_p_kw" value="45" step="0.1" min="0.1">
            <small class="field-hint">Nameplate or measured electrical active load</small>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="p3_pf">Operating Power Factor (\\(\\cos\\phi\\)):</label>
            <input type="number" id="p3_pf" value="0.82" step="0.01" min="0.1" max="1.0">
            <small class="field-hint">Lagging (inductive) load power factor</small>
        </div>
        <div class="calc-field">
            <label for="p3_target_pf">Target Power Factor:</label>
            <input type="number" id="p3_target_pf" value="0.95" step="0.01" min="0.80" max="1.0">
            <small class="field-hint">Desired utility compliant power factor</small>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="p3_freq">AC Line Frequency:</label>
            <select id="p3_freq">
                <option value="60">60 Hz (North America, ANSI)</option>
                <option value="50">50 Hz (Europe, Asia, IEC)</option>
            </select>
        </div>
        <div class="calc-field">
            <label for="p3_eff">Motor / Load Efficiency \\(\\eta\\) (%):</label>
            <input type="number" id="p3_eff" value="100" step="1" min="50" max="100">
            <small class="field-hint">Set 100% for electrical input, &lt;100% for shaft output</small>
        </div>
    </div>
    <button type="button" class="btn btn-primary" id="btn_calc_p3" style="width:100%; margin-top:1rem;">Calculate 3-Phase Power Parameters</button>

    <div class="calc-results" id="p3_results" style="margin-top:1.5rem;">
        <h3>3-Phase Electrical Load Analysis</h3>
        <div class="results-grid">
            <div class="result-item">
                <span class="result-label">Real Power \\(P\\):</span>
                <span class="result-value" id="res_p3_p">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Apparent Power \\(S\\):</span>
                <span class="result-value" id="res_p3_s">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Reactive Power \\(Q\\):</span>
                <span class="result-value" id="res_p3_q">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Line Current \\(I_L\\):</span>
                <span class="result-value" id="res_p3_il">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Phase Voltage \\(V_{ph}\\):</span>
                <span class="result-value" id="res_p3_vph">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Phase Current \\(I_{ph}\\):</span>
                <span class="result-value" id="res_p3_iph">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Correction Capacitor \\(Q_c\\):</span>
                <span class="result-value" id="res_p3_qc">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Capacitance / Phase \\(C_{ph}\\):</span>
                <span class="result-value" id="res_p3_cph">--</span>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const modeSelect = document.getElementById('p3_calc_mode');
    const boxIline = document.getElementById('box_p3_iline');
    const boxPower = document.getElementById('box_p3_power_input');

    modeSelect.addEventListener('change', function() {
        if (modeSelect.value === 'from_vi') {
            boxIline.style.display = 'block';
            boxPower.style.display = 'none';
        } else {
            boxIline.style.display = 'none';
            boxPower.style.display = 'block';
        }
    });

    function calculate3Phase() {
        const mode = modeSelect.value;
        const conn = document.getElementById('p3_connection').value;
        const vll = parseFloat(document.getElementById('p3_vll').value) || 480;
        const pf = parseFloat(document.getElementById('p3_pf').value) || 0.82;
        const targetPf = parseFloat(document.getElementById('p3_target_pf').value) || 0.95;
        const freq = parseFloat(document.getElementById('p3_freq').value) || 60;
        const eff = (parseFloat(document.getElementById('p3_eff').value) || 100) / 100;

        let pKw, iline, sKva, qKvar;

        if (mode === 'from_vi') {
            iline = parseFloat(document.getElementById('p3_iline').value) || 65;
            sKva = (Math.sqrt(3) * vll * iline) / 1000;
            pKw = sKva * pf * eff;
            const sinPhi = Math.sin(Math.acos(pf));
            qKvar = sKva * sinPhi;
        } else {
            pKw = parseFloat(document.getElementById('p3_p_kw').value) || 45;
            const pInputKw = pKw / eff;
            sKva = pInputKw / pf;
            iline = (sKva * 1000) / (Math.sqrt(3) * vll);
            const sinPhi = Math.sin(Math.acos(pf));
            qKvar = sKva * sinPhi;
        }

        // Phase voltages and currents
        let vph, iph;
        if (conn === 'wye') {
            vph = vll / Math.sqrt(3);
            iph = iline;
        } else {
            vph = vll;
            iph = iline / Math.sqrt(3);
        }

        // Power factor correction
        // Qc = P * (tan(phi1) - tan(phi2))
        const phi1 = Math.acos(pf);
        const phi2 = Math.acos(Math.min(1.0, targetPf));
        let qc = pKw * (Math.tan(phi1) - Math.tan(phi2));
        if (qc < 0) qc = 0;

        // Capacitance calculation per phase (Delta-connected capacitor bank is standard)
        // Qc_total = 3 * (Vll^2 * 2 * pi * f * C_delta)
        // C_delta = (Qc * 1000) / (3 * 2 * pi * freq * Vll^2)
        const omega = 2 * Math.PI * freq;
        const cDeltaFarads = (qc * 1000) / (3 * omega * Math.pow(vll, 2));
        const cMicroFarad = (cDeltaFarads * 1e6).toFixed(1) + ' µF (Δ)';

        document.getElementById('res_p3_p').textContent = pKw.toFixed(2) + ' kW';
        document.getElementById('res_p3_s').textContent = sKva.toFixed(2) + ' kVA';
        document.getElementById('res_p3_q').textContent = qKvar.toFixed(2) + ' kVAR';
        document.getElementById('res_p3_il').textContent = iline.toFixed(2) + ' A';
        document.getElementById('res_p3_vph').textContent = vph.toFixed(1) + ' V';
        document.getElementById('res_p3_iph').textContent = iph.toFixed(2) + ' A';
        document.getElementById('res_p3_qc').textContent = qc.toFixed(2) + ' kVAR';
        document.getElementById('res_p3_cph').textContent = cMicroFarad;
    }

    document.getElementById('btn_calc_p3').addEventListener('click', calculate3Phase);
    calculate3Phase();
});
</script>"""

    article_content = """<h2>1. Fundamental Principles of Polyphase Alternating Current</h2>
<p>Three-phase alternating current (AC) electrical transmission and distribution constitutes the backbone of modern industrial power grids and commercial electrical infrastructure. Engineered originally by Nikola Tesla and Charles Proteus Steinmetz, three-phase systems deliver a continuous, constant instantaneous power transfer to rotating machines, unlike single-phase AC circuits which pulsate between zero and peak power twice per cycle at line frequency.</p>

<p>In a balanced three-phase generator or load, three separate sinusoidal voltages of identical amplitude and frequency are displaced from each other by an electrical phase angle of exactly \(120^\circ\) (\(2\pi/3\text{ radians}\)):</p>

$$v_A(t) = V_{pk} \cos(\omega t)$$

$$v_B(t) = V_{pk} \cos\left(\omega t - \frac{2\pi}{3}\right)$$

$$v_C(t) = V_{pk} \cos\left(\omega t - \frac{4\pi}{3}\right)$$

<p>Because the sum of three identical vectors displaced by \(120^\circ\) equals zero (\(v_A + v_B + v_C = 0\)), balanced three-phase systems eliminate the requirement for a return neutral conductor of equal cross-section, reducing copper usage by approximately 25% compared to three independent single-phase circuits transporting equivalent energy.</p>

<h2>2. Wye (Star) vs. Delta Network Topologies</h2>
<p>Three-phase circuits are wired in either a <strong>Wye (Star, Y)</strong> or <strong>Delta (\(\Delta\))</strong> configuration, governing the spatial and mathematical relationship between line quantities (measured at the external supply terminals) and phase quantities (experienced across individual internal load windings):</p>

<h3>Wye (Star, Y) Connection</h3>
<p>In a Wye configuration, three load impedances meet at a common central neutral point \(N\). The current traversing any incoming line conductor flows directly into that respective phase winding without splitting:</p>

$$I_{line} = I_{phase}$$

<p>The line-to-line voltage \(V_{L-L}\) is the vector difference between two phase-to-neutral voltages displaced by \(120^\circ\). Applying vector trigonometry yields the fundamental \(\sqrt{3} \approx 1.73205\) relationship:</p>

$$V_{L-L} = \sqrt{3} \cdot V_{phase} = \sqrt{3} \cdot V_{L-N}$$

<h3>Delta (\(\Delta\)) Connection</h3>
<p>In a Delta configuration, the three load impedances are connected end-to-end in a closed loop, forming an equilateral triangle. Each phase winding is connected directly across two line conductors, meaning line-to-line voltage equals phase voltage:</p>

$$V_{line} = V_{phase}$$

<p>Conversely, the line current divides between two adjacent phase branches. For balanced conditions, Kirchhoff's Current Law gives:</p>

$$I_{line} = \sqrt{3} \cdot I_{phase}$$

<h2>3. Power Equations: Active (kW), Reactive (kVAR), and Apparent (kVA)</h2>
<p>Regardless of whether the load is wired in Wye or Delta, total power in a balanced three-phase electrical circuit is derived directly from terminal line-to-line voltage \(V_{L-L}\) and line current \(I_{line}\):</p>

<h3>Active / Real Power (\(P\))</h3>
<p>Real power is the actual thermodynamic work converted into mechanical rotation, heat, or illumination, measured in kilowatts (kW):</p>

$$P = \sqrt{3} \cdot V_{L-L} \cdot I_{line} \cdot \cos\phi \quad [\text{W}]$$

<p>where \(\cos\phi\) is the operating power factor (\(PF\)), representing the cosine of the phase displacement angle between phase voltage and phase current.</p>

<h3>Apparent Power (\(S\))</h3>
<p>Apparent power represents the total complex volt-ampere product that utility transformers, switchgear, and conductors must be sized to transport, measured in kilovolt-amperes (kVA):</p>

$$S = \sqrt{3} \cdot V_{L-L} \cdot I_{line} \quad [\text{VA}]$$

<h3>Reactive Power (\(Q\))</h3>
<p>Reactive power oscillates cyclically between inductive magnetic fields (in motors, solenoids, transformers) and the AC supply without performing net mechanical work, measured in reactive kilovolt-amperes (kVAR):</p>

$$Q = \sqrt{3} \cdot V_{L-L} \cdot I_{line} \cdot \sin\phi \quad [\text{VAR}]$$

<p>These three quantities form the classical <strong>Power Triangle</strong>:</p>

$$S = \sqrt{P^2 + Q^2} \quad \implies \quad PF = \cos\phi = \frac{P}{S}$$

<h2>4. Industrial Voltage Standards Reference Table</h2>
<p>The following engineering data table lists standard commercial and industrial three-phase utilization voltages across North American (ANSI/IEEE) and International (IEC) standards, along with typical applications:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Nominal System Voltage</th>
            <th>Configuration</th>
            <th>Phase-to-Neutral</th>
            <th>Standard Region</th>
            <th>Primary Utilization</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>480Y / 277 V</strong></td>
            <td>4-Wire Wye</td>
            <td>277 V</td>
            <td>North America (ANSI)</td>
            <td>Industrial motors, commercial HVAC, fluorescent/LED high-bay lighting</td>
        </tr>
        <tr>
            <td><strong>208Y / 120 V</strong></td>
            <td>4-Wire Wye</td>
            <td>120 V</td>
            <td>North America (ANSI)</td>
            <td>Commercial office buildings, retail, servers, receptacle convenience loads</td>
        </tr>
        <tr>
            <td><strong>400Y / 230 V</strong></td>
            <td>4-Wire Wye</td>
            <td>230 V</td>
            <td>Europe, IEC International</td>
            <td>Standard commercial &amp; industrial distribution, residential single-phase derived</td>
        </tr>
        <tr>
            <td><strong>600Y / 347 V</strong></td>
            <td>4-Wire Wye</td>
            <td>347 V</td>
            <td>Canada (CSA)</td>
            <td>Heavy manufacturing, mining, industrial pumping, institutional facilities</td>
        </tr>
        <tr>
            <td><strong>240 V Delta</strong></td>
            <td>3-Wire Delta / High-Leg</td>
            <td>120 V / 208 V (high leg)</td>
            <td>North America (Legacy)</td>
            <td>Small machine shops, legacy 3-phase machinery with 120V single-phase tap</td>
        </tr>
        <tr>
            <td><strong>4160 V (Medium Voltage)</strong></td>
            <td>3-Wire Wye / Delta</td>
            <td>2400 V</td>
            <td>Global (IEEE / IEC)</td>
            <td>Large industrial chillers, utility water pumps, municipal compressors (&gt;500 HP)</td>
        </tr>
    </tbody>
</table>

<h2>5. Power Factor Correction Engineering Methodology</h2>
<p>Inductive industrial loads (induction motors operating below full rated shaft torque) cause the line current to lag voltage, leading to poor power factor (\(PF &lt; 0.85\)). Low power factor increases \(I^2R\) transmission losses in upstream conductors and triggers punitive reactive power surcharge billing from electrical utility providers.</p>

<p>To correct the power factor from an initial lagging value \(PF_1 = \cos\phi_1\) to a target value \(PF_2 = \cos\phi_2\), a balanced shunt capacitor bank is installed across the supply bus. The required corrective capacitive kVAR rating \(Q_c\) is:</p>

$$Q_c = P \cdot \left(\tan\phi_1 - \tan\phi_2\right) = P \cdot \left(\tan(\arccos(PF_1)) - \tan(\arccos(PF_2))\right)$$

<p>When connecting the capacitor bank in Delta (\(\Delta\)) configuration across line-to-line terminals, the required capacitance per phase \(C_\Delta\) at frequency \(f\) is calculated as:</p>

$$C_\Delta = \frac{Q_c \times 1000}{3 \cdot 2\pi f \cdot V_{L-L}^2} \quad [\text{Farads}]$$

<h2>6. Worked Industrial Calculation Example: Manufacturing Facility Feeder</h2>
<div class="worked-example-card">
    <h3>Engineering Case Study: Sizing Feeder for 480V Industrial Machine Cell</h3>
    <p>A manufacturing facility operates an automated machining cell consisting of multiple three-phase induction motor drives. The electrical feeder operates at \(V_{L-L} = 480\text{ V}\), \(60\text{ Hz}\). A digital power quality meter records a steady-state line current \(I_{line} = 65.0\text{ A}\) with a lagging power factor \(PF = 0.82\). The plant engineer must compute the active power (kW), apparent power (kVA), reactive power (kVAR), and determine the required Delta capacitor bank to elevate the power factor to \(0.95\).</p>

    <div class="step-solution">
        <h4>Step 1: Compute Total Apparent Power (\(S\))</h4>
        $$S = \sqrt{3} \cdot V_{L-L} \cdot I_{line} = 1.73205 \times 480\text{ V} \times 65.0\text{ A} = 54{,}040\text{ VA} = 54.04\text{ kVA}$$

        <h4>Step 2: Compute Total Active Real Power (\(P\))</h4>
        $$P = S \times PF = 54.04\text{ kVA} \times 0.82 = 44.31\text{ kW}$$

        <h4>Step 3: Compute Initial Reactive Power (\(Q_1\))</h4>
        $$\phi_1 = \arccos(0.82) \approx 34.915^\circ$$
        $$\sin\phi_1 = \sin(34.915^\circ) = 0.5724$$
        $$Q_1 = S \times \sin\phi_1 = 54.04\text{ kVA} \times 0.5724 = 30.93\text{ kVAR}$$

        <h4>Step 4: Compute Power Factor Correction Capacitor Rating (\(Q_c\))</h4>
        $$\phi_2 = \arccos(0.95) \approx 18.195^\circ$$
        $$\tan\phi_1 = \tan(34.915^\circ) = 0.6980$$
        $$\tan\phi_2 = \tan(18.195^\circ) = 0.3287$$
        $$Q_c = P \cdot (\tan\phi_1 - \tan\phi_2) = 44.31\text{ kW} \times (0.6980 - 0.3287) = 44.31 \times 0.3693 = 16.36\text{ kVAR}$$

        <h4>Step 5: Compute Required Capacitance per Phase for Delta Bank</h4>
        $$C_\Delta = \frac{Q_c \times 1000}{3 \cdot 2\pi f \cdot V_{L-L}^2} = \frac{16{,}360}{3 \times 2\pi \times 60 \times (480)^2} = \frac{16{,}360}{3 \times 376.99 \times 230{,}400} = \frac{16{,}360}{260{,}551{,}884} \approx 62.8 \times 10^{-6}\text{ F} \approx 62.8\text{ }\mu\text{F}$$
        <p>A standard 3-phase, \(480\text{ V}\), \(17.5\text{ kVAR}\) enclosed capacitor bank with internal discharge resistors will successfully bring the power factor to \(0.95+\), lowering line current from \(65.0\text{ A}\) down to \(56.1\text{ A}\) and releasing \(8.9\text{ A}\) of feeder ampacity capacity.</p>
    </div>
</div>

<h2>7. Frequently Asked Questions</h2>
<div class="faq-accordion">
    <div class="faq-item">
        <h3>Why is the square root of 3 (sqrt(3) ≈ 1.732) used in 3-phase power calculations?</h3>
        <p>The factor \(\sqrt{3}\) originates from the trigonometric vector relationship between the three sinusoidal phases displaced by \(120^\circ\). In a Wye system, the line-to-line voltage is obtained by subtracting two phase vectors: \(\vec{V}_{AB} = \vec{V}_{AN} - \vec{V}_{BN}\). Solving the vector triangle with interior angles of \(30^\circ\), \(30^\circ\), and \(120^\circ\) proves that \(V_{AB} = 2 \cdot V_{AN} \cdot \cos(30^\circ) = 2 \cdot V_{AN} \cdot (\sqrt{3}/2) = \sqrt{3} \cdot V_{AN}\).</p>
    </div>
    <div class="faq-item">
        <h3>What is the difference between active (kW), reactive (kVAR), and apparent (kVA) power?</h3>
        <p>Active power (\(P\), kW) is the productive electrical energy converted directly into mechanical rotation, thermal heat, or optical radiation. Reactive power (\(Q\), kVAR) represents non-dissipative circulating energy required to magnetize transformer cores and motor stator windings. Apparent power (\(S\), kVA) is the total geometric vector sum (\(S = \sqrt{P^2 + Q^2}\)), defining the thermal loading capacity required from utility generators, transformers, and distribution cables.</p>
    </div>
    <div class="faq-item">
        <h3>What happens if a three-phase system experiences severe phase voltage imbalance?</h3>
        <p>Even small voltage imbalances induce severe, disproportionate current imbalances in induction motors due to low negative-sequence impedance. A 3% voltage unbalance can trigger a 20% to 30% phase current unbalance, leading to localized stator winding overheating, vibration, and significant motor insulation life reduction. In such scenarios, NEMA MG-1 standards require derating the motor's horsepower capacity.</p>
    </div>
    <div class="faq-item">
        <h3>Why are power factor correction capacitors usually connected in Delta rather than Wye?</h3>
        <p>In a Delta connection, each capacitor experiences full line-to-line voltage \(V_{L-L}\), whereas in Wye each capacitor experiences only \(V_{L-L} / \sqrt{3}\). Since capacitive reactive power output scales with the square of applied voltage (\(Q_c \propto V^2\)), a Delta-connected capacitor bank delivers three times more reactive kVAR than an identically rated capacitance connected in Wye, drastically reducing physical capacitor cell volume and cost.</p>
    </div>
</div>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article_content)


def main():
    tools = [
        ("buck-boost-converter-calculator.html", gen_buck_boost()),
        ("3-phase-power-calculator.html", gen_three_phase())
    ]
    for filename, content in tools:
        filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {filename}")

if __name__ == "__main__":
    main()
