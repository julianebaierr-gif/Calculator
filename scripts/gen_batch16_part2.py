# -*- coding: utf-8 -*-
"""
Script to generate Batch 16 Part 2 tools:
3. molarity-calculator.html
4. ph-calculator.html
"""
import os

TOOL_3_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Molarity Calculator | Solution Concentration &amp; Mass Sizer</title>
  <meta name="description" content="Calculate molarity (M), mass of solute, solution volume, and molar concentration interconversions. Includes normality, molality, and dilution equivalents.">
  <link rel="canonical" href="https://calchub.cloud/molarity-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "Molarity Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates solution molarity, required solute mass, total volumetric dilution, and chemical reagent concentration for laboratory and industrial formulations.",
        "offers": {
          "@type": "Offer",
          "price": "0.00",
          "priceCurrency": "USD"
        }
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "What is the mathematical definition of molarity?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Molarity (M), or molar concentration, is defined as the number of moles of solute dissolved per liter of total solution volume: M = n / V = m / (MW * V), where n is moles, m is solute mass in grams, MW is the solute molar mass in g/mol, and V is total solution volume in liters."
            }
          },
          {
            "@type": "Question",
            "name": "What is the key difference between molarity (M) and molality (m)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Molarity is moles of solute per liter of total solution (mol/L), whereas molality is moles of solute per kilogram of pure solvent (mol/kg). Molarity changes with temperature because liquid volume expands and contracts thermally, while molality is completely temperature-independent."
            }
          },
          {
            "@type": "Question",
            "name": "How is normality (N) related to molarity?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Normality represents equivalent concentration: N = M * z, where z is the equivalence factor (number of reactive protons H+ for acids, hydroxide ions OH- for bases, or transferred electrons in redox titrations). For instance, a 1.0 M solution of diprotic sulfuric acid (H2SO4) has a normality of 2.0 N."
            }
          },
          {
            "@type": "Question",
            "name": "How does chemical hydration affect the solute mass required for molarity?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "When formulating a solution from a hydrated crystalline chemical (such as copper sulfate pentahydrate CuSO4·5H2O vs anhydrous CuSO4), the water of crystallization must be included in the molar mass. Failing to use the hydrated molecular weight results in under-dosing the active solute species."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="chemical">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">
        <span class="logo-icon">&pi;</span>
        <span class="logo-text">Calc<strong>Hub</strong></span>
      </a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="engineering.html">Engineering</a>
        <a href="mechanical.html">Mechanical</a>
        <a href="civil.html">Civil &amp; Roof</a>
        <a href="solar-energy.html">Solar</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo; 
      <a href="chemical.html">Chemical &amp; Water Treatment</a> &rsaquo; 
      <span>Molarity Calculator</span>
    </nav>

    <h1 class="tool-title">Molarity &amp; Solution Preparation Calculator</h1>
    <p class="tool-subtitle">Molar Concentration (mol/L), Solute Mass Sizing, Volume &amp; Normality Equivalents</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="solutePreset">Chemical Solute Preset</label>
            <select id="solutePreset" class="form-control" onchange="updateSolutePreset()">
              <option value="nacl" selected>Sodium Chloride (NaCl, M = 58.44 g/mol)</option>
              <option value="naoh">Sodium Hydroxide (NaOH, M = 40.00 g/mol)</option>
              <option value="hcl">Hydrochloric Acid (HCl, M = 36.46 g/mol)</option>
              <option value="h2so4">Sulfuric Acid (H₂SO₄, M = 98.08 g/mol, z = 2)</option>
              <option value="glucose">D-Glucose (C₆H₁₂O₆, M = 180.16 g/mol)</option>
              <option value="tris">Tris Base (C₄H₁₁NO₃, M = 121.14 g/mol)</option>
              <option value="kmno4">Potassium Permanganate (KMnO₄, M = 158.03 g/mol)</option>
              <option value="cuso4_5h2o">Copper Sulfate Pentahydrate (CuSO₄·5H₂O, M = 249.68 g/mol)</option>
              <option value="edta">EDTA Disodium Salt (C₁₀H₁₄N₂Na₂O₈·2H₂O, M = 372.24 g/mol)</option>
              <option value="custom">Custom Solute / Unknown Compound</option>
            </select>
          </div>

          <div class="form-group">
            <label for="molaritySolveTarget">Variable to Calculate</label>
            <select id="molaritySolveTarget" class="form-control" onchange="updateMolarityInputs()">
              <option value="mass" selected>Mass of Solute (m) Required [Given M &amp; V]</option>
              <option value="molarity">Molarity (M) [Given Mass &amp; V]</option>
              <option value="volume">Solution Volume (V) [Given Mass &amp; M]</option>
            </select>
          </div>

          <!-- Molar Mass Input -->
          <div class="form-group">
            <label for="soluteMolarMass">Solute Molar Mass (MW) (g/mol)</label>
            <input type="number" id="soluteMolarMass" class="form-control" value="58.44" step="0.01" min="0.1">
          </div>

          <!-- Molarity Input -->
          <div id="molarityInputGroup" class="grid-2-col">
            <div class="form-group">
              <label for="molarityVal">Target Concentration</label>
              <input type="number" id="molarityVal" class="form-control" value="0.5" step="0.05" min="0.000001">
            </div>
            <div class="form-group">
              <label for="molarityUnit">Concentration Unit</label>
              <select id="molarityUnit" class="form-control">
                <option value="m" selected>Molar (M, mol/L)</option>
                <option value="mm">Millimolar (mM, mmol/L)</option>
                <option value="um">Micromolar (&mu;M, &mu;mol/L)</option>
              </select>
            </div>
          </div>

          <!-- Volume Input -->
          <div id="volumeInputGroup" class="grid-2-col">
            <div class="form-group">
              <label for="volumeVal">Solution Volume</label>
              <input type="number" id="volumeVal" class="form-control" value="1.0" step="0.1" min="0.000001">
            </div>
            <div class="form-group">
              <label for="volumeUnit">Volume Unit</label>
              <select id="volumeUnit" class="form-control">
                <option value="l" selected>Liters (L)</option>
                <option value="ml">Milliliters (mL)</option>
                <option value="ul">Microliters (&mu;L)</option>
                <option value="m3">Cubic Meters (m³)</option>
                <option value="gal">US Gallons</option>
              </select>
            </div>
          </div>

          <!-- Mass Input -->
          <div id="massInputGroup" class="grid-2-col" style="display: none;">
            <div class="form-group">
              <label for="massVal">Solute Mass</label>
              <input type="number" id="massVal" class="form-control" value="29.22" step="0.1" min="0.000001">
            </div>
            <div class="form-group">
              <label for="massUnit">Mass Unit</label>
              <select id="massUnit" class="form-control">
                <option value="g" selected>Grams (g)</option>
                <option value="mg">Milligrams (mg)</option>
                <option value="kg">Kilograms (kg)</option>
                <option value="lb">Pounds (lbs)</option>
              </select>
            </div>
          </div>

          <div class="form-group">
            <label for="soluteEquivZ">Valence Factor (z) for Normality</label>
            <input type="number" id="soluteEquivZ" class="form-control" value="1" step="1" min="1" max="6">
            <span class="field-hint">1 for monoprotic (HCl, NaOH), 2 for diprotic (H₂SO₄), 3 for triprotic (H₃PO₄)</span>
          </div>

          <button type="button" class="btn btn-primary" onclick="calcMolarity()" style="width: 100%; margin-top: 15px;">Calculate Solution Concentration</button>
        </div>
      </div>

      <!-- Output Results Panel -->
      <div class="results-card">
        <div class="result-box primary-result">
          <div id="resPrimaryLabel" class="result-label">Required Solute Mass (m)</div>
          <div id="resPrimaryVal" class="result-value">29.220 grams</div>
          <div id="resPrimaryAlt" class="result-subtext">0.02922 kg (0.06442 lbs)</div>
        </div>

        <div class="result-grid">
          <div class="result-item">
            <span class="result-label">Molar Concentration (M)</span>
            <span id="resMolarConc" class="result-value highlight">0.500 M</span>
            <span id="resMolarConcSub" class="result-subtext">500.0 mM (0.500 mol/L)</span>
          </div>
          <div class="result-item">
            <span class="result-label">Total Substance Quantity</span>
            <span id="resMolesTotal" class="result-value">0.500 mol</span>
            <span class="result-subtext">Moles of active solute</span>
          </div>
          <div class="result-item">
            <span class="result-label">Normality Equivalent (N)</span>
            <span id="resNormality" class="result-value">0.500 N</span>
            <span class="result-subtext">N = M &times; z (eq/L)</span>
          </div>
          <div class="result-item">
            <span class="result-label">Mass Concentration (ppm)</span>
            <span id="resMassPpm" class="result-value">29,220 mg/L</span>
            <span class="result-subtext">29.22 g/L (ppm in water)</span>
          </div>
          <div class="result-item">
            <span class="result-label">Weight Percent (% w/v)</span>
            <span id="resWeightVolPct" class="result-value">2.922%</span>
            <span class="result-subtext">Grams solute per 100 mL</span>
          </div>
          <div class="result-item">
            <span class="result-label">Total Molecules Dissolved</span>
            <span id="resMoleculesTotal" class="result-value">3.011 &times; 10²³</span>
            <span class="result-subtext">Via Avogadro constant Nₐ</span>
          </div>
        </div>

        <div class="result-details" style="margin-top: 15px;">
          <p><strong>Bench Preparation Protocol:</strong> <span id="resPrepProtocol">Weigh 29.220 g of solute, dissolve in ~800 mL deionized water, then bring to exactly 1.000 L mark.</span></p>
          <p><strong>Volumetric Tolerance:</strong> <span id="resToleranceNote">Standard Class A volumetric glassware provides &plusmn;0.2% measurement accuracy at 20&deg;C.</span></p>
        </div>
      </div>
    </div>

    <!-- 1000+ Words Engineering Body -->
    <article class="article-body">
      <h2>Principles of Chemical Solution Concentrations</h2>
      <p>In analytical chemistry, biochemical pharmacology, and industrial process engineering, accurate solution preparation constitutes the foundational prerequisite for all experimental reproducibility and manufacturing quality control. Whether preparing high-purity mobile phases for high-performance liquid chromatography (HPLC), formulating parenteral electrolyte infusions, or dosing coagulants in municipal water treatment, engineers must precisely regulate the number of dissolved solute particles per unit volume of solvent.</p>

      <p>The primary quantitative metric for liquid solutions is <strong>molarity</strong> (also termed <em>molar concentration</em>, designated by symbol $M$ or $c$), defined by the International Union of Pure and Applied Chemistry (IUPAC) as the amount of substance in moles divided by the total final volume of the solution in liters:</p>

      <div class="formula-box">
        $$M = \frac{n}{V} = \frac{m}{M_w \cdot V}$$
      </div>

      <p>Where $n$ represents the substance quantity in moles ($\text{mol}$), $m$ is the physical mass of the solute in grams ($\text{g}$), $M_w$ is the molar mass (molecular weight) of the solute in grams per mole ($\text{g/mol}$), and $V$ is the total final solution volume in liters ($\text{L}$). Under standard SI convention, molarity is expressed in units of $\text{mol/dm}^3$, $\text{mol/L}$, or represented simply by the capitalized unit symbol $\text{M}$.</p>

      <h2>Mathematical Rearrangements for Laboratory Bench Calculations</h2>
      <p>Depending on the laboratory scenario, the governing equation is rearranged algebraically to solve for the target operational parameter:</p>

      <h3>1. Calculating Solute Mass Required to Formulate a Specific Volume</h3>
      <p>When a chemist needs to prepare a target volume $V$ at an exact molarity $M$:</p>
      <div class="formula-box">
        $$m\text{ (grams)} = M\text{ (mol/L)} \times V\text{ (L)} \times M_w\text{ (g/mol)}$$
      </div>
      <p>For micro-scale and biochemical solutions where concentrations are specified in millimolar ($\text{mM} = 10^{-3}\text{ M}$) or micromolar ($\mu\text{M} = 10^{-6}\text{ M}$) and volumes in milliliters ($\text{mL} = 10^{-3}\text{ L}$):</p>
      <div class="formula-box">
        $$m\text{ (mg)} = M\text{ (mM)} \times V\text{ (mL)} \times M_w\text{ (g/mol)} \times 10^{-3}$$
      </div>

      <h3>2. Calculating Molarity from Observed Solute Mass</h3>
      <p>When an existing mass of solute $m$ is dissolved into a known volumetric flask $V$:</p>
      <div class="formula-box">
        $$M\text{ (mol/L)} = \frac{m\text{ (g)}}{M_w\text{ (g/mol)} \times V\text{ (L)}}$$
      </div>

      <h3>3. Calculating Maximum Deliverable Solution Volume</h3>
      <p>When a limited inventory of chemical reagent $m$ is available and a fixed molarity $M$ is mandated:</p>
      <div class="formula-box">
        $$V\text{ (L)} = \frac{m\text{ (g)}}{M\text{ (mol/L)} \times M_w\text{ (g/mol)}}$$
      </div>

      <h2>Normality (N) and Equivalence Factors (z)</h2>
      <p>In acid-base neutralization and oxidation-reduction titrations, stoichiometry frequently involves multivalent interactions. <strong>Normality</strong> ($N$) represents the equivalent concentration of a solution, defined as the number of gram-equivalents of solute per liter of solution:</p>

      <div class="formula-box">
        $$N = M \times z$$
      </div>

      <p>Where $z$ denotes the integer <strong>equivalence factor</strong>:</p>
      <ul>
        <li><strong>For Acids:</strong> $z$ is the number of reactive hydronium ions ($\text{H}^+$) yielded per molecule. For hydrochloric acid ($\text{HCl}$), $z = 1$, so $1.0\text{ M} = 1.0\text{ N}$. For diprotic sulfuric acid ($\text{H}_2\text{SO}_4$), $z = 2$, so $1.0\text{ M} = 2.0\text{ N}$. For triprotic phosphoric acid ($\text{H}_3\text{PO}_4$), $z = 3$, so $1.0\text{ M} = 3.0\text{ N}$.</li>
        <li><strong>For Bases:</strong> $z$ is the number of hydroxide ions ($\text{OH}^-$) neutralized. For sodium hydroxide ($\text{NaOH}$), $z = 1$; for calcium hydroxide ($\text{Ca(OH)}_2$), $z = 2$.</li>
        <li><strong>For Redox Reagents:</strong> $z$ is the number of electrons ($\text{e}^-$) transferred per formula unit. For potassium permanganate ($\text{KMnO}_4$) in acidic media ($\text{Mn}^{7+} + 5\text{e}^- \to \text{Mn}^{2+}$), $z = 5$, making a $0.10\text{ M KMnO}_4$ solution equivalent to $0.50\text{ N}$.</li>
      </ul>

      <h2>Molarity vs. Molality vs. Mass Percentage Comparison Table</h2>
      <p>Different concentration scales serve distinct thermodynamic and physical functions. The table below delineates the mathematical definitions, temperature dependencies, and appropriate scientific use cases:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Concentration Unit</th>
              <th>Symbol</th>
              <th>Formal Definition</th>
              <th>Dimensional Units</th>
              <th>Temperature Sensitive?</th>
              <th>Primary Industrial / Laboratory Use</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Molarity</td>
              <td>M or c</td>
              <td>Moles of solute / Liters of total solution</td>
              <td>mol / L (mol / dm³)</td>
              <td>Yes (liquids expand thermally)</td>
              <td>Standard bench wet-chemistry, titrations, buffers</td>
            </tr>
            <tr>
              <td>Molality</td>
              <td>m or b</td>
              <td>Moles of solute / Kilograms of pure solvent</td>
              <td>mol / kg solvent</td>
              <td>No (mass is conserved)</td>
              <td>Colligative properties (boiling elevation, freezing depression)</td>
            </tr>
            <tr>
              <td>Normality</td>
              <td>N</td>
              <td>Equivalents of solute / Liters of solution</td>
              <td>eq / L</td>
              <td>Yes</td>
              <td>Acid-base and redox analytical titrimetry</td>
            </tr>
            <tr>
              <td>Mass Percent</td>
              <td>% w/w</td>
              <td>(Mass solute / Total solution mass) &times; 100%</td>
              <td>Dimensionless %</td>
              <td>No</td>
              <td>Commercial bulk reagents (e.g., 37% HCl, 50% NaOH)</td>
            </tr>
            <tr>
              <td>Parts per Million</td>
              <td>ppm</td>
              <td>mg solute / Liters of solution (or kg total)</td>
              <td>mg / L &asymp; ppm</td>
              <td>Negligible in dilute water</td>
              <td>Environmental trace contaminants, water quality limits</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Practical Worked Case Study: Formulating 2.50 L of 0.200 M Potassium Permanganate</h2>
      <div class="worked-example-card">
        <h3>Analytical Chemistry Case Study: Preparing a Primary Redox Titrant</h3>
        <p><strong>Scenario:</strong> An environmental analytical laboratory requires $V = 2.50\text{ Liters}$ of a $M = 0.200\text{ mol/L (M)}$ potassium permanganate ($\text{KMnO}_4$) standard titrant for chemical oxygen demand (COD) assays under EPA Method 410. The molecular weight of pure crystalline $\text{KMnO}_4$ is $M_w = 158.034\text{ g/mol}$. In an acidic redox titration ($\text{MnO}_4^- + 8\text{H}^+ + 5\text{e}^- \to \text{Mn}^{2+} + 4\text{H}_2\text{O}$), the equivalence factor is $z = 5$. Determine: (1) the gravimetric mass of dry salt required, (2) the normality of the solution, (3) the mass concentration in parts per million ($\text{mg/L}$), and (4) the precise Class A volumetric laboratory preparation protocol.</p>

        <p><strong>Step 1: Calculate Total Moles Required:</strong></p>
        $$n = M \times V = 0.200\text{ mol/L} \times 2.50\text{ L} = 0.500\text{ moles of KMnO}_4$$

        <p><strong>Step 2: Compute Gravimetric Solute Mass:</strong></p>
        $$m = n \times M_w = 0.500\text{ mol} \times 158.034\text{ g/mol} = 79.017\text{ grams of pure KMnO}_4$$

        <p><strong>Step 3: Determine Normality (N):</strong></p>
        $$N = M \times z = 0.200\text{ M} \times 5\text{ eq/mol} = 1.000\text{ N (Normal)}$$

        <p><strong>Step 4: Compute Mass Concentration and Weight Percent:</strong></p>
        $$\text{Mass Concentration} = \frac{79.017\text{ g}}{2.50\text{ L}} = 31.607\text{ g/L} = 31,607\text{ mg/L (ppm)}$$
        $$\% \text{w/v} = \frac{79.017\text{ g}}{2,500\text{ mL}} \times 100\% = 3.161\%\text{ w/v}$$

        <p><strong>Step 5: Rigorous Standard Operating Procedure (SOP):</strong></p>
        <ol>
          <li>Tear an analytical balance ($\pm 0.0001\text{ g}$ precision) with an acid-washed glass weighing boat.</li>
          <li>Weigh exactly $79.017\text{ g}$ of reagent-grade dry crystalline $\text{KMnO}_4$.</li>
          <li>Transfer the dry crystals quantitatively into a clean $2\text{ Liter}$ borosilicate beaker containing approximately $1,500\text{ mL}$ of boiling deionized water (high heat accelerates dissolution of dark purple $\text{KMnO}_4$).</li>
          <li>Cool the solution to $20.0^\circ\text{C}$ (calibrated glassware reference temperature).</li>
          <li>Filter through a sintered glass crucible (to remove trace manganese dioxide $\text{MnO}_2$ precipitates) into a calibrated $2,500\text{ mL}$ Class A volumetric flask.</li>
          <li>Dilute with deionized water until the bottom of the curved purple meniscus aligns tangentially with the calibration graduation mark. Stopper and invert 20 times to achieve complete concentration homogeneity.</li>
        </ol>
      </div>

      <h2>Thermal Expansion and Volumetric Glassware Calibration</h2>
      <p>Because liquids expand and contract thermally (for pure water, volumetric thermal expansion coefficient $\beta \approx 2.1 \times 10^{-4}\text{ K}^{-1}$ at $20^\circ\text{C}$), a solution prepared at $20^\circ\text{C}$ will expand by approximately $0.4\%\text{ to } 0.8\%$ when warmed to typical summer ambient temperatures of $30^\circ\text{C}\text{ to } 35^\circ\text{C}$. This thermal expansion increases solution volume $V$, causing the true molarity to drop:</p>

      <div class="formula-box">
        $$M_{T_2} = M_{T_1} \times \left( \frac{\rho_{T_2}}{\rho_{T_1}} \right)$$
      </div>
      <p>Where $\rho_T$ denotes solution density at temperature $T$. For precision titrations conforming to ISO 17025 standards, chemists must either utilize temperature-controlled water baths, apply volumetric temperature correction factors, or utilize molality ($m$), which remains strictly invariant with temperature.</p>
    </article>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-grid">
        <div class="footer-col">
          <div class="footer-logo">
            <span class="logo-icon">&pi;</span>
            <span class="logo-text">Calc<strong>Hub</strong></span>
          </div>
          <p class="footer-about">High-precision chemical concentration, solution stoichiometry, and laboratory molarity preparation tools conforming to IUPAC and NIST standards.</p>
        </div>
        <div class="footer-col">
          <h4 class="footer-title">Engineering Disciplines</h4>
          <ul class="footer-links">
            <li><a href="chemical.html">Chemical &amp; Water Treatment</a></li>
            <li><a href="mechanical.html">Mechanical &amp; HVAC</a></li>
            <li><a href="engineering.html">Electrical &amp; Electronics</a></li>
            <li><a href="civil.html">Civil &amp; Construction</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4 class="footer-title">Standard References</h4>
          <ul class="footer-links">
            <li><a href="https://www.iupac.org" target="_blank" rel="noopener">IUPAC Compendium of Chemical Terminology</a></li>
            <li><a href="https://webbook.nist.gov" target="_blank" rel="noopener">NIST Standard Reference Data</a></li>
            <li><a href="https://www.iso.org" target="_blank" rel="noopener">ISO 17025 Laboratory Testing Standards</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    const SOLUTE_PRESETS = {
      nacl: { mw: 58.44, z: 1 },
      naoh: { mw: 40.00, z: 1 },
      hcl: { mw: 36.46, z: 1 },
      h2so4: { mw: 98.08, z: 2 },
      glucose: { mw: 180.16, z: 1 },
      tris: { mw: 121.14, z: 1 },
      kmno4: { mw: 158.03, z: 5 },
      cuso4_5h2o: { mw: 249.68, z: 2 },
      edta: { mw: 372.24, z: 2 },
      custom: { mw: 58.44, z: 1 }
    };

    function updateSolutePreset() {
      const p = document.getElementById("solutePreset").value;
      if (p !== "custom") {
        const item = SOLUTE_PRESETS[p];
        document.getElementById("soluteMolarMass").value = item.mw;
        document.getElementById("soluteEquivZ").value = item.z;
        calcMolarity();
      }
    }

    function updateMolarityInputs() {
      const target = document.getElementById("molaritySolveTarget").value;
      document.getElementById("molarityInputGroup").style.display = target === "molarity" ? "none" : "grid";
      document.getElementById("volumeInputGroup").style.display = target === "volume" ? "none" : "grid";
      document.getElementById("massInputGroup").style.display = (target === "molarity" || target === "volume") ? "grid" : "none";
    }

    function calcMolarity() {
      const target = document.getElementById("molaritySolveTarget").value;
      const mw = parseFloat(document.getElementById("soluteMolarMass").value) || 58.44;
      const z = parseFloat(document.getElementById("soluteEquivZ").value) || 1;

      // Extract Molarity
      let M = 0.5;
      if (target !== "molarity") {
        let mVal = parseFloat(document.getElementById("molarityVal").value) || 0.5;
        let mUnit = document.getElementById("molarityUnit").value;
        if (mUnit === "m") M = mVal;
        else if (mUnit === "mm") M = mVal / 1000.0;
        else if (mUnit === "um") M = mVal / 1000000.0;
      }

      // Extract Volume in Liters
      let V_liters = 1.0;
      if (target !== "volume") {
        let vVal = parseFloat(document.getElementById("volumeVal").value) || 1.0;
        let vUnit = document.getElementById("volumeUnit").value;
        if (vUnit === "l") V_liters = vVal;
        else if (vUnit === "ml") V_liters = vVal / 1000.0;
        else if (vUnit === "ul") V_liters = vVal / 1000000.0;
        else if (vUnit === "m3") V_liters = vVal * 1000.0;
        else if (vUnit === "gal") V_liters = vVal * 3.78541;
      }

      // Extract Mass in Grams
      let mass_grams = 0;
      if (target === "molarity" || target === "volume") {
        let massVal = parseFloat(document.getElementById("massVal").value) || 29.22;
        let massUnit = document.getElementById("massUnit").value;
        if (massUnit === "g") mass_grams = massVal;
        else if (massUnit === "mg") mass_grams = massVal / 1000.0;
        else if (massUnit === "kg") mass_grams = massVal * 1000.0;
        else if (massUnit === "lb") mass_grams = massVal * 453.592;
      }

      let primaryLabel = "";
      let primaryVal = "";
      let primaryAlt = "";

      if (target === "mass") {
        mass_grams = M * V_liters * mw;
        primaryLabel = "Required Solute Mass (m)";
        if (mass_grams >= 1000) {
          primaryVal = (mass_grams / 1000.0).toFixed(3) + " kg";
          primaryAlt = mass_grams.toFixed(2) + " grams (" + (mass_grams * 0.00220462).toFixed(3) + " lbs)";
        } else if (mass_grams < 0.01) {
          primaryVal = (mass_grams * 1000.0).toFixed(2) + " mg";
          primaryAlt = mass_grams.toExponential(3) + " grams";
        } else {
          primaryVal = mass_grams.toFixed(3) + " grams";
          primaryAlt = (mass_grams / 1000.0).toFixed(5) + " kg (" + (mass_grams * 0.00220462).toFixed(4) + " lbs)";
        }
      } else if (target === "molarity") {
        M = mass_grams / (mw * V_liters);
        primaryLabel = "Resultant Molarity (M)";
        primaryVal = M < 0.001 ? M.toExponential(4) + " M" : M.toFixed(4) + " M";
        primaryAlt = (M * 1000.0).toFixed(2) + " mM (" + (M * 1e6).toFixed(1) + " μM)";
      } else if (target === "volume") {
        V_liters = mass_grams / (M * mw);
        primaryLabel = "Resultant Solution Volume (V)";
        if (V_liters >= 1.0) {
          primaryVal = V_liters.toFixed(3) + " Liters";
          primaryAlt = (V_liters * 1000.0).toFixed(1) + " mL (" + (V_liters * 0.264172).toFixed(3) + " US gal)";
        } else {
          primaryVal = (V_liters * 1000.0).toFixed(2) + " mL";
          primaryAlt = V_liters.toFixed(5) + " Liters (" + (V_liters * 1e6).toFixed(0) + " μL)";
        }
      }

      const totalMoles = M * V_liters;
      const normality = M * z;
      const massConcMgL = (mass_grams / V_liters) * 1000.0;
      const weightVolPct = (mass_grams / (V_liters * 1000.0)) * 100.0;
      const totalMolecules = totalMoles * 6.02214076e23;

      document.getElementById("resPrimaryLabel").textContent = primaryLabel;
      document.getElementById("resPrimaryVal").textContent = primaryVal;
      document.getElementById("resPrimaryAlt").textContent = primaryAlt;

      document.getElementById("resMolarConc").textContent = M < 0.001 ? M.toExponential(3) + " M" : M.toFixed(4) + " M";
      document.getElementById("resMolarConcSub").textContent = (M * 1000.0).toFixed(2) + " mM (" + (M * 1e6).toFixed(1) + " μM)";

      document.getElementById("resMolesTotal").textContent = totalMoles < 0.001 ? totalMoles.toExponential(3) + " mol" : totalMoles.toFixed(4) + " mol";
      document.getElementById("resNormality").textContent = normality.toFixed(4) + " N (z = " + z + ")";
      document.getElementById("resMassPpm").textContent = massConcMgL.toLocaleString(undefined, {maximumFractionDigits: 1}) + " mg/L";
      document.getElementById("resWeightVolPct").textContent = weightVolPct.toFixed(3) + "% w/v";
      document.getElementById("resMoleculesTotal").textContent = totalMolecules.toExponential(3);

      let prepStr = "Weigh " + (mass_grams >= 1000 ? (mass_grams / 1000).toFixed(3) + " kg" : mass_grams.toFixed(3) + " g") + " of solute, dissolve in ~" + (V_liters * 0.75).toFixed(2) + " L solvent, then dilute to exactly " + V_liters.toFixed(3) + " L mark.";
      document.getElementById("resPrepProtocol").textContent = prepStr;
    }

    window.addEventListener("DOMContentLoaded", () => {
      calcMolarity();
    });
  </script>
</body>
</html>
"""

TOOL_4_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>pH Calculator | Aqueous [H+] Hydronium &amp; pOH Equilibrium Solver</title>
  <meta name="description" content="Calculate pH, pOH, [H+] hydronium ion concentration, [OH-] hydroxide, and degree of ionization for strong/weak acids and bases across 0°C to 100°C.">
  <link rel="canonical" href="https://calchub.cloud/ph-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "pH Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates aqueous pH, pOH, hydronium ion concentration, and weak acid-base chemical equilibria using exact quadratic and temperature-adjusted Kw formulations.",
        "offers": {
          "@type": "Offer",
          "price": "0.00",
          "priceCurrency": "USD"
        }
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "What is the mathematical definition of pH?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Originally formulated by Søren Sørensen in 1909, pH is the negative decimal logarithm of the thermodynamic hydronium (or hydrogen) ion activity: pH = -log10[H3O+]. In dilute aqueous solutions where activity coefficients approach unity, concentration in mol/L is used directly."
            }
          },
          {
            "@type": "Question",
            "name": "How does water temperature change neutral pH?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The autoionization of water 2H2O <=> H3O+ + OH- is endothermic. As temperature rises from 0°C to 100°C, the ion product Kw increases from 0.114x10^-14 to 51.3x10^-14 (pKw drops from 14.94 to 12.29). Consequently, pure neutral water ([H+] = [OH-]) has a pH of 7.47 at 0°C, 7.00 at 25°C, and 6.14 at 100°C."
            }
          },
          {
            "@type": "Question",
            "name": "How do you calculate pH for a weak acid using the quadratic equation?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For weak acid HA <=> H+ + A- with equilibrium constant Ka and initial concentration C, mass action gives Ka = [H+]^2 / (C - [H+]). Rearranging yields the quadratic equation [H+]^2 + Ka[H+] - Ka*C = 0. Solving via quadratic formula yields [H+] = (-Ka + sqrt(Ka^2 + 4*Ka*C)) / 2, avoiding inaccurate simplifications when Ka/C exceeds 0.05."
            }
          },
          {
            "@type": "Question",
            "name": "Can pH ever be negative or greater than 14?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes. The standard 0 to 14 scale reflects dilute aqueous solutions around 25°C. Highly concentrated strong acids (such as concentrated 12 M HCl with [H+] = 12 mol/L) have a theoretical pH of -log10(12) = -1.08. Conversely, concentrated 10 M NaOH has a theoretical pOH of -1.00 and pH of 15.00."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="chemical">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">
        <span class="logo-icon">&pi;</span>
        <span class="logo-text">Calc<strong>Hub</strong></span>
      </a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="engineering.html">Engineering</a>
        <a href="mechanical.html">Mechanical</a>
        <a href="civil.html">Civil &amp; Roof</a>
        <a href="solar-energy.html">Solar</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo; 
      <a href="chemical.html">Chemical &amp; Water Treatment</a> &rsaquo; 
      <span>pH Calculator</span>
    </nav>

    <h1 class="tool-title">Aqueous pH &amp; [H⁺] / [OH⁻] Equilibrium Calculator</h1>
    <p class="tool-subtitle">Hydronium Concentration, Strong/Weak Acids &amp; Bases, pOH &amp; Temperature-Adjusted Kw</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="electrolyteTypeSelect">Chemical Electrolyte Classification</label>
            <select id="electrolyteTypeSelect" class="form-control" onchange="updateElectrolyteType()">
              <option value="strong_acid" selected>Strong Monoprotic Acid (HCl, HNO₃, HClO₄)</option>
              <option value="strong_acid_di">Strong Diprotic Acid (H₂SO₄)</option>
              <option value="strong_base">Strong Monobasic Base (NaOH, KOH, LiOH)</option>
              <option value="strong_base_di">Strong Dibasic Base [Ca(OH)₂, Ba(OH)₂]</option>
              <option value="weak_acid">Weak Acid (Acetic, Formic, Citric) - Ka Solver</option>
              <option value="weak_base">Weak Base (Ammonia, Methylamine) - Kb Solver</option>
              <option value="direct_ph">Direct pH / [H⁺] / [OH⁻] Value Conversion</option>
            </select>
          </div>

          <!-- Direct Input Value (when direct_ph selected) -->
          <div id="directInputGroup" class="grid-2-col" style="display: none;">
            <div class="form-group">
              <label for="directVal">Enter Known Parameter</label>
              <input type="number" id="directVal" class="form-control" value="7.0" step="0.1">
            </div>
            <div class="form-group">
              <label for="directType">Parameter Type</label>
              <select id="directType" class="form-control">
                <option value="ph" selected>pH</option>
                <option value="poh">pOH</option>
                <option value="h">Hydronium [H⁺] (mol/L)</option>
                <option value="oh">Hydroxide [OH⁻] (mol/L)</option>
              </select>
            </div>
          </div>

          <!-- Concentration Input -->
          <div id="concInputGroup" class="grid-2-col">
            <div class="form-group">
              <label for="soluteConcVal">Analytical Solute Concentration (C)</label>
              <input type="number" id="soluteConcVal" class="form-control" value="0.05" step="0.01" min="0.000000001">
            </div>
            <div class="form-group">
              <label for="soluteConcUnit">Concentration Unit</label>
              <select id="soluteConcUnit" class="form-control">
                <option value="m" selected>Molar (M, mol/L)</option>
                <option value="mm">Millimolar (mM, mmol/L)</option>
                <option value="um">Micromolar (&mu;M)</option>
              </select>
            </div>
          </div>

          <!-- Ka / pKa Input for Weak Acid -->
          <div id="weakAcidGroup" class="grid-2-col" style="display: none;">
            <div class="form-group">
              <label for="weakAcidPreset">Acid Preset</label>
              <select id="weakAcidPreset" class="form-control" onchange="updateWeakAcidPreset()">
                <option value="acetic" selected>Acetic Acid (CH₃COOH, pKa = 4.76)</option>
                <option value="formic">Formic Acid (HCOOH, pKa = 3.75)</option>
                <option value="benzoic">Benzoic Acid (C₆H₅COOH, pKa = 4.20)</option>
                <option value="hf">Hydrofluoric Acid (HF, pKa = 3.17)</option>
                <option value="custom">Custom pKa Entry</option>
              </select>
            </div>
            <div class="form-group">
              <label for="acidPkaVal">Acid Dissociation pKₐ</label>
              <input type="number" id="acidPkaVal" class="form-control" value="4.76" step="0.01" min="0.0">
            </div>
          </div>

          <!-- Kb / pKb Input for Weak Base -->
          <div id="weakBaseGroup" class="grid-2-col" style="display: none;">
            <div class="form-group">
              <label for="weakBasePreset">Base Preset</label>
              <select id="weakBasePreset" class="form-control" onchange="updateWeakBasePreset()">
                <option value="ammonia" selected>Ammonia (NH₃, pKb = 4.75)</option>
                <option value="methylamine">Methylamine (CH₃NH₂, pKb = 3.36)</option>
                <option value="pyridine">Pyridine (C₅H₅N, pKb = 8.77)</option>
                <option value="custom">Custom pKb Entry</option>
              </select>
            </div>
            <div class="form-group">
              <label for="basePkbVal">Base Dissociation pK_b</label>
              <input type="number" id="basePkbVal" class="form-control" value="4.75" step="0.01" min="0.0">
            </div>
          </div>

          <!-- Solution Temperature -->
          <div class="form-group">
            <label for="solnTempC">Solution Temperature (&deg;C) [Kw Shift]</label>
            <input type="number" id="solnTempC" class="form-control" value="25.0" step="1.0" min="0.0" max="100.0">
            <span class="field-hint">Autoionization Kw changes from 14.94 at 0&deg;C to 12.29 at 100&deg;C</span>
          </div>

          <button type="button" class="btn btn-primary" onclick="calcPH()" style="width: 100%; margin-top: 15px;">Compute Equilibrium pH &amp; Ions</button>
        </div>
      </div>

      <!-- Output Results Panel -->
      <div class="results-card">
        <div class="result-box primary-result">
          <div class="result-label">Resultant Solution pH</div>
          <div id="resPHVal" class="result-value">1.30 pH</div>
          <div id="resPHCategory" class="result-subtext">Strongly Acidic | pOH = 12.70</div>
        </div>

        <div class="result-grid">
          <div class="result-item">
            <span class="result-label">Hydronium Ion [H₃O⁺]</span>
            <span id="resHydroniumVal" class="result-value highlight">5.00 &times; 10⁻² M</span>
            <span id="resHydroniumSub" class="result-subtext">0.0500 mol/L</span>
          </div>
          <div class="result-item">
            <span class="result-label">Hydroxide Ion [OH⁻]</span>
            <span id="resHydroxideVal" class="result-value">2.00 &times; 10⁻¹³ M</span>
            <span id="resHydroxideSub" class="result-subtext">0.200 pmol/L</span>
          </div>
          <div class="result-item">
            <span class="result-label">Solution pOH</span>
            <span id="resPOHVal" class="result-value">12.70</span>
            <span class="result-subtext">pOH = -log₁₀[OH⁻]</span>
          </div>
          <div class="result-item">
            <span class="result-label">Degree of Ionization (&alpha;)</span>
            <span id="resIonizationAlpha" class="result-value">100.0%</span>
            <span class="result-subtext">Completely dissociated</span>
          </div>
          <div class="result-item">
            <span class="result-label">Autoionization pK_w</span>
            <span id="resPKwVal" class="result-value">14.00</span>
            <span id="resPKwSub" class="result-subtext">Neutrality pH = 7.00 at 25°C</span>
          </div>
          <div class="result-item">
            <span class="result-label">Acid/Base Dissociation K</span>
            <span id="resEquilKVal" class="result-value">&infin; (Strong)</span>
            <span class="result-subtext">Complete forward reaction</span>
          </div>
        </div>

        <div class="result-details" style="margin-top: 15px;">
          <p><strong>Equilibrium Chemistry Status:</strong> <span id="resChemStatus">Hydrochloric Acid complete dissociation into H⁺ and Cl⁻ ions.</span></p>
          <p><strong>Colorimetric Indicator Anticipation:</strong> <span id="resIndicatorColor">Universal Indicator: Deep Red (pH &lt; 2) | Phenolphthalein: Colorless.</span></p>
        </div>
      </div>
    </div>

    <!-- 1000+ Words Engineering Body -->
    <article class="article-body">
      <h2>Thermodynamic Foundation of the pH Scale</h2>
      <p>The concept of <strong>pH</strong> (from the Latin <em>potentia hydrogenii</em>, power of hydrogen) was conceived in 1909 by Danish biochemist Søren Peder Lauritz Sørensen at the Carlsberg Laboratory as a logarithmic scale to compress vastly sprawling hydronium ion concentrations spanning over 14 orders of magnitude into an intuitive operational metric. In modern physical chemistry and IUPAC metrology, pH is rigorously defined as the negative base-10 logarithm of the thermodynamic activity of the aqueous hydronium ion ($a_{\text{H}_3\text{O}^+}$):</p>

      <div class="formula-box">
        $$\text{pH} = -\log_{10}(a_{\text{H}_3\text{O}^+}) = -\log_{10}\left(\gamma_{\text{H}^+} \cdot \frac{[\text{H}_3\text{O}^+]}{c^\circ}\right)$$
      </div>

      <p>Where $[\text{H}_3\text{O}^+]$ is the analytical molar concentration of hydronium in $\text{mol/L}$, $c^\circ = 1.0\text{ mol/L}$ is the thermodynamic standard state reference, and $\gamma_{\text{H}^+}$ is the single-ion activity coefficient. In dilute aqueous solutions ($c &lt; 0.1\text{ M}$), electrostatic interactions between ions are minimal, allowing the activity coefficient to approach unity ($\gamma_{\text{H}^+} \approx 1.0$), reducing the formal relationship to the familiar practical expression:</p>

      <div class="formula-box">
        $$\text{pH} \approx -\log_{10}[\text{H}_3\text{O}^+] \quad \iff \quad [\text{H}_3\text{O}^+] = 10^{-\text{pH}}$$
      </div>

      <p>Analogously, the <strong>pOH</strong> scale measures the negative base-10 logarithm of the free aqueous hydroxide ion concentration:</p>

      <div class="formula-box">
        $$\text{pOH} = -\log_{10}[\text{OH}^-] \quad \iff \quad [\text{OH}^-] = 10^{-\text{pOH}}$$
      </div>

      <h2>Autoionization of Water and the Ion Product (Kw)</h2>
      <p>Pure liquid water is not an inert solvent; it spontaneously undergoes self-ionization (autoprotolysis), in which one amphiprotic water molecule donates a proton to another:</p>

      <div class="formula-box">
        $$2\text{H}_2\text{O (l)} \rightleftharpoons \text{H}_3\text{O}^+\text{ (aq)} + \text{OH}^-\text{ (aq)}$$
      </div>

      <p>The thermodynamic equilibrium constant for this autoprotolysis reaction is the <strong>ion product of water</strong> ($K_w$):</p>

      <div class="formula-box">
        $$K_w = [\text{H}_3\text{O}^+][\text{OH}^-]$$
      </div>

      <p>Taking the negative logarithm of both sides yields the fundamental reciprocal relationship connecting pH and pOH:</p>

      <div class="formula-box">
        $$-\log_{10}(K_w) = -\log_{10}[\text{H}_3\text{O}^+] - \log_{10}[\text{OH}^-] \quad \implies \quad pK_w = \text{pH} + \text{pOH}$$
      </div>

      <h2>Temperature Dependence of Kw and the Neutrality Threshold</h2>
      <p>A critical engineering fallacy is the assumption that "neutral pH is always 7.00." Because the autodissociation of water breaks covalent bonds, it is an endothermic thermodynamic process ($\Delta H^\circ = +55.8\text{ kJ/mol}$). By Le Chatelier's principle, elevating temperature drives the forward equilibrium, generating higher concentrations of both $[\text{H}_3\text{O}^+]$ and $[\text{OH}^-]$ simultaneously. As temperature increases from freezing ($0^\circ\text{C}$) to boiling ($100^\circ\text{C}$), $K_w$ increases by more than 400-fold!</p>

      <div class="formula-box">
        $$\text{Neutrality Condition: } [\text{H}_3\text{O}^+] = [\text{OH}^-] = \sqrt{K_w} \quad \implies \quad \text{pH}_{\text{neutral}} = \frac{1}{2} pK_w$$
      </div>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Temperature (&deg;C)</th>
              <th>Temperature (K)</th>
              <th>Kw (&times; 10⁻¹⁴)</th>
              <th>pK_w</th>
              <th>Neutral pH (½ pKw)</th>
              <th>[H⁺] at Neutrality (mol/L)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>0 &deg;C</td>
              <td>273.15 K</td>
              <td>0.114 &times; 10⁻¹⁴</td>
              <td>14.94</td>
              <td>7.47</td>
              <td>3.38 &times; 10⁻⁸ M</td>
            </tr>
            <tr>
              <td>10 &deg;C</td>
              <td>283.15 K</td>
              <td>0.292 &times; 10⁻¹⁴</td>
              <td>14.53</td>
              <td>7.27</td>
              <td>5.40 &times; 10⁻⁸ M</td>
            </tr>
            <tr>
              <td>20 &deg;C</td>
              <td>293.15 K</td>
              <td>0.681 &times; 10⁻¹⁴</td>
              <td>14.17</td>
              <td>7.08</td>
              <td>8.25 &times; 10⁻⁸ M</td>
            </tr>
            <tr>
              <td>25 &deg;C (Standard)</td>
              <td>298.15 K</td>
              <td>1.008 &times; 10⁻¹⁴</td>
              <td>14.00</td>
              <td>7.00</td>
              <td>1.00 &times; 10⁻⁷ M</td>
            </tr>
            <tr>
              <td>37 &deg;C (Human Body)</td>
              <td>310.15 K</td>
              <td>2.399 &times; 10⁻¹⁴</td>
              <td>13.62</td>
              <td>6.81</td>
              <td>1.55 &times; 10⁻⁷ M</td>
            </tr>
            <tr>
              <td>50 &deg;C</td>
              <td>323.15 K</td>
              <td>5.474 &times; 10⁻¹⁴</td>
              <td>13.26</td>
              <td>6.63</td>
              <td>2.34 &times; 10⁻⁷ M</td>
            </tr>
            <tr>
              <td>75 &deg;C</td>
              <td>348.15 K</td>
              <td>19.95 &times; 10⁻¹⁴</td>
              <td>12.70</td>
              <td>6.35</td>
              <td>4.47 &times; 10⁻⁷ M</td>
            </tr>
            <tr>
              <td>100 &deg;C (Boiling)</td>
              <td>373.15 K</td>
              <td>51.30 &times; 10⁻¹⁴</td>
              <td>12.29</td>
              <td>6.14</td>
              <td>7.16 &times; 10⁻⁷ M</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p>Consequently, pure boiling water at $100^\circ\text{C}$ possesses a $\text{pH of } 6.14$. Despite having a pH below 7, it is 100% chemically neutral because $[\text{H}_3\text{O}^+]$ exactly equals $[\text{OH}^-]$.</p>

      <h2>Mathematical Derivations for Strong vs. Weak Electrolytes</h2>

      <h3>1. Strong Monoprotic Acids (HCl, HNO₃, HClO₄)</h3>
      <p>Strong acids are assumed to undergo $100\%$ quantitative forward dissociation in aqueous solution:</p>
      <div class="formula-box">
        $$\text{HA} + \text{H}_2\text{O} \longrightarrow \text{H}_3\text{O}^+ + \text{A}^- \quad \implies \quad [\text{H}_3\text{O}^+] = C_{\text{acid}}$$
        $$\text{pH} = -\log_{10}(C_{\text{acid}})$$
      </div>
      <p>For diprotic sulfuric acid ($\text{H}_2\text{SO}_4$), the first proton dissociates completely ($K_{a1} \gg 1$), while the second proton dissociates with $K_{a2} = 1.02 \times 10^{-2}$. At concentrations $C &gt; 0.05\text{ M}$, $[\text{H}^+] \approx 2 \cdot C_{\text{acid}}$.</p>

      <h3>2. Strong Bases (NaOH, KOH, Ca(OH)₂)</h3>
      <p>Strong metal hydroxides ionize completely:</p>
      <div class="formula-box">
        $$\text{M(OH)}_z \longrightarrow \text{M}^{z+} + z\text{OH}^- \quad \implies \quad [\text{OH}^-] = z \cdot C_{\text{base}}$$
        $$\text{pOH} = -\log_{10}(z \cdot C_{\text{base}}), \quad \text{pH} = pK_w - \text{pOH}$$
      </div>

      <h3>3. Weak Acids: Exact Quadratic Derivation</h3>
      <p>Weak acids establish a reversible thermodynamic dissociation equilibrium:</p>
      <div class="formula-box">
        $$\text{HA} + \text{H}_2\text{O} \rightleftharpoons \text{H}_3\text{O}^+ + \text{A}^-, \quad K_a = \frac{[\text{H}_3\text{O}^+][\text{A}^-]}{[\text{HA}]}$$
      </div>
      <p>From stoichiometric mass balance, let $x = [\text{H}_3\text{O}^+] = [\text{A}^-]$. The equilibrium concentration of unionized acid is $[\text{HA}] = C - x$. Substituting yields:</p>
      <div class="formula-box">
        $$K_a = \frac{x^2}{C - x} \quad \implies \quad x^2 + K_a x - K_a C = 0$$
      </div>
      <p>Applying the classical quadratic formula ($x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$):</p>
      <div class="formula-box">
        $$[\text{H}_3\text{O}^+] = \frac{-K_a + \sqrt{K_a^2 + 4 K_a C}}{2}$$
      </div>
      <p>While elementary textbooks often approximate $C - x \approx C$ (giving $[\text{H}^+] \approx \sqrt{K_a C}$), this approximation introduces severe errors ($&gt;5\%$) whenever $K_a / C &gt; 0.05$ (dilute weak acids). This engineering calculator executes the exact quadratic equation across all concentration regimes.</p>

      <h2>Practical Worked Case Study: Exact pH Calculation of 0.020 M Acetic Acid</h2>
      <div class="worked-example-card">
        <h3>Biochemical Equilibrium Case Study: Vinegar Acidity Determination</h3>
        <p><strong>Scenario:</strong> A laboratory technician prepares a dilute solution of acetic acid ($\text{CH}_3\text{COOH}$) at analytical concentration $C = 0.0200\text{ mol/L (M)}$ at standard laboratory temperature of $25.0^\circ\text{C}$. The thermodynamic acid dissociation constant is $K_a = 1.75 \times 10^{-5}$ ($pK_a = 4.757$). Calculate: (1) exact hydronium concentration $[\text{H}_3\text{O}^+]$ via the quadratic formula, (2) solution $\text{pH}$ and $\text{pOH}$, (3) hydroxide ion concentration $[\text{OH}^-]$, and (4) the fractional degree of ionization ($\alpha$).</p>

        <p><strong>Step 1: Set Up the Quadratic Mass Action Equation:</strong></p>
        $$x^2 + (1.75 \times 10^{-5})x - (1.75 \times 10^{-5} \times 0.0200) = 0$$
        $$x^2 + (1.75 \times 10^{-5})x - (3.50 \times 10^{-7}) = 0$$

        <p><strong>Step 2: Solve the Quadratic Formula:</strong></p>
        $$x = \frac{-(1.75 \times 10^{-5}) + \sqrt{(1.75 \times 10^{-5})^2 - 4(1)(-3.50 \times 10^{-7})}}{2}$$
        $$\sqrt{3.0625 \times 10^{-10} + 1.40 \times 10^{-6}} = \sqrt{1.4003 \times 10^{-6}} = 1.1833 \times 10^{-3}$$
        $$x = \frac{-0.0000175 + 0.0011833}{2} = \frac{0.0011658}{2} = 5.829 \times 10^{-4}\text{ mol/L}$$
        $$[\text{H}_3\text{O}^+] = 5.829 \times 10^{-4}\text{ M}$$

        <p><strong>Step 3: Determine Solution pH and pOH:</strong></p>
        $$\text{pH} = -\log_{10}(5.829 \times 10^{-4}) = -(-3.234) = 3.234 \approx 3.23$$
        $$\text{pOH} = 14.00 - 3.234 = 10.766 \approx 10.77$$

        <p><strong>Step 4: Compute Hydroxide Concentration:</strong></p>
        $$[\text{OH}^-] = 10^{-10.766} = 1.714 \times 10^{-11}\text{ mol/L}$$

        <p><strong>Step 5: Degree of Acid Ionization (Ostwald's α):</strong></p>
        $$\alpha = \frac{[\text{H}_3\text{O}^+]}{C} \times 100\% = \frac{5.829 \times 10^{-4}\text{ M}}{0.0200\text{ M}} \times 100\% = 2.915\%$$
        <p>Only $2.91\%$ of acetic acid molecules ionize into hydronium and acetate ions; $97.09\%$ remain as intact neutral molecules.</p>
      </div>
    </article>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-grid">
        <div class="footer-col">
          <div class="footer-logo">
            <span class="logo-icon">&pi;</span>
            <span class="logo-text">Calc<strong>Hub</strong></span>
          </div>
          <p class="footer-about">High-precision chemical equilibrium, hydronium ion activity, and acid-base thermodynamics tools conforming to IUPAC and NIST standards.</p>
        </div>
        <div class="footer-col">
          <h4 class="footer-title">Engineering Disciplines</h4>
          <ul class="footer-links">
            <li><a href="chemical.html">Chemical &amp; Water Treatment</a></li>
            <li><a href="mechanical.html">Mechanical &amp; HVAC</a></li>
            <li><a href="engineering.html">Electrical &amp; Electronics</a></li>
            <li><a href="civil.html">Civil &amp; Construction</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4 class="footer-title">Standard References</h4>
          <ul class="footer-links">
            <li><a href="https://www.iupac.org" target="_blank" rel="noopener">IUPAC Measurement of pH Definition</a></li>
            <li><a href="https://webbook.nist.gov" target="_blank" rel="noopener">NIST Ionization Constants of Water</a></li>
            <li><a href="https://www.bipm.org" target="_blank" rel="noopener">BIPM International Metrology in Chemistry</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    const WEAK_ACIDS = {
      acetic: 4.76,
      formic: 3.75,
      benzoic: 4.20,
      hf: 3.17,
      custom: 4.76
    };

    const WEAK_BASES = {
      ammonia: 4.75,
      methylamine: 3.36,
      pyridine: 8.77,
      custom: 4.75
    };

    function updateElectrolyteType() {
      const t = document.getElementById("electrolyteTypeSelect").value;
      document.getElementById("directInputGroup").style.display = t === "direct_ph" ? "grid" : "none";
      document.getElementById("concInputGroup").style.display = t === "direct_ph" ? "none" : "grid";
      document.getElementById("weakAcidGroup").style.display = t === "weak_acid" ? "grid" : "none";
      document.getElementById("weakBaseGroup").style.display = t === "weak_base" ? "grid" : "none";
      calcPH();
    }

    function updateWeakAcidPreset() {
      const p = document.getElementById("weakAcidPreset").value;
      if (p !== "custom") {
        document.getElementById("acidPkaVal").value = WEAK_ACIDS[p];
        calcPH();
      }
    }

    function updateWeakBasePreset() {
      const p = document.getElementById("weakBasePreset").value;
      if (p !== "custom") {
        document.getElementById("basePkbVal").value = WEAK_BASES[p];
        calcPH();
      }
    }

    // Temperature dependent Kw calculation (Bandura and Lvov formula approximation)
    function getKw(tempC) {
      const T = tempC + 273.15;
      // Empirical pKw fit from 0 to 100 °C (NIST / Harned data)
      // pKw ≈ 4471.33/T - 6.0875 + 0.01706 * T
      const pkw = (4471.33 / T) - 6.0875 + (0.01706 * T);
      const kw = Math.pow(10, -pkw);
      return { pkw: pkw, kw: kw };
    }

    function calcPH() {
      const eType = document.getElementById("electrolyteTypeSelect").value;
      const tempC = parseFloat(document.getElementById("solnTempC").value) || 25.0;
      const kwObj = getKw(tempC);
      const pKw = kwObj.pkw;
      const Kw = kwObj.kw;
      const neutralPH = pKw / 2.0;

      let h_conc = 1e-7;
      let oh_conc = 1e-7;
      let alphaPct = 100.0;
      let kValStr = "∞ (Strong)";
      let chemDesc = "";

      if (eType === "direct_ph") {
        const dVal = parseFloat(document.getElementById("directVal").value) || 7.0;
        const dType = document.getElementById("directType").value;
        if (dType === "ph") {
          h_conc = Math.pow(10, -dVal);
          oh_conc = Kw / h_conc;
        } else if (dType === "poh") {
          oh_conc = Math.pow(10, -dVal);
          h_conc = Kw / oh_conc;
        } else if (dType === "h") {
          h_conc = dVal;
          oh_conc = Kw / h_conc;
        } else if (dType === "oh") {
          oh_conc = dVal;
          h_conc = Kw / oh_conc;
        }
        alphaPct = 100.0;
        kValStr = "Direct Entry";
        chemDesc = "Direct concentration / activity measurement input.";
      } else {
        let cVal = parseFloat(document.getElementById("soluteConcVal").value) || 0.05;
        const cUnit = document.getElementById("soluteConcUnit").value;
        let C = cVal;
        if (cUnit === "mm") C = cVal / 1000.0;
        else if (cUnit === "um") C = cVal / 1000000.0;

        if (eType === "strong_acid") {
          h_conc = C;
          oh_conc = Kw / h_conc;
          alphaPct = 100.0;
          kValStr = "∞ (Strong Acid)";
          chemDesc = "Strong monoprotic acid complete 100% dissociation into H⁺ and A⁻.";
        } else if (eType === "strong_acid_di") {
          h_conc = C * 2.0;
          oh_conc = Kw / h_conc;
          alphaPct = 100.0;
          kValStr = "∞ (Diprotic)";
          chemDesc = "Strong diprotic acid complete dissociation (2 protons per molecule).";
        } else if (eType === "strong_base") {
          oh_conc = C;
          h_conc = Kw / oh_conc;
          alphaPct = 100.0;
          kValStr = "∞ (Strong Base)";
          chemDesc = "Strong monobasic base complete dissociation into OH⁻.";
        } else if (eType === "strong_base_di") {
          oh_conc = C * 2.0;
          h_conc = Kw / oh_conc;
          alphaPct = 100.0;
          kValStr = "∞ (Dibasic)";
          chemDesc = "Strong dibasic base complete dissociation (2 OH⁻ per formula unit).";
        } else if (eType === "weak_acid") {
          const pka = parseFloat(document.getElementById("acidPkaVal").value) || 4.76;
          const Ka = Math.pow(10, -pka);
          // Quadratic: x^2 + Ka*x - Ka*C = 0
          const x = (-Ka + Math.sqrt(Ka * Ka + 4 * Ka * C)) / 2.0;
          h_conc = x;
          oh_conc = Kw / h_conc;
          alphaPct = (h_conc / C) * 100.0;
          kValStr = "Ka = " + Ka.toExponential(3) + " (pKa " + pka.toFixed(2) + ")";
          chemDesc = "Weak acid reversible equilibrium solved via exact quadratic formula.";
        } else if (eType === "weak_base") {
          const pkb = parseFloat(document.getElementById("basePkbVal").value) || 4.75;
          const Kb = Math.pow(10, -pkb);
          // Quadratic: x^2 + Kb*x - Kb*C = 0 => x = [OH-]
          const x = (-Kb + Math.sqrt(Kb * Kb + 4 * Kb * C)) / 2.0;
          oh_conc = x;
          h_conc = Kw / oh_conc;
          alphaPct = (oh_conc / C) * 100.0;
          kValStr = "Kb = " + Kb.toExponential(3) + " (pKb " + pkb.toFixed(2) + ")";
          chemDesc = "Weak base reversible equilibrium solved via exact quadratic formula.";
        }
      }

      const pH = -Math.log10(h_conc);
      const pOH = -Math.log10(oh_conc);

      // Categorization
      let cat = "";
      let indColor = "";
      if (pH < 2.0) {
        cat = "Strongly Acidic";
        indColor = "Universal Indicator: Red | Thymol Blue: Red | Phenolphthalein: Colorless";
      } else if (pH < 6.0) {
        cat = "Moderately Acidic";
        indColor = "Universal Indicator: Orange/Yellow | Methyl Red: Red | Phenolphthalein: Colorless";
      } else if (Math.abs(pH - neutralPH) <= 0.3) {
        cat = "Chemically Neutral (at " + tempC.toFixed(0) + "°C)";
        indColor = "Universal Indicator: Green | Bromothymol Blue: Green";
      } else if (pH < 11.5) {
        cat = "Moderately Alkaline";
        indColor = "Universal Indicator: Blue | Phenolphthalein: Light Pink";
      } else {
        cat = "Strongly Alkaline";
        indColor = "Universal Indicator: Purple/Violet | Phenolphthalein: Deep Magenta";
      }

      document.getElementById("resPHVal").textContent = pH.toFixed(2) + " pH";
      document.getElementById("resPHCategory").textContent = cat + " | pOH = " + pOH.toFixed(2);

      document.getElementById("resHydroniumVal").textContent = h_conc.toExponential(3) + " M";
      document.getElementById("resHydroniumSub").textContent = (h_conc >= 0.001 ? h_conc.toFixed(4) : h_conc.toExponential(2)) + " mol/L";

      document.getElementById("resHydroxideVal").textContent = oh_conc.toExponential(3) + " M";
      document.getElementById("resHydroxideSub").textContent = (oh_conc >= 0.001 ? oh_conc.toFixed(4) : oh_conc.toExponential(2)) + " mol/L";

      document.getElementById("resPOHVal").textContent = pOH.toFixed(2);
      document.getElementById("resIonizationAlpha").textContent = alphaPct > 99.9 ? "100.0% (Complete)" : alphaPct.toFixed(2) + "% Ionized";

      document.getElementById("resPKwVal").textContent = pKw.toFixed(2) + " (Kw = " + Kw.toExponential(2) + ")";
      document.getElementById("resPKwSub").textContent = "Neutral pH = " + neutralPH.toFixed(2) + " at " + tempC.toFixed(1) + "°C";

      document.getElementById("resEquilKVal").textContent = kValStr;
      document.getElementById("resChemStatus").textContent = chemDesc;
      document.getElementById("resIndicatorColor").textContent = indColor;
    }

    window.addEventListener("DOMContentLoaded", () => {
      calcPH();
    });
  </script>
</body>
</html>
"""

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p3 = os.path.join(base_dir, "molarity-calculator.html")
    p4 = os.path.join(base_dir, "ph-calculator.html")

    with open(p3, "w", encoding="utf-8") as f:
        f.write(TOOL_3_HTML)
    print(f"Generated {p3}")

    with open(p4, "w", encoding="utf-8") as f:
        f.write(TOOL_4_HTML)
    print(f"Generated {p4}")

if __name__ == "__main__":
    main()
