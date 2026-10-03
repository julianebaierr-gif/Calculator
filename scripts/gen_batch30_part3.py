# -*- coding: utf-8 -*-
"""
Generator for Batch 30 - Part 3:
5. factors-calculator.html
6. sum-of-integers-calculator.html
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 5. factors-calculator.html
HTML_FACTORS = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Factors Calculator - Find All Divisors, Factor Pairs & Prime Tree</title>
  <meta name="description" content="Find all factors, divisor pairs, prime factorization, divisor sum, and perfect number classification for any integer with step-by-step trial division.">
  <link rel="canonical" href="https://calchub.org/factors-calculator.html">
  <meta property="og:title" content="Factors Calculator - Divisors, Factor Pairs & Prime Factors">
  <meta property="og:description" content="Calculate integer divisors, factor pairs, prime power factorizations, and aliquot sums with complete number-theoretic classification.">
  <meta property="og:url" content="https://calchub.org/factors-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Factors Calculator - Divisor & Factor Pair Solver">
  <meta name="twitter:description" content="Free online factors calculator. Find all factors, prime factor tree, factor pairs, and divisor counts for any integer with full step-by-step breakdown.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Factors Calculator",
    "url": "https://calchub.org/factors-calculator.html",
    "description": "Calculates integer divisors, factor pairs, prime factor trees, total factor count d(n), and sum of divisors sigma(n) with step-by-step algorithms.",
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
        "name": "What is a factor of an integer?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A factor (or divisor) of an integer N is an integer d that divides N with zero remainder (N mod d = 0). For example, the factors of 12 are 1, 2, 3, 4, 6, and 12."
        }
      },
      {
        "@type": "Question",
        "name": "What are factor pairs?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Factor pairs are pairs of integers (a, b) that multiply together to produce the given number (a · b = N). For example, the factor pairs of 24 are (1, 24), (2, 12), (3, 8), and (4, 6)."
        }
      },
      {
        "@type": "Question",
        "name": "How do you calculate the total number of divisors d(N)?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Using prime factorization N = p1^a1 · p2^a2 · ... · pk^ak, the total count of divisors is given by the multiplicative formula: d(N) = (a1 + 1)(a2 + 1) · ... · (ak + 1)."
        }
      },
      {
        "@type": "Question",
        "name": "What is a perfect number?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A perfect number is a positive integer equal to the sum of its proper positive divisors (excluding the number itself). The first two perfect numbers are 6 (1 + 2 + 3 = 6) and 28 (1 + 2 + 4 + 7 + 14 = 28)."
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
      <span>Factors Calculator</span>
    </nav>

    <div class="content-layout">
      <div class="main-column">
        <div class="calculator-card">
          <div class="calculator-header">
            <span class="calc-icon">🔢</span>
            <h1>Factors & Divisors Calculator</h1>
          </div>
          <p class="calc-description">
            Extract all positive divisors, factor pairs, unique prime factorization, divisor count \(d(n)\), and aliquot sum for any positive integer.
          </p>

          <form id="calc-form" class="calc-form" onsubmit="return false;">
            <div class="input-grid">
              <div class="form-group">
                <label for="integer_n">Target Integer (\(N\)):</label>
                <input type="number" id="integer_n" class="form-control" value="72" step="1" min="1" max="1000000000" placeholder="e.g. 72 or 360" required>
                <span class="help-text">Positive integer (\(N \ge 1\)).</span>
              </div>
              <div class="form-group" style="display:flex;align-items:flex-end;">
                <button type="button" id="btn-calculate" class="btn btn-primary" style="width:100%;" onclick="calculateFactors()">Find All Factors</button>
              </div>
            </div>
          </form>

          <div id="result-box" class="result-box" style="display:none;">
            <h3>Factor Analysis Results</h3>
            <div class="result-highlight" id="primary-result">12 Factors Found for 72</div>
            
            <div class="result-grid">
              <div class="result-item">
                <span class="res-label">Total Factors Count (\(d(n)\)):</span>
                <span class="res-val" id="res-count">12</span>
              </div>
              <div class="result-item">
                <span class="res-label">Prime Factorization:</span>
                <span class="res-val" id="res-prime-factors">2³ &times; 3²</span>
              </div>
              <div class="result-item">
                <span class="res-label">Sum of Divisors (\(\sigma(n)\)):</span>
                <span class="res-val" id="res-sum">195</span>
              </div>
              <div class="result-item">
                <span class="res-label">Classification:</span>
                <span class="res-val" id="res-class">Abundant (Proper Sum = 123)</span>
              </div>
            </div>

            <div style="margin-top:1.25rem;">
              <h4>All Positive Factors of <span id="span-target-n">72</span>:</h4>
              <p id="p-factors-list" style="font-size:1.05rem;font-weight:600;color:var(--primary);line-height:1.6;"></p>
            </div>

            <div style="margin-top:1.25rem;">
              <h4>Factor Pairs:</h4>
              <ul id="ul-factor-pairs" style="display:grid;grid-template-columns:repeat(auto-fit, minmax(140px, 1fr));gap:0.5rem;padding:0;list-style:none;">
                <!-- Populated dynamically -->
              </ul>
            </div>

            <div class="conversion-steps" id="steps-output">
              <!-- Steps output -->
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. Fundamental Number Theory of Divisors and Factorization</h2>
          <p>
            In number theory and elementary algebra, a <strong>factor</strong> (or <strong>divisor</strong>) of an integer \(N\) is an integer \(d\) that divides \(N\) completely with zero remainder:
          </p>
          $$d \mid N \iff \exists q \in \mathbb{Z} \text{ such that } N = d \cdot q \iff N \pmod d = 0$$
          <p>
            The two integers \((d, q)\) constitute a <strong>factor pair</strong> because their algebraic product reconstructs the dividend \(N\). By pairing every factor \(d \le \sqrt{N}\) with its complementary factor \(q = N/d \ge \sqrt{N}\), trial division algorithms terminate at the square root boundary \(\sqrt{N}\), reducing algorithmic time complexity from \(O(N)\) to \(O(\sqrt{N})\).
          </p>

          <h2>2. The Fundamental Theorem of Arithmetic and Divisor Counting</h2>
          <p>
            The <strong>Fundamental Theorem of Arithmetic</strong> guarantees that every integer \(N > 1\) can be represented uniquely (up to the ordering of factors) as a product of prime powers:
          </p>
          $$N = p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdots p_k^{\alpha_k} = \prod_{i=1}^k p_i^{\alpha_i}$$
          <p>
            where \(p_1 < p_2 < \dots < p_k\) are distinct prime numbers and \(\alpha_i \in \mathbb{N}^+\) are positive integer exponents.
          </p>

          <h3>2.1 The Divisor Function \(d(N)\)</h3>
          <p>
            Every divisor \(d\) of \(N\) must be composed of prime factors from the same set, with exponents bounded by \(\alpha_i\):
          </p>
          $$d = p_1^{\beta_1} \cdot p_2^{\beta_2} \cdots p_k^{\beta_k} \quad \text{where } 0 \le \beta_i \le \alpha_i$$
          <p>
            By the combinatorial multiplication rule, each exponent \(\beta_i\) can independently assume any of \((\alpha_i + 1)\) integer values (\(0, 1, 2, \dots, \alpha_i\)). Consequently, the total number of positive divisors \(d(N)\) (often written \(\tau(N)\)) is given by:
          </p>
          $$d(N) = (\alpha_1 + 1)(\alpha_2 + 1) \cdots (\alpha_k + 1) = \prod_{i=1}^k (\alpha_i + 1)$$
          <p>
            For example, for \(N = 72 = 2^3 \times 3^2\):
          </p>
          $$d(72) = (3 + 1)(2 + 1) = 4 \times 3 = 12 \text{ divisors}$$

          <h3>2.2 Sum of Divisors Function \(\sigma(N)\)</h3>
          <p>
            The arithmetic sum of all positive divisors \(\sigma(N)\) is a multiplicative arithmetic function evaluated through the closed-form geometric progression series:
          </p>
          $$\sigma(N) = \prod_{i=1}^k \left( \sum_{j=0}^{\alpha_i} p_i^j \right) = \prod_{i=1}^k \left( \frac{p_i^{\alpha_i + 1} - 1}{p_i - 1} \right)$$
          <p>
            For \(72 = 2^3 \times 3^2\):
          </p>
          $$\sigma(72) = \left( \frac{2^{4} - 1}{2 - 1} \right) \left( \frac{3^{3} - 1}{3 - 1} \right) = (15) \left( \frac{26}{2} \right) = 15 \times 13 = 195$$

          <h2>3. Number-Theoretic Classification by Aliquot Sum</h2>
          <p>
            In recreational and theoretical mathematics, integers are classified based on their <strong>aliquot sum</strong> \(s(N)\), which is the sum of all <em>proper</em> divisors (excluding \(N\) itself): \(s(N) = \sigma(N) - N\).
          </p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Classification</th>
                <th>Mathematical Criterion</th>
                <th>Proper Divisor Sum (\(s(N)\))</th>
                <th>Examples</th>
                <th>Analytical Significance</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Prime Number</strong></td>
                <td>\(d(N) = 2\)</td>
                <td>\(s(N) = 1\)</td>
                <td>2, 3, 5, 7, 11, 13, 17</td>
                <td>Atomic building blocks of arithmetic; basis of RSA cryptography.</td>
              </tr>
              <tr>
                <td><strong>Composite Number</strong></td>
                <td>\(d(N) > 2\)</td>
                <td>\(s(N) > 1\)</td>
                <td>4, 6, 8, 9, 10, 12, 14</td>
                <td>Possesses non-trivial factorization.</td>
              </tr>
              <tr>
                <td><strong>Perfect Number</strong></td>
                <td>\(\sigma(N) = 2N\)</td>
                <td>\(s(N) = N\)</td>
                <td>6, 28, 496, 8128</td>
                <td>Euclid-Euler theorem: \(2^{p-1}(2^p - 1)\) for Mersenne primes.</td>
              </tr>
              <tr>
                <td><strong>Deficient Number</strong></td>
                <td>\(\sigma(N) < 2N\)</td>
                <td>\(s(N) < N\)</td>
                <td>1, 2, 3, 4, 5, 7, 8, 9, 10</td>
                <td>All prime numbers and their prime powers are deficient.</td>
              </tr>
              <tr>
                <td><strong>Abundant Number</strong></td>
                <td>\(\sigma(N) > 2N\)</td>
                <td>\(s(N) > N\)</td>
                <td>12, 18, 20, 24, 30, 36, 72</td>
                <td>Excess divisor abundance; abundant numbers possess high symmetry.</td>
              </tr>
            </tbody>
          </table>

          <h2>4. Benchmark Integer Factor Matrix</h2>
          <p>
            The table below provides factorization data for canonical engineering and structural integers:
          </p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Integer (\(N\))</th>
                <th>Prime Factorization</th>
                <th>Divisor Count (\(d(N)\))</th>
                <th>Complete Divisors List</th>
                <th>Sum (\(\sigma(N)\))</th>
                <th>Class</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>12</td>
                <td>\(2^2 \times 3^1\)</td>
                <td>6</td>
                <td>1, 2, 3, 4, 6, 12</td>
                <td>28</td>
                <td>Abundant</td>
              </tr>
              <tr>
                <td>24</td>
                <td>\(2^3 \times 3^1\)</td>
                <td>8</td>
                <td>1, 2, 3, 4, 6, 8, 12, 24</td>
                <td>60</td>
                <td>Abundant</td>
              </tr>
              <tr>
                <td>28</td>
                <td>\(2^2 \times 7^1\)</td>
                <td>6</td>
                <td>1, 2, 4, 7, 14, 28</td>
                <td>56</td>
                <td><strong>Perfect</strong></td>
              </tr>
              <tr>
                <td>36</td>
                <td>\(2^2 \times 3^2\)</td>
                <td>9</td>
                <td>1, 2, 3, 4, 6, 9, 12, 18, 36</td>
                <td>91</td>
                <td>Abundant (Square)</td>
              </tr>
              <tr>
                <td>60</td>
                <td>\(2^2 \times 3 \times 5\)</td>
                <td>12</td>
                <td>1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60</td>
                <td>168</td>
                <td>Abundant (Sexagesimal base)</td>
              </tr>
              <tr>
                <td>72</td>
                <td>\(2^3 \times 3^2\)</td>
                <td>12</td>
                <td>1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72</td>
                <td>195</td>
                <td>Abundant</td>
              </tr>
              <tr>
                <td>100</td>
                <td>\(2^2 \times 5^2\)</td>
                <td>9</td>
                <td>1, 2, 4, 5, 10, 20, 25, 50, 100</td>
                <td>217</td>
                <td>Abundant (Square)</td>
              </tr>
              <tr>
                <td>360</td>
                <td>\(2^3 \times 3^2 \times 5\)</td>
                <td>24</td>
                <td>1, 2, 3, ..., 180, 360 (24 total)</td>
                <td>1170</td>
                <td>Highly Composite</td>
              </tr>
            </tbody>
          </table>

          <h2>5. Mechanical Engineering and Cryptographic Case Studies</h2>

          <div class="worked-example-card">
            <h3>Case Study 1: Mechanical Gearbox Tooth Count Factorization for Uniform Wear</h3>
            <p>
              A mechanical powertrain design engineer designs a two-gear reduction drive where the driving pinion has \(N_1 = 17\text{ teeth}\) and the driven gear has \(N_2 = 72\text{ teeth}\). Factorization analysis is required to verify that the gear set possesses the "hunting tooth" property to maximize gear life.
            </p>
            <div class="example-body">
              <p><strong>Factorization of \(N_1 = 17\):</strong> 17 is a prime number (factors: 1, 17).</p>
              <p><strong>Factorization of \(N_2 = 72\):</strong> \(72 = 2^3 \times 3^2\) (factors: 1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72).</p>
              <p><strong>Coprime Analysis:</strong></p>
              $$\gcd(17, 72) = 1$$
              <p><strong>Engineering Finding:</strong> Because 17 and 72 share no common factors other than 1, every individual pinion tooth meshes with every driven gear tooth before any two teeth meet again. This guarantees uniform wear and prevents localized tooth failure.</p>
            </div>
          </div>

          <div class="worked-example-card">
            <h3>Case Study 2: Cryptographic RSA Semi-Prime Factoring Complexity</h3>
            <p>
              In public-key cryptography, security relies on the asymmetry between multiplication and factoring. A public key modulus is a semi-prime \(N = 8,989\). Find the prime factors \(p\) and \(q\) via trial division up to \(\sqrt{N}\).
            </p>
            <div class="example-body">
              <p><strong>Step 1: Compute square root boundary:</strong></p>
              $$\sqrt{8989} \approx 94.81$$
              <p>Trial division only needs to test prime numbers up to 89: \(\{2, 3, 5, 7, 11, 13, \dots, 89\}\).</p>
              <p><strong>Step 2: Testing primes:</strong></p>
              $$8989 \div 89 = 101 \implies 89 \times 101 = 8989$$
              <p><strong>Cryptographic Result:</strong> Both \(p = 89\) and \(q = 101\) are prime. The totient is \(\phi(N) = (89-1)(101-1) = 88 \times 100 = 8,800\), enabling private key recovery.</p>
            </div>
          </div>

          <h2>6. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-accordion">
            <div class="faq-item">
              <h3 class="faq-question">Why do perfect square numbers have an odd number of factors?</h3>
              <div class="faq-answer">
                <p>
                  Factors of an integer occur in pairs \((a, b)\) where \(a \cdot b = N\). If \(N\) is not a perfect square, all factor pairs are distinct, yielding an even count of factors. If \(N\) is a perfect square, one pair consists of identical integers (\(\sqrt{N} \cdot \sqrt{N} = N\)), adding only a single unique factor to the set and making the total divisor count odd.
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">What is a highly composite number?</h3>
              <div class="faq-answer">
                <p>
                  A highly composite number is a positive integer that has strictly more divisors than any smaller positive integer. Examples include 1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, and 360. They are widely used as measurement radices (such as 360 degrees in a circle or 60 seconds in a minute) due to their high divisibility.
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">How does finding factors relate to GCD and LCM?</h3>
              <div class="faq-answer">
                <p>
                  The Greatest Common Divisor (GCD) of two numbers is the largest shared factor from their respective factor lists. You can compute greatest common divisors and least common multiples using our <a href="gcd-lcm-calculator.html">GCD & LCM Calculator</a>.
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">How do you know if a number is prime using factors?</h3>
              <div class="faq-answer">
                <p>
                  A number \(N > 1\) is prime if and only if it possesses exactly two distinct factors: 1 and \(N\). You can test primality and view divisor trees using our <a href="prime-number-calculator.html">Prime Number Calculator</a>.
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
            <li><a href="prime-number-calculator.html">Prime Number Calculator</a></li>
            <li><a href="gcd-lcm-calculator.html">GCD & LCM Calculator</a></li>
            <li><a href="square-root-calculator.html">Square Root Calculator</a></li>
            <li><a href="long-division-calculator.html">Long Division Calculator</a></li>
            <li><a href="modulo-calculator.html">Modulo Calculator</a></li>
            <li><a href="fraction-calculator.html">Fraction Calculator</a></li>
            <li><a href="scientific-notation-calculator.html">Scientific Notation Calculator</a></li>
            <li><a href="exponent-calculator.html">Exponent Calculator</a></li>
          </ul>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-col">
        <h4>CalcHub</h4>
        <p>Comprehensive mathematical, number-theoretic, and scientific calculation tools.</p>
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
    function calculateFactors() {
      var n = parseInt(document.getElementById("integer_n").value);

      if (isNaN(n) || n < 1) {
        alert("Please enter a positive integer greater than or equal to 1.");
        return;
      }

      var factors = [];
      var factorPairs = [];
      var limit = Math.floor(Math.sqrt(n));

      for (var d = 1; d <= limit; d++) {
        if (n % d === 0) {
          factors.push(d);
          var comp = n / d;
          factorPairs.push([d, comp]);
          if (comp !== d) {
            factors.push(comp);
          }
        }
      }

      factors.sort(function(a, b) { return a - b; });

      // Prime factorization
      var temp = n;
      var primeFactors = {};
      var divisor = 2;
      while (divisor * divisor <= temp) {
        while (temp % divisor === 0) {
          primeFactors[divisor] = (primeFactors[divisor] || 0) + 1;
          temp /= divisor;
        }
        divisor++;
      }
      if (temp > 1) {
        primeFactors[temp] = (primeFactors[temp] || 0) + 1;
      }

      // Format prime factorization
      var supMap = {
        "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵",
        "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹", "0": "⁰"
      };
      var primeParts = [];
      for (var p in primeFactors) {
        var exp = primeFactors[p];
        if (exp === 1) {
          primeParts.push(p);
        } else {
          var expStr = exp.toString();
          var supExp = "";
          for (var i = 0; i < expStr.length; i++) {
            supExp += supMap[expStr[i]] || expStr[i];
          }
          primeParts.push(p + supExp);
        }
      }
      var primeFactorStr = (n === 1) ? "None (Unit)" : primeParts.join(" &times; ");

      // Sum of divisors
      var sum = 0;
      for (var k = 0; k < factors.length; k++) {
        sum += factors[k];
      }

      var properSum = sum - n;
      var classText = "";
      if (n === 1) {
        classText = "Unit (Neither Prime nor Composite)";
      } else if (factors.length === 2) {
        classText = "Prime Number";
      } else if (properSum === n) {
        classText = "Perfect Number (Proper Sum = " + n + ")";
      } else if (properSum < n) {
        classText = "Deficient (Proper Sum = " + properSum + " < " + n + ")";
      } else {
        classText = "Abundant (Proper Sum = " + properSum + " > " + n + ")";
      }

      document.getElementById("primary-result").innerText = factors.length + " Factors Found for " + n;
      document.getElementById("res-count").innerText = factors.length.toString();
      document.getElementById("res-prime-factors").innerHTML = primeFactorStr;
      document.getElementById("res-sum").innerText = sum.toString();
      document.getElementById("res-class").innerText = classText;
      document.getElementById("span-target-n").innerText = n.toString();

      document.getElementById("p-factors-list").innerText = factors.join(", ");

      // Populate pairs
      var ulPairs = document.getElementById("ul-factor-pairs");
      ulPairs.innerHTML = "";
      for (var pIdx = 0; pIdx < factorPairs.length; pIdx++) {
        var pair = factorPairs[pIdx];
        var li = document.createElement("li");
        li.style.background = "#F8FAFC";
        li.style.border = "1px solid var(--border-light, #E2E8F0)";
        li.style.padding = "0.5rem 0.75rem";
        li.style.borderRadius = "6px";
        li.style.textAlign = "center";
        li.innerHTML = pair[0] + " &times; " + pair[1] + " = " + n;
        ulPairs.appendChild(li);
      }

      var steps = "<h4>Step-by-Step Divisor Analysis:</h4><ol>";
      steps += "<li><strong>Trial Division Limit:</strong> Check divisors up to &radic;" + n + " &approx; " + limit + "</li>";
      steps += "<li><strong>Prime Factorization:</strong> " + n + " = " + primeFactorStr + "</li>";
      steps += "<li><strong>Divisor Count Formula:</strong> d(" + n + ") = " + factors.length + " total divisors</li>";
      steps += "<li><strong>Sum of Divisors:</strong> &sigma;(" + n + ") = " + sum + " (Proper Sum = " + properSum + ")</li>";
      steps += "</ol>";

      document.getElementById("steps-output").innerHTML = steps;
      document.getElementById("result-box").style.display = "block";
    }

    window.addEventListener("DOMContentLoaded", function() {
      calculateFactors();
    });
  </script>
</body>
</html>
"""

