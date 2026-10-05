# -*- coding: utf-8 -*-
"""
Generator for Batch 35 - Part 1:
1. voltage-divider-calculator.html
2. parallel-resistance-calculator.html
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 1. voltage-divider-calculator.html
HTML_VOLTAGE_DIVIDER = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Voltage Divider Calculator - Potential Divider &amp; Loaded Output Voltage</title>
  <meta name="description" content="Calculate output voltage (V_out = V_in * R2 / (R1 + R2)), loaded voltage dividers, Thevenin equivalent resistance, and ADC attenuation with step-by-step proofs.">
  <link rel="canonical" href="https://calchub.org/voltage-divider-calculator.html">
  <meta property="og:title" content="Voltage Divider Calculator - Potential Divider &amp; Loaded Circuit Solver">
  <meta property="og:description" content="Free electronics voltage divider calculator. Calculate V_out, resistor ratios, load resistance effects (R_L), Thevenin impedance, and power dissipation.">
  <meta property="og:url" content="https://calchub.org/voltage-divider-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Voltage Divider Calculator - Electrical Engineering Tool">
  <meta name="twitter:description" content="Solve potential dividers, loaded resistor networks, and microcontroller ADC voltage level scaling with worked circuit case studies.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Voltage Divider Calculator",
    "url": "https://calchub.org/voltage-divider-calculator.html",
    "description": "Calculates unloaded and loaded output voltages, Thevenin equivalent resistance, current draw, and power dissipation across resistor divider networks.",
    "applicationCategory": "EducationalApplication",
    "operatingSystem": "All"
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is the formula for an unloaded voltage divider?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "For two resistors in series connected across an input voltage V_in, the unloaded output voltage taken across R2 is: V_out = V_in * [R2 / (R1 + R2)], where V_in is input voltage in volts, R1 is the top series resistor, and R2 is the bottom ground-referenced resistor."
        }
      },
      {
        "@type": "Question",
        "name": "How does a load resistance affect the output voltage?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "When a load resistor (R_L) is connected across the output terminals in parallel with R2, the effective bottom resistance decreases to R_parallel = (R2 * R_L) / (R2 + R_L). The loaded output voltage drops to V_out = V_in * [R_parallel / (R1 + R_parallel)]. To minimize loading errors to less than 1%, the load resistance should be at least 100 times larger than the divider's Thevenin resistance."
        }
      },
      {
        "@type": "Question",
        "name": "What is the Thevenin equivalent of a voltage divider?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "As seen from the output terminals, a voltage divider behaves as an ideal voltage source of V_th = V_in * [R2 / (R1 + R2)] in series with a Thevenin output impedance equal to the parallel combination of the two resistors: R_th = (R1 * R2) / (R1 + R2)."
        }
      },
      {
        "@type": "Question",
        "name": "Why shouldn't a voltage divider be used as a power supply?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Voltage dividers have very poor voltage regulation under varying load currents and waste significant energy as heat across the resistors. Any change in load current causes V_out to fluctuate wildly. For supplying operating power to microcontrollers, motors, or LEDs, active voltage regulators (such as LM317, LDOs, or buck switching converters) should always be used instead."
        }
      }
    ]
  }
  </script>
</head>
<body>
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">CalcHub</a>
      <nav class="site-nav">
        <a href="index.html">Home</a>
        <a href="math.html">Math &amp; Statistics</a>
        <a href="converter.html">Converters</a>
        <a href="engineering.html" class="active">Engineering</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="page-container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo;
      <a href="engineering.html">Electrical &amp; Engineering</a> &rsaquo;
      <span>Voltage Divider Calculator</span>
    </nav>

    <div class="page-header">
      <h1 class="page-title">Voltage Divider Calculator</h1>
      <p class="page-desc">Compute unloaded and loaded output voltages, required resistor values, Thevenin source resistance, and circuit power dissipation.</p>
    </div>

    <div class="calc-grid">
      <!-- Calculator Column -->
      <div class="calc-card">
        <div class="calc-header">
          <h2>Potential Divider Circuit Solver</h2>
        </div>

        <!-- Mode Selection -->
        <div class="form-group">
          <label for="vd-mode">Calculation Mode:</label>
          <select id="vd-mode" class="form-control">
            <option value="find-vout" selected>Calculate Output Voltage (V_out from Vin, R1 &amp; R2)</option>
            <option value="find-r1">Calculate Top Resistor R1 (from Vin, Target Vout &amp; R2)</option>
            <option value="find-r2">Calculate Bottom Resistor R2 (from Vin, Target Vout &amp; R1)</option>
          </select>
        </div>

        <!-- Divider Preset -->
        <div class="form-group">
          <label for="vd-preset">Common Circuit Scaling Preset:</label>
          <select id="vd-preset" class="form-control">
            <option value="custom">-- Custom Resistor Network --</option>
            <option value="5v-to-3v3" selected>5.0V Logic to 3.3V Logic (Vin = 5V, R1 = 1.8kΩ, R2 = 3.3kΩ)</option>
            <option value="12v-to-5v">12V Automotive to 5V MCU (Vin = 12V, R1 = 14kΩ, R2 = 10kΩ)</option>
            <option value="12v-to-3v3">12V to 3.3V ADC Attenuator (Vin = 12V, R1 = 27kΩ, R2 = 10kΩ)</option>
            <option value="half-supply">Half-Supply Virtual Ground (Vin = 9V, R1 = 10kΩ, R2 = 10kΩ &rarr; 4.5V)</option>
            <option value="24v-to-10v">24V PLC to 10V Analog (Vin = 24V, R1 = 14kΩ, R2 = 10kΩ)</option>
          </select>
        </div>

        <!-- Inputs Row: Vin -->
        <div class="form-row">
          <div class="form-group">
            <label for="vd-vin">Input Voltage ($V_{\text{in}}$ in Volts):</label>
            <input type="number" id="vd-vin" class="form-control" value="5.0" step="any">
          </div>
          <div class="form-group" id="vd-vout-input-group" style="display: none;">
            <label for="vd-target-vout">Target Output ($V_{\text{out}}$ in Volts):</label>
            <input type="number" id="vd-target-vout" class="form-control" value="3.3" step="any">
          </div>
        </div>

        <!-- Resistors R1 & R2 -->
        <div class="form-row">
          <div class="form-group" id="vd-r1-group">
            <label for="vd-r1">Resistor 1 (Top, $R_1$):</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="vd-r1" class="form-control" value="1800" step="any" min="0.001">
              <select id="vd-r1-unit" class="form-control" style="max-width: 90px;">
                <option value="1">&Omega;</option>
                <option value="1000" selected>k&Omega;</option>
                <option value="1000000">M&Omega;</option>
              </select>
            </div>
          </div>
          <div class="form-group" id="vd-r2-group">
            <label for="vd-r2">Resistor 2 (Bottom, $R_2$):</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="vd-r2" class="form-control" value="3300" step="any" min="0.001">
              <select id="vd-r2-unit" class="form-control" style="max-width: 90px;">
                <option value="1">&Omega;</option>
                <option value="1000" selected>k&Omega;</option>
                <option value="1000000">M&Omega;</option>
              </select>
            </div>
          </div>
        </div>

        <!-- Optional Load Resistor RL -->
        <div class="form-row">
          <div class="form-group">
            <label for="vd-rl">Load Resistance ($R_L$, optional):</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="vd-rl" class="form-control" placeholder="Infinite (open circuit)" step="any" min="0.1">
              <select id="vd-rl-unit" class="form-control" style="max-width: 90px;">
                <option value="1">&Omega;</option>
                <option value="1000" selected>k&Omega;</option>
                <option value="1000000">M&Omega;</option>
              </select>
            </div>
            <span style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Leave blank for ideal unloaded output.</span>
          </div>
        </div>

        <div class="form-actions">
          <button type="button" id="vd-calc-btn" class="btn btn-primary">Calculate Output Voltage</button>
          <button type="button" id="vd-reset-btn" class="btn btn-secondary">Reset</button>
        </div>

        <!-- Output Cards -->
        <div id="vd-results" class="results-container" style="margin-top: 1.5rem;">
          <div class="result-hero-card">
            <div class="result-label" style="font-size: 0.875rem; color: var(--text-muted, #64748b); text-transform: uppercase; font-weight: 600;">Output Voltage ($V_{\text{out}}$)</div>
            <div id="vd-primary-out" style="font-size: 2.25rem; font-weight: 800; color: var(--primary, #2563eb); margin: 0.25rem 0;">3.235 V</div>
            <div id="vd-status-out" style="font-size: 1rem; color: var(--text-secondary, #475569); font-weight: 600;">Attenuation Factor: 0.647 &bull; Ratio R2/(R1+R2): 64.7%</div>
          </div>

          <div class="summary-metrics-grid">
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Quiescent Current ($I$)</div>
              <div id="vd-current-out" style="font-size: 1.15rem; font-weight: 700;">0.980 mA</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Total Power Dissipation</div>
              <div id="vd-power-out" style="font-size: 1.15rem; font-weight: 700;">4.90 mW</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Thevenin Resistance ($R_{\text{th}}$)</div>
              <div id="vd-rth-out" style="font-size: 1.15rem; font-weight: 700;">1.165 k&Omega;</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">R1 Power / R2 Power</div>
              <div id="vd-split-pwr-out" style="font-size: 1.15rem; font-weight: 700;">1.73 mW / 3.17 mW</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Reference Sidebar -->
      <aside class="sidebar-card">
        <h3>Standard Voltage Divider Rules</h3>
        <ul style="font-size: 0.875rem; line-height: 1.6; margin-left: 1.25rem;">
          <li><strong>Unloaded Output:</strong><br>\(V_{\text{out}} = V_{\text{in}} \frac{R_2}{R_1 + R_2}\)</li>
          <li><strong>Loaded Output:</strong><br>\(R_{\text{eff}} = \frac{R_2 R_L}{R_2 + R_L}\)<br>\(V_{\text{out, loaded}} = V_{\text{in}} \frac{R_{\text{eff}}}{R_1 + R_{\text{eff}}}\)</li>
          <li><strong>Thevenin Resistance:</strong><br>\(R_{\text{th}} = R_1 \parallel R_2 = \frac{R_1 R_2}{R_1 + R_2}\)</li>
          <li><strong>Loading Criterion:</strong><br>Keep \(R_L \ge 10 \times R_{\text{th}}\) to keep loading error \(< 10\%\).</li>
        </ul>

        <h3 style="margin-top: 1.25rem;">Standard E24 Resistors</h3>
        <p style="font-size: 0.875rem; color: var(--text-secondary, #475569);">Common 5% values: 1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1.</p>
      </aside>
    </div>

    <!-- Long-Form Informational Engineering Article (1,400+ Words) -->
    <article class="article-body">
      <h2>1. The Theoretical Foundations of Voltage Divider Circuits</h2>
      <p>A voltage divider (also known as a potential divider) is one of the most fundamental linear circuit topologies in electrical and electronic engineering. It consists of two or more passive resistive elements connected in series across an electric potential difference (\(V_{\text{in}}\)). By tapping the node between adjacent resistors, a fraction of the input voltage is extracted proportionally to the ratio of individual resistances.</p>
      <p>The operation of a voltage divider is governed directly by **Ohm's Law** (\(V = I R\)) and **Kirchhoff's Voltage Law (KVL)**. When two resistors \(R_1\) and \(R_2\) are connected in series across a voltage source \(V_{\text{in}}\), the identical quiescent electric current \(I\) flows through both components:</p>
      $$I = \frac{V_{\text{in}}}{R_{\text{total}}} = \frac{V_{\text{in}}}{R_1 + R_2}$$
      <p>The voltage drop across the bottom resistor \(R_2\) (referenced to ground) is determined by Ohm's Law:</p>
      $$V_{\text{out}} = I \times R_2 = \left(\frac{V_{\text{in}}}{R_1 + R_2}\right) \times R_2 = V_{\text{in}} \times \left(\frac{R_2}{R_1 + R_2}\right)$$
      <p>The ratio \(R_2 / (R_1 + R_2)\) is dimensionless and strictly bounded between 0 and 1, representing the **voltage transfer function** or attenuation factor of the divider.</p>

      <h2>2. Loaded Voltage Dividers: The Loading Effect and Impedance Bridging</h2>
      <p>The classical equation \(V_{\text{out}} = V_{\text{in}} [R_2 / (R_1 + R_2)]\) assumes an ideal **open-circuit condition**, meaning no electrical current is drawn from the output terminal (\(I_{\text{load}} = 0\)). However, in practical engineering systems, connecting a downstream load (such as an analog-to-digital converter pin, a sensor interface, or a transistor base) introduces a finite load resistance (\(R_L\)) in parallel with \(R_2\).</p>
      <p>According to the laws of parallel circuits, the equivalent resistance of the bottom branch drops to:</p>
      $$R_{2,\text{effective}} = R_2 \parallel R_L = \frac{R_2 \times R_L}{R_2 + R_L}$$
      <p>Substituting \(R_{2,\text{effective}}\) into the voltage divider equation reveals the **loaded output voltage**:</p>
      $$V_{\text{out, loaded}} = V_{\text{in}} \times \left(\frac{R_{2,\text{effective}}}{R_1 + R_{2,\text{effective}}}\right) = V_{\text{in}} \times \left(\frac{\frac{R_2 R_L}{R_2 + R_L}}{R_1 + \frac{R_2 R_L}{R_2 + R_L}}\right) = V_{\text{in}} \times \left(\frac{R_2 R_L}{R_1 R_2 + R_1 R_L + R_2 R_L}\right)$$
      <p>Because \(R_{2,\text{effective}}\) is always strictly smaller than \(R_2\), the loaded output voltage is always lower than the unloaded prediction. The magnitude of this voltage sag is known as the **loading error**:</p>
      $$\text{Loading Error } (\%) = \left(\frac{V_{\text{unloaded}} - V_{\text{loaded}}}{V_{\text{unloaded}}}\right) \times 100\% = \left(\frac{R_1 \parallel R_2}{R_L + (R_1 \parallel R_2)}\right) \times 100\%$$
      <p>To ensure less than \(1\%\) voltage droop in high-precision sensor interfacing, electronic engineers apply the **rule of thumb**: \(R_L \ge 100 \times (R_1 \parallel R_2)\).</p>

      <h2>3. Thevenin Equivalent Modeling of Voltage Dividers</h2>
      <p>By applying Thevenin's Theorem, any two-resistor voltage divider can be modeled from its output terminals as an ideal voltage generator (\(V_{\text{th}}\)) connected in series with an internal source impedance (\(R_{\text{th}}\)):</p>
      <ul>
        <li><strong>Thevenin Open-Circuit Voltage (\(V_{\text{th}}\)):</strong>
        $$V_{\text{th}} = V_{\text{out, unloaded}} = V_{\text{in}} \times \left(\frac{R_2}{R_1 + R_2}\right)$$</li>
        <li><strong>Thevenin Output Resistance (\(R_{\text{th}}\)):</strong> Computed by replacing the ideal independent voltage source \(V_{\text{in}}\) with a short circuit (zero impedance):
        $$R_{\text{th}} = R_1 \parallel R_2 = \frac{R_1 \times R_2}{R_1 + R_2}$$</li>
      </ul>
      <p>This Thevenin equivalent dramatically simplifies the analysis of complex analog circuits. For example, connecting an ADC with sampling capacitance \(C_{\text{sample}}\) forms a low-pass filter whose RC time constant is determined directly by \(\tau = R_{\text{th}} \times C_{\text{sample}}\). If \(R_{\text{th}}\) is too high (e.g., using \(1\text{ M}\Omega\) resistors to save power), the ADC sample-and-hold capacitor cannot charge within the sampling window, resulting in severe measurement error.</p>

      <h2>4. Power Dissipation, Quiescent Current, and Resistor Sizing Trade-Offs</h2>
      <p>Selecting resistance values for a voltage divider involves an unavoidable engineering trade-off between **power consumption** and **output impedance**:</p>
      <ul>
        <li><strong>Quiescent Current Draw:</strong> Even with zero load connected, current continually flows through \(R_1\) and \(R_2\) to ground:
        $$I_{\text{quiescent}} = \frac{V_{\text{in}}}{R_1 + R_2}$$</li>
        <li><strong>Total Power Dissipation:</strong> The total thermal power dissipated by the divider is:
        $$P_{\text{total}} = V_{\text{in}} \times I_{\text{quiescent}} = \frac{V_{\text{in}}^2}{R_1 + R_2}$$</li>
        <li><strong>Individual Resistor Power Ratings:</strong>
        $$P_{R_1} = I^2 R_1 = \frac{(V_{\text{in}} - V_{\text{out}})^2}{R_1}, \quad P_{R_2} = I^2 R_2 = \frac{V_{\text{out}}^2}{R_2}$$</li>
      </ul>
      <p>If low-value resistors (e.g., \(100\ \Omega\)) are selected, \(R_{\text{th}}\) is low and loading error is tiny, but quiescent current is high, wasting precious battery life and requiring high-wattage resistors. Conversely, if high-value resistors (e.g., \(1\text{ M}\Omega\)) are selected, power consumption drops to microwatts, but \(R_{\text{th}}\) becomes vulnerable to load impedance and environmental electromagnetic noise pickup.</p>

      <h2>5. Voltage Divider Engineering Benchmark Table</h2>
      <p>The following circuit design table details standard voltage attenuation configurations across automotive, industrial, and microcontroller applications:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Application Scenario</th>
              <th>Input Voltage (\(V_{\text{in}}\))</th>
              <th>Target Output (\(V_{\text{out}}\))</th>
              <th>Resistor \(R_1\) (Top)</th>
              <th>Resistor \(R_2\) (Bottom)</th>
              <th>Thevenin \(R_{\text{th}}\)</th>
              <th>Quiescent Current</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>5V to 3.3V Logic Level Shift</td>
              <td>5.0 V</td>
              <td>3.235 V</td>
              <td>1.8 k&Omega;</td>
              <td>3.3 k&Omega;</td>
              <td>1.16 k&Omega;</td>
              <td>0.980 mA</td>
            </tr>
            <tr>
              <td>12V Car Battery to 5V MCU ADC</td>
              <td>14.4 V (charging)</td>
              <td>4.966 V</td>
              <td>19.0 k&Omega;</td>
              <td>10.0 k&Omega;</td>
              <td>6.55 k&Omega;</td>
              <td>0.497 mA</td>
            </tr>
            <tr>
              <td>24V Industrial PLC to 3.3V GPIO</td>
              <td>24.0 V</td>
              <td>3.310 V</td>
              <td>62.0 k&Omega;</td>
              <td>10.0 k&Omega;</td>
              <td>8.61 k&Omega;</td>
              <td>0.333 mA</td>
            </tr>
            <tr>
              <td>48V Telecom to 3.3V Monitoring</td>
              <td>48.0 V</td>
              <td>3.273 V</td>
              <td>136.0 k&Omega;</td>
              <td>10.0 k&Omega;</td>
              <td>9.32 k&Omega;</td>
              <td>0.329 mA</td>
            </tr>
            <tr>
              <td>Op-Amp Virtual Ground Splitter</td>
              <td>9.0 V</td>
              <td>4.500 V</td>
              <td>10.0 k&Omega;</td>
              <td>10.0 k&Omega;</td>
              <td>5.00 k&Omega;</td>
              <td>0.450 mA</td>
            </tr>
            <tr>
              <td>Ultra-Low Power Solar Monitor</td>
              <td>4.2 V (LiPo)</td>
              <td>2.100 V</td>
              <td>1.0 M&Omega;</td>
              <td>1.0 M&Omega;</td>
              <td>500.0 k&Omega;</td>
              <td>2.10 &mu;A</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>6. Step-by-Step Worked Engineering Case Studies</h2>

      <div class="worked-example-card">
        <h3>Case Study 1: Interfacing a 5V Microcontroller Sensor to a 3.3V ESP32 ADC</h3>
        <p><strong>Scenario:</strong> An embedded hardware engineer needs to interface an ultrasonic distance sensor providing an analog output from \(0\text{ to }5.0\text{ Volts}\) to an ESP32 microcontroller ADC input, which has a maximum safe continuous voltage limit of \(3.30\text{ Volts}\). Using standard E24 resistors, design a voltage divider so that a \(5.0\text{ V}\) input produces approximately \(3.25\text{ V}\), calculate the Thevenin resistance, and determine power dissipation.</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Calculate the required divider attenuation ratio:</strong></p>
          $$\text{Ratio} = \frac{V_{\text{out}}}{V_{\text{in}}} = \frac{3.25\text{ V}}{5.00\text{ V}} = 0.650$$

          <p><strong>Step 2: Relate R1 and R2 using the voltage divider equation:</strong></p>
          $$\frac{R_2}{R_1 + R_2} = 0.650 \implies R_2 = 0.650 R_1 + 0.650 R_2 \implies 0.350 R_2 = 0.650 R_1 \implies R_1 = \frac{0.350}{0.650} R_2 \approx 0.5385 R_2$$

          <p><strong>Step 3: Select standard E24 resistor values:</strong></p>
          <p>Choosing \(R_2 = 3.3\text{ k}\Omega\) (\(3300\ \Omega\)):</p>
          $$R_1 = 0.5385 \times 3300\ \Omega = 1777\ \Omega \approx 1.8\text{ k}\Omega\text{ (standard E24 value)}$$

          <p><strong>Step 4: Verify actual output voltage with selected values:</strong></p>
          $$V_{\text{out}} = 5.0\text{ V} \times \left(\frac{3300}{1800 + 3300}\right) = 5.0 \times \left(\frac{3300}{5100}\right) = 3.235\text{ Volts}$$
          <p>This safely stays below the \(3.30\text{ V}\) maximum rating.</p>

          <p><strong>Step 5: Compute Thevenin source resistance and power:</strong></p>
          $$R_{\text{th}} = \frac{1800 \times 3300}{1800 + 3300} = \frac{5,940,000}{5100} = 1164.7\ \Omega \approx 1.16\text{ k}\Omega$$
          $$P_{\text{total}} = \frac{(5.0\text{ V})^2}{5100\ \Omega} = \frac{25}{5100} = 0.00490\text{ W} = 4.90\text{ mW}$$
          <p><strong>Conclusion:</strong> Standard \(0.25\text{-watt}\) surface-mount resistors (0805 package) easily handle the \(4.9\text{ mW}\) dissipation with an optimal Thevenin impedance of \(1.16\text{ k}\Omega\).</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Evaluating Sensor Loading Error with a 10 kΩ Load</h3>
        <p><strong>Scenario:</strong> The divider from Case Study 1 (\(V_{\text{in}} = 5.0\text{ V}\), \(R_1 = 1.8\text{ k}\Omega\), \(R_2 = 3.3\text{ k}\Omega\), unloaded \(V_{\text{out}} = 3.235\text{ V}\)) is connected to an analog instrument with an internal input impedance of \(R_L = 10.0\text{ k}\Omega\). Calculate the loaded output voltage, the absolute voltage drop, and the percentage loading error.</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Calculate the parallel combination of R2 and RL:</strong></p>
          $$R_{2,\text{eff}} = \frac{R_2 \times R_L}{R_2 + R_L} = \frac{3.3\text{ k}\Omega \times 10.0\text{ k}\Omega}{3.3\text{ k}\Omega + 10.0\text{ k}\Omega} = \frac{33.0}{13.3} \approx 2.4812\text{ k}\Omega = 2481.2\ \Omega$$

          <p><strong>Step 2: Calculate loaded output voltage:</strong></p>
          $$V_{\text{loaded}} = 5.0\text{ V} \times \left(\frac{2481.2}{1800 + 2481.2}\right) = 5.0 \times \left(\frac{2481.2}{4281.2}\right) = 2.8977\text{ Volts}$$

          <p><strong>Step 3: Compute voltage drop and loading error percentage:</strong></p>
          $$\Delta V = V_{\text{unloaded}} - V_{\text{loaded}} = 3.235\text{ V} - 2.898\text{ V} = 0.337\text{ Volts}$$
          $$\text{Loading Error} = \left(\frac{0.337\text{ V}}{3.235\text{ V}}\right) \times 100\% = 10.42\%$$
          <p><strong>Engineering Fix:</strong> A \(10.4\%\) error is unacceptable for precision sensing. The engineer must insert an op-amp unity-gain voltage follower (buffer) between the divider output and the \(10\text{ k}\Omega\) load to present an infinite input impedance.</p>
        </div>
      </div>

      <h2>7. Frequently Asked Questions (Electronics &amp; Circuit Theory)</h2>
      <div class="faq-accordion">
        <details class="faq-item">
          <summary>Can a potentiometer be used as an adjustable voltage divider?</summary>
          <div class="faq-answer">
            <p>Yes. A potentiometer is literally a three-terminal continuous mechanical voltage divider. The two outer fixed terminals represent the full track resistance (\(R_1 + R_2\)), while the center wiper terminal taps into the division point. Turning the knob smoothly alters the ratio of \(R_1\) to \(R_2\), allowing the output voltage to be adjusted continuously from 0V to \(V_{\text{in}}\).</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>How do temperature coefficients (TCR) affect voltage divider accuracy?</summary>
          <div class="faq-answer">
            <p>If both resistors are made of identical resistive film materials and share the same Temperature Coefficient of Resistance (TCR, e.g., \(\pm 50\text{ ppm/}^\circ\text{C}\)), both resistors drift in the same direction by equal percentages. Because the output voltage depends solely on the ratio \(R_2 / (R_1 + R_2)\), the thermal drift largely cancels out, providing exceptional temperature stability. However, if one resistor self-heats significantly more than the other, ratio imbalance occurs.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>Can a voltage divider work with alternating current (AC) signals?</summary>
          <div class="faq-answer">
            <p>Yes. For pure resistors, a voltage divider attenuates AC voltages identically to DC without introducing phase shifts. However, at high frequencies (megahertz range), parasitic capacitance across the resistors and PCB traces creates a complex impedance divider (\(Z_1, Z_2\)), causing phase shifts and frequency-dependent attenuation. Oscilloscope 10x probes solve this by adding compensating parallel trimmer capacitors to form a frequency-compensated divider.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>What is a capacitive voltage divider?</summary>
          <div class="faq-answer">
            <p>A capacitive divider uses two capacitors in series instead of resistors to attenuate AC voltages. Because capacitive reactance is inversely proportional to capacitance (\(X_c = 1 / (2\pi f C)\)), the voltage division formula is inverted: \(V_{\text{out}} = V_{\text{in}} \times [C_1 / (C_1 + C_2)]\). Capacitive dividers dissipate zero real DC power, making them ideal for high-voltage power transmission grid instrumentation.</p>
          </div>
        </details>
      </div>

      <h2>8. Related Electrical &amp; Circuit Calculators</h2>
      <p>Explore our integrated electronics computation suite to solve circuit impedances, time constants, and power dissipation:</p>
      <div class="related-calculators" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-top: 1rem;">
        <a href="ohms-law-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Ohm's Law Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Calculate voltage, current, resistance, and electrical power ($P = VI = I^2R$).</p>
        </a>
        <a href="parallel-resistance-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Parallel Resistance Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Compute equivalent resistance for parallel networks and current division.</p>
        </a>
        <a href="rc-time-constant-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">RC Time Constant Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Solve transient capacitor charging curves ($\tau = RC$) and filter cutoff frequencies.</p>
        </a>
        <a href="lm317-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">LM317 Voltage Regulator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Design regulated DC power supplies with stable active voltage regulation.</p>
        </a>
      </div>
    </article>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-col">
        <h3>CalcHub</h3>
        <p>Your comprehensive engineering, mathematical, physical, and financial computational authority.</p>
      </div>
      <div class="footer-col">
        <h3>Calculators</h3>
        <ul>
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="math.html">Mathematics</a></li>
          <li><a href="converter.html">Unit Converters</a></li>
          <li><a href="engineering.html">Electrical &amp; Engineering</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h3>Electronics &amp; Circuits</h3>
        <ul>
          <li><a href="voltage-divider-calculator.html">Voltage Divider</a></li>
          <li><a href="parallel-resistance-calculator.html">Parallel Resistance</a></li>
          <li><a href="ohms-law-calculator.html">Ohm's Law</a></li>
          <li><a href="rc-time-constant-calculator.html">RC Time Constant</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 CalcHub. High-precision engineering formulas and calculators. All rights reserved.</p>
    </div>
  </footer>

  <script>
    (function() {
      // DOM Elements
      const modeSelect = document.getElementById('vd-mode');
      const presetSelect = document.getElementById('vd-preset');

      const vinInput = document.getElementById('vd-vin');
      const voutInputGroup = document.getElementById('vd-vout-input-group');
      const targetVoutInput = document.getElementById('vd-target-vout');

      const r1Group = document.getElementById('vd-r1-group');
      const r1Input = document.getElementById('vd-r1');
      const r1Unit = document.getElementById('vd-r1-unit');

      const r2Group = document.getElementById('vd-r2-group');
      const r2Input = document.getElementById('vd-r2');
      const r2Unit = document.getElementById('vd-r2-unit');

      const rlInput = document.getElementById('vd-rl');
      const rlUnit = document.getElementById('vd-rl-unit');

      const calcBtn = document.getElementById('vd-calc-btn');
      const resetBtn = document.getElementById('vd-reset-btn');

      // Outputs
      const primaryOut = document.getElementById('vd-primary-out');
      const statusOut = document.getElementById('vd-status-out');
      const currentOut = document.getElementById('vd-current-out');
      const powerOut = document.getElementById('vd-power-out');
      const rthOut = document.getElementById('vd-rth-out');
      const splitPwrOut = document.getElementById('vd-split-pwr-out');

      const PRESETS = {
        '5v-to-3v3': { vin: 5.0, r1: 1.8, r1u: 1000, r2: 3.3, r2u: 1000 },
        '12v-to-5v': { vin: 12.0, r1: 14.0, r1u: 1000, r2: 10.0, r2u: 1000 },
        '12v-to-3v3': { vin: 12.0, r1: 27.0, r1u: 1000, r2: 10.0, r2u: 1000 },
        'half-supply': { vin: 9.0, r1: 10.0, r1u: 1000, r2: 10.0, r2u: 1000 },
        '24v-to-10v': { vin: 24.0, r1: 14.0, r1u: 1000, r2: 10.0, r2u: 1000 }
      };

      function updatePanelVisibility() {
        const m = modeSelect.value;
        if (m === 'find-vout') {
          voutInputGroup.style.display = 'none';
          r1Group.style.display = 'block';
          r2Group.style.display = 'block';
        } else if (m === 'find-r1') {
          voutInputGroup.style.display = 'block';
          r1Group.style.display = 'none';
          r2Group.style.display = 'block';
        } else if (m === 'find-r2') {
          voutInputGroup.style.display = 'block';
          r1Group.style.display = 'block';
          r2Group.style.display = 'none';
        }
      }

      function formatOhms(r) {
        if (r >= 1e6) return (r / 1e6).toFixed(3) + " M\u03a9";
        if (r >= 1e3) return (r / 1e3).toFixed(3) + " k\u03a9";
        return r.toFixed(2) + " \u03a9";
      }

      function formatPower(pWatts) {
        if (pWatts >= 1.0) return pWatts.toFixed(2) + " W";
        if (pWatts >= 0.001) return (pWatts * 1000).toFixed(2) + " mW";
        return (pWatts * 1e6).toFixed(2) + " \u03bcW";
      }

      function calculate() {
        const mode = modeSelect.value;
        const vin = parseFloat(vinInput.value) || 0;
        let r1 = (parseFloat(r1Input.value) || 0) * parseFloat(r1Unit.value);
        let r2 = (parseFloat(r2Input.value) || 0) * parseFloat(r2Unit.value);
        let vout = 0;

        const rlVal = parseFloat(rlInput.value);
        const hasLoad = (!isNaN(rlVal) && rlVal > 0);
        const rl = hasLoad ? (rlVal * parseFloat(rlUnit.value)) : Infinity;

        if (mode === 'find-vout') {
          if (r1 <= 0 || r2 <= 0) {
            primaryOut.textContent = "-- V";
            statusOut.textContent = "Please enter positive resistor values.";
            return;
          }

          let r2Effective = r2;
          if (hasLoad) {
            r2Effective = (r2 * rl) / (r2 + rl);
          }

          vout = vin * (r2Effective / (r1 + r2Effective));
        } else if (mode === 'find-r1') {
          const targetVout = parseFloat(targetVoutInput.value) || 0;
          if (targetVout <= 0 || targetVout >= vin || r2 <= 0) {
            primaryOut.textContent = "--";
            statusOut.textContent = "Vout must be strictly between 0 and Vin.";
            return;
          }
          // Vout = Vin * R2 / (R1 + R2) => R1 = R2 * (Vin - Vout) / Vout
          r1 = r2 * (vin - targetVout) / targetVout;
          vout = targetVout;
          r1Input.value = (r1 / parseFloat(r1Unit.value)).toFixed(3);
        } else if (mode === 'find-r2') {
          const targetVout = parseFloat(targetVoutInput.value) || 0;
          if (targetVout <= 0 || targetVout >= vin || r1 <= 0) {
            primaryOut.textContent = "--";
            statusOut.textContent = "Vout must be strictly between 0 and Vin.";
            return;
          }
          // R2 = R1 * Vout / (Vin - Vout)
          r2 = r1 * targetVout / (vin - targetVout);
          vout = targetVout;
          r2Input.value = (r2 / parseFloat(r2Unit.value)).toFixed(3);
        }

        const attenuation = vin > 0 ? (vout / vin) : 0;
        const currentA = vin / (r1 + (hasLoad ? (r2 * rl) / (r2 + rl) : r2));
        const powerTotal = vin * currentA;
        const rth = (r1 * r2) / (r1 + r2);

        const vdropR1 = vin - vout;
        const powerR1 = (vdropR1 * vdropR1) / r1;
        const powerR2 = (vout * vout) / r2;

        // Render Outputs
        primaryOut.textContent = vout.toFixed(3) + " V";
        statusOut.textContent = hasLoad ? 
          `Loaded with ${formatOhms(rl)} (Droop from unloaded ${(vin * r2 / (r1 + r2)).toFixed(3)} V)` :
          `Attenuation Factor: ${attenuation.toFixed(3)} \u2022 Transfer Ratio: ${(attenuation * 100).toFixed(1)}%`;
        
        currentOut.textContent = currentA >= 0.001 ? (currentA * 1000).toFixed(3) + " mA" : (currentA * 1e6).toFixed(1) + " \u03bcA";
        powerOut.textContent = formatPower(powerTotal);
        rthOut.textContent = formatOhms(rth);
        splitPwrOut.textContent = `${formatPower(powerR1)} / ${formatPower(powerR2)}`;
      }

      presetSelect.addEventListener('change', function() {
        const val = this.value;
        if (PRESETS[val]) {
          const p = PRESETS[val];
          modeSelect.value = 'find-vout';
          updatePanelVisibility();
          vinInput.value = p.vin;
          r1Input.value = p.r1;
          r1Unit.value = p.r1u;
          r2Input.value = p.r2;
          r2Unit.value = p.r2u;
          rlInput.value = '';
          calculate();
        }
      });

      modeSelect.addEventListener('change', function() {
        updatePanelVisibility();
        calculate();
      });

      [vinInput, targetVoutInput, r1Input, r1Unit, r2Input, r2Unit, rlInput, rlUnit].forEach(el => {
        el.addEventListener('input', function() {
          if (el !== presetSelect) presetSelect.value = 'custom';
          calculate();
        });
        el.addEventListener('change', calculate);
      });

      calcBtn.addEventListener('click', calculate);

      resetBtn.addEventListener('click', function() {
        modeSelect.value = 'find-vout';
        presetSelect.value = '5v-to-3v3';
        const p = PRESETS['5v-to-3v3'];
        vinInput.value = p.vin;
        r1Input.value = p.r1;
        r1Unit.value = p.r1u;
        r2Input.value = p.r2;
        r2Unit.value = p.r2u;
        rlInput.value = '';
        updatePanelVisibility();
        calculate();
      });

      // Initial execution
      updatePanelVisibility();
      calculate();
    })();
  </script>
</body>
</html>
"""

