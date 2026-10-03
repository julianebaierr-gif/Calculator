import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 1. ABSOLUTE VALUE CALCULATOR
# -------------------------------------------------------------
abs_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Absolute Value Calculator — Real Modulus, Complex Norm & Distance | CalcHub</title>
  <meta name="description" content="Calculate absolute value |x|, complex modulus |a + bi|, Euclidean vector norms, piecewise equations, distance on number lines, and triangle inequality proofs.">
  <meta name="keywords" content="absolute value calculator, modulus calculator, complex number modulus, distance on number line, triangle inequality, absolute value equations, L1 norm, magnitude of number">
  <meta name="author" content="CalcHub Real Analysis & Analytical Geometry Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/absolute-value-calculator.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="Absolute Value Calculator — Real Modulus, Complex Norm & Distance | CalcHub">
  <meta property="og:description" content="Compute real and complex absolute values, distance between numbers, piece-wise algebraic equations, and vector magnitude.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/absolute-value-calculator.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/absolute-value-calculator.html#app",
      "name": "Absolute Value & Modulus Solver",
      "url": "https://calchub.org/absolute-value-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "High-precision calculator for absolute value of real numbers, complex moduli |a + bi|, 1D Euclidean distance, and vector norms."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Math & Engineering Calculators", "item": "https://calchub.org/math.html"},
        {"@type": "ListItem", "position": 3, "name": "Absolute Value Calculator", "item": "https://calchub.org/absolute-value-calculator.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the formal mathematical definition of the absolute value function?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The absolute value (or modulus) of a real number x, denoted |x|, is defined piece-wise as |x| = x when x ≥ 0, and |x| = -x when x < 0. Equivalently in real analysis, it can be defined algebraically as the principal non-negative square root of x squared: |x| = √(x²). Geometrically, |x| represents the non-directional Euclidean distance between the coordinate x and the origin (0) along the one-dimensional real number line."
          }
        },
        {
          "@type": "Question",
          "name": "How is the absolute value of a complex number (z = a + bi) evaluated?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "For a complex number z = a + bi (where a and b are real numbers and i = √(-1)), the absolute value is called the modulus or complex magnitude. Geometrically, it represents the straight-line Euclidean distance from the origin (0, 0) to the point (a, b) in the complex Argand plane. Applying the Pythagorean theorem yields: |z| = √(a² + b²) = √(z · z*), where z* = a - bi is the complex conjugate of z."
          }
        },
        {
          "@type": "Question",
          "name": "What is the Triangle Inequality and why is it essential across mathematics?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The Triangle Inequality states that for any two real or complex numbers x and y, |x + y| ≤ |x| + |y|. Geometrically, it asserts that the length of any side of a triangle cannot exceed the sum of the lengths of the other two sides. In mathematical analysis, functional analysis, and topology, the triangle inequality is one of the mandatory axioms defining any valid metric space and normed vector space."
          }
        },
        {
          "@type": "Question",
          "name": "Is the absolute value function differentiable everywhere in calculus?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. The absolute value function f(x) = |x| is continuous everywhere on the real line (-∞, +∞), but it is not differentiable at x = 0. As x approaches 0 from the right, the derivative limit is +1; as x approaches 0 from the left, the derivative limit is -1. Because the one-sided limits disagree at x = 0 (forming a sharp geometric cusp or corner), f'(0) does not exist. For all x ≠ 0, the derivative is f'(x) = x / |x| = sgn(x)."
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
            <div class="badge-tag">Real Analysis & Metric Spaces</div>
            <h1 class="tool-title">Absolute Value Calculator</h1>
            <p class="tool-subtitle">Calculate real modulus \(|x|\), complex plane magnitude \(|a + bi|\), number line distance \(|x - y|\), and explore metric properties and vector norms.</p>
          </header>

          <section class="calculator-card" aria-label="Absolute Value Solver">
            <div class="calc-grid">
              <div class="input-group">
                <label for="absMode" class="input-label">Analysis Mode</label>
                <select id="absMode" class="calc-input">
                  <option value="real">Real Number Modulus |x|</option>
                  <option value="distance">Distance Between Two Points |x - y|</option>
                  <option value="complex">Complex Number Modulus |a + bi|</option>
                </select>
              </div>

              <div class="input-group" id="inputXGroup">
                <label for="valX" class="input-label" id="labelValX">Value (x)</label>
                <input type="number" id="valX" class="calc-input" value="-42.75" step="any">
              </div>

              <div class="input-group" id="inputYGroup" style="display:none;">
                <label for="valY" class="input-label" id="labelValY">Second Value (y)</label>
                <input type="number" id="valY" class="calc-input" value="18.5" step="any">
              </div>
            </div>

            <div class="primary-result" style="margin-top: 25px;">
              <div class="result-label" id="absPrimaryLabel">Absolute Value |x|</div>
              <div class="result-value" id="absPrimaryResult">42.75</div>
              <div class="result-subtext" id="absSubtext">Distance from origin: |-42.75| = 42.75</div>
            </div>

            <div class="results-grid" style="margin-top: 20px;">
              <div class="result-item">
                <div class="result-label">Signum / Sign Function \(\operatorname{sgn}(x)\)</div>
                <div class="result-value" id="resSignum">-1 (Negative)</div>
              </div>
              <div class="result-item">
                <div class="result-label">Squared Modulus \(|x|^2\)</div>
                <div class="result-value" id="resSqMod">1,827.5625</div>
              </div>
              <div class="result-item">
                <div class="result-label">Opposite Value \(-x\)</div>
                <div class="result-value" id="resOpposite">42.75</div>
              </div>
              <div class="result-item">
                <div class="result-label">Algebraic Form</div>
                <div class="result-value" id="resAlgForm">\(\sqrt{(-42.75)^2}\)</div>
              </div>
            </div>

            <div class="conversion-steps" style="margin-top: 25px;">
              <h3>Mathematical &amp; Metric Resolution</h3>
              <div id="absStepsDisplay" style="font-family: monospace; font-size: 0.95rem; line-height: 1.6; background: rgba(0,0,0,0.03); padding: 16px; border-radius: 8px; border-left: 4px solid var(--accent, #2563eb);">
                Loading mathematical breakdown...
              </div>
            </div>
          </section>

          <article class="article-body">
            <h2>1. Foundations and Formal Definition of Absolute Value</h2>
            <p>In classical mathematical analysis, algebra, and topology, the concept of magnitude divorced from direction is formalized through the <strong>absolute value function</strong> (traditionally termed the <em>modulus</em> in European mathematical literature). Introduced symbolically by German mathematician Karl Weierstrass in 1841 using vertical bars \(|x|\), the function provides the foundational definition of metric distance across Euclidean spaces.</p>

            <p>For any real number \(x \in \mathbb{R}\), the absolute value is defined piece-wise by the piecewise linear rule:</p>

            $$|x| = \begin{cases} x & \text{if } x \ge 0 \\ -x & \text{if } x < 0 \end{cases}$$

            <p>Under this definition, the absolute value of a positive number or zero is identically itself (\(|7| = 7\), \(|0| = 0\)), whereas the absolute value of a negative number negates the negative sign, yielding a strictly non-negative magnitude (\(|-7| = -(-7) = 7\)). Consequently, for all real \(x\), the absolute value satisfies the non-negativity axiom: \(|x| \ge 0\), with \(|x| = 0 \iff x = 0\).</p>

            <h3>1.1 Algebraic Radical Formulation</h3>
            <p>An alternative, purely algebraic definition of absolute value that avoids piecewise piecewise conditional logic defines \(|x|\) as the principal (positive) square root of the square of \(x\):</p>

            $$|x| = \sqrt{x^2}$$

            <p>This identity reinforces a critical axiom in elementary algebra often misunderstood by students: \(\sqrt{x^2}\) does <em>not</em> equal \(x\); rather, it equals \(|x|\). For instance, \(\sqrt{(-5)^2} = \sqrt{25} = +5 = |-5|\).</p>

            <h2>2. Geometrical Interpretation: The 1D Euclidean Metric</h2>
            <p>Geometrically, the real number line \(\mathbb{R}\) is a one-dimensional metric space. The absolute value of a single coordinate \(|x|\) represents the geometric distance between the point \(x\) and the origin \(0\). Because physical distance cannot be negative, \(|x|\) is inherently scalar and positive.</p>

            <h3>2.1 Distance Between Two Coordinates</h3>
            <p>Given any two arbitrary points \(x, y \in \mathbb{R}\), the Euclidean distance \(d(x, y)\) separating them along the real number line is defined by:</p>

            $$d(x, y) = |x - y| = |y - x|$$

            <p>Because \(|x - y| = |-(y - x)| = |y - x|\), metric distance is inherently symmetric: the distance from point \(A\) to point \(B\) is identical to the distance from \(B\) to \(A\). For example, if temperature drops from \(15^\circ\text{C}\) to \(-8^\circ\text{C}\), the total temperature shift magnitude is \(|15 - (-8)| = |15 + 8| = 23^\circ\text{C}\).</p>

            <h2>3. Fundamental Algebraic Properties and Axioms</h2>
            <p>The absolute value satisfies four core algebraic axioms that establish it as a formal norm on the field of real numbers:</p>
            <ol>
              <li><strong>Non-negativity:</strong> \(|x| \ge 0\) for all \(x \in \mathbb{R}\).</li>
              <li><strong>Positive Definiteness:</strong> \(|x| = 0\) if and only if \(x = 0\).</li>
              <li><strong>Multiplicativity:</strong> \(|x \cdot y| = |x| \cdot |y|\), and for \(y \neq 0\), \(\left|\frac{x}{y}\right| = \frac{|x|}{|y|}\).</li>
              <li><strong>Subadditivity (The Triangle Inequality):</strong> \(|x + y| \le |x| + |y|\).</li>
            </ol>

            <h3>3.1 The Triangle Inequality and Reverse Triangle Inequality</h3>
            <p>The <strong>Triangle Inequality</strong> is arguably the most indispensable inequality in mathematical analysis. It dictates that the magnitude of a sum cannot exceed the sum of the individual magnitudes:</p>

            $$|x + y| \le |x| + |y|$$

            <p>Equality holds (\(|x + y| = |x| + |y|\)) if and only if \(x\) and \(y\) share the same sign (\(x \cdot y \ge 0\)). If \(x\) and \(y\) possess opposite signs, internal cancellation occurs, making \(|x + y|\) strictly smaller than \(|x| + |y|\) (e.g., \(|5 + (-3)| = |2| = 2 < |5| + |-3| = 5 + 3 = 8\)).</p>

            <p>From the standard inequality, one derives the <strong>Reverse Triangle Inequality</strong>, which provides a lower bound on the difference between magnitudes:</p>

            $$\big||x| - |y|\big| \le |x - y|$$

            <p>This relationship is paramount when proving the continuity of functions and establishing convergence criteria in calculus \(\epsilon\)-\(\delta\) proofs.</p>

            <h2>4. Calculus of the Absolute Value: Non-Differentiability at the Origin</h2>
            <p>In differential calculus, the absolute value function \(f(x) = |x|\) serves as the classic counterexample demonstrating that continuity does not imply differentiability.</p>

            <h3>4.1 Derivative Analysis and the Signum Function</h3>
            <p>For all non-zero values of \(x\) (\(x \neq 0\)), the function is differentiable. Using the radical form \(f(x) = \sqrt{x^2}\) and applying the chain rule:</p>

            $$f'(x) = \frac{d}{dx}\left(\sqrt{x^2}\right) = \frac{1}{2\sqrt{x^2}} \cdot 2x = \frac{x}{|x|} = \operatorname{sgn}(x)$$

            <p>where \(\operatorname{sgn}(x)\) is the <strong>signum function</strong>:</p>

            $$\operatorname{sgn}(x) = \begin{cases} +1 & \text{if } x > 0 \\ -1 & \text{if } x < 0 \end{cases}$$

            <h3>4.2 Singularity at \(x = 0\)</h3>
            <p>At \(x = 0\), the derivative fails to exist. Evaluating the difference quotient via one-sided limits:</p>

            $$\lim_{h \to 0^+} \frac{f(0 + h) - f(0)}{h} = \lim_{h \to 0^+} \frac{|h| - 0}{h} = \lim_{h \to 0^+} \frac{h}{h} = +1$$

            $$\lim_{h \to 0^-} \frac{f(0 + h) - f(0)}{h} = \lim_{h \to 0^-} \frac{|h| - 0}{h} = \lim_{h \to 0^-} \frac{-h}{h} = -1$$

            <p>Because the left-hand limit (\(-1\)) and right-hand limit (\(+1\)) are unequal, the two-sided limit does not exist. Geometrically, the graph of \(y = |x|\) forms a sharp \(90^\circ\) corner (cusp) at the origin \((0, 0)\). In optimization theory, algorithms optimizing functions with absolute value terms (such as \(L_1\) regularization in machine learning Lasso regression) must utilize <em>subgradient calculus</em> rather than standard gradient descent.</p>

            <h2>5. Extension to Complex Numbers: The Modulus in the Argand Plane</h2>
            <p>When extending numbers into the complex domain \(\mathbb{C}\), let \(z = a + bi\) be a complex number, where \(a = \operatorname{Re}(z)\) is the real component, \(b = \operatorname{Im}(z)\) is the imaginary component, and \(i^2 = -1\).</p>

            <p>The absolute value of \(z\), termed its <strong>modulus</strong>, is defined as the Euclidean distance from the origin \((0, 0)\) to the point \((a, b)\) in the complex Argand plane:</p>

            $$|z| = |a + bi| = \sqrt{a^2 + b^2}$$

            <p>In terms of the complex conjugate \(z^* = a - bi\), the modulus satisfies the profound algebraic identity:</p>

            $$|z|^2 = z \cdot z^* = (a + bi)(a - bi) = a^2 - (bi)^2 = a^2 + b^2 \implies |z| = \sqrt{z \cdot z^*}$$

            <p>In polar form, writing \(z = r e^{i\theta} = r(\cos\theta + i\sin\theta)\), the modulus is simply the radial distance: \(|z| = r\).</p>

            <h2>6. Multidimensional Vector Norms: \(L_1\), \(L_2\), and \(L_\infty\)</h2>
            <p>In linear algebra and data science, the absolute value generalizes into vector norms across \(n\)-dimensional spaces \(\mathbb{R}^n\) for vector \(\mathbf{x} = (x_1, x_2, \dots, x_n)\):</p>
            <ul>
              <li><strong>\(L_1\) Norm (Manhattan / Taxicab Norm):</strong> Sum of absolute values:
                $$\|\mathbf{x}\|_1 = \sum_{i=1}^n |x_i| = |x_1| + |x_2| + \dots + |x_n|$$
                Used in robust statistics and compressed sensing.</li>
              <li><strong>\(L_2\) Norm (Euclidean Norm):</strong> Straight-line vector magnitude:
                $$\|\mathbf{x}\|_2 = \sqrt{\sum_{i=1}^n x_i^2} = \sqrt{x_1^2 + x_2^2 + \dots + x_n^2}$$</li>
              <li><strong>\(L_\infty\) Norm (Chebyshev / Maximum Norm):</strong> Maximum absolute component:
                $$\|\mathbf{x}\|_\infty = \max(|x_1|, |x_2|, \dots, |x_n|)$$</li>
            </ul>

            <h2>7. Benchmark Comparative Reference Table</h2>
            <p>The table below catalogues benchmark real and complex values, illustrating their absolute values, squared moduli, signum values, and algebraic expressions.</p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>Input Value</th>
                  <th>Domain</th>
                  <th>Absolute Value / Modulus</th>
                  <th>Squared Modulus</th>
                  <th>Signum / Direction</th>
                  <th>Algebraic Radical Form</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>\(-42.75\)</td>
                  <td>Real (\(\mathbb{R}\))</td>
                  <td>\(42.75\)</td>
                  <td>\(1,827.5625\)</td>
                  <td>\(-1\)</td>
                  <td>\(\sqrt{(-42.75)^2}\)</td>
                </tr>
                <tr>
                  <td>\(+128.5\)</td>
                  <td>Real (\(\mathbb{R}\))</td>
                  <td>\(128.5\)</td>
                  <td>\(16,512.25\)</td>
                  <td>\(+1\)</td>
                  <td>\(\sqrt{(128.5)^2}\)</td>
                </tr>
                <tr>
                  <td>\(0\)</td>
                  <td>Real (\(\mathbb{R}\))</td>
                  <td>\(0\)</td>
                  <td>\(0\)</td>
                  <td>\(0\)</td>
                  <td>\(\sqrt{0^2}\)</td>
                </tr>
                <tr>
                  <td>\(3 + 4i\)</td>
                  <td>Complex (\(\mathbb{C}\))</td>
                  <td>\(5.000\)</td>
                  <td>\(25.0\)</td>
                  <td>\(\angle 53.13^\circ\)</td>
                  <td>\(\sqrt{3^2 + 4^2} = \sqrt{25}\)</td>
                </tr>
                <tr>
                  <td>\(-5 + 12i\)</td>
                  <td>Complex (\(\mathbb{C}\))</td>
                  <td>\(13.000\)</td>
                  <td>\(169.0\)</td>
                  <td>\(\angle 112.62^\circ\)</td>
                  <td>\(\sqrt{(-5)^2 + 12^2} = \sqrt{169}\)</td>
                </tr>
                <tr>
                  <td>\(-7.071\)</td>
                  <td>Real (\(\mathbb{R}\))</td>
                  <td>\(7.071\)</td>
                  <td>\(50.000\)</td>
                  <td>\(-1\)</td>
                  <td>\(\sqrt{(-7.071)^2}\)</td>
                </tr>
                <tr>
                  <td>\(1 - i\)</td>
                  <td>Complex (\(\mathbb{C}\))</td>
                  <td>\(\sqrt{2} \approx 1.414\)</td>
                  <td>\(2.0\)</td>
                  <td>\(\angle -45.0^\circ\)</td>
                  <td>\(\sqrt{1^2 + (-1)^2} = \sqrt{2}\)</td>
                </tr>
                <tr>
                  <td>\(-1000\)</td>
                  <td>Real (\(\mathbb{R}\))</td>
                  <td>\(1,000\)</td>
                  <td>\(1,000,000\)</td>
                  <td>\(-1\)</td>
                  <td>\(\sqrt{(-1000)^2}\)</td>
                </tr>
              </tbody>
            </table>

            <h2>8. Worked Engineering Case Study: Error Tolerancing & Deviation Limits</h2>
            <div class="worked-example-card">
              <div class="example-header">
                <strong>Precision Manufacturing Case Study:</strong> CNC Turbine Shaft Runout Tolerancing
              </div>
              <div class="example-body">
                <p><strong>Scenario:</strong> An aerospace quality assurance engineer inspects a precision high-pressure turbine drive shaft. The blueprint nominal outer diameter is \(D_{\text{nominal}} = 75.000\text{ mm}\) with a strict bilateral dimensional tolerance of \(\pm 0.025\text{ mm}\). A laser micrometer records an actual measured diameter of \(D_{\text{measured}} = 74.968\text{ mm}\). The engineer must: (1) express the dimensional acceptance criteria as a formal absolute value inequality, (2) calculate the absolute error deviation, and (3) determine whether the shaft passes or requires rejection.</p>

                <p><strong>Step 1: Formulate the Absolute Value Tolerance Inequality</strong><br>
                A fabricated part satisfies specification if and only if the absolute deviation between actual and nominal diameter does not exceed the maximum allowable tolerance \(\delta = 0.025\text{ mm}\):
                $$|D_{\text{measured}} - D_{\text{nominal}}| \le 0.025\text{ mm}$$
                Expanding this absolute value inequality produces the two-sided acceptable interval:
                $$-0.025 \le D_{\text{measured}} - 75.000 \le +0.025$$
                $$74.975\text{ mm} \le D_{\text{measured}} \le 75.025\text{ mm}$$</p>

                <p><strong>Step 2: Calculate Actual Absolute Deviation</strong><br>
                $$|D_{\text{measured}} - D_{\text{nominal}}| = |74.968 - 75.000| = |-0.032\text{ mm}| = 0.032\text{ mm}$$</p>

                <p><strong>Step 3: Quality Control Verdict</strong><br>
                Comparing the observed deviation against the specification limit:
                $$0.032\text{ mm} > 0.025\text{ mm}$$
                The absolute error exceeds allowable tolerance by \(0.032 - 0.025 = 0.007\text{ mm}\) (\(7\text{ }\mu\text{m}\)). The turbine shaft fails inspection and is routed for CNC re-machining.</p>
              </div>
            </div>

            <h2>9. Frequently Asked Questions (FAQ)</h2>
            <div class="faq-accordion">
              <div class="faq-item">
                <h3 class="faq-question">How do you solve equations involving absolute values, such as |2x - 3| = 7?</h3>
                <div class="faq-answer">
                  <p>An equation of the form \(|A| = B\) (where \(B \ge 0\)) splits into two separate linear branches: \(A = B\) or \(A = -B\). For \(|2x - 3| = 7\):
                  Branch 1: \(2x - 3 = 7 \implies 2x = 10 \implies x = 5\).
                  Branch 2: \(2x - 3 = -7 \implies 2x = -4 \implies x = -2\).
                  Both solutions (\(x = 5\) and \(x = -2\)) must be checked against the original expression.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">What is the difference between absolute error and relative error?</h3>
                <div class="faq-answer">
                  <p>Absolute error is the absolute difference between an experimental measurement \(x\) and the true accepted value \(x_0\): \(\Delta_{\text{abs}} = |x - x_0|\). Relative error normalizes this deviation against the magnitude of the true value: \(\Delta_{\text{rel}} = \frac{|x - x_0|}{|x_0|}\). Multiplying relative error by 100% yields percentage error.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">Can the absolute value of a number ever be negative?</h3>
                <div class="faq-answer">
                  <p>No. By definition in both real and complex mathematics, absolute value represents a metric distance from the origin. Distance is strictly non-negative (\(|x| \ge 0\)). If an equation states \(|x| = -5\), it has no solution in the real or complex numbers.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">Why does the absolute value appear in computer science integer abs() functions?</h3>
                <div class="faq-answer">
                  <p>In computer programming (e.g. C, Python, Java), <code>abs()</code> computes mathematical modulus. However, in two's complement integer hardware, 32-bit signed integers range from \(-2,147,483,648\) to \(+2,147,483,647\). Calling <code>abs(-2147483648)</code> causes integer overflow because the positive value \(+2,147,483,648\) cannot be represented in a 32-bit signed register, demonstrating a famous edge-case bug in systems engineering.</p>
                </div>
              </div>
            </div>
          </article>
        </div>

        <aside class="sidebar-column">
          <div class="sidebar-card">
            <h3 class="sidebar-title">Related Math Calculators</h3>
            <ul class="sidebar-nav">
              <li><a href="pythagorean-theorem-calculator.html">Pythagorean Theorem Calculator</a></li>
              <li><a href="quadratic-equation-calculator.html">Quadratic Equation Calculator</a></li>
              <li><a href="gcd-lcm-calculator.html">GCD and LCM Calculator</a></li>
              <li><a href="scientific-notation-calculator.html">Scientific Notation Calculator</a></li>
              <li><a href="significant-figures-calculator.html">Significant Figures Calculator</a></li>
              <li><a href="standard-deviation-calculator.html">Standard Deviation Calculator</a></li>
              <li><a href="percentage-calculator.html">Percentage Calculator</a></li>
              <li><a href="fraction-calculator.html">Fraction Calculator</a></li>
            </ul>
          </div>

          <div class="sidebar-card">
            <h3 class="sidebar-title">Metric Identities</h3>
            <div style="font-size:0.875rem; line-height:1.5; color:var(--text-muted, #4b5563);">
              <p><strong>Definition:</strong> \(|x| = \sqrt{x^2}\)</p>
              <p><strong>Distance:</strong> \(d(x, y) = |x - y|\)</p>
              <p><strong>Triangle:</strong> \(|x+y| \le |x| + |y|\)</p>
              <p><strong>Complex:</strong> \(|a+bi| = \sqrt{a^2 + b^2}\)</p>
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
        <h4>Hub Categories</h4>
        <ul>
          <li><a href="converter.html">Unit Converters</a></li>
          <li><a href="engineering.html">Engineering Tools</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 CalcHub. All rights reserved. Peer-reviewed computational algorithms.</p>
    </div>
  </footer>

  <script>
    function updateAbsMode() {
      const mode = document.getElementById('absMode').value;
      const inputYGroup = document.getElementById('inputYGroup');
      const labelX = document.getElementById('labelValX');
      const labelY = document.getElementById('labelValY');

      if (mode === 'real') {
        inputYGroup.style.display = 'none';
        labelX.textContent = "Value (x)";
        document.getElementById('absPrimaryLabel').textContent = "Absolute Value |x|";
      } else if (mode === 'distance') {
        inputYGroup.style.display = 'block';
        labelX.textContent = "First Coordinate (x)";
        labelY.textContent = "Second Coordinate (y)";
        document.getElementById('absPrimaryLabel').textContent = "Distance |x - y|";
      } else {
        inputYGroup.style.display = 'block';
        labelX.textContent = "Real Part (a)";
        labelY.textContent = "Imaginary Part (b)";
        document.getElementById('absPrimaryLabel').textContent = "Complex Modulus |a + bi|";
      }
      calcAbs();
    }

    function calcAbs() {
      const mode = document.getElementById('absMode').value;
      const x = parseFloat(document.getElementById('valX').value);
      const y = parseFloat(document.getElementById('valY').value);

      if (isNaN(x)) return;

      let primaryVal = 0;
      let subtext = "";
      let signumText = "";
      let sqModText = "";
      let oppText = "";
      let algForm = "";
      let stepsHtml = "";

      if (mode === 'real') {
        primaryVal = Math.abs(x);
        subtext = `Distance from origin: |${x}| = ${primaryVal}`;
        const sgn = x > 0 ? 1 : (x < 0 ? -1 : 0);
        signumText = sgn === 1 ? "+1 (Positive)" : (sgn === -1 ? "-1 (Negative)" : "0 (Zero)");
        sqModText = (x * x).toLocaleString();
        oppText = (-x).toLocaleString();
        algForm = `√(${x})² = √${(x*x).toFixed(4)}`;

        stepsHtml += `1. Input Real Number: x = ${x}<br>`;
        if (x >= 0) {
          stepsHtml += `2. Condition x ≥ 0 holds: |${x}| = ${x}<br>`;
        } else {
          stepsHtml += `2. Condition x < 0 holds: |${x}| = -(${x}) = ${primaryVal}<br>`;
        }
        stepsHtml += `3. Principal square root identity: √(${x}²) = √${(x*x).toFixed(4)} = ${primaryVal}`;
      } else if (mode === 'distance') {
        if (isNaN(y)) return;
        const diff = x - y;
        primaryVal = Math.abs(diff);
        subtext = `Distance between points: |${x} - (${y})| = ${primaryVal}`;
        signumText = diff > 0 ? `x > y (+${primaryVal})` : (diff < 0 ? `x < y (-${primaryVal})` : "x = y (Coincident)");
        sqModText = (diff * diff).toLocaleString();
        oppText = (y - x).toLocaleString();
        algForm = `√(${x} - ${y})² = √${(diff*diff).toFixed(4)}`;

        stepsHtml += `1. Point 1: x = ${x}; Point 2: y = ${y}<br>`;
        stepsHtml += `2. Displacement: Δ = x - y = ${x} - (${y}) = ${diff.toFixed(4)}<br>`;
        stepsHtml += `3. Metric Euclidean Distance: d(x, y) = |${diff.toFixed(4)}| = ${primaryVal.toFixed(4)}`;
      } else {
        if (isNaN(y)) return;
        const sqSum = (x * x) + (y * y);
        primaryVal = Math.sqrt(sqSum);
        const thetaRad = Math.atan2(y, x);
        const thetaDeg = thetaRad * (180 / Math.PI);
        subtext = `Argand magnitude: |${x} + ${y}i| = ${primaryVal.toFixed(4)}`;
        signumText = `Phase Angle: ${thetaDeg.toFixed(2)}° (${thetaRad.toFixed(4)} rad)`;
        sqModText = sqSum.toFixed(4);
        oppText = `Conjugate: ${x} - ${y}i`;
        algForm = `√(${x}² + ${y}²) = √${sqSum.toFixed(4)}`;

        stepsHtml += `1. Complex number z = ${x} + (${y})i<br>`;
        stepsHtml += `2. Real component a = ${x}; Imaginary component b = ${y}<br>`;
        stepsHtml += `3. Modulus formula: |z| = √(a² + b²) = √(${x}² + ${y}²)<br>`;
        stepsHtml += `4. Sum of squares: ${ (x*x).toFixed(4) } + ${ (y*y).toFixed(4) } = ${sqSum.toFixed(4)}<br>`;
        stepsHtml += `5. Principal root: √${sqSum.toFixed(4)} = ${primaryVal.toFixed(4)}`;
      }

      document.getElementById('absPrimaryResult').textContent = primaryVal.toLocaleString();
      document.getElementById('absSubtext').textContent = subtext;
      document.getElementById('resSignum').textContent = signumText;
      document.getElementById('resSqMod').textContent = sqModText;
      document.getElementById('resOpposite').textContent = oppText;
      document.getElementById('resAlgForm').innerHTML = algForm;
      document.getElementById('absStepsDisplay').innerHTML = stepsHtml;
    }

    document.getElementById('absMode').addEventListener('change', updateAbsMode);
    document.getElementById('valX').addEventListener('input', calcAbs);
    document.getElementById('valY').addEventListener('input', calcAbs);
    updateAbsMode();
  </script>
</body>
</html>
"""

# -------------------------------------------------------------
# 2. AREA CALCULATOR
# -------------------------------------------------------------
area_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Area Calculator — Geometric Shapes, Formulas & Surveying | CalcHub</title>
  <meta name="description" content="Calculate surface area for rectangle, triangle, circle, trapezoid, ellipse, regular polygons, Heron's formula, and land surveying coordinate grids.">
  <meta name="keywords" content="area calculator, geometric area, circle area, triangle area calculator, trapezoid area, polygon area calculator, herons formula, surface area, square footage calculator">
  <meta name="author" content="CalcHub Euclidean Geometry & Applied Mensuration Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/area-calculator.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="Area Calculator — Geometric Shapes, Formulas & Surveying | CalcHub">
  <meta property="og:description" content="Compute two-dimensional surface area for all standard geometric shapes, polygons, and irregular land parcels with instant unit conversions.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/area-calculator.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/area-calculator.html#app",
      "name": "Geometric Planar Area Calculator",
      "url": "https://calchub.org/area-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "High-precision geometric mensuration engine for computing 2D area across polygons, circles, ellipses, triangles, and land parcels."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Math & Engineering Calculators", "item": "https://calchub.org/math.html"},
        {"@type": "ListItem", "position": 3, "name": "Area Calculator", "item": "https://calchub.org/area-calculator.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How is Heron's Formula used to calculate the area of any triangle from side lengths?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Heron's Formula allows the computation of triangle area without requiring perpendicular height or angle measurements. Given three side lengths a, b, and c, first compute the semi-perimeter: s = (a + b + c) / 2. The area A is then calculated as: A = √[s(s - a)(s - b)(s - c)]. The formula requires that the triangle inequality holds (a + b > c, a + c > b, b + c > a); otherwise the term inside the radical becomes zero or negative."
          }
        },
        {
          "@type": "Question",
          "name": "What is the formula for the area of an ellipse and how does it relate to a circle?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The area of an ellipse with semi-major axis 'a' and semi-minor axis 'b' is given by A = π · a · b. A circle is simply a special case of an ellipse where the semi-major and semi-minor axes are equal to the radius (a = b = r), which simplifies the equation directly back to A = π · r · r = πr²."
          }
        },
        {
          "@type": "Question",
          "name": "How is the area of a regular n-sided polygon calculated?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "For a regular polygon with n equal sides of length s, the area can be computed using the perimeter P = n · s and the apothem 'a' (the perpendicular distance from the center to any side): A = 0.5 · P · a = 0.5 · n · s · a. Alternatively, expressing the apothem via trigonometry gives: A = (n · s²) / [4 · tan(π / n)]. As n approaches infinity, this formula converges exactly to the area of a circle πr²."
          }
        },
        {
          "@type": "Question",
          "name": "What is the Shoelace Formula (Gauss's Area Formula) for irregular land parcels?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The Shoelace Formula computes the 2D area of any non-self-intersecting polygon given the Cartesian coordinates of its vertices {(x₁, y₁), (x₂, y₂), ..., (x_n, y_n)}. The formula sums the cross-products of coordinate pairs: A = 0.5 · |Σ(x_i · y_{i+1} - x_{i+1} · y_i)|, wrapping from vertex n back to vertex 1. It is the primary computational method utilized in GIS software and civil land surveying."
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
            <div class="badge-tag">Euclidean Geometry & Mensuration</div>
            <h1 class="tool-title">Area Calculator</h1>
            <p class="tool-subtitle">Calculate 2D surface area across rectangles, triangles, circles, trapezoids, ellipses, and regular polygons with instant multi-unit conversions.</p>
          </header>

          <section class="calculator-card" aria-label="Geometric Area Solver">
            <div class="calc-grid">
              <div class="input-group">
                <label for="shapeSelect" class="input-label">Geometric Shape</label>
                <select id="shapeSelect" class="calc-input">
                  <option value="rectangle">Rectangle (Length × Width)</option>
                  <option value="triangle">Triangle (Base &amp; Height)</option>
                  <option value="heron">Triangle (Heron's 3 Sides)</option>
                  <option value="circle">Circle (Radius r)</option>
                  <option value="trapezoid">Trapezoid (Bases a, b &amp; Height h)</option>
                  <option value="ellipse">Ellipse (Semi-axes a &amp; b)</option>
                  <option value="polygon">Regular Polygon (Sides n &amp; Length s)</option>
                </select>
              </div>

              <div class="input-group" id="dim1Group">
                <label for="dim1" class="input-label" id="labelDim1">Length</label>
                <input type="number" id="dim1" class="calc-input" value="12" step="any" min="0.0001">
              </div>

              <div class="input-group" id="dim2Group">
                <label for="dim2" class="input-label" id="labelDim2">Width</label>
                <input type="number" id="dim2" class="calc-input" value="8" step="any" min="0.0001">
              </div>

              <div class="input-group" id="dim3Group" style="display:none;">
                <label for="dim3" class="input-label" id="labelDim3">Third Dimension</label>
                <input type="number" id="dim3" class="calc-input" value="10" step="any" min="0.0001">
              </div>
            </div>

            <div class="primary-result" style="margin-top: 25px;">
              <div class="result-label">Computed Surface Area</div>
              <div class="result-value" id="areaPrimaryResult">96.0000 sq units</div>
              <div class="result-subtext" id="areaSubtext">Rectangle: 12 × 8 = 96 sq units</div>
            </div>

            <div class="results-grid" style="margin-top: 20px;">
              <div class="result-item">
                <div class="result-label">Square Feet (\(\text{ft}^2\))</div>
                <div class="result-value" id="resSqFt">96.000 ft²</div>
              </div>
              <div class="result-item">
                <div class="result-label">Square Meters (\(\text{m}^2\))</div>
                <div class="result-value" id="resSqM">8.9186 m²</div>
              </div>
              <div class="result-item">
                <div class="result-label">Square Inches (\(\text{in}^2\))</div>
                <div class="result-value" id="resSqIn">13,824 in²</div>
              </div>
              <div class="result-item">
                <div class="result-label">Acres</div>
                <div class="result-value" id="resAcres">0.00220 ac</div>
              </div>
            </div>

            <div class="conversion-steps" style="margin-top: 25px;">
              <h3>Step-by-Step Geometric Resolution</h3>
              <div id="areaStepsDisplay" style="font-family: monospace; font-size: 0.95rem; line-height: 1.6; background: rgba(0,0,0,0.03); padding: 16px; border-radius: 8px; border-left: 4px solid var(--accent, #2563eb);">
                Loading calculation steps...
              </div>
            </div>
          </section>

          <article class="article-body">
            <h2>1. Foundations and Axiomatic Principles of Planar Area</h2>
            <p>In classical geometry, mensuration, and analytical surveying, <strong>area</strong> constitutes the quantitative measure of two-dimensional surface extent enclosed within a continuous closed boundary in a flat Euclidean plane. Rooted historically in the agrarian surveying needs of ancient Egypt (the Nile flood inundation redistribution) and formalized in Euclid's <em>Elements</em>, area is defined axiomatically through three fundamental geometric properties:</p>
            <ul>
              <li><strong>Unit Square Axiom:</strong> The area of a unit square with side length 1 is defined identically as 1 square unit (\(\mathcal{A} = 1\)).</li>
              <li><strong>Congruence Invariance:</strong> If two geometric figures are congruent (identical in shape and size), their surface areas are identical.</li>
              <li><strong>Additivity (Finite Dissection):</strong> If a planar region \(\mathcal{R}\) is partitioned into two non-overlapping sub-regions \(\mathcal{R}_1\) and \(\mathcal{R}_2\), the total area is the sum of the constituent areas: \(\mathcal{A}(\mathcal{R}) = \mathcal{A}(\mathcal{R}_1) + \mathcal{A}(\mathcal{R}_2)\).</li>
            </ul>

            <p>From these basic axioms, all closed-form geometric area formulas across polygons, curved conic sections, and multi-sided land tracts are rigorously derived.</p>

            <h2>2. Core Geometric Area Formulas</h2>

            <h3>2.1 Rectangles and Squares</h3>
            <p>The rectangle represents the fundamental baseline of area mensuration. For a rectangle with orthogonal length \(l\) and width \(w\):</p>

            $$\mathcal{A}_{\text{rect}} = l \times w$$

            <p>For a square with equal sides \(s\), this reduces directly to the second power: \(\mathcal{A}_{\text{square}} = s^2\).</p>

            <h3>2.2 Triangles: Standard Base-Height and Heron's Formula</h3>
            <p>Because any triangle can be viewed as exactly half of a parallelogram sharing the same base \(b\) and perpendicular height \(h\):</p>

            $$\mathcal{A}_{\text{tri}} = \frac{1}{2} b \cdot h$$

            <p>When the perpendicular altitude is unknown, but all three side lengths \(a, b, c\) are measured, <strong>Heron's Formula</strong> (derived by Hero of Alexandria, c. 60 CE) provides an exact solution. First, calculate the semi-perimeter \(s\):</p>

            $$s = \frac{a + b + c}{2}$$

            <p>The enclosed surface area is then given by:</p>

            $$\mathcal{A}_{\text{Heron}} = \sqrt{s(s - a)(s - b)(s - c)}$$

            <p>Heron's formula requires the <em>Triangle Inequality</em>: \(a + b > c\), \(a + c > b\), and \(b + c > a\). If any side is equal to or exceeds the sum of the other two, the radicand becomes zero or negative, indicating a degenerate straight line or physically impossible triangle.</p>

            <h3>2.3 Circles and Ellipses</h3>
            <p>For a circle of radius \(r\) and diameter \(d = 2r\), the area is derived from integral calculus as the continuous accumulation of concentric thin annular rings:</p>

            $$\mathcal{A}_{\text{circle}} = \int_0^r 2\pi x \, dx = \pi r^2 = \frac{\pi d^2}{4}$$

            <p>An ellipse is a scaled affine transformation of a circle. If the semi-major axis is \(a\) and the semi-minor axis is \(b\), the area scales proportionally:</p>

            $$\mathcal{A}_{\text{ellipse}} = \pi \cdot a \cdot b$$

            <h3>2.4 Trapezoids (Trapeziums) and Parallelograms</h3>
            <p>A trapezoid possesses two parallel horizontal bases, \(a\) and \(b\), separated by perpendicular altitude \(h\). Its area represents the product of its average base width and height:</p>

            $$\mathcal{A}_{\text{trap}} = \left(\frac{a + b}{2}\right) h$$

            <p>For a parallelogram with base \(b\) and vertical height \(h\), \(\mathcal{A} = b \cdot h\). If the interior acute angle \(\theta\) between adjacent sides \(a\) and \(b\) is given: \(\mathcal{A} = a \cdot b \cdot \sin(\theta)\).</p>

            <h3>2.5 Regular Polygons (\(n\)-gons)</h3>
            <p>A regular polygon has \(n\) congruent sides of length \(s\). Partitioning the polygon from its geometric centroid into \(n\) congruent isosceles triangles yields:</p>

            $$\mathcal{A}_{\text{poly}} = \frac{1}{2} P \cdot a_{\text{apo}}$$

            <p>where \(P = n \cdot s\) is the perimeter and \(a_{\text{apo}} = \frac{s}{2 \tan(\pi / n)}\) is the apothem (inradius). Substituting the apothem into the area expression gives:</p>

            $$\mathcal{A}_{\text{poly}} = \frac{n \cdot s^2}{4 \tan\left(\frac{\pi}{n}\right)}$$

            <p>As \(n \to \infty\), \(\tan(\pi/n) \to \pi/n\), causing \(\mathcal{A}_{\text{poly}}\) to converge continuously to \(\pi r^2\), demonstrating how Archimedes historically bounded \(\pi\) using 96-sided circumscribed polygons.</p>

            <h2>3. Advanced Surveying: Gauss's Shoelace Area Formula</h2>
            <p>In civil engineering, cadastral land surveying, and geographic information systems (GIS), boundaries rarely conform to simple geometric shapes. For an irregular planar polygon defined by \(N\) ordered Cartesian coordinate vertices \((x_1, y_1), (x_2, y_2), \dots, (x_N, y_N)\), <strong>Gauss's Area Formula</strong> (the Shoelace Formula) provides the exact enclosed area:</p>

            $$\mathcal{A}_{\text{shoelace}} = \frac{1}{2} \left| \sum_{i=1}^N (x_i y_{i+1} - x_{i+1} y_i) \right|$$

            <p>with the wrap-around cyclic boundary condition \((x_{N+1}, y_{N+1}) = (x_1, y_1)\). The formula represents the algebraic application of Green's Theorem in the plane, reducing double surface integrals \(\iint dx\,dy\) to a 1D discrete line boundary summation.</p>

            <h2>4. Imperial and Metric Area Unit Conversion Factors</h2>
            <p>Accurate engineering conversion across metric and Imperial units requires exact dimensional standards:</p>
            <ul>
              <li>\(1\text{ m}^2 = 10.7639104\text{ ft}^2 = 1,550.0031\text{ in}^2\)</li>
              <li>\(1\text{ ft}^2 = 144\text{ in}^2 = 0.09290304\text{ m}^2\)</li>
              <li>\(1\text{ Acre} = 43,560\text{ ft}^2 = 4,046.85642\text{ m}^2 \approx 0.404686\text{ hectares}\)</li>
              <li>\(1\text{ Hectare (ha)} = 10,000\text{ m}^2 = 2.4710538\text{ acres}\)</li>
              <li>\(1\text{ Square Mile (sq mi)} = 640\text{ acres} = 2.589988\text{ km}^2\)</li>
            </ul>

            <h2>5. Benchmark Comparative Reference Table</h2>
            <p>The table below catalogues standard geometric shapes across representative dimensions, displaying exact area formulas, numerical areas, and conversions.</p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>Geometric Shape</th>
                  <th>Primary Dimensions</th>
                  <th>Governing Area Formula</th>
                  <th>Calculated Area</th>
                  <th>Square Feet (\(\text{ft}^2\))</th>
                  <th>Square Meters (\(\text{m}^2\))</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Rectangle</td>
                  <td>\(L = 12\text{ ft}, W = 8\text{ ft}\)</td>
                  <td>\(L \times W\)</td>
                  <td>\(96.00\)</td>
                  <td>\(96.000\)</td>
                  <td>\(8.919\)</td>
                </tr>
                <tr>
                  <td>Square</td>
                  <td>\(s = 15\text{ ft}\)</td>
                  <td>\(s^2\)</td>
                  <td>\(225.00\)</td>
                  <td>\(225.000\)</td>
                  <td>\(20.903\)</td>
                </tr>
                <tr>
                  <td>Circle</td>
                  <td>\(r = 7\text{ m}\)</td>
                  <td>\(\pi r^2\)</td>
                  <td>\(153.938\)</td>
                  <td>\(1,656.974\)</td>
                  <td>\(153.938\)</td>
                </tr>
                <tr>
                  <td>Right Triangle</td>
                  <td>\(b = 10\text{ ft}, h = 6\text{ ft}\)</td>
                  <td>\(\frac{1}{2} b h\)</td>
                  <td>\(30.00\)</td>
                  <td>\(30.000\)</td>
                  <td>\(2.787\)</td>
                </tr>
                <tr>
                  <td>Heron's Triangle</td>
                  <td>\(a = 7, b = 8, c = 9\text{ m}\)</td>
                  <td>\(\sqrt{s(s-a)(s-b)(s-c)}\)</td>
                  <td>\(26.833\)</td>
                  <td>\(288.827\)</td>
                  <td>\(26.833\)</td>
                </tr>
                <tr>
                  <td>Trapezoid</td>
                  <td>\(a = 14, b = 20, h = 8\text{ ft}\)</td>
                  <td>\(\frac{a+b}{2} \cdot h\)</td>
                  <td>\(136.00\)</td>
                  <td>\(136.000\)</td>
                  <td>\(12.635\)</td>
                </tr>
                <tr>
                  <td>Ellipse</td>
                  <td>\(a = 6\text{ m}, b = 4\text{ m}\)</td>
                  <td>\(\pi a b\)</td>
                  <td>\(75.398\)</td>
                  <td>\(811.581\)</td>
                  <td>\(75.398\)</td>
                </tr>
                <tr>
                  <td>Regular Hexagon</td>
                  <td>\(n = 6, s = 5\text{ ft}\)</td>
                  <td>\(\frac{3\sqrt{3}}{2} s^2\)</td>
                  <td>\(64.952\)</td>
                  <td>\(64.952\)</td>
                  <td>\(6.034\)</td>
                </tr>
              </tbody>
            </table>

            <h2>6. Worked Architectural Case Study: Commercial Flooring & Material Takeoff</h2>
            <div class="worked-example-card">
              <div class="example-header">
                <strong>Architectural Engineering Case Study:</strong> Atrium Floor Area and Luxury Vinyl Tile (LVT) Takeoff
              </div>
              <div class="example-body">
                <p><strong>Scenario:</strong> A commercial interior contractor is preparing a flooring material bid for a corporate lobby. The floor consists of a central rectangular foyer measuring \(L_1 = 36.0\text{ ft}\) by \(W_1 = 24.0\text{ ft}\), adjoined by a semicircular seating rotunda of radius \(r = 12.0\text{ ft}\). The architect specifies luxury vinyl tile (LVT) packaged in cartons covering \(24.0\text{ ft}^2\) per box, with a mandatory \(10\%\) cutting waste factor. The estimator must compute: (1) the net composite floor area, (2) the gross area with waste, and (3) the exact carton purchase count.</p>

                <p><strong>Step 1: Calculate Net Rectangular Foyer Area (\(\mathcal{A}_{\text{foyer}}\))</strong><br>
                $$\mathcal{A}_{\text{foyer}} = L_1 \times W_1 = 36.0\text{ ft} \times 24.0\text{ ft} = 864.0\text{ ft}^2$$</p>

                <p><strong>Step 2: Calculate Net Semicircular Rotunda Area (\(\mathcal{A}_{\text{rotunda}}\))</strong><br>
                A semicircle represents half of a circle of radius \(r = 12.0\text{ ft}\):
                $$\mathcal{A}_{\text{rotunda}} = \frac{1}{2} \pi r^2 = \frac{1}{2} \times 3.14159265 \times (12.0)^2 = 0.5 \times 3.14159265 \times 144 = 226.195\text{ ft}^2$$</p>

                <p><strong>Step 3: Compute Total Net Floor Area</strong><br>
                $$\mathcal{A}_{\text{net}} = \mathcal{A}_{\text{foyer}} + \mathcal{A}_{\text{rotunda}} = 864.0 + 226.195 = 1,090.195\text{ ft}^2$$</p>

                <p><strong>Step 4: Incorporate 10% Cutting and Pattern Waste</strong><br>
                $$\mathcal{A}_{\text{gross}} = \mathcal{A}_{\text{net}} \times 1.10 = 1,090.195 \times 1.10 = 1,199.215\text{ ft}^2$$</p>

                <p><strong>Step 5: Determine Carton Purchase Order Quantity</strong><br>
                $$N_{\text{boxes}} = \left\lceil \frac{\mathcal{A}_{\text{gross}}}{\text{Coverage per Box}} \right\rceil = \left\lceil \frac{1,199.215}{24.0} \right\rceil = \lceil 49.967 \rceil = 50\text{ cartons}$$
                The project requires exactly 50 cartons of LVT covering \(1,200.0\text{ ft}^2\).</p>
              </div>
            </div>

            <h2>7. Frequently Asked Questions (FAQ)</h2>
            <div class="faq-accordion">
              <div class="faq-item">
                <h3 class="faq-question">What is the difference between area and surface area?</h3>
                <div class="faq-answer">
                  <p>Area refers to the two-dimensional extent of a flat, planar shape (such as a square, circle, or triangle). Surface area refers to the total sum of all 2D boundary areas covering the exterior surfaces of a three-dimensional solid object (such as the 6 faces of a cube, the cylindrical shell plus ends of a pipe, or the spherical envelope of a globe).</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">Why must angle measurements be in radians when using trigonometric area formulas?</h3>
                <div class="faq-answer">
                  <p>In elementary formulas like \(\mathcal{A} = \frac{1}{2} a b \sin(\theta)\), degrees or radians can be used provided the sine function is evaluated in matching angular units. However, in calculus derivations, polygon apothem formulas, and circular sector integrations (\(\mathcal{A}_{\text{sector}} = \frac{1}{2} r^2 \theta\)), \(\theta\) must be in radians because the radian is the dimensionless SI unit that naturally relates arc length to radius (\(s = r\theta\)).</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">How do you calculate the area of an irregular 4-sided quadrilateral?</h3>
                <div class="faq-answer">
                  <p>If only the four side lengths are known, a quadrilateral is flexible (not rigid) and its area is not uniquely fixed. To find the area, you must either know an internal diagonal length (splitting it into two triangles solved via Heron's formula), or know two opposite angles and use Bretschneider's Formula: \(\mathcal{A} = \sqrt{(s-a)(s-b)(s-c)(s-d) - abcd \cos^2\left(\frac{\alpha+\gamma}{2}\right)}\).</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">How does scaling linear dimensions affect the area of a shape?</h3>
                <div class="faq-answer">
                  <p>Area scales quadratically with linear dimensions (the Square-Cube Law). If all linear dimensions of any 2D shape are multiplied by a scale factor \(k\), the surface area increases by \(k^2\). For example, doubling the diameter of a circular pipe (\(k = 2\)) quadruples its cross-sectional flow area (\(2^2 = 4\)).</p>
                </div>
              </div>
            </div>
          </article>
        </div>

        <aside class="sidebar-column">
          <div class="sidebar-card">
            <h3 class="sidebar-title">Related Math Calculators</h3>
            <ul class="sidebar-nav">
              <li><a href="pythagorean-theorem-calculator.html">Pythagorean Theorem Calculator</a></li>
              <li><a href="quadratic-equation-calculator.html">Quadratic Equation Calculator</a></li>
              <li><a href="gcd-lcm-calculator.html">GCD and LCM Calculator</a></li>
              <li><a href="scientific-notation-calculator.html">Scientific Notation Calculator</a></li>
              <li><a href="significant-figures-calculator.html">Significant Figures Calculator</a></li>
              <li><a href="percentage-calculator.html">Percentage Calculator</a></li>
              <li><a href="fraction-calculator.html">Fraction Calculator</a></li>
              <li><a href="area-converter.html">Area Unit Converter</a></li>
            </ul>
          </div>

          <div class="sidebar-card">
            <h3 class="sidebar-title">Area Formulas</h3>
            <div style="font-size:0.875rem; line-height:1.5; color:var(--text-muted, #4b5563);">
              <p><strong>Rectangle:</strong> \(L \times W\)</p>
              <p><strong>Triangle:</strong> \(\frac{1}{2} b \cdot h\)</p>
              <p><strong>Circle:</strong> \(\pi r^2\)</p>
              <p><strong>Trapezoid:</strong> \(\frac{a+b}{2} \cdot h\)</p>
              <p><strong>Ellipse:</strong> \(\pi a b\)</p>
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
        <h4>Hub Categories</h4>
        <ul>
          <li><a href="converter.html">Unit Converters</a></li>
          <li><a href="engineering.html">Engineering Tools</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 CalcHub. All rights reserved. Peer-reviewed computational algorithms.</p>
    </div>
  </footer>

  <script>
    function updateShapeUi() {
      const shape = document.getElementById('shapeSelect').value;
      const d1G = document.getElementById('dim1Group');
      const d2G = document.getElementById('dim2Group');
      const d3G = document.getElementById('dim3Group');
      const l1 = document.getElementById('labelDim1');
      const l2 = document.getElementById('labelDim2');
      const l3 = document.getElementById('labelDim3');

      d3G.style.display = 'none';

      if (shape === 'rectangle') {
        d1G.style.display = 'block'; d2G.style.display = 'block';
        l1.textContent = "Length (L)"; l2.textContent = "Width (W)";
      } else if (shape === 'triangle') {
        d1G.style.display = 'block'; d2G.style.display = 'block';
        l1.textContent = "Base (b)"; l2.textContent = "Height (h)";
      } else if (shape === 'heron') {
        d1G.style.display = 'block'; d2G.style.display = 'block'; d3G.style.display = 'block';
        l1.textContent = "Side a"; l2.textContent = "Side b"; l3.textContent = "Side c";
      } else if (shape === 'circle') {
        d1G.style.display = 'block'; d2G.style.display = 'none';
        l1.textContent = "Radius (r)";
      } else if (shape === 'trapezoid') {
        d1G.style.display = 'block'; d2G.style.display = 'block'; d3G.style.display = 'block';
        l1.textContent = "Base a"; l2.textContent = "Base b"; l3.textContent = "Height h";
      } else if (shape === 'ellipse') {
        d1G.style.display = 'block'; d2G.style.display = 'block';
        l1.textContent = "Semi-major axis (a)"; l2.textContent = "Semi-minor axis (b)";
      } else if (shape === 'polygon') {
        d1G.style.display = 'block'; d2G.style.display = 'block';
        l1.textContent = "Number of sides (n)"; l2.textContent = "Side length (s)";
      }
      calcArea();
    }

    function calcArea() {
      const shape = document.getElementById('shapeSelect').value;
      const v1 = parseFloat(document.getElementById('dim1').value);
      const v2 = parseFloat(document.getElementById('dim2').value);
      const v3 = parseFloat(document.getElementById('dim3').value);

      if (isNaN(v1) || v1 <= 0) return;

      let area = 0;
      let subtext = "";
      let stepsHtml = "";

      if (shape === 'rectangle') {
        if (isNaN(v2) || v2 <= 0) return;
        area = v1 * v2;
        subtext = `Rectangle: ${v1} × ${v2} = ${area.toFixed(4)} sq units`;
        stepsHtml = `1. Formula: Area = Length × Width<br>2. Substitute: ${v1} × ${v2}<br>3. Result: ${area.toFixed(4)} sq units`;
      } else if (shape === 'triangle') {
        if (isNaN(v2) || v2 <= 0) return;
        area = 0.5 * v1 * v2;
        subtext = `Triangle: 0.5 × ${v1} × ${v2} = ${area.toFixed(4)} sq units`;
        stepsHtml = `1. Formula: Area = ½ × Base × Height<br>2. Substitute: 0.5 × ${v1} × ${v2}<br>3. Result: ${area.toFixed(4)} sq units`;
      } else if (shape === 'heron') {
        if (isNaN(v2) || isNaN(v3) || v2 <= 0 || v3 <= 0) return;
        const a = v1, b = v2, c = v3;
        if (a + b <= c || a + c <= b || b + c <= a) {
          document.getElementById('areaPrimaryResult').textContent = "Error: Invalid Triangle";
          document.getElementById('areaSubtext').textContent = "Violates triangle inequality (sum of two sides must exceed third)";
          return;
        }
        const s = (a + b + c) / 2;
        area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
        subtext = `Heron's Formula: s = ${s.toFixed(2)} | Area = ${area.toFixed(4)} sq units`;
        stepsHtml = `1. Semi-perimeter: s = (${a} + ${b} + ${c}) / 2 = ${s.toFixed(4)}<br>`;
        stepsHtml += `2. Radical terms: (${s.toFixed(2)} - ${a}) = ${(s-a).toFixed(2)}; (${s.toFixed(2)} - ${b}) = ${(s-b).toFixed(2)}; (${s.toFixed(2)} - ${c}) = ${(s-c).toFixed(2)}<br>`;
        stepsHtml += `3. Product: ${s.toFixed(2)} × ${(s-a).toFixed(2)} × ${(s-b).toFixed(2)} × ${(s-c).toFixed(2)} = ${(s*(s-a)*(s-b)*(s-c)).toFixed(4)}<br>`;
        stepsHtml += `4. Result: √${(s*(s-a)*(s-b)*(s-c)).toFixed(4)} = ${area.toFixed(4)} sq units`;
      } else if (shape === 'circle') {
        area = Math.PI * v1 * v1;
        subtext = `Circle: π × (${v1})² = ${area.toFixed(4)} sq units`;
        stepsHtml = `1. Formula: Area = π × r²<br>2. Substitute: π × (${v1})² = π × ${(v1*v1).toFixed(4)}<br>3. Result: ${area.toFixed(4)} sq units`;
      } else if (shape === 'trapezoid') {
        if (isNaN(v2) || isNaN(v3) || v2 <= 0 || v3 <= 0) return;
        area = 0.5 * (v1 + v2) * v3;
        subtext = `Trapezoid: 0.5 × (${v1} + ${v2}) × ${v3} = ${area.toFixed(4)} sq units`;
        stepsHtml = `1. Formula: Area = ½ × (Base a + Base b) × Height<br>2. Average base: (${v1} + ${v2}) / 2 = ${((v1+v2)/2).toFixed(4)}<br>3. Result: ${((v1+v2)/2).toFixed(4)} × ${v3} = ${area.toFixed(4)} sq units`;
      } else if (shape === 'ellipse') {
        if (isNaN(v2) || v2 <= 0) return;
        area = Math.PI * v1 * v2;
        subtext = `Ellipse: π × ${v1} × ${v2} = ${area.toFixed(4)} sq units`;
        stepsHtml = `1. Formula: Area = π × a × b<br>2. Substitute: π × ${v1} × ${v2} = π × ${(v1*v2).toFixed(4)}<br>3. Result: ${area.toFixed(4)} sq units`;
      } else if (shape === 'polygon') {
        const n = Math.floor(v1);
        const s = v2;
        if (n < 3 || isNaN(s) || s <= 0) {
          document.getElementById('areaPrimaryResult').textContent = "Error: n must be ≥ 3";
          return;
        }
        area = (n * s * s) / (4 * Math.tan(Math.PI / n));
        subtext = `Regular ${n}-gon: Area = ${area.toFixed(4)} sq units`;
        stepsHtml = `1. Formula: Area = (n × s²) / [4 × tan(π / n)]<br>2. n = ${n}; side = ${s}<br>3. Apothem: s / [2 × tan(π/${n})] = ${(s / (2 * Math.tan(Math.PI / n))).toFixed(4)}<br>4. Result: ${area.toFixed(4)} sq units`;
      }

      document.getElementById('areaPrimaryResult').textContent = `${area.toFixed(4)} sq units`;
      document.getElementById('areaSubtext').textContent = subtext;
      document.getElementById('resSqFt').textContent = `${area.toFixed(4)} ft²`;
      document.getElementById('resSqM').textContent = `${(area * 0.092903).toFixed(4)} m²`;
      document.getElementById('resSqIn').textContent = `${(area * 144).toLocaleString()} in²`;
      document.getElementById('resAcres').textContent = `${(area / 43560).toFixed(5)} ac`;
      document.getElementById('areaStepsDisplay').innerHTML = stepsHtml;
    }

    document.getElementById('shapeSelect').addEventListener('change', updateShapeUi);
    document.getElementById('dim1').addEventListener('input', calcArea);
    document.getElementById('dim2').addEventListener('input', calcArea);
    document.getElementById('dim3').addEventListener('input', calcArea);
    updateShapeUi();
  </script>
</body>
</html>
"""

# Write files
with open(os.path.join(BASE_DIR, 'absolute-value-calculator.html'), 'w', encoding='utf-8') as f:
    f.write(abs_html)
print("Generated absolute-value-calculator.html successfully!")

with open(os.path.join(BASE_DIR, 'area-calculator.html'), 'w', encoding='utf-8') as f:
    f.write(area_html)
print("Generated area-calculator.html successfully!")