# 6. sum-of-integers-calculator.html
HTML_SUM_OF_INTEGERS = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sum of Integers Calculator - Consecutive Numbers & Gauss Series</title>
  <meta name="description" content="Calculate the sum of consecutive integers, sum of first n numbers, sum of squares, and sum of cubes using Gauss's arithmetic series formulas with step-by-step proofs.">
  <link rel="canonical" href="https://calchub.org/sum-of-integers-calculator.html">
  <meta property="og:title" content="Sum of Integers Calculator - Gauss Series & Range Sum">
  <meta property="og:description" content="Compute consecutive integer sums, triangular numbers, square series, and cube series with closed-form mathematical derivations.">
  <meta property="og:url" content="https://calchub.org/sum-of-integers-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Sum of Integers Calculator - Arithmetic Series Solver">
  <meta name="twitter:description" content="Free sum of integers calculator. Evaluates consecutive sums from a to b, triangular numbers, sums of squares, and loop iteration complexities.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Sum of Integers Calculator",
    "url": "https://calchub.org/sum-of-integers-calculator.html",
    "description": "Calculates the sum of consecutive integers from a to b, triangular numbers, sum of squares, and sum of cubes using Gauss arithmetic progression formulas.",
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
        "name": "What is Gauss's formula for the sum of the first n integers?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The sum of the first n consecutive positive integers is given by Carl Friedrich Gauss's formula: S_n = n(n + 1) / 2."
        }
      },
      {
        "@type": "Question",
        "name": "How do you calculate the sum of integers between a and b?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The sum of consecutive integers from a to b inclusive is: S = n · (a + b) / 2, where the number of terms is n = b - a + 1."
        }
      },
      {
        "@type": "Question",
        "name": "What is the formula for the sum of consecutive squares?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The sum of the squares of the first n integers is: ∑ k² = n(n + 1)(2n + 1) / 6."
        }
      },
      {
        "@type": "Question",
        "name": "What is the formula for the sum of consecutive cubes?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Nicomachus's Theorem states that the sum of the first n cubes equals the square of the sum of the first n integers: ∑ k³ = [n(n + 1) / 2]² = S_n²."
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
      <span>Sum of Integers Calculator</span>
    </nav>

    <div class="content-layout">
      <div class="main-column">
        <div class="calculator-card">
          <div class="calculator-header">
            <span class="calc-icon">∑</span>
            <h1>Sum of Integers Calculator</h1>
          </div>
          <p class="calc-description">
            Calculate the sum of consecutive integers between any starting and ending values, triangular numbers, sum of squares \(\sum k^2\), and sum of cubes \(\sum k^3\).
          </p>

          <form id="calc-form" class="calc-form" onsubmit="return false;">
            <div class="input-grid">
              <div class="form-group">
                <label for="start_int">Start Integer (\(a\)):</label>
                <input type="number" id="start_int" class="form-control" value="1" step="1" placeholder="e.g. 1" required>
                <span class="help-text">First term of the sequence.</span>
              </div>
              <div class="form-group">
                <label for="end_int">End Integer (\(b\)):</label>
                <input type="number" id="end_int" class="form-control" value="100" step="1" placeholder="e.g. 100" required>
                <span class="help-text">Last term of the sequence (\(b \ge a\)).</span>
              </div>
              <div class="form-group" style="display:flex;align-items:flex-end;">
                <button type="button" id="btn-calculate" class="btn btn-primary" style="width:100%;" onclick="calculateSumOfIntegers()">Compute Series Sum</button>
              </div>
            </div>
          </form>

          <div id="result-box" class="result-box" style="display:none;">
            <h3>Series Summation Results</h3>
            <div class="result-highlight" id="primary-result">Sum (1 to 100) = 5,050</div>
            
            <div class="result-grid">
              <div class="result-item">
                <span class="res-label">Consecutive Linear Sum (\(S\)):</span>
                <span class="res-val" id="res-sum">5,050</span>
              </div>
              <div class="result-item">
                <span class="res-label">Number of Terms (\(n\)):</span>
                <span class="res-val" id="res-terms">100</span>
              </div>
              <div class="result-item">
                <span class="res-label">Arithmetic Mean (\(\bar{x}\)):</span>
                <span class="res-val" id="res-mean">50.50</span>
              </div>
              <div class="result-item">
                <span class="res-label">Sum of Squares (\(\sum k^2\)):</span>
                <span class="res-val" id="res-sum-sq">338,350</span>
              </div>
              <div class="result-item">
                <span class="res-label">Sum of Cubes (\(\sum k^3\)):</span>
                <span class="res-val" id="res-sum-cube">25,502,500</span>
              </div>
              <div class="result-item">
                <span class="res-label">Formula Representation:</span>
                <span class="res-val" id="res-formula">\(\frac{n(a + b)}{2}\)</span>
              </div>
            </div>

            <div class="conversion-steps" id="steps-output">
              <!-- Steps output -->
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. Mathematical Foundations of Consecutive Integer Summation</h2>
          <p>
            The summation of consecutive integers is one of the foundational cornerstones of discrete mathematics, combinatorics, and algorithmic complexity. Formally, a sequence of consecutive integers constitutes an <strong>arithmetic progression</strong> with initial term \(a\), terminal term \(b\), and common difference \(d = 1\).
          </p>
          <p>
            The total number of terms \(n\) in the inclusive interval \([a, b]\) is:
          </p>
          $$n = b - a + 1$$
          <p>
            The total sum \(S\) of these \(n\) consecutive integers is given by the pairing theorem:
          </p>
          $$S = \sum_{k=a}^b k = \frac{n(a + b)}{2} = n \cdot \bar{x}$$
          <p>
            where \(\bar{x} = \frac{a + b}{2}\) represents the exact arithmetic mean of the sequence.
          </p>

          <h2>2. Gauss's Pairing Proof and Triangular Numbers</h2>
          <p>
            According to mathematical lore, when Carl Friedrich Gauss was an elementary schoolboy in Brunswick, Germany (c. 1787), his teacher asked the class to compute the sum of the first 100 integers: \(1 + 2 + 3 + \dots + 100\). While other students began laborious addition, young Gauss noticed that folding the sequence back upon itself created 50 pairs that each summed to 101:
          </p>
          $$\begin{aligned}
          S &= 1 &+ 2 &+ 3 &+ \dots &+ 99 &+ 100 \\
          S &= 100 &+ 99 &+ 98 &+ \dots &+ 2 &+ 1 \\
          \hline
          2S &= 101 &+ 101 &+ 101 &+ \dots &+ 101 &+ 101
          \end{aligned}$$
          <p>
            Because there are exactly 100 terms:
          </p>
          $$2S = 100 \times 101 \implies S = \frac{100 \times 101}{2} = 5,050$$
          <p>
            This established the universal formula for the \(n\)th <strong>triangular number</strong> \(T_n\):
          </p>
          $$T_n = \sum_{k=1}^n k = \frac{n(n + 1)}{2}$$

          <h2>3. Higher Power Integer Sums: Squares, Cubes and Faulhaber's Theorem</h2>
          <p>
            In mathematical analysis, evaluating Riemann sums and polynomial integrals requires closed-form formulas for higher powers of integers, codified by Johann Faulhaber in 1631:
          </p>

          <h3>3.1 Sum of Consecutive Squares (\(\sum k^2\))</h3>
          <p>
            The sum of the squares of the first \(n\) positive integers is:
          </p>
          $$\sum_{k=1}^n k^2 = 1^2 + 2^2 + 3^2 + \dots + n^2 = \frac{n(n + 1)(2n + 1)}{6}$$
          <p>
            For an arbitrary interval \([a, b]\), evaluate:
          </p>
          $$\sum_{k=a}^b k^2 = \sum_{k=1}^b k^2 - \sum_{k=1}^{a-1} k^2$$

          <h3>3.2 Sum of Consecutive Cubes (\(\sum k^3\)) - Nicomachus's Theorem</h3>
          <p>
            Remarkably, the sum of the cubes of the first \(n\) integers is identically equal to the square of the sum of the integers themselves:
          </p>
          $$\sum_{k=1}^n k^3 = 1^3 + 2^3 + 3^3 + \dots + n^3 = \left[ \frac{n(n + 1)}{2} \right]^2 = T_n^2$$

          <h3>3.3 Mathematical Induction Proof of the Gauss Sum</h3>
          <p>
            To rigorously verify Gauss's formula for all \(n \in \mathbb{N}^+\), apply mathematical induction:
          </p>
          <ol>
            <li>
              <strong>Base Case (\(n = 1\)):</strong>
              $$\sum_{k=1}^1 k = 1, \quad \frac{1(1 + 1)}{2} = \frac{2}{2} = 1 \quad (\text{Holds true})$$
            </li>
            <li>
              <strong>Induction Hypothesis:</strong> Assume true for \(n = m\): \(\sum_{k=1}^m k = \frac{m(m + 1)}{2}\).
            </li>
            <li>
              <strong>Induction Step (\(n = m + 1\)):</strong>
              $$\sum_{k=1}^{m+1} k = \left( \sum_{k=1}^m k \right) + (m + 1) = \frac{m(m + 1)}{2} + (m + 1)$$
              Factoring out \((m + 1)\):
              $$(m + 1) \left( \frac{m}{2} + 1 \right) = (m + 1) \left( \frac{m + 2}{2} \right) = \frac{(m + 1)((m + 1) + 1)}{2}$$
              The identity holds for \(m + 1\), completing the proof for all natural numbers \(\mathbb{N}^+\).
            </li>
          </ol>

          <h2>4. Reference Matrix: Consecutive Sums and Triangular Numbers</h2>
          <p>
            The matrix below compiles standard benchmark summation horizons:
          </p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Range Horizon (\(n\))</th>
                <th>Linear Sum (\(S_n\))</th>
                <th>Arithmetic Mean (\(\bar{x}\))</th>
                <th>Sum of Squares (\(\sum k^2\))</th>
                <th>Sum of Cubes (\(\sum k^3\))</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>1 to 5</td>
                <td>15</td>
                <td>3.0</td>
                <td>55</td>
                <td>225</td>
              </tr>
              <tr>
                <td>1 to 10</td>
                <td>55</td>
                <td>5.5</td>
                <td>385</td>
                <td>3,025</td>
              </tr>
              <tr>
                <td>1 to 20</td>
                <td>210</td>
                <td>10.5</td>
                <td>2,870</td>
                <td>44,100</td>
              </tr>
              <tr>
                <td>1 to 50</td>
                <td>1,275</td>
                <td>25.5</td>
                <td>42,925</td>
                <td>1,625,625</td>
              </tr>
              <tr>
                <td>1 to 100</td>
                <td>5,050</td>
                <td>50.5</td>
                <td>338,350</td>
                <td>25,502,500</td>
              </tr>
              <tr>
                <td>1 to 500</td>
                <td>125,250</td>
                <td>250.5</td>
                <td>41,791,750</td>
                <td>15,687,562,500</td>
              </tr>
              <tr>
                <td>1 to 1,000</td>
                <td>500,500</td>
                <td>500.5</td>
                <td>333,833,500</td>
                <td>250,500,250,000</td>
              </tr>
            </tbody>
          </table>

          <h2>5. Computer Science, Networking & Civil Engineering Case Studies</h2>

          <div class="worked-example-card">
            <h3>Case Study 1: Computer Science Nested Loop Algorithmic Time Complexity</h3>
            <p>
              A software performance engineer analyzes a quadratic bubble-sort routine containing nested loops:
            </p>
            <pre style="background:#F8FAFC;padding:0.75rem;border-radius:6px;font-size:0.85rem;border:1px solid #E2E8F0;">
for (int i = 1; i < N; i++) {
    for (int j = i + 1; j <= N; j++) {
        compare_and_swap(j, i);
    }
}</pre>
            <p>
              For an input dataset of size \(N = 500\), determine the exact number of comparisons executed.
            </p>
            <div class="example-body">
              <p><strong>Analysis:</strong> On outer iteration \(i = 1\), the inner loop runs \(N - 1\) times. On iteration \(i = 2\), it runs \(N - 2\) times, down to 1 time. The total operations equal the sum of integers from 1 to \(N - 1 = 499\):</p>
              $$\text{Comparisons} = \sum_{k=1}^{499} k = \frac{499(500)}{2} = 499 \times 250 = 124,750 \text{ operations}$$
              <p><strong>Complexity Result:</strong> The nested loops execute exactly \(124,750\) operations, confirming the asymptotic bound \(O(N^2) \approx \frac{1}{2}N^2\).</p>
            </div>
          </div>

          <div class="worked-example-card">
            <h3>Case Study 2: Civil Structural Tiered Amphitheater Seating Capacity</h3>
            <p>
              An architectural design team designs a fan-shaped tiered outdoor amphitheater. Row 1 (the lowest row) has \(a = 36\text{ seats}\). Due to radial expansion, each subsequent row adds exactly 1 additional seat (\(d = 1\)). The theater has \(n = 25\text{ rows}\), so the top row has \(b = 36 + 24 = 60\text{ seats}\). Calculate the total seating capacity.
            </p>
            <div class="example-body">
              <p><strong>Parameters:</strong> \(a = 36\), \(b = 60\), \(n = 25\).</p>
              <p><strong>Step 1: Compute total capacity:</strong></p>
              $$S = \frac{n(a + b)}{2} = \frac{25 \times (36 + 60)}{2} = \frac{25 \times 96}{2} = 25 \times 48 = 1,200\text{ seats}$$
              <p><strong>Architectural Verification:</strong> The venue provides an exact total capacity of \(1,200\) spectator seats.</p>
            </div>
          </div>

          <div class="worked-example-card">
            <h3>Case Study 3: Cloud Data Center Full-Mesh VPC Peering Connections</h3>
            <p>
              A cloud infrastructure architect designs a multi-region VPC topology linking \(V = 48\text{ virtual networks}\) in a non-blocking full-mesh peering configuration. Calculate the required peering connection tunnels.
            </p>
            <div class="example-body">
              <p><strong>Graph Theory Formulation:</strong> In a complete undirected graph \(K_V\), the number of bidirectional connections equals the sum of integers from 1 to \(V - 1\):</p>
              $$E = \frac{V(V - 1)}{2} = \frac{48 \times 47}{2} = 24 \times 47 = 1,128\text{ peering tunnels}$$
              <p><strong>Network Finding:</strong> Because maintaining 1,128 tunnels exceeds cloud quota limits (typically 50-125 peerings per VPC), the architect transitions the design to a centralized Transit Gateway topology.</p>
            </div>
          </div>

          <h2>6. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-accordion">
            <div class="faq-item">
              <h3 class="faq-question">Can the starting integer \(a\) be negative?</h3>
              <div class="faq-answer">
                <p>
                  Yes! The formula \(S = \frac{n(a + b)}{2}\) is universally valid for all integers, positive, zero, or negative. For example, summing from \(-5\) to \(+5\): \(n = 5 - (-5) + 1 = 11\) terms, \(S = \frac{11(-5 + 5)}{2} = 0\), because symmetric positive and negative terms cancel out.
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">What is the handshake problem in network graph theory?</h3>
              <div class="faq-answer">
                <p>
                  If \(N\) people in a room each shake hands with every other person, the total handshakes is equal to the sum of integers from 1 to \(N-1\): \(\frac{N(N-1)}{2}\). This formula defines the number of edges in a complete network graph \(K_N\).
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">How does this relate to an arithmetic sequence?</h3>
              <div class="faq-answer">
                <p>
                  Consecutive integers represent a specific arithmetic sequence where the common difference is \(d = 1\). For sequences with different step sizes (e.g., odd numbers where \(d = 2\)), use our generalized <a href="arithmetic-sequence-calculator.html">Arithmetic Sequence Calculator</a>.
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">How do you find the sum of only even or only odd integers?</h3>
              <div class="faq-answer">
                <p>
                  The sum of the first \(n\) even integers is \(n(n + 1)\). The sum of the first \(n\) odd integers is a perfect square: \(n^2\). For example, the sum of the first 4 odd numbers is \(1 + 3 + 5 + 7 = 16 = 4^2\).
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
            <li><a href="geometric-sequence-calculator.html">Geometric Sequence Calculator</a></li>
            <li><a href="mean-median-mode-calculator.html">Mean Median Mode Calculator</a></li>
            <li><a href="factorial-calculator.html">Factorial Calculator</a></li>
            <li><a href="prime-number-calculator.html">Prime Number Calculator</a></li>
            <li><a href="gcd-lcm-calculator.html">GCD & LCM Calculator</a></li>
            <li><a href="factors-calculator.html">Factors Calculator</a></li>
            <li><a href="pythagorean-theorem-calculator.html">Pythagorean Theorem Calculator</a></li>
          </ul>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-col">
        <h4>CalcHub</h4>
        <p>Comprehensive mathematical, combinatorial, and discrete calculation tools.</p>
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
    function sumSquares(n) {
      return (n * (n + 1) * (2 * n + 1)) / 6;
    }

    function sumCubes(n) {
      var s = (n * (n + 1)) / 2;
      return s * s;
    }

    function calculateSumOfIntegers() {
      var a = parseInt(document.getElementById("start_int").value);
      var b = parseInt(document.getElementById("end_int").value);

      if (isNaN(a) || isNaN(b)) {
        alert("Please enter valid integers for start and end.");
        return;
      }

      if (b < a) {
        alert("Ending integer b must be greater than or equal to starting integer a.");
        return;
      }

      var n = b - a + 1;
      var sum = (n * (a + b)) / 2;
      var mean = (a + b) / 2;

      // Sum of squares & cubes between a and b
      var sqSum = 0;
      var cubeSum = 0;
      if (a >= 1) {
        sqSum = sumSquares(b) - sumSquares(a - 1);
        cubeSum = sumCubes(b) - sumCubes(a - 1);
      } else {
        // Direct accumulation for non-positive start
        for (var k = a; k <= b; k++) {
          sqSum += (k * k);
          cubeSum += (k * k * k);
        }
      }

      document.getElementById("primary-result").innerText = "Sum (" + a + " to " + b + ") = " + sum.toLocaleString();
      document.getElementById("res-sum").innerText = sum.toLocaleString();
      document.getElementById("res-terms").innerText = n.toLocaleString();
      document.getElementById("res-mean").innerText = mean.toFixed(2);
      document.getElementById("res-sum-sq").innerText = sqSum.toLocaleString();
      document.getElementById("res-sum-cube").innerText = cubeSum.toLocaleString();
      document.getElementById("res-formula").innerText = n + " &times; (" + a + " + " + b + ") / 2";

      var steps = "<h4>Step-by-Step Gauss Summation:</h4><ol>";
      steps += "<li><strong>Count Terms:</strong> n = " + b + " - " + a + " + 1 = <strong>" + n + " terms</strong></li>";
      steps += "<li><strong>Average of Bounds:</strong> (" + a + " + " + b + ") / 2 = <strong>" + mean.toFixed(2) + "</strong></li>";
      steps += "<li><strong>Gauss Sum Formula:</strong> S = n &times; (a + b) / 2 = " + n + " &times; " + (a + b) + " / 2 = <strong>" + sum.toLocaleString() + "</strong></li>";
      steps += "<li><strong>Sum of Squares (&sum;k&sup2;):</strong> <strong>" + sqSum.toLocaleString() + "</strong></li>";
      steps += "<li><strong>Sum of Cubes (&sum;k&sup3;):</strong> <strong>" + cubeSum.toLocaleString() + "</strong></li>";
      steps += "</ol>";

      document.getElementById("steps-output").innerHTML = steps;
      document.getElementById("result-box").style.display = "block";
    }

    window.addEventListener("DOMContentLoaded", function() {
      calculateSumOfIntegers();
    });
  </script>
</body>
</html>
"""

def main():
    p5 = os.path.join(BASE_DIR, "factors-calculator.html")
    with open(p5, "w", encoding="utf-8") as f:
        f.write(HTML_FACTORS)
    print(f"Generated: {p5}")

    p6 = os.path.join(BASE_DIR, "sum-of-integers-calculator.html")
    with open(p6, "w", encoding="utf-8") as f:
        f.write(HTML_SUM_OF_INTEGERS)
    print(f"Generated: {p6}")

if __name__ == "__main__":
    main()
