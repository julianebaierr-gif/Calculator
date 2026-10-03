# -*- coding: utf-8 -*-
"""
Generator for Batch 31 - Part 2:
3. permutation-combination-calculator.html
4. probability-calculator.html
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 3. permutation-combination-calculator.html
HTML_PERM_COMB = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Permutation and Combination Calculator - nPr &amp; nCr Combinatorics Solver</title>
  <meta name="description" content="Calculate permutations (nPr) and combinations (nCr) with and without repetition. Includes factorials, stars and bars, step-by-step math, and formulas.">
  <link rel="canonical" href="https://calchub.org/permutation-combination-calculator.html">
  <meta property="og:title" content="Permutation and Combination Calculator - nPr &amp; nCr Solver">
  <meta property="og:description" content="Free combinatorics calculator. Compute permutations nPr, combinations nCr, permutations with repetition n^r, and multiset combinations with step-by-step proofs.">
  <meta property="og:url" content="https://calchub.org/permutation-combination-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Permutation &amp; Combination Calculator - nPr and nCr">
  <meta name="twitter:description" content="Calculate permutations and combinations with or without replacement. Full step-by-step factorial breakdowns, worked examples, and formulas.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Permutation and Combination Calculator",
    "url": "https://calchub.org/permutation-combination-calculator.html",
    "description": "Calculates permutations nPr, combinations nCr, arrangements with repetition, and multiset combinations with complete step-by-step factorial evaluations.",
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
        "name": "What is the core difference between a permutation and a combination?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The fundamental difference is whether arrangement order matters. In permutations, sequence and order are critical (e.g., lock codes where 1-2-3 differs from 3-2-1). In combinations, order is irrelevant; only the composition of the selected subset matters (e.g., a hand of cards or a committee)."
        }
      },
      {
        "@type": "Question",
        "name": "What are the formulas for nPr and nCr without repetition?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The permutation formula is P(n, r) = n! / (n - r)!. The combination formula is C(n, r) = n! / [r! * (n - r)!]. Notice that C(n, r) = P(n, r) / r!, dividing out the r! redundant internal permutations of the selected items."
        }
      },
      {
        "@type": "Question",
        "name": "How do you calculate combinations when repetition or replacement is allowed?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "When items can be chosen multiple times without regard to order (multisets), use the stars and bars formula: C_rep(n, r) = (n + r - 1)! / [r! * (n - 1)!] = C(n + r - 1, r)."
        }
      },
      {
        "@type": "Question",
        "name": "Can r be greater than n in permutations and combinations?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Without repetition, r cannot exceed n because you cannot select more unique items than exist in the pool; C(n, r) = P(n, r) = 0 when r > n. However, with repetition allowed, r can be arbitrarily larger than n (for example, rolling a 6-sided die 20 times yields 6^20 permutations)."
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
        <a href="math.html" class="active">Math &amp; Statistics</a>
        <a href="converter.html">Converters</a>
        <a href="engineering.html">Engineering</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="calculator-container">
    <div class="calculator-header">
      <div class="calc-icon" aria-hidden="true">&#9881;</div>
      <h1>Permutation and Combination Calculator</h1>
      <p class="calc-description">Compute permutations (nPr), combinations (nCr), arrangements with repetition, and multiset selections with step-by-step factorial expansions.</p>
    </div>

    <div class="calculator-body">
      <div class="input-grid">
        <div class="input-group">
          <label for="n-val">Total Number of Items (n)</label>
          <input type="number" id="n-val" class="form-control" value="8" min="0" max="100" step="1">
          <span class="help-text">Size of the universal set (integer &ge; 0)</span>
        </div>
        <div class="input-group">
          <label for="r-val">Items Selected / Subgroup (r)</label>
          <input type="number" id="r-val" class="form-control" value="3" min="0" max="100" step="1">
          <span class="help-text">Number of items chosen (integer &ge; 0)</span>
        </div>
      </div>

      <div style="display:flex; gap:12px; margin-top:16px;">
        <button id="calc-btn" class="btn-primary" onclick="calculatePermComb()" style="flex:1;">Compute Combinatorics</button>
        <button id="reset-btn" class="btn-secondary" onclick="resetPermComb()">Reset</button>
      </div>

      <div id="result-box" class="result-box" style="margin-top:24px;">
        <h2 class="result-title">Combinatorial Solutions Summary</h2>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap:16px; margin-bottom:20px;">
          <div style="background:var(--bg-subtle, #f8fafc); border:1px solid #BFDBFE; border-radius:8px; padding:16px; text-align:center;">
            <div style="font-size:0.85rem; font-weight:600; color:var(--text-muted, #64748B); text-transform:uppercase;">Combinations (nCr)</div>
            <div style="font-size:1.8rem; font-weight:800; color:var(--primary, #2563EB); margin:8px 0;" id="res-ncr">56</div>
            <div style="font-size:0.8rem; color:var(--text-muted, #64748B);">Order does NOT matter, No repetition</div>
          </div>
          <div style="background:var(--bg-subtle, #f8fafc); border:1px solid #BFDBFE; border-radius:8px; padding:16px; text-align:center;">
            <div style="font-size:0.85rem; font-weight:600; color:var(--text-muted, #64748B); text-transform:uppercase;">Permutations (nPr)</div>
            <div style="font-size:1.8rem; font-weight:800; color:var(--primary, #2563EB); margin:8px 0;" id="res-npr">336</div>
            <div style="font-size:0.8rem; color:var(--text-muted, #64748B);">Order MATTERS, No repetition</div>
          </div>
          <div style="background:var(--bg-subtle, #f8fafc); border:1px solid var(--border-color, #e2e8f0); border-radius:8px; padding:16px; text-align:center;">
            <div style="font-size:0.85rem; font-weight:600; color:var(--text-muted, #64748B); text-transform:uppercase;">Permutations with Repetition (nʳ)</div>
            <div style="font-size:1.8rem; font-weight:800; color:var(--text-dark, #0F172A); margin:8px 0;" id="res-npr-rep">512</div>
            <div style="font-size:0.8rem; color:var(--text-muted, #64748B);">Order MATTERS, Repetition allowed</div>
          </div>
          <div style="background:var(--bg-subtle, #f8fafc); border:1px solid var(--border-color, #e2e8f0); border-radius:8px; padding:16px; text-align:center;">
            <div style="font-size:0.85rem; font-weight:600; color:var(--text-muted, #64748B); text-transform:uppercase;">Combinations with Repetition</div>
            <div style="font-size:1.8rem; font-weight:800; color:var(--text-dark, #0F172A); margin:8px 0;" id="res-ncr-rep">120</div>
            <div style="font-size:0.8rem; color:var(--text-muted, #64748B);">Order does NOT matter, Repetition allowed</div>
          </div>
        </div>

        <h3 style="margin-top:20px; font-size:1.1rem; color:var(--text-dark);">Step-by-Step Mathematical Factorial Expansions</h3>
        <div id="res-steps" style="background:var(--bg-subtle, #f8fafc); padding:16px; border-radius:8px; font-family:monospace; font-size:0.95rem; white-space:pre-wrap; border:1px solid var(--border-color, #e2e8f0);"></div>
      </div>
    </div>

    <article class="article-body">
      <h2>Comprehensive Engineering &amp; Mathematical Guide to Combinatorics</h2>
      <p>Combinatorics is the fundamental branch of pure mathematics and theoretical computer science that studies the enumeration, arrangement, and operational grouping of elements from finite sets. Whether designing fault-tolerant cryptographic keys, estimating lottery odds in actuarial risk models, allocating computing threads in distributed clusters, or designing randomized clinical trials, the twin concepts of permutations and combinations govern the combinatorial state space.</p>

      <p>The core distinction in combinatorics answers a single essential question: <em>Does the sequential order of selection matter?</em> If altering the order produces a distinct outcome (such as a keypad passcode or a race podium ranking), the problem is a <strong>permutation</strong>. If changing the order results in the identical physical collection (such as a poker hand, a lottery draw, or a legislative committee), the problem is a <strong>combination</strong>. Related factorial principles are also explored in our <a href="factorial-calculator.html">Factorial Calculator</a>.</p>

      <h2>The Four Fundamental Combinatorial Regimes</h2>
      <p>Depending on whether order matters and whether replacement is permitted, all discrete selection problems fall into one of four mathematical frameworks:</p>

      <h3>1. Permutations Without Repetition (\(nPr\))</h3>
      <p>When selecting \(r\) items from a pool of \(n\) distinct items where each item can only be picked once and order matters, the first position can be filled in \(n\) ways, the second in \(n - 1\) ways, and so on until the \(r\)-th position, which has \(n - r + 1\) options. By the Fundamental Counting Principle, the product is expressed concisely using <a href="factorial-calculator.html">factorials</a>:</p>
      $$P(n, r) = n \times (n - 1) \times (n - 2) \times \dots \times (n - r + 1) = \frac{n!}{(n - r)!}$$
      <p>Where \(n \ge r \ge 0\). When all \(n\) items are arranged (\(r = n\)), \(P(n, n) = \frac{n!}{0!} = n!\) (since \(0! = 1\) by definition).</p>

      <h3>2. Combinations Without Repetition (\(nCr\))</h3>
      <p>In combinations, we seek the number of unique subsets of size \(r\) that can be formed from \(n\) items without regard to order. Because every subset of size \(r\) can be internally ordered in \(r!\) different ways, the number of permutations \(P(n, r)\) overcounts each unique combination exactly \(r!\) times. Dividing out this redundancy yields the binomial coefficient \(\binom{n}{r}\):</p>
      $$C(n, r) = \binom{n}{r} = \frac{P(n, r)}{r!} = \frac{n!}{r!(n - r)!}$$
      <p>Combinations exhibit fundamental algebraic symmetry: \(\binom{n}{r} = \binom{n}{n - r}\). Choosing \(r\) items to include is mathematically identical to choosing \(n - r\) items to exclude.</p>

      <h3>3. Permutations With Repetition (\(n^r\))</h3>
      <p>When an item can be chosen repeatedly across \(r\) positions and sequential order matters (such as generating an \(r\)-digit alphanumeric password from an alphabet of \(n\) characters), each position independently has \(n\) possibilities:</p>
      $$P_{\text{rep}}(n, r) = \underbrace{n \times n \times \dots \times n}_{r \text{ factors}} = n^r$$
      <p>Unlike non-repeating permutations, there is no restriction that \(r \le n\); \(r\) can be arbitrarily large.</p>

      <h3>4. Combinations With Repetition (Multisets &amp; Stars and Bars)</h3>
      <p>When selecting \(r\) items from \(n\) categories where each category has an unlimited supply of identical items and order does not matter (e.g., purchasing 10 scoops of ice cream from 4 available flavors), we apply the Stars and Bars theorem formulated by William Feller. The problem maps to arranging \(r\) identical items ("stars") and \(n - 1\) category dividers ("bars") in a sequence of length \(r + n - 1\):</p>
      $$C_{\text{rep}}(n, r) = \binom{n + r - 1}{r} = \frac{(n + r - 1)!}{r!(n - 1)!}$$

      <h2>Algebraic Identities &amp; Algorithmic Stability</h2>
      <p>In software implementations, computing \(n!\) directly for values like \(n = 50\) results in numbers exceeding \(10^{64}\), instantly causing 64-bit integer overflow. To compute combinations with absolute precision, modern software evaluates the multiplicative formula:</p>
      $$\binom{n}{r} = \prod_{i=1}^{r} \frac{n - r + i}{i} = \frac{n - r + 1}{1} \times \frac{n - r + 2}{2} \times \dots \times \frac{n}{r}$$
      <p>By dividing by \(i\) at each iterative step, every intermediate product remains an exact integer, eliminating both overflow and floating-point rounding errors. Combinations also satisfy Pascal's Identity:</p>
      $$\binom{n}{r} = \binom{n - 1}{r - 1} + \binom{n - 1}{r}$$

      <h2>Combinatorial Metrics &amp; Formula Benchmark Reference</h2>
      <p>The following technical reference table synthesizes the four combinatorial paradigms, their mathematical expressions, order constraints, and typical applications:</p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Combinatorial Framework</th>
            <th>Notation</th>
            <th>Closed-Form Formula</th>
            <th>Order Sensitivity</th>
            <th>Repetition Allowed?</th>
            <th>Typical Real-World Use Case</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Permutation (No Repetition)</td>
            <td>\(nPr\) or \(P(n, r)\)</td>
            <td>\(\frac{n!}{(n - r)!}\)</td>
            <td>Yes (Strict)</td>
            <td>No</td>
            <td>Podium finishes, password permutations, task schedules</td>
          </tr>
          <tr>
            <td>Combination (No Repetition)</td>
            <td>\(nCr\) or \(\binom{n}{r}\)</td>
            <td>\(\frac{n!}{r!(n - r)!}\)</td>
            <td>No (Ignored)</td>
            <td>No</td>
            <td>Lottery numbers, poker hands, committee selection</td>
          </tr>
          <tr>
            <td>Permutation With Repetition</td>
            <td>\(n^r\)</td>
            <td>\(n^r\)</td>
            <td>Yes (Strict)</td>
            <td>Yes</td>
            <td>PIN codes, IP address octets, DNA sequence strings</td>
          </tr>
          <tr>
            <td>Combination With Repetition</td>
            <td>\(\left(\!\binom{n}{r}\!\right)\)</td>
            <td>\(\frac{(n + r - 1)!}{r!(n - 1)!}\)</td>
            <td>No (Ignored)</td>
            <td>Yes</td>
            <td>Inventory stocking, coin change combinations, multisets</td>
          </tr>
          <tr>
            <td>Circular Permutation</td>
            <td>\(P_{\text{circ}}(n)\)</td>
            <td>\((n - 1)!\)</td>
            <td>Relative only</td>
            <td>No</td>
            <td>Seating arrangements around a circular table, bead necklaces</td>
          </tr>
          <tr>
            <td>Multinomial Permutation</td>
            <td>\(\binom{n}{k_1, \dots, k_m}\)</td>
            <td>\(\frac{n!}{k_1! k_2! \dots k_m!}\)</td>
            <td>Yes (Strict)</td>
            <td>Specified counts</td>
            <td>Anagrams of words with repeated letters (e.g., MISSISSIPPI)</td>
          </tr>
        </tbody>
      </table>

      <h2>Real-World Engineering, Cybersecurity &amp; Actuarial Case Studies</h2>
      <p>The following worked case studies demonstrate how combinatorial algorithms solve practical problems in cryptography, game theory, and software test engineering.</p>

      <div class="worked-example-card">
        <h3>Case Study 1: Cryptographic Entropy &amp; Alphanumeric Password Search Space</h3>
        <p><strong>Scenario:</strong> A cybersecurity architect defines authentication policies for a banking portal. Passwords must be exactly 8 characters long chosen from a character pool consisting of lowercase letters (26), uppercase letters (26), and digits (10), totaling \(n = 62\) available characters. The architect must calculate the total search space when characters can repeat versus a restricted policy where characters cannot repeat.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Identify pool size \(n = 62\) and password length \(r = 8\).</li>
          <li>Calculate password permutations with repetition allowed (\(n^r\)):
            $$P_{\text{rep}} = 62^8 \approx 2.1834 \times 10^{14} \text{ combinations}$$
          </li>
          <li>Calculate password permutations without repetition (\(nPr\)):
            $$P(62, 8) = \frac{62!}{(62 - 8)!} = \frac{62!}{54!} = 62 \times 61 \times 60 \times 59 \times 58 \times 57 \times 56 \times 55$$
            $$P(62, 8) \approx 1.3632 \times 10^{14} \text{ combinations}$$
          </li>
          <li>Calculate search space reduction factor:
            $$\text{Reduction} = \frac{2.1834 \times 10^{14} - 1.3632 \times 10^{14}}{2.1834 \times 10^{14}} \times 100\% \approx 37.56\%$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> Permitting repetition yields \(2.1834 \times 10^{14}\) permutations. Restricting passwords to unique non-repeating characters reduces brute-force search complexity by over \(37.5\%\), demonstrating why modern security standards advise against disallowing repeated characters.</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Actuarial Lottery Jackpot Odds Calculation</h3>
        <p><strong>Scenario:</strong> A state lottery requires players to select 6 numbers from a pool of 49 distinct integers (1 to 49) without repetition, where order of selection does not matter. An actuarial risk analyst must compute the total number of possible combinations to verify the exact probability of winning the jackpot.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Identify total pool \(n = 49\) and selection size \(r = 6\).</li>
          <li>Apply the combination formula without repetition:
            $$C(49, 6) = \frac{49!}{6!(49 - 6)!} = \frac{49!}{6! \times 43!}$$
          </li>
          <li>Expand factorials and simplify by canceling \(43!\):
            $$C(49, 6) = \frac{49 \times 48 \times 47 \times 46 \times 45 \times 44}{6 \times 5 \times 4 \times 3 \times 2 \times 1}$$
          </li>
          <li>Perform sequential integer divisions:
            $$C(49, 6) = \frac{10,068,347,520}{720} = 13,983,816$$
          </li>
          <li>Compute single-ticket win probability:
            $$P(\text{Jackpot}) = \frac{1}{13,983,816} \approx 7.1511 \times 10^{-8}$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> There are exactly \(13,983,816\) possible lottery combinations, resulting in an exact individual winning probability of \(1\) in \(13,983,816\).</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 3: Software QA Pairwise Test Configuration Combinations</h3>
        <p><strong>Scenario:</strong> A software QA automation engineer designs an integration test suite across 5 independent microservices. A complete system test requires forming test clusters consisting of exactly 3 microservices at a time. The engineer must determine how many unique 3-service test environments must be provisioned.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Identify total microservices \(n = 5\) and cluster size \(r = 3\).</li>
          <li>Apply the combinations formula:
            $$C(5, 3) = \frac{5!}{3!(5 - 3)!} = \frac{5!}{3! \times 2!} = \frac{120}{6 \times 2} = 10$$
          </li>
          <li>Verify using binomial symmetry:
            $$C(5, 3) = C(5, 5 - 3) = C(5, 2) = \frac{5 \times 4}{2 \times 1} = 10$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> Exactly 10 unique 3-service test environments must be configured to achieve full combinatorial coverage across the system.</p>
      </div>

      <h2>Frequently Asked Questions</h2>
      <div class="faq-item">
        <div class="faq-question">Why is 0 factorial equal to 1 (0! = 1)?</div>
        <div class="faq-answer">In combinatorics, \(0!\) represents the number of ways to arrange zero items, and there is exactly one way to do nothing (the empty set). Algebraically, the recurrence relation \(n! = n \times (n - 1)!\) for \(n = 1\) states \(1! = 1 \times 0!\), which necessitates \(0! = 1\). This definition also preserves the consistency of formulas like \(P(n, n) = n! / 0! = n!\).</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">How does nCr relate to the binomial expansion theorem?</div>
        <div class="faq-answer">The coefficients in the binomial expansion of \((x + y)^n = \sum_{r=0}^n \binom{n}{r} x^{n-r} y^r\) are exactly the combination values \(nCr\). When multiplying \(n\) identical factors of \((x + y)\), the term \(x^{n-r}y^r\) is generated by choosing \(y\) from \(r\) of the factors and \(x\) from the remaining \(n - r\) factors. There are \(\binom{n}{r}\) ways to make this selection.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Why is C(n, r) always an integer?</div>
        <div class="faq-answer">\(C(n, r)\) is always an exact integer because it counts the number of distinct subsets in a physical set, which cannot be fractional. Mathematically, in the product of any \(r\) consecutive integers \(n(n - 1)\dots(n - r + 1)\), there is guaranteed to be at least one multiple of 2, one multiple of 3, up to a multiple of \(r\), ensuring that \(r!\) divides the numerator evenly.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">What is a multiset and how does it relate to combinations with repetition?</div>
        <div class="faq-answer">In standard set theory, sets cannot contain duplicate elements. A multiset is a generalized set that allows elements to appear with multiplicities. Choosing a sub-multiset of size \(r\) from \(n\) available types corresponds precisely to combinations with repetition, evaluated via the formula \(\binom{n + r - 1}{r}\).</div>
      </div>
    </article>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-col">
        <h4>CalcHub</h4>
        <p>Comprehensive mathematical, statistical, and engineering calculation tools.</p>
      </div>
      <div class="footer-col">
        <h4>Discipline Hubs</h4>
        <ul class="footer-links">
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="math.html">Mathematics</a></li>
          <li><a href="converter.html">Unit Converters</a></li>
          <li><a href="engineering.html">Electrical &amp; Engineering</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 CalcHub. All rights reserved. Peer-reviewed computational algorithms.</p>
    </div>
  </footer>

  <script>
    // BigInt factorial implementation for large n up to 100
    function bigFactorial(num) {
      var res = BigInt(1);
      for (var i = BigInt(2); i <= BigInt(num); i++) {
        res *= i;
      }
      return res;
    }

    function bigNpr(n, r) {
      if (r < 0 || r > n) return BigInt(0);
      var res = BigInt(1);
      for (var i = BigInt(n); i > BigInt(n - r); i--) {
        res *= i;
      }
      return res;
    }

    function bigNcr(n, r) {
      if (r < 0 || r > n) return BigInt(0);
      if (r === 0 || r === n) return BigInt(1);
      if (r > n / 2) r = n - r;
      var num = BigInt(1);
      var den = BigInt(1);
      for (var i = 1; i <= r; i++) {
        num *= BigInt(n - r + i);
        den *= BigInt(i);
      }
      return num / den;
    }

    function bigPow(base, exp) {
      var res = BigInt(1);
      var b = BigInt(base);
      for (var i = 0; i < exp; i++) {
        res *= b;
      }
      return res;
    }

    function formatBig(val) {
      var str = val.toString();
      if (str.length > 18) {
        var exp = str.length - 1;
        var mantissa = str[0] + "." + str.substring(1, 5);
        return mantissa + " × 10<sup>" + exp + "</sup>";
      }
      return val.toLocaleString();
    }

    function calculatePermComb() {
      var n = parseInt(document.getElementById('n-val').value, 10);
      var r = parseInt(document.getElementById('r-val').value, 10);

      if (isNaN(n) || isNaN(r) || n < 0 || r < 0) {
        showError("Please enter non-negative integers for both n and r.");
        return;
      }

      if (n > 100 || r > 100) {
        showError("Values of n and r must be 100 or less to ensure numerical safety.");
        return;
      }

      var ncrVal = bigNcr(n, r);
      var nprVal = bigNpr(n, r);
      var nprRep = bigPow(n, r);
      var ncrRep = (n === 0 && r > 0) ? BigInt(0) : bigNcr(n + r - 1, r);

      document.getElementById('res-ncr').innerHTML = (r > n) ? "0 (r &gt; n)" : formatBig(ncrVal);
      document.getElementById('res-npr').innerHTML = (r > n) ? "0 (r &gt; n)" : formatBig(nprVal);
      document.getElementById('res-npr-rep').innerHTML = formatBig(nprRep);
      document.getElementById('res-ncr-rep').innerHTML = (n === 0 && r > 0) ? "0" : formatBig(ncrRep);

      var steps = "Parameters: Universal Pool n = " + n + ", Selected Items r = " + r + "\n\n" +
                  "1. Combinations (Order irrelevant, No repetition):\n" +
                  "   Formula: C(n, r) = n! / [r! * (n - r)!]\n";
      if (r <= n) {
        steps += "   C(" + n + ", " + r + ") = " + n + "! / [" + r + "! * (" + n + " - " + r + ")!]\n" +
                 "   C(" + n + ", " + r + ") = " + n + "! / [" + r + "! * " + (n - r) + "!] = " + ncrVal.toString() + "\n\n";
      } else {
        steps += "   Result: 0 (Cannot select " + r + " unique items from a set of size " + n + ")\n\n";
      }

      steps += "2. Permutations (Order matters, No repetition):\n" +
               "   Formula: P(n, r) = n! / (n - r)!\n";
      if (r <= n) {
        steps += "   P(" + n + ", " + r + ") = " + n + "! / (" + (n - r) + "!) = " + nprVal.toString() + "\n\n";
      } else {
        steps += "   Result: 0 (r exceeds n without repetition)\n\n";
      }

      steps += "3. Permutations with Repetition (Order matters, Repetition allowed):\n" +
               "   Formula: n^r = " + n + "^" + r + " = " + nprRep.toString() + "\n\n" +
               "4. Combinations with Repetition (Multiset selection):\n" +
               "   Formula: C(n + r - 1, r) = (" + n + " + " + r + " - 1)! / [" + r + "! * (" + n + " - 1)!]\n" +
               "   C(" + (n + r - 1) + ", " + r + ") = " + ncrRep.toString();

      document.getElementById('res-steps').innerText = steps;
    }

    function showError(msg) {
      document.getElementById('res-ncr').innerText = "Error";
      document.getElementById('res-npr').innerText = "Error";
      document.getElementById('res-npr-rep').innerText = "Error";
      document.getElementById('res-ncr-rep').innerText = "Error";
      document.getElementById('res-steps').innerText = "Error: " + msg;
    }

    function resetPermComb() {
      document.getElementById('n-val').value = '8';
      document.getElementById('r-val').value = '3';
      calculatePermComb();
    }

    window.addEventListener('DOMContentLoaded', function() {
      calculatePermComb();
    });
  </script>
</body>
</html>
"""

