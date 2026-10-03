# -*- coding: utf-8 -*-
"""
Generator for Batch 29 - Part 2:
3. logarithm-calculator.html
4. long-division-calculator.html
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 3. logarithm-calculator.html
HTML_LOGARITHM = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Logarithm Calculator - Log, Ln, Log2 & Change of Base</title>
  <meta name="description" content="Calculate logarithms for any base: natural log ln(x), common log log10(x), binary log log2(x), and arbitrary base log_b(x) with step-by-step algebraic identities.">
  <link rel="canonical" href="https://calchub.org/logarithm-calculator.html">
  <meta property="og:title" content="Logarithm Calculator - Log10, Ln, Log2 & Arbitrary Bases">
  <meta property="og:description" content="Compute natural logarithms, common logarithms, binary logs, and change of base transformations with full mathematical properties and engineering applications.">
  <meta property="og:url" content="https://calchub.org/logarithm-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Logarithm Calculator - Natural Log & Change of Base">
  <meta name="twitter:description" content="Free scientific logarithm solver. Computes ln, log10, log2, and arbitrary base logs with decibel, pH, and information entropy derivations.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Logarithm Calculator",
    "url": "https://calchub.org/logarithm-calculator.html",
    "description": "Calculates natural log ln(x), common log log10(x), binary log log2(x), and arbitrary base logarithms with change-of-base identities and step-by-step solutions.",
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
        "name": "What is the definition of a logarithm?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A logarithm is the exponent to which a specified base b must be raised to produce a given number x. Mathematically, y = log_b(x) is equivalent to b^y = x, where x > 0, b > 0, and b ≠ 1."
        }
      },
      {
        "@type": "Question",
        "name": "What is the difference between log, ln, and log2?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Common log log10(x) utilizes base 10 (prevalent in acoustics and chemistry). Natural log ln(x) uses Euler's constant e ≈ 2.71828 (foundational in calculus and physical kinetics). Binary log log2(x) uses base 2 (ubiquitous in computer science and information theory)."
        }
      },
      {
        "@type": "Question",
        "name": "Why can you not take the logarithm of a negative number or zero?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "In real arithmetic, raising any positive base b to any real power y always yields a strictly positive result (b^y > 0). Therefore, b^y cannot equal zero or a negative number. In complex analysis, logarithms of negative numbers exist and involve imaginary multiples of π: ln(-x) = ln(x) + iπ."
        }
      },
      {
        "@type": "Question",
        "name": "What is the change of base formula?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The change of base formula allows calculating a logarithm in any base b using natural or common logarithms: log_b(x) = ln(x) / ln(b) = log10(x) / log10(b)."
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
      <span>Logarithm Calculator</span>
    </nav>

    <div class="content-layout">
      <div class="main-column">
        <div class="calculator-card">
          <div class="calculator-header">
            <span class="calc-icon">🪵</span>
            <h1>Logarithm Calculator</h1>
          </div>
          <p class="calc-description">
            Evaluate arbitrary base logarithms \(\log_b(x)\), natural log \(\ln(x)\), common log \(\log_{10}(x)\), and binary log \(\log_2(x)\) with change-of-base expansions and analytical properties.
          </p>

          <form id="calc-form" class="calc-form" onsubmit="return false;">
            <div class="input-grid">
              <div class="form-group">
                <label for="log_argument">Argument (\(x\)):</label>
                <input type="number" id="log_argument" class="form-control" value="1000" step="any" min="0.000000000000001" placeholder="e.g. 1000" required>
                <span class="help-text">Input value (\(x > 0\)).</span>
              </div>
              <div class="form-group">
                <label for="log_base">Base (\(b\)):</label>
                <input type="number" id="log_base" class="form-control" value="10" step="any" min="0.000000000000001" placeholder="e.g. 10 or 2" required>
                <span class="help-text">Base (\(b > 0, b \neq 1\)).</span>
              </div>
              <div class="form-group">
                <label for="precision">Output Precision:</label>
                <select id="precision" class="form-control">
                  <option value="4">4 decimal places</option>
                  <option value="6" selected>6 decimal places (High)</option>
                  <option value="8">8 decimal places</option>
                  <option value="12">12 decimal places (Scientific)</option>
                </select>
                <span class="help-text">Display precision for results.</span>
              </div>
              <div class="form-group">
                <label for="quick_base">Quick Preset Bases:</label>
                <select id="quick_base" class="form-control" onchange="setQuickBase(this.value)">
                  <option value="10" selected>Base 10 (Common Log, log₁₀)</option>
                  <option value="e">Base e (Natural Log, ln)</option>
                  <option value="2">Base 2 (Binary Log, log₂)</option>
                  <option value="custom">Custom Base</option>
                </select>
                <span class="help-text">Pre-fill standard scientific bases.</span>
              </div>
            </div>

            <button type="button" id="btn-calculate" class="btn btn-primary" onclick="calculateLogarithm()">Compute Logarithm</button>
          </form>

          <div id="result-box" class="result-box" style="display:none;">
            <h3>Logarithmic Results</h3>
            <div class="result-highlight" id="primary-result">log₁₀(1000) = 3</div>
            
            <div class="result-grid">
              <div class="result-item">
                <span class="res-label">Natural Log (\(\ln x\)):</span>
                <span class="res-val" id="res-ln">6.907755</span>
              </div>
              <div class="result-item">
                <span class="res-label">Common Log (\(\log_{10} x\)):</span>
                <span class="res-val" id="res-log10">3.000000</span>
              </div>
              <div class="result-item">
                <span class="res-label">Binary Log (\(\log_2 x\)):</span>
                <span class="res-val" id="res-log2">9.965784</span>
              </div>
              <div class="result-item">
                <span class="res-label">Inverse Check (\(b^y\)):</span>
                <span class="res-val" id="res-inverse">10³ = 1000</span>
              </div>
            </div>

            <div class="conversion-steps" id="steps-output">
              <!-- Analytical steps populated dynamically -->
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. Theoretical Foundations of the Logarithmic Function</h2>
          <p>
            In mathematical analysis, a <strong>logarithm</strong> is the inverse mathematical operation to exponentiation. For a given positive base \(b\) (where \(b > 0\) and \(b \neq 1\)) and a strictly positive real argument \(x > 0\), the logarithm \(y = \log_b(x)\) represents the exact real exponent to which \(b\) must be raised to yield \(x\):
          </p>
          $$y = \log_b(x) \iff b^y = x$$
          <p>
            Introduced historically by John Napier in 1614 to simplify astronomical and trigonometric multiplications into manageable additions, logarithms fundamentally compress multi-order-of-magnitude exponential ranges onto linear computational scales.
          </p>
          <p>
            The analytical domain of the real logarithmic function is strictly positive:
          </p>
          $$\text{Domain: } x \in (0, +\infty), \quad \text{Range: } y \in (-\infty, +\infty)$$
          <p>
            When \(x \to 0^+\), \(\log_b(x) \to -\infty\) (for \(b > 1\)). At the unit argument, \(\log_b(1) = 0\) for every valid base because \(b^0 = 1\). At the base itself, \(\log_b(b) = 1\) because \(b^1 = b\).
          </p>

          <h2>2. Canonical Logarithm Bases and Their Scientific Roles</h2>
          <p>
            While any positive real number distinct from 1 can serve as a base, three specific logarithmic bases dominate modern physical, computational, and financial systems:
          </p>
          <ol>
            <li>
              <strong>Natural Logarithm (\(\ln x = \log_e x\)):</strong> Anchored to Euler's transcendental constant \(e = \lim_{n \to \infty} (1 + 1/n)^n \approx 2.718281828459\dots\). The natural logarithm is uniquely characterized in calculus by its derivative:
              $$\frac{d}{dx} \ln(x) = \frac{1}{x} \implies \int \frac{1}{x} \, dx = \ln|x| + C$$
              This makes \(\ln(x)\) the canonical language of continuous compounding, chemical reaction kinetics (Arrhenius equation), radioactive decay, and thermal conduction.
            </li>
            <li>
              <strong>Common Logarithm (\(\log_{10} x = \lg x\)):</strong> Based on the decimal radix 10. Every integer increase in the common logarithm signifies a 10-fold multiplicative expansion (one order of magnitude). It is the basis for empirical scientific scales:
              <ul>
                <li><strong>Acoustics & Signal Processing:</strong> Sound Pressure Level (SPL) and power gains in Decibels (\(\text{dB} = 10 \log_{10}(P/P_0)\) or \(20 \log_{10}(V/V_0)\)).</li>
                <li><strong>Chemistry:</strong> The acidity/alkalinity scale \(\text{pH} = -\log_{10}[\text{H}^+]\).</li>
                <li><strong>Seismology:</strong> The Richter earthquake magnitude scale \(M = \log_{10}(A/A_0)\).</li>
                <li><strong>Spectrophotometry:</strong> Optical absorbance \(A = -\log_{10}(T)\).</li>
              </ul>
            </li>
            <li>
              <strong>Binary Logarithm (\(\log_2 x = \text{lb } x\)):</strong> Based on radix 2. Foundational in digital computer science, algorithmic complexity, and Claude Shannon's information theory. The quantity \(\log_2(N)\) dictates the height of a balanced binary search tree, the minimum number of binary questions required to isolate an item in a set of size \(N\), and Shannon information entropy:
              $$H(X) = -\sum_{i=1}^n P(x_i) \log_2 P(x_i) \quad [\text{bits / shannons}]$$
            </li>
          </ol>

          <h2>3. Fundamental Algebraic Laws and Identities of Logarithms</h2>
          <p>
            All logarithmic calculations satisfy a set of invariant algebraic laws directly inherited from the fundamental laws of exponents:
          </p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Identity Name</th>
                <th>Logarithmic Formulation</th>
                <th>Dual Exponential Law</th>
                <th>Analytical Utility</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Product Rule</strong></td>
                <td>\(\log_b(xy) = \log_b(x) + \log_b(y)\)</td>
                <td>\(b^{u+v} = b^u \cdot b^v\)</td>
                <td>Transforms multiplication into addition</td>
              </tr>
              <tr>
                <td><strong>Quotient Rule</strong></td>
                <td>\(\log_b(x/y) = \log_b(x) - \log_b(y)\)</td>
                <td>\(b^{u-v} = b^u / b^v\)</td>
                <td>Transforms division into subtraction</td>
              </tr>
              <tr>
                <td><strong>Power Rule</strong></td>
                <td>\(\log_b(x^k) = k \cdot \log_b(x)\)</td>
                <td>\((b^u)^k = b^{uk}\)</td>
                <td>Pulls exponents down into linear multipliers</td>
              </tr>
              <tr>
                <td><strong>Root Rule</strong></td>
                <td>\(\log_b(\sqrt[k]{x}) = \frac{1}{k} \log_b(x)\)</td>
                <td>\(b^{u/k} = (b^u)^{1/k}\)</td>
                <td>Simplifies high-order radicals into scalar division</td>
              </tr>
              <tr>
                <td><strong>Change of Base</strong></td>
                <td>\(\log_b(x) = \frac{\log_k(x)}{\log_k(b)} = \frac{\ln(x)}{\ln(b)}\)</td>
                <td>\((k^v)^u = k^{uv}\)</td>
                <td>Enables evaluation on scientific processors</td>
              </tr>
              <tr>
                <td><strong>Reciprocal Base</strong></td>
                <td>\(\log_b(x) = \frac{1}{\log_x(b)}\)</td>
                <td>\(b = x^{1/\log_b(x)}\)</td>
                <td>Inverts base and argument</td>
              </tr>
              <tr>
                <td><strong>Base Power Rule</strong></td>
                <td>\(\log_{b^m}(x) = \frac{1}{m} \log_b(x)\)</td>
                <td>\((b^m)^{y/m} = b^y\)</td>
                <td>Extracts exponent from base</td>
              </tr>
            </tbody>
          </table>

          <h2>4. Change of Base Formula: Mathematical Proof</h2>
          <p>
            Because microprocessors and calculators natively compute natural logarithms (\(\ln\)) via Chebyshev polynomials or Padé rational approximations, arbitrary base logarithms \(\log_b(x)\) are universally computed via the <strong>Change of Base Formula</strong>.
          </p>
          <p><strong>Formal Derivation:</strong></p>
          <ol>
            <li>Let \(y = \log_b(x)\). By definition, \(b^y = x\).</li>
            <li>Take the natural logarithm of both sides: \(\ln(b^y) = \ln(x)\).</li>
            <li>Apply the power rule on the left side: \(y \cdot \ln(b) = \ln(x)\).</li>
            <li>Since \(b > 0\) and \(b \neq 1\), \(\ln(b) \neq 0\). Divide both sides by \(\ln(b)\):</li>
          </ol>
          $$y = \frac{\ln(x)}{\ln(b)} \implies \log_b(x) = \frac{\ln(x)}{\ln(b)}$$

          <h2>5. Engineering and Physical Science Case Studies</h2>

          <div class="worked-example-card">
            <h3>Case Study 1: RF Antenna Power Gain in Decibels (dB)</h3>
            <p>
              A telecommunications microwave transmitter boosts an initial input signal power of \(P_{\text{in}} = 2.5\text{ mW}\) to an amplified output power of \(P_{\text{out}} = 125\text{ W}\) (\(125,000\text{ mW}\)). Compute the amplifier's power gain in decibels (\(\text{dB}\)) using common logarithms.
            </p>
            <div class="example-body">
              <p><strong>Formula:</strong></p>
              $$G_{\text{dB}} = 10 \cdot \log_{10}\left(\frac{P_{\text{out}}}{P_{\text{in}}}\right)$$
              <p><strong>Step 1: Calculate the dimensionless power ratio:</strong></p>
              $$\text{Ratio} = \frac{125,000\text{ mW}}{2.5\text{ mW}} = 50,000$$
              <p><strong>Step 2: Evaluate the common logarithm \(\log_{10}(50,000)\):</strong></p>
              $$\log_{10}(50,000) = \log_{10}(5 \times 10^4) = \log_{10}(5) + \log_{10}(10^4) = 0.698970 + 4 = 4.698970$$
              <p><strong>Step 3: Multiply by 10:</strong></p>
              $$G_{\text{dB}} = 10 \times 4.698970 = 46.9897\text{ dB}$$
              <p><strong>Engineering Conclusion:</strong> The RF transmitter delivers an exact power gain of \(46.99\text{ dB}\).</p>
            </div>
          </div>

          <div class="worked-example-card">
            <h3>Case Study 2: Water Chemistry pH and Hydronium Ion Concentration</h3>
            <p>
              An environmental water treatment facility measures a hydronium ion concentration of \([\text{H}_3\text{O}^+] = 3.16 \times 10^{-8}\text{ mol/L}\) in a municipal effluent reservoir. Determine the exact pH of the discharge water.
            </p>
            <div class="example-body">
              <p><strong>Formula:</strong></p>
              $$\text{pH} = -\log_{10}[\text{H}_3\text{O}^+]$$
              <p><strong>Step 1: Apply the logarithm power and product rules:</strong></p>
              $$\log_{10}(3.16 \times 10^{-8}) = \log_{10}(3.16) + \log_{10}(10^{-8}) = 0.499687 - 8 = -7.500313$$
              <p><strong>Step 2: Negate the result:</strong></p>
              $$\text{pH} = -(-7.500313) = 7.5003 \approx 7.50$$
              <p><strong>Chemical Analysis:</strong> The municipal effluent has a slightly basic pH of 7.50, fully compliant with environmental discharge standards (6.5 to 8.5).</p>
            </div>
          </div>

          <h2>6. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-accordion">
            <div class="faq-item">
              <h3 class="faq-question">What is \(\log(0)\)? Why is it undefined?</h3>
              <div class="faq-answer">
                <p>
                  In real arithmetic, \(\log_b(0)\) is undefined. Raising any positive base \(b > 0\) to any finite exponent \(y\) yields \(b^y > 0\). As \(y \to -\infty\), \(b^y \to 0\), but it never reaches 0 for any finite number. Thus, \(\lim_{x \to 0^+} \log_b(x) = -\infty\), creating a vertical asymptote at the y-axis.
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">Can logarithms have negative values?</h3>
              <div class="faq-answer">
                <p>
                  Yes! While the input argument \(x\) must be strictly positive (\(x > 0\)), the output logarithm \(\log_b(x)\) is negative whenever \(0 < x < 1\) (assuming \(b > 1\)). For example, \(\log_{10}(0.01) = -2\) because \(10^{-2} = 1/100 = 0.01\).
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">How does a logarithm work in computer algorithm complexity \(O(\log n)\)?</h3>
              <div class="faq-answer">
                <p>
                  An algorithm with \(O(\log n)\) time complexity (like binary search) cuts the problem size in half on each step. For an array of size \(n = 1,000,000\), binary search requires at most \(\lceil \log_2(1,000,000) \rceil = 20\) comparisons, illustrating the logarithmic compression power.
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">What is the relationship between logarithms and exponents?</h3>
              <div class="faq-answer">
                <p>
                  Logarithms and exponents are mutual inverses. If you take the logarithm of an exponent: \(\log_b(b^x) = x\). If you exponentiate a logarithm: \(b^{\log_b(x)} = x\). You can compute powers and exponential curves using our <a href="exponent-calculator.html">Exponent Calculator</a> or <a href="scientific-notation-calculator.html">Scientific Notation Calculator</a>.
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
            <li><a href="exponent-calculator.html">Exponent Calculator</a></li>
            <li><a href="scientific-notation-calculator.html">Scientific Notation Calculator</a></li>
            <li><a href="significant-figures-calculator.html">Significant Figures Calculator</a></li>
            <li><a href="cube-root-calculator.html">Cube Root Calculator</a></li>
            <li><a href="geometric-sequence-calculator.html">Geometric Sequence Calculator</a></li>
            <li><a href="factorial-calculator.html">Factorial Calculator</a></li>
            <li><a href="quadratic-equation-calculator.html">Quadratic Equation Calculator</a></li>
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
        <p>Advanced engineering, scientific, and mathematical calculation engines.</p>
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
    function setQuickBase(val) {
      if (val === "10") {
        document.getElementById("log_base").value = "10";
      } else if (val === "e") {
        document.getElementById("log_base").value = Math.E.toFixed(10);
      } else if (val === "2") {
        document.getElementById("log_base").value = "2";
      }
      calculateLogarithm();
    }

    function calculateLogarithm() {
      var x = parseFloat(document.getElementById("log_argument").value);
      var b = parseFloat(document.getElementById("log_base").value);
      var prec = parseInt(document.getElementById("precision").value) || 6;

      if (isNaN(x) || x <= 0) {
        alert("The argument x must be a strictly positive real number (x > 0).");
        return;
      }
      if (isNaN(b) || b <= 0 || Math.abs(b - 1) < 1e-12) {
        alert("The base b must be positive and not equal to 1 (b > 0, b ≠ 1).");
        return;
      }

      var lnX = Math.log(x);
      var lnB = Math.log(b);
      var logBX = lnX / lnB;
      var log10X = Math.log10 ? Math.log10(x) : (lnX / Math.LN10);
      var log2X = Math.log2 ? Math.log2(x) : (lnX / Math.LN2);

      // Format base label
      var baseLabel = Math.abs(b - Math.E) < 1e-6 ? "e" : b.toString();

      document.getElementById("primary-result").innerText = "log" + (baseLabel === "e" ? "ₑ" : "₍" + baseLabel + "₎") + "(" + x + ") = " + logBX.toFixed(prec);
      document.getElementById("res-ln").innerText = lnX.toFixed(prec);
      document.getElementById("res-log10").innerText = log10X.toFixed(prec);
      document.getElementById("res-log2").innerText = log2X.toFixed(prec);
      document.getElementById("res-inverse").innerText = b + "^(" + logBX.toFixed(prec) + ") ≈ " + Math.pow(b, logBX).toFixed(prec);

      var steps = "<h4>Step-by-Step Calculation:</h4><ol>";
      steps += "<li><strong>Change of Base Formula:</strong> log_b(x) = ln(x) / ln(b)</li>";
      steps += "<li><strong>Evaluate Natural Logs:</strong> ln(" + x + ") = " + lnX.toFixed(prec + 2) + ", ln(" + b + ") = " + lnB.toFixed(prec + 2) + "</li>";
      steps += "<li><strong>Perform Division:</strong> " + lnX.toFixed(prec + 2) + " &divide; " + lnB.toFixed(prec + 2) + " = <strong>" + logBX.toFixed(prec) + "</strong></li>";
      steps += "<li><strong>Exponential Verification:</strong> (" + b + ")^(" + logBX.toFixed(prec) + ") = <strong>" + Math.pow(b, logBX).toFixed(4) + "</strong> &approx; " + x + "</li>";
      steps += "</ol>";

      document.getElementById("steps-output").innerHTML = steps;
      document.getElementById("result-box").style.display = "block";
    }

    window.addEventListener("DOMContentLoaded", function() {
      calculateLogarithm();
    });
  </script>
</body>
</html>
"""

