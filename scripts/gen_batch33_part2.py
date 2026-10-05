# -*- coding: utf-8 -*-
"""
Generator for Batch 33 - Part 2:
3. impulse-calculator.html
4. potential-energy-calculator.html
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 3. impulse-calculator.html
HTML_IMPULSE = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Impulse Calculator - Impulse-Momentum Theorem (J = FΔt = Δp)</title>
  <meta name="description" content="Calculate impulse (J = F·Δt = Δp), average impact force, collision duration, and velocity changes. Master crash dynamics, crumple zones, and sports ball strikes.">
  <link rel="canonical" href="https://calchub.org/impulse-calculator.html">
  <meta property="og:title" content="Impulse Calculator - Impulse-Momentum Theorem &amp; Impact Force Solver">
  <meta property="og:description" content="Free physics impulse calculator. Compute impulse J = F·Δt = Δp, peak impact forces, and crash deceleration times with step-by-step mathematical proofs.">
  <meta property="og:url" content="https://calchub.org/impulse-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Impulse Calculator - Crash Dynamics &amp; Impact Force Solver">
  <meta name="twitter:description" content="Solve impulse, impact force, and collision time with multi-unit conversions and real-world engineering case studies.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Impulse Calculator",
    "url": "https://calchub.org/impulse-calculator.html",
    "description": "Calculates mechanical impulse, average collision impact force, contact time, and momentum change across engineering units.",
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
        "name": "What is the Impulse-Momentum Theorem?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Impulse-Momentum Theorem states that the net impulse (J) delivered to an object equals the resulting change in its linear momentum: J = F_avg * Δt = Δp = m * (v_final - v_initial). In SI units, impulse is measured in Newton-seconds (N·s) or kilogram-meters per second (kg·m/s)."
        }
      },
      {
        "@type": "Question",
        "name": "Why do airbags reduce collision injuries during car accidents?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "In a crash, bringing a vehicle occupant to rest requires a fixed change in momentum (Δp). By inflating and yielding under passenger contact, an airbag significantly extends the collision duration (Δt). Because F_avg = Δp / Δt, lengthening the contact time reduces the average impact force transmitted to the human body."
        }
      },
      {
        "@type": "Question",
        "name": "How is impulse calculated from a force-time graph?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Impulse is mathematically the definite integral of force with respect to time: J = ∫ F(t) dt. On a force-versus-time graph, impulse equals the net geometric area under the force curve between the initial and final impact times."
        }
      },
      {
        "@type": "Question",
        "name": "What is specific impulse (Isp) in rocket propulsion?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Specific impulse (Isp) measures rocket propellant mass efficiency, defined as the total impulse produced per unit weight of propellant consumed: Isp = J / (m_propellant * g_0) = F_thrust / (m_dot * g_0), measured in seconds."
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
      <div class="calc-icon" aria-hidden="true">&#128165;</div>
      <h1>Impulse Calculator</h1>
      <p class="calc-description">Compute mechanical impulse (\(J = F\Delta t = \Delta p\)), collision contact force, impact duration, and velocity changes with step-by-step dynamics proofs.</p>
    </div>

    <div class="calculator-body">
      <div class="input-group">
        <label for="imp-mode">Calculation Mode</label>
        <select id="imp-mode" class="form-control" onchange="switchImpulseMode()">
          <option value="force-time" selected>Force &amp; Contact Time &rarr; Solve Impulse (\(J = F \times \Delta t\))</option>
          <option value="momentum-change">Mass &amp; Velocity Change &rarr; Solve Impulse &amp; Impact Force (\(J = m \Delta v\))</option>
          <option value="solve-force">Impulse &amp; Time &rarr; Solve Average Impact Force (\(F = J / \Delta t\))</option>
        </select>
      </div>

      <!-- Mode 1: Force & Time -->
      <div id="panel-ft">
        <div class="input-grid">
          <div class="input-group">
            <label for="ft-force">Average Applied Force (\(F_{\text{avg}}\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="ft-force" class="form-control" value="8500" step="any" min="0" style="flex: 2;">
              <select id="ft-unit-force" class="form-control" style="flex: 1;" onchange="calculateImpulse()">
                <option value="N" selected>N</option>
                <option value="kN">kN</option>
                <option value="lbf">lbf</option>
              </select>
            </div>
          </div>

          <div class="input-group">
            <label for="ft-time">Collision / Contact Duration (\(\Delta t\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="ft-time" class="form-control" value="25" step="any" min="0" style="flex: 2;">
              <select id="ft-unit-time" class="form-control" style="flex: 1;" onchange="calculateImpulse()">
                <option value="ms" selected>milliseconds (ms)</option>
                <option value="s">seconds (s)</option>
                <option value="us">microseconds (&mu;s)</option>
              </select>
            </div>
          </div>
        </div>
      </div>

      <!-- Mode 2: Mass & Delta V -->
      <div id="panel-mv" style="display: none;">
        <div class="input-grid">
          <div class="input-group">
            <label for="mv-mass">Object Mass (\(m\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="mv-mass" class="form-control" value="1400" step="any" min="0" style="flex: 2;">
              <select id="mv-unit-mass" class="form-control" style="flex: 1;" onchange="calculateImpulse()">
                <option value="kg" selected>kg</option>
                <option value="g">g</option>
                <option value="lb">lb</option>
              </select>
            </div>
          </div>

          <div class="input-group">
            <label for="mv-dt">Collision Time (\(\Delta t\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="mv-dt" class="form-control" value="120" step="any" min="0" style="flex: 2;">
              <select id="mv-unit-dt" class="form-control" style="flex: 1;" onchange="calculateImpulse()">
                <option value="ms" selected>ms</option>
                <option value="s">s</option>
              </select>
            </div>
          </div>
        </div>

        <div class="input-grid">
          <div class="input-group">
            <label for="mv-v1">Initial Velocity (\(v_i\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="mv-v1" class="form-control" value="20" step="any" style="flex: 2;">
              <select id="mv-unit-v" class="form-control" style="flex: 1;" onchange="calculateImpulse()">
                <option value="m_s" selected>m/s</option>
                <option value="km_h">km/h</option>
                <option value="mph">mph</option>
              </select>
            </div>
          </div>

          <div class="input-group">
            <label for="mv-v2">Final Velocity (\(v_f\))</label>
            <input type="number" id="mv-v2" class="form-control" value="0" step="any">
            <small style="color: var(--text-muted, #6c757d);">e.g. 0 for full stop, negative for rebound</small>
          </div>
        </div>
      </div>

      <!-- Mode 3: Solve Force -->
      <div id="panel-force" style="display: none;">
        <div class="input-grid">
          <div class="input-group">
            <label for="sf-imp">Target Impulse (\(J\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="sf-imp" class="form-control" value="28000" step="any" min="0" style="flex: 2;">
              <select id="sf-unit-imp" class="form-control" style="flex: 1;" onchange="calculateImpulse()">
                <option value="N_s" selected>N&middot;s</option>
                <option value="kN_s">kN&middot;s</option>
                <option value="lbf_s">lbf&middot;s</option>
              </select>
            </div>
          </div>

          <div class="input-group">
            <label for="sf-time">Impact Duration (\(\Delta t\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="sf-time" class="form-control" value="80" step="any" min="0" style="flex: 2;">
              <select id="sf-unit-time" class="form-control" style="flex: 1;" onchange="calculateImpulse()">
                <option value="ms" selected>ms</option>
                <option value="s">s</option>
              </select>
            </div>
          </div>
        </div>
      </div>

      <div class="btn-group">
        <button type="button" class="btn btn-primary" onclick="calculateImpulse()">Compute Impulse Dynamics</button>
        <button type="button" class="btn btn-secondary" onclick="resetImpulse()">Reset Defaults</button>
      </div>

      <!-- Results Display Grid -->
      <div class="results-grid" style="margin-top: 1.5rem;">
        <div class="result-card primary-result">
          <div class="result-label" id="res-primary-label">Mechanical Impulse (\(J\))</div>
          <div class="result-value" id="res-primary-val">212.50 N&middot;s</div>
          <div class="result-subtext" id="res-primary-sub">212.50 kg&middot;m/s &bull; 47.77 lbf&middot;s</div>
        </div>

        <div class="result-card">
          <div class="result-label" id="res-f-label">Average Impact Force</div>
          <div class="result-value" id="res-f-val">8,500.00 N</div>
          <div class="result-subtext" id="res-f-sub">8.50 kN &bull; 1,910.87 lbf</div>
        </div>

        <div class="result-card">
          <div class="result-label">Momentum Change (\(\Delta p\))</div>
          <div class="result-value" id="res-dp">212.50 kg&middot;m/s</div>
          <div class="result-subtext">Direct vector equivalence</div>
        </div>

        <div class="result-card">
          <div class="result-label">Deceleration G-Force</div>
          <div class="result-value" id="res-gforce">N/A</div>
          <div class="result-subtext" id="res-gsub">Relative to standard gravity</div>
        </div>
      </div>

      <!-- Step-by-step Math Breakdown Card -->
      <div class="info-card" style="margin-top: 1.5rem;">
        <h3>Step-by-Step Physics &amp; Impact Derivation</h3>
        <pre id="res-steps" style="white-space: pre-wrap; font-family: monospace; background: var(--bg-secondary, #f8f9fa); padding: 1rem; border-radius: 6px; font-size: 0.9rem; line-height: 1.5; color: var(--text-primary, #212529);"></pre>
      </div>
    </div>

    <!-- Article Content: 1000+ Words Clinical / Physics Deep Dive -->
    <article class="article-body">
      <h2>The Physical Foundations of Mechanical Impulse and Crash Dynamics</h2>
      <p>
        In classical Newtonian mechanics, trauma biomechanics, and structural survivability engineering, <strong>impulse</strong> (\(\vec{J}\)) is defined as the time-integral of an applied force acting across a finite temporal duration. While force quantifies the instantaneous intensity of a mechanical interaction at a single infinitesimal point in time, impulse quantifies the cumulative, time-integrated effect of that force acting over an entire collision interval.
      </p>
      <p>
        Understanding and manipulating impulse is the cornerstone of modern transportation safety, sports equipment engineering, and ballistics. Automotive crash engineers design deformable aluminum crumple zones and deploying pyrotechnic airbags specifically to prolong the deceleration impact time, drastically reducing peak forces transmitted to human organ systems. Similarly, athletic footwear designers incorporate viscous polyurethane midsoles to dampen heel-strike ground reaction forces, and baseball catchers use thick leather mitts to mitigate high-velocity pitch impact shocks.
      </p>

      <h2>Mathematical Formulations: The Impulse-Momentum Theorem</h2>
      <p>
        Starting from Newton's Second Law of Motion in its original differential form:
      </p>
      $$\vec{F}_{\text{net}} = \frac{d\vec{p}}{dt}$$
      <p>
        Integrating both sides with respect to time over the collision interval from \(t_i\) to \(t_f\):
      </p>
      $$\vec{J} = \int_{t_i}^{t_f} \vec{F}_{\text{net}}(t) \, dt = \int_{\vec{p}_i}^{\vec{p}_f} d\vec{p} = \vec{p}_f - \vec{p}_i = \Delta \vec{p}$$
      <p>
        For a body of constant inertial mass \(m\) undergoing a velocity change from \(\vec{v}_i\) to \(\vec{v}_f\):
      </p>
      $$\vec{J} = \Delta \vec{p} = m (\vec{v}_f - \vec{v}_i) = m \Delta \vec{v}$$
      <p>
        If the applied force is approximated as a constant average force \(\vec{F}_{\text{avg}}\) across duration \(\Delta t = t_f - t_i\):
      </p>
      $$\vec{J} = \vec{F}_{\text{avg}} \times \Delta t$$
      <p>
        Equating these two expressions yields the canonical <strong>Impulse-Momentum Theorem</strong>:
      </p>
      $$\vec{F}_{\text{avg}} \times \Delta t = m \Delta \vec{v}$$

      <h3>The Mechanics of Impact Force Attenuation</h3>
      <p>
        Solving for average impact force reveals the inverse relationship between collision contact duration and transmitted force:
      </p>
      $$\vec{F}_{\text{avg}} = \frac{m \Delta \vec{v}}{\Delta t} = \frac{\Delta \vec{p}}{\Delta t}$$
      <p>
        This equation is the governing equation of vehicular crashworthiness:
      </p>
      <ul>
        <li>When an automobile traveling at \(20\text{ m/s}\) collides with a rigid concrete bridge pier, the unyielding stone stops the vehicle over an extremely brief duration of \(\Delta t \approx 10\text{ ms}\) (\(0.010\text{ s}\)), creating a catastrophic peak deceleration force of hundreds of kilonewtons.</li>
        <li>If the vehicle is equipped with modern progressive crumple zones and an inflating airbag, the deceleration is extended over \(\Delta t \approx 120\text{ ms}\) (\(0.120\text{ s}\)). Lengthening the impact time by a factor of 12 reduces average impact force by an identical factor of 12 (a 91.7% reduction in bone-shattering mechanical shock), converting what would have been a fatal trauma into a survivable event.</li>
      </ul>

      <h2>International Impulse Units and Conversions</h2>
      <p>
        In the International System of Units (SI), impulse is measured in <strong>Newton-seconds (\(\text{N}\cdot\text{s}\))</strong>. Dimensional analysis demonstrates that:
      </p>
      $$1\text{ N}\cdot\text{s} = 1\text{ (kg}\cdot\text{m/s}^2\text{)}\cdot\text{s} = 1\text{ kg}\cdot\text{m/s}$$
      <p>
        In imperial engineering, impulse is measured in <strong>pound-force seconds (\(\text{lbf}\cdot\text{s}\))</strong> or slug-feet per second. One pound-force second equals exactly \(4.448221615\text{ N}\cdot\text{s}\).
      </p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Impulse Unit</th>
            <th>Symbol</th>
            <th>Value in SI (N&middot;s)</th>
            <th>Value in Imperial (lbf&middot;s)</th>
            <th>Primary Application Domain</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Newton-second (SI Base)</td>
            <td>N&middot;s</td>
            <td>1.0 (Exact)</td>
            <td>0.224809</td>
            <td>Classical dynamics, robotics, vehicle crashes</td>
          </tr>
          <tr>
            <td>Kilonewton-second</td>
            <td>kN&middot;s</td>
            <td>1,000</td>
            <td>224.809</td>
            <td>Aerospace solid rocket booster burn impulse</td>
          </tr>
          <tr>
            <td>Pound-force second</td>
            <td>lbf&middot;s</td>
            <td>4.448222</td>
            <td>1.0 (Exact)</td>
            <td>US military ballistics, rocket motor sizing</td>
          </tr>
          <tr>
            <td>Dyne-second (CGS)</td>
            <td>dyn&middot;s</td>
            <td>\(1.0 \times 10^{-5}\)</td>
            <td>\(2.248 \times 10^{-6}\)</td>
            <td>Microfluidic drop impacts, MEMS acoustic sensors</td>
          </tr>
        </tbody>
      </table>

      <h2>Benchmark Impulse Events Across Physical Scales</h2>
      <p>
        To illustrate impulse magnitudes across biological, sporting, industrial, and space exploration regimes:
      </p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Physical Collision / Interaction</th>
            <th>Approximate Impulse (\(J\))</th>
            <th>Typical Contact Duration (\(\Delta t\))</th>
            <th>Peak Impact Force (\(F_{\text{peak}}\))</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Tennis Ball Serve Impact</td>
            <td>\(3.0 &ndash; 3.5\text{ N}\cdot\text{s}\)</td>
            <td>\(4 &ndash; 6\text{ ms}\)</td>
            <td>\(700 &ndash; 900\text{ N}\)</td>
          </tr>
          <tr>
            <td>Golf Club Driver Strike</td>
            <td>\(4.5 &ndash; 5.0\text{ N}\cdot\text{s}\)</td>
            <td>\(0.45 &ndash; 0.50\text{ ms}\)</td>
            <td>\(15,000 &ndash; 18,000\text{ N}\)</td>
          </tr>
          <tr>
            <td>Heavyweight Boxer Right Hook</td>
            <td>\(25 &ndash; 40\text{ N}\cdot\text{s}\)</td>
            <td>\(12 &ndash; 18\text{ ms}\)</td>
            <td>\(3,000 &ndash; 4,500\text{ N}\)</td>
          </tr>
          <tr>
            <td>Automobile Head-On 60 km/h Crash</td>
            <td>\(20,000 &ndash; 35,000\text{ N}\cdot\text{s}\)</td>
            <td>\(100 &ndash; 140\text{ ms}\)</td>
            <td>\(200 &ndash; 350\text{ kN}\)</td>
          </tr>
          <tr>
            <td>Commercial Aircraft Runway Touchdown</td>
            <td>\(150,000 &ndash; 300,000\text{ N}\cdot\text{s}\)</td>
            <td>\(300 &ndash; 500\text{ ms}\)</td>
            <td>\(500 &ndash; 900\text{ kN}\)</td>
          </tr>
          <tr>
            <td>Space Shuttle Solid Rocket Booster Burn</td>
            <td>\(1.3 \times 10^9\text{ N}\cdot\text{s}\) (1.3 GN&middot;s)</td>
            <td>\(123\text{ seconds}\)</td>
            <td>\(13.8\text{ MN}\) (Max Thrust)</td>
          </tr>
        </tbody>
      </table>

      <h2>Practical Real-World Engineering Case Studies</h2>

      <div class="worked-example-card">
        <h3>Case Study 1: Automotive Airbag Deployment Biomechanics</h3>
        <p><strong>Scenario:</strong> A \(75\text{ kg}\) adult vehicle occupant travels at \(v_i = 15.0\text{ m/s}\) (54 km/h / 33.5 mph) when their car strikes an obstacle, bringing the passenger compartment to rest (\(v_f = 0\)).</p>
        <p><strong>Objective:</strong> Compare occupant deceleration forces in two cases: (A) Unrestrained occupant striking the rigid steering column over \(\Delta t = 10\text{ ms}\) (\(0.010\text{ s}\)), and (B) Restrained occupant cushioned by seatbelt pretensioners and an inflated airbag over \(\Delta t = 100\text{ ms}\) (\(0.100\text{ s}\)).</p>
        <div class="step-solution">
          <p><strong>1. Fixed Required Momentum Change (Impulse):</strong></p>
          $$J = \Delta p = m (v_f - v_i) = 75\text{ kg} \times (0 - 15.0\text{ m/s}) = -1,125\text{ N}\cdot\text{s}$$
          <p><strong>2. Case A (Rigid Steering Wheel Impact, \(\Delta t = 0.010\text{ s}\)):</strong></p>
          $$F_{\text{avg, A}} = \frac{|J|}{\Delta t_A} = \frac{1,125\text{ N}\cdot\text{s}}{0.010\text{ s}} = 112,500\text{ N} = 112.5\text{ kN} \ (25,291\text{ lbf})$$
          $$\text{Deceleration G-Force} = \frac{F_{\text{avg}}}{m g} = \frac{112,500\text{ N}}{75 \times 9.807} \approx 153.0\text{ g}_0 \quad \text{(Lethal Thoracic Crush)}$$
          <p><strong>3. Case B (Airbag &amp; Seatbelt Deceleration, \(\Delta t = 0.100\text{ s}\)):</strong></p>
          $$F_{\text{avg, B}} = \frac{|J|}{\Delta t_B} = \frac{1,125\text{ N}\cdot\text{s}}{0.100\text{ s}} = 11,250\text{ N} = 11.25\text{ kN} \ (2,529\text{ lbf})$$
          $$\text{Deceleration G-Force} = \frac{11,250\text{ N}}{75 \times 9.807} \approx 15.3\text{ g}_0 \quad \text{(Fully Survivable With Minor Bruising)}$$
          <p>Lengthening the deceleration duration by 90 ms reduces the transmitted impact force by an extraordinary 90%!</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Sports Engineering &ndash; High-Velocity Golf Driver Launch</h3>
        <p><strong>Scenario:</strong> A titanium golf driver head of mass \(M = 200\text{ g}\) strikes a stationary golf ball of mass \(m = 45.9\text{ g}\) (\(0.0459\text{ kg}\)) resting on a tee (\(v_i = 0\)). High-speed phantom cameras record that the ball leaves the clubface at launch velocity \(v_f = 72.0\text{ m/s}\) (161.1 mph) after a microscopic contact window of \(\Delta t = 0.48\text{ ms}\) (\(0.00048\text{ s}\)).</p>
        <p><strong>Objective:</strong> Calculate the impulse delivered to the ball and determine the peak impact force endured by the dimpled golf ball core.</p>
        <div class="step-solution">
          <p><strong>1. Impulse Transferred:</strong></p>
          $$J = m (v_f - v_i) = 0.0459\text{ kg} \times (72.0 - 0\text{ m/s}) \approx 3.3048\text{ N}\cdot\text{s}$$
          <p><strong>2. Average Contact Force:</strong></p>
          $$F_{\text{avg}} = \frac{J}{\Delta t} = \frac{3.3048\text{ N}\cdot\text{s}}{0.00048\text{ s}} \approx 6,885\text{ N} \ (1,547.8\text{ lbf})$$
          <p><strong>3. Peak Force Estimation:</strong></p>
          <p>Because impact force follows a sinusoidal half-wave rather than a flat rectangle, peak force is approximately \(F_{\text{peak}} \approx \frac{\pi}{2} F_{\text{avg}}\):</p>
          $$F_{\text{peak}} \approx 1.5708 \times 6,885\text{ N} \approx 10,815\text{ N} \ (2,431.3\text{ lbf})$$
          <p>For less than half a millisecond, the tiny golf ball sustains over one metric ton of compressive load!</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 3: Aerospace Rocket Propulsion Specific Impulse</h3>
        <p><strong>Scenario:</strong> A liquid rocket engine generates a constant thrust of \(F = 450\text{ kN}\) (\(450,000\text{ N}\)) during an orbital insertion burn lasting \(\Delta t = 180\text{ seconds}\). During the burn, the engine consumes \(m_p = 26,500\text{ kg}\) of LOX/RP-1 propellants. Standard sea-level gravity is \(g_0 = 9.80665\text{ m/s}^2\).</p>
        <p><strong>Objective:</strong> Compute the total delivered impulse and calculate the engine's vacuum specific impulse (\(I_{\text{sp}}\)).</p>
        <div class="step-solution">
          <p><strong>1. Total Delivered Impulse:</strong></p>
          $$J_{\text{total}} = F \times \Delta t = 450,000\text{ N} \times 180\text{ s} = 81,000,000\text{ N}\cdot\text{s} = 81.0\text{ MN}\cdot\text{s}$$
          <p><strong>2. Specific Impulse (\(I_{\text{sp}}\)):</strong></p>
          $$I_{\text{sp}} = \frac{J_{\text{total}}}{m_p \times g_0} = \frac{81,000,000\text{ N}\cdot\text{s}}{26,500\text{ kg} \times 9.80665\text{ m/s}^2} = \frac{81,000,000}{259,876} \approx 311.69\text{ seconds}$$
          <p>The propulsion engineer verifies that the engine achieves an \(I_{\text{sp}}\) of \(311.7\text{ s}\), meeting orbital delivery propellant mass fraction criteria.</p>
        </div>
      </div>

      <h2>Frequently Asked Questions</h2>
      <div class="faq-accordion">
        <details class="faq-item">
          <summary class="faq-question">Why is impulse measured in Newton-seconds instead of Joules?</summary>
          <div class="faq-answer">
            <p>Although both units derive from Newtons, they quantify fundamentally different physical realities. Work (measured in Joules) is force integrated over spatial <em>distance</em>: \(W = \int F \, dx = \text{N}\cdot\text{m}\), representing energy transfer. Impulse (measured in Newton-seconds) is force integrated over temporal <em>duration</em>: \(J = \int F \, dt = \text{N}\cdot\text{s}\), representing momentum transfer. Work is a scalar related to velocity squared, while impulse is a vector linear in velocity.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">Why do follow-through strokes in tennis and golf increase ball speed?</summary>
          <div class="faq-answer">
            <p>A committed follow-through stroke prevents the athlete from prematurely decelerating the racket or clubface prior to contact. By keeping the impact surface driving through the strike zone, the club remains in contact with the compressing ball for a fractionally longer interval (\(\Delta t\)). Per \(J = F_{\text{avg}} \Delta t = m \Delta v\), maximizing contact duration increases total impulse, yielding higher ball launch velocity.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">What is the difference between peak force and average force during a collision?</summary>
          <div class="faq-answer">
            <p>During a collision, contact force is not flat: it starts at zero upon initial contact, spikes rapidly to a high peak as materials compress, and decays back to zero as objects separate. The average force (\(F_{\text{avg}} = J / \Delta t\)) represents a steady equivalent force producing identical momentum change. In real collisions, the peak force is typically 1.5 to 2.5 times higher than the average force, which is why peak force usually causes structural or biological failure.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">How does catching a ball by pulling your hands back reduce pain?</summary>
          <div class="faq-answer">
            <p>Bringing a fast-moving ball to rest requires absorbing a fixed quantity of momentum (\(\Delta p\)). Stiffening your hands stops the ball over a tiny fraction of a second (\(\Delta t \approx 5\text{ ms}\)), generating intense stinging impact force. By pulling your hands backward as the ball lands, you extend the stopping duration to \(\Delta t \approx 100\text{ ms}\), slashing the impact force on your palms by over 90%.</p>
          </div>
        </details>
      </div>

      <!-- Cross-Disciplinary Internal Links -->
      <div class="related-calculators" style="margin-top: 2rem; padding: 1.5rem; background: var(--bg-secondary, #f8f9fa); border-radius: 8px;">
        <h3>Related Physics &amp; Dynamics Calculators</h3>
        <ul style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.75rem; list-style: none; padding: 0;">
          <li><a href="momentum-calculator.html">&rarr; Linear Momentum &amp; Collision Solver (p = mv)</a></li>
          <li><a href="force-calculator.html">&rarr; Force &amp; Newton's Second Law Solver (F = ma)</a></li>
          <li><a href="speed-calculator.html">&rarr; Speed &amp; Kinematics Calculator (v = d/t)</a></li>
          <li><a href="kinetic-energy-calculator.html">&rarr; Kinetic Energy Calculator (Ek = 0.5mv²)</a></li>
          <li><a href="acceleration-calculator.html">&rarr; Acceleration Kinematics Solver</a></li>
          <li><a href="pressure-calculator.html">&rarr; Mechanical Pressure Calculator (P = F/A)</a></li>
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
    var TIME_FACTORS = {
      'ms': 0.001,
      's': 1.0,
      'us': 0.000001
    };

    var FORCE_FACTORS = {
      'N': 1.0,
      'kN': 1000.0,
      'lbf': 4.448221615
    };

    var MASS_FACTORS = {
      'kg': 1.0,
      'g': 0.001,
      'lb': 0.45359237
    };

    var VEL_FACTORS = {
      'm_s': 1.0,
      'km_h': 0.277777778,
      'mph': 0.44704
    };

    var IMP_FACTORS = {
      'N_s': 1.0,
      'kN_s': 1000.0,
      'lbf_s': 4.448221615
    };

    function switchImpulseMode() {
      var mode = document.getElementById('imp-mode').value;
      document.getElementById('panel-ft').style.display = (mode === 'force-time') ? 'block' : 'none';
      document.getElementById('panel-mv').style.display = (mode === 'momentum-change') ? 'block' : 'none';
      document.getElementById('panel-force').style.display = (mode === 'solve-force') ? 'block' : 'none';

      var lbl = document.getElementById('res-primary-label');
      var fLbl = document.getElementById('res-f-label');
      if (mode === 'solve-force') {
        lbl.innerText = "Average Impact Force";
        fLbl.innerText = "Supplied Impulse (J)";
      } else {
        lbl.innerText = "Mechanical Impulse (J)";
        fLbl.innerText = "Average Impact Force";
      }

      calculateImpulse();
    }

    function calculateImpulse() {
      var mode = document.getElementById('imp-mode').value;
      var j_Ns = 0, f_N = 0, dt_s = 0;
      var gforceStr = "N/A", gsubStr = "Requires mass input";
      var steps = "";

      if (mode === 'force-time') {
        var fVal = parseFloat(document.getElementById('ft-force').value);
        var fUnit = document.getElementById('ft-unit-force').value;
        var tVal = parseFloat(document.getElementById('ft-time').value);
        var tUnit = document.getElementById('ft-unit-time').value;

        if (isNaN(fVal) || isNaN(tVal) || fVal < 0 || tVal <= 0) {
          showError("Force and collision duration must be positive values.");
          return;
        }

        f_N = fVal * FORCE_FACTORS[fUnit];
        dt_s = tVal * TIME_FACTORS[tUnit];
        j_Ns = f_N * dt_s;

        steps = "Mode: Force & Contact Duration (J = F * Δt)\n" +
                "Inputs: F = " + fVal + " " + fUnit + ", Δt = " + tVal + " " + tUnit + "\n\n" +
                "1. Force in SI: F = " + f_N.toFixed(2) + " N\n" +
                "2. Duration in SI: Δt = " + dt_s.toExponential(4) + " s (" + (dt_s * 1000).toFixed(2) + " ms)\n\n" +
                "3. Compute Impulse: J = F * Δt = " + f_N.toFixed(2) + " * " + dt_s.toExponential(4) + "\n" +
                "   J = " + j_Ns.toFixed(3) + " N·s (" + j_Ns.toFixed(3) + " kg·m/s, " + (j_Ns / 4.448222).toFixed(3) + " lbf·s)";

        document.getElementById('res-primary-val').innerText = j_Ns.toFixed(2) + " N·s";
        document.getElementById('res-primary-sub').innerText = j_Ns.toFixed(2) + " kg·m/s • " + (j_Ns / 4.448222).toFixed(2) + " lbf·s";
        document.getElementById('res-f-val').innerText = f_N.toLocaleString(undefined, {maximumFractionDigits: 1}) + " N";
        document.getElementById('res-f-sub').innerText = (f_N / 1000).toFixed(3) + " kN • " + (f_N / 4.448222).toFixed(1) + " lbf";

      } else if (mode === 'momentum-change') {
        var mVal = parseFloat(document.getElementById('mv-mass').value);
        var mUnit = document.getElementById('mv-unit-mass').value;
        var tVal2 = parseFloat(document.getElementById('mv-dt').value);
        var tUnit2 = document.getElementById('mv-unit-dt').value;
        var v1Val = parseFloat(document.getElementById('mv-v1').value);
        var vUnit2 = document.getElementById('mv-unit-v').value;
        var v2Val = parseFloat(document.getElementById('mv-v2').value);

        if (isNaN(mVal) || isNaN(tVal2) || isNaN(v1Val) || isNaN(v2Val) || mVal <= 0 || tVal2 <= 0) {
          showError("Mass and duration must be strictly positive real numbers.");
          return;
        }

        var mKg = mVal * MASS_FACTORS[mUnit];
        dt_s = tVal2 * TIME_FACTORS[tUnit2];
        var v1MS = v1Val * VEL_FACTORS[vUnit2];
        var v2MS = v2Val * VEL_FACTORS[vUnit2];
        var dvMS = v2MS - v1MS;

        j_Ns = mKg * Math.abs(dvMS);
        f_N = j_Ns / dt_s;

        var accelMS2 = Math.abs(dvMS) / dt_s;
        var gVal = accelMS2 / 9.80665;
        gforceStr = gVal.toFixed(1) + " g₀";
        gsubStr = "Deceleration: " + accelMS2.toFixed(1) + " m/s²";

        steps = "Mode: Momentum Change (J = m * |Δv| = m * |vf - vi|)\n" +
                "Inputs: m = " + mVal + " " + mUnit + ", vi = " + v1Val + " " + vUnit2.replace('_', '/') + ", vf = " + v2Val + " " + vUnit2.replace('_', '/') + ", Δt = " + tVal2 + " " + tUnit2 + "\n\n" +
                "1. Mass in SI: m = " + mKg.toFixed(2) + " kg\n" +
                "2. Velocity Change: |Δv| = |" + v2MS.toFixed(2) + " - " + v1MS.toFixed(2) + "| = " + Math.abs(dvMS).toFixed(2) + " m/s\n\n" +
                "3. Compute Impulse: J = m * |Δv| = " + mKg.toFixed(2) + " * " + Math.abs(dvMS).toFixed(2) + " = " + j_Ns.toFixed(2) + " N·s\n\n" +
                "4. Average Impact Force: F_avg = J / Δt = " + j_Ns.toFixed(2) + " / " + dt_s.toFixed(4) + "\n" +
                "   F_avg = " + f_N.toFixed(1) + " N (" + (f_N / 1000).toFixed(3) + " kN, " + (f_N / 4.448222).toFixed(1) + " lbf)\n\n" +
                "5. Deceleration: a = |Δv| / Δt = " + accelMS2.toFixed(2) + " m/s² (" + gVal.toFixed(1) + " g₀)";

        document.getElementById('res-primary-val').innerText = j_Ns.toLocaleString(undefined, {maximumFractionDigits: 1}) + " N·s";
        document.getElementById('res-primary-sub').innerText = j_Ns.toLocaleString(undefined, {maximumFractionDigits: 1}) + " kg·m/s • " + (j_Ns / 4.448222).toFixed(1) + " lbf·s";
        document.getElementById('res-f-val').innerText = f_N.toLocaleString(undefined, {maximumFractionDigits: 1}) + " N";
        document.getElementById('res-f-sub').innerText = (f_N / 1000).toFixed(3) + " kN • " + (f_N / 4.448222).toFixed(1) + " lbf";

      } else if (mode === 'solve-force') {
        var jVal = parseFloat(document.getElementById('sf-imp').value);
        var jUnit = document.getElementById('sf-unit-imp').value;
        var tVal3 = parseFloat(document.getElementById('sf-time').value);
        var tUnit3 = document.getElementById('sf-unit-time').value;

        if (isNaN(jVal) || isNaN(tVal3) || jVal < 0 || tVal3 <= 0) {
          showError("Impulse and time must be positive numbers.");
          return;
        }

        j_Ns = jVal * IMP_FACTORS[jUnit];
        dt_s = tVal3 * TIME_FACTORS[tUnit3];
        f_N = j_Ns / dt_s;

        steps = "Mode: Solve Average Force (F = J / Δt)\n" +
                "Inputs: J = " + jVal + " " + jUnit.replace('_', '·') + ", Δt = " + tVal3 + " " + tUnit3 + "\n\n" +
                "1. Impulse in SI: J = " + j_Ns.toFixed(2) + " N·s\n" +
                "2. Duration in SI: Δt = " + dt_s.toFixed(4) + " s (" + (dt_s * 1000).toFixed(1) + " ms)\n\n" +
                "3. Average Impact Force: F_avg = J / Δt = " + j_Ns.toFixed(2) + " / " + dt_s.toFixed(4) + "\n" +
                "   F_avg = " + f_N.toFixed(1) + " N (" + (f_N / 1000).toFixed(3) + " kN, " + (f_N / 4.448222).toFixed(1) + " lbf)";

        document.getElementById('res-primary-val').innerText = f_N.toLocaleString(undefined, {maximumFractionDigits: 1}) + " N";
        document.getElementById('res-primary-sub').innerText = (f_N / 1000).toFixed(3) + " kN • " + (f_N / 4.448222).toFixed(1) + " lbf";
        document.getElementById('res-f-val').innerText = j_Ns.toLocaleString(undefined, {maximumFractionDigits: 1}) + " N·s";
        document.getElementById('res-f-sub').innerText = (j_Ns / 4.448222).toFixed(1) + " lbf·s";
      }

      document.getElementById('res-dp').innerText = j_Ns.toLocaleString(undefined, {maximumFractionDigits: 1}) + " kg·m/s";
      document.getElementById('res-gforce').innerText = gforceStr;
      document.getElementById('res-gsub').innerText = gsubStr;

      document.getElementById('res-steps').innerText = steps;
    }

    function showError(msg) {
      document.getElementById('res-primary-val').innerText = "Error";
      document.getElementById('res-primary-sub').innerText = "Invalid calculation";
      document.getElementById('res-f-val').innerText = "N/A";
      document.getElementById('res-f-sub').innerText = "N/A";
      document.getElementById('res-dp').innerText = "N/A";
      document.getElementById('res-gforce').innerText = "N/A";
      document.getElementById('res-steps').innerText = "Error: " + msg;
    }

    function resetImpulse() {
      document.getElementById('imp-mode').value = 'force-time';
      document.getElementById('ft-force').value = '8500';
      document.getElementById('ft-unit-force').value = 'N';
      document.getElementById('ft-time').value = '25';
      document.getElementById('ft-unit-time').value = 'ms';
      document.getElementById('mv-mass').value = '1400';
      document.getElementById('mv-unit-mass').value = 'kg';
      document.getElementById('mv-dt').value = '120';
      document.getElementById('mv-unit-dt').value = 'ms';
      document.getElementById('mv-v1').value = '20';
      document.getElementById('mv-unit-v').value = 'm_s';
      document.getElementById('mv-v2').value = '0';
      document.getElementById('sf-imp').value = '28000';
      document.getElementById('sf-unit-imp').value = 'N_s';
      document.getElementById('sf-time').value = '80';
      document.getElementById('sf-unit-time').value = 'ms';
      switchImpulseMode();
    }

    window.addEventListener('DOMContentLoaded', function() {
      calculateImpulse();
    });
  </script>
</body>
</html>
"""

