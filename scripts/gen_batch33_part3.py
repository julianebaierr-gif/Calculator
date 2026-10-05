# -*- coding: utf-8 -*-
"""
Generator for Batch 33 - Part 3:
5. work-power-calculator.html
6. stress-strain-calculator.html
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 5. work-power-calculator.html
HTML_WORK_POWER = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Work and Power Calculator - Mechanical Work (W = Fd) &amp; Power (P = W/t)</title>
  <meta name="description" content="Calculate mechanical work (W = Fd cos θ), power (P = W/t = Fv), electrical wattage, and horsepower (HP). Master motor sizing, lifting dynamics, and efficiency.">
  <link rel="canonical" href="https://calchub.org/work-power-calculator.html">
  <meta property="og:title" content="Work &amp; Power Calculator - Mechanical &amp; Electrical Power Solver">
  <meta property="og:description" content="Free physics work and power calculator. Compute work W = Fd cos θ, mechanical power P = W/t, horsepower HP, and kilowatt ratings with step-by-step proofs.">
  <meta property="og:url" content="https://calchub.org/work-power-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Work &amp; Power Calculator - Classical Mechanics Tool">
  <meta name="twitter:description" content="Solve mechanical work, rate of energy transfer, and horsepower with multi-unit conversions and worked engineering case studies.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Work and Power Calculator",
    "url": "https://calchub.org/work-power-calculator.html",
    "description": "Calculates mechanical work, rate of energy transfer, electrical wattage, and mechanical horsepower across SI and imperial engineering units.",
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
        "name": "What is the formula for mechanical work in physics?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Mechanical work is defined as the dot product of force and displacement vectors: W = F * d * cos(θ), where W is work in Joules (J), F is applied force in Newtons (N), d is displacement in meters (m), and θ is the angle between the force and displacement vectors."
        }
      },
      {
        "@type": "Question",
        "name": "What is the relationship between work, power, and velocity?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Power is the temporal rate of doing work: P = W / t. Since W = F * d for constant parallel force, P = (F * d) / t = F * (d / t) = F * v, where v is instantaneous linear velocity."
        }
      },
      {
        "@type": "Question",
        "name": "How many Watts are in one mechanical horsepower (HP)?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "One imperial mechanical horsepower (1 HP) equals exactly 550 foot-pounds per second, which converts to approximately 745.699872 Watts (~746 W). Metric horsepower (PS or cv) equals approximately 735.49875 Watts."
        }
      },
      {
        "@type": "Question",
        "name": "Can mechanical work be zero even when a large force is applied?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. Work is zero if displacement is zero (d = 0, such as pushing against an unyielding brick wall) or if the applied force is perpendicular to displacement (θ = 90°, cos(90°) = 0, such as centripetal force in circular planetary orbits or carrying a suitcase horizontally)."
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
      <div class="calc-icon" aria-hidden="true">&#9889;</div>
      <h1>Work and Power Calculator</h1>
      <p class="calc-description">Compute mechanical work (\(W = Fd \cos\theta\)), power delivery (\(P = W/t = Fv\)), horsepower (HP), and electrical wattage with step-by-step engineering derivations.</p>
    </div>

    <div class="calculator-body">
      <div class="input-group">
        <label for="wp-mode">Calculation Mode</label>
        <select id="wp-mode" class="form-control" onchange="switchWPMode()">
          <option value="work-linear" selected>Mechanical Work: Force, Distance &amp; Angle (\(W = Fd \cos\theta\))</option>
          <option value="power-time">Power from Work &amp; Time (\(P = W / t\))</option>
          <option value="power-velocity">Power from Force &amp; Velocity (\(P = F \times v\))</option>
        </select>
      </div>

      <!-- Mode 1: Work Linear W = F d cos θ -->
      <div id="panel-work">
        <div class="input-grid">
          <div class="input-group">
            <label for="w-force">Applied Force (\(F\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="w-force" class="form-control" value="2500" step="any" min="0" style="flex: 2;">
              <select id="w-unit-force" class="form-control" style="flex: 1;" onchange="calculateWP()">
                <option value="N" selected>N</option>
                <option value="kN">kN</option>
                <option value="lbf">lbf</option>
              </select>
            </div>
          </div>

          <div class="input-group">
            <label for="w-dist">Displacement / Distance (\(d\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="w-dist" class="form-control" value="15" step="any" min="0" style="flex: 2;">
              <select id="w-unit-dist" class="form-control" style="flex: 1;" onchange="calculateWP()">
                <option value="m" selected>m</option>
                <option value="ft">ft</option>
                <option value="km">km</option>
              </select>
            </div>
          </div>
        </div>

        <div class="input-grid">
          <div class="input-group">
            <label for="w-angle">Force Angle to Motion (\(\theta\)) [degrees]</label>
            <input type="number" id="w-angle" class="form-control" value="0" step="any" min="0" max="360">
            <small style="color: var(--text-muted, #6c757d);">0&deg; = Parallel in direction of motion, 90&deg; = Perpendicular (Zero work)</small>
          </div>

          <div class="input-group">
            <label for="w-time">Elapsed Time (\(t\)) [seconds]</label>
            <input type="number" id="w-time" class="form-control" value="5.0" step="any" min="0.001">
            <small style="color: var(--text-muted, #6c757d);">Used to solve continuous power</small>
          </div>
        </div>
      </div>

      <!-- Mode 2: Power from Work & Time -->
      <div id="panel-pw-time" style="display: none;">
        <div class="input-grid">
          <div class="input-group">
            <label for="pt-work">Total Work Done (\(W\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="pt-work" class="form-control" value="75000" step="any" min="0" style="flex: 2;">
              <select id="pt-unit-work" class="form-control" style="flex: 1;" onchange="calculateWP()">
                <option value="J" selected>Joules (J)</option>
                <option value="kJ">kJ</option>
                <option value="MJ">MJ</option>
                <option value="ft_lbf">ft&middot;lbf</option>
                <option value="kWh">kWh</option>
              </select>
            </div>
          </div>

          <div class="input-group">
            <label for="pt-time">Elapsed Duration (\(t\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="pt-time" class="form-control" value="12" step="any" min="0.001" style="flex: 2;">
              <select id="pt-unit-time" class="form-control" style="flex: 1;" onchange="calculateWP()">
                <option value="s" selected>seconds (s)</option>
                <option value="min">minutes (min)</option>
                <option value="hr">hours (hr)</option>
              </select>
            </div>
          </div>
        </div>
      </div>

      <!-- Mode 3: Power from Force & Velocity -->
      <div id="panel-pw-vel" style="display: none;">
        <div class="input-grid">
          <div class="input-group">
            <label for="pv-force">Driving Force (\(F\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="pv-force" class="form-control" value="3200" step="any" min="0" style="flex: 2;">
              <select id="pv-unit-force" class="form-control" style="flex: 1;" onchange="calculateWP()">
                <option value="N" selected>N</option>
                <option value="kN">kN</option>
                <option value="lbf">lbf</option>
              </select>
            </div>
          </div>

          <div class="input-group">
            <label for="pv-vel">Linear Velocity (\(v\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="pv-vel" class="form-control" value="22" step="any" min="0" style="flex: 2;">
              <select id="pv-unit-vel" class="form-control" style="flex: 1;" onchange="calculateWP()">
                <option value="m_s" selected>m/s</option>
                <option value="km_h">km/h</option>
                <option value="mph">mph</option>
              </select>
            </div>
          </div>
        </div>
      </div>

      <div class="btn-group">
        <button type="button" class="btn btn-primary" onclick="calculateWP()">Calculate Work &amp; Power</button>
        <button type="button" class="btn btn-secondary" onclick="resetWP()">Reset Defaults</button>
      </div>

      <!-- Results Display Grid -->
      <div class="results-grid" style="margin-top: 1.5rem;">
        <div class="result-card primary-result">
          <div class="result-label" id="res-primary-label">Mechanical Work Done (\(W\))</div>
          <div class="result-value" id="res-primary-val">37.50 kJ</div>
          <div class="result-subtext" id="res-primary-sub">37,500.00 Joules (N&middot;m)</div>
        </div>

        <div class="result-card">
          <div class="result-label">Continuous Power Delivery</div>
          <div class="result-value" id="res-power-w">7,500.0 W</div>
          <div class="result-subtext" id="res-power-kw">7.500 kW (Kilowatts)</div>
        </div>

        <div class="result-card">
          <div class="result-label">Mechanical Horsepower</div>
          <div class="result-value" id="res-hp">10.06 HP</div>
          <div class="result-subtext" id="res-hp-metric">10.20 Metric HP (PS)</div>
        </div>

        <div class="result-card">
          <div class="result-label">Imperial Work &amp; Torque</div>
          <div class="result-value" id="res-imp-w">27,659 ft&middot;lbf</div>
          <div class="result-subtext">5,531.7 ft&middot;lbf/s</div>
        </div>
      </div>

      <!-- Equivalent Units Table Card -->
      <div class="info-card" style="margin-top: 1.5rem;">
        <h3>Equivalent Multi-System Power Ratings</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 0.75rem; margin-top: 0.5rem;">
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">Watts (W)</div>
            <strong id="eq-w">7,500 W</strong>
          </div>
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">Kilowatts (kW)</div>
            <strong id="eq-kw">7.500 kW</strong>
          </div>
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">BTU per hour (BTU/hr)</div>
            <strong id="eq-btuhr">25,591 BTU/hr</strong>
          </div>
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">Calories / sec (cal/s)</div>
            <strong id="eq-cals">1,792.5 cal/s</strong>
          </div>
        </div>
      </div>

      <!-- Step-by-step Math Breakdown Card -->
      <div class="info-card" style="margin-top: 1.5rem;">
        <h3>Step-by-Step Physics &amp; Dimensional Derivation</h3>
        <pre id="res-steps" style="white-space: pre-wrap; font-family: monospace; background: var(--bg-secondary, #f8f9fa); padding: 1rem; border-radius: 6px; font-size: 0.9rem; line-height: 1.5; color: var(--text-primary, #212529);"></pre>
      </div>
    </div>

    <!-- Article Content: 1000+ Words Clinical / Engineering Deep Dive -->
    <article class="article-body">
      <h2>The Physical Foundations of Mechanical Work and Rate of Power Delivery</h2>
      <p>
        In classical Newtonian mechanics, thermodynamics, and electrical engineering, <strong>work</strong> (\(W\)) and <strong>power</strong> (\(P\)) are the two fundamental scalar quantities that govern the transfer and transformation of energy. Work quantifies the cumulative amount of mechanical energy transferred into or out of a physical system when a force causes displacement. Power quantifies the temporal rapidity—the exact rate per unit of time—at which that work is executed.
      </p>
      <p>
        Distinguishing between total energy transferred (work) and the rate of energy transfer (power) is essential across industrial design and technology: an electric vehicle motor and a tiny household toy motor might both perform an identical 100 kilojoules of work to elevate an identical load; however, the automotive motor delivers this work in 1 second (operating at 100 kilowatts of power), whereas the toy motor requires 1,000 seconds (operating at only 100 watts).
      </p>

      <h2>Mathematical Formulations and Governing Laws</h2>

      <h3>1. Mechanical Work in One and Three Dimensions</h3>
      <p>
        When a constant force vector \(\vec{F}\) acts upon a physical particle while it undergoes a linear displacement vector \(\vec{d}\), the mechanical work performed is mathematically defined as the scalar dot product of the two vectors:
      </p>
      $$W = \vec{F} \cdot \vec{d} = |\vec{F}| |\vec{d}| \cos(\theta)$$
      <p>
        Where:
      </p>
      <ul>
        <li>\(W\) is mechanical work in Joules (\(\text{J} = \text{N}\cdot\text{m}\)).</li>
        <li>\(F\) is the magnitude of the applied force in Newtons (\(\text{N}\)).</li>
        <li>\(d\) is the magnitude of net displacement in meters (\(\text{m}\)).</li>
        <li>\(\theta\) is the spatial angle between the force direction vector and the displacement vector.</li>
      </ul>

      <h3>Geometric Regimes of the Dot Product Angle \(\theta\)</h3>
      <ul>
        <li><strong>Parallel Force (\(\theta = 0^\circ, \cos(0^\circ) = +1\)):</strong> Maximum positive work (\(W = +F d\)). Force actively accelerates the body in the direction of travel, adding kinetic energy.</li>
        <li><strong>Perpendicular Force (\(\theta = 90^\circ, \cos(90^\circ) = 0\)):</strong> Zero work (\(W = 0\)). No energy is transferred. For example, centripetal force holding a satellite in circular orbit acts strictly perpendicular to the orbital path, doing exactly zero work and leaving orbital kinetic energy invariant.</li>
        <li><strong>Opposing Force (\(\theta = 180^\circ, \cos(180^\circ) = -1\)):</strong> Maximum negative work (\(W = -F d\)). Force opposes motion, extracting kinetic energy from the object (e.g., kinetic friction, automotive braking).</li>
      </ul>

      <h3>2. Power: The Temporal Rate of Energy Expenditure</h3>
      <p>
        Average power is defined as the total work executed divided by the elapsed time duration:
      </p>
      $$P_{\text{avg}} = \frac{W}{\Delta t}$$
      <p>
        For continuous processes where a constant force drives an object at steady velocity \(\vec{v}\):
      </p>
      $$P = \frac{\vec{F} \cdot \Delta\vec{d}}{\Delta t} = \vec{F} \cdot \left(\frac{\Delta\vec{d}}{\Delta t}\right) = \vec{F} \cdot \vec{v} = F v \cos(\theta)$$
      <p>
        In SI units, power is measured in <strong>Watts (\(\text{W}\))</strong>, named after Scottish engineer James Watt. One Watt equals one Joule of energy delivered per second (\(1\text{ W} = 1\text{ J/s}\)).
      </p>

      <h3>3. Rotational Work and Shaft Power</h3>
      <p>
        In rotating machinery (turbines, crankshafts, electric motors), work is executed by an applied rotational torque \(\tau\) rotating through an angular displacement \(\theta\) (in radians):
      </p>
      $$W = \tau \times \theta$$
      <p>
        Rotational power delivery is the product of shaft torque and rotational angular velocity \(\omega\) (in radians per second):
      </p>
      $$P = \tau \times \omega = \tau \times \left( \frac{2\pi \times N}{60} \right) = \frac{2\pi N \tau}{60}$$
      <p>
        Where \(N\) is rotational speed in revolutions per minute (RPM).
      </p>

      <h2>International Power Units and Conversion Standards</h2>
      <p>
        The table below provides exact conversions between SI metric Watts, electrical kilowatts, imperial horsepower, and thermal heating units.
      </p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Power Unit</th>
            <th>Symbol</th>
            <th>Value in Watts (W)</th>
            <th>Value in Horsepower (HP)</th>
            <th>Primary Application Context</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Watt (SI Coherent Derived)</td>
            <td>W</td>
            <td>1.0 (Exact)</td>
            <td>0.00134102</td>
            <td>Electronics, LED lighting, physics research</td>
          </tr>
          <tr>
            <td>Kilowatt</td>
            <td>kW</td>
            <td>1,000</td>
            <td>1.341022</td>
            <td>EV motors, residential electrical services</td>
          </tr>
          <tr>
            <td>Megawatt</td>
            <td>MW</td>
            <td>1,000,000</td>
            <td>1,341.02</td>
            <td>Power generation stations, utility grids</td>
          </tr>
          <tr>
            <td>Mechanical Horsepower (Imperial)</td>
            <td>HP</td>
            <td>745.699872</td>
            <td>1.0 (Exact)</td>
            <td>Internal combustion engines, industrial pumps</td>
          </tr>
          <tr>
            <td>Metric Horsepower (Pferdestärke)</td>
            <td>PS / cv</td>
            <td>735.49875</td>
            <td>0.986320</td>
            <td>European automotive power ratings (DIN 66036)</td>
          </tr>
          <tr>
            <td>Foot-Pound per Second</td>
            <td>\(\text{ft}\cdot\text{lbf/s}\)</td>
            <td>1.355818</td>
            <td>0.00181818</td>
            <td>Classical imperial mechanical dynamics</td>
          </tr>
          <tr>
            <td>BTU per Hour</td>
            <td>BTU/hr</td>
            <td>0.293071</td>
            <td>0.00039301</td>
            <td>HVAC air conditioning cooling and furnace heating</td>
          </tr>
          <tr>
            <td>Ton of Refrigeration</td>
            <td>TR</td>
            <td>3,516.853</td>
            <td>4.71618</td>
            <td>Commercial chiller sizing (12,000 BTU/hr)</td>
          </tr>
        </tbody>
      </table>

      <h2>Benchmark Power Levels Across the Physical Universe</h2>
      <p>
        To conceptualize energy transfer rates across biological, technological, and astrophysical scales:
      </p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Physical Entity / System</th>
            <th>Approximate Power (Watts)</th>
            <th>Description &amp; Engineering Significance</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Human Brain Basal Metabolic Rate</td>
            <td>\(20\text{ W}\)</td>
            <td>Resting neural ionic pump homeostasis</td>
          </tr>
          <tr>
            <td>Human Body at Rest (BMR)</td>
            <td>\(80 &ndash; 100\text{ W}\)</td>
            <td>Metabolic heat output of sedentary adult</td>
          </tr>
          <tr>
            <td>Tour de France Cyclist Peak Sprint</td>
            <td>\(1,200 &ndash; 1,600\text{ W}\) (1.6 &ndash; 2.1 HP)</td>
            <td>Maximum anaerobic lactic power expenditure</td>
          </tr>
          <tr>
            <td>Household Microwave Oven</td>
            <td>\(1,000 &ndash; 1,500\text{ W}\) (1.0 &ndash; 1.5 kW)</td>
            <td>High-frequency 2.45 GHz magnetron radiation</td>
          </tr>
          <tr>
            <td>Tesla Model S Plaid Electric Drive</td>
            <td>\(760,000\text{ W}\) (760 kW / 1,020 HP)</td>
            <td>Tri-motor carbon-sleeved rotor output</td>
          </tr>
          <tr>
            <td>General Electric GE90 Jet Engine</td>
            <td>\(75,000,000\text{ W}\) (75 MW / 100,000 HP)</td>
            <td>Boeing 777 cruise gas turbine shaft output</td>
          </tr>
          <tr>
            <td>Hoover Hydroelectric Dam</td>
            <td>\(2.08 \times 10^9\text{ W}\) (2,080 MW / 2.08 GW)</td>
            <td>17 hydraulic Francis turbines in generation</td>
          </tr>
          <tr>
            <td>Solar Radiation Intercepted by Earth</td>
            <td>\(1.74 \times 10^{17}\text{ W}\) (174 Petawatts)</td>
            <td>Top-of-atmosphere total solar irradiance</td>
          </tr>
        </tbody>
      </table>

      <h2>Practical Real-World Engineering Case Studies</h2>

      <div class="worked-example-card">
        <h3>Case Study 1: Industrial Crane Hoist Motor Sizing &amp; Electrical Efficiency</h3>
        <p><strong>Scenario:</strong> A shipyard gantry crane hoists a loaded shipping container of gross mass \(m = 32,000\text{ kg}\) (32 metric tons) vertically through a height of \(h = 24.0\text{ m}\) at a steady hoist speed of \(v = 0.40\text{ m/s}\). The mechanical gear transmission has an efficiency of \(\eta_{\text{mech}} = 88\%\), and the electric induction drive motor has an efficiency of \(\eta_{\text{elec}} = 94\%\). Local gravity is \(g = 9.80665\text{ m/s}^2\).</p>
        <p><strong>Objective:</strong> Compute the net mechanical work done on the container, the net lifting power requirement, and the gross electrical line power (in kW and HP) drawn from the substation grid.</p>
        <div class="step-solution">
          <p><strong>1. Net Mechanical Work:</strong></p>
          $$W = m g h = 32,000\text{ kg} \times 9.80665\text{ m/s}^2 \times 24.0\text{ m} \approx 7,531,507\text{ Joules} \approx 7.532\text{ MJ} \ (2.092\text{ kWh})$$
          <p><strong>2. Net Mechanical Lifting Power:</strong></p>
          $$P_{\text{net}} = F \times v = (m g) \times v = (32,000 \times 9.80665) \times 0.40\text{ m/s} = 313,813\text{ N} \times 0.40 = 125,525\text{ W} \approx 125.53\text{ kW}$$
          <p><strong>3. Gross Electrical Line Power Input:</strong></p>
          $$\eta_{\text{total}} = \eta_{\text{mech}} \times \eta_{\text{elec}} = 0.88 \times 0.94 \approx 0.8272 \ (82.72\%)$$
          $$P_{\text{electrical}} = \frac{P_{\text{net}}}{\eta_{\text{total}}} = \frac{125.525\text{ kW}}{0.8272} \approx 151.75\text{ kW}$$
          $$\text{Motor Horsepower Rating} = \frac{151,750\text{ W}}{745.7\text{ W/HP}} \approx 203.5\text{ HP}$$
          <p>The electrical engineer specifies a standard 250 HP (185 kW) heavy-duty industrial hoist motor to ensure adequate thermal margin.</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Automotive Highway Cruise Aerodynamic Power Demand</h3>
        <p><strong>Scenario:</strong> A passenger vehicle travels on a level highway at a constant cruise speed of \(v = 120\text{ km/h}\) (\(33.33\text{ m/s}\) / 74.6 mph). Total vehicle mass is \(m = 1,700\text{ kg}\). Rolling resistance force is \(F_{\text{roll}} = 220\text{ N}\). The frontal area is \(A = 2.30\text{ m}^2\) with drag coefficient \(C_d = 0.28\). Ambient air density is \(\rho = 1.20\text{ kg/m}^3\).</p>
        <p><strong>Objective:</strong> Calculate aerodynamic drag force, total resisting force, and required mechanical wheel power to maintain steady speed.</p>
        <div class="step-solution">
          <p><strong>1. Aerodynamic Drag Force:</strong></p>
          $$F_{\text{drag}} = \frac{1}{2} \rho v^2 C_d A = \frac{1}{2} (1.20\text{ kg/m}^3) \times (33.33\text{ m/s})^2 \times 0.28 \times 2.30\text{ m}^2$$
          $$F_{\text{drag}} = 0.60 \times 1,111.1 \times 0.0644 = 429.3\text{ N}$$
          <p><strong>2. Total Resistive Traction Force:</strong></p>
          $$F_{\text{total}} = F_{\text{drag}} + F_{\text{roll}} = 429.3\text{ N} + 220.0\text{ N} = 649.3\text{ N}$$
          <p><strong>3. Mechanical Wheel Power Requirement:</strong></p>
          $$P = F_{\text{total}} \times v = 649.3\text{ N} \times 33.33\text{ m/s} = 21,641\text{ W} \approx 21.64\text{ kW}$$
          $$\text{Horsepower} = \frac{21,641\text{ W}}{745.7} \approx 29.02\text{ HP}$$
          <p>Notice that power required to overcome air resistance scales with velocity cubed (\(P_{\text{drag}} \propto v^3\)): accelerating from 120 km/h to 150 km/h increases aerodynamic power demand by nearly 95%!</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 3: Hydropower Pelton Turbine Jet Kinetic Power Extraction</h3>
        <p><strong>Scenario:</strong> A high-head alpine hydroelectric facility uses a Pelton impulse water turbine fed by a penstock nozzle discharging a water jet of volumetric flow rate \(Q = 2.40\text{ m}^3/\text{s}\) at jet velocity \(v = 85.0\text{ m/s}\). Water density is \(\rho = 1,000\text{ kg/m}^3\).</p>
        <p><strong>Objective:</strong> Compute the kinetic energy flux (kinetic power) delivered by the high-velocity water jet.</p>
        <div class="step-solution">
          <p><strong>1. Mass Flow Rate:</strong></p>
          $$\dot{m} = \rho \times Q = 1,000\text{ kg/m}^3 \times 2.40\text{ m}^3/\text{s} = 2,400\text{ kg/s}$$
          <p><strong>2. Jet Kinetic Power Delivery:</strong></p>
          $$P = \frac{1}{2} \dot{m} v^2 = \frac{1}{2} \times 2,400\text{ kg/s} \times (85.0\text{ m/s})^2 = 1,200 \times 7,225 = 8,670,000\text{ Watts} = 8.67\text{ MW}$$
          $$\text{Turbine Mechanical HP} = \frac{8,670,000\text{ W}}{745.7\text{ W/HP}} \approx 11,626.7\text{ HP}$$
          <p>The high-pressure Pelton turbine buckets extract up to 90% of this 8.67 MW of kinetic jet power, converting it into rotational electricity.</p>
        </div>
      </div>

      <h2>Frequently Asked Questions</h2>
      <div class="faq-accordion">
        <details class="faq-item">
          <summary class="faq-question">What is the difference between instantaneous power and average power?</summary>
          <div class="faq-answer">
            <p>Average power divides total work performed by gross elapsed time: \(P_{\text{avg}} = \Delta W / \Delta t\). Instantaneous power represents the exact power delivery at one infinitesimal moment in time, defined mathematically as the first derivative of work with respect to time: \(P(t) = dW / dt = \vec{F} \cdot \vec{v}\). In machinery with fluctuating torque or stroke cycles, instantaneous power fluctuates around the mean average power.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">Why did James Watt define horsepower using a draft pony?</summary>
          <div class="faq-answer">
            <p>In 1782, James Watt was marketing his revolutionary steam engine to coal mine owners who used pit ponies to turn winches. To prove the commercial value of his engines, Watt estimated that a strong draft horse could turn a 12-foot radius mill wheel 144 times per hour, exerting a pulling force of 180 pounds. Rounding up conservatively to ensure his engines would exceed customer expectations, Watt defined 1 Horsepower as 33,000 foot-pounds per minute (550 ft·lbf/s, or ~746 Watts).</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">How does mechanical work relate to the Work-Energy Theorem?</summary>
          <div class="faq-answer">
            <p>The Work-Energy Theorem states that the net work performed by all forces acting upon a rigid body equals the exact change in its translational kinetic energy: \(W_{\text{net}} = \Delta E_k = \frac{1}{2} m v_f^2 - \frac{1}{2} m v_i^2\). If positive net work is done on an object, its speed increases; if negative net work is done (such as by friction or braking), its speed decreases.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">Why does aerodynamic power scale with the cube of speed?</summary>
          <div class="faq-answer">
            <p>Aerodynamic drag force is proportional to velocity squared (\(F_{\text{drag}} \propto v^2\)) because an object moving twice as fast collides with twice as many air molecules per second, and impacts each molecule with twice the velocity. Because power equals force multiplied by velocity (\(P = F \times v\)), aerodynamic power scales with velocity cubed: \(P_{\text{drag}} \propto v^2 \times v = v^3\). Doubling travel speed requires an eight-fold increase in engine power!</p>
          </div>
        </details>
      </div>

      <!-- Cross-Disciplinary Internal Links -->
      <div class="related-calculators" style="margin-top: 2rem; padding: 1.5rem; background: var(--bg-secondary, #f8f9fa); border-radius: 8px;">
        <h3>Related Engineering &amp; Physics Calculators</h3>
        <ul style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.75rem; list-style: none; padding: 0;">
          <li><a href="potential-energy-calculator.html">&rarr; Potential Energy Calculator (U = mgh)</a></li>
          <li><a href="kinetic-energy-calculator.html">&rarr; Kinetic Energy Calculator (Ek = 0.5mv²)</a></li>
          <li><a href="force-calculator.html">&rarr; Force &amp; Newton's Second Law Solver (F = ma)</a></li>
          <li><a href="speed-calculator.html">&rarr; Speed &amp; Kinematics Calculator (v = d/t)</a></li>
          <li><a href="torque-calculator.html">&rarr; Torque &amp; Shaft Power Calculator</a></li>
          <li><a href="power-converter.html">&rarr; Universal Power Unit Converter</a></li>
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
      'lbf': 4.448221615
    };

    var DIST_FACTORS = {
      'm': 1.0,
      'ft': 0.3048,
      'km': 1000.0
    };

    var WORK_FACTORS = {
      'J': 1.0,
      'kJ': 1000.0,
      'MJ': 1000000.0,
      'ft_lbf': 1.355818,
      'kWh': 3600000.0
    };

    var TIME_FACTORS = {
      's': 1.0,
      'min': 60.0,
      'hr': 3600.0
    };

    var VEL_FACTORS = {
      'm_s': 1.0,
      'km_h': 0.277777778,
      'mph': 0.44704
    };

    function switchWPMode() {
      var mode = document.getElementById('wp-mode').value;
      document.getElementById('panel-work').style.display = (mode === 'work-linear') ? 'block' : 'none';
      document.getElementById('panel-pw-time').style.display = (mode === 'power-time') ? 'block' : 'none';
      document.getElementById('panel-pw-vel').style.display = (mode === 'power-velocity') ? 'block' : 'none';

      var lbl = document.getElementById('res-primary-label');
      if (mode === 'work-linear') {
        lbl.innerText = "Mechanical Work Done (W)";
      } else {
        lbl.innerText = "Calculated Work Done (W)";
      }

      calculateWP();
    }

    function calculateWP() {
      var mode = document.getElementById('wp-mode').value;
      var w_J = 0, p_W = 0;
      var steps = "";

      if (mode === 'work-linear') {
        var fVal = parseFloat(document.getElementById('w-force').value);
        var fUnit = document.getElementById('w-unit-force').value;
        var dVal = parseFloat(document.getElementById('w-dist').value);
        var dUnit = document.getElementById('w-unit-dist').value;
        var deg = parseFloat(document.getElementById('w-angle').value);
        var tSec = parseFloat(document.getElementById('w-time').value);

        if (isNaN(fVal) || isNaN(dVal) || isNaN(deg) || isNaN(tSec) || fVal < 0 || dVal < 0 || tSec <= 0) {
          showError("Force, distance, and duration must be non-negative real numbers.");
          return;
        }

        var fN = fVal * FORCE_FACTORS[fUnit];
        var dM = dVal * DIST_FACTORS[dUnit];
        var rad = deg * (Math.PI / 180.0);
        var cosVal = Math.cos(rad);

        w_J = fN * dM * cosVal;
        p_W = w_J / tSec;

        steps = "Mode: Linear Mechanical Work (W = F * d * cos θ)\n" +
                "Inputs: F = " + fVal + " " + fUnit + ", d = " + dVal + " " + dUnit + ", θ = " + deg + "°, t = " + tSec + " s\n\n" +
                "1. Force in SI: F = " + fN.toFixed(2) + " N\n" +
                "2. Distance in SI: d = " + dM.toFixed(2) + " m\n" +
                "3. cos(" + deg + "°) = " + cosVal.toFixed(4) + "\n\n" +
                "4. Compute Work: W = F * d * cos θ = " + fN.toFixed(2) + " * " + dM.toFixed(2) + " * " + cosVal.toFixed(4) + "\n" +
                "   W = " + w_J.toFixed(2) + " Joules (" + (w_J / 1000).toFixed(3) + " kJ, " + (w_J / 1.355818).toFixed(1) + " ft·lbf)\n\n" +
                "5. Continuous Power: P = W / t = " + w_J.toFixed(2) + " / " + tSec + " = " + p_W.toFixed(2) + " Watts (" + (p_W / 1000).toFixed(3) + " kW, " + (p_W / 745.7).toFixed(2) + " HP)";

      } else if (mode === 'power-time') {
        var wVal = parseFloat(document.getElementById('pt-work').value);
        var wUnit = document.getElementById('pt-unit-work').value;
        var tVal = parseFloat(document.getElementById('pt-time').value);
        var tUnit = document.getElementById('pt-unit-time').value;

        if (isNaN(wVal) || isNaN(tVal) || wVal < 0 || tVal <= 0) {
          showError("Work must be positive and duration must be greater than zero.");
          return;
        }

        w_J = wVal * WORK_FACTORS[wUnit];
        var tS = tVal * TIME_FACTORS[tUnit];
        p_W = w_J / tS;

        steps = "Mode: Power from Work & Duration (P = W / t)\n" +
                "Inputs: W = " + wVal + " " + wUnit.replace('_', '·') + ", t = " + tVal + " " + tUnit + "\n\n" +
                "1. Work in SI: W = " + w_J.toFixed(2) + " Joules\n" +
                "2. Duration in SI: t = " + tS.toFixed(2) + " seconds\n\n" +
                "3. Compute Power: P = W / t = " + w_J.toFixed(2) + " / " + tS.toFixed(2) + "\n" +
                "   P = " + p_W.toFixed(2) + " Watts (" + (p_W / 1000).toFixed(4) + " kW, " + (p_W / 745.7).toFixed(2) + " HP)";

      } else if (mode === 'power-velocity') {
        var fvForce = parseFloat(document.getElementById('pv-force').value);
        var fvUnitF = document.getElementById('pv-unit-force').value;
        var fvVel = parseFloat(document.getElementById('pv-vel').value);
        var fvUnitV = document.getElementById('pv-unit-vel').value;

        if (isNaN(fvForce) || isNaN(fvVel) || fvForce < 0 || fvVel < 0) {
          showError("Force and velocity must be non-negative.");
          return;
        }

        var fN2 = fvForce * FORCE_FACTORS[fvUnitF];
        var vMS2 = fvVel * VEL_FACTORS[fvUnitV];
        p_W = fN2 * vMS2;
        w_J = p_W * 1.0; // Work per 1 second

        steps = "Mode: Power from Force & Velocity (P = F * v)\n" +
                "Inputs: Force F = " + fvForce + " " + fvUnitF + ", Velocity v = " + fvVel + " " + fvUnitV.replace('_', '/') + "\n\n" +
                "1. Force in SI: F = " + fN2.toFixed(2) + " N\n" +
                "2. Velocity in SI: v = " + vMS2.toFixed(4) + " m/s\n\n" +
                "3. Compute Power: P = F * v = " + fN2.toFixed(2) + " * " + vMS2.toFixed(4) + "\n" +
                "   P = " + p_W.toFixed(2) + " Watts (" + (p_W / 1000).toFixed(4) + " kW, " + (p_W / 745.7).toFixed(2) + " HP)\n" +
                "   Work per second: W = " + p_W.toFixed(2) + " Joules/second";
      }

      var wKj = w_J / 1000.0;
      var pKw = p_W / 1000.0;
      var pHP = p_W / 745.699872;
      var pPS = p_W / 735.49875;
      var ftlbf = w_J / 1.355818;
      var btuhr = p_W * 3.412142;
      var cals = p_W / 4.184;

      document.getElementById('res-primary-val').innerText = (Math.abs(wKj) >= 1000) ? (wKj / 1000).toFixed(3) + " MJ" : wKj.toFixed(2) + " kJ";
      document.getElementById('res-primary-sub').innerText = w_J.toLocaleString(undefined, {maximumFractionDigits: 1}) + " Joules (N·m)";
      document.getElementById('res-power-w').innerText = p_W.toLocaleString(undefined, {maximumFractionDigits: 1}) + " W";
      document.getElementById('res-power-kw').innerText = pKw.toFixed(3) + " kW (Kilowatts)";
      document.getElementById('res-hp').innerText = pHP.toFixed(2) + " HP";
      document.getElementById('res-hp-metric').innerText = pPS.toFixed(2) + " Metric HP (PS)";
      document.getElementById('res-imp-w').innerText = Math.round(ftlbf).toLocaleString() + " ft·lbf";

      document.getElementById('eq-w').innerText = p_W.toLocaleString(undefined, {maximumFractionDigits: 1}) + " W";
      document.getElementById('eq-kw').innerText = pKw.toFixed(3) + " kW";
      document.getElementById('eq-btuhr').innerText = Math.round(btuhr).toLocaleString() + " BTU/hr";
      document.getElementById('eq-cals').innerText = cals.toFixed(1) + " cal/s";

      document.getElementById('res-steps').innerText = steps;
    }

    function showError(msg) {
      document.getElementById('res-primary-val').innerText = "Error";
      document.getElementById('res-primary-sub').innerText = "Invalid calculation";
      document.getElementById('res-power-w').innerText = "N/A";
      document.getElementById('res-power-kw').innerText = "N/A";
      document.getElementById('res-hp').innerText = "N/A";
      document.getElementById('res-hp-metric').innerText = "N/A";
      document.getElementById('res-imp-w').innerText = "N/A";
      document.getElementById('res-steps').innerText = "Error: " + msg;
    }

    function resetWP() {
      document.getElementById('wp-mode').value = 'work-linear';
      document.getElementById('w-force').value = '2500';
      document.getElementById('w-unit-force').value = 'N';
      document.getElementById('w-dist').value = '15';
      document.getElementById('w-unit-dist').value = 'm';
      document.getElementById('w-angle').value = '0';
      document.getElementById('w-time').value = '5.0';
      document.getElementById('pt-work').value = '75000';
      document.getElementById('pt-unit-work').value = 'J';
      document.getElementById('pt-time').value = '12';
      document.getElementById('pt-unit-time').value = 's';
      document.getElementById('pv-force').value = '3200';
      document.getElementById('pv-unit-force').value = 'N';
      document.getElementById('pv-vel').value = '22';
      document.getElementById('pv-unit-vel').value = 'm_s';
      switchWPMode();
    }

    window.addEventListener('DOMContentLoaded', function() {
      calculateWP();
    });
  </script>
</body>
</html>
"""

