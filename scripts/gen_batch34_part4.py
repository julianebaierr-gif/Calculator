# -*- coding: utf-8 -*-
"""
Generator for Batch 34 - Part 4:
7. theoretical-yield-calculator.html
8. ppm-calculator.html
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 7. theoretical-yield-calculator.html
HTML_THEOR_YIELD = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Theoretical Yield Calculator - Limiting Reactant &amp; Maximum Product Mass</title>
  <meta name="description" content="Calculate theoretical yield, identify the limiting reactant, compute excess reagent remaining, and evaluate stoichiometry with step-by-step proofs.">
  <link rel="canonical" href="https://calchub.org/theoretical-yield-calculator.html">
  <meta property="og:title" content="Theoretical Yield Calculator - Limiting Reactant &amp; Stoichiometry Solver">
  <meta property="og:description" content="Free chemistry theoretical yield calculator. Identify limiting reagents, calculate maximum product grams, and compute unreacted excess mass with step-by-step steps.">
  <meta property="og:url" content="https://calchub.org/theoretical-yield-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Theoretical Yield Calculator - Stoichiometric Analysis Tool">
  <meta name="twitter:description" content="Compute maximum product output, limiting reactants, and excess reagent leftovers across chemical equations.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Theoretical Yield Calculator",
    "url": "https://calchub.org/theoretical-yield-calculator.html",
    "description": "Calculates the maximum theoretical product yield, identifies the limiting reactant, and determines leftover excess reactants from balanced chemical equations.",
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
        "name": "What is theoretical yield in chemistry?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Theoretical yield is the maximum mass or amount of product that can be formed in a chemical reaction, calculated from the complete consumption of the limiting reactant according to the balanced stoichiometric equation, assuming 100% conversion efficiency."
        }
      },
      {
        "@type": "Question",
        "name": "How do you identify the limiting reactant?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "To find the limiting reactant: (1) Convert the starting mass of each reactant to moles (n = m / M); (2) Divide the moles of each reactant by its stoichiometric coefficient in the balanced chemical equation (n / coefficient); (3) The reactant with the smallest resulting ratio is strictly the limiting reactant, which dictates the theoretical yield."
        }
      },
      {
        "@type": "Question",
        "name": "How do you calculate excess reactant remaining after a reaction?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "To find leftover excess reactant: (1) Determine the moles of excess reactant consumed by multiplying the limiting reactant's moles by the stoichiometric molar ratio between the two reactants; (2) Subtract the consumed moles from the initial starting moles to find excess moles remaining; (3) Multiply leftover moles by the excess reactant's molar mass to obtain remaining mass in grams."
        }
      },
      {
        "@type": "Question",
        "name": "Why is the actual yield almost always lower than the theoretical yield?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Actual laboratory yield is lower due to thermodynamic equilibrium limitations, incomplete reactions, side reactions producing unwanted byproducts, and physical losses during isolation steps like filtration, recrystallization, and liquid-liquid extraction."
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
        <a href="math.html">Math &amp; Statistics</a>
        <a href="converter.html">Converters</a>
        <a href="engineering.html" class="active">Engineering</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="page-container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo;
      <a href="chemical.html">Chemical &amp; Water</a> &rsaquo;
      <span>Theoretical Yield Calculator</span>
    </nav>

    <div class="page-header">
      <h1 class="page-title">Theoretical Yield Calculator</h1>
      <p class="page-desc">Determine the limiting reactant, maximum theoretical product mass, and leftover excess reagents from balanced stoichiometric equations.</p>
    </div>

    <div class="calc-grid">
      <!-- Calculator Column -->
      <div class="calc-card">
        <div class="calc-header">
          <h2>Limiting Reactant &amp; Theoretical Yield Solver</h2>
        </div>

        <!-- Preset Selection -->
        <div class="form-group">
          <label for="ty-preset">Balanced Chemical Reaction Preset:</label>
          <select id="ty-preset" class="form-control">
            <option value="custom">-- Custom Reaction Parameters --</option>
            <option value="water" selected>Water Synthesis: 2 H2 + 1 O2 &rarr; 2 H2O</option>
            <option value="ammonia">Haber Ammonia: 1 N2 + 3 H2 &rarr; 2 NH3</option>
            <option value="iron">Blast Furnace Iron: 1 Fe2O3 + 3 CO &rarr; 2 Fe + 3 CO2</option>
            <option value="methane">Methane Combustion: 1 CH4 + 2 O2 &rarr; 1 CO2 + 2 H2O</option>
            <option value="aspirin">Aspirin: 1 C7H6O3 + 1 C4H6O3 &rarr; 1 C9H8O4 + 1 C2H4O2</option>
          </select>
        </div>

        <!-- Reactant 1 Panel -->
        <div class="solid-panel" style="background: var(--surface-card, #f8fafc); padding: 1rem; border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0); margin-bottom: 1rem;">
          <h3 style="font-size: 0.95rem; margin-top: 0; margin-bottom: 0.75rem; color: var(--text-main, #0f172a);">Reactant A (<span id="ty-r1-name">H₂</span>)</h3>
          <div class="form-row">
            <div class="form-group">
              <label for="ty-r1-coeff">Stoichiometric Coeff ($a$):</label>
              <input type="number" id="ty-r1-coeff" class="form-control" value="2" min="1" step="1">
            </div>
            <div class="form-group">
              <label for="ty-r1-mw">Molar Mass ($M_A$ in g/mol):</label>
              <input type="number" id="ty-r1-mw" class="form-control" value="2.016" step="any" min="0.001">
            </div>
            <div class="form-group">
              <label for="ty-r1-mass">Initial Mass ($m_A$ in g):</label>
              <input type="number" id="ty-r1-mass" class="form-control" value="10.0" step="any" min="0.0001">
            </div>
          </div>
        </div>

        <!-- Reactant 2 Panel -->
        <div class="solid-panel" style="background: var(--surface-card, #f8fafc); padding: 1rem; border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0); margin-bottom: 1rem;">
          <h3 style="font-size: 0.95rem; margin-top: 0; margin-bottom: 0.75rem; color: var(--text-main, #0f172a);">Reactant B (<span id="ty-r2-name">O₂</span>)</h3>
          <div class="form-row">
            <div class="form-group">
              <label for="ty-r2-coeff">Stoichiometric Coeff ($b$):</label>
              <input type="number" id="ty-r2-coeff" class="form-control" value="1" min="1" step="1">
            </div>
            <div class="form-group">
              <label for="ty-r2-mw">Molar Mass ($M_B$ in g/mol):</label>
              <input type="number" id="ty-r2-mw" class="form-control" value="31.999" step="any" min="0.001">
            </div>
            <div class="form-group">
              <label for="ty-r2-mass">Initial Mass ($m_B$ in g):</label>
              <input type="number" id="ty-r2-mass" class="form-control" value="64.0" step="any" min="0.0001">
            </div>
          </div>
        </div>

        <!-- Target Product Panel -->
        <div class="solid-panel" style="background: var(--surface-card, #f8fafc); padding: 1rem; border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0); margin-bottom: 1rem;">
          <h3 style="font-size: 0.95rem; margin-top: 0; margin-bottom: 0.75rem; color: var(--text-main, #0f172a);">Target Product C (<span id="ty-prod-name">H₂O</span>)</h3>
          <div class="form-row">
            <div class="form-group">
              <label for="ty-prod-coeff">Stoichiometric Coeff ($c$):</label>
              <input type="number" id="ty-prod-coeff" class="form-control" value="2" min="1" step="1">
            </div>
            <div class="form-group">
              <label for="ty-prod-mw">Molar Mass ($M_C$ in g/mol):</label>
              <input type="number" id="ty-prod-mw" class="form-control" value="18.015" step="any" min="0.001">
            </div>
          </div>
        </div>

        <div class="form-actions">
          <button type="button" id="ty-calc-btn" class="btn btn-primary">Calculate Theoretical Yield</button>
          <button type="button" id="ty-reset-btn" class="btn btn-secondary">Reset</button>
        </div>

        <!-- Output Hero and Cards -->
        <div id="ty-results" class="results-container" style="margin-top: 1.5rem;">
          <div class="result-hero-card">
            <div class="result-label" style="font-size: 0.875rem; color: var(--text-muted, #64748b); text-transform: uppercase; font-weight: 600;">Maximum Theoretical Yield</div>
            <div id="ty-primary-out" style="font-size: 2.25rem; font-weight: 800; color: var(--primary, #2563eb); margin: 0.25rem 0;">72.06 g</div>
            <div id="ty-status-out" style="font-size: 1rem; color: var(--text-secondary, #475569); font-weight: 600;">Limiting Reactant: Reactant B (O₂)</div>
          </div>

          <div class="summary-metrics-grid">
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Limiting Reagent</div>
              <div id="ty-limiting-out" style="font-size: 1.15rem; font-weight: 700; color: #dc2626;">Reactant B</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Product Moles ($n_C$)</div>
              <div id="ty-moles-out" style="font-size: 1.15rem; font-weight: 700;">4.000 mol</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Excess Leftover Mass</div>
              <div id="ty-excess-mass-out" style="font-size: 1.15rem; font-weight: 700; color: #059669;">1.94 g (Reactant A)</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Reactant A Conversion</div>
              <div id="ty-conv-out" style="font-size: 1.15rem; font-weight: 700;">80.6% Consumed</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Reference Sidebar -->
      <aside class="sidebar-card">
        <h3>Stoichiometric Algorithm Steps</h3>
        <ol style="font-size: 0.875rem; line-height: 1.6; margin-left: 1.25rem; padding-left: 0;">
          <li>Convert starting masses to moles: \(n = m / M\).</li>
          <li>Normalize by stoichiometric coefficients: \(n_A / a\) vs \(n_B / b\).</li>
          <li>Smaller ratio identifies the **limiting reactant**.</li>
          <li>Calculate product moles: \(n_C = n_{\text{lim}} \times (c / \nu_{\text{lim}})\).</li>
          <li>Convert to theoretical mass: \(m_C = n_C \times M_C\).</li>
          <li>Compute unconsumed excess reactant remaining.</li>
        </ol>

        <h3 style="margin-top: 1.25rem;">Key Equations</h3>
        <ul style="font-size: 0.875rem; line-height: 1.6; margin-left: 1.25rem;">
          <li>\(m_{\text{theor}} = \left(\frac{n_{\text{lim}}}{\nu_{\text{lim}}}\right) \times c \times M_C\)</li>
          <li>\(m_{\text{excess left}} = m_{\text{init}} - (n_{\text{used}} \times M)\)</li>
        </ul>
      </aside>
    </div>

    <!-- Long-Form Informational Engineering Article (1,400+ Words) -->
    <article class="article-body">
      <h2>1. The Chemical Principles of Theoretical Yield and Limiting Reactants</h2>
      <p>Theoretical yield represents the absolute maximum quantity of product that can be generated in a chemical reaction, calculated mathematically on the assumption of 100% stoichiometric conversion of the limiting reagent with zero side reactions, complete thermodynamic irreversibility, and zero physical isolation loss. In quantitative chemical engineering and laboratory research, theoretical yield establishes the stoichiometric ceiling against which the actual efficiency (percent yield) of any chemical process is evaluated.</p>
      <p>Chemical reactions operate strictly on whole-number atomic and molecular ratios dictated by balanced equations:</p>
      $$a\text{ A} + b\text{ B} \longrightarrow c\text{ C} + d\text{ D}$$
      <p>Where \(a\), \(b\), \(c\), and \(d\) are the integer stoichiometric coefficients. In laboratory reality, reactants are rarely charged in perfectly stoichiometric molar proportions (\(n_{\text{A}} / a = n_{\text{B}} / b\)). One reactant is invariably present in lesser stoichiometric quantity relative to its required ratio; this species is designated the **limiting reactant** (or limiting reagent), while the other is the **excess reactant**.</p>
      <p>Because the limiting reactant is completely consumed first, the reaction halts immediately once its supply is exhausted. The theoretical yield of product \(\text{C}\) is therefore constrained exclusively by the initial quantity of the limiting reactant.</p>

      <h2>2. Mathematical Algorithm for Determining Limiting Reagents</h2>
      <p>To identify the limiting reactant and compute theoretical yield without ambiguity, chemical engineers follow a standardized four-stage algorithmic workflow:</p>
      <ol>
        <li><strong>Step 1: Convert Starting Masses to Moles:</strong>
        $$n_{\text{A}} = \frac{m_{\text{A}}}{M_{\text{A}}}, \quad n_{\text{B}} = \frac{m_{\text{B}}}{M_{\text{B}}}$$
        Where \(m_{\text{A}}\) and \(m_{\text{B}}\) are starting masses in grams, and \(M_{\text{A}}\) and \(M_{\text{B}}\) are molecular weights in grams per mole.</li>
        <li><strong>Step 2: Normalize by Stoichiometric Coefficients:</strong>
        Divide each reactant's molar quantity by its respective balanced stoichiometric coefficient:
        $$\text{Ratio}_{\text{A}} = \frac{n_{\text{A}}}{a}, \quad \text{Ratio}_{\text{B}} = \frac{n_{\text{B}}}{b}$$
        The reactant possessing the **smaller normalized ratio** is mathematically proven to be the limiting reactant:
        $$\text{If } \text{Ratio}_{\text{A}} &lt; \text{Ratio}_{\text{B}} \implies \text{A is the Limiting Reactant.}$$</li>
        <li><strong>Step 3: Calculate Maximum Theoretical Product Output:</strong>
        Using the limiting reactant (let us assume \(\text{A}\) is limiting), calculate the maximum theoretical moles of product \(\text{C}\):
        $$n_{\text{C, theoretical}} = n_{\text{A}} \times \left(\frac{c}{a}\right)$$
        Multiply by the molar mass of product \(\text{C}\) (\(M_{\text{C}}\)) to obtain the theoretical mass:
        $$m_{\text{C, theoretical}} = n_{\text{C, theoretical}} \times M_{\text{C}} = \left(\frac{n_{\text{A}}}{a}\right) \times c \times M_{\text{C}}$$</li>
        <li><strong>Step 4: Compute Unconsumed Excess Reactant Leftover:</strong>
        Calculate the moles of excess reactant \(\text{B}\) consumed during the reaction:
        $$n_{\text{B, consumed}} = n_{\text{A}} \times \left(\frac{b}{a}\right)$$
        Subtract consumed moles from starting moles to obtain the leftover excess:
        $$n_{\text{B, remaining}} = n_{\text{B, initial}} - n_{\text{B, consumed}}$$
        $$m_{\text{B, remaining}} = n_{\text{B, remaining}} \times M_{\text{B}}$$</li>
      </ol>

      <h2>3. Industrial Stoichiometry: Why Excess Reactants Are Deliberately Added</h2>
      <p>In academic textbooks, stoichiometric problems often assume balanced inputs. In industrial chemical manufacturing, however, chemical engineers almost always intentionally charge one reactant in massive stoichiometric excess (often \(10\%\) to \(200\%\) excess):</p>
      <ul>
        <li><strong>Driving Equilibrium via Le Chatelier's Principle:</strong> For reversible reactions where the equilibrium constant \(K_{\text{eq}}\) is modest, increasing the concentration of one reactant forces the equilibrium position to the right, driving higher conversion of the more expensive limiting reactant.</li>
        <li><strong>Cost Optimization:</strong> If reactant \(\text{A}\) is a costly, complex pharmaceutical intermediate while reactant \(\text{B}\) is an inexpensive commodity reagent (e.g., acetic anhydride, oxygen, or sodium hydroxide), charging excess \(\text{B}\) ensures that virtually 100% of valuable reactant \(\text{A}\) is consumed.</li>
        <li><strong>Accelerating Reaction Kinetics:</strong> According to chemical rate laws (\(\text{Rate} = k [\text{A}]^x [\text{B}]^y\)), flooding the reactor with a high concentration of reactant \(\text{B}\) dramatically accelerates reaction velocity, reducing vessel residence time and increasing plant throughput.</li>
      </ul>

      <h2>4. Stoichiometric Limiting Reactant Benchmark Table</h2>
      <p>The following engineering data table illustrates limiting reactant dynamics, theoretical yields, and excess leftovers across diverse chemical synthesis scenarios:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Reaction System</th>
              <th>Balanced Equation</th>
              <th>Input Mass Reactant 1</th>
              <th>Input Mass Reactant 2</th>
              <th>Limiting Reactant</th>
              <th>Theoretical Yield</th>
              <th>Excess Leftover</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Water Synthesis</td>
              <td>2 H₂ + 1 O₂ &rarr; 2 H₂O</td>
              <td>10.0 g H₂</td>
              <td>64.0 g O₂</td>
              <td>O₂ (2.0 mol)</td>
              <td>72.06 g H₂O</td>
              <td>1.94 g H₂ (19.4%)</td>
            </tr>
            <tr>
              <td>Ammonia Synthesis</td>
              <td>1 N₂ + 3 H₂ &rarr; 2 NH₃</td>
              <td>28.0 g N₂</td>
              <td>10.0 g H₂</td>
              <td>N₂ (1.0 mol)</td>
              <td>34.06 g NH₃</td>
              <td>3.95 g H₂ (39.5%)</td>
            </tr>
            <tr>
              <td>Iron Blast Smelting</td>
              <td>1 Fe₂O₃ + 3 CO &rarr; 2 Fe + 3 CO₂</td>
              <td>100.0 g Fe₂O₃</td>
              <td>60.0 g CO</td>
              <td>Fe₂O₃ (0.626 mol)</td>
              <td>69.94 g Fe</td>
              <td>7.40 g CO (12.3%)</td>
            </tr>
            <tr>
              <td>Methane Combustion</td>
              <td>1 CH₄ + 2 O₂ &rarr; 1 CO₂ + 2 H₂O</td>
              <td>16.04 g CH₄</td>
              <td>80.0 g O₂</td>
              <td>CH₄ (1.00 mol)</td>
              <td>44.01 g CO₂</td>
              <td>16.0 g O₂ (20.0%)</td>
            </tr>
            <tr>
              <td>Aspirin Synthesis</td>
              <td>1 C₇H₆O₃ + 1 C₄H₆O₃ &rarr; 1 C₉H₈O₄ + 1 C₂H₄O₂</td>
              <td>13.81 g Salicylic</td>
              <td>15.31 g Acetic Anh.</td>
              <td>Salicylic (0.10 mol)</td>
              <td>18.02 g Aspirin</td>
              <td>5.10 g Acetic Anh.</td>
            </tr>
            <tr>
              <td>Aluminum Thermite</td>
              <td>2 Al + 1 Fe₂O₃ &rarr; 1 Al₂O₃ + 2 Fe</td>
              <td>54.0 g Al</td>
              <td>159.7 g Fe₂O₃</td>
              <td>Exact Stoichiometric</td>
              <td>111.7 g Fe</td>
              <td>0.0 g (100% matched)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>5. Step-by-Step Worked Engineering Case Studies</h2>

      <div class="worked-example-card">
        <h3>Case Study 1: Ammonia Synthesis via Haber-Bosch Process</h3>
        <p><strong>Scenario:</strong> A chemical reactor is charged with \(280.0\text{ kilograms}\) of nitrogen gas (\(\text{N}_2\), \(M = 28.013\text{ g/mol}\)) and \(75.0\text{ kilograms}\) of hydrogen gas (\(\text{H}_2\), \(M = 2.016\text{ g/mol}\)) to produce ammonia according to \(\text{N}_2 + 3\text{H}_2 \to 2\text{NH}_3\). The molar mass of ammonia is \(M = 17.031\text{ g/mol}\). Determine the limiting reactant, calculate the maximum theoretical yield of \(\text{NH}_3\) in kilograms, and determine the mass of excess reactant remaining.</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Convert input masses to moles:</strong></p>
          $$n_{\text{N}_2} = \frac{280,000\text{ g}}{28.013\text{ g/mol}} = 9,995.36\text{ moles}$$
          $$n_{\text{H}_2} = \frac{75,000\text{ g}}{2.016\text{ g/mol}} = 37,202.38\text{ moles}$$

          <p><strong>Step 2: Normalize by stoichiometric coefficients:</strong></p>
          $$\text{Ratio for N}_2 = \frac{9,995.36}{1} = 9,995.36$$
          $$\text{Ratio for H}_2 = \frac{37,202.38}{3} = 12,400.79$$
          <p>Because \(9,995.36 &lt; 12,400.79\), **Nitrogen Gas (\(\text{N}_2\)) is strictly the Limiting Reactant**, while Hydrogen is in excess.</p>

          <p><strong>Step 3: Calculate theoretical yield of ammonia (\(\text{NH}_3\)):</strong></p>
          $$n_{\text{NH}_3, \text{theor}} = n_{\text{N}_2} \times \left(\frac{2\text{ mol NH}_3}{1\text{ mol N}_2}\right) = 9,995.36 \times 2 = 19,990.72\text{ moles}$$
          $$m_{\text{NH}_3, \text{theor}} = 19,990.72\text{ mol} \times 17.031\text{ g/mol} = 340,462\text{ grams} \approx 340.46\text{ kg}$$

          <p><strong>Step 4: Determine leftover excess hydrogen:</strong></p>
          $$n_{\text{H}_2, \text{consumed}} = n_{\text{N}_2} \times 3 = 9,995.36 \times 3 = 29,986.08\text{ moles}$$
          $$n_{\text{H}_2, \text{remaining}} = 37,202.38 - 29,986.08 = 7,216.30\text{ moles}$$
          $$m_{\text{H}_2, \text{remaining}} = 7,216.30\text{ mol} \times 2.016\text{ g/mol} = 14,548\text{ grams} \approx 14.55\text{ kg}$$
          <p><strong>Engineering Result:</strong> The theoretical maximum ammonia output is \(340.46\text{ kg}\), with \(14.55\text{ kg}\) of unreacted hydrogen gas recycled back through the synthesis loop.</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Blast Furnace Smelting of Iron(III) Oxide</h3>
        <p><strong>Scenario:</strong> An industrial blast furnace charges \(500.0\text{ kg}\) of hematite ore containing iron(III) oxide (\(\text{Fe}_2\text{O}_3\), \(M = 159.69\text{ g/mol}\)) with \(250.0\text{ kg}\) of carbon monoxide (\(\text{CO}\), \(M = 28.01\text{ g/mol}\)) according to \(\text{Fe}_2\text{O}_3 + 3\text{CO} \to 2\text{Fe} + 3\text{CO}_2\). Calculate the theoretical yield of metallic iron (\(\text{Fe}\), \(M = 55.845\text{ g/mol}\)).</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Calculate moles of reactants:</strong></p>
          $$n_{\text{Fe}_2\text{O}_3} = \frac{500,000\text{ g}}{159.69\text{ g/mol}} = 3131.07\text{ moles}$$
          $$n_{\text{CO}} = \frac{250,000\text{ g}}{28.01\text{ g/mol}} = 8925.38\text{ moles}$$

          <p><strong>Step 2: Normalize by stoichiometric coefficients:</strong></p>
          $$\text{Ratio for Fe}_2\text{O}_3 = \frac{3131.07}{1} = 3131.07$$
          $$\text{Ratio for CO} = \frac{8925.38}{3} = 2975.13$$
          <p>Because \(2975.13 &lt; 3131.07\), **Carbon Monoxide (\(\text{CO}\)) is the Limiting Reactant**, while \(\text{Fe}_2\text{O}_3\) is in excess!</p>

          <p><strong>Step 3: Calculate theoretical yield of iron based on CO:</strong></p>
          $$n_{\text{Fe, theor}} = n_{\text{CO}} \times \left(\frac{2\text{ mol Fe}}{3\text{ mol CO}}\right) = 8925.38 \times \left(\frac{2}{3}\right) = 5950.25\text{ moles}$$
          $$m_{\text{Fe, theor}} = 5950.25\text{ mol} \times 55.845\text{ g/mol} = 332,292\text{ grams} \approx 332.29\text{ kg}$$
          <p><strong>Smelting Result:</strong> The maximum theoretical yield of metallic iron is \(332.29\text{ kg}\), limited by the available carbon monoxide reducing gas.</p>
        </div>
      </div>

      <h2>6. Frequently Asked Questions (Industrial Stoichiometry)</h2>
      <div class="faq-accordion">
        <details class="faq-item">
          <summary>Can the limiting reactant change if starting masses change slightly?</summary>
          <div class="faq-answer">
            <p>Yes. The identity of the limiting reactant depends strictly on the ratio of starting moles to stoichiometric coefficients, not starting mass. Because different molecules have vastly different molar masses (e.g., H2 = 2 g/mol vs Fe2O3 = 160 g/mol), a smaller starting mass in grams does not necessarily indicate the limiting reagent. For example, 10 g of H2 contains 5.0 moles, while 10 g of Fe2O3 contains only 0.063 moles.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>What is an equimolar mixture versus a stoichiometric mixture?</summary>
          <div class="faq-answer">
            <p>An equimolar mixture contains exactly equal numbers of moles of two substances (1:1 molar ratio, \(n_A = n_B\)). A stoichiometric mixture contains reactants in the exact proportions specified by the balanced chemical equation (\(n_A / a = n_B / b\)). These are identical only when the stoichiometric coefficients are both equal to 1.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>How does reactant purity affect theoretical yield calculations?</summary>
          <div class="faq-answer">
            <p>If starting chemicals are technical-grade rather than analytical-grade (e.g., 90% pure), the effective mass of active reactant must be multiplied by the purity fraction (\(m_{\text{active}} = m_{\text{crude}} \times \text{Purity}\%\)) before computing moles. Neglecting reactant purity produces an artificially inflated theoretical yield that distorts subsequent percent yield evaluations.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>What is the difference between theoretical yield and percent yield?</summary>
          <div class="faq-answer">
            <p>Theoretical yield is a mass or molar quantity (e.g., 50.0 grams) representing the maximum mathematical output possible. Percent yield is a percentage (% w/w) comparing the actual mass isolated in the real experiment to that theoretical maximum: \(\% Y = (\text{Actual} / \text{Theoretical}) \times 100\%\).</p>
          </div>
        </details>
      </div>

      <h2>7. Related Stoichiometric &amp; Reaction Calculators</h2>
      <p>Explore our integrated chemistry computation suite to solve reaction yields, molar quantities, and concentrations:</p>
      <div class="related-calculators" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-top: 1rem;">
        <a href="percent-yield-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Percent Yield Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Calculate reaction efficiency from actual and theoretical yield limits.</p>
        </a>
        <a href="moles-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Moles Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Convert between grams, moles ($n = m/M$), and Avogadro particle counts.</p>
        </a>
        <a href="percent-composition-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Percent Composition Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Determine elemental mass percentages (% w/w) in chemical formulas.</p>
        </a>
        <a href="molar-mass-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Molar Mass Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Calculate molecular weights and elemental proportions from chemical formulas.</p>
        </a>
      </div>
    </article>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-col">
        <h3>CalcHub</h3>
        <p>Your comprehensive engineering, mathematical, physical, and financial computational authority.</p>
      </div>
      <div class="footer-col">
        <h3>Calculators</h3>
        <ul>
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="math.html">Mathematics</a></li>
          <li><a href="converter.html">Unit Converters</a></li>
          <li><a href="engineering.html">Electrical &amp; Engineering</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h3>Chemical &amp; Water</h3>
        <ul>
          <li><a href="theoretical-yield-calculator.html">Theoretical Yield</a></li>
          <li><a href="percent-yield-calculator.html">Percent Yield</a></li>
          <li><a href="moles-calculator.html">Moles Calculator</a></li>
          <li><a href="molar-mass-calculator.html">Molar Mass Calculator</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 CalcHub. High-precision engineering formulas and calculators. All rights reserved.</p>
    </div>
  </footer>

  <script>
    (function() {
      // DOM Elements
      const presetSelect = document.getElementById('ty-preset');

      const r1Name = document.getElementById('ty-r1-name');
      const r1Coeff = document.getElementById('ty-r1-coeff');
      const r1Mw = document.getElementById('ty-r1-mw');
      const r1Mass = document.getElementById('ty-r1-mass');

      const r2Name = document.getElementById('ty-r2-name');
      const r2Coeff = document.getElementById('ty-r2-coeff');
      const r2Mw = document.getElementById('ty-r2-mw');
      const r2Mass = document.getElementById('ty-r2-mass');

      const prodName = document.getElementById('ty-prod-name');
      const prodCoeff = document.getElementById('ty-prod-coeff');
      const prodMw = document.getElementById('ty-prod-mw');

      const calcBtn = document.getElementById('ty-calc-btn');
      const resetBtn = document.getElementById('ty-reset-btn');

      // Outputs
      const primaryOut = document.getElementById('ty-primary-out');
      const statusOut = document.getElementById('ty-status-out');
      const limitingOut = document.getElementById('ty-limiting-out');
      const molesOut = document.getElementById('ty-moles-out');
      const excessMassOut = document.getElementById('ty-excess-mass-out');
      const convOut = document.getElementById('ty-conv-out');

      const PRESETS = {
        'water': {
          r1: { name: 'H₂', a: 2, mw: 2.016, mass: 10.0 },
          r2: { name: 'O₂', b: 1, mw: 31.999, mass: 64.0 },
          prod: { name: 'H₂O', c: 2, mw: 18.015 }
        },
        'ammonia': {
          r1: { name: 'N₂', a: 1, mw: 28.013, mass: 28.0 },
          r2: { name: 'H₂', b: 3, mw: 2.016, mass: 10.0 },
          prod: { name: 'NH₃', c: 2, mw: 17.031 }
        },
        'iron': {
          r1: { name: 'Fe₂O₃', a: 1, mw: 159.69, mass: 100.0 },
          r2: { name: 'CO', b: 3, mw: 28.01, mass: 60.0 },
          prod: { name: 'Fe', c: 2, mw: 55.845 }
        },
        'methane': {
          r1: { name: 'CH₄', a: 1, mw: 16.043, mass: 16.04 },
          r2: { name: 'O₂', b: 2, mw: 31.999, mass: 80.0 },
          prod: { name: 'CO₂', c: 1, mw: 44.01 }
        },
        'aspirin': {
          r1: { name: 'Salicylic Acid', a: 1, mw: 138.12, mass: 13.81 },
          r2: { name: 'Acetic Anhydride', b: 1, mw: 102.09, mass: 15.31 },
          prod: { name: 'Aspirin', c: 1, mw: 180.16 }
        }
      };

      function calculate() {
        const a = parseFloat(r1Coeff.value) || 1;
        const mwA = parseFloat(r1Mw.value) || 1;
        const massA = parseFloat(r1Mass.value) || 0;

        const b = parseFloat(r2Coeff.value) || 1;
        const mwB = parseFloat(r2Mw.value) || 1;
        const massB = parseFloat(r2Mass.value) || 0;

        const c = parseFloat(prodCoeff.value) || 1;
        const mwC = parseFloat(prodMw.value) || 1;

        if (massA <= 0 || massB <= 0 || mwA <= 0 || mwB <= 0 || mwC <= 0 || a <= 0 || b <= 0 || c <= 0) {
          primaryOut.textContent = "-- g";
          statusOut.textContent = "Please enter valid positive stoichiometric values.";
          return;
        }

        const molesA = massA / mwA;
        const molesB = massB / mwB;

        const ratioA = molesA / a;
        const ratioB = molesB / b;

        let isALimiting = (ratioA <= ratioB);
        let limitingMols = isALimiting ? molesA : molesB;
        let limitingCoeff = isALimiting ? a : b;
        let limitingName = isALimiting ? (r1Name.textContent || "Reactant A") : (r2Name.textContent || "Reactant B");
        let excessName = isALimiting ? (r2Name.textContent || "Reactant B") : (r1Name.textContent || "Reactant A");

        // Product moles
        const prodMoles = (limitingMols / limitingCoeff) * c;
        const prodTheorMass = prodMoles * mwC;

        // Excess remaining
        let excessConsumedMoles = 0;
        let excessInitialMoles = isALimiting ? molesB : molesA;
        let excessInitialMass = isALimiting ? massB : massA;
        let excessMw = isALimiting ? mwB : mwA;

        if (isALimiting) {
          excessConsumedMoles = molesA * (b / a);
        } else {
          excessConsumedMoles = molesB * (a / b);
        }

        const excessRemainingMoles = Math.max(0, excessInitialMoles - excessConsumedMoles);
        const excessRemainingMass = excessRemainingMoles * excessMw;
        const convPct = ((excessInitialMoles - excessRemainingMoles) / excessInitialMoles) * 100;

        // Render to UI
        primaryOut.textContent = prodTheorMass >= 1000 ? (prodTheorMass / 1000).toFixed(3) + " kg" : prodTheorMass.toFixed(2) + " g";
        statusOut.textContent = `Limiting Reactant: ${limitingName} (100% Consumed)`;
        limitingOut.textContent = limitingName;
        molesOut.textContent = prodMoles.toFixed(4) + " mol";
        excessMassOut.textContent = `${excessRemainingMass.toFixed(2)} g (${excessName})`;
        convOut.textContent = `${convPct.toFixed(1)}% of ${excessName} Used`;
      }

      presetSelect.addEventListener('change', function() {
        const val = this.value;
        if (PRESETS[val]) {
          const p = PRESETS[val];
          r1Name.textContent = p.r1.name;
          r1Coeff.value = p.r1.a;
          r1Mw.value = p.r1.mw;
          r1Mass.value = p.r1.mass;

          r2Name.textContent = p.r2.name;
          r2Coeff.value = p.r2.b;
          r2Mw.value = p.r2.mw;
          r2Mass.value = p.r2.mass;

          prodName.textContent = p.prod.name;
          prodCoeff.value = p.prod.c;
          prodMw.value = p.prod.mw;
          calculate();
        }
      });

      [r1Coeff, r1Mw, r1Mass, r2Coeff, r2Mw, r2Mass, prodCoeff, prodMw].forEach(el => {
        el.addEventListener('input', function() {
          presetSelect.value = 'custom';
          calculate();
        });
        el.addEventListener('change', calculate);
      });

      calcBtn.addEventListener('click', calculate);

      resetBtn.addEventListener('click', function() {
        presetSelect.value = 'water';
        const p = PRESETS['water'];
        r1Name.textContent = p.r1.name;
        r1Coeff.value = p.r1.a;
        r1Mw.value = p.r1.mw;
        r1Mass.value = p.r1.mass;

        r2Name.textContent = p.r2.name;
        r2Coeff.value = p.r2.b;
        r2Mw.value = p.r2.mw;
        r2Mass.value = p.r2.mass;

        prodName.textContent = p.prod.name;
        prodCoeff.value = p.prod.c;
        prodMw.value = p.prod.mw;
        calculate();
      });

      // Initial execution
      calculate();
    })();
  </script>
</body>
</html>
"""