# 4. potential-energy-calculator.html
HTML_POTENTIAL_ENERGY = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Potential Energy Calculator - Gravitational &amp; Elastic Spring Energy</title>
  <meta name="description" content="Calculate gravitational potential energy (U = mgh), elastic spring energy (U = 0.5kx²), and free-fall impact velocity with step-by-step physics formulas and proofs.">
  <link rel="canonical" href="https://calchub.org/potential-energy-calculator.html">
  <meta property="og:title" content="Potential Energy Calculator - Gravitational &amp; Elastic Energy Solver">
  <meta property="og:description" content="Free physics potential energy calculator. Solve U = mgh and U = 0.5kx², free fall velocity v = √(2gh), and multi-unit conversions (Joules, kJ, kWh, ft-lbf).">
  <meta property="og:url" content="https://calchub.org/potential-energy-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Potential Energy Calculator - Mechanics &amp; Gravity Solver">
  <meta name="twitter:description" content="Solve gravitational and spring potential energy with full step-by-step proofs, celestial fields, and engineering case studies.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Potential Energy Calculator",
    "url": "https://calchub.org/potential-energy-calculator.html",
    "description": "Calculates gravitational potential energy (U = mgh) and elastic spring potential energy (U = 0.5kx²) across international scientific and engineering units.",
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
        "name": "What is the formula for gravitational potential energy?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Near Earth's surface, gravitational potential energy is calculated using U = m * g * h, where m is mass in kilograms (kg), g is gravitational acceleration (9.80665 m/s^2), and h is vertical elevation height in meters (m). In SI units, energy is measured in Joules (J)."
        }
      },
      {
        "@type": "Question",
        "name": "What is the formula for elastic potential energy in a spring?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Per Hooke's Law, elastic potential energy stored in a deformed spring is U = 0.5 * k * x^2, where k is the spring stiffness constant in Newtons per meter (N/m) and x is displacement from equilibrium in meters (m)."
        }
      },
      {
        "@type": "Question",
        "name": "How does gravitational potential energy convert into velocity during free fall?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "By conservation of mechanical energy (neglecting air drag), potential energy lost equals kinetic energy gained: m * g * h = 0.5 * m * v^2. Canceling mass m yields the Torricelli velocity: v = √(2 * g * h)."
        }
      },
      {
        "@type": "Question",
        "name": "How many Joules are in one kilowatt-hour (kWh)?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "One kilowatt-hour (1 kWh) equals exactly 3,600,000 Joules (3.6 Megajoules, or MJ). It represents one kilowatt of continuous power expended over one full hour."
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
      <div class="calc-icon" aria-hidden="true">&#9883;</div>
      <h1>Potential Energy Calculator</h1>
      <p class="calc-description">Compute gravitational potential energy (\(U = mgh\)), elastic spring energy (\(U = \frac{1}{2}kx^2\)), and free-fall impact velocities across international engineering units.</p>
    </div>

    <div class="calculator-body">
      <div class="input-group">
        <label for="pe-mode">Potential Energy Type</label>
        <select id="pe-mode" class="form-control" onchange="switchPEMode()">
          <option value="gravitational" selected>Gravitational Potential Energy: Mass &amp; Elevation (\(U = mgh\))</option>
          <option value="elastic">Elastic Spring Energy: Stiffness &amp; Displacement (\(U = \frac{1}{2}kx^2\))</option>
        </select>
      </div>

      <!-- Panel: Gravitational U = mgh -->
      <div id="panel-grav">
        <div class="input-grid">
          <div class="input-group">
            <label for="pe-m">Object Mass (\(m\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="pe-m" class="form-control" value="250" step="any" min="0" style="flex: 2;">
              <select id="pe-unit-m" class="form-control" style="flex: 1;" onchange="calculatePE()">
                <option value="kg" selected>kg</option>
                <option value="g">g</option>
                <option value="lb">lb</option>
                <option value="ton">ton</option>
              </select>
            </div>
          </div>

          <div class="input-group">
            <label for="pe-h">Vertical Elevation / Height (\(h\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="pe-h" class="form-control" value="40" step="any" min="0" style="flex: 2;">
              <select id="pe-unit-h" class="form-control" style="flex: 1;" onchange="calculatePE()">
                <option value="m" selected>m</option>
                <option value="ft">ft</option>
                <option value="km">km</option>
                <option value="cm">cm</option>
              </select>
            </div>
          </div>
        </div>

        <div class="input-grid">
          <div class="input-group">
            <label for="pe-celestial">Celestial Gravitational Field</label>
            <select id="pe-celestial" class="form-control" onchange="loadPEGravity()">
              <option value="9.80665" selected>Earth Surface (9.807 m/s²)</option>
              <option value="1.62">Moon (1.620 m/s²)</option>
              <option value="3.71">Mars (3.710 m/s²)</option>
              <option value="24.79">Jupiter (24.79 m/s²)</option>
              <option value="custom">-- Custom Acceleration --</option>
            </select>
          </div>

          <div class="input-group">
            <label for="pe-g">Gravitational Field Strength (\(g\)) [m/s²]</label>
            <input type="number" id="pe-g" class="form-control" value="9.80665" step="any" min="0">
          </div>
        </div>
      </div>

      <!-- Panel: Elastic U = 0.5 k x^2 -->
      <div id="panel-elastic" style="display: none;">
        <div class="input-grid">
          <div class="input-group">
            <label for="el-k">Spring Stiffness Constant (\(k\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="el-k" class="form-control" value="15000" step="any" min="0" style="flex: 2;">
              <select id="el-unit-k" class="form-control" style="flex: 1;" onchange="calculatePE()">
                <option value="N_m" selected>N/m</option>
                <option value="kN_m">kN/m</option>
                <option value="lbf_in">lbf/in</option>
                <option value="lbf_ft">lbf/ft</option>
              </select>
            </div>
          </div>

          <div class="input-group">
            <label for="el-x">Displacement from Equilibrium (\(x\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="el-x" class="form-control" value="0.15" step="any" min="0" style="flex: 2;">
              <select id="el-unit-x" class="form-control" style="flex: 1;" onchange="calculatePE()">
                <option value="m" selected>m</option>
                <option value="cm">cm</option>
                <option value="mm">mm</option>
                <option value="in">in</option>
              </select>
            </div>
          </div>
        </div>
      </div>

      <div class="btn-group">
        <button type="button" class="btn btn-primary" onclick="calculatePE()">Calculate Potential Energy</button>
        <button type="button" class="btn btn-secondary" onclick="resetPE()">Reset Defaults</button>
      </div>

      <!-- Results Display Grid -->
      <div class="results-grid" style="margin-top: 1.5rem;">
        <div class="result-card primary-result">
          <div class="result-label" id="res-primary-label">Potential Energy (\(U\))</div>
          <div class="result-value" id="res-primary-val">98.07 kJ</div>
          <div class="result-subtext" id="res-primary-sub">98,066.50 Joules (N&middot;m)</div>
        </div>

        <div class="result-card">
          <div class="result-label">Kilowatt-Hours (Electrical)</div>
          <div class="result-value" id="res-kwh">0.0272 kWh</div>
          <div class="result-subtext">27.24 Watt-hours</div>
        </div>

        <div class="result-card">
          <div class="result-label">Imperial Foot-Pounds</div>
          <div class="result-value" id="res-ftlb">72,329 ft&middot;lbf</div>
          <div class="result-subtext">23.44 Kilocalories (kcal)</div>
        </div>

        <div class="result-card">
          <div class="result-label" id="res-sec-label">Theoretical Fall Velocity</div>
          <div class="result-value" id="res-sec-val">28.01 m/s</div>
          <div class="result-subtext" id="res-sec-sub">100.83 km/h &bull; 62.66 mph</div>
        </div>
      </div>

      <!-- Equivalent Energy Units Table Card -->
      <div class="info-card" style="margin-top: 1.5rem;">
        <h3>Comprehensive Multi-System Energy Equivalencies</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 0.75rem; margin-top: 0.5rem;">
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">Joules (J)</div>
            <strong id="eq-j">98,067 J</strong>
          </div>
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">Kilojoules (kJ)</div>
            <strong id="eq-kj">98.07 kJ</strong>
          </div>
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">British Thermal Units (BTU)</div>
            <strong id="eq-btu">92.95 BTU</strong>
          </div>
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">Calorie (thermochemical)</div>
            <strong id="eq-cal">23,439 cal</strong>
          </div>
        </div>
      </div>

      <!-- Step-by-step Math Breakdown Card -->
      <div class="info-card" style="margin-top: 1.5rem;">
        <h3>Step-by-Step Physics &amp; Energy Derivation</h3>
        <pre id="res-steps" style="white-space: pre-wrap; font-family: monospace; background: var(--bg-secondary, #f8f9fa); padding: 1rem; border-radius: 6px; font-size: 0.9rem; line-height: 1.5; color: var(--text-primary, #212529);"></pre>
      </div>
    </div>

    <!-- Article Content: 1000+ Words Clinical / Physics Deep Dive -->
    <article class="article-body">
      <h2>The Physics of Potential Energy in Conservative Force Fields</h2>
      <p>
        In classical mechanics, thermodynamics, and astrophysics, <strong>potential energy</strong> (\(U\) or \(E_p\)) is the latent mechanical energy stored within a physical system by virtue of the relative positions, spatial configurations, or internal geometry of its constituent parts. Unlike kinetic energy—which quantifies energy manifested in physical motion—potential energy represents the capacity of conservative forces to perform mechanical work if the system's geometric constraints are released.
      </p>
      <p>
        The concept of potential energy is inseparable from the mathematical definition of a <strong>conservative force field</strong>. A physical force \(\vec{F}\) is strictly conservative if the net work it performs on a particle traversing a closed loop is identically zero (\(\oint \vec{F} \cdot d\vec{r} = 0\)), or equivalently, if the curl of the force field vanishes (\(\nabla \times \vec{F} = 0\)). In any conservative field, force is mathematically defined as the negative spatial gradient of the scalar potential energy function:
      </p>
      $$\vec{F} = -\nabla U = -\left( \frac{\partial U}{\partial x}\hat{i} + \frac{\partial U}{\partial y}\hat{j} + \frac{\partial U}{\partial z}\hat{k} \right)$$
      <p>
        The negative sign physically dictates that natural conservative forces always accelerate matter down the potential gradient—from states of high potential energy toward states of lower potential energy (e.g., masses fall downward toward lower gravitational potential; compressed springs expand outward to relieve elastic stress).
      </p>

      <h2>Mathematical Formulations and Governing Laws</h2>

      <h3>1. Gravitational Potential Energy Near Earth's Surface</h3>
      <p>
        Within a uniform gravitational field where field strength \(g\) is assumed invariant over height interval \(h\), the work required to elevate an object of mass \(m\) against gravity defines its gravitational potential energy:
      </p>
      $$U_g = m \times g \times h$$
      <p>
        Where:
      </p>
      <ul>
        <li>\(U_g\) is gravitational potential energy in Joules (\(\text{J} = \text{N}\cdot\text{m} = \text{kg}\cdot\text{m}^2/\text{s}^2\)).</li>
        <li>\(m\) is the inertial mass of the body in kilograms (\(\text{kg}\)).</li>
        <li>\(g\) is local gravitational acceleration (\(9.80665\text{ m/s}^2\) on Earth's sea-level surface).</li>
        <li>\(h\) is the vertical elevation displacement above an arbitrarily chosen reference datum plane (\(h = 0\)) in meters (\(\text{m}\)).</li>
      </ul>

      <h3>2. Free-Fall Kinetic Energy Conversion (Torricelli's Law)</h3>
      <p>
        Per the Law of Conservation of Mechanical Energy, when an object falls freely from rest at height \(h\) in a vacuum, its entire initial gravitational potential energy converts into translational kinetic energy:
      </p>
      $$U_g = E_k \implies m g h = \frac{1}{2} m v^2$$
      <p>
        Because mass \(m\) appears linearly on both sides, it cancels completely—proving Galileo Galilei's historic 1589 Pisa observation that, neglecting atmospheric air drag, all objects accelerate and strike the ground with identical velocity regardless of their weight:
      </p>
      $$v = \sqrt{2 g h}$$

      <h3>3. Elastic Potential Energy in Hookean Springs</h3>
      <p>
        When an elastic spring or deformable solid complying with Hooke's Law (\(F = -k x\)) is compressed or stretched by distance \(x\) from its natural neutral equilibrium position, the restorative force increases linearly with displacement. Integrating this force over displacement:
      </p>
      $$U_s = \int_0^x k s \, ds = \frac{1}{2} k x^2$$
      <p>
        Where:
      </p>
      <ul>
        <li>\(U_s\) is the stored elastic potential energy in Joules (\(\text{J}\)).</li>
        <li>\(k\) is the spring stiffness constant in Newtons per meter (\(\text{N/m}\)).</li>
        <li>\(x\) is the linear displacement (compression or elongation) in meters (\(\text{m}\)).</li>
      </ul>
      <p>
        Notice that because displacement \(x\) is squared, stored energy is strictly positive regardless of whether the spring is compressed (\(x < 0\)) or extended (\(x > 0\)).
      </p>

      <h2>International Energy Units and Exact Conversion Constants</h2>
      <p>
        Energy is quantified across multiple international disciplines according to thermal, mechanical, electrical, and imperial traditions.
      </p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Energy Unit</th>
            <th>Symbol</th>
            <th>Value in Joules (J)</th>
            <th>Value in Kilowatt-Hours</th>
            <th>Primary Engineering Application</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Joule (SI Coherent)</td>
            <td>J</td>
            <td>1.0 (Exact)</td>
            <td>\(2.77778 \times 10^{-7}\)</td>
            <td>Scientific physics, mechanical work</td>
          </tr>
          <tr>
            <td>Kilojoule</td>
            <td>kJ</td>
            <td>1,000</td>
            <td>\(2.77778 \times 10^{-4}\)</td>
            <td>Chemical bond enthalpies, nutritional kJ</td>
          </tr>
          <tr>
            <td>Megajoule</td>
            <td>MJ</td>
            <td>1,000,000</td>
            <td>0.277778</td>
            <td>Automotive fuel energy, ballistics</td>
          </tr>
          <tr>
            <td>Kilowatt-Hour</td>
            <td>kWh</td>
            <td>3,600,000 (Exact)</td>
            <td>1.0 (Exact)</td>
            <td>Electrical utility billing, EV battery packs</td>
          </tr>
          <tr>
            <td>Foot-Pound Force</td>
            <td>\(\text{ft}\cdot\text{lbf}\)</td>
            <td>1.355818</td>
            <td>\(3.76616 \times 10^{-7}\)</td>
            <td>Imperial structural torque work, rifle muzzle energy</td>
          </tr>
          <tr>
            <td>British Thermal Unit</td>
            <td>BTU (ISO)</td>
            <td>1,055.056</td>
            <td>\(2.93071 \times 10^{-4}\)</td>
            <td>HVAC heating capacity, natural gas billing</td>
          </tr>
          <tr>
            <td>Kilocalorie (Food Calorie)</td>
            <td>kcal</td>
            <td>4,184.0 (Exact)</td>
            <td>0.001162</td>
            <td>Dietary metabolic nutrition, human exercise</td>
          </tr>
          <tr>
            <td>Electron-Volt</td>
            <td>eV</td>
            <td>\(1.602176634 \times 10^{-19}\)</td>
            <td>\(4.45049 \times 10^{-26}\)</td>
            <td>Atomic spectroscopy, semiconductor bandgaps</td>
          </tr>
        </tbody>
      </table>

      <h2>Practical Real-World Engineering Case Studies</h2>

      <div class="worked-example-card">
        <h3>Case Study 1: Pumped-Storage Hydroelectric Dam Grid Energy Reserve</h3>
        <p><strong>Scenario:</strong> A utility-scale pumped-storage hydroelectric plant features an upper mountain reservoir containing \(V = 4,500,000\text{ m}^3\) of water at an average head elevation of \(h = 320\text{ m}\) above its powerhouse turbines. Water density is \(\rho = 1,000\text{ kg/m}^3\). Hydro-turbine generation combined efficiency is \(\eta = 82\%\).</p>
        <p><strong>Objective:</strong> Calculate the gross stored gravitational potential energy and determine the net electrical megawatt-hours (MWh) deliverable to the regional power grid.</p>
        <div class="step-solution">
          <p><strong>1. Reservoir Total Water Mass:</strong></p>
          $$m = V \times \rho = 4,500,000\text{ m}^3 \times 1,000\text{ kg/m}^3 = 4.50 \times 10^9\text{ kg} \text{ (4.50 million metric tons)}$$
          <p><strong>2. Gross Gravitational Potential Energy:</strong></p>
          $$U_g = m g h = 4.50 \times 10^9\text{ kg} \times 9.80665\text{ m/s}^2 \times 320\text{ m} \approx 1.41216 \times 10^{13}\text{ J} = 14.122\text{ TJ (Terajoules)}$$
          <p><strong>3. Net Electrical Grid Energy Output:</strong></p>
          $$E_{\text{elec}} = U_g \times \eta = 1.41216 \times 10^{13}\text{ J} \times 0.82 \approx 1.15797 \times 10^{13}\text{ Joules}$$
          $$\text{Grid Output (MWh)} = \frac{1.15797 \times 10^{13}\text{ J}}{3.60 \times 10^9\text{ J/MWh}} \approx 3,216.58\text{ MWh}$$
          <p>The facility functions as a massive green energy storage battery capable of delivering 400 MW of continuous baseload electric power for over 8 hours during peak demand!</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Civil Construction &ndash; Diesel Drop Hammer Pile Driver</h3>
        <p><strong>Scenario:</strong> A foundation pile driver utilizes a heavy steel ram of mass \(m = 4,200\text{ kg}\) lifted to an elevation height of \(h = 2.40\text{ m}\) above the top of a precast concrete foundation pile. When released, the ram falls freely under gravity before striking the pile cap.</p>
        <p><strong>Objective:</strong> Calculate the potential energy stored prior to release and determine the impact velocity at the exact instant the ram strikes the pile.</p>
        <div class="step-solution">
          <p><strong>1. Stored Potential Energy:</strong></p>
          $$U_g = m g h = 4,200\text{ kg} \times 9.80665\text{ m/s}^2 \times 2.40\text{ m} = 98,851.03\text{ J} \approx 98.85\text{ kJ} \ (72,909\text{ ft}\cdot\text{lbf})$$
          <p><strong>2. Pile Impact Velocity:</strong></p>
          $$v = \sqrt{2 g h} = \sqrt{2 \times 9.80665\text{ m/s}^2 \times 2.40\text{ m}} = \sqrt{47.0719} \approx 6.8609\text{ m/s} \ (24.70\text{ km/h} / 15.35\text{ mph})$$
          <p>At impact, all 98.85 kJ of kinetic energy delivers a compressive shock wave into the pile, driving it into dense geotechnical bedrock strata.</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 3: Automotive Suspension Coil Spring Elastic Energy Storage</h3>
        <p><strong>Scenario:</strong> An off-road vehicle suspension uses a heavy-duty chrome-silicon steel coil spring with spring stiffness rate \(k = 42,000\text{ N/m}\) (\(42\text{ kN/m}\)). When traversing a severe boulder obstacle, the suspension arm compresses the coil spring by \(x = 18.0\text{ cm}\) (\(0.180\text{ m}\)).</p>
        <p><strong>Objective:</strong> Compute the peak compressive resistance force and total elastic strain energy stored in the compressed spring.</p>
        <div class="step-solution">
          <p><strong>1. Peak Compressive Force (Hooke's Law):</strong></p>
          $$F = k \times x = 42,000\text{ N/m} \times 0.180\text{ m} = 7,560\text{ N} \ (7.56\text{ kN} / 1,699.6\text{ lbf})$$
          <p><strong>2. Stored Elastic Potential Energy:</strong></p>
          $$U_s = \frac{1}{2} k x^2 = \frac{1}{2} \times 42,000\text{ N/m} \times (0.180\text{ m})^2 = 21,000 \times 0.0324 = 680.40\text{ Joules} \ (501.84\text{ ft}\cdot\text{lbf})$$
          <p>As the suspension rebounds, hydraulic shock absorbers dissipate this 680 Joules into viscous thermal heat to prevent uncontrolled vehicle chassis bouncing.</p>
        </div>
      </div>

      <h2>Universal Gravitational Potential in Orbital Mechanics</h2>
      <p>
        When considering astronomical distances where gravitational field strength \(g\) falls off with the square of distance, near-surface formula \(U = mgh\) fails. The true universal gravitational potential energy of mass \(m\) at radial distance \(r\) from a celestial body of mass \(M\) is:
      </p>
      $$U(r) = -G \frac{M m}{r}$$
      <p>
        Notice that potential energy is strictly negative, approaching zero as separation distance \(r \to \infty\). This negative value reflects a <strong>gravitational bound state</strong>: external positive energy equal to \(E_{\text{escape}} = G \frac{Mm}{r}\) must be supplied to the object to lift it completely out of the gravitational well to infinity, which directly establishes planetary escape velocity:
      </p>
      $$\frac{1}{2} m v_{\text{esc}}^2 = G \frac{M m}{r} \implies v_{\text{esc}} = \sqrt{\frac{2 G M}{r}}$$

      <h2>Frequently Asked Questions</h2>
      <div class="faq-accordion">
        <details class="faq-item">
          <summary class="faq-question">Why can potential energy assume negative values?</summary>
          <div class="faq-answer">
            <p>Potential energy is physically defined relative to an arbitrarily chosen reference datum. In terrestrial physics, we often choose ground level as \(h = 0\), making elevations above ground positive (\(+mgh\)) and excavations below ground negative (\(-mgh\)). In celestial mechanics, physicists set zero potential at infinite separation (\(r = \infty\)); because gravity is always attractive, bringing masses closer together releases energy, making potential energy negative (\(U = -GMm/r\)) everywhere in space.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">What is the distinction between potential energy and electric potential?</summary>
          <div class="faq-answer">
            <p>Electric potential energy (\(U_e\), in Joules) is the total energy stored by a collection of electrical charges. Electric potential (\(V\), measured in Volts) is the electric potential energy <em>per unit charge</em>: \(V = U_e / q\). Electric potential is an intrinsic property of the electric field at a spatial point, independent of whether a physical charge is placed there.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">Does an elevated object gain mass according to Einstein's mass-energy equivalence?</summary>
          <div class="faq-answer">
            <p>Yes. Per Einstein's mass-energy equivalence equation (\(E = mc^2\)), storing potential energy \(\Delta U\) increases the total relativistic invariant mass of the combined earth-object system by \(\Delta m = \Delta U / c^2\). For lifting a 1,000 kg car by 100 meters (\(U \approx 981,000\text{ J}\)), the mass increase is an imperceptible \(1.09 \times 10^{-11}\text{ grams}\)—undetectable macroscopically, yet fundamentally real.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">How does air drag affect free-fall velocity compared to Torricelli's formula?</summary>
          <div class="faq-answer">
            <p>Torricelli's formula \(v = \sqrt{2gh}\) assumes a pure vacuum with zero friction. In atmospheric air, fluid drag force \(F_d = \frac{1}{2}\rho v^2 C_d A\) opposes downward motion. As falling velocity increases, air resistance grows quadratically until it exactly balances gravitational weight, causing acceleration to cease at terminal velocity: \(v_t = \sqrt{2mg / (\rho C_d A)}\). Real fall velocity is always strictly less than \(\sqrt{2gh}\).</p>
          </div>
        </details>
      </div>

      <!-- Cross-Disciplinary Internal Links -->
      <div class="related-calculators" style="margin-top: 2rem; padding: 1.5rem; background: var(--bg-secondary, #f8f9fa); border-radius: 8px;">
        <h3>Related Physics &amp; Mechanics Calculators</h3>
        <ul style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.75rem; list-style: none; padding: 0;">
          <li><a href="kinetic-energy-calculator.html">&rarr; Kinetic Energy Calculator (Ek = 0.5mv²)</a></li>
          <li><a href="force-calculator.html">&rarr; Force &amp; Newton's Second Law Solver (F = ma)</a></li>
          <li><a href="speed-calculator.html">&rarr; Speed &amp; Kinematics Calculator (v = d/t)</a></li>
          <li><a href="momentum-calculator.html">&rarr; Linear Momentum &amp; Collisions (p = mv)</a></li>
          <li><a href="free-fall-calculator.html">&rarr; Free Fall &amp; Terminal Velocity Calculator</a></li>
          <li><a href="energy-converter.html">&rarr; Universal Energy Unit Converter</a></li>
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
    var MASS_FACTORS = {
      'kg': 1.0,
      'g': 0.001,
      'lb': 0.45359237,
      'ton': 1000.0
    };

    var DIST_FACTORS = {
      'm': 1.0,
      'ft': 0.3048,
      'km': 1000.0,
      'cm': 0.01,
      'mm': 0.001,
      'in': 0.0254
    };

    var K_FACTORS = {
      'N_m': 1.0,
      'kN_m': 1000.0,
      'lbf_in': 175.126835,
      'lbf_ft': 14.593903
    };

    function switchPEMode() {
      var mode = document.getElementById('pe-mode').value;
      document.getElementById('panel-grav').style.display = (mode === 'gravitational') ? 'block' : 'none';
      document.getElementById('panel-elastic').style.display = (mode === 'elastic') ? 'block' : 'none';

      var lbl = document.getElementById('res-primary-label');
      var secLbl = document.getElementById('res-sec-label');
      if (mode === 'elastic') {
        lbl.innerText = "Elastic Spring Energy (Us)";
        secLbl.innerText = "Peak Spring Force";
      } else {
        lbl.innerText = "Gravitational Potential Energy (Ug)";
        secLbl.innerText = "Theoretical Fall Velocity";
      }

      calculatePE();
    }

    function loadPEGravity() {
      var val = document.getElementById('pe-celestial').value;
      if (val !== 'custom') {
        document.getElementById('pe-g').value = val;
        calculatePE();
      }
    }

    function calculatePE() {
      var mode = document.getElementById('pe-mode').value;
      var u_J = 0;
      var secVal = "", secSub = "";
      var steps = "";

      if (mode === 'gravitational') {
        var mVal = parseFloat(document.getElementById('pe-m').value);
        var mUnit = document.getElementById('pe-unit-m').value;
        var hVal = parseFloat(document.getElementById('pe-h').value);
        var hUnit = document.getElementById('pe-unit-h').value;
        var gVal = parseFloat(document.getElementById('pe-g').value);

        if (isNaN(mVal) || isNaN(hVal) || isNaN(gVal) || mVal < 0 || hVal < 0 || gVal < 0) {
          showError("Mass, elevation, and gravity must be non-negative real numbers.");
          return;
        }

        var mKg = mVal * MASS_FACTORS[mUnit];
        var hM = hVal * DIST_FACTORS[hUnit];
        u_J = mKg * gVal * hM;

        var v_ms = Math.sqrt(2 * gVal * hM);
        secVal = v_ms.toFixed(2) + " m/s";
        secSub = (v_ms * 3.6).toFixed(2) + " km/h • " + (v_ms / 0.44704).toFixed(2) + " mph";

        steps = "Mode: Gravitational Potential Energy (U = m * g * h)\n" +
                "Inputs: Mass m = " + mVal + " " + mUnit + ", Height h = " + hVal + " " + hUnit + ", g = " + gVal + " m/s²\n\n" +
                "1. Mass in SI: m = " + mKg.toFixed(4) + " kg\n" +
                "2. Height in SI: h = " + hM.toFixed(4) + " m\n\n" +
                "3. Compute Potential Energy: U = m * g * h\n" +
                "   U = " + mKg.toFixed(4) + " * " + gVal + " * " + hM.toFixed(4) + "\n" +
                "   U = " + u_J.toFixed(2) + " Joules (" + (u_J / 1000).toFixed(3) + " kJ, " + (u_J / 3600000).toFixed(5) + " kWh)\n\n" +
                "4. Torricelli Free-Fall Velocity: v = √(2gh) = √(2 * " + gVal + " * " + hM.toFixed(2) + ")\n" +
                "   v = " + v_ms.toFixed(3) + " m/s (" + (v_ms * 3.6).toFixed(2) + " km/h, " + (v_ms / 0.44704).toFixed(2) + " mph)";

      } else if (mode === 'elastic') {
        var kVal = parseFloat(document.getElementById('el-k').value);
        var kUnit = document.getElementById('el-unit-k').value;
        var xVal = parseFloat(document.getElementById('el-x').value);
        var xUnit = document.getElementById('el-unit-x').value;

        if (isNaN(kVal) || isNaN(xVal) || kVal < 0 || xVal < 0) {
          showError("Spring constant and displacement must be non-negative.");
          return;
        }

        var kNM = kVal * K_FACTORS[kUnit];
        var xM = xVal * DIST_FACTORS[xUnit];
        u_J = 0.5 * kNM * xM * xM;

        var fPeakN = kNM * xM;
        secVal = fPeakN.toFixed(1) + " N";
        secSub = (fPeakN / 1000).toFixed(3) + " kN • " + (fPeakN / 4.448222).toFixed(1) + " lbf";

        steps = "Mode: Elastic Spring Potential Energy (U = 0.5 * k * x²)\n" +
                "Inputs: Stiffness k = " + kVal + " " + kUnit.replace('_', '/') + ", Displacement x = " + xVal + " " + xUnit + "\n\n" +
                "1. Spring Constant in SI: k = " + kNM.toFixed(2) + " N/m\n" +
                "2. Displacement in SI: x = " + xM.toFixed(4) + " m\n\n" +
                "3. Compute Elastic Energy: U = 0.5 * k * x²\n" +
                "   U = 0.5 * " + kNM.toFixed(2) + " * (" + xM.toFixed(4) + ")²\n" +
                "   U = " + u_J.toFixed(2) + " Joules (" + (u_J / 1000).toFixed(3) + " kJ)\n\n" +
                "4. Peak Spring Force: F = k * x = " + fPeakN.toFixed(2) + " N (" + (fPeakN / 4.448222).toFixed(2) + " lbf)";
      }

      var kj = u_J / 1000.0;
      var kwh = u_J / 3600000.0;
      var ftlb = u_J / 1.355818;
      var kcal = u_J / 4184.0;
      var btu = u_J / 1055.056;

      document.getElementById('res-primary-val').innerText = (kj >= 1000) ? (kj / 1000).toFixed(3) + " MJ" : kj.toFixed(2) + " kJ";
      document.getElementById('res-primary-sub').innerText = u_J.toLocaleString(undefined, {maximumFractionDigits: 1}) + " Joules (N·m)";
      document.getElementById('res-kwh').innerText = kwh.toFixed(4) + " kWh";
      document.getElementById('res-ftlb').innerText = Math.round(ftlb).toLocaleString() + " ft·lbf";
      document.getElementById('res-sec-val').innerText = secVal;
      document.getElementById('res-sec-sub').innerText = secSub;

      document.getElementById('eq-j').innerText = u_J.toLocaleString(undefined, {maximumFractionDigits: 0}) + " J";
      document.getElementById('eq-kj').innerText = kj.toFixed(2) + " kJ";
      document.getElementById('eq-btu').innerText = btu.toFixed(2) + " BTU";
      document.getElementById('eq-cal').innerText = Math.round(u_J / 4.184).toLocaleString() + " cal";

      document.getElementById('res-steps').innerText = steps;
    }

    function showError(msg) {
      document.getElementById('res-primary-val').innerText = "Error";
      document.getElementById('res-primary-sub').innerText = "Invalid calculation";
      document.getElementById('res-kwh').innerText = "N/A";
      document.getElementById('res-ftlb').innerText = "N/A";
      document.getElementById('res-sec-val').innerText = "N/A";
      document.getElementById('res-sec-sub').innerText = "N/A";
      document.getElementById('res-steps').innerText = "Error: " + msg;
    }

    function resetPE() {
      document.getElementById('pe-mode').value = 'gravitational';
      document.getElementById('pe-m').value = '250';
      document.getElementById('pe-unit-m').value = 'kg';
      document.getElementById('pe-h').value = '40';
      document.getElementById('pe-unit-h').value = 'm';
      document.getElementById('pe-celestial').value = '9.80665';
      document.getElementById('pe-g').value = '9.80665';
      document.getElementById('el-k').value = '15000';
      document.getElementById('el-unit-k').value = 'N_m';
      document.getElementById('el-x').value = '0.15';
      document.getElementById('el-unit-x').value = 'm';
      switchPEMode();
    }

    window.addEventListener('DOMContentLoaded', function() {
      calculatePE();
    });
  </script>
</body>
</html>
"""

def generate_part2():
    f3 = os.path.join(BASE_DIR, "impulse-calculator.html")
    with open(f3, "w", encoding="utf-8") as fp:
        fp.write(HTML_IMPULSE.strip() + "\n")
    print(f"Generated: {f3}")

    f4 = os.path.join(BASE_DIR, "potential-energy-calculator.html")
    with open(f4, "w", encoding="utf-8") as fp:
        fp.write(HTML_POTENTIAL_ENERGY.strip() + "\n")
    print(f"Generated: {f4}")

if __name__ == "__main__":
    generate_part2()
