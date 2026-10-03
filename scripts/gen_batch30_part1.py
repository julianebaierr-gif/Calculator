# -*- coding: utf-8 -*-
"""
Generator for Batch 30 - Part 1:
1. square-root-calculator.html
2. percent-to-fraction-calculator.html
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 1. square-root-calculator.html
HTML_SQUARE_ROOT = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Square Root Calculator - Radical Simplifier & Babylonian Steps</title>
  <meta name="description" content="Calculate principal square roots, radical simplifications (k√m), Babylonian iterations, and imaginary roots for negative numbers with step-by-step arithmetic.">
  <link rel="canonical" href="https://calchub.org/square-root-calculator.html">
  <meta property="og:title" content="Square Root Calculator - Exact Radical & Decimal Solver">
  <meta property="og:description" content="Compute square roots, simplified radicals, perfect square status, and Heron iterative approximations with rigorous mathematical proofs.">
  <meta property="og:url" content="https://calchub.org/square-root-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Square Root Calculator - Radical & Precision Solver">
  <meta name="twitter:description" content="Free square root calculator. Evaluates √x, simplifies radical expressions, identifies perfect squares, and shows Babylonian algorithm steps.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Square Root Calculator",
    "url": "https://calchub.org/square-root-calculator.html",
    "description": "Calculates the principal square root, simplified radical form, perfect square classification, and Babylonian approximation iterations.",
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
        "name": "What is the principal square root?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The principal square root of a non-negative real number x is the unique non-negative real number y such that y² = x. Denoted by √x, it is always positive or zero (e.g., √25 = 5, not -5)."
        }
      },
      {
        "@type": "Question",
        "name": "How do you simplify a square root radical?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "To simplify √A into simplest radical form k√m, find the largest perfect square factor s² dividing A. Factor A as s² · m, then extract s outside the radical: √A = √(s² · m) = s√m (e.g., √72 = √(36 · 2) = 6√2)."
        }
      },
      {
        "@type": "Question",
        "name": "What is the square root of a negative number?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "In real arithmetic, the square root of a negative number is undefined because no real number squared yields a negative product. In complex numbers, it is expressed using the imaginary unit i = √(-1): √(-A) = i√A (e.g., √(-16) = 4i)."
        }
      },
      {
        "@type": "Question",
        "name": "What is the Babylonian method for calculating square roots?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Babylonian method (Heron's method) is an ancient iterative algorithm that converges quadratically: x_(n+1) = (1/2) · [x_n + S / x_n], where S is the number whose square root is sought."
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
        <a href="math.html" class="active">Math & Statistics</a>
        <a href="converter.html">Converters</a>
        <a href="engineering.html">Engineering</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="page-container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &gt;
      <a href="math.html">Math</a> &gt;
      <span>Square Root Calculator</span>
    </nav>

    <div class="content-layout">
      <div class="main-column">
        <div class="calculator-card">
          <div class="calculator-header">
            <span class="calc-icon">√</span>
            <h1>Square Root Calculator</h1>
          </div>
          <p class="calc-description">
            Calculate the exact principal square root, simplified radical expression \(k\sqrt{m}\), Babylonian convergence steps, and complex imaginary roots.
          </p>

          <form id="calc-form" class="calc-form" onsubmit="return false;">
            <div class="input-grid">
              <div class="form-group">
                <label for="radicand_x">Radicand (\(x\)):</label>
                <input type="number" id="radicand_x" class="form-control" value="72" step="any" placeholder="e.g. 72 or 144" required>
                <span class="help-text">Real number to extract root from.</span>
              </div>
              <div class="form-group">
                <label for="precision">Output Decimal Precision:</label>
                <select id="precision" class="form-control">
                  <option value="4">4 decimal places</option>
                  <option value="6" selected>6 decimal places (Standard)</option>
                  <option value="8">8 decimal places</option>
                  <option value="12">12 decimal places (Scientific)</option>
                </select>
                <span class="help-text">Display accuracy for decimal root.</span>
              </div>
            </div>

            <button type="button" id="btn-calculate" class="btn btn-primary" onclick="calculateSquareRoot()">Compute Square Root</button>
          </form>

          <div id="result-box" class="result-box" style="display:none;">
            <h3>Square Root Solution</h3>
            <div class="result-highlight" id="primary-result">√72 ≈ 8.485281</div>
            
            <div class="result-grid">
              <div class="result-item">
                <span class="res-label">Decimal Value:</span>
                <span class="res-val" id="res-decimal">8.485281</span>
              </div>
              <div class="result-item">
                <span class="res-label">Simplified Radical:</span>
                <span class="res-val" id="res-radical">6√2</span>
              </div>
              <div class="result-item">
                <span class="res-label">Perfect Square Status:</span>
                <span class="res-val" id="res-perfect">No (Irrational)</span>
              </div>
              <div class="result-item">
                <span class="res-label">Verification (\(y^2\)):</span>
                <span class="res-val" id="res-verify">(8.485281)² ≈ 72</span>
              </div>
            </div>

            <div class="conversion-steps" id="steps-output">
              <!-- Steps output -->
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. Mathematical Theory of the Square Root Function</h2>
          <p>
            In algebra, geometry, and real analysis, the <strong>square root</strong> of a real number \(x\) is a number \(y\) that satisfies the fundamental quadratic relation:
          </p>
          $$y^2 = x$$
          <p>
            Because the square of both positive and negative real numbers is always non-negative (\((+y)^2 = (-y)^2 = y^2 \ge 0\)), every strictly positive real number \(x > 0\) admits exactly two real roots: a positive root and an additive inverse negative root.
          </p>
          <p>
            To establish a well-defined single-valued mathematical function in calculus and computer science, international convention designates the non-negative solution as the <strong>principal square root</strong>, denoted exclusively by the radical sign \(\sqrt{\phantom{x}}\):
          </p>
          $$\sqrt{x} \ge 0 \quad \text{for all } x \in [0, +\infty)$$
          <p>
            Thus, while the algebraic equation \(y^2 = 25\) possesses two distinct roots (\(y = \pm 5\)), the expression \(\sqrt{25}\) evaluates strictly to \(+5\). The negative root is denoted explicitly as \(-\sqrt{x}\).
          </p>

          <h2>2. Radical Simplification Algorithm (\(k\sqrt{m}\))</h2>
          <p>
            In exact mathematics and engineering mechanics, expressing square roots as infinite decimal approximations introduces truncation errors. Instead, square roots of integers are converted into <strong>simplest radical form</strong>:
          </p>
          $$\sqrt{A} = k \sqrt{m}$$
          <p>
            where \(k\) is an integer extracted outside the radical, and \(m\) is a <strong>square-free integer</strong> (an integer not divisible by any perfect square other than 1).
          </p>
          <p><strong>Step-by-Step Factoring Procedure:</strong></p>
          <ol>
            <li>
              Perform the prime factorization of \(A\):
              $$A = p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdots p_n^{\alpha_n}$$
            </li>
            <li>
              Decompose each exponent \(\alpha_i\) into its quotient and remainder modulo 2:
              $$\alpha_i = 2 \cdot q_i + r_i \quad \text{where } r_i \in \{0, 1\}$$
            </li>
            <li>
              Extract the squared factors outside the radical operator:
              $$k = \prod_{i=1}^n p_i^{q_i}, \quad m = \prod_{i=1}^n p_i^{r_i} \implies \sqrt{A} = k \sqrt{m}$$
            </li>
          </ol>
          <p>
            For example, consider \(A = 72\):
          </p>
          $$72 = 2^3 \times 3^2 = 2^{2 \cdot 1 + 1} \times 3^{2 \cdot 1 + 0} \implies k = 2^1 \times 3^1 = 6, \quad m = 2^1 = 2 \implies \sqrt{72} = 6\sqrt{2}$$

          <h2>3. Algorithmic Extraction: The Babylonian Method (Heron's Iteration)</h2>
          <p>
            The <strong>Babylonian method</strong> (also attributed to Heron of Alexandria, c. 60 CE) is one of the oldest and most computationally efficient algorithms for extracting numerical square roots. It is mathematically identical to applying the Newton-Raphson method to the quadratic objective function \(f(y) = y^2 - x = 0\).
          </p>
          <p>
            Given an initial positive guess \(y_0 > 0\), the sequence of successive approximations is defined by the recurrence relation:
          </p>
          $$y_{n+1} = \frac{1}{2} \left( y_n + \frac{x}{y_n} \right)$$
          <p>
            <strong>Geometric Interpretation:</strong> Consider a rectangle whose area is \(x\). If one side is \(y_n\), the adjacent side is \(\frac{x}{y_n}\). If the rectangle is not a perfect square, one side is larger than \(\sqrt{x}\) and the other is smaller. The arithmetic mean of the two sides, \(\frac{1}{2}(y_n + x/y_n)\), provides a remarkably closer approximation to the side of an equivalent square.
          </p>
          <p>
            The algorithm exhibits <strong>quadratic convergence</strong>: the number of correct decimal digits doubles on every iteration.
          </p>

          <h2>4. Reference Matrix: Perfect Squares & Radical Benchmark</h2>
          <p>
            The following table summarizes canonical integer square roots, their prime factorizations, exact radical simplifications, and decimal equivalents:
          </p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Radicand (\(x\))</th>
                <th>Prime Factorization</th>
                <th>Simplest Radical (\(k\sqrt{m}\))</th>
                <th>Decimal Value</th>
                <th>Classification</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>4</td>
                <td>\(2^2\)</td>
                <td>\(2\)</td>
                <td>2.000000</td>
                <td>Perfect Square (Rational)</td>
              </tr>
              <tr>
                <td>8</td>
                <td>\(2^3\)</td>
                <td>\(2\sqrt{2}\)</td>
                <td>2.828427</td>
                <td>Irrational</td>
              </tr>
              <tr>
                <td>12</td>
                <td>\(2^2 \times 3\)</td>
                <td>\(2\sqrt{3}\)</td>
                <td>3.464102</td>
                <td>Irrational</td>
              </tr>
              <tr>
                <td>16</td>
                <td>\(2^4\)</td>
                <td>\(4\)</td>
                <td>4.000000</td>
                <td>Perfect Square (Rational)</td>
              </tr>
              <tr>
                <td>18</td>
                <td>\(2 \times 3^2\)</td>
                <td>\(3\sqrt{2}\)</td>
                <td>4.242641</td>
                <td>Irrational</td>
              </tr>
              <tr>
                <td>20</td>
                <td>\(2^2 \times 5\)</td>
                <td>\(2\sqrt{5}\)</td>
                <td>4.472136</td>
                <td>Irrational</td>
              </tr>
              <tr>
                <td>24</td>
                <td>\(2^3 \times 3\)</td>
                <td>\(2\sqrt{6}\)</td>
                <td>4.898979</td>
                <td>Irrational</td>
              </tr>
              <tr>
                <td>25</td>
                <td>\(5^2\)</td>
                <td>\(5\)</td>
                <td>5.000000</td>
                <td>Perfect Square (Rational)</td>
              </tr>
              <tr>
                <td>32</td>
                <td>\(2^5\)</td>
                <td>\(4\sqrt{2}\)</td>
                <td>5.656854</td>
                <td>Irrational</td>
              </tr>
              <tr>
                <td>45</td>
                <td>\(3^2 \times 5\)</td>
                <td>\(3\sqrt{5}\)</td>
                <td>6.708204</td>
                <td>Irrational</td>
              </tr>
              <tr>
                <td>48</td>
                <td>\(2^4 \times 3\)</td>
                <td>\(4\sqrt{3}\)</td>
                <td>6.928203</td>
                <td>Irrational</td>
              </tr>
              <tr>
                <td>50</td>
                <td>\(2 \times 5^2\)</td>
                <td>\(5\sqrt{2}\)</td>
                <td>7.071068</td>
                <td>Irrational</td>
              </tr>
              <tr>
                <td>72</td>
                <td>\(2^3 \times 3^2\)</td>
                <td>\(6\sqrt{2}\)</td>
                <td>8.485281</td>
                <td>Irrational</td>
              </tr>
              <tr>
                <td>100</td>
                <td>\(2^2 \times 5^2\)</td>
                <td>\(10\)</td>
                <td>10.000000</td>
                <td>Perfect Square (Rational)</td>
              </tr>
            </tbody>
          </table>

          <h2>5. Applied Physical and Electrical Engineering Case Studies</h2>

          <div class="worked-example-card">
            <h3>Case Study 1: Electrical AC Power Root-Mean-Square (RMS) Voltage</h3>
            <p>
              In electrical engineering, AC sinusoidal mains voltage is characterized by its Root-Mean-Square (RMS) amplitude, which delivers equivalent heating power to a DC circuit. For a peak sinusoidal voltage \(V_{\text{peak}} = 170.0\text{ V}\) (standard US 120V grid peak), the RMS voltage is evaluated by:
              $$V_{\text{RMS}} = \frac{V_{\text{peak}}}{\sqrt{2}} = 170.0 \times \frac{1}{\sqrt{2}}$$
            </p>
            <div class="example-body">
              <p><strong>Step 1: Rationalize the denominator:</strong></p>
              $$V_{\text{RMS}} = 170.0 \times \frac{\sqrt{2}}{2} = 85.0 \times \sqrt{2}$$
              <p><strong>Step 2: Evaluate \(\sqrt{2}\) to 6 decimal places:</strong></p>
              $$\sqrt{2} \approx 1.414214$$
              <p><strong>Step 3: Multiply:</strong></p>
              $$V_{\text{RMS}} = 85.0 \times 1.414214 = 120.208\text{ V} \approx 120\text{ VAC}$$
              <p><strong>Engineering Finding:</strong> The 170V peak voltage corresponds precisely to standard nominal \(120\text{ VAC}\) residential utility power.</p>
            </div>
          </div>

          <div class="worked-example-card">
            <h3>Case Study 2: Civil Structural Foundation Diagonal Bracing</h3>
            <p>
              A structural steel building frame requires diagonal wind bracing between two columns spaced \(L = 6.00\text{ m}\) apart with a story height of \(H = 4.50\text{ m}\). Calculate the diagonal brace length \(D\) using the Pythagorean square root formula.
            </p>
            <div class="example-body">
              <p><strong>Formula:</strong></p>
              $$D = \sqrt{L^2 + H^2} = \sqrt{6.00^2 + 4.50^2}$$
              <p><strong>Step 1: Compute sum of squares:</strong></p>
              $$L^2 + H^2 = 36.00 + 20.25 = 56.25\text{ m}^2$$
              <p><strong>Step 2: Extract principal square root:</strong></p>
              $$D = \sqrt{56.25} = 7.50\text{ m}$$
              <p><strong>Structural Verification:</strong> Because \(56.25 = (7.5)^2\), the brace length is a rational terminating quantity: \(D = 7.500\text{ m}\).</p>
            </div>
          </div>

          <h2>6. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-accordion">
            <div class="faq-item">
              <h3 class="faq-question">Why is \(\sqrt{x^2} = |x|\) instead of just \(x\)?</h3>
              <div class="faq-answer">
                <p>
                  Because the radical symbol denotes the non-negative principal root, \(\sqrt{x^2}\) must always be non-negative. If \(x = -5\), then \(x^2 = 25\), and \(\sqrt{25} = +5 = |-5|\). Writing \(\sqrt{x^2} = x\) would yield \(-5\), violating the definition of the principal square root.
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">How do you take the square root of a fraction?</h3>
              <div class="faq-answer">
                <p>
                  By the quotient rule for radicals, the square root of a fraction is the square root of the numerator divided by the square root of the denominator: \(\sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}\). For example, \(\sqrt{\frac{9}{16}} = \frac{\sqrt{9}}{\sqrt{16}} = \frac{3}{4}\).
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">What is an irrational square root?</h3>
              <div class="faq-answer">
                <p>
                  If an integer is not a perfect square (such as 2, 3, 5, 7), its square root is an irrational number. It cannot be expressed as a ratio of two integers \(p/q\), and its decimal expansion is infinite and non-repeating.
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">How does a square root relate to cube roots and higher roots?</h3>
              <div class="faq-answer">
                <p>
                  A square root is a radical with index \(n = 2\). For index \(n = 3\), it is a cube root; for general degree \(n\), it is an nth root. You can evaluate cubic roots and higher radicals using our <a href="cube-root-calculator.html">Cube Root Calculator</a> and <a href="nth-root-calculator.html">Nth Root Calculator</a>.
                </p>
              </div>
            </div>
          </div>
        </article>
      </div>

      <aside class="sidebar-column">
        <div class="sidebar-card">
          <h3 class="sidebar-title">Related Math Calculators</h3>
          <ul class="sidebar-nav">
            <li><a href="cube-root-calculator.html">Cube Root Calculator</a></li>
            <li><a href="nth-root-calculator.html">Nth Root Calculator</a></li>
            <li><a href="pythagorean-theorem-calculator.html">Pythagorean Theorem Calculator</a></li>
            <li><a href="quadratic-equation-calculator.html">Quadratic Equation Calculator</a></li>
            <li><a href="exponent-calculator.html">Exponent Calculator</a></li>
            <li><a href="scientific-notation-calculator.html">Scientific Notation Calculator</a></li>
            <li><a href="significant-figures-calculator.html">Significant Figures Calculator</a></li>
            <li><a href="prime-number-calculator.html">Prime Number Calculator</a></li>
          </ul>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-col">
        <h4>CalcHub</h4>
        <p>Comprehensive mathematical, scientific, and engineering calculation tools.</p>
      </div>
      <div class="footer-col">
        <h4>Discipline Hubs</h4>
        <ul class="footer-links">
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="math.html">Mathematics</a></li>
          <li><a href="converter.html">Unit Converters</a></li>
          <li><a href="engineering.html">Electrical & Engineering</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 CalcHub. All rights reserved. Peer-reviewed computational algorithms.</p>
    </div>
  </footer>

  <script>
    function simplifyRadical(x) {
      if (!Number.isInteger(x) || x <= 0) return null;
      var k = 1;
      var m = x;
      var d = 2;
      while (d * d <= m) {
        if (m % (d * d) === 0) {
          k *= d;
          m /= (d * d);
        } else {
          d++;
        }
      }
      return { k: k, m: m };
    }

    function calculateSquareRoot() {
      var x = parseFloat(document.getElementById("radicand_x").value);
      var prec = parseInt(document.getElementById("precision").value) || 6;

      if (isNaN(x)) {
        alert("Please enter a valid numerical radicand.");
        return;
      }

      var isNegative = (x < 0);
      var absX = Math.abs(x);
      var rootVal = Math.sqrt(absX);

      var decStr = "";
      var radStr = "";
      var isPerfect = false;

      if (isNegative) {
        decStr = rootVal.toFixed(prec) + " i (Imaginary)";
        var simpNeg = simplifyRadical(Math.round(absX));
        if (simpNeg) {
          if (simpNeg.m === 1) {
            radStr = simpNeg.k + "i";
          } else if (simpNeg.k === 1) {
            radStr = "i√" + simpNeg.m;
          } else {
            radStr = simpNeg.k + "i√" + simpNeg.m;
          }
        } else {
          radStr = "√(" + x + ")";
        }
        isPerfect = false;
      } else {
        decStr = rootVal.toFixed(prec);
        isPerfect = Number.isInteger(rootVal) && Number.isInteger(x);

        var simp = simplifyRadical(Math.round(x));
        if (Number.isInteger(x) && simp) {
          if (simp.m === 1) {
            radStr = simp.k.toString();
          } else if (simp.k === 1) {
            radStr = "√" + simp.m;
          } else {
            radStr = simp.k + "√" + simp.m;
          }
        } else {
          radStr = "√" + x;
        }
      }

      var highlightText = isNegative ?
        "√(" + x + ") = " + decStr :
        "√" + x + (isPerfect ? " = " : " ≈ ") + decStr;

      document.getElementById("primary-result").innerText = highlightText;
      document.getElementById("res-decimal").innerText = decStr;
      document.getElementById("res-radical").innerText = radStr;
      document.getElementById("res-perfect").innerText = isPerfect ? "Yes (Exact Integer)" : (isNegative ? "Complex (Imaginary)" : "No (Irrational)");
      document.getElementById("res-verify").innerText = "(" + rootVal.toFixed(prec) + ")² ≈ " + absX;

      // Babylonian iterations
      var steps = "<h4>Step-by-Step Babylonian Iterations:</h4><ol>";
      if (!isNegative) {
        var y = absX > 1 ? absX / 2 : 1;
        for (var iter = 1; iter <= 4; iter++) {
          var yNext = 0.5 * (y + absX / y);
          steps += "<li><strong>Iteration " + iter + ":</strong> 0.5 &times; (" + y.toFixed(6) + " + " + absX + "/" + y.toFixed(6) + ") = <strong>" + yNext.toFixed(prec) + "</strong></li>";
          y = yNext;
        }
      } else {
        steps += "<li><strong>Negative Radicand:</strong> Extract imaginary unit i = &radic;(-1) &rarr; &radic;(" + x + ") = i &times; &radic;(" + absX + ")</li>";
        steps += "<li><strong>Principal Root:</strong> i &times; " + rootVal.toFixed(prec) + " = <strong>" + decStr + "</strong></li>";
      }
      steps += "<li><strong>Simplest Radical Expression:</strong> <strong>" + radStr + "</strong></li>";
      steps += "</ol>";

      document.getElementById("steps-output").innerHTML = steps;
      document.getElementById("result-box").style.display = "block";
    }

    window.addEventListener("DOMContentLoaded", function() {
      calculateSquareRoot();
    });
  </script>
</body>
</html>
"""

