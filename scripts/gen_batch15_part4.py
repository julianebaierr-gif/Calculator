# -*- coding: utf-8 -*-
"""
Script to generate Batch 15 Part 4 tools:
7. hydrazine-dosing-calculator.html
8. ideal-gas-law-calculator.html
"""
import os

TOOL_7_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hydrazine Dosing Calculator | Boiler Feedwater Oxygen Scavenger Sizer</title>
  <meta name="description" content="Calculate boiler feedwater hydrazine (N2H4) dosing rates, dissolved oxygen scavenging, feed pump stroke settings, residual concentration, and chemical consumption.">
  <link rel="canonical" href="https://calchub.cloud/hydrazine-dosing-calculator.html">
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
        "name": "Hydrazine Dosing Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates commercial hydrazine solution feed rates, dissolved oxygen scavenging stoichiometry, target feedwater residual, and metering pump stroke parameters for industrial boilers.",
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
            "name": "What is the stoichiometric ratio of hydrazine to dissolved oxygen in boiler water?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The chemical reaction is N2H4 + O2 -> N2 + 2H2O. Stoichiometrically, 32.05 grams of pure hydrazine react with 31.998 grams of dissolved oxygen, establishing a theoretical weight ratio of 1.0016:1 (approximately 1.0 lb pure hydrazine per 1.0 lb dissolved oxygen). In practice, an excess of 10% to 20% is dosed to maintain a protective residual of 0.02 to 0.10 mg/L."
            }
          },
          {
            "@type": "Question",
            "name": "Why is hydrazine preferred over sodium sulfite in high-pressure steam boilers?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Unlike sodium sulfite (Na2SO3), which adds dissolved solids (TDS) and decomposes above 600 psig (41 bar) into corrosive sulfur dioxide (SO2) and hydrogen sulfide (H2S), hydrazine is an all-volatile treatment (AVT). Its reaction products are pure nitrogen gas and water, adding zero dissolved solids to boiler blowdown and steam turbines."
            }
          },
          {
            "@type": "Question",
            "name": "What causes hydrazine to decompose into ammonia inside high-temperature boilers?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "At temperatures exceeding 200°C (392°F) in superheaters and steam drums, unreacted hydrazine undergoes thermal decomposition: 3N2H4 -> 4NH3 + N2. The generated volatile ammonia (NH3) vaporizes with steam, elevating the pH of condensing steam and protecting downstream condensate piping from carbonic acid grooving corrosion."
            }
          },
          {
            "@type": "Question",
            "name": "What safety precautions must be enforced when handling commercial hydrazine hydrate?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Hydrazine is classified by IARC as a Group 2A probable human carcinogen and potent volatile toxin with an OSHA permissible exposure limit (PEL) of 1.0 ppm (0.01 ppm ACGIH TLV). Facilities must enforce closed-loop chemical transfer systems (e.g., dry-break camlocks, sealed chemical metering skids, vapor recovery) and specialized PPE including butyl rubber gloves and positive-pressure respirators."
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
      <span>Hydrazine Dosing Calculator</span>
    </nav>

    <h1 class="tool-title">Hydrazine Dosing &amp; Oxygen Scavenging Calculator</h1>
    <p class="tool-subtitle">Boiler Feedwater Deoxygenation, Passivation Stoichiometry &amp; Feed Pump Sizing</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="boilerTypePreset">Boiler Operating Class &amp; Guidelines</label>
            <select id="boilerTypePreset" class="form-control" onchange="updateBoilerPreset()">
              <option value="utility_high" selected>Utility Boiler (&gt;1,500 psig / 100 bar) - ASME / EPRI AVT(R)</option>
              <option value="industrial_med">Industrial Boiler (600 - 1,500 psig / 40 - 100 bar)</option>
              <option value="package_low">Low-Pressure Package Boiler (&lt;600 psig / 40 bar)</option>
              <option value="marine_steam">Marine Steam Propulsion Plant</option>
              <option value="custom">Custom Water Quality Parameters</option>
            </select>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="feedFlowVal">Feedwater Flow Rate</label>
              <input type="number" id="feedFlowVal" class="form-control" value="1000" step="50" min="0.1">
            </div>
            <div class="form-group">
              <label for="feedFlowUnit">Flow Rate Units</label>
              <select id="feedFlowUnit" class="form-control">
                <option value="gpm" selected>Gallons / Minute (GPM)</option>
                <option value="m3h">Cubic Meters / Hour (m³/h)</option>
                <option value="mgd">Million Gallons / Day (MGD)</option>
                <option value="lbhr">Pounds / Hour Steam (lb/hr)</option>
                <option value="th">Metric Tons / Hour (t/h)</option>
              </select>
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="dissolvedO2Val">Deaerator Outlet Dissolved O₂</label>
              <input type="number" id="dissolvedO2Val" class="form-control" value="7.0" step="0.5" min="0.0">
            </div>
            <div class="form-group">
              <label for="dissolvedO2Unit">Dissolved O₂ Concentration Units</label>
              <select id="dissolvedO2Unit" class="form-control">
                <option value="ppb" selected>Micrograms / Liter (ppb, &mu;g/L)</option>
                <option value="ppm">Milligrams / Liter (ppm, mg/L)</option>
              </select>
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="targetResidualVal">Target Hydrazine Residual (N₂H₄)</label>
              <input type="number" id="targetResidualVal" class="form-control" value="25.0" step="1.0" min="0.0">
            </div>
            <div class="form-group">
              <label for="targetResidualUnit">Residual Concentration Units</label>
              <select id="targetResidualUnit" class="form-control">
                <option value="ppb" selected>Micrograms / Liter (ppb, &mu;g/L)</option>
                <option value="ppm">Milligrams / Liter (ppm, mg/L)</option>
              </select>
            </div>
          </div>

          <div class="form-group">
            <label for="chemProductSelect">Hydrazine Stock Solution Grade</label>
            <select id="chemProductSelect" class="form-control" onchange="updateProductGrade()">
              <option value="35" selected>Standard Aqueous Hydrazine (35% w/w, SG = 1.022)</option>
              <option value="54">Concentrated Hydrazine Hydrate (54.4% w/w, SG = 1.030)</option>
              <option value="64">High-Purity Hydrazine Hydrate (64% w/w, SG = 1.032)</option>
              <option value="15">Dilute Ready-to-Use Feed (15% w/w, SG = 1.010)</option>
              <option value="100">100% Anhydrous Hydrazine (Theoretical, SG = 1.004)</option>
              <option value="custom">Custom Concentration &amp; Specific Gravity</option>
            </select>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="chemStrengthVal">Active N₂H₄ Concentration (% w/w)</label>
              <input type="number" id="chemStrengthVal" class="form-control" value="35.0" step="0.5" min="1.0" max="100.0">
            </div>
            <div class="form-group">
              <label for="chemSGVal">Solution Specific Gravity (SG)</label>
              <input type="number" id="chemSGVal" class="form-control" value="1.022" step="0.005" min="0.8" max="1.5">
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="pumpMaxCapacity">Dosing Pump Max Capacity (L/h)</label>
              <input type="number" id="pumpMaxCapacity" class="form-control" value="5.0" step="0.5" min="0.1">
              <span class="field-hint">Rated maximum flow for stroke% sizing</span>
            </div>
            <div class="form-group">
              <label for="feedHoursPerDay">Operating Hours Per Day</label>
              <input type="number" id="feedHoursPerDay" class="form-control" value="24" step="1" min="1" max="24">
            </div>
          </div>

          <button type="button" class="btn btn-primary" onclick="calcHydrazineDosing()" style="width: 100%; margin-top: 15px;">Calculate Dosing &amp; Feed Rate</button>
        </div>
      </div>

      <!-- Output Results Panel -->
      <div class="results-card">
        <div class="result-box primary-result">
          <div class="result-label">Active Pure Hydrazine Dose Rate</div>
          <div id="resPureDosePpm" class="result-value">0.032 mg/L (ppm)</div>
          <div id="resPureDoseAlt" class="result-subtext">32.0 ppb (7.0 ppb O₂ scavenge + 25.0 ppb residual)</div>
        </div>

        <div class="result-grid">
          <div class="result-item">
            <span class="result-label">Feed Pump Volumetric Rate</span>
            <span id="resPumpLph" class="result-value highlight">0.021 L/h</span>
            <span id="resPumpMlMin" class="result-subtext">0.347 mL/min (0.0055 GPH)</span>
          </div>
          <div class="result-item">
            <span class="result-label">Pump Stroke Setting</span>
            <span id="resPumpStroke" class="result-value">4.2%</span>
            <span id="resPumpStrokeStatus" class="result-subtext">Of 5.0 L/h maximum pump rating</span>
          </div>
          <div class="result-item">
            <span class="result-label">Pure N₂H₄ Daily Consumption</span>
            <span id="resPureMassDay" class="result-value">0.174 kg / day</span>
            <span id="resPureMassDayLbs" class="result-subtext">0.384 lbs / day pure N₂H₄</span>
          </div>
          <div class="result-item">
            <span class="result-label">Commercial Stock Consumption</span>
            <span id="resStockMassDay" class="result-value">0.500 L / day</span>
            <span id="resStockMassDayKg" class="result-subtext">0.511 kg / day commercial 35%</span>
          </div>
          <div class="result-item">
            <span class="result-label">Magnetite Passivation Potential</span>
            <span id="resMagnetiteYield" class="result-value">1.26 kg Fe₃O₄/day</span>
            <span class="result-subtext">Theoretical rust reduction capacity</span>
          </div>
          <div class="result-item">
            <span class="result-label">Thermal NH₃ Steam Off-Gas</span>
            <span id="resAmmoniaYield" class="result-value">0.123 kg NH₃/day</span>
            <span class="result-subtext">If 100% decomposed at &gt;200°C</span>
          </div>
        </div>

        <div class="result-details" style="margin-top: 15px;">
          <p><strong>Drum Autonomy (200 L / 55 Gal Drum):</strong> <span id="resDrumAutonomy">400 Days</span></p>
          <p><strong>ASME AVT Compliance:</strong> <span id="resAsmeCompliance">Fully within EPRI AVT(R) recommended guidelines.</span></p>
        </div>
      </div>
    </div>

    <!-- 1000+ Words Engineering Body -->
    <article class="article-body">
      <h2>Engineering Fundamentals of Hydrazine Feedwater Deoxygenation</h2>
      <p>In high-pressure utility steam generators, combined-cycle heat recovery steam generators (HRSGs), and nuclear power secondary loops, dissolved oxygen ($\text{O}_2$) is the primary initiator of severe localized pitting attack on boiler tubes, economizers, and downcomers. While modern mechanical vacuum and thermal deaerators routinely strip bulk dissolved oxygen down to concentrations between $5\text{ and } 10\ \mu\text{g/L (ppb)}$, residual micro-quantities of $\text{O}_2$ cause catastrophic pinhole penetration if left chemically uninhibited under high thermal flux and pressures exceeding $40\text{ bar} \ (600\text{ psig})$.</p>

      <p>Hydrazine ($\text{N}_2\text{H}_4$), historically utilized under the <strong>All-Volatile Treatment Reducing [AVT(R)]</strong> protocol, represents the industrial benchmark chemical oxygen scavenger for high-pressure power generation. Unlike traditional low-pressure scavenging reagents such as sodium sulfite ($\text{Na}_2\text{SO}_3$) or sodium bisulfite ($\text{NaHSO}_3$), hydrazine is completely volatile. It reacts cleanly to yield inert nitrogen gas and pure water, introducing zero non-volatile dissolved mineral solids (TDS) into the boiler water. Consequently, it generates no mineral buildup on high-heat-flux boiler tubing, requires zero increase in continuous boiler blowdown, and prevents mineral carryover onto high-temperature superheaters and steam turbine blades.</p>

      <h2>Chemical Reaction Stoichiometry and Mass Balance</h2>
      <p>The primary direct deoxygenation pathway between aqueous hydrazine and dissolved oxygen is represented by the following bimolecular redox reaction:</p>

      <div class="formula-box">
        $$\text{N}_2\text{H}_4\text{ (aq)} + \text{O}_2\text{ (aq)} \longrightarrow \text{N}_2\text{ (g)} \uparrow + 2\text{H}_2\text{O}\text{ (l)}$$
      </div>

      <p>Evaluating the reaction through molecular weights ($\text{MW}_{\text{N}_2\text{H}_4} = 32.045\text{ g/mol}$, $\text{MW}_{\text{O}_2} = 31.998\text{ g/mol}$) reveals an almost perfect 1:1 stoichiometric mass relationship:</p>

      <div class="formula-box">
        $$\text{Stoichiometric Mass Ratio} = \frac{32.045\text{ g N}_2\text{H}_4}{31.998\text{ g O}_2} = 1.00147 \approx 1.00\text{ lb N}_2\text{H}_4\text{ per lb O}_2$$
      </div>

      <p>To ensure quantitative oxygen removal across dynamic load fluctuations, the total required chemical dose ($D_{\text{total}}$ in $\text{mg/L}$ or $\text{ppm}$) is calculated as the sum of the stoichiometric oxygen requirement and the target unreacted residual concentration ($C_{\text{residual}}$):</p>

      <div class="formula-box">
        $$D_{\text{total}}\text{ (mg/L)} = \left(1.0015 \times C_{\text{O}_2}\text{ (mg/L)}\right) + C_{\text{residual}}\text{ (mg/L)}$$
      </div>

      <p>For volumetric feed flow rate $Q_{\text{feed}}$ (expressed in $\text{m}^3/\text{h}$ or $\text{GPM}$), the mass consumption rate of 100% active hydrazine ($\dot{m}_{\text{pure}}$) is formulated as:</p>

      <div class="formula-box">
        $$\dot{m}_{\text{pure}}\text{ (kg/h)} = \frac{Q_{\text{feed}}\text{ (m}^3/\text{h)} \times D_{\text{total}}\text{ (mg/L)}}{1,000}$$
        $$\dot{m}_{\text{pure}}\text{ (lb/day)} = Q_{\text{feed}}\text{ (GPM)} \times 1,440\text{ min/day} \times 8.3454\text{ lb/gal} \times D_{\text{total}}\text{ (ppm)} \times 10^{-6}$$
      </div>

      <h2>Commercial Stock Solution Metering Sizing Formulas</h2>
      <p>Hydrazine is commercially supplied as an aqueous solution of hydrazine hydrate ($\text{N}_2\text{H}_4 \cdot \text{H}_2\text{O}$), most commonly standardized at $35.0\%\text{ w/w active N}_2\text{H}_4$ ($54.7\%\text{ hydrazine hydrate}$), possessing a specific gravity of $\text{SG} \approx 1.022\text{ at } 20^\circ\text{C}$. The required volumetric feed rate of commercial stock solution ($q_{\text{stock}}$ in Liters per hour or Gallons per hour) delivered by the positive-displacement metering pump is defined by:</p>

      <div class="formula-box">
        $$q_{\text{stock}}\text{ (L/h)} = \frac{\dot{m}_{\text{pure}}\text{ (kg/h)}}{\left(\frac{\%_{\text{active}}}{100}\right) \times \rho_{\text{solution}}\text{ (kg/L)}} = \frac{Q_{\text{feed}}\text{ (m}^3/\text{h)} \times D_{\text{total}}\text{ (g/m}^3)}{1,000 \times \left(\frac{\%_{\text{active}}}{100}\right) \times \text{SG}}$$
      </div>

      <p>For chemical metering skid integration, the target pump stroke percentage setting ($\text{Stroke}\%$) against the maximum rated pump capacity ($q_{\text{pump, max}}$) is given by:</p>

      <div class="formula-box">
        $$\text{Stroke}\% = \left( \frac{q_{\text{stock}}}{q_{\text{pump, max}}} \right) \times 100\%$$
      </div>
      <p>Engineering design standards dictate sizing the dosing pump so that the calculated continuous feed rate corresponds to between $30\%\text{ and } 70\%$ of the maximum stroke stroke length to ensure linear, repeatable stroke delivery without diaphragm cavitation.</p>

      <h2>Surface Metal Passivation: Formation of Protective Magnetite &amp; Cuprite</h2>
      <p>Beyond scavenging dissolved oxygen in the bulk water, hydrazine actively passivates carbon steel and copper-alloy heat transfer surfaces. Under elevated economizer and boiler water temperatures ($&gt;100^\circ\text{C} / 212^\circ\text{F}$), hydrazine chemically reduces loose, porous ferric oxide (red rust, $\text{Fe}_2\text{O}_3$) into dense, tightly adherent, protective <strong>magnetite</strong> ($\text{Fe}_3\text{O}_4$):</p>

      <div class="formula-box">
        $$6\text{Fe}_2\text{O}_3\text{ (hematite rust)} + \text{N}_2\text{H}_4 \longrightarrow 4\text{Fe}_3\text{O}_4\text{ (protective magnetite)} + \text{N}_2 \uparrow + 2\text{H}_2\text{O}$$
      </div>

      <p>Similarly, for pre-boiler piping and heat exchangers fabricated from copper-nickel brass alloys, hydrazine passivates cupric oxide ($\text{CuO}$) to form an insoluble protective cuprous oxide film ($\text{Cu}_2\text{O}$, cuprite):</p>

      <div class="formula-box">
        $$4\text{CuO} + \text{N}_2\text{H}_4 \longrightarrow 2\text{Cu}_2\text{O} + \text{N}_2 \uparrow + 2\text{H}_2\text{O}$$
      </div>
      <p>This self-healing magnetite film acts as a physical barrier preventing bare metal contact with corrosive electrolyte ions, reducing boiler iron transport rates to well below the EPRI threshold of $&lt;2.0\ \mu\text{g/L Fe}$.</p>

      <h2>Thermal Decomposition and Condensate Ammonia Chemistry</h2>
      <p>At temperatures exceeding $200^\circ\text{C}\ (392^\circ\text{F})$, such as those prevailing inside the steam drum, superheater circuits, and high-pressure steam turbines, unreacted excess hydrazine undergoes homogeneous thermal cracking into ammonia ($\text{NH}_3$) and nitrogen gas:</p>

      <div class="formula-box">
        $$3\text{N}_2\text{H}_4 \xrightarrow{&gt;200^\circ\text{C}} 4\text{NH}_3 + \text{N}_2 \uparrow$$
      </div>

      <p>Because ammonia is highly volatile (distribution coefficient $K_D \approx 10$ at $100^\circ\text{C}$), it vaporizes immediately into the steam phase and travels downstream into the surface condenser and steam extraction feedwater heaters. Upon steam condensation, ammonia hydrates to form ammonium hydroxide ($\text{NH}_4\text{OH}$):</p>

      <div class="formula-box">
        $$\text{NH}_3 + \text{H}_2\text{O} \rightleftharpoons \text{NH}_4^+ + \text{OH}^-$$
      </div>
      <p>This in-situ alkaline generation neutralizes acidic carbonic acid ($\text{H}_2\text{CO}_3$) formed by trace carbon dioxide ingress, elevating condensate pH to the target range of $9.0\text{ to } 9.6$. However, in legacy systems featuring copper-alloy condenser tubes, free ammonia concentrations exceeding $0.5\text{ mg/L}$ in the presence of oxygen promote catastrophic stress corrosion cracking (SCC) via the formation of soluble cupric-amine complexes $[\text{Cu}(\text{NH}_3)_4]^{2+}$, requiring strict limitation of hydrazine over-feed.</p>

      <h2>Boiler Water Chemistry Guidelines Benchmark Table</h2>
      <p>The table below summarizes international industry benchmark chemistry parameters across low-, medium-, and high-pressure steam utility boilers per <strong>ASME CRTD-34</strong> and <strong>EPRI Steam Chemistry Standards</strong>:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Boiler Pressure Class</th>
              <th>Operating Pressure (psig / bar)</th>
              <th>Deaerator O₂ Limit (ppb)</th>
              <th>Feedwater Residual N₂H₄ (ppb)</th>
              <th>Feedwater Target pH (at 25°C)</th>
              <th>Max Feedwater Total Iron (ppb)</th>
              <th>Treatment Protocol</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Low-Pressure Industrial</td>
              <td>0 &ndash; 300 psig (0 &ndash; 21 bar)</td>
              <td>&lt; 20 ppb</td>
              <td>100 &ndash; 250 ppb (0.1&ndash;0.25 ppm)</td>
              <td>8.5 &ndash; 9.2</td>
              <td>&lt; 100 ppb</td>
              <td>Sulfite or Hydrazine Scavenging</td>
            </tr>
            <tr>
              <td>Medium-Pressure Process</td>
              <td>301 &ndash; 900 psig (21 &ndash; 62 bar)</td>
              <td>&lt; 10 ppb</td>
              <td>50 &ndash; 150 ppb (0.05&ndash;0.15 ppm)</td>
              <td>8.8 &ndash; 9.4</td>
              <td>&lt; 20 ppb</td>
              <td>Coordinated Phosphate / AVT(R)</td>
            </tr>
            <tr>
              <td>High-Pressure Industrial</td>
              <td>901 &ndash; 1,500 psig (62 &ndash; 103 bar)</td>
              <td>&lt; 7 ppb</td>
              <td>20 &ndash; 50 ppb</td>
              <td>9.0 &ndash; 9.6</td>
              <td>&lt; 10 ppb</td>
              <td>All-Volatile Treatment Reducing [AVT(R)]</td>
            </tr>
            <tr>
              <td>Supercritical Utility / HRSG</td>
              <td>&gt; 1,500 psig (&gt; 103 bar)</td>
              <td>&lt; 5 ppb</td>
              <td>10 &ndash; 30 ppb (or 0 in AVT-O)</td>
              <td>9.2 &ndash; 9.6</td>
              <td>&lt; 2 ppb</td>
              <td>AVT(R) or Oxygenated Treatment (OT)</td>
            </tr>
            <tr>
              <td>Marine Propulsion Turbines</td>
              <td>600 &ndash; 1,200 psig (41 &ndash; 83 bar)</td>
              <td>&lt; 10 ppb</td>
              <td>30 &ndash; 100 ppb</td>
              <td>8.8 &ndash; 9.4</td>
              <td>&lt; 15 ppb</td>
              <td>Hydrazine / Morpholine Congener</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Practical Worked Case Study: Sizing Hydrazine Dosing for a 500 MW Power Plant</h2>
      <div class="worked-example-card">
        <h3>Power Generation Case Study: Coal-Fired Supercritical Feedwater Train</h3>
        <p><strong>Scenario:</strong> A $500\text{ MW}$ utility boiler operates at an economizer inlet steam production rate of $Q_{\text{feed}} = 3,000,000\text{ lb/hr}$ ($1,360,777\text{ kg/h}$, equivalent to $6,000\text{ GPM}$ or $1,361\text{ m}^3/\text{h}$). Continuous electrochemical luminescent dissolved oxygen analyzers at the deaerator storage tank drop-leg measure a mean dissolved $\text{O}_2$ concentration of $C_{\text{O}_2} = 8.0\ \mu\text{g/L (ppb)}$. Plant water chemistry guidelines mandate maintaining a protective residual hydrazine concentration of $C_{\text{residual}} = 20.0\ \mu\text{g/L (ppb)}$ at the economizer inlet to safeguard the boiler from pitting during peaking cycles. The chemical feed skid is equipped with a positive-displacement diaphragm metering pump rated at $q_{\text{pump, max}} = 10.0\text{ L/h}$. Commercial aqueous hydrazine solution is supplied at $35.0\%\text{ active N}_2\text{H}_4$ by weight ($\text{SG} = 1.022$).</p>

        <p><strong>Step 1: Compute Total Required Active Hydrazine Concentration:</strong></p>
        $$D_{\text{total}} = (1.0015 \times C_{\text{O}_2}) + C_{\text{residual}} = (1.0015 \times 8.0) + 20.0 = 8.012 + 20.0 = 28.012\ \mu\text{g/L (ppb)} = 0.028012\text{ mg/L}$$

        <p><strong>Step 2: Determine Pure Active Hydrazine Mass Delivery Rate:</strong></p>
        $$\dot{m}_{\text{pure}} = \frac{1,360.78\text{ m}^3/\text{h} \times 0.028012\text{ g/m}^3}{1,000} = 0.038118\text{ kg/h of pure N}_2\text{H}_4$$
        $$\text{Daily Pure Consumption} = 0.038118\text{ kg/h} \times 24\text{ h/day} = 0.9148\text{ kg/day pure N}_2\text{H}_4\ (2.017\text{ lb/day})$$

        <p><strong>Step 3: Calculate Commercial 35% Stock Solution Volumetric Flow Rate:</strong></p>
        <p>Accounting for the $35.0\%$ solution concentration and specific gravity ($\text{Density} = 1.022\text{ kg/L}$):</p>
        $$q_{\text{stock}} = \frac{0.038118\text{ kg/h}}{0.35 \times 1.022\text{ kg/L}} = \frac{0.038118}{0.3577} = 0.10656\text{ Liters / Hour}$$
        $$q_{\text{stock, min}} = \frac{0.10656 \times 1,000\text{ mL}}{60\text{ min}} = 1.776\text{ mL / minute}$$
        $$\text{Daily Commercial Stock Consumption} = 0.10656\text{ L/h} \times 24\text{ h} = 2.557\text{ Liters / day}$$

        <p><strong>Step 4: Metering Pump Calibration and Stroke Setting:</strong></p>
        $$\text{Stroke}\% = \left(\frac{0.10656\text{ L/h}}{10.0\text{ L/h}}\right) \times 100\% = 1.07\%$$
        <p><em>Engineering Recommendation:</em> Because operating at $1.07\%$ stroke is well below the linear accuracy threshold ($&gt;10\%$), the plant should dilute the 35% commercial hydrazine stock $1:10$ with demineralized condensate in a dedicated day tank, or install a micro-metering pump head rated at $0.5\text{ to } 1.0\text{ L/h}$ to achieve a highly reliable $20\%\text{ to } 50\%$ stroke calibration.</p>

        <p><strong>Step 5: Storage Drum Autonomy:</strong></p>
        <p>A standard $200\text{ Liter (55 gallon)}$ shipping drum of 35% hydrazine provides:</p>
        $$\text{Autonomy} = \frac{200\text{ Liters}}{2.557\text{ Liters / day}} \approx 78.2\text{ operating days (approx. 2.6 months)}$$
      </div>

      <h2>Health, Safety, and Regulatory Environmental Controls</h2>
      <p>Hydrazine is classified by the International Agency for Research on Cancer (IARC) as a <strong>Group 2A probable human carcinogen</strong> and poses severe acute inhalation, dermal, and ocular toxicity hazards. To satisfy strict OSHA, NIOSH, and EU REACH workplace safety mandates, industrial plants must adhere to the following containment standards:</p>
      <ul>
        <li><strong>Closed-Loop Chemical Transfer:</strong> Commercial hydrazine tote tanks and drums must be equipped with sealed suction wands and dry-break dry-disconnect camlock couplings. Operators must never perform open-pour decanting.</li>
        <li><strong>Vapor Recovery Systems:</strong> Day tanks and chemical pump skid head-spaces must be vented through acid scrubbers or sealed nitrogen blanketing systems to prevent occupational exposure above the OSHA Permissible Exposure Limit (PEL) of $1.0\text{ ppm}\ (1.3\text{ mg/m}^3)$ and ACGIH Threshold Limit Value (TLV) of $0.01\text{ ppm}$.</li>
        <li><strong>Emergency Spill Neutralization:</strong> Unintentional spills of aqueous hydrazine must never be neutralized with concentrated hypochlorite (which generates toxic chloramines). Instead, spills must be diluted with large volumes of water and oxidized with dilute sodium hypochlorite ($&lt;5\%$) under controlled alkaline pH, or destroyed with catalyzed hydrogen peroxide ($\text{H}_2\text{O}_2$).</li>
        <li><strong>All-Volatile Treatment Alternatives:</strong> Due to handling hazards, many modern power plants utilize substitute volatile oxygen scavengers with superior toxicological profiles, such as carbohydrazide ($(\text{NH}_2\text{NH})_2\text{CO}$, which hydrolyzes to hydrazine at boiler temperature), diethylhydroxylamine (DEHA), or methylethylketoxime (MEKO).</li>
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
          <p class="footer-about">High-precision boiler water treatment, oxygen scavenging stoichiometry, and thermal power plant engineering tools conforming to ASME and EPRI standards.</p>
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
            <li><a href="https://www.asme.org" target="_blank" rel="noopener">ASME Boiler Water Quality CRTD-34</a></li>
            <li><a href="https://www.epri.com" target="_blank" rel="noopener">EPRI Steam Turbine Chemistry</a></li>
            <li><a href="https://www.osha.gov" target="_blank" rel="noopener">OSHA Hydrazine Safety Standards</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    const BOILER_PRESETS = {
      utility_high: { o2: 7.0, o2Unit: "ppb", res: 25.0, resUnit: "ppb" },
      industrial_med: { o2: 15.0, o2Unit: "ppb", res: 80.0, resUnit: "ppb" },
      package_low: { o2: 0.05, o2Unit: "ppm", res: 0.15, resUnit: "ppm" },
      marine_steam: { o2: 10.0, o2Unit: "ppb", res: 50.0, resUnit: "ppb" },
      custom: { o2: 7.0, o2Unit: "ppb", res: 25.0, resUnit: "ppb" }
    };

    const PRODUCT_PRESETS = {
      "35": { strength: 35.0, sg: 1.022 },
      "54": { strength: 54.4, sg: 1.030 },
      "64": { strength: 64.0, sg: 1.032 },
      "15": { strength: 15.0, sg: 1.010 },
      "100": { strength: 100.0, sg: 1.004 },
      "custom": { strength: 35.0, sg: 1.022 }
    };

    function updateBoilerPreset() {
      const p = document.getElementById("boilerTypePreset").value;
      if (p !== "custom") {
        const d = BOILER_PRESETS[p];
        document.getElementById("dissolvedO2Val").value = d.o2;
        document.getElementById("dissolvedO2Unit").value = d.o2Unit;
        document.getElementById("targetResidualVal").value = d.res;
        document.getElementById("targetResidualUnit").value = d.resUnit;
      }
    }

    function updateProductGrade() {
      const g = document.getElementById("chemProductSelect").value;
      if (g !== "custom") {
        const prod = PRODUCT_PRESETS[g];
        document.getElementById("chemStrengthVal").value = prod.strength;
        document.getElementById("chemSGVal").value = prod.sg;
      }
    }

    function calcHydrazineDosing() {
      const flowVal = parseFloat(document.getElementById("feedFlowVal").value) || 0;
      const flowUnit = document.getElementById("feedFlowUnit").value;
      
      let o2Val = parseFloat(document.getElementById("dissolvedO2Val").value) || 0;
      const o2Unit = document.getElementById("dissolvedO2Unit").value;
      let o2_ppm = o2Unit === "ppb" ? o2Val / 1000.0 : o2Val;

      let resVal = parseFloat(document.getElementById("targetResidualVal").value) || 0;
      const resUnit = document.getElementById("targetResidualUnit").value;
      let res_ppm = resUnit === "ppb" ? resVal / 1000.0 : resVal;

      const strengthPct = parseFloat(document.getElementById("chemStrengthVal").value) || 35.0;
      const sg = parseFloat(document.getElementById("chemSGVal").value) || 1.022;
      const maxPumpLph = parseFloat(document.getElementById("pumpMaxCapacity").value) || 5.0;
      const opHours = parseFloat(document.getElementById("feedHoursPerDay").value) || 24;

      // Convert flow to m3/h
      let m3_per_h = 0;
      if (flowUnit === "gpm") {
        m3_per_h = flowVal * 0.227125;
      } else if (flowUnit === "m3h") {
        m3_per_h = flowVal;
      } else if (flowUnit === "mgd") {
        m3_per_h = (flowVal * 1000000 / 24) * 0.00378541;
      } else if (flowUnit === "lbhr") {
        m3_per_h = (flowVal * 0.453592) / 1000.0;
      } else if (flowUnit === "th") {
        m3_per_h = flowVal; // 1 metric ton water approx 1 m3
      }

      // Total pure active dose in mg/L (ppm)
      // Stoichiometric ratio = 1.00147
      const stoichDose_ppm = o2_ppm * 1.0015;
      const totalDose_ppm = stoichDose_ppm + res_ppm;
      const totalDose_ppb = totalDose_ppm * 1000.0;

      // Pure active N2H4 mass per hour in kg/h
      // m3/h * g/m3 / 1000 = kg/h
      const pureKgPerHour = (m3_per_h * totalDose_ppm) / 1000.0;
      const pureKgPerDay = pureKgPerHour * opHours;
      const pureLbsPerDay = pureKgPerDay * 2.20462;

      // Commercial stock solution
      // kg stock/h = pureKgPerHour / (strengthPct / 100)
      // Liters stock/h = kg stock/h / SG
      const stockKgPerHour = pureKgPerHour / (strengthPct / 100.0);
      const stockLitersPerHour = stockKgPerHour / sg;
      const stockMlPerMin = (stockLitersPerHour * 1000.0) / 60.0;
      const stockGph = stockLitersPerHour * 0.264172;

      const stockLitersPerDay = stockLitersPerHour * opHours;
      const stockKgPerDay = stockKgPerHour * opHours;

      // Pump stroke
      const strokePct = (stockLitersPerHour / maxPumpLph) * 100.0;

      // Passivation yield: 6 Fe2O3 + N2H4 -> 4 Fe3O4 + N2 + 2 H2O
      // 4 mol Fe3O4 (231.533 g/mol = 926.13 g) produced per 1 mol N2H4 (32.045 g)
      // Ratio = 926.13 / 32.045 = 28.9 g Fe3O4 per g N2H4
      // Magnetite yield theoretical = pureKgPerDay * 7.22 (if residual reacts with rust)
      const magnetiteKgDay = (res_ppm / totalDose_ppm) * pureKgPerDay * 7.22;

      // Thermal decomposition: 3 N2H4 -> 4 NH3 + N2
      // 4*17.031 = 68.124 g NH3 per 3*32.045 = 96.135 g N2H4 => 0.7086 kg NH3 / kg N2H4
      const nh3KgDay = (res_ppm / totalDose_ppm) * pureKgPerDay * 0.7086;

      // Drum autonomy (200 L drum)
      const drumDays = stockLitersPerDay > 0 ? (200.0 / stockLitersPerDay).toFixed(1) : "N/A";

      // Render outputs
      document.getElementById("resPureDosePpm").textContent = totalDose_ppm.toFixed(3) + " mg/L (ppm)";
      document.getElementById("resPureDoseAlt").textContent = totalDose_ppb.toFixed(1) + " ppb (" + (stoichDose_ppm * 1000).toFixed(1) + " ppb scavenge + " + (res_ppm * 1000).toFixed(1) + " ppb residual)";

      document.getElementById("resPumpLph").textContent = stockLitersPerHour.toFixed(3) + " L/h";
      document.getElementById("resPumpMlMin").textContent = stockMlPerMin.toFixed(2) + " mL/min (" + stockGph.toFixed(4) + " GPH)";

      document.getElementById("resPumpStroke").textContent = strokePct.toFixed(1) + "%";
      let strokeDesc = "Of " + maxPumpLph.toFixed(1) + " L/h max rating";
      if (strokePct < 10) strokeDesc += " (Caution: Below 10% linearity, consider stock dilution)";
      else if (strokePct > 90) strokeDesc += " (Warning: Above 90% capacity, pump upgrade recommended)";
      else strokeDesc += " (Optimal 10-90% linear operating range)";
      document.getElementById("resPumpStrokeStatus").textContent = strokeDesc;

      document.getElementById("resPureMassDay").textContent = pureKgPerDay.toFixed(3) + " kg / day";
      document.getElementById("resPureMassDayLbs").textContent = pureLbsPerDay.toFixed(3) + " lbs / day pure N₂H₄";

      document.getElementById("resStockMassDay").textContent = stockLitersPerDay.toFixed(2) + " L / day";
      document.getElementById("resStockMassDayKg").textContent = stockKgPerDay.toFixed(2) + " kg / day commercial " + strengthPct + "%";

      document.getElementById("resMagnetiteYield").textContent = magnetiteKgDay.toFixed(2) + " kg Fe₃O₄/day";
      document.getElementById("resAmmoniaYield").textContent = nh3KgDay.toFixed(2) + " kg NH₃/day";

      document.getElementById("resDrumAutonomy").textContent = drumDays + " Days (55 gal / 200 L standard drum)";

      let comp = "Complies with EPRI / ASME AVT(R) recommended residual range.";
      if (res_ppm > 0.10) comp = "Warning: Residual exceeds 100 ppb EPRI AVT(R) limit for high-pressure boilers. Potential ammonia carryover risk.";
      else if (res_ppm < 0.01 && o2_ppm > 0) comp = "Caution: Residual below 10 ppb may leave economizer vulnerable to transient oxygen ingress.";
      document.getElementById("resAsmeCompliance").textContent = comp;
    }

    window.addEventListener("DOMContentLoaded", () => {
      calcHydrazineDosing();
    });
  </script>
</body>
</html>
"""

TOOL_8_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ideal Gas Law Calculator | PV = nRT State Equation Solver</title>
  <meta name="description" content="Calculate pressure, volume, temperature, moles, mass, and gas density with the Ideal Gas Law equation of state (PV=nRT). Includes real gas compressibility factor Z.">
  <link rel="canonical" href="https://calchub.cloud/ideal-gas-law-calculator.html">
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
        "name": "Ideal Gas Law Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates thermodynamic pressure, volume, temperature, molar mass, substance quantity, and density using the universal ideal gas equation of state PV=nRT.",
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
            "name": "What is the universal Ideal Gas Law formula?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The ideal gas law equation of state is PV = nRT, where P is absolute pressure, V is volume, n is the number of moles, R is the universal gas constant (8.314462 J/(mol·K) or 0.082057 L·atm/(mol·K)), and T is absolute temperature in Kelvin."
            }
          },
          {
            "@type": "Question",
            "name": "How is gas density calculated from the ideal gas law?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Because moles n = m / M (mass divided by molar mass), substituting yields PV = (m/M)RT. Rearranging for density (rho = m / V) produces the direct density equation: rho = (P * M) / (R * T)."
            }
          },
          {
            "@type": "Question",
            "name": "When does the ideal gas law fail for real gases?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The ideal gas equation assumes zero molecular volume and zero intermolecular attractive/repulsive forces. It breaks down at very high pressures (where particle volume becomes significant) and low temperatures near the condensation point (where van der Waals attractive forces dominate), requiring real gas equations of state like Van der Waals or Peng-Robinson."
            }
          },
          {
            "@type": "Question",
            "name": "What is the compressibility factor Z?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The compressibility factor Z is the thermodynamic ratio of the real molar volume to the ideal molar volume: Z = PV / (nRT). For an ideal gas, Z = 1.000 exactly. Values of Z < 1 indicate dominant attractive intermolecular forces, while Z > 1 indicates dominant repulsive molecular volume exclusion."
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
      <span>Ideal Gas Law Calculator</span>
    </nav>

    <h1 class="tool-title">Ideal Gas Law Calculator (PV = nRT)</h1>
    <p class="tool-subtitle">Universal Gas State Equation, Thermodynamic Density &amp; Real Gas Compressibility</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="gasPreset">Standard Gas Species Preset</label>
            <select id="gasPreset" class="form-control" onchange="updateGasPreset()">
              <option value="air" selected>Air (Standard Dry Atmospheric, M = 28.97 g/mol)</option>
              <option value="n2">Nitrogen (N₂, M = 28.013 g/mol)</option>
              <option value="o2">Oxygen (O₂, M = 31.998 g/mol)</option>
              <option value="co2">Carbon Dioxide (CO₂, M = 44.01 g/mol)</option>
              <option value="ch4">Methane (CH₄, M = 16.04 g/mol)</option>
              <option value="he">Helium (He, M = 4.003 g/mol)</option>
              <option value="h2">Hydrogen (H₂, M = 2.016 g/mol)</option>
              <option value="ar">Argon (Ar, M = 39.948 g/mol)</option>
              <option value="steam">Water Vapor / Steam (H₂O, M = 18.015 g/mol)</option>
              <option value="custom">Custom Gas Species / Unknown Vapor</option>
            </select>
          </div>

          <div class="form-group">
            <label for="solveTarget">Thermodynamic Variable to Solve For</label>
            <select id="solveTarget" class="form-control" onchange="updateSolveInputs()">
              <option value="p" selected>Pressure (P)</option>
              <option value="v">Volume (V)</option>
              <option value="n">Amount of Substance (n, Moles)</option>
              <option value="t">Temperature (T)</option>
              <option value="m">Mass of Gas (m)</option>
              <option value="density">Gas Density (&rho;)</option>
              <option value="molar_mass">Molar Mass (M) - Vapor Density Method</option>
            </select>
          </div>

          <!-- Pressure Input -->
          <div id="pGroup" class="grid-2-col" style="display: none;">
            <div class="form-group">
              <label for="pVal">Absolute Pressure (P)</label>
              <input type="number" id="pVal" class="form-control" value="1.0" step="0.1" min="0.000001">
            </div>
            <div class="form-group">
              <label for="pUnit">Pressure Units</label>
              <select id="pUnit" class="form-control">
                <option value="atm" selected>Atmospheres (atm)</option>
                <option value="kpa">Kilopascals (kPa)</option>
                <option value="bar">Bar (bar)</option>
                <option value="psi">Pounds / sq. inch (psia)</option>
                <option value="torr">Torr / mmHg</option>
                <option value="pa">Pascals (Pa)</option>
              </select>
            </div>
          </div>

          <!-- Volume Input -->
          <div id="vGroup" class="grid-2-col">
            <div class="form-group">
              <label for="vVal">Gas Volume (V)</label>
              <input type="number" id="vVal" class="form-control" value="22.414" step="0.5" min="0.000001">
            </div>
            <div class="form-group">
              <label for="vUnit">Volume Units</label>
              <select id="vUnit" class="form-control">
                <option value="l" selected>Liters (L)</option>
                <option value="m3">Cubic Meters (m³)</option>
                <option value="ft3">Cubic Feet (ft³)</option>
                <option value="ml">Milliliters (mL)</option>
                <option value="gal">US Gallons</option>
              </select>
            </div>
          </div>

          <!-- Temperature Input -->
          <div id="tGroup" class="grid-2-col">
            <div class="form-group">
              <label for="tVal">Temperature (T)</label>
              <input type="number" id="tVal" class="form-control" value="0.0" step="1.0">
            </div>
            <div class="form-group">
              <label for="tUnit">Temperature Scale</label>
              <select id="tUnit" class="form-control">
                <option value="c" selected>Celsius (&deg;C)</option>
                <option value="k">Kelvin (K)</option>
                <option value="f">Fahrenheit (&deg;F)</option>
                <option value="r">Rankine (&deg;R)</option>
              </select>
            </div>
          </div>

          <!-- Amount / Moles Input -->
          <div id="nGroup" class="form-group">
            <label for="nVal">Amount of Substance (n)</label>
            <input type="number" id="nVal" class="form-control" value="1.0" step="0.1" min="0.000001">
            <span class="field-hint">Quantity in gram-moles (mol)</span>
          </div>

          <!-- Mass Input (when solving for mass or molar mass) -->
          <div id="mGroup" class="grid-2-col" style="display: none;">
            <div class="form-group">
              <label for="mVal">Total Gas Mass (m)</label>
              <input type="number" id="mVal" class="form-control" value="28.97" step="1.0" min="0.000001">
            </div>
            <div class="form-group">
              <label for="mUnit">Mass Units</label>
              <select id="mUnit" class="form-control">
                <option value="g" selected>Grams (g)</option>
                <option value="kg">Kilograms (kg)</option>
                <option value="lb">Pounds (lbs)</option>
              </select>
            </div>
          </div>

          <!-- Molar Mass Input -->
          <div id="molarMassGroup" class="form-group">
            <label for="molarMassVal">Molar Mass (M) (g/mol)</label>
            <input type="number" id="molarMassVal" class="form-control" value="28.97" step="0.01" min="0.5">
          </div>

          <button type="button" class="btn btn-primary" onclick="calcIdealGasLaw()" style="width: 100%; margin-top: 15px;">Solve Gas Law Equation</button>
        </div>
      </div>

      <!-- Output Results Panel -->
      <div class="results-card">
        <div class="result-box primary-result">
          <div id="resTargetLabel" class="result-label">Calculated Pressure (P)</div>
          <div id="resTargetVal" class="result-value">1.000 atm</div>
          <div id="resTargetAlt" class="result-subtext">101.325 kPa (1.013 bar / 14.696 psia)</div>
        </div>

        <div class="result-grid">
          <div class="result-item">
            <span class="result-label">Gas Density (&rho;)</span>
            <span id="resGasDensity" class="result-value highlight">1.293 g/L</span>
            <span id="resGasDensityAlt" class="result-subtext">1.293 kg/m³ (0.0807 lb/ft³)</span>
          </div>
          <div class="result-item">
            <span class="result-label">Molar Volume (Vₘ)</span>
            <span id="resMolarVolume" class="result-value">22.414 L/mol</span>
            <span class="result-subtext">Volume occupied by 1.0 mol</span>
          </div>
          <div class="result-item">
            <span class="result-label">Total Gas Mass (m)</span>
            <span id="resTotalMass" class="result-value">28.97 g</span>
            <span id="resTotalMassAlt" class="result-subtext">0.02897 kg (0.0638 lbs)</span>
          </div>
          <div class="result-item">
            <span class="result-label">Molecular Particle Count (N)</span>
            <span id="resParticleCount" class="result-value">6.022 &times; 10²³</span>
            <span class="result-subtext">Via Avogadro's Number Nₐ</span>
          </div>
          <div class="result-item">
            <span class="result-label">Ideal Compressibility (Z)</span>
            <span id="resZFactor" class="result-value">1.0000</span>
            <span class="result-subtext">PV / nRT thermodynamic ratio</span>
          </div>
          <div class="result-item">
            <span class="result-label">RMS Molecular Speed (vᵣₘₛ)</span>
            <span id="resRmsSpeed" class="result-value">484.8 m/s</span>
            <span class="result-subtext">Thermal Maxwellian velocity</span>
          </div>
        </div>

        <div class="result-details" style="margin-top: 15px;">
          <p><strong>Thermodynamic State:</strong> <span id="resThermoState">Absolute Temperature: 273.15 K (491.67 °R)</span></p>
          <p><strong>Ideal Gas Validity:</strong> <span id="resGasValidity">Conditions conform to ideal gas assumptions (&lt;2% deviation).</span></p>
        </div>
      </div>
    </div>

    <!-- 1000+ Words Engineering Body -->
    <article class="article-body">
      <h2>Thermodynamic Derivation of the Universal Ideal Gas Law</h2>
      <p>The <strong>Ideal Gas Law</strong>, also known as the universal equation of state for classical gases, provides the mathematical foundation for modern thermodynamics, mechanical power cycles, chemical reactor design, and aerodynamic propulsion. Historically formulated in 1834 by French engineer &Eacute;mile Clapeyron, the law synthesizes four empirical 17th- and 18th-century gas observations into a unified governing equation of state:</p>
      <ul>
        <li><strong>Boyle-Mariotte Law (1662):</strong> Pressure is inversely proportional to volume at constant temperature ($P \propto \frac{1}{V}$).</li>
        <li><strong>Charles-Gay-Lussac Law (1787):</strong> Volume is directly proportional to absolute thermodynamic temperature at constant pressure ($V \propto T$).</li>
        <li><strong>Avogadro's Hypothesis (1811):</strong> Equal volumes of all gases at identical temperature and pressure contain an identical number of molecules, establishing that volume is proportional to molar quantity ($V \propto n$).</li>
        <li><strong>Amontons' Law (1702):</strong> Absolute pressure is directly proportional to absolute temperature at constant volume ($P \propto T$).</li>
      </ul>

      <p>Combining these four fundamental proportionalities yields:</p>

      <div class="formula-box">
        $$V \propto \frac{n T}{P} \quad \implies \quad P V = n R T$$
      </div>

      <p>Where $P$ represents absolute static pressure ($\text{Pa}$ or $\text{N/m}^2$), $V$ denotes gas volume ($\text{m}^3$), $n$ signifies substance quantity in gram-moles ($\text{mol}$), $T$ is absolute thermodynamic temperature in Kelvin ($\text{K}$), and $R$ represents the <strong>Universal Gas Constant</strong>, defined precisely by the 2019 SI redefinition as:</p>

      <div class="formula-box">
        $$R = N_A \cdot k_B = 6.02214076 \times 10^{23}\text{ mol}^{-1} \times 1.380649 \times 10^{-23}\text{ J/K} = 8.314462618\dots\text{ J/(mol}\cdot\text{K)}$$
      </div>

      <h2>Universal Gas Constant (R) Across Dimensional Systems</h2>
      <p>Depending on the dimensional engineering units selected, $R$ adopts various numerical magnitudes:</p>
      <ul>
        <li><strong>SI Metric Standard:</strong> $R = 8.31446\text{ J/(mol}\cdot\text{K)} = 8.31446\text{ Pa}\cdot\text{m}^3/(\text{mol}\cdot\text{K}) = 8.31446\text{ kPa}\cdot\text{L}/(\text{mol}\cdot\text{K})$</li>
        <li><strong>Chemical Laboratory Standard:</strong> $R = 0.08205736\text{ L}\cdot\text{atm}/(\text{mol}\cdot\text{K})$</li>
        <li><strong>Barometric Pressure Standard:</strong> $R = 62.3637\text{ L}\cdot\text{mmHg}/(\text{mol}\cdot\text{K}) = 62.3637\text{ L}\cdot\text{Torr}/(\text{mol}\cdot\text{K})$</li>
        <li><strong>Imperial / US Customary Engineering:</strong> $R = 10.7316\text{ ft}^3\cdot\text{psi}/(\text{lbmol}\cdot^\circ\text{R}) = 1,545.35\text{ ft}\cdot\text{lbf}/(\text{lbmol}\cdot^\circ\text{R})$</li>
      </ul>

      <h2>Analytical Inversion Formulas for Gas State Properties</h2>
      <p>Any individual state variable in the ideal gas formulation can be isolated algebraically depending on the engineering unknown:</p>
      <ul>
        <li><strong>Absolute Pressure ($P$):</strong>
        $$P = \frac{n R T}{V}$$</li>
        <li><strong>Gas Volume ($V$):</strong>
        $$V = \frac{n R T}{P}$$</li>
        <li><strong>Quantity of Substance ($n$):</strong>
        $$n = \frac{P V}{R T}$$</li>
        <li><strong>Absolute Temperature ($T$):</strong>
        $$T = \frac{P V}{n R}$$</li>
      </ul>

      <h2>Gas Density, Molar Mass &amp; Vapor Density Determinations</h2>
      <p>Because the number of moles is related to total sample mass ($m$) and molecular molar mass ($M$ in $\text{g/mol}$) by $n = \frac{m}{M}$, substituting into $PV = nRT$ produces:</p>

      <div class="formula-box">
        $$P V = \left(\frac{m}{M}\right) R T \quad \implies \quad P \cdot M = \left(\frac{m}{V}\right) R T$$
      </div>

      <p>Recognizing that mass per unit volume represents volumetric gas density ($\rho = \frac{m}{V}$), we obtain the direct thermodynamic <strong>Gas Density Equation</strong>:</p>

      <div class="formula-box">
        $$\rho = \frac{P \cdot M}{R \cdot T}$$
      </div>

      <p>Rearranging for molar mass yields the classical <strong>Dumas / Victor Meyer Vapor Density Equation</strong>, widely employed in chemical characterization to determine the molecular weight of volatile unknown liquids from vaporized gas measurements:</p>

      <div class="formula-box">
        $$M = \frac{m \cdot R \cdot T}{P \cdot V} = \frac{\rho \cdot R \cdot T}{P}$$
      </div>

      <h2>Microscopic Kinetic Theory &amp; Molecular Speed (v_rms)</h2>
      <p>From the microscopic Maxwell-Boltzmann distribution of statistical mechanics, absolute temperature is a direct measure of the average translational kinetic energy of gas molecules:</p>

      <div class="formula-box">
        $$\overline{E_k} = \frac{1}{2} m_0 \overline{v^2} = \frac{3}{2} k_B T$$
      </div>

      <p>Multiplying by Avogadro's number ($N_A$) converts single-particle mass $m_0$ to molar mass $M = N_A m_0$, yielding the <strong>Root-Mean-Square (RMS) Molecular Speed</strong> ($v_{\text{rms}}$):</p>

      <div class="formula-box">
        $$v_{\text{rms}} = \sqrt{\frac{3 R T}{M}}$$
      </div>
      <p>For example, at standard room temperature ($298.15\text{ K}$), lighter gas molecules such as Hydrogen ($\text{H}_2, M = 2.016\text{ g/mol}$) travel at an average thermal speed of $1,920\text{ m/s}$ (nearly Mach 5.6), whereas heavier molecules such as Carbon Dioxide ($\text{CO}_2, M = 44.01\text{ g/mol}$) travel at a leisurely $411\text{ m/s}$.</p>

      <h2>Real Gas Deviations: Compressibility Factor (Z) &amp; Van der Waals Correction</h2>
      <p>The ideal gas law relies strictly on two theoretical postulates:</p>
      <ol>
        <li>Gas molecules are infinitesimally small dimensionless point masses occupying zero volume ($V_{\text{molecules}} = 0$).</li>
        <li>No attractive or repulsive intermolecular forces exist between gas molecules ($F_{\text{intermolecular}} = 0$).</li>
      </ol>

      <p>In real industrial processes involving high pressures ($P &gt; 10\text{ bar}$) or low temperatures near condensation, real gases deviate markedly. The degree of non-ideality is quantified by the <strong>Compressibility Factor ($Z$)</strong>:</p>

      <div class="formula-box">
        $$Z = \frac{P V_m}{R T} = \frac{P V}{n R T}$$
      </div>
      <p>For an ideal gas, $Z = 1.000$ exactly across all conditions. When attractive van der Waals dipole-dipole forces dominate (moderate pressure, low temperature), molecules pull closer together than ideal behavior predicts, resulting in $Z &lt; 1.0$. At extreme pressures ($&gt;100\text{ bar}$), molecular co-volume exclusion becomes dominant, resisting compression and causing $Z &gt; 1.0$.</p>

      <p>To correct for non-ideality, Dutch physicist Johannes Diderik van der Waals formulated his modified equation of state:</p>

      <div class="formula-box">
        $$\left( P + \frac{a n^2}{V^2} \right) (V - n b) = n R T$$
      </div>
      <p>Where constant $a$ accounts for intermolecular attractive forces (reducing observed wall pressure), and constant $b$ accounts for the physical co-volume occupied by the molecules themselves.</p>

      <h2>Gas Physical Constants Reference Table</h2>
      <p>The table below summarizes molecular molar masses, critical temperatures ($T_c$), critical pressures ($P_c$), and Van der Waals constants across representative industrial and atmospheric gases per NIST Chemistry WebBook:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Gas Species</th>
              <th>Formula</th>
              <th>Molar Mass (g/mol)</th>
              <th>Critical Temp T_c (K)</th>
              <th>Critical Pressure P_c (bar)</th>
              <th>Van der Waals a (bar·L²/mol²)</th>
              <th>Van der Waals b (L/mol)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Standard Atmospheric Air</td>
              <td>Dry Mix</td>
              <td>28.97</td>
              <td>132.5 K</td>
              <td>37.7 bar</td>
              <td>1.358</td>
              <td>0.0364</td>
            </tr>
            <tr>
              <td>Nitrogen</td>
              <td>N₂</td>
              <td>28.013</td>
              <td>126.2 K</td>
              <td>33.9 bar</td>
              <td>1.370</td>
              <td>0.0387</td>
            </tr>
            <tr>
              <td>Oxygen</td>
              <td>O₂</td>
              <td>31.998</td>
              <td>154.6 K</td>
              <td>50.4 bar</td>
              <td>1.382</td>
              <td>0.0319</td>
            </tr>
            <tr>
              <td>Carbon Dioxide</td>
              <td>CO₂</td>
              <td>44.010</td>
              <td>304.2 K</td>
              <td>73.8 bar</td>
              <td>3.658</td>
              <td>0.0429</td>
            </tr>
            <tr>
              <td>Methane</td>
              <td>CH₄</td>
              <td>16.043</td>
              <td>190.6 K</td>
              <td>46.0 bar</td>
              <td>2.303</td>
              <td>0.0431</td>
            </tr>
            <tr>
              <td>Helium</td>
              <td>He</td>
              <td>4.003</td>
              <td>5.19 K</td>
              <td>2.27 bar</td>
              <td>0.0346</td>
              <td>0.0238</td>
            </tr>
            <tr>
              <td>Hydrogen</td>
              <td>H₂</td>
              <td>2.016</td>
              <td>33.2 K</td>
              <td>13.0 bar</td>
              <td>0.245</td>
              <td>0.0265</td>
            </tr>
            <tr>
              <td>Argon</td>
              <td>Ar</td>
              <td>39.948</td>
              <td>150.9 K</td>
              <td>48.7 bar</td>
              <td>1.355</td>
              <td>0.0320</td>
            </tr>
            <tr>
              <td>Water Vapor (Steam)</td>
              <td>H₂O</td>
              <td>18.015</td>
              <td>647.1 K</td>
              <td>220.6 bar</td>
              <td>5.536</td>
              <td>0.0305</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Practical Worked Case Study: Sizing a Compressed Nitrogen Gas Cylinder</h2>
      <div class="worked-example-card">
        <h3>Mechanical Engineering Case Study: High-Pressure Industrial Gas Storage</h3>
        <p><strong>Scenario:</strong> A semiconductor manufacturing facility utilizes a standard $50.0\text{ Liter}$ water-capacity steel gas cylinder to store high-purity dry Nitrogen gas ($\text{N}_2, M = 28.013\text{ g/mol}$) at an ambient manifold room temperature of $20.0^\circ\text{C}$ ($293.15\text{ K}$). The cylinder is charged to an absolute operating pressure of $P = 200.0\text{ bar}$ ($20.0\text{ MPa}$, equivalent to $197.38\text{ atm}$ or $2,900.8\text{ psia}$). Determine: (1) the molar quantity of nitrogen contained under ideal gas assumptions, (2) the total physical mass of nitrogen stored, (3) the expanded usable volume of nitrogen gas available at Standard Ambient Temperature and Pressure (SATP: $1.0\text{ bar}$, $25^\circ\text{C}$), and (4) compare the ideal gas prediction with the real gas compressibility factor $Z$ for nitrogen at $200\text{ bar}$.</p>

        <p><strong>Step 1: Compute Molar Quantity via Ideal Gas Law:</strong></p>
        <p>Converting parameters to consistent SI metric units: $P = 200.0\text{ bar} = 20,000\text{ kPa}$, $V = 50.0\text{ L} = 0.050\text{ m}^3$, $T = 293.15\text{ K}$, $R = 8.31446\text{ kPa}\cdot\text{L}/(\text{mol}\cdot\text{K})$:</p>
        $$n = \frac{P \cdot V}{R \cdot T} = \frac{20,000\text{ kPa} \times 50.0\text{ L}}{8.31446\text{ kPa}\cdot\text{L}/(\text{mol}\cdot\text{K}) \times 293.15\text{ K}} = \frac{1,000,000}{2,437.38} = 410.28\text{ moles}$$

        <p><strong>Step 2: Calculate Stored Physical Gas Mass:</strong></p>
        $$m = n \times M = 410.28\text{ mol} \times 28.013\text{ g/mol} = 11,493\text{ grams} = 11.493\text{ kg}\ (25.34\text{ lbs})$$
        <p>Volumetric density inside the pressurized cylinder is:</p>
        $$\rho_{\text{cylinder}} = \frac{11.493\text{ kg}}{0.050\text{ m}^3} = 229.86\text{ kg/m}^3$$

        <p><strong>Step 3: Calculate Expanded Usable Volume at SATP ($P_2 = 1.0\text{ bar}$, $T_2 = 298.15\text{ K}$):</strong></p>
        $$V_2 = \frac{n \cdot R \cdot T_2}{P_2} = \frac{410.28\text{ mol} \times 0.083145\text{ bar}\cdot\text{L}/(\text{mol}\cdot\text{K}) \times 298.15\text{ K}}{1.0\text{ bar}} = 10,171\text{ Liters} = 10.17\text{ m}^3$$
        <p>The cylinder provides an expansion expansion ratio of $10,171 / 50 = 203.4 : 1$.</p>

        <p><strong>Step 4: Real Gas Non-Ideality Comparison ($Z$-factor):</strong></p>
        <p>At $P = 200\text{ bar}$ and $T = 293.15\text{ K}$, the NIST thermodynamic tables report the real compressibility factor of pure Nitrogen is $Z \approx 1.042$ (repulsive molecular volume effects exceed attractive dispersion forces by $4.2\%$). The actual moles contained in the cylinder are:</p>
        $$n_{\text{real}} = \frac{n_{\text{ideal}}}{Z} = \frac{410.28}{1.042} = 393.74\text{ moles}$$
        $$m_{\text{real}} = 393.74 \times 28.013 = 11.030\text{ kg}$$
        <p><em>Engineering Takeaway:</em> The ideal gas law over-predicts the stored mass and usable gas volume by approximately $4.2\%$ ($463\text{ grams}$ of $\text{N}_2$), underscoring the critical necessity of compressibility factors in high-pressure gas custody transfer.</p>
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
          <p class="footer-about">High-precision chemical thermodynamics, gas law state equations, and kinetic gas theory tools conforming to IUPAC and NIST standards.</p>
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
            <li><a href="https://webbook.nist.gov" target="_blank" rel="noopener">NIST Chemistry WebBook</a></li>
            <li><a href="https://www.iupac.org" target="_blank" rel="noopener">IUPAC Physical Chemistry Standards</a></li>
            <li><a href="https://www.bipm.org" target="_blank" rel="noopener">BIPM SI Fundamental Constants</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    const GAS_PRESETS = {
      air: 28.97,
      n2: 28.013,
      o2: 31.998,
      co2: 44.01,
      ch4: 16.04,
      he: 4.003,
      h2: 2.016,
      ar: 39.948,
      steam: 18.015,
      custom: 28.97
    };

    function updateGasPreset() {
      const g = document.getElementById("gasPreset").value;
      if (g !== "custom") {
        document.getElementById("molarMassVal").value = GAS_PRESETS[g];
      }
    }

    function updateSolveInputs() {
      const target = document.getElementById("solveTarget").value;
      document.getElementById("pGroup").style.display = target === "p" ? "none" : "grid";
      document.getElementById("vGroup").style.display = target === "v" ? "none" : "grid";
      document.getElementById("tGroup").style.display = target === "t" ? "none" : "grid";
      document.getElementById("nGroup").style.display = (target === "n" || target === "molar_mass" || target === "m") ? "none" : "block";
      document.getElementById("mGroup").style.display = (target === "molar_mass" || target === "m") ? "grid" : "none";
      document.getElementById("molarMassGroup").style.display = (target === "molar_mass") ? "none" : "block";
    }

    function calcIdealGasLaw() {
      const target = document.getElementById("solveTarget").value;
      const R_SI = 8.314462618; // J / (mol·K) = Pa·m3 / (mol·K)

      // Get Molar Mass
      let M = parseFloat(document.getElementById("molarMassVal").value) || 28.97; // g/mol
      let M_kg = M / 1000.0; // kg/mol

      // Convert Pressure to Pa
      let pVal = parseFloat(document.getElementById("pVal").value) || 1.0;
      let pUnit = document.getElementById("pUnit").value;
      let P_pa = 101325;
      if (target !== "p") {
        if (pUnit === "atm") P_pa = pVal * 101325;
        else if (pUnit === "kpa") P_pa = pVal * 1000;
        else if (pUnit === "bar") P_pa = pVal * 100000;
        else if (pUnit === "psi") P_pa = pVal * 6894.757;
        else if (pUnit === "torr") P_pa = pVal * 133.3224;
        else if (pUnit === "pa") P_pa = pVal;
      }

      // Convert Volume to m3
      let vVal = parseFloat(document.getElementById("vVal").value) || 22.414;
      let vUnit = document.getElementById("vUnit").value;
      let V_m3 = 0.022414;
      if (target !== "v") {
        if (vUnit === "l") V_m3 = vVal * 0.001;
        else if (vUnit === "m3") V_m3 = vVal;
        else if (vUnit === "ft3") V_m3 = vVal * 0.0283168;
        else if (vUnit === "ml") V_m3 = vVal * 1e-6;
        else if (vUnit === "gal") V_m3 = vVal * 0.00378541;
      }

      // Convert Temperature to Kelvin
      let tVal = parseFloat(document.getElementById("tVal").value) || 0.0;
      let tUnit = document.getElementById("tUnit").value;
      let T_k = 273.15;
      if (target !== "t") {
        if (tUnit === "c") T_k = tVal + 273.15;
        else if (tUnit === "k") T_k = tVal;
        else if (tUnit === "f") T_k = (tVal - 32) * 5/9 + 273.15;
        else if (tUnit === "r") T_k = tVal * 5/9;
      }
      if (T_k <= 0) { alert("Absolute temperature must be above absolute zero (0 K)"); return; }

      // Get Moles or Mass
      let n_moles = parseFloat(document.getElementById("nVal").value) || 1.0;
      if (target === "m" || target === "molar_mass") {
        let mVal = parseFloat(document.getElementById("mVal").value) || 28.97;
        let mUnit = document.getElementById("mUnit").value;
        let m_grams = mVal;
        if (mUnit === "kg") m_grams = mVal * 1000;
        else if (mUnit === "lb") m_grams = mVal * 453.592;
        if (target === "molar_mass") {
          // n will be calculated via PV = nRT
        } else {
          n_moles = m_grams / M;
        }
      }

      let resLabel = "";
      let resVal = "";
      let resAlt = "";

      if (target === "p") {
        P_pa = (n_moles * R_SI * T_k) / V_m3;
        const p_atm = P_pa / 101325;
        const p_kpa = P_pa / 1000;
        const p_bar = P_pa / 100000;
        const p_psi = P_pa / 6894.757;
        resLabel = "Calculated Pressure (P)";
        resVal = p_atm < 0.01 ? p_atm.toExponential(3) + " atm" : p_atm.toFixed(3) + " atm";
        resAlt = p_kpa.toFixed(2) + " kPa (" + p_bar.toFixed(3) + " bar / " + p_psi.toFixed(2) + " psia)";
      } else if (target === "v") {
        V_m3 = (n_moles * R_SI * T_k) / P_pa;
        const v_l = V_m3 * 1000;
        const v_ft3 = V_m3 / 0.0283168;
        resLabel = "Calculated Volume (V)";
        resVal = v_l >= 1000 ? (v_l / 1000).toFixed(3) + " m³" : v_l.toFixed(3) + " Liters";
        resAlt = v_l.toFixed(2) + " L (" + v_ft3.toFixed(2) + " ft³ / " + (v_l * 0.264172).toFixed(2) + " US gal)";
      } else if (target === "n") {
        n_moles = (P_pa * V_m3) / (R_SI * T_k);
        resLabel = "Amount of Substance (n)";
        resVal = n_moles < 0.01 ? n_moles.toExponential(4) + " mol" : n_moles.toFixed(4) + " mol";
        resAlt = (n_moles * M).toFixed(2) + " grams (" + (n_moles * M / 1000).toFixed(4) + " kg)";
      } else if (target === "t") {
        T_k = (P_pa * V_m3) / (n_moles * R_SI);
        const t_c = T_k - 273.15;
        const t_f = t_c * 9/5 + 32;
        resLabel = "Calculated Temperature (T)";
        resVal = t_c.toFixed(2) + " °C";
        resAlt = T_k.toFixed(2) + " K (" + t_f.toFixed(2) + " °F / " + (T_k * 1.8).toFixed(2) + " °R)";
      } else if (target === "m") {
        n_moles = (P_pa * V_m3) / (R_SI * T_k);
        const mass_g = n_moles * M;
        resLabel = "Calculated Gas Mass (m)";
        resVal = mass_g >= 1000 ? (mass_g / 1000).toFixed(3) + " kg" : mass_g.toFixed(2) + " grams";
        resAlt = (mass_g * 0.00220462).toFixed(3) + " lbs (" + n_moles.toFixed(3) + " moles)";
      } else if (target === "density") {
        const rho_kg_m3 = (P_pa * M_kg) / (R_SI * T_k);
        resLabel = "Calculated Gas Density (ρ)";
        resVal = rho_kg_m3.toFixed(3) + " g/L (kg/m³)";
        resAlt = (rho_kg_m3 * 0.062428).toFixed(4) + " lb/ft³";
      } else if (target === "molar_mass") {
        let mVal = parseFloat(document.getElementById("mVal").value) || 28.97;
        let mUnit = document.getElementById("mUnit").value;
        let m_grams = mVal;
        if (mUnit === "kg") m_grams = mVal * 1000;
        else if (mUnit === "lb") m_grams = mVal * 453.592;
        n_moles = (P_pa * V_m3) / (R_SI * T_k);
        M = m_grams / n_moles;
        M_kg = M / 1000.0;
        resLabel = "Calculated Molar Mass (M)";
        resVal = M.toFixed(2) + " g/mol";
        resAlt = "Sample contains " + n_moles.toFixed(4) + " moles in " + m_grams.toFixed(2) + " g";
      }

      // Supplementary outputs
      const totalMass_g = n_moles * M;
      const density_kg_m3 = (P_pa * M_kg) / (R_SI * T_k);
      const molarVol_L = (R_SI * T_k) / (P_pa / 1000); // L / mol
      const particles = n_moles * 6.02214076e23;
      const v_rms = Math.sqrt((3 * R_SI * T_k) / M_kg);

      document.getElementById("resTargetLabel").textContent = resLabel;
      document.getElementById("resTargetVal").textContent = resVal;
      document.getElementById("resTargetAlt").textContent = resAlt;

      document.getElementById("resGasDensity").textContent = density_kg_m3.toFixed(3) + " g/L";
      document.getElementById("resGasDensityAlt").textContent = density_kg_m3.toFixed(3) + " kg/m³ (" + (density_kg_m3 * 0.062428).toFixed(4) + " lb/ft³)";

      document.getElementById("resMolarVolume").textContent = molarVol_L.toFixed(3) + " L/mol";

      document.getElementById("resTotalMass").textContent = totalMass_g >= 1000 ? (totalMass_g / 1000).toFixed(3) + " kg" : totalMass_g.toFixed(2) + " g";
      document.getElementById("resTotalMassAlt").textContent = (totalMass_g / 1000).toFixed(4) + " kg (" + (totalMass_g * 0.00220462).toFixed(3) + " lbs)";

      document.getElementById("resParticleCount").textContent = particles.toExponential(3);
      document.getElementById("resZFactor").textContent = "1.0000";
      document.getElementById("resRmsSpeed").textContent = v_rms.toFixed(1) + " m/s";

      document.getElementById("resThermoState").textContent = "P = " + (P_pa / 101325).toFixed(3) + " atm | V = " + (V_m3 * 1000).toFixed(2) + " L | T = " + T_k.toFixed(2) + " K (" + (T_k - 273.15).toFixed(1) + " °C)";

      let valMsg = "Conditions conform to ideal gas assumptions (<2% error).";
      const p_bar = P_pa / 100000;
      if (p_bar > 20 || T_k < 150) {
        valMsg = "Warning: High pressure (" + p_bar.toFixed(1) + " bar) or low temperature introduces non-ideal real gas deviations. Consider Van der Waals or Redlich-Kwong EOS.";
      }
      document.getElementById("resGasValidity").textContent = valMsg;
    }

    window.addEventListener("DOMContentLoaded", () => {
      calcIdealGasLaw();
    });
  </script>
</body>
</html>
"""

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p7 = os.path.join(base_dir, "hydrazine-dosing-calculator.html")
    p8 = os.path.join(base_dir, "ideal-gas-law-calculator.html")

    with open(p7, "w", encoding="utf-8") as f:
        f.write(TOOL_7_HTML)
    print(f"Generated {p7}")

    with open(p8, "w", encoding="utf-8") as f:
        f.write(TOOL_8_HTML)
    print(f"Generated {p8}")

if __name__ == "__main__":
    main()
