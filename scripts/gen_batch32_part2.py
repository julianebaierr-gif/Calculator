# -*- coding: utf-8 -*-
"""
Generator for Batch 32 - Part 2:
3. volume-calculator.html
4. percentage-change-calculator.html
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 3. volume-calculator.html
HTML_VOLUME = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Volume Calculator - 3D Solids, Cylinders, Spheres &amp; Prisms</title>
  <meta name="description" content="Calculate volume of cylinders, rectangular prisms, cubes, spheres, cones, pyramids, and ellipsoids with unit conversions to liters, gallons, and cubic feet.">
  <link rel="canonical" href="https://calchub.org/volume-calculator.html">
  <meta property="og:title" content="Volume Calculator - 3D Geometric Solids &amp; Capacity Solver">
  <meta property="og:description" content="Free multi-solid volume calculator. Compute enclosed cubic volume for cylinders, spheres, cones, prisms, and pyramids with instant conversions to liters and gallons.">
  <meta property="og:url" content="https://calchub.org/volume-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Volume Calculator - Accurate 3D Geometric Capacity Tool">
  <meta name="twitter:description" content="Calculate volume of cylinders, spheres, cones, cubes, and prisms with full step-by-step proofs, formulas, and real-world engineering examples.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Volume Calculator",
    "url": "https://calchub.org/volume-calculator.html",
    "description": "Calculates 3D geometric volume and volumetric capacity across cylinders, cubes, spheres, cones, pyramids, and ellipsoids with unit conversions.",
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
        "name": "What is the formula for the volume of a cylinder?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The volume of a cylinder is calculated by multiplying its circular base area by its vertical height: V = pi * r^2 * h, where r is the radius of the circular base and h is the height."
        }
      },
      {
        "@type": "Question",
        "name": "How does the volume of a cone relate to the volume of a cylinder with the same dimensions?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The volume of a cone is exactly one-third of the volume of a cylinder having the identical base radius r and height h: V_cone = (1/3) * pi * r^2 * h. This relationship derives from Cavalieri's principle and triple integration."
        }
      },
      {
        "@type": "Question",
        "name": "What is Cavalieri's Principle in volume geometry?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Cavalieri's Principle states that if two three-dimensional solids have equal altitudes and every cross-sectional slice parallel to their bases at identical heights has equal area, then the two solids possess exactly equal volumes."
        }
      },
      {
        "@type": "Question",
        "name": "How do you convert cubic meters to liters and US gallons?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "One cubic meter (1 m^3) equals exactly 1,000 liters. To convert to US liquid gallons, multiply cubic meters by 264.172 (1 m^3 = 264.172 gallons), or divide liters by 3.78541 (1 gallon = 3.78541 liters)."
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
        <a href="math.html" class="active">Math &amp; Statistics</a>
        <a href="converter.html">Converters</a>
        <a href="engineering.html">Engineering</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="calculator-container">
    <div class="calculator-header">
      <div class="calc-icon" aria-hidden="true">&#9638;</div>
      <h1>Volume Calculator</h1>
      <p class="calc-description">Compute 3D geometric volume and fluid capacity for cylinders, prisms, spheres, cones, pyramids, and ellipsoids with multi-unit conversions.</p>
    </div>

    <div class="calculator-body">
      <div class="input-group">
        <label for="solid-select">3D Solid Geometry</label>
        <select id="solid-select" class="form-control" onchange="switchSolid()">
          <option value="cylinder" selected>Cylinder (Radius &amp; Height)</option>
          <option value="rectangular-prism">Rectangular Prism / Tank (Length, Width &amp; Height)</option>
          <option value="cube">Cube (Side Length)</option>
          <option value="sphere">Sphere (Radius)</option>
          <option value="cone">Cone (Radius &amp; Height)</option>
          <option value="square-pyramid">Square Pyramid (Base Edge &amp; Height)</option>
          <option value="ellipsoid">Ellipsoid (Semi-Axes a, b, c)</option>
        </select>
      </div>

      <!-- Panel: Cylinder -->
      <div id="panel-cylinder" class="solid-panel">
        <div class="input-grid">
          <div class="input-group">
            <label for="cyl-r">Base Radius (r)</label>
            <input type="number" id="cyl-r" class="form-control" value="4" step="any" min="0">
          </div>
          <div class="input-group">
            <label for="cyl-h">Height (h)</label>
            <input type="number" id="cyl-h" class="form-control" value="10" step="any" min="0">
          </div>
        </div>
      </div>

      <!-- Panel: Rectangular Prism -->
      <div id="panel-rectangular-prism" class="solid-panel" style="display:none;">
        <div class="input-grid">
          <div class="input-group">
            <label for="prism-l">Length (l)</label>
            <input type="number" id="prism-l" class="form-control" value="8" step="any" min="0">
          </div>
          <div class="input-group">
            <label for="prism-w">Width (w)</label>
            <input type="number" id="prism-w" class="form-control" value="5" step="any" min="0">
          </div>
          <div class="input-group">
            <label for="prism-h">Height (h)</label>
            <input type="number" id="prism-h" class="form-control" value="6" step="any" min="0">
          </div>
        </div>
      </div>

      <!-- Panel: Cube -->
      <div id="panel-cube" class="solid-panel" style="display:none;">
        <div class="input-grid">
          <div class="input-group">
            <label for="cube-s">Side Length (s)</label>
            <input type="number" id="cube-s" class="form-control" value="5" step="any" min="0">
          </div>
        </div>
      </div>

      <!-- Panel: Sphere -->
      <div id="panel-sphere" class="solid-panel" style="display:none;">
        <div class="input-grid">
          <div class="input-group">
            <label for="sph-r">Radius (r)</label>
            <input type="number" id="sph-r" class="form-control" value="6" step="any" min="0">
          </div>
        </div>
      </div>

      <!-- Panel: Cone -->
      <div id="panel-cone" class="solid-panel" style="display:none;">
        <div class="input-grid">
          <div class="input-group">
            <label for="cone-r">Base Radius (r)</label>
            <input type="number" id="cone-r" class="form-control" value="3" step="any" min="0">
          </div>
          <div class="input-group">
            <label for="cone-h">Height (h)</label>
            <input type="number" id="cone-h" class="form-control" value="8" step="any" min="0">
          </div>
        </div>
      </div>

      <!-- Panel: Square Pyramid -->
      <div id="panel-square-pyramid" class="solid-panel" style="display:none;">
        <div class="input-grid">
          <div class="input-group">
            <label for="pyr-b">Base Side (b)</label>
            <input type="number" id="pyr-b" class="form-control" value="6" step="any" min="0">
          </div>
          <div class="input-group">
            <label for="pyr-h">Height (h)</label>
            <input type="number" id="pyr-h" class="form-control" value="9" step="any" min="0">
          </div>
        </div>
      </div>

      <!-- Panel: Ellipsoid -->
      <div id="panel-ellipsoid" class="solid-panel" style="display:none;">
        <div class="input-grid">
          <div class="input-group">
            <label for="el-a">Semi-Axis a</label>
            <input type="number" id="el-a" class="form-control" value="6" step="any" min="0">
          </div>
          <div class="input-group">
            <label for="el-b">Semi-Axis b</label>
            <input type="number" id="el-b" class="form-control" value="4" step="any" min="0">
          </div>
          <div class="input-group">
            <label for="el-c">Semi-Axis c</label>
            <input type="number" id="el-c" class="form-control" value="3" step="any" min="0">
          </div>
        </div>
      </div>

      <div class="input-group">
        <label for="precision-select">Decimal Precision</label>
        <select id="precision-select" class="form-control" onchange="calculateVolume()">
          <option value="2">2 decimal places</option>
          <option value="4" selected>4 decimal places</option>
          <option value="6">6 decimal places</option>
        </select>
      </div>

      <div style="display:flex; gap:12px; margin-top:16px;">
        <button id="calc-btn" class="btn-primary" onclick="calculateVolume()" style="flex:1;">Calculate Volume</button>
        <button id="reset-btn" class="btn-secondary" onclick="resetVolume()">Reset</button>
      </div>

      <div id="result-box" class="result-box" style="margin-top:24px;">
        <h2 class="result-title">Enclosed Volume &amp; Capacity Breakdown</h2>
        <div class="result-highlight" style="font-size:1.8rem; font-weight:700; color:var(--primary); margin-bottom:16px;" id="res-vol">
          Volume: 502.6548 cubic units
        </div>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:16px;">
          <div><span class="res-label">Liters (if input in meters):</span> <strong class="res-val" id="res-liters">502,654.8 L</strong></div>
          <div><span class="res-label">US Liquid Gallons:</span> <strong class="res-val" id="res-gallons">132,787.3 gal</strong></div>
          <div><span class="res-label">Cubic Feet (ft&sup3;):</span> <strong class="res-val" id="res-cuft">17,751.1 ft&sup3;</strong></div>
          <div><span class="res-label">Total Surface Area:</span> <strong class="res-val" id="res-sa">351.8584 sq units</strong></div>
          <div><span class="res-label">Solid Shape:</span> <strong class="res-val" id="res-solid-name">Cylinder</strong></div>
          <div><span class="res-label">Governing Formula:</span> <strong class="res-val" id="res-formula">V = πr²h</strong></div>
        </div>

        <h3 style="margin-top:20px; font-size:1.1rem; color:var(--text-dark);">Mathematical Step-by-Step Derivation</h3>
        <div id="res-steps" style="background:var(--bg-subtle, #f8fafc); padding:16px; border-radius:8px; font-family:monospace; font-size:0.95rem; white-space:pre-wrap; border:1px solid var(--border-color, #e2e8f0);"></div>
      </div>
    </div>

    <article class="article-body">
      <h2>Comprehensive Engineering &amp; Geometric Guide to Volume</h2>
      <p>Volume is the scalar physical quantity that quantifies the three-dimensional capacity of a closed boundary surface. In differential calculus and fluid dynamics, volume represents the triple integral of unity over an enclosed spatial domain: \(V = \iiint_D dV\). Computing geometric volume is an indispensable requirement in chemical reactor engineering, civil concrete foundation placement, geotechnical earthwork excavation, aerospace propellant tank sizing, and pharmaceutical liquid filling lines.</p>

      <p>Understanding volume calculations connects directly to surface area considerations, as explored in our <a href="surface-area-calculator.html">Surface Area Calculator</a>. While surface area dictates external heat and mass transfer, volume determines total internal storage mass, thermal heat capacity, and buoyant lift via Archimedes' Principle.</p>

      <h2>Mathematical Formulations for Standard 3D Geometric Solids</h2>
      <p>Depending on the symmetry and profile curves of the solid, classical Euclidean geometry establishes exact closed-form algebraic formulations.</p>

      <h3>1. Cylinder (Right Circular)</h3>
      <p>For a cylinder with base radius \(r\) and height \(h\), the volume is the uniform extrusion of its circular base along the altitude axis:</p>
      $$V = \pi r^2 h$$
      <p>This formulation underpins industrial piping volume, liquid storage silos, and engine piston displacement calculations.</p>

      <h3>2. Rectangular Prism &amp; Cube</h3>
      <p>For a rectangular cuboid with length \(l\), width \(w\), and height \(h\):</p>
      $$V = l \cdot w \cdot h$$
      <p>For a cube of edge length \(s\), where all orthogonal dimensions are equal: \(V = s^3\). Rectangular volumes form the foundation of building structural footing estimates, as calculated in our <a href="concrete-calculator.html">Concrete Calculator</a>.</p>

      <h3>3. Sphere</h3>
      <p>In 225 BC, Archimedes derived the volume of a sphere of radius \(r\) using exhaustion and mechanical lever balance arguments:</p>
      $$V = \frac{4}{3} \pi r^3 = \frac{1}{6} \pi d^3$$
      <p>The sphere encloses the maximum possible volume for any given surface area, minimizing thermal exchange and structural wall material costs for pressurized gas storage tanks.</p>

      <h3>4. Right Circular Cone</h3>
      <p>A right circular cone with base radius \(r\) and vertical height \(h\) has a volume equal to exactly one-third of the circumscribing cylinder:</p>
      $$V = \frac{1}{3} \pi r^2 h$$
      <p>This \(1/3\) ratio holds universally for any cone or pyramid regardless of base geometry, as proven by Eudoxus and Cavalieri's Principle.</p>

      <h3>5. Regular Square Pyramid</h3>
      <p>For a pyramid with a square base of side length \(b\) and vertical altitude \(h\):</p>
      $$V = \frac{1}{3} b^2 h$$
      <p>For a general pyramid with arbitrary base area \(B\), the volume is \(V = \frac{1}{3} B h\).</p>

      <h3>6. Ellipsoid</h3>
      <p>An ellipsoid with three principal semi-axes \(a\), \(b\), and \(c\) represents the affine scaling of a unit sphere along the three Cartesian coordinate axes:</p>
      $$V = \frac{4}{3} \pi a b c$$
      <p>When all three semi-axes are equal (\(a = b = c = r\)), the ellipsoid simplifies immediately to the classic sphere formula \(\frac{4}{3}\pi r^3\).</p>

      <h2>Cavalieri's Principle &amp; Volumetric Integration</h2>
      <p>In 1635, Italian mathematician Bonaventura Cavalieri established that if two solids have equal heights and cross-sections of equal area at every parallel height \(z\), their enclosed volumes are identically equal:</p>
      $$V = \int_{0}^{h} A(z) \, dz$$
      <p>This theorem proves why oblique (tilted) cylinders, prisms, and cones possess the exact same volumes as their right orthogonal counterparts, provided their perpendicular vertical altitudes and cross-sectional areas remain invariant.</p>

      <h2>3D Solid Volume Formulas &amp; Volumetric Invariants Table</h2>
      <p>The following technical reference matrix summarizes standard 3D solids, their governing volume equations, and unit conversion multipliers:</p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Geometric Solid</th>
            <th>Governing Volume Formula</th>
            <th>Key Dimension Parameters</th>
            <th>Base Area \(B\)</th>
            <th>Volume to Cylinder/Prism Ratio</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Cube</td>
            <td>\(V = s^3\)</td>
            <td>Edge length \(s\)</td>
            <td>\(s^2\)</td>
            <td>\(1.0000\) (Baseline)</td>
          </tr>
          <tr>
            <td>Rectangular Prism</td>
            <td>\(V = l \cdot w \cdot h\)</td>
            <td>Length \(l\), Width \(w\), Height \(h\)</td>
            <td>\(l \cdot w\)</td>
            <td>\(1.0000\) (Extrusion)</td>
          </tr>
          <tr>
            <td>Cylinder</td>
            <td>\(V = \pi r^2 h\)</td>
            <td>Radius \(r\), Height \(h\)</td>
            <td>\(\pi r^2\)</td>
            <td>\(1.0000\) (Circular Extrusion)</td>
          </tr>
          <tr>
            <td>Cone</td>
            <td>\(V = \frac{1}{3}\pi r^2 h\)</td>
            <td>Radius \(r\), Height \(h\)</td>
            <td>\(\pi r^2\)</td>
            <td>\(\frac{1}{3} \approx 0.3333\) of Cylinder</td>
          </tr>
          <tr>
            <td>Sphere</td>
            <td>\(V = \frac{4}{3}\pi r^3\)</td>
            <td>Radius \(r\)</td>
            <td>\(\pi r^2\) (Equatorial)</td>
            <td>\(\frac{2}{3} \approx 0.6667\) of Cylinder (\(h=2r\))</td>
          </tr>
          <tr>
            <td>Square Pyramid</td>
            <td>\(V = \frac{1}{3}b^2 h\)</td>
            <td>Base edge \(b\), Height \(h\)</td>
            <td>\(b^2\)</td>
            <td>\(\frac{1}{3} \approx 0.3333\) of Prism</td>
          </tr>
          <tr>
            <td>Ellipsoid</td>
            <td>\(V = \frac{4}{3}\pi a b c\)</td>
            <td>Semi-axes \(a, b, c\)</td>
            <td>\(\pi a b\) (Base ellipse)</td>
            <td>Affine sphere scaling</td>
          </tr>
        </tbody>
      </table>

      <h2>Real-World Engineering, Construction &amp; Petrochemical Case Studies</h2>
      <p>The following practical examples demonstrate how volume calculations govern physical procurement and design in civil foundations, petrochemical storage, and pharmaceutical manufacturing.</p>

      <div class="worked-example-card">
        <h3>Case Study 1: Civil Engineering Concrete Foundation Slab Placement</h3>
        <p><strong>Scenario:</strong> A structural engineer designs a reinforced concrete mat foundation for a commercial sub-station. The excavated pad measures length \(l = 24.0 \text{ m}\), width \(w = 15.0 \text{ m}\), and uniform depth \(h = 0.45 \text{ m}\). Concrete ready-mix transit trucks deliver in batches of \(8.0 \text{ m}^3\). The engineer must compute the net volume, apply a \(6\%\) placing overage allowance, and determine the required truck fleet deliveries.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Compute net rectangular prism foundation volume:
            $$V_{\text{net}} = l \times w \times h = 24.0 \times 15.0 \times 0.45 = 162.0000 \text{ m}^3$$
          </li>
          <li>Apply \(6\%\) contractor waste and pump priming overage factor:
            $$V_{\text{order}} = 162.0 \times 1.06 = 171.7200 \text{ m}^3$$
          </li>
          <li>Calculate number of ready-mix concrete delivery loads:
            $$N = \frac{171.72 \text{ m}^3}{8.0 \text{ m}^3/\text{truck}} \approx 21.465 \implies 22 \text{ truck loads}$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The foundation requires \(162.0000 \text{ m}^3\) net concrete, requiring an order of \(171.72 \text{ m}^3\) delivered across \(22\) truck loads.</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Petrochemical Cylindrical Fuel Oil Storage Tank Capacity</h3>
        <p><strong>Scenario:</strong> A bulk fuel depot constructs a vertical cylindrical diesel storage tank with internal radius \(r = 8.50 \text{ meters}\) and usable liquid height \(h = 16.0 \text{ meters}\). The terminal manager must compute the total capacity in cubic meters, liters, and US liquid barrels (\(1 \text{ bbl} = 42 \text{ gallons} \approx 0.158987 \text{ m}^3\)).</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Compute cylinder volume in cubic meters:
            $$V = \pi r^2 h = \pi \times 8.50^2 \times 16.0 = \pi \times 72.25 \times 16.0 = 1156\pi \approx 3631.6811 \text{ m}^3$$
          </li>
          <li>Convert to metric liters:
            $$V_{\text{liters}} = 3631.6811 \times 1000 = 3,631,681.1 \text{ Liters}$$
          </li>
          <li>Convert to petroleum barrels:
            $$V_{\text{bbl}} = \frac{3631.6811 \text{ m}^3}{0.158987 \text{ m}^3/\text{bbl}} \approx 22,842.6 \text{ barrels}$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The storage tank has a working volumetric capacity of \(3,631.6811 \text{ m}^3\) (\(3.63\) million liters, or \(22,842.6\) barrels of diesel).</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 3: Pharmaceutical Gel Capsule Ellipsoid Dosage Sizing</h3>
        <p><strong>Scenario:</strong> A pharmaceutical formulations lab develops a gelatin softgel capsule shaped as a prolate ellipsoid. The semi-major axis along the length is \(a = 9.0 \text{ mm}\), and the two transverse equatorial semi-axes are \(b = c = 4.5 \text{ mm}\). The active pharmaceutical oil solution has a density of \(0.92 \text{ mg/mm}^3\). The formulation scientist must calculate the capsule fill volume and active drug payload mass.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Apply ellipsoid volume formula:
            $$V = \frac{4}{3} \pi a b c = \frac{4}{3} \times \pi \times 9.0 \times 4.5 \times 4.5$$
            $$V = \frac{4}{3} \times \pi \times 182.25 = 243\pi \approx 763.4070 \text{ mm}^3 \text{ (or } 0.7634 \text{ mL)}$$
          </li>
          <li>Calculate fluid payload mass:
            $$m = V \times \rho = 763.4070 \text{ mm}^3 \times 0.92 \text{ mg/mm}^3 \approx 702.3344 \text{ mg}$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> Each gelatin softgel capsule encloses \(763.4070 \text{ mm}^3\) (\(0.7634 \text{ mL}\)) containing \(702.33 \text{ mg}\) of therapeutic formulation.</p>
      </div>

      <h2>Frequently Asked Questions</h2>
      <div class="faq-item">
        <div class="faq-question">What is the difference between volume and capacity?</div>
        <div class="faq-answer">While often used interchangeably, volume refers to the total three-dimensional space occupied by an object's external boundary or enclosed by its interior walls (expressed in cubic meters, cubic feet, etc.). Capacity specifically denotes the volume of fluid or substance a container can hold (typically measured in liters, gallons, or barrels).</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Why does the cone formula have a 1/3 factor?</div>
        <div class="faq-answer">The 1/3 factor arises because the cross-sectional area of a cone shrinks quadratically with height: \(A(z) = \pi r^2 (1 - z/h)^2\). Integrating this quadratic function from base to apex (\(\int_0^h (1 - z/h)^2 dz\)) yields exactly \(h/3\), resulting in \(V = \frac{1}{3}\pi r^2 h\).</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">How does scaling linear dimensions affect volume?</div>
        <div class="faq-answer">According to the square-cube law, scaling all linear dimensions by a factor \(k\) multiplies the enclosed volume by \(k^3\). For example, doubling the radius and height of a cylinder (\(k = 2\)) increases its volume by \(2^3 = 8\) times. Tripling dimensions (\(k = 3\)) increases volume by \(3^3 = 27\) times.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">How do you calculate the volume of an irregularly shaped rock or metal casting?</div>
        <div class="faq-answer">For irregular shapes lacking geometric symmetry, Archimedes' water displacement method is used: submerging the solid in a graduated fluid container causes the fluid level to rise by a volume exactly equal to the object's submerged volume. Alternatively, dividing the solid into a 3D CAD mesh (tetrahedral finite element discretization) sums the individual polyhedral volumes.</div>
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
    function switchSolid() {
      var solid = document.getElementById('solid-select').value;
      var panels = document.querySelectorAll('.solid-panel');
      panels.forEach(function(p) { p.style.display = 'none'; });

      var active = document.getElementById('panel-' + solid);
      if (active) active.style.display = 'block';
      calculateVolume();
    }

    function calculateVolume() {
      var solid = document.getElementById('solid-select').value;
      var prec = parseInt(document.getElementById('precision-select').value, 10) || 4;

      var vol = 0, sa = 0;
      var solidName = "";
      var formulaStr = "";
      var steps = "";

      if (solid === 'cylinder') {
        var r = parseFloat(document.getElementById('cyl-r').value);
        var h = parseFloat(document.getElementById('cyl-h').value);
        if (isNaN(r) || isNaN(h) || r <= 0 || h <= 0) {
          showError("Radius and height must be positive real numbers.");
          return;
        }
        vol = Math.PI * r * r * h;
        sa = 2 * Math.PI * r * (r + h);
        solidName = "Cylinder";
        formulaStr = "V = πr²h";
        steps = "Solid: Right Circular Cylinder\n" +
                "Radius r = " + r + ", Height h = " + h + "\n\n" +
                "1. Base Area: B = π * r² = π * (" + (r * r) + ") = " + (Math.PI * r * r).toFixed(prec) + "\n\n" +
                "2. Volume: V = B * h = π * r² * h\n" +
                "   V = " + (Math.PI * r * r).toFixed(prec) + " * " + h + " = " + vol.toFixed(prec) + " cubic units";

      } else if (solid === 'rectangular-prism') {
        var l = parseFloat(document.getElementById('prism-l').value);
        var w = parseFloat(document.getElementById('prism-w').value);
        var hp = parseFloat(document.getElementById('prism-h').value);
        if ([l, w, hp].some(function(v) { return isNaN(v) || v <= 0; })) {
          showError("Dimensions must be positive real numbers.");
          return;
        }
        vol = l * w * hp;
        sa = 2 * (l * w + l * hp + w * hp);
        solidName = "Rectangular Prism";
        formulaStr = "V = l * w * h";
        steps = "Solid: Rectangular Prism\n" +
                "Length l = " + l + ", Width w = " + w + ", Height h = " + hp + "\n\n" +
                "1. Volume: V = l * w * h\n" +
                "   V = " + l + " * " + w + " * " + hp + " = " + vol.toFixed(prec) + " cubic units";

      } else if (solid === 'cube') {
        var s = parseFloat(document.getElementById('cube-s').value);
        if (isNaN(s) || s <= 0) {
          showError("Cube side length must be a positive real number.");
          return;
        }
        vol = s * s * s;
        sa = 6 * s * s;
        solidName = "Cube";
        formulaStr = "V = s³";
        steps = "Solid: Cube\n" +
                "Edge length s = " + s + "\n\n" +
                "1. Volume: V = s³ = " + s + "³ = " + vol.toFixed(prec) + " cubic units";

      } else if (solid === 'sphere') {
        var rs = parseFloat(document.getElementById('sph-r').value);
        if (isNaN(rs) || rs <= 0) {
          showError("Sphere radius must be a positive real number.");
          return;
        }
        vol = (4 / 3) * Math.PI * rs * rs * rs;
        sa = 4 * Math.PI * rs * rs;
        solidName = "Sphere";
        formulaStr = "V = (4/3)πr³";
        steps = "Solid: Sphere\n" +
                "Radius r = " + rs + "\n\n" +
                "1. Volume: V = (4/3) * π * r³ = (4/3) * π * (" + (rs * rs * rs) + ")\n" +
                "   V = " + vol.toFixed(prec) + " cubic units";

      } else if (solid === 'cone') {
        var rc = parseFloat(document.getElementById('cone-r').value);
        var hc = parseFloat(document.getElementById('cone-h').value);
        if (isNaN(rc) || isNaN(hc) || rc <= 0 || hc <= 0) {
          showError("Cone radius and height must be positive real numbers.");
          return;
        }
        vol = (1 / 3) * Math.PI * rc * rc * hc;
        var slant = Math.sqrt(rc * rc + hc * hc);
        sa = Math.PI * rc * (rc + slant);
        solidName = "Cone";
        formulaStr = "V = (1/3)πr²h";
        steps = "Solid: Right Circular Cone\n" +
                "Radius r = " + rc + ", Height h = " + hc + "\n\n" +
                "1. Volume: V = (1/3) * π * r² * h = (1/3) * π * (" + (rc * rc) + ") * " + hc + "\n" +
                "   V = " + vol.toFixed(prec) + " cubic units";

      } else if (solid === 'square-pyramid') {
        var b = parseFloat(document.getElementById('pyr-b').value);
        var hpyr = parseFloat(document.getElementById('pyr-h').value);
        if (isNaN(b) || isNaN(hpyr) || b <= 0 || hpyr <= 0) {
          showError("Pyramid dimensions must be positive real numbers.");
          return;
        }
        vol = (1 / 3) * b * b * hpyr;
        var sPyr = Math.sqrt(hpyr * hpyr + (b / 2) * (b / 2));
        sa = b * b + 2 * b * sPyr;
        solidName = "Square Pyramid";
        formulaStr = "V = (1/3)b²h";
        steps = "Solid: Square Pyramid\n" +
                "Base Edge b = " + b + ", Height h = " + hpyr + "\n\n" +
                "1. Base Area: B = b² = " + (b * b) + "\n\n" +
                "2. Volume: V = (1/3) * b² * h = (1/3) * " + (b * b) + " * " + hpyr + " = " + vol.toFixed(prec) + " cubic units";

      } else if (solid === 'ellipsoid') {
        var ea = parseFloat(document.getElementById('el-a').value);
        var eb = parseFloat(document.getElementById('el-b').value);
        var ec = parseFloat(document.getElementById('el-c').value);
        if ([ea, eb, ec].some(function(v) { return isNaN(v) || v <= 0; })) {
          showError("All three semi-axes must be positive real numbers.");
          return;
        }
        vol = (4 / 3) * Math.PI * ea * eb * ec;
        var pEll = 1.6075;
        sa = 4 * Math.PI * Math.pow((Math.pow(ea * eb, pEll) + Math.pow(ea * ec, pEll) + Math.pow(eb * ec, pEll)) / 3, 1 / pEll);
        solidName = "Ellipsoid";
        formulaStr = "V = (4/3)πabc";
        steps = "Solid: Ellipsoid\n" +
                "Semi-axes: a = " + ea + ", b = " + eb + ", c = " + ec + "\n\n" +
                "1. Volume: V = (4/3) * π * a * b * c\n" +
                "   V = (4/3) * π * " + (ea * eb * ec) + " = " + vol.toFixed(prec) + " cubic units";
      }

      // Unit conversions assuming cubic meters
      var liters = vol * 1000.0;
      var gallons = vol * 264.172;
      var cuft = vol * 35.3147;

      document.getElementById('res-vol').innerText = "Volume: " + vol.toFixed(prec) + " cubic units";
      document.getElementById('res-liters').innerText = liters.toLocaleString(undefined, {maximumFractionDigits: 1}) + " L";
      document.getElementById('res-gallons').innerText = gallons.toLocaleString(undefined, {maximumFractionDigits: 1}) + " gal";
      document.getElementById('res-cuft').innerText = cuft.toLocaleString(undefined, {maximumFractionDigits: 1}) + " ft³";
      document.getElementById('res-sa').innerText = sa.toFixed(prec) + " sq units";
      document.getElementById('res-solid-name').innerText = solidName;
      document.getElementById('res-formula').innerText = formulaStr;
      document.getElementById('res-steps').innerText = steps;
    }

    function showError(msg) {
      document.getElementById('res-vol').innerText = "Error";
      document.getElementById('res-liters').innerText = "N/A";
      document.getElementById('res-gallons').innerText = "N/A";
      document.getElementById('res-cuft').innerText = "N/A";
      document.getElementById('res-sa').innerText = "N/A";
      document.getElementById('res-solid-name').innerText = "Invalid Input";
      document.getElementById('res-formula').innerText = "N/A";
      document.getElementById('res-steps').innerText = "Error: " + msg;
    }

    function resetVolume() {
      document.getElementById('solid-select').value = 'cylinder';
      document.getElementById('cyl-r').value = '4';
      document.getElementById('cyl-h').value = '10';
      document.getElementById('prism-l').value = '8';
      document.getElementById('prism-w').value = '5';
      document.getElementById('prism-h').value = '6';
      document.getElementById('cube-s').value = '5';
      document.getElementById('sph-r').value = '6';
      document.getElementById('cone-r').value = '3';
      document.getElementById('cone-h').value = '8';
      document.getElementById('pyr-b').value = '6';
      document.getElementById('pyr-h').value = '9';
      document.getElementById('el-a').value = '6';
      document.getElementById('el-b').value = '4';
      document.getElementById('el-c').value = '3';
      document.getElementById('precision-select').value = '4';
      switchSolid();
    }

    window.addEventListener('DOMContentLoaded', function() {
      calculateVolume();
    });
  </script>
</body>
</html>
"""

