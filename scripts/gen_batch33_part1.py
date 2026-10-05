# -*- coding: utf-8 -*-
"""
Generator for Batch 33 - Part 1:
1. force-calculator.html
2. momentum-calculator.html
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 1. force-calculator.html
HTML_FORCE = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Force Calculator - Newton's Second Law (F = ma) &amp; Gravitational Force</title>
  <meta name="description" content="Calculate force, mass, or acceleration using Newton's Second Law (F = ma). Computes gravitational weight, universal gravitation, and multi-unit conversions (N, kN, lbf, kgf).">
  <link rel="canonical" href="https://calchub.org/force-calculator.html">
  <meta property="og:title" content="Force Calculator - Newton's Laws &amp; Gravitational Force Solver">
  <meta property="og:description" content="Free physics force calculator. Solve F = ma, gravitational weight across celestial bodies, and universal planetary gravitation with step-by-step mathematical proofs.">
  <meta property="og:url" content="https://calchub.org/force-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Force Calculator - Classical Dynamics &amp; Gravitation Solver">
  <meta name="twitter:description" content="Calculate force, mass, and acceleration with multi-unit conversions (N, kN, lbf, kgf, dynes) and worked engineering case studies.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Force Calculator",
    "url": "https://calchub.org/force-calculator.html",
    "description": "Calculates net mechanical force, gravitational weight, and mutual planetary gravitational attraction across SI and imperial engineering units.",
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
        "name": "What is the formula for calculating force?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Per Newton's Second Law of Motion, net force is the product of mass and acceleration: F = m * a, where F is force in Newtons (N), m is mass in kilograms (kg), and a is acceleration in meters per second squared (m/s^2)."
        }
      },
      {
        "@type": "Question",
        "name": "How is weight distinguished from mass in physics?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Mass is an intrinsic measure of the quantity of matter and inertia in an object (measured in kg), which remains invariant anywhere in the universe. Weight is the gravitational downward force exerted on that mass by a celestial body: W = m * g (measured in Newtons or pounds-force)."
        }
      },
      {
        "@type": "Question",
        "name": "How many Newtons are in one pound-force (lbf)?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "One pound-force (1 lbf) equals exactly 4.448221615 Newtons. Conversely, 1 Newton equals approximately 0.224809 pounds-force."
        }
      },
      {
        "@type": "Question",
        "name": "What is Newton's Law of Universal Gravitation?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Every point mass attracts every other point mass by a force acting along the line intersecting their centers: F = G * (m1 * m2) / r^2, where G is the gravitational constant (6.67430 x 10^-11 N*m^2/kg^2) and r is the distance separating their centers of mass."
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
      <h1>Force Calculator</h1>
      <p class="calc-description">Solve for force, mass, or acceleration using Newton's Second Law (\(F = ma\)), compute gravitational weight across celestial bodies, or calculate universal planetary gravitation.</p>
    </div>

    <div class="calculator-body">
      <div class="input-group">
        <label for="force-mode">Force Model</label>
        <select id="force-mode" class="form-control" onchange="switchForceMode()">
          <option value="newton2" selected>Newton's Second Law: Acceleration (\(F = m \times a\))</option>
          <option value="weight">Gravitational Weight (\(W = m \times g\))</option>
          <option value="gravitation">Universal Gravitation (\(F = G \frac{m_1 m_2}{r^2}\))</option>
        </select>
      </div>

      <!-- Panel: Newton's Second Law F = ma -->
      <div id="panel-newton2">
        <div class="input-group">
          <label for="solve-target">Variable to Calculate</label>
          <select id="solve-target" class="form-control" onchange="switchSolveTarget()">
            <option value="force" selected>Net Force (\(F = m \times a\))</option>
            <option value="mass">Mass (\(m = F / a\))</option>
            <option value="accel">Acceleration (\(a = F / m\))</option>
          </select>
        </div>

        <div class="input-grid">
          <div class="input-group" id="grp-mass">
            <label for="inp-mass">Mass (\(m\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="inp-mass" class="form-control" value="1200" step="any" min="0" style="flex: 2;">
              <select id="unit-mass" class="form-control" style="flex: 1;" onchange="calculateForce()">
                <option value="kg" selected>kg</option>
                <option value="g">g</option>
                <option value="lb">lb</option>
                <option value="oz">oz</option>
                <option value="ton">ton (metric)</option>
              </select>
            </div>
          </div>

          <div class="input-group" id="grp-accel">
            <label for="inp-accel">Acceleration (\(a\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="inp-accel" class="form-control" value="4.5" step="any" style="flex: 2;">
              <select id="unit-accel" class="form-control" style="flex: 1;" onchange="calculateForce()">
                <option value="m_s2" selected>m/s²</option>
                <option value="ft_s2">ft/s²</option>
                <option value="g0">g₀ (Standard)</option>
                <option value="km_h_s">km/h per s</option>
              </select>
            </div>
          </div>

          <div class="input-group" id="grp-force" style="display: none;">
            <label for="inp-force">Applied Force (\(F\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="inp-force" class="form-control" value="5400" step="any" style="flex: 2;">
              <select id="unit-force" class="form-control" style="flex: 1;" onchange="calculateForce()">
                <option value="N" selected>N</option>
                <option value="kN">kN</option>
                <option value="lbf">lbf</option>
                <option value="kgf">kgf</option>
              </select>
            </div>
          </div>
        </div>
      </div>

      <!-- Panel: Weight W = mg -->
      <div id="panel-weight" style="display: none;">
        <div class="input-grid">
          <div class="input-group">
            <label for="wt-mass">Object Mass (\(m\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="wt-mass" class="form-control" value="75" step="any" min="0" style="flex: 2;">
              <select id="wt-unit-mass" class="form-control" style="flex: 1;" onchange="calculateForce()">
                <option value="kg" selected>kg</option>
                <option value="lb">lb</option>
                <option value="g">g</option>
              </select>
            </div>
          </div>

          <div class="input-group">
            <label for="wt-body">Celestial Body Gravitational Field</label>
            <select id="wt-body" class="form-control" onchange="loadCelestialBody()">
              <option value="9.80665" selected>Earth Surface (9.807 m/s² &bull; 1.00 g₀)</option>
              <option value="1.62">Moon (1.620 m/s² &bull; 0.165 g₀)</option>
              <option value="3.71">Mars (3.710 m/s² &bull; 0.378 g₀)</option>
              <option value="24.79">Jupiter (24.79 m/s² &bull; 2.528 g₀)</option>
              <option value="8.87">Venus (8.870 m/s² &bull; 0.905 g₀)</option>
              <option value="274.0">Sun Surface (274.0 m/s² &bull; 27.9 g₀)</option>
              <option value="custom">-- Custom Acceleration --</option>
            </select>
          </div>
        </div>

        <div class="input-group">
          <label for="wt-g">Gravitational Acceleration (\(g\)) [m/s²]</label>
          <input type="number" id="wt-g" class="form-control" value="9.80665" step="any" min="0">
        </div>
      </div>

      <!-- Panel: Universal Gravitation -->
      <div id="panel-gravitation" style="display: none;">
        <div class="input-grid">
          <div class="input-group">
            <label for="grav-m1">Mass of Body 1 (\(m_1\)) [kg]</label>
            <input type="number" id="grav-m1" class="form-control" value="5.972e24" step="any" min="0">
            <small style="color: var(--text-muted, #6c757d);">e.g. Earth Mass: 5.972e24 kg</small>
          </div>

          <div class="input-group">
            <label for="grav-m2">Mass of Body 2 (\(m_2\)) [kg]</label>
            <input type="number" id="grav-m2" class="form-control" value="7.348e22" step="any" min="0">
            <small style="color: var(--text-muted, #6c757d);">e.g. Moon Mass: 7.348e22 kg</small>
          </div>
        </div>

        <div class="input-group">
          <label for="grav-r">Distance Between Centers (\(r\)) [meters]</label>
          <input type="number" id="grav-r" class="form-control" value="384400000" step="any" min="0">
          <small style="color: var(--text-muted, #6c757d);">e.g. Earth-Moon Distance: 3.844e8 meters</small>
        </div>
      </div>

      <div class="btn-group">
        <button type="button" class="btn btn-primary" onclick="calculateForce()">Calculate Force</button>
        <button type="button" class="btn btn-secondary" onclick="resetForce()">Reset Defaults</button>
      </div>

      <!-- Results Display Grid -->
      <div class="results-grid" style="margin-top: 1.5rem;">
        <div class="result-card primary-result">
          <div class="result-label" id="res-primary-label">Calculated Force (SI Base)</div>
          <div class="result-value" id="res-primary-val">5,400.00 N</div>
          <div class="result-subtext" id="res-primary-sub">5.40 kN &bull; 1,213.97 lbf</div>
        </div>

        <div class="result-card">
          <div class="result-label">Engineering Kilonewtons</div>
          <div class="result-value" id="res-kn">5.400 kN</div>
          <div class="result-subtext">5,400.0 kg&middot;m/s²</div>
        </div>

        <div class="result-card">
          <div class="result-label">Imperial Pound-Force</div>
          <div class="result-value" id="res-lbf">1,213.97 lbf</div>
          <div class="result-subtext">1.214 kips (1,000 lbf)</div>
        </div>

        <div class="result-card">
          <div class="result-label">Gravitational Kilogram-Force</div>
          <div class="result-value" id="res-kgf">550.65 kgf</div>
          <div class="result-subtext">5.40 &times; 10⁸ Dynes</div>
        </div>
      </div>

      <!-- Equivalent Units Table Card -->
      <div class="info-card" style="margin-top: 1.5rem;">
        <h3>Equivalent Multi-System Force Units</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 0.75rem; margin-top: 0.5rem;">
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">Newtons (N)</div>
            <strong id="eq-n">5,400 N</strong>
          </div>
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">Pound-Force (lbf)</div>
            <strong id="eq-lbf">1,213.97 lbf</strong>
          </div>
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">Dynes (dyn)</div>
            <strong id="eq-dyn">5.40 &times; 10⁸ dyn</strong>
          </div>
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">Poundals (pdl)</div>
            <strong id="eq-pdl">39,058.2 pdl</strong>
          </div>
        </div>
      </div>

      <!-- Step-by-step Math Breakdown Card -->
      <div class="info-card" style="margin-top: 1.5rem;">
        <h3>Step-by-Step Physics &amp; Dimensional Derivation</h3>
        <pre id="res-steps" style="white-space: pre-wrap; font-family: monospace; background: var(--bg-secondary, #f8f9fa); padding: 1rem; border-radius: 6px; font-size: 0.9rem; line-height: 1.5; color: var(--text-primary, #212529);"></pre>
      </div>
    </div>

    <!-- Article Content: 1000+ Words Clinical / Physics Deep Dive -->
    <article class="article-body">
      <h2>The Physical Foundations of Mechanical Force in Classical Dynamics</h2>
      <p>
        In classical Newtonian mechanics, astrophysics, and structural engineering, <strong>force</strong> (\(F\)) is the fundamental physical vector interaction that, when unopposed, alters the motion of a physical body. A force can cause an object with mass to change its velocity—which includes transitioning from a state of rest to motion, accelerating, decelerating, or altering its spatial direction. Beyond kinematic changes, force also induces mechanical deformation, internal stress, and elastic strain within solid bodies.
      </p>
      <p>
        Formulated by Sir Isaac Newton in his masterwork <em>Philosophiae Naturalis Principia Mathematica</em> (1687), the laws of motion transformed physics from qualitative philosophy into an exact, predictive quantitative science. Today, force computations govern modern civilization: civil engineers analyze structural dead and live loads to prevent bridge collapse; aerospace engineers calculate engine thrust-to-weight ratios to escape planetary gravity; biomechanists evaluate joint contact forces to design orthopedic implants; and automotive designers tune crash crumple zones to minimize deceleration impact forces on vehicle occupants.
      </p>

      <h2>Mathematical Formulations and Governing Laws</h2>

      <h3>1. Newton's Second Law of Motion</h3>
      <p>
        Newton's Second Law states that the time rate of change of an object's linear momentum is directly proportional to the applied net force and occurs in the direction of that force. For a body with constant mass \(m\), this simplifies to the famous linear relation:
      </p>
      $$\vec{F}_{\text{net}} = m \vec{a}$$
      <p>
        Where:
      </p>
      <ul>
        <li>\(\vec{F}_{\text{net}}\) is the vector sum of all external forces acting on the body, measured in Newtons (\(\text{N}\)). One Newton is defined as the force required to accelerate a one-kilogram mass at a rate of one meter per second squared (\(1\text{ N} = 1\text{ kg}\cdot\text{m/s}^2\)).</li>
        <li>\(m\) is the inertial mass of the object in kilograms (\(\text{kg}\)), quantifying its resistance to acceleration.</li>
        <li>\(\vec{a}\) is the resulting acceleration vector in meters per second squared (\(\text{m/s}^2\)).</li>
      </ul>

      <h3>Algebraic Rearrangements for Mass and Acceleration</h3>
      <p>
        When different dynamic parameters are measured experimentally, the governing equation is algebraically transposed:
      </p>
      <p><strong>Solving for Acceleration:</strong></p>
      $$a = \frac{F_{\text{net}}}{m}$$
      <p><strong>Solving for Inertial Mass:</strong></p>
      $$m = \frac{F_{\text{net}}}{a}$$

      <h3>2. Gravitational Weight Force</h3>
      <p>
        Weight (\(W\)) is the downward gravitational force exerted on an object by a massive planetary body:
      </p>
      $$W = m \times g$$
      <p>
        Where \(g\) is the local gravitational field strength. On the surface of Earth, standard gravitational acceleration is standardized by international agreement as \(g_0 = 9.80665\text{ m/s}^2\) (\(32.1740\text{ ft/s}^2\)). Because \(g\) depends on planetary mass and radius, an astronaut with a mass of \(80\text{ kg}\) weighs \(784.5\text{ N}\) on Earth, but only \(129.6\text{ N}\) on the Moon (\(g = 1.62\text{ m/s}^2\)) and \(296.8\text{ N}\) on Mars (\(g = 3.71\text{ m/s}^2\)), despite retaining an identical \(80\text{ kg}\) of mass.
      </p>

      <h3>3. Newton's Law of Universal Gravitation</h3>
      <p>
        Across cosmic distances, mutual gravitational attraction between any two discrete bodies is governed by Newton's inverse-square law:
      </p>
      $$F_g = G \frac{m_1 m_2}{r^2}$$
      <p>
        Where:
      </p>
      <ul>
        <li>\(G\) is the Newtonian constant of gravitation, empirically established as \(6.67430(15) \times 10^{-11}\text{ N}\cdot\text{m}^2/\text{kg}^2\).</li>
        <li>\(m_1\) and \(m_2\) are the interacting masses in kilograms.</li>
        <li>\(r\) is the distance separating their respective centers of mass in meters.</li>
      </ul>

      <h2>International Force Units and Exact Conversion Constants</h2>
      <p>
        Because mechanical engineering originated across disparate industrial traditions, engineers routinely convert between metric SI units, imperial gravitational units, and astronomical magnitudes.
      </p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Force Unit</th>
            <th>Symbol</th>
            <th>Value in Newtons (N)</th>
            <th>Value in Pound-Force (lbf)</th>
            <th>Standard Engineering Domain</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Newton (SI Base Derived)</td>
            <td>N</td>
            <td>1.0 (Exact)</td>
            <td>0.224809</td>
            <td>Scientific research, robotics, general physics</td>
          </tr>
          <tr>
            <td>Kilonewton</td>
            <td>kN</td>
            <td>1,000</td>
            <td>224.809</td>
            <td>Structural civil engineering, concrete prestressing</td>
          </tr>
          <tr>
            <td>Meganewton</td>
            <td>MN</td>
            <td>1,000,000</td>
            <td>224,809</td>
            <td>Rocket propulsion thrust, naval ship bollard pull</td>
          </tr>
          <tr>
            <td>Pound-force (Avoirdupois)</td>
            <td>lbf</td>
            <td>4.448222</td>
            <td>1.0 (Exact)</td>
            <td>US aerospace, automotive horsepower, HVAC</td>
          </tr>
          <tr>
            <td>Kip (Kilopound)</td>
            <td>kip</td>
            <td>4,448.222</td>
            <td>1,000</td>
            <td>US structural building design, bridge cable tension</td>
          </tr>
          <tr>
            <td>Kilogram-force (Kilopond)</td>
            <td>kgf / kp</td>
            <td>9.80665 (Exact)</td>
            <td>2.204623</td>
            <td>Legacy European engineering, crane load limits</td>
          </tr>
          <tr>
            <td>Dyne (CGS Metric)</td>
            <td>dyn</td>
            <td>\(1.0 \times 10^{-5}\)</td>
            <td>\(2.248 \times 10^{-6}\)</td>
            <td>Surface tension, microfluidics, biological cell mechanics</td>
          </tr>
          <tr>
            <td>Poundal (Imperial Absolute)</td>
            <td>pdl</td>
            <td>0.138255</td>
            <td>0.031081</td>
            <td>Theoretical imperial mechanics (1 lb accelerated at 1 ft/s²)</td>
          </tr>
        </tbody>
      </table>

      <h2>Benchmark Physical Forces Across the Universe</h2>
      <p>
        To contextualize force magnitudes across atomic, biological, industrial, and astrophysical scales:
      </p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Physical Interaction / Phenomenon</th>
            <th>Approximate Force (Newtons)</th>
            <th>Description &amp; Context</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Single Optical Laser Photon Pressure</td>
            <td>\(10^{-18}\text{ N}\)</td>
            <td>Radiation pressure on microscopic dust particles</td>
          </tr>
          <tr>
            <td>DNA Double-Helix Rupture Force</td>
            <td>\(5 \times 10^{-11}\text{ N}\)</td>
            <td>Optical tweezer single-molecule biophysics</td>
          </tr>
          <tr>
            <td>Mosquito Landing on Human Skin</td>
            <td>\(2 \times 10^{-5}\text{ N}\)</td>
            <td>Sensory threshold for tactile cutaneous mechanoreceptors</td>
          </tr>
          <tr>
            <td>Small Apple Weight on Earth (\(102\text{ g}\))</td>
            <td>1.0 N</td>
            <td>Classic intuitive benchmark for 1 Newton of gravitational force</td>
          </tr>
          <tr>
            <td>Human Handshake Grip Strength</td>
            <td>300 &ndash; 500 N</td>
            <td>Isometric dynamometer clinical physical therapy norm</td>
          </tr>
          <tr>
            <td>Adult Human Biting Force (Molars)</td>
            <td>700 &ndash; 1,100 N</td>
            <td>Masseter and temporalis muscular contraction</td>
          </tr>
          <tr>
            <td>Compact Passenger Car Braking Force</td>
            <td>8,000 &ndash; 12,000 N</td>
            <td>Four-wheel emergency ABS stop on dry asphalt (\(0.8 - 1.0\text{ g}\))</td>
          </tr>
          <tr>
            <td>SpaceX Merlin 1D Rocket Engine Thrust</td>
            <td>845,000 N (845 kN)</td>
            <td>Single Falcon 9 sea-level rocket engine at full throttle</td>
          </tr>
          <tr>
            <td>Earth-Moon Gravitational Attraction</td>
            <td>\(1.98 \times 10^{20}\text{ N}\)</td>
            <td>Mutual orbital binding force driving ocean tidal bulges</td>
          </tr>
        </tbody>
      </table>

      <h2>Practical Real-World Engineering Case Studies</h2>

      <div class="worked-example-card">
        <h3>Case Study 1: Aerospace Rocket Launch Thrust-to-Weight Dynamics</h3>
        <p><strong>Scenario:</strong> A two-stage orbital satellite launch vehicle has a total gross liftoff mass of \(m = 420,000\text{ kg}\) (420 metric tons). Its first-stage rocket cluster produces a combined sea-level thrust of \(F_{\text{thrust}} = 5,880\text{ kN}\) (\(5,880,000\text{ N}\)). Local gravitational acceleration is \(g = 9.80665\text{ m/s}^2\).</p>
        <p><strong>Objective:</strong> Compute the vehicle's initial Thrust-to-Weight Ratio (TWR), net upward launch force, and initial vertical liftoff acceleration.</p>
        <div class="step-solution">
          <p><strong>1. Gravitational Weight Force at Liftoff:</strong></p>
          $$W = m \times g = 420,000\text{ kg} \times 9.80665\text{ m/s}^2 = 4,118,793\text{ N} \approx 4.119\text{ MN}$$
          <p><strong>2. Thrust-to-Weight Ratio (TWR):</strong></p>
          $$\text{TWR} = \frac{F_{\text{thrust}}}{W} = \frac{5,880,000\text{ N}}{4,118,793\text{ N}} \approx 1.428$$
          <p>Because \(\text{TWR} > 1.0\), the rocket possesses sufficient thrust margin to accelerate upward against gravity.</p>
          <p><strong>3. Net Force and Vertical Acceleration:</strong></p>
          $$F_{\text{net}} = F_{\text{thrust}} - W = 5,880,000\text{ N} - 4,118,793\text{ N} = 1,761,207\text{ N} \approx 1.761\text{ MN}$$
          $$a_{\text{liftoff}} = \frac{F_{\text{net}}}{m} = \frac{1,761,207\text{ N}}{420,000\text{ kg}} \approx 4.193\text{ m/s}^2 \ (0.428\text{ g}_0)$$
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Structural Elevator Cable Tension Under Dynamic Acceleration</h3>
        <p><strong>Scenario:</strong> A commercial high-rise traction elevator carries a fully loaded cab and passenger mass of \(m = 2,400\text{ kg}\). The motor control system accelerates the elevator upward from the ground lobby at \(a = 1.80\text{ m/s}^2\). The safety code specifies that the suspension wire ropes must maintain a minimum safety factor of \(SF = 6.0\).</p>
        <p><strong>Objective:</strong> Calculate dynamic cable tension during upward acceleration and determine the minimum rated breaking strength required for the wire rope bundle.</p>
        <div class="step-solution">
          <p><strong>1. Free-Body Dynamic Tension:</strong></p>
          <p>Applying Newton's Second Law upward: \(T - mg = ma \implies T = m(g + a)\):</p>
          $$T = 2,400\text{ kg} \times (9.80665\text{ m/s}^2 + 1.80\text{ m/s}^2) = 2,400 \times 11.60665 = 27,855.96\text{ N} \approx 27.86\text{ kN} \ (6,262.3\text{ lbf})$$
          <p>Dynamic upward acceleration increases cable tension by 18.35% above static rest weight (\(23.54\text{ kN}\)).</p>
          <p><strong>2. Minimum Breaking Strength Specification:</strong></p>
          $$T_{\text{break, min}} = T \times SF = 27.856\text{ kN} \times 6.0 = 167.14\text{ kN} \ (37,574\text{ lbf})$$
          <p>The elevator engineer specifies an array of high-strength steel wire ropes with a combined breaking capacity exceeding \(170\text{ kN}\).</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 3: Automotive High-Performance Braking Force &amp; Road Adhesion</h3>
        <p><strong>Scenario:</strong> A sports sedan of total curb mass \(m = 1,650\text{ kg}\) travels at an initial highway speed of \(v_0 = 108\text{ km/h}\) (\(30.0\text{ m/s}\)). The driver executes an emergency stop, bringing the vehicle to a full halt (\(v_f = 0\)) over a braking distance of \(d = 36.0\text{ m}\).</p>
        <p><strong>Objective:</strong> Compute the average braking deceleration, total net stopping force exerted by tire-road friction, and the minimum required friction coefficient \(\mu\).</p>
        <div class="step-solution">
          <p><strong>1. Kinematic Deceleration:</strong></p>
          $$v_f^2 = v_0^2 + 2 a d \implies 0 = 30.0^2 + 2 a (36.0) \implies a = -\frac{900}{72.0} = -12.50\text{ m/s}^2 \ (-1.275\text{ g}_0)$$
          <p><strong>2. Net Stopping Force:</strong></p>
          $$F_{\text{braking}} = m \times |a| = 1,650\text{ kg} \times 12.50\text{ m/s}^2 = 20,625\text{ N} = 20.625\text{ kN} \ (4,636.7\text{ lbf})$$
          <p><strong>3. Required Road Friction Coefficient (\(\mu\)):</strong></p>
          $$\mu = \frac{F_{\text{braking}}}{W} = \frac{20,625\text{ N}}{1,650\text{ kg} \times 9.80665\text{ m/s}^2} = \frac{20,625}{16,181} \approx 1.275$$
          <p>Stopping in 36 meters from 108 km/h requires ultra-high-performance sticky compound tires generating aerodynamic downforce or \(\mu > 1.25\) on pristine dry asphalt.</p>
        </div>
      </div>

      <h2>The Four Fundamental Interactions of Physics</h2>
      <p>
        In modern quantum field theory and general relativity, all macroscopic forces (tension, normal contact, friction, buoyancy, and elasticity) are manifestations of just four fundamental physical forces:
      </p>
      <ul>
        <li><strong>Gravitation:</strong> Infinite in range, universally attractive, governs planetary orbits and cosmological structure. Relative strength: \(10^{-38}\).</li>
        <li><strong>Electromagnetism:</strong> Governed by Maxwell's equations and quantum electrodynamics (QED). It mediates chemical bonding, atomic lattice structures, and all mechanical contact forces. Relative strength: \(10^{-2}\).</li>
        <li><strong>Weak Nuclear Force:</strong> Governs radioactive beta decay, neutrino interactions, and solar stellar fusion. Range: \(&lt; 10^{-18}\text{ m}\). Relative strength: \(10^{-13}\).</li>
        <li><strong>Strong Nuclear Force:</strong> Mediated by gluons in quantum chromodynamics (QCD). Binds quarks into nucleons and holds atomic nuclei together against electromagnetic repulsion. Relative strength: \(1.0\).</li>
      </ul>

      <h2>Frequently Asked Questions</h2>
      <div class="faq-accordion">
        <details class="faq-item">
          <summary class="faq-question">Why does an object in free fall experience zero net perceived weight?</summary>
          <div class="faq-answer">
            <p>Per Einstein's Equivalence Principle, an observer inside a freely falling frame (such as the International Space Station or a dropped elevator) accelerates at the identical rate as their enclosure. Because no normal supporting contact force pushes back against the body's feet, the perceived apparent weight measured on a scale is exactly zero, producing the sensation of weightlessness (microgravity), even though gravitational pull remains near 90% of sea level.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">What is the distinction between contact forces and action-at-a-distance field forces?</summary>
          <div class="faq-answer">
            <p>Contact forces occur when physical matter directly collides or touches at macroscopic interfaces (friction, normal force, tension, air resistance). Field forces act across spatial vacuums without physical contact via fundamental fields (gravitational attraction, electrostatic Coulomb forces, and magnetic Lorentz forces).</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">How does d'Alembert's principle transform dynamic force problems into statics?</summary>
          <div class="faq-answer">
            <p>D'Alembert's principle introduces an imaginary "inertial force" equal to \(-m\vec{a}\). By adding this reversed effective force vector to the real applied external forces, a dynamic accelerating system satisfies static equilibrium: \(\sum \vec{F} - m\vec{a} = 0\), allowing engineers to solve complex dynamic machinery using straightforward static force and moment balances.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">Can force exist without acceleration?</summary>
          <div class="faq-answer">
            <p>Yes. When multiple forces act on a body in static equilibrium, their vector sum is zero (\(\sum \vec{F} = 0\)), resulting in zero acceleration. For example, a heavy book resting on a table experiences downward gravitational force balanced by an equal upward normal contact force, remaining at rest while withstanding internal compressive stresses.</p>
          </div>
        </details>
      </div>

      <!-- Cross-Disciplinary Internal Links -->
      <div class="related-calculators" style="margin-top: 2rem; padding: 1.5rem; background: var(--bg-secondary, #f8f9fa); border-radius: 8px;">
        <h3>Related Physics &amp; Engineering Calculators</h3>
        <ul style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.75rem; list-style: none; padding: 0;">
          <li><a href="momentum-calculator.html">&rarr; Momentum &amp; Collision Solver</a></li>
          <li><a href="pressure-calculator.html">&rarr; Mechanical Pressure Calculator (P = F/A)</a></li>
          <li><a href="speed-calculator.html">&rarr; Speed &amp; Kinematics Calculator</a></li>
          <li><a href="density-calculator.html">&rarr; Density &amp; Buoyancy Solver</a></li>
          <li><a href="acceleration-calculator.html">&rarr; Acceleration Kinematics Solver</a></li>
          <li><a href="force-converter.html">&rarr; Universal Force Unit Converter</a></li>
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
      'oz': 0.028349523125,
      'ton': 1000.0
    };

    var ACCEL_FACTORS = {
      'm_s2': 1.0,
      'ft_s2': 0.3048,
      'g0': 9.80665,
      'km_h_s': 0.277777778
    };

    var FORCE_FACTORS = {
      'N': 1.0,
      'kN': 1000.0,
      'lbf': 4.448221615,
      'kgf': 9.80665
    };

    var G_CONST = 6.67430e-11;

    function switchForceMode() {
      var mode = document.getElementById('force-mode').value;
      document.getElementById('panel-newton2').style.display = (mode === 'newton2') ? 'block' : 'none';
      document.getElementById('panel-weight').style.display = (mode === 'weight') ? 'block' : 'none';
      document.getElementById('panel-gravitation').style.display = (mode === 'gravitation') ? 'block' : 'none';

      var lbl = document.getElementById('res-primary-label');
      if (mode === 'weight') {
        lbl.innerText = "Gravitational Weight (W = mg)";
      } else if (mode === 'gravitation') {
        lbl.innerText = "Mutual Gravitational Force (F)";
      } else {
        lbl.innerText = "Calculated Force (F = ma)";
      }

      calculateForce();
    }

    function switchSolveTarget() {
      var target = document.getElementById('solve-target').value;
      var grpM = document.getElementById('grp-mass');
      var grpA = document.getElementById('grp-accel');
      var grpF = document.getElementById('grp-force');

      grpM.style.display = (target === 'mass') ? 'none' : 'block';
      grpA.style.display = (target === 'accel') ? 'none' : 'block';
      grpF.style.display = (target === 'force') ? 'none' : 'block';

      var lbl = document.getElementById('res-primary-label');
      if (target === 'force') lbl.innerText = "Net Applied Force (F)";
      if (target === 'mass') lbl.innerText = "Calculated Mass (m)";
      if (target === 'accel') lbl.innerText = "Resulting Acceleration (a)";

      calculateForce();
    }

    function loadCelestialBody() {
      var val = document.getElementById('wt-body').value;
      if (val !== 'custom') {
        document.getElementById('wt-g').value = val;
        calculateForce();
      }
    }

    function calculateForce() {
      var mode = document.getElementById('force-mode').value;
      var f_N = 0;
      var steps = "";

      if (mode === 'newton2') {
        var target = document.getElementById('solve-target').value;
        var mVal = parseFloat(document.getElementById('inp-mass').value);
        var mUnit = document.getElementById('unit-mass').value;
        var aVal = parseFloat(document.getElementById('inp-accel').value);
        var aUnit = document.getElementById('unit-accel').value;
        var fVal = parseFloat(document.getElementById('inp-force').value);
        var fUnit = document.getElementById('unit-force').value;

        if (target === 'force') {
          if (isNaN(mVal) || isNaN(aVal) || mVal <= 0) {
            showError("Mass must be positive and acceleration must be a valid number.");
            return;
          }
          var mKg = mVal * MASS_FACTORS[mUnit];
          var aMS2 = aVal * ACCEL_FACTORS[aUnit];
          f_N = mKg * aMS2;

          steps = "Mode: Newton's Second Law - Solve for Force (F = m * a)\n" +
                  "Inputs: Mass m = " + mVal + " " + mUnit + ", Accel a = " + aVal + " " + aUnit + "\n\n" +
                  "1. Convert Mass to SI: m = " + mKg.toFixed(4) + " kg\n" +
                  "2. Convert Accel to SI: a = " + aMS2.toFixed(4) + " m/s²\n\n" +
                  "3. Compute Force: F = m * a = " + mKg.toFixed(4) + " * " + aMS2.toFixed(4) + "\n" +
                  "   F = " + f_N.toFixed(2) + " N (" + (f_N / 1000).toFixed(4) + " kN, " + (f_N / 4.448222).toFixed(2) + " lbf)";

          document.getElementById('res-primary-val').innerText = f_N.toLocaleString(undefined, {maximumFractionDigits: 2}) + " N";
          document.getElementById('res-primary-sub').innerText = (f_N / 1000).toFixed(3) + " kN • " + (f_N / 4.448222).toFixed(2) + " lbf";

        } else if (target === 'mass') {
          if (isNaN(fVal) || isNaN(aVal) || aVal === 0) {
            showError("Force must be a number and acceleration cannot be zero.");
            return;
          }
          var fInN = fVal * FORCE_FACTORS[fUnit];
          var aMS2_2 = aVal * ACCEL_FACTORS[aUnit];
          var mResKg = Math.abs(fInN / aMS2_2);
          f_N = fInN;

          steps = "Mode: Newton's Second Law - Solve for Mass (m = F / a)\n" +
                  "Inputs: Force F = " + fVal + " " + fUnit + ", Accel a = " + aVal + " " + aUnit + "\n\n" +
                  "1. Convert Force to SI: F = " + fInN.toFixed(2) + " N\n" +
                  "2. Convert Accel to SI: a = " + aMS2_2.toFixed(4) + " m/s²\n\n" +
                  "3. Compute Mass: m = F / a = " + fInN.toFixed(2) + " / " + aMS2_2.toFixed(4) + "\n" +
                  "   m = " + mResKg.toFixed(4) + " kg (" + (mResKg * 2.20462).toFixed(4) + " lb)";

          document.getElementById('res-primary-val').innerText = mResKg.toLocaleString(undefined, {maximumFractionDigits: 4}) + " kg";
          document.getElementById('res-primary-sub').innerText = (mResKg * 2.20462).toFixed(2) + " lb • " + (mResKg / 1000).toFixed(4) + " metric tons";

        } else if (target === 'accel') {
          if (isNaN(fVal) || isNaN(mVal) || mVal <= 0) {
            showError("Force must be a number and mass must be strictly positive.");
            return;
          }
          var fInN_3 = fVal * FORCE_FACTORS[fUnit];
          var mKg_3 = mVal * MASS_FACTORS[mUnit];
          var aResMS2 = fInN_3 / mKg_3;
          f_N = fInN_3;

          steps = "Mode: Newton's Second Law - Solve for Acceleration (a = F / m)\n" +
                  "Inputs: Force F = " + fVal + " " + fUnit + ", Mass m = " + mVal + " " + mUnit + "\n\n" +
                  "1. Convert Force to SI: F = " + fInN_3.toFixed(2) + " N\n" +
                  "2. Convert Mass to SI: m = " + mKg_3.toFixed(4) + " kg\n\n" +
                  "3. Compute Acceleration: a = F / m = " + fInN_3.toFixed(2) + " / " + mKg_3.toFixed(4) + "\n" +
                  "   a = " + aResMS2.toFixed(4) + " m/s² (" + (aResMS2 / 9.80665).toFixed(3) + " g₀)";

          document.getElementById('res-primary-val').innerText = aResMS2.toFixed(4) + " m/s²";
          document.getElementById('res-primary-sub').innerText = (aResMS2 / 9.80665).toFixed(3) + " g₀ • " + (aResMS2 * 3.28084).toFixed(3) + " ft/s²";
        }

      } else if (mode === 'weight') {
        var wm = parseFloat(document.getElementById('wt-mass').value);
        var wmUnit = document.getElementById('wt-unit-mass').value;
        var wg = parseFloat(document.getElementById('wt-g').value);

        if (isNaN(wm) || isNaN(wg) || wm <= 0 || wg < 0) {
          showError("Mass must be positive and gravity must be non-negative.");
          return;
        }

        var wKg = wm * MASS_FACTORS[wmUnit];
        f_N = wKg * wg;

        steps = "Mode: Gravitational Weight (W = m * g)\n" +
                "Inputs: Mass m = " + wm + " " + wmUnit + ", Gravity g = " + wg + " m/s²\n\n" +
                "1. Mass in SI: m = " + wKg.toFixed(4) + " kg\n\n" +
                "2. Gravitational Weight: W = m * g = " + wKg.toFixed(4) + " * " + wg.toFixed(4) + "\n" +
                "   W = " + f_N.toFixed(2) + " N (" + (f_N / 4.448222).toFixed(2) + " lbf, " + (f_N / 9.80665).toFixed(2) + " kgf)";

        document.getElementById('res-primary-val').innerText = f_N.toLocaleString(undefined, {maximumFractionDigits: 2}) + " N";
        document.getElementById('res-primary-sub').innerText = (f_N / 4.448222).toFixed(2) + " lbf • " + (f_N / 1000).toFixed(3) + " kN";

      } else if (mode === 'gravitation') {
        var m1 = parseFloat(document.getElementById('grav-m1').value);
        var m2 = parseFloat(document.getElementById('grav-m2').value);
        var r = parseFloat(document.getElementById('grav-r').value);

        if (isNaN(m1) || isNaN(m2) || isNaN(r) || m1 <= 0 || m2 <= 0 || r <= 0) {
          showError("Planetary masses and separation distance must be strictly positive.");
          return;
        }

        f_N = (G_CONST * m1 * m2) / (r * r);

        steps = "Mode: Universal Planetary Gravitation (F = G * m1 * m2 / r²)\n" +
                "Inputs: m1 = " + m1.toExponential(4) + " kg, m2 = " + m2.toExponential(4) + " kg, r = " + r.toExponential(4) + " m\n" +
                "G = 6.67430 × 10⁻¹¹ N·m²/kg²\n\n" +
                "1. Mutual Gravitational Force: F = (6.67430e-11 * " + m1.toExponential(4) + " * " + m2.toExponential(4) + ") / (" + r.toExponential(4) + ")²\n" +
                "   F = " + f_N.toExponential(4) + " N (" + (f_N / 1000).toExponential(4) + " kN)";

        document.getElementById('res-primary-val').innerText = (f_N >= 1e6 || f_N <= 1e-3) ? f_N.toExponential(4) + " N" : f_N.toLocaleString(undefined, {maximumFractionDigits: 2}) + " N";
        document.getElementById('res-primary-sub').innerText = (f_N / 1000).toExponential(4) + " kN • " + (f_N / 4.448222).toExponential(4) + " lbf";
      }

      var kn = f_N / 1000.0;
      var lbf = f_N / 4.448221615;
      var kgf = f_N / 9.80665;
      var dyn = f_N * 100000.0;
      var pdl = f_N / 0.138255;

      document.getElementById('res-kn').innerText = (Math.abs(kn) >= 1e6 || (Math.abs(kn) <= 1e-3 && kn !== 0)) ? kn.toExponential(4) + " kN" : kn.toFixed(3) + " kN";
      document.getElementById('res-lbf').innerText = (Math.abs(lbf) >= 1e6 || (Math.abs(lbf) <= 1e-3 && lbf !== 0)) ? lbf.toExponential(4) + " lbf" : lbf.toFixed(2) + " lbf";
      document.getElementById('res-kgf').innerText = (Math.abs(kgf) >= 1e6 || (Math.abs(kgf) <= 1e-3 && kgf !== 0)) ? kgf.toExponential(4) + " kgf" : kgf.toFixed(2) + " kgf";

      document.getElementById('eq-n').innerText = (Math.abs(f_N) >= 1e6 || (Math.abs(f_N) <= 1e-3 && f_N !== 0)) ? f_N.toExponential(4) + " N" : f_N.toLocaleString(undefined, {maximumFractionDigits: 1}) + " N";
      document.getElementById('eq-lbf').innerText = (Math.abs(lbf) >= 1e6 || (Math.abs(lbf) <= 1e-3 && lbf !== 0)) ? lbf.toExponential(4) + " lbf" : lbf.toLocaleString(undefined, {maximumFractionDigits: 2}) + " lbf";
      document.getElementById('eq-dyn').innerText = (Math.abs(dyn) >= 1e6 || (Math.abs(dyn) <= 1e-3 && dyn !== 0)) ? dyn.toExponential(4) + " dyn" : dyn.toLocaleString(undefined, {maximumFractionDigits: 0}) + " dyn";
      document.getElementById('eq-pdl').innerText = (Math.abs(pdl) >= 1e6 || (Math.abs(pdl) <= 1e-3 && pdl !== 0)) ? pdl.toExponential(4) + " pdl" : pdl.toLocaleString(undefined, {maximumFractionDigits: 1}) + " pdl";

      document.getElementById('res-steps').innerText = steps;
    }

    function showError(msg) {
      document.getElementById('res-primary-val').innerText = "Error";
      document.getElementById('res-primary-sub').innerText = "Invalid calculation";
      document.getElementById('res-kn').innerText = "N/A";
      document.getElementById('res-lbf').innerText = "N/A";
      document.getElementById('res-kgf').innerText = "N/A";
      document.getElementById('res-steps').innerText = "Error: " + msg;
    }

    function resetForce() {
      document.getElementById('force-mode').value = 'newton2';
      document.getElementById('solve-target').value = 'force';
      document.getElementById('inp-mass').value = '1200';
      document.getElementById('unit-mass').value = 'kg';
      document.getElementById('inp-accel').value = '4.5';
      document.getElementById('unit-accel').value = 'm_s2';
      document.getElementById('inp-force').value = '5400';
      document.getElementById('unit-force').value = 'N';
      document.getElementById('wt-mass').value = '75';
      document.getElementById('wt-unit-mass').value = 'kg';
      document.getElementById('wt-body').value = '9.80665';
      document.getElementById('wt-g').value = '9.80665';
      document.getElementById('grav-m1').value = '5.972e24';
      document.getElementById('grav-m2').value = '7.348e22';
      document.getElementById('grav-r').value = '384400000';
      switchForceMode();
      switchSolveTarget();
    }

    window.addEventListener('DOMContentLoaded', function() {
      calculateForce();
    });
  </script>
</body>
</html>
"""

