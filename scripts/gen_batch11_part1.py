# -*- coding: utf-8 -*-
"""
Script to generate Batch 11 Part 1 tools:
1. pump-flow-calculator.html
2. rainwater-downpipe-calculator.html
"""
import os

TOOL_1_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pump Flow Calculator | Volumetric Flow Rate, Pipe Velocity &amp; Sizing</title>
  <meta name="description" content="Calculate pump flow rate (LPM, GPM, m³/h), liquid flow velocity, reservoir tank fill time, and affinity laws for centrifugal and positive displacement pumps.">
  <link rel="canonical" href="https://calchub.cloud/pump-flow-calculator.html">
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
        "name": "Pump Flow Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Hydraulic pipe velocity and volumetric pump flow sizing calculator evaluating Q = A * v continuity, tank fill durations, and affinity laws per Hydraulic Institute standards.",
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
            "name": "What is the formula relating pipe diameter, liquid velocity, and pump flow rate?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "By the fluid continuity principle for incompressible liquids: Q = A * v = (pi * D^2 / 4) * v. In metric engineering units: Q [m^3/h] = 0.002827 * D^2 [mm] * v [m/s], or Q [L/min] = 0.04712 * D^2 [mm] * v [m/s]. In US imperial units: Q [GPM] = 2.448 * D^2 [inches] * v [ft/s]."
            }
          },
          {
            "@type": "Question",
            "name": "What are recommended fluid velocities for pump suction versus discharge piping?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Per Hydraulic Institute guidelines, pump suction piping velocities should be maintained between 0.8 to 1.5 m/s (2.5 to 5.0 ft/s) to minimize frictional head loss and prevent pump cavitation (NPSHa degradation). Discharge lines operate economically between 1.8 to 3.0 m/s (6.0 to 10.0 ft/s) to balance capital pipe costs against pumping energy consumption."
            }
          },
          {
            "@type": "Question",
            "name": "How do the Affinity Laws predict flow changes with pump rotational speed (RPM)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The first Affinity Law states that volumetric flow rate (Q) is directly proportional to impeller rotational speed (N): Q_2 = Q_1 * (N_2 / N_1). For example, operating a 1450 RPM motor at 1160 RPM via a variable frequency drive (VFD) scales volumetric flow capacity down to exactly 80%."
            }
          },
          {
            "@type": "Question",
            "name": "How is vessel filling or emptying time calculated from pump flow?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Assuming a constant pump delivery rate Q, the filling time is the ratio of tank fluid volume to flow rate: t = V / Q. For a 10,000 liter water storage tank served by a 200 L/min pump, filling requires 10,000 / 200 = 50 minutes (0.833 hours)."
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
      <a href="engineering.html">Engineering</a> &rsaquo; 
      <a href="mechanical.html">Mechanical</a> &rsaquo; 
      <span>Pump Flow Calculator</span>
    </nav>

    <header class="calc-header">
      <div class="calc-badge">Fluid Hydraulics &amp; Piping</div>
      <h1 class="calc-title">Pump Flow Calculator</h1>
      <p class="calc-tagline">Calculate pump delivery flow rate, internal pipe velocity, tank fill duration, and affinity laws scaling per Hydraulic Institute and ISO 5199 standards.</p>
    </header>

    <div class="calc-grid">
      <div class="calc-main">
        <div class="tool-card">
          <form id="pumpFlowForm">
            <div class="form-row">
              <div class="form-group">
                <label for="flowMode">Calculation Objective</label>
                <select id="flowMode" class="form-control">
                  <option value="solveQ" selected>Solve Flow Rate from Pipe Diameter &amp; Velocity</option>
                  <option value="solveV">Solve Fluid Velocity from Flow Rate &amp; Diameter</option>
                  <option value="solveD">Size Pipe Diameter from Flow Rate &amp; Max Velocity</option>
                </select>
              </div>
              <div class="form-group">
                <label for="unitsSelect">Unit Standards</label>
                <select id="unitsSelect" class="form-control">
                  <option value="metric" selected>Metric (mm, m/s, m³/h, L/min)</option>
                  <option value="imperial">Imperial (inches, ft/s, GPM)</option>
                </select>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group" id="grpPipeD">
                <label for="pipeD">Pipe Internal Diameter ($D_{int}$)</label>
                <input type="number" id="pipeD" class="form-control" value="80" min="1" step="any" required>
                <span class="hint" id="pipeDHint">Internal bore in millimeters (e.g., DN80 = ~80mm)</span>
              </div>
              <div class="form-group" id="grpVelocity">
                <label for="fluidV">Fluid Flow Velocity ($v$)</label>
                <input type="number" id="fluidV" class="form-control" value="2.0" min="0.01" step="any" required>
                <span class="hint" id="fluidVHint">Recommended: 1.0&ndash;1.5 m/s (suction), 2.0&ndash;3.0 m/s (discharge)</span>
              </div>
            </div>

            <div class="form-row" id="grpFlowInput" style="display: none;">
              <div class="form-group">
                <label for="flowValInput">Pump Volumetric Flow Rate ($Q$)</label>
                <input type="number" id="flowValInput" class="form-control" value="36.2" min="0.01" step="any">
                <span class="hint" id="flowInputHint">Flow rate in m³/h</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="tankVol">Reservoir / Tank Volume (Optional)</label>
                <div style="display: flex; gap: 0.5rem;">
                  <input type="number" id="tankVol" class="form-control" value="20" min="0" step="any">
                  <select id="tankVolUnit" class="form-control" style="width: 110px;">
                    <option value="m3" selected>m³</option>
                    <option value="liters">Liters</option>
                    <option value="gallons">US Gallons</option>
                  </select>
                </div>
                <span class="hint">Leave zero if not calculating tank fill/drain duration</span>
              </div>
              <div class="form-group">
                <label for="vfdRpm">VFD Affinity Law Speed Ratio ($N_2 / N_1$)</label>
                <input type="number" id="vfdRpm" class="form-control" value="1.0" min="0.1" max="2.0" step="0.05">
                <span class="hint">1.0 = Base motor speed (100%), 0.8 = 80% VFD turndown</span>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcFlowBtn">Calculate Flow &amp; Piping Hydraulics</button>
              <button type="reset" class="btn btn-secondary" id="resetFlowBtn">Reset</button>
            </div>
          </form>

          <div id="pumpFlowResultBox" class="results-container" style="display: none; margin-top: 1.5rem;">
            <h3>Calculated Flow &amp; Piping Parameters</h3>
            <div class="results-grid">
              <div class="result-tile highlight">
                <span class="result-label">Volumetric Delivery Flow Rate ($Q$)</span>
                <span class="result-value" id="resFlowM3h">-- m³/h</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Flow Rate in LPM / GPM</span>
                <span class="result-value" id="resFlowLpm">-- L/min</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Pipe Mean Fluid Velocity ($v$)</span>
                <span class="result-value" id="resFluidVelocity">-- m/s</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Internal Pipe Cross-Section Area ($A$)</span>
                <span class="result-value" id="resPipeArea">-- mm²</span>
              </div>
              <div class="result-tile">
                <span class="result-label">VFD Adjusted Flow Rate ($Q_{vfd}$)</span>
                <span class="result-value" id="resVfdFlow">-- m³/h</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Estimated Tank Fill / Empty Time</span>
                <span class="result-value" id="resFillTime">-- min</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Velocity Application Compliance</span>
                <span class="result-value" id="resVelocityStatus">--</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Hydraulic Principles of Pump Volumetric Flow Sizing</h2>
          <p>
            In industrial process engineering, municipal water distribution, HVAC chilled water loops, and chemical processing, accurate determination of <strong>pump flow rate</strong> is the primary prerequisite for sizing pipe networks, selecting centrifugal or positive displacement pumps, and safeguarding against severe fluid dynamic failure modes like <em>cavitation</em>, <em>pipe erosion</em>, and <em>water hammer</em>.
          </p>
          <p>
            Volumetric flow rate ($Q$) quantifies the bulk volume of fluid passing through a designated conduit cross-sectional area per unit of time. Under the assumption of steady-state incompressible liquid flow (where fluid density $\rho$ remains constant), the relationship between conduit geometry, mean flow velocity ($v$), and volumetric capacity is dictated by the fundamental <strong>Equation of Continuity</strong>:
          </p>
          <div class="formula-box">
            $$Q = A \cdot v = \frac{\pi \cdot D_{int}^2}{4} \cdot v$$
          </div>
          <p>
            Where $A$ is the internal cross-sectional area of the pipe, $D_{int}$ is the internal bore diameter, and $v$ is the spatially averaged fluid velocity across the pipe section.
          </p>

          <h2>Engineering Flow Formulations and Practical Unit Conversions</h2>
          <p>
            Depending on geographic standards and specific industry conventions (such as Hydraulic Institute HI 9.6 or ISO 5199), engineers utilize standardized dimensional conversion coefficients:
          </p>

          <h3>1. Metric SI Engineering Units</h3>
          <p>
            When pipe internal diameter $D$ is measured in millimeters ($\text{mm}$) and mean velocity $v$ in meters per second ($\text{m/s}$):
          </p>
          <div class="formula-box">
            $$Q (\text{m}^3/\text{h}) = 3600 \cdot \frac{\pi \cdot (D / 1000)^2}{4} \cdot v = 0.0028274 \cdot D^2 \cdot v$$
            $$Q (\text{L/min}) = \frac{Q (\text{m}^3/\text{h}) \times 1000}{60} = 0.047124 \cdot D^2 \cdot v$$
          </div>

          <h3>2. US Customary (Imperial) Units</h3>
          <p>
            When internal diameter $D$ is specified in inches ($\text{in}$) and velocity $v$ in feet per second ($\text{ft/s}$), volumetric flow in US Gallons per Minute ($\text{GPM}$) is derived as:
          </p>
          <div class="formula-box">
            $$Q (\text{GPM}) = \frac{v (\text{ft/s}) \times \frac{\pi D^2}{4 \times 144} \times 7.48052 \times 60}{1} \approx 2.448 \cdot D^2 \cdot v$$
          </div>
          <p>
            Conversely, to size the internal pipe diameter ($D_{int}$) required to convey a target flow rate $Q$ while honoring an upper design velocity threshold $v_{max}$:
          </p>
          <div class="formula-box">
            $$D_{int} (\text{mm}) = \sqrt{\frac{4 \cdot Q (\text{m}^3/\text{h}) \times 10^6}{3600 \cdot \pi \cdot v_{max}}} \approx 18.806 \cdot \sqrt{\frac{Q (\text{m}^3/\text{h})}{v_{max} (\text{m/s})}}$$
          </div>

          <h2>Recommended Fluid Velocities in Pumping Systems (HI Standards)</h2>
          <p>
            Designing a piping system is an economic and hydrodynamic optimization. Sizing pipes too small forces excessive fluid velocity, exponentially multiplying frictional pressure drops ($\Delta P_f \propto v^2$) and causing internal pipe wall erosion and cavitation noise. Sizing pipes excessively large reduces pumping energy costs but increases initial piping capital investment and structural support weights.
          </p>
          <table class="reference-table">
            <thead>
              <tr>
                <th>Piping Service / Application</th>
                <th>Recommended Velocity (Metric)</th>
                <th>Recommended Velocity (Imperial)</th>
                <th>Engineering Justification</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Pump Suction Lines (Flooded)</td>
                <td>0.8 &ndash; 1.5 m/s</td>
                <td>2.5 &ndash; 5.0 ft/s</td>
                <td>Minimizes head loss to preserve Net Positive Suction Head Available (NPSHa)</td>
              </tr>
              <tr>
                <td>Pump Suction Lines (Lift Conditions)</td>
                <td>0.6 &ndash; 1.0 m/s</td>
                <td>2.0 &ndash; 3.3 ft/s</td>
                <td>Prevents vacuum vapor formation and cavitation pitting on impeller vanes</td>
              </tr>
              <tr>
                <td>General Pump Discharge Headers</td>
                <td>1.8 &ndash; 2.5 m/s</td>
                <td>6.0 &ndash; 8.2 ft/s</td>
                <td>Optimal economic balance between pipe schedule cost and life-cycle motor energy</td>
              </tr>
              <tr>
                <td>Short Discharge / Manifold Run</td>
                <td>2.5 &ndash; 3.5 m/s</td>
                <td>8.2 &ndash; 11.5 ft/s</td>
                <td>Acceptable for short spans where overall cumulative friction loss is low</td>
              </tr>
              <tr>
                <td>Slurry / Suspended Solids Piping</td>
                <td>1.2 &ndash; 2.2 m/s</td>
                <td>4.0 &ndash; 7.2 ft/s</td>
                <td>Maintains critical settling velocity without causing accelerated abrasive wall erosion</td>
              </tr>
              <tr>
                <td>Drain / Gravity Return Lines</td>
                <td>0.5 &ndash; 1.0 m/s</td>
                <td>1.6 &ndash; 3.3 ft/s</td>
                <td>Ensures non-pressurized gravity flow without air entrainment surging</td>
              </tr>
            </tbody>
          </table>

          <h2>The Affinity Laws: Rotational Speed &amp; Impeller Scaling</h2>
          <p>
            For rotodynamic centrifugal pumps handling low-viscosity fluids (such as clean water, glycols, and light hydrocarbons), the <strong>Affinity Laws</strong> (IEC 60193 / Hydraulic Institute 14.1) govern how operating characteristics scale with changes in shaft rotational speed ($N$) or impeller outer diameter ($D_{imp}$):
          </p>
          <div class="formula-box">
            $$\text{Flow Rate Scaling: } \frac{Q_1}{Q_2} = \left(\frac{N_1}{N_2}\right) \cdot \left(\frac{D_{imp,1}}{D_{imp,2}}\right)$$
            $$\text{Total Head Scaling: } \frac{H_1}{H_2} = \left(\frac{N_1}{N_2}\right)^2 \cdot \left(\frac{D_{imp,1}}{D_{imp,2}}\right)^2$$
            $$\text{Brake Power Scaling: } \frac{P_1}{P_2} = \left(\frac{N_1}{N_2}\right)^3 \cdot \left(\frac{D_{imp,1}}{D_{imp,2}}\right)^3$$
          </div>
          <p>
            These cubic power laws reveal why Variable Frequency Drives (VFDs) provide massive energy savings: reducing pump rotational speed by just $20\%$ ($N_2 / N_1 = 0.80$) drops flow rate to $80\%$, but slashes mechanical motor power consumption to $(0.80)^3 = 0.512$ ($51.2\%$)&mdash;a remarkable $48.8\%$ energy reduction!
          </p>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: Cooling Tower Circulation Pump Sizing</h3>
            <p><strong>Design Scenario:</strong> An industrial facility HVAC chiller requires a condenser cooling water flow rate of $Q = 180\text{ m}^3\text{/h}$ ($3,000\text{ L/min}$ or $\approx 792.5\text{ GPM}$) circulating through a closed circuit between the chiller barrel and a rooftop cooling tower. The plant engineering specification mandates a maximum suction velocity of $v_{suct} \le 1.20\text{ m/s}$ and a maximum discharge velocity of $v_{disc} \le 2.40\text{ m/s}$. The system feeds a $45\text{ m}^3$ reserve storage basin. Determine the minimum required internal diameters for both suction and discharge lines, recommend standard nominal pipe sizes (NPS), and compute the basin replenishment duration.</p>
            
            <p><strong>Step 1: Calculate Minimum Suction Pipe Internal Diameter</strong></p>
            <div class="formula-box">
              $$D_{suct,min} = 18.806 \times \sqrt{\frac{180\text{ m}^3\text{/h}}{1.20\text{ m/s}}} = 18.806 \times \sqrt{150} = 18.806 \times 12.247 \approx 230.33\text{ mm}$$
            </div>
            <p>
              Consulting ASME B36.10M standard steel pipe schedules: A standard <strong>DN250 (NPS 10-inch Schedule 40)</strong> pipe provides an internal diameter of $D_{int} = 254.5\text{ mm}$. The actual suction velocity in this pipe will be:
            </p>
            <div class="formula-box">
              $$v_{suct,actual} = \frac{180 / 3600}{\frac{\pi \times (0.2545)^2}{4}} = \frac{0.050}{0.05087} \approx 0.983\text{ m/s} \quad (\text{Compliant: } < 1.20\text{ m/s})$$
            </div>

            <p><strong>Step 2: Calculate Minimum Discharge Pipe Internal Diameter</strong></p>
            <div class="formula-box">
              $$D_{disc,min} = 18.806 \times \sqrt{\frac{180\text{ m}^3\text{/h}}{2.40\text{ m/s}}} = 18.806 \times \sqrt{75} = 18.806 \times 8.660 \approx 162.86\text{ mm}$$
            </div>
            <p>
              Selecting a standard <strong>DN200 (NPS 8-inch Schedule 40)</strong> pipe with internal diameter $D_{int} = 202.7\text{ mm}$ yields an actual discharge velocity of:
            </p>
            <div class="formula-box">
              $$v_{disc,actual} = \frac{180 / 3600}{\frac{\pi \times (0.2027)^2}{4}} = \frac{0.050}{0.03227} \approx 1.55\text{ m/s} \quad (\text{Optimal: } 1.5 - 2.0\text{ m/s})$$
            </div>

            <p><strong>Step 3: Calculate Storage Basin Fill Duration</strong></p>
            <div class="formula-box">
              $$t_{fill} = \frac{V_{basin}}{Q} = \frac{45\text{ m}^3}{180\text{ m}^3\text{/h}} = 0.25\text{ hours} = 15.0\text{ minutes}$$
            </div>
            <p>
              <strong>Engineering Sizing Summary:</strong> Installing DN250 suction and DN200 discharge piping guarantees minimal suction friction loss, preserving the required Net Positive Suction Head Margin ($\text{NPSHa} - \text{NPSHr} \ge 1.0\text{ m}$) while ensuring the basin can be fully replenished or turned over in exactly 15 minutes.
            </p>
          </div>

          <h2>Net Positive Suction Head (NPSH) and Cavitation Prevention</h2>
          <p>
            When calculating pump flow rate and pipe velocities, engineers must verify that the <strong>Net Positive Suction Head Available (NPSHa)</strong> exceeds the pump manufacturer's <strong>Net Positive Suction Head Required (NPSHr)</strong> by a mandatory safety margin ($\text{NPSHa} - \text{NPSHr} \ge 0.6 \text{ to } 1.0\text{ m}$):
          </p>
          <div class="formula-box">
            $$\text{NPSHa} = \frac{P_{atm} - P_{vap}}{\rho \cdot g} + h_{static} - h_{friction} \quad [\text{m}]$$
          </div>
          <p>
            Where $P_{atm}$ is ambient atmospheric pressure, $P_{vap}$ is fluid saturation vapor pressure at operating temperature, $h_{static}$ is liquid elevation above or below the pump centerline, and $h_{friction}$ is suction line head loss governed by Darcy-Weisbach flow velocity ($h_f = f \frac{L}{D} \frac{v^2}{2g}$).
          </p>
          <p>
            If high suction pipe velocity causes local static pressure to drop below vapor pressure, micro-bubbles spontaneously nucleate. As these vapor cavities travel into high-pressure regions of the pump impeller, they collapse violently with localized micro-jet velocities reaching $1,000\text{ m/s}$ and shockwave pressures exceeding $1,000\text{ MPa}$. This phenomenon (cavitation) destroys impeller metallurgy, generates intense rattling noise, and severely degrades volumetric flow capacity.
          </p>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Piping &amp; Fluid Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="pump-head-calculator.html">Pump Head (TDH) Calculator</a></li>
            <li><a href="pipe-sizing-calculator.html">Pipe Sizing &amp; Velocity</a></li>
            <li><a href="hydraulic-pump-power-calculator.html">Hydraulic Pump Power</a></li>
            <li><a href="cooling-load-calculator.html">Cooling Load Calculator</a></li>
            <li><a href="heat-exchanger-calculator.html">Heat Exchanger LMTD</a></li>
            <li><a href="psychrometric-calculator.html">Psychrometric Calculator</a></li>
          </ul>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container footer-content">
      <div class="footer-col">
        <h4>CalcHub</h4>
        <p>High-precision professional engineering and scientific calculation engines.</p>
      </div>
      <div class="footer-col">
        <h4>Directories</h4>
        <ul class="footer-links">
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="mechanical.html">Mechanical Engineering</a></li>
          <li><a href="engineering.html">Civil &amp; Structural</a></li>
          <li><a href="sitemap.xml">XML Sitemap</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom text-center">
      <p>&copy; 2026 CalcHub. Standard Engineering Reference Systems.</p>
    </div>
  </footer>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const calcBtn = document.getElementById('calcFlowBtn');
      const resetBtn = document.getElementById('resetFlowBtn');
      const resultBox = document.getElementById('pumpFlowResultBox');
      const flowMode = document.getElementById('flowMode');
      const unitsSelect = document.getElementById('unitsSelect');

      const grpPipeD = document.getElementById('grpPipeD');
      const grpVelocity = document.getElementById('grpVelocity');
      const grpFlowInput = document.getElementById('grpFlowInput');

      const pipeD = document.getElementById('pipeD');
      const fluidV = document.getElementById('fluidV');
      const flowValInput = document.getElementById('flowValInput');
      const pipeDHint = document.getElementById('pipeDHint');
      const fluidVHint = document.getElementById('fluidVHint');
      const flowInputHint = document.getElementById('flowInputHint');

      flowMode.addEventListener('change', function() {
        const mode = this.value;
        if (mode === 'solveQ') {
          grpPipeD.style.display = 'block';
          grpVelocity.style.display = 'block';
          grpFlowInput.style.display = 'none';
        } else if (mode === 'solveV') {
          grpPipeD.style.display = 'block';
          grpVelocity.style.display = 'none';
          grpFlowInput.style.display = 'block';
        } else if (mode === 'solveD') {
          grpPipeD.style.display = 'none';
          grpVelocity.style.display = 'block';
          grpFlowInput.style.display = 'block';
        }
      });

      unitsSelect.addEventListener('change', function() {
        const isMetric = this.value === 'metric';
        if (isMetric) {
          pipeDHint.textContent = 'Internal bore in millimeters (e.g., DN80 = ~80mm)';
          fluidVHint.textContent = 'Recommended: 1.0–1.5 m/s (suction), 2.0–3.0 m/s (discharge)';
          flowInputHint.textContent = 'Flow rate in m³/h';
          if (parseFloat(pipeD.value) < 15) pipeD.value = (parseFloat(pipeD.value) * 25.4).toFixed(0);
          if (parseFloat(fluidV.value) > 10) fluidV.value = (parseFloat(fluidV.value) * 0.3048).toFixed(2);
        } else {
          pipeDHint.textContent = 'Internal bore in inches (e.g., 3 inches)';
          fluidVHint.textContent = 'Recommended: 3–5 ft/s (suction), 6–10 ft/s (discharge)';
          flowInputHint.textContent = 'Flow rate in US Gallons per Minute (GPM)';
          if (parseFloat(pipeD.value) > 15) pipeD.value = (parseFloat(pipeD.value) / 25.4).toFixed(2);
          if (parseFloat(fluidV.value) < 10) fluidV.value = (parseFloat(fluidV.value) / 0.3048).toFixed(2);
        }
      });

      function calculateFlow() {
        const mode = flowMode.value;
        const isMetric = unitsSelect.value === 'metric';
        const vfdRatio = parseFloat(document.getElementById('vfdRpm').value) || 1.0;
        const tankVal = parseFloat(document.getElementById('tankVol').value) || 0;
        const tankUnit = document.getElementById('tankVolUnit').value;

        let d_mm = 0;
        let v_mps = 0;
        let q_m3h = 0;

        if (mode === 'solveQ') {
          let d_in = parseFloat(pipeD.value);
          let v_in = parseFloat(fluidV.value);
          if (isNaN(d_in) || d_in <= 0 || isNaN(v_in) || v_in <= 0) {
            alert('Please enter positive values for pipe diameter and velocity.');
            return;
          }
          if (isMetric) {
            d_mm = d_in;
            v_mps = v_in;
          } else {
            d_mm = d_in * 25.4;
            v_mps = v_in * 0.3048;
          }
          const area_m2 = (Math.PI * Math.pow(d_mm / 1000.0, 2)) / 4.0;
          q_m3h = area_m2 * v_mps * 3600.0;
        } else if (mode === 'solveV') {
          let d_in = parseFloat(pipeD.value);
          let q_in = parseFloat(flowValInput.value);
          if (isNaN(d_in) || d_in <= 0 || isNaN(q_in) || q_in <= 0) {
            alert('Please enter positive values for pipe diameter and flow rate.');
            return;
          }
          if (isMetric) {
            d_mm = d_in;
            q_m3h = q_in;
          } else {
            d_mm = d_in * 25.4;
            q_m3h = q_in * 0.2271247; // GPM to m3/h
          }
          const area_m2 = (Math.PI * Math.pow(d_mm / 1000.0, 2)) / 4.0;
          v_mps = (q_m3h / 3600.0) / area_m2;
        } else if (mode === 'solveD') {
          let v_in = parseFloat(fluidV.value);
          let q_in = parseFloat(flowValInput.value);
          if (isNaN(v_in) || v_in <= 0 || isNaN(q_in) || q_in <= 0) {
            alert('Please enter positive values for fluid velocity and flow rate.');
            return;
          }
          if (isMetric) {
            v_mps = v_in;
            q_m3h = q_in;
          } else {
            v_mps = v_in * 0.3048;
            q_m3h = q_in * 0.2271247;
          }
          const area_m2 = (q_m3h / 3600.0) / v_mps;
          d_mm = Math.sqrt((4.0 * area_m2) / Math.PI) * 1000.0;
        }

        // Secondary units
        const q_lpm = (q_m3h * 1000.0) / 60.0;
        const q_gpm = q_m3h * 4.402868;
        const v_fps = v_mps * 3.28084;
        const pipeArea_mm2 = (Math.PI * Math.pow(d_mm, 2)) / 4.0;
        const q_vfd_m3h = q_m3h * vfdRatio;

        // Tank fill time
        let fillTimeMin = '--';
        if (tankVal > 0 && q_m3h > 0) {
          let tank_m3 = tankVal;
          if (tankUnit === 'liters') tank_m3 = tankVal / 1000.0;
          else if (tankUnit === 'gallons') tank_m3 = tankVal * 0.00378541;
          const t_hours = tank_m3 / q_m3h;
          fillTimeMin = (t_hours * 60.0).toFixed(1) + ' min (' + t_hours.toFixed(2) + ' hrs)';
        }

        // Velocity status assessment
        let statusClass = 'Optimal Discharge Range';
        if (v_mps < 0.8) {
          statusClass = 'Low Velocity (Oversized Pipe - Risk of Sedimentation)';
        } else if (v_mps >= 0.8 && v_mps <= 1.5) {
          statusClass = 'Optimal for Pump Suction Lines (Low NPSH Loss)';
        } else if (v_mps > 1.5 && v_mps <= 2.8) {
          statusClass = 'Optimal for General Pump Discharge Pipelines';
        } else if (v_mps > 2.8 && v_mps <= 3.5) {
          statusClass = 'High Velocity (Acceptable for Short Manifolds)';
        } else {
          statusClass = 'EXCESSIVE VELOCITY (High Friction & Erosion Risk)';
        }

        // Display results
        document.getElementById('resFlowM3h').textContent = q_m3h.toFixed(2) + ' m³/h (' + (q_m3h / 3600.0 * 1000.0).toFixed(2) + ' L/s)';
        document.getElementById('resFlowLpm').textContent = q_lpm.toFixed(1) + ' L/min (' + q_gpm.toFixed(1) + ' GPM)';
        document.getElementById('resFluidVelocity').textContent = v_mps.toFixed(2) + ' m/s (' + v_fps.toFixed(2) + ' ft/s)';
        document.getElementById('resPipeArea').textContent = pipeArea_mm2.toFixed(0) + ' mm² (' + (d_mm / 25.4).toFixed(2) + ' in dia)';
        document.getElementById('resVfdFlow').textContent = q_vfd_m3h.toFixed(2) + ' m³/h (' + (q_vfd_m3h * 4.402868).toFixed(1) + ' GPM)';
        document.getElementById('resFillTime').textContent = fillTimeMin;
        document.getElementById('resVelocityStatus').textContent = statusClass;

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculateFlow);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
      });

      calculateFlow();
    });
  </script>