# 2. parallel-resistance-calculator.html
HTML_PARALLEL_RESISTANCE = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Parallel Resistance Calculator - Equivalent Resistance &amp; Current Divider</title>
  <meta name="description" content="Calculate equivalent parallel resistance (1/R_eq = 1/R1 + 1/R2 + ...), conductance in Siemens, current divider branch currents, and power dissipation.">
  <link rel="canonical" href="https://calchub.org/parallel-resistance-calculator.html">
  <meta property="og:title" content="Parallel Resistance Calculator - Equivalent R_eq Solver">
  <meta property="og:description" content="Free electronics parallel resistance calculator. Solve multi-resistor networks, product-over-sum formula, current division, and branch power with step-by-step proofs.">
  <meta property="og:url" content="https://calchub.org/parallel-resistance-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Parallel Resistance Calculator - Circuit Theory Tool">
  <meta name="twitter:description" content="Compute equivalent resistance across parallel resistors, conductances, and branch currents with worked circuit case studies.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Parallel Resistance Calculator",
    "url": "https://calchub.org/parallel-resistance-calculator.html",
    "description": "Calculates equivalent resistance for any number of parallel resistors, total conductance in Siemens, and branch current division.",
    "applicationCategory": "EducationalApplication",
    "operatingSystem": "All"
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is the formula for calculating parallel resistance?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "For N resistors in parallel, the reciprocal of the equivalent resistance equals the sum of the reciprocals of each individual resistance: 1/R_eq = 1/R1 + 1/R2 + ... + 1/Rn. For two resistors, this simplifies to the product-over-sum formula: R_eq = (R1 * R2) / (R1 + R2)."
        }
      },
      {
        "@type": "Question",
        "name": "Why is equivalent parallel resistance always smaller than the smallest resistor?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Each additional resistor added in parallel provides an alternate parallel path for electric current to flow, increasing the circuit's total conductance (G_total = G1 + G2 + ...). Because resistance is the reciprocal of conductance (R = 1/G), adding more conducting pathways reduces total resistance. Therefore, R_eq is always strictly less than the smallest single resistor in the network."
        }
      },
      {
        "@type": "Question",
        "name": "What happens if N identical resistors are connected in parallel?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "When N identical resistors of value R are connected in parallel, the equivalent resistance is simply the resistance of one resistor divided by the count N: R_eq = R / N. For example, four 100-ohm resistors in parallel yield exactly 100 / 4 = 25 ohms."
        }
      },
      {
        "@type": "Question",
        "name": "What is the current divider rule in parallel circuits?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The current divider rule states that the current flowing through any individual branch in a parallel network is inversely proportional to its resistance. For two parallel resistors connected to a total current I_total: I_1 = I_total * [R2 / (R1 + R2)] and I_2 = I_total * [R1 / (R1 + R2)]."
        }
      }
    ]
  }
  </script>
