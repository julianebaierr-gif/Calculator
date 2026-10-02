# -*- coding: utf-8 -*-
"""
Script to generate Batch 11 Part 2 tools:
3. reynolds-number-calculator.html
4. shaft-diameter-calculator.html
"""
import os

TOOL_3_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Reynolds Number Calculator | Laminar, Critical &amp; Turbulent Flow</title>
  <meta name="description" content="Calculate Reynolds number (Re) for circular and non-circular ducts. Determine laminar, transition, or turbulent flow regime and Darcy friction factor.">
  <link rel="canonical" href="https://calchub.cloud/reynolds-number-calculator.html">
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
        "name": "Reynolds Number Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Fluid mechanics kinematic calculator evaluating Reynolds number Re = (rho * v * D) / mu, hydraulic diameter Dh, flow regime classification, and Darcy friction factor.",
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
            "name": "What is the physical meaning of the Reynolds number?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The Reynolds number (Re) is a dimensionless ratio of inertial forces to viscous forces within a moving fluid: Re = (rho * v * L) / mu. At low Reynolds numbers, viscous viscous damping suppresses disturbances, maintaining smooth laminar streamlines. At high Reynolds numbers, fluid inertia dominates, causing destabilization, swirling eddies, and chaotic turbulent mixing."
            }
          },
          {
            "@type": "Question",
            "name": "What are the critical Reynolds number boundaries for internal pipe flow?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For internal conduit flow through circular pipes: Re < 2,300 represents laminar flow; 2,300 <= Re <= 4,000 represents the critical transition regime where flow alternates between laminar and turbulent bursts; and Re > 4,000 indicates fully developed turbulent flow."
            }
          },
          {
            "@type": "Question",
            "name": "How is the Reynolds number computed for non-circular conduits or rectangular ducts?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For non-circular cross-sections, the geometric pipe diameter is replaced with the Hydraulic Diameter (D_h), defined as: D_h = 4 * A / P, where A is the cross-sectional flow area and P is the wetted perimeter. For a rectangular duct of width a and height b, D_h = (2 * a * b) / (a + b)."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between dynamic and kinematic viscosity?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Dynamic (absolute) viscosity (mu) measures a fluid's internal shear resistance against deformation, expressed in Pascal-seconds (Pa*s) or centipoise (cP). Kinematic viscosity (nu) is dynamic viscosity divided by mass density: nu = mu / rho, expressed in m^2/s or centistokes (cSt). 1 cSt = 1 mm^2/s = 10^-6 m^2/s."
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
      <span>Reynolds Number Calculator</span>
    </nav>

    <header class="calc-header">
      <div class="calc-badge">Fluid Dynamics &amp; Transport Phenomena</div>
      <h1 class="calc-title">Reynolds Number Calculator</h1>
      <p class="calc-tagline">Calculate the dimensionless Reynolds number ($Re$), determine laminar vs. turbulent flow regimes, and compute Darcy friction factor per the Moody chart.</p>
    </header>

    <div class="calc-grid">
      <div class="calc-main">
        <div class="tool-card">
          <form id="reForm">
            <div class="form-row">
              <div class="form-group">
                <label for="fluidPreset">Standard Fluid Selection</label>
                <select id="fluidPreset" class="form-control">
                  <option value="water20" selected>Water @ 20&deg;C (ρ = 998.2 kg/m³, μ = 1.002 cP)</option>
                  <option value="water60">Water @ 60&deg;C (ρ = 983.2 kg/m³, μ = 0.467 cP)</option>
                  <option value="air20">Air @ 20&deg;C, 1 atm (ρ = 1.204 kg/m³, μ = 0.0182 cP)</option>
                  <option value="oilISO46">Hydraulic Oil ISO VG 46 @ 40&deg;C (ρ = 875 kg/m³, ν = 46 cSt)</option>
                  <option value="engineOil30">Engine Oil SAE 30 @ 20&deg;C (ρ = 890 kg/m³, μ = 290 cP)</option>
                  <option value="ethanol20">Ethanol @ 20&deg;C (ρ = 789 kg/m³, μ = 1.20 cP)</option>
                  <option value="glycerol20">Glycerol (100%) @ 20&deg;C (ρ = 1261 kg/m³, μ = 1412 cP)</option>
                  <option value="custom">Custom Fluid Properties</option>
                </select>
              </div>
              <div class="form-group">
                <label for="conduitType">Conduit Cross-Section Geometry</label>
                <select id="conduitType" class="form-control">
                  <option value="circular" selected>Circular Pipe / Tube (Internal Diameter $D$)</option>
                  <option value="rectangular">Rectangular Duct (Width $a$ &times; Height $b$)</option>
                </select>
              </div>
            </div>

            <div class="form-row" id="grpCircular">
              <div class="form-group">
                <label for="pipeDia">Internal Pipe Diameter ($D$ in mm)</label>
                <input type="number" id="pipeDia" class="form-control" value="50" min="0.1" step="any" required>
                <span class="hint">E.g., DN50 / 2-inch pipe ≈ 50mm bore</span>
              </div>
              <div class="form-group">
                <label for="fluidVelocity">Mean Fluid Flow Velocity ($v$ in m/s)</label>
                <input type="number" id="fluidVelocity" class="form-control" value="1.5" min="0.001" step="any" required>
                <span class="hint">Average velocity across pipe cross-section</span>
              </div>
            </div>

            <div class="form-row" id="grpRectangular" style="display: none;">
              <div class="form-group">
                <label for="ductWidth">Duct Width ($a$ in mm)</label>
                <input type="number" id="ductWidth" class="form-control" value="300" min="1" step="any">
              </div>
              <div class="form-group">
                <label for="ductHeight">Duct Height ($b$ in mm)</label>
                <input type="number" id="ductHeight" class="form-control" value="200" min="1" step="any">
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="fluidDensity">Fluid Mass Density ($\rho$ in kg/m³)</label>
                <input type="number" id="fluidDensity" class="form-control" value="998.2" min="0.01" step="any" required>
              </div>
              <div class="form-group">
                <label for="dynViscosity">Dynamic Viscosity ($\mu$ in cP or mPa&middot;s)</label>
                <input type="number" id="dynViscosity" class="form-control" value="1.002" min="0.0001" step="any" required>
                <span class="hint">1 cP = 1 mPa·s = 0.001 Pa·s (water ≈ 1 cP)</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="pipeRoughness">Pipe Absolute Roughness ($\varepsilon$ in mm)</label>
                <select id="pipeRoughness" class="form-control">
                  <option value="0.0015">0.0015 mm - Drawn Copper / Brass / PVC / Glass</option>
                  <option value="0.045" selected>0.045 mm - Commercial Carbon Steel / Welded</option>
                  <option value="0.15">0.15 mm - Galvanized Iron / Mild Rust</option>
                  <option value="0.26">0.26 mm - Cast Iron (As-cast)</option>
                  <option value="1.5">1.50 mm - Riveted Steel / Rough Concrete</option>
                </select>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcReBtn">Calculate Reynolds Number &amp; Regime</button>
              <button type="reset" class="btn btn-secondary" id="resetReBtn">Reset</button>
            </div>
          </form>

          <div id="reResultBox" class="results-container" style="display: none; margin-top: 1.5rem;">
            <h3>Hydrodynamic State &amp; Reynolds Number</h3>
            <div class="results-grid">
              <div class="result-tile highlight">
                <span class="result-label">Reynolds Number ($Re$)</span>
                <span class="result-value" id="resReVal">--</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Flow Regime Classification</span>
                <span class="result-value" id="resRegime">--</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Hydraulic Diameter ($D_h$)</span>
                <span class="result-value" id="resHydDia">-- mm</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Kinematic Viscosity ($\nu$)</span>
                <span class="result-value" id="resKinVisc">-- cSt (mm²/s)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Darcy Friction Factor ($f$)</span>
                <span class="result-value" id="resFrictionFactor">--</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Relative Roughness ($\varepsilon / D_h$)</span>
                <span class="result-value" id="resRelRoughness">--</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Physics and Dimensionless Fundamentals of the Reynolds Number</h2>
          <p>
            The <strong>Reynolds number ($Re$)</strong> is universally recognized as the most foundational dimensionless parameter in fluid mechanics, aerodynamics, chemical reactor engineering, and heat transfer. Formulated by the British physicist and engineer Osborne Reynolds in his landmark 1883 experimental investigations on pipe flow transitions, the Reynolds number quantifies the relative ratio between <strong>dynamic inertial forces</strong> (which promote turbulence and fluid mixing) and <strong>viscous shear forces</strong> (which dampen disturbances and enforce laminar streamline parallelism):
          </p>
          <div class="formula-box">
            $$Re = \frac{\text{Inertial Forces}}{\text{Viscous Forces}} = \frac{\rho \cdot v \cdot D_{char}}{\mu} = \frac{v \cdot D_{char}}{\nu}$$
          </div>
          <p>
            Where:
          </p>
          <ul>
            <li>$\rho$ is the fluid mass density in kilograms per cubic meter ($\text{kg/m}^3$).</li>
            <li>$v$ is the mean spatial flow velocity in meters per second ($\text{m/s}$).</li>
            <li>$D_{char}$ is the characteristic geometric dimension (internal diameter $D$ for circular pipes, or hydraulic diameter $D_h$ for non-circular conduits) in meters ($\text{m}$).</li>
            <li>$\mu$ is dynamic (absolute) viscosity in Pascal-seconds ($\text{Pa}\cdot\text{s} = \text{N}\cdot\text{s/m}^2 = 1,000\text{ cP}$).</li>
            <li>$\nu$ is kinematic viscosity in square meters per second ($\text{m}^2/\text{s} = 10^6\text{ cSt}$), where $\nu = \mu / \rho$.</li>
          </ul>

          <h2>Flow Regime Classification in Internal Conduit Flows</h2>
          <p>
            For fluid conveyance through closed conduits and pipelines, fluid behavior fundamentally alters across three well-defined regimes:
          </p>

          <h3>1. Laminar Flow ($Re < 2,300$)</h3>
          <p>
            In the laminar regime, viscous damping forces overwhelmingly predominate. The fluid moves in smooth, concentric cylindrical macroscopic layers or laminae sliding past one another without transverse momentum exchange. The velocity profile across the circular cross-section adopts a perfect parabolic shape (Poiseuille flow) where centerline velocity is exactly twice the mean velocity ($v_{max} = 2 v_{avg}$). Pressure drop along the pipe varies strictly linearly with flow velocity ($h_f \propto v$), and the Darcy friction factor is entirely independent of pipe wall roughness:
          </p>
          <div class="formula-box">
            $$f_{laminar} = \frac{64}{Re}$$
          </div>

          <h3>2. Critical Transition Regime ($2,300 \le Re \le 4,000$)</h3>
          <p>
            In this unstable transition zone, inertial forces begin to overpower viscous stabilization. The boundary layer experiences intermittent turbulent spots or "slugs" of turbulence interspersed with decaying laminar flow. Hydrodynamic behavior is non-deterministic and highly sensitive to external pipe vibrations, valve disturbances, and inlet fitting geometry. Engineers avoid sizing critical metering or cooling equipment within this erratic band.
          </p>

          <h3>3. Fully Developed Turbulent Flow ($Re > 4,000$)</h3>
          <p>
            In the turbulent regime, inertial momentum dominates. The flow field degenerates into a three-dimensional spectrum of chaotic swirling eddies, vortex stretching, and intense cross-stream turbulent diffusion. The velocity profile flattens substantially, characterized by a steep velocity gradient in the viscous sublayer immediately adjacent to the pipe wall. Frictional pressure drop scales approximately with the square of velocity ($h_f \propto v^2$).
          </p>

          <h2>Hydraulic Diameter ($D_h$) for Non-Circular Conduits</h2>
          <p>
            When fluid flows through non-circular conduits&mdash;such as rectangular HVAC sheet metal ductwork, oval tunnels, or annular spaces between concentric pipes&mdash;hydrodynamic similitude is preserved by substituting the <strong>Hydraulic Diameter ($D_h$)</strong> into the Reynolds number formulation:
          </p>
          <div class="formula-box">
            $$D_h = \frac{4 \cdot A}{P_{wetted}}$$
          </div>
          <p>
            Where $A$ is the net cross-sectional fluid area and $P_{wetted}$ is the wetted perimeter in contact with the flowing fluid stream. For a rectangular duct of width $a$ and height $b$:
          </p>
          <div class="formula-box">
            $$D_h = \frac{4 \cdot (a \cdot b)}{2 \cdot (a + b)} = \frac{2 \cdot a \cdot b}{a + b}$$
          </div>

          <h2>Darcy Friction Factor Evaluation ($f$) &amp; The Colebrook-White Equation</h2>
          <p>
            The Darcy-Weisbach equation governs frictional head loss in piping: $h_f = f \frac{L}{D} \frac{v^2}{2g}$. In the turbulent regime ($Re > 4,000$), the friction factor ($f$) depends simultaneously on both the Reynolds number and the relative surface roughness ($\varepsilon / D$). The international standard implicit formulation is the <strong>Colebrook-White equation</strong> (1939):
          </p>
          <div class="formula-box">
            $$\frac{1}{\sqrt{f}} = -2 \cdot \log_{10}\left(\frac{\varepsilon / D_h}{3.7} + \frac{2.51}{Re \cdot \sqrt{f}}\right)$$
          </div>
          <p>
            Because the Colebrook equation is transcendental, this calculator executes an explicit, highly accurate closed-form approximation developed by <strong>Swamee and Jain (1976)</strong> (accurate to within $\pm 1.0\%$ across $5,000 \le Re \le 10^8$ and $10^{-6} \le \varepsilon / D \le 10^{-2}$):
          </p>
          <div class="formula-box">
            $$f = \frac{0.25}{\left[\log_{10}\left(\frac{\varepsilon / D_h}{3.7} + \frac{5.74}{Re^{0.9}}\right)\right]^2}$$
          </div>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Fluid Medium</th>
                <th>Temperature (&deg;C)</th>
                <th>Density $\rho$ (kg/m³)</th>
                <th>Dynamic Viscosity $\mu$ (cP)</th>
                <th>Kinematic Viscosity $\nu$ (cSt)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Clean Fresh Water</td>
                <td>20 &deg;C</td>
                <td>998.2</td>
                <td>1.002</td>
                <td>1.004</td>
              </tr>
              <tr>
                <td>Hot Water (District Heating)</td>
                <td>80 &deg;C</td>
                <td>971.8</td>
                <td>0.355</td>
                <td>0.365</td>
              </tr>
              <tr>
                <td>Dry Atmospheric Air (1 atm)</td>
                <td>20 &deg;C</td>
                <td>1.204</td>
                <td>0.0182</td>
                <td>15.11</td>
              </tr>
              <tr>
                <td>Hydraulic Fluid (ISO VG 46)</td>
                <td>40 &deg;C</td>
                <td>875.0</td>
                <td>40.25</td>
                <td>46.00</td>
              </tr>
              <tr>
                <td>Light Fuel Oil / Diesel</td>
                <td>15 &deg;C</td>
                <td>850.0</td>
                <td>3.00</td>
                <td>3.53</td>
              </tr>
              <tr>
                <td>Crude Heavy Petroleum</td>
                <td>20 &deg;C</td>
                <td>920.0</td>
                <td>120.0</td>
                <td>130.4</td>
              </tr>
            </tbody>
          </table>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: District Chilled Water Supply Pipeline</h3>
            <p><strong>Design Scenario:</strong> A central municipal district cooling plant conveys chilled water at $T = 6.0^\circ\text{C}$ ($\rho = 1,000\text{ kg/m}^3$, $\mu = 1.472\text{ cP} = 0.001472\text{ Pa}\cdot\text{s}$) to a commercial high-rise development. The carbon steel distribution main has an internal bore of $D = 200\text{ mm}$ ($0.200\text{ m}$) with an absolute commercial roughness of $\varepsilon = 0.045\text{ mm}$. The required volumetric flow rate is $Q = 200\text{ m}^3\text{/h}$ ($0.05556\text{ m}^3\text{/s}$). Calculate the mean flow velocity, the Reynolds number, classify the flow regime, and determine the Darcy friction factor.</p>
            
            <p><strong>Step 1: Calculate Mean Fluid Velocity ($v$)</strong></p>
            <div class="formula-box">
              $$A = \frac{\pi \times (0.200\text{ m})^2}{4} = 0.031416\text{ m}^2$$
              $$v = \frac{Q}{A} = \frac{0.05556\text{ m}^3\text{/s}}{0.031416\text{ m}^2} \approx 1.768\text{ m/s}$$
            </div>

            <p><strong>Step 2: Compute the Reynolds Number ($Re$)</strong></p>
            <div class="formula-box">
              $$Re = \frac{\rho \cdot v \cdot D}{\mu} = \frac{1000\text{ kg/m}^3 \times 1.768\text{ m/s} \times 0.200\text{ m}}{0.001472\text{ Pa}\cdot\text{s}} = \frac{353.6}{0.001472} \approx 240,217$$
            </div>
            <p>
              Because $Re = 240,217 \gg 4,000$, the flow is located deeply in the <strong>fully developed turbulent regime</strong>.
            </p>

            <p><strong>Step 3: Evaluate Relative Roughness ($\varepsilon / D$)</strong></p>
            <div class="formula-box">
              $$\frac{\varepsilon}{D} = \frac{0.045\text{ mm}}{200.0\text{ mm}} = 0.000225$$
            </div>

            <p><strong>Step 4: Calculate Darcy Friction Factor ($f$) via Swamee-Jain</strong></p>
            <div class="formula-box">
              $$\begin{aligned}
              f &= \frac{0.25}{\left[\log_{10}\left(\frac{0.000225}{3.7} + \frac{5.74}{(240217)^{0.9}}\right)\right]^2} = \frac{0.25}{\left[\log_{10}(0.00006081 + 0.00008585)\right]^2} \\
              &= \frac{0.25}{\left[\log_{10}(0.00014666)\right]^2} = \frac{0.25}{(-3.8337)^2} = \frac{0.25}{14.697} \approx 0.0170
              \end{aligned}$$
            </div>
            <p>
              <strong>Engineering Conclusion:</strong> Operating at $Re = 240,217$ with $f = 0.0170$ provides excellent thermal heat transfer coefficients inside heat exchangers while generating predictable, moderate pumping head losses along the distribution pipeline.
            </p>
          </div>

          <h2>Hydrodynamic Entry Length ($L_e$) and Velocity Profile Development</h2>
          <p>
            When fluid enters a pipe from a reservoir or plenum, the velocity profile is initially uniform. As boundary shear layers grow inward from the conduit walls due to viscosity, they eventually coalesce at the centerline. The axial distance required to establish an invariant, fully developed velocity profile is the <strong>hydrodynamic entry length ($L_e$)</strong>:
          </p>
          <div class="formula-box">
            $$\text{Laminar Flow: } \frac{L_{e,lam}}{D} \approx 0.05 \cdot Re$$
            $$\text{Turbulent Flow: } \frac{L_{e,turb}}{D} \approx 4.4 \cdot Re^{1/6} \approx 25 \text{ to } 40 \text{ pipe diameters}$$
          </div>
          <p>
            In laminar flows at $Re = 2,000$, the hydrodynamic entry length can exceed $100$ pipe diameters ($L_e \approx 0.05 \times 2000 \times D = 100 D$). For turbulent flows, intense radial eddy mixing accelerates boundary layer merger, establishing fully developed turbulent profiles within $25$ to $40$ pipe diameters. Flow metering sensors (such as electromagnetic flow meters, vortex shedding meters, and orifice plates) mandate minimum straight upstream runs to avoid severe measurement errors induced by developing boundary profiles.
          </p>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Fluid &amp; Thermal Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="pump-flow-calculator.html">Pump Flow &amp; Pipe Velocity</a></li>
            <li><a href="pipe-sizing-calculator.html">Pipe Sizing &amp; Velocity</a></li>
            <li><a href="heat-exchanger-calculator.html">Heat Exchanger LMTD</a></li>
            <li><a href="cooling-load-calculator.html">Cooling Load Calculator</a></li>
            <li><a href="hydraulic-pump-power-calculator.html">Hydraulic Pump Power</a></li>
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
      const calcBtn = document.getElementById('calcReBtn');
      const resetBtn = document.getElementById('resetReBtn');
      const resultBox = document.getElementById('reResultBox');
      const fluidPreset = document.getElementById('fluidPreset');
      const conduitType = document.getElementById('conduitType');
      const pipeRoughness = document.getElementById('pipeRoughness');

      const grpCircular = document.getElementById('grpCircular');
      const grpRectangular = document.getElementById('grpRectangular');

      const fluidDensity = document.getElementById('fluidDensity');
      const dynViscosity = document.getElementById('dynViscosity');
      const pipeDia = document.getElementById('pipeDia');
      const fluidVelocity = document.getElementById('fluidVelocity');
      const ductWidth = document.getElementById('ductWidth');
      const ductHeight = document.getElementById('ductHeight');

      const presets = {
        water20: { rho: 998.2, mu: 1.002 },
        water60: { rho: 983.2, mu: 0.467 },
        air20: { rho: 1.204, mu: 0.0182 },
        oilISO46: { rho: 875.0, mu: 40.25 },
        engineOil30: { rho: 890.0, mu: 290.0 },
        ethanol20: { rho: 789.0, mu: 1.20 },
        glycerol20: { rho: 1261.0, mu: 1412.0 }
      };

      fluidPreset.addEventListener('change', function() {
        if (this.value !== 'custom' && presets[this.value]) {
          fluidDensity.value = presets[this.value].rho;
          dynViscosity.value = presets[this.value].mu;
        }
      });

      conduitType.addEventListener('change', function() {
        if (this.value === 'circular') {
          grpCircular.style.display = 'grid';
          grpRectangular.style.display = 'none';
        } else {
          grpCircular.style.display = 'grid';
          grpRectangular.style.display = 'grid';
        }
      });

      function calculateReynolds() {
        const rho = parseFloat(fluidDensity.value);
        const mu_cP = parseFloat(dynViscosity.value);
        const v = parseFloat(fluidVelocity.value);
        const rough_mm = parseFloat(pipeRoughness.value);

        if (isNaN(rho) || rho <= 0 || isNaN(mu_cP) || mu_cP <= 0 || isNaN(v) || v <= 0) {
          alert('Please enter valid positive values for density, viscosity, and velocity.');
          return;
        }

        // Convert dynamic viscosity to Pa*s (1 cP = 0.001 Pa*s)
        const mu_Pa_s = mu_cP * 0.001;

        // Kinematic viscosity (cSt)
        const nu_m2_s = mu_Pa_s / rho;
        const nu_cSt = nu_m2_s * 1e6;

        // Characteristic diameter Dh (m)
        let dh_mm = 0;
        if (conduitType.value === 'circular') {
          dh_mm = parseFloat(pipeDia.value);
        } else {
          const a = parseFloat(ductWidth.value);
          const b = parseFloat(ductHeight.value);
          if (isNaN(a) || a <= 0 || isNaN(b) || b <= 0) {
            alert('Please enter valid duct dimensions.');
            return;
          }
          dh_mm = (2.0 * a * b) / (a + b);
        }

        const dh_m = dh_mm / 1000.0;

        // Reynolds number Re = (rho * v * D) / mu
        const re = (rho * v * dh_m) / mu_Pa_s;

        // Flow regime classification
        let regimeText = '';
        let fFactor = 0;
        const relRoughness = rough_mm / dh_mm;

        if (re < 2300) {
          regimeText = 'Laminar Flow (Smooth Streamlines, Re < 2,300)';
          fFactor = 64.0 / re;
        } else if (re >= 2300 && re <= 4000) {
          regimeText = 'Critical Transition Zone (Unstable, 2,300 ≤ Re ≤ 4,000)';
          // Linear interpolation for transition friction factor
          const f_lam = 64.0 / 2300.0;
          const f_turb = 0.25 / Math.pow(Math.log10((relRoughness / 3.7) + (5.74 / Math.pow(4000.0, 0.9))), 2);
          const ratio = (re - 2300.0) / 1700.0;
          fFactor = f_lam + ratio * (f_turb - f_lam);
        } else {
          regimeText = 'Fully Developed Turbulent Flow (Re > 4,000)';
          // Swamee-Jain formula
          const term = (relRoughness / 3.7) + (5.74 / Math.pow(re, 0.9));
          fFactor = 0.25 / Math.pow(Math.log10(term), 2);
        }

        // Render outputs
        document.getElementById('resReVal').textContent = re.toLocaleString('en-US', {maximumFractionDigits: 0});
        document.getElementById('resRegime').textContent = regimeText;
        document.getElementById('resHydDia').textContent = dh_mm.toFixed(1) + ' mm (' + (dh_mm / 25.4).toFixed(2) + ' in)';
        document.getElementById('resKinVisc').textContent = nu_cSt.toFixed(3) + ' cSt';
        document.getElementById('resFrictionFactor').textContent = fFactor.toFixed(4);
        document.getElementById('resRelRoughness').textContent = relRoughness.toExponential(3);

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculateReynolds);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
      });

      calculateReynolds();
    });
  </script>