</body>
</html>
"""

TOOL_2_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Rainwater Downpipe Calculator | Roof Drainage &amp; Pipe Sizing</title>
  <meta name="description" content="Calculate rainwater downpipe size, effective roof catchment area, design rainfall runoff (L/s), and gutter outlet capacity per BS EN 12056-3 &amp; AS/NZS 3500.">
  <link rel="canonical" href="https://calchub.cloud/rainwater-downpipe-calculator.html">
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
        "name": "Rainwater Downpipe Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Roof drainage and vertical rainwater leader sizing calculator evaluating effective catchment area, design storm runoff, and downpipe capacity per BS EN 12056-3.",
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
            "name": "How is effective roof catchment area calculated for pitched roofs?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Per BS EN 12056-3 and AS/NZS 3500, wind-driven rain hits roof slopes at an angle. The effective catchment area (A_e) accounts for horizontal plan projection plus vertical elevation: A_e = L * (W + H / 2), where L is roof gutter length, W is horizontal plan span from eaves to ridge, and H is vertical rise height from eaves to ridge."
            }
          },
          {
            "@type": "Question",
            "name": "What is the formula for design rainwater runoff flow rate (Q)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The design rainwater runoff flow rate is computed as: Q = (r * A_e * C) / 3600, where Q is flow in liters per second (L/s), r is design rainfall intensity in mm/hr (typically a 1-in-50 or 1-in-100 year storm event), A_e is effective catchment area in square meters (m^2), and C is runoff discharge coefficient (typically 0.95 to 1.0 for impermeable metal, slate, and tile roofs)."
            }
          },
          {
            "@type": "Question",
            "name": "Why are vertical rainwater downpipes not sized for 100% full-bore hydraulic flow?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In conventional gravity drainage, water enters downpipes around the perimeter, forming an annular sheet clinging to the pipe walls with a continuous central air core. Sizing pipes to operate at a filling ratio f <= 0.25 to 0.33 prevents sub-atmospheric pressure surges, noise, and sudden violent siphonage that could collapse eaves gutters."
            }
          },
          {
            "@type": "Question",
            "name": "How many downpipes are required for a large commercial roof?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The minimum number of downpipes is calculated as: N_pipes = ceil(Q_total / Q_pipe_capacity). However, architectural plumbing guidelines also enforce maximum downpipe spacing (typically no more than 15 meters or 50 feet apart along a continuous eaves gutter) to prevent gutter overtopping during peak cloudbursts."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="civil">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">
        <span class="logo-icon">&pi;</span>
        <span class="logo-text">Calc<strong>Hub</strong></span>
      </a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="engineering.html">Engineering</a>
        <a href="mechanical.html">Mechanical</a>
        <a href="civil.html" class="active">Civil &amp; Roof</a>
        <a href="solar-energy.html">Solar</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo; 
      <a href="civil.html">Civil &amp; Construction</a> &rsaquo; 
      <span>Rainwater Downpipe Calculator</span>
    </nav>

    <header class="calc-header">
      <div class="calc-badge">Roof Drainage &amp; Plumbing</div>
      <h1 class="calc-title">Rainwater Downpipe Calculator</h1>
      <p class="calc-tagline">Size roof rainwater downpipes (leaders), calculate wind-driven effective catchment area, and determine design storm runoff per BS EN 12056-3.</p>
    </header>

    <div class="calc-grid">
      <div class="calc-main">
        <div class="tool-card">
          <form id="downpipeForm">
            <div class="form-row">
              <div class="form-group">
                <label for="roofLength">Gutter Length ($L$ in meters)</label>
                <input type="number" id="roofLength" class="form-control" value="20" min="0.5" step="any" required>
                <span class="hint">Longitudinal length of the eaves line</span>
              </div>
              <div class="form-group">
                <label for="roofWidth">Eaves-to-Ridge Horizontal Span ($W$ in meters)</label>
                <input type="number" id="roofWidth" class="form-control" value="8" min="0.5" step="any" required>
                <span class="hint">Horizontal plan projection of the roof slope</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="roofHeight">Vertical Rise from Eaves to Ridge ($H$ in meters)</label>
                <input type="number" id="roofHeight" class="form-control" value="3" min="0" step="any" required>
                <span class="hint">Vertical height (set 0 for flat roofs)</span>
              </div>
              <div class="form-group">
                <label for="rainIntensity">Design Storm Rainfall Intensity ($r$)</label>
                <div style="display: flex; gap: 0.5rem;">
                  <input type="number" id="rainIntensity" class="form-control" value="75" min="10" step="1" required>
                  <select id="rainPreset" class="form-control" style="width: 140px;">
                    <option value="50">50 mm/h (UK/Eur standard)</option>
                    <option value="75" selected>75 mm/h (Heavy storm)</option>
                    <option value="100">100 mm/h (Severe storm)</option>
                    <option value="150">150 mm/h (Tropical monsoon)</option>
                  </select>
                </div>
                <span class="hint">Design storm rainfall rate per local meteorological data</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="downpipeSize">Selected Downpipe Internal Diameter ($D$)</label>
                <select id="downpipeSize" class="form-control">
                  <option value="68">68 mm (~2.7 in) - Residential Round PVC/Zinc</option>
                  <option value="82" selected>82 mm (~3.2 in) - Standard Domestic / Commercial</option>
                  <option value="100">100 mm (~4.0 in) - Heavy Commercial / Industrial</option>
                  <option value="150">150 mm (~6.0 in) - Large Warehouse / Industrial Hub</option>
                  <option value="200">200 mm (~8.0 in) - Major Logistics Terminal</option>
                </select>
              </div>
              <div class="form-group">
                <label for="runoffCoeff">Roof Surface Discharge Coefficient ($C$)</label>
                <select id="runoffCoeff" class="form-control">
                  <option value="1.0" selected>1.00 - Impermeable Metal Sheeting / Glazed Tile</option>
                  <option value="0.95">0.95 - Standard Concrete Tile / Slate Shingles</option>
                  <option value="0.90">0.90 - Asphalt Shingle / Bitumen Roofing Felt</option>
                  <option value="0.50">0.50 - Extensive Green Roof (Sedum Retaining)</option>
                </select>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcDownpipeBtn">Calculate Downpipe &amp; Catchment Sizing</button>
              <button type="reset" class="btn btn-secondary" id="resetDownpipeBtn">Reset</button>
            </div>
          </form>

          <div id="downpipeResultBox" class="results-container" style="display: none; margin-top: 1.5rem;">
            <h3>Calculated Drainage &amp; Downpipe Sizing</h3>
            <div class="results-grid">
              <div class="result-tile highlight">
                <span class="result-label">Total Design Rainwater Runoff ($Q_{design}$)</span>
                <span class="result-value" id="resDesignFlow">-- L/s</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Effective Catchment Area ($A_e$)</span>
                <span class="result-value" id="resEffectiveArea">-- m²</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Single Downpipe Capacity ($Q_{cap}$)</span>
                <span class="result-value" id="resPipeCap">-- L/s</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Minimum Downpipes Required ($N_{pipes}$)</span>
                <span class="result-value" id="resPipesReq">-- Pipes</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Max Spacing Between Downpipes</span>
                <span class="result-value" id="resSpacing">-- m</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Drainage System Sizing Assessment</span>
                <span class="result-value" id="resStatus">--</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Principles of Roof Rainwater Drainage (BS EN 12056-3)</h2>
          <p>
            Effective architectural rainwater drainage protects building structures from catastrophic water ingress, structural roof overload, and facade staining. In accordance with <strong>BS EN 12056-3</strong> (<em>Gravity drainage systems inside buildings &ndash; Roof drainage, layout and calculation</em>) and regional standards like <strong>AS/NZS 3500.3</strong>, rainwater downpipes (also referred to as rainwater leaders or conductors) must be sized to convey design storm rainfall runoff safely away from eaves gutters without risk of backflow or overflowing.
          </p>
          <p>
            Designing roof drainage involves three interconnected technical stages:
          </p>
          <ol>
            <li>Evaluating the <strong>effective catchment area ($A_e$)</strong> accounting for wind-driven rainfall pitch factors.</li>
            <li>Determining peak design storm runoff flow rate ($Q$) based on localized rainfall intensity ($r$).</li>
            <li>Sizing vertical downpipes and gutter outlets based on gravity annular-flow hydraulic discharge limits.</li>
          </ol>

          <h2>Effective Roof Catchment Area Formulation ($A_e$)</h2>
          <p>
            Rain rarely falls strictly vertically; during severe thunderstorms and squall lines, prevailing wind drives raindrops at angles ranging from $25^\circ$ to $45^\circ$ from vertical. Consequently, a pitched roof slope intercepts significantly more rainwater than its simple flat horizontal footprint. Under the formulation of BS EN 12056-3 Clause 4.2.2:
          </p>
          <div class="formula-box">
            $$A_e = L \cdot \left(W + \frac{H}{2}\right) \quad [\text{m}^2]$$
          </div>
          <p>
            Where:
          </p>
          <ul>
            <li>$L$ is the length of the eaves gutter line in meters ($\text{m}$).</li>
            <li>$W$ is the horizontal distance (plan projection) from eaves to ridge in meters ($\text{m}$).</li>
            <li>$H$ is the vertical elevation rise from eaves to ridge in meters ($\text{m}$).</li>
          </ul>
          <p>
            For a flat roof ($H = 0$), the formula simplifies to true plan area: $A_e = L \times W$. If an abutting vertical masonry parapet wall drains onto the roof, 50% of the vertical wall face area ($0.5 \times L_{wall} \times H_{wall}$) must be added to $A_e$.
          </p>

          <h2>Design Storm Runoff Flow Rate ($Q$)</h2>
          <p>
            The design rainwater runoff flow rate delivered from the catchment into the eaves gutter is evaluated using the classic Rational-type hydrological formulation:
          </p>
          <div class="formula-box">
            $$Q = \frac{r \cdot A_e \cdot C}{3600} \quad [\text{L/s}]$$
          </div>
          <p>
            Where:
          </p>
          <ul>
            <li>$r$ is the design rainfall intensity in millimeters per hour ($\text{mm/h}$), typically chosen from national meteorological return-period curves (e.g., a 2-minute peak storm event with a 1-in-50 year return frequency).</li>
            <li>$A_e$ is the effective catchment area in square meters ($\text{m}^2$).</li>
            <li>$C$ is the dimensionless runoff discharge coefficient, reflecting roof impermeability and surface water retention ($C = 1.0$ for metal and smooth tiles, $C \approx 0.50$ for green living roofs).</li>
            <li>$3600$ converts hours to seconds and millimeters over square meters ($1\text{ mm} \times 1\text{ m}^2 = 1\text{ Liter}$) to liters per second ($\text{L/s}$).</li>
          </ul>

          <h2>Vertical Downpipe Hydraulic Capacities (Annular Flow Mechanics)</h2>
          <p>
            Unlike pressurized water distribution pipes, conventional building downpipes operate under gravity non-siphonic conditions. Water enters the top of the downpipe through a gutter outlet nozzle. As water accelerates downward under gravity, surface tension and boundary drag cause the fluid to adhere to the interior pipe circumference, forming an <strong>annular falling film</strong> enclosing a continuous central core of air.
          </p>
          <p>
            To prevent erratic air choking, acoustic hammering, and self-siphonage that can rapidly collapse thin-gauge gutters, BS EN 12056-3 caps the allowable water-to-pipe cross-sectional filling ratio at:
          </p>
          <div class="formula-box">
            $$f = \frac{A_{water}}{A_{pipe}} \le 0.25 \text{ to } 0.33$$
          </div>
          <p>
            Under these annular gravity flow conditions with a standard sharp-edged or bellmouth gutter outlet, empirical downpipe discharge capacities are standardized as:
          </p>
          <div class="formula-box">
            $$Q_{max} \approx 0.0000188 \cdot D_{int}^{2.625} \quad [\text{L/s}]$$
          </div>
          <p>
            Where $D_{int}$ is internal diameter in millimeters. The reference table below details standard commercial rainwater pipe capacities:
          </p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Nominal Pipe Diameter</th>
                <th>Internal Bore ($D_{int}$)</th>
                <th>Hydraulic Flow Capacity ($Q_{cap}$)</th>
                <th>Max Catchment Served ($r = 75\text{ mm/h}$)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>68 mm Round PVC / Zinc</td>
                <td>65 mm</td>
                <td>2.35 L/s</td>
                <td>112.8 m² effective area</td>
              </tr>
              <tr>
                <td>82 mm Round PVC / Cast Iron</td>
                <td>78 mm</td>
                <td>3.85 L/s</td>
                <td>184.8 m² effective area</td>
              </tr>
              <tr>
                <td>100 mm (4-inch) Round PVC / AL</td>
                <td>96 mm</td>
                <td>6.70 L/s</td>
                <td>321.6 m² effective area</td>
              </tr>
              <tr>
                <td>150 mm (6-inch) Heavy Industrial</td>
                <td>146 mm</td>
                <td>19.80 L/s</td>
                <td>950.4 m² effective area</td>
              </tr>
              <tr>
                <td>200 mm (8-inch) Logistics Hub</td>
                <td>194 mm</td>
                <td>41.50 L/s</td>
                <td>1,992.0 m² effective area</td>
              </tr>
            </tbody>
          </table>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: Commercial Distribution Warehouse Roof</h3>
            <p><strong>Design Scenario:</strong> A logistics distribution center features a dual-pitch portal frame roof. Each roof slope has an eaves gutter length of $L = 60.0\text{ m}$, a horizontal plan span of $W = 18.0\text{ m}$, and a ridge height of $H = 4.0\text{ m}$. The roofing material is profiled trapezoidal pre-painted metal cladding ($C = 1.0$). Local meteorological data for a 1-in-50 year storm specifies a design rainfall intensity of $r = 75\text{ mm/h}$. The project specification considers standard $100\text{ mm}$ round PVC downpipes (rated hydraulic capacity $Q_{cap} = 6.70\text{ L/s}$). Determine the effective catchment area, peak runoff flow rate, and minimum number and maximum spacing of downpipes.</p>
            
            <p><strong>Step 1: Calculate Effective Catchment Area ($A_e$)</strong></p>
            <div class="formula-box">
              $$A_e = L \times \left(W + \frac{H}{2}\right) = 60.0\text{ m} \times \left(18.0 + \frac{4.0}{2}\right) = 60.0 \times 20.0 = 1,200.0\text{ m}^2$$
            </div>

            <p><strong>Step 2: Calculate Peak Storm Rainwater Runoff ($Q$)</strong></p>
            <div class="formula-box">
              $$Q = \frac{75\text{ mm/h} \times 1,200.0\text{ m}^2 \times 1.0}{3600} = \frac{90,000}{3600} = 25.00\text{ L/s}$$
            </div>

            <p><strong>Step 3: Determine Minimum Number of Downpipes ($N_{pipes}$)</strong></p>
            <div class="formula-box">
              $$N_{pipes} \ge \frac{Q_{total}}{Q_{cap}} = \frac{25.00\text{ L/s}}{6.70\text{ L/s}} \approx 3.73 \implies \text{Round up to } 4\text{ Downpipes}$$
            </div>

            <p><strong>Step 4: Check Downpipe Spacing Along Gutter Line</strong></p>
            <div class="formula-box">
              $$\text{Downpipe Spacing} = \frac{L}{N_{pipes}} = \frac{60.0\text{ m}}{4} = 15.0\text{ m}$$
            </div>
            <p>
              <strong>Engineering Conclusion:</strong> Installing <strong>4 downpipes of 100 mm diameter</strong> spaced at $15.0\text{ m}$ intervals perfectly satisfies both the hydraulic capacity requirement ($4 \times 6.70 = 26.8\text{ L/s} > 25.0\text{ L/s}$) and the maximum $15\text{ m}$ spacing guideline of BS EN 12056-3, guaranteeing that eaves gutters will not overflow during a severe $75\text{ mm/h}$ design cloudburst.
            </p>
          </div>

          <h2>Siphonic Roof Drainage vs. Conventional Gravity Systems (BS 8490 &amp; ASME A112.6.9)</h2>
          <p>
            In modern large-scale industrial distribution hubs, airport terminals, and sports stadiums, conventional gravity downpipes operating under annular flow ($f \le 0.33$) can require dozens of vertical leaders piercing through valuable interior floor space. To overcome this spatial penalty, structural engineers frequently design <strong>siphonic roof drainage systems</strong> governed by <strong>BS 8490</strong> and <strong>ASME A112.6.9</strong>.
          </p>
          <p>
            A siphonic system uses specialized roof drain outlets equipped with anti-vortex air baffle plates. During intense design cloudbursts, the water level over the outlet submerges the baffle, sealing the inlet against air entry. The vertical downpipe rapidly primes, creating a continuous water column that drops through the full building height ($H_{total}$):
          </p>
          <div class="formula-box">
            $$Q_{siphonic} = A \cdot v = A \cdot \sqrt{\frac{2g \cdot H_{total}}{\sum K_{loss}}}$$
          </div>
          <p>
            Because the entire vertical pipe runs at a 100% water filling ratio ($f = 1.0$) under negative gauge pressure (sub-atmospheric suction), linear water velocities reach $4.0\text{ to } 8.0\text{ m/s}$. Consequently, a single $75\text{ mm}$ or $100\text{ mm}$ siphonic pipe can discharge the equivalent flow volume that would require three $150\text{ mm}$ conventional gravity downpipes. Furthermore, siphonic collection manifolds can run horizontally across ceiling trusses with zero slope, eliminating subterranean trenching under warehouse floor slabs.
          </p>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Civil &amp; Hydraulic Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="pump-flow-calculator.html">Pump Flow &amp; Pipe Velocity</a></li>
            <li><a href="concrete-calculator.html">Concrete Volume Calculator</a></li>
            <li><a href="rebar-calculator.html">Rebar Weight &amp; Grid Sizing</a></li>
            <li><a href="retaining-wall-calculator.html">Retaining Wall Sizing</a></li>
            <li><a href="pipe-sizing-calculator.html">Pipe Sizing Calculator</a></li>
            <li><a href="brick-calculator.html">Brick Masonry Calculator</a></li>
          </ul>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container footer-content">
      <div class="footer-col">
        <h4>CalcHub</h4>
        <p>High-precision professional engineering and scientific calculation engines.</p>
      </div>
      <div class="footer-col">
        <h4>Directories</h4>
        <ul class="footer-links">
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="civil.html">Civil &amp; Construction</a></li>
          <li><a href="mechanical.html">Mechanical Engineering</a></li>
          <li><a href="sitemap.xml">XML Sitemap</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom text-center">
      <p>&copy; 2026 CalcHub. Standard Engineering Reference Systems.</p>
    </div>
  </footer>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const calcBtn = document.getElementById('calcDownpipeBtn');
      const resetBtn = document.getElementById('resetDownpipeBtn');
      const resultBox = document.getElementById('downpipeResultBox');
      const rainPreset = document.getElementById('rainPreset');
      const rainIntensity = document.getElementById('rainIntensity');

      rainPreset.addEventListener('change', function() {
        rainIntensity.value = this.value;
      });

      function calculateDownpipe() {
        const l = parseFloat(document.getElementById('roofLength').value);
        const w = parseFloat(document.getElementById('roofWidth').value);
        const h = parseFloat(document.getElementById('roofHeight').value) || 0;
        const r = parseFloat(rainIntensity.value);
        const pipeDia = parseInt(document.getElementById('downpipeSize').value, 10);
        const coeff = parseFloat(document.getElementById('runoffCoeff').value);

        if (isNaN(l) || l <= 0 || isNaN(w) || w <= 0 || isNaN(r) || r <= 0) {
          alert('Please enter valid positive dimensions and rainfall intensity.');
          return;
        }

        // 1. Effective catchment area Ae = L * (W + H / 2)
        const ae = l * (w + (h / 2.0));

        // 2. Design runoff flow rate Q = (r * Ae * C) / 3600 [L/s]
        const q_design = (r * ae * coeff) / 3600.0;

        // 3. Downpipe flow capacity per BS EN 12056 empirical capacities
        let q_cap = 3.85;
        if (pipeDia === 68) q_cap = 2.35;
        else if (pipeDia === 82) q_cap = 3.85;
        else if (pipeDia === 100) q_cap = 6.70;
        else if (pipeDia === 150) q_cap = 19.80;
        else if (pipeDia === 200) q_cap = 41.50;

        // 4. Minimum pipes required
        const pipesReq = Math.max(1, Math.ceil(q_design / q_cap));

        // 5. Average spacing
        const spacing = l / pipesReq;

        // 6. Status check
        let statusMsg = 'Optimal Drainage Design (Capacity Exceeds Peak Runoff)';
        if (spacing > 18.0) {
          statusMsg = 'Warning: Downpipe spacing exceeds 18m. Consider adding extra downpipes to prevent gutter overtopping.';
        } else if (pipesReq === 1 && q_design > q_cap * 0.9) {
          statusMsg = 'Close to capacity threshold (>90%). Recommend adding a secondary leader.';
        }

        document.getElementById('resDesignFlow').textContent = q_design.toFixed(2) + ' L/s (' + (q_design * 60.0).toFixed(0) + ' L/min)';
        document.getElementById('resEffectiveArea').textContent = ae.toFixed(1) + ' m² (' + (ae * 10.7639).toFixed(0) + ' sq ft)';
        document.getElementById('resPipeCap').textContent = q_cap.toFixed(2) + ' L/s per downpipe';
        document.getElementById('resPipesReq').textContent = pipesReq + (pipesReq === 1 ? ' Downpipe' : ' Downpipes');
        document.getElementById('resSpacing').textContent = spacing.toFixed(1) + ' m (' + (spacing * 3.28084).toFixed(1) + ' ft)';
        document.getElementById('resStatus').textContent = statusMsg;

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculateDownpipe);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
      });

      calculateDownpipe();
    });
  </script>
</body>
</html>
"""

def main():
    with open("pump-flow-calculator.html", "w", encoding="utf-8") as f:
        f.write(TOOL_1_HTML.strip() + "\n")
    print("[PASS] pump-flow-calculator.html generated successfully!")

    with open("rainwater-downpipe-calculator.html", "w", encoding="utf-8") as f:
        f.write(TOOL_2_HTML.strip() + "\n")
    print("[PASS] rainwater-downpipe-calculator.html generated successfully!")

if __name__ == "__main__":
    main()
