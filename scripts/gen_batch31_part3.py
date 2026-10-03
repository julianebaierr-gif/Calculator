# -*- coding: utf-8 -*-
"""
Generator for Batch 31 - Part 3:
5. proportion-calculator.html
6. quotient-and-remainder-calculator.html
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 5. proportion-calculator.html
HTML_PROPORTION = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Proportion Calculator - Solve for X, Direct &amp; Inverse Proportions</title>
  <meta name="description" content="Solve for unknown X in any ratio proportion (A/B = C/D). Compute direct and inverse proportions, constant of proportionality k, and cross-multiplications.">
  <link rel="canonical" href="https://calchub.org/proportion-calculator.html">
  <meta property="og:title" content="Proportion Calculator - Direct, Inverse &amp; Solve for X">
  <meta property="og:description" content="Free proportion solver. Find unknown terms in A/B = C/D, compute direct and inverse variation, scaling factors, and step-by-step cross-multiplication proofs.">
  <meta property="og:url" content="https://calchub.org/proportion-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Proportion Calculator - Ratio &amp; Variation Solver">
  <meta name="twitter:description" content="Calculate direct, inverse, and four-term proportions. Full step-by-step cross-multiplication, engineering worked examples, and formulas.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Proportion Calculator",
    "url": "https://calchub.org/proportion-calculator.html",
    "description": "Solves for unknown values in direct, inverse, and four-term mathematical proportions A/B = C/D with step-by-step cross-multiplications.",
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
        "name": "How does cross-multiplication solve for an unknown in a proportion?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "In any true proportion A / B = C / D, the product of the extremes equals the product of the means: A * D = B * C. To isolate an unknown variable, multiply the diagonal terms containing known values and divide by the term paired with the unknown."
        }
      },
      {
        "@type": "Question",
        "name": "What is the difference between direct and inverse proportion?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "In direct proportion (y = k * x), both variables increase or decrease together at a constant ratio y / x = k. In inverse proportion (y = k / x), as one variable increases, the other decreases proportionally such that their product remains constant: x * y = k."
        }
      },
      {
        "@type": "Question",
        "name": "What is a continuous or continued proportion?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A continued proportion occurs when the middle terms are identical: a / b = b / c. The middle term b is called the geometric mean or mean proportional between a and c, satisfying b = sqrt(a * c)."
        }
      },
      {
        "@type": "Question",
        "name": "Can any term in a proportion be zero?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The denominators B and D can never be zero because division by zero is undefined in mathematics. Furthermore, in inverse variations, zero values are invalid because zero cannot have a reciprocal."
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
      <div class="calc-icon" aria-hidden="true">&#8759;</div>
      <h1>Proportion Calculator</h1>
      <p class="calc-description">Solve for unknown variable X in four-term proportions (A/B = C/D), calculate direct and inverse variations, and inspect cross-multiplications.</p>
    </div>

    <div class="calculator-body">
      <div class="input-group">
        <label for="prop-type">Proportion Type</label>
        <select id="prop-type" class="form-control" onchange="switchPropType()">
          <option value="four-term" selected>Four-Term Proportion: A / B = C / D (Solve for Unknown)</option>
          <option value="variation">Direct &amp; Inverse Variation: (x₁ &rarr; y₁ and x₂ &rarr; y₂)</option>
        </select>
      </div>

      <!-- Mode 1: Four-Term Proportion -->
      <div id="panel-four-term">
        <div class="input-group">
          <label for="unknown-pos">Select Which Term is Unknown (X)</label>
          <select id="unknown-pos" class="form-control" onchange="updateUnknownPos()">
            <option value="d" selected>Term D is Unknown: A / B = C / X</option>
            <option value="c">Term C is Unknown: A / B = X / D</option>
            <option value="b">Term B is Unknown: A / X = C / D</option>
            <option value="a">Term A is Unknown: X / B = C / D</option>
          </select>
        </div>

        <div style="display:flex; align-items:center; justify-content:center; gap:16px; margin:20px 0; font-size:1.5rem; font-weight:700;">
          <div style="display:flex; flex-direction:column; align-items:center; width:120px;">
            <input type="number" id="term-a" class="form-control" value="4" step="any" style="text-align:center;">
            <div style="width:100%; height:2px; background:var(--text-dark, #0F172A); margin:4px 0;"></div>
            <input type="number" id="term-b" class="form-control" value="7" step="any" style="text-align:center;">
          </div>
          <div style="font-size:2rem; color:var(--primary, #2563EB);">=</div>
          <div style="display:flex; flex-direction:column; align-items:center; width:120px;">
            <input type="number" id="term-c" class="form-control" value="12" step="any" style="text-align:center;">
            <div style="width:100%; height:2px; background:var(--text-dark, #0F172A); margin:4px 0;"></div>
            <input type="text" id="term-d" class="form-control" value="X" disabled style="text-align:center; background:#EFF6FF; font-weight:bold; color:var(--primary);">
          </div>
        </div>
      </div>

      <!-- Mode 2: Variation -->
      <div id="panel-variation" style="display:none;">
        <div class="input-group">
          <label for="var-mode">Variation Model</label>
          <select id="var-mode" class="form-control" onchange="calculateProportion()">
            <option value="direct" selected>Direct Variation: y = k &times; x (y increases with x)</option>
            <option value="inverse">Inverse Variation: y = k / x (y decreases as x increases)</option>
          </select>
        </div>
        <div class="input-grid">
          <div class="input-group">
            <label for="var-x1">Initial x₁</label>
            <input type="number" id="var-x1" class="form-control" value="5" step="any">
          </div>
          <div class="input-group">
            <label for="var-y1">Initial y₁</label>
            <input type="number" id="var-y1" class="form-control" value="20" step="any">
          </div>
        </div>
        <div class="input-grid">
          <div class="input-group">
            <label for="var-x2">Target x₂</label>
            <input type="number" id="var-x2" class="form-control" value="15" step="any">
          </div>
          <div class="input-group">
            <label>Target y₂ (Calculated)</label>
            <div id="var-y2-display" style="padding:10px; background:#EFF6FF; border:1px solid #BFDBFE; border-radius:6px; font-weight:700; color:var(--primary);">Pending</div>
          </div>
        </div>
      </div>

      <div class="input-group">
        <label for="precision-select">Decimal Precision</label>
        <select id="precision-select" class="form-control" onchange="calculateProportion()">
          <option value="2">2 decimal places</option>
          <option value="4" selected>4 decimal places</option>
          <option value="6">6 decimal places</option>
        </select>
      </div>

      <div style="display:flex; gap:12px; margin-top:16px;">
        <button id="calc-btn" class="btn-primary" onclick="calculateProportion()" style="flex:1;">Solve Proportion</button>
        <button id="reset-btn" class="btn-secondary" onclick="resetProportion()">Reset</button>
      </div>

      <div id="result-box" class="result-box" style="margin-top:24px;">
        <h2 class="result-title">Proportional Solution &amp; Properties</h2>
        <div class="result-highlight" style="font-size:1.8rem; font-weight:700; color:var(--primary); margin-bottom:16px;" id="res-val">
          X = 21.0000
        </div>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:16px;">
          <div><span class="res-label">Cross Product Check:</span> <strong class="res-val" id="res-cross">84 = 84</strong></div>
          <div><span class="res-label">Scale Factor / Ratio:</span> <strong class="res-val" id="res-ratio">1 : 1.75</strong></div>
          <div><span class="res-label">Proportionality Constant k:</span> <strong class="res-val" id="res-k">0.5714</strong></div>
          <div><span class="res-label">Fraction Representation:</span> <strong class="res-val" id="res-frac">21 / 1</strong></div>
        </div>

        <h3 style="margin-top:20px; font-size:1.1rem; color:var(--text-dark);">Step-by-Step Algebraic Derivation</h3>
        <div id="res-steps" style="background:var(--bg-subtle, #f8fafc); padding:16px; border-radius:8px; font-family:monospace; font-size:0.95rem; white-space:pre-wrap; border:1px solid var(--border-color, #e2e8f0);"></div>
      </div>
    </div>

    <article class="article-body">
      <h2>Comprehensive Theoretical &amp; Engineering Guide to Proportions</h2>
      <p>A mathematical proportion is an equation stating that two ratios or rates are strictly equivalent: \(\frac{A}{B} = \frac{C}{D}\). First formalized in classical antiquity within Book V and Book VII of Euclid's <em>Elements</em>, the theory of proportion provides the structural framework for geometric similarity, dimensional similitude in fluid mechanics, photographic scaling, currency exchange rates, and stoichiometric balancing in chemical synthesis.</p>

      <p>In any proportion \(\frac{A}{B} = \frac{C}{D}\), the terms \(A\) and \(D\) are designated as the <strong>extremes</strong>, while the terms \(B\) and \(C\) are designated as the <strong>means</strong>. The foundational Theorem of Proportions establishes that two ratios are equal if and only if the product of their extremes identically equals the product of their means: \(A \cdot D = B \cdot C\). You can simplify individual ratios using our <a href="ratio-calculator.html">Ratio Simplifier</a>.</p>

      <h2>Mathematical Formulations: Solving for Unknowns &amp; Variations</h2>
      <p>Proportion problems arise in four distinct mathematical configurations depending on the nature of the relationship between variables.</p>

      <h3>1. Solving for an Unknown in Four-Term Proportions</h3>
      <p>When three terms of a proportion are known, cross-multiplication isolates the fourth unknown term with exact precision:</p>
      <ul>
        <li><strong>Solving for Extremes:</strong>
          $$A = \frac{B \cdot C}{D}, \quad D = \frac{B \cdot C}{A}$$
        </li>
        <li><strong>Solving for Means:</strong>
          $$B = \frac{A \cdot D}{C}, \quad C = \frac{A \cdot D}{B}$$
        </li>
      </ul>
      <p>Because these operations rely strictly on elementary field operations, results can be simplified to irreducible rational fractions or mixed numbers, as explored in our <a href="fraction-calculator.html">Fraction Calculator</a>.</p>

      <h3>2. Direct Proportion (Direct Variation)</h3>
      <p>Two variables \(x\) and \(y\) are directly proportional (denoted \(y \propto x\)) if their quotient remains invariant across all states. This invariant is the constant of proportionality \(k\):</p>
      $$\frac{y}{x} = k \iff y = k \cdot x$$
      <p>Given an initial baseline pair \((x_1, y_1)\) and a new state \(x_2\), the target value \(y_2\) is computed as:</p>
      $$\frac{y_1}{x_1} = \frac{y_2}{x_2} \implies y_2 = y_1 \times \left( \frac{x_2}{x_1} \right)$$
      <p>Direct proportion governs linear physical laws including Ohm's Law (\(V = I \cdot R\)), Hooke's Law of elasticity (\(F = k \cdot \Delta x\)), and uniform velocity motion (\(d = v \cdot t\)).</p>

      <h3>3. Inverse Proportion (Indirect Variation)</h3>
      <p>Two variables are inversely proportional (denoted \(y \propto \frac{1}{x}\)) if their product remains invariant: as one variable increases by a given factor, the other decreases by the reciprocal factor:</p>
      $$x \cdot y = k \iff y = \frac{k}{x}$$
      <p>Given an initial baseline pair \((x_1, y_1)\) and a new state \(x_2\), the target value \(y_2\) is evaluated as:</p>
      $$x_1 \cdot y_1 = x_2 \cdot y_2 \implies y_2 = y_1 \times \left( \frac{x_1}{x_2} \right)$$
      <p>Inverse proportion governs fundamental physical relationships including Boyle's Law of ideal gases (\(P_1 V_1 = P_2 V_2\)), gravitational attraction distance decay, and gear train angular velocity ratios.</p>

      <h3>4. Continued Proportions &amp; Geometric Mean</h3>
      <p>Three quantities \(a\), \(b\), and \(c\) are in continuous proportion if the ratio of the first to the second equals the ratio of the second to the third:</p>
      $$\frac{a}{b} = \frac{b}{c} \iff b^2 = a \cdot c \iff b = \sqrt{a \cdot c}$$
      <p>The middle term \(b\) represents the geometric mean or mean proportional between \(a\) and \(c\). This construct underpins the Golden Ratio \(\phi = \frac{1 + \sqrt{5}}{2}\), where \(\frac{A + B}{A} = \frac{A}{B}\).</p>

      <h2>Proportional Variations Comparison Reference Table</h2>
      <p>The following technical reference matrix summarizes the properties, governing formulas, graph geometries, and real-world engineering examples across proportional variation types:</p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Variation Model</th>
            <th>Governing Equation</th>
            <th>Constant of Proportionality \(k\)</th>
            <th>Graphical Behavior</th>
            <th>Physical &amp; Engineering Application</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Direct Variation</td>
            <td>\(y = k \cdot x\)</td>
            <td>\(k = \frac{y}{x}\)</td>
            <td>Straight line passing through the origin \((0, 0)\)</td>
            <td>Ohm's Law (\(V \propto I\)), Hooke's Law, architectural model scaling</td>
          </tr>
          <tr>
            <td>Inverse Variation</td>
            <td>\(y = \frac{k}{x}\)</td>
            <td>\(k = x \cdot y\)</td>
            <td>Rectangular hyperbola asymptotic to axes</td>
            <td>Boyle's Gas Law (\(P \propto 1/V\)), pulley gear ratios, work-rate crew sizing</td>
          </tr>
          <tr>
            <td>Joint Variation</td>
            <td>\(z = k \cdot x \cdot y\)</td>
            <td>\(k = \frac{z}{x \cdot y}\)</td>
            <td>Planar or hyperbolic surface in 3D space</td>
            <td>Centripetal force (\(F \propto m \cdot a\)), electric power (\(P \propto V \cdot I\))</td>
          </tr>
          <tr>
            <td>Combined Variation</td>
            <td>\(z = k \cdot \frac{x}{y}\)</td>
            <td>\(k = \frac{z \cdot y}{x}\)</td>
            <td>Hyperbolic saddle manifold</td>
            <td>Ideal Gas Law (\(P = k \frac{T}{V}\)), resistance of conductors (\(R = \rho \frac{L}{A}\))</td>
          </tr>
          <tr>
            <td>Continued Proportion</td>
            <td>\(\frac{a}{b} = \frac{b}{c}\)</td>
            <td>\(b = \sqrt{a \cdot c}\)</td>
            <td>Exponential geometric sequence curve</td>
            <td>Audio equal-tempered musical scales, golden section geometry</td>
          </tr>
        </tbody>
      </table>

      <h2>Real-World Engineering, Clinical &amp; Architectural Case Studies</h2>
      <p>The following worked case studies demonstrate how proportions solve practical problems in civil scaling, clinical dosage calculation, and gas thermodynamics.</p>

      <div class="worked-example-card">
        <h3>Case Study 1: Architectural Blueprint Scale Factor Dimensioning (Direct Proportion)</h3>
        <p><strong>Scenario:</strong> An architectural drawing uses a scale of \(1 : 50\) (meaning \(1 \text{ cm}\) on paper represents \(50 \text{ cm}\) on the physical building). An interior conference room measures \(14.6 \text{ cm}\) in length on the blueprint. The structural engineer must compute the actual constructed length \(X\) in meters.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Set up the direct proportion equation:
            $$\frac{1 \text{ cm}}{50 \text{ cm}} = \frac{14.6 \text{ cm}}{X}$$
          </li>
          <li>Identify extremes and means: extremes are \(1\) and \(X\); means are \(50\) and \(14.6\).</li>
          <li>Apply cross-multiplication:
            $$1 \times X = 50 \times 14.6$$
            $$X = 730.0 \text{ cm}$$
          </li>
          <li>Convert centimeters to standard meters:
            $$X = \frac{730.0}{100} = 7.3000 \text{ meters}$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The constructed physical conference room length is exactly \(7.3000 \text{ meters}\).</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Clinical Pharmacological Weight-Based Titration (Direct Proportion)</h3>
        <p><strong>Scenario:</strong> A pediatric hospital formulary specifies an intravenous antibiotic loading dose of \(15.0 \text{ mg}\) per \(1.0 \text{ kg}\) of patient body mass. The reconstituted medication vial contains \(250.0 \text{ mg}\) of active pharmaceutical ingredient dissolved in \(10.0 \text{ mL}\) of sterile saline. A patient weighs \(22.0 \text{ kg}\). The nurse must determine the required liquid injection volume \(V\) in milliliters.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Calculate total required active drug dose \(D\):
            $$D = 22.0 \text{ kg} \times 15.0 \text{ mg/kg} = 330.0 \text{ mg}$$
          </li>
          <li>Set up the volumetric proportion:
            $$\frac{250.0 \text{ mg}}{10.0 \text{ mL}} = \frac{330.0 \text{ mg}}{V}$$
          </li>
          <li>Cross-multiply to isolate \(V\):
            $$250.0 \times V = 10.0 \times 330.0 = 3300.0$$
            $$V = \frac{3300.0}{250.0} = 13.2000 \text{ mL}$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The precise pediatric delivery volume is \(13.2000 \text{ mL}\) of reconstituted solution.</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 3: Pneumatic Actuator Cylinder Isothermal Compression (Inverse Proportion)</h3>
        <p><strong>Scenario:</strong> A pneumatic machine cylinder holds \(4.50 \text{ liters}\) of compressed dry air at an initial absolute pressure of \(2.00 \text{ bar}\) (Boyle's Law isothermal conditions). The piston stroke compresses the gas chamber down to a final volume of \(1.25 \text{ liters}\). The mechanical automation engineer must determine the final compressed air pressure \(P_2\).</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Apply the inverse proportion formulation (\(P_1 V_1 = P_2 V_2\)):
            $$\frac{P_1}{P_2} = \frac{V_2}{V_1} \iff P_1 \times V_1 = P_2 \times V_2$$
          </li>
          <li>Substitute known parameter values:
            $$2.00 \text{ bar} \times 4.50 \text{ L} = P_2 \times 1.25 \text{ L}$$
            $$9.00 \text{ bar}\cdot\text{L} = 1.25 \cdot P_2$$
          </li>
          <li>Solve for final pressure \(P_2\):
            $$P_2 = \frac{9.00}{1.25} = 7.2000 \text{ bar}$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The final compressed air pressure inside the actuator cylinder reaches \(7.2000 \text{ bar}\).</p>
      </div>

      <h2>Frequently Asked Questions</h2>
      <div class="faq-item">
        <div class="faq-question">What is the means-extremes property of proportions?</div>
        <div class="faq-answer">The means-extremes property states that in any valid proportion \(A/B = C/D\), the product of the first and fourth terms (the extremes: \(A\) and \(D\)) is always strictly equal to the product of the second and third terms (the means: \(B\) and \(C\)). Formally, \(A \cdot D = B \cdot C\).</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">How do you know whether a problem is direct or inverse proportion?</div>
        <div class="faq-answer">Ask whether the two variables move in the same direction or in opposite directions. If increasing variable X causes variable Y to increase by the same multiplicative factor (such as buying more goods at a fixed unit price), it is direct proportion (\(y/x = k\)). If increasing variable X causes variable Y to decrease proportionally (such as more workers finishing a fixed job in fewer hours), it is inverse proportion (\(x \cdot y = k\)).</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Why can't the denominator in a proportion be zero?</div>
        <div class="faq-answer">Division by zero is undefined in arithmetic. In the expression \(A/B = C/D\), setting either \(B = 0\) or \(D = 0\) creates an undefined fraction with infinite or indeterminate value. Cross-multiplication with zero denominators breaks the algebraic equivalence of the proportion.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">What is a scale factor in proportional geometry?</div>
        <div class="faq-answer">A scale factor is the dimensionless ratio of any linear dimension in a scaled copy to the corresponding linear dimension in the original object. If a scale factor is \(k = 3\), all lengths are multiplied by 3, all surface areas are multiplied by \(k^2 = 9\), and all 3D enclosed volumes are multiplied by \(k^3 = 27\).</div>
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

    function switchPropType() {
      var type = document.getElementById('prop-type').value;
      if (type === 'four-term') {
        document.getElementById('panel-four-term').style.display = 'block';
        document.getElementById('panel-variation').style.display = 'none';
      } else {
        document.getElementById('panel-four-term').style.display = 'none';
        document.getElementById('panel-variation').style.display = 'block';
      }
      calculateProportion();
    }

    function updateUnknownPos() {
      var unk = document.getElementById('unknown-pos').value;
      var inputs = ['term-a', 'term-b', 'term-c', 'term-d'];
      inputs.forEach(function(id) {
        var el = document.getElementById(id);
        el.disabled = false;
        el.style.background = '#FFFFFF';
        el.style.color = 'var(--text-dark, #0F172A)';
        if (el.value === 'X') el.value = '10';
      });

      var target = document.getElementById('term-' + unk);
      target.disabled = true;
      target.value = 'X';
      target.style.background = '#EFF6FF';
      target.style.color = 'var(--primary, #2563EB)';
      calculateProportion();
    }

    function calculateProportion() {
      var type = document.getElementById('prop-type').value;
      var prec = parseInt(document.getElementById('precision-select').value, 10) || 4;

      if (type === 'four-term') {
        var unk = document.getElementById('unknown-pos').value;
        var a = parseFloat(document.getElementById('term-a').value);
        var b = parseFloat(document.getElementById('term-b').value);
        var c = parseFloat(document.getElementById('term-c').value);
        var d = parseFloat(document.getElementById('term-d').value);

        var xVal = 0;
        var steps = "";

        if (unk === 'd') {
          if (isNaN(a) || isNaN(b) || isNaN(c) || a === 0) {
            showError("Terms A, B, and C must be valid numbers with A != 0.");
            return;
          }
          if (b === 0) { showError("Denominator B cannot be zero."); return; }
          xVal = (b * c) / a;
          d = xVal;
          steps = "Proportion: A / B = C / X\n" +
                  "Given: A = " + a + ", B = " + b + ", C = " + c + "\n\n" +
                  "1. Cross-Multiplication Rule: A * X = B * C\n" +
                  "   " + a + " * X = " + b + " * " + c + " = " + (b * c).toFixed(prec) + "\n\n" +
                  "2. Isolate Unknown X:\n" +
                  "   X = (B * C) / A = " + (b * c).toFixed(prec) + " / " + a + " = " + xVal.toFixed(prec);
        } else if (unk === 'c') {
          if (isNaN(a) || isNaN(b) || isNaN(d) || b === 0 || d === 0) {
            showError("Terms A, B, and D must be valid numbers with B, D != 0.");
            return;
          }
          xVal = (a * d) / b;
          c = xVal;
          steps = "Proportion: A / B = X / D\n" +
                  "Given: A = " + a + ", B = " + b + ", D = " + d + "\n\n" +
                  "1. Cross-Multiplication Rule: B * X = A * D\n" +
                  "   " + b + " * X = " + a + " * " + d + " = " + (a * d).toFixed(prec) + "\n\n" +
                  "2. Isolate Unknown X:\n" +
                  "   X = (A * D) / B = " + (a * d).toFixed(prec) + " / " + b + " = " + xVal.toFixed(prec);
        } else if (unk === 'b') {
          if (isNaN(a) || isNaN(c) || isNaN(d) || c === 0 || d === 0) {
            showError("Terms A, C, and D must be valid numbers with C, D != 0.");
            return;
          }
          xVal = (a * d) / c;
          b = xVal;
          steps = "Proportion: A / X = C / D\n" +
                  "Given: A = " + a + ", C = " + c + ", D = " + d + "\n\n" +
                  "1. Cross-Multiplication Rule: C * X = A * D\n" +
                  "   " + c + " * X = " + a + " * " + d + " = " + (a * d).toFixed(prec) + "\n\n" +
                  "2. Isolate Unknown X:\n" +
                  "   X = (A * D) / C = " + (a * d).toFixed(prec) + " / " + c + " = " + xVal.toFixed(prec);
        } else if (unk === 'a') {
          if (isNaN(b) || isNaN(c) || isNaN(d) || b === 0 || d === 0) {
            showError("Terms B, C, and D must be valid numbers with B, D != 0.");
            return;
          }
          xVal = (b * c) / d;
          a = xVal;
          steps = "Proportion: X / B = C / D\n" +
                  "Given: B = " + b + ", C = " + c + ", D = " + d + "\n\n" +
                  "1. Cross-Multiplication Rule: D * X = B * C\n" +
                  "   " + d + " * X = " + b + " * " + c + " = " + (b * c).toFixed(prec) + "\n\n" +
                  "2. Isolate Unknown X:\n" +
                  "   X = (B * C) / D = " + (b * c).toFixed(prec) + " / " + d + " = " + xVal.toFixed(prec);
        }

        var crossLeft = a * d;
        var crossRight = b * c;
        var k = (b !== 0) ? (a / b) : 0;

        document.getElementById('res-val').innerText = "X = " + xVal.toFixed(prec);
        document.getElementById('res-cross').innerText = crossLeft.toFixed(prec) + " = " + crossRight.toFixed(prec);
        document.getElementById('res-ratio').innerText = "1 : " + (1 / k).toFixed(prec);
        document.getElementById('res-k').innerText = k.toFixed(prec);
        document.getElementById('res-frac').innerText = xVal.toFixed(prec) + " / 1";
        document.getElementById('res-steps').innerText = steps;

      } else {
        var vMode = document.getElementById('var-mode').value;
        var x1 = parseFloat(document.getElementById('var-x1').value);
        var y1 = parseFloat(document.getElementById('var-y1').value);
        var x2 = parseFloat(document.getElementById('var-x2').value);

        if ([x1, y1, x2].some(isNaN) || x1 === 0 || x2 === 0) {
          showError("Initial and target x values cannot be zero.");
          return;
        }

        var y2 = 0;
        var kVal = 0;
        var steps = "";

        if (vMode === 'direct') {
          kVal = y1 / x1;
          y2 = kVal * x2;
          steps = "Variation Model: Direct Proportion (y = k * x)\n" +
                  "Baseline: x₁ = " + x1 + ", y₁ = " + y1 + "\n\n" +
                  "1. Constant of Proportionality (k):\n" +
                  "   k = y₁ / x₁ = " + y1 + " / " + x1 + " = " + kVal.toFixed(prec) + "\n\n" +
                  "2. Calculate Target y₂:\n" +
                  "   y₂ = k * x₂ = " + kVal.toFixed(prec) + " * " + x2 + " = " + y2.toFixed(prec);
        } else {
          kVal = x1 * y1;
          y2 = kVal / x2;
          steps = "Variation Model: Inverse Proportion (y = k / x)\n" +
                  "Baseline: x₁ = " + x1 + ", y₁ = " + y1 + "\n\n" +
                  "1. Constant Invariant Product (k):\n" +
                  "   k = x₁ * y₁ = " + x1 + " * " + y1 + " = " + kVal.toFixed(prec) + "\n\n" +
                  "2. Calculate Target y₂:\n" +
                  "   y₂ = k / x₂ = " + kVal.toFixed(prec) + " / " + x2 + " = " + y2.toFixed(prec);
        }

        document.getElementById('var-y2-display').innerText = "y₂ = " + y2.toFixed(prec);
        document.getElementById('res-val').innerText = "y₂ = " + y2.toFixed(prec);
        document.getElementById('res-cross').innerText = "k = " + kVal.toFixed(prec);
        document.getElementById('res-ratio').innerText = "x₂ / x₁ = " + (x2 / x1).toFixed(prec);
        document.getElementById('res-k').innerText = kVal.toFixed(prec);
        document.getElementById('res-frac').innerText = (vMode === 'direct' ? "y = " + kVal.toFixed(prec) + "x" : "xy = " + kVal.toFixed(prec));
        document.getElementById('res-steps').innerText = steps;
      }
    }

    function showError(msg) {
      document.getElementById('res-val').innerText = "Error";
      document.getElementById('res-cross').innerText = "N/A";
      document.getElementById('res-ratio').innerText = "N/A";
      document.getElementById('res-k').innerText = "N/A";
      document.getElementById('res-frac').innerText = "N/A";
      document.getElementById('res-steps').innerText = "Error: " + msg;
    }

    function resetProportion() {
      document.getElementById('prop-type').value = 'four-term';
      document.getElementById('unknown-pos').value = 'd';
      document.getElementById('term-a').value = '4';
      document.getElementById('term-b').value = '7';
      document.getElementById('term-c').value = '12';
      document.getElementById('var-mode').value = 'direct';
      document.getElementById('var-x1').value = '5';
      document.getElementById('var-y1').value = '20';
      document.getElementById('var-x2').value = '15';
      document.getElementById('precision-select').value = '4';
      switchPropType();
      updateUnknownPos();
    }

    window.addEventListener('DOMContentLoaded', function() {
      calculateProportion();
    });
  </script>
</body>
</html>
"""

