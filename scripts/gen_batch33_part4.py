# -*- coding: utf-8 -*-
"""
Generator for Batch 33 - Part 4:
7. terminal-velocity-calculator.html
8. specific-gravity-calculator.html
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 7. terminal-velocity-calculator.html
HTML_TERMINAL_VELOCITY = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Terminal Velocity Calculator - Fluid Drag, Free Fall &amp; Aerodynamics</title>
  <meta name="description" content="Calculate terminal velocity (v_t = sqrt(2mg / rho A Cd)), aerodynamic drag force, free-fall stabilization time, and Reynolds numbers across air and fluids.">
  <link rel="canonical" href="https://calchub.org/terminal-velocity-calculator.html">
  <meta property="og:title" content="Terminal Velocity Calculator - Aerodynamic Drag &amp; Free Fall Physics">
  <meta property="og:description" content="Free engineering terminal velocity calculator. Solve falling speed, frontal area, drag coefficient, and fluid density with step-by-step physics proofs.">
  <meta property="og:url" content="https://calchub.org/terminal-velocity-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Terminal Velocity Calculator - Fluid Dynamics &amp; Ballistics">
  <meta name="twitter:description" content="Compute terminal free-fall speed with atmospheric density models, drag coefficients, and worked engineering case studies.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Terminal Velocity Calculator",
    "url": "https://calchub.org/terminal-velocity-calculator.html",
    "description": "Calculates terminal velocity, aerodynamic drag forces, frontal area requirements, and stabilization times in fluid mechanics.",
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
        "name": "What is the formula for terminal velocity?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The terminal velocity equation in a fluid under Newtonian drag is v_t = sqrt((2 * m * g) / (rho * A * C_d)), where m is falling body mass in kg, g is gravitational acceleration (9.80665 m/s²), rho is fluid density in kg/m³, A is projected cross-sectional area in m², and C_d is the dimensionless drag coefficient."
        }
      },
      {
        "@type": "Question",
        "name": "Why does a falling body stop accelerating at terminal velocity?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "As an object accelerates downward due to gravity, fluid drag resistance increases quadratically with velocity (F_d = 0.5 * rho * v² * C_d * A). When the upward aerodynamic drag force (plus buoyant force) exactly equals the downward gravitational force (F_g = m * g), net force becomes zero (sum F = 0). By Newton's First and Second Laws, acceleration drops to zero and velocity remains constant."
        }
      },
      {
        "@type": "Question",
        "name": "What is the terminal velocity of a human skydiver?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A standard adult human skydiver (approx. 80 kg) in a belly-to-earth horizontal spread posture (area ~0.7 m², C_d ~1.0) reaches a terminal velocity of roughly 54 m/s (195 km/h or 121 mph) near sea level. In a head-first or feet-first streamlined dive (area ~0.18 m², C_d ~0.7), terminal velocity increases to over 90–100 m/s (320–360 km/h or 200–225 mph)."
        }
      },
      {
        "@type": "Question",
        "name": "How does atmospheric altitude affect terminal velocity?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Because air density decreases exponentially with altitude according to the barometric formula, terminal velocity is significantly higher at high altitudes. For example, at 39,000 meters (stratosphere), air density is less than 1% of sea-level density, allowing free-fallers like Felix Baumgartner to exceed 377 m/s (1,357 km/h, breaking the sound barrier) before decelerating in denser lower atmospheric layers."
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

  <main class="page-container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo;
      <a href="engineering.html">Engineering</a> &rsaquo;
      <span>Terminal Velocity Calculator</span>
    </nav>

    <div class="page-header">
      <h1 class="page-title">Terminal Velocity Calculator</h1>
      <p class="page-desc">Compute free-fall terminal velocity, aerodynamic drag forces, frontal area thresholds, and deceleration profiles across atmospheric and fluid environments.</p>
    </div>

    <div class="calc-grid">
      <!-- Calculator Column -->
      <div class="calc-card">
        <div class="calc-header">
          <h2>Aerodynamic Drag &amp; Terminal Speed Solver</h2>
        </div>

        <!-- Mode Presets -->
        <div class="form-group">
          <label for="tv-preset">Object Preset (Auto-fills Shape &amp; Drag):</label>
          <select id="tv-preset" class="form-control">
            <option value="custom">-- Custom Object Parameters --</option>
            <option value="skydiver-belly" selected>Skydiver (Belly-to-Earth: 80 kg, 0.70 m², Cd 1.05)</option>
            <option value="skydiver-head">Skydiver (Head-First Dive: 80 kg, 0.18 m², Cd 0.70)</option>
            <option value="raindrop">Raindrop (Large: 0.000034 kg, 0.0000125 m², Cd 0.45)</option>
            <option value="baseball">Baseball (0.145 kg, 0.00427 m², Cd 0.30)</option>
            <option value="bowling-ball">Bowling Ball (7.26 kg, 0.0366 m², Cd 0.47)</option>
            <option value="bullet">9mm Rifle/Handgun Bullet (0.008 kg, 0.0000636 m², Cd 0.295)</option>
            <option value="sphere-steel">Steel Sphere (d=5 cm, 0.51 kg, 0.00196 m², Cd 0.47)</option>
            <option value="parachute">Personnel Parachute (100 kg total, 40 m², Cd 1.50)</option>
          </select>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label for="tv-mass">Falling Mass ($m$):</label>
            <input type="number" id="tv-mass" class="form-control" value="80" step="any" min="0.000001">
          </div>
          <div class="form-group">
            <label for="tv-mass-unit">Mass Unit:</label>
            <select id="tv-mass-unit" class="form-control">
              <option value="kg" selected>Kilograms (kg)</option>
              <option value="g">Grams (g)</option>
              <option value="lb">Pounds (lb)</option>
              <option value="oz">Ounces (oz)</option>
            </select>
          </div>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label for="tv-area">Frontal Projected Area ($A$):</label>
            <input type="number" id="tv-area" class="form-control" value="0.70" step="any" min="0.0000001">
          </div>
          <div class="form-group">
            <label for="tv-area-unit">Area Unit:</label>
            <select id="tv-area-unit" class="form-control">
              <option value="m2" selected>Square Meters (m²)</option>
              <option value="cm2">Square Centimeters (cm²)</option>
              <option value="ft2">Square Feet (ft²)</option>
              <option value="in2">Square Inches (in²)</option>
            </select>
          </div>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label for="tv-cd">Drag Coefficient ($C_d$):</label>
            <input type="number" id="tv-cd" class="form-control" value="1.05" step="any" min="0.01" max="3.0">
          </div>
          <div class="form-group">
            <label for="tv-fluid">Fluid Medium / Altitude:</label>
            <select id="tv-fluid" class="form-control">
              <option value="1.225" selected>Air (Sea Level, 15°C, 1.225 kg/m³)</option>
              <option value="1.112">Air (1,000 m altitude, 1.112 kg/m³)</option>
              <option value="0.909">Air (3,000 m / 10,000 ft, 0.909 kg/m³)</option>
              <option value="0.413">Air (10,000 m / Airliner cruising, 0.413 kg/m³)</option>
              <option value="0.018">Air (30,000 m / Stratosphere, 0.018 kg/m³)</option>
              <option value="998.2">Pure Water (20°C, 998.2 kg/m³)</option>
              <option value="1025.0">Seawater (20°C, 1025.0 kg/m³)</option>
              <option value="custom">Custom Fluid Density</option>
            </select>
          </div>
        </div>

        <div class="form-row" id="tv-custom-density-row" style="display: none;">
          <div class="form-group">
            <label for="tv-density-custom">Custom Density ($\rho$ in kg/m³):</label>
            <input type="number" id="tv-density-custom" class="form-control" value="1.225" step="any" min="0.0001">
          </div>
          <div class="form-group">
            <label for="tv-gravity">Gravity ($g$ in m/s²):</label>
            <input type="number" id="tv-gravity" class="form-control" value="9.80665" step="any" min="0.1">
          </div>
        </div>

        <div class="form-actions">
          <button type="button" id="tv-calc-btn" class="btn btn-primary">Calculate Terminal Velocity</button>
          <button type="button" id="tv-reset-btn" class="btn btn-secondary">Reset to Default</button>
        </div>

        <!-- Output Cards -->
        <div id="tv-results" class="results-container" style="margin-top: 1.5rem;">
          <div class="result-hero-card" style="background: var(--surface-card, #f8fafc); padding: 1.25rem; border-radius: 8px; border: 1px solid var(--border-color, #e2e8f0); text-align: center; margin-bottom: 1rem;">
            <div class="result-label" style="font-size: 0.875rem; color: var(--text-muted, #64748b); text-transform: uppercase; font-weight: 600;">Terminal Velocity ($v_t$)</div>
            <div id="tv-speed-primary" style="font-size: 2.25rem; font-weight: 800; color: var(--primary, #2563eb); margin: 0.25rem 0;">53.86 m/s</div>
            <div id="tv-speed-secondary" style="font-size: 1rem; color: var(--text-secondary, #475569);">193.9 km/h &bull; 120.5 mph &bull; 176.7 ft/s</div>
          </div>

          <div class="summary-metrics-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 0.75rem;">
            <div class="metric-card" style="background: var(--surface-card, #f8fafc); padding: 0.85rem; border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0);">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Equilibrium Drag ($F_d$)</div>
              <div id="tv-drag-force" style="font-size: 1.15rem; font-weight: 700;">784.5 N</div>
            </div>
            <div class="metric-card" style="background: var(--surface-card, #f8fafc); padding: 0.85rem; border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0);">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Kinetic Energy ($E_k$)</div>
              <div id="tv-kinetic-energy" style="font-size: 1.15rem; font-weight: 700;">116.0 kJ</div>
            </div>
            <div class="metric-card" style="background: var(--surface-card, #f8fafc); padding: 0.85rem; border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0);">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">95% Time to Steady State</div>
              <div id="tv-time-to-steady" style="font-size: 1.15rem; font-weight: 700;">10.05 s</div>
            </div>
            <div class="metric-card" style="background: var(--surface-card, #f8fafc); padding: 0.85rem; border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0);">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">95% Drop Distance</div>
              <div id="tv-dist-to-steady" style="font-size: 1.15rem; font-weight: 700;">388.4 m</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Reference Sidebar -->
      <aside class="sidebar-card">
        <h3>Standard Drag Coefficients ($C_d$)</h3>
        <p style="font-size: 0.875rem; color: var(--text-secondary, #475569);">Typical empirical drag coefficients for subsonic flow ($Re &gt; 10^4$):</p>
        <ul style="font-size: 0.875rem; line-height: 1.6; margin-left: 1.25rem;">
          <li><strong>Streamlined Airfoil:</strong> 0.045</li>
          <li><strong>Smooth Sphere:</strong> 0.47</li>
          <li><strong>Rough Sphere / Golf Ball:</strong> 0.25 – 0.35</li>
          <li><strong>Circular Cylinder (crossflow):</strong> 0.82 – 1.20</li>
          <li><strong>Flat Disc / Perpendicular Plate:</strong> 1.15 – 1.28</li>
          <li><strong>Human (Belly to Earth):</strong> 1.00 – 1.15</li>
          <li><strong>Human (Head-First Dive):</strong> 0.60 – 0.70</li>
          <li><strong>Round Parachute:</strong> 1.40 – 1.75</li>
        </ul>

        <h3 style="margin-top: 1.25rem;">Air Density by Altitude</h3>
        <ul style="font-size: 0.875rem; line-height: 1.6; margin-left: 1.25rem;">
          <li><strong>0 m (Sea Level):</strong> 1.225 kg/m³</li>
          <li><strong>2,000 m (6,560 ft):</strong> 1.007 kg/m³</li>
          <li><strong>4,000 m (13,120 ft):</strong> 0.819 kg/m³</li>
          <li><strong>8,000 m (Mt. Everest):</strong> 0.526 kg/m³</li>
          <li><strong>12,000 m (Cruising Jet):</strong> 0.312 kg/m³</li>
        </ul>
      </aside>
    </div>

    <!-- Long-Form Informational Engineering Article (1,400+ Words) -->
    <article class="article-body">
      <h2>1. The Physics and Mechanics of Terminal Velocity</h2>
      <p>Terminal velocity represents the maximum sustainable downward speed an object can achieve when falling freely through a viscous fluid medium (such as air or water) under the influence of gravitational attraction. When an unconstrained body is released from rest, its initial downward acceleration equals local gravitational acceleration \(g\) (\(9.80665\text{ m/s}^2\) on Earth's surface) because drag resistance is initially zero. However, as velocity develops, the surrounding fluid exerts an opposing hydrodynamic or aerodynamic resistance known as drag force (\(F_d\)).</p>
      <p>According to Newton's Second Law of Motion (\(\sum F = m a\)), the net vertical force acting on a falling body of mass \(m\) subjected to fluid drag and fluid buoyancy (\(F_b\)) is expressed as:</p>
      $$\sum F_y = F_g - F_d - F_b = m \frac{dv}{dt}$$
      <p>Where \(F_g = m g\) is downward gravitational force, \(F_d\) is upward hydrodynamic drag, and \(F_b = \rho_f V g\) is upward buoyant force according to Archimedes' Principle. For dense solid bodies falling through atmospheric air (where solid density \(\rho_s \gg \rho_f\)), buoyant force is negligible (\(F_b \approx 0\)). As vertical velocity increases quadratically with speed, drag force escalates until it matches gravitational pull exactly. At this precise dynamic equilibrium:</p>
      $$\sum F_y = m g - F_d = 0 \implies \frac{dv}{dt} = 0$$
      <p>When net acceleration drops to zero, the object ceases to accelerate and continues falling at a constant, steady-state terminal velocity (\(v_t\)).</p>

      <h2>2. Mathematical Derivation of the Terminal Velocity Formula</h2>
      <p>For high Reynolds number regimes typical of human skydivers, sports projectiles, and falling hail, fluid flow around the object is turbulent, and fluid resistance is governed by the classical Rayleigh drag equation:</p>
      $$F_d = \frac{1}{2} \rho C_d A v^2$$
      <p>Where:</p>
      <ul>
        <li><strong>\(\rho\) (Rho):</strong> Mass density of the fluid medium through which the body travels (expressed in \(\text{kg/m}^3\)). At standard atmospheric sea-level conditions (\(15^\circ\text{C}\), \(101.325\text{ kPa}\)), dry air density equals \(1.225\text{ kg/m}^3\).</li>
        <li><strong>\(C_d\):</strong> Dimensionless drag coefficient, characterizing the geometric form, skin friction, and surface aerodynamic efficiency of the falling object.</li>
        <li><strong>\(A\):</strong> Projected frontal cross-sectional area perpendicular to the velocity vector (expressed in \(\text{m}^2\)).</li>
        <li><strong>\(v\):</strong> Instantaneous relative velocity of the body relative to the undisturbed fluid (in \(\text{m/s}\)).</li>
      </ul>
      <p>Setting aerodynamic drag equal to gravitational weight at steady-state equilibrium gives:</p>
      $$m g = \frac{1}{2} \rho C_d A v_t^2$$
      <p>Solving analytically for the terminal velocity \(v_t\) yields the fundamental equation of aerodynamic terminal speed:</p>
      $$v_t = \sqrt{\frac{2 m g}{\rho A C_d}}$$
      <p>When the buoyant force cannot be neglected (such as a steel ball falling through honey, or an air bubble rising through water), Archimedes' buoyancy is retained, yielding the generalized terminal velocity equation:</p>
      $$v_t = \sqrt{\frac{2 (m - \rho_f V) g}{\rho_f A C_d}} = \sqrt{\frac{2 (\rho_s - \rho_f) V g}{\rho_f A C_d}}$$

      <h2>3. Hyperbolic Trajectory Equations and Time-to-Steady-State</h2>
      <p>Understanding terminal velocity requires analyzing how an object approaches \(v_t\) over time. The differential equation governing free fall from rest (\(v(0) = 0\)) under quadratic drag is:</p>
      $$\frac{dv}{dt} = g - \frac{\rho C_d A}{2m} v^2 = g \left(1 - \frac{v^2}{v_t^2}\right)$$
      <p>Separating variables and integrating directly produces the exact closed-form hyperbolic tangent solution for instantaneous velocity:</p>
      $$\int_0^v \frac{dv}{1 - \frac{v^2}{v_t^2}} = g \int_0^t dt \implies v(t) = v_t \tanh\left(\frac{g t}{v_t}\right)$$
      <p>Integrating velocity with respect to time yields the exact vertical drop distance \(y(t)\) as a function of elapsed time:</p>
      $$y(t) = \int_0^t v(t') dt' = \frac{v_t^2}{g} \ln\left[\cosh\left(\frac{g t}{v_t}\right)\right]$$
      <p>Because the hyperbolic tangent function \(\tanh(x)\) asymptotically approaches 1 as \(x \to \infty\), a falling object mathematically never reaches 100% of its terminal velocity. In practical aerodynamics and ballistics, engineers define the **95% steady-state threshold** (\(v = 0.95 v_t\)). Since \(\tanh(1.8318) \approx 0.95\), the time required to attain 95% of terminal velocity is:</p>
      $$t_{95\%} \approx 1.8318 \frac{v_t}{g}$$
      <p>For an average skydiver with \(v_t = 54\text{ m/s}\), \(t_{95\%} \approx 1.8318 \times \frac{54}{9.80665} \approx 10.1\text{ seconds}\), traversing approximately \(390\text{ meters}\) (\(1,280\text{ feet}\)) of vertical airspace before acceleration ceases.</p>

      <h2>4. Comparative Aerodynamic Drag and Terminal Speeds</h2>
      <p>The following engineering data table contrasts falling masses, projected areas, drag coefficients, and resulting sea-level terminal velocities across standard projectiles and natural phenomena:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Object / System</th>
              <th>Mass (\(m\))</th>
              <th>Frontal Area (\(A\))</th>
              <th>Drag Coeff. (\(C_d\))</th>
              <th>Terminal Speed (\(v_t\))</th>
              <th>Equivalent Speed</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Skydiver (Belly-to-Earth)</td>
              <td>80.0 kg</td>
              <td>0.700 m²</td>
              <td>1.05</td>
              <td>53.9 m/s</td>
              <td>194.0 km/h (120.5 mph)</td>
            </tr>
            <tr>
              <td>Skydiver (Head-Down Dive)</td>
              <td>80.0 kg</td>
              <td>0.180 m²</td>
              <td>0.70</td>
              <td>99.6 m/s</td>
              <td>358.6 km/h (222.8 mph)</td>
            </tr>
            <tr>
              <td>Personnel Parachute</td>
              <td>100.0 kg</td>
              <td>40.00 m²</td>
              <td>1.50</td>
              <td>5.17 m/s</td>
              <td>18.6 km/h (11.6 mph)</td>
            </tr>
            <tr>
              <td>Raindrop (Large, 5 mm dia.)</td>
              <td>65.4 mg</td>
              <td>1.96 &times; 10⁻⁵ m²</td>
              <td>0.45</td>
              <td>9.1 m/s</td>
              <td>32.8 km/h (20.4 mph)</td>
            </tr>
            <tr>
              <td>Baseball (MLB Standard)</td>
              <td>145.0 g</td>
              <td>4.27 &times; 10⁻³ m²</td>
              <td>0.30</td>
              <td>42.6 m/s</td>
              <td>153.4 km/h (95.3 mph)</td>
            </tr>
            <tr>
              <td>Bowling Ball (16 lb)</td>
              <td>7.26 kg</td>
              <td>3.66 &times; 10⁻² m²</td>
              <td>0.47</td>
              <td>82.4 m/s</td>
              <td>296.6 km/h (184.3 mph)</td>
            </tr>
            <tr>
              <td>9mm Pistol Bullet (Nose Down)</td>
              <td>8.0 g</td>
              <td>6.36 &times; 10⁻⁵ m²</td>
              <td>0.295</td>
              <td>82.8 m/s</td>
              <td>298.1 km/h (185.2 mph)</td>
            </tr>
            <tr>
              <td>Dandelion Seed (Achene)</td>
              <td>0.5 mg</td>
              <td>1.25 &times; 10⁻⁴ m²</td>
              <td>1.20</td>
              <td>0.23 m/s</td>
              <td>0.83 km/h (0.51 mph)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>5. Fluid Regimes: Stokes' Law vs. Quadratic Newtonian Drag</h2>
      <p>The quadratic terminal velocity equation assumes Newtonian turbulent drag where inertial forces dominate viscous shear forces. Fluid flow characteristics are governed by the dimensionless **Reynolds Number** (\(Re\)):</p>
      $$Re = \frac{\rho v D}{\mu}$$
      <p>Where \(D\) is the characteristic diameter or dimension of the body, and \(\mu\) is dynamic fluid viscosity (\(\sim 1.81 \times 10^{-5}\text{ Pa}\cdot\text{s}\) for air at \(15^\circ\text{C}\)). Two distinct regimes dictate terminal velocity:</p>
      <ul>
        <li><strong>Laminar Creeping Flow (\(Re &lt; 1\), Stokes' Flow):</strong> For microscopic particles, atmospheric aerosols, fog droplets, and silt settling in water, viscous friction dominates. Stokes' Law dictates drag force:
        $$F_d = 6 \pi \mu r v$$
        Equating Stokes drag with net submerged weight yields the linear Stokes terminal settling velocity:
        $$v_t = \frac{2 r^2 (\rho_s - \rho_f) g}{9 \mu}$$
        Here, terminal velocity scales quadratically with particle radius (\(r^2\)) rather than the square root of radius.</li>
        <li><strong>Newtonian Turbulent Flow (\(Re &gt; 1,000\)):</strong> For macro objects falling in air (raindrops, skydivers, meteorites, vehicles), boundary layer separation creates a low-pressure turbulent wake behind the body. Pressure drag dominates skin friction, making \(C_d\) roughly constant, validating the square-root Rayleigh formula.</li>
      </ul>

      <h2>6. Atmospheric Altitude Variation and Supersonic Free Fall</h2>
      <p>Because terminal velocity is inversely proportional to the square root of fluid density (\(v_t \propto 1 / \sqrt{\rho}\)), falling objects in the upper atmosphere reach extraordinary speeds before decelerating as they enter denser air masses. Dry atmospheric air density at geopotential altitude \(h\) in the troposphere (\(h &lt; 11,000\text{ m}\)) follows the barometric formula:</p>
      $$\rho(h) = \rho_0 \left(1 - \frac{L h}{T_0}\right)^{\frac{g M}{R_0 L} - 1}$$
      <p>Where \(T_0 = 288.15\text{ K}\), \(L = 0.0065\text{ K/m}\) is the temperature lapse rate, and \(R_0\) is the universal gas constant. On October 14, 2012, skydiver Felix Baumgartner jumped from a helium balloon at an altitude of \(38,969\text{ meters}\) (\(127,851\text{ feet}\)) in the stratosphere, where air density was approximately \(0.004\text{ kg/m}^3\) (less than 0.35% of sea level). His terminal velocity reached a maximum of \(377.1\text{ m/s}\) (\(1,357.6\text{ km/h}\) or \(843.6\text{ mph}\)), Mach 1.25, demonstrating how rarefied gas density transforms subsonic terminal dynamics into supersonic shockwave regimes.</p>

      <h2>7. Step-by-Step Worked Engineering Case Studies</h2>

      <div class="worked-example-card">
        <h3>Case Study 1: Calculating Skydiver Terminal Speed in Belly-to-Earth Orientation</h3>
        <p><strong>Scenario:</strong> A skydiver with an all-up mass \(m = 85.0\text{ kg}\) (including jumpsuit, rig, and altimeter) jumps from an airplane at an altitude where air density \(\rho = 1.15\text{ kg/m}^3\). In a stable horizontal arch, their projected frontal area is \(A = 0.72\text{ m}^2\) and their measured aerodynamic drag coefficient is \(C_d = 1.08\). Compute the terminal velocity in meters per second and miles per hour.</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Identify all input parameters in SI units:</strong></p>
          <ul>
            <li>Mass \(m = 85.0\text{ kg}\)</li>
            <li>Gravitational acceleration \(g = 9.80665\text{ m/s}^2\)</li>
            <li>Air density \(\rho = 1.15\text{ kg/m}^3\)</li>
            <li>Frontal area \(A = 0.72\text{ m}^2\)</li>
            <li>Drag coefficient \(C_d = 1.08\)</li>
          </ul>

          <p><strong>Step 2: Calculate downward gravitational weight force (\(F_g\)):</strong></p>
          $$F_g = m g = 85.0 \times 9.80665 = 833.565\text{ N}$$

          <p><strong>Step 3: Calculate the aerodynamic denominator product (\(\rho A C_d\)):</strong></p>
          $$\text{Denominator} = \rho \times A \times C_d = 1.15 \times 0.72 \times 1.08 = 0.89424\text{ kg/m}$$

          <p><strong>Step 4: Apply the terminal velocity equation:</strong></p>
          $$v_t = \sqrt{\frac{2 \times 833.565}{0.89424}} = \sqrt{\frac{1667.13}{0.89424}} = \sqrt{1864.30} \approx 43.18\text{ m/s}$$

          <p><strong>Step 5: Convert into practical units:</strong></p>
          $$v_t = 43.18 \times 3.6 = 155.45\text{ km/h}$$
          $$v_t = 43.18 \times 2.23694 = 96.59\text{ mph}$$
          <p><strong>Conclusion:</strong> At this altitude, the skydiver achieves terminal equilibrium at \(43.18\text{ m/s}\) (\(96.6\text{ mph}\)), exerting exactly \(833.6\text{ N}\) of upward aerodynamic drag against their body.</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Personnel Parachute Sizing for Safe Landing Impact</h3>
        <p><strong>Scenario:</strong> Military airborne operations specify that paratroopers carrying field gear (total payload mass \(m = 120.0\text{ kg}\)) must touch down at a maximum safe vertical descent rate of \(v_t \le 6.0\text{ m/s}\) at sea level (\(\rho = 1.225\text{ kg/m}^3\)). If the round parachute canopy has a known drag coefficient \(C_d = 1.45\), calculate the minimum required canopy surface area \(A\).</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Rearrange the terminal velocity equation to isolate projected area \(A\):</strong></p>
          $$v_t = \sqrt{\frac{2 m g}{\rho A C_d}} \implies v_t^2 = \frac{2 m g}{\rho A C_d} \implies A = \frac{2 m g}{\rho C_d v_t^2}$$

          <p><strong>Step 2: Compute downward gravitational weight:</strong></p>
          $$W = 120.0 \times 9.80665 = 1176.80\text{ N}$$

          <p><strong>Step 3: Substitute values into the solved area formula:</strong></p>
          $$A = \frac{2 \times 1176.80}{1.225 \times 1.45 \times (6.0)^2} = \frac{2353.60}{1.225 \times 1.45 \times 36.0} = \frac{2353.60}{63.945} \approx 36.81\text{ m}^2$$

          <p><strong>Step 4: Determine equivalent canopy diameter for a hemispherical parachute:</strong></p>
          $$A = \frac{\pi D^2}{4} \implies D = \sqrt{\frac{4 A}{\pi}} = \sqrt{\frac{4 \times 36.81}{3.14159}} = \sqrt{46.87} \approx 6.85\text{ meters}$$
          <p><strong>Engineering Result:</strong> The parachute canopy requires a minimum projected frontal area of \(36.81\text{ m}^2\), corresponding to a nominal canopy diameter of \(6.85\text{ meters}\) (\(22.5\text{ feet}\)) to guarantee landing survivability.</p>
        </div>
      </div>

      <h2>8. Frequently Asked Questions (Technical &amp; Applied Mechanics)</h2>
      <div class="faq-accordion">
        <details class="faq-item">
          <summary>Does a heavier object fall faster in air than a lighter object?</summary>
          <div class="faq-answer">
            <p>Yes, in a fluid medium with drag resistance, a heavier object of identical geometric shape and frontal area will always achieve a higher terminal velocity. Examining the equation \(v_t = \sqrt{2mg / (\rho A C_d)}\), terminal velocity is directly proportional to \(\sqrt{m}\). While Galileo proved that all masses accelerate equally in a pure vacuum (\(g\)), fluid drag acts as an equal upward resistance force for equal sizes; thus, the heavier object requires a higher downward velocity to generate sufficient drag force to balance its larger weight (\(m g\)).</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>Can a penny dropped from a skyscraper kill someone?</summary>
          <div class="faq-answer">
            <p>No. A standard US one-cent coin weighs only \(2.5\text{ grams}\) (\(0.0025\text{ kg}\)) and has a relatively broad surface area with a fluttering, tumbling aerodynamic profile (\(C_d \approx 1.2\)). Its calculated terminal velocity is only about \(11\text{ to }14\text{ m/s}\) (\(25\text{ to }31\text{ mph}\)). At this speed, its terminal kinetic energy is less than \(0.25\text{ Joules}\), which feels like a sharp sting or flick, far below the threshold needed to penetrate human skull tissue or cause fatal trauma.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>What is the terminal velocity of a cat or squirrel falling from a high building?</summary>
          <div class="faq-answer">
            <p>Small animals exhibit very high surface-area-to-mass ratios (\(A / m\)). A small tree squirrel reaches terminal velocity at just \(10\text{ to }12\text{ m/s}\) (\(22\text{ to }27\text{ mph}\)), allowing it to survive falls from any height onto soft soil. Domestic cats reflexively spread their limbs into a horizontal parachute-like posture (the feline righting reflex), reaching a maximum terminal velocity of approximately \(27\text{ m/s}\) (\(60\text{ mph}\)), significantly lower than an adult human skydiver.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>How does temperature and humidity influence terminal velocity?</summary>
          <div class="faq-answer">
            <p>Air density (\(\rho\)) decreases with increasing temperature according to the Ideal Gas Law (\(P = \rho R T \implies \rho = P / (RT)\)), causing terminal velocity to increase in hot weather. Counterintuitively, humid air is less dense than dry air because water vapor (\(M = 18.015\text{ g/mol}\)) is lighter than diatomic nitrogen and oxygen (\(M \approx 28.97\text{ g/mol}\)). Consequently, high humidity marginally reduces air density and slightly increases terminal falling speed.</p>
          </div>
        </details>
      </div>

      <h2>9. Related Classical Mechanics and Aerodynamic Calculators</h2>
      <p>Explore our integrated suite of engineering and physical dynamic tools to analyze motion, forces, and material responses:</p>
      <div class="related-calculators" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-top: 1rem;">
        <a href="force-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Force Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Solve Newton's Second Law ($F = ma$) and gravitational weight across planetary bodies.</p>
        </a>
        <a href="momentum-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Momentum Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Calculate linear momentum ($p = mv$) and elastic collision kinetic energy conservation.</p>
        </a>
        <a href="impulse-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Impulse Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Compute crash impact attenuation ($J = F\Delta t = \Delta p$) and rocket specific impulse.</p>
        </a>
        <a href="density-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Density Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Convert fluid densities ($\rho = m/V$) and evaluate Archimedes buoyancy thresholds.</p>
        </a>
      </div>
    </article>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-col">
        <h3>CalcHub</h3>
        <p>Your comprehensive engineering, mathematical, physical, and financial computational authority.</p>
      </div>
      <div class="footer-col">
        <h3>Calculators</h3>
        <ul>
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="math.html">Mathematics</a></li>
          <li><a href="converter.html">Unit Converters</a></li>
          <li><a href="engineering.html">Electrical &amp; Engineering</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h3>Physics &amp; Mechanics</h3>
        <ul>
          <li><a href="speed-calculator.html">Speed Calculator</a></li>
          <li><a href="density-calculator.html">Density Calculator</a></li>
          <li><a href="terminal-velocity-calculator.html">Terminal Velocity</a></li>
          <li><a href="specific-gravity-calculator.html">Specific Gravity</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 CalcHub. High-precision engineering formulas and calculators. All rights reserved.</p>
    </div>
  </footer>

  <script>
    (function() {
      // DOM Elements
      const presetSelect = document.getElementById('tv-preset');
      const massInput = document.getElementById('tv-mass');
      const massUnit = document.getElementById('tv-mass-unit');
      const areaInput = document.getElementById('tv-area');
      const areaUnit = document.getElementById('tv-area-unit');
      const cdInput = document.getElementById('tv-cd');
      const fluidSelect = document.getElementById('tv-fluid');
      const customDensityRow = document.getElementById('tv-custom-density-row');
      const customDensityInput = document.getElementById('tv-density-custom');
      const gravityInput = document.getElementById('tv-gravity');
      const calcBtn = document.getElementById('tv-calc-btn');
      const resetBtn = document.getElementById('tv-reset-btn');

      // Outputs
      const speedPrimary = document.getElementById('tv-speed-primary');
      const speedSecondary = document.getElementById('tv-speed-secondary');
      const dragForceOut = document.getElementById('tv-drag-force');
      const kineticEnergyOut = document.getElementById('tv-kinetic-energy');
      const timeSteadyOut = document.getElementById('tv-time-to-steady');
      const distSteadyOut = document.getElementById('tv-dist-to-steady');

      const PRESETS = {
        'skydiver-belly': { mass: 80, massUnit: 'kg', area: 0.70, areaUnit: 'm2', cd: 1.05 },
        'skydiver-head': { mass: 80, massUnit: 'kg', area: 0.18, areaUnit: 'm2', cd: 0.70 },
        'raindrop': { mass: 0.034, massUnit: 'g', area: 12.5, areaUnit: 'cm2', cd: 0.45 },
        'baseball': { mass: 145, massUnit: 'g', area: 42.7, areaUnit: 'cm2', cd: 0.30 },
        'bowling-ball': { mass: 7.26, massUnit: 'kg', area: 0.0366, areaUnit: 'm2', cd: 0.47 },
        'bullet': { mass: 8.0, massUnit: 'g', area: 0.636, areaUnit: 'cm2', cd: 0.295 },
        'sphere-steel': { mass: 0.51, massUnit: 'kg', area: 19.6, areaUnit: 'cm2', cd: 0.47 },
        'parachute': { mass: 100, massUnit: 'kg', area: 40.0, areaUnit: 'm2', cd: 1.50 }
      };

      function updateDensityVisibility() {
        if (fluidSelect.value === 'custom') {
          customDensityRow.style.display = 'flex';
        } else {
          customDensityRow.style.display = 'none';
        }
      }

      function getFluidDensity() {
        if (fluidSelect.value === 'custom') {
          return parseFloat(customDensityInput.value) || 1.225;
        }
        return parseFloat(fluidSelect.value) || 1.225;
      }

      function getMassKg() {
        const val = parseFloat(massInput.value) || 0;
        const unit = massUnit.value;
        if (unit === 'g') return val / 1000;
        if (unit === 'lb') return val * 0.45359237;
        if (unit === 'oz') return val * 0.02834952;
        return val; // kg
      }

      function getAreaM2() {
        const val = parseFloat(areaInput.value) || 0;
        const unit = areaUnit.value;
        if (unit === 'cm2') return val * 0.0001;
        if (unit === 'ft2') return val * 0.09290304;
        if (unit === 'in2') return val * 0.00064516;
        return val; // m2
      }

      function calculate() {
        const m = getMassKg();
        const A = getAreaM2();
        const cd = parseFloat(cdInput.value) || 1.0;
        const rho = getFluidDensity();
        const g = parseFloat(gravityInput.value) || 9.80665;

        if (m <= 0 || A <= 0 || cd <= 0 || rho <= 0 || g <= 0) {
          speedPrimary.textContent = "-- m/s";
          speedSecondary.textContent = "Please enter positive numerical values.";
          return;
        }

        // v_t = sqrt( (2 * m * g) / (rho * A * cd) )
        const numerator = 2 * m * g;
        const denominator = rho * A * cd;
        const vt = Math.sqrt(numerator / denominator);

        // Unit conversions
        const kmh = vt * 3.6;
        const mph = vt * 2.236936;
        const fts = vt * 3.28084;

        // Equilibrium forces & metrics
        const dragForce = m * g; // in N
        const ke = 0.5 * m * vt * vt; // in J
        const keStr = ke >= 1000 ? (ke / 1000).toFixed(1) + " kJ" : ke.toFixed(1) + " J";

        // Time to 95% steady state: t95 = 1.8318 * vt / g
        const t95 = 1.8318 * (vt / g);
        // Distance to 95%: y = (vt^2 / g) * ln(cosh(1.8318)) where ln(cosh(1.8318)) approx 1.154
        const dist95 = (vt * vt / g) * 1.1544;

        // Display
        speedPrimary.textContent = vt.toFixed(2) + " m/s";
        speedSecondary.innerHTML = kmh.toFixed(1) + " km/h &bull; " + mph.toFixed(1) + " mph &bull; " + fts.toFixed(1) + " ft/s";
        dragForceOut.textContent = dragForce >= 1000 ? (dragForce / 1000).toFixed(2) + " kN" : dragForce.toFixed(1) + " N";
        kineticEnergyOut.textContent = keStr;
        timeSteadyOut.textContent = t95.toFixed(2) + " s";
        distSteadyOut.textContent = dist95 >= 1000 ? (dist95 / 1000).toFixed(2) + " km" : dist95.toFixed(1) + " m";
      }

      // Preset change handler
      presetSelect.addEventListener('change', function() {
        const key = this.value;
        if (PRESETS[key]) {
          const p = PRESETS[key];
          massInput.value = p.mass;
          massUnit.value = p.massUnit;
          areaInput.value = p.area;
          areaUnit.value = p.areaUnit;
          cdInput.value = p.cd;
          calculate();
        }
      });

      fluidSelect.addEventListener('change', function() {
        updateDensityVisibility();
        calculate();
      });

      // Inputs real-time listener
      [massInput, massUnit, areaInput, areaUnit, cdInput, customDensityInput, gravityInput].forEach(el => {
        el.addEventListener('input', function() {
          presetSelect.value = 'custom';
          calculate();
        });
        el.addEventListener('change', calculate);
      });

      calcBtn.addEventListener('click', calculate);

      resetBtn.addEventListener('click', function() {
        presetSelect.value = 'skydiver-belly';
        const p = PRESETS['skydiver-belly'];
        massInput.value = p.mass;
        massUnit.value = p.massUnit;
        areaInput.value = p.area;
        areaUnit.value = p.areaUnit;
        cdInput.value = p.cd;
        fluidSelect.value = '1.225';
        updateDensityVisibility();
        gravityInput.value = '9.80665';
        calculate();
      });

      // Initial execution
      updateDensityVisibility();
      calculate();
    })();
  </script>
</body>
</html>
"""