# 8. ppm-calculator.html
HTML_PPM = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PPM Calculator - Parts Per Million, PPB &amp; mg/L Concentration Converter</title>
  <meta name="description" content="Convert parts per million (ppm), parts per billion (ppb), mass percent (% w/w), mg/L in water, and atmospheric gas ppm_v to mg/m³ with step-by-step proofs.">
  <link rel="canonical" href="https://calchub.org/ppm-calculator.html">
  <meta property="og:title" content="PPM Calculator - Parts Per Million &amp; mg/L Converter">
  <meta property="og:description" content="Free environmental &amp; chemistry PPM calculator. Convert mass to ppm, mg/L in aqueous solution, ppb, percent concentration, and air pollutant ppm_v.">
  <meta property="og:url" content="https://calchub.org/ppm-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="PPM Calculator - Environmental &amp; Water Analysis Tool">
  <meta name="twitter:description" content="Convert ppm to mg/L, ppb, and mass percent with EPA drinking water standards and atmospheric pollution benchmarks.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "PPM Calculator",
    "url": "https://calchub.org/ppm-calculator.html",
    "description": "Calculates parts per million (ppm), parts per billion (ppb), milligrams per liter (mg/L), and gas phase volume fractions (ppm_v).",
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
        "name": "What does parts per million (ppm) mean?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Parts per million (ppm) is a dimensionless ratio that expresses the concentration of a substance as one part solute per one million parts of total solution or mixture: ppm = (Mass of Solute / Total Mass of Solution) * 10^6. One ppm represents 1 milligram of solute per 1 kilogram of solution."
        }
      },
      {
        "@type": "Question",
        "name": "Is 1 ppm equal to 1 mg/L in water?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes, for dilute aqueous solutions at room temperature. Because pure water has a density of approximately 1.000 kg/L (1,000,000 mg/L), dissolving 1 milligram of solute in 1 liter of water produces 1 mg / 1,000,000 mg = 1 part per million (1 ppm = 1 mg/L)."
        }
      },
      {
        "@type": "Question",
        "name": "How do you convert percent (%) concentration to ppm?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "To convert percent concentration (% w/w) to ppm, multiply by 10,000: ppm = % * 10,000. For example, 1.0% equals 10,000 ppm, and 0.05% equals 500 ppm."
        }
      },
      {
        "@type": "Question",
        "name": "How is gas ppm_v converted to mg/m³ in air pollution?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "For gases at standard ambient temperature (25°C) and pressure (1 atm), the conversion is: Concentration (mg/m³) = [ppm_v * Molar Mass (g/mol)] / 24.45, where 24.45 is the molar volume of an ideal gas in liters at 25°C."
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
        <a href="math.html">Math &amp; Statistics</a>
        <a href="converter.html">Converters</a>
        <a href="engineering.html" class="active">Engineering</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="page-container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo;
      <a href="chemical.html">Chemical &amp; Water</a> &rsaquo;
      <span>PPM Calculator</span>
    </nav>

    <div class="page-header">
      <h1 class="page-title">PPM Calculator</h1>
      <p class="page-desc">Convert between parts per million (ppm), parts per billion (ppb), milligrams per liter (mg/L), mass percent (% w/w), and gas concentrations.</p>
    </div>

    <div class="calc-grid">
      <!-- Calculator Column -->
      <div class="calc-card">
        <div class="calc-header">
          <h2>Parts Per Million &amp; Concentration Solver</h2>
        </div>

        <!-- Mode Selection -->
        <div class="form-group">
          <label for="ppm-mode">Calculation Mode:</label>
          <select id="ppm-mode" class="form-control">
            <option value="mass-ratio" selected>From Solute Mass &amp; Solution Mass &rarr; PPM &amp; PPB</option>
            <option value="mgl-water">From mg/L in Water &rarr; PPM &amp; Percentage</option>
            <option value="percent-to-ppm">From Mass Percentage (% w/w) &rarr; PPM &amp; PPB</option>
            <option value="gas-ppm">Atmospheric Gas: ppm_v &harr; mg/m³ Converter</option>
          </select>
        </div>

        <!-- Environmental Presets -->
        <div class="form-group">
          <label for="ppm-preset">Environmental / Water Benchmark Preset:</label>
          <select id="ppm-preset" class="form-control">
            <option value="custom">-- Custom Concentration Values --</option>
            <option value="epa-lead">EPA Drinking Water Lead Action Limit (0.015 ppm / 15 ppb)</option>
            <option value="epa-arsenic">EPA Arsenic MCL in Drinking Water (0.010 ppm / 10 ppb)</option>
            <option value="tap-fluoride">Municipal Tap Water Fluoride Target (0.70 ppm)</option>
            <option value="chlorine-pool">Swimming Pool Free Chlorine Target (2.0 ppm)</option>
            <option value="co2-air">Atmospheric Carbon Dioxide Level (~425 ppm_v CO2)</option>
            <option value="co-osha">OSHA Workplace Carbon Monoxide Permissible Limit (50 ppm_v CO)</option>
            <option value="ocean-salinity">Ocean Seawater Salinity (35,000 ppm / 3.5% w/w)</option>
          </select>
        </div>

        <!-- Mode 1: Mass Ratio Panel -->
        <div id="ppm-mass-panel">
          <div class="form-row">
            <div class="form-group">
              <label for="ppm-solute-val">Solute Mass ($m_{\text{solute}}$):</label>
              <input type="number" id="ppm-solute-val" class="form-control" value="15.0" step="any" min="0.000001">
            </div>
            <div class="form-group">
              <label for="ppm-solute-unit">Solute Unit:</label>
              <select id="ppm-solute-unit" class="form-control">
                <option value="mg" selected>Milligrams (mg)</option>
                <option value="ug">Micrograms (&mu;g)</option>
                <option value="g">Grams (g)</option>
                <option value="kg">Kilograms (kg)</option>
              </select>
            </div>
          </div>
          <div class="form-row">
            <div class="form-group">
              <label for="ppm-sol-val">Total Solution Mass ($m_{\text{solution}}$):</label>
              <input type="number" id="ppm-sol-val" class="form-control" value="1.0" step="any" min="0.000001">
            </div>
            <div class="form-group">
              <label for="ppm-sol-unit">Solution Unit:</label>
              <select id="ppm-sol-unit" class="form-control">
                <option value="kg" selected>Kilograms (kg / Liters water)</option>
                <option value="g">Grams (g / mL water)</option>
                <option value="m3">Cubic Meters (m³ / metric tons)</option>
              </select>
            </div>
          </div>
        </div>

        <!-- Mode 2: mg/L Panel -->
        <div id="ppm-mgl-panel" style="display: none;">
          <div class="form-group">
            <label for="ppm-mgl-val">Aqueous Concentration in mg/L:</label>
            <input type="number" id="ppm-mgl-val" class="form-control" value="0.70" step="any" min="0.000001">
          </div>
        </div>

        <!-- Mode 3: Percent to PPM Panel -->
        <div id="ppm-pct-panel" style="display: none;">
          <div class="form-group">
            <label for="ppm-pct-val">Mass Percent (% w/w):</label>
            <input type="number" id="ppm-pct-val" class="form-control" value="0.05" step="any" min="0.000001" max="100.0">
          </div>
        </div>

        <!-- Mode 4: Gas PPM Panel -->
        <div id="ppm-gas-panel" style="display: none;">
          <div class="form-row">
            <div class="form-group">
              <label for="ppm-gas-ppmv">Gas Concentration (ppm_v):</label>
              <input type="number" id="ppm-gas-ppmv" class="form-control" value="50.0" step="any" min="0.0001">
            </div>
            <div class="form-group">
              <label for="ppm-gas-mw">Gas Molar Mass ($M$ in g/mol):</label>
              <input type="number" id="ppm-gas-mw" class="form-control" value="28.01" step="any" min="1.0">
            </div>
          </div>
          <div class="form-row">
            <div class="form-group">
              <label for="ppm-gas-temp">Temperature (°C):</label>
              <input type="number" id="ppm-gas-temp" class="form-control" value="25.0" step="any">
            </div>
            <div class="form-group">
              <label for="ppm-gas-press">Pressure (atm):</label>
              <input type="number" id="ppm-gas-press" class="form-control" value="1.0" step="any">
            </div>
          </div>
        </div>

        <div class="form-actions">
          <button type="button" id="ppm-calc-btn" class="btn btn-primary">Calculate Concentration</button>
          <button type="button" id="ppm-reset-btn" class="btn btn-secondary">Reset</button>
        </div>

        <!-- Output Hero and Cards -->
        <div id="ppm-results" class="results-container" style="margin-top: 1.5rem;">
          <div class="result-hero-card">
            <div class="result-label" style="font-size: 0.875rem; color: var(--text-muted, #64748b); text-transform: uppercase; font-weight: 600;">Parts Per Million (PPM)</div>
            <div id="ppm-primary-out" style="font-size: 2.25rem; font-weight: 800; color: var(--primary, #2563eb); margin: 0.25rem 0;">15.00 ppm</div>
            <div id="ppm-status-out" style="font-size: 1rem; color: var(--text-secondary, #475569); font-weight: 600;">15.00 mg/kg &bull; 15,000 ppb</div>
          </div>

          <div class="summary-metrics-grid">
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Parts Per Billion (PPB)</div>
              <div id="ppm-ppb-out" style="font-size: 1.15rem; font-weight: 700;">15,000 ppb</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Mass Percent (% w/w)</div>
              <div id="ppm-pct-out" style="font-size: 1.15rem; font-weight: 700;">0.0015%</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Aqueous Equivalent</div>
              <div id="ppm-aq-out" style="font-size: 1.15rem; font-weight: 700;">15.00 mg/L</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Parts Per Trillion (PPT)</div>
              <div id="ppm-ppt-out" style="font-size: 1.15rem; font-weight: 700;">15,000,000 ppt</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Reference Sidebar -->
      <aside class="sidebar-card">
        <h3>Environmental PPM Standards</h3>
        <ul style="font-size: 0.875rem; line-height: 1.6; margin-left: 1.25rem;">
          <li><strong>EPA Lead Action Limit:</strong><br>0.015 ppm (15 ppb) in drinking water</li>
          <li><strong>EPA Arsenic MCL:</strong><br>0.010 ppm (10 ppb)</li>
          <li><strong>EPA Nitrate MCL:</strong><br>10.0 ppm (10 mg/L as N)</li>
          <li><strong>Tap Water Fluoride:</strong><br>0.70 ppm target (CDC recommended)</li>
          <li><strong>Atmospheric CO₂:</strong><br>~425 ppm (0.0425% by volume)</li>
          <li><strong>OSHA Carbon Monoxide:</strong><br>50 ppm 8-hour TWA permissible limit</li>
        </ul>

        <h3 style="margin-top: 1.25rem;">Scale Interconversions</h3>
        <ul style="font-size: 0.875rem; line-height: 1.6; margin-left: 1.25rem;">
          <li>\(1\% = 10,000\text{ ppm}\)</li>
          <li>\(1\text{ ppm} = 1,000\text{ ppb} = 1\text{ mg/L}\)</li>
          <li>\(1\text{ ppb} = 1,000\text{ ppt} = 1\text{ }\mu\text{g/L}\)</li>
          <li>\(1\text{ ppm} = 0.0001\%\)</li>
        </ul>
      </aside>
    </div>

    <!-- Long-Form Informational Engineering Article (1,400+ Words) -->
    <article class="article-body">
      <h2>1. The Definition and Fundamental Mathematics of Parts Per Million (PPM)</h2>
      <p>Parts per million (conventionally abbreviated as **ppm**) is a dimensionless pseudo-unit of concentration used in environmental science, analytical chemistry, toxicology, and industrial process engineering to quantify ultra-trace quantities of a solute or contaminant dispersed within a larger solvent or matrix. Expressing concentrations of minute fractions in standard percentages often results in cumbersome decimals (e.g., \(0.000015\%\)); ppm provides an intuitive, readable alternative by scaling the dimensionless mass fraction to parts per \(10^6\) (one million).</p>
      <p>Formally, the mass-based concentration in parts per million is defined as:</p>
      $$\text{ppm} = \left(\frac{m_{\text{solute}}}{m_{\text{total mixture}}}\right) \times 10^6 = \left(\frac{m_{\text{solute}}}{m_{\text{solute}} + m_{\text{solvent}}}\right) \times 1,000,000$$
      <p>Where \(m_{\text{solute}}\) and \(m_{\text{total mixture}}\) are expressed in identical units of mass (e.g., milligrams of solute per million milligrams of solution). In dimensional terms, because \(1\text{ kilogram} = 1,000\text{ grams} = 1,000,000\text{ milligrams}\):</p>
      $$1\text{ ppm} = \frac{1\text{ milligram of solute}}{1\text{ kilogram of solution}} = 1\text{ mg/kg}$$
      <p>Similarly, for extreme ultra-trace analysis in semiconductor fabrication and forensic toxicology, concentration is extended to **parts per billion** (ppb, \(10^{-9}\)) and **parts per trillion** (ppt, \(10^{-12}\)):</p>
      $$\text{ppb} = \left(\frac{m_{\text{solute}}}{m_{\text{solution}}}\right) \times 10^9 = \text{ppm} \times 1,000 = \frac{1\text{ microgram}}{1\text{ kilogram}}$$
      $$\text{ppt} = \left(\frac{m_{\text{solute}}}{m_{\text{solution}}}\right) \times 10^{12} = \text{ppb} \times 1,000 = \frac{1\text{ nanogram}}{1\text{ kilogram}}$$

      <h2>2. Why 1 PPM Equals 1 mg/L in Aqueous Solutions</h2>
      <p>In environmental water testing, wastewater management, and municipal water treatment, analytical laboratories frequently treat **ppm** and **milligrams per liter (mg/L)** as interchangeable equivalents. The physical justification rests on the density of pure water:</p>
      <ul>
        <li>At standard conditions (\(20^\circ\text{C}\)), pure water has a volumetric density of \(\rho \approx 1.000\text{ g/mL} = 1.000\text{ kg/L}\).</li>
        <li>One liter of water therefore has a mass of exactly \(1.000\text{ kg} = 1,000,000\text{ milligrams}\).</li>
        <li>Dissolving \(1.0\text{ milligram}\) of a trace contaminant (such as lead or arsenic) into \(1.0\text{ liter}\) of water yields:
        $$\text{Concentration} = \frac{1\text{ mg solute}}{1\text{ L water}} = \frac{1\text{ mg solute}}{1,000,000\text{ mg water}} = 1\text{ part per million (ppm)}$$</li>
      </ul>
      <p>This equivalence holds with high accuracy (\(&gt;99.5\%\)) for dilute freshwater systems. However, for dense or saline matrices (such as ocean seawater with density \(\rho = 1.025\text{ kg/L}\), or concentrated industrial brines), 1 mg/L does NOT equal 1 ppm; specific gravity must be factored in:</p>
      $$\text{ppm (w/w)} = \frac{\text{Concentration (mg/L)}}{\text{Solution Density (kg/L)}}$$

      <h2>3. Atmospheric Air Pollution: Volume PPM (ppm_v) vs. mg/m³</h2>
      <p>In atmospheric chemistry, air quality monitoring (EPA NAAQS), and industrial workplace hygiene (OSHA), gas concentrations are expressed as **volume parts per million** (\(\text{ppm}_v\)):</p>
      $$\text{ppm}_v = \left(\frac{V_{\text{gas contaminant}}}{V_{\text{total air}}}\right) \times 10^6$$
      <p>By Avogadro's Law, volume fractions in an ideal gas mixture are directly identical to mole fractions (\(V_i / V_{\text{total}} = n_i / n_{\text{total}}\)). To convert volumetric gas concentration in \(\text{ppm}_v\) to mass concentration in milligrams per cubic meter (\(\text{mg/m}^3\)), engineers apply the Ideal Gas Law:</p>
      $$\text{Concentration (mg/m}^3\text{)} = \frac{\text{ppm}_v \times M \times P}{R \times T}$$
      <p>Under OSHA standard ambient temperature and pressure (\(25^\circ\text{C} = 298.15\text{ K}\), \(P = 1.000\text{ atm}\)), where the molar volume of an ideal gas equals \(24.45\text{ Liters/mol}\):</p>
      $$\text{mg/m}^3 = \frac{\text{ppm}_v \times M}{24.45} \iff \text{ppm}_v = \frac{\text{mg/m}^3 \times 24.45}{M}$$
      <p>Where \(M\) is the molecular weight of the contaminant gas in grams per mole.</p>

      <h2>4. Environmental and Industrial PPM Benchmark Table</h2>
      <p>The following engineering data table contrasts global environmental standards, water quality limits, and industrial thresholds across ppm, ppb, and mass percentages:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Substance / Scenario</th>
              <th>Matrix</th>
              <th>PPM Value</th>
              <th>PPB Value</th>
              <th>Mass Percent (% w/w)</th>
              <th>Regulatory Standard</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Lead (Pb)</td>
              <td>Drinking Water</td>
              <td>0.015 ppm</td>
              <td>15.0 ppb</td>
              <td>0.0000015%</td>
              <td>EPA Lead Action Level</td>
            </tr>
            <tr>
              <td>Arsenic (As)</td>
              <td>Drinking Water</td>
              <td>0.010 ppm</td>
              <td>10.0 ppb</td>
              <td>0.0000010%</td>
              <td>EPA Maximum Contaminant Level</td>
            </tr>
            <tr>
              <td>Mercury (Hg)</td>
              <td>Drinking Water</td>
              <td>0.002 ppm</td>
              <td>2.0 ppb</td>
              <td>0.0000002%</td>
              <td>EPA Primary Drinking Water Reg</td>
            </tr>
            <tr>
              <td>Fluoride (F⁻)</td>
              <td>Municipal Tap</td>
              <td>0.70 ppm</td>
              <td>700 ppb</td>
              <td>0.000070%</td>
              <td>US CDC Recommended Fluoridation</td>
            </tr>
            <tr>
              <td>Chlorine (Free Cl₂)</td>
              <td>Swimming Pools</td>
              <td>2.0 – 4.0 ppm</td>
              <td>2,000 – 4,000 ppb</td>
              <td>0.0002 – 0.0004%</td>
              <td>Public Health Sanitization Range</td>
            </tr>
            <tr>
              <td>Nitrate (NO₃⁻ as N)</td>
              <td>Groundwater</td>
              <td>10.0 ppm</td>
              <td>10,000 ppb</td>
              <td>0.0010%</td>
              <td>Blue Baby Syndrome Safety Cap</td>
            </tr>
            <tr>
              <td>Carbon Monoxide (CO)</td>
              <td>Workplace Air</td>
              <td>50 ppm_v</td>
              <td>50,000 ppb_v</td>
              <td>0.0050% (vol)</td>
              <td>OSHA 8-hour TWA PEL</td>
            </tr>
            <tr>
              <td>Carbon Dioxide (CO₂)</td>
              <td>Ambient Atmosphere</td>
              <td>~425 ppm_v</td>
              <td>425,000 ppb_v</td>
              <td>0.0425% (vol)</td>
              <td>Global Keeling Curve (Mauna Loa)</td>
            </tr>
            <tr>
              <td>Ocean Seawater Salts</td>
              <td>Marine Waters</td>
              <td>35,000 ppm</td>
              <td>35,000,000 ppb</td>
              <td>3.50%</td>
              <td>Standard Global Salinity (35 PSU)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>5. Step-by-Step Worked Environmental Case Studies</h2>

      <div class="worked-example-card">
        <h3>Case Study 1: Municipal Water Reservoir Chlorine Disinfection Dosing</h3>
        <p><strong>Scenario:</strong> A municipal water treatment facility pumps \(2.50\text{ million liters}\) (\(2,500\text{ m}^3\)) of raw reservoir water into a contact chamber. Treatment protocols mandate achieving a target residual free chlorine concentration of \(1.80\text{ ppm}\) (\(\text{mg/L}\)). If the plant uses commercial sodium hypochlorite solution (\(\text{NaOCl}\)) containing \(12.5\%\text{ w/w}\) available chlorine with a solution density of \(\rho = 1.20\text{ kg/L}\), calculate the mass of pure chlorine gas equivalent required and the volume of commercial bleach solution in liters.</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Calculate total mass of chlorine required:</strong></p>
          <p>Since \(1\text{ ppm} = 1\text{ mg/L}\):</p>
          $$m_{\text{pure Cl}_2} = 2,500,000\text{ L} \times 1.80\text{ mg/L} = 4,500,000\text{ mg} = 4,500.0\text{ grams} = 4.50\text{ kg}$$

          <p><strong>Step 2: Determine mass of \(12.5\%\) commercial bleach solution:</strong></p>
          $$m_{\text{bleach solution}} = \frac{4.50\text{ kg}}{0.125} = 36.00\text{ kilograms}$$

          <p><strong>Step 3: Calculate liquid volume of bleach required:</strong></p>
          $$V_{\text{bleach}} = \frac{\text{Mass}}{\text{Density}} = \frac{36.00\text{ kg}}{1.20\text{ kg/L}} = 30.00\text{ Liters}$$
          <p><strong>Dosing Protocol:</strong> The dosing pump must meter exactly \(30.0\text{ Liters}\) of \(12.5\%\) sodium hypochlorite into the \(2.50\text{-million liter}\) reservoir to establish a \(1.80\text{ ppm}\) sanitizing residual.</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Converting Workplace Carbon Monoxide Exposure from PPM to mg/m³</h3>
        <p><strong>Scenario:</strong> An industrial hygienist tests ambient air in an underground parking garage using a photoionization gas detector, logging a peak carbon monoxide (\(\text{CO}\)) concentration of \(35.0\text{ ppm}_v\). Ambient conditions are \(20.0^\circ\text{C}\) (\(293.15\text{ K}\)) and \(1.00\text{ atm}\). The molecular weight of carbon monoxide is \(M = 28.01\text{ g/mol}\). Compute the contaminant concentration in milligrams per cubic meter (\(\text{mg/m}^3\)).</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Calculate molar volume of ideal gas at \(20.0^\circ\text{C}\):</strong></p>
          $$V_m = \frac{R T}{P} = \frac{0.082057 \times 293.15}{1.000} = 24.055\text{ Liters/mol}$$

          <p><strong>Step 2: Apply the temperature-corrected gas conversion formula:</strong></p>
          $$\text{Concentration (mg/m}^3\text{)} = \frac{\text{ppm}_v \times M}{V_m} = \frac{35.0 \times 28.01\text{ g/mol}}{24.055\text{ L/mol}}$$
          $$\text{Concentration} = \frac{980.35}{24.055} = 40.75\text{ mg/m}^3$$
          <p><strong>Hygiene Interpretation:</strong> A reading of \(35.0\text{ ppm}_v\) \(\text{CO}\) corresponds to \(40.75\text{ mg/m}^3\) of particulate-free carbon monoxide in ambient air, remaining within the OSHA 8-hour permissible exposure limit of \(50\text{ ppm}_v\) (\(55\text{ mg/m}^3\)).</p>
        </div>
      </div>

      <h2>6. Frequently Asked Questions (Trace Analysis &amp; Water Testing)</h2>
      <div class="faq-accordion">
        <details class="faq-item">
          <summary>How many drops of water represent one part per million?</summary>
          <div class="faq-answer">
            <p>One milliliter of water contains approximately 20 standard drops. One liter contains 20,000 drops. A 50-liter domestic aquarium contains about 1,000,000 drops of water. Therefore, adding a single drop of food coloring into a 50-liter tank represents an exact real-world visualization of 1 part per million (1 ppm).</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>What is the difference between ppm and mg/kg in soil testing?</summary>
          <div class="faq-answer">
            <p>In soil and agricultural agronomy testing, ppm and mg/kg are strictly identical. Because 1 kilogram equals 1,000,000 milligrams, a pesticide residue level of 5 mg per kilogram of dry soil is precisely 5 ppm. Unlike water, soil density varies widely (bulk density ~1.3 to 1.6 g/cm³); thus, soil concentrations are always reported on a dry mass-to-mass basis (mg/kg = ppm) rather than volume.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>Can TDS meters accurately measure chemical ppm?</summary>
          <div class="faq-answer">
            <p>Handheld Total Dissolved Solids (TDS) meters measure electrical conductivity (EC, in microSiemens per centimeter, \(\mu\text{S/cm}\)) and multiply by an empirical conversion factor (typically 0.50 to 0.70) to estimate ppm. While convenient for monitoring reverse osmosis filters or hydroponics, they only detect conductive charged ions (\(\text{Na}^+\), \(\text{Ca}^{2+}\), \(\text{Cl}^-\)) and cannot detect non-conductive dissolved contaminants such as pesticides, bacteria, pharmaceutical residues, or neutral sugars.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>How do you dilute a 1,000 ppm stock standard to 10 ppm?</summary>
          <div class="faq-answer">
            <p>Using the standard dilution equation \(C_1 V_1 = C_2 V_2\): To prepare \(1000\text{ mL}\) of \(10\text{ ppm}\) calibration standard from a \(1,000\text{ ppm}\) stock solution: \(V_1 = (10\text{ ppm} \times 1000\text{ mL}) / 1000\text{ ppm} = 10.0\text{ mL}\). Pipette exactly \(10.0\text{ mL}\) of stock standard into a \(1000\text{-mL}\) volumetric flask and dilute with deionized water to the line.</p>
          </div>
        </details>
      </div>

      <h2>7. Related Environmental &amp; Chemical Calculators</h2>
      <p>Explore our integrated directory of chemical tools to solve dilutions, mass percentages, and molar concentrations:</p>
      <div class="related-calculators" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-top: 1rem;">
        <a href="mass-percent-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Mass Percent Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Determine solution weight concentration (% w/w) and solute/solvent mass ratios.</p>
        </a>
        <a href="dilution-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Dilution Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Solve $C_1 V_1 = C_2 V_2$ for laboratory serial dilutions and buffer compounding.</p>
        </a>
        <a href="molarity-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Molarity Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Compute volumetric solution concentration ($M = \text{mol/L}$) in moles per liter.</p>
        </a>
        <a href="specific-gravity-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Specific Gravity Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Convert hydrometer °API, Baumé, and Brix to relative solution density.</p>
        </a>
      </div>
    </article>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-col">
        <h3>CalcHub</h3>
        <p>Your comprehensive engineering, mathematical, physical, and financial computational authority.</p>
      </div>
      <div class="footer-col">
        <h3>Calculators</h3>
        <ul>
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="math.html">Mathematics</a></li>
          <li><a href="converter.html">Unit Converters</a></li>
          <li><a href="engineering.html">Electrical &amp; Engineering</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h3>Chemical &amp; Water</h3>
        <ul>
          <li><a href="ppm-calculator.html">PPM Calculator</a></li>
          <li><a href="mass-percent-calculator.html">Mass Percent</a></li>
          <li><a href="dilution-calculator.html">Dilution (C1V1 = C2V2)</a></li>
          <li><a href="density-calculator.html">Density &amp; Specific Gravity</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 CalcHub. High-precision engineering formulas and calculators. All rights reserved.</p>
    </div>
  </footer>

  <script>
    (function() {
      // DOM Elements
      const modeSelect = document.getElementById('ppm-mode');
      const presetSelect = document.getElementById('ppm-preset');

      const massPanel = document.getElementById('ppm-mass-panel');
      const mglPanel = document.getElementById('ppm-mgl-panel');
      const pctPanel = document.getElementById('ppm-pct-panel');
      const gasPanel = document.getElementById('ppm-gas-panel');

      const soluteValInput = document.getElementById('ppm-solute-val');
      const soluteUnitSelect = document.getElementById('ppm-solute-unit');
      const solValInput = document.getElementById('ppm-sol-val');
      const solUnitSelect = document.getElementById('ppm-sol-unit');

      const mglValInput = document.getElementById('ppm-mgl-val');
      const pctValInput = document.getElementById('ppm-pct-val');

      const gasPpmvInput = document.getElementById('ppm-gas-ppmv');
      const gasMwInput = document.getElementById('ppm-gas-mw');
      const gasTempInput = document.getElementById('ppm-gas-temp');
      const gasPressInput = document.getElementById('ppm-gas-press');

      const calcBtn = document.getElementById('ppm-calc-btn');
      const resetBtn = document.getElementById('ppm-reset-btn');

      // Outputs
      const primaryOut = document.getElementById('ppm-primary-out');
      const statusOut = document.getElementById('ppm-status-out');
      const ppbOut = document.getElementById('ppm-ppb-out');
      const pctOut = document.getElementById('ppm-pct-out');
      const aqOut = document.getElementById('ppm-aq-out');
      const pptOut = document.getElementById('ppm-ppt-out');

      const PRESETS = {
        'epa-lead': { mode: 'mass-ratio', solute: 15.0, sUnit: 'ug', sol: 1.0, solUnit: 'kg' },
        'epa-arsenic': { mode: 'mass-ratio', solute: 10.0, sUnit: 'ug', sol: 1.0, solUnit: 'kg' },
        'tap-fluoride': { mode: 'mgl-water', mgl: 0.70 },
        'chlorine-pool': { mode: 'mgl-water', mgl: 2.0 },
        'co2-air': { mode: 'gas-ppm', ppmv: 425.0, mw: 44.01, temp: 25.0, press: 1.0 },
        'co-osha': { mode: 'gas-ppm', ppmv: 50.0, mw: 28.01, temp: 25.0, press: 1.0 },
        'ocean-salinity': { mode: 'percent-to-ppm', pct: 3.5 }
      };

      const SOLUTE_TO_MG = {
        'mg': 1.0,
        'ug': 0.001,
        'g': 1000.0,
        'kg': 1000000.0
      };

      const SOLUTION_TO_KG = {
        'kg': 1.0,
        'g': 0.001,
        'm3': 1000.0
      };

      function updatePanelVisibility() {
        const m = modeSelect.value;
        massPanel.style.display = m === 'mass-ratio' ? 'block' : 'none';
        mglPanel.style.display = m === 'mgl-water' ? 'block' : 'none';
        pctPanel.style.display = m === 'percent-to-ppm' ? 'block' : 'none';
        gasPanel.style.display = m === 'gas-ppm' ? 'block' : 'none';
      }

      function calculate() {
        const mode = modeSelect.value;
        let ppm = 0;

        if (mode === 'mass-ratio') {
          const rawSolute = parseFloat(soluteValInput.value) || 0;
          const soluteMg = rawSolute * (SOLUTE_TO_MG[soluteUnitSelect.value] || 1.0);

          const rawSol = parseFloat(solValInput.value) || 0;
          const solKg = rawSol * (SOLUTION_TO_KG[solUnitSelect.value] || 1.0);

          if (soluteMg <= 0 || solKg <= 0) {
            primaryOut.textContent = "-- ppm";
            statusOut.textContent = "Please enter positive mass values.";
            return;
          }

          ppm = soluteMg / solKg; // 1 mg / 1 kg = 1 ppm
        } else if (mode === 'mgl-water') {
          const mgl = parseFloat(mglValInput.value) || 0;
          if (mgl <= 0) {
            primaryOut.textContent = "-- ppm";
            statusOut.textContent = "Please enter positive mg/L value.";
            return;
          }
          ppm = mgl;
        } else if (mode === 'percent-to-ppm') {
          const pct = parseFloat(pctValInput.value) || 0;
          if (pct <= 0) {
            primaryOut.textContent = "-- ppm";
            statusOut.textContent = "Please enter positive percentage.";
            return;
          }
          ppm = pct * 10000;
        } else if (mode === 'gas-ppm') {
          const ppmv = parseFloat(gasPpmvInput.value) || 0;
          const mw = parseFloat(gasMwInput.value) || 28.01;
          const tempC = parseFloat(gasTempInput.value) || 25.0;
          const pressAtm = parseFloat(gasPressInput.value) || 1.0;

          if (ppmv <= 0 || mw <= 0 || pressAtm <= 0) {
            primaryOut.textContent = "-- ppm";
            statusOut.textContent = "Please enter positive gas values.";
            return;
          }

          ppm = ppmv;
          // Calculate mg/m3
          const tempK = tempC + 273.15;
          const vm = (0.082057 * tempK) / pressAtm;
          const mgM3 = (ppmv * mw) / vm;

          primaryOut.textContent = ppm.toFixed(2) + " ppm_v";
          statusOut.textContent = `${mgM3.toFixed(2)} mg/m³ in ambient air at ${tempC}°C, ${pressAtm} atm`;
          ppbOut.textContent = (ppm * 1000).toLocaleString('en-US', { maximumFractionDigits: 1 }) + " ppb_v";
          pctOut.textContent = (ppm / 10000).toFixed(6) + "% (vol)";
          aqOut.textContent = `${mgM3.toFixed(2)} mg/m³`;
          pptOut.textContent = (ppm * 1000000).toLocaleString('en-US', { maximumFractionDigits: 0 }) + " ppt_v";
          return;
        }

        const ppb = ppm * 1000;
        const ppt = ppm * 1000000;
        const pct = ppm / 10000;
        const mgl = ppm;

        // Render to UI
        primaryOut.textContent = ppm >= 1000 ? ppm.toLocaleString('en-US', { maximumFractionDigits: 2 }) + " ppm" : ppm.toFixed(4) + " ppm";
        statusOut.textContent = `${mgl.toFixed(4)} mg/L (aqueous) \u2022 ${ppb.toLocaleString('en-US', { maximumFractionDigits: 1 })} ppb`;
        ppbOut.textContent = ppb.toLocaleString('en-US', { maximumFractionDigits: 2 }) + " ppb";
        pctOut.textContent = pct >= 0.0001 ? pct.toFixed(4) + "%" : pct.toExponential(4) + "%";
        aqOut.textContent = mgl >= 1000 ? (mgl / 1000).toFixed(3) + " g/L" : mgl.toFixed(4) + " mg/L";
        pptOut.textContent = ppt >= 1e9 ? ppt.toExponential(3) + " ppt" : ppt.toLocaleString('en-US', { maximumFractionDigits: 0 }) + " ppt";
      }

      presetSelect.addEventListener('change', function() {
        const val = this.value;
        if (PRESETS[val]) {
          const p = PRESETS[val];
          modeSelect.value = p.mode;
          updatePanelVisibility();

          if (p.mode === 'mass-ratio') {
            soluteValInput.value = p.solute;
            soluteUnitSelect.value = p.sUnit;
            solValInput.value = p.sol;
            solUnitSelect.value = p.solUnit;
          } else if (p.mode === 'mgl-water') {
            mglValInput.value = p.mgl;
          } else if (p.mode === 'percent-to-ppm') {
            pctValInput.value = p.pct;
          } else if (p.mode === 'gas-ppm') {
            gasPpmvInput.value = p.ppmv;
            gasMwInput.value = p.mw;
            gasTempInput.value = p.temp;
            gasPressInput.value = p.press;
          }
          calculate();
        }
      });

      modeSelect.addEventListener('change', function() {
        updatePanelVisibility();
        calculate();
      });

      [soluteValInput, soluteUnitSelect, solValInput, solUnitSelect, mglValInput, pctValInput, gasPpmvInput, gasMwInput, gasTempInput, gasPressInput].forEach(el => {
        el.addEventListener('input', function() {
          presetSelect.value = 'custom';
          calculate();
        });
        el.addEventListener('change', calculate);
      });

      calcBtn.addEventListener('click', calculate);

      resetBtn.addEventListener('click', function() {
        modeSelect.value = 'mass-ratio';
        presetSelect.value = 'epa-lead';
        soluteValInput.value = '15.0';
        soluteUnitSelect.value = 'ug';
        solValInput.value = '1.0';
        solUnitSelect.value = 'kg';
        updatePanelVisibility();
        calculate();
      });

      // Initial execution
      updatePanelVisibility();
      calculate();
    })();
  </script>
</body>
</html>
"""

def generate_files():
    p1 = os.path.join(BASE_DIR, "theoretical-yield-calculator.html")
    with open(p1, "w", encoding="utf-8") as f:
        f.write(HTML_THEOR_YIELD.strip() + "\n")
    print(f"Generated: {p1}")

    p2 = os.path.join(BASE_DIR, "ppm-calculator.html")
    with open(p2, "w", encoding="utf-8") as f:
        f.write(HTML_PPM.strip() + "\n")
    print(f"Generated: {p2}")

if __name__ == "__main__":
    generate_files()