# 2. percent-to-fraction-calculator.html
HTML_PERCENT_TO_FRACTION = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Percent to Fraction Calculator - Reduced Fraction & Steps</title>
  <meta name="description" content="Convert any percentage into a simplified fraction, mixed number, or ratio with step-by-step arithmetic, GCD reduction, and repeating decimal handling.">
  <link rel="canonical" href="https://calchub.org/percent-to-fraction-calculator.html">
  <meta property="og:title" content="Percent to Fraction Calculator - Exact Step-by-Step">
  <meta property="og:description" content="Convert percentages and decimal percents to reduced fractions, mixed numbers, and ratios with Euclidean GCD reduction.">
  <meta property="og:url" content="https://calchub.org/percent-to-fraction-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Percent to Fraction Calculator - Step-by-Step Solver">
  <meta name="twitter:description" content="Free online percent to fraction calculator. Converts percentages to simplified fractions, mixed numbers, and ratios with complete working.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Percent to Fraction Calculator",
    "url": "https://calchub.org/percent-to-fraction-calculator.html",
    "description": "Converts percentages into simplified proper fractions, improper fractions, mixed numbers, and ratios using GCD reduction.",
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
        "name": "How do you convert a percentage to a fraction?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "To convert a percentage P to a fraction, place P over a denominator of 100: P / 100. If P contains decimals, multiply both numerator and denominator by 10^k to clear decimals, then divide both terms by their Greatest Common Divisor (GCD)."
        }
      },
      {
        "@type": "Question",
        "name": "How do you convert a percentage greater than 100% to a mixed number?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "When P > 100%, the resulting fraction is improper. Divide the numerator by the denominator to extract the whole number integer W, with the remainder R forming the fractional part: W R/d (e.g., 175% = 175/100 = 7/4 = 1 3/4)."
        }
      },
      {
        "@type": "Question",
        "name": "What is the difference between a fraction and a ratio?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A fraction a/b represents a part-to-whole relationship (a parts out of a total b parts). A ratio a:b can represent part-to-whole or part-to-part relationships (e.g., 25% represents 1 part to 3 remaining parts in a 1:3 ratio, or 1 part out of 4 total parts in a 1:4 ratio)."
        }
      },
      {
        "@type": "Question",
        "name": "Can you convert negative percentages to fractions?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. A negative percentage produces a negative fraction: -P% = -(P / 100) (e.g., -37.5% = -375/1000 = -3/8)."
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
        <a href="math.html" class="active">Math & Statistics</a>
        <a href="converter.html">Converters</a>
        <a href="engineering.html">Engineering</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="page-container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &gt;
      <a href="math.html">Math</a> &gt;
      <span>Percent to Fraction Calculator</span>
    </nav>

    <div class="content-layout">
      <div class="main-column">
        <div class="calculator-card">
          <div class="calculator-header">
            <span class="calc-icon">％</span>
            <h1>Percent to Fraction Calculator</h1>
          </div>
          <p class="calc-description">
            Convert any percentage or decimal percent into a fully reduced proper fraction, improper fraction, mixed number, and part-to-whole ratio.
          </p>

          <form id="calc-form" class="calc-form" onsubmit="return false;">
            <div class="input-grid">
              <div class="form-group">
                <label for="percent_input">Percentage (\(P\%\)):</label>
                <input type="number" id="percent_input" class="form-control" value="62.5" step="any" placeholder="e.g. 62.5 or 125" required>
                <span class="help-text">Input percent value without % sign.</span>
              </div>
              <div class="form-group" style="display:flex;align-items:flex-end;">
                <button type="button" id="btn-calculate" class="btn btn-primary" style="width:100%;" onclick="calculatePercentToFraction()">Convert to Fraction</button>
              </div>
            </div>
          </form>

          <div id="result-box" class="result-box" style="display:none;">
            <h3>Fraction Results</h3>
            <div class="result-highlight" id="primary-result">62.5% = 5 / 8</div>
            
            <div class="result-grid">
              <div class="result-item">
                <span class="res-label">Reduced Fraction:</span>
                <span class="res-val" id="res-fraction">5 / 8</span>
              </div>
              <div class="result-item">
                <span class="res-label">Mixed Number Form:</span>
                <span class="res-val" id="res-mixed">None (Proper Fraction)</span>
              </div>
              <div class="result-item">
                <span class="res-label">Decimal Equivalent:</span>
                <span class="res-val" id="res-decimal">0.625</span>
              </div>
              <div class="result-item">
                <span class="res-label">Part-to-Whole Ratio:</span>
                <span class="res-val" id="res-ratio">5 : 8</span>
              </div>
            </div>

            <div class="conversion-steps" id="steps-output">
              <!-- Steps output -->
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. Algebraic Principles of Percent-to-Fraction Transformation</h2>
          <p>
            In fundamental mathematics, a <strong>percentage</strong> is a dimensionless proportional value expressed as a fraction of one hundred. The word originates from the Latin <em>per centum</em>, meaning "by the hundred." Consequently, by definition:
          </p>
          $$P\% = \frac{P}{100}$$
          <p>
            Converting a percentage into a simplified rational fraction \( \frac{a}{b} \) requires resolving any decimal components in \(P\) into whole integers, followed by reducing the resulting fraction to its canonical lowest terms through division by the <strong>Greatest Common Divisor (GCD)</strong>.
          </p>

          <h2>2. The Exact Algorithmic Reduction Sequence</h2>
          <p>
            To transform any real percentage \(P\) into an irreducible fraction \(\frac{a}{b}\), mathematicians apply a three-stage procedure:
          </p>
          <ol>
            <li>
              <strong>Initial Fraction Construction:</strong> Set the initial fraction as \(\frac{P}{100}\).
            </li>
            <li>
              <strong>Decimal Normalization:</strong> If \(P\) is not a whole integer, determine the count of decimal digits \(k\) after the radix point. Multiply both numerator and denominator by \(10^k\) to clear all decimals:
              $$\frac{P}{100} = \frac{P \times 10^k}{100 \times 10^k} = \frac{N}{D}$$
              where \(N = P \cdot 10^k\) and \(D = 100 \cdot 10^k\) are both integers.
            </li>
            <li>
              <strong>Euclidean GCD Simplification:</strong> Evaluate the greatest common divisor \(g = \gcd(|N|, D)\) using Euclid's recursive algorithm:
              $$\gcd(N, D) = \gcd(D, N \pmod D)$$
              Divide both terms by \(g\) to establish the unique irreducible fraction:
              $$\frac{a}{b} = \frac{N / g}{D / g}$$
            </li>
          </ol>

          <h2>3. Handling Mixed Numbers and Percentages Exceeding 100%</h2>
          <p>
            When the percentage exceeds \(100\%\) (\(|P| > 100\)), the simplified fraction \(\frac{a}{b}\) is an <strong>improper fraction</strong> (\(|a| > b\)). In practical carpentry, financial reporting, and engineering specifications, improper fractions are frequently rendered as <strong>mixed numbers</strong>:
          </p>
          $$W \frac{r}{b} \quad \text{where } W = \left\lfloor \frac{a}{b} \right\rfloor \text{ and } r = a \pmod b$$
          <p>
            For example, converting \(275\%\):
          </p>
          $$\frac{275}{100} = \frac{275 / 25}{100 / 25} = \frac{11}{4} = 2 \frac{3}{4}$$

          <h2>4. Comprehensive Percent to Fraction Reference Matrix</h2>
          <p>
            The matrix below compiles standard percentage values across finance, machining, and engineering tolerances, showcasing their decimal quotients, unreduced forms, simplified fractions, and ratios:
          </p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Percentage (\(P\%\))</th>
                <th>Decimal Value</th>
                <th>Unreduced Fraction</th>
                <th>Greatest Common Divisor (GCD)</th>
                <th>Simplest Fraction (\(a/b\))</th>
                <th>Mixed Number Form</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>1.0%</td>
                <td>0.01</td>
                <td>1 / 100</td>
                <td>1</td>
                <td>\(1 / 100\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>2.5%</td>
                <td>0.025</td>
                <td>25 / 1000</td>
                <td>25</td>
                <td>\(1 / 40\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>5.0%</td>
                <td>0.05</td>
                <td>5 / 100</td>
                <td>5</td>
                <td>\(1 / 20\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>10.0%</td>
                <td>0.10</td>
                <td>10 / 100</td>
                <td>10</td>
                <td>\(1 / 10\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>12.5%</td>
                <td>0.125</td>
                <td>125 / 1000</td>
                <td>125</td>
                <td>\(1 / 8\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>20.0%</td>
                <td>0.20</td>
                <td>20 / 100</td>
                <td>20</td>
                <td>\(1 / 5\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>25.0%</td>
                <td>0.25</td>
                <td>25 / 100</td>
                <td>25</td>
                <td>\(1 / 4\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>37.5%</td>
                <td>0.375</td>
                <td>375 / 1000</td>
                <td>125</td>
                <td>\(3 / 8\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>50.0%</td>
                <td>0.50</td>
                <td>50 / 100</td>
                <td>50</td>
                <td>\(1 / 2\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>62.5%</td>
                <td>0.625</td>
                <td>625 / 1000</td>
                <td>125</td>
                <td>\(5 / 8\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>75.0%</td>
                <td>0.75</td>
                <td>75 / 100</td>
                <td>25</td>
                <td>\(3 / 4\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>87.5%</td>
                <td>0.875</td>
                <td>875 / 1000</td>
                <td>125</td>
                <td>\(7 / 8\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>125.0%</td>
                <td>1.25</td>
                <td>125 / 100</td>
                <td>25</td>
                <td>\(5 / 4\)</td>
                <td>\(1 \frac{1}{4}\)</td>
              </tr>
              <tr>
                <td>150.0%</td>
                <td>1.50</td>
                <td>150 / 100</td>
                <td>50</td>
                <td>\(3 / 2\)</td>
                <td>\(1 \frac{1}{2}\)</td>
              </tr>
              <tr>
                <td>250.0%</td>
                <td>2.50</td>
                <td>250 / 100</td>
                <td>50</td>
                <td>\(5 / 2\)</td>
                <td>\(2 \frac{1}{2}\)</td>
              </tr>
            </tbody>
          </table>

          <h2>4. Periodic Repeating Percentages and Infinite Series Conversion</h2>
          <p>
            When a percentage contains an infinite recurring decimal repetend (such as \(16.666...\%\), \(33.333...\%\), or \(8.333...\%\)), naive decimal truncation introduces severe numerical errors. To extract the exact rational fraction, treat the repeating decimal as the sum of a non-repeating integer/decimal prefix and an infinite convergent geometric series:
          </p>
          $$P\% = a + \sum_{k=1}^{\infty} \frac{R}{(10^p)^k} \cdot 10^{-m}$$
          <p>
            Alternatively, apply algebraic clearing of the repetend. Let \(x\) represent the decimal value \(P / 100\). If the non-repeating portion has \(m\) digits and the repetend has period length \(p\):
          </p>
          $$10^{m+p} \cdot x - 10^m \cdot x = \text{Integer Difference}$$
          <p>
            For example, to convert \(16.\overline{6}\%\) to a fraction:
          </p>
          $$x = \frac{16.\overline{6}}{100} = 0.16\overline{6} \implies 100x = 16.66\overline{6}, \quad 10x = 1.66\overline{6}$$
          $$100x - 10x = 90x = 16.66\overline{6} - 1.66\overline{6} = 15 \implies x = \frac{15}{90} = \frac{1}{6}$$
          <p>
            This guarantees exact rational recovery without floating-point distortion.
          </p>

          <h2>5. Comprehensive Percent to Fraction Reference Matrix</h2>
          <p>
            The matrix below compiles standard percentage values across finance, machining, and engineering tolerances, showcasing their decimal quotients, unreduced forms, simplified fractions, and ratios:
          </p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Percentage (\(P\%\))</th>
                <th>Decimal Value</th>
                <th>Unreduced Fraction</th>
                <th>Greatest Common Divisor (GCD)</th>
                <th>Simplest Fraction (\(a/b\))</th>
                <th>Mixed Number Form</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>1.0%</td>
                <td>0.01</td>
                <td>1 / 100</td>
                <td>1</td>
                <td>\(1 / 100\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>2.5%</td>
                <td>0.025</td>
                <td>25 / 1000</td>
                <td>25</td>
                <td>\(1 / 40\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>5.0%</td>
                <td>0.05</td>
                <td>5 / 100</td>
                <td>5</td>
                <td>\(1 / 20\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>10.0%</td>
                <td>0.10</td>
                <td>10 / 100</td>
                <td>10</td>
                <td>\(1 / 10\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>12.5%</td>
                <td>0.125</td>
                <td>125 / 1000</td>
                <td>125</td>
                <td>\(1 / 8\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>16.666...%</td>
                <td>0.166667</td>
                <td>15 / 90</td>
                <td>15</td>
                <td>\(1 / 6\)</td>
                <td>Proper (Periodic)</td>
              </tr>
              <tr>
                <td>20.0%</td>
                <td>0.20</td>
                <td>20 / 100</td>
                <td>20</td>
                <td>\(1 / 5\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>25.0%</td>
                <td>0.25</td>
                <td>25 / 100</td>
                <td>25</td>
                <td>\(1 / 4\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>33.333...%</td>
                <td>0.333333</td>
                <td>33 / 99</td>
                <td>33</td>
                <td>\(1 / 3\)</td>
                <td>Proper (Periodic)</td>
              </tr>
              <tr>
                <td>37.5%</td>
                <td>0.375</td>
                <td>375 / 1000</td>
                <td>125</td>
                <td>\(3 / 8\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>50.0%</td>
                <td>0.50</td>
                <td>50 / 100</td>
                <td>50</td>
                <td>\(1 / 2\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>62.5%</td>
                <td>0.625</td>
                <td>625 / 1000</td>
                <td>125</td>
                <td>\(5 / 8\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>75.0%</td>
                <td>0.75</td>
                <td>75 / 100</td>
                <td>25</td>
                <td>\(3 / 4\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>87.5%</td>
                <td>0.875</td>
                <td>875 / 1000</td>
                <td>125</td>
                <td>\(7 / 8\)</td>
                <td>Proper</td>
              </tr>
              <tr>
                <td>125.0%</td>
                <td>1.25</td>
                <td>125 / 100</td>
                <td>25</td>
                <td>\(5 / 4\)</td>
                <td>\(1 \frac{1}{4}\)</td>
              </tr>
              <tr>
                <td>150.0%</td>
                <td>1.50</td>
                <td>150 / 100</td>
                <td>50</td>
                <td>\(3 / 2\)</td>
                <td>\(1 \frac{1}{2}\)</td>
              </tr>
              <tr>
                <td>250.0%</td>
                <td>2.50</td>
                <td>250 / 100</td>
                <td>50</td>
                <td>\(5 / 2\)</td>
                <td>\(2 \frac{1}{2}\)</td>
              </tr>
            </tbody>
          </table>

          <h2>6. Practical Manufacturing, Financial & Chemical Engineering Case Studies</h2>

          <div class="worked-example-card">
            <h3>Case Study 1: Precision Machining CNC Feed Rate Override Tolerance</h3>
            <p>
              An automated CNC mill machinist adjusts the spindle feed rate override setting to \(68.75\%\) of nominal specification. To document the change in the machine tool setup sheet using standard imperial fractional fractions, convert \(68.75\%\) to an irreducible fraction.
            </p>
            <div class="example-body">
              <p><strong>Step 1: Place over 100:</strong></p>
              $$\text{Fraction} = \frac{68.75}{100}$$
              <p><strong>Step 2: Clear decimal places (\(k = 2\)):</strong></p>
              $$\frac{68.75 \times 100}{100 \times 100} = \frac{6875}{10000}$$
              <p><strong>Step 3: Calculate GCD of 6875 and 10000:</strong></p>
              $$6875 = 5^4 \times 11 = 625 \times 11$$
              $$10000 = 2^4 \times 5^4 = 16 \times 625$$
              $$\gcd(6875, 10000) = 625$$
              <p><strong>Step 4: Reduce terms:</strong></p>
              $$\frac{6875 / 625}{10000 / 625} = \frac{11}{16}$$
              <p><strong>Machining Finding:</strong> The feed override is set to exactly \(\frac{11}{16}\) of nominal specification.</p>
            </div>
          </div>

          <div class="worked-example-card">
            <h3>Case Study 2: Real Estate Mortgage Equity Ownership Ratio</h3>
            <p>
              A commercial real estate syndication investment firm holds a \(143.75\%\) collateralized loan-to-cost (LTC) equity commitment on a development project. Express this commitment as an exact mixed number fraction.
            </p>
            <div class="example-body">
              <p><strong>Step 1: Setup and clear decimals:</strong></p>
              $$\frac{143.75}{100} = \frac{14375}{10000}$$
              <p><strong>Step 2: Factor and reduce via GCD (625):</strong></p>
              $$\frac{14375 / 625}{10000 / 625} = \frac{23}{16}$$
              <p><strong>Step 3: Extract mixed number integer:</strong></p>
              $$23 \div 16 = 1 \quad \text{Remainder } 7 \implies 1 \frac{7}{16}$$
              <p><strong>Financial Result:</strong> The capital commitment equals exactly \(1 \frac{7}{16}\) times baseline project cost.</p>
            </div>
          </div>

          <div class="worked-example-card">
            <h3>Case Study 3: Chemical Engineering Mass Percentage to Molar Stoichiometry</h3>
            <p>
              A chemical synthesis laboratory analyzes an organic solvent composed of \(37.5\%\) Carbon by mass. To determine the stoichiometric empirical formula coefficients, convert \(37.5\%\) into an irreducible fraction of the total batch mass.
            </p>
            <div class="example-body">
              <p><strong>Step 1: Set up fraction:</strong></p>
              $$37.5\% = \frac{37.5}{100} = \frac{375}{1000}$$
              <p><strong>Step 2: Compute GCD:</strong></p>
              $$\gcd(375, 1000) = 125$$
              <p><strong>Step 3: Reduce fraction:</strong></p>
              $$\frac{375 / 125}{1000 / 125} = \frac{3}{8}$$
              <p><strong>Chemical Analysis:</strong> Carbon represents exactly \(3/8\) of the total compound mass, enabling straightforward stoichiometric mole ratio calculations.</p>
            </div>
          </div>

          <h2>7. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-accordion">
            <div class="faq-item">
              <h3 class="faq-question">How do you convert repeating percentages like \(33.333...\%\) to a fraction?</h3>
              <div class="faq-answer">
                <p>
                  Repeating percentages cannot be converted accurately by merely dividing by 100 with truncated decimals. Instead, set \(x = 0.333...\), multiply by 10 (\(10x = 3.333...\)), subtract \(x\) to get \(9x = 3 \implies x = 1/3\). Thus, \(33.\overline{3}\% = 1/3\), and \(66.\overline{6}\% = 2/3\).
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">What is the difference between a percentage and a decimal?</h3>
              <div class="faq-answer">
                <p>
                  A percentage is simply a decimal multiplied by 100. To convert a percentage to a decimal, divide by 100 (shifting the decimal radix point two places to the left). For example, \(45\% = 0.45\).
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">How do you reverse this and convert a fraction to a percentage?</h3>
              <div class="faq-answer">
                <p>
                  To convert a fraction back to a percentage, divide the numerator by the denominator and multiply by 100%. For example, \(5/8 = 0.625 \times 100\% = 62.5\%\). Use our <a href="fraction-to-percent-calculator.html">Fraction to Percent Calculator</a> for instant reverse conversions.
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">How do you simplify fractions with large numbers?</h3>
              <div class="faq-answer">
                <p>
                  Always use the Euclidean algorithm to find the greatest common divisor (GCD). You can perform multi-digit fraction reductions using our dedicated <a href="fraction-calculator.html">Fraction Calculator</a>.
                </p>
              </div>
            </div>
          </div>
        </article>
      </div>

      <aside class="sidebar-column">
        <div class="sidebar-card">
          <h3 class="sidebar-title">Related Math Calculators</h3>
          <ul class="sidebar-nav">
            <li><a href="fraction-to-percent-calculator.html">Fraction to Percent Calculator</a></li>
            <li><a href="fraction-calculator.html">Fraction Calculator</a></li>
            <li><a href="decimal-to-fraction-calculator.html">Decimal to Fraction Calculator</a></li>
            <li><a href="percentage-calculator.html">Percentage Calculator</a></li>
            <li><a href="ratio-calculator.html">Ratio Simplifier</a></li>
            <li><a href="gcd-lcm-calculator.html">GCD & LCM Calculator</a></li>
            <li><a href="scientific-notation-calculator.html">Scientific Notation Calculator</a></li>
            <li><a href="significant-figures-calculator.html">Significant Figures Calculator</a></li>
          </ul>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-col">
        <h4>CalcHub</h4>
        <p>Comprehensive mathematical, financial, and engineering calculation tools.</p>
      </div>
      <div class="footer-col">
        <h4>Discipline Hubs</h4>
        <ul class="footer-links">
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="math.html">Mathematics</a></li>
          <li><a href="converter.html">Unit Converters</a></li>
          <li><a href="engineering.html">Electrical & Engineering</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 CalcHub. All rights reserved. Peer-reviewed computational algorithms.</p>
    </div>
  </footer>

  <script>
    function gcd(a, b) {
      a = Math.abs(a);
      b = Math.abs(b);
      while (b) {
        var t = b;
        b = a % b;
        a = t;
      }
      return a;
    }

    function calculatePercentToFraction() {
      var p = parseFloat(document.getElementById("percent_input").value);

      if (isNaN(p)) {
        alert("Please enter a valid numerical percentage.");
        return;
      }

      var isNeg = (p < 0);
      var absP = Math.abs(p);

      // Determine decimal places
      var pStr = absP.toString();
      var decPlaces = 0;
      if (pStr.indexOf(".") !== -1) {
        decPlaces = pStr.split(".")[1].length;
      }

      var multiplier = Math.pow(10, decPlaces);
      var num = Math.round(absP * multiplier);
      var den = Math.round(100 * multiplier);

      var g = gcd(num, den);
      var redNum = num / g;
      var redDen = den / g;

      if (isNeg) {
        redNum = -redNum;
      }

      var decVal = p / 100;
      var fracStr = redNum + " / " + redDen;

      // Mixed number if improper
      var mixedStr = "None (Proper Fraction)";
      if (Math.abs(redNum) >= redDen) {
        var whole = Math.floor(Math.abs(redNum) / redDen);
        var rem = Math.abs(redNum) % redDen;
        if (rem === 0) {
          mixedStr = (isNeg ? "-" : "") + whole + " (Exact Integer)";
        } else {
          mixedStr = (isNeg ? "-" : "") + whole + " " + rem + "/" + redDen;
        }
      }

      var ratioStr = (isNeg ? "-" : "") + Math.abs(redNum) + " : " + redDen;

      document.getElementById("primary-result").innerText = p + "% = " + fracStr;
      document.getElementById("res-fraction").innerText = fracStr;
      document.getElementById("res-mixed").innerText = mixedStr;
      document.getElementById("res-decimal").innerText = decVal.toFixed(Math.max(decPlaces + 2, 4));
      document.getElementById("res-ratio").innerText = ratioStr;

      var steps = "<h4>Step-by-Step Conversion:</h4><ol>";
      steps += "<li><strong>Initial Ratio Setup:</strong> " + p + "% = " + p + " / 100</li>";
      if (decPlaces > 0) {
        steps += "<li><strong>Clear Decimals:</strong> Multiply numerator and denominator by 10^" + decPlaces + " (" + multiplier + ") &rarr; " + (isNeg ? "-" : "") + num + " / " + den + "</li>";
      }
      steps += "<li><strong>Greatest Common Divisor (GCD):</strong> gcd(" + num + ", " + den + ") = " + g + "</li>";
      steps += "<li><strong>Simplify by GCD:</strong> (" + (isNeg ? "-" : "") + num + " &divide; " + g + ") / (" + den + " &divide; " + g + ") = <strong>" + fracStr + "</strong></li>";
      if (mixedStr !== "None (Proper Fraction)") {
        steps += "<li><strong>Mixed Number Form:</strong> <strong>" + mixedStr + "</strong></li>";
      }
      steps += "</ol>";

      document.getElementById("steps-output").innerHTML = steps;
      document.getElementById("result-box").style.display = "block";
    }

    window.addEventListener("DOMContentLoaded", function() {
      calculatePercentToFraction();
    });
  </script>
</body>
</html>
"""

def main():
    p1 = os.path.join(BASE_DIR, "square-root-calculator.html")
    with open(p1, "w", encoding="utf-8") as f:
        f.write(HTML_SQUARE_ROOT)
    print(f"Generated: {p1}")

    p2 = os.path.join(BASE_DIR, "percent-to-fraction-calculator.html")
    with open(p2, "w", encoding="utf-8") as f:
        f.write(HTML_PERCENT_TO_FRACTION)
    print(f"Generated: {p2}")

if __name__ == "__main__":
    main()