# 8. specific-gravity-calculator.html
HTML_SPECIFIC_GRAVITY = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Specific Gravity Calculator - Relative Density, API &amp; Baumé Converter</title>
  <meta name="description" content="Calculate specific gravity (SG = rho / rho_ref), API gravity, Baumé degrees, Brix, and liquid buoyancy. Master density ratios across solids, liquids &amp; petroleum.">
  <link rel="canonical" href="https://calchub.org/specific-gravity-calculator.html">
  <meta property="og:title" content="Specific Gravity Calculator - Relative Density &amp; Hydrometer Solver">
  <meta property="og:description" content="Free specific gravity calculator. Convert substance density to water/air references, API gravity, Baumé scale, Brix %, and submerged flotation fraction.">
  <meta property="og:url" content="https://calchub.org/specific-gravity-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Specific Gravity Calculator - Chemical &amp; Petroleum Engineering Tool">
  <meta name="twitter:description" content="Solve specific gravity and relative density with multi-scale hydrometer conversions, material benchmarks, and worked case studies.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Specific Gravity Calculator",
    "url": "https://calchub.org/specific-gravity-calculator.html",
    "description": "Calculates specific gravity (relative density), API gravity, Baumé degrees, Brix sugar percentage, and fluid flotation fractions across liquids, solids, and gases.",
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
        "name": "What is specific gravity and how is it calculated?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Specific gravity (SG), also known as relative density, is the dimensionless ratio of the density of a substance to the density of a reference material at specified temperatures and pressures: SG = rho_substance / rho_reference. For liquids and solids, pure distilled water at 4°C (1000 kg/m³ or 1.000 g/cm³) is the standard reference; for gases, dry air at standard temperature and pressure (1.225 kg/m³) is typically used."
        }
      },
      {
        "@type": "Question",
        "name": "What is the difference between specific gravity and density?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Density is an absolute physical property expressing mass per unit volume (e.g., kg/m³, g/cm³, lb/ft³), carrying physical units. In contrast, specific gravity is a dimensionless relative ratio comparing two densities. Because the density of water in the CGS system is exactly 1.000 g/cm³ at 4°C, a substance's specific gravity is numerically equal to its density expressed in grams per cubic centimeter."
        }
      },
      {
        "@type": "Question",
        "name": "What does a specific gravity less than 1.0 mean?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "For solids and liquids evaluated against water, a specific gravity of less than 1.0 (SG < 1.0) indicates that the substance is less dense than water and will float on pure water. An SG greater than 1.0 indicates that the substance is denser than water and will sink (assuming no surface tension or vessel geometry effects)."
        }
      },
      {
        "@type": "Question",
        "name": "How is specific gravity converted to API gravity in the oil industry?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The American Petroleum Institute (API) gravity is defined mathematically by the standard equation: °API = (141.5 / SG_60/60) - 131.5, where SG_60/60 is specific gravity measured at 60°F (15.56°C). Light crude oils have higher °API values (>31.1°), while heavy crude oils have low °API values (<22.3°)."
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

  <main class="page-container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo;
      <a href="engineering.html">Engineering</a> &rsaquo;
      <span>Specific Gravity Calculator</span>
    </nav>

    <div class="page-header">
      <h1 class="page-title">Specific Gravity Calculator</h1>
      <p class="page-desc">Convert substance density to specific gravity, hydrometer scales (°API, Baumé, Brix), and calculate flotation percentages and buoyancy forces.</p>
    </div>

    <div class="calc-grid">
      <!-- Calculator Column -->
      <div class="calc-card">
        <div class="calc-header">
          <h2>Relative Density &amp; Hydrometer Solver</h2>
        </div>

        <!-- Mode Selection -->
        <div class="form-group">
          <label for="sg-mode">Calculation Mode:</label>
          <select id="sg-mode" class="form-control">
            <option value="density-to-sg" selected>From Substance Density &rarr; Specific Gravity &amp; Scales</option>
            <option value="sg-to-density">From Specific Gravity (SG) &rarr; Absolute Density</option>
            <option value="api-to-sg">From API Gravity (°API) &rarr; SG &amp; Density</option>
            <option value="mass-vol">From Mass &amp; Volume &rarr; SG &amp; Density</option>
          </select>
        </div>

        <!-- Material Presets -->
        <div class="form-group">
          <label for="sg-preset">Common Material Preset:</label>
          <select id="sg-preset" class="form-control">
            <option value="custom">-- Custom Material / Liquid --</option>
            <option value="water">Pure Water (4°C: 1000.0 kg/m³, SG = 1.000)</option>
            <option value="seawater">Seawater (1025.0 kg/m³, SG = 1.025)</option>
            <option value="gasoline">Gasoline (Automotive: 720.0 kg/m³, SG = 0.720)</option>
            <option value="diesel">Diesel Fuel (850.0 kg/m³, SG = 0.850)</option>
            <option value="crude-light">Light Crude Oil (825.0 kg/m³, 40.0 °API, SG = 0.825)</option>
            <option value="crude-heavy">Heavy Crude Oil (965.0 kg/m³, 15.1 °API, SG = 0.965)</option>
            <option value="ethanol">Ethanol (Pure Ethyl Alcohol: 789.0 kg/m³, SG = 0.789)</option>
            <option value="olive-oil">Olive Oil (920.0 kg/m³, SG = 0.920)</option>
            <option value="mercury">Mercury (Liquid metal: 13,546 kg/m³, SG = 13.546)</option>
            <option value="sulfuric-acid">Sulfuric Acid (Battery Acid, 98%: 1840.0 kg/m³, SG = 1.840)</option>
            <option value="steel">Structural Steel (7850.0 kg/m³, SG = 7.850)</option>
            <option value="aluminum">Aluminum (2700.0 kg/m³, SG = 2.700)</option>
            <option value="ice">Ice (Freshwater at 0°C: 917.0 kg/m³, SG = 0.917)</option>
            <option value="oak">Oak Wood (750.0 kg/m³, SG = 0.750)</option>
          </select>
        </div>

        <!-- Density Input Panel -->
        <div id="sg-density-panel">
          <div class="form-row">
            <div class="form-group">
              <label for="sg-sub-density">Substance Density ($\rho$):</label>
              <input type="number" id="sg-sub-density" class="form-control" value="1000" step="any" min="0.0001">
            </div>
            <div class="form-group">
              <label for="sg-density-unit">Density Unit:</label>
              <select id="sg-density-unit" class="form-control">
                <option value="kg_m3" selected>Kilograms / m³ (kg/m³)</option>
                <option value="g_cm3">Grams / cm³ (g/cm³)</option>
                <option value="lb_ft3">Pounds / ft³ (lb/ft³)</option>
                <option value="lb_gal">Pounds / US Gallon (lb/gal)</option>
              </select>
            </div>
          </div>
        </div>

        <!-- SG Direct Input Panel -->
        <div id="sg-direct-panel" style="display: none;">
          <div class="form-group">
            <label for="sg-direct-val">Specific Gravity ($SG$):</label>
            <input type="number" id="sg-direct-val" class="form-control" value="1.000" step="any" min="0.0001">
          </div>
        </div>

        <!-- API Input Panel -->
        <div id="sg-api-panel" style="display: none;">
          <div class="form-group">
            <label for="sg-api-val">API Gravity ($^{\circ}\text{API}$):</label>
            <input type="number" id="sg-api-val" class="form-control" value="35.0" step="any">
          </div>
        </div>

        <!-- Mass / Volume Input Panel -->
        <div id="sg-mass-vol-panel" style="display: none;">
          <div class="form-row">
            <div class="form-group">
              <label for="sg-mass">Mass ($m$ in kg):</label>
              <input type="number" id="sg-mass" class="form-control" value="10.0" step="any" min="0.0001">
            </div>
            <div class="form-group">
              <label for="sg-volume">Volume ($V$ in Liters):</label>
              <input type="number" id="sg-volume" class="form-control" value="10.0" step="any" min="0.0001">
            </div>
          </div>
        </div>

        <!-- Reference Fluid Selection -->
        <div class="form-row">
          <div class="form-group">
            <label for="sg-ref-select">Reference Fluid ($\rho_{\text{ref}}$):</label>
            <select id="sg-ref-select" class="form-control">
              <option value="1000.0" selected>Pure Water @ 4°C (1000.0 kg/m³ / 62.43 lb/ft³)</option>
              <option value="998.2">Pure Water @ 20°C (998.2 kg/m³)</option>
              <option value="997.0">Pure Water @ 25°C (997.0 kg/m³)</option>
              <option value="999.07">Water @ 60°F / Petroleum (999.07 kg/m³)</option>
              <option value="1.225">Dry Air @ STP (1.225 kg/m³, for gas SG)</option>
              <option value="1025.0">Seawater (1025.0 kg/m³)</option>
            </select>
          </div>
        </div>

        <div class="form-actions">
          <button type="button" id="sg-calc-btn" class="btn btn-primary">Calculate Specific Gravity</button>
          <button type="button" id="sg-reset-btn" class="btn btn-secondary">Reset</button>
        </div>

        <!-- Output Hero and Cards -->
        <div id="sg-results" class="results-container" style="margin-top: 1.5rem;">
          <div class="result-hero-card" style="background: var(--surface-card, #f8fafc); padding: 1.25rem; border-radius: 8px; border: 1px solid var(--border-color, #e2e8f0); text-align: center; margin-bottom: 1rem;">
            <div class="result-label" style="font-size: 0.875rem; color: var(--text-muted, #64748b); text-transform: uppercase; font-weight: 600;">Specific Gravity ($SG$)</div>
            <div id="sg-primary-out" style="font-size: 2.25rem; font-weight: 800; color: var(--primary, #2563eb); margin: 0.25rem 0;">1.0000</div>
            <div id="sg-status-out" style="font-size: 1rem; color: var(--text-secondary, #475569); font-weight: 600;">Neutral Flotation in Water (100.0% Submerged)</div>
          </div>

          <div class="summary-metrics-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(135px, 1fr)); gap: 0.75rem;">
            <div class="metric-card" style="background: var(--surface-card, #f8fafc); padding: 0.85rem; border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0);">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Density ($\rho$)</div>
              <div id="sg-density-kgm3" style="font-size: 1.1rem; font-weight: 700;">1000.0 kg/m³</div>
              <div id="sg-density-lbft3" style="font-size: 0.75rem; color: var(--text-muted, #64748b);">62.43 lb/ft³</div>
            </div>
            <div class="metric-card" style="background: var(--surface-card, #f8fafc); padding: 0.85rem; border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0);">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">API Gravity</div>
              <div id="sg-api-out" style="font-size: 1.1rem; font-weight: 700;">10.00 °API</div>
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Water Equivalent</div>
            </div>
            <div class="metric-card" style="background: var(--surface-card, #f8fafc); padding: 0.85rem; border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0);">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Baumé Scale</div>
              <div id="sg-baume-out" style="font-size: 1.1rem; font-weight: 700;">0.00 °Bé</div>
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Hydrometer Reading</div>
            </div>
            <div class="metric-card" style="background: var(--surface-card, #f8fafc); padding: 0.85rem; border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0);">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Approx. Brix (Sugar)</div>
              <div id="sg-brix-out" style="font-size: 1.1rem; font-weight: 700;">0.00 °Bx</div>
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Aqueous Sucrose</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Reference Sidebar -->
      <aside class="sidebar-card">
        <h3>Specific Gravity Benchmarks</h3>
        <p style="font-size: 0.875rem; color: var(--text-secondary, #475569);">Standard relative density values relative to pure water ($4^\circ\text{C}$):</p>
        <ul style="font-size: 0.875rem; line-height: 1.6; margin-left: 1.25rem;">
          <li><strong>Pure Gold:</strong> 19.32</li>
          <li><strong>Lead:</strong> 11.34</li>
          <li><strong>Copper:</strong> 8.96</li>
          <li><strong>Cast Iron:</strong> 7.20</li>
          <li><strong>Structural Steel:</strong> 7.85</li>
          <li><strong>Aluminum:</strong> 2.70</li>
          <li><strong>Concrete:</strong> 2.30 – 2.50</li>
          <li><strong>Seawater:</strong> 1.025</li>
          <li><strong>Pure Water:</strong> 1.000</li>
          <li><strong>Olive Oil:</strong> 0.915 – 0.920</li>
          <li><strong>Freshwater Ice:</strong> 0.917</li>
          <li><strong>Automotive Gasoline:</strong> 0.710 – 0.770</li>
        </ul>

        <h3 style="margin-top: 1.25rem;">Hydrometer Formula Quick Guide</h3>
        <ul style="font-size: 0.875rem; line-height: 1.6; margin-left: 1.25rem;">
          <li>\(^{\circ}\text{API} = \frac{141.5}{SG} - 131.5\)</li>
          <li>\(^{\circ}\text{Bé (heavy)} = 145 - \frac{145}{SG}\)</li>
          <li>\(^{\circ}\text{Bé (light)} = \frac{140}{SG} - 130\)</li>
          <li>\(^{\circ}\text{Bx} \approx 261.3 \times \left(1 - \frac{1}{SG}\right)\)</li>
        </ul>
      </aside>
    </div>

    <!-- Long-Form Informational Engineering Article (1,400+ Words) -->
    <article class="article-body">
      <h2>1. The Definition and Fundamental Principles of Specific Gravity</h2>
      <p>Specific gravity (\(SG\)), historically designated as **relative density**, is defined as the dimensionless ratio between the mass density of a test material and the mass density of a standard reference substance under specified thermal and barometric reference conditions. Formally, for any solid, liquid, or gas:</p>
      $$SG = \frac{\rho_{\text{substance}}}{\rho_{\text{reference}}} = \frac{m / V}{\rho_{\text{reference}}}$$
      <p>Where \(\rho_{\text{substance}}\) is the volumetric mass density of the investigated material (\(\text{kg/m}^3\) or \(\text{g/cm}^3\)), and \(\rho_{\text{reference}}\) is the density of the reference benchmark at standard calibration temperature. In physical sciences, materials engineering, and chemical processing:</p>
      <ul>
        <li><strong>For Liquids and Solids:</strong> The universal reference standard is pure, gas-free distilled water at its temperature of maximum density: \(3.98^\circ\text{C}\) (\(\approx 4.0^\circ\text{C}\)) under standard atmospheric pressure (\(101.325\text{ kPa}\)). At this point, \(\rho_{\text{water}} = 1000.0\text{ kg/m}^3 = 1.000\text{ g/cm}^3 = 62.428\text{ lb/ft}^3\).</li>
        <li><strong>For Gases and Vapors:</strong> The universal reference standard is dry, carbon-dioxide-free air at standard temperature and pressure (\(0^\circ\text{C}\) or \(15^\circ\text{C}\) and \(1\text{ atm}\)), where \(\rho_{\text{air}} \approx 1.225\text{ kg/m}^3\) (at \(15^\circ\text{C}\)) or \(1.293\text{ kg/m}^3\) (at \(0^\circ\text{C}\)).</li>
      </ul>
      <p>Because specific gravity is a ratio of two identical physical dimensions (\([\text{M}\cdot\text{L}^{-3}] / [\text{M}\cdot\text{L}^{-3}]\)), all physical units cancel out completely, yielding a pure **dimensionless scalar**. This property makes specific gravity universally interoperable across SI metric units and imperial engineering standards without requiring unit conversion constants.</p>

      <h2>2. Flotation, Buoyancy, and Archimedes' Principle</h2>
      <p>A primary mechanical consequence of specific gravity is the prediction of equilibrium flotation behavior in fluid environments. According to Archimedes' Principle, a body partially or completely submerged in a static fluid experiences an upward buoyant force (\(F_b\)) equal to the weight of the fluid displaced by the body:</p>
      $$F_b = \rho_{\text{fluid}} V_{\text{submerged}} g$$
      <p>Meanwhile, the downward gravitational weight of the object is:</p>
      $$W = m g = \rho_{\text{solid}} V_{\text{total}} g$$
      <p>For an unconstrained floating object in static equilibrium, upward buoyancy must exactly balance downward weight (\(F_b = W\)):</p>
      $$\rho_{\text{fluid}} V_{\text{submerged}} g = \rho_{\text{solid}} V_{\text{total}} g \implies \frac{V_{\text{submerged}}}{V_{\text{total}}} = \frac{\rho_{\text{solid}}}{\rho_{\text{fluid}}}$$
      <p>When the fluid medium is pure water (\(\rho_{\text{fluid}} = \rho_{\text{ref}}\)), this ratio simplifies directly to the solid's specific gravity:</p>
      $$\text{Flotation Fraction Submerged } (f_{\text{sub}}) = \frac{SG_{\text{solid}}}{SG_{\text{fluid}}}$$
      <p>This governing principle explains fundamental physical behaviors:</p>
      <ul>
        <li><strong>\(SG &lt; 1.0\):</strong> The object is less dense than water and floats stably on the surface. The exact percentage of the object submerged equals \(SG \times 100\%\). For instance, freshwater ice has \(SG \approx 0.917\); therefore, exactly \(91.7\%\) of an iceberg's total volume remains submerged beneath freshwater, with only \(8.3\%\) visible above the waterline. In denser ocean seawater (\(SG = 1.025\)), the submerged fraction is \(0.917 / 1.025 \approx 89.5\%\).</li>
        <li><strong>\(SG = 1.0\):</strong> The object exhibits neutral buoyancy, neither rising nor sinking, maintaining equilibrium at any depth within the fluid column.</li>
        <li><strong>\(SG &gt; 1.0\):</strong> The object is denser than water and sinks to the bottom unless counteracted by dynamic lift or buoyant containment chambers (such as submarine ballast tanks).</li>
      </ul>

      <h2>3. Industrial Hydrometer Scales: API, Baumé, Brix, and Plato</h2>
      <p>In chemical manufacturing, petroleum refining, brewing, and battery maintenance, specific gravity is measured experimentally using calibrated glass hydrometers or digital oscillating U-tube densitometers. Historical industries created dedicated non-linear hydrometer scales to linearize measurements or quantify dissolved chemical concentrations:</p>

      <h3>A. American Petroleum Institute (API) Gravity</h3>
      <p>Adopted by the global oil and gas industry, API gravity provides an inverse scale where lighter, higher-value hydrocarbon distillates (such as gasoline and jet fuel) have high numerical values, while heavy residual fuel oils have low values. The standard formula defined by the American Petroleum Institute at \(60^\circ\text{F}\) (\(15.56^\circ\text{C}\)) is:</p>
      $$^{\circ}\text{API} = \frac{141.5}{SG_{60/60}} - 131.5 \iff SG_{60/60} = \frac{141.5}{^{\circ}\text{API} + 131.5}$$
      <p>Under this standard, pure water at \(60^\circ\text{F}\) has \(SG = 1.000\), yielding exactly \(^{\circ}\text{API} = (141.5 / 1.0) - 131.5 = 10.0^\circ\text{API}\). Crude oils are categorized globally as:</p>
      <ul>
        <li><strong>Light Crude:</strong> \(^{\circ}\text{API} &gt; 31.1^\circ\) (\(SG &lt; 0.870\)) — high gasoline yield, lowest refining cost.</li>
        <li><strong>Medium Crude:</strong> \(22.3^\circ \le ^{\circ}\text{API} \le 31.1^\circ\) (\(0.870 \le SG \le 0.920\)).</li>
        <li><strong>Heavy Crude:</strong> \(10.0^\circ \le ^{\circ}\text{API} &lt; 22.3^\circ\) (\(0.920 &lt; SG \le 1.000\)).</li>
        <li><strong>Extra Heavy / Bitumen:</strong> \(^{\circ}\text{API} &lt; 10.0^\circ\) (\(SG &gt; 1.000\)) — denser than water, sinks in freshwater spills.</li>
      </ul>

      <h3>B. The Baumé Scale (°Bé)</h3>
      <p>Developed in 1768 by French chemist Antoine Baumé, this scale was historically used in industrial acid, alkali, and pharmaceutical production. Because liquids may be heavier or lighter than water, two distinct equations exist:</p>
      $$\text{For liquids heavier than water } (SG \ge 1.0): \quad ^{\circ}\text{Bé} = 145 - \frac{145}{SG} \iff SG = \frac{145}{145 - ^{\circ}\text{Bé}}$$
      $$\text{For liquids lighter than water } (SG &lt; 1.0): \quad ^{\circ}\text{Bé} = \frac{140}{SG} - 130 \iff SG = \frac{140}{130 + ^{\circ}\text{Bé}}$$

      <h3>C. The Brix Scale (°Bx) and Plato (°P)</h3>
      <p>In agriculture, fruit juice processing, winemaking, and brewing, specific gravity directly correlates with dissolved sucrose sugar content. One degree Brix (\(1^\circ\text{Bx}\)) corresponds to \(1\text{ gram}\) of sucrose dissolved in \(100\text{ grams}\) of aqueous solution (\(1\%\text{ w/w}\)). The approximate conversion between specific gravity and degrees Brix at \(20^\circ\text{C}\) is:</p>
      $$^{\circ}\text{Bx} \approx 261.3 \times \left(1 - \frac{1}{SG}\right) \approx 182.4601 \times SG^3 - 775.6821 \times SG^2 + 1262.7794 \times SG - 669.5622$$

      <h2>4. Comprehensive Material Specific Gravity Reference Table</h2>
      <p>The following engineering benchmark table lists specific gravity values, standard mass densities, and industrial flotation behavior across representative metals, construction materials, petrochemicals, and biological fluids:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Material / Substance</th>
              <th>Specific Gravity (\(SG\))</th>
              <th>Density (\(\text{kg/m}^3\))</th>
              <th>Density (\(\text{lb/ft}^3\))</th>
              <th>Flotation Status in Water</th>
              <th>Primary Industrial Application</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Gold (Pure, 24k)</td>
              <td>19.32</td>
              <td>19,320</td>
              <td>1,206.1</td>
              <td>Sinks rapidly</td>
              <td>Precious metal, electronics bonding</td>
            </tr>
            <tr>
              <td>Mercury (Liquid metal)</td>
              <td>13.55</td>
              <td>13,546</td>
              <td>845.6</td>
              <td>Sinks (liquids float on it)</td>
              <td>Barometers, chemical electrodes</td>
            </tr>
            <tr>
              <td>Lead (Pure Pb)</td>
              <td>11.34</td>
              <td>11,340</td>
              <td>707.9</td>
              <td>Sinks rapidly</td>
              <td>Radiation shielding, battery plates</td>
            </tr>
            <tr>
              <td>Copper</td>
              <td>8.96</td>
              <td>8,960</td>
              <td>559.3</td>
              <td>Sinks</td>
              <td>Electrical conductors, heat exchangers</td>
            </tr>
            <tr>
              <td>Structural Steel (A36)</td>
              <td>7.85</td>
              <td>7,850</td>
              <td>490.1</td>
              <td>Sinks</td>
              <td>Civil frameworks, pressure vessels</td>
            </tr>
            <tr>
              <td>Aluminum (6061-T6)</td>
              <td>2.70</td>
              <td>2,700</td>
              <td>168.6</td>
              <td>Sinks</td>
              <td>Aerospace, lightweight structural</td>
            </tr>
            <tr>
              <td>Portland Concrete</td>
              <td>2.40</td>
              <td>2,400</td>
              <td>149.8</td>
              <td>Sinks</td>
              <td>Foundations, structural slabs</td>
            </tr>
            <tr>
              <td>Sulfuric Acid (98%)</td>
              <td>1.84</td>
              <td>1,840</td>
              <td>114.9</td>
              <td>Sinks (miscible)</td>
              <td>Lead-acid battery electrolyte</td>
            </tr>
            <tr>
              <td>Human Whole Blood</td>
              <td>1.055</td>
              <td>1,055</td>
              <td>65.9</td>
              <td>Sinks slowly</td>
              <td>Clinical hematology diagnostics</td>
            </tr>
            <tr>
              <td>Ocean Seawater (3.5% sal)</td>
              <td>1.025</td>
              <td>1,025</td>
              <td>64.0</td>
              <td>Reference medium</td>
              <td>Marine naval architecture</td>
            </tr>
            <tr>
              <td>Pure Distilled Water (4°C)</td>
              <td>1.000</td>
              <td>1,000</td>
              <td>62.4</td>
              <td>Neutral benchmark</td>
              <td>Universal reference standard</td>
            </tr>
            <tr>
              <td>Olive Oil</td>
              <td>0.918</td>
              <td>918</td>
              <td>57.3</td>
              <td>Floats (91.8% submerged)</td>
              <td>Food processing, lubricants</td>
            </tr>
            <tr>
              <td>Freshwater Ice (0°C)</td>
              <td>0.917</td>
              <td>917</td>
              <td>57.2</td>
              <td>Floats (91.7% submerged)</td>
              <td>Glaciology, refrigeration</td>
            </tr>
            <tr>
              <td>Diesel Fuel No. 2</td>
              <td>0.850</td>
              <td>850</td>
              <td>53.1</td>
              <td>Floats (85.0% submerged)</td>
              <td>Compression ignition engines</td>
            </tr>
            <tr>
              <td>Automotive Gasoline</td>
              <td>0.730</td>
              <td>730</td>
              <td>45.6</td>
              <td>Floats (73.0% submerged)</td>
              <td>Internal combustion engines</td>
            </tr>
            <tr>
              <td>Balsa Wood</td>
              <td>0.160</td>
              <td>160</td>
              <td>10.0</td>
              <td>Floats (16.0% submerged)</td>
              <td>Model aircraft, core composite</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>5. Thermal Expansion and Temperature Standardization</h2>
      <p>Density decreases with temperature for nearly all fluids due to thermal expansion. Consequently, reporting specific gravity requires specifying both the test sample temperature \(T_s\) and the reference fluid temperature \(T_r\), formally denoted as:</p>
      $$SG_{T_s / T_r} = \frac{\rho_{\text{sample}}(T_s)}{\rho_{\text{reference}}(T_r)}$$
      <p>Common industrial thermal standardization pairs include:</p>
      <ul>
        <li><strong>\(SG_{20/4}\):</strong> Substance measured at \(20^\circ\text{C}\), referenced to water at its maximum density point of \(4^\circ\text{C}\). Widely used in academic laboratory chemistry and analytical physics.</li>
        <li><strong>\(SG_{20/20}\):</strong> Substance measured at \(20^\circ\text{C}\), referenced to water at \(20^\circ\text{C}\) (\(\rho = 998.2\text{ kg/m}^3\)). Standard for British and European pharmacopoeias and beverage testing.</li>
        <li><strong>\(SG_{60/60}\):</strong> Both substance and water measured at \(60^\circ\text{F}\) (\(15.56^\circ\text{C}\)). The universal standard in ASTM, API, and US petrochemical engineering.</li>
      </ul>
      <p>To convert an observed specific gravity \(SG_{T}\) measured at an off-spec temperature \(T\) to the standard reference temperature \(T_0\), chemical engineers apply volumetric thermal expansion coefficients (\(\beta\)):</p>
      $$SG_{T_0} \approx SG_T \left[1 + \beta (T - T_0)\right]$$
      <p>For petroleum hydrocarbons, \(\beta \approx 0.0008\text{ K}^{-1}\); for aqueous sugar solutions, \(\beta \approx 0.0003\text{ K}^{-1}\).</p>

      <h2>6. Step-by-Step Worked Engineering Case Studies</h2>

      <div class="worked-example-card">
        <h3>Case Study 1: Lead-Acid Battery State-of-Charge from Hydrometer SG</h3>
        <p><strong>Scenario:</strong> A power substation technician measures the specific gravity of the liquid electrolyte (dilute sulfuric acid, \(\text{H}_2\text{SO}_4\)) in a backup stationary battery cell at \(25^\circ\text{C}\) using an optical refractometer, obtaining an observed value of \(SG = 1.265\). Verify the volumetric mass density in both metric and imperial units, and determine the acid's Baumé degree.</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Identify reference density of pure water:</strong></p>
          $$\rho_{\text{ref}} = 1000.0\text{ kg/m}^3 = 62.428\text{ lb/ft}^3$$

          <p><strong>Step 2: Calculate absolute mass density:</strong></p>
          $$\rho = SG \times \rho_{\text{ref}} = 1.265 \times 1000.0 = 1265.0\text{ kg/m}^3$$
          $$\rho = 1.265 \times 62.428 = 78.97\text{ lb/ft}^3$$
          $$\rho = \frac{1265.0}{1000} = 1.265\text{ g/cm}^3$$

          <p><strong>Step 3: Calculate degrees Baumé (°Bé) for a heavy liquid (\(SG &gt; 1.0\)):</strong></p>
          $$^{\circ}\text{Bé} = 145 - \frac{145}{SG} = 145 - \frac{145}{1.265} = 145 - 114.625 = 30.375^\circ\text{Bé}$$

          <p><strong>Technical Interpretation:</strong> An electrolyte specific gravity between \(1.265\) and \(1.280\) (approx. \(30.4^\circ\text{Bé}\)) confirms a \(100\%\) fully charged lead-acid battery cell. A discharged cell drops below \(1.120\text{ SG}\) as sulfate ions deposit onto the lead plates as \(\text{PbSO}_4\), diluting the electrolyte toward pure water.</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Offshore Oil Cargo Classification from API Gravity</h3>
        <p><strong>Scenario:</strong> A petroleum surveyor measures an offshore cargo sample with a hydrometer, finding \(38.5^\circ\text{API}\) at \(60^\circ\text{F}\). The vessel's cargo tanks hold a total volume of \(85,000\text{ barrels}\) (where \(1\text{ barrel} = 42\text{ US gallons} = 0.158987\text{ m}^3\)). Compute the specific gravity, determine total cargo mass in metric tons, and classify the crude grade.</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Calculate specific gravity from API gravity:</strong></p>
          $$SG_{60/60} = \frac{141.5}{^{\circ}\text{API} + 131.5} = \frac{141.5}{38.5 + 131.5} = \frac{141.5}{170.0} = 0.83235$$

          <p><strong>Step 2: Determine absolute mass density in \(\text{kg/m}^3\):</strong></p>
          $$\rho = SG \times 999.07\text{ kg/m}^3 = 0.83235 \times 999.07 = 831.58\text{ kg/m}^3$$

          <p><strong>Step 3: Calculate total volume in cubic meters:</strong></p>
          $$V = 85,000\text{ bbl} \times 0.158987\text{ m}^3/\text{bbl} = 13,513.9\text{ m}^3$$

          <p><strong>Step 4: Calculate total cargo mass and convert to metric tons:</strong></p>
          $$M = \rho \times V = 831.58\text{ kg/m}^3 \times 13,513.9\text{ m}^3 = 11,237,899\text{ kg}$$
          $$\text{Mass in Metric Tons} = \frac{11,237,899}{1,000} = 11,237.9\text{ MT}$$

          <p><strong>Conclusion:</strong> With \(38.5^\circ\text{API} &gt; 31.1^\circ\), this cargo is classified as **Light Sweet Crude Oil** (comparable to Brent or West Texas Intermediate), delivering high gasoline and diesel distillation fractions.</p>
        </div>
      </div>

      <h2>7. Frequently Asked Questions (Applied Science &amp; Diagnostics)</h2>
      <div class="faq-accordion">
        <details class="faq-item">
          <summary>What is a urine specific gravity test in clinical medicine?</summary>
          <div class="faq-answer">
            <p>In medical urinalysis, urine specific gravity evaluates the kidney's ability to concentrate or dilute urine relative to pure water. Normal physiological values for healthy adults range from 1.005 to 1.030. Low urine SG (&lt; 1.005) suggests overhydration, diabetes insipidus, or impaired renal tubule concentration. Elevated urine SG (&gt; 1.030) indicates severe dehydration, congestive heart failure, or glycosuria (high glucose excretion in uncontrolled diabetes mellitus).</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>Why does ice float on water when most solids sink in their liquid phase?</summary>
          <div class="faq-answer">
            <p>Water exhibits a rare thermodynamic anomaly known as density inversion. In liquid form at 4°C, water molecules form dynamic hydrogen-bonded clusters at maximum packing density (1000 kg/m³). As water freezes into ice at 0°C, the molecules arrange into a rigid, open hexagonal crystalline lattice held by fixed hydrogen bonds. This open cage-like lattice increases molecular spacing and expands volume by approximately 9%, reducing solid ice density to 917 kg/m³ (SG = 0.917), causing ice to float.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>How do brewers use specific gravity to calculate alcohol by volume (ABV)?</summary>
          <div class="faq-answer">
            <p>In commercial brewing, brewers measure original gravity (OG) before fermentation, which is high (e.g., 1.055) due to dissolved fermentable sugars. During fermentation, yeast converts dense sugars (SG &gt; 1.0) into lighter ethanol (SG = 0.789) and carbon dioxide gas. When fermentation ceases, final gravity (FG) is lower (e.g., 1.010). The alcohol by volume percentage is computed via the empirical brewing equation: \(\text{ABV}\% = (\text{OG} - \text{FG}) \times 131.25\). For OG = 1.055 and FG = 1.010, \(\text{ABV} = (1.055 - 1.010) \times 131.25 = 5.91\%\).</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>Can specific gravity be measured without a hydrometer?</summary>
          <div class="faq-answer">
            <p>Yes. Laboratory pycnometers (precisely calibrated volumetric glass flasks) allow weighing exact liquid volumes on analytical balances. Modern industrial laboratories use digital oscillating U-tube densitometers (which measure the resonant frequency shift of a hollow glass tube filled with fluid) or optical refractometers (which correlate the fluid's optical refractive index directly with specific gravity via Snell's Law).</p>
          </div>
        </details>
      </div>

      <h2>8. Related Fluid Mechanics and Material Calculators</h2>
      <p>Explore our integrated directory of physical calculation engines to analyze fluid mechanics, forces, and material stresses:</p>
      <div class="related-calculators" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-top: 1rem;">
        <a href="density-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Density Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Calculate volumetric mass density ($\rho = m/V$) with imperial and metric unit conversions.</p>
        </a>
        <a href="terminal-velocity-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Terminal Velocity Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Compute fluid drag resistance, free-fall stabilization, and Reynolds number thresholds.</p>
        </a>
        <a href="pressure-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Pressure Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Solve hydrostatic head pressure ($P = \rho gh$) and Pascal force distributions.</p>
        </a>
        <a href="stress-strain-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Stress &amp; Strain Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Evaluate material yields ($\sigma = E\varepsilon$), shear deformation, and design safety margins.</p>
        </a>
      </div>
    </article>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-col">
        <h3>CalcHub</h3>
        <p>Your comprehensive engineering, mathematical, physical, and financial computational authority.</p>
      </div>
      <div class="footer-col">
        <h3>Calculators</h3>
        <ul>
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="math.html">Mathematics</a></li>
          <li><a href="converter.html">Unit Converters</a></li>
          <li><a href="engineering.html">Electrical &amp; Engineering</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h3>Chemical &amp; Petroleum</h3>
        <ul>
          <li><a href="density-calculator.html">Density Calculator</a></li>
          <li><a href="specific-gravity-calculator.html">Specific Gravity</a></li>
          <li><a href="pressure-calculator.html">Pressure Calculator</a></li>
          <li><a href="terminal-velocity-calculator.html">Terminal Velocity</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 CalcHub. High-precision engineering formulas and calculators. All rights reserved.</p>
    </div>
  </footer>

  <script>
    (function() {
      // DOM Elements
      const modeSelect = document.getElementById('sg-mode');
      const presetSelect = document.getElementById('sg-preset');
      const densityPanel = document.getElementById('sg-density-panel');
      const directPanel = document.getElementById('sg-direct-panel');
      const apiPanel = document.getElementById('sg-api-panel');
      const massVolPanel = document.getElementById('sg-mass-vol-panel');

      const subDensityInput = document.getElementById('sg-sub-density');
      const densityUnit = document.getElementById('sg-density-unit');
      const directInput = document.getElementById('sg-direct-val');
      const apiInput = document.getElementById('sg-api-val');
      const massInput = document.getElementById('sg-mass');
      const volInput = document.getElementById('sg-volume');
      const refSelect = document.getElementById('sg-ref-select');
      const calcBtn = document.getElementById('sg-calc-btn');
      const resetBtn = document.getElementById('sg-reset-btn');

      // Outputs
      const primaryOut = document.getElementById('sg-primary-out');
      const statusOut = document.getElementById('sg-status-out');
      const densityKgm3Out = document.getElementById('sg-density-kgm3');
      const densityLbft3Out = document.getElementById('sg-density-lbft3');
      const apiOut = document.getElementById('sg-api-out');
      const baumeOut = document.getElementById('sg-baume-out');
      const brixOut = document.getElementById('sg-brix-out');

      const PRESETS = {
        'water': { rhoKgm3: 1000.0, sg: 1.000 },
        'seawater': { rhoKgm3: 1025.0, sg: 1.025 },
        'gasoline': { rhoKgm3: 720.0, sg: 0.720 },
        'diesel': { rhoKgm3: 850.0, sg: 0.850 },
        'crude-light': { rhoKgm3: 825.0, sg: 0.825 },
        'crude-heavy': { rhoKgm3: 965.0, sg: 0.965 },
        'ethanol': { rhoKgm3: 789.0, sg: 0.789 },
        'olive-oil': { rhoKgm3: 920.0, sg: 0.920 },
        'mercury': { rhoKgm3: 13546.0, sg: 13.546 },
        'sulfuric-acid': { rhoKgm3: 1840.0, sg: 1.840 },
        'steel': { rhoKgm3: 7850.0, sg: 7.850 },
        'aluminum': { rhoKgm3: 2700.0, sg: 2.700 },
        'ice': { rhoKgm3: 917.0, sg: 0.917 },
        'oak': { rhoKgm3: 750.0, sg: 0.750 }
      };

      function updatePanelVisibility() {
        const mode = modeSelect.value;
        densityPanel.style.display = mode === 'density-to-sg' ? 'block' : 'none';
        directPanel.style.display = mode === 'sg-to-density' ? 'block' : 'none';
        apiPanel.style.display = mode === 'api-to-sg' ? 'block' : 'none';
        massVolPanel.style.display = mode === 'mass-vol' ? 'block' : 'none';
      }

      function getRefDensity() {
        return parseFloat(refSelect.value) || 1000.0;
      }

      function calculate() {
        const mode = modeSelect.value;
        const refDensity = getRefDensity();
        let sg = 1.0;
        let rhoKgm3 = 1000.0;

        if (mode === 'density-to-sg') {
          let rawRho = parseFloat(subDensityInput.value) || 0;
          const unit = densityUnit.value;
          if (unit === 'g_cm3') rhoKgm3 = rawRho * 1000.0;
          else if (unit === 'lb_ft3') rhoKgm3 = rawRho * 16.018463;
          else if (unit === 'lb_gal') rhoKgm3 = rawRho * 119.826427;
          else rhoKgm3 = rawRho; // kg_m3

          sg = rhoKgm3 / refDensity;
        } else if (mode === 'sg-to-density') {
          sg = parseFloat(directInput.value) || 1.0;
          rhoKgm3 = sg * refDensity;
        } else if (mode === 'api-to-sg') {
          const api = parseFloat(apiInput.value) || 10.0;
          // SG = 141.5 / (API + 131.5)
          sg = 141.5 / (api + 131.5);
          rhoKgm3 = sg * refDensity;
        } else if (mode === 'mass-vol') {
          const m = parseFloat(massInput.value) || 0;
          const vLiters = parseFloat(volInput.value) || 0;
          if (vLiters > 0) {
            const vM3 = vLiters * 0.001;
            rhoKgm3 = m / vM3;
            sg = rhoKgm3 / refDensity;
          } else {
            sg = 0;
            rhoKgm3 = 0;
          }
        }

        if (sg <= 0 || isNaN(sg)) {
          primaryOut.textContent = "--";
          statusOut.textContent = "Please enter valid positive values.";
          return;
        }

        // Secondary conversions
        const rhoLbft3 = rhoKgm3 * 0.06242796;
        
        // API Gravity: °API = (141.5 / SG) - 131.5
        const apiVal = (141.5 / sg) - 131.5;
        const apiStr = apiVal.toFixed(2) + " °API";

        // Baumé
        let baumeVal = 0;
        if (sg >= 1.0) {
          baumeVal = 145.0 - (145.0 / sg);
        } else {
          baumeVal = (140.0 / sg) - 130.0;
        }
        const baumeStr = baumeVal.toFixed(2) + " °Bé";

        // Brix approximate
        let brixVal = 261.3 * (1.0 - (1.0 / sg));
        if (brixVal < 0) brixVal = 0;
        const brixStr = brixVal.toFixed(2) + " °Bx";

        // Flotation status
        let statusText = "";
        if (sg < 0.9995) {
          const pctSub = (sg * 100).toFixed(1);
          statusText = "Floats in Water (" + pctSub + "% Submerged)";
        } else if (sg > 1.0005) {
          statusText = "Sinks in Pure Water (Specific Gravity > 1.0)";
        } else {
          statusText = "Neutral Buoyancy in Pure Water (100% Submerged)";
        }

        // Render to UI
        primaryOut.textContent = sg.toFixed(4);
        statusOut.textContent = statusText;
        densityKgm3Out.textContent = rhoKgm3.toFixed(1) + " kg/m³";
        densityLbft3Out.textContent = rhoLbft3.toFixed(2) + " lb/ft³";
        apiOut.textContent = apiStr;
        baumeOut.textContent = baumeStr;
        brixOut.textContent = brixStr;
      }

      // Presets
      presetSelect.addEventListener('change', function() {
        const val = this.value;
        if (PRESETS[val]) {
          const p = PRESETS[val];
          modeSelect.value = 'density-to-sg';
          updatePanelVisibility();
          subDensityInput.value = p.rhoKgm3;
          densityUnit.value = 'kg_m3';
          directInput.value = p.sg;
          calculate();
        }
      });

      modeSelect.addEventListener('change', function() {
        updatePanelVisibility();
        calculate();
      });

      refSelect.addEventListener('change', calculate);

      [subDensityInput, densityUnit, directInput, apiInput, massInput, volInput].forEach(el => {
        el.addEventListener('input', function() {
          presetSelect.value = 'custom';
          calculate();
        });
        el.addEventListener('change', calculate);
      });

      calcBtn.addEventListener('click', calculate);

      resetBtn.addEventListener('click', function() {
        modeSelect.value = 'density-to-sg';
        presetSelect.value = 'water';
        updatePanelVisibility();
        subDensityInput.value = '1000';
        densityUnit.value = 'kg_m3';
        directInput.value = '1.000';
        apiInput.value = '35.0';
        massInput.value = '10.0';
        volInput.value = '10.0';
        refSelect.value = '1000.0';
        calculate();
      });

      // Initial execution
      updatePanelVisibility();
      calculate();
    })();
  </script>
</body>
</html>
"""

def generate_files():
    p1 = os.path.join(BASE_DIR, "terminal-velocity-calculator.html")
    with open(p1, "w", encoding="utf-8") as f:
        f.write(HTML_TERMINAL_VELOCITY.strip() + "\n")
    print(f"Generated: {p1}")

    p2 = os.path.join(BASE_DIR, "specific-gravity-calculator.html")
    with open(p2, "w", encoding="utf-8") as f:
        f.write(HTML_SPECIFIC_GRAVITY.strip() + "\n")
    print(f"Generated: {p2}")

if __name__ == "__main__":
    generate_files()
