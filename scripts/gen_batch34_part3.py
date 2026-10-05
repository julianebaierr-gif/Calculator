# -*- coding: utf-8 -*-
"""
Generator for Batch 34 - Part 3:
5. percent-composition-calculator.html
6. percent-yield-calculator.html
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 5. percent-composition-calculator.html
HTML_PERCENT_COMP = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Percent Composition Calculator - Elemental Mass Percentage in Compounds</title>
  <meta name="description" content="Calculate elemental percent composition by mass, molecular formula weights, empirical formulas, and combustion analysis with step-by-step chemistry proofs.">
  <link rel="canonical" href="https://calchub.org/percent-composition-calculator.html">
  <meta property="og:title" content="Percent Composition Calculator - Elemental Mass % Solver">
  <meta property="og:description" content="Free chemistry percent composition calculator. Compute elemental mass percentages (% E = n * M_E / M_total * 100%), empirical formulas, and molecular weights.">
  <meta property="og:url" content="https://calchub.org/percent-composition-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Percent Composition Calculator - Chemical Formula Analysis">
  <meta name="twitter:description" content="Determine mass percentages of elements in chemical formulas with empirical and molecular analysis case studies.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Percent Composition Calculator",
    "url": "https://calchub.org/percent-composition-calculator.html",
    "description": "Calculates the mass percent composition of elements in chemical compounds, total formula weights, and empirical formula proportions.",
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
        "name": "What is the formula for percent composition by mass?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The percent composition of an element in a chemical compound is calculated as: % Composition = (n * Molar Mass of Element / Total Molar Mass of Compound) * 100%, where n is the number of atoms of that element in one formula unit or molecule."
        }
      },
      {
        "@type": "Question",
        "name": "How do you find the empirical formula from percent composition?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "To determine an empirical formula: (1) Assume a 100-gram sample, converting each element's percentage directly into grams; (2) Convert grams to moles by dividing by each element's atomic mass; (3) Divide all molar amounts by the smallest calculated mole value to obtain relative molar ratios; (4) If non-integers result, multiply by the smallest common factor to obtain the simplest whole-number ratio."
        }
      },
      {
        "@type": "Question",
        "name": "What is the difference between an empirical formula and a molecular formula?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "An empirical formula represents the simplest whole-number ratio of atoms in a compound (e.g., CH2O for glucose), whereas a molecular formula gives the exact actual number of atoms of each element in a single discrete molecule (e.g., C6H12O6 for glucose). The molecular formula is always an integer multiple (n) of the empirical formula."
        }
      },
      {
        "@type": "Question",
        "name": "Why must the sum of all percent compositions equal 100%?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "By the Law of Conservation of Mass and the Law of Definite Proportions (Proust's Law), the total mass of any chemical compound is precisely the sum of the masses of its constituent elements. Therefore, the sum of all individual elemental mass percentages in a pure compound must equal exactly 100% (within minor rounding discrepancies)."
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
      <span>Percent Composition Calculator</span>
    </nav>

    <div class="page-header">
      <h1 class="page-title">Percent Composition Calculator</h1>
      <p class="page-desc">Determine elemental mass percentages (% w/w) in chemical formulas, molecular weights, and empirical formula ratios with step-by-step breakdowns.</p>
    </div>

    <div class="calc-grid">
      <!-- Calculator Column -->
      <div class="calc-card">
        <div class="calc-header">
          <h2>Elemental Mass Percentage Solver</h2>
        </div>

        <!-- Compound Presets -->
        <div class="form-group">
          <label for="pc-preset">Common Chemical Compound Preset:</label>
          <select id="pc-preset" class="form-control">
            <option value="custom">-- Custom Chemical Compound --</option>
            <option value="water" selected>Water (H2O: H = 11.19%, O = 88.81%)</option>
            <option value="glucose">Glucose (C6H12O6: C = 40.00%, H = 6.71%, O = 53.29%)</option>
            <option value="co2">Carbon Dioxide (CO2: C = 27.29%, O = 72.71%)</option>
            <option value="ethanol">Ethanol (C2H6O: C = 52.14%, H = 13.13%, O = 34.73%)</option>
            <option value="caffeine">Caffeine (C8H10N4O2: C = 49.48%, H = 5.19%, N = 28.85%, O = 16.48%)</option>
            <option value="paracetamol">Acetaminophen / Paracetamol (C8H9NO2)</option>
            <option value="caco3">Calcium Carbonate (CaCO3: Ca = 40.04%, C = 12.00%, O = 47.96%)</option>
            <option value="h2so4">Sulfuric Acid (H2SO4: H = 2.06%, S = 32.69%, O = 65.25%)</option>
            <option value="aspirin">Aspirin / Acetylsalicylic Acid (C9H8O4)</option>
          </select>
        </div>

        <!-- Dynamic Element Rows Container -->
        <div id="pc-elements-container">
          <div style="font-size: 0.875rem; font-weight: 600; color: var(--text-muted, #64748b); margin-bottom: 0.5rem; text-transform: uppercase;">Elements in Compound:</div>
          <!-- Rows will be populated via JS -->
        </div>

        <div style="margin-top: 0.75rem; display: flex; gap: 0.5rem;">
          <button type="button" id="pc-add-element-btn" class="btn btn-secondary" style="font-size: 0.85rem; padding: 0.4rem 0.8rem;">+ Add Element</button>
        </div>

        <div class="form-actions" style="margin-top: 1.25rem;">
          <button type="button" id="pc-calc-btn" class="btn btn-primary">Calculate Percent Composition</button>
          <button type="button" id="pc-reset-btn" class="btn btn-secondary">Reset</button>
        </div>

        <!-- Output Cards -->
        <div id="pc-results" class="results-container" style="margin-top: 1.5rem;">
          <div class="result-hero-card">
            <div class="result-label" style="font-size: 0.875rem; color: var(--text-muted, #64748b); text-transform: uppercase; font-weight: 600;">Total Molecular Weight</div>
            <div id="pc-mw-out" style="font-size: 2.25rem; font-weight: 800; color: var(--primary, #2563eb); margin: 0.25rem 0;">18.015 g/mol</div>
            <div id="pc-summary-out" style="font-size: 1rem; color: var(--text-secondary, #475569); font-weight: 600;">2 Elements &bull; 3 Total Atoms</div>
          </div>

          <!-- Breakdown Table -->
          <div class="table-responsive" style="margin-top: 1rem;">
            <table class="data-table" id="pc-breakdown-table" style="font-size: 0.9rem;">
              <thead>
                <tr>
                  <th>Element</th>
                  <th>Subscript (\(n\))</th>
                  <th>Atomic Mass (\(\text{g/mol}\))</th>
                  <th>Total Mass (\(\text{g/mol}\))</th>
                  <th>Percent by Mass</th>
                </tr>
              </thead>
              <tbody id="pc-breakdown-body">
                <!-- Dynamically generated rows -->
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Quick Reference Sidebar -->
      <aside class="sidebar-card">
        <h3>Standard Atomic Weights (IUPAC)</h3>
        <ul style="font-size: 0.875rem; line-height: 1.6; margin-left: 1.25rem;">
          <li><strong>Hydrogen (H):</strong> 1.008 g/mol</li>
          <li><strong>Carbon (C):</strong> 12.011 g/mol</li>
          <li><strong>Nitrogen (N):</strong> 14.007 g/mol</li>
          <li><strong>Oxygen (O):</strong> 15.999 g/mol</li>
          <li><strong>Sodium (Na):</strong> 22.990 g/mol</li>
          <li><strong>Magnesium (Mg):</strong> 24.305 g/mol</li>
          <li><strong>Phosphorus (P):</strong> 30.974 g/mol</li>
          <li><strong>Sulfur (S):</strong> 32.065 g/mol</li>
          <li><strong>Chlorine (Cl):</strong> 35.453 g/mol</li>
          <li><strong>Potassium (K):</strong> 39.098 g/mol</li>
          <li><strong>Calcium (Ca):</strong> 40.078 g/mol</li>
          <li><strong>Iron (Fe):</strong> 55.845 g/mol</li>
        </ul>

        <h3 style="margin-top: 1.25rem;">Key Formula</h3>
        <ul style="font-size: 0.875rem; line-height: 1.6; margin-left: 1.25rem;">
          <li>\(\% E = \frac{n \times M_E}{M_{\text{compound}}} \times 100\%\)</li>
          <li>\(\sum \% E_i = 100.0\%\)</li>
        </ul>
      </aside>
    </div>

    <!-- Long-Form Informational Engineering Article (1,400+ Words) -->
    <article class="article-body">
      <h2>1. The Fundamental Chemical Principles of Percent Composition</h2>
      <p>The percent composition by mass of a chemical compound defines the relative proportion of each constituent chemical element present within the substance, expressed as a percentage of the compound's total molecular weight or formula mass. In analytical chemistry, materials science, and synthetic organic synthesis, determining elemental percent composition is the foundational step for verifying compound purity, establishing empirical formulas, and characterizing novel synthesized pharmaceuticals.</p>
      <p>The mathematical equation for the mass percentage of any chemical element \(E\) in a pure compound is:</p>
      $$\% E = \left(\frac{n_E \times M_E}{M_{\text{compound}}}\right) \times 100\%$$
      <p>Where:</p>
      <ul>
        <li><strong>\(n_E\):</strong> The stoichiometric subscript representing the number of atoms of element \(E\) contained in one discrete molecular formula unit.</li>
        <li><strong>\(M_E\):</strong> The standard atomic weight (molar mass) of element \(E\) in grams per mole (\(\text{g/mol}\)), grounded in IUPAC standard atomic weights.</li>
        <li><strong>\(M_{\text{compound}}\):</strong> The aggregate molar mass (molecular weight) of the chemical compound, computed by summing the atomic weights of all constituent atoms:
        $$M_{\text{compound}} = \sum_{i=1}^k (n_i \times M_i)$$</li>
      </ul>
      <p>By the Law of Conservation of Mass and the Law of Definite Proportions (formulated by French chemist Joseph Proust in 1799), every pure chemical compound always contains its constituent elements in strictly fixed, invariant mass ratios, regardless of the method of synthesis or geographical origin. Consequently, the sum of the individual elemental mass percentages must sum precisely to unity (100%):</p>
      $$\sum_{i=1}^k \% E_i = 100.00\%$$

      <h2>2. Empirical Formulas vs. Molecular Formulas</h2>
      <p>A crucial distinction in chemical analysis exists between empirical and molecular formulas:</p>
      <ul>
        <li><strong>Empirical Formula:</strong> The simplest integer ratio of elements present in a compound. For instance, the empirical formula of both acetylene (\(\text{C}_2\text{H}_2\)) and benzene (\(\text{C}_6\text{H}_6\)) is \(\text{CH}\), because both contain carbon and hydrogen in a \(1:1\) atomic ratio, corresponding to \(92.26\%\text{ C}\) and \(7.74\%\text{ H}\) by mass.</li>
        <li><strong>Molecular Formula:</strong> The exact actual number of atoms of each element present in a single discrete molecule. The molecular formula of benzene is \(\text{C}_6\text{H}_6\), while for glucose it is \(\text{C}_6\text{H}_{12}\text{O}_6\) (whose empirical formula is \(\text{CH}_2\text{O}\)).</li>
      </ul>
      <p>The integer scaling factor \(n_{\text{factor}}\) between the empirical formula and molecular formula is determined by dividing the experimentally measured molecular molar mass (e.g., via mass spectrometry) by the empirical formula weight:</p>
      $$n_{\text{factor}} = \frac{M_{\text{molecular (measured)}}}{M_{\text{empirical}}} \implies \text{Molecular Formula} = (\text{Empirical Formula})_{n_{\text{factor}}}$$

      <h2>3. Combustion Analysis: From Experimental Combustion to Percent Composition</h2>
      <p>For organic compounds composed primarily of carbon, hydrogen, nitrogen, and oxygen, analytical laboratories determine elemental percentages using instrumental **combustion elemental analysis** (CHN analysis). In this method, a precisely weighed sample (\(m_{\text{sample}}\)) is combusted in pure oxygen at temperatures exceeding \(1,000^\circ\text{C}\):</p>
      $$\text{C}_x\text{H}_y\text{O}_z\text{N}_w + \text{excess O}_2 \longrightarrow x\text{ CO}_2 + \frac{y}{2}\text{ H}_2\text{O} + \frac{w}{2}\text{ N}_2$$
      <p>The combustion products are captured and weighed selectively:</p>
      <ol>
        <li><strong>Carbon Determination:</strong> All carbon in the sample is converted into carbon dioxide (\(\text{CO}_2\), \(M = 44.01\text{ g/mol}\)). The mass of carbon in the original sample is:
        $$m_{\text{C}} = m_{\text{CO}_2} \times \left(\frac{12.011}{44.010}\right) \implies \% \text{C} = \left(\frac{m_{\text{C}}}{m_{\text{sample}}}\right) \times 100\%$$</li>
        <li><strong>Hydrogen Determination:</strong> All hydrogen is trapped as water vapor (\(\text{H}_2\text{O}\), \(M = 18.015\text{ g/mol}\)):
        $$m_{\text{H}} = m_{\text{H}_2\text{O}} \times \left(\frac{2 \times 1.008}{18.015}\right) \implies \% \text{H} = \left(\frac{m_{\text{H}}}{m_{\text{sample}}}\right) \times 100\%$$</li>
        <li><strong>Oxygen Determination (by Difference):</strong> Because oxygen cannot be measured directly due to the combustion gas atmosphere, its mass percentage is determined by subtracting all other quantified elements from 100%:
        $$\% \text{O} = 100.00\% - (\% \text{C} + \% \text{H} + \% \text{N})$$</li>
      </ol>

      <h2>4. Elemental Percent Composition Benchmark Table</h2>
      <p>The following engineering reference table details molecular formulas, molecular weights, and individual elemental mass percentages across common industrial compounds, fuels, and biological molecules:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Compound Name</th>
              <th>Molecular Formula</th>
              <th>Molar Mass (\(M\))</th>
              <th>Primary Element %</th>
              <th>Secondary Element %</th>
              <th>Other Elements %</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Water</td>
              <td>H₂O</td>
              <td>18.015 g/mol</td>
              <td>O: 88.79%</td>
              <td>H: 11.21%</td>
              <td>&mdash;</td>
            </tr>
            <tr>
              <td>Methane</td>
              <td>CH₄</td>
              <td>16.043 g/mol</td>
              <td>C: 74.87%</td>
              <td>H: 25.13%</td>
              <td>&mdash;</td>
            </tr>
            <tr>
              <td>Carbon Dioxide</td>
              <td>CO₂</td>
              <td>44.010 g/mol</td>
              <td>O: 72.71%</td>
              <td>C: 27.29%</td>
              <td>&mdash;</td>
            </tr>
            <tr>
              <td>Ethanol</td>
              <td>C₂H₆O</td>
              <td>46.068 g/mol</td>
              <td>C: 52.14%</td>
              <td>O: 34.73%</td>
              <td>H: 13.13%</td>
            </tr>
            <tr>
              <td>Glucose (Dextrose)</td>
              <td>C₆H₁₂O₆</td>
              <td>180.156 g/mol</td>
              <td>O: 53.29%</td>
              <td>C: 40.00%</td>
              <td>H: 6.71%</td>
            </tr>
            <tr>
              <td>Caffeine</td>
              <td>C₈H₁₀N₄O₂</td>
              <td>194.191 g/mol</td>
              <td>C: 49.48%</td>
              <td>N: 28.85%</td>
              <td>O: 16.48%, H: 5.19%</td>
            </tr>
            <tr>
              <td>Aspirin</td>
              <td>C₉H₈O₄</td>
              <td>180.157 g/mol</td>
              <td>C: 60.00%</td>
              <td>O: 35.52%</td>
              <td>H: 4.48%</td>
            </tr>
            <tr>
              <td>Acetaminophen</td>
              <td>C₈H₉NO₂</td>
              <td>151.163 g/mol</td>
              <td>C: 63.56%</td>
              <td>O: 21.17%</td>
              <td>N: 9.27%, H: 6.00%</td>
            </tr>
            <tr>
              <td>Sulfuric Acid</td>
              <td>H₂SO₄</td>
              <td>98.079 g/mol</td>
              <td>O: 65.25%</td>
              <td>S: 32.69%</td>
              <td>H: 2.06%</td>
            </tr>
            <tr>
              <td>Calcium Carbonate</td>
              <td>CaCO₃</td>
              <td>100.087 g/mol</td>
              <td>O: 47.96%</td>
              <td>Ca: 40.04%</td>
              <td>C: 12.00%</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>5. Step-by-Step Worked Chemical Case Studies</h2>

      <div class="worked-example-card">
        <h3>Case Study 1: Calculating Elemental Percent Composition of Caffeine (C₈H₁₀N₄O₂)</h3>
        <p><strong>Scenario:</strong> Analytical chemists quality-testing synthetic caffeine (\(\text{C}_8\text{H}_{10}\text{N}_4\text{O}_2\)) need to establish theoretical elemental mass percentages to benchmark combustion CHN microanalysis. Calculate the molecular formula weight and the exact mass percentage of Carbon, Hydrogen, Nitrogen, and Oxygen.</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Identify standard atomic weights:</strong></p>
          <ul>
            <li>Carbon (C): \(12.011\text{ g/mol}\), subscript \(n = 8\)</li>
            <li>Hydrogen (H): \(1.008\text{ g/mol}\), subscript \(n = 10\)</li>
            <li>Nitrogen (N): \(14.007\text{ g/mol}\), subscript \(n = 4\)</li>
            <li>Oxygen (O): \(15.999\text{ g/mol}\), subscript \(n = 2\)</li>
          </ul>

          <p><strong>Step 2: Calculate total mass contributed by each element:</strong></p>
          $$m_{\text{C}} = 8 \times 12.011 = 96.088\text{ g/mol}$$
          $$m_{\text{H}} = 10 \times 1.008 = 10.080\text{ g/mol}$$
          $$m_{\text{N}} = 4 \times 14.007 = 56.028\text{ g/mol}$$
          $$m_{\text{O}} = 2 \times 15.999 = 31.998\text{ g/mol}$$

          <p><strong>Step 3: Calculate total molecular weight:</strong></p>
          $$M_{\text{caffeine}} = 96.088 + 10.080 + 56.028 + 31.998 = 194.194\text{ g/mol}$$

          <p><strong>Step 4: Compute individual percent compositions:</strong></p>
          $$\% \text{C} = \left(\frac{96.088}{194.194}\right) \times 100\% = 49.480\%$$
          $$\% \text{H} = \left(\frac{10.080}{194.194}\right) \times 100\% = 5.191\%$$
          $$\% \text{N} = \left(\frac{56.028}{194.194}\right) \times 100\% = 28.852\%$$
          $$\% \text{O} = \left(\frac{31.998}{194.194}\right) \times 100\% = 16.477\%$$

          <p><strong>Step 5: Verify summation:</strong></p>
          $$\sum \% = 49.480 + 5.191 + 28.852 + 16.477 = 100.00\%$$
          <p><strong>Result:</strong> Pure caffeine contains \(49.48\%\text{ C}\), \(5.19\%\text{ H}\), \(28.85\%\text{ N}\), and \(16.48\%\text{ O}\) by mass.</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Deriving Empirical and Molecular Formula of Vitamin C (Ascorbic Acid)</h3>
        <p><strong>Scenario:</strong> Elemental microanalysis of a \(10.00\text{-gram}\) sample of purified Vitamin C yields \(40.92\%\) Carbon, \(4.58\%\) Hydrogen, and \(54.50\%\) Oxygen by mass. Mass spectrometry indicates a molecular molar mass of approximately \(176.12\text{ g/mol}\). Determine the empirical formula and the true molecular formula.</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Convert percentages to grams (assuming 100 g sample):</strong></p>
          $$m_{\text{C}} = 40.92\text{ g}, \quad m_{\text{H}} = 4.58\text{ g}, \quad m_{\text{O}} = 54.50\text{ g}$$

          <p><strong>Step 2: Convert grams to moles of each element:</strong></p>
          $$n_{\text{C}} = \frac{40.92\text{ g}}{12.011\text{ g/mol}} = 3.4069\text{ mol}$$
          $$n_{\text{H}} = \frac{4.58\text{ g}}{1.008\text{ g/mol}} = 4.5436\text{ mol}$$
          $$n_{\text{O}} = \frac{54.50\text{ g}}{15.999\text{ g/mol}} = 3.4065\text{ mol}$$

          <p><strong>Step 3: Divide by smallest mole value (\(3.4065\text{ mol}\)):</strong></p>
          $$\text{C}: \frac{3.4069}{3.4065} = 1.00, \quad \text{H}: \frac{4.5436}{3.4065} = 1.334 \approx 1\frac{1}{3}, \quad \text{O}: \frac{3.4065}{3.4065} = 1.00$$

          <p><strong>Step 4: Multiply by 3 to clear the fraction (\(4/3\)):</strong></p>
          $$\text{C}: 1 \times 3 = 3, \quad \text{H}: 1.333 \times 3 = 4, \quad \text{O}: 1 \times 3 = 3$$
          $$\textbf{Empirical Formula: } \text{C}_3\text{H}_4\text{O}_3$$

          <p><strong>Step 5: Compute empirical formula mass and scaling factor:</strong></p>
          $$M_{\text{empirical}} = (3 \times 12.011) + (4 \times 1.008) + (3 \times 15.999) = 36.033 + 4.032 + 47.997 = 88.062\text{ g/mol}$$
          $$n_{\text{factor}} = \frac{M_{\text{molecular}}}{M_{\text{empirical}}} = \frac{176.12}{88.062} \approx 2.00$$
          $$\textbf{Molecular Formula: } (\text{C}_3\text{H}_4\text{O}_3)_2 = \text{C}_6\text{H}_8\text{O}_6$$
          <p><strong>Conclusion:</strong> The empirical formula is \(\text{C}_3\text{H}_4\text{O}_3\) and the true molecular formula of Vitamin C is \(\text{C}_6\text{H}_8\text{O}_6\).</p>
        </div>
      </div>

      <h2>6. Frequently Asked Questions (Applied Chemistry &amp; Assay)</h2>
      <div class="faq-accordion">
        <details class="faq-item">
          <summary>Can two different compounds have identical percent compositions?</summary>
          <div class="faq-answer">
            <p>Yes. Chemical isomers (compounds with identical molecular formulas but different structural connectivity, such as ethanol and dimethyl ether, both C2H6O) have completely identical percent compositions. Furthermore, any two compounds that share the same empirical formula (such as formaldehyde CH2O, acetic acid C2H4O2, and glucose C6H12O6) possess exactly identical mass percentages (40.0% C, 6.71% H, 53.29% O) despite having vastly different physical, chemical, and biological properties.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>How does isotopic abundance affect percent composition calculations?</summary>
          <div class="faq-answer">
            <p>Standard periodic table atomic weights represent the weighted average of all naturally occurring stable isotopes on Earth. For example, carbon is 98.93% Carbon-12 and 1.07% Carbon-13, yielding an average atomic mass of 12.011 g/mol. In specialty applications like nuclear reactor engineering or NMR isotopic labeling, isotopically enriched compounds (such as deuterated water D2O, where deuterium has mass 2.014 g/mol) have dramatically altered percent compositions (D2O is 20.1% Hydrogen/Deuterium by mass, compared to 11.2% for normal H2O).</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>What is water of crystallization and how is it included in percent composition?</summary>
          <div class="faq-answer">
            <p>Many inorganic salts incorporate water molecules into their solid crystal matrix (hydrates), such as copper(II) sulfate pentahydrate: CuSO4·5H2O. When calculating percent composition, the mass of the 5 bound water molecules (5 * 18.015 = 90.075 g/mol) must be included in the total formula mass (249.68 g/mol). Water of crystallization itself can be treated as an individual component: % H2O = (90.075 / 249.68) * 100% = 36.08%.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>How do mineralogists use percent composition?</summary>
          <div class="faq-answer">
            <p>Mining engineers and geochemists use percent composition to determine theoretical ore grade and metal recovery potential. For example, in copper mining, chalcopyrite (CuFeS2, formula mass 183.52 g/mol) has a theoretical copper content of % Cu = (63.546 / 183.52) * 100% = 34.63%. Knowing this theoretical ceiling allows metallurgists to evaluate extraction efficiency from crushed raw ore.</p>
          </div>
        </details>
      </div>

      <h2>7. Related Stoichiometry &amp; Chemical Calculators</h2>
      <p>Explore our integrated directory of chemical tools to solve empirical formulas, reaction yields, and solution preparations:</p>
      <div class="related-calculators" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-top: 1rem;">
        <a href="molar-mass-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Molar Mass Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Compute formula weights and molecular weights from chemical symbols.</p>
        </a>
        <a href="moles-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Moles Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Convert between grams, moles ($n = m/M$), and Avogadro particle counts.</p>
        </a>
        <a href="mass-percent-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Mass Percent Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Determine solution weight concentration (% w/w) and solute/solvent mass ratios.</p>
        </a>
        <a href="percent-yield-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Percent Yield Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Calculate reaction efficiency from actual and theoretical yield limits.</p>
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
          <li><a href="percent-composition-calculator.html">Percent Composition</a></li>
          <li><a href="molar-mass-calculator.html">Molar Mass Calculator</a></li>
          <li><a href="moles-calculator.html">Moles Calculator</a></li>
          <li><a href="mass-percent-calculator.html">Mass Percent</a></li>
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
      const presetSelect = document.getElementById('pc-preset');
      const elementsContainer = document.getElementById('pc-elements-container');
      const addElementBtn = document.getElementById('pc-add-element-btn');
      const calcBtn = document.getElementById('pc-calc-btn');
      const resetBtn = document.getElementById('pc-reset-btn');

      const mwOut = document.getElementById('pc-mw-out');
      const summaryOut = document.getElementById('pc-summary-out');
      const breakdownBody = document.getElementById('pc-breakdown-body');

      const COMMON_ELEMENTS = {
        'H': 1.008, 'He': 4.003, 'Li': 6.941, 'Be': 9.012, 'B': 10.811,
        'C': 12.011, 'N': 14.007, 'O': 15.999, 'F': 18.998, 'Ne': 20.180,
        'Na': 22.990, 'Mg': 24.305, 'Al': 26.982, 'Si': 28.085, 'P': 30.974,
        'S': 32.065, 'Cl': 35.453, 'K': 39.098, 'Ca': 40.078, 'Fe': 55.845,
        'Cu': 63.546, 'Zn': 65.380, 'Br': 79.904, 'Ag': 107.868, 'I': 126.904
      };

      const PRESETS = {
        'water': [
          { symbol: 'H', count: 2, mw: 1.008 },
          { symbol: 'O', count: 1, mw: 15.999 }
        ],
        'glucose': [
          { symbol: 'C', count: 6, mw: 12.011 },
          { symbol: 'H', count: 12, mw: 1.008 },
          { symbol: 'O', count: 6, mw: 15.999 }
        ],
        'co2': [
          { symbol: 'C', count: 1, mw: 12.011 },
          { symbol: 'O', count: 2, mw: 15.999 }
        ],
        'ethanol': [
          { symbol: 'C', count: 2, mw: 12.011 },
          { symbol: 'H', count: 6, mw: 1.008 },
          { symbol: 'O', count: 1, mw: 15.999 }
        ],
        'caffeine': [
          { symbol: 'C', count: 8, mw: 12.011 },
          { symbol: 'H', count: 10, mw: 1.008 },
          { symbol: 'N', count: 4, mw: 14.007 },
          { symbol: 'O', count: 2, mw: 15.999 }
        ],
        'paracetamol': [
          { symbol: 'C', count: 8, mw: 12.011 },
          { symbol: 'H', count: 9, mw: 1.008 },
          { symbol: 'N', count: 1, mw: 14.007 },
          { symbol: 'O', count: 2, mw: 15.999 }
        ],
        'caco3': [
          { symbol: 'Ca', count: 1, mw: 40.078 },
          { symbol: 'C', count: 1, mw: 12.011 },
          { symbol: 'O', count: 3, mw: 15.999 }
        ],
        'h2so4': [
          { symbol: 'H', count: 2, mw: 1.008 },
          { symbol: 'S', count: 1, mw: 32.065 },
          { symbol: 'O', count: 4, mw: 15.999 }
        ],
        'aspirin': [
          { symbol: 'C', count: 9, mw: 12.011 },
          { symbol: 'H', count: 8, mw: 1.008 },
          { symbol: 'O', count: 4, mw: 15.999 }
        ]
      };

      function createRow(symbol = 'H', count = 1, mw = 1.008) {
        const row = document.createElement('div');
        row.className = 'form-row pc-element-row';
        row.style.marginBottom = '0.5rem';
        row.style.alignItems = 'flex-end';

        row.innerHTML = `
          <div class="form-group" style="flex: 1; min-width: 80px;">
            <label style="font-size: 0.75rem;">Element</label>
            <input type="text" class="form-control pc-el-symbol" value="${symbol}" placeholder="e.g. C">
          </div>
          <div class="form-group" style="flex: 1; min-width: 80px;">
            <label style="font-size: 0.75rem;">Subscript (n)</label>
            <input type="number" class="form-control pc-el-count" value="${count}" min="1" step="1">
          </div>
          <div class="form-group" style="flex: 1.5; min-width: 110px;">
            <label style="font-size: 0.75rem;">Atomic Wt (g/mol)</label>
            <input type="number" class="form-control pc-el-mw" value="${mw}" step="any" min="0.001">
          </div>
          <button type="button" class="btn btn-secondary pc-remove-btn" style="padding: 0.5rem 0.75rem; margin-bottom: 1rem; color: #dc2626;">&times;</button>
        `;

        const symInput = row.querySelector('.pc-el-symbol');
        const countInput = row.querySelector('.pc-el-count');
        const mwInput = row.querySelector('.pc-el-mw');
        const removeBtn = row.querySelector('.pc-remove-btn');

        symInput.addEventListener('input', function() {
          const sym = this.value.trim();
          if (COMMON_ELEMENTS[sym]) {
            mwInput.value = COMMON_ELEMENTS[sym];
          }
          presetSelect.value = 'custom';
          calculate();
        });

        countInput.addEventListener('input', function() {
          presetSelect.value = 'custom';
          calculate();
        });

        mwInput.addEventListener('input', function() {
          presetSelect.value = 'custom';
          calculate();
        });

        removeBtn.addEventListener('click', function() {
          if (elementsContainer.querySelectorAll('.pc-element-row').length > 1) {
            row.remove();
            presetSelect.value = 'custom';
            calculate();
          }
        });

        return row;
      }

      function loadPreset(key) {
        elementsContainer.innerHTML = '';
        const list = PRESETS[key] || PRESETS['water'];
        list.forEach(item => {
          elementsContainer.appendChild(createRow(item.symbol, item.count, item.mw));
        });
        calculate();
      }

      function calculate() {
        const rows = elementsContainer.querySelectorAll('.pc-element-row');
        let totalMW = 0;
        let totalAtoms = 0;
        const elementsData = [];

        rows.forEach(r => {
          const sym = r.querySelector('.pc-el-symbol').value.trim() || 'X';
          const n = parseInt(r.querySelector('.pc-el-count').value, 10) || 1;
          const mw = parseFloat(r.querySelector('.pc-el-mw').value) || 1.0;

          const mass = n * mw;
          totalMW += mass;
          totalAtoms += n;

          elementsData.push({
            symbol: sym,
            count: n,
            atomicMass: mw,
            totalMass: mass
          });
        });

        if (totalMW <= 0) {
          mwOut.textContent = "-- g/mol";
          summaryOut.textContent = "Please enter valid elements.";
          breakdownBody.innerHTML = '';
          return;
        }

        mwOut.textContent = totalMW.toFixed(3) + " g/mol";
        summaryOut.textContent = `${elementsData.length} Elements \u2022 ${totalAtoms} Total Atoms`;

        // Render Breakdown Table
        breakdownBody.innerHTML = '';
        elementsData.forEach(el => {
          const pct = (el.totalMass / totalMW) * 100;
          const tr = document.createElement('tr');
          tr.innerHTML = `
            <td><strong>${el.symbol}</strong></td>
            <td>${el.count}</td>
            <td>${el.atomicMass.toFixed(3)}</td>
            <td>${el.totalMass.toFixed(3)}</td>
            <td><strong style="color: var(--primary, #2563eb);">${pct.toFixed(2)}%</strong></td>
          `;
          breakdownBody.appendChild(tr);
        });
      }

      presetSelect.addEventListener('change', function() {
        if (this.value !== 'custom') {
          loadPreset(this.value);
        }
      });

      addElementBtn.addEventListener('click', function() {
        elementsContainer.appendChild(createRow('C', 1, 12.011));
        presetSelect.value = 'custom';
        calculate();
      });

      calcBtn.addEventListener('click', calculate);

      resetBtn.addEventListener('click', function() {
        presetSelect.value = 'water';
        loadPreset('water');
      });

      // Initial execution
      loadPreset('water');
    })();
  </script>
</body>
</html>
"""

