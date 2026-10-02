# -*- coding: utf-8 -*-
"""
Script to generate Batch 18 Part 1 tools:
1. friction-calculator.html
2. gravitational-force-calculator.html
"""
import os

TOOL_1_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Friction Calculator | Static, Kinetic & Inclined Plane Sizer</title>
  <meta name="description" content="Calculate static and kinetic friction force, coefficient of friction, inclined plane normal force, angle of repose, and slide acceleration with materials presets.">
  <link rel="canonical" href="https://calchub.cloud/friction-calculator.html">
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
        "name": "Friction Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates static friction threshold, kinetic dynamic friction force, normal force, inclined ramp angle of repose, and downhill slide acceleration based on Coulomb friction laws.",
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
            "name": "What is the primary equation for calculating frictional force?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The primary formulation for Coulomb dry friction is F_f = μ × N, where F_f is frictional resisting force in Newtons, μ is the dimensionless coefficient of friction (static μ_s or kinetic μ_k), and N is normal force pressing the two contact surfaces together in Newtons."
            }
          },
          {
            "@type": "Question",
            "name": "Why is the coefficient of static friction almost always higher than kinetic friction?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "At the microscopic level, contact surfaces touch only at microscopic peaks called asperities. While stationary, asperities undergo microscopic plastic deformation and form adhesive molecular bonds (cold welding). Once sliding motion begins, these bonds are continually sheared before they can fully establish, lowering kinetic resistance."
            }
          },
          {
            "@type": "Question",
            "name": "How is the angle of repose determined on an inclined ramp?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The critical angle of repose (the maximum incline angle before an object begins sliding downward under gravity) is determined purely by the coefficient of static friction: θ_repose = arctan(μ_s). Mass cancels out completely."
            }
          },
          {
            "@type": "Question",
            "name": "Does surface contact area affect frictional force in dry sliding?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Under classical Amontons-Coulomb dry friction laws, frictional force is independent of apparent macroscopic contact area. Increasing surface area spreads the normal force over more asperities, but reduces the pressure at each individual contact point proportionally, leaving net frictional force unchanged."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body>
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="logo">CalcHub</a>
      <nav class="nav-links">
        <a href="index.html">Home</a>
        <a href="physics.html" class="active">Physics</a>
        <a href="mechanical.html">Mechanical</a>
        <a href="engineering.html">Electrical</a>
        <a href="civil.html">Civil</a>
      </nav>
    </div>
  </header>

  <main class="page-container">
    <div class="content-wrapper">
      <div class="calculator-container">
        <h1>Friction Calculator</h1>
        <p class="lead-text">Calculate static and kinetic friction force, normal force, inclined ramp slide acceleration, and critical angle of repose with industrial material presets.</p>

        <div class="calc-card">
          <div class="form-row">
            <div class="form-group col-half">
              <label for="materialPreset">Material Contact Pair Preset</label>
              <select id="materialPreset" class="form-control">
                <option value="rubber_concrete" selected>Rubber on Dry Concrete (μ_s = 1.00, μ_k = 0.80)</option>
                <option value="steel_steel">Steel on Mild Steel Dry (μ_s = 0.74, μ_k = 0.57)</option>
                <option value="wood_wood">Wood on Clean Wood (μ_s = 0.50, μ_k = 0.30)</option>
                <option value="brake_castiron">Brake Pad on Cast Iron (μ_s = 0.40, μ_k = 0.35)</option>
                <option value="ice_steel">Ice on Steel Blade (μ_s = 0.03, μ_k = 0.015)</option>
                <option value="teflon_steel">PTFE (Teflon) on Steel (μ_s = 0.04, μ_k = 0.04)</option>
                <option value="custom">Custom Friction Coefficients</option>
              </select>
            </div>

            <div class="form-group col-half">
              <label for="calcSurface">Surface Geometry Configuration</label>
              <select id="calcSurface" class="form-control">
                <option value="flat" selected>Horizontal Flat Surface (Incline θ = 0°)</option>
                <option value="incline">Inclined Ramp Plane (Variable Incline Angle)</option>
              </select>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group col-third">
              <label for="massVal">Object Mass (m)</label>
              <div class="input-with-unit">
                <input type="number" id="massVal" class="form-control" value="500" step="any" min="0.001">
                <select id="massUnit" class="unit-select">
                  <option value="kg" selected>kg</option>
                  <option value="lbs">lbs</option>
                  <option value="ton">Metric Tons</option>
                </select>
              </div>
            </div>

            <div class="form-group col-third">
              <label for="muS">Static Coefficient (&mu;_s)</label>
              <input type="number" id="muS" class="form-control" value="1.00" step="0.01" min="0">
            </div>

            <div class="form-group col-third">
              <label for="muK">Kinetic Coefficient (&mu;_k)</label>
              <input type="number" id="muK" class="form-control" value="0.80" step="0.01" min="0">
            </div>
          </div>

          <div class="form-row" id="inclineRow" style="display:none;">
            <div class="form-group col-full">
              <label for="inclineAngle">Ramp Incline Angle (&theta;) in Degrees</label>
              <div class="input-with-unit">
                <input type="number" id="inclineAngle" class="form-control" value="15" step="0.5" min="0" max="89.9">
                <span style="font-size:12px; padding:6px 12px; background:#fff; border:1px solid #cbd5e1; border-left:none; border-radius:0 4px 4px 0; display:flex; align-items:center;">Degrees (°)</span>
              </div>
            </div>
          </div>

          <div class="btn-group">
            <button type="button" id="calcBtn" class="btn btn-primary">Calculate Frictional Forces</button>
            <button type="button" id="resetBtn" class="btn btn-secondary">Reset to Rubber/Concrete</button>
          </div>

          <div id="resultsPanel" class="results-panel">
            <div class="result-box primary-result">
              <div class="result-label" id="resFricLabel">Kinetic Dynamic Friction Force (F_k)</div>
              <div class="result-value" id="resFricVal">3,922.7 N</div>
              <div class="result-sub" id="resFricSub">Breakaway Static Threshold: 4,903.3 N (1,102.3 lbf)</div>
            </div>

            <div class="result-grid">
              <div class="result-item">
                <span class="sub-label">Normal Force (N)</span>
                <span class="sub-value" id="resNormal">4,903.3 N (500.0 kgf)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Angle of Repose (&theta;_c)</span>
                <span class="sub-value" id="resRepose">45.00&deg; (100.0% grade)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Parallel Gravity Component (F_&parallel;)</span>
                <span class="sub-value" id="resParallel">0.0 N (Flat Surface)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Net Sliding Acceleration (a)</span>
                <span class="sub-value" id="resAcc">0.00 m/s² (Stationary)</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. Physical Foundations of Coulomb Dry Friction</h2>
          <p>Friction is the resistive contact force that opposes the relative tangential motion or impending motion between two solid surfaces in physical contact. In engineering mechanics and tribology, classical dry friction is described by the <strong>Amontons-Coulomb laws of friction</strong>, first systematically formulated by French physicist Charles-Augustin de Coulomb in 1785 based on earlier observations by Leonardo da Vinci and Guillaume Amontons.</p>
          <p>Coulomb's experimental investigations established three foundational empirical laws for dry, unlubricated contact:</p>
          <ul>
            <li><strong>First Law (Proportionality):</strong> The frictional force is directly proportional to the compressive normal force pressing the two contact surfaces together.</li>
            <li><strong>Second Law (Area Independence):</strong> The frictional force is independent of the apparent macroscopic surface contact area.</li>
            <li><strong>Third Law (Velocity Independence):</strong> Once sliding occurs, the kinetic frictional force is largely independent of the sliding velocity over moderate speed regimes.</li>
          </ul>
          <p>At the microscopic atomic scale, solid surfaces are never perfectly smooth; even optically polished steel displays jagged microscopic peaks and valleys known as <strong>asperities</strong>. When two bodies touch, true physical contact occurs only at the microscopic summits of these asperities, covering a tiny fraction (often \(< 1\%\)) of the apparent macroscopic geometric area. Under the intense local contact pressures generated at these contact points, microscopic asperities deform plastically and form adhesive molecular bonds (cold welding). Sliding requires shearing these microscopic junctions and mechanically plowing asperities through one another.</p>

          <h2>2. Mathematical Formulations: Static vs. Kinetic Friction</h2>
          <p>Tribology distinguishes sharply between two operational regimes of friction:</p>
          <div class="math-block">
            $$\text{Static Friction: } F_s \le F_{s,\max} = \mu_s N$$
          </div>
          <div class="math-block">
            $$\text{Kinetic Friction: } F_k = \mu_k N$$
          </div>
          <p>Where \(\mu_s\) is the dimensionless <strong>coefficient of static friction</strong>, \(\mu_k\) is the <strong>coefficient of kinetic (dynamic) friction</strong>, and \(N\) is the perpendicular compressive <strong>normal force</strong> in Newtons (\(\text{N}\)).</p>
          <p>Static friction is an adaptable, self-adjusting reaction force: if you push against a heavy steel machine with \(50\text{ N}\) of lateral force and it does not move, the static friction force is exactly \(50\text{ N}\) (not \(\mu_s N\)). It increases linearly with applied lateral force until reaching the critical breakaway threshold \(F_{s,\max} = \mu_s N\). Beyond this point, the adhesive asperity bonds shear, the body accelerates into motion, and resistive force immediately drops to the lower steady-state kinetic friction force \(F_k = \mu_k N\).</p>

          <h2>3. Inclined Plane Mechanics and the Critical Angle of Repose</h2>
          <p>When an object of mass \(m\) rests upon an inclined plane inclined at an angle \(\theta\) above the horizontal, Earth's downward gravitational force vector (\(\vec{F}_g = mg\)) resolves into two orthogonal vector components:</p>
          <ul>
            <li><strong>Normal Component (Perpendicular to Ramp):</strong> \(N = mg \cos\theta\)</li>
            <li><strong>Parallel Component (Downhill Sliding Force):</strong> \(F_\parallel = mg \sin\theta\)</li>
          </ul>
          <p>The maximum static resistive force opposing downhill sliding is:</p>
          <div class="math-block">
            $$F_{s,\max} = \mu_s N = \mu_s mg \cos\theta$$
          </div>
          <p>For the mass to remain stationary in static equilibrium without sliding downhill, the downhill component must not exceed maximum static friction (\(mg \sin\theta \le \mu_s mg \cos\theta\)). Dividing both sides by \(mg \cos\theta\) yields the classic civil and geotechnical relation for the <strong>angle of repose</strong> (\(\theta_c\)):</p>
          <div class="math-block">
            $$\tan\theta_c = \mu_s \implies \theta_c = \arctan(\mu_s)$$
          </div>
          <p>If the incline angle exceeds the angle of repose (\(\theta > \theta_c\)), the object accelerates downhill with net acceleration \(a\) governed by kinetic friction:</p>
          <div class="math-block">
            $$m a = mg \sin\theta - \mu_k mg \cos\theta \implies a = g(\sin\theta - \mu_k \cos\theta)$$
          </div>

          <h2>4. Engineering Friction Coefficient Benchmark Reference Table</h2>
          <p>To assist mechanical rotating machinery designers, brake system engineers, and geotechnical analysts, the table below documents representative static and kinetic friction coefficients across common material pairings:</p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Contact Interface Materials</th>
                <th>Static Coeff (\(\mu_s\))</th>
                <th>Kinetic Coeff (\(\mu_k\))</th>
                <th>Standard Operational Application</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Rubber Tire on Dry Asphalt / Concrete</td>
                <td>0.90 – 1.10</td>
                <td>0.70 – 0.85</td>
                <td>Dry highway passenger vehicle braking performance</td>
              </tr>
              <tr>
                <td>Rubber Tire on Wet Asphalt Pavement</td>
                <td>0.50 – 0.70</td>
                <td>0.40 – 0.50</td>
                <td>Wet weather stopping distance and hydroplaning safety</td>
              </tr>
              <tr>
                <td>Rubber Tire on Solid Packed Snow / Ice</td>
                <td>0.15 – 0.25</td>
                <td>0.10 – 0.15</td>
                <td>Winter traction, ABS engagement, and studded tire threshold</td>
              </tr>
              <tr>
                <td>Mild Steel on Mild Steel (Clean & Dry)</td>
                <td>0.74 – 0.80</td>
                <td>0.57 – 0.60</td>
                <td>Dry structural steel bolted friction connections</td>
              </tr>
              <tr>
                <td>Mild Steel on Mild Steel (Engine Oil Lubricated)</td>
                <td>0.10 – 0.15</td>
                <td>0.05 – 0.08</td>
                <td>Internal combustion engine crank and camshaft journals</td>
              </tr>
              <tr>
                <td>Semi-Metallic Brake Pad on Cast Iron Rotor</td>
                <td>0.38 – 0.45</td>
                <td>0.32 – 0.38</td>
                <td>Automotive disc brake caliper stopping friction</td>
              </tr>
              <tr>
                <td>PTFE (Teflon) on Polished Stainless Steel</td>
                <td>0.04 – 0.05</td>
                <td>0.04 – 0.04</td>
                <td>Bridge expansion sliding bearings and non-stick guides</td>
              </tr>
              <tr>
                <td>Ice on Polished Steel Runner (Curling / Skating)</td>
                <td>0.02 – 0.03</td>
                <td>0.01 – 0.015</td>
                <td>Speed skating blades and winter sport sled runners</td>
              </tr>
            </tbody>
          </table>

          <h2>5. Worked Engineering Case Study: Industrial Winch Sizing for Equipment Ramp</h2>
          <div class="worked-example-card">
            <h3>Problem Statement</h3>
            <p>An industrial manufacturing facility needs to haul a crated electrical transformer with total mass \(m = 2,500\text{ kg}\) up an outdoor concrete loading ramp. The ramp is inclined at an angle of \(\theta = 20^\circ\) above the horizontal. The wooden shipping skid contacts dry concrete pavement, with measured friction coefficients of \(\mu_s = 0.55\) (static) and \(\mu_k = 0.40\) (kinetic). Earth's gravitational acceleration is \(g = 9.80665\text{ m/s}^2\).</p>
            <p><strong>Required:</strong></p>
            <ol>
              <li>Compute the normal force \(N\) pressing the skid against the ramp surface.</li>
              <li>Determine the peak breakaway pull force \(T_{\text{static}}\) that the haulage cable must exert to initiate upward motion from a dead standstill.</li>
              <li>Determine the steady-state cable tension \(T_{\text{kinetic}}\) required to sustain upward movement at constant speed.</li>
            </ol>

            <h3>Step-by-Step Mathematical Solution</h3>
            <p><strong>Step 1: Calculate normal force \(N\):</strong></p>
            <div class="math-block">
              $$N = mg \cos\theta = 2,500\text{ kg} \times 9.80665\text{ m/s}^2 \times \cos(20^\circ)$$
            </div>
            <div class="math-block">
              $$N = 24,516.63\text{ N} \times 0.93969 \approx 23,038.1\text{ N (23.04 kN)}$$
            </div>

            <p><strong>Step 2: Calculate the downhill gravitational parallel force component \(F_\parallel\):</strong></p>
            <div class="math-block">
              $$F_\parallel = mg \sin\theta = 24,516.63\text{ N} \times \sin(20^\circ) = 24,516.63 \times 0.34202 \approx 8,385.2\text{ N (8.39 kN)}$$
            </div>

            <p><strong>Step 3: Calculate peak breakaway static cable tension \(T_{\text{static}}\):</strong></p>
            <p>To initiate upward motion, the winch cable tension must overcome both the downhill gravitational pull and the maximum opposing static friction force directed downhill:</p>
            <div class="math-block">
              $$F_{s,\max} = \mu_s N = 0.55 \times 23,038.1\text{ N} \approx 12,671.0\text{ N}$$
            </div>
            <div class="math-block">
              $$T_{\text{static}} = F_\parallel + F_{s,\max} = 8,385.2\text{ N} + 12,671.0\text{ N} = 21,056.2\text{ N (21.06 kN)}$$
            </div>
            <p>Converting to gravitational force units: \(21,056.2\text{ N} \div 4.44822 \approx 4,733.6\text{ lbf}\).</p>

            <p><strong>Step 4: Calculate steady-state kinetic cable tension \(T_{\text{kinetic}}\):</strong></p>
            <div class="math-block">
              $$F_k = \mu_k N = 0.40 \times 23,038.1\text{ N} \approx 9,215.2\text{ N}$$
            </div>
            <div class="math-block">
              $$T_{\text{kinetic}} = F_\parallel + F_k = 8,385.2\text{ N} + 9,215.2\text{ N} = 17,600.4\text{ N (17.60 kN or 3,956.7 lbf)}$$
            </div>
            <p><strong>Engineering Sizing Conclusion:</strong> The electric winch motor must be selected with a starting pull rating of at least \(21.1\text{ kN}\) (\(4,750\text{ lbf}\)) to overcome the static breakaway barrier, after which cruising power will demand \(17.6\text{ kN}\). Incorporating standard ASME B30 hoisting safety factor (\(SF \ge 3.0\)), the steel wire rope must possess a certified breaking strength of at least \(63.2\text{ kN}\) (\(14,200\text{ lbf}\)).</p>
          </div>

          <h2>5. Advanced Tribology: Stick-Slip Vibrations and Brake Fade</h2>
          <p>In mechanical powertrain engineering, friction behavior departs from idealized textbook constants under high loads and temperatures:</p>
          <ul>
            <li><strong>Stick-Slip Vibration Phenomenon:</strong> Because \(\mu_s > \mu_k\), mechanical systems driven by flexible elastic components (such as machine tool slides, squealing brake pads, or tectonic earthquake fault lines) alternate between static sticking and kinetic slipping. When the elastic drive force builds up to \(F_{s,\max}\), the junction breaks away and accelerates forward until relative speed drops, causing re-sticking in an audible high-frequency oscillation known as chatter.</li>
            <li><strong>Thermal Brake Fade:</strong> Under repeated severe decelerations, friction converts kinetic energy into intense heat. When brake pad temperatures exceed \(450^\circ\text{C}\), organic binder resins volatilize into an outgassing boundary film that acts as an unintended lubricant, causing \(\mu_k\) to collapse dramatically—a dangerous condition known as <strong>brake fade</strong>.</li>
          </ul>

          <h2>6. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-item">
            <h3>Can the coefficient of friction ever be greater than 1.0?</h3>
            <p>Yes. A common misconception is that \(\mu\) must range strictly between 0 and 1. High-grip racing tires on clean dry asphalt can exhibit friction coefficients of \(\mu = 1.3\text{ to } 1.7\) due to microscopic mechanical interlock (tread rubber conforming into pavement pore cavities) and chemical polymer adhesion.</p>
          </div>
          <div class="faq-item">
            <h3>Why do wide racing tires provide more grip if friction is independent of area?</h3>
            <p>Coulomb's law of area independence applies strictly to hard, unyielding solids like metals. Soft viscoelastic polymers like tire rubber exhibit non-linear pressure dependence: spreading normal load over a wider contact patch reduces local rubber pressure, allowing the compound to operate in its peak adhesive shear regime while improving thermal heat dissipation.</p>
          </div>
          <div class="faq-item">
            <h3>How do Anti-Lock Braking Systems (ABS) leverage friction principles?</h3>
            <p>Because static friction exceeds kinetic friction (\(\mu_s > \mu_k\)), a rolling tire maintaining traction with the road provides significantly higher braking force than a skidding locked tire sliding on rubber-melt smoke. ABS rapidly modulates brake hydraulic pressure (15–20 times per second) to keep tires operating at the peak of the static traction curve rather than sliding in the kinetic regime.</p>
          </div>
          <div class="faq-item">
            <h3>What is rolling resistance, and how does it differ from sliding friction?</h3>
            <p>Rolling resistance is the energy dissipation caused primarily by inelastic hysteresis deformation of the rolling wheel and roadway surface (such as a tire flattening against pavement). Its coefficient (\(C_{rr} \approx 0.005\text{ to } 0.015\)) is typically 50 to 100 times smaller than sliding kinetic friction.</p>
          </div>
        </article>
      </div>

      <aside class="sidebar" id="toolSidebar">
        <!-- Injected via apply_sidebars_all.py -->
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <p>&copy; 2026 CalcHub. All rights reserved. Precision engineering, science, and technical calculation tools.</p>
    </div>
  </footer>

  <script>
    // Friction Presets Data
    const presets = {
      rubber_concrete: { s: 1.00, k: 0.80 },
      steel_steel: { s: 0.74, k: 0.57 },
      wood_wood: { s: 0.50, k: 0.30 },
      brake_castiron: { s: 0.40, k: 0.35 },
      ice_steel: { s: 0.03, k: 0.015 },
      teflon_steel: { s: 0.04, k: 0.04 }
    };

    const toKg = (m, unit) => {
      switch(unit) {
        case 'lbs': return m * 0.45359237;
        case 'ton': return m * 1000;
        default: return m;
      }
    };

    function applyPreset() {
      const p = document.getElementById('materialPreset').value;
      if (p !== 'custom' && presets[p]) {
        document.getElementById('muS').value = presets[p].s;
        document.getElementById('muK').value = presets[p].k;
      }
      calculate();
    }

    function toggleSurface() {
      const s = document.getElementById('calcSurface').value;
      document.getElementById('inclineRow').style.display = s === 'incline' ? 'flex' : 'none';
      calculate();
    }

    function calculate() {
      const rawMass = parseFloat(document.getElementById('massVal').value) || 0;
      const massUnit = document.getElementById('massUnit').value;
      const m = toKg(rawMass, massUnit);

      const mu_s = parseFloat(document.getElementById('muS').value) || 0;
      const mu_k = parseFloat(document.getElementById('muK').value) || 0;

      const surface = document.getElementById('calcSurface').value;
      let angleDeg = 0;
      if (surface === 'incline') {
        angleDeg = parseFloat(document.getElementById('inclineAngle').value) || 0;
      }

      const g = 9.80665;
      const angleRad = angleDeg * (Math.PI / 180);

      // Normal force N = m * g * cos(theta)
      const N = m * g * Math.cos(angleRad);
      // Downhill parallel gravity force F_parallel = m * g * sin(theta)
      const F_parallel = m * g * Math.sin(angleRad);

      // Frictions
      const F_s_max = mu_s * N;
      const F_k = mu_k * N;

      // Angle of repose theta_c = atan(mu_s)
      const theta_c_rad = Math.atan(mu_s);
      const theta_c_deg = theta_c_rad * (180 / Math.PI);
      const slopePct = Math.tan(theta_c_rad) * 100;

      // Downhill acceleration if incline
      let acc = 0;
      let isSliding = false;
      if (surface === 'incline') {
        if (F_parallel > F_s_max && m > 0) {
          isSliding = true;
          acc = (F_parallel - F_k) / m;
          if (acc < 0) acc = 0;
        }
      }

      // Render Primary Box
      document.getElementById('resFricLabel').textContent = "Kinetic Dynamic Friction Force (F_k)";
      document.getElementById('resFricVal').textContent = F_k.toFixed(1) + " N (" + (F_k / 4.44822).toFixed(1) + " lbf)";
      document.getElementById('resFricSub').textContent = 
        "Breakaway Static Threshold: " + F_s_max.toFixed(1) + " N (" + (F_s_max / 4.44822).toFixed(1) + " lbf)";

      // Render Grid Items
      document.getElementById('resNormal').textContent = 
        N.toFixed(1) + " N (" + (N / g).toFixed(1) + " kgf | " + (N / 4.44822).toFixed(1) + " lbf)";

      document.getElementById('resRepose').textContent = 
        theta_c_deg.toFixed(2) + "° (slope " + slopePct.toFixed(1) + "%)";

      if (surface === 'incline') {
        document.getElementById('resParallel').textContent = 
          F_parallel.toFixed(1) + " N (" + (F_parallel / 4.44822).toFixed(1) + " lbf)";
        if (isSliding) {
          document.getElementById('resAcc').textContent = acc.toFixed(2) + " m/s² (Sliding Downhill)";
        } else {
          document.getElementById('resAcc').textContent = "0.00 m/s² (Held by Static Friction)";
        }
      } else {
        document.getElementById('resParallel').textContent = "0.0 N (Horizontal Surface)";
        document.getElementById('resAcc').textContent = "0.00 m/s² (Stationary)";
      }
    }

    document.getElementById('materialPreset').addEventListener('change', applyPreset);
    document.getElementById('calcSurface').addEventListener('change', toggleSurface);
    document.querySelectorAll('input, select').forEach(el => {
      if (el.id !== 'materialPreset' && el.id !== 'calcSurface') {
        el.addEventListener('input', () => {
          if (el.id === 'muS' || el.id === 'muK') {
            document.getElementById('materialPreset').value = 'custom';
          }
          calculate();
        });
        el.addEventListener('change', () => {
          if (el.id === 'muS' || el.id === 'muK') {
            document.getElementById('materialPreset').value = 'custom';
          }
          calculate();
        });
      }
    });

    document.getElementById('calcBtn').addEventListener('click', calculate);
    document.getElementById('resetBtn').addEventListener('click', () => {
      document.getElementById('materialPreset').value = 'rubber_concrete';
      document.getElementById('calcSurface').value = 'flat';
      document.getElementById('massVal').value = '500';
      document.getElementById('massUnit').value = 'kg';
      document.getElementById('inclineAngle').value = '15';
      applyPreset();
      toggleSurface();
    });

    window.addEventListener('DOMContentLoaded', calculate);
  </script>
</body>
</html>
"""

TOOL_2_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gravitational Force Calculator | Newton's Universal Law of Gravity</title>
  <meta name="description" content="Calculate gravitational attraction force between two masses, mutual gravitational accelerations, and potential energy using Newton's inverse-square law.">
  <link rel="canonical" href="https://calchub.cloud/gravitational-force-calculator.html">
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
        "name": "Gravitational Force Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates mutual Newtonian gravitational attractive force, relative gravitational accelerations, and gravitational potential energy across planets and masses.",
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
            "name": "What is Newton's Law of Universal Gravitation formula?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The law of universal gravitation states that every point mass attracts every other point mass with a force directly proportional to the product of their masses and inversely proportional to the square of the distance between their centers: F = G × (m₁ × m₂) / r², where G is Newton's constant (6.67430 × 10⁻¹¹ m³/(kg·s²))."
            }
          },
          {
            "@type": "Question",
            "name": "Why is the gravitational force between everyday objects imperceptible?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The universal gravitational constant G is exceedingly small (~6.674 × 10⁻¹¹). For two 70 kg people standing 1 meter apart, the gravitational force between them is only 3.27 × 10⁻⁷ Newtons (equivalent to the weight of a microscopic speck of dust), which is completely masked by contact friction."
            }
          },
          {
            "@type": "Question",
            "name": "What is the physical meaning of the negative sign in gravitational potential energy?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Gravitational potential energy is formulated as U = -G × (m₁ × m₂) / r. The negative sign signifies a bound attractive system. By universal convention, potential energy is defined as zero at infinite separation (r → ∞). Because attractive gravity does positive work as masses come closer together, potential energy becomes increasingly negative."
            }
          },
          {
            "@type": "Question",
            "name": "Does Earth exert a greater force on you than you exert on Earth?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "No. According to Newton's Third Law of Motion, the gravitational force you exert on Earth is identical in magnitude and opposite in direction to the force Earth exerts on you. However, because Earth's mass is ~5.972 × 10²⁴ kg, your mutual force accelerates Earth by an unmeasurably tiny fraction of a millimeter per century."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body>
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="logo">CalcHub</a>
      <nav class="nav-links">
        <a href="index.html">Home</a>
        <a href="physics.html" class="active">Physics</a>
        <a href="mechanical.html">Mechanical</a>
        <a href="engineering.html">Electrical</a>
        <a href="civil.html">Civil</a>
      </nav>
    </div>
  </header>

  <main class="page-container">
    <div class="content-wrapper">
      <div class="calculator-container">
        <h1>Gravitational Force Calculator</h1>
        <p class="lead-text">Calculate mutual gravitational attraction, individual accelerations, and gravitational potential energy between planets, moons, satellites, and physical bodies.</p>

        <div class="calc-card">
          <div class="form-group">
            <label for="gravPreset">Astrophysical Preset Scenario</label>
            <select id="gravPreset" class="form-control">
              <option value="earth_moon" selected>Earth & Moon (r = 384,400 km)</option>
              <option value="earth_sun">Earth & Sun (r = 1.0 AU / 149.6M km)</option>
              <option value="earth_iss">Earth & International Space Station (420 km alt)</option>
              <option value="earth_person">Earth & 70 kg Person at Sea Level</option>
              <option value="moon_person">Moon & 70 kg Person on Lunar Surface</option>
              <option value="two_humans">Two 75 kg Humans (Separation r = 1.0 m)</option>
              <option value="custom">Custom Masses and Distance</option>
            </select>
          </div>

          <div class="form-row">
            <div class="form-group col-half">
              <label for="valM1">Primary Body Mass (m₁)</label>
              <div class="input-with-unit">
                <input type="number" id="valM1" class="form-control" value="5.9722e24" step="any" min="0">
                <select id="unitM1" class="unit-select">
                  <option value="kg" selected>kg</option>
                  <option value="earth">Earth Masses</option>
                  <option value="solar">Solar Masses</option>
                </select>
              </div>
            </div>

            <div class="form-group col-half">
              <label for="valM2">Secondary Body Mass (m₂)</label>
              <div class="input-with-unit">
                <input type="number" id="valM2" class="form-control" value="7.342e22" step="any" min="0">
                <select id="unitM2" class="unit-select">
                  <option value="kg" selected>kg</option>
                  <option value="earth">Earth Masses</option>
                  <option value="lbs">lbs</option>
                </select>
              </div>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group col-full">
              <label for="valDist">Center-to-Center Distance (r)</label>
              <div class="input-with-unit">
                <input type="number" id="valDist" class="form-control" value="384400" step="any" min="0.0001">
                <select id="unitDist" class="unit-select">
                  <option value="km" selected>Kilometers (km)</option>
                  <option value="m">Meters (m)</option>
                  <option value="au">Astronomical Units (AU)</option>
                  <option value="mi">Miles</option>
                </select>
              </div>
            </div>
          </div>

          <div class="btn-group">
            <button type="button" id="calcBtn" class="btn btn-primary">Calculate Gravitational Dynamics</button>
            <button type="button" id="resetBtn" class="btn btn-secondary">Reset to Earth & Moon</button>
          </div>

          <div id="resultsPanel" class="results-panel">
            <div class="result-box primary-result">
              <div class="result-label">Mutual Gravitational Force (F_g)</div>
              <div class="result-value" id="resForce">1.982 × 10²⁰ N</div>
              <div class="result-sub" id="resForceSub">198.2 Quintillion Newtons • 4.456 × 10¹⁹ lbf</div>
            </div>

            <div class="result-grid">
              <div class="result-item">
                <span class="sub-label">Acceleration on Body 1 (a₁)</span>
                <span class="sub-value" id="resAcc1">3.319 × 10⁻⁵ m/s²</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Acceleration on Body 2 (a₂)</span>
                <span class="sub-value" id="resAcc2">2.699 × 10⁻³ m/s² (Moon orbital a_c)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Gravitational Potential Energy (U)</span>
                <span class="sub-value" id="resPotEnergy">-7.619 × 10²⁸ Joules</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Radial Center Distance</span>
                <span class="sub-value" id="resDistFormat">384,400 km (238,855 miles)</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. Classical Newtonian Gravitation & The Inverse-Square Law</h2>
          <p>In 1687, Sir Isaac Newton published his landmark masterpiece <em>Philosophiae Naturalis Principia Mathematica</em>, unifying celestial motions and terrestrial falling bodies under a single universal mathematical law. Newton posited that every particle of matter in the universe exerts an attractive gravitational force on every other particle, directed along the line joining their centers of mass.</p>
          <p>Newton's <strong>Law of Universal Gravitation</strong> states that the mutual gravitational attraction force \(F\) between two point masses \(m_1\) and \(m_2\) separated by a spatial distance \(r\) is formulated as:</p>
          <div class="math-block">
            $$F = G \frac{m_1 m_2}{r^2}$$
          </div>
          <p>Where:</p>
          <ul>
            <li>\(F\) = Mutual gravitational attractive force (\(\text{Newtons, N}\))</li>
            <li>\(G\) = Universal Newtonian gravitational constant (\(6.67430 \times 10^{-11}\text{ m}^3\text{kg}^{-1}\text{s}^{-2}\))</li>
            <li>\(m_1, m_2\) = Masses of the two interacting bodies (\(\text{kilograms, kg}\))</li>
            <li>\(r\) = Radial separation between their respective centers of mass (\(\text{meters, m}\))</li>
          </ul>
          <p>The inverse-square dependence (\(\propto 1/r^2\)) is a fundamental geometric property of three-dimensional Euclidean space: gravitational flux spreads out over the surface area of an expanding imaginary sphere (\(A = 4\pi r^2\)). Consequently, doubling the radial separation between two planets reduces their gravitational pull to exactly one-quarter (\(1/4\)), while tripling distance weakens the attraction by a factor of nine (\(1/9\)).</p>

          <h2>2. Newton's Shell Theorem and Terrestrial Surface Gravity</h2>
          <p>A crucial mathematical challenge Newton overcame was proving whether a vast spherical planet like Earth could be treated as a single concentrated point mass located at its geometric core. Through integral calculus, Newton developed the <strong>Spherical Shell Theorem</strong>:</p>
          <ul>
            <li><strong>External Points:</strong> A spherically symmetric body of mass \(M\) attracts an external object outside its radius as if its entire mass were concentrated at its exact center.</li>
            <li><strong>Internal Points:</strong> Inside a uniform hollow spherical shell, the net gravitational force exerted on any interior particle is identically zero everywhere, regardless of the particle's internal position.</li>
          </ul>
          <p>Consequently, for an object of mass \(m\) resting on the surface of Earth (radius \(R_E \approx 6,371\text{ km}\) and mass \(M_E \approx 5.972 \times 10^{24}\text{ kg}\)), the gravitational force simplifies directly to its familiar weight equation:</p>
          <div class="math-block">
            $$F = G \frac{M_E \cdot m}{R_E^2} = m \left(\frac{G M_E}{R_E^2}\right) = m \cdot g_0$$
          </div>
          <p>Evaluating this quotient yields standard terrestrial sea-level surface gravity:</p>
          <div class="math-block">
            $$g_0 = \frac{6.67430 \times 10^{-11} \times 5.9722 \times 10^{24}}{(6.371 \times 10^6)^2} \approx 9.818\text{ m/s}^2$$
          </div>

          <h2>3. Astrophysical Benchmark Reference Table</h2>
          <p>To provide concrete physical perspective across disparate cosmic regimes, the table below compiles mutual gravitational forces and resultant orbital accelerations across notable Solar System systems:</p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Interacting Gravitational System</th>
                <th>Mass 1 & Mass 2</th>
                <th>Mean Separation (\(r\))</th>
                <th>Mutual Gravitational Force (\(F_g\))</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Sun and Planet Earth</td>
                <td>\(1.989 \times 10^{30}\text{ kg}\) & \(5.972 \times 10^{24}\text{ kg}\)</td>
                <td>149.6M km (1.0 AU)</td>
                <td>\(3.542 \times 10^{22}\text{ N}\) (Orbital centripetal force)</td>
              </tr>
              <tr>
                <td>Earth and Moon</td>
                <td>\(5.972 \times 10^{24}\text{ kg}\) & \(7.342 \times 10^{22}\text{ kg}\)</td>
                <td>384,400 km</td>
                <td>\(1.982 \times 10^{20}\text{ N}\) (Ocean tidal drivers)</td>
              </tr>
              <tr>
                <td>Jupiter and Moon Io</td>
                <td>\(1.898 \times 10^{27}\text{ kg}\) & \(8.932 \times 10^{22}\text{ kg}\)</td>
                <td>421,700 km</td>
                <td>\(6.353 \times 10^{22}\text{ N}\) (Extreme volcanic tidal heating)</td>
              </tr>
              <tr>
                <td>Earth and Space Station (ISS, 420 tonnes)</td>
                <td>\(5.972 \times 10^{24}\text{ kg}\) & \(4.20 \times 10^5\text{ kg}\)</td>
                <td>6,791 km (Orbit center)</td>
                <td>\(3.633 \times 10^6\text{ N}\) (3.63 MN in free fall)</td>
              </tr>
              <tr>
                <td>Earth and 80 kg Adult Human</td>
                <td>\(5.972 \times 10^{24}\text{ kg}\) & 80.0 kg</td>
                <td>6,371 km (Surface)</td>
                <td>784.5 N (176.4 lbf / weight)</td>
              </tr>
              <tr>
                <td>Two 75 kg People (1 Meter Apart)</td>
                <td>75.0 kg & 75.0 kg</td>
                <td>1.0 m</td>
                <td>\(3.754 \times 10^{-7}\text{ N}\) (0.038 milligrams force)</td>
              </tr>
            </tbody>
          </table>

          <h2>4. Worked Engineering Case Study: Satellite Orbital Speed from Gravitational Force</h2>
          <div class="worked-example-card">
            <h3>Problem Statement</h3>
            <p>A weather observation satellite with mass \(m = 1,200\text{ kg}\) is deployed into a circular orbit at an altitude of \(h = 800\text{ km}\) above Earth's surface (\(R_E = 6,371\text{ km}\), \(M_E = 5.9722 \times 10^{24}\text{ kg}\)).</p>
            <p><strong>Required:</strong></p>
            <ol>
              <li>Compute the total radial orbital distance \(r\) from Earth's core.</li>
              <li>Determine the exact gravitational attractive force \(F_g\) acting on the satellite.</li>
              <li>Equate gravitational force to centripetal force (\(F_g = m v^2 / r\)) to determine the required circular orbital cruising speed \(v\) and orbital period \(T\).</li>
            </ol>

            <h3>Step-by-Step Mathematical Solution</h3>
            <p><strong>Step 1: Calculate total radial orbital distance \(r\):</strong></p>
            <div class="math-block">
              $$r = R_E + h = 6,371\text{ km} + 800\text{ km} = 7,171\text{ km} = 7.171 \times 10^6\text{ m}$$
            </div>

            <p><strong>Step 2: Calculate gravitational attractive force \(F_g\):</strong></p>
            <div class="math-block">
              $$F_g = G \frac{M_E \cdot m}{r^2} = (6.67430 \times 10^{-11}) \times \frac{(5.9722 \times 10^{24}) \times 1,200}{(7.171 \times 10^6)^2}$$
            </div>
            <div class="math-block">
              $$F_g = \frac{4.7834 \times 10^{17}}{5.1423 \times 10^{13}} \approx 9,302.1\text{ N (9.30 kN)}$$
            </div>
            <p>Notice that at 800 km altitude, the satellite still experiences \(\approx 79\%\) of its sea-level weight (\(1,200 \times 9.81 = 11,772\text{ N}\)).</p>

            <p><strong>Step 3: Solve for orbital circular velocity \(v\):</strong></p>
            <p>Because gravity provides the entire centripetal force holding the satellite in circular orbit:</p>
            <div class="math-block">
              $$F_g = \frac{m v^2}{r} \implies v = \sqrt{\frac{F_g \cdot r}{m}} = \sqrt{\frac{G M_E}{r}}$$
            </div>
            <div class="math-block">
              $$v = \sqrt{\frac{3.9860 \times 10^{14}}{7.171 \times 10^6}} = \sqrt{5.5585 \times 10^7} \approx 7,455.5\text{ m/s (7.456 km/s)}$$
            </div>
            <p>Converting to kilometers per hour: \(7,455.5 \times 3.6 = 26,840\text{ km/h}\) (approx \(16,678\text{ mph}\)).</p>

            <p><strong>Step 4: Compute orbital revolution period \(T\):</strong></p>
            <div class="math-block">
              $$T = \frac{2\pi r}{v} = \frac{2\pi \times 7.171 \times 10^6\text{ m}}{7,455.5\text{ m/s}} \approx \frac{45,056,633}{7,455.5} \approx 6,043.4\text{ seconds}$$
            </div>
            <p>Converting to minutes: \(6,043.4 \div 60 \approx 100.72\text{ minutes (1.68 hours)}\). The satellite completes approximately 14.3 orbits around Earth every 24 hours.</p>
          </div>

          <h2>5. Gravitational Potential Energy in Classical Mechanics</h2>
          <p>Unlike localized terrestrial potential energy (\(U = mgh\)), which presumes constant gravity over tiny heights, universal gravitation requires integrating Newton's force law from infinity inward:</p>
          <div class="math-block">
            $$U(r) = -\int_{\infty}^r F(r')\,dr' = -G \frac{m_1 m_2}{r}$$
          </div>
          <p>By international scientific convention, gravitational potential energy is chosen to be zero at infinite separation (\(r \to \infty\)). Because gravity is an attractive interaction that performs positive work drawing masses together, moving from infinity toward a planet decreases potential energy, rendering \(U(r)\) consistently negative. To escape the planet's gravitational well, the spacecraft must inject enough kinetic energy to drive total energy \(E = K + U \ge 0\).</p>

          <h2>6. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-item">
            <h3>How was the universal gravitational constant G first measured?</h3>
            <p>Newton formulated the law of gravitation in 1687, but the numerical value of \(G\) was unknown for over a century. In 1798, British scientist Henry Cavendish performed the famed <strong>Cavendish Torsion Balance Experiment</strong>, measuring the minuscule deflection of lead spheres suspended on a delicate torsion fiber to determine \(G\) and compute Earth’s density.</p>
          </div>
          <div class="faq-item">
            <h3>Why do ocean tides occur on both sides of Earth simultaneously?</h3>
            <p>Tidal forces are caused by differential gravitational attraction across Earth’s finite diameter (\(12,742\text{ km}\)). The ocean facing the Moon experiences a stronger gravitational pull than Earth's solid center, creating a bulge toward the Moon. Simultaneously, Earth's center is pulled toward the Moon more strongly than the far-side oceans, leaving a secondary tidal bulge on the opposite side.</p>
          </div>
          <div class="faq-item">
            <h3>How does Einstein's General Relativity modify Newtonian gravity?</h3>
            <p>Newton treated gravity as an instantaneous action-at-a-distance force across static space. In 1915, Albert Einstein’s General Relativity revealed that mass and energy curve the four-dimensional fabric of spacetime (\(G_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}\)). Objects simply follow geodesic straight lines through curved spacetime. Newtonian gravity serves as a near-perfect low-mass, low-speed approximation to Einstein’s field equations.</p>
          </div>
          <div class="faq-item">
            <h3>What are the Lagrange Points in a two-body gravitational system?</h3>
            <p>In orbital mechanics, Lagrange points (\(L_1\) through \(L_5\)) are five equilibrium positions in an orbital configuration where the combined gravitational pull of two large masses (such as the Sun and Earth) precisely matches the centripetal force required for a small third body to orbit with them synchronously.</p>
          </div>
        </article>
      </div>

      <aside class="sidebar" id="toolSidebar">
        <!-- Injected via apply_sidebars_all.py -->
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <p>&copy; 2026 CalcHub. All rights reserved. Precision engineering, science, and technical calculation tools.</p>
    </div>
  </footer>

  <script>
    // Astrophysical Presets
    const gravPresets = {
      earth_moon: { m1: 5.9722e24, u1: 'kg', m2: 7.342e22, u2: 'kg', r: 384400, ur: 'km' },
      earth_sun: { m1: 1.989e30, u1: 'kg', m2: 5.9722e24, u2: 'kg', r: 1.496e8, ur: 'km' },
      earth_iss: { m1: 5.9722e24, u1: 'kg', m2: 420000, u2: 'kg', r: 6791, ur: 'km' },
      earth_person: { m1: 5.9722e24, u1: 'kg', m2: 70, u2: 'kg', r: 6371, ur: 'km' },
      moon_person: { m1: 7.342e22, u1: 'kg', m2: 70, u2: 'kg', r: 1737.4, ur: 'km' },
      two_humans: { m1: 75, u1: 'kg', m2: 75, u2: 'kg', r: 1.0, ur: 'm' }
    };

    const G = 6.67430e-11;

    const toKg = (m, unit) => {
      switch(unit) {
        case 'earth': return m * 5.9722e24;
        case 'solar': return m * 1.989e30;
        case 'lbs': return m * 0.45359237;
        default: return m;
      }
    };
    const toMeters = (r, unit) => {
      switch(unit) {
        case 'km': return r * 1000;
        case 'au': return r * 149597870700;
        case 'mi': return r * 1609.344;
        default: return r;
      }
    };

    function applyPreset() {
      const p = document.getElementById('gravPreset').value;
      if (p !== 'custom' && gravPresets[p]) {
        const data = gravPresets[p];
        document.getElementById('valM1').value = data.m1;
        document.getElementById('unitM1').value = data.u1;
        document.getElementById('valM2').value = data.m2;
        document.getElementById('unitM2').value = data.u2;
        document.getElementById('valDist').value = data.r;
        document.getElementById('unitDist').value = data.ur;
      }
      calculate();
    }

    function calculate() {
      const rawM1 = parseFloat(document.getElementById('valM1').value) || 0;
      const unitM1 = document.getElementById('unitM1').value;
      const m1 = toKg(rawM1, unitM1);

      const rawM2 = parseFloat(document.getElementById('valM2').value) || 0;
      const unitM2 = document.getElementById('unitM2').value;
      const m2 = toKg(rawM2, unitM2);

      const rawDist = parseFloat(document.getElementById('valDist').value) || 1;
      const unitDist = document.getElementById('unitDist').value;
      const r = toMeters(rawDist, unitDist);

      if (r <= 0 || m1 <= 0 || m2 <= 0) return;

      // F = G * m1 * m2 / r^2
      const F = (G * m1 * m2) / (r * r);
      const a1 = F / m1;
      const a2 = F / m2;
      const U = -(G * m1 * m2) / r;

      // Render Primary Box
      if (F > 1e18) {
        document.getElementById('resForce').textContent = F.toExponential(3) + " N";
      } else if (F > 1000000) {
        document.getElementById('resForce').textContent = (F / 1000000).toFixed(2) + " MN (" + F.toExponential(2) + " N)";
      } else if (F > 1000) {
        document.getElementById('resForce').textContent = (F / 1000).toFixed(2) + " kN (" + F.toFixed(1) + " N)";
      } else if (F < 0.001) {
        document.getElementById('resForce').textContent = F.toExponential(3) + " N";
      } else {
        document.getElementById('resForce').textContent = F.toFixed(3) + " N";
      }

      const lbf = F / 4.4482216;
      let lbfStr = lbf > 1e6 ? lbf.toExponential(3) : lbf.toLocaleString('en-US', {maximumFractionDigits: 1});
      document.getElementById('resForceSub').textContent = "Equivalent to " + lbfStr + " lbf mutual attraction";

      // Render Grid Items
      document.getElementById('resAcc1').textContent = a1 < 0.0001 ? a1.toExponential(3) + " m/s²" : a1.toFixed(3) + " m/s²";
      document.getElementById('resAcc2').textContent = a2 < 0.0001 ? a2.toExponential(3) + " m/s²" : a2.toFixed(3) + " m/s²";
      document.getElementById('resPotEnergy').textContent = U.toExponential(3) + " Joules";

      const r_km = r / 1000;
      const r_mi = r / 1609.344;
      document.getElementById('resDistFormat').textContent = 
        r_km.toLocaleString('en-US', {maximumFractionDigits: 1}) + " km (" + 
        r_mi.toLocaleString('en-US', {maximumFractionDigits: 0}) + " miles)";
    }

    document.getElementById('gravPreset').addEventListener('change', applyPreset);
    document.querySelectorAll('input, select').forEach(el => {
      if (el.id !== 'gravPreset') {
        el.addEventListener('input', () => {
          document.getElementById('gravPreset').value = 'custom';
          calculate();
        });
        el.addEventListener('change', () => {
          document.getElementById('gravPreset').value = 'custom';
          calculate();
        });
      }
    });

    document.getElementById('calcBtn').addEventListener('click', calculate);
    document.getElementById('resetBtn').addEventListener('click', () => {
      document.getElementById('gravPreset').value = 'earth_moon';
      applyPreset();
    });

    window.addEventListener('DOMContentLoaded', calculate);
  </script>
</body>
</html>
"""

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p1 = os.path.join(base_dir, "friction-calculator.html")
    p2 = os.path.join(base_dir, "gravitational-force-calculator.html")

    with open(p1, "w", encoding="utf-8") as f:
        f.write(TOOL_1_HTML)
    print(f"Generated {p1}")

    with open(p2, "w", encoding="utf-8") as f:
        f.write(TOOL_2_HTML)
    print(f"Generated {p2}")

if __name__ == "__main__":
    main()
