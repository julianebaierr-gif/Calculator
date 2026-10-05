# -*- coding: utf-8 -*-
"""
Generator for Batch 34 - Part 1:
1. mass-percent-calculator.html
2. molality-calculator.html
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 1. mass-percent-calculator.html
HTML_MASS_PERCENT = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mass Percent Calculator - Percent by Mass (w/w%) &amp; Solution Concentration</title>
  <meta name="description" content="Calculate mass percent concentration (w/w% = m_solute / m_solution * 100%), solute mass, solvent mass, and alloy percentages with worked chemical proofs.">
  <link rel="canonical" href="https://calchub.org/mass-percent-calculator.html">
  <meta property="og:title" content="Mass Percent Calculator - Solution Concentration &amp; Weight Percent Solver">
  <meta property="og:description" content="Free chemistry mass percent calculator. Calculate percent by mass (w/w%), solute and solvent mass, solution preparation, and metal alloy composition.">
  <meta property="og:url" content="https://calchub.org/mass-percent-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Mass Percent Calculator - Chemistry &amp; Material Analysis">
  <meta name="twitter:description" content="Compute weight percent concentration across aqueous solutions, metallurgical alloys, and chemical mixtures with step-by-step solutions.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Mass Percent Calculator",
    "url": "https://calchub.org/mass-percent-calculator.html",
    "description": "Calculates mass percent concentration (w/w%), required solute mass, solvent mass, and chemical solution preparation quantities.",
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
        "name": "What is the formula for mass percent in chemistry?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The mass percent (also called weight percent or w/w%) is calculated by dividing the mass of the solute by the total mass of the solution (solute plus solvent) and multiplying by 100%: Mass Percent = (Mass of Solute / Total Mass of Solution) * 100% = [Mass of Solute / (Mass of Solute + Mass of Solvent)] * 100%."
        }
      },
      {
        "@type": "Question",
        "name": "Is mass percent temperature-dependent?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No. Unlike molarity (moles per liter) or volume percent (v/v%), mass is an invariant physical quantity that does not change with thermal expansion or contraction. Consequently, mass percent concentration remains strictly constant across all temperatures and pressures."
        }
      },
      {
        "@type": "Question",
        "name": "How do you prepare 500 grams of a 5% saline (NaCl) solution?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "For a 5.0% w/w solution with total mass 500 g: Solute Mass = 500 g * 0.05 = 25.0 grams of sodium chloride (NaCl). Solvent Mass = Total Mass - Solute Mass = 500 g - 25 g = 475.0 grams of pure distilled water (475 mL). Dissolve 25 g NaCl into 475 g water to achieve exactly 500 g of 5% saline."
        }
      },
      {
        "@type": "Question",
        "name": "What is the difference between mass percent and volume percent?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Mass percent (w/w%) compares the masses of components, whereas volume percent (v/v%) compares the volumes of liquids before mixing. Because intermolecular forces cause volume contraction upon mixing (e.g., mixing 50 mL ethanol with 50 mL water yields ~96 mL total solution), volume percent and mass percent are generally not equal unless both substances have identical density (1.0 g/mL) and zero excess volume of mixing."
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
      <span>Mass Percent Calculator</span>
    </nav>

    <div class="page-header">
      <h1 class="page-title">Mass Percent Calculator</h1>
      <p class="page-desc">Determine weight percent concentration (w/w%), required solute mass, solvent mass, and recipe proportions for chemical solutions and metallurgical alloys.</p>
    </div>

    <div class="calc-grid">
      <!-- Calculator Column -->
      <div class="calc-card">
        <div class="calc-header">
          <h2>Solution Concentration &amp; Weight Percent Solver</h2>
        </div>

        <!-- Mode Selection -->
        <div class="form-group">
          <label for="mp-mode">Calculation Mode:</label>
          <select id="mp-mode" class="form-control">
            <option value="find-percent" selected>Calculate Mass % (from Solute &amp; Solvent / Solution Mass)</option>
            <option value="find-solute">Calculate Required Solute Mass (from Target % &amp; Total Solution)</option>
            <option value="find-solvent">Calculate Required Solvent Mass (from Target % &amp; Solute Mass)</option>
          </select>
        </div>

        <!-- Preset Selection -->
        <div class="form-group">
          <label for="mp-preset">Common Chemical Solution Preset:</label>
          <select id="mp-preset" class="form-control">
            <option value="custom">-- Custom Mixture / Chemical Solution --</option>
            <option value="normal-saline">Normal Saline (0.9% w/w NaCl, IV infusion)</option>
            <option value="hypertonic-saline">Hypertonic Saline (3.0% w/w NaCl)</option>
            <option value="bleach">Household Bleach (5.25% w/w NaOCl in water)</option>
            <option value="vinegar">Distilled White Vinegar (5.0% w/w Acetic Acid)</option>
            <option value="rubbing-alcohol">Rubbing Alcohol (70.0% w/w Isopropanol)</option>
            <option value="battery-acid">Lead-Acid Battery Electrolyte (37.0% w/w H2SO4)</option>
            <option value="bronze-alloy">Standard Phosphor Bronze (92% Cu, 8% Sn alloy)</option>
            <option value="brass-alloy">Cartridge Brass Alloy (70% Cu, 30% Zn)</option>
            <option value="sterling-silver">Sterling Silver (92.5% Ag, 7.5% Cu)</option>
          </select>
        </div>

        <!-- Inputs Container -->
        <div id="mp-inputs-container">
          <!-- Solute Mass Input -->
          <div class="form-row" id="mp-solute-row">
            <div class="form-group">
              <label for="mp-solute-mass">Solute Mass ($m_{\text{solute}}$):</label>
              <input type="number" id="mp-solute-mass" class="form-control" value="25" step="any" min="0.0001">
            </div>
            <div class="form-group">
              <label for="mp-solute-unit">Solute Unit:</label>
              <select id="mp-solute-unit" class="form-control">
                <option value="g" selected>Grams (g)</option>
                <option value="mg">Milligrams (mg)</option>
                <option value="kg">Kilograms (kg)</option>
                <option value="oz">Ounces (oz)</option>
                <option value="lb">Pounds (lb)</option>
              </select>
            </div>
          </div>

          <!-- Total Mass Option for find-percent mode -->
          <div class="form-group" id="mp-basis-toggle-group">
            <label for="mp-basis-select">Known Secondary Mass:</label>
            <select id="mp-basis-select" class="form-control">
              <option value="solvent" selected>Solvent Mass (Water / Base Liquid)</option>
              <option value="solution">Total Solution Mass (Solute + Solvent)</option>
            </select>
          </div>

          <!-- Solvent / Solution Mass Input -->
          <div class="form-row" id="mp-secondary-row">
            <div class="form-group">
              <label id="mp-secondary-label" for="mp-secondary-mass">Solvent Mass ($m_{\text{solvent}}$):</label>
              <input type="number" id="mp-secondary-mass" class="form-control" value="475" step="any" min="0.0001">
            </div>
            <div class="form-group">
              <label for="mp-secondary-unit">Unit:</label>
              <select id="mp-secondary-unit" class="form-control">
                <option value="g" selected>Grams (g)</option>
                <option value="mg">Milligrams (mg)</option>
                <option value="kg">Kilograms (kg)</option>
                <option value="oz">Ounces (oz)</option>
                <option value="lb">Pounds (lb)</option>
              </select>
            </div>
          </div>

          <!-- Target Percent Row (for find-solute and find-solvent modes) -->
          <div class="form-row" id="mp-target-row" style="display: none;">
            <div class="form-group">
              <label for="mp-target-percent">Target Mass Percent (% w/w):</label>
              <input type="number" id="mp-target-percent" class="form-control" value="5.0" step="any" min="0.0001" max="99.999">
            </div>
          </div>
        </div>

        <div class="form-actions">
          <button type="button" id="mp-calc-btn" class="btn btn-primary">Calculate Concentration</button>
          <button type="button" id="mp-reset-btn" class="btn btn-secondary">Reset to Default</button>
        </div>

        <!-- Output Cards -->
        <div id="mp-results" class="results-container" style="margin-top: 1.5rem;">
          <div class="result-hero-card">
            <div class="result-label" style="font-size: 0.875rem; color: var(--text-muted, #64748b); text-transform: uppercase; font-weight: 600;">Mass Percent Concentration</div>
            <div id="mp-primary-out" style="font-size: 2.25rem; font-weight: 800; color: var(--primary, #2563eb); margin: 0.25rem 0;">5.000% w/w</div>
            <div id="mp-status-out" style="font-size: 1rem; color: var(--text-secondary, #475569); font-weight: 600;">25.00 g Solute in 500.00 g Total Solution</div>
          </div>

          <div class="summary-metrics-grid">
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Solute Mass ($m_1$)</div>
              <div id="mp-solute-out" style="font-size: 1.15rem; font-weight: 700;">25.00 g</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Solvent Mass ($m_2$)</div>
              <div id="mp-solvent-out" style="font-size: 1.15rem; font-weight: 700;">475.00 g</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Total Solution ($M$)</div>
              <div id="mp-solution-out" style="font-size: 1.15rem; font-weight: 700;">500.00 g</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Parts Per Million (ppm)</div>
              <div id="mp-ppm-out" style="font-size: 1.15rem; font-weight: 700;">50,000 ppm</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Reference Sidebar -->
      <aside class="sidebar-card">
        <h3>Standard Solution Concentrations</h3>
        <p style="font-size: 0.875rem; color: var(--text-secondary, #475569);">Common industrial and clinical aqueous mass percentages (w/w%):</p>
        <ul style="font-size: 0.875rem; line-height: 1.6; margin-left: 1.25rem;">
          <li><strong>Normal Saline (IV):</strong> 0.9% NaCl</li>
          <li><strong>Seawater (Average):</strong> 3.5% dissolved salts</li>
          <li><strong>Hydrogen Peroxide (Antiseptic):</strong> 3.0% H₂O₂</li>
          <li><strong>Table Vinegar:</strong> 5.0% CH₃COOH</li>
          <li><strong>Commercial Bleach:</strong> 5.25 – 6.0% NaOCl</li>
          <li><strong>Rubbing Alcohol:</strong> 70.0% Isopropanol</li>
          <li><strong>Battery Acid:</strong> 37.0% H₂SO₄</li>
          <li><strong>Concentrated HCl:</strong> 37.2% HCl</li>
          <li><strong>Concentrated Nitric Acid:</strong> 68.0% HNO₃</li>
          <li><strong>Concentrated Sulfuric Acid:</strong> 96.0 – 98.0% H₂SO₄</li>
        </ul>

        <h3 style="margin-top: 1.25rem;">Concentration Formulas</h3>
        <ul style="font-size: 0.875rem; line-height: 1.6; margin-left: 1.25rem;">
          <li>\(\text{w/w}\% = \frac{m_{\text{solute}}}{m_{\text{solution}}} \times 100\%\)</li>
          <li>\(m_{\text{solution}} = m_{\text{solute}} + m_{\text{solvent}}\)</li>
          <li>\(\text{ppm} = \text{w/w}\% \times 10,000\)</li>
          <li>\(\text{ppb} = \text{w/w}\% \times 10,000,000\)</li>
        </ul>
      </aside>
    </div>

    <!-- Long-Form Informational Engineering Article (1,400+ Words) -->
    <article class="article-body">
      <h2>1. The Definition and Physical Foundations of Mass Percent</h2>
      <p>Mass percent, also known as weight percent (\(\%\text{ w/w}\) or percent by mass), expresses the concentration of a chemical component within a homogeneous mixture or solution as the fraction of total mass attributable to that individual component, scaled to parts per hundred. In physical chemistry, chemical engineering, and metallurgical assaying, mass percent represents one of the most reliable and fundamental concentration metrics because mass is an extensive, conserved physical quantity strictly independent of temperature, atmospheric pressure, and liquid thermal expansion.</p>
      <p>Mathematically, for any two-component binary system consisting of a solute (component 1) dissolved in a solvent (component 2):</p>
      $$\text{Mass Percent } (\%\text{ w/w}) = \left(\frac{m_{\text{solute}}}{m_{\text{total solution}}}\right) \times 100\% = \left(\frac{m_{\text{solute}}}{m_{\text{solute}} + m_{\text{solvent}}}\right) \times 100\%$$
      <p>Where:</p>
      <ul>
        <li><strong>\(m_{\text{solute}}\):</strong> Mass of the dissolved substance or dispersed phase (e.g., sodium chloride crystals, sucrose, concentrated acid).</li>
        <li><strong>\(m_{\text{solvent}}\):</strong> Mass of the continuous dispersing liquid phase (e.g., pure deionized water, ethanol, acetone).</li>
        <li><strong>\(m_{\text{total solution}}\):</strong> Total aggregate mass of the finished solution (\(m_{\text{solution}} = m_{\text{solute}} + m_{\text{solvent}}\)). By the Law of Conservation of Mass (Lavoisier's Law), total mass before and after dissolution is identical, neglecting negligible relativistic binding energy differentials.</li>
      </ul>
      <p>For multicomponent mixtures containing \(k\) chemical species (such as stainless steel alloys or complex petrochemical streams), the mass percent of any arbitrary \(i\)-th component is defined as:</p>
      $$w_i\% = \left(\frac{m_i}{\sum_{j=1}^k m_j}\right) \times 100\%, \quad \text{such that } \sum_{i=1}^k w_i\% = 100.0\%$$

      <h2>2. Mass Percent vs. Molarity, Molality, and Volume Percent</h2>
      <p>Laboratory practitioners frequently encounter diverse concentration scales. Understanding their distinctions is crucial for laboratory accuracy and reactor stoichiometry:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Concentration Metric</th>
              <th>Symbol / Unit</th>
              <th>Defining Mathematical Formula</th>
              <th>Temperature Dependence?</th>
              <th>Primary Industrial Field</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Mass Percent</strong></td>
              <td>\(\%\text{ w/w}\)</td>
              <td>\((m_{\text{solute}} / m_{\text{solution}}) \times 100\%\)</td>
              <td>Strictly Independent</td>
              <td>Chemical synthesis, bulk shipping, alloys</td>
            </tr>
            <tr>
              <td><strong>Molarity</strong></td>
              <td>\(\text{M}\) (\(\text{mol/L}\))</td>
              <td>\(n_{\text{solute}} / V_{\text{solution}}\)</td>
              <td>Temperature Dependent</td>
              <td>Analytical volumetric titrations</td>
            </tr>
            <tr>
              <td><strong>Molality</strong></td>
              <td>\(m\) (\(\text{mol/kg}\))</td>
              <td>\(n_{\text{solute}} / m_{\text{solvent (kg)}}\)</td>
              <td>Strictly Independent</td>
              <td>Colligative properties, cryoscopy</td>
            </tr>
            <tr>
              <td><strong>Volume Percent</strong></td>
              <td>\(\%\text{ v/v}\)</td>
              <td>\((V_{\text{solute}} / V_{\text{solution}}) \times 100\%\)</td>
              <td>Temperature Dependent</td>
              <td>Alcoholic beverages, fuels, gas mixtures</td>
            </tr>
            <tr>
              <td><strong>Mass/Volume Ratio</strong></td>
              <td>\(\%\text{ w/v}\) (\(\text{g/100 mL}\))</td>
              <td>\((m_{\text{solute (g)}} / V_{\text{solution (mL)}}) \times 100\%\)</td>
              <td>Temperature Dependent</td>
              <td>Pharmaceutical dosage, clinical IV bags</td>
            </tr>
            <tr>
              <td><strong>Parts Per Million</strong></td>
              <td>\(\text{ppm}\) (\(\text{mg/kg}\))</td>
              <td>\((m_{\text{solute}} / m_{\text{solution}}) \times 10^6\)</td>
              <td>Strictly Independent</td>
              <td>Trace environmental contaminants, water quality</td>
            </tr>
          </tbody>
        </table>
      </div>

      <p>Because liquids expand when heated (positive thermal expansion coefficient \(\beta &gt; 0\)), a solution's total volume increases with temperature while mass remains invariant. Consequently, a \(1.000\text{ M}\) aqueous solution prepared at \(20^\circ\text{C}\) dilutes to approximately \(0.997\text{ M}\) at \(35^\circ\text{C}\) due to water expansion. In contrast, a \(10.0\%\text{ w/w}\) solution remains precisely \(10.0\%\text{ w/w}\) whether frozen at \(-10^\circ\text{C}\) or heated to boiling at \(100^\circ\text{C}\).</p>

      <h2>3. Interconverting Mass Percent with Molarity and Density</h2>
      <p>To convert between mass percent (\(w\%\)) and molar concentration (\(C\), in \(\text{mol/L}\) or \(\text{M}\)), the solution's volumetric mass density (\(\rho_{\text{solution}}\), in \(\text{g/mL}\) or \(\text{kg/L}\)) and the solute's molar mass (\(M_{\text{solute}}\), in \(\text{g/mol}\)) must be known.</p>
      <p>Consider \(1.0\text{ Liter}\) (\(1000\text{ mL}\)) of solution. Its total mass is:</p>
      $$m_{\text{solution}} = V \times \rho = 1000\text{ mL} \times \rho_{\text{solution}}\text{ (g/mL)}$$
      <p>The mass of dissolved solute present in that liter is:</p>
      $$m_{\text{solute}} = m_{\text{solution}} \times \left(\frac{w\%}{100}\right) = 1000 \times \rho_{\text{solution}} \times \left(\frac{w\%}{100}\right) = 10 \times \rho_{\text{solution}} \times w\%$$
      <p>Dividing by the solute's molar mass \(M_{\text{solute}}\) yields the fundamental interconversion formula for molarity:</p>
      $$\text{Molarity } (M) = \frac{10 \times \rho_{\text{solution}} \times w\%}{M_{\text{solute}}}$$
      <p>Conversely, solving for mass percent from known molarity yields:</p>
      $$w\% = \frac{M \times M_{\text{solute}}}{10 \times \rho_{\text{solution}}}$$

      <h2>4. Preparing Laboratory Solutions by Mass Percent</h2>
      <p>Analytical chemists use three distinct workflows to compound solutions of designated mass percentage:</p>
      <ol>
        <li><strong>Compounding by Total Desired Solution Mass:</strong> When a specific gross quantity of finished solution \(M_{\text{total}}\) is required:
        $$m_{\text{solute}} = M_{\text{total}} \times \left(\frac{\text{Target } w\%}{100}\right)$$
        $$m_{\text{solvent}} = M_{\text{total}} - m_{\text{solute}} = M_{\text{total}} \times \left(1 - \frac{\text{Target } w\%}{100}\right)$$
        The technician tares an analytical balance with a clean beaker, weighs out \(m_{\text{solute}}\), and adds solvent until the total mass reading hits \(M_{\text{total}}\).</li>
        <li><strong>Compounding from Fixed Solute Mass:</strong> When a researcher has a limited quantity of expensive or hazardous solute \(m_{\text{solute}}\) and wishes to dissolve all of it into a target concentration:
        $$m_{\text{solution}} = \frac{m_{\text{solute}}}{\text{Target } w\% / 100} \implies m_{\text{solvent}} = m_{\text{solute}} \times \left(\frac{100 - \text{Target } w\%}{\text{Target } w\%}\right)$$</li>
        <li><strong>Diluting Concentrated Stock Reagents:</strong> Diluting a commercial stock solution of initial mass fraction \(w_1\%\) with solvent to produce a dilute solution of mass fraction \(w_2\%\):
        $$m_1 \times w_1\% = m_2 \times w_2\% \implies m_{\text{stock}} = m_{\text{target}} \times \left(\frac{w_2\%}{w_1\%}\right)$$
        $$\text{Added Solvent Mass } = m_{\text{target}} - m_{\text{stock}}$$</li>
      </ol>

      <h2>5. Metallurgical and Solid Mixture Formulations</h2>
      <p>In materials science, mass percent is the primary metric used to specify the phase diagrams of alloys, ceramic compositions, and polymer blends. For example:</p>
      <ul>
        <li><strong>Carbon Steel:</strong> Iron with \(0.05\%\) to \(2.1\%\) carbon by mass. Mild steel contains \(0.15\%\text{ to }0.25\%\text{ C}\), whereas high-carbon tool steel contains \(0.60\%\text{ to }1.00\%\text{ C}\).</li>
        <li><strong>Austenitic Stainless Steel (AISI 304):</strong> Composed of \(18.0\%\text{ to }20.0\%\) Chromium (\(\text{Cr}\)), \(8.0\%\text{ to }10.5\%\) Nickel (\(\text{Ni}\)), \(\le 0.08\%\) Carbon, and the balance Iron (\(\approx 70\%\text{ Fe}\)).</li>
        <li><strong>Sterling Silver:</strong> Regulated by international hallmarking standards at \(92.5\%\) fine silver (\(\text{Ag}\)) and \(7.5\%\) alloying copper (\(\text{Cu}\)) by mass.</li>
        <li><strong>Karat Gold:</strong> Pure elemental gold is 24-karat (\(100.0\%\text{ Au}\)). 18-karat gold represents \(18/24 = 75.0\%\text{ Au}\) by mass, with the remaining \(25.0\%\) comprising copper, silver, or zinc to provide mechanical hardness.</li>
      </ul>

      <h2>6. Step-by-Step Worked Engineering Case Studies</h2>

      <div class="worked-example-card">
        <h3>Case Study 1: Compounding Medical Grade Normal Saline (0.90% w/w NaCl)</h3>
        <p><strong>Scenario:</strong> A hospital pharmacy compounding facility needs to prepare \(12.0\text{ kilograms}\) of sterile isotonic normal saline solution (\(0.90\%\text{ w/w NaCl}\) in pure deionized water) for intravenous infusion. Compute the exact masses of pharmaceutical-grade sodium chloride and purified water required.</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Identify given specifications:</strong></p>
          <ul>
            <li>Total solution mass \(M_{\text{total}} = 12.0\text{ kg} = 12,000.0\text{ g}\)</li>
            <li>Target mass percent \(w\% = 0.90\%\)</li>
          </ul>

          <p><strong>Step 2: Calculate required mass of sodium chloride solute (\(m_{\text{NaCl}}\)):</strong></p>
          $$m_{\text{NaCl}} = M_{\text{total}} \times \left(\frac{w\%}{100}\right) = 12,000.0\text{ g} \times 0.0090 = 108.0\text{ grams}$$

          <p><strong>Step 3: Calculate required mass of sterile water solvent (\(m_{\text{water}}\)):</strong></p>
          $$m_{\text{water}} = M_{\text{total}} - m_{\text{NaCl}} = 12,000.0\text{ g} - 108.0\text{ g} = 11,892.0\text{ grams} = 11.892\text{ kg}$$

          <p><strong>Step 4: Verify the concentration percentage:</strong></p>
          $$\%_{\text{NaCl}} = \left(\frac{108.0\text{ g}}{108.0\text{ g} + 11,892.0\text{ g}}\right) \times 100\% = \left(\frac{108.0}{12,000.0}\right) \times 100\% = 0.900\%$$
          <p><strong>Compounding Protocol:</strong> Weigh exactly \(108.0\text{ grams}\) of pure USP sodium chloride into a sterile compounding vessel, and add \(11,892.0\text{ grams}\) (\(11.892\text{ liters}\) at \(20^\circ\text{C}\)) of water for injection (WFI).</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Converting Concentrated Battery Acid (37.0% H₂SO₄) to Molarity</h3>
        <p><strong>Scenario:</strong> Commercial lead-acid automotive battery electrolyte is shipped as a \(37.0\%\text{ w/w}\) aqueous sulfuric acid solution (\(\text{H}_2\text{SO}_4\)). At \(20^\circ\text{C}\), the electrolyte has a measured specific gravity / density \(\rho = 1.280\text{ g/mL}\). The molar mass of sulfuric acid is \(M = 98.079\text{ g/mol}\). Calculate the molarity (\(\text{M}\)) and the parts-per-million (\(\text{ppm}\)) concentration.</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Identify all chemical parameters:</strong></p>
          <ul>
            <li>Mass percent \(w\% = 37.0\%\)</li>
            <li>Solution density \(\rho = 1.280\text{ g/mL} = 1280.0\text{ g/L}\)</li>
            <li>Solute molar mass \(M_{\text{H}_2\text{SO}_4} = 98.079\text{ g/mol}\)</li>
          </ul>

          <p><strong>Step 2: Determine mass of 1.0 Liter of battery electrolyte:</strong></p>
          $$m_{\text{1 L solution}} = 1000\text{ mL} \times 1.280\text{ g/mL} = 1280.0\text{ grams}$$

          <p><strong>Step 3: Calculate mass of pure \(\text{H}_2\text{SO}_4\) dissolved in 1.0 Liter:</strong></p>
          $$m_{\text{acid}} = 1280.0\text{ g} \times 0.370 = 473.6\text{ grams}$$

          <p><strong>Step 4: Compute molar concentration (Molarity):</strong></p>
          $$n_{\text{acid}} = \frac{473.6\text{ g}}{98.079\text{ g/mol}} = 4.8288\text{ moles}$$
          $$\text{Molarity } (M) = \frac{4.8288\text{ mol}}{1.0\text{ L}} = 4.83\text{ M (mol/L)}$$

          <p><strong>Step 5: Convert mass percent to parts per million (ppm):</strong></p>
          $$\text{ppm} = w\% \times 10,000 = 37.0 \times 10,000 = 370,000\text{ ppm}$$
          <p><strong>Result:</strong> The battery acid has a molarity of \(4.83\text{ M}\) and a concentration of \(370,000\text{ ppm}\).</p>
        </div>
      </div>

      <h2>7. Frequently Asked Questions (Applied Chemistry &amp; Dilutions)</h2>
      <div class="faq-accordion">
        <details class="faq-item">
          <summary>Can mass percent ever exceed 100%?</summary>
          <div class="faq-answer">
            <p>No. By definition, mass percent is the ratio of a part to the whole multiplied by 100%. Because the solute is a component of the total solution, its mass can never exceed the total mass (\(m_{\text{solute}} \le m_{\text{solution}}\)). Therefore, mass percent is bounded between 0% (pure solvent with zero solute) and 100% (pure dry solute with zero solvent).</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>How is parts per million (ppm) related to mass percent?</summary>
          <div class="faq-answer">
            <p>Both are dimensionless mass ratios. While mass percent expresses parts per hundred (\(10^{-2}\)), ppm expresses parts per million (\(10^{-6}\)). Consequently, \(1.0\%\text{ w/w}\) equals exactly \(10,000\text{ ppm}\). For ultra-trace analysis, parts per billion (ppb) represents parts per billion (\(10^{-9}\)), where \(1.0\%\text{ w/w} = 10,000,000\text{ ppb}\).</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>Does dissolving a solid salt increase the volume of water?</summary>
          <div class="faq-answer">
            <p>Yes, but not additively. Dissolving 50 grams of table salt into 500 mL of water does not produce 550 mL of solution. The hydrated ions (\(\text{Na}^+\) and \(\text{Cl}^-\)) nestle between polar water molecules in a phenomenon called electrostriction. The resulting solution volume is typically around 518 mL, demonstrating why mass percent (which depends solely on mass conservation) is much easier to measure accurately than volume-based concentrations.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>What is proof in alcoholic spirits compared to mass percent?</summary>
          <div class="faq-answer">
            <p>In the United States, alcohol proof is defined as double the volume percent (\(\%\text{ v/v}\)) of ethanol at 60°F. An 80-proof vodka contains 40.0% ethanol by volume. Because ethanol is less dense than water (\(\rho_{\text{EtOH}} \approx 0.789\text{ g/mL}\) vs \(\rho_{\text{water}} \approx 1.000\text{ g/mL}\)), 40.0% v/v converts to approximately 33.3% mass percent (\(\text{w/w}\% = (40 \times 0.789) / [(40 \times 0.789) + (60 \times 1.0)] \times 100\% \approx 34.5\%\)).</p>
          </div>
        </details>
      </div>

      <h2>8. Related Chemical Engineering &amp; Solution Calculators</h2>
      <p>Explore our integrated chemical calculation engines to solve dilutions, gas laws, and molar concentrations:</p>
      <div class="related-calculators" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-top: 1rem;">
        <a href="density-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Density Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Compute mass density ($\rho = m/V$) and specific gravity across fluid solutions.</p>
        </a>
        <a href="dilution-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Dilution Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Solve $C_1 V_1 = C_2 V_2$ for laboratory serial dilutions and buffer compounding.</p>
        </a>
        <a href="molarity-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Molarity Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Determine molar concentration ($M = n/V$) from solute formula weight.</p>
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
          <li><a href="mass-percent-calculator.html">Mass Percent</a></li>
          <li><a href="dilution-calculator.html">Dilution (C1V1 = C2V2)</a></li>
          <li><a href="density-calculator.html">Density &amp; Specific Gravity</a></li>
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
      const modeSelect = document.getElementById('mp-mode');
      const presetSelect = document.getElementById('mp-preset');
      const soluteRow = document.getElementById('mp-solute-row');
      const soluteMassInput = document.getElementById('mp-solute-mass');
      const soluteUnitSelect = document.getElementById('mp-solute-unit');
      const basisToggleGroup = document.getElementById('mp-basis-toggle-group');
      const basisSelect = document.getElementById('mp-basis-select');
      const secondaryRow = document.getElementById('mp-secondary-row');
      const secondaryLabel = document.getElementById('mp-secondary-label');
      const secondaryMassInput = document.getElementById('mp-secondary-mass');
      const secondaryUnitSelect = document.getElementById('mp-secondary-unit');
      const targetRow = document.getElementById('mp-target-row');
      const targetPercentInput = document.getElementById('mp-target-percent');

      const calcBtn = document.getElementById('mp-calc-btn');
      const resetBtn = document.getElementById('mp-reset-btn');

      // Outputs
      const primaryOut = document.getElementById('mp-primary-out');
      const statusOut = document.getElementById('mp-status-out');
      const soluteOut = document.getElementById('mp-solute-out');
      const solventOut = document.getElementById('mp-solvent-out');
      const solutionOut = document.getElementById('mp-solution-out');
      const ppmOut = document.getElementById('mp-ppm-out');

      const UNIT_TO_GRAMS = {
        'g': 1.0,
        'mg': 0.001,
        'kg': 1000.0,
        'oz': 28.349523,
        'lb': 453.59237
      };

      const PRESETS = {
        'normal-saline': { mode: 'find-percent', solute: 9, sUnit: 'g', basis: 'solution', sec: 1000, secUnit: 'g' },
        'hypertonic-saline': { mode: 'find-percent', solute: 30, sUnit: 'g', basis: 'solution', sec: 1000, secUnit: 'g' },
        'bleach': { mode: 'find-percent', solute: 52.5, sUnit: 'g', basis: 'solution', sec: 1000, secUnit: 'g' },
        'vinegar': { mode: 'find-percent', solute: 50, sUnit: 'g', basis: 'solution', sec: 1000, secUnit: 'g' },
        'rubbing-alcohol': { mode: 'find-percent', solute: 700, sUnit: 'g', basis: 'solution', sec: 1000, secUnit: 'g' },
        'battery-acid': { mode: 'find-percent', solute: 370, sUnit: 'g', basis: 'solution', sec: 1000, secUnit: 'g' },
        'bronze-alloy': { mode: 'find-percent', solute: 80, sUnit: 'g', basis: 'solution', sec: 1000, secUnit: 'g' },
        'brass-alloy': { mode: 'find-percent', solute: 300, sUnit: 'g', basis: 'solution', sec: 1000, secUnit: 'g' },
        'sterling-silver': { mode: 'find-percent', solute: 75, sUnit: 'g', basis: 'solution', sec: 1000, secUnit: 'g' }
      };

      function updateLayout() {
        const mode = modeSelect.value;
        if (mode === 'find-percent') {
          soluteRow.style.display = 'flex';
          basisToggleGroup.style.display = 'block';
          secondaryRow.style.display = 'flex';
          targetRow.style.display = 'none';
          secondaryLabel.textContent = basisSelect.value === 'solvent' ? 
            'Solvent Mass (m_solvent):' : 'Total Solution Mass (m_solution):';
        } else if (mode === 'find-solute') {
          soluteRow.style.display = 'none';
          basisToggleGroup.style.display = 'none';
          secondaryRow.style.display = 'flex';
          secondaryLabel.textContent = 'Total Solution Mass Desired (M_solution):';
          targetRow.style.display = 'flex';
        } else if (mode === 'find-solvent') {
          soluteRow.style.display = 'flex';
          basisToggleGroup.style.display = 'none';
          secondaryRow.style.display = 'none';
          targetRow.style.display = 'flex';
        }
      }

      function toGrams(val, unit) {
        return val * (UNIT_TO_GRAMS[unit] || 1.0);
      }

      function formatMass(grams) {
        if (grams >= 1000) return (grams / 1000).toFixed(3) + " kg";
        if (grams < 0.01) return (grams * 1000).toFixed(2) + " mg";
        return grams.toFixed(2) + " g";
      }

      function calculate() {
        const mode = modeSelect.value;
        let soluteGrams = 0;
        let solventGrams = 0;
        let totalGrams = 0;
        let massPercent = 0;

        if (mode === 'find-percent') {
          const rawSolute = parseFloat(soluteMassInput.value) || 0;
          soluteGrams = toGrams(rawSolute, soluteUnitSelect.value);

          const rawSec = parseFloat(secondaryMassInput.value) || 0;
          const secGrams = toGrams(rawSec, secondaryUnitSelect.value);

          if (basisSelect.value === 'solvent') {
            solventGrams = secGrams;
            totalGrams = soluteGrams + solventGrams;
          } else {
            totalGrams = secGrams;
            solventGrams = totalGrams - soluteGrams;
          }

          if (totalGrams <= 0 || soluteGrams < 0 || solventGrams < 0) {
            primaryOut.textContent = "-- %";
            statusOut.textContent = "Please enter valid non-negative mass values.";
            return;
          }

          massPercent = (soluteGrams / totalGrams) * 100;
        } else if (mode === 'find-solute') {
          const targetPct = parseFloat(targetPercentInput.value) || 0;
          const rawSol = parseFloat(secondaryMassInput.value) || 0;
          totalGrams = toGrams(rawSol, secondaryUnitSelect.value);

          if (totalGrams <= 0 || targetPct <= 0 || targetPct >= 100) {
            primaryOut.textContent = "-- %";
            statusOut.textContent = "Please enter target percentage between 0 and 100%.";
            return;
          }

          massPercent = targetPct;
          soluteGrams = totalGrams * (targetPct / 100);
          solventGrams = totalGrams - soluteGrams;
        } else if (mode === 'find-solvent') {
          const targetPct = parseFloat(targetPercentInput.value) || 0;
          const rawSolute = parseFloat(soluteMassInput.value) || 0;
          soluteGrams = toGrams(rawSolute, soluteUnitSelect.value);

          if (soluteGrams <= 0 || targetPct <= 0 || targetPct >= 100) {
            primaryOut.textContent = "-- %";
            statusOut.textContent = "Please enter valid solute and target % (0-100%).";
            return;
          }

          massPercent = targetPct;
          totalGrams = soluteGrams / (targetPct / 100);
          solventGrams = totalGrams - soluteGrams;
        }

        const ppm = massPercent * 10000;

        // Render to UI
        primaryOut.textContent = massPercent.toFixed(3) + "% w/w";
        statusOut.textContent = `${formatMass(soluteGrams)} Solute in ${formatMass(totalGrams)} Total Solution`;
        soluteOut.textContent = formatMass(soluteGrams);
        solventOut.textContent = formatMass(solventGrams);
        solutionOut.textContent = formatMass(totalGrams);
        ppmOut.textContent = ppm.toLocaleString('en-US', { maximumFractionDigits: 1 }) + " ppm";
      }

      // Preset selection
      presetSelect.addEventListener('change', function() {
        const val = this.value;
        if (PRESETS[val]) {
          const p = PRESETS[val];
          modeSelect.value = p.mode;
          basisSelect.value = p.basis;
          soluteMassInput.value = p.solute;
          soluteUnitSelect.value = p.sUnit;
          secondaryMassInput.value = p.sec;
          secondaryUnitSelect.value = p.secUnit;
          updateLayout();
          calculate();
        }
      });

      modeSelect.addEventListener('change', function() {
        updateLayout();
        calculate();
      });

      basisSelect.addEventListener('change', function() {
        updateLayout();
        calculate();
      });

      [soluteMassInput, soluteUnitSelect, secondaryMassInput, secondaryUnitSelect, targetPercentInput].forEach(el => {
        el.addEventListener('input', function() {
          presetSelect.value = 'custom';
          calculate();
        });
        el.addEventListener('change', calculate);
      });

      calcBtn.addEventListener('click', calculate);

      resetBtn.addEventListener('click', function() {
        modeSelect.value = 'find-percent';
        presetSelect.value = 'custom';
        basisSelect.value = 'solvent';
        soluteMassInput.value = '25';
        soluteUnitSelect.value = 'g';
        secondaryMassInput.value = '475';
        secondaryUnitSelect.value = 'g';
        targetPercentInput.value = '5.0';
        updateLayout();
        calculate();
      });

      // Initial execution
      updateLayout();
      calculate();
    })();
  </script>
</body>
</html>
"""

