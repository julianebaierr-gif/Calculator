import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 1. EXPONENT CALCULATOR
# -------------------------------------------------------------
exp_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Exponent Calculator — Laws of Exponents, Powers & Scientific Bases | CalcHub</title>
  <meta name="description" content="Calculate base raised to power (bⁿ), negative exponents (b⁻ⁿ = 1/bⁿ), fractional powers, and review the seven canonical laws of exponents.">
  <meta name="keywords" content="exponent calculator, power calculator, negative exponent, fractional exponent, laws of exponents, base and power, compound interest, exponential growth">
  <meta name="author" content="CalcHub Real Analysis & Exponential Dynamics Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/exponent-calculator.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="Exponent Calculator — Laws of Exponents, Powers & Scientific Bases | CalcHub">
  <meta property="og:description" content="Compute powers bⁿ with integer, negative, and fractional exponents, complete with scientific notation and step-by-step exponent laws.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/exponent-calculator.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/exponent-calculator.html#app",
      "name": "Exponential Power & Exponent Law Engine",
      "url": "https://calchub.org/exponent-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "High-precision calculator evaluating powers with integer, fractional, and negative exponents using canonical exponent laws."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Math & Engineering Calculators", "item": "https://calchub.org/math.html"},
        {"@type": "ListItem", "position": 3, "name": "Exponent Calculator", "item": "https://calchub.org/exponent-calculator.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Why is any non-zero number raised to the power of zero equal to 1?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "By the Quotient Law of exponents, bᵐ / bⁿ = bᵐ⁻ⁿ. When m = n, the quotient divides a number by itself: bᵐ / bᵐ = 1. Simultaneously applying the exponent rule yields: bᵐ / bᵐ = bᵐ⁻ᵐ = b⁰. Equating both results proves that b⁰ = 1 for any non-zero base b. The expression 0⁰ is mathematically indeterminate."
          }
        },
        {
          "@type": "Question",
          "name": "How are negative exponents interpreted algebraically?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A negative exponent represents the multiplicative inverse (reciprocal) of the base raised to the positive power: b⁻ⁿ = 1 / bⁿ. For example, 2⁻³ = 1 / 2³ = 1 / 8 = 0.125. Negative exponents allow division to be expressed as multiplication, simplifying calculus derivatives and polynomial manipulations."
          }
        },
        {
          "@type": "Question",
          "name": "What is the meaning of a fractional or rational exponent like b^(p/q)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A fractional exponent represents both an integer power and a radical root simultaneously: b^(p/q) = ⁿ√(bᵖ) = (ⁿ√b)ᵖ. The numerator p dictates the power to which the base is raised, while the denominator q indicates the index of the radical root. For example, 8^(2/3) = (∛8)² = 2² = 4."
          }
        },
        {
          "@type": "Question",
          "name": "Where is exponentiation applied in computing and cryptography?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In digital computer architecture, addressing spaces scale exponentially as 2ⁿ (e.g., 2³² ≈ 4.29 billion memory addresses in a 32-bit CPU, while 2⁶⁴ ≈ 1.84 × 10¹⁹ bytes in 64-bit systems). In asymmetric cryptography (RSA and Diffie-Hellman), security relies on modular exponentiation (c = mᵉ mod n), which can be computed in logarithmic time via repeated squaring, while inverting it requires discrete logarithms."
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
            <div class="badge-tag">Algebraic Powers &amp; Exponential Dynamics</div>
            <h1 class="tool-title">Exponent Calculator</h1>
            <p class="tool-subtitle">Calculate any base raised to a power (\(b^n\)), negative reciprocals, fractional roots, and explore the seven canonical laws of exponents.</p>
          </header>

          <section class="calculator-card" aria-label="Exponent Solver">
            <div class="calc-grid">
              <div class="input-group">
                <label for="baseVal" class="input-label">Base (\(b\))</label>
                <input type="number" id="baseVal" class="calc-input" value="2" step="any">
              </div>

              <div class="input-group">
                <label for="expVal" class="input-label">Exponent (\(n\))</label>
                <input type="number" id="expVal" class="calc-input" value="10" step="any">
              </div>
            </div>

            <div class="primary-result" style="margin-top: 25px;">
              <div class="result-label">Calculated Power (\(b^n\))</div>
              <div class="result-value" id="resPowerPrimary">1,024</div>
              <div class="result-subtext" id="resPowerSubtext">2¹⁰ = 1,024</div>
            </div>

            <div class="results-grid" style="margin-top: 20px;">
              <div class="result-item">
                <div class="result-label">Scientific Notation</div>
                <div class="result-value" id="resExpSci">1.0240 × 10³</div>
              </div>
              <div class="result-item">
                <div class="result-label">Negative Reciprocal (\(b^{-n}\))</div>
                <div class="result-value" id="resReciprocal">0.00097656</div>
              </div>
              <div class="result-item">
                <div class="result-label">Natural Log of Result (\(\ln(b^n)\))</div>
                <div class="result-value" id="resNatLog">6.9315</div>
              </div>
              <div class="result-item">
                <div class="result-label">Radical Equivalent</div>
                <div class="result-value" id="resRadical">2¹⁰</div>
              </div>
            </div>

            <div class="conversion-steps" style="margin-top: 25px;">
              <h3>Step-by-Step Exponent Evaluation</h3>
              <div id="expStepsDisplay" style="font-family: monospace; font-size: 0.95rem; line-height: 1.6; background: rgba(0,0,0,0.03); padding: 16px; border-radius: 8px; border-left: 4px solid var(--accent, #2563eb);">
                Loading calculation steps...
              </div>
            </div>
          </section>

          <article class="article-body">
            <h2>1. Axiomatic Principles of Exponentiation</h2>
            <p>In elementary arithmetic and abstract algebra, <strong>exponentiation</strong> represents a mathematical operation involving two numbers: the <strong>base</strong> \(b\) and the <strong>exponent</strong> (or power) \(n\), written symbolically as \(b^n\). When \(n\) is a positive integer, exponentiation corresponds to repeated multiplication:</p>

            $$b^n = \underbrace{b \times b \times b \times \dots \times b}_{n \text{ factors}}$$

            <p>From this foundational definition, the domain of the exponent \(n\) extends systematically through the real numbers \(\mathbb{R}\) and complex numbers \(\mathbb{C}\) by enforcing algebraic consistency:</p>

            <h3>1.1 Zero Exponent Principle</h3>
            <p>For any non-zero base \(b \neq 0\), raising to the zero power yields identically 1:</p>

            $$b^0 = 1 \quad (\forall b \in \mathbb{R}, \; b \neq 0)$$

            <p><strong>Proof:</strong> By the quotient rule of exponents, \(\frac{b^k}{b^k} = b^{k - k} = b^0\). Because any non-zero quantity divided by itself equals 1, it follows that \(b^0 = 1\). The expression \(0^0\) is mathematically undefined (indeterminate in calculus limits, though defined as 1 in discrete combinatorics to preserve the binomial theorem).</p>

            <h3>1.2 Negative Exponent Principle</h3>
            <p>A negative exponent indicates repeated division or the multiplicative reciprocal of the positive power:</p>

            $$b^{-n} = \frac{1}{b^n} \quad (b \neq 0)$$

            <p>For example, \(10^{-3} = \frac{1}{10^3} = \frac{1}{1000} = 0.001\). In physical systems, negative exponents express microscopic quantities (such as the wavelength of light or electron mass).</p>

            <h3>1.3 Rational and Fractional Exponents</h3>
            <p>When the exponent is a rational fraction \(\frac{p}{q}\) (with \(q \in \mathbb{Z}^+\)), exponentiation combines an integer power with a radical root:</p>

            $$b^{p/q} = \sqrt[q]{b^p} = \left(\sqrt[q]{b}\right)^p$$

            <p>For instance, \(27^{2/3} = (\sqrt[3]{27})^2 = 3^2 = 9\). If the base \(b\) is negative and the root denominator \(q\) is even (such as \((-4)^{1/2} = \sqrt{-4}\)), the result exits the real number field and yields an imaginary number (\(2i\)).</p>

            <h2>2. The Seven Canonical Laws of Exponents</h2>
            <p>Mathematical calculations adhere to seven universal exponent rules that dictate algebraic manipulation across science and engineering:</p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>Law Name</th>
                  <th>Algebraic Identity</th>
                  <th>Example Application</th>
                  <th>Physical Significance</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>1. Product Law</td>
                  <td>\(b^m \cdot b^n = b^{m+n}\)</td>
                  <td>\(2^3 \cdot 2^4 = 2^7 = 128\)</td>
                  <td>Combining orders of magnitude</td>
                </tr>
                <tr>
                  <td>2. Quotient Law</td>
                  <td>\(\frac{b^m}{b^n} = b^{m-n}\)</td>
                  <td>\(\frac{5^6}{5^2} = 5^4 = 625\)</td>
                  <td>Relative magnitude ratios</td>
                </tr>
                <tr>
                  <td>3. Power of a Power</td>
                  <td>\((b^m)^n = b^{m \cdot n}\)</td>
                  <td>\((3^2)^3 = 3^6 = 729\)</td>
                  <td>Multi-stage compounding</td>
                </tr>
                <tr>
                  <td>4. Power of a Product</td>
                  <td>\((a \cdot b)^n = a^n \cdot b^n\)</td>
                  <td>\((2 \cdot 5)^3 = 2^3 \cdot 5^3 = 1000\)</td>
                  <td>Dimensional scaling</td>
                </tr>
                <tr>
                  <td>5. Power of a Quotient</td>
                  <td>\(\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n}\)</td>
                  <td>\(\left(\frac{3}{4}\right)^2 = \frac{9}{16}\)</td>
                  <td>Scaling volumetric densities</td>
                </tr>
                <tr>
                  <td>6. Negative Exponent</td>
                  <td>\(b^{-n} = \frac{1}{b^n}\)</td>
                  <td>\(4^{-2} = \frac{1}{16} = 0.0625\)</td>
                  <td>Reciprocal attenuation</td>
                </tr>
                <tr>
                  <td>7. Fractional Exponent</td>
                  <td>\(b^{m/n} = \sqrt[n]{b^m}\)</td>
                  <td>\(16^{3/4} = (\sqrt[4]{16})^3 = 8\)</td>
                  <td>Allometric geometric roots</td>
                </tr>
              </tbody>
            </table>

            <h2>3. Continuous and Real Exponentiation via Euler's Number (\(e\))</h2>
            <p>In advanced calculus and differential equations, exponentiation with an arbitrary real base \(b > 0\) and real power \(x \in \mathbb{R}\) is formally defined through the natural exponential function and the natural logarithm:</p>

            $$b^x = e^{x \ln(b)}$$

            <p>This definition allows calculus to compute derivatives and integrals of exponential functions seamlessly:</p>

            $$\frac{d}{dx}\left(b^x\right) = \frac{d}{dx}\left(e^{x \ln b}\right) = \ln(b) \cdot e^{x \ln b} = b^x \ln(b)$$

            <p>When the base is Euler's constant (\(b = e \approx 2.7182818\dots\)), \(\ln(e) = 1\), making \(e^x\) uniquely the only mathematical function that is identically equal to its own derivative (\(\frac{d}{dx} e^x = e^x\)).</p>

            <h2>4. Engineering, Financial, and Cryptographic Applications</h2>

            <h3>4.1 Financial Compound Growth and the Continuum Limit</h3>
            <p>An investment principal \(P\) compounding at an annual interest rate \(r\) partitioned into \(k\) compounding intervals per year matures over \(t\) years according to:</p>

            $$A(t) = P \left(1 + \frac{r}{k}\right)^{k \cdot t}$$

            <p>As the frequency of compounding approaches infinity (\(k \to \infty\)), the limit converges to continuous exponential growth: \(A(t) = P e^{rt}\).</p>

            <h3>4.2 Computer Science: Binary Addressing Spaces</h3>
            <p>In digital computer hardware, a memory bus with \(N\) address lines can address exactly \(2^N\) discrete memory locations. An 8-bit register addresses \(2^8 = 256\) bytes; a 32-bit architecture addresses \(2^{32} = 4,294,967,296\text{ bytes} = 4\text{ GB}\); and a modern 64-bit architecture can address \(2^{64} \approx 1.84467 \times 10^{19}\text{ bytes} \approx 18.4\text{ Exabytes}\).</p>

            <h2>5. Benchmark Comparative Reference Table</h2>
            <p>The table below catalogues benchmark exponential calculations, illustrating the base \(b\), exponent \(n\), algebraic nature, and exact output.</p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>Base (\(b\))</th>
                  <th>Exponent (\(n\))</th>
                  <th>Mathematical Expression</th>
                  <th>Result Value</th>
                  <th>Scientific Notation</th>
                  <th>Category</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>2</td>
                  <td>10</td>
                  <td>\(2^{10}\)</td>
                  <td>1,024</td>
                  <td>\(1.024 \times 10^3\)</td>
                  <td>Binary Kibi (\(1\text{ KiB}\))</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>-3</td>
                  <td>\(2^{-3} = 1/8\)</td>
                  <td>0.125</td>
                  <td>\(1.250 \times 10^{-1}\)</td>
                  <td>Negative Integer</td>
                </tr>
                <tr>
                  <td>10</td>
                  <td>6</td>
                  <td>\(10^6\)</td>
                  <td>1,000,000</td>
                  <td>\(1.000 \times 10^6\)</td>
                  <td>Metric Mega (M)</td>
                </tr>
                <tr>
                  <td>10</td>
                  <td>-9</td>
                  <td>\(10^{-9}\)</td>
                  <td>0.000 000 001</td>
                  <td>\(1.000 \times 10^{-9}\)</td>
                  <td>Metric Nano (n)</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>0</td>
                  <td>\(5^0\)</td>
                  <td>1</td>
                  <td>\(1.000 \times 10^0\)</td>
                  <td>Zero Exponent</td>
                </tr>
                <tr>
                  <td>16</td>
                  <td>0.5</td>
                  <td>\(16^{1/2} = \sqrt{16}\)</td>
                  <td>4</td>
                  <td>\(4.000 \times 10^0\)</td>
                  <td>Square Root</td>
                </tr>
                <tr>
                  <td>27</td>
                  <td>0.3333</td>
                  <td>\(27^{1/3} = \sqrt[3]{27}\)</td>
                  <td>3</td>
                  <td>\(3.000 \times 10^0\)</td>
                  <td>Cube Root</td>
                </tr>
                <tr>
                  <td>-3</td>
                  <td>4</td>
                  <td>\((-3)^4\)</td>
                  <td>81</td>
                  <td>\(8.100 \times 10^1\)</td>
                  <td>Negative Base (Even Power)</td>
                </tr>
                <tr>
                  <td>-3</td>
                  <td>3</td>
                  <td>\((-3)^3\)</td>
                  <td>-27</td>
                  <td>\(-2.700 \times 10^1\)</td>
                  <td>Negative Base (Odd Power)</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>32</td>
                  <td>\(2^{32}\)</td>
                  <td>4,294,967,296</td>
                  <td>\(4.295 \times 10^9\)</td>
                  <td>32-bit Integer Cap</td>
                </tr>
              </tbody>
            </table>

            <h2>6. Worked Cryptographic Case Study: 256-Bit Symmetric Key Security</h2>
            <div class="worked-example-card">
              <div class="example-header">
                <strong>Cyber-Security Case Study:</strong> AES-256 Brute-Force Key Space Entropy Evaluation
              </div>
              <div class="example-body">
                <p><strong>Scenario:</strong> A cyber-security cryptographer explains the mathematical impossibility of brute-forcing the Advanced Encryption Standard (AES) with a 256-bit key length. The key consists of a sequence of 256 binary bits, each of which can be either 0 or 1. The engineer must: (1) calculate the total possible key combinations \(K = 2^{256}\), (2) express the keyspace in scientific notation, and (3) determine how long a supercomputing cluster testing \(10^{18}\text{ keys/second}\) would require to check the keyspace.</p>

                <p><strong>Step 1: Express Total Keyspace via Base 2 Exponentiation</strong><br>
                $$K = 2^{256}$$</p>

                <p><strong>Step 2: Convert Base 2 to Base 10 Power using Logarithms</strong><br>
                Recall that \(2 = 10^{\log_{10}(2)}\), where \(\log_{10}(2) \approx 0.30102999566\).
                $$K = \left(10^{0.30103}\right)^{256} = 10^{256 \times 0.30102999566} = 10^{77.06368}$$
                Decomposing the decimal exponent:
                $$K = 10^{0.06368} \times 10^{77} \approx 1.15792 \times 10^{77}\text{ combinations}$$</p>

                <p><strong>Step 3: Evaluate Brute-Force Search Duration</strong><br>
                An exascale supercomputer testing \(10^{18}\text{ keys/sec}\) checks:
                $$\text{Keys/Year} = 10^{18} \times (365.25 \times 86400\text{ s}) \approx 3.15576 \times 10^{25}\text{ keys/year}$$
                The time required to exhaust the keyspace is:
                $$T = \frac{1.15792 \times 10^{77}}{3.15576 \times 10^{25}} \approx 3.669 \times 10^{51}\text{ years}$$
                Because the current age of the universe is approximately \(1.38 \times 10^{10}\text{ years}\), cracking AES-256 by brute-force is physically impossible under known laws of thermodynamics.</p>
              </div>
            </div>

            <h2>7. Frequently Asked Questions (FAQ)</h2>
            <div class="faq-accordion">
              <div class="faq-item">
                <h3 class="faq-question">What is the difference between -2^4 and (-2)^4?</h3>
                <div class="faq-answer">
                  <p>In standard mathematical order of operations (PEMDAS/BODMAS), exponentiation has higher precedence than negation (multiplication by -1). Therefore, \(-2^4 = -(2^4) = -(16) = -16\). In contrast, \((-2)^4\) encloses the negative sign within the base: \((-2) \times (-2) \times (-2) \times (-2) = +16\). Parentheses are essential when raising negative numbers to powers.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">Why does (b^m)^n equal b^(m·n) while b^(m^n) evaluates from the top down?</h3>
                <div class="faq-answer">
                  <p>Parentheses enforce grouping: \((b^m)^n\) means taking \(b^m\) and multiplying it by itself \(n\) times, yielding \(b^{m \cdot n}\). Without parentheses, tower exponentiation \(b^{m^n}\) is right-associative by international convention: it is evaluated from the top down as \(b^{(m^n)}\). For example, \((2^3)^2 = 8^2 = 64\), whereas \(2^{3^2} = 2^9 = 512\).</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">Can an exponent be an irrational number like 2^√2?</h3>
                <div class="faq-answer">
                  <p>Yes. Exponentiation with irrational powers is defined rigorously through sequences of rational approximations: \(2^{\sqrt{2}} = \lim_{q \to \sqrt{2}} 2^q\). Because \(\sqrt{2} \approx 1.4142135...\), the value is bounded between rational powers: \(2^{1.4} < 2^{\sqrt{2}} < 2^{1.5}\). Analytically, \(2^{\sqrt{2}} = e^{\sqrt{2} \ln(2)} \approx 2.665144\).</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">How does exponentiation differ from tetration?</h3>
                <div class="faq-answer">
                  <p>Exponentiation represents repeated multiplication (level 3 hyperoperation). <em>Tetration</em> represents repeated exponentiation (level 4 hyperoperation), written as \(^n b = \underbrace{b^{b^{b^{\dots}}}}_{n \text{ copies of } b}\). Tetration produces monstrous growth rates that eclipse standard exponential curves.</p>
                </div>
              </div>
            </div>
          </article>
        </div>

        <aside class="sidebar-column">
          <div class="sidebar-card">
            <h3 class="sidebar-title">Related Math Calculators</h3>
            <ul class="sidebar-nav">
              <li><a href="scientific-notation-calculator.html">Scientific Notation Calculator</a></li>
              <li><a href="cube-root-calculator.html">Cube Root Calculator</a></li>
              <li><a href="quadratic-equation-calculator.html">Quadratic Equation Calculator</a></li>
              <li><a href="pythagorean-theorem-calculator.html">Pythagorean Theorem Calculator</a></li>
              <li><a href="gcd-lcm-calculator.html">GCD and LCM Calculator</a></li>
              <li><a href="significant-figures-calculator.html">Significant Figures Calculator</a></li>
              <li><a href="percentage-calculator.html">Percentage Calculator</a></li>
              <li><a href="fraction-calculator.html">Fraction Calculator</a></li>
            </ul>
          </div>

          <div class="sidebar-card">
            <h3 class="sidebar-title">Exponent Rules</h3>
            <div style="font-size:0.875rem; line-height:1.5; color:var(--text-muted, #4b5563);">
              <p><strong>Product:</strong> \(b^m \cdot b^n = b^{m+n}\)</p>
              <p><strong>Quotient:</strong> \(b^m / b^n = b^{m-n}\)</p>
              <p><strong>Power:</strong> \((b^m)^n = b^{mn}\)</p>
              <p><strong>Negative:</strong> \(b^{-n} = 1/b^n\)</p>
              <p><strong>Zero:</strong> \(b^0 = 1 \quad (b \neq 0)\)</p>
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
    function calcExponent() {
      const b = parseFloat(document.getElementById('baseVal').value);
      const n = parseFloat(document.getElementById('expVal').value);

      if (isNaN(b) || isNaN(n)) return;

      const res = Math.pow(b, n);
      const recip = Math.pow(b, -n);

      let primaryText = "";
      if (isNaN(res)) {
        primaryText = "NaN (Complex / Undefined)";
      } else if (!isFinite(res)) {
        primaryText = "Overflow (Infinity)";
      } else if (Math.abs(res) >= 1e12 || (Math.abs(res) < 1e-4 && res !== 0)) {
        primaryText = res.toExponential(6);
      } else {
        primaryText = Number.isInteger(res) ? res.toLocaleString() : res.toFixed(6);
      }

      document.getElementById('resPowerPrimary').textContent = primaryText;
      document.getElementById('resPowerSubtext').textContent = `${b}^(${n}) = ${primaryText}`;

      document.getElementById('resExpSci').textContent = isFinite(res) && !isNaN(res) ? res.toExponential(4) : "N/A";
      document.getElementById('resReciprocal').textContent = isFinite(recip) && !isNaN(recip) ? (Math.abs(recip) < 1e-4 ? recip.toExponential(6) : recip.toFixed(8)) : "N/A";
      
      const lnVal = (b > 0 && isFinite(res) && res > 0) ? (n * Math.log(b)).toFixed(4) : "Undefined (b ≤ 0)";
      document.getElementById('resNatLog').textContent = lnVal;
      document.getElementById('resRadical').textContent = n % 1 !== 0 ? `(${b})^(${n})` : `${b}^${n}`;

      let steps = `1. Base b = ${b}; Exponent n = ${n}<br>`;
      if (n === 0) {
        steps += `2. Zero Exponent Rule: b⁰ = 1 for any non-zero base.<br>3. Result: 1`;
      } else if (n < 0) {
        steps += `2. Negative Exponent Rule: b⁻ⁿ = 1 / bⁿ<br>`;
        steps += `3. Evaluate denominator: (${b})^${Math.abs(n)} = ${Math.pow(b, Math.abs(n))}<br>`;
        steps += `4. Result: 1 / ${Math.pow(b, Math.abs(n))} = ${res}`;
      } else {
        steps += `2. Power evaluation: (${b})^${n}<br>`;
        steps += `3. Natural log identity: e^(${n} × ln(${b})) = ${primaryText}`;
      }

      document.getElementById('expStepsDisplay').innerHTML = steps;
    }

    document.getElementById('baseVal').addEventListener('input', calcExponent);
    document.getElementById('expVal').addEventListener('input', calcExponent);
    calcExponent();
  </script>
