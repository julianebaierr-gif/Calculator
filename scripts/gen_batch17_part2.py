# -*- coding: utf-8 -*-
"""
Script to generate Batch 17 Part 2 tools:
1. acceleration-calculator.html
2. angular-velocity-calculator.html
"""
import os

TOOL_1_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Acceleration Calculator | Kinematic Motion & SUVAT Solver</title>
  <meta name="description" content="Calculate uniform linear acceleration, final velocity, initial speed, displacement, travel time, and g-force equivalents using Newtonian SUVAT kinematics.">
  <link rel="canonical" href="https://calchub.cloud/acceleration-calculator.html">
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
        "name": "Acceleration Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Computes linear acceleration, final velocity, displacement, elapsed transit time, and gravitational force load factors based on standard classical kinematic equations.",
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
            "name": "What is the primary formula for calculating uniform acceleration?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The primary kinematic formula for uniform linear acceleration is a = (v - u) / t, where 'a' represents acceleration in meters per second squared (m/s²), 'v' is final velocity in m/s, 'u' is initial velocity in m/s, and 't' is time interval in seconds."
            }
          },
          {
            "@type": "Question",
            "name": "How does acceleration convert into standard Earth G-forces (g)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Standard gravitational acceleration at Earth's surface (1g) equals exactly 9.80665 m/s² (32.174 ft/s²). To convert linear acceleration into G-force load, divide the calculated acceleration value by 9.80665 m/s²."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between negative acceleration and deceleration?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Acceleration is a directional vector quantity. 'Negative acceleration' mathematically denotes acceleration pointing in the negative coordinate direction. 'Deceleration' specifically refers to a reduction in absolute speed, which occurs whenever the acceleration vector opposes the current velocity vector."
            }
          },
          {
            "@type": "Question",
            "name": "Which kinematic equation should be used if elapsed time is unknown?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "When elapsed time 't' is unknown, the Torricelli kinematic equation v² = u² + 2as should be used, enabling direct calculation of acceleration as a = (v² - u²) / (2s), where 's' is total linear displacement."
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
        <h1>Acceleration Calculator</h1>
        <p class="lead-text">Compute uniform acceleration, final velocity, elapsed travel time, braking distance, and peak g-force load using classical Newtonian SUVAT kinematics.</p>

        <div class="calc-card">
          <div class="form-group">
            <label for="calcMode">Calculation Target</label>
            <select id="calcMode" class="form-control">
              <option value="find_a">Solve for Acceleration (a) [Given u, v, t]</option>
              <option value="find_a_dist">Solve for Acceleration (a) [Given u, v, s]</option>
              <option value="find_v">Solve for Final Velocity (v) [Given u, a, t]</option>
              <option value="find_s">Solve for Distance / Displacement (s) [Given u, a, t]</option>
              <option value="find_t">Solve for Time (t) [Given u, v, a]</option>
            </select>
          </div>

          <div class="form-row">
            <div class="form-group col-half" id="grp_u">
              <label for="val_u">Initial Velocity (u)</label>
              <div class="input-with-unit">
                <input type="number" id="val_u" class="form-control" value="0" step="any">
                <select id="unit_u" class="unit-select">
                  <option value="mps">m/s</option>
                  <option value="kph">km/h</option>
                  <option value="mph">mph</option>
                  <option value="fps">ft/s</option>
                </select>
              </div>
            </div>

            <div class="form-group col-half" id="grp_v">
              <label for="val_v">Final Velocity (v)</label>
              <div class="input-with-unit">
                <input type="number" id="val_v" class="form-control" value="27.778" step="any">
                <select id="unit_v" class="unit-select">
                  <option value="mps" selected>m/s (100 km/h)</option>
                  <option value="kph">km/h</option>
                  <option value="mph">mph</option>
                  <option value="fps">ft/s</option>
                </select>
              </div>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group col-half" id="grp_a" style="display:none;">
              <label for="val_a">Acceleration (a)</label>
              <div class="input-with-unit">
                <input type="number" id="val_a" class="form-control" value="3.5" step="any">
                <select id="unit_a" class="unit-select">
                  <option value="mps2">m/s²</option>
                  <option value="fps2">ft/s²</option>
                  <option value="g">g (standard)</option>
                </select>
              </div>
            </div>

            <div class="form-group col-half" id="grp_t">
              <label for="val_t">Elapsed Time (t)</label>
              <div class="input-with-unit">
                <input type="number" id="val_t" class="form-control" value="7.5" step="any" min="0.0001">
                <select id="unit_t" class="unit-select">
                  <option value="s">Seconds (s)</option>
                  <option value="min">Minutes</option>
                  <option value="h">Hours</option>
                </select>
              </div>
            </div>

            <div class="form-group col-half" id="grp_s" style="display:none;">
              <label for="val_s">Displacement / Distance (s)</label>
              <div class="input-with-unit">
                <input type="number" id="val_s" class="form-control" value="100" step="any">
                <select id="unit_s" class="unit-select">
                  <option value="m">Meters (m)</option>
                  <option value="km">Kilometers (km)</option>
                  <option value="ft">Feet (ft)</option>
                  <option value="mi">Miles</option>
                </select>
              </div>
            </div>
          </div>

          <div class="btn-group">
            <button type="button" id="calcBtn" class="btn btn-primary">Calculate Motion</button>
            <button type="button" id="resetBtn" class="btn btn-secondary">Reset Defaults</button>
          </div>

          <div id="resultsPanel" class="results-panel">
            <div class="result-box primary-result">
              <div class="result-label" id="primaryLabel">Calculated Acceleration (a)</div>
              <div class="result-value" id="primaryValue">3.704 m/s²</div>
              <div class="result-sub" id="primarySub">Equivalent to 0.378 g load factor</div>
            </div>

            <div class="result-grid">
              <div class="result-item">
                <span class="sub-label">Displacement / Distance (s)</span>
                <span class="sub-value" id="secDistance">104.17 m (341.8 ft)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Average Velocity (v_avg)</span>
                <span class="sub-value" id="secAvgVel">13.89 m/s (50.0 km/h)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Elapsed Transit Time (t)</span>
                <span class="sub-value" id="secTime">7.50 seconds</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Specific Kinetic Energy Change</span>
                <span class="sub-value" id="secEnergy">385.8 J/kg</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. Fundamentals of Classical Linear Acceleration</h2>
          <p>In classical Newtonian mechanics, acceleration describes the instantaneous or time-averaged rate of change of an object's velocity vector with respect to time. Because velocity comprises both magnitude (speed) and directional orientation, acceleration can arise through increasing linear speed, decreasing linear speed (commonly referred to as braking or deceleration), or continuously redirecting the trajectory path as observed in orbital and circular motions.</p>
          <p>For one-dimensional rectilinear translation under the assumption of a constant (uniform) net force, the average acceleration \(\bar{a}\) over an elapsed time interval \(\Delta t = t_2 - t_1\) is defined by the fundamental differential quotient:</p>
          <div class="math-block">
            $$a = \frac{\Delta v}{\Delta t} = \frac{v - u}{t}$$
          </div>
          <p>Where \(u\) is initial translational velocity in meters per second (\(\text{m/s}\)), \(v\) is final translational velocity in \(\text{m/s}\), and \(t\) is total elapsed duration in seconds (\(\text{s}\)). The standard Système International (SI) derived unit of linear acceleration is meters per second squared (\(\text{m/s}^2\)), which directly represents the velocity change in meters per second accumulated during every single second of sustained motion.</p>

          <h2>2. The Core SUVAT Kinematic Equations</h2>
          <p>When an engineering system undergoes constant linear acceleration—such as an aircraft accelerating down an uninclined runway, a high-speed passenger train decelerating during regenerative service braking, or an elevator carriage rising between skyscraper floors—the motion is completely governed by five interconnected variables collectively known by the British acronym <strong>SUVAT</strong>:</p>
          <ul>
            <li><strong>s</strong> = Linear displacement or net distance traversed (\(\text{m}\))</li>
            <li><strong>u</strong> = Initial translational velocity (\(\text{m/s}\))</li>
            <li><strong>v</strong> = Final translational velocity (\(\text{m/s}\))</li>
            <li><strong>a</strong> = Uniform linear acceleration (\(\text{m/s}^2\))</li>
            <li><strong>t</strong> = Total elapsed travel duration (\(\text{s}\))</li>
          </ul>
          <p>By algebraically integrating Newton's second law of motion under constant boundary conditions, physicists and mechanical engineers utilize four invariant kinematic formulations:</p>
          <div class="math-block">
            $$v = u + at$$
          </div>
          <div class="math-block">
            $$s = ut + \frac{1}{2}at^2$$
          </div>
          <div class="math-block">
            $$v^2 = u^2 + 2as$$
          </div>
          <div class="math-block">
            $$s = \left(\frac{u + v}{2}\right) t$$
          </div>
          <p>In real-world engineering projects where tracking continuous temporal position is unfeasible—such as forensic automobile crash reconstruction or structural crash-cushion design—the Torricelli equation \(v^2 = u^2 + 2as\) eliminates the time parameter entirely, allowing engineers to isolate required deceleration rates directly from tire skid-mark measurements and residual vehicle structural deformations:</p>
          <div class="math-block">
            $$a = \frac{v^2 - u^2}{2s}$$
          </div>

          <h2>3. Real-World Engineering Acceleration Benchmarks</h2>
          <p>To provide practical physical context when verifying mechanical simulations, robotic motion profiles, and automotive dynamometer testing, the reference table below outlines representative linear acceleration rates and corresponding standardized gravitational load factors (\(g = 9.80665\text{ m/s}^2\)):</p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Physical Dynamic Scenario</th>
                <th>Acceleration (\(\text{m/s}^2\))</th>
                <th>Equivalent G-Force (\(g\))</th>
                <th>Typical Operational Context</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Commercial High-Speed Rail (TGV / Shinkansen)</td>
                <td>0.5 – 0.8</td>
                <td>0.05 – 0.08 g</td>
                <td>Passenger comfort ceiling during normal station departure</td>
              </tr>
              <tr>
                <td>Modern Skyscraper Passenger Elevator</td>
                <td>1.0 – 1.5</td>
                <td>0.10 – 0.15 g</td>
                <td>ISO 18738 passenger ride quality vertical comfort limit</td>
              </tr>
              <tr>
                <td>Standard Family Sedan (0 to 100 km/h in 9.5 s)</td>
                <td>2.92</td>
                <td>0.30 g</td>
                <td>Typical highway on-ramp merge acceleration rate</td>
              </tr>
              <tr>
                <td>Heavy Road Truck Emergency Antilock Braking</td>
                <td>5.5 – 6.5</td>
                <td>0.56 – 0.66 g</td>
                <td>Dry asphalt road tire-pavement friction coefficient limit</td>
              </tr>
              <tr>
                <td>Earth Surface Free-Fall Gravity (\(g_0\))</td>
                <td>9.81</td>
                <td>1.00 g</td>
                <td>Unresisted gravitational acceleration at sea level (45° lat)</td>
              </tr>
              <tr>
                <td>Formula 1 Braking Zone (Corner Entry)</td>
                <td>45.0 – 55.0</td>
                <td>4.6 – 5.6 g</td>
                <td>High aerodynamic downforce carbon-ceramic brake engagement</td>
              </tr>
              <tr>
                <td>Spacecraft Ascent Stage Max-Q (Falcon 9 / Saturn V)</td>
                <td>29.4 – 39.2</td>
                <td>3.0 – 4.0 g</td>
                <td>Human astronaut sustained acceleration structural safety threshold</td>
              </tr>
              <tr>
                <td>Automotive Airbag Pyrotechnic Sensor Trigger</td>
                <td>150.0 – 300.0</td>
                <td>15 – 30 g</td>
                <td>Micro-electro-mechanical (MEMS) crash deceleration boundary</td>
              </tr>
            </tbody>
          </table>

          <h2>4. Worked Engineering Case Study: High-Speed Train Deceleration Profile</h2>
          <div class="worked-example-card">
            <h3>Problem Statement</h3>
            <p>An intercity electric passenger train travels at a cruising velocity of \(250\text{ km/h}\) (\(69.444\text{ m/s}\)). Approaching a metropolitan terminal zone, signal interlocking automation commands the braking system to bring the train smoothly to a controlled stop (\(v = 0\text{ m/s}\)) across an allowable track length of \(2,200\text{ meters}\).</p>
            <p><strong>Required:</strong> Determine the uniform deceleration rate \(a\) (in \(\text{m/s}^2\) and \(g\)-load) and calculate the total stopping time \(t\) required to reach a complete standstill.</p>

            <h3>Step-by-Step Mathematical Solution</h3>
            <p><strong>Step 1: Convert units into standard SI metric values:</strong></p>
            <ul>
              <li>Initial velocity: \(u = 250\text{ km/h} \div 3.6 = 69.444\text{ m/s}\)</li>
              <li>Final velocity: \(v = 0\text{ m/s}\)</li>
              <li>Stopping distance: \(s = 2,200\text{ m}\)</li>
            </ul>

            <p><strong>Step 2: Calculate required deceleration rate using the Torricelli equation:</strong></p>
            <div class="math-block">
              $$v^2 = u^2 + 2as \implies a = \frac{v^2 - u^2}{2s}$$
            </div>
            <div class="math-block">
              $$a = \frac{0^2 - (69.444)^2}{2 \times 2,200} = \frac{-4822.53}{4,400} = -1.096\text{ m/s}^2$$
            </div>
            <p>The negative sign confirms deceleration opposing the travel direction. The absolute deceleration magnitude is \(1.096\text{ m/s}^2\).</p>

            <p><strong>Step 3: Convert deceleration into gravitational G-force load factor:</strong></p>
            <div class="math-block">
              $$\text{G-force} = \frac{|a|}{9.80665} = \frac{1.096}{9.80665} \approx 0.112\text{ g}$$
            </div>
            <p>This falls comfortably within European railway passenger ride-quality standards (maximum service deceleration \(\le 1.2\text{ m/s}^2\)).</p>

            <p><strong>Step 4: Calculate total elapsed stopping duration:</strong></p>
            <div class="math-block">
              $$t = \frac{v - u}{a} = \frac{0 - 69.444}{-1.096} \approx 63.36\text{ seconds (1.06 minutes)}$$
            </div>
            <p><strong>Verification via average velocity:</strong> Average speed \(\bar{v} = (69.444 + 0)/2 = 34.722\text{ m/s}\). Total distance \(s = \bar{v} \times t = 34.722 \times 63.36 = 2,200.0\text{ m}\), confirming algebraic exactness.</p>
          </div>

          <h2>5. Critical Design Considerations and Common Pitfalls</h2>
          <p>When applying kinematic formulations across physical and mechanical designs, engineers and students must guard against three prevalent misconceptions:</p>
          <ul>
            <li><strong>Non-Constant Acceleration Regimes:</strong> SUVAT relationships strictly presuppose constant linear acceleration. In internal combustion or electric motor vehicles, torque curves and aerodynamic drag (\(F_{\text{drag}} \propto v^2\)) cause instantaneous acceleration to drop significantly as velocity increases. When acceleration varies with time or speed, differential integration \(s = \int v(t)\,dt\) or numerical Euler/Runge-Kutta solvers must be deployed.</li>
            <li><strong>Deceleration Direction Confusion:</strong> A negative sign on acceleration does not inherently indicate slowing down. If an object is moving in the negative coordinate direction (\(u < 0\)) and undergoes negative acceleration (\(a < 0\)), its absolute speed actually increases. Deceleration occurs if and only if the vector dot product \(\vec{a} \cdot \vec{v} < 0\).</li>
            <li><strong>Aerodynamic Drag in Gravitational Free-Fall:</strong> Treating falling bodies as possessing pure \(9.81\text{ m/s}^2\) acceleration over long vertical drops introduces severe design errors. Atmospheric drag rapidly balances weight at terminal velocity \(v_t = \sqrt{2mg / (\rho C_d A)}\), at which point net linear acceleration drops identically to zero.</li>
          </ul>

          <h2>6. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-item">
            <h3>How do you calculate acceleration without having the elapsed time?</h3>
            <p>When time is unmeasured or variable, utilize the kinematic energy relation \(v^2 = u^2 + 2as\). Rearranging the formula yields \(a = (v^2 - u^2) / (2s)\). You only need the initial speed, final speed, and total linear distance traversed.</p>
          </div>
          <div class="faq-item">
            <h3>What is the difference between average and instantaneous acceleration?</h3>
            <p>Average acceleration measures total net velocity change across an extended macroscopic time window (\(\Delta v / \Delta t\)). Instantaneous acceleration represents the infinitesimal first time derivative of velocity (\(a = dv/dt\)) at one exact mathematical instant, measured continuously by vehicle accelerometers.</p>
          </div>
          <div class="faq-item">
            <h3>Can an object have a velocity of zero while having non-zero acceleration?</h3>
            <p>Yes. A classic example is a ball thrown vertically into the air. At the apex of its trajectory, its instantaneous velocity is precisely zero (\(v = 0\text{ m/s}\)). However, Earth's downward gravitational acceleration remains fully active at \(9.81\text{ m/s}^2\), causing the ball to immediately transition into downward motion.</p>
          </div>
          <div class="faq-item">
            <h3>How do units of km/h² relate to standard m/s²?</h3>
            <p>To convert kilometers per hour squared (\(\text{km/h}^2\)) into meters per second squared (\(\text{m/s}^2\)), divide by \(12,960\) (\(3,600^2 / 1,000\)). Conversely, to convert \(\text{m/s}^2\) into \(\text{km/h}^2\), multiply the value by \(12,960\).</p>
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
    // Calculation Engine
    const toMps = (v, unit) => {
      switch(unit) {
        case 'kph': return v / 3.6;
        case 'mph': return v * 0.44704;
        case 'fps': return v * 0.3048;
        default: return v;
      }
    };
    const fromMps = (v, unit) => {
      switch(unit) {
        case 'kph': return v * 3.6;
        case 'mph': return v / 0.44704;
        case 'fps': return v / 0.3048;
        default: return v;
      }
    };
    const toSeconds = (t, unit) => {
      switch(unit) {
        case 'min': return t * 60;
        case 'h': return t * 3600;
        default: return t;
      }
    };
    const toMeters = (s, unit) => {
      switch(unit) {
        case 'km': return s * 1000;
        case 'ft': return s * 0.3048;
        case 'mi': return s * 1609.344;
        default: return s;
      }
    };
    const toMps2 = (a, unit) => {
      switch(unit) {
        case 'fps2': return a * 0.3048;
        case 'g': return a * 9.80665;
        default: return a;
      }
    };

    function updateFormVisibility() {
      const mode = document.getElementById('calcMode').value;
      document.getElementById('grp_u').style.display = 'block';
      document.getElementById('grp_v').style.display = 'block';
      document.getElementById('grp_t').style.display = 'block';
      document.getElementById('grp_s').style.display = 'none';
      document.getElementById('grp_a').style.display = 'none';

      if (mode === 'find_a') {
        // u, v, t visible
      } else if (mode === 'find_a_dist') {
        document.getElementById('grp_t').style.display = 'none';
        document.getElementById('grp_s').style.display = 'block';
      } else if (mode === 'find_v') {
        document.getElementById('grp_v').style.display = 'none';
        document.getElementById('grp_a').style.display = 'block';
      } else if (mode === 'find_s') {
        document.getElementById('grp_v').style.display = 'none';
        document.getElementById('grp_a').style.display = 'block';
      } else if (mode === 'find_t') {
        document.getElementById('grp_t').style.display = 'none';
        document.getElementById('grp_a').style.display = 'block';
      }
      calculate();
    }

    function calculate() {
      const mode = document.getElementById('calcMode').value;
      const u = toMps(parseFloat(document.getElementById('val_u').value) || 0, document.getElementById('unit_u').value);
      const v = toMps(parseFloat(document.getElementById('val_v').value) || 0, document.getElementById('unit_v').value);
      const t = toSeconds(parseFloat(document.getElementById('val_t').value) || 1, document.getElementById('unit_t').value);
      const s = toMeters(parseFloat(document.getElementById('val_s').value) || 1, document.getElementById('unit_s').value);
      const a = toMps2(parseFloat(document.getElementById('val_a').value) || 0, document.getElementById('unit_a').value);

      let calc_a = 0, calc_v = 0, calc_s = 0, calc_t = 0;

      if (mode === 'find_a') {
        calc_a = (v - u) / (t || 0.0001);
        calc_v = v;
        calc_t = t;
        calc_s = u * t + 0.5 * calc_a * t * t;
      } else if (mode === 'find_a_dist') {
        calc_a = (v * v - u * u) / (2 * (s || 0.0001));
        calc_v = v;
        calc_s = s;
        calc_t = Math.abs(calc_a) > 1e-6 ? (v - u) / calc_a : (2 * s) / (u + v || 0.0001);
      } else if (mode === 'find_v') {
        calc_a = a;
        calc_t = t;
        calc_v = u + a * t;
        calc_s = u * t + 0.5 * a * t * t;
      } else if (mode === 'find_s') {
        calc_a = a;
        calc_t = t;
        calc_v = u + a * t;
        calc_s = u * t + 0.5 * a * t * t;
      } else if (mode === 'find_t') {
        calc_a = a;
        calc_v = v;
        calc_t = Math.abs(a) > 1e-6 ? (v - u) / a : 0;
        calc_s = u * calc_t + 0.5 * a * calc_t * calc_t;
      }

      const pLabel = document.getElementById('primaryLabel');
      const pVal = document.getElementById('primaryValue');
      const pSub = document.getElementById('primarySub');

      if (mode === 'find_a' || mode === 'find_a_dist') {
        pLabel.textContent = "Calculated Acceleration (a)";
        pVal.textContent = calc_a.toFixed(3) + " m/s² (" + (calc_a * 3.28084).toFixed(3) + " ft/s²)";
        pSub.textContent = "Gravitational Load Equivalent: " + (calc_a / 9.80665).toFixed(3) + " g";
      } else if (mode === 'find_v') {
        pLabel.textContent = "Calculated Final Velocity (v)";
        pVal.textContent = calc_v.toFixed(2) + " m/s (" + (calc_v * 3.6).toFixed(1) + " km/h)";
        pSub.textContent = "Equivalent to " + (calc_v * 2.23694).toFixed(1) + " mph (" + (calc_v * 3.28084).toFixed(1) + " ft/s)";
      } else if (mode === 'find_s') {
        pLabel.textContent = "Calculated Displacement / Distance (s)";
        pVal.textContent = calc_s.toFixed(2) + " m (" + (calc_s * 3.28084).toFixed(1) + " ft)";
        pSub.textContent = "Equivalent to " + (calc_s / 1000).toFixed(3) + " km (" + (calc_s / 1609.344).toFixed(3) + " miles)";
      } else if (mode === 'find_t') {
        pLabel.textContent = "Calculated Transit Time (t)";
        pVal.textContent = calc_t.toFixed(3) + " seconds";
        pSub.textContent = "Equivalent to " + (calc_t / 60).toFixed(2) + " minutes";
      }

      document.getElementById('secDistance').textContent = calc_s.toFixed(2) + " m (" + (calc_s * 3.28084).toFixed(1) + " ft)";
      const avgVel = (u + calc_v) / 2;
      document.getElementById('secAvgVel').textContent = avgVel.toFixed(2) + " m/s (" + (avgVel * 3.6).toFixed(1) + " km/h)";
      document.getElementById('secTime').textContent = calc_t.toFixed(2) + " seconds";
      const deltaEk = 0.5 * (calc_v * calc_v - u * u);
      document.getElementById('secEnergy').textContent = deltaEk.toFixed(1) + " J/kg";
    }

    document.getElementById('calcMode').addEventListener('change', updateFormVisibility);
    document.querySelectorAll('input, select').forEach(el => {
      el.addEventListener('input', calculate);
      el.addEventListener('change', calculate);
    });
    document.getElementById('calcBtn').addEventListener('click', calculate);
    document.getElementById('resetBtn').addEventListener('click', () => {
      document.getElementById('calcMode').value = 'find_a';
      document.getElementById('val_u').value = '0';
      document.getElementById('val_v').value = '27.778';
      document.getElementById('val_t').value = '7.5';
      updateFormVisibility();
    });

    window.addEventListener('DOMContentLoaded', updateFormVisibility);
  </script>
</body>
</html>
"""

TOOL_2_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Angular Velocity Calculator | RPM, Rad/s & Tangential Speed</title>
  <meta name="description" content="Convert between RPM, radians per second (rad/s), and degrees/s. Calculate tangential linear velocity, centripetal acceleration, and rotation period.">
  <link rel="canonical" href="https://calchub.cloud/angular-velocity-calculator.html">
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
        "name": "Angular Velocity Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates rotational speed conversions (RPM, rad/s, Hz), tangential peripheral velocity, radial centripetal acceleration, and rotational period for rotating machinery.",
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
            "name": "How do you convert RPM (revolutions per minute) to radians per second (rad/s)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Because one complete revolution encompasses 2π radians and one minute equals 60 seconds, the exact conversion formula is: ω (rad/s) = RPM × (2π / 60) ≈ RPM × 0.104719755."
            }
          },
          {
            "@type": "Question",
            "name": "What is the relationship between angular velocity and linear tangential speed?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Linear tangential velocity (v) at any radial point is directly proportional to angular velocity (ω in rad/s) and radial distance (r): v = ω × r. Doubling the distance from the axis of rotation doubles the peripheral linear speed."
            }
          },
          {
            "@type": "Question",
            "name": "How is centripetal acceleration derived from angular velocity?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The inward radial acceleration keeping a mass in circular trajectory equals a_c = v² / r = ω² × r. Expressing centripetal acceleration in terms of angular velocity demonstrates quadratic scaling with rotational speed."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between rotational frequency and angular velocity?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Rotational frequency (f or Hz) measures complete cycles or revolutions per unit time (rev/s). Angular velocity (ω) measures the swept angular displacement in radians per unit time. They are related by the factor 2π: ω = 2πf."
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
        <h1>Angular Velocity Calculator</h1>
        <p class="lead-text">Convert rotational speed across RPM, rad/s, and Hz, while evaluating peripheral tangential speed, rim centripetal acceleration, and cycle period.</p>

        <div class="calc-card">
          <div class="form-row">
            <div class="form-group col-half">
              <label for="rotSpeed">Rotational Speed / Angular Velocity</label>
              <div class="input-with-unit">
                <input type="number" id="rotSpeed" class="form-control" value="1800" step="any">
                <select id="rotUnit" class="unit-select">
                  <option value="rpm" selected>RPM (rev/min)</option>
                  <option value="radps">rad/s</option>
                  <option value="hz">Hz (rev/s)</option>
                  <option value="degps">deg/s</option>
                </select>
              </div>
            </div>

            <div class="form-group col-half">
              <label for="radius">Rotor / Wheel Radius (r)</label>
              <div class="input-with-unit">
                <input type="number" id="radius" class="form-control" value="150" step="any">
                <select id="radUnit" class="unit-select">
                  <option value="mm" selected>Millimeters (mm)</option>
                  <option value="cm">Centimeters (cm)</option>
                  <option value="m">Meters (m)</option>
                  <option value="in">Inches (in)</option>
                  <option value="ft">Feet (ft)</option>
                </select>
              </div>
            </div>
          </div>

          <div class="btn-group">
            <button type="button" id="calcBtn" class="btn btn-primary">Calculate Dynamics</button>
            <button type="button" id="resetBtn" class="btn btn-secondary">Reset to Standard 4-Pole Motor</button>
          </div>

          <div id="resultsPanel" class="results-panel">
            <div class="result-box primary-result">
              <div class="result-label">Angular Velocity (&omega;)</div>
              <div class="result-value" id="resOmega">188.50 rad/s</div>
              <div class="result-sub" id="resOmegaSub">1,800.0 RPM &bull; 30.00 Hz (rev/s) &bull; 10,800.0 &deg;/s</div>
            </div>

            <div class="result-grid">
              <div class="result-item">
                <span class="sub-label">Tangential Linear Velocity (v)</span>
                <span class="sub-value" id="resTangVel">28.27 m/s (101.8 km/h)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Centripetal Acceleration (a_c)</span>
                <span class="sub-value" id="resCentAcc">5,329.6 m/s² (543.5 g)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Period of One Revolution (T)</span>
                <span class="sub-value" id="resPeriod">33.33 ms (0.0333 s)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Rotational Frequency (f)</span>
                <span class="sub-value" id="resFreq">30.00 Hz (cycles/sec)</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. Theoretical Foundation of Angular Velocity</h2>
          <p>Angular velocity represents the vector rate at which an object rotates or revolves around a specified central axis, quantifying how rapidly an angular displacement \(\theta\) changes with elapsed time \(t\). While linear velocity describes the straight-line displacement per unit time in meters per second (\(\text{m/s}\)), angular velocity describes rotational progress in radians per second (\(\text{rad/s}\)).</p>
          <p>For uniform circular rotation, the average angular velocity \(\omega\) is formulated as:</p>
          <div class="math-block">
            $$\omega = \frac{\Delta \theta}{\Delta t} = \frac{2\pi}{T} = 2\pi f$$
          </div>
          <p>Where \(\Delta \theta\) represents angular swept angle in radians, \(\Delta t\) is elapsed time in seconds, \(T\) is the period required to complete one full revolution (\(T = 1/f\)), and \(f\) is rotational frequency in revolutions per second (\(\text{Hz}\)). In vector mechanics, angular velocity \(\vec{\omega}\) is an axial pseudovector oriented perpendicular to the plane of rotation, with its pointing direction rigorously dictated by the classical Right-Hand Grip Rule.</p>

          <h2>2. Conversion Mathematics: RPM, Rad/s, and Degrees/s</h2>
          <p>Rotating machinery, industrial prime movers, automotive internal combustion engines, and electric servomotors are overwhelmingly rated on equipment nameplates in revolutions per minute (<strong>RPM</strong>). However, all core physical dynamics and stress formulations mandate the use of radians per second. The derivation for the dimensional conversion factor proceeds as follows:</p>
          <ul>
            <li>One full revolution equals exactly \(2\pi\) radians (\(\approx 6.2831853\text{ rad}\)).</li>
            <li>One minute contains exactly \(60\) seconds.</li>
          </ul>
          <p>Consequently, the direct scaling relationship connecting rotational RPM to angular speed \(\omega\) in \(\text{rad/s}\) is:</p>
          <div class="math-block">
            $$\omega = \text{RPM} \times \left(\frac{2\pi\text{ rad}}{60\text{ s}}\right) = \text{RPM} \times \left(\frac{\pi}{30}\right) \approx \text{RPM} \times 0.104719755$$
          </div>
          <p>Conversely, to convert known angular velocity in \(\text{rad/s}\) back into operational RPM:</p>
          <div class="math-block">
            $$\text{RPM} = \omega \times \left(\frac{30}{\pi}\right) \approx \omega \times 9.5492966$$
          </div>

          <h2>3. Tangential Velocity and Centripetal Acceleration</h2>
          <p>Every point on a rotating rigid body shares the exact same angular velocity \(\omega\). However, the linear peripheral speed—known as <strong>tangential velocity</strong> \(v\)—scales directly with the radial distance \(r\) from the rotational axis:</p>
          <div class="math-block">
            $$v = \omega \cdot r = \left(\frac{2\pi \cdot \text{RPM}}{60}\right) r$$
          </div>
          <p>Because the direction of the tangential velocity vector is continually changing throughout the circular orbit, the mass at radius \(r\) is subject to an inward radial acceleration called <strong>centripetal acceleration</strong> \(a_c\):</p>
          <div class="math-block">
            $$a_c = \frac{v^2}{r} = \omega^2 r = \left(\frac{2\pi \cdot \text{RPM}}{60}\right)^2 r$$
          </div>
          <p>This formulation illustrates the fundamental reason why high-speed rotating components—such as gas turbine impellers, centrifugal superchargers, and ultracentrifuge rotors—experience massive structural hoop stresses: the centripetal acceleration and associated centrifugal bursting forces scale quadratically with rotational speed (\(\propto \omega^2\)).</p>

          <h2>4. Industrial and Engineering Benchmark Reference Table</h2>
          <p>To assist mechanical rotating equipment designers and test engineers, the table below provides representative angular velocities, operational RPMs, and typical rim tangential speeds across diverse engineering applications:</p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Rotating System / Machine</th>
                <th>Standard Speed (RPM)</th>
                <th>Angular Velocity \(\omega\) (rad/s)</th>
                <th>Typical Radius \(r\)</th>
                <th>Peripheral Tip Speed \(v\)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Earth Planetary Rotation (Sidereal Day)</td>
                <td>0.000694</td>
                <td>\(7.292 \times 10^{-5}\)</td>
                <td>6,378 km (Equator)</td>
                <td>465.1 m/s (1,674 km/h)</td>
              </tr>
              <tr>
                <td>Offshore Wind Turbine Rotor (15 MW)</td>
                <td>7.5 – 10.0</td>
                <td>0.785 – 1.047</td>
                <td>118 m (Blade tip)</td>
                <td>92.6 – 123.6 m/s (445 km/h)</td>
              </tr>
              <tr>
                <td>Hydraulic Francis Hydro-Turbine Runner</td>
                <td>100 – 375</td>
                <td>10.47 – 39.27</td>
                <td>2.5 m</td>
                <td>26.2 – 98.2 m/s</td>
              </tr>
              <tr>
                <td>4-Pole 60 Hz AC Induction Motor</td>
                <td>1,750 (Nominal slip)</td>
                <td>183.26</td>
                <td>75 mm (Shaft surface)</td>
                <td>13.74 m/s (49.5 km/h)</td>
              </tr>
              <tr>
                <td>Commercial Vehicle Alternator / Supercharger</td>
                <td>12,000 – 18,000</td>
                <td>1,256.6 – 1,885.0</td>
                <td>35 mm (Pulley rim)</td>
                <td>44.0 – 66.0 m/s</td>
              </tr>
              <tr>
                <td>Automotive Turbocharger Turbine Wheel</td>
                <td>120,000 – 220,000</td>
                <td>12,566 – 23,038</td>
                <td>25 mm (Inducer tip)</td>
                <td>314 – 576 m/s (Supersonic)</td>
              </tr>
              <tr>
                <td>High-Speed Dental Air-Bearing Drill</td>
                <td>350,000 – 400,000</td>
                <td>36,652 – 41,888</td>
                <td>0.8 mm (Bur edge)</td>
                <td>29.3 – 33.5 m/s</td>
              </tr>
              <tr>
                <td>Laboratory Analytical Ultracentrifuge</td>
                <td>60,000 – 100,000</td>
                <td>6,283 – 10,472</td>
                <td>70 mm (Tube well)</td>
                <td>440 – 733 m/s (\(> 800,000\text{ g}\))</td>
              </tr>
            </tbody>
          </table>

          <h2>5. Worked Engineering Case Study: High-Speed Centrifuge Rotor Stress Design</h2>
          <div class="worked-example-card">
            <h3>Problem Statement</h3>
            <p>A biochemical laboratory centrifuge is designed to separate viral particles from cell suspensions. The titanium rotor operates at a rotational speed of \(24,000\text{ RPM}\). The biological test samples sit in outer test-tube buckets located at a maximum radial distance of \(r = 120\text{ mm}\) (\(0.12\text{ m}\)) from the central spindle axis.</p>
            <p><strong>Required:</strong></p>
            <ol>
              <li>Compute the angular velocity \(\omega\) in radians per second.</li>
              <li>Determine the linear tangential speed \(v\) of the test-tube carriage.</li>
              <li>Calculate the centripetal acceleration \(a_c\) and express it as Relative Centrifugal Force (RCF in multiples of Earth \(g = 9.80665\text{ m/s}^2\)).</li>
            </ol>

            <h3>Step-by-Step Mathematical Solution</h3>
            <p><strong>Step 1: Calculate angular velocity \(\omega\):</strong></p>
            <div class="math-block">
              $$\omega = \text{RPM} \times \left(\frac{2\pi}{60}\right) = 24,000 \times \left(\frac{\pi}{30}\right) = 800\pi \approx 2,513.274\text{ rad/s}$$
            </div>

            <p><strong>Step 2: Calculate peripheral tangential velocity \(v\):</strong></p>
            <div class="math-block">
              $$v = \omega \cdot r = 2,513.274\text{ rad/s} \times 0.12\text{ m} \approx 301.59\text{ m/s}$$
            </div>
            <p>Converting to kilometers per hour: \(301.59 \times 3.6 = 1,085.7\text{ km/h}\) (nearing the speed of sound in air, requiring an evacuated vacuum chamber to mitigate aerodynamic frictional heating).</p>

            <p><strong>Step 3: Calculate centripetal acceleration \(a_c\):</strong></p>
            <div class="math-block">
              $$a_c = \omega^2 \cdot r = (2,513.274)^2 \times 0.12 \approx 6,316,547 \times 0.12 = 757,985.6\text{ m/s}^2$$
            </div>

            <p><strong>Step 4: Convert into Relative Centrifugal Force (G-force load factor):</strong></p>
            <div class="math-block">
              $$\text{RCF} = \frac{a_c}{g} = \frac{757,985.6}{9.80665} \approx 77,293\text{ g}$$
            </div>
            <p><strong>Engineering Conclusion:</strong> Every gram of biological fluid and carrier tube experiences an apparent outward body force equivalent to \(77.29\text{ kilograms}\) of gravitational weight, verifying that the titanium grade must possess high fatigue strength and ultrasonic flaw inspection certification.</p>
          </div>

          <h2>6. Practical Dynamics: Critical Speeds and Flywheel Kinetic Energy</h2>
          <p>In mechanical powertrain engineering, angular velocity directly determines two critical design phenomena:</p>
          <ul>
            <li><strong>Rotational Kinetic Energy Storage:</strong> Flywheels store kinetic energy based on their mass moment of inertia \(I\) and the square of angular velocity:
              <div class="math-block">
                $$E_k = \frac{1}{2} I \omega^2$$
              </div>
              Doubling the operational angular velocity quadruples the stored kinetic energy, making speed increase far more mass-efficient than adding physical flywheel weight.
            </li>
            <li><strong>Critical Shaft Whirling Resonance:</strong> Flexible transmission shafts exhibit natural lateral bending frequencies. When the rotational angular velocity matches the shaft's lateral natural frequency (\(\omega = \omega_n = \sqrt{k/m}\)), resonance causes severe dynamic deflection and catastrophic bearing failure unless traversed rapidly during startup acceleration.</li>
          </ul>

          <h2>7. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-item">
            <h3>Why must angular velocity be in rad/s rather than RPM for physical formulas?</h3>
            <p>A radian is a dimensionless ratio of arc length to radius (\(s / r\)). When calculating tangential speed (\(v = \omega r\)) or acceleration (\(a = \omega^2 r\)), using radians preserves consistent SI dimensional units (\(\text{m/s}\) and \(\text{m/s}^2\)). RPM includes an arbitrary unit of time (minutes) and cycles (revolutions) that require continuous conversion factors.</p>
          </div>
          <div class="faq-item">
            <h3>How is angular velocity related to motor torque and output shaft power?</h3>
            <p>Mechanical shaft power \(P\) in watts equals torque \(\tau\) in Newton-meters multiplied directly by angular velocity \(\omega\) in rad/s: \(P = \tau \times \omega\). Expressed in terms of RPM: \(P (\text{kW}) = (\tau \times \text{RPM}) / 9,548.8\).</p>
          </div>
          <div class="faq-item">
            <h3>What is the difference between angular speed and angular velocity?</h3>
            <p>Angular speed is a scalar representing solely the magnitude of rotational rate (e.g., \(100\text{ rad/s}\)). Angular velocity is a vector that specifies both rotational rate and axis orientation with direction defined by the right-hand rule.</p>
          </div>
          <div class="faq-item">
            <h3>How does angular acceleration (\(\alpha\)) relate to angular velocity (\(\omega\))?</h3>
            <p>Angular acceleration \(\alpha\) is the rate of change of angular velocity with respect to time: \(\alpha = d\omega / dt = (\omega_2 - \omega_1) / t\), measured in radians per second squared (\(\text{rad/s}^2\)).</p>
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
    // Rotational Speed Conversion Engine
    const toRadPerSec = (val, unit) => {
      switch(unit) {
        case 'rpm': return val * (Math.PI / 30);
        case 'hz': return val * (2 * Math.PI);
        case 'degps': return val * (Math.PI / 180);
        default: return val;
      }
    };
    const toMeters = (r, unit) => {
      switch(unit) {
        case 'mm': return r / 1000;
        case 'cm': return r / 100;
        case 'in': return r * 0.0254;
        case 'ft': return r * 0.3048;
        default: return r;
      }
    };

    function calculate() {
      const rawSpeed = parseFloat(document.getElementById('rotSpeed').value) || 0;
      const speedUnit = document.getElementById('rotUnit').value;
      const rawRadius = parseFloat(document.getElementById('radius').value) || 0;
      const radUnit = document.getElementById('radUnit').value;

      const omega = toRadPerSec(rawSpeed, speedUnit);
      const r_m = toMeters(rawRadius, radUnit);

      const rpm = omega * (30 / Math.PI);
      const hz = omega / (2 * Math.PI);
      const degps = omega * (180 / Math.PI);
      const period = hz > 1e-6 ? 1 / hz : 0;

      const v_tang = omega * r_m;
      const a_cent = omega * omega * r_m;
      const g_force = a_cent / 9.80665;

      document.getElementById('resOmega').textContent = omega.toFixed(2) + " rad/s";
      document.getElementById('resOmegaSub').textContent = 
        rpm.toLocaleString('en-US', {maximumFractionDigits: 1}) + " RPM • " + 
        hz.toFixed(2) + " Hz (rev/s) • " + 
        degps.toLocaleString('en-US', {maximumFractionDigits: 1}) + " °/s";

      document.getElementById('resTangVel').textContent = 
        v_tang.toFixed(2) + " m/s (" + (v_tang * 3.6).toFixed(1) + " km/h | " + (v_tang * 2.23694).toFixed(1) + " mph)";

      if (a_cent > 100000) {
        document.getElementById('resCentAcc').textContent = 
          a_cent.toExponential(3) + " m/s² (" + g_force.toLocaleString('en-US', {maximumFractionDigits: 1}) + " g)";
      } else {
        document.getElementById('resCentAcc').textContent = 
          a_cent.toFixed(1) + " m/s² (" + g_force.toFixed(1) + " g)";
      }

      if (period < 0.01 && period > 0) {
        document.getElementById('resPeriod').textContent = (period * 1000).toFixed(2) + " ms (" + period.toExponential(3) + " s)";
      } else {
        document.getElementById('resPeriod').textContent = period.toFixed(4) + " s";
      }

      document.getElementById('resFreq').textContent = hz.toFixed(2) + " Hz (" + (hz * 60).toFixed(0) + " rev/min)";
    }

    document.querySelectorAll('input, select').forEach(el => {
      el.addEventListener('input', calculate);
      el.addEventListener('change', calculate);
    });
    document.getElementById('calcBtn').addEventListener('click', calculate);
    document.getElementById('resetBtn').addEventListener('click', () => {
      document.getElementById('rotSpeed').value = '1750';
      document.getElementById('rotUnit').value = 'rpm';
      document.getElementById('radius').value = '75';
      document.getElementById('radUnit').value = 'mm';
      calculate();
    });

    window.addEventListener('DOMContentLoaded', calculate);
  </script>
</body>
</html>
"""

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p1 = os.path.join(base_dir, "acceleration-calculator.html")
    p2 = os.path.join(base_dir, "angular-velocity-calculator.html")

    with open(p1, "w", encoding="utf-8") as f:
        f.write(TOOL_1_HTML)
    print(f"Generated {p1}")

    with open(p2, "w", encoding="utf-8") as f:
        f.write(TOOL_2_HTML)
    print(f"Generated {p2}")

if __name__ == "__main__":
    main()
