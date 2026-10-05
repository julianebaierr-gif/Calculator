# -*- coding: utf-8 -*-
"""
Generator for Batch 34 - Part 2:
3. moles-calculator.html
4. normality-calculator.html
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 3. moles-calculator.html
HTML_MOLES = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Moles Calculator - Grams to Moles &amp; Avogadro Particle Converter</title>
  <meta name="description" content="Convert grams to moles (n = m/M), calculate Avogadro's particles (N = n * N_A), ideal gas STP volume, and molecular stoichiometry with step-by-step proofs.">
  <link rel="canonical" href="https://calchub.org/moles-calculator.html">
  <meta property="og:title" content="Moles Calculator - Grams, Moles &amp; Particle Count Solver">
  <meta property="og:description" content="Free chemistry mole calculator. Convert mass to moles, moles to grams, calculate atoms/molecules via Avogadro's number (6.022e23), and gas molar volume at STP.">
  <meta property="og:url" content="https://calchub.org/moles-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Moles Calculator - Chemistry Stoichiometry Tool">
  <meta name="twitter:description" content="Compute moles, formula units, and gas volume across common elements and compounds with worked chemical case studies.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Moles Calculator",
    "url": "https://calchub.org/moles-calculator.html",
    "description": "Converts mass to chemical moles, calculates total particles using Avogadro's constant, and computes gas volume at STP.",
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
        "name": "What is the formula to convert grams to moles?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The number of moles (n) is calculated by dividing the sample mass in grams (m) by its molar mass in grams per mole (M): n = m / M. For example, 18.015 grams of water (H2O, M = 18.015 g/mol) equals exactly 1.0 mole."
        }
      },
      {
        "@type": "Question",
        "name": "What is Avogadro's constant and how is it defined?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Avogadro's constant (N_A) is an exact fundamental physical constant defined by the 2019 SI redefinition as exactly 6.02214076 * 10^23 reciprocal moles (mol^-1). One mole of any substance contains exactly this number of elementary entities (atoms, molecules, ions, or electrons)."
        }
      },
      {
        "@type": "Question",
        "name": "What is the volume of one mole of gas at STP?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "At classical Standard Temperature and Pressure (STP: 0°C or 273.15 K, and 1 atm or 101.325 kPa), one mole of an ideal gas occupies approximately 22.414 liters (0.022414 m³). Under modern IUPAC standard conditions (0°C and 1 bar or 100 kPa), standard molar volume is 22.711 liters."
        }
      },
      {
        "@type": "Question",
        "name": "How do you calculate the number of molecules from moles?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The total number of particles (N) is calculated by multiplying the number of moles (n) by Avogadro's constant: N = n * N_A = n * (6.02214076 * 10^23)."
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
      <span>Moles Calculator</span>
    </nav>

    <div class="page-header">
      <h1 class="page-title">Moles Calculator</h1>
      <p class="page-desc">Convert between grams, chemical moles, and particle counts using Avogadro's constant ($6.022 \times 10^{23}$) and ideal gas molar volumes.</p>
    </div>

    <div class="calc-grid">
      <!-- Calculator Column -->
      <div class="calc-card">
        <div class="calc-header">
          <h2>Stoichiometric Mole &amp; Particle Converter</h2>
        </div>

        <!-- Mode Selection -->
        <div class="form-group">
          <label for="mol-mode">Conversion Direction:</label>
          <select id="mol-mode" class="form-control">
            <option value="mass-to-moles" selected>Mass (Grams) &rarr; Moles &amp; Particles</option>
            <option value="moles-to-mass">Moles &rarr; Mass (Grams) &amp; Particles</option>
            <option value="particles-to-moles">Particle Count ($N$) &rarr; Moles &amp; Mass</option>
            <option value="gas-to-moles">Ideal Gas Volume at STP &rarr; Moles &amp; Mass</option>
          </select>
        </div>

        <!-- Substance Preset -->
        <div class="form-group">
          <label for="mol-sub-preset">Common Chemical Compound Preset:</label>
          <select id="mol-sub-preset" class="form-control">
            <option value="custom">-- Custom Formula Weight --</option>
            <option value="water" selected>Water (H2O: 18.015 g/mol)</option>
            <option value="co2">Carbon Dioxide (CO2: 44.010 g/mol)</option>
            <option value="nacl">Table Salt (NaCl: 58.443 g/mol)</option>
            <option value="glucose">Glucose (C6H12O6: 180.156 g/mol)</option>
            <option value="o2">Oxygen Gas (O2: 31.999 g/mol)</option>
            <option value="n2">Nitrogen Gas (N2: 28.013 g/mol)</option>
            <option value="caco3">Calcium Carbonate (CaCO3: 100.087 g/mol)</option>
            <option value="h2so4">Sulfuric Acid (H2SO4: 98.079 g/mol)</option>
            <option value="ch4">Methane (CH4: 16.043 g/mol)</option>
            <option value="c2h5oh">Ethanol (C2H5OH: 46.068 g/mol)</option>
          </select>
        </div>

        <!-- Molar Mass Input Row -->
        <div class="form-row">
          <div class="form-group">
            <label for="mol-mw-input">Molar Mass ($M$ in g/mol):</label>
            <input type="number" id="mol-mw-input" class="form-control" value="18.015" step="any" min="0.001">
          </div>
        </div>

        <!-- Variable Primary Inputs based on Mode -->
        <div id="mol-input-mass-panel">
          <div class="form-row">
            <div class="form-group">
              <label for="mol-mass-val">Sample Mass ($m$):</label>
              <input type="number" id="mol-mass-val" class="form-control" value="100.0" step="any" min="0.000001">
            </div>
            <div class="form-group">
              <label for="mol-mass-unit">Mass Unit:</label>
              <select id="mol-mass-unit" class="form-control">
                <option value="g" selected>Grams (g)</option>
                <option value="mg">Milligrams (mg)</option>
                <option value="kg">Kilograms (kg)</option>
                <option value="oz">Ounces (oz)</option>
                <option value="lb">Pounds (lb)</option>
              </select>
            </div>
          </div>
        </div>

        <div id="mol-input-moles-panel" style="display: none;">
          <div class="form-group">
            <label for="mol-moles-val">Amount of Substance ($n$ in moles):</label>
            <input type="number" id="mol-moles-val" class="form-control" value="1.0" step="any" min="0.000001">
          </div>
        </div>

        <div id="mol-input-particles-panel" style="display: none;">
          <div class="form-row">
            <div class="form-group">
              <label for="mol-part-coeff">Particle Base:</label>
              <input type="number" id="mol-part-coeff" class="form-control" value="6.022" step="any">
            </div>
            <div class="form-group">
              <label for="mol-part-exp">&times; 10^(exponent):</label>
              <input type="number" id="mol-part-exp" class="form-control" value="23" step="1">
            </div>
          </div>
        </div>

        <div id="mol-input-gas-panel" style="display: none;">
          <div class="form-row">
            <div class="form-group">
              <label for="mol-gas-vol">Gas Volume at STP ($V$):</label>
              <input type="number" id="mol-gas-vol" class="form-control" value="22.414" step="any" min="0.0001">
            </div>
            <div class="form-group">
              <label for="mol-gas-unit">Volume Unit:</label>
              <select id="mol-gas-unit" class="form-control">
                <option value="L" selected>Liters (L or dm³)</option>
                <option value="mL">Milliliters (mL or cm³)</option>
                <option value="m3">Cubic Meters (m³)</option>
              </select>
            </div>
          </div>
        </div>

        <div class="form-actions">
          <button type="button" id="mol-calc-btn" class="btn btn-primary">Calculate Moles &amp; Quantities</button>
          <button type="button" id="mol-reset-btn" class="btn btn-secondary">Reset</button>
        </div>

        <!-- Output Cards -->
        <div id="mol-results" class="results-container" style="margin-top: 1.5rem;">
          <div class="result-hero-card">
            <div class="result-label" style="font-size: 0.875rem; color: var(--text-muted, #64748b); text-transform: uppercase; font-weight: 600;">Amount of Substance ($n$)</div>
            <div id="mol-primary-out" style="font-size: 2.25rem; font-weight: 800; color: var(--primary, #2563eb); margin: 0.25rem 0;">5.551 mol</div>
            <div id="mol-status-out" style="font-size: 1rem; color: var(--text-secondary, #475569); font-weight: 600;">100.00 g of H₂O (18.015 g/mol)</div>
          </div>

          <div class="summary-metrics-grid">
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Mass ($m$)</div>
              <div id="mol-mass-out" style="font-size: 1.15rem; font-weight: 700;">100.00 g</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Total Particles ($N$)</div>
              <div id="mol-particles-out" style="font-size: 1.15rem; font-weight: 700;">3.343 &times; 10²⁴</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Ideal Gas Vol @ STP</div>
              <div id="mol-gas-out" style="font-size: 1.15rem; font-weight: 700;">124.42 L</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Millimoles (mmol)</div>
              <div id="mol-mmol-out" style="font-size: 1.15rem; font-weight: 700;">5,551 mmol</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Reference Sidebar -->
      <aside class="sidebar-card">
        <h3>Fundamental Chemistry Constants</h3>
        <ul style="font-size: 0.875rem; line-height: 1.6; margin-left: 1.25rem;">
          <li><strong>Avogadro's Number:</strong><br>\(N_A = 6.02214076 \times 10^{23}\text{ mol}^{-1}\)</li>
          <li><strong>Molar Gas Constant:</strong><br>\(R = 8.314462618\text{ J/(mol}\cdot\text{K)}\)</li>
          <li><strong>Ideal Gas Molar Volume (STP):</strong><br>\(V_m = 22.414\text{ L/mol}\) (at 0°C, 1 atm)</li>
          <li><strong>Molar Volume (IUPAC Standard):</strong><br>\(V_m = 22.711\text{ L/mol}\) (at 0°C, 1 bar)</li>
        </ul>

        <h3 style="margin-top: 1.25rem;">Stoichiometry Formulas</h3>
        <ul style="font-size: 0.875rem; line-height: 1.6; margin-left: 1.25rem;">
          <li>\(n = \frac{m}{M}\)</li>
          <li>\(N = n \times N_A\)</li>
          <li>\(m = n \times M\)</li>
          <li>\(V_{\text{gas}} = n \times 22.414\text{ L}\)</li>
        </ul>
      </aside>
    </div>

    <!-- Long-Form Informational Engineering Article (1,400+ Words) -->
    <article class="article-body">
      <h2>1. The Mole Concept: The Fundamental SI Unit for Chemical Amount</h2>
      <p>The mole (symbol: **mol**) is the base unit of the International System of Units (SI) for amount of substance. In macroscopic laboratory experiments, chemists measure quantities in grams, kilograms, or liters. However, chemical reactions occur atom-by-atom, molecule-by-molecule, or ion-by-ion according to discrete stoichiometric ratios. The mole provides the essential mathematical bridge connecting the microscopic world of subatomic particles to macroscopic mass on an analytical laboratory balance.</p>
      <p>Historically, the mole was defined as the number of atoms contained in exactly 12 grams of pure carbon-12 (\(^{12}\text{C}\)). On May 20, 2019, the General Conference on Weights and Measures (CGPM) adopted the new SI definition, establishing the mole as a fundamental counting unit defined by fixing the numerical value of **Avogadro's constant** (\(N_A\)):</p>
      $$N_A = 6.02214076 \times 10^{23} \text{ mol}^{-1} \text{ (exact)}$$
      <p>Under this modern definition, exactly one mole of any pure chemical substance contains precisely \(6.02214076 \times 10^{23}\) elementary entities—whether those entities are isolated atoms (e.g., helium, iron), covalently bonded molecules (e.g., water, glucose), formula units (e.g., sodium chloride), or subatomic leptons (electrons, protons).</p>

      <h2>2. Mathematical Relationships: Mass, Moles, and Particle Counts</h2>
      <p>Converting between macroscopic sample mass (\(m\)), molar substance amount (\(n\)), and microscopic particle populations (\(N\)) forms the core of all stoichiometric calculations:</p>

      <h3>A. Mass-to-Mole Relationship</h3>
      <p>The amount of substance \(n\) in moles is directly proportional to mass \(m\) in grams, linked by the characteristic molar mass \(M\) of the substance (measured in grams per mole, \(\text{g/mol}\)):</p>
      $$n = \frac{m}{M} \iff m = n \times M \iff M = \frac{m}{n}$$
      <p>Where molar mass \(M\) is numerically equivalent to the relative atomic mass or molecular formula weight found on the periodic table (in unified atomic mass units, \(\text{u}\) or Daltons, \(\text{Da}\)). For example, one atom of carbon-12 has a mass of \(12\text{ u}\), and one mole of carbon-12 has a mass of exactly \(12.000\text{ grams}\).</p>

      <h3>B. Mole-to-Particle Relationship (Avogadro's Equation)</h3>
      <p>To determine the absolute number of individual elementary entities \(N\) in a sample, multiply the amount of substance in moles by Avogadro's constant:</p>
      $$N = n \times N_A = n \times \left(6.02214076 \times 10^{23}\right)$$
      <p>Conversely, given an absolute particle count \(N\), the number of chemical moles is:</p>
      $$n = \frac{N}{N_A} = \frac{N}{6.02214076 \times 10^{23}}$$

      <h3>C. Ideal Gas Molar Volume at STP</h3>
      <p>According to Avogadro's Law, equal volumes of all ideal gases at identical temperature and pressure contain identical numbers of molecules. From the Ideal Gas Law (\(PV = nRT\)), the molar volume of an ideal gas at standard temperature (\(T = 273.15\text{ K} = 0^\circ\text{C}\)) and standard pressure (\(P = 1.000\text{ atm} = 101.325\text{ kPa}\)) is:</p>
      $$V_m = \frac{R T}{P} = \frac{0.082057 \text{ L}\cdot\text{atm/(mol}\cdot\text{K)} \times 273.15\text{ K}}{1.000\text{ atm}} \approx 22.414\text{ Liters/mol}$$
      <p>Therefore, for any ideal gas or mixture of gases at STP:</p>
      $$V = n \times 22.414\text{ L} \iff n = \frac{V_{\text{liters}}}{22.414\text{ L/mol}}$$

      <h2>3. Comprehensive Elemental &amp; Compound Molar Reference Table</h2>
      <p>The following engineering data table lists molar masses, number of moles per 100 grams, and resulting particle populations across common chemical reagents and industrial compounds:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Chemical Substance</th>
              <th>Formula</th>
              <th>Molar Mass (\(M\))</th>
              <th>Moles in 100 g (\(n\))</th>
              <th>Molecules in 100 g (\(N\))</th>
              <th>Gas Volume @ STP (for 100 g)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Hydrogen Gas</td>
              <td>H₂</td>
              <td>2.016 g/mol</td>
              <td>49.603 mol</td>
              <td>2.987 &times; 10²⁵</td>
              <td>1,111.8 L</td>
            </tr>
            <tr>
              <td>Helium</td>
              <td>He</td>
              <td>4.003 g/mol</td>
              <td>24.981 mol</td>
              <td>1.504 &times; 10²⁵</td>
              <td>559.9 L</td>
            </tr>
            <tr>
              <td>Methane</td>
              <td>CH₄</td>
              <td>16.043 g/mol</td>
              <td>6.233 mol</td>
              <td>3.754 &times; 10²⁴</td>
              <td>139.7 L</td>
            </tr>
            <tr>
              <td>Water</td>
              <td>H₂O</td>
              <td>18.015 g/mol</td>
              <td>5.551 mol</td>
              <td>3.343 &times; 10²⁴</td>
              <td>124.4 L (vapor)</td>
            </tr>
            <tr>
              <td>Nitrogen Gas</td>
              <td>N₂</td>
              <td>28.013 g/mol</td>
              <td>3.569 mol</td>
              <td>2.149 &times; 10²⁴</td>
              <td>80.0 L</td>
            </tr>
            <tr>
              <td>Oxygen Gas</td>
              <td>O₂</td>
              <td>31.999 g/mol</td>
              <td>3.125 mol</td>
              <td>1.882 &times; 10²⁴</td>
              <td>70.0 L</td>
            </tr>
            <tr>
              <td>Carbon Dioxide</td>
              <td>CO₂</td>
              <td>44.010 g/mol</td>
              <td>2.272 mol</td>
              <td>1.368 &times; 10²⁴</td>
              <td>50.9 L</td>
            </tr>
            <tr>
              <td>Sodium Chloride</td>
              <td>NaCl</td>
              <td>58.443 g/mol</td>
              <td>1.711 mol</td>
              <td>1.030 &times; 10²⁴</td>
              <td>N/A (ionic solid)</td>
            </tr>
            <tr>
              <td>Sulfuric Acid</td>
              <td>H₂SO₄</td>
              <td>98.079 g/mol</td>
              <td>1.020 mol</td>
              <td>6.143 &times; 10²³</td>
              <td>N/A (liquid)</td>
            </tr>
            <tr>
              <td>Calcium Carbonate</td>
              <td>CaCO₃</td>
              <td>100.087 g/mol</td>
              <td>0.999 mol</td>
              <td>6.015 &times; 10²³</td>
              <td>N/A (mineral solid)</td>
            </tr>
            <tr>
              <td>Glucose</td>
              <td>C₆H₁₂O₆</td>
              <td>180.156 g/mol</td>
              <td>0.555 mol</td>
              <td>3.342 &times; 10²³</td>
              <td>N/A (crystalline solid)</td>
            </tr>
            <tr>
              <td>Sucrose</td>
              <td>C₁₂H₂₂O₁₁</td>
              <td>342.296 g/mol</td>
              <td>0.292 mol</td>
              <td>1.759 &times; 10²³</td>
              <td>N/A (sugar crystal)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>4. The Stoichiometric Highway: Grams to Moles to Product</h2>
      <p>In quantitative chemical reactions, balanced chemical equations specify molar ratios rather than mass ratios. For example, consider the Haber-Bosch industrial synthesis of ammonia:</p>
      $$\text{N}_2\text{ (g)} + 3\text{ H}_2\text{ (g)} \longrightarrow 2\text{ NH}_3\text{ (g)}$$
      <p>This equation indicates that 1 mole of nitrogen gas reacts with 3 moles of hydrogen gas to produce 2 moles of ammonia. It does NOT mean 1 gram of \(N_2\) reacts with 3 grams of \(H_2\). Converting to moles is the mandatory intermediate step for all stoichiometric predictions:</p>
      <ol>
        <li><strong>Step 1: Convert Reactant Mass to Moles:</strong> Divide starting mass by reactant molar mass (\(n_{\text{reactant}} = m / M\)).</li>
        <li><strong>Step 2: Apply Stoichiometric Molar Ratio:</strong> Multiply by the mole ratio from the balanced chemical coefficients (\(n_{\text{product}} = n_{\text{reactant}} \times \frac{\nu_{\text{product}}}{\nu_{\text{reactant}}}\)).</li>
        <li><strong>Step 3: Convert Product Moles to Desired Unit:</strong> Multiply product moles by its molar mass to obtain theoretical grams (\(m_{\text{product}} = n_{\text{product}} \times M_{\text{product}}\)), or by \(22.414\text{ L/mol}\) for gas volume.</li>
      </ol>

      <h2>5. Clinical and Pharmacological Applications of Moles</h2>
      <p>In medical biochemistry and clinical pharmacology, chemical amount is measured in millimoles (\(\text{mmol}\), \(10^{-3}\text{ mol}\)) or micromoles (\(\mu\text{mol}\), \(10^{-6}\text{ mol}\)):</p>
      <ul>
        <li><strong>Blood Electrolytes:</strong> Serum sodium (\(\text{Na}^+\)) is clinically reported internationally in millimoles per liter (\(\text{mmol/L}\)), where normal physiological concentration is \(135\text{ to }145\text{ mmol/L}\).</li>
        <li><strong>Serum Glucose:</strong> Normal fasting blood sugar is \(3.9\text{ to }5.6\text{ mmol/L}\) (equivalent to \(70\text{ to }100\text{ mg/dL}\) in US imperial reporting). To convert \(\text{mmol/L}\) glucose to \(\text{mg/dL}\), multiply by \(18.016\) (the molar mass of glucose divided by 10).</li>
        <li><strong>Receptor-Ligand Binding:</strong> Drug dissociation constants (\(K_d\)) and enzyme Michaelis constants (\(K_m\)) are expressed in nanomolar (\(\text{nM}\)) or micromolar (\(\mu\text{M}\)) concentrations to measure molecular affinity.</li>
      </ul>

      <h2>6. Step-by-Step Worked Engineering Case Studies</h2>

      <div class="worked-example-card">
        <h3>Case Study 1: Combustion Analysis and Carbon Dioxide Generation</h3>
        <p><strong>Scenario:</strong> A power station burns natural gas consisting predominantly of methane (\(\text{CH}_4\), molar mass \(M = 16.043\text{ g/mol}\)). If a turbine combusts \(50.0\text{ kilograms}\) of methane completely according to \(\text{CH}_4 + 2\text{O}_2 \to \text{CO}_2 + 2\text{H}_2\text{O}\), calculate the moles of methane burned, the number of molecules of \(\text{CO}_2\) emitted, and the volume of \(\text{CO}_2\) at STP in cubic meters.</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Calculate moles of methane consumed:</strong></p>
          $$m_{\text{CH}_4} = 50.0\text{ kg} = 50,000.0\text{ grams}$$
          $$n_{\text{CH}_4} = \frac{50,000.0\text{ g}}{16.043\text{ g/mol}} = 3116.62\text{ moles}$$

          <p><strong>Step 2: Determine moles of carbon dioxide produced:</strong></p>
          <p>From the stoichiometric ratio (\(1\text{ mol CH}_4 : 1\text{ mol CO}_2\)):</p>
          $$n_{\text{CO}_2} = n_{\text{CH}_4} = 3116.62\text{ moles}$$

          <p><strong>Step 3: Calculate total molecules of \(\text{CO}_2\) emitted using Avogadro's constant:</strong></p>
          $$N = n \times N_A = 3116.62\text{ mol} \times (6.02214 \times 10^{23}\text{ molecules/mol}) \approx 1.877 \times 10^{27}\text{ molecules}$$

          <p><strong>Step 4: Compute volume of \(\text{CO}_2\) at STP:</strong></p>
          $$V = 3116.62\text{ mol} \times 22.414\text{ L/mol} = 69,856\text{ Liters} = 69.86\text{ m}^3$$
          <p><strong>Result:</strong> Burning \(50.0\text{ kg}\) of methane generates \(3,117\text{ moles}\) of \(\text{CO}_2\), releasing \(1.88 \times 10^{27}\) individual greenhouse gas molecules and occupying \(69.86\text{ m}^3\) of gas at STP.</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Pharmacological Dosage and Molecular Quantification</h3>
        <p><strong>Scenario:</strong> An intravenous chemotherapy formulation contains \(250\text{ milligrams}\) of paclitaxel (\(\text{C}_{47}\text{H}_{51}\text{NO}_{14}\), molecular weight \(M = 853.91\text{ g/mol}\)). Calculate the exact amount of drug in micromoles (\(\mu\text{mol}\)) and the total number of active paclitaxel molecules administered to the patient.</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Convert sample mass to grams:</strong></p>
          $$m = 250\text{ mg} = 0.250\text{ grams}$$

          <p><strong>Step 2: Calculate moles of paclitaxel:</strong></p>
          $$n = \frac{0.250\text{ g}}{853.91\text{ g/mol}} = 0.00029277\text{ moles} = 2.928 \times 10^{-4}\text{ mol}$$

          <p><strong>Step 3: Express in micromoles (\(\mu\text{mol}\)):</strong></p>
          $$n_{\mu\text{mol}} = 0.00029277 \times 10^6 = 292.8\text{ }\mu\text{mol}$$

          <p><strong>Step 4: Calculate total molecule population:</strong></p>
          $$N = n \times N_A = (2.9277 \times 10^{-4}\text{ mol}) \times (6.02214 \times 10^{23}\text{ molecules/mol}) \approx 1.763 \times 10^{20}\text{ molecules}$$
          <p><strong>Clinical Result:</strong> The patient receives \(292.8\text{ }\mu\text{mol}\) of drug, delivering approximately \(1.76 \times 10^{20}\) cytotoxic molecules into systemic circulation.</p>
        </div>
      </div>

      <h2>7. Frequently Asked Questions (Stoichiometry &amp; Atomic Physics)</h2>
      <div class="faq-accordion">
        <details class="faq-item">
          <summary>Why is Avogadro's number such a large value?</summary>
          <div class="faq-answer">
            <p>Individual atoms and molecules have unimaginably small masses. A single water molecule weighs only about \(2.99 \times 10^{-23}\text{ grams}\). To assemble enough of these microscopic particles into an ordinary, measurable macroscopic quantity that humans can weigh on a laboratory scale (such as 18 grams of water in a small sip), you must aggregate an enormous quantity of entities—specifically, \(6.022 \times 10^{23}\) particles.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>Does one mole of lead weigh the same as one mole of helium?</summary>
          <div class="faq-answer">
            <p>No. Both contain the exact same number of atoms (\(6.022 \times 10^{23}\)), but lead atoms have 82 protons and about 125 neutrons, making each lead atom roughly 52 times heavier than a helium atom (2 protons, 2 neutrons). Therefore, 1 mole of lead weighs 207.2 grams, whereas 1 mole of helium weighs only 4.003 grams.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>What is the difference between atomic weight, molecular weight, and formula weight?</summary>
          <div class="faq-answer">
            <p>Atomic weight refers to the weighted average mass of an individual chemical element across its natural isotopes (e.g., Fe = 55.845 g/mol). Molecular weight refers to discrete covalently bonded molecules (e.g., H2O = 18.015 g/mol). Formula weight is used for non-molecular ionic crystal lattices (e.g., NaCl = 58.44 g/mol) where distinct isolated molecules do not exist in the solid state. All three share the identical numerical units of g/mol.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>How does temperature and pressure alter the molar volume of a gas?</summary>
          <div class="faq-answer">
            <p>The standard value of 22.414 L/mol applies strictly at STP (0°C, 1 atm). If temperature rises or pressure drops, the volume occupied by one mole expands according to the Ideal Gas Law: \(V_m = RT / P\). At room temperature and pressure (25°C or 298.15 K, and 1 atm), one mole of gas occupies 24.465 liters.</p>
          </div>
        </details>
      </div>

      <h2>8. Related Chemical Calculation Engines</h2>
      <p>Explore our integrated chemistry and stoichiometry suite to solve solution concentrations and reaction yields:</p>
      <div class="related-calculators" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-top: 1rem;">
        <a href="molar-mass-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Molar Mass Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Determine chemical formula weights and elemental mass percentages.</p>
        </a>
        <a href="molarity-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Molarity Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Calculate volumetric solution concentration ($M = n/V$) in moles per liter.</p>
        </a>
        <a href="molality-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Molality Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Compute temperature-independent molality ($m = n/m_{\text{kg}}$) and cryoscopy.</p>
        </a>
        <a href="ideal-gas-law-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Ideal Gas Law Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Solve $PV = nRT$ across pressure, volume, temperature, and moles.</p>
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
          <li><a href="moles-calculator.html">Moles Calculator</a></li>
          <li><a href="molar-mass-calculator.html">Molar Mass</a></li>
          <li><a href="molality-calculator.html">Molality Calculator</a></li>
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
      const modeSelect = document.getElementById('mol-mode');
      const presetSelect = document.getElementById('mol-sub-preset');
      const mwInput = document.getElementById('mol-mw-input');

      const massPanel = document.getElementById('mol-input-mass-panel');
      const molesPanel = document.getElementById('mol-input-moles-panel');
      const particlesPanel = document.getElementById('mol-input-particles-panel');
      const gasPanel = document.getElementById('mol-input-gas-panel');

      const massValInput = document.getElementById('mol-mass-val');
      const massUnitSelect = document.getElementById('mol-mass-unit');
      const molesValInput = document.getElementById('mol-moles-val');
      const partCoeffInput = document.getElementById('mol-part-coeff');
      const partExpInput = document.getElementById('mol-part-exp');
      const gasVolInput = document.getElementById('mol-gas-vol');
      const gasUnitSelect = document.getElementById('mol-gas-unit');

      const calcBtn = document.getElementById('mol-calc-btn');
      const resetBtn = document.getElementById('mol-reset-btn');

      // Outputs
      const primaryOut = document.getElementById('mol-primary-out');
      const statusOut = document.getElementById('mol-status-out');
      const massOut = document.getElementById('mol-mass-out');
      const particlesOut = document.getElementById('mol-particles-out');
      const gasOut = document.getElementById('mol-gas-out');
      const mmolOut = document.getElementById('mol-mmol-out');

      const NA = 6.02214076e23;
      const VM_STP = 22.413962; // Liters per mole

      const PRESETS = {
        'water': 18.015,
        'co2': 44.010,
        'nacl': 58.443,
        'glucose': 180.156,
        'o2': 31.999,
        'n2': 28.013,
        'caco3': 100.087,
        'h2so4': 98.079,
        'ch4': 16.043,
        'c2h5oh': 46.068
      };

      const UNIT_TO_GRAMS = {
        'g': 1.0,
        'mg': 0.001,
        'kg': 1000.0,
        'oz': 28.349523,
        'lb': 453.59237
      };

      function updatePanelVisibility() {
        const m = modeSelect.value;
        massPanel.style.display = m === 'mass-to-moles' ? 'block' : 'none';
        molesPanel.style.display = m === 'moles-to-mass' ? 'block' : 'none';
        particlesPanel.style.display = m === 'particles-to-moles' ? 'block' : 'none';
        gasPanel.style.display = m === 'gas-to-moles' ? 'block' : 'none';
      }

      function formatSci(num) {
        if (num === 0) return "0";
        const exp = Math.floor(Math.log10(Math.abs(num)));
        const coeff = num / Math.pow(10, exp);
        return coeff.toFixed(3) + " \u00d7 10" + toSuperscript(exp);
      }

      function toSuperscript(n) {
        const map = { '-': '\u207B', '0': '\u2070', '1': '\u00B9', '2': '\u00B2', '3': '\u00B3', '4': '\u2074', '5': '\u2075', '6': '\u2076', '7': '\u2077', '8': '\u2078', '9': '\u2079' };
        return String(n).split('').map(c => map[c] || c).join('');
      }

      function calculate() {
        const mode = modeSelect.value;
        const mw = parseFloat(mwInput.value) || 18.015;
        let moles = 0;
        let massGrams = 0;

        if (mw <= 0) {
          primaryOut.textContent = "-- mol";
          statusOut.textContent = "Please enter a positive molar mass.";
          return;
        }

        if (mode === 'mass-to-moles') {
          const raw = parseFloat(massValInput.value) || 0;
          massGrams = raw * (UNIT_TO_GRAMS[massUnitSelect.value] || 1.0);
          if (massGrams <= 0) {
            primaryOut.textContent = "-- mol";
            statusOut.textContent = "Please enter a positive mass.";
            return;
          }
          moles = massGrams / mw;
        } else if (mode === 'moles-to-mass') {
          moles = parseFloat(molesValInput.value) || 0;
          if (moles <= 0) {
            primaryOut.textContent = "-- mol";
            statusOut.textContent = "Please enter positive moles.";
            return;
          }
          massGrams = moles * mw;
        } else if (mode === 'particles-to-moles') {
          const coeff = parseFloat(partCoeffInput.value) || 0;
          const exp = parseInt(partExpInput.value, 10) || 0;
          const particles = coeff * Math.pow(10, exp);
          if (particles <= 0) {
            primaryOut.textContent = "-- mol";
            statusOut.textContent = "Please enter positive particle count.";
            return;
          }
          moles = particles / NA;
          massGrams = moles * mw;
        } else if (mode === 'gas-to-moles') {
          const volRaw = parseFloat(gasVolInput.value) || 0;
          const u = gasUnitSelect.value;
          let volL = volRaw;
          if (u === 'mL') volL = volRaw * 0.001;
          if (u === 'm3') volL = volRaw * 1000.0;
          if (volL <= 0) {
            primaryOut.textContent = "-- mol";
            statusOut.textContent = "Please enter positive gas volume.";
            return;
          }
          moles = volL / VM_STP;
          massGrams = moles * mw;
        }

        const totalParticles = moles * NA;
        const gasLitersSTP = moles * VM_STP;
        const mmol = moles * 1000;

        // Render Outputs
        primaryOut.textContent = moles.toFixed(4) + " mol";
        statusOut.textContent = `${massGrams.toFixed(2)} g at ${mw.toFixed(3)} g/mol`;
        massOut.textContent = massGrams >= 1000 ? (massGrams / 1000).toFixed(3) + " kg" : massGrams.toFixed(2) + " g";
        particlesOut.textContent = formatSci(totalParticles);
        gasOut.textContent = gasLitersSTP.toFixed(2) + " L";
        mmolOut.textContent = mmol >= 10000 ? mmol.toExponential(3) + " mmol" : mmol.toFixed(1) + " mmol";
      }

      // Preset Change
      presetSelect.addEventListener('change', function() {
        const val = this.value;
        if (PRESETS[val]) {
          mwInput.value = PRESETS[val];
          calculate();
        }
      });

      modeSelect.addEventListener('change', function() {
        updatePanelVisibility();
        calculate();
      });

      [mwInput, massValInput, massUnitSelect, molesValInput, partCoeffInput, partExpInput, gasVolInput, gasUnitSelect].forEach(el => {
        el.addEventListener('input', function() {
          if (el === mwInput) presetSelect.value = 'custom';
          calculate();
        });
        el.addEventListener('change', calculate);
      });

      calcBtn.addEventListener('click', calculate);

      resetBtn.addEventListener('click', function() {
        modeSelect.value = 'mass-to-moles';
        presetSelect.value = 'water';
        mwInput.value = '18.015';
        massValInput.value = '100.0';
        massUnitSelect.value = 'g';
        molesValInput.value = '1.0';
        partCoeffInput.value = '6.022';
        partExpInput.value = '23';
        gasVolInput.value = '22.414';
        gasUnitSelect.value = 'L';
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

# 4. normality-calculator.html
HTML_NORMALITY = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Normality Calculator - Chemical Equivalent Concentration (N = M * n)</title>
  <meta name="description" content="Calculate normality (N = M * n_eq), equivalent weight (EW = M/n), acid-base titration dilution (N1V1 = N2V2), and redox equivalents in analytical chemistry.">
  <link rel="canonical" href="https://calchub.org/normality-calculator.html">
  <meta property="og:title" content="Normality Calculator - Equivalent Concentration &amp; Titration Solver">
  <meta property="og:description" content="Free chemistry normality calculator. Compute normality N = M * n, equivalent mass, acid-base neutralization N1V1 = N2V2, and redox equivalents with step-by-step proofs.">
  <meta property="og:url" content="https://calchub.org/normality-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Normality Calculator - Analytical Chemistry Tool">
  <meta name="twitter:description" content="Solve normality, equivalents per liter, and volumetric titrations across acids, bases, and redox reagents with worked case studies.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Normality Calculator",
    "url": "https://calchub.org/normality-calculator.html",
    "description": "Calculates solution normality (N = equivalents / Liter), equivalent weights, and volumetric titration neutralizations.",
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
        "name": "What is the relationship between normality and molarity?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Normality (N) equals molarity (M) multiplied by the equivalence factor (n_eq): N = M * n_eq. For monoprotic acids like HCl (n = 1), 1 M = 1 N. For diprotic acids like H2SO4 (n = 2), 1 M = 2 N. For triprotic acids like H3PO4 (n = 3), 1 M = 3 N."
        }
      },
      {
        "@type": "Question",
        "name": "How is equivalent weight (EW) calculated?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Equivalent weight is calculated by dividing the compound's molar mass (M) by its valence or equivalence factor (n_eq): EW = Molar Mass / n_eq. For sulfuric acid (H2SO4, M = 98.08 g/mol, n = 2), EW = 98.08 / 2 = 49.04 g/equivalent."
        }
      },
      {
        "@type": "Question",
        "name": "What is the titration neutralization formula using normality?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "At the equivalence point of any volumetric titration, the number of equivalents of acid exactly equals the number of equivalents of base: N1 * V1 = N2 * V2, where N1 and V1 are the normality and volume of solution 1, and N2 and V2 are the normality and volume of solution 2."
        }
      },
      {
        "@type": "Question",
        "name": "What is the equivalence factor for redox reactions?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "In oxidation-reduction (redox) reactions, the equivalence factor (n) is the number of moles of electrons gained or lost per mole of reactant in the balanced half-reaction. For example, in acidic permanganate titrations (MnO4- + 5e- -> Mn2+), n = 5; thus a 1 M KMnO4 solution is 5 N."
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
      <span>Normality Calculator</span>
    </nav>

    <div class="page-header">
      <h1 class="page-title">Normality Calculator</h1>
      <p class="page-desc">Calculate chemical normality ($N = M \times n_{\text{eq}}$), gram equivalent weights, and volumetric titration neutralizations ($N_1 V_1 = N_2 V_2$).</p>
    </div>

    <div class="calc-grid">
      <!-- Calculator Column -->
      <div class="calc-card">
        <div class="calc-header">
          <h2>Normality &amp; Equivalents Solver</h2>
        </div>

        <!-- Mode Selection -->
        <div class="form-group">
          <label for="norm-mode">Calculation Mode:</label>
          <select id="norm-mode" class="form-control">
            <option value="molarity-to-norm" selected>From Molarity ($M$) &amp; Equivalence Factor ($n_{\text{eq}}$) &rarr; Normality ($N$)</option>
            <option value="mass-to-norm">From Solute Mass ($m$), Molar Mass ($M$) &amp; Volume ($V$) &rarr; Normality</option>
            <option value="titration">Titration Neutralization ($N_1 V_1 = N_2 V_2$)</option>
          </select>
        </div>

        <!-- Chemical Preset -->
        <div class="form-group" id="norm-preset-group">
          <label for="norm-preset">Common Chemical Reagent Preset:</label>
          <select id="norm-preset" class="form-control">
            <option value="custom">-- Custom Chemical Formula --</option>
            <option value="hcl" selected>Hydrochloric Acid (HCl: M = 36.46 g/mol, n = 1 eq/mol)</option>
            <option value="h2so4">Sulfuric Acid (H2SO4: M = 98.08 g/mol, n = 2 eq/mol)</option>
            <option value="h3po4">Phosphoric Acid (H3PO4: M = 98.00 g/mol, n = 3 eq/mol)</option>
            <option value="naoh">Sodium Hydroxide (NaOH: M = 40.00 g/mol, n = 1 eq/mol)</option>
            <option value="caoh2">Calcium Hydroxide (Ca(OH)2: M = 74.09 g/mol, n = 2 eq/mol)</option>
            <option value="kmno4-acid">Potassium Permanganate (KMnO4 acidic: M = 158.03, n = 5 e-)</option>
            <option value="k2cr2o7">Potassium Dichromate (K2Cr2O7 acidic: M = 294.18, n = 6 e-)</option>
            <option value="na2co3">Sodium Carbonate (Na2CO3: M = 105.99 g/mol, n = 2 eq/mol)</option>
            <option value="oxalic">Oxalic Acid Dihydrate (H2C2O4·2H2O: M = 126.07, n = 2)</option>
          </select>
        </div>

        <!-- Inputs Container -->
        <div id="norm-molarity-panel">
          <div class="form-row">
            <div class="form-group">
              <label for="norm-molarity-val">Molar Concentration ($M$ in mol/L):</label>
              <input type="number" id="norm-molarity-val" class="form-control" value="1.0" step="any" min="0.0001">
            </div>
            <div class="form-group">
              <label for="norm-neq-val">Equivalence Factor ($n_{\text{eq}}$):</label>
              <input type="number" id="norm-neq-val" class="form-control" value="1" step="1" min="1" max="10">
            </div>
          </div>
        </div>

        <div id="norm-mass-panel" style="display: none;">
          <div class="form-row">
            <div class="form-group">
              <label for="norm-solute-mass">Solute Mass ($m$ in grams):</label>
              <input type="number" id="norm-solute-mass" class="form-control" value="49.04" step="any" min="0.0001">
            </div>
            <div class="form-group">
              <label for="norm-mw-val">Molar Mass ($M$ in g/mol):</label>
              <input type="number" id="norm-mw-val" class="form-control" value="98.079" step="any" min="0.01">
            </div>
          </div>
          <div class="form-row">
            <div class="form-group">
              <label for="norm-neq-mass">Equivalence Factor ($n_{\text{eq}}$):</label>
              <input type="number" id="norm-neq-mass" class="form-control" value="2" step="1" min="1" max="10">
            </div>
            <div class="form-group">
              <label for="norm-vol-val">Total Volume ($V$ in Liters):</label>
              <input type="number" id="norm-vol-val" class="form-control" value="1.0" step="any" min="0.0001">
            </div>
          </div>
        </div>

        <div id="norm-titration-panel" style="display: none;">
          <div class="form-row">
            <div class="form-group">
              <label for="titr-n1">Reagent 1 Normality ($N_1$):</label>
              <input type="number" id="titr-n1" class="form-control" value="0.100" step="any" min="0.0001">
            </div>
            <div class="form-group">
              <label for="titr-v1">Reagent 1 Volume ($V_1$ in mL):</label>
              <input type="number" id="titr-v1" class="form-control" value="25.0" step="any" min="0.0001">
            </div>
          </div>
          <div class="form-row">
            <div class="form-group">
              <label for="titr-solve-for">Solve For:</label>
              <select id="titr-solve-for" class="form-control">
                <option value="n2" selected>Reagent 2 Normality (N2)</option>
                <option value="v2">Reagent 2 Volume (V2 in mL)</option>
              </select>
            </div>
            <div class="form-group" id="titr-v2-group">
              <label for="titr-v2">Reagent 2 Titrated Volume ($V_2$ in mL):</label>
              <input type="number" id="titr-v2" class="form-control" value="20.0" step="any" min="0.0001">
            </div>
            <div class="form-group" id="titr-n2-group" style="display: none;">
              <label for="titr-n2">Reagent 2 Known Normality ($N_2$):</label>
              <input type="number" id="titr-n2" class="form-control" value="0.125" step="any" min="0.0001">
            </div>
          </div>
        </div>

        <div class="form-actions">
          <button type="button" id="norm-calc-btn" class="btn btn-primary">Calculate Normality</button>
          <button type="button" id="norm-reset-btn" class="btn btn-secondary">Reset to Default</button>
        </div>

        <!-- Output Hero and Cards -->
        <div id="norm-results" class="results-container" style="margin-top: 1.5rem;">
          <div class="result-hero-card">
            <div class="result-label" style="font-size: 0.875rem; color: var(--text-muted, #64748b); text-transform: uppercase; font-weight: 600;">Solution Normality ($N$)</div>
            <div id="norm-primary-out" style="font-size: 2.25rem; font-weight: 800; color: var(--primary, #2563eb); margin: 0.25rem 0;">1.000 N</div>
            <div id="norm-status-out" style="font-size: 1rem; color: var(--text-secondary, #475569); font-weight: 600;">1.000 equivalents per liter</div>
          </div>

          <div class="summary-metrics-grid">
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Molarity ($M$)</div>
              <div id="norm-molarity-out" style="font-size: 1.15rem; font-weight: 700;">1.000 M</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Equivalent Weight ($EW$)</div>
              <div id="norm-ew-out" style="font-size: 1.15rem; font-weight: 700;">36.46 g/eq</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Equivalents Factor ($n_{\text{eq}}$)</div>
              <div id="norm-neq-out" style="font-size: 1.15rem; font-weight: 700;">1 eq/mol</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Mass per Liter (g/L)</div>
              <div id="norm-gpl-out" style="font-size: 1.15rem; font-weight: 700;">36.46 g/L</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Reference Sidebar -->
      <aside class="sidebar-card">
        <h3>Common Equivalence Factors ($n_{\text{eq}}$)</h3>
        <p style="font-size: 0.875rem; color: var(--text-secondary, #475569);">Valence factor based on reaction mechanism:</p>
        <ul style="font-size: 0.875rem; line-height: 1.6; margin-left: 1.25rem;">
          <li><strong>Hydrochloric Acid (HCl):</strong> \(n = 1\)</li>
          <li><strong>Nitric Acid (HNO₃):</strong> \(n = 1\)</li>
          <li><strong>Sulfuric Acid (H₂SO₄):</strong> \(n = 2\)</li>
          <li><strong>Phosphoric Acid (H₃PO₄):</strong> \(n = 3\)</li>
          <li><strong>Sodium Hydroxide (NaOH):</strong> \(n = 1\)</li>
          <li><strong>Calcium Hydroxide (Ca(OH)₂):</strong> \(n = 2\)</li>
          <li><strong>KMnO₄ (Acidic Medium):</strong> \(n = 5\) (redox)</li>
          <li><strong>K₂Cr₂O₇ (Acidic Medium):</strong> \(n = 6\) (redox)</li>
        </ul>

        <h3 style="margin-top: 1.25rem;">Normality Formulas</h3>
        <ul style="font-size: 0.875rem; line-height: 1.6; margin-left: 1.25rem;">
          <li>\(N = M \times n_{\text{eq}}\)</li>
          <li>\(EW = \frac{M_{\text{molar}}}{n_{\text{eq}}}\)</li>
          <li>\(N = \frac{m / EW}{V_{\text{liters}}}\)</li>
          <li>\(N_1 V_1 = N_2 V_2\)</li>
        </ul>
      </aside>
    </div>

    <!-- Long-Form Informational Engineering Article (1,400+ Words) -->
    <article class="article-body">
      <h2>1. The Definition and Theoretical Role of Normality in Chemistry</h2>
      <p>Normality (designated by the capital letter \(N\)), also termed **equivalent concentration**, is a measure of concentration in analytical chemistry defined as the number of gram equivalents (equivalents, \(\text{eq}\)) of a reactive solute contained in one liter of finished solution. Formally:</p>
      $$\text{Normality } (N) = \frac{\text{Equivalents of Solute}}{\text{Volume of Solution in Liters}} = \frac{n_{\text{eq, total}}}{V_{\text{solution (L)}}}$$
      <p>While molarity (\(M = \text{mol/L}\)) counts the total chemical molecules or formula units in solution regardless of their functional reactivity, normality specifically counts the reactive capacity of the solute based on the specific type of chemical transformation taking place. Consequently, a single chemical substance can possess multiple different normalities depending on the target reaction medium.</p>
      <p>The universal mathematical bridge linking normality directly to molarity is:</p>
      $$N = M \times n_{\text{eq}}$$
      <p>Where \(M\) is the molar concentration (\(\text{mol/L}\)), and \(n_{\text{eq}}\) is the dimensionless **equivalence factor** (valence factor or stoichiometric reactive capacity, in equivalents per mole, \(\text{eq/mol}\)).</p>

      <h2>2. Determining the Equivalence Factor (\(n_{\text{eq}}\)) Across Reaction Types</h2>
      <p>The value of \(n_{\text{eq}}\) depends fundamentally on the reaction category:</p>

      <h3>A. Acid-Base Reactions (Proton Exchange)</h3>
      <p>For acids, \(n_{\text{eq}}\) equals the number of ionizable, dissociable hydronium protons (\(\text{H}^+\)) that one molecule of the acid can donate to a base. For bases, \(n_{\text{eq}}\) equals the number of hydroxide ions (\(\text{OH}^-\)) it can supply, or the number of protons it can accept:</p>
      <ul>
        <li><strong>Monoprotic Acids (\(n = 1\)):</strong> Hydrochloric acid (\(\text{HCl}\)), nitric acid (\(\text{HNO}_3\)), and acetic acid (\(\text{CH}_3\text{COOH}\)) each donate exactly 1 proton:
        $$\text{HCl} \to \text{H}^+ + \text{Cl}^- \implies 1.0\text{ M HCl} = 1.0\text{ N HCl}$$</li>
        <li><strong>Diprotic Acids (\(n = 2\)):</strong> Sulfuric acid (\(\text{H}_2\text{SO}_4\)) and oxalic acid (\(\text{H}_2\text{C}_2\text{O}_4\)) donate 2 protons:
        $$\text{H}_2\text{SO}_4 \to 2\text{H}^+ + \text{SO}_4^{2-} \implies 1.0\text{ M H}_2\text{SO}_4 = 2.0\text{ N H}_2\text{SO}_4$$</li>
        <li><strong>Triprotic Acids (\(n = 3\)):</strong> Phosphoric acid (\(\text{H}_3\text{PO}_4\)) donates up to 3 protons:
        $$\text{H}_3\text{PO}_4 \to 3\text{H}^+ + \text{PO}_4^{3-} \implies 1.0\text{ M H}_3\text{PO}_4 = 3.0\text{ N H}_3\text{PO}_4$$</li>
        <li><strong>Hydroxide Bases:</strong> Sodium hydroxide (\(\text{NaOH}\), \(n=1\)) produces 1 eq/mol, whereas calcium hydroxide (\(\text{Ca(OH)}_2\), \(n=2\)) produces 2 eq/mol. Therefore, a \(0.5\text{ M Ca(OH)}_2\) solution is \(1.0\text{ N}\).</li>
      </ul>

      <h3>B. Oxidation-Reduction (Redox) Reactions (Electron Exchange)</h3>
      <p>In redox chemistry, \(n_{\text{eq}}\) equals the number of moles of electrons transferred (gained or lost) per mole of reagent according to the balanced half-reaction:</p>
      <ul>
        <li><strong>Potassium Permanganate in Acidic Medium (\(n = 5\)):</strong>
        $$\text{MnO}_4^- + 8\text{H}^+ + 5e^- \longrightarrow \text{Mn}^{2+} + 4\text{H}_2\text{O} \implies n = 5 \implies 1.0\text{ M KMnO}_4 = 5.0\text{ N}$$</li>
        <li><strong>Potassium Permanganate in Strongly Alkaline Medium (\(n = 1\)):</strong>
        $$\text{MnO}_4^- + e^- \longrightarrow \text{MnO}_4^{2-} \implies n = 1 \implies 1.0\text{ M KMnO}_4 = 1.0\text{ N}$$</li>
        <li><strong>Potassium Dichromate in Acidic Medium (\(n = 6\)):</strong>
        $$\text{Cr}_2\text{O}_7^{2-} + 14\text{H}^+ + 6e^- \longrightarrow 2\text{Cr}^{3+} + 7\text{H}_2\text{O} \implies n = 6 \implies 1.0\text{ M K}_2\text{Cr}_2\text{O}_7 = 6.0\text{ N}$$</li>
      </ul>

      <h3>C. Precipitation and Complexation Reactions (Ionic Charge)</h3>
      <p>For neutral salts involved in double-displacement or precipitation titrations, \(n_{\text{eq}}\) equals the total positive electrical charge (valence) of the cation present in the formula unit:</p>
      <ul>
        <li>Sodium chloride (\(\text{NaCl}\)): \(\text{Na}^+ \implies n = 1\).</li>
        <li>Calcium chloride (\(\text{CaCl}_2\)): \(\text{Ca}^{2+} \implies n = 2\).</li>
        <li>Aluminum sulfate (\(\text{Al}_2(\text{SO}_4)_3\)): Two \(\text{Al}^{3+}\) ions \(\implies n = 2 \times 3 = 6\). A \(1.0\text{ M Al}_2(\text{SO}_4)_3\) solution is \(6.0\text{ N}\).</li>
      </ul>

      <h2>3. Equivalent Weight (\(EW\)) and Mass Compounding</h2>
      <p>The equivalent weight (\(EW\), historically called gram equivalent) is the mass of a substance that will supply, consume, or react with exactly one mole of hydrogen ions (\(1.008\text{ g H}^+\)), one mole of electrons (\(6.022 \times 10^{23}\text{ electrons}\)), or one equivalent of any other reactant:</p>
      $$EW = \frac{\text{Molar Mass } (M)}{n_{\text{eq}}}$$
      <p>To compound \(V\) liters of an \(N\)-normal solution from pure dry solid reagent of known equivalent weight:</p>
      $$\text{Required Solute Mass } (m) = N \times V \times EW = N \times V \times \left(\frac{M}{n_{\text{eq}}}\right)$$

      <h2>4. The Universal Titration Equivalence Law (\(N_1 V_1 = N_2 V_2\))</h2>
      <p>The primary advantage of normality over molarity is the simplification of volumetric titration calculations. When using molarity, stoichiometric coefficients (\(a\text{A} + b\text{B} \to \text{Products}\)) require cross-multiplying mole ratios (\(M_1 V_1 / a = M_2 V_2 / b\)). In contrast, by definition, one equivalent of any acid reacts completely with exactly one equivalent of any base (or one equivalent of oxidizer with one equivalent of reducer). Therefore, at the titration stoichiometric endpoint:</p>
      $$\text{Equivalents of Analyte} = \text{Equivalents of Titrant}$$
      $$N_1 \times V_1 = N_2 \times V_2$$
      <p>Where \(N_1\) and \(V_1\) are the normality and volume of the first reagent, and \(N_2\) and \(V_2\) are the normality and volume of the second reagent. This linear relation holds universally regardless of whether the acid is monoprotic, diprotic, or triprotic, eliminating balancing errors during routine laboratory assays.</p>

      <h2>5. Comprehensive Reagent Normality Reference Table</h2>
      <p>The following analytical chemistry benchmark table details molar masses, equivalence factors, and resulting equivalent weights for standardized volumetric reagents:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Reagent Name</th>
              <th>Formula</th>
              <th>Molar Mass (\(M\))</th>
              <th>Equivalence Factor (\(n_{\text{eq}}\))</th>
              <th>Equivalent Weight (\(EW\))</th>
              <th>Mass to Prepare 1.0 L of 1.0 N Solution</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Hydrochloric Acid</td>
              <td>HCl</td>
              <td>36.46 g/mol</td>
              <td>1 eq/mol (acid)</td>
              <td>36.46 g/eq</td>
              <td>36.46 g</td>
            </tr>
            <tr>
              <td>Nitric Acid</td>
              <td>HNO₃</td>
              <td>63.01 g/mol</td>
              <td>1 eq/mol (acid)</td>
              <td>63.01 g/eq</td>
              <td>63.01 g</td>
            </tr>
            <tr>
              <td>Sulfuric Acid</td>
              <td>H₂SO₄</td>
              <td>98.08 g/mol</td>
              <td>2 eq/mol (acid)</td>
              <td>49.04 g/eq</td>
              <td>49.04 g</td>
            </tr>
            <tr>
              <td>Phosphoric Acid</td>
              <td>H₃PO₄</td>
              <td>98.00 g/mol</td>
              <td>3 eq/mol (acid)</td>
              <td>32.67 g/eq</td>
              <td>32.67 g</td>
            </tr>
            <tr>
              <td>Sodium Hydroxide</td>
              <td>NaOH</td>
              <td>40.00 g/mol</td>
              <td>1 eq/mol (base)</td>
              <td>40.00 g/eq</td>
              <td>40.00 g</td>
            </tr>
            <tr>
              <td>Potassium Hydroxide</td>
              <td>KOH</td>
              <td>56.11 g/mol</td>
              <td>1 eq/mol (base)</td>
              <td>56.11 g/eq</td>
              <td>56.11 g</td>
            </tr>
            <tr>
              <td>Calcium Hydroxide</td>
              <td>Ca(OH)₂</td>
              <td>74.09 g/mol</td>
              <td>2 eq/mol (base)</td>
              <td>37.05 g/eq</td>
              <td>37.05 g</td>
            </tr>
            <tr>
              <td>Oxalic Acid Dihydrate</td>
              <td>H₂C₂O₄·2H₂O</td>
              <td>126.07 g/mol</td>
              <td>2 eq/mol (acid)</td>
              <td>63.03 g/eq</td>
              <td>63.03 g</td>
            </tr>
            <tr>
              <td>Potassium Permanganate</td>
              <td>KMnO₄ (acidic)</td>
              <td>158.03 g/mol</td>
              <td>5 e⁻ (redox)</td>
              <td>31.61 g/eq</td>
              <td>31.61 g</td>
            </tr>
            <tr>
              <td>Potassium Dichromate</td>
              <td>K₂Cr₂O₇ (acidic)</td>
              <td>294.18 g/mol</td>
              <td>6 e⁻ (redox)</td>
              <td>49.03 g/eq</td>
              <td>49.03 g</td>
            </tr>
            <tr>
              <td>Sodium Thiosulfate Pentahydrate</td>
              <td>Na₂S₂O₃·5H₂O</td>
              <td>248.18 g/mol</td>
              <td>1 e⁻ (iodometry)</td>
              <td>248.18 g/eq</td>
              <td>248.18 g</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>6. Step-by-Step Worked Analytical Case Studies</h2>

      <div class="worked-example-card">
        <h3>Case Study 1: Standardizing Industrial Hydrochloric Acid via NaOH Titration</h3>
        <p><strong>Scenario:</strong> An environmental water quality technician titrates an unknown wastewater stream containing hydrochloric acid (\(\text{HCl}\)). A \(25.0\text{ mL}\) sample of the acid requires exactly \(31.25\text{ mL}\) of standardized \(0.1040\text{ N}\) sodium hydroxide (\(\text{NaOH}\)) to reach the phenolphthalein end point. Calculate the exact normality and molarity of the acid sample.</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Identify titration parameters:</strong></p>
          <ul>
            <li>Volume of acid sample \(V_1 = 25.0\text{ mL}\)</li>
            <li>Normality of titrant base \(N_2 = 0.1040\text{ N}\)</li>
            <li>Titrated volume of base \(V_2 = 31.25\text{ mL}\)</li>
          </ul>

          <p><strong>Step 2: Apply the universal titration equation (\(N_1 V_1 = N_2 V_2\)):</strong></p>
          $$N_1 \times 25.0\text{ mL} = 0.1040\text{ N} \times 31.25\text{ mL}$$
          $$N_1 = \frac{0.1040 \times 31.25}{25.0} = \frac{3.250}{25.0} = 0.1300\text{ N}$$

          <p><strong>Step 3: Convert normality to molarity:</strong></p>
          <p>Since \(\text{HCl}\) is monoprotic (\(n_{\text{eq}} = 1\)):</p>
          $$M = \frac{N}{n_{\text{eq}}} = \frac{0.1300\text{ N}}{1} = 0.1300\text{ M}$$

          <p><strong>Step 4: Compute concentration in grams per liter:</strong></p>
          $$C = M \times M_{\text{HCl}} = 0.1300\text{ mol/L} \times 36.46\text{ g/mol} = 4.740\text{ g/L}$$
          <p><strong>Conclusion:</strong> The wastewater acid concentration is \(0.1300\text{ N}\) (\(0.1300\text{ M}\)), containing \(4.74\text{ g/L}\) of dissolved \(\text{HCl}\).</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Preparing Standard 0.0500 N Potassium Permanganate Redox Solution</h3>
        <p><strong>Scenario:</strong> A laboratory chemist needs to prepare \(2.00\text{ Liters}\) of standard \(0.0500\text{ N}\) potassium permanganate (\(\text{KMnO}_4\)) solution for iron ore titrations in dilute sulfuric acid. The molar mass of \(\text{KMnO}_4\) is \(158.034\text{ g/mol}\). Compute the required mass of pure analytical-grade \(\text{KMnO}_4\) crystals.</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Determine the redox equivalence factor (\(n_{\text{eq}}\)):</strong></p>
          <p>In acidic iron assays, permanganate is reduced to manganese(II):</p>
          $$\text{MnO}_4^- + 8\text{H}^+ + 5e^- \longrightarrow \text{Mn}^{2+} + 4\text{H}_2\text{O} \implies n_{\text{eq}} = 5\text{ eq/mol}$$

          <p><strong>Step 2: Calculate equivalent weight (\(EW\)):</strong></p>
          $$EW = \frac{M}{n_{\text{eq}}} = \frac{158.034\text{ g/mol}}{5} = 31.6068\text{ g/equivalent}$$

          <p><strong>Step 3: Calculate required mass of reagent:</strong></p>
          $$m = N \times V \times EW = 0.0500\text{ eq/L} \times 2.00\text{ L} \times 31.6068\text{ g/eq}$$
          $$m = 0.1000\text{ eq} \times 31.6068\text{ g/eq} = 3.1607\text{ grams}$$

          <p><strong>Step 4: Verify solution molarity:</strong></p>
          $$M = \frac{N}{n_{\text{eq}}} = \frac{0.0500\text{ N}}{5} = 0.0100\text{ M (mol/L)}$$
          <p><strong>Preparation Protocol:</strong> Dissolve exactly \(3.161\text{ grams}\) of pure \(\text{KMnO}_4\) crystals into deionized water and dilute to the calibration mark in a \(2.00\text{-L}\) volumetric flask.</p>
        </div>
      </div>

      <h2>7. Frequently Asked Questions (Analytical Titrations &amp; Standards)</h2>
      <div class="faq-accordion">
        <details class="faq-item">
          <summary>Why is normality declining in modern IUPAC publications?</summary>
          <div class="faq-answer">
            <p>IUPAC and modern physical chemistry textbooks increasingly discourage the standalone use of normality because it is ambiguous without specifying the reaction context. For example, a 1 M KMnO4 solution can be 5 N, 3 N, or 1 N depending on solution pH. To prevent catastrophic dosage or analytical errors, modern standards recommend reporting molarity (which is an unambiguous property of the solution) and explicitly stating the reaction equation.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>Can normality ever be lower than molarity?</summary>
          <div class="faq-answer">
            <p>No. By definition, the equivalence factor \(n_{\text{eq}}\) is an integer greater than or equal to 1 (\(n_{\text{eq}} \ge 1\)). Because \(N = M \times n_{\text{eq}}\), normality is always greater than or equal to molarity (\(N \ge M\)). Normality equals molarity only when \(n_{\text{eq}} = 1\) (such as in monoprotic acids or univalent salts).</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>Does normality change if a solution is diluted with pure water?</summary>
          <div class="faq-answer">
            <p>Yes. Diluting a solution increases total volume while keeping the number of equivalents constant. Like molarity, normality is inversely proportional to volume: \(N_{\text{new}} = N_{\text{old}} \times (V_{\text{old}} / V_{\text{new}})\). Adding water decreases the normality proportionately.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>What is a primary standard in volumetric analysis?</summary>
          <div class="faq-answer">
            <p>A primary standard is a reagent that is extremely pure (typically > 99.9%), stable in air, non-hygroscopic, and has a high equivalent weight to minimize balance weighing errors. Examples include anhydrous sodium carbonate (Na2CO3) for standardizing acids, potassium hydrogen phthalate (KHP) for standardizing bases, and potassium dichromate (K2Cr2O7) for redox titrations.</p>
          </div>
        </details>
      </div>

      <h2>8. Related Analytical Chemistry Calculators</h2>
      <p>Explore our integrated chemical calculation engines to solve dilutions, molar masses, and acid-base equilibria:</p>
      <div class="related-calculators" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-top: 1rem;">
        <a href="molarity-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Molarity Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Compute molar concentration ($M = n/V$) from solute formula weight.</p>
        </a>
        <a href="dilution-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Dilution Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Solve $C_1 V_1 = C_2 V_2$ for laboratory serial dilutions and buffer compounding.</p>
        </a>
        <a href="moles-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Moles Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Convert between grams, chemical moles, and particle populations.</p>
        </a>
        <a href="ph-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">pH Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Compute solution hydronium activity ($-\log[H^+]$) and pOH values.</p>
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
          <li><a href="normality-calculator.html">Normality Calculator</a></li>
          <li><a href="molarity-calculator.html">Molarity Calculator</a></li>
          <li><a href="dilution-calculator.html">Dilution (C1V1 = C2V2)</a></li>
          <li><a href="moles-calculator.html">Moles Calculator</a></li>
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
      const modeSelect = document.getElementById('norm-mode');
      const presetGroup = document.getElementById('norm-preset-group');
      const presetSelect = document.getElementById('norm-preset');

      const molarityPanel = document.getElementById('norm-molarity-panel');
      const massPanel = document.getElementById('norm-mass-panel');
      const titrationPanel = document.getElementById('norm-titration-panel');

      const molarityValInput = document.getElementById('norm-molarity-val');
      const neqValInput = document.getElementById('norm-neq-val');

      const soluteMassInput = document.getElementById('norm-solute-mass');
      const mwValInput = document.getElementById('norm-mw-val');
      const neqMassInput = document.getElementById('norm-neq-mass');
      const volValInput = document.getElementById('norm-vol-val');

      const titrN1Input = document.getElementById('titr-n1');
      const titrV1Input = document.getElementById('titr-v1');
      const titrSolveFor = document.getElementById('titr-solve-for');
      const titrV2Group = document.getElementById('titr-v2-group');
      const titrN2Group = document.getElementById('titr-n2-group');
      const titrV2Input = document.getElementById('titr-v2');
      const titrN2Input = document.getElementById('titr-n2');

      const calcBtn = document.getElementById('norm-calc-btn');
      const resetBtn = document.getElementById('norm-reset-btn');

      // Outputs
      const primaryOut = document.getElementById('norm-primary-out');
      const statusOut = document.getElementById('norm-status-out');
      const molarityOut = document.getElementById('norm-molarity-out');
      const ewOut = document.getElementById('norm-ew-out');
      const neqOut = document.getElementById('norm-neq-out');
      const gplOut = document.getElementById('norm-gpl-out');

      const PRESETS = {
        'hcl': { mw: 36.461, neq: 1 },
        'h2so4': { mw: 98.079, neq: 2 },
        'h3po4': { mw: 97.994, neq: 3 },
        'naoh': { mw: 39.997, neq: 1 },
        'caoh2': { mw: 74.093, neq: 2 },
        'kmno4-acid': { mw: 158.034, neq: 5 },
        'k2cr2o7': { mw: 294.185, neq: 6 },
        'na2co3': { mw: 105.988, neq: 2 },
        'oxalic': { mw: 126.066, neq: 2 }
      };

      function updatePanelVisibility() {
        const m = modeSelect.value;
        presetGroup.style.display = m === 'titration' ? 'none' : 'block';
        molarityPanel.style.display = m === 'molarity-to-norm' ? 'block' : 'none';
        massPanel.style.display = m === 'mass-to-norm' ? 'block' : 'none';
        titrationPanel.style.display = m === 'titration' ? 'block' : 'none';
      }

      function updateTitrationVisibility() {
        const solve = titrSolveFor.value;
        if (solve === 'n2') {
          titrV2Group.style.display = 'block';
          titrN2Group.style.display = 'none';
        } else {
          titrV2Group.style.display = 'none';
          titrN2Group.style.display = 'block';
        }
      }

      function calculate() {
        const mode = modeSelect.value;
        let normality = 0;
        let molarity = 0;
        let neq = 1;
        let ew = 0;
        let gpl = 0;

        if (mode === 'molarity-to-norm') {
          molarity = parseFloat(molarityValInput.value) || 0;
          neq = parseFloat(neqValInput.value) || 1;
          const mw = PRESETS[presetSelect.value] ? PRESETS[presetSelect.value].mw : 36.46;

          if (molarity <= 0 || neq <= 0) {
            primaryOut.textContent = "-- N";
            statusOut.textContent = "Please enter valid positive values.";
            return;
          }

          normality = molarity * neq;
          ew = mw / neq;
          gpl = molarity * mw;

          primaryOut.textContent = normality.toFixed(4) + " N";
          statusOut.textContent = `${normality.toFixed(4)} equivalents/L (${molarity.toFixed(4)} M)`;
        } else if (mode === 'mass-to-norm') {
          const mass = parseFloat(soluteMassInput.value) || 0;
          const mw = parseFloat(mwValInput.value) || 36.46;
          neq = parseFloat(neqMassInput.value) || 1;
          const vol = parseFloat(volValInput.value) || 1.0;

          if (mass <= 0 || mw <= 0 || neq <= 0 || vol <= 0) {
            primaryOut.textContent = "-- N";
            statusOut.textContent = "Please enter valid positive values.";
            return;
          }

          ew = mw / neq;
          const equivalents = mass / ew;
          normality = equivalents / vol;
          molarity = (mass / mw) / vol;
          gpl = mass / vol;

          primaryOut.textContent = normality.toFixed(4) + " N";
          statusOut.textContent = `${equivalents.toFixed(4)} eq in ${vol.toFixed(2)} L solution`;
        } else if (mode === 'titration') {
          const n1 = parseFloat(titrN1Input.value) || 0;
          const v1 = parseFloat(titrV1Input.value) || 0;
          const solve = titrSolveFor.value;

          if (n1 <= 0 || v1 <= 0) {
            primaryOut.textContent = "--";
            statusOut.textContent = "Please enter positive titration values.";
            return;
          }

          if (solve === 'n2') {
            const v2 = parseFloat(titrV2Input.value) || 0;
            if (v2 <= 0) {
              primaryOut.textContent = "--";
              statusOut.textContent = "Please enter positive volume V2.";
              return;
            }
            // N2 = (N1 * V1) / V2
            const n2 = (n1 * v1) / v2;
            normality = n2;
            primaryOut.textContent = n2.toFixed(4) + " N";
            statusOut.textContent = `N₂ = (${n1} N \u00d7 ${v1} mL) / ${v2} mL`;
          } else {
            const n2 = parseFloat(titrN2Input.value) || 0;
            if (n2 <= 0) {
              primaryOut.textContent = "--";
              statusOut.textContent = "Please enter positive normality N2.";
              return;
            }
            // V2 = (N1 * V1) / N2
            const v2 = (n1 * v1) / n2;
            normality = n2;
            primaryOut.textContent = v2.toFixed(2) + " mL";
            statusOut.textContent = `V₂ = (${n1} N \u00d7 ${v1} mL) / ${n2} N`;
          }

          molarity = normality; // nominal 1:1 fallback display
          ew = 0;
          gpl = 0;
        }

        // Render Cards
        molarityOut.textContent = molarity > 0 ? molarity.toFixed(4) + " M" : "--";
        ewOut.textContent = ew > 0 ? ew.toFixed(2) + " g/eq" : "--";
        neqOut.textContent = neq + " eq/mol";
        gplOut.textContent = gpl > 0 ? gpl.toFixed(2) + " g/L" : "--";
      }

      // Presets
      presetSelect.addEventListener('change', function() {
        const val = this.value;
        if (PRESETS[val]) {
          const p = PRESETS[val];
          neqValInput.value = p.neq;
          neqMassInput.value = p.neq;
          mwValInput.value = p.mw;
          calculate();
        }
      });

      modeSelect.addEventListener('change', function() {
        updatePanelVisibility();
        calculate();
      });

      titrSolveFor.addEventListener('change', function() {
        updateTitrationVisibility();
        calculate();
      });

      [molarityValInput, neqValInput, soluteMassInput, mwValInput, neqMassInput, volValInput, titrN1Input, titrV1Input, titrV2Input, titrN2Input].forEach(el => {
        el.addEventListener('input', function() {
          if (el === neqValInput || el === neqMassInput || el === mwValInput) presetSelect.value = 'custom';
          calculate();
        });
        el.addEventListener('change', calculate);
      });

      calcBtn.addEventListener('click', calculate);

      resetBtn.addEventListener('click', function() {
        modeSelect.value = 'molarity-to-norm';
        presetSelect.value = 'hcl';
        molarityValInput.value = '1.0';
        neqValInput.value = '1';
        soluteMassInput.value = '49.04';
        mwValInput.value = '98.079';
        neqMassInput.value = '2';
        volValInput.value = '1.0';
        titrN1Input.value = '0.100';
        titrV1Input.value = '25.0';
        titrSolveFor.value = 'n2';
        titrV2Input.value = '20.0';
        titrN2Input.value = '0.125';
        updatePanelVisibility();
        updateTitrationVisibility();
        calculate();
      });

      // Initial execution
      updatePanelVisibility();
      updateTitrationVisibility();
      calculate();
    })();
  </script>
</body>
</html>
"""

def generate_files():
    p1 = os.path.join(BASE_DIR, "moles-calculator.html")
    with open(p1, "w", encoding="utf-8") as f:
        f.write(HTML_MOLES.strip() + "\n")
    print(f"Generated: {p1}")

    p2 = os.path.join(BASE_DIR, "normality-calculator.html")
    with open(p2, "w", encoding="utf-8") as f:
        f.write(HTML_NORMALITY.strip() + "\n")
    print(f"Generated: {p2}")

if __name__ == "__main__":
    generate_files()
