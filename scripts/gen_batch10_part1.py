# -*- coding: utf-8 -*-
"""
Script to generate Batch 10 Part 1 tools:
1. hydraulic-cylinder-calculator.html
2. hydraulic-cylinder-force-calculator.html
"""
import os

TOOL_1_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hydraulic Cylinder Calculator | Force, Speed, Flow Rate & Cycle Time</title>
  <meta name="description" content="Calculate hydraulic cylinder extension and retraction force, piston velocity, required pump flow rate (GPM/LPM), stroke volume, and cycle times per ISO 6020/2 and NFPA standards.">
  <link rel="canonical" href="https://calchub.cloud/hydraulic-cylinder-calculator.html">
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
        "name": "Hydraulic Cylinder Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Comprehensive fluid power calculation tool determining hydraulic cylinder push/pull force, extension velocity, stroke volume, pump flow rate, and column buckling safety per ISO 6020/2.",
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
            "name": "How is hydraulic cylinder extension (push) force calculated?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Extension force is the product of operating hydraulic pressure and full piston bore area: F_ext = P * A_bore = P * (pi * D_bore^2 / 4). In metric: Force [N] = Pressure [bar] * Area [mm^2] / 10. In imperial: Force [lbf] = Pressure [psi] * Area [sq in]."
            }
          },
          {
            "@type": "Question",
            "name": "Why is retraction (pull) force always lower than extension force in a single-rod cylinder?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In a standard single-rod double-acting cylinder, the piston rod occupies volume inside the rod-end cap. When pressurized to retract, hydraulic oil acts only on the net annular area: A_annulus = A_bore - A_rod = (pi / 4) * (D_bore^2 - d_rod^2). Because annular area is 20% to 50% smaller than full bore area, retraction force is proportionally lower at the same hydraulic pressure."
            }
          },
          {
            "@type": "Question",
            "name": "How does cylinder velocity relate to hydraulic pump flow rate (GPM or LPM)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Linear piston speed is volumetric flow rate divided by effective area: v = Q / A. In metric: v [m/s] = (Q [L/min] * 10^3) / (A [mm^2] * 60). In imperial: v [in/s] = (231 * Q [GPM]) / (A [sq in] * 60) approx 3.85 * Q / A. Because the annular area is smaller, retraction velocity is always faster than extension velocity for a constant pump flow rate."
            }
          },
          {
            "@type": "Question",
            "name": "What is column buckling in hydraulic cylinder rods and how is it prevented?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Under heavy compressive push loads across long strokes, a slender piston rod behaves as an Euler structural column. If the load exceeds the critical Euler buckling load (P_crit = pi^2 * E * I / (K * L)^2), the rod suddenly bows and bends plastically, destroying cylinder gland seals. Sizing requires verifying that the working force remains below P_crit divided by a safety factor of 3.0 to 4.0."
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
      <span>Hydraulic Cylinder Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">ISO 6020/2 &amp; NFPA Fluid Power Standards</div>
          <h1 class="calc-title">Hydraulic Cylinder Calculator</h1>
          <p class="calc-tagline">Calculate hydraulic cylinder extension and retraction force, piston velocities, fluid volume requirements, pump flow rate, and full cycle times.</p>
        </header>

        <div class="tool-card">
          <form id="cylCalcForm">
            <div class="calc-grid">
              <div class="form-group">
                <label for="cylUnits">Engineering Units</label>
                <select id="cylUnits">
                  <option value="metric" selected>Metric (mm, bar, kN, L/min, m/s)</option>
                  <option value="imperial">Imperial (in, psi, lbf, GPM, in/s)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="boreDiam" id="lblBoreDiam">Piston Bore Diameter (D) [mm]</label>
                <input type="number" id="boreDiam" step="1" min="10" max="1000" value="80">
              </div>

              <div class="form-group">
                <label for="rodDiam" id="lblRodDiam">Piston Rod Diameter (d) [mm]</label>
                <input type="number" id="rodDiam" step="1" min="5" max="950" value="45">
              </div>

              <div class="form-group">
                <label for="strokeLength" id="lblStrokeLength">Stroke Length (S) [mm]</label>
                <input type="number" id="strokeLength" step="10" min="10" max="10000" value="500">
              </div>

              <div class="form-group">
                <label for="operatingPressure" id="lblPressure">Operating Hydraulic Pressure (P) [bar]</label>
                <input type="number" id="operatingPressure" step="5" min="5" max="1000" value="210">
              </div>

              <div class="form-group">
                <label for="pumpFlow" id="lblPumpFlow">Pump Flow Rate to Cylinder (Q) [L/min]</label>
                <input type="number" id="pumpFlow" step="1" min="0.1" max="2000" value="30">
              </div>

              <div class="form-group">
                <label for="mechEfficiency">Cylinder Mechanical Seal Efficiency (&eta;m)</label>
                <select id="mechEfficiency">
                  <option value="0.95" selected>95% (Standard Polyurethane Lip Seals)</option>
                  <option value="0.90">90% (Heavy Duty Cast Iron Piston Rings)</option>
                  <option value="0.98">98% (Low-Friction PTFE Bronze Step Seals)</option>
                  <option value="1.00">100% (Theoretical Ideal / No Friction)</option>
                </select>
              </div>
            </div>

            <div class="calc-actions">
              <button type="button" id="calcCylBtn" class="btn btn-primary">Calculate Cylinder Dynamics</button>
              <button type="reset" id="resetCylBtn" class="btn btn-secondary">Reset Defaults</button>
            </div>
          </form>

          <div id="cylResultBox" class="results-container" style="display: none;">
            <h3>Fluid Power Performance Results</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label">Extension Force (Push)</span>
                <span id="resExtForce" class="result-value">-- kN</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Retraction Force (Pull)</span>
                <span id="resRetForce" class="result-value">-- kN</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Extension Velocity (v_ext)</span>
                <span id="resExtSpeed" class="result-value">-- m/s</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Retraction Velocity (v_ret)</span>
                <span id="resRetSpeed" class="result-value">-- m/s</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Extension Time (t_ext)</span>
                <span id="resExtTime" class="result-value">-- s</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Retraction Time (t_ret)</span>
                <span id="resRetTime" class="result-value">-- s</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Full Stroke Fluid Volume (Ext)</span>
                <span id="resExtVol" class="result-value">-- L</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Hydraulic Power Required</span>
                <span id="resHydPower" class="result-value">-- kW</span>
              </div>
            </div>
            <div id="cylNotesBox" style="margin-top: 1rem; color: #1e40af; background: #eff6ff; border: 1px solid #bfdbfe; padding: 0.75rem; border-radius: 6px;"></div>
          </div>
        </div>

        <article class="article-body">
          <h2>Applied Fluid Power & Hydraulic Actuator Fundamentals</h2>
          <p>Hydraulic cylinders (linear hydraulic actuators) convert fluid energy supplied by a high-pressure pump into linear mechanical force and motion. Governed by Pascal's principle and standardized internationally under <strong>ISO 6020/2</strong> and <strong>NFPA/T3.6.7 R2</strong>, hydraulic cylinders deliver the highest power-to-weight and power-to-size density of any mechanical actuator, generating thousands of kilonewtons of force in earthmoving excavators, industrial metal-forming presses, plastic injection molding clamps, and offshore lifting cranes.</p>

          <p>Proper cylinder sizing requires precise coordination between hydraulic fluid operating pressure, piston bore diameter, rod diameter, and pump delivery flow rate. Undersizing a cylinder forces the hydraulic system to constantly operate near the relief valve pressure threshold, causing severe oil overheating and premature pump cavitation. Conversely, gross oversizing demands excessive oil reservoir volumes, reduces actuation speed, and multiplies structural deadweight.</p>

          <h2>Mathematical Formulations for Cylinder Force</h2>
          <p>In a double-acting, single-rod hydraulic cylinder, fluid pressure can be applied alternately to the piston bore side (cap end) to extend the rod, or to the rod side (annular end) to retract the rod.</p>

          <h3>1. Extension (Push) Force Formulation</h3>
          <p>During extension, pressurized oil acts across the entire circular surface of the piston head. The theoretical push force (\(F_{\text{ext}}\)) is:</p>

          <div class="formula-box">
            $$A_{\text{bore}} = \frac{\pi}{4} D_{\text{bore}}^2 \quad \implies \quad F_{\text{ext}} = \eta_m \cdot P \cdot A_{\text{bore}}$$
          </div>

          <p>Where:</p>
          <ul>
            <li><strong>\(P\)</strong>: Operating hydraulic gauge pressure (\(\text{bar}\) or \(\text{psi}\)).</li>
            <li><strong>\(D_{\text{bore}}\)</strong>: Inside diameter of the cylinder tube barrel.</li>
            <li><strong>\(\eta_m\)</strong>: Mechanical seal efficiency (typically 0.92 to 0.96, accounting for dynamic seal friction drag).</li>
          </ul>

          <h3>2. Retraction (Pull) Force Formulation</h3>
          <p>During retraction, hydraulic fluid enters the rod end. Because the solid steel piston rod displaces oil volume, pressure acts exclusively on the ring-shaped <strong>annular area</strong> (\(A_{\text{annulus}}\)):</p>

          <div class="formula-box">
            $$A_{\text{annulus}} = A_{\text{bore}} - A_{\text{rod}} = \frac{\pi}{4} \left( D_{\text{bore}}^2 - d_{\text{rod}}^2 \right)$$
            $$F_{\text{ret}} = \eta_m \cdot P \cdot A_{\text{annulus}}$$
          </div>

          <p>Because \(A_{\text{annulus}} < A_{\text{bore}}\), a single-rod cylinder produces a lower pulling force than pushing force at identical hydraulic pressures. The force differential ratio is governed by the diameter ratio:</p>

          <div class="formula-box">
            $$\frac{F_{\text{ret}}}{F_{\text{ext}}} = 1 - \left(\frac{d_{\text{rod}}}{D_{\text{bore}}}\right)^2$$
          </div>

          <h2>Actuator Kinematics: Piston Speed, Flow Rate & Cycle Time</h2>
          <p>The linear velocity (\(v\)) of the piston is directly proportional to volumetric flow rate (\(Q\)) delivered into the cylinder and inversely proportional to the effective area:</p>

          <div class="formula-box">
            $$v_{\text{ext}} = \frac{Q}{A_{\text{bore}}} \quad \text{and} \quad v_{\text{ret}} = \frac{Q}{A_{\text{annulus}}}$$
          </div>

          <p>Because the annular volume is smaller than the bore volume, <strong>retraction velocity is always faster than extension velocity</strong> for a fixed pump discharge rate. The time (\(t\)) required to traverse stroke length (\(S\)) is:</p>

          <div class="formula-box">
            $$t_{\text{ext}} = \frac{S}{v_{\text{ext}}} = \frac{A_{\text{bore}} \cdot S}{Q}, \quad t_{\text{ret}} = \frac{S}{v_{\text{ret}}} = \frac{A_{\text{annulus}} \cdot S}{Q}$$
            $$t_{\text{cycle}} = t_{\text{ext}} + t_{\text{ret}}$$
          </div>

          <h2>Hydraulic Fluid Volume and Power Consumption</h2>
          <p>The fluid volume (\(V\)) displaced during each stroke determines reservoir sizing and accumulator capacity:</p>

          <div class="formula-box">
            $$V_{\text{ext}} = A_{\text{bore}} \cdot S \quad \text{and} \quad V_{\text{ret}} = A_{\text{annulus}} \cdot S$$
          </div>

          <p>Theoretical hydraulic power (\(P_{\text{hyd}}\)) consumed during actuation is the product of operating pressure and volumetric flow:</p>

          <div class="formula-box">
            $$P_{\text{hyd}} = \frac{P \cdot Q}{600} \quad [\text{kW}] \quad (\text{with } P \text{ in bar and } Q \text{ in L/min})$$
            $$P_{\text{hyd}} = \frac{P \cdot Q}{1714} \quad [\text{HP}] \quad (\text{with } P \text{ in psi and } Q \text{ in GPM})$$
          </div>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Standard Metric Bore / Rod Combinations (ISO 6020/2)</th>
                <th>Bore Area (\(\text{cm}^2\))</th>
                <th>Annular Area (\(\text{cm}^2\))</th>
                <th>Area Ratio (\(A_{\text{ann}} / A_{\text{bore}}\))</th>
                <th>Force at 210 bar (kN Ext / Ret)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>40 mm Bore / 22 mm Rod</td>
                <td>12.57</td>
                <td>8.76</td>
                <td>0.70</td>
                <td>25.1 kN / 17.5 kN</td>
              </tr>
              <tr>
                <td>50 mm Bore / 28 mm Rod</td>
                <td>19.63</td>
                <td>13.48</td>
                <td>0.69</td>
                <td>39.2 kN / 26.9 kN</td>
              </tr>
              <tr>
                <td>63 mm Bore / 36 mm Rod</td>
                <td>31.17</td>
                <td>20.99</td>
                <td>0.67</td>
                <td>62.2 kN / 41.9 kN</td>
              </tr>
              <tr>
                <td>80 mm Bore / 45 mm Rod</td>
                <td>50.27</td>
                <td>34.36</td>
                <td>0.68</td>
                <td>100.3 kN / 68.5 kN</td>
              </tr>
              <tr>
                <td>100 mm Bore / 56 mm Rod</td>
                <td>78.54</td>
                <td>53.91</td>
                <td>0.69</td>
                <td>156.7 kN / 107.5 kN</td>
              </tr>
              <tr>
                <td>125 mm Bore / 70 mm Rod</td>
                <td>122.72</td>
                <td>84.23</td>
                <td>0.69</td>
                <td>244.8 kN / 168.0 kN</td>
              </tr>
              <tr>
                <td>160 mm Bore / 90 mm Rod</td>
                <td>201.06</td>
                <td>137.44</td>
                <td>0.68</td>
                <td>401.1 kN / 274.2 kN</td>
              </tr>
            </tbody>
          </table>

          <h2>Euler Column Buckling Constraints on Cylinder Rods</h2>
          <p>A hydraulic cylinder pushing a heavy load with an extended rod acts as an axially loaded slender column. If the compressive push force exceeds the <strong>Euler critical buckling load</strong> (\(F_{\text{buckling}}\)), the piston rod will suddenly deflect sideways and buckle permanently:</p>

          <div class="formula-box">
            $$F_{\text{buckling}} = \frac{\pi^2 \cdot E \cdot I}{L_k^2} \quad \implies \quad F_{\text{allowable}} = \frac{F_{\text{buckling}}}{SF}$$
          </div>

          <p>Where \(E\) is Young's Modulus (\(2.1 \times 10^5\text{ N/mm}^2\) for steel), \(I = \frac{\pi}{64} d_{\text{rod}}^4\) is the second moment of area of the solid rod, \(L_k\) is the effective buckling stroke length (dependent on pin-clevis vs rigid flange mounting geometry), and \(SF\) is the mandatory safety factor (typically \(3.5\) to \(4.0\)).</p>

          <div class="worked-example-card">
            <h3>Step-by-Step Worked Case Study: Scrap Metal Baler Compactor Cylinder</h3>
            <p><strong>Design Scenario:</strong> An engineer is designing a hydraulic compactor for an industrial recycling scrap baler using standard 210 bar (3,045 psi) hydraulics:</p>
            <ul>
              <li>Piston bore: \(D_{\text{bore}} = 80\text{ mm}\) (\(0.080\text{ m}\)).</li>
              <li>Piston rod: \(d_{\text{rod}} = 45\text{ mm}\) (\(0.045\text{ m}\)).</li>
              <li>Stroke length: \(S = 500\text{ mm}\) (\(0.50\text{ m}\)).</li>
              <li>Working pressure: \(P = 210\text{ bar}\) (\(21.0\text{ MPa}\)).</li>
              <li>Pump delivery flow rate: \(Q = 30\text{ L/min}\) (\(0.0005\text{ m}^3/\text{s}\)).</li>
              <li>Mechanical efficiency: \(\eta_m = 0.95\).</li>
            </ul>

            <p><strong>Step 1: Compute bore and annular effective areas</strong></p>
            <div class="formula-box">
              $$A_{\text{bore}} = \frac{\pi}{4} (80)^2 = 5,026.55\text{ mm}^2 = 50.27\text{ cm}^2$$
              $$A_{\text{rod}} = \frac{\pi}{4} (45)^2 = 1,590.43\text{ mm}^2 = 15.90\text{ cm}^2$$
              $$A_{\text{annulus}} = 5,026.55 - 1,590.43 = 3,436.12\text{ mm}^2 = 34.36\text{ cm}^2$$
            </div>

            <p><strong>Step 2: Calculate extension and retraction forces</strong></p>
            <div class="formula-box">
              $$F_{\text{ext}} = 0.95 \cdot (21.0\text{ N/mm}^2) \cdot 5,026.55\text{ mm}^2 = 100,280\text{ N} = 100.28\text{ kN} \quad (22,544\text{ lbf})$$
              $$F_{\text{ret}} = 0.95 \cdot (21.0\text{ N/mm}^2) \cdot 3,436.12\text{ mm}^2 = 68,551\text{ N} = 68.55\text{ kN} \quad (15,411\text{ lbf})$$
            </div>

            <p><strong>Step 3: Determine piston velocities and stroke cycle time</strong></p>
            <div class="formula-box">
              $$v_{\text{ext}} = \frac{30 \times 10^6\text{ mm}^3 / 60\text{ s}}{5026.55\text{ mm}^2} = \frac{500,000}{5026.55} = 99.47\text{ mm/s} = 0.0995\text{ m/s}$$
              $$v_{\text{ret}} = \frac{500,000}{3436.12} = 145.51\text{ mm/s} = 0.1455\text{ m/s}$$
              $$t_{\text{ext}} = \frac{500\text{ mm}}{99.47\text{ mm/s}} = 5.03\text{ seconds}$$
              $$t_{\text{ret}} = \frac{500\text{ mm}}{145.51\text{ mm/s}} = 3.44\text{ seconds}$$
              $$t_{\text{total}} = 5.03 + 3.44 = 8.47\text{ seconds}$$
            </div>

            <p><strong>Step 4: Compute hydraulic pump driving power</strong></p>
            <div class="formula-box">
              $$P_{\text{hyd}} = \frac{210\text{ bar} \cdot 30\text{ L/min}}{600} = 10.50\text{ kW} \quad (14.08\text{ HP})$$
            </div>
            <p><strong>Engineering Conclusion:</strong> Operating at 210 bar, the 80/45 mm cylinder delivers a robust <strong>100.3 kN (10.2 metric tons)</strong> compaction force with a rapid 8.5-second complete cycle time powered by a 10.5 kW electric motor.</p>
          </div>

          <h2>Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3>What is a regenerative hydraulic cylinder circuit and when is it used?</h3>
            <p>A regenerative circuit connects the rod-end port directly back into the cap-end fluid supply line during extension. Because fluid leaving the rod end re-enters the cap end, the effective pump delivery increases, accelerating extension speed by 30% to 100%. However, because the fluid pressure acts simultaneously on both sides, the effective pushing area becomes equal only to the rod area (\(A_{\text{rod}}\)), reducing extension force.</p>
          </div>

          <div class="faq-item">
            <h3>How do end-of-stroke cushions protect hydraulic cylinders?</h3>
            <p>Adjustable cushions utilize tapered spear spuds that throttle discharging oil as the piston nears the end caps, creating a controlled hydraulic backpressure deceleration cushion. This prevents destructive metal-to-metal impact between the piston and cylinder heads, dampens acoustic shockwaves, and protects mechanical linkage pins from fatigue failure.</p>
          </div>

          <div class="faq-item">
            <h3>What is the difference between tie-rod cylinders and welded body cylinders?</h3>
            <p>NFPA tie-rod cylinders utilize four or more high-strength exterior threaded tie-rods to clamp the end caps to the barrel, making them easy to disassemble and repair in standard industrial factory machines. Welded body cylinders weld the end caps directly to the barrel, eliminating tie-rod stretch, providing a much narrower footprint, and offering higher structural strength in rugged mobile construction and mining machinery.</p>
          </div>

          <div class="faq-item">
            <h3>What causes cylinder seal failure and fluid bypass?</h3>
            <p>The primary cause (> 80%) of hydraulic cylinder seal breakdown is fluid particulate contamination (silica dust, metal wear debris) that scores rod chrome plating and cuts elastomer lip seals. Secondary causes include extreme oil overheating (> 80&deg;C) which hardens nitrile/polyurethane seals, side-load misalignment which wears guide wear-rings, and pressure spikes that cause seal extrusion through clearance gaps.</p>
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
    const cylUnitsSelect = document.getElementById('cylUnits');
    const boreDiamInput = document.getElementById('boreDiam');
    const rodDiamInput = document.getElementById('rodDiam');
    const strokeLengthInput = document.getElementById('strokeLength');
    const operatingPressureInput = document.getElementById('operatingPressure');
    const pumpFlowInput = document.getElementById('pumpFlow');
    const mechEfficiencySelect = document.getElementById('mechEfficiency');

    const lblBoreDiam = document.getElementById('lblBoreDiam');
    const lblRodDiam = document.getElementById('lblRodDiam');
    const lblStrokeLength = document.getElementById('lblStrokeLength');
    const lblPressure = document.getElementById('lblPressure');
    const lblPumpFlow = document.getElementById('lblPumpFlow');

    const cylResultBox = document.getElementById('cylResultBox');
    const resExtForce = document.getElementById('resExtForce');
    const resRetForce = document.getElementById('resRetForce');
    const resExtSpeed = document.getElementById('resExtSpeed');
    const resRetSpeed = document.getElementById('resRetSpeed');
    const resExtTime = document.getElementById('resExtTime');
    const resRetTime = document.getElementById('resRetTime');
    const resExtVol = document.getElementById('resExtVol');
    const resHydPower = document.getElementById('resHydPower');
    const cylNotesBox = document.getElementById('cylNotesBox');

    cylUnitsSelect.addEventListener('change', function() {
      const isMetric = this.value === 'metric';
      if (isMetric) {
        lblBoreDiam.textContent = "Piston Bore Diameter (D) [mm]";
        lblRodDiam.textContent = "Piston Rod Diameter (d) [mm]";
        lblStrokeLength.textContent = "Stroke Length (S) [mm]";
        lblPressure.textContent = "Operating Hydraulic Pressure (P) [bar]";
        lblPumpFlow.textContent = "Pump Flow Rate to Cylinder (Q) [L/min]";
        boreDiamInput.value = 80;
        rodDiamInput.value = 45;
        strokeLengthInput.value = 500;
        operatingPressureInput.value = 210;
        pumpFlowInput.value = 30;
      } else {
        lblBoreDiam.textContent = "Piston Bore Diameter (D) [in]";
        lblRodDiam.textContent = "Piston Rod Diameter (d) [in]";
        lblStrokeLength.textContent = "Stroke Length (S) [in]";
        lblPressure.textContent = "Operating Hydraulic Pressure (P) [psi]";
        lblPumpFlow.textContent = "Pump Flow Rate to Cylinder (Q) [GPM]";
        boreDiamInput.value = 3.25;
        rodDiamInput.value = 1.75;
        strokeLengthInput.value = 20.0;
        operatingPressureInput.value = 3000;
        pumpFlowInput.value = 8.0;
      }
      calculateCylinder();
    });

    function calculateCylinder() {
      const isMetric = cylUnitsSelect.value === 'metric';
      const eta = parseFloat(mechEfficiencySelect.value);

      let D = parseFloat(boreDiamInput.value);
      let d = parseFloat(rodDiamInput.value);
      let S = parseFloat(strokeLengthInput.value);
      let P = parseFloat(operatingPressureInput.value);
      let Q = parseFloat(pumpFlowInput.value);

      if (isNaN(D) || D <= 0) D = isMetric ? 80 : 3.25;
      if (isNaN(d) || d <= 0) d = isMetric ? 45 : 1.75;
      if (d >= D) d = D * 0.55; // Rod must be smaller than bore
      if (isNaN(S) || S <= 0) S = isMetric ? 500 : 20;
      if (isNaN(P) || P <= 0) P = isMetric ? 210 : 3000;
      if (isNaN(Q) || Q <= 0) Q = isMetric ? 30 : 8;

      let A_bore_mm2 = 0;
      let A_rod_mm2 = 0;
      let A_ann_mm2 = 0;

      let F_ext_N = 0;
      let F_ret_N = 0;
      let v_ext_mps = 0;
      let v_ret_mps = 0;
      let V_ext_L = 0;
      let P_hyd_kW = 0;

      if (isMetric) {
        A_bore_mm2 = (Math.PI / 4) * Math.pow(D, 2);
        A_rod_mm2 = (Math.PI / 4) * Math.pow(d, 2);
        A_ann_mm2 = A_bore_mm2 - A_rod_mm2;

        // Force [N] = P [bar] * 0.1 * A [mm^2] * eta
        F_ext_N = P * 0.1 * A_bore_mm2 * eta;
        F_ret_N = P * 0.1 * A_ann_mm2 * eta;

        // Velocity: v [m/s] = (Q [L/min] * 10^3) / (A [mm^2] * 60)
        v_ext_mps = (Q * 1000) / (A_bore_mm2 * 60);
        v_ret_mps = (Q * 1000) / (A_ann_mm2 * 60);

        // Volume [L] = A_bore [mm^2] * S [mm] / 10^6
        V_ext_L = (A_bore_mm2 * S) / 1e6;

        // Power [kW] = (P [bar] * Q [L/min]) / 600
        P_hyd_kW = (P * Q) / 600;

        resExtForce.textContent = (F_ext_N / 1000).toFixed(2) + " kN (" + (F_ext_N / 9806.65).toFixed(1) + " t)";
        resRetForce.textContent = (F_ret_N / 1000).toFixed(2) + " kN (" + (F_ret_N / 9806.65).toFixed(1) + " t)";
        resExtSpeed.textContent = v_ext_mps.toFixed(3) + " m/s (" + (v_ext_mps * 1000).toFixed(0) + " mm/s)";
        resRetSpeed.textContent = v_ret_mps.toFixed(3) + " m/s (" + (v_ret_mps * 1000).toFixed(0) + " mm/s)";
        resExtVol.textContent = V_ext_L.toFixed(2) + " Liters";
        resHydPower.textContent = P_hyd_kW.toFixed(2) + " kW (" + (P_hyd_kW * 1.341).toFixed(1) + " HP)";
      } else {
        const A_bore_in2 = (Math.PI / 4) * Math.pow(D, 2);
        const A_rod_in2 = (Math.PI / 4) * Math.pow(d, 2);
        const A_ann_in2 = A_bore_in2 - A_rod_in2;

        const F_ext_lbf = P * A_bore_in2 * eta;
        const F_ret_lbf = P * A_ann_in2 * eta;

        // Velocity: v [in/s] = (231 * Q) / (A * 60)
        const v_ext_ips = (231 * Q) / (A_bore_in2 * 60);
        const v_ret_ips = (231 * Q) / (A_ann_in2 * 60);

        // Volume [Gal] = (A_bore_in2 * S) / 231
        const V_ext_gal = (A_bore_in2 * S) / 231;

        // Power [HP] = (P * Q) / 1714
        const P_hyd_hp = (P * Q) / 1714;

        resExtForce.textContent = Math.round(F_ext_lbf).toLocaleString() + " lbf (" + (F_ext_lbf / 2000).toFixed(1) + " tons)";
        resRetForce.textContent = Math.round(F_ret_lbf).toLocaleString() + " lbf (" + (F_ret_lbf / 2000).toFixed(1) + " tons)";
        resExtSpeed.textContent = v_ext_ips.toFixed(2) + " in/s (" + (v_ext_ips * 5).toFixed(0) + " ft/min)";
        resRetSpeed.textContent = v_ret_ips.toFixed(2) + " in/s (" + (v_ret_ips * 5).toFixed(0) + " ft/min)";
        resExtVol.textContent = V_ext_gal.toFixed(2) + " Gallons";
        resHydPower.textContent = P_hyd_hp.toFixed(2) + " HP (" + (P_hyd_hp * 0.7457).toFixed(1) + " kW)";
      }

      // Times
      let t_ext_s = 0;
      let t_ret_s = 0;
      if (isMetric) {
        t_ext_s = S / (v_ext_mps * 1000);
        t_ret_s = S / (v_ret_mps * 1000);
      } else {
        const v_ext_ips = (231 * Q) / (((Math.PI / 4) * Math.pow(D, 2)) * 60);
        const v_ret_ips = (231 * Q) / (((Math.PI / 4) * (Math.pow(D, 2) - Math.pow(d, 2))) * 60);
        t_ext_s = S / v_ext_ips;
        t_ret_s = S / v_ret_ips;
      }

      resExtTime.textContent = t_ext_s.toFixed(2) + " seconds";
      resRetTime.textContent = t_ret_s.toFixed(2) + " seconds (Total: " + (t_ext_s + t_ret_s).toFixed(2) + " s)";

      let notes = `<strong>Cylinder Kinematics:</strong> At <strong>${P} ${isMetric ? 'bar' : 'psi'}</strong> with <strong>${Q} ${isMetric ? 'L/min' : 'GPM'}</strong> flow, full stroke extension takes <strong>${t_ext_s.toFixed(1)} s</strong> and retraction takes <strong>${t_ret_s.toFixed(1)} s</strong>. Annular area ratio is <strong>${((1 - Math.pow(d/D, 2)) * 100).toFixed(0)}%</strong>.`;
      cylNotesBox.innerHTML = notes;

      cylResultBox.style.display = 'block';
    }

    document.getElementById('calcCylBtn').addEventListener('click', calculateCylinder);
    document.getElementById('resetCylBtn').addEventListener('click', function() {
      setTimeout(calculateCylinder, 50);
    });

    window.addEventListener('DOMContentLoaded', calculateCylinder);
  </script>
</body>
</html>
"""

TOOL_2_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hydraulic Cylinder Force Calculator | Push & Pull Force, Load Acceleration</title>
  <meta name="description" content="Calculate net hydraulic cylinder push and pull force, seal friction breakout drag, backpressure opposing force, and dynamic load acceleration per ISO 3320 and NFPA standards.">
  <link rel="canonical" href="https://calchub.cloud/hydraulic-cylinder-force-calculator.html">
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
        "name": "Hydraulic Cylinder Force Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Fluid power force engineering tool computing net push and pull force accounting for seal friction breakout, backpressure derating, dynamic acceleration forces, and mechanical efficiency per ISO 3320.",
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
            "name": "How does return line backpressure affect hydraulic cylinder output force?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Return line backpressure acts on the opposing side of the piston, resisting cylinder movement. During extension: F_net = (P_supply * A_bore) - (P_back * A_annulus) - F_friction. In long return piping runs with restrictive proportional valves or counter-balance valves, backpressure can reduce net cylinder thrust by 10% to 25%."
            }
          },
          {
            "@type": "Question",
            "name": "What is the typical breakout seal friction in a hydraulic cylinder?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Hydraulic seals (piston cap seals and rod wiper/step seals) exert initial static breakout friction that is typically 2 to 3 times higher than dynamic running friction. For sizing calculations, mechanical seal efficiency is standardized between 90% and 95% (eta_m = 0.90 to 0.95), meaning 5% to 10% of theoretical force is consumed overcoming seal and bearing friction."
            }
          },
          {
            "@type": "Question",
            "name": "How do you calculate dynamic force required to accelerate a heavy load?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "By Newton's second law: F_total = F_static + F_acceleration = F_load + (m * a). If a 5,000 kg mass must accelerate to 0.25 m/s in 0.1 seconds, the acceleration is a = 2.5 m/s^2, requiring an additional dynamic inertial thrust of: F_acc = 5,000 kg * 2.5 m/s^2 = 12,500 N (12.5 kN) during the acceleration stroke."
            }
          },
          {
            "@type": "Question",
            "name": "What is the hydraulic force ratio between push and pull?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The force ratio is the ratio of pull force to push force: R_force = F_pull / F_push = (D_bore^2 - d_rod^2) / D_bore^2 = 1 - (d_rod / D_bore)^2. For standard ISO 6020 cylinders where the rod diameter is approximately 56% of bore diameter, the pull force is typically 65% to 70% of the push force."
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
      <span>Hydraulic Cylinder Force Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">ISO 3320 &amp; NFPA Fluid Power Standards</div>
          <h1 class="calc-title">Hydraulic Cylinder Force Calculator</h1>
          <p class="calc-tagline">Calculate net pushing and pulling force, return line backpressure losses, dynamic mass acceleration forces, and seal friction derating.</p>
        </header>

        <div class="tool-card">
          <form id="cylForceCalcForm">
            <div class="calc-grid">
              <div class="form-group">
                <label for="forceUnits">Engineering Units</label>
                <select id="forceUnits">
                  <option value="metric" selected>Metric (mm, bar, kN, kg)</option>
                  <option value="imperial">Imperial (in, psi, lbf, lbs)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="forceDirection">Actuation Direction</label>
                <select id="forceDirection">
                  <option value="both" selected>Analyze Both Push (Extend) & Pull (Retract)</option>
                  <option value="push">Push Only (Extension)</option>
                  <option value="pull">Pull Only (Retraction)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="boreD" id="lblForceBoreD">Cylinder Bore Diameter (D) [mm]</label>
                <input type="number" id="boreD" step="1" min="10" max="1500" value="100">
              </div>

              <div class="form-group">
                <label for="rodD" id="lblForceRodD">Piston Rod Diameter (d) [mm]</label>
                <input type="number" id="rodD" step="1" min="5" max="1400" value="56">
              </div>

              <div class="form-group">
                <label for="supplyPressure" id="lblSupplyPress">Supply Working Pressure (P_supply) [bar]</label>
                <input type="number" id="supplyPressure" step="5" min="5" max="1000" value="250">
              </div>

              <div class="form-group">
                <label for="backPressure" id="lblBackPress">Opposing Backpressure (P_back) [bar]</label>
                <input type="number" id="backPressure" step="1" min="0" max="200" value="15">
              </div>

              <div class="form-group">
                <label for="sealFrictionPct">Seal & Bearing Friction Drag Loss</label>
                <select id="sealFrictionPct">
                  <option value="0.05" selected>5% Loss (&eta;m = 95% - Standard Industrial)</option>
                  <option value="0.08">8% Loss (&eta;m = 92% - Cold Weather / High Viscosity)</option>
                  <option value="0.02">2% Loss (&eta;m = 98% - PTFE Low-Friction Aerospace)</option>
                  <option value="0.00">0% Loss (Theoretical Maximum)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="loadMass" id="lblLoadMass">Accelerated Load Mass (m) [kg]</label>
                <input type="number" id="loadMass" step="10" min="0" max="100000" value="2500">
              </div>

              <div class="form-group">
                <label for="accelTime">Acceleration Time to Full Speed [seconds]</label>
                <input type="number" id="accelTime" step="0.05" min="0.01" max="10" value="0.20">
              </div>

              <div class="form-group">
                <label for="targetVelocity" id="lblTargetVel">Target Steady-State Speed [m/s]</label>
                <input type="number" id="targetVelocity" step="0.05" min="0.01" max="5.0" value="0.25">
              </div>
            </div>

            <div class="calc-actions">
              <button type="button" id="calcForceBtn" class="btn btn-primary">Calculate Hydraulic Force</button>
              <button type="reset" id="resetForceBtn" class="btn btn-secondary">Reset Defaults</button>
            </div>
          </form>

          <div id="cylForceResultBox" class="results-container" style="display: none;">
            <h3>Net Cylinder Thrust & Opposing Resistance Results</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label">Net Effective Push Force (Extend)</span>
                <span id="resNetPush" class="result-value">-- kN</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Net Effective Pull Force (Retract)</span>
                <span id="resNetPull" class="result-value">-- kN</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Theoretical Push Force (Zero Loss)</span>
                <span id="resTheoPush" class="result-value">-- kN</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Theoretical Pull Force (Zero Loss)</span>
                <span id="resTheoPull" class="result-value">-- kN</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Backpressure Force Penalty (Push)</span>
                <span id="resBackLossPush" class="result-value">-- kN</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Dynamic Inertial Accel Force (F_acc)</span>
                <span id="resAccelForce" class="result-value">-- kN</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Force Ratio (Pull / Push)</span>
                <span id="resForceRatio" class="result-value">-- %</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Effective Pressure Loss to Friction</span>
                <span id="resFrictionLossBar" class="result-value">-- bar</span>
              </div>
            </div>
            <div id="cylForceNotesBox" style="margin-top: 1rem; color: #1e40af; background: #eff6ff; border: 1px solid #bfdbfe; padding: 0.75rem; border-radius: 6px;"></div>
          </div>
        </div>

        <article class="article-body">
          <h2>Precision Fluid Power Force Mechanics & Load Dynamics</h2>
          <p>Determining the real-world output force of a hydraulic cylinder requires moving beyond basic theoretical textbook formulas (\(F = P \times A\)). While the hydrostatic pressure generated by a hydraulic pump provides the primary driving energy, real-world machines endure substantial opposing forces, including <strong>seal breakout friction drag</strong>, <strong>return-line backpressure resistance</strong>, and <strong>inertial acceleration loads</strong> required to move heavy physical masses from rest.</p>

          <p>Underestimating these counter-acting parasitic loads leads to stalled machinery, sluggish cycle times, and violent hydraulic pressure spikes. Overcoming these real-world losses requires engineering hydraulic systems compliant with <strong>ISO 3320</strong> and <strong>NFPA Fluid Power Standards</strong>.</p>

          <h2>Net Effective Force Equations (Accounting for Losses)</h2>
          <p>When a cylinder extends, the cap-end chamber is supplied with pressurized oil, while fluid in the rod-end chamber must exhaust through the control valve, manifold, and return piping back to the reservoir. The net available pushing force (\(F_{\text{push, net}}\)) is:</p>

          <div class="formula-box">
            $$F_{\text{push, net}} = \eta_m \cdot P_{\text{supply}} \cdot A_{\text{bore}} - P_{\text{back}} \cdot A_{\text{annulus}} - F_{\text{acceleration}}$$
          </div>

          <p>Conversely, during retraction, pressurized oil enters the rod end while the cap end discharges to tank:</p>

          <div class="formula-box">
            $$F_{\text{pull, net}} = \eta_m \cdot P_{\text{supply}} \cdot A_{\text{annulus}} - P_{\text{back}} \cdot A_{\text{bore}} - F_{\text{acceleration}}$$
          </div>

          <p>Where the geometric areas are defined per standard circular geometry:</p>
          <ul>
            <li><strong>\(A_{\text{bore}} = \frac{\pi}{4} D_{\text{bore}}^2\)</strong>: Full cross-sectional area of the cylinder tube bore.</li>
            <li><strong>\(A_{\text{annulus}} = \frac{\pi}{4} (D_{\text{bore}}^2 - d_{\text{rod}}^2)\)</strong>: Net annular ring area on the rod side.</li>
            <li><strong>\(P_{\text{back}}\)</strong>: Return-line backpressure (typically 5 to 25 bar created by tank line filters, check valves, and counterbalance valves).</li>
            <li><strong>\(\eta_m\)</strong>: Mechanical seal efficiency (\(1 - \text{friction loss}\)).</li>
          </ul>

          <h2>Dynamic Mass Acceleration Forces (Newton's Second Law)</h2>
          <p>When a hydraulic cylinder actuates a stationary load (such as a 10,000 kg steel mold or a loaded excavator boom), initial static force alone cannot begin motion. An additional dynamic inertial thrust force (\(F_{\text{acc}}\)) is required during the acceleration phase:</p>

          <div class="formula-box">
            $$a = \frac{v_{\text{target}}}{t_{\text{accel}}} \quad \implies \quad F_{\text{acc}} = m \cdot a = m \cdot \left(\frac{v_{\text{target}}}{t_{\text{accel}}}\right)$$
          </div>

          <p>Where \(m\) is the combined mass of the load, mounting platen, and piston rod, \(v_{\text{target}}\) is steady-state linear speed, and \(t_{\text{accel}}\) is acceleration duration. If a high-speed cylinder is accelerated rapidly in less than 0.1 seconds, the dynamic inertial force can exceed the steady-state working load by more than 200%, frequently tripping relief valves if not accounted for during design.</p>

          <h2>Return Line Backpressure Derating Mechanics</h2>
          <p>A frequent error in fluid power engineering is assuming that the discharging end of a cylinder is at zero gauge pressure. In industrial reality, exhausting oil encounters flow resistance across directional control valve spools, proportional throttle orifices, long hard-lines, and return filter elements (typically creating 5 to 15 bar of backpressure). Furthermore, counterbalance valves (used to prevent overrunning gravitational loads on vertical presses) deliberately impose 20 to 50 bar of backpressure.</p>

          <p>During retraction, this backpressure acts across the <strong>full bore area</strong> (\(A_{\text{bore}}\)), producing a massive opposing resistive force that can deduct 15% to 30% from the cylinder's available pulling capacity.</p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Bore & Rod Size (mm)</th>
                <th>Bore Area (\(\text{cm}^2\))</th>
                <th>Annulus Area (\(\text{cm}^2\))</th>
                <th>Backpressure Force Penalty at 15 bar (kN)</th>
                <th>Net Push Force at 250 bar (kN)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>50 mm Bore / 28 mm Rod</td>
                <td>19.63</td>
                <td>13.48</td>
                <td>2.02 kN</td>
                <td>44.6 kN</td>
              </tr>
              <tr>
                <td>63 mm Bore / 36 mm Rod</td>
                <td>31.17</td>
                <td>20.99</td>
                <td>3.15 kN</td>
                <td>70.9 kN</td>
              </tr>
              <tr>
                <td>80 mm Bore / 45 mm Rod</td>
                <td>50.27</td>
                <td>34.36</td>
                <td>5.15 kN</td>
                <td>114.2 kN</td>
              </tr>
              <tr>
                <td>100 mm Bore / 56 mm Rod</td>
                <td>78.54</td>
                <td>53.91</td>
                <td>8.09 kN</td>
                <td>178.4 kN</td>
              </tr>
              <tr>
                <td>125 mm Bore / 70 mm Rod</td>
                <td>122.72</td>
                <td>84.23</td>
                <td>12.63 kN</td>
                <td>278.8 kN</td>
              </tr>
              <tr>
                <td>160 mm Bore / 90 mm Rod</td>
                <td>201.06</td>
                <td>137.44</td>
                <td>20.62 kN</td>
                <td>456.9 kN</td>
              </tr>
              <tr>
                <td>200 mm Bore / 110 mm Rod</td>
                <td>314.16</td>
                <td>219.13</td>
                <td>32.87 kN</td>
                <td>713.3 kN</td>
              </tr>
            </tbody>
          </table>

          <div class="worked-example-card">
            <h3>Step-by-Step Worked Case Study: Die Casting Injection Cylinder</h3>
            <p><strong>Design Scenario:</strong> An engineer is sizing the shot injection cylinder for an aluminum high-pressure die casting machine:</p>
            <ul>
              <li>Piston bore diameter: \(D_{\text{bore}} = 100\text{ mm}\) (\(0.100\text{ m}\)).</li>
              <li>Piston rod diameter: \(d_{\text{rod}} = 56\text{ mm}\) (\(0.056\text{ m}\)).</li>
              <li>Hydraulic supply pressure: \(P_{\text{supply}} = 250\text{ bar}\) (\(25.0\text{ MPa}\)).</li>
              <li>Return line backpressure: \(P_{\text{back}} = 15\text{ bar}\) (\(1.5\text{ MPa}\)).</li>
              <li>Mechanical seal friction loss: \(5\%\) (\(\eta_m = 0.95\)).</li>
              <li>Injection shot mass (piston rod + plunger + molten metal): \(m = 2,500\text{ kg}\).</li>
              <li>Target injection velocity: \(v = 0.25\text{ m/s}\), reached in \(t_{\text{acc}} = 0.20\text{ seconds}\).</li>
            </ul>

            <p><strong>Step 1: Compute effective bore and annular areas</strong></p>
            <div class="formula-box">
              $$A_{\text{bore}} = \frac{\pi}{4} (100)^2 = 7,853.98\text{ mm}^2 = 78.54\text{ cm}^2$$
              $$A_{\text{annulus}} = \frac{\pi}{4} \left[ (100)^2 - (56)^2 \right] = \frac{\pi}{4} [10000 - 3136] = 5,390.97\text{ mm}^2 = 53.91\text{ cm}^2$$
            </div>

            <p><strong>Step 2: Compute theoretical push force (zero loss)</strong></p>
            <div class="formula-box">
              $$F_{\text{theo, push}} = P_{\text{supply}} \cdot A_{\text{bore}} = (25.0\text{ N/mm}^2) \cdot 7,853.98\text{ mm}^2 = 196,350\text{ N} = 196.35\text{ kN}$$
            </div>

            <p><strong>Step 3: Calculate opposing backpressure force</strong></p>
            <div class="formula-box">
              $$F_{\text{back, push}} = P_{\text{back}} \cdot A_{\text{annulus}} = (1.5\text{ N/mm}^2) \cdot 5,390.97\text{ mm}^2 = 8,086\text{ N} = 8.09\text{ kN}$$
            </div>

            <p><strong>Step 4: Calculate dynamic load acceleration force (\(F_{\text{acc}}\))</strong></p>
            <div class="formula-box">
              $$a = \frac{v}{t_{\text{acc}}} = \frac{0.25\text{ m/s}}{0.20\text{ s}} = 1.25\text{ m/s}^2$$
              $$F_{\text{acc}} = m \cdot a = 2,500\text{ kg} \times 1.25\text{ m/s}^2 = 3,125\text{ N} = 3.13\text{ kN}$$
            </div>

            <p><strong>Step 5: Determine net effective push force</strong></p>
            <div class="formula-box">
              $$F_{\text{net, push}} = (0.95 \times 196.35\text{ kN}) - 8.09\text{ kN} - 3.13\text{ kN} = 186.53 - 11.22 = 175.31\text{ kN}$$
            </div>
            <p><strong>Engineering Conclusion:</strong> While the nominal catalog rating indicates 196.4 kN, real-world backpressure, dynamic acceleration, and seal friction derate available thrust to <strong>175.3 kN (17.9 metric tons)</strong>—an exact 10.7% real-world reduction.</p>
          </div>

          <h2>Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3>How does temperature affect hydraulic cylinder force?</h3>
            <p>Hydraulic fluid viscosity decreases exponentially with temperature. In cold weather (< 0&deg;C), thick oil creates massive viscous shear drag across seals and valve orifices, increasing backpressure and reducing net cylinder thrust by up to 20%. Conversely, at high temperatures (> 70&deg;C), internal leakage past worn piston seals increases, allowing pressurized oil to slip across the piston, causing pressure equalization and severe loss of holding force.</p>
          </div>

          <div class="faq-item">
            <h3>What is the difference between static holding force and dynamic operating force?</h3>
            <p>Dynamic force is the net thrust exerted while the piston is actively moving fluid through lines, subject to continuous fluid friction and backpressure. Static holding force occurs when the directional valve is closed (or a pilot-operated check valve locks fluid in the cylinder) at zero velocity. In static lockup, fluid flow is zero, meaning backpressure and line losses disappear, allowing the cylinder to hold loads up to full hydrostatic relief pressure.</p>
          </div>

          <div class="faq-item">
            <h3>Why does pressure intensification occur in hydraulic cylinders?</h3>
            <p>Pressure intensification occurs if the fluid discharge line from the rod end is accidentally blocked or restricted while the cap end is pressurized. Because the force balance requires \(P_1 A_1 = P_2 A_2\), blocking the smaller annular area forces its pressure to spike: \(P_{\text{rod}} = P_{\text{supply}} \times (A_{\text{bore}} / A_{\text{annulus}})\). For high area ratios, rod-end pressure can spike to 1.5 to 2.0 times supply pressure, frequently rupturing cylinder barrels or blowing out rod seals.</p>
          </div>

          <div class="faq-item">
            <h3>How do counterbalance valves affect cylinder pull force?</h3>
            <p>Counterbalance valves (overcenter valves) are installed on cylinders supporting suspended vertical loads to prevent uncontrolled falling. The valve remains closed until a pilot pressure from the opposite line unseats it. Setting the counterbalance valve too high increases parasitic backpressure during powered downward retraction, reducing available pulling force by the valve's cracking pressure setting (typically 20 to 50 bar).</p>
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
    const forceUnitsSelect = document.getElementById('forceUnits');
    const forceDirectionSelect = document.getElementById('forceDirection');
    const boreDInput = document.getElementById('boreD');
    const rodDInput = document.getElementById('rodD');
    const supplyPressureInput = document.getElementById('supplyPressure');
    const backPressureInput = document.getElementById('backPressure');
    const sealFrictionPctSelect = document.getElementById('sealFrictionPct');
    const loadMassInput = document.getElementById('loadMass');
    const accelTimeInput = document.getElementById('accelTime');
    const targetVelocityInput = document.getElementById('targetVelocity');

    const lblForceBoreD = document.getElementById('lblForceBoreD');
    const lblForceRodD = document.getElementById('lblForceRodD');
    const lblSupplyPress = document.getElementById('lblSupplyPress');
    const lblBackPress = document.getElementById('lblBackPress');
    const lblLoadMass = document.getElementById('lblLoadMass');
    const lblTargetVel = document.getElementById('lblTargetVel');

    const cylForceResultBox = document.getElementById('cylForceResultBox');
    const resNetPush = document.getElementById('resNetPush');
    const resNetPull = document.getElementById('resNetPull');
    const resTheoPush = document.getElementById('resTheoPush');
    const resTheoPull = document.getElementById('resTheoPull');
    const resBackLossPush = document.getElementById('resBackLossPush');
    const resAccelForce = document.getElementById('resAccelForce');
    const resForceRatio = document.getElementById('resForceRatio');
    const resFrictionLossBar = document.getElementById('resFrictionLossBar');
    const cylForceNotesBox = document.getElementById('cylForceNotesBox');

    forceUnitsSelect.addEventListener('change', function() {
      const isMetric = this.value === 'metric';
      if (isMetric) {
        lblForceBoreD.textContent = "Cylinder Bore Diameter (D) [mm]";
        lblForceRodD.textContent = "Piston Rod Diameter (d) [mm]";
        lblSupplyPress.textContent = "Supply Working Pressure (P_supply) [bar]";
        lblBackPress.textContent = "Opposing Backpressure (P_back) [bar]";
        lblLoadMass.textContent = "Accelerated Load Mass (m) [kg]";
        lblTargetVel.textContent = "Target Steady-State Speed [m/s]";
        boreDInput.value = 100;
        rodDInput.value = 56;
        supplyPressureInput.value = 250;
        backPressureInput.value = 15;
        loadMassInput.value = 2500;
        targetVelocityInput.value = 0.25;
      } else {
        lblForceBoreD.textContent = "Cylinder Bore Diameter (D) [in]";
        lblForceRodD.textContent = "Piston Rod Diameter (d) [in]";
        lblSupplyPress.textContent = "Supply Working Pressure (P_supply) [psi]";
        lblBackPress.textContent = "Opposing Backpressure (P_back) [psi]";
        lblLoadMass.textContent = "Accelerated Load Mass (m) [lbs]";
        lblTargetVel.textContent = "Target Steady-State Speed [in/s]";
        boreDInput.value = 4.0;
        rodDInput.value = 2.25;
        supplyPressureInput.value = 3500;
        backPressureInput.value = 200;
        loadMassInput.value = 5500;
        targetVelocityInput.value = 10.0;
      }
      calculateForce();
    });

    function calculateForce() {
      const isMetric = forceUnitsSelect.value === 'metric';
      const frictionRatio = parseFloat(sealFrictionPctSelect.value);
      const eta_m = 1.0 - frictionRatio;

      let D = parseFloat(boreDInput.value);
      let d = parseFloat(rodDInput.value);
      let P_sup = parseFloat(supplyPressureInput.value);
      let P_back = parseFloat(backPressureInput.value);
      let mass = parseFloat(loadMassInput.value);
      let t_acc = parseFloat(accelTimeInput.value);
      let v_tgt = parseFloat(targetVelocityInput.value);

      if (isNaN(D) || D <= 0) D = isMetric ? 100 : 4.0;
      if (isNaN(d) || d <= 0) d = isMetric ? 56 : 2.25;
      if (d >= D) d = D * 0.56;
      if (isNaN(P_sup) || P_sup <= 0) P_sup = isMetric ? 250 : 3500;
      if (isNaN(P_back) || P_back < 0) P_back = 0;
      if (isNaN(mass) || mass < 0) mass = 0;
      if (isNaN(t_acc) || t_acc <= 0) t_acc = 0.2;
      if (isNaN(v_tgt) || v_tgt < 0) v_tgt = 0;

      // Acceleration: a = v / t
      const accel = v_tgt / t_acc; // m/s^2 (metric) or in/s^2 (imperial)

      let F_acc_N = 0;
      let F_acc_disp = 0;
      let uForce = isMetric ? 'kN' : 'lbf';

      if (isMetric) {
        F_acc_N = mass * accel; // N
        F_acc_disp = F_acc_N / 1000; // kN
      } else {
        // mass in lbs -> mass_slugs = mass / 32.174
        // accel in in/s^2 -> ft/s^2 = accel / 12
        const accel_fts2 = accel / 12;
        const mass_slugs = mass / 32.174;
        const F_acc_lbf = mass_slugs * accel_fts2;
        F_acc_disp = F_acc_lbf;
      }

      let A_bore = 0;
      let A_rod = 0;
      let A_ann = 0;

      let F_theo_push = 0;
      let F_theo_pull = 0;
      let F_back_push = 0;
      let F_net_push = 0;
      let F_net_pull = 0;

      if (isMetric) {
        A_bore = (Math.PI / 4) * Math.pow(D, 2); // mm^2
        A_rod = (Math.PI / 4) * Math.pow(d, 2);
        A_ann = A_bore - A_rod;

        // Theoretical Force (N) = P_sup [bar] * 0.1 * A [mm^2]
        F_theo_push = (P_sup * 0.1 * A_bore) / 1000; // kN
        F_theo_pull = (P_sup * 0.1 * A_ann) / 1000; // kN

        // Backpressure loss during push (acting on annulus)
        F_back_push = (P_back * 0.1 * A_ann) / 1000; // kN

        // Backpressure loss during pull (acting on bore)
        const F_back_pull = (P_back * 0.1 * A_bore) / 1000; // kN

        // Net push
        F_net_push = Math.max(0, (F_theo_push * eta_m) - F_back_push - F_acc_disp);
        // Net pull
        F_net_pull = Math.max(0, (F_theo_pull * eta_m) - F_back_pull - F_acc_disp);

        resNetPush.textContent = F_net_push.toFixed(2) + " kN (" + (F_net_push / 9.80665).toFixed(1) + " t)";
        resNetPull.textContent = F_net_pull.toFixed(2) + " kN (" + (F_net_pull / 9.80665).toFixed(1) + " t)";
        resTheoPush.textContent = F_theo_push.toFixed(2) + " kN";
        resTheoPull.textContent = F_theo_pull.toFixed(2) + " kN";
        resBackLossPush.textContent = "-" + F_back_push.toFixed(2) + " kN";
        resAccelForce.textContent = F_acc_disp.toFixed(2) + " kN";
        resFrictionLossBar.textContent = (P_sup * frictionRatio).toFixed(1) + " bar";
      } else {
        A_bore = (Math.PI / 4) * Math.pow(D, 2); // in^2
        A_rod = (Math.PI / 4) * Math.pow(d, 2);
        A_ann = A_bore - A_rod;

        F_theo_push = P_sup * A_bore; // lbf
        F_theo_pull = P_sup * A_ann; // lbf

        F_back_push = P_back * A_ann;
        const F_back_pull = P_back * A_bore;

        F_net_push = Math.max(0, (F_theo_push * eta_m) - F_back_push - F_acc_disp);
        F_net_pull = Math.max(0, (F_theo_pull * eta_m) - F_back_pull - F_acc_disp);

        resNetPush.textContent = Math.round(F_net_push).toLocaleString() + " lbf (" + (F_net_push / 2000).toFixed(1) + " tons)";
        resNetPull.textContent = Math.round(F_net_pull).toLocaleString() + " lbf (" + (F_net_pull / 2000).toFixed(1) + " tons)";
        resTheoPush.textContent = Math.round(F_theo_push).toLocaleString() + " lbf";
        resTheoPull.textContent = Math.round(F_theo_pull).toLocaleString() + " lbf";
        resBackLossPush.textContent = "-" + Math.round(F_back_push).toLocaleString() + " lbf";
        resAccelForce.textContent = Math.round(F_acc_disp).toLocaleString() + " lbf";
        resFrictionLossBar.textContent = Math.round(P_sup * frictionRatio) + " psi";
      }

      const forceRatio = (F_theo_pull / F_theo_push) * 100;
      resForceRatio.textContent = forceRatio.toFixed(1) + "%";

      let notes = `<strong>Force Balance Analysis:</strong> At <strong>${P_sup} ${isMetric ? 'bar' : 'psi'}</strong>, net push force is <strong>${isMetric ? F_net_push.toFixed(1) + ' kN' : Math.round(F_net_push).toLocaleString() + ' lbf'}</strong> after deducting backpressure (-${isMetric ? F_back_push.toFixed(1) + ' kN' : Math.round(F_back_push).toLocaleString() + ' lbf'}) and acceleration (-${isMetric ? F_acc_disp.toFixed(1) + ' kN' : Math.round(F_acc_disp).toLocaleString() + ' lbf'}).`;
      cylForceNotesBox.innerHTML = notes;

      cylForceResultBox.style.display = 'block';
    }

    document.getElementById('calcForceBtn').addEventListener('click', calculateForce);
    document.getElementById('resetForceBtn').addEventListener('click', function() {
      setTimeout(calculateForce, 50);
    });

    window.addEventListener('DOMContentLoaded', calculateForce);
  </script>
</body>
</html>
"""

def main():
    target_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    file1 = os.path.join(target_dir, "hydraulic-cylinder-calculator.html")
    with open(file1, "w", encoding="utf-8") as f:
        f.write(TOOL_1_HTML)
    print(f"[PASS] hydraulic-cylinder-calculator.html generated successfully!")

    file2 = os.path.join(target_dir, "hydraulic-cylinder-force-calculator.html")
    with open(file2, "w", encoding="utf-8") as f:
        f.write(TOOL_2_HTML)
    print(f"[PASS] hydraulic-cylinder-force-calculator.html generated successfully!")

if __name__ == "__main__":
    main()
