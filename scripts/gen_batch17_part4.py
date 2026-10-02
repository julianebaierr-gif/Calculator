# -*- coding: utf-8 -*-
"""
Script to generate Batch 17 Part 4 tools:
1. escape-velocity-calculator.html
2. free-fall-calculator.html
"""
import os

TOOL_1_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Escape Velocity Calculator | Planetary Gravity & Orbital Speed</title>
  <meta name="description" content="Calculate gravitational escape velocity, circular orbital speed, surface gravity, and Schwarzschild black hole radius for planets, moons, and celestial bodies.">
  <link rel="canonical" href="https://calchub.cloud/escape-velocity-calculator.html">
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
        "name": "Escape Velocity Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates gravitational escape speed, circular orbital velocity, surface acceleration, and event horizon radii for celestial bodies, planets, and orbital altitudes.",
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
            "name": "What is the mathematical formula for gravitational escape velocity?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The formula for gravitational escape velocity is v_e = √(2GM / r), where 'G' is the universal gravitational constant (6.67430 × 10⁻¹¹ m³/(kg·s²)), 'M' is celestial body mass in kilograms, and 'r' is distance from the center of mass in meters. At the surface of a spherical body, this can also be expressed as v_e = √(2gr), where 'g' is surface gravity."
            }
          },
          {
            "@type": "Question",
            "name": "What is the escape velocity from Earth's surface?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "At Earth's surface (mean radius 6,371 km and mass 5.972 × 10²⁴ kg), the theoretical unpowered ballistic escape velocity is approximately 11.186 km/s (40,270 km/h or 25,022 mph), ignoring atmospheric aerodynamic friction."
            }
          },
          {
            "@type": "Question",
            "name": "How does escape velocity relate to circular orbital velocity?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Escape velocity is exactly √2 (approximately 1.414) times greater than circular orbital velocity at the exact same radial distance: v_e = √2 × v_orbit. An orbiting spacecraft only needs to increase its speed by roughly 41.4% to break free into a parabolic escape trajectory."
            }
          },
          {
            "@type": "Question",
            "name": "Does a rocket have to reach escape velocity to leave Earth?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "No. Escape velocity represents the speed required for an unpowered ballistic projectile (with no ongoing propulsion) to coast to infinity. A vehicle under continuous rocket thrust could technically escape at any low, constant speed (e.g., 100 km/h), provided it carried sufficient fuel to maintain thrust against gravitational pull."
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
        <h1>Escape Velocity Calculator</h1>
        <p class="lead-text">Calculate gravitational escape speed, low-orbit circular velocity, local surface gravity, and event horizon radii across celestial bodies and custom orbital altitudes.</p>

        <div class="calc-card">
          <div class="form-group">
            <label for="presetSelect">Celestial Body Preset</label>
            <select id="presetSelect" class="form-control">
              <option value="earth" selected>Earth (M = 5.972 × 10²⁴ kg, R = 6,371 km)</option>
              <option value="moon">Moon (M = 7.342 × 10²² kg, R = 1,737 km)</option>
              <option value="mars">Mars (M = 6.417 × 10²³ kg, R = 3,390 km)</option>
              <option value="jupiter">Jupiter (M = 1.898 × 10²⁷ kg, R = 69,911 km)</option>
              <option value="sun">Sun (M = 1.989 × 10³⁰ kg, R = 696,340 km)</option>
              <option value="venus">Venus (M = 4.867 × 10²⁴ kg, R = 6,052 km)</option>
              <option value="titan">Titan (Saturn Moon, M = 1.345 × 10²³ kg, R = 2,575 km)</option>
              <option value="custom">Custom Celestial Body</option>
            </select>
          </div>

          <div class="form-row">
            <div class="form-group col-half">
              <label for="bodyMass">Celestial Body Mass (M)</label>
              <div class="input-with-unit">
                <input type="number" id="bodyMass" class="form-control" value="5.972e24" step="any">
                <select id="massUnit" class="unit-select">
                  <option value="kg" selected>kg</option>
                  <option value="earth">Earth Masses</option>
                  <option value="solar">Solar Masses</option>
                </select>
              </div>
            </div>

            <div class="form-group col-half">
              <label for="bodyRadius">Mean Equatorial Radius (R)</label>
              <div class="input-with-unit">
                <input type="number" id="bodyRadius" class="form-control" value="6371" step="any" min="0.001">
                <select id="radiusUnit" class="unit-select">
                  <option value="km" selected>Kilometers (km)</option>
                  <option value="m">Meters (m)</option>
                  <option value="mi">Miles</option>
                </select>
              </div>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group col-full">
              <label for="orbitAlt">Altitude Above Surface (h)</label>
              <div class="input-with-unit">
                <input type="number" id="orbitAlt" class="form-control" value="0" step="any" min="0">
                <select id="altUnit" class="unit-select">
                  <option value="km" selected>Kilometers (km) [0 = Surface]</option>
                  <option value="m">Meters (m)</option>
                  <option value="mi">Miles</option>
                </select>
              </div>
            </div>
          </div>

          <div class="btn-group">
            <button type="button" id="calcBtn" class="btn btn-primary">Calculate Escape Mechanics</button>
            <button type="button" id="resetBtn" class="btn btn-secondary">Reset to Earth Surface</button>
          </div>

          <div id="resultsPanel" class="results-panel">
            <div class="result-box primary-result">
              <div class="result-label">Gravitational Escape Velocity (v_e)</div>
              <div class="result-value" id="resVe">11.19 km/s</div>
              <div class="result-sub" id="resVeSub">40,270 km/h • 25,023 mph • 11,186 m/s</div>
            </div>

            <div class="result-grid">
              <div class="result-item">
                <span class="sub-label">Circular Orbital Velocity (v_orb)</span>
                <span class="sub-value" id="resVorb">7.91 km/s (28,475 km/h)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Local Gravitational Acceleration (g)</span>
                <span class="sub-value" id="resGrav">9.81 m/s² (1.000 Earth g)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Radial Distance from Core (r)</span>
                <span class="sub-value" id="resRadialDist">6,371 km</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Schwarzschild Event Horizon Radius</span>
                <span class="sub-value" id="resSchwRadius">8.87 mm (0.887 cm)</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. Astrodynamic Principles of Gravitational Escape Velocity</h2>
          <p>In orbital celestial mechanics and astrophysics, <strong>escape velocity</strong> (\(v_e\)) represents the minimum unpowered speed an object must possess at a given radial distance from a massive celestial body to overcome that body's gravitational pull and coast outward to spatial infinity without ever being pulled back into a closed bound orbit.</p>
          <p>The mathematical formulation emerges directly from the <strong>Law of Conservation of Total Mechanical Energy</strong>. For a projectile of test mass \(m\) moving radially away from a spherical body of mass \(M\), the total energy is the algebraic sum of its translational kinetic energy \(E_k\) and its Newtonian gravitational potential energy \(E_p\):</p>
          <div class="math-block">
            $$E_{\text{total}} = E_k + E_p = \frac{1}{2}m v^2 - \frac{G M m}{r}$$
          </div>
          <p>Where \(G\) is Newton’s universal gravitational constant (\(6.67430 \times 10^{-11}\text{ m}^3\text{kg}^{-1}\text{s}^{-2}\)) and \(r\) is distance from the center of mass. For the projectile to just reach infinity with zero residual velocity (\(v_\infty = 0\) as \(r \to \infty\)), its total orbital energy must equal precisely zero (\(E_{\text{total}} = 0\)). Setting the energy equation to zero and isolating velocity yields the canonical escape velocity equation:</p>
          <div class="math-block">
            $$\frac{1}{2}m v_e^2 - \frac{G M m}{r} = 0 \implies v_e = \sqrt{\frac{2GM}{r}}$$
          </div>
          <p>Notice that the mass of the escaping vehicle \(m\) cancels out entirely: a micro-satellite, a super-heavy starship, and a microscopic cosmic dust particle all require the exact same ballistic escape speed to break free from a planet's gravity well.</p>

          <h2>2. Relationship to Orbital Speed and Surface Gravity</h2>
          <p>Astrodynamics reveals two vital mathematical connections linking escape velocity to everyday planetary and orbital parameters:</p>
          <ul>
            <li><strong>Circular Orbital Velocity (\(v_{\text{orbit}}\)):</strong> For a satellite maintaining a stable circular orbit at radius \(r\), gravitational attraction supplies the exact centripetal force required (\(G M m / r^2 = m v^2 / r\)), giving \(v_{\text{orbit}} = \sqrt{GM / r}\). Comparing this to escape velocity exposes an elegant universal constant:
              <div class="math-block">
                $$v_e = \sqrt{2} \cdot v_{\text{orbit}} \approx 1.4142 \cdot v_{\text{orbit}}$$
              </div>
              This means a spacecraft coasting in Low Earth Orbit (LEO) at \(7.8\text{ km/s}\) only needs to burn enough propellant to increase its orbital speed by roughly \(41.4\%\) (\(\Delta v \approx 3.2\text{ km/s}\)) to enter a parabolic interplanetary trajectory.
            </li>
            <li><strong>Surface Gravitational Acceleration (\(g\)):</strong> Local surface acceleration is defined as \(g = GM / R^2\). Multiplying by \(R\) gives \(gR = GM / R\). Substituting this into the escape equation provides the practical surface formula:
              <div class="math-block">
                $$v_e = \sqrt{2 g R}$$
              </div>
            </li>
          </ul>

          <h2>3. Solar System Planetary Benchmark Reference Table</h2>
          <p>To assist aerospace mission planners and astrophysics students, the table below compiles the mass, mean volumetric radius, surface gravity, and surface escape velocity across all principal Solar System bodies:</p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Celestial Body</th>
                <th>Mass (kg)</th>
                <th>Mean Radius (km)</th>
                <th>Surface Gravity (\(\text{m/s}^2\))</th>
                <th>Escape Velocity (\(v_e\))</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Sun (Solar Surface / Photosphere)</td>
                <td>\(1.989 \times 10^{30}\)</td>
                <td>696,340 km</td>
                <td>274.0 m/s² (27.9 g)</td>
                <td>617.5 km/s (2,223,000 km/h)</td>
              </tr>
              <tr>
                <td>Mercury</td>
                <td>\(3.301 \times 10^{23}\)</td>
                <td>2,439.7 km</td>
                <td>3.70 m/s² (0.377 g)</td>
                <td>4.25 km/s (15,300 km/h)</td>
              </tr>
              <tr>
                <td>Venus</td>
                <td>\(4.867 \times 10^{24}\)</td>
                <td>6,051.8 km</td>
                <td>8.87 m/s² (0.905 g)</td>
                <td>10.36 km/s (37,300 km/h)</td>
              </tr>
              <tr>
                <td>Earth (Mean Sea Level)</td>
                <td>\(5.972 \times 10^{24}\)</td>
                <td>6,371.0 km</td>
                <td>9.807 m/s² (1.000 g)</td>
                <td>11.19 km/s (40,270 km/h)</td>
              </tr>
              <tr>
                <td>Moon (Lunar Surface)</td>
                <td>\(7.342 \times 10^{22}\)</td>
                <td>1,737.4 km</td>
                <td>1.62 m/s² (0.165 g)</td>
                <td>2.38 km/s (8,570 km/h)</td>
              </tr>
              <tr>
                <td>Mars</td>
                <td>\(6.417 \times 10^{23}\)</td>
                <td>3,389.5 km</td>
                <td>3.72 m/s² (0.379 g)</td>
                <td>5.03 km/s (18,100 km/h)</td>
              </tr>
              <tr>
                <td>Jupiter (1-bar cloud top)</td>
                <td>\(1.898 \times 10^{27}\)</td>
                <td>69,911 km</td>
                <td>24.79 m/s² (2.528 g)</td>
                <td>59.54 km/s (214,300 km/h)</td>
              </tr>
              <tr>
                <td>Saturn (Cloud layer)</td>
                <td>\(5.683 \times 10^{26}\)</td>
                <td>58,232 km</td>
                <td>10.44 m/s² (1.065 g)</td>
                <td>35.51 km/s (127,800 km/h)</td>
              </tr>
              <tr>
                <td>Titan (Saturn’s Atmosphere Moon)</td>
                <td>\(1.345 \times 10^{23}\)</td>
                <td>2,574.7 km</td>
                <td>1.35 m/s² (0.138 g)</td>
                <td>2.64 km/s (9,500 km/h)</td>
              </tr>
              <tr>
                <td>Pluto (Kuiper Belt Dwarf)</td>
                <td>\(1.303 \times 10^{22}\)</td>
                <td>1,188.3 km</td>
                <td>0.62 m/s² (0.063 g)</td>
                <td>1.21 km/s (4,360 km/h)</td>
              </tr>
            </tbody>
          </table>

          <h2>4. Worked Engineering Case Study: Trans-Mars Injection Velocity from LEO</h2>
          <div class="worked-example-card">
            <h3>Problem Statement</h3>
            <p>An exploration spacecraft has been placed into a standard circular Low Earth Orbit (LEO) parking orbit at an altitude of \(h = 300\text{ km}\) above Earth's mean radius (\(R_E = 6,371\text{ km}\)). To embark on a Hohmann transfer trajectory toward Mars, mission trajectories calculate that the vehicle must achieve an unpowered hyperbolic excess velocity of \(v_\infty = 2.94\text{ km/s}\) upon departing Earth's sphere of influence.</p>
            <p><strong>Required:</strong></p>
            <ol>
              <li>Calculate the local circular orbital velocity \(v_{\text{orbit}}\) at the 300 km parking orbit.</li>
              <li>Determine the local parabolic escape velocity \(v_e\) at this orbital altitude.</li>
              <li>Calculate the required departure velocity \(v_{\text{burn}}\) and the net rocket engine delta-V (\(\Delta v\)) burn required to escape onto the Mars trajectory.</li>
            </ol>

            <h3>Step-by-Step Mathematical Solution</h3>
            <p><strong>Step 1: Determine total radial distance \(r\) from Earth's center:</strong></p>
            <div class="math-block">
              $$r = R_E + h = 6,371\text{ km} + 300\text{ km} = 6,671\text{ km} = 6.671 \times 10^6\text{ m}$$
            </div>
            <p>Earth's standard gravitational parameter: \(\mu = GM = 3.986004418 \times 10^{14}\text{ m}^3/\text{s}^2\).</p>

            <p><strong>Step 2: Calculate circular orbital speed \(v_{\text{orbit}}\):</strong></p>
            <div class="math-block">
              $$v_{\text{orbit}} = \sqrt{\frac{\mu}{r}} = \sqrt{\frac{3.9860 \times 10^{14}}{6.671 \times 10^6}} = \sqrt{5.9751 \times 10^7} \approx 7,730\text{ m/s (7.730 km/s)}$$
            </div>

            <p><strong>Step 3: Calculate local escape velocity \(v_e\) at 300 km altitude:</strong></p>
            <div class="math-block">
              $$v_e = \sqrt{\frac{2\mu}{r}} = \sqrt{2} \times 7,730\text{ m/s} \approx 10,932\text{ m/s (10.932 km/s)}$$
            </div>
            <p>Notice that because the spacecraft is 300 km above the surface, local escape velocity has reduced from the surface value of \(11.19\text{ km/s}\) down to \(10.93\text{ km/s}\).</p>

            <p><strong>Step 4: Compute departure injection velocity \(v_{\text{burn}}\) with hyperbolic excess:</strong></p>
            <p>According to the orbital vis-viva energy conservation equation:</p>
            <div class="math-block">
              $$v_{\text{burn}}^2 = v_e^2 + v_\infty^2$$
            </div>
            <div class="math-block">
              $$v_{\text{burn}} = \sqrt{(10.932)^2 + (2.940)^2} = \sqrt{119.51 + 8.64} = \sqrt{128.15} \approx 11.320\text{ km/s}$$
            </div>

            <p><strong>Step 5: Determine required rocket engine burn delta-V (\(\Delta v\)):</strong></p>
            <div class="math-block">
              $$\Delta v = v_{\text{burn}} - v_{\text{orbit}} = 11.320\text{ km/s} - 7.730\text{ km/s} = 3.590\text{ km/s (3,590 m/s)}$$
            </div>
            <p><strong>Engineering Result:</strong> The spacecraft upper stage must perform a prograde thrust maneuver delivering exactly \(3,590\text{ m/s}\) of delta-V at perigee, leveraging the Oberth effect to inject the payload onto the transfer orbit toward Mars.</p>
          </div>

          <h2>5. Black Holes and the Schwarzschild Singularity Boundary</h2>
          <p>What happens if a celestial mass is compressed so densely that its calculated escape velocity matches or exceeds the ultimate physical speed limit of the universe—the speed of light in vacuum (\(c = 299,792,458\text{ m/s}\))? Setting \(v_e = c\) in Newton's escape equation yields Karl Schwarzschild's general relativistic formula for the radius of a non-rotating black hole's <strong>Event Horizon</strong>:</p>
          <div class="math-block">
            $$c = \sqrt{\frac{2GM}{R_s}} \implies R_s = \frac{2GM}{c^2}$$
          </div>
          <p>If our Earth were compressed into a black hole, its entire mass would have to be squeezed into a sphere with a radius of just \(8.87\text{ millimeters}\) (smaller than a marble). For our Sun, the Schwarzschild radius is approximately \(2.95\text{ kilometers}\). Within this event horizon boundary, spacetime curvature is so severe that all prospective null trajectories point inexorably toward the central gravitational singularity.</p>

          <h2>6. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-item">
            <h3>Does the direction of launch affect escape velocity?</h3>
            <p>In pure spherical gravity, escape velocity is a scalar magnitude: launching at any angle above the horizon (neglecting atmospheric drag and planetary obstacles) enables escape with the exact same initial speed. However, launching eastward from near the equator allows rockets to take advantage of Earth’s rotational surface speed (\(\approx 465\text{ m/s}\)), significantly reducing propellant requirements.</p>
          </div>
          <div class="faq-item">
            <h3>Why is escape velocity smaller at higher altitudes?</h3>
            <p>Because gravitational potential energy weakens inversely with radial distance (\(U \propto -1/r\)), a spacecraft already stationed high above a planet is situated shallower in the gravitational well. Consequently, less kinetic energy is required to bridge the remaining potential barrier to infinity.</p>
          </div>
          <div class="faq-item">
            <h3>How does atmospheric drag influence actual spacecraft escape requirements?</h3>
            <p>Atmospheric friction renders direct sea-level launches at escape velocity (\(11.2\text{ km/s}\)) utterly impossible: hypersonic air resistance would incinerate the vehicle within seconds. Rockets therefore climb vertically through dense lower air layers at moderate subsonic and supersonic speeds before performing their high-velocity horizontal acceleration burns in the vacuum of space.</p>
          </div>
          <div class="faq-item">
            <h3>What is the difference between escape velocity and orbital velocity?</h3>
            <p>Orbital velocity (\(v_{\text{orbit}} = \sqrt{GM/r}\)) creates a closed, repeating circular or elliptical trajectory around the central body. Escape velocity (\(v_e = \sqrt{2GM/r}\)) provides the kinetic energy to enter an open, unclosed parabolic or hyperbolic trajectory that departs the body indefinitely.</p>
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
    // Celestial Presets Data
    const presets = {
      earth: { m: 5.972e24, r: 6371 },
      moon: { m: 7.342e22, r: 1737.4 },
      mars: { m: 6.417e23, r: 3389.5 },
      jupiter: { m: 1.898e27, r: 69911 },
      sun: { m: 1.989e30, r: 696340 },
      venus: { m: 4.867e24, r: 6051.8 },
      titan: { m: 1.345e23, r: 2574.7 }
    };

    const G = 6.67430e-11;
    const c_light = 299792458;

    const toKg = (m, unit) => {
      switch(unit) {
        case 'earth': return m * 5.972e24;
        case 'solar': return m * 1.989e30;
        default: return m;
      }
    };
    const toMeters = (r, unit) => {
      switch(unit) {
        case 'km': return r * 1000;
        case 'mi': return r * 1609.344;
        default: return r;
      }
    };

    function applyPreset() {
      const p = document.getElementById('presetSelect').value;
      if (p !== 'custom' && presets[p]) {
        document.getElementById('bodyMass').value = presets[p].m;
        document.getElementById('massUnit').value = 'kg';
        document.getElementById('bodyRadius').value = presets[p].r;
        document.getElementById('radiusUnit').value = 'km';
        document.getElementById('orbitAlt').value = '0';
        document.getElementById('altUnit').value = 'km';
      }
      calculate();
    }

    function calculate() {
      const rawMass = parseFloat(document.getElementById('bodyMass').value) || 0;
      const massUnit = document.getElementById('massUnit').value;
      const M = toKg(rawMass, massUnit);

      const rawRadius = parseFloat(document.getElementById('bodyRadius').value) || 1;
      const radiusUnit = document.getElementById('radiusUnit').value;
      const R_m = toMeters(rawRadius, radiusUnit);

      const rawAlt = parseFloat(document.getElementById('orbitAlt').value) || 0;
      const altUnit = document.getElementById('altUnit').value;
      const h_m = toMeters(rawAlt, altUnit);

      const total_r = R_m + h_m;

      if (total_r <= 0 || M <= 0) return;

      // v_e = sqrt(2*G*M / r)
      const v_e = Math.sqrt((2 * G * M) / total_r);
      const v_orb = v_e / Math.SQRT2;

      // local gravity g = G*M / r^2
      const g_local = (G * M) / (total_r * total_r);
      const g_ratio = g_local / 9.80665;

      // Schwarzschild radius R_s = 2*G*M / c^2
      const R_s = (2 * G * M) / (c_light * c_light);

      // Render Outputs
      const ve_kms = v_e / 1000;
      const ve_kph = v_e * 3.6;
      const ve_mph = v_e * 2.23694;

      document.getElementById('resVe').textContent = ve_kms.toFixed(2) + " km/s";
      document.getElementById('resVeSub').textContent = 
        ve_kph.toLocaleString('en-US', {maximumFractionDigits: 0}) + " km/h • " + 
        ve_mph.toLocaleString('en-US', {maximumFractionDigits: 0}) + " mph • " + 
        v_e.toLocaleString('en-US', {maximumFractionDigits: 0}) + " m/s";

      const vorb_kms = v_orb / 1000;
      document.getElementById('resVorb').textContent = 
        vorb_kms.toFixed(2) + " km/s (" + (v_orb * 3.6).toLocaleString('en-US', {maximumFractionDigits: 0}) + " km/h)";

      document.getElementById('resGrav').textContent = 
        g_local.toFixed(2) + " m/s² (" + g_ratio.toFixed(3) + " Earth g)";

      document.getElementById('resRadialDist').textContent = 
        (total_r / 1000).toLocaleString('en-US', {maximumFractionDigits: 1}) + " km";

      if (R_s < 0.01) {
        document.getElementById('resSchwRadius').textContent = (R_s * 1000).toFixed(2) + " mm (" + (R_s * 100).toFixed(3) + " cm)";
      } else if (R_s < 1000) {
        document.getElementById('resSchwRadius').textContent = R_s.toFixed(2) + " m";
      } else {
        document.getElementById('resSchwRadius').textContent = (R_s / 1000).toFixed(2) + " km";
      }
    }

    document.getElementById('presetSelect').addEventListener('change', applyPreset);
    document.querySelectorAll('input, select').forEach(el => {
      if (el.id !== 'presetSelect') {
        el.addEventListener('input', () => {
          document.getElementById('presetSelect').value = 'custom';
          calculate();
        });
        el.addEventListener('change', () => {
          document.getElementById('presetSelect').value = 'custom';
          calculate();
        });
      }
    });

    document.getElementById('calcBtn').addEventListener('click', calculate);
    document.getElementById('resetBtn').addEventListener('click', () => {
      document.getElementById('presetSelect').value = 'earth';
      applyPreset();
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
  <title>Free Fall Calculator | Gravity, Terminal Velocity & Fall Time</title>
  <meta name="description" content="Calculate free fall time, impact speed, distance fallen, and terminal velocity with aerodynamic air drag or in vacuum across Earth, Moon, and Mars.">
  <link rel="canonical" href="https://calchub.cloud/free-fall-calculator.html">
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
        "name": "Free Fall Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates free fall drop duration, impact velocity, distance fallen, aerodynamic drag effects, and terminal velocity in atmospheric air or planetary vacuum.",
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
            "name": "What are the primary kinematic formulas for free fall in a vacuum?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For free fall from rest in a vacuum under constant gravity g (9.80665 m/s² on Earth): impact velocity is v = g × t = √(2gh), fall duration is t = √(2h / g), and fall height is h = ½ × g × t²."
            }
          },
          {
            "@type": "Question",
            "name": "How does aerodynamic drag determine terminal velocity?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "As an object accelerates downwards, aerodynamic drag increases with the square of speed: F_drag = ½ × ρ × C_d × A × v². When drag equals gravitational weight (F_drag = mg), net acceleration drops to zero and the object falls at constant terminal velocity: v_t = √((2mg) / (ρ × C_d × A))."
            }
          },
          {
            "@type": "Question",
            "name": "What is the typical terminal velocity of a human skydiver?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In a standard belly-to-earth flat stable body position (cross-sectional area ~0.7 m², drag coefficient ~1.0), an adult skydiver reaches a terminal velocity of roughly 54 m/s (194 km/h or 120 mph) at sea level. In a head-down streamlined dive, terminal velocity can exceed 90 m/s (324 km/h or 200 mph)."
            }
          },
          {
            "@type": "Question",
            "name": "Did Galileo prove that all objects fall at the same rate regardless of mass?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes. In the absence of atmospheric air resistance (such as inside a vacuum chamber or on the surface of the Moon), the gravitational acceleration g = GM / R² is independent of the falling object's mass. A hammer and a falcon feather dropped simultaneously strike the ground at the exact same instant."
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
        <h1>Free Fall Calculator</h1>
        <p class="lead-text">Calculate free fall impact velocity, drop duration, distance fallen, terminal velocity, and kinetic energy with aerodynamic drag or in a vacuum.</p>

        <div class="calc-card">
          <div class="form-row">
            <div class="form-group col-half">
              <label for="calcMode">Solve Based On</label>
              <select id="calcMode" class="form-control">
                <option value="from_h" selected>Drop Height (Distance fallen)</option>
                <option value="from_t">Fall Duration (Time elapsed)</option>
                <option value="from_v">Impact Velocity</option>
              </select>
            </div>

            <div class="form-group col-half">
              <label for="gravPreset">Gravity Environment</label>
              <select id="gravPreset" class="form-control">
                <option value="9.80665" selected>Earth Surface (g = 9.81 m/s²)</option>
                <option value="1.62">Moon (g = 1.62 m/s²)</option>
                <option value="3.72">Mars (g = 3.72 m/s²)</option>
                <option value="24.79">Jupiter (g = 24.79 m/s²)</option>
                <option value="custom">Custom Gravity</option>
              </select>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group col-half" id="grpH">
              <label for="valHeight">Drop Height / Fall Distance (h)</label>
              <div class="input-with-unit">
                <input type="number" id="valHeight" class="form-control" value="100" step="any" min="0">
                <select id="unitHeight" class="unit-select">
                  <option value="m" selected>Meters (m)</option>
                  <option value="ft">Feet (ft)</option>
                  <option value="km">Kilometers (km)</option>
                </select>
              </div>
            </div>

            <div class="form-group col-half" id="grpT" style="display:none;">
              <label for="valTime">Fall Duration (t)</label>
              <div class="input-with-unit">
                <input type="number" id="valTime" class="form-control" value="4.5" step="any" min="0">
                <select id="unitTime" class="unit-select">
                  <option value="s" selected>Seconds (s)</option>
                  <option value="min">Minutes</option>
                </select>
              </div>
            </div>

            <div class="form-group col-half" id="grpV" style="display:none;">
              <label for="valVel">Desired Impact Velocity (v)</label>
              <div class="input-with-unit">
                <input type="number" id="valVel" class="form-control" value="44.29" step="any" min="0">
                <select id="unitVel" class="unit-select">
                  <option value="mps" selected>m/s</option>
                  <option value="kph">km/h</option>
                  <option value="mph">mph</option>
                </select>
              </div>
            </div>

            <div class="form-group col-half">
              <label for="valMass">Object Mass (m) [for Energy & Drag]</label>
              <div class="input-with-unit">
                <input type="number" id="valMass" class="form-control" value="75" step="any" min="0.001">
                <select id="unitMass" class="unit-select">
                  <option value="kg" selected>kg</option>
                  <option value="lbs">lbs</option>
                  <option value="g">grams (g)</option>
                </select>
              </div>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group col-full">
              <label><input type="checkbox" id="enableDrag"> Enable Aerodynamic Air Resistance (Drag Modeling)</label>
            </div>
          </div>

          <div id="dragOptions" style="display:none; background:#f8fafc; padding:12px; border-radius:6px; margin-bottom:15px; border:1px solid #e2e8f0;">
            <div class="form-row">
              <div class="form-group col-third">
                <label for="cdSelect">Object Drag Coefficient (C_d)</label>
                <select id="cdSelect" class="form-control">
                  <option value="1.0" selected>Human Skydiver (Belly: 1.0)</option>
                  <option value="0.7">Human Skydiver (Head-first: 0.7)</option>
                  <option value="0.47">Smooth Sphere / Ball (0.47)</option>
                  <option value="1.15">Short Cylinder (1.15)</option>
                  <option value="0.04">Streamlined Teardrop (0.04)</option>
                </select>
              </div>
              <div class="form-group col-third">
                <label for="areaVal">Cross-Sectional Area (A)</label>
                <div class="input-with-unit">
                  <input type="number" id="areaVal" class="form-control" value="0.7" step="any" min="0.0001">
                  <span style="font-size:12px; padding:6px; background:#fff; border:1px solid #cbd5e1; border-left:none; border-radius:0 4px 4px 0;">m²</span>
                </div>
              </div>
              <div class="form-group col-third">
                <label for="airDensity">Air Density (&rho;)</label>
                <div class="input-with-unit">
                  <input type="number" id="airDensity" class="form-control" value="1.225" step="any" min="0.001">
                  <span style="font-size:12px; padding:6px; background:#fff; border:1px solid #cbd5e1; border-left:none; border-radius:0 4px 4px 0;">kg/m³</span>
                </div>
              </div>
            </div>
          </div>

          <div class="btn-group">
            <button type="button" id="calcBtn" class="btn btn-primary">Calculate Free Fall</button>
            <button type="button" id="resetBtn" class="btn btn-secondary">Reset to 100m Drop</button>
          </div>

          <div id="resultsPanel" class="results-panel">
            <div class="result-box primary-result">
              <div class="result-label">Impact Velocity at Ground</div>
              <div class="result-value" id="resImpactVel">44.29 m/s</div>
              <div class="result-sub" id="resVelSub">159.4 km/h • 99.1 mph • 145.3 ft/s</div>
            </div>

            <div class="result-grid">
              <div class="result-item">
                <span class="sub-label">Elapsed Fall Duration</span>
                <span class="sub-value" id="resTime">4.52 seconds</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Drop Height / Fall Distance</span>
                <span class="sub-value" id="resHeight">100.00 m (328.1 ft)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Impact Kinetic Energy</span>
                <span class="sub-value" id="resEnergy">73.55 kJ (54,248 ft-lb)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Terminal Velocity (v_t)</span>
                <span class="sub-value" id="resTermVel">54.0 m/s (194.4 km/h) [Vacuum: &infin;]</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. Classical Physics of Gravitational Free Fall</h2>
          <p>In classical mechanics, <strong>free fall</strong> refers to the state of motion of an object where gravity is the sole physical force exerting an acceleration upon it. When an object is dropped from a stationary resting position near the surface of Earth in the absence of an atmosphere, it undergoes uniform linear acceleration equal to standard gravitational acceleration (\(g = 9.80665\text{ m/s}^2\)).</p>
          <p>This fundamental property was famously articulated by Italian physicist Galileo Galilei through his conceptual thought experiments dismantling Aristotelian mechanics. Galileo proved that in a true physical vacuum, all falling bodies accelerate at the exact same uniform rate regardless of their internal mass, density, shape, or chemical composition. This was verified dramatically on the lunar surface during Apollo 15 in 1971, when astronaut David Scott dropped a 1.32 kg geological hammer and a 0.03 kg falcon feather simultaneously, watching both strike the lunar dust at the exact same instant.</p>

          <h2>2. Mathematical Formulations: Vacuum Free Fall Kinematics</h2>
          <p>Under idealized vacuum conditions with constant gravitational acceleration \(g\), the motion of a body falling from rest (\(u = 0\)) is completely characterized by the standard Newtonian kinematic relationships:</p>
          <div class="math-block">
            $$v = g \cdot t = \sqrt{2gh}$$
          </div>
          <div class="math-block">
            $$h = \frac{1}{2} g t^2 = \frac{v^2}{2g}$$
          </div>
          <div class="math-block">
            $$t = \frac{v}{g} = \sqrt{\frac{2h}{g}}$$
          </div>
          <p>Upon impact with the surface after falling through height \(h\), the body’s initial gravitational potential energy (\(E_p = mgh\)) is converted entirely into translational kinetic energy (\(E_k = \frac{1}{2}mv^2\)):</p>
          <div class="math-block">
            $$E_k = \frac{1}{2} m v^2 = mgh$$
          </div>

          <h2>3. Atmospheric Air Resistance and Terminal Velocity Dynamics</h2>
          <p>In realistic terrestrial engineering environments, falling bodies interact with the surrounding atmospheric gas. As the downward velocity \(v\) increases, the body displaces air molecules, generating an upward aerodynamic drag force \(F_{\text{drag}}\) that opposes gravitational downward weight (\(F_g = mg\)). For turbulent Reynolds numbers characteristic of macro-scale drops, drag follows Lord Rayleigh's quadratic formulation:</p>
          <div class="math-block">
            $$F_{\text{drag}} = \frac{1}{2} \rho \cdot C_d \cdot A \cdot v^2$$
          </div>
          <p>Where \(\rho\) is ambient atmospheric air density (\(1.225\text{ kg/m}^3\) at sea level and \(15^\circ\text{C}\)), \(C_d\) is the dimensionless aerodynamic drag coefficient, \(A\) is the projected cross-sectional area perpendicular to the velocity vector (\(\text{m}^2\)), and \(v\) is instantaneous downward speed (\(\text{m/s}\)).</p>
          <p>By applying Newton's second law of motion, the instantaneous acceleration \(a(t)\) of the falling body is:</p>
          <div class="math-block">
            $$m \frac{dv}{dt} = mg - \frac{1}{2}\rho C_d A v^2 \implies a(t) = g \left(1 - \frac{v^2}{v_t^2}\right)$$
          </div>
          <p>As the velocity climbs, the opposing drag force grows quadratically until it precisely balances gravitational weight (\(F_{\text{drag}} = mg\)). At this equilibrium point, net acceleration drops identically to zero (\(a = 0\)), and the body continues falling at a constant maximum speed designated as <strong>terminal velocity</strong> (\(v_t\)):</p>
          <div class="math-block">
            $$mg = \frac{1}{2} \rho C_d A v_t^2 \implies v_t = \sqrt{\frac{2mg}{\rho C_d A}}$$
          </div>
          <p>Integrating the differential equation with initial condition \(v(0) = 0\) produces the closed-form hyperbolic tangent velocity equation:</p>
          <div class="math-block">
            $$v(t) = v_t \tanh\left(\frac{gt}{v_t}\right)$$
          </div>

          <h2>4. Engineering Benchmark Terminal Velocity Reference Table</h2>
          <p>To assist aerospace safety engineers, ballistics analysts, and meteorologists, the table below documents representative terminal velocities and drag parameters at sea level:</p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Falling Object / Physical System</th>
                <th>Typical Mass (\(m\))</th>
                <th>Cross-Section (\(A\))</th>
                <th>Drag Coeff (\(C_d\))</th>
                <th>Terminal Velocity (\(v_t\))</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Atmospheric Raindrop (Medium droplet, 2 mm)</td>
                <td>4.2 mg</td>
                <td>\(3.1 \times 10^{-6}\text{ m}^2\)</td>
                <td>0.60</td>
                <td>6.5 m/s (23.4 km/h)</td>
              </tr>
              <tr>
                <td>Hailstone (Severe storm, 25 mm diameter)</td>
                <td>7.5 g</td>
                <td>\(4.9 \times 10^{-4}\text{ m}^2\)</td>
                <td>0.45</td>
                <td>24.0 m/s (86.4 km/h)</td>
              </tr>
              <tr>
                <td>Standard Golf Ball (42.7 mm diameter)</td>
                <td>45.9 g</td>
                <td>\(1.43 \times 10^{-3}\text{ m}^2\)</td>
                <td>0.30</td>
                <td>41.5 m/s (149.4 km/h)</td>
              </tr>
              <tr>
                <td>Adult Skydiver (Belly-to-Earth Flat Position)</td>
                <td>80.0 kg</td>
                <td>\(0.70\text{ m}^2\)</td>
                <td>1.00</td>
                <td>54.0 m/s (194.4 km/h)</td>
              </tr>
              <tr>
                <td>Adult Skydiver (Streamlined Head-First Dive)</td>
                <td>80.0 kg</td>
                <td>\(0.18\text{ m}^2\)</td>
                <td>0.70</td>
                <td>99.0 m/s (356.4 km/h)</td>
              </tr>
              <tr>
                <td>Standard Deployed Parachute (Round Military)</td>
                <td>100.0 kg (with troop)</td>
                <td>\(45.0\text{ m}^2\)</td>
                <td>1.50</td>
                <td>4.9 m/s (17.6 km/h)</td>
              </tr>
              <tr>
                <td>Stratospheric Space Jumper (Felix Baumgartner, 39 km)</td>
                <td>118.0 kg (with suit)</td>
                <td>\(0.60\text{ m}^2\) (\(\rho \approx 0.005\))</td>
                <td>0.80</td>
                <td>377 m/s (1,357 km/h, Mach 1.25)</td>
              </tr>
            </tbody>
          </table>

          <h2>5. Worked Engineering Case Study: Skydiver Drop from 4,000 Meters</h2>
          <div class="worked-example-card">
            <h3>Problem Statement</h3>
            <p>A skydiver with total equipment mass \(m = 80\text{ kg}\) jumps from a jump plane cruising at an altitude of \(4,000\text{ meters}\) above sea level. The skydiver adopts a stable spread-eagled belly-to-earth posture presenting a projected surface area of \(A = 0.70\text{ m}^2\) with an aerodynamic drag coefficient of \(C_d = 1.05\). The mean atmospheric air density is approximated at \(\rho = 1.20\text{ kg/m}^3\).</p>
            <p><strong>Required:</strong></p>
            <ol>
              <li>Compute the skydiver's terminal velocity \(v_t\) in \(\text{m/s}\) and \(\text{km/h}\).</li>
              <li>Determine the theoretical impact speed if falling in a total vacuum from 4,000 meters.</li>
              <li>Calculate the time required in the atmosphere to reach \(95\%\) of terminal velocity.</li>
            </ol>

            <h3>Step-by-Step Mathematical Solution</h3>
            <p><strong>Step 1: Compute aerodynamic terminal velocity \(v_t\):</strong></p>
            <div class="math-block">
              $$v_t = \sqrt{\frac{2mg}{\rho C_d A}} = \sqrt{\frac{2 \times 80 \times 9.80665}{1.20 \times 1.05 \times 0.70}}$$
            </div>
            <div class="math-block">
              $$v_t = \sqrt{\frac{1569.06}{0.882}} = \sqrt{1778.98} \approx 42.18\text{ m/s}$$
            </div>
            <p>Converting to kilometers per hour: \(42.18 \times 3.6 = 151.8\text{ km/h}\) (approx \(94.4\text{ mph}\)).</p>

            <p><strong>Step 2: Compare with theoretical vacuum free fall speed:</strong></p>
            <div class="math-block">
              $$v_{\text{vacuum}} = \sqrt{2gh} = \sqrt{2 \times 9.80665 \times 4000} = \sqrt{78,453} \approx 280.1\text{ m/s (1,008 km/h)}$$
            </div>
            <p>In a vacuum, the skydiver would strike the ground at over \(1,000\text{ km/h}\), underscoring that atmospheric drag dissipates over \(97\%\) of the falling body's kinetic energy into thermal heating of the air.</p>

            <p><strong>Step 3: Calculate time required to reach 95% of terminal velocity:</strong></p>
            <p>Using the hyperbolic velocity equation \(v(t) = v_t \tanh(gt / v_t)\), setting \(v/v_t = 0.95\) yields:</p>
            <div class="math-block">
              $$\tanh\left(\frac{gt}{v_t}\right) = 0.95 \implies \frac{gt}{v_t} = \text{artanh}(0.95) \approx 1.8318$$
            </div>
            <div class="math-block">
              $$t = \frac{1.8318 \times v_t}{g} = \frac{1.8318 \times 42.18}{9.80665} \approx \frac{77.27}{9.80665} \approx 7.88\text{ seconds}$$
            </div>
            <p><strong>Engineering Conclusion:</strong> Within just \(8\text{ seconds}\) of free fall and after descending approximately \(170\text{ meters}\), the skydiver achieves steady terminal velocity.</p>
          </div>

          <h2>6. Gravitational Free Fall Across the Solar System</h2>
          <p>Because free fall acceleration is dictated by \(g = GM / R^2\), drop durations and impact velocities diverge wildly across celestial worlds:</p>
          <ul>
            <li><strong>The Moon (\(g = 1.62\text{ m/s}^2\), No Atmosphere):</strong> Dropping a rock from 100 meters on the Moon takes \(t = \sqrt{2 \times 100 / 1.62} = 11.1\text{ seconds}\) and strikes at \(18.0\text{ m/s}\) (\(64.8\text{ km/h}\)), over 2.4 times slower than on Earth.</li>
            <li><strong>Mars (\(g = 3.72\text{ m/s}^2\), Ultra-Thin Atmosphere):</strong> With Martian surface gravity at \(38\%\) of Earth and atmospheric density less than \(1\%\) of Earth (\(\rho \approx 0.015\text{ kg/m}^3\)), aerodynamic terminal velocities are over 9 times higher than on Earth, demanding supersonic retro-propulsion and massive parachutes for rover landings.</li>
          </ul>

          <h2>7. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-item">
            <h3>How long does it take an object to fall 100 meters in a vacuum?</h3>
            <p>In Earth's gravitational field in a vacuum, fall time is \(t = \sqrt{2h / g} = \sqrt{200 / 9.80665} \approx 4.52\text{ seconds}\). The impact velocity upon striking the ground is \(v = gt = 9.80665 \times 4.52 = 44.29\text{ m/s}\) (\(159.4\text{ km/h}\) or \(99.1\text{ mph}\)).</p>
          </div>
          <div class="faq-item">
            <h3>Why do heavier skydivers fall faster in air?</h3>
            <p>Terminal velocity is \(v_t = \sqrt{2mg / (\rho C_d A)}\). Because mass \(m\) scales with body volume (\(\propto r^3\)) while cross-sectional area \(A\) scales with surface area (\(\propto r^2\)), larger and heavier individuals have a higher mass-to-surface-area ratio (ballistic coefficient), resulting in a noticeably higher terminal velocity.</p>
          </div>
          <div class="faq-item">
            <h3>Does free fall mean zero gravity?</h3>
            <p>No. Astronauts in low Earth orbit aboard the International Space Station experience roughly \(89\%\) of sea-level gravity (\(g \approx 8.7\text{ m/s}^2\)). They feel "weightless" because they, along with the space station, are in perpetual free fall toward Earth while maintaining sufficient tangential velocity (\(7.7\text{ km/s}\)) to continually match the curvature of the planet.</p>
          </div>
          <div class="faq-item">
            <h3>Can terminal velocity exceed the speed of sound?</h3>
            <p>Yes, at very high altitudes where atmospheric density \(\rho\) is extremely low. During the Red Bull Stratos jump from 38,969 meters, Felix Baumgartner achieved a peak terminal velocity of \(1,357.6\text{ km/h}\) (Mach 1.25) due to the near-vacuum rarefied air of the stratosphere before decelerating as he entered denser lower air.</p>
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
    // Free Fall Calculation Engine
    const toMeters = (h, unit) => {
      switch(unit) {
        case 'ft': return h * 0.3048;
        case 'km': return h * 1000;
        default: return h;
      }
    };
    const toSeconds = (t, unit) => {
      switch(unit) {
        case 'min': return t * 60;
        default: return t;
      }
    };
    const toMps = (v, unit) => {
      switch(unit) {
        case 'kph': return v / 3.6;
        case 'mph': return v * 0.44704;
        default: return v;
      }
    };
    const toKg = (m, unit) => {
      switch(unit) {
        case 'lbs': return m * 0.45359237;
        case 'g': return m / 1000;
        default: return m;
      }
    };

    function updateMode() {
      const mode = document.getElementById('calcMode').value;
      document.getElementById('grpH').style.display = mode === 'from_h' ? 'block' : 'none';
      document.getElementById('grpT').style.display = mode === 'from_t' ? 'block' : 'none';
      document.getElementById('grpV').style.display = mode === 'from_v' ? 'block' : 'none';
      calculate();
    }

    function calculate() {
      const mode = document.getElementById('calcMode').value;
      let g = parseFloat(document.getElementById('gravPreset').value) || 9.80665;
      const rawMass = parseFloat(document.getElementById('valMass').value) || 75;
      const m = toKg(rawMass, document.getElementById('unitMass').value);

      const hasDrag = document.getElementById('enableDrag').checked;
      const Cd = parseFloat(document.getElementById('cdSelect').value) || 1.0;
      const A = parseFloat(document.getElementById('areaVal').value) || 0.7;
      const rho = parseFloat(document.getElementById('airDensity').value) || 1.225;

      let v_term = Infinity;
      if (hasDrag && Cd > 0 && A > 0 && rho > 0) {
        v_term = Math.sqrt((2 * m * g) / (rho * Cd * A));
      }

      let h = 0, t = 0, v = 0;

      if (!hasDrag) {
        // Pure Vacuum Formulations
        if (mode === 'from_h') {
          h = toMeters(parseFloat(document.getElementById('valHeight').value) || 0, document.getElementById('unitHeight').value);
          t = g > 0 ? Math.sqrt((2 * h) / g) : 0;
          v = g * t;
        } else if (mode === 'from_t') {
          t = toSeconds(parseFloat(document.getElementById('valTime').value) || 0, document.getElementById('unitTime').value);
          v = g * t;
          h = 0.5 * g * t * t;
        } else if (mode === 'from_v') {
          v = toMps(parseFloat(document.getElementById('valVel').value) || 0, document.getElementById('unitVel').value);
          t = g > 0 ? v / g : 0;
          h = g > 0 ? (v * v) / (2 * g) : 0;
        }
      } else {
        // Drag Modeling via Hyperbolic Functions
        // v(t) = vt * tanh(gt / vt)
        // y(t) = (vt^2 / g) * ln(cosh(gt / vt))
        if (mode === 'from_h') {
          h = toMeters(parseFloat(document.getElementById('valHeight').value) || 0, document.getElementById('unitHeight').value);
          // Numerical / inverse solve for t: cosh(gt/vt) = exp(g*h / vt^2)
          const exponent = (g * h) / (v_term * v_term);
          if (exponent < 700) {
            const coshVal = Math.exp(exponent);
            // acosh(x) = ln(x + sqrt(x^2 - 1))
            const acoshVal = Math.log(coshVal + Math.sqrt(coshVal * coshVal - 1));
            t = (v_term / g) * acoshVal;
          } else {
            // Very high drop, effectively at terminal velocity: h = vt*t - ...
            t = h / v_term;
          }
          const tanhVal = Math.tanh((g * t) / v_term);
          v = v_term * tanhVal;
        } else if (mode === 'from_t') {
          t = toSeconds(parseFloat(document.getElementById('valTime').value) || 0, document.getElementById('unitTime').value);
          const tanhVal = Math.tanh((g * t) / v_term);
          v = v_term * tanhVal;
          // cosh(x) can overflow for large x, handle safely
          const arg = (g * t) / v_term;
          let lnCosh = 0;
          if (arg > 20) {
            lnCosh = arg - Math.LN2;
          } else {
            lnCosh = Math.log(Math.cosh(arg));
          }
          h = ((v_term * v_term) / g) * lnCosh;
        } else if (mode === 'from_v') {
          v = toMps(parseFloat(document.getElementById('valVel').value) || 0, document.getElementById('unitVel').value);
          if (v >= v_term) v = v_term * 0.9999;
          // atanh(v / vt)
          const atanhVal = 0.5 * Math.log((1 + (v / v_term)) / (1 - (v / v_term)));
          t = (v_term / g) * atanhVal;
          const arg = (g * t) / v_term;
          h = ((v_term * v_term) / g) * Math.log(Math.cosh(arg));
        }
      }

      // Kinetic energy E_k = 0.5 * m * v^2
      const Ek = 0.5 * m * v * v;

      // Render Outputs
      document.getElementById('resImpactVel').textContent = v.toFixed(2) + " m/s";
      document.getElementById('resVelSub').textContent = 
        (v * 3.6).toFixed(1) + " km/h • " + 
        (v * 2.23694).toFixed(1) + " mph • " + 
        (v * 3.28084).toFixed(1) + " ft/s";

      document.getElementById('resTime').textContent = t.toFixed(2) + " seconds";
      document.getElementById('resHeight').textContent = h.toFixed(2) + " m (" + (h * 3.28084).toFixed(1) + " ft)";

      if (Ek > 1000000) {
        document.getElementById('resEnergy').textContent = (Ek / 1000000).toFixed(3) + " MJ";
      } else if (Ek > 1000) {
        document.getElementById('resEnergy').textContent = (Ek / 1000).toFixed(2) + " kJ";
      } else {
        document.getElementById('resEnergy').textContent = Ek.toFixed(1) + " J";
      }

      if (hasDrag && isFinite(v_term)) {
        document.getElementById('resTermVel').textContent = 
          v_term.toFixed(1) + " m/s (" + (v_term * 3.6).toFixed(1) + " km/h)";
      } else {
        document.getElementById('resTermVel').textContent = "Infinite (Vacuum Mode)";
      }
    }

    document.getElementById('calcMode').addEventListener('change', updateMode);
    document.getElementById('enableDrag').addEventListener('change', (e) => {
      document.getElementById('dragOptions').style.display = e.target.checked ? 'block' : 'none';
      calculate();
    });

    document.querySelectorAll('input, select').forEach(el => {
      el.addEventListener('input', calculate);
      el.addEventListener('change', calculate);
    });

    document.getElementById('calcBtn').addEventListener('click', calculate);
    document.getElementById('resetBtn').addEventListener('click', () => {
      document.getElementById('calcMode').value = 'from_h';
      document.getElementById('gravPreset').value = '9.80665';
      document.getElementById('valHeight').value = '100';
      document.getElementById('unitHeight').value = 'm';
      document.getElementById('valMass').value = '75';
      document.getElementById('unitMass').value = 'kg';
      document.getElementById('enableDrag').checked = false;
      document.getElementById('dragOptions').style.display = 'none';
      updateMode();
    });

    window.addEventListener('DOMContentLoaded', updateMode);
  </script>
</body>
</html>
"""

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p1 = os.path.join(base_dir, "escape-velocity-calculator.html")
    p2 = os.path.join(base_dir, "free-fall-calculator.html")

    with open(p1, "w", encoding="utf-8") as f:
        f.write(TOOL_1_HTML)
    print(f"Generated {p1}")

    with open(p2, "w", encoding="utf-8") as f:
        f.write(TOOL_2_HTML)
    print(f"Generated {p2}")

if __name__ == "__main__":
    main()
