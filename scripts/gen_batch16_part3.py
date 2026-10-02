# -*- coding: utf-8 -*-
"""
Script to generate Batch 16 Part 3 tools:
5. ph-poh-calculator.html
6. phosphate-dosing-calculator.html
"""
import os

TOOL_5_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>pH to pOH Calculator | [H+] &amp; [OH-] Ion Concentration Sizer</title>
  <meta name="description" content="Convert between pH, pOH, [H+] hydronium, and [OH-] hydroxide concentrations. Features temperature-dependent Kw autoionization from 0°C to 100°C.">
  <link rel="canonical" href="https://calchub.cloud/ph-poh-calculator.html">
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
        "name": "pH to pOH Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates interconnected aqueous acid-base equilibrium parameters including pH, pOH, hydronium and hydroxide ion concentrations, and thermal Kw shifts.",
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
            "name": "What is the relationship between pH and pOH?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In any aqueous solution, the autoprotolysis equilibrium of water establishes that the product of hydronium and hydroxide concentrations equals the ion product constant: [H3O+][OH-] = Kw. Taking negative logarithms yields: pH + pOH = pKw. At standard room temperature (25°C), Kw = 1.0x10^-14, making pH + pOH = 14.00."
            }
          },
          {
            "@type": "Question",
            "name": "How does water temperature affect the sum of pH and pOH?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The autoionization of water is endothermic, meaning higher temperatures increase the dissociation constant Kw. At 0°C, pKw = 14.94 (neutral pH = 7.47), at 25°C, pKw = 14.00 (neutral pH = 7.00), and at 100°C, pKw = 12.29 (neutral pH = 6.14). Thus, the sum pH + pOH decreases as temperature rises."
            }
          },
          {
            "@type": "Question",
            "name": "How do you calculate [H+] and [OH-] from pH and pOH?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "By definition, [H3O+] = 10^(-pH) and [OH-] = 10^(-pOH). For example, at pH 3.50, [H3O+] = 10^(-3.50) = 3.162x10^-4 mol/L. At 25°C, the corresponding pOH is 14.00 - 3.50 = 10.50, giving [OH-] = 10^(-10.50) = 3.162x10^-11 mol/L."
            }
          },
          {
            "@type": "Question",
            "name": "Why is hot water with pH 6.5 not acidic?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Acidity is defined strictly as an excess of hydronium over hydroxide ([H+] > [OH-]), not by an arbitrary numerical threshold of 7.00. At 60°C, neutral pure water has a pH of 6.51. Therefore, water at 60°C with pH 6.50 contains virtually equal concentrations of [H+] and [OH-], making it chemically neutral."
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
      <span>pH to pOH Calculator</span>
    </nav>

    <h1 class="tool-title">pH to pOH &amp; Ion Concentration Calculator</h1>
    <p class="tool-subtitle">Mutual Equilibrium Interconversion: pH, pOH, [H₃O⁺], [OH⁻] &amp; Thermal Kw Shifts</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="fluidPresetSelect">Common Solution Reference Presets</label>
            <select id="fluidPresetSelect" class="form-control" onchange="updateFluidPreset()">
              <option value="battery">Automotive Battery Acid (pH ~0.80)</option>
              <option value="stomach">Human Gastric Acid (pH ~1.50)</option>
              <option value="lemon">Fresh Lemon Juice (pH ~2.40)</option>
              <option value="vinegar">Household Vinegar 5% (pH ~2.80)</option>
              <option value="coffee">Black Drip Coffee (pH ~5.00)</option>
              <option value="milk">Fresh Whole Milk (pH ~6.60)</option>
              <option value="pure_water" selected>Pure Deionized Water (pH 7.00 at 25°C)</option>
              <option value="blood">Human Blood Plasma (pH ~7.40)</option>
              <option value="seawater">Open Ocean Seawater (pH ~8.15)</option>
              <option value="baking_soda">Baking Soda Solution (pH ~8.50)</option>
              <option value="ammonia">Household Ammonia Cleaner (pH ~11.50)</option>
              <option value="bleach">Liquid Chlorine Bleach (pH ~12.50)</option>
              <option value="drain">1.0 M Lye / Drain Cleaner (pH ~14.00)</option>
              <option value="custom">Custom Numerical Input</option>
            </select>
          </div>

          <div class="form-group">
            <label for="activeInputType">Parameter to Specify</label>
            <select id="activeInputType" class="form-control" onchange="updateActiveInputUI()">
              <option value="ph" selected>Solution pH [-log₁₀[H⁺]]</option>
              <option value="poh">Solution pOH [-log₁₀[OH⁻]]</option>
              <option value="h_conc">Hydronium Ion [H₃O⁺] Concentration (M)</option>
              <option value="oh_conc">Hydroxide Ion [OH⁻] Concentration (M)</option>
            </select>
          </div>

          <!-- Parameter Value Input -->
          <div class="form-group">
            <label id="activeInputLabel" for="activeInputVal">Solution pH Value</label>
            <input type="number" id="activeInputVal" class="form-control" value="7.00" step="0.05">
            <span id="activeInputHint" class="field-hint">Standard aqueous range: -1.0 to 15.0</span>
          </div>

          <!-- Temperature Input -->
          <div class="grid-2-col">
            <div class="form-group">
              <label for="tempCelsiusVal">Solution Temperature (&deg;C)</label>
              <input type="number" id="tempCelsiusVal" class="form-control" value="25.0" step="1.0" min="0.0" max="100.0">
            </div>
            <div class="form-group">
              <label for="tempRefPreset">Thermal Standard</label>
              <select id="tempRefPreset" class="form-control" onchange="updateTempPreset()">
                <option value="25" selected>25°C (Standard Laboratory Standard)</option>
                <option value="37">37°C (Human Physiological Body Temp)</option>
                <option value="20">20°C (ISO Calibrated Volumetric)</option>
                <option value="4">4°C (Maximum Water Density)</option>
                <option value="60">60°C (Hot Water Distribution)</option>
                <option value="100">100°C (Boiling Point at 1 atm)</option>
              </select>
            </div>
          </div>

          <button type="button" class="btn btn-primary" onclick="calcPHtoPOH()" style="width: 100%; margin-top: 15px;">Interconvert Equilibrium Parameters</button>
        </div>
      </div>

      <!-- Output Results Panel -->
      <div class="results-card">
        <div class="result-box primary-result">
          <div class="result-label">Solution Acidity / Basicity State</div>
          <div id="resSummaryTitle" class="result-value">pH 7.00 &bull; Neutral</div>
          <div id="resSummarySub" class="result-subtext">pOH = 7.00 | [H⁺] = 1.00 &times; 10⁻⁷ M | [OH⁻] = 1.00 &times; 10⁻⁷ M</div>
        </div>

        <div class="result-grid">
          <div class="result-item">
            <span class="result-label">Calculated pH</span>
            <span id="resPH" class="result-value highlight">7.00</span>
            <span id="resPHSub" class="result-subtext">-log₁₀[H⁺]</span>
          </div>
          <div class="result-item">
            <span class="result-label">Calculated pOH</span>
            <span id="resPOH" class="result-value">7.00</span>
            <span id="resPOHSub" class="result-subtext">-log₁₀[OH⁻]</span>
          </div>
          <div class="result-item">
            <span class="result-label">Hydronium [H₃O⁺]</span>
            <span id="resHConc" class="result-value">1.00 &times; 10⁻⁷ M</span>
            <span id="resHConcSub" class="result-subtext">100.0 nmol/L</span>
          </div>
          <div class="result-item">
            <span class="result-label">Hydroxide [OH⁻]</span>
            <span id="resOHConc" class="result-value">1.00 &times; 10⁻⁷ M</span>
            <span id="resOHConcSub" class="result-subtext">100.0 nmol/L</span>
          </div>
          <div class="result-item">
            <span class="result-label">Water Ion Product pK_w</span>
            <span id="resPKw" class="result-value">14.00</span>
            <span id="resPKwSub" class="result-subtext">Kw = 1.01 &times; 10⁻¹⁴</span>
          </div>
          <div class="result-item">
            <span class="result-label">[H⁺] / [OH⁻] Ion Ratio</span>
            <span id="resRatio" class="result-value">1.00 : 1</span>
            <span id="resRatioSub" class="result-subtext">Exact parity (Neutral)</span>
          </div>
        </div>

        <div class="result-details" style="margin-top: 15px;">
          <p><strong>Neutral Point at Operating Temperature:</strong> <span id="resNeutralPoint">pH 7.00 (at 25.0°C)</span></p>
          <p><strong>Universal Indicator Spectrum:</strong> <span id="resIndicatorColor">Pure Green (Neutral pH 7)</span></p>
        </div>
      </div>
    </div>

    <!-- 1000+ Words Engineering Body -->
    <article class="article-body">
      <h2>Thermodynamics of Aqueous Proton-Hydroxide Duality</h2>
      <p>In all aqueous systems—from industrial high-pressure steam generators and biological cell cytoplasm to wastewater neutralization basins—liquid water molecules continuously engage in microscopic proton transfer collisions. This fundamental chemical behavior, termed <strong>water autoprotolysis</strong> or self-ionization, creates an unbroken mathematical duality between the hydronium ion ($\text{H}_3\text{O}^+$, commonly abbreviated as $\text{H}^+$) and the hydroxide ion ($\text{OH}^-$):</p>

      <div class="formula-box">
        $$2\text{H}_2\text{O (l)} \rightleftharpoons \text{H}_3\text{O}^+\text{ (aq)} + \text{OH}^-\text{ (aq)}$$
      </div>

      <p>Applying the thermodynamic law of mass action to this reversible equilibrium yields the <strong>autoprotolysis constant</strong> or <strong>ion product of water</strong> ($K_w$):</p>

      <div class="formula-box">
        $$K_w = a_{\text{H}_3\text{O}^+} \cdot a_{\text{OH}^-} \approx [\text{H}_3\text{O}^+][\text{OH}^-]$$
      </div>

      <p>Because the concentration of solvent water molecules ($55.5\text{ mol/L}$) is enormous and remains essentially constant in dilute solutions, its chemical activity is assigned unity ($a_{\text{H}_2\text{O}} \approx 1.0$), making $K_w$ an exclusive function of temperature and pressure.</p>

      <h2>Mathematical Derivations Connecting pH and pOH</h2>
      <p>By international chemical metrology convention, the lowercase prefix "$p$" represents the negative decimal logarithm operator ($pX = -\log_{10}X$). Applying this transformation to both sides of the ion product equation produces the universal bridge linking the acidic and basic scales:</p>

      <div class="formula-box">
        $$-\log_{10}(K_w) = -\log_{10}\left( [\text{H}_3\text{O}^+] \cdot [\text{OH}^-] \right)$$
        $$-\log_{10}(K_w) = -\log_{10}[\text{H}_3\text{O}^+] + \left( -\log_{10}[\text{OH}^-] \right)$$
      </div>

      <p>Substituting the defined terms yields the universal equation of state for aqueous acid-base balance:</p>

      <div class="formula-box">
        $$pK_w = \text{pH} + \text{pOH}$$
      </div>

      <p>Under standard thermodynamic laboratory reference conditions ($25.0^\circ\text{C} / 298.15\text{ K}$, $1.0\text{ atm}$), $K_w = 1.008 \times 10^{-14}$, which gives $pK_w = 14.00$. Hence, the classical relationship:</p>

      <div class="formula-box">
        $$\text{pH} + \text{pOH} = 14.00 \quad \iff \quad \text{pOH} = 14.00 - \text{pH}$$
      </div>

      <h2>Analytical Inversion Formulas for Ion Concentrations</h2>
      <p>To convert from logarithmic scales back to absolute molar concentrations (in $\text{mol/L}$ or $\text{M}$), we employ the base-10 exponential inverse:</p>
      <ul>
        <li><strong>From pH to Hydronium Concentration:</strong>
        $$[\text{H}_3\text{O}^+] = 10^{-\text{pH}}$$</li>
        <li><strong>From pOH to Hydroxide Concentration:</strong>
        $$[\text{OH}^-] = 10^{-\text{pOH}}$$</li>
        <li><strong>From Hydroxide directly to Hydronium via Kw:</strong>
        $$[\text{H}_3\text{O}^+] = \frac{K_w}{[\text{OH}^-]}$$</li>
        <li><strong>From Hydronium directly to Hydroxide via Kw:</strong>
        $$[\text{OH}^-] = \frac{K_w}{[\text{H}_3\text{O}^+]}$$</li>
      </ul>

      <h2>Temperature Dependency of Kw and Neutrality Shifts</h2>
      <p>A widespread misconception across engineering teams is that "pH 7.00 always represents neutrality." In reality, chemical neutrality is defined strictly by the thermodynamic equality of hydronium and hydroxide ions:</p>

      <div class="formula-box">
        $$\text{Chemical Neutrality Condition: } [\text{H}_3\text{O}^+] = [\text{OH}^-] = \sqrt{K_w}$$
      </div>

      <p>Because the autoprotolysis of liquid water is an endothermic bond-breaking reaction ($\Delta H^\circ = +55.84\text{ kJ/mol}$), increasing temperature forces the equilibrium to shift forward according to Le Chatelier's principle and the Van 't Hoff equation:</p>

      <div class="formula-box">
        $$\frac{d(\ln K_w)}{dT} = \frac{\Delta H^\circ}{R T^2}$$
      </div>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Temperature (&deg;C)</th>
              <th>Temperature (K)</th>
              <th>Kw Value</th>
              <th>pK_w</th>
              <th>Neutral pH (½ pKw)</th>
              <th>[H⁺] = [OH⁻] at Neutrality</th>
              <th>Classification of pH 7.00 at this Temp</th>
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
              <td>Moderately Acidic (pH &lt; 7.47)</td>
            </tr>
            <tr>
              <td>10 &deg;C</td>
              <td>283.15 K</td>
              <td>0.292 &times; 10⁻¹⁴</td>
              <td>14.53</td>
              <td>7.27</td>
              <td>5.40 &times; 10⁻⁸ M</td>
              <td>Slightly Acidic (pH &lt; 7.27)</td>
            </tr>
            <tr>
              <td>20 &deg;C</td>
              <td>293.15 K</td>
              <td>0.681 &times; 10⁻¹⁴</td>
              <td>14.17</td>
              <td>7.08</td>
              <td>8.25 &times; 10⁻⁸ M</td>
              <td>Slightly Acidic (pH &lt; 7.08)</td>
            </tr>
            <tr>
              <td>25 &deg;C</td>
              <td>298.15 K</td>
              <td>1.008 &times; 10⁻¹⁴</td>
              <td>14.00</td>
              <td>7.00</td>
              <td>1.00 &times; 10⁻⁷ M</td>
              <td>Exactly Chemically Neutral</td>
            </tr>
            <tr>
              <td>37 &deg;C (Body)</td>
              <td>310.15 K</td>
              <td>2.399 &times; 10⁻¹⁴</td>
              <td>13.62</td>
              <td>6.81</td>
              <td>1.55 &times; 10⁻⁷ M</td>
              <td>Slightly Alkaline (pH &gt; 6.81)</td>
            </tr>
            <tr>
              <td>50 &deg;C</td>
              <td>323.15 K</td>
              <td>5.474 &times; 10⁻¹⁴</td>
              <td>13.26</td>
              <td>6.63</td>
              <td>2.34 &times; 10⁻⁷ M</td>
              <td>Moderately Alkaline (pH &gt; 6.63)</td>
            </tr>
            <tr>
              <td>75 &deg;C</td>
              <td>348.15 K</td>
              <td>19.95 &times; 10⁻¹⁴</td>
              <td>12.70</td>
              <td>6.35</td>
              <td>4.47 &times; 10⁻⁷ M</td>
              <td>Strongly Alkaline (pH &gt; 6.35)</td>
            </tr>
            <tr>
              <td>100 &deg;C</td>
              <td>373.15 K</td>
              <td>51.30 &times; 10⁻¹⁴</td>
              <td>12.29</td>
              <td>6.14</td>
              <td>7.16 &times; 10⁻⁷ M</td>
              <td>Highly Alkaline (pH &gt; 6.14)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Practical Worked Case Study: High-Temperature Boiler Condensate Chemistry</h2>
      <div class="worked-example-card">
        <h3>Power Plant Engineering Case Study: Condensate Return Quality Control</h3>
        <p><strong>Scenario:</strong> A power station's high-temperature condensate return line operates at $T = 75.0^\circ\text{C}$ ($348.15\text{ K}$). Online glass electrode pH instrumentation with automatic temperature compensation (ATC) measures the in-situ stream pH at $\text{pH} = 6.65$. An operator expresses alarm that the water appears "acidic" and will cause carbonic acid grooving of carbon steel pipe walls. Using the thermodynamic properties of water at $75^\circ\text{C}$ ($K_w = 1.995 \times 10^{-13}$, $pK_w = 12.70$), determine: (1) the neutral pH at $75^\circ\text{C}$, (2) the stream pOH, (3) hydronium and hydroxide concentrations, (4) whether the water is acidic or alkaline, and (5) verify compliance with EPRI boiler standards.</p>

        <p><strong>Step 1: Compute True Neutrality at 75°C:</strong></p>
        $$\text{pH}_{\text{neutral}} = \frac{pK_w}{2} = \frac{12.70}{2} = 6.35$$
        <p>At $75^\circ\text{C}$, pure neutral water exhibits a pH of $6.35$. Because the measured stream pH ($6.65$) is greater than the neutral threshold ($6.65 &gt; 6.35$), the condensate is unambiguously <strong>alkaline</strong>, not acidic!</p>

        <p><strong>Step 2: Calculate Stream pOH:</strong></p>
        $$\text{pOH} = pK_w - \text{pH} = 12.70 - 6.65 = 6.05$$

        <p><strong>Step 3: Determine Specific Ion Concentrations:</strong></p>
        $$[\text{H}_3\text{O}^+] = 10^{-\text{pH}} = 10^{-6.65} = 2.239 \times 10^{-7}\text{ mol/L}$$
        $$[\text{OH}^-] = 10^{-\text{pOH}} = 10^{-6.05} = 8.913 \times 10^{-7}\text{ mol/L}$$

        <p><strong>Step 4: Hydroxide-to-Hydronium Ratio:</strong></p>
        $$\text{Ratio} = \frac{[\text{OH}^-]}{[\text{H}_3\text{O}^+]} = \frac{8.913 \times 10^{-7}}{2.239 \times 10^{-7}} = 3.98 : 1$$
        <p>Hydroxide ions outnumber hydronium ions by nearly $4:1$.</p>

        <p><strong>Step 5: Operational Conclusion:</strong></p>
        <p>When cooled to $25.0^\circ\text{C}$ in a sample cooler, the water will display a standard laboratory bench pH of approximately $9.35$ (due to volatile neutralizing amines such as cyclohexylamine), perfectly satisfying the EPRI guideline of $9.2\text{ to } 9.6$ for pre-boiler piping passivation.</p>
      </div>

      <h2>Ionic Strength Effects and Non-Ideal Deviations</h2>
      <p>In high-salinity brines, sea water ($I \approx 0.7\text{ M}$), and concentrated battery electrolytes, Debye-Hückel electrostatic screening causes single-ion activity coefficients to deviate substantially from unity ($\gamma_{\text{H}^+} \neq 1.0$). Precision electrometric glass electrodes respond directly to chemical activity rather than analytical molarity:</p>

      <div class="formula-box">
        $$\text{pH}_{\text{measured}} = -\log_{10}(\gamma_{\text{H}^+} \cdot [\text{H}^+])$$
      </div>
      <p>Consequently, in concentrated acids (e.g., $5\text{ M HCl}$), the apparent pH measured by a calibrated glass electrode is significantly lower than theoretical concentration calculations predict because crowding increases the effective activity coefficient of the proton ($\gamma_{\text{H}^+} &gt; 1.0$).</p>
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
          <p class="footer-about">High-precision chemical thermodynamics, aqueous acid-base equilibrium, and autoprotolysis tools conforming to IUPAC, NIST, and EPRI standards.</p>
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
            <li><a href="https://webbook.nist.gov" target="_blank" rel="noopener">NIST Ionization Constants of Water</a></li>
            <li><a href="https://www.iupac.org" target="_blank" rel="noopener">IUPAC Physical Chemistry Division</a></li>
            <li><a href="https://www.epri.com" target="_blank" rel="noopener">EPRI Boiler Water Chemistry Guidelines</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    const FLUID_PRESETS = {
      battery: 0.80,
      stomach: 1.50,
      lemon: 2.40,
      vinegar: 2.80,
      coffee: 5.00,
      milk: 6.60,
      pure_water: 7.00,
      blood: 7.40,
      seawater: 8.15,
      baking_soda: 8.50,
      ammonia: 11.50,
      bleach: 12.50,
      drain: 14.00,
      custom: 7.00
    };

    function updateFluidPreset() {
      const p = document.getElementById("fluidPresetSelect").value;
      if (p !== "custom") {
        document.getElementById("activeInputType").value = "ph";
        document.getElementById("activeInputVal").value = FLUID_PRESETS[p];
        updateActiveInputUI();
        calcPHtoPOH();
      }
    }

    function updateTempPreset() {
      const t = document.getElementById("tempRefPreset").value;
      document.getElementById("tempCelsiusVal").value = t;
      calcPHtoPOH();
    }

    function updateActiveInputUI() {
      const type = document.getElementById("activeInputType").value;
      const label = document.getElementById("activeInputLabel");
      const hint = document.getElementById("activeInputHint");
      const inp = document.getElementById("activeInputVal");

      if (type === "ph") {
        label.textContent = "Solution pH Value";
        hint.textContent = "Standard aqueous range: -1.0 to 15.0";
        inp.step = "0.05";
      } else if (type === "poh") {
        label.textContent = "Solution pOH Value";
        hint.textContent = "Standard aqueous range: -1.0 to 15.0";
        inp.step = "0.05";
      } else if (type === "h_conc") {
        label.textContent = "Hydronium [H₃O⁺] Concentration (mol/L)";
        hint.textContent = "e.g., 0.001 M or 1e-7 M";
        inp.step = "0.000001";
      } else if (type === "oh_conc") {
        label.textContent = "Hydroxide [OH⁻] Concentration (mol/L)";
        hint.textContent = "e.g., 0.001 M or 1e-7 M";
        inp.step = "0.000001";
      }
      calcPHtoPOH();
    }

    // Precise temperature fit for pKw from 0 to 100 °C (Harned & Owen / NIST data)
    function calcPKw(tempC) {
      const T = tempC + 273.15;
      const pkw = (4471.33 / T) - 6.0875 + (0.01706 * T);
      const kw = Math.pow(10, -pkw);
      return { pkw: pkw, kw: kw };
    }

    function calcPHtoPOH() {
      const inputType = document.getElementById("activeInputType").value;
      const inVal = parseFloat(document.getElementById("activeInputVal").value) || 7.0;
      const tempC = parseFloat(document.getElementById("tempCelsiusVal").value) || 25.0;

      const kwData = calcPKw(tempC);
      const pKw = kwData.pkw;
      const Kw = kwData.kw;
      const neutralPH = pKw / 2.0;

      let pH = 7.0;
      let pOH = 7.0;
      let h_conc = 1e-7;
      let oh_conc = 1e-7;

      if (inputType === "ph") {
        pH = inVal;
        pOH = pKw - pH;
        h_conc = Math.pow(10, -pH);
        oh_conc = Math.pow(10, -pOH);
      } else if (inputType === "poh") {
        pOH = inVal;
        pH = pKw - pOH;
        h_conc = Math.pow(10, -pH);
        oh_conc = Math.pow(10, -pOH);
      } else if (inputType === "h_conc") {
        if (inVal <= 0) { alert("Concentration must be positive non-zero"); return; }
        h_conc = inVal;
        pH = -Math.log10(h_conc);
        pOH = pKw - pH;
        oh_conc = Math.pow(10, -pOH);
      } else if (inputType === "oh_conc") {
        if (inVal <= 0) { alert("Concentration must be positive non-zero"); return; }
        oh_conc = inVal;
        pOH = -Math.log10(oh_conc);
        pH = pKw - pOH;
        h_conc = Math.pow(10, -pH);
      }

      // Determine Acidity Status relative to temperature-dependent neutral point
      let statusDesc = "";
      let indicator = "";
      const delta = pH - neutralPH;

      if (Math.abs(delta) < 0.05) {
        statusDesc = "Chemically Neutral";
        indicator = "Universal Indicator: Emerald Green (pH ≈ " + neutralPH.toFixed(2) + ")";
      } else if (delta < -3.5) {
        statusDesc = "Strongly Acidic";
        indicator = "Universal Indicator: Deep Red | Phenolphthalein: Colorless";
      } else if (delta < -1.0) {
        statusDesc = "Moderately Acidic";
        indicator = "Universal Indicator: Orange/Yellow | Methyl Orange: Red";
      } else if (delta < 0) {
        statusDesc = "Slightly Acidic";
        indicator = "Universal Indicator: Yellow-Green | Bromothymol Blue: Yellow";
      } else if (delta < 1.5) {
        statusDesc = "Slightly Alkaline";
        indicator = "Universal Indicator: Blue-Green | Phenolphthalein: Colorless/Faint Pink";
      } else if (delta < 3.5) {
        statusDesc = "Moderately Alkaline";
        indicator = "Universal Indicator: Cobalt Blue | Phenolphthalein: Vibrant Pink";
      } else {
        statusDesc = "Strongly Alkaline";
        indicator = "Universal Indicator: Deep Violet/Purple | Phenolphthalein: Magenta";
      }

      // Ratio calculation
      let ratioStr = "1.00 : 1";
      let ratioSub = "Exact parity (Neutral)";
      if (h_conc >= oh_conc) {
        const r = h_conc / oh_conc;
        ratioStr = r > 1e4 ? r.toExponential(2) + " : 1" : r.toFixed(2) + " : 1";
        ratioSub = "Excess [H⁺] over [OH⁻]";
      } else {
        const r = oh_conc / h_conc;
        ratioStr = "1 : " + (r > 1e4 ? r.toExponential(2) : r.toFixed(2));
        ratioSub = "Excess [OH⁻] over [H⁺]";
      }

      // Update UI
      document.getElementById("resSummaryTitle").textContent = "pH " + pH.toFixed(2) + " • " + statusDesc;
      document.getElementById("resSummarySub").textContent = "pOH = " + pOH.toFixed(2) + " | [H⁺] = " + h_conc.toExponential(3) + " M | [OH⁻] = " + oh_conc.toExponential(3) + " M";

      document.getElementById("resPH").textContent = pH.toFixed(2);
      document.getElementById("resPOH").textContent = pOH.toFixed(2);

      document.getElementById("resHConc").textContent = h_conc.toExponential(3) + " M";
      document.getElementById("resHConcSub").textContent = (h_conc * 1e9 >= 1 ? (h_conc * 1e9).toFixed(1) + " nmol/L" : (h_conc * 1e12).toFixed(1) + " pmol/L");

      document.getElementById("resOHConc").textContent = oh_conc.toExponential(3) + " M";
      document.getElementById("resOHConcSub").textContent = (oh_conc * 1e9 >= 1 ? (oh_conc * 1e9).toFixed(1) + " nmol/L" : (oh_conc * 1e12).toFixed(1) + " pmol/L");

      document.getElementById("resPKw").textContent = pKw.toFixed(2);
      document.getElementById("resPKwSub").textContent = "Kw = " + Kw.toExponential(2) + " at " + tempC.toFixed(1) + "°C";

      document.getElementById("resRatio").textContent = ratioStr;
      document.getElementById("resRatioSub").textContent = ratioSub;

      document.getElementById("resNeutralPoint").textContent = "pH " + neutralPH.toFixed(2) + " (at " + tempC.toFixed(1) + "°C)";
      document.getElementById("resIndicatorColor").textContent = indicator;
    }

    window.addEventListener("DOMContentLoaded", () => {
      calcPHtoPOH();
    });
  </script>
</body>
</html>
"""

TOOL_6_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Phosphate Dosing Calculator | Boiler Water &amp; Lead Corrosion Inhibitor Sizer</title>
  <meta name="description" content="Calculate boiler water phosphate conditioning (TSP, DSP, MSP), sodium-to-phosphate ratio, and municipal drinking water orthophosphate corrosion inhibitor dosing.">
  <link rel="canonical" href="https://calchub.cloud/phosphate-dosing-calculator.html">
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
        "name": "Phosphate Dosing Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates industrial boiler water phosphate treatment programs, sodium-to-phosphate Na:PO4 congruent ratios, and municipal lead and copper corrosion inhibitor dosing.",
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
            "name": "What is the primary function of phosphate treatment in industrial boilers?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Phosphate dosing serves two critical boiler functions: (1) Calcium scale precipitation: dissolved calcium hardness is reacted to precipitate soft, non-adherent hydroxyapatite sludge [Ca10(PO4)6(OH)2] that is easily purged through continuous blowdown rather than baking into hard calcium silicate or carbonate scale; and (2) pH buffering: maintaining alkalinity between pH 9.0 and 10.5 to prevent acidic and caustic gouging corrosion."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between Congruent Phosphate Treatment (CPT) and Equilibrium Phosphate Treatment (EPT)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Congruent Phosphate Treatment maintains a sodium-to-phosphate (Na:PO4) molar ratio between 2.3 and 2.8 using blends of trisodium phosphate (TSP, Na:PO4 = 3.0) and disodium phosphate (DSP, Na:PO4 = 2.0) to prevent free caustic (NaOH) generation during phosphate hideout. Equilibrium Phosphate Treatment (EPT) operates at lower phosphate residuals (0.5 to 2.5 mg/L) with small amounts of free NaOH specifically for high-pressure utility boilers (>1,500 psig)."
            }
          },
          {
            "@type": "Question",
            "name": "How does orthophosphate inhibit lead and copper corrosion in municipal drinking water?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Under the EPA Lead and Copper Rule (LCR), orthophosphate (PO4) is dosed at 0.5 to 3.0 mg/L as PO4 into drinking water mains. It forms a microscopically thin, highly insoluble mineral passivating layer of basic lead carbonate, lead pyromorphite [Pb5(PO4)3Cl], and copper phosphate minerals over aged pipes, preventing toxic lead leaching into tap water."
            }
          },
          {
            "@type": "Question",
            "name": "What causes 'phosphate hideout' in high-pressure boilers?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "At boiler pressures exceeding 1,200 psig (83 bar) and high heat fluxes, sodium phosphate salts exhibit retrograde solubility. Sodium phosphate precipitates onto the hottest boiler tube surfaces during high load ('hideout'), then re-dissolves back into the bulk water when boiler load drops, causing erratic phosphate residual swings and localized caustic gouging if Na:PO4 ratios are unmanaged."
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
      <span>Phosphate Dosing Calculator</span>
    </nav>

    <h1 class="tool-title">Phosphate Dosing &amp; Corrosion Inhibitor Calculator</h1>
    <p class="tool-subtitle">Boiler Water TSP/DSP Congruent Conditioning &amp; Municipal Lead/Copper Orthophosphate Passivation</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="phosphateAppPreset">Treatment Application &amp; Regulatory Standard</label>
            <select id="phosphateAppPreset" class="form-control" onchange="updatePhosphateApp()">
              <option value="boiler_congruent" selected>High-Pressure Boiler Congruent Treatment (ASME / EPRI Na:PO₄ 2.6)</option>
              <option value="boiler_low_press">Low-Pressure Package Boiler Residual (0 - 600 psig / 10 - 30 ppm PO₄)</option>
              <option value="municipal_lead">Municipal Drinking Water Lead &amp; Copper Rule (EPA LCR 1.0 - 3.0 mg/L PO₄)</option>
              <option value="cooling_inhibitor">Open Recirculating Cooling Tower Scale/Corrosion Inhibitor</option>
              <option value="custom">Custom Phosphate Application &amp; Dose</option>
            </select>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="pFlowRateVal">Water / Steam Flow Rate</label>
              <input type="number" id="pFlowRateVal" class="form-control" value="250" step="25" min="0.1">
            </div>
            <div class="form-group">
              <label for="pFlowRateUnit">Flow Rate Units</label>
              <select id="pFlowRateUnit" class="form-control">
                <option value="th" selected>Metric Tons / Hour (t/h steam)</option>
                <option value="gpm">Gallons / Minute (GPM)</option>
                <option value="mgd">Million Gallons / Day (MGD)</option>
                <option value="m3h">Cubic Meters / Hour (m³/h)</option>
                <option value="lbhr">Pounds / Hour Steam (lb/hr)</option>
              </select>
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="targetPO4DoseVal">Target Active PO₄³⁻ Dose</label>
              <input type="number" id="targetPO4DoseVal" class="form-control" value="4.0" step="0.5" min="0.05">
            </div>
            <div class="form-group">
              <label for="targetPO4DoseUnit">Concentration Units</label>
              <select id="targetPO4DoseUnit" class="form-control">
                <option value="ppm" selected>mg/L as PO₄³⁻ (ppm)</option>
                <option value="p_elem">mg/L as Elemental P</option>
              </select>
            </div>
          </div>

          <!-- Phosphate Chemical Reagent Selection -->
          <div class="form-group">
            <label for="chemReagentSelect">Phosphate Chemical Stock Form</label>
            <select id="chemReagentSelect" class="form-control" onchange="updateReagentSelection()">
              <option value="tsp_anhydrous">Trisodium Phosphate Anhydrous [Na₃PO₄, MW 163.94, Na:P = 3.0]</option>
              <option value="tsp_crystal" selected>Trisodium Phosphate Dodecahydrate [Na₃PO₄·12H₂O, MW 380.12]</option>
              <option value="dsp_anhydrous">Disodium Phosphate Anhydrous [Na₂HPO₄, MW 141.96, Na:P = 2.0]</option>
              <option value="msp_anhydrous">Monosodium Phosphate [NaH₂PO₄, MW 119.98, Na:P = 1.0]</option>
              <option value="ortho_liquid">Commercial Liquid Orthophosphate (36% w/w H₃PO₄ equiv, SG = 1.34)</option>
              <option value="polyphosphate">Sodium Hexametaphosphate (SHMP, Glassy Polyphosphate)</option>
            </select>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="chemPurityPct">Commercial Active Strength (%)</label>
              <input type="number" id="chemPurityPct" class="form-control" value="98.0" step="0.5" min="10.0" max="100.0">
            </div>
            <div class="form-group">
              <label for="chemStockSG">Stock Solution Specific Gravity (SG)</label>
              <input type="number" id="chemStockSG" class="form-control" value="1.05" step="0.01" min="1.0" max="1.6">
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="dayTankVolumeL">Day Tank Volume (Liters)</label>
              <input type="number" id="dayTankVolumeL" class="form-control" value="500" step="50" min="10">
              <span class="field-hint">Chemical solution batch tank size</span>
            </div>
            <div class="form-group">
              <label for="feedPumpMaxLph">Dosing Pump Max Flow (L/h)</label>
              <input type="number" id="feedPumpMaxLph" class="form-control" value="10.0" step="1.0" min="0.5">
            </div>
          </div>

          <button type="button" class="btn btn-primary" onclick="calcPhosphateDosing()" style="width: 100%; margin-top: 15px;">Calculate Phosphate Sizing &amp; Feed Rate</button>
        </div>
      </div>

      <!-- Output Results Panel -->
      <div class="results-card">
        <div class="result-box primary-result">
          <div class="result-label">Daily Commercial Reagent Required</div>
          <div id="resDailyCommercialKg" class="result-value">97.99 kg / day</div>
          <div id="resDailyCommercialLbs" class="result-subtext">216.03 lbs/day commercial TSP·12H₂O</div>
        </div>

        <div class="result-grid">
          <div class="result-item">
            <span class="result-label">Pure Active PO₄³⁻ Mass</span>
            <span id="resPurePO4MassDay" class="result-value highlight">24.00 kg/day</span>
            <span id="resPurePO4MassDaySub" class="result-subtext">52.91 lbs/day active PO₄</span>
          </div>
          <div class="result-item">
            <span class="result-label">Feed Pump Volumetric Rate</span>
            <span id="resPumpLph" class="result-value">4.08 L/h</span>
            <span id="resPumpGph" class="result-subtext">1.08 GPH (68.1 mL/min)</span>
          </div>
          <div class="result-item">
            <span class="result-label">Pump Stroke Setting</span>
            <span id="resPumpStroke" class="result-value">40.8%</span>
            <span id="resPumpStrokeSub" class="result-subtext">Of 10.0 L/h maximum pump rating</span>
          </div>
          <div class="result-item">
            <span class="result-label">Active Phosphate as P</span>
            <span id="resElemPConc" class="result-value">1.31 mg/L as P</span>
            <span class="result-subtext">Elemental P equivalent</span>
          </div>
          <div class="result-item">
            <span class="result-label">Day Tank Refill Autonomy</span>
            <span id="resTankAutonomy" class="result-value">5.1 Days</span>
            <span class="result-subtext">At continuous design feed rate</span>
          </div>
          <div class="result-item">
            <span class="result-label">Batch Day Tank Mix Recipe</span>
            <span id="resBatchRecipe" class="result-value">98.0 kg dry salt</span>
            <span class="result-subtext">Dissolve in 500 L water</span>
          </div>
        </div>

        <div class="result-details" style="margin-top: 15px;">
          <p><strong>Water Chemistry Program:</strong> <span id="resProgramGuideline">Complies with ASME CRTD-34 / EPRI boiler water congruent phosphate treatment limits.</span></p>
          <p><strong>Corrosion Passivation Layer:</strong> <span id="resCorrosionNote">Forms protective hydroxyapatite sludge in boilers or insoluble lead pyromorphite in drinking water mains.</span></p>
        </div>
      </div>
    </div>

    <!-- 1000+ Words Engineering Body -->
    <article class="article-body">
      <h2>Engineering Fundamentals of Industrial Phosphate Water Chemistry</h2>
      <p>Phosphate compounds ($\text{PO}_4^{3-}$) represent one of the most versatile, reliable, and foundational chemical treatment families utilized across modern thermal power generation, heavy industrial cooling towers, and municipal drinking water distribution networks. In high-temperature steam generation systems, phosphate dosing serves as the premier defense against catastrophic calcium carbonate and silicate scaling on high-heat-flux boiler tubes. In municipal potable water distribution, dilute orthophosphate dosing prevents toxic lead ($\text{Pb}^{2+}$) and copper ($\text{Cu}^{2+}$) leaching from aging subterranean service lines into drinking taps.</p>

      <p>In steam boiler systems, raw make-up water inevitably carries trace residual calcium ions ($\text{Ca}^{2+}$). If untreated, calcium precipitates at elevated heat-transfer surfaces to form rock-hard calcium carbonate ($\text{CaCO}_3$) or insulating calcium silicate ($\text{CaSiO}_3$) scale. A calcium scale layer merely $1.0\text{ mm}\ (0.04\text{ inches})$ thick reduces heat conduction by up to $15\%$, elevating tube wall temperatures past the metallurgy creep threshold and triggering tube rupture. Dosing orthophosphate transforms this scaling reaction into a protective precipitation mechanism:</p>

      <div class="formula-box">
        $$10\text{Ca}^{2+} + 6\text{PO}_4^{3-} + 2\text{OH}^- \longrightarrow \text{Ca}_{10}(\text{PO}_4)_6(\text{OH})_2\downarrow\text{ (hydroxyapatite)}$$
      </div>

      <p>Unlike crystalline carbonate or silicate scale, <strong>hydroxyapatite</strong> forms a soft, flocculent, non-adherent sludge that settles naturally into the mud drum or lower boiler headers, where it is effortlessly evacuated via automated continuous bottom blowdown without fouling boiler heat exchanger surfaces.</p>

      <h2>The Phosphate Triad and Sodium-to-Phosphate Molar Ratios</h2>
      <p>Industrial phosphate conditioning utilizes three inorganic sodium orthophosphate salts possessing distinct sodium-to-phosphate ($\text{Na}:\text{PO}_4$) molar ratios:</p>
      <ul>
        <li><strong>Trisodium Phosphate (TSP, Na₃PO₄):</strong> $\text{Na}:\text{PO}_4\text{ molar ratio} = 3.0 : 1$. Strongly alkaline in solution ($\text{pH } 11.5\text{ to } 12.0$ at 1% concentration). Yields both phosphate for hardness precipitation and hydroxide ($\text{OH}^-$) for alkalinity elevation:
        $$\text{Na}_3\text{PO}_4 + \text{H}_2\text{O} \rightleftharpoons 3\text{Na}^+ + \text{HPO}_4^{2-} + \text{OH}^-$$</li>
        <li><strong>Disodium Phosphate (DSP, Na₂HPO₄):</strong> $\text{Na}:\text{PO}_4\text{ molar ratio} = 2.0 : 1$. Moderately alkaline buffer ($\text{pH } 9.0\text{ to } 9.2$ at 1%). Used to buffer excess alkalinity without generating free hydroxide ions.</li>
        <li><strong>Monosodium Phosphate (MSP, NaH₂PO₄):</strong> $\text{Na}:\text{PO}_4\text{ molar ratio} = 1.0 : 1$. Weakly acidic salt ($\text{pH } 4.5$ at 1%). Dosed strictly to suppress runaway caustic generation during operational upsets.</li>
      </ul>

      <h2>Boiler Phosphate Programs: CPT, EPT, and Hideout Control</h2>
      <p>As boiler operating pressures increase, the behavior of sodium phosphate changes dramatically due to <strong>retrograde solubility</strong> (phosphate solubility decreases as water temperature rises):</p>

      <h3>1. Coordinated Phosphate Treatment (CPT)</h3>
      <p>CPT maintains a fixed $\text{Na}:\text{PO}_4$ molar ratio of exactly $3.0 : 1$, matching the stoichiometry of pure trisodium phosphate. The objective is to maintain an alkaline protective environment ($\text{pH } 9.5\text{ to } 10.5$) while guaranteeing that zero uncombined "free caustic" ($\text{NaOH}$) exists in the bulk water, preventing caustic embrittlement of rolled tube joints.</p>

      <h3>2. Congruent Phosphate Treatment</h3>
      <p>At operating pressures above $60\text{ bar}\ (870\text{ psig})$, TSP undergoes incongruent dissolution. Phosphate precipitates onto hot tube walls as a sodium-rich complex ($x\text{Na}_2\text{O} \cdot y\text{P}_2\text{O}_5$), leaving unbuffered free sodium hydroxide in the boundary layer. To combat this, <strong>Congruent Phosphate Treatment</strong> enforces a reduced $\text{Na}:\text{PO}_4$ molar ratio between $2.3\text{ and } 2.8$ through precision co-injection of TSP and DSP:</p>

      <div class="formula-box">
        $$\text{Molar Ratio} = \frac{\text{Moles of Na}^+}{\text{Moles of PO}_4^{3-}} = \frac{3 \cdot n_{\text{TSP}} + 2 \cdot n_{\text{DSP}}}{n_{\text{TSP}} + n_{\text{DSP}}} \quad (2.3 \le \text{Ratio} \le 2.8)$$
      </div>

      <h3>3. Equilibrium Phosphate Treatment (EPT)</h3>
      <p>In supercritical and high-pressure utility boilers ($&gt;100\text{ bar} / 1,500\text{ psig}$), severe phosphate hideout occurs. EPT restricts phosphate residual to ultra-low thresholds ($0.2\text{ to } 2.0\text{ mg/L PO}_4$) with a target $\text{pH } 9.0\text{ to } 9.6$ maintained by micro-dosing caustic soda ($\text{NaOH}$) or volatile neutralizing amines.</p>

      <h2>Municipal Drinking Water Lead &amp; Copper Rule (EPA LCR) Passivation</h2>
      <p>Under the United States Environmental Protection Agency (EPA) <strong>Lead and Copper Rule Revisions (LCRR)</strong>, public water systems with lead service lines or copper plumbing with lead solder must maintain an approved corrosion control treatment (CCT). Injecting food-grade orthophosphate ($\text{H}_3\text{PO}_4$ or $\text{Zn}_3(\text{PO}_4)_2$) establishes an insoluble passivating mineral scale over internal pipe lumens:</p>

      <div class="formula-box">
        $$5\text{Pb}^{2+} + 3\text{PO}_4^{3-} + \text{Cl}^- \longrightarrow \text{Pb}_5(\text{PO}_4)_3\text{Cl}\downarrow\text{ (chloropyromorphite)}$$
      </div>
      <p>Chloropyromorphite has an extraordinarily low solubility product ($K_{sp} \approx 10^{-84}$), effectively locking toxic lead cations inside a crystalline mineral matrix and reducing dissolved lead concentrations at consumer taps well below the EPA action level of $15\ \mu\text{g/L (ppb)}$ (lowered toward $10\ \mu\text{g/L}$ under newer standards).</p>

      <h2>Mathematical Sizing Formulas for Reagent Dosing</h2>
      <p>To convert from active phosphate target concentration ($C_{\text{PO}_4}$ in $\text{mg/L}$) to commercial chemical feed rate, engineers apply stoichiometric molecular weight ratios:</p>

      <div class="formula-box">
        $$F_{\text{stoich}} = \frac{M_{\text{reagent}}}{M_{\text{PO}_4}} = \frac{M_{\text{reagent}}}{94.971\text{ g/mol}}$$
      </div>
      <p>For common commercial reagents:</p>
      <ul>
        <li>Trisodium Phosphate Dodecahydrate ($\text{Na}_3\text{PO}_4 \cdot 12\text{H}_2\text{O}, \text{MW} = 380.12$): $F_{\text{stoich}} = \frac{380.12}{94.971} = 4.0025$</li>
        <li>Trisodium Phosphate Anhydrous ($\text{Na}_3\text{PO}_4, \text{MW} = 163.94$): $F_{\text{stoich}} = \frac{163.94}{94.971} = 1.7262$</li>
        <li>Disodium Phosphate Anhydrous ($\text{Na}_2\text{HPO}_4, \text{MW} = 141.96$): $F_{\text{stoich}} = \frac{141.96}{94.971} = 1.4948$</li>
        <li>Commercial Liquid Orthophosphate ($36\%\text{ H}_3\text{PO}_4\text{ equivalent}$): $F_{\text{stoich}} = \frac{97.994}{94.971 \times 0.36} = 2.866$</li>
      </ul>

      <p>The daily commercial mass delivery rate ($\dot{M}_{\text{reagent}}$) is calculated from the volumetric flow rate ($Q$ in $\text{m}^3/\text{day}$ or $\text{MGD}$):</p>

      <div class="formula-box">
        $$\dot{M}_{\text{reagent}}\text{ (kg/day)} = \frac{Q\text{ (m}^3/\text{day)} \times C_{\text{PO}_4}\text{ (g/m}^3) \times F_{\text{stoich}}}{1,000 \times \left(\frac{\%_{\text{purity}}}{100}\right)}$$
      </div>

      <h2>ASME and EPRI Water Chemistry Benchmark Table</h2>
      <p>The table below summarizes recommended phosphate control parameters across industrial boiler pressure classes per <strong>ASME Consensus CRTD-34</strong>:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Operating Pressure (psig / bar)</th>
              <th>Recommended Control Program</th>
              <th>Target PO₄³⁻ Residual (mg/L)</th>
              <th>Target Boiler pH (at 25°C)</th>
              <th>Allowed Na:PO₄ Ratio</th>
              <th>Max Feedwater Silica (ppm)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>0 &ndash; 300 psig (0 &ndash; 21 bar)</td>
              <td>Conventional / Continuous Phosphate</td>
              <td>15 &ndash; 30 mg/L</td>
              <td>10.0 &ndash; 11.2</td>
              <td>2.8 &ndash; 3.0</td>
              <td>&lt; 5.0 ppm</td>
            </tr>
            <tr>
              <td>301 &ndash; 600 psig (21 &ndash; 41 bar)</td>
              <td>Coordinated Phosphate (CPT)</td>
              <td>10 &ndash; 20 mg/L</td>
              <td>9.5 &ndash; 10.5</td>
              <td>2.6 &ndash; 2.8</td>
              <td>&lt; 2.0 ppm</td>
            </tr>
            <tr>
              <td>601 &ndash; 900 psig (41 &ndash; 62 bar)</td>
              <td>Congruent Phosphate (CPT)</td>
              <td>5 &ndash; 10 mg/L</td>
              <td>9.2 &ndash; 10.0</td>
              <td>2.4 &ndash; 2.6</td>
              <td>&lt; 0.5 ppm</td>
            </tr>
            <tr>
              <td>901 &ndash; 1,500 psig (62 &ndash; 103 bar)</td>
              <td>Congruent / Equilibrium (EPT)</td>
              <td>2 &ndash; 6 mg/L</td>
              <td>9.0 &ndash; 9.6</td>
              <td>2.2 &ndash; 2.5</td>
              <td>&lt; 0.1 ppm</td>
            </tr>
            <tr>
              <td>&gt; 1,500 psig (&gt; 103 bar) Utility</td>
              <td>Equilibrium Phosphate or AVT</td>
              <td>0.5 &ndash; 2.0 mg/L</td>
              <td>9.0 &ndash; 9.4</td>
              <td>Congruent / Caustic Trim</td>
              <td>&lt; 0.02 ppm</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Practical Worked Case Study: Sizing a Boiler Chemical Feed Skid</h2>
      <div class="worked-example-card">
        <h3>Thermal Power Case Study: Congruent Phosphate Treatment</h3>
        <p><strong>Scenario:</strong> A co-generation power boiler produces $Q = 200.0\text{ metric tons / hour}$ ($200\text{ m}^3/\text{h}$, equivalent to $440,924\text{ lb/hr}$ or $880\text{ GPM}$) of superheated steam at $P = 65\text{ bar}\ (942\text{ psig})$. Continuous economizer blowdown is maintained at $2.0\%$ of steam flow. Water chemistry protocols require maintaining an active orthophosphate concentration of $C_{\text{PO}_4} = 5.0\text{ mg/L as PO}_4^{3-}$ in the boiler drum water. Commercial crystalline trisodium phosphate dodecahydrate ($\text{Na}_3\text{PO}_4 \cdot 12\text{H}_2\text{O}, \text{MW} = 380.12\text{ g/mol}$, $98.0\%\text{ chemical purity}$) is utilized. The chemical day tank has a liquid volume of $V_{\text{tank}} = 1,000\text{ Liters}$, and the diaphragm metering pump is rated at a maximum capacity of $q_{\text{pump, max}} = 15.0\text{ L/h}$.</p>

        <p><strong>Step 1: Compute Pure Active PO₄³⁻ Mass Requirement:</strong></p>
        $$\text{Daily Treated Water Volume} = 200\text{ m}^3/\text{h} \times 24\text{ h/day} = 4,800\text{ m}^3/\text{day}$$
        $$\dot{m}_{\text{pure PO}_4} = \frac{4,800\text{ m}^3/\text{day} \times 5.0\text{ g/m}^3}{1,000} = 24.00\text{ kg / day pure PO}_4^{3-}\ (52.91\text{ lbs/day})$$

        <p><strong>Step 2: Account for Reagent Stoichiometry and Purity:</strong></p>
        $$F_{\text{stoich}} = \frac{380.12\text{ g/mol}}{94.971\text{ g/mol}} = 4.0025$$
        $$\text{Daily Commercial Product} = \frac{24.00\text{ kg/day} \times 4.0025}{0.98\text{ purity}} = \frac{96.06}{0.98} = 98.02\text{ kg / day}\ (216.1\text{ lbs/day})$$

        <p><strong>Step 3: Day Tank Solution Batch Formulation:</strong></p>
        <p>If the operator dissolves exactly one $25\text{ kg}$ commercial sack of TSP·12H₂O per batch into the $1,000\text{ Liter}$ day tank:</p>
        $$\text{Batch Concentration} = \frac{25\text{ kg}}{1,000\text{ L}} = 2.50\%\text{ w/v solution}\ (25\text{ g/L})$$
        $$\text{Active PO}_4\text{ per Liter of Tank} = \frac{25\text{ g} \times 0.98}{4.0025} = 6.121\text{ g PO}_4 / \text{L}$$

        <p><strong>Step 4: Metering Pump Dosing Rate and Stroke Percentage:</strong></p>
        $$q_{\text{pump}} = \frac{24.00\text{ kg PO}_4/\text{day} \times 1,000\text{ g/kg}}{6.121\text{ g/L} \times 24\text{ h/day}} = \frac{24,000}{146.90} = 163.37\text{ Liters / day}$$
        $$q_{\text{pump, hourly}} = \frac{163.37\text{ L/day}}{24\text{ h}} = 6.807\text{ Liters / Hour}$$
        $$\text{Stroke}\% = \left(\frac{6.807\text{ L/h}}{15.0\text{ L/h}}\right) \times 100\% = 45.38\%$$
        <p>Operating at $45.4\%$ stroke provides optimal linear metering without diaphragm cavitation.</p>

        <p><strong>Step 5: Tank Autonomy:</strong></p>
        $$\text{Autonomy} = \frac{1,000\text{ Liters}}{163.37\text{ L/day}} = 6.12\text{ Operating Days}$$
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
          <p class="footer-about">High-precision boiler water conditioning, orthophosphate corrosion inhibition, and chemical feed skid engineering tools conforming to ASME, EPRI, and EPA standards.</p>
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
            <li><a href="https://www.asme.org" target="_blank" rel="noopener">ASME Boiler Water Quality Consensus CRTD-34</a></li>
            <li><a href="https://www.epri.com" target="_blank" rel="noopener">EPRI Steam Generator Chemistry Guidelines</a></li>
            <li><a href="https://www.epa.gov" target="_blank" rel="noopener">EPA Lead and Copper Rule Revisions (LCRR)</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    const REAGENT_PROPERTIES = {
      tsp_anhydrous: { mw: 163.94, po4_mw: 94.971, purity: 98.0, sg: 1.05, desc: "Anhydrous TSP" },
      tsp_crystal: { mw: 380.12, po4_mw: 94.971, purity: 98.0, sg: 1.05, desc: "TSP Dodecahydrate" },
      dsp_anhydrous: { mw: 141.96, po4_mw: 94.971, purity: 98.0, sg: 1.04, desc: "Anhydrous DSP" },
      msp_anhydrous: { mw: 119.98, po4_mw: 94.971, purity: 98.0, sg: 1.04, desc: "Monosodium Phosphate" },
      ortho_liquid: { mw: 97.994, po4_mw: 94.971, purity: 36.0, sg: 1.34, desc: "Liquid Orthophosphate 36%" },
      polyphosphate: { mw: 101.96, po4_mw: 94.971, purity: 68.0, sg: 1.10, desc: "Sodium Hexametaphosphate" }
    };

    function updatePhosphateApp() {
      const app = document.getElementById("phosphateAppPreset").value;
      if (app === "boiler_congruent") {
        document.getElementById("targetPO4DoseVal").value = 4.0;
        document.getElementById("targetPO4DoseUnit").value = "ppm";
        document.getElementById("chemReagentSelect").value = "tsp_crystal";
      } else if (app === "boiler_low_press") {
        document.getElementById("targetPO4DoseVal").value = 15.0;
        document.getElementById("targetPO4DoseUnit").value = "ppm";
        document.getElementById("chemReagentSelect").value = "tsp_crystal";
      } else if (app === "municipal_lead") {
        document.getElementById("targetPO4DoseVal").value = 2.0;
        document.getElementById("targetPO4DoseUnit").value = "ppm";
        document.getElementById("chemReagentSelect").value = "ortho_liquid";
      } else if (app === "cooling_inhibitor") {
        document.getElementById("targetPO4DoseVal").value = 6.0;
        document.getElementById("targetPO4DoseUnit").value = "ppm";
        document.getElementById("chemReagentSelect").value = "polyphosphate";
      }
      updateReagentSelection();
    }

    function updateReagentSelection() {
      const r = document.getElementById("chemReagentSelect").value;
      if (REAGENT_PROPERTIES[r]) {
        document.getElementById("chemPurityPct").value = REAGENT_PROPERTIES[r].purity;
        document.getElementById("chemStockSG").value = REAGENT_PROPERTIES[r].sg;
      }
      calcPhosphateDosing();
    }

    function calcPhosphateDosing() {
      const flowVal = parseFloat(document.getElementById("pFlowRateVal").value) || 0;
      const flowUnit = document.getElementById("pFlowRateUnit").value;
      let doseVal = parseFloat(document.getElementById("targetPO4DoseVal").value) || 0;
      const doseUnit = document.getElementById("targetPO4DoseUnit").value;

      const reagentKey = document.getElementById("chemReagentSelect").value;
      const reagent = REAGENT_PROPERTIES[reagentKey] || REAGENT_PROPERTIES.tsp_crystal;
      const purityPct = parseFloat(document.getElementById("chemPurityPct").value) || reagent.purity;
      const sg = parseFloat(document.getElementById("chemStockSG").value) || reagent.sg;
      const tankVolL = parseFloat(document.getElementById("dayTankVolumeL").value) || 500;
      const maxPumpLph = parseFloat(document.getElementById("feedPumpMaxLph").value) || 10.0;

      // Convert target dose to mg/L active PO4
      let po4_ppm = doseVal;
      if (doseUnit === "p_elem") {
        // P (30.974) to PO4 (94.971) => factor 94.971 / 30.974 = 3.066
        po4_ppm = doseVal * 3.066;
      }
      const elemP_ppm = po4_ppm / 3.066;

      // Flow conversion to m3/day
      let m3_per_day = 0;
      let flow_mgd = 0;
      if (flowUnit === "th") {
        m3_per_day = flowVal * 24.0;
        flow_mgd = (flowVal * 24.0) / 3785.41;
      } else if (flowUnit === "m3h") {
        m3_per_day = flowVal * 24.0;
        flow_mgd = (flowVal * 24.0) / 3785.41;
      } else if (flowUnit === "gpm") {
        m3_per_day = flowVal * 5.45099;
        flow_mgd = (flowVal * 1440.0) / 1000000.0;
      } else if (flowUnit === "mgd") {
        flow_mgd = flowVal;
        m3_per_day = flowVal * 3785.41;
      } else if (flowUnit === "lbhr") {
        const kg_hr = flowVal * 0.453592;
        m3_per_day = (kg_hr * 24.0) / 1000.0;
        flow_mgd = m3_per_day / 3785.41;
      }

      // Pure active PO4 mass
      const purePO4KgDay = (m3_per_day * po4_ppm) / 1000.0;
      const purePO4LbsDay = purePO4KgDay * 2.20462;

      // Stoichiometric multiplier: reagent MW / PO4 MW
      const stoichFactor = reagent.mw / reagent.po4_mw;

      // Commercial mass required
      const commKgDay = (purePO4KgDay * stoichFactor) / (purityPct / 100.0);
      const commLbsDay = commKgDay * 2.20462;

      // Volumetric rate of chemical solution
      // In typical day tank batch, 1 day of commercial chemical is dissolved in tankVolL
      // Pump feed rate = tankVolL / 24 h (if 1 tank per day) or calculated if batching
      // Here: assume batch contains commKgDay dissolved in tankVolL:
      // Density = sg kg/L
      let pumpLph = 0;
      if (reagentKey === "ortho_liquid") {
        // Direct liquid feed
        const commLitersDay = commKgDay / sg;
        pumpLph = commLitersDay / 24.0;
      } else {
        // Dry powder dissolved in day tank: size pump to deliver 1 tank per 2-5 days
        // Standard assumption: 10% solution make-up
        const solutionLitersDay = commKgDay / (0.10 * sg);
        pumpLph = solutionLitersDay / 24.0;
      }

      const pumpGph = pumpLph * 0.264172;
      const pumpStrokePct = (pumpLph / maxPumpLph) * 100.0;

      // Tank autonomy
      const autonomyDays = pumpLph > 0 ? (tankVolL / (pumpLph * 24.0)).toFixed(1) : "N/A";

      // Render Outputs
      document.getElementById("resDailyCommercialKg").textContent = commKgDay.toFixed(2) + " kg / day";
      document.getElementById("resDailyCommercialLbs").textContent = commLbsDay.toFixed(2) + " lbs / day " + reagent.desc;

      document.getElementById("resPurePO4MassDay").textContent = purePO4KgDay.toFixed(2) + " kg / day";
      document.getElementById("resPurePO4MassDaySub").textContent = purePO4LbsDay.toFixed(2) + " lbs / day active PO₄³⁻";

      document.getElementById("resPumpLph").textContent = pumpLph.toFixed(2) + " L/h";
      document.getElementById("resPumpGph").textContent = pumpGph.toFixed(2) + " GPH (" + (pumpLph * 1000 / 60).toFixed(1) + " mL/min)";

      document.getElementById("resPumpStroke").textContent = pumpStrokePct.toFixed(1) + "%";
      let strokeNote = "Of " + maxPumpLph.toFixed(1) + " L/h pump capacity";
      if (pumpStrokePct < 10) strokeNote += " (Consider smaller pump or greater dilution)";
      else if (pumpStrokePct > 90) strokeNote += " (Consider pump capacity upgrade)";
      else strokeNote += " (Optimal 10-90% linear operating range)";
      document.getElementById("resPumpStrokeSub").textContent = strokeNote;

      document.getElementById("resElemPConc").textContent = elemP_ppm.toFixed(2) + " mg/L as P";
      document.getElementById("resTankAutonomy").textContent = autonomyDays + " Days";

      document.getElementById("resBatchRecipe").textContent = (commKgDay / (autonomyDays > 0 ? autonomyDays : 1)).toFixed(1) + " kg dry chemical";
    }

    window.addEventListener("DOMContentLoaded", () => {
      calcPhosphateDosing();
    });
  </script>
</body>
</html>
"""

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p5 = os.path.join(base_dir, "ph-poh-calculator.html")
    p6 = os.path.join(base_dir, "phosphate-dosing-calculator.html")

    with open(p5, "w", encoding="utf-8") as f:
        f.write(TOOL_5_HTML)
    print(f"Generated {p5}")

    with open(p6, "w", encoding="utf-8") as f:
        f.write(TOOL_6_HTML)
    print(f"Generated {p6}")

if __name__ == "__main__":
    main()