# 6. percent-yield-calculator.html
HTML_PERCENT_YIELD = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Percent Yield Calculator - Chemical Reaction Efficiency &amp; Actual Yield</title>
  <meta name="description" content="Calculate reaction percent yield (% Yield = Actual / Theoretical * 100%), percent error, stoichiometric limits, and chemical synthesis efficiency.">
  <link rel="canonical" href="https://calchub.org/percent-yield-calculator.html">
  <meta property="og:title" content="Percent Yield Calculator - Reaction Efficiency Solver">
  <meta property="og:description" content="Free chemistry percent yield calculator. Compute percentage yield (% Yield = Actual / Theoretical * 100%), required theoretical mass, and percent error.">
  <meta property="og:url" content="https://calchub.org/percent-yield-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Percent Yield Calculator - Chemistry Synthesis Tool">
  <meta name="twitter:description" content="Determine organic synthesis yield percentages, purification losses, and chemical reaction efficiency with worked proofs.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Percent Yield Calculator",
    "url": "https://calchub.org/percent-yield-calculator.html",
    "description": "Calculates chemical reaction percent yield, percent error, and required theoretical reactant amounts for chemical syntheses.",
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
        "name": "What is the formula for percent yield in chemistry?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Percent yield is calculated by dividing the experimental actual yield by the stoichiometric theoretical yield and multiplying by 100%: Percent Yield = (Actual Yield / Theoretical Yield) * 100%."
        }
      },
      {
        "@type": "Question",
        "name": "What is the difference between actual yield and theoretical yield?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Theoretical yield is the maximum possible quantity of product predicted by stoichiometry from the limiting reactant, assuming 100% complete conversion with zero loss. Actual yield is the real mass of pure product measured on an analytical balance after reaction, isolation, and purification in the laboratory."
        }
      },
      {
        "@type": "Question",
        "name": "Can a reaction percent yield exceed 100%?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A genuine chemical reaction can never exceed 100% yield due to the Law of Conservation of Mass. However, an apparent yield >100% commonly occurs in laboratory experiments due to experimental errors, such as incomplete drying (residual solvent/water in the sample), presence of unreacted starting materials, or co-crystallized impurities."
        }
      },
      {
        "@type": "Question",
        "name": "What causes reaction percent yields to be less than 100%?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Common factors reducing percent yield include: (1) Reversible thermodynamic equilibrium preventing 100% completion; (2) Competing side reactions forming undesired byproducts; (3) Mechanical losses during filtration, transfer, washing, and recrystallization; (4) Impure starting reactants."
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
      <span>Percent Yield Calculator</span>
    </nav>

    <div class="page-header">
      <h1 class="page-title">Percent Yield Calculator</h1>
      <p class="page-desc">Compute reaction percentage yield, actual experimental yields, theoretical maximums, and stoichiometric synthesis efficiency.</p>
    </div>

    <div class="calc-grid">
      <!-- Calculator Column -->
      <div class="calc-card">
        <div class="calc-header">
          <h2>Reaction Efficiency &amp; Percent Yield Solver</h2>
        </div>

        <!-- Mode Selection -->
        <div class="form-group">
          <label for="py-mode">Calculation Mode:</label>
          <select id="py-mode" class="form-control">
            <option value="find-percent" selected>Calculate Percent Yield (from Actual &amp; Theoretical Yield)</option>
            <option value="find-actual">Calculate Actual Yield (from Target % &amp; Theoretical Yield)</option>
            <option value="find-theoretical">Calculate Required Theoretical Yield (from Actual Yield &amp; %)</option>
          </select>
        </div>

        <!-- Reaction Presets -->
        <div class="form-group">
          <label for="py-preset">Common Reaction Synthesis Preset:</label>
          <select id="py-preset" class="form-control">
            <option value="custom">-- Custom Laboratory Synthesis --</option>
            <option value="aspirin" selected>Aspirin Synthesis (Theor: 15.0 g, Actual: 12.3 g &rarr; 82.0%)</option>
            <option value="ester">Esterification / Ethyl Acetate (Theor: 50.0 g, Actual: 42.5 g &rarr; 85.0%)</option>
            <option value="precip">BaSO4 Precipitation (Theor: 2.33 g, Actual: 2.21 g &rarr; 94.8%)</option>
            <option value="haber">Haber Ammonia Pilot (Theor: 100.0 kg, Actual: 18.0 kg &rarr; 18.0% single-pass)</option>
            <option value="copper">Copper Displacement (Theor: 6.35 g, Actual: 5.85 g &rarr; 92.1%)</option>
          </select>
        </div>

        <!-- Inputs Container -->
        <div id="py-inputs-container">
          <!-- Actual Yield Row -->
          <div class="form-row" id="py-actual-row">
            <div class="form-group">
              <label for="py-actual-val">Actual Experimental Yield ($Y_{\text{actual}}$):</label>
              <input type="number" id="py-actual-val" class="form-control" value="12.3" step="any" min="0.0001">
            </div>
            <div class="form-group">
              <label for="py-actual-unit">Unit:</label>
              <select id="py-actual-unit" class="form-control">
                <option value="g" selected>Grams (g)</option>
                <option value="mg">Milligrams (mg)</option>
                <option value="kg">Kilograms (kg)</option>
                <option value="mol">Moles (mol)</option>
              </select>
            </div>
          </div>

          <!-- Theoretical Yield Row -->
          <div class="form-row" id="py-theor-row">
            <div class="form-group">
              <label for="py-theor-val">Theoretical Stoichiometric Yield ($Y_{\text{theor}}$):</label>
              <input type="number" id="py-theor-val" class="form-control" value="15.0" step="any" min="0.0001">
            </div>
            <div class="form-group">
              <label for="py-theor-unit">Unit:</label>
              <select id="py-theor-unit" class="form-control">
                <option value="g" selected>Grams (g)</option>
                <option value="mg">Milligrams (mg)</option>
                <option value="kg">Kilograms (kg)</option>
                <option value="mol">Moles (mol)</option>
              </select>
            </div>
          </div>

          <!-- Target Percent Row -->
          <div class="form-row" id="py-target-row" style="display: none;">
            <div class="form-group">
              <label for="py-target-pct">Target Percent Yield (%):</label>
              <input type="number" id="py-target-pct" class="form-control" value="82.0" step="any" min="0.01" max="100.0">
            </div>
          </div>
        </div>

        <div class="form-actions">
          <button type="button" id="py-calc-btn" class="btn btn-primary">Calculate Percent Yield</button>
          <button type="button" id="py-reset-btn" class="btn btn-secondary">Reset</button>
        </div>

        <!-- Output Cards -->
        <div id="py-results" class="results-container" style="margin-top: 1.5rem;">
          <div class="result-hero-card">
            <div class="result-label" style="font-size: 0.875rem; color: var(--text-muted, #64748b); text-transform: uppercase; font-weight: 600;">Reaction Percent Yield</div>
            <div id="py-primary-out" style="font-size: 2.25rem; font-weight: 800; color: var(--primary, #2563eb); margin: 0.25rem 0;">82.00%</div>
            <div id="py-status-out" style="font-size: 1rem; color: var(--text-secondary, #475569); font-weight: 600;">Good Synthetic Yield (Typical Laboratory Isolation)</div>
          </div>

          <div class="summary-metrics-grid">
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Actual Yield</div>
              <div id="py-act-out" style="font-size: 1.15rem; font-weight: 700;">12.30 g</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Theoretical Yield</div>
              <div id="py-theor-out" style="font-size: 1.15rem; font-weight: 700;">15.00 g</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Mass Loss / Discrepancy</div>
              <div id="py-loss-out" style="font-size: 1.15rem; font-weight: 700; color: #dc2626;">2.70 g (18.00%)</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Percent Error</div>
              <div id="py-error-out" style="font-size: 1.15rem; font-weight: 700;">18.00%</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Reference Sidebar -->
      <aside class="sidebar-card">
        <h3>Percent Yield Benchmark Scale</h3>
        <p style="font-size: 0.875rem; color: var(--text-secondary, #475569);">General rating of chemical synthesis efficiency:</p>
        <ul style="font-size: 0.875rem; line-height: 1.6; margin-left: 1.25rem;">
          <li><strong>&gt; 90%:</strong> Excellent yield (high purity, minimal side products)</li>
          <li><strong>75% – 90%:</strong> Good synthetic yield (standard academic organic lab)</li>
          <li><strong>50% – 75%:</strong> Moderate yield (multi-step loss or equilibrium limit)</li>
          <li><strong>&lt; 50%:</strong> Poor yield (competing pathways or difficult isolation)</li>
          <li><strong>&gt; 100%:</strong> Incomplete drying (residual solvent) or contaminated</li>
        </ul>

        <h3 style="margin-top: 1.25rem;">Fundamental Equations</h3>
        <ul style="font-size: 0.875rem; line-height: 1.6; margin-left: 1.25rem;">
          <li>\(\% \text{Yield} = \frac{\text{Actual}}{\text{Theoretical}} \times 100\%\)</li>
          <li>\(\% \text{Error} = \frac{|\text{Theor} - \text{Actual}|}{\text{Theor}} \times 100\%\)</li>
          <li>\(\text{Loss} = \text{Theor} - \text{Actual}\)</li>
        </ul>
      </aside>
    </div>

    <!-- Long-Form Informational Engineering Article (1,400+ Words) -->
    <article class="article-body">
      <h2>1. The Chemical Definition and Practical Purpose of Percent Yield</h2>
      <p>In synthetic chemistry, chemical manufacturing, and process engineering, percent yield quantifies the efficiency of a chemical reaction by comparing the actual quantity of pure product isolated from a laboratory experiment with the theoretical maximum quantity predicted by stoichiometric laws. Formally:</p>
      $$\text{Percent Yield } (\% Y) = \left(\frac{\text{Actual Yield}}{\text{Theoretical Yield}}\right) \times 100\%$$
      <p>Where:</p>
      <ul>
        <li><strong>Actual Yield:</strong> The real, experimentally measured mass or molar quantity of purified product obtained after reaction completion, filtration, solvent evaporation, and crystallization.</li>
        <li><strong>Theoretical Yield:</strong> The maximum calculated quantity of product that could form if 100% of the limiting reactant were converted into the desired product with zero physical loss, zero competing side reactions, and complete stoichiometric conversion.</li>
      </ul>
      <p>Percent yield serves as the primary benchmark metric for chemical process optimization, economic feasibility assessment in pharmaceutical manufacturing, and the evaluation of green chemistry atom economies.</p>

      <h2>2. Understanding Theoretical Yield and Limiting Reactants</h2>
      <p>Theoretical yield is calculated through rigorous stoichiometric dimensional analysis based on the **limiting reactant** (the reactant that is consumed first and stops the reaction). Consider a generalized chemical reaction:</p>
      $$a\text{ A} + b\text{ B} \longrightarrow c\text{ C}$$
      <p>To determine the theoretical yield of product \(\text{C}\):</p>
      <ol>
        <li>Calculate the starting moles of all reactants: \(n_{\text{A}} = m_{\text{A}} / M_{\text{A}}\) and \(n_{\text{B}} = m_{\text{B}} / M_{\text{B}}\).</li>
        <li>Normalize by their balanced stoichiometric coefficients to identify the limiting reactant:
        $$\text{If } \frac{n_{\text{A}}}{a} &lt; \frac{n_{\text{B}}}{b}, \quad \text{then A is the limiting reactant.}$$</li>
        <li>Calculate the theoretical maximum moles of product \(\text{C}\) based strictly on limiting reactant \(\text{A}\):
        $$n_{\text{C, theoretical}} = n_{\text{A}} \times \left(\frac{c}{a}\right)$$</li>
        <li>Convert moles of \(\text{C}\) into mass:
        $$m_{\text{theoretical}} = n_{\text{C, theoretical}} \times M_{\text{C}}$$</li>
      </ol>

      <h2>3. Why Chemical Yields Rarely Reach 100%</h2>
      <p>In real-world laboratories and chemical production plants, reactions rarely achieve a 100% yield. The discrepancy between theoretical predictions and experimental realities stems from several physical, chemical, and operational mechanisms:</p>

      <h3>A. Reversible Chemical Equilibria</h3>
      <p>Many chemical reactions are thermodynamically reversible. Rather than proceeding to complete \(100\%\) consumption of reactants, the system reaches dynamic chemical equilibrium governed by an equilibrium constant (\(K_{\text{eq}}\)):</p>
      $$K_{\text{eq}} = \frac{[\text{Products}]^c}{[\text{Reactants}]^a}$$
      <p>Unless products are continuously removed (e.g., Le Chatelier's principle applied by boiling off a volatile ester or precipitating an insoluble salt), the reaction reaches a steady-state ceiling where reactants and products coexist.</p>

      <h3>B. Competing Side Reactions and Parallel Pathways</h3>
      <p>Organic molecules frequently react through multiple competing thermodynamic or kinetic pathways. For example, during nucleophilic substitution (\(\text{S}_N2\)), competing elimination (\(\text{E}2\)) reactions often occur simultaneously, diverting a portion of the limiting reactant into unwanted alkene byproducts.</p>

      <h3>C. Physical Separation and Purification Losses</h3>
      <p>The steps required to isolate pure product invariably cause mechanical losses:</p>
      <ul>
        <li><strong>Liquid-Liquid Extraction:</strong> Incomplete partition coefficient distribution between aqueous and organic phases leaves traces of product in the discarded aqueous layer.</li>
        <li><strong>Recrystallization:</strong> In accordance with solubility curves, a fraction of the desired compound remains dissolved in the cold mother liquor.</li>
        <li><strong>Adsorption:</strong> Products adhere to filter paper, rotary evaporator glassware, and chromatographic silica gel columns.</li>
      </ul>

      <h2>4. Diagnosing Yields Exceeding 100%</h2>
      <p>Because matter can neither be created nor destroyed (Law of Conservation of Mass), an experimental percent yield greater than \(100.0\%\) is physically impossible for a pure product. When an analytical balance reports an apparent yield \(&gt; 100\%\), it signals experimental contamination or weighing error:</p>
      <ul>
        <li><strong>Residual Solvent / Moisture:</strong> The most common laboratory cause. If a filtered precipitate is weighed before reaching constant mass in a desiccator or vacuum oven, trapped water or organic solvent inflates the mass reading.</li>
        <li><strong>Unreacted Starting Material:</strong> Incomplete separation leaves unconsumed reactants co-crystallized with the product.</li>
        <li><strong>Precipitated Salts:</strong> Byproduct inorganic salts (such as \(\text{NaCl}\) or \(\text{MgSO}_4\) drying agent) may have co-precipitated into the final product flask.</li>
        <li><strong>Analytical Taring Error:</strong> Failure to properly tare the collection vessel on the laboratory balance.</li>
      </ul>

      <h2>5. Green Chemistry: Atom Economy vs. Percent Yield</h2>
      <p>While percent yield measures how efficiently a given chemical procedure executes, it does not assess whether the reaction itself is environmentally sustainable. In modern green chemistry, percent yield is evaluated alongside **Atom Economy** and the **Environmental Factor (\(E\)-Factor\)):</p>
      $$\text{Atom Economy } (\%) = \left(\frac{\text{Molecular Weight of Desired Product}}{\sum \text{Molecular Weights of All Reactants}}\right) \times 100\%$$
      <p>A reaction can have a \(95\%\) percent yield but still generate vast quantities of toxic waste if its atom economy is only \(25\%\) (e.g., classical Wittig reactions producing massive triphenylphosphine oxide waste). Modern pharmaceutical green synthesis strives to maximize both percent yield (\(&gt; 85\%\)) and atom economy (\(&gt; 70\%\)).</p>

      <h2>6. Step-by-Step Worked Chemical Case Studies</h2>

      <div class="worked-example-card">
        <h3>Case Study 1: Laboratory Synthesis of Aspirin (Acetylsalicylic Acid)</h3>
        <p><strong>Scenario:</strong> An undergraduate chemistry student synthesizes aspirin by reacting \(10.00\text{ grams}\) of salicylic acid (\(\text{C}_7\text{H}_6\text{O}_3\), \(M = 138.12\text{ g/mol}\)) with excess acetic anhydride (\(\text{C}_4\text{H}_6\text{O}_3\)) according to: \(\text{C}_7\text{H}_6\text{O}_3 + \text{C}_4\text{H}_6\text{O}_3 \to \text{C}_9\text{H}_8\text{O}_4 + \text{C}_2\text{H}_4\text{O}_2\). After crystallization and vacuum drying, the student isolates \(10.92\text{ grams}\) of pure dry aspirin (\(\text{C}_9\text{H}_8\text{O}_4\), \(M = 180.16\text{ g/mol}\)). Calculate the theoretical yield and the reaction percent yield.</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Calculate moles of limiting reactant (salicylic acid):</strong></p>
          $$n_{\text{salicylic}} = \frac{10.00\text{ g}}{138.12\text{ g/mol}} = 0.07240\text{ moles}$$

          <p><strong>Step 2: Determine theoretical moles of aspirin produced:</strong></p>
          <p>From the \(1:1\) stoichiometric molar ratio:</p>
          $$n_{\text{aspirin, theoretical}} = 0.07240\text{ moles}$$

          <p><strong>Step 3: Calculate theoretical yield mass:</strong></p>
          $$m_{\text{theoretical}} = 0.07240\text{ mol} \times 180.16\text{ g/mol} = 13.044\text{ grams}$$

          <p><strong>Step 4: Calculate percent yield from actual isolated mass (\(10.92\text{ g}\)):</strong></p>
          $$\% \text{Yield} = \left(\frac{10.92\text{ g}}{13.044\text{ g}}\right) \times 100\% = 83.72\%$$

          <p><strong>Step 5: Compute percent error and lost mass:</strong></p>
          $$\text{Mass Lost in Purification} = 13.044\text{ g} - 10.920\text{ g} = 2.124\text{ grams}$$
          $$\% \text{Error} = 100.0\% - 83.72\% = 16.28\%$$
          <p><strong>Conclusion:</strong> The aspirin synthesis achieved an \(83.72\%\) yield, representing a high-efficiency academic organic preparation.</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Sizing Reactant Mass for Pilot Scale Production Target</h3>
        <p><strong>Scenario:</strong> A pilot pharmaceutical plant needs to produce exactly \(25.0\text{ kilograms}\) of an active pharmaceutical ingredient (API). Historical manufacturing telemetry demonstrates that this specific chemical coupling reaction operates at an average percent yield of \(78.5\%\). If the theoretical stoichiometric mass ratio is \(1.20\text{ kg}\) of limiting starting material per \(1.00\text{ kg}\) of theoretical API, calculate the required theoretical yield and the mass of starting reactant needed.</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Calculate required theoretical yield from target actual yield:</strong></p>
          $$\% \text{Yield} = \frac{\text{Actual}}{\text{Theoretical}} \times 100\% \implies \text{Theoretical} = \frac{\text{Actual}}{\% \text{Yield} / 100}$$
          $$\text{Theoretical Yield Required} = \frac{25.0\text{ kg}}{0.785} = 31.847\text{ kilograms}$$

          <p><strong>Step 2: Calculate required starting material mass:</strong></p>
          $$m_{\text{starting material}} = 31.847\text{ kg theoretical API} \times 1.20\text{ kg reactant/kg API} = 38.22\text{ kg}$$
          <p><strong>Engineering Result:</strong> The chemical plant must charge \(38.22\text{ kg}\) of limiting reactant into the reactor to guarantee obtaining \(25.0\text{ kg}\) of finished isolated API under \(78.5\%\) operating yield conditions.</p>
        </div>
      </div>

      <h2>7. Frequently Asked Questions (Synthetic Organic Chemistry)</h2>
      <div class="faq-accordion">
        <details class="faq-item">
          <summary>What is an isolated yield versus an assay yield?</summary>
          <div class="faq-answer">
            <p>An isolated yield is the mass of pure, dry product collected in a vial after all purification steps (recrystallization, chromatography). An assay yield (or in-situ NMR/HPLC yield) measures the percentage of product present in the crude reaction mixture before any workup or isolation. The difference between assay yield and isolated yield reveals how much product is lost specifically during mechanical purification.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>How does multi-step synthesis affect overall cumulative yield?</summary>
          <div class="faq-answer">
            <p>In multi-step chemical syntheses (such as total synthesis of natural products), overall cumulative yield is the mathematical product of the individual step yields: \(\% Y_{\text{overall}} = Y_1 \times Y_2 \times \dots \times Y_n\). If an 8-step sequence has an impressive 85% yield at each step, the overall yield is: \(0.85^8 \approx 0.272\) or only 27.2%. This compounding decay demonstrates why process chemists seek convergent rather than linear synthetic routes.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>Does temperature influence percent yield?</summary>
          <div class="faq-answer">
            <p>Significantly. For exothermic reversible reactions, Le Chatelier's principle dictates that raising temperature shifts equilibrium toward reactants, reducing theoretical equilibrium yield. Conversely, running a reaction at too low a temperature may reduce kinetic reaction rates to near zero, resulting in incomplete conversion within practical reaction times. Finding the optimal temperature window balances reaction velocity against equilibrium yield and byproduct formation.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>What is the difference between percent yield and percent purity?</summary>
          <div class="faq-answer">
            <p>Percent yield measures quantity (how much of the theoretical maximum product was made), whereas percent purity measures quality (what percentage of the isolated solid is actually the target molecule versus impurities). A chemist might isolate a 95% yield of crude product that is only 70% pure; after recrystallization, they might obtain an 80% yield that is 99.5% pure.</p>
          </div>
        </details>
      </div>

      <h2>8. Related Chemical Stoichiometry Calculators</h2>
      <p>Explore our integrated chemistry computation suite to solve theoretical yields, moles, and solution concentrations:</p>
      <div class="related-calculators" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-top: 1rem;">
        <a href="moles-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Moles Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Convert between sample grams, chemical moles, and Avogadro particle counts.</p>
        </a>
        <a href="percent-composition-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Percent Composition Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Determine elemental mass percentages (% w/w) in chemical formulas.</p>
        </a>
        <a href="molar-mass-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Molar Mass Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Calculate molecular weights and elemental proportions from chemical formulas.</p>
        </a>
        <a href="mass-percent-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Mass Percent Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Determine solution weight concentration (% w/w) and solute/solvent mass ratios.</p>
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
          <li><a href="percent-yield-calculator.html">Percent Yield</a></li>
          <li><a href="percent-composition-calculator.html">Percent Composition</a></li>
          <li><a href="moles-calculator.html">Moles Calculator</a></li>
          <li><a href="mass-percent-calculator.html">Mass Percent</a></li>
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
      const modeSelect = document.getElementById('py-mode');
      const presetSelect = document.getElementById('py-preset');

      const actualRow = document.getElementById('py-actual-row');
      const actualValInput = document.getElementById('py-actual-val');
      const actualUnitSelect = document.getElementById('py-actual-unit');

      const theorRow = document.getElementById('py-theor-row');
      const theorValInput = document.getElementById('py-theor-val');
      const theorUnitSelect = document.getElementById('py-theor-unit');

      const targetRow = document.getElementById('py-target-row');
      const targetPctInput = document.getElementById('py-target-pct');

      const calcBtn = document.getElementById('py-calc-btn');
      const resetBtn = document.getElementById('py-reset-btn');

      // Outputs
      const primaryOut = document.getElementById('py-primary-out');
      const statusOut = document.getElementById('py-status-out');
      const actOut = document.getElementById('py-act-out');
      const theorOut = document.getElementById('py-theor-out');
      const lossOut = document.getElementById('py-loss-out');
      const errorOut = document.getElementById('py-error-out');

      const UNIT_TO_GRAMS = {
        'g': 1.0,
        'mg': 0.001,
        'kg': 1000.0,
        'mol': 1.0 // nominal equivalent
      };

      const PRESETS = {
        'aspirin': { act: 12.3, theor: 15.0, unit: 'g' },
        'ester': { act: 42.5, theor: 50.0, unit: 'g' },
        'precip': { act: 2.21, theor: 2.33, unit: 'g' },
        'haber': { act: 18.0, theor: 100.0, unit: 'kg' },
        'copper': { act: 5.85, theor: 6.35, unit: 'g' }
      };

      function updatePanelVisibility() {
        const m = modeSelect.value;
        if (m === 'find-percent') {
          actualRow.style.display = 'flex';
          theorRow.style.display = 'flex';
          targetRow.style.display = 'none';
        } else if (m === 'find-actual') {
          actualRow.style.display = 'none';
          theorRow.style.display = 'flex';
          targetRow.style.display = 'flex';
        } else if (m === 'find-theoretical') {
          actualRow.style.display = 'flex';
          theorRow.style.display = 'none';
          targetRow.style.display = 'flex';
        }
      }

      function calculate() {
        const mode = modeSelect.value;
        let actual = 0;
        let theoretical = 0;
        let pctYield = 0;
        const unit = actualUnitSelect.value;

        if (mode === 'find-percent') {
          actual = parseFloat(actualValInput.value) || 0;
          theoretical = parseFloat(theorValInput.value) || 0;

          if (actual <= 0 || theoretical <= 0) {
            primaryOut.textContent = "-- %";
            statusOut.textContent = "Please enter positive yield values.";
            return;
          }

          pctYield = (actual / theoretical) * 100;
        } else if (mode === 'find-actual') {
          theoretical = parseFloat(theorValInput.value) || 0;
          const targetPct = parseFloat(targetPctInput.value) || 0;

          if (theoretical <= 0 || targetPct <= 0) {
            primaryOut.textContent = "-- %";
            statusOut.textContent = "Please enter positive target % and theoretical yield.";
            return;
          }

          pctYield = targetPct;
          actual = theoretical * (targetPct / 100);
        } else if (mode === 'find-theoretical') {
          actual = parseFloat(actualValInput.value) || 0;
          const targetPct = parseFloat(targetPctInput.value) || 0;

          if (actual <= 0 || targetPct <= 0) {
            primaryOut.textContent = "-- %";
            statusOut.textContent = "Please enter positive actual yield and target %.";
            return;
          }

          pctYield = targetPct;
          theoretical = actual / (targetPct / 100);
        }

        const massLoss = theoretical - actual;
        const pctError = Math.abs(theoretical - actual) / theoretical * 100;

        // Status Message
        let statusMsg = "";
        if (pctYield > 100) {
          statusMsg = "Warning: Yield > 100% indicates solvent contamination or drying error.";
        } else if (pctYield >= 90) {
          statusMsg = "Excellent Yield (>90% synthetic efficiency)";
        } else if (pctYield >= 70) {
          statusMsg = "Good Synthetic Yield (standard laboratory reaction)";
        } else if (pctYield >= 50) {
          statusMsg = "Moderate Yield (equilibrium or purification limits)";
        } else {
          statusMsg = "Low Yield (<50% - significant side reactions or loss)";
        }

        // Render to UI
        primaryOut.textContent = pctYield.toFixed(2) + "%";
        statusOut.textContent = statusMsg;
        actOut.textContent = actual.toFixed(2) + " " + unit;
        theorOut.textContent = theoretical.toFixed(2) + " " + unit;
        lossOut.textContent = massLoss >= 0 ? `${massLoss.toFixed(2)} ${unit} (${(100 - pctYield).toFixed(2)}%)` : `+${Math.abs(massLoss).toFixed(2)} ${unit} excess`;
        errorOut.textContent = pctError.toFixed(2) + "%";
      }

      presetSelect.addEventListener('change', function() {
        const val = this.value;
        if (PRESETS[val]) {
          const p = PRESETS[val];
          modeSelect.value = 'find-percent';
          updatePanelVisibility();
          actualValInput.value = p.act;
          theorValInput.value = p.theor;
          actualUnitSelect.value = p.unit;
          theorUnitSelect.value = p.unit;
          calculate();
        }
      });

      modeSelect.addEventListener('change', function() {
        updatePanelVisibility();
        calculate();
      });

      [actualValInput, actualUnitSelect, theorValInput, theorUnitSelect, targetPctInput].forEach(el => {
        el.addEventListener('input', function() {
          presetSelect.value = 'custom';
          calculate();
        });
        el.addEventListener('change', calculate);
      });

      calcBtn.addEventListener('click', calculate);

      resetBtn.addEventListener('click', function() {
        modeSelect.value = 'find-percent';
        presetSelect.value = 'aspirin';
        actualValInput.value = '12.3';
        theorValInput.value = '15.0';
        actualUnitSelect.value = 'g';
        theorUnitSelect.value = 'g';
        targetPctInput.value = '82.0';
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
    p1 = os.path.join(BASE_DIR, "percent-composition-calculator.html")
    with open(p1, "w", encoding="utf-8") as f:
        f.write(HTML_PERCENT_COMP.strip() + "\n")
    print(f"Generated: {p1}")

    p2 = os.path.join(BASE_DIR, "percent-yield-calculator.html")
    with open(p2, "w", encoding="utf-8") as f:
        f.write(HTML_PERCENT_YIELD.strip() + "\n")
    print(f"Generated: {p2}")

if __name__ == "__main__":
    generate_files()
