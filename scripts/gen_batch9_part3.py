# -*- coding: utf-8 -*-
"""
Script to generate Batch 9 Part 3 tools:
5. flywheel-energy-calculator.html
6. gear-module-calculator.html
"""
import os

TOOL_5_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Flywheel Energy Calculator | Rotational Kinetic Energy & Rim Stress</title>
  <meta name="description" content="Calculate flywheel rotational kinetic energy, mass moment of inertia, coefficient of speed fluctuation, and centrifugal hoop stress per ASME and ISO mechanical engineering standards.">
  <link rel="canonical" href="https://calchub.cloud/flywheel-energy-calculator.html">
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
        "name": "Flywheel Energy Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Mechanical energy storage calculation engine determining flywheel kinetic energy E = 0.5*I*omega^2, fluctuation energy Delta_E, moment of inertia, and centrifugal hoop stress.",
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
            "name": "What is the formula for rotational kinetic energy of a flywheel?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The kinetic energy stored in a rotating flywheel is: E = 0.5 * I * omega^2, where I is the mass moment of inertia in kg*m^2 (or lb*ft^2) and omega is angular velocity in radians per second: omega = (2 * pi * N) / 60, with N representing rotational speed in RPM."
            }
          },
          {
            "@type": "Question",
            "name": "How is the usable fluctuation energy (Delta E) calculated for punching presses or engines?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "During an operational cycle, a flywheel delivers energy by decelerating from maximum speed (omega_1) to minimum speed (omega_2). The usable energy release is: Delta_E = 0.5 * I * (omega_1^2 - omega_2^2) = I * omega_avg^2 * C_s, where C_s is the coefficient of speed fluctuation: C_s = (omega_1 - omega_2) / omega_avg."
            }
          },
          {
            "@type": "Question",
            "name": "How is centrifugal hoop stress calculated in a rotating flywheel rim?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Centrifugal forces create tensile tangential stress (hoop stress) across the rim: sigma_hoop = rho * v^2 = rho * (omega * R)^2, where rho is material density (e.g., 7,200 kg/m^3 for gray cast iron, 7,850 kg/m^3 for steel) and v is linear rim velocity in m/s. Rim stress depends solely on material density and peripheral speed, independent of rim cross-sectional area."
            }
          },
          {
            "@type": "Question",
            "name": "What are maximum safe peripheral rim speeds for flywheel materials?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Standard gray cast iron flywheels are strictly restricted to peripheral speeds below 30 - 35 m/s (6,000 - 7,000 ft/min) due to low tensile strength. Ductile/nodular iron flywheels can operate up to 50 m/s. Forged alloy steel rotors safely achieve 100 - 150 m/s. Advanced high-speed vacuum flywheel energy storage systems (FESS) utilizing carbon-fiber composite rotors achieve tip speeds exceeding 800 - 1,000 m/s."
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
      <span>Flywheel Energy Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">ASME Mechanical Power &amp; FESS Standards</div>
          <h1 class="calc-title">Flywheel Energy Calculator</h1>
          <p class="calc-tagline">Calculate rotational kinetic energy storage, usable fluctuation energy, mass moment of inertia, centrifugal hoop stress, and burst velocity limits.</p>
        </header>

        <div class="tool-card">
          <form id="flywheelCalcForm">
            <div class="calc-grid">
              <div class="form-group">
                <label for="rotorGeometry">Rotor Cross-Section Geometry</label>
                <select id="rotorGeometry">
                  <option value="solidDisc" selected>Solid Uniform Disc / Cylinder</option>
                  <option value="hollowRim">Hollow Cylindrical Rim (Thick Rim)</option>
                  <option value="thinRim">Thin Annular Rim (Rim with Thin Web)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="flywheelUnits">Engineering Units</label>
                <select id="flywheelUnits">
                  <option value="metric" selected>Metric (kg, mm, Joules, MPa)</option>
                  <option value="imperial">Imperial (lbs, in, ft-lbf, PSI)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="materialPreset">Rotor Construction Material</label>
                <select id="materialPreset">
                  <option value="castIron" selected>Class 35 Gray Cast Iron (&rho; = 7200 kg/m³)</option>
                  <option value="ductileIron">Ductile / Nodular Iron (&rho; = 7100 kg/m³)</option>
                  <option value="structuralSteel">Structural Carbon Steel AISI 1045 (&rho; = 7850 kg/m³)</option>
                  <option value="alloySteel">High-Strength 4340 Alloy Steel (&rho; = 7850 kg/m³)</option>
                  <option value="carbonFiber">Carbon-Fiber Epoxy Composite (&rho; = 1600 kg/m³)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="outerDiam" id="lblOuterDiam">Outer Diameter (Do) [mm]</label>
                <input type="number" id="outerDiam" step="10" min="50" max="10000" value="600">
              </div>

              <div class="form-group" id="grpHollowInner" style="display: none;">
                <label for="innerDiam" id="lblInnerDiam">Inner Rim Diameter (Di) [mm]</label>
                <input type="number" id="innerDiam" step="10" min="10" max="9500" value="450">
              </div>

              <div class="form-group">
                <label for="rotorAxialWidth" id="lblRotorAxialWidth">Axial Width / Thickness (b) [mm]</label>
                <input type="number" id="rotorAxialWidth" step="5" min="5" max="2000" value="100">
              </div>

              <div class="form-group">
                <label for="maxRpm">Maximum Operating Speed (N1) [RPM]</label>
                <input type="number" id="maxRpm" step="50" min="10" max="100000" value="1800">
              </div>

              <div class="form-group">
                <label for="minRpm">Minimum Discharged Speed (N2) [RPM]</label>
                <input type="number" id="minRpm" step="50" min="0" max="99000" value="1600">
              </div>
            </div>

            <div class="calc-actions">
              <button type="button" id="calcFlywheelBtn" class="btn btn-primary">Calculate Flywheel Dynamics</button>
              <button type="reset" id="resetFlywheelBtn" class="btn btn-secondary">Reset Defaults</button>
            </div>
          </form>

          <div id="flywheelResultBox" class="results-container" style="display: none;">
            <h3>Flywheel Kinetic Energy & Stress Analysis</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label">Total Stored Kinetic Energy (at N1)</span>
                <span id="resTotalEnergy" class="result-value">-- kJ</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Usable Fluctuation Energy (&Delta;E)</span>
                <span id="resUsableEnergy" class="result-value">-- kJ</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Mass Moment of Inertia (I)</span>
                <span id="resMomentInertia" class="result-value">-- kg·m²</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Calculated Rotor Mass (m)</span>
                <span id="resRotorMass" class="result-value">-- kg</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Centrifugal Hoop Stress (&sigma;_hoop)</span>
                <span id="resHoopStress" class="result-value">-- MPa</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Linear Rim Tip Velocity (v_rim)</span>
                <span id="resRimVelocity" class="result-value">-- m/s</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Speed Fluctuation Coefficient (Cs)</span>
                <span id="resFluctCoeff" class="result-value">--</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Structural Safety Status</span>
                <span id="resSafetyStatus" class="result-value">--</span>
              </div>
            </div>
            <div id="flywheelNotesBox" style="margin-top: 1rem; color: #1e40af; background: #eff6ff; border: 1px solid #bfdbfe; padding: 0.75rem; border-radius: 6px;"></div>
          </div>
        </div>

        <article class="article-body">
          <h2>Mechanical Energy Storage & Flywheel Dynamics Principles</h2>
          <p>A flywheel is a heavy, rotating mechanical wheel designed to store kinetic energy during periods where energy supply exceeds demand and discharge that energy during peak operational loads. From classical reciprocating internal combustion engines and heavy industrial stamping presses to modern grid-scale <strong>Flywheel Energy Storage Systems (FESS)</strong> supporting renewable microgrids, flywheels smooth cyclical torque ripples, dampen torsional resonance, and provide instantaneous, high-power bursts.</p>

          <p>The mathematical sizing of a flywheel involves balancing two competing physical phenomena: maximizing the <strong>mass moment of inertia</strong> (\(I\)) to maximize stored kinetic energy while strictly restricting <strong>centrifugal hoop stress</strong> (\(\sigma_{\text{hoop}}\)) below the ultimate tensile strength of the rotor material to prevent catastrophic, explosive burst failure.</p>

          <h2>Rotational Kinetic Energy Formulations</h2>
          <p>The total kinetic energy (\(E_k\)) stored within a rotating body is governed by its mass moment of inertia and angular velocity:</p>

          <div class="formula-box">
            $$E_k = \frac{1}{2} I \omega^2 = \frac{1}{2} I \left(\frac{2\pi N}{60}\right)^2 \quad [\text{Joules or ft-lbf}]$$
          </div>

          <p>Where:</p>
          <ul>
            <li><strong>\(I\)</strong>: Mass moment of inertia about the axis of rotation (\(\text{kg}\cdot\text{m}^2\) or \(\text{lb}\cdot\text{ft}^2\)).</li>
            <li><strong>\(\omega\)</strong>: Angular velocity in radians per second (\(\text{rad/s}\)).</li>
            <li><strong>\(N\)</strong>: Rotational frequency in revolutions per minute (\(\text{RPM}\)).</li>
          </ul>

          <p>Crucially, because kinetic energy scales with the <em>square of rotational speed</em> (\(\omega^2\)), doubling the RPM quadruples the stored energy. This fundamental principle drives modern FESS designs toward ultra-high-speed composite rotors operating in vacuum enclosures on magnetic bearings.</p>

          <h2>Usable Fluctuation Energy & Coefficient of Fluctuation</h2>
          <p>In industrial production machinery (such as mechanical punch presses, shears, rock crushers, and diesel generators), the flywheel does not decelerate to a complete standstill during normal operation. Instead, it operates between a maximum speed (\(N_1\)) and a minimum speed (\(N_2\)). The <strong>usable fluctuation energy</strong> (\(\Delta E\)) extracted during this cycle is:</p>

          <div class="formula-box">
            $$\Delta E = \frac{1}{2} I (\omega_1^2 - \omega_2^2) = I \omega_{\text{avg}}^2 \cdot C_s$$
          </div>

          <p>Where the mean angular velocity (\(\omega_{\text{avg}}\)) and the <strong>coefficient of speed fluctuation</strong> (\(C_s\)) are defined as:</p>

          <div class="formula-box">
            $$\omega_{\text{avg}} = \frac{\omega_1 + \omega_2}{2} \quad \text{and} \quad C_s = \frac{\omega_1 - \omega_2}{\omega_{\text{avg}}}$$
          </div>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Machine Application</th>
                <th>Permissible Fluctuation (\(C_s\))</th>
                <th>Operational Rationale</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>AC Electric Synchronous Generators</td>
                <td>0.003 &ndash; 0.005 (0.3% &ndash; 0.5%)</td>
                <td>Mandatory to preserve tight 50/60 Hz grid frequency stability.</td>
              </tr>
              <tr>
                <td>Precision Machine Tools & Grinders</td>
                <td>0.005 &ndash; 0.010 (0.5% &ndash; 1.0%)</td>
                <td>Prevents chatter marks and preserves micro-inch surface finish.</td>
              </tr>
              <tr>
                <td>Centrifugal Pumps & Blowers</td>
                <td>0.030 &ndash; 0.050 (3.0% &ndash; 5.0%)</td>
                <td>Tolerates moderate hydraulic head and pressure variations.</td>
              </tr>
              <tr>
                <td>Heavy Punching & Stamping Presses</td>
                <td>0.100 &ndash; 0.200 (10% &ndash; 20%)</td>
                <td>Delivers massive energy bursts during brief stamping stroke.</td>
              </tr>
              <tr>
                <td>Rock Jaw Crushers & Ball Mills</td>
                <td>0.150 &ndash; 0.250 (15% &ndash; 25%)</td>
                <td>Absorbs violent shock loads without stalling electric motor.</td>
              </tr>
            </tbody>
          </table>

          <h2>Mass Moment of Inertia for Common Flywheel Profiles</h2>
          <p>The mass distribution relative to the rotational axis determines inertia. Sizing formulas vary by geometric configuration:</p>

          <h3>1. Solid Uniform Disc / Cylinder</h3>
          <div class="formula-box">
            $$m = \rho \cdot \pi \left(\frac{D_o}{2}\right)^2 b \quad \implies \quad I = \frac{1}{2} m R_o^2 = \frac{1}{8} m D_o^2$$
          </div>

          <h3>2. Hollow Cylindrical Rim (Heavy Annular Ring)</h3>
          <div class="formula-box">
            $$m = \rho \cdot \pi \left( R_o^2 - R_i^2 \right) b \quad \implies \quad I = \frac{1}{2} m \left( R_o^2 + R_i^2 \right) = \frac{1}{8} m \left( D_o^2 + D_i^2 \right)$$
          </div>
          <p>Hollow rim configurations concentrate over 90% of mass at the outer perimeter, delivering substantially higher inertia per kilogram of material compared to solid discs.</p>

          <h2>Centrifugal Rim Stress (Hoop Stress) & Burst Velocity</h2>
          <p>Every element of a spinning rim experiences radical outward centrifugal acceleration (\(a_c = v^2 / R\)). This acceleration creates uniform tangential tensile stress (hoop stress) across the rim section:</p>

          <div class="formula-box">
            $$\sigma_{\text{hoop}} = \rho \cdot v_{\text{rim}}^2 = \rho \cdot \left(\omega \cdot R_o\right)^2 \quad [\text{Pascals or PSI}]$$
          </div>

          <p>This reveals a profound engineering reality: <strong>rim stress depends strictly on material density and peripheral linear velocity</strong>, completely independent of rim thickness or cross-sectional area. The maximum theoretical burst tip speed (\(v_{\text{burst}}\)) is:</p>

          <div class="formula-box">
            $$v_{\text{burst}} = \sqrt{\frac{\sigma_{\text{UTS}}}{\rho}}$$
          </div>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Rotor Material</th>
                <th>Density \(\rho\) (\(\text{kg/m}^3\))</th>
                <th>Tensile Strength \(\sigma_u\) (MPa)</th>
                <th>Safe Max Rim Speed (m/s)</th>
                <th>Specific Energy (Wh/kg)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Class 35 Gray Cast Iron</td>
                <td>7,200</td>
                <td>240</td>
                <td>30 &ndash; 35 m/s</td>
                <td>~3 &ndash; 5 Wh/kg</td>
              </tr>
              <tr>
                <td>Ductile Iron 80-55-06</td>
                <td>7,100</td>
                <td>550</td>
                <td>45 &ndash; 55 m/s</td>
                <td>~8 &ndash; 12 Wh/kg</td>
              </tr>
              <tr>
                <td>Alloy Steel AISI 4340 (Q&T)</td>
                <td>7,850</td>
                <td>1,100</td>
                <td>100 &ndash; 140 m/s</td>
                <td>~25 &ndash; 40 Wh/kg</td>
              </tr>
              <tr>
                <td>High-Modulus Carbon Fiber</td>
                <td>1,600</td>
                <td>2,400</td>
                <td>600 &ndash; 900 m/s</td>
                <td>~100 &ndash; 200 Wh/kg</td>
              </tr>
            </tbody>
          </table>

          <div class="worked-example-card">
            <h3>Step-by-Step Worked Case Study: Stamping Press Flywheel Sizing</h3>
            <p><strong>Design Scenario:</strong> An engineer is sizing a cast iron rim flywheel for a 50-ton mechanical punch press. The press cycle requires 18 kJ of energy during each 0.3-second stamping stroke, while the electric motor runs between 1,800 RPM and 1,600 RPM.</p>
            <ul>
              <li>Flywheel rim outer diameter: \(D_o = 600\text{ mm}\) (\(R_o = 0.30\text{ m}\)).</li>
              <li>Rim inner diameter: \(D_i = 450\text{ mm}\) (\(R_i = 0.225\text{ m}\)).</li>
              <li>Axial width: \(b = 100\text{ mm}\) (\(0.10\text{ m}\)).</li>
              <li>Material: Class 35 Gray Cast Iron (\(\rho = 7,200\text{ kg/m}^3\), \(\sigma_u = 240\text{ MPa}\)).</li>
              <li>Speeds: \(N_1 = 1,800\text{ RPM}\), \(N_2 = 1,600\text{ RPM}\).</li>
            </ul>

            <p><strong>Step 1: Compute rotor mass and moment of inertia</strong></p>
            <div class="formula-box">
              $$m = \rho \cdot \pi (R_o^2 - R_i^2) b = 7200 \cdot \pi (0.30^2 - 0.225^2) \cdot 0.10$$
              $$m = 7200 \cdot \pi (0.09 - 0.0506) \cdot 0.10 = 7200 \cdot \pi \cdot 0.0394 \cdot 0.10 = 89.12\text{ kg}$$
              $$I = \frac{1}{2} m (R_o^2 + R_i^2) = \frac{1}{2} (89.12) (0.09 + 0.0506) = 44.56 \times 0.1406 = 6.265\text{ kg}\cdot\text{m}^2$$
            </div>

            <p><strong>Step 2: Calculate angular velocities and stored kinetic energy</strong></p>
            <div class="formula-box">
              $$\omega_1 = \frac{2\pi \cdot 1800}{60} = 188.50\text{ rad/s}, \quad \omega_2 = \frac{2\pi \cdot 1600}{60} = 167.55\text{ rad/s}$$
              $$E_{\text{total}} = \frac{1}{2} I \omega_1^2 = \frac{1}{2} (6.265) (188.50)^2 = 111,304\text{ J} = 111.3\text{ kJ}$$
            </div>

            <p><strong>Step 3: Calculate usable fluctuation energy (\(\Delta E\))</strong></p>
            <div class="formula-box">
              $$\Delta E = \frac{1}{2} (6.265) \left[ (188.50)^2 - (167.55)^2 \right] = 3.1325 \times [35532 - 28073] = 23,365\text{ J} = 23.37\text{ kJ}$$
            </div>
            <p>Because \(\Delta E = 23.4\text{ kJ}\) exceeds the required 18 kJ punch demand, the flywheel satisfies the energy requirement.</p>

            <p><strong>Step 4: Check rim tip velocity and centrifugal hoop stress</strong></p>
            <div class="formula-box">
              $$v_{\text{rim}} = \omega_1 \cdot R_o = 188.50 \cdot 0.30 = 56.55\text{ m/s}$$
              $$\sigma_{\text{hoop}} = \rho \cdot v_{\text{rim}}^2 = 7200 \cdot (56.55)^2 = 7200 \cdot 3197.9 = 23.02\text{ MPa}$$
            </div>
            <p><strong>Safety Evaluation:</strong> Gray cast iron has an ultimate strength of 240 MPa. The hoop stress of 23.0 MPa provides a generous safety factor of \(SF = 240 / 23.0 = 10.4\), guaranteeing secure fatigue life.</p>
          </div>

          <h2>Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3>Why are modern grid-scale flywheels built from carbon fiber rather than steel?</h3>
            <p>In kinetic energy storage, specific energy (energy per unit mass, Wh/kg) is governed by the specific strength of the material (\(\sigma_u / \rho\)). Carbon-fiber composites have a very low density (1,600 kg/m³) combined with massive tensile strength (> 2,000 MPa), allowing tip speeds up to 1,000 m/s and delivering 5 to 10 times higher energy density per kilogram than forged alloy steels.</p>
          </div>

          <div class="faq-item">
            <h3>What causes flywheel burst failures and how are they contained?</h3>
            <p>Flywheel burst failures occur when centrifugal hoop stresses exceed material tensile limits or when micro-cracks propagate under cyclic fatigue. In metallic flywheels, failure produces massive, razor-sharp fragmentation projectiles capable of breaching heavy factory walls. Modern FESS units house the rotor in sub-surface steel vacuum containment vessels lined with energy-absorbing honeycomb liners.</p>
          </div>

          <div class="faq-item">
            <h3>Why is dynamic balancing critical for high-speed flywheels?</h3>
            <p>Any mass eccentricity (\(e\)) between the geometric center and center of mass creates a rotating centrifugal unbalance force: \(F_{\text{unbalance}} = m \cdot e \cdot \omega^2\). At high speeds, even a few grams of unbalance creates thousands of pounds of cyclic force on bearings, causing destructive resonant vibration and premature bearing seizure.</p>
          </div>

          <div class="faq-item">
            <h3>How do vacuum enclosures and magnetic bearings reduce flywheel standby losses?</h3>
            <p>At high peripheral speeds (> 200 m/s), aerodynamic air friction (windage drag) generates extreme parasitic power loss and thermal buildup. Enclosing the flywheel rotor in a high-vacuum vessel (< 0.001 mbar) eliminates aerodynamic drag, while non-contact active magnetic bearings (AMB) eliminate mechanical contact friction, reducing standby self-discharge losses to less than 1% to 2% per hour.</p>
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
    const DENSITIES_METRIC = {
      castIron: 7200,
      ductileIron: 7100,
      structuralSteel: 7850,
      alloySteel: 7850,
      carbonFiber: 1600
    };

    const TENSILE_LIMITS_MPA = {
      castIron: 240,
      ductileIron: 550,
      structuralSteel: 600,
      alloySteel: 1100,
      carbonFiber: 2200
    };

    const rotorGeometrySelect = document.getElementById('rotorGeometry');
    const flywheelUnitsSelect = document.getElementById('flywheelUnits');
    const materialPresetSelect = document.getElementById('materialPreset');
    const outerDiamInput = document.getElementById('outerDiam');
    const innerDiamInput = document.getElementById('innerDiam');
    const rotorAxialWidthInput = document.getElementById('rotorAxialWidth');
    const maxRpmInput = document.getElementById('maxRpm');
    const minRpmInput = document.getElementById('minRpm');

    const lblOuterDiam = document.getElementById('lblOuterDiam');
    const lblInnerDiam = document.getElementById('lblInnerDiam');
    const lblRotorAxialWidth = document.getElementById('lblRotorAxialWidth');
    const grpHollowInner = document.getElementById('grpHollowInner');

    const flywheelResultBox = document.getElementById('flywheelResultBox');
    const resTotalEnergy = document.getElementById('resTotalEnergy');
    const resUsableEnergy = document.getElementById('resUsableEnergy');
    const resMomentInertia = document.getElementById('resMomentInertia');
    const resRotorMass = document.getElementById('resRotorMass');
    const resHoopStress = document.getElementById('resHoopStress');
    const resRimVelocity = document.getElementById('resRimVelocity');
    const resFluctCoeff = document.getElementById('resFluctCoeff');
    const resSafetyStatus = document.getElementById('resSafetyStatus');
    const flywheelNotesBox = document.getElementById('flywheelNotesBox');

    rotorGeometrySelect.addEventListener('change', function() {
      if (this.value === 'solidDisc') {
        grpHollowInner.style.display = 'none';
      } else {
        grpHollowInner.style.display = 'block';
      }
      calculateFlywheel();
    });

    flywheelUnitsSelect.addEventListener('change', function() {
      const isMetric = this.value === 'metric';
      if (isMetric) {
        lblOuterDiam.textContent = "Outer Diameter (Do) [mm]";
        lblInnerDiam.textContent = "Inner Rim Diameter (Di) [mm]";
        lblRotorAxialWidth.textContent = "Axial Width / Thickness (b) [mm]";
        outerDiamInput.value = 600;
        innerDiamInput.value = 450;
        rotorAxialWidthInput.value = 100;
      } else {
        lblOuterDiam.textContent = "Outer Diameter (Do) [in]";
        lblInnerDiam.textContent = "Inner Rim Diameter (Di) [in]";
        lblRotorAxialWidth.textContent = "Axial Width / Thickness (b) [in]";
        outerDiamInput.value = 24.0;
        innerDiamInput.value = 18.0;
        rotorAxialWidthInput.value = 4.0;
      }
      calculateFlywheel();
    });

    function calculateFlywheel() {
      const geom = rotorGeometrySelect.value;
      const isMetric = flywheelUnitsSelect.value === 'metric';
      const matKey = materialPresetSelect.value;
      const densityMetric = DENSITIES_METRIC[matKey] || 7200;
      const maxTensileMpa = TENSILE_LIMITS_MPA[matKey] || 240;

      let Do_raw = parseFloat(outerDiamInput.value);
      let Di_raw = parseFloat(innerDiamInput.value);
      let b_raw = parseFloat(rotorAxialWidthInput.value);
      let N1 = parseFloat(maxRpmInput.value);
      let N2 = parseFloat(minRpmInput.value);

      if (isNaN(Do_raw) || Do_raw <= 0) Do_raw = isMetric ? 600 : 24;
      if (isNaN(Di_raw) || Di_raw <= 0) Di_raw = isMetric ? 450 : 18;
      if (isNaN(b_raw) || b_raw <= 0) b_raw = isMetric ? 100 : 4;
      if (isNaN(N1) || N1 <= 0) N1 = 1800;
      if (isNaN(N2) || N2 < 0) N2 = 1600;
      if (N2 > N1) {
        const tmp = N1; N1 = N2; N2 = tmp;
      }

      // Standardize to Metric meters
      const Do_m = isMetric ? (Do_raw / 1000) : (Do_raw * 0.0254);
      let Di_m = isMetric ? (Di_raw / 1000) : (Di_raw * 0.0254);
      const b_m = isMetric ? (b_raw / 1000) : (b_raw * 0.0254);

      if (geom === 'solidDisc') {
        Di_m = 0;
      } else {
        if (Di_m >= Do_m) Di_m = Do_m * 0.75;
      }

      const Ro_m = Do_m / 2;
      const Ri_m = Di_m / 2;

      // Mass (kg)
      let volume_m3 = Math.PI * (Math.pow(Ro_m, 2) - Math.pow(Ri_m, 2)) * b_m;
      let mass_kg = volume_m3 * densityMetric;

      // Moment of Inertia (kg*m^2)
      let I_kgm2 = 0.5 * mass_kg * (Math.pow(Ro_m, 2) + Math.pow(Ri_m, 2));

      // Angular velocities (rad/s)
      const omega1 = (2 * Math.PI * N1) / 60;
      const omega2 = (2 * Math.PI * N2) / 60;
      const omegaAvg = (omega1 + omega2) / 2;

      // Kinetic Energies (Joules)
      const E_total_J = 0.5 * I_kgm2 * Math.pow(omega1, 2);
      const E_usable_J = 0.5 * I_kgm2 * (Math.pow(omega1, 2) - Math.pow(omega2, 2));

      // Speed Fluctuation Coefficient
      const Cs = (omega1 - omega2) / (omegaAvg > 0 ? omegaAvg : 1);

      // Linear Rim Speed (m/s)
      const v_rim_mps = omega1 * Ro_m;

      // Hoop Stress (sigma = rho * v^2)
      const sigma_hoop_Pa = densityMetric * Math.pow(v_rim_mps, 2);
      const sigma_hoop_Mpa = sigma_hoop_Pa / 1e6;

      // Safety Factor
      const sf = maxTensileMpa / sigma_hoop_Mpa;
      let safetyStatus = `Safe (SF = ${sf.toFixed(1)})`;
      let statusColor = "#166534";
      if (sf < 2.0) {
        safetyStatus = `Warning: High Stress (SF = ${sf.toFixed(2)})`;
        statusColor = "#b45309";
      }
      if (sf < 1.0) {
        safetyStatus = `CRITICAL DANGER: EXCEEDS BURST LIMIT`;
        statusColor = "#dc2626";
      }

      // Display conversions
      if (isMetric) {
        resTotalEnergy.textContent = (E_total_J / 1000).toFixed(2) + " kJ";
        resUsableEnergy.textContent = (E_usable_J / 1000).toFixed(2) + " kJ";
        resMomentInertia.textContent = I_kgm2.toFixed(3) + " kg·m²";
        resRotorMass.textContent = mass_kg.toFixed(1) + " kg";
        resHoopStress.textContent = sigma_hoop_Mpa.toFixed(2) + " MPa";
        resRimVelocity.textContent = v_rim_mps.toFixed(1) + " m/s";
      } else {
        // Imperial conversions
        const E_total_ftlb = E_total_J * 0.737562;
        const E_usable_ftlb = E_usable_J * 0.737562;
        const I_lbft2 = I_kgm2 * 23.73036;
        const mass_lbs = mass_kg * 2.20462;
        const sigma_psi = sigma_hoop_Mpa * 145.038;
        const v_rim_fpm = v_rim_mps * 196.85;

        resTotalEnergy.textContent = (E_total_ftlb / 1000).toFixed(2) + " kft·lbf";
        resUsableEnergy.textContent = (E_usable_ftlb / 1000).toFixed(2) + " kft·lbf";
        resMomentInertia.textContent = I_lbft2.toFixed(2) + " lb·ft²";
        resRotorMass.textContent = mass_lbs.toFixed(1) + " lbs";
        resHoopStress.textContent = sigma_psi.toFixed(0) + " PSI";
        resRimVelocity.textContent = v_rim_fpm.toFixed(0) + " ft/min";
      }

      resFluctCoeff.textContent = (Cs * 100).toFixed(2) + "% (Cs=" + Cs.toFixed(3) + ")";
      resSafetyStatus.textContent = safetyStatus;
      resSafetyStatus.style.color = statusColor;

      let notes = `<strong>Stress & Kinetic Dynamics:</strong> Rotating at <strong>${N1} RPM</strong>, the rotor tip speed reaches <strong>${v_rim_mps.toFixed(1)} m/s</strong>, generating <strong>${sigma_hoop_Mpa.toFixed(1)} MPa</strong> of centrifugal hoop stress. Usable energy between ${N1} and ${N2} RPM is <strong>${(E_usable_J / 1000).toFixed(2)} kJ</strong>.`;
      flywheelNotesBox.innerHTML = notes;

      flywheelResultBox.style.display = 'block';
    }

    document.getElementById('calcFlywheelBtn').addEventListener('click', calculateFlywheel);
    document.getElementById('resetFlywheelBtn').addEventListener('click', function() {
      setTimeout(calculateFlywheel, 50);
    });

    window.addEventListener('DOMContentLoaded', calculateFlywheel);
  </script>
</body>
</html>
"""

TOOL_6_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gear Module Calculator | ISO 53 Metric Spur & Helical Gear Dimensions</title>
  <meta name="description" content="Calculate metric gear module (m), diametral pitch (DP), pitch diameter, addendum, dedendum, outside diameter, and center distance per ISO 53 and AGMA standards.">
  <link rel="canonical" href="https://calchub.cloud/gear-module-calculator.html">
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
        "name": "Gear Module Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Metric involute gear dimensioning tool calculating gear module m = d/z, diametral pitch DP, addendum, root diameter, and center distance per ISO 53.",
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
            "name": "What is the gear module (m) and how is it defined?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The metric gear module (m) is the ratio of the gear pitch diameter (d in millimeters) to the number of teeth (z): m = d / z. It represents the unit size of a gear tooth. For two gears to mesh properly, they must have identical modules and pressure angles."
            }
          },
          {
            "@type": "Question",
            "name": "How do you convert between Metric Module (m) and Diametral Pitch (DP)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Diametral pitch (DP) is the imperial standard defined as teeth per inch of pitch diameter: DP = z / d_inches. The exact mathematical relationship between module and diametral pitch is: m = 25.4 / DP, and DP = 25.4 / m."
            }
          },
          {
            "@type": "Question",
            "name": "What are the standard tooth proportions for full-depth 20-degree involute gears per ISO 53?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Per ISO 53 standard rack: Addendum ha = 1.0 * m; Dedendum hf = 1.25 * m (bottom clearance c = 0.25 * m); Whole tooth depth h = 2.25 * m; Tip diameter da = d + 2*ha = m * (z + 2); Root diameter df = d - 2*hf = m * (z - 2.5); Circular pitch p = pi * m."
            }
          },
          {
            "@type": "Question",
            "name": "How is the center distance of a mating spur gear pair calculated?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For standard unshifted spur gears operating at nominal center distance: a = (d1 + d2) / 2 = m * (z1 + z2) / 2, where z1 and z2 are the tooth counts of the pinion and mating gear."
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
      <span>Gear Module Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">ISO 53 &amp; DIN 867 Spur Gear Standards</div>
          <h1 class="calc-title">Gear Module Calculator</h1>
          <p class="calc-tagline">Calculate metric gear module (m), Diametral Pitch (DP), pitch diameter, tip diameter, dedendum, and mating gear center distance per ISO 53 standards.</p>
        </header>

        <div class="tool-card">
          <form id="gearCalcForm">
            <div class="calc-grid">
              <div class="form-group">
                <label for="gearInputMode">Known Input Parameters</label>
                <select id="gearInputMode">
                  <option value="fromModule" selected>Specify Module (m) & Teeth (z)</option>
                  <option value="fromPitchDiam">Specify Pitch Diameter (d) & Teeth (z)</option>
                  <option value="fromDp">Specify Diametral Pitch (DP) & Teeth (z)</option>
                  <option value="fromTipDiam">Specify Outside Tip Diameter (da) & Teeth (z)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="pressureAngle">Standard Pressure Angle (&alpha;)</label>
                <select id="pressureAngle">
                  <option value="20" selected>20&deg; Full-Depth Involute (Universal Modern Standard)</option>
                  <option value="14.5">14.5&deg; Involute (Legacy / Low Separation Force)</option>
                  <option value="25">25&deg; Heavy Duty (High Load / Reduced Undercutting)</option>
                </select>
              </div>

              <div class="form-group" id="grpModule">
                <label for="moduleVal">Gear Module (m) [mm]</label>
                <select id="moduleVal">
                  <option value="1.0">m = 1.0 mm</option>
                  <option value="1.25">m = 1.25 mm</option>
                  <option value="1.5">m = 1.5 mm</option>
                  <option value="2.0">m = 2.0 mm</option>
                  <option value="2.5" selected>m = 2.5 mm</option>
                  <option value="3.0">m = 3.0 mm</option>
                  <option value="4.0">m = 4.0 mm</option>
                  <option value="5.0">m = 5.0 mm</option>
                  <option value="6.0">m = 6.0 mm</option>
                  <option value="8.0">m = 8.0 mm</option>
                  <option value="10.0">m = 10.0 mm</option>
                  <option value="custom">Custom Module...</option>
                </select>
              </div>

              <div class="form-group" id="grpCustomModule" style="display: none;">
                <label for="customModule">Custom Module (m) [mm]</label>
                <input type="number" id="customModule" step="0.1" min="0.1" max="50" value="2.5">
              </div>

              <div class="form-group" id="grpPitchDiam" style="display: none;">
                <label for="pitchDiam">Pitch Diameter (d) [mm]</label>
                <input type="number" id="pitchDiam" step="0.5" min="1" max="5000" value="75.0">
              </div>

              <div class="form-group" id="grpDp" style="display: none;">
                <label for="dpVal">Diametral Pitch (DP) [teeth/in]</label>
                <input type="number" id="dpVal" step="0.5" min="0.5" max="100" value="10.16">
              </div>

              <div class="form-group" id="grpTipDiam" style="display: none;">
                <label for="tipDiam">Outside Tip Diameter (da) [mm]</label>
                <input type="number" id="tipDiam" step="0.5" min="2" max="5000" value="80.0">
              </div>

              <div class="form-group">
                <label for="teethPinion">Pinion Tooth Count (z1)</label>
                <input type="number" id="teethPinion" min="5" max="500" step="1" value="24">
              </div>

              <div class="form-group">
                <label for="teethGear">Mating Gear Tooth Count (z2)</label>
                <input type="number" id="teethGear" min="5" max="1000" step="1" value="72">
              </div>

              <div class="form-group">
                <label for="helixAngle">Helix Angle (&beta;) [0&deg; = Spur Gear]</label>
                <input type="number" id="helixAngle" step="1" min="0" max="45" value="0">
              </div>
            </div>

            <div class="calc-actions">
              <button type="button" id="calcGearBtn" class="btn btn-primary">Calculate Gear Geometry</button>
              <button type="reset" id="resetGearBtn" class="btn btn-secondary">Reset Defaults</button>
            </div>
          </form>

          <div id="gearResultBox" class="results-container" style="display: none;">
            <h3>ISO 53 Involute Gear Dimensioning Results</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label">Metric Module (m)</span>
                <span id="resModule" class="result-value">-- mm</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Diametral Pitch (DP)</span>
                <span id="resDp" class="result-value">--</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Pinion Pitch Diameter (d1)</span>
                <span id="resD1" class="result-value">-- mm</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Mating Gear Pitch Diameter (d2)</span>
                <span id="resD2" class="result-value">-- mm</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Outside Tip Diameter (da1)</span>
                <span id="resDa1" class="result-value">-- mm</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Root Diameter (df1)</span>
                <span id="resDf1" class="result-value">-- mm</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Base Circle Diameter (db1)</span>
                <span id="resDb1" class="result-value">-- mm</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Mating Center Distance (a)</span>
                <span id="resCenterDist" class="result-value">-- mm</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Circular Pitch (p)</span>
                <span id="resCircPitch" class="result-value">-- mm</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Gear Ratio & Undercut Check</span>
                <span id="resRatioStatus" class="result-value">--</span>
              </div>
            </div>
            <div id="gearNotesBox" style="margin-top: 1rem; color: #1e40af; background: #eff6ff; border: 1px solid #bfdbfe; padding: 0.75rem; border-radius: 6px;"></div>
          </div>
        </div>

        <article class="article-body">
          <h2>Fundamentals of Involute Gear Tooth Geometry & Standardization</h2>
          <p>Gear tooth geometry represents one of the most rigorously standardized branches of mechanical engineering. To achieve conjugate tooth action—wherein rotating meshing teeth maintain a strictly constant instantaneous angular velocity ratio—gears utilize the <strong>involute of a circle</strong> profile. The fundamental parameter that dictates tooth proportions, bending strength, and interchangeability in the metric system is the <strong>Module (\(m\))</strong>, standardized internationally under <strong>ISO 53</strong> and <strong>DIN 867</strong>.</p>

          <p>Mating gears can only mesh properly if they share an identical module and identical operating pressure angle (\(\alpha\)). If two gears with different modules are forced into mesh, improper tooth contact, extreme edge loading, violent acoustic noise, and rapid tooth flank spalling will destroy the transmission within minutes.</p>

          <h2>Mathematical Formulations for Metric Module and Pitch Geometry</h2>
          <p>The module (\(m\)) is defined as the millimeters of pitch diameter per tooth. Mathematically:</p>

          <div class="formula-box">
            $$m = \frac{d}{z} \quad [\text{mm}] \quad \Longleftrightarrow \quad d = m \cdot z \quad [\text{mm}]$$
          </div>

          <p>Where:</p>
          <ul>
            <li><strong>\(m\)</strong>: Metric gear module in millimeters.</li>
            <li><strong>\(d\)</strong>: Reference pitch circle diameter in millimeters.</li>
            <li><strong>\(z\)</strong>: Total number of teeth on the gear.</li>
          </ul>

          <p>The <strong>circular pitch</strong> (\(p\)) is the circular arc distance measured along the pitch circle from a point on one tooth to the corresponding point on the adjacent tooth:</p>

          <div class="formula-box">
            $$p = \frac{\pi \cdot d}{z} = \pi \cdot m \quad [\text{mm}]$$
          </div>

          <h2>Metric Module vs. Imperial Diametral Pitch (DP)</h2>
          <p>While European, Japanese, and international machinery adheres strictly to the ISO metric module, North American manufacturing historically developed around <strong>Diametral Pitch (\(DP\))</strong>, defined as the number of teeth per inch of pitch diameter:</p>

          <div class="formula-box">
            $$DP = \frac{z}{d_{\text{inches}}} \quad [\text{in}^{-1}]$$
          </div>

          <p>Because \(1\text{ inch} = 25.4\text{ mm}\), the direct conversion between Metric Module and Diametral Pitch is an exact inverse relationship:</p>

          <div class="formula-box">
            $$m = \frac{25.4}{DP} \quad \Longleftrightarrow \quad DP = \frac{25.4}{m}$$
          </div>

          <p>Notice the inverse behavior: A <em>larger module</em> signifies a larger, stronger tooth. In contrast, a <em>higher diametral pitch</em> signifies a smaller, finer tooth.</p>

          <h2>ISO 53 Standard Full-Depth Tooth Proportions</h2>
          <p>For standard unshifted spur gears operating at a 20&deg; pressure angle per ISO 53 basic rack profile:</p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Tooth Dimension</th>
                <th>Standard ISO Formula</th>
                <th>Physical Engineering Significance</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Addendum (\(h_a\))</td>
                <td>\(h_a = 1.00 \cdot m\)</td>
                <td>Radial height of tooth above pitch circle.</td>
              </tr>
              <tr>
                <td>Dedendum (\(h_f\))</td>
                <td>\(h_f = 1.25 \cdot m\)</td>
                <td>Radial depth of tooth below pitch circle (includes clearance).</td>
              </tr>
              <tr>
                <td>Bottom Clearance (\(c\))</td>
                <td>\(c = h_f - h_a = 0.25 \cdot m\)</td>
                <td>Radial gap between mating tip and root to prevent bottoming out.</td>
              </tr>
              <tr>
                <td>Whole Depth (\(h\))</td>
                <td>\(h = h_a + h_f = 2.25 \cdot m\)</td>
                <td>Total radial tooth depth from tip to root.</td>
              </tr>
              <tr>
                <td>Tip Outside Diameter (\(d_a\))</td>
                <td>\(d_a = d + 2h_a = m(z + 2)\)</td>
                <td>Maximum blank diameter turned on lathe before hobbing teeth.</td>
              </tr>
              <tr>
                <td>Root Diameter (\(d_f\))</td>
                <td>\(d_f = d - 2h_f = m(z - 2.5)\)</td>
                <td>Diameter at the bottom of the tooth troughs.</td>
              </tr>
              <tr>
                <td>Base Circle Diameter (\(d_b\))</td>
                <td>\(d_b = d \cdot \cos\alpha\)</td>
                <td>Circle from which the involute profile curve is generated.</td>
              </tr>
              <tr>
                <td>Tooth Thickness (\(s\))</td>
                <td>\(s = \frac{p}{2} = \frac{\pi \cdot m}{2} \approx 1.5708 \cdot m\)</td>
                <td>Nominal circular thickness along the pitch circle.</td>
              </tr>
            </tbody>
          </table>

          <h2>Mating Gear Center Distance & Undercutting Threshold</h2>
          <p>For a pair of standard external spur gears with tooth counts \(z_1\) (pinion) and \(z_2\) (gear), the nominal center-to-center shaft distance (\(a\)) is:</p>

          <div class="formula-box">
            $$a = \frac{d_1 + d_2}{2} = \frac{m(z_1 + z_2)}{2} \quad [\text{mm}]$$
          </div>

          <p>For helical gears with helix angle \(\beta\), the transverse module is \(m_t = m_n / \cos\beta\), resulting in center distance \(a = m_n(z_1 + z_2) / (2\cos\beta)\).</p>

          <p><strong>Undercutting Limitation:</strong> When generating gear teeth with a standard hob, if the pinion has too few teeth, the hob tip cuts away and hollows out the involute base of the tooth flank. The minimum theoretical tooth count to completely avoid undercutting at a standard 20&deg; pressure angle is:</p>

          <div class="formula-box">
            $$z_{\text{min}} = \frac{2}{\sin^2\alpha} = \frac{2}{\sin^2(20^\circ)} = \frac{2}{(0.3420)^2} = 17.1 \implies z_{\text{min}} = 17\text{ teeth}$$
          </div>
          <p>Pinions with fewer than 17 teeth require <strong>positive profile shift (addendum modification \(x \cdot m\))</strong> to eliminate undercutting and prevent tooth root fatigue fracture.</p>

          <div class="worked-example-card">
            <h3>Step-by-Step Worked Case Study: Gearbox Reducer Mating Pair</h3>
            <p><strong>Design Scenario:</strong> An engineer is designing an industrial speed reducer gearbox with a 3:1 reduction ratio using module \(m = 2.5\text{ mm}\) and a 20&deg; pressure angle. The pinion has \(z_1 = 24\text{ teeth}\) and the gear has \(z_2 = 72\text{ teeth}\).</p>

            <p><strong>Step 1: Calculate pitch diameters (\(d_1\) and \(d_2\))</strong></p>
            <div class="formula-box">
              $$d_1 = m \cdot z_1 = 2.5 \times 24 = 60.0\text{ mm}$$
              $$d_2 = m \cdot z_2 = 2.5 \times 72 = 180.0\text{ mm}$$
            </div>

            <p><strong>Step 2: Determine outside tip diameters (\(d_{a1}\) and \(d_{a2}\))</strong></p>
            <div class="formula-box">
              $$d_{a1} = m(z_1 + 2) = 2.5(24 + 2) = 2.5 \times 26 = 65.0\text{ mm}$$
              $$d_{a2} = m(z_2 + 2) = 2.5(72 + 2) = 2.5 \times 74 = 185.0\text{ mm}$$
            </div>

            <p><strong>Step 3: Determine root diameters (\(d_{f1}\) and \(d_{f2}\))</strong></p>
            <div class="formula-box">
              $$d_{f1} = m(z_1 - 2.5) = 2.5(24 - 2.5) = 2.5 \times 21.5 = 53.75\text{ mm}$$
              $$d_{f2} = m(z_2 - 2.5) = 2.5(72 - 2.5) = 2.5 \times 69.5 = 173.75\text{ mm}$$
            </div>

            <p><strong>Step 4: Compute center-to-center shaft distance (\(a\))</strong></p>
            <div class="formula-box">
              $$a = \frac{d_1 + d_2}{2} = \frac{60.0 + 180.0}{2} = \frac{240.0}{2} = 120.0\text{ mm}$$
            </div>

            <p><strong>Step 5: Verify undercutting and base circle</strong></p>
            <div class="formula-box">
              $$d_{b1} = d_1 \cdot \cos(20^\circ) = 60.0 \times 0.93969 = 56.38\text{ mm}$$
            </div>
            <p>Because \(z_1 = 24 > 17\), the pinion is completely free of undercutting, ensuring maximum root bending fatigue strength.</p>
          </div>

          <h2>Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3>Why are 20-degree pressure angles standard over 14.5-degree gears?</h3>
            <p>Historical gears utilized 14.5&deg; pressure angles, which minimized radial separation forces on bearings. However, 14.5&deg; gears require a minimum of 32 teeth to prevent undercutting, making compact gearboxes impossible. The modern 20&deg; standard significantly thickens the tooth root, increasing bending load capacity by over 15% and lowering the undercutting limit to only 17 teeth.</p>
          </div>

          <div class="faq-item">
            <h3>What is the difference between normal module (mn) and transverse module (mt) in helical gears?</h3>
            <p>In helical gears with teeth angled at helix angle \(\beta\), the <em>normal module</em> (\(m_n\)) is measured in the plane perpendicular to the tooth flank and matches standard hob tooling. The <em>transverse module</em> (\(m_t = m_n / \cos\beta\)) is measured in the plane of rotation and dictates pitch diameter: \(d = m_t \cdot z = (m_n \cdot z) / \cos\beta\).</p>
          </div>

          <div class="faq-item">
            <h3>What is profile shift (addendum modification) in gear design?</h3>
            <p>Profile shift involves moving the hob cutter radially inward or outward by an amount \(x \cdot m\) during cutting. Positive profile shift (\(x > 0\)) prevents undercutting on pinions with fewer than 17 teeth, thickens the tooth root, increases tooth bending strength, and allows gear pairs to fit custom non-standard center distances.</p>
          </div>

          <div class="faq-item">
            <h3>How do I select the proper module for an application based on torque?</h3>
            <p>Gear module is selected to withstand Lewis tooth bending fatigue stress: \(\sigma_b = (2 \cdot T) / (m^3 \cdot z \cdot Y \cdot k_b) \le \sigma_{\text{allow}}\), where \(T\) is torque, \(Y\) is the Lewis form factor, and \(k_b\) is the face width ratio (\(b/m \approx 8 - 12\)). Higher torque transmissions demand larger modules to prevent tooth shear failure.</p>
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
    const gearInputModeSelect = document.getElementById('gearInputMode');
    const pressureAngleSelect = document.getElementById('pressureAngle');
    const moduleValSelect = document.getElementById('moduleVal');
    const customModuleInput = document.getElementById('customModule');
    const pitchDiamInput = document.getElementById('pitchDiam');
    const dpValInput = document.getElementById('dpVal');
    const tipDiamInput = document.getElementById('tipDiam');
    const teethPinionInput = document.getElementById('teethPinion');
    const teethGearInput = document.getElementById('teethGear');
    const helixAngleInput = document.getElementById('helixAngle');

    const grpModule = document.getElementById('grpModule');
    const grpCustomModule = document.getElementById('grpCustomModule');
    const grpPitchDiam = document.getElementById('grpPitchDiam');
    const grpDp = document.getElementById('grpDp');
    const grpTipDiam = document.getElementById('grpTipDiam');

    const gearResultBox = document.getElementById('gearResultBox');
    const resModule = document.getElementById('resModule');
    const resDp = document.getElementById('resDp');
    const resD1 = document.getElementById('resD1');
    const resD2 = document.getElementById('resD2');
    const resDa1 = document.getElementById('resDa1');
    const resDf1 = document.getElementById('resDf1');
    const resDb1 = document.getElementById('resDb1');
    const resCenterDist = document.getElementById('resCenterDist');
    const resCircPitch = document.getElementById('resCircPitch');
    const resRatioStatus = document.getElementById('resRatioStatus');
    const gearNotesBox = document.getElementById('gearNotesBox');

    gearInputModeSelect.addEventListener('change', function() {
      const mode = this.value;
      grpModule.style.display = (mode === 'fromModule') ? 'block' : 'none';
      grpCustomModule.style.display = (mode === 'fromModule' && moduleValSelect.value === 'custom') ? 'block' : 'none';
      grpPitchDiam.style.display = (mode === 'fromPitchDiam') ? 'block' : 'none';
      grpDp.style.display = (mode === 'fromDp') ? 'block' : 'none';
      grpTipDiam.style.display = (mode === 'fromTipDiam') ? 'block' : 'none';
      calculateGear();
    });

    moduleValSelect.addEventListener('change', function() {
      if (this.value === 'custom') {
        grpCustomModule.style.display = 'block';
      } else {
        grpCustomModule.style.display = 'none';
      }
      calculateGear();
    });

    function calculateGear() {
      const mode = gearInputModeSelect.value;
      const alphaDeg = parseFloat(pressureAngleSelect.value);
      const alphaRad = (alphaDeg * Math.PI) / 180;
      const betaDeg = parseFloat(helixAngleInput.value) || 0;
      const betaRad = (betaDeg * Math.PI) / 180;
      const cosBeta = Math.cos(betaRad);

      let z1 = parseInt(teethPinionInput.value, 10);
      let z2 = parseInt(teethGearInput.value, 10);
      if (isNaN(z1) || z1 < 1) z1 = 20;
      if (isNaN(z2) || z2 < 1) z2 = 60;

      let m = 2.5;

      if (mode === 'fromModule') {
        if (moduleValSelect.value === 'custom') {
          m = parseFloat(customModuleInput.value);
        } else {
          m = parseFloat(moduleValSelect.value);
        }
      } else if (mode === 'fromPitchDiam') {
        const d_input = parseFloat(pitchDiamInput.value);
        if (!isNaN(d_input) && d_input > 0) {
          m = (d_input * cosBeta) / z1;
        }
      } else if (mode === 'fromDp') {
        const dp_input = parseFloat(dpValInput.value);
        if (!isNaN(dp_input) && dp_input > 0) {
          m = 25.4 / dp_input;
        }
      } else if (mode === 'fromTipDiam') {
        const da_input = parseFloat(tipDiamInput.value);
        if (!isNaN(da_input) && da_input > 0) {
          m = da_input / ((z1 / cosBeta) + 2);
        }
      }

      if (isNaN(m) || m <= 0) m = 2.5;

      // Transverse module mt
      const mt = m / cosBeta;
      const DP = 25.4 / m;

      // Pitch diameters
      const d1 = mt * z1;
      const d2 = mt * z2;

      // Addendum, dedendum (ISO standard)
      const ha = 1.0 * m;
      const hf = 1.25 * m;

      // Tip and root diameters for pinion
      const da1 = d1 + 2 * ha;
      const df1 = d1 - 2 * hf;

      // Base circle diameter
      const db1 = d1 * Math.cos(alphaRad);

      // Center distance a
      const a = (d1 + d2) / 2;

      // Circular pitch p
      const p = Math.PI * m;

      // Gear ratio
      const ratio = z2 / z1;

      // Undercut check
      const zMin = Math.round(2 / Math.pow(Math.sin(alphaRad), 2));
      let undercutMsg = z1 < zMin ? `<span style="color:#b45309;">Warning: z1 < ${zMin} (Undercut Risk)</span>` : `<span style="color:#166534;">No Undercutting (z1 &ge; ${zMin})</span>`;

      resModule.textContent = m.toFixed(3) + " mm";
      resDp.textContent = DP.toFixed(2) + " teeth/in";
      resD1.textContent = d1.toFixed(2) + " mm";
      resD2.textContent = d2.toFixed(2) + " mm";
      resDa1.textContent = da1.toFixed(2) + " mm";
      resDf1.textContent = df1.toFixed(2) + " mm";
      resDb1.textContent = db1.toFixed(2) + " mm";
      resCenterDist.textContent = a.toFixed(2) + " mm";
      resCircPitch.textContent = p.toFixed(3) + " mm";
      resRatioStatus.innerHTML = `${ratio.toFixed(2)}:1 | ${undercutMsg}`;

      let notes = `<strong>ISO 53 Gear Meshing:</strong> Pinion (${z1}T) and Gear (${z2}T) at module <strong>m = ${m.toFixed(2)} mm</strong> have an exact center distance of <strong>${a.toFixed(2)} mm</strong>. Whole tooth depth is <strong>${(2.25 * m).toFixed(2)} mm</strong>.`;
      gearNotesBox.innerHTML = notes;

      gearResultBox.style.display = 'block';
    }

    document.getElementById('calcGearBtn').addEventListener('click', calculateGear);
    document.getElementById('resetGearBtn').addEventListener('click', function() {
      setTimeout(calculateGear, 50);
    });

    window.addEventListener('DOMContentLoaded', calculateGear);
  </script>
</body>
</html>
"""

def main():
    target_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    file5 = os.path.join(target_dir, "flywheel-energy-calculator.html")
    with open(file5, "w", encoding="utf-8") as f:
        f.write(TOOL_5_HTML)
    print(f"[PASS] flywheel-energy-calculator.html generated successfully!")

    file6 = os.path.join(target_dir, "gear-module-calculator.html")
    with open(file6, "w", encoding="utf-8") as f:
        f.write(TOOL_6_HTML)
    print(f"[PASS] gear-module-calculator.html generated successfully!")

if __name__ == "__main__":
    main()