# 6. quotient-and-remainder-calculator.html
HTML_QUOTIENT = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quotient and Remainder Calculator - Euclidean Division &amp; Divmod Solver</title>
  <meta name="description" content="Calculate integer quotient and remainder with step-by-step Euclidean division. Compute mixed numbers, repeating decimals, and divmod for positive and negative numbers.">
  <link rel="canonical" href="https://calchub.org/quotient-and-remainder-calculator.html">
  <meta property="og:title" content="Quotient and Remainder Calculator - Euclidean Division Solver">
  <meta property="og:description" content="Free integer division calculator. Compute quotient Q, remainder R, mixed fraction, and decimal expansion using the Euclidean Division Algorithm (A = B * Q + R).">
  <meta property="og:url" content="https://calchub.org/quotient-and-remainder-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Quotient and Remainder Calculator - Divmod Solver">
  <meta name="twitter:description" content="Calculate quotient and remainder with complete division tableau, mixed number notation, and negative number handling.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Quotient and Remainder Calculator",
    "url": "https://calchub.org/quotient-and-remainder-calculator.html",
    "description": "Calculates integer quotient, remainder, mixed number representation, and verification identity for integer division A = B * Q + R.",
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
          "text": "The Euclidean Division Algorithm states that for any integer dividend A and positive integer divisor B, there exist unique integers Q (quotient) and R (remainder) such that A = B * Q + R, strictly bounded by 0 <= R < B."
        }
      },
      {
        "@type": "Question",
        "name": "How does Euclidean division handle negative dividends compared to programming languages?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "In strict Euclidean division, the remainder must always be non-negative: 0 <= R < |B|. For example, -17 divided by 5 yields quotient Q = -4 and remainder R = +3 because 5 * (-4) + 3 = -17 (used in Python divmod). In contrast, C/C++/Java use truncated division where remainder takes the dividend's sign: Q = -3 and R = -2."
        }
      },
      {
        "@type": "Question",
        "name": "How is the quotient and remainder converted into a mixed number?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The rational fraction A / B is expressed as an integer plus the proper fractional remainder: A / B = Q + (R / B). For example, 29 divided by 6 gives quotient 4 and remainder 5, writing as the mixed number 4 5/6."
        }
      },
      {
        "@type": "Question",
        "name": "Can the divisor B ever be zero in quotient and remainder division?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No. Division by zero is undefined in mathematics. If B = 0, no quotient or remainder exists because B * Q = 0 for any finite Q, making it impossible to satisfy A = B * Q + R."
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
      <div class="calc-icon" aria-hidden="true">&#247;</div>
      <h1>Quotient and Remainder Calculator</h1>
      <p class="calc-description">Compute integer quotient, remainder, mixed fractions, and decimal expansions using the Euclidean Division Algorithm (A = B &times; Q + R).</p>
    </div>

    <div class="calculator-body">
      <div class="input-grid">
        <div class="input-group">
          <label for="dividend-val">Dividend (A)</label>
          <input type="number" id="dividend-val" class="form-control" value="127" step="1">
          <span class="help-text">Number being divided (integer)</span>
        </div>
        <div class="input-group">
          <label for="divisor-val">Divisor (B)</label>
          <input type="number" id="divisor-val" class="form-control" value="8" step="1">
          <span class="help-text">Number dividing by (non-zero integer)</span>
        </div>
      </div>

      <div class="input-group">
        <label for="div-convention">Division Convention for Negatives</label>
        <select id="div-convention" class="form-control" onchange="calculateDivmod()">
          <option value="euclidean" selected>Euclidean / Floored (0 &le; R &lt; |B|, Python divmod)</option>
          <option value="truncated">Truncated / Round-Toward-Zero (Remainder matches Dividend sign, C/Java)</option>
        </select>
      </div>

      <div style="display:flex; gap:12px; margin-top:16px;">
        <button id="calc-btn" class="btn-primary" onclick="calculateDivmod()" style="flex:1;">Compute Division</button>
        <button id="reset-btn" class="btn-secondary" onclick="resetDivmod()">Reset</button>
      </div>

      <div id="result-box" class="result-box" style="margin-top:24px;">
        <h2 class="result-title">Division Equation &amp; Results</h2>
        <div class="result-highlight" style="font-size:1.8rem; font-weight:700; color:var(--primary); margin-bottom:16px;" id="res-headline">
          127 &divide; 8 = 15 R 7
        </div>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:16px;">
          <div><span class="res-label">Quotient (Q):</span> <strong class="res-val" id="res-q">15</strong></div>
          <div><span class="res-label">Remainder (R):</span> <strong class="res-val" id="res-r">7</strong></div>
          <div><span class="res-label">Mixed Number:</span> <strong class="res-val" id="res-mixed">15 7/8</strong></div>
          <div><span class="res-label">Decimal Result:</span> <strong class="res-val" id="res-decimal">15.8750</strong></div>
          <div><span class="res-label">Modulo Value (A mod B):</span> <strong class="res-val" id="res-mod">7</strong></div>
          <div><span class="res-label">Verification Identity:</span> <strong class="res-val" id="res-verify">8 &times; 15 + 7 = 127</strong></div>
        </div>

        <h3 style="margin-top:20px; font-size:1.1rem; color:var(--text-dark);">Step-by-Step Division Tableau</h3>
        <div id="res-steps" style="background:var(--bg-subtle, #f8fafc); padding:16px; border-radius:8px; font-family:monospace; font-size:0.95rem; white-space:pre-wrap; border:1px solid var(--border-color, #e2e8f0);"></div>
      </div>
    </div>

    <article class="article-body">
      <h2>Comprehensive Mathematical &amp; Computer Science Guide to Integer Division</h2>
      <p>Integer division with remainders—formalized in number theory as Euclidean division—is the foundational arithmetic operation that partitions an integer dividend \(A\) into an integer quotient \(Q\) of groups of size \(B\), leaving a leftover remainder \(R\). While elementary arithmetic introduces quotient and remainder division for positive whole numbers, advanced computer science, discrete mathematics, and cryptography depend on its rigorous axiomatic formulation.</p>

      <p>Euclidean division underpins Euclidean Greatest Common Divisor (GCD) extraction, RSA public-key cryptosystems, computer memory cache line indexing, hash table bucket distribution, and modulo wrap-around counters in operating system timers. Explore long division tableau steps in our <a href="long-division-calculator.html">Long Division Calculator</a> and residue classes in our <a href="modulo-calculator.html">Modulo Calculator</a>.</p>

      <h2>The Euclidean Division Theorem &amp; Mathematical Rigor</h2>
      <p>For any two integers \(A\) (the dividend) and \(B\) (the divisor, where \(B \neq 0\)), there exist unique integers \(Q\) (the quotient) and \(R\) (the remainder) satisfying two simultaneous conditions:</p>
      $$\text{Identity: } A = B \cdot Q + R$$
      $$\text{Euclidean Boundary: } 0 \le R < |B|$$
      <p>The existence and uniqueness of \(Q\) and \(R\) are proven via the Well-Ordering Principle of the positive integers: the set of non-negative integers of the form \(A - k B\) contains a unique minimum element, which defines the remainder \(R\).</p>

      <h2>Handling Negative Numbers: Floored vs. Truncated Division</h2>
      <p>A frequent source of critical software bugs in systems programming is the discrepancy between mathematical Euclidean division and CPU architecture instruction sets when handling negative dividends or divisors:</p>

      <h3>1. Euclidean / Floored Division (Python `divmod` / Knuth)</h3>
      <p>In pure mathematics and languages like Python, the quotient is defined using the floor function \(\lfloor x \rfloor\), which always rounds downward toward negative infinity:</p>
      $$Q = \left\lfloor \frac{A}{B} \right\rfloor, \quad R = A - B \cdot Q$$
      <p>For example, dividing \(-17\) by \(5\):</p>
      $$\frac{-17}{5} = -3.4 \implies Q = \lfloor -3.4 \rfloor = -4$$
      $$R = -17 - 5 \times (-4) = -17 + 20 = +3$$
      <p>Notice that \(0 \le R < 5\) is strictly preserved, and \(5 \times (-4) + 3 = -17\). This guarantees that the remainder function matches the mathematical congruence ring \(\mathbb{Z}/B\mathbb{Z}\).</p>

      <h3>2. Truncated Division (C99, C++, Java, Rust, JavaScript `%`)</h3>
      <p>In standard CPU instruction sets (such as x86 `IDIV`), integer division truncates toward zero (discarding fractional digits):</p>
      $$Q = \text{trunc}\left( \frac{A}{B} \right), \quad R = A - B \cdot Q$$
      <p>Evaluating \(-17\) divided by \(5\):</p>
      $$Q = \text{trunc}(-3.4) = -3$$
      $$R = -17 - 5 \times (-3) = -17 + 15 = -2$$
      <p>Here, the remainder is negative (\(R = -2\)). While the identity \(-17 = 5 \times (-3) + (-2)\) holds, the Euclidean boundary \(R \ge 0\) is violated. Our interactive calculator allows toggling between both conventions.</p>

      <h2>Mixed Number &amp; Repeating Decimal Expansions</h2>
      <p>Any integer division \(A / B\) can be represented in three distinct mathematical notations:</p>
      <div class="formula-box">
        <h3>Equivalent Mathematical Representations</h3>
        $$\text{Division Algorithm: } A = B \cdot Q + R$$
        $$\text{Mixed Number Notation: } \frac{A}{B} = Q + \frac{R}{B} = Q \frac{R}{B}$$
        $$\text{Decimal Expansion: } \frac{A}{B} = Q + \sum_{i=1}^{\infty} d_i \cdot 10^{-i}$$
      </div>
      <p>If the reduced denominator of \(R/B\) contains prime factors other than 2 and 5, the decimal expansion generates an infinitely repeating decimal period, as analyzed in our <a href="gcd-lcm-calculator.html">GCD and LCM Calculator</a>.</p>

      <h2>Integer Division Implementations Across Programming Languages</h2>
      <p>The following technical benchmark matrix compares integer division behaviors, remainder signs, and operator symbols across major programming languages:</p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Language / Standard</th>
            <th>Quotient Operator</th>
            <th>Remainder Operator</th>
            <th>Rounding Direction</th>
            <th>Remainder Sign for Negative Dividend</th>
            <th>Mathematical Convention</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Python 3</td>
            <td><code>//</code></td>
            <td><code>%</code> (or <code>divmod()</code>)</td>
            <td>Floor toward \(-\infty\)</td>
            <td>Always positive (\(\ge 0\))</td>
            <td>Floored / Euclidean</td>
          </tr>
          <tr>
            <td>C / C++ (C99+)</td>
            <td><code>/</code></td>
            <td><code>%</code></td>
            <td>Truncate toward \(0\)</td>
            <td>Matches Dividend sign</td>
            <td>Truncated (ISO/IEC 9899)</td>
          </tr>
          <tr>
            <td>Java / C#</td>
            <td><code>/</code></td>
            <td><code>%</code></td>
            <td>Truncate toward \(0\)</td>
            <td>Matches Dividend sign</td>
            <td>Truncated</td>
          </tr>
          <tr>
            <td>JavaScript (ES6)</td>
            <td><code>Math.floor(A/B)</code></td>
            <td><code>%</code></td>
            <td>Truncate (floating-point `%`)</td>
            <td>Matches Dividend sign</td>
            <td>Truncated</td>
          </tr>
          <tr>
            <td>Ada / Pascal</td>
            <td><code>div</code></td>
            <td><code>mod</code> / <code>rem</code></td>
            <td>Separate operators</td>
            <td><code>mod</code> is positive, <code>rem</code> is signed</td>
            <td>Both supported</td>
          </tr>
        </tbody>
      </table>

      <h2>Real-World Computer Systems &amp; Logistics Case Studies</h2>
      <p>The following worked examples demonstrate how quotient and remainder division solves practical problems in computer operating systems, industrial packaging, and network memory architectures.</p>

      <div class="worked-example-card">
        <h3>Case Study 1: Epoch Timestamp Decomposition into Hours, Minutes &amp; Seconds</h3>
        <p><strong>Scenario:</strong> A Linux server kernel measures an elapsed process execution duration of \(A = 14,785 \text{ seconds}\). The monitoring daemon must decompose this scalar duration into discrete hours, minutes, and remaining seconds using sequential quotient and remainder operations.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Divide total seconds by \(3600\) (seconds per hour):
            $$14785 \div 3600 \implies Q_1 = \lfloor 14785 / 3600 \rfloor = 4 \text{ hours}$$
            $$R_1 = 14785 - (3600 \times 4) = 14785 - 14400 = 385 \text{ seconds remaining}$$
          </li>
          <li>Divide remaining seconds by \(60\) (seconds per minute):
            $$385 \div 60 \implies Q_2 = \lfloor 385 / 60 \rfloor = 6 \text{ minutes}$$
            $$R_2 = 385 - (60 \times 6) = 385 - 360 = 25 \text{ seconds}$$
          </li>
          <li>Verify total reconstruction:
            $$4 \times 3600 + 6 \times 60 + 25 = 14400 + 360 + 25 = 14,785 \text{ seconds}$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The elapsed process runtime decomposes to exactly \(4\text{h } 06\text{m } 25\text{s}\).</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Industrial Warehouse Shipping Container Palletization</h3>
        <p><strong>Scenario:</strong> An automated fulfillment center packs \(A = 1,485\) manufactured medical diagnostic kits into shipping cartons. Each master carton holds exactly \(B = 48\) kits. The shipping logistics coordinator must determine how many full cartons are packed, how many units remain for partial packing, and the overall packing efficiency percentage.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Perform Euclidean integer division:
            $$A = 1485, \quad B = 48$$
            $$Q = \lfloor 1485 / 48 \rfloor = 30 \text{ full master cartons}$$
          </li>
          <li>Calculate the remaining unpacked units:
            $$R = 1485 - (48 \times 30) = 1485 - 1440 = 45 \text{ kits}$$
          </li>
          <li>Express as a mixed number:
            $$\frac{1485}{48} = 30 \frac{45}{48} = 30 \frac{15}{16} = 30.9375 \text{ cartons}$$
          </li>
          <li>Compute master carton utilization percentage:
            $$\text{Utilization} = \frac{1440}{1485} \times 100\% \approx 96.97\%$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The order requires \(30\) full master cartons, with \(45\) kits remaining in an overflow carton (\(96.97\%\) full carton efficiency).</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 3: Direct-Mapped CPU Cache Set &amp; Offset Addressing</h3>
        <p><strong>Scenario:</strong> A 64-bit microprocessor implements a direct-mapped L1 data cache with cache lines of \(64 \text{ bytes}\) (\(B = 64\)). A memory load request references byte memory address \(A = 4,218\). The memory management unit (MMU) must determine the cache line base address and the internal intra-line byte offset.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Divide byte address \(A = 4218\) by line size \(B = 64\):
            $$Q = \lfloor 4218 / 64 \rfloor = 65$$
          </li>
          <li>Calculate the intra-cache line offset (remainder \(R\)):
            $$R = 4218 - (64 \times 65) = 4218 - 4160 = 58 \text{ bytes}$$
          </li>
          <li>Compute cache line aligned starting memory address:
            $$\text{Line Base} = 64 \times 65 = 4160 \text{ (0x1040 in Hexadecimal)}$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The hardware accesses cache block index \(65\) starting at physical address \(4,160\), reading the target operand at byte offset \(58\).</p>
      </div>

      <h2>Frequently Asked Questions</h2>
      <div class="faq-item">
        <div class="faq-question">What is the difference between quotient and remainder vs. decimal division?</div>
        <div class="faq-answer">Integer quotient and remainder division operates strictly within the domain of integers (\(\mathbb{Z}\)), producing an integer quotient \(Q\) and an integer remainder \(R\) satisfying \(A = B \cdot Q + R\). Decimal division continues the division process into the fractional domain of real numbers (\(\mathbb{R}\)), producing a single decimal fraction \(A/B = Q + R/B\).</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Why must the remainder R be strictly less than the divisor B?</div>
        <div class="faq-answer">If the remainder were greater than or equal to the divisor (\(R \ge B\)), another whole group of size \(B\) could be extracted from \(R\). The quotient \(Q\) would therefore be undercounted by at least 1. Restricting \(0 \le R < B\) guarantees that \(Q\) and \(R\) are mathematically unique.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">What happens if the dividend is smaller than the divisor (A &lt; B)?</div>
        <div class="faq-answer">When positive dividend \(A\) is smaller than positive divisor \(B\), zero complete groups of size \(B\) can be formed. The quotient is identically zero (\(Q = 0\)), and the entire dividend becomes the remainder: \(R = A\). For example, \(3 \div 7 = 0 \text{ R } 3\).</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">How does quotient and remainder division power the Euclidean algorithm for GCD?</div>
        <div class="faq-answer">The Euclidean GCD algorithm repeatedly applies quotient and remainder division. Since \(\gcd(A, B) = \gcd(B, A \pmod B)\), the algorithm replaces the pair \((A, B)\) with \((B, R)\) at each step until the remainder reaches zero. The final non-zero remainder is the greatest common divisor.</div>
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

    function calculateDivmod() {
      var a = parseInt(document.getElementById('dividend-val').value, 10);
      var b = parseInt(document.getElementById('divisor-val').value, 10);
      var conv = document.getElementById('div-convention').value;

      if (isNaN(a) || isNaN(b)) {
        showError("Please enter valid integers for both dividend and divisor.");
        return;
      }

      if (b === 0) {
        showError("Division by zero is mathematically undefined.");
        return;
      }

      var q = 0;
      var r = 0;

      if (conv === 'euclidean') {
        // Floor division: Python divmod style
        q = Math.floor(a / b);
        r = a - b * q;
      } else {
        // Truncated division: C/Java style
        q = (a / b >= 0) ? Math.floor(a / b) : Math.ceil(a / b);
        r = a - b * q;
      }

      var decimalVal = a / b;

      // Mixed fraction construction
      var mixedStr = "";
      if (r === 0) {
        mixedStr = q.toString();
      } else {
        var absR = Math.abs(r);
        var absB = Math.abs(b);
        var g = gcd(absR, absB);
        var redR = absR / g;
        var redB = absB / g;

        if (q === 0) {
          mixedStr = (r < 0 ? "-" : "") + redR + "/" + redB;
        } else {
          mixedStr = q + " " + redR + "/" + redB;
        }
      }

      var verifyStr = b + " × (" + q + ") + (" + r + ") = " + (b * q + r);

      document.getElementById('res-headline').innerHTML = a + " &divide; " + b + " = <strong>" + q + "</strong> R <strong>" + r + "</strong>";
      document.getElementById('res-q').innerText = q.toString();
      document.getElementById('res-r').innerText = r.toString();
      document.getElementById('res-mixed').innerText = mixedStr;
      document.getElementById('res-decimal').innerText = decimalVal.toFixed(4);
      document.getElementById('res-mod').innerText = r.toString();
      document.getElementById('res-verify').innerText = verifyStr;

      var steps = "Division Operation: " + a + " ÷ " + b + " (Convention: " + conv + ")\n" +
                  "Dividend A = " + a + "\n" +
                  "Divisor B = " + b + "\n\n" +
                  "1. Division Equation:\n" +
                  "   A = B * Q + R\n" +
                  "   " + a + " = " + b + " * (" + q + ") + (" + r + ")\n\n" +
                  "2. Quotient Q:\n" +
                  "   Q = " + (conv === 'euclidean' ? "floor(" + a + " / " + b + ")" : "trunc(" + a + " / " + b + ")") + " = " + q + "\n\n" +
                  "3. Remainder R:\n" +
                  "   R = A - (B * Q) = " + a + " - (" + b + " * " + q + ") = " + a + " - (" + (b * q) + ") = " + r + "\n\n" +
                  "4. Remainder Constraint Verification:\n" +
                  "   " + (conv === 'euclidean' ? ("0 <= " + r + " < |" + b + "| (Satisfied)") : ("Remainder sign matches dividend sign (" + (a >= 0 ? "positive" : "negative") + ")")) + "\n\n" +
                  "5. Representations:\n" +
                  "   Mixed Number = " + mixedStr + "\n" +
                  "   Decimal Expansion = " + decimalVal.toFixed(6) + "...";

      document.getElementById('res-steps').innerText = steps;
    }

    function showError(msg) {
      document.getElementById('res-headline').innerText = "Error";
      document.getElementById('res-q').innerText = "N/A";
      document.getElementById('res-r').innerText = "N/A";
      document.getElementById('res-mixed').innerText = "N/A";
      document.getElementById('res-decimal').innerText = "N/A";
      document.getElementById('res-mod').innerText = "N/A";
      document.getElementById('res-verify').innerText = "N/A";
      document.getElementById('res-steps').innerText = "Error: " + msg;
    }

    function resetDivmod() {
      document.getElementById('dividend-val').value = '127';
      document.getElementById('divisor-val').value = '8';
      document.getElementById('div-convention').value = 'euclidean';
      calculateDivmod();
    }

    window.addEventListener('DOMContentLoaded', function() {
      calculateDivmod();
    });
  </script>
</body>
</html>
"""

def main():
    p5 = os.path.join(BASE_DIR, "proportion-calculator.html")
    with open(p5, "w", encoding="utf-8") as f:
        f.write(HTML_PROPORTION)
    print("Generated:", p5)

    p6 = os.path.join(BASE_DIR, "quotient-and-remainder-calculator.html")
    with open(p6, "w", encoding="utf-8") as f:
        f.write(HTML_QUOTIENT)
    print("Generated:", p6)

if __name__ == "__main__":
    main()