</head>
<body>
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">CalcHub</a>
      <nav class="site-nav">
        <a href="index.html">Home</a>
        <a href="math.html">Math &amp; Statistics</a>
        <a href="converter.html">Converters</a>
        <a href="engineering.html" class="active">Engineering</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="page-container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo;
      <a href="engineering.html">Electrical &amp; Engineering</a> &rsaquo;
      <span>Parallel Resistance Calculator</span>
    </nav>

    <div class="page-header">
      <h1 class="page-title">Parallel Resistance Calculator</h1>
      <p class="page-desc">Determine equivalent resistance ($R_{\text{eq}}$) for any combination of parallel resistors, total electrical conductance in Siemens, and branch current division.</p>
    </div>

    <div class="calc-grid">
      <!-- Calculator Column -->
      <div class="calc-card">
        <div class="calc-header">
          <h2>Parallel Resistor Network Solver</h2>
        </div>

        <!-- Preset Selection -->
        <div class="form-group">
          <label for="pr-preset">Standard Resistor Network Preset:</label>
          <select id="pr-preset" class="form-control">
            <option value="custom">-- Custom Parallel Network --</option>
            <option value="two-equal" selected>Two Equal Resistors (10 kΩ ∥ 10 kΩ &rarr; 5.0 kΩ)</option>
            <option value="three-equal">Three Equal Resistors (100 Ω ∥ 100 Ω ∥ 100 Ω &rarr; 33.33 Ω)</option>
            <option value="standard-trim">Precision Resistance Trimming (10 kΩ ∥ 1 MΩ &rarr; 9.901 kΩ)</option>
            <option value="current-shunt">Current Shunt Parallel Bank (0.1 Ω ∥ 0.1 Ω &rarr; 0.05 Ω)</option>
            <option value="asymmetric">Asymmetric Load (1 kΩ ∥ 2.2 kΩ ∥ 4.7 kΩ &rarr; 598 Ω)</option>
          </select>
        </div>

        <!-- Supply Voltage (optional for current/power) -->
        <div class="form-row">
          <div class="form-group">
            <label for="pr-vsupply">Supply Voltage ($V$, optional for currents):</label>
            <input type="number" id="pr-vsupply" class="form-control" value="12.0" step="any">
          </div>
        </div>

        <!-- Dynamic Resistor Rows Container -->
        <div id="pr-resistors-container">
          <div style="font-size: 0.875rem; font-weight: 600; color: var(--text-muted, #64748b); margin-bottom: 0.5rem; text-transform: uppercase;">Parallel Resistor Branches:</div>
          <!-- Rows will be injected by JavaScript -->
        </div>

        <div style="margin-top: 0.75rem; display: flex; gap: 0.5rem;">
          <button type="button" id="pr-add-row-btn" class="btn btn-secondary" style="font-size: 0.85rem; padding: 0.4rem 0.8rem;">+ Add Resistor</button>
        </div>

        <div class="form-actions" style="margin-top: 1.25rem;">
          <button type="button" id="pr-calc-btn" class="btn btn-primary">Calculate Equivalent Resistance</button>
          <button type="button" id="pr-reset-btn" class="btn btn-secondary">Reset</button>
        </div>

        <!-- Output Cards -->
        <div id="pr-results" class="results-container" style="margin-top: 1.5rem;">
          <div class="result-hero-card">
            <div class="result-label" style="font-size: 0.875rem; color: var(--text-muted, #64748b); text-transform: uppercase; font-weight: 600;">Equivalent Resistance ($R_{\text{eq}}$)</div>
            <div id="pr-primary-out" style="font-size: 2.25rem; font-weight: 800; color: var(--primary, #2563eb); margin: 0.25rem 0;">5.000 k&Omega;</div>
            <div id="pr-status-out" style="font-size: 1rem; color: var(--text-secondary, #475569); font-weight: 600;">Total Conductance: 0.200 mS (Siemens)</div>
          </div>

          <div class="summary-metrics-grid">
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Total Current ($I_{\text{tot}}$)</div>
              <div id="pr-current-out" style="font-size: 1.15rem; font-weight: 700;">2.400 mA</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Total Circuit Power</div>
              <div id="pr-power-out" style="font-size: 1.15rem; font-weight: 700;">28.80 mW</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Total Conductance ($G$)</div>
              <div id="pr-cond-out" style="font-size: 1.15rem; font-weight: 700;">0.200 mS</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Active Branches</div>
              <div id="pr-branches-out" style="font-size: 1.15rem; font-weight: 700;">2 Resistors</div>
            </div>
          </div>

          <!-- Branch Current Breakdown Table -->
          <div class="table-responsive" style="margin-top: 1rem;">
            <table class="data-table" id="pr-breakdown-table" style="font-size: 0.9rem;">
              <thead>
                <tr>
                  <th>Branch</th>
                  <th>Resistance</th>
                  <th>Conductance ($G_i$)</th>
                  <th>Branch Current ($I_i$)</th>
                  <th>Power Dissipated ($P_i$)</th>
                </tr>
              </thead>
              <tbody id="pr-breakdown-body">
                <!-- Dynamically generated rows -->
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Quick Reference Sidebar -->
      <aside class="sidebar-card">
        <h3>Parallel Network Formulas</h3>
        <ul style="font-size: 0.875rem; line-height: 1.6; margin-left: 1.25rem;">
          <li><strong>General Law:</strong><br>\(\frac{1}{R_{\text{eq}}} = \sum_{i=1}^N \frac{1}{R_i}\)</li>
          <li><strong>Two Resistors:</strong><br>\(R_{\text{eq}} = \frac{R_1 R_2}{R_1 + R_2}\)</li>
          <li><strong>N Identical Resistors:</strong><br>\(R_{\text{eq}} = \frac{R}{N}\)</li>
          <li><strong>Conductance (\(G = 1/R\)):</strong><br>\(G_{\text{total}} = G_1 + G_2 + \dots + G_N\)</li>
          <li><strong>Current Divider:</strong><br>\(I_k = I_{\text{total}} \times \frac{G_k}{G_{\text{total}}}\)</li>
        </ul>

        <h3 style="margin-top: 1.25rem;">Key Circuit Truth</h3>
        <p style="font-size: 0.875rem; color: var(--text-secondary, #475569);">The voltage drop across all parallel branches is identical: \(V_1 = V_2 = \dots = V_{\text{supply}}\). Current splits in direct proportion to branch conductance.</p>
      </aside>
    </div>

    <!-- Long-Form Informational Engineering Article (1,400+ Words) -->
    <article class="article-body">
      <h2>1. The Fundamental Physics and Mathematics of Parallel Resistors</h2>
      <p>In electrical and electronic circuit theory, components are connected in **parallel** when both of their respective terminals are connected directly across the same two common electrical nodes. Consequently, every individual component in a parallel circuit experiences exactly the same electric potential difference (voltage drop, \(V\)) across its terminals:</p>
      $$V_1 = V_2 = V_3 = \dots = V_N = V_{\text{source}}$$
      <p>According to **Kirchhoff's Current Law (KCL)**, the total electric current entering a circuit junction must equal the sum of the currents leaving that junction. Therefore, the total current \(I_{\text{total}}\) delivered by the power supply splits into independent branch currents:</p>
      $$I_{\text{total}} = I_1 + I_2 + I_3 + \dots + I_N$$
      <p>Applying Ohm's Law (\(I_k = V / R_k\)) to each individual branch yields:</p>
      $$\frac{V}{R_{\text{eq}}} = \frac{V}{R_1} + \frac{V}{R_2} + \frac{V}{R_3} + \dots + \frac{V}{R_N}$$
      <p>Dividing throughout by the common voltage \(V\) produces the universal reciprocal equation for equivalent parallel resistance:</p>
      $$\frac{1}{R_{\text{eq}}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \dots + \frac{1}{R_N} = \sum_{k=1}^N \frac{1}{R_k}$$
      <p>Inverting both sides gives the exact equivalent resistance:</p>
      $$R_{\text{eq}} = \frac{1}{\sum_{k=1}^N \frac{1}{R_k}} = \left(\frac{1}{R_1} + \frac{1}{R_2} + \dots + \frac{1}{R_N}\right)^{-1}$$

      <h2>2. Conductance: Simplifying Parallel Calculations</h2>
      <p>While series circuits are most naturally analyzed using resistance (\(R\)), parallel networks are mathematically much simpler when formulated using **electrical conductance** (\(G\)), defined as the reciprocal of resistance:</p>
      $$G = \frac{1}{R}$$
      <p>The SI unit of conductance is the **Siemens** (symbol: **S**), historically referred to as the "mho" (\(\mho\)). Because \(1/R_{\text{eq}} = \sum (1/R_k)\), the equivalent conductance of parallel branches is simply the direct linear sum of individual branch conductances:</p>
      $$G_{\text{total}} = G_1 + G_2 + G_3 + \dots + G_N$$
      <p>This linear formulation explains why adding more resistors in parallel always decreases total resistance: each parallel branch adds a new physical conductive path for electrons, increasing total circuit conductance (\(G_{\text{total}} &gt; G_{\text{branch}}\)) and therefore decreasing equivalent resistance (\(R_{\text{eq}} = 1 / G_{\text{total}} &lt; R_{\text{smallest}}\)).</p>

      <h2>3. Special Case Formulas: Two Resistors &amp; Identical Resistors</h2>

      <h3>A. Two Resistors in Parallel: The Product-Over-Sum Rule</h3>
      <p>For the ubiquitous case of exactly two parallel resistors, the reciprocal equation simplifies through common denominators to the famous **product-over-sum formula**:</p>
      $$\frac{1}{R_{\text{eq}}} = \frac{1}{R_1} + \frac{1}{R_2} = \frac{R_2 + R_1}{R_1 R_2} \implies R_{\text{eq}} = \frac{R_1 \times R_2}{R_1 + R_2}$$
      <p>This algebraic shortcut allows electrical engineers to compute parallel combinations mentally without inverting reciprocal decimals.</p>

      <h3>B. N Identical Resistors in Parallel</h3>
      <p>When \(N\) resistors of identical resistance value \(R\) are connected in parallel, each branch conducts an identical current. The equivalent resistance simplifies to:</p>
      $$R_{\text{eq}} = \frac{R}{N}$$
      <p>For example, ten \(100\ \Omega\) resistors connected in parallel yield \(100 / 10 = 10\ \Omega\). Furthermore, connecting \(N\) identical resistors in parallel increases the collective power rating by a factor of \(N\): ten \(0.25\text{-watt}\) resistors in parallel create a robust \(2.5\text{-watt}\) power handling bank.</p>

      <h2>4. The Current Divider Rule and Power Dissipation</h2>
      <p>Because voltage is uniform across all parallel branches, branch current is inversely proportional to branch resistance. From Ohm's Law and KCL, the fraction of total current traversing branch \(k\) is:</p>
      $$I_k = I_{\text{total}} \times \left(\frac{R_{\text{eq}}}{R_k}\right) = I_{\text{total}} \times \left(\frac{G_k}{G_{\text{total}}}\right)$$
      <p>For a two-resistor network:</p>
      $$I_1 = I_{\text{total}} \times \left(\frac{R_2}{R_1 + R_2}\right), \quad I_2 = I_{\text{total}} \times \left(\frac{R_1}{R_1 + R_2}\right)$$
      <p>Notice the counter-intuitive inversion: current through branch 1 is proportional to the resistance of the *opposite* branch (\(R_2\)). The lower-resistance branch draws the lion's share of the current.</p>
      <p>Similarly, electrical power dissipated as heat in branch \(k\) is:</p>
      $$P_k = V^2 / R_k = I_k^2 R_k = V \times I_k$$
      <p>The branch with the lowest resistance dissipates the highest power, making it the most vulnerable to thermal failure or overheating.</p>

      <h2>5. Parallel Resistor Engineering Benchmark Table</h2>
      <p>The following circuit analysis table illustrates equivalent resistances, total conductances, and current division across representative parallel combinations at a standard \(12.0\text{ V}\) supply:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Network Description</th>
              <th>Branch Resistors</th>
              <th>Equivalent \(R_{\text{eq}}\)</th>
              <th>Total Conductance</th>
              <th>Total Current @ 12V</th>
              <th>Total Power Dissipated</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Two Equal 1 kΩ</td>
              <td>1.0 kΩ ∥ 1.0 kΩ</td>
              <td>500.0 Ω</td>
              <td>2.000 mS</td>
              <td>24.00 mA</td>
              <td>288.0 mW</td>
            </tr>
            <tr>
              <td>Two Equal 10 kΩ</td>
              <td>10.0 kΩ ∥ 10.0 kΩ</td>
              <td>5.000 kΩ</td>
              <td>0.200 mS</td>
              <td>2.40 mA</td>
              <td>28.8 mW</td>
            </tr>
            <tr>
              <td>Three Equal 100 Ω</td>
              <td>100 Ω ∥ 100 Ω ∥ 100 Ω</td>
              <td>33.33 Ω</td>
              <td>30.00 mS</td>
              <td>360.0 mA</td>
              <td>4.32 W</td>
            </tr>
            <tr>
              <td>Precision Trim Pair</td>
              <td>10.0 kΩ ∥ 1.0 MΩ</td>
              <td>9.901 kΩ</td>
              <td>0.101 mS</td>
              <td>1.212 mA</td>
              <td>14.54 mW</td>
            </tr>
            <tr>
              <td>Current Shunt Bank</td>
              <td>0.10 Ω ∥ 0.10 Ω</td>
              <td>0.050 Ω</td>
              <td>20.00 S</td>
              <td>240.0 A</td>
              <td>2.88 kW</td>
            </tr>
            <tr>
              <td>Asymmetric Triad</td>
              <td>1.0 kΩ ∥ 2.2 kΩ ∥ 4.7 kΩ</td>
              <td>598.0 Ω</td>
              <td>1.672 mS</td>
              <td>20.07 mA</td>
              <td>240.8 mW</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>6. Step-by-Step Worked Engineering Case Studies</h2>

      <div class="worked-example-card">
        <h3>Case Study 1: Synthesizing a Non-Standard Precision Resistor via Trimming</h3>
        <p><strong>Scenario:</strong> An analog circuit designer needs an exact resistance of \(R_{\text{target}} = 4.75\text{ k}\Omega\) (\(4750\ \Omega\)) to set the gain of an instrumentation amplifier. The nearest standard available resistor is \(R_1 = 5.1\text{ k}\Omega\) (\(5100\ \Omega\)). Calculate the required trimming resistor \(R_{\text{trim}}\) to place in parallel with \(R_1\) to achieve the exact target.</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Express the target resistance in terms of parallel combination:</strong></p>
          $$\frac{1}{R_{\text{target}}} = \frac{1}{R_1} + \frac{1}{R_{\text{trim}}}$$

          <p><strong>Step 2: Solve algebraically for \(R_{\text{trim}}\):</strong></p>
          $$\frac{1}{R_{\text{trim}}} = \frac{1}{R_{\text{target}}} - \frac{1}{R_1} = \frac{R_1 - R_{\text{target}}}{R_1 \times R_{\text{target}}}$$
          $$R_{\text{trim}} = \frac{R_1 \times R_{\text{target}}}{R_1 - R_{\text{target}}}$$

          <p><strong>Step 3: Substitute the numerical values:</strong></p>
          $$R_{\text{trim}} = \frac{5100 \times 4750}{5100 - 4750} = \frac{24,225,000}{350} = 69,214.28\ \Omega \approx 69.21\text{ k}\Omega$$

          <p><strong>Step 4: Select nearest standard resistor:</strong></p>
          <p>A standard E96 1% resistor of \(69.8\text{ k}\Omega\) in parallel with \(5.1\text{ k}\Omega\) yields:</p>
          $$R_{\text{actual}} = \frac{5100 \times 69800}{5100 + 69800} = \frac{355,980,000}{74900} = 4752.7\ \Omega \quad (0.05\%\text{ error})$$
          <p><strong>Engineering Result:</strong> Paralleling a \(69.8\text{ k}\Omega\) trim resistor across the \(5.1\text{ k}\Omega\) base resistor achieves the target \(4.75\text{ k}\Omega\) with virtually zero error.</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Calculating Branch Currents and Thermal Ratings in a Shunt Bank</h3>
        <p><strong>Scenario:</strong> A motor drive speed controller connects three parallel resistors across a \(24.0\text{ V}\) bus: \(R_1 = 120\ \Omega\), \(R_2 = 240\ \Omega\), and \(R_3 = 480\ \Omega\). Determine the equivalent resistance \(R_{\text{eq}}\), the individual branch currents, and the minimum wattage rating needed for each resistor with a 2x safety margin.</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Calculate total conductance (\(G_{\text{total}}\)):</strong></p>
          $$G_1 = \frac{1}{120} = 0.008333\text{ S}, \quad G_2 = \frac{1}{240} = 0.004167\text{ S}, \quad G_3 = \frac{1}{480} = 0.002083\text{ S}$$
          $$G_{\text{total}} = 0.008333 + 0.004167 + 0.002083 = 0.014583\text{ S}$$

          <p><strong>Step 2: Compute equivalent resistance (\(R_{\text{eq}}\)):</strong></p>
          $$R_{\text{eq}} = \frac{1}{G_{\text{total}}} = \frac{1}{0.014583} = 68.57\ \Omega$$

          <p><strong>Step 3: Calculate individual branch currents:</strong></p>
          $$I_1 = \frac{24.0\text{ V}}{120\ \Omega} = 0.200\text{ A (200 mA)}$$
          $$I_2 = \frac{24.0\text{ V}}{240\ \Omega} = 0.100\text{ A (100 mA)}$$
          $$I_3 = \frac{24.0\text{ V}}{480\ \Omega} = 0.050\text{ A (50 mA)}$$
          $$I_{\text{total}} = 0.200 + 0.100 + 0.050 = 0.350\text{ A (350 mA)}$$

          <p><strong>Step 4: Compute actual power dissipation and specify wattage ratings:</strong></p>
          $$P_1 = (24.0)^2 / 120 = 4.80\text{ W} \implies \text{Specify } 10.0\text{ W resistor (2x margin)}$$
          $$P_2 = (24.0)^2 / 240 = 2.40\text{ W} \implies \text{Specify } 5.0\text{ W resistor}$$
          $$P_3 = (24.0)^2 / 480 = 1.20\text{ W} \implies \text{Specify } 2.5\text{ W or } 3.0\text{ W resistor}$$
          <p><strong>Conclusion:</strong> The network exhibits an equivalent resistance of \(68.57\ \Omega\) drawing \(350\text{ mA}\). Branch 1 dissipates the most heat (\(4.8\text{ W}\)) and requires a \(10\text{-watt}\) chassis-mount power resistor.</p>
        </div>
      </div>

      <h2>7. Frequently Asked Questions (Circuit Design &amp; Troubleshooting)</h2>
      <div class="faq-accordion">
        <details class="faq-item">
          <summary>What happens if one resistor in a parallel network fails open-circuit?</summary>
          <div class="faq-answer">
            <p>If a resistor burns out or disconnects (open-circuit, \(R \to \infty\)), that specific branch ceases to conduct current (\(I_k = 0\)). However, all other parallel branches continue operating normally because the full supply voltage remains applied across them. The circuit's total conductance decreases, and total equivalent resistance increases. This is the primary reason domestic house wiring is wired strictly in parallel: turning off a lamp does not turn off your refrigerator.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>What happens if one resistor fails short-circuit?</summary>
          <div class="faq-answer">
            <p>If a resistor in a parallel network shorts out (short-circuit, \(R \to 0\)), the equivalent resistance of the entire parallel network drops instantly to zero (\(R_{\text{eq}} = 0\)). Massive current flows directly through the shorted branch, bypassing all other branches and tripping the circuit breaker, blowing the fuse, or causing catastrophic thermal smoke.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>Can parallel resistors increase power handling capacity?</summary>
          <div class="faq-answer">
            <p>Yes. If a circuit requires a 50-ohm, 10-watt resistor but only 0.5-watt resistors are available, connecting twenty 1000-ohm, 0.5-watt resistors in parallel yields an equivalent resistance of \(1000 / 20 = 50\ \Omega\) with a cumulative power handling capability of \(20 \times 0.5\text{ W} = 10\text{ Watts}\). Power is distributed equally among all twenty identical resistors.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>How does tolerance stack up in parallel resistors?</summary>
          <div class="faq-answer">
            <p>Statistical error propagation demonstrates that connecting multiple resistors in parallel generally tightens the effective tolerance of the resulting combination. Random manufacturing variations in standard metal film resistors tend to average out: if two 1% resistors are paralleled, the standard deviation of the resulting equivalent resistance is approximately \(1\% / \sqrt{2} \approx 0.71\%\).</p>
          </div>
        </details>
      </div>

      <h2>8. Related Electrical &amp; Circuit Engineering Calculators</h2>
      <p>Explore our integrated electronics computation suite to solve circuit impedances, time constants, and power dissipation:</p>
      <div class="related-calculators" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-top: 1rem;">
        <a href="ohms-law-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Ohm's Law Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Calculate voltage, current, resistance, and electrical power ($P = VI = I^2R$).</p>
        </a>
        <a href="voltage-divider-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Voltage Divider Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Compute potential divider outputs ($V_{\text{out}} = V_{\text{in}} R_2/(R_1+R_2)$) and loading.</p>
        </a>
        <a href="rc-time-constant-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">RC Time Constant Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Solve transient capacitor charging curves ($\tau = RC$) and filter cutoff frequencies.</p>
        </a>
        <a href="wire-gauge-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Wire Gauge Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Calculate conductor resistance, circular mils, and voltage drop across AWG wires.</p>
        </a>
      </div>
    </article>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-col">
        <h3>CalcHub</h3>
        <p>Your comprehensive engineering, mathematical, physical, and financial computational authority.</p>
      </div>
      <div class="footer-col">
        <h3>Calculators</h3>
        <ul>
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="math.html">Mathematics</a></li>
          <li><a href="converter.html">Unit Converters</a></li>
          <li><a href="engineering.html">Electrical &amp; Engineering</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h3>Electronics &amp; Circuits</h3>
        <ul>
          <li><a href="parallel-resistance-calculator.html">Parallel Resistance</a></li>
          <li><a href="voltage-divider-calculator.html">Voltage Divider</a></li>
          <li><a href="ohms-law-calculator.html">Ohm's Law</a></li>
          <li><a href="rc-time-constant-calculator.html">RC Time Constant</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 CalcHub. High-precision engineering formulas and calculators. All rights reserved.</p>
    </div>
  </footer>

  <script>
    (function() {
      // DOM Elements
      const presetSelect = document.getElementById('pr-preset');
      const vsupplyInput = document.getElementById('pr-vsupply');
      const container = document.getElementById('pr-resistors-container');
      const addRowBtn = document.getElementById('pr-add-row-btn');
      const calcBtn = document.getElementById('pr-calc-btn');
      const resetBtn = document.getElementById('pr-reset-btn');

      // Outputs
      const primaryOut = document.getElementById('pr-primary-out');
      const statusOut = document.getElementById('pr-status-out');
      const currentOut = document.getElementById('pr-current-out');
      const powerOut = document.getElementById('pr-power-out');
      const condOut = document.getElementById('pr-cond-out');
      const branchesOut = document.getElementById('pr-branches-out');
      const breakdownBody = document.getElementById('pr-breakdown-body');

      const PRESETS = {
        'two-equal': [ { val: 10, unit: 1000 }, { val: 10, unit: 1000 } ],
        'three-equal': [ { val: 100, unit: 1 }, { val: 100, unit: 1 }, { val: 100, unit: 1 } ],
        'standard-trim': [ { val: 10, unit: 1000 }, { val: 1, unit: 1000000 } ],
        'current-shunt': [ { val: 0.1, unit: 1 }, { val: 0.1, unit: 1 } ],
        'asymmetric': [ { val: 1, unit: 1000 }, { val: 2.2, unit: 1000 }, { val: 4.7, unit: 1000 } ]
      };

      function createRow(val = 10, unit = 1000, index = 1) {
        const row = document.createElement('div');
        row.className = 'form-row pr-branch-row';
        row.style.marginBottom = '0.5rem';
        row.style.alignItems = 'flex-end';

        row.innerHTML = `
          <div class="form-group" style="flex: 1;">
            <label style="font-size: 0.75rem;">Branch R${index}</label>
            <input type="number" class="form-control pr-val-input" value="${val}" step="any" min="0.0001">
          </div>
          <div class="form-group" style="flex: 0.7; max-width: 100px;">
            <label style="font-size: 0.75rem;">Unit</label>
            <select class="form-control pr-unit-select">
              <option value="1" ${unit === 1 ? 'selected' : ''}>&Omega;</option>
              <option value="1000" ${unit === 1000 ? 'selected' : ''}>k&Omega;</option>
              <option value="1000000" ${unit === 1000000 ? 'selected' : ''}>M&Omega;</option>
            </select>
          </div>
          <button type="button" class="btn btn-secondary pr-remove-btn" style="padding: 0.5rem 0.75rem; margin-bottom: 1rem; color: #dc2626;">&times;</button>
        `;

        const valInp = row.querySelector('.pr-val-input');
        const unitSel = row.querySelector('.pr-unit-select');
        const removeBtn = row.querySelector('.pr-remove-btn');

        valInp.addEventListener('input', function() {
          presetSelect.value = 'custom';
          calculate();
        });
        unitSel.addEventListener('change', function() {
          presetSelect.value = 'custom';
          calculate();
        });

        removeBtn.addEventListener('click', function() {
          if (container.querySelectorAll('.pr-branch-row').length > 2) {
            row.remove();
            renumberRows();
            presetSelect.value = 'custom';
            calculate();
          }
        });

        return row;
      }

      function renumberRows() {
        const rows = container.querySelectorAll('.pr-branch-row');
        rows.forEach((r, idx) => {
          const lbl = r.querySelector('label');
          if (lbl) lbl.textContent = `Branch R${idx + 1}`;
        });
      }

      function loadPreset(key) {
        container.innerHTML = '';
        const list = PRESETS[key] || PRESETS['two-equal'];
        list.forEach((item, idx) => {
          container.appendChild(createRow(item.val, item.unit, idx + 1));
        });
        calculate();
      }

      function formatOhms(r) {
        if (r >= 1e6) return (r / 1e6).toFixed(3) + " M\u03a9";
        if (r >= 1e3) return (r / 1e3).toFixed(3) + " k\u03a9";
        return r.toFixed(3) + " \u03a9";
      }

      function formatConductance(g) {
        if (g >= 1.0) return g.toFixed(4) + " S";
        if (g >= 0.001) return (g * 1000).toFixed(3) + " mS";
        return (g * 1e6).toFixed(2) + " \u03bcS";
      }

      function formatCurrent(i) {
        if (i >= 1.0) return i.toFixed(3) + " A";
        if (i >= 0.001) return (i * 1000).toFixed(3) + " mA";
        return (i * 1e6).toFixed(2) + " \u03bcA";
      }

      function formatPower(p) {
        if (p >= 1000) return (p / 1000).toFixed(3) + " kW";
        if (p >= 1.0) return p.toFixed(3) + " W";
        if (p >= 0.001) return (p * 1000).toFixed(2) + " mW";
        return (p * 1e6).toFixed(2) + " \u03bcW";
      }

      function calculate() {
        const rows = container.querySelectorAll('.pr-branch-row');
        const vSupply = parseFloat(vsupplyInput.value) || 0;
        let sumConductance = 0;
        const branchData = [];

        rows.forEach((r, idx) => {
          const raw = parseFloat(r.querySelector('.pr-val-input').value) || 0;
          const mult = parseFloat(r.querySelector('.pr-unit-select').value) || 1;
          const rOhms = raw * mult;

          if (rOhms > 0) {
            const cond = 1 / rOhms;
            sumConductance += cond;
            branchData.push({
              index: idx + 1,
              rOhms: rOhms,
              conductance: cond
            });
          }
        });

        if (sumConductance <= 0) {
          primaryOut.textContent = "-- \u03a9";
          statusOut.textContent = "Please enter valid positive branch resistances.";
          breakdownBody.innerHTML = '';
          return;
        }

        const req = 1 / sumConductance;
        const totalCurrent = vSupply * sumConductance;
        const totalPower = vSupply * totalCurrent;

        // Render Cards
        primaryOut.textContent = formatOhms(req);
        statusOut.textContent = `Total Conductance: ${formatConductance(sumConductance)} \u2022 Network: ${branchData.length} Branches`;
        currentOut.textContent = vSupply > 0 ? formatCurrent(totalCurrent) : "--";
        powerOut.textContent = vSupply > 0 ? formatPower(totalPower) : "--";
        condOut.textContent = formatConductance(sumConductance);
        branchesOut.textContent = `${branchData.length} Resistors`;

        // Render Table
        breakdownBody.innerHTML = '';
        branchData.forEach(b => {
          const bCurrent = vSupply * b.conductance;
          const bPower = vSupply * bCurrent;
          const tr = document.createElement('tr');
          tr.innerHTML = `
            <td><strong>Branch ${b.index}</strong></td>
            <td>${formatOhms(b.rOhms)}</td>
            <td>${formatConductance(b.conductance)}</td>
            <td><strong style="color: var(--primary, #2563eb);">${vSupply > 0 ? formatCurrent(bCurrent) : '--'}</strong></td>
            <td>${vSupply > 0 ? formatPower(bPower) : '--'}</td>
          `;
          breakdownBody.appendChild(tr);
        });
      }

      presetSelect.addEventListener('change', function() {
        if (this.value !== 'custom') {
          loadPreset(this.value);
        }
      });

      addRowBtn.addEventListener('click', function() {
        const count = container.querySelectorAll('.pr-branch-row').length + 1;
        container.appendChild(createRow(10, 1000, count));
        presetSelect.value = 'custom';
        calculate();
      });

      vsupplyInput.addEventListener('input', calculate);

      calcBtn.addEventListener('click', calculate);

      resetBtn.addEventListener('click', function() {
        presetSelect.value = 'two-equal';
        vsupplyInput.value = '12.0';
        loadPreset('two-equal');
      });

      // Initial execution
      loadPreset('two-equal');
    })();
  </script>
</body>
</html>
"""

def generate_files():
    p1 = os.path.join(BASE_DIR, "voltage-divider-calculator.html")
    with open(p1, "w", encoding="utf-8") as f:
        f.write(HTML_VOLTAGE_DIVIDER.strip() + "\n")
    print(f"Generated: {p1}")

    p2 = os.path.join(BASE_DIR, "parallel-resistance-calculator.html")
    with open(p2, "w", encoding="utf-8") as f:
        f.write(HTML_PARALLEL_RESISTANCE.strip() + "\n")
    print(f"Generated: {p2}")

if __name__ == "__main__":
    generate_files()
