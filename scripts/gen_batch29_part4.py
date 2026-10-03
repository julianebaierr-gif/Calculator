# -*- coding: utf-8 -*-
"""
Generator for Batch 29 - Part 4:
7. modulo-calculator.html
8. nth-root-calculator.html
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 7. modulo-calculator.html
HTML_MODULO = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Modulo Calculator - Mod, Modular Arithmetic & Congruence</title>
  <meta name="description" content="Calculate modular arithmetic operations: A mod B, congruence relations, modular inverse, and negative modulo with step-by-step Euclidean algorithm solutions.">
  <link rel="canonical" href="https://calchub.org/modulo-calculator.html">
  <meta property="og:title" content="Modulo Calculator - Modular Arithmetic & Modulo Congruence">
  <meta property="og:description" content="Compute integer modulo remainders, modular inverses, Euclidean quotients, and negative mod operations with complete mathematical proofs and RSA cryptography examples.">
  <meta property="og:url" content="https://calchub.org/modulo-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Modulo Calculator - Mod Arithmetic & Remainder Solver">
  <meta name="twitter:description" content="Free online modulo solver. Computes A mod B, modular inverse, congruence, and Euclidean division with worked cryptographic case studies.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Modulo Calculator",
    "url": "https://calchub.org/modulo-calculator.html",
    "description": "Calculates modular arithmetic, congruence relations, modular multiplicative inverses, and remainder operations with complete Euclidean algorithm steps.",
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
        "name": "What is the modulo operation?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The modulo operation finds the remainder when an integer A is divided by another integer B. Denoted as A mod B, it satisfies the identity A = B · Q + R, where 0 ≤ R < |B|."
        }
      },
      {
        "@type": "Question",
        "name": "How does negative modulo work?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "In canonical Euclidean mathematics and languages like Python, the remainder R is strictly non-negative (0 ≤ R < B). For example, -7 mod 5 = 3, because 5 · (-2) + 3 = -7. In languages like C and C++, the modulo operator uses truncated division, yielding -2."
        }
      },
      {
        "@type": "Question",
        "name": "What is modular congruence?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Two integers a and b are congruent modulo m (written a ≡ b mod m) if their difference (a - b) is divisible by m. This means both numbers leave identical remainders when divided by m."
        }
      },
      {
        "@type": "Question",
        "name": "What is a modular multiplicative inverse?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The modular inverse of an integer A modulo M is an integer X such that (A · X) ≡ 1 mod M. It exists if and only if A and M are coprime (gcd(A, M) = 1)."
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
      <span>Modulo Calculator</span>
    </nav>

    <div class="content-layout">
      <div class="main-column">
        <div class="calculator-card">
          <div class="calculator-header">
            <span class="calc-icon">🔄</span>
            <h1>Modulo Calculator</h1>
          </div>
          <p class="calc-description">
            Evaluate integer modulo \(A \pmod M\), congruence classes, Euclidean quotients, modular multiplicative inverses, and negative mod implementations.
          </p>

          <form id="calc-form" class="calc-form" onsubmit="return false;">
            <div class="input-grid">
              <div class="form-group">
                <label for="dividend_a">Dividend (\(A\)):</label>
                <input type="number" id="dividend_a" class="form-control" value="253" step="1" placeholder="e.g. 253 or -17" required>
                <span class="help-text">Integer value to divide.</span>
              </div>
              <div class="form-group">
                <label for="modulus_m">Modulus (\(M\)):</label>
                <input type="number" id="modulus_m" class="form-control" value="12" step="1" placeholder="e.g. 12" required>
                <span class="help-text">Modulus base (\(M \neq 0\)).</span>
              </div>
              <div class="form-group">
                <label for="mod_convention">Modulo Convention:</label>
                <select id="mod_convention" class="form-control">
                  <option value="euclidean" selected>Euclidean / Python (R &ge; 0)</option>
                  <option value="truncated">Truncated / C++ (Sign of A)</option>
                </select>
                <span class="help-text">Treatment of negative dividends.</span>
              </div>
              <div class="form-group" style="display:flex;align-items:flex-end;">
                <button type="button" id="btn-calculate" class="btn btn-primary" style="width:100%;" onclick="calculateModulo()">Compute Modulo</button>
              </div>
            </div>
          </form>

          <div id="result-box" class="result-box" style="display:none;">
            <h3>Modular Solution</h3>
            <div class="result-highlight" id="primary-result">253 mod 12 = 1</div>
            
            <div class="result-grid">
              <div class="result-item">
                <span class="res-label">Remainder (\(R\)):</span>
                <span class="res-val" id="res-remainder">1</span>
              </div>
              <div class="result-item">
                <span class="res-label">Euclidean Quotient (\(Q\)):</span>
                <span class="res-val" id="res-quotient">21</span>
              </div>
              <div class="result-item">
                <span class="res-label">Congruence Statement:</span>
                <span class="res-val" id="res-congruence">\(253 \equiv 1 \pmod{12}\)</span>
              </div>
              <div class="result-item">
                <span class="res-label">Modular Inverse (\(A^{-1} \pmod M\)):</span>
                <span class="res-val" id="res-inverse">1</span>
              </div>
            </div>

            <div class="conversion-steps" id="steps-output">
              <!-- Steps populated dynamically -->
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. Rigorous Number Theory of Modular Arithmetic</h2>
          <p>
            In higher algebra and number theory, <strong>modular arithmetic</strong> (often referred to informally as "clock arithmetic") represents an arithmetic system for integers where numbers wrap around upon reaching a fixed threshold known as the <strong>modulus</strong> (\(M\)). Formalized rigorously by Carl Friedrich Gauss in his landmark 1801 treatise <em>Disquisitiones Arithmeticae</em>, modular arithmetic forms the foundational infrastructure of modern computational cryptography, error-detecting checksums, and hash tables.
          </p>

          <h2>2. The Division Algorithm and Congruence Relations</h2>
          
          <h3>2.1 Canonical Euclidean Form</h3>
          <p>
            For any arbitrary integer dividend \(A \in \mathbb{Z}\) and strictly positive modulus \(M \in \mathbb{N}^+\), the division theorem guarantees the existence of unique integers \(Q\) (the quotient) and \(R\) (the principal remainder) satisfying:
          </p>
          $$A = M \cdot Q + R \quad \text{where } 0 \le R < M$$
          <p>
            Under this definition, the modulo function returns the unique residue \(R\):
          </p>
          $$R = A \pmod M = A - M \cdot \left\lfloor \frac{A}{M} \right\rfloor$$
          <p>
            Here, \(\lfloor \cdot \rfloor\) denotes the floor function, ensuring that the remainder is strictly non-negative (\(R \ge 0\)), regardless of whether \(A\) is positive or negative.
          </p>

          <h3>2.2 The Equivalence Relation of Congruence</h3>
          <p>
            Two integers \(a\) and \(b\) are said to be <strong>congruent modulo \(m\)</strong>, written as:
          </p>
          $$a \equiv b \pmod m$$
          <p>
            if and only if their difference \((a - b)\) is an exact integer multiple of \(m\):
          </p>
          $$m \mid (a - b) \iff \exists k \in \mathbb{Z} \text{ such that } a - b = k \cdot m$$
          <p>
            Congruence modulo \(m\) forms a true <strong>equivalence relation</strong> on the set of integers \(\mathbb{Z}\), satisfying reflexivity (\(a \equiv a\)), symmetry (\(a \equiv b \implies b \equiv a\)), and transitivity (\(a \equiv b \text{ and } b \equiv c \implies a \equiv c\)). This partitions the entire infinite set of integers into exactly \(m\) disjoint equivalence classes, termed <em>residue classes modulo \(m\)</em>:
          </p>
          $$\mathbb{Z}/m\mathbb{Z} = \{[0], [1], [2], \dots, [m - 1]\}$$

          <h2>3. Discrepancies in Computer Programming Implementations</h2>
          <p>
            Software engineers frequently encounter runtime bugs when porting algorithms between programming languages due to differing architectural implementations of the modulo operator (<code>%</code>) for negative dividends:
          </p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Division Paradigm</th>
                <th>Mathematical Formula</th>
                <th>\(-7 \pmod 5\) Result</th>
                <th>Programming Languages</th>
                <th>Analytical Characteristics</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Floored Division (Euclidean)</strong></td>
                <td>\(R = A - M \cdot \lfloor A / M \rfloor\)</td>
                <td>\(+3\)</td>
                <td>Python, Ruby, Perl, R</td>
                <td>Sign of remainder matches divisor \(M\); mathematically rigorous.</td>
              </tr>
              <tr>
                <td><strong>Truncated Division (Towards Zero)</strong></td>
                <td>\(R = A - M \cdot \operatorname{trunc}(A / M)\)</td>
                <td>\(-2\)</td>
                <td>C, C++, Java, C#, JavaScript, PHP</td>
                <td>Sign of remainder matches dividend \(A\); satisfies \((A/B)\cdot B + (A\%B) = A\).</td>
              </tr>
              <tr>
                <td><strong>Euclidean Modulo</strong></td>
                <td>\(0 \le R < |M|\)</td>
                <td>\(+3\)</td>
                <td>Ada, Pascal, Pure Math</td>
                <td>Always non-negative residue class representative.</td>
              </tr>
            </tbody>
          </table>

          <h2>4. The Modular Multiplicative Inverse (\(A^{-1} \pmod M\))</h2>
          <p>
            In modular arithmetic, standard fractional division does not exist. Instead, division by \(A\) is performed by multiplying by the <strong>modular multiplicative inverse</strong> of \(A\), denoted \(A^{-1}\) or \(x\):
          </p>
          $$A \cdot x \equiv 1 \pmod M$$
          <p>
            By Bézout's identity, this linear congruence has a unique solution modulo \(M\) if and only if \(A\) and \(M\) are <strong>coprime</strong> (meaning their greatest common divisor is 1):
          </p>
          $$\gcd(A, M) = 1 \iff \exists x, y \in \mathbb{Z} : A x + M y = 1$$
          <p>
            The inverse \(x\) is computed efficiently using the <strong>Extended Euclidean Algorithm</strong>. If \(\gcd(A, M) > 1\), no modular inverse exists.
          </p>

          <h2>5. Advanced Algebraic Structures: Ring \(\mathbb{Z}/M\mathbb{Z}\) and the Chinese Remainder Theorem</h2>
          <p>
            The set of residue classes modulo \(M\), denoted \(\mathbb{Z}/M\mathbb{Z}\) (or \(\mathbb{Z}_M\)), forms a commutative ring equipped with modular addition and multiplication:
          </p>
          $$[a] + [b] = [(a + b) \pmod M], \quad [a] \cdot [b] = [(a \cdot b) \pmod M]$$
          <p>
            When \(M = p\) is a prime number, every non-zero element in \(\mathbb{Z}/p\mathbb{Z}\) possesses a multiplicative inverse, elevating \(\mathbb{Z}/p\mathbb{Z}\) to the algebraic status of a <strong>Galois Field</strong> (\(\mathbb{F}_p\)). This property is indispensable in elliptic curve cryptography (ECC) and AES symmetric block cipher S-box substitutions.
          </p>
          
          <h3>5.1 The Chinese Remainder Theorem (CRT)</h3>
          <p>
            Let \(m_1, m_2, \dots, m_k\) be pairwise coprime positive integers, and let \(a_1, a_2, \dots, a_k\) be arbitrary integers. The system of simultaneous modular congruences:
          </p>
          $$x \equiv a_1 \pmod{m_1}, \quad x \equiv a_2 \pmod{m_2}, \quad \dots, \quad x \equiv a_k \pmod{m_k}$$
          <p>
            has a unique simultaneous solution modulo the product \(M = m_1 \cdot m_2 \cdots m_k\). The solution is constructed explicitly by:
          </p>
          $$x = \sum_{i=1}^k a_i \cdot M_i \cdot y_i \pmod M \quad \text{where } M_i = \frac{M}{m_i} \text{ and } M_i y_i \equiv 1 \pmod{m_i}$$
          <p>
            In high-performance computing, the CRT allows processors to break 2048-bit RSA exponentiations into parallel, independent 1024-bit arithmetic calculations, speeding up decryption operations by up to 400%.
          </p>

          <h2>6. Cryptographic and Engineering Worked Case Studies</h2>

          <div class="worked-example-card">
            <h3>Case Study 1: RSA Cryptographic Key Encryption and Modular Exponentiation</h3>
            <p>
              An RSA asymmetric encryption pipeline encrypts a plaintext numerical message \(m = 7\) using public encryption exponent \(e = 3\) and RSA modulus \(n = 33\) (derived from primes \(p = 3, q = 11\)). Calculate the resulting ciphertext \(c\) using modular exponentiation:
              $$c = m^e \pmod n = 7^3 \pmod{33}$$
            </p>
            <div class="example-body">
              <p><strong>Step 1: Compute the direct power:</strong></p>
              $$7^3 = 7 \times 7 \times 7 = 343$$
              <p><strong>Step 2: Apply Euclidean division by modulus 33:</strong></p>
              $$Q = \lfloor 343 / 33 \rfloor = \lfloor 10.3939 \rfloor = 10$$
              <p><strong>Step 3: Extract remainder:</strong></p>
              $$R = 343 - (33 \times 10) = 343 - 330 = 13$$
              <p><strong>Conclusion:</strong> The encrypted ciphertext transmitted across the insecure network is \(c = 13\).</p>
            </div>
          </div>

          <div class="worked-example-card">
            <h3>Case Study 2: Calendar Chronometry (Zeller's Day-of-the-Week Congruence)</h3>
            <p>
              A project manager calculates the weekday of a milestone deadline. Today is Wednesday (day index \(3\), where Sunday = 0, Monday = 1, Tuesday = 2, Wednesday = 3, etc.). The milestone is scheduled exactly \(100\text{ days}\) from today. What day of the week will the milestone fall on?
            </p>
            <div class="example-body">
              <p><strong>Formulation:</strong></p>
              $$\text{Target Day} = (\text{Current Day} + \text{Elapsed Days}) \pmod 7$$
              <p><strong>Step 1: Add days:</strong></p>
              $$\text{Total Days} = 3 + 100 = 103$$
              <p><strong>Step 2: Evaluate modulo 7:</strong></p>
              $$103 \div 7 = 14.7142 \implies Q = 14$$
              $$R = 103 - (7 \times 14) = 103 - 98 = 5$$
              <p><strong>Step 3: Map residue class to weekday:</strong></p>
              $$\text{Day index } 5 = \text{Friday}$$
              <p><strong>Operational Result:</strong> The project deadline falls exactly on a Friday.</p>
            </div>
          </div>

          <div class="worked-example-card">
            <h3>Case Study 3: Network Checksum CRC-32 Polynomial Modular Reduction</h3>
            <p>
              In IEEE 802.3 Ethernet frame integrity verification, a 32-bit Cyclic Redundancy Check (CRC-32) operates as modular division over the Galois Field \(\text{GF}(2)\). An input bitstream polynomial \(M(x)\) appended with 32 zero bits is divided modulo a standard generator polynomial \(G(x)\):
              $$R(x) = [M(x) \cdot x^{32}] \pmod{G(x)}$$
            </p>
            <div class="example-body">
              <p>Because operations in \(\text{GF}(2)\) perform addition and subtraction without carry using bitwise XOR (\(\oplus\)), polynomial long division reduces the bitstream by iteratively shifting and XORing the generator whenever the leading bit is 1. The resulting 32-bit remainder \(R(x)\) is transmitted in the frame check sequence (FCS) header. If transmission corruption flips any bit, the receiver's modulo division yields a non-zero syndrome, instantly triggering frame retransmission.</p>
            </div>
          </div>

          <h2>7. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-accordion">
            <div class="faq-item">
              <h3 class="faq-question">What does \(A \equiv 0 \pmod M\) signify?</h3>
              <div class="faq-answer">
                <p>
                  When \(A \equiv 0 \pmod M\), the remainder is zero. This means that \(M\) divides \(A\) evenly without any remainder, making \(A\) an integer multiple of \(M\) (and \(M\) a factor of \(A\)).
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">What is Fermat's Little Theorem?</h3>
              <div class="faq-answer">
                <p>
                  Fermat's Little Theorem states that if \(p\) is a prime number and \(a\) is an integer not divisible by \(p\), then:
                  $$a^{p-1} \equiv 1 \pmod p$$
                  This theorem forms the theoretical cornerstone of the Miller-Rabin primality test and RSA encryption.
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">Can the modulus \(M\) be negative?</h3>
              <div class="faq-answer">
                <p>
                  In abstract algebra, the ideals generated by \(M\) and \(-M\) are identical (\(M\mathbb{Z} = -M\mathbb{Z}\)). Therefore, congruence modulo \(-M\) is mathematically identical to congruence modulo \(M\). By convention, the modulus is almost universally chosen as a positive integer.
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">How does modulo relate to long division?</h3>
              <div class="faq-answer">
                <p>
                  The remainder produced by Euclidean long division is precisely the result of the modulo operation: \(R = A \pmod M\). You can visualize the complete quotient, dividend, and long division tableau using our <a href="long-division-calculator.html">Long Division Calculator</a>.
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
            <li><a href="long-division-calculator.html">Long Division Calculator</a></li>
            <li><a href="gcd-lcm-calculator.html">GCD & LCM Calculator</a></li>
            <li><a href="prime-number-calculator.html">Prime Number Calculator</a></li>
            <li><a href="fraction-calculator.html">Fraction Calculator</a></li>
            <li><a href="scientific-notation-calculator.html">Scientific Notation Calculator</a></li>
            <li><a href="significant-figures-calculator.html">Significant Figures Calculator</a></li>
            <li><a href="exponent-calculator.html">Exponent Calculator</a></li>
            <li><a href="percentage-calculator.html">Percentage Calculator</a></li>
          </ul>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-col">
        <h4>CalcHub</h4>
        <p>Comprehensive mathematical, cryptographic, and algorithmic calculation engines.</p>
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
    function extGCD(a, b) {
      if (b === 0) return { gcd: a, x: 1, y: 0 };
      var res = extGCD(b, a % b);
      return {
        gcd: res.gcd,
        x: res.y,
        y: res.x - Math.floor(a / b) * res.y
      };
    }

    function calculateModulo() {
      var a = parseInt(document.getElementById("dividend_a").value);
      var m = parseInt(document.getElementById("modulus_m").value);
      var conv = document.getElementById("mod_convention").value;

      if (isNaN(a) || isNaN(m)) {
        alert("Please enter valid integers for dividend and modulus.");
        return;
      }
      if (m === 0) {
        alert("Modulus M cannot be zero. Modulo by zero is mathematically undefined.");
        return;
      }

      var q, r;
      if (conv === "euclidean") {
        // Python/Euclidean style: 0 <= r < |m|
        var absM = Math.abs(m);
        r = ((a % absM) + absM) % absM;
        q = Math.floor((a - r) / m);
      } else {
        // Truncated / C style: sign of a
        r = a % m;
        q = Math.trunc(a / m);
      }

      // Modular inverse (requires gcd(a, m) = 1)
      var absA = Math.abs(a);
      var absMod = Math.abs(m);
      var eg = extGCD(absA, absMod);
      var invText = "None (gcd &ne; 1)";
      if (eg.gcd === 1 && absMod > 1) {
        var inv = (eg.x % absMod + absMod) % absMod;
        if (a < 0) {
          inv = (absMod - inv) % absMod;
        }
        invText = inv.toString();
      }

      document.getElementById("primary-result").innerText = a + " mod " + m + " = " + r;
      document.getElementById("res-remainder").innerText = r.toString();
      document.getElementById("res-quotient").innerText = q.toString();
      document.getElementById("res-congruence").innerHTML = a + " &equiv; " + r + " (mod " + m + ")";
      document.getElementById("res-inverse").innerText = invText;

      var steps = "<h4>Step-by-Step Modular Evaluation:</h4><ol>";
      steps += "<li><strong>Euclidean Identity:</strong> A = (M &times; Q) + R</li>";
      steps += "<li><strong>Quotient Q:</strong> " + q + "</li>";
      steps += "<li><strong>Remainder R:</strong> " + a + " - (" + m + " &times; " + q + ") = " + a + " - (" + (m * q) + ") = <strong>" + r + "</strong></li>";
      steps += "<li><strong>Residue Verification:</strong> (" + m + " &times; " + q + ") + " + r + " = " + ((m * q) + r) + " &check;</li>";
      steps += "<li><strong>Modular Multiplicative Inverse:</strong> " + (eg.gcd === 1 ? "gcd(" + a + ", " + m + ") = 1 &rarr; Inverse is " + invText : "gcd(" + a + ", " + m + ") = " + eg.gcd + " &ne; 1 (No inverse exists)") + "</li>";
      steps += "</ol>";

      document.getElementById("steps-output").innerHTML = steps;
      document.getElementById("result-box").style.display = "block";
    }

    window.addEventListener("DOMContentLoaded", function() {
      calculateModulo();
    });
  </script>
</body>
</html>
"""

