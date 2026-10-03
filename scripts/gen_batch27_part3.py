import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 1. PYTHAGOREAN THEOREM CALCULATOR
# -------------------------------------------------------------
pyth_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pythagorean Theorem Calculator — Hypotenuse, Legs, Triangles & 3D Distance | CalcHub</title>
  <meta name="description" content="Calculate right triangle hypotenuse, legs, acute angles, area, and 3D Euclidean distance using the Pythagorean Theorem (a² + b² = c²) with step-by-step proofs.">
  <meta name="keywords" content="pythagorean theorem calculator, right triangle calculator, find hypotenuse, a2 + b2 = c2, pythagorean triples, 3d distance formula, 3 4 5 triangle, right triangle angles">
  <meta name="author" content="CalcHub Euclidean Geometry & Trigonometry Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/pythagorean-theorem-calculator.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="Pythagorean Theorem Calculator — Hypotenuse, Legs, Triangles & 3D Distance | CalcHub">
  <meta property="og:description" content="Solve right-angled triangles and 3D Euclidean vectors with exact radical roots, area, acute angles, and step-by-step algebraic breakdown.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/pythagorean-theorem-calculator.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/pythagorean-theorem-calculator.html#app",
      "name": "Pythagorean Theorem & Right Triangle Engine",
      "url": "https://calchub.org/pythagorean-theorem-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "High-precision geometric solver for right-angled triangles and Euclidean space diagonals using the Pythagorean theorem a² + b² = c²."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Math & Engineering Calculators", "item": "https://calchub.org/math.html"},
        {"@type": "ListItem", "position": 3, "name": "Pythagorean Theorem Calculator", "item": "https://calchub.org/pythagorean-theorem-calculator.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the Pythagorean Theorem and under what conditions does it apply?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The Pythagorean Theorem states that in any right-angled triangle in flat Euclidean space, the square of the length of the hypotenuse (c, the side opposite the 90-degree right angle) is exactly equal to the sum of the squares of the lengths of the two remaining perpendicular sides (legs a and b): a² + b² = c². The theorem holds strictly for planar Euclidean geometry and fails on curved spherical or hyperbolic surfaces."
          }
        },
        {
          "@type": "Question",
          "name": "How does the Pythagorean Theorem extend to three-dimensional (3D) space?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The 3D space diagonal of a rectangular cuboid with width w, length l, and height h is derived by applying the Pythagorean theorem twice in succession. First, the diagonal of the floor base is d_base = √(w² + l²). Second, treating d_base and height h as perpendicular legs yields the 3D space diagonal: d_space = √(d_base² + h²) = √(w² + l² + h²). In Cartesian coordinates, the Euclidean distance between points (x₁, y₁, z₁) and (x₂, y₂, z₂) is √[(x₂ - x₁)² + (y₂ - y₁)² + (z₂ - z₁)²]."
          }
        },
        {
          "@type": "Question",
          "name": "What are primitive Pythagorean triples and how are they generated?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A Pythagorean triple is a set of three positive integers (a, b, c) satisfying a² + b² = c². A triple is primitive if a, b, and c are coprime (gcd(a, b, c) = 1). By Euclid's generating formula, for any two coprime positive integers m and n with m > n and one even while the other is odd, the formulas a = m² - n², b = 2mn, and c = m² + n² generate all primitive Pythagorean triples, such as (3, 4, 5), (5, 12, 13), and (8, 15, 17)."
          }
        },
        {
          "@type": "Question",
          "name": "Why is the 3-4-5 rule widely utilized in carpentry and building construction?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Carpenters and foundation masons use the 3-4-5 rule to establish perfect 90-degree right angles without complex optical tools. By measuring 3 units along one wall baseline, 4 units along the perpendicular wall, and adjusting the angle until the diagonal distance between the endpoints measures exactly 5 units, the converse of the Pythagorean Theorem guarantees that the corner is an exact right angle (since 3² + 4² = 9 + 16 = 25 = 5²)."
          }
        }
      ]
    }
  ]
}
  </script>
