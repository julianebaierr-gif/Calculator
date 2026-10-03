import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 1. ARITHMETIC SEQUENCE CALCULATOR
# -------------------------------------------------------------
arith_seq_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Arithmetic Sequence Calculator — Nth Term, Common Difference & Sum | CalcHub</title>
  <meta name="description" content="Calculate arithmetic sequence nth term an = a1 + (n-1)d, common difference, partial sum Sn, recursive formulas, and Gauss summation with step-by-step solutions.">
  <meta name="keywords" content="arithmetic sequence calculator, arithmetic progression calculator, nth term of ap, sum of arithmetic sequence, common difference, gauss summation, ap calculator">
  <meta name="author" content="CalcHub Discrete Mathematics & Series Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/arithmetic-sequence-calculator.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="Arithmetic Sequence Calculator — Nth Term, Common Difference & Sum | CalcHub">
  <meta property="og:description" content="Solve arithmetic progressions, calculate nth terms, evaluate series sums using Gauss's formula, and find common differences.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/arithmetic-sequence-calculator.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/arithmetic-sequence-calculator.html#app",
      "name": "Arithmetic Sequence & Progression Solver",
      "url": "https://calchub.org/arithmetic-sequence-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "High-precision algebraic solver for arithmetic sequences and series, evaluating the nth term an, common difference d, and partial sum Sn."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Math & Engineering Calculators", "item": "https://calchub.org/math.html"},
        {"@type": "ListItem", "position": 3, "name": "Arithmetic Sequence Calculator", "item": "https://calchub.org/arithmetic-sequence-calculator.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is an arithmetic sequence and how is it defined?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "An arithmetic sequence (or arithmetic progression, AP) is a sequence of numbers in which the difference between any two consecutive terms is a constant value termed the common difference (d). It is defined recursively as a_n = a_{n-1} + d, and explicitly as a_n = a_1 + (n - 1)d, where a_1 is the first term and n is the term index."
          }
        },
        {
          "@type": "Question",
          "name": "How did Carl Friedrich Gauss derive the formula for the sum of an arithmetic series?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Legend holds that as a schoolchild, Gauss summed 1 to 100 by pairing terms from opposite ends: (1 + 100) = 101, (2 + 99) = 101, through (50 + 51) = 101. Having 50 pairs of 101 gave 5,050. Algebraically, writing the sum forwards and backwards and adding both equations yields: 2·S_n = n·(a_1 + a_n), which produces the universal formula S_n = (n / 2)·(a_1 + a_n) = (n / 2)·[2a_1 + (n - 1)d]."
          }
        },
        {
          "@type": "Question",
          "name": "What is the difference between an arithmetic sequence and an arithmetic series?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "An arithmetic sequence is an ordered list of numbers separated by a constant difference (e.g., 3, 7, 11, 15, 19). An arithmetic series is the indicated sum of the terms of an arithmetic sequence (e.g., 3 + 7 + 11 + 15 + 19 = 55). In mathematical notation, sequences use commas while series use addition signs."
          }
        },
        {
          "@type": "Question",
          "name": "Where are arithmetic progressions applied in engineering and physics?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In physics, Galileo's Law of Odd Numbers proves that an object falling under uniform gravitational acceleration covers distances during successive equal time intervals proportional to 1, 3, 5, 7, 9... which forms an arithmetic progression with d = 2. In civil engineering, stadium seating tiers and pyramid truss loadings follow arithmetic series, as do straight-line asset depreciation models in finance."
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
            <div class="badge-tag">Discrete Mathematics & Series</div>
            <h1 class="tool-title">Arithmetic Sequence Calculator</h1>
            <p class="tool-subtitle">Calculate the \(n\)-th term \(a_n\), common difference \(d\), and partial sum \(S_n\) of any arithmetic progression with step-by-step algebraic breakdown.</p>
          </header>

          <section class="calculator-card" aria-label="Arithmetic Progression Solver">
            <div class="calc-grid">
              <div class="input-group">
                <label for="firstTerm" class="input-label">First Term (\(a_1\))</label>
                <input type="number" id="firstTerm" class="calc-input" value="5" step="any">
              </div>

              <div class="input-group">
                <label for="commonDiff" class="input-label">Common Difference (\(d\))</label>
                <input type="number" id="commonDiff" class="calc-input" value="3" step="any">
              </div>

              <div class="input-group">
                <label for="termN" class="input-label">Term Number (\(n\))</label>
                <input type="number" id="termN" class="calc-input" value="20" min="1" step="1">
              </div>
            </div>

            <div class="primary-result" style="margin-top: 25px;">
              <div class="result-label">Calculated \(n\)-th Term (\(a_n\))</div>
              <div class="result-value" id="resNthTerm">a₂₀ = 62</div>
              <div class="result-subtext" id="resSubtext">Formula: a₂₀ = 5 + (20 - 1) × 3 = 62</div>
            </div>

            <div class="results-grid" style="margin-top: 20px;">
              <div class="result-item">
                <div class="result-label">Sum of First \(n\) Terms (\(S_n\))</div>
                <div class="result-value" id="resSum">670</div>
              </div>
              <div class="result-item">
                <div class="result-label">Arithmetic Mean of Sequence</div>
                <div class="result-value" id="resMean">33.50</div>
              </div>
              <div class="result-item">
                <div class="result-label">Explicit Linear Formula</div>
                <div class="result-value" id="resLinearForm">aₙ = 3n + 2</div>
              </div>
              <div class="result-item">
                <div class="result-label">Previous Term (\(a_{n-1}\))</div>
                <div class="result-value" id="resPrevTerm">59</div>
              </div>
            </div>

            <div class="conversion-steps" style="margin-top: 25px;">
              <h3>Algorithmic Resolution &amp; Sequence Preview</h3>
              <div id="seqStepsDisplay" style="font-family: monospace; font-size: 0.95rem; line-height: 1.6; background: rgba(0,0,0,0.03); padding: 16px; border-radius: 8px; border-left: 4px solid var(--accent, #2563eb);">
                Loading calculation steps...
              </div>
            </div>
          </section>

          <article class="article-body">
            <h2>1. Foundations and Definitions of Arithmetic Progressions</h2>
            <p>In discrete mathematics, numerical analysis, and algorithm theory, a <strong>sequence</strong> is an ordered mapping from the set of positive integers \(\mathbb{N} = \{1, 2, 3, \dots\}\) into a numerical field such as the real numbers \(\mathbb{R}\). An <strong>Arithmetic Sequence</strong>—also historically designated as an <em>Arithmetic Progression (AP)</em>—is a special class of sequence characterized by a strictly linear recurrence relation: the difference between any two consecutive terms is an invariant constant.</p>

            <p>Formally, a sequence \(\{a_n\}_{n=1}^\infty\) is arithmetic if and only if there exists a fixed real constant \(d \in \mathbb{R}\), termed the <strong>common difference</strong>, such that:</p>

            $$a_{n+1} - a_n = d \quad \forall n \ge 1$$

            <p>Depending on the sign of the common difference \(d\):</p>
            <ul>
              <li><strong>Monotonically Increasing (\(d > 0\)):</strong> Each successive term exceeds the previous term (e.g., \(2, 5, 8, 11, \dots\)).</li>
              <li><strong>Monotonically Decreasing (\(d < 0\)):</strong> Each successive term is smaller than the previous term (e.g., \(20, 16, 12, 8, \dots\)).</li>
              <li><strong>Constant / Stationary (\(d = 0\)):</strong> All terms in the sequence are identically equal to the first term \(a_1\).</li>
            </ul>

            <h2>2. Explicit Closed-Form Formula for the \(n\)-th Term</h2>
            <p>While the recursive definition \(a_n = a_{n-1} + d\) requires calculating all preceding terms sequentially, mathematical induction provides an immediate closed-form explicit expression for any arbitrary index \(n\).</p>

            <h3>2.1 Derivation by Unrolling the Recurrence</h3>
            <p>Observing the cumulative additions of the common difference:</p>

            $$\begin{aligned}
            a_1 &= a_1 \\
            a_2 &= a_1 + d \\
            a_3 &= a_2 + d = (a_1 + d) + d = a_1 + 2d \\
            a_4 &= a_3 + d = (a_1 + 2d) + d = a_1 + 3d \\
            &\;\vdots \\
            a_n &= a_1 + (n - 1)d
            \end{aligned}$$

            <p>Because the first term requires zero additions of \(d\), the \(n\)-th term requires exactly \(n - 1\) additions. Thus, the universal explicit formula is:</p>

            $$a_n = a_1 + (n - 1)d$$

            <h3>2.2 The Linear Function Perspective</h3>
            <p>Expanding the explicit formula algebraically:</p>

            $$a_n = d \cdot n + (a_1 - d)$$

            <p>This formulation reveals that an arithmetic sequence is simply the discrete integer domain restriction of a continuous linear function \(f(x) = mx + c\), where the common difference \(d\) acts as the line slope (\(m = d\)) and \(a_1 - d\) corresponds to the virtual \(y\)-intercept at \(n = 0\).</p>

            <h2>3. Partial Sum of an Arithmetic Series (\(S_n\))</h2>
            <p>The sum of the first \(n\) terms of an arithmetic sequence is termed an <strong>Arithmetic Series</strong>, denoted \(S_n = \sum_{k=1}^n a_k\). Deriving its closed-form expression represents one of the celebrated anecdotes in the history of mathematics.</p>

            <h3>3.1 Gauss's Reversal and Pairing Method</h3>
            <p>Let \(S_n\) be written forwards, and simultaneously written backwards:</p>

            $$\begin{aligned}
            S_n &= a_1 &+& \;(a_1 + d) &+& \;\dots &+& \;(a_n - d) &+& \;a_n \\
            S_n &= a_n &+& \;(a_n - d) &+& \;\dots &+& \;(a_1 + d) &+& \;a_1
            \end{aligned}$$

            <p>Adding both equations vertically term by term:</p>

            $$2S_n = (a_1 + a_n) + (a_1 + a_n) + \dots + (a_1 + a_n)$$

            <p>Because there are exactly \(n\) terms, and each vertical sum equals \(a_1 + a_n\), the sum simplifies to:</p>

            $$2S_n = n(a_1 + a_n) \implies S_n = \frac{n}{2}(a_1 + a_n)$$

            <p>Substituting the explicit formula for the terminal term \(a_n = a_1 + (n-1)d\) yields the second classic formulation:</p>

            $$S_n = \frac{n}{2}\big[2a_1 + (n - 1)d\big]$$

            <p>Geometrically, this represents the average of the initial and terminal terms multiplied by the total number of terms: \(S_n = n \times \bar{a}\), where \(\bar{a} = \frac{a_1 + a_n}{2}\) is the <strong>arithmetic mean</strong>.</p>

            <h2>4. Solving for Missing Variables and Intermediate Means</h2>
            <p>Given any subset of parameters among \(\{a_1, d, n, a_n, S_n\}\), algebraic substitution allows for the exact derivation of all remaining unknown variables:</p>
            <ul>
              <li><strong>Finding Common Difference (\(d\)) from two terms \(a_p\) and \(a_q\) (\(q > p\)):</strong>
                $$d = \frac{a_q - a_p}{q - p}$$</li>
              <li><strong>Finding Number of Terms (\(n\)) from \(a_1\), \(a_n\), and \(d\):</strong>
                $$n = \frac{a_n - a_1}{d} + 1$$</li>
              <li><strong>Inserting \(k\) Arithmetic Means between \(x\) and \(y\):</strong>
                Treat \(x\) as term 1 and \(y\) as term \(k + 2\). The required common difference is \(d = \frac{y - x}{k + 1}\).</li>
            </ul>

            <h2>5. Physical, Engineering, and Computational Applications</h2>
            <p>Arithmetic sequences govern phenomena across diverse physical and applied sciences:</p>

            <h3>5.1 Kinematics: Galileo's Odd Number Law</h3>
            <p>Consider a body falling from rest (\(v_0 = 0\)) under uniform gravitational acceleration \(g\). The distance covered during the \(n\)-th consecutive time interval of duration \(\Delta t\) is:</p>

            $$\Delta s_n = s(n\Delta t) - s((n-1)\Delta t) = \frac{1}{2}g(n\Delta t)^2 - \frac{1}{2}g((n-1)\Delta t)^2 = \frac{1}{2}g(\Delta t)^2 (2n - 1)$$

            <p>The sequence of distances \(\Delta s_1, \Delta s_2, \Delta s_3, \dots\) is directly proportional to \(1, 3, 5, 7, 9, \dots\)—a classic arithmetic progression with first term 1 and common difference 2.</p>

            <h3>5.2 Structural Engineering and Architectural Seating</h3>
            <p>In structural amphitheater, stadium, and auditorium design, sightline optimization requires concentric tiers of seating to expand radially. If the first row contains \(a_1\) seats and each successive row adds \(d\) seats to accommodate the expanding perimeter, the total capacity of an \(n\)-row stadium is governed precisely by \(S_n = \frac{n}{2}[2a_1 + (n-1)d]\).</p>

            <h3>5.3 Computer Architecture: Memory Strides and Loop Unrolling</h3>
            <p>In high-performance computing (HPC) and GPU kernel programming, fetching array elements with a constant memory stride (e.g., accessing matrix columns stored in row-major layout) accesses memory addresses in an arithmetic progression: \(\text{Addr}_n = \text{Base} + n \times \text{Stride}\). Understanding this progression enables compilers to optimize SIMD vectorization and hardware prefetching.</p>

            <h2>6. Benchmark Comparative Reference Table</h2>
            <p>The table below catalogues eight benchmark arithmetic progressions, illustrating the first term \(a_1\), common difference \(d\), explicit formula, 10th term, and partial sum \(S_{10}\).</p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>Sequence Description</th>
                  <th>First Term (\(a_1\))</th>
                  <th>Difference (\(d\))</th>
                  <th>Explicit Formula (\(a_n\))</th>
                  <th>10th Term (\(a_{10}\))</th>
                  <th>Partial Sum (\(S_{10}\))</th>
                  <th>Nature</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Counting Numbers</td>
                  <td>1</td>
                  <td>+1</td>
                  <td>\(a_n = n\)</td>
                  <td>10</td>
                  <td>55</td>
                  <td>Increasing</td>
                </tr>
                <tr>
                  <td>Odd Positive Integers</td>
                  <td>1</td>
                  <td>+2</td>
                  <td>\(a_n = 2n - 1\)</td>
                  <td>19</td>
                  <td>100 (\(n^2\))</td>
                  <td>Increasing</td>
                </tr>
                <tr>
                  <td>Even Positive Integers</td>
                  <td>2</td>
                  <td>+2</td>
                  <td>\(a_n = 2n\)</td>
                  <td>20</td>
                  <td>110 (\(n(n+1)\))</td>
                  <td>Increasing</td>
                </tr>
                <tr>
                  <td>Industrial Shift (5, 8, 11...)</td>
                  <td>5</td>
                  <td>+3</td>
                  <td>\(a_n = 3n + 2\)</td>
                  <td>32</td>
                  <td>185</td>
                  <td>Increasing</td>
                </tr>
                <tr>
                  <td>Cooling Rate Decline</td>
                  <td>100</td>
                  <td>-7</td>
                  <td>\(a_n = 107 - 7n\)</td>
                  <td>37</td>
                  <td>685</td>
                  <td>Decreasing</td>
                </tr>
                <tr>
                  <td>Fractional Precision</td>
                  <td>0.5</td>
                  <td>+0.25</td>
                  <td>\(a_n = 0.25n + 0.25\)</td>
                  <td>2.75</td>
                  <td>16.25</td>
                  <td>Increasing</td>
                </tr>
                <tr>
                  <td>Negative Progression</td>
                  <td>-20</td>
                  <td>-5</td>
                  <td>\(a_n = -5n - 15\)</td>
                  <td>-65</td>
                  <td>-425</td>
                  <td>Decreasing</td>
                </tr>
                <tr>
                  <td>Stationary Sequence</td>
                  <td>42</td>
                  <td>0</td>
                  <td>\(a_n = 42\)</td>
                  <td>42</td>
                  <td>420</td>
                  <td>Constant</td>
                </tr>
              </tbody>
            </table>

            <h2>7. Worked Civil Engineering Case Study: Stadium Amphitheater Seating Capacity</h2>
            <div class="worked-example-card">
              <div class="example-header">
                <strong>Civil Engineering Case Study:</strong> Municipal Amphitheater Tier Sizing & Structural Load
              </div>
              <div class="example-body">
                <p><strong>Scenario:</strong> A structural engineering firm is designing a reinforced concrete amphitheater. Due to sightline curvature, Row 1 (innermost) accommodates exactly \(a_1 = 44\text{ seats}\). Each subsequent row expands along a wider radius, adding exactly \(d = 4\text{ seats}\) per row. The architectural footprint permits a total of \(n = 28\text{ rows}\). The team must calculate: (1) the seat count in the topmost 28th row, (2) the total seating capacity of the amphitheater, and (3) the average seats per row for evacuation modeling.</p>

                <p><strong>Step 1: Calculate Topmost Row Capacity (\(a_{28}\))</strong><br>
                Using the explicit formula \(a_n = a_1 + (n - 1)d\):
                $$a_{28} = 44 + (28 - 1) \times 4 = 44 + (27 \times 4) = 44 + 108 = 152\text{ seats}$$
                Row 28 accommodates exactly 152 spectators.</p>

                <p><strong>Step 2: Calculate Total Amphitheater Seating Capacity (\(S_{28}\))</strong><br>
                Using Gauss's summation formula:
                $$S_{28} = \frac{n}{2}(a_1 + a_{28}) = \frac{28}{2}(44 + 152) = 14 \times 196 = 2,744\text{ seats}$$
                Alternatively, using the parameter form:
                $$S_{28} = \frac{28}{2}\big[2(44) + (28 - 1)(4)\big] = 14 \times [88 + 108] = 14 \times 196 = 2,744\text{ seats}$$</p>

                <p><strong>Step 3: Compute Mean Egress Density</strong><br>
                The average row capacity is:
                $$\bar{a} = \frac{S_{28}}{n} = \frac{2,744}{28} = 98.0\text{ seats/row}$$
                The fire life safety engineer dimensions the aisleways based on a mean egress density of 98 patrons per row.</p>
              </div>
            </div>

            <h2>8. Frequently Asked Questions (FAQ)</h2>
            <div class="faq-accordion">
              <div class="faq-item">
                <h3 class="faq-question">Can the common difference of an arithmetic sequence be negative or a fraction?</h3>
                <div class="faq-answer">
                  <p>Yes. The common difference \(d\) can be any real number (\(d \in \mathbb{R}\)), including negative integers, rational fractions (e.g., \(d = \frac{1}{3}\)), or irrational numbers (e.g., \(d = \sqrt{2}\)). A negative common difference produces a strictly decreasing sequence.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">How does an arithmetic sequence differ from a geometric sequence?</h3>
                <div class="faq-answer">
                  <p>In an arithmetic sequence, consecutive terms change by <em>adding</em> a constant common difference (\(a_n = a_1 + (n-1)d\)), exhibiting linear growth. In a geometric sequence, consecutive terms change by <em>multiplying</em> by a constant common ratio (\(g_n = g_1 \cdot r^{n-1}\)), exhibiting exponential growth or decay.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">Why is the sum of the first n odd numbers always a perfect square?</h3>
                <div class="faq-answer">
                  <p>The first \(n\) odd numbers form an arithmetic sequence with \(a_1 = 1\) and \(d = 2\). The \(n\)-th odd number is \(a_n = 2n - 1\). Applying Gauss's sum formula: \(S_n = \frac{n}{2}(a_1 + a_n) = \frac{n}{2}(1 + 2n - 1) = \frac{n}{2}(2n) = n^2\). Thus, \(1 + 3 + 5 + \dots + (2n-1) = n^2\) identically for all positive integers.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">Can an arithmetic series have an infinite sum?</h3>
                <div class="faq-answer">
                  <p>If \(d \neq 0\), the terms grow unboundedly in magnitude, causing an infinite arithmetic series to diverge to \(+\infty\) or \(-\infty\). The only case where an infinite arithmetic series converges is the trivial sequence where every term is zero (\(a_1 = 0, d = 0\)), yielding an infinite sum of 0.</p>
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
              <li><a href="fraction-calculator.html">Fraction Calculator</a></li>
              <li><a href="percentage-calculator.html">Percentage Calculator</a></li>
              <li><a href="quadratic-equation-calculator.html">Quadratic Equation Calculator</a></li>
              <li><a href="pythagorean-theorem-calculator.html">Pythagorean Theorem Calculator</a></li>
              <li><a href="scientific-notation-calculator.html">Scientific Notation Calculator</a></li>
              <li><a href="significant-figures-calculator.html">Significant Figures Calculator</a></li>
              <li><a href="prime-number-calculator.html">Prime Number Calculator</a></li>
            </ul>
          </div>

          <div class="sidebar-card">
            <h3 class="sidebar-title">Progression Formulas</h3>
            <div style="font-size:0.875rem; line-height:1.5; color:var(--text-muted, #4b5563);">
              <p><strong>Nth Term:</strong> \(a_n = a_1 + (n-1)d\)</p>
              <p><strong>Partial Sum:</strong> \(S_n = \frac{n}{2}(a_1 + a_n)\)</p>
              <p><strong>Parameter Sum:</strong> \(S_n = \frac{n}{2}[2a_1 + (n-1)d]\)</p>
              <p><strong>Mean:</strong> \(\bar{a} = \frac{a_1 + a_n}{2}\)</p>
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
    function calcArithSeq() {
      const a1 = parseFloat(document.getElementById('firstTerm').value);
      const d = parseFloat(document.getElementById('commonDiff').value);
      const n = parseInt(document.getElementById('termN').value, 10);

      if (isNaN(a1) || isNaN(d) || isNaN(n) || n < 1) return;

      const an = a1 + (n - 1) * d;
      const sn = (n / 2) * (a1 + an);
      const mean = (a1 + an) / 2;
      const prevTerm = a1 + (n - 2) * d;

      const signStr = (a1 - d) >= 0 ? `+ ${(a1 - d)}` : `- ${Math.abs(a1 - d)}`;
      const linearExpr = `aₙ = ${d}n ${signStr}`;

      document.getElementById('resNthTerm').textContent = `a${subscript(n)} = ${an.toLocaleString()}`;
      document.getElementById('resSubtext').textContent = `Formula: a${subscript(n)} = ${a1} + (${n} - 1) × ${d} = ${an}`;
      document.getElementById('resSum').textContent = sn.toLocaleString();
      document.getElementById('resMean').textContent = mean.toFixed(2);
      document.getElementById('resLinearForm').textContent = linearExpr;
      document.getElementById('resPrevTerm').textContent = n > 1 ? prevTerm.toLocaleString() : "None (Initial)";

      // Generate preview of first min(n, 10) terms
      const previewCount = Math.min(n, 10);
      const terms = [];
      for (let k = 1; k <= previewCount; k++) {
        terms.push(a1 + (k - 1) * d);
      }
      let previewStr = terms.join(", ");
      if (n > 10) {
        previewStr += `, ... , ${an}`;
      }

      let stepsHtml = `1. Explicit Formula: aₙ = a₁ + (n - 1)d<br>`;
      stepsHtml += `2. Substitute: a${subscript(n)} = ${a1} + (${n} - 1) × ${d} = ${a1} + ${ (n-1)*d } = ${an}<br>`;
      stepsHtml += `3. Partial Sum Formula: Sₙ = (n / 2) × (a₁ + aₙ)<br>`;
      stepsHtml += `4. Substitute: S${subscript(n)} = (${n} / 2) × (${a1} + ${an}) = ${n/2} × ${a1 + an} = ${sn}<br><br>`;
      stepsHtml += `<strong>Sequence Preview:</strong> [ ${previewStr} ]`;

      document.getElementById('seqStepsDisplay').innerHTML = stepsHtml;
    }

    function subscript(num) {
      const map = {
        '0':'₀','1':'₁','2':'₂','3':'₃','4':'₄',
        '5':'₅','6':'₆','7':'₇','8':'₈','9':'₉'
      };
      return String(num).split('').map(c => map[c] || c).join('');
    }

    document.getElementById('firstTerm').addEventListener('input', calcArithSeq);
    document.getElementById('commonDiff').addEventListener('input', calcArithSeq);
    document.getElementById('termN').addEventListener('input', calcArithSeq);
    calcArithSeq();
  </script>
</body>
</html>
"""

# -------------------------------------------------------------
# 2. CIRCLE CALCULATOR
# -------------------------------------------------------------
circle_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Circle Calculator — Radius, Diameter, Circumference & Sector Area | CalcHub</title>
  <meta name="description" content="Calculate circle radius, diameter, circumference, area, arc length, chord length, sector area, and circular segment with exact geometric formulas.">
  <meta name="keywords" content="circle calculator, radius to circumference, circle area calculator, diameter to radius, arc length calculator, sector area calculator, chord length, circular segment">
  <meta name="author" content="CalcHub Euclidean Geometry & Conic Sections Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/circle-calculator.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="Circle Calculator — Radius, Diameter, Circumference & Sector Area | CalcHub">
  <meta property="og:description" content="Solve all circle geometric properties from any single input: radius, diameter, circumference, total area, sector area, arc length, and chord.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/circle-calculator.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/circle-calculator.html#app",
      "name": "Circle & Circular Sector Geometry Engine",
      "url": "https://calchub.org/circle-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "High-precision geometric solver for circles, circumference, diameter, area, circular sectors, chords, and arc segments."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Math & Engineering Calculators", "item": "https://calchub.org/math.html"},
        {"@type": "ListItem", "position": 3, "name": "Circle Calculator", "item": "https://calchub.org/circle-calculator.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How are the fundamental circle formulas derived from the definition of Pi (π)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "By mathematical definition, Pi (π ≈ 3.1415926535...) is the ratio of any circle's circumference C to its diameter d: π = C / d. From this axiom, multiplying by d gives C = π · d = 2πr. In calculus, dividing a circle of radius r into infinitely thin concentric rings of circumference 2πx and thickness dx, the area is the integral A = ∫₀ʳ 2πx dx = [πx²]₀ʳ = πr²."
          }
        },
        {
          "@type": "Question",
          "name": "What is the difference between a circular sector and a circular segment?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A circular sector is a pie-shaped portion of a circle enclosed by two radii and an arc (Area = 0.5 · r² · θ, where θ is in radians). A circular segment is the region enclosed between a straight chord line and the adjacent arc. The area of a circular segment is calculated by subtracting the area of the central triangle from the sector: Area_segment = 0.5 · r² · (θ - sin θ)."
          }
        },
        {
          "@type": "Question",
          "name": "How do you calculate arc length and chord length for a given central angle?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "For a central angle θ in radians, arc length along the circumference is s = r · θ. If θ is in degrees, s = (θ / 360°) · 2πr. The straight-line chord length connecting the two arc endpoints is derived from a right triangle splitting the central angle: c = 2r · sin(θ / 2)."
          }
        },
        {
          "@type": "Question",
          "name": "What is the sagitta of a circular arc and where is it used in engineering?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The sagitta (or height of an arc) is the perpendicular distance from the midpoint of a chord to the peak of the arc. It is calculated as h = r - √(r² - (c / 2)²). Sagitta calculations are essential in optical lens manufacturing to verify curvature radius and in civil transportation engineering for measuring railway curve deflection."
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
            <div class="badge-tag">Euclidean Geometry & Conic Sections</div>
            <h1 class="tool-title">Circle Calculator</h1>
            <p class="tool-subtitle">Compute radius, diameter, circumference, area, arc length, sector area, chord length, and sagitta from any known circle dimension.</p>
          </header>

          <section class="calculator-card" aria-label="Circle Geometry Solver">
            <div class="calc-grid">
              <div class="input-group">
                <label for="circleInputMode" class="input-label">Known Primary Parameter</label>
                <select id="circleInputMode" class="calc-input">
                  <option value="radius">Radius (r)</option>
                  <option value="diameter">Diameter (d)</option>
                  <option value="circumference">Circumference (C)</option>
                  <option value="area">Total Area (A)</option>
                </select>
              </div>

              <div class="input-group">
                <label for="primaryValue" class="input-label" id="labelPrimaryVal">Radius (r)</label>
                <input type="number" id="primaryValue" class="calc-input" value="10" step="any" min="0.0001">
              </div>

              <div class="input-group">
                <label for="sectorAngle" class="input-label">Sector Central Angle (\(\theta^\circ\))</label>
                <input type="number" id="sectorAngle" class="calc-input" value="60" min="0.001" max="360" step="any">
              </div>
            </div>

            <div class="primary-result" style="margin-top: 25px;">
              <div class="result-label">Computed Circle Area (\(A\))</div>
              <div class="result-value" id="circlePrimaryArea">314.1593</div>
              <div class="result-subtext" id="circlePrimarySubtext">Formula: A = π × (10)² = 314.1593</div>
            </div>

            <div class="results-grid" style="margin-top: 20px;">
              <div class="result-item">
                <div class="result-label">Radius (\(r\))</div>
                <div class="result-value" id="resRadius">10.0000</div>
              </div>
              <div class="result-item">
                <div class="result-label">Diameter (\(d = 2r\))</div>
                <div class="result-value" id="resDiameter">20.0000</div>
              </div>
              <div class="result-item">
                <div class="result-label">Circumference (\(C = 2\pi r\))</div>
                <div class="result-value" id="resCircumference">62.8319</div>
              </div>
              <div class="result-item">
                <div class="result-label">Arc Length (\(s = r\theta\))</div>
                <div class="result-value" id="resArcLength">10.4720</div>
              </div>
              <div class="result-item">
                <div class="result-label">Sector Area (\(A_{\text{sec}}\))</div>
                <div class="result-value" id="resSectorArea">52.3599</div>
              </div>
              <div class="result-item">
                <div class="result-label">Chord Length (\(c\))</div>
                <div class="result-value" id="resChordLength">10.0000</div>
              </div>
              <div class="result-item">
                <div class="result-label">Segment Area (\(A_{\text{seg}}\))</div>
                <div class="result-value" id="resSegmentArea">9.0590</div>
              </div>
              <div class="result-item">
                <div class="result-label">Sagitta Height (\(h\))</div>
                <div class="result-value" id="resSagitta">1.3397</div>
              </div>
            </div>

            <div class="conversion-steps" style="margin-top: 25px;">
              <h3>Step-by-Step Geometric Calculations</h3>
              <div id="circleStepsDisplay" style="font-family: monospace; font-size: 0.95rem; line-height: 1.6; background: rgba(0,0,0,0.03); padding: 16px; border-radius: 8px; border-left: 4px solid var(--accent, #2563eb);">
                Loading geometric breakdown...
              </div>
            </div>
          </section>

          <article class="article-body">
            <h2>1. The Circle in Classical Geometry and Conic Sections</h2>
            <p>Among all geometric curves in Euclidean two-dimensional space, the <strong>circle</strong> exhibits maximal symmetry, invariant rotational curvature, and optimal area enclosure. Formally, a circle is defined as the locus of all coplanar points equidistant from a fixed central reference point \(O(h, k)\). The constant separation distance is designated as the <strong>radius</strong> (\(r\)). In Cartesian coordinates, the circle is governed by the second-degree implicit equation:</p>

            $$(x - h)^2 + (y - k)^2 = r^2$$

            <p>In the theory of conic sections, a circle represents an ellipse whose eccentricity vanishes entirely (\(e = 0\)), formed when a circular cone is sliced by a cutting plane exactly perpendicular to the cone's axis of symmetry.</p>

            <h2>2. The Constant Pi (\(\pi\)) and Fundamental Mensuration Formulas</h2>
            <p>The mathematical constant \(\pi\) (approximately \(3.141592653589793\dots\)) is the fundamental transcendental ratio relating a circle's perimeter to its linear width:</p>

            $$\pi = \frac{C}{d} = \frac{C}{2r}$$

            <p>From this foundational definition, all primary circle mensuration properties follow immediately:</p>

            <h3>2.1 Diameter and Circumference</h3>
            <ul>
              <li><strong>Diameter (\(d\)):</strong> The maximum chord distance spanning through the center point: \(d = 2r\).</li>
              <li><strong>Circumference (\(C\)):</strong> The perimeter length enclosing the circular boundary: \(C = 2\pi r = \pi d\).</li>
            </ul>

            <h3>2.2 Surface Area: Calculus Derivation</h3>
            <p>The area \(\mathcal{A}\) of a circle can be proven rigorously using Riemann integration. Divide the circle into an infinite sequence of thin concentric circular rings of radius \(x\) and differential radial thickness \(dx\). Each infinitesimal ring unrolls into a thin rectangle of length \(2\pi x\) and width \(dx\), yielding differential area \(dA = 2\pi x \, dx\). Integrating from the origin \(x = 0\) to the perimeter boundary \(x = r\):</p>

            $$\mathcal{A} = \int_0^r 2\pi x \, dx = 2\pi \left[ \frac{x^2}{2} \right]_0^r = \pi r^2 = \frac{\pi d^2}{4} = \frac{C^2}{4\pi}$$

            <p>The Isoperimetric Theorem in differential geometry proves that among all closed plane curves of a fixed perimeter \(C\), the circle encloses the absolute maximum possible surface area.</p>

            <h2>3. Circular Sectors, Arcs, Chords, and Segments</h2>
            <p>When analyzing portions of a circle subtended by a central angle \(\theta\), trigonometry provides exact closed-form expressions:</p>

            <h3>3.1 Arc Length (\(s\))</h3>
            <p>An arc represents a fraction of the circumference. If the central angle \(\theta\) is measured in radians:</p>

            $$s = r \cdot \theta \quad (\theta \text{ in radians})$$

            <p>If \(\theta\) is provided in degrees (\(^\circ\)), scale by the degree-to-radian conversion factor \(\frac{\pi}{180^\circ}\):</p>

            $$s = \left(\frac{\theta^\circ}{360^\circ}\right) 2\pi r = \frac{\pi r \theta^\circ}{180^\circ}$$

            <h3>3.2 Sector Area (\(\mathcal{A}_{\text{sector}}\))</h3>
            <p>A circular sector is the region bounded by two radii and the connecting arc (a slice of pie):</p>

            $$\mathcal{A}_{\text{sector}} = \frac{1}{2} r^2 \theta \quad (\theta \text{ in rad}) = \left(\frac{\theta^\circ}{360^\circ}\right) \pi r^2 = \frac{1}{2} s \cdot r$$

            <h3>3.3 Chord Length (\(c\))</h3>
            <p>A chord is a straight line segment joining two points along the circle. Dropping an altitude from the center bisects the isosceles central triangle into two right triangles with hypotenuse \(r\) and opposite angle \(\frac{\theta}{2}\):</p>

            $$c = 2r \sin\left(\frac{\theta}{2}\right)$$

            <h3>3.4 Circular Segment Area (\(\mathcal{A}_{\text{segment}}\))</h3>
            <p>A circular segment is the region bounded strictly between the chord and the arc. Its area equals the sector area minus the area of the isosceles triangle formed by the radii and the chord (\(\mathcal{A}_{\text{tri}} = \frac{1}{2} r^2 \sin\theta\)):</p>

            $$\mathcal{A}_{\text{segment}} = \mathcal{A}_{\text{sector}} - \mathcal{A}_{\text{tri}} = \frac{1}{2} r^2 (\theta - \sin\theta) \quad (\theta \text{ in rad})$$

            <h3>3.5 Sagitta (Height of Arc, \(h\))</h3>
            <p>The sagitta \(h\) is the maximum perpendicular clearance between the midpoint of the chord and the peak of the arc:</p>

            $$h = r - \sqrt{r^2 - \left(\frac{c}{2}\right)^2} = r \left(1 - \cos\left(\frac{\theta}{2}\right)\right)$$

            <h2>4. Engineering and Physical Mechanics Applications</h2>

            <h3>4.1 Hoop Stress in Cylindrical Pressure Vessels</h3>
            <p>In mechanical and chemical piping engineering, a pressurized cylindrical vessel of inner radius \(r\) with internal fluid pressure \(P\) and wall thickness \(t\) experiences circumferential tensile stress (hoop stress) derived from circular equilibrium:</p>

            $$\sigma_{\text{hoop}} = \frac{P \cdot r}{t}$$

            <p>Because hoop stress is directly proportional to radius, doubling the pipe diameter doubles the tensile wall stress under identical internal fluid pressures, dictating thicker steel walls in large-diameter pipelines.</p>

            <h3>4.2 Horizontal Curve Radius in Transportation Engineering</h3>
            <p>In highway and railway engineering, curves are designed as circular arcs to prevent vehicle rollover and skidding under lateral centrifugal acceleration. For a design speed \(V\) (in mph), highway superelevation bank angle \(e\), and tire-pavement side friction factor \(f\), the American Association of State Highway and Transportation Officials (AASHTO) mandates the minimum curve radius:</p>

            $$R_{\min} = \frac{V^2}{15(e + f)}$$

            <h2>5. Benchmark Comparative Reference Table</h2>
            <p>The table below provides benchmark circle calculations across standard radii, detailing diameter, circumference, area, and sector properties at \(\theta = 60^\circ\).</p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>Radius (\(r\))</th>
                  <th>Diameter (\(d\))</th>
                  <th>Circumference (\(C\))</th>
                  <th>Total Area (\(\mathcal{A}\))</th>
                  <th>Arc Length (\(60^\circ\))</th>
                  <th>Sector Area (\(60^\circ\))</th>
                  <th>Chord (\(60^\circ\))</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>1.0</td>
                  <td>2.0</td>
                  <td>6.2832</td>
                  <td>3.1416</td>
                  <td>1.0472</td>
                  <td>0.5236</td>
                  <td>1.0000</td>
                </tr>
                <tr>
                  <td>5.0</td>
                  <td>10.0</td>
                  <td>31.4159</td>
                  <td>78.5398</td>
                  <td>5.2360</td>
                  <td>13.0900</td>
                  <td>5.0000</td>
                </tr>
                <tr>
                  <td>10.0</td>
                  <td>20.0</td>
                  <td>62.8319</td>
                  <td>314.1593</td>
                  <td>10.4720</td>
                  <td>52.3599</td>
                  <td>10.0000</td>
                </tr>
                <tr>
                  <td>14.0</td>
                  <td>28.0</td>
                  <td>87.9646</td>
                  <td>615.7522</td>
                  <td>14.6608</td>
                  <td>102.6254</td>
                  <td>14.0000</td>
                </tr>
                <tr>
                  <td>25.0</td>
                  <td>50.0</td>
                  <td>157.0796</td>
                  <td>1,963.4954</td>
                  <td>26.1799</td>
                  <td>327.2492</td>
                  <td>25.0000</td>
                </tr>
                <tr>
                  <td>50.0</td>
                  <td>100.0</td>
                  <td>314.1593</td>
                  <td>7,853.9816</td>
                  <td>52.3599</td>
                  <td>1,308.9969</td>
                  <td>50.0000</td>
                </tr>
                <tr>
                  <td>100.0</td>
                  <td>200.0</td>
                  <td>628.3185</td>
                  <td>31,415.9265</td>
                  <td>104.7198</td>
                  <td>5,235.9878</td>
                  <td>100.0000</td>
                </tr>
              </tbody>
            </table>

            <h2>6. Worked Highway Civil Case Study: Circular Horizontal Roadway Alignment</h2>
            <div class="worked-example-card">
              <div class="example-header">
                <strong>Transportation Engineering Case Study:</strong> Horizontal Freeway Curve Sizing & Arc Geometry
              </div>
              <div class="example-body">
                <p><strong>Scenario:</strong> A highway design engineer aligns a two-lane state connector curving around an environmental wetlands preserve. The design centerline radius is \(R = 1,200.0\text{ ft}\), and the intersection of tangents yields an internal deflection angle \(\Delta = 45.0^\circ\) (\(\frac{\pi}{4}\text{ rad}\)). The surveying crew needs to establish: (1) the curve arc length (\(L\)), (2) the straight-line chord length (\(C\)), (3) the tangent distance from point of curve to vertex (\(T\)), and (4) the middle ordinate sagitta (\(M\)) for roadside barrier clearance.</p>

                <p><strong>Step 1: Calculate Arc Length (\(L\))</strong><br>
                $$L = R \times \Delta_{\text{rad}} = 1,200.0 \times \left(45.0^\circ \times \frac{\pi}{180^\circ}\right) = 1,200.0 \times 0.785398 = 942.48\text{ ft}$$</p>

                <p><strong>Step 2: Calculate Long Chord Length (\(C\))</strong><br>
                $$C = 2R \sin\left(\frac{\Delta}{2}\right) = 2(1,200.0) \times \sin(22.5^\circ) = 2,400.0 \times 0.382683 = 918.44\text{ ft}$$</p>

                <p><strong>Step 3: Calculate Tangent Distance (\(T\))</strong><br>
                $$T = R \tan\left(\frac{\Delta}{2}\right) = 1,200.0 \times \tan(22.5^\circ) = 1,200.0 \times 0.414214 = 497.06\text{ ft}$$</p>

                <p><strong>Step 4: Calculate Middle Ordinate Sagitta (\(M\))</strong><br>
                $$M = R \left[1 - \cos\left(\frac{\Delta}{2}\right)\right] = 1,200.0 \times [1 - \cos(22.5^\circ)] = 1,200.0 \times [1 - 0.923880] = 91.34\text{ ft}$$
                The highway guardrail clearance requires at least \(91.34\text{ ft}\) of sightline clearance from the centerline chord.</p>
              </div>
            </div>

            <h2>7. Frequently Asked Questions (FAQ)</h2>
            <div class="faq-accordion">
              <div class="faq-item">
                <h3 class="faq-question">Why is a central angle of 60 degrees unique for chord length?</h3>
                <div class="faq-answer">
                  <p>When the central angle is \(\theta = 60^\circ\), the triangle formed by the circle center and the two endpoints of the chord is an equilateral triangle (all three angles are \(60^\circ\)). Consequently, the chord length is exactly equal to the radius: \(c = 2r \sin(30^\circ) = 2r(0.5) = r\).</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">How do you find the radius if only the area of the circle is known?</h3>
                <div class="faq-answer">
                  <p>To find radius from area, rearrange the formula \(\mathcal{A} = \pi r^2\). Divide both sides by \(\pi\) and extract the principal square root: \(r = \sqrt{\frac{\mathcal{A}}{\pi}}\). For example, if a circle has an area of \(100\text{ m}^2\), its radius is \(r = \sqrt{100 / 3.14159} \approx 5.642\text{ m}\).</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">What is the difference between a secant line and a tangent line to a circle?</h3>
                <div class="faq-answer">
                  <p>A <em>secant line</em> intersects the circle at exactly two discrete points, containing a chord in its interior. A <em>tangent line</em> touches the circle at exactly one point (the point of tangency) and is strictly perpendicular to the radius drawn to that point.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">How does doubling the radius affect the circumference and area of a circle?</h3>
                <div class="faq-answer">
                  <p>Circumference scales linearly with radius (\(C \propto r\)), so doubling the radius doubles the circumference (\(2 \times\)). In contrast, area scales quadratically (\(\mathcal{A} \propto r^2\)), so doubling the radius quadruples the area (\(2^2 = 4 \times\)).</p>
                </div>
              </div>
            </div>
          </article>
        </div>

        <aside class="sidebar-column">
          <div class="sidebar-card">
            <h3 class="sidebar-title">Related Math Calculators</h3>
            <ul class="sidebar-nav">
              <li><a href="area-calculator.html">Area Calculator</a></li>
              <li><a href="pythagorean-theorem-calculator.html">Pythagorean Theorem Calculator</a></li>
              <li><a href="quadratic-equation-calculator.html">Quadratic Equation Calculator</a></li>
              <li><a href="fraction-calculator.html">Fraction Calculator</a></li>
              <li><a href="percentage-calculator.html">Percentage Calculator</a></li>
              <li><a href="gcd-lcm-calculator.html">GCD and LCM Calculator</a></li>
              <li><a href="scientific-notation-calculator.html">Scientific Notation Calculator</a></li>
              <li><a href="length-converter.html">Length Converter</a></li>
            </ul>
          </div>

          <div class="sidebar-card">
            <h3 class="sidebar-title">Circle Identities</h3>
            <div style="font-size:0.875rem; line-height:1.5; color:var(--text-muted, #4b5563);">
              <p><strong>Diameter:</strong> \(d = 2r\)</p>
              <p><strong>Circumference:</strong> \(C = 2\pi r\)</p>
              <p><strong>Area:</strong> \(A = \pi r^2\)</p>
              <p><strong>Arc:</strong> \(s = r\theta\)</p>
              <p><strong>Sector:</strong> \(A_{\text{sec}} = \frac{1}{2}r^2\theta\)</p>
              <p><strong>Chord:</strong> \(c = 2r\sin(\theta/2)\)</p>
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
    function updateCircleInputLabel() {
      const mode = document.getElementById('circleInputMode').value;
      const lbl = document.getElementById('labelPrimaryVal');
      if (mode === 'radius') lbl.textContent = "Radius (r)";
      else if (mode === 'diameter') lbl.textContent = "Diameter (d)";
      else if (mode === 'circumference') lbl.textContent = "Circumference (C)";
      else lbl.textContent = "Total Area (A)";
      calcCircle();
    }

    function calcCircle() {
      const mode = document.getElementById('circleInputMode').value;
      const val = parseFloat(document.getElementById('primaryValue').value);
      const thetaDeg = parseFloat(document.getElementById('sectorAngle').value);

      if (isNaN(val) || val <= 0 || isNaN(thetaDeg) || thetaDeg <= 0) return;

      let r = 0;
      if (mode === 'radius') {
        r = val;
      } else if (mode === 'diameter') {
        r = val / 2;
      } else if (mode === 'circumference') {
        r = val / (2 * Math.PI);
      } else {
        r = Math.sqrt(val / Math.PI);
      }

      const d = 2 * r;
      const c = 2 * Math.PI * r;
      const a = Math.PI * r * r;

      const thetaRad = thetaDeg * (Math.PI / 180);
      const arcLen = r * thetaRad;
      const sectorArea = 0.5 * r * r * thetaRad;
      const chordLen = 2 * r * Math.sin(thetaRad / 2);
      const segmentArea = 0.5 * r * r * (thetaRad - Math.sin(thetaRad));
      const sagitta = r * (1 - Math.cos(thetaRad / 2));

      document.getElementById('circlePrimaryArea').textContent = a.toFixed(4);
      document.getElementById('circlePrimarySubtext').textContent = `Formula: A = π × (${r.toFixed(4)})² = ${a.toFixed(4)}`;

      document.getElementById('resRadius').textContent = r.toFixed(4);
      document.getElementById('resDiameter').textContent = d.toFixed(4);
      document.getElementById('resCircumference').textContent = c.toFixed(4);
      document.getElementById('resArcLength').textContent = arcLen.toFixed(4);
      document.getElementById('resSectorArea').textContent = sectorArea.toFixed(4);
      document.getElementById('resChordLength').textContent = chordLen.toFixed(4);
      document.getElementById('resSegmentArea').textContent = segmentArea.toFixed(4);
      document.getElementById('resSagitta').textContent = sagitta.toFixed(4);

      let stepsHtml = `1. Derived Radius: r = ${r.toFixed(4)}<br>`;
      stepsHtml += `2. Diameter: d = 2 × ${r.toFixed(4)} = ${d.toFixed(4)}<br>`;
      stepsHtml += `3. Circumference: C = 2π × ${r.toFixed(4)} = ${c.toFixed(4)}<br>`;
      stepsHtml += `4. Total Area: A = π × (${r.toFixed(4)})² = ${a.toFixed(4)}<br>`;
      stepsHtml += `5. Central Angle: θ = ${thetaDeg}° (${thetaRad.toFixed(4)} rad)<br>`;
      stepsHtml += `6. Arc Length: s = r × θ = ${r.toFixed(4)} × ${thetaRad.toFixed(4)} = ${arcLen.toFixed(4)}<br>`;
      stepsHtml += `7. Sector Area: A_sec = ½ × r² × θ = ${sectorArea.toFixed(4)}<br>`;
      stepsHtml += `8. Chord Length: c = 2r × sin(θ/2) = 2(${r.toFixed(4)}) × sin(${ (thetaDeg/2).toFixed(1) }°) = ${chordLen.toFixed(4)}`;

      document.getElementById('circleStepsDisplay').innerHTML = stepsHtml;
    }

    document.getElementById('circleInputMode').addEventListener('change', updateCircleInputLabel);
    document.getElementById('primaryValue').addEventListener('input', calcCircle);
    document.getElementById('sectorAngle').addEventListener('input', calcCircle);
    updateCircleInputLabel();
  </script>
</body>
</html>
"""

# Write files
with open(os.path.join(BASE_DIR, 'arithmetic-sequence-calculator.html'), 'w', encoding='utf-8') as f:
    f.write(arith_seq_html)
print("Generated arithmetic-sequence-calculator.html successfully!")

with open(os.path.join(BASE_DIR, 'circle-calculator.html'), 'w', encoding='utf-8') as f:
    f.write(circle_html)
print("Generated circle-calculator.html successfully!")
