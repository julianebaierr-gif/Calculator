# -*- coding: utf-8 -*-
"""
Generator for Batch 32 - Part 4:
7. pressure-calculator.html
8. speed-calculator.html
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 7. pressure-calculator.html
HTML_PRESSURE = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pressure Calculator - Fluid, Mechanical &amp; Hydrostatic Pressure</title>
  <meta name="description" content="Calculate pressure from force and area (P = F/A) or hydrostatic fluid depth (P = ρgh). Convert between Pa, bar, psi, atm, and mmHg with formulas and engineering case studies.">
  <link rel="canonical" href="https://calchub.org/pressure-calculator.html">
  <meta property="og:title" content="Pressure Calculator - Fluid &amp; Mechanical Pressure Solver">
  <meta property="og:description" content="Free engineering pressure calculator. Calculate mechanical contact pressure, hydrostatic liquid head, gauge vs absolute pressure, and convert across 10 global units.">
  <meta property="og:url" content="https://calchub.org/pressure-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Pressure Calculator - Mechanical &amp; Hydrostatic Tool">
  <meta name="twitter:description" content="Solve P = F/A and P = ρgh with multi-unit conversions (psi, bar, kPa, atm, mmHg). Includes step-by-step proofs and engineering case studies.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Pressure Calculator",
    "url": "https://calchub.org/pressure-calculator.html",
    "description": "Calculates mechanical pressure, hydrostatic liquid head pressure, and absolute vs gauge pressure across metric and imperial engineering units.",
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
        "name": "What is the primary equation for mechanical pressure?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Mechanical pressure is defined as perpendicular compressive force distributed over an area: P = F / A, where P is pressure in Pascals (N/m^2), F is normal force in Newtons, and A is surface contact area in square meters."
        }
      },
      {
        "@type": "Question",
        "name": "How is hydrostatic pressure calculated at a specific liquid depth?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Hydrostatic pressure at depth h is computed using P = rho * g * h, where rho is fluid density (kg/m^3), g is gravitational acceleration (9.80665 m/s^2), and h is fluid column height in meters. For total absolute pressure, atmospheric surface pressure is added: P_abs = P_atm + rho * g * h."
        }
      },
      {
        "@type": "Question",
        "name": "What is the difference between gauge pressure and absolute pressure?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Gauge pressure measures pressure relative to ambient atmospheric pressure (a tire gauge reading zero at 1 atm). Absolute pressure measures pressure relative to a perfect vacuum: P_absolute = P_gauge + P_atmospheric."
        }
      },
      {
        "@type": "Question",
        "name": "How many Pascals are in one atmosphere and one bar?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "One standard atmosphere (1 atm) equals exactly 101,325 Pascals (101.325 kPa or 14.696 psi). One bar equals exactly 100,000 Pascals (100 kPa or 0.98692 atm)."
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

  <main class="calculator-container">
    <div class="calculator-header">
      <div class="calc-icon" aria-hidden="true">&#9881;</div>
      <h1>Pressure Calculator</h1>
      <p class="calc-description">Compute mechanical contact pressure (\(P = F/A\)), hydrostatic fluid column depth (\(P = \rho gh\)), and gauge vs absolute pressure across multi-unit engineering systems.</p>
    </div>

    <div class="calculator-body">
      <div class="input-group">
        <label for="pressure-mode">Pressure Model</label>
        <select id="pressure-mode" class="form-control" onchange="switchPressureMode()">
          <option value="mechanical" selected>Mechanical Pressure: Force over Area (\(P = F / A\))</option>
          <option value="hydrostatic">Hydrostatic Fluid Column: Depth &amp; Density (\(P = \rho g h\))</option>
          <option value="gauge-abs">Gauge &harr; Absolute Atmospheric Conversion</option>
        </select>
      </div>

      <!-- Panel: Mechanical P = F / A -->
      <div id="panel-mechanical">
        <div class="input-grid">
          <div class="input-group">
            <label for="mech-force">Normal Applied Force (\(F\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="mech-force" class="form-control" value="5000" step="any" min="0" style="flex: 2;">
              <select id="unit-force" class="form-control" style="flex: 1;" onchange="calculatePressure()">
                <option value="N" selected>N</option>
                <option value="kN">kN</option>
                <option value="lbf">lbf</option>
                <option value="kgf">kgf</option>
              </select>
            </div>
          </div>

          <div class="input-group">
            <label for="mech-area">Contact Surface Area (\(A\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="mech-area" class="form-control" value="0.025" step="any" min="0" style="flex: 2;">
              <select id="unit-area" class="form-control" style="flex: 1;" onchange="calculatePressure()">
                <option value="m2" selected>m²</option>
                <option value="cm2">cm²</option>
                <option value="mm2">mm²</option>
                <option value="in2">in²</option>
                <option value="ft2">ft²</option>
              </select>
            </div>
          </div>
        </div>
      </div>

      <!-- Panel: Hydrostatic P = rho * g * h -->
      <div id="panel-hydrostatic" style="display: none;">
        <div class="input-grid">
          <div class="input-group">
            <label for="hydro-fluid">Preset Liquid</label>
            <select id="hydro-fluid" class="form-control" onchange="loadFluidPreset()">
              <option value="1000" selected>Fresh Water (1,000 kg/m³)</option>
              <option value="1025">Seawater (1,025 kg/m³)</option>
              <option value="13546">Mercury (13,546 kg/m³)</option>
              <option value="850">Hydraulic Oil (850 kg/m³)</option>
              <option value="789">Ethanol (789 kg/m³)</option>
              <option value="custom">-- Custom Density --</option>
            </select>
          </div>

          <div class="input-group">
            <label for="hydro-dens">Fluid Density (\(\rho\)) [kg/m³]</label>
            <input type="number" id="hydro-dens" class="form-control" value="1000" step="any" min="0">
          </div>
        </div>

        <div class="input-grid">
          <div class="input-group">
            <label for="hydro-depth">Column Depth / Head (\(h\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="hydro-depth" class="form-control" value="20" step="any" min="0" style="flex: 2;">
              <select id="unit-depth" class="form-control" style="flex: 1;" onchange="calculatePressure()">
                <option value="m" selected>m</option>
                <option value="cm">cm</option>
                <option value="ft">ft</option>
                <option value="in">in</option>
              </select>
            </div>
          </div>

          <div class="input-group">
            <label for="hydro-gravity">Gravitational Acceleration (\(g\))</label>
            <select id="hydro-gravity" class="form-control" onchange="calculatePressure()">
              <option value="9.80665" selected>Standard Earth (9.80665 m/s²)</option>
              <option value="9.81">Approx. Earth (9.81 m/s²)</option>
              <option value="1.62">Moon (1.62 m/s²)</option>
              <option value="3.71">Mars (3.71 m/s²)</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Panel: Gauge vs Absolute -->
      <div id="panel-gauge-abs" style="display: none;">
        <div class="input-grid">
          <div class="input-group">
            <label for="conv-direction">Conversion Mode</label>
            <select id="conv-direction" class="form-control" onchange="calculatePressure()">
              <option value="gauge-to-abs" selected>Gauge Pressure &rarr; Absolute Pressure</option>
              <option value="abs-to-gauge">Absolute Pressure &rarr; Gauge Pressure</option>
            </select>
          </div>

          <div class="input-group">
            <label for="conv-val">Input Pressure Reading</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="conv-val" class="form-control" value="32.0" step="any" style="flex: 2;">
              <select id="conv-unit" class="form-control" style="flex: 1;" onchange="calculatePressure()">
                <option value="psi" selected>psi</option>
                <option value="bar">bar</option>
                <option value="kPa">kPa</option>
                <option value="atm">atm</option>
              </select>
            </div>
          </div>
        </div>

        <div class="input-group">
          <label for="conv-patm">Ambient Atmospheric Pressure (\(P_{\text{atm}}\))</label>
          <div style="display: flex; gap: 0.5rem;">
            <input type="number" id="conv-patm" class="form-control" value="14.696" step="any" min="0" style="flex: 2;">
            <span style="display: flex; align-items: center; padding: 0 0.5rem; background: var(--bg-secondary, #e9ecef); border-radius: 4px; font-size: 0.85rem;" id="lbl-patm-unit">psi (1.0 atm standard)</span>
          </div>
        </div>
      </div>

      <div class="btn-group">
        <button type="button" class="btn btn-primary" onclick="calculatePressure()">Calculate Pressure</button>
        <button type="button" class="btn btn-secondary" onclick="resetPressure()">Reset Defaults</button>
      </div>

      <!-- Results Display Grid -->
      <div class="results-grid" style="margin-top: 1.5rem;">
        <div class="result-card primary-result">
          <div class="result-label">Calculated Pressure (SI Base)</div>
          <div class="result-value" id="res-pa">200.00 kPa</div>
          <div class="result-subtext" id="res-pa-exact">200,000.00 Pascals (N/m²)</div>
        </div>

        <div class="result-card">
          <div class="result-label">Engineering Bar</div>
          <div class="result-value" id="res-bar">2.000 bar</div>
          <div class="result-subtext">2,000.0 mbar</div>
        </div>

        <div class="result-card">
          <div class="result-label">Imperial PSI (Pounds/sq.in)</div>
          <div class="result-value" id="res-psi">29.008 psi</div>
          <div class="result-subtext">4,177.1 lb/ft²</div>
        </div>

        <div class="result-card">
          <div class="result-label">Standard Atmospheres</div>
          <div class="result-value" id="res-atm">1.974 atm</div>
          <div class="result-subtext" id="res-mmhg">1,500.1 mmHg / Torr</div>
        </div>
      </div>

      <!-- Equivalent Pressure Table Card -->
      <div class="info-card" style="margin-top: 1.5rem;">
        <h3>Comprehensive Multi-System Pressure Equivalencies</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 0.75rem; margin-top: 0.5rem;">
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">Pascals (Pa)</div>
            <strong id="eq-pa">200,000 Pa</strong>
          </div>
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">Megapascals (MPa)</div>
            <strong id="eq-mpa">0.200 MPa</strong>
          </div>
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">Kilopounds / sq. in (ksi)</div>
            <strong id="eq-ksi">0.029 ksi</strong>
          </div>
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">Water Column (mH₂O)</div>
            <strong id="eq-mh2o">20.39 mH₂O</strong>
          </div>
        </div>
      </div>

      <!-- Step-by-step Math Breakdown Card -->
      <div class="info-card" style="margin-top: 1.5rem;">
        <h3>Step-by-Step Computational Breakdown</h3>
        <pre id="res-steps" style="white-space: pre-wrap; font-family: monospace; background: var(--bg-secondary, #f8f9fa); padding: 1rem; border-radius: 6px; font-size: 0.9rem; line-height: 1.5; color: var(--text-primary, #212529);"></pre>
      </div>
    </div>

    <!-- Article Content: 1000+ Words Clinical / Engineering Deep Dive -->
    <article class="article-body">
      <h2>The Physical Foundations of Mechanical and Fluid Pressure</h2>
      <p>
        In continuum mechanics, fluid dynamics, and thermodynamics, <strong>pressure</strong> (\(P\)) is defined as the magnitude of normal compressive force acting per unit area across an infinitesimal surface boundary. Unlike force, which is a vector possessing both magnitude and spatial direction, pressure inside a static fluid is an isotropic scalar state variable: it acts uniformly in all three-dimensional orientations perpendicular to any bounding surface with which it comes into contact.
      </p>
      <p>
        Across civil engineering, mechanical design, aerospace propulsion, and clinical physiology, pressure governs fundamental phenomena. Structural engineers analyze foundation bearing pressures to avert catastrophic structural shearing; hydraulic engineers harness Pascal's principle to multiply mechanical forces in excavators and braking systems; meteorologists monitor barometric pressure gradients to forecast storm systems; and biomedical clinicians assess systemic arterial pressures to evaluate vascular resistance and cardiac workload.
      </p>

      <h2>Mathematical Formulations and Governing Laws</h2>

      <h3>1. Mechanical Contact Pressure</h3>
      <p>
        For a solid body exerting an evenly distributed perpendicular load onto a flat supporting plane, the fundamental mechanical equation is:
      </p>
      $$P = \frac{F_{\perp}}{A}$$
      <p>
        Where:
      </p>
      <ul>
        <li>\(P\) is the contact pressure in Pascals (\(\text{Pa} = \text{N/m}^2\)).</li>
        <li>\(F_{\perp}\) is the normal compressive force acting perpendicular to the contact interface in Newtons (\(\text{N}\)).</li>
        <li>\(A\) is the cross-sectional contact surface area in square meters (\(\text{m}^2\)).</li>
      </ul>
      <p>
        This relation demonstrates that pressure is inversely proportional to contact area: concentrating a constant force over a smaller surface area produces exponentially magnified local stresses, which is the foundational principle underlying cutting blades, nails, and hydraulic punches.
      </p>

      <h3>2. Hydrostatic Fluid Pressure and Liquid Head</h3>
      <p>
        Inside a static, incompressible liquid subjected to uniform gravitational acceleration, pressure escalates linearly with increasing submersion depth due to the cumulative gravitational weight of the overlying fluid column:
      </p>
      $$P_{\text{hydrostatic}} = \rho \times g \times h$$
      <p>
        Where:
      </p>
      <ul>
        <li>\(\rho\) is the mass density of the liquid in kilograms per cubic meter (\(\text{kg/m}^3\)).</li>
        <li>\(g\) is local gravitational acceleration (\(9.80665\text{ m/s}^2\) on Earth).</li>
        <li>\(h\) is the vertical column depth or hydraulic head measured downward from the fluid's free surface in meters (\(\text{m}\)).</li>
      </ul>
      <p>
        To determine the <strong>total absolute pressure</strong> (\(P_{\text{abs}}\)) acting upon a submerged body (such as a submarine hull or deep-sea scuba diver), ambient atmospheric pressure acting upon the liquid's free surface must be incorporated:
      </p>
      $$P_{\text{abs}} = P_{\text{atm}} + \rho g h$$

      <h3>3. Gauge Pressure vs. Absolute Pressure vs. Vacuum</h3>
      <p>
        Pressure measurement instrumentation utilizes two distinct reference baselines:
      </p>
      <ul>
        <li><strong>Absolute Pressure (\(P_{\text{abs}}\)):</strong> Pressure measured relative to a perfect absolute vacuum (zero pressure). Absolute pressure cannot assume negative values.</li>
        <li><strong>Gauge Pressure (\(P_{\text{gauge}}\)):</strong> Pressure measured relative to local ambient atmospheric pressure (\(P_{\text{atm}} \approx 101.325\text{ kPa} = 14.696\text{ psi}\)). When a tire pressure gauge reads \(32.0\text{ psi}\), the internal absolute pressure is actually \(32.0 + 14.7 = 46.7\text{ psi}\).</li>
        <li><strong>Vacuum Pressure (\(P_{\text{vac}}\)):</strong> The depression below ambient atmospheric pressure, defined mathematically as \(P_{\text{vac}} = P_{\text{atm}} - P_{\text{abs}}\).</li>
      </ul>
      $$P_{\text{abs}} = P_{\text{gauge}} + P_{\text{atm}}$$

      <h2>International Pressure Units and Exact Conversion Constants</h2>
      <p>
        Because pressure has historically been measured using liquid manometers (mercury and water columns), imperial deadweight testers, and metric SI standards, modern engineering demands conversions across diverse unit systems.
      </p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Unit Name</th>
            <th>Symbol</th>
            <th>Value in Pascals (Pa)</th>
            <th>Value in Bar</th>
            <th>Value in PSI</th>
            <th>Primary Engineering Application</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Pascal (SI Derived)</td>
            <td>Pa</td>
            <td>1.0 (Exact)</td>
            <td>\(1.0 \times 10^{-5}\)</td>
            <td>\(1.45038 \times 10^{-4}\)</td>
            <td>Acoustic sound waves, cleanroom differentials</td>
          </tr>
          <tr>
            <td>Kilopascal</td>
            <td>kPa</td>
            <td>1,000</td>
            <td>0.01</td>
            <td>0.145038</td>
            <td>HVAC ductwork, civil engineering soil mechanics</td>
          </tr>
          <tr>
            <td>Megapascal</td>
            <td>MPa</td>
            <td>1,000,000</td>
            <td>10.0</td>
            <td>145.038</td>
            <td>Structural steel yield stress, concrete strength</td>
          </tr>
          <tr>
            <td>Bar</td>
            <td>bar</td>
            <td>100,000</td>
            <td>1.0 (Exact)</td>
            <td>14.5038</td>
            <td>Industrial hydraulics, scuba diving tanks</td>
          </tr>
          <tr>
            <td>Millibar</td>
            <td>mbar / hPa</td>
            <td>100</td>
            <td>0.001</td>
            <td>0.014504</td>
            <td>Meteorological weather forecasting, aviation altimeters</td>
          </tr>
          <tr>
            <td>Pound per square inch</td>
            <td>psi (\(\text{lbf/in}^2\))</td>
            <td>6,894.757</td>
            <td>0.068948</td>
            <td>1.0 (Exact)</td>
            <td>Automotive tire pressure, American gas pipelines</td>
          </tr>
          <tr>
            <td>Standard Atmosphere</td>
            <td>atm</td>
            <td>101,325 (Exact)</td>
            <td>1.01325</td>
            <td>14.69595</td>
            <td>Thermodynamic standard conditions, diving depth</td>
          </tr>
          <tr>
            <td>Millimeter of Mercury</td>
            <td>mmHg / Torr</td>
            <td>133.3224</td>
            <td>0.001333</td>
            <td>0.019337</td>
            <td>Clinical blood pressure, laboratory high vacuum</td>
          </tr>
          <tr>
            <td>Meter of Water Column</td>
            <td>\(\text{mH}_2\text{O}\)</td>
            <td>9,806.65</td>
            <td>0.098066</td>
            <td>1.42233</td>
            <td>Municipal water distribution, civil sump pumps</td>
          </tr>
          <tr>
            <td>Inch of Mercury</td>
            <td>inHg</td>
            <td>3,386.389</td>
            <td>0.033864</td>
            <td>0.491154</td>
            <td>Aviation barometric altimeter settings (Kollsman)</td>
          </tr>
        </tbody>
      </table>

      <h2>Practical Real-World Engineering Case Studies</h2>

      <div class="worked-example-card">
        <h3>Case Study 1: Hydraulic Press Force Multiplication (Pascal's Principle)</h3>
        <p><strong>Scenario:</strong> An automotive shop hydraulic lift utilizes two connected fluid cylinders. The input piston has diameter \(d_1 = 5.0\text{ cm}\) (\(r_1 = 0.025\text{ m}\)), while the output lifting piston has diameter \(d_2 = 30.0\text{ cm}\) (\(r_2 = 0.15\text{ m}\)). A technician applies a foot pedal force of \(F_1 = 250\text{ N}\) to the input cylinder.</p>
        <p><strong>Objective:</strong> Calculate hydraulic line pressure and determine the maximum vehicle mass the lift can elevate in equilibrium.</p>
        <div class="step-solution">
          <p><strong>1. Input Piston Contact Area &amp; System Pressure:</strong></p>
          $$A_1 = \pi r_1^2 = \pi (0.025\text{ m})^2 \approx 0.0019635\text{ m}^2$$
          $$P = \frac{F_1}{A_1} = \frac{250\text{ N}}{0.0019635\text{ m}^2} \approx 127,324\text{ Pa} \approx 1.273\text{ bar} \ (18.47\text{ psi})$$
          <p><strong>2. Output Piston Area &amp; Lift Force:</strong></p>
          <p>Per Pascal's principle, fluid pressure transmits undiminished throughout the enclosed fluid: \(P_2 = P_1\):</p>
          $$A_2 = \pi r_2^2 = \pi (0.15\text{ m})^2 \approx 0.070686\text{ m}^2$$
          $$F_2 = P \times A_2 = 127,324\text{ Pa} \times 0.070686\text{ m}^2 = 9,000\text{ N}$$
          <p>Force multiplication ratio is \(\frac{A_2}{A_1} = \left(\frac{30}{5}\right)^2 = 36.0\times\). Maximum suspended mass:</p>
          $$m_{\text{vehicle}} = \frac{F_2}{g} = \frac{9,000\text{ N}}{9.80665\text{ m/s}^2} \approx 917.7\text{ kg}$$
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Marine Deep-Sea Submersible Hydrostatic Hull Stress</h3>
        <p><strong>Scenario:</strong> A deep-sea research submersible descends into the Mariana Trench to an extreme depth of \(h = 8,500\text{ m}\). Average seawater density across the deep vertical water column is \(\rho = 1,040\text{ kg/m}^3\). Ambient surface atmospheric pressure is \(P_{\text{atm}} = 101,325\text{ Pa}\).</p>
        <p><strong>Objective:</strong> Calculate total absolute pressure acting on the submersible titanium viewport, and compute total normal force across a circular viewing port of diameter \(d = 20.0\text{ cm}\).</p>
        <div class="step-solution">
          <p><strong>1. Hydrostatic Gauge Pressure:</strong></p>
          $$P_{\text{gauge}} = \rho g h = 1,040\text{ kg/m}^3 \times 9.80665\text{ m/s}^2 \times 8,500\text{ m} = 86,690,786\text{ Pa} \approx 86.69\text{ MPa}$$
          <p><strong>2. Total Absolute Pressure:</strong></p>
          $$P_{\text{abs}} = P_{\text{atm}} + P_{\text{gauge}} = 101,325\text{ Pa} + 86,690,786\text{ Pa} = 86,792,111\text{ Pa} \approx 867.92\text{ bar} \ (12,588.1\text{ psi})$$
          <p><strong>3. Viewport Compressive Force:</strong></p>
          $$A_{\text{port}} = \pi r^2 = \pi (0.10\text{ m})^2 = 0.031416\text{ m}^2$$
          $$F_{\text{net}} \approx P_{\text{abs}} \times A_{\text{port}} = 86,792,111\text{ Pa} \times 0.031416\text{ m}^2 \approx 2,726,660\text{ N} \text{ (2,726.7 kN)}$$
          <p>This immense compressive load is equivalent to supporting the gravitational weight of approximately 278 metric tons on a window no larger than a dinner plate!</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 3: Structural Civil Engineering &ndash; Foundation Bearing Pressure</h3>
        <p><strong>Scenario:</strong> A reinforced concrete multi-story column carries a combined dead and live axial compressive building load of \(F = 4,800\text{ kN}\) (\(4,800,000\text{ N}\)). Geotechnical soil analysis determines the safe allowable bearing capacity of the underlying compacted clay soil is \(q_{\text{allow}} = 220\text{ kPa}\) (\(220,000\text{ N/m}^2\)).</p>
        <p><strong>Objective:</strong> Determine the minimum required square footing dimension \(B \times B\) to avoid soil shear failure and differential foundation settlement.</p>
        <div class="step-solution">
          <p><strong>1. Minimum Footing Area Requirement:</strong></p>
          $$A_{\text{req}} = \frac{F}{q_{\text{allow}}} = \frac{4,800,000\text{ N}}{220,000\text{ N/m}^2} \approx 21.818\text{ m}^2$$
          <p><strong>2. Side Dimension for Square Footing:</strong></p>
          $$B = \sqrt{A_{\text{req}}} = \sqrt{21.818\text{ m}^2} \approx 4.671\text{ m}$$
          <p>Rounding up to standard structural construction specifications, the civil engineer specifies a \(4.70\text{ m} \times 4.70\text{ m}\) square reinforced concrete pad footing, producing an operating soil pressure of:</p>
          $$P_{\text{actual}} = \frac{4,800,000\text{ N}}{(4.70\text{ m})^2} = \frac{4,800,000}{22.09} \approx 217.29\text{ kPa} \le 220\text{ kPa (PASS)}$$
        </div>
      </div>

      <h2>Barometric Altitude Lapse Rate in Atmospheric Physics</h2>
      <p>
        In compressible atmospheric gas columns, air density decreases with altitude. For the lower troposphere (up to \(11,000\text{ m}\)), the barometric formula establishes pressure as an exponential decay function:
      </p>
      $$P(h) = P_0 \left(1 - \frac{L \cdot h}{T_0}\right)^{\frac{g \cdot M}{R \cdot L}}$$
      <p>
        Where \(P_0 = 101,325\text{ Pa}\) is sea-level pressure, \(L = 0.0065\text{ K/m}\) is the standard temperature lapse rate, \(T_0 = 288.15\text{ K}\) (15°C), \(M = 0.0289644\text{ kg/mol}\) is molar mass of dry air, and \(R = 8.31446\text{ J/(mol}\cdot\text{K)}\). At Mount Everest's summit (\(8,848\text{ m}\)), ambient atmospheric pressure plummets to approximately \(33.7\text{ kPa}\) (roughly 33% of sea level), severely reducing arterial oxygen saturation.
      </p>

      <h2>Frequently Asked Questions</h2>
      <div class="faq-accordion">
        <details class="faq-item">
          <summary class="faq-question">Why does a high heel exert more pressure on a floor than an elephant's foot?</summary>
          <div class="faq-answer">
            <p>An adult elephant weighs roughly 5,000 kg (50,000 N) distributed across four large flat feet with a combined area of about 0.8 m², producing a modest ground pressure of approximately 62.5 kPa. A 60 kg person (600 N) momentarily balancing on a stilettos heel with a tiny contact area of 0.5 cm² (0.00005 m²) exerts a staggering contact pressure of 12,000 kPa (12 MPa)—nearly 200 times greater than the elephant's footprint! Pressure depends equally on area as on force.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">How does water depth relate to pressure in scuba diving?</summary>
          <div class="faq-answer">
            <p>Because seawater has a density of ~1,025 kg/m³, every 10 meters (33 feet) of seawater depth adds approximately 1.0 atmosphere (101.3 kPa or 14.7 psi) of hydrostatic pressure. At sea level surface, ambient pressure is 1 atm; at 10 meters depth it is 2 atm; at 20 meters it is 3 atm; and at 30 meters it reaches 4 atm absolute pressure.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">What is the distinction between psia and psig?</summary>
          <div class="faq-answer">
            <p>The abbreviation <strong>psia</strong> denotes <em>pounds per square inch absolute</em> (measured relative to total vacuum), whereas <strong>psig</strong> denotes <em>pounds per square inch gauge</em> (measured relative to ambient atmospheric pressure). Standard ambient sea level pressure is 14.7 psia, which corresponds to exactly 0 psig.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">Why is blood pressure clinically measured in millimeters of mercury (mmHg)?</summary>
          <div class="faq-answer">
            <p>Historical medical sphygmomanometers directly balanced vascular pressure against the physical vertical height of a column of dense liquid mercury. A standard healthy adult blood pressure reading of 120/80 mmHg represents peak systolic pressure sufficient to elevate liquid mercury 120 millimeters (16.0 kPa) above atmospheric pressure, and resting diastolic pressure supporting 80 millimeters (10.7 kPa).</p>
          </div>
        </details>
      </div>

      <!-- Cross-Disciplinary Internal Links -->
      <div class="related-calculators" style="margin-top: 2rem; padding: 1.5rem; background: var(--bg-secondary, #f8f9fa); border-radius: 8px;">
        <h3>Related Engineering &amp; Physics Calculators</h3>
        <ul style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.75rem; list-style: none; padding: 0;">
          <li><a href="density-calculator.html">&rarr; Density &amp; Buoyancy Solver</a></li>
          <li><a href="force-converter.html">&rarr; Force &amp; Newton's Second Law Solver</a></li>
          <li><a href="speed-calculator.html">&rarr; Speed &amp; Kinematics Calculator</a></li>
          <li><a href="volume-calculator.html">&rarr; Volume Calculator (3D Solids)</a></li>
          <li><a href="scientific-notation-calculator.html">&rarr; Scientific Notation Calculator</a></li>
        </ul>
      </div>
    </article>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-col">
        <h4>CalcHub</h4>
        <p>Comprehensive mathematical, statistical, and engineering calculation tools.</p>
      </div>
      <div class="footer-col">
        <h4>Discipline Hubs</h4>
        <ul class="footer-links">
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="math.html">Mathematics</a></li>
          <li><a href="converter.html">Unit Converters</a></li>
          <li><a href="engineering.html">Electrical &amp; Engineering</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 CalcHub. All rights reserved. Peer-reviewed computational algorithms.</p>
    </div>
  </footer>

  <script>
    var FORCE_FACTORS = {
      'N': 1.0,
      'kN': 1000.0,
      'lbf': 4.448221615,
      'kgf': 9.80665
    };

    var AREA_FACTORS = {
      'm2': 1.0,
      'cm2': 0.0001,
      'mm2': 0.000001,
      'in2': 0.00064516,
      'ft2': 0.09290304
    };

    var DEPTH_FACTORS = {
      'm': 1.0,
      'cm': 0.01,
      'ft': 0.3048,
      'in': 0.0254
    };

    var PRES_FACTORS_TO_PA = {
      'psi': 6894.75729,
      'bar': 100000.0,
      'kPa': 1000.0,
      'atm': 101325.0
    };

    function switchPressureMode() {
      var mode = document.getElementById('pressure-mode').value;
      document.getElementById('panel-mechanical').style.display = (mode === 'mechanical') ? 'block' : 'none';
      document.getElementById('panel-hydrostatic').style.display = (mode === 'hydrostatic') ? 'block' : 'none';
      document.getElementById('panel-gauge-abs').style.display = (mode === 'gauge-abs') ? 'block' : 'none';
      calculatePressure();
    }

    function loadFluidPreset() {
      var val = document.getElementById('hydro-fluid').value;
      if (val !== 'custom') {
        document.getElementById('hydro-dens').value = val;
        calculatePressure();
      }
    }

    function calculatePressure() {
      var mode = document.getElementById('pressure-mode').value;
      var pa = 0;
      var steps = "";

      if (mode === 'mechanical') {
        var fVal = parseFloat(document.getElementById('mech-force').value);
        var fUnit = document.getElementById('unit-force').value;
        var aVal = parseFloat(document.getElementById('mech-area').value);
        var aUnit = document.getElementById('unit-area').value;

        if (isNaN(fVal) || isNaN(aVal) || fVal < 0 || aVal <= 0) {
          showError("Force must be non-negative and contact area must be strictly positive.");
          return;
        }

        var fN = fVal * FORCE_FACTORS[fUnit];
        var aM2 = aVal * AREA_FACTORS[aUnit];
        pa = fN / aM2;

        steps = "Mode: Mechanical Contact Pressure (P = F / A)\n" +
                "Inputs: Force F = " + fVal + " " + fUnit + ", Area A = " + aVal + " " + aUnit + "\n\n" +
                "1. Convert Force to SI: F = " + fN.toFixed(4) + " N\n" +
                "2. Convert Area to SI: A = " + aM2.toExponential(4) + " m²\n\n" +
                "3. Compute Pressure: P = F / A\n" +
                "   P = " + fN.toFixed(4) + " / " + aM2.toExponential(4) + " = " + pa.toFixed(2) + " Pa\n" +
                "   P = " + (pa / 1000).toFixed(4) + " kPa (" + (pa / 100000).toFixed(4) + " bar)";

      } else if (mode === 'hydrostatic') {
        var rho = parseFloat(document.getElementById('hydro-dens').value);
        var hVal = parseFloat(document.getElementById('hydro-depth').value);
        var hUnit = document.getElementById('unit-depth').value;
        var g = parseFloat(document.getElementById('hydro-gravity').value);

        if (isNaN(rho) || isNaN(hVal) || isNaN(g) || rho <= 0 || hVal < 0 || g <= 0) {
          showError("Density, depth, and gravity must be valid positive values.");
          return;
        }

        var hM = hVal * DEPTH_FACTORS[hUnit];
        pa = rho * g * hM;

        steps = "Mode: Hydrostatic Fluid Column Pressure (P = ρ * g * h)\n" +
                "Inputs: Density ρ = " + rho + " kg/m³, Depth h = " + hVal + " " + hUnit + ", g = " + g + " m/s²\n\n" +
                "1. Convert Depth to SI: h = " + hM.toFixed(4) + " m\n\n" +
                "2. Compute Hydrostatic Pressure: P = ρ * g * h\n" +
                "   P = " + rho + " * " + g + " * " + hM.toFixed(4) + "\n" +
                "   P = " + pa.toFixed(2) + " Pa (" + (pa / 1000).toFixed(4) + " kPa, " + (pa / 100000).toFixed(4) + " bar)\n\n" +
                "3. Absolute Pressure (Surface 1 atm + Hydrostatic):\n" +
                "   P_abs = 101,325 + " + pa.toFixed(2) + " = " + (pa + 101325).toFixed(2) + " Pa";

      } else if (mode === 'gauge-abs') {
        var dir = document.getElementById('conv-direction').value;
        var inVal = parseFloat(document.getElementById('conv-val').value);
        var inUnit = document.getElementById('conv-unit').value;
        var pAtmVal = parseFloat(document.getElementById('conv-patm').value);

        if (isNaN(inVal) || isNaN(pAtmVal) || pAtmVal < 0) {
          showError("Please enter valid pressure numbers.");
          return;
        }

        var inPa = inVal * PRES_FACTORS_TO_PA[inUnit];
        var pAtmPa = pAtmVal * PRES_FACTORS_TO_PA['psi']; // default label is psi

        if (dir === 'gauge-to-abs') {
          pa = inPa + pAtmPa;
          steps = "Mode: Gauge Pressure to Absolute Pressure (P_abs = P_gauge + P_atm)\n" +
                  "Inputs: Gauge = " + inVal + " " + inUnit + ", P_atm = " + pAtmVal + " psi\n\n" +
                  "1. Convert Gauge to Pa: " + inPa.toFixed(2) + " Pa\n" +
                  "2. Convert Atmospheric to Pa: " + pAtmPa.toFixed(2) + " Pa\n\n" +
                  "3. Absolute Pressure: P_abs = " + inPa.toFixed(2) + " + " + pAtmPa.toFixed(2) + "\n" +
                  "   P_abs = " + pa.toFixed(2) + " Pa (" + (pa / PRES_FACTORS_TO_PA[inUnit]).toFixed(4) + " " + inUnit + " abs)";
        } else {
          pa = inPa - pAtmPa;
          steps = "Mode: Absolute Pressure to Gauge Pressure (P_gauge = P_abs - P_atm)\n" +
                  "Inputs: Absolute = " + inVal + " " + inUnit + ", P_atm = " + pAtmVal + " psi\n\n" +
                  "1. Convert Absolute to Pa: " + inPa.toFixed(2) + " Pa\n" +
                  "2. Convert Atmospheric to Pa: " + pAtmPa.toFixed(2) + " Pa\n\n" +
                  "3. Gauge Pressure: P_gauge = " + inPa.toFixed(2) + " - " + pAtmPa.toFixed(2) + "\n" +
                  "   P_gauge = " + pa.toFixed(2) + " Pa (" + (pa / PRES_FACTORS_TO_PA[inUnit]).toFixed(4) + " " + inUnit + " gauge)";
        }
      }

      var kpa = pa / 1000.0;
      var bar = pa / 100000.0;
      var psi = pa / 6894.75729;
      var atm = pa / 101325.0;
      var mmhg = pa / 133.3224;
      var mpa = pa / 1000000.0;
      var ksi = psi / 1000.0;
      var mh2o = pa / 9806.65;

      document.getElementById('res-pa').innerText = (kpa >= 1000 || kpa <= -1000) ? mpa.toFixed(3) + " MPa" : kpa.toFixed(2) + " kPa";
      document.getElementById('res-pa-exact').innerText = pa.toLocaleString(undefined, {maximumFractionDigits: 1}) + " Pascals (N/m²)";
      document.getElementById('res-bar').innerText = bar.toFixed(3) + " bar";
      document.getElementById('res-psi').innerText = psi.toFixed(3) + " psi";
      document.getElementById('res-atm').innerText = atm.toFixed(3) + " atm";
      document.getElementById('res-mmhg').innerText = mmhg.toLocaleString(undefined, {maximumFractionDigits: 1}) + " mmHg / Torr";

      document.getElementById('eq-pa').innerText = pa.toLocaleString(undefined, {maximumFractionDigits: 0}) + " Pa";
      document.getElementById('eq-mpa').innerText = mpa.toFixed(4) + " MPa";
      document.getElementById('eq-ksi').innerText = ksi.toFixed(4) + " ksi";
      document.getElementById('eq-mh2o').innerText = mh2o.toFixed(2) + " mH₂O";

      document.getElementById('res-steps').innerText = steps;
    }

    function showError(msg) {
      document.getElementById('res-pa').innerText = "Error";
      document.getElementById('res-pa-exact').innerText = "Invalid inputs";
      document.getElementById('res-bar').innerText = "N/A";
      document.getElementById('res-psi').innerText = "N/A";
      document.getElementById('res-atm').innerText = "N/A";
      document.getElementById('res-mmhg').innerText = "N/A";
      document.getElementById('res-steps').innerText = "Error: " + msg;
    }

    function resetPressure() {
      document.getElementById('pressure-mode').value = 'mechanical';
      document.getElementById('mech-force').value = '5000';
      document.getElementById('unit-force').value = 'N';
      document.getElementById('mech-area').value = '0.025';
      document.getElementById('unit-area').value = 'm2';
      document.getElementById('hydro-fluid').value = '1000';
      document.getElementById('hydro-dens').value = '1000';
      document.getElementById('hydro-depth').value = '20';
      document.getElementById('unit-depth').value = 'm';
      document.getElementById('hydro-gravity').value = '9.80665';
      document.getElementById('conv-direction').value = 'gauge-to-abs';
      document.getElementById('conv-val').value = '32.0';
      document.getElementById('conv-unit').value = 'psi';
      document.getElementById('conv-patm').value = '14.696';
      switchPressureMode();
    }

    window.addEventListener('DOMContentLoaded', function() {
      calculatePressure();
    });
  </script>
</body>
</html>
"""

