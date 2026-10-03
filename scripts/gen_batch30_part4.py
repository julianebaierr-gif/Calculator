# -*- coding: utf-8 -*-
"""
Generator for Batch 30 - Part 4:
7. triangle-area-calculator.html
8. variance-calculator.html
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 7. triangle-area-calculator.html
HTML_TRIANGLE = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Triangle Area Calculator - Heron's Formula, SAS, Base & Height, Coordinates</title>
  <meta name="description" content="Calculate triangle area using base and height, three sides (Heron's formula), side-angle-side (SAS), or 2D vertex coordinates with full step-by-step derivations.">
  <link rel="canonical" href="https://calchub.org/triangle-area-calculator.html">
  <meta property="og:title" content="Triangle Area Calculator - Multi-Method Geometric Solver">
  <meta property="og:description" content="Free multi-method triangle area calculator. Compute area, perimeter, inradius, and circumradius using Heron's formula, SAS, base-height, or coordinate geometry.">
  <meta property="og:url" content="https://calchub.org/triangle-area-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Triangle Area Calculator - Accurate Geometric Solver">
  <meta name="twitter:description" content="Calculate triangle area from 3 sides, base and height, SAS, or vertices. Includes step-by-step Heron's formula proofs, worked engineering examples, and formulas.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Triangle Area Calculator",
    "url": "https://calchub.org/triangle-area-calculator.html",
    "description": "Calculates the area, perimeter, semi-perimeter, inradius, and circumradius of any triangle using Base-Height, Heron's 3-side formula, SAS trigonometry, or Cartesian coordinates.",
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
        "name": "How do you calculate triangle area when only the three side lengths are known?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "When all three side lengths a, b, and c are known, use Heron's formula. First compute the semi-perimeter s = (a + b + c) / 2. Then the area is given by A = sqrt(s * (s - a) * (s - b) * (s - c))."
        }
      },
      {
        "@type": "Question",
        "name": "What is the formula for triangle area given two sides and the included angle (SAS)?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Given two side lengths a and b with included angle gamma between them, the area is calculated using trigonometry: A = 0.5 * a * b * sin(gamma). If the angle is provided in degrees, convert it to radians before evaluating the sine function."
        }
      },
      {
        "@type": "Question",
        "name": "How does the Shoelace formula calculate triangle area from coordinate vertices?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "For vertices (x1, y1), (x2, y2), and (x3, y3), the Shoelace (Gauss) formula calculates area as A = 0.5 * |x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)|. The absolute value ensures a positive area regardless of whether vertices are ordered clockwise or counterclockwise."
        }
      },
      {
        "@type": "Question",
        "name": "Can three arbitrary side lengths always form a valid triangle?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No. The triangle inequality theorem requires that the sum of any two side lengths must be strictly greater than the third side length: a + b > c, a + c > b, and b + c > a. If the sum equals the third side, the triangle degenerates into a flat line with zero area."
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
      <div class="calc-icon" aria-hidden="true">&#9651;</div>
      <h1>Triangle Area Calculator</h1>
      <p class="calc-description">Compute triangle area, perimeter, semi-perimeter, inradius, and circumradius using Base &amp; Height, Heron's Formula (3 sides), Side-Angle-Side (SAS), or Coordinate Geometry.</p>
    </div>

    <div class="calculator-body">
      <div class="input-group">
        <label for="method-select">Calculation Method</label>
        <select id="method-select" class="form-control" onchange="switchMethod()">
          <option value="base-height" selected>Base &amp; Height</option>
          <option value="sss">Three Sides (SSS / Heron's Formula)</option>
          <option value="sas">Side-Angle-Side (SAS Trigonometry)</option>
          <option value="coords">Vertex Coordinates (Shoelace Formula)</option>
        </select>
      </div>

      <!-- Method 1: Base & Height -->
      <div id="method-base-height" class="method-panel">
        <div class="input-grid">
          <div class="input-group">
            <label for="bh-base">Base Length (b)</label>
            <input type="number" id="bh-base" class="form-control" value="12" step="any" min="0">
            <span class="help-text">Linear dimension of triangle base</span>
          </div>
          <div class="input-group">
            <label for="bh-height">Perpendicular Height (h)</label>
            <input type="number" id="bh-height" class="form-control" value="8" step="any" min="0">
            <span class="help-text">Perpendicular altitude to the base</span>
          </div>
        </div>
      </div>

      <!-- Method 2: SSS / Heron's -->
      <div id="method-sss" class="method-panel" style="display:none;">
        <div class="input-grid">
          <div class="input-group">
            <label for="sss-a">Side a</label>
            <input type="number" id="sss-a" class="form-control" value="7" step="any" min="0">
            <span class="help-text">First side length</span>
          </div>
          <div class="input-group">
            <label for="sss-b">Side b</label>
            <input type="number" id="sss-b" class="form-control" value="8" step="any" min="0">
            <span class="help-text">Second side length</span>
          </div>
          <div class="input-group">
            <label for="sss-c">Side c</label>
            <input type="number" id="sss-c" class="form-control" value="9" step="any" min="0">
            <span class="help-text">Third side length</span>
          </div>
        </div>
      </div>

      <!-- Method 3: SAS -->
      <div id="method-sas" class="method-panel" style="display:none;">
        <div class="input-grid">
          <div class="input-group">
            <label for="sas-a">Side a</label>
            <input type="number" id="sas-a" class="form-control" value="10" step="any" min="0">
            <span class="help-text">First adjacent side</span>
          </div>
          <div class="input-group">
            <label for="sas-b">Side b</label>
            <input type="number" id="sas-b" class="form-control" value="14" step="any" min="0">
            <span class="help-text">Second adjacent side</span>
          </div>
          <div class="input-group">
            <label for="sas-angle">Included Angle (&gamma;)</label>
            <input type="number" id="sas-angle" class="form-control" value="45" step="any" min="0">
            <span class="help-text">Angle between sides a and b</span>
          </div>
          <div class="input-group">
            <label for="sas-unit">Angle Unit</label>
            <select id="sas-unit" class="form-control">
              <option value="deg" selected>Degrees (&deg;)</option>
              <option value="rad">Radians (rad)</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Method 4: Coordinates -->
      <div id="method-coords" class="method-panel" style="display:none;">
        <div class="input-grid">
          <div class="input-group">
            <label for="pt1-x">Vertex 1: x1</label>
            <input type="number" id="pt1-x" class="form-control" value="0" step="any">
          </div>
          <div class="input-group">
            <label for="pt1-y">Vertex 1: y1</label>
            <input type="number" id="pt1-y" class="form-control" value="0" step="any">
          </div>
          <div class="input-group">
            <label for="pt2-x">Vertex 2: x2</label>
            <input type="number" id="pt2-x" class="form-control" value="6" step="any">
          </div>
          <div class="input-group">
            <label for="pt2-y">Vertex 2: y2</label>
            <input type="number" id="pt2-y" class="form-control" value="0" step="any">
          </div>
          <div class="input-group">
            <label for="pt3-x">Vertex 3: x3</label>
            <input type="number" id="pt3-x" class="form-control" value="3" step="any">
          </div>
          <div class="input-group">
            <label for="pt3-y">Vertex 3: y3</label>
            <input type="number" id="pt3-y" class="form-control" value="5" step="any">
          </div>
        </div>
      </div>

      <div class="input-group">
        <label for="precision-select">Decimal Precision</label>
        <select id="precision-select" class="form-control">
          <option value="2">2 decimal places</option>
          <option value="4" selected>4 decimal places</option>
          <option value="6">6 decimal places</option>
        </select>
      </div>

      <div style="display:flex; gap:12px; margin-top:16px;">
        <button id="calc-btn" class="btn-primary" onclick="calculateTriangle()" style="flex:1;">Calculate Area</button>
        <button id="reset-btn" class="btn-secondary" onclick="resetTriangle()">Reset</button>
      </div>

      <div id="result-box" class="result-box" style="margin-top:24px;">
        <h2 class="result-title">Geometric Properties &amp; Dimensions</h2>
        <div class="result-highlight" style="font-size:1.8rem; font-weight:700; color:var(--primary); margin-bottom:16px;" id="res-area">
          Area: 48.0000 sq units
        </div>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:16px;">
          <div><span class="res-label">Perimeter (P):</span> <strong class="res-val" id="res-perimeter">N/A</strong></div>
          <div><span class="res-label">Semi-Perimeter (s):</span> <strong class="res-val" id="res-semiperimeter">N/A</strong></div>
          <div><span class="res-label">Inradius (r):</span> <strong class="res-val" id="res-inradius">N/A</strong></div>
          <div><span class="res-label">Circumradius (R):</span> <strong class="res-val" id="res-circumradius">N/A</strong></div>
          <div><span class="res-label">Triangle Type:</span> <strong class="res-val" id="res-type">Arbitrary Planar</strong></div>
        </div>
        <div id="res-steps" style="background:var(--bg-subtle, #f8fafc); padding:16px; border-radius:8px; font-family:monospace; font-size:0.95rem; white-space:pre-wrap; border:1px solid var(--border-color, #e2e8f0);"></div>
      </div>
    </div>

    <article class="article-body">
      <h2>Comprehensive Engineering &amp; Mathematical Guide to Triangle Area</h2>
      <p>The triangle represents the most fundamental two-dimensional polygonal structure in Euclidean geometry and structural engineering. Because three points in space define a unique plane and a triangle cannot deform without altering the length of its edges, triangles form the non-deformable building block of geodesic domes, architectural roof trusses, finite element meshes, and computer graphics polygon pipelines. Computing the area enclosed by a triangle is an indispensable operation across land surveying, geodesy, mechanical design, physics simulations, and satellite navigation.</p>
      
      <p>Depending on the spatial constraints, available measurement tools, and coordinate systems in a given engineering application, different geometric formulations must be employed. When surveying elevation and baseline dimensions, the classical perpendicular altitude method provides immediate results. When working with laser rangefinders measuring boundary fences, <a href="pythagorean-theorem-calculator.html">Heron's formula</a> yields exact surface areas from edge lengths without angle sensors. When robotic arms or total station theodolites measure angular bearing between arms, trigonometric formulations apply directly. In digital cartography and GIS shapefiles, coordinate determinants through the Shoelace algorithm provide closed-form polygon integration.</p>

      <h2>Mathematical Formulations &amp; Rigorous Proofs</h2>
      <p>To evaluate triangular areas with mathematical precision, we examine the four primary theoretical frameworks used in computational geometry.</p>

      <h3>1. Base and Perpendicular Altitude Formulation</h3>
      <p>The most elementary formulation derives from the area of an encompassing parallelogram or rectangle. For any triangle with a base side of length \(b\) and perpendicular altitude \(h\) extending from the opposite vertex to the line containing \(b\):</p>
      $$\text{Area} = \frac{1}{2} b h$$
      <p>This formulation holds true for acute, right, and obtuse triangles. In obtuse triangles where the altitude falls outside the boundary of the physical base, the signed area subtraction of the exterior right triangle proves identical equivalence through Euclid's dissection principle.</p>

      <h3>2. Heron's Formula (Three Known Sides: SSS)</h3>
      <p>Named after Hero of Alexandria (c. 10&ndash;70 AD), Heron's formula computes the area of a triangle directly from the lengths of its three sides \(a\), \(b\), and \(c\) without requiring explicit knowledge of internal angles or perpendicular heights. We first establish the semi-perimeter \(s\):</p>
      $$s = \frac{a + b + c}{2}$$
      <p>The enclosed planar area is expressed as the square root of the continued product:</p>
      $$\text{Area} = \sqrt{s(s - a)(s - b)(s - c)}$$
      <p>Heron's formula can be algebraically verified by combining the Law of Cosines with the trigonometric identity \(\sin^2(\gamma) + \cos^2(\gamma) = 1\). From the Law of Cosines, \(\cos(\gamma) = \frac{a^2 + b^2 - c^2}{2ab}\). Substituting into the trigonometric area formula \(\text{Area} = \frac{1}{2}ab\sin(\gamma) = \frac{1}{2}ab\sqrt{1 - \cos^2(\gamma)}\) and factoring the difference of squares yields the exact polynomial product \(s(s-a)(s-b)(s-c)\). You can explore radical evaluations using our <a href="square-root-calculator.html">Square Root Calculator</a>.</p>

      <h3>3. Side-Angle-Side (SAS) Trigonometric Formulation</h3>
      <p>When two boundary sides \(a\) and \(b\) and their included vertex angle \(\gamma\) are measured, trigonometry expresses the perpendicular altitude as \(h = b \sin(\gamma)\). Substituting this into the base-height formula produces:</p>
      $$\text{Area} = \frac{1}{2} a b \sin(\gamma)$$
      <p>By cyclic permutation of the vertices, equivalent formulations exist for all pairs of sides and included angles: \(\text{Area} = \frac{1}{2}bc\sin(\alpha) = \frac{1}{2}ca\sin(\beta)\). When dealing with a right-angled triangle where the included angle is \(\gamma = 90^\circ\), \(\sin(90^\circ) = 1\), simplifying immediately to the classic orthogonal product \(\frac{1}{2}ab\).</p>

      <h3>4. Shoelace Algorithm / Determinant Formulation (Coordinate Vertices)</h3>
      <p>In Cartesian coordinate geometry, GIS databases, and graphics shaders, triangle vertices are defined as ordered coordinate pairs \((x_1, y_1)\), \((x_2, y_2)\), and \((x_3, y_3)\). The area is calculated via the absolute value of the cross product determinant:</p>
      $$\text{Area} = \frac{1}{2} \left| x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2) \right|$$
      <p>In matrix notation, this represents half the determinant of a \(3 \times 3\) homogeneous coordinate matrix:</p>
      $$\text{Area} = \frac{1}{2} \left| \det \begin{pmatrix} x_1 & y_1 & 1 \\ x_2 & y_2 & 1 \\ x_3 & y_3 & 1 \end{pmatrix} \right|$$
      <p>This formulation provides numerical robustness and eliminates trigonometric rounding errors when processing digital vector geometry.</p>

      <h2>Inscribed, Circumscribed Circles and Geometric Invariants</h2>
      <p>Every planar non-degenerate triangle possesses an incircle (the unique circle tangent to all three sides) and a circumcircle (the unique circle passing through all three vertices). These auxiliary circles establish critical invariants in mechanical design and packing problems:</p>
      <div class="formula-box">
        <h3>Geometric Invariants</h3>
        $$\text{Inradius: } r = \frac{\text{Area}}{s} = \sqrt{\frac{(s-a)(s-b)(s-c)}{s}}$$
        $$\text{Circumradius: } R = \frac{a \cdot b \cdot c}{4 \cdot \text{Area}}$$
        $$\text{Euler's Inequality: } R \ge 2r \quad (\text{equality holds if and only if the triangle is equilateral})$$
      </div>

      <h2>Triangle Classification &amp; Geometric Benchmark Reference</h2>
      <p>The following technical reference matrix summarizes standard triangle classifications, required edge and angle relationships, and specialized closed-form area expressions:</p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Triangle Classification</th>
            <th>Side Relationships</th>
            <th>Internal Angles</th>
            <th>Specialized Area Formula</th>
            <th>Geometric Properties</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Equilateral</td>
            <td>\(a = b = c\)</td>
            <td>\(\alpha = \beta = \gamma = 60^\circ\)</td>
            <td>\(A = \frac{\sqrt{3}}{4} a^2 \approx 0.433013 a^2\)</td>
            <td>Maximal area per perimeter; \(R = 2r\)</td>
          </tr>
          <tr>
            <td>Right Isosceles (45-45-90)</td>
            <td>\(a = b, \; c = a\sqrt{2}\)</td>
            <td>\(45^\circ, 45^\circ, 90^\circ\)</td>
            <td>\(A = \frac{1}{2} a^2 = \frac{1}{4} c^2\)</td>
            <td>Half of a square; hypotenuse is diameter of circumcircle</td>
          </tr>
          <tr>
            <td>Special Right (30-60-90)</td>
            <td>\(a, \; b = a\sqrt{3}, \; c = 2a\)</td>
            <td>\(30^\circ, 60^\circ, 90^\circ\)</td>
            <td>\(A = \frac{\sqrt{3}}{2} a^2 \approx 0.866025 a^2\)</td>
            <td>Half of an equilateral triangle</td>
          </tr>
          <tr>
            <td>General Isosceles</td>
            <td>Two equal sides (\(a = b\))</td>
            <td>Two equal base angles</td>
            <td>\(A = \frac{c}{4} \sqrt{4a^2 - c^2}\)</td>
            <td>Altitude bisects base \(c\) orthogonally</td>
          </tr>
          <tr>
            <td>General Scalene (SSS)</td>
            <td>\(a \neq b \neq c\)</td>
            <td>All angles distinct</td>
            <td>\(A = \sqrt{s(s-a)(s-b)(s-c)}\)</td>
            <td>Requires Heron's general formulation</td>
          </tr>
          <tr>
            <td>Degenerate / Collinear</td>
            <td>\(a + b = c\)</td>
            <td>\(0^\circ, 0^\circ, 180^\circ\)</td>
            <td>\(A = 0.0000\)</td>
            <td>Vertices lie on a single line; zero enclosed area</td>
          </tr>
        </tbody>
      </table>

      <h2>Real-World Engineering &amp; Architectural Case Studies</h2>
      <p>The following practical examples demonstrate how these formulas are executed in actual architectural, civil, and geographic engineering scenarios.</p>

      <div class="worked-example-card">
        <h3>Case Study 1: Land Surveying &amp; Cadastral Boundary Computation (Coordinates)</h3>
        <p><strong>Scenario:</strong> A licensed land surveyor maps a triangular property plot using satellite RTK-GPS coordinates. The boundary pins are recorded at the following local plane coordinates (in meters): Vertex 1 \((12.0, 18.0)\), Vertex 2 \((84.0, 36.0)\), and Vertex 3 \((45.0, 92.0)\). The surveyor must determine the legal cadastral deed area.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Apply the Shoelace determinant formula:
            $$A = \frac{1}{2} |x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)|$$
          </li>
          <li>Substitute the coordinate values:
            $$x_1(y_2 - y_3) = 12.0 \times (36.0 - 92.0) = 12.0 \times (-56.0) = -672.0$$
            $$x_2(y_3 - y_1) = 84.0 \times (92.0 - 18.0) = 84.0 \times 74.0 = 6216.0$$
            $$x_3(y_1 - y_2) = 45.0 \times (18.0 - 36.0) = 45.0 \times (-18.0) = -810.0$$
          </li>
          <li>Sum the components and compute half the absolute value:
            $$\text{Sum} = -672.0 + 6216.0 - 810.0 = 4734.0$$
            $$A = \frac{1}{2} |4734.0| = 2367.0000 \text{ m}^2$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The triangular parcel encloses exactly \(2,367.0000 \text{ m}^2\) (approximately \(0.2367\) hectares or \(0.585\) acres).</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Structural Roof Truss Wind-Load Analysis (Heron's Formula)</h3>
        <p><strong>Scenario:</strong> A structural engineer designs a timber roof truss spanning three structural steel connection nodes. Laser distance measurement confirms the lengths of the three timber beams forming the triangular bay are \(a = 15.0 \text{ ft}\), \(b = 20.0 \text{ ft}\), and \(c = 25.0 \text{ ft}\). The tributary wind exposure calculation requires the exact surface area of the bay.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Verify the triangle inequality: \(15 + 20 = 35 > 25\), confirming a valid triangle.</li>
          <li>Calculate the semi-perimeter \(s\):
            $$s = \frac{15.0 + 20.0 + 25.0}{2} = \frac{60.0}{2} = 30.0 \text{ ft}$$
          </li>
          <li>Calculate the side differences:
            $$s - a = 30.0 - 15.0 = 15.0 \text{ ft}$$
            $$s - b = 30.0 - 20.0 = 10.0 \text{ ft}$$
            $$s - c = 30.0 - 25.0 = 5.0 \text{ ft}$$
          </li>
          <li>Apply Heron's formula:
            $$A = \sqrt{30.0 \times 15.0 \times 10.0 \times 5.0} = \sqrt{22500} = 150.0000 \text{ ft}^2$$
          </li>
        </ol>
        <p><strong>Cross-Check:</strong> Notice that \(15^2 + 20^2 = 225 + 400 = 625 = 25^2\). This is a scaled 3-4-5 right triangle. The standard right triangle formula confirms \(\frac{1}{2} \times 15 \times 20 = 150 \text{ ft}^2\), perfectly matching Heron's result.</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 3: Robotic Arm Workspace Triangular Sector (SAS Formulation)</h3>
        <p><strong>Scenario:</strong> A dual-link SCARA manufacturing robot has linkage arm lengths \(a = 450 \text{ mm}\) and \(b = 600 \text{ mm}\). When the elbow joint flexes to an included interior angle of \(\gamma = 54^\circ\), the robotic safety system must compute the dynamic swept triangular collision envelope.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Convert the angle from degrees to radians for numerical computation:
            $$\gamma = 54^\circ \times \frac{\pi}{180^\circ} \approx 0.942478 \text{ rad}$$
          </li>
          <li>Compute the sine of the included angle:
            $$\sin(54^\circ) \approx 0.809017$$
          </li>
          <li>Apply the Side-Angle-Side area formula:
            $$A = \frac{1}{2} \times 450 \times 600 \times 0.809017 = 135000 \times 0.809017 = 109217.2936 \text{ mm}^2$$
          </li>
          <li>Convert to standard SI square meters:
            $$A = 109217.2936 \times 10^{-6} \text{ m}^2 \approx 0.1092 \text{ m}^2$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The swept instantaneous safety envelope encompasses \(109,217.2936 \text{ mm}^2\).</p>
      </div>

      <h2>Numerical Stability &amp; Floating-Point Precision Considerations</h2>
      <p>When implementing Heron's formula in computer software for "needle-like" triangles (where two sides are nearly equal and the third side is extremely short or nearly equals their sum), standard floating-point evaluation can suffer catastrophic cancellation. Subtracting numbers that are nearly identical in \((s - c)\) causes significant loss of significant digits. In 1986, computer scientist William Kahan proposed a numerically stable reformulation:</p>
      $$\text{First sort sides such that } a \ge b \ge c$$
      $$\text{Area} = \frac{1}{4} \sqrt{(a + (b + c))(c - (a - b))(c + (a - b))(a + (b - c))}$$
      <p>By evaluating the innermost parentheses first, catastrophic subtractive cancellation is eliminated across IEEE 754 floating-point arithmetic engines.</p>

      <h2>Frequently Asked Questions</h2>
      <div class="faq-item">
        <div class="faq-question">What is a degenerate triangle and how does the calculator handle it?</div>
        <div class="faq-answer">A degenerate triangle occurs when the sum of the two shorter sides exactly equals the longest side (\(a + b = c\)). In this case, the three vertices fall on a single straight collinear line. The semi-perimeter product \((s - c)\) becomes zero, resulting in an area of zero square units. If the sum is strictly less than the longest side, the side lengths violate the triangle inequality theorem and cannot close into a geometric polygon.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">How are inradius and circumradius derived from the triangle area?</div>
        <div class="faq-answer">The inradius \(r\) is calculated by dividing the total area by the semi-perimeter: \(r = A / s\). This comes from dissecting the triangle into three smaller triangles sharing the incenter. The circumradius \(R\) is determined by dividing the product of all three sides by four times the area: \(R = (a \cdot b \cdot c) / (4A)\).</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Why does the Shoelace formula produce a negative number if vertices are in clockwise order?</div>
        <div class="faq-answer">The Shoelace algorithm calculates the signed area of a 2D planar polygon. If vertices are traversed in counterclockwise (CCW) orientation according to the right-hand rule, the cross products sum to a positive value. Traversing in clockwise order reverses the orientation of the boundary normal vector, resulting in a negative sign. Taking the absolute value guarantees the physical geometric area is always positive.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Which method is most accurate for measuring irregularly shaped property plots?</div>
        <div class="faq-answer">For legal cadastral boundaries, the coordinate method (Shoelace formula) using geodetic GPS coordinates provides the highest accuracy because it directly processes plane coordinates without accumulating angle or slope measuring errors. For onsite physical measurements where only boundary tape or laser distometers are available, dividing the land into triangles and applying Heron's formula on each segment is standard practice.</div>
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
    function switchMethod() {
      var method = document.getElementById('method-select').value;
      var panels = document.querySelectorAll('.method-panel');
      panels.forEach(function(p) { p.style.display = 'none'; });
      var activePanel = document.getElementById('method-' + method);
      if (activePanel) activePanel.style.display = 'block';
      calculateTriangle();
    }

    function calculateTriangle() {
      var method = document.getElementById('method-select').value;
      var prec = parseInt(document.getElementById('precision-select').value, 10) || 4;
      
      var area = 0, p = 0, s = 0, inradius = 0, circumradius = 0;
      var triType = "General Planar";
      var steps = "";

      if (method === 'base-height') {
        var b = parseFloat(document.getElementById('bh-base').value);
        var h = parseFloat(document.getElementById('bh-height').value);
        if (isNaN(b) || isNaN(h) || b <= 0 || h <= 0) {
          showError("Base and height must be positive real numbers.");
          return;
        }
        area = 0.5 * b * h;
        steps = "Calculation Method: Base & Height\n" +
                "Formula: Area = (1/2) * b * h\n" +
                "Substitution: Area = 0.5 * " + b + " * " + h + " = " + area.toFixed(prec) + " sq units\n\n" +
                "Note: Perimeter and auxiliary radii require side lengths.";
        document.getElementById('res-area').innerText = "Area: " + area.toFixed(prec) + " sq units";
        document.getElementById('res-perimeter').innerText = "Requires side lengths";
        document.getElementById('res-semiperimeter').innerText = "Requires side lengths";
        document.getElementById('res-inradius').innerText = "Requires side lengths";
        document.getElementById('res-circumradius').innerText = "Requires side lengths";
        document.getElementById('res-type').innerText = "Right or General (Base & Alt)";
        document.getElementById('res-steps').innerText = steps;
        return;
      }

      var a = 0, b_side = 0, c = 0;

      if (method === 'sss') {
        a = parseFloat(document.getElementById('sss-a').value);
        b_side = parseFloat(document.getElementById('sss-b').value);
        c = parseFloat(document.getElementById('sss-c').value);

        if (isNaN(a) || isNaN(b_side) || isNaN(c) || a <= 0 || b_side <= 0 || c <= 0) {
          showError("All three side lengths must be positive real numbers.");
          return;
        }

        // Triangle Inequality check
        if (a + b_side <= c || a + c <= b_side || b_side + c <= a) {
          showError("Triangle Inequality Violated: The sum of any two sides must exceed the third side.");
          return;
        }

        p = a + b_side + c;
        s = p / 2;
        var radicand = s * (s - a) * (s - b_side) * (s - c);
        area = Math.sqrt(Math.max(0, radicand));
        inradius = area / s;
        circumradius = (a * b_side * c) / (4 * area);

        steps = "Calculation Method: Heron's Formula (SSS)\n" +
                "Side a = " + a + ", Side b = " + b_side + ", Side c = " + c + "\n" +
                "1. Semi-Perimeter s = (a + b + c) / 2 = (" + a + " + " + b_side + " + " + c + ") / 2 = " + s.toFixed(prec) + "\n" +
                "2. Factors:\n" +
                "   (s - a) = " + (s - a).toFixed(prec) + "\n" +
                "   (s - b) = " + (s - b_side).toFixed(prec) + "\n" +
                "   (s - c) = " + (s - c).toFixed(prec) + "\n" +
                "3. Area = sqrt[s * (s - a) * (s - b) * (s - c)]\n" +
                "   Area = sqrt[" + s.toFixed(prec) + " * " + (s - a).toFixed(prec) + " * " + (s - b_side).toFixed(prec) + " * " + (s - c).toFixed(prec) + "]\n" +
                "   Area = " + area.toFixed(prec) + " sq units\n\n" +
                "4. Aux Radii:\n" +
                "   Inradius r = Area / s = " + inradius.toFixed(prec) + "\n" +
                "   Circumradius R = (a*b*c) / (4*Area) = " + circumradius.toFixed(prec);

      } else if (method === 'sas') {
        a = parseFloat(document.getElementById('sas-a').value);
        b_side = parseFloat(document.getElementById('sas-b').value);
        var angleVal = parseFloat(document.getElementById('sas-angle').value);
        var unit = document.getElementById('sas-unit').value;

        if (isNaN(a) || isNaN(b_side) || isNaN(angleVal) || a <= 0 || b_side <= 0 || angleVal <= 0) {
          showError("Sides and angle must be positive real numbers.");
          return;
        }

        var radAngle = (unit === 'deg') ? (angleVal * Math.PI / 180) : angleVal;
        if (radAngle >= Math.PI) {
          showError("Included angle must be strictly less than 180 degrees (pi radians).");
          return;
        }

        area = 0.5 * a * b_side * Math.sin(radAngle);
        // Compute side c via law of cosines
        c = Math.sqrt(Math.max(0, a * a + b_side * b_side - 2 * a * b_side * Math.cos(radAngle)));
        p = a + b_side + c;
        s = p / 2;
        inradius = area / s;
        circumradius = (a * b_side * c) / (4 * area);

        steps = "Calculation Method: Side-Angle-Side (SAS)\n" +
                "Side a = " + a + ", Side b = " + b_side + ", Included Angle = " + angleVal + " " + unit + "\n" +
                "1. Area = (1/2) * a * b * sin(gamma)\n" +
                "   Area = 0.5 * " + a + " * " + b_side + " * sin(" + radAngle.toFixed(prec) + " rad)\n" +
                "   Area = " + area.toFixed(prec) + " sq units\n\n" +
                "2. Third Side c (Law of Cosines): c = sqrt[a^2 + b^2 - 2ab*cos(gamma)] = " + c.toFixed(prec) + "\n" +
                "3. Perimeter P = " + p.toFixed(prec) + ", Semi-perimeter s = " + s.toFixed(prec) + "\n" +
                "4. Inradius r = " + inradius.toFixed(prec) + ", Circumradius R = " + circumradius.toFixed(prec);

      } else if (method === 'coords') {
        var x1 = parseFloat(document.getElementById('pt1-x').value);
        var y1 = parseFloat(document.getElementById('pt1-y').value);
        var x2 = parseFloat(document.getElementById('pt2-x').value);
        var y2 = parseFloat(document.getElementById('pt2-y').value);
        var x3 = parseFloat(document.getElementById('pt3-x').value);
        var y3 = parseFloat(document.getElementById('pt3-y').value);

        if ([x1,y1,x2,y2,x3,y3].some(isNaN)) {
          showError("All six vertex coordinate values must be valid real numbers.");
          return;
        }

        var det = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2);
        area = 0.5 * Math.abs(det);

        // Side lengths
        a = Math.hypot(x2 - x3, y2 - y3);
        b_side = Math.hypot(x1 - x3, y1 - y3);
        c = Math.hypot(x1 - x2, y1 - y2);

        if (area < 1e-9) {
          showError("Collinear Points: The three coordinates lie on a straight line. Area is 0.");
          return;
        }

        p = a + b_side + c;
        s = p / 2;
        inradius = area / s;
        circumradius = (a * b_side * c) / (4 * area);

        steps = "Calculation Method: Shoelace Coordinate Formula\n" +
                "Vertices: (" + x1 + "," + y1 + "), (" + x2 + "," + y2 + "), (" + x3 + "," + y3 + ")\n" +
                "1. Determinant = x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)\n" +
                "   = " + x1 + "*(" + (y2-y3) + ") + " + x2 + "*(" + (y3-y1) + ") + " + x3 + "*(" + (y1-y2) + ") = " + det.toFixed(prec) + "\n" +
                "2. Area = (1/2) * |Determinant| = " + area.toFixed(prec) + " sq units\n\n" +
                "3. Edge lengths:\n" +
                "   Side a = " + a.toFixed(prec) + ", Side b = " + b_side.toFixed(prec) + ", Side c = " + c.toFixed(prec) + "\n" +
                "4. Perimeter P = " + p.toFixed(prec) + ", Inradius r = " + inradius.toFixed(prec) + ", Circumradius R = " + circumradius.toFixed(prec);
      }

      // Classify triangle
      var sides = [a, b_side, c].sort(function(x, y) { return x - y; });
      var s1 = sides[0], s2 = sides[1], s3 = sides[2];
      var sideClass = "Scalene";
      if (Math.abs(s1 - s3) < 1e-5) sideClass = "Equilateral";
      else if (Math.abs(s1 - s2) < 1e-5 || Math.abs(s2 - s3) < 1e-5) sideClass = "Isosceles";

      var angleClass = "Acute";
      var pythDiff = s1 * s1 + s2 * s2 - s3 * s3;
      if (Math.abs(pythDiff) < 1e-4) angleClass = "Right";
      else if (pythDiff < 0) angleClass = "Obtuse";

      triType = sideClass + " (" + angleClass + ")";

      document.getElementById('res-area').innerText = "Area: " + area.toFixed(prec) + " sq units";
      document.getElementById('res-perimeter').innerText = p.toFixed(prec);
      document.getElementById('res-semiperimeter').innerText = s.toFixed(prec);
      document.getElementById('res-inradius').innerText = inradius.toFixed(prec);
      document.getElementById('res-circumradius').innerText = circumradius.toFixed(prec);
      document.getElementById('res-type').innerText = triType;
      document.getElementById('res-steps').innerText = steps;
    }

    function showError(msg) {
      document.getElementById('res-area').innerText = "Error";
      document.getElementById('res-perimeter').innerText = "N/A";
      document.getElementById('res-semiperimeter').innerText = "N/A";
      document.getElementById('res-inradius').innerText = "N/A";
      document.getElementById('res-circumradius').innerText = "N/A";
      document.getElementById('res-type').innerText = "Invalid Geometry";
      document.getElementById('res-steps').innerText = "Error: " + msg;
    }

    function resetTriangle() {
      document.getElementById('method-select').value = 'base-height';
      document.getElementById('bh-base').value = '12';
      document.getElementById('bh-height').value = '8';
      document.getElementById('sss-a').value = '7';
      document.getElementById('sss-b').value = '8';
      document.getElementById('sss-c').value = '9';
      document.getElementById('sas-a').value = '10';
      document.getElementById('sas-b').value = '14';
      document.getElementById('sas-angle').value = '45';
      document.getElementById('sas-unit').value = 'deg';
      document.getElementById('pt1-x').value = '0';
      document.getElementById('pt1-y').value = '0';
      document.getElementById('pt2-x').value = '6';
      document.getElementById('pt2-y').value = '0';
      document.getElementById('pt3-x').value = '3';
      document.getElementById('pt3-y').value = '5';
      document.getElementById('precision-select').value = '4';
      switchMethod();
    }

    window.addEventListener('DOMContentLoaded', function() {
      calculateTriangle();
    });
  </script>
</body>
</html>
"""