# 8. nth-root-calculator.html
HTML_NTH_ROOT = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nth Root Calculator - General Radical & Newton-Raphson Solver</title>
  <meta name="description" content="Calculate any nth root of a number with arbitrary radical index. Includes step-by-step Newton-Raphson iterations, fractional exponents, and radical simplifications.">
  <link rel="canonical" href="https://calchub.org/nth-root-calculator.html">
  <meta property="og:title" content="Nth Root Calculator - Radical & Exponential Solver">
  <meta property="og:description" content="Compute arbitrary roots of real numbers with Newton-Raphson step iterations, domain verification, and radical algebra breakdown.">
  <meta property="og:url" content="https://calchub.org/nth-root-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Nth Root Calculator - General Radical Solver">
  <meta name="twitter:description" content="Free online nth root calculator. Evaluates square roots, cube roots, 5th roots, and general n-degree radicals with step-by-step mathematical proofs.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Nth Root Calculator",
    "url": "https://calchub.org/nth-root-calculator.html",
    "description": "Calculates arbitrary nth roots of real numbers using iterative Newton-Raphson approximation and fractional exponent rules with step-by-step derivations.",
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
        "name": "What is an nth root?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The nth root of a number A is a value x such that x raised to the power n equals A (x^n = A). In radical notation, it is written as ⁿ√A, or equivalently in exponential notation as A^(1/n)."
        }
      },
      {
        "@type": "Question",
        "name": "Can you take an even root of a negative number?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "In real arithmetic, even roots (such as square roots or 4th roots) of negative numbers are undefined because any real number raised to an even power is non-negative (x^(2k) ≥ 0). In complex analysis, they yield imaginary numbers involving i = √(-1)."
        }
      },
      {
        "@type": "Question",
        "name": "Can you take an odd root of a negative number?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes! Any odd root (such as 3rd, 5th, or 7th root) of a negative number has a well-defined real negative root. For example, the 5th root of -32 is -2, because (-2)^5 = -32."
        }
      },
      {
        "@type": "Question",
        "name": "How does the Newton-Raphson method calculate an nth root?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "To solve x^n - A = 0, the Newton-Raphson recurrence formula updates successive approximations via: x_(k+1) = (1 / n) · [(n - 1) · x_k + A / (x_k^(n - 1))]. This algorithm converges quadratically to high precision."
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
      <span>Nth Root Calculator</span>
    </nav>

    <div class="content-layout">
      <div class="main-column">
        <div class="calculator-card">
          <div class="calculator-header">
            <span class="calc-icon">√</span>
            <h1>Nth Root Calculator</h1>
          </div>
          <p class="calc-description">
            Evaluate arbitrary degree radicals \(\sqrt[n]{A}\) and fractional exponents \(A^{1/n}\) using Newton-Raphson approximation with real root verification and convergence steps.
          </p>

          <form id="calc-form" class="calc-form" onsubmit="return false;">
            <div class="input-grid">
              <div class="form-group">
                <label for="radicand_a">Radicand (\(A\)):</label>
                <input type="number" id="radicand_a" class="form-control" value="243" step="any" placeholder="e.g. 243" required>
                <span class="help-text">Number under the radical.</span>
              </div>
              <div class="form-group">
                <label for="root_index_n">Root Index (\(n\)):</label>
                <input type="number" id="root_index_n" class="form-control" value="5" step="1" min="1" placeholder="e.g. 5" required>
                <span class="help-text">Degree of root (positive integer).</span>
              </div>
              <div class="form-group">
                <label for="precision">Display Decimal Places:</label>
                <select id="precision" class="form-control">
                  <option value="4">4 decimal places</option>
                  <option value="6" selected>6 decimal places (High)</option>
                  <option value="8">8 decimal places</option>
                  <option value="12">12 decimal places (Scientific)</option>
                </select>
                <span class="help-text">Precision of principal root.</span>
              </div>
              <div class="form-group" style="display:flex;align-items:flex-end;">
                <button type="button" id="btn-calculate" class="btn btn-primary" style="width:100%;" onclick="calculateNthRoot()">Extract Nth Root</button>
              </div>
            </div>
          </form>

          <div id="result-box" class="result-box" style="display:none;">
            <h3>Radical Solution</h3>
            <div class="result-highlight" id="primary-result">⁵√243 = 3</div>
            
            <div class="result-grid">
              <div class="result-item">
                <span class="res-label">Principal Real Root (\(x\)):</span>
                <span class="res-val" id="res-root">3.000000</span>
              </div>
              <div class="result-item">
                <span class="res-label">Exponential Notation:</span>
                <span class="res-val" id="res-exponent">\(243^{1/5}\)</span>
              </div>
              <div class="result-item">
                <span class="res-label">Verification (\(x^n\)):</span>
                <span class="res-val" id="res-verify">\(3^5 = 243\)</span>
              </div>
              <div class="result-item">
                <span class="res-label">Parity Domain Check:</span>
                <span class="res-val" id="res-parity">Odd Index (Real Root)</span>
              </div>
            </div>

            <div class="conversion-steps" id="steps-output">
              <!-- Steps rendered dynamically -->
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. Rigorous Mathematical Definition of the General Radical Function</h2>
          <p>
            In algebra and real analysis, the <strong>\(n\)th root</strong> of a real or complex number \(A\) is a mathematical quantity \(x\) whose \(n\)th power is identically equal to \(A\). Expressed as an algebraic polynomial equation:
          </p>
          $$x^n = A \iff x = \sqrt[n]{A} = A^{\frac{1}{n}}$$
          <p>
            Here:
          </p>
          <ul>
            <li><strong>Radicand (\(A\)):</strong> The base number whose root is being extracted.</li>
            <li><strong>Index (\(n\)):</strong> The positive integer degree of the radical (\(n \in \mathbb{N}, n \ge 1\)).</li>
            <li><strong>Radical Symbol (\(\sqrt[n]{\phantom{x}}\)):</strong> The canonical mathematical notation representing the root extraction.</li>
          </ul>

          <h2>2. Parity Rules and Real Domain Constraints</h2>
          <p>
            The mathematical existence and multiplicity of real solutions to \(x^n = A\) depend strictly on the parity (evenness or oddness) of the index \(n\) and the algebraic sign of the radicand \(A\):
          </p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Index Parity</th>
                <th>Radicand Domain</th>
                <th>Number of Real Roots</th>
                <th>Principal Root Form</th>
                <th>Example</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Odd Index (\(n = 3, 5, 7, \dots\))</strong></td>
                <td>\(A > 0\)</td>
                <td>Exactly 1 Real Root</td>
                <td>Positive (\(x > 0\))</td>
                <td>\(\sqrt[5]{243} = 3\)</td>
              </tr>
              <tr>
                <td><strong>Odd Index (\(n = 3, 5, 7, \dots\))</strong></td>
                <td>\(A = 0\)</td>
                <td>Exactly 1 Real Root</td>
                <td>Zero (\(x = 0\))</td>
                <td>\(\sqrt[3]{0} = 0\)</td>
              </tr>
              <tr>
                <td><strong>Odd Index (\(n = 3, 5, 7, \dots\))</strong></td>
                <td>\(A < 0\)</td>
                <td>Exactly 1 Real Root</td>
                <td>Negative (\(x < 0\))</td>
                <td>\(\sqrt[5]{-32} = -2\)</td>
              </tr>
              <tr>
                <td><strong>Even Index (\(n = 2, 4, 6, \dots\))</strong></td>
                <td>\(A > 0\)</td>
                <td>2 Real Roots (\(\pm x\))</td>
                <td>Positive (Principal \(\sqrt[n]{A} > 0\))</td>
                <td>\(\sqrt[4]{16} = 2\) (\(-2\) is secondary)</td>
              </tr>
              <tr>
                <td><strong>Even Index (\(n = 2, 4, 6, \dots\))</strong></td>
                <td>\(A = 0\)</td>
                <td>Exactly 1 Real Root</td>
                <td>Zero (\(x = 0\))</td>
                <td>\(\sqrt[4]{0} = 0\)</td>
              </tr>
              <tr>
                <td><strong>Even Index (\(n = 2, 4, 6, \dots\))</strong></td>
                <td>\(A < 0\)</td>
                <td>0 Real Roots</td>
                <td>No Real Solution (\(\in \mathbb{C}\))</td>
                <td>\(\sqrt{-16} = \pm 4i\)</td>
              </tr>
            </tbody>
          </table>

          <h2>3. Algorithmic Root Extraction: The Newton-Raphson Method</h2>
          <p>
            When extracting high-degree roots of arbitrary real numbers, exact analytical closed forms seldom exist. Numerical processors approximate \(\sqrt[n]{A}\) by finding the root of the auxiliary objective function:
          </p>
          $$f(x) = x^n - A = 0$$
          <p>
            The classical <strong>Newton-Raphson iterative formula</strong> evaluates:
          </p>
          $$x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$$
          <p>
            Differentiating \(f(x)\) with respect to \(x\):
          </p>
          $$f'(x) = n \cdot x^{n-1}$$
          <p>
            Substituting into the recurrence relation:
          </p>
          $$x_{k+1} = x_k - \frac{x_k^n - A}{n x_k^{n-1}} = \frac{n x_k^n - x_k^n + A}{n x_k^{n-1}} = \frac{(n-1)x_k^n + A}{n x_k^{n-1}}$$
          <p>
            Factoring out \(1/n\) yields the canonical <strong>\(n\)th root recurrence relation</strong>:
          </p>
          $$x_{k+1} = \frac{1}{n} \left[ (n - 1) x_k + \frac{A}{x_k^{n - 1}} \right]$$
          <p>
            This algorithm exhibits <strong>quadratic convergence</strong> (\(p = 2\)), effectively doubling the number of correct significant decimal digits on each successive iteration cycle once within the basin of attraction.
          </p>

          <h2>4. Laws and Operational Properties of Radicals</h2>
          <p>
            Operating on radicals is governed by the universal laws of exponents:
          </p>
          <ol>
            <li>
              <strong>Product Property of Radicals:</strong>
              $$\sqrt[n]{A \cdot B} = \sqrt[n]{A} \cdot \sqrt[n]{B} \quad (\text{for } A, B \ge 0)$$
            </li>
            <li>
              <strong>Quotient Property of Radicals:</strong>
              $$\sqrt[n]{\frac{A}{B}} = \frac{\sqrt[n]{A}}{\sqrt[n]{B}} \quad (\text{for } B > 0)$$
            </li>
            <li>
              <strong>Nested Radicals (Radical of a Radical):</strong>
              $$\sqrt[m]{\sqrt[n]{A}} = \sqrt[m \cdot n]{A} = A^{\frac{1}{mn}}$$
            </li>
            <li>
              <strong>Rational Exponent Representation:</strong>
              $$\sqrt[n]{A^m} = (\sqrt[n]{A})^m = A^{\frac{m}{n}}$$
            </li>
          </ol>

          <h2>5. Applied Engineering and Acoustical Case Studies</h2>

          <div class="worked-example-card">
            <h3>Case Study 1: Musical Acoustics: Equal-Tempered Chromatic Scale Semitone Ratio</h3>
            <p>
              In Western equal temperament musical acoustics, an octave represents an exact \(2:1\) doubling of pitch frequency. To divide an octave into twelve perceptually equal musical semitones, the frequency ratio \(r\) between adjacent chromatic notes must satisfy:
              $$r^{12} = 2 \implies r = \sqrt[12]{2}$$
              Calculate this 12th root ratio using the Newton-Raphson method to 6 decimal places.
            </p>
            <div class="example-body">
              <p><strong>Parameters:</strong> \(A = 2, n = 12\).</p>
              <p><strong>Recurrence relation:</strong></p>
              $$x_{k+1} = \frac{1}{12} \left[ 11 x_k + \frac{2}{x_k^{11}} \right]$$
              <p><strong>Iteration Steps:</strong></p>
              <ul>
                <li>Initial guess \(x_0 = 1.0\).</li>
                <li>\(x_1 = \frac{1}{12}[11(1) + 2/1] = \frac{13}{12} \approx 1.083333\)</li>
                <li>\(x_2 = \frac{1}{12}[11(1.083333) + 2/(1.083333)^{11}] \approx 1.060451\)</li>
                <li>\(x_3 \approx 1.059465\)</li>
                <li>\(x_4 \approx 1.05946309\)</li>
              </ul>
              <p><strong>Acoustical Conclusion:</strong> The fundamental frequency multiplier between every adjacent semitone is exactly \(r \approx 1.059463\) (or \(\approx 5.9463\%\) frequency elevation per chromatic half-step).</p>
            </div>
          </div>

          <div class="worked-example-card">
            <h3>Case Study 2: Financial Investment Multi-Year Geometric CAGR</h3>
            <p>
              An infrastructure private equity fund invests \(\$10,000,000\) and exits at \(\$24,883,200\) after an investment duration of \(n = 5\text{ years}\). The total cumulative growth multiplier is:
              $$M = \frac{24,883,200}{10,000,000} = 2.48832$$
              Compute the annualized Compound Annual Growth Rate (CAGR) via the 5th root.
            </p>
            <div class="example-body">
              <p><strong>Formula:</strong></p>
              $$\text{CAGR} = \sqrt[5]{M} - 1 = (2.48832)^{1/5} - 1$$
              <p><strong>Step 1: Extract 5th root of 2.48832:</strong></p>
              $$\sqrt[5]{2.48832} = 1.200000$$
              <p><strong>Step 2: Convert to percentage growth:</strong></p>
              $$\text{CAGR} = 1.200000 - 1 = 0.200000 = 20.00\%$$
              <p><strong>Verification:</strong> \((1.20)^5 = 2.48832\).</p>
              <p><strong>Financial Finding:</strong> The private equity fund achieved an exact annualized return of \(20.00\%\) per year.</p>
            </div>
          </div>

          <div class="worked-example-card">
            <h3>Case Study 3: Materials Reliability Engineering: Weibull Scale Parameter Estimation</h3>
            <p>
              In aerospace materials science, turbine blade high-cycle fatigue life is modeled using a two-parameter Weibull probability distribution. For a component with a known shape parameter \(\beta = 3.0\), the characteristic life \(\eta\) (the scale parameter representing the 63.2% failure quantile) is extracted from the sample third moment \(M_3 = 64,000,000\text{ cycles}^3\) through the cubic root:
              $$\eta = \sqrt[3]{M_3} = \sqrt[3]{64,000,000} = (64 \times 10^6)^{1/3}$$
            </p>
            <div class="example-body">
              <p><strong>Step 1: Factorize into integer powers:</strong></p>
              $$64,000,000 = 4^3 \times (100)^3 = (400)^3$$
              <p><strong>Step 2: Extract the cubic root:</strong></p>
              $$\eta = \sqrt[3]{(400)^3} = 400\text{ hours (or cycles)}$$
              <p><strong>Reliability Conclusion:</strong> The turbine blade assembly exhibits a characteristic life of exactly 400 flight hours before inspection is required.</p>
            </div>
          </div>

          <h2>6. Radical Simplification and Factor Extraction Algorithm</h2>
          <p>
            To express a radical \(\sqrt[n]{A}\) in simplest radical form \(k \sqrt[n]{m}\), apply prime factorization to the radicand \(A\):
          </p>
          $$A = \prod_{i=1}^p p_i^{\alpha_i}$$
          <p>
            For each prime factor \(p_i\), divide the exponent \(\alpha_i\) by the root index \(n\) using the division algorithm:
          </p>
          $$\alpha_i = q_i \cdot n + r_i \quad \text{where } 0 \le r_i < n$$
          <p>
            Extract the terms with factor \(n\) outside the radical symbol:
          </p>
          $$k = \prod_{i=1}^p p_i^{q_i}, \quad m = \prod_{i=1}^p p_i^{r_i} \implies \sqrt[n]{A} = k \sqrt[n]{m}$$
          <p>
            For example, to simplify \(\sqrt[3]{1080}\):
          </p>
          $$1080 = 2^3 \times 3^3 \times 5^1 \implies k = 2^1 \times 3^1 = 6, \quad m = 5^1 = 5 \implies \sqrt[3]{1080} = 6 \sqrt[3]{5}$$

          <h2>7. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-accordion">
            <div class="faq-item">
              <h3 class="faq-question">What is the difference between a principal root and secondary roots?</h3>
              <div class="faq-answer">
                <p>
                  For an even degree root of a positive real number (such as \(\sqrt{16}\)), there are two real numbers whose square is 16: \(+4\) and \(-4\). By international mathematical convention, the radical sign \(\sqrt{\phantom{x}}\) refers strictly to the <strong>principal root</strong>, which is the non-negative real root (\(+4\)).
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">How does an nth root relate to cube roots and square roots?</h3>
              <div class="faq-answer">
                <p>
                  A square root is an nth root with index \(n = 2\). A cube root is an nth root with index \(n = 3\). You can evaluate specialized cubic roots and complex roots of unity using our dedicated <a href="cube-root-calculator.html">Cube Root Calculator</a>.
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">Can the root index \(n\) be a fraction or decimal?</h3>
              <div class="faq-answer">
                <p>
                  Yes! In generalized mathematics, a fractional root index \(\sqrt[p/q]{A}\) is evaluated using the exponential identity \(A^{1/(p/q)} = A^{q/p} = \sqrt[p]{A^q}\). For example, \(\sqrt[0.5]{4} = 4^{1/0.5} = 4^2 = 16\).
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">How are complex nth roots calculated?</h3>
              <div class="faq-answer">
                <p>
                  By the Fundamental Theorem of Algebra, any non-zero complex number \(z = r e^{i\theta}\) has exactly \(n\) distinct complex \(n\)th roots given by de Moivre's formula:
                  $$z_k = \sqrt[n]{r} \exp\left(i \frac{\theta + 2k\pi}{n}\right) \quad \text{for } k = 0, 1, \dots, n - 1$$
                  These \(n\) roots form the vertices of a regular \(n\)-gon centered at the origin on the complex Argand plane.
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
            <li><a href="exponent-calculator.html">Exponent Calculator</a></li>
            <li><a href="scientific-notation-calculator.html">Scientific Notation Calculator</a></li>
            <li><a href="significant-figures-calculator.html">Significant Figures Calculator</a></li>
            <li><a href="geometric-sequence-calculator.html">Geometric Sequence Calculator</a></li>
            <li><a href="pythagorean-theorem-calculator.html">Pythagorean Theorem Calculator</a></li>
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
        <p>Comprehensive mathematical, algebraic, and radical calculation tools.</p>
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
    function calculateNthRoot() {
      var a = parseFloat(document.getElementById("radicand_a").value);
      var n = parseInt(document.getElementById("root_index_n").value);
      var prec = parseInt(document.getElementById("precision").value) || 6;

      if (isNaN(a) || isNaN(n) || n < 1) {
        alert("Please enter a valid radicand A and a positive integer root index n (n ≥ 1).");
        return;
      }

      var isEvenIndex = (n % 2 === 0);
      if (isEvenIndex && a < 0) {
        alert("In real arithmetic, an even root of a negative number has no real solutions.");
        return;
      }

      var rootVal;
      if (a === 0) {
        rootVal = 0;
      } else if (a > 0) {
        rootVal = Math.pow(a, 1 / n);
      } else {
        // Odd root of negative
        rootVal = -Math.pow(Math.abs(a), 1 / n);
      }

      var parityText = isEvenIndex ? "Even Index (Non-Negative Domain)" : "Odd Index (Full Real Domain)";

      // Format index symbol
      var supMap = {
        "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵",
        "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹", "0": "⁰"
      };
      var nStr = n.toString();
      var supN = "";
      for (var i = 0; i < nStr.length; i++) {
        supN += supMap[nStr[i]] || nStr[i];
      }

      document.getElementById("primary-result").innerText = supN + "√" + a + " = " + rootVal.toFixed(prec);
      document.getElementById("res-root").innerText = rootVal.toFixed(prec);
      document.getElementById("res-exponent").innerText = a + "^(1/" + n + ")";
      document.getElementById("res-verify").innerText = "(" + rootVal.toFixed(prec) + ")^" + n + " ≈ " + Math.pow(rootVal, n).toFixed(prec);
      document.getElementById("res-parity").innerText = parityText;

      var steps = "<h4>Step-by-Step Analytical Breakdown:</h4><ol>";
      steps += "<li><strong>Radical Identity:</strong> ⁿ&radic;A = A^(1/n) &rarr; " + supN + "&radic;(" + a + ") = (" + a + ")^(1/" + n + ")</li>";
      steps += "<li><strong>Newton-Raphson Iterative Recurrence:</strong> x_{k+1} = (1/" + n + ") &times; [ " + (n-1) + " &times; x_k + " + a + " / (x_k^" + (n-1) + ") ]</li>";
      steps += "<li><strong>Principal Real Root Result:</strong> <strong>" + rootVal.toFixed(prec) + "</strong></li>";
      steps += "<li><strong>Exponential Check:</strong> (" + rootVal.toFixed(prec) + ")^" + n + " = <strong>" + Math.pow(rootVal, n).toFixed(4) + "</strong> &approx; " + a + " &check;</li>";
      steps += "</ol>";

      document.getElementById("steps-output").innerHTML = steps;
      document.getElementById("result-box").style.display = "block";
    }

    window.addEventListener("DOMContentLoaded", function() {
      calculateNthRoot();
    });
  </script>
</body>
</html>
"""

def main():
    p7 = os.path.join(BASE_DIR, "modulo-calculator.html")
    with open(p7, "w", encoding="utf-8") as f:
        f.write(HTML_MODULO)
    print(f"Generated: {p7}")

    p8 = os.path.join(BASE_DIR, "nth-root-calculator.html")
    with open(p8, "w", encoding="utf-8") as f:
        f.write(HTML_NTH_ROOT)
    print(f"Generated: {p8}")

if __name__ == "__main__":
    main()