# 6. stress-strain-calculator.html
HTML_STRESS_STRAIN = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Stress and Strain Calculator - Hooke's Law &amp; Young's Modulus (σ = Eε)</title>
  <meta name="description" content="Calculate tensile and compressive stress (σ = F/A), engineering strain (ε = ΔL/L0), Young's modulus (E = σ/ε), and safety factors with material presets and step-by-step proofs.">
  <link rel="canonical" href="https://calchub.org/stress-strain-calculator.html">
  <meta property="og:title" content="Stress and Strain Calculator - Solid Mechanics &amp; Young's Modulus Solver">
  <meta property="og:description" content="Free engineering stress-strain calculator. Compute normal stress σ = F/A, strain ε = ΔL/L, Hooke's Law, shear stress, and safety factor across steel, aluminum, and titanium.">
  <meta property="og:url" content="https://calchub.org/stress-strain-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Stress &amp; Strain Calculator - Solid Mechanics Tool">
  <meta name="twitter:description" content="Solve normal stress, strain, Young's modulus, and safety factor with material presets and full engineering case studies.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Stress and Strain Calculator",
    "url": "https://calchub.org/stress-strain-calculator.html",
    "description": "Calculates normal mechanical stress, engineering strain, Young's modulus of elasticity, and design safety factors across structural engineering materials.",
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
        "name": "What is the difference between stress and strain?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Stress (σ) is the internal mechanical resistive force distributed over an area: σ = F / A, measured in Pascals (N/m²) or psi. Strain (ε) is the resulting dimensionless geometric deformation or fractional change in length: ε = ΔL / L0."
        }
      },
      {
        "@type": "Question",
        "name": "What is Hooke's Law for elastic solids?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Within the linear elastic limit of a material, stress is directly proportional to strain: σ = E * ε, where E is Young's Modulus of Elasticity (measured in Gigapascals, GPa, or psi)."
        }
      },
      {
        "@type": "Question",
        "name": "What is a structural Safety Factor (SF)?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The structural Safety Factor (SF) is the ratio of a material's structural strength capacity to the maximum anticipated operating stress: SF = σ_yield / σ_operating. An SF > 1 indicates that the structure operates safely below permanent plastic deformation."
        }
      },
      {
        "@type": "Question",
        "name": "What is Poisson's Ratio in solid mechanics?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Poisson's Ratio (ν) is the negative ratio of transverse lateral strain to axial longitudinal strain: ν = -ε_transverse / ε_axial. For most structural metals, Poisson's ratio ranges between 0.25 and 0.35."
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
      <div class="calc-icon" aria-hidden="true">&#128295;</div>
      <h1>Stress and Strain Calculator</h1>
      <p class="calc-description">Compute mechanical stress (\(\sigma = F/A\)), engineering strain (\(\varepsilon = \Delta L/L_0\)), Young's modulus, and structural safety factors with material presets.</p>
    </div>

    <div class="calculator-body">
      <div class="input-grid">
        <div class="input-group">
          <label for="ss-mode">Variable to Calculate</label>
          <select id="ss-mode" class="form-control" onchange="switchSSMode()">
            <option value="stress" selected>Normal Stress (\(\sigma = F / A\)) &amp; Strain (\(\varepsilon\))</option>
            <option value="deformation">Deformation Elongation (\(\Delta L = \frac{F L_0}{E A}\))</option>
            <option value="youngs">Young's Modulus (\(E = \sigma / \varepsilon\))</option>
          </select>
        </div>

        <div class="input-group">
          <label for="material-preset">Load Material Preset</label>
          <select id="material-preset" class="form-control" onchange="loadMaterialPreset()">
            <option value="custom" selected>-- Custom Material Properties --</option>
            <option value="200,250">Structural Steel (A36) &ndash; E: 200 GPa, Yield: 250 MPa</option>
            <option value="69,276">Aluminum (6061-T6) &ndash; E: 69 GPa, Yield: 276 MPa</option>
            <option value="114,880">Titanium (Ti-6Al-4V) &ndash; E: 114 GPa, Yield: 880 MPa</option>
            <option value="117,70">Copper (C11000) &ndash; E: 117 GPa, Yield: 70 MPa</option>
            <option value="25,28">Structural Concrete &ndash; E: 25 GPa, Compressive: 28 MPa</option>
            <option value="150,1500">Carbon Fiber (CFRP) &ndash; E: 150 GPa, Tensile: 1500 MPa</option>
          </select>
        </div>
      </div>

      <!-- Inputs Grid -->
      <div class="input-grid">
        <div class="input-group">
          <label for="ss-force">Axial Load / Force (\(F\))</label>
          <div style="display: flex; gap: 0.5rem;">
            <input type="number" id="ss-force" class="form-control" value="85" step="any" min="0" style="flex: 2;">
            <select id="ss-unit-f" class="form-control" style="flex: 1;" onchange="calculateSS()">
              <option value="kN" selected>kN</option>
              <option value="N">N</option>
              <option value="lbf">lbf</option>
              <option value="kip">kips</option>
            </select>
          </div>
        </div>

        <div class="input-group">
          <label for="ss-area">Cross-Sectional Area (\(A\))</label>
          <div style="display: flex; gap: 0.5rem;">
            <input type="number" id="ss-area" class="form-control" value="650" step="any" min="0.0001" style="flex: 2;">
            <select id="ss-unit-a" class="form-control" style="flex: 1;" onchange="calculateSS()">
              <option value="mm2" selected>mm²</option>
              <option value="cm2">cm²</option>
              <option value="m2">m²</option>
              <option value="in2">in²</option>
            </select>
          </div>
        </div>
      </div>

      <div class="input-grid">
        <div class="input-group">
          <label for="ss-l0">Original Member Length (\(L_0\))</label>
          <div style="display: flex; gap: 0.5rem;">
            <input type="number" id="ss-l0" class="form-control" value="2.5" step="any" min="0.001" style="flex: 2;">
            <select id="ss-unit-l" class="form-control" style="flex: 1;" onchange="calculateSS()">
              <option value="m" selected>m</option>
              <option value="mm">mm</option>
              <option value="in">in</option>
              <option value="ft">ft</option>
            </select>
          </div>
        </div>

        <div class="input-group">
          <label for="ss-e">Young's Modulus of Elasticity (\(E\))</label>
          <div style="display: flex; gap: 0.5rem;">
            <input type="number" id="ss-e" class="form-control" value="200" step="any" min="0.01" style="flex: 2;">
            <select id="ss-unit-e" class="form-control" style="flex: 1;" onchange="calculateSS()">
              <option value="GPa" selected>GPa</option>
              <option value="MPa">MPa</option>
              <option value="psi">psi</option>
              <option value="ksi">ksi</option>
            </select>
          </div>
        </div>
      </div>

      <div class="input-group">
        <label for="ss-yield">Material Yield Strength (\(\sigma_{\text{yield}}\)) [MPa] (For Safety Factor)</label>
        <input type="number" id="ss-yield" class="form-control" value="250" step="any" min="0">
        <small style="color: var(--text-muted, #6c757d);">e.g. 250 MPa for A36 steel, 276 MPa for 6061-T6 aluminum</small>
      </div>

      <div class="btn-group">
        <button type="button" class="btn btn-primary" onclick="calculateSS()">Compute Solid Mechanics</button>
        <button type="button" class="btn btn-secondary" onclick="resetSS()">Reset Defaults</button>
      </div>

      <!-- Results Display Grid -->
      <div class="results-grid" style="margin-top: 1.5rem;">
        <div class="result-card primary-result">
          <div class="result-label">Normal Mechanical Stress (\(\sigma\))</div>
          <div class="result-value" id="res-stress">130.77 MPa</div>
          <div class="result-subtext" id="res-stress-sub">18,966.5 psi &bull; 18.97 ksi</div>
        </div>

        <div class="result-card">
          <div class="result-label">Engineering Strain (\(\varepsilon\))</div>
          <div class="result-value" id="res-strain">0.000654</div>
          <div class="result-subtext" id="res-microstrain">653.8 &mu;&epsilon; (microstrain) &bull; 0.065%</div>
        </div>

        <div class="result-card">
          <div class="result-label">Elongation Displacement (\(\Delta L\))</div>
          <div class="result-value" id="res-elong">1.63 mm</div>
          <div class="result-subtext" id="res-elong-sub">0.0644 inches</div>
        </div>

        <div class="result-card">
          <div class="result-label">Design Safety Factor (SF)</div>
          <div class="result-value" id="res-sf" style="color: #28a745;">1.91 (SAFE)</div>
          <div class="result-subtext" id="res-sf-sub">Ratio to 250 MPa yield limit</div>
        </div>
      </div>

      <!-- Step-by-step Math Breakdown Card -->
      <div class="info-card" style="margin-top: 1.5rem;">
        <h3>Step-by-Step Solid Mechanics Derivation</h3>
        <pre id="res-steps" style="white-space: pre-wrap; font-family: monospace; background: var(--bg-secondary, #f8f9fa); padding: 1rem; border-radius: 6px; font-size: 0.9rem; line-height: 1.5; color: var(--text-primary, #212529);"></pre>
      </div>
    </div>

    <!-- Article Content: 1000+ Words Clinical / Engineering Deep Dive -->
    <article class="article-body">
      <h2>The Mechanics of Materials: Stress, Strain, and Constitutive Relations</h2>
      <p>
        In structural engineering, continuum mechanics, and materials science, <strong>stress</strong> and <strong>strain</strong> are the fundamental physical tensors that govern how solid materials deform, absorb internal forces, and ultimately fail under external mechanical loading. Rather than evaluating total external force alone—which varies drastically with physical dimensions—stress normalizes force over contact area, enabling structural engineers to evaluate material durability universally, regardless of whether a specimen is a microscopic laboratory wire or a massive suspension bridge stay cable.
      </p>
      <p>
        Formulated by French mathematician Augustin-Louis Cauchy in 1822, stress-strain theory forms the computational bedrock of civil infrastructure design, aerospace airframe certification, and biomedical prosthetic implant engineering. Structural engineers calculate tensile stresses to ensure skyscraper columns do not buckle under axial compression; aerospace metallurgists model cyclic fatigue strains in jet engine turbine blades; and automotive designers tune crash structures to maximize plastic strain energy absorption during high-speed vehicle impacts.
      </p>

      <h2>Governing Mathematical Equations and Solid Mechanics</h2>

      <h3>1. Normal Engineering Stress</h3>
      <p>
        When an axial tensile or compressive load \(F\) acts perpendicular to a uniform structural cross-section of area \(A\), the average normal stress (\(\sigma\), the Greek letter sigma) is defined as:
      </p>
      $$\sigma = \frac{F}{A}$$
      <p>
        Where:
      </p>
      <ul>
        <li>\(\sigma\) is the mechanical stress, measured in Pascals (\(1\text{ Pa} = 1\text{ N/m}^2\)). In engineering practice, stresses are commonly expressed in Megapascals (\(1\text{ MPa} = 1\text{ N/mm}^2 = 10^6\text{ Pa}\)) or imperial kips per square inch (\(1\text{ ksi} = 1,000\text{ psi} \approx 6.89476\text{ MPa}\)).</li>
        <li>\(F\) is the normal axial tensile (pulling) or compressive (pushing) force in Newtons (\(\text{N}\)).</li>
        <li>\(A\) is the original unloaded cross-sectional area in square meters (\(\text{m}^2\)) or square millimeters (\(\text{mm}^2\)).</li>
      </ul>

      <h3>2. Engineering Strain</h3>
      <p>
        Under applied stress, a material elongates or contracts. <strong>Engineering strain</strong> (\(\varepsilon\), the Greek letter epsilon) is defined as the fractional ratio of linear deformation displacement (\(\Delta L = L - L_0\)) to the original undeformed reference length (\(L_0\)):
      </p>
      $$\varepsilon = \frac{\Delta L}{L_0} = \frac{L - L_0}{L_0}$$
      <p>
        Because strain is a ratio of two lengths (\(\text{m/m}\) or \(\text{in/in}\)), it is a purely <strong>dimensionless quantity</strong>. Engineers frequently express strain as a percentage (\(\varepsilon \times 100\%\)) or in <strong>microstrain</strong> (\(\mu\varepsilon = \varepsilon \times 10^6\)), where \(1,000\,\mu\varepsilon = 0.0010 = 0.1\%\) deformation.
      </p>

      <h3>3. Hooke's Law and Young's Modulus of Elasticity</h3>
      <p>
        For linear elastic materials operating below their proportional elastic limit, stress and strain obey Hooke's Law:
      </p>
      $$\sigma = E \times \varepsilon$$
      <p>
        Where \(E\) is <strong>Young's Modulus of Elasticity</strong>, named after British polymath Thomas Young (1807). Young's modulus represents the fundamental stiffness of a material—the theoretical stress that would double the length of a specimen if it remained perfectly elastic. Solving for elastic elongation \(\Delta L\):
      </p>
      $$\Delta L = \varepsilon \times L_0 = \left( \frac{\sigma}{E} \right) L_0 = \frac{F \times L_0}{A \times E}$$

      <h3>4. Design Safety Factor (SF)</h3>
      <p>
        To prevent structural members from yielding, buckling, or fracturing catastrophically under unforeseen peak service overloads, structural design codes specify a minimum <strong>Safety Factor (SF)</strong>:
      </p>
      $$\text{SF} = \frac{\sigma_{\text{yield}}}{\sigma_{\text{actual}}}$$
      <p>
        Where \(\sigma_{\text{yield}}\) is the material's yield strength (the stress threshold where permanent, irreversible plastic deformation begins). An \(\text{SF} > 1.0\) indicates that the operating stress remains within the reversible elastic regime; values typically range from 1.5 to 2.0 in building structures and 1.25 to 1.5 in weight-sensitive aerospace applications.
      </p>

      <h2>Material Mechanical Properties Benchmark Table</h2>
      <p>
        The table below details benchmark elastic moduli, yield strengths, ultimate tensile strengths (UTS), and Poisson's ratios across fundamental structural alloys, polymers, and ceramics.
      </p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Engineering Material</th>
            <th>Young's Modulus (\(E\)) [GPa]</th>
            <th>Yield Strength (\(\sigma_y\)) [MPa]</th>
            <th>Tensile Strength (\(\sigma_u\)) [MPa]</th>
            <th>Poisson's Ratio (\(\nu\))</th>
            <th>Typical Engineering Applications</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Structural Carbon Steel (ASTM A36)</td>
            <td>200</td>
            <td>250</td>
            <td>400 &ndash; 550</td>
            <td>0.26 &ndash; 0.29</td>
            <td>Building I-beams, welded bridge girders</td>
          </tr>
          <tr>
            <td>High-Strength Low-Alloy Steel (A572 Gr 50)</td>
            <td>205</td>
            <td>345</td>
            <td>450 &ndash; 620</td>
            <td>0.29</td>
            <td>Skyscrapers, heavy equipment frames</td>
          </tr>
          <tr>
            <td>Aircraft Aluminum Alloy (6061-T6)</td>
            <td>68.9</td>
            <td>276</td>
            <td>310</td>
            <td>0.33</td>
            <td>Aircraft fuselage ribs, bicycle frames</td>
          </tr>
          <tr>
            <td>High-Strength Aluminum (7075-T6)</td>
            <td>71.7</td>
            <td>503</td>
            <td>572</td>
            <td>0.33</td>
            <td>Aerospace wing spars, defense equipment</td>
          </tr>
          <tr>
            <td>Titanium Alloy (Ti-6Al-4V Grade 5)</td>
            <td>113.8</td>
            <td>880</td>
            <td>950</td>
            <td>0.342</td>
            <td>Jet turbine compressor disks, surgical bone implants</td>
          </tr>
          <tr>
            <td>Electrolytic Copper (C11000)</td>
            <td>117</td>
            <td>69 &ndash; 310</td>
            <td>220 &ndash; 380</td>
            <td>0.34</td>
            <td>Electrical busbars, heat exchanger tubes</td>
          </tr>
          <tr>
            <td>Structural Concrete (Normal Weight)</td>
            <td>21 &ndash; 30</td>
            <td>&mdash;</td>
            <td>2 &ndash; 5 (Tensile) / 25 &ndash; 45 (Compressive)</td>
            <td>0.15 &ndash; 0.20</td>
            <td>Building foundations, highway roadbeds</td>
          </tr>
          <tr>
            <td>Carbon Fiber Composite (CFRP UD)</td>
            <td>135 &ndash; 180</td>
            <td>&mdash;</td>
            <td>1,500 &ndash; 2,200</td>
            <td>0.28 &ndash; 0.32</td>
            <td>Formula 1 monocoques, Boeing 787 wing skins</td>
          </tr>
          <tr>
            <td>Structural Timber (Douglas Fir, Parallel)</td>
            <td>11 &ndash; 13</td>
            <td>30 &ndash; 50</td>
            <td>50 &ndash; 80</td>
            <td>0.29 &ndash; 0.37</td>
            <td>Residential roof framing, engineered glulam beams</td>
          </tr>
        </tbody>
      </table>

      <h2>Practical Real-World Engineering Case Studies</h2>

      <div class="worked-example-card">
        <h3>Case Study 1: Structural Steel Tie-Rod Sizing in Suspended Pedestrian Bridge</h3>
        <p><strong>Scenario:</strong> A suspended pedestrian footbridge uses solid round ASTM A36 structural steel tie-rods (\(E = 200\text{ GPa} = 200,000\text{ MPa}\), yield strength \(\sigma_y = 250\text{ MPa}\)). Each rod has an unsupported length of \(L_0 = 8.0\text{ m}\) and carries a peak tensile design load of \(F = 180\text{ kN}\) (\(180,000\text{ N}\)). Structural safety code mandates a minimum safety factor of \(SF \ge 2.0\).</p>
        <p><strong>Objective:</strong> Determine the minimum required rod diameter \(d\), calculate the operating tensile stress, and determine total elastic elongation \(\Delta L\) under full design live load.</p>
        <div class="step-solution">
          <p><strong>1. Allowable Tensile Stress Limit:</strong></p>
          $$\sigma_{\text{allow}} = \frac{\sigma_y}{SF} = \frac{250\text{ MPa}}{2.0} = 125.0\text{ MPa} \ (125\text{ N/mm}^2)$$
          <p><strong>2. Minimum Required Cross-Sectional Area and Diameter:</strong></p>
          $$A_{\text{req}} = \frac{F}{\sigma_{\text{allow}}} = \frac{180,000\text{ N}}{125\text{ N/mm}^2} = 1,440\text{ mm}^2$$
          $$d_{\text{min}} = \sqrt{\frac{4 A_{\text{req}}}{\pi}} = \sqrt{\frac{4 \times 1,440}{\pi}} = \sqrt{1,833.46} \approx 42.82\text{ mm}$$
          <p>The structural engineer specifies standard \(45\text{ mm}\) diameter round tie-bars (\(A_{\text{actual}} = \frac{\pi}{4}(45)^2 = 1,590.43\text{ mm}^2\)).</p>
          <p><strong>3. Operating Stress and Elastic Elongation:</strong></p>
          $$\sigma_{\text{actual}} = \frac{180,000\text{ N}}{1,590.43\text{ mm}^2} = 113.18\text{ MPa} \implies SF_{\text{actual}} = \frac{250}{113.18} = 2.21 \ge 2.0 \text{ (PASS)}$$
          $$\Delta L = \frac{F L_0}{A E} = \frac{180,000\text{ N} \times 8,000\text{ mm}}{1,590.43\text{ mm}^2 \times 200,000\text{ N/mm}^2} = \frac{1.44 \times 10^9}{3.18086 \times 10^8} \approx 4.527\text{ mm}$$
          <p>Under full live load, the 8-meter rod safely stretches by just 4.53 mm, fully recovering upon load removal.</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Aerospace Titanium Hydraulic Actuator Piston Rod Sizing</h3>
        <p><strong>Scenario:</strong> An aircraft flight control surface uses a solid titanium Ti-6Al-4V piston actuator rod (\(E = 114\text{ GPa}\), yield strength \(\sigma_y = 880\text{ MPa}\)) of diameter \(d = 20.0\text{ mm}\) and length \(L_0 = 600\text{ mm}\). During a high-speed aerodynamic maneuver, the hydraulic cylinder exerts an axial compressive thrust of \(F = 95\text{ kN}\) (\(95,000\text{ N}\)).</p>
        <p><strong>Objective:</strong> Compute compressive stress, operating safety factor against material yielding, and total elastic stroke compression.</p>
        <div class="step-solution">
          <p><strong>1. Cross-Sectional Area:</strong></p>
          $$A = \frac{\pi}{4} d^2 = \frac{\pi}{4} (20.0\text{ mm})^2 = 314.16\text{ mm}^2 = 3.1416 \times 10^{-4}\text{ m}^2$$
          <p><strong>2. Compressive Stress and Safety Factor:</strong></p>
          $$\sigma = \frac{F}{A} = \frac{95,000\text{ N}}{314.16\text{ mm}^2} \approx 302.39\text{ MPa} \ (43,858\text{ psi})$$
          $$SF = \frac{\sigma_y}{\sigma} = \frac{880\text{ MPa}}{302.39\text{ MPa}} \approx 2.91 \ge 1.50 \text{ (PASS)}$$
          <p><strong>3. Elastic Stroke Compression:</strong></p>
          $$\Delta L = \frac{F L_0}{A E} = \frac{95,000\text{ N} \times 600\text{ mm}}{314.16\text{ mm}^2 \times 114,000\text{ N/mm}^2} = \frac{5.70 \times 10^7}{3.5814 \times 10^7} \approx 1.5916\text{ mm}$$
          <p>The actuator compresses elastically by 1.59 mm, a displacement compensated for by the aircraft's closed-loop fly-by-wire servo control software.</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 3: Concrete Pier Compressive Stress in Civil Substructure</h3>
        <p><strong>Scenario:</strong> A highway overpass bridge bent is supported by a square reinforced concrete column pier of dimensions \(800\text{ mm} \times 800\text{ mm}\) (\(A = 640,000\text{ mm}^2 = 0.64\text{ m}^2\)) and height \(L_0 = 6.5\text{ m}\). Concrete 28-day cylinder compressive strength is \(f'_c = 35.0\text{ MPa}\), with elastic modulus \(E_c = 28,000\text{ MPa}\). The pier carries a total factored dead and live load of \(F = 7,200\text{ kN}\) (\(7,200,000\text{ N}\)).</p>
        <p><strong>Objective:</strong> Compute the direct compressive bearing stress, verify compliance against ACI 318 design limits, and determine total vertical column settlement.</p>
        <div class="step-solution">
          <p><strong>1. Direct Compressive Stress:</strong></p>
          $$\sigma = \frac{F}{A} = \frac{7,200,000\text{ N}}{640,000\text{ mm}^2} = 11.25\text{ MPa} \ (1,631.7\text{ psi})$$
          <p><strong>2. Structural Verification (ACI 318 Code):</strong></p>
          <p>Per ACI 318, allowable pure axial bearing stress is \(\phi P_n / A = 0.65 \times 0.85 f'_c \approx 0.5525 \times 35.0 = 19.34\text{ MPa}\):</p>
          $$\sigma_{\text{actual}} = 11.25\text{ MPa} \le 19.34\text{ MPa} \implies \text{Adequate Sectional Capacity (PASS)}$$
          <p><strong>3. Elastic Vertical Compression (Settlement):</strong></p>
          $$\Delta L = \frac{F L_0}{A E_c} = \frac{7,200,000\text{ N} \times 6,500\text{ mm}}{640,000\text{ mm}^2 \times 28,000\text{ N/mm}^2} = \frac{4.68 \times 10^{10}}{1.792 \times 10^{10}} \approx 2.6116\text{ mm}$$
          <p>The column compresses vertically by only 2.61 mm under full bridge traffic loading.</p>
        </div>
      </div>

      <h2>Frequently Asked Questions</h2>
      <div class="faq-accordion">
        <details class="faq-item">
          <summary class="faq-question">What is the difference between true stress and engineering stress?</summary>
          <div class="faq-answer">
            <p>Engineering stress (\(\sigma_{\text{eng}} = F / A_0\)) calculates stress dividing force by the original, undeformed cross-sectional area. True stress (\(\sigma_{\text{true}} = F / A_{\text{inst}}\)) divides force by the actual instantaneous cross-sectional area measured in real time. Because a ductile tensile specimen necks down (thins) during plastic deformation, true stress is always higher than engineering stress in tension.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">What occurs beyond the yield point on a stress-strain curve?</summary>
          <div class="faq-answer">
            <p>Below the yield point, a material deforms elastically: if unloaded, it returns 100% to its original shape. Beyond the yield point, dislocation movement causes irreversible plastic deformation: when unloaded, the material retains permanent deformation along an offset parallel to the elastic line. Continuing stress leads to work hardening, ultimate tensile strength (UTS), necking, and eventual ductile or brittle fracture.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">How does temperature affect Young's modulus and yield strength?</summary>
          <div class="faq-answer">
            <p>Elevated temperatures increase atomic thermal kinetic energy, weakening intermolecular metallic and covalent bonds. Consequently, increasing temperature decreases Young's modulus (making materials less stiff) and significantly lowers yield and tensile strength, increasing ductility. At temperatures above 40% of absolute melting temperature, materials experience time-dependent plastic flow known as creep.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">What is shear stress versus normal stress?</summary>
          <div class="faq-answer">
            <p>Normal stress (\(\sigma\)) acts perpendicular to a surface plane, tending to pull it apart (tension) or push it together (compression). Shear stress (\(\tau\)) acts parallel (tangential) to the surface plane, tending to slide adjacent layers of material past one another (such as scissors cutting paper, or bolted flange connections resisting transverse shear).</p>
          </div>
        </details>
      </div>

      <!-- Cross-Disciplinary Internal Links -->
      <div class="related-calculators" style="margin-top: 2rem; padding: 1.5rem; background: var(--bg-secondary, #f8f9fa); border-radius: 8px;">
        <h3>Related Engineering &amp; Solid Mechanics Calculators</h3>
        <ul style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.75rem; list-style: none; padding: 0;">
          <li><a href="force-calculator.html">&rarr; Force &amp; Newton's Second Law Solver (F = ma)</a></li>
          <li><a href="pressure-calculator.html">&rarr; Mechanical Pressure Calculator (P = F/A)</a></li>
          <li><a href="hookes-law-calculator.html">&rarr; Hooke's Law Spring Stiffness Calculator</a></li>
          <li><a href="thermal-expansion-calculator.html">&rarr; Thermal Expansion &amp; Stress Solver</a></li>
          <li><a href="beam-calculator.html">&rarr; Beam Bending Moment &amp; Shear Calculator</a></li>
          <li><a href="pressure-converter.html">&rarr; Universal Pressure &amp; Stress Unit Converter</a></li>
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
      'kN': 1000.0,
      'N': 1.0,
      'lbf': 4.448221615,
      'kip': 4448.221615
    };

    var AREA_FACTORS = {
      'mm2': 0.000001,
      'cm2': 0.0001,
      'm2': 1.0,
      'in2': 0.00064516
    };

    var LENGTH_FACTORS = {
      'm': 1.0,
      'mm': 0.001,
      'in': 0.0254,
      'ft': 0.3048
    };

    var E_FACTORS = {
      'GPa': 1000000000.0,
      'MPa': 1000000.0,
      'psi': 6894.75729,
      'ksi': 6894757.29
    };

    function switchSSMode() {
      calculateSS();
    }

    function loadMaterialPreset() {
      var val = document.getElementById('material-preset').value;
      if (val === 'custom') return;

      var parts = val.split(',');
      var eGpa = parseFloat(parts[0]);
      var yMpa = parseFloat(parts[1]);

      document.getElementById('ss-e').value = eGpa;
      document.getElementById('ss-unit-e').value = 'GPa';
      document.getElementById('ss-yield').value = yMpa;

      calculateSS();
    }

    function calculateSS() {
      var fVal = parseFloat(document.getElementById('ss-force').value);
      var fUnit = document.getElementById('ss-unit-f').value;
      var aVal = parseFloat(document.getElementById('ss-area').value);
      var aUnit = document.getElementById('ss-unit-a').value;
      var lVal = parseFloat(document.getElementById('ss-l0').value);
      var lUnit = document.getElementById('ss-unit-l').value;
      var eVal = parseFloat(document.getElementById('ss-e').value);
      var eUnit = document.getElementById('ss-unit-e').value;
      var yMpa = parseFloat(document.getElementById('ss-yield').value);

      if (isNaN(fVal) || isNaN(aVal) || isNaN(lVal) || isNaN(eVal) || fVal < 0 || aVal <= 0 || lVal <= 0 || eVal <= 0) {
        showError("Applied force, area, length, and modulus must be valid positive numbers.");
        return;
      }

      var fN = fVal * FORCE_FACTORS[fUnit];
      var aM2 = aVal * AREA_FACTORS[aUnit];
      var lM = lVal * LENGTH_FACTORS[lUnit];
      var ePa = eVal * E_FACTORS[eUnit];

      // Stress: sigma = F / A in Pascals
      var stressPa = fN / aM2;
      var stressMpa = stressPa / 1000000.0;
      var stressPsi = stressPa / 6894.75729;
      var stressKsi = stressPsi / 1000.0;

      // Strain: epsilon = sigma / E (dimensionless)
      var strain = stressPa / ePa;
      var microstrain = strain * 1000000.0;
      var pctStrain = strain * 100.0;

      // Elongation: delta L = epsilon * L0 in meters
      var deltaLM = strain * lM;
      var deltaLMm = deltaLM * 1000.0;
      var deltaLIn = deltaLM / 0.0254;

      // Safety factor: SF = yield / actual
      var sfStr = "N/A", sfColor = "#6c757d", sfSub = "Yield strength not specified";
      if (!isNaN(yMpa) && yMpa > 0) {
        var sf = yMpa / stressMpa;
        sfSub = "Ratio to " + yMpa + " MPa yield limit";
        if (sf >= 1.5) {
          sfStr = sf.toFixed(2) + " (SAFE)";
          sfColor = "#28a745";
        } else if (sf >= 1.0) {
          sfStr = sf.toFixed(2) + " (MARGINAL)";
          sfColor = "#fd7e14";
        } else {
          sfStr = sf.toFixed(2) + " (YIELD / FAILURE)";
          sfColor = "#dc3545";
        }
      }

      var steps = "Mode: Normal Stress & Strain Solid Mechanics\n" +
                  "Inputs: F = " + fVal + " " + fUnit + ", Area A = " + aVal + " " + aUnit + ", L0 = " + lVal + " " + lUnit + ", E = " + eVal + " " + eUnit + "\n\n" +
                  "1. Force in SI: F = " + fN.toFixed(2) + " N\n" +
                  "2. Area in SI: A = " + aM2.toExponential(4) + " m² (" + (aM2 * 1e6).toFixed(2) + " mm²)\n\n" +
                  "3. Normal Stress: σ = F / A = " + fN.toFixed(2) + " / " + aM2.toExponential(4) + "\n" +
                  "   σ = " + stressPa.toFixed(2) + " Pa = " + stressMpa.toFixed(2) + " MPa (" + stressPsi.toFixed(1) + " psi, " + stressKsi.toFixed(2) + " ksi)\n\n" +
                  "4. Engineering Strain: ε = σ / E = " + stressPa.toFixed(2) + " / " + ePa.toExponential(4) + "\n" +
                  "   ε = " + strain.toExponential(4) + " (" + microstrain.toFixed(1) + " με, " + pctStrain.toFixed(4) + "%)\n\n" +
                  "5. Elastic Elongation: ΔL = ε * L0 = " + strain.toExponential(4) + " * " + lM.toFixed(4) + " m\n" +
                  "   ΔL = " + deltaLMm.toFixed(3) + " mm (" + deltaLIn.toFixed(4) + " inches)\n\n" +
                  "6. Safety Factor: SF = σ_yield / σ_actual = " + (!isNaN(yMpa) && yMpa > 0 ? (yMpa + " / " + stressMpa.toFixed(2) + " = " + (yMpa / stressMpa).toFixed(2)) : "N/A");

      document.getElementById('res-stress').innerText = stressMpa.toFixed(2) + " MPa";
      document.getElementById('res-stress-sub').innerText = stressPsi.toLocaleString(undefined, {maximumFractionDigits: 1}) + " psi • " + stressKsi.toFixed(2) + " ksi";
      document.getElementById('res-strain').innerText = strain.toPrecision(4);
      document.getElementById('res-microstrain').innerText = microstrain.toFixed(1) + " με (microstrain) • " + pctStrain.toFixed(4) + "%";
      document.getElementById('res-elong').innerText = deltaLMm.toFixed(2) + " mm";
      document.getElementById('res-elong-sub').innerText = deltaLIn.toFixed(4) + " inches";
      document.getElementById('res-sf').innerText = sfStr;
      document.getElementById('res-sf').style.color = sfColor;
      document.getElementById('res-sf-sub').innerText = sfSub;

      document.getElementById('res-steps').innerText = steps;
    }

    function showError(msg) {
      document.getElementById('res-stress').innerText = "Error";
      document.getElementById('res-stress-sub').innerText = "Invalid calculation";
      document.getElementById('res-strain').innerText = "N/A";
      document.getElementById('res-microstrain').innerText = "N/A";
      document.getElementById('res-elong').innerText = "N/A";
      document.getElementById('res-elong-sub').innerText = "N/A";
      document.getElementById('res-sf').innerText = "N/A";
      document.getElementById('res-sf').style.color = "#6c757d";
      document.getElementById('res-steps').innerText = "Error: " + msg;
    }

    function resetSS() {
      document.getElementById('ss-force').value = '85';
      document.getElementById('ss-unit-f').value = 'kN';
      document.getElementById('ss-area').value = '650';
      document.getElementById('ss-unit-a').value = 'mm2';
      document.getElementById('ss-l0').value = '2.5';
      document.getElementById('ss-unit-l').value = 'm';
      document.getElementById('ss-e').value = '200';
      document.getElementById('ss-unit-e').value = 'GPa';
      document.getElementById('ss-yield').value = '250';
      document.getElementById('material-preset').value = 'custom';
      calculateSS();
    }

    window.addEventListener('DOMContentLoaded', function() {
      calculateSS();
    });
  </script>
</body>
</html>
"""

def generate_part3():
    f5 = os.path.join(BASE_DIR, "work-power-calculator.html")
    with open(f5, "w", encoding="utf-8") as fp:
        fp.write(HTML_WORK_POWER.strip() + "\n")
    print(f"Generated: {f5}")

    f6 = os.path.join(BASE_DIR, "stress-strain-calculator.html")
    with open(f6, "w", encoding="utf-8") as fp:
        fp.write(HTML_STRESS_STRAIN.strip() + "\n")
    print(f"Generated: {f6}")

if __name__ == "__main__":
    generate_part3()
