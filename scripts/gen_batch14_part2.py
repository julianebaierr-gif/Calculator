# -*- coding: utf-8 -*-
"""
Script to generate Batch 14 Part 2 tools:
3. alum-dosing-calculator.html
4. boyles-law-calculator.html
"""
import os

TOOL_3_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Alum Dosing Calculator | Water Treatment Coagulation &amp; Feed Rate</title>
  <meta name="description" content="Calculate liquid and dry aluminum sulfate (alum) dosing rates, chemical feed pump output in mL/min and GPH, alkalinity consumption, and sludge production.">
  <link rel="canonical" href="https://calchub.cloud/alum-dosing-calculator.html">
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
        "name": "Alum Dosing Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates dry and commercial liquid aluminum sulfate coagulant feed rates, metering pump stroke calibration, stoichiometric alkalinity destruction, and coagulation solids per AWWA standards.",
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
            "name": "How is dry alum feed rate calculated from raw water flow and dosage?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The dry chemical feed rate in pounds per day is determined by the standard waterworks formula: Feed Rate (lb/day) = Flow (MGD) * Target Dose (mg/L) * 8.34 lb/gal. In metric units, Mass Rate (kg/day) = Flow (m3/day) * Target Dose (g/m3) / 1,000."
            }
          },
          {
            "@type": "Question",
            "name": "How do you convert dry alum dosage to commercial liquid alum pump feed rate?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Commercial liquid alum typically has a specific gravity of 1.33 and contains approximately 48.5% dry aluminum sulfate by weight, yielding about 5.4 lbs of dry alum per gallon of solution. The liquid feed rate in gallons per day is: GPD = (Pounds Dry Alum per Day) / (5.4 lbs dry alum/gal). To calibrate a diaphragm metering pump, convert GPD to mL/min by multiplying by 2.6288."
            }
          },
          {
            "@type": "Question",
            "name": "How much natural alkalinity does alum coagulation consume?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Stoichiometrically, each 1.0 mg/L of commercial dry alum (Al2(SO4)3 * 14H2O) added consumes approximately 0.505 mg/L of natural alkalinity as calcium carbonate (CaCO3). If raw water alkalinity falls below 30-45 mg/L as CaCO3, the pH will plunge below the optimum sweep floc range (pH 5.8-7.2), requiring supplemental dosing of hydrated lime or caustic soda."
            }
          },
          {
            "@type": "Question",
            "name": "What is the optimal pH window for aluminum sulfate coagulation?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The optimum pH range for sweep floc coagulation with alum is 5.8 to 7.2. Below pH 5.5, aluminum remains partially dissolved as trivalent Al3+ and hydrated cations, leading to elevated residual aluminum in finished water. Above pH 7.8, the amphoteric aluminate ion Al(OH)4- forms, which increases solubility and causes turbidity carryover."
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
      <span>Alum Dosing Calculator</span>
    </nav>

    <h1 class="tool-title">Alum Dosing &amp; Coagulation Feed Calculator</h1>
    <p class="tool-subtitle">Water Works Coagulant Feed Sizing, Pump Calibration (mL/min, GPH) &amp; Alkalinity Stoichiometry</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="alumForm">Alum Chemical Product Form</label>
            <select id="alumForm" class="form-control" onchange="toggleAlumForm()">
              <option value="liquid" selected>Commercial Liquid Alum (48.5% dry basis, SG = 1.33, ~5.4 lb dry/gal)</option>
              <option value="dry">Dry Granular Alum (Al₂(SO₄)₃·14H₂O, 100% active basis)</option>
              <option value="custom">Custom Liquid Solution (Specific Gravity &amp; Concentration)</option>
            </select>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="flowUnit">Raw Water Flow Units</label>
              <select id="flowUnit" class="form-control" onchange="toggleFlowUnits()">
                <option value="mgd" selected>MGD (Million Gallons per Day)</option>
                <option value="gpm">GPM (Gallons per Minute)</option>
                <option value="m3h">m³/h (Cubic Meters per Hour)</option>
                <option value="m3d">m³/day (Cubic Meters per Day)</option>
                <option value="lps">L/s (Liters per Second)</option>
              </select>
            </div>
            <div class="form-group">
              <label for="rawFlow" id="flowLabel">Raw Water Plant Flow (MGD)</label>
              <input type="number" id="rawFlow" class="form-control" value="6.0" step="0.1" min="0.01">
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="targetDose">Jar Test Coagulant Dose (mg/L or ppm dry)</label>
              <input type="number" id="targetDose" class="form-control" value="25.0" step="0.5" min="0.1">
              <span class="field-hint">Optimized dosage from jar testing (typically 10&ndash;60 mg/L)</span>
            </div>
            <div class="form-group">
              <label for="rawAlkalinity">Raw Water Alkalinity (mg/L as CaCO₃)</label>
              <input type="number" id="rawAlkalinity" class="form-control" value="55" step="1" min="0">
              <span class="field-hint">Total alkalinity before coagulant addition</span>
            </div>
          </div>

          <div id="customAlumParams" class="grid-2-col" style="display:none;">
            <div class="form-group">
              <label for="liquidSG">Solution Specific Gravity (SG)</label>
              <input type="number" id="liquidSG" class="form-control" value="1.33" step="0.01" min="1.0">
            </div>
            <div class="form-group">
              <label for="solStrength">Solution Strength (% dry alum by wt)</label>
              <input type="number" id="solStrength" class="form-control" value="48.5" step="0.5" min="1" max="100">
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="pumpTubes">Chemical Feed Pump Count</label>
              <input type="number" id="pumpTubes" class="form-control" value="1" step="1" min="1" max="6">
            </div>
            <div class="form-group">
              <label for="rawTSS">Raw Water Suspended Solids / Turbidity (NTU/mg/L)</label>
              <input type="number" id="rawTSS" class="form-control" value="20" step="1" min="0">
              <span class="field-hint">Used for coagulant sludge production modeling</span>
            </div>
          </div>

          <button type="button" class="btn btn-primary" onclick="calcAlumDosing()">Calculate Coagulant Feed &amp; Stoichiometry</button>
        </div>

        <div id="alumResults" class="results-box" style="display:none;margin-top:1.5rem;">
          <h3 class="results-title">Coagulant Feed Sizing &amp; Dosing Summary</h3>
          <div class="result-grid">
            <div class="result-card">
              <div class="result-label">Dry Alum Mass Rate</div>
              <div class="result-value highlight" id="resDryMass">--</div>
              <div class="result-subtext" id="resDryMassAlt">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Liquid Feed Rate (Per Pump)</div>
              <div class="result-value highlight" id="resPumpCalibration">--</div>
              <div class="result-subtext" id="resPumpCalibrationAlt">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Commercial Liquid Volume</div>
              <div class="result-value" id="resLiquidVol">--</div>
              <div class="result-subtext" id="resLiquidVolDay">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Residual Alkalinity</div>
              <div class="result-value" id="resResidAlk">--</div>
              <div class="result-subtext" id="resAlkStatus">--</div>
            </div>
          </div>

          <div class="result-details" style="margin-top:1rem;padding:1rem;background:var(--card-bg);border-radius:6px;border:1px solid var(--border-light);">
            <h4 style="margin-top:0;">Chemical Consumption &amp; Sludge Diagnostics</h4>
            <ul style="margin-bottom:0;line-height:1.7;">
              <li><strong>Alkalinity Consumed:</strong> <span id="resConsumedAlk">--</span></li>
              <li><strong>Supplemental Lime/Caustic Need:</strong> <span id="resSupplNeed">--</span></li>
              <li><strong>Estimated Dry Sludge Production:</strong> <span id="resDrySludge">--</span></li>
              <li><strong>Daily Bulk Chemical Storage Usage:</strong> <span id="resStorageUsage">--</span></li>
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
            <li><a href="chlorine-dosing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Chlorine Dosing Calculator</a></li>
            <li><a href="chemical-dosing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Chemical Dosing Rate Calculator</a></li>
            <li><a href="pipe-sizing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Pipe Sizing &amp; Water Flow</a></li>
            <li><a href="cooling-load-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Cooling Load (HVAC) Sizing</a></li>
          </ul>
          <div style="margin-top:1.25rem;padding-top:1rem;border-top:1px solid var(--border-light);">
            <a href="chemical.html" class="sidebar-category-link">View All Chemical Calculators &rarr;</a>
          </div>
        </div>
      </aside>
    </div>

    <!-- Technical Educational Article Body (1000+ Words) -->
    <article class="article-body">
      <h2>Principles of Coagulation Chemistry Using Aluminum Sulfate</h2>
      <p>Coagulation and flocculation represent the primary physicochemical barrier in surface water and wastewater clarification facilities. Natural raw waters contain suspended colloidal solids, clay minerals, microorganisms, and natural organic matter (NOM) that carry negative surface electrostatic charges (&zeta;-potential typically between &minus;15 mV and &minus;30 mV). Mutual electrical repulsion prevents these microscopic particles from aggregating, maintaining a permanent colloidal suspension.</p>

      <p>Aluminum sulfate—commonly referred to in municipal water engineering as <strong>alum</strong> with empirical formula $\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O}$ (molecular weight approximately $594.4\text{ g/mol}$)—acts as a multi-functional trivalent coagulant. When introduced into raw water, aluminum ions undergo instantaneous hydration and hydrolysis, generating a dynamic distribution of monomeric, polymeric, and amorphous precipitate species governed by pH, temperature, and mixing energy.</p>

      <h2>Two Primary Coagulation Mechanisms: Charge Neutralization vs. Sweep Floc</h2>
      <p>Depending on the coagulant dosage and aqueous pH regime, alum functions through two fundamental pathways:</p>
      <ul>
        <li><strong>Charge Neutralization / Adsorption (Lower Dose, pH 4.5 &ndash; 5.5):</strong> At acidic pH, positively charged hydrolyzed aluminum monomers and polymers (such as $\text{AlOH}^{2+}$, $\text{Al}_2(\text{OH})_2^{4+}$, and the tridecameric Keggin ion $\text{Al}_{13}\text{O}_4(\text{OH})_{24}^{7+}$) adsorb onto negatively charged colloidal surfaces, compressing the electrical double layer and collapsing the zeta potential toward zero. Under-dosing leaves particles negatively charged; over-dosing causes charge reversal and restabilization.</li>
        <li><strong>Sweep Floc Coagulation (Higher Dose, pH 5.8 &ndash; 7.2):</strong> At municipal operating pH and typical dosages (&gt;15 mg/L), alum rapidly supersaturates with respect to amorphous aluminum hydroxide precipitate:
        $$\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O} + 6\text{HCO}_3^- \longrightarrow 2\text{Al(OH)}_3\downarrow + 3\text{SO}_4^{2-} + 6\text{CO}_2 + 14\text{H}_2\text{O}$$
        The resulting sticky, volumetric $\text{Al(OH)}_3$ gel sweeps through the water column, physically entrapping suspended silts, algae, and colloidal color compounds as it settles.</li>
      </ul>

      <h2>Governing Mathematical Formulas for Alum Feed Systems</h2>
      <p>The calculation framework translates raw water volumetric flow rates ($Q$) and jar-tested target chemical dosages ($C_{\text{dose}}$) into physical pump feed rates and storage consumption.</p>

      <p>The daily dry chemical demand in US standard waterworks units is:</p>
      <div class="formula-box">
        $$\text{Feed Rate}_{\text{dry}} \, (\text{lb/day}) = Q \, (\text{MGD}) \times C_{\text{dose}} \, (\text{mg/L}) \times 8.34 \, \left(\frac{\text{lb/Mgal}}{\text{mg/L}}\right)$$
      </div>

      <p>In metric SI engineering units:</p>
      <div class="formula-box">
        $$\text{Feed Rate}_{\text{dry}} \, (\text{kg/day}) = \frac{Q \, (\text{m}^3/\text{day}) \times C_{\text{dose}} \, (\text{g/m}^3)}{1,000}$$
      </div>

      <p>Because commercial water utilities almost universally handle liquid alum delivered in bulk tankers, the liquid volumetric feed rate ($Q_{\text{liquid}}$) must account for solution specific gravity ($SG$) and dry chemical weight fraction ($w$):</p>
      <div class="formula-box">
        $$\text{Concentration}_{\text{liquid}} = 8.34 \times SG \times w \quad (\text{lb dry alum per gallon of solution})$$
      </div>
      <p>For standard AWWA B403 commercial liquid alum ($SG = 1.33, w = 0.485$):</p>
      <div class="formula-box">
        $$\text{Concentration}_{\text{liquid}} = 8.34 \times 1.33 \times 0.485 \approx 5.38 \, \text{lb dry alum/gal (or } 645 \, \text{g dry/L)}$$
      </div>

      <p>The liquid volumetric feed rate delivered by the metering pumps is therefore:</p>
      <div class="formula-box">
        $$Q_{\text{liquid}} \, (\text{gal/day}) = \frac{\text{Feed Rate}_{\text{dry}} \, (\text{lb/day})}{5.38 \, \text{lb/gal}}, \quad Q_{\text{liquid}} \, (\text{GPH}) = \frac{Q_{\text{liquid}} \, (\text{gal/day})}{24}$$
      </div>

      <p>For chemical pump stroke calibration using a graduated draw-down calibration cylinder (graduated in milliliters), the instantaneous volumetric rate is:</p>
      <div class="formula-box">
        $$\text{Pump Drawdown Rate} \, (\text{mL/min}) = \frac{Q_{\text{liquid}} \, (\text{gal/day}) \times 3,785.41 \, \text{mL/gal}}{1,440 \, \text{min/day}} = Q_{\text{liquid}} \, (\text{GPD}) \times 2.6288$$
      </div>

      <h2>Stoichiometric Alkalinity Consumption and pH Control</h2>
      <p>Every mole of aluminum sulfate reacts stoichiometrically with six moles of bicarbonate alkalinity ($\text{HCO}_3^-$). Evaluating the molar ratio reveals the exact chemical consumption:</p>
      <div class="formula-box">
        $$\text{Ratio} = \frac{3 \times \text{MW}_{\text{CaCO}_3}}{\text{MW}_{\text{Alum}}} = \frac{3 \times 100.09}{594.4} = 0.505 \, \frac{\text{mg/L alkalinity as CaCO}_3}{\text{mg/L dry alum}}$$
      </div>
      <p>Thus, each $1.0\text{ mg/L}$ of dry alum dosed removes $0.505\text{ mg/L}$ of alkalinity. If raw water alkalinity is insufficient, the pH drops precipitously, destabilizing floc and causing elevated dissolved aluminum residuals (&gt;0.20 mg/L) that violate the EPA Secondary Maximum Contaminant Level (SMCL). In such conditions, supplemental alkalinity must be fed:</p>
      <ul>
        <li><strong>Hydrated Lime ($\text{Ca(OH)}_2$, 74.09 g/mol):</strong> $1.0\text{ mg/L}$ dry alum requires $0.374\text{ mg/L}$ pure $\text{Ca(OH)}_2$ for neutral balance.</li>
        <li><strong>Caustic Soda ($\text{NaOH}$, 40.00 g/mol):</strong> $1.0\text{ mg/L}$ dry alum requires $0.404\text{ mg/L}$ $100\%\text{ NaOH}$ ($0.808\text{ mg/L}$ of $50\%\text{ NaOH}$).</li>
        <li><strong>Soda Ash ($\text{Na}_2\text{CO}_3$, 105.99 g/mol):</strong> $1.0\text{ mg/L}$ dry alum requires $0.535\text{ mg/L}$ soda ash.</li>
      </ul>

      <h2>Coagulant Sludge Production Modeling</h2>
      <p>Alum sludge generated in sedimentation basins and backwash holding lagoons consists of both precipitated aluminum hydroxide flocs and removed raw water suspended solids:</p>
      <div class="formula-box">
        $$W_{\text{sludge, dry}} \, (\text{lb/day}) = Q \, (\text{MGD}) \times \left(0.263 \times C_{\text{dose}} + 1.0 \times \text{TSS}_{\text{removed}}\right) \times 8.34$$
      </div>
      <p>Where $0.263$ represents the stoichiometric ratio of dry $\text{Al(OH)}_3$ solids generated per unit mass of commercial alum $(\frac{2 \times 78.0}{594.4} \approx 0.263)$.</p>

      <h2>Alum Dosing Benchmark Table Across Raw Water Quality Regimes</h2>
      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Water Quality Regime</th>
              <th>Raw Turbidity (NTU)</th>
              <th>TOC / True Color (mg/L / Pt-Co)</th>
              <th>Typical Alum Dose (mg/L)</th>
              <th>Alkalinity Consumed (mg/L CaCO₃)</th>
              <th>Recommended Coagulation pH</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Low Turbidity, Low Color (Protected Aquifer/Lake)</td>
              <td>0.5 &ndash; 3.0</td>
              <td>&lt; 2.0 / &lt; 5</td>
              <td>8 &ndash; 15</td>
              <td>4.0 &ndash; 7.6</td>
              <td>6.8 &ndash; 7.2</td>
            </tr>
            <tr>
              <td>Moderate Surface Water (Typical Reservoir)</td>
              <td>5.0 &ndash; 25</td>
              <td>2.5 &ndash; 6.0 / 10 &ndash; 25</td>
              <td>18 &ndash; 35</td>
              <td>9.1 &ndash; 17.7</td>
              <td>6.4 &ndash; 6.9</td>
            </tr>
            <tr>
              <td>Storm Runoff / River Flash Flood</td>
              <td>50 &ndash; 250</td>
              <td>6.0 &ndash; 15 / 30 &ndash; 80</td>
              <td>40 &ndash; 75</td>
              <td>20.2 &ndash; 37.9</td>
              <td>6.0 &ndash; 6.5</td>
            </tr>
            <tr>
              <td>High Organic Carbon / Humic Swamp Water</td>
              <td>2.0 &ndash; 10</td>
              <td>8.0 &ndash; 25 / 50 &ndash; 150</td>
              <td>35 &ndash; 65 (Enhanced Coagulation)</td>
              <td>17.7 &ndash; 32.8</td>
              <td>5.5 &ndash; 6.2</td>
            </tr>
            <tr>
              <td>Cold Winter Water (&lt; 4°C / 39°F)</td>
              <td>2.0 &ndash; 15</td>
              <td>3.0 &ndash; 8.0 / 15 &ndash; 30</td>
              <td>25 &ndash; 45 (+ Polymer Aid)</td>
              <td>12.6 &ndash; 22.7</td>
              <td>6.5 &ndash; 7.0</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Practical Worked Case Study: 10 MGD Municipal Clarification Facility</h2>
      <div class="worked-example-card">
        <h3>Engineering Design Example: River Intake Flash Runoff Event</h3>
        <p><strong>Treatment Plant Context:</strong> A conventional surface water treatment facility treats an intake flow of $10.0\text{ MGD}$. A sudden upstream rain event increases river turbidity to $45\text{ NTU}$ and total organic carbon to $5.5\text{ mg/L}$. Raw water total alkalinity is measured at $50.0\text{ mg/L as CaCO}_3$. Jar tests establish an optimum dry alum dosage of $32.0\text{ mg/L}$. The plant utilizes commercial liquid alum with specific gravity $1.33$ and $48.5\%$ concentration ($5.38\text{ lb dry alum/gal}$). Two chemical metering pumps operate in parallel duty.</p>

        <p><strong>Step 1: Calculate Daily Dry Chemical Mass:</strong></p>
        $$\text{Mass Rate}_{\text{dry}} = 10.0\text{ MGD} \times 32.0\text{ mg/L} \times 8.34 = 2,668.8\text{ lb/day dry alum (1,210.5 kg/day)}$$

        <p><strong>Step 2: Determine Commercial Liquid Volumetric Delivery:</strong></p>
        $$Q_{\text{liquid}} = \frac{2,668.8\text{ lb/day}}{5.38\text{ lb/gal}} = 496.06\text{ gal/day}$$
        $$\text{Hourly Feed Rate} = \frac{496.06\text{ GPD}}{24\text{ hours}} = 20.67\text{ GPH}$$

        <p><strong>Step 3: Diaphragm Metering Pump Calibration Rate:</strong></p>
        <p>For two duty metering pumps splitting the load evenly:</p>
        $$\text{Flow per Pump} = \frac{496.06\text{ GPD}}{2} = 248.03\text{ GPD (10.33 GPH)}$$
        $$\text{Calibration Drawdown per Pump} = 248.03 \times 2.6288 = 652.0\text{ mL/min}$$

        <p><strong>Step 4: Stoichiometric Alkalinity Destruction &amp; Residual Verification:</strong></p>
        $$\text{Alkalinity Consumed} = 32.0\text{ mg/L} \times 0.505 = 16.16\text{ mg/L as CaCO}_3$$
        $$\text{Residual Alkalinity} = 50.0 - 16.16 = 33.84\text{ mg/L as CaCO}_3$$
        <p>Because residual alkalinity remains above the critical $30\text{ mg/L}$ floor, finished water pH remains stable without mandatory supplemental lime feed, though pre-lime readiness is advised if river alkalinity drops further.</p>

        <p><strong>Step 5: Coagulation Sludge Solids Generation:</strong></p>
        <p>Assuming 95% turbidity/TSS removal ($45 \times 0.95 = 42.75\text{ mg/L}$):</p>
        $$W_{\text{sludge}} = 10.0 \times \left(0.263 \times 32.0 + 42.75\right) \times 8.34 = 10.0 \times (8.416 + 42.75) \times 8.34 = 4,267.2\text{ lb/day dry solids}$$
      </div>

      <h2>Operational Guidelines and Storage Specifications</h2>
      <p>Handling and applying liquid aluminum sulfate requires careful engineering design:</p>
      <ul>
        <li><strong>Crystallization Temperature:</strong> Commercial liquid alum has a freezing point of roughly &minus;13&deg;C (8&deg;F) to &minus;15&deg;C (5&deg;F). In northern climates, outdoor chemical bulk storage tanks require heat tracing and insulation to prevent viscous crystallization in pipe headers.</li>
        <li><strong>Corrosion Resistance Materials:</strong> Alum solutions have an acidic pH between 2.1 and 2.7. All wetted piping, metering heads, valves, and tank linings must be constructed from non-metallic materials (HDPE, cross-linked polyethylene XLPE, PVDF, PTFE, or FRP) or high-grade alloys (Hastelloy C, Carpenter 20). Standard 304 or 316 stainless steels suffer rapid pitting and chloride-induced stress corrosion.</li>
        <li><strong>Rapid Flash Mixing:</strong> Coagulant hydrolysis occurs within microseconds (10 to 100 milliseconds). Rapid mixing units (in-line static mixers or high-speed mechanical flash mixers with velocity gradients $G &gt; 700\text{ s}^{-1}$) are mandatory at the point of chemical injection to ensure uniform micro-floc formation prior to slow flocculation ($G = 20\text{ to }70\text{ s}^{-1}$).</li>
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
          <p class="footer-about">High-precision chemical, environmental, and water works calculation tools conforming to AWWA, EPA, and Ten State Standards.</p>
        </div>
        <div class="footer-col">
          <h4 class="footer-title">Engineering Disciplines</h4>
          <ul class="footer-links">
            <li><a href="chemical.html">Chemical &amp; Water Treatment</a></li>
            <li><a href="civil.html">Civil &amp; Construction</a></li>
            <li><a href="mechanical.html">Mechanical &amp; HVAC</a></li>
            <li><a href="engineering.html">Electrical &amp; Electronics</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4 class="footer-title">Standard References</h4>
          <ul class="footer-links">
            <li><a href="https://www.awwa.org" target="_blank" rel="noopener">AWWA B403 (Liquid Alum)</a></li>
            <li><a href="https://www.epa.gov" target="_blank" rel="noopener">US EPA Surface Water Rules</a></li>
            <li><a href="https://www.wef.org" target="_blank" rel="noopener">Water Environment Federation</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    function toggleAlumForm() {
      const f = document.getElementById("alumForm").value;
      document.getElementById("customAlumParams").style.display = (f === "custom") ? "grid" : "none";
    }

    function toggleFlowUnits() {
      const u = document.getElementById("flowUnit").value;
      const lbl = document.getElementById("flowLabel");
      if (u === "mgd") lbl.textContent = "Raw Water Plant Flow (MGD)";
      else if (u === "gpm") lbl.textContent = "Raw Water Plant Flow (GPM)";
      else if (u === "m3h") lbl.textContent = "Raw Water Plant Flow (m³/h)";
      else if (u === "m3d") lbl.textContent = "Raw Water Plant Flow (m³/day)";
      else if (u === "lps") lbl.textContent = "Raw Water Plant Flow (L/s)";
    }

    function calcAlumDosing() {
      const u = document.getElementById("flowUnit").value;
      const rawFlowInput = parseFloat(document.getElementById("rawFlow").value) || 0;
      const dose = parseFloat(document.getElementById("targetDose").value) || 0;
      const rawAlk = parseFloat(document.getElementById("rawAlkalinity").value) || 0;
      const form = document.getElementById("alumForm").value;
      const pumps = parseInt(document.getElementById("pumpTubes").value) || 1;
      const rawTss = parseFloat(document.getElementById("rawTSS").value) || 0;

      if (rawFlowInput <= 0 || dose <= 0) {
        alert("Please enter valid positive values for flow and coagulant dosage.");
        return;
      }

      // Convert raw flow to MGD and m3/day
      let flowMGD = 0;
      let flowM3D = 0;
      if (u === "mgd") {
        flowMGD = rawFlowInput;
        flowM3D = flowMGD * 3785.41;
      } else if (u === "gpm") {
        flowMGD = (rawFlowInput * 1440) / 1000000;
        flowM3D = flowMGD * 3785.41;
      } else if (u === "m3h") {
        flowM3D = rawFlowInput * 24;
        flowMGD = flowM3D / 3785.41;
      } else if (u === "m3d") {
        flowM3D = rawFlowInput;
        flowMGD = flowM3D / 3785.41;
      } else if (u === "lps") {
        flowM3D = (rawFlowInput * 86400) / 1000;
        flowMGD = flowM3D / 3785.41;
      }

      // Dry alum mass
      const dryLbsPerDay = flowMGD * dose * 8.34;
      const dryKgPerDay = (flowM3D * dose) / 1000;

      // Solution parameters
      let sg = 1.33;
      let strength = 0.485;
      if (form === "dry") {
        sg = 1.0;
        strength = 1.0;
      } else if (form === "custom") {
        sg = parseFloat(document.getElementById("liquidSG").value) || 1.33;
        strength = (parseFloat(document.getElementById("solStrength").value) || 48.5) / 100;
      }

      const dryLbsPerGal = 8.34 * sg * strength;
      const liquidGalPerDay = form === "dry" ? 0 : dryLbsPerDay / dryLbsPerGal;
      const liquidGPH = liquidGalPerDay / 24;
      const liquidLitersPerDay = liquidGalPerDay * 3.78541;

      // Pump calibration mL/min per pump
      const gpdPerPump = liquidGalPerDay / pumps;
      const mlPerMinPerPump = gpdPerPump * 2.6288;
      const lphPerPump = (gpdPerPump * 3.78541) / 24;

      // Alkalinity
      const alkConsumed = dose * 0.505;
      const residAlk = rawAlk - alkConsumed;

      // Sludge (lb/day)
      const drySludgeLbs = flowMGD * (dose * 0.263 + rawTss * 0.95) * 8.34;
      const drySludgeKg = drySludgeLbs * 0.453592;

      // UI Population
      document.getElementById("resDryMass").textContent = dryLbsPerDay.toFixed(1) + " lbs/day";
      document.getElementById("resDryMassAlt").textContent = dryKgPerDay.toFixed(1) + " kg/day dry alum";

      if (form === "dry") {
        document.getElementById("resPumpCalibration").textContent = (dryLbsPerDay / (pumps * 24)).toFixed(2) + " lbs/hr";
        document.getElementById("resPumpCalibrationAlt").textContent = "Dry feeder speed per hopper";
        document.getElementById("resLiquidVol").textContent = "N/A (Dry Feeder)";
        document.getElementById("resLiquidVolDay").textContent = dryLbsPerDay.toFixed(1) + " lbs dry chemical/day";
      } else {
        document.getElementById("resPumpCalibration").textContent = mlPerMinPerPump.toFixed(1) + " mL/min";
        document.getElementById("resPumpCalibrationAlt").textContent = lphPerPump.toFixed(2) + " L/h (" + (liquidGPH / pumps).toFixed(2) + " GPH per pump)";
        document.getElementById("resLiquidVol").textContent = liquidGPH.toFixed(2) + " GPH";
        document.getElementById("resLiquidVolDay").textContent = liquidGalPerDay.toFixed(1) + " GPD (" + liquidLitersPerDay.toFixed(1) + " L/day)";
      }

      document.getElementById("resResidAlk").textContent = residAlk.toFixed(1) + " mg/L";
      const alkStatus = document.getElementById("resAlkStatus");
      if (residAlk >= 30) {
        alkStatus.textContent = "Adequate buffer (Residual >= 30 mg/L)";
        alkStatus.style.color = "var(--success, #16a34a)";
      } else if (residAlk > 0) {
        alkStatus.textContent = "Warning: Marginal buffer (< 30 mg/L). pH drop risk.";
        alkStatus.style.color = "#ca8a04";
      } else {
        alkStatus.textContent = "CRITICAL: Total alkalinity depletion! Immediate caustic/lime feed required.";
        alkStatus.style.color = "#dc2626";
      }

      document.getElementById("resConsumedAlk").textContent = alkConsumed.toFixed(1) + " mg/L as CaCO₃ (" + ((alkConsumed / (rawAlk || 1)) * 100).toFixed(0) + "% of raw alkalinity)";

      if (residAlk < 30) {
        const deficit = 30 - residAlk;
        const limeNeeded = deficit * 0.74 * flowMGD * 8.34;
        const causticNeeded = deficit * 0.80 * flowMGD * 8.34;
        document.getElementById("resSupplNeed").textContent = "Required: " + limeNeeded.toFixed(1) + " lbs/day Lime or " + causticNeeded.toFixed(1) + " lbs/day 100% NaOH to maintain 30 mg/L residual";
      } else {
        document.getElementById("resSupplNeed").textContent = "None required. Natural raw buffer maintains stable floc pH.";
      }

      document.getElementById("resDrySludge").textContent = drySludgeLbs.toFixed(1) + " lbs/day dry solids (" + drySludgeKg.toFixed(1) + " kg/day)";
      document.getElementById("resStorageUsage").textContent = (liquidGalPerDay * 30).toLocaleString(undefined, {maximumFractionDigits: 0}) + " gal/month liquid storage volume (~" + ((liquidGalPerDay * 30 * 11.1) / 2000).toFixed(1) + " tons)";

      document.getElementById("alumResults").style.display = "block";
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
  <title>Boyle's Law Calculator | P₁V₁ = P₂V₂ Isothermal Gas Law Sizer</title>
  <meta name="description" content="Calculate pressure and volume changes for gases at constant temperature using Boyle's Law (P1V1 = P2V2), isothermal compression work, and compressibility factor.">
  <link rel="canonical" href="https://calchub.cloud/boyles-law-calculator.html">
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
        "name": "Boyle's Law Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Computes isothermal gas expansion and compression states using Boyle's Law P1V1 = P2V2, reversible isothermal mechanical work, and real gas compressibility adjustments.",
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
            "name": "What is Boyle's Law and what condition must remain constant?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Boyle's Law states that the absolute pressure exerted by a given mass of an ideal gas is inversely proportional to the volume it occupies, provided the temperature and amount of gas remain strictly constant: P1 * V1 = P2 * V2 = k. When pressure doubles, volume is halved."
            }
          },
          {
            "@type": "Question",
            "name": "Why must absolute pressure and absolute units be used in gas law calculations?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Gas laws describe thermodynamic states relative to absolute zero. Gauge pressure (psig, bar-gauge) measures pressure relative to ambient atmospheric pressure. One must always convert to absolute pressure (psia = psig + 14.696, or bar-abs = bar-gauge + 1.01325) before computing gas behavior."
            }
          },
          {
            "@type": "Question",
            "name": "How is reversible isothermal mechanical work calculated for Boyle compression?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For a quasi-static isothermal process, work is given by the integral W = - integral(P dV) = - P1 * V1 * ln(V2 / V1) = - n * R * T * ln(V2 / V1). Under compression (V2 < V1), external work is done ON the gas (positive or negative depending on thermodynamic sign convention)."
            }
          },
          {
            "@type": "Question",
            "name": "Under what physical conditions does real gas behavior deviate from Boyle's Law?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Real gases deviate from Boyle's ideal relationship at high pressures (typically above 20-50 bar) and low temperatures near their critical points due to intermolecular attraction forces and finite molecular volume, quantified by the compressibility factor Z = PV / (nRT)."
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
      <span>Boyle's Law Calculator</span>
    </nav>

    <h1 class="tool-title">Boyle's Law Calculator (P₁V₁ = P₂V₂)</h1>
    <p class="tool-subtitle">Isothermal Gas State Transformation, Pressure-Volume Sizing &amp; Thermodynamic Work</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="solveTarget">Variable to Solve For</label>
            <select id="solveTarget" class="form-control" onchange="updateSolveInputs()">
              <option value="v2" selected>Final Volume (V₂)</option>
              <option value="p2">Final Pressure (P₂)</option>
              <option value="v1">Initial Volume (V₁)</option>
              <option value="p1">Initial Pressure (P₁)</option>
            </select>
          </div>

          <!-- P1 Input -->
          <div id="p1Group" class="grid-2-col">
            <div class="form-group">
              <label for="p1Val">Initial Absolute Pressure (P₁)</label>
              <input type="number" id="p1Val" class="form-control" value="1.01325" step="0.01" min="0.0001">
            </div>
            <div class="form-group">
              <label for="p1Unit">P₁ Pressure Unit</label>
              <select id="p1Unit" class="form-control">
                <option value="atm">Atmospheres (atm)</option>
                <option value="bar" selected>Bar (bar absolute)</option>
                <option value="kpa">Kilopascals (kPa)</option>
                <option value="psi">Pounds/sq in absolute (psia)</option>
                <option value="pa">Pascals (Pa)</option>
                <option value="torr">Torr / mmHg</option>
              </select>
            </div>
          </div>

          <!-- V1 Input -->
          <div id="v1Group" class="grid-2-col">
            <div class="form-group">
              <label for="v1Val">Initial Volume (V₁)</label>
              <input type="number" id="v1Val" class="form-control" value="100.0" step="1.0" min="0.0001">
            </div>
            <div class="form-group">
              <label for="v1Unit">V₁ Volume Unit</label>
              <select id="v1Unit" class="form-control">
                <option value="l" selected>Liters (L)</option>
                <option value="m3">Cubic Meters (m³)</option>
                <option value="cm3">Cubic Centimeters (cm³ / mL)</option>
                <option value="ft3">Cubic Feet (ft³)</option>
                <option value="gal">US Gallons (gal)</option>
              </select>
            </div>
          </div>

          <!-- P2 Input -->
          <div id="p2Group" class="grid-2-col">
            <div class="form-group">
              <label for="p2Val">Final Absolute Pressure (P₂)</label>
              <input type="number" id="p2Val" class="form-control" value="10.0" step="0.1" min="0.0001">
            </div>
            <div class="form-group">
              <label for="p2Unit">P₂ Pressure Unit</label>
              <select id="p2Unit" class="form-control">
                <option value="atm">Atmospheres (atm)</option>
                <option value="bar" selected>Bar (bar absolute)</option>
                <option value="kpa">Kilopascals (kPa)</option>
                <option value="psi">Pounds/sq in absolute (psia)</option>
                <option value="pa">Pascals (Pa)</option>
                <option value="torr">Torr / mmHg</option>
              </select>
            </div>
          </div>

          <!-- V2 Input -->
          <div id="v2Group" class="grid-2-col" style="display:none;">
            <div class="form-group">
              <label for="v2Val">Final Volume (V₂)</label>
              <input type="number" id="v2Val" class="form-control" value="10.0" step="1.0" min="0.0001">
            </div>
            <div class="form-group">
              <label for="v2Unit">V₂ Volume Unit</label>
              <select id="v2Unit" class="form-control">
                <option value="l" selected>Liters (L)</option>
                <option value="m3">Cubic Meters (m³)</option>
                <option value="cm3">Cubic Centimeters (cm³ / mL)</option>
                <option value="ft3">Cubic Feet (ft³)</option>
                <option value="gal">US Gallons (gal)</option>
              </select>
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="gasTemp">Isothermal System Temperature (°C)</label>
              <input type="number" id="gasTemp" class="form-control" value="20" step="1">
              <span class="field-hint">Held constant throughout the process (T₁ = T₂)</span>
            </div>
            <div class="form-group">
              <label for="gasSpecies">Gas Molecular Identity</label>
              <select id="gasSpecies" class="form-control">
                <option value="air" selected>Atmospheric Air (MW = 28.97 g/mol)</option>
                <option value="n2">Pure Nitrogen N₂ (MW = 28.01 g/mol)</option>
                <option value="o2">Pure Oxygen O₂ (MW = 32.00 g/mol)</option>
                <option value="co2">Carbon Dioxide CO₂ (MW = 44.01 g/mol)</option>
                <option value="ch4">Methane CH₄ (MW = 16.04 g/mol)</option>
                <option value="h2">Hydrogen H₂ (MW = 2.016 g/mol)</option>
                <option value="he">Helium He (MW = 4.003 g/mol)</option>
              </select>
            </div>
          </div>

          <button type="button" class="btn btn-primary" onclick="calcBoylesLaw()">Solve Boyle's Gas Equation</button>
        </div>

        <div id="boyleResults" class="results-box" style="display:none;margin-top:1.5rem;">
          <h3 class="results-title">Isothermal Gas State &amp; Thermodynamic Diagnostics</h3>
          <div class="result-grid">
            <div class="result-card">
              <div class="result-label" id="resTargetLabel">Calculated Value</div>
              <div class="result-value highlight" id="resTargetVal">--</div>
              <div class="result-subtext" id="resTargetAlt">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Volume Compression / Expansion Ratio</div>
              <div class="result-value" id="resRatioVal">--</div>
              <div class="result-subtext" id="resRatioDesc">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Isothermal Mechanical Work (W)</div>
              <div class="result-value highlight" id="resWorkVal">--</div>
              <div class="result-subtext" id="resWorkAlt">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Boyle State Constant (k = P·V)</div>
              <div class="result-value" id="resBoyleConstant">--</div>
              <div class="result-subtext">Joules of pressure-volume energy</div>
            </div>
          </div>

          <div class="result-details" style="margin-top:1rem;padding:1rem;background:var(--card-bg);border-radius:6px;border:1px solid var(--border-light);">
            <h4 style="margin-top:0;">Thermodynamic &amp; Mass Quantities</h4>
            <ul style="margin-bottom:0;line-height:1.7;">
              <li><strong>Total Gas Moles (n):</strong> <span id="resGasMoles">--</span></li>
              <li><strong>Total Contained Gas Mass:</strong> <span id="resGasMass">--</span></li>
              <li><strong>Thermodynamic Process Nature:</strong> <span id="resProcessNature">--</span></li>
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
            <li><a href="alum-dosing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Alum Dosing Calculator</a></li>
            <li><a href="chlorine-dosing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Chlorine Dosing Calculator</a></li>
            <li><a href="chemical-dosing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Chemical Dosing Rate Calculator</a></li>
            <li><a href="reynolds-number-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Reynolds Number (Moody)</a></li>
          </ul>
          <div style="margin-top:1.25rem;padding-top:1rem;border-top:1px solid var(--border-light);">
            <a href="chemical.html" class="sidebar-category-link">View All Chemical Calculators &rarr;</a>
          </div>
        </div>
      </aside>
    </div>

    <!-- Technical Educational Article Body (1000+ Words) -->
    <article class="article-body">
      <h2>Thermodynamic Foundation of Boyle's Law</h2>
      <p>Boyle's Law (also recognized historically as Mariotte's Law) represents the earliest empirical equation of state established in experimental thermodynamics. Formulated by Anglo-Irish natural philosopher Robert Boyle in 1662 and independently verified by French physicist Edme Mariotte in 1676, the law establishes the fundamental inverse relationship governing the mechanical behavior of a confined gas undergoing a strictly isothermal (constant temperature) process.</p>

      <p>Under classical kinetic molecular theory, gas pressure originates from continuous, elastic collisions of sub-microscopic molecules against the bounding walls of their container. When the physical boundaries of the vessel contract while the kinetic energy distribution of the molecules remains constant (governed purely by temperature $T$), molecular collision frequency per unit surface area increases in exact inverse proportion to the volumetric reduction. This fundamental physical postulate underpins pneumatic compressors, scuba diving regulators, hyperbaric chambers, autoclave sterilization vessels, and gas transport pipelines.</p>

      <h2>Mathematical Formulation and the Equation of State</h2>
      <p>Mathematically, Boyle's Law states that for a fixed quantity of gas (constant mass or molar quantity $n$) maintained at constant absolute thermodynamic temperature ($T$), the product of absolute pressure ($P$) and volume ($V$) remains constant:</p>

      <div class="formula-box">
        $$P \cdot V = k \quad \implies \quad P_1 V_1 = P_2 V_2 \quad (T = \text{constant}, \, n = \text{constant})$$
      </div>

      <p>Where:</p>
      <ul>
        <li>$P_1, P_2$ = Initial and final absolute pressures (expressed in Pa, bar, atm, or psia).</li>
        <li>$V_1, V_2$ = Initial and final gas volumes (expressed in $\text{m}^3$, liters, or $\text{ft}^3$).</li>
        <li>$k$ = The Boyle state constant, equivalent to $n R T$, where $R = 8.314462\text{ J/(mol}\cdot\text{K)}$ is the universal gas constant.</li>
      </ul>

      <p>Rearranging the equation allows direct analytical determination of any fourth boundary condition when three are established:</p>

      <div class="formula-box">
        $$V_2 = \frac{P_1 V_1}{P_2}, \quad P_2 = \frac{P_1 V_1}{V_2}, \quad V_1 = \frac{P_2 V_2}{P_1}, \quad P_1 = \frac{P_2 V_2}{V_1}$$
      </div>

      <h2>Reversible Isothermal Mechanical Work</h2>
      <p>When a gas expands or contracts isothermally, boundary work is exchanged across the control surface. In a quasi-static reversible expansion or compression, pressure follows the hyperbolic curve $P(V) = \frac{nRT}{V} = \frac{P_1 V_1}{V}$. Integrating boundary work ($W = -\int_{V_1}^{V_2} P \, dV$) yields:</p>

      <div class="formula-box">
        $$W_{\text{isothermal}} = - \int_{V_1}^{V_2} \frac{P_1 V_1}{V} \, dV = - P_1 V_1 \ln\left(\frac{V_2}{V_1}\right) = - n R T \ln\left(\frac{V_2}{V_1}\right)$$
      </div>

      <p>Under compression ($V_2 &lt; V_1$), the ratio $\frac{V_2}{V_1} &lt; 1$, making $\ln(V_2/V_1)$ negative and resulting in positive work transferred into the gas system from the surroundings ($W_{\text{comp}} &gt; 0$). Conversely, during expansion ($V_2 &gt; V_1$), work is performed by the expanding gas against external boundaries. Because internal energy of an ideal gas depends solely on temperature ($\Delta U = C_v \Delta T = 0$ for isothermal conditions), the First Law of Thermodynamics dictates that heat exchanged with the thermal reservoir exactly equals boundary work ($Q = -W$).</p>

      <h2>Real Gas Deviations: The Compressibility Factor (Z)</h2>
      <p>Boyle's Law models ideal gases where molecules are treated as point masses with zero physical volume and zero inter-molecular attractive or repulsive forces. In industrial chemical processing, refrigeration circuits, and high-pressure gas storage (e.g., CNG, hydrogen fuel cells, or deep-sea diving at 200 to 350 bar), real gases deviate significantly from Boyle's hyperbolic curve. Engineers correct for this non-ideality using the compressibility factor ($Z$):</p>

      <div class="formula-box">
        $$P V = Z \cdot n R T \quad \implies \quad \frac{P_1 V_1}{Z_1} = \frac{P_2 V_2}{Z_2}$$
      </div>

      <p>The table below details compressibility factor deviations across industrial gases at $20^\circ\text{C}$ (293.15 K) spanning atmospheric to extreme pressures:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Gas Identity</th>
              <th>Critical Temp T_c (K)</th>
              <th>Critical Pres P_c (bar)</th>
              <th>Z @ 1 bar (Ideal)</th>
              <th>Z @ 50 bar</th>
              <th>Z @ 100 bar</th>
              <th>Z @ 200 bar</th>
              <th>Boyle Law Error @ 200 bar</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Hydrogen (H₂)</td>
              <td>33.19</td>
              <td>13.13</td>
              <td>1.0006</td>
              <td>1.0315</td>
              <td>1.0638</td>
              <td>1.1292</td>
              <td>&plusmn;12.9% (Repulsive finite volume)</td>
            </tr>
            <tr>
              <td>Helium (He)</td>
              <td>5.19</td>
              <td>2.27</td>
              <td>1.0005</td>
              <td>1.0250</td>
              <td>1.0502</td>
              <td>1.1011</td>
              <td>&plusmn;10.1% (Near-ideal noble gas)</td>
            </tr>
            <tr>
              <td>Nitrogen (N₂)</td>
              <td>126.19</td>
              <td>33.96</td>
              <td>0.9998</td>
              <td>0.9850</td>
              <td>0.9890</td>
              <td>1.0450</td>
              <td>&plusmn;4.5% (Crossover behavior)</td>
            </tr>
            <tr>
              <td>Atmospheric Air</td>
              <td>132.50</td>
              <td>37.70</td>
              <td>0.9997</td>
              <td>0.9810</td>
              <td>0.9850</td>
              <td>1.0520</td>
              <td>&plusmn;5.2% (Matches N₂ closely)</td>
            </tr>
            <tr>
              <td>Methane (CH₄ / Natural Gas)</td>
              <td>190.56</td>
              <td>45.99</td>
              <td>0.9980</td>
              <td>0.8920</td>
              <td>0.7950</td>
              <td>0.8650</td>
              <td>&minus;13.5% (Strong Van der Waals attraction)</td>
            </tr>
            <tr>
              <td>Carbon Dioxide (CO₂)</td>
              <td>304.13</td>
              <td>73.77</td>
              <td>0.9950</td>
              <td>0.6800</td>
              <td>Supercritical Fluid</td>
              <td>Supercritical Fluid</td>
              <td>&gt; 32% (Severe non-ideality near T_c)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Practical Worked Case Study: Industrial Air Compressor Receiver Charging</h2>
      <div class="worked-example-card">
        <h3>Engineering Design Example: Pneumatic Shop Receiver Pressurization</h3>
        <p><strong>System Scenario:</strong> An industrial reciprocal air compressor charges a rigid steel receiver tank with an internal water-volume capacity of $V_2 = 500\text{ Liters}$ ($0.50\text{ m}^3$). The receiver must be pressurized from an unpressurized initial state up to an operating threshold of $P_2 = 8.50\text{ bar absolute}$ ($123.3\text{ psia}$ or $\approx 108.7\text{ psig}$). Ambient atmospheric intake conditions are measured at $P_1 = 1.01325\text{ bar absolute}$ ($1.00\text{ atm}$) at an isothermal ambient temperature of $20^\circ\text{C}$ ($293.15\text{ K}$). Assume the compressed air aftercooler successfully cools the discharged air back to $20^\circ\text{C}$.</p>

        <p><strong>Step 1: Calculate Total Free Air Volume Required (V₁):</strong></p>
        <p>Applying Boyle's Law to determine the volume of free atmospheric air ($V_1$) that must be drawn through the intake filters to occupy the 500 L receiver at 8.50 bar:</p>
        $$P_1 V_1 = P_2 V_2 \implies V_1 = \frac{P_2 V_2}{P_1}$$
        $$V_1 = \frac{8.50\text{ bar} \times 500\text{ L}}{1.01325\text{ bar}} = \frac{4,250}{1.01325} = 4,194.4\text{ Liters (or } 4.194\text{ m}^3\text{)}$$

        <p><strong>Step 2: Determine Compression Ratio:</strong></p>
        $$r_c = \frac{P_2}{P_1} = \frac{V_1}{V_2} = \frac{8.50}{1.01325} = 8.389 : 1$$

        <p><strong>Step 3: Compute Total Contained Moles and Air Mass:</strong></p>
        <p>Using the ideal gas relation with $P_1 = 101,325\text{ Pa}$ and $V_1 = 4.1944\text{ m}^3$:</p>
        $$n = \frac{P_1 V_1}{R T} = \frac{101,325\text{ Pa} \times 4.1944\text{ m}^3}{8.3145\text{ J/(mol}\cdot\text{K)} \times 293.15\text{ K}} = \frac{425,000}{2,437.4} = 174.37\text{ moles}$$
        <p>Mass of air ($MW = 28.97\text{ g/mol}$):</p>
        $$m_{\text{air}} = 174.37\text{ mol} \times 0.02897\text{ kg/mol} = 5.05\text{ kg (11.13 lbs)}$$

        <p><strong>Step 4: Calculate Minimum Reversible Isothermal Work of Compression:</strong></p>
        $$W_{\text{isothermal}} = P_1 V_1 \ln\left(\frac{P_2}{P_1}\right) = 425,000\text{ J} \times \ln(8.389) = 425,000 \times 2.1269 = 903,932\text{ Joules} = 903.93\text{ kJ}$$
        <p>In electrical power units, this represents approximately $0.251\text{ kWh}$ of ideal theoretical compression energy.</p>
      </div>

      <h2>Operational Applications and Safety Limitations</h2>
      <p>Engineering practice requires clear recognition of when Boyle's Law can be directly deployed versus when advanced multi-parameter equations of state (Peng-Robinson, Soave-Redlich-Kwong) are necessary:</p>
      <ul>
        <li><strong>Isothermal vs. Adiabatic Compression:</strong> True isothermal compression requires infinite heat transfer rate to remove the heat of compression as rapidly as it is generated. Rapid compression (such as in an internal combustion engine cylinder or high-speed reciprocating compressor) is actually <strong>adiabatic</strong> ($P V^\gamma = \text{constant}$, where $\gamma = 1.4$ for diatomic air). Boyle's Law applies accurately to the initial and final stabilized states once the compressed gas cools back to ambient equilibrium.</li>
        <li><strong>Scuba and Life Support Physiology:</strong> Boyle's Law directly governs barotrauma risks in diving. As a diver descends from sea level (1.0 bar) to a depth of 30 meters (4.0 bar absolute), the volume of air in a flexible lung or drysuit is reduced to one-fourth ($V_2 = V_1 / 4$). Ascending while holding one's breath causes trapped gas to expand by $400\%$, causing pulmonary over-pressurization and alveolar rupture.</li>
        <li><strong>Pipeline Pneumatic Testing:</strong> Pressure testing gas utility pipelines with dry nitrogen or compressed air requires monitoring ambient temperature swings. A diurnal temperature drop of $15^\circ\text{C}$ during a 24-hour test can drop pressure by 5%, which uncalibrated operators may misinterpret as a joint leak.</li>
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
            <li><a href="https://webbook.nist.gov" target="_blank" rel="noopener">NIST Chemistry WebBook</a></li>
            <li><a href="https://www.asme.org" target="_blank" rel="noopener">ASME Boiler &amp; Pressure Vessel</a></li>
            <li><a href="https://www.iupac.org" target="_blank" rel="noopener">IUPAC Compendium of Chemical Term</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    const GAS_MW = {
      air: 28.97,
      n2: 28.013,
      o2: 31.999,
      co2: 44.01,
      ch4: 16.043,
      h2: 2.016,
      he: 4.003
    };

    function updateSolveInputs() {
      const target = document.getElementById("solveTarget").value;
      document.getElementById("p1Group").style.display = target === "p1" ? "none" : "grid";
      document.getElementById("v1Group").style.display = target === "v1" ? "none" : "grid";
      document.getElementById("p2Group").style.display = target === "p2" ? "none" : "grid";
      document.getElementById("v2Group").style.display = target === "v2" ? "none" : "grid";
    }

    function toPascals(val, unit) {
      if (unit === "atm") return val * 101325;
      if (unit === "bar") return val * 100000;
      if (unit === "kpa") return val * 1000;
      if (unit === "psi") return val * 6894.757;
      if (unit === "torr") return val * 133.322;
      return val; // pa
    }

    function fromPascals(pa, unit) {
      if (unit === "atm") return pa / 101325;
      if (unit === "bar") return pa / 100000;
      if (unit === "kpa") return pa / 1000;
      if (unit === "psi") return pa / 6894.757;
      if (unit === "torr") return pa / 133.322;
      return pa;
    }

    function toCubicMeters(val, unit) {
      if (unit === "l") return val * 0.001;
      if (unit === "cm3") return val * 0.000001;
      if (unit === "ft3") return val * 0.0283168;
      if (unit === "gal") return val * 0.00378541;
      return val; // m3
    }

    function fromCubicMeters(m3, unit) {
      if (unit === "l") return m3 * 1000;
      if (unit === "cm3") return m3 * 1000000;
      if (unit === "ft3") return m3 / 0.0283168;
      if (unit === "gal") return m3 / 0.00378541;
      return m3;
    }

    function calcBoylesLaw() {
      const target = document.getElementById("solveTarget").value;
      const gasKey = document.getElementById("gasSpecies").value;
      const mw = GAS_MW[gasKey];
      const tempC = parseFloat(document.getElementById("gasTemp").value) || 20;
      const tempK = tempC + 273.15;
      const R = 8.314462;

      let p1_pa = 0, v1_m3 = 0, p2_pa = 0, v2_m3 = 0;

      if (target !== "p1") {
        const v = parseFloat(document.getElementById("p1Val").value) || 0;
        const u = document.getElementById("p1Unit").value;
        p1_pa = toPascals(v, u);
      }
      if (target !== "v1") {
        const v = parseFloat(document.getElementById("v1Val").value) || 0;
        const u = document.getElementById("v1Unit").value;
        v1_m3 = toCubicMeters(v, u);
      }
      if (target !== "p2") {
        const v = parseFloat(document.getElementById("p2Val").value) || 0;
        const u = document.getElementById("p2Unit").value;
        p2_pa = toPascals(v, u);
      }
      if (target !== "v2") {
        const v = parseFloat(document.getElementById("v2Val").value) || 0;
        const u = document.getElementById("v2Unit").value;
        v2_m3 = toCubicMeters(v, u);
      }

      // Solve equation P1 * V1 = P2 * V2
      let resultText = "";
      let resultAltText = "";
      let targetLabel = "";

      if (target === "v2") {
        if (p2_pa <= 0) { alert("P2 must be positive"); return; }
        v2_m3 = (p1_pa * v1_m3) / p2_pa;
        const outUnit = document.getElementById("v1Unit").value;
        const v2_disp = fromCubicMeters(v2_m3, outUnit);
        targetLabel = "Final Volume (V₂)";
        resultText = v2_disp.toFixed(4) + " " + outUnit.toUpperCase();
        resultAltText = (v2_m3 * 1000).toFixed(2) + " L (" + v2_m3.toFixed(4) + " m³)";
      } else if (target === "p2") {
        if (v2_m3 <= 0) { alert("V2 must be positive"); return; }
        p2_pa = (p1_pa * v1_m3) / v2_m3;
        const outUnit = document.getElementById("p1Unit").value;
        const p2_disp = fromPascals(p2_pa, outUnit);
        targetLabel = "Final Absolute Pressure (P₂)";
        resultText = p2_disp.toFixed(4) + " " + outUnit.toUpperCase();
        resultAltText = (p2_pa / 100000).toFixed(3) + " bar (" + (p2_pa / 6894.757).toFixed(2) + " psia)";
      } else if (target === "v1") {
        if (p1_pa <= 0) { alert("P1 must be positive"); return; }
        v1_m3 = (p2_pa * v2_m3) / p1_pa;
        const outUnit = document.getElementById("v2Unit").value;
        const v1_disp = fromCubicMeters(v1_m3, outUnit);
        targetLabel = "Initial Volume (V₁)";
        resultText = v1_disp.toFixed(4) + " " + outUnit.toUpperCase();
        resultAltText = (v1_m3 * 1000).toFixed(2) + " L (" + v1_m3.toFixed(4) + " m³)";
      } else if (target === "p1") {
        if (v1_m3 <= 0) { alert("V1 must be positive"); return; }
        p1_pa = (p2_pa * v2_m3) / v1_m3;
        const outUnit = document.getElementById("p2Unit").value;
        const p1_disp = fromPascals(p1_pa, outUnit);
        targetLabel = "Initial Absolute Pressure (P₁)";
        resultText = p1_disp.toFixed(4) + " " + outUnit.toUpperCase();
        resultAltText = (p1_pa / 100000).toFixed(3) + " bar (" + (p1_pa / 6894.757).toFixed(2) + " psia)";
      }

      // PV product
      const boyleConstant = p1_pa * v1_m3; // Joules
      const compRatio = v1_m3 / v2_m3;
      const isCompression = compRatio > 1.0;

      // Isothermal work: W = - P1*V1 * ln(V2/V1) = P1*V1*ln(V1/V2)
      // Positive work into gas during compression
      const workJoules = p1_pa * v1_m3 * Math.log(v1_m3 / v2_m3);
      const workKJ = workJoules / 1000;
      const workKWh = workKJ / 3600;

      // Moles & Mass
      const moles = boyleConstant / (R * tempK);
      const massKg = (moles * mw) / 1000;
      const massLb = massKg * 2.20462;

      document.getElementById("resTargetLabel").textContent = targetLabel;
      document.getElementById("resTargetVal").textContent = resultText;
      document.getElementById("resTargetAlt").textContent = resultAltText;

      document.getElementById("resRatioVal").textContent = compRatio.toFixed(3) + " : 1";
      document.getElementById("resRatioDesc").textContent = isCompression ? "Isothermal Compression (Volume decreases)" : "Isothermal Expansion (Volume increases)";

      document.getElementById("resWorkVal").textContent = Math.abs(workKJ).toFixed(2) + " kJ";
      document.getElementById("resWorkAlt").textContent = (isCompression ? "Work done ON gas: " : "Work done BY gas: ") + Math.abs(workKWh).toFixed(4) + " kWh";

      document.getElementById("resBoyleConstant").textContent = boyleConstant.toLocaleString(undefined, {maximumFractionDigits: 1}) + " N·m (J)";

      document.getElementById("resGasMoles").textContent = moles.toFixed(2) + " mol";
      document.getElementById("resGasMass").textContent = massKg.toFixed(3) + " kg (" + massLb.toFixed(2) + " lbs) of " + gasKey.toUpperCase();
      document.getElementById("resProcessNature").textContent = isCompression ? "Mechanical Compression (Requires heat rejection Q = Wout to maintain " + tempC + "°C)" : "Mechanical Expansion (Requires heat addition Qin = Win to maintain " + tempC + "°C)";

      document.getElementById("boyleResults").style.display = "block";
    }
  </script>
</body>
</html>
"""

def generate():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p1 = os.path.join(root, "alum-dosing-calculator.html")
    p2 = os.path.join(root, "boyles-law-calculator.html")
    
    with open(p1, "w", encoding="utf-8") as f:
        f.write(TOOL_3_HTML.strip() + "\n")
    print(f"Generated {p1}")

    with open(p2, "w", encoding="utf-8") as f:
        f.write(TOOL_4_HTML.strip() + "\n")
    print(f"Generated {p2}")

if __name__ == "__main__":
    generate()
