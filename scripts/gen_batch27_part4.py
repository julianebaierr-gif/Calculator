import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 1. SIGNIFICANT FIGURES CALCULATOR
# -------------------------------------------------------------
sigfig_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Significant Figures Calculator — Sig Fig Counter, Rounding & Arithmetic | CalcHub</title>
  <meta name="description" content="Identify significant figures, round to n sig figs, and compute arithmetic operations with measurement uncertainty rules and round-to-even algorithms.">
  <meta name="keywords" content="significant figures calculator, sig fig counter, round to sig figs, sig fig rules, significant digits calculator, significant figures addition, chemistry sig figs">
  <meta name="author" content="CalcHub Metrology & Experimental Measurement Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/significant-figures-calculator.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="Significant Figures Calculator — Sig Fig Counter, Rounding & Arithmetic | CalcHub">
  <meta property="og:description" content="Count significant digits, round to target precision, and solve multi-term arithmetic following strict metrological rules.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/significant-figures-calculator.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/significant-figures-calculator.html#app",
      "name": "Significant Figures & Metrology Engine",
      "url": "https://calchub.org/significant-figures-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "High-precision metrology calculator for identifying significant digits, applying round-to-even rounding, and resolving multi-step scientific arithmetic."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Math & Engineering Calculators", "item": "https://calchub.org/math.html"},
        {"@type": "ListItem", "position": 3, "name": "Significant Figures Calculator", "item": "https://calchub.org/significant-figures-calculator.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What are the universal rules for identifying significant figures in a number?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The fundamental rules are: (1) All non-zero digits (1-9) are always significant. (2) Captive or trapped zeros between non-zero digits are always significant (e.g., 405 has 3 sig figs). (3) Leading zeros preceding all non-zero digits are never significant; they serve purely as scale placeholders (e.g., 0.0045 has 2 sig figs). (4) Trailing zeros after a decimal point are always significant (e.g., 4.500 has 4 sig figs). (5) Trailing zeros in a whole number without a decimal point are ambiguous (e.g., 5000) and must be clarified using scientific notation or an explicit decimal point."
          }
        },
        {
          "@type": "Question",
          "name": "How do significant figure rules differ between multiplication/division and addition/subtraction?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "For multiplication and division, the final result must retain the same number of significant figures as the least precise input value having the lowest count of sig figs. In contrast, for addition and subtraction, the final result is governed by decimal precision (decimal places) rather than total sig figs: the result can have no more digits after the decimal point than the measurement with the fewest decimal places."
          }
        },
        {
          "@type": "Question",
          "name": "What is the 'Round-Half-to-Even' (Banker's Rounding) rule and why is it preferred in metrology?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Classical rounding always rounds 0.5 upward, which introduces a systemic positive statistical drift in large experimental datasets. Round-half-to-even rounds an exact half-way tie (such as 2.5 or 3.5) to the nearest even integer (2.5 rounds to 2, while 3.5 rounds to 4). Because roughly half of all integers are even and half odd, this rule balances upward and downward rounding over repeated trials, eliminating statistical bias."
          }
        },
        {
          "@type": "Question",
          "name": "Do exact numbers affect significant figures in scientific calculations?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. Exact numbers—such as counted discrete objects (e.g., 4 beakers), defined conversion constants (e.g., exactly 12 inches per foot, 1000 meters per kilometer, or 2.54 cm per inch), and theoretical mathematical constants (e.g., π or e)—possess an infinite number of significant figures. They never limit or constrain the precision of a calculation."
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
            <div class="badge-tag">Metrology & Experimental Measurement</div>
            <h1 class="tool-title">Significant Figures Calculator</h1>
            <p class="tool-subtitle">Identify significant digits, perform round-to-even operations, and solve multi-term scientific arithmetic with experimental uncertainty rules.</p>
          </header>

          <section class="calculator-card" aria-label="Significant Figures Solver">
            <div class="calc-grid">
              <div class="input-group">
                <label for="sigMode" class="input-label">Analysis Mode</label>
                <select id="sigMode" class="calc-input">
                  <option value="counter">Sig Fig Counter &amp; Rounder (Single Value)</option>
                  <option value="arithmetic">Sig Fig Arithmetic (Two Measurements)</option>
                </select>
              </div>

              <div class="input-group" id="inputVal1Group">
                <label for="sigInput1" class="input-label" id="labelSig1">Measurement Value</label>
                <input type="text" id="sigInput1" class="calc-input" value="0.0040500">
              </div>

              <div class="input-group" id="roundTargetGroup">
                <label for="roundDigits" class="input-label">Round to Target Sig Figs</label>
                <input type="number" id="roundDigits" class="calc-input" value="3" min="1" max="15">
              </div>

              <div class="input-group" id="sigOpGroup" style="display:none;">
                <label for="sigOp" class="input-label">Operation</label>
                <select id="sigOp" class="calc-input">
                  <option value="mul">Multiplication (×)</option>
                  <option value="div">Division (÷)</option>
                  <option value="add">Addition (+)</option>
                  <option value="sub">Subtraction (−)</option>
                </select>
              </div>

              <div class="input-group" id="inputVal2Group" style="display:none;">
                <label for="sigInput2" class="input-label">Second Measurement</label>
                <input type="text" id="sigInput2" class="calc-input" value="12.3">
              </div>
            </div>

            <div class="primary-result" style="margin-top: 25px;">
              <div class="result-label" id="sigPrimaryLabel">Significant Figures Count</div>
              <div class="result-value" id="sigPrimaryResult">5 Sig Figs</div>
              <div class="result-subtext" id="sigSubtext">Significant Digits: 4, 0, 5, 0, 0</div>
            </div>

            <div class="results-grid" style="margin-top: 20px;">
              <div class="result-item">
                <div class="result-label">Rounded to Target Sig Figs</div>
                <div class="result-value" id="resRoundedVal">0.00405</div>
              </div>
              <div class="result-item">
                <div class="result-label">Scientific Notation</div>
                <div class="result-value" id="resSigSci">4.0500 × 10⁻³</div>
              </div>
              <div class="result-item">
                <div class="result-label">Decimal Places</div>
                <div class="result-value" id="resDecPlaces">7</div>
              </div>
              <div class="result-item">
                <div class="result-label">Least Significant Column</div>
                <div class="result-value" id="resLeastCol">10⁻⁷ (0.0000001)</div>
              </div>
            </div>

            <div class="conversion-steps" style="margin-top: 25px;">
              <h3>Rule Breakdown &amp; Analysis</h3>
              <div id="sigStepsDisplay" style="font-family: monospace; font-size: 0.95rem; line-height: 1.6; background: rgba(0,0,0,0.03); padding: 16px; border-radius: 8px; border-left: 4px solid var(--accent, #2563eb);">
                Loading digit analysis...
              </div>
            </div>
          </section>

          <article class="article-body">
            <h2>1. The Physical Philosophy of Significant Figures in Metrology</h2>
            <p>In pure mathematics, numbers are abstract entities endowed with infinite precision: the integer \(5\) is identically \(5.000000\dots\) to limitless decimal digits. In empirical science, physics, chemistry, and experimental engineering, however, every recorded number represents an observation derived from physical instrumentation subjected to unavoidable measurement uncertainty. An analytical chemist weighing a crystalline precipitate on a four-place analytical balance records \(0.1420\text{ g}\), while a student using a mechanical pan scale records \(0.14\text{ g}\). Though numerically close, these two records convey vastly different degrees of experimental precision.</p>

            <p><strong>Significant Figures</strong> (often abbreviated as <em>sig figs</em> or <em>significant digits</em>) constitute an internationally standardized convention for communicating measurement precision. The number of significant figures in a reported quantity consists of all digits known with absolute certainty, plus exactly one terminal digit that is estimated or subject to instrumental tolerance (\(\pm 1\) in the last decimal place).</p>

            <h2>2. Canonical Rules for Counting Significant Digits</h2>
            <p>Every digit within a recorded measurement falls into one of several distinct functional categories. The universal rules for classifying digits are codified under ASTM E29 and international metrology guidelines:</p>

            <h3>2.1 Non-Zero Digits</h3>
            <p>All non-zero integers (\(1, 2, 3, 4, 5, 6, 7, 8, 9\)) are <strong>always significant</strong> regardless of their position relative to the decimal point. For example, the measurement \(384.72\text{ km}\) contains five non-zero digits and thus possesses exactly 5 significant figures.</p>

            <h3>2.2 Captive (Trapped) Zeros</h3>
            <p>Zeros situated between non-zero digits are <strong>always significant</strong> because their position is constrained by confirmed measurements on either side. For example, in \(6,005\text{ m}\) and \(40.08\text{ g}\), every zero is significant (giving 4 sig figs in each case).</p>

            <h3>2.3 Leading Zeros</h3>
            <p>Zeros that precede all non-zero digits are <strong>never significant</strong>. They serve solely as positional scale placeholders to indicate the order of magnitude of the decimal point. For example, in \(0.00054\text{ s}\), the four zeros are merely placeholders; the measurement possesses only 2 significant figures (\(5\) and \(4\)). Converting to scientific notation (\(5.4 \times 10^{-4}\text{ s}\)) or an SI metric prefix (\(540\text{ }\mu\text{s}\)) demonstrates that the leading zeros vanish without any loss of measurement information.</p>

            <h3>2.4 Trailing Zeros with an Explicit Decimal Point</h3>
            <p>Zeros at the end of a number to the right of a decimal point are <strong>always significant</strong>. By deliberately writing trailing zeros after a decimal point, the experimenter asserts that the measurement was verified down to that specific decimal threshold. For example, \(8.500\text{ cm}\) contains 4 significant figures, indicating that the instrument was precise to \(\pm 0.001\text{ cm}\). In contrast, writing \(8.5\text{ cm}\) conveys only 2 significant figures (precision \(\pm 0.1\text{ cm}\)).</p>

            <h3>2.5 Trailing Zeros in Whole Numbers (The Ambiguity Dilemma)</h3>
            <p>Trailing zeros in integers lacking a decimal point—such as \(1,200\text{ meters}\) or \(50,000\text{ kg}\)—are intrinsically ambiguous. It is impossible from the numerals alone to know whether the zeros represent measured values or approximate scale rounding. To eliminate this ambiguity, metrologists employ three standard methods:</p>
            <ul>
              <li><strong>Scientific Notation (Recommended):</strong> Writing \(1.2 \times 10^3\) denotes 2 sig figs; \(1.20 \times 10^3\) denotes 3 sig figs; \(1.200 \times 10^3\) denotes 4 sig figs.</li>
              <li><strong>Explicit Terminal Decimal:</strong> Writing <code>1200.</code> with a trailing decimal point explicitly indicates 4 sig figs.</li>
              <li><strong>Overline / Underline:</strong> Placing a bar over the last significant zero (\(12\bar{0}0\)) indicates 3 sig figs.</li>
            </ul>

            <h2>3. Arithmetic Operations with Uncertainty Propagation</h2>
            <p>When performing mathematical operations on experimental data, the calculation can never artificially fabricate precision: the output can never be more reliable than the least reliable measured input.</p>

            <h3>3.1 Multiplication and Division: The Sig Fig Count Rule</h3>
            <p>In multiplication and division, the calculated result is constrained strictly by the total number of significant figures of the input factors. The rule dictates:</p>

            <blockquote>
              <p>The product or quotient can have no more significant figures than the input value possessing the smallest number of significant figures.</p>
            </blockquote>

            <p>For example, consider calculating density \(\rho = \frac{m}{V}\):</p>

            $$\rho = \frac{45.26\text{ g}}{3.2\text{ cm}^3} = 14.14375\text{ g/cm}^3$$

            <p>Here, the mass \(45.26\text{ g}\) has 4 sig figs, while the volume \(3.2\text{ cm}^3\) has only 2 sig figs. The least precise factor has 2 sig figs. Therefore, the terminal result must be rounded to exactly 2 significant figures: \(\rho = 14\text{ g/cm}^3\).</p>

            <h3>3.2 Addition and Subtraction: The Decimal Place Rule</h3>
            <p>In addition and subtraction, the limiting constraint is not the total count of significant figures, but rather the <strong>decimal place position</strong> (the least significant decimal column). The rule dictates:</p>

            <blockquote>
              <p>The sum or difference can have no more digits to the right of the decimal point than the measurement with the fewest digits to the right of the decimal point.</p>
            </blockquote>

            <p>Consider summing three fluid volumes:</p>

            $$V_{\text{total}} = 125.1\text{ mL} + 1.254\text{ mL} + 0.08\text{ mL} = 126.434\text{ mL}$$

            <p>The least precise decimal position belongs to \(125.1\text{ mL}\) (tenths column, 1 decimal place). Therefore, the sum must be rounded to the tenths column: \(V_{\text{total}} = 126.4\text{ mL}\), even though the final result has 4 significant figures.</p>

            <h2>4. Rounding Rules and Banker's Rounding (Round-Half-to-Even)</h2>
            <p>When rounding intermediate numbers to conform to significant figure limits, the standard rule evaluates the first digit to be dropped (the rounding guard digit):</p>
            <ul>
              <li>If the first dropped digit is strictly less than 5 (\(0, 1, 2, 3, 4\)), the preceding digit remains unchanged (round down).</li>
              <li>If the first dropped digit is strictly greater than 5 (\(6, 7, 8, 9\)), or is 5 followed by non-zero digits, increment the preceding digit by 1 (round up).</li>
              <li><strong>The Half-Way Tie:</strong> When the dropped portion is exactly 5 followed by nothing or only zeros, standard metrology employs <em>Round-Half-to-Even</em> (Banker's Rounding, ASTM E29). Under this rule, round so that the final remaining digit is an even number:
                <ul>
                  <li>\(4.65\) rounded to 2 sig figs becomes \(4.6\) (since 6 is even).</li>
                  <li>\(4.75\) rounded to 2 sig figs becomes \(4.8\) (since 8 is even).</li>
                </ul>
              </li>
            </ul>
            <p>Round-half-to-even ensures that across large statistical datasets, 50% of borderline cases round down and 50% round up, neutralizing systematic cumulative upward bias.</p>

            <h2>5. Benchmark Comparative Reference Table</h2>
            <p>The table below provides a comprehensive breakdown of ten representative numerical values, illustrating sig fig counts, decimal places, scientific forms, and rounded results.</p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>Input Number</th>
                  <th>Total Sig Figs</th>
                  <th>Significant Digits</th>
                  <th>Decimal Places</th>
                  <th>Scientific Notation</th>
                  <th>Rounded to 3 Sig Figs</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>\(0.0040500\)</td>
                  <td>5</td>
                  <td>4, 0, 5, 0, 0</td>
                  <td>7</td>
                  <td>\(4.0500 \times 10^{-3}\)</td>
                  <td>\(0.00405\)</td>
                </tr>
                <tr>
                  <td>\(120.00\)</td>
                  <td>5</td>
                  <td>1, 2, 0, 0, 0</td>
                  <td>2</td>
                  <td>\(1.2000 \times 10^2\)</td>
                  <td>\(120\)</td>
                </tr>
                <tr>
                  <td>\(45000\)</td>
                  <td>2 (ambiguous)</td>
                  <td>4, 5</td>
                  <td>0</td>
                  <td>\(4.5 \times 10^4\)</td>
                  <td>\(4.50 \times 10^4\)</td>
                </tr>
                <tr>
                  <td>\(0.00008\)</td>
                  <td>1</td>
                  <td>8</td>
                  <td>5</td>
                  <td>\(8 \times 10^{-5}\)</td>
                  <td>\(0.0000800\)</td>
                </tr>
                <tr>
                  <td>\(100.04\)</td>
                  <td>5</td>
                  <td>1, 0, 0, 0, 4</td>
                  <td>2</td>
                  <td>\(1.0004 \times 10^2\)</td>
                  <td>\(100\)</td>
                </tr>
                <tr>
                  <td>\(3.14159265\)</td>
                  <td>9</td>
                  <td>3, 1, 4, 1, 5, 9, 2, 6, 5</td>
                  <td>8</td>
                  <td>\(3.14159 \times 10^0\)</td>
                  <td>\(3.14\)</td>
                </tr>
                <tr>
                  <td>\(5.00 \times 10^8\)</td>
                  <td>3</td>
                  <td>5, 0, 0</td>
                  <td>N/A</td>
                  <td>\(5.00 \times 10^8\)</td>
                  <td>\(5.00 \times 10^8\)</td>
                </tr>
                <tr>
                  <td>\(0.01020\)</td>
                  <td>4</td>
                  <td>1, 0, 2, 0</td>
                  <td>5</td>
                  <td>\(1.020 \times 10^{-2}\)</td>
                  <td>\(0.0102\)</td>
                </tr>
                <tr>
                  <td>\(65.45\)</td>
                  <td>4</td>
                  <td>6, 5, 4, 5</td>
                  <td>2</td>
                  <td>\(6.545 \times 10^1\)</td>
                  <td>\(65.4\) (even tie)</td>
                </tr>
                <tr>
                  <td>\(65.35\)</td>
                  <td>4</td>
                  <td>6, 5, 3, 5</td>
                  <td>2</td>
                  <td>\(6.35 \times 10^1\)</td>
                  <td>\(65.4\) (even tie)</td>
                </tr>
              </tbody>
            </table>

            <h2>6. Worked Chemical Laboratory Case Study: Analytical Titration Molarity</h2>
            <div class="worked-example-card">
              <div class="example-header">
                <strong>Analytical Chemistry Case Study:</strong> Acid-Base Standard Solution Standardization
              </div>
              <div class="example-body">
                <p><strong>Scenario:</strong> An analytical chemist standardizes a solution of sodium hydroxide (\(\text{NaOH}\)) by titrating against primary standard potassium hydrogen phthalate (\(\text{KHP}\), molecular weight \(MW = 204.22\text{ g/mol}\), known to 5 significant figures). The analytical balance records a KHP mass of \(m = 0.5124\text{ g}\). The initial burette reading is \(V_{\text{initial}} = 0.45\text{ mL}\) and the final reading at the phenolphthalein endpoint is \(V_{\text{final}} = 25.80\text{ mL}\). The chemist must calculate the exact molarity of \(\text{NaOH}\) following rigorous significant figure rules.</p>

                <p><strong>Step 1: Calculate Net Titrant Volume via Subtraction (Decimal Rule)</strong><br>
                $$V = V_{\text{final}} - V_{\text{initial}} = 25.80\text{ mL} - 0.45\text{ mL} = 25.35\text{ mL}$$
                Both burette readings have 2 decimal places. Therefore, the difference \(25.35\text{ mL}\) preserves 2 decimal places and has exactly 4 significant figures. Convert volume to liters:
                $$V = \frac{25.35\text{ mL}}{1000\text{ mL/L}} = 0.02535\text{ L} \quad (4 \text{ sig figs, 1000 is an exact conversion factor})$$</p>

                <p><strong>Step 2: Formulate the Molarity Equation (Multiplication/Division Rule)</strong><br>
                The stoichiometric reaction is \(1:1\). Molarity \(M\) satisfies:
                $$M = \frac{m_{\text{KHP}}}{MW_{\text{KHP}} \times V} = \frac{0.5124\text{ g}}{(204.22\text{ g/mol}) \times (0.02535\text{ L})}$$</p>

                <p><strong>Step 3: Analyze Input Significant Figures</strong><br>
                <ul>
                  <li>Mass \(m = 0.5124\text{ g}\): 4 significant figures.</li>
                  <li>Molecular weight \(MW = 204.22\text{ g/mol}\): 5 significant figures.</li>
                  <li>Volume \(V = 0.02535\text{ L}\): 4 significant figures.</li>
                </ul>
                The limiting precision is 4 significant figures.</p>

                <p><strong>Step 4: Compute Intermediate and Terminal Rounded Output</strong><br>
                $$M = \frac{0.5124}{5.176977} = 0.09897668\dots\text{ mol/L}$$
                Rounding to 4 significant figures yields:
                $$M = 0.09898\text{ mol/L} \quad (\text{or } 9.898 \times 10^{-2}\text{ M})$$
                Reporting any further digits (such as 0.098977) would fabricate non-existent instrumental precision.</p>
              </div>
            </div>

            <h2>7. Frequently Asked Questions (FAQ)</h2>
            <div class="faq-accordion">
              <div class="faq-item">
                <h3 class="faq-question">Why do conversion factors like 1 foot = 12 inches not limit significant figures?</h3>
                <div class="faq-answer">
                  <p>Definitions established by international standard agreements are exact quantities. By definition, 1 foot contains exactly 12 inches without any experimental tolerance (12.00000... to infinity). Because exact definitions possess infinite significant figures, they never constrain or reduce the precision of an experimental calculation.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">What are guard digits and when should they be retained during multi-step math?</h3>
                <div class="faq-answer">
                  <p>Guard digits are extra decimal digits carried through intermediate computational steps beyond the nominal significant figure limit. You should always retain at least 1 or 2 guard digits (or keep full floating-point precision in a calculator) during intermediate calculations, applying significant figure rounding strictly to the final result. Premature intermediate rounding causes cumulative rounding error drift.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">How does logarithmic calculation affect significant figures (e.g. pH in chemistry)?</h3>
                <div class="faq-answer">
                  <p>In logarithmic operations such as \(\text{pH} = -\log_{10}[\text{H}^+]\), the integer part of the logarithm (the characteristic) serves purely as an exponent/scale indicator. Only the decimal part (the mantissa) reflects the significant figures of the original quantity. Thus, if \([\text{H}^+] = 3.5 \times 10^{-5}\text{ M}\) (2 sig figs), then \(\text{pH} = 4.46\) (2 decimal places in the mantissa represent the 2 sig figs).</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">Is 100 with a decimal point (100.) accepted as having 3 significant figures?</h3>
                <div class="faq-answer">
                  <p>Yes. Placing an explicit decimal point at the end of a whole number (e.g., <code>100.</code>) is standard scientific shorthand indicating that all preceding zeros are measured and significant (3 sig figs). Without the terminal decimal point, 100 is treated as having only 1 significant figure unless specified otherwise in scientific notation (\(1.00 \times 10^2\)).</p>
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
              <li><a href="percentage-calculator.html">Percentage Calculator</a></li>
              <li><a href="standard-deviation-calculator.html">Standard Deviation Calculator</a></li>
              <li><a href="fraction-calculator.html">Fraction Calculator</a></li>
              <li><a href="gcd-lcm-calculator.html">GCD and LCM Calculator</a></li>
              <li><a href="quadratic-equation-calculator.html">Quadratic Equation Calculator</a></li>
              <li><a href="pythagorean-theorem-calculator.html">Pythagorean Theorem Calculator</a></li>
              <li><a href="prime-number-calculator.html">Prime Number Calculator</a></li>
            </ul>
          </div>

          <div class="sidebar-card">
            <h3 class="sidebar-title">Sig Fig Core Rules</h3>
            <div style="font-size:0.875rem; line-height:1.5; color:var(--text-muted, #4b5563);">
              <p><strong>Non-zeros:</strong> Always significant</p>
              <p><strong>Trapped zeros:</strong> Always significant</p>
              <p><strong>Leading zeros:</strong> Never significant</p>
              <p><strong>Trailing with dec:</strong> Always significant</p>
              <p><strong>Multiply/Divide:</strong> Fewest total sig figs</p>
              <p><strong>Add/Subtract:</strong> Fewest decimal places</p>
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
    function parseSigFigs(str) {
      str = str.trim();
      if (!str) return { count: 0, digits: [], decPlaces: 0, isSci: false };

      // Handle scientific notation e.g. 4.05e-3 or 4.05 * 10^-3
      let isSci = false;
      let expPart = "";
      if (/[eE]/.test(str)) {
        isSci = true;
        const parts = str.split(/[eE]/);
        str = parts[0];
        expPart = parts[1];
      }

      const hasDec = str.includes('.');
      const clean = str.replace('-', '');
      const parts = clean.split('.');
      const intPart = parts[0] || "";
      const decPart = parts.length > 1 ? parts[1] : "";

      let count = 0;
      const sigDigits = [];
      let started = false;

      // Scan characters
      for (let i = 0; i < clean.length; i++) {
        const c = clean[i];
        if (c === '.') continue;
        if (!started) {
          if (c !== '0') {
            started = true;
            count++;
            sigDigits.push(c);
          }
        } else {
          count++;
          sigDigits.push(c);
        }
      }

      // If no decimal and has trailing zeros
      if (!hasDec && !isSci) {
        // Trailing zeros in whole numbers are ambiguous, conventionally stripped
        while (sigDigits.length > 0 && sigDigits[sigDigits.length - 1] === '0') {
          sigDigits.pop();
          count--;
        }
      }

      const decPlaces = decPart.length;
      return { count: count, digits: sigDigits, decPlaces: decPlaces, hasDec: hasDec };
    }

    function roundToSigFigs(num, targetFigs) {
      if (num === 0) return "0";
      const d = Math.ceil(Math.log10(num < 0 ? -num : num));
      const power = targetFigs - d;
      const magnitude = Math.pow(10, power);
      const shifted = Math.round(num * magnitude);
      const rounded = shifted / magnitude;
      return rounded.toPrecision(targetFigs);
    }

    function updateSigMode() {
      const mode = document.getElementById('sigMode').value;
      const isArith = mode === 'arithmetic';
      document.getElementById('sigOpGroup').style.display = isArith ? 'block' : 'none';
      document.getElementById('inputVal2Group').style.display = isArith ? 'block' : 'none';
      document.getElementById('roundTargetGroup').style.display = isArith ? 'none' : 'block';
      document.getElementById('labelSig1').textContent = isArith ? "First Measurement" : "Measurement Value";
      computeSigFigs();
    }

    function computeSigFigs() {
      const mode = document.getElementById('sigMode').value;
      const val1Str = document.getElementById('sigInput1').value.trim();
      const val1 = parseFloat(val1Str);

      if (isNaN(val1) || !val1Str) return;

      const parsed1 = parseSigFigs(val1Str);
      let steps = "";

      if (mode === 'counter') {
        const targetFigs = parseInt(document.getElementById('roundDigits').value, 10) || 3;
        const rounded = roundToSigFigs(val1, targetFigs);
        const sci = val1.toExponential(parsed1.count > 1 ? parsed1.count - 1 : 1);

        document.getElementById('sigPrimaryLabel').textContent = "Significant Figures Count";
        document.getElementById('sigPrimaryResult').textContent = `${parsed1.count} Sig Figs`;
        document.getElementById('sigSubtext').textContent = `Significant Digits: ${parsed1.digits.join(', ')}`;
        document.getElementById('resRoundedVal').textContent = rounded;
        document.getElementById('resSigSci').textContent = sci;
        document.getElementById('resDecPlaces').textContent = parsed1.decPlaces;
        document.getElementById('resLeastCol').textContent = parsed1.hasDec ? `10⁻${parsed1.decPlaces}` : "Units (10⁰)";

        steps += `1. Non-zero sequence starts at '${parsed1.digits[0] || '0'}'.<br>`;
        steps += `2. Leading zeros are omitted (scale placeholders only).<br>`;
        steps += `3. Total confirmed significant digits: ${parsed1.count}.<br>`;
        steps += `4. Target rounding to ${targetFigs} sig figs: ${rounded}.`;
      } else {
        const val2Str = document.getElementById('sigInput2').value.trim();
        const val2 = parseFloat(val2Str);
        if (isNaN(val2) || !val2Str) return;

        const parsed2 = parseSigFigs(val2Str);
        const op = document.getElementById('sigOp').value;
        let resNum = 0;
        let finalStr = "";

        if (op === 'mul' || op === 'div') {
          const limitFigs = Math.min(parsed1.count, parsed2.count);
          resNum = op === 'mul' ? (val1 * val2) : (val1 / val2);
          finalStr = roundToSigFigs(resNum, limitFigs);
          document.getElementById('sigPrimaryLabel').textContent = "Arithmetic Result (Sig Fig Rule)";
          document.getElementById('sigPrimaryResult').textContent = finalStr;
          document.getElementById('sigSubtext').textContent = `Limited by ${limitFigs} sig figs (least precise input)`;
          steps += `Multiplication/Division Rule:<br>`;
          steps += `Term 1 has ${parsed1.count} sig figs; Term 2 has ${parsed2.count} sig figs.<br>`;
          steps += `Result constrained to min(${parsed1.count}, ${parsed2.count}) = ${limitFigs} sig figs.<br>`;
          steps += `Raw Calculation: ${resNum} → Rounded: ${finalStr}`;
        } else {
          const limitDec = Math.min(parsed1.decPlaces, parsed2.decPlaces);
          resNum = op === 'add' ? (val1 + val2) : (val1 - val2);
          finalStr = resNum.toFixed(limitDec);
          document.getElementById('sigPrimaryLabel').textContent = "Arithmetic Result (Decimal Rule)";
          document.getElementById('sigPrimaryResult').textContent = finalStr;
          document.getElementById('sigSubtext').textContent = `Limited by ${limitDec} decimal places (least precise column)`;
          steps += `Addition/Subtraction Rule:<br>`;
          steps += `Term 1 has ${parsed1.decPlaces} dec places; Term 2 has ${parsed2.decPlaces} dec places.<br>`;
          steps += `Result constrained to min(${parsed1.decPlaces}, ${parsed2.decPlaces}) = ${limitDec} decimal places.<br>`;
          steps += `Raw Calculation: ${resNum} → Rounded: ${finalStr}`;
        }

        document.getElementById('resRoundedVal').textContent = finalStr;
        document.getElementById('resSigSci').textContent = resNum.toExponential(3);
        document.getElementById('resDecPlaces').textContent = `Term 1: ${parsed1.decPlaces} | Term 2: ${parsed2.decPlaces}`;
        document.getElementById('resLeastCol').textContent = `Term 1: ${parsed1.count} SF | Term 2: ${parsed2.count} SF`;
      }

      document.getElementById('sigStepsDisplay').innerHTML = steps;
    }

    document.getElementById('sigMode').addEventListener('change', updateSigMode);
    document.getElementById('sigOp').addEventListener('change', computeSigFigs);
    document.getElementById('sigInput1').addEventListener('input', computeSigFigs);
    document.getElementById('sigInput2').addEventListener('input', computeSigFigs);
    document.getElementById('roundDigits').addEventListener('input', computeSigFigs);
    updateSigMode();
  </script>
</body>
</html>
"""

# -------------------------------------------------------------
# 2. PRIME NUMBER CALCULATOR
# -------------------------------------------------------------
prime_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Prime Number Calculator — Primality Test, Factorization & Divisors | CalcHub</title>
  <meta name="description" content="Test primality of any integer, generate complete prime factorizations, calculate divisor sums, and explore prime number theorems and RSA cryptography.">
  <meta name="keywords" content="prime number calculator, primality test, prime factorization calculator, is it prime, prime number checker, sieve of eratosthenes, twin primes, mersenne primes, rsa cryptography">
  <meta name="author" content="CalcHub Number Theory & Cryptographic Mathematics Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/prime-number-calculator.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="Prime Number Calculator — Primality Test, Factorization & Divisors | CalcHub">
  <meta property="og:description" content="Instant primality checking, prime factor tree decomposition, total divisor counts, and nearest prime navigation for any integer.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/prime-number-calculator.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/prime-number-calculator.html#app",
      "name": "Prime Number & Factorization Engine",
      "url": "https://calchub.org/prime-number-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "High-precision computational number theory tool for primality verification, canonical prime factorization, and divisor arithmetic."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Math & Engineering Calculators", "item": "https://calchub.org/math.html"},
        {"@type": "ListItem", "position": 3, "name": "Prime Number Calculator", "item": "https://calchub.org/prime-number-calculator.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the formal definition of a prime number and why is 1 excluded?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A prime number is defined as a positive integer strictly greater than 1 that possesses exactly two distinct positive divisors: 1 and itself. The number 1 is deliberately excluded from primes because if 1 were prime, the Fundamental Theorem of Arithmetic (which guarantees the unique prime factorization of every integer up to factor order) would be violated, since one could introduce arbitrarily many powers of 1 (e.g., 6 = 2 * 3 = 1 * 2 * 3 = 1² * 2 * 3), destroying uniqueness."
          }
        },
        {
          "@type": "Question",
          "name": "Why is trial division only required up to the square root of n (√n)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "If an integer n is composite, it can be factored as n = a * b. If both factors a and b were strictly greater than √n, their product would exceed n (a * b > √n * √n = n), which is a contradiction. Therefore, at least one non-trivial factor must satisfy factor ≤ √n. If no integer d in the range 2 ≤ d ≤ √n divides n, then n is guaranteed to be prime."
          }
        },
        {
          "@type": "Question",
          "name": "What is the Sieve of Eratosthenes and how efficient is it?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The Sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to a specified integer limit N. It works iteratively by marking the multiples of each prime starting from 2² = 4 as composite. The algorithm requires O(N log log N) arithmetic operations and O(N) memory, making it far superior to testing each individual integer independently."
          }
        },
        {
          "@type": "Question",
          "name": "How do prime numbers form the cryptographic backbone of modern internet security?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Asymmetric cryptosystems like RSA rely on the computational difficulty of prime factorization. Multiplying two large prime numbers (each 1024 or 2048 bits long) to produce a composite semiprime modulus n = p * q requires fractions of a millisecond. However, finding p and q given only n using the best known classical factoring algorithms would require millions of years of supercomputer time, creating a one-way trapdoor function that secures digital signatures, HTTPS connections, and banking transactions."
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
            <div class="badge-tag">Number Theory & Cryptographic Mathematics</div>
            <h1 class="tool-title">Prime Number Calculator</h1>
            <p class="tool-subtitle">Verify primality, generate canonical prime factor trees, calculate divisor sums, and find neighboring primes with trial division and sieve algorithms.</p>
          </header>

          <section class="calculator-card" aria-label="Prime Number Solver">
            <div class="calc-grid">
              <div class="input-group">
                <label for="primeInput" class="input-label">Positive Integer to Test (N)</label>
                <input type="number" id="primeInput" class="calc-input" value="9973" min="1" max="9007199254740991" step="1">
              </div>
            </div>

            <div class="primary-result" style="margin-top: 25px;">
              <div class="result-label">Primality Verification Status</div>
              <div class="result-value" id="primePrimaryStatus">9,973 is a PRIME NUMBER</div>
              <div class="result-subtext" id="primePrimarySubtext">Has exactly 2 distinct divisors: 1 and 9,973</div>
            </div>

            <div class="results-grid" style="margin-top: 20px;">
              <div class="result-item">
                <div class="result-label">Canonical Prime Factorization</div>
                <div class="result-value" id="resFactorization">9973¹</div>
              </div>
              <div class="result-item">
                <div class="result-label">Total Divisors Count \(d(n)\)</div>
                <div class="result-value" id="resDivCount">2 divisors</div>
              </div>
              <div class="result-item">
                <div class="result-label">Sum of Divisors \(\sigma(n)\)</div>
                <div class="result-value" id="resDivSum">9,974</div>
              </div>
              <div class="result-item">
                <div class="result-label">Nearest Lower Prime</div>
                <div class="result-value" id="resPrevPrime">9,967</div>
              </div>
              <div class="result-item">
                <div class="result-label">Nearest Higher Prime</div>
                <div class="result-value" id="resNextPrime">9,977</div>
              </div>
              <div class="result-item">
                <div class="result-label">Trial Limit (\(\lfloor\sqrt{N}\rfloor\))</div>
                <div class="result-value" id="resSqrtLimit">99</div>
              </div>
            </div>

            <div class="conversion-steps" style="margin-top: 25px;">
              <h3>Algorithmic Factorization Breakdown</h3>
              <div id="primeStepsDisplay" style="font-family: monospace; font-size: 0.95rem; line-height: 1.6; background: rgba(0,0,0,0.03); padding: 16px; border-radius: 8px; border-left: 4px solid var(--accent, #2563eb);">
                Loading factorization breakdown...
              </div>
            </div>
          </section>

          <article class="article-body">
            <h2>1. Number-Theoretic Foundations of Prime Numbers</h2>
            <p>In discrete mathematics and abstract algebra, <strong>prime numbers</strong> constitute the fundamental multiplicative building blocks of the positive integers \(\mathbb{Z}^+\). Formally, an integer \(p \in \mathbb{Z}^+\) is defined as prime if and only if \(p > 1\) and its only positive divisors are \(1\) and \(p\). Any integer \(n > 1\) that is not prime is termed <strong>composite</strong>, meaning it can be factored into a product of at least two smaller integers strictly greater than 1.</p>

            <p>The foundational status of primes is immortalized in the <strong>Fundamental Theorem of Arithmetic</strong> (Unique Factorization Theorem), first proven in Euclid's <em>Elements</em> (Book IX, Proposition 14):</p>

            <blockquote>
              <p>Every integer \(n > 1\) can be represented uniquely as a product of prime powers:</p>
              $$n = p_1^{\alpha_1} p_2^{\alpha_2} \cdots p_k^{\alpha_k} = \prod_{i=1}^k p_i^{\alpha_i}$$
              <p>where \(p_1 < p_2 < \dots < p_k\) are distinct prime numbers and \(\alpha_i \in \mathbb{Z}^+\) are positive integer exponents. This factorization is unique up to the permutation of factors.</p>
            </blockquote>

            <h3>1.1 Why the Number 1 is Neither Prime Nor Composite</h3>
            <p>Throughout mathematical history, 1 was occasionally considered prime by early thinkers because it has no divisors other than itself. However, modern number theory strictly classifies 1 as a <em>unit</em>. If 1 were classified as a prime, the Fundamental Theorem of Arithmetic would collapse: a number like \(12\) could be factored infinitely many ways (\(2^2 \times 3 = 1 \times 2^2 \times 3 = 1^5 \times 2^2 \times 3\)), requiring awkward ad-hoc qualifications across thousands of algebraic theorems.</p>

            <h2>2. Algorithmic Primality Testing and Complexity</h2>
            <p>Determining whether a given arbitrary integer \(N\) is prime or composite represents one of the most celebrated algorithmic problems in computer science.</p>

            <h3>2.1 Optimized Trial Division up to \(\sqrt{N}\)</h3>
            <p>The simplest deterministic primality test checks whether any integer \(d \ge 2\) divides \(N\). A profound mathematical optimization establishes that trial division needs to test divisors only up to the floor of the square root of \(N\) (\(\lfloor\sqrt{N}\rfloor\)).</p>

            <p><strong>Proof:</strong> Suppose \(N\) is composite. Then \(N = a \times b\) for some integers \(a, b\) with \(1 < a \le b < N\). If both factors were strictly greater than \(\sqrt{N}\), their product would satisfy \(a \times b > \sqrt{N} \times \sqrt{N} = N\), creating an algebraic contradiction. Hence, at least one factor must satisfy \(a \le \sqrt{N}\). If no divisor exists in the interval \([2, \sqrt{N}]\), \(N\) is guaranteed to be prime.</p>

            <p>Furthermore, testing all integers is wasteful: by first checking divisibility by 2 and 3, all subsequent prime candidates must be of the form \(6k \pm 1\) for \(k \ge 1\). This cuts the number of candidate test divisions by two-thirds.</p>

            <h3>2.2 The Sieve of Eratosthenes</h3>
            <p>When identifying all prime numbers up to a specified bound \(M\) (rather than testing a single isolated integer), the ancient Greek polymath Eratosthenes of Cyrene (c. 276 BCE) devised the <strong>Sieve of Eratosthenes</strong>:</p>
            <ol>
              <li>Create an indexed boolean array of size \(M\) initialized to <code>true</code>. Set indices 0 and 1 to <code>false</code>.</li>
              <li>Starting from the smallest prime \(p = 2\), mark all multiples \(2p, 3p, 4p, \dots \le M\) as composite (<code>false</code>). In practice, marking can begin at \(p^2\), since smaller multiples will already have been crossed off by smaller primes.</li>
              <li>Advance to the next unmarked number and repeat until \(p > \sqrt{M}\).</li>
            </ol>
            <p>The total computational complexity is \(O(M \log(\log M))\) arithmetic operations, executing in milliseconds for \(M = 10^7\).</p>

            <h3>2.3 Advanced Probabilistic and Deterministic Tests</h3>
            <p>For cryptographic numbers spanning hundreds or thousands of decimal digits, trial division up to \(\sqrt{N}\) would require more operations than there are atoms in the universe. Modern systems use advanced algorithms:</p>
            <ul>
              <li><strong>Miller-Rabin Primality Test:</strong> A randomized polynomial-time test based on Fermat's Little Theorem. Using deterministic prime bases, it deterministically verifies any 64-bit integer in fewer than 12 modular exponentiations.</li>
              <li><strong>Baillie-PSW Test:</strong> Combines Miller-Rabin base-2 with a Lucas pseudoprime test; has zero known counterexamples below \(2^{64}\).</li>
              <li><strong>AKS Primality Test:</strong> Discovered in 2002 by Agrawal, Kayal, and Saxena, proving unconditionally that primality testing belongs to the complexity class <strong>P</strong> (deterministic polynomial time).</li>
            </ul>

            <h2>3. Divisor Functions and Arithmetic Properties</h2>
            <p>From the unique prime factorization \(n = \prod_{i=1}^k p_i^{\alpha_i}\), several fundamental multiplicative arithmetic functions can be derived analytically:</p>

            <h3>3.1 Number of Divisors \(\tau(n)\) or \(d(n)\)</h3>
            <p>The total number of positive divisors of \(n\) equals the product of each prime exponent plus one:</p>

            $$d(n) = \prod_{i=1}^k (\alpha_i + 1) = (\alpha_1 + 1)(\alpha_2 + 1)\cdots(\alpha_k + 1)$$

            <p>For any prime \(p\), \(\alpha_1 = 1\), giving \(d(p) = 1 + 1 = 2\) (divisors 1 and \(p\)).</p>

            <h3>3.2 Sum of Divisors \(\sigma(n)\)</h3>
            <p>The sum of all positive divisors is given by the geometric series formula:</p>

            $$\sigma(n) = \prod_{i=1}^k \left(\frac{p_i^{\alpha_i + 1} - 1}{p_i - 1}\right)$$

            <p>For any prime \(p\), \(\sigma(p) = p + 1\). If \(\sigma(n) = 2n\), the integer \(n\) is termed a <em>perfect number</em> (such as 6, 28, 496, 8128), which by the Euclid-Euler theorem are intimately linked to Mersenne primes.</p>

            <h2>4. Prime Distribution and Famous Conjectures</h2>
            <p>Although primes appear irregularly distributed across the number line, their macro-scale asymptotic density adheres to precise mathematical laws:</p>

            <h3>4.1 The Prime Number Theorem (PNT)</h3>
            <p>Let \(\pi(x)\) denote the prime counting function, representing the number of primes less than or equal to \(x\). Proven independently by Jacques Hadamard and Charles Jean de la Vallée Poussin in 1896, the Prime Number Theorem establishes:</p>

            $$\lim_{x \to \infty} \frac{\pi(x)}{x / \ln(x)} = 1 \implies \pi(x) \sim \frac{x}{\ln(x)} \sim \operatorname{Li}(x)$$

            <p>This implies that the probability of an integer near \(x\) being prime is approximately \(\frac{1}{\ln x}\).</p>

            <h3>4.2 Deep Unsolved Conjectures in Prime Theory</h3>
            <ul>
              <li><strong>The Riemann Hypothesis:</strong> Asserts that all non-trivial zeros of the Riemann zeta function \(\zeta(s) = \sum_{n=1}^\infty n^{-s}\) have real part \(\operatorname{Re}(s) = \frac{1}{2}\). Proving this would yield the tightest possible error bounds for the distribution of primes.</li>
              <li><strong>Goldbach's Strong Conjecture:</strong> Every even integer greater than 2 can be expressed as the sum of two prime numbers (\(2n = p_1 + p_2\)). Verified computationally past \(4 \times 10^{18}\), but unproven in general.</li>
              <li><strong>Twin Prime Conjecture:</strong> There are infinitely many pairs of primes \((p, p + 2)\) differing by exactly 2 (such as 3 and 5, 11 and 13, 9971 and 9973).</li>
            </ul>

            <h2>5. Benchmark Comparative Reference Table</h2>
            <p>The table below provides a detailed structural breakdown across ten benchmark integers, contrasting primes, composites, semiprimes, divisor counts, and divisor sums.</p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>Integer \(N\)</th>
                  <th>Classification</th>
                  <th>Prime Factorization</th>
                  <th>Divisors Count \(d(N)\)</th>
                  <th>Divisors Sum \(\sigma(N)\)</th>
                  <th>Nearest Lower Prime</th>
                  <th>Nearest Higher Prime</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>9,973</td>
                  <td>Prime</td>
                  <td>\(9973^1\)</td>
                  <td>2</td>
                  <td>9,974</td>
                  <td>9,967</td>
                  <td>9,977</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>Smallest Prime (Only Even)</td>
                  <td>\(2^1\)</td>
                  <td>2</td>
                  <td>3</td>
                  <td>None</td>
                  <td>3</td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>Unit (Neither)</td>
                  <td>None</td>
                  <td>1</td>
                  <td>1</td>
                  <td>None</td>
                  <td>2</td>
                </tr>
                <tr>
                  <td>360</td>
                  <td>Highly Composite</td>
                  <td>\(2^3 \times 3^2 \times 5^1\)</td>
                  <td>24</td>
                  <td>1,170</td>
                  <td>359</td>
                  <td>367</td>
                </tr>
                <tr>
                  <td>1,009</td>
                  <td>Prime</td>
                  <td>\(1009^1\)</td>
                  <td>2</td>
                  <td>1,010</td>
                  <td>997</td>
                  <td>1,013</td>
                </tr>
                <tr>
                  <td>1,729</td>
                  <td>Composite (Ramanujan-Hardy)</td>
                  <td>\(7 \times 13 \times 19\)</td>
                  <td>8</td>
                  <td>2,688</td>
                  <td>1,723</td>
                  <td>1,733</td>
                </tr>
                <tr>
                  <td>8,191</td>
                  <td>Mersenne Prime (\(2^{13}-1\))</td>
                  <td>\(8191^1\)</td>
                  <td>2</td>
                  <td>8,192</td>
                  <td>8,179</td>
                  <td>8,209</td>
                </tr>
                <tr>
                  <td>10,000</td>
                  <td>Composite</td>
                  <td>\(2^4 \times 5^4\)</td>
                  <td>25</td>
                  <td>24,211</td>
                  <td>9,973</td>
                  <td>10,007</td>
                </tr>
                <tr>
                  <td>89</td>
                  <td>Fibonacci Prime</td>
                  <td>\(89^1\)</td>
                  <td>2</td>
                  <td>90</td>
                  <td>83</td>
                  <td>97</td>
                </tr>
                <tr>
                  <td>121</td>
                  <td>Composite (Square of Prime)</td>
                  <td>\(11^2\)</td>
                  <td>3</td>
                  <td>133</td>
                  <td>113</td>
                  <td>127</td>
                </tr>
              </tbody>
            </table>

            <h2>6. Worked Cryptographic Case Study: RSA Keypair Generation from Prime Primitives</h2>
            <div class="worked-example-card">
              <div class="example-header">
                <strong>Cryptographic Mathematics Case Study:</strong> Generating RSA Keys from Two Prime Primitives
              </div>
              <div class="example-body">
                <p><strong>Scenario:</strong> A cyber-security software engineer demonstrates the mathematical underpinnings of the RSA public-key cryptosystem using two verified 3-digit prime numbers: \(p = 251\) and \(q = 359\). The engineer must calculate: (1) the composite modulus \(n\), (2) Euler's totient function \(\phi(n)\), (3) a coprime public exponent \(e\), and (4) the private decryption exponent \(d\) using the Extended Euclidean Algorithm.</p>

                <p><strong>Step 1: Verify Primality of \(p\) and \(q\)</strong><br>
                For \(p = 251\): \(\lfloor\sqrt{251}\rfloor = 15\). Primes to test: \(2, 3, 5, 7, 11, 13\). None divide 251, so 251 is prime.<br>
                For \(q = 359\): \(\lfloor\sqrt{359}\rfloor = 18\). Primes to test: \(2, 3, 5, 7, 11, 13, 17\). None divide 359, so 359 is prime.</p>

                <p><strong>Step 2: Compute the Semiprime Modulus \(n\)</strong><br>
                $$n = p \times q = 251 \times 359 = 90,109$$
                The integer \(n = 90,109\) is published publicly as the encryption modulus.</p>

                <p><strong>Step 3: Calculate Euler's Totient Function \(\phi(n)\)</strong><br>
                Because \(p\) and \(q\) are prime, the count of integers coprime to \(n\) is:
                $$\phi(n) = (p - 1)(q - 1) = (250) \times (358) = 89,500$$</p>

                <p><strong>Step 4: Select Public Exponent \(e\) and Compute Private Key \(d\)</strong><br>
                Choose standard public exponent \(e = 17\) (verifying that \(\gcd(17, 89500) = 1\)).<br>
                The private decryption key \(d\) must satisfy the modular inverse identity:
                $$e \cdot d \equiv 1 \pmod{\phi(n)} \implies 17 \cdot d \equiv 1 \pmod{89500}$$
                Running the Extended Euclidean Algorithm:
                $$\begin{aligned}
                89500 &= 17 \times 5264 + 12 \\
                17 &= 12 \times 1 + 5 \\
                12 &= 5 \times 2 + 2 \\
                5 &= 2 \times 2 + 1
                \end{aligned}$$
                Back-substituting yields the Bézout identity:
                $$17 \times (42118) - 89500 \times (8) = 1$$
                Thus, the private decryption key is \(d = 42,118\). An adversary attempting to decrypt an intercepted message must factor \(90,109\) back into \(251 \times 359\) to derive \(\phi(n)\), which is intractable for large numbers.</p>
              </div>
            </div>

            <h2>7. Frequently Asked Questions (FAQ)</h2>
            <div class="faq-accordion">
              <div class="faq-item">
                <h3 class="faq-question">What are Mersenne primes and why are they so heavily studied?</h3>
                <div class="faq-answer">
                  <p>A Mersenne prime is a prime number of the form \(M_p = 2^p - 1\), where the exponent \(p\) is itself prime. They are studied intensely through the Great Internet Mersenne Prime Search (GIMPS) because the Lucas-Lehmer test provides an ultra-fast primality test tailored exclusively to this form, enabling computers to discover record-breaking primes containing tens of millions of decimal digits.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">Are negative numbers ever considered prime?</h3>
                <div class="faq-answer">
                  <p>In standard arithmetic and elementary number theory, primes are defined strictly as positive integers (\(p \in \mathbb{Z}^+\)). In advanced ring theory and abstract algebra, elements like \(-2, -3, -5\) are considered <em>irreducible associate elements</em> of the positive primes, differing only by multiplication by a unit (\(-1\)). For all practical computational purposes, primes are positive.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">What is a semiprime number?</h3>
                <div class="faq-answer">
                  <p>A semiprime (also termed a 2-almost prime) is a natural number that is the product of exactly two prime numbers: \(n = p \times q\). The primes may be distinct (e.g., \(15 = 3 \times 5\)) or identical (e.g., \(9 = 3^2\)). Semiprimes are the core component of RSA encryption moduli.</p>
                </div>
              </div>

              <div class="faq-item">
                <h3 class="faq-question">Can an even number greater than 2 ever be prime?</h3>
                <div class="faq-answer">
                  <p>No. By definition, every even number is divisible by 2. For an even number \(n > 2\), its positive divisors include at least 1, 2, and \(n\). Having at least three distinct divisors violates the primality definition requiring exactly two divisors. Thus, 2 is uniquely the only even prime number.</p>
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
              <li><a href="quadratic-equation-calculator.html">Quadratic Equation Calculator</a></li>
              <li><a href="pythagorean-theorem-calculator.html">Pythagorean Theorem Calculator</a></li>
              <li><a href="scientific-notation-calculator.html">Scientific Notation Calculator</a></li>
              <li><a href="significant-figures-calculator.html">Significant Figures Calculator</a></li>
              <li><a href="percentage-calculator.html">Percentage Calculator</a></li>
              <li><a href="matrix-calculator.html">Matrix Calculator</a></li>
            </ul>
          </div>

          <div class="sidebar-card">
            <h3 class="sidebar-title">Number Theory Rules</h3>
            <div style="font-size:0.875rem; line-height:1.5; color:var(--text-muted, #4b5563);">
              <p><strong>Prime:</strong> Exactly 2 divisors (\(1, p\))</p>
              <p><strong>Limit:</strong> Test up to \(\lfloor\sqrt{n}\rfloor\)</p>
              <p><strong>Form:</strong> All primes \(>3\) are \(6k \pm 1\)</p>
              <p><strong>Divisors:</strong> \(d(n) = \prod (\alpha_i + 1)\)</p>
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
    function isPrimeSimple(n) {
      if (n <= 1) return false;
      if (n <= 3) return true;
      if (n % 2 === 0 || n % 3 === 0) return false;
      let i = 5;
      while (i * i <= n) {
        if (n % i === 0 || n % (i + 2) === 0) return false;
        i += 6;
      }
      return true;
    }

    function factorize(n) {
      const factors = {};
      let d = 2;
      while (d * d <= n) {
        while (n % d === 0) {
          factors[d] = (factors[d] || 0) + 1;
          n = Math.floor(n / d);
        }
        d = d === 2 ? 3 : d + 2;
      }
      if (n > 1) {
        factors[n] = (factors[n] || 0) + 1;
      }
      return factors;
    }

    function checkPrime() {
      const inputVal = parseInt(document.getElementById('primeInput').value, 10);
      if (isNaN(inputVal) || inputVal < 1) return;

      const n = inputVal;
      const sqrtN = Math.floor(Math.sqrt(n));
      document.getElementById('resSqrtLimit').textContent = sqrtN.toLocaleString();

      if (n === 1) {
        document.getElementById('primePrimaryStatus').textContent = "1 is NEITHER Prime nor Composite";
        document.getElementById('primePrimarySubtext').textContent = "1 is a unit, having exactly one positive divisor: itself.";
        document.getElementById('resFactorization').textContent = "None (Unit)";
        document.getElementById('resDivCount').textContent = "1 divisor";
        document.getElementById('resDivSum').textContent = "1";
        document.getElementById('resPrevPrime').textContent = "None";
        document.getElementById('resNextPrime').textContent = "2";
        document.getElementById('primeStepsDisplay').innerHTML = "1 is classified as a unit in number theory to preserve the unique factorization theorem.";
        return;
      }

      const isPrime = isPrimeSimple(n);
      const factors = factorize(n);

      // Total divisors d(n) and sum sigma(n)
      let dCount = 1;
      let dSum = 1;
      const factorTerms = [];

      for (const pStr in factors) {
        const p = parseInt(pStr, 10);
        const a = factors[pStr];
        dCount *= (a + 1);
        dSum *= (Math.pow(p, a + 1) - 1) / (p - 1);
        factorTerms.push(a > 1 ? `${p}^${a}` : `${p}`);
      }

      const factorStr = factorTerms.join(" × ");

      if (isPrime) {
        document.getElementById('primePrimaryStatus').textContent = `${n.toLocaleString()} is a PRIME NUMBER`;
        document.getElementById('primePrimarySubtext').textContent = `Has exactly 2 distinct divisors: 1 and ${n.toLocaleString()}`;
      } else {
        document.getElementById('primePrimaryStatus').textContent = `${n.toLocaleString()} is a COMPOSITE NUMBER`;
        document.getElementById('primePrimarySubtext').textContent = `Can be factored as ${factorStr}`;
      }

      document.getElementById('resFactorization').textContent = factorStr;
      document.getElementById('resDivCount').textContent = `${dCount} divisors`;
      document.getElementById('resDivSum').textContent = dSum.toLocaleString();

      // Find nearest primes
      let prevP = "None";
      for (let p = n - 1; p >= 2; p--) {
        if (isPrimeSimple(p)) {
          prevP = p.toLocaleString();
          break;
        }
      }
      document.getElementById('resPrevPrime').textContent = prevP;

      let nextP = n + 1;
      while (!isPrimeSimple(nextP)) {
        nextP++;
      }
      document.getElementById('resNextPrime').textContent = nextP.toLocaleString();

      let stepsHtml = `1. Target integer N = ${n.toLocaleString()}<br>`;
      stepsHtml += `2. Maximum trial division limit: ⌊√${n}⌋ = ${sqrtN.toLocaleString()}<br>`;
      if (isPrime) {
        stepsHtml += `3. Tested all prime divisors up to ${sqrtN.toLocaleString()}. No integer divides ${n}.<br>`;
        stepsHtml += `4. Conclusion: ${n} is strictly prime.`;
      } else {
        stepsHtml += `3. Found non-trivial factors via prime decomposition.<br>`;
        stepsHtml += `4. Canonical Prime Factorization: ${factorStr}<br>`;
        stepsHtml += `5. Total Divisors d(${n}) = ${dCount}; Sum σ(${n}) = ${dSum.toLocaleString()}.`;
      }
      document.getElementById('primeStepsDisplay').innerHTML = stepsHtml;
    }

    document.getElementById('primeInput').addEventListener('input', checkPrime);
    checkPrime();
  </script>
</body>
</html>
"""

# Write files
with open(os.path.join(BASE_DIR, 'significant-figures-calculator.html'), 'w', encoding='utf-8') as f:
    f.write(sigfig_html)
print("Generated significant-figures-calculator.html successfully!")

with open(os.path.join(BASE_DIR, 'prime-number-calculator.html'), 'w', encoding='utf-8') as f:
    f.write(prime_html)
print("Generated prime-number-calculator.html successfully!")
