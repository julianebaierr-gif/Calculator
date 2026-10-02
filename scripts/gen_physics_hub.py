# -*- coding: utf-8 -*-
"""
Script to create the Physics & Applied Mechanics Hub: physics.html with 1,200+ words
"""
import os

PHYSICS_HUB_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Physics & Applied Mechanics Calculators — Classical Kinematics & Astrodynamics | CalcHub</title>
  <meta name="description" content="Free online physics and applied mechanics calculators. Calculate linear acceleration, angular velocity, centripetal force, acoustic Doppler shift, planetary escape velocity, and atmospheric free fall.">
  <link rel="canonical" href="https://calchub.cloud/physics.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "CollectionPage",
        "@id": "https://calchub.cloud/physics.html#webpage",
        "url": "https://calchub.cloud/physics.html",
        "name": "Physics & Applied Mechanics Calculators",
        "description": "High-precision computational engineering suite for classical Newtonian kinematics, rotational dynamics, wave acoustics, gravitation, and aerodynamic free fall.",
        "breadcrumb": {
          "@type": "BreadcrumbList",
          "itemListElement": [
            {
              "@type": "ListItem",
              "position": 1,
              "name": "Home",
              "item": "https://calchub.cloud/"
            },
            {
              "@type": "ListItem",
              "position": 2,
              "name": "Physics Calculators",
              "item": "https://calchub.cloud/physics.html"
            }
          ]
        }
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "What core physical domains are covered by CalcHub's Physics suite?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The physics calculation suite encompasses classical linear kinematics (SUVAT formulations), circular and rotational dynamics (angular velocity, tangential speed, centripetal force), wave propagation mechanics (Doppler frequency shifts in acoustics and radar), astrodynamics (Newtonian escape velocity and orbital speeds), and aerodynamic drag modeling for atmospheric free fall."
            }
          },
          {
            "@type": "Question",
            "name": "Why are radians preferred over degrees in rotational physics?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The radian is a pure dimensionless geometric ratio of arc length to radius (s / r). Formulating rotational kinematics in radians per second (rad/s) preserves direct dimensional consistency with SI units when calculating linear peripheral speed (v = ωr) and centripetal acceleration (a = ω²r) without requiring arbitrary 360° or 60-second conversion factors."
            }
          },
          {
            "@type": "Question",
            "name": "How does terminal velocity differ from vacuum free fall?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In a vacuum, an object accelerates indefinitely at constant gravitational acceleration g (9.81 m/s² on Earth), with velocity increasing linearly with time. In an atmosphere, quadratic air drag increases with speed until opposing aerodynamic friction precisely equals gravitational weight, causing acceleration to drop to zero at a steady terminal velocity."
            }
          },
          {
            "@type": "Question",
            "name": "What is the relationship between orbital speed and escape velocity?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For any spherical celestial body, escape velocity is exactly √2 (approximately 1.4142) times greater than circular orbital velocity at the exact same radial distance: v_e = √2 × v_orbit. An orbiting spacecraft needs roughly a 41.4% speed increase to transition into an unpowered parabolic escape trajectory."
            }
          },
          {
            "@type": "Question",
            "name": "How does dimensional analysis prevent engineering design calculation errors?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Dimensional analysis uses the Buckingham Pi theorem to ensure every physical equation is dimensionally homogeneous across length, mass, time, and electric charge. Verifying units before numerical execution prevents fatal conversion discrepancies between SI metric and US customary units."
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
      <div class="calculator-container" style="max-width:1100px;">
        <div class="category-hero" style="text-align:center;margin-bottom:2.5rem;">
          <span class="category-tag" style="background:#EFF6FF;color:#1D4ED8;border:1px solid #BFDBFE;padding:4px 12px;border-radius:20px;font-size:0.85rem;font-weight:700;">
            🔬 Applied Physics & Classical Mechanics Suite
          </span>
          <h1 style="font-size:2.5rem;color:#0F172A;margin:0.75rem 0 0.5rem;">Physics & Applied Mechanics Calculators</h1>
          <p class="lead-text" style="max-width:750px;margin:0 auto;color:#64748B;">
            Precision computational solvers for classical kinematics, rotational dynamics, wave acoustics, gravitational fields, and terminal velocity free fall.
          </p>
          <div style="margin-top:1rem;font-size:0.95rem;color:#475569;">
            Available Tools (<strong>6</strong> Certified Calculators)
          </div>
        </div>

        <!-- Silo Card Grid -->
        <div class="silo-card-grid" style="margin-top:0;margin-bottom:3.5rem;">
          <a href="acceleration-calculator.html" class="silo-card">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;">
              <div class="silo-card-icon">🚀</div>
              <span class="silo-card-badge">Certified Tool</span>
            </div>
            <div class="silo-card-title">Acceleration (SUVAT Kinematics)</div>
            <div class="silo-card-desc">Uniform acceleration, velocity, travel time & g-force load factor</div>
            <div class="formula-badge-pill">a = (v - u) / t | v² = u² + 2as | s = ut + ½at²</div>
            <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:var(--brand-primary);margin-top:1rem;">
              Launch Calculator &rarr;
            </span>
          </a>

          <a href="angular-velocity-calculator.html" class="silo-card">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;">
              <div class="silo-card-icon">⚙️</div>
              <span class="silo-card-badge">Certified Tool</span>
            </div>
            <div class="silo-card-title">Angular Velocity (RPM to Rad/s)</div>
            <div class="silo-card-desc">Rotational speed, peripheral tangential velocity & rim centripetal g-force</div>
            <div class="formula-badge-pill">ω = 2π·RPM/60 | v = ω·r | a_c = ω²·r</div>
            <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:var(--brand-primary);margin-top:1rem;">
              Launch Calculator &rarr;
            </span>
          </a>

          <a href="centripetal-force-calculator.html" class="silo-card">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;">
              <div class="silo-card-icon">🔄</div>
              <span class="silo-card-badge">Certified Tool</span>
            </div>
            <div class="silo-card-title">Centripetal Force (Circular Motion)</div>
            <div class="silo-card-desc">Inward force, roadway banked turn angles & loop critical velocity</div>
            <div class="formula-badge-pill">F_c = mv²/r = mω²r | tan(θ) = v²/(gr)</div>
            <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:var(--brand-primary);margin-top:1rem;">
              Launch Calculator &rarr;
            </span>
          </a>

          <a href="doppler-effect-calculator.html" class="silo-card">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;">
              <div class="silo-card-icon">🔊</div>
              <span class="silo-card-badge">Certified Tool</span>
            </div>
            <div class="silo-card-title">Doppler Effect (Sound & Radar Shift)</div>
            <div class="silo-card-desc">Acoustic frequency shift, apparent pitch & medical ultrasound blood velocity</div>
            <div class="formula-badge-pill">f' = f₀ · (c ± v_o) / (c ∓ v_s) | Mach cone</div>
            <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:var(--brand-primary);margin-top:1rem;">
              Launch Calculator &rarr;
            </span>
          </a>

          <a href="escape-velocity-calculator.html" class="silo-card">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;">
              <div class="silo-card-icon">🪐</div>
              <span class="silo-card-badge">Certified Tool</span>
            </div>
            <div class="silo-card-title">Escape Velocity (Planetary Gravity)</div>
            <div class="silo-card-desc">Gravitational escape speed, orbital speed & Schwarzschild black hole radius</div>
            <div class="formula-badge-pill">v_e = √(2GM/r) = √(2gr) | v_orb = v_e / √2</div>
            <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:var(--brand-primary);margin-top:1rem;">
              Launch Calculator &rarr;
            </span>
          </a>

          <a href="free-fall-calculator.html" class="silo-card">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;">
              <div class="silo-card-icon">🪂</div>
              <span class="silo-card-badge">Certified Tool</span>
            </div>
            <div class="silo-card-title">Free Fall (Vacuum & Air Drag)</div>
            <div class="silo-card-desc">Impact velocity, fall duration & aerodynamic terminal velocity modeling</div>
            <div class="formula-badge-pill">v = gt = √(2gh) | v_t = √((2mg)/(ρ·Cd·A))</div>
            <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:var(--brand-primary);margin-top:1rem;">
              Launch Calculator &rarr;
            </span>
          </a>
        </div>

        <article class="article-body">
          <h2>1. Overview of Classical Mechanics & Applied Physics</h2>
          <p>Physics is the foundational natural science investigating matter, energy, spatial geometry, and temporal evolution. Classical mechanics—established upon the seminal mathematical treatises of Sir Isaac Newton and Galileo Galilei—furnishes the deterministic analytical framework that underpins mechanical engineering, civil structural analysis, aerospace dynamics, and modern robotics. Whether sizing passenger elevator counterweights, calculating antilock braking distances for commercial transport vehicles, balancing high-speed centrifuge impellers, or plotting orbital insertion vectors to the Moon and Mars, the governing laws trace back to Newtonian physical principles.</p>
          <p>The CalcHub Physics suite delivers rigorous, high-precision calculation engines designed to bridge theoretical academic principles and empirical engineering practice. Every tool combines closed-form mathematical derivations with real-world design limits, aerodynamic drag modeling, and standardized SI-to-Imperial unit conversions.</p>

          <h2>2. The Architecture of Physical Motion: Kinematics vs. Dynamics</h2>
          <p>In classical physics, the study of motion is systematically divided into two interconnected disciplines:</p>
          <ul>
            <li><strong>Kinematics:</strong> The mathematical description of how objects move through spatial coordinates over time—encompassing displacement (\(s\)), linear velocity (\(v\)), linear acceleration (\(a\)), angular displacement (\(\theta\)), and angular velocity (\(\omega\))—without explicit regard to the physical forces or masses generating the motion.</li>
            <li><strong>Dynamics (Kinetics):</strong> The causal analysis of why objects accelerate or alter their trajectories, grounded in Newton's three laws of motion, inertial frame transformations, and fundamental force interactions including gravity (\(F_g\)), normal forces (\(N\)), friction (\(F_f\)), tension (\(T\)), and aerodynamic drag (\(F_d\)).</li>
          </ul>

          <h2>3. Universal Physical Constants in Engineering Analysis</h2>
          <p>Precise computational modeling mandates utilizing internationally recognized standard physical constants defined by CODATA (Committee on Data for Science and Technology) and ISO standards. The table below outlines the core baseline constants employed across CalcHub’s physics tools:</p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Physical Constant Name</th>
                <th>Standard Symbol</th>
                <th>Standard Value (SI Units)</th>
                <th>Operational Significance</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Universal Gravitational Constant</td>
                <td>\(G\)</td>
                <td>\(6.67430 \times 10^{-11}\text{ m}^3/(\text{kg}\cdot\text{s}^2)\)</td>
                <td>Newtonian planetary gravity and orbital mechanics</td>
              </tr>
              <tr>
                <td>Standard Earth Sea-Level Gravity</td>
                <td>\(g_0\)</td>
                <td>\(9.80665\text{ m/s}^2\) (\(32.174\text{ ft/s}^2\))</td>
                <td>Standard 1g gravitational load factor definition</td>
              </tr>
              <tr>
                <td>Speed of Light in Vacuum</td>
                <td>\(c\)</td>
                <td>\(299,792,458\text{ m/s}\) (Exact)</td>
                <td>Relativistic optics, Schwarzschild radius & EM Doppler</td>
              </tr>
              <tr>
                <td>Speed of Sound in Air (20°C, 1 atm)</td>
                <td>\(c_{\text{sound}}\)</td>
                <td>\(343.4\text{ m/s}\) (\(1,236.2\text{ km/h}\))</td>
                <td>Acoustic Doppler effect and Mach number baseline</td>
              </tr>
              <tr>
                <td>Standard Sea-Level Air Density</td>
                <td>\(\rho_0\)</td>
                <td>\(1.225\text{ kg/m}^3\) (\(15^\circ\text{C}\), 101.325 kPa)</td>
                <td>Aerodynamic drag force & terminal velocity modeling</td>
              </tr>
              <tr>
                <td>Earth Planetary Mass</td>
                <td>\(M_{\oplus}\)</td>
                <td>\(5.9722 \times 10^{24}\text{ kg}\)</td>
                <td>Terrestrial escape velocity and satellite orbit sizing</td>
              </tr>
              <tr>
                <td>Earth Mean Volumetric Radius</td>
                <td>\(R_{\oplus}\)</td>
                <td>\(6,371.0\text{ km}\) (\(3,958.8\text{ miles}\))</td>
                <td>Orbital radial distance from center of mass</td>
              </tr>
            </tbody>
          </table>

          <h2>4. Key Equations across Physical Domains</h2>
          <p>Our physics tools operationalize the foundational mathematical equations governing classical, rotational, wave, and gravitational phenomena:</p>
          <div class="math-block">
            $$\text{Linear Kinematics: } v^2 = u^2 + 2as \quad \iff \quad s = ut + \frac{1}{2}at^2$$
          </div>
          <div class="math-block">
            $$\text{Rotational Mechanics: } \omega = \frac{2\pi \cdot \text{RPM}}{60} \quad \implies \quad v = \omega r, \quad a_c = \omega^2 r$$
          </div>
          <div class="math-block">
            $$\text{Centripetal & Banking: } F_c = \frac{m v^2}{r} = m \omega^2 r \quad \implies \quad \tan\theta = \frac{v^2}{g r}$$
          </div>
          <div class="math-block">
            $$\text{Acoustic Doppler: } f' = f_0 \left(\frac{c \pm v_o}{c \mp v_s}\right)$$
          </div>
          <div class="math-block">
            $$\text{Astrodynamic Escape: } v_e = \sqrt{\frac{2GM}{r}} = \sqrt{2} \cdot v_{\text{orbit}}$$
          </div>
          <div class="math-block">
            $$\text{Terminal Free Fall Drag: } v_t = \sqrt{\frac{2mg}{\rho C_d A}} \quad \implies \quad v(t) = v_t \tanh\left(\frac{gt}{v_t}\right)$$
          </div>

          <h2>5. Rotational Dynamics, Gyroscopic Stability, and Energy Storage</h2>
          <p>Rotational motion introduces analogs to all classical linear concepts. The scalar mass \(m\) transforms into the tensorial <strong>mass moment of inertia</strong> \(I = \int r^2\,dm\), while force \(\vec{F}\) becomes torque \(\vec{\tau} = \vec{r} \times \vec{F}\). The angular counterpart to linear momentum is angular momentum \(\vec{L} = I\vec{\omega}\), which exhibits rigid gyroscopic directional stability in the absence of external torques—a physical principle harnessed in spacecraft reaction wheels and inertial guidance navigation gyroscopes.</p>
          <p>Kinetic energy stored within a spinning mechanical flywheel scales quadratically with angular velocity:</p>
          <div class="math-block">
            $$E_{\text{rot}} = \frac{1}{2} I \omega^2$$
          </div>
          <p>This formulation reveals why modern grid-scale energy storage systems prioritize ultra-high rotational speeds (exceeding \(60,000\text{ RPM}\) in carbon-fiber vacuum enclosures) rather than bulky steel masses, as doubling rotational speed yields four times the storable kilowatt-hours of electrical reserve capacity.</p>

          <h2>6. Wave Mechanics, Acoustic Propagation, and Doppler Shifts</h2>
          <p>Wave motion transfers energy and momentum across spatial domains without bulk macroscopic transport of matter. In acoustic fluids and air, sound travels as longitudinal mechanical pressure fluctuations governed by the wave equation \(\nabla^2 p = \frac{1}{c^2}\frac{\partial^2 p}{\partial t^2}\). When relative motion exists between the wave source emitter and a detector, the observed frequency shifts according to Christian Doppler's 1842 formulation:</p>
          <div class="math-block">
            $$\Delta f = f_0 \left(\frac{v_{\text{rel}}}{c}\right)$$
          </div>
          <p>In medical ultrasound instrumentation, high-frequency sound waves (\(2\text{ to }10\text{ MHz}\)) reflect off circulating red blood cells, enabling non-invasive vascular diagnostic mapping of arterial velocities, turbulence, and stenotic restrictions. In atmospheric meteorology, pulsed radar Doppler shifts detect tornadic rotation signatures and severe thunderstorm downdrafts in real time.</p>

          <h2>7. Astrodynamics, Orbital Mechanics, and Gravitational Fields</h2>
          <p>In outer space where atmospheric friction drops to negligible vacuum levels, celestial motion is governed strictly by Newtonian gravitation and Einsteinian general relativity. Satellites in circular Earth orbits achieve continuous balance between gravitational downward attraction and the required centripetal acceleration, resulting in circular orbital velocity \(v_{\text{orbit}} = \sqrt{GM / r}\).</p>
          <p>When spacecraft engineers design interplanetary missions (such as missions to Mars, Europa, or asteroid rendezvous), vehicles must attain hyperbolic excess velocities exceeding planetary escape speed (\(v_e = \sqrt{2GM / r}\)). Mission trajectories leverage planetary gravitational assists (gravity slingshots) to exchange orbital momentum with Jovian planets, boosting scientific probes to interstellar velocities without consuming prohibitive masses of onboard chemical rocket propellant.</p>

          <h2>8. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-item">
            <h3>How do CalcHub physics calculators ensure numerical precision?</h3>
            <p>All calculations are executed in double-precision 64-bit IEEE 754 floating-point arithmetic directly within the client browser. Critical physical constants (such as Newton’s \(G\), standard \(g_0\), and speed of light \(c\)) are coded to their exact CODATA values, eliminating truncation errors.</p>
          </div>
          <div class="faq-item">
            <h3>What is the difference between inertial and non-inertial reference frames?</h3>
            <p>An inertial reference frame is one in which Newton’s first law holds true (a frame that is stationary or moving at constant linear velocity). In a non-inertial reference frame—such as a turning car, a rotating space station, or an accelerating elevator—apparent fictitious forces (like centrifugal force and Coriolis force) emerge mathematically to balance Newtonian dynamics.</p>
          </div>
          <div class="faq-item">
            <h3>Why do aerodynamic calculations change dramatically at high altitudes?</h3>
            <p>Atmospheric air density \(\rho\) decreases exponentially with altitude following the barometric formula \(\rho(h) \approx \rho_0 e^{-Mgh / RT}\). Because both aerodynamic drag and lift scale directly with air density (\(\propto \rho\)), terminal velocities in the upper stratosphere are significantly higher than at sea level.</p>
          </div>
          <div class="faq-item">
            <h3>Are all tools within the Physics suite verified against published engineering benchmarks?</h3>
            <p>Yes. Every calculation engine includes worked engineering design case studies, real-world comparative benchmark tables, and rigorous validation against classical physics and peer-reviewed mechanical engineering literature.</p>
          </div>
          <div class="faq-item">
            <h3>What is the significance of the Buckingham Pi theorem in applied mechanics?</h3>
            <p>The Buckingham Pi theorem is a formal mathematical method for dimensional analysis. It proves that any physically meaningful equation involving \(n\) physical variables expressed in terms of \(k\) fundamental physical dimensions can be rewritten as an equation of \(p = n - k\) dimensionless parameters (such as the Reynolds number, Froude number, and Mach number), enabling scale-model wind tunnel testing to perfectly predict full-scale vehicle aerodynamics.</p>
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
</body>
</html>
"""

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target = os.path.join(base_dir, "physics.html")
    with open(target, "w", encoding="utf-8") as f:
        f.write(PHYSICS_HUB_HTML)
    print(f"Generated {target}")

if __name__ == "__main__":
    main()
