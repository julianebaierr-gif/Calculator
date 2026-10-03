# -*- coding: utf-8 -*-
"""
Generator for Batch 29 - Part 1:
1. fraction-to-percent-calculator.html
2. geometric-sequence-calculator.html
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 1. fraction-to-percent-calculator.html
HTML_FRACTION_TO_PERCENT = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fraction to Percent Calculator - Instant Conversion & Step-by-Step</title>
  <meta name="description" content="Convert proper, improper, and mixed fractions into precise percentages and decimals. Includes step-by-step arithmetic, repeating decimal detection, and reduction formulas.">
  <link rel="canonical" href="https://calchub.org/fraction-to-percent-calculator.html">
  <meta property="og:title" content="Fraction to Percent Calculator - Exact Steps & Decimals">
  <meta property="og:description" content="Convert any fraction or mixed number into an exact percentage and decimal with step-by-step reduction, long division, and recurring period analysis.">
  <meta property="og:url" content="https://calchub.org/fraction-to-percent-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Fraction to Percent Calculator - Step-by-Step Conversion">
  <meta name="twitter:description" content="Free online fraction to percent calculator. Calculate decimal equivalents, recurring decimals, and simplified proportions with full math breakdown.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Fraction to Percent Calculator",
    "url": "https://calchub.org/fraction-to-percent-calculator.html",
    "description": "Calculates exact percentage equivalents for proper, improper, and mixed fractions with full step-by-step arithmetic, GCD reduction, and recurring decimal expansion.",
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
        "name": "How do you convert a fraction to a percentage?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "To convert a fraction a/b to a percentage, divide the numerator a by the denominator b to obtain the decimal value, then multiply by 100 and append the percent sign (%). Mathematically: P = (a / b) × 100%."
        }
      },
      {
        "@type": "Question",
        "name": "How do you convert a mixed number to a percentage?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "First, convert the mixed number W n/d into an improper fraction: Numerator = (W × d) + n, with the same denominator d. Then divide the improper numerator by d and multiply by 100%. Alternatively, add the whole number W multiplied by 100% to the fractional part percentage."
        }
      },
      {
        "@type": "Question",
        "name": "What causes repeating decimals in percentage conversions?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "In base 10, a fraction in lowest terms produces a terminating decimal if and only if the prime factorization of its denominator contains only prime factors 2 and 5. If the denominator contains any other prime factor (such as 3, 7, 11, or 13), the decimal expansion repeats indefinitely."
        }
      },
      {
        "@type": "Question",
        "name": "Can a percentage from a fraction exceed 100%?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. An improper fraction where the numerator is greater than the denominator (a > b) represents a value strictly greater than 1, yielding a percentage greater than 100% (e.g., 5/4 = 1.25 = 125%)."
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
      <span>Fraction to Percent Calculator</span>
    </nav>

    <div class="content-layout">
      <div class="main-column">
        <div class="calculator-card">
          <div class="calculator-header">
            <span class="calc-icon">➗</span>
            <h1>Fraction to Percent Calculator</h1>
          </div>
          <p class="calc-description">
            Convert proper fractions, improper fractions, and mixed numbers into precise percentages, decimals, and reduced forms with full long-division steps.
          </p>

          <form id="calc-form" class="calc-form" onsubmit="return false;">
            <div class="input-grid">
              <div class="form-group">
                <label for="whole_part">Whole Number (Optional for Mixed):</label>
                <input type="number" id="whole_part" class="form-control" value="0" step="1" placeholder="e.g. 0">
                <span class="help-text">Leave 0 for regular fractions.</span>
              </div>
              <div class="form-group">
                <label for="numerator">Numerator (\(a\)):</label>
                <input type="number" id="numerator" class="form-control" value="3" step="any" placeholder="e.g. 3" required>
                <span class="help-text">Top number of the fraction.</span>
              </div>
              <div class="form-group">
                <label for="denominator">Denominator (\(b\)):</label>
                <input type="number" id="denominator" class="form-control" value="8" step="any" placeholder="e.g. 8" required>
                <span class="help-text">Bottom number (cannot be zero).</span>
              </div>
              <div class="form-group">
                <label for="precision">Display Decimal Places:</label>
                <select id="precision" class="form-control">
                  <option value="2">2 decimal places (Standard)</option>
                  <option value="4" selected>4 decimal places</option>
                  <option value="6">6 decimal places (High)</option>
                  <option value="8">8 decimal places (Scientific)</option>
                </select>
                <span class="help-text">Rounding precision for percentages.</span>
              </div>
            </div>

            <button type="button" id="btn-calculate" class="btn btn-primary" onclick="calculateFractionToPercent()">Convert to Percent</button>
          </form>

          <div id="result-box" class="result-box" style="display:none;">
            <h3>Conversion Results</h3>
            <div class="result-highlight" id="primary-result">37.5%</div>
            
            <div class="result-grid">
              <div class="result-item">
                <span class="res-label">Exact Decimal Value:</span>
                <span class="res-val" id="res-decimal">0.375</span>
              </div>
              <div class="result-item">
                <span class="res-label">Reduced Fraction:</span>
                <span class="res-val" id="res-reduced">3 / 8</span>
              </div>
              <div class="result-item">
                <span class="res-label">Fraction Type:</span>
                <span class="res-val" id="res-type">Proper Fraction</span>
              </div>
              <div class="result-item">
                <span class="res-label">Expansion Character:</span>
                <span class="res-val" id="res-repeating">Terminating Decimal</span>
              </div>
            </div>

            <div class="conversion-steps" id="conversion-steps">
              <!-- Steps populated dynamically -->
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. Fundamental Principles of Fraction-to-Percentage Conversion</h2>
          <p>
            In elementary arithmetic and applied algebra, fractions and percentages represent two alternative mathematical formalisms for expressing rational proportions and parts of a whole. A <strong>fraction</strong> \( \frac{a}{b} \) defines the quotient of two integers where \(a\) is the numerator (representing the partition count) and \(b\) is the denominator (representing the total partition scale, with \(b \neq 0\)). Conversely, a <strong>percentage</strong> is a dimensionless ratio whose scale is intrinsically anchored to a base of one hundred, denoted by the per-centum symbol (\(\%\)).
          </p>
          <p>
            The mathematical translation between a rational fraction and a per-centum value proceeds through the canonical division identity:
          </p>
          $$P = \left( \frac{a}{b} \right) \times 100\% = \frac{100a}{b}\%$$
          <p>
            When handling mixed numbers possessing an integer whole part \(W\) alongside a fractional remainder \( \frac{n}{d} \), the mixed quantity must first be converted into an improper fraction prior to computing the decimal quotient:
          </p>
          $$W \frac{n}{d} = \frac{(W \times d) + n}{d} \implies P = \left( \frac{W \cdot d + n}{d} \right) \times 100\%$$
          <p>
            Alternatively, by exploiting the distributive law of multiplication over addition, one may evaluate the whole number and fractional components separately:
          </p>
          $$P = (W \times 100\%) + \left( \frac{n}{d} \times 100\% \right)$$

          <h2>2. Algorithmic Steps and the Euclidean Reduction</h2>
          <p>
            To achieve maximal analytical clarity and avoid floating-point rounding errors during computation, professional mathematical workflows employ an algorithmic three-phase sequence:
          </p>
          <ol>
            <li>
              <strong>Greatest Common Divisor (GCD) Factorization:</strong> Calculate \(g = \gcd(|a|, |b|)\) utilizing the classical Euclidean algorithm:
              $$\gcd(a, b) = \gcd(b, a \pmod b)$$
              Divide both numerator and denominator by \(g\) to establish the canonical irreducible fraction \( \frac{a'}{b'} = \frac{a/g}{b/g} \).
            </li>
            <li>
              <strong>Long Division Decimal Expansion:</strong> Evaluate the quotient \(q = a' / b'\) through iterative long division. If \(b'\) contains prime factors other than 2 or 5, determine the repetend period length.
            </li>
            <li>
              <strong>Scaling and Per-Centum Normalization:</strong> Multiply the quotient by \(10^{2}\) (shifting the decimal radix point two places to the right) and append the percent operator.
            </li>
          </ol>

          <h2>3. Decimal Terminations vs. Repeating Periods (Euler-Fermat Totient Theorem)</h2>
          <p>
            A common source of confusion in empirical mathematics is why certain fractions yield finite, neat percentages (e.g., \(1/8 = 12.5\%\)), while others yield infinite recurring sequences (e.g., \(1/7 = 14.285714...\%\)). The underlying phenomenon is strictly governed by the prime factorization of the denominator in base-10 arithmetic.
          </p>
          <p>
            In the decimal number system, the base is \(10 = 2 \times 5\). According to number theory, a fully reduced rational fraction \( \frac{a}{b} \) terminates in a finite number of decimal digits if and only if the prime factorization of the denominator \(b\) satisfies:
          </p>
          $$b = 2^m \cdot 5^n \quad \text{for non-negative integers } m, n \ge 0$$
          <p>
            The maximum number of digits after the decimal point before termination occurs is precisely \(\max(m, n)\). When scaled to a percentage (which multiplies by \(10^2\)), the number of decimal digits in the percentage is \(\max(m-2, n-2, 0)\).
          </p>
          <p>
            If \(b\) contains any prime factor \(p \notin \{2, 5\}\), the decimal representation becomes an infinite periodic repeating decimal. The maximum length of the repeating period \(L\) cannot exceed \(b - 1\). By Euler's totient theorem, if \(\gcd(10, b) = 1\), the period length \(L\) is the multiplicative order of 10 modulo \(b\):
          </p>
          $$10^L \equiv 1 \pmod b$$

          <h2>4. Comprehensive Rational Fraction to Percent Reference Table</h2>
          <p>
            The following benchmark reference matrix compiles canonical fractions encountered across engineering, finance, statistics, and carpentry, detailing their exact decimal fractions, percentage values, and expansion classes:
          </p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Fraction (\(a/b\))</th>
                <th>Decimal Equivalent</th>
                <th>Exact / Standard Percentage</th>
                <th>Denominator Primes</th>
                <th>Expansion Class</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>\(1/2\)</td>
                <td>0.5</td>
                <td>50.0%</td>
                <td>\(2^1\)</td>
                <td>Terminating</td>
              </tr>
              <tr>
                <td>\(1/3\)</td>
                <td>0.333333...</td>
                <td>\(33.\overline{3}\%\) (33.3333%)</td>
                <td>\(3^1\)</td>
                <td>Pure Repeating (Period = 1)</td>
              </tr>
              <tr>
                <td>\(1/4\)</td>
                <td>0.25</td>
                <td>25.0%</td>
                <td>\(2^2\)</td>
                <td>Terminating</td>
              </tr>
              <tr>
                <td>\(1/5\)</td>
                <td>0.2</td>
                <td>20.0%</td>
                <td>\(5^1\)</td>
                <td>Terminating</td>
              </tr>
              <tr>
                <td>\(1/6\)</td>
                <td>0.166666...</td>
                <td>\(16.6\overline{6}\%\) (16.6667%)</td>
                <td>\(2 \times 3\)</td>
                <td>Delayed Repeating (Period = 1)</td>
              </tr>
              <tr>
                <td>\(1/7\)</td>
                <td>0.142857...</td>
                <td>\(14.\overline{285714}\%\) (14.2857%)</td>
                <td>\(7^1\)</td>
                <td>Pure Repeating (Period = 6)</td>
              </tr>
              <tr>
                <td>\(1/8\)</td>
                <td>0.125</td>
                <td>12.5%</td>
                <td>\(2^3\)</td>
                <td>Terminating</td>
              </tr>
              <tr>
                <td>\(1/9\)</td>
                <td>0.111111...</td>
                <td>\(11.\overline{1}\%\) (11.1111%)</td>
                <td>\(3^2\)</td>
                <td>Pure Repeating (Period = 1)</td>
              </tr>
              <tr>
                <td>\(1/10\)</td>
                <td>0.1</td>
                <td>10.0%</td>
                <td>\(2 \times 5\)</td>
                <td>Terminating</td>
              </tr>
              <tr>
                <td>\(1/12\)</td>
                <td>0.083333...</td>
                <td>\(8.3\overline{3}\%\) (8.3333%)</td>
                <td>\(2^2 \times 3\)</td>
                <td>Delayed Repeating (Period = 1)</td>
              </tr>
              <tr>
                <td>\(1/16\)</td>
                <td>0.0625</td>
                <td>6.25%</td>
                <td>\(2^4\)</td>
                <td>Terminating</td>
              </tr>
              <tr>
                <td>\(3/8\)</td>
                <td>0.375</td>
                <td>37.5%</td>
                <td>\(2^3\)</td>
                <td>Terminating</td>
              </tr>
              <tr>
                <td>\(5/8\)</td>
                <td>0.625</td>
                <td>62.5%</td>
                <td>\(2^3\)</td>
                <td>Terminating</td>
              </tr>
              <tr>
                <td>\(7/8\)</td>
                <td>0.875</td>
                <td>87.5%</td>
                <td>\(2^3\)</td>
                <td>Terminating</td>
              </tr>
              <tr>
                <td>\(5/6\)</td>
                <td>0.833333...</td>
                <td>\(83.\overline{3}\%\) (83.3333%)</td>
                <td>\(2 \times 3\)</td>
                <td>Delayed Repeating (Period = 1)</td>
              </tr>
              <tr>
                <td>\(7/12\)</td>
                <td>0.583333...</td>
                <td>\(58.3\overline{3}\%\) (58.3333%)</td>
                <td>\(2^2 \times 3\)</td>
                <td>Delayed Repeating (Period = 1)</td>
              </tr>
            </tbody>
          </table>

          <h2>5. Practical Worked Engineering & Analytical Case Studies</h2>
          
          <div class="worked-example-card">
            <h3>Case Study 1: Structural Fastener Tensile Yield Ratio</h3>
            <p>
              An aerospace structural engineer evaluates a titanium bolt under shear and tension. The applied static load is measured at \(19\text{ kN}\), against an ultimate design yield capacity of \(24\text{ kN}\). The load ratio is \( \frac{19}{24} \). Calculate the capacity utilization percentage with step-by-step arithmetic.
            </p>
            <div class="example-body">
              <p><strong>Step 1: Inspect and reduce the fraction:</strong></p>
              $$\gcd(19, 24) = 1 \implies \text{The fraction } \frac{19}{24} \text{ is already irreducible.}$$
              <p><strong>Step 2: Factorize the denominator to analyze decimal expansion:</strong></p>
              $$24 = 2^3 \times 3^1$$
              <p>Because of the prime factor 3, the decimal will not terminate; it will exhibit a delayed repeating period.</p>
              <p><strong>Step 3: Execute division:</strong></p>
              $$\frac{19}{24} = 0.791666666...$$
              <p><strong>Step 4: Scale to percent:</strong></p>
              $$P = 0.791666666... \times 100\% = 79.16\overline{6}\% \approx 79.1667\%$$
              <p><strong>Conclusion:</strong> The bolt operates at \(79.17\%\) of its allowable design capacity, maintaining a safety margin of \(20.83\%\).</p>
            </div>
          </div>

          <div class="worked-example-card">
            <h3>Case Study 2: Mixed-Number Financial Portfolio Allocation</h3>
            <p>
              An institutional portfolio manager holds an asset allocation specified as \(2 \frac{5}{16}\) times the benchmark index baseline. Convert this mixed allocation weighting into an exact percentage.
            </p>
            <div class="example-body">
              <p><strong>Step 1: Convert the mixed number into an improper fraction:</strong></p>
              $$W = 2, \quad n = 5, \quad d = 16$$
              $$\text{Improper Numerator} = (2 \times 16) + 5 = 32 + 5 = 37$$
              $$\text{Fraction} = \frac{37}{16}$$
              <p><strong>Step 2: Factorize the denominator:</strong></p>
              $$16 = 2^4$$
              <p>Since the only prime factor is 2, the expansion terminates exactly in at most 4 decimal places.</p>
              <p><strong>Step 3: Long division:</strong></p>
              $$\frac{37}{16} = 2.3125$$
              <p><strong>Step 4: Multiply by 100:</strong></p>
              $$P = 2.3125 \times 100\% = 231.25\%$$
              <p><strong>Conclusion:</strong> The asset weighting corresponds to exactly \(231.25\%\) of the benchmark baseline.</p>
            </div>
          </div>

          <h2>6. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-accordion">
            <div class="faq-item">
              <h3 class="faq-question">How does this calculator handle negative fractions?</h3>
              <div class="faq-answer">
                <p>
                  Negative fractions are supported seamlessly. If either the numerator or denominator is negative, the resulting decimal and percentage will be negative (e.g., \(-3/4 = -0.75 = -75\%\)). If both the numerator and denominator are negative, their signs cancel out in accordance with the algebraic rule \((-a)/(-b) = a/b\), yielding a positive percentage.
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">What is the difference between a percentage and a percentage point?</h3>
              <div class="faq-answer">
                <p>
                  A percentage represents a relative ratio proportional to a base value. A percentage point refers to the arithmetic difference between two percentage values. For instance, an increase from \(20\%\) to \(25\%\) is an absolute increase of \(5\) percentage points, but a relative increase of \( \frac{25-20}{20} \times 100\% = 25\% \).
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">Why does dividing by zero cause an error?</h3>
              <div class="faq-answer">
                <p>
                  Division by zero (\(b = 0\)) is mathematically undefined in standard arithmetic. The equation \( \frac{a}{0} = x \) implies \(x \times 0 = a\). If \(a \neq 0\), no real number satisfies this condition; if \(a = 0\), every number satisfies it, rendering the quotient indeterminate. The calculator enforces strict validation to block zero denominators.
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">How do you convert a percentage back into a fraction?</h3>
              <div class="faq-answer">
                <p>
                  To reverse the operation, place the percentage value over a denominator of 100 (\(P / 100\)). If \(P\) contains decimals, multiply both numerator and denominator by \(10^k\) to clear decimals, then divide both terms by their greatest common divisor (GCD). For example, \(37.5\% = \frac{37.5}{100} = \frac{375}{1000} = \frac{3}{8}\). You can use our <a href="decimal-to-fraction-calculator.html">Decimal to Fraction Calculator</a> or <a href="fraction-calculator.html">Fraction Calculator</a> for instant automated reversal.
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
            <li><a href="decimal-to-fraction-calculator.html">Decimal to Fraction Calculator</a></li>
            <li><a href="percentage-calculator.html">Percentage Calculator</a></li>
            <li><a href="ratio-calculator.html">Ratio Simplifier</a></li>
            <li><a href="scientific-notation-calculator.html">Scientific Notation Calculator</a></li>
            <li><a href="significant-figures-calculator.html">Significant Figures Calculator</a></li>
            <li><a href="gcd-lcm-calculator.html">GCD & LCM Calculator</a></li>
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
        <p>Comprehensive engineering, scientific, financial, and mathematical calculation tools.</p>
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
      <p>&copy; 2026 CalcHub. All rights reserved. Precise peer-reviewed calculation engines.</p>
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

    function calculateFractionToPercent() {
      var whole = parseFloat(document.getElementById("whole_part").value) || 0;
      var num = parseFloat(document.getElementById("numerator").value);
      var den = parseFloat(document.getElementById("denominator").value);
      var prec = parseInt(document.getElementById("precision").value) || 4;

      if (isNaN(num) || isNaN(den)) {
        alert("Please enter valid numerical values for the numerator and denominator.");
        return;
      }

      if (den === 0) {
        alert("The denominator cannot be zero. Division by zero is undefined.");
        return;
      }

      // Consolidate mixed fraction
      var isNegative = false;
      if (whole < 0) {
        isNegative = true;
        whole = Math.abs(whole);
      }
      if (num < 0 && den < 0) {
        num = Math.abs(num);
        den = Math.abs(den);
      } else if (num < 0 || den < 0) {
        isNegative = !isNegative;
        num = Math.abs(num);
        den = Math.abs(den);
      }

      var improperNum = (whole * den) + num;
      if (isNegative) {
        improperNum = -improperNum;
      }

      var decimalValue = improperNum / den;
      var percentValue = decimalValue * 100;

      var g = gcd(improperNum, den);
      var redNum = improperNum / g;
      var redDen = den / g;

      // Classify fraction
      var fracType = "Proper Fraction";
      if (Math.abs(improperNum) >= Math.abs(den)) {
        fracType = "Improper Fraction";
      }
      if (whole !== 0) {
        fracType = "Mixed Number (" + whole + " " + num + "/" + den + ")";
      }

      // Check terminating vs repeating
      var testDen = Math.abs(redDen);
      while (testDen % 2 === 0) testDen /= 2;
      while (testDen % 5 === 0) testDen /= 5;
      var isTerminating = (testDen === 1);
      var expansionClass = isTerminating ? "Terminating Decimal" : "Repeating Decimal (Periodic)";

      document.getElementById("primary-result").innerText = percentValue.toFixed(prec) + "%";
      document.getElementById("res-decimal").innerText = decimalValue.toFixed(prec + 2);
      document.getElementById("res-reduced").innerText = redNum + " / " + redDen;
      document.getElementById("res-type").innerText = fracType;
      document.getElementById("res-repeating").innerText = expansionClass;

      // Construct detailed step HTML
      var stepsHtml = "<h4>Step-by-Step Calculation Breakdown:</h4><ol>";
      if (whole !== 0) {
        stepsHtml += "<li><strong>Convert Mixed to Improper:</strong> (" + whole + " × " + den + " + " + num + ") / " + den + " = " + improperNum + "/" + den + "</li>";
      }
      stepsHtml += "<li><strong>Simplify Fraction:</strong> GCD(" + Math.abs(improperNum) + ", " + den + ") = " + g + " &rarr; Reduced to " + redNum + "/" + redDen + "</li>";
      stepsHtml += "<li><strong>Calculate Decimal Quotient:</strong> " + redNum + " &divide; " + redDen + " = " + decimalValue.toFixed(prec + 4) + "</li>";
      stepsHtml += "<li><strong>Scale by 100%:</strong> " + decimalValue.toFixed(prec + 4) + " × 100% = <strong>" + percentValue.toFixed(prec) + "%</strong></li>";
      stepsHtml += "</ol>";

      document.getElementById("conversion-steps").innerHTML = stepsHtml;
      document.getElementById("result-box").style.display = "block";
    }

    // Run on initial load
    window.addEventListener("DOMContentLoaded", function() {
      calculateFractionToPercent();
    });
  </script>
</body>
</html>
"""

