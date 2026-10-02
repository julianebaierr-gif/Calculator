# -*- coding: utf-8 -*-
"""
Script to generate Batch 8 Part 4 tools:
7. fire-sprinkler-hydraulic-calculator.html
8. strobe-candela-calculator.html
"""
import os

TOOL_7_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fire Sprinkler Hydraulic Calculator | NFPA 13 Flow & Pressure Loss</title>
  <meta name="description" content="Calculate fire sprinkler hydraulic discharge and pipe friction loss using NFPA 13 standards and the Hazen-Williams equation. Computes head discharge (Q=K√P), friction loss, velocity, and elevation pressure head.">
  <link rel="canonical" href="https://calchub.cloud/fire-sprinkler-hydraulic-calculator.html">
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
        "name": "Fire Sprinkler Hydraulic Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "NFPA 13 compliant hydraulic calculation engine solving sprinkler head flow Q = K*sqrt(P), Hazen-Williams pipe friction loss, equivalent fitting lengths, and static elevation pressure head.",
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
            "name": "What is the Hazen-Williams formula used in NFPA 13 fire sprinkler hydraulic calculations?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "NFPA 13 mandates the Hazen-Williams formula for determining friction loss in water-based fire suppression piping: p = 4.52 * Q^1.85 / (C^1.85 * d^4.87), where p is the frictional pressure gradient in psi per foot of pipe, Q is discharge flow in gallons per minute (gpm), C is the pipe roughness coefficient (e.g., 120 for black steel, 150 for CPVC/copper), and d is the actual internal diameter of the pipe in inches."
            }
          },
          {
            "@type": "Question",
            "name": "How is the discharge flow rate (Q) of a fire sprinkler head determined?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Sprinkler head flow follows the orifice discharge relationship: Q = K * sqrt(P), where Q is the flow rate in gpm, K is the manufacturer discharge coefficient (K-factor, e.g., 5.6 for standard 1/2-inch orifice, 8.0 for 3/4-inch large orifice), and P is the operating water pressure at the head in pounds per square inch (psi). Conversely, the minimum required pressure is P = (Q / K)^2."
            }
          },
          {
            "@type": "Question",
            "name": "What Hazen-Williams C-factor should be used for fire sprinkler piping?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Per NFPA 13 Table 27.2.4.8.1: Wet black steel pipe uses C = 120; dry steel pipe and preaction systems use C = 100 to account for accelerated internal oxidation; galvanized steel wet pipe uses C = 120; copper tubing and chlorinated polyvinyl chloride (CPVC) use C = 150; and cement-lined ductile iron underground pipe uses C = 140."
            }
          },
          {
            "@type": "Question",
            "name": "How does elevation change affect fire sprinkler system hydraulic calculations?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Water exerts a hydrostatic head pressure of 0.433 psi per foot of vertical elevation (1 psi = 2.31 feet of head). For upward piping risers feeding elevated sprinklers, an elevation penalty of 0.433 psi/ft must be added to the required supply pressure. Conversely, downhill piping runs gain 0.433 psi/ft of static pressure."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="fire">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo"><span class="logo-icon">&pi;</span><span class="logo-text">Calc<strong>Hub</strong></span></a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="engineering.html">Engineering</a>
        <a href="solar-energy.html">Solar</a>
        <a href="fire-safety.html" class="active">Fire Safety</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo; <a href="fire-safety.html">Fire Safety</a> &rsaquo; <span>Fire Sprinkler Hydraulic Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">NFPA 13 Standards &amp; Fluid Mechanics</div>
          <h1 class="calc-title">Fire Sprinkler Hydraulic Calculator</h1>
          <p class="calc-tagline">Calculate sprinkler head discharge rates, Hazen-Williams friction loss gradients, equivalent fitting lengths, and total source pressure demands in accordance with NFPA 13 fire protection engineering standards.</p>
        </header>

        <div class="tool-card">
          <form id="sprinklerCalcForm">
            <div class="calc-grid">
              <div class="form-group">
                <label for="kFactor">Sprinkler Orifice K-Factor</label>
                <select id="kFactor">
                  <option value="5.6" selected>K = 5.6 (1/2" Standard Orifice)</option>
                  <option value="8.0">K = 8.0 (3/4" Large Orifice)</option>
                  <option value="11.2">K = 11.2 (17/32" Extra Large Orifice - ELO)</option>
                  <option value="14.0">K = 14.0 (3/4" Early Suppression Fast Response - ESFR)</option>
                  <option value="16.8">K = 16.8 (3/4" Storage / Control Mode Specific App)</option>
                  <option value="22.4">K = 22.4 (1" High Density ESFR)</option>
                  <option value="25.2">K = 25.2 (1" Storage ESFR)</option>
                  <option value="custom">Custom K-Factor...</option>
                </select>
              </div>

              <div class="form-group" id="customKGroup" style="display: none;">
                <label for="customK">Custom K-Factor [gpm / &radic;psi]</label>
                <input type="number" id="customK" step="0.1" min="1.0" max="50.0" value="5.6">
              </div>

              <div class="form-group">
                <label for="flowMode">Flow Calculation Basis</label>
                <select id="flowMode">
                  <option value="headPress" selected>Specify Head Operating Pressure (psi)</option>
                  <option value="headFlow">Specify Required Discharge Flow per Head (gpm)</option>
                </select>
              </div>

              <div class="form-group" id="headPressGroup">
                <label for="headPress">Remote Head Pressure [psi] (Min 7.0 psi NFPA 13)</label>
                <input type="number" id="headPress" step="0.5" min="7.0" max="175.0" value="7.0">
              </div>

              <div class="form-group" id="headFlowGroup" style="display: none;">
                <label for="headFlow">Required Discharge per Head [gpm]</label>
                <input type="number" id="headFlow" step="0.5" min="5.0" max="250.0" value="14.8">
              </div>

              <div class="form-group">
                <label for="numHeads">Active Sprinklers on Branch Line</label>
                <input type="number" id="numHeads" min="1" max="50" step="1" value="4">
              </div>

              <div class="form-group">
                <label for="pipeSize">Nominal Pipe Size (Schedule 40 Steel)</label>
                <select id="pipeSize">
                  <option value="1.049">1" (Actual ID: 1.049 in)</option>
                  <option value="1.380">1-1/4" (Actual ID: 1.380 in)</option>
                  <option value="1.610" selected>1-1/2" (Actual ID: 1.610 in)</option>
                  <option value="2.067">2" (Actual ID: 2.067 in)</option>
                  <option value="2.469">2-1/2" (Actual ID: 2.469 in)</option>
                  <option value="3.068">3" (Actual ID: 3.068 in)</option>
                  <option value="4.026">4" (Actual ID: 4.026 in)</option>
                  <option value="6.065">6" (Actual ID: 6.065 in)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="pipeLength">Physical Pipe Length [feet]</label>
                <input type="number" id="pipeLength" step="1" min="1" max="1000" value="60">
              </div>

              <div class="form-group">
                <label for="cFactor">Pipe Material Hazen-Williams C-Factor</label>
                <select id="cFactor">
                  <option value="120" selected>C = 120 (Wet Black Steel Pipe)</option>
                  <option value="100">C = 100 (Dry Pipe / Preaction Steel Systems)</option>
                  <option value="150">C = 150 (CPVC Plastic / Type K/L Copper Tubing)</option>
                  <option value="140">C = 140 (Cement-Lined Ductile Iron Underground)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="numElbows">Standard 90&deg; Screwed/Flanged Elbows</label>
                <input type="number" id="numElbows" min="0" max="20" step="1" value="2">
              </div>

              <div class="form-group">
                <label for="numTees">Tees (Flow Turned Through Branch)</label>
                <input type="number" id="numTees" min="0" max="20" step="1" value="1">
              </div>

              <div class="form-group">
                <label for="elevChange">Elevation Change &Delta;h [feet] (+ Up, - Down)</label>
                <input type="number" id="elevChange" step="0.5" min="-100" max="200" value="12">
              </div>
            </div>

            <div class="calc-actions">
              <button type="button" id="calcBtn" class="btn btn-primary">Calculate Hydraulic Demand</button>
              <button type="reset" id="resetBtn" class="btn btn-secondary">Reset Defaults</button>
            </div>
          </form>

          <div id="sprinklerResultBox" class="results-container" style="display: none;">
            <h3>Hydraulic Analysis & Friction Demand Results</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label">Total Required Source Pressure</span>
                <span id="resTotalPress" class="result-value">-- psi</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Flow per Sprinkler Head</span>
                <span id="resHeadFlow" class="result-value">-- gpm</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Operating Head Pressure (Remote)</span>
                <span id="resHeadPress" class="result-value">-- psi</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Total System Discharge Flow</span>
                <span id="resTotalFlow" class="result-value">-- gpm</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Total Equivalent Pipe Length</span>
                <span id="resEquivLength" class="result-value">-- ft</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Pipe Friction Loss (&Delta;P_friction)</span>
                <span id="resFrictionLoss" class="result-value">-- psi</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Friction Gradient (psi / ft)</span>
                <span id="resGradient" class="result-value">-- psi/ft</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Water Velocity in Pipe</span>
                <span id="resVelocity" class="result-value">-- ft/s</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Elevation Static Head (&Delta;P_elev)</span>
                <span id="resElevHead" class="result-value">-- psi</span>
              </div>
            </div>
            <div id="velocityWarning" style="display: none; margin-top: 1rem; color: #b45309; background: #fffbeb; border: 1px solid #fde68a; padding: 0.75rem; border-radius: 6px;"></div>
          </div>
        </div>

        <article class="article-body">
          <h2>Fundamental Hydraulics of Fire Sprinkler Systems</h2>
          <p>Fire sprinkler system hydraulic calculations form the engineering foundation of life safety design across commercial, industrial, institutional, and residential buildings. Governed strictly by the National Fire Protection Association under <strong>NFPA 13</strong> (<em>Standard for the Installation of Sprinkler Systems</em>), hydraulic sizing dictates the precise balance between available water supply pressure, volumetric discharge capacity, pipe diameter constraints, and internal friction losses.</p>

          <p>Historical pipe schedule methods—which relied on prescriptive tables matching head counts to pipe nominal diameters—have been largely superseded in modern building codes by rigorous, computerized hydraulic calculations. Hydraulic calculation proves whether a municipal water main, fire pump, or elevated storage reservoir can simultaneously deliver the minimum operating pressure at the hydraulically most remote sprinkler head while pushing hundreds of gallons per minute through interconnected branch lines, cross mains, risers, backflow preventers, and underground yard piping.</p>

          <h2>The Hazen-Williams Friction Loss Equation & Fluid Mechanics</h2>
          <p>Unlike civil engineering open-channel flows or chemical process pipelines operating across turbulent transition zones where the Darcy-Weisbach equation dominates, fire protection engineering universally adopts the empirical <strong>Hazen-Williams formula</strong>. This equation specifically models water flow through pressurized circular conduits between 40&deg;F and 75&deg;F (4&deg;C to 24&deg;C):</p>

          <div class="formula-box">
            $$p = \frac{4.52 \cdot Q^{1.85}}{C^{1.85} \cdot d^{4.87}}$$
          </div>

          <p>Where the hydraulic parameters are defined per NFPA 13 Section 27.2.2.1 as follows:</p>
          <ul>
            <li><strong>\(p\)</strong>: Frictional pressure loss per unit length of pipe, expressed in pounds per square inch per linear foot (\(\text{psi/ft}\)).</li>
            <li><strong>\(Q\)</strong>: Volumetric water discharge flow traversing the conduit, expressed in gallons per minute (\(\text{gpm}\)).</li>
            <li><strong>\(C\)</strong>: Hazen-Williams pipe roughness coefficient (dimensionless), reflecting internal boundary roughness and long-term corrosion resistance.</li>
            <li><strong>\(d\)</strong>: True internal pipe diameter (inside diameter, ID), expressed in inches (\(\text{in}\)). Note that nominal pipe sizes differ substantially from internal diameters (e.g., a 2-inch Schedule 40 steel pipe exhibits an ID of 2.067 inches).</li>
          </ul>

          <p>To calculate the cumulative friction loss (\(\Delta P_f\)) across a pipeline run containing valves, tees, and elbows, the unit friction gradient \(p\) is multiplied by the total equivalent length (\(L_{\text{equiv}}\)):</p>

          <div class="formula-box">
            $$\Delta P_f = p \cdot L_{\text{equiv}} = p \cdot \left( L_{\text{physical}} + \sum L_{\text{fittings}} \right)$$
          </div>

          <h2>Sprinkler Orifice Discharge: The K-Factor Equation</h2>
          <p>Every automatic fire sprinkler head acts as a calibrated hydraulic nozzle with a precision-machined discharge orifice. Water discharging across the deflector plate satisfies the classical Torricelli orifice flow relationship, parameterized via the sprinkler discharge coefficient, universally designated as the <strong>K-factor</strong>:</p>

          <div class="formula-box">
            $$Q = K \cdot \sqrt{P} \quad \Longleftrightarrow \quad P = \left( \frac{Q}{K} \right)^2$$
          </div>

          <p>Where \(Q\) represents discharge flow in gallons per minute (\(\text{gpm}\)), \(P\) is the operating gauge pressure at the sprinkler inlet in pounds per square inch (\(\text{psi}\)), and \(K\) is the manufacturer rated orifice coefficient (\(\text{gpm}/\sqrt{\text{psi}}\)).</p>

          <p>NFPA 13 establishes minimum operating thresholds to guarantee effective droplet atomization and droplet momentum capable of penetrating vigorous fire thermal updrafts:</p>
          <ul>
            <li><strong>Absolute Minimum Pressure:</strong> NFPA 13 Section 27.2.4.1 dictates that no standard spray sprinkler head shall operate at a pressure below <strong>7.0 psi (0.5 bar)</strong>, which yields a minimum discharge of 14.8 gpm for a standard \(K=5.6\) head.</li>
            <li><strong>Extended Coverage and Storage Sprinklers:</strong> High-density control mode specific application (CMSA) and early suppression fast response (ESFR) sprinkler heads typically mandate minimum starting pressures between <strong>25 psi and 75 psi</strong> depending on ceiling height, storage commodity classification, and listing parameters.</li>
          </ul>

          <h2>Equivalent Lengths of Fittings, Valves, and Devices</h2>
          <p>Fluid accelerating, dividing, and turning through elbows, tees, control valves, and strainers experiences substantial turbulent eddy dissipation and localized wall shear stress. NFPA 13 Table 27.2.3.1.1 standardizes these localized geometric disruptions by converting every individual fitting into an <em>equivalent length of straight pipe</em> of the same nominal diameter:</p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Nominal Pipe Size</th>
                <th>Standard 90&deg; Elbow (ft)</th>
                <th>45&deg; Elbow (ft)</th>
                <th>Tee (Turn into Branch) (ft)</th>
                <th>Gate Valve (ft)</th>
                <th>Butterfly Valve (ft)</th>
                <th>Swing Check Valve (ft)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>1" (25 mm)</td>
                <td>2</td>
                <td>1</td>
                <td>5</td>
                <td>0</td>
                <td>6</td>
                <td>5</td>
              </tr>
              <tr>
                <td>1-1/4" (32 mm)</td>
                <td>3</td>
                <td>1</td>
                <td>6</td>
                <td>0</td>
                <td>7</td>
                <td>7</td>
              </tr>
              <tr>
                <td>1-1/2" (40 mm)</td>
                <td>4</td>
                <td>2</td>
                <td>8</td>
                <td>0</td>
                <td>10</td>
                <td>9</td>
              </tr>
              <tr>
                <td>2" (50 mm)</td>
                <td>5</td>
                <td>2</td>
                <td>10</td>
                <td>1</td>
                <td>12</td>
                <td>11</td>
              </tr>
              <tr>
                <td>2-1/2" (65 mm)</td>
                <td>6</td>
                <td>3</td>
                <td>12</td>
                <td>1</td>
                <td>15</td>
                <td>14</td>
              </tr>
              <tr>
                <td>3" (80 mm)</td>
                <td>7</td>
                <td>3</td>
                <td>15</td>
                <td>1</td>
                <td>19</td>
                <td>16</td>
              </tr>
              <tr>
                <td>4" (100 mm)</td>
                <td>10</td>
                <td>4</td>
                <td>20</td>
                <td>2</td>
                <td>21</td>
                <td>22</td>
              </tr>
              <tr>
                <td>6" (150 mm)</td>
                <td>14</td>
                <td>6</td>
                <td>30</td>
                <td>3</td>
                <td>36</td>
                <td>32</td>
              </tr>
            </tbody>
          </table>

          <h2>Hazen-Williams Roughness Coefficients (C-Factors)</h2>
          <p>The \(C\)-factor dictates pipe carrying efficiency. A higher \(C\)-factor denotes a smoother internal lumen, producing significantly lower friction losses. As specified in NFPA 13 Table 27.2.4.8.1:</p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Piping Material</th>
                <th>Hazen-Williams C-Factor</th>
                <th>Primary Application and Code Constraints</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Black Steel (Wet System)</td>
                <td>120</td>
                <td>Standard wet pipe commercial/industrial distribution systems.</td>
              </tr>
              <tr>
                <td>Black Steel (Dry / Preaction)</td>
                <td>100</td>
                <td>Dry systems subjected to cyclic oxygen and moisture, accelerating internal tuberculation.</td>
              </tr>
              <tr>
                <td>Galvanized Steel (Wet System)</td>
                <td>120</td>
                <td>Wet installations requiring atmospheric corrosion defense.</td>
              </tr>
              <tr>
                <td>Galvanized Steel (Dry System)</td>
                <td>100</td>
                <td>Dry and preaction systems (restricted by recent NFPA 13 editions due to pinhole leaks).</td>
              </tr>
              <tr>
                <td>Copper Tube (Type K, L, M)</td>
                <td>150</td>
                <td>Residential, institutional, and healthcare wet pipe distribution.</td>
              </tr>
              <tr>
                <td>Chlorinated Polyvinyl Chloride (CPVC)</td>
                <td>150</td>
                <td>Light Hazard occupancies and NFPA 13R/13D residential systems.</td>
              </tr>
              <tr>
                <td>Cement-Lined Ductile Iron</td>
                <td>140</td>
                <td>Underground fire service supply mains and yard loops.</td>
              </tr>
            </tbody>
          </table>

          <h2>Fluid Velocity Limits & Static Elevation Head</h2>
          <p>Water velocity inside fire sprinkler piping must be monitored during hydraulic design to prevent severe pipe erosion, excessive pressure surges (water hammer), and destructive acoustic vibration. The mean linear fluid velocity is computed from volumetric discharge and pipe geometry:</p>

          <div class="formula-box">
            $$v = \frac{0.408 \cdot Q}{d^2}$$
          </div>

          <p>Where \(v\) is in feet per second (\(\text{ft/s}\)), \(Q\) is in \(\text{gpm}\), and \(d\) is inside diameter in inches. While NFPA 13 does not enforce an arbitrary upper velocity ceiling for standard tree systems, professional engineering practice and insurer standards (FM Global Datasheet 2-0) strongly advise restricting branch line velocities below <strong>20 ft/s (6.1 m/s)</strong> and main/feed riser velocities below <strong>15 ft/s (4.6 m/s)</strong> to mitigate cavitation and water hammer.</p>

          <p>Furthermore, vertical elevation differences between water sources, pumps, and elevated heads create static hydrostatic pressure variations governed by water density:</p>

          <div class="formula-box">
            $$\Delta P_{\text{elev}} = 0.4335 \cdot \Delta h$$
          </div>

          <p>Where \(\Delta h\) is the vertical elevation rise in feet. Pumping water upward incurs an unavoidable static pressure penalty of <strong>0.433 psi per foot of rise</strong> (or 43.35 psi per 100 feet). When analyzing multi-story buildings, this static head requirement frequently constitutes over 40% of the total fire pump discharge pressure requirement.</p>

          <div class="worked-example-card">
            <h3>Step-by-Step Worked Case Study: Light Hazard Office Branch Line</h3>
            <p><strong>Design Scenario:</strong> An engineer is sizing a 1-1/2" Schedule 40 black steel wet branch line feeding 4 hydraulically remote \(K=5.6\) standard spray sprinklers in a modern commercial office building (Light Hazard, design density \(0.10\text{ gpm/ft}^2\)).</p>
            <ul>
              <li>Physical pipe run length: \(L = 60\text{ ft}\).</li>
              <li>Fittings: Two 90&deg; standard elbows and one tee (flow turned through branch).</li>
              <li>Pipe: 1-1/2" Schedule 40 black steel (\(d = 1.610\text{ in}\), \(C = 120\)).</li>
              <li>Remote sprinkler head minimum operating pressure: \(P_{\text{head}} = 7.0\text{ psi}\).</li>
              <li>Elevation rise from cross main to sprinkler heads: \(\Delta h = 12\text{ ft}\).</li>
            </ul>

            <p><strong>Step 1: Calculate remote head discharge flow rate (\(Q_{\text{head}}\))</strong></p>
            <div class="formula-box">
              $$Q_{\text{head}} = K \cdot \sqrt{P} = 5.6 \cdot \sqrt{7.0} = 5.6 \cdot 2.6458 = 14.82\text{ gpm}$$
            </div>

            <p><strong>Step 2: Total cumulative flow traversing branch line (\(Q_{\text{total}}\))</strong></p>
            <div class="formula-box">
              $$Q_{\text{total}} = 4 \times 14.82\text{ gpm} = 59.28\text{ gpm}$$
            </div>

            <p><strong>Step 3: Determine total equivalent length (\(L_{\text{total}}\))</strong></p>
            <p>From NFPA 13 Table 27.2.3.1.1 for 1-1/2" fittings:</p>
            <ul>
              <li>Two 90&deg; elbows: \(2 \times 4\text{ ft} = 8\text{ ft}\)</li>
              <li>One tee (turn into branch): \(1 \times 8\text{ ft} = 8\text{ ft}\)</li>
              <li>Total Equivalent Length: \(L_{\text{total}} = 60\text{ ft} + 8\text{ ft} + 8\text{ ft} = 76.0\text{ ft}\)</li>
            </ul>

            <p><strong>Step 4: Compute Hazen-Williams friction gradient (\(p\))</strong></p>
            <div class="formula-box">
              $$p = \frac{4.52 \cdot (59.28)^{1.85}}{(120)^{1.85} \cdot (1.610)^{4.87}} = \frac{4.52 \cdot 1899.41}{7060.78 \cdot 10.124} = \frac{8585.33}{71483.3} = 0.1201\text{ psi/ft}$$
            </div>

            <p><strong>Step 5: Compute total friction loss (\(\Delta P_f\)) and fluid velocity (\(v\))</strong></p>
            <div class="formula-box">
              $$\Delta P_f = p \cdot L_{\text{total}} = 0.1201\text{ psi/ft} \cdot 76.0\text{ ft} = 9.13\text{ psi}$$
              $$v = \frac{0.408 \cdot 59.28}{(1.610)^2} = \frac{24.186}{2.592} = 9.33\text{ ft/s}$$
            </div>
            <p>The velocity of 9.33 ft/s is well within the acceptable 20 ft/s threshold for branch lines.</p>

            <p><strong>Step 6: Compute elevation static pressure penalty (\(\Delta P_{\text{elev}}\))</strong></p>
            <div class="formula-box">
              $$\Delta P_{\text{elev}} = 0.433 \cdot 12\text{ ft} = 5.20\text{ psi}$$
            </div>

            <p><strong>Step 7: Total required hydraulic pressure at branch supply inlet (\(P_{\text{total}}\))</strong></p>
            <div class="formula-box">
              $$P_{\text{total}} = P_{\text{head}} + \Delta P_f + \Delta P_{\text{elev}} = 7.0 + 9.13 + 5.20 = 21.33\text{ psi}$$
            </div>
            <p><strong>Engineering Conclusion:</strong> The branch supply connection must supply at least <strong>59.3 gpm at 21.4 psi</strong> to satisfy NFPA 13 minimum discharge criteria.</p>
          </div>

          <h2>Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3>What is the difference between Pipe Schedule systems and Hydraulically Calculated systems?</h3>
            <p>Pipe schedule systems determine pipe sizes purely based on pre-established historical lookup tables that specify the maximum number of sprinkler heads permitted on a given pipe size (e.g., 2 heads on 1", 3 heads on 1-1/4", 5 heads on 1-1/2"). In contrast, hydraulically calculated systems use fluid mechanics, Hazen-Williams friction equations, actual water supply flow test curves, and K-factors to optimize pipe diameters, frequently resulting in smaller pipe sizes, reduced structural loads, and substantial material cost savings.</p>
          </div>

          <div class="faq-item">
            <h3>Why does dry pipe steel have a lower Hazen-Williams C-factor (100) than wet pipe (120)?</h3>
            <p>Dry pipe and preaction systems contain pressurized air or nitrogen during standby. When condensation collects or during quarterly trip tests, moisture combines with atmospheric oxygen, accelerating internal oxidation, pitting, and ferric tuberculation. NFPA 13 mandates a conservative \(C = 100\) to account for this long-term surface degradation, which increases internal pipe roughness and hydraulic resistance.</p>
          </div>

          <div class="faq-item">
            <h3>How do ESFR sprinklers differ hydraulically from standard spray sprinklers?</h3>
            <p>Early Suppression Fast Response (ESFR) sprinklers feature massive discharge orifices (\(K=14.0\) to \(K=25.2\)) and operate at high pressures (typically 25 to 75 psi). Rather than merely controlling a warehouse storage fire by wetting surrounding goods until firefighters arrive, ESFR heads discharge high-momentum, large-droplet water streams that penetrate severe convective fire plumes directly to extinguish high-piled palletized and rack storage fires without requiring in-rack sprinklers.</p>
          </div>

          <div class="faq-item">
            <h3>What is velocity pressure and when must it be included in fire sprinkler hydraulic calculations?</h3>
            <p>Velocity pressure (\(P_v = 0.001123 \cdot Q^2 / d^4\)) represents the kinetic energy of water moving through the conduit. NFPA 13 allows velocity pressure to be neglected in standard branch line and cross main calculations (treating normal static pressure as total pressure), which provides an inherent conservative safety factor. However, velocity pressure must be accounted for when performing complex computerized network loops, grid systems, or velocity head recovery analyses.</p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar" id="toolSidebar">
        <!-- Dynamically injected category links -->
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; 2026 CalcHub. All rights reserved. Engineering and mathematical tools grounded in international standards.</p>
      <ul class="footer-links">
        <li><a href="index.html">Home</a></li>
        <li><a href="fire-safety.html">Fire Safety</a></li>
        <li><a href="ohms-law-calculator.html">Ohm's Law</a></li>
        <li><a href="sitemap.xml">Sitemap</a></li>
      </ul>
    </div>
  </footer>

  <script>
    // Fitting equivalent lengths lookup table (NFPA 13 Table 27.2.3.1.1)
    // Mapping nominal sizes to equivalent lengths for: [elbow90, teeBranch]
    const FITTING_TABLE = {
      "1.049": { elbow: 2, tee: 5 },
      "1.380": { elbow: 3, tee: 6 },
      "1.610": { elbow: 4, tee: 8 },
      "2.067": { elbow: 5, tee: 10 },
      "2.469": { elbow: 6, tee: 12 },
      "3.068": { elbow: 7, tee: 15 },
      "4.026": { elbow: 10, tee: 20 },
      "6.065": { elbow: 14, tee: 30 }
    };

    const kFactorSelect = document.getElementById('kFactor');
    const customKGroup = document.getElementById('customKGroup');
    const customKInput = document.getElementById('customK');
    const flowModeSelect = document.getElementById('flowMode');
    const headPressGroup = document.getElementById('headPressGroup');
    const headFlowGroup = document.getElementById('headFlowGroup');
    const headPressInput = document.getElementById('headPress');
    const headFlowInput = document.getElementById('headFlow');
    const numHeadsInput = document.getElementById('numHeads');
    const pipeSizeSelect = document.getElementById('pipeSize');
    const pipeLengthInput = document.getElementById('pipeLength');
    const cFactorSelect = document.getElementById('cFactor');
    const numElbowsInput = document.getElementById('numElbows');
    const numTeesInput = document.getElementById('numTees');
    const elevChangeInput = document.getElementById('elevChange');

    const sprinklerResultBox = document.getElementById('sprinklerResultBox');
    const resTotalPress = document.getElementById('resTotalPress');
    const resHeadFlow = document.getElementById('resHeadFlow');
    const resHeadPress = document.getElementById('resHeadPress');
    const resTotalFlow = document.getElementById('resTotalFlow');
    const resEquivLength = document.getElementById('resEquivLength');
    const resFrictionLoss = document.getElementById('resFrictionLoss');
    const resGradient = document.getElementById('resGradient');
    const resVelocity = document.getElementById('resVelocity');
    const resElevHead = document.getElementById('resElevHead');
    const velocityWarning = document.getElementById('velocityWarning');

    kFactorSelect.addEventListener('change', function() {
      if (this.value === 'custom') {
        customKGroup.style.display = 'block';
      } else {
        customKGroup.style.display = 'none';
      }
      calculateHydraulics();
    });

    flowModeSelect.addEventListener('change', function() {
      if (this.value === 'headPress') {
        headPressGroup.style.display = 'block';
        headFlowGroup.style.display = 'none';
      } else {
        headPressGroup.style.display = 'none';
        headFlowGroup.style.display = 'block';
      }
      calculateHydraulics();
    });

    function calculateHydraulics() {
      let K = (kFactorSelect.value === 'custom') ? parseFloat(customKInput.value) : parseFloat(kFactorSelect.value);
      if (isNaN(K) || K <= 0) K = 5.6;

      const flowMode = flowModeSelect.value;
      let P_head = 7.0;
      let Q_head = 14.8;

      if (flowMode === 'headPress') {
        P_head = parseFloat(headPressInput.value);
        if (isNaN(P_head) || P_head <= 0) P_head = 7.0;
        Q_head = K * Math.sqrt(P_head);
      } else {
        Q_head = parseFloat(headFlowInput.value);
        if (isNaN(Q_head) || Q_head <= 0) Q_head = 14.8;
        P_head = Math.pow(Q_head / K, 2);
      }

      let numHeads = parseInt(numHeadsInput.value, 10);
      if (isNaN(numHeads) || numHeads < 1) numHeads = 1;

      const Q_total = numHeads * Q_head;

      const d = parseFloat(pipeSizeSelect.value);
      let physicalLength = parseFloat(pipeLengthInput.value);
      if (isNaN(physicalLength) || physicalLength < 0) physicalLength = 0;

      const C = parseFloat(cFactorSelect.value);

      let elbows = parseInt(numElbowsInput.value, 10);
      if (isNaN(elbows) || elbows < 0) elbows = 0;

      let tees = parseInt(numTeesInput.value, 10);
      if (isNaN(tees) || tees < 0) tees = 0;

      const fittingKey = pipeSizeSelect.value;
      const fittingData = FITTING_TABLE[fittingKey] || { elbow: 4, tee: 8 };
      const eqFittings = (elbows * fittingData.elbow) + (tees * fittingData.tee);
      const L_equiv = physicalLength + eqFittings;

      // Hazen-Williams friction gradient (psi per ft)
      // p = 4.52 * Q^1.85 / (C^1.85 * d^4.87)
      const numerator = 4.52 * Math.pow(Q_total, 1.85);
      const denominator = Math.pow(C, 1.85) * Math.pow(d, 4.87);
      const p_gradient = numerator / denominator;
      const P_friction = p_gradient * L_equiv;

      // Water Velocity: v = 0.408 * Q / d^2 (ft/s)
      const velocity = (0.408 * Q_total) / Math.pow(d, 2);

      // Elevation head: deltaP = 0.433 * deltaH
      let elevChange = parseFloat(elevChangeInput.value);
      if (isNaN(elevChange)) elevChange = 0;
      const P_elev = 0.433 * elevChange;

      // Total required pressure at supply
      const P_total = Math.max(0, P_head + P_friction + P_elev);

      resTotalPress.textContent = P_total.toFixed(2) + " psi";
      resHeadFlow.textContent = Q_head.toFixed(2) + " gpm";
      resHeadPress.textContent = P_head.toFixed(2) + " psi";
      resTotalFlow.textContent = Q_total.toFixed(2) + " gpm";
      resEquivLength.textContent = L_equiv.toFixed(1) + " ft (incl. " + eqFittings + " ft fittings)";
      resFrictionLoss.textContent = P_friction.toFixed(2) + " psi";
      resGradient.textContent = p_gradient.toFixed(4) + " psi/ft";
      resVelocity.textContent = velocity.toFixed(2) + " ft/s";
      resElevHead.textContent = (P_elev >= 0 ? "+" : "") + P_elev.toFixed(2) + " psi (" + elevChange + " ft)";

      if (velocity > 20.0) {
        velocityWarning.style.display = 'block';
        velocityWarning.innerHTML = `<strong>High Velocity Warning:</strong> Water velocity of <strong>${velocity.toFixed(1)} ft/s</strong> exceeds the standard NFPA/FM recommendation of 20 ft/s for branch lines. Consider stepping up to a larger nominal pipe diameter to avoid internal pipe erosion and destructive water hammer.`;
      } else {
        velocityWarning.style.display = 'none';
      }

      sprinklerResultBox.style.display = 'block';
    }

    document.getElementById('calcBtn').addEventListener('click', calculateHydraulics);
    document.getElementById('resetBtn').addEventListener('click', function() {
      setTimeout(calculateHydraulics, 50);
    });

    // Auto-calculate on initial load
    window.addEventListener('DOMContentLoaded', calculateHydraulics);
  </script>
</body>
</html>
"""

TOOL_8_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Strobe Candela Calculator | NFPA 72 Visual Notification Appliance Sizing</title>
  <meta name="description" content="Calculate fire alarm strobe candela ratings and visual appliance coverage per NFPA 72 and UL 1971 standards. Determines required wall-mounted and ceiling-mounted candela, corridor spacing, and sleeping area candela.">
  <link rel="canonical" href="https://calchub.cloud/strobe-candela-calculator.html">
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
        "name": "Strobe Candela Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Life safety visual notification calculation tool sizing fire alarm strobe candela ratings for rooms, corridors, and sleeping areas per NFPA 72 Chapter 18 and UL 1971.",
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
            "name": "How is fire alarm strobe candela determined for a room per NFPA 72?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "NFPA 72 Table 18.5.5.4.1(a) dictates the minimum effective candela rating based on room dimensions. A single wall-mounted strobe centered on a wall requires 15 cd for a 20x20 ft room, 30 cd for 30x30 ft, 60 cd for 40x40 ft, 95 cd for 50x50 ft, and up to 185 cd for 70x70 ft. If ceiling-mounted, candela ratings are governed by Table 18.5.5.4.1(b), which accounts for ceiling heights up to 30 feet."
            }
          },
          {
            "@type": "Question",
            "name": "What are the NFPA 72 candela requirements for sleeping areas?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Per NFPA 72 Section 18.5.5.7, visual appliances installed in sleeping rooms to awaken hearing-impaired occupants must deliver significantly higher luminous intensity: Wall-mounted strobes located 24 inches or less from the ceiling must be rated at least 110 cd (or 177 cd if mounted more than 24 inches below the ceiling); ceiling-mounted strobes must provide 177 cd for ceiling heights up to 10 feet."
            }
          },
          {
            "@type": "Question",
            "name": "What is the maximum spacing between fire alarm strobes in corridors?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Per NFPA 72 Section 18.5.5.5, visual notification appliances in corridors up to 20 feet wide must be rated at least 15 cd, positioned no more than 100 feet apart, and located within 15 feet of each end of the corridor. Any change in corridor direction requires an additional visual appliance."
            }
          },
          {
            "@type": "Question",
            "name": "Why is strobe synchronization mandatory when multiple strobes are visible?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "NFPA 72 Section 18.5.5.4.2 mandates that whenever two or more strobes are located within the same field of view, they must be synchronized within 10 milliseconds. Unsynchronized flashing at combined frequencies between 2 Hz and 60 Hz can trigger photo-sensitive epileptic seizures under the Americans with Disabilities Act (ADA) and UL 1971 standards."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="fire">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo"><span class="logo-icon">&pi;</span><span class="logo-text">Calc<strong>Hub</strong></span></a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="engineering.html">Engineering</a>
        <a href="solar-energy.html">Solar</a>
        <a href="fire-safety.html" class="active">Fire Safety</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo; <a href="fire-safety.html">Fire Safety</a> &rsaquo; <span>Strobe Candela Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">NFPA 72 Chapter 18 &amp; UL 1971 Photometric Standards</div>
          <h1 class="calc-title">Strobe Candela Calculator</h1>
          <p class="calc-tagline">Calculate visual notification appliance candela ratings, coverage boundaries, and current loads for rooms, corridors, and sleeping quarters per NFPA 72 Chapter 18 and UL 1971 standards.</p>
        </header>

        <div class="tool-card">
          <form id="strobeCalcForm">
            <div class="calc-grid">
              <div class="form-group">
                <label for="roomType">Application & Occupancy Type</label>
                <select id="roomType">
                  <option value="nonSleeping" selected>Standard Non-Sleeping Room (Office, Classroom, Retail)</option>
                  <option value="sleeping">Sleeping Area (Hotel, Dormitory, Patient Room)</option>
                  <option value="corridor">Corridor / Hallway (&le; 20 ft wide)</option>
                </select>
              </div>

              <div class="form-group" id="mountConfigGroup">
                <label for="mountConfig">Mounting Location & Configuration</label>
                <select id="mountConfig">
                  <option value="wallSingle" selected>Single Wall-Mount (Centered on Wall)</option>
                  <option value="wallTwo">Two Wall-Mount Strobes (Opposite Walls)</option>
                  <option value="wallFour">Four Wall-Mount Strobes (One per Wall)</option>
                  <option value="ceilingCenter">Ceiling Mount (Centered in Room)</option>
                </select>
              </div>

              <div class="form-group" id="roomLengthGroup">
                <label for="roomLength">Room Length [feet]</label>
                <input type="number" id="roomLength" step="1" min="5" max="150" value="30">
              </div>

              <div class="form-group" id="roomWidthGroup">
                <label for="roomWidth">Room Width [feet]</label>
                <input type="number" id="roomWidth" step="1" min="5" max="150" value="30">
              </div>

              <div class="form-group" id="ceilingHeightGroup">
                <label for="ceilingHeight">Ceiling Height [feet]</label>
                <select id="ceilingHeight">
                  <option value="10" selected>Up to 10 ft (Standard Ceiling)</option>
                  <option value="20">Up to 20 ft (Medium High Ceiling)</option>
                  <option value="30">Up to 30 ft (High Industrial / Auditorium Ceiling)</option>
                </select>
              </div>

              <div class="form-group" id="corridorLengthGroup" style="display: none;">
                <label for="corridorLength">Corridor Length [feet]</label>
                <input type="number" id="corridorLength" step="5" min="10" max="1000" value="120">
              </div>

              <div class="form-group">
                <label for="operatingVoltage">Strobe Operating Circuit Voltage</label>
                <select id="operatingVoltage">
                  <option value="24" selected>24 VDC Regulated NAC (Standard Commercial)</option>
                  <option value="12">12 VDC Regulated NAC (Specialty / Legacy)</option>
                </select>
              </div>
            </div>

            <div class="calc-actions">
              <button type="button" id="calcStrobeBtn" class="btn btn-primary">Calculate Strobe Candela</button>
              <button type="reset" id="resetStrobeBtn" class="btn btn-secondary">Reset Defaults</button>
            </div>
          </form>

          <div id="strobeResultBox" class="results-container" style="display: none;">
            <h3>Visual Notification Sizing Results</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label">Minimum Required Rating (Each Strobe)</span>
                <span id="resCandelaEach" class="result-value">-- cd</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Number of Appliances Required</span>
                <span id="resNumStrobes" class="result-value">-- units</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Total Candela Output</span>
                <span id="resTotalCandela" class="result-value">-- cd</span>
              </div>
              <div class="result-tile">
                <span class="result-label">NFPA 72 Standard Rating Tier</span>
                <span id="resRatingTier" class="result-value">--</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Maximum Corner Distance</span>
                <span id="resCornerDist" class="result-value">-- ft</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Estimated Current per Appliance</span>
                <span id="resCurrentEach" class="result-value">-- mA</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Total NAC Current Draw</span>
                <span id="resTotalCurrent" class="result-value">-- A</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Synchronization Status</span>
                <span id="resSyncRequired" class="result-value">--</span>
              </div>
            </div>
            <div id="strobeNotesBox" style="margin-top: 1rem; color: #1e40af; background: #eff6ff; border: 1px solid #bfdbfe; padding: 0.75rem; border-radius: 6px;"></div>
          </div>
        </div>

        <article class="article-body">
          <h2>Photometric Engineering and Visual Notification Appliance Fundamentals</h2>
          <p>Fire alarm visual notification appliances (strobes) deliver high-intensity, pulsed optical energy to alert occupants of immediate life safety hazards, smoke, or fire conditions. In spaces occupied by hearing-impaired individuals or in environments featuring ambient noise levels exceeding 85 dBA (such as mechanical rooms, manufacturing floors, and data centers), visual appliances represent the primary means of egress notification under the <strong>Americans with Disabilities Act (ADA)</strong> and <strong>NFPA 72</strong> (<em>National Fire Alarm and Signaling Code</em>).</p>

          <p>Unlike continuous architectural lighting measured in average lux or lumens, fire alarm strobes are characterized by their <strong>effective intensity</strong>, measured in candela (\(\text{cd}\)). Sizing strobes requires precise matching of room geometry, viewing angle, ceiling height, and flash synchronization to satisfy mandatory minimum boundary illuminance thresholds without inducing harmful optical reflections or photosensitive epileptic reactions.</p>

          <h2>NFPA 72 Candela Tables & Geometric Coverage Rules</h2>
          <p>NFPA 72 Chapter 18 establishes two distinct design methodologies for sizing visual notification appliances: the prescriptive <strong>Table Method</strong> and the engineered <strong>Performance-Based (Inverse Square) Method</strong>. The Table Method is universally favored for standard commercial and institutional architecture.</p>

          <p>For standard rectangular or square spaces, the design dimension is dictated by the <em>maximum room dimension</em> (the longer wall). If a room measures 24 ft by 38 ft, it must be evaluated as a 40 ft by 40 ft room to guarantee compliance across all boundary extremities.</p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Maximum Room Dimensions (ft)</th>
                <th>Single Wall-Mount Strobe (cd)</th>
                <th>Two Wall-Mount Strobes (cd each)</th>
                <th>Four Wall-Mount Strobes (cd each)</th>
                <th>Ceiling Mount (up to 10 ft) (cd)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>20 &times; 20 (6.1 &times; 6.1 m)</td>
                <td>15</td>
                <td>N/A</td>
                <td>N/A</td>
                <td>15</td>
              </tr>
              <tr>
                <td>30 &times; 30 (9.1 &times; 9.1 m)</td>
                <td>30</td>
                <td>15</td>
                <td>N/A</td>
                <td>30</td>
              </tr>
              <tr>
                <td>40 &times; 40 (12.2 &times; 12.2 m)</td>
                <td>60</td>
                <td>30</td>
                <td>15</td>
                <td>60</td>
              </tr>
              <tr>
                <td>50 &times; 50 (15.2 &times; 15.2 m)</td>
                <td>95</td>
                <td>60</td>
                <td>30</td>
                <td>95</td>
              </tr>
              <tr>
                <td>60 &times; 60 (18.3 &times; 18.3 m)</td>
                <td>135</td>
                <td>95</td>
                <td>30</td>
                <td>115</td>
              </tr>
              <tr>
                <td>70 &times; 70 (21.3 &times; 21.3 m)</td>
                <td>185</td>
                <td>115</td>
                <td>60</td>
                <td>150</td>
              </tr>
              <tr>
                <td>80 &times; 80 (24.4 &times; 24.4 m)</td>
                <td>N/A (Multi-strobe required)</td>
                <td>135</td>
                <td>60</td>
                <td>177</td>
              </tr>
              <tr>
                <td>100 &times; 100 (30.5 &times; 30.5 m)</td>
                <td>N/A (Multi-strobe required)</td>
                <td>185</td>
                <td>95</td>
                <td>N/A (Subdivide space)</td>
              </tr>
            </tbody>
          </table>

          <h2>Ceiling-Mounted Strobe Derating for High Ceilings</h2>
          <p>When strobes are installed on elevated ceilings, optical energy dissipates significantly before illuminating occupant eye level (defined at 5.5 feet above the finished floor). NFPA 72 Table 18.5.5.4.1(b) establishes stringent candela upgrades for ceiling heights of 10 ft, 20 ft, and 30 ft:</p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Room Dimensions (ft)</th>
                <th>Ceiling Height &le; 10 ft</th>
                <th>Ceiling Height &le; 20 ft</th>
                <th>Ceiling Height &le; 30 ft</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>20 &times; 20</td>
                <td>15 cd</td>
                <td>30 cd</td>
                <td>55 cd</td>
              </tr>
              <tr>
                <td>30 &times; 30</td>
                <td>30 cd</td>
                <td>45 cd</td>
                <td>75 cd</td>
              </tr>
              <tr>
                <td>40 &times; 40</td>
                <td>60 cd</td>
                <td>80 cd</td>
                <td>115 cd</td>
              </tr>
              <tr>
                <td>50 &times; 50</td>
                <td>95 cd</td>
                <td>115 cd</td>
                <td>150 cd</td>
              </tr>
              <tr>
                <td>60 &times; 60</td>
                <td>115 cd</td>
                <td>150 cd</td>
                <td>185 cd</td>
              </tr>
              <tr>
                <td>70 &times; 70</td>
                <td>150 cd</td>
                <td>177 cd</td>
                <td>N/A (Use Wall Mounts)</td>
              </tr>
              <tr>
                <td>80 &times; 80</td>
                <td>177 cd</td>
                <td>N/A</td>
                <td>N/A</td>
              </tr>
            </tbody>
          </table>

          <h2>UL 1971 Polar Dispersion & Illuminance Thresholds</h2>
          <p>Every commercial fire alarm strobe sold in North America must comply with <strong>UL 1971</strong> (<em>Standard for Signaling Devices for the Hearing Impaired</em>). UL 1971 dictates that a strobe must produce an instantaneous direct illuminance of at least <strong>0.0375 foot-candles (lumens per square foot)</strong> or <strong>0.404 lux</strong> at every point across the coverage boundary.</p>

          <p>The inverse square law governs optical attenuation through clear air:</p>

          <div class="formula-box">
            $$E = \frac{I_v}{D^2} \ge 0.0375\text{ ft-c}$$
          </div>

          <p>Where \(I_v\) represents effective candela intensity along the observation axis, and \(D\) is the straight-line Euclidean distance from the strobe lens to the farthest corner point:</p>

          <div class="formula-box">
            $$D = \sqrt{\left(\frac{L}{2}\right)^2 + \left(\frac{W}{2}\right)^2 + H_{\text{eff}}^2}$$
          </div>

          <p>Because xenon flash tubes and high-output LED strobes do not radiate light uniformly, UL 1971 enforces a standardized polar distribution curve. When viewed from an off-axis angle of 45&deg; (such as looking up from a room corner toward a center-wall strobe), the appliance is allowed to emit only 75% of its on-axis rating. At 90&deg; perpendicular, output may drop to 25%. The NFPA 72 tables account directly for these angular roll-offs.</p>

          <h2>Sleeping Area Requirements: High-Intensity Awakening Standards</h2>
          <p>Sleeping individuals require substantially greater optical excitation to be aroused from deep rapid-eye-movement (REM) sleep. NFPA 72 Section 18.5.5.7 enforces strict elevated candela standards in hotel guest rooms, college dormitories, and hospital residential quarters:</p>
          <ul>
            <li><strong>Wall-Mounted Near Ceiling:</strong> If mounted within 24 inches (610 mm) of the ceiling, the strobe must deliver a minimum of <strong>110 cd</strong>.</li>
            <li><strong>Wall-Mounted Lower on Wall:</strong> If mounted more than 24 inches below the ceiling, the strobe must deliver a minimum of <strong>177 cd</strong>.</li>
            <li><strong>Ceiling-Mounted in Sleeping Rooms:</strong> For ceiling heights up to 10 feet, the strobe must be rated at least <strong>177 cd</strong>.</li>
            <li><strong>Proximity Rule:</strong> In all cases, the visual notification appliance in a sleeping room must be installed within <strong>16 feet (4.9 meters)</strong> horizontal distance of the pillow location.</li>
          </ul>

          <h2>Corridor Notification Appliance Spacing Rules</h2>
          <p>Corridors exhibit narrow, elongated aspect ratios where standard room square tables do not apply. NFPA 72 Section 18.5.5.5 provides dedicated corridor rules:</p>
          <ul>
            <li><strong>Maximum Width:</strong> Applicable to corridors with a maximum width of <strong>20 feet (6.1 m)</strong>.</li>
            <li><strong>Minimum Candela Rating:</strong> Every corridor strobe must have a minimum rating of <strong>15 cd</strong>.</li>
            <li><strong>Maximum Spacing:</strong> Strobes must not be spaced greater than <strong>100 feet (30.5 m)</strong> apart along the corridor length.</li>
            <li><strong>End-of-Corridor Setback:</strong> A strobe must be installed within <strong>15 feet (4.6 m)</strong> of each corridor termination or end wall.</li>
            <li><strong>Turns and Intersections:</strong> Every change in corridor direction (such as an L-turn, T-junction, or cross intersection) requires an additional strobe positioned to illuminate both intersecting legs.</li>
          </ul>

          <h2>Synchronization and Circuit Loading Constraints</h2>
          <p>Flash synchronization is an essential life safety requirement. Under NFPA 72 Section 18.5.5.4.2, whenever two or more visual appliances are within the same field of view, their flash cycles must be synchronized within <strong>10 milliseconds</strong> of each other. If unsynchronized strobes flash independently, their combined visual pulse frequency can exceed 2 flashes per second (2 Hz), entering the 3 Hz to 60 Hz danger band capable of triggering photosensitive epileptic seizures.</p>

          <p>Furthermore, higher candela ratings exponentially increase current draw on the 24VDC Notification Appliance Circuit (NAC). The table below lists typical regulated 24VDC RMS operating currents across standard candela settings:</p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Candela Setting (cd)</th>
                <th>UL Regulated 24VDC Current (mA)</th>
                <th>Max Strobes on a 2.0 A NAC (with 20% Headroom)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>15 cd</td>
                <td>38 &ndash; 43 mA</td>
                <td>~37 appliances</td>
              </tr>
              <tr>
                <td>30 cd</td>
                <td>58 &ndash; 63 mA</td>
                <td>~25 appliances</td>
              </tr>
              <tr>
                <td>75 cd</td>
                <td>102 &ndash; 115 mA</td>
                <td>~14 appliances</td>
              </tr>
              <tr>
                <td>95 cd / 110 cd</td>
                <td>145 &ndash; 165 mA</td>
                <td>~10 appliances</td>
              </tr>
              <tr>
                <td>135 cd / 150 cd</td>
                <td>195 &ndash; 220 mA</td>
                <td>~7 appliances</td>
              </tr>
              <tr>
                <td>177 cd / 185 cd</td>
                <td>250 &ndash; 280 mA</td>
                <td>~5 appliances</td>
              </tr>
            </tbody>
          </table>

          <div class="worked-example-card">
            <h3>Step-by-Step Worked Case Study: Commercial Conference Room</h3>
            <p><strong>Design Scenario:</strong> An electrical engineer is laying out visual notification for an executive conference room measuring <strong>36 ft wide by 38 ft long</strong> with an <strong>11 ft finished ceiling</strong> in an unsprinklered commercial building.</p>

            <p><strong>Step 1: Determine Room Geometric Class</strong></p>
            <p>The maximum dimension is 38 ft. Under NFPA 72 Section 18.5.5.4.1, rooms must be rounded up to the next standard bracket in Table 18.5.5.4.1(a). Therefore, this room is classified as <strong>40 ft &times; 40 ft</strong>.</p>

            <p><strong>Step 2: Evaluate Layout Options</strong></p>
            <ul>
              <li><strong>Option A (Single Wall Mount):</strong> Table 18.5.5.4.1(a) requires a <strong>60 cd</strong> strobe centered on one of the 38 ft walls, mounted between 80 inches and 96 inches above the finished floor.</li>
              <li><strong>Option B (Single Ceiling Mount):</strong> Because the ceiling is 11 ft (which exceeds the 10 ft table tier), we must inspect Table 18.5.5.4.1(b) for &le; 20 ft ceilings. For a 40 &times; 40 ft room at 20 ft ceiling height, the required ceiling strobe rating is <strong>80 cd</strong> (standardized commercially to <strong>95 cd or 115 cd</strong>).</li>
              <li><strong>Option C (Two Wall Mounts):</strong> Two <strong>30 cd</strong> strobes mounted on opposite walls facing each other, with mandatory circuit synchronization.</li>
            </ul>

            <p><strong>Step 3: Calculate Circuit Current for Option A (Single 60 cd / 75 cd Strobe)</strong></p>
            <p>A typical multi-candela wall strobe set to 75 cd (the nearest standard commercial setting covering 60 cd) draws approximately <strong>105 mA at 24VDC</strong>. Choosing Option A saves installation labor and draws only 0.105 A of NAC capacity, leaving abundant power for downstream notification devices.</p>
          </div>

          <h2>Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3>What mounting height is required for wall-mounted strobes under NFPA 72?</h3>
            <p>NFPA 72 Section 18.5.5.1 mandates that wall-mounted visual notification appliances must be installed such that the entire lens is between <strong>80 inches (2.03 m) and 96 inches (2.44 m)</strong> above the finished floor. If ceiling heights are lower than 80 inches, the appliance must be mounted within 6 inches (150 mm) of the ceiling.</p>
          </div>

          <div class="faq-item">
            <h3>Can I use two 15 cd strobes to replace a single 30 cd strobe in a room?</h3>
            <p>Yes, provided the strobes are installed in accordance with NFPA 72 Table 18.5.5.4.1(a). For a 30 &times; 30 ft room, two 15 cd strobes positioned on opposite walls satisfy code. Both appliances must be synchronized within 10 ms to prevent seizure-inducing flash rates.</p>
          </div>

          <div class="faq-item">
            <h3>How do LED strobes differ hydraulically/electrically from traditional Xenon strobes?</h3>
            <p>Traditional xenon flash lamps rely on high-voltage capacitor discharges that create large instantaneous current spikes (inrush currents) and draw approximately 100&ndash;150 mA at 75 cd. Modern LED fire alarm strobes utilize pulse-width modulation (PWM) across solid-state emitters, reducing operating current by up to 50&ndash;70% (e.g., ~30&ndash;45 mA at 75 cd). This allows significantly more visual appliances per NAC circuit and smaller gauge wire.</p>
          </div>

          <div class="faq-item">
            <h3>Are visual strobes required inside individual private offices?</h3>
            <p>Model building codes (such as IBC Section 907.5.2.3.1) mandate visual appliances in public use areas and common use areas (lobbies, restrooms, conference rooms, break rooms, corridors). While individual private single-occupant offices are generally exempt from mandatory strobes upon initial construction, ADA Title III requires building owners to provide visual notification retrofits as a "reasonable accommodation" whenever requested by a deaf or hard-of-hearing employee.</p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar" id="toolSidebar">
        <!-- Dynamically injected category links -->
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; 2026 CalcHub. All rights reserved. Engineering and mathematical tools grounded in international standards.</p>
      <ul class="footer-links">
        <li><a href="index.html">Home</a></li>
        <li><a href="fire-safety.html">Fire Safety</a></li>
        <li><a href="ohms-law-calculator.html">Ohm's Law</a></li>
        <li><a href="sitemap.xml">Sitemap</a></li>
      </ul>
    </div>
  </footer>

  <script>
    // NFPA 72 Table 18.5.5.4.1(a) & (b) Candela Lookups
    const ROOM_WALL_TABLE = [
      { dim: 20, single: 15, two: 15, four: 15 },
      { dim: 30, single: 30, two: 15, four: 15 },
      { dim: 40, single: 60, two: 30, four: 15 },
      { dim: 50, single: 95, two: 60, four: 30 },
      { dim: 60, single: 135, two: 95, four: 30 },
      { dim: 70, single: 185, two: 115, four: 60 },
      { dim: 80, single: 240, two: 135, four: 60 },
      { dim: 100, single: 300, two: 185, four: 95 }
    ];

    const CEILING_TABLE = [
      { dim: 20, h10: 15, h20: 30, h30: 55 },
      { dim: 30, h10: 30, h20: 45, h30: 75 },
      { dim: 40, h10: 60, h20: 80, h30: 115 },
      { dim: 50, h10: 95, h20: 115, h30: 150 },
      { dim: 60, h10: 115, h20: 150, h30: 185 },
      { dim: 70, h10: 150, h20: 177, h30: 240 },
      { dim: 80, h10: 177, h20: 240, h30: 300 }
    ];

    // Current draw approximations per candela rating at 24VDC (mA)
    const CURRENT_MAP_24V = {
      15: 42,
      30: 62,
      45: 80,
      55: 90,
      60: 98,
      75: 112,
      80: 120,
      95: 148,
      110: 160,
      115: 168,
      135: 195,
      150: 210,
      177: 255,
      185: 265,
      240: 320,
      300: 380
    };

    const roomTypeSelect = document.getElementById('roomType');
    const mountConfigSelect = document.getElementById('mountConfig');
    const mountConfigGroup = document.getElementById('mountConfigGroup');
    const roomLengthGroup = document.getElementById('roomLengthGroup');
    const roomWidthGroup = document.getElementById('roomWidthGroup');
    const ceilingHeightGroup = document.getElementById('ceilingHeightGroup');
    const corridorLengthGroup = document.getElementById('corridorLengthGroup');
    const operatingVoltageSelect = document.getElementById('operatingVoltage');

    const roomLengthInput = document.getElementById('roomLength');
    const roomWidthInput = document.getElementById('roomWidth');
    const corridorLengthInput = document.getElementById('corridorLength');
    const ceilingHeightSelect = document.getElementById('ceilingHeight');

    const strobeResultBox = document.getElementById('strobeResultBox');
    const resCandelaEach = document.getElementById('resCandelaEach');
    const resNumStrobes = document.getElementById('resNumStrobes');
    const resTotalCandela = document.getElementById('resTotalCandela');
    const resRatingTier = document.getElementById('resRatingTier');
    const resCornerDist = document.getElementById('resCornerDist');
    const resCurrentEach = document.getElementById('resCurrentEach');
    const resTotalCurrent = document.getElementById('resTotalCurrent');
    const resSyncRequired = document.getElementById('resSyncRequired');
    const strobeNotesBox = document.getElementById('strobeNotesBox');

    roomTypeSelect.addEventListener('change', function() {
      const type = this.value;
      if (type === 'corridor') {
        corridorLengthGroup.style.display = 'block';
        roomLengthGroup.style.display = 'none';
        roomWidthGroup.style.display = 'none';
        ceilingHeightGroup.style.display = 'none';
        mountConfigGroup.style.display = 'none';
      } else {
        corridorLengthGroup.style.display = 'none';
        roomLengthGroup.style.display = 'block';
        roomWidthGroup.style.display = 'block';
        ceilingHeightGroup.style.display = 'block';
        mountConfigGroup.style.display = 'block';
      }
      calculateStrobe();
    });

    function calculateStrobe() {
      const type = roomTypeSelect.value;
      const voltage = parseFloat(operatingVoltageSelect.value);
      const voltageMult = (voltage === 12) ? 1.85 : 1.0;

      let candelaEach = 15;
      let numStrobes = 1;
      let ratingTier = "15 cd";
      let cornerDist = 0;
      let syncReq = "Not Mandatory (Single Strobe)";
      let notes = "";

      if (type === 'corridor') {
        let length = parseFloat(corridorLengthInput.value);
        if (isNaN(length) || length < 10) length = 10;
        // Corridor spacing: 15 cd strobes spaced <= 100 ft, within 15 ft of ends
        // If length <= 30 ft: 1 strobe
        if (length <= 30) {
          numStrobes = 1;
        } else {
          numStrobes = Math.ceil((length - 30) / 100) + 1;
        }
        candelaEach = 15;
        ratingTier = "15 cd (Corridor Standard NFPA 72 Table 18.5.5.5)";
        cornerDist = (length / numStrobes).toFixed(1);
        syncReq = numStrobes > 1 ? "Mandatory Synchronization (NFPA 72 §18.5.5.4.2)" : "Single Strobe (Sync Optional)";
        notes = `<strong>NFPA 72 Corridor Rules:</strong> Corridor requires <strong>${numStrobes} strobes</strong> rated at <strong>15 cd each</strong>. Strobes must be spaced at intervals no greater than 100 ft along the corridor, with appliances located within 15 ft of each corridor termination.`;
      } else if (type === 'sleeping') {
        let L = parseFloat(roomLengthInput.value);
        let W = parseFloat(roomWidthInput.value);
        if (isNaN(L) || L < 5) L = 5;
        if (isNaN(W) || W < 5) W = 5;
        cornerDist = Math.sqrt(Math.pow(L / 2, 2) + Math.pow(W / 2, 2)).toFixed(1);
        numStrobes = 1;

        const config = mountConfigSelect.value;
        if (config === 'ceilingCenter') {
          candelaEach = 177;
          ratingTier = "177 cd (Sleeping Area Ceiling Mount)";
          notes = `<strong>NFPA 72 Sleeping Area Standard:</strong> Ceiling-mounted strobe in sleeping rooms requires <strong>177 cd</strong> (up to 10 ft ceiling) and must be located within 16 ft horizontal distance of the head of the bed.`;
        } else {
          candelaEach = 110;
          ratingTier = "110 cd (Wall Mount &le; 24\" Below Ceiling) / 177 cd (> 24\")";
          notes = `<strong>NFPA 72 Sleeping Area Standard:</strong> Wall-mounted strobe requires <strong>110 cd</strong> if installed within 24 inches of ceiling, or <strong>177 cd</strong> if installed more than 24 inches below ceiling. Must be within 16 ft of pillow.`;
        }
        syncReq = "Single Appliance (Sync Optional)";
      } else {
        // Standard Non-sleeping room
        let L = parseFloat(roomLengthInput.value);
        let W = parseFloat(roomWidthInput.value);
        if (isNaN(L) || L < 5) L = 5;
        if (isNaN(W) || W < 5) W = 5;
        const maxDim = Math.max(L, W);
        cornerDist = Math.sqrt(Math.pow(L / 2, 2) + Math.pow(W / 2, 2)).toFixed(1);

        const config = mountConfigSelect.value;
        const ceilHeight = parseInt(ceilingHeightSelect.value, 10);

        if (config === 'ceilingCenter') {
          numStrobes = 1;
          let match = CEILING_TABLE[CEILING_TABLE.length - 1];
          for (let row of CEILING_TABLE) {
            if (maxDim <= row.dim) {
              match = row;
              break;
            }
          }
          if (ceilHeight <= 10) candelaEach = match.h10;
          else if (ceilHeight <= 20) candelaEach = match.h20;
          else candelaEach = match.h30;

          ratingTier = `${candelaEach} cd (Ceiling Mount at &le; ${ceilHeight} ft)`;
          notes = `<strong>Ceiling Mount Analysis:</strong> A single centered ceiling strobe covers <strong>${maxDim} &times; ${maxDim} ft</strong> at an effective ceiling elevation of ${ceilHeight} ft per NFPA 72 Table 18.5.5.4.1(b).`;
        } else {
          // Wall mount
          let match = ROOM_WALL_TABLE[ROOM_WALL_TABLE.length - 1];
          for (let row of ROOM_WALL_TABLE) {
            if (maxDim <= row.dim) {
              match = row;
              break;
            }
          }

          if (config === 'wallSingle') {
            numStrobes = 1;
            candelaEach = match.single;
            ratingTier = `${candelaEach} cd (Single Wall Mount)`;
            notes = `<strong>Wall Mount Sizing:</strong> Based on maximum room dimension of <strong>${maxDim} ft</strong>, NFPA 72 Table 18.5.5.4.1(a) requires a single centered <strong>${candelaEach} cd</strong> strobe.`;
          } else if (config === 'wallTwo') {
            numStrobes = 2;
            candelaEach = match.two;
            ratingTier = `${candelaEach} cd (Two Wall Mounts - Opposite Walls)`;
            syncReq = "Mandatory Synchronization (NFPA 72 §18.5.5.4.2)";
            notes = `<strong>Two Strobe Configuration:</strong> Two <strong>${candelaEach} cd</strong> strobes mounted centered on opposing walls. <strong>Synchronization is strictly mandatory</strong> to prevent seizure-inducing flash frequencies.`;
          } else {
            numStrobes = 4;
            candelaEach = match.four;
            ratingTier = `${candelaEach} cd (Four Wall Mounts - One per Wall)`;
            syncReq = "Mandatory Synchronization (NFPA 72 §18.5.5.4.2)";
            notes = `<strong>Four Strobe Configuration:</strong> Four <strong>${candelaEach} cd</strong> strobes mounted one per wall. Strobes must be synchronized within 10 ms.`;
          }
        }
      }

      // Lookup current draw
      let baseCurrent = CURRENT_MAP_24V[candelaEach] || Math.round(candelaEach * 1.45);
      let currentEach = Math.round(baseCurrent * voltageMult);
      let totalCurrent = ((currentEach * numStrobes) / 1000).toFixed(3);
      let totalCandela = candelaEach * numStrobes;

      resCandelaEach.textContent = candelaEach + " cd";
      resNumStrobes.textContent = numStrobes + (numStrobes === 1 ? " appliance" : " appliances");
      resTotalCandela.textContent = totalCandela + " cd";
      resRatingTier.textContent = ratingTier;
      resCornerDist.textContent = cornerDist + " ft";
      resCurrentEach.textContent = currentEach + " mA";
      resTotalCurrent.textContent = totalCurrent + " A";
      resSyncRequired.textContent = syncReq;
      strobeNotesBox.innerHTML = notes;

      strobeResultBox.style.display = 'block';
    }

    document.getElementById('calcStrobeBtn').addEventListener('click', calculateStrobe);
    document.getElementById('resetStrobeBtn').addEventListener('click', function() {
      setTimeout(calculateStrobe, 50);
    });

    // Auto-calculate on initial load
    window.addEventListener('DOMContentLoaded', calculateStrobe);
  </script>
</body>
</html>
"""

def main():
    target_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    file7 = os.path.join(target_dir, "fire-sprinkler-hydraulic-calculator.html")
    with open(file7, "w", encoding="utf-8") as f:
        f.write(TOOL_7_HTML)
    print(f"[PASS] fire-sprinkler-hydraulic-calculator.html generated successfully!")

    file8 = os.path.join(target_dir, "strobe-candela-calculator.html")
    with open(file8, "w", encoding="utf-8") as f:
        f.write(TOOL_8_HTML)
    print(f"[PASS] strobe-candela-calculator.html generated successfully!")

if __name__ == "__main__":
    main()