# 4. long-division-calculator.html
HTML_LONG_DIVISION = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Long Division Calculator with Remainders & Steps</title>
  <meta name="description" content="Free long division calculator with step-by-step working, quotient, remainder, decimal representation, and Euclidean division algorithm breakdown.">
  <link rel="canonical" href="https://calchub.org/long-division-calculator.html">
  <meta property="og:title" content="Long Division Calculator with Steps & Remainders">
  <meta property="og:description" content="Calculate quotients, remainders, and decimal expansions with clear step-by-step visual long division tableau and Euclidean algorithm checks.">
  <meta property="og:url" content="https://calchub.org/long-division-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Long Division Calculator - Detailed Working & Steps">
  <meta name="twitter:description" content="Online long division solver. Computes quotient, remainder, decimal conversion, and step-by-step long division workings for any integers or decimals.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Long Division Calculator",
    "url": "https://calchub.org/long-division-calculator.html",
    "description": "Calculates integer quotient, remainder, fractional form, and decimal expansion using the classical Euclidean long division algorithm with visual steps.",
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
        "name": "What is the Euclidean Division Algorithm?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Division Algorithm states that for any integer dividend A and positive integer divisor B, there exist unique integers Q (quotient) and R (remainder) such that: A = B · Q + R, where 0 ≤ R < B."
        }
      },
      {
        "@type": "Question",
        "name": "What is the difference between quotient and remainder?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The quotient is the greatest whole number of times the divisor fits into the dividend. The remainder is the integer quantity left over after that complete integer division."
        }
      },
      {
        "@type": "Question",
        "name": "How is long division represented as a mixed number and decimal?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "In mixed number form: A / B = Q + (R / B) = Q R/B. In decimal form, long division continues past the decimal radix point by appending zeros to successive remainders."
        }
      },
      {
        "@type": "Question",
        "name": "Can you perform long division with negative numbers?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. Under canonical Euclidean division, the remainder R is strictly non-negative (0 ≤ R < |B|). If A is negative, Q is chosen such that R remains positive (e.g., -25 ÷ 4 yields Q = -7 and R = 3, because 4 · (-7) + 3 = -25)."
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
      <span>Long Division Calculator</span>
    </nav>

    <div class="content-layout">
      <div class="main-column">
        <div class="calculator-card">
          <div class="calculator-header">
            <span class="calc-icon">➗</span>
            <h1>Long Division Calculator</h1>
          </div>
          <p class="calc-description">
            Execute step-by-step long division on any integers or decimals to determine the integer quotient, Euclidean remainder, fractional remainder, and repeating decimal expansion.
          </p>

          <form id="calc-form" class="calc-form" onsubmit="return false;">
            <div class="input-grid">
              <div class="form-group">
                <label for="dividend">Dividend (\(A\)):</label>
                <input type="number" id="dividend" class="form-control" value="487" step="any" placeholder="e.g. 487" required>
                <span class="help-text">Number being divided.</span>
              </div>
              <div class="form-group">
                <label for="divisor">Divisor (\(B\)):</label>
                <input type="number" id="divisor" class="form-control" value="32" step="any" placeholder="e.g. 32" required>
                <span class="help-text">Number dividing by (not 0).</span>
              </div>
              <div class="form-group">
                <label for="decimal_places">Decimal Digits:</label>
                <select id="decimal_places" class="form-control">
                  <option value="4" selected>4 decimal places</option>
                  <option value="6">6 decimal places</option>
                  <option value="8">8 decimal places</option>
                </select>
                <span class="help-text">Precision for decimal quotient.</span>
              </div>
            </div>

            <button type="button" id="btn-calculate" class="btn btn-primary" onclick="calculateLongDivision()">Execute Long Division</button>
          </form>

          <div id="result-box" class="result-box" style="display:none;">
            <h3>Long Division Results</h3>
            <div class="result-highlight" id="primary-result">Quotient: 15 R 7</div>
            
            <div class="result-grid">
              <div class="result-item">
                <span class="res-label">Integer Quotient (\(Q\)):</span>
                <span class="res-val" id="res-quotient">15</span>
              </div>
              <div class="result-item">
                <span class="res-label">Remainder (\(R\)):</span>
                <span class="res-val" id="res-remainder">7</span>
              </div>
              <div class="result-item">
                <span class="res-label">Mixed Number Form:</span>
                <span class="res-val" id="res-mixed">15 7/32</span>
              </div>
              <div class="result-item">
                <span class="res-label">Exact Decimal Value:</span>
                <span class="res-val" id="res-decimal">15.21875</span>
              </div>
            </div>

            <div class="conversion-steps" id="division-steps">
              <!-- Visual steps output -->
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. The Mathematical Theory of Long Division</h2>
          <p>
            In arithmetic and elementary number theory, <strong>division</strong> is the inverse operation of multiplication. When dividing an integer dividend \(A\) by a non-zero integer divisor \(B\), the fundamental <strong>Euclidean Division Theorem</strong> guarantees the existence of two unique integers: the <strong>quotient</strong> \(Q\) and the <strong>remainder</strong> \(R\), satisfying:
          </p>
          $$A = B \cdot Q + R \quad \text{where } 0 \le R < |B|$$
          <p>
            Here:
          </p>
          <ul>
            <li><strong>Dividend (\(A\)):</strong> The total quantity subject to partition.</li>
            <li><strong>Divisor (\(B\)):</strong> The size or count of equal partitions into which \(A\) is divided (\(B \neq 0\)).</li>
            <li><strong>Quotient (\(Q\)):</strong> The integer number of complete groups formed: \(Q = \lfloor A / B \rfloor\).</li>
            <li><strong>Remainder (\(R\)):</strong> The leftover integer that cannot form another full partition: \(R = A - (B \cdot Q)\).</li>
          </ul>
          <p>
            When \(R = 0\), we say that \(B\) divides \(A\) evenly (\(B \mid A\)), making \(B\) an aliquot factor or divisor of \(A\). When \(R > 0\), the rational quotient can be written in fractional or mixed form:
          </p>
          $$\frac{A}{B} = Q + \frac{R}{B} = Q \frac{R}{B}$$

          <h2>2. The Classical Long Division Algorithm Walkthrough</h2>
          <p>
            The traditional pen-and-paper long division algorithm decomposes a complex multi-digit division into a recursive four-stage cycle: <em>Divide, Multiply, Subtract, Bring Down</em> (frequently memorized through the mnemonic DMSB).
          </p>
          <ol>
            <li>
              <strong>Divide:</strong> Examine the leftmost prefix of digits of the dividend \(A\). Determine the largest single digit \(d \in \{0, 1, \dots, 9\}\) such that \(d \cdot B\) does not exceed the current working value. Place \(d\) in the quotient row above.
            </li>
            <li>
              <strong>Multiply:</strong> Compute the product \(d \cdot B\).
            </li>
            <li>
              <strong>Subtract:</strong> Subtract \(d \cdot B\) from the current working value to find the intermediate partial remainder: \(r_{\text{part}} = \text{Current} - (d \cdot B)\). By design, \(0 \le r_{\text{part}} < B\).
            </li>
            <li>
              <strong>Bring Down:</strong> Append the next digit of the dividend to the right of the partial remainder to form the new working value: \(\text{Next} = (r_{\text{part}} \times 10) + \text{digit}\).
            </li>
            <li>
              <strong>Iterate:</strong> Repeat stages 1 through 4 until all digits of the dividend have been consumed. The final subtraction yields the integer remainder \(R\).
            </li>
          </ol>

          <h2>3. Decimal Expansion and Periodicity Analysis</h2>
          <p>
            If a decimal result is desired rather than an integer quotient and remainder, the algorithm does not terminate when the dividend's digits run out. Instead, a decimal radix point is placed in the quotient, and a sequence of trailing zeros (\(0\)) is brought down consecutively:
          </p>
          $$R_1 = (R \times 10) - (d_1 \cdot B), \quad R_2 = (R_1 \times 10) - (d_2 \cdot B), \quad \dots$$
          <p>
            The behavior of this sequence depends entirely on the prime factorization of the reduced denominator \(B / \gcd(A, B)\):
          </p>
          <ul>
            <li>
              <strong>Terminating Decimal:</strong> If \(B = 2^m \cdot 5^n\), the remainder eventually hits 0 within \(\max(m, n)\) steps.
            </li>
            <li>
              <strong>Repeating Decimal:</strong> If \(B\) contains any other prime factor, the remainder must repeat one of the \(B - 1\) possible non-zero values, generating an infinitely periodic repeating decimal cycle.
            </li>
          </ul>

          <h2>4. Benchmark Long Division Reference Matrix</h2>
          <p>
            The table below illustrates sample division operations across varied dividend-to-divisor combinations, showing their quotient, remainder, mixed number, and decimal forms:
          </p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Dividend (\(A\))</th>
                <th>Divisor (\(B\))</th>
                <th>Quotient (\(Q\))</th>
                <th>Remainder (\(R\))</th>
                <th>Verification (\(B \cdot Q + R\))</th>
                <th>Mixed Number Form</th>
                <th>Decimal Value</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>100</td>
                <td>7</td>
                <td>14</td>
                <td>2</td>
                <td>\(7 \times 14 + 2 = 100\)</td>
                <td>\(14 \frac{2}{7}\)</td>
                <td>\(14.\overline{285714}\)</td>
              </tr>
              <tr>
                <td>487</td>
                <td>32</td>
                <td>15</td>
                <td>7</td>
                <td>\(32 \times 15 + 7 = 487\)</td>
                <td>\(15 \frac{7}{32}\)</td>
                <td>15.21875</td>
              </tr>
              <tr>
                <td>1250</td>
                <td>25</td>
                <td>50</td>
                <td>0</td>
                <td>\(25 \times 50 + 0 = 1250\)</td>
                <td>50 (Exact)</td>
                <td>50.0</td>
              </tr>
              <tr>
                <td>1789</td>
                <td>13</td>
                <td>137</td>
                <td>8</td>
                <td>\(13 \times 137 + 8 = 1789\)</td>
                <td>\(137 \frac{8}{13}\)</td>
                <td>\(137.\overline{615384}\)</td>
              </tr>
              <tr>
                <td>10,000</td>
                <td>64</td>
                <td>156</td>
                <td>16</td>
                <td>\(64 \times 156 + 16 = 10,000\)</td>
                <td>\(156 \frac{1}{4}\)</td>
                <td>156.25</td>
              </tr>
              <tr>
                <td>355</td>
                <td>113</td>
                <td>3</td>
                <td>16</td>
                <td>\(113 \times 3 + 16 = 355\)</td>
                <td>\(3 \frac{16}{113}\)</td>
                <td>3.1415929...</td>
              </tr>
            </tbody>
          </table>

          <h2>5. Engineering and Computer Science Applications</h2>

          <div class="worked-example-card">
            <h3>Case Study 1: Memory Buffer Paging and Offset Calculation in OS Kernels</h3>
            <p>
              In computer operating systems with virtual memory management, a physical RAM page size is configured at \(4,096\text{ bytes}\) (\(4\text{ KiB}\)). A program requests access to byte linear address \(A = 94,520\). Determine: (a) the virtual page index (\(Q\)), and (b) the intra-page byte offset (\(R\)).
            </p>
            <div class="example-body">
              <p><strong>Parameters:</strong> \(A = 94,520\), \(B = 4,096\).</p>
              <p><strong>Step 1: Compute the page number (integer quotient \(Q\)):</strong></p>
              $$Q = \lfloor 94,520 / 4,096 \rfloor = \lfloor 23.07617 \rfloor = 23$$
              <p><strong>Step 2: Compute the memory offset (remainder \(R\)):</strong></p>
              $$R = 94,520 - (4,096 \times 23) = 94,520 - 94,208 = 312\text{ bytes}$$
              <p><strong>Verification:</strong></p>
              $$4,096 \times 23 + 312 = 94,208 + 312 = 94,520$$
              <p><strong>Systems Conclusion:</strong> The memory management unit (MMU) directs the memory access to Page 23 at an exact byte offset of 312.</p>
            </div>
          </div>

          <div class="worked-example-card">
            <h3>Case Study 2: Industrial Manufacturing Batch Packaging Logistics</h3>
            <p>
              A pharmaceutical manufacturing plant produces \(14,850\) blister packs of amoxicillin in a single shift. Packaging cartons are designed to hold exactly \(48\) blister packs each. How many full shipping cartons can be sealed, and how many loose packs remain for sample testing?
            </p>
            <div class="example-body">
              <p><strong>Parameters:</strong> Dividend \(A = 14,850\), Divisor \(B = 48\).</p>
              <p><strong>Step 1: Perform long division:</strong></p>
              $$14,850 \div 48 = 309.375$$
              <p><strong>Step 2: Extract quotient and remainder:</strong></p>
              $$Q = 309 \text{ sealed cartons}$$
              $$R = 14,850 - (48 \times 309) = 14,850 - 14,832 = 18 \text{ loose packs}$$
              <p><strong>Step 3: Fractional remainder:</strong></p>
              $$\frac{18}{48} = \frac{3}{8} = 0.375 \text{ of a carton}$$
              <p><strong>Operational Result:</strong> The production team packs 309 complete cartons and sends 18 loose packs to the quality assurance laboratory.</p>
            </div>
          </div>

          <h2>6. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-accordion">
            <div class="faq-item">
              <h3 class="faq-question">What happens when the divisor is larger than the dividend (\(B > A\))?</h3>
              <div class="faq-answer">
                <p>
                  When \(B > A\) for positive integers, the divisor cannot fit into the dividend even once. Therefore, the integer quotient is 0 and the remainder is the entire dividend itself: \(Q = 0, R = A\). For example, \(5 \div 12\) yields \(Q = 0\) and \(R = 5\), because \(12 \times 0 + 5 = 5\).
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">How does long division relate to modulo arithmetic?</h3>
              <div class="faq-answer">
                <p>
                  The remainder of integer long division is identically the result of the modulo operation: \(R = A \pmod B\). For instance, \(487 \pmod{32} = 7\). You can test modular congruence and cyclic shifts using our <a href="gcd-lcm-calculator.html">GCD & LCM Calculator</a>.
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">Can you divide decimal numbers using long division?</h3>
              <div class="faq-answer">
                <p>
                  Yes. If the divisor \(B\) has decimals, multiply both the dividend and the divisor by \(10^k\) (where \(k\) is the number of decimal digits in the divisor) to make the divisor a whole integer. For example, to evaluate \(14.4 \div 1.2\), multiply both by 10 to obtain \(144 \div 12 = 12\). The quotient remains identical.
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">What is polynomial long division?</h3>
              <div class="faq-answer">
                <p>
                  Polynomial long division applies the identical DMSB algorithm to algebraic polynomials \(P(x) / D(x)\), dividing the highest-degree term of the dividend by the highest-degree term of the divisor at each step to obtain a quotient polynomial \(Q(x)\) and remainder polynomial \(R(x)\) where \(\deg(R) < \deg(D)\).
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
            <li><a href="fraction-calculator.html">Fraction Calculator</a></li>
            <li><a href="fraction-to-percent-calculator.html">Fraction to Percent Calculator</a></li>
            <li><a href="decimal-to-fraction-calculator.html">Decimal to Fraction Calculator</a></li>
            <li><a href="gcd-lcm-calculator.html">GCD & LCM Calculator</a></li>
            <li><a href="prime-number-calculator.html">Prime Number Calculator</a></li>
            <li><a href="scientific-notation-calculator.html">Scientific Notation Calculator</a></li>
            <li><a href="percentage-calculator.html">Percentage Calculator</a></li>
            <li><a href="ratio-calculator.html">Ratio Simplifier</a></li>
          </ul>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-col">
        <h4>CalcHub</h4>
        <p>Comprehensive mathematical, engineering, and scientific calculation tools.</p>
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
    function calculateLongDivision() {
      var a = parseFloat(document.getElementById("dividend").value);
      var b = parseFloat(document.getElementById("divisor").value);
      var prec = parseInt(document.getElementById("decimal_places").value) || 4;

      if (isNaN(a) || isNaN(b)) {
        alert("Please enter valid numerical values for the dividend and divisor.");
        return;
      }
      if (b === 0) {
        alert("Division by zero is undefined in standard mathematics.");
        return;
      }

      var isNeg = (a < 0) !== (b < 0);
      var absA = Math.abs(a);
      var absB = Math.abs(b);

      // Check if integers
      var isIntA = Number.isInteger(absA);
      var isIntB = Number.isInteger(absB);

      var qInt = Math.floor(absA / absB);
      var rInt = absA - (absB * qInt);

      if (isNeg) {
        qInt = -qInt;
      }

      var decVal = a / b;

      document.getElementById("primary-result").innerText = "Quotient: " + qInt + (rInt !== 0 ? " R " + rInt : "");
      document.getElementById("res-quotient").innerText = qInt.toLocaleString();
      document.getElementById("res-remainder").innerText = rInt.toLocaleString();
      document.getElementById("res-mixed").innerText = qInt + (rInt !== 0 ? " " + rInt + "/" + absB : "");
      document.getElementById("res-decimal").innerText = decVal.toFixed(prec);

      // Generate step by step explanation
      var steps = "<h4>Long Division Analytical Steps:</h4><ol>";
      steps += "<li><strong>Euclidean Theorem Formula:</strong> A = (B &times; Q) + R</li>";
      steps += "<li><strong>Integer Division:</strong> " + absA + " &divide; " + absB + " = " + Math.floor(absA / absB) + " (Quotient Q)</li>";
      steps += "<li><strong>Multiplication:</strong> " + absB + " &times; " + Math.floor(absA / absB) + " = " + (absB * Math.floor(absA / absB)) + "</li>";
      steps += "<li><strong>Subtraction for Remainder:</strong> " + absA + " - " + (absB * Math.floor(absA / absB)) + " = <strong>" + rInt + "</strong> (Remainder R)</li>";
      steps += "<li><strong>Verification Check:</strong> (" + absB + " &times; " + Math.floor(absA / absB) + ") + " + rInt + " = " + ((absB * Math.floor(absA / absB)) + rInt) + " &check;</li>";
      steps += "<li><strong>Decimal Value:</strong> " + a + " &divide; " + b + " = <strong>" + decVal.toFixed(prec + 2) + "</strong></li>";
      steps += "</ol>";

      document.getElementById("division-steps").innerHTML = steps;
      document.getElementById("result-box").style.display = "block";
    }

    window.addEventListener("DOMContentLoaded", function() {
      calculateLongDivision();
    });
  </script>
</body>
</html>
"""

def main():
    p3 = os.path.join(BASE_DIR, "logarithm-calculator.html")
    with open(p3, "w", encoding="utf-8") as f:
        f.write(HTML_LOGARITHM)
    print(f"Generated: {p3}")

    p4 = os.path.join(BASE_DIR, "long-division-calculator.html")
    with open(p4, "w", encoding="utf-8") as f:
        f.write(HTML_LONG_DIVISION)
    print(f"Generated: {p4}")

if __name__ == "__main__":
    main()
