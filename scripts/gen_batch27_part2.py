import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 1. GCD & LCM CALCULATOR
# -------------------------------------------------------------
gcd_lcm_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GCD and LCM Calculator — Greatest Common Divisor & Least Common Multiple | CalcHub</title>
  <meta name="description" content="Calculate the Greatest Common Divisor (GCD/GCF) and Least Common Multiple (LCM) with step-by-step Euclidean algorithm, prime factorization, and Bézout identity breakdown.">
  <meta name="keywords" content="gcd calculator, lcm calculator, greatest common divisor, least common multiple, gcf calculator, euclidean algorithm, prime factorization, coprime numbers, bezout identity">
  <meta name="author" content="CalcHub Discrete Mathematics & Number Theory Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/gcd-lcm-calculator.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="GCD and LCM Calculator — Greatest Common Divisor & Least Common Multiple | CalcHub">
  <meta property="og:description" content="Calculate GCD and LCM with step-by-step Euclidean algorithm, prime factorization trees, and mechanical gear sync applications.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/gcd-lcm-calculator.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/gcd-lcm-calculator.html#app",
      "name": "GCD and LCM Multi-Algorithm Engine",
      "url": "https://calchub.org/gcd-lcm-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "High-precision number theory calculator for computing Greatest Common Divisor (GCD/HCF) and Least Common Multiple (LCM) with Euclidean reduction steps and prime factorization."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Math & Engineering Calculators", "item": "https://calchub.org/math.html"},
        {"@type": "ListItem", "position": 3, "name": "GCD & LCM Calculator", "item": "https://calchub.org/gcd-lcm-calculator.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the mathematical difference between GCD (Greatest Common Divisor) and LCM (Least Common Multiple)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The Greatest Common Divisor (GCD), also known as the Greatest Common Factor (GCF) or Highest Common Factor (HCF), is the largest positive integer that divides two or more given integers without leaving a remainder. In contrast, the Least Common Multiple (LCM) is the smallest positive non-zero integer that is an exact multiple of all given numbers. In terms of prime factorizations, the GCD takes the minimum power of all common prime factors, whereas the LCM takes the maximum power across all prime factors present in either number."
          }
        },
        {
          "@type": "Question",
          "name": "How does the Euclidean Algorithm compute GCD in logarithmic time?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The Euclidean Algorithm operates on the fundamental lemma that gcd(a, b) = gcd(b, a mod b). By repeatedly taking the remainder of division until the remainder equals zero, the divisor at that final step is the exact GCD. Lamé's Theorem proves that the number of division steps required never exceeds 5 times the number of decimal digits of the smaller number, giving it an asymptotic computational complexity of O(log(min(a, b))), making it exponentially faster than brute-force factor checking."
          }
        },
        {
          "@type": "Question",
          "name": "What is the relationship between GCD, LCM, and the product of two integers?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "For any two positive integers a and b, their product is exactly equal to the product of their GCD and their LCM: a * b = gcd(a, b) * lcm(a, b). This fundamental identity allows for the instantaneous derivation of the LCM once the GCD is known: lcm(a, b) = (a * b) / gcd(a, b). Note that this simple two-number product identity does not generalize directly to three or more numbers without applying inclusion-exclusion principles."
          }
        },
        {
          "@type": "Question",
          "name": "Where are GCD and LCM applied in mechanical engineering and computer science?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In mechanical engineering, GCD and LCM determine gear train synchronicity and wear patterns. If two meshing gears have coprime tooth counts (GCD = 1), every tooth of gear A contacts every tooth of gear B before repeating, maximizing wear distribution. The LCM defines the exact number of teeth that must pass before the exact same pair of teeth mesh again. In computer science, GCD algorithms underpin RSA asymmetric cryptography key generation via the Extended Euclidean Algorithm to calculate modular multiplicative inverses."
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
            <div class="badge-tag">Discrete Mathematics & Number Theory</div>
            <h1 class="tool-title">GCD and LCM Calculator</h1>
            <p class="tool-subtitle">Compute the Greatest Common Divisor (GCD/HCF) and Least Common Multiple (LCM) with Euclidean step-by-step reduction, prime factor analysis, and algebraic verification.</p>
          </header>

          <section class="calculator-card" aria-label="GCD and LCM Calculator">
            <div class="calc-grid">
              <div class="input-group">
                <label for="gcdNum1" class="input-label">First Integer (A)</label>
                <input type="number" id="gcdNum1" class="calc-input" value="48" step="1" min="1">
              </div>

              <div class="input-group">
                <label for="gcdNum2" class="input-label">Second Integer (B)</label>
                <input type="number" id="gcdNum2" class="calc-input" value="180" step="1" min="1">
              </div>
            </div>

            <div class="input-group" style="margin-top: 15px;">
              <label for="gcdNum3" class="input-label">Third Integer (C) <span style="font-size:0.8rem; font-weight:normal; opacity:0.75;">(Optional for 3-number analysis)</span></label>
              <input type="number" id="gcdNum3" class="calc-input" placeholder="Leave empty or enter integer" step="1" min="1">
            </div>

            <div class="primary-result" style="margin-top: 25px;">
              <div class="result-label">Computed Greatest Common Divisor (GCD / GCF)</div>
              <div class="result-value" id="gcdPrimaryResult">12</div>
              <div class="result-subtext" id="gcdSubtext">Euclidean reduction: gcd(48, 180) = 12</div>
            </div>

            <div class="results-grid" style="margin-top: 20px;">
              <div class="result-item">
                <div class="result-label">Least Common Multiple (LCM)</div>
                <div class="result-value" id="resLcm">720</div>
              </div>
              <div class="result-item">
                <div class="result-label">Coprime Status</div>
                <div class="result-value" id="resCoprime">No (gcd &gt; 1)</div>
              </div>
              <div class="result-item">
                <div class="result-label">Product A × B</div>
                <div class="result-value" id="resProduct">8,640</div>
              </div>
              <div class="result-item">
                <div class="result-label">Identity (GCD × LCM)</div>
                <div class="result-value" id="resIdentity">8,640</div>
              </div>
            </div>

            <div class="conversion-steps" style="margin-top: 25px;">
              <h3>Algorithmic Reduction & Prime Factorization</h3>
              <div id="stepsDisplay" style="font-family: monospace; font-size: 0.95rem; line-height: 1.6; background: rgba(0,0,0,0.03); padding: 16px; border-radius: 8px; border-left: 4px solid var(--accent, #2563eb);">
                Loading calculation steps...
              </div>
            </div>
          </section>

          <article class="article-body">
            <h2>1. Foundations of Divisibility, Greatest Common Divisor, and Least Common Multiple</h2>
            <p>In discrete mathematics, number theory, and modern computational algebra, the concepts of divisibility form the bedrock upon which cryptography, distributed consensus algorithms, and harmonic analysis are constructed. Let \(\mathbb{Z}\) denote the set of all integers. Given two integers \(a, b \in \mathbb{Z}\) with \(b \neq 0\), we say that \(b\) divides \(a\) (denoted symbolically as \(b \mid a\)) if and only if there exists an integer \(k \in \mathbb{Z}\) such that \(a = k \cdot b\). When this condition is met, \(b\) is termed a divisor or factor of \(a\), and \(a\) is termed a multiple of \(b\).</p>

            <p>The <strong>Greatest Common Divisor (GCD)</strong>—frequently referred to in secondary education as the <strong>Greatest Common Factor (GCF)</strong> or <strong>Highest Common Factor (HCF)</strong>—of two non-zero integers \(a\) and \(b\) is defined as the largest positive integer \(d\) that satisfies both \(d \mid a\) and \(d \mid b\). Formally, the set of common divisors is defined by:</p>

            $$\mathcal{D}(a, b) = \{x \in \mathbb{Z}^+ : x \mid a \land x \mid b\}$$

            <p>Because \(\mathcal{D}(a, b)\) is a non-empty, finite subset of positive integers (since \(1 \in \mathcal{D}(a, b)\) and every divisor of \(a\) is strictly \(\le |a|\)), the well-ordering principle of natural numbers guarantees that \(\mathcal{D}(a, b)\) contains a unique maximum element, denoted \(\gcd(a, b)\). When \(\gcd(a, b) = 1\), the integers \(a\) and \(b\) are defined as <em>mutually prime</em> or <em>coprime</em>, indicating that they share no non-trivial factors.</p>

            <p>Conversely, the <strong>Least Common Multiple (LCM)</strong> of two non-zero integers \(a\) and \(b\) is defined as the smallest positive integer \(m\) that is a simultaneous multiple of both \(a\) and \(b\). Formally, the set of common multiples is:</p>

            $$\mathcal{M}(a, b) = \{y \in \mathbb{Z}^+ : a \mid y \land b \mid y\}$$

            <p>The unique minimum positive element of \(\mathcal{M}(a, b)\) is denoted \(\operatorname{lcm}(a, b)\). While naive human computation frequently relies on listing multiples or manual factor trees, computational systems utilize foundational number-theoretic theorems to derive these values in microsecond timescales.</p>

            <h2>2. The Euclidean Algorithm: Principles, History, and Proof</h2>
            <p>Originating around 300 BCE in Book VII of Euclid's <em>Elements</em>, the Euclidean Algorithm remains one of the oldest, most elegant, and most computationally efficient numerical algorithms in active use across computer hardware and software. The algorithm avoids prime factorization entirely, relying instead on a simple division lemma.</p>

            <h3>2.1 Division Algorithm and Invariance Lemma</h3>
            <p>By the classical Division Algorithm theorem, for any integers \(a\) and \(b\) with \(b > 0\), there exist unique integers \(q\) (quotient) and \(r\) (remainder) such that:</p>

            $$a = b \cdot q + r \quad \text{where} \quad 0 \le r < b$$

            <p>The core invariance principle of the Euclidean algorithm asserts that the common divisors of \(a\) and \(b\) are identical to the common divisors of \(b\) and \(r\). That is:</p>

            $$\gcd(a, b) = \gcd(b, a \bmod b)$$

            <p><strong>Proof of the Lemma:</strong> Let \(d = \gcd(a, b)\). By definition, \(d \mid a\) and \(d \mid b\). Because \(r = a - b \cdot q\), any integer that divides both \(a\) and \(b\) must also divide their linear combination \(a - b \cdot q\). Hence, \(d \mid r\). Thus, \(d\) is a common divisor of \(b\) and \(r\), proving that \(\gcd(a, b) \le \gcd(b, r)\). Conversely, let \(c = \gcd(b, r)\). Since \(c \mid b\) and \(c \mid r\), it follows that \(c \mid (b \cdot q + r)\), meaning \(c \mid a\). Thus \(c\) is a common divisor of \(a\) and \(b\), proving that \(\gcd(b, r) \le \gcd(a, b)\). Combining both inequalities establishes that \(\gcd(a, b) = \gcd(b, r)\) identically.</p>

            <h3>2.2 Algorithmic Execution Steps</h3>
            <p>The Euclidean reduction proceeds via successive divisions: let \(r_0 = a\) and \(r_1 = b\). For \(k \ge 1\), compute:</p>

            $$\begin{aligned}
            r_0 &= r_1 \cdot q_1 + r_2 \quad &(0 \le r_2 < r_1) \\
            r_1 &= r_2 \cdot q_2 + r_3 \quad &(0 \le r_3 < r_2) \\
            r_2 &= r_3 \cdot q_3 + r_4 \quad &(0 \le r_4 < r_3) \\
            &\;\vdots \\
            r_{n-2} &= r_{n-1} \cdot q_{n-1} + r_n \quad &(0 \le r_n < r_{n-1}) \\
            r_{n-1} &= r_n \cdot q_n + 0
            \end{aligned}$$

            <p>Because the sequence of remainders strictly decreases (\(r_1 > r_2 > r_3 > \dots \ge 0\)), the process must terminate in a finite number of steps when the remainder reaches zero. The final non-zero remainder, \(r_n\), is exactly \(\gcd(a, b)\).</p>

            <h3>2.3 Computational Complexity and Lamé's Theorem</h3>
            <p>Gabriel Lamé proved in 1844 that the Euclidean algorithm represents the historical beginning of computational complexity theory. Lamé's theorem proves that the number of division steps required by the Euclidean algorithm never exceeds five times the number of decimal digits in the smaller number \(b\). In big-O notation, the algorithm executes in \(O(\log(\min(a, b)))\) operations, rendering it virtually instantaneous even for 4096-bit cryptographic keys.</p>

            <h2>3. The Fundamental Theorem of Arithmetic and Prime Factorization</h2>
            <p>An alternative foundational perspective stems from the <strong>Fundamental Theorem of Arithmetic</strong>, which guarantees that every positive integer \(n > 1\) can be represented uniquely as a product of prime powers:</p>

            $$n = \prod_{i=1}^{k} p_i^{\alpha_i} = p_1^{\alpha_1} p_2^{\alpha_2} \cdots p_k^{\alpha_k}$$

            <p>where \(p_1 < p_2 < \dots < p_k\) are distinct prime numbers and \(\alpha_i \in \mathbb{Z}^+\) are positive integer exponents. When analyzing two numbers \(a\) and \(b\), we can express both using a shared union of distinct prime bases \(\{p_1, p_2, \dots, p_m\}\), permitting exponents of zero where a prime is absent:</p>

            $$a = \prod_{i=1}^{m} p_i^{\alpha_i}, \quad b = \prod_{i=1}^{m} p_i^{\beta_i} \quad (\alpha_i, \beta_i \ge 0)$$

            <h3>3.1 Deriving GCD and LCM from Prime Exponents</h3>
            <p>Under this canonical representation, the Greatest Common Divisor must incorporate each prime factor to the lowest power common to both numbers. Conversely, the Least Common Multiple must incorporate each prime factor to the highest power required by either number:</p>

            $$\gcd(a, b) = \prod_{i=1}^{m} p_i^{\min(\alpha_i, \beta_i)}$$

            $$\operatorname{lcm}(a, b) = \prod_{i=1}^{m} p_i^{\max(\alpha_i, \beta_i)}$$

            <h3>3.2 The Product-GCD-LCM Fundamental Identity</h3>
            <p>For any two real numbers \(x, y\), the algebraic identity \(\min(x, y) + \max(x, y) = x + y\) holds unconditionally. Applying this principle exponent-by-exponent across all prime factors:</p>

            $$\min(\alpha_i, \beta_i) + \max(\alpha_i, \beta_i) = \alpha_i + \beta_i$$

            <p>Multiplying across all prime factors yields the fundamental product identity:</p>

            $$\gcd(a, b) \times \operatorname{lcm}(a, b) = \prod_{i=1}^{m} p_i^{\min(\alpha_i, \beta_i) + \max(\alpha_i, \beta_i)} = \prod_{i=1}^{m} p_i^{\alpha_i + \beta_i} = a \times b$$

            <p>This magnificent result means that once \(\gcd(a, b)\) is computed via the ultra-fast Euclidean algorithm, the LCM can be derived with a single 64-bit integer division:</p>

            $$\operatorname{lcm}(a, b) = \frac{a \times b}{\gcd(a, b)} = \frac{|a \cdot b|}{\gcd(a, b)}$$

            <h2>4. Bézout's Identity and the Extended Euclidean Algorithm</h2>
            <p>Beyond finding the divisor itself, Etienne Bézout established in 1779 that the greatest common divisor can always be expressed as an integer linear combination of the initial numbers. Specifically, for non-zero integers \(a\) and \(b\), there exist integers \(x, y \in \mathbb{Z}\) (known as Bézout coefficients) such that:</p>

            $$a \cdot x + b \cdot y = \gcd(a, b)$$

            <p>The <strong>Extended Euclidean Algorithm</strong> computes these coefficients \(x\) and \(y\) concurrently with the GCD by maintaining auxiliary recurrence relations during the back-substitution phase. This capability is paramount in modern cryptographic systems:</p>
            <ul>
              <li><strong>Modular Multiplicative Inverses:</strong> When \(\gcd(a, m) = 1\), Bézout's identity simplifies to \(a \cdot x + m \cdot y = 1\). Reducing this modulo \(m\) produces \(a \cdot x \equiv 1 \pmod m\), proving that \(x\) is the modular multiplicative inverse of \(a\) modulo \(m\) (\(x = a^{-1} \bmod m\)).</li>
              <li><strong>RSA Key Derivation:</strong> In RSA public-key cryptosystems, the private decryption key exponent \(d\) is calculated as the modular inverse of the public encryption exponent \(e\) modulo Euler's totient function \(\phi(n)\): \(d \equiv e^{-1} \pmod{\phi(n)}\).</li>
              <li><strong>Linear Diophantine Equations:</strong> Equations of the form \(a \cdot x + b \cdot y = c\) possess integer solutions if and only if \(\gcd(a, b) \mid c\).</li>
            </ul>

            <h2>5. Engineering and Physical Systems Applications</h2>
            <p>Outside abstract pure mathematics, GCD and LCM govern physical phenomena across mechanical, electrical, and chronometric engineering:</p>

            <h3>5.1 Gear Mesh Wear and Hunting Tooth Frequency</h3>
            <p>In mechanical gear design, two meshing gears with tooth counts \(N_1\) and \(N_2\) experience physical contact cycles determined entirely by number theory. The total number of tooth mesh events before the exact same pair of teeth touch again is governed by \(\operatorname{lcm}(N_1, N_2)\). If \(\gcd(N_1, N_2) = d > 1\), tooth 1 on gear 1 will only ever touch \(N_2 / d\) specific teeth on gear 2. Any imperfection or manufacturing defect on a tooth repeatedly batters the exact same subset of teeth, inducing localized fatigue and premature mechanical failure. Consequently, precision machine designers deliberately choose <em>hunting tooth</em> gear designs where \(\gcd(N_1, N_2) = 1\) (coprime tooth counts), ensuring that every tooth meshes with every other tooth in rotation, evening out wear and prolonging gearbox lifespans.</p>

            <h3>5.2 Microcontroller PWM, Baud Rates, and Clock Synchronization</h3>
            <p>Digital systems operating across multiple clock domains (e.g., synchronizing a 16 MHz microcontroller with a 115,200 baud serial UART communication bus or an external SPI peripheral at 10 MHz) require clock dividers. Determining the shortest master period over which two asynchronous periodic signals repeat their relative phase orientation requires calculating the LCM of their respective clock period lengths.</p>

            <h2>6. Benchmark Comparative Reference Table</h2>
            <p>The following table provides verified GCD, LCM, prime factorizations, and coprimality classifications across representative mathematical and engineering integer pairs.</p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>Integer Pair (A, B)</th>
                  <th>Prime Factorization (A)</th>
                  <th>Prime Factorization (B)</th>
                  <th>GCD / GCF</th>
                  <th>LCM</th>
                  <th>Coprime?</th>
                  <th>Verification (\(A \times B = \gcd \times \operatorname{lcm}\))</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>(48, 180)</td>
                  <td>\(2^4 \times 3^1\)</td>
                  <td>\(2^2 \times 3^2 \times 5^1\)</td>
                  <td>12</td>
                  <td>720</td>
                  <td>No</td>
                  <td>\(8,640 = 12 \times 720\)</td>
                </tr>
                <tr>
                  <td>(17, 31)</td>
                  <td>\(17^1\)</td>
                  <td>\(31^1\)</td>
                  <td>1</td>
                  <td>527</td>
                  <td>Yes</td>
                  <td>\(527 = 1 \times 527\)</td>
                </tr>
                <tr>
                  <td>(144, 360)</td>
                  <td>\(2^4 \times 3^2\)</td>
                  <td>\(2^3 \times 3^2 \times 5^1\)</td>
                  <td>72</td>
                  <td>720</td>
                  <td>No</td>
                  <td>\(51,840 = 72 \times 720\)</td>
                </tr>
                <tr>
                  <td>(35, 64)</td>
                  <td>\(5^1 \times 7^1\)</td>
                  <td>\(2^6\)</td>
                  <td>1</td>
                  <td>2,240</td>
                  <td>Yes</td>
                  <td>\(2,240 = 1 \times 2,240\)</td>
                </tr>
                <tr>
                  <td>(210, 525)</td>
                  <td>\(2^1 \times 3^1 \times 5^1 \times 7^1\)</td>
                  <td>\(3^1 \times 5^2 \times 7^1\)</td>
                  <td>105</td>
                  <td>1,050</td>
                  <td>No</td>
                  <td>\(110,250 = 105 \times 1,050\)</td>
                </tr>
                <tr>
                  <td>(81, 243)</td>
                  <td>\(3^4\)</td>
                  <td>\(3^5\)</td>
                  <td>81</td>
                  <td>243</td>
                  <td>No</td>
                  <td>\(19,683 = 81 \times 243\)</td>
                </tr>
                <tr>
                  <td>(1024, 768)</td>
                  <td>\(2^{10}\)</td>
                  <td>\(2^8 \times 3^1\)</td>
                  <td>256</td>
                  <td>3,072</td>
                  <td>No</td>
                  <td>\(786,432 = 256 \times 3,072\)</td>
                </tr>
                <tr>
                  <td>(59, 101)</td>
                  <td>\(59^1\)</td>
                  <td>\(101^1\)</td>
                  <td>1</td>
                  <td>5,959</td>
                  <td>Yes</td>
                  <td>\(5,959 = 1 \times 5,959\)</td>
                </tr>
              </tbody>
            </table>

            <h2>7. Worked Engineering Case Study: Industrial Gearbox Meshing & Service Interval</h2>
            <div class="worked-example-card">
              <div class="example-header">
                <strong>Case Study:</strong> Planetary Gear Mesh Wear and Cyclic Inspection Schedule
              </div>
              <div class="example-body">
                <p><strong>Scenario:</strong> An industrial conveyor drive gearbox connects a motor pinion gear with \(N_1 = 36\) teeth to a secondary driven spur gear with \(N_2 = 84\) teeth. The motor operates continuously at \(n_1 = 1,200\text{ RPM}\). The reliability engineering team needs to determine: (1) whether the gear mesh is prone to localized harmonic wear, (2) the exact rotational periods before the same teeth re-engage, and (3) the hunting tooth engagement frequency.</p>

                <p><strong>Step 1: Calculate the Greatest Common Divisor (GCD)</strong><br>
                Using the Euclidean algorithm:
                $$\begin{aligned}
                84 &= 36 \times 2 + 12 \\
                36 &= 12 \times 3 + 0
                \end{aligned}$$
                The final non-zero remainder is 12. Therefore, \(\gcd(36, 84) = 12\).</p>

                <p><strong>Step 2: Assess Wear Distribution & Tooth Engagement Sets</strong><br>
                Because \(\gcd(36, 84) = 12 \neq 1\), the gears are <em>not coprime</em>. A given tooth on the 36-tooth pinion will only ever mesh with:
                $$\frac{84}{\gcd(36, 84)} = \frac{84}{12} = 7 \text{ distinct teeth on the 84-tooth gear}$$
                Likewise, each tooth on the 84-tooth gear will only ever mesh with \(36 / 12 = 3\) distinct teeth on the pinion. This represents a heavy localized wear vulnerability: if tooth #1 develops a microscopic pit or burr, it will repeatedly strike the exact same 7 teeth on the driven gear, causing accelerated mechanical breakdown.</p>

                <p><strong>Step 3: Calculate the Least Common Multiple (LCM)</strong><br>
                $$\operatorname{lcm}(36, 84) = \frac{36 \times 84}{\gcd(36, 84)} = \frac{3,024}{12} = 252 \text{ teeth}$$
                The exact same tooth pair meshes once every 252 tooth passages.</p>

                <p><strong>Step 4: Compute Rotational Frequency and Time Interval</strong><br>
                The pinion rotates at 1,200 RPM = \(20\text{ rev/sec}\). Teeth mesh at a tooth-passing frequency of:
                $$f_{\text{mesh}} = 20 \times 36 = 720 \text{ teeth/second}$$
                The time required for 252 teeth to pass is:
                $$\Delta t = \frac{252 \text{ teeth}}{720 \text{ teeth/sec}} = 0.35 \text{ seconds}$$
                Every 0.35 seconds (or every \(252 / 36 = 7\) revolutions of the pinion and \(252 / 84 = 3\) revolutions of the driven gear), the exact same tooth pair collides. The vibration analysis team can isolate a prominent spectral spike at \(1 / 0.35\text{ s} \approx 2.857\text{ Hz}\) to diagnose pinion pitting defects.</p>
              </div>
            </div>

            <h2>8. Frequently Asked Questions (FAQ)</h2>
            <div class="faq-accordion">
              <div class="faq-item">
                <h3 class="faq-question">Can the GCD of two negative integers be computed?</h3>
                <div class="faq-answer">
                  <p>Yes. By mathematical convention, the GCD is defined strictly as a positive integer. For negative integers \(a\) and \(b\), \(\gcd(a, b) = \gcd(|a|, |b|)\). For example, \(\gcd(-48, 180) = \gcd(48, -180) = \gcd(-48, -180) = 12\). The sign of the numbers does not alter their set of positive divisors.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">How does one compute GCD and LCM for three or more numbers?</h3>
                <div class="faq-answer">
                  <p>The GCD and LCM operations are both associative and commutative. For three integers \(a, b, c\):
                  $$\gcd(a, b, c) = \gcd(\gcd(a, b), c)$$
                  $$\operatorname{lcm}(a, b, c) = \operatorname{lcm}(\operatorname{lcm}(a, b), c)$$
                  Note, however, that the product formula does not hold in the simple form \(a \cdot b \cdot c \neq \gcd(a, b, c) \cdot \operatorname{lcm}(a, b, c)\). The correct three-variable relation involves pairwise GCDs and LCMs via inclusion-exclusion.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">What occurs when one of the input numbers is zero?</h3>
                <div class="faq-answer">
                  <p>Every non-zero integer divides 0 because \(0 = 0 \times k\). Therefore, for any non-zero integer \(a\), \(\gcd(a, 0) = |a|\). The case \(\gcd(0, 0)\) is mathematically undefined (or formally defined as 0 in some abstract algebra contexts) because every integer divides zero, yielding no greatest divisor. For LCM, if either number is 0, the LCM is defined as 0.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">Why is finding prime factors much slower than running Euclid's algorithm?</h3>
                <div class="faq-answer">
                  <p>Finding the prime factors of an arbitrary large composite integer is currently believed to belong to computational complexity class NP-intermediate, with the fastest classical algorithm (the General Number Field Sieve) having sub-exponential running time. In stark contrast, the Euclidean algorithm requires only repeated modular divisions and completes in polynomial logarithmic time \(O(\log(\min(a, b)))\). This fundamental asymmetry makes modern asymmetric RSA cryptography secure.</p>
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
              <li><a href="percentage-calculator.html">Percentage Calculator</a></li>
              <li><a href="scientific-notation-calculator.html">Scientific Notation Calculator</a></li>
              <li><a href="significant-figures-calculator.html">Significant Figures Calculator</a></li>
              <li><a href="quadratic-equation-calculator.html">Quadratic Equation Calculator</a></li>
              <li><a href="pythagorean-theorem-calculator.html">Pythagorean Theorem Calculator</a></li>
              <li><a href="prime-number-calculator.html">Prime Number Calculator</a></li>
              <li><a href="matrix-calculator.html">Matrix Calculator</a></li>
            </ul>
          </div>

          <div class="sidebar-card">
            <h3 class="sidebar-title">Mathematical Identities</h3>
            <div style="font-size:0.875rem; line-height:1.5; color:var(--text-muted, #4b5563);">
              <p><strong>Divisibility:</strong> \(b \mid a \iff \exists k \in \mathbb{Z}: a = kb\)</p>
              <p><strong>Euclidean Lemma:</strong> \(\gcd(a, b) = \gcd(b, a \bmod b)\)</p>
              <p><strong>Product Law:</strong> \(a \cdot b = \gcd(a, b) \cdot \operatorname{lcm}(a, b)\)</p>
              <p><strong>Bézout:</strong> \(ax + by = \gcd(a, b)\)</p>
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
    function primeFactors(n) {
      n = Math.abs(Math.floor(n));
      const factors = {};
      let d = 2;
      while (d * d <= n) {
        while (n % d === 0) {
          factors[d] = (factors[d] || 0) + 1;
          n /= d;
        }
        d = d === 2 ? 3 : d + 2;
      }
      if (n > 1) {
        factors[n] = (factors[n] || 0) + 1;
      }
      return factors;
    }

    function formatFactors(factors) {
      const keys = Object.keys(factors).map(Number).sort((a,b) => a - b);
      if (keys.length === 0) return "1";
      return keys.map(p => factors[p] > 1 ? `${p}^${factors[p]}` : `${p}`).join(" × ");
    }

    function computeGcdTwo(a, b, recordSteps) {
      let r0 = Math.abs(a);
      let r1 = Math.abs(b);
      const steps = [];
      if (r1 === 0) return { gcd: r0, steps: ["gcd(" + r0 + ", 0) = " + r0] };
      
      while (r1 > 0) {
        const q = Math.floor(r0 / r1);
        const r = r0 % r1;
        if (recordSteps) {
          steps.push(`${r0} = ${r1} × ${q} + ${r}`);
        }
        r0 = r1;
        r1 = r;
      }
      return { gcd: r0, steps: steps };
    }

    function compute() {
      const n1 = Math.abs(parseInt(document.getElementById('gcdNum1').value, 10)) || 1;
      const n2 = Math.abs(parseInt(document.getElementById('gcdNum2').value, 10)) || 1;
      const n3Val = document.getElementById('gcdNum3').value.trim();
      const hasN3 = n3Val !== "" && !isNaN(parseInt(n3Val, 10)) && parseInt(n3Val, 10) > 0;
      const n3 = hasN3 ? Math.abs(parseInt(n3Val, 10)) : null;

      const res12 = computeGcdTwo(n1, n2, true);
      let finalGcd = res12.gcd;
      let finalLcm = (n1 * n2) / finalGcd;

      let displayHtml = "<strong>Euclidean Algorithm (A & B):</strong><br>";
      displayHtml += res12.steps.join("<br>");

      if (hasN3) {
        const res3 = computeGcdTwo(finalGcd, n3, true);
        finalGcd = res3.gcd;
        finalLcm = (finalLcm * n3) / computeGcdTwo(finalLcm, n3, false).gcd;
        displayHtml += "<br><br><strong>Euclidean Algorithm with C (" + n3 + "):</strong><br>";
        displayHtml += res3.steps.join("<br>");
      }

      const factorsA = primeFactors(n1);
      const factorsB = primeFactors(n2);
      displayHtml += "<br><br><strong>Prime Factorizations:</strong><br>";
      displayHtml += `A (${n1}) = ${formatFactors(factorsA)}<br>`;
      displayHtml += `B (${n2}) = ${formatFactors(factorsB)}`;
      if (hasN3) {
        displayHtml += `<br>C (${n3}) = ${formatFactors(primeFactors(n3))}`;
      }

      document.getElementById('gcdPrimaryResult').textContent = finalGcd.toLocaleString();
      document.getElementById('gcdSubtext').textContent = hasN3
        ? `gcd(${n1}, ${n2}, ${n3}) = ${finalGcd}`
        : `gcd(${n1}, ${n2}) = ${finalGcd}`;

      document.getElementById('resLcm').textContent = finalLcm.toLocaleString();
      document.getElementById('resCoprime').textContent = finalGcd === 1 ? "Yes (Coprime)" : `No (gcd = ${finalGcd})`;

      if (!hasN3) {
        const prod = n1 * n2;
        const identity = finalGcd * finalLcm;
        document.getElementById('resProduct').textContent = prod.toLocaleString();
        document.getElementById('resIdentity').textContent = identity.toLocaleString();
      } else {
        document.getElementById('resProduct').textContent = (n1 * n2 * n3).toLocaleString();
        document.getElementById('resIdentity').textContent = "Multi-number";
      }

      document.getElementById('stepsDisplay').innerHTML = displayHtml;
    }

    document.getElementById('gcdNum1').addEventListener('input', compute);
    document.getElementById('gcdNum2').addEventListener('input', compute);
    document.getElementById('gcdNum3').addEventListener('input', compute);
    compute();
  </script>
</body>
</html>
"""

# -------------------------------------------------------------
# 2. QUADRATIC EQUATION CALCULATOR
# -------------------------------------------------------------
quad_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quadratic Equation Calculator — Roots, Vertex, Discriminant & Parabola | CalcHub</title>
  <meta name="description" content="Solve quadratic equations ax² + bx + c = 0 with real and complex roots, discriminant analysis, vertex coordinates, axis of symmetry, and projectile motion modeling.">
  <meta name="keywords" content="quadratic equation calculator, quadratic formula, discriminant calculator, parabola vertex, solve quadratic, roots of polynomial, completing the square, projectile motion calculator">
  <meta name="author" content="CalcHub Polynomial & Applied Mechanics Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/quadratic-equation-calculator.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="Quadratic Equation Calculator — Roots, Vertex, Discriminant & Parabola | CalcHub">
  <meta property="og:description" content="Calculate real and complex roots, discriminant, parabola vertex, and axis of symmetry for any quadratic polynomial ax² + bx + c = 0.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/quadratic-equation-calculator.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/quadratic-equation-calculator.html#app",
      "name": "Quadratic Polynomial & Parabolic Solver",
      "url": "https://calchub.org/quadratic-equation-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "High-precision algebraic solver for quadratic equations ax² + bx + c = 0 providing exact real/complex roots, discriminant evaluation, and parabola vertex coordinates."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Math & Engineering Calculators", "item": "https://calchub.org/math.html"},
        {"@type": "ListItem", "position": 3, "name": "Quadratic Equation Calculator", "item": "https://calchub.org/quadratic-equation-calculator.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How does the discriminant (b² - 4ac) determine the nature of quadratic roots?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The discriminant, symbolized as Δ = b² - 4ac, dictates the geometric and algebraic nature of the roots. If Δ > 0, the equation has two distinct real roots, and the corresponding parabola intersects the x-axis at two separate points. If Δ = 0, the equation has exactly one real repeated root (a double root), meaning the parabola's vertex is tangent to the x-axis. If Δ < 0, the square root yields an imaginary number, resulting in two complex conjugate roots (u ± vi), and the parabola never crosses the x-axis."
          }
        },
        {
          "@type": "Question",
          "name": "How are the coordinates of the parabola's vertex derived?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The vertex represents the extreme point (global minimum if a > 0, or global maximum if a < 0) of the quadratic function f(x) = ax² + bx + c. From calculus, setting the first derivative f'(x) = 2ax + b equal to zero yields the x-coordinate of the vertex: h = -b / (2a). Substituting h back into f(x) yields the y-coordinate: k = f(-b / (2a)) = c - b² / (4a) = -Δ / (4a). In vertex form, the function is expressed as f(x) = a(x - h)² + k."
          }
        },
        {
          "@type": "Question",
          "name": "Why must the leading coefficient 'a' never equal zero in a quadratic equation?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "By mathematical definition, a polynomial is of second degree (quadratic) if and only if the coefficient of the squared term x² is non-zero (a ≠ 0). If a = 0, the quadratic term vanishes, degenerating the equation into a first-degree linear equation bx + c = 0, which has only a single root x = -c / b (assuming b ≠ 0), losing all parabolic and discriminant properties."
          }
        },
        {
          "@type": "Question",
          "name": "How is the quadratic formula used in classical projectile motion physics?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Under constant downward gravitational acceleration g, the vertical position of an object launched with initial vertical velocity v₀ from initial height y₀ follows the kinematic quadratic equation: y(t) = -0.5*g*t² + v₀*t + y₀. Setting y(t) = 0 models when the projectile strikes the ground. Solving this quadratic equation for t using the quadratic formula yields the exact flight duration."
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
            <div class="badge-tag">Polynomial Algebra & Analytical Geometry</div>
            <h1 class="tool-title">Quadratic Equation Calculator</h1>
            <p class="tool-subtitle">Solve any quadratic equation \(ax^2 + bx + c = 0\) with exact real/complex roots, discriminant classification, parabola vertex, and step-by-step algebraic breakdown.</p>
          </header>

          <section class="calculator-card" aria-label="Quadratic Equation Solver">
            <div class="calc-grid" style="grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));">
              <div class="input-group">
                <label for="coefA" class="input-label">Coefficient <em>a</em> (\(x^2\))</label>
                <input type="number" id="coefA" class="calc-input" value="1" step="any">
              </div>

              <div class="input-group">
                <label for="coefB" class="input-label">Coefficient <em>b</em> (\(x\))</label>
                <input type="number" id="coefB" class="calc-input" value="-5" step="any">
              </div>

              <div class="input-group">
                <label for="coefC" class="input-label">Constant <em>c</em></label>
                <input type="number" id="coefC" class="calc-input" value="6" step="any">
              </div>
            </div>

            <div class="primary-result" style="margin-top: 25px;">
              <div class="result-label">Calculated Roots (\(x_1, x_2\))</div>
              <div class="result-value" id="quadRootsPrimary">x₁ = 3, x₂ = 2</div>
              <div class="result-subtext" id="quadNatureSubtext">Two distinct real rational roots</div>
            </div>

            <div class="results-grid" style="margin-top: 20px;">
              <div class="result-item">
                <div class="result-label">Discriminant (\(\Delta = b^2 - 4ac\))</div>
                <div class="result-value" id="resDelta">1.0000</div>
              </div>
              <div class="result-item">
                <div class="result-label">Parabola Vertex \((h, k)\)</div>
                <div class="result-value" id="resVertex">(2.500, -0.250)</div>
              </div>
              <div class="result-item">
                <div class="result-label">Axis of Symmetry</div>
                <div class="result-value" id="resAxis">x = 2.5000</div>
              </div>
              <div class="result-item">
                <div class="result-label">Parabola Concavity</div>
                <div class="result-value" id="resConcavity">Upward (a &gt; 0)</div>
              </div>
            </div>

            <div class="conversion-steps" style="margin-top: 25px;">
              <h3>Step-by-Step Algebraic Solution</h3>
              <div id="quadStepsDisplay" style="font-family: monospace; font-size: 0.95rem; line-height: 1.6; background: rgba(0,0,0,0.03); padding: 16px; border-radius: 8px; border-left: 4px solid var(--accent, #2563eb);">
                Loading algebraic resolution...
              </div>
            </div>
          </section>

          <article class="article-body">
            <h2>1. Algebraic Anatomy of the Quadratic Polynomial</h2>
            <p>A second-degree polynomial equation in a single variable \(x\) is known fundamentally as a <strong>quadratic equation</strong>. In its canonical standard form, it is expressed as:</p>

            $$a x^2 + b x + c = 0$$

            <p>where \(x\) represents an unknown variable, and \(a, b, c \in \mathbb{R}\) are real numerical coefficients subjected to the single non-degeneracy axiom that \(a \neq 0\). The quadratic term \(a x^2\) imparts curvature and non-linear properties to the function, the linear term \(b x\) governs horizontal translation and skew, and the constant term \(c\) dictates the vertical intercept where the curve crosses the ordinate axis (\(x = 0 \implies y = c\)).</p>

            <p>Quadratic equations appear ubiquitously throughout classical physics, optics, structural mechanics, signal analysis, economics, and computational biology. Whenever a physical law incorporates an inverse-square distance force (such as Newton's Universal Gravitation or Coulomb's Electrostatic Law), kinetic energy (\(E_k = \frac{1}{2}m v^2\)), gravitational projectile ballistics, or revenue functions in microeconomics, the governing equations reduce directly to quadratic expressions.</p>

            <h2>2. The Quadratic Formula and Derivation via Completing the Square</h2>
            <p>The universal algebraic solution for finding the roots of any quadratic equation without iterative numerical approximations is given by the renowned <strong>Quadratic Formula</strong>:</p>

            $$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

            <p>While often memorized by rote, the formula is a direct consequence of the algebraic technique known as <em>completing the square</em>, originally formulated in geometric terms by Persian mathematician Muhammad ibn Musa al-Khwarizmi in the 9th century CE.</p>

            <h3>2.1 Step-by-Step Rigorous Algebraic Derivation</h3>
            <p>Consider the general equation with \(a \neq 0\):</p>

            $$a x^2 + b x + c = 0$$

            <p><strong>Step 1: Normalize by the leading coefficient \(a\).</strong><br>
            Dividing every term across the equation by \(a\):</p>

            $$x^2 + \frac{b}{a} x + \frac{c}{a} = 0$$

            <p><strong>Step 2: Isolate the constant term.</strong><br>
            Subtracting \(\frac{c}{a}\) from both sides:</p>

            $$x^2 + \frac{b}{a} x = -\frac{c}{a}$$

            <p><strong>Step 3: Complete the square on the left-hand side.</strong><br>
            Recall the binomial expansion \((x + d)^2 = x^2 + 2dx + d^2\). Matching the linear coefficient \(\frac{b}{a} = 2d\) reveals that \(d = \frac{b}{2a}\). To make the left-hand side a perfect square trinomial, add \(d^2 = \left(\frac{b}{2a}\right)^2 = \frac{b^2}{4a^2}\) to both sides of the equation:</p>

            $$x^2 + \frac{b}{a} x + \frac{b^2}{4a^2} = -\frac{c}{a} + \frac{b^2}{4a^2}$$

            <p><strong>Step 4: Factor the trinomial and find a common denominator.</strong><br>
            The left side contracts to a squared binomial, and the right side combines over \(4a^2\):</p>

            $$\left(x + \frac{b}{2a}\right)^2 = \frac{b^2 - 4ac}{4a^2}$$

            <p><strong>Step 5: Extract the square root and solve for \(x\).</strong><br>
            Taking the square root of both sides introduces the dual sign \(\pm\):</p>

            $$x + \frac{b}{2a} = \pm \frac{\sqrt{b^2 - 4ac}}{2a}$$

            <p>Subtracting \(\frac{b}{2a}\) yields the standard quadratic formula:</p>

            $$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

            <h2>3. The Discriminant: Classifying the Nature of the Roots</h2>
            <p>The algebraic expression nested within the radical, denoted by the Greek capital letter Delta (\(\Delta\)), is termed the <strong>discriminant</strong>:</p>

            $$\Delta = b^2 - 4ac$$

            <p>The discriminant acts as a diagnostic mathematical determinant, completely classifying the number, reality, and algebraic nature of the roots without explicitly computing the roots themselves:</p>

            <h3>3.1 Case 1: Positive Discriminant (\(\Delta > 0\))</h3>
            <p>When \(\Delta > 0\), the square root \(\sqrt{\Delta}\) is a strictly positive real number. Consequently, the equation possesses exactly <strong>two distinct real roots</strong>:</p>

            $$x_1 = \frac{-b + \sqrt{\Delta}}{2a}, \quad x_2 = \frac{-b - \sqrt{\Delta}}{2a}$$

            <p>Geometrically, the parabola intersects the horizontal \(x\)-axis at two discrete locations \((x_1, 0)\) and \((x_2, 0)\). Furthermore, if \(a, b, c \in \mathbb{Q}\) are rational numbers and \(\Delta\) is a perfect square of a rational number, both roots are rational numbers. If \(\Delta\) is not a perfect square, both roots are real irrational conjugate numbers.</p>

            <h3>3.2 Case 2: Zero Discriminant (\(\Delta = 0\))</h3>
            <p>When \(\Delta = 0\), the radical term vanishes entirely (\(\sqrt{0} = 0\)). The equation yields exactly <strong>one real repeated root</strong> (a double root of algebraic multiplicity 2):</p>

            $$x_1 = x_2 = -\frac{b}{2a}$$

            <p>Geometrically, the parabola is tangent to the \(x\)-axis; its extreme vertex point touches the axis without crossing it.</p>

            <h3>3.3 Case 3: Negative Discriminant (\(\Delta < 0\))</h3>
            <p>When \(\Delta < 0\), taking the square root in the real number domain \(\mathbb{R}\) is undefined. In the complex number domain \(\mathbb{C}\), we introduce the imaginary unit \(i = \sqrt{-1}\). Writing \(\sqrt{\Delta} = \sqrt{-1 \cdot |\Delta|} = i\sqrt{|\Delta|}\), the equation yields <strong>two complex conjugate roots</strong>:</p>

            $$x = \frac{-b}{2a} \pm i \frac{\sqrt{|\Delta|}}{2a} = u \pm vi$$

            <p>where the real part is \(u = -\frac{b}{2a}\) and the imaginary magnitude is \(v = \frac{\sqrt{4ac - b^2}}{2a}\). Geometrically, the parabola lies entirely above the \(x\)-axis (if \(a > 0\)) or entirely below the \(x\)-axis (if \(a < 0\)), never making contact with the horizontal axis in the real Cartesian plane.</p>

            <h2>4. Parabolic Geometry: Vertex, Axis of Symmetry, and Forms</h2>
            <p>Every quadratic equation corresponds to a planar curve termed a <strong>parabola</strong>, defined by the real function \(f(x) = ax^2 + bx + c\). Understanding its geometric properties is critical in structural engineering and orbital mechanics.</p>

            <h3>4.1 The Parabola Vertex \((h, k)\)</h3>
            <p>The vertex represents the turning point or extremum of the curve. If \(a > 0\), the parabola opens upward, and the vertex is the absolute global minimum. If \(a < 0\), the parabola opens downward, and the vertex is the absolute global maximum. From differential calculus, the extremum occurs where the tangent slope equals zero:</p>

            $$f'(x) = \frac{d}{dx}(ax^2 + bx + c) = 2ax + b = 0 \implies x = h = -\frac{b}{2a}$$

            <p>Evaluating the function at this critical coordinate yields the vertical height \(k\):</p>

            $$k = f(h) = a\left(-\frac{b}{2a}\right)^2 + b\left(-\frac{b}{2a}\right) + c = \frac{b^2}{4a} - \frac{2b^2}{4a} + c = c - \frac{b^2}{4a} = -\frac{\Delta}{4a}$$

            <h3>4.2 Vertex Form and Transformations</h3>
            <p>By substituting the vertex coordinates \((h, k)\), any quadratic function can be rewritten in <strong>vertex form</strong>:</p>

            $$f(x) = a(x - h)^2 + k$$

            <p>This form explicitly reveals the rigid body transformations: the standard parabola \(y = ax^2\) is shifted horizontally by \(h\) units and vertically by \(k\) units.</p>

            <h3>4.3 Focus, Directrix, and Reflective Properties</h3>
            <p>In geometric optics and radio antenna engineering, a parabola is defined as the locus of points equidistant from a fixed point (the <em>focus</em> \(F\)) and a fixed line (the <em>directrix</em> \(D\)). For a vertical parabola with vertex \((h, k)\):</p>
            <ul>
              <li><strong>Focal Length:</strong> \(p = \frac{1}{4a}\)</li>
              <li><strong>Focus Coordinates:</strong> \(F = \left(h, k + \frac{1}{4a}\right)\)</li>
              <li><strong>Directrix Equation:</strong> \(y = k - \frac{1}{4a}\)</li>
            </ul>
            <p>Due to the law of reflection, any parallel ray entering a parabolic reflector parallel to the axis of symmetry reflects directly through the focus. This geometric property underpins satellite dishes, astronomical telescopes, flashlight reflectors, and solar thermal concentrators.</p>

            <h2>5. Viète's Formulas and Symmetric Polynomial Relations</h2>
            <p>French mathematician François Viète established direct relations between the roots of a polynomial and its coefficients. For a quadratic equation with roots \(x_1\) and \(x_2\):</p>

            $$x_1 + x_2 = -\frac{b}{a}$$

            $$x_1 \cdot x_2 = \frac{c}{a}$$

            <p>These formulas enable instantaneous verification of calculated roots. For example, in electrical filter design, Viète's formulas allow engineers to design second-order transfer functions with predetermined resonant frequencies and damping factors by directly specifying the sum and product of the system poles.</p>

            <h2>6. Benchmark Comparative Reference Table</h2>
            <p>The table below catalogues benchmark quadratic equations spanning distinct coefficient signs, discriminant classifications, exact roots, and vertex coordinates.</p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>Equation (\(ax^2 + bx + c = 0\))</th>
                  <th>\(a, b, c\)</th>
                  <th>Discriminant \(\Delta\)</th>
                  <th>Root Classification</th>
                  <th>Exact Roots (\(x_1, x_2\))</th>
                  <th>Vertex \((h, k)\)</th>
                  <th>Axis of Symmetry</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>\(x^2 - 5x + 6 = 0\)</td>
                  <td>1, -5, 6</td>
                  <td>+1</td>
                  <td>Two Distinct Real Rational</td>
                  <td>\(3,\; 2\)</td>
                  <td>\((2.5, -0.25)\)</td>
                  <td>\(x = 2.5\)</td>
                </tr>
                <tr>
                  <td>\(x^2 - 6x + 9 = 0\)</td>
                  <td>1, -6, 9</td>
                  <td>0</td>
                  <td>One Real Double Root</td>
                  <td>\(3\) (multiplicity 2)</td>
                  <td>\((3, 0)\)</td>
                  <td>\(x = 3.0\)</td>
                </tr>
                <tr>
                  <td>\(x^2 + 4x + 13 = 0\)</td>
                  <td>1, 4, 13</td>
                  <td>-36</td>
                  <td>Two Complex Conjugate</td>
                  <td>\(-2 \pm 3i\)</td>
                  <td>\((-2, 9)\)</td>
                  <td>\(x = -2.0\)</td>
                </tr>
                <tr>
                  <td>\(2x^2 + 3x - 5 = 0\)</td>
                  <td>2, 3, -5</td>
                  <td>+49</td>
                  <td>Two Distinct Real Rational</td>
                  <td>\(1,\; -2.5\)</td>
                  <td>\((-0.75, -6.125)\)</td>
                  <td>\(x = -0.75\)</td>
                </tr>
                <tr>
                  <td>\(-4.9t^2 + 19.6t + 0 = 0\)</td>
                  <td>-4.9, 19.6, 0</td>
                  <td>+384.16</td>
                  <td>Two Distinct Real Rational</td>
                  <td>\(0,\; 4.0\)</td>
                  <td>\((2.0, 19.6)\)</td>
                  <td>\(t = 2.0\)</td>
                </tr>
                <tr>
                  <td>\(3x^2 - 2x + 1 = 0\)</td>
                  <td>3, -2, 1</td>
                  <td>-8</td>
                  <td>Two Complex Conjugate</td>
                  <td>\(\frac{1}{3} \pm i\frac{\sqrt{2}}{3}\)</td>
                  <td>\((0.333, 0.667)\)</td>
                  <td>\(x = 0.333\)</td>
                </tr>
                <tr>
                  <td>\(x^2 - 2 = 0\)</td>
                  <td>1, 0, -2</td>
                  <td>+8</td>
                  <td>Two Distinct Real Irrational</td>
                  <td>\(\pm \sqrt{2} \approx \pm 1.414\)</td>
                  <td>\((0, -2)\)</td>
                  <td>\(x = 0.0\)</td>
                </tr>
                <tr>
                  <td>\(-x^2 + 8x - 16 = 0\)</td>
                  <td>-1, 8, -16</td>
                  <td>0</td>
                  <td>One Real Double Root</td>
                  <td>\(4\) (multiplicity 2)</td>
                  <td>\((4, 0)\)</td>
                  <td>\(x = 4.0\)</td>
                </tr>
              </tbody>
            </table>

            <h2>7. Worked Physics Case Study: Ballistic Projectile Flight Duration & Apogee</h2>
            <div class="worked-example-card">
              <div class="example-header">
                <strong>Physics Case Study:</strong> Artillery Shell Flight Time from an Elevated Coastal Battery
              </div>
              <div class="example-body">
                <p><strong>Scenario:</strong> A coastal defense battery situated on a cliff \(y_0 = 45\text{ meters}\) above sea level fires a projectile with an initial muzzle velocity \(v_0 = 150\text{ m/s}\) at an elevation angle \(\theta = 30^\circ\). Standard sea-level gravitational acceleration is \(g = 9.8\text{ m/s}^2\). The artillery ballistician must determine: (1) the quadratic equation governing vertical altitude, (2) the maximum altitude (apogee), and (3) the exact time of impact with the sea.</p>

                <p><strong>Step 1: Formulate the Kinematic Trajectory Equation</strong><br>
                The initial vertical velocity component is:
                $$v_{y0} = v_0 \sin(\theta) = 150 \times \sin(30^\circ) = 150 \times 0.5 = 75\text{ m/s}$$
                Under Newton's laws of motion with constant gravity, vertical position \(y(t)\) as a function of time \(t\) satisfies:
                $$y(t) = y_0 + v_{y0} t - \frac{1}{2} g t^2 = 45 + 75t - 4.9t^2$$
                Rewriting in standard quadratic form \(a t^2 + b t + c = 0\) for sea-level impact (\(y = 0\)):
                $$-4.9 t^2 + 75 t + 45 = 0$$
                Here, \(a = -4.9\), \(b = 75\), and \(c = 45\).</p>

                <p><strong>Step 2: Calculate the Apogee (Parabola Vertex)</strong><br>
                The time to reach maximum altitude corresponds to the vertex time coordinate \(h\):
                $$t_{\text{apogee}} = -\frac{b}{2a} = -\frac{75}{2(-4.9)} = \frac{75}{9.8} \approx 7.653\text{ seconds}$$
                The peak altitude reached above sea level is the vertex height \(k\):
                $$y_{\max} = c - \frac{b^2}{4a} = 45 - \frac{75^2}{4(-4.9)} = 45 + \frac{5625}{19.6} = 45 + 287.0 \approx 332.0\text{ meters}$$</p>

                <p><strong>Step 3: Calculate the Discriminant and Flight Duration to Sea Level</strong><br>
                $$\Delta = b^2 - 4ac = 75^2 - 4(-4.9)(45) = 5625 + 882 = 6507$$
                Because \(\Delta > 0\), the equation possesses two real roots:
                $$\sqrt{\Delta} = \sqrt{6507} \approx 80.6659$$
                Applying the quadratic formula:
                $$t = \frac{-75 \pm 80.6659}{2(-4.9)} = \frac{-75 \pm 80.6659}{-9.8}$$
                Evaluating both branches:
                $$t_1 = \frac{-75 - 80.6659}{-9.8} = \frac{-155.6659}{-9.8} \approx +15.884\text{ seconds}$$
                $$t_2 = \frac{-75 + 80.6659}{-9.8} = \frac{5.6659}{-9.8} \approx -0.578\text{ seconds}$$
                The negative root \(t_2 = -0.578\text{ s}\) represents the mathematical extrapolation backwards in time to when a projectile fired from sea level would have passed the cliff height. The physical flight duration until splashdown is \(t_1 \approx 15.88\text{ seconds}\).</p>
              </div>
            </div>

            <h2>8. Frequently Asked Questions (FAQ)</h2>
            <div class="faq-accordion">
              <div class="faq-item">
                <h3 class="faq-question">What is the difference between quadratic roots and zeros of a function?</h3>
                <div class="faq-answer">
                  <p>The terms are closely related but technically distinct. The <em>zeros</em> of a function \(f(x)\) are the input values of \(x\) for which \(f(x) = 0\). The <em>roots</em> of an equation are the values of the variable that satisfy the equation \(f(x) = 0\). In practice for quadratic equations, finding the roots of \(ax^2 + bx + c = 0\) is mathematically identical to finding the zeros of the quadratic function \(f(x) = ax^2 + bx + c\).</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">Why can complex roots only appear in conjugate pairs?</h3>
                <div class="faq-answer">
                  <p>According to the Complex Conjugate Root Theorem, if a polynomial has purely real coefficients (\(a, b, c \in \mathbb{R}\)), any non-real complex roots must occur in conjugate pairs \(u + vi\) and \(u - vi\). This stems directly from the quadratic formula: the imaginary component arises entirely from \(\pm \sqrt{\Delta}\) when \(\Delta < 0\). The \(\pm\) sign enforces exact symmetry across the real axis in the complex plane.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">How do you solve a quadratic equation when \(b = 0\)?</h3>
                <div class="faq-answer">
                  <p>When the linear term vanishes (\(b = 0\)), the equation reduces to the pure quadratic form \(ax^2 + c = 0\). Subtracting \(c\) and dividing by \(a\) gives \(x^2 = -c/a\). Taking the square root directly yields \(x = \pm \sqrt{-c/a}\). If \(-c/a > 0\), the roots are real (\(\pm \sqrt{-c/a}\)). If \(-c/a < 0\), the roots are imaginary (\(\pm i\sqrt{c/a}\)). Completing the full quadratic formula is unnecessary in this simplified case.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">Can quadratic equations be solved using numerical algorithms?</h3>
                <div class="faq-answer">
                  <p>Yes. While analytical closed-form solutions are readily available via the quadratic formula, floating-point computers often encounter <em>catastrophic cancellation</em> when \(b^2 \gg 4ac\) and \(b > 0\), where computing \(-b + \sqrt{b^2 - 4ac}\) subtracts two nearly equal numbers, losing numerical precision. Numerically stable algorithms use the alternative Citardauq formula \(x_1 = \frac{2c}{-b - \operatorname{sgn}(b)\sqrt{b^2 - 4ac}}\) and compute the second root via Viète's relation \(x_2 = \frac{c}{a x_1}\).</p>
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
              <li><a href="pythagorean-theorem-calculator.html">Pythagorean Theorem Calculator</a></li>
              <li><a href="scientific-notation-calculator.html">Scientific Notation Calculator</a></li>
              <li><a href="significant-figures-calculator.html">Significant Figures Calculator</a></li>
              <li><a href="prime-number-calculator.html">Prime Number Calculator</a></li>
              <li><a href="fraction-calculator.html">Fraction Calculator</a></li>
              <li><a href="matrix-calculator.html">Matrix Calculator</a></li>
              <li><a href="standard-deviation-calculator.html">Standard Deviation Calculator</a></li>
            </ul>
          </div>

          <div class="sidebar-card">
            <h3 class="sidebar-title">Quadratic Identities</h3>
            <div style="font-size:0.875rem; line-height:1.5; color:var(--text-muted, #4b5563);">
              <p><strong>Formula:</strong> \(x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}\)</p>
              <p><strong>Discriminant:</strong> \(\Delta = b^2 - 4ac\)</p>
              <p><strong>Vertex:</strong> \(h = -\frac{b}{2a}, \; k = c - \frac{b^2}{4a}\)</p>
              <p><strong>Viète:</strong> \(x_1 + x_2 = -\frac{b}{a}, \; x_1 x_2 = \frac{c}{a}\)</p>
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
    function solveQuadratic() {
      const a = parseFloat(document.getElementById('coefA').value);
      const b = parseFloat(document.getElementById('coefB').value);
      const c = parseFloat(document.getElementById('coefC').value);

      if (isNaN(a) || isNaN(b) || isNaN(c)) return;

      if (Math.abs(a) < 1e-12) {
        document.getElementById('quadRootsPrimary').textContent = "Error: a cannot equal 0";
        document.getElementById('quadNatureSubtext').textContent = "Equation degenerates into linear form bx + c = 0";
        document.getElementById('resDelta').textContent = "N/A";
        document.getElementById('resVertex').textContent = "N/A (Linear)";
        document.getElementById('resAxis').textContent = "N/A";
        document.getElementById('resConcavity').textContent = "Linear Line";
        document.getElementById('quadStepsDisplay').innerHTML = "Leading coefficient a must be non-zero for quadratic analysis.";
        return;
      }

      const delta = (b * b) - (4 * a * c);
      const h = -b / (2 * a);
      const k = c - ((b * b) / (4 * a));

      document.getElementById('resDelta').textContent = delta.toFixed(4);
      document.getElementById('resVertex').textContent = `(${h.toFixed(3)}, ${k.toFixed(3)})`;
      document.getElementById('resAxis').textContent = `x = ${h.toFixed(4)}`;
      document.getElementById('resConcavity').textContent = a > 0 ? "Upward (a > 0)" : "Downward (a < 0)";

      let rootsText = "";
      let natureText = "";
      let stepsHtml = "";

      stepsHtml += `1. Standard Form: (${a})x² + (${b})x + (${c}) = 0<br>`;
      stepsHtml += `2. Discriminant: Δ = b² - 4ac = (${b})² - 4(${a})(${c}) = ${delta.toFixed(4)}<br>`;

      if (delta > 1e-12) {
        const sqrtDelta = Math.sqrt(delta);
        const x1 = (-b + sqrtDelta) / (2 * a);
        const x2 = (-b - sqrtDelta) / (2 * a);
        rootsText = `x₁ = ${x1.toFixed(4)}, x₂ = ${x2.toFixed(4)}`;
        natureText = "Two distinct real roots (parabola intersects x-axis twice)";
        stepsHtml += `3. Square root of discriminant: √Δ = ${sqrtDelta.toFixed(4)}<br>`;
        stepsHtml += `4. x₁ = (-(${b}) + ${sqrtDelta.toFixed(4)}) / (2 × ${a}) = ${x1.toFixed(4)}<br>`;
        stepsHtml += `5. x₂ = (-(${b}) - ${sqrtDelta.toFixed(4)}) / (2 × ${a}) = ${x2.toFixed(4)}`;
      } else if (Math.abs(delta) <= 1e-12) {
        const x = -b / (2 * a);
        rootsText = `x = ${x.toFixed(4)} (double root)`;
        natureText = "One repeated real root (parabola tangent to x-axis)";
        stepsHtml += `3. Discriminant Δ = 0 implies single double root.<br>`;
        stepsHtml += `4. x = -b / (2a) = -(${b}) / (2 × ${a}) = ${x.toFixed(4)}`;
      } else {
        const realPart = -b / (2 * a);
        const imagPart = Math.sqrt(Math.abs(delta)) / (2 * Math.abs(a));
        rootsText = `x = ${realPart.toFixed(4)} ± ${imagPart.toFixed(4)}i`;
        natureText = "Two complex conjugate roots (no real x-axis intersections)";
        stepsHtml += `3. Negative discriminant (Δ < 0) yields imaginary components.<br>`;
        stepsHtml += `4. Real part u = -b / (2a) = ${realPart.toFixed(4)}<br>`;
        stepsHtml += `5. Imaginary part v = √|Δ| / (2|a|) = ${imagPart.toFixed(4)}<br>`;
        stepsHtml += `6. Roots: ${realPart.toFixed(4)} + ${imagPart.toFixed(4)}i and ${realPart.toFixed(4)} - ${imagPart.toFixed(4)}i`;
      }

      document.getElementById('quadRootsPrimary').textContent = rootsText;
      document.getElementById('quadNatureSubtext').textContent = natureText;
      document.getElementById('quadStepsDisplay').innerHTML = stepsHtml;
    }

    document.getElementById('coefA').addEventListener('input', solveQuadratic);
    document.getElementById('coefB').addEventListener('input', solveQuadratic);
    document.getElementById('coefC').addEventListener('input', solveQuadratic);
    solveQuadratic();
  </script>
</body>
</html>
"""

# Write files
with open(os.path.join(BASE_DIR, 'gcd-lcm-calculator.html'), 'w', encoding='utf-8') as f:
    f.write(gcd_lcm_html)
print("Generated gcd-lcm-calculator.html successfully!")

with open(os.path.join(BASE_DIR, 'quadratic-equation-calculator.html'), 'w', encoding='utf-8') as f:
    f.write(quad_html)
print("Generated quadratic-equation-calculator.html successfully!")
