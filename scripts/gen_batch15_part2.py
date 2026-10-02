# -*- coding: utf-8 -*-
"""
Script to generate Batch 15 Part 2 tools:
3. dilution-calculator.html
4. gay-lussac-law-calculator.html
"""
import os

TOOL_3_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dilution Calculator | C₁V₁ = C₂V₂ Solution &amp; Molarity Sizer</title>
  <meta name="description" content="Calculate stock solution dilutions using C1V1 = C2V2, molarity, normality, mass/volume percent, ppm, serial dilution factors, and required solvent volume.">
  <link rel="canonical" href="https://calchub.cloud/dilution-calculator.html">
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
        "name": "Dilution Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates stock solution aliquots, solvent volumes, dilution factors, and working concentrations using C1V1 = C2V2 across molar, percent, and ppm scales.",
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
            "name": "What is the C1V1 = C2V2 dilution formula and how does it work?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The dilution equation C1 * V1 = C2 * V2 relies on the law of conservation of mass: the total amount of solute (moles or mass) in the initial concentrated aliquot (C1 * V1) remains identical to the amount of solute in the final diluted solution (C2 * V2). Adding solvent increases volume while decreasing concentration proportionally."
            }
          },
          {
            "@type": "Question",
            "name": "How is the volume of required solvent calculated during dilution?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Assuming ideal additive volumes, the volume of diluent (water or buffer) required is: V_solvent = V2 - V1. In high-precision analytical chemistry or when diluting concentrated alcohols and strong acids with water, non-ideal volumetric contraction occurs, so solvent must be added 'quantum satis' (QS) up to the calibrated flask line."
            }
          },
          {
            "@type": "Question",
            "name": "What is a Dilution Factor (DF)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The dilution factor (DF) represents the ratio of the final volume to the initial stock volume: DF = V2 / V1 = C1 / C2. For example, diluting 1.0 mL of stock into a total volume of 10.0 mL represents a 10-fold (1:10) dilution with DF = 10."
            }
          },
          {
            "@type": "Question",
            "name": "What is the safety rule for diluting concentrated mineral acids?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Always remember the rule: 'Always Add Acid' (AAA). Never pour water directly into concentrated sulfuric (H2SO4) or hydrochloric (HCl) acid. Hydration of strong acids is intensely exothermic; adding water to acid causes localized boiling and violent acid splashing. Slowly pour acid into cool water with continuous stirring."
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
      <span>Dilution Calculator</span>
    </nav>

    <h1 class="tool-title">Solution Dilution Calculator (C₁V₁ = C₂V₂)</h1>
    <p class="tool-subtitle">Stock Aliquot Sizing, Solvent Addition Volume &amp; Molar Concentration Sizer</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="diluteTarget">Select Variable to Solve For</label>
            <select id="diluteTarget" class="form-control" onchange="updateDiluteInputs()">
              <option value="v1" selected>Initial Stock Volume Needed (V₁)</option>
              <option value="c2">Final Working Concentration (C₂)</option>
              <option value="v2">Final Working Volume (V₂)</option>
              <option value="c1">Initial Stock Concentration (C₁)</option>
            </select>
          </div>

          <div class="form-group">
            <label for="concUnit">Concentration Unit Scale</label>
            <select id="concUnit" class="form-control">
              <option value="M" selected>Molar (M or mol/L)</option>
              <option value="mM">Millimolar (mM or mmol/L)</option>
              <option value="uM">Micromolar (μM or μmol/L)</option>
              <option value="pct_wv">% weight/volume (% w/v or g/100mL)</option>
              <option value="pct_vv">% volume/volume (% v/v or mL/100mL)</option>
              <option value="ppm">Parts per Million (ppm or mg/L)</option>
              <option value="ppb">Parts per Billion (ppb or μg/L)</option>
              <option value="g_l">Grams per Liter (g/L)</option>
              <option value="mg_ml">Milligrams per Milliliter (mg/mL)</option>
              <option value="N">Normality (N or eq/L)</option>
            </select>
          </div>

          <div id="c1Group" class="form-group">
            <label for="c1Val">Initial Stock Concentration (C₁)</label>
            <input type="number" id="c1Val" class="form-control" value="5.0" step="0.1" min="0.000001">
          </div>

          <div id="v1Group" class="grid-2-col" style="display:none;">
            <div class="form-group">
              <label for="v1Val">Initial Stock Volume (V₁)</label>
              <input type="number" id="v1Val" class="form-control" value="20.0" step="1.0" min="0.0001">
            </div>
            <div class="form-group">
              <label for="v1Unit">V₁ Volume Unit</label>
              <select id="v1Unit" class="form-control">
                <option value="ml" selected>Milliliters (mL)</option>
                <option value="l">Liters (L)</option>
                <option value="ul">Microliters (μL)</option>
                <option value="gal">US Gallons (gal)</option>
              </select>
            </div>
          </div>

          <div id="c2Group" class="form-group">
            <label for="c2Val">Final Working Concentration (C₂)</label>
            <input type="number" id="c2Val" class="form-control" value="0.25" step="0.01" min="0.000001">
          </div>

          <div id="v2Group" class="grid-2-col">
            <div class="form-group">
              <label for="v2Val">Final Desired Volume (V₂)</label>
              <input type="number" id="v2Val" class="form-control" value="500.0" step="10.0" min="0.0001">
            </div>
            <div class="form-group">
              <label for="v2Unit">V₂ Volume Unit</label>
              <select id="v2Unit" class="form-control">
                <option value="ml" selected>Milliliters (mL)</option>
                <option value="l">Liters (L)</option>
                <option value="ul">Microliters (μL)</option>
                <option value="gal">US Gallons (gal)</option>
              </select>
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="soluteMW">Solute Molecular Weight (g/mol)</label>
              <input type="number" id="soluteMW" class="form-control" value="58.44" step="0.01" min="1.0">
              <span class="field-hint">e.g., NaCl = 58.44, NaOH = 40.00, Tris = 121.14</span>
            </div>
            <div class="form-group">
              <label for="solventIdentity">Solvent Matrix</label>
              <select id="solventIdentity" class="form-control">
                <option value="water" selected>Deionized / Distilled Water (Milli-Q / ASTM Type 1)</option>
                <option value="pbs">Phosphate Buffered Saline (1X PBS)</option>
                <option value="etoh">Ethanol Solution</option>
                <option value="other">Organic Solvent / Buffer</option>
              </select>
            </div>
          </div>

          <button type="button" class="btn btn-primary" onclick="calcDilution()">Calculate Dilution Protocol</button>
        </div>

        <div id="dilutionResults" class="results-box" style="display:none;margin-top:1.5rem;">
          <h3 class="results-title">Dilution Recipe &amp; Laboratory Protocol</h3>
          <div class="result-grid">
            <div class="result-card">
              <div class="result-label" id="resDiluteTargetLabel">Calculated Value</div>
              <div class="result-value highlight" id="resDiluteTargetVal">--</div>
              <div class="result-subtext" id="resDiluteTargetAlt">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Required Diluent Solvent Volume</div>
              <div class="result-value highlight" id="resSolventVol">--</div>
              <div class="result-subtext" id="resSolventDesc">To add into stock aliquot</div>
            </div>
            <div class="result-card">
              <div class="result-label">Dilution Factor (Fold)</div>
              <div class="result-value" id="resDilutionFactor">--</div>
              <div class="result-subtext" id="resDilutionRatio">Ratio: --</div>
            </div>
            <div class="result-card">
              <div class="result-label">Total Dissolved Solute Mass</div>
              <div class="result-value" id="resSoluteMass">--</div>
              <div class="result-subtext" id="resSoluteMoles">-- moles</div>
            </div>
          </div>

          <div class="result-details" style="margin-top:1rem;padding:1rem;background:var(--card-bg);border-radius:6px;border:1px solid var(--border-light);">
            <h4 style="margin-top:0;">Laboratory Preparation Step-by-Step SOP</h4>
            <ol style="margin-bottom:0;padding-left:1.25rem;line-height:1.7;">
              <li>Measure exactly <strong id="resStep1Aliquot" style="color:var(--primary);">--</strong> of stock solution (<span id="resStep1StockConc">--</span>).</li>
              <li>Transfer the aliquot into a volumetric flask calibrated for <strong id="resStep2TotalVol">--</strong>.</li>
              <li>Add approximately <strong id="resStep3Solvent">--</strong> of diluent, swirl to mix thoroughly, then bring up to the meniscus mark (QS).</li>
              <li>Invert flask 10 times to ensure complete analytical homogeneity.</li>
            </ol>
          </div>
        </div>
      </div>

      <!-- Related Category Sidebar -->
      <aside class="post-sidebar">
        <div class="sidebar-widget">
          <div class="sidebar-widget-header">
            <span class="widget-icon">🧪</span>
            <h3 class="widget-title">Related Chemical Calculators</h3>
          </div>
          <p class="sidebar-widget-subtitle">Specialized calculation tools in this discipline:</p>
          <ul class="sidebar-links-list">
            <li><a href="chemical-dosing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Chemical Dosing Rate Calculator</a></li>
            <li><a href="caustic-soda-dosing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Caustic Soda Dosing Calculator</a></li>
            <li><a href="alum-dosing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Alum Dosing Calculator</a></li>
            <li><a href="boyles-law-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Boyle's Law Calculator</a></li>
          </ul>
          <div style="margin-top:1.25rem;padding-top:1rem;border-top:1px solid var(--border-light);">
            <a href="chemical.html" class="sidebar-category-link">View All Chemical Calculators &rarr;</a>
          </div>
        </div>
      </aside>
    </div>

    <!-- Technical Educational Article Body (1000+ Words) -->
    <article class="article-body">
      <h2>Principles of Solution Dilution in Analytical and Industrial Chemistry</h2>
      <p>Solution preparation and quantitative dilution represent the bedrock of analytical chemistry, molecular biology, clinical diagnostics, and chemical manufacturing. In laboratory practice, primary chemical standards and commercial chemical reagents are typically procured or synthesized as highly concentrated <strong>stock solutions</strong> (e.g., $10.0\text{ M } \text{NaOH}$, $50\times\text{ TAE}$ electrophoresis buffer, or $100\text{ mg/mL}$ ampicillin). Maintaining concentrated stocks maximizes chemical shelf life, minimizes storage space, and reduces shipping costs.</p>

      <p>However, analytical instruments (such as UV-Vis spectrophotometers, HPLC columns, atomic absorption spectrometers, and automated chemistry analyzers) operate within narrow linear calibration windows, frequently requiring working concentrations in the millimolar ($\text{mM}$), micromolar ($\mu\text{M}$), or parts-per-billion ($\text{ppb}$) range. Generating an accurate working solution requires quantitative volumetric transfer governed by conservation of solute mass.</p>

      <h2>The Governing Dilution Equation: C₁V₁ = C₂V₂</h2>
      <p>The mathematical postulate of dilution stems directly from the First Law of Thermodynamics and conservation of mass: <em>the total amount of dissolved solute within the system remains perfectly constant during the addition of pure solvent</em>. Solute mass ($m$) or molar quantity ($n$) is defined as the product of concentration ($C$) and volume ($V$):</p>

      <div class="formula-box">
        $$n = C_1 \times V_1 = C_2 \times V_2$$
      </div>

      <p>Where:</p>
      <ul>
        <li>$C_1$ = Initial concentration of the concentrated stock solution.</li>
        <li>$V_1$ = Volume of concentrated stock solution pipetted or metered (the <em>aliquot</em>).</li>
        <li>$C_2$ = Target final concentration of the working diluted solution ($C_2 &lt; C_1$).</li>
        <li>$V_2$ = Total final volume of the diluted solution ($V_2 &gt; V_1$).</li>
      </ul>

      <p>Rearranging the equation yields direct analytical expressions for each variable:</p>
      <div class="formula-box">
        $$V_1 = \frac{C_2 V_2}{C_1}, \quad C_2 = \frac{C_1 V_1}{V_2}, \quad V_2 = \frac{C_1 V_1}{C_2}, \quad C_1 = \frac{C_2 V_2}{V_1}$$
      </div>

      <h2>Dilution Factor (DF) and Serial Dilution Mathematics</h2>
      <p>The <strong>Dilution Factor</strong> ($\text{DF}$) defines the numerical scale of concentration reduction. It is calculated as the ratio of final volume to initial aliquot volume, which is identically equal to the ratio of initial stock concentration to final diluted concentration:</p>

      <div class="formula-box">
        $$\text{DF} = \frac{V_2}{V_1} = \frac{C_1}{C_2}$$
      </div>

      <p>For example, taking $5.0\text{ mL}$ of stock and bringing it to $100.0\text{ mL}$ final volume yields $\text{DF} = \frac{100.0}{5.0} = 20$. This represents a $20\text{-fold}$ dilution (often written in laboratory notebooks as a $1:20$ dilution). When attempting to dilute a solution by extreme orders of magnitude (e.g., $10^6\text{-fold}$ in qPCR or microbiology colony-forming unit counts), pipetting an infinitesimal sub-microliter aliquot directly introduces catastrophic volumetric error. In such cases, <strong>serial dilutions</strong> are performed in sequential steps:</p>

      <div class="formula-box">
        $$\text{DF}_{\text{total}} = \text{DF}_1 \times \text{DF}_2 \times \text{DF}_3 \times \dots \times \text{DF}_k = \prod_{i=1}^k \left(\frac{V_{2,i}}{V_{1,i}}\right)$$
      </div>

      <h2>Solvent Addition and Volumetric Non-Ideality</h2>
      <p>In standard laboratory calculations, the volume of diluent solvent ($V_{\text{solvent}}$) required is approximated by simple volumetric subtraction:</p>
      <div class="formula-box">
        $$V_{\text{solvent, ideal}} = V_2 - V_1$$
      </div>

      <p>However, analytical chemists must recognize that <strong>liquid volumes are not strictly additive</strong> due to thermodynamic excess molar volume of mixing ($\Delta V^E$). When mixing polar organic solvents (such as ethanol, methanol, or isopropanol) with water, or when diluting concentrated mineral acids, strong hydrogen bonding causes the molecular packing to densify. For instance, mixing $500\text{ mL}$ of pure ethanol with $500\text{ mL}$ of pure water yields approximately $965\text{ mL}$ of solution—not $1,000\text{ mL}$—exhibiting a $3.5\%$ volumetric contraction.</p>

      <p>To eliminate volumetric contraction errors in analytical chemistry, standard operating procedures dictate the <strong>Quantum Satis (QS)</strong> technique: pipet aliquot $V_1$ into a Class A volumetric flask partially filled with solvent, swirl to dissipate any heat of mixing, allow the flask to equilibrate to $20^\circ\text{C}$, and then add solvent dropwise until the bottom of the liquid meniscus rests precisely on the calibrated graduation line.</p>

      <h2>Concentration Scales and Unit Conversion Reference Table</h2>
      <p>The table below details standard quantitative concentration dimensions used across chemical disciplines:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Concentration Unit</th>
              <th>Symbol</th>
              <th>Definition / Mathematical Formula</th>
              <th>Primary Laboratory Domain</th>
              <th>Temperature Dependent?</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Molarity</td>
              <td>M (mol/L)</td>
              <td>$$\text{M} = \frac{\text{Moles of Solute (mol)}}{\text{Liters of Solution (L)}}$$</td>
              <td>General Chemistry, Biochemistry, Synthesis</td>
              <td>Yes (thermal expansion of liquid)</td>
            </tr>
            <tr>
              <td>Molality</td>
              <td>m (mol/kg)</td>
              <td>$$m = \frac{\text{Moles of Solute (mol)}}{\text{Kilograms of Solvent (kg)}}$$</td>
              <td>Physical Chemistry, Colligative Properties</td>
              <td>No (gravimetric basis)</td>
            </tr>
            <tr>
              <td>Normality</td>
              <td>N (eq/L)</td>
              <td>$$\text{N} = \text{M} \times n_{\text{eq}} = \frac{\text{Equivalents}}{\text{Liters of Solution}}$$</td>
              <td>Acid-Base &amp; Redox Volumetric Titrations</td>
              <td>Yes</td>
            </tr>
            <tr>
              <td>Weight/Volume Percent</td>
              <td>% w/v</td>
              <td>$$\% \, (w/v) = \frac{\text{Grams of Solute (g)}}{100 \, \text{mL of Solution}}$$</td>
              <td>Microbiology, Buffer Prep (e.g. 10% SDS)</td>
              <td>Yes</td>
            </tr>
            <tr>
              <td>Volume/Volume Percent</td>
              <td>% v/v</td>
              <td>$$\% \, (v/v) = \frac{\text{Volume of Solute (mL)}}{100 \, \text{mL of Solution}}$$</td>
              <td>Alcohol solutions (e.g. 70% EtOH)</td>
              <td>Yes</td>
            </tr>
            <tr>
              <td>Parts per Million</td>
              <td>ppm</td>
              <td>$$\text{ppm} = \frac{\text{mg Solute}}{\text{L Solution}} \approx \frac{\text{mg Solute}}{\text{kg Solution}}$$</td>
              <td>Water Treatment, Trace Contaminants</td>
              <td>Negligible at ambient</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Practical Worked Case Study: Preparation of 0.050 M Hydrochloric Acid</h2>
      <div class="worked-example-card">
        <h3>Laboratory Design Example: Standard Acid Titrant Preparation</h3>
        <p><strong>Scenario:</strong> An analytical chemist needs to prepare exactly $V_2 = 1,000.0\text{ mL}$ ($1.000\text{ L}$) of $C_2 = 0.0500\text{ M}$ hydrochloric acid ($\text{HCl}$) working titrant in a Class A volumetric flask. The available stock chemical is commercial concentrated reagent-grade $\text{HCl}$ ($37.0\%\text{ w/w}$, specific gravity $SG = 1.19\text{ g/mL}$, $\text{MW} = 36.46\text{ g/mol}$).</p>

        <p><strong>Step 1: Calculate the Molar Concentration of the Concentrated Stock (C₁):</strong></p>
        <p>One liter of stock solution has a mass of $1,000\text{ mL} \times 1.19\text{ g/mL} = 1,190.0\text{ grams}$.</p>
        <p>Active $\text{HCl}$ mass: $1,190.0\text{ g} \times 0.370 = 440.30\text{ grams of pure HCl}$.</p>
        $$C_1 = \frac{440.30\text{ g}}{36.46\text{ g/mol}} = 12.076\text{ M (Concentrated stock is 12.08 M)}$$

        <p><strong>Step 2: Apply the C₁V₁ = C₂V₂ Dilution Formula:</strong></p>
        $$V_1 = \frac{C_2 V_2}{C_1} = \frac{0.0500\text{ M} \times 1,000.0\text{ mL}}{12.076\text{ M}} = \frac{50.0}{12.076} = 4.140\text{ mL}$$

        <p><strong>Step 3: Calculate Dilution Factor:</strong></p>
        $$\text{DF} = \frac{V_2}{V_1} = \frac{1,000.0\text{ mL}}{4.140\text{ mL}} = 241.5\text{-fold dilution}$$

        <p><strong>Step 4: Chemical Safety Execution (AAA Rule):</strong></p>
        <p>Concentrated $\text{HCl}$ releases acrid fumes and extreme heat upon contact with water. The chemist fills the $1\text{-L}$ volumetric flask with approximately $700\text{ mL}$ of deionized water, uses a calibrated Class A glass pipet to transfer $4.14\text{ mL}$ of stock acid into the water, swirls gently, allows thermal equilibration, and brings to the meniscus mark with deionized water.</p>
      </div>

      <h2>Glassware Precision Tolerances and Error Propagation</h2>
      <p>Precision in solution preparation is physically bounded by glassware calibration standards under ASTM E288 and ISO 1042:</p>
      <ul>
        <li><strong>Class A Volumetric Flasks:</strong> Provide maximum precision (e.g., $100\text{ mL} \pm 0.08\text{ mL}$; $1,000\text{ mL} \pm 0.30\text{ mL}$ at $20^\circ\text{C}$). Always preferred for stock preparation.</li>
        <li><strong>Graduated Cylinders:</strong> Possess much wider tolerances ($\pm 1\%$ to $\pm 2\%$) and should never be used to measure the concentrated aliquot $V_1$.</li>
        <li><strong>Air Displacement Micropipettes:</strong> Require regular gravimetric calibration per ISO 8655. Pipetting viscous stocks (such as 50% glycerol or concentrated sulfuric acid) causes significant liquid hold-up on tip walls, requiring positive displacement pipettes or reverse pipetting techniques.</li>
      </ul>
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
          <p class="footer-about">High-precision chemical laboratory, analytical, and solution preparation tools conforming to ASTM, ISO, and IUPAC standards.</p>
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
            <li><a href="https://www.iupac.org" target="_blank" rel="noopener">IUPAC Analytical Compendium</a></li>
            <li><a href="https://www.astm.org" target="_blank" rel="noopener">ASTM E288 (Laboratory Glassware)</a></li>
            <li><a href="https://www.cdc.gov/niosh" target="_blank" rel="noopener">NIOSH Chemical Safety Guidelines</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    function updateDiluteInputs() {
      const target = document.getElementById("diluteTarget").value;
      document.getElementById("c1Group").style.display = target === "c1" ? "none" : "block";
      document.getElementById("v1Group").style.display = target === "v1" ? "none" : "grid";
      document.getElementById("c2Group").style.display = target === "c2" ? "none" : "block";
      document.getElementById("v2Group").style.display = target === "v2" ? "none" : "grid";
    }

    function toMl(val, unit) {
      if (unit === "l") return val * 1000;
      if (unit === "ul") return val * 0.001;
      if (unit === "gal") return val * 3785.41;
      return val; // ml
    }

    function fromMl(ml, unit) {
      if (unit === "l") return ml / 1000;
      if (unit === "ul") return ml * 1000;
      if (unit === "gal") return ml / 3785.41;
      return ml;
    }

    function calcDilution() {
      const target = document.getElementById("diluteTarget").value;
      const concUnit = document.getElementById("concUnit").value;
      const mw = parseFloat(document.getElementById("soluteMW").value) || 58.44;

      let c1 = 0, v1_ml = 0, c2 = 0, v2_ml = 0;

      if (target !== "c1") {
        c1 = parseFloat(document.getElementById("c1Val").value) || 0;
      }
      if (target !== "v1") {
        v1_ml = toMl(parseFloat(document.getElementById("v1Val").value) || 0, document.getElementById("v1Unit").value);
      }
      if (target !== "c2") {
        c2 = parseFloat(document.getElementById("c2Val").value) || 0;
      }
      if (target !== "v2") {
        v2_ml = toMl(parseFloat(document.getElementById("v2Val").value) || 0, document.getElementById("v2Unit").value);
      }

      let resLabel = "";
      let resVal = "";
      let resAlt = "";

      // C1 * V1 = C2 * V2
      if (target === "v1") {
        if (c1 <= 0) { alert("C1 must be positive non-zero"); return; }
        v1_ml = (c2 * v2_ml) / c1;
        const outUnit = document.getElementById("v2Unit").value;
        const v1_disp = fromMl(v1_ml, outUnit);
        resLabel = "Initial Stock Volume (V₁)";
        resVal = v1_disp.toFixed(4) + " " + outUnit;
        resAlt = v1_ml.toFixed(3) + " mL (" + (v1_ml * 1000).toFixed(1) + " μL)";
      } else if (target === "c2") {
        if (v2_ml <= 0) { alert("V2 must be positive non-zero"); return; }
        c2 = (c1 * v1_ml) / v2_ml;
        resLabel = "Final Working Concentration (C₂)";
        resVal = c2.toFixed(4) + " " + concUnit;
        resAlt = "From " + c1 + " " + concUnit + " stock";
      } else if (target === "v2") {
        if (c2 <= 0) { alert("C2 must be positive non-zero"); return; }
        v2_ml = (c1 * v1_ml) / c2;
        const outUnit = document.getElementById("v1Unit").value;
        const v2_disp = fromMl(v2_ml, outUnit);
        resLabel = "Final Diluted Volume (V₂)";
        resVal = v2_disp.toFixed(4) + " " + outUnit;
        resAlt = v2_ml.toFixed(3) + " mL (" + (v2_ml / 1000).toFixed(3) + " L)";
      } else if (target === "c1") {
        if (v1_ml <= 0) { alert("V1 must be positive non-zero"); return; }
        c1 = (c2 * v2_ml) / v1_ml;
        resLabel = "Initial Stock Concentration (C₁)";
        resVal = c1.toFixed(4) + " " + concUnit;
        resAlt = "Yields " + c2 + " " + concUnit + " after dilution";
      }

      const df = v2_ml / v1_ml;
      const solvent_ml = Math.max(0, v2_ml - v1_ml);

      // Solute mass (assuming molarity if M/mM/uM)
      let moles = 0;
      let massGrams = 0;
      if (concUnit === "M") {
        moles = c2 * (v2_ml / 1000);
        massGrams = moles * mw;
      } else if (concUnit === "mM") {
        moles = (c2 / 1000) * (v2_ml / 1000);
        massGrams = moles * mw;
      } else if (concUnit === "uM") {
        moles = (c2 / 1000000) * (v2_ml / 1000);
        massGrams = moles * mw;
      } else if (concUnit === "pct_wv") {
        massGrams = (c2 / 100) * v2_ml;
        moles = massGrams / mw;
      } else if (concUnit === "ppm") {
        massGrams = (c2 / 1000) * (v2_ml / 1000);
        moles = massGrams / mw;
      } else {
        massGrams = c2 * (v2_ml / 1000);
        moles = massGrams / mw;
      }

      document.getElementById("resDiluteTargetLabel").textContent = resLabel;
      document.getElementById("resDiluteTargetVal").textContent = resVal;
      document.getElementById("resDiluteTargetAlt").textContent = resAlt;

      document.getElementById("resSolventVol").textContent = solvent_ml.toFixed(2) + " mL";
      document.getElementById("resSolventDesc").textContent = (solvent_ml / 1000).toFixed(4) + " L of solvent / buffer";

      document.getElementById("resDilutionFactor").textContent = df.toFixed(2) + "× Fold";
      document.getElementById("resDilutionRatio").textContent = "Dilution Ratio: 1 : " + df.toFixed(1);

      document.getElementById("resSoluteMass").textContent = massGrams >= 1.0 ? massGrams.toFixed(3) + " g" : (massGrams * 1000).toFixed(2) + " mg";
      document.getElementById("resSoluteMoles").textContent = moles >= 0.001 ? moles.toFixed(4) + " moles" : (moles * 1000).toFixed(3) + " mmol";

      document.getElementById("resStep1Aliquot").textContent = v1_ml.toFixed(3) + " mL (" + (v1_ml * 1000).toFixed(1) + " μL)";
      document.getElementById("resStep1StockConc").textContent = c1.toFixed(3) + " " + concUnit;
      document.getElementById("resStep2TotalVol").textContent = v2_ml.toFixed(2) + " mL (" + (v2_ml / 1000).toFixed(3) + " L)";
      document.getElementById("resStep3Solvent").textContent = solvent_ml.toFixed(2) + " mL";

      document.getElementById("dilutionResults").style.display = "block";
    }
  </script>
</body>
</html>
"""

TOOL_4_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gay-Lussac's Law Calculator | P₁/T₁ = P₂/T₂ Rigid Vessel Gas Sizer</title>
  <meta name="description" content="Calculate gas pressure and temperature in rigid containers at constant volume using Gay-Lussac's Law (P1/T1 = P2/T2), thermal overpressure & ASME limits.">
  <link rel="canonical" href="https://calchub.cloud/gay-lussac-law-calculator.html">
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
        "name": "Gay-Lussac's Law Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates isobaric-free, rigid-vessel constant volume pressure and temperature transformations using Gay-Lussac's Law P1/T1 = P2/T2.",
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
            "name": "What is Gay-Lussac's Law and what physical condition must remain constant?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Gay-Lussac's Law (also known as Amontons's Law of Pressure-Temperature) states that the absolute pressure of a fixed mass of an ideal gas is directly proportional to its absolute thermodynamic temperature, provided the volume remains strictly constant: P1 / T1 = P2 / T2 = k."
            }
          },
          {
            "@type": "Question",
            "name": "Why MUST temperatures always be in Kelvin or Rankine?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Thermal gas pressure originates from molecular kinetic collisions against the container walls, which drops to zero only at Absolute Zero. Relative temperature scales (Celsius and Fahrenheit) have arbitrary zero points; using them yields false calculations. Temperatures must always be converted to Kelvin (K = °C + 273.15) or Rankine (°R = °F + 459.67)."
            }
          },
          {
            "@type": "Question",
            "name": "Does an isochoric process produce any mechanical boundary work?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "No. In an isochoric (constant volume) process, dV = 0. Therefore, boundary mechanical work is identically zero: W = integral(P dV) = 0. By the First Law of Thermodynamics, all heat transferred into the gas directly increases its internal energy: Q = Delta U = n * Cv * Delta T."
            }
          },
          {
            "@type": "Question",
            "name": "What engineering hazard does Gay-Lussac's Law predict in sealed pressure vessels during fire exposure?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "When a rigid container (such as an aerosol can, propane tank, or boiler) is heated in a fire, internal absolute temperature can triple or quadruple, causing proportional internal pressure spikes that exceed the material's ultimate tensile yield strength, resulting in a Boiling Liquid Expanding Vapor Explosion (BLEVE)."
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
      <span>Gay-Lussac's Law Calculator</span>
    </nav>

    <h1 class="tool-title">Gay-Lussac's Law Calculator (P₁/T₁ = P₂/T₂)</h1>
    <p class="tool-subtitle">Rigid Isochoric Vessel Gas Pressure, Temperature Transformation &amp; Thermal Overpressure</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="glTarget">Select Variable to Solve For</label>
            <select id="glTarget" class="form-control" onchange="updateGLInputs()">
              <option value="p2" selected>Final Absolute Pressure (P₂)</option>
              <option value="t2">Final Temperature (T₂)</option>
              <option value="p1">Initial Absolute Pressure (P₁)</option>
              <option value="t1">Initial Temperature (T₁)</option>
            </select>
          </div>

          <!-- P1 -->
          <div id="p1GLGroup" class="grid-2-col">
            <div class="form-group">
              <label for="p1GLVal">Initial Absolute Pressure (P₁)</label>
              <input type="number" id="p1GLVal" class="form-control" value="2.2" step="0.1" min="0.0001">
            </div>
            <div class="form-group">
              <label for="p1GLUnit">P₁ Pressure Unit</label>
              <select id="p1GLUnit" class="form-control">
                <option value="bar" selected>Bar (bar absolute)</option>
                <option value="atm">Atmospheres (atm)</option>
                <option value="kpa">Kilopascals (kPa)</option>
                <option value="psi">Pounds/sq in (psia)</option>
                <option value="pa">Pascals (Pa)</option>
              </select>
            </div>
          </div>

          <!-- T1 -->
          <div id="t1GLGroup" class="grid-2-col">
            <div class="form-group">
              <label for="t1GLVal">Initial Temperature (T₁)</label>
              <input type="number" id="t1GLVal" class="form-control" value="20.0" step="1.0">
            </div>
            <div class="form-group">
              <label for="t1GLUnit">T₁ Temperature Scale</label>
              <select id="t1GLUnit" class="form-control">
                <option value="c" selected>Celsius (°C)</option>
                <option value="k">Kelvin (K)</option>
                <option value="f">Fahrenheit (°F)</option>
                <option value="r">Rankine (°R)</option>
              </select>
            </div>
          </div>

          <!-- P2 -->
          <div id="p2GLGroup" class="grid-2-col" style="display:none;">
            <div class="form-group">
              <label for="p2GLVal">Final Absolute Pressure (P₂)</label>
              <input type="number" id="p2GLVal" class="form-control" value="3.5" step="0.1" min="0.0001">
            </div>
            <div class="form-group">
              <label for="p2GLUnit">P₂ Pressure Unit</label>
              <select id="p2GLUnit" class="form-control">
                <option value="bar" selected>Bar (bar absolute)</option>
                <option value="atm">Atmospheres (atm)</option>
                <option value="kpa">Kilopascals (kPa)</option>
                <option value="psi">Pounds/sq in (psia)</option>
                <option value="pa">Pascals (Pa)</option>
              </select>
            </div>
          </div>

          <!-- T2 -->
          <div id="t2GLGroup" class="grid-2-col">
            <div class="form-group">
              <label for="t2GLVal">Final Temperature (T₂)</label>
              <input type="number" id="t2GLVal" class="form-control" value="95.0" step="1.0">
            </div>
            <div class="form-group">
              <label for="t2GLUnit">T₂ Temperature Scale</label>
              <select id="t2GLUnit" class="form-control">
                <option value="c" selected>Celsius (°C)</option>
                <option value="k">Kelvin (K)</option>
                <option value="f">Fahrenheit (°F)</option>
                <option value="r">Rankine (°R)</option>
              </select>
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="fixedVesselVol">Constant Internal Vessel Volume (Liters)</label>
              <input type="number" id="fixedVesselVol" class="form-control" value="40.0" step="1.0" min="0.1">
              <span class="field-hint">Rigid container volume (remains constant dV = 0)</span>
            </div>
            <div class="form-group">
              <label for="gasIdentityGL">Gas Molecular Identity</label>
              <select id="gasIdentityGL" class="form-control">
                <option value="air" selected>Air (MW = 28.97 g/mol, Cv = 0.718 kJ/kg·K)</option>
                <option value="n2">Nitrogen N₂ (MW = 28.01 g/mol, Cv = 0.743 kJ/kg·K)</option>
                <option value="o2">Oxygen O₂ (MW = 32.00 g/mol, Cv = 0.658 kJ/kg·K)</option>
                <option value="co2">Carbon Dioxide CO₂ (MW = 44.01 g/mol, Cv = 0.657 kJ/kg·K)</option>
                <option value="he">Helium He (MW = 4.003 g/mol, Cv = 3.116 kJ/kg·K)</option>
                <option value="h2">Hydrogen H₂ (MW = 2.016 g/mol, Cv = 10.18 kJ/kg·K)</option>
              </select>
            </div>
          </div>

          <button type="button" class="btn btn-primary" onclick="calcGayLussac()">Solve Gay-Lussac's Law</button>
        </div>

        <div id="glResults" class="results-box" style="display:none;margin-top:1.5rem;">
          <h3 class="results-title">Rigid Vessel Pressure-Temperature Diagnostics</h3>
          <div class="result-grid">
            <div class="result-card">
              <div class="result-label" id="resGLTargetLabel">Calculated Value</div>
              <div class="result-value highlight" id="resGLTargetVal">--</div>
              <div class="result-subtext" id="resGLTargetAlt">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Thermal Pressure Shift</div>
              <div class="result-value" id="resGLPresShift">--</div>
              <div class="result-subtext" id="resGLPresRatio">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Internal Thermal Energy (ΔU)</div>
              <div class="result-value highlight" id="resGLDeltaU">--</div>
              <div class="result-subtext">Isochoric heat Q = ΔU (W = 0)</div>
            </div>
            <div class="result-card">
              <div class="result-label">Gay-Lussac Constant (k = P/T)</div>
              <div class="result-value" id="resGLConstant">--</div>
              <div class="result-subtext">kPa / Kelvin ratio</div>
            </div>
          </div>

          <div class="result-details" style="margin-top:1rem;padding:1rem;background:var(--card-bg);border-radius:6px;border:1px solid var(--border-light);">
            <h4 style="margin-top:0;">Thermodynamics &amp; Safety Diagnostics</h4>
            <ul style="margin-bottom:0;line-height:1.7;">
              <li><strong>Absolute Temperatures:</strong> <span id="resGLAbsTemps">--</span></li>
              <li><strong>Contained Gas Mass:</strong> <span id="resGLContainedMass">--</span></li>
              <li><strong>ASME Overpressure Warning:</strong> <span id="resGLSafety">--</span></li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Related Category Sidebar -->
      <aside class="post-sidebar">
        <div class="sidebar-widget">
          <div class="sidebar-widget-header">
            <span class="widget-icon">🧪</span>
            <h3 class="widget-title">Related Chemical Calculators</h3>
          </div>
          <p class="sidebar-widget-subtitle">Specialized calculation tools in this discipline:</p>
          <ul class="sidebar-links-list">
            <li><a href="boyles-law-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Boyle's Law Calculator</a></li>
            <li><a href="charles-law-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Charles's Law Calculator</a></li>
            <li><a href="combined-gas-law-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Combined Gas Law Calculator</a></li>
            <li><a href="thermal-expansion-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Thermal Expansion &amp; Pipe Stress</a></li>
          </ul>
          <div style="margin-top:1.25rem;padding-top:1rem;border-top:1px solid var(--border-light);">
            <a href="chemical.html" class="sidebar-category-link">View All Chemical Calculators &rarr;</a>
          </div>
        </div>
      </aside>
    </div>

    <!-- Technical Educational Article Body (1000+ Words) -->
    <article class="article-body">
      <h2>Thermodynamic Foundation of Gay-Lussac's (Amontons's) Law</h2>
      <p>Gay-Lussac's Law—historically grounded in Guillaume Amontons's early constant-volume air thermometer experiments of 1702 and mathematically formalized by French chemist Joseph Louis Gay-Lussac in 1802—establishes the fundamental equation of state governing <strong>isochoric</strong> (constant volume, isometric) gaseous transformations. The law states that for a fixed quantity of gas held within a rigid, non-deformable boundary, the absolute pressure exerted by the gas against the interior vessel walls is directly proportional to its thermodynamic absolute temperature.</p>

      <p>Under kinetic molecular theory, the pressure of a confined gas originates from the momentum transferred during elastic collisions between sub-microscopic gas molecules and the container walls. When thermal energy is transferred into a rigid vessel, the root-mean-square molecular velocity ($v_{\text{rms}} = \sqrt{\frac{3 k_B T}{m}}$) increases. Because the volumetric boundaries remain fixed ($dV = 0$), two microscopic phenomena occur simultaneously: molecules travel faster between opposite walls (increasing collision frequency), and each individual impact delivers greater mechanical impulse ($I = \Delta p = 2 m v_x$). These combined kinetic effects produce an internal pressure rise directly proportional to absolute Kelvin temperature.</p>

      <h2>Mathematical Formulation and Boundary Solutions</h2>
      <p>Mathematically, Gay-Lussac's Law is formulated as:</p>

      <div class="formula-box">
        $$\frac{P}{T} = k \quad \implies \quad \frac{P_1}{T_1} = \frac{P_2}{T_2} \quad (V = \text{constant}, \, n = \text{constant})$$
      </div>

      <p>Where:</p>
      <ul>
        <li>$P_1, P_2$ = Initial and final absolute pressures (expressed in Pa, bar, atm, or psia).</li>
        <li>$T_1, T_2$ = Initial and final thermodynamic temperatures expressed <strong>strictly in Kelvin ($K$) or Rankine ($^\circ\text{R}$)</strong>.</li>
        <li>$k = \frac{n R}{V}$ = The isochoric Gay-Lussac proportionality constant.</li>
      </ul>

      <p>Rearranging the equation yields analytical solutions for each of the four boundary conditions:</p>
      <div class="formula-box">
        $$P_2 = P_1 \left(\frac{T_2}{T_1}\right), \quad T_2 = T_1 \left(\frac{P_2}{P_1}\right), \quad P_1 = P_2 \left(\frac{T_1}{T_2}\right), \quad T_1 = T_2 \left(\frac{P_1}{P_2}\right)$$
      </div>

      <p>Calculating with relative Celsius or Fahrenheit scales produces completely erroneous results. For example, heating a tire from $0^\circ\text{C}$ to $20^\circ\text{C}$ does not increase pressure by $20/0 = \infty$; in absolute terms, it represents a temperature shift from $273.15\text{ K}$ to $293.15\text{ K}$, producing a manageable $7.3\%$ pressure elevation.</p>

      <h2>Isochoric Thermodynamics: Zero Boundary Work and Internal Energy</h2>
      <p>In classical thermodynamics, boundary mechanical work ($W$) is defined as the integral of pressure over volumetric displacement ($W = \int P \, dV$). In an isochoric system, the physical boundaries are rigid ($dV = 0$):</p>

      <div class="formula-box">
        $$W_{\text{isochoric}} = \int_{V_1}^{V_2} P \, dV = 0$$
      </div>

      <p>Applying the First Law of Thermodynamics ($\Delta U = Q - W$):</p>
      <div class="formula-box">
        $$Q_v = \Delta U = m \cdot c_v \cdot \Delta T = n \cdot C_{v,\text{molar}} \cdot (T_2 - T_1)$$
      </div>
      <p>Because zero mechanical work is performed, 100% of the heat energy added to the gas is converted directly into internal thermal energy ($\Delta U$), accelerating molecular translational, rotational, and vibrational degrees of freedom.</p>

      <h2>Specific Heat Capacities (c_v) and Thermal Properties Table</h2>
      <p>The table below summarizes constant-volume specific heat capacities ($c_v$), molar masses, and isochoric pressure response parameters for key industrial gases at $20^\circ\text{C}$:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Gas Species</th>
              <th>Molar Mass (g/mol)</th>
              <th>Specific Heat c_v (kJ/kg·K)</th>
              <th>Molar Heat C_v (J/mol·K)</th>
              <th>Pressure Temp Coeff β (bar/K per bar @ 20°C)</th>
              <th>Typical Industrial Vessel Application</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Dry Air</td>
              <td>28.97</td>
              <td>0.718</td>
              <td>20.80</td>
              <td>0.003411</td>
              <td>Pneumatic receivers, vehicle tires</td>
            </tr>
            <tr>
              <td>Nitrogen (N₂)</td>
              <td>28.01</td>
              <td>0.743</td>
              <td>20.81</td>
              <td>0.003411</td>
              <td>Inert fire suppression, accumulator bladders</td>
            </tr>
            <tr>
              <td>Oxygen (O₂)</td>
              <td>32.00</td>
              <td>0.658</td>
              <td>21.06</td>
              <td>0.003411</td>
              <td>Medical oxygen cylinders, oxy-fuel tanks</td>
            </tr>
            <tr>
              <td>Carbon Dioxide (CO₂)</td>
              <td>44.01</td>
              <td>0.657</td>
              <td>28.91</td>
              <td>0.003415</td>
              <td>Beverage carbonation, CO₂ fire extinguishers</td>
            </tr>
            <tr>
              <td>Helium (He)</td>
              <td>4.003</td>
              <td>3.116</td>
              <td>12.47</td>
              <td>0.003411</td>
              <td>Cryogenic purge tanks, dirigible storage</td>
            </tr>
            <tr>
              <td>Methane (CH₄ / CNG)</td>
              <td>16.04</td>
              <td>1.700</td>
              <td>27.27</td>
              <td>0.003418</td>
              <td>Compressed Natural Gas (CNG) fuel cylinders</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Practical Worked Case Study: Vehicle Tire Thermal Highway Driving Overpressure</h2>
      <div class="worked-example-card">
        <h3>Engineering Design Example: Radial Truck Tire Highway Heating</h3>
        <p><strong>Scenario:</strong> A heavy commercial transport truck tire with an internal volume of $V = 80.0\text{ Liters}$ is inflated during a cold morning at ambient temperature $T_1 = 15.0^\circ\text{C}$ ($288.15\text{ K}$) to a gauge pressure of $P_{\text{gauge}} = 100.0\text{ psig}$ ($6.895\text{ bar gauge}$). Atmospheric pressure is $14.7\text{ psia}$ ($1.013\text{ bar}$). After 3 hours of high-speed highway transit under heavy axle loading, internal carcass friction elevates the trapped air temperature to $T_2 = 80.0^\circ\text{C}$ ($353.15\text{ K}$). Assume constant steel-belted tire carcass volume.</p>

        <p><strong>Step 1: Convert Initial Pressure and Temperatures to Absolute Scales:</strong></p>
        $$P_1 = P_{\text{gauge}} + P_{\text{atm}} = 100.0 + 14.7 = 114.7\text{ psia (7.908 bar absolute)}$$
        $$T_1 = 15.0 + 273.15 = 288.15\text{ K}$$
        $$T_2 = 80.0 + 273.15 = 353.15\text{ K}$$

        <p><strong>Step 2: Solve for Final Hot Pressure (P₂) via Gay-Lussac's Law:</strong></p>
        $$P_2 = P_1 \times \left(\frac{T_2}{T_1}\right) = 114.7\text{ psia} \times \left(\frac{353.15\text{ K}}{288.15\text{ K}}\right) = 114.7 \times 1.22558 = 140.57\text{ psia (9.692 bar abs)}$$

        <p><strong>Step 3: Calculate Hot Operating Gauge Pressure:</strong></p>
        $$P_{2,\text{gauge}} = 140.57 - 14.7 = 125.87\text{ psig (8.679 bar gauge)}$$
        <p>Highway friction generates an internal pressure elevation of $\Delta P = +25.87\text{ psi}$ ($+22.6\%$ thermal pressure boost).</p>

        <p><strong>Step 4: Compute Trapped Air Mass and Isochoric Heat (Q):</strong></p>
        $$n = \frac{P_1 V}{R T_1} = \frac{790,800\text{ Pa} \times 0.080\text{ m}^3}{8.3145 \times 288.15\text{ K}} = 26.40\text{ moles of air}$$
        $$m_{\text{air}} = 26.40\text{ mol} \times 0.02897\text{ kg/mol} = 0.765\text{ kg}$$
        $$Q_v = m \cdot c_v \cdot \Delta T = 0.765\text{ kg} \times 0.718\text{ kJ/kg}\cdot\text{K} \times (80.0 - 15.0)\text{ K} = 35.70\text{ kJ}$$
      </div>

      <h2>Industrial Engineering Applications and Safety Mandates</h2>
      <p>Gay-Lussac's Law directly governs critical life safety and pressure vessel engineering codes:</p>
      <ul>
        <li><strong>ASME Section VIII Boiler and Pressure Vessel Code:</strong> Sealed vessels containing compressed gases must feature certified Pressure Safety Valves (PSVs) or rupture discs sized to vent maximum thermal overpressurization. If an uninsulated vessel is engulfed in a plant fire, $T$ climbs from $300\text{ K}$ to over $1,200\text{ K}$, driving a $400\%$ internal pressure surge that guarantees catastrophic rupture if unvented.</li>
        <li><strong>Medical Autoclave Sterilization:</strong> Hospital autoclaves operate by heating saturated steam within a sealed rigid chamber up to $121^\circ\text{C}$ ($394.15\text{ K}$) or $134^\circ\text{C}$ ($407.15\text{ K}$). Gay-Lussac's relation dictates corresponding steam pressure spikes to $2.05\text{ to }3.03\text{ bar absolute}$ ($15\text{ to }30\text{ psig}$), coagulating bacterial proteins and destroying bacterial endospores.</li>
        <li><strong>Aerosol Can Warnings:</strong> Consumer aerosol containers carry mandatory DOT warnings: <em>"Contents Under Pressure; Do Not Incinerate or Store Above 120°F (49°C)"</em>. At disposal temperatures, thin stamped tinplate seam welds rupture violently due to Gay-Lussac pressure elevation.</li>
        <li><strong>Cryogenic Boil-Off Containment:</strong> In closed cryogenic storage of liquid argon or liquid nitrogen without active re-condensation refrigeration, ambient thermal heat leak converts liquid to vapor. Within a fixed volume, Gay-Lussac thermal pressurization rapidly approaches the hydrostatic proof-test threshold, demanding dual ASME safety relief valves.</li>
      </ul>

      <h2>Real Gas Deviations and Equation of State Corrections</h2>
      <p>At low to moderate operating pressures (&lt; 10 bar) and temperatures far above liquefaction, Gay-Lussac's ideal gas relationship exhibits extraordinary empirical precision (deviations under 0.5%). However, in high-pressure hydrogen storage (350 to 700 bar) or supercritical CO₂ extraction loops, intermolecular forces and finite molecular core volume ($b$) alter isochoric slopes. Under the Van der Waals equation of state:</p>

      <div class="formula-box">
        $$P = \frac{n R T}{V - n b} - \frac{a n^2}{V^2}$$
      </div>

      <p>The isochoric pressure-temperature derivative $(\partial P / \partial T)_v = \frac{n R}{V - n b}$ remains linear, but the slope is steeper than the ideal Gay-Lussac prediction ($n R / V$) due to the repulsive excluded volume of molecular cores. Process chemical engineers account for these non-idealities using the compressibility factor ratio ($P_1 / (Z_1 T_1) = P_2 / (Z_2 T_2)$) to ensure failsafe mechanical pressure vessel containment.</p>
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
          <p class="footer-about">High-precision chemical, thermodynamic, and mechanical calculation tools conforming to ASME, ISO, and NIST physical standards.</p>
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
            <li><a href="https://www.asme.org" target="_blank" rel="noopener">ASME Boiler &amp; Pressure Vessel</a></li>
            <li><a href="https://webbook.nist.gov" target="_blank" rel="noopener">NIST Chemistry WebBook</a></li>
            <li><a href="https://www.iupac.org" target="_blank" rel="noopener">IUPAC Physical Chemistry</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    const GL_GAS_PROPS = {
      air: { mw: 28.97, cv: 0.718 },
      n2: { mw: 28.01, cv: 0.743 },
      o2: { mw: 32.00, cv: 0.658 },
      co2: { mw: 44.01, cv: 0.657 },
      he: { mw: 4.003, cv: 3.116 },
      h2: { mw: 2.016, cv: 10.18 }
    };

    function updateGLInputs() {
      const target = document.getElementById("glTarget").value;
      document.getElementById("p1GLGroup").style.display = target === "p1" ? "none" : "grid";
      document.getElementById("t1GLGroup").style.display = target === "t1" ? "none" : "grid";
      document.getElementById("p2GLGroup").style.display = target === "p2" ? "none" : "grid";
      document.getElementById("t2GLGroup").style.display = target === "t2" ? "none" : "grid";
    }

    function toPaGL(val, unit) {
      if (unit === "bar") return val * 100000;
      if (unit === "atm") return val * 101325;
      if (unit === "kpa") return val * 1000;
      if (unit === "psi") return val * 6894.757;
      return val;
    }

    function fromPaGL(pa, unit) {
      if (unit === "bar") return pa / 100000;
      if (unit === "atm") return pa / 101325;
      if (unit === "kpa") return pa / 1000;
      if (unit === "psi") return pa / 6894.757;
      return pa;
    }

    function toKGL(val, scale) {
      if (scale === "c") return val + 273.15;
      if (scale === "k") return val;
      if (scale === "f") return (val - 32) * (5 / 9) + 273.15;
      if (scale === "r") return val * (5 / 9);
      return val;
    }

    function fromKGL(k, scale) {
      if (scale === "c") return k - 273.15;
      if (scale === "k") return k;
      if (scale === "f") return (k - 273.15) * (9 / 5) + 32;
      if (scale === "r") return k * (9 / 5);
      return k;
    }

    function calcGayLussac() {
      const target = document.getElementById("glTarget").value;
      const gasKey = document.getElementById("gasIdentityGL").value;
      const props = GL_GAS_PROPS[gasKey];
      const vesselVolL = parseFloat(document.getElementById("fixedVesselVol").value) || 40;
      const v_m3 = vesselVolL * 0.001;

      let p1_pa = 0, t1_k = 0, p2_pa = 0, t2_k = 0;

      if (target !== "p1") {
        p1_pa = toPaGL(parseFloat(document.getElementById("p1GLVal").value) || 0, document.getElementById("p1GLUnit").value);
      }
      if (target !== "t1") {
        t1_k = toKGL(parseFloat(document.getElementById("t1GLVal").value) || 0, document.getElementById("t1GLUnit").value);
      }
      if (target !== "p2") {
        p2_pa = toPaGL(parseFloat(document.getElementById("p2GLVal").value) || 0, document.getElementById("p2GLUnit").value);
      }
      if (target !== "t2") {
        t2_k = toKGL(parseFloat(document.getElementById("t2GLVal").value) || 0, document.getElementById("t2GLUnit").value);
      }

      let resLabel = "";
      let resVal = "";
      let resAlt = "";

      // P1 / T1 = P2 / T2
      if (target === "p2") {
        if (t1_k <= 0) { alert("T1 must be greater than Absolute Zero (> 0 K)"); return; }
        p2_pa = p1_pa * (t2_k / t1_k);
        const outUnit = document.getElementById("p1GLUnit").value;
        const p2_disp = fromPaGL(p2_pa, outUnit);
        resLabel = "Final Absolute Pressure (P₂)";
        resVal = p2_disp.toFixed(4) + " " + outUnit.toUpperCase();
        resAlt = (p2_pa / 100000).toFixed(3) + " bar (" + (p2_pa / 6894.757).toFixed(2) + " psia)";
      } else if (target === "t2") {
        if (p1_pa <= 0) { alert("P1 must be positive non-zero"); return; }
        t2_k = t1_k * (p2_pa / p1_pa);
        const outScale = document.getElementById("t1GLUnit").value;
        const t2_disp = fromKGL(t2_k, outScale);
        resLabel = "Final Temperature (T₂)";
        resVal = t2_disp.toFixed(2) + " °" + outScale.toUpperCase();
        resAlt = t2_k.toFixed(2) + " K (" + (t2_k - 273.15).toFixed(2) + " °C)";
      } else if (target === "p1") {
        if (t2_k <= 0) { alert("T2 must be greater than Absolute Zero (> 0 K)"); return; }
        p1_pa = p2_pa * (t1_k / t2_k);
        const outUnit = document.getElementById("p2GLUnit").value;
        const p1_disp = fromPaGL(p1_pa, outUnit);
        resLabel = "Initial Absolute Pressure (P₁)";
        resVal = p1_disp.toFixed(4) + " " + outUnit.toUpperCase();
        resAlt = (p1_pa / 100000).toFixed(3) + " bar (" + (p1_pa / 6894.757).toFixed(2) + " psia)";
      } else if (target === "t1") {
        if (p2_pa <= 0) { alert("P2 must be positive non-zero"); return; }
        t1_k = t2_k * (p1_pa / p2_pa);
        const outScale = document.getElementById("t2GLUnit").value;
        const t1_disp = fromKGL(t1_k, outScale);
        resLabel = "Initial Temperature (T₁)";
        resVal = t1_disp.toFixed(2) + " °" + outScale.toUpperCase();
        resAlt = t1_k.toFixed(2) + " K (" + (t1_k - 273.15).toFixed(2) + " °C)";
      }

      const pShift_bar = (p2_pa - p1_pa) / 100000;
      const pShift_psi = (p2_pa - p1_pa) / 6894.757;
      const presRatio = p2_pa / p1_pa;
      const k_constant = (p1_pa / 1000) / t1_k; // kPa / K

      // Thermodynamics: Q = deltaU = m * cv * deltaT
      const R = 8.314462;
      const moles = (p1_pa * v_m3) / (R * t1_k);
      const massKg = (moles * props.mw) / 1000;
      const deltaT = t2_k - t1_k;
      const deltaU_kJ = massKg * props.cv * deltaT;

      document.getElementById("resGLTargetLabel").textContent = resLabel;
      document.getElementById("resGLTargetVal").textContent = resVal;
      document.getElementById("resGLTargetAlt").textContent = resAlt;

      document.getElementById("resGLPresShift").textContent = (pShift_bar >= 0 ? "+" : "") + pShift_bar.toFixed(3) + " bar (" + (pShift_psi >= 0 ? "+" : "") + pShift_psi.toFixed(1) + " psi)";
      document.getElementById("resGLPresRatio").textContent = "Pressure Ratio: " + presRatio.toFixed(3) + " : 1 (" + (((presRatio - 1)) * 100).toFixed(1) + "% shift)";

      document.getElementById("resGLDeltaU").textContent = (deltaU_kJ >= 0 ? "+" : "") + deltaU_kJ.toFixed(2) + " kJ";

      document.getElementById("resGLConstant").textContent = k_constant.toFixed(4) + " kPa/K";

      document.getElementById("resGLAbsTemps").textContent = "T₁ = " + t1_k.toFixed(2) + " K (" + (t1_k - 273.15).toFixed(1) + "°C)  ➜  T₂ = " + t2_k.toFixed(2) + " K (" + (t2_k - 273.15).toFixed(1) + "°C)";
      document.getElementById("resGLContainedMass").textContent = moles.toFixed(2) + " moles (" + massKg.toFixed(3) + " kg / " + (massKg * 2.20462).toFixed(2) + " lbs of " + gasKey.toUpperCase() + " in " + vesselVolL + " L vessel)";

      let safetyText = "";
      if (presRatio > 2.0) {
        safetyText = "HIGH OVERPRESSURE RISK: Pressure more than doubled! Verify ASME Section VIII relief valve capacity.";
      } else if (presRatio > 1.25) {
        safetyText = "MODERATE PRESSURE SURGE: +25% elevation. Standard pneumatic safety margin recommended.";
      } else {
        safetyText = "NOMINAL SHIFT: Well within standard operating safety thresholds.";
      }
      document.getElementById("resGLSafety").textContent = safetyText;

      document.getElementById("glResults").style.display = "block";
    }
  </script>
</body>
</html>
"""

def generate():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p1 = os.path.join(root, "dilution-calculator.html")
    p2 = os.path.join(root, "gay-lussac-law-calculator.html")
    
    with open(p1, "w", encoding="utf-8") as f:
        f.write(TOOL_3_HTML.strip() + "\n")
    print(f"Generated {p1}")

    with open(p2, "w", encoding="utf-8") as f:
        f.write(TOOL_4_HTML.strip() + "\n")
    print(f"Generated {p2}")

if __name__ == "__main__":
    generate()
