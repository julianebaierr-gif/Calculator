# -*- coding: utf-8 -*-
"""
Generator for Batch 31 - Part 1:
1. distance-calculator.html
2. midrange-calculator.html
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 1. distance-calculator.html
HTML_DISTANCE = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Distance Calculator - 2D &amp; 3D Euclidean, Manhattan &amp; Coordinate Solver</title>
  <meta name="description" content="Calculate 2D and 3D Euclidean distance, Manhattan distance, Chebyshev distance, vector displacement, line slope, and midpoint with step-by-step math.">
  <link rel="canonical" href="https://calchub.org/distance-calculator.html">
  <meta property="og:title" content="Distance Calculator - 2D &amp; 3D Coordinate Geometry Solver">
  <meta property="og:description" content="Free multi-metric distance calculator. Compute Euclidean distance in 2D and 3D space, Manhattan distance, Chebyshev metric, displacement, slope, and midpoints.">
  <meta property="og:url" content="https://calchub.org/distance-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Distance Calculator - 2D/3D Euclidean &amp; Coordinate Geometry">
  <meta name="twitter:description" content="Calculate Euclidean distance, Manhattan distance, 3D space diagonal, midpoint, and vector displacement with complete step-by-step coordinate derivations.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Distance Calculator",
    "url": "https://calchub.org/distance-calculator.html",
    "description": "Calculates 2D and 3D Euclidean distance, Manhattan distance, Chebyshev distance, displacement vector, slope, and midpoint between coordinate points.",
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
        "name": "What is the Euclidean distance formula in 2D and 3D space?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "In 2D Cartesian space, Euclidean distance between (x1, y1) and (x2, y2) is d = sqrt((x2 - x1)^2 + (y2 - y1)^2). In 3D space with points (x1, y1, z1) and (x2, y2, z2), it expands via the 3D Pythagorean theorem to d = sqrt((x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2)."
        }
      },
      {
        "@type": "Question",
        "name": "How does Manhattan distance differ from Euclidean distance?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Euclidean distance measures the direct straight-line distance (as the crow flies) through the L2 norm. Manhattan distance (L1 norm or taxicab metric) measures distance along strictly orthogonal grid axes: d_M = |x2 - x1| + |y2 - y1| (+ |z2 - z1| in 3D), representing grid navigation where diagonal travel is prohibited."
        }
      },
      {
        "@type": "Question",
        "name": "What is the Chebyshev distance and where is it applied?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Chebyshev distance (L-infinity norm) is the maximum coordinate difference along any single axis: d_C = max(|x2 - x1|, |y2 - y1|, |z2 - z1|). It models the number of moves a King makes on a chessboard or crane motion where all orthogonal axes move simultaneously at identical maximum velocity."
        }
      },
      {
        "@type": "Question",
        "name": "Can Euclidean distance between two real coordinate points ever be negative?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No. In real metric spaces, Euclidean distance satisfies the non-negativity axiom (d(P, Q) >= 0) and the identity of indiscernibles (d(P, Q) = 0 if and only if P = Q). Because distance is the square root of a sum of squared real numbers, it is always non-negative."
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
      <div class="calc-icon" aria-hidden="true">&#10138;</div>
      <h1>Distance Calculator (2D &amp; 3D Coordinates)</h1>
      <p class="calc-description">Compute Euclidean distance, Manhattan taxicab distance, Chebyshev maximum metric, 3D space diagonal, displacement vector, slope, and midpoint with step-by-step derivations.</p>
    </div>

    <div class="calculator-body">
      <div class="input-group">
        <label for="dim-select">Coordinate Space Dimensionality</label>
        <select id="dim-select" class="form-control" onchange="switchDimension()">
          <option value="2d" selected>2D Plane Space (x, y)</option>
          <option value="3d">3D Volume Space (x, y, z)</option>
        </select>
      </div>

      <div class="input-grid">
        <div class="input-group">
          <label for="p1-x">Point 1: x₁</label>
          <input type="number" id="p1-x" class="form-control" value="2" step="any">
        </div>
        <div class="input-group">
          <label for="p1-y">Point 1: y₁</label>
          <input type="number" id="p1-y" class="form-control" value="3" step="any">
        </div>
        <div class="input-group dim-3d-group" id="group-p1-z" style="display:none;">
          <label for="p1-z">Point 1: z₁</label>
          <input type="number" id="p1-z" class="form-control" value="1" step="any">
        </div>
      </div>

      <div class="input-grid">
        <div class="input-group">
          <label for="p2-x">Point 2: x₂</label>
          <input type="number" id="p2-x" class="form-control" value="7" step="any">
        </div>
        <div class="input-group">
          <label for="p2-y">Point 2: y₂</label>
          <input type="number" id="p2-y" class="form-control" value="15" step="any">
        </div>
        <div class="input-group dim-3d-group" id="group-p2-z" style="display:none;">
          <label for="p2-z">Point 2: z₂</label>
          <input type="number" id="p2-z" class="form-control" value="9" step="any">
        </div>
      </div>

      <div class="input-group">
        <label for="precision-select">Decimal Precision</label>
        <select id="precision-select" class="form-control" onchange="calculateDistance()">
          <option value="2">2 decimal places</option>
          <option value="4" selected>4 decimal places</option>
          <option value="6">6 decimal places</option>
        </select>
      </div>

      <div style="display:flex; gap:12px; margin-top:16px;">
        <button id="calc-btn" class="btn-primary" onclick="calculateDistance()" style="flex:1;">Calculate Distance</button>
        <button id="reset-btn" class="btn-secondary" onclick="resetDistance()">Reset</button>
      </div>

      <div id="result-box" class="result-box" style="margin-top:24px;">
        <h2 class="result-title">Metric Distance &amp; Spatial Properties</h2>
        <div class="result-highlight" style="font-size:1.8rem; font-weight:700; color:var(--primary); margin-bottom:16px;" id="res-euclidean">
          Euclidean Distance: 13.0000 units
        </div>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:16px;">
          <div><span class="res-label">Manhattan Distance (L₁):</span> <strong class="res-val" id="res-manhattan">17.0000</strong></div>
          <div><span class="res-label">Chebyshev Distance (L_&infin;):</span> <strong class="res-val" id="res-chebyshev">12.0000</strong></div>
          <div><span class="res-label">Displacement Vector:</span> <strong class="res-val" id="res-vector">&lang;5, 12&rang;</strong></div>
          <div><span class="res-label">Midpoint Coordinates:</span> <strong class="res-val" id="res-midpoint">(4.5, 9.0)</strong></div>
          <div id="box-slope"><span class="res-label">2D Slope (m):</span> <strong class="res-val" id="res-slope">2.4000 (67.38&deg;)</strong></div>
          <div><span class="res-label">Squared Distance (d&sup2;):</span> <strong class="res-val" id="res-dsq">169.0000</strong></div>
        </div>

        <h3 style="margin-top:20px; font-size:1.1rem; color:var(--text-dark);">Mathematical Step-by-Step Derivation</h3>
        <div id="res-steps" style="background:var(--bg-subtle, #f8fafc); padding:16px; border-radius:8px; font-family:monospace; font-size:0.95rem; white-space:pre-wrap; border:1px solid var(--border-color, #e2e8f0);"></div>
      </div>
    </div>

    <article class="article-body">
      <h2>Comprehensive Theoretical &amp; Engineering Guide to Distance Metrics</h2>
      <p>Distance is the fundamental scalar quantity in analytic geometry, mechanics, physical geodesy, and computer vision that measures the separation between two distinct points in coordinate space. In mathematical analysis, a function \(d(P, Q)\) is formally classified as a distance metric on a set if and only if it satisfies four rigorous metric axioms:</p>
      <ol>
        <li><strong>Non-negativity:</strong> \(d(P, Q) \ge 0\) for all points \(P\) and \(Q\).</li>
        <li><strong>Identity of Indiscernibles:</strong> \(d(P, Q) = 0 \iff P = Q\).</li>
        <li><strong>Symmetry:</strong> \(d(P, Q) = d(Q, P)\).</li>
        <li><strong>Triangle Inequality:</strong> \(d(P, R) \le d(P, Q) + d(Q, R)\) for any intermediate point \(Q\).</li>
      </ol>
      <p>While the straight-line Euclidean distance remains the standard metric of physical space, modern engineering and computational sciences frequently require non-Euclidean norms such as the Manhattan metric for urban transportation networks, the Chebyshev metric for robotic gantry routing, and the Minkowski generalized \(L_p\) norm for high-dimensional feature spaces in machine learning clustering algorithms.</p>

      <h2>Mathematical Formulations: 2D, 3D &amp; Non-Euclidean Metrics</h2>
      <p>Depending on the degrees of freedom and spatial constraints of an engineering system, different coordinate formulas apply.</p>

      <h3>1. 2D Euclidean Distance (Planar \(L_2\) Norm)</h3>
      <p>For any two points \(P_1 = (x_1, y_1)\) and \(P_2 = (x_2, y_2)\) on a two-dimensional Cartesian plane, Euclidean distance derives directly from the <a href="pythagorean-theorem-calculator.html">Pythagorean Theorem</a> by constructing a right-angled triangle with perpendicular legs \(\Delta x = x_2 - x_1\) and \(\Delta y = y_2 - y_1\):</p>
      $$d = \sqrt{(\Delta x)^2 + (\Delta y)^2} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
      <p>The squared distance \(d^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2\) is often utilized in high-performance computer graphics, collision detection, and spatial database indexing to avoid the computational cost of evaluating radical square roots. You can compute explicit radical evaluations using our <a href="square-root-calculator.html">Square Root Calculator</a>.</p>

      <h3>2. 3D Euclidean Distance (Spatial \(L_2\) Space Diagonal)</h3>
      <p>In three-dimensional space, points possess altitude or depth coordinates: \(P_1 = (x_1, y_1, z_1)\) and \(P_2 = (x_2, y_2, z_2)\). Extending the Pythagorean theorem across the orthogonal base plane and the vertical elevation axis yields the 3D space diagonal:</p>
      $$d = \sqrt{(\Delta x)^2 + (\Delta y)^2 + (\Delta z)^2} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$
      <p>This formulation underpins aerospace flight trajectory calculations, orbital mechanics, structural truss member sizing, and 3D computer-aided design (CAD) spatial clearance verifications.</p>

      <h3>3. Manhattan Distance (Taxicab Metric / \(L_1\) Norm)</h3>
      <p>In city navigation where physical streets form a rigid rectangular grid, diagonal travel through buildings is prohibited. The Manhattan distance \(d_M\), also known as the \(L_1\) norm or taxicab metric, computes the sum of the absolute differences along each orthogonal axis:</p>
      $$\text{In 2D: } d_M = |\Delta x| + |\Delta y| = |x_2 - x_1| + |y_2 - y_1|$$
      $$\text{In 3D: } d_M = |\Delta x| + |\Delta y| + |\Delta z| = |x_2 - x_1| + |y_2 - y_1| + |z_2 - z_1|$$
      <p>Manhattan distance is extensively applied in integrated circuit (IC) routing algorithms, warehouse automated guided vehicle (AGV) pathfinding, and compressed sensing (LASSO \(L_1\) regularization).</p>

      <h3>4. Chebyshev Distance (Chessboard Metric / \(L_\infty\) Norm)</h3>
      <p>Named after Pafnuty Chebyshev, the Chebyshev distance \(d_C\) measures the greatest absolute difference between coordinate components along any single dimension:</p>
      $$d_C = \max\left( |\Delta x|, |\Delta y|, |\Delta z| \right)$$
      <p>On an \(8 \times 8\) chessboard, the King can move one square in any direction (orthogonal or diagonal). The minimum number of moves required for a King to travel between \((x_1, y_1)\) and \((x_2, y_2)\) exactly equals the Chebyshev distance. In industrial gantry robotics where independent stepper motors drive the X, Y, and Z axes simultaneously at identical maximum speeds, the cycle time to complete a motion is governed by the Chebyshev metric.</p>

      <h3>5. Midpoint and Direction Vector Relations</h3>
      <p>Connecting two points in space defines both a displacement vector and an exact central midpoint. The midpoint \(M\) bisects the line segment into two equal segments, as computed in our <a href="midpoint-calculator.html">Midpoint Calculator</a>:</p>
      $$\text{Midpoint in 3D: } M = \left( \frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}, \frac{z_1 + z_2}{2} \right)$$
      $$\text{Displacement Vector: } \vec{v} = \langle \Delta x, \Delta y, \Delta z \rangle = \langle x_2 - x_1, y_2 - y_1, z_2 - z_1 \rangle$$
      $$\text{2D Directional Angle: } \theta = \arctan2(\Delta y, \Delta x)$$

      <h2>Distance Metrics Comparison &amp; Invariants Table</h2>
      <p>The following technical reference matrix compares the mathematical properties, metric balls, and practical applications of standard coordinate distance norms:</p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Distance Metric</th>
            <th>Mathematical Formula</th>
            <th>Metric Space Norm</th>
            <th>Unit Ball Geometry</th>
            <th>Primary Engineering Application</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Euclidean Distance</td>
            <td>\(\sqrt{\sum (x_i - y_i)^2}\)</td>
            <td>\(L_2\) Norm</td>
            <td>Circle / Sphere</td>
            <td>Straight-line physics, ballistics, radar, surveying, CAD</td>
          </tr>
          <tr>
            <td>Manhattan Distance</td>
            <td>\(\sum |x_i - y_i|\)</td>
            <td>\(L_1\) Norm</td>
            <td>Diamond (rotated square) / Octahedron</td>
            <td>City street grids, PCB wire routing, LASSO regularization</td>
          </tr>
          <tr>
            <td>Chebyshev Distance</td>
            <td>\(\max_i |x_i - y_i|\)</td>
            <td>\(L_\infty\) Norm</td>
            <td>Square / Cube</td>
            <td>CNC gantry routers, automated warehousing, King chess moves</td>
          </tr>
          <tr>
            <td>Minkowski Distance</td>
            <td>\(\left(\sum |x_i - y_i|^p\right)^{1/p}\)</td>
            <td>\(L_p\) Norm</td>
            <td>Superellipse / Lam&eacute; curves</td>
            <td>Machine learning clustering, k-NN classification, data mining</td>
          </tr>
          <tr>
            <td>Squared Euclidean</td>
            <td>\(\sum (x_i - y_i)^2\)</td>
            <td>Quadratic Form</td>
            <td>Paraboloid contour</td>
            <td>K-means clustering, collision detection (avoids square roots)</td>
          </tr>
        </tbody>
      </table>

      <h2>Real-World Engineering, Surveying &amp; Robotics Case Studies</h2>
      <p>The following practical examples demonstrate how these distance formulations solve real-world problems in civil engineering, industrial robotics, and urban logistics.</p>

      <div class="worked-example-card">
        <h3>Case Study 1: Civil Engineering Land Surveying &amp; Elevation Clearance (3D Space)</h3>
        <p><strong>Scenario:</strong> A civil surveyor establishes two benchmark survey pins on an inclined hillside for a high-voltage transmission tower. Pin A is recorded at local coordinates \((120.0 \text{ m}, 250.0 \text{ m}, 45.0 \text{ m})\), and Pin B is recorded at \((360.0 \text{ m}, 430.0 \text{ m}, 95.0 \text{ m})\). The project engineer requires the true spatial 3D cable span distance, the flat plan-view 2D distance, and the terrain elevation slope.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Calculate coordinate differentials:
            $$\Delta x = 360.0 - 120.0 = 240.0 \text{ m}$$
            $$\Delta y = 430.0 - 250.0 = 180.0 \text{ m}$$
            $$\Delta z = 95.0 - 45.0 = 50.0 \text{ m}$$
          </li>
          <li>Compute horizontal 2D plan-view distance:
            $$d_{2D} = \sqrt{240.0^2 + 180.0^2} = \sqrt{57600 + 32400} = \sqrt{90000} = 300.0000 \text{ m}$$
          </li>
          <li>Compute spatial 3D Euclidean distance:
            $$d_{3D} = \sqrt{d_{2D}^2 + \Delta z^2} = \sqrt{300.0^2 + 50.0^2} = \sqrt{90000 + 2500} = \sqrt{92500} \approx 304.1381 \text{ m}$$
          </li>
          <li>Compute terrain slope percentage:
            $$\text{Slope} = \frac{\Delta z}{d_{2D}} \times 100\% = \frac{50.0}{300.0} \times 100\% \approx 16.6667\%$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The true 3D spatial span length is \(304.1381 \text{ m}\), with a horizontal plan-view distance of \(300.0000 \text{ m}\) and a hillside grade of \(16.67\%\).</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Industrial Gantry CNC Router Toolpath (Chebyshev vs. Euclidean)</h3>
        <p><strong>Scenario:</strong> A 3-axis CNC milling machine operates independent servomotors for the X, Y, and Z axes. Each axis has a rapid transit velocity limit of \(200 \text{ mm/s}\). The toolhead must move from rapid position \(P_1 = (50.0, 40.0, 10.0 \text{ mm})\) to cutting start position \(P_2 = (290.0, 160.0, 70.0 \text{ mm})\). The controls engineer must determine the physical Euclidean travel distance and the actual cycle transit time.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Calculate axis displacements:
            $$|\Delta x| = |290.0 - 50.0| = 240.0 \text{ mm}$$
            $$|\Delta y| = |160.0 - 40.0| = 120.0 \text{ mm}$$
            $$|\Delta z| = |70.0 - 10.0| = 60.0 \text{ mm}$$
          </li>
          <li>Calculate physical 3D Euclidean straight-line distance:
            $$d = \sqrt{240.0^2 + 120.0^2 + 60.0^2} = \sqrt{57600 + 14400 + 3600} = \sqrt{75600} \approx 274.9545 \text{ mm}$$
          </li>
          <li>Calculate Chebyshev distance governing simultaneous multi-axis transit:
            $$d_C = \max(240.0, 120.0, 60.0) = 240.0000 \text{ mm}$$
          </li>
          <li>Calculate minimum motion cycle time:
            $$t = \frac{d_C}{v_{\max}} = \frac{240.0 \text{ mm}}{200.0 \text{ mm/s}} = 1.2000 \text{ seconds}$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> While the straight-line physical displacement is \(274.9545 \text{ mm}\), the CNC machine cycle time is strictly governed by the Chebyshev distance of \(240.0000 \text{ mm}\), completing transit in exactly \(1.2000\) seconds.</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 3: Urban Automated Delivery Fleet Routing (Manhattan vs. Euclidean)</h3>
        <p><strong>Scenario:</strong> An autonomous delivery robot navigates a downtown city grid with avenues aligned on a Cartesian coordinate plane (coordinates in blocks, where 1 block = 100 meters). The distribution hub is at \((12, 8)\), and the delivery destination is at \((27, 28)\). The dispatch system must calculate the straight-line line-of-sight distance (for drone delivery) versus the ground wheel travel distance (for sidewalk rover delivery).</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Compute block differentials:
            $$\Delta x = 27 - 12 = 15 \text{ blocks}$$
            $$\Delta y = 28 - 8 = 20 \text{ blocks}$$
          </li>
          <li>Calculate aerial drone distance (Euclidean metric):
            $$d_{\text{drone}} = \sqrt{15^2 + 20^2} = \sqrt{225 + 400} = \sqrt{625} = 25.0 \text{ blocks} = 2,500.0 \text{ meters}$$
          </li>
          <li>Calculate ground rover distance (Manhattan metric):
            $$d_{\text{rover}} = |\Delta x| + |\Delta y| = 15 + 20 = 35.0 \text{ blocks} = 3,500.0 \text{ meters}$$
          </li>
          <li>Calculate grid detour circuity factor:
            $$\text{Circuity Factor} = \frac{d_{\text{rover}}}{d_{\text{drone}}} = \frac{35.0}{25.0} = 1.4000$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The aerial line-of-sight distance is \(2,500.0 \text{ m}\), whereas the sidewalk wheel distance is \(3,500.0 \text{ m}\), representing a \(40\%\) routing detour over straight-line flight.</p>
      </div>

      <h2>Frequently Asked Questions</h2>
      <div class="faq-item">
        <div class="faq-question">What is the difference between distance and displacement?</div>
        <div class="faq-answer">Distance is a scalar quantity representing the absolute spatial magnitude of separation between two locations (\(d \ge 0\)), independent of heading. Displacement is a vector quantity that encompasses both magnitude and directional orientation (\(\vec{v} = \langle \Delta x, \Delta y, \Delta z \rangle\)), indicating the directed path from the initial point to the terminal point.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Why does the 3D distance formula have three squared terms inside the radical?</div>
        <div class="faq-answer">The 3D distance formula applies the Pythagorean theorem twice in succession. First, it computes the hypotenuse across the horizontal base plane: \(d_{xy}^2 = \Delta x^2 + \Delta y^2\). Second, it treats this planar diagonal as the base of a vertical right triangle with altitude \(\Delta z\): \(d_{3D}^2 = d_{xy}^2 + \Delta z^2 = \Delta x^2 + \Delta y^2 + \Delta z^2\). Taking the square root yields the complete 3D formula.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">When should I compute Manhattan distance instead of Euclidean distance?</div>
        <div class="faq-answer">Use Manhattan distance whenever motion is physically constrained to orthogonal grid axes—such as vehicular traffic navigating city street grids, warehouse Automated Guided Vehicles (AGVs) following aisle tape, or integrated circuit trace routing on printed circuit boards (PCBs). In these scenarios, diagonal Euclidean shortcuts cannot physically be traversed.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">How does Chebyshev distance relate to robotic cycle times?</div>
        <div class="faq-answer">In multi-axis motion controllers where individual servo actuators for the X, Y, and Z axes can accelerate and travel concurrently at equal maximum speeds, all axes operate in parallel. The total travel duration is limited by the single axis that must traverse the greatest distance: \(t = \max(|\Delta x|, |\Delta y|, |\Delta z|) / v_{\max}\). This maximum coordinate differential is the Chebyshev distance.</div>
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
    function switchDimension() {
      var dim = document.getElementById('dim-select').value;
      var z1 = document.getElementById('group-p1-z');
      var z2 = document.getElementById('group-p2-z');
      var slopeBox = document.getElementById('box-slope');

      if (dim === '3d') {
        z1.style.display = 'block';
        z2.style.display = 'block';
        slopeBox.style.display = 'none';
      } else {
        z1.style.display = 'none';
        z2.style.display = 'none';
        slopeBox.style.display = 'block';
      }
      calculateDistance();
    }

    function calculateDistance() {
      var dim = document.getElementById('dim-select').value;
      var prec = parseInt(document.getElementById('precision-select').value, 10) || 4;

      var x1 = parseFloat(document.getElementById('p1-x').value);
      var y1 = parseFloat(document.getElementById('p1-y').value);
      var x2 = parseFloat(document.getElementById('p2-x').value);
      var y2 = parseFloat(document.getElementById('p2-y').value);

      if ([x1, y1, x2, y2].some(isNaN)) {
        showError("Please enter valid real numbers for all coordinate inputs.");
        return;
      }

      var dx = x2 - x1;
      var dy = y2 - y1;
      var dz = 0;
      var z1 = 0, z2 = 0;

      if (dim === '3d') {
        z1 = parseFloat(document.getElementById('p1-z').value);
        z2 = parseFloat(document.getElementById('p2-z').value);
        if (isNaN(z1) || isNaN(z2)) {
          showError("Please enter valid real numbers for z-coordinates in 3D mode.");
          return;
        }
        dz = z2 - z1;
      }

      var dsq = (dim === '3d') ? (dx * dx + dy * dy + dz * dz) : (dx * dx + dy * dy);
      var euclidean = Math.sqrt(dsq);
      var manhattan = (dim === '3d') ? (Math.abs(dx) + Math.abs(dy) + Math.abs(dz)) : (Math.abs(dx) + Math.abs(dy));
      var chebyshev = (dim === '3d') ? Math.max(Math.abs(dx), Math.abs(dy), Math.abs(dz)) : Math.max(Math.abs(dx), Math.abs(dy));

      var mx = (x1 + x2) / 2;
      var my = (y1 + y2) / 2;
      var mz = (z1 + z2) / 2;

      document.getElementById('res-euclidean').innerText = "Euclidean Distance: " + euclidean.toFixed(prec) + " units";
      document.getElementById('res-manhattan').innerText = manhattan.toFixed(prec);
      document.getElementById('res-chebyshev').innerText = chebyshev.toFixed(prec);
      document.getElementById('res-dsq').innerText = dsq.toFixed(prec);

      if (dim === '3d') {
        document.getElementById('res-vector').innerHTML = "&lang;" + dx.toFixed(prec) + ", " + dy.toFixed(prec) + ", " + dz.toFixed(prec) + "&rang;";
        document.getElementById('res-midpoint').innerText = "(" + mx.toFixed(prec) + ", " + my.toFixed(prec) + ", " + mz.toFixed(prec) + ")";
      } else {
        document.getElementById('res-vector').innerHTML = "&lang;" + dx.toFixed(prec) + ", " + dy.toFixed(prec) + "&rang;";
        document.getElementById('res-midpoint').innerText = "(" + mx.toFixed(prec) + ", " + my.toFixed(prec) + ")";
        
        var slopeText = "Undefined (Vertical)";
        if (Math.abs(dx) > 1e-12) {
          var slope = dy / dx;
          var angleDeg = Math.atan2(dy, dx) * 180 / Math.PI;
          slopeText = slope.toFixed(prec) + " (" + angleDeg.toFixed(2) + "°)";
        }
        document.getElementById('res-slope').innerText = slopeText;
      }

      var steps = "";
      if (dim === '3d') {
        steps = "Mode: 3D Spatial Cartesian Coordinates\n" +
                "Point 1: (" + x1 + ", " + y1 + ", " + z1 + ")\n" +
                "Point 2: (" + x2 + ", " + y2 + ", " + z2 + ")\n\n" +
                "1. Differentials:\n" +
                "   Δx = x₂ - x₁ = " + x2 + " - " + x1 + " = " + dx.toFixed(prec) + "\n" +
                "   Δy = y₂ - y₁ = " + y2 + " - " + y1 + " = " + dy.toFixed(prec) + "\n" +
                "   Δz = z₂ - z₁ = " + z2 + " - " + z1 + " = " + dz.toFixed(prec) + "\n\n" +
                "2. Euclidean Distance (L₂ norm):\n" +
                "   d = sqrt((Δx)² + (Δy)² + (Δz)²)\n" +
                "   d = sqrt((" + dx.toFixed(prec) + ")² + (" + dy.toFixed(prec) + ")² + (" + dz.toFixed(prec) + ")²)\n" +
                "   d = sqrt(" + (dx*dx).toFixed(prec) + " + " + (dy*dy).toFixed(prec) + " + " + (dz*dz).toFixed(prec) + ") = sqrt(" + dsq.toFixed(prec) + ")\n" +
                "   d = " + euclidean.toFixed(prec) + " units\n\n" +
                "3. Manhattan Distance (L₁ norm):\n" +
                "   d_M = |Δx| + |Δy| + |Δz| = " + Math.abs(dx).toFixed(prec) + " + " + Math.abs(dy).toFixed(prec) + " + " + Math.abs(dz).toFixed(prec) + " = " + manhattan.toFixed(prec) + "\n\n" +
                "4. Chebyshev Distance (L_∞ norm):\n" +
                "   d_C = max(|Δx|, |Δy|, |Δz|) = " + chebyshev.toFixed(prec) + "\n\n" +
                "5. Midpoint Coordinates:\n" +
                "   M = ((x₁+x₂)/2, (y₁+y₂)/2, (z₁+z₂)/2) = (" + mx.toFixed(prec) + ", " + my.toFixed(prec) + ", " + mz.toFixed(prec) + ")";
      } else {
        steps = "Mode: 2D Planar Cartesian Coordinates\n" +
                "Point 1: (" + x1 + ", " + y1 + ")\n" +
                "Point 2: (" + x2 + ", " + y2 + ")\n\n" +
                "1. Differentials:\n" +
                "   Δx = x₂ - x₁ = " + x2 + " - " + x1 + " = " + dx.toFixed(prec) + "\n" +
                "   Δy = y₂ - y₁ = " + y2 + " - " + y1 + " = " + dy.toFixed(prec) + "\n\n" +
                "2. Euclidean Distance (L₂ norm):\n" +
                "   d = sqrt((Δx)² + (Δy)²)\n" +
                "   d = sqrt((" + dx.toFixed(prec) + ")² + (" + dy.toFixed(prec) + ")²)\n" +
                "   d = sqrt(" + (dx*dx).toFixed(prec) + " + " + (dy*dy).toFixed(prec) + ") = sqrt(" + dsq.toFixed(prec) + ")\n" +
                "   d = " + euclidean.toFixed(prec) + " units\n\n" +
                "3. Manhattan Distance (L₁ norm):\n" +
                "   d_M = |Δx| + |Δy| = " + Math.abs(dx).toFixed(prec) + " + " + Math.abs(dy).toFixed(prec) + " = " + manhattan.toFixed(prec) + "\n\n" +
                "4. Chebyshev Distance (L_∞ norm):\n" +
                "   d_C = max(|Δx|, |Δy|) = " + chebyshev.toFixed(prec) + "\n\n" +
                "5. Midpoint: M = (" + mx.toFixed(prec) + ", " + my.toFixed(prec) + ")";
      }

      document.getElementById('res-steps').innerText = steps;
    }

    function showError(msg) {
      document.getElementById('res-euclidean').innerText = "Error";
      document.getElementById('res-manhattan').innerText = "N/A";
      document.getElementById('res-chebyshev').innerText = "N/A";
      document.getElementById('res-vector').innerText = "N/A";
      document.getElementById('res-midpoint').innerText = "N/A";
      document.getElementById('res-slope').innerText = "N/A";
      document.getElementById('res-dsq').innerText = "N/A";
      document.getElementById('res-steps').innerText = "Error: " + msg;
    }

    function resetDistance() {
      document.getElementById('dim-select').value = '2d';
      document.getElementById('p1-x').value = '2';
      document.getElementById('p1-y').value = '3';
      document.getElementById('p1-z').value = '1';
      document.getElementById('p2-x').value = '7';
      document.getElementById('p2-y').value = '15';
      document.getElementById('p2-z').value = '9';
      document.getElementById('precision-select').value = '4';
      switchDimension();
    }

    window.addEventListener('DOMContentLoaded', function() {
      calculateDistance();
    });
  </script>
</body>
</html>
"""