</body>
</html>
"""

TOOL_4_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Shaft Diameter Calculator | ASME B106.1M Torsion &amp; Bending Sizing</title>
  <meta name="description" content="Calculate solid and hollow transmission shaft diameter under combined torsion and bending moment per ASME B106.1M and Tresca / von Mises failure criteria.">
  <link rel="canonical" href="https://calchub.cloud/shaft-diameter-calculator.html">
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
        "name": "Shaft Diameter Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Mechanical transmission shaft sizing engine calculating solid and hollow shaft diameters under combined bending and torsional fatigue per ASME B106.1M.",
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
            "name": "What is the ASME Code equation for sizing transmission drive shafts?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Per ASME B106.1M, solid shaft diameter under combined loading is sized as: d = [ (16 / (pi * tau_allow)) * sqrt((K_m * M)^2 + (K_t * T)^2) ]^(1/3), where M is bending moment, T is torsional moment, K_m is bending fatigue/shock factor (typically 1.5 to 2.0), K_t is torsional fatigue factor (typically 1.0 to 1.5), and tau_allow is allowable design shear stress."
            }
          },
          {
            "@type": "Question",
            "name": "How does cutting a standard keyway affect allowable shaft shear stress?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Per ASME standards and DIN 6885, milling a keyway creates stress concentrations and reduces the effective polar section modulus. The allowable design shear stress is de-rated by 25%: tau_allow,keyway = 0.75 * tau_allow."
            }
          },
          {
            "@type": "Question",
            "name": "How is a hollow drive shaft sized compared to a solid shaft?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For a hollow shaft with inside-to-outside diameter ratio k = d_i / d_o, the polar section modulus is Z_p = (pi / 16) * d_o^3 * (1 - k^4). The required outer diameter is: d_o = [ (16 / (pi * tau_allow * (1 - k^4))) * sqrt((K_m * M)^2 + (K_t * T)^2) ]^(1/3). Hollow shafts achieve up to 40-50% weight reduction while maintaining equivalent torsional rigidity."
            }
          },
          {
            "@type": "Question",
            "name": "What are allowable design stresses for commercial steel transmission shafts?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "ASME B106.1M establishes allowable design shear stress as tau_allow = min(0.30 * S_yield, 0.18 * S_ult), with a maximum allowable ceiling of 55 MPa (8,000 psi) for commercial carbon steel without verified material certifications, or 41 MPa (6,000 psi) with keyway."
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
      <span>Shaft Diameter Calculator</span>
    </nav>

    <header class="calc-header">
      <div class="calc-badge">Machine Elements &amp; Drivelines</div>
      <h1 class="calc-title">Shaft Diameter Calculator</h1>
      <p class="calc-tagline">Calculate minimum solid and hollow drive shaft diameters under combined bending and torsion per ASME B106.1M and Guest / Tresca failure criteria.</p>
    </header>

    <div class="calc-grid">
      <div class="calc-main">
        <div class="tool-card">
          <form id="shaftForm">
            <div class="form-row">
              <div class="form-group">
                <label for="shaftType">Shaft Geometry Configuration</label>
                <select id="shaftType" class="form-control">
                  <option value="solid" selected>Solid Circular Transmission Shaft</option>
                  <option value="hollow">Hollow Cylindrical Shaft (Weight Optimized)</option>
                </select>
              </div>
              <div class="form-group">
                <label for="torqueInput">Applied Torsional Moment ($T$ in N&middot;m)</label>
                <input type="number" id="torqueInput" class="form-control" value="850" min="0" step="any" required>
                <span class="hint">Continuous or peak driving torque</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="bendingInput">Bending Moment ($M$ in N&middot;m)</label>
                <input type="number" id="bendingInput" class="form-control" value="450" min="0" step="any" required>
                <span class="hint">From overhung pulleys, gears, or self-weight</span>
              </div>
              <div class="form-group">
                <label for="materialYield">Shaft Material Specification</label>
                <select id="materialYield" class="form-control">
                  <option value="55" selected>AISI 1045 Carbon Steel (Commercial, τ_allow ≈ 55 MPa)</option>
                  <option value="42">Commercial Steel with Keyway (τ_allow ≈ 41.25 MPa)</option>
                  <option value="75">AISI 4140 Quenched &amp; Tempered (Alloy, τ_allow ≈ 75 MPa)</option>
                  <option value="90">AISI 4340 High-Strength Alloy (τ_allow ≈ 90 MPa)</option>
                  <option value="custom">Custom Design Allowable Stress</option>
                </select>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="tauAllow">Allowable Design Shear Stress ($\tau_{allow}$ in MPa)</label>
                <input type="number" id="tauAllow" class="form-control" value="55" min="1" step="any" required>
                <span class="hint">Max allowable shear stress per ASME B106.1M</span>
              </div>
              <div class="form-group">
                <label for="hasKeyway">Keyway Stress Concentration Reduction</label>
                <select id="hasKeyway" class="form-control">
                  <option value="1.0">No Keyway (Splined or Shrink-Fit Coupling, 100% capacity)</option>
                  <option value="0.75" selected>Milled Parallel Keyway (Apply 25% ASME Stress De-rating)</option>
                </select>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="serviceShock">ASME Shock &amp; Fatigue Factors ($K_m, K_t$)</label>
                <select id="serviceShock" class="form-control">
                  <option value="gradual">Gradual Loading (Km = 1.5, Kt = 1.0)</option>
                  <option value="minor" selected>Minor Shock / Rotating Shaft (Km = 1.5, Kt = 1.25)</option>
                  <option value="heavy">Heavy Shock / Pulsating Load (Km = 2.0, Kt = 1.5)</option>
                  <option value="extreme">Extreme Shock / Reversing (Km = 3.0, Kt = 2.0)</option>
                </select>
              </div>
              <div class="form-group" id="grpHollowRatio" style="display: none;">
                <label for="kRatio">Hollow Diameter Ratio ($k = d_i / d_o$)</label>
                <input type="number" id="kRatio" class="form-control" value="0.6" min="0.1" max="0.9" step="0.05">
                <span class="hint">Standard hollow ratio: 0.5 to 0.7 (40-60% weight reduction)</span>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcShaftBtn">Size Drive Shaft Diameter</button>
              <button type="reset" class="btn btn-secondary" id="resetShaftBtn">Reset</button>
            </div>
          </form>

          <div id="shaftResultBox" class="results-container" style="display: none; margin-top: 1.5rem;">
            <h3>Calculated Structural Shaft Sizing</h3>
            <div class="results-grid">
              <div class="result-tile highlight">
                <span class="result-label">Minimum Required Outer Diameter ($d_{min}$)</span>
                <span class="result-value" id="resOuterDia">-- mm</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Recommended Standard Stock Diameter</span>
                <span class="result-value" id="resStdDia">-- mm</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Equivalent Torsional Moment ($T_e$)</span>
                <span class="result-value" id="resEquivTorque">-- N·m</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Equivalent Bending Moment ($M_e$)</span>
                <span class="result-value" id="resEquivBending">-- N·m</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Effective Design Allowable Stress</span>
                <span class="result-value" id="resEffStress">-- MPa</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Hollow Bore Inside Diameter ($d_i$)</span>
                <span class="result-value" id="resInnerDia">-- mm</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Mechanical Principles of Transmission Shaft Design (ASME B106.1M)</h2>
          <p>
            A <strong>transmission shaft</strong> is a rotating machine element that transmits mechanical power and torque from a prime mover (electric motor, turbine, or internal combustion engine) to driven machinery such as gearboxes, centrifugal pumps, conveyor drums, and marine propellers. During operation, rotating shafts rarely experience pure torsion alone; transverse forces exerted by overhung belt pulleys, spur or helical gear teeth meshes, chain sprockets, and rotor self-weight generate substantial <strong>bending moments ($M$)</strong> simultaneously with <strong>torsional twisting moments ($T$)</strong>.
          </p>
          <p>
            Because the shaft rotates continuously, any given fiber on the outer surface cycles alternatingly between peak tension and peak compression once per revolution ($1\text{ RPM} = 1\text{ full stress cycle}$). This continuous cyclic bending creates high risk of progressive fatigue failure. Structural design of power transmission shafting is governed internationally by the classic <strong>ASME Code for Design of Transmission Shafting (ASME B106.1M)</strong> and <strong>DIN 743</strong>.
          </p>

          <h2>ASME Combined Loading Formulation</h2>
          <p>
            According to the Maximum Shear Stress Failure Theory (Guest / Tresca criterion) combined with empirical fatigue and shock multiplication factors, the equivalent torsional moment ($T_e$) and equivalent bending moment ($M_e$) are formulated as:
          </p>
          <div class="formula-box">
            $$T_e = \sqrt{(K_m \cdot M)^2 + (K_t \cdot T)^2}$$
            $$M_e = \frac{1}{2} \cdot \left[ K_m \cdot M + \sqrt{(K_m \cdot M)^2 + (K_t \cdot T)^2} \right]$$
          </div>
          <p>
            Where:
          </p>
          <ul>
            <li>$M$ is the maximum resultant bending moment calculated from vertical and horizontal shear force diagrams: $M = \sqrt{M_v^2 + M_h^2}$.</li>
            <li>$T$ is the nominal transmitted twisting torque: $T = \frac{9548.8 \cdot P (\text{kW})}{N (\text{RPM})}$.</li>
            <li>$K_m$ is the numerical fatigue bending factor accounting for cyclic reversal and shock loading.</li>
            <li>$K_t$ is the numerical torsional fatigue shock factor.</li>
          </ul>

          <h2>Governing Diameter Sizing Equations: Solid vs. Hollow Shafts</h2>

          <h3>1. Solid Circular Drive Shaft</h3>
          <p>
            Equating the maximum torsional shear stress $\tau_{max} = \frac{16 \cdot T_e}{\pi \cdot d^3}$ to the effective allowable design shear stress ($\tau_{allow}$), the minimum allowable solid shaft diameter ($d_{min}$) is derived as:
          </p>
          <div class="formula-box">
            $$d_{min} = \sqrt[3]{\frac{16 \cdot T_e}{\pi \cdot \tau_{allow}}} = \sqrt[3]{\frac{16 \cdot \sqrt{(K_m \cdot M)^2 + (K_t \cdot T)^2}}{\pi \cdot \tau_{allow}}}$$
          </div>

          <h3>2. Hollow Cylindrical Drive Shaft</h3>
          <p>
            In aerospace propulsion, high-performance motorsport driveshafts, and long marine propeller line shafting, minimizing rotating mass and rotational moment of inertia ($I$) is paramount. Defining the diametral bore ratio $k = d_i / d_o$ (where $d_i$ is inside bore diameter and $d_o$ is outside diameter):
          </p>
          <div class="formula-box">
            $$d_o = \sqrt[3]{\frac{16 \cdot T_e}{\pi \cdot \tau_{allow} \cdot (1 - k^4)}}, \quad d_i = k \cdot d_o$$
          </div>
          <p>
            A hollow shaft with $k = 0.60$ achieves a $36\%$ weight reduction compared to a solid shaft of identical outside diameter while retaining more than $87\%$ of its torsional strength and stiffness ($1 - k^4 = 1 - 0.1296 = 0.8704$).
          </p>

          <h2>ASME Shock &amp; Fatigue Factors Reference Matrix</h2>
          <table class="reference-table">
            <thead>
              <tr>
                <th>Nature of Mechanical Loading</th>
                <th>Bending Shock Factor ($K_m$)</th>
                <th>Torsional Shock Factor ($K_t$)</th>
                <th>Typical Machinery Applications</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Stationary Shaft / Pure Gradual Load</td>
                <td>1.0 &ndash; 1.5</td>
                <td>1.0</td>
                <td>Fixed jackshafts, steady centrifugal pump spindles</td>
              </tr>
              <tr>
                <td>Rotating Shaft / Minor Shock (Standard)</td>
                <td>1.5 &ndash; 2.0</td>
                <td>1.0 &ndash; 1.5</td>
                <td>Conveyors, machine tool spindles, gear reducers</td>
              </tr>
              <tr>
                <td>Rotating Shaft / Heavy Shock Loads</td>
                <td>2.0 &ndash; 2.5</td>
                <td>1.5 &ndash; 2.0</td>
                <td>Reciprocating compressors, punch presses, shears</td>
              </tr>
              <tr>
                <td>Reversing / Extreme Vibratory Shock</td>
                <td>2.5 &ndash; 3.0</td>
                <td>2.0 &ndash; 3.0</td>
                <td>Jaw crushers, vibratory screens, rolling mills</td>
              </tr>
            </tbody>
          </table>

          <h2>Keyway De-rating Factors and Stress Concentrations</h2>
          <p>
            Cutting a longitudinal slot (keyway per DIN 6885 or ANSI B17.1) to accommodate drive keys introduces sharp re-entrant corners that create severe stress concentrations ($K_t \approx 1.8 \text{ to } 2.4$). Rather than requiring complex localized finite-element notch analysis for everyday mechanical sizing, the <strong>ASME Shaft Code mandates an across-the-board 25% de-rating of the allowable design stress</strong>:
          </p>
          <div class="formula-box">
            $$\tau_{allow,keyway} = 0.75 \cdot \tau_{allow}$$
          </div>
          <p>
            Per ASME B106.1M, the baseline allowable stress for steel shafts without material test certifications is capped at:
          </p>
          <div class="formula-box">
            $$\tau_{allow} \le \min(0.30 \cdot S_{yield}, 0.18 \cdot S_{ultimate}) \le 55\text{ MPa } (8,000\text{ psi})$$
          </div>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: Gearbox Intermediate Countershaft Sizing</h3>
            <p><strong>Design Scenario:</strong> A dual-stage industrial gearbox countershaft transmits $P = 30\text{ kW}$ at a rotational speed of $N = 450\text{ RPM}$. Transverse forces from an overhung helical pinion generate a maximum resultant bending moment of $M = 520\text{ N}\cdot\text{m}$. The shaft is manufactured from hot-rolled AISI 1045 carbon steel ($S_{yield} = 310\text{ MPa}$, $S_{ult} = 565\text{ MPa}$) and features standard profile keyways. The application experiences moderate shock loading ($K_m = 1.75, K_t = 1.25$). Determine nominal torque, equivalent design torque, and size the minimum solid shaft diameter.</p>
            
            <p><strong>Step 1: Calculate Nominal Transmitted Torque ($T$)</strong></p>
            <div class="formula-box">
              $$T = \frac{9548.8 \times 30\text{ kW}}{450\text{ RPM}} = 636.59\text{ N}\cdot\text{m}$$
            </div>

            <p><strong>Step 2: Determine Effective Allowable Design Shear Stress ($\tau_{allow}$)</strong></p>
            <div class="formula-box">
              $$0.30 \times S_y = 0.30 \times 310 = 93.0\text{ MPa}, \quad 0.18 \times S_{ut} = 0.18 \times 565 = 101.7\text{ MPa}$$
              $$\text{ASME Baseline Cap: } \tau_{allow} = 55.0\text{ MPa}$$
              $$\text{Apply 25% Keyway De-rating: } \tau_{eff} = 55.0 \times 0.75 = 41.25\text{ MPa} = 41.25\text{ N/mm}^2$$
            </div>

            <p><strong>Step 3: Calculate Equivalent Design Torsional Moment ($T_e$)</strong></p>
            <div class="formula-box">
              $$K_m \times M = 1.75 \times 520 = 910.0\text{ N}\cdot\text{m}$$
              $$K_t \times T = 1.25 \times 636.59 = 795.74\text{ N}\cdot\text{m}$$
              $$T_e = \sqrt{(910.0)^2 + (795.74)^2} = \sqrt{828,100 + 633,202} = \sqrt{1,461,302} \approx 1,208.84\text{ N}\cdot\text{m} = 1,208,843\text{ N}\cdot\text{mm}$$
            </div>

            <p><strong>Step 4: Calculate Minimum Required Solid Shaft Diameter ($d_{min}$)</strong></p>
            <div class="formula-box">
              $$d_{min} = \sqrt[3]{\frac{16 \times 1,208,843\text{ N}\cdot\text{mm}}{\pi \times 41.25\text{ N/mm}^2}} = \sqrt[3]{\frac{19,341,488}{129.59}} = \sqrt[3]{149,251} \approx 53.05\text{ mm}$$
            </div>
            <p>
              <strong>Engineering Sizing Selection:</strong> Consulting standard commercial shafting stock bar diameters (ISO 286 / ANSI B4.1), the design engineer selects a standard <strong>$55\text{ mm}$</strong> (or $2.25\text{ inch}$) diameter shaft. This provides a safety margin of $\approx 11.5\%$ above the theoretical minimum requirement, fully accommodating bearing seating shoulders and fillet radii stress relief.
            </p>
          </div>

          <h2>Torsional Rigidity and Lateral Critical Whirl Frequency</h2>
          <p>
            In high-speed machinery, satisfying static and fatigue stress criteria alone does not guarantee reliable operation. Transmission shafts must also satisfy two critical dynamic stiffness constraints:
          </p>
          <ol>
            <li><strong>Torsional Rigidity (Angular Deflection Limit):</strong> To prevent timing errors in cam drives or excessive tooth contact misalignment in precision gearboxes, angular twist ($\theta$) is strictly restricted (typically $\theta \le 0.25^\circ \text{ to } 1.0^\circ$ per meter of span):
              <div class="formula-box">
                $$\theta = \frac{T \cdot L}{G \cdot J} \le \theta_{allow}$$
              </div>
              Where $G \approx 79.3\text{ GPa}$ is the shear modulus of carbon steel and $J = \frac{\pi d^4}{32}$ is polar moment of inertia.
            </li>
            <li><strong>Lateral Critical Whirling Speed (Rayleigh Method):</strong> Rotating shafts exhibit natural lateral vibration frequencies. If rotational speed ($N$) approaches the first natural flexural frequency ($\omega_{cr}$), slight center-of-mass eccentricity creates runaway centrifugal whirling forces that can fracture bearing supports. Operating speeds must remain safely separated from critical speed ($N \le 0.75 N_{cr}$ or $N \ge 1.25 N_{cr}$).
            </li>
          </ol>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Driveline &amp; Machine Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="power-to-torque-calculator.html">Power to Torque Calculator</a></li>
            <li><a href="torque-calculator.html">Torque &amp; Shaft Power</a></li>
            <li><a href="bearing-life-calculator.html">Bearing Life (ISO 281)</a></li>
            <li><a href="pulley-rpm-calculator.html">Pulley RPM &amp; Belt Speed</a></li>
            <li><a href="bolt-torque-calculator.html">Bolt Torque &amp; Preload</a></li>
            <li><a href="flywheel-energy-calculator.html">Flywheel Energy Storage</a></li>
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
      const calcBtn = document.getElementById('calcShaftBtn');
      const resetBtn = document.getElementById('resetShaftBtn');
      const resultBox = document.getElementById('shaftResultBox');

      const shaftType = document.getElementById('shaftType');
      const grpHollowRatio = document.getElementById('grpHollowRatio');
      const materialYield = document.getElementById('materialYield');
      const tauAllow = document.getElementById('tauAllow');
      const hasKeyway = document.getElementById('hasKeyway');
      const serviceShock = document.getElementById('serviceShock');

      shaftType.addEventListener('change', function() {
        if (this.value === 'hollow') {
          grpHollowRatio.style.display = 'block';
        } else {
          grpHollowRatio.style.display = 'none';
        }
      });

      materialYield.addEventListener('change', function() {
        if (this.value !== 'custom') {
          tauAllow.value = this.value;
        }
      });

      function calculateShaft() {
        const t_Nm = parseFloat(document.getElementById('torqueInput').value) || 0;
        const m_Nm = parseFloat(document.getElementById('bendingInput').value) || 0;
        const baseTau = parseFloat(tauAllow.value);
        const kwFactor = parseFloat(hasKeyway.value);
        const isHollow = shaftType.value === 'hollow';
        const kRatioVal = parseFloat(document.getElementById('kRatio').value) || 0.6;

        if (isNaN(baseTau) || baseTau <= 0) {
          alert('Please enter a valid allowable stress.');
          return;
        }
        if (t_Nm === 0 && m_Nm === 0) {
          alert('Please enter at least one torque or bending moment.');
          return;
        }

        // Determine shock factors
        let km = 1.5;
        let kt = 1.25;
        const shockMode = serviceShock.value;
        if (shockMode === 'gradual') { km = 1.5; kt = 1.0; }
        else if (shockMode === 'minor') { km = 1.5; kt = 1.25; }
        else if (shockMode === 'heavy') { km = 2.0; kt = 1.5; }
        else if (shockMode === 'extreme') { km = 3.0; kt = 2.0; }

        // Equivalent moments
        const km_m = km * m_Nm;
        const kt_t = kt * t_Nm;
        const te_Nm = Math.sqrt(Math.pow(km_m, 2) + Math.pow(kt_t, 2));
        const me_Nm = 0.5 * (km_m + te_Nm);

        // Effective allowable shear stress (MPa -> N/mm^2)
        const effTau = baseTau * kwFactor;

        // Equivalent torque in N*mm
        const te_Nmm = te_Nm * 1000.0;

        let d_min_mm = 0;
        let di_mm = 0;

        if (!isHollow) {
          // Solid shaft d = ( (16 * Te) / (pi * tau) )^(1/3)
          d_min_mm = Math.cbrt((16.0 * te_Nmm) / (Math.PI * effTau));
        } else {
          // Hollow shaft do = ( (16 * Te) / (pi * tau * (1 - k^4)) )^(1/3)
          const k4 = Math.pow(kRatioVal, 4);
          d_min_mm = Math.cbrt((16.0 * te_Nmm) / (Math.PI * effTau * (1.0 - k4)));
          di_mm = d_min_mm * kRatioVal;
        }

        // Recommend next standard diameter
        const stdSizes = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 110, 120, 130, 140, 150, 160, 180, 200];
        let stdRec = d_min_mm;
        for (let s of stdSizes) {
          if (s >= d_min_mm) {
            stdRec = s;
            break;
          }
        }

        // Display results
        document.getElementById('resOuterDia').textContent = d_min_mm.toFixed(2) + ' mm (' + (d_min_mm / 25.4).toFixed(2) + ' in)';
        document.getElementById('resStdDia').textContent = stdRec + ' mm standard bar stock';
        document.getElementById('resEquivTorque').textContent = te_Nm.toFixed(1) + ' N·m (' + (te_Nm * 0.737562).toFixed(1) + ' lb·ft)';
        document.getElementById('resEquivBending').textContent = me_Nm.toFixed(1) + ' N·m';
        document.getElementById('resEffStress').textContent = effTau.toFixed(2) + ' MPa (' + (effTau * 145.038).toFixed(0) + ' psi)';
        document.getElementById('resInnerDia').textContent = isHollow ? (di_mm.toFixed(1) + ' mm bore') : 'N/A (Solid Shaft)';

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculateShaft);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
      });

      calculateShaft();
    });
  </script>
</body>
</html>
"""

def main():
    with open("reynolds-number-calculator.html", "w", encoding="utf-8") as f:
        f.write(TOOL_3_HTML.strip() + "\n")
    print("[PASS] reynolds-number-calculator.html generated successfully!")

    with open("shaft-diameter-calculator.html", "w", encoding="utf-8") as f:
        f.write(TOOL_4_HTML.strip() + "\n")
    print("[PASS] shaft-diameter-calculator.html generated successfully!")

if __name__ == "__main__":
    main()
