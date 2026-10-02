# -*- coding: utf-8 -*-
"""
Script to generate Batch 17 Part 1 tools:
1. sulphuric-acid-dosing-calculator.html
2. titration-calculator.html
"""
import os

TOOL_1_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sulfuric Acid Dosing Calculator | H2SO4 Neutralization Sizer</title>
  <meta name="description" content="Calculate sulfuric acid (H2SO4) dosing rates for water alkalinity reduction, pH neutralization, cooling tower scale control, and chemical feed pump sizing.">
  <link rel="canonical" href="https://calchub.cloud/sulphuric-acid-dosing-calculator.html">
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
        "name": "Sulfuric Acid Dosing Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates concentrated sulfuric acid (93% and 98% H2SO4) feed rates, alkalinity reduction stoichiometry, wastewater pH neutralization, and metering pump stroke parameters.",
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
            "name": "What is the stoichiometric ratio of sulfuric acid to water alkalinity?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The reaction between sulfuric acid and calcium bicarbonate alkalinity is: Ca(HCO3)2 + H2SO4 -> CaSO4 + 2CO2 + 2H2O. Stoichiometrically, 98.08 grams of pure H2SO4 neutralizes 100.09 grams of alkalinity as CaCO3, establishing a mass ratio of 0.980 mg/L of pure H2SO4 per 1.0 mg/L of alkalinity as CaCO3 reduced."
            }
          },
          {
            "@type": "Question",
            "name": "Why is 93% (66° Baumé) sulfuric acid preferred over 98% in industrial feed systems?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "While 98% sulfuric acid is more concentrated, 93.2% H2SO4 (66° Baumé) has a significantly lower freezing point of -35°C (-31°F) compared to +3°C (+37°F) for 98% acid. In cold climates, 98% sulfuric acid freezes readily in unheated outdoor storage tanks and pipelines, whereas 93% acid remains liquid without electrical heat tracing."
            }
          },
          {
            "@type": "Question",
            "name": "How does sulfuric acid dosing impact sulfate concentration and calcium sulfate scaling?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Every 1.0 mg/L of pure H2SO4 added to water contributes exactly 0.979 mg/L of sulfate ions (SO4 2-). In cooling towers and reverse osmosis reject streams, excessive sulfuric acid dosing can trigger calcium sulfate (gypsum, CaSO4·2H2O) precipitation once the solubility product exceeds [Ca2+][SO4 2-] > 5x10^-5."
            }
          },
          {
            "@type": "Question",
            "name": "What safety precautions are critical when diluting concentrated sulfuric acid?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Diluting sulfuric acid is intensely exothermic, releasing approximately 74.7 kJ/mol of heat. Operators must strictly follow the rule: ALWAYS ADD ACID TO WATER, NEVER WATER TO ACID. Adding water to concentrated acid causes violent localized boiling, explosive steam generation, and hazardous acid splattering."
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
      <span>Sulfuric Acid Dosing Calculator</span>
    </nav>

    <h1 class="tool-title">Sulfuric Acid Dosing &amp; Neutralization Calculator</h1>
    <p class="tool-subtitle">H₂SO₄ Alkalinity Reduction, Wastewater pH Neutralization &amp; Chemical Pump Sizing</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="treatmentApplication">Process Application Objective</label>
            <select id="treatmentApplication" class="form-control" onchange="updateApplicationPreset()">
              <option value="alkalinity_trim" selected>Cooling Tower Alkalinity Trimming (M-Alkalinity Scale Prevention)</option>
              <option value="wastewater_neut">Alkaline Wastewater Neutralization (pH 11 &rarr; pH 7.5)</option>
              <option value="ro_pretreat">Reverse Osmosis Feed Decarbonation (LSI Suppression)</option>
              <option value="direct_dose">Direct Target Acid Concentration (mg/L Dose)</option>
            </select>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="waterFlowVal">Water Flow Rate</label>
              <input type="number" id="waterFlowVal" class="form-control" value="500" step="50" min="0.1">
            </div>
            <div class="form-group">
              <label for="waterFlowUnit">Flow Units</label>
              <select id="waterFlowUnit" class="form-control">
                <option value="gpm" selected>Gallons / Minute (GPM)</option>
                <option value="m3h">Cubic Meters / Hour (m³/h)</option>
                <option value="mgd">Million Gallons / Day (MGD)</option>
                <option value="lps">Liters / Second (L/s)</option>
                <option value="mld">Million Liters / Day (MLD)</option>
              </select>
            </div>
          </div>

          <!-- Alkalinity Inputs -->
          <div id="alkalinityInputsGroup" class="grid-2-col">
            <div class="form-group">
              <label for="initialAlkVal">Initial Alkalinity (as CaCO₃)</label>
              <input type="number" id="initialAlkVal" class="form-control" value="220" step="5" min="0">
              <span class="field-hint">Raw water mg/L as CaCO₃</span>
            </div>
            <div class="form-group">
              <label for="targetAlkVal">Target Alkalinity (as CaCO₃)</label>
              <input type="number" id="targetAlkVal" class="form-control" value="80" step="5" min="0">
              <span class="field-hint">Desired treated mg/L as CaCO₃</span>
            </div>
          </div>

          <!-- Direct Dose Input -->
          <div id="directDoseGroup" class="form-group" style="display: none;">
            <label for="directAcidDosePpm">Target Pure H₂SO₄ Dose (mg/L ppm)</label>
            <input type="number" id="directAcidDosePpm" class="form-control" value="50.0" step="5.0" min="0.1">
          </div>

          <!-- Commercial Acid Grade -->
          <div class="grid-2-col">
            <div class="form-group">
              <label for="acidCommercialGrade">Sulfuric Acid Commercial Grade</label>
              <select id="acidCommercialGrade" class="form-control" onchange="updateGradeProps()">
                <option value="93" selected>66° Baumé / 93.2% Industrial (SG = 1.835, Freezes -35°C)</option>
                <option value="98">98.0% Concentrated Technical (SG = 1.840, Freezes +3°C)</option>
                <option value="77">60° Baumé / 77.7% (SG = 1.706, Freezes -11°C)</option>
                <option value="50">50.0% Dilute / Battery Grade (SG = 1.395)</option>
                <option value="custom">Custom Concentration &amp; Specific Gravity</option>
              </select>
            </div>
            <div class="form-group">
              <label for="acidStrengthPct">Active H₂SO₄ Concentration (% w/w)</label>
              <input type="number" id="acidStrengthPct" class="form-control" value="93.2" step="0.5" min="10.0" max="100.0">
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="acidSGVal">Solution Specific Gravity (SG)</label>
              <input type="number" id="acidSGVal" class="form-control" value="1.835" step="0.005" min="1.05" max="1.90">
            </div>
            <div class="form-group">
              <label for="dosingPumpMaxCapacityLph">Metering Pump Max Rating (L/h)</label>
              <input type="number" id="dosingPumpMaxCapacityLph" class="form-control" value="50.0" step="5.0" min="0.5">
            </div>
          </div>

          <button type="button" class="btn btn-primary" onclick="calcSulfuricAcid()" style="width: 100%; margin-top: 15px;">Calculate Acid Dosing Rate</button>
        </div>
      </div>

      <!-- Output Results Panel -->
      <div class="results-card">
        <div class="result-box primary-result">
          <div class="result-label">Feed Pump Volumetric Delivery Rate</div>
          <div id="resPumpLphVal" class="result-value">9.16 L / hour</div>
          <div id="resPumpAlternateUnits" class="result-subtext">152.7 mL/min (2.42 GPH commercial 93.2% acid)</div>
        </div>

        <div class="result-grid">
          <div class="result-item">
            <span class="result-label">Active Pure H₂SO₄ Dose</span>
            <span id="resPureAcidDose" class="result-value highlight">137.2 mg/L</span>
            <span id="resPureAcidDoseSub" class="result-subtext">Neutralizes 140.0 mg/L Alkalinity</span>
          </div>
          <div class="result-item">
            <span class="result-label">Daily Commercial Acid Mass</span>
            <span id="resDailyCommercialKg" class="result-value">403.4 kg / day</span>
            <span id="resDailyCommercialLbs" class="result-subtext">889.4 lbs / day commercial acid</span>
          </div>
          <div class="result-item">
            <span class="result-label">Daily Volumetric Acid Use</span>
            <span id="resDailyCommercialLiters" class="result-value">219.8 L / day</span>
            <span class="result-subtext">58.1 US Gallons / day</span>
          </div>
          <div class="result-item">
            <span class="result-label">Pump Stroke Setting</span>
            <span id="resPumpStrokeSetting" class="result-value">18.3%</span>
            <span class="result-subtext">Of 50.0 L/h maximum pump rating</span>
          </div>
          <div class="result-item">
            <span class="result-label">Sulfate Ion (SO₄²⁻) Increase</span>
            <span id="resSulfateIncrease" class="result-value">+134.4 mg/L</span>
            <span class="result-subtext">Added mineral sulfate load</span>
          </div>
          <div class="result-item">
            <span class="result-label">Exothermic Heat Release</span>
            <span id="resExothermicHeat" class="result-value">7.8 kW</span>
            <span class="result-subtext">Continuous heat of mixing</span>
          </div>
        </div>

        <div class="result-details" style="margin-top: 15px;">
          <p><strong>Drum / Tote Storage Autonomy:</strong> <span id="resStorageAutonomy">Standard 1,000 L IBC Tote lasts 4.5 Days | 200 L Drum lasts 0.9 Days.</span></p>
          <p><strong>Gypsum Scaling Warning:</strong> <span id="resGypsumWarning">Sulfate increase is within safe limits for non-scaling calcium sulfate operation.</span></p>
        </div>
      </div>
    </div>

    <!-- 1000+ Words Engineering Body -->
    <article class="article-body">
      <h2>Principles of Industrial Sulfuric Acid Water Treatment</h2>
      <p><strong>Sulfuric acid</strong> ($\text{H}_2\text{SO}_4$, hydrogen sulfate) is the world's most widely consumed commodity chemical and the primary mineral acid utilized across industrial cooling water systems, municipal drinking water decarbonation, reverse osmosis pretreatment, and wastewater neutralization facilities. Renowned for its high electronegativity, intense chemical density, and low unit production cost, sulfuric acid provides double the neutralization capacity per mole compared to monoprotic acids like hydrochloric acid ($\text{HCl}$) or nitric acid ($\text{HNO}_3$).</p>

      <p>In aqueous environments, sulfuric acid acts as a <strong>diprotic strong mineral acid</strong>. Its dissociation occurs in two sequential equilibrium stages:</p>

      <div class="formula-box">
        $$\text{Stage 1: } \text{H}_2\text{SO}_4 + \text{H}_2\text{O} \longrightarrow \text{H}_3\text{O}^+ + \text{HSO}_4^- \quad (K_{a1} \gg 10^3, \text{ essentially 100% dissociated})$$
        $$\text{Stage 2: } \text{HSO}_4^- + \text{H}_2\text{O} \rightleftharpoons \text{H}_3\text{O}^+ + \text{SO}_4^{2-} \quad (K_{a2} = 1.02 \times 10^{-2}\text{ at } 25^\circ\text{C}, pK_{a2} = 1.99)$$
      </div>

      <p>Because the second dissociation constant $K_{a2}$ is relatively large, both hydrogen protons dissociate completely at all operational pH levels encountered in industrial water treatment ($\text{pH } &gt; 3.5$). Consequently, every mole of pure $\text{H}_2\text{SO}_4$ ($98.078\text{ g/mol}$) releases exactly two equivalents of reactive hydronium ions ($\text{H}^+$), yielding an equivalent weight of:</p>

      <div class="formula-box">
        $$\text{Equivalent Weight} = \frac{\text{MW}}{z} = \frac{98.078\text{ g/mol}}{2\text{ eq/mol}} = 49.039\text{ g/equivalent}$$
      </div>

      <h2>Alkalinity Destruction Stoichiometry in Cooling Towers and RO</h2>
      <p>In recirculating evaporative cooling towers, evaporation removes pure water vapor while leaving dissolved minerals behind. This concentrates calcium bicarbonate ($\text{Ca(HCO}_3)_2$), elevating pH and carbonate ion ($\text{CO}_3^{2-}$) levels until insoluble calcium carbonate ($\text{CaCO}_3$) scale forms on condenser tubes. To maximize cycles of concentration ($CoC$) without scaling, water treatment engineers inject sulfuric acid to selectively destroy bicarbonate alkalinity, converting it into soluble calcium sulfate ($\text{CaSO}_4$) and off-gassed carbon dioxide ($\text{CO}_2$):</p>

      <div class="formula-box">
        $$\text{Ca(HCO}_3)_2 + \text{H}_2\text{SO}_4 \longrightarrow \text{CaSO}_4 + 2\text{CO}_2\uparrow + 2\text{H}_2\text{O}$$
      </div>

      <p>Because alkalinity is universally reported in terms of calcium carbonate equivalents ($\text{mg/L as CaCO}_3$, $\text{MW} = 100.087\text{ g/mol}$), the exact stoichiometric relationship between pure sulfuric acid demand and alkalinity destruction is:</p>

      <div class="formula-box">
        $$\text{Stoichiometric Mass Ratio} = \frac{\text{MW}(\text{H}_2\text{SO}_4)}{\text{MW}(\text{CaCO}_3)} = \frac{98.078\text{ g}}{100.087\text{ g}} = 0.97993 \approx 0.980\text{ mg/L H}_2\text{SO}_4\text{ per mg/L Alk destroyed}$$
      </div>

      <p>Conversely, $1.0\text{ mg/L of pure 100% H}_2\text{SO}_4$ destroys exactly $1.0205\text{ mg/L of alkalinity as CaCO}_3$. The required pure acid dosage ($D_{\text{pure}}$ in $\text{mg/L}$) for a target alkalinity reduction ($\Delta\text{Alk} = \text{Alk}_{\text{initial}} - \text{Alk}_{\text{target}}$) is formulated as:</p>

      <div class="formula-box">
        $$D_{\text{pure}}\text{ (mg/L)} = 0.980 \times \left( \text{Alk}_{\text{initial}} - \text{Alk}_{\text{target}} \right)$$
      </div>

      <h2>Commercial Grades: 66° Baumé (93.2%) vs. 98% Concentrated Acid</h2>
      <p>Commercial sulfuric acid is manufactured and transported in standardized grades designated either by percentage weight or by the historical <strong>Baumé hydrometer scale (°Bé)</strong>:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Commercial Grade Designation</th>
              <th>Baumé Gravity (°Bé)</th>
              <th>H₂SO₄ Concentration (% w/w)</th>
              <th>Specific Gravity (at 15.5°C)</th>
              <th>Freezing Point (°C / °F)</th>
              <th>Viscosity (cP at 20°C)</th>
              <th>Primary Industrial Application</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>66° Baumé (Technical / Industrial)</td>
              <td>66.0 &deg;Bé</td>
              <td>93.19 &ndash; 93.50%</td>
              <td>1.835 kg/L</td>
              <td>&minus;35.0 &deg;C (&minus;31 &deg;F)</td>
              <td>23.5 cP</td>
              <td>Water treatment benchmark (does not freeze)</td>
            </tr>
            <tr>
              <td>Concentrated Technical Grade</td>
              <td>66.3 &deg;Bé</td>
              <td>98.00 &ndash; 98.50%</td>
              <td>1.840 kg/L</td>
              <td>+3.0 &deg;C (+37.4 &deg;F)</td>
              <td>27.0 cP</td>
              <td>Chemical synthesis, high-volume shipping</td>
            </tr>
            <tr>
              <td>60° Baumé (Glover Acid)</td>
              <td>60.0 &deg;Bé</td>
              <td>77.67%</td>
              <td>1.706 kg/L</td>
              <td>&minus;11.2 &deg;C (+11.8 &deg;F)</td>
              <td>14.0 cP</td>
              <td>Fertilizer acidulation, battery manufacturing</td>
            </tr>
            <tr>
              <td>Dilute Battery Grade</td>
              <td>35.0 &deg;Bé</td>
              <td>50.00%</td>
              <td>1.395 kg/L</td>
              <td>&minus;37.0 &deg;C (&minus;35 &deg;F)</td>
              <td>4.5 cP</td>
              <td>Small-scale automated metering, lower fuming</td>
            </tr>
          </tbody>
        </table>
      </div>

      <p>A crucial engineering decision in water plant design is choosing between <strong>93%</strong> and <strong>98%</strong> acid. While 98% sulfuric acid offers higher active payload per truckload, it displays an anomalously high freezing point of $+3.0^\circ\text{C}\ (37.4^\circ\text{F})$. In temperate and cold climates, 98% acid will solidify inside outdoor pipelines and unheated bulk storage tanks during winter nights. In contrast, 93.2% acid sits precisely within a eutectic freezing depression valley, remaining fully liquid down to $-35.0^\circ\text{C}\ (-31^\circ\text{F})$, eliminating the need for expensive electrical heat tracing.</p>

      <h2>Mathematical Sizing Formulas for Dosing Metering Skids</h2>
      <p>To convert active acid demand ($D_{\text{pure}}$) into commercial stock solution consumption, calculations must account for reagent concentration ($\%_{\text{active}}$) and specific gravity ($\text{SG}$):</p>

      <div class="formula-box">
        $$\dot{m}_{\text{comm}}\text{ (kg/day)} = \frac{Q\text{ (m}^3/\text{day)} \times D_{\text{pure}}\text{ (mg/L)}}{1,000 \times \left(\frac{\%_{\text{active}}}{100}\right)}$$
        $$\dot{m}_{\text{comm}}\text{ (lb/day)} = Q\text{ (MGD)} \times D_{\text{pure}}\text{ (ppm)} \times 8.3454 \times \frac{1}{\left(\frac{\%_{\text{active}}}{100}\right)}$$
      </div>

      <p>The volumetric feed rate delivered by the positive displacement metering pump ($q_{\text{pump}}$ in Liters per hour or Gallons per hour) is:</p>

      <div class="formula-box">
        $$q_{\text{pump}}\text{ (L/h)} = \frac{\dot{m}_{\text{comm}}\text{ (kg/day)}}{24\text{ h/day} \times \text{SG}\text{ (kg/L)}} = \frac{Q\text{ (m}^3/\text{h)} \times D_{\text{pure}}\text{ (g/m}^3)}{\left(\frac{\%_{\text{active}}}{100}\right) \times \text{SG} \times 1,000}$$
      </div>

      <h2>Sulfate Accumulation and Calcium Sulfate (Gypsum) Limits</h2>
      <p>A fundamental side-effect of sulfuric acid dosing is the introduction of sulfate anions ($\text{SO}_4^{2-}$). Every $1.0\text{ mg/L of 100% H}_2\text{SO}_4$ adds exactly:</p>

      <div class="formula-box">
        $$\Delta[\text{SO}_4^{2-}] = D_{\text{pure}} \times \left(\frac{\text{MW}(\text{SO}_4)}{\text{MW}(\text{H}_2\text{SO}_4)}\right) = D_{\text{pure}} \times \left(\frac{96.06}{98.08}\right) = 0.9794 \times D_{\text{pure}}\text{ (mg/L)}$$
      </div>

      <p>In waters with elevated natural calcium hardness, excessive sulfate accumulation can trigger the precipitation of <strong>calcium sulfate dihydrate (gypsum, $\text{CaSO}_4 \cdot 2\text{H}_2\text{O}$)</strong>:</p>

      <div class="formula-box">
        $$\text{Ca}^{2+} + \text{SO}_4^{2-} + 2\text{H}_2\text{O} \rightleftharpoons \text{CaSO}_4 \cdot 2\text{H}_2\text{O}\downarrow \quad (K_{sp} \approx 4.93 \times 10^{-5}\text{ at } 25^\circ\text{C})$$
      </div>
      <p>Unlike calcium carbonate, gypsum cannot be dissolved with acid cleaning. Once formed, it requires aggressive chelating agents (such as hot alkaline EDTA) or high-pressure mechanical hydro-blasting. Industrial guidelines mandate that the product of calcium (as $\text{Ca}^{2+}$ in $\text{mg/L}$) and sulfate (as $\text{SO}_4^{2-}$ in $\text{mg/L}$) must not exceed the gypsum threshold limit: $[\text{Ca}^{2+}] \times [\text{SO}_4^{2-}] &lt; 500,000\text{ (mg/L)}^2$. If this threshold is approached, hydrochloric acid ($\text{HCl}$) must be substituted for alkalinity trimming.</p>

      <h2>Practical Worked Case Study: Cooling Tower Alkalinity Neutralization</h2>
      <div class="worked-example-card">
        <h3>Industrial Water Treatment Case Study: 1,000 GPM Make-up Stream</h3>
        <p><strong>Scenario:</strong> A power plant cooling tower operates at $CoC = 4.0$ cycles of concentration. The raw make-up water flow rate is $Q = 1,000\text{ GPM}$ ($227.1\text{ m}^3/\text{h}$, equivalent to $1.44\text{ MGD}$). Raw make-up analysis shows a total alkalinity of $240.0\text{ mg/L as CaCO}_3$. To prevent calcium carbonate scaling while maintaining a mild protective Langelier Saturation Index ($LSI = +0.3$) in the recirculating basin, plant chemistry dictates reducing the make-up alkalinity down to $70.0\text{ mg/L as CaCO}_3$. Commercial $93.2\%\text{ w/w (66° Bé)}$ sulfuric acid ($\text{SG} = 1.835\text{ kg/L}$) is utilized. Sizing target: determine active acid dose, commercial mass flow rate, dosing pump volumetric feed rate, and verify pump stroke percentage on a $50.0\text{ L/h}$ diaphragm pump skid.</p>

        <p><strong>Step 1: Compute Alkalinity Reduction and Active Pure Acid Dose:</strong></p>
        $$\Delta\text{Alk} = 240.0\text{ mg/L} - 70.0\text{ mg/L} = 170.0\text{ mg/L as CaCO}_3\text{ reduced}$$
        $$D_{\text{pure}} = 170.0\text{ mg/L} \times 0.980 = 166.60\text{ mg/L pure 100% H}_2\text{SO}_4\ (166.6\text{ ppm})$$

        <p><strong>Step 2: Calculate Daily Pure Acid Delivery:</strong></p>
        $$\dot{m}_{\text{pure}} = 1.44\text{ MGD} \times 166.60\text{ ppm} \times 8.3454\text{ lb/(MGD}\cdot\text{ppm)} = 2,002.1\text{ lbs/day}\ (908.1\text{ kg/day})$$

        <p><strong>Step 3: Account for 93.2% Commercial Strength and Specific Gravity:</strong></p>
        $$\dot{m}_{\text{comm}} = \frac{908.1\text{ kg/day}}{0.932} = 974.36\text{ kg / day commercial 93.2% acid}\ (2,148.1\text{ lbs/day})$$
        $$\text{Daily Volume} = \frac{974.36\text{ kg/day}}{1.835\text{ kg/L}} = 531.0\text{ Liters / day}\ (140.3\text{ Gallons/day})$$

        <p><strong>Step 4: Metering Pump Delivery Rate and Stroke Setting:</strong></p>
        $$q_{\text{pump}} = \frac{531.0\text{ Liters}}{24\text{ hours}} = 22.125\text{ Liters / hour}\ (368.8\text{ mL/min} = 5.845\text{ GPH})$$
        $$\text{Stroke}\% = \left( \frac{22.125\text{ L/h}}{50.0\text{ L/h}} \right) \times 100\% = 44.25\%$$
        <p>Operating at $44.3\%$ stroke length is within the ideal linear metering band ($20\%\text{ to } 80\%$).</p>

        <p><strong>Step 5: Storage Tank Autonomy:</strong></p>
        <p>A standard $1,000\text{ Liter}$ intermediate bulk container (IBC tote) of 93% sulfuric acid provides:</p>
        $$\text{Autonomy} = \frac{1,000\text{ Liters}}{531.0\text{ Liters / day}} \approx 1.88\text{ Operating Days}$$
        <p><em>Engineering Recommendation:</em> Due to rapid turnover, the facility should install a permanent bulk carbon steel or lined storage tank rated for a minimum of $20,000\text{ Liters}$ (approx. 35 days autonomy).</p>
      </div>

      <h2>Materials of Construction and Safety Handling Protocols</h2>
      <p>Concentrated sulfuric acid exhibits unique corrosive behavior depending on water content:</p>
      <ul>
        <li><strong>Concentrated Acid (&gt;90% H₂SO₄):</strong> Concentrated acid acts as an oxidizing agent, passivating carbon steel by forming an insoluble iron sulfate ($\text{FeSO}_4$) protective barrier. Carbon steel tanks (with $1/4\text{ inch}$ corrosion allowance), Alloy 20, Hastelloy C-276, and PTFE/PVDF piping are standard. Velocity must be kept below $0.9\text{ m/s}\ (3\text{ ft/s})$ to prevent scouring the iron sulfate passivating film.</li>
        <li><strong>Dilute Acid (&lt;70% H₂SO₄):</strong> Once diluted, the protective iron sulfate layer dissolves and sulfuric acid aggressively attacks carbon steel. Wetted components must be fabricated from PVDF (Kynar), PTFE (Teflon), FRP (vinyl ester), or high-nickel alloys.</li>
        <li><strong>Exothermic Heat Release:</strong> Diluting sulfuric acid releases immense thermal energy ($\Delta H_{\text{dilution}} = -74.7\text{ kJ/mol}$). In-line chemical injection quills must project into the turbulent center third of the pipe ($v &gt; 1.5\text{ m/s}$) fabricated from Hastelloy C-276 to prevent local boiling and thermal stress cracking.</li>
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
          <p class="footer-about">High-precision chemical neutralization, sulfuric acid stoichiometry, and cooling water alkalinity control engineering tools conforming to AWWA and CTI standards.</p>
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
            <li><a href="https://www.cti.org" target="_blank" rel="noopener">Cooling Technology Institute (CTI) Guidelines</a></li>
            <li><a href="https://www.awwa.org" target="_blank" rel="noopener">AWWA Standard B511 Sulfuric Acid</a></li>
            <li><a href="https://www.osha.gov" target="_blank" rel="noopener">OSHA Chemical Safety Standard 1910.119</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    const ACID_GRADES = {
      "93": { strength: 93.2, sg: 1.835 },
      "98": { strength: 98.0, sg: 1.840 },
      "77": { strength: 77.7, sg: 1.706 },
      "50": { strength: 50.0, sg: 1.395 },
      "custom": { strength: 93.2, sg: 1.835 }
    };

    function updateApplicationPreset() {
      const app = document.getElementById("treatmentApplication").value;
      if (app === "alkalinity_trim") {
        document.getElementById("alkalinityInputsGroup").style.display = "grid";
        document.getElementById("directDoseGroup").style.display = "none";
        document.getElementById("initialAlkVal").value = 220;
        document.getElementById("targetAlkVal").value = 80;
      } else if (app === "wastewater_neut") {
        document.getElementById("alkalinityInputsGroup").style.display = "grid";
        document.getElementById("directDoseGroup").style.display = "none";
        document.getElementById("initialAlkVal").value = 450;
        document.getElementById("targetAlkVal").value = 50;
      } else if (app === "ro_pretreat") {
        document.getElementById("alkalinityInputsGroup").style.display = "grid";
        document.getElementById("directDoseGroup").style.display = "none";
        document.getElementById("initialAlkVal").value = 180;
        document.getElementById("targetAlkVal").value = 40;
      } else if (app === "direct_dose") {
        document.getElementById("alkalinityInputsGroup").style.display = "none";
        document.getElementById("directDoseGroup").style.display = "block";
      }
      calcSulfuricAcid();
    }

    function updateGradeProps() {
      const g = document.getElementById("acidCommercialGrade").value;
      if (g !== "custom") {
        const item = ACID_GRADES[g];
        document.getElementById("acidStrengthPct").value = item.strength;
        document.getElementById("acidSGVal").value = item.sg;
      }
      calcSulfuricAcid();
    }

    function calcSulfuricAcid() {
      const flowVal = parseFloat(document.getElementById("waterFlowVal").value) || 0;
      const flowUnit = document.getElementById("waterFlowUnit").value;
      const app = document.getElementById("treatmentApplication").value;
      const strengthPct = parseFloat(document.getElementById("acidStrengthPct").value) || 93.2;
      const sg = parseFloat(document.getElementById("acidSGVal").value) || 1.835;
      const maxPumpLph = parseFloat(document.getElementById("dosingPumpMaxCapacityLph").value) || 50.0;

      // Flow conversion to m3/day and m3/h
      let m3_per_day = 0;
      let m3_per_hour = 0;
      if (flowUnit === "gpm") {
        m3_per_hour = flowVal * 0.227125;
        m3_per_day = m3_per_hour * 24.0;
      } else if (flowUnit === "m3h") {
        m3_per_hour = flowVal;
        m3_per_day = flowVal * 24.0;
      } else if (flowUnit === "mgd") {
        m3_per_day = flowVal * 3785.41;
        m3_per_hour = m3_per_day / 24.0;
      } else if (flowUnit === "lps") {
        m3_per_hour = flowVal * 3.6;
        m3_per_day = m3_per_hour * 24.0;
      } else if (flowUnit === "mld") {
        m3_per_day = flowVal * 1000.0;
        m3_per_hour = m3_per_day / 24.0;
      }

      // Calculate pure active H2SO4 dose
      let pureDoseMgL = 50.0;
      let alkDestroyed = 0;

      if (app === "direct_dose") {
        pureDoseMgL = parseFloat(document.getElementById("directAcidDosePpm").value) || 50.0;
        alkDestroyed = pureDoseMgL / 0.980;
      } else {
        const initAlk = parseFloat(document.getElementById("initialAlkVal").value) || 0;
        const targetAlk = parseFloat(document.getElementById("targetAlkVal").value) || 0;
        alkDestroyed = Math.max(0, initAlk - targetAlk);
        pureDoseMgL = alkDestroyed * 0.980; // 0.980 mg H2SO4 per mg CaCO3
      }

      // Mass rates
      const pureKgPerDay = (m3_per_day * pureDoseMgL) / 1000.0;
      const pureKgPerHour = pureKgPerDay / 24.0;

      const commKgPerDay = pureKgPerDay / (strengthPct / 100.0);
      const commLbsPerDay = commKgPerDay * 2.20462;

      const commLitersPerDay = commKgPerDay / sg;
      const commLitersPerHour = commLitersPerDay / 24.0;
      const commMlPerMin = (commLitersPerHour * 1000.0) / 60.0;
      const commGph = commLitersPerHour * 0.264172;

      // Pump stroke
      const strokePct = (commLitersPerHour / maxPumpLph) * 100.0;

      // Sulfate addition: 96.06 / 98.08 = 0.9794
      const deltaSulfateMgL = pureDoseMgL * 0.9794;

      // Heat of dilution approx 74.7 kJ/mol H2SO4
      // mol/s = (pureKgPerHour / 3600) * 1000 / 98.08
      const molesPerSec = (pureKgPerHour * 1000.0) / (3600.0 * 98.08);
      const heatKw = molesPerSec * 74.7;

      // Autonomy
      const toteDays = commLitersPerDay > 0 ? (1000.0 / commLitersPerDay).toFixed(1) : "N/A";
      const drumDays = commLitersPerDay > 0 ? (200.0 / commLitersPerDay).toFixed(1) : "N/A";

      // Render Outputs
      document.getElementById("resPumpLphVal").textContent = commLitersPerHour.toFixed(2) + " L / hour";
      document.getElementById("resPumpAlternateUnits").textContent = commMlPerMin.toFixed(1) + " mL/min (" + commGph.toFixed(2) + " GPH commercial " + strengthPct + "% acid)";

      document.getElementById("resPureAcidDose").textContent = pureDoseMgL.toFixed(1) + " mg/L";
      document.getElementById("resPureAcidDoseSub").textContent = "Neutralizes " + alkDestroyed.toFixed(1) + " mg/L Alkalinity as CaCO₃";

      document.getElementById("resDailyCommercialKg").textContent = commKgPerDay.toLocaleString(undefined, {maximumFractionDigits: 1}) + " kg / day";
      document.getElementById("resDailyCommercialLbs").textContent = commLbsPerDay.toLocaleString(undefined, {maximumFractionDigits: 1}) + " lbs / day commercial acid";

      document.getElementById("resDailyCommercialLiters").textContent = commLitersPerDay.toFixed(1) + " L / day";

      document.getElementById("resPumpStrokeSetting").textContent = strokePct.toFixed(1) + "%";

      document.getElementById("resSulfateIncrease").textContent = "+" + deltaSulfateMgL.toFixed(1) + " mg/L";
      document.getElementById("resExothermicHeat").textContent = heatKw.toFixed(1) + " kW";

      document.getElementById("resStorageAutonomy").textContent = "Standard 1,000 L IBC Tote lasts " + toteDays + " Days | 200 L Drum lasts " + drumDays + " Days.";

      let gypMsg = "Sulfate increase is within safe limits for non-scaling calcium sulfate operation.";
      if (deltaSulfateMgL > 250) {
        gypMsg = "Caution: Sulfate increase (" + deltaSulfateMgL.toFixed(0) + " mg/L) is substantial. Verify [Ca²⁺] × [SO₄²⁻] < 500,000 to prevent gypsum precipitation.";
      }
      document.getElementById("resGypsumWarning").textContent = gypMsg;
    }

    window.addEventListener("DOMContentLoaded", () => {
      calcSulfuricAcid();
    });
  </script>
</body>
</html>
"""

TOOL_2_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Titration Calculator | Acid-Base Equivalence &amp; Molarity Solver</title>
  <meta name="description" content="Calculate unknown analyte concentration, equivalence point volume, normality, titration curves, and indicator selection for acid-base and redox titrations.">
  <link rel="canonical" href="https://calchub.cloud/titration-calculator.html">
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
        "name": "Titration Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates volumetric analytical titration stoichiometry, unknown analyte concentration and mass, equivalence point burette volumes, and color indicator selection.",
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
            "name": "What is the primary equation for volumetric titration?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "At the stoichiometric equivalence point, the moles of reactive equivalents of titrant equal the equivalents of analyte: N1 * V1 = N2 * V2, or in terms of molarity: M_titrant * V_titrant * z_titrant = M_analyte * V_analyte * z_analyte, where z represents the valence or stoichiometric factor (protons H+ donated/accepted or electrons transferred)."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between the equivalence point and the end point?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The equivalence point is the exact theoretical stoichiometric state where moles of titrant added chemically equal moles of analyte. The end point is the experimentally observed physical event (such as a color change from phenolphthalein or an electrometric potential jump) where the titrator stops adding reagent. Proper indicator selection minimizes the titration error between end point and equivalence point."
            }
          },
          {
            "@type": "Question",
            "name": "Why is the equivalence point pH not always 7.0 in acid-base titrations?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "While titrating a strong acid with a strong base produces neutral salt and water with pH = 7.00 at 25°C, titrating a weak acid (e.g., acetic acid) with a strong base (NaOH) produces a conjugate base (acetate CH3COO-) that hydrolyzes water, causing the equivalence point to be alkaline (pH 8.5 to 9.2). Conversely, titrating a weak base with a strong acid results in an acidic equivalence point (pH 4.5 to 5.5)."
            }
          },
          {
            "@type": "Question",
            "name": "How does burette reading precision affect titration accuracy?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A standard 50 mL Class A analytical burette has graduation marks of 0.1 mL and can be interpolated to ±0.02 mL. Delivering an equivalence volume greater than 20 mL ensures the volumetric measurement uncertainty remains below ±0.1%, conforming to ISO/IEC 17025 testing standards."
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
      <span>Titration Calculator</span>
    </nav>

    <h1 class="tool-title">Analytical Titration &amp; Molarity Calculator</h1>
    <p class="tool-subtitle">Equivalence Point Stoichiometry, Normality (N₁V₁ = N₂V₂), Analyte Mass &amp; Indicator Sizer</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="titrationPreset">Titration Chemistry Preset</label>
            <select id="titrationPreset" class="form-control" onchange="updateTitrationPreset()">
              <option value="sa_sb" selected>Strong Acid (HCl) vs. Strong Base (NaOH)</option>
              <option value="wa_sb">Weak Acid (Acetic Acid) vs. Strong Base (NaOH)</option>
              <option value="sb_sa_di">Diprotic Acid (H₂SO₄) vs. Strong Base (NaOH)</option>
              <option value="khp_naoh">Primary Standard KHP vs. NaOH Standardization</option>
              <option value="redox_kmno4">Redox Titration: KMnO₄ (z=5) vs. Fe²⁺ (z=1)</option>
              <option value="edta_hardness">Complexometric: EDTA vs. Total Water Hardness (Ca²⁺)</option>
              <option value="custom">Custom Titrant &amp; Analyte Entry</option>
            </select>
          </div>

          <div class="form-group">
            <label for="titrationSolveTarget">Variable to Solve For</label>
            <select id="titrationSolveTarget" class="form-control" onchange="updateTitrationInputs()">
              <option value="analyte_conc" selected>Analyte Concentration (M &amp; N) [Given Titrant Volume]</option>
              <option value="titrant_vol">Required Titrant Volume (Vₜ) [Given Analyte Molarity]</option>
            </select>
          </div>

          <!-- Titrant Parameters -->
          <div style="background: #F8FAFC; padding: 12px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #E2E8F0;">
            <h4 style="font-size: 0.95rem; font-weight: 700; margin-bottom: 10px; color: var(--primary);">Standard Titrant in Burette</h4>
            <div class="grid-2-col">
              <div class="form-group">
                <label for="titrantMolarityVal">Titrant Molarity (Mₜ)</label>
                <input type="number" id="titrantMolarityVal" class="form-control" value="0.1000" step="0.005" min="0.0001">
                <span class="field-hint">Known standard mol/L</span>
              </div>
              <div class="form-group">
                <label for="titrantValenceZ">Titrant Valence (zₜ)</label>
                <input type="number" id="titrantValenceZ" class="form-control" value="1" step="1" min="1" max="6">
                <span class="field-hint">e.g., 1 for NaOH/HCl, 5 for KMnO₄</span>
              </div>
            </div>
            <div id="titrantVolGroup" class="form-group">
              <label for="titrantVolumeMl">Delivered Burette Volume (Vₜ) (mL)</label>
              <input type="number" id="titrantVolumeMl" class="form-control" value="24.35" step="0.05" min="0.01">
              <span class="field-hint">Final burette reading minus initial</span>
            </div>
          </div>

          <!-- Analyte Parameters -->
          <div style="background: #F8FAFC; padding: 12px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #E2E8F0;">
            <h4 style="font-size: 0.95rem; font-weight: 700; margin-bottom: 10px; color: var(--text-main);">Unknown Analyte in Flask</h4>
            <div class="grid-2-col">
              <div class="form-group">
                <label for="analyteVolumeMl">Analyte Aliquot Volume (Vₐ) (mL)</label>
                <input type="number" id="analyteVolumeMl" class="form-control" value="25.00" step="1.0" min="0.1">
                <span class="field-hint">Pipetted sample volume</span>
              </div>
              <div class="form-group">
                <label for="analyteValenceZ">Analyte Valence (zₐ)</label>
                <input type="number" id="analyteValenceZ" class="form-control" value="1" step="1" min="1" max="6">
                <span class="field-hint">Reactive protons/electrons per mole</span>
              </div>
            </div>
            <div id="analyteConcInputGroup" class="form-group" style="display: none;">
              <label for="analyteMolarityInputVal">Analyte Known Molarity (Mₐ)</label>
              <input type="number" id="analyteMolarityInputVal" class="form-control" value="0.0974" step="0.005" min="0.0001">
            </div>
            <div class="form-group">
              <label for="analyteMolarMassVal">Analyte Molar Mass (MW) (g/mol)</label>
              <input type="number" id="analyteMolarMassVal" class="form-control" value="36.46" step="0.01" min="1.0">
              <span class="field-hint">For gravimetric mass determination</span>
            </div>
          </div>

          <button type="button" class="btn btn-primary" onclick="calcTitration()" style="width: 100%; margin-top: 10px;">Solve Titration Stoichiometry</button>
        </div>
      </div>

      <!-- Output Results Panel -->
      <div class="results-card">
        <div class="result-box primary-result">
          <div id="resPrimaryTitrationLabel" class="result-label">Calculated Analyte Concentration</div>
          <div id="resPrimaryTitrationVal" class="result-value">0.09740 M</div>
          <div id="resPrimaryTitrationAlt" class="result-subtext">Normality = 0.09740 N | 3.551 g/L active analyte</div>
        </div>

        <div class="result-grid">
          <div class="result-item">
            <span class="result-label">Analyte Aliquot Mass</span>
            <span id="resAnalyteSampleMass" class="result-value highlight">88.78 mg</span>
            <span id="resAnalyteSampleMassSub" class="result-subtext">In 25.00 mL sample flask</span>
          </div>
          <div class="result-item">
            <span class="result-label">Equivalence Titrant Volume</span>
            <span id="resEquivalenceVolume" class="result-value">24.35 mL</span>
            <span class="result-subtext">Burette delivery volume</span>
          </div>
          <div class="result-item">
            <span class="result-label">Substance Quantity</span>
            <span id="resTotalMolesAnalyte" class="result-value">2.435 mmol</span>
            <span class="result-subtext">0.002435 moles in flask</span>
          </div>
          <div class="result-item">
            <span class="result-label">Equivalence Point pH</span>
            <span id="resEquilPH" class="result-value">pH 7.00</span>
            <span class="result-subtext">Neutral salt formed</span>
          </div>
          <div class="result-item">
            <span class="result-label">Recommended Indicator</span>
            <span id="resRecIndicator" class="result-value">Bromothymol Blue</span>
            <span id="resRecIndicatorRange" class="result-subtext">Transition pH 6.0 &ndash; 7.6</span>
          </div>
          <div class="result-item">
            <span class="result-label">Titration Precision</span>
            <span id="resTitrationError" class="result-value">&plusmn;0.08% Error</span>
            <span class="result-subtext">Class A burette &plusmn;0.02 mL</span>
          </div>
        </div>

        <div class="result-details" style="margin-top: 15px;">
          <p><strong>Stoichiometric Reaction Ratio:</strong> <span id="resReactionRatio">1 mole Titrant reacts with 1 mole Analyte (1:1 stoichiometry).</span></p>
          <p><strong>Color Transition End-Point:</strong> <span id="resColorTransition">Yellow (acid) &rarr; Emerald Green &rarr; Blue (basic) at equivalence.</span></p>
        </div>
      </div>
    </div>

    <!-- 1000+ Words Engineering Body -->
    <article class="article-body">
      <h2>Foundations of Quantitative Volumetric Titrimetry</h2>
      <p><strong>Titration</strong> (also termed <em>volumetric analysis</em> or <em>titrimetry</em>) represents one of the oldest, most accurate, and foundational analytical methodologies in chemical metrology, pharmaceutical quality assurance, and environmental water testing. Originating in late 18th-century France through the pioneering work of François-Antoine-Henri Descroizilles and Joseph Louis Gay-Lussac, titrimetry determines the unknown concentration of an identified chemical substance (the <strong>analyte</strong>) by quantitatively reacting it with a measured volume of a standardized reagent solution of known concentration (the <strong>titrant</strong>).</p>

      <p>Unlike instrumental spectroscopic techniques that rely on empirical calibration curves, volumetric titration is a <strong>primary ratio method</strong> grounded directly in the fundamental laws of chemical stoichiometry. When executed with calibrated Class A volumetric glassware (transfer pipettes and analytical burettes), titration routinely delivers measurement uncertainties below $\pm 0.1\%$, making it the definitive referee technique for standardizing secondary working solutions and validating automated online chemical analyzers.</p>

      <h2>The Principle of Chemical Equivalents (N₁V₁ = N₂V₂)</h2>
      <p>At the center of volumetric analysis lies the concept of <strong>chemical equivalence</strong>. The reaction reaches its theoretical completion at the <strong>stoichiometric equivalence point</strong>, where the number of reactive equivalents of titrant added from the burette exactly equals the number of equivalents of analyte initially present in the titration vessel:</p>

      <div class="formula-box">
        $$\text{Equivalents of Titrant} = \text{Equivalents of Analyte}$$
        $$N_{\text{titrant}} \times V_{\text{titrant}} = N_{\text{analyte}} \times V_{\text{analyte}}$$
      </div>

      <p>Where $N$ represents normality (equivalents per liter, $\text{eq/L}$) and $V$ is liquid volume. Because normality is related to molar concentration ($M$ in $\text{mol/L}$) by the equivalence factor $z$ ($N = M \cdot z$):</p>

      <div class="formula-box">
        $$M_{\text{titrant}} \cdot V_{\text{titrant}} \cdot z_{\text{titrant}} = M_{\text{analyte}} \cdot V_{\text{analyte}} \cdot z_{\text{analyte}}$$
      </div>

      <p>Where $z$ denotes the stoichiometric valence factor:</p>
      <ul>
        <li><strong>In Acid-Base Neutralization:</strong> $z$ is the number of reactive hydronium ions ($\text{H}^+$) donated or accepted per molecule. For hydrochloric acid ($\text{HCl}$) and sodium hydroxide ($\text{NaOH}$), $z = 1$. For diprotic sulfuric acid ($\text{H}_2\text{SO}_4$) or oxalic acid ($\text{H}_2\text{C}_2\text{O}_4$), $z = 2$. For triprotic citric acid ($\text{H}_3\text{C}_6\text{H}_5\text{O}_7$), $z = 3$.</li>
        <li><strong>In Oxidation-Reduction (Redox):</strong> $z$ is the integer number of electrons transferred per formula unit in the half-reaction. In permanganate redox titrations in acidic media ($\text{MnO}_4^- + 8\text{H}^+ + 5\text{e}^- \to \text{Mn}^{2+} + 4\text{H}_2\text{O}$), $z_{\text{KMnO}_4} = 5$, reacting with ferrous iron ($\text{Fe}^{2+} \to \text{Fe}^{3+} + \text{e}^-$, where $z_{\text{Fe}} = 1$).</li>
        <li><strong>In Complexometric Titrations:</strong> In standard water hardness determination using ethylenediaminetetraacetic acid (EDTA), disodium EDTA forms a $1:1$ hexadentate chelate complex with divalent metal cations ($\text{Ca}^{2+} + \text{EDTA}^{4-} \to [\text{Ca-EDTA}]^{2-}$), establishing an effective $z = 1$ stoichiometry for both species.</li>
      </ul>

      <h2>Analytical Inversion Formulas for Analyte Properties</h2>
      <p>Rearranging the equivalence relation allows direct calculation of the target analytical metrics:</p>

      <h3>1. Unknown Analyte Molar Concentration (M_analyte)</h3>
      <div class="formula-box">
        $$M_{\text{analyte}} = \frac{M_{\text{titrant}} \times V_{\text{titrant}} \times z_{\text{titrant}}}{V_{\text{analyte}} \times z_{\text{analyte}}}$$
      </div>

      <h3>2. Unknown Analyte Mass in Aliquot (m_analyte)</h3>
      <p>Multiplying the calculated moles by the molecular weight ($M_w$ in $\text{g/mol}$) gives the absolute gravimetric mass of pure substance contained within the pipetted sample volume:</p>
      <div class="formula-box">
        $$m_{\text{analyte}}\text{ (grams)} = M_{\text{analyte}}\text{ (mol/L)} \times V_{\text{analyte}}\text{ (L)} \times M_w\text{ (g/mol)}$$
        $$m_{\text{analyte}}\text{ (mg)} = M_{\text{analyte}} \times V_{\text{analyte}}\text{ (mL)} \times M_w$$
      </div>

      <h3>3. Mass Concentration in Original Sample</h3>
      <div class="formula-box">
        $$C_{\text{mass}}\text{ (g/L)} = M_{\text{analyte}}\text{ (mol/L)} \times M_w\text{ (g/mol)}$$
      </div>

      <h2>Equivalence Point vs. End Point and Titration Curves</h2>
      <p>A critical distinction in analytical chemistry is the divergence between the theoretical <strong>equivalence point</strong> and the experimental <strong>end point</strong>:</p>
      <ul>
        <li><strong>Equivalence Point:</strong> The exact thermodynamic point where stoichiometric chemical parity is achieved. It is fixed strictly by chemistry.</li>
        <li><strong>End Point:</strong> The physical detection event where the human operator or automated photometric titrator halts the burette (e.g., visual color transition of a dye, inflection point of a potentiometric pH curve, or permanent faint pink tint of excess $\text{MnO}_4^-$).</li>
      </ul>

      <p>The mathematical difference between the end point volume and the true equivalence volume represents the <strong>titration error</strong>. To minimize titration error, the color change interval of the visual indicator must align precisely with the steep vertical inflection zone of the titration curve:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Titration System</th>
              <th>Equivalence Point pH</th>
              <th>Chemical Cause of Equivalence pH</th>
              <th>Steep Inflection Range</th>
              <th>Recommended Visual Indicator</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Strong Acid vs. Strong Base (e.g., HCl + NaOH)</td>
              <td>pH = 7.00 (at 25°C)</td>
              <td>Neutral spectator ions (Na⁺, Cl⁻)</td>
              <td>pH 4.0 &ndash; 10.0</td>
              <td>Bromothymol Blue (6.0&ndash;7.6) or Phenolphthalein</td>
            </tr>
            <tr>
              <td>Weak Acid vs. Strong Base (e.g., Acetic + NaOH)</td>
              <td>pH = 8.5 &ndash; 9.2</td>
              <td>Conjugate base hydrolysis (CH₃COO⁻ + H₂O &rightleftharpoons; CH₃COOH + OH⁻)</td>
              <td>pH 7.0 &ndash; 10.5</td>
              <td>Phenolphthalein (8.2&ndash;10.0) or Thymol Blue</td>
            </tr>
            <tr>
              <td>Strong Acid vs. Weak Base (e.g., HCl + NH₃)</td>
              <td>pH = 4.8 &ndash; 5.5</td>
              <td>Conjugate acid hydrolysis (NH₄⁺ + H₂O &rightleftharpoons; NH₃ + H₃O⁺)</td>
              <td>pH 3.5 &ndash; 6.5</td>
              <td>Methyl Red (4.4&ndash;6.2) or Methyl Orange</td>
            </tr>
            <tr>
              <td>Weak Acid vs. Weak Base (e.g., Acetic + NH₃)</td>
              <td>Variable (near 7)</td>
              <td>Both ions hydrolyze; very gentle slope</td>
              <td>No sharp inflection</td>
              <td>Not recommended for visual titration (use pH meter)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Standard Visual Indicators Reference Table</h2>
      <p>The table below summarizes standard analytical pH indicators, their transition intervals, and color transformations per <strong>ASTM E200 Standard Practice for Preparation, Standardization, and Storage of Standard and Reagent Solutions</strong>:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Indicator Name</th>
              <th>Acid Form Color</th>
              <th>Transition Interval (pH)</th>
              <th>Base Form Color</th>
              <th>pKa Value</th>
              <th>Typical Analytical Application</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Thymol Blue (Acid Range)</td>
              <td>Red</td>
              <td>1.2 &ndash; 2.8</td>
              <td>Yellow</td>
              <td>1.65</td>
              <td>Extremely strong acid titrations</td>
            </tr>
            <tr>
              <td>Methyl Orange</td>
              <td>Red</td>
              <td>3.1 &ndash; 4.4</td>
              <td>Orange-Yellow</td>
              <td>3.47</td>
              <td>Total alkalinity ($M$-alkalinity), weak base titrations</td>
            </tr>
            <tr>
              <td>Bromocresol Green</td>
              <td>Yellow</td>
              <td>3.8 &ndash; 5.4</td>
              <td>Blue</td>
              <td>4.68</td>
              <td>Ammonia Kjeldahl nitrogen determination</td>
            </tr>
            <tr>
              <td>Methyl Red</td>
              <td>Red</td>
              <td>4.4 &ndash; 6.2</td>
              <td>Yellow</td>
              <td>4.95</td>
              <td>Mineral acid standardization against sodium carbonate</td>
            </tr>
            <tr>
              <td>Bromothymol Blue</td>
              <td>Yellow</td>
              <td>6.0 &ndash; 7.6</td>
              <td>Blue</td>
              <td>7.10</td>
              <td>Strong acid &ndash; strong base neutral titrations</td>
            </tr>
            <tr>
              <td>Phenol Red</td>
              <td>Yellow</td>
              <td>6.8 &ndash; 8.4</td>
              <td>Red-Violet</td>
              <td>7.90</td>
              <td>Swimming pool water testing, biological assays</td>
            </tr>
            <tr>
              <td>Phenolphthalein</td>
              <td>Colorless</td>
              <td>8.2 &ndash; 10.0</td>
              <td>Deep Magenta-Pink</td>
              <td>9.40</td>
              <td>Phenolphthalein alkalinity ($P$-alk), organic acids</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Practical Worked Case Study: Primary Standardization of 0.1 M NaOH with KHP</h2>
      <div class="worked-example-card">
        <h3>Quality Assurance Analytical Case Study: Primary Reagent Standardization</h3>
        <p><strong>Scenario:</strong> Sodium hydroxide ($\text{NaOH}$) pellets cannot serve as a primary analytical standard because dry $\text{NaOH}$ is deliquescent and absorbs atmospheric carbon dioxide to form sodium carbonate ($\text{Na}_2\text{CO}_3$). To determine its exact analytical molarity, a chemist standardizes a newly formulated nominal $0.1\text{ M NaOH}$ solution against high-purity potassium hydrogen phthalate ($\text{KHP}$, chemical formula $\text{KHC}_8\text{H}_4\text{O}_4$, $\text{MW} = 204.2212\text{ g/mol}$, $100.0\%\text{ primary standard grade}$). The chemist accurately weighs $m_{\text{KHP}} = 0.5106\text{ grams}$ on a calibrated 5-place analytical balance and dissolves it into $V_{\text{water}} = 50.0\text{ mL}$ of carbon-dioxide-free deionized water with 3 drops of phenolphthalein indicator. Titration to a permanent faint pink persistence ($30\text{ seconds}$) requires $V_{\text{NaOH}} = 24.85\text{ mL}$ delivered from a Class A burette. Calculate: (1) moles of KHP neutralized, (2) exact molarity of the $\text{NaOH}$ titrant, (3) titrant normality, and (4) estimate the burette volumetric reading uncertainty.</p>

        <p><strong>Step 1: Calculate Substance Quantity of Primary Standard KHP:</strong></p>
        <p>KHP is a monoprotic acid ($z = 1$):</p>
        $$\text{KHC}_8\text{H}_4\text{O}_4 + \text{NaOH} \longrightarrow \text{KNaC}_8\text{H}_4\text{O}_4 + \text{H}_2\text{O}$$
        $$n_{\text{KHP}} = \frac{m_{\text{KHP}}}{M_w} = \frac{0.5106\text{ g}}{204.2212\text{ g/mol}} = 2.50023 \times 10^{-3}\text{ moles}\ (2.50023\text{ mmol})$$

        <p><strong>Step 2: Determine Exact Molarity of Sodium Hydroxide:</strong></p>
        <p>Because the stoichiometric reaction ratio is $1:1$ ($z_{\text{NaOH}} = 1, z_{\text{KHP}} = 1$):</p>
        $$n_{\text{NaOH}} = n_{\text{KHP}} = 2.50023 \times 10^{-3}\text{ moles}$$
        $$M_{\text{NaOH}} = \frac{n_{\text{NaOH}}}{V_{\text{NaOH}}\text{ (L)}} = \frac{2.50023 \times 10^{-3}\text{ mol}}{0.02485\text{ L}} = 0.100613\text{ mol/L}$$
        $$\text{Standardized Concentration: } M = 0.1006\text{ M (mol/L)}, \quad N = 0.1006\text{ N}$$

        <p><strong>Step 3: Uncertainty Analysis (Class A Burette):</strong></p>
        <p>A $50\text{ mL}$ Class A burette possesses a tolerance of $\pm 0.05\text{ mL}$ (with interpolation repeatability $\pm 0.02\text{ mL}$). The relative volumetric uncertainty is:</p>
        $$\text{Relative Uncertainty} = \frac{\pm 0.02\text{ mL}}{24.85\text{ mL}} \times 100\% = \pm 0.080\%$$
        <p>Because the delivered volume ($24.85\text{ mL}$) exceeds half-scale capacity ($&gt;20\text{ mL}$), volumetric error is constrained well below $0.1\%$, proving the reliability of the standardized concentration.</p>
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
          <p class="footer-about">High-precision analytical chemistry, volumetric titration stoichiometry, and equivalence point calculation tools conforming to IUPAC, ASTM, and ISO 17025 standards.</p>
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
            <li><a href="https://www.iupac.org" target="_blank" rel="noopener">IUPAC Analytical Chemistry Compendium</a></li>
            <li><a href="https://www.astm.org" target="_blank" rel="noopener">ASTM E200 Standard Titrimetric Practice</a></li>
            <li><a href="https://www.iso.org" target="_blank" rel="noopener">ISO/IEC 17025 Testing &amp; Calibration</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    const TITRATION_PRESETS = {
      sa_sb: { tM: 0.1000, tZ: 1, aZ: 1, aMw: 36.46, eqPH: "pH 7.00", ind: "Bromothymol Blue", indRange: "pH 6.0 - 7.6", indTrans: "Yellow (acid) → Green → Blue (base)" },
      wa_sb: { tM: 0.1000, tZ: 1, aZ: 1, aMw: 60.05, eqPH: "pH 8.72", ind: "Phenolphthalein", indRange: "pH 8.2 - 10.0", indTrans: "Colorless (acid) → Faint Pink (endpoint)" },
      sb_sa_di: { tM: 0.1000, tZ: 1, aZ: 2, aMw: 98.08, eqPH: "pH 7.00", ind: "Bromothymol Blue", indRange: "pH 6.0 - 7.6", indTrans: "Yellow → Green → Blue" },
      khp_naoh: { tM: 0.1000, tZ: 1, aZ: 1, aMw: 204.22, eqPH: "pH 8.90", ind: "Phenolphthalein", indRange: "pH 8.2 - 10.0", indTrans: "Colorless → Permanent Faint Pink" },
      redox_kmno4: { tM: 0.0200, tZ: 5, aZ: 1, aMw: 55.85, eqPH: "Redox Equiv", ind: "Self-Indicating (KMnO₄)", indRange: "Colorless → Faint Purple", indTrans: "First persistent pink drop" },
      edta_hardness: { tM: 0.0100, tZ: 1, aZ: 1, aMw: 100.09, eqPH: "pH 10.0 buffer", ind: "Eriochrome Black T (EBT)", indRange: "pH 9.0 - 11.0", indTrans: "Wine Red (Ca-EBT) → Sky Blue (free EBT)" },
      custom: { tM: 0.1000, tZ: 1, aZ: 1, aMw: 36.46, eqPH: "Variable", ind: "Bromothymol Blue", indRange: "pH 6.0 - 7.6", indTrans: "Visual color transition" }
    };

    function updateTitrationPreset() {
      const p = document.getElementById("titrationPreset").value;
      if (p !== "custom") {
        const item = TITRATION_PRESETS[p];
        document.getElementById("titrantMolarityVal").value = item.tM;
        document.getElementById("titrantValenceZ").value = item.tZ;
        document.getElementById("analyteValenceZ").value = item.aZ;
        document.getElementById("analyteMolarMassVal").value = item.aMw;
      }
      calcTitration();
    }

    function updateTitrationInputs() {
      const target = document.getElementById("titrationSolveTarget").value;
      document.getElementById("titrantVolGroup").style.display = target === "analyte_conc" ? "block" : "none";
      document.getElementById("analyteConcInputGroup").style.display = target === "titrant_vol" ? "block" : "none";
      calcTitration();
    }

    function calcTitration() {
      const target = document.getElementById("titrationSolveTarget").value;
      const tM = parseFloat(document.getElementById("titrantMolarityVal").value) || 0.1;
      const tZ = parseFloat(document.getElementById("titrantValenceZ").value) || 1;
      const aV = parseFloat(document.getElementById("analyteVolumeMl").value) || 25.0;
      const aZ = parseFloat(document.getElementById("analyteValenceZ").value) || 1;
      const aMw = parseFloat(document.getElementById("analyteMolarMassVal").value) || 36.46;

      const presetKey = document.getElementById("titrationPreset").value;
      const preset = TITRATION_PRESETS[presetKey] || TITRATION_PRESETS.sa_sb;

      let aM = 0;
      let tV = 0;

      if (target === "analyte_conc") {
        tV = parseFloat(document.getElementById("titrantVolumeMl").value) || 24.35;
        // M_a * V_a * z_a = M_t * V_t * z_t
        aM = (tM * tV * tZ) / (aV * aZ);
      } else {
        aM = parseFloat(document.getElementById("analyteMolarityInputVal").value) || 0.1;
        // V_t = (M_a * V_a * z_a) / (M_t * z_t)
        tV = (aM * aV * aZ) / (tM * tZ);
      }

      const aN = aM * aZ;
      const totalMoles = aM * (aV / 1000.0);
      const sampleMassGrams = totalMoles * aMw;
      const massConcGL = aM * aMw;

      const relError = tV > 0 ? (0.02 / tV) * 100.0 : 0.1;

      // Update UI
      if (target === "analyte_conc") {
        document.getElementById("resPrimaryTitrationLabel").textContent = "Calculated Analyte Concentration";
        document.getElementById("resPrimaryTitrationVal").textContent = aM < 0.001 ? aM.toExponential(4) + " M" : aM.toFixed(5) + " M";
        document.getElementById("resPrimaryTitrationAlt").textContent = "Normality = " + aN.toFixed(5) + " N | " + massConcGL.toFixed(3) + " g/L (" + (massConcGL * 1000).toLocaleString(undefined, {maximumFractionDigits: 0}) + " ppm)";
      } else {
        document.getElementById("resPrimaryTitrationLabel").textContent = "Required Titrant Equivalence Volume";
        document.getElementById("resPrimaryTitrationVal").textContent = tV.toFixed(2) + " mL";
        document.getElementById("resPrimaryTitrationAlt").textContent = "Burette delivery volume for " + aV.toFixed(1) + " mL of " + aM.toFixed(4) + " M analyte";
      }

      if (sampleMassGrams >= 1.0) {
        document.getElementById("resAnalyteSampleMass").textContent = sampleMassGrams.toFixed(4) + " g";
      } else {
        document.getElementById("resAnalyteSampleMass").textContent = (sampleMassGrams * 1000.0).toFixed(2) + " mg";
      }
      document.getElementById("resAnalyteSampleMassSub").textContent = "In " + aV.toFixed(2) + " mL sample flask";

      document.getElementById("resEquivalenceVolume").textContent = tV.toFixed(2) + " mL";
      document.getElementById("resTotalMolesAnalyte").textContent = (totalMoles * 1000.0).toFixed(3) + " mmol";

      document.getElementById("resEquilPH").textContent = preset.eqPH;
      document.getElementById("resRecIndicator").textContent = preset.ind;
      document.getElementById("resRecIndicatorRange").textContent = "Transition: " + preset.indRange;

      document.getElementById("resTitrationError").textContent = "±" + relError.toFixed(2) + "% Error";

      document.getElementById("resReactionRatio").textContent = tZ + " eq Titrant reacts with " + aZ + " eq Analyte (Ratio: " + (tZ/aZ).toFixed(2) + " : 1).";
      document.getElementById("resColorTransition").textContent = preset.indTrans;
    }

    window.addEventListener("DOMContentLoaded", () => {
      calcTitration();
    });
  </script>
</body>
</html>
"""

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p1 = os.path.join(base_dir, "sulphuric-acid-dosing-calculator.html")
    p2 = os.path.join(base_dir, "titration-calculator.html")

    with open(p1, "w", encoding="utf-8") as f:
        f.write(TOOL_1_HTML)
    print(f"Generated {p1}")

    with open(p2, "w", encoding="utf-8") as f:
        f.write(TOOL_2_HTML)
    print(f"Generated {p2}")

if __name__ == "__main__":
    main()
