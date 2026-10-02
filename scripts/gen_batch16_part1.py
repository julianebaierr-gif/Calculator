# -*- coding: utf-8 -*-
"""
Script to generate Batch 16 Part 1 tools:
1. lime-dosing-calculator.html
2. molar-mass-calculator.html
"""
import os

TOOL_1_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lime Dosing Calculator | Hydrated &amp; Quicklime Water Softening Sizer</title>
  <meta name="description" content="Calculate hydrated lime (Ca(OH)2) and quicklime (CaO) dosing rates for water softening, dissolved CO2 neutralization, slurry feed rate, and sludge production.">
  <link rel="canonical" href="https://calchub.cloud/lime-dosing-calculator.html">
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
        "name": "Lime Dosing Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates stoichiometric hydrated lime and quicklime feed rates for water softening, dissolved CO2 neutralization, carbonate hardness precipitation, and sludge mass generation.",
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
            "name": "What is the difference between quicklime (CaO) and hydrated lime (Ca(OH)2)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Quicklime (calcium oxide, CaO, MW = 56.08 g/mol) is manufactured by calcining limestone (CaCO3) at 900-1000°C. Hydrated lime (calcium hydroxide, Ca(OH)2, MW = 74.09 g/mol) is produced by slaking quicklime with water: CaO + H2O -> Ca(OH)2 + 65.2 kJ/mol heat. Because CaO has a lower molecular weight, 1.0 lb of 100% pure CaO is stoichiometrically equivalent to 1.321 lbs of pure Ca(OH)2."
            }
          },
          {
            "@type": "Question",
            "name": "What chemical reactions occur during lime softening of drinking water?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Lime softening proceeds through three sequential chemical reactions: (1) Neutralization of dissolved carbonic acid/CO2: CO2 + Ca(OH)2 -> CaCO3 + H2O; (2) Removal of calcium carbonate hardness: Ca(HCO3)2 + Ca(OH)2 -> 2CaCO3 + 2H2O; and (3) Removal of magnesium hardness at pH > 10.8: Mg(HCO3)2 + 2Ca(OH)2 -> 2CaCO3 + Mg(OH)2 + 2H2O."
            }
          },
          {
            "@type": "Question",
            "name": "Why is excess lime required to remove magnesium hardness?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Calcium carbonate (CaCO3) precipitates effectively at pH 9.2 to 9.6. However, magnesium hydroxide (Mg(OH)2) is significantly more soluble and requires raising water pH to between 10.8 and 11.2 to achieve precipitation. This requires dosing approximately 30 to 50 mg/L of 'excess lime' beyond the stoichiometric carbonate demand."
            }
          },
          {
            "@type": "Question",
            "name": "How much dry sludge solids are generated during lime softening?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For every mole of calcium carbonate hardness removed, two moles of solid CaCO3 precipitate (one from the raw water hardness and one from the added lime reagent). The dry sludge solids generation typically ranges from 2.0 to 2.8 times the weight of pure quicklime dosed, producing heavy chemical sludge that requires gravity thickening and dewatering."
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
      <span>Lime Dosing Calculator</span>
    </nav>

    <h1 class="tool-title">Lime Dosing &amp; Softening Calculator</h1>
    <p class="tool-subtitle">Hydrated Lime Ca(OH)₂, Quicklime CaO Stoichiometry, Slurry Feeder &amp; Sludge Sizer</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="treatmentObjective">Water Treatment Process Objective</label>
            <select id="treatmentObjective" class="form-control" onchange="updateObjectivePreset()">
              <option value="single_stage" selected>Single-Stage Softening (Calcium Hardness Removal to pH 9.4)</option>
              <option value="excess_lime">Excess Lime Softening (Magnesium + Calcium Removal to pH 11.0)</option>
              <option value="ph_corrosion">pH / Alkalinity Adjustment &amp; Lead/Copper Corrosion Control</option>
              <option value="wastewater_p">Wastewater Phosphorus Precipitation (pH &gt; 11.5)</option>
              <option value="custom">Custom Stoichiometric Dosage</option>
            </select>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="flowRateVal">Raw Water Flow Rate</label>
              <input type="number" id="flowRateVal" class="form-control" value="10.0" step="0.5" min="0.01">
            </div>
            <div class="form-group">
              <label for="flowRateUnit">Flow Units</label>
              <select id="flowRateUnit" class="form-control">
                <option value="mgd" selected>Million Gallons / Day (MGD)</option>
                <option value="gpm">Gallons / Minute (GPM)</option>
                <option value="m3h">Cubic Meters / Hour (m³/h)</option>
                <option value="mld">Million Liters / Day (MLD)</option>
                <option value="lps">Liters / Second (L/s)</option>
              </select>
            </div>
          </div>

          <!-- Water Chemistry Inputs -->
          <div class="grid-2-col">
            <div class="form-group">
              <label for="dissolvedCO2Val">Dissolved CO₂ (as CO₂)</label>
              <input type="number" id="dissolvedCO2Val" class="form-control" value="8.0" step="0.5" min="0.0">
              <span class="field-hint">mg/L as CO₂ (consumes lime first)</span>
            </div>
            <div class="form-group">
              <label for="bicarbAlkVal">Total Alkalinity (as CaCO₃)</label>
              <input type="number" id="bicarbAlkVal" class="form-control" value="160.0" step="5.0" min="0.0">
              <span class="field-hint">mg/L as CaCO₃ (carbonate hardness)</span>
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="mgHardnessVal">Magnesium Hardness (as CaCO₃)</label>
              <input type="number" id="mgHardnessVal" class="form-control" value="40.0" step="2.0" min="0.0">
              <span class="field-hint">mg/L as CaCO₃</span>
            </div>
            <div class="form-group">
              <label for="excessLimeVal">Excess Lime Allowance (as CaCO₃)</label>
              <input type="number" id="excessLimeVal" class="form-control" value="0.0" step="5.0" min="0.0">
              <span class="field-hint">30-50 mg/L if removing Mg</span>
            </div>
          </div>

          <!-- Lime Reagent Type -->
          <div class="grid-2-col">
            <div class="form-group">
              <label for="limeReagentType">Lime Chemical Reagent Form</label>
              <select id="limeReagentType" class="form-control" onchange="updateReagentType()">
                <option value="hydrated" selected>Hydrated Lime [Ca(OH)₂] - Slaked Powder</option>
                <option value="quicklime">Quicklime [CaO] - Pebble / Granular</option>
              </select>
            </div>
            <div class="form-group">
              <label for="limePurityPct">Commercial Purity (% Active)</label>
              <input type="number" id="limePurityPct" class="form-control" value="92.0" step="0.5" min="50.0" max="100.0">
              <span class="field-hint">Typically 90-95% for Ca(OH)₂, 88-94% for CaO</span>
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="slurryConcPct">Slurry Make-up Concentration (% w/w)</label>
              <input type="number" id="slurryConcPct" class="form-control" value="10.0" step="1.0" min="1.0" max="25.0">
              <span class="field-hint">Feed slurry typically 5% to 15%</span>
            </div>
            <div class="form-group">
              <label for="slurrySGVal">Slurry Specific Gravity (SG)</label>
              <input type="number" id="slurrySGVal" class="form-control" value="1.065" step="0.005" min="1.00" max="1.25">
            </div>
          </div>

          <button type="button" class="btn btn-primary" onclick="calcLimeDosing()" style="width: 100%; margin-top: 15px;">Calculate Lime Demand &amp; Slurry Feed</button>
        </div>
      </div>

      <!-- Output Results Panel -->
      <div class="results-card">
        <div class="result-box primary-result">
          <div class="result-label">Pure Reagent Stoichiometric Dose</div>
          <div id="resPureDoseMgL" class="result-value">132.8 mg/L</div>
          <div id="resPureDoseAlt" class="result-subtext">As 100% active Ca(OH)₂ (144.3 mg/L commercial 92% product)</div>
        </div>

        <div class="result-grid">
          <div class="result-item">
            <span class="result-label">Daily Commercial Lime</span>
            <span id="resCommercialDailyKg" class="result-value highlight">5,463 kg/day</span>
            <span id="resCommercialDailyLbs" class="result-subtext">12,044 lbs/day (6.02 tons/day)</span>
          </div>
          <div class="result-item">
            <span class="result-label">Dry Lime Feed Rate</span>
            <span id="resDryFeedRateKgHr" class="result-value">227.6 kg/h</span>
            <span id="resDryFeedRateLbMin" class="result-subtext">3.79 kg/min (8.36 lb/min)</span>
          </div>
          <div class="result-item">
            <span class="result-label">Slurry Feeder Pump Rate</span>
            <span id="resSlurryPumpLph" class="result-value">2,137 L/h</span>
            <span id="resSlurryPumpGpm" class="result-subtext">9.41 GPM (35.6 L/min)</span>
          </div>
          <div class="result-item">
            <span class="result-label">Dry Sludge Solids Yield</span>
            <span id="resDrySludgeKgDay" class="result-value">9,520 kg/day</span>
            <span id="resDrySludgeLbsDay" class="result-subtext">20,988 lbs/day dry solids</span>
          </div>
          <div class="result-item">
            <span class="result-label">Quicklime Heat of Slaking</span>
            <span id="resSlakingHeat" class="result-value">N/A (Hydrated Lime)</span>
            <span id="resSlakingHeatSub" class="result-subtext">Exothermic rise during slaking</span>
          </div>
          <div class="result-item">
            <span class="result-label">Target Process pH</span>
            <span id="resProcessPH" class="result-value">9.3 &ndash; 9.5</span>
            <span class="result-subtext">Optimum CaCO₃ precipitation zone</span>
          </div>
        </div>

        <div class="result-details" style="margin-top: 15px;">
          <p><strong>Lime Truckload Frequency (25-Ton Silo Tanker):</strong> <span id="resTruckloadFreq">1 Truckload every 4.2 Days</span></p>
          <p><strong>Process Stoichiometry Breakdown:</strong> <span id="resStoichBreakdown">CO₂: 13.5 mg/L | Carbonate Alk: 118.5 mg/L | Mg: 0.0 mg/L</span></p>
        </div>
      </div>
    </div>

    <!-- 1000+ Words Engineering Body -->
    <article class="article-body">
      <h2>Principles of Chemical Precipitation Softening</h2>
      <p>Water hardness in municipal water supplies and industrial cooling circuits is caused primarily by multivalent metallic cations, dominated by calcium ($\text{Ca}^{2+}$) and magnesium ($\text{Mg}^{2+}$). When water containing high concentrations of calcium bicarbonate is heated, cooled, or evaporated, it precipitates insoluble calcium carbonate ($\text{CaCO}_3$) scale inside boilers, heat exchangers, cooling towers, and domestic piping, drastically degrading heat transfer coefficients and causing pipe occlusion.</p>

      <p>Chemical precipitation softening via <strong>lime addition</strong> remains the most cost-effective and scalable technology for large-scale municipal drinking water facilities and heavy industrial wastewater reclamation plants. Depending on the mineral composition of the raw water and the target finished water hardness, treatment facilities utilize either <strong>quicklime</strong> (calcium oxide, $\text{CaO}$) or <strong>hydrated lime</strong> (calcium hydroxide, $\text{Ca(OH)}_2$). The added hydroxyl ions ($\text{OH}^-$) react with carbonic species, converting soluble bicarbonate ($\text{HCO}_3^-$) into carbonate ($\text{CO}_3^{2-}$), which then combines with soluble $\text{Ca}^{2+}$ to exceed the solubility product ($K_{sp} = 3.3 \times 10^{-9}\text{ at } 25^\circ\text{C}$), precipitating dense crystalline $\text{CaCO}_3$.</p>

      <h2>Chemical Reactions and Stoichiometric Mass Balance</h2>
      <p>Lime softening proceeds through three sequential chemical pathways governed by solution pH and carbonate equilibrium:</p>

      <h3>1. Neutralization of Free Dissolved Carbon Dioxide (CO₂)</h3>
      <p>Dissolved carbon dioxide acts as carbonic acid ($\text{H}_2\text{CO}_3$) and consumes lime reagent immediately without yielding any hardness reduction. It must be quantitatively neutralized before pH can rise sufficiently to initiate calcium precipitation:</p>

      <div class="formula-box">
        $$\text{CO}_2 + \text{Ca(OH)}_2 \longrightarrow \text{CaCO}_3\downarrow + \text{H}_2\text{O}$$
      </div>
      <p>Stoichiometrically, $44.01\text{ g of CO}_2$ requires $74.09\text{ g of pure Ca(OH)}_2$ (ratio $= 1.683$) or $56.08\text{ g of pure CaO}$ (ratio $= 1.274$). Expressed per unit of $\text{mg/L as CO}_2$:</p>
      <div class="formula-box">
        $$\text{Ca(OH)}_2\text{ Demand} = \text{CO}_2\text{ (mg/L)} \times \frac{74.09}{44.01} = 1.683 \times \text{CO}_2\text{ (mg/L)}$$
        $$\text{CaO Demand} = \text{CO}_2\text{ (mg/L)} \times \frac{56.08}{44.01} = 1.274 \times \text{CO}_2\text{ (mg/L)}$$
      </div>

      <h3>2. Removal of Calcium Carbonate Hardness (Alkalinity)</h3>
      <p>Calcium associated with natural alkalinity (carbonate hardness) is precipitated as calcium carbonate at $\text{pH } 9.2\text{ to } 9.6$:</p>

      <div class="formula-box">
        $$\text{Ca(HCO}_3)_2 + \text{Ca(OH)}_2 \longrightarrow 2\text{CaCO}_3\downarrow + 2\text{H}_2\text{O}$$
      </div>
      <p>Notice that for each mole of calcium hardness removed from the water, two moles of $\text{CaCO}_3$ precipitate (one from the incoming hardness and one from the lime reagent). Because alkalinity is conventionally reported in terms of $\text{mg/L as CaCO}_3$ ($\text{MW} = 100.09\text{ g/mol}$):</p>
      <div class="formula-box">
        $$\text{Ca(OH)}_2\text{ Demand} = \text{Alkalinity (mg/L as CaCO}_3) \times \frac{74.09}{100.09} = 0.7402 \times \text{Alk}$$
        $$\text{CaO Demand} = \text{Alkalinity (mg/L as CaCO}_3) \times \frac{56.08}{100.09} = 0.5603 \times \text{Alk}$$
      </div>

      <h3>3. Removal of Magnesium Hardness (Excess Lime Process)</h3>
      <p>Magnesium carbonate ($\text{MgCO}_3$) is relatively soluble ($K_{sp} \approx 6.8 \times 10^{-6}$). To precipitate magnesium, the pH must be elevated above $10.8$ to convert magnesium into highly insoluble magnesium hydroxide ($\text{Mg(OH)}_2$, brucite, $K_{sp} = 5.6 \times 10^{-12}$):</p>

      <div class="formula-box">
        $$\text{Mg(HCO}_3)_2 + 2\text{Ca(OH)}_2 \longrightarrow 2\text{CaCO}_3\downarrow + \text{Mg(OH)}_2\downarrow + 2\text{H}_2\text{O}$$
      </div>
      <p>If non-carbonate magnesium hardness is present (e.g., $\text{MgSO}_4$ or $\text{MgCl}_2$), the reaction proceeds as:</p>
      <div class="formula-box">
        $$\text{MgSO}_4 + \text{Ca(OH)}_2 \longrightarrow \text{Mg(OH)}_2\downarrow + \text{CaSO}_4$$
      </div>
      <p>In both cases, each mole of magnesium hardness ($\text{as CaCO}_3$) requires one stoichiometric mole of lime, plus an operational <strong>excess lime allowance</strong> ($30\text{ to } 50\text{ mg/L as CaCO}_3$) to maintain the elevated $\text{pH } 11.0$ required for complete driving force:</p>
      <div class="formula-box">
        $$\text{Ca(OH)}_2\text{ Demand for Mg} = \left[ \text{Mg (mg/L as CaCO}_3) + \text{Excess} \right] \times \frac{74.09}{100.09} = 0.7402 \times (\text{Mg} + \text{Excess})$$
        $$\text{CaO Demand for Mg} = \left[ \text{Mg (mg/L as CaCO}_3) + \text{Excess} \right] \times \frac{56.08}{100.09} = 0.5603 \times (\text{Mg} + \text{Excess})$$
      </div>

      <h2>Unified Stoichiometric Dosing Formula</h2>
      <p>Combining all chemical demands and dividing by the commercial reagent purity fraction ($P_{\text{lime}}$) gives the total commercial dosing requirement ($D_{\text{commercial}}$ in $\text{mg/L}$):</p>

      <div class="formula-box">
        $$D_{\text{commercial, Ca(OH)}_2}\text{ (mg/L)} = \frac{1.683 \cdot [\text{CO}_2] + 0.7402 \cdot [\text{Alk}] + 0.7402 \cdot [\text{Mg}] + 0.7402 \cdot [\text{Excess}]}{P_{\text{lime}}}$$
        $$D_{\text{commercial, CaO}}\text{ (mg/L)} = \frac{1.274 \cdot [\text{CO}_2] + 0.5603 \cdot [\text{Alk}] + 0.5603 \cdot [\text{Mg}] + 0.5603 \cdot [\text{Excess}]}{P_{\text{lime}}}$$
      </div>

      <h2>Quicklime Slaking Thermodynamics and Feeder Sizing</h2>
      <p>When municipal facilities utilize quicklime ($\text{CaO}$), dry pebble lime is transported via screw conveyor into an automated detention, paste, or ball mill lime slaker. The reaction with water is intensely exothermic:</p>

      <div class="formula-box">
        $$\text{CaO (s)} + \text{H}_2\text{O (l)} \longrightarrow \text{Ca(OH)}_2\text{ (s)} + \Delta H \quad (\Delta H = -65.2\text{ kJ/mol} = -1,162\text{ kJ/kg CaO})$$
      </div>
      <p>Under optimum slaking conditions, water temperature inside the slaker rises to between $70^\circ\text{C}\text{ and } 85^\circ\text{C}\ (160^\circ\text{F}\text{ to } 185^\circ\text{F})$. This high thermal energy shatters the calcium oxide crystals into ultra-fine sub-micron particles, maximizing specific surface area and chemical reactivity. Slurry feed systems typically blend the slaked product with service water to form a $5\%\text{ to } 15\%\text{ w/w}$ milk-of-lime suspension, pumped using peristaltic hose or recessed impeller centrifugal pumps equipped with flushing cycles to prevent calcium scaling.</p>

      <h2>Dry Sludge Solids Generation Formulas</h2>
      <p>The total mass of dry chemical sludge solids produced ($\dot{M}_{\text{sludge}}$) is computed by summing the precipitates of calcium carbonate and magnesium hydroxide:</p>

      <div class="formula-box">
        $$\text{Precipitated CaCO}_3\text{ (mg/L)} = \text{CO}_2\text{ (mg/L)} \times \left(\frac{100.09}{44.01}\right) + 2 \times \text{Alk}_{\text{removed}} + \text{Ca}_{\text{non-carb removed}}$$
        $$\text{Precipitated Mg(OH)}_2\text{ (mg/L)} = \text{Mg}_{\text{removed}}\text{ (as CaCO}_3) \times \left(\frac{58.32}{100.09}\right) = 0.5827 \times \text{Mg}_{\text{removed}}$$
      </div>
      <p>In practice, lime softening generates approximately $2.0\text{ to } 2.8\text{ kg of dry sludge solids}$ for every $1.0\text{ kg of pure CaO}$ consumed, requiring substantial clarifier sludge blanket capacity, gravity thickeners, and belt filter presses or centrifuges capable of dewatering lime sludge cake to $50\%\text{ to } 65\%\text{ dry solids}$.</p>

      <h2>Benchmark Engineering Standards for Lime Softening</h2>
      <p>The table below summarizes treatment criteria, pH targets, and sludge characteristics across established softening configurations per <strong>AWWA Manual M37</strong> and <strong>Ten States Standards</strong>:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Softening Configuration</th>
              <th>Operating pH Range</th>
              <th>Target Hardness Reduction</th>
              <th>Typical Excess Lime</th>
              <th>Sludge Volume Index (SVI)</th>
              <th>Recarbonation Requirement</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Single-Stage Lime (Selective Calcium)</td>
              <td>9.2 &ndash; 9.6</td>
              <td>Calcium carbonate hardness only</td>
              <td>0 mg/L (Stoichiometric)</td>
              <td>40 &ndash; 70 mL/g (Fast settling)</td>
              <td>Single-stage CO₂ to pH 8.5</td>
            </tr>
            <tr>
              <td>Excess Lime (Two-Stage Softening)</td>
              <td>10.8 &ndash; 11.2</td>
              <td>Both Calcium and Magnesium</td>
              <td>35 &ndash; 50 mg/L as CaCO₃</td>
              <td>80 &ndash; 120 mL/g (Gelatinous Mg)</td>
              <td>Two-stage recarbonation (pH 9.5 then 8.3)</td>
            </tr>
            <tr>
              <td>Split Treatment</td>
              <td>10.5 &ndash; 11.0 (Stage 1)</td>
              <td>Optimized Mg removal with bypass</td>
              <td>20 &ndash; 40 mg/L</td>
              <td>60 &ndash; 90 mL/g</td>
              <td>Raw water bypass neutralizes Stage 1</td>
            </tr>
            <tr>
              <td>Corrosion Inhibition / pH Trim</td>
              <td>7.8 &ndash; 8.4</td>
              <td>Alkalinity increase for lead/copper</td>
              <td>None (5 &ndash; 15 mg/L dose)</td>
              <td>Negligible solids</td>
              <td>None required</td>
            </tr>
            <tr>
              <td>Tertiary Phosphorus Coagulation</td>
              <td>&gt; 11.2</td>
              <td>Precipitates Hydroxyapatite [Ca₅(PO₄)₃OH]</td>
              <td>Excess to reach pH threshold</td>
              <td>100 &ndash; 160 mL/g</td>
              <td>Acid or CO₂ neutralization</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Practical Worked Case Study: Municipal Softening Plant Design</h2>
      <div class="worked-example-card">
        <h3>Civil / Environmental Engineering Design Example: 15 MGD Facility</h3>
        <p><strong>Scenario:</strong> A municipal water treatment authority operates a $Q = 15.0\text{ MGD}$ ($56,781\text{ m}^3/\text{day}$ or $10,417\text{ GPM}$) surface water softening plant. Laboratory titration data indicates: dissolved carbon dioxide $[\text{CO}_2] = 10.0\text{ mg/L}$, total carbonate alkalinity $= 180.0\text{ mg/L as CaCO}_3$, and magnesium hardness $[\text{Mg}^{2+}] = 44.0\text{ mg/L as CaCO}_3$. The plant utilizes two-stage excess lime softening to reduce finished water hardness below $85\text{ mg/L as CaCO}_3$ and magnesium below $10\text{ mg/L}$. An excess lime dose of $35.0\text{ mg/L as CaCO}_3$ is maintained in the primary contact clarifier. Commercial pebble quicklime ($\text{CaO}$) is purchased at $90.0\%\text{ available CaO purity}$. Slurry is slaked and fed as a $10.0\%\text{ w/w}$ suspension ($\text{SG} = 1.065$).</p>

        <p><strong>Step 1: Compute Stoichiometric Pure Quicklime (CaO) Demand:</strong></p>
        $$\text{Pure CaO Demand} = (1.274 \times 10.0) + [0.5603 \times (180.0 + 44.0 + 35.0)]$$
        $$\text{Pure CaO Demand} = 12.74 + [0.5603 \times 259.0] = 12.74 + 145.12 = 157.86\text{ mg/L pure CaO}$$

        <p><strong>Step 2: Account for 90.0% Commercial Purity:</strong></p>
        $$D_{\text{commercial}} = \frac{157.86\text{ mg/L}}{0.90} = 175.40\text{ mg/L commercial quicklime}$$

        <p><strong>Step 3: Calculate Daily Commercial Quicklime Mass Feed Rate:</strong></p>
        $$\text{Mass Rate} = 15.0\text{ MGD} \times 175.40\text{ mg/L} \times 8.3454\text{ lb/(MGD}\cdot\text{mg/L)} = 21,956\text{ lbs/day}\ (9,959\text{ kg/day})$$
        $$\text{Hourly Dry Feed} = \frac{21,956\text{ lbs}}{24\text{ hours}} = 914.8\text{ lbs/hour}\ (414.9\text{ kg/hour})$$
        $$\text{Tonnage} = \frac{21,956\text{ lbs/day}}{2,000\text{ lbs/ton}} = 10.98\text{ US tons / day}$$

        <p><strong>Step 4: Sizing the 10% Slurry Dosing Pumps:</strong></p>
        <p>Each kilogram of dry commercial quicklime slakes into $1.321\text{ kg of Ca(OH)}_2$. In a $10\%\text{ w/w}$ slurry with specific gravity $\text{SG} = 1.065$ ($\text{density} = 1.065\text{ kg/L}$):</p>
        $$\text{Slurry Volumetric Flow} = \frac{9,959\text{ kg commercial CaO/day} \times 1.321}{0.10 \times 1.065\text{ kg/L}} = \frac{13,156}{0.1065} = 123,530\text{ Liters / day}$$
        $$q_{\text{slurry}} = \frac{123,530\text{ L/day}}{24\text{ h}} = 5,147\text{ L/hour}\ (22.66\text{ GPM})$$

        <p><strong>Step 5: Dry Sludge Solids Generation:</strong></p>
        $$\text{CaCO}_3\text{ Solids} = (10.0 \times 2.274) + (2 \times 180.0) = 22.74 + 360.0 = 382.74\text{ mg/L}$$
        $$\text{Mg(OH)}_2\text{ Solids} = 44.0 \times 0.5827 = 25.64\text{ mg/L}$$
        $$\text{Total Dry Sludge} = (382.74 + 25.64) = 408.38\text{ mg/L}$$
        $$\text{Daily Dry Sludge} = 15.0\text{ MGD} \times 408.38\text{ mg/L} \times 8.3454 = 51,123\text{ lbs/day dry solids}\ (23,189\text{ kg/day})$$
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
          <p class="footer-about">High-precision water treatment softening stoichiometry, lime slaking kinetics, and sludge management tools conforming to AWWA and EPA standards.</p>
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
            <li><a href="https://www.awwa.org" target="_blank" rel="noopener">AWWA Manual M37 Water Softening</a></li>
            <li><a href="https://www.epa.gov" target="_blank" rel="noopener">EPA Water Treatment Technology</a></li>
            <li><a href="https://www.lime.org" target="_blank" rel="noopener">National Lime Association Engineering</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    function updateObjectivePreset() {
      const obj = document.getElementById("treatmentObjective").value;
      if (obj === "single_stage") {
        document.getElementById("dissolvedCO2Val").value = 8.0;
        document.getElementById("bicarbAlkVal").value = 160.0;
        document.getElementById("mgHardnessVal").value = 0.0;
        document.getElementById("excessLimeVal").value = 0.0;
      } else if (obj === "excess_lime") {
        document.getElementById("dissolvedCO2Val").value = 10.0;
        document.getElementById("bicarbAlkVal").value = 180.0;
        document.getElementById("mgHardnessVal").value = 45.0;
        document.getElementById("excessLimeVal").value = 35.0;
      } else if (obj === "ph_corrosion") {
        document.getElementById("dissolvedCO2Val").value = 5.0;
        document.getElementById("bicarbAlkVal").value = 20.0;
        document.getElementById("mgHardnessVal").value = 0.0;
        document.getElementById("excessLimeVal").value = 0.0;
      } else if (obj === "wastewater_p") {
        document.getElementById("dissolvedCO2Val").value = 15.0;
        document.getElementById("bicarbAlkVal").value = 220.0;
        document.getElementById("mgHardnessVal").value = 30.0;
        document.getElementById("excessLimeVal").value = 50.0;
      }
    }

    function updateReagentType() {
      const r = document.getElementById("limeReagentType").value;
      if (r === "quicklime") {
        document.getElementById("limePurityPct").value = 90.0;
      } else {
        document.getElementById("limePurityPct").value = 92.0;
      }
    }

    function calcLimeDosing() {
      const flowVal = parseFloat(document.getElementById("flowRateVal").value) || 0;
      const flowUnit = document.getElementById("flowRateUnit").value;
      const co2 = parseFloat(document.getElementById("dissolvedCO2Val").value) || 0;
      const alk = parseFloat(document.getElementById("bicarbAlkVal").value) || 0;
      const mg = parseFloat(document.getElementById("mgHardnessVal").value) || 0;
      const excess = parseFloat(document.getElementById("excessLimeVal").value) || 0;
      const reagent = document.getElementById("limeReagentType").value;
      const purityPct = parseFloat(document.getElementById("limePurityPct").value) || 90.0;
      const slurryPct = parseFloat(document.getElementById("slurryConcPct").value) || 10.0;
      const slurrySG = parseFloat(document.getElementById("slurrySGVal").value) || 1.065;

      // Flow conversion to MGD and m3/day
      let flow_mgd = 0;
      let flow_m3_day = 0;
      if (flowUnit === "mgd") {
        flow_mgd = flowVal;
        flow_m3_day = flowVal * 3785.41;
      } else if (flowUnit === "gpm") {
        flow_mgd = (flowVal * 1440) / 1000000;
        flow_m3_day = flowVal * 5.45099;
      } else if (flowUnit === "m3h") {
        flow_m3_day = flowVal * 24;
        flow_mgd = (flowVal * 24) / 3785.41;
      } else if (flowUnit === "mld") {
        flow_m3_day = flowVal * 1000;
        flow_mgd = flowVal * 0.264172;
      } else if (flowUnit === "lps") {
        flow_m3_day = flowVal * 86.4;
        flow_mgd = flow_m3_day / 3785.41;
      }

      // Stoichiometry
      let k_co2 = 0;
      let k_alk = 0;
      let reagentName = "";
      if (reagent === "hydrated") {
        k_co2 = 74.093 / 44.01; // 1.6835
        k_alk = 74.093 / 100.087; // 0.7403
        reagentName = "Ca(OH)₂";
      } else {
        k_co2 = 56.077 / 44.01; // 1.2742
        k_alk = 56.077 / 100.087; // 0.5603
        reagentName = "CaO";
      }

      const co2Demand = co2 * k_co2;
      const alkDemand = alk * k_alk;
      const mgDemand = mg * k_alk;
      const excessDemand = excess * k_alk;

      const pureDoseMgL = co2Demand + alkDemand + mgDemand + excessDemand;
      const commDoseMgL = pureDoseMgL / (purityPct / 100.0);

      // Mass calculations
      const dailyCommKg = (flow_m3_day * commDoseMgL) / 1000.0;
      const dailyCommLbs = flow_mgd * commDoseMgL * 8.3454;
      const hourlyDryFeedKg = dailyCommKg / 24.0;
      const minDryFeedKg = hourlyDryFeedKg / 60.0;
      const minDryFeedLbs = (dailyCommLbs / 24.0) / 60.0;

      // Slurry flow calculation
      // Commercial lime slaked or dispersed
      let activeSlurryKgDay = dailyCommKg;
      if (reagent === "quicklime") {
        // CaO slakes to Ca(OH)2: factor 74.09 / 56.08 = 1.321
        activeSlurryKgDay = dailyCommKg * (purityPct / 100.0 * 1.321 + (1 - purityPct / 100.0));
      }
      const totalSlurryKgDay = activeSlurryKgDay / (slurryPct / 100.0);
      const totalSlurryLitersDay = totalSlurryKgDay / slurrySG;
      const slurryLph = totalSlurryLitersDay / 24.0;
      const slurryGpm = (slurryLph * 0.264172) / 60.0;

      // Dry sludge solids
      // CaCO3 precipitated = CO2*(100/44) + 2*Alk_removed
      // Mg(OH)2 precipitated = Mg * (58.32 / 100.09) = 0.5827
      const caco3PrecipMgL = (co2 * 2.274) + (2.0 * alk);
      const mgoh2PrecipMgL = mg * 0.5827;
      const totalSludgeMgL = caco3PrecipMgL + mgoh2PrecipMgL;
      const drySludgeKgDay = (flow_m3_day * totalSludgeMgL) / 1000.0;
      const drySludgeLbsDay = flow_mgd * totalSludgeMgL * 8.3454;

      // Silo truckload frequency (25 ton truck = 22,680 kg)
      const truckDays = dailyCommKg > 0 ? (22680.0 / dailyCommKg).toFixed(1) : "N/A";

      // Heat of slaking
      let heatStr = "N/A (Hydrated Lime)";
      let heatSub = "Dry slaked powder (no slaking reaction)";
      if (reagent === "quicklime") {
        // 1162 kJ / kg pure CaO
        const heatKj = (dailyCommKg * (purityPct / 100.0)) * 1162;
        const heatKwh = heatKj / 3600.0;
        heatStr = (heatKwh / 24.0).toFixed(1) + " kW continuous";
        heatSub = (heatKj / 1000000).toFixed(2) + " GJ / day exothermic release";
      }

      // Process pH
      let pHStr = "9.2 – 9.5";
      if (mg > 0 || excess > 0) pHStr = "10.8 – 11.2 (Mg removal)";
      else if (alk < 40 && co2 < 10) pHStr = "8.2 – 8.6 (Corrosion control)";

      // Render outputs
      document.getElementById("resPureDoseMgL").textContent = pureDoseMgL.toFixed(1) + " mg/L pure " + reagentName;
      document.getElementById("resPureDoseAlt").textContent = "Commercial " + purityPct + "%: " + commDoseMgL.toFixed(1) + " mg/L (ppm)";

      document.getElementById("resCommercialDailyKg").textContent = dailyCommKg.toLocaleString(undefined, {maximumFractionDigits: 0}) + " kg/day";
      document.getElementById("resCommercialDailyLbs").textContent = dailyCommLbs.toLocaleString(undefined, {maximumFractionDigits: 0}) + " lbs/day (" + (dailyCommLbs / 2000).toFixed(2) + " tons/day)";

      document.getElementById("resDryFeedRateKgHr").textContent = hourlyDryFeedKg.toFixed(1) + " kg/h";
      document.getElementById("resDryFeedRateLbMin").textContent = minDryFeedKg.toFixed(2) + " kg/min (" + minDryFeedLbs.toFixed(2) + " lb/min)";

      document.getElementById("resSlurryPumpLph").textContent = slurryLph.toFixed(0) + " L/h";
      document.getElementById("resSlurryPumpGpm").textContent = slurryGpm.toFixed(2) + " GPM (" + (slurryLph / 60.0).toFixed(1) + " L/min)";

      document.getElementById("resDrySludgeKgDay").textContent = drySludgeKgDay.toLocaleString(undefined, {maximumFractionDigits: 0}) + " kg/day";
      document.getElementById("resDrySludgeLbsDay").textContent = drySludgeLbsDay.toLocaleString(undefined, {maximumFractionDigits: 0}) + " lbs/day dry solids";

      document.getElementById("resSlakingHeat").textContent = heatStr;
      document.getElementById("resSlakingHeatSub").textContent = heatSub;

      document.getElementById("resProcessPH").textContent = pHStr;

      document.getElementById("resTruckloadFreq").textContent = "1 Truckload (25-Ton Silo Tanker) every " + truckDays + " Days";

      document.getElementById("resStoichBreakdown").textContent = "CO₂: " + co2Demand.toFixed(1) + " mg/L | Carbonate Alk: " + alkDemand.toFixed(1) + " mg/L | Mg: " + mgDemand.toFixed(1) + " mg/L | Excess: " + excessDemand.toFixed(1) + " mg/L";
    }

    window.addEventListener("DOMContentLoaded", () => {
      calcLimeDosing();
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
  <title>Molar Mass Calculator | Molecular Weight &amp; Formula Mass Sizer</title>
  <meta name="description" content="Calculate molar mass, molecular weight, elemental mass percent composition, and mole-to-gram conversions using standard IUPAC atomic weights.">
  <link rel="canonical" href="https://calchub.cloud/molar-mass-calculator.html">
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
        "name": "Molar Mass Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates molecular weight, molar mass, elemental percentage composition, and empirical formula mass for chemical compounds using standard IUPAC atomic weights.",
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
            "name": "What is the difference between molecular weight, molar mass, and formula weight?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Molecular weight (relative molecular mass, Mr) is a dimensionless ratio comparing the mass of a molecule to 1/12th the mass of a carbon-12 atom. Molar mass (M) is the mass of one mole of substance expressed in units of grams per mole (g/mol) or kg/kmol. Formula weight applies specifically to ionic compounds (such as NaCl or CaCO3) that do not exist as discrete discrete molecules."
            }
          },
          {
            "@type": "Question",
            "name": "How does the formula parser handle hydrates and parentheses?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The chemical formula parser processes nested parentheses and dot-separated hydrates algebraically. For example, in aluminum sulfate octadecahydrate Al2(SO4)3·18H2O, the subscript 3 multiplies both sulfur (1*3=3) and oxygen (4*3=12), while the hydrate coefficient 18 adds 36 hydrogens and 18 oxygens, yielding a total molar mass of 666.42 g/mol."
            }
          },
          {
            "@type": "Question",
            "name": "What standard atomic weights are utilized in modern molar mass calculations?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "This calculator adheres strictly to the Commission on Isotopic Abundances and Atomic Weights (CIAAW) under IUPAC. Because terrestrial isotopic abundances vary slightly by geographical origin, IUPAC publishes standard atomic weights reflecting natural terrestrial occurrence (e.g., Carbon = 12.011 g/mol, Oxygen = 15.999 g/mol, Hydrogen = 1.008 g/mol)."
            }
          },
          {
            "@type": "Question",
            "name": "How do you calculate mass percent of an element in a chemical compound?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The mass percentage (w/w%) of an element i is calculated as: % Mass = (n_i * A_r(i) / M_total) * 100%, where n_i is the number of atoms of element i in the chemical formula, A_r(i) is its standard atomic weight, and M_total is the total molar mass of the compound."
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
      <span>Molar Mass Calculator</span>
    </nav>

    <h1 class="tool-title">Molar Mass &amp; Molecular Weight Calculator</h1>
    <p class="tool-subtitle">IUPAC Atomic Weights, Elemental Mass Composition &amp; Gram-Mole Interconversion</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="compoundPreset">Common Compound Presets</label>
            <select id="compoundPreset" class="form-control" onchange="updateCompoundPreset()">
              <option value="H2O">Water (H₂O)</option>
              <option value="C6H12O6" selected>D-Glucose (C₆H₁₂O₆)</option>
              <option value="H2SO4">Sulfuric Acid (H₂SO₄)</option>
              <option value="CaCO3">Calcium Carbonate (CaCO₃)</option>
              <option value="Al2(SO4)3.18H2O">Alum Hydrate [Al₂(SO₄)₃·18H₂O]</option>
              <option value="C8H10N4O2">Caffeine (C₈H₁₀N₄O₂)</option>
              <option value="C9H8O4">Aspirin (Acetylsalicylic Acid, C₉H₈O₄)</option>
              <option value="Fe2O3">Iron(III) Oxide / Rust (Fe₂O₃)</option>
              <option value="NaCl">Sodium Chloride (Table Salt, NaCl)</option>
              <option value="custom">Custom Chemical Formula Entry</option>
            </select>
          </div>

          <div class="form-group">
            <label for="chemFormulaInput">Chemical Formula Entry</label>
            <input type="text" id="chemFormulaInput" class="form-control" value="C6H12O6" placeholder="e.g. Ca(OH)2, Al2(SO4)3.18H2O, CuSO4.5H2O" style="font-size: 1.2rem; font-weight: bold; font-family: monospace;">
            <span class="field-hint">Supports element symbols, subscripts, parentheses, and dot hydrates (e.g. .5H2O)</span>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="convertMode">Conversion Sizing Mode</label>
              <select id="convertMode" class="form-control" onchange="updateConvertMode()">
                <option value="mass_to_mol" selected>Given Mass &rarr; Find Moles &amp; Molecules</option>
                <option value="mol_to_mass">Given Moles &rarr; Find Total Mass</option>
              </select>
            </div>
            <div class="form-group">
              <label for="convertValueInput">Quantity to Convert</label>
              <input type="number" id="convertValueInput" class="form-control" value="100.0" step="1.0" min="0.000001">
              <span id="convertUnitLabel" class="field-hint">Grams (g)</span>
            </div>
          </div>

          <button type="button" class="btn btn-primary" onclick="calcMolarMass()" style="width: 100%; margin-top: 15px;">Parse Formula &amp; Calculate Molar Mass</button>
        </div>
      </div>

      <!-- Output Results Panel -->
      <div class="results-card">
        <div class="result-box primary-result">
          <div class="result-label">Total Molar Mass (M)</div>
          <div id="resMolarMassVal" class="result-value">180.156 g/mol</div>
          <div id="resMolarMassAlt" class="result-subtext">0.18016 kg/mol (180.156 amu / Da)</div>
        </div>

        <div class="result-grid">
          <div class="result-item">
            <span class="result-label">Substance Quantity (n)</span>
            <span id="resMolesVal" class="result-value highlight">0.5551 mol</span>
            <span id="resMolesAlt" class="result-subtext">555.07 mmol</span>
          </div>
          <div class="result-item">
            <span class="result-label">Particle Count (N)</span>
            <span id="resMoleculesVal" class="result-value">3.343 &times; 10²³</span>
            <span class="result-subtext">Molecules via Avogadro Nₐ</span>
          </div>
          <div class="result-item">
            <span class="result-label">Total Sample Mass</span>
            <span id="resSampleMassVal" class="result-value">100.00 g</span>
            <span id="resSampleMassAlt" class="result-subtext">0.1000 kg (0.2205 lbs)</span>
          </div>
          <div class="result-item">
            <span class="result-label">Atom Count per Formula</span>
            <span id="resTotalAtomsVal" class="result-value">24 Atoms</span>
            <span class="result-subtext">Sum of atomic subscripts</span>
          </div>
        </div>

        <!-- Dynamic Element Breakdown Table -->
        <div style="margin-top: 20px;">
          <h4 style="font-size: 1rem; font-weight: 700; margin-bottom: 8px;">Elemental Mass Percent Breakdown</h4>
          <div class="table-responsive">
            <table class="data-table" style="font-size: 0.88rem;">
              <thead>
                <tr>
                  <th>Element</th>
                  <th>Symbol</th>
                  <th>Atomic Wt</th>
                  <th>Atoms</th>
                  <th>Mass (g/mol)</th>
                  <th>Mass %</th>
                </tr>
              </thead>
              <tbody id="elementBreakdownBody">
                <!-- Populated via JavaScript -->
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- 1000+ Words Engineering Body -->
    <article class="article-body">
      <h2>Foundational Principles of Chemical Metrology and Molar Mass</h2>
      <p>In quantitative chemistry, process engineering, and industrial stoichiometry, chemical reactions occur between individual atoms, ions, and molecules in discrete integer ratios governed by quantum mechanics. However, macroscopic laboratory balances and chemical feed equipment measure physical mass in grams, kilograms, or tons. The <strong>mole</strong> ($\text{mol}$) serves as the fundamental SI base unit bridging the submicroscopic molecular scale and the macroscopic engineering world.</p>

      <p>Following the 2019 redefinition of SI base units, the mole is defined by fixing the numerical value of <strong>Avogadro's constant</strong> ($N_A$) to exactly:</p>

      <div class="formula-box">
        $$N_A = 6.02214076 \times 10^{23}\text{ entities per mole}$$
      </div>

      <p>The <strong>molar mass</strong> ($M$) of a chemical entity is defined as the physical mass of one mole of that substance, conventionally reported in grams per mole ($\text{g/mol}$) or kilograms per kilomole ($\text{kg/kmol}$). For discrete molecular covalent substances (such as water $\text{H}_2\text{O}$ or glucose $\text{C}_6\text{H}_{12}\text{O}_6$), molar mass is numerically equivalent to the relative molecular mass ($M_r$). For ionic networks and crystalline minerals (such as sodium chloride $\text{NaCl}$ or calcite $\text{CaCO}_3$) that exist as continuous electrostatic crystal lattices rather than isolated molecules, the quantity is properly termed the <strong>formula mass</strong> or <strong>formula weight</strong>.</p>

      <h2>Mathematical Derivation of Compound Molar Mass</h2>
      <p>The total molar mass of any chemical compound represented by the general empirical formula $\text{A}_a\text{B}_b\text{C}_c\dots$ is calculated as the sum of the standard atomic weights of its constituent chemical elements weighted by their stoichiometric coefficients:</p>

      <div class="formula-box">
        $$M = \sum_{i=1}^{k} n_i \cdot A_r(i)$$
      </div>

      <p>Where $n_i$ represents the number of atoms of element $i$ in the chemical formula unit, and $A_r(i)$ denotes the standard atomic weight (relative atomic mass) of element $i$ established by the IUPAC Commission on Isotopic Abundances and Atomic Weights (CIAAW).</p>

      <h2>Elemental Mass Percentage Composition Formula</h2>
      <p>Gravimetric analytical chemistry and materials characterization frequently require determining the theoretical mass fraction ($w_i$) or mass percentage ($\%_{\text{mass}, i}$) contributed by each individual element within a compound:</p>

      <div class="formula-box">
        $$w_i = \frac{n_i \cdot A_r(i)}{M_{\text{total}}} \quad \implies \quad \%_{\text{mass}, i} = \left(\frac{n_i \cdot A_r(i)}{M_{\text{total}}}\right) \times 100\%$$
      </div>

      <p>By the law of conservation of mass, the sum of all elemental mass percentages across the chemical formula must equal exactly $100.00\%$, establishing a crucial verification audit in chemical assays and combustion elemental analysis ($\text{CHNS-O}$).</p>

      <h2>Mole-to-Mass and Particle Count Conversions</h2>
      <p>Interconverting between physical mass ($m$), molar quantity ($n$), and absolute particle count ($N$) forms the core of stoichiometric pipeline calculations:</p>
      <ul>
        <li><strong>Calculating Substance Quantity (Moles) from Mass:</strong>
        $$n\text{ (mol)} = \frac{m\text{ (g)}}{M\text{ (g/mol)}}$$</li>
        <li><strong>Calculating Total Mass from Moles:</strong>
        $$m\text{ (g)} = n\text{ (mol)} \times M\text{ (g/mol)}$$</li>
        <li><strong>Calculating Absolute Molecular Count:</strong>
        $$N = n\text{ (mol)} \times N_A = \left(\frac{m}{M}\right) \times 6.02214076 \times 10^{23}$$</li>
      </ul>

      <h2>IUPAC Standard Atomic Weights Reference Table</h2>
      <p>The table below summarizes standard atomic weights ($A_r$), atomic numbers ($Z$), standard terrestrial isotopic abundances, and valence states across 15 essential engineering and biological elements per the latest <strong>IUPAC CIAAW 2021 Table of Atomic Weights</strong>:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Atomic No. (Z)</th>
              <th>Element Name</th>
              <th>Symbol</th>
              <th>Standard Atomic Wt (g/mol)</th>
              <th>Major Terrestrial Isotopes</th>
              <th>Key Industrial Function</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1</td>
              <td>Hydrogen</td>
              <td>H</td>
              <td>1.0080</td>
              <td>¹H (99.988%), ²H (0.012%)</td>
              <td>Acids, hydration, hydrocarbons</td>
            </tr>
            <tr>
              <td>6</td>
              <td>Carbon</td>
              <td>C</td>
              <td>12.011</td>
              <td>¹²C (98.93%), ¹³C (1.07%)</td>
              <td>Organic backbone, carbonates, polymers</td>
            </tr>
            <tr>
              <td>7</td>
              <td>Nitrogen</td>
              <td>N</td>
              <td>14.007</td>
              <td>¹⁴N (99.63%), ¹⁵N (0.37%)</td>
              <td>Ammonia, nitric acid, amines, fertilizers</td>
            </tr>
            <tr>
              <td>8</td>
              <td>Oxygen</td>
              <td>O</td>
              <td>15.999</td>
              <td>¹⁶O (99.76%), ¹⁸O (0.20%)</td>
              <td>Oxides, water, combustion oxidant</td>
            </tr>
            <tr>
              <td>11</td>
              <td>Sodium</td>
              <td>Na</td>
              <td>22.990</td>
              <td>²³Na (100% monoisotopic)</td>
              <td>Caustic soda, salts, brine regeneration</td>
            </tr>
            <tr>
              <td>12</td>
              <td>Magnesium</td>
              <td>Mg</td>
              <td>24.305</td>
              <td>²⁴Mg (78.99%), ²⁵Mg (10.00%)</td>
              <td>Water hardness, structural light alloys</td>
            </tr>
            <tr>
              <td>13</td>
              <td>Aluminum</td>
              <td>Al</td>
              <td>26.982</td>
              <td>²⁷Al (100% monoisotopic)</td>
              <td>Alum coagulation, structural metals</td>
            </tr>
            <tr>
              <td>14</td>
              <td>Silicon</td>
              <td>Si</td>
              <td>28.085</td>
              <td>²⁸Si (92.22%), ²⁹Si (4.69%)</td>
              <td>Silicates, zeolites, semiconductors</td>
            </tr>
            <tr>
              <td>15</td>
              <td>Phosphorus</td>
              <td>P</td>
              <td>30.974</td>
              <td>³¹P (100% monoisotopic)</td>
              <td>Phosphates, scale inhibitors, fertilizers</td>
            </tr>
            <tr>
              <td>16</td>
              <td>Sulfur</td>
              <td>S</td>
              <td>32.06</td>
              <td>³²S (94.99%), ³⁴S (4.25%)</td>
              <td>Sulfuric acid, sulfates, vulcanization</td>
            </tr>
            <tr>
              <td>17</td>
              <td>Chlorine</td>
              <td>Cl</td>
              <td>35.45</td>
              <td>³⁵Cl (75.76%), ³⁷Cl (24.24%)</td>
              <td>Bleach, water disinfection, PVC polymer</td>
            </tr>
            <tr>
              <td>19</td>
              <td>Potassium</td>
              <td>K</td>
              <td>39.098</td>
              <td>³⁹K (93.26%), ⁴¹K (6.73%)</td>
              <td>Potash fertilizers, biochemical electrolytes</td>
            </tr>
            <tr>
              <td>20</td>
              <td>Calcium</td>
              <td>Ca</td>
              <td>40.078</td>
              <td>⁴⁰Ca (96.94%), ⁴⁴Ca (2.09%)</td>
              <td>Lime softening, cement, scale formation</td>
            </tr>
            <tr>
              <td>26</td>
              <td>Iron</td>
              <td>Fe</td>
              <td>55.845</td>
              <td>⁵⁶Fe (91.75%), ⁵⁴Fe (5.85%)</td>
              <td>Ferric chloride coagulant, structural steel</td>
            </tr>
            <tr>
              <td>29</td>
              <td>Copper</td>
              <td>Cu</td>
              <td>63.546</td>
              <td>⁶³Cu (69.15%), ⁶⁵Cu (30.85%)</td>
              <td>Piping, heat exchanger tubes, algaecides</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Practical Worked Case Study: Complex Hydrate Stoichiometry</h2>
      <div class="worked-example-card">
        <h3>Chemical Engineering Case Study: Water Treatment Alum Hydrate</h3>
        <p><strong>Scenario:</strong> A municipal water treatment plant purchases solid aluminum sulfate octadecahydrate (commercial filter alum, chemical formula $\text{Al}_2(\text{SO}_4)_3 \cdot 18\text{H}_2\text{O}$) to coagulate suspended clay colloids. To optimize chemical feed inventory, determine: (1) the precise molecular weight of the hydrated salt, (2) the elemental mass percent of active trivalent aluminum ($\text{Al}^{3+}$), (3) the mass percent of water of crystallization, and (4) how many moles of active aluminum are delivered by a $1,000\text{ kg}$ bulk tote bag.</p>

        <p><strong>Step 1: Inventory the Elemental Formula Unit:</strong></p>
        <p>Expanding the formula $\text{Al}_2(\text{SO}_4)_3 \cdot 18\text{H}_2\text{O}$ yields:</p>
        <ul>
          <li>Aluminum: $2\text{ atoms} \times 26.9815386\text{ g/mol} = 53.9631\text{ g/mol}$</li>
          <li>Sulfur: $3\text{ atoms} \times 32.06\text{ g/mol} = 96.1800\text{ g/mol}$</li>
          <li>Oxygen (in sulfate): $3 \times 4 = 12\text{ atoms} \times 15.9994\text{ g/mol} = 191.9928\text{ g/mol}$</li>
          <li>Hydrogen (in water): $18 \times 2 = 36\text{ atoms} \times 1.0080\text{ g/mol} = 36.2880\text{ g/mol}$</li>
          <li>Oxygen (in water): $18 \times 1 = 18\text{ atoms} \times 15.9994\text{ g/mol} = 287.9892\text{ g/mol}$</li>
        </ul>

        <p><strong>Step 2: Sum Total Molar Mass:</strong></p>
        $$M = 53.9631 + 96.1800 + 191.9928 + 36.2880 + 287.9892 = 666.4131\text{ g/mol}$$
        <p>Anhydrous aluminum sulfate $\text{Al}_2(\text{SO}_4)_3$ contributes $342.15\text{ g/mol}$ ($51.34\%$), while the 18 hydration waters contribute $18 \times 18.0153 = 324.28\text{ g/mol}$ ($48.66\%$).</p>

        <p><strong>Step 3: Compute Elemental Mass Percent of Aluminum:</strong></p>
        $$\%_{\text{Al}} = \left(\frac{53.9631\text{ g/mol}}{666.4131\text{ g/mol}}\right) \times 100\% = 8.0975\% \approx 8.10\%\text{ w/w Al}$$

        <p><strong>Step 4: Moles and Aluminum Delivery per 1,000 kg Bulk Tote:</strong></p>
        $$n_{\text{alum}} = \frac{1,000,000\text{ g}}{666.4131\text{ g/mol}} = 1,500.57\text{ moles of alum}$$
        $$\text{Moles of Al}^{3+} = 1,500.57\text{ mol} \times 2 = 3,001.14\text{ moles of Al}^{3+}$$
        $$\text{Mass of pure Al metal} = 1,000\text{ kg} \times 0.080975 = 80.98\text{ kg of active aluminum}$$
      </div>

      <h2>Isotopic Variations and Mass Spectrometry Considerations</h2>
      <p>While standard atomic weights represent the geographic average across the Earth's crust, precise isotopic ratios can deviate slightly depending on geological origin, biological fractionation, or artificial enrichment (such as depleted uranium $^{238}\text{U}$ or heavy water $\text{D}_2\text{O}$). In high-resolution electrospray ionization mass spectrometry (ESI-MS) and matrix-assisted laser desorption (MALDI), analytical chemists differentiate between:</p>
      <ul>
        <li><strong>Average Molar Mass:</strong> Calculated using natural isotopic abundance weighted averages ($180.156\text{ g/mol}$ for glucose), representing bulk wet-chemical titrations.</li>
        <li><strong>Monoisotopic Mass:</strong> Calculated using the exact mass of the single most abundant naturally occurring stable isotope for each element ($^{12}\text{C} = 12.000000$, $^{1}\text{H} = 1.007825$, $^{16}\text{O} = 15.994915$), producing a monoisotopic mass of $180.06339\text{ Da}$ for glucose, corresponding to the dominant base peak observed in mass spectra.</li>
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
          <p class="footer-about">High-precision chemical metrology, molecular weight calculation, and elemental stoichiometry tools conforming to IUPAC and CIAAW standards.</p>
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
            <li><a href="https://www.ciaaw.org" target="_blank" rel="noopener">IUPAC Commission on Isotopic Abundances</a></li>
            <li><a href="https://webbook.nist.gov" target="_blank" rel="noopener">NIST Chemistry WebBook</a></li>
            <li><a href="https://www.bipm.org" target="_blank" rel="noopener">BIPM 2019 SI Base Units</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    // IUPAC Standard Atomic Weights (CIAAW 2021)
    const ATOMIC_WEIGHTS = {
      H: { name: "Hydrogen", mass: 1.0080 },
      He: { name: "Helium", mass: 4.0026 },
      Li: { name: "Lithium", mass: 6.94 },
      Be: { name: "Beryllium", mass: 9.0122 },
      B: { name: "Boron", mass: 10.81 },
      C: { name: "Carbon", mass: 12.011 },
      N: { name: "Nitrogen", mass: 14.007 },
      O: { name: "Oxygen", mass: 15.999 },
      F: { name: "Fluorine", mass: 18.9984 },
      Ne: { name: "Neon", mass: 20.1797 },
      Na: { name: "Sodium", mass: 22.9898 },
      Mg: { name: "Magnesium", mass: 24.305 },
      Al: { name: "Aluminum", mass: 26.9815 },
      Si: { name: "Silicon", mass: 28.085 },
      P: { name: "Phosphorus", mass: 30.9738 },
      S: { name: "Sulfur", mass: 32.06 },
      Cl: { name: "Chlorine", mass: 35.45 },
      Ar: { name: "Argon", mass: 39.948 },
      K: { name: "Potassium", mass: 39.0983 },
      Ca: { name: "Calcium", mass: 40.078 },
      Sc: { name: "Scandium", mass: 44.9559 },
      Ti: { name: "Titanium", mass: 47.867 },
      V: { name: "Vanadium", mass: 50.9415 },
      Cr: { name: "Chromium", mass: 51.9961 },
      Mn: { name: "Manganese", mass: 54.9380 },
      Fe: { name: "Iron", mass: 55.845 },
      Co: { name: "Cobalt", mass: 58.9332 },
      Ni: { name: "Nickel", mass: 58.6934 },
      Cu: { name: "Copper", mass: 63.546 },
      Zn: { name: "Zinc", mass: 65.38 },
      Ga: { name: "Gallium", mass: 69.723 },
      Ge: { name: "Germanium", mass: 72.630 },
      As: { name: "Arsenic", mass: 74.9216 },
      Se: { name: "Selenium", mass: 78.971 },
      Br: { name: "Bromine", mass: 79.904 },
      Kr: { name: "Krypton", mass: 83.798 },
      Rb: { name: "Rubidium", mass: 85.4678 },
      Sr: { name: "Strontium", mass: 87.62 },
      Y: { name: "Yttrium", mass: 88.9058 },
      Zr: { name: "Zirconium", mass: 91.224 },
      Mo: { name: "Molybdenum", mass: 95.95 },
      Ag: { name: "Silver", mass: 107.8682 },
      Cd: { name: "Cadmium", mass: 112.414 },
      In: { name: "Indium", mass: 114.818 },
      Sn: { name: "Tin", mass: 118.710 },
      Sb: { name: "Antimony", mass: 121.760 },
      Te: { name: "Tellurium", mass: 127.60 },
      I: { name: "Iodine", mass: 126.9045 },
      Xe: { name: "Xenon", mass: 131.293 },
      Cs: { name: "Cesium", mass: 132.9055 },
      Ba: { name: "Barium", mass: 137.327 },
      La: { name: "Lanthanum", mass: 138.9055 },
      Ce: { name: "Cerium", mass: 140.116 },
      W: { name: "Tungsten", mass: 183.84 },
      Pt: { name: "Platinum", mass: 195.084 },
      Au: { name: "Gold", mass: 196.9666 },
      Hg: { name: "Mercury", mass: 200.592 },
      Pb: { name: "Lead", mass: 207.2 },
      Bi: { name: "Bismuth", mass: 208.9804 },
      U: { name: "Uranium", mass: 238.0289 }
    };

    function updateCompoundPreset() {
      const p = document.getElementById("compoundPreset").value;
      if (p !== "custom") {
        document.getElementById("chemFormulaInput").value = p;
        calcMolarMass();
      }
    }

    function updateConvertMode() {
      const mode = document.getElementById("convertMode").value;
      document.getElementById("convertUnitLabel").textContent = mode === "mass_to_mol" ? "Sample Mass in Grams (g)" : "Substance in Moles (mol)";
    }

    // Formula parser with parentheses & hydrates
    function parseFormula(formulaStr) {
      let f = formulaStr.trim().replace(/\s+/g, "");
      // Handle hydrate dots e.g. CuSO4.5H2O or Al2(SO4)3·18H2O
      const parts = f.split(/[\.·]/);
      let totalCounts = {};

      for (let pIdx = 0; pIdx < parts.length; pIdx++) {
        let part = parts[pIdx];
        if (!part) continue;

        let multiplier = 1;
        // Check leading coefficient for hydrate e.g. 18H2O or 5H2O
        let matchCoeff = part.match(/^(\d+)(.*)$/);
        if (pIdx > 0 && matchCoeff) {
          multiplier = parseInt(matchCoeff[1], 10);
          part = matchCoeff[2];
        }

        let counts = parseSingleFormula(part);
        for (let elem in counts) {
          totalCounts[elem] = (totalCounts[elem] || 0) + counts[elem] * multiplier;
        }
      }
      return totalCounts;
    }

    function parseSingleFormula(s) {
      // Handles brackets and parentheses
      let stack = [{}];
      let i = 0;
      let n = s.length;

      while (i < n) {
        let char = s[i];

        if (char === "(" || char === "[" || char === "{") {
          stack.push({});
          i++;
        } else if (char === ")" || char === "]" || char === "}") {
          i++;
          // Parse following number
          let numStart = i;
          while (i < n && /\d/.test(s[i])) i++;
          let repeat = numStart === i ? 1 : parseInt(s.substring(numStart, i), 10);
          let popped = stack.pop();
          let top = stack[stack.length - 1];
          for (let el in popped) {
            top[el] = (top[el] || 0) + popped[el] * repeat;
          }
        } else if (/[A-Z]/.test(char)) {
          // Element name (1 uppercase + optional lowercase)
          let elem = char;
          i++;
          if (i < n && /[a-z]/.test(s[i])) {
            elem += s[i];
            i++;
          }
          // Parse following number
          let numStart = i;
          while (i < n && /\d/.test(s[i])) i++;
          let count = numStart === i ? 1 : parseInt(s.substring(numStart, i), 10);
          let top = stack[stack.length - 1];
          top[elem] = (top[elem] || 0) + count;
        } else {
          i++;
        }
      }

      return stack[0];
    }

    function calcMolarMass() {
      const formulaInput = document.getElementById("chemFormulaInput").value.trim();
      if (!formulaInput) return;

      let counts;
      try {
        counts = parseFormula(formulaInput);
      } catch (err) {
        alert("Invalid chemical formula syntax: " + err.message);
        return;
      }

      let totalMolarMass = 0;
      let totalAtoms = 0;
      let breakdown = [];
      let unknownElements = [];

      for (let el in counts) {
        let atomCount = counts[el];
        totalAtoms += atomCount;
        if (ATOMIC_WEIGHTS[el]) {
          let atMass = ATOMIC_WEIGHTS[el].mass;
          let elTotalMass = atomCount * atMass;
          totalMolarMass += elTotalMass;
          breakdown.push({
            symbol: el,
            name: ATOMIC_WEIGHTS[el].name,
            atWeight: atMass,
            count: atomCount,
            totalMass: elTotalMass
          });
        } else {
          unknownElements.push(el);
        }
      }

      if (unknownElements.length > 0) {
        alert("Unknown element symbol(s): " + unknownElements.join(", "));
        return;
      }

      if (totalMolarMass === 0) {
        alert("No valid chemical elements detected.");
        return;
      }

      // Sort breakdown descending by total mass
      breakdown.sort((a, b) => b.totalMass - a.totalMass);

      // Conversion calculation
      const mode = document.getElementById("convertMode").value;
      const inputVal = parseFloat(document.getElementById("convertValueInput").value) || 100.0;
      const N_A = 6.02214076e23;

      let calcMassGrams = 0;
      let calcMoles = 0;

      if (mode === "mass_to_mol") {
        calcMassGrams = inputVal;
        calcMoles = calcMassGrams / totalMolarMass;
      } else {
        calcMoles = inputVal;
        calcMassGrams = calcMoles * totalMolarMass;
      }

      const totalParticles = calcMoles * N_A;

      // Update primary UI
      document.getElementById("resMolarMassVal").textContent = totalMolarMass.toFixed(3) + " g/mol";
      document.getElementById("resMolarMassAlt").textContent = (totalMolarMass / 1000.0).toFixed(5) + " kg/mol (" + totalMolarMass.toFixed(3) + " amu / Da)";

      document.getElementById("resMolesVal").textContent = calcMoles < 0.001 ? calcMoles.toExponential(4) + " mol" : calcMoles.toFixed(4) + " mol";
      document.getElementById("resMolesAlt").textContent = (calcMoles * 1000).toFixed(2) + " mmol";

      document.getElementById("resMoleculesVal").textContent = totalParticles.toExponential(3);
      document.getElementById("resSampleMassVal").textContent = calcMassGrams >= 1000 ? (calcMassGrams / 1000).toFixed(3) + " kg" : calcMassGrams.toFixed(2) + " g";
      document.getElementById("resSampleMassAlt").textContent = (calcMassGrams / 1000).toFixed(4) + " kg (" + (calcMassGrams * 0.00220462).toFixed(4) + " lbs)";

      document.getElementById("resTotalAtomsVal").textContent = totalAtoms + " Atoms";

      // Populate Table
      const tbody = document.getElementById("elementBreakdownBody");
      tbody.innerHTML = "";

      breakdown.forEach(item => {
        const pct = (item.totalMass / totalMolarMass) * 100.0;
        const row = document.createElement("tr");
        row.innerHTML = `
          <td><strong>${item.name}</strong></td>
          <td><code>${item.symbol}</code></td>
          <td>${item.atWeight.toFixed(4)}</td>
          <td>${item.count}</td>
          <td>${item.totalMass.toFixed(3)}</td>
          <td><span style="font-weight:700;color:var(--primary);">${pct.toFixed(2)}%</span></td>
        `;
        tbody.appendChild(row);
      });
    }

    window.addEventListener("DOMContentLoaded", () => {
      calcMolarMass();
    });
  </script>
</body>
</html>
"""

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p1 = os.path.join(base_dir, "lime-dosing-calculator.html")
    p2 = os.path.join(base_dir, "molar-mass-calculator.html")

    with open(p1, "w", encoding="utf-8") as f:
        f.write(TOOL_1_HTML)
    print(f"Generated {p1}")

    with open(p2, "w", encoding="utf-8") as f:
        f.write(TOOL_2_HTML)
    print(f"Generated {p2}")

if __name__ == "__main__":
    main()