# 2. molality-calculator.html
HTML_MOLALITY = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Molality Calculator - Solution Molal Concentration (m = mol/kg)</title>
  <meta name="description" content="Calculate molality (m = n_solute / m_solvent(kg)), solute mass, solvent mass, and colligative properties (freezing point depression & boiling elevation).">
  <link rel="canonical" href="https://calchub.org/molality-calculator.html">
  <meta property="og:title" content="Molality Calculator - Colligative Properties &amp; Molal Concentration">
  <meta property="og:description" content="Free chemistry molality calculator. Compute molal concentration (m = mol/kg), solute grams from molar mass, solvent kilograms, and delta T_f freezing depression.">
  <meta property="og:url" content="https://calchub.org/molality-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Molality Calculator - Thermodynamics &amp; Solution Chemistry">
  <meta name="twitter:description" content="Solve molality, freezing point depression, and boiling point elevation with temperature-independent solvent mass calculations.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Molality Calculator",
    "url": "https://calchub.org/molality-calculator.html",
    "description": "Calculates solution molality (m = moles of solute / kg of solvent), solute mass requirements, and colligative temperature shifts.",
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
        "name": "What is the formula for molality in chemistry?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Molality (denoted by lowercase m or b) is defined as the number of moles of solute divided by the mass of the pure solvent in kilograms: Molality (m) = Moles of Solute / Mass of Solvent (kg) = [Mass of Solute (g) / Molar Mass (g/mol)] / Mass of Solvent (kg). Its SI unit is mol/kg (or molal)."
        }
      },
      {
        "@type": "Question",
        "name": "Why is molality preferred over molarity for colligative properties?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Molarity (moles per liter of solution) changes with temperature because liquids expand and contract thermally, altering the denominator volume. In contrast, molality is defined per kilogram of solvent mass, which is strictly invariant with temperature. Because colligative properties like freezing point depression and boiling point elevation involve significant temperature changes, molality ensures rigorous thermodynamic precision."
        }
      },
      {
        "@type": "Question",
        "name": "What is the van 't Hoff factor (i) in molality calculations?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The van 't Hoff factor (i) represents the number of discrete particles (ions or molecules) into which a solute dissociates when dissolved in solution. For non-electrolytes like glucose or sucrose, i = 1. For strong electrolytes that dissociate completely, i equals the number of ions formed (e.g., NaCl -> Na+ + Cl- gives i = 2; CaCl2 -> Ca2+ + 2Cl- gives i = 3)."
        }
      },
      {
        "@type": "Question",
        "name": "How is freezing point depression calculated from molality?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Freezing point depression follows Blagden's Law: ΔT_f = i * K_f * m, where ΔT_f is the decrease in freezing point, i is the van 't Hoff factor, K_f is the cryoscopic constant of the solvent (1.86 °C·kg/mol for water), and m is the solution molality in mol/kg."
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
      <span>Molality Calculator</span>
    </nav>

    <div class="page-header">
      <h1 class="page-title">Molality Calculator</h1>
      <p class="page-desc">Compute molal concentration ($m = \text{mol/kg}$), required solute grams, solvent mass, and colligative freezing point depression and boiling elevation.</p>
    </div>

    <div class="calc-grid">
      <!-- Calculator Column -->
      <div class="calc-card">
        <div class="calc-header">
          <h2>Solution Molality &amp; Colligative Solver</h2>
        </div>

        <!-- Solute Preset Selection -->
        <div class="form-group">
          <label for="mol-solute-preset">Common Solute Preset (Auto-fills Molar Mass &amp; $i$):</label>
          <select id="mol-solute-preset" class="form-control">
            <option value="custom">-- Custom Solute Formula --</option>
            <option value="nacl" selected>Sodium Chloride (NaCl: 58.44 g/mol, i = 2.0)</option>
            <option value="glucose">Glucose / Dextrose (C6H12O6: 180.16 g/mol, i = 1.0)</option>
            <option value="sucrose">Sucrose / Cane Sugar (C12H22O11: 342.30 g/mol, i = 1.0)</option>
            <option value="cacl2">Calcium Chloride (CaCl2: 110.98 g/mol, i = 3.0)</option>
            <option value="mgcl2">Magnesium Chloride (MgCl2: 95.21 g/mol, i = 3.0)</option>
            <option value="urea">Urea ((NH2)2CO: 60.06 g/mol, i = 1.0)</option>
            <option value="etoh">Ethanol (C2H5OH: 46.07 g/mol, i = 1.0)</option>
            <option value="eg">Ethylene Glycol (Antifreeze: C2H6O2, 62.07 g/mol, i = 1.0)</option>
            <option value="kcl">Potassium Chloride (KCl: 74.55 g/mol, i = 2.0)</option>
          </select>
        </div>

        <!-- Solute Inputs -->
        <div class="form-row">
          <div class="form-group">
            <label for="mol-solute-mass">Solute Mass ($m_{\text{solute}}$):</label>
            <input type="number" id="mol-solute-mass" class="form-control" value="58.44" step="any" min="0.0001">
          </div>
          <div class="form-group">
            <label for="mol-solute-unit">Solute Unit:</label>
            <select id="mol-solute-unit" class="form-control">
              <option value="g" selected>Grams (g)</option>
              <option value="mg">Milligrams (mg)</option>
              <option value="kg">Kilograms (kg)</option>
              <option value="lb">Pounds (lb)</option>
            </select>
          </div>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label for="mol-molar-mass">Molar Mass ($M$ in g/mol):</label>
            <input type="number" id="mol-molar-mass" class="form-control" value="58.44" step="any" min="0.01">
          </div>
          <div class="form-group">
            <label for="mol-van-hoff">van 't Hoff Factor ($i$):</label>
            <input type="number" id="mol-van-hoff" class="form-control" value="2.0" step="any" min="1.0" max="6.0">
          </div>
        </div>

        <!-- Solvent Inputs -->
        <div class="form-row">
          <div class="form-group">
            <label for="mol-solvent-mass">Solvent Mass ($m_{\text{solvent}}$):</label>
            <input type="number" id="mol-solvent-mass" class="form-control" value="1.0" step="any" min="0.0001">
          </div>
          <div class="form-group">
            <label for="mol-solvent-unit">Solvent Unit:</label>
            <select id="mol-solvent-unit" class="form-control">
              <option value="kg" selected>Kilograms (kg)</option>
              <option value="g">Grams (g)</option>
              <option value="lb">Pounds (lb)</option>
            </select>
          </div>
        </div>

        <!-- Solvent Selection (Kf & Kb) -->
        <div class="form-group">
          <label for="mol-solvent-preset">Solvent Cryoscopic &amp; Ebullioscopic Constants:</label>
          <select id="mol-solvent-preset" class="form-control">
            <option value="water" selected>Water (H2O: Kf = 1.86 °C·kg/mol, Kb = 0.512 °C·kg/mol, Tf = 0°C, Tb = 100°C)</option>
            <option value="benzene">Benzene (C6H6: Kf = 5.12 °C·kg/mol, Kb = 2.53 °C·kg/mol, Tf = 5.5°C, Tb = 80.1°C)</option>
            <option value="ethanol">Ethanol (C2H5OH: Kf = 1.99 °C·kg/mol, Kb = 1.22 °C·kg/mol, Tf = -114.1°C, Tb = 78.4°C)</option>
            <option value="cyclohexane">Cyclohexane (C6H12: Kf = 20.2 °C·kg/mol, Kb = 2.79 °C·kg/mol, Tf = 6.5°C, Tb = 80.7°C)</option>
            <option value="camphor">Camphor (Kf = 40.0 °C·kg/mol, Tf = 178.4°C)</option>
          </select>
        </div>

        <div class="form-actions">
          <button type="button" id="mol-calc-btn" class="btn btn-primary">Calculate Molality</button>
          <button type="button" id="mol-reset-btn" class="btn btn-secondary">Reset</button>
        </div>

        <!-- Output Hero and Cards -->
        <div id="mol-results" class="results-container" style="margin-top: 1.5rem;">
          <div class="result-hero-card">
            <div class="result-label" style="font-size: 0.875rem; color: var(--text-muted, #64748b); text-transform: uppercase; font-weight: 600;">Solution Molality ($m$)</div>
            <div id="mol-primary-out" style="font-size: 2.25rem; font-weight: 800; color: var(--primary, #2563eb); margin: 0.25rem 0;">1.000 mol/kg</div>
            <div id="mol-status-out" style="font-size: 1rem; color: var(--text-secondary, #475569); font-weight: 600;">1.000 mol Solute in 1.000 kg Solvent</div>
          </div>

          <div class="summary-metrics-grid">
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Moles of Solute ($n$)</div>
              <div id="mol-moles-out" style="font-size: 1.15rem; font-weight: 700;">1.0000 mol</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Freezing Point ($\Delta T_f$)</div>
              <div id="mol-freeze-out" style="font-size: 1.15rem; font-weight: 700; color: #0284c7;">-3.72 °C</div>
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Depression: 3.72 °C</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Boiling Point ($\Delta T_b$)</div>
              <div id="mol-boil-out" style="font-size: 1.15rem; font-weight: 700; color: #d97706;">101.02 °C</div>
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Elevation: +1.02 °C</div>
            </div>
            <div class="metric-card">
              <div style="font-size: 0.75rem; color: var(--text-muted, #64748b);">Mass Percent (\% w/w)</div>
              <div id="mol-masspct-out" style="font-size: 1.15rem; font-weight: 700;">5.52% w/w</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Reference Sidebar -->
      <aside class="sidebar-card">
        <h3>Solvent Cryoscopic &amp; Ebullioscopic Table</h3>
        <p style="font-size: 0.875rem; color: var(--text-secondary, #475569);">Freezing depression ($K_f$) and boiling elevation ($K_b$) constants:</p>
        <ul style="font-size: 0.875rem; line-height: 1.6; margin-left: 1.25rem;">
          <li><strong>Water ($H_2O$):</strong><br>\(K_f = 1.86\), \(K_b = 0.512\) \(^\circ\text{C}\cdot\text{kg/mol}\)</li>
          <li><strong>Benzene ($C_6H_6$):</strong><br>\(K_f = 5.12\), \(K_b = 2.53\) \(^\circ\text{C}\cdot\text{kg/mol}\)</li>
          <li><strong>Ethanol ($C_2H_5OH$):</strong><br>\(K_f = 1.99\), \(K_b = 1.22\) \(^\circ\text{C}\cdot\text{kg/mol}\)</li>
          <li><strong>Cyclohexane ($C_6H_{12}$):</strong><br>\(K_f = 20.2\), \(K_b = 2.79\) \(^\circ\text{C}\cdot\text{kg/mol}\)</li>
          <li><strong>Acetic Acid ($CH_3COOH$):</strong><br>\(K_f = 3.90\), \(K_b = 3.07\) \(^\circ\text{C}\cdot\text{kg/mol}\)</li>
          <li><strong>Camphor ($C_{10}H_{16}O$):</strong><br>\(K_f = 40.0\) \(^\circ\text{C}\cdot\text{kg/mol}\)</li>
        </ul>

        <h3 style="margin-top: 1.25rem;">Colligative Formulas</h3>
        <ul style="font-size: 0.875rem; line-height: 1.6; margin-left: 1.25rem;">
          <li>\(m = \frac{n_{\text{solute}}}{m_{\text{solvent (kg)}}}\)</li>
          <li>\(\Delta T_f = i \times K_f \times m\)</li>
          <li>\(\Delta T_b = i \times K_b \times m\)</li>
          <li>\(T_{f,\text{new}} = T_{f,\text{pure}} - \Delta T_f\)</li>
          <li>\(T_{b,\text{new}} = T_{b,\text{pure}} + \Delta T_b\)</li>
        </ul>
      </aside>
    </div>

    <!-- Long-Form Informational Engineering Article (1,400+ Words) -->
    <article class="article-body">
      <h2>1. The Definition and Thermodynamic Significance of Molality</h2>
      <p>In physical chemistry and chemical thermodynamics, molality (conventionally denoted by the lowercase letter \(m\) or the symbol \(b\)) is defined as the chemical amount of a solute (expressed in moles) dissolved per unit mass of pure solvent (expressed in kilograms). Formally:</p>
      $$\text{Molality } (m) = \frac{n_{\text{solute}}}{m_{\text{solvent (kg)}}} = \frac{m_{\text{solute (g)}} / M_{\text{solute (g/mol)}}}{m_{\text{solvent (kg)}}}$$
      <p>Where:</p>
      <ul>
        <li><strong>\(n_{\text{solute}}\):</strong> Amount of substance of the solute in moles (\(\text{mol}\)), calculated as mass in grams divided by molar mass (\(n = m / M\)).</li>
        <li><strong>\(M_{\text{solute}}\):</strong> Molar mass (molecular weight) of the chemical solute in grams per mole (\(\text{g/mol}\)).</li>
        <li><strong>\(m_{\text{solvent (kg)}}\):</strong> Mass of the pure solvent in kilograms (\(\text{kg}\)), completely excluding the mass of the solute.</li>
      </ul>
      <p>The standard SI unit for molality is moles per kilogram (\(\text{mol/kg}\)), historically referred to as "molal" (e.g., a \(2.0\text{ mol/kg}\) solution is termed "2.0 molal"). Unlike molarity (\(\text{M} = \text{mol/L}\)), which relies on total solution volume, molality relates moles of solute directly to a fixed invariant mass of solvent.</p>

      <h2>2. Why Molality is Strictly Temperature-Independent</h2>
      <p>The distinction between molarity and molality is critical when analyzing thermal and thermodynamic processes. Consider what occurs when an aqueous solution is heated from \(4^\circ\text{C}\) to \(90^\circ\text{C}\):</p>
      <ul>
        <li><strong>Volumetric Expansion:</strong> Water has a positive thermal expansion coefficient. One liter of pure water at \(4^\circ\text{C}\) expands to approximately \(1.036\text{ liters}\) at \(90^\circ\text{C}\), representing a \(3.6\%\) volumetric dilation. Because molarity is defined per liter of solution (\(M = n / V\)), the apparent molarity drops by \(3.6\%\) without any change in the physical quantity of solute.</li>
        <li><strong>Mass Invariance:</strong> Under classical Newtonian and relativistic regimes, mass is strictly conserved. The \(1.000\text{ kg}\) of water solvent present at \(4^\circ\text{C}\) remains exactly \(1.000\text{ kg}\) of water at \(90^\circ\text{C}\) (in a closed system). Therefore, the solution's molality remains strictly invariant across all temperatures and hydrostatic pressures.</li>
      </ul>
      <p>For this reason, all thermodynamic equilibrium constants, activity coefficients, phase diagrams, and colligative property equations are rigorously formulated in terms of molality or mole fractions rather than molarity.</p>

      <h2>3. Colligative Properties: Freezing Point Depression and Boiling Point Elevation</h2>
      <p>Colligative properties are physical properties of solutions that depend solely on the ratio of the number of solute particles to the number of solvent molecules, completely independent of the chemical identity or molecular size of the solute particles. The four classical colligative properties are:</p>
      <ol>
        <li>Vapor Pressure Lowering (Raoult's Law: \(\Delta P = X_{\text{solute}} P^\circ\))</li>
        <li>Freezing Point Depression (Cryoscopy)</li>
        <li>Boiling Point Elevation (Ebullioscopy)</li>
        <li>Osmotic Pressure (van 't Hoff's Equation: \(\Pi = i M R T\))</li>
      </ol>

      <h3>A. Freezing Point Depression (Cryoscopy)</h3>
      <p>When a non-volatile solute is dissolved into a liquid solvent, the chemical potential of the liquid phase decreases, shifting the solid-liquid thermodynamic phase equilibrium to a lower temperature. The freezing point of the solution is depressed by an amount \(\Delta T_f\) proportional to molality:</p>
      $$\Delta T_f = i \times K_f \times m$$
      <p>Where:</p>
      <ul>
        <li><strong>\(\Delta T_f\):</strong> The positive freezing point depression (\(\Delta T_f = T_{f,\text{pure solvent}} - T_{f,\text{solution}}\)).</li>
        <li><strong>\(i\):</strong> Dimensionless van 't Hoff factor, representing the number of discrete ions or particles produced per formula unit of solute in solution.</li>
        <li><strong>\(K_f\):</strong> Cryoscopic constant (molal freezing point depression constant) of the specific solvent, measured in \(^\circ\text{C}\cdot\text{kg/mol}\) or \(\text{K}\cdot\text{kg/mol}\). For pure water, \(K_f = 1.86^\circ\text{C}\cdot\text{kg/mol}\).</li>
        <li><strong>\(m\):</strong> Solution molality in \(\text{mol/kg}\).</li>
      </ul>
      <p>The resulting depressed freezing temperature of the mixture is:</p>
      $$T_{f,\text{solution}} = T_{f,\text{pure}} - \Delta T_f = 0.0^\circ\text{C} - (i K_f m)$$

      <h3>B. Boiling Point Elevation (Ebullioscopy)</h3>
      <p>Simultaneously, the presence of solute particles reduces the solvent's vapor pressure, requiring a higher temperature for vapor pressure to reach atmospheric pressure. The boiling point of the solution is elevated by an amount \(\Delta T_b\):</p>
      $$\Delta T_b = i \times K_b \times m$$
      <p>Where \(K_b\) is the ebullioscopic constant (molal boiling point elevation constant). For pure water, \(K_b = 0.512^\circ\text{C}\cdot\text{kg/mol}\). The elevated boiling temperature is:</p>
      $$T_{b,\text{solution}} = T_{b,\text{pure}} + \Delta T_b = 100.0^\circ\text{C} + (i K_b m)$$

      <h2>4. The van 't Hoff Factor (\(i\)) and Ionic Dissociation</h2>
      <p>The van 't Hoff factor accounts for electrolytic dissociation into free ions in polar solvents:</p>
      <ul>
        <li><strong>Non-Electrolytes (\(i = 1.0\)):</strong> Organic molecules like glucose (\(\text{C}_6\text{H}_{12}\text{O}_6\)), sucrose (\(\text{C}_{12}\text{H}_{22}\text{O}_{11}\)), urea (\(\text{CO(NH}_2)_2\)), and ethylene glycol do not dissociate into ions. Each dissolved mole contributes exactly one mole of particles.</li>
        <li><strong>Strong Binary Electrolytes (\(i \approx 2.0\)):</strong> Salts like sodium chloride (\(\text{NaCl} \to \text{Na}^+ + \text{Cl}^-\)) and potassium chloride (\(\text{KCl}\)) dissociate into 2 ions per formula unit. At infinite dilution, \(i = 2.0\). In real solutions, interionic electrostatic attractions slightly reduce the effective value (for a \(1.0\text{ m NaCl}\) solution, experimental \(i \approx 1.81\)).</li>
        <li><strong>Ternary Electrolytes (\(i \approx 3.0\)):</strong> Salts like calcium chloride (\(\text{CaCl}_2 \to \text{Ca}^{2+} + 2\text{Cl}^-\)) and magnesium chloride (\(\text{MgCl}_2\)) yield 3 ions per formula unit, depressing freezing points 3 times more effectively per mole than glucose. This explains why highway departments prefer spreading \(\text{CaCl}_2\) rather than \(\text{NaCl}\) during sub-zero winter storms.</li>
      </ul>

      <h2>5. Comparing Solvents and Their Cryoscopic Constants</h2>
      <p>The magnitude of freezing point depression depends fundamentally on the solvent's enthalpy of fusion (\(\Delta H_{\text{fus}}\)) and normal freezing point (\(T_f\)), governed by the thermodynamic relation:</p>
      $$K_f = \frac{R \times T_f^2 \times M_{\text{solvent}}}{1000 \times \Delta H_{\text{fus}}}$$
      <p>The following benchmark table contrasts standard solvents used in chemical cryoscopy and molecular weight determination:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Solvent</th>
              <th>Normal Freezing Point (\(T_f\))</th>
              <th>Cryoscopic Constant (\(K_f\))</th>
              <th>Normal Boiling Point (\(T_b\))</th>
              <th>Ebullioscopic Constant (\(K_b\))</th>
              <th>Primary Laboratory Use</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Water (\(\text{H}_2\text{O}\))</td>
              <td>0.00 °C</td>
              <td>1.86 °C·kg/mol</td>
              <td>100.00 °C</td>
              <td>0.512 °C·kg/mol</td>
              <td>Aqueous biochemistry, physiology</td>
            </tr>
            <tr>
              <td>Benzene (\(\text{C}_6\text{H}_6\))</td>
              <td>5.53 °C</td>
              <td>5.12 °C·kg/mol</td>
              <td>80.10 °C</td>
              <td>2.530 °C·kg/mol</td>
              <td>Organic polymer molecular weights</td>
            </tr>
            <tr>
              <td>Ethanol (\(\text{C}_2\text{H}_5\text{OH}\))</td>
              <td>-114.10 °C</td>
              <td>1.99 °C·kg/mol</td>
              <td>78.37 °C</td>
              <td>1.220 °C·kg/mol</td>
              <td>Low-temperature organic synthesis</td>
            </tr>
            <tr>
              <td>Cyclohexane (\(\text{C}_6\text{H}_{12}\))</td>
              <td>6.55 °C</td>
              <td>20.20 °C·kg/mol</td>
              <td>80.74 °C</td>
              <td>2.790 °C·kg/mol</td>
              <td>High-sensitivity Rast cryoscopy</td>
            </tr>
            <tr>
              <td>Acetic Acid (\(\text{CH}_3\text{COOH}\))</td>
              <td>16.60 °C</td>
              <td>3.90 °C·kg/mol</td>
              <td>117.90 °C</td>
              <td>3.070 °C·kg/mol</td>
              <td>Glacial non-aqueous titrations</td>
            </tr>
            <tr>
              <td>Camphor (\(\text{C}_{10}\text{H}_{16}\text{O}\))</td>
              <td>178.40 °C</td>
              <td>40.00 °C·kg/mol</td>
              <td>204.00 °C</td>
              <td>5.610 °C·kg/mol</td>
              <td>Rast method for macromolecule MW</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>6. Step-by-Step Worked Engineering Case Studies</h2>

      <div class="worked-example-card">
        <h3>Case Study 1: Automotive Radiator Antifreeze Freezing Point Protection</h3>
        <p><strong>Scenario:</strong> An automotive mechanic prepares an engine cooling mixture by dissolving \(1.55\text{ kilograms}\) of pure ethylene glycol (\(\text{C}_2\text{H}_6\text{O}_2\), molar mass \(M = 62.07\text{ g/mol}\), non-electrolyte \(i = 1.0\)) into \(2.50\text{ kilograms}\) of pure water. The cryoscopic constant of water is \(K_f = 1.86^\circ\text{C}\cdot\text{kg/mol}\). Calculate the molality of the antifreeze solution, the freezing point depression \(\Delta T_f\), and the minimum safe winter operating temperature.</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Calculate moles of ethylene glycol solute (\(n_{\text{solute}}\)):</strong></p>
          $$m_{\text{glycol}} = 1.55\text{ kg} = 1550.0\text{ grams}$$
          $$n_{\text{glycol}} = \frac{1550.0\text{ g}}{62.07\text{ g/mol}} = 24.9718\text{ moles}$$

          <p><strong>Step 2: Calculate solution molality (\(m\)):</strong></p>
          $$m = \frac{n_{\text{glycol}}}{m_{\text{solvent (kg)}}} = \frac{24.9718\text{ mol}}{2.50\text{ kg}} = 9.9887\text{ mol/kg} \approx 9.99\text{ m}$$

          <p><strong>Step 3: Calculate freezing point depression (\(\Delta T_f\)):</strong></p>
          $$\Delta T_f = i \times K_f \times m = 1.0 \times 1.86^\circ\text{C}\cdot\text{kg/mol} \times 9.9887\text{ mol/kg} = 18.579^\circ\text{C}$$

          <p><strong>Step 4: Determine the new freezing temperature:</strong></p>
          $$T_{f,\text{solution}} = 0.00^\circ\text{C} - 18.58^\circ\text{C} = -18.58^\circ\text{C} \quad (-1.4^\circ\text{F})$$

          <p><strong>Step 5: Calculate boiling point elevation at sea level:</strong></p>
          $$\Delta T_b = i \times K_b \times m = 1.0 \times 0.512 \times 9.9887 = 5.114^\circ\text{C}$$
          $$T_{b,\text{solution}} = 100.00^\circ\text{C} + 5.11^\circ\text{C} = 105.11^\circ\text{C} \quad (221.2^\circ\text{F})$$
          <p><strong>Engineering Conclusion:</strong> This \(9.99\text{ molal}\) radiator mix protects the automotive cooling block from freezing ruptures down to \(-18.6^\circ\text{C}\) while preventing coolant boilover up to \(105.1^\circ\text{C}\).</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Determining Unknown Organic Compound Molar Mass via Cryoscopy</h3>
        <p><strong>Scenario:</strong> A forensic chemist isolates an unknown white crystalline pesticide. A \(4.50\text{-gram}\) sample of this non-electrolyte compound (\(i = 1.0\)) is completely dissolved into \(125.0\text{ grams}\) of pure benzene (\(K_f = 5.12^\circ\text{C}\cdot\text{kg/mol}\), normal freezing point \(T_f = 5.53^\circ\text{C}\)). The solution freezes at \(4.25^\circ\text{C}\). Determine the molality of the solution and the experimental molar mass of the unknown pesticide.</p>
        
        <div class="step-solution">
          <p><strong>Step 1: Calculate the observed freezing point depression (\(\Delta T_f\)):</strong></p>
          $$\Delta T_f = T_{f,\text{pure}} - T_{f,\text{solution}} = 5.53^\circ\text{C} - 4.25^\circ\text{C} = 1.28^\circ\text{C}$$

          <p><strong>Step 2: Solve the cryoscopy equation for molality (\(m\)):</strong></p>
          $$\Delta T_f = i K_f m \implies m = \frac{\Delta T_f}{i K_f} = \frac{1.28^\circ\text{C}}{1.0 \times 5.12^\circ\text{C}\cdot\text{kg/mol}} = 0.250\text{ mol/kg}$$

          <p><strong>Step 3: Calculate moles of unknown compound in the \(125.0\text{ g}\) (\(0.125\text{ kg}\)) of solvent:</strong></p>
          $$n_{\text{solute}} = m \times m_{\text{solvent (kg)}} = 0.250\text{ mol/kg} \times 0.125\text{ kg} = 0.03125\text{ moles}$$

          <p><strong>Step 4: Calculate the compound's molar mass (\(M\)):</strong></p>
          $$M = \frac{m_{\text{sample}}}{n_{\text{solute}}} = \frac{4.50\text{ g}}{0.03125\text{ mol}} = 144.0\text{ g/mol}$$
          <p><strong>Analytical Conclusion:</strong> The compound has a molar mass of \(144.0\text{ g/mol}\), consistent with alpha-naphthol (\(\text{C}_{10}\text{H}_8\text{O}\), \(144.17\text{ g/mol}\)).</p>
        </div>
      </div>

      <h2>7. Frequently Asked Questions (Physical Chemistry &amp; Solution Physics)</h2>
      <div class="faq-accordion">
        <details class="faq-item">
          <summary>When are molarity and molality virtually identical?</summary>
          <div class="faq-answer">
            <p>For very dilute aqueous solutions at room temperature (near 4°C to 20°C), molarity and molality are numerically almost indistinguishable. Because the density of pure water is approximately 1.000 kg/L (or 1.000 g/mL), 1.000 liter of water has a mass of 1.000 kilogram. In dilute solutions where solute mass is negligible, 1 kg of solvent occupies roughly 1 L of total volume, making \(M \approx m\). However, for concentrated solutions or non-aqueous solvents with densities far from 1.0 (such as chloroform at 1.49 g/mL or ethanol at 0.79 g/mL), molarity and molality diverge dramatically.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>Why does road salt stop working below -10°C (14°F)?</summary>
          <div class="faq-answer">
            <p>Common road salt (NaCl) and water form a eutectic system. The eutectic point (the lowest possible freezing temperature achievable by saturated brine) occurs at 23.3% NaCl by mass at -21.1°C (-6.0°F). In practice, as temperature drops below -10°C, the rate of ice dissolution slows exponentially, and moisture required to initiate brine formation is absent. In extreme Arctic freezes below -15°C, highway departments switch to calcium chloride (CaCl2) or magnesium chloride (MgCl2), which release exothermic heat of solution upon hydration and achieve eutectic temperatures below -30°C.</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>Can molality be calculated if only molarity and density are known?</summary>
          <div class="faq-answer">
            <p>Yes. By considering 1.0 Liter (1000 mL) of solution with known molarity \(M\) and density \(\rho\) (in g/mL): Total solution mass equals \(1000 \times \rho\) grams. Solute mass equals \(M \times M_{\text{solute}}\) grams. The solvent mass in kilograms is \([(1000 \times \rho) - (M \times M_{\text{solute}})] / 1000\). Molality is then obtained by dividing \(M\) by this solvent mass: \(m = M / [\rho - (M \times M_{\text{solute}} / 1000)]\).</p>
          </div>
        </details>
        <details class="faq-item">
          <summary>Does adding salt to cooking water make pasta cook significantly faster?</summary>
          <div class="faq-answer">
            <p>Practically, no. Typical culinary seasoning involves adding about 1 tablespoon (approx. 15 grams) of table salt to 2 liters (2000 g) of boiling water. This corresponds to a molality of \(m = (15 / 58.44) / 2.0 \approx 0.128\text{ mol/kg}\). With \(i = 2\) and \(K_b = 0.512^\circ\text{C}\cdot\text{kg/mol}\), the boiling point elevation is \(\Delta T_b = 2 \times 0.512 \times 0.128 \approx 0.13^\circ\text{C}\). Water boils at 100.13°C instead of 100.00°C—a microscopic temperature rise that does not noticeably accelerate cooking times. Salt is added strictly for culinary flavor seasoning.</p>
          </div>
        </details>
      </div>

      <h2>8. Related Physical Chemistry &amp; Solution Calculators</h2>
      <p>Explore our integrated chemical and thermal calculation tools to analyze solutions, molar quantities, and reactions:</p>
      <div class="related-calculators" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-top: 1rem;">
        <a href="mass-percent-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Mass Percent Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Determine solution weight concentration (% w/w) and solute/solvent mass ratios.</p>
        </a>
        <a href="molarity-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Molarity Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Compute volumetric molarity ($M = \text{mol/L}$) and laboratory compound recipes.</p>
        </a>
        <a href="dilution-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Dilution Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Calculate stock reagent dilutions via standard mass and molar balance ($C_1 V_1 = C_2 V_2$).</p>
        </a>
        <a href="specific-heat-calculator.html" class="calc-card" style="padding: 1rem; text-decoration: none; color: inherit;">
          <h4 style="margin: 0 0 0.5rem 0; color: var(--primary, #2563eb);">Specific Heat Calculator</h4>
          <p style="margin: 0; font-size: 0.85rem; color: var(--text-secondary, #475569);">Calculate sensible heat transfer ($Q = mc\Delta T$) and thermal equilibrium states.</p>
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
          <li><a href="molality-calculator.html">Molality Calculator</a></li>
          <li><a href="mass-percent-calculator.html">Mass Percent</a></li>
          <li><a href="molar-mass-calculator.html">Molar Mass Calculator</a></li>
          <li><a href="dilution-calculator.html">Dilution (C1V1 = C2V2)</a></li>
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
      const solutePreset = document.getElementById('mol-solute-preset');
      const soluteMassInput = document.getElementById('mol-solute-mass');
      const soluteUnitSelect = document.getElementById('mol-solute-unit');
      const molarMassInput = document.getElementById('mol-molar-mass');
      const vanHoffInput = document.getElementById('mol-van-hoff');
      const solventMassInput = document.getElementById('mol-solvent-mass');
      const solventUnitSelect = document.getElementById('mol-solvent-unit');
      const solventPreset = document.getElementById('mol-solvent-preset');

      const calcBtn = document.getElementById('mol-calc-btn');
      const resetBtn = document.getElementById('mol-reset-btn');

      // Outputs
      const primaryOut = document.getElementById('mol-primary-out');
      const statusOut = document.getElementById('mol-status-out');
      const molesOut = document.getElementById('mol-moles-out');
      const freezeOut = document.getElementById('mol-freeze-out');
      const boilOut = document.getElementById('mol-boil-out');
      const massPctOut = document.getElementById('mol-masspct-out');

      const SOLUTES = {
        'nacl': { mw: 58.44, i: 2.0 },
        'glucose': { mw: 180.16, i: 1.0 },
        'sucrose': { mw: 342.30, i: 1.0 },
        'cacl2': { mw: 110.98, i: 3.0 },
        'mgcl2': { mw: 95.21, i: 3.0 },
        'urea': { mw: 60.06, i: 1.0 },
        'etoh': { mw: 46.07, i: 1.0 },
        'eg': { mw: 62.07, i: 1.0 },
        'kcl': { mw: 74.55, i: 2.0 }
      };

      const SOLVENTS = {
        'water': { kf: 1.86, kb: 0.512, tf: 0.0, tb: 100.0 },
        'benzene': { kf: 5.12, kb: 2.53, tf: 5.53, tb: 80.1 },
        'ethanol': { kf: 1.99, kb: 1.22, tf: -114.1, tb: 78.37 },
        'cyclohexane': { kf: 20.2, kb: 2.79, tf: 6.55, tb: 80.74 },
        'camphor': { kf: 40.0, kb: 5.61, tf: 178.4, tb: 204.0 }
      };

      function getSoluteGrams() {
        const val = parseFloat(soluteMassInput.value) || 0;
        const u = soluteUnitSelect.value;
        if (u === 'mg') return val * 0.001;
        if (u === 'kg') return val * 1000;
        if (u === 'lb') return val * 453.59237;
        return val;
      }

      function getSolventKg() {
        const val = parseFloat(solventMassInput.value) || 0;
        const u = solventUnitSelect.value;
        if (u === 'g') return val * 0.001;
        if (u === 'lb') return val * 0.45359237;
        return val; // kg
      }

      function calculate() {
        const soluteGrams = getSoluteGrams();
        const solventKg = getSolventKg();
        const mw = parseFloat(molarMassInput.value) || 58.44;
        const i = parseFloat(vanHoffInput.value) || 1.0;
        const sData = SOLVENTS[solventPreset.value] || SOLVENTS['water'];

        if (soluteGrams <= 0 || solventKg <= 0 || mw <= 0 || i < 1.0) {
          primaryOut.textContent = "-- mol/kg";
          statusOut.textContent = "Please enter valid positive chemical values.";
          return;
        }

        // Moles of solute
        const moles = soluteGrams / mw;
        // Molality (m = moles / kg)
        const molality = moles / solventKg;

        // Colligative properties
        const deltaTf = i * sData.kf * molality;
        const deltaTb = i * sData.kb * molality;
        const newTf = sData.tf - deltaTf;
        const newTb = sData.tb + deltaTb;

        // Mass percent: m_solute / (m_solute + m_solvent) * 100
        const solventGrams = solventKg * 1000;
        const massPct = (soluteGrams / (soluteGrams + solventGrams)) * 100;

        // Render to UI
        primaryOut.textContent = molality.toFixed(3) + " mol/kg";
        statusOut.textContent = `${moles.toFixed(4)} mol Solute in ${solventKg.toFixed(3)} kg Solvent`;
        molesOut.textContent = moles.toFixed(4) + " mol";
        freezeOut.textContent = newTf.toFixed(2) + " °C";
        freezeOut.parentElement.querySelector('div:last-child').textContent = `Depression: ${deltaTf.toFixed(2)} °C`;
        boilOut.textContent = newTb.toFixed(2) + " °C";
        boilOut.parentElement.querySelector('div:last-child').textContent = `Elevation: +${deltaTb.toFixed(2)} °C`;
        massPctOut.textContent = massPct.toFixed(2) + "% w/w";
      }

      // Presets
      solutePreset.addEventListener('change', function() {
        const val = this.value;
        if (SOLUTES[val]) {
          const s = SOLUTES[val];
          molarMassInput.value = s.mw;
          vanHoffInput.value = s.i;
          calculate();
        }
      });

      solventPreset.addEventListener('change', calculate);

      [soluteMassInput, soluteUnitSelect, molarMassInput, vanHoffInput, solventMassInput, solventUnitSelect].forEach(el => {
        el.addEventListener('input', function() {
          solutePreset.value = 'custom';
          calculate();
        });
        el.addEventListener('change', calculate);
      });

      calcBtn.addEventListener('click', calculate);

      resetBtn.addEventListener('click', function() {
        solutePreset.value = 'nacl';
        const s = SOLUTES['nacl'];
        soluteMassInput.value = '58.44';
        soluteUnitSelect.value = 'g';
        molarMassInput.value = s.mw;
        vanHoffInput.value = s.i;
        solventMassInput.value = '1.0';
        solventUnitSelect.value = 'kg';
        solventPreset.value = 'water';
        calculate();
      });

      // Initial execution
      calculate();
    })();
  </script>
</body>
</html>
"""

def generate_files():
    p1 = os.path.join(BASE_DIR, "mass-percent-calculator.html")
    with open(p1, "w", encoding="utf-8") as f:
        f.write(HTML_MASS_PERCENT.strip() + "\n")
    print(f"Generated: {p1}")

    p2 = os.path.join(BASE_DIR, "molality-calculator.html")
    with open(p2, "w", encoding="utf-8") as f:
        f.write(HTML_MOLALITY.strip() + "\n")
    print(f"Generated: {p2}")

if __name__ == "__main__":
    generate_files()