</head>
<body class="converter-page">
  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="logo">
        <span class="logo-badge">∑</span>
        <span>Calc<span class="accent">Hub</span></span>
      </a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="converter.html">Converters</a>
        <a href="math.html" class="active">Math & Engineering</a>
      </nav>
    </div>
  </header>

  <main class="main-content">
    <div class="container">
      <div class="page-layout">
        <div class="content-column">
          <header class="tool-header">
            <div class="badge-tag">Euclidean Geometry & Trigonometry</div>
            <h1 class="tool-title">Pythagorean Theorem Calculator</h1>
            <p class="tool-subtitle">Solve right-angled triangles \(a^2 + b^2 = c^2\) for hypotenuse or perpendicular legs with exact radicals, acute angles, triangle area, and 3D Euclidean distances.</p>
          </header>

          <section class="calculator-card" aria-label="Pythagorean Theorem Solver">
            <div class="calc-grid">
              <div class="input-group">
                <label for="solveForSelect" class="input-label">Variable to Solve For</label>
                <select id="solveForSelect" class="calc-input">
                  <option value="hypotenuse">Hypotenuse (c) — from legs a &amp; b</option>
                  <option value="legA">Leg (a) — from leg b &amp; hypotenuse c</option>
                  <option value="legB">Leg (b) — from leg a &amp; hypotenuse c</option>
                </select>
              </div>

              <div class="input-group">
                <label for="side1Input" class="input-label" id="side1Label">Leg a</label>
                <input type="number" id="side1Input" class="calc-input" value="3" step="any" min="0.0001">
              </div>

              <div class="input-group">
                <label for="side2Input" class="input-label" id="side2Label">Leg b</label>
                <input type="number" id="side2Input" class="calc-input" value="4" step="any" min="0.0001">
              </div>
            </div>

            <div class="primary-result" style="margin-top: 25px;">
              <div class="result-label" id="pythPrimaryLabel">Calculated Hypotenuse (c)</div>
              <div class="result-value" id="pythPrimaryResult">5.0000</div>
              <div class="result-subtext" id="pythRadicalSubtext">Exact form: c = √25 = 5</div>
            </div>

            <div class="results-grid" style="margin-top: 20px;">
              <div class="result-item">
                <div class="result-label">Acute Angle α (opposite a)</div>
                <div class="result-value" id="resAngleA">36.87°</div>
              </div>
              <div class="result-item">
                <div class="result-label">Acute Angle β (opposite b)</div>
                <div class="result-value" id="resAngleB">53.13°</div>
              </div>
              <div class="result-item">
                <div class="result-label">Triangle Area (½ × a × b)</div>
                <div class="result-value" id="resArea">6.0000</div>
              </div>
              <div class="result-item">
                <div class="result-label">Perimeter (a + b + c)</div>
                <div class="result-value" id="resPerimeter">12.0000</div>
              </div>
              <div class="result-item">
                <div class="result-label">Altitude to Hypotenuse (\(h_c\))</div>
                <div class="result-value" id="resAltitude">2.4000</div>
              </div>
              <div class="result-item">
                <div class="result-label">Inradius (\(r\))</div>
                <div class="result-value" id="resInradius">1.0000</div>
              </div>
            </div>

            <div class="conversion-steps" style="margin-top: 25px;">
              <h3>Algorithmic Resolution Steps</h3>
              <div id="pythStepsDisplay" style="font-family: monospace; font-size: 0.95rem; line-height: 1.6; background: rgba(0,0,0,0.03); padding: 16px; border-radius: 8px; border-left: 4px solid var(--accent, #2563eb);">
                Loading calculation steps...
              </div>
            </div>
          </section>

          <article class="article-body">
            <h2>1. Axiomatic Principles of the Pythagorean Theorem</h2>
            <p>Among all geometrical relationships discovered in human history, none has exerted a deeper impact across mathematics, physical sciences, and architectural engineering than the <strong>Pythagorean Theorem</strong>. Formalized in Greek antiquity around 500 BCE by the Pythagorean school of Croton and documented rigorously in Book I, Proposition 47 of Euclid's <em>Elements</em>, the theorem establishes the invariant metric relationship governing the sides of a right-angled triangle in flat Euclidean space.</p>

            <p>Let \(\triangle ABC\) be a planar triangle with a right angle (\(90^\circ\) or \(\frac{\pi}{2}\text{ radians}\)) at vertex \(C\). Let \(a\) and \(b\) denote the lengths of the two legs adjacent to the right angle (the catheti), and let \(c\) denote the length of the side opposing the right angle (the <strong>hypotenuse</strong>). The theorem dictates:</p>

            $$a^2 + b^2 = c^2$$

            <p>Equivalently, the area of the square constructed on the hypotenuse is exactly equal to the sum of the areas of the two squares constructed on the perpendicular legs. Solving explicitly for each individual variable gives the three fundamental operational formulas:</p>

            $$c = \sqrt{a^2 + b^2}$$

            $$a = \sqrt{c^2 - b^2} \quad (\text{subject to } c > b > 0)$$

            $$b = \sqrt{c^2 - a^2} \quad (\text{subject to } c > a > 0)$$

            <p>Because lengths are physical geometric distances, all side quantities are strictly positive real numbers (\(a, b, c \in \mathbb{R}^+\)). Furthermore, by the triangle inequality and the nature of right triangles, the hypotenuse is strictly the longest side of the triangle: \(c > a\) and \(c > b\).</p>

            <h2>2. Classical Proofs of the Theorem</h2>
            <p>Over four hundred distinct mathematical proofs of the Pythagorean theorem have been compiled throughout history, spanning synthetic geometry, vector algebra, differential calculus, and physical mass-center statics. Two proofs are celebrated for their elegance and clarity:</p>

            <h3>2.1 Proof by Area Rearrangement (Geometric Algebra)</h3>
            <p>Consider a large square whose side length is \(a + b\). The total surface area of this large outer square is given by:</p>

            $$\mathcal{A}_{\text{total}} = (a + b)^2 = a^2 + 2ab + b^2$$

            <p>Now, partition the interior of this large square into four identical right-angled triangles, each having base \(b\), height \(a\), and hypotenuse \(c\). Arrange these four triangles around the four corners such that their hypotenuses enclose a central quadrilateral with four equal sides of length \(c\). Because each acute angle sum satisfies \(\alpha + \beta = 90^\circ\), the interior angles of this central quadrilateral must each equal \(180^\circ - (\alpha + \beta) = 90^\circ\), proving that the central shape is a perfect square of area \(c^2\).</p>

            <p>The total area of the large square can thus be expressed as the sum of the inner square plus the four congruent right triangles:</p>

            $$\mathcal{A}_{\text{total}} = c^2 + 4 \times \left(\frac{1}{2}ab\right) = c^2 + 2ab$$

            <p>Equating both algebraic formulations for the same area:</p>

            $$a^2 + 2ab + b^2 = c^2 + 2ab$$

            <p>Subtracting the shared cross-product term \(2ab\) from both sides produces the desired identity:</p>

            $$a^2 + b^2 = c^2$$

            <h3>2.2 Proof Using Similar Triangles via Hypotenuse Altitude</h3>
            <p>Drop a perpendicular altitude line from the right-angled vertex \(C\) onto the hypotenuse \(AB\), intersecting at point \(D\). Let \(h_c = CD\), and let \(D\) partition the hypotenuse \(c\) into two segments: \(c_1 = AD\) and \(c_2 = DB\), such that \(c = c_1 + c_2\).</p>

            <p>The altitude creates two smaller right triangles, \(\triangle ACD\) and \(\triangle CBD\). Both smaller triangles share an acute angle with the parent triangle \(\triangle ABC\). By angle-angle-angle (AAA) similarity:</p>

            $$\triangle ACD \sim \triangle ABC \implies \frac{c_1}{a} = \frac{a}{c} \implies a^2 = c \cdot c_1$$

            $$\triangle CBD \sim \triangle ABC \implies \frac{c_2}{b} = \frac{b}{c} \implies b^2 = c \cdot c_2$$

            <p>Summing both equations:</p>

            $$a^2 + b^2 = c \cdot c_1 + c \cdot c_2 = c (c_1 + c_2) = c \cdot c = c^2$$

            <p>This proof directly establishes the geometric mean theorems and shows that the Pythagorean relation reflects the self-similar scale invariance of right triangles.</p>

            <h2>3. Acute Angles, Trigonometry, and Inscribed Circles</h2>
            <p>Once the side lengths \(a, b, c\) are determined, all remaining trigonometric and geometric properties of the right triangle are uniquely locked:</p>

            <h3>3.1 Acute Angles (\(\alpha\) and \(\beta\))</h3>
            <p>The two non-right angles are complementary, summing to exactly \(90^\circ\) (\(\alpha + \beta = 90^\circ\)). Applying the standard inverse trigonometric functions:</p>

            $$\alpha = \arcsin\left(\frac{a}{c}\right) = \arccos\left(\frac{b}{c}\right) = \arctan\left(\frac{a}{b}\right)$$

            $$\beta = \arcsin\left(\frac{b}{c}\right) = \arccos\left(\frac{a}{c}\right) = \arctan\left(\frac{b}{a}\right) = 90^\circ - \alpha$$

            <h3>3.2 Triangle Area, Altitude, and Inradius</h3>
            <ul>
              <li><strong>Triangle Area:</strong> \(\mathcal{A} = \frac{1}{2} a b\)</li>
              <li><strong>Altitude to Hypotenuse:</strong> Setting area \(\frac{1}{2} c h_c = \frac{1}{2} a b\) yields \(h_c = \frac{ab}{c}\)</li>
              <li><strong>Inradius (radius of incircle):</strong> \(r = \frac{a + b - c}{2} = \frac{\mathcal{A}}{s}\) where semi-perimeter \(s = \frac{a + b + c}{2}\)</li>
              <li><strong>Circumradius (radius of circumcircle):</strong> By Thales's Theorem, the hypotenuse is the diameter of the circumscribed circle, so \(R = \frac{c}{2}\)</li>
            </ul>

            <h2>4. Extension to 3D and n-Dimensional Euclidean Space</h2>
            <p>The Pythagorean theorem is the axiomatic foundation of the Euclidean metric in multidimensional spaces. In Cartesian coordinates, the straight-line distance \(d\) between two points \(P_1(x_1, y_1)\) and \(P_2(x_2, y_2)\) is obtained directly from a right triangle with legs \(\Delta x = |x_2 - x_1|\) and \(\Delta y = |y_2 - y_1|\):</p>

            $$d = \sqrt{(\Delta x)^2 + (\Delta y)^2} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

            <h3>4.1 The 3D Space Diagonal</h3>
            <p>In three-dimensional solid geometry, consider a rectangular box (cuboid) with dimensions width \(w\), length \(l\), and height \(h\). To find the internal space diagonal connecting opposite corners:</p>
            <ol>
              <li>First compute the planar diagonal of the base rectangle: \(d_{\text{base}} = \sqrt{w^2 + l^2}\).</li>
              <li>The space diagonal forms a right triangle with \(d_{\text{base}}\) as one leg and the vertical height \(h\) as the perpendicular leg:</li>
            </ol>

            $$d_{\text{space}} = \sqrt{(d_{\text{base}})^2 + h^2} = \sqrt{(\sqrt{w^2 + l^2})^2 + h^2} = \sqrt{w^2 + l^2 + h^2}$$

            <p>In general \(n\)-dimensional Euclidean space \(\mathbb{R}^n\), the distance between vectors \(\mathbf{u}\) and \(\mathbf{v}\) is the Euclidean norm (\(L_2\) norm):</p>

            $$\|\mathbf{u} - \mathbf{v}\|_2 = \sqrt{\sum_{i=1}^n (u_i - v_i)^2}$$

            <h2>5. Pythagorean Triples and Number Theory</h2>
            <p>When all three side lengths of a right triangle are positive integers, the tuple \((a, b, c)\) is termed a <strong>Pythagorean Triple</strong>. If \(\gcd(a, b, c) = 1\), the triple is termed <strong>primitive</strong>. Any non-primitive triple is simply an integer scalar multiple \(k(a, b, c) = (ka, kb, kc)\) of a primitive triple.</p>

            <h3>5.1 Euclid's Generating Formula</h3>
            <p>Euclid proved that every primitive Pythagorean triple can be generated by choosing two coprime positive integers \(m\) and \(n\) such that \(m > n\), with exactly one of them being even and the other odd:</p>

            $$a = m^2 - n^2, \quad b = 2mn, \quad c = m^2 + n^2$$

            <p>Verification by algebraic expansion:</p>

            $$a^2 + b^2 = (m^2 - n^2)^2 + (2mn)^2 = m^4 - 2m^2 n^2 + n^4 + 4m^2 n^2 = m^4 + 2m^2 n^2 + n^4 = (m^2 + n^2)^2 = c^2$$

            <h2>6. Benchmark Comparative Reference Table</h2>
            <p>The table below presents ten fundamental Primitive Pythagorean Triples, detailing their generator parameters \((m, n)\), side lengths, acute angles, area, and inradius.</p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>Triple \((a, b, c)\)</th>
                  <th>Generators \((m, n)\)</th>
                  <th>Leg \(a\)</th>
                  <th>Leg \(b\)</th>
                  <th>Hypotenuse \(c\)</th>
                  <th>Acute Angle \(\alpha\)</th>
                  <th>Triangle Area</th>
                  <th>Inradius \(r\)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>(3, 4, 5)</td>
                  <td>(2, 1)</td>
                  <td>3</td>
                  <td>4</td>
                  <td>5</td>
                  <td>36.87°</td>
                  <td>6</td>
                  <td>1</td>
                </tr>
                <tr>
                  <td>(5, 12, 13)</td>
                  <td>(3, 2)</td>
                  <td>5</td>
                  <td>12</td>
                  <td>13</td>
                  <td>22.62°</td>
                  <td>30</td>
                  <td>2</td>
                </tr>
                <tr>
                  <td>(8, 15, 17)</td>
                  <td>(4, 1)</td>
                  <td>8</td>
                  <td>15</td>
                  <td>17</td>
                  <td>28.07°</td>
                  <td>60</td>
                  <td>3</td>
                </tr>
                <tr>
                  <td>(7, 24, 25)</td>
                  <td>(4, 3)</td>
                  <td>7</td>
                  <td>24</td>
                  <td>25</td>
                  <td>16.26°</td>
                  <td>84</td>
                  <td>3</td>
                </tr>
                <tr>
                  <td>(20, 21, 29)</td>
                  <td>(5, 2)</td>
                  <td>20</td>
                  <td>21</td>
                  <td>29</td>
                  <td>43.60°</td>
                  <td>210</td>
                  <td>6</td>
                </tr>
                <tr>
                  <td>(12, 35, 37)</td>
                  <td>(6, 1)</td>
                  <td>12</td>
                  <td>35</td>
                  <td>37</td>
                  <td>18.92°</td>
                  <td>210</td>
                  <td>5</td>
                </tr>
                <tr>
                  <td>(9, 40, 41)</td>
                  <td>(5, 4)</td>
                  <td>9</td>
                  <td>40</td>
                  <td>41</td>
                  <td>12.68°</td>
                  <td>180</td>
                  <td>4</td>
                </tr>
                <tr>
                  <td>(28, 45, 53)</td>
                  <td>(7, 2)</td>
                  <td>28</td>
                  <td>45</td>
                  <td>53</td>
                  <td>31.89°</td>
                  <td>630</td>
                  <td>10</td>
                </tr>
                <tr>
                  <td>(11, 60, 61)</td>
                  <td>(6, 5)</td>
                  <td>11</td>
                  <td>60</td>
                  <td>61</td>
                  <td>10.39°</td>
                  <td>330</td>
                  <td>5</td>
                </tr>
                <tr>
                  <td>(16, 63, 65)</td>
                  <td>(8, 1)</td>
                  <td>16</td>
                  <td>63</td>
                  <td>65</td>
                  <td>14.25°</td>
                  <td>504</td>
                  <td>7</td>
                </tr>
              </tbody>
            </table>

            <h2>7. Worked Construction Case Study: Building Foundation Squaring & Diagonal Bracing</h2>
            <div class="worked-example-card">
              <div class="example-header">
                <strong>Structural Engineering Case Study:</strong> Commercial Foundation Squaring and Wind-Shear Diagonal Bracing
              </div>
              <div class="example-body">
                <p><strong>Scenario:</strong> A construction superintendent is staking out concrete footings for a rectangular industrial storage building measuring \(W = 24.00\text{ ft}\) along the north-south axis and \(L = 32.00\text{ ft}\) along the east-west axis. The vertical wall height is \(H = 10.00\text{ ft}\). The engineering team must calculate: (1) the corner-to-corner diagonal distance to verify a square \(90^\circ\) foundation before pouring concrete, (2) the length of a steel wind-shear cross-brace installed along the building's exterior diagonal wall, and (3) the 3D space diagonal connecting the bottom northwest corner to the upper southeast corner.</p>

                <p><strong>Step 1: Calculate the Foundation Floor Diagonal (\(c_{\text{floor}}\))</strong><br>
                Treating the rectangular perimeter as two right triangles with legs \(a = 24.00\text{ ft}\) and \(b = 32.00\text{ ft}\):
                $$c_{\text{floor}} = \sqrt{a^2 + b^2} = \sqrt{24^2 + 32^2} = \sqrt{576 + 1024} = \sqrt{1600} = 40.00\text{ ft}$$
                Notice that \((24, 32, 40) = 8 \times (3, 4, 5)\). If the measured tape distance between opposite diagonal stakes equals exactly \(40.00\text{ ft}\), the foundation is verified to be square.</p>

                <p><strong>Step 2: Calculate Exterior Wall Diagonal Bracing Length (\(d_{\text{wall}}\))</strong><br>
                A steel tension strap is bolted diagonally across the long side wall (\(L = 32.00\text{ ft}\), \(H = 10.00\text{ ft}\)):
                $$d_{\text{wall}} = \sqrt{L^2 + H^2} = \sqrt{32^2 + 10^2} = \sqrt{1024 + 100} = \sqrt{1124} \approx 33.526\text{ ft}$$
                The structural steel fabricator must cut the cross-brace to \(33\text{ ft } 6\frac{5}{16}\text{ in}\).</p>

                <p><strong>Step 3: Calculate the 3D Space Diagonal (\(d_{\text{space}}\))</strong><br>
                The 3D vector length spanning the entire interior envelope:
                $$d_{\text{space}} = \sqrt{W^2 + L^2 + H^2} = \sqrt{24^2 + 32^2 + 10^2} = \sqrt{576 + 1024 + 100} = \sqrt{1700} \approx 41.231\text{ ft}$$
                The interior clearance distance from corner to ceiling opposite corner is \(41.23\text{ ft}\).</p>
              </div>
            </div>

            <h2>8. Frequently Asked Questions (FAQ)</h2>
            <div class="faq-accordion">
              <div class="faq-item">
                <h3 class="faq-question">Does the Pythagorean Theorem hold on curved surfaces like the Earth?</h3>
                <div class="faq-answer">
                  <p>No. The Pythagorean theorem is strictly valid in flat Euclidean space. On a sphere (elliptic non-Euclidean geometry), the sum of angles in a triangle exceeds \(180^\circ\), and the relationship is governed by the Spherical Law of Cosines: \(\cos(c/R) = \cos(a/R) \cos(b/R)\), where \(R\) is Earth's radius. For terrestrial triangles on human scales, the Earth's curvature is negligible, so the standard formula provides millimeter-level accuracy.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">What is the converse of the Pythagorean Theorem?</h3>
                <div class="faq-answer">
                  <p>The converse states that if a triangle with sides \(a\), \(b\), and \(c\) satisfies \(a^2 + b^2 = c^2\), then the angle opposite side \(c\) is guaranteed to be an exact \(90^\circ\) right angle. Furthermore, if \(a^2 + b^2 > c^2\), the triangle is <em>acute</em>; if \(a^2 + b^2 < c^2\), the triangle is <em>obtuse</em>.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">Can a right-angled triangle have legs of equal length?</h3>
                <div class="faq-answer">
                  <p>Yes. When \(a = b\), the triangle is an isosceles right triangle (a 45°-45°-90° triangle). In this case, \(c^2 = a^2 + a^2 = 2a^2\), yielding \(c = a\sqrt{2}\). The discovery that the diagonal of a unit square (\(\sqrt{2}\)) cannot be expressed as a ratio of two integers was what historically led the Pythagoreans to the crisis of irrational numbers.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">How does the Pythagorean Theorem relate to the Law of Cosines?</h3>
                <div class="faq-answer">
                  <p>The Law of Cosines is the generalized version of the Pythagorean theorem for any arbitrary triangle: \(c^2 = a^2 + b^2 - 2ab \cos(\gamma)\), where \(\gamma\) is the angle between sides \(a\) and \(b\). When \(\gamma = 90^\circ\), \(\cos(90^\circ) = 0\), causing the \(-2ab \cos(\gamma)\) term to vanish completely, reducing directly back to \(c^2 = a^2 + b^2\).</p>
                </div>
              </div>
            </div>
          </article>
        </div>

        <aside class="sidebar-column">
          <div class="sidebar-card">
            <h3 class="sidebar-title">Related Math Calculators</h3>
            <ul class="sidebar-nav">
              <li><a href="gcd-lcm-calculator.html">GCD and LCM Calculator</a></li>
              <li><a href="quadratic-equation-calculator.html">Quadratic Equation Calculator</a></li>
              <li><a href="scientific-notation-calculator.html">Scientific Notation Calculator</a></li>
              <li><a href="significant-figures-calculator.html">Significant Figures Calculator</a></li>
              <li><a href="prime-number-calculator.html">Prime Number Calculator</a></li>
              <li><a href="fraction-calculator.html">Fraction Calculator</a></li>
              <li><a href="matrix-calculator.html">Matrix Calculator</a></li>
              <li><a href="distance-converter.html">Distance Converter</a></li>
            </ul>
          </div>

          <div class="sidebar-card">
            <h3 class="sidebar-title">Geometric Formulas</h3>
            <div style="font-size:0.875rem; line-height:1.5; color:var(--text-muted, #4b5563);">
              <p><strong>Hypotenuse:</strong> \(c = \sqrt{a^2 + b^2}\)</p>
              <p><strong>Leg:</strong> \(a = \sqrt{c^2 - b^2}\)</p>
              <p><strong>Area:</strong> \(\mathcal{A} = \frac{1}{2}ab\)</p>
              <p><strong>3D Diagonal:</strong> \(d = \sqrt{x^2 + y^2 + z^2}\)</p>
            </div>
          </div>
        </aside>
      </div>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-col">
        <h3>CalcHub</h3>
        <p>High-precision technical calculation engines, engineering references, and discrete mathematical tools.</p>
      </div>
      <div class="footer-col">
        <h4>Navigation</h4>
        <ul>
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="converter.html">Unit Converters</a></li>
          <li><a href="math.html">Math & Engineering</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Legal</h4>
        <ul>
          <li><a href="privacy.html">Privacy Policy</a></li>
          <li><a href="terms.html">Terms of Service</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 CalcHub. All rights reserved. Peer-reviewed computational algorithms.</p>
    </div>
  </footer>

  <script>
    function updateLabels() {
      const mode = document.getElementById('solveForSelect').value;
      const s1Label = document.getElementById('side1Label');
      const s2Label = document.getElementById('side2Label');
      const primLabel = document.getElementById('pythPrimaryLabel');

      if (mode === 'hypotenuse') {
        s1Label.textContent = "Leg a";
        s2Label.textContent = "Leg b";
        primLabel.textContent = "Calculated Hypotenuse (c)";
      } else if (mode === 'legA') {
        s1Label.textContent = "Leg b";
        s2Label.textContent = "Hypotenuse c";
        primLabel.textContent = "Calculated Leg (a)";
      } else {
        s1Label.textContent = "Leg a";
        s2Label.textContent = "Hypotenuse c";
        primLabel.textContent = "Calculated Leg (b)";
      }
      solvePythagoras();
    }

    function solvePythagoras() {
      const mode = document.getElementById('solveForSelect').value;
      const s1 = parseFloat(document.getElementById('side1Input').value);
      const s2 = parseFloat(document.getElementById('side2Input').value);

      if (isNaN(s1) || isNaN(s2) || s1 <= 0 || s2 <= 0) return;

      let a = 0, b = 0, c = 0;
      let primaryVal = 0;
      let radicalExpr = "";
      let steps = "";

      if (mode === 'hypotenuse') {
        a = s1;
        b = s2;
        const cSq = (a * a) + (b * b);
        c = Math.sqrt(cSq);
        primaryVal = c;
        radicalExpr = `Exact form: c = √${cSq.toFixed(2)} = ${c.toFixed(4)}`;
        steps = `1. Formula: c = √(a² + b²)<br>`;
        steps += `2. Substitute: c = √(${a}² + ${b}²)<br>`;
        steps += `3. Square terms: c = √(${ (a*a).toFixed(2) } + ${ (b*b).toFixed(2) }) = √${ cSq.toFixed(2) }<br>`;
        steps += `4. Result: c = ${c.toFixed(4)}`;
      } else if (mode === 'legA') {
        b = s1;
        c = s2;
        if (c <= b) {
          document.getElementById('pythPrimaryResult').textContent = "Error: c must be > b";
          document.getElementById('pythRadicalSubtext').textContent = "Hypotenuse must be longer than leg b";
          return;
        }
        const aSq = (c * c) - (b * b);
        a = Math.sqrt(aSq);
        primaryVal = a;
        radicalExpr = `Exact form: a = √${aSq.toFixed(2)} = ${a.toFixed(4)}`;
        steps = `1. Formula: a = √(c² - b²)<br>`;
        steps += `2. Substitute: a = √(${c}² - ${b}²)<br>`;
        steps += `3. Square terms: a = √(${ (c*c).toFixed(2) } - ${ (b*b).toFixed(2) }) = √${ aSq.toFixed(2) }<br>`;
        steps += `4. Result: a = ${a.toFixed(4)}`;
      } else {
        a = s1;
        c = s2;
        if (c <= a) {
          document.getElementById('pythPrimaryResult').textContent = "Error: c must be > a";
          document.getElementById('pythRadicalSubtext').textContent = "Hypotenuse must be longer than leg a";
          return;
        }
        const bSq = (c * c) - (a * a);
        b = Math.sqrt(bSq);
        primaryVal = b;
        radicalExpr = `Exact form: b = √${bSq.toFixed(2)} = ${b.toFixed(4)}`;
        steps = `1. Formula: b = √(c² - a²)<br>`;
        steps += `2. Substitute: b = √(${c}² - ${a}²)<br>`;
        steps += `3. Square terms: b = √(${ (c*c).toFixed(2) } - ${ (a*a).toFixed(2) }) = √${ bSq.toFixed(2) }<br>`;
        steps += `4. Result: b = ${b.toFixed(4)}`;
      }

      const angleARad = Math.asin(a / c);
      const angleADeg = angleARad * (180 / Math.PI);
      const angleBDeg = 90 - angleADeg;
      const area = 0.5 * a * b;
      const perimeter = a + b + c;
      const altitude = (a * b) / c;
      const inradius = (a + b - c) / 2;

      document.getElementById('pythPrimaryResult').textContent = primaryVal.toFixed(4);
      document.getElementById('pythRadicalSubtext').textContent = radicalExpr;
      document.getElementById('resAngleA').textContent = `${angleADeg.toFixed(2)}° (${angleARad.toFixed(4)} rad)`;
      document.getElementById('resAngleB').textContent = `${angleBDeg.toFixed(2)}°`;
      document.getElementById('resArea').textContent = area.toFixed(4);
      document.getElementById('resPerimeter').textContent = perimeter.toFixed(4);
      document.getElementById('resAltitude').textContent = altitude.toFixed(4);
      document.getElementById('resInradius').textContent = inradius.toFixed(4);
      document.getElementById('pythStepsDisplay').innerHTML = steps;
    }

    document.getElementById('solveForSelect').addEventListener('change', updateLabels);
    document.getElementById('side1Input').addEventListener('input', solvePythagoras);
    document.getElementById('side2Input').addEventListener('input', solvePythagoras);
    updateLabels();
  </script>