# 8. speed-calculator.html
HTML_SPEED = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Speed Calculator - Velocity, Distance, Time &amp; Running Pace</title>
  <meta name="description" content="Calculate speed (v = d/t), distance, or travel time with unit conversions. Computes average velocity, running pace (min/km, min/mi), and acceleration kinematics.">
  <link rel="canonical" href="https://calchub.org/speed-calculator.html">
  <meta property="og:title" content="Speed Calculator - Velocity, Distance &amp; Travel Time Solver">
  <meta property="og:description" content="Free multi-unit speed and velocity calculator. Solve for speed, distance, or elapsed time. Convert between mph, km/h, m/s, knots, and running pace.">
  <meta property="og:url" content="https://calchub.org/speed-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Speed Calculator - Velocity &amp; Pace Kinematics Tool">
  <meta name="twitter:description" content="Solve v = d/t with step-by-step physics formulas, athletic pace conversions, and kinematic equations.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Speed Calculator",
    "url": "https://calchub.org/speed-calculator.html",
    "description": "Calculates speed, travel distance, elapsed time, running pace, and kinematic motion properties across international units.",
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
        "name": "What is the formula to calculate speed?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The basic formula for average scalar speed is v = d / t, where v is speed, d is distance traveled, and t is elapsed travel time. In SI units, speed is expressed in meters per second (m/s)."
        }
      },
      {
        "@type": "Question",
        "name": "What is the difference between speed and velocity?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Speed is a scalar quantity indicating only how fast an object moves regardless of direction. Velocity is a vector quantity that specifies both the speed of travel and the precise spatial direction of displacement."
        }
      },
      {
        "@type": "Question",
        "name": "How do you calculate running pace from speed?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Pace is the mathematical reciprocal of speed, representing the time required to travel one unit of distance: Pace = 1 / Speed. For instance, traveling at 12 km/h corresponds to a pace of 60 / 12 = 5 minutes per kilometer."
        }
      },
      {
        "@type": "Question",
        "name": "Why is average speed not the simple arithmetic mean of two trip speeds?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "When traveling equal distances at two different speeds, average speed is the harmonic mean, not the arithmetic average. Because more time is spent traveling at the slower speed, the slower velocity carries greater temporal weight: v_avg = 2 * v1 * v2 / (v1 + v2)."
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

  <main class="calculator-container">
    <div class="calculator-header">
      <div class="calc-icon" aria-hidden="true">&#9201;</div>
      <h1>Speed Calculator</h1>
      <p class="calc-description">Solve for speed (\(v = d/t\)), travel distance, or trip duration with multi-unit conversions (mph, km/h, m/s, knots) and running pace analysis.</p>
    </div>

    <div class="calculator-body">
      <div class="input-group">
        <label for="speed-target">Variable to Calculate</label>
        <select id="speed-target" class="form-control" onchange="switchSpeedMode()">
          <option value="speed" selected>Speed (\(v = d / t\))</option>
          <option value="distance">Distance (\(d = v \times t\))</option>
          <option value="time">Travel Time (\(t = d / v\))</option>
        </select>
      </div>

      <!-- Distance Input Group -->
      <div class="input-grid" id="grp-distance">
        <div class="input-group">
          <label for="inp-dist">Distance (\(d\))</label>
          <div style="display: flex; gap: 0.5rem;">
            <input type="number" id="inp-dist" class="form-control" value="100" step="any" min="0" style="flex: 2;">
            <select id="unit-dist" class="form-control" style="flex: 1;" onchange="calculateSpeed()">
              <option value="km" selected>km</option>
              <option value="mi">miles</option>
              <option value="m">meters</option>
              <option value="ft">feet</option>
              <option value="nmi">nautical miles</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Speed Input Group (Visible only when solving for distance or time) -->
      <div class="input-grid" id="grp-speed" style="display: none;">
        <div class="input-group">
          <label for="inp-speed">Speed (\(v\))</label>
          <div style="display: flex; gap: 0.5rem;">
            <input type="number" id="inp-speed" class="form-control" value="65" step="any" min="0" style="flex: 2;">
            <select id="unit-speed" class="form-control" style="flex: 1;" onchange="calculateSpeed()">
              <option value="km_h">km/h</option>
              <option value="mph" selected>mph</option>
              <option value="m_s">m/s</option>
              <option value="knot">knots</option>
              <option value="ft_s">ft/s</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Time Input Group (Split into Hours, Minutes, Seconds) -->
      <div class="input-group" id="grp-time">
        <label>Elapsed Time (\(t\))</label>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0.5rem;">
          <div>
            <span style="font-size: 0.75rem; color: var(--text-muted, #6c757d);">Hours</span>
            <input type="number" id="time-hr" class="form-control" value="1" min="0" step="any">
          </div>
          <div>
            <span style="font-size: 0.75rem; color: var(--text-muted, #6c757d);">Minutes</span>
            <input type="number" id="time-min" class="form-control" value="15" min="0" max="59" step="any">
          </div>
          <div>
            <span style="font-size: 0.75rem; color: var(--text-muted, #6c757d);">Seconds</span>
            <input type="number" id="time-sec" class="form-control" value="0" min="0" max="59" step="any">
          </div>
        </div>
      </div>

      <div class="btn-group">
        <button type="button" class="btn btn-primary" onclick="calculateSpeed()">Calculate Motion</button>
        <button type="button" class="btn btn-secondary" onclick="resetSpeed()">Reset Defaults</button>
      </div>

      <!-- Results Display Grid -->
      <div class="results-grid" style="margin-top: 1.5rem;">
        <div class="result-card primary-result">
          <div class="result-label" id="res-primary-label">Average Speed (\(v\))</div>
          <div class="result-value" id="res-primary-val">80.00 km/h</div>
          <div class="result-subtext" id="res-primary-sub">49.71 mph &bull; 22.22 m/s</div>
        </div>

        <div class="result-card">
          <div class="result-label">Running Pace (Metric)</div>
          <div class="result-value" id="res-pace-km">0:45 min/km</div>
          <div class="result-subtext">Minutes per kilometer</div>
        </div>

        <div class="result-card">
          <div class="result-label">Running Pace (Imperial)</div>
          <div class="result-value" id="res-pace-mi">1:12 min/mi</div>
          <div class="result-subtext">Minutes per mile</div>
        </div>

        <div class="result-card">
          <div class="result-label">Maritime Speed</div>
          <div class="result-value" id="res-knots">43.20 knots</div>
          <div class="result-subtext">Nautical miles per hour</div>
        </div>
      </div>

      <!-- Multi-Unit Speed Conversion Table Card -->
      <div class="info-card" style="margin-top: 1.5rem;">
        <h3>Equivalent Multi-System Velocity Equivalents</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 0.75rem; margin-top: 0.5rem;">
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">Kilometers/hour (km/h)</div>
            <strong id="eq-kmh">80.00 km/h</strong>
          </div>
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">Miles/hour (mph)</div>
            <strong id="eq-mph">49.71 mph</strong>
          </div>
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">SI Metric (m/s)</div>
            <strong id="eq-ms">22.22 m/s</strong>
          </div>
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">Feet/second (ft/s)</div>
            <strong id="eq-fts">72.91 ft/s</strong>
          </div>
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">Mach Number (Air 20°C)</div>
            <strong id="eq-mach">0.065 Mach</strong>
          </div>
        </div>
      </div>

      <!-- Step-by-step Math Breakdown Card -->
      <div class="info-card" style="margin-top: 1.5rem;">
        <h3>Step-by-Step Kinematic &amp; Dimensional Breakdown</h3>
        <pre id="res-steps" style="white-space: pre-wrap; font-family: monospace; background: var(--bg-secondary, #f8f9fa); padding: 1rem; border-radius: 6px; font-size: 0.9rem; line-height: 1.5; color: var(--text-primary, #212529);"></pre>
      </div>
    </div>

    <!-- Article Content: 1000+ Words Clinical / Physics Deep Dive -->
    <article class="article-body">
      <h2>The Kinematics of Speed, Velocity, and Elapsed Time</h2>
      <p>
        In classical Newtonian mechanics, <strong>speed</strong> (\(v\)) is the fundamental scalar rate at which an object covers distance along a trajectory over time. It measures the magnitude of position change per unit temporal duration, completely independent of spatial heading or vector direction. In contrast, <strong>velocity</strong> (\(\vec{v}\)) is a vector quantity possessing both speed (magnitude) and directional orientation in Euclidean space.
      </p>
      <p>
        Mastery of kinematic motion formulas is indispensable across transportation planning, automotive engineering, athletics, orbital mechanics, and aviation. Logistics managers compute precise route velocity profiles to optimize freight schedules and fuel economy; marathon runners structure pacing splits to conserve glycogen reserves; and traffic accident reconstructionists utilize kinematic braking equations to estimate pre-impact vehicle velocities from roadway skid marks.
      </p>

      <h2>Governing Mathematical Equations</h2>

      <h3>1. The Fundamental Speed Triangle</h3>
      <p>
        For uniform rectilinear motion, the governing relationship connects scalar distance (\(d\)), elapsed time (\(t\)), and average speed (\(v\)):
      </p>
      $$v = \frac{d}{t}$$
      <p>
        From this primary relation, algebraic manipulation yields the complementary kinematic formulas:
      </p>
      <p><strong>Solving for Distance:</strong></p>
      $$d = v \times t$$
      <p><strong>Solving for Elapsed Time:</strong></p>
      $$t = \frac{d}{v}$$

      <h3>2. The Harmonic Mean Trap in Average Trip Speed</h3>
      <p>
        One of the most widespread mathematical errors in physics and navigation is assuming that average speed over a two-leg journey is the simple arithmetic mean of the two leg speeds. If a commuter travels from Town A to Town B at \(60\text{ km/h}\) and returns over the exact same route at \(40\text{ km/h}\), the intuitive guess of \(50\text{ km/h}\) is mathematically false.
      </p>
      <p>
        Because average speed is defined strictly as total distance divided by total elapsed time:
      </p>
      $$v_{\text{avg}} = \frac{d_{\text{total}}}{t_{\text{total}}} = \frac{2d}{t_1 + t_2} = \frac{2d}{\frac{d}{v_1} + \frac{d}{v_2}} = \frac{2}{\frac{1}{v_1} + \frac{1}{v_2}} = \frac{2 v_1 v_2}{v_1 + v_2}$$
      <p>
        Substituting the journey velocities:
      </p>
      $$v_{\text{avg}} = \frac{2 \times 60 \times 40}{60 + 40} = \frac{4,800}{100} = 48.0\text{ km/h}$$
      <p>
        The slower speed occupies a greater fraction of total travel time (\(1.5\times\) as long), heavily skewing the true average toward \(40\text{ km/h}\).
      </p>

      <h3>3. Athletic Running Pace and Reciprocal Mechanics</h3>
      <p>
        In competitive endurance sports (running, rowing, swimming), athletes quantify speed inversely as <strong>pace</strong>—the time duration required to traverse a standardized unit of distance:
      </p>
      $$\text{Pace} = \frac{t}{d} = \frac{1}{v}$$
      <p>
        To convert between velocity in kilometers per hour and running pace in minutes per kilometer:
      </p>
      $$\text{Pace (min/km)} = \frac{60}{v\text{ (km/h)}}$$
      <p>
        Similarly, for miles per hour to minutes per mile:
      </p>
      $$\text{Pace (min/mi)} = \frac{60}{v\text{ (mph)}}$$

      <h2>International Velocity Systems and Conversion Constants</h2>
      <p>
        The table below provides rigorous conversion factors across SI metric, imperial, nautical, and astronomical speed benchmarks.
      </p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Speed Unit</th>
            <th>Symbol</th>
            <th>SI Metric (m/s)</th>
            <th>Metric (km/h)</th>
            <th>Imperial (mph)</th>
            <th>Maritime (knots)</th>
            <th>Domain Application</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Meter per second (SI)</td>
            <td>m/s</td>
            <td>1.0 (Exact)</td>
            <td>3.6 (Exact)</td>
            <td>2.23694</td>
            <td>1.94384</td>
            <td>Physics laboratory, ballistic windage</td>
          </tr>
          <tr>
            <td>Kilometer per hour</td>
            <td>km/h</td>
            <td>0.27778</td>
            <td>1.0 (Exact)</td>
            <td>0.621371</td>
            <td>0.539957</td>
            <td>International road traffic, rail transport</td>
          </tr>
          <tr>
            <td>Mile per hour</td>
            <td>mph</td>
            <td>0.44704 (Exact)</td>
            <td>1.609344 (Exact)</td>
            <td>1.0 (Exact)</td>
            <td>0.868976</td>
            <td>US &amp; UK roadways, NASCAR racing</td>
          </tr>
          <tr>
            <td>Knot (Nautical mi/h)</td>
            <td>kt / kn</td>
            <td>0.514444</td>
            <td>1.852 (Exact)</td>
            <td>1.150779</td>
            <td>1.0 (Exact)</td>
            <td>Maritime shipping, commercial aviation</td>
          </tr>
          <tr>
            <td>Foot per second</td>
            <td>ft/s</td>
            <td>0.3048 (Exact)</td>
            <td>1.09728</td>
            <td>0.681818</td>
            <td>0.592484</td>
            <td>Ballistics muzzle velocity, hydraulic flumes</td>
          </tr>
          <tr>
            <td>Speed of Sound (Mach 1, 20°C)</td>
            <td>Ma</td>
            <td>343.2</td>
            <td>1,235.5</td>
            <td>767.7</td>
            <td>667.2</td>
            <td>Supersonic aviation, shock wave physics</td>
          </tr>
          <tr>
            <td>Speed of Light (Vacuum)</td>
            <td>\(c\)</td>
            <td>299,792,458 (Exact)</td>
            <td>\(1.079 \times 10^9\)</td>
            <td>\(6.706 \times 10^8\)</td>
            <td>\(5.827 \times 10^8\)</td>
            <td>Relativistic physics, quantum electrodynamics</td>
          </tr>
        </tbody>
      </table>

      <h2>Benchmark Velocities Across the Universe</h2>
      <p>
        To contextualize physical velocity scales from biological organisms to cosmic phenomena:
      </p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Physical Entity / Event</th>
            <th>Approximate Speed (m/s)</th>
            <th>Approximate Speed (km/h)</th>
            <th>Approximate Speed (mph)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Garden Snail (\(Cornu\ aspersum\))</td>
            <td>0.001</td>
            <td>0.0036</td>
            <td>0.0022</td>
          </tr>
          <tr>
            <td>Human Walking Stride (Average)</td>
            <td>1.4</td>
            <td>5.0</td>
            <td>3.1</td>
          </tr>
          <tr>
            <td>Usain Bolt 100m Sprint (Peak Velocity)</td>
            <td>12.42</td>
            <td>44.72</td>
            <td>27.78</td>
          </tr>
          <tr>
            <td>Cheetah (\(Acinonyx\ jubatus\)) Full Sprint</td>
            <td>29.0</td>
            <td>104.4</td>
            <td>64.9</td>
          </tr>
          <tr>
            <td>Peregrine Falcon Diving stoop</td>
            <td>108.0</td>
            <td>389.0</td>
            <td>242.0</td>
          </tr>
          <tr>
            <td>Boeing 787 Dreamliner Cruise</td>
            <td>250.0</td>
            <td>903.0</td>
            <td>561.0</td>
          </tr>
          <tr>
            <td>Rifle Bullet (5.56×45mm NATO M855)</td>
            <td>940.0</td>
            <td>3,384.0</td>
            <td>2,103.0</td>
          </tr>
          <tr>
            <td>International Space Station (LEO Orbit)</td>
            <td>7,660.0</td>
            <td>27,576.0</td>
            <td>17,135.0</td>
          </tr>
          <tr>
            <td>Earth Orbital Speed around Sun</td>
            <td>29,780.0</td>
            <td>107,208.0</td>
            <td>66,616.0</td>
          </tr>
        </tbody>
      </table>

      <h2>Practical Real-World Kinematic Case Studies</h2>

      <div class="worked-example-card">
        <h3>Case Study 1: Marathon Race Strategy &ndash; Pacing and Negative Splits</h3>
        <p><strong>Scenario:</strong> A marathon runner aims to achieve a sub-3-hour finish time on a certified \(42.195\text{ km}\) course (\(26.21875\text{ miles}\)). The runner adopts a negative split strategy: completing the first half (\(21.0975\text{ km}\)) in 1 hour 31 minutes (91.0 min), and accelerating to complete the second half in 1 hour 27 minutes (87.0 min).</p>
        <p><strong>Objective:</strong> Calculate required speeds and exact pacing splits in minutes per kilometer and minutes per mile for both race halves and the overall event.</p>
        <div class="step-solution">
          <p><strong>1. First Half Kinematics:</strong></p>
          $$v_1 = \frac{21.0975\text{ km}}{1.5167\text{ hr}} \approx 13.910\text{ km/h} \ (8.643\text{ mph})$$
          $$\text{Pace}_1 = \frac{91.0\text{ min}}{21.0975\text{ km}} \approx 4.313\text{ min/km} \rightarrow 4\text{ min } 19\text{ sec / km}$$
          $$\text{Imperial Pace}_1 = \frac{91.0\text{ min}}{13.109\text{ mi}} \approx 6.942\text{ min/mi} \rightarrow 6\text{ min } 56\text{ sec / mi}$$
          <p><strong>2. Second Half Kinematics (Negative Split Acceleration):</strong></p>
          $$v_2 = \frac{21.0975\text{ km}}{1.4500\text{ hr}} \approx 14.550\text{ km/h} \ (9.041\text{ mph})$$
          $$\text{Pace}_2 = \frac{87.0\text{ min}}{21.0975\text{ km}} \approx 4.124\text{ min/km} \rightarrow 4\text{ min } 07\text{ sec / km}$$
          $$\text{Imperial Pace}_2 = \frac{87.0\text{ min}}{13.109\text{ mi}} \approx 6.637\text{ min/mi} \rightarrow 6\text{ min } 38\text{ sec / mi}$$
          <p><strong>3. Total Marathon Outcome:</strong> Total time = 2 hr 58 min 00 sec. Overall average velocity = \(14.223\text{ km/h}\) (\(8.838\text{ mph}\)), achieving an average pace of \(4\text{ min } 13\text{ sec / km}\) (\(6\text{ min } 47\text{ sec / mi}\)), successfully breaking the 3:00 barrier!</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Traffic Forensic Accident Reconstruction &ndash; Skid Mark Analysis</h3>
        <p><strong>Scenario:</strong> Following a dry asphalt collision, forensic investigators measure continuous, locked four-wheel tire skid marks of length \(d = 42.0\text{ m}\) (\(137.8\text{ ft}\)) before the vehicle came to a complete stop (\(v_f = 0\)). The road surface has a measured dry friction drag factor of \(\mu = 0.75\). Gravitational acceleration is \(g = 9.80665\text{ m/s}^2\).</p>
        <p><strong>Objective:</strong> Calculate the minimum initial speed \(v_0\) of the vehicle at the exact instant the driver locked the brakes, and determine if the driver exceeded the posted \(60\text{ km/h}\) speed limit.</p>
        <div class="step-solution">
          <p><strong>1. Deceleration from Coulomb Friction:</strong></p>
          <p>The braking deceleration is \(a = -\mu g = -0.75 \times 9.80665\text{ m/s}^2 \approx -7.355\text{ m/s}^2\).</p>
          <p><strong>2. Kinematic Torricelli Formula:</strong></p>
          $$v_f^2 = v_0^2 + 2 a d \implies 0 = v_0^2 - 2 \mu g d$$
          $$v_0 = \sqrt{2 \mu g d} = \sqrt{2 \times 0.75 \times 9.80665\text{ m/s}^2 \times 42.0\text{ m}} = \sqrt{617.819} \approx 24.856\text{ m/s}$$
          <p><strong>3. Unit Conversion &amp; Legal Finding:</strong></p>
          $$v_0 = 24.856\text{ m/s} \times 3.6 = 89.48\text{ km/h} \ (55.60\text{ mph})$$
          <p>The vehicle was traveling at nearly \(90\text{ km/h}\) when brakes were applied—substantially exceeding the \(60\text{ km/h}\) limit by nearly 50%!</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 3: Commercial Logistics &ndash; Multi-Modal Freight Transit Planning</h3>
        <p><strong>Scenario:</strong> A logistics carrier transports containerized cargo across a \(720\text{ km}\) corridor consisting of three distinct segments: (1) Urban drayage trucking: \(60\text{ km}\) at an average congested speed of \(30\text{ km/h}\); (2) High-speed dedicated rail freight: \(540\text{ km}\) at \(90\text{ km/h}\); (3) Final rural delivery trucking: \(120\text{ km}\) at \(60\text{ km/h}\).</p>
        <p><strong>Objective:</strong> Compute the elapsed travel time for each segment, determine overall transit duration, and calculate true end-to-end average transport velocity.</p>
        <div class="step-solution">
          <p><strong>1. Segment Durations:</strong></p>
          $$t_1 = \frac{60\text{ km}}{30\text{ km/h}} = 2.0\text{ hours}$$
          $$t_2 = \frac{540\text{ km}}{90\text{ km/h}} = 6.0\text{ hours}$$
          $$t_3 = \frac{120\text{ km}}{60\text{ km/h}} = 2.0\text{ hours}$$
          <p><strong>2. Total Transit Duration:</strong></p>
          $$t_{\text{total}} = 2.0 + 6.0 + 2.0 = 10.0\text{ hours}$$
          <p><strong>3. True End-to-End Average Speed:</strong></p>
          $$v_{\text{avg}} = \frac{d_{\text{total}}}{t_{\text{total}}} = \frac{720\text{ km}}{10.0\text{ hr}} = 72.0\text{ km/h} \ (44.74\text{ mph})$$
          <p>Notice that the simple unweighted average of the three segment speeds would have been \(\frac{30 + 90 + 60}{3} = 60.0\text{ km/h}\). Because the fast rail segment comprised 75% of total route distance, the genuine composite velocity is significantly higher (\(72.0\text{ km/h}\)).</p>
        </div>
      </div>

      <h2>Kinematic Acceleration and Non-Uniform Velocity</h2>
      <p>
        When an object's speed changes over time at a constant linear acceleration \(a\), four classic kinematic equations describe its motion:
      </p>
      $$\text{1. } v_f = v_0 + a t$$
      $$\text{2. } d = v_0 t + \frac{1}{2} a t^2$$
      $$\text{3. } v_f^2 = v_0^2 + 2 a d$$
      $$\text{4. } d = \frac{v_0 + v_f}{2} t$$
      <p>
        Where \(v_0\) is initial velocity, \(v_f\) is final velocity, \(a\) is constant acceleration in \(\text{m/s}^2\), \(t\) is elapsed time in seconds, and \(d\) is net displacement in meters. These equations govern rocketry boost phases, aircraft runway roll distances, and emergency automotive stopping sight distances on civil highways.
      </p>

      <h2>Frequently Asked Questions</h2>
      <div class="faq-accordion">
        <details class="faq-item">
          <summary class="faq-question">What is instantaneous speed versus average speed?</summary>
          <div class="faq-answer">
            <p>Average speed calculates the gross distance traveled divided by total elapsed time over a finite interval: \(v_{\text{avg}} = \Delta d / \Delta t\). Instantaneous speed represents velocity at one infinitesimal exact moment in time, mathematically defined as the first derivative of position with respect to time: \(v(t) = \lim_{\Delta t \to 0} \frac{\Delta d}{\Delta t} = \frac{dd}{dt}\). A car's speedometer displays instantaneous speed.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">How does a nautical knot differ from a standard statute mile per hour?</summary>
          <div class="faq-answer">
            <p>One knot equals one nautical mile per hour. A nautical mile is historically defined as one minute of arc along a meridian of Earth's latitude, standardized internationally as exactly 1,852 meters (1.15078 statute miles). Therefore, 1 knot is roughly 15% faster than 1 mph (1 knot = 1.151 mph = 1.852 km/h).</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">What is escape velocity?</summary>
          <div class="faq-answer">
            <p>Escape velocity is the minimum initial speed a non-propelled ballistic projectile must achieve to break free from the gravitational pull of a celestial body without further propulsion. For Earth, escape velocity is: \(v_e = \sqrt{\frac{2 G M}{R}} \approx 11.186\text{ km/s}\) (approx. \(40,270\text{ km/h}\) or \(25,020\text{ mph}\)).</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">How do you convert km/h to m/s in your head?</summary>
          <div class="faq-answer">
            <p>Because there are 1,000 meters in a kilometer and 3,600 seconds in an hour, the exact conversion factor is: \(1\text{ m/s} = 3.6\text{ km/h}\). To convert km/h to m/s, simply divide by 3.6 (e.g., 90 km/h ÷ 3.6 = 25 m/s). To convert m/s to km/h, multiply by 3.6 (e.g., 20 m/s × 3.6 = 72 km/h).</p>
          </div>
        </details>
      </div>

      <!-- Cross-Disciplinary Internal Links -->
      <div class="related-calculators" style="margin-top: 2rem; padding: 1.5rem; background: var(--bg-secondary, #f8f9fa); border-radius: 8px;">
        <h3>Related Engineering &amp; Physics Calculators</h3>
        <ul style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.75rem; list-style: none; padding: 0;">
          <li><a href="density-calculator.html">&rarr; Density &amp; Buoyancy Solver</a></li>
          <li><a href="pressure-calculator.html">&rarr; Mechanical &amp; Hydrostatic Pressure Calculator</a></li>
          <li><a href="force-converter.html">&rarr; Force &amp; Newton's Laws Solver</a></li>
          <li><a href="volume-calculator.html">&rarr; Volume Calculator (3D Solids)</a></li>
          <li><a href="distance-calculator.html">&rarr; Coordinate Distance Calculator</a></li>
          <li><a href="average-calculator.html">&rarr; Average &amp; Harmonic Mean Calculator</a></li>
        </ul>
      </div>
    </article>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-col">
        <h4>CalcHub</h4>
        <p>Comprehensive mathematical, statistical, and engineering calculation tools.</p>
      </div>
      <div class="footer-col">
        <h4>Discipline Hubs</h4>
        <ul class="footer-links">
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="math.html">Mathematics</a></li>
          <li><a href="converter.html">Unit Converters</a></li>
          <li><a href="engineering.html">Electrical &amp; Engineering</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 CalcHub. All rights reserved. Peer-reviewed computational algorithms.</p>
    </div>
  </footer>

  <script>
    var DIST_FACTORS_TO_METERS = {
      'km': 1000.0,
      'mi': 1609.344,
      'm': 1.0,
      'ft': 0.3048,
      'nmi': 1852.0
    };

    var SPEED_FACTORS_TO_MS = {
      'km_h': 0.277777778,
      'mph': 0.44704,
      'm_s': 1.0,
      'knot': 0.514444444,
      'ft_s': 0.3048
    };

    function switchSpeedMode() {
      var target = document.getElementById('speed-target').value;
      var grpDist = document.getElementById('grp-distance');
      var grpSpeed = document.getElementById('grp-speed');
      var grpTime = document.getElementById('grp-time');

      grpDist.style.display = (target === 'distance') ? 'none' : 'block';
      grpSpeed.style.display = (target === 'speed') ? 'none' : 'block';
      grpTime.style.display = (target === 'time') ? 'none' : 'block';

      var lbl = document.getElementById('res-primary-label');
      if (target === 'speed') {
        lbl.innerText = "Average Speed (v)";
      } else if (target === 'distance') {
        lbl.innerText = "Calculated Distance (d)";
      } else if (target === 'time') {
        lbl.innerText = "Calculated Travel Time (t)";
      }

      calculateSpeed();
    }

    function calculateSpeed() {
      var target = document.getElementById('speed-target').value;
      var dVal = parseFloat(document.getElementById('inp-dist').value);
      var dUnit = document.getElementById('unit-dist').value;
      var sVal = parseFloat(document.getElementById('inp-speed').value);
      var sUnit = document.getElementById('unit-speed').value;

      var hr = parseFloat(document.getElementById('time-hr').value) || 0;
      var min = parseFloat(document.getElementById('time-min').value) || 0;
      var sec = parseFloat(document.getElementById('time-sec').value) || 0;
      var totalSec = hr * 3600 + min * 60 + sec;

      var v_ms = 0, d_m = 0, t_s = 0;
      var steps = "";

      if (target === 'speed') {
        if (isNaN(dVal) || dVal <= 0 || totalSec <= 0) {
          showError("Distance and elapsed time must be strictly positive.");
          return;
        }
        d_m = dVal * DIST_FACTORS_TO_METERS[dUnit];
        t_s = totalSec;
        v_ms = d_m / t_s;

        var kmh = v_ms * 3.6;
        var mph = v_ms / 0.44704;
        steps = "Mode: Calculate Speed (v = d / t)\n" +
                "Inputs: Distance = " + dVal + " " + dUnit + ", Time = " + hr + "h " + min + "m " + sec + "s (" + totalSec + "s)\n\n" +
                "1. Convert Distance to SI: d = " + d_m.toFixed(2) + " m\n" +
                "2. Total Time in Seconds: t = " + totalSec + " s\n\n" +
                "3. Average Speed: v = d / t\n" +
                "   v = " + d_m.toFixed(2) + " / " + totalSec + " = " + v_ms.toFixed(4) + " m/s\n" +
                "   v = " + kmh.toFixed(2) + " km/h (" + mph.toFixed(2) + " mph)";

        document.getElementById('res-primary-val').innerText = kmh.toFixed(2) + " km/h";
        document.getElementById('res-primary-sub').innerText = mph.toFixed(2) + " mph • " + v_ms.toFixed(2) + " m/s";

      } else if (target === 'distance') {
        if (isNaN(sVal) || sVal <= 0 || totalSec <= 0) {
          showError("Speed and elapsed time must be strictly positive.");
          return;
        }
        v_ms = sVal * SPEED_FACTORS_TO_MS[sUnit];
        t_s = totalSec;
        d_m = v_ms * t_s;

        var dDisplay = d_m / DIST_FACTORS_TO_METERS[dUnit];
        steps = "Mode: Calculate Distance (d = v * t)\n" +
                "Inputs: Speed = " + sVal + " " + sUnit.replace('_', '/') + ", Time = " + totalSec + " s\n\n" +
                "1. Speed in SI: v = " + v_ms.toFixed(4) + " m/s\n" +
                "2. Total Seconds: t = " + totalSec + " s\n\n" +
                "3. Traveled Distance: d = v * t\n" +
                "   d = " + v_ms.toFixed(4) + " * " + totalSec + " = " + d_m.toFixed(2) + " m\n" +
                "   d = " + dDisplay.toFixed(3) + " " + dUnit + " (" + (d_m / 1000).toFixed(3) + " km, " + (d_m / 1609.344).toFixed(3) + " miles)";

        document.getElementById('res-primary-val').innerText = dDisplay.toLocaleString(undefined, {maximumFractionDigits: 3}) + " " + dUnit;
        document.getElementById('res-primary-sub').innerText = (d_m / 1000).toFixed(3) + " km • " + (d_m / 1609.344).toFixed(3) + " miles";

      } else if (target === 'time') {
        if (isNaN(dVal) || isNaN(sVal) || dVal <= 0 || sVal <= 0) {
          showError("Distance and speed must be strictly positive.");
          return;
        }
        d_m = dVal * DIST_FACTORS_TO_METERS[dUnit];
        v_ms = sVal * SPEED_FACTORS_TO_MS[sUnit];
        t_s = d_m / v_ms;

        var th = Math.floor(t_s / 3600);
        var tm = Math.floor((t_s % 3600) / 60);
        var ts = (t_s % 60).toFixed(1);

        steps = "Mode: Calculate Travel Time (t = d / v)\n" +
                "Inputs: Distance = " + dVal + " " + dUnit + ", Speed = " + sVal + " " + sUnit.replace('_', '/') + "\n\n" +
                "1. Distance in SI: d = " + d_m.toFixed(2) + " m\n" +
                "2. Speed in SI: v = " + v_ms.toFixed(4) + " m/s\n\n" +
                "3. Elapsed Time: t = d / v\n" +
                "   t = " + d_m.toFixed(2) + " / " + v_ms.toFixed(4) + " = " + t_s.toFixed(2) + " seconds\n" +
                "   Time = " + th + " hr " + tm + " min " + ts + " sec";

        document.getElementById('res-primary-val').innerText = th + "h " + tm + "m " + Math.round(ts) + "s";
        document.getElementById('res-primary-sub').innerText = (t_s / 3600).toFixed(2) + " hours • " + t_s.toFixed(0) + " seconds";
      }

      // Calculations for equivalent speed units
      var vKmH = v_ms * 3.6;
      var vMph = v_ms / 0.44704;
      var vFtS = v_ms / 0.3048;
      var vKnots = v_ms / 0.514444444;
      var vMach = v_ms / 343.2;

      // Running pace calculations
      if (vKmH > 0) {
        var secPerKm = 3600.0 / vKmH;
        var pKmMin = Math.floor(secPerKm / 60);
        var pKmSec = Math.floor(secPerKm % 60);
        document.getElementById('res-pace-km').innerText = pKmMin + ":" + (pKmSec < 10 ? "0" : "") + pKmSec + " min/km";
      } else {
        document.getElementById('res-pace-km').innerText = "N/A";
      }

      if (vMph > 0) {
        var secPerMi = 3600.0 / vMph;
        var pMiMin = Math.floor(secPerMi / 60);
        var pMiSec = Math.floor(secPerMi % 60);
        document.getElementById('res-pace-mi').innerText = pMiMin + ":" + (pMiSec < 10 ? "0" : "") + pMiSec + " min/mi";
      } else {
        document.getElementById('res-pace-mi').innerText = "N/A";
      }

      document.getElementById('res-knots').innerText = vKnots.toFixed(2) + " knots";

      document.getElementById('eq-kmh').innerText = vKmH.toFixed(2) + " km/h";
      document.getElementById('eq-mph').innerText = vMph.toFixed(2) + " mph";
      document.getElementById('eq-ms').innerText = v_ms.toFixed(2) + " m/s";
      document.getElementById('eq-fts').innerText = vFtS.toFixed(2) + " ft/s";
      document.getElementById('eq-mach').innerText = vMach.toFixed(4) + " Mach";

      document.getElementById('res-steps').innerText = steps;
    }

    function showError(msg) {
      document.getElementById('res-primary-val').innerText = "Error";
      document.getElementById('res-primary-sub').innerText = "Invalid calculation";
      document.getElementById('res-pace-km').innerText = "N/A";
      document.getElementById('res-pace-mi').innerText = "N/A";
      document.getElementById('res-knots').innerText = "N/A";
      document.getElementById('res-steps').innerText = "Error: " + msg;
    }

    function resetSpeed() {
      document.getElementById('speed-target').value = 'speed';
      document.getElementById('inp-dist').value = '100';
      document.getElementById('unit-dist').value = 'km';
      document.getElementById('inp-speed').value = '65';
      document.getElementById('unit-speed').value = 'mph';
      document.getElementById('time-hr').value = '1';
      document.getElementById('time-min').value = '15';
      document.getElementById('time-sec').value = '0';
      switchSpeedMode();
    }

    window.addEventListener('DOMContentLoaded', function() {
      calculateSpeed();
    });
  </script>
</body>
</html>
"""

def generate_part4():
    f7 = os.path.join(BASE_DIR, "pressure-calculator.html")
    with open(f7, "w", encoding="utf-8") as fp:
        fp.write(HTML_PRESSURE.strip() + "\n")
    print(f"Generated: {f7}")

    f8 = os.path.join(BASE_DIR, "speed-calculator.html")
    with open(f8, "w", encoding="utf-8") as fp:
        fp.write(HTML_SPEED.strip() + "\n")
    print(f"Generated: {f8}")

if __name__ == "__main__":
    generate_part4()