# 4. probability-calculator.html
HTML_PROBABILITY = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Probability Calculator - Single, Compound Events &amp; Bayes' Theorem</title>
  <meta name="description" content="Calculate single event probability, compound probabilities (AND, OR, NOT), conditional probability P(A|B), and Bayes' theorem with step-by-step math.">
  <link rel="canonical" href="https://calchub.org/probability-calculator.html">
  <meta property="og:title" content="Probability Calculator - Single &amp; Compound Events Solver">
  <meta property="og:description" content="Free statistical probability calculator. Compute union P(A U B), intersection P(A and B), conditional P(A|B), odds ratios, and Bayes' theorem updates.">
  <meta property="og:url" content="https://calchub.org/probability-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Probability Calculator - Multi-Event &amp; Bayesian Solver">
  <meta name="twitter:description" content="Calculate probability of single events, independent/dependent events, complement, union, intersection, and Bayes' rule with complete step-by-step proofs.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Probability Calculator",
    "url": "https://calchub.org/probability-calculator.html",
    "description": "Calculates probability of single events, independent and mutually exclusive compound events, conditional probabilities, odds, and Bayes' theorem.",
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
        "name": "What is the formula for the probability of A OR B occurring?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "By the general addition rule of probability, P(A or B) = P(A union B) = P(A) + P(B) - P(A and B). If events A and B are mutually exclusive (cannot occur simultaneously), P(A and B) = 0, simplifying to P(A or B) = P(A) + P(B)."
        }
      },
      {
        "@type": "Question",
        "name": "How do you calculate the probability of two independent events both occurring?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "By the multiplication rule for independent events, the probability of both events occurring is the product of their individual probabilities: P(A and B) = P(A intersect B) = P(A) * P(B)."
        }
      },
      {
        "@type": "Question",
        "name": "What is Bayes' Theorem and what is its mathematical formula?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Bayes' Theorem updates the conditional probability of an event given prior knowledge of related conditions: P(A|B) = [P(B|A) * P(A)] / P(B). By the law of total probability, P(B) = P(B|A)*P(A) + P(B|not A)*P(not A)."
        }
      },
      {
        "@type": "Question",
        "name": "What is the relationship between probability and odds in favor of an event?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Probability expresses favorable outcomes relative to all possible outcomes: P = F / (F + U). Odds in favor express favorable outcomes directly relative to unfavorable outcomes: Odds = P / (1 - P) or F : U."
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
        <a href="math.html" class="active">Math &amp; Statistics</a>
        <a href="converter.html">Converters</a>
        <a href="engineering.html">Engineering</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="calculator-container">
    <div class="calculator-header">
      <div class="calc-icon" aria-hidden="true">&#127922;</div>
      <h1>Probability Calculator</h1>
      <p class="calc-description">Compute single event probability, compound probabilities (A or B, A and B), conditional probability, odds ratios, and Bayes' Theorem updates.</p>
    </div>

    <div class="calculator-body">
      <div class="input-group">
        <label for="prob-mode">Probability Model</label>
        <select id="prob-mode" class="form-control" onchange="switchProbMode()">
          <option value="two-events" selected>Two Events A &amp; B (Union, Intersection &amp; Conditional)</option>
          <option value="single-event">Single Event P(A) (Favorable vs Total Outcomes)</option>
          <option value="bayes">Bayes' Theorem (Prior, Likelihood &amp; Posterior)</option>
        </select>
      </div>

      <!-- Mode 1: Two Events A & B -->
      <div id="panel-two-events" class="prob-panel">
        <div class="input-grid">
          <div class="input-group">
            <label for="p-a">Probability of Event A: P(A)</label>
            <input type="number" id="p-a" class="form-control" value="0.40" min="0" max="1" step="0.01">
            <span class="help-text">Decimal between 0.0 and 1.0 (or %)</span>
          </div>
          <div class="input-group">
            <label for="p-b">Probability of Event B: P(B)</label>
            <input type="number" id="p-b" class="form-control" value="0.50" min="0" max="1" step="0.01">
            <span class="help-text">Decimal between 0.0 and 1.0 (or %)</span>
          </div>
        </div>

        <div class="input-group">
          <label for="rel-type">Relationship Between Event A and Event B</label>
          <select id="rel-type" class="form-control" onchange="toggleIntersectionInput()">
            <option value="independent" selected>Independent Events: P(A &cap; B) = P(A) &times; P(B)</option>
            <option value="mutually-exclusive">Mutually Exclusive: P(A &cap; B) = 0</option>
            <option value="custom">Custom Intersection: Specify P(A &cap; B)</option>
          </select>
        </div>

        <div class="input-group" id="group-custom-intersection" style="display:none;">
          <label for="p-ab">Joint Probability: P(A &cap; B)</label>
          <input type="number" id="p-ab" class="form-control" value="0.10" min="0" max="1" step="0.01">
          <span class="help-text">Must satisfy P(A &cap; B) &le; min(P(A), P(B))</span>
        </div>
      </div>

      <!-- Mode 2: Single Event -->
      <div id="panel-single-event" class="prob-panel" style="display:none;">
        <div class="input-grid">
          <div class="input-group">
            <label for="single-fav">Number of Favorable Outcomes: n(A)</label>
            <input type="number" id="single-fav" class="form-control" value="3" min="0" step="1">
          </div>
          <div class="input-group">
            <label for="single-total">Total Sample Space Outcomes: n(S)</label>
            <input type="number" id="single-total" class="form-control" value="12" min="1" step="1">
          </div>
        </div>
      </div>

      <!-- Mode 3: Bayes' Theorem -->
      <div id="panel-bayes" class="prob-panel" style="display:none;">
        <div class="input-grid">
          <div class="input-group">
            <label for="bayes-prior">Prior Probability: P(A)</label>
            <input type="number" id="bayes-prior" class="form-control" value="0.01" min="0" max="1" step="0.001">
            <span class="help-text">Base rate / prior belief</span>
          </div>
          <div class="input-group">
            <label for="bayes-sens">True Positive Rate / Likelihood: P(B|A)</label>
            <input type="number" id="bayes-sens" class="form-control" value="0.95" min="0" max="1" step="0.01">
            <span class="help-text">Probability of test positive given condition</span>
          </div>
          <div class="input-group">
            <label for="bayes-fp">False Positive Rate: P(B|not A)</label>
            <input type="number" id="bayes-fp" class="form-control" value="0.05" min="0" max="1" step="0.01">
            <span class="help-text">Probability of positive given no condition</span>
          </div>
        </div>
      </div>

      <div class="input-group">
        <label for="precision-select">Decimal Precision</label>
        <select id="precision-select" class="form-control" onchange="calculateProbability()">
          <option value="2">2 decimal places</option>
          <option value="4" selected>4 decimal places</option>
          <option value="6">6 decimal places</option>
        </select>
      </div>

      <div style="display:flex; gap:12px; margin-top:16px;">
        <button id="calc-btn" class="btn-primary" onclick="calculateProbability()" style="flex:1;">Compute Probability</button>
        <button id="reset-btn" class="btn-secondary" onclick="resetProbability()">Reset</button>
      </div>

      <div id="result-box" class="result-box" style="margin-top:24px;">
        <h2 class="result-title">Probability Solutions &amp; Metrics</h2>
        <div class="result-highlight" style="font-size:1.8rem; font-weight:700; color:var(--primary); margin-bottom:16px;" id="res-main">
          P(A &cup; B) = 0.7000 (70.00%)
        </div>

        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:16px;" id="res-grid">
          <div><span class="res-label">P(A and B) / Intersection:</span> <strong class="res-val" id="res-intersection">0.2000 (20.00%)</strong></div>
          <div><span class="res-label">P(A only) / A \ B:</span> <strong class="res-val" id="res-a-only">0.2000 (20.00%)</strong></div>
          <div><span class="res-label">P(B only) / B \ A:</span> <strong class="res-val" id="res-b-only">0.3000 (30.00%)</strong></div>
          <div><span class="res-label">P(Neither A nor B):</span> <strong class="res-val" id="res-neither">0.3000 (30.00%)</strong></div>
          <div><span class="res-label">Conditional P(A|B):</span> <strong class="res-val" id="res-cond-ab">0.4000 (40.00%)</strong></div>
          <div><span class="res-label">Conditional P(B|A):</span> <strong class="res-val" id="res-cond-ba">0.5000 (50.00%)</strong></div>
        </div>

        <h3 style="margin-top:20px; font-size:1.1rem; color:var(--text-dark);">Step-by-Step Mathematical Derivation</h3>
        <div id="res-steps" style="background:var(--bg-subtle, #f8fafc); padding:16px; border-radius:8px; font-family:monospace; font-size:0.95rem; white-space:pre-wrap; border:1px solid var(--border-color, #e2e8f0);"></div>
      </div>
    </div>

    <article class="article-body">
      <h2>Comprehensive Engineering &amp; Statistical Guide to Probability</h2>
      <p>Probability is the mathematical calculus of uncertainty, measuring the likelihood that an uncertain event or proposition will occur. Formally codified by Andrey Kolmogorov in 1933 through axiomatic probability theory, modern probability forms the bedrock of quantum physics, actuarial insurance pricing, machine learning algorithms, statistical hypothesis testing, and mission-critical reliability engineering.</p>

      <p>Every probabilistic calculation operates within a defined <strong>sample space (\(S\))</strong>—the complete set of all possible mutually exclusive outcomes of a random trial. An <strong>event (\(A\))</strong> represents any defined subset of the sample space. Kolmogorov's three fundamental axioms establish the mathematical boundaries of probability:</p>
      <ol>
        <li><strong>Axiom of Non-negativity:</strong> For any event \(A\), \(0 \le P(A) \le 1\). An impossible event has \(P(\emptyset) = 0\), while an absolute certainty has \(P(S) = 1\).</li>
        <li><strong>Axiom of Unit Measure:</strong> The probability of the entire sample space equals unity: \(P(S) = 1\).</li>
        <li><strong>Axiom of Additivity:</strong> For any sequence of mutually exclusive (disjoint) events \(A_1, A_2, \dots\), the probability of their union is the sum of their individual probabilities: \(P(\bigcup A_i) = \sum P(A_i)\).</li>
      </ol>

      <h2>Mathematical Formulations for Single &amp; Compound Events</h2>
      <p>Depending on the causal relationship and dependence between events, different fundamental algebraic rules govern their joint probabilities.</p>

      <h3>1. Single Event &amp; Classical Complement Rule</h3>
      <p>In discrete sample spaces with equally likely outcomes (the Laplace classical model), the probability of event \(A\) is the ratio of favorable outcomes \(n(A)\) to total possible outcomes \(n(S)\):</p>
      $$P(A) = \frac{n(A)}{n(S)}$$
      <p>The probability of the complement event \(A'\) (the event that \(A\) does NOT happen) follows directly from unit measure:</p>
      $$P(A') = P(\text{not } A) = 1 - P(A)$$
      <p>The odds in favor of event \(A\) express the ratio of favorable outcomes to unfavorable outcomes: \(\text{Odds} = \frac{P(A)}{1 - P(A)}\).</p>

      <h3>2. General Addition Rule (Probability of A OR B: \(P(A \cup B)\))</h3>
      <p>When evaluating the probability that at least one of two events \(A\) or \(B\) occurs, summing \(P(A) + P(B)\) counts the overlap region (where both events occur simultaneously) twice. Subtracting the intersection corrects for this double-counting:</p>
      $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
      <p>If events \(A\) and \(B\) are <strong>mutually exclusive</strong> (disjoint), they cannot occur concurrently: \(P(A \cap B) = 0\). The formula simplifies to: \(P(A \cup B) = P(A) + P(B)\).</p>

      <h3>3. General Multiplication Rule &amp; Conditional Probability</h3>
      <p>The conditional probability \(P(A|B)\) represents the updated probability of event \(A\) occurring given that event \(B\) has already occurred. Restricting the effective sample space to event \(B\) yields:</p>
      $$P(A|B) = \frac{P(A \cap B)}{P(B)} \quad (\text{for } P(B) > 0)$$
      <p>Rearranging this definition produces the General Multiplication Rule for joint probability:</p>
      $$P(A \cap B) = P(B) \times P(A|B) = P(A) \times P(B|A)$$
      <p>Two events are formally defined as <strong>statistically independent</strong> if and only if knowledge of one provides zero information about the likelihood of the other: \(P(A|B) = P(A)\). For independent events, the intersection simplifies to the direct product:</p>
      $$P(A \cap B) = P(A) \times P(B)$$

      <h3>4. Bayes' Theorem &amp; Bayesian Updating</h3>
      <p>Named after Reverend Thomas Bayes (1701&ndash;1761), Bayes' Theorem provides a rigorous mathematical bridge between prior knowledge and observed evidence. It reverses conditional probabilities, calculating the posterior probability \(P(A|B)\) from the likelihood \(P(B|A)\) and prior probability \(P(A)\):</p>
      $$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$
      <p>By the Law of Total Probability, the marginal evidence \(P(B)\) is expanded across all mutually exclusive hypotheses (partition of sample space):</p>
      $$P(B) = P(B|A) \cdot P(A) + P(B|A') \cdot P(A')$$
      <p>Bayes' Theorem is the cornerstone of spam filtering algorithms, clinical medical diagnostics, robotic Bayesian SLAM navigation, and statistical machine learning.</p>

      <h2>Probability Rules &amp; Operations Reference Matrix</h2>
      <p>The following technical reference matrix compares standard probabilistic operators, Venn diagram interpretations, mathematical formulas, and sample constraints:</p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Probabilistic Operator</th>
            <th>Venn Diagram Region</th>
            <th>General Formula</th>
            <th>Independent Events Simplification</th>
            <th>Mutually Exclusive Simplification</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Union (\(A\) or \(B\))</td>
            <td>Entire shaded area of \(A\) and \(B\)</td>
            <td>\(P(A) + P(B) - P(A \cap B)\)</td>
            <td>\(P(A) + P(B) - P(A)P(B)\)</td>
            <td>\(P(A) + P(B)\)</td>
          </tr>
          <tr>
            <td>Intersection (\(A\) and \(B\))</td>
            <td>Overlap lens between \(A\) and \(B\)</td>
            <td>\(P(A) \cdot P(B|A)\)</td>
            <td>\(P(A) \cdot P(B)\)</td>
            <td>\(0.0000\) (Impossible)</td>
          </tr>
          <tr>
            <td>Difference (\(A\) only)</td>
            <td>Crescent of \(A\) excluding overlap</td>
            <td>\(P(A) - P(A \cap B)\)</td>
            <td>\(P(A)(1 - P(B))\)</td>
            <td>\(P(A)\)</td>
          </tr>
          <tr>
            <td>Joint Complement (Neither)</td>
            <td>Background area outside \(A\) and \(B\)</td>
            <td>\(1 - P(A \cup B)\)</td>
            <td>\((1 - P(A))(1 - P(B))\)</td>
            <td>\(1 - [P(A) + P(B)]\)</td>
          </tr>
          <tr>
            <td>Conditional (\(A\) given \(B\))</td>
            <td>Fraction of circle \(B\) inside \(A\)</td>
            <td>\(\frac{P(A \cap B)}{P(B)}\)</td>
            <td>\(P(A)\)</td>
            <td>\(0.0000\)</td>
          </tr>
          <tr>
            <td>Bayes' Posterior (\(A\) given evidence \(B\))</td>
            <td>Evidence normalization</td>
            <td>\(\frac{P(B|A)P(A)}{P(B)}\)</td>
            <td>\(P(A)\)</td>
            <td>\(0.0000\)</td>
          </tr>
        </tbody>
      </table>

      <h2>Real-World Engineering, Clinical &amp; Actuarial Case Studies</h2>
      <p>The following worked case studies demonstrate how probability formulas govern decisions in clinical diagnostics, aerospace redundancy engineering, and industrial quality control.</p>

      <div class="worked-example-card">
        <h3>Case Study 1: Medical Diagnostic Screening &amp; The Base Rate Fallacy (Bayes' Rule)</h3>
        <p><strong>Scenario:</strong> A clinical screening assay for a rare metabolic condition is evaluated in a general population. The disease prevalence (prior probability) is \(P(D) = 0.5\% = 0.005\). The assay has a sensitivity (true positive rate) of \(P(+|D) = 98.0\% = 0.98\), and a false positive rate of \(P(+|D') = 3.0\% = 0.03\). A patient receives a positive test result. The clinical director must calculate the true probability that the patient actually has the disease.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>State the known priors and likelihoods:
            $$P(D) = 0.005, \quad P(D') = 1 - 0.005 = 0.995$$
            $$P(+|D) = 0.98, \quad P(+|D') = 0.03$$
          </li>
          <li>Apply the Law of Total Probability to compute the total probability of a positive test \(P(+)\):
            $$P(+) = P(+|D)P(D) + P(+|D')P(D')$$
            $$P(+) = (0.98 \times 0.005) + (0.03 \times 0.995) = 0.0049 + 0.02985 = 0.03475$$
          </li>
          <li>Apply Bayes' Theorem to compute the posterior probability \(P(D|+)\):
            $$P(D|+) = \frac{P(+|D) \times P(D)}{P(+)} = \frac{0.0049}{0.03475} \approx 0.141007$$
          </li>
          <li>Express as a percentage:
            $$P(D|+) \approx 14.10\%$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> Despite the test being \(98\%\) accurate, a patient testing positive has only a \(14.10\%\) probability of actually having the condition. This counterintuitive result is the famous base rate fallacy: because the disease is rare (\(0.5\%\)), false positives from the large healthy population (\(0.02985\)) outnumber true positives (\(0.0049\)) by roughly 6 to 1.</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Aerospace Triply Redundant Flight Computer Reliability (Independence)</h3>
        <p><strong>Scenario:</strong> A commercial airliner utilizes three independent redundant flight control computers running identical flight management software. The probability of any single computer experiencing a hardware failure during a transatlantic flight is \(P(F) = 0.002\) (\(0.2\%\)). Hardware failures occur independently. The aerospace engineer must compute the probability that all three computers fail, and the probability that at least one computer remains operational.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Identify single computer failure probability \(P(F_1) = P(F_2) = P(F_3) = 0.002\).</li>
          <li>Calculate joint probability of total system failure (all three failing independently):
            $$P(\text{All 3 Fail}) = P(F_1 \cap F_2 \cap F_3) = 0.002 \times 0.002 \times 0.002 = 0.002^3$$
            $$P(\text{All 3 Fail}) = 8.0 \times 10^{-9} = 0.000000008$$
          </li>
          <li>Calculate probability that at least one computer survives (complement rule):
            $$P(\text{At least 1 Survives}) = 1 - P(\text{All 3 Fail}) = 1 - 8.0 \times 10^{-9} = 0.999999992$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> Triple modular redundancy reduces catastrophic flight computer failure risk to \(8\) in \(1\) billion (\(0.0000008\%\)), achieving FAA aircraft airworthiness safety standards.</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 3: Manufacturing QA Dual-Defect Inspection (Union Rule)</h3>
        <p><strong>Scenario:</strong> An electronics assembly line inspects circuit boards for two independent defects: soldering bridges (Defect A) with probability \(P(A) = 0.04\) (\(4.0\%\)), and component misalignment (Defect B) with probability \(P(B) = 0.06\) (\(6.0\%\)). A board is rejected if it has either defect or both. The QA engineer must calculate the overall rejection rate.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Since defects occur independently, compute joint defect rate:
            $$P(A \cap B) = P(A) \times P(B) = 0.04 \times 0.06 = 0.0024$$
          </li>
          <li>Apply the General Addition Rule:
            $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
            $$P(A \cup B) = 0.04 + 0.06 - 0.0024 = 0.10 - 0.0024 = 0.0976$$
          </li>
          <li>Convert to percentage:
            $$\text{Rejection Rate} = 9.76\%$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The manufacturing rejection rate is exactly \(9.76\%\), with \(90.24\%\) of boards passing inspection with zero defects.</p>
      </div>

      <h2>Frequently Asked Questions</h2>
      <div class="faq-item">
        <div class="faq-question">Why can't probabilities be added directly when events are not mutually exclusive?</div>
        <div class="faq-answer">When events are not mutually exclusive, they share overlapping outcomes where both events occur simultaneously (\(A \cap B\)). If you simply add \(P(A) + P(B)\), the outcomes in the intersection are added twice—once within \(P(A)\) and once within \(P(B)\). Subtracting \(P(A \cap B)\) ensures every outcome in the union is counted exactly once.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">What is the difference between independent events and mutually exclusive events?</div>
        <div class="faq-answer">They are polar opposites. Mutually exclusive events CANNOT happen together (\(P(A \cap B) = 0\)); if one occurs, the other is guaranteed not to occur. Independent events CAN happen together, and the occurrence of one provides zero information about the likelihood of the other (\(P(A \cap B) = P(A) \times P(B)\)). In fact, two non-zero events cannot be both independent and mutually exclusive.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">What is the Gambler's Fallacy?</div>
        <div class="faq-answer">The Gambler's Fallacy is the mistaken belief that past random outcomes affect the probability of future independent events. For example, if a fair coin lands on Heads 5 times in a row, the probability of Tails on the 6th flip remains exactly \(0.5\) (\(50\%\)). Independent trials have no memory.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">How do conditional probability and Bayes' Theorem differ?</div>
        <div class="faq-answer">Conditional probability is the general definition of updating a probability given new information: \(P(A|B) = P(A \cap B) / P(B)\). Bayes' Theorem is a specific algebraic formulation of conditional probability that expresses \(P(A|B)\) in terms of the reverse conditional probability \(P(B|A)\) and prior probabilities, enabling inference from evidence to hypothesis.</div>
      </div>
    </article>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-col">
        <h4>CalcHub</h4>
        <p>Comprehensive mathematical, statistical, and engineering calculation tools.</p>
      </div>
      <div class="footer-col">
        <h4>Discipline Hubs</h4>
        <ul class="footer-links">
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="math.html">Mathematics</a></li>
          <li><a href="converter.html">Unit Converters</a></li>
          <li><a href="engineering.html">Electrical &amp; Engineering</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 CalcHub. All rights reserved. Peer-reviewed computational algorithms.</p>
    </div>
  </footer>

  <script>
    function switchProbMode() {
      var mode = document.getElementById('prob-mode').value;
      var panels = document.querySelectorAll('.prob-panel');
      panels.forEach(function(p) { p.style.display = 'none'; });

      if (mode === 'two-events') document.getElementById('panel-two-events').style.display = 'block';
      else if (mode === 'single-event') document.getElementById('panel-single-event').style.display = 'block';
      else if (mode === 'bayes') document.getElementById('panel-bayes').style.display = 'block';

      calculateProbability();
    }

    function toggleIntersectionInput() {
      var rel = document.getElementById('rel-type').value;
      var grp = document.getElementById('group-custom-intersection');
      if (rel === 'custom') grp.style.display = 'block';
      else grp.style.display = 'none';
      calculateProbability();
    }

    function calculateProbability() {
      var mode = document.getElementById('prob-mode').value;
      var prec = parseInt(document.getElementById('precision-select').value, 10) || 4;

      if (mode === 'two-events') {
        var pa = parseFloat(document.getElementById('p-a').value);
        var pb = parseFloat(document.getElementById('p-b').value);
        var rel = document.getElementById('rel-type').value;

        if (isNaN(pa) || isNaN(pb) || pa < 0 || pa > 1 || pb < 0 || pb > 1) {
          showError("Probabilities P(A) and P(B) must be between 0.0 and 1.0.");
          return;
        }

        var pab = 0;
        if (rel === 'independent') {
          pab = pa * pb;
        } else if (rel === 'mutually-exclusive') {
          pab = 0;
          if (pa + pb > 1) {
            showError("Mutually exclusive events cannot have P(A) + P(B) > 1.0.");
            return;
          }
        } else if (rel === 'custom') {
          pab = parseFloat(document.getElementById('p-ab').value);
          if (isNaN(pab) || pab < 0 || pab > Math.min(pa, pb) || pab < Math.max(0, pa + pb - 1)) {
            showError("Joint probability P(A and B) must satisfy max(0, P(A)+P(B)-1) <= P(A and B) <= min(P(A), P(B)).");
            return;
          }
        }

        var pUnion = pa + pb - pab;
        var pAonly = pa - pab;
        var pBonly = pb - pab;
        var pNeither = 1 - pUnion;
        var pCondAB = (pb > 0) ? (pab / pb) : 0;
        var pCondBA = (pa > 0) ? (pab / pa) : 0;

        document.getElementById('res-main').innerText = "P(A ∪ B) = " + pUnion.toFixed(prec) + " (" + (pUnion * 100).toFixed(2) + "%)";
        document.getElementById('res-intersection').innerText = pab.toFixed(prec) + " (" + (pab * 100).toFixed(2) + "%)";
        document.getElementById('res-a-only').innerText = pAonly.toFixed(prec) + " (" + (pAonly * 100).toFixed(2) + "%)";
        document.getElementById('res-b-only').innerText = pBonly.toFixed(prec) + " (" + (pBonly * 100).toFixed(2) + "%)";
        document.getElementById('res-neither').innerText = pNeither.toFixed(prec) + " (" + (pNeither * 100).toFixed(2) + "%)";
        document.getElementById('res-cond-ab').innerText = (pb > 0) ? pCondAB.toFixed(prec) + " (" + (pCondAB * 100).toFixed(2) + "%)" : "Undefined";
        document.getElementById('res-cond-ba').innerText = (pa > 0) ? pCondBA.toFixed(prec) + " (" + (pCondBA * 100).toFixed(2) + "%)" : "Undefined";
        document.getElementById('res-grid').style.display = 'grid';

        var steps = "Mode: Two Events A & B (Relationship: " + rel + ")\n" +
                    "Input Probabilities: P(A) = " + pa.toFixed(prec) + ", P(B) = " + pb.toFixed(prec) + "\n\n" +
                    "1. Joint Probability (Intersection):\n" +
                    "   P(A ∩ B) = " + pab.toFixed(prec) + "\n\n" +
                    "2. General Addition Rule (Union: A or B):\n" +
                    "   P(A ∪ B) = P(A) + P(B) - P(A ∩ B)\n" +
                    "   P(A ∪ B) = " + pa.toFixed(prec) + " + " + pb.toFixed(prec) + " - " + pab.toFixed(prec) + " = " + pUnion.toFixed(prec) + "\n\n" +
                    "3. Component Breakdown:\n" +
                    "   P(A only) = P(A) - P(A ∩ B) = " + pAonly.toFixed(prec) + "\n" +
                    "   P(B only) = P(B) - P(A ∩ B) = " + pBonly.toFixed(prec) + "\n" +
                    "   P(Neither A nor B) = 1 - P(A ∪ B) = " + pNeither.toFixed(prec) + "\n\n" +
                    "4. Conditional Probabilities:\n" +
                    "   P(A|B) = P(A ∩ B) / P(B) = " + (pb > 0 ? (pab.toFixed(prec) + " / " + pb.toFixed(prec) + " = " + pCondAB.toFixed(prec)) : "Undefined") + "\n" +
                    "   P(B|A) = P(A ∩ B) / P(A) = " + (pa > 0 ? (pab.toFixed(prec) + " / " + pa.toFixed(prec) + " = " + pCondBA.toFixed(prec)) : "Undefined");

        document.getElementById('res-steps').innerText = steps;

      } else if (mode === 'single-event') {
        var fav = parseFloat(document.getElementById('single-fav').value);
        var total = parseFloat(document.getElementById('single-total').value);

        if (isNaN(fav) || isNaN(total) || fav < 0 || total <= 0 || fav > total) {
          showError("Favorable outcomes must be between 0 and total sample space outcomes.");
          return;
        }

        var pSingle = fav / total;
        var pComp = 1 - pSingle;
        var oddsFav = (pComp > 0) ? (pSingle / pComp) : Infinity;

        document.getElementById('res-main').innerText = "P(A) = " + pSingle.toFixed(prec) + " (" + (pSingle * 100).toFixed(2) + "%)";
        document.getElementById('res-grid').style.display = 'none';

        var steps = "Mode: Single Classical Event\n" +
                    "Favorable Outcomes n(A) = " + fav + "\n" +
                    "Total Outcomes n(S) = " + total + "\n\n" +
                    "1. Classical Probability Formula:\n" +
                    "   P(A) = n(A) / n(S) = " + fav + " / " + total + " = " + pSingle.toFixed(prec) + " (" + (pSingle * 100).toFixed(2) + "%)\n\n" +
                    "2. Complement Probability (A does not occur):\n" +
                    "   P(A') = 1 - P(A) = 1 - " + pSingle.toFixed(prec) + " = " + pComp.toFixed(prec) + " (" + (pComp * 100).toFixed(2) + "%)\n\n" +
                    "3. Odds in Favor:\n" +
                    "   Odds = " + fav + " : " + (total - fav) + (pComp > 0 ? (" (Ratio: " + oddsFav.toFixed(prec) + " to 1)") : " (Absolute Certainty)");

        document.getElementById('res-steps').innerText = steps;

      } else if (mode === 'bayes') {
        var prior = parseFloat(document.getElementById('bayes-prior').value);
        var sens = parseFloat(document.getElementById('bayes-sens').value);
        var fp = parseFloat(document.getElementById('bayes-fp').value);

        if ([prior, sens, fp].some(function(v) { return isNaN(v) || v < 0 || v > 1; })) {
          showError("All Bayesian probabilities must be real numbers between 0.0 and 1.0.");
          return;
        }

        var priorNotA = 1 - prior;
        var totalEvidence = (sens * prior) + (fp * priorNotA);
        var posterior = (totalEvidence > 0) ? ((sens * prior) / totalEvidence) : 0;

        document.getElementById('res-main').innerText = "Posterior P(A|B) = " + posterior.toFixed(prec) + " (" + (posterior * 100).toFixed(2) + "%)";
        document.getElementById('res-grid').style.display = 'none';

        var steps = "Mode: Bayes' Theorem Posterior Update\n" +
                    "Prior Probability P(A) = " + prior.toFixed(prec) + "\n" +
                    "Likelihood / Sensitivity P(B|A) = " + sens.toFixed(prec) + "\n" +
                    "False Positive Rate P(B|not A) = " + fp.toFixed(prec) + "\n\n" +
                    "1. Marginal Total Evidence P(B):\n" +
                    "   P(B) = P(B|A)*P(A) + P(B|not A)*P(not A)\n" +
                    "   P(B) = (" + sens.toFixed(prec) + " * " + prior.toFixed(prec) + ") + (" + fp.toFixed(prec) + " * " + priorNotA.toFixed(prec) + ")\n" +
                    "   P(B) = " + (sens * prior).toFixed(prec) + " + " + (fp * priorNotA).toFixed(prec) + " = " + totalEvidence.toFixed(prec) + "\n\n" +
                    "2. Posterior Probability P(A|B):\n" +
                    "   P(A|B) = [P(B|A) * P(A)] / P(B)\n" +
                    "   P(A|B) = " + (sens * prior).toFixed(prec) + " / " + totalEvidence.toFixed(prec) + " = " + posterior.toFixed(prec) + " (" + (posterior * 100).toFixed(2) + "%)";

        document.getElementById('res-steps').innerText = steps;
      }
    }

    function showError(msg) {
      document.getElementById('res-main').innerText = "Error";
      document.getElementById('res-steps').innerText = "Error: " + msg;
      document.getElementById('res-grid').style.display = 'none';
    }

    function resetProbability() {
      document.getElementById('prob-mode').value = 'two-events';
      document.getElementById('p-a').value = '0.40';
      document.getElementById('p-b').value = '0.50';
      document.getElementById('rel-type').value = 'independent';
      document.getElementById('single-fav').value = '3';
      document.getElementById('single-total').value = '12';
      document.getElementById('bayes-prior').value = '0.01';
      document.getElementById('bayes-sens').value = '0.95';
      document.getElementById('bayes-fp').value = '0.05';
      document.getElementById('precision-select').value = '4';
      switchProbMode();
    }

    window.addEventListener('DOMContentLoaded', function() {
      calculateProbability();
    });
  </script>
</body>
</html>
"""

def main():
    p3 = os.path.join(BASE_DIR, "permutation-combination-calculator.html")
    with open(p3, "w", encoding="utf-8") as f:
        f.write(HTML_PERM_COMB)
    print("Generated:", p3)

    p4 = os.path.join(BASE_DIR, "probability-calculator.html")
    with open(p4, "w", encoding="utf-8") as f:
        f.write(HTML_PROBABILITY)
    print("Generated:", p4)

if __name__ == "__main__":
    main()