# 2. midrange-calculator.html
HTML_MIDRANGE = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Midrange Calculator - Statistical Measure of Center &amp; Range Sizer</title>
  <meta name="description" content="Calculate the midrange of any statistical dataset with step-by-step arithmetic. Compare midrange vs mean, median, midhinge, trimean, and total range.">
  <link rel="canonical" href="https://calchub.org/midrange-calculator.html">
  <meta property="og:title" content="Midrange Calculator - Center of Range &amp; Dispersion Solver">
  <meta property="og:description" content="Free statistical midrange calculator. Compute midrange (L + S)/2, data range (L - S), arithmetic mean, median, midhinge, and outlier sensitivity.">
  <meta property="og:url" content="https://calchub.org/midrange-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Midrange Calculator - Center of Data Range Solver">
  <meta name="twitter:description" content="Calculate the statistical midrange, minimum, maximum, range, mean, and midhinge for any dataset with complete step-by-step mathematical breakdowns.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Midrange Calculator",
    "url": "https://calchub.org/midrange-calculator.html",
    "description": "Calculates the statistical midrange (L + S) / 2, range, minimum, maximum, mean, median, midhinge, and trimean for any numerical dataset.",
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
        "name": "What is the midrange in statistics and what is its formula?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The midrange is a measure of central tendency representing the exact arithmetic midpoint between the highest (maximum, L) and lowest (minimum, S) values in a dataset. Its mathematical formula is Midrange = (Maximum + Minimum) / 2 or (L + S) / 2."
        }
      },
      {
        "@type": "Question",
        "name": "How does the midrange differ from the mean and median?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The arithmetic mean uses every single observation in the dataset by dividing their sum by n. The median is the physical middle observation in a sorted list and is robust against extreme outliers. The midrange depends solely on the two extreme values (min and max); it ignores all intermediate data points and has a breakdown point of 0%, making it highly sensitive to outliers."
        }
      },
      {
        "@type": "Question",
        "name": "When is the midrange a useful or optimal statistical estimator?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The midrange is the uniformly minimum-variance unbiased estimator (UMVUE) for the center of a continuous uniform distribution U(a, b). It is also widely used in daily meteorological temperature reporting (averaging daily high and low) and rapid industrial quality control checks where quick range appraisals are required without full data tallying."
        }
      },
      {
        "@type": "Question",
        "name": "What is the difference between midrange and midhinge?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The midrange averages the extreme values: (Min + Max) / 2. The midhinge averages the first and third quartiles: (Q1 + Q3) / 2. Because the midhinge relies on quartiles rather than the extreme minimum and maximum, it is substantially more resistant to statistical outliers while retaining the symmetry of range-based centering."
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
      <div class="calc-icon" aria-hidden="true">&#9878;</div>
      <h1>Midrange Calculator</h1>
      <p class="calc-description">Calculate the statistical midrange, minimum, maximum, total range, arithmetic mean, median, midhinge, and trimean for any numerical dataset.</p>
    </div>

    <div class="calculator-body">
      <div class="input-group">
        <label for="dataset-input">Dataset Observations</label>
        <textarea id="dataset-input" class="form-control" rows="4" placeholder="Enter numbers separated by commas, spaces, or newlines, e.g. 18, 24, 32, 15, 45, 29, 38">18, 24, 32, 15, 45, 29, 38</textarea>
        <span class="help-text">Accepts positive, negative, and decimal values separated by commas, spaces, tabs, or line breaks.</span>
      </div>

      <div class="input-group">
        <label for="precision-select">Decimal Precision</label>
        <select id="precision-select" class="form-control" onchange="calculateMidrange()">
          <option value="2">2 decimal places</option>
          <option value="4" selected>4 decimal places</option>
          <option value="6">6 decimal places</option>
        </select>
      </div>

      <div style="display:flex; gap:12px; margin-top:16px;">
        <button id="calc-btn" class="btn-primary" onclick="calculateMidrange()" style="flex:1;">Compute Midrange</button>
        <button id="reset-btn" class="btn-secondary" onclick="resetMidrange()">Reset</button>
      </div>

      <div id="result-box" class="result-box" style="margin-top:24px;">
        <h2 class="result-title">Central Tendency &amp; Range Analysis</h2>
        <div class="result-highlight" style="font-size:1.8rem; font-weight:700; color:var(--primary); margin-bottom:16px;" id="res-midrange">
          Midrange: 30.0000
        </div>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:16px;">
          <div><span class="res-label">Minimum Value (S):</span> <strong class="res-val" id="res-min">15.0000</strong></div>
          <div><span class="res-label">Maximum Value (L):</span> <strong class="res-val" id="res-max">45.0000</strong></div>
          <div><span class="res-label">Total Range (L - S):</span> <strong class="res-val" id="res-range">30.0000</strong></div>
          <div><span class="res-label">Arithmetic Mean (x̄):</span> <strong class="res-val" id="res-mean">28.7143</strong></div>
          <div><span class="res-label">Median (Q₂):</span> <strong class="res-val" id="res-median">29.0000</strong></div>
          <div><span class="res-label">Midhinge (Q₁+Q₃)/2:</span> <strong class="res-val" id="res-midhinge">26.5000</strong></div>
          <div><span class="res-label">Dataset Count (n):</span> <strong class="res-val" id="res-count">7</strong></div>
        </div>

        <h3 style="margin-top:20px; font-size:1.1rem; color:var(--text-dark);">Step-by-Step Calculation Breakdown</h3>
        <div id="res-steps" style="background:var(--bg-subtle, #f8fafc); padding:16px; border-radius:8px; font-family:monospace; font-size:0.95rem; white-space:pre-wrap; border:1px solid var(--border-color, #e2e8f0); margin-bottom:16px;"></div>

        <h3 style="margin-top:16px; font-size:1.1rem; color:var(--text-dark);">Sorted Dataset &amp; Order Statistics</h3>
        <div id="res-sorted" style="background:var(--bg-subtle, #f8fafc); padding:12px; border-radius:6px; font-size:0.95rem; color:var(--text-dark); border:1px solid var(--border-color, #e2e8f0);"></div>
      </div>
    </div>

    <article class="article-body">
      <h2>Comprehensive Theoretical &amp; Statistical Guide to the Midrange</h2>
      <p>In descriptive and mathematical statistics, the midrange (also referred to as the mid-range or center of range) is a classic measure of central tendency that quantifies the exact arithmetic midpoint between the extreme endpoints of a distribution. While elementary statistics primarily emphasizes the <a href="mean-median-mode-calculator.html">mean, median, and mode</a>, the midrange represents the boundary-based anchor of a sample space. It is defined as the arithmetic mean of the maximum and minimum observations in an ordered dataset.</p>

      <p>Despite being computationally trivial to calculate, the midrange exhibits unique mathematical properties in estimation theory. In classical robust statistics, the midrange has a breakdown point of \(0\%\), meaning a single erroneous outlier can distort its value arbitrarily. However, in statistical physics, industrial quality assurance, and climatology, the midrange serves as an indispensable tool. Most notably, for bounded continuous uniform distributions \(U(a, b)\), the midrange is the uniformly minimum-variance unbiased estimator (UMVUE) of the distribution's true center, outperforming both the sample mean and the sample median in statistical efficiency.</p>

      <h2>Mathematical Formulation &amp; Order Statistics</h2>
      <p>Let a random sample of size \(n\) be denoted as \(X = \{x_1, x_2, \dots, x_n\}\). Sorting the sample in ascending order yields the sequence of order statistics:</p>
      $$x_{(1)} \le x_{(2)} \le \dots \le x_{(n-1)} \le x_{(n)}$$
      <p>Where:</p>
      <ul>
        <li>\(x_{(1)} = \min(X) = S\) represents the first order statistic (sample minimum).</li>
        <li>\(x_{(n)} = \max(X) = L\) represents the \(n\)-th order statistic (sample maximum).</li>
      </ul>

      <h3>1. Primary Midrange Formulation</h3>
      <p>The statistical midrange \(M_{\text{mid}}\) is evaluated as:</p>
      $$M_{\text{mid}} = \frac{x_{(1)} + x_{(n)}}{2} = \frac{\min(X) + \max(X)}{2} = \frac{S + L}{2}$$
      <p>Geometrically, the midrange divides the total sample range \(R = x_{(n)} - x_{(1)} = L - S\) into two exactly equal halves of width \(\frac{R}{2}\):</p>
      $$x_{(1)} + \frac{R}{2} = M_{\text{mid}} = x_{(n)} - \frac{R}{2}$$

      <h3>2. Comparison with Related L-Estimators</h3>
      <p>The midrange is an extreme member of the family of \(L\)-estimators (linear combinations of order statistics). Other prominent members include:</p>
      <div class="formula-box">
        <h3>Related Range-Centering Metrics</h3>
        $$\text{Sample Range: } R = x_{(n)} - x_{(1)} = L - S$$
        $$\text{Midhinge: } \text{MH} = \frac{Q_1 + Q_3}{2}$$
        $$\text{Trimean (Tukey): } \text{TM} = \frac{Q_1 + 2Q_2 + Q_3}{4} = \frac{\text{Midhinge} + \text{Median}}{2}$$
        $$\text{Trimmed Midrange (}\alpha\text{-trimmed): } M_{\alpha} = \frac{x_{(\lfloor \alpha n \rfloor + 1)} + x_{(n - \lfloor \alpha n \rfloor)}}{2}$$
      </div>
      <p>While the midrange uses the \(0\%\) and \(100\%\) percentiles, the midhinge uses the \(25\%\) and \(75\%\) quartiles (\(Q_1\) and \(Q_3\)), providing robust center estimation that resists up to \(25\%\) extreme outlier contamination.</p>

      <h2>Statistical Efficiency: Bounded Uniform vs. Normal Distributions</h2>
      <p>A critical question in estimation theory is determining which measure of central tendency minimizes the mean squared error (MSE) for a given probability distribution:</p>
      <ul>
        <li><strong>Continuous Uniform Distribution \(U(a, b)\):</strong> For a uniform distribution where data points are evenly distributed between lower bound \(a\) and upper bound \(b\), the sample mean \(\bar{x}\) converges to the center with a variance of \(\mathcal{O}(1/n)\). However, the midrange converges at a much faster rate of \(\mathcal{O}(1/n^2)\). Consequently, the midrange is the maximum likelihood estimator (MLE) and UMVUE, vastly outperforming the sample mean.</li>
        <li><strong>Standard Normal Distribution \(N(\mu, \sigma^2)\):</strong> For a Gaussian distribution, the sample mean is the optimal UMVUE with \(100\%\) efficiency. In contrast, the asymptotic relative efficiency of the midrange drops to zero as \(n \to \infty\) because normal distributions have infinite tails where extreme order statistics fluctuate widely, as explored in our <a href="variance-calculator.html">Variance Calculator</a>.</li>
        <li><strong>Heavy-Tailed Distributions (Cauchy / Pareto):</strong> When data exhibits extreme tail behavior, the midrange is completely destabilized, and the sample median or trimmed mean must be employed.</li>
      </ul>

      <h2>Central Tendency &amp; Centering Metric Benchmark Matrix</h2>
      <p>The following multi-column benchmark matrix summarizes how the midrange compares against alternative statistical measures of center across breakdown points, data utilization, and optimal distribution regimes:</p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Central Metric</th>
            <th>Formula</th>
            <th>Data Utilization</th>
            <th>Breakdown Point</th>
            <th>Optimal Distribution Regime</th>
            <th>Sensitivity to Outliers</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Midrange</td>
            <td>\(\frac{\min + \max}{2}\)</td>
            <td>2 Extreme points</td>
            <td>\(0\%\) (Worst)</td>
            <td>Continuous Uniform \(U(a, b)\)</td>
            <td>Extremely High (Maximally sensitive)</td>
          </tr>
          <tr>
            <td>Arithmetic Mean</td>
            <td>\(\frac{\sum x_i}{n}\)</td>
            <td>All \(n\) observations</td>
            <td>\(0\%\)</td>
            <td>Gaussian / Normal \(N(\mu, \sigma^2)\)</td>
            <td>High (Shifts proportionally with outlier)</td>
          </tr>
          <tr>
            <td>Sample Median</td>
            <td>\(x_{((n+1)/2)}\)</td>
            <td>Middle rank(s)</td>
            <td>\(50\%\) (Optimal)</td>
            <td>Laplace (Double Exponential)</td>
            <td>Very Low (Robust against \(50\%\) corruption)</td>
          </tr>
          <tr>
            <td>Midhinge</td>
            <td>\(\frac{Q_1 + Q_3}{2}\)</td>
            <td>2 Quartile bounds</td>
            <td>\(25\%\)</td>
            <td>Symmetric bounded distributions</td>
            <td>Moderate (Ignores outer \(25\%\) extremes)</td>
          </tr>
          <tr>
            <td>Trimean</td>
            <td>\(\frac{Q_1 + 2Q_2 + Q_3}{4}\)</td>
            <td>3 Quartile points</td>
            <td>\(25\%\)</td>
            <td>Skewed exploratory data analysis</td>
            <td>Low (Tukey exploratory standard)</td>
          </tr>
          <tr>
            <td>Mode</td>
            <td>\(\arg\max f(x)\)</td>
            <td>Peak frequency</td>
            <td>\(N/A\)</td>
            <td>Categorical / Multimodal data</td>
            <td>Immune to tail values, sensitive to binning</td>
          </tr>
        </tbody>
      </table>

      <h2>Real-World Practical Engineering &amp; Climatology Case Studies</h2>
      <p>The following real-world case studies illustrate the practical application of the midrange across meteorology, industrial quality engineering, and telecommunications.</p>

      <div class="worked-example-card">
        <h3>Case Study 1: Climatological Daily Mean Temperature Reporting</h3>
        <p><strong>Scenario:</strong> The World Meteorological Organization (WMO) and national weather services (such as the US National Weather Service) traditionally record daily climate records using maximum-minimum thermometers. On a given summer day, a weather station logs the following hourly temperatures (\(^\circ\text{C}\)): \(16.2, 18.0, 21.5, 25.8, 29.4, 32.6, 31.0, 27.2, 22.1, 18.5, 17.0\). The station meteorologist must determine the official daily midrange temperature versus the 11-hour arithmetic mean.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Identify the minimum daily temperature (\(S\)):
            $$S = \min(T) = 16.2^\circ\text{C}$$
          </li>
          <li>Identify the maximum daily temperature (\(L\)):
            $$L = \max(T) = 32.6^\circ\text{C}$$
          </li>
          <li>Calculate the official climatological daily midrange:
            $$M_{\text{mid}} = \frac{S + L}{2} = \frac{16.2 + 32.6}{2} = \frac{48.8}{2} = 24.4000^\circ\text{C}$$
          </li>
          <li>Calculate the true 11-observation arithmetic mean for comparison:
            $$\sum T = 16.2 + 18.0 + 21.5 + 25.8 + 29.4 + 32.6 + 31.0 + 27.2 + 22.1 + 18.5 + 17.0 = 259.3^\circ\text{C}$$
            $$\bar{T} = \frac{259.3}{11} \approx 23.5727^\circ\text{C}$$
          </li>
          <li>Compute discrepancy between midrange and arithmetic mean:
            $$\Delta = 24.4000 - 23.5727 = +0.8273^\circ\text{C}$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The official climatological daily midrange is \(24.4000^\circ\text{C}\), differing from the full hourly arithmetic mean by \(0.83^\circ\text{C}\) due to asymmetric afternoon peak warming.</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Industrial Manufacturing Tolerance Midrange &amp; Range</h3>
        <p><strong>Scenario:</strong> An automotive machining facility inspects the outer diameter of precision steel transmission pins (nominal specification \(25.000 \pm 0.050 \text{ mm}\)). A quality control technician samples a subgroup of 5 pins from a production run: \(25.012, 24.988, 25.004, 25.035, 24.995 \text{ mm}\). The technician must evaluate the subgroup midrange and range to populate an \(\bar{X}-R\) Shewhart control chart.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Sort the subgroup in ascending order:
            $$x_{(1)} = 24.988, \; x_{(2)} = 24.995, \; x_{(3)} = 25.004, \; x_{(4)} = 25.012, \; x_{(5)} = 25.035$$
          </li>
          <li>Determine sample minimum and maximum:
            $$S = 24.988 \text{ mm}, \quad L = 25.035 \text{ mm}$$
          </li>
          <li>Calculate subgroup range \(R\):
            $$R = L - S = 25.035 - 24.988 = 0.0470 \text{ mm}$$
          </li>
          <li>Calculate subgroup midrange \(M_{\text{mid}}\):
            $$M_{\text{mid}} = \frac{24.988 + 25.035}{2} = \frac{50.023}{2} = 25.0115 \text{ mm}$$
          </li>
          <li>Compare against nominal target:
            $$\text{Offset from nominal } 25.000 = 25.0115 - 25.000 = +0.0115 \text{ mm}$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The subgroup exhibits a total range of \(0.0470 \text{ mm}\) and a midrange of \(25.0115 \text{ mm}\), confirming the cutting tool is centered within the allowable \(\pm 0.050 \text{ mm}\) design boundaries.</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 3: Analog-to-Digital Converter Dynamic Range Midpoint</h3>
        <p><strong>Scenario:</strong> An embedded systems firmware engineer calibrates a 12-bit Analog-to-Digital Converter (ADC) input channel. Over a continuous test scan of a sensor input signal, the lowest digital raw code observed is \(S = 420\) and the highest code observed is \(L = 3680\). The firmware calibration table requires the midrange zero-bias centerpoint and the midhinge calculated from the first quartile \(Q_1 = 1240\) and third quartile \(Q_3 = 2860\).</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Compute raw digital code midrange:
            $$M_{\text{mid}} = \frac{420 + 3680}{2} = \frac{4100}{2} = 2050.0000 \text{ ADC codes}$$
          </li>
          <li>Compute interquartile midhinge:
            $$\text{MH} = \frac{Q_1 + Q_3}{2} = \frac{1240 + 2860}{2} = \frac{4100}{2} = 2050.0000 \text{ ADC codes}$$
          </li>
          <li>Convert code midrange to physical analog voltage on a \(3.3 \text{ V}\) reference scale:
            $$V_{\text{mid}} = \frac{M_{\text{mid}}}{4095} \times 3.3 \text{ V} = \frac{2050}{4095} \times 3.3 \approx 1.6520 \text{ V}$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> Because the midrange and midhinge are identical at \(2050.0000\) codes (\(1.6520 \text{ V}\)), the sensor dynamic range is highly symmetric around the \(1.650 \text{ V}\) half-rail analog reference bias.</p>
      </div>

      <h2>Frequently Asked Questions</h2>
      <div class="faq-item">
        <div class="faq-question">Why is the midrange considered an L-estimator?</div>
        <div class="faq-answer">An L-estimator is any statistical estimator formed as a linear combination of order statistics: \(L = \sum c_i x_{(i)}\). The midrange sets the coefficient weights of the first and last order statistics to \(c_1 = 0.5\) and \(c_n = 0.5\), while assigning \(c_i = 0\) to all intermediate data points. It is therefore a boundary-weighted L-estimator.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Why does the midrange have a 0% breakdown point?</div>
        <div class="faq-answer">The breakdown point measures the smallest fraction of observations that can arbitrarily alter an estimator's value. In a sample of size n, replacing just one single observation with infinity (\(+\infty\) or \(-\infty\)) replaces either the maximum or the minimum, driving the midrange to infinity. Because \(1/n \to 0\%\) as sample size grows, the midrange has a zero breakdown point.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Can the midrange equal the median and the mean?</div>
        <div class="faq-answer">Yes. In any perfectly symmetric distribution without skewness (such as a uniform, triangular, or standard normal distribution), the expected values of the midrange, mean, and median are identical. In empirical samples, if the data is symmetrically spaced around its center, all three metrics will coincide.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">How does Tukey's Trimean improve upon the midrange?</div>
        <div class="faq-answer">John Tukey introduced the Trimean \(\text{TM} = (Q_1 + 2Q_2 + Q_3) / 4\) to retain the intuitive centering structure of range-based L-estimators while overcoming the zero-breakdown vulnerability of the midrange. By weighting the median at \(50\%\) and the quartiles at \(25\%\) each, the trimean achieves a robust \(25\%\) breakdown point.</div>
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
    function parseNumbers(text) {
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

    function calculateMidrange() {
      var raw = document.getElementById('dataset-input').value;
      var data = parseNumbers(raw);
      var prec = parseInt(document.getElementById('precision-select').value, 10) || 4;

      if (data.length === 0) {
        showError("Please enter at least one valid numerical observation.");
        return;
      }

      var sorted = data.slice().sort(function(a, b) { return a - b; });
      var n = sorted.length;
      var minVal = sorted[0];
      var maxVal = sorted[n - 1];
      var rangeVal = maxVal - minVal;
      var midrange = (minVal + maxVal) / 2;

      var sum = 0;
      for (var i = 0; i < n; i++) sum += sorted[i];
      var mean = sum / n;

      var median = 0;
      if (n % 2 === 1) {
        median = sorted[Math.floor(n / 2)];
      } else {
        median = (sorted[n / 2 - 1] + sorted[n / 2]) / 2;
      }

      // Quartiles for midhinge
      function getQuartile(arr, q) {
        var pos = (arr.length - 1) * q;
        var base = Math.floor(pos);
        var rest = pos - base;
        if (arr[base + 1] !== undefined) {
          return arr[base] + rest * (arr[base + 1] - arr[base]);
        } else {
          return arr[base];
        }
      }

      var q1 = getQuartile(sorted, 0.25);
      var q3 = getQuartile(sorted, 0.75);
      var midhinge = (q1 + q3) / 2;

      document.getElementById('res-midrange').innerText = "Midrange: " + midrange.toFixed(prec);
      document.getElementById('res-min').innerText = minVal.toFixed(prec);
      document.getElementById('res-max').innerText = maxVal.toFixed(prec);
      document.getElementById('res-range').innerText = rangeVal.toFixed(prec);
      document.getElementById('res-mean').innerText = mean.toFixed(prec);
      document.getElementById('res-median').innerText = median.toFixed(prec);
      document.getElementById('res-midhinge').innerText = midhinge.toFixed(prec);
      document.getElementById('res-count').innerText = n.toString();

      var steps = "Dataset Analysis (Sample Size n = " + n + "):\n" +
                  "1. Identify Extremes:\n" +
                  "   Minimum (S) = " + minVal.toFixed(prec) + "\n" +
                  "   Maximum (L) = " + maxVal.toFixed(prec) + "\n\n" +
                  "2. Midrange Formula:\n" +
                  "   Midrange = (Minimum + Maximum) / 2\n" +
                  "   Midrange = (" + minVal.toFixed(prec) + " + " + maxVal.toFixed(prec) + ") / 2 = " + (minVal + maxVal).toFixed(prec) + " / 2\n" +
                  "   Midrange = " + midrange.toFixed(prec) + "\n\n" +
                  "3. Range: L - S = " + maxVal.toFixed(prec) + " - " + minVal.toFixed(prec) + " = " + rangeVal.toFixed(prec) + "\n" +
                  "4. Comparisons:\n" +
                  "   Arithmetic Mean = " + mean.toFixed(prec) + "\n" +
                  "   Median (Q₂) = " + median.toFixed(prec) + "\n" +
                  "   Midhinge (Q₁+Q₃)/2 = (" + q1.toFixed(prec) + " + " + q3.toFixed(prec) + ") / 2 = " + midhinge.toFixed(prec);

      document.getElementById('res-steps').innerText = steps;
      document.getElementById('res-sorted').innerText = "Sorted Data: " + sorted.join(", ");
    }

    function showError(msg) {
      document.getElementById('res-midrange').innerText = "Error";
      document.getElementById('res-min').innerText = "N/A";
      document.getElementById('res-max').innerText = "N/A";
      document.getElementById('res-range').innerText = "N/A";
      document.getElementById('res-mean').innerText = "N/A";
      document.getElementById('res-median').innerText = "N/A";
      document.getElementById('res-midhinge').innerText = "N/A";
      document.getElementById('res-count').innerText = "0";
      document.getElementById('res-steps').innerText = "Error: " + msg;
      document.getElementById('res-sorted').innerText = "No data available";
    }

    function resetMidrange() {
      document.getElementById('dataset-input').value = "18, 24, 32, 15, 45, 29, 38";
      document.getElementById('precision-select').value = "4";
      calculateMidrange();
    }

    window.addEventListener('DOMContentLoaded', function() {
      calculateMidrange();
    });
  </script>
</body>
</html>
"""

def main():
    p1 = os.path.join(BASE_DIR, "distance-calculator.html")
    with open(p1, "w", encoding="utf-8") as f:
        f.write(HTML_DISTANCE)
    print("Generated:", p1)

    p2 = os.path.join(BASE_DIR, "midrange-calculator.html")
    with open(p2, "w", encoding="utf-8") as f:
        f.write(HTML_MIDRANGE)
    print("Generated:", p2)

if __name__ == "__main__":
    main()