# 8. variance-calculator.html
HTML_VARIANCE = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Variance Calculator - Sample &amp; Population Dispersion Solver</title>
  <meta name="description" content="Calculate sample variance (s^2), population variance (sigma^2), standard deviation, mean, and sum of squared deviations with full step-by-step tables.">
  <link rel="canonical" href="https://calchub.org/variance-calculator.html">
  <meta property="og:title" content="Variance Calculator - Sample &amp; Population Statistical Dispersion">
  <meta property="og:description" content="Free statistical variance calculator. Compute sample variance with Bessel's correction (n - 1), population variance (N), standard deviation, and step-by-step deviations.">
  <meta property="og:url" content="https://calchub.org/variance-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Variance Calculator - Accurate Statistical Dispersion Tool">
  <meta name="twitter:description" content="Calculate statistical variance, standard deviation, and sum of squares for sample and population data with complete step-by-step deviation tables.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Variance Calculator",
    "url": "https://calchub.org/variance-calculator.html",
    "description": "Calculates sample variance (s^2), population variance (sigma^2), standard deviation, mean, sum of squared deviations, and step-by-step deviation tables.",
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
        "name": "What is the difference between sample variance and population variance?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Population variance (sigma^2) measures dispersion across every single member of an entire target population and divides the sum of squared deviations by N. Sample variance (s^2) estimates population variance from a subset sample and divides by n - 1 (Bessel's correction) to correct for sample mean bias."
        }
      },
      {
        "@type": "Question",
        "name": "Why does sample variance divide by (n - 1) instead of n?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Dividing by n - 1 is known as Bessel's correction. Because the true population mean is unknown, sample deviations are calculated relative to the sample mean x-bar. Deviations around x-bar are always smaller on average than deviations around the true mean mu, causing an uncorrected sample variance to underestimate true variance. Dividing by n - 1 restores an unbiased expected value."
        }
      },
      {
        "@type": "Question",
        "name": "How does variance relate to standard deviation?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Standard deviation is simply the positive square root of variance: s = sqrt(s^2) or sigma = sqrt(sigma^2). While variance is expressed in squared units of the original data, standard deviation is expressed in the identical original measurement units, making it more intuitive to interpret."
        }
      },
      {
        "@type": "Question",
        "name": "Can statistical variance ever be negative?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No. In real-valued mathematical statistics, variance can never be negative. It is the average of squared deviations (x - mean)^2, and the square of any real number is non-negative. A variance of zero indicates that every single observation in the dataset is identical."
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
      <div class="calc-icon" aria-hidden="true">&#963;<sup>2</sup></div>
      <h1>Variance Calculator</h1>
      <p class="calc-description">Compute sample variance (s<sup>2</sup>), population variance (&sigma;<sup>2</sup>), standard deviation, sum of squares, and complete step-by-step deviation tables.</p>
    </div>

    <div class="calculator-body">
      <div class="input-group">
        <label for="dataset-input">Dataset Values</label>
        <textarea id="dataset-input" class="form-control" rows="4" placeholder="Enter numbers separated by commas, spaces, or newlines, e.g. 14, 22, 19, 25, 30, 21, 28">14, 22, 19, 25, 30, 21, 28</textarea>
        <span class="help-text">Accepts integers and decimal values separated by commas, spaces, tabs, or line breaks.</span>
      </div>

      <div class="input-grid">
        <div class="input-group">
          <label for="var-type">Calculation Scope</label>
          <select id="var-type" class="form-control" onchange="calculateVariance()">
            <option value="sample" selected>Sample Variance (s&sup2;, divide by n - 1)</option>
            <option value="population">Population Variance (&sigma;&sup2;, divide by N)</option>
          </select>
        </div>
        <div class="input-group">
          <label for="precision-select">Decimal Precision</label>
          <select id="precision-select" class="form-control" onchange="calculateVariance()">
            <option value="2">2 decimal places</option>
            <option value="4" selected>4 decimal places</option>
            <option value="6">6 decimal places</option>
          </select>
        </div>
      </div>

      <div style="display:flex; gap:12px; margin-top:16px;">
        <button id="calc-btn" class="btn-primary" onclick="calculateVariance()" style="flex:1;">Compute Variance</button>
        <button id="reset-btn" class="btn-secondary" onclick="resetVariance()">Reset</button>
      </div>

      <div id="result-box" class="result-box" style="margin-top:24px;">
        <h2 class="result-title">Statistical Dispersion Summary</h2>
        <div class="result-highlight" style="font-size:1.8rem; font-weight:700; color:var(--primary); margin-bottom:16px;" id="res-var">
          Variance (s&sup2;): 28.2381
        </div>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:16px;">
          <div><span class="res-label">Standard Deviation:</span> <strong class="res-val" id="res-sd">5.3140</strong></div>
          <div><span class="res-label">Arithmetic Mean (&mu; / x̄):</span> <strong class="res-val" id="res-mean">22.7143</strong></div>
          <div><span class="res-label">Observations Count (n):</span> <strong class="res-val" id="res-count">7</strong></div>
          <div><span class="res-label">Sum of Squares (SS):</span> <strong class="res-val" id="res-ss">169.4286</strong></div>
          <div><span class="res-label">Sum (&sum;x):</span> <strong class="res-val" id="res-sum">159.0000</strong></div>
          <div><span class="res-label">Std Error of Mean (SE):</span> <strong class="res-val" id="res-se">2.0085</strong></div>
          <div><span class="res-label">Coeff. of Variation (CV):</span> <strong class="res-val" id="res-cv">23.3941%</strong></div>
        </div>

        <h3 style="margin-top:20px; font-size:1.1rem; color:var(--text-dark);">Step-by-Step Calculation Breakdown</h3>
        <div id="res-steps" style="background:var(--bg-subtle, #f8fafc); padding:16px; border-radius:8px; font-family:monospace; font-size:0.95rem; white-space:pre-wrap; border:1px solid var(--border-color, #e2e8f0); margin-bottom:16px;"></div>

        <h3 style="margin-top:16px; font-size:1.1rem; color:var(--text-dark);">Data Point Deviation Table</h3>
        <div style="overflow-x:auto;">
          <table class="data-table" id="res-table" style="width:100%; margin-top:8px;">
            <thead>
              <tr>
                <th>Index (i)</th>
                <th>Observation (x<sub>i</sub>)</th>
                <th>Deviation (x<sub>i</sub> - x̄)</th>
                <th>Squared Deviation (x<sub>i</sub> - x̄)&sup2;</th>
              </tr>
            </thead>
            <tbody id="res-table-body"></tbody>
          </table>
        </div>
      </div>
    </div>

    <article class="article-body">
      <h2>Comprehensive Engineering &amp; Statistical Guide to Variance</h2>
      <p>In mathematical statistics, probability theory, and data science, variance represents the second central moment of a probability distribution. It serves as the primary quantitative measure of statistical dispersion, quantifying the expected squared distance of individual data points from their arithmetic mean. While the mean, median, and mode describe the central tendency of a dataset (explored in our <a href="mean-median-mode-calculator.html">Mean Median Mode Calculator</a>), variance reveals how tightly the data clusters around that center or how broadly it is dispersed across the distribution space.</p>

      <p>Variance plays an indispensable role across scientific and engineering disciplines. In finance and asset management, variance quantifies portfolio volatility and underpins Harry Markowitz's Modern Portfolio Theory. In mechanical engineering and manufacturing quality control, variance in machine tolerances defines Six Sigma process capability indices (\(C_p\) and \(C_{pk}\)). In genetics, Ronald Fisher introduced the Analysis of Variance (ANOVA) to partition total phenotypic variance into additive genetic and environmental components. In machine learning, the bias-variance tradeoff governs model generalization error, regularization, and overfitting.</p>

      <h2>Mathematical Formulations: Population vs. Sample Variance</h2>
      <p>A crucial distinction in inferential statistics is the difference between an entire population and a representative sample drawn from that population.</p>

      <h3>1. Population Variance (\(\sigma^2\))</h3>
      <p>When you have access to every individual observation in a complete target population consisting of \(N\) elements, the population mean \(\mu\) is known with absolute certainty. The population variance \(\sigma^2\) is defined as the arithmetic average of all squared deviations:</p>
      $$\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2$$
      <p>Where:</p>
      <ul>
        <li>\(\sigma^2\) is the population variance (sigma squared).</li>
        <li>\(N\) is the total finite population size.</li>
        <li>\(x_i\) represents each individual observation.</li>
        <li>\(\mu = \frac{1}{N}\sum_{i=1}^{N} x_i\) is the true population arithmetic mean.</li>
      </ul>

      <h3>2. Sample Variance (\(s^2\)) &amp; Bessel's Correction</h3>
      <p>In virtually all real-world scientific investigations, observing the entire population is financially or physically impossible. Instead, researchers collect a random sample of size \(n\). Because the true population mean \(\mu\) is unknown, researchers must approximate it using the sample mean \(\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i\).</p>
      <p>Crucially, individual sample data points are mathematically closer to their own sample mean \(\bar{x}\) than to the true, unknown population mean \(\mu\). If we were to divide the sum of squared sample deviations by \(n\), the resulting estimator would systematically underestimate the true population variance by a factor of \(\frac{n-1}{n}\). To eliminate this downward bias, German astronomer Friedrich Wilhelm Bessel introduced Bessel's correction, replacing \(n\) with the degrees of freedom \(n - 1\):</p>
      $$s^2 = \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2$$
      <p>Because the expected value of this estimator satisfies \(\mathbb{E}[s^2] = \sigma^2\), sample variance using \(n - 1\) is an unbiased estimator of population variance.</p>

      <h3>3. Computational Shortcut Formula vs. Two-Pass Algorithm</h3>
      <p>Expanding the polynomial \((x_i - \bar{x})^2 = x_i^2 - 2x_i\bar{x} + \bar{x}^2\) yields the classic computational shortcut formula:</p>
      $$s^2 = \frac{\sum_{i=1}^{n} x_i^2 - \frac{(\sum_{i=1}^{n} x_i)^2}{n}}{n - 1}$$
      <p>While mathematically identical in infinite-precision arithmetic, this shortcut formula can suffer from catastrophic cancellation in floating-point software when data values are large with tiny variance. To ensure absolute numerical accuracy, modern statistical software (including this calculator) computes the mean first, then sums the squared differences in a stable two-pass algorithm, or utilizes B. P. Welford's running one-pass recurrence algorithm.</p>

      <h2>Relationship to Standard Deviation &amp; Auxiliary Dispersion Metrics</h2>
      <p>Because variance squares the deviation distances, its resulting numerical output is expressed in squared units (e.g., \(\text{meters}^2\), \(\text{dollars}^2\), or \(\text{seconds}^2\)). While mathematically essential for linear algebra and ANOVA partitions, squared units lack intuitive dimensional interpretability. Taking the positive square root of variance yields the <a href="standard-deviation-calculator.html">Standard Deviation</a>, which returns the measure of dispersion back to original units:</p>
      $$s = \sqrt{s^2}, \quad \sigma = \sqrt{\sigma^2}$$
      <p>Other vital dispersion metrics derived directly from variance include:</p>
      <div class="formula-box">
        <h3>Derived Dispersion Metrics</h3>
        $$\text{Standard Error of the Mean (SE): } SE = \frac{s}{\sqrt{n}}$$
        $$\text{Coefficient of Variation (CV): } CV = \left( \frac{s}{\bar{x}} \right) \times 100\%$$
        $$\text{Sum of Squared Errors (SS): } SS = \sum_{i=1}^{n} (x_i - \bar{x})^2 = (n - 1)s^2$$
      </div>

      <h2>Statistical Dispersion Metric Comparison Table</h2>
      <p>The following multi-column benchmark matrix summarizes the mathematical characteristics, bias properties, degrees of freedom, and typical applications of variance and its related dispersion metrics:</p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Dispersion Metric</th>
            <th>Symbol</th>
            <th>Formula</th>
            <th>Denominator</th>
            <th>Bias Property</th>
            <th>Primary Application</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Sample Variance</td>
            <td>\(s^2\)</td>
            <td>\(\frac{\sum (x_i - \bar{x})^2}{n - 1}\)</td>
            <td>\(n - 1\) (Degrees of Freedom)</td>
            <td>Unbiased for \(\sigma^2\)</td>
            <td>Inferential research, ANOVA, t-tests, regression analysis</td>
          </tr>
          <tr>
            <td>Population Variance</td>
            <td>\(\sigma^2\)</td>
            <td>\(\frac{\sum (x_i - \mu)^2}{N}\)</td>
            <td>\(N\) (Total Population)</td>
            <td>Exact parameter</td>
            <td>Complete census datasets, theoretical probability distributions</td>
          </tr>
          <tr>
            <td>Sample Standard Deviation</td>
            <td>\(s\)</td>
            <td>\(\sqrt{s^2}\)</td>
            <td>\(\sqrt{n - 1}\)</td>
            <td>Slightly biased (Jensen's inequality)</td>
            <td>Confidence intervals, error bars, empirical rule (68-95-99.7%)</td>
          </tr>
          <tr>
            <td>Population Standard Deviation</td>
            <td>\(\sigma\)</td>
            <td>\(\sqrt{\sigma^2}\)</td>
            <td>\(\sqrt{N}\)</td>
            <td>Exact parameter</td>
            <td>Z-score standardization, normal distribution modeling</td>
          </tr>
          <tr>
            <td>Sum of Squares (SS)</td>
            <td>\(SS\)</td>
            <td>\(\sum (x_i - \bar{x})^2\)</td>
            <td>\(1\) (No division)</td>
            <td>Additive metric</td>
            <td>Partition of variance in regression sum of squares (SSR, SSE, SST)</td>
          </tr>
          <tr>
            <td>Standard Error of the Mean</td>
            <td>\(SE\)</td>
            <td>\(\frac{s}{\sqrt{n}}\)</td>
            <td>\(\sqrt{n(n - 1)}\)</td>
            <td>Unbiased estimator of sampling variability</td>
            <td>Sampling distribution spread, margin of error in polling</td>
          </tr>
          <tr>
            <td>Coefficient of Variation</td>
            <td>\(CV\)</td>
            <td>\(\frac{s}{\bar{x}} \times 100\%\)</td>
            <td>Dimensionless ratio</td>
            <td>Normalized relative variability</td>
            <td>Comparing variability across different units (e.g. weight vs height)</td>
          </tr>
        </tbody>
      </table>

      <h2>Real-World Engineering, Clinical &amp; Financial Case Studies</h2>
      <p>The following real-world worked case studies demonstrate how statistical variance is computed and applied in practical industrial, financial, and clinical environments.</p>

      <div class="worked-example-card">
        <h3>Case Study 1: Modern Portfolio Theory &amp; Financial Asset Variance</h3>
        <p><strong>Scenario:</strong> A quantitative investment analyst evaluates the annual return volatility of a technology hedge fund over a 5-year sample window. The recorded annual returns are: \(12.0\%\), \(-4.0\%\), \(18.0\%\), \(6.0\%\), and \(8.0\%\). The analyst must compute the sample variance and standard deviation to determine the portfolio's Sharpe ratio risk penalty.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Calculate the sample mean return \(\bar{x}\):
            $$\bar{x} = \frac{12.0 + (-4.0) + 18.0 + 6.0 + 8.0}{5} = \frac{40.0}{5} = 8.0\%$$
          </li>
          <li>Compute deviations and squared deviations from the mean for each year:
            <ul>
              <li>Year 1: \((12.0 - 8.0) = +4.0 \implies (+4.0)^2 = 16.0\)</li>
              <li>Year 2: \((-4.0 - 8.0) = -12.0 \implies (-12.0)^2 = 144.0\)</li>
              <li>Year 3: \((18.0 - 8.0) = +10.0 \implies (+10.0)^2 = 100.0\)</li>
              <li>Year 4: \((6.0 - 8.0) = -2.0 \implies (-2.0)^2 = 4.0\)</li>
              <li>Year 5: \((8.0 - 8.0) = 0.0 \implies (0.0)^2 = 0.0\)</li>
            </ul>
          </li>
          <li>Sum the squared deviations (Sum of Squares, SS):
            $$SS = 16.0 + 144.0 + 100.0 + 4.0 + 0.0 = 264.0$$
          </li>
          <li>Apply Bessel's correction with degrees of freedom \(n - 1 = 5 - 1 = 4\):
            $$s^2 = \frac{SS}{n - 1} = \frac{264.0}{4} = 66.0000 (\%^2)$$
          </li>
          <li>Compute sample standard deviation:
            $$s = \sqrt{66.0} \approx 8.1240\%$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The hedge fund has a sample variance of \(66.0000 (\%^2)\) and an annualized return volatility (standard deviation) of \(8.1240\%\).</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Six Sigma Precision Machining Quality Control</h3>
        <p><strong>Scenario:</strong> A CNC lathe manufactures titanium orthopedic bone screws with a nominal target shaft diameter of \(4.500 \text{ mm}\). A quality assurance engineer measures a random batch of 6 finished screws: \(4.502\), \(4.498\), \(4.505\), \(4.496\), \(4.500\), and \(4.501 \text{ mm}\). The ISO 13485 quality standard mandates that the batch variance \(s^2\) must not exceed \(0.000015 \text{ mm}^2\).</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Calculate sample mean shaft diameter:
            $$\bar{x} = \frac{4.502 + 4.498 + 4.505 + 4.496 + 4.500 + 4.501}{6} = \frac{27.002}{6} \approx 4.500333 \text{ mm}$$
          </li>
          <li>Calculate deviations and squared deviations:
            <ul>
              <li>\(d_1 = (4.502 - 4.500333) = +0.001667 \implies d_1^2 \approx 0.00000278\)</li>
              <li>\(d_2 = (4.498 - 4.500333) = -0.002333 \implies d_2^2 \approx 0.00000544\)</li>
              <li>\(d_3 = (4.505 - 4.500333) = +0.004667 \implies d_3^2 \approx 0.00002178\)</li>
              <li>\(d_4 = (4.496 - 4.500333) = -0.004333 \implies d_4^2 \approx 0.00001878\)</li>
              <li>\(d_5 = (4.500 - 4.500333) = -0.000333 \implies d_5^2 \approx 0.00000011\)</li>
              <li>\(d_6 = (4.501 - 4.500333) = +0.000667 \implies d_6^2 \approx 0.00000044\)</li>
            </ul>
          </li>
          <li>Sum of squared deviations:
            $$SS \approx 0.00004933 \text{ mm}^2$$
          </li>
          <li>Compute sample variance dividing by \(n - 1 = 6 - 1 = 5\):
            $$s^2 = \frac{0.00004933}{5} \approx 0.00000987 \text{ mm}^2$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> Because the calculated sample variance \(s^2 = 0.00000987 \text{ mm}^2\) is strictly below the maximum threshold of \(0.000015 \text{ mm}^2\), the manufacturing batch passes quality inspection.</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 3: Clinical Laboratory Automated Immunoassay Precision</h3>
        <p><strong>Scenario:</strong> A clinical pathology laboratory validates a new automated chemiluminescence immunoassay analyzer for serum troponin-T measurements (ng/L). A reference control serum with known uniform concentration is tested in 8 replicate runs: \(24, 26, 25, 23, 27, 25, 26, 24\). The laboratory manager requires both sample variance and the Coefficient of Variation (CV) to ensure analytical repeatability.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Calculate mean troponin-T level:
            $$\bar{x} = \frac{24 + 26 + 25 + 23 + 27 + 25 + 26 + 24}{8} = \frac{200}{8} = 25.0000 \text{ ng/L}$$
          </li>
          <li>Compute squared deviations from \(25.0\):
            $$\sum (x_i - \bar{x})^2 = (-1)^2 + (1)^2 + (0)^2 + (-2)^2 + (2)^2 + (0)^2 + (1)^2 + (-1)^2$$
            $$SS = 1 + 1 + 0 + 4 + 4 + 0 + 1 + 1 = 12.0000$$
          </li>
          <li>Calculate sample variance with \(n - 1 = 7\):
            $$s^2 = \frac{12.0}{7} \approx 1.7143 \text{ (ng/L)}^2$$
          </li>
          <li>Calculate sample standard deviation:
            $$s = \sqrt{1.7143} \approx 1.3093 \text{ ng/L}$$
          </li>
          <li>Calculate Coefficient of Variation:
            $$CV = \frac{s}{\bar{x}} \times 100\% = \frac{1.3093}{25.0} \times 100\% = 5.2372\%$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The analyzer exhibits a replicate sample variance of \(1.7143 \text{ (ng/L)}^2\) and a Coefficient of Variation of \(5.2372\%\), demonstrating excellent analytical precision within clinical diagnostic guidelines.</p>
      </div>

      <h2>Properties of Mathematical Variance</h2>
      <p>Understanding the algebraic transformations of variance is essential when modeling stochastic systems, propagating experimental uncertainties, or combining multiple independent random variables:</p>
      <ul>
        <li><strong>Additive Invariance:</strong> Adding a constant \(c\) to every data point shifts the mean by \(c\) but does not alter the spread: \(\text{Var}(X + c) = \text{Var}(X)\).</li>
        <li><strong>Multiplicative Scaling:</strong> Multiplying every observation by a constant scalar \(a\) scales the variance quadratically: \(\text{Var}(aX) = a^2 \text{Var}(X)\). For instance, converting measurements from meters to centimeters multiplies the variance by \(100^2 = 10,000\).</li>
        <li><strong>Sum of Independent Variables:</strong> For two independent random variables \(X\) and \(Y\), the variance of their sum or difference equals the sum of their individual variances: \(\text{Var}(X \pm Y) = \text{Var}(X) + \text{Var}(Y)\). Notice that variance adds even when subtracting random variables because uncertainty always accumulates.</li>
        <li><strong>Variance of Correlated Variables:</strong> If \(X\) and \(Y\) are correlated, their covariance \(\text{Cov}(X, Y)\) enters the equation: \(\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X, Y)\).</li>
      </ul>

      <h2>Frequently Asked Questions</h2>
      <div class="faq-item">
        <div class="faq-question">When should I select Sample Variance instead of Population Variance?</div>
        <div class="faq-answer">Select Sample Variance whenever your dataset represents a subset, trial sample, clinical cohort, or experimental batch drawn from a broader real-world population. Use Population Variance only when you have collected data on every single entity in the entire universe of interest (such as a 100% complete census of all employees in a closed private firm, or when evaluating a purely theoretical mathematical distribution).</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Why does Bessel's correction use (n - 1) instead of (n - 2) or another value?</div>
        <div class="faq-answer">The denominator represents the "degrees of freedom." In a sample of n values, you have n independent pieces of information. However, to calculate deviations, you must first calculate the sample mean x-bar. Once the sample mean is fixed, the last deviation is mathematically determined because the sum of deviations around the mean must identically equal zero: \(\sum (x_i - \bar{x}) = 0\). This consumes exactly 1 degree of freedom, leaving n - 1 free variables.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Why can't standard deviation be directly averaged across subgroups?</div>
        <div class="faq-answer">Standard deviations cannot be linearly averaged because square roots are non-linear operators (Jensen's inequality). To combine dispersion across multiple distinct subgroups, you must pool their variances using weighted sums of squares and pooled degrees of freedom, and only take the square root at the final step.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">How does variance differ from Mean Absolute Deviation (MAD)?</div>
        <div class="faq-answer">Variance squares each deviation \((x_i - \bar{x})^2\), which heavily penalizes large outliers and makes variance mathematically differentiable for calculus, optimization algorithms, and ordinary least squares (OLS) regression. Mean Absolute Deviation takes the absolute value \(|x_i - \bar{x}|\), which gives equal proportional weight to all deviations and is more robust against extreme anomalies, but is non-differentiable at zero.</div>
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
    function parseData(text) {
      if (!text) return [];
      var parts = text.split(/[\s,;\n\r\t]+/);
      var nums = [];
      for (var i = 0; i < parts.length; i++) {
        var str = parts[i].trim();
        if (str !== "") {
          var val = parseFloat(str);
          if (!isNaN(val)) nums.push(val);
        }
      }
      return nums;
    }

    function calculateVariance() {
      var raw = document.getElementById('dataset-input').value;
      var data = parseData(raw);
      var type = document.getElementById('var-type').value;
      var prec = parseInt(document.getElementById('precision-select').value, 10) || 4;

      if (data.length === 0) {
        showError("Please enter at least one valid numerical observation.");
        return;
      }

      if (type === 'sample' && data.length < 2) {
        showError("Sample variance requires at least 2 observations for (n - 1) degrees of freedom.");
        return;
      }

      var n = data.length;
      var sum = 0;
      for (var i = 0; i < n; i++) sum += data[i];
      var mean = sum / n;

      var ss = 0;
      var rowsHtml = "";
      for (var i = 0; i < n; i++) {
        var dev = data[i] - mean;
        var devSq = dev * dev;
        ss += devSq;
        rowsHtml += "<tr>" +
                    "<td>" + (i + 1) + "</td>" +
                    "<td>" + data[i].toFixed(prec) + "</td>" +
                    "<td>" + (dev >= 0 ? "+" : "") + dev.toFixed(prec) + "</td>" +
                    "<td>" + devSq.toFixed(prec) + "</td>" +
                    "</tr>";
      }

      var denom = (type === 'sample') ? (n - 1) : n;
      var variance = ss / denom;
      var sd = Math.sqrt(variance);
      var se = (type === 'sample') ? (sd / Math.sqrt(n)) : (sd / Math.sqrt(n));
      var cv = (mean !== 0) ? (sd / Math.abs(mean) * 100) : 0;

      var varLabel = (type === 'sample') ? "Sample Variance (s²)" : "Population Variance (σ²)";
      var denomLabel = (type === 'sample') ? "(n - 1) = " + denom : "N = " + denom;

      document.getElementById('res-var').innerText = varLabel + ": " + variance.toFixed(prec);
      document.getElementById('res-sd').innerText = sd.toFixed(prec);
      document.getElementById('res-mean').innerText = mean.toFixed(prec);
      document.getElementById('res-count').innerText = n.toString();
      document.getElementById('res-ss').innerText = ss.toFixed(prec);
      document.getElementById('res-sum').innerText = sum.toFixed(prec);
      document.getElementById('res-se').innerText = se.toFixed(prec);
      document.getElementById('res-cv').innerText = cv.toFixed(prec) + "%";

      var steps = "Dataset Size: " + n + " values\n" +
                  "1. Arithmetic Mean: Sum / " + n + " = " + sum.toFixed(prec) + " / " + n + " = " + mean.toFixed(prec) + "\n" +
                  "2. Sum of Squared Deviations (SS): " + ss.toFixed(prec) + "\n" +
                  "3. Denominator (" + denomLabel + ")\n" +
                  "4. Variance Formula: " + (type === 'sample' ? "s² = SS / (n - 1)" : "σ² = SS / N") + "\n" +
                  "   Variance = " + ss.toFixed(prec) + " / " + denom + " = " + variance.toFixed(prec) + "\n" +
                  "5. Standard Deviation = sqrt(Variance) = sqrt(" + variance.toFixed(prec) + ") = " + sd.toFixed(prec);

      document.getElementById('res-steps').innerText = steps;
      document.getElementById('res-table-body').innerHTML = rowsHtml;
    }

    function showError(msg) {
      document.getElementById('res-var').innerText = "Error";
      document.getElementById('res-sd').innerText = "N/A";
      document.getElementById('res-mean').innerText = "N/A";
      document.getElementById('res-count').innerText = "0";
      document.getElementById('res-ss').innerText = "N/A";
      document.getElementById('res-sum').innerText = "N/A";
      document.getElementById('res-se').innerText = "N/A";
      document.getElementById('res-cv').innerText = "N/A";
      document.getElementById('res-steps').innerText = "Error: " + msg;
      document.getElementById('res-table-body').innerHTML = "<tr><td colspan='4' style='text-align:center;'>No valid data</td></tr>";
    }

    function resetVariance() {
      document.getElementById('dataset-input').value = "14, 22, 19, 25, 30, 21, 28";
      document.getElementById('var-type').value = "sample";
      document.getElementById('precision-select').value = "4";
      calculateVariance();
    }

    window.addEventListener('DOMContentLoaded', function() {
      calculateVariance();
    });
  </script>
</body>
</html>
"""

def main():
    p7 = os.path.join(BASE_DIR, "triangle-area-calculator.html")
    with open(p7, "w", encoding="utf-8") as f:
        f.write(HTML_TRIANGLE)
    print("Generated:", p7)

    p8 = os.path.join(BASE_DIR, "variance-calculator.html")
    with open(p8, "w", encoding="utf-8") as f:
        f.write(HTML_VARIANCE)
    print("Generated:", p8)

if __name__ == "__main__":
    main()