</body>
</html>
"""

# -------------------------------------------------------------
# 2. SCIENTIFIC NOTATION CALCULATOR
# -------------------------------------------------------------
sci_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Scientific Notation Calculator — Standard, Engineering & E-Notation | CalcHub</title>
  <meta name="description" content="Convert and perform arithmetic operations in scientific notation (m × 10ⁿ), engineering notation, E-notation, standard decimal format, and SI metric prefixes.">
  <meta name="keywords" content="scientific notation calculator, standard form calculator, engineering notation, e notation, convert to scientific notation, scientific notation multiplication, scientific notation addition, powers of 10">
  <meta name="author" content="CalcHub Scientific Computing & Applied Metrics Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/scientific-notation-calculator.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="Scientific Notation Calculator — Standard, Engineering & E-Notation | CalcHub">
  <meta property="og:description" content="Calculate and convert scientific notation (m × 10ⁿ), engineering format, E-notation, significant figures, and SI prefixes with step-by-step arithmetic.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/scientific-notation-calculator.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/scientific-notation-calculator.html#app",
      "name": "Scientific & Engineering Notation Converter",
      "url": "https://calchub.org/scientific-notation-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "High-precision calculator and converter for standard scientific notation, engineering notation, E-notation, and SI metric prefix scales."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Math & Engineering Calculators", "item": "https://calchub.org/math.html"},
        {"@type": "ListItem", "position": 3, "name": "Scientific Notation Calculator", "item": "https://calchub.org/scientific-notation-calculator.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the difference between scientific notation and engineering notation?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In normalized scientific notation, a number is written as m × 10ⁿ where the significand (mantissa) m satisfies 1 ≤ |m| < 10, and n can be any integer. In engineering notation, the exponent n is strictly constrained to multiples of 3 (e.g., 10³, 10⁶, 10⁻⁹), and the significand satisfies 1 ≤ |m| < 1000. This alignment ensures that engineering notation corresponds directly to standard SI prefixes like micro-, milli-, kilo-, and mega-."
          }
        },
        {
          "@type": "Question",
          "name": "How does E-notation work in programming languages and scientific calculators?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "E-notation (or e-notation) is an alphanumeric shorthand designed for keyboards, text-only consoles, and programming languages (such as C, Python, JavaScript, and FORTRAN) where superscript formatting is unavailable. The letter 'e' or 'E' replaces '× 10^'. For example, 6.022 × 10²³ is written as 6.022e23 or 6.022E+23, and 1.6 × 10⁻¹⁹ is written as 1.6e-19."
          }
        },
        {
          "@type": "Question",
          "name": "How do you multiply and divide numbers in scientific notation?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "To multiply two numbers in scientific notation, multiply their significands and add their exponents: (a × 10ᵖ) × (b × 10ᵍ) = (a × b) × 10ᵖ⁺ᵍ. To divide, divide the significands and subtract the exponents: (a × 10ᵖ) ÷ (b × 10ᵍ) = (a / b) × 10ᵖ⁻ᵍ. In both cases, if the resulting significand does not fall in the range 1 ≤ |m| < 10, shift the decimal point and adjust the exponent accordingly."
          }
        },
        {
          "@type": "Question",
          "name": "How do you add or subtract numbers with different exponents in scientific notation?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Before adding or subtracting, the exponents must be made identical. The standard method converts the number with the smaller exponent to match the larger exponent by shifting its decimal point to the left. Once exponents match, factor out the common power of 10 and perform addition/subtraction on the significands: (a × 10ⁿ) + (b × 10ⁿ) = (a + b) × 10ⁿ."
          }
        }
      ]
    }
  ]
}
  </script>
</head>
<body class="converter-page">
  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="logo">
        <span class="logo-badge">∑</span>
        <span>Calc<span class="accent">Hub</span></span>
      </a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="converter.html">Converters</a>
        <a href="math.html" class="active">Math & Engineering</a>
      </nav>
    </div>
  </header>

  <main class="main-content">
    <div class="container">
      <div class="page-layout">
        <div class="content-column">
          <header class="tool-header">
            <div class="badge-tag">Scientific Computing & Applied Metrics</div>
            <h1 class="tool-title">Scientific Notation Calculator</h1>
            <p class="tool-subtitle">Convert and perform multi-term arithmetic in scientific notation (\(m \times 10^n\)), engineering notation, E-notation, decimal format, and SI metric prefixes.</p>
          </header>

          <section class="calculator-card" aria-label="Scientific Notation Solver">
            <div class="calc-grid">
              <div class="input-group">
                <label for="sciMode" class="input-label">Calculation Mode</label>
                <select id="sciMode" class="calc-input">
                  <option value="convert">Format Converter (Single Number)</option>
                  <option value="arithmetic">Scientific Arithmetic (Two Numbers)</option>
                </select>
              </div>

              <div class="input-group" id="input1Group">
                <label for="numInput1" class="input-label" id="labelNum1">Number (Decimal or e-notation, e.g. 0.00045 or 4.5e-4)</label>
                <input type="text" id="numInput1" class="calc-input" value="149600000000">
              </div>

              <div class="input-group" id="opGroup" style="display:none;">
                <label for="sciOperator" class="input-label">Operator</label>
                <select id="sciOperator" class="calc-input">
                  <option value="mul">Multiply (×)</option>
                  <option value="div">Divide (÷)</option>
                  <option value="add">Add (+)</option>
                  <option value="sub">Subtract (−)</option>
                </select>
              </div>

              <div class="input-group" id="input2Group" style="display:none;">
                <label for="numInput2" class="input-label">Second Number</label>
                <input type="text" id="numInput2" class="calc-input" value="2.99792e8">
              </div>
            </div>

            <div class="primary-result" style="margin-top: 25px;">
              <div class="result-label">Standard Scientific Notation</div>
              <div class="result-value" id="resSciNotation">1.496 × 10¹¹</div>
              <div class="result-subtext" id="resSciSubtext">Significand: 1.496 | Exponent: 11</div>
            </div>

            <div class="results-grid" style="margin-top: 20px;">
              <div class="result-item">
                <div class="result-label">Engineering Notation</div>
                <div class="result-value" id="resEngNotation">149.6 × 10⁹</div>
              </div>
              <div class="result-item">
                <div class="result-label">E-Notation</div>
                <div class="result-value" id="resENotation">1.496e+11</div>
              </div>
              <div class="result-item">
                <div class="result-label">Standard Decimal</div>
                <div class="result-value" id="resDecimal">149,600,000,000</div>
              </div>
              <div class="result-item">
                <div class="result-label">Closest SI Prefix</div>
                <div class="result-value" id="resSIPrefix">149.6 Giga (G)</div>
              </div>
            </div>

            <div class="conversion-steps" style="margin-top: 25px;">
              <h3>Mathematical Breakdown</h3>
              <div id="sciStepsDisplay" style="font-family: monospace; font-size: 0.95rem; line-height: 1.6; background: rgba(0,0,0,0.03); padding: 16px; border-radius: 8px; border-left: 4px solid var(--accent, #2563eb);">
                Loading calculation steps...
              </div>
            </div>
          </section>

          <article class="article-body">
            <h2>1. Purpose and Foundations of Scientific Notation</h2>
            <p>In physical sciences, engineering, astrophysics, and quantum mechanics, numbers span staggering orders of magnitude. The observable universe has an estimated diameter of approximately \(880,000,000,000,000,000,000,000,000\text{ meters}\), while the Planck length—the fundamental quantum limit of spatial measurability—is a minuscule \(0.00000000000000000000000000000000001616\text{ meters}\). Writing, printing, and manipulating such extreme numbers in traditional positional decimal format is inherently prone to transcription errors, cumbersome, and visually unreadable.</p>

            <p><strong>Scientific Notation</strong>—historically termed <em>standard form</em> or <em>exponential notation</em>—solves this problem by decoupling the significant digits of a quantity from its magnitude. Every non-zero real number \(x \in \mathbb{R}\) is uniquely represented in normalized scientific notation as:</p>

            $$x = m \times 10^n$$

            <p>where:</p>
            <ul>
              <li><strong>\(m\) (Significand or Mantissa):</strong> A real decimal number whose absolute value is strictly bounded by \(1 \le |m| < 10\). The sign of \(m\) dictates whether the entire number is positive or negative.</li>
              <li><strong>\(10\) (Radix or Base):</strong> The standard decimal base of numeration.</li>
              <li><strong>\(n\) (Exponent or Order of Magnitude):</strong> An integer (\(n \in \mathbb{Z}\)). A positive exponent (\(n > 0\)) indicates a magnitude greater than or equal to 10; a negative exponent (\(n < 0\)) indicates a fractional magnitude strictly less than 1; and an exponent of zero (\(n = 0\)) indicates a magnitude in the interval \([1, 10)\).</li>
            </ul>

            <h2>2. Comparative Taxonomy: Scientific, Engineering, and E-Notation</h2>
            <p>Modern applied mathematics and computing employ three distinct variations of exponential representation depending on the technical domain:</p>

            <h3>2.1 Normalized Scientific Notation</h3>
            <p>Normalized scientific notation is the universal standard in academic physics, chemistry, and mathematics textbooks. By requiring exactly one non-zero digit to the left of the decimal point (\(1 \le |m| < 10\)), representation is strictly unique. For example, Avogadro's constant is written as \(6.02214076 \times 10^{23}\text{ mol}^{-1}\), and the elementary charge is written as \(1.602176634 \times 10^{-19}\text{ C}\).</p>

            <h3>2.2 Engineering Notation</h3>
            <p>Introduced in electrical and mechanical engineering, <strong>Engineering Notation</strong> constrains the exponent \(n\) to be an exact multiple of 3 (\(n \equiv 0 \pmod 3\)). Consequently, the significand \(m\) spans a wider interval: \(1 \le |m| < 1000\). The primary advantage is that every exponent directly maps onto an official International System of Units (SI) metric prefix:</p>
            <ul>
              <li>\(10^{-12}\): pico- (p)</li>
              <li>\(10^{-9}\): nano- (n)</li>
              <li>\(10^{-6}\): micro- (\(\mu\))</li>
              <li>\(10^{-3}\): milli- (m)</li>
              <li>\(10^3\): kilo- (k)</li>
              <li>\(10^6\): mega- (M)</li>
              <li>\(10^9\): giga- (G)</li>
              <li>\(10^{12}\): tera- (T)</li>
            </ul>
            <p>For example, a frequency of \(45,000,000\text{ Hz}\) is written in scientific notation as \(4.5 \times 10^7\text{ Hz}\), but in engineering notation as \(45 \times 10^6\text{ Hz}\), which immediately translates to \(45\text{ MHz}\).</p>

            <h3>2.3 E-Notation in Computing Systems</h3>
            <p>In software development, ASCII console interfaces, and CSV data files where superscript HTML or typesetting engines are unavailable, <strong>E-notation</strong> replaces the \(\times 10^n\) phrase with the character <code>e</code> or <code>E</code> followed by a signed integer exponent. For instance, \(2.99792 \times 10^8\) is formatted as <code>2.99792e+08</code> or <code>2.99792E8</code>. All major programming languages—including Python, C++, Java, JavaScript, and MATLAB—parse and format IEEE 754 floating-point numbers natively via E-notation.</p>

            <h2>3. Algebraic Operations with Scientific Notation</h2>
            <p>Performing arithmetic on numbers expressed in scientific notation requires strict adherence to exponent laws and significand re-normalization.</p>

            <h3>3.1 Multiplication Law</h3>
            <p>To multiply two quantities in scientific notation, multiply their significands and add their exponents algebraically:</p>

            $$(a \times 10^p) \times (b \times 10^q) = (a \cdot b) \times 10^{p + q}$$

            <p>If the intermediate product \(a \cdot b\) falls outside the normalized interval \([1, 10)\), re-normalize: if \(a \cdot b \ge 10\), divide the mantissa by 10 and add 1 to the exponent: \((a \cdot b) \times 10^{p+q} = \frac{a \cdot b}{10} \times 10^{p+q+1}\).</p>

            <h3>3.2 Division Law</h3>
            <p>To divide two numbers, divide the dividend significand by the divisor significand and subtract the divisor's exponent from the dividend's exponent:</p>

            $$\frac{a \times 10^p}{b \times 10^q} = \left(\frac{a}{b}\right) \times 10^{p - q}$$

            <p>If \(\frac{a}{b} < 1\), multiply the mantissa by 10 and subtract 1 from the exponent: \(\frac{a}{b} \times 10^{p-q} = \left(10 \cdot \frac{a}{b}\right) \times 10^{p-q-1}\).</p>

            <h3>3.3 Addition and Subtraction: Exponent Alignment</h3>
            <p>Unlike multiplication and division, addition and subtraction cannot be executed directly on the significands unless their exponents are identical. Given \(a \times 10^p\) and \(b \times 10^q\) with \(p \ge q\):</p>
            <ol>
              <li>Express \(b \times 10^q\) in terms of base \(10^p\): \(b \times 10^q = (b \times 10^{-(p - q)}) \times 10^p\).</li>
              <li>Factor out the shared power of 10:</li>
            </ol>

            $$(a \times 10^p) \pm (b \times 10^q) = \left[a \pm \left(b \times 10^{-(p - q)}\right)\right] \times 10^p$$

            <p>Once combined, re-normalize the resulting significand if necessary.</p>

            <h2>4. Significant Figures and Elimination of Measurement Ambiguity</h2>
            <p>A crucial pedagogical advantage of scientific notation is the complete elimination of ambiguity regarding <em>trailing zeros</em> in standard decimal notation. For example, if an engineer states that a highway stretch measures \(5,000\text{ meters}\), it is impossible from the decimal representation alone to discern whether the measurement has 1 significant figure (accurate to the nearest 1,000 m), 2 significant figures (accurate to the nearest 100 m), 3 significant figures (accurate to the nearest 10 m), or 4 significant figures (accurate to the exact meter).</p>

            <p>In scientific notation, every recorded digit in the significand \(m\) is explicitly significant:</p>
            <ul>
              <li>\(5 \times 10^3\text{ m}\): Exactly 1 significant figure (uncertainty \(\pm 500\text{ m}\)).</li>
              <li>\(5.0 \times 10^3\text{ m}\): Exactly 2 significant figures (uncertainty \(\pm 50\text{ m}\)).</li>
              <li>\(5.00 \times 10^3\text{ m}\): Exactly 3 significant figures (uncertainty \(\pm 5\text{ m}\)).</li>
              <li>\(5.000 \times 10^3\text{ m}\): Exactly 4 significant figures (uncertainty \(\pm 0.5\text{ m}\)).</li>
            </ul>

            <h2>5. Comprehensive SI Metric Prefixes Table</h2>
            <p>The table below catalogues the complete official International System of Units (SI) prefixes covering 48 orders of magnitude, connecting scientific exponents with their engineering symbols.</p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>SI Prefix</th>
                  <th>Symbol</th>
                  <th>Scientific Power (\(10^n\))</th>
                  <th>Engineering Power</th>
                  <th>Decimal Multiplier</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Yotta</td>
                  <td>Y</td>
                  <td>\(10^{24}\)</td>
                  <td>\(10^{24}\)</td>
                  <td>1,000,000,000,000,000,000,000,000</td>
                </tr>
                <tr>
                  <td>Zetta</td>
                  <td>Z</td>
                  <td>\(10^{21}\)</td>
                  <td>\(10^{21}\)</td>
                  <td>1,000,000,000,000,000,000,000</td>
                </tr>
                <tr>
                  <td>Exa</td>
                  <td>E</td>
                  <td>\(10^{18}\)</td>
                  <td>\(10^{18}\)</td>
                  <td>1,000,000,000,000,000,000</td>
                </tr>
                <tr>
                  <td>Peta</td>
                  <td>P</td>
                  <td>\(10^{15}\)</td>
                  <td>\(10^{15}\)</td>
                  <td>1,000,000,000,000,000</td>
                </tr>
                <tr>
                  <td>Tera</td>
                  <td>T</td>
                  <td>\(10^{12}\)</td>
                  <td>\(10^{12}\)</td>
                  <td>1,000,000,000,000</td>
                </tr>
                <tr>
                  <td>Giga</td>
                  <td>G</td>
                  <td>\(10^9\)</td>
                  <td>\(10^9\)</td>
                  <td>1,000,000,000</td>
                </tr>
                <tr>
                  <td>Mega</td>
                  <td>M</td>
                  <td>\(10^6\)</td>
                  <td>\(10^6\)</td>
                  <td>1,000,000</td>
                </tr>
                <tr>
                  <td>Kilo</td>
                  <td>k</td>
                  <td>\(10^3\)</td>
                  <td>\(10^3\)</td>
                  <td>1,000</td>
                </tr>
                <tr>
                  <td>Milli</td>
                  <td>m</td>
                  <td>\(10^{-3}\)</td>
                  <td>\(10^{-3}\)</td>
                  <td>0.001</td>
                </tr>
                <tr>
                  <td>Micro</td>
                  <td>\(\mu\)</td>
                  <td>\(10^{-6}\)</td>
                  <td>\(10^{-6}\)</td>
                  <td>0.000 001</td>
                </tr>
                <tr>
                  <td>Nano</td>
                  <td>n</td>
                  <td>\(10^{-9}\)</td>
                  <td>\(10^{-9}\)</td>
                  <td>0.000 000 001</td>
                </tr>
                <tr>
                  <td>Pico</td>
                  <td>p</td>
                  <td>\(10^{-12}\)</td>
                  <td>\(10^{-12}\)</td>
                  <td>0.000 000 000 001</td>
                </tr>
                <tr>
                  <td>Femto</td>
                  <td>f</td>
                  <td>\(10^{-15}\)</td>
                  <td>\(10^{-15}\)</td>
                  <td>0.000 000 000 000 001</td>
                </tr>
                <tr>
                  <td>Atto</td>
                  <td>a</td>
                  <td>\(10^{-18}\)</td>
                  <td>\(10^{-18}\)</td>
                  <td>0.000 000 000 000 000 001</td>
                </tr>
              </tbody>
            </table>

            <h2>6. Benchmark Physical Constants in Multiple Notations</h2>
            <p>The following table lists core physical and astronomical constants across scientific notation, engineering notation, E-notation, and traditional decimal values.</p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>Physical Quantity</th>
                  <th>Scientific Notation</th>
                  <th>Engineering Notation</th>
                  <th>E-Notation</th>
                  <th>Standard SI Units</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Speed of Light in Vacuum (\(c\))</td>
                  <td>\(2.99792458 \times 10^8\)</td>
                  <td>\(299.792458 \times 10^6\)</td>
                  <td>2.997925e+08</td>
                  <td>\(\text{m/s}\)</td>
                </tr>
                <tr>
                  <td>Planck's Constant (\(h\))</td>
                  <td>\(6.62607015 \times 10^{-34}\)</td>
                  <td>\(662.607015 \times 10^{-36}\)</td>
                  <td>6.626070e-34</td>
                  <td>\(\text{J}\cdot\text{s}\)</td>
                </tr>
                <tr>
                  <td>Avogadro's Number (\(N_A\))</td>
                  <td>\(6.02214076 \times 10^{23}\)</td>
                  <td>\(602.214076 \times 10^{21}\)</td>
                  <td>6.022141e+23</td>
                  <td>\(\text{mol}^{-1}\)</td>
                </tr>
                <tr>
                  <td>Elementary Charge (\(e\))</td>
                  <td>\(1.60217663 \times 10^{-19}\)</td>
                  <td>\(160.217663 \times 10^{-21}\)</td>
                  <td>1.602177e-19</td>
                  <td>\(\text{C}\)</td>
                </tr>
                <tr>
                  <td>Mass of Electron (\(m_e\))</td>
                  <td>\(9.1093837 \times 10^{-31}\)</td>
                  <td>\(910.93837 \times 10^{-33}\)</td>
                  <td>9.109384e-31</td>
                  <td>\(\text{kg}\)</td>
                </tr>
                <tr>
                  <td>Gravitational Constant (\(G\))</td>
                  <td>\(6.67430 \times 10^{-11}\)</td>
                  <td>\(66.7430 \times 10^{-12}\)</td>
                  <td>6.674300e-11</td>
                  <td>\(\text{m}^3/(\text{kg}\cdot\text{s}^2)\)</td>
                </tr>
                <tr>
                  <td>Mass of the Sun (\(M_\odot\))</td>
                  <td>\(1.98847 \times 10^{30}\)</td>
                  <td>\(1.98847 \times 10^{30}\)</td>
                  <td>1.988470e+30</td>
                  <td>\(\text{kg}\)</td>
                </tr>
                <tr>
                  <td>Astronomical Unit (\(1\text{ AU}\))</td>
                  <td>\(1.4959787 \times 10^{11}\)</td>
                  <td>\(149.59787 \times 10^9\)</td>
                  <td>1.495979e+11</td>
                  <td>\(\text{m}\)</td>
                </tr>
              </tbody>
            </table>

            <h2>7. Worked Physics Case Study: Mass-Energy Equivalence in Antimatter Annihilation</h2>
            <div class="worked-example-card">
              <div class="example-header">
                <strong>Relativistic Physics Case Study:</strong> Total Energy Release in Positron-Electron Annihilation
              </div>
              <div class="example-body">
                <p><strong>Scenario:</strong> In a high-energy particle physics experiment, an antimatter containment trap undergoes controlled annihilation involving \(m_{\text{anti}} = 1.25 \times 10^{-6}\text{ kg}\) of positrons and an equal mass of electrons, for a total annihilated rest mass of \(m_{\text{total}} = 2.50 \times 10^{-6}\text{ kg}\). The research team must compute the released energy using Einstein's relativistic mass-energy relation \(E = m c^2\) in both scientific notation and engineering notation, and convert the output to megajoules (MJ) and kilowatt-hours (kWh).</p>

                <p><strong>Step 1: Define Given Quantities in Scientific Notation</strong><br>
                $$m = 2.50 \times 10^{-6}\text{ kg}$$
                $$c = 2.99792 \times 10^8\text{ m/s}$$</p>

                <p><strong>Step 2: Square the Speed of Light (\(c^2\))</strong><br>
                $$c^2 = (2.99792 \times 10^8)^2 = (2.99792)^2 \times 10^{8 \times 2} = 8.98752 \times 10^{16}\text{ m}^2/\text{s}^2$$</p>

                <p><strong>Step 3: Multiply Mass by \(c^2\)</strong><br>
                $$E = m \cdot c^2 = (2.50 \times 10^{-6}) \times (8.98752 \times 10^{16})$$
                Multiply the mantissas:
                $$2.50 \times 8.98752 = 22.4688$$
                Add the exponents:
                $$-6 + 16 = 10$$
                Thus, the intermediate result is:
                $$E = 22.4688 \times 10^{10}\text{ Joules}$$</p>

                <p><strong>Step 4: Re-Normalize to Standard Scientific Notation</strong><br>
                Because \(22.4688 \ge 10\), shift the decimal point one place to the left and increment the exponent by 1:
                $$E = 2.24688 \times 10^{11}\text{ Joules}$$</p>

                <p><strong>Step 5: Convert to Engineering Notation and Practical Energy Units</strong><br>
                To express in engineering notation (\(n \pmod 3 = 0\)), choose exponent \(10^9\) (Giga):
                $$E = 224.688 \times 10^9\text{ J} = 224.688\text{ Gigajoules (GJ)}$$
                In megajoules (\(10^6\text{ J}\)):
                $$E = 224,688\text{ MJ}$$
                In kilowatt-hours (\(1\text{ kWh} = 3.60 \times 10^6\text{ J}\)):
                $$E = \frac{2.24688 \times 10^{11}\text{ J}}{3.60 \times 10^6\text{ J/kWh}} \approx 6.2413 \times 10^4\text{ kWh} = 62,413\text{ kWh}$$
                A tiny mass of 2.5 milligrams yields over 62,400 kilowatt-hours of electrical energy equivalent.</p>
              </div>
            </div>

            <h2>8. Frequently Asked Questions (FAQ)</h2>
            <div class="faq-accordion">
              <div class="faq-item">
                <h3 class="faq-question">What is the scientific notation for zero?</h3>
                <div class="faq-answer">
                  <p>In pure mathematics, zero cannot be expressed in strict normalized scientific notation because no non-zero digit exists for the leading mantissa (\(1 \le |m| < 10\)). By conventional consensus in computer science and calculators, zero is represented simply as \(0\), \(0 \times 10^0\), or <code>0.0e+00</code>.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">Why does multiplying numbers in scientific notation add the exponents?</h3>
                <div class="faq-answer">
                  <p>This follows directly from the fundamental exponent law: \(10^p \times 10^q = 10^{p+q}\). Because powers represent repeated multiplication (e.g., \(10^3 = 10 \times 10 \times 10\)), multiplying \(10^3\) by \(10^4\) combines three tens with four tens, yielding seven tens multiplied together (\(10^7\)).</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">What is normalized versus unnormalized scientific notation?</h3>
                <div class="faq-answer">
                  <p>In normalized notation, the significand \(m\) must satisfy \(1 \le |m| < 10\) (having exactly one non-zero digit before the decimal point). In unnormalized (or loose) scientific notation, this restriction is relaxed (for example, \(0.45 \times 10^6\) or \(450 \times 10^3\)). While mathematically equal, unnormalized forms are avoided in standardized scientific literature to prevent ambiguity.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">How does binary floating-point representation compare to decimal scientific notation?</h3>
                <div class="faq-answer">
                  <p>Computers represent real numbers using the IEEE 754 standard, which is binary scientific notation: \((-1)^s \times (1.f)_2 \times 2^{e - \text{bias}}\). Instead of powers of 10, binary scientific notation uses powers of 2. The significand is normalized with a leading binary bit of 1, which is often omitted in hardware registers (the 'hidden bit') to maximize floating-point precision.</p>
                </div>
              </div>
            </div>
          </article>
        </div>

        <aside class="sidebar-column">
          <div class="sidebar-card">
            <h3 class="sidebar-title">Related Math Calculators</h3>
            <ul class="sidebar-nav">
              <li><a href="significant-figures-calculator.html">Significant Figures Calculator</a></li>
              <li><a href="gcd-lcm-calculator.html">GCD and LCM Calculator</a></li>
              <li><a href="quadratic-equation-calculator.html">Quadratic Equation Calculator</a></li>
              <li><a href="pythagorean-theorem-calculator.html">Pythagorean Theorem Calculator</a></li>
              <li><a href="prime-number-calculator.html">Prime Number Calculator</a></li>
              <li><a href="fraction-calculator.html">Fraction Calculator</a></li>
              <li><a href="percentage-calculator.html">Percentage Calculator</a></li>
              <li><a href="number-base-converter.html">Number Base Converter</a></li>
            </ul>
          </div>

          <div class="sidebar-card">
            <h3 class="sidebar-title">Scientific Notation Laws</h3>
            <div style="font-size:0.875rem; line-height:1.5; color:var(--text-muted, #4b5563);">
              <p><strong>Form:</strong> \(m \times 10^n \quad (1 \le |m| < 10)\)</p>
              <p><strong>Multiply:</strong> \((a \cdot 10^p)(b \cdot 10^q) = (ab) \cdot 10^{p+q}\)</p>
              <p><strong>Divide:</strong> \((a \cdot 10^p)/(b \cdot 10^q) = (a/b) \cdot 10^{p-q}\)</p>
              <p><strong>Eng. Rule:</strong> \(n \bmod 3 = 0\)</p>
            </div>
          </div>
        </aside>
      </div>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-col">
        <h3>CalcHub</h3>
        <p>High-precision technical calculation engines, engineering references, and discrete mathematical tools.</p>
      </div>
      <div class="footer-col">
        <h4>Navigation</h4>
        <ul>
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="converter.html">Unit Converters</a></li>
          <li><a href="math.html">Math & Engineering</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Legal</h4>
        <ul>
          <li><a href="privacy.html">Privacy Policy</a></li>
          <li><a href="terms.html">Terms of Service</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 CalcHub. All rights reserved. Peer-reviewed computational algorithms.</p>
    </div>
  </footer>

  <script>
    const SI_PREFIXES = [
      { exp: 24, name: "Yotta", sym: "Y" },
      { exp: 21, name: "Zetta", sym: "Z" },
      { exp: 18, name: "Exa", sym: "E" },
      { exp: 15, name: "Peta", sym: "P" },
      { exp: 12, name: "Tera", sym: "T" },
      { exp: 9,  name: "Giga", sym: "G" },
      { exp: 6,  name: "Mega", sym: "M" },
      { exp: 3,  name: "Kilo", sym: "k" },
      { exp: 0,  name: "", sym: "" },
      { exp: -3, name: "Milli", sym: "m" },
      { exp: -6, name: "Micro", sym: "μ" },
      { exp: -9, name: "Nano", sym: "n" },
      { exp: -12, name: "Pico", sym: "p" },
      { exp: -15, name: "Femto", sym: "f" },
      { exp: -18, name: "Atto", sym: "a" },
      { exp: -21, name: "Zepto", sym: "z" },
      { exp: -24, name: "Yocto", sym: "y" }
    ];

    function toScientific(val) {
      if (val === 0) return { m: 0, n: 0 };
      const sign = val < 0 ? -1 : 1;
      const absVal = Math.abs(val);
      const n = Math.floor(Math.log10(absVal));
      const m = (sign * absVal) / Math.pow(10, n);
      return { m: m, n: n };
    }

    function toEngineering(val) {
      if (val === 0) return { m: 0, n: 0 };
      const sci = toScientific(val);
      let engN = Math.floor(sci.n / 3) * 3;
      let engM = val / Math.pow(10, engN);
      return { m: engM, n: engN };
    }

    function formatNumberSci(num) {
      if (num === 0) return "0";
      const sci = toScientific(num);
      return `${sci.m.toFixed(5)} × 10^{${sci.n}}`;
    }

    function updateUiMode() {
      const mode = document.getElementById('sciMode').value;
      const isArith = mode === 'arithmetic';
      document.getElementById('opGroup').style.display = isArith ? 'block' : 'none';
      document.getElementById('input2Group').style.display = isArith ? 'block' : 'none';
      document.getElementById('labelNum1').textContent = isArith ? "First Number" : "Number (Decimal or e-notation, e.g. 0.00045 or 4.5e-4)";
      computeSci();
    }

    function computeSci() {
      const mode = document.getElementById('sciMode').value;
      const input1Str = document.getElementById('numInput1').value.trim();
      const val1 = parseFloat(input1Str);

      if (isNaN(val1)) return;

      let resultVal = val1;
      let stepsHtml = "";

      if (mode === 'arithmetic') {
        const input2Str = document.getElementById('numInput2').value.trim();
        const val2 = parseFloat(input2Str);
        if (isNaN(val2)) return;

        const op = document.getElementById('sciOperator').value;
        const sci1 = toScientific(val1);
        const sci2 = toScientific(val2);

        stepsHtml += `Term 1: ${sci1.m.toFixed(4)} × 10^(${sci1.n})<br>`;
        stepsHtml += `Term 2: ${sci2.m.toFixed(4)} × 10^(${sci2.n})<br><br>`;

        if (op === 'mul') {
          resultVal = val1 * val2;
          const rawM = sci1.m * sci2.m;
          const rawN = sci1.n + sci2.n;
          stepsHtml += `Multiplication: (${sci1.m.toFixed(4)} × ${sci2.m.toFixed(4)}) × 10^(${sci1.n} + ${sci2.n})<br>`;
          stepsHtml += `= ${rawM.toFixed(4)} × 10^(${rawN})<br>`;
        } else if (op === 'div') {
          if (val2 === 0) {
            document.getElementById('resSciNotation').textContent = "Error: Division by 0";
            return;
          }
          resultVal = val1 / val2;
          const rawM = sci1.m / sci2.m;
          const rawN = sci1.n - sci2.n;
          stepsHtml += `Division: (${sci1.m.toFixed(4)} ÷ ${sci2.m.toFixed(4)}) × 10^(${sci1.n} - ${sci2.n})<br>`;
          stepsHtml += `= ${rawM.toFixed(4)} × 10^(${rawN})<br>`;
        } else if (op === 'add') {
          resultVal = val1 + val2;
          stepsHtml += `Addition: Aligning exponents to higher power...<br>`;
          stepsHtml += `= (${val1.toExponential(4)}) + (${val2.toExponential(4)})<br>`;
        } else if (op === 'sub') {
          resultVal = val1 - val2;
          stepsHtml += `Subtraction: Aligning exponents to higher power...<br>`;
          stepsHtml += `= (${val1.toExponential(4)}) - (${val2.toExponential(4)})<br>`;
        }
      } else {
        stepsHtml += `Single Number Conversion:<br>`;
        stepsHtml += `Original Input: ${input1Str}<br>`;
      }

      const sci = toScientific(resultVal);
      const eng = toEngineering(resultVal);

      // Closest SI prefix
      let closestSI = SI_PREFIXES.find(p => p.exp === eng.n);
      let siText = closestSI && closestSI.sym !== ""
        ? `${eng.m.toFixed(4)} ${closestSI.name} (${closestSI.sym})`
        : `${eng.m.toFixed(4)} × 10^(${eng.n})`;

      const supMap = {
        '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
        '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '-': '⁻'
      };
      const nStr = String(sci.n).split('').map(c => supMap[c] || c).join('');
      const engNStr = String(eng.n).split('').map(c => supMap[c] || c).join('');

      document.getElementById('resSciNotation').textContent = resultVal === 0 ? "0" : `${sci.m.toFixed(5)} × 10${nStr}`;
      document.getElementById('resSciSubtext').textContent = `Significand: ${sci.m.toFixed(5)} | Exponent: ${sci.n}`;
      document.getElementById('resEngNotation').textContent = resultVal === 0 ? "0" : `${eng.m.toFixed(4)} × 10${engNStr}`;
      document.getElementById('resENotation').textContent = resultVal.toExponential(5);
      
      let decStr = Math.abs(resultVal) < 1e15 && Math.abs(resultVal) > 1e-6
        ? resultVal.toLocaleString('en-US', { maximumFractionDigits: 8 })
        : resultVal.toString();
      document.getElementById('resDecimal').textContent = decStr;
      document.getElementById('resSIPrefix').textContent = siText;

      stepsHtml += `<br><strong>Final Normalized Scientific Form:</strong> ${sci.m.toFixed(5)} × 10^(${sci.n})<br>`;
      stepsHtml += `<strong>Engineering Form:</strong> ${eng.m.toFixed(4)} × 10^(${eng.n})`;
      document.getElementById('sciStepsDisplay').innerHTML = stepsHtml;
    }

    document.getElementById('sciMode').addEventListener('change', updateUiMode);
    document.getElementById('sciOperator').addEventListener('change', computeSci);
    document.getElementById('numInput1').addEventListener('input', computeSci);
    document.getElementById('numInput2').addEventListener('input', computeSci);
    updateUiMode();
  </script>
</body>
</html>
"""

# Write files
with open(os.path.join(BASE_DIR, 'pythagorean-theorem-calculator.html'), 'w', encoding='utf-8') as f:
    f.write(pyth_html)
print("Generated pythagorean-theorem-calculator.html successfully!")

with open(os.path.join(BASE_DIR, 'scientific-notation-calculator.html'), 'w', encoding='utf-8') as f:
    f.write(sci_html)
print("Generated scientific-notation-calculator.html successfully!")
