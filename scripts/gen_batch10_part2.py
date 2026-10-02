# -*- coding: utf-8 -*-
"""
Script to generate Batch 10 Part 2 tools:
3. hydraulic-cylinder-speed-calculator.html
4. hydraulic-pump-power-calculator.html
"""
import os

TOOL_3_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hydraulic Cylinder Speed Calculator | Piston Velocity & Flow Rate</title>
  <meta name="description" content="Calculate hydraulic cylinder extension and retraction velocity, required pump flow rate (LPM & GPM), stroke cycle duration, and regenerative speed boost per ISO 6020.">
  <link rel="canonical" href="https://calchub.cloud/hydraulic-cylinder-speed-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "Hydraulic Cylinder Speed Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Fluid power kinematic sizing engine computing cylinder linear speed v = Q / A, stroke extension/retraction time, fluid port velocity, and regenerative circuit boost per ISO 6020.",
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
            "name": "What is the formula for hydraulic cylinder linear velocity?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Linear piston speed is calculated as: v = Q / A, where Q is volumetric flow rate entering the cylinder and A is the active piston cross-sectional area. In metric units: v [m/s] = (Q [L/min] * 1000) / (A [mm^2] * 60). In imperial units: v [in/s] = (231 * Q [GPM]) / (A [sq in] * 60) approx (3.85 * Q) / A."
            }
          },
          {
            "@type": "Question",
            "name": "Why does a cylinder retract faster than it extends?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In a single-rod cylinder, the steel rod occupies space inside the rod-end cap. When oil is pumped into the rod end during retraction, it only fills the annular area: A_annulus = A_bore - A_rod. Because this area is significantly smaller than the full bore area, the same pump flow rate fills the chamber faster, driving higher retraction speed."
            }
          },
          {
            "@type": "Question",
            "name": "How does a regenerative hydraulic circuit increase extension speed?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A regenerative circuit routes oil exhausted from the rod end directly into the cap end during extension, combining with the pump flow. Because fluid acts on both sides, the effective advance area equals only the rod area: v_regen = Q_pump / A_rod. This increases extension velocity by 30% to 100%, though it reduces output force to: F_regen = P * A_rod."
            }
          },
          {
            "@type": "Question",
            "name": "What are maximum safe fluid flow velocities through hydraulic ports and hoses?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "To prevent extreme pressure drops, oil overheating, and fluid cavitation: Pump suction lines are limited to 0.8 - 1.5 m/s (2 - 5 ft/s); return lines to tank are limited to 2.0 - 4.0 m/s (6 - 13 ft/s); high-pressure delivery lines are limited to 3.0 - 6.0 m/s (10 - 20 ft/s); short cylinder port passages are typically restricted below 7.5 m/s (25 ft/s)."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="mechanical">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">
        <span class="logo-icon">&pi;</span>
        <span class="logo-text">Calc<strong>Hub</strong></span>
      </a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="engineering.html">Engineering</a>
        <a href="mechanical.html" class="active">Mechanical</a>
        <a href="solar-energy.html">Solar</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo;
      <a href="mechanical.html">Mechanical &amp; Machine Design</a> &rsaquo;
      <span>Hydraulic Cylinder Speed Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">ISO 6020 &amp; NFPA Cylinder Kinematics</div>
          <h1 class="calc-title">Hydraulic Cylinder Speed Calculator</h1>
          <p class="calc-tagline">Calculate cylinder piston extension and retraction velocities, required pump flow rate, stroke travel times, port velocities, and regenerative circuit speed boost.</p>
        </header>

        <div class="tool-card">
          <form id="cylSpeedCalcForm">
            <div class="calc-grid">
              <div class="form-group">
                <label for="speedCalcObjective">Calculation Objective</label>
                <select id="speedCalcObjective">
                  <option value="findSpeed" selected>Calculate Piston Speed from Known Pump Flow</option>
                  <option value="findFlow">Calculate Required Pump Flow from Target Speed</option>
                </select>
              </div>

              <div class="form-group">
                <label for="speedUnits">Engineering Units</label>
                <select id="speedUnits">
                  <option value="metric" selected>Metric (mm, m/s, L/min, mm/s)</option>
                  <option value="imperial">Imperial (in, in/s, GPM, ft/min)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="boreD" id="lblBoreD">Cylinder Bore Diameter (D) [mm]</label>
                <input type="number" id="boreD" step="1" min="10" max="1500" value="80">
              </div>

              <div class="form-group">
                <label for="rodD" id="lblRodD">Piston Rod Diameter (d) [mm]</label>
                <input type="number" id="rodD" step="1" min="5" max="1400" value="45">
              </div>

              <div class="form-group">
                <label for="strokeLen" id="lblStrokeLen">Stroke Length (S) [mm]</label>
                <input type="number" id="strokeLen" step="10" min="10" max="10000" value="600">
              </div>

              <div class="form-group" id="grpInputFlow">
                <label for="inputFlowRate" id="lblInputFlow">Pump Delivery Flow Rate (Q) [L/min]</label>
                <input type="number" id="inputFlowRate" step="1" min="0.1" max="2500" value="35">
              </div>

              <div class="form-group" id="grpTargetSpeed" style="display: none;">
                <label for="targetPistonSpeed" id="lblTargetSpeed">Target Extension Speed [m/s]</label>
                <input type="number" id="targetPistonSpeed" step="0.01" min="0.005" max="5.0" value="0.15">
              </div>

              <div class="form-group">
                <label for="portDiam" id="lblPortDiam">Cylinder Port Inside Diameter [mm]</label>
                <input type="number" id="portDiam" step="0.5" min="2" max="150" value="12.0">
              </div>

              <div class="form-group">
                <label for="circuitMode">Hydraulic Circuit Configuration</label>
                <select id="circuitMode">
                  <option value="standard" selected>Standard 4/3 Valve (Non-Regenerative)</option>
                  <option value="regen">Regenerative Circuit (High-Speed Extend)</option>
                </select>
              </div>
            </div>

            <div class="calc-actions">
              <button type="button" id="calcSpeedBtn" class="btn btn-primary">Calculate Actuation Speed</button>
              <button type="reset" id="resetSpeedBtn" class="btn btn-secondary">Reset Defaults</button>
            </div>
          </form>

          <div id="cylSpeedResultBox" class="results-container" style="display: none;">
            <h3>Cylinder Kinematic & Flow Velocity Results</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label" id="resPrimaryExtSpeedLabel">Extension Speed (v_ext)</span>
                <span id="resExtSpeed" class="result-value">-- m/s</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Retraction Speed (v_ret)</span>
                <span id="resRetSpeed" class="result-value">-- m/s</span>
              </div>
              <div class="result-tile">
                <span class="result-label" id="resPrimaryFlowLabel">Active Pump Flow Rate</span>
                <span id="resPumpFlow" class="result-value">-- L/min</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Extension Travel Time (t_ext)</span>
                <span id="resExtTime" class="result-value">-- s</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Retraction Travel Time (t_ret)</span>
                <span id="resRetTime" class="result-value">-- s</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Full Stroke Cycle Duration</span>
                <span id="resCycleTime" class="result-value">-- s</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Fluid Port Flow Velocity (v_port)</span>
                <span id="resPortVelocity" class="result-value">-- m/s</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Speed Ratio (Retract / Extend)</span>
                <span id="resSpeedRatio" class="result-value">--</span>
              </div>
            </div>
            <div id="cylSpeedNotesBox" style="margin-top: 1rem; color: #1e40af; background: #eff6ff; border: 1px solid #bfdbfe; padding: 0.75rem; border-radius: 6px;"></div>
          </div>
        </div>

        <article class="article-body">
          <h2>Kinematic Principles of Hydraulic Actuator Velocity</h2>
          <p>The operating velocity of a hydraulic cylinder is governed entirely by fluid kinematics: the volumetric rate at which incompressible hydraulic fluid is pumped into the cylinder barrel divided by the internal cross-sectional area displacing that fluid. While hydraulic system pressure dictates available force, <strong>pump flow rate dictates piston velocity</strong>.</p>

          <p>Proper speed regulation is crucial in industrial automated assembly, plastics molding, metal shearing, and aerospace flight control actuators. If a cylinder moves too rapidly without deceleration cushioning, the kinetic energy of the moving mass (\(E_k = \frac{1}{2} m v^2\)) slams the piston head into the steel cylinder cap, generating destructive hydraulic shockwaves (water hammer) and cracking tie-rods. Conversely, if a cylinder operates too slowly, machine cycle times stretch, severely cutting factory throughput.</p>

          <h2>Mathematical Velocity Formulations: Extension vs. Retraction</h2>
          <p>In standard double-acting hydraulic cylinders, linear speed depends on whether the piston is extending or retracting:</p>

          <h3>1. Extension (Forward Stroke) Velocity</h3>
          <p>During extension, fluid enters the cap end to fill the full bore diameter (\(D_{\text{bore}}\)):</p>

          <div class="formula-box">
            $$v_{\text{ext}} = \frac{Q}{A_{\text{bore}}} = \frac{Q}{\frac{\pi}{4} D_{\text{bore}}^2}$$
          </div>

          <h3>2. Retraction (Return Stroke) Velocity</h3>
          <p>During retraction, fluid enters the rod-end port to fill only the annular area (\(A_{\text{annulus}}\)):</p>

          <div class="formula-box">
            $$v_{\text{ret}} = \frac{Q}{A_{\text{annulus}}} = \frac{Q}{\frac{\pi}{4} (D_{\text{bore}}^2 - d_{\text{rod}}^2)}$$
          </div>

          <p>Because \(A_{\text{annulus}} < A_{\text{bore}}\), <strong>retraction speed is always higher than extension speed</strong> when driven by a fixed-displacement pump. The kinematic speed ratio is the inverse of the area ratio:</p>

          <div class="formula-box">
            $$\text{Speed Ratio} = \frac{v_{\text{ret}}}{v_{\text{ext}}} = \frac{A_{\text{bore}}}{A_{\text{annulus}}} = \frac{D_{\text{bore}}^2}{D_{\text{bore}}^2 - d_{\text{rod}}^2} = \frac{1}{1 - (d_{\text{rod}} / D_{\text{bore}})^2}$$
          </div>

          <h2>Regenerative High-Speed Circuit Mechanics</h2>
          <p>In applications such as wood splitters, garbage truck compactors, and injection molding clamping units, the machine requires rapid advance during the unloaded approach stroke followed by high force during final contact. A <strong>regenerative circuit</strong> redirects oil exhausting from the rod end directly into the cap end, combining it with pump flow.</p>

          <p>Because pressurized oil acts simultaneously on both sides of the piston, the effective forward advance area reduces to <em>only the rod cross-sectional area</em> (\(A_{\text{rod}}\)):</p>

          <div class="formula-box">
            $$v_{\text{regen}} = \frac{Q_{\text{pump}}}{A_{\text{rod}}} = \frac{Q_{\text{pump}}}{\frac{\pi}{4} d_{\text{rod}}^2}$$
          </div>

          <p>For a standard cylinder where \(d_{\text{rod}} \approx 0.707 \cdot D_{\text{bore}}\), the rod area equals half the bore area, exactly <strong>doubling extension velocity (100% speed increase)</strong> without requiring a larger, expensive hydraulic pump.</p>

          <h2>Fluid Flow Velocity in Cylinder Ports & Hoses</h2>
          <p>When high pump flows traverse narrow cylinder port fittings, fluid velocities can reach turbulent extremes. The fluid linear speed (\(v_{\text{port}}\)) traversing a port of inside diameter \(d_{\text{port}}\) is:</p>

          <div class="formula-box">
            $$v_{\text{port}} = \frac{Q}{\frac{\pi}{4} d_{\text{port}}^2}$$
          </div>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Hydraulic Line Type</th>
                <th>Recommended Max Fluid Speed (m/s)</th>
                <th>Imperial Velocity Limit (ft/s)</th>
                <th>Consequence of Exceeding Velocity Limits</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Pump Suction Lines</td>
                <td>0.8 &ndash; 1.5 m/s</td>
                <td>2.5 &ndash; 5.0 ft/s</td>
                <td>Vapor cavitation, pump impeller erosion, extreme whine.</td>
              </tr>
              <tr>
                <td>Return Lines to Tank</td>
                <td>2.0 &ndash; 3.5 m/s</td>
                <td>6.5 &ndash; 11.5 ft/s</td>
                <td>High backpressure, reservoir aeration, filter bypass.</td>
              </tr>
              <tr>
                <td>Medium Pressure Lines (&le; 160 bar)</td>
                <td>3.0 &ndash; 5.0 m/s</td>
                <td>10.0 &ndash; 16.5 ft/s</td>
                <td>Elevated line friction, oil overheating.</td>
              </tr>
              <tr>
                <td>High Pressure Lines (> 250 bar)</td>
                <td>4.5 &ndash; 6.5 m/s</td>
                <td>15.0 &ndash; 21.0 ft/s</td>
                <td>Extreme laminar-to-turbulent friction losses.</td>
              </tr>
              <tr>
                <td>Short Internal Cylinder Ports</td>
                <td>6.0 &ndash; 8.0 m/s</td>
                <td>20.0 &ndash; 26.0 ft/s</td>
                <td>Localized pressure drop, seal thermal degradation.</td>
              </tr>
            </tbody>
          </table>

          <div class="worked-example-card">
            <h3>Step-by-Step Worked Case Study: Automated CNC Loading Cylinder</h3>
            <p><strong>Design Scenario:</strong> An automation engineer is sizing the actuator kinematics for a robotic gantry loader servicing a CNC turning center:</p>
            <ul>
              <li>Piston bore: \(D_{\text{bore}} = 80\text{ mm}\) (\(0.080\text{ m}\)).</li>
              <li>Piston rod: \(d_{\text{rod}} = 45\text{ mm}\) (\(0.045\text{ m}\)).</li>
              <li>Stroke length: \(S = 600\text{ mm}\) (\(0.600\text{ m}\)).</li>
              <li>Pump delivery flow: \(Q = 35\text{ L/min}\) (\(0.000583\text{ m}^3/\text{s}\)).</li>
              <li>Cylinder port internal diameter: \(d_{\text{port}} = 12.0\text{ mm}\).</li>
            </ul>

            <p><strong>Step 1: Compute bore and annular effective areas</strong></p>
            <div class="formula-box">
              $$A_{\text{bore}} = \frac{\pi}{4} (80)^2 = 5,026.55\text{ mm}^2 = 5.0265 \times 10^{-3}\text{ m}^2$$
              $$A_{\text{rod}} = \frac{\pi}{4} (45)^2 = 1,590.43\text{ mm}^2$$
              $$A_{\text{annulus}} = 5,026.55 - 1,590.43 = 3,436.12\text{ mm}^2 = 3.4361 \times 10^{-3}\text{ m}^2$$
            </div>

            <p><strong>Step 2: Calculate extension and retraction speeds</strong></p>
            <div class="formula-box">
              $$v_{\text{ext}} = \frac{0.0005833\text{ m}^3/\text{s}}{0.0050265\text{ m}^2} = 0.1161\text{ m/s} = 116.1\text{ mm/s} \quad (4.57\text{ in/s})$$
              $$v_{\text{ret}} = \frac{0.0005833\text{ m}^3/\text{s}}{0.0034361\text{ m}^2} = 0.1698\text{ m/s} = 169.8\text{ mm/s} \quad (6.68\text{ in/s})$$
            </div>

            <p><strong>Step 3: Determine travel times and total cycle duration</strong></p>
            <div class="formula-box">
              $$t_{\text{ext}} = \frac{0.600\text{ m}}{0.1161\text{ m/s}} = 5.17\text{ seconds}$$
              $$t_{\text{ret}} = \frac{0.600\text{ m}}{0.1698\text{ m/s}} = 3.53\text{ seconds}$$
              $$t_{\text{cycle}} = 5.17 + 3.53 = 8.70\text{ seconds}$$
            </div>

            <p><strong>Step 4: Check fluid velocity in 12 mm cylinder ports</strong></p>
            <div class="formula-box">
              $$A_{\text{port}} = \frac{\pi}{4} (12)^2 = 113.1\text{ mm}^2 = 1.131 \times 10^{-4}\text{ m}^2$$
              $$v_{\text{port}} = \frac{0.0005833\text{ m}^3/\text{s}}{0.0001131\text{ m}^2} = 5.16\text{ m/s} \quad (16.9\text{ ft/s})$$
            </div>
            <p><strong>Engineering Conclusion:</strong> The port velocity of 5.16 m/s is within the safe 6.0 m/s limit for cylinder ports, and the complete stroke cycle of 8.7 seconds easily satisfies the required 10-second gantry load cycle.</p>
          </div>

          <h2>Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3>How do flow control valves (meter-in vs. meter-out) affect cylinder speed stability?</h3>
            <p>Meter-in flow control restricts fluid entering the cylinder, making it suitable only for resistive loads. If the load is overrunning (pulling in the direction of motion, such as a descending hoist), meter-in allows the cylinder to runaway out of control. <strong>Meter-out control</strong> restricts fluid leaving the opposing chamber, creating a stabilizing hydraulic backpressure cushion that positively controls cylinder speed regardless of load direction.</p>
          </div>

          <div class="faq-item">
            <h3>Why does cylinder speed fluctuate when using a fixed displacement pump?</h3>
            <p>Speed fluctuations typically stem from pressure-dependent fluid leakage past internal pump gear teeth or piston clearances (decreasing pump volumetric efficiency as system pressure climbs), or thermal oil thinning. Installing a <strong>pressure-compensated proportional flow control valve</strong> maintains a strictly constant flow rate to the cylinder regardless of fluctuating working pressures.</p>
          </div>

          <div class="faq-item">
            <h3>What is the maximum recommended speed for industrial hydraulic cylinders?</h3>
            <p>Standard industrial cylinders equipped with nitrile/polyurethane lip seals operate optimally between <strong>0.05 m/s and 0.50 m/s (2 to 20 in/s)</strong>. Speeds below 0.03 m/s induce "stick-slip" chatter due to static seal friction breakout. Speeds above 0.80 m/s require specialized low-friction PTFE bronze step seals, high-temperature Viton compounds, and external proportional electronic deceleration profiling to prevent seal burning.</p>
          </div>

          <div class="faq-item">
            <h3>How do telescopic cylinders maintain speed across stages?</h3>
            <p>In standard multi-stage telescopic cylinders, each successive sleeve has a smaller effective bore area. Driven by a constant pump flow rate, each smaller stage extends significantly faster than the previous stage (\(v \propto 1 / A\)). To achieve uniform linear speed across all stages, variable displacement pumps or proportional flow controllers must progressively throttle oil flow as each stage deploys.</p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar" id="toolSidebar">
        <!-- Dynamically rendered sidebar -->
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; 2026 CalcHub. All rights reserved. Engineering and mathematical tools grounded in international standards.</p>
      <ul class="footer-links">
        <li><a href="index.html">Home</a></li>
        <li><a href="mechanical.html">Mechanical</a></li>
        <li><a href="ohms-law-calculator.html">Ohm's Law</a></li>
        <li><a href="sitemap.xml">Sitemap</a></li>
      </ul>
    </div>
  </footer>

  <script>
    const speedCalcObjectiveSelect = document.getElementById('speedCalcObjective');
    const speedUnitsSelect = document.getElementById('speedUnits');
    const boreDInput = document.getElementById('boreD');
    const rodDInput = document.getElementById('rodD');
    const strokeLenInput = document.getElementById('strokeLen');
    const inputFlowRateInput = document.getElementById('inputFlowRate');
    const targetPistonSpeedInput = document.getElementById('targetPistonSpeed');
    const portDiamInput = document.getElementById('portDiam');
    const circuitModeSelect = document.getElementById('circuitMode');

    const lblBoreD = document.getElementById('lblBoreD');
    const lblRodD = document.getElementById('lblRodD');
    const lblStrokeLen = document.getElementById('lblStrokeLen');
    const lblInputFlow = document.getElementById('lblInputFlow');
    const lblTargetSpeed = document.getElementById('lblTargetSpeed');
    const lblPortDiam = document.getElementById('lblPortDiam');
    const grpInputFlow = document.getElementById('grpInputFlow');
    const grpTargetSpeed = document.getElementById('grpTargetSpeed');

    const cylSpeedResultBox = document.getElementById('cylSpeedResultBox');
    const resPrimaryExtSpeedLabel = document.getElementById('resPrimaryExtSpeedLabel');
    const resExtSpeed = document.getElementById('resExtSpeed');
    const resRetSpeed = document.getElementById('resRetSpeed');
    const resPrimaryFlowLabel = document.getElementById('resPrimaryFlowLabel');
    const resPumpFlow = document.getElementById('resPumpFlow');
    const resExtTime = document.getElementById('resExtTime');
    const resRetTime = document.getElementById('resRetTime');
    const resCycleTime = document.getElementById('resCycleTime');
    const resPortVelocity = document.getElementById('resPortVelocity');
    const resSpeedRatio = document.getElementById('resSpeedRatio');
    const cylSpeedNotesBox = document.getElementById('cylSpeedNotesBox');

    speedCalcObjectiveSelect.addEventListener('change', function() {
      if (this.value === 'findSpeed') {
        grpInputFlow.style.display = 'block';
        grpTargetSpeed.style.display = 'none';
        resPrimaryExtSpeedLabel.textContent = "Extension Speed (v_ext)";
        resPrimaryFlowLabel.textContent = "Active Pump Flow Rate";
      } else {
        grpInputFlow.style.display = 'none';
        grpTargetSpeed.style.display = 'block';
        resPrimaryExtSpeedLabel.textContent = "Specified Target Speed";
        resPrimaryFlowLabel.textContent = "Required Pump Flow Rate";
      }
      calculateCylSpeed();
    });

    speedUnitsSelect.addEventListener('change', function() {
      const isMetric = this.value === 'metric';
      if (isMetric) {
        lblBoreD.textContent = "Cylinder Bore Diameter (D) [mm]";
        lblRodD.textContent = "Piston Rod Diameter (d) [mm]";
        lblStrokeLen.textContent = "Stroke Length (S) [mm]";
        lblInputFlow.textContent = "Pump Delivery Flow Rate (Q) [L/min]";
        lblTargetSpeed.textContent = "Target Extension Speed [m/s]";
        lblPortDiam.textContent = "Cylinder Port Inside Diameter [mm]";
        boreDInput.value = 80;
        rodDInput.value = 45;
        strokeLenInput.value = 600;
        inputFlowRateInput.value = 35;
        targetPistonSpeedInput.value = 0.15;
        portDiamInput.value = 12.0;
      } else {
        lblBoreD.textContent = "Cylinder Bore Diameter (D) [in]";
        lblRodD.textContent = "Piston Rod Diameter (d) [in]";
        lblStrokeLen.textContent = "Stroke Length (S) [in]";
        lblInputFlow.textContent = "Pump Delivery Flow Rate (Q) [GPM]";
        lblTargetSpeed.textContent = "Target Extension Speed [in/s]";
        lblPortDiam.textContent = "Cylinder Port Inside Diameter [in]";
        boreDInput.value = 3.25;
        rodDInput.value = 1.75;
        strokeLenInput.value = 24.0;
        inputFlowRateInput.value = 9.0;
        targetPistonSpeedInput.value = 6.0;
        portDiamInput.value = 0.50;
      }
      calculateCylSpeed();
    });

    function calculateCylSpeed() {
      const isMetric = speedUnitsSelect.value === 'metric';
      const isFindSpeed = (speedCalcObjectiveSelect.value === 'findSpeed');
      const isRegen = (circuitModeSelect.value === 'regen');

      let D = parseFloat(boreDInput.value);
      let d = parseFloat(rodDInput.value);
      let S = parseFloat(strokeLenInput.value);
      let d_port = parseFloat(portDiamInput.value);

      if (isNaN(D) || D <= 0) D = isMetric ? 80 : 3.25;
      if (isNaN(d) || d <= 0) d = isMetric ? 45 : 1.75;
      if (d >= D) d = D * 0.55;
      if (isNaN(S) || S <= 0) S = isMetric ? 600 : 24;
      if (isNaN(d_port) || d_port <= 0) d_port = isMetric ? 12 : 0.5;

      let A_bore = 0;
      let A_rod = 0;
      let A_ann = 0;
      let A_port = 0;

      let v_ext_disp = 0;
      let v_ret_disp = 0;
      let Q_disp = 0;
      let v_port_disp = 0;

      let t_ext = 0;
      let t_ret = 0;

      if (isMetric) {
        A_bore = (Math.PI / 4) * Math.pow(D, 2); // mm^2
        A_rod = (Math.PI / 4) * Math.pow(d, 2);
        A_ann = A_bore - A_rod;
        A_port = (Math.PI / 4) * Math.pow(d_port, 2);

        const A_ext_active = isRegen ? A_rod : A_bore;

        let Q_Lpm = 0;
        let v_ext_mps = 0;

        if (isFindSpeed) {
          Q_Lpm = parseFloat(inputFlowRateInput.value);
          if (isNaN(Q_Lpm) || Q_Lpm <= 0) Q_Lpm = 35;
          // v [m/s] = (Q [L/min] * 10^3) / (A [mm^2] * 60)
          v_ext_mps = (Q_Lpm * 1000) / (A_ext_active * 60);
          Q_disp = Q_Lpm;
        } else {
          v_ext_mps = parseFloat(targetPistonSpeedInput.value);
          if (isNaN(v_ext_mps) || v_ext_mps <= 0) v_ext_mps = 0.15;
          // Q [L/min] = (v [m/s] * A [mm^2] * 60) / 1000
          Q_Lpm = (v_ext_mps * A_ext_active * 60) / 1000;
          Q_disp = Q_Lpm;
        }

        const v_ret_mps = (Q_Lpm * 1000) / (A_ann * 60);
        v_ext_disp = v_ext_mps;
        v_ret_disp = v_ret_mps;

        t_ext = S / (v_ext_mps * 1000);
        t_ret = S / (v_ret_mps * 1000);

        // Fluid port speed (m/s)
        const v_port_mps = (Q_Lpm * 1000) / (A_port * 60);
        v_port_disp = v_port_mps;

        resExtSpeed.textContent = (v_ext_disp * 1000).toFixed(0) + " mm/s (" + v_ext_disp.toFixed(3) + " m/s)";
        resRetSpeed.textContent = (v_ret_disp * 1000).toFixed(0) + " mm/s (" + v_ret_disp.toFixed(3) + " m/s)";
        resPumpFlow.textContent = Q_disp.toFixed(1) + " L/min";
        resPortVelocity.textContent = v_port_disp.toFixed(2) + " m/s";
      } else {
        A_bore = (Math.PI / 4) * Math.pow(D, 2); // in^2
        A_rod = (Math.PI / 4) * Math.pow(d, 2);
        A_ann = A_bore - A_rod;
        A_port = (Math.PI / 4) * Math.pow(d_port, 2);

        const A_ext_active = isRegen ? A_rod : A_bore;

        let Q_gpm = 0;
        let v_ext_ips = 0;

        if (isFindSpeed) {
          Q_gpm = parseFloat(inputFlowRateInput.value);
          if (isNaN(Q_gpm) || Q_gpm <= 0) Q_gpm = 9.0;
          v_ext_ips = (231 * Q_gpm) / (A_ext_active * 60);
          Q_disp = Q_gpm;
        } else {
          v_ext_ips = parseFloat(targetPistonSpeedInput.value);
          if (isNaN(v_ext_ips) || v_ext_ips <= 0) v_ext_ips = 6.0;
          Q_gpm = (v_ext_ips * A_ext_active * 60) / 231;
          Q_disp = Q_gpm;
        }

        const v_ret_ips = (231 * Q_gpm) / (A_ann * 60);
        v_ext_disp = v_ext_ips;
        v_ret_disp = v_ret_ips;

        t_ext = S / v_ext_ips;
        t_ret = S / v_ret_ips;

        // Port velocity ft/s
        const v_port_fps = (Q_gpm * 0.3208) / A_port;
        v_port_disp = v_port_fps;

        resExtSpeed.textContent = v_ext_disp.toFixed(2) + " in/s (" + (v_ext_disp * 5).toFixed(0) + " ft/min)";
        resRetSpeed.textContent = v_ret_disp.toFixed(2) + " in/s (" + (v_ret_disp * 5).toFixed(0) + " ft/min)";
        resPumpFlow.textContent = Q_disp.toFixed(1) + " GPM";
        resPortVelocity.textContent = v_port_disp.toFixed(1) + " ft/s";
      }

      const speedRatio = v_ret_disp / v_ext_disp;
      resSpeedRatio.textContent = speedRatio.toFixed(2) + "× (Retract is " + ((speedRatio - 1) * 100).toFixed(0) + "% faster)";
      resExtTime.textContent = t_ext.toFixed(2) + " s";
      resRetTime.textContent = t_ret.toFixed(2) + " s";
      resCycleTime.textContent = (t_ext + t_ret).toFixed(2) + " s (Complete Cycle)";

      let notes = `<strong>Kinematic Assessment:</strong> At <strong>${Q_disp.toFixed(1)} ${isMetric ? 'L/min' : 'GPM'}</strong>, extension travel requires <strong>${t_ext.toFixed(1)} s</strong> and retraction requires <strong>${t_ret.toFixed(1)} s</strong>. `;
      if (isRegen) {
        notes += `Regenerative mode is <strong>ACTIVE</strong>: advancing across rod area only to boost extension speed. `;
      }
      if ((isMetric && v_port_disp > 6.0) || (!isMetric && v_port_disp > 20.0)) {
        notes += `<span style="color:#b45309;">Warning: Port fluid velocity (${v_port_disp.toFixed(1)} ${isMetric ? 'm/s' : 'ft/s'}) exceeds the recommended threshold. Enlarge port size to avoid oil overheating.</span>`;
      }
      cylSpeedNotesBox.innerHTML = notes;

      cylSpeedResultBox.style.display = 'block';
    }

    document.getElementById('calcSpeedBtn').addEventListener('click', calculateCylSpeed);
    document.getElementById('resetSpeedBtn').addEventListener('click', function() {
      setTimeout(calculateCylSpeed, 50);
    });

    window.addEventListener('DOMContentLoaded', calculateCylSpeed);
  </script>
</body>
</html>
"""

TOOL_4_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hydraulic Pump Power Calculator | Flow, Pressure, Electric Motor kW & HP</title>
  <meta name="description" content="Calculate hydraulic pump power, electric motor size (kW & HP), drive shaft torque, pump displacement (cc/rev), and overall efficiency per ISO 4409 standards.">
  <link rel="canonical" href="https://calchub.cloud/hydraulic-pump-power-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "Hydraulic Pump Power Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Fluid power sizing calculator computing required electric motor drive power P = (p * Q) / (600 * eta), hydraulic fluid power, pump displacement, and shaft drive torque per ISO 4409.",
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
            "name": "What is the formula for hydraulic pump electric motor power?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In metric units: P_motor [kW] = (Pressure [bar] * Flow [L/min]) / (600 * eta_total), where eta_total is overall pump efficiency (typically 0.82 to 0.92). In imperial units: P_motor [HP] = (Pressure [psi] * Flow [GPM]) / (1714 * eta_total)."
            }
          },
          {
            "@type": "Question",
            "name": "How is hydraulic pump displacement (cc/rev) calculated from flow rate and RPM?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Pump geometric displacement per revolution (V_g) is: V_g [cm^3/rev] = (Flow [L/min] * 1000) / (N [RPM] * eta_volumetric). For example, a pump delivering 60 L/min at 1,500 RPM with 95% volumetric efficiency requires a displacement of 42.1 cc/rev."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between volumetric efficiency and hydromechanical efficiency?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Volumetric efficiency (eta_v) accounts for internal fluid slippage/leakage past rotating gear teeth, vanes, or piston clearances. Hydromechanical efficiency (eta_hm) accounts for mechanical friction in bearings, shaft seals, and fluid viscous shear drag. Overall efficiency is the product: eta_total = eta_v * eta_hm."
            }
          },
          {
            "@type": "Question",
            "name": "How is input drive shaft torque calculated for a hydraulic pump?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Theoretical pump drive shaft torque is: T_theo [N*m] = (V_g [cm^3/rev] * Pressure [bar]) / (20 * pi). The actual required drive torque accounting for friction is: T_actual = T_theo / eta_hm."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="mechanical">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">
        <span class="logo-icon">&pi;</span>
        <span class="logo-text">Calc<strong>Hub</strong></span>
      </a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="engineering.html">Engineering</a>
        <a href="mechanical.html" class="active">Mechanical</a>
        <a href="solar-energy.html">Solar</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo;
      <a href="mechanical.html">Mechanical &amp; Machine Design</a> &rsaquo;
      <span>Hydraulic Pump Power Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">ISO 4409 &amp; NFPA Fluid Power Standards</div>
          <h1 class="calc-title">Hydraulic Pump Power Calculator</h1>
          <p class="calc-tagline">Calculate hydraulic pump output power, required electric motor drive sizing (kW & HP), drive shaft input torque, pump displacement (cc/rev), and overall efficiency.</p>
        </header>

        <div class="tool-card">
          <form id="pumpPowerCalcForm">
            <div class="calc-grid">
              <div class="form-group">
                <label for="pumpCalcMode">Calculation Input Basis</label>
                <select id="pumpCalcMode">
                  <option value="fromFlow" selected>Specify Delivery Flow Rate (Q) & Pressure (P)</option>
                  <option value="fromDisplacement">Specify Pump Displacement (Vg) & Drive RPM (N)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="powerUnits">Engineering Units</label>
                <select id="powerUnits">
                  <option value="metric" selected>Metric (bar, L/min, kW, N·m, cc/rev)</option>
                  <option value="imperial">Imperial (psi, GPM, HP, lb·ft, cu in/rev)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="pumpType">Hydraulic Pump Type Preset</label>
                <select id="pumpType">
                  <option value="axialPiston" selected>Axial Piston Pump (High Pressure / &eta;t = 90%)</option>
                  <option value="externalGear">External Gear Pump (Standard / &eta;t = 82%)</option>
                  <option value="internalGear">Internal Gear / Gerotor Pump (&eta;t = 85%)</option>
                  <option value="vanePump">Variable Vane Pump (&eta;t = 86%)</option>
                  <option value="radialPiston">Radial Piston Pump (Ultra High Press / &eta;t = 92%)</option>
                  <option value="custom">Custom Efficiency...</option>
                </select>
              </div>

              <div class="form-group">
                <label for="pumpPressure" id="lblPumpPress">Operating Working Pressure [bar]</label>
                <input type="number" id="pumpPressure" step="5" min="5" max="1000" value="210">
              </div>

              <div class="form-group" id="grpFlowRate">
                <label for="flowRateVal" id="lblFlowRate">Delivered Flow Rate (Q) [L/min]</label>
                <input type="number" id="flowRateVal" step="1" min="0.5" max="2500" value="60">
              </div>

              <div class="form-group" id="grpDisplacement" style="display: none;">
                <label for="displacementVal" id="lblDisplacement">Pump Displacement (Vg) [cc/rev]</label>
                <input type="number" id="displacementVal" step="1" min="1" max="1000" value="45">
              </div>

              <div class="form-group">
                <label for="driveRpm">Electric Motor Drive Speed (N) [RPM]</label>
                <select id="driveRpm">
                  <option value="1450">1,450 RPM (4-Pole 50 Hz European Standard)</option>
                  <option value="1750" selected>1,750 RPM (4-Pole 60 Hz US Standard)</option>
                  <option value="960">960 RPM (6-Pole 50 Hz)</option>
                  <option value="1160">1,160 RPM (6-Pole 60 Hz)</option>
                  <option value="2900">2,900 RPM (2-Pole 50 Hz High Speed)</option>
                  <option value="3500">3,500 RPM (2-Pole 60 Hz High Speed)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="volEfficiency">Volumetric Efficiency (&eta;v)</label>
                <input type="number" id="volEfficiency" step="1" min="60" max="100" value="95">
              </div>

              <div class="form-group">
                <label for="mechEfficiency">Hydromechanical Efficiency (&eta;hm)</label>
                <input type="number" id="mechEfficiency" step="1" min="60" max="100" value="92">
              </div>
            </div>

            <div class="calc-actions">
              <button type="button" id="calcPowerBtn" class="btn btn-primary">Calculate Power & Torque</button>
              <button type="reset" id="resetPowerBtn" class="btn btn-secondary">Reset Defaults</button>
            </div>
          </form>

          <div id="pumpPowerResultBox" class="results-container" style="display: none;">
            <h3>Pump Power, Drive Motor Sizing & Torque Results</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label">Required Electric Motor Shaft Power</span>
                <span id="resMotorPower" class="result-value">-- kW</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Hydraulic Fluid Output Power (P_hyd)</span>
                <span id="resHydPower" class="result-value">-- kW</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Drive Shaft Input Torque (T_shaft)</span>
                <span id="resDriveTorque" class="result-value">-- N·m</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Calculated Pump Displacement (Vg)</span>
                <span id="resDisplacement" class="result-value">-- cc/rev</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Delivered Actual Flow Rate (Q)</span>
                <span id="resActualFlow" class="result-value">-- L/min</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Overall Total Efficiency (&eta;t)</span>
                <span id="resTotalEfficiency" class="result-value">-- %</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Parasitic Internal Heat Loss</span>
                <span id="resHeatLoss" class="result-value">-- kW</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Standard Motor Frame Recommendation</span>
                <span id="resMotorRec" class="result-value">--</span>
              </div>
            </div>
            <div id="pumpPowerNotesBox" style="margin-top: 1rem; color: #1e40af; background: #eff6ff; border: 1px solid #bfdbfe; padding: 0.75rem; border-radius: 6px;"></div>
          </div>
        </div>

        <article class="article-body">
          <h2>Applied Fluid Power & Hydraulic Prime Mover Sizing</h2>
          <p>A hydraulic pump is the heart of every fluid power system, converting mechanical rotary power from an electric motor or internal combustion engine into high-pressure fluid energy. Sizing the drive motor is one of the most critical engineering steps in power unit (HPU) design. Over-sizing the motor multiplies capital cost and causes poor electrical power factor (\(\cos\varphi < 0.70\)), while undersizing causes the motor to stall, trip thermal overloads, or burn windings when the hydraulic system reaches full relief valve pressure.</p>

          <p>Rigorous sizing per <strong>ISO 4409</strong> and <strong>NFPA Fluid Power Standards</strong> accounts for the thermodynamic transition from mechanical shaft torque to fluid hydrostatic work, including both volumetric slip leakage and mechanical bearing friction losses.</p>

          <h2>Core Mathematical Equations for Hydraulic Power</h2>
          <p>The useful fluid output power (\(P_{\text{hyd}}\)) delivered into the hydraulic circuit is the product of operating pressure and volumetric flow rate:</p>

          <h3>Metric System Formulations (bar and L/min)</h3>
          <p>Because \(1\text{ bar} = 10^5\text{ N/m}^2\) and \(1\text{ L/min} = 10^{-3} / 60\text{ m}^3/\text{s}\):</p>

          <div class="formula-box">
            $$P_{\text{hyd}} = \frac{P \cdot Q}{600} \quad [\text{kW}]$$
          </div>

          <h3>Imperial System Formulations (psi and GPM)</h3>
          <p>Because 1 horsepower equals 33,000 ft-lbf/min and 1 gallon equals 231 cubic inches:</p>

          <div class="formula-box">
            $$P_{\text{hyd}} = \frac{P \cdot Q}{1714} \quad [\text{HP}]$$
          </div>

          <h2>Required Motor Shaft Drive Power & Efficiency Derating</h2>
          <p>No hydraulic pump operates without losses. The input mechanical power (\(P_{\text{shaft}}\)) demanded from the electric motor or diesel engine must supply both fluid work and internal losses:</p>

          <div class="formula-box">
            $$P_{\text{shaft}} = \frac{P_{\text{hyd}}}{\eta_{\text{total}}} = \frac{P \cdot Q}{600 \cdot \eta_{\text{total}}} \quad [\text{kW}] \quad \Longleftrightarrow \quad P_{\text{shaft}} = \frac{P \cdot Q}{1714 \cdot \eta_{\text{total}}} \quad [\text{HP}]$$
          </div>

          <p>Overall pump efficiency (\(\eta_{\text{total}}\)) is the product of two distinct physical loss mechanisms:</p>

          <div class="formula-box">
            $$\eta_{\text{total}} = \eta_{\text{volumetric}} \cdot \eta_{\text{hydromechanical}}$$
          </div>

          <ol>
            <li><strong>Volumetric Efficiency (\(\eta_v\)):</strong> Quantifies fluid slippage escaping through micro-clearances between rotating pistons, valve plates, or gear teeth from the high-pressure discharge port back to suction or case drain (typically 0.90 to 0.98).</li>
            <li><strong>Hydromechanical Efficiency (\(\eta_{hm}\)):</strong> Quantifies mechanical friction inside shaft bearings, swashplate pivots, and oil viscous shear resistance (typically 0.85 to 0.95).</li>
          </ol>

          <h2>Drive Shaft Input Torque Formulation</h2>
          <p>The mechanical torque (\(T\)) demanded by the pump shaft determines coupling selection and shaft shear safety:</p>

          <div class="formula-box">
            $$T = \frac{V_g \cdot P}{20 \cdot \pi \cdot \eta_{hm}} \quad [\text{N}\cdot\text{m}] \quad \Longleftrightarrow \quad T = \frac{V_g \cdot P}{24 \cdot \pi \cdot \eta_{hm}} \quad [\text{lb}\cdot\text{ft}]$$
          </div>

          <p>Where \(V_g\) is pump geometric displacement per revolution (\(\text{cm}^3/\text{rev}\) or \(\text{in}^3/\text{rev}\)).</p>

          <h2>Pump Displacement & Delivery Flow Rate Relationships</h2>
          <p>Theoretical discharge flow rate (\(Q_{\text{theo}}\)) is purely geometric, whereas actual delivered flow (\(Q_{\text{actual}}\)) reflects volumetric slippage:</p>

          <div class="formula-box">
            $$Q_{\text{theo}} = \frac{V_g \cdot N}{1000} \quad [\text{L/min}] \quad \implies \quad Q_{\text{actual}} = Q_{\text{theo}} \cdot \eta_v$$
          </div>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Hydraulic Pump Architecture</th>
                <th>Typical Pressure Rating</th>
                <th>Volumetric Efficiency (\(\eta_v\))</th>
                <th>Hydromechanical (\(\eta_{hm}\))</th>
                <th>Overall Efficiency (\(\eta_t\))</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>External Gear Pump</td>
                <td>150 &ndash; 250 bar (2,200 &ndash; 3,600 psi)</td>
                <td>0.88 &ndash; 0.93</td>
                <td>0.85 &ndash; 0.90</td>
                <td>0.75 &ndash; 0.84</td>
              </tr>
              <tr>
                <td>Internal Gear / Gerotor</td>
                <td>100 &ndash; 210 bar (1,500 &ndash; 3,000 psi)</td>
                <td>0.90 &ndash; 0.95</td>
                <td>0.88 &ndash; 0.92</td>
                <td>0.80 &ndash; 0.87</td>
              </tr>
              <tr>
                <td>Vane Pump (Balanced)</td>
                <td>140 &ndash; 210 bar (2,000 &ndash; 3,000 psi)</td>
                <td>0.90 &ndash; 0.96</td>
                <td>0.88 &ndash; 0.93</td>
                <td>0.80 &ndash; 0.88</td>
              </tr>
              <tr>
                <td>Axial Piston (Swashplate)</td>
                <td>250 &ndash; 420 bar (3,600 &ndash; 6,000 psi)</td>
                <td>0.95 &ndash; 0.98</td>
                <td>0.92 &ndash; 0.96</td>
                <td>0.88 &ndash; 0.94</td>
              </tr>
              <tr>
                <td>Radial Piston Pump</td>
                <td>350 &ndash; 700 bar (5,000 &ndash; 10,000 psi)</td>
                <td>0.96 &ndash; 0.99</td>
                <td>0.93 &ndash; 0.97</td>
                <td>0.90 &ndash; 0.95</td>
              </tr>
            </tbody>
          </table>

          <div class="worked-example-card">
            <h3>Step-by-Step Worked Case Study: CNC Machine Tool HPU Sizing</h3>
            <p><strong>Design Scenario:</strong> An engineer is sizing the electric motor and pump for a modern CNC machine tool clamping and pallet changer hydraulic power unit:</p>
            <ul>
              <li>Required flow rate: \(Q = 60\text{ L/min}\) (\(15.85\text{ GPM}\)).</li>
              <li>Maximum operating pressure: \(P = 210\text{ bar}\) (\(3,045\text{ psi}\)).</li>
              <li>Drive motor speed: 4-pole 60 Hz electric motor running at \(N = 1,750\text{ RPM}\).</li>
              <li>Pump type: Variable-displacement axial piston pump.</li>
              <li>Efficiencies: Volumetric \(\eta_v = 0.95\) (\(95\%\)), Hydromechanical \(\eta_{hm} = 0.92\) (\(92\%\)).</li>
            </ul>

            <p><strong>Step 1: Compute overall total pump efficiency (\(\eta_{\text{total}}\))</strong></p>
            <div class="formula-box">
              $$\eta_{\text{total}} = \eta_v \cdot \eta_{hm} = 0.95 \times 0.92 = 0.874 \quad (87.4\%)$$
            </div>

            <p><strong>Step 2: Calculate hydraulic fluid output power (\(P_{\text{hyd}}\))</strong></p>
            <div class="formula-box">
              $$P_{\text{hyd}} = \frac{P \cdot Q}{600} = \frac{210\text{ bar} \cdot 60\text{ L/min}}{600} = \frac{12,600}{600} = 21.00\text{ kW} \quad (28.16\text{ HP})$$
            </div>

            <p><strong>Step 3: Calculate required electric motor shaft power (\(P_{\text{shaft}}\))</strong></p>
            <div class="formula-box">
              $$P_{\text{shaft}} = \frac{P_{\text{hyd}}}{\eta_{\text{total}}} = \frac{21.00\text{ kW}}{0.874} = 24.03\text{ kW} \quad (32.22\text{ HP})$$
            </div>
            <p>The engineer selects the next standard commercial electric motor size: <strong>30 kW (40 HP)</strong>.</p>

            <p><strong>Step 4: Calculate required pump displacement (\(V_g\))</strong></p>
            <div class="formula-box">
              $$V_g = \frac{Q \cdot 1000}{N \cdot \eta_v} = \frac{60 \cdot 1000}{1750 \cdot 0.95} = \frac{60000}{1662.5} = 36.09\text{ cc/rev}$$
            </div>
            <p>The engineer selects a standard <strong>45 cc/rev</strong> variable displacement pump derated to 36 cc/rev.</p>

            <p><strong>Step 5: Compute required drive shaft input torque (\(T\))</strong></p>
            <div class="formula-box">
              $$T = \frac{V_g \cdot P}{20 \cdot \pi \cdot \eta_{hm}} = \frac{36.09 \cdot 210}{20 \cdot \pi \cdot 0.92} = \frac{7578.9}{57.805} = 131.1\text{ N}\cdot\text{m} \quad (96.7\text{ lb}\cdot\text{ft})$$
            </div>
          </div>

          <h2>Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3>Why does electric motor power depend on overall pump efficiency?</h3>
            <p>If overall efficiency (\(\eta_{\text{total}} = 0.80\)) is ignored, calculating power purely as \(P \cdot Q / 600\) underestimates required shaft power by 25%. A 20 kW hydraulic load with 80% pump efficiency actually demands 25 kW from the electric motor. Sizing the motor without efficiency losses causes motor overload trips, blown fuses, and premature winding insulation failure.</p>
          </div>

          <div class="faq-item">
            <h3>What happens to the energy lost to pump inefficiency?</h3>
            <p>Every watt of energy lost due to volumetric leakage and hydromechanical friction transforms directly into <strong>heat within the hydraulic fluid</strong>. In a 30 kW system operating at 85% efficiency, 4.5 kW of continuous thermal energy enters the oil reservoir. If an air/oil heat exchanger is not sized to dissipate this parasitic heat, fluid temperatures will rapidly exceed 80&deg;C, destroying seals and degrading oil viscosity.</p>
          </div>

          <div class="faq-item">
            <h3>How do pressure-compensated variable displacement pumps save power?</h3>
            <p>A fixed displacement pump constantly pumps its full rated flow (\(Q_{\text{max}}\)). When actuators are stationary, the entire flow dumps over the relief valve at full pressure, wasting 100% of motor power as boiling heat. In contrast, a pressure-compensated pump automatically destroke its swashplate to near-zero displacement (\(Q \to 0\)) when pressure reaches setpoint, holding full pressure while drawing only 5% to 10% standby motor power.</p>
          </div>

          <div class="faq-item">
            <h3>How does altitude affect hydraulic pump power and performance?</h3>
            <p>While hydraulic pressure is generated mechanically, atmospheric pressure pushes oil from the open reservoir into the pump suction port. At high altitudes (> 2,000 meters / 6,500 ft), lower atmospheric pressure reduces net positive suction head (NPSH), causing severe pump cavitation. To prevent pump destruction at high elevations, reservoirs must be pressurized to 0.2 &ndash; 0.5 bar, or pump suction lines must be enlarged to lower fluid velocity below 0.8 m/s.</p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar" id="toolSidebar">
        <!-- Dynamically rendered sidebar -->
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; 2026 CalcHub. All rights reserved. Engineering and mathematical tools grounded in international standards.</p>
      <ul class="footer-links">
        <li><a href="index.html">Home</a></li>
        <li><a href="mechanical.html">Mechanical</a></li>
        <li><a href="ohms-law-calculator.html">Ohm's Law</a></li>
        <li><a href="sitemap.xml">Sitemap</a></li>
      </ul>
    </div>
  </footer>

  <script>
    const PUMP_PRESETS = {
      axialPiston: { vol: 96, hm: 94 },
      externalGear: { vol: 90, hm: 91 },
      internalGear: { vol: 93, hm: 91 },
      vanePump: { vol: 93, hm: 92 },
      radialPiston: { vol: 97, hm: 95 }
    };

    const pumpCalcModeSelect = document.getElementById('pumpCalcMode');
    const powerUnitsSelect = document.getElementById('powerUnits');
    const pumpTypeSelect = document.getElementById('pumpType');
    const pumpPressureInput = document.getElementById('pumpPressure');
    const flowRateValInput = document.getElementById('flowRateVal');
    const displacementValInput = document.getElementById('displacementVal');
    const driveRpmSelect = document.getElementById('driveRpm');
    const volEfficiencyInput = document.getElementById('volEfficiency');
    const mechEfficiencyInput = document.getElementById('mechEfficiency');

    const lblPumpPress = document.getElementById('lblPumpPress');
    const lblFlowRate = document.getElementById('lblFlowRate');
    const lblDisplacement = document.getElementById('lblDisplacement');
    const grpFlowRate = document.getElementById('grpFlowRate');
    const grpDisplacement = document.getElementById('grpDisplacement');

    const pumpPowerResultBox = document.getElementById('pumpPowerResultBox');
    const resMotorPower = document.getElementById('resMotorPower');
    const resHydPower = document.getElementById('resHydPower');
    const resDriveTorque = document.getElementById('resDriveTorque');
    const resDisplacement = document.getElementById('resDisplacement');
    const resActualFlow = document.getElementById('resActualFlow');
    const resTotalEfficiency = document.getElementById('resTotalEfficiency');
    const resHeatLoss = document.getElementById('resHeatLoss');
    const resMotorRec = document.getElementById('resMotorRec');
    const pumpPowerNotesBox = document.getElementById('pumpPowerNotesBox');

    pumpTypeSelect.addEventListener('change', function() {
      const type = this.value;
      if (type !== 'custom') {
        const p = PUMP_PRESETS[type] || { vol: 95, hm: 92 };
        volEfficiencyInput.value = p.vol;
        mechEfficiencyInput.value = p.hm;
      }
      calculatePumpPower();
    });

    pumpCalcModeSelect.addEventListener('change', function() {
      if (this.value === 'fromFlow') {
        grpFlowRate.style.display = 'block';
        grpDisplacement.style.display = 'none';
      } else {
        grpFlowRate.style.display = 'none';
        grpDisplacement.style.display = 'block';
      }
      calculatePumpPower();
    });

    powerUnitsSelect.addEventListener('change', function() {
      const isMetric = this.value === 'metric';
      if (isMetric) {
        lblPumpPress.textContent = "Operating Working Pressure [bar]";
        lblFlowRate.textContent = "Delivered Flow Rate (Q) [L/min]";
        lblDisplacement.textContent = "Pump Displacement (Vg) [cc/rev]";
        pumpPressureInput.value = 210;
        flowRateValInput.value = 60;
        displacementValInput.value = 45;
      } else {
        lblPumpPress.textContent = "Operating Working Pressure [psi]";
        lblFlowRate.textContent = "Delivered Flow Rate (Q) [GPM]";
        lblDisplacement.textContent = "Pump Displacement (Vg) [cu in/rev]";
        pumpPressureInput.value = 3000;
        flowRateValInput.value = 16;
        displacementValInput.value = 2.75;
      }
      calculatePumpPower();
    });

    function calculatePumpPower() {
      const mode = pumpCalcModeSelect.value;
      const isMetric = powerUnitsSelect.value === 'metric';
      const N = parseFloat(driveRpmSelect.value) || 1750;

      const eta_v = (parseFloat(volEfficiencyInput.value) || 95) / 100;
      const eta_hm = (parseFloat(mechEfficiencyInput.value) || 92) / 100;
      const eta_total = eta_v * eta_hm;

      let P = parseFloat(pumpPressureInput.value);
      if (isNaN(P) || P <= 0) P = isMetric ? 210 : 3000;

      let Q = 0; // L/min (metric) or GPM (imperial)
      let Vg = 0; // cc/rev (metric) or cu in/rev (imperial)

      if (mode === 'fromFlow') {
        Q = parseFloat(flowRateValInput.value);
        if (isNaN(Q) || Q <= 0) Q = isMetric ? 60 : 16;

        if (isMetric) {
          // Vg [cc/rev] = (Q [L/min] * 1000) / (N * eta_v)
          Vg = (Q * 1000) / (N * eta_v);
        } else {
          // Vg [cu in/rev] = (Q [GPM] * 231) / (N * eta_v)
          Vg = (Q * 231) / (N * eta_v);
        }
      } else {
        Vg = parseFloat(displacementValInput.value);
        if (isNaN(Vg) || Vg <= 0) Vg = isMetric ? 45 : 2.75;

        if (isMetric) {
          // Q [L/min] = (Vg [cc/rev] * N * eta_v) / 1000
          Q = (Vg * N * eta_v) / 1000;
        } else {
          // Q [GPM] = (Vg [cu in/rev] * N * eta_v) / 231
          Q = (Vg * N * eta_v) / 231;
        }
      }

      // Hydraulic Power (P_hyd)
      let P_hyd = 0;
      let P_shaft = 0;
      let T_shaft = 0;
      let uPwr = isMetric ? 'kW' : 'HP';
      let uTorque = isMetric ? 'N·m' : 'lb·ft';
      let uFlow = isMetric ? 'L/min' : 'GPM';
      let uDisp = isMetric ? 'cc/rev' : 'in³/rev';

      if (isMetric) {
        P_hyd = (P * Q) / 600; // kW
        P_shaft = P_hyd / eta_total; // kW
        // Torque [N*m] = (Vg [cc] * P [bar]) / (20 * pi * eta_hm)
        T_shaft = (Vg * P) / (20 * Math.PI * eta_hm);
      } else {
        P_hyd = (P * Q) / 1714; // HP
        P_shaft = P_hyd / eta_total; // HP
        // Torque [lb*ft] = (Vg [in^3] * P [psi]) / (24 * pi * eta_hm)
        T_shaft = (Vg * P) / (24 * Math.PI * eta_hm);
      }

      const heatLoss = P_shaft - P_hyd;

      // Recommended standard electric motor rating
      const STANDARD_MOTORS_KW = [0.75, 1.1, 1.5, 2.2, 3.0, 4.0, 5.5, 7.5, 11, 15, 18.5, 22, 30, 37, 45, 55, 75, 90, 110, 132, 160, 200];
      const STANDARD_MOTORS_HP = [1, 1.5, 2, 3, 5, 7.5, 10, 15, 20, 25, 30, 40, 50, 60, 75, 100, 125, 150, 200, 250];

      let recMotorStr = "";
      if (isMetric) {
        let matchKw = STANDARD_MOTORS_KW[STANDARD_MOTORS_KW.length - 1];
        for (let kw of STANDARD_MOTORS_KW) {
          if (kw >= P_shaft) {
            matchKw = kw;
            break;
          }
        }
        recMotorStr = `${matchKw} kW (${Math.round(matchKw * 1.341)} HP) Standard Frame`;
      } else {
        let matchHp = STANDARD_MOTORS_HP[STANDARD_MOTORS_HP.length - 1];
        for (let hp of STANDARD_MOTORS_HP) {
          if (hp >= P_shaft) {
            matchHp = hp;
            break;
          }
        }
        recMotorStr = `${matchHp} HP (${(matchHp * 0.7457).toFixed(1)} kW) NEMA Frame`;
      }

      resMotorPower.textContent = P_shaft.toFixed(2) + " " + uPwr;
      resHydPower.textContent = P_hyd.toFixed(2) + " " + uPwr;
      resDriveTorque.textContent = T_shaft.toFixed(1) + " " + uTorque;
      resDisplacement.textContent = Vg.toFixed(1) + " " + uDisp;
      resActualFlow.textContent = Q.toFixed(1) + " " + uFlow;
      resTotalEfficiency.textContent = (eta_total * 100).toFixed(1) + "%";
      resHeatLoss.textContent = heatLoss.toFixed(2) + " " + uPwr;
      resMotorRec.textContent = recMotorStr;

      let notes = `<strong>ISO 4409 Sizing Analysis:</strong> Pumping <strong>${Q.toFixed(1)} ${uFlow}</strong> at <strong>${P} ${isMetric ? 'bar' : 'psi'}</strong> demands <strong>${P_shaft.toFixed(1)} ${uPwr}</strong> at <strong>${T_shaft.toFixed(1)} ${uTorque}</strong> torque. Parasitic heat dissipation into oil is <strong>${heatLoss.toFixed(2)} ${uPwr}</strong>.`;
      pumpPowerNotesBox.innerHTML = notes;

      pumpPowerResultBox.style.display = 'block';
    }

    document.getElementById('calcPowerBtn').addEventListener('click', calculatePumpPower);
    document.getElementById('resetPowerBtn').addEventListener('click', function() {
      setTimeout(calculatePumpPower, 50);
    });

    window.addEventListener('DOMContentLoaded', calculatePumpPower);
  </script>
</body>
</html>
"""

def main():
    target_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    file3 = os.path.join(target_dir, "hydraulic-cylinder-speed-calculator.html")
    with open(file3, "w", encoding="utf-8") as f:
        f.write(TOOL_3_HTML)
    print(f"[PASS] hydraulic-cylinder-speed-calculator.html generated successfully!")

    file4 = os.path.join(target_dir, "hydraulic-pump-power-calculator.html")
    with open(file4, "w", encoding="utf-8") as f:
        f.write(TOOL_4_HTML)
    print(f"[PASS] hydraulic-pump-power-calculator.html generated successfully!")

if __name__ == "__main__":
    main()