# 4. percentage-change-calculator.html
HTML_PERCENT_CHANGE = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Percentage Change Calculator - Increase, Decrease &amp; Growth Rates</title>
  <meta name="description" content="Calculate percentage increase, percentage decrease, relative difference, and growth rate between two values with step-by-step math and formulas.">
  <link rel="canonical" href="https://calchub.org/percentage-change-calculator.html">
  <meta property="og:title" content="Percentage Change Calculator - Increase &amp; Decrease Solver">
  <meta property="og:description" content="Free percentage change calculator. Compute percent increase, percent decrease, absolute difference, and growth factor multipliers with step-by-step proofs.">
  <meta property="og:url" content="https://calchub.org/percentage-change-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Percentage Change Calculator - Percent Growth Solver">
  <meta name="twitter:description" content="Calculate percentage change, relative difference, and new values from percentage adjustments. Full step-by-step mathematical breakdowns.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Percentage Change Calculator",
    "url": "https://calchub.org/percentage-change-calculator.html",
    "description": "Calculates percentage increase, percentage decrease, relative change, absolute difference, and growth multiplier between initial and final values.",
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
        "name": "What is the formula for percentage change?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The formula for percentage change is: Percentage Change = [(Final Value - Initial Value) / |Initial Value|] * 100%. If the result is positive, it represents a percentage increase; if negative, it represents a percentage decrease."
        }
      },
      {
        "@type": "Question",
        "name": "Why is a 50% drop not restored by a 50% increase?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "This asymmetry occurs because the baseline denominator changes. If a $100 stock drops 50%, it falls to $50. A subsequent 50% increase from $50 only adds $25, reaching $75. To return from $50 back to $100 requires a 100% increase (doubling)."
        }
      },
      {
        "@type": "Question",
        "name": "What is the difference between percentage change and percentage points?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Percentage change measures relative growth compared to the initial level. Percentage points measure the arithmetic difference between two percentages. For instance, if an interest rate moves from 4% to 5%, it increased by 1 percentage point, but represents a 25% relative percentage change."
        }
      },
      {
        "@type": "Question",
        "name": "What is the percentage difference between two non-directional numbers?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "When neither number is designated as the initial reference point, percentage difference divides the absolute difference by the average of the two numbers: Percent Difference = [|A - B| / ((A + B) / 2)] * 100%."
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
        <a href="math.html" class="active">Math &amp; Statistics</a>
        <a href="converter.html">Converters</a>
        <a href="engineering.html">Engineering</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="calculator-container">
    <div class="calculator-header">
      <div class="calc-icon" aria-hidden="true">&#916;%</div>
      <h1>Percentage Change Calculator</h1>
      <p class="calc-description">Calculate percent increase, percent decrease, relative difference, absolute change, and growth multiplier between initial and final values.</p>
    </div>

    <div class="calculator-body">
      <div class="input-group">
        <label for="change-mode">Calculation Mode</label>
        <select id="change-mode" class="form-control" onchange="switchChangeMode()">
          <option value="change" selected>Percentage Change: (Initial Value V₁ &rarr; Final Value V₂)</option>
          <option value="difference">Percentage Difference: (Compare Two Numbers A and B)</option>
          <option value="apply">Apply Percentage: (Initial Value &plusmn; X% &rarr; Final Value)</option>
        </select>
      </div>

      <!-- Mode 1: Change -->
      <div id="panel-change">
        <div class="input-grid">
          <div class="input-group">
            <label for="val-v1">Initial Value (V₁)</label>
            <input type="number" id="val-v1" class="form-control" value="80" step="any">
            <span class="help-text">Starting reference benchmark</span>
          </div>
          <div class="input-group">
            <label for="val-v2">Final Value (V₂)</label>
            <input type="number" id="val-v2" class="form-control" value="120" step="any">
            <span class="help-text">New resulting value</span>
          </div>
        </div>
      </div>

      <!-- Mode 2: Difference -->
      <div id="panel-difference" style="display:none;">
        <div class="input-grid">
          <div class="input-group">
            <label for="diff-a">Value A</label>
            <input type="number" id="diff-a" class="form-control" value="25" step="any">
          </div>
          <div class="input-group">
            <label for="diff-b">Value B</label>
            <input type="number" id="diff-b" class="form-control" value="35" step="any">
          </div>
        </div>
      </div>

      <!-- Mode 3: Apply -->
      <div id="panel-apply" style="display:none;">
        <div class="input-grid">
          <div class="input-group">
            <label for="apply-base">Base Initial Value</label>
            <input type="number" id="apply-base" class="form-control" value="150" step="any">
          </div>
          <div class="input-group">
            <label for="apply-pct">Percentage (% Change)</label>
            <input type="number" id="apply-pct" class="form-control" value="25" step="any">
            <span class="help-text">Positive for increase (+), negative for decrease (-)</span>
          </div>
        </div>
      </div>

      <div class="input-group">
        <label for="precision-select">Decimal Precision</label>
        <select id="precision-select" class="form-control" onchange="calculatePercentChange()">
          <option value="2">2 decimal places</option>
          <option value="4" selected>4 decimal places</option>
          <option value="6">6 decimal places</option>
        </select>
      </div>

      <div style="display:flex; gap:12px; margin-top:16px;">
        <button id="calc-btn" class="btn-primary" onclick="calculatePercentChange()" style="flex:1;">Compute Percentage</button>
        <button id="reset-btn" class="btn-secondary" onclick="resetPercentChange()">Reset</button>
      </div>

      <div id="result-box" class="result-box" style="margin-top:24px;">
        <h2 class="result-title">Relative Change &amp; Growth Analysis</h2>
        <div class="result-highlight" style="font-size:1.8rem; font-weight:700; color:var(--primary); margin-bottom:16px;" id="res-main">
          +50.0000% Increase
        </div>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:16px;">
          <div><span class="res-label">Absolute Difference (&Delta;):</span> <strong class="res-val" id="res-abs">+40.0000</strong></div>
          <div><span class="res-label">Growth Multiplier:</span> <strong class="res-val" id="res-mult">1.5000&times;</strong></div>
          <div><span class="res-label">Reverse Needed to Reset:</span> <strong class="res-val" id="res-rev">-33.3333%</strong></div>
          <div><span class="res-label">Directional Status:</span> <strong class="res-val" id="res-status">Net Expansion</strong></div>
        </div>

        <h3 style="margin-top:20px; font-size:1.1rem; color:var(--text-dark);">Mathematical Step-by-Step Breakdown</h3>
        <div id="res-steps" style="background:var(--bg-subtle, #f8fafc); padding:16px; border-radius:8px; font-family:monospace; font-size:0.95rem; white-space:pre-wrap; border:1px solid var(--border-color, #e2e8f0);"></div>
      </div>
    </div>

    <article class="article-body">
      <h2>Comprehensive Engineering &amp; Financial Guide to Percentage Change</h2>
      <p>Percentage change is the standard mathematical operator that normalizes the difference between an initial benchmark value \(V_1\) and a subsequent final value \(V_2\) into a relative dimensionless percentage. Unlike absolute differences (such as an increase of \(50 \text{ dollars}\) or \(12 \text{ kilograms}\)), percentage change expresses growth or contraction relative to the initial starting scale, enabling standardized comparisons across companies, engineering systems, and historical eras.</p>

      <p>Percentage change calculations govern critical performance indicators across financial markets (portfolio returns, quarterly revenue shifts), epidemiology (viral transmission growth rates), manufacturing (tolerance dimensional shifts), and macroeconomic analysis (inflation indices, gross domestic product growth). Related fractional and percentage foundations are detailed in our <a href="percentage-calculator.html">Percentage Calculator</a> and <a href="percent-error-calculator.html">Percent Error Calculator</a>.</p>

      <h2>Mathematical Formulations for Relative &amp; Percentage Change</h2>
      <p>Depending on whether a temporal sequence exists and whether directional polarity is defined, different formulas apply.</p>

      <h3>1. Standard Directional Percentage Change Formulation</h3>
      <p>When an initial observation \(V_1\) transitions to a final observation \(V_2\), the percentage change \(\Delta\%\) is given by:</p>
      $$\Delta\% = \frac{V_2 - V_1}{|V_1|} \times 100\%$$
      <p>Where:</p>
      <ul>
        <li>\(V_1\) is the initial baseline value (\(V_1 \neq 0\)). The absolute value in the denominator \(|V_1|\) ensures that transitions from negative baselines preserve correct growth polarity.</li>
        <li>\(V_2\) is the final resulting value.</li>
        <li>\(V_2 - V_1\) represents the signed absolute change (\(\Delta V\)).</li>
      </ul>
      <p>If \(\Delta\% > 0\), the transition represents a <strong>percentage increase</strong>. If \(\Delta\% < 0\), it represents a <strong>percentage decrease</strong>.</p>

      <h3>2. Non-Directional Percentage Difference</h3>
      <p>When comparing two independent physical measurements \(A\) and \(B\) where neither value serves as an initial chronological starting point (such as comparing two laboratory instruments or two competing products), dividing by either \(A\) or \(B\) arbitrarily biases the result. The standard solution divides the absolute difference by their arithmetic average:</p>
      $$\text{Percent Difference} = \frac{|A - B|}{\frac{A + B}{2}} \times 100\% = \frac{2 \cdot |A - B|}{A + B} \times 100\%$$

      <h3>3. The Fundamental Asymmetry of Percentage Changes</h3>
      <p>A classic cognitive pitfall in investment and risk management is the mathematical asymmetry between percentage gains and percentage losses. Because losses reduce the capital base while gains build upon an already depressed base, a percentage loss requires a strictly larger percentage gain to restore the original value:</p>
      $$\text{Required Gain to Break Even} = \left( \frac{1}{1 - L} - 1 \right) \times 100\%$$
      <p>Where \(L\) is the fractional loss (\(0 < L < 1\)):</p>
      <ul>
        <li>A \(10\%\) loss requires an \(11.11\%\) gain to break even.</li>
        <li>A \(25\%\) loss requires a \(33.33\%\) gain to break even.</li>
        <li>A \(50\%\) loss requires a \(100.00\%\) gain (doubling) to break even.</li>
        <li>A \(90\%\) loss requires a \(900.00\%\) gain (\(10\times\)) to break even.</li>
      </ul>

      <h3>4. Percentage Change vs. Percentage Points</h3>
      <p>Confusion between percentage change and percentage points is frequent in public discourse:</p>
      <ul>
        <li><strong>Percentage Points:</strong> The simple arithmetic difference between two percentage values: \(\Delta_{\text{pp}} = P_2 - P_1\).</li>
        <li><strong>Percentage Change:</strong> The relative percentage increase of the initial percentage: \(\Delta\% = \frac{P_2 - P_1}{P_1} \times 100\%\).</li>
      </ul>
      <p>For example, if a central bank increases interest rates from \(4.0\%\) to \(5.0\%\), the rate increased by \(1.0 \text{ percentage point}\), but the cost of borrowing rose by a relative \(\frac{5.0 - 4.0}{4.0} \times 100\% = 25.0\%\).</p>

      <h2>Loss vs. Required Break-Even Recovery Matrix</h2>
      <p>The following benchmark reference table illustrates the mathematical asymmetry between drawdowns and required recovery gains:</p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Drawdown / Loss Percentage</th>
            <th>Residual Capital Factor</th>
            <th>Required Gain to Break Even</th>
            <th>Capital Multiplier Needed</th>
            <th>Risk Implication</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>\(-5.0\%\)</td>
            <td>\(0.9500\)</td>
            <td>\(+5.26\%\)</td>
            <td>\(1.0526\times\)</td>
            <td>Minimal portfolio impact</td>
          </tr>
          <tr>
            <td>\(-10.0\%\)</td>
            <td>\(0.9000\)</td>
            <td>\(+11.11\%\)</td>
            <td>\(1.1111\times\)</td>
            <td>Typical market correction</td>
          </tr>
          <tr>
            <td>\(-20.0\%\)</td>
            <td>\(0.8000\)</td>
            <td>\(+25.00\%\)</td>
            <td>\(1.2500\times\)</td>
            <td>Bear market threshold</td>
          </tr>
          <tr>
            <td>\(-33.33\%\)</td>
            <td>\(0.6667\)</td>
            <td>\(+50.00\%\)</td>
            <td>\(1.5000\times\)</td>
            <td>Severe recession drawdown</td>
          </tr>
          <tr>
            <td>\(-50.0\%\)</td>
            <td>\(0.5000\)</td>
            <td>\(+100.00\%\)</td>
            <td>\(2.0000\times\)</td>
            <td>Requires doubling portfolio</td>
          </tr>
          <tr>
            <td>\(-75.0\%\)</td>
            <td>\(0.2500\)</td>
            <td>\(+300.00\%\)</td>
            <td>\(4.0000\times\)</td>
            <td>Catastrophic asset impairment</td>
          </tr>
          <tr>
            <td>\(-90.0\%\)</td>
            <td>\(0.1000\)</td>
            <td>\(+900.00\%\)</td>
            <td>\(10.0000\times\)</td>
            <td>Total restructuring required</td>
          </tr>
        </tbody>
      </table>

      <h2>Real-World Financial, Industrial &amp; Clinical Case Studies</h2>
      <p>The following worked case studies demonstrate how percentage change formulations govern performance evaluations in corporate finance, manufacturing yield, and clinical diagnostics.</p>

      <div class="worked-example-card">
        <h3>Case Study 1: Corporate Revenue Year-over-Year (YoY) Growth Analysis</h3>
        <p><strong>Scenario:</strong> A SaaS technology company reports fourth-quarter subscription revenue of \(V_1 = \$4.25 \text{ million}\) in fiscal year 2024. In the fourth quarter of fiscal year 2025, revenue reaches \(V_2 = \$6.80 \text{ million}\). The Chief Financial Officer (CFO) must compute the annual Year-over-Year percentage change and the revenue growth multiplier.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Identify initial and final values: \(V_1 = \$4.25\text{M}, \; V_2 = \$6.80\text{M}\).</li>
          <li>Calculate absolute dollar expansion:
            $$\Delta V = V_2 - V_1 = 6.80 - 4.25 = +\$2.55 \text{ million}$$
          </li>
          <li>Apply directional percentage change formula:
            $$\Delta\% = \frac{V_2 - V_1}{V_1} \times 100\% = \frac{2.55}{4.25} \times 100\% = 0.6000 \times 100\% = +60.0000\%$$
          </li>
          <li>Compute revenue growth multiplier:
            $$M = \frac{V_2}{V_1} = \frac{6.80}{4.25} = 1.6000\times$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The company achieved a \(+60.0000\%\) YoY revenue expansion, representing a \(1.60\times\) growth factor.</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Industrial Scrap Reduction Quality Improvement</h3>
        <p><strong>Scenario:</strong> An automotive stamping plant implements Six Sigma lean initiatives to reduce scrap metal generation. Before process optimization, the stamping line generated \(V_1 = 18.4 \text{ metric tons}\) of scrap per month. Six months after installing automated vision sorting, monthly scrap fell to \(V_2 = 11.5 \text{ metric tons}\). The plant quality manager must report the net percentage scrap reduction.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Identify values: \(V_1 = 18.4 \text{ tons}, \; V_2 = 11.5 \text{ tons}\).</li>
          <li>Calculate signed absolute change:
            $$\Delta V = V_2 - V_1 = 11.5 - 18.4 = -6.9 \text{ metric tons}$$
          </li>
          <li>Calculate percentage change:
            $$\Delta\% = \frac{-6.9}{18.4} \times 100\% \approx -0.3750 \times 100\% = -37.5000\%$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The manufacturing facility achieved a \(37.5000\%\) reduction in scrap generation.</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 3: Clinical Blood Analyte Cholesterol Reduction (Statin Therapy)</h3>
        <p><strong>Scenario:</strong> A cardiology patient with hyperlipidemia has an initial baseline serum LDL cholesterol level of \(V_1 = 192.0 \text{ mg/dL}\). After 12 weeks of high-intensity statin therapy, follow-up lipid panels show an LDL concentration of \(V_2 = 86.4 \text{ mg/dL}\). The clinical cardiologist must evaluate whether the treatment satisfied the AHA/ACC guideline target of at least a \(50\%\) LDL reduction.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Compute absolute LDL decline:
            $$\Delta = 86.4 - 192.0 = -105.6 \text{ mg/dL}$$
          </li>
          <li>Apply percentage change formula:
            $$\Delta\% = \frac{-105.6}{192.0} \times 100\% = -0.5500 \times 100\% = -55.0000\%$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The patient achieved a \(55.0000\%\) relative reduction in serum LDL cholesterol, successfully exceeding the \(50\%\) clinical therapeutic threshold.</p>
      </div>

      <h2>Frequently Asked Questions</h2>
      <div class="faq-item">
        <div class="faq-question">Can percentage change exceed 100%?</div>
        <div class="faq-answer">Yes, for percentage increases. If a value doubles (e.g., from 10 to 20), the percentage increase is exactly \(100\%\). If it triples (e.g., from 10 to 30), the increase is \(200\%\). However, for positive physical quantities, a percentage decrease cannot exceed \(100\%\), because a \(100\%\) decrease reduces the value completely to zero.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">What happens if the initial value is zero (V1 = 0)?</div>
        <div class="faq-answer">If the initial value is zero, percentage change is mathematically undefined because division by zero is impossible. Going from 0 to any positive number represents an infinite relative increase. In practical business reporting, analysts state "not meaningful" (N/M) or report the absolute difference instead.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">How does percentage change work with negative numbers?</div>
        <div class="faq-answer">By using the absolute value of the initial value in the denominator (\(|V_1|\)), correct directional polarity is preserved. For example, moving from a profit of -\$50 (a \$50 loss) to +\$50 profit yields \([50 - (-50)] / |-50| = 100 / 50 = +200\%\), accurately showing a positive financial improvement.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">How do you calculate compound percentage change across multiple periods?</div>
        <div class="faq-answer">You cannot simply add percentage changes together. Instead, convert each percentage change into a growth multiplier (\(1 + r_i\)), multiply the factors together, and subtract 1: \(\Delta_{\text{total}} = [(1 + r_1)(1 + r_2)\dots(1 + r_n) - 1] \times 100\%\). For equal periods, the Compound Annual Growth Rate (CAGR) computes the geometric mean rate.</div>
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
    function switchChangeMode() {
      var mode = document.getElementById('change-mode').value;
      document.getElementById('panel-change').style.display = (mode === 'change') ? 'block' : 'none';
      document.getElementById('panel-difference').style.display = (mode === 'difference') ? 'block' : 'none';
      document.getElementById('panel-apply').style.display = (mode === 'apply') ? 'block' : 'none';
      calculatePercentChange();
    }

    function calculatePercentChange() {
      var mode = document.getElementById('change-mode').value;
      var prec = parseInt(document.getElementById('precision-select').value, 10) || 4;

      if (mode === 'change') {
        var v1 = parseFloat(document.getElementById('val-v1').value);
        var v2 = parseFloat(document.getElementById('val-v2').value);

        if (isNaN(v1) || isNaN(v2)) {
          showError("Initial and final values must be valid real numbers.");
          return;
        }

        if (v1 === 0) {
          showError("Initial value cannot be zero (division by zero is undefined).");
          return;
        }

        var diff = v2 - v1;
        var pctChange = (diff / Math.abs(v1)) * 100;
        var mult = v2 / v1;

        // Reset needed to reverse back to v1
        var revPct = (v2 !== 0) ? ((v1 - v2) / Math.abs(v2) * 100) : 0;

        var typeStr = (pctChange >= 0) ? "Increase" : "Decrease";
        var signStr = (pctChange >= 0) ? "+" : "";
        var statusStr = (pctChange >= 0) ? "Net Expansion" : "Net Contraction";

        document.getElementById('res-main').innerText = signStr + pctChange.toFixed(prec) + "% " + typeStr;
        document.getElementById('res-abs').innerText = (diff >= 0 ? "+" : "") + diff.toFixed(prec);
        document.getElementById('res-mult').innerText = mult.toFixed(prec) + "×";
        document.getElementById('res-rev').innerText = (revPct >= 0 ? "+" : "") + revPct.toFixed(prec) + "%";
        document.getElementById('res-status').innerText = statusStr;

        var steps = "Mode: Directional Percentage Change\n" +
                    "Initial Value V₁ = " + v1 + ", Final Value V₂ = " + v2 + "\n\n" +
                    "1. Absolute Difference: ΔV = V₂ - V₁\n" +
                    "   ΔV = " + v2 + " - " + v1 + " = " + diff.toFixed(prec) + "\n\n" +
                    "2. Percentage Change Formula: Δ% = (ΔV / |V₁|) * 100%\n" +
                    "   Δ% = (" + diff.toFixed(prec) + " / " + Math.abs(v1) + ") * 100% = " + pctChange.toFixed(prec) + "%\n\n" +
                    "3. Growth Multiplier: V₂ / V₁ = " + v2 + " / " + v1 + " = " + mult.toFixed(prec) + "×\n\n" +
                    "4. Break-Even Reversal: To return from " + v2 + " back to " + v1 + " requires " + revPct.toFixed(prec) + "% change.";

        document.getElementById('res-steps').innerText = steps;

      } else if (mode === 'difference') {
        var a = parseFloat(document.getElementById('diff-a').value);
        var b = parseFloat(document.getElementById('diff-b').value);

        if (isNaN(a) || isNaN(b)) {
          showError("Both values must be valid real numbers.");
          return;
        }

        var avg = (a + b) / 2;
        if (avg === 0) {
          showError("Average of the two values cannot be zero.");
          return;
        }

        var absDiff = Math.abs(a - b);
        var pctDiff = (absDiff / Math.abs(avg)) * 100;

        document.getElementById('res-main').innerText = pctDiff.toFixed(prec) + "% Difference";
        document.getElementById('res-abs').innerText = absDiff.toFixed(prec);
        document.getElementById('res-mult').innerText = (a !== 0 ? (b / a).toFixed(prec) + "×" : "N/A");
        document.getElementById('res-rev').innerText = "Average: " + avg.toFixed(prec);
        document.getElementById('res-status').innerText = "Non-Directional Comparison";

        var steps = "Mode: Non-Directional Percentage Difference\n" +
                    "Value A = " + a + ", Value B = " + b + "\n\n" +
                    "1. Absolute Discrepancy: |A - B| = |" + a + " - " + b + "| = " + absDiff.toFixed(prec) + "\n\n" +
                    "2. Average of Values: (A + B) / 2 = (" + a + " + " + b + ") / 2 = " + avg.toFixed(prec) + "\n\n" +
                    "3. Percentage Difference: [|A - B| / |Average|] * 100%\n" +
                    "   Diff% = (" + absDiff.toFixed(prec) + " / " + Math.abs(avg).toFixed(prec) + ") * 100% = " + pctDiff.toFixed(prec) + "%";

        document.getElementById('res-steps').innerText = steps;

      } else if (mode === 'apply') {
        var base = parseFloat(document.getElementById('apply-base').value);
        var pct = parseFloat(document.getElementById('apply-pct').value);

        if (isNaN(base) || isNaN(pct)) {
          showError("Base and percentage values must be valid numbers.");
          return;
        }

        var changeAmount = base * (pct / 100);
        var finalVal = base + changeAmount;
        var factor = 1 + (pct / 100);

        document.getElementById('res-main').innerText = "Result: " + finalVal.toFixed(prec);
        document.getElementById('res-abs').innerText = (changeAmount >= 0 ? "+" : "") + changeAmount.toFixed(prec);
        document.getElementById('res-mult').innerText = factor.toFixed(prec) + "×";
        document.getElementById('res-rev').innerText = (- (pct / (100 + pct)) * 100).toFixed(prec) + "% to reset";
        document.getElementById('res-status').innerText = (pct >= 0 ? "Applied Increase" : "Applied Decrease");

        var steps = "Mode: Apply Percentage to Initial Base\n" +
                    "Base = " + base + ", Adjustment = " + pct + "%\n\n" +
                    "1. Change Amount: Base * (% / 100)\n" +
                    "   Δ = " + base + " * (" + pct + " / 100) = " + changeAmount.toFixed(prec) + "\n\n" +
                    "2. Final Result: Base + Δ\n" +
                    "   Result = " + base + " + (" + changeAmount.toFixed(prec) + ") = " + finalVal.toFixed(prec);

        document.getElementById('res-steps').innerText = steps;
      }
    }

    function showError(msg) {
      document.getElementById('res-main').innerText = "Error";
      document.getElementById('res-abs').innerText = "N/A";
      document.getElementById('res-mult').innerText = "N/A";
      document.getElementById('res-rev').innerText = "N/A";
      document.getElementById('res-status').innerText = "Invalid Input";
      document.getElementById('res-steps').innerText = "Error: " + msg;
    }

    function resetPercentChange() {
      document.getElementById('change-mode').value = 'change';
      document.getElementById('val-v1').value = '80';
      document.getElementById('val-v2').value = '120';
      document.getElementById('diff-a').value = '25';
      document.getElementById('diff-b').value = '35';
      document.getElementById('apply-base').value = '150';
      document.getElementById('apply-pct').value = '25';
      document.getElementById('precision-select').value = '4';
      switchChangeMode();
    }

    window.addEventListener('DOMContentLoaded', function() {
      calculatePercentChange();
    });
  </script>
</body>
</html>
"""

def main():
    p3 = os.path.join(BASE_DIR, "volume-calculator.html")
    with open(p3, "w", encoding="utf-8") as f:
        f.write(HTML_VOLUME)
    print("Generated:", p3)

    p4 = os.path.join(BASE_DIR, "percentage-change-calculator.html")
    with open(p4, "w", encoding="utf-8") as f:
        f.write(HTML_PERCENT_CHANGE)
    print("Generated:", p4)

if __name__ == "__main__":
    main()