</body>
</html>
"""

# -------------------------------------------------------------
# 2. FACTORIAL CALCULATOR
# -------------------------------------------------------------
fact_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Factorial Calculator — n!, Permutations, Combinations & Stirling | CalcHub</title>
  <meta name="description" content="Calculate factorial n!, permutations P(n, r), combinations C(n, r), Stirling's asymptotic approximation, Euler's Gamma function, and Pascal identities.">
  <meta name="keywords" content="factorial calculator, n factorial, permutations calculator, combinations calculator, stirlings approximation, gamma function, zero factorial, combinatorics">
  <meta name="author" content="CalcHub Combinatorics & Asymptotic Analysis Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/factorial-calculator.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="Factorial Calculator — n!, Permutations, Combinations & Stirling | CalcHub">
  <meta property="og:description" content="Calculate exact factorials n!, permutations P(n,r), combinations C(n,r), and Stirling's asymptotic formula with complete combinatorics.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/factorial-calculator.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/factorial-calculator.html#app",
      "name": "Factorial & Combinatorial Mathematics Engine",
      "url": "https://calchub.org/factorial-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "High-precision combinatorics calculator computing n!, permutations P(n,r), combinations C(n,r), and Stirling's asymptotic formula."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Math & Engineering Calculators", "item": "https://calchub.org/math.html"},
        {"@type": "ListItem", "position": 3, "name": "Factorial Calculator", "item": "https://calchub.org/factorial-calculator.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Why is zero factorial (0!) equal to 1?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Algebraically, the recursive definition of factorials dictates that n! = n · (n - 1)!. Setting n = 1 yields: 1! = 1 · (0)!. Since 1! = 1, dividing by 1 gives 0! = 1. Combinatorially, n! represents the number of distinct ways to arrange n objects in an ordered sequence. For an empty set (n = 0), there is exactly one way to arrange nothing (the empty arrangement), establishing 0! = 1."
          }
        },
        {
          "@type": "Question",
          "name": "What is Stirling's Approximation and when is it utilized?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Stirling's Formula provides an asymptotic approximation for factorials of large numbers: n! ≈ √(2πn) · (n / e)ⁿ. Because calculating exact factorials for large values (like 1000!) causes numerical overflow in computers, Stirling's logarithmic formula ln(n!) ≈ n·ln(n) - n is universally utilized in statistical mechanics, entropy calculations, and thermal physics."
          }
        },
        {
          "@type": "Question",
          "name": "How do permutations P(n, r) differ from combinations C(n, r)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Permutations P(n, r) = n! / (n - r)! count the number of ordered arrangements of r items chosen from n available items (order matters, such as race finishing podiums or PIN codes). Combinations C(n, r) = n! / [r! · (n - r)!] count the number of unordered selections (order does not matter, such as lottery numbers or poker card hands)."
          }
        },
        {
          "@type": "Question",
          "name": "How does Euler's Gamma function extend factorials to non-integers and fractions?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Leonhard Euler defined the Gamma function via the continuous integral Γ(z) = ∫₀^∞ t^(z-1) · e^(-t) dt. Integrating by parts proves Γ(z + 1) = z · Γ(z). For positive integers, Γ(n + 1) = n!. Furthermore, Euler evaluated half-integers: Γ(1/2) = √π, which allows the computation of fractional factorials such as (1/2)! = 0.5 · √π ≈ 0.886227."
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
            <div class="badge-tag">Combinatorics &amp; Asymptotic Analysis</div>
            <h1 class="tool-title">Factorial Calculator</h1>
            <p class="tool-subtitle">Calculate exact factorials \(n!\), permutations \(P(n, r)\), combinations \(C(n, r)\), and evaluate Stirling's asymptotic approximation.</p>
          </header>

          <section class="calculator-card" aria-label="Factorial Solver">
            <div class="calc-grid">
              <div class="input-group">
                <label for="factN" class="input-label">Total Elements (\(n\))</label>
                <input type="number" id="factN" class="calc-input" value="10" min="0" max="170" step="1">
              </div>

              <div class="input-group">
                <label for="factR" class="input-label">Subset Selection (\(r\))</label>
                <input type="number" id="factR" class="calc-input" value="4" min="0" max="170" step="1">
              </div>
            </div>

            <div class="primary-result" style="margin-top: 25px;">
              <div class="result-label">Computed Factorial (\(n!\))</div>
              <div class="result-value" id="resFactorialPrimary">3,628,800</div>
              <div class="result-subtext" id="resFactorialSubtext">10! = 10 × 9 × 8 × ... × 1 = 3,628,800</div>
            </div>

            <div class="results-grid" style="margin-top: 20px;">
              <div class="result-item">
                <div class="result-label">Permutations \(P(n, r)\)</div>
                <div class="result-value" id="resPermutations">5,040</div>
              </div>
              <div class="result-item">
                <div class="result-label">Combinations \(C(n, r)\)</div>
                <div class="result-value" id="resCombinations">210</div>
              </div>
              <div class="result-item">
                <div class="result-label">Stirling's Approximation</div>
                <div class="result-value" id="resStirling">3,598,695.6</div>
              </div>
              <div class="result-item">
                <div class="result-label">Scientific Notation</div>
                <div class="result-value" id="resFactSci">3.6288 × 10⁶</div>
              </div>
            </div>

            <div class="conversion-steps" style="margin-top: 25px;">
              <h3>Combinatorial Formulas &amp; Expansions</h3>
              <div id="factStepsDisplay" style="font-family: monospace; font-size: 0.95rem; line-height: 1.6; background: rgba(0,0,0,0.03); padding: 16px; border-radius: 8px; border-left: 4px solid var(--accent, #2563eb);">
                Loading combinatorial steps...
              </div>
            </div>
          </section>

          <article class="article-body">
            <h2>1. Foundations of Factorials in Discrete Mathematics</h2>
            <p>In discrete mathematics, combinatorics, and probability theory, the <strong>factorial</strong> of a non-negative integer \(n\), denoted by the exclamation mark symbol \(n!\) (introduced by French mathematician Christian Kramp in 1808), represents the product of all positive integers less than or equal to \(n\):</p>

            $$n! = \prod_{k=1}^n k = n \times (n - 1) \times (n - 2) \times \dots \times 3 \times 2 \times 1$$

            <p>The factorial operation is defined recursively by the difference equation:</p>

            $$n! = n \times (n - 1)! \quad \text{for } n \ge 1$$

            <p>with the fundamental initial boundary condition:</p>

            $$0! = 1$$

            <h3>1.1 Rigorous Mathematical Proofs that \(0! = 1\)</h3>
            <p>The identity \(0! = 1\) is often considered counterintuitive, but it is mathematically mandatory for three distinct reasons:</p>
            <ol>
              <li><strong>Algebraic Consistency:</strong> Rearranging the recursive definition gives \((n - 1)! = \frac{n!}{n}\). Substituting \(n = 1\):
                $$0! = (1 - 1)! = \frac{1!}{1} = \frac{1}{1} = 1$$
                If \(0!\) were defined as 0, evaluating \((n-1)!\) would induce catastrophic division by zero across all higher factorials.</li>
              <li><strong>Combinatorial Permutations of the Empty Set:</strong> The quantity \(n!\) counts the number of distinct ways to arrange \(n\) items in an ordered queue. An empty set (\(\emptyset\)) containing zero elements has exactly one unique arrangement: the trivial empty arrangement. Thus, \(0! = 1\).</li>
              <li><strong>The Empty Product Convention:</strong> In mathematical algebra, the empty product of zero factors is universally defined as the multiplicative identity element (1), just as an empty sum equals the additive identity element (0).</li>
            </ol>

            <h2>2. Permutations and Combinations in Enumerative Combinatorics</h2>
            <p>Factorials form the mathematical engine underlying all counting problems where subsets of size \(r\) are selected from a universe of size \(n\).</p>

            <h3>2.1 Permutations: Order-Dependent Arrangements</h3>
            <p>A <strong>permutation</strong> counts the number of ways to select and arrange \(r\) elements from a set of \(n\) distinct elements, where the sequence order matters (such as podium places in an Olympic sprint, horse race trifectas, or alphanumeric passwords):</p>

            $$P(n, r) = {}_n P_r = \frac{n!}{(n - r)!} = n \times (n - 1) \times \dots \times (n - r + 1)$$

            <p>When all \(n\) elements are arranged (\(r = n\)), \(P(n, n) = \frac{n!}{0!} = \frac{n!}{1} = n!\).</p>

            <h3>2.2 Combinations: Unordered Subsets</h3>
            <p>A <strong>combination</strong> counts the number of ways to select \(r\) elements from \(n\) distinct elements, where the arrangement order does not matter (such as drawing 5 cards in poker, selecting lottery balls, or choosing a committee of delegates):</p>

            $$C(n, r) = \binom{n}{r} = \frac{P(n, r)}{r!} = \frac{n!}{r! (n - r)!}$$

            <p>The binomial coefficients \(\binom{n}{r}\) form the rows of <em>Pascal's Triangle</em> and govern the algebraic expansion of polynomials via the Binomial Theorem:</p>

            $$(x + y)^n = \sum_{k=0}^n \binom{n}{k} x^{n - k} y^k$$

            <h2>3. Euler's Gamma Function: Extending Factorials to the Complex Plane</h2>
            <p>In standard arithmetic, factorials are restricted to integer inputs. In 1729, Leonhard Euler solved the problem of interpolating factorials across continuous real and complex numbers by introducing the <strong>Gamma Function</strong> \(\Gamma(z)\):</p>

            $$\Gamma(z) = \int_0^\infty t^{z - 1} e^{-t} \, dt \quad (\operatorname{Re}(z) > 0)$$

            <p>Using integration by parts, Euler proved the fundamental functional recurrence relation:</p>

            $$\Gamma(z + 1) = z \cdot \Gamma(z)$$

            <p>For any positive integer \(n\), iterating this relation reveals that the Gamma function shifts the factorial by exactly one:</p>

            $$\Gamma(n + 1) = n! \iff n! = \Gamma(n + 1)$$

            <h3>3.1 Half-Integer Factorials and \(\sqrt{\pi}\)</h3>
            <p>Evaluating Euler's integral at \(z = \frac{1}{2}\) transforms via Gaussian integration into:</p>

            $$\Gamma\left(\frac{1}{2}\right) = \int_0^\infty t^{-1/2} e^{-t} \, dt = \sqrt{\pi}$$

            <p>Consequently, fractional factorials are exact multiples of \(\sqrt{\pi}\):</p>

            $$\left(\frac{1}{2}\right)! = \Gamma\left(\frac{3}{2}\right) = \frac{1}{2} \Gamma\left(\frac{1}{2}\right) = \frac{\sqrt{\pi}}{2} \approx 0.8862269$$

            $$\left(\frac{3}{2}\right)! = \frac{3}{2} \left(\frac{1}{2}\right)! = \frac{3\sqrt{\pi}}{4} \approx 1.3293403$$

            <h2>4. Stirling's Asymptotic Approximation</h2>
            <p>As \(n\) increases, \(n!\) grows with astonishing speed, eclipsing exponential growth. In statistical physics and thermodynamics, Scottish mathematician James Stirling derived an asymptotic formula for large \(n\):</p>

            $$n! \sim \sqrt{2\pi n} \left(\frac{n}{e}\right)^n \quad \text{as } n \to \infty$$

            <p>Taking the natural logarithm yields the form indispensable in statistical mechanics (Boltzmann's entropy equation \(S = k_B \ln \Omega\)):</p>

            $$\ln(n!) \approx n \ln(n) - n + \frac{1}{2}\ln(2\pi n) \approx n \ln(n) - n$$

            <p>Stirling's approximation achieves high precision rapidly: for \(n = 10\), the approximation error is less than \(0.8\%\); for \(n = 100\), the error drops below \(0.08\%\).</p>

            <h2>5. Benchmark Comparative Reference Table</h2>
            <p>The table below catalogues factorials from \(0!\) through \(15!\), illustrating exact values, scientific representations, and Stirling approximations.</p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>\(n\)</th>
                  <th>Exact Factorial (\(n!\))</th>
                  <th>Scientific Notation</th>
                  <th>Stirling Approximation</th>
                  <th>Relative Error</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>0</td>
                  <td>1</td>
                  <td>\(1.000 \times 10^0\)</td>
                  <td>N/A</td>
                  <td>0.00%</td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>1</td>
                  <td>\(1.000 \times 10^0\)</td>
                  <td>\(0.922\)</td>
                  <td>-7.79%</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>2</td>
                  <td>\(2.000 \times 10^0\)</td>
                  <td>\(1.919\)</td>
                  <td>-4.05%</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>6</td>
                  <td>\(6.000 \times 10^0\)</td>
                  <td>\(5.836\)</td>
                  <td>-2.73%</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>24</td>
                  <td>\(2.400 \times 10^1\)</td>
                  <td>\(23.506\)</td>
                  <td>-2.06%</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>120</td>
                  <td>\(1.200 \times 10^2\)</td>
                  <td>\(118.019\)</td>
                  <td>-1.65%</td>
                </tr>
                <tr>
                  <td>6</td>
                  <td>720</td>
                  <td>\(7.200 \times 10^2\)</td>
                  <td>\(710.078\)</td>
                  <td>-1.38%</td>
                </tr>
                <tr>
                  <td>7</td>
                  <td>5,040</td>
                  <td>\(5.040 \times 10^3\)</td>
                  <td>\(4,980.396\)</td>
                  <td>-1.18%</td>
                </tr>
                <tr>
                  <td>8</td>
                  <td>40,320</td>
                  <td>\(4.032 \times 10^4\)</td>
                  <td>\(39,902.395\)</td>
                  <td>-1.04%</td>
                </tr>
                <tr>
                  <td>9</td>
                  <td>362,880</td>
                  <td>\(3.629 \times 10^5\)</td>
                  <td>\(359,536.873\)</td>
                  <td>-0.92%</td>
                </tr>
                <tr>
                  <td>10</td>
                  <td>3,628,800</td>
                  <td>\(3.629 \times 10^6\)</td>
                  <td>\(3,598,695.619\)</td>
                  <td>-0.83%</td>
                </tr>
                <tr>
                  <td>12</td>
                  <td>479,001,600</td>
                  <td>\(4.790 \times 10^8\)</td>
                  <td>\(475,687,486.47\)</td>
                  <td>-0.69%</td>
                </tr>
                <tr>
                  <td>15</td>
                  <td>1,307,674,368,000</td>
                  <td>\(1.308 \times 10^{12}\)</td>
                  <td>\(1,300,430,722,199\)</td>
                  <td>-0.55%</td>
                </tr>
              </tbody>
            </table>

            <h2>6. Worked Probability Case Study: The 52-Card Deck Permutations</h2>
            <div class="worked-example-card">
              <div class="example-header">
                <strong>Probability & Information Theory Case Study:</strong> Total Combinations of a Shuffled Deck of Cards
              </div>
              <div class="example-body">
                <p><strong>Scenario:</strong> A casino statistician models the probability of card shuffling collisions. A standard deck of playing cards contains \(N = 52\text{ cards}\). The statistician must: (1) calculate the total permutations of arrangements in a shuffled deck (\(52!\)), (2) express the result in scientific notation using Stirling's approximation, and (3) calculate the likelihood that any two thoroughly shuffled decks in history have ever shared the identical card sequence.</p>

                <p><strong>Step 1: Formulate the Permutation Count</strong><br>
                Because all 52 distinct cards are arranged in order, the total possible unique sequences is:
                $$\Omega = 52!$$</p>

                <p><strong>Step 2: Evaluate using Stirling's Approximation</strong><br>
                $$52! \sim \sqrt{2\pi(52)} \left(\frac{52}{e}\right)^{52} = \sqrt{104\pi} \times (19.13)^{52}$$
                Taking common base-10 logarithms:
                $$\log_{10}(52!) = \sum_{k=1}^{52} \log_{10}(k) \approx 67.906648$$
                Converting to scientific notation:
                $$\Omega = 10^{0.906648} \times 10^{67} \approx 8.0658 \times 10^{67}\text{ unique permutations}$$</p>

                <p><strong>Step 3: Cosmic Probability Analysis</strong><br>
                Assume 7 billion humans have each shuffled a deck 1,000 times per year since the invention of cards 700 years ago:
                $$\text{Total Human Shuffles} \approx 7 \times 10^9 \times 1,000 \times 700 \approx 4.9 \times 10^{15}\text{ shuffles}$$
                The ratio of shuffles to total possibilities is:
                $$\frac{4.9 \times 10^{15}}{8.0658 \times 10^{67}} \approx 6.07 \times 10^{-53}$$
                Whenever a deck is thoroughly shuffled, that exact sequence of cards has almost certainly never existed before in the entire history of the universe.</p>
              </div>
            </div>

            <h2>7. Frequently Asked Questions (FAQ)</h2>
            <div class="faq-accordion">
              <div class="faq-item">
                <h3 class="faq-question">Why does computing 171! cause an overflow error in calculators?</h3>
                <div class="faq-answer">
                  <p>Standard 64-bit floating-point registers conform to the IEEE 754 standard, which has a maximum finite exponent threshold of \(2^{1024} \approx 1.797693 \times 10^{308}\). Because \(170! \approx 7.257 \times 10^{306}\), it fits within the limit. However, \(171! \approx 1.241 \times 10^{309}\), which exceeds the maximum possible value representable by a 64-bit double precision float, causing computers to output <code>Infinity</code>.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">What is a double factorial (n!!)?</h3>
                <div class="faq-answer">
                  <p>A double factorial \(n!!\) (not to be confused with \((n!)!\)) is the product of integers having the same parity (odd or even) down to 1 or 2: if \(n\) is odd, \(n!! = n \times (n-2) \times (n-4) \times \dots \times 3 \times 1\) (e.g., \(7!! = 7 \times 5 \times 3 \times 1 = 105\)); if \(n\) is even, \(n!! = n \times (n-2) \times \dots \times 4 \times 2\) (e.g., \(6!! = 6 \times 4 \times 2 = 48\)). Double factorials appear in quantum mechanics integrals and Taylor series expansions of \((1+x)^{1/2}\).</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">Can a negative integer have a factorial?</h3>
                <div class="faq-answer">
                  <p>In standard real and complex analysis, the factorial of a negative integer (\(-1!, -2!, -3!, \dots\)) is undefined and diverges to infinity. Under Euler's Gamma function, \(\Gamma(z)\) has simple poles (infinite vertical asymptotes) at all non-positive integers \(z \in \{0, -1, -2, -3, \dots\}\).</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">How does Legendre's formula count the trailing zeros of a factorial?</h3>
                <div class="faq-answer">
                  <p>Trailing zeros in \(n!\) are produced by factors of 10, which come from pairs of prime factors 2 and 5. Because factors of 2 are always more plentiful than 5, the count of trailing zeros equals the multiplicity of 5 in \(n!\), given by Legendre's formula: \(Z(n) = \sum_{k=1}^\infty \lfloor\frac{n}{5^k}\rfloor = \lfloor\frac{n}{5}\rfloor + \lfloor\frac{n}{25}\rfloor + \lfloor\frac{n}{125}\rfloor + \dots\). For example, \(100!\) has \(\lfloor 100/5 \rfloor + \lfloor 100/25 \rfloor = 20 + 4 = 24\) trailing zeros.</p>
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
              <li><a href="arithmetic-sequence-calculator.html">Arithmetic Sequence Calculator</a></li>
              <li><a href="gcd-lcm-calculator.html">GCD and LCM Calculator</a></li>
              <li><a href="prime-number-calculator.html">Prime Number Calculator</a></li>
              <li><a href="significant-figures-calculator.html">Significant Figures Calculator</a></li>
              <li><a href="percentage-calculator.html">Percentage Calculator</a></li>
              <li><a href="fraction-calculator.html">Fraction Calculator</a></li>
            </ul>
          </div>

          <div class="sidebar-card">
            <h3 class="sidebar-title">Factorial Rules</h3>
            <div style="font-size:0.875rem; line-height:1.5; color:var(--text-muted, #4b5563);">
              <p><strong>Definition:</strong> \(n! = \prod_{k=1}^n k\)</p>
              <p><strong>Zero:</strong> \(0! = 1\)</p>
              <p><strong>Permutations:</strong> \(P(n,r) = \frac{n!}{(n-r)!}\)</p>
              <p><strong>Combinations:</strong> \(C(n,r) = \frac{n!}{r!(n-r)!}\)</p>
              <p><strong>Stirling:</strong> \(n! \sim \sqrt{2\pi n}(n/e)^n\)</p>
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
    function fact(n) {
      if (n === 0 || n === 1) return 1;
      let res = 1;
      for (let i = 2; i <= n; i++) {
        res *= i;
      }
      return res;
    }

    function calcFactorial() {
      const n = parseInt(document.getElementById('factN').value, 10);
      const r = parseInt(document.getElementById('factR').value, 10);

      if (isNaN(n) || n < 0) return;

      const nFact = fact(n);
      let pVal = 0, cVal = 0;

      if (!isNaN(r) && r >= 0 && r <= n) {
        pVal = fact(n) / fact(n - r);
        cVal = pVal / fact(r);
      }

      let stirling = 0;
      if (n > 0) {
        stirling = Math.sqrt(2 * Math.PI * n) * Math.pow(n / Math.E, n);
      } else {
        stirling = 1;
      }

      let primaryText = "";
      if (nFact > 1e15) {
        primaryText = nFact.toExponential(6);
      } else {
        primaryText = nFact.toLocaleString();
      }

      document.getElementById('resFactorialPrimary').textContent = primaryText;
      document.getElementById('resFactorialSubtext').textContent = `${n}! = ${n > 0 ? (n <= 5 ? [...Array(n).keys()].map(k => k+1).join(' × ') : `${n} × ${n-1} × ... × 1`) : '1'}`;

      document.getElementById('resPermutations').textContent = (!isNaN(r) && r <= n) ? (pVal > 1e12 ? pVal.toExponential(4) : pVal.toLocaleString()) : "N/A (r > n)";
      document.getElementById('resCombinations').textContent = (!isNaN(r) && r <= n) ? (cVal > 1e12 ? cVal.toExponential(4) : cVal.toLocaleString()) : "N/A (r > n)";
      document.getElementById('resStirling').textContent = stirling > 1e12 ? stirling.toExponential(4) : stirling.toFixed(1);
      document.getElementById('resFactSci').textContent = nFact.toExponential(4);

      let steps = `1. Factorial n = ${n}<br>`;
      steps += `2. Expansion: ${n}! = ${primaryText}<br>`;
      if (!isNaN(r) && r <= n) {
        steps += `3. Permutations P(${n}, ${r}) = ${n}! / (${n} - ${r})! = ${nFact.toLocaleString()} / ${fact(n-r).toLocaleString()} = ${pVal.toLocaleString()}<br>`;
        steps += `4. Combinations C(${n}, ${r}) = P(${n}, ${r}) / ${r}! = ${pVal.toLocaleString()} / ${fact(r).toLocaleString()} = ${cVal.toLocaleString()}<br>`;
      }
      steps += `5. Stirling's Asymptotic Approximation: √[2π(${n})] × (${n} / e)^${n} ≈ ${stirling > 1e12 ? stirling.toExponential(4) : stirling.toFixed(1)}`;

      document.getElementById('factStepsDisplay').innerHTML = steps;
    }

    document.getElementById('factN').addEventListener('input', calcFactorial);
    document.getElementById('factR').addEventListener('input', calcFactorial);
    calcFactorial();
  </script>
</body>
</html>
"""

# Write files
with open(os.path.join(BASE_DIR, 'exponent-calculator.html'), 'w', encoding='utf-8') as f:
    f.write(exp_html)
print("Generated exponent-calculator.html successfully!")

with open(os.path.join(BASE_DIR, 'factorial-calculator.html'), 'w', encoding='utf-8') as f:
    f.write(fact_html)
print("Generated factorial-calculator.html successfully!")