# 2. geometric-sequence-calculator.html
HTML_GEOMETRIC_SEQUENCE = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Geometric Sequence Calculator - Nth Term, Partial & Infinite Sum</title>
  <meta name="description" content="Calculate the nth term, common ratio (r), partial sum (Sn), and infinite series sum (S∞) of a geometric progression with detailed step-by-step formulas.">
  <link rel="canonical" href="https://calchub.org/geometric-sequence-calculator.html">
  <meta property="og:title" content="Geometric Sequence & Series Calculator - Nth Term & Sum">
  <meta property="og:description" content="Compute terms, finite series sums, and infinite geometric series limits with complete mathematical derivation and convergence analysis.">
  <meta property="og:url" content="https://calchub.org/geometric-sequence-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Geometric Sequence Calculator - Formulas & Step-by-Step">
  <meta name="twitter:description" content="Free geometric progression solver. Computes a_n, common ratio, finite sum S_n, and infinite series convergence S_infinity with worked engineering examples.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Geometric Sequence Calculator",
    "url": "https://calchub.org/geometric-sequence-calculator.html",
    "description": "Calculates the nth term, common ratio r, finite series sum Sn, and infinite geometric series convergence limit S_infinity with detailed mathematical derivations.",
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
        "name": "What is the formula for the nth term of a geometric sequence?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The nth term a_n of a geometric sequence with initial term a_1 and common ratio r is given by: a_n = a_1 · r^(n - 1)."
        }
      },
      {
        "@type": "Question",
        "name": "How do you calculate the sum of a finite geometric sequence?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The partial sum of the first n terms S_n when r ≠ 1 is calculated using: S_n = a_1 · (1 - r^n) / (1 - r). If r = 1, then S_n = n · a_1."
        }
      },
      {
        "@type": "Question",
        "name": "When does an infinite geometric series converge?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "An infinite geometric series converges to a finite sum if and only if the absolute value of the common ratio is strictly less than 1 (|r| < 1). The sum is then: S_∞ = a_1 / (1 - r). If |r| ≥ 1, the series diverges."
        }
      },
      {
        "@type": "Question",
        "name": "What is the difference between an arithmetic and a geometric sequence?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "In an arithmetic sequence, successive terms differ by a constant addition of a common difference d (a_n = a_1 + (n-1)d). In a geometric sequence, successive terms differ by constant multiplication by a common ratio r (a_n = a_1 · r^(n-1))."
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
      <span>Geometric Sequence Calculator</span>
    </nav>

    <div class="content-layout">
      <div class="main-column">
        <div class="calculator-card">
          <div class="calculator-header">
            <span class="calc-icon">📈</span>
            <h1>Geometric Sequence Calculator</h1>
          </div>
          <p class="calc-description">
            Determine the \(n\)th term \(a_n\), common ratio \(r\), partial sum \(S_n\), and infinite series limit \(S_\infty\) of any geometric progression with analytical convergence verification.
          </p>

          <form id="calc-form" class="calc-form" onsubmit="return false;">
            <div class="input-grid">
              <div class="form-group">
                <label for="first_term">First Term (\(a_1\)):</label>
                <input type="number" id="first_term" class="form-control" value="2" step="any" placeholder="e.g. 2" required>
                <span class="help-text">Initial value of the sequence.</span>
              </div>
              <div class="form-group">
                <label for="common_ratio">Common Ratio (\(r\)):</label>
                <input type="number" id="common_ratio" class="form-control" value="3" step="any" placeholder="e.g. 3 or 0.5" required>
                <span class="help-text">Multiplier between successive terms.</span>
              </div>
              <div class="form-group">
                <label for="term_index">Target Term Number (\(n\)):</label>
                <input type="number" id="term_index" class="form-control" value="6" step="1" min="1" placeholder="e.g. 6" required>
                <span class="help-text">Positive integer position index.</span>
              </div>
              <div class="form-group">
                <label for="num_preview">Preview First Terms Count:</label>
                <select id="num_preview" class="form-control">
                  <option value="5">First 5 terms</option>
                  <option value="8" selected>First 8 terms</option>
                  <option value="12">First 12 terms</option>
                </select>
                <span class="help-text">Sequence table expansion length.</span>
              </div>
            </div>

            <button type="button" id="btn-calculate" class="btn btn-primary" onclick="calculateGeometricSequence()">Compute Progression</button>
          </form>

          <div id="result-box" class="result-box" style="display:none;">
            <h3>Geometric Progression Results</h3>
            <div class="result-highlight" id="primary-result">a₆ = 486</div>
            
            <div class="result-grid">
              <div class="result-item">
                <span class="res-label">Partial Sum (\(S_n\)):</span>
                <span class="res-val" id="res-partial-sum">728</span>
              </div>
              <div class="result-item">
                <span class="res-label">Infinite Series (\(S_\infty\)):</span>
                <span class="res-val" id="res-infinite-sum">Diverges (|r| ≥ 1)</span>
              </div>
              <div class="result-item">
                <span class="res-label">Sequence Behavior:</span>
                <span class="res-val" id="res-behavior">Monotonically Diverging</span>
              </div>
              <div class="result-item">
                <span class="res-label">Preceding Term (\(a_{n-1}\)):</span>
                <span class="res-val" id="res-prev-term">162</span>
              </div>
            </div>

            <div class="conversion-steps" id="steps-output">
              <!-- Analytical steps rendered dynamically -->
            </div>

            <div style="margin-top:1.5rem;">
              <h4>Sequence Expansion Preview:</h4>
              <div style="overflow-x:auto;">
                <table class="data-table" id="table-terms">
                  <thead>
                    <tr>
                      <th>Index (\(k\))</th>
                      <th>Term Formula</th>
                      <th>Numerical Value (\(a_k\))</th>
                      <th>Running Sum (\(S_k\))</th>
                    </tr>
                  </thead>
                  <tbody id="tbody-terms">
                    <!-- Populated dynamically -->
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. Mathematical Architecture of Geometric Progressions</h2>
          <p>
            A <strong>geometric sequence</strong> (or geometric progression, GP) is an ordered succession of numbers where each term after the initial one is obtained by multiplying the immediately preceding term by a fixed, non-zero constant termed the <strong>common ratio</strong> (\(r\)). If we denote the sequence as \((a_k)_{k=1}^{\infty}\), the formal recurrence relation is defined by:
          </p>
          $$a_{k+1} = a_k \cdot r \quad \text{for } k \in \mathbb{N}$$
          <p>
            By unwinding this recurrence iteratively starting from the initial boundary condition \(a_1\):
          </p>
          $$a_2 = a_1 r, \quad a_3 = a_2 r = a_1 r^2, \quad a_4 = a_3 r = a_1 r^3, \dots$$
          <p>
            We establish the closed-form <strong>general \(n\)th term formula</strong>:
          </p>
          $$a_n = a_1 \cdot r^{n-1}$$
          <p>
            Geometric sequences serve as the fundamental mathematical backbone modeling compounding processes across the physical and social sciences: exponential population kinetics, compound interest accumulation in financial economics, nuclear chain fission reactions, photon attenuation through absorbing media (Beer-Lambert Law), and algorithmic divide-and-conquer runtime complexities.
          </p>

          <h2>2. Derivation of the Finite Geometric Series Sum (\(S_n\))</h2>
          <p>
            A <strong>geometric series</strong> is the accumulated summation of the terms of a geometric progression. Let \(S_n\) represent the \(n\)th partial sum:
          </p>
          $$S_n = \sum_{k=1}^n a_k = a_1 + a_1 r + a_1 r^2 + a_1 r^3 + \dots + a_1 r^{n-1}$$
          <p>
            To derive its closed-form expression without summing \(n\) individual terms, multiply the entire equation by the common ratio \(r\):
          </p>
          $$r S_n = a_1 r + a_1 r^2 + a_1 r^3 + \dots + a_1 r^{n-1} + a_1 r^n$$
          <p>
            Now subtract the second equation from the first. Notice that all intermediate terms from \(a_1 r\) through \(a_1 r^{n-1}\) cancel out telescopically:
          </p>
          $$S_n - r S_n = a_1 - a_1 r^n$$
          $$S_n (1 - r) = a_1 (1 - r^n)$$
          <p>
            Assuming \(r \neq 1\), dividing through by \((1 - r)\) produces the classical finite sum formula:
          </p>
          $$S_n = a_1 \left( \frac{1 - r^n}{1 - r} \right) = a_1 \left( \frac{r^n - 1}{r - 1} \right)$$
          <p>
            In the trivial degenerate case where \(r = 1\), every term equals \(a_1\), yielding:
          </p>
          $$S_n = \sum_{k=1}^n a_1 = n \cdot a_1$$

          <h2>3. Convergence and the Infinite Geometric Series Limit (\(S_\infty\))</h2>
          <p>
            In mathematical analysis, when considering an infinite number of terms (\(n \to \infty\)), the infinite geometric series is defined as the limit of the sequence of partial sums:
          </p>
          $$S_\infty = \lim_{n \to \infty} S_n = \lim_{n \to \infty} a_1 \left( \frac{1 - r^n}{1 - r} \right) = \frac{a_1}{1 - r} \left( 1 - \lim_{n \to \infty} r^n \right)$$
          <p>
            The convergence behavior is strictly determined by the asymptotic limit of \(r^n\):
          </p>
          <ul>
            <li>
              <strong>Case 1: \(|r| < 1\) (Convergence).</strong> As \(n \to \infty\), \(r^n \to 0\). The infinite series converges absolutely to the finite limit:
              $$S_\infty = \frac{a_1}{1 - r}$$
            </li>
            <li>
              <strong>Case 2: \(r > 1\) (Monotonic Divergence).</strong> As \(n \to \infty\), \(r^n \to +\infty\). The series diverges to \(+\infty\) (or \(-\infty\) if \(a_1 < 0\)).
            </li>
            <li>
              <strong>Case 3: \(r \le -1\) (Oscillatory Divergence).</strong> The sequence \(r^n\) oscillates wildly between large positive and negative values without converging (e.g., Grandi's series when \(a_1=1, r=-1\)).
            </li>
            <li>
              <strong>Case 4: \(r = 1\) (Linear Divergence).</strong> \(S_n = n a_1 \to \pm\infty\).
            </li>
          </ul>

          <h2>4. Characteristic Regimes of Geometric Sequences</h2>
          <p>
            The qualitative analytical dynamics of a geometric progression depend entirely on the algebraic sign and absolute magnitude of the common ratio \(r\), as summarized in the taxonomy table below:
          </p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Common Ratio Domain</th>
                <th>Sequence Trajectory</th>
                <th>Sign Behavior</th>
                <th>Infinite Series Convergence (\(S_\infty\))</th>
                <th>Physical / Engineering Analogy</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>\(r > 1\)</td>
                <td>Strictly Increasing Magnitude</td>
                <td>Constant sign (same as \(a_1\))</td>
                <td>Diverges to \(\pm \infty\)</td>
                <td>Unconstrained population growth, nuclear chain reaction</td>
              </tr>
              <tr>
                <td>\(r = 1\)</td>
                <td>Constant Sequence (\(a_k = a_1\))</td>
                <td>Constant</td>
                <td>Diverges to \(\pm \infty\)</td>
                <td>Steady DC electrical current without loss</td>
              </tr>
              <tr>
                <td>\(0 < r < 1\)</td>
                <td>Monotonically Decaying to 0</td>
                <td>Constant sign</td>
                <td><strong>Converges</strong> to \( \frac{a_1}{1-r} \)</td>
                <td>Radioactive decay, capacitor discharge, drug metabolism</td>
              </tr>
              <tr>
                <td>\(r = 0\)</td>
                <td>Collapses to 0 for \(k \ge 2\)</td>
                <td>Zero</td>
                <td>Converges to \(a_1\)</td>
                <td>Immediate complete attenuation</td>
              </tr>
              <tr>
                <td>\(-1 < r < 0\)</td>
                <td>Damped Alternating Oscillation</td>
                <td>Alternating (+, -, +, -)</td>
                <td><strong>Converges</strong> to \( \frac{a_1}{1-r} \)</td>
                <td>Bouncing ball damped rebound, feedback hunting</td>
              </tr>
              <tr>
                <td>\(r = -1\)</td>
                <td>Constant Amplitude Oscillation</td>
                <td>Alternating (\(a_1, -a_1, \dots\))</td>
                <td>Diverges (Grandi-type oscillation)</td>
                <td>Ideal lossless clock pendulum, toggle flip-flop</td>
              </tr>
              <tr>
                <td>\(r < -1\)</td>
                <td>Exploding Alternating Oscillation</td>
                <td>Alternating</td>
                <td>Diverges wildly</td>
                <td>Unstable control system runaway oscillation</td>
              </tr>
            </tbody>
          </table>

          <h2>5. Practical Engineering and Financial Worked Examples</h2>

          <div class="worked-example-card">
            <h3>Case Study 1: Mechanical Shock Absorber Damping Energy Dissipation</h3>
            <p>
              An industrial vibratory compactor incorporates an elastomeric shock damper. On the initial impact stroke, the damper absorbs \(E_1 = 800\text{ Joules}\) of kinetic energy. Due to viscoelastic thermal dissipation, each subsequent rebound cycle dissipates exactly \(65\%\) of the energy of the preceding stroke (\(r = 0.65\)).
            </p>
            <p>
              Calculate: (a) The energy dissipated on the 5th stroke (\(E_5\)), (b) The cumulative energy absorbed over the first 5 strokes (\(S_5\)), and (c) The theoretical total infinite energy capacity until complete rest (\(S_\infty\)).
            </p>
            <div class="example-body">
              <p><strong>Parameters:</strong> \(a_1 = 800\text{ J}\), \(r = 0.65\), \(n = 5\).</p>
              <p><strong>Part (a): Compute the 5th stroke energy (\(a_5\)):</strong></p>
              $$a_5 = a_1 \cdot r^{5-1} = 800 \times (0.65)^4 = 800 \times 0.17850625 = 142.805\text{ J}$$
              <p><strong>Part (b): Compute the partial sum of the first 5 strokes (\(S_5\)):</strong></p>
              $$S_5 = 800 \left( \frac{1 - 0.65^5}{1 - 0.65} \right) = 800 \left( \frac{1 - 0.116029}{0.35} \right) = 800 \left( \frac{0.883971}{0.35} \right) \approx 2020.505\text{ J}$$
              <p><strong>Part (c): Compute the total infinite dissipation (\(S_\infty\)):</strong></p>
              <p>Since \(|r| = 0.65 < 1\), the infinite series converges:</p>
              $$S_\infty = \frac{a_1}{1 - r} = \frac{800}{1 - 0.65} = \frac{800}{0.35} \approx 2285.714\text{ J}$$
              <p><strong>Engineering Finding:</strong> The damper dissipates over \(88.4\%\) of its ultimate lifetime energy capacity in the first 5 cycles.</p>
            </div>
          </div>

          <div class="worked-example-card">
            <h3>Case Study 2: Financial Annuity Sinking Fund Compounding</h3>
            <p>
              An infrastructure capital renewal sinking fund deposits an initial \(\$50,000\) into an asset pool growing at an annual compounding growth multiplier of \(r = 1.08\) (\(8\%\) annual geometric growth). Determine the asset balance at year \(n = 10\) and the cumulative total geometric expansion.
            </p>
            <div class="example-body">
              <p><strong>Parameters:</strong> \(a_1 = 50,000\), \(r = 1.08\), \(n = 10\).</p>
              <p><strong>Step 1: Compute the 10th year term:</strong></p>
              $$a_{10} = 50000 \times (1.08)^{9} = 50000 \times 1.9990046 \approx \$99,950.23$$
              <p><strong>Step 2: Compute the 10-year cumulative sum (\(S_{10}\)):</strong></p>
              $$S_{10} = 50000 \left( \frac{1.08^{10} - 1}{1.08 - 1} \right) = 50000 \left( \frac{2.158925 - 1}{0.08} \right) = 50000 \times 14.48656 = \$724,328.12$$
              <p><strong>Analytical Result:</strong> At year 10, the annual cash flow nearly doubles, with the cumulative capital sum exceeding \(\$724,300\).</p>
            </div>
          </div>

          <h2>6. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-accordion">
            <div class="faq-item">
              <h3 class="faq-question">How do you find the common ratio \(r\) if only two arbitrary terms are given?</h3>
              <div class="faq-answer">
                <p>
                  If you are given term \(a_j\) at index \(j\) and term \(a_k\) at index \(k\) (with \(k > j\)), their quotient satisfies:
                  $$\frac{a_k}{a_j} = \frac{a_1 r^{k-1}}{a_1 r^{j-1}} = r^{k - j} \implies r = \left( \frac{a_k}{a_j} \right)^{\frac{1}{k - j}}$$
                  For example, if the 2nd term is 6 and the 5th term is 162, \(r^{5-2} = r^3 = 162/6 = 27\), so \(r = \sqrt[3]{27} = 3\).
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">Can the common ratio \(r\) of a geometric progression be negative?</h3>
              <div class="faq-answer">
                <p>
                  Yes. When \(r < 0\), the sequence alternates signs on every term. For example, if \(a_1 = 5\) and \(r = -2\), the progression yields: \(5, -10, 20, -40, 80, -160, \dots\). The odd-indexed terms remain positive while even-indexed terms become negative.
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">What happens if the common ratio is zero (\(r = 0\))?</h3>
              <div class="faq-answer">
                <p>
                  If \(r = 0\), the sequence is \(a_1, 0, 0, 0, \dots\). The first term is \(a_1\) and all subsequent terms for \(k \ge 2\) equal zero. While technically conforming to the definition \(a_{k+1} = a_k \cdot 0\), it is considered a degenerate case and is usually excluded from non-trivial mathematical analysis.
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">What is the geometric mean between two numbers?</h3>
              <div class="faq-answer">
                <p>
                  The geometric mean of two positive numbers \(A\) and \(B\) is \(G = \sqrt{A \cdot B}\). In a geometric progression of three terms \(a_1, a_2, a_3\), the middle term is precisely the geometric mean of the surrounding terms: \(a_2 = \sqrt{a_1 \cdot a_3}\). You can explore arithmetic means and statistics using our <a href="arithmetic-sequence-calculator.html">Arithmetic Sequence Calculator</a>.
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
            <li><a href="arithmetic-sequence-calculator.html">Arithmetic Sequence Calculator</a></li>
            <li><a href="exponent-calculator.html">Exponent Calculator</a></li>
            <li><a href="factorial-calculator.html">Factorial Calculator</a></li>
            <li><a href="scientific-notation-calculator.html">Scientific Notation Calculator</a></li>
            <li><a href="quadratic-equation-calculator.html">Quadratic Equation Calculator</a></li>
            <li><a href="fraction-calculator.html">Fraction Calculator</a></li>
            <li><a href="percentage-calculator.html">Percentage Calculator</a></li>
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
        <p>Precision mathematical, engineering, physical, and financial calculation tools.</p>
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
    function calculateGeometricSequence() {
      var a1 = parseFloat(document.getElementById("first_term").value);
      var r = parseFloat(document.getElementById("common_ratio").value);
      var n = parseInt(document.getElementById("term_index").value);
      var previewCount = parseInt(document.getElementById("num_preview").value) || 8;

      if (isNaN(a1) || isNaN(r) || isNaN(n) || n < 1) {
        alert("Please enter valid numerical parameters. N must be a positive integer.");
        return;
      }

      // Compute an
      var an = a1 * Math.pow(r, n - 1);
      var prevTerm = (n > 1) ? (a1 * Math.pow(r, n - 2)) : a1;

      // Compute Sn
      var Sn = 0;
      if (Math.abs(r - 1) < 1e-12) {
        Sn = n * a1;
      } else {
        Sn = a1 * (1 - Math.pow(r, n)) / (1 - r);
      }

      // Compute S_infinity
      var sInfText = "";
      if (Math.abs(r) < 1) {
        var sInf = a1 / (1 - r);
        sInfText = sInf.toLocaleString(undefined, {maximumFractionDigits: 6});
      } else {
        sInfText = "Diverges (|r| ≥ 1)";
      }

      // Behavior
      var behavior = "";
      if (Math.abs(r) < 1) {
        behavior = (r > 0) ? "Decaying to Zero (Convergent)" : "Damped Oscillation (Convergent)";
      } else if (Math.abs(r - 1) < 1e-12) {
        behavior = "Constant Sequence";
      } else if (Math.abs(r + 1) < 1e-12) {
        behavior = "Undamped Constant Oscillation";
      } else {
        behavior = (r > 0) ? "Monotonically Diverging" : "Exploding Alternating Oscillation";
      }

      document.getElementById("primary-result").innerText = "a" + n + " = " + an.toLocaleString(undefined, {maximumFractionDigits: 6});
      document.getElementById("res-partial-sum").innerText = Sn.toLocaleString(undefined, {maximumFractionDigits: 6});
      document.getElementById("res-infinite-sum").innerText = sInfText;
      document.getElementById("res-behavior").innerText = behavior;
      document.getElementById("res-prev-term").innerText = (n > 1) ? prevTerm.toLocaleString(undefined, {maximumFractionDigits: 6}) : "None (Initial)";

      // Build step breakdown
      var steps = "<h4>Analytical Derivation Steps:</h4><ol>";
      steps += "<li><strong>Nth Term Formula:</strong> a_n = a_1 &times; r^(n-1) = " + a1 + " &times; (" + r + ")^(" + (n - 1) + ") = <strong>" + an.toLocaleString(undefined, {maximumFractionDigits: 6}) + "</strong></li>";
      if (Math.abs(r - 1) < 1e-12) {
        steps += "<li><strong>Finite Sum (r = 1):</strong> S_n = n &times; a_1 = " + n + " &times; " + a1 + " = <strong>" + Sn.toLocaleString(undefined, {maximumFractionDigits: 6}) + "</strong></li>";
      } else {
        steps += "<li><strong>Finite Sum (r &ne; 1):</strong> S_" + n + " = " + a1 + " &times; (1 - " + r + "^" + n + ") / (1 - " + r + ") = <strong>" + Sn.toLocaleString(undefined, {maximumFractionDigits: 6}) + "</strong></li>";
      }
      if (Math.abs(r) < 1) {
        var sInfVal = a1 / (1 - r);
        steps += "<li><strong>Infinite Series Limit (|r| < 1):</strong> S_&infin; = a_1 / (1 - r) = " + a1 + " / (1 - " + r + ") = <strong>" + sInfVal.toLocaleString(undefined, {maximumFractionDigits: 6}) + "</strong></li>";
      } else {
        steps += "<li><strong>Infinite Series:</strong> Since |r| = " + Math.abs(r) + " &ge; 1, the infinite series diverges.</li>";
      }
      steps += "</ol>";

      document.getElementById("steps-output").innerHTML = steps;

      // Populate preview table
      var tbody = document.getElementById("tbody-terms");
      tbody.innerHTML = "";
      var runningSum = 0;
      var maxTable = Math.min(previewCount, 25);

      for (var k = 1; k <= maxTable; k++) {
        var termK = a1 * Math.pow(r, k - 1);
        runningSum += termK;
        var tr = document.createElement("tr");
        tr.innerHTML = "<td>" + k + "</td>" +
          "<td>" + a1 + " &times; (" + r + ")^" + (k - 1) + "</td>" +
          "<td>" + termK.toLocaleString(undefined, {maximumFractionDigits: 6}) + "</td>" +
          "<td>" + runningSum.toLocaleString(undefined, {maximumFractionDigits: 6}) + "</td>";
        if (k === n) {
          tr.style.backgroundColor = "var(--bg-highlight, #eef2ff)";
          tr.style.fontWeight = "bold";
        }
        tbody.appendChild(tr);
      }

      document.getElementById("result-box").style.display = "block";
    }

    window.addEventListener("DOMContentLoaded", function() {
      calculateGeometricSequence();
    });
  </script>
</body>
</html>
"""

def main():
    p1 = os.path.join(BASE_DIR, "fraction-to-percent-calculator.html")
    with open(p1, "w", encoding="utf-8") as f:
        f.write(HTML_FRACTION_TO_PERCENT)
    print(f"Generated: {p1}")

    p2 = os.path.join(BASE_DIR, "geometric-sequence-calculator.html")
    with open(p2, "w", encoding="utf-8") as f:
        f.write(HTML_GEOMETRIC_SEQUENCE)
    print(f"Generated: {p2}")

if __name__ == "__main__":
    main()