# 2. momentum-calculator.html
HTML_MOMENTUM = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Momentum Calculator - Linear Momentum (p = mv) &amp; Collisions</title>
  <meta name="description" content="Calculate linear momentum (p = mv), velocity, mass, and kinetic energy. Solves elastic and inelastic two-body collisions with conservation of momentum formulas.">
  <link rel="canonical" href="https://calchub.org/momentum-calculator.html">
  <meta property="og:title" content="Momentum Calculator - Linear Momentum &amp; Collision Solver">
  <meta property="og:description" content="Free physics momentum calculator. Calculate p = mv, kinetic energy, elastic and inelastic 1D collisions, and coefficient of restitution with step-by-step proofs.">
  <meta property="og:url" content="https://calchub.org/momentum-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Momentum Calculator - Mechanics &amp; Collisions Solver">
  <meta name="twitter:description" content="Solve linear momentum p = mv, kinetic energy Ek = p^2/(2m), and two-body collision dynamics with full worked engineering case studies.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Momentum Calculator",
    "url": "https://calchub.org/momentum-calculator.html",
    "description": "Calculates linear momentum, velocity, mass, kinetic energy, and one-dimensional elastic and inelastic collision kinematics.",
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
        "name": "What is the formula for calculating linear momentum?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Linear momentum (p) is the vector product of an object's mass and its velocity: p = m * v, where p is momentum in kilogram-meters per second (kg*m/s or N*s), m is mass in kg, and v is velocity in m/s."
        }
      },
      {
        "@type": "Question",
        "name": "What is the Law of Conservation of Momentum?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Law of Conservation of Momentum states that in an isolated system subject to no net external forces, the total vector momentum remains constant across all internal interactions and collisions: m1*v1_initial + m2*v2_initial = m1*v1_final + m2*v2_final."
        }
      },
      {
        "@type": "Question",
        "name": "What is the difference between elastic and inelastic collisions?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "In an elastic collision, both total linear momentum and total kinetic energy are conserved. In an inelastic collision, total linear momentum is conserved, but part of the kinetic energy is converted into thermal heat, acoustic sound, and permanent structural deformation."
        }
      },
      {
        "@type": "Question",
        "name": "How is kinetic energy expressed in terms of momentum?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Kinetic energy (Ek) can be expressed in terms of momentum as: Ek = p^2 / (2 * m), because Ek = 0.5 * m * v^2 and p = m * v. This relationship is crucial in quantum mechanics and particle physics."
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
      <h1>Momentum Calculator</h1>
      <p class="calc-description">Compute linear momentum (\(p = mv\)), kinetic energy, and solve two-body elastic and inelastic collision kinematics with step-by-step proofs.</p>
    </div>

    <div class="calculator-body">
      <div class="input-group">
        <label for="mom-mode">Calculation Mode</label>
        <select id="mom-mode" class="form-control" onchange="switchMomentumMode()">
          <option value="single" selected>Single Object: Momentum, Mass or Velocity (\(p = m \times v\))</option>
          <option value="collision">Two-Body 1D Collision: Elastic / Inelastic Solver</option>
        </select>
      </div>

      <!-- Panel: Single Object p = mv -->
      <div id="panel-single">
        <div class="input-group">
          <label for="solve-target-mom">Variable to Calculate</label>
          <select id="solve-target-mom" class="form-control" onchange="switchSolveTargetMom()">
            <option value="momentum" selected>Momentum (\(p = m \times v\))</option>
            <option value="mass">Mass (\(m = p / v\))</option>
            <option value="velocity">Velocity (\(v = p / m\))</option>
          </select>
        </div>

        <div class="input-grid">
          <div class="input-group" id="grp-mom-m">
            <label for="inp-mom-m">Mass (\(m\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="inp-mom-m" class="form-control" value="1500" step="any" min="0" style="flex: 2;">
              <select id="unit-mom-m" class="form-control" style="flex: 1;" onchange="calculateMomentum()">
                <option value="kg" selected>kg</option>
                <option value="g">g</option>
                <option value="lb">lb</option>
                <option value="oz">oz</option>
                <option value="ton">ton</option>
              </select>
            </div>
          </div>

          <div class="input-group" id="grp-mom-v">
            <label for="inp-mom-v">Velocity (\(v\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="inp-mom-v" class="form-control" value="25" step="any" style="flex: 2;">
              <select id="unit-mom-v" class="form-control" style="flex: 1;" onchange="calculateMomentum()">
                <option value="m_s" selected>m/s</option>
                <option value="km_h">km/h</option>
                <option value="mph">mph</option>
                <option value="ft_s">ft/s</option>
                <option value="knot">knots</option>
              </select>
            </div>
          </div>

          <div class="input-group" id="grp-mom-p" style="display: none;">
            <label for="inp-mom-p">Momentum (\(p\))</label>
            <div style="display: flex; gap: 0.5rem;">
              <input type="number" id="inp-mom-p" class="form-control" value="37500" step="any" style="flex: 2;">
              <select id="unit-mom-p" class="form-control" style="flex: 1;" onchange="calculateMomentum()">
                <option value="kg_m_s" selected>kg&middot;m/s (N&middot;s)</option>
                <option value="lb_ft_s">lb&middot;ft/s</option>
                <option value="g_cm_s">g&middot;cm/s</option>
              </select>
            </div>
          </div>
        </div>
      </div>

      <!-- Panel: Two-Body Collision -->
      <div id="panel-collision" style="display: none;">
        <div class="input-group">
          <label for="collision-type">Collision Physics Nature</label>
          <select id="collision-type" class="form-control" onchange="calculateMomentum()">
            <option value="elastic" selected>Perfectly Elastic Collision (Kinetic Energy Conserved &bull; e = 1.0)</option>
            <option value="inelastic">Perfectly Inelastic Collision (Bodies Stick Together &bull; e = 0.0)</option>
            <option value="custom-e">Partially Inelastic (Specify Coefficient of Restitution e)</option>
          </select>
        </div>

        <div class="input-grid">
          <div class="input-group">
            <label for="col-m1">Body 1 Mass (\(m_1\)) [kg]</label>
            <input type="number" id="col-m1" class="form-control" value="1200" step="any" min="0">
          </div>
          <div class="input-group">
            <label for="col-v1">Body 1 Initial Velocity (\(v_{1i}\)) [m/s]</label>
            <input type="number" id="col-v1" class="form-control" value="20" step="any">
          </div>
        </div>

        <div class="input-grid">
          <div class="input-group">
            <label for="col-m2">Body 2 Mass (\(m_2\)) [kg]</label>
            <input type="number" id="col-m2" class="form-control" value="800" step="any" min="0">
          </div>
          <div class="input-group">
            <label for="col-v2">Body 2 Initial Velocity (\(v_{2i}\)) [m/s]</label>
            <input type="number" id="col-v2" class="form-control" value="-10" step="any">
            <small style="color: var(--text-muted, #6c757d);">Negative indicates opposite direction</small>
          </div>
        </div>

        <div class="input-group" id="grp-restitution" style="display: none;">
          <label for="col-e">Coefficient of Restitution (\(e\)) [0.0 = Sticking, 1.0 = Bouncing]</label>
          <input type="number" id="col-e" class="form-control" value="0.75" step="0.01" min="0" max="1">
        </div>
      </div>

      <div class="btn-group">
        <button type="button" class="btn btn-primary" onclick="calculateMomentum()">Compute Dynamics</button>
        <button type="button" class="btn btn-secondary" onclick="resetMomentum()">Reset Defaults</button>
      </div>

      <!-- Results Display Grid -->
      <div class="results-grid" style="margin-top: 1.5rem;">
        <div class="result-card primary-result">
          <div class="result-label" id="res-primary-label">Total Momentum (\(p\))</div>
          <div class="result-value" id="res-primary-val">37,500.00 kg&middot;m/s</div>
          <div class="result-subtext" id="res-primary-sub">37,500.00 N&middot;s (Newton-seconds)</div>
        </div>

        <div class="result-card">
          <div class="result-label">Kinetic Energy (\(E_k\))</div>
          <div class="result-value" id="res-ke">468.75 kJ</div>
          <div class="result-subtext">468,750.0 Joules (\(p^2 / 2m\))</div>
        </div>

        <div class="result-card">
          <div class="result-label">Imperial Momentum</div>
          <div class="result-value" id="res-imp">271,232 lb&middot;ft/s</div>
          <div class="result-subtext">slug&middot;ft/s: 8,430.7</div>
        </div>

        <div class="result-card">
          <div class="result-label" id="res-col-label">Velocity Status</div>
          <div class="result-value" id="res-col-val">25.00 m/s</div>
          <div class="result-subtext" id="res-col-sub">90.00 km/h &bull; 55.92 mph</div>
        </div>
      </div>

      <!-- Step-by-step Math Breakdown Card -->
      <div class="info-card" style="margin-top: 1.5rem;">
        <h3>Step-by-Step Physics &amp; Conservation Derivation</h3>
        <pre id="res-steps" style="white-space: pre-wrap; font-family: monospace; background: var(--bg-secondary, #f8f9fa); padding: 1rem; border-radius: 6px; font-size: 0.9rem; line-height: 1.5; color: var(--text-primary, #212529);"></pre>
      </div>
    </div>

    <!-- Article Content: 1000+ Words Physics & Dynamics Deep Dive -->
    <article class="article-body">
      <h2>The Physics of Linear Momentum and Conservation Laws</h2>
      <p>
        In classical Newtonian dynamics, relativistic mechanics, and astrophysics, <strong>linear momentum</strong> (\(\vec{p}\)), historically termed <em>quantity of motion</em> by Sir Isaac Newton, is the fundamental vector product of an object's mass and its instantaneous velocity vector. Momentum quantifies the inertia of a moving body: it measures how difficult it is to bring that moving body to a complete halt or alter its trajectory.
      </p>
      <p>
        Across physics, momentum occupies a uniquely revered status because it obeys one of nature's most absolute conservation principles. As proven by mathematician Emmy Noether in her seminal 1915 theorem, the <strong>Law of Conservation of Linear Momentum</strong> is not merely an empirical coincidence—it is the direct mathematical consequence of the fundamental <em>spatial translational symmetry</em> of the universe: the laws of physics are invariant whether an experiment is conducted in New York, Tokyo, or the Andromeda Galaxy.
      </p>

      <h2>Mathematical Formulations and Governing Equations</h2>

      <h3>1. Linear Momentum Definition</h3>
      <p>
        For a classical body of inertial mass \(m\) traveling at velocity \(\vec{v}\), momentum is defined as:
      </p>
      $$\vec{p} = m \vec{v}$$
      <p>
        Where:
      </p>
      <ul>
        <li>\(\vec{p}\) is the linear momentum vector, measured in kilogram-meters per second (\(\text{kg}\cdot\text{m/s}\)), which is dimensionally equivalent to Newton-seconds (\(\text{N}\cdot\text{s}\)).</li>
        <li>\(m\) is the inertial mass in kilograms (\(\text{kg}\)).</li>
        <li>\(\vec{v}\) is the instantaneous velocity vector in meters per second (\(\text{m/s}\)).</li>
      </ul>

      <h3>Algebraic Transpositions</h3>
      <p><strong>Solving for Velocity:</strong></p>
      $$v = \frac{p}{m}$$
      <p><strong>Solving for Mass:</strong></p>
      $$m = \frac{p}{v}$$

      <h3>2. Kinetic Energy in Terms of Momentum</h3>
      <p>
        Translational kinetic energy \(E_k = \frac{1}{2} m v^2\) is directly connected to momentum by substituting \(v = p / m\):
      </p>
      $$E_k = \frac{1}{2} m \left(\frac{p}{m}\right)^2 = \frac{p^2}{2m}$$
      <p>
        This relation demonstrates that if two objects possess identical momentum, the lighter object carries substantially greater kinetic energy:
      </p>
      $$\frac{E_{k,1}}{E_{k,2}} = \frac{m_2}{m_1} \quad (\text{at constant } p)$$
      <p>
        This fundamental disparity explains why a lightweight, high-velocity rifle bullet easily penetrates armor plates that readily deflect a slow-moving, heavy bowling ball of equal momentum.
      </p>

      <h3>3. One-Dimensional Collision Kinematics</h3>
      <p>
        Consider two bodies of masses \(m_1\) and \(m_2\) traveling along a straight line with initial velocities \(v_{1i}\) and \(v_{2i}\). In an isolated system subject to no external forces, the total momentum before collision equals total momentum after collision:
      </p>
      $$m_1 v_{1i} + m_2 v_{2i} = m_1 v_{1f} + m_2 v_{2f}$$

      <h4>A. Perfectly Elastic Collisions (\(e = 1.0\))</h4>
      <p>
        In an elastic collision, kinetic energy is conserved simultaneously with momentum:
      </p>
      $$\frac{1}{2} m_1 v_{1i}^2 + \frac{1}{2} m_2 v_{2i}^2 = \frac{1}{2} m_1 v_{1f}^f + \frac{1}{2} m_2 v_{2f}^2$$
      <p>
        Solving these two simultaneous equations yields the exact post-collision velocities:
      </p>
      $$v_{1f} = \left(\frac{m_1 - m_2}{m_1 + m_2}\right) v_{1i} + \left(\frac{2 m_2}{m_1 + m_2}\right) v_{2i}$$
      $$v_{2f} = \left(\frac{2 m_1}{m_1 + m_2}\right) v_{1i} + \left(\frac{m_2 - m_1}{m_1 + m_2}\right) v_{2i}$$
      <p>
        When two identical masses collide elastically (\(m_1 = m_2\)), they completely exchange velocities: \(v_{1f} = v_{2i}\) and \(v_{2f} = v_{1i}\)—the exact mechanics observed in Newton's Cradle.
      </p>

      <h4>B. Perfectly Inelastic Collisions (\(e = 0.0\))</h4>
      <p>
        When two bodies collide and fuse or stick together into a single combined mass \((m_1 + m_2)\), they travel with a unified common final velocity \(v_f\):
      </p>
      $$v_f = \frac{m_1 v_{1i} + m_2 v_{2i}}{m_1 + m_2}$$
      <p>
        Kinetic energy lost to heat and deformation during a perfectly inelastic collision is maximized:
      </p>
      $$\Delta E_k = E_{k, i} - E_{k, f} = \frac{1}{2} \left(\frac{m_1 m_2}{m_1 + m_2}\right) (v_{1i} - v_{2i})^2$$

      <h4>C. Coefficient of Restitution (\(e\))</h4>
      <p>
        For real-world collisions between ideal elastic and completely inelastic extremes, the <strong>Coefficient of Restitution</strong> (\(e\)) defines the ratio of relative separation velocity to relative approach velocity:
      </p>
      $$e = \frac{v_{2f} - v_{1f}}{v_{1i} - v_{2i}}$$
      <p>
        General post-collision velocities for arbitrary \(e\) (\(0 \le e \le 1\)):
      </p>
      $$v_{1f} = \frac{m_1 v_{1i} + m_2 v_{2i} - m_2 e (v_{1i} - v_{2i})}{m_1 + m_2}$$
      $$v_{2f} = \frac{m_1 v_{1i} + m_2 v_{2i} + m_1 e (v_{1i} - v_{2i})}{m_1 + m_2}$$

      <h2>Benchmark Momentum Across Physical Scales</h2>
      <p>
        The table below catalogs linear momentum and kinetic energy across atomic, sports, transportation, and cosmic realms.
      </p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Physical Object / System</th>
            <th>Mass (\(m\))</th>
            <th>Velocity (\(v\))</th>
            <th>Momentum (\(p\)) [kg&middot;m/s]</th>
            <th>Kinetic Energy (\(E_k\))</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Thermal Neutron (300 K)</td>
            <td>\(1.67 \times 10^{-27}\text{ kg}\)</td>
            <td>\(2,200\text{ m/s}\)</td>
            <td>\(3.68 \times 10^{-24}\)</td>
            <td>\(0.025\text{ eV}\)</td>
          </tr>
          <tr>
            <td>Dust Mite in Air Current</td>
            <td>\(1.0 \times 10^{-8}\text{ kg}\)</td>
            <td>\(0.10\text{ m/s}\)</td>
            <td>\(1.0 \times 10^{-9}\)</td>
            <td>\(5.0 \times 10^{-11}\text{ J}\)</td>
          </tr>
          <tr>
            <td>Pistol Bullet (9×19mm Parabellum)</td>
            <td>\(0.008\text{ kg}\) (8 g)</td>
            <td>\(360\text{ m/s}\)</td>
            <td>2.88</td>
            <td>\(518.4\text{ J}\)</td>
          </tr>
          <tr>
            <td>Major League Baseball Pitch</td>
            <td>\(0.145\text{ kg}\)</td>
            <td>\(45\text{ m/s}\) (101 mph)</td>
            <td>6.53</td>
            <td>\(146.8\text{ J}\)</td>
          </tr>
          <tr>
            <td>Sprinting Track Athlete (Usain Bolt)</td>
            <td>\(94\text{ kg}\)</td>
            <td>\(12.4\text{ m/s}\)</td>
            <td>1,165.6</td>
            <td>\(7,227\text{ J}\)</td>
          </tr>
          <tr>
            <td>Passenger Automobile (65 mph)</td>
            <td>\(1,600\text{ kg}\)</td>
            <td>\(29.0\text{ m/s}\)</td>
            <td>46,400</td>
            <td>\(672.8\text{ kJ}\)</td>
          </tr>
          <tr>
            <td>Heavy Freight Train (100 cars)</td>
            <td>\(1.2 \times 10^7\text{ kg}\)</td>
            <td>\(20\text{ m/s}\) (45 mph)</td>
            <td>\(2.4 \times 10^8\)</td>
            <td>\(2.40\text{ GJ}\)</td>
          </tr>
          <tr>
            <td>Container Super-Vessel (Full Load)</td>
            <td>\(2.2 \times 10^8\text{ kg}\)</td>
            <td>\(11\text{ m/s}\) (21 kt)</td>
            <td>\(2.42 \times 10^9\)</td>
            <td>\(13.31\text{ GJ}\)</td>
          </tr>
          <tr>
            <td>Moon in Orbit around Earth</td>
            <td>\(7.35 \times 10^{22}\text{ kg}\)</td>
            <td>\(1,022\text{ m/s}\)</td>
            <td>\(7.51 \times 10^{25}\)</td>
            <td>\(3.84 \times 10^{28}\text{ J}\)</td>
          </tr>
        </tbody>
      </table>

      <h2>Practical Real-World Engineering Case Studies</h2>

      <div class="worked-example-card">
        <h3>Case Study 1: Ballistic Pendulum Bullet Velocity Measurement</h3>
        <p><strong>Scenario:</strong> In forensic firearms investigation, a rifle bullet of mass \(m_b = 9.50\text{ g}\) (\(0.0095\text{ kg}\)) is fired horizontally into a suspended wooden ballistic pendulum block of mass \(M = 4.75\text{ kg}\). The bullet embeds completely into the block in a perfectly inelastic collision. The block-bullet system swings upward, reaching a peak vertical height of \(h = 8.50\text{ cm}\) (\(0.085\text{ m}\)).</p>
        <p><strong>Objective:</strong> Calculate the muzzle velocity \(v_b\) of the rifle bullet using conservation of momentum and energy principles.</p>
        <div class="step-solution">
          <p><strong>1. Post-Collision Velocity from Gravitational Potential Energy:</strong></p>
          <p>During the upward swing, kinetic energy converts into potential energy: \(\frac{1}{2}(m_b + M)v_f^2 = (m_b + M)gh\):</p>
          $$v_f = \sqrt{2gh} = \sqrt{2 \times 9.80665\text{ m/s}^2 \times 0.085\text{ m}} = \sqrt{1.66713} \approx 1.2912\text{ m/s}$$
          <p><strong>2. Conservation of Linear Momentum at Impact:</strong></p>
          $$p_{\text{initial}} = p_{\text{final}} \implies m_b v_b + M(0) = (m_b + M) v_f$$
          $$v_b = \frac{(m_b + M) v_f}{m_b} = \frac{(0.0095 + 4.75)\text{ kg} \times 1.2912\text{ m/s}}{0.0095\text{ kg}} = \frac{4.7595 \times 1.2912}{0.0095} \approx 646.88\text{ m/s}$$
          <p>The forensic investigator establishes that the bullet's muzzle velocity was \(646.9\text{ m/s}\) (\(2,122\text{ ft/s}\)).</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Railcar Shunting &amp; Automatic Coupler Impact</h3>
        <p><strong>Scenario:</strong> In a classification switching yard, an uncoupled moving hopper railcar of mass \(m_1 = 65,000\text{ kg}\) rolls at \(v_{1i} = 3.20\text{ m/s}\) and collides with two stationary coupled railcars of combined mass \(m_2 = 110,000\text{ kg}\) (\(v_{2i} = 0\)). The knuckle couplers engage, locking all three cars together.</p>
        <p><strong>Objective:</strong> Compute the final coupled roll velocity \(v_f\) and calculate the mechanical kinetic energy dissipated into the draft gear hydraulic draft dampers.</p>
        <div class="step-solution">
          <p><strong>1. Conservation of Momentum for Inelastic Latch:</strong></p>
          $$p_{\text{initial}} = m_1 v_{1i} = 65,000\text{ kg} \times 3.20\text{ m/s} = 208,000\text{ kg}\cdot\text{m/s}$$
          $$v_f = \frac{p_{\text{initial}}}{m_1 + m_2} = \frac{208,000\text{ kg}\cdot\text{m/s}}{65,000 + 110,000\text{ kg}} = \frac{208,000}{175,000} \approx 1.1886\text{ m/s} \ (4.28\text{ km/h})$$
          <p><strong>2. Kinetic Energy Loss Calculation:</strong></p>
          $$E_{k, i} = \frac{1}{2} m_1 v_{1i}^2 = \frac{1}{2} \times 65,000 \times (3.20)^2 = 332,800\text{ J}$$
          $$E_{k, f} = \frac{1}{2} (m_1 + m_2) v_f^2 = \frac{1}{2} \times 175,000 \times (1.1886)^2 = 123,616\text{ J}$$
          $$\Delta E_k = E_{k, i} - E_{k, f} = 332,800\text{ J} - 123,616\text{ J} = 209,184\text{ J} \ (209.2\text{ kJ})$$
          <p>62.86% of the initial kinetic energy was absorbed by the heavy spring draft gear friction dampers, preventing railcar frame deformation.</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 3: Spacecraft Planetary Gravity Assist (Slingshot Trajectory)</h3>
        <p><strong>Scenario:</strong> Deep-space probe Voyager 1 approaches Jupiter (\(M_J = 1.898 \times 10^{27}\text{ kg}\)) in an orbital flyby. In the Sun's heliocentric reference frame, Jupiter moves along its orbital path at \(V_J = 13.0\text{ km/s}\). Voyager 1 approaches Jupiter from the opposite direction at \(v_{\text{probe}, i} = 10.0\text{ km/s}\) relative to the Sun.</p>
        <p><strong>Objective:</strong> Model the flyby as a 1D elastic gravitational interaction and determine Voyager's departing heliocentric velocity after swinging around Jupiter.</p>
        <div class="step-solution">
          <p><strong>1. Transformation to Jupiter's Center of Mass Frame:</strong></p>
          <p>In Jupiter's rest frame, the probe approaches at relative speed: \(v_{\text{rel}, i} = v_{\text{probe}, i} + V_J = 10.0 + 13.0 = 23.0\text{ km/s}\).</p>
          <p><strong>2. Elastic Gravitational Deflection:</strong></p>
          <p>Because the planet is vastly more massive than the probe (\(M_J \gg m_{\text{probe}}\)), Jupiter's orbital speed is unaffected (\(\Delta V_J \approx 0\)). The probe loops behind Jupiter and departs with identical relative speed in Jupiter's frame: \(v_{\text{rel}, f} = 23.0\text{ km/s}\) in the forward direction of Jupiter's orbital motion.</p>
          <p><strong>3. Transformation Back to Sun's Heliocentric Frame:</strong></p>
          $$v_{\text{probe}, f} = V_J + v_{\text{rel}, f} = 13.0\text{ km/s} + 23.0\text{ km/s} = 36.0\text{ km/s}$$
          <p>Voyager 1 gained a massive \(26.0\text{ km/s}\) of heliocentric speed—extracting an infinitesimally tiny fraction of Jupiter's vast orbital momentum to propel itself toward the outer solar system!</p>
        </div>
      </div>

      <h2>Relativistic Linear Momentum in High-Energy Physics</h2>
      <p>
        As an object's speed approaches the vacuum speed of light (\(c = 299,792,458\text{ m/s}\)), classical mechanics fails. In special relativity, momentum is modified by the Lorentz factor \(\gamma\):
      </p>
      $$\vec{p} = \gamma m_0 \vec{v} = \frac{m_0 \vec{v}}{\sqrt{1 - \frac{v^2}{c^2}}}$$
      <p>
        As \(v \to c\), the Lorentz factor \(\gamma \to \infty\), requiring infinite momentum and infinite energy to accelerate a massive particle to the speed of light. Furthermore, even massless particles such as photons carry linear momentum proportional to their electromagnetic energy:
      </p>
      $$p_{\text{photon}} = \frac{E}{c} = \frac{h}{\lambda}$$
      <p>
        Where \(h\) is Planck's constant and \(\lambda\) is wavelength. This radiation momentum exerts physical force, enabling solar sail spacecraft propulsion.
      </p>

      <h2>Frequently Asked Questions</h2>
      <div class="faq-accordion">
        <details class="faq-item">
          <summary class="faq-question">Can an isolated system have zero momentum while possessing vast kinetic energy?</summary>
          <div class="faq-answer">
            <p>Yes. Linear momentum is a vector quantity that accounts for directional signs (+ and -), whereas kinetic energy is a positive scalar quantity (\(E_k = \frac{1}{2}mv^2 \ge 0\)). For example, two identical 1,000 kg cars speeding directly toward each other at equal speeds of 30 m/s possess a net system momentum of zero: \(1000(30) + 1000(-30) = 0\text{ kg}\cdot\text{m/s}\), yet their combined kinetic energy is substantial: \(2 \times \frac{1}{2}(1000)(900) = 900,000\text{ Joules}\).</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">How does linear momentum relate to impulse?</summary>
          <div class="faq-answer">
            <p>Impulse (\(J\)) is the integral of force over time: \(J = \int F dt = F_{\text{avg}} \Delta t\). By Newton's Second Law, impulse equals the net change in momentum: \(J = \Delta p = p_{\text{final}} - p_{\text{initial}}\). Extending collision contact duration \(\Delta t\) decreases peak impact force \(F_{\text{avg}}\), which is the operating principle behind automobile airbags and padded boxing gloves.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">Why is angular momentum separate from linear momentum?</summary>
          <div class="faq-answer">
            <p>Linear momentum describes translational movement through space (\(\vec{p} = m\vec{v}\)), deriving from spatial translational symmetry. Angular momentum describes rotational motion around a pivot axis (\(\vec{L} = \vec{r} \times \vec{p} = I\vec{\omega}\)), deriving from rotational spatial symmetry. Both conservation laws operate independently in isolated systems.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">What is the center of mass frame (zero-momentum frame)?</summary>
          <div class="faq-answer">
            <p>The center of mass (CM) frame is an inertial reference frame whose origin moves with the velocity of the system's center of mass. In this frame, the total vector linear momentum is identically zero by definition (\(\sum \vec{p}_{\text{CM}} = 0\)). Particle physicists analyze collisions in the CM frame because collision kinematics and invariant mass calculations become dramatically simplified.</p>
          </div>
        </details>
      </div>

      <!-- Cross-Disciplinary Internal Links -->
      <div class="related-calculators" style="margin-top: 2rem; padding: 1.5rem; background: var(--bg-secondary, #f8f9fa); border-radius: 8px;">
        <h3>Related Physics &amp; Dynamics Calculators</h3>
        <ul style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.75rem; list-style: none; padding: 0;">
          <li><a href="force-calculator.html">&rarr; Force &amp; Newton's Laws Solver (F = ma)</a></li>
          <li><a href="speed-calculator.html">&rarr; Speed &amp; Kinematics Calculator</a></li>
          <li><a href="kinetic-energy-calculator.html">&rarr; Kinetic Energy Calculator (Ek = 0.5mv²)</a></li>
          <li><a href="acceleration-calculator.html">&rarr; Acceleration Kinematics Solver</a></li>
          <li><a href="density-calculator.html">&rarr; Density &amp; Buoyancy Solver</a></li>
          <li><a href="pressure-calculator.html">&rarr; Pressure Calculator (P = F/A)</a></li>
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
      'oz': 0.028349523125,
      'ton': 1000.0
    };

    var VEL_FACTORS = {
      'm_s': 1.0,
      'km_h': 0.277777778,
      'mph': 0.44704,
      'ft_s': 0.3048,
      'knot': 0.514444444
    };

    var MOM_FACTORS = {
      'kg_m_s': 1.0,
      'lb_ft_s': 0.138254954376,
      'g_cm_s': 0.00001
    };

    function switchMomentumMode() {
      var mode = document.getElementById('mom-mode').value;
      document.getElementById('panel-single').style.display = (mode === 'single') ? 'block' : 'none';
      document.getElementById('panel-collision').style.display = (mode === 'collision') ? 'block' : 'none';

      var lbl = document.getElementById('res-primary-label');
      var colLbl = document.getElementById('res-col-label');
      if (mode === 'collision') {
        lbl.innerText = "Total System Momentum";
        colLbl.innerText = "Post-Collision Velocities";
      } else {
        lbl.innerText = "Linear Momentum (p)";
        colLbl.innerText = "Velocity Status";
      }

      calculateMomentum();
    }

    function switchSolveTargetMom() {
      var target = document.getElementById('solve-target-mom').value;
      var grpM = document.getElementById('grp-mom-m');
      var grpV = document.getElementById('grp-mom-v');
      var grpP = document.getElementById('grp-mom-p');

      grpM.style.display = (target === 'mass') ? 'none' : 'block';
      grpV.style.display = (target === 'velocity') ? 'none' : 'block';
      grpP.style.display = (target === 'momentum') ? 'none' : 'block';

      calculateMomentum();
    }

    function calculateMomentum() {
      var mode = document.getElementById('mom-mode').value;
      var p_SI = 0, ke_J = 0;
      var steps = "";

      if (mode === 'single') {
        var target = document.getElementById('solve-target-mom').value;
        var mVal = parseFloat(document.getElementById('inp-mom-m').value);
        var mUnit = document.getElementById('unit-mom-m').value;
        var vVal = parseFloat(document.getElementById('inp-mom-v').value);
        var vUnit = document.getElementById('unit-mom-v').value;
        var pVal = parseFloat(document.getElementById('inp-mom-p').value);
        var pUnit = document.getElementById('unit-mom-p').value;

        if (target === 'momentum') {
          if (isNaN(mVal) || isNaN(vVal) || mVal <= 0) {
            showError("Mass must be positive and velocity must be a valid number.");
            return;
          }
          var mKg = mVal * MASS_FACTORS[mUnit];
          var vMS = vVal * VEL_FACTORS[vUnit];
          p_SI = mKg * vMS;
          ke_J = 0.5 * mKg * vMS * vMS;

          steps = "Mode: Single Body Linear Momentum (p = m * v)\n" +
                  "Inputs: Mass m = " + mVal + " " + mUnit + ", Velocity v = " + vVal + " " + vUnit.replace('_', '/') + "\n\n" +
                  "1. Convert Mass to SI: m = " + mKg.toFixed(4) + " kg\n" +
                  "2. Convert Velocity to SI: v = " + vMS.toFixed(4) + " m/s\n\n" +
                  "3. Compute Momentum: p = m * v\n" +
                  "   p = " + mKg.toFixed(4) + " * " + vMS.toFixed(4) + " = " + p_SI.toFixed(2) + " kg·m/s (N·s)\n\n" +
                  "4. Kinetic Energy: Ek = p² / (2m) = ½ m v²\n" +
                  "   Ek = " + (ke_J / 1000).toFixed(3) + " kJ (" + ke_J.toFixed(1) + " Joules)";

          document.getElementById('res-primary-val').innerText = p_SI.toLocaleString(undefined, {maximumFractionDigits: 2}) + " kg·m/s";
          document.getElementById('res-primary-sub').innerText = p_SI.toLocaleString(undefined, {maximumFractionDigits: 2}) + " N·s";
          document.getElementById('res-col-val').innerText = vMS.toFixed(2) + " m/s";
          document.getElementById('res-col-sub').innerText = (vMS * 3.6).toFixed(2) + " km/h • " + (vMS / 0.44704).toFixed(2) + " mph";

        } else if (target === 'mass') {
          if (isNaN(pVal) || isNaN(vVal) || vVal === 0) {
            showError("Momentum must be a number and velocity cannot be zero.");
            return;
          }
          var pInSI = pVal * MOM_FACTORS[pUnit];
          var vMS_2 = vVal * VEL_FACTORS[vUnit];
          var mResKg = Math.abs(pInSI / vMS_2);
          p_SI = pInSI;
          ke_J = 0.5 * mResKg * vMS_2 * vMS_2;

          steps = "Mode: Single Body - Solve for Mass (m = p / v)\n" +
                  "Inputs: Momentum p = " + pVal + " " + pUnit + ", Velocity v = " + vVal + " " + vUnit.replace('_', '/') + "\n\n" +
                  "1. Momentum in SI: p = " + pInSI.toFixed(2) + " kg·m/s\n" +
                  "2. Velocity in SI: v = " + vMS_2.toFixed(4) + " m/s\n\n" +
                  "3. Mass: m = p / v = " + pInSI.toFixed(2) + " / " + vMS_2.toFixed(4) + "\n" +
                  "   m = " + mResKg.toFixed(4) + " kg (" + (mResKg * 2.20462).toFixed(2) + " lb)";

          document.getElementById('res-primary-val').innerText = mResKg.toLocaleString(undefined, {maximumFractionDigits: 4}) + " kg";
          document.getElementById('res-primary-sub').innerText = (mResKg * 2.20462).toFixed(2) + " lb";
          document.getElementById('res-col-val').innerText = vMS_2.toFixed(2) + " m/s";
          document.getElementById('res-col-sub').innerText = (vMS_2 * 3.6).toFixed(2) + " km/h • " + (vMS_2 / 0.44704).toFixed(2) + " mph";

        } else if (target === 'velocity') {
          if (isNaN(pVal) || isNaN(mVal) || mVal <= 0) {
            showError("Momentum must be a number and mass must be positive.");
            return;
          }
          var pInSI_3 = pVal * MOM_FACTORS[pUnit];
          var mKg_3 = mVal * MASS_FACTORS[mUnit];
          var vResMS = pInSI_3 / mKg_3;
          p_SI = pInSI_3;
          ke_J = 0.5 * mKg_3 * vResMS * vResMS;

          steps = "Mode: Single Body - Solve for Velocity (v = p / m)\n" +
                  "Inputs: Momentum p = " + pVal + " " + pUnit + ", Mass m = " + mVal + " " + mUnit + "\n\n" +
                  "1. Momentum in SI: p = " + pInSI_3.toFixed(2) + " kg·m/s\n" +
                  "2. Mass in SI: m = " + mKg_3.toFixed(4) + " kg\n\n" +
                  "3. Velocity: v = p / m = " + pInSI_3.toFixed(2) + " / " + mKg_3.toFixed(4) + "\n" +
                  "   v = " + vResMS.toFixed(4) + " m/s (" + (vResMS * 3.6).toFixed(2) + " km/h, " + (vResMS / 0.44704).toFixed(2) + " mph)";

          document.getElementById('res-primary-val').innerText = vResMS.toFixed(2) + " m/s";
          document.getElementById('res-primary-sub').innerText = (vResMS * 3.6).toFixed(2) + " km/h • " + (vResMS / 0.44704).toFixed(2) + " mph";
          document.getElementById('res-col-val').innerText = vResMS.toFixed(2) + " m/s";
          document.getElementById('res-col-sub').innerText = (vResMS * 3.6).toFixed(2) + " km/h";
        }

      } else if (mode === 'collision') {
        var cType = document.getElementById('collision-type').value;
        var m1 = parseFloat(document.getElementById('col-m1').value);
        var v1i = parseFloat(document.getElementById('col-v1').value);
        var m2 = parseFloat(document.getElementById('col-m2').value);
        var v2i = parseFloat(document.getElementById('col-v2').value);

        var grpE = document.getElementById('grp-restitution');
        grpE.style.display = (cType === 'custom-e') ? 'block' : 'none';

        if (isNaN(m1) || isNaN(v1i) || isNaN(m2) || isNaN(v2i) || m1 <= 0 || m2 <= 0) {
          showError("Masses must be positive and velocities must be real numbers.");
          return;
        }

        var e = 1.0;
        if (cType === 'inelastic') e = 0.0;
        if (cType === 'custom-e') {
          e = parseFloat(document.getElementById('col-e').value);
          if (isNaN(e) || e < 0 || e > 1) {
            showError("Coefficient of restitution e must be between 0.0 and 1.0.");
            return;
          }
        }

        var p_init = m1 * v1i + m2 * v2i;
        p_SI = p_init;
        var ke_init = 0.5 * m1 * v1i * v1i + 0.5 * m2 * v2i * v2i;

        var v1f = 0, v2f = 0;
        if (cType === 'inelastic') {
          v1f = p_init / (m1 + m2);
          v2f = v1f;
        } else {
          v1f = (m1 * v1i + m2 * v2i - m2 * e * (v1i - v2i)) / (m1 + m2);
          v2f = (m1 * v1i + m2 * v2i + m1 * e * (v1i - v2i)) / (m1 + m2);
        }

        var ke_final = 0.5 * m1 * v1f * v1f + 0.5 * m2 * v2f * v2f;
        var ke_lost = ke_init - ke_final;
        ke_J = ke_final;

        steps = "Mode: 1D Two-Body Collision (" + cType + ", e = " + e.toFixed(2) + ")\n" +
                "Inputs: m1 = " + m1 + " kg, v1i = " + v1i + " m/s | m2 = " + m2 + " kg, v2i = " + v2i + " m/s\n\n" +
                "1. Total Initial Momentum: p_tot = m1*v1i + m2*v2i\n" +
                "   p_tot = (" + m1 + " * " + v1i + ") + (" + m2 + " * " + v2i + ") = " + p_init.toFixed(2) + " kg·m/s\n\n" +
                "2. Post-Collision Velocities:\n" +
                "   v1_final = " + v1f.toFixed(3) + " m/s (" + (v1f * 3.6).toFixed(2) + " km/h)\n" +
                "   v2_final = " + v2f.toFixed(3) + " m/s (" + (v2f * 3.6).toFixed(2) + " km/h)\n\n" +
                "3. Energy Conservation Analysis:\n" +
                "   Initial Kinetic Energy: " + (ke_init / 1000).toFixed(3) + " kJ\n" +
                "   Final Kinetic Energy:   " + (ke_final / 1000).toFixed(3) + " kJ\n" +
                "   Kinetic Energy Lost:    " + (ke_lost / 1000).toFixed(3) + " kJ (" + (ke_init > 0 ? (ke_lost / ke_init * 100).toFixed(2) : 0) + "% dissipated)";

        document.getElementById('res-primary-val').innerText = p_SI.toLocaleString(undefined, {maximumFractionDigits: 2}) + " kg·m/s";
        document.getElementById('res-primary-sub').innerText = "Initial & Final Momentum Conserved";
        document.getElementById('res-col-val').innerText = "v1': " + v1f.toFixed(2) + " | v2': " + v2f.toFixed(2) + " m/s";
        document.getElementById('res-col-sub').innerText = "Dissipated Energy: " + (ke_lost / 1000).toFixed(2) + " kJ";
      }

      document.getElementById('res-ke').innerText = (ke_J >= 1e6) ? (ke_J / 1e6).toFixed(3) + " MJ" : (ke_J / 1000).toFixed(2) + " kJ";
      var impMom = p_SI / 0.138254954376;
      document.getElementById('res-imp').innerText = Math.round(impMom).toLocaleString() + " lb·ft/s";

      document.getElementById('res-steps').innerText = steps;
    }

    function showError(msg) {
      document.getElementById('res-primary-val').innerText = "Error";
      document.getElementById('res-primary-sub').innerText = "Invalid inputs";
      document.getElementById('res-ke').innerText = "N/A";
      document.getElementById('res-imp').innerText = "N/A";
      document.getElementById('res-col-val').innerText = "N/A";
      document.getElementById('res-col-sub').innerText = "N/A";
      document.getElementById('res-steps').innerText = "Error: " + msg;
    }

    function resetMomentum() {
      document.getElementById('mom-mode').value = 'single';
      document.getElementById('solve-target-mom').value = 'momentum';
      document.getElementById('inp-mom-m').value = '1500';
      document.getElementById('unit-mom-m').value = 'kg';
      document.getElementById('inp-mom-v').value = '25';
      document.getElementById('unit-mom-v').value = 'm_s';
      document.getElementById('inp-mom-p').value = '37500';
      document.getElementById('unit-mom-p').value = 'kg_m_s';
      document.getElementById('collision-type').value = 'elastic';
      document.getElementById('col-m1').value = '1200';
      document.getElementById('col-v1').value = '20';
      document.getElementById('col-m2').value = '800';
      document.getElementById('col-v2').value = '-10';
      document.getElementById('col-e').value = '0.75';
      switchMomentumMode();
      switchSolveTargetMom();
    }

    window.addEventListener('DOMContentLoaded', function() {
      calculateMomentum();
    });
  </script>
</body>
</html>
"""

def generate_part1():
    f1 = os.path.join(BASE_DIR, "force-calculator.html")
    with open(f1, "w", encoding="utf-8") as fp:
        fp.write(HTML_FORCE.strip() + "\n")
    print(f"Generated: {f1}")

    f2 = os.path.join(BASE_DIR, "momentum-calculator.html")
    with open(f2, "w", encoding="utf-8") as fp:
        fp.write(HTML_MOMENTUM.strip() + "\n")
    print(f"Generated: {f2}")

if __name__ == "__main__":
    generate_part1()
