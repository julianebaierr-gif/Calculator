# -*- coding: utf-8 -*-
"""
Script to generate Batch 15 Part 1 tools:
1. coagulant-dosing-calculator.html
2. combined-gas-law-calculator.html
"""
import os

TOOL_1_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Coagulant Dosing Calculator | Ferric, Alum &amp; PAC Water Treatment Sizer</title>
  <meta name="description" content="Calculate coagulant feed rates for water treatment: Alum, Ferric Chloride, Ferric Sulfate, and Polyaluminum Chloride (PAC), jar test calibration, and alkalinity.">
  <link rel="canonical" href="https://calchub.cloud/coagulant-dosing-calculator.html">
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
        "name": "Coagulant Dosing Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates primary coagulant feed rates for Alum, Ferric Chloride, Ferric Sulfate, and Polyaluminum Chloride (PAC), metering pump stroke calibration, and alkalinity consumption.",
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
            "name": "How does Ferric Chloride compare to Alum in water treatment coagulation?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Ferric chloride (FeCl3) forms denser, heavier iron hydroxide flocs that settle faster than aluminum hydroxide flocs. Ferric operates across a broader pH spectrum (4.0 to 11.0) compared to alum (5.8 to 7.2), but it consumes nearly double the alkalinity per mg/L (0.925 mg/L as CaCO3 vs 0.505 mg/L for alum) and requires highly corrosion-resistant wetted materials."
            }
          },
          {
            "@type": "Question",
            "name": "What is Polyaluminum Chloride (PAC) and why does it consume less alkalinity?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Polyaluminum Chloride (PAC) consists of pre-polymerized aluminum hydroxychloride complexes [Aln(OH)mCl(3n-m)]. Because PAC has been partially neutralized with hydroxyl ions during manufacturing (possessing a 'basicity' typically between 50% and 75%), it consumes significantly less raw water alkalinity (0.15 to 0.30 mg/L as CaCO3) and produces lower finished water pH depression."
            }
          },
          {
            "@type": "Question",
            "name": "How do you translate jar test results to full-scale plant chemical pump feed rates?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A jar test establishes the optimum coagulant concentration (mg/L or ppm). For plant feed: Feed Rate (lb/day dry) = Plant Flow (MGD) * Target Dose (mg/L) * 8.34 lb/gal. The volumetric liquid feed rate is GPD = (lb/day dry) / (active lbs coagulant per gallon of commercial solution). Drawdown calibration is Rate (mL/min) = GPD * 2.6288."
            }
          },
          {
            "@type": "Question",
            "name": "How is chemical sludge generation estimated from coagulant addition?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Total dry chemical sludge includes precipitated metal hydroxide flocs plus removed suspended solids: Sludge (lb/day) = Flow (MGD) * [Coagulant Constant * Dose (mg/L) + Removed TSS (mg/L)] * 8.34. The coagulant constant is 0.263 for Alum, 0.66 for Ferric Chloride, and 0.54 for Ferric Sulfate."
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
      <span>Coagulant Dosing Calculator</span>
    </nav>

    <h1 class="tool-title">Universal Coagulant Dosing &amp; Feed Calculator</h1>
    <p class="tool-subtitle">Ferric Chloride, Alum, Ferric Sulfate &amp; PAC Feed Sizing, Pump Calibration &amp; Alkalinity Stoichiometry</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="coagulantType">Coagulant Chemical Selection</label>
            <select id="coagulantType" class="form-control" onchange="updateCoagulantPreset()">
              <option value="ferric_cl" selected>Ferric Chloride (FeCl₃ 38% liquid, SG = 1.42, 4.49 lb dry/gal)</option>
              <option value="alum_liquid">Liquid Alum (Al₂(SO₄)₃ 48.5% dry basis, SG = 1.33, 5.38 lb dry/gal)</option>
              <option value="ferric_so4">Ferric Sulfate (Fe₂(SO₄)₃ 50% liquid, SG = 1.55, 6.46 lb dry/gal)</option>
              <option value="pac_liquid">Polyaluminum Chloride (PAC 30% liquid, SG = 1.25, 3.13 lb dry/gal, 70% basicity)</option>
              <option value="alum_dry">Dry Granular Alum (Al₂(SO₄)₃·14H₂O 100% active basis)</option>
              <option value="custom">Custom Liquid Coagulant (Specific Gravity &amp; Strength)</option>
            </select>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="plantFlowUnit">Plant Water Flow Units</label>
              <select id="plantFlowUnit" class="form-control" onchange="toggleFlowUnitLabels()">
                <option value="mgd" selected>MGD (Million Gallons per Day)</option>
                <option value="gpm">GPM (Gallons per Minute)</option>
                <option value="m3h">m³/hour (Cubic Meters per Hour)</option>
                <option value="m3d">m³/day (Cubic Meters per Day)</option>
                <option value="lps">Liters per Second (L/s)</option>
              </select>
            </div>
            <div class="form-group">
              <label for="plantFlowVal" id="flowValLabel">Plant Influent Flow Rate (MGD)</label>
              <input type="number" id="plantFlowVal" class="form-control" value="10.0" step="0.5" min="0.01">
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="targetCoagDose">Optimum Jar Test Dosage (mg/L or ppm dry)</label>
              <input type="number" id="targetCoagDose" class="form-control" value="28.0" step="0.5" min="0.1">
              <span class="field-hint">Dry chemical basis determined from jar testing</span>
            </div>
            <div class="form-group">
              <label for="rawWaterAlkalinity">Raw Water Alkalinity (mg/L as CaCO₃)</label>
              <input type="number" id="rawWaterAlkalinity" class="form-control" value="65" step="1" min="0">
              <span class="field-hint">Total bicarbonate buffer prior to chemical feed</span>
            </div>
          </div>

          <div id="customCoagGrid" class="grid-2-col" style="display:none;">
            <div class="form-group">
              <label for="coagSG">Solution Specific Gravity (SG)</label>
              <input type="number" id="coagSG" class="form-control" value="1.42" step="0.01" min="1.0">
            </div>
            <div class="form-group">
              <label for="coagStrength">Chemical Concentration (% by wt dry)</label>
              <input type="number" id="coagStrength" class="form-control" value="38.0" step="0.5" min="1" max="100">
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="numCoagPumps">Duty Chemical Metering Pumps</label>
              <input type="number" id="numCoagPumps" class="form-control" value="2" step="1" min="1" max="6">
            </div>
            <div class="form-group">
              <label for="rawTurbidityTss">Raw Suspended Solids / Turbidity (mg/L or NTU)</label>
              <input type="number" id="rawTurbidityTss" class="form-control" value="30" step="1" min="0">
              <span class="field-hint">Used for chemical sludge solids generation modeling</span>
            </div>
          </div>

          <div class="form-group">
            <label for="bulkCoagCost">Bulk Coagulant Solution Price ($ / Gallon)</label>
            <input type="number" id="bulkCoagCost" class="form-control" value="3.15" step="0.05" min="0">
          </div>

          <button type="button" class="btn btn-primary" onclick="calcCoagulantDosing()">Calculate Coagulant Feed &amp; Stoichiometry</button>
        </div>

        <div id="coagResults" class="results-box" style="display:none;margin-top:1.5rem;">
          <h3 class="results-title">Coagulant Feed Sizing &amp; Process Diagnostics</h3>
          <div class="result-grid">
            <div class="result-card">
              <div class="result-label">Pure Active Chemical Demand</div>
              <div class="result-value highlight" id="resDryMass">--</div>
              <div class="result-subtext" id="resDryMassAlt">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Feed Rate (Per Duty Pump)</div>
              <div class="result-value highlight" id="resPumpDrawdown">--</div>
              <div class="result-subtext" id="resPumpDrawdownAlt">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Daily Commercial Liquid Feed</div>
              <div class="result-value" id="resLiquidDay">--</div>
              <div class="result-subtext" id="resLiquidDayAlt">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Residual Alkalinity</div>
              <div class="result-value" id="resResidAlk">--</div>
              <div class="result-subtext" id="resAlkStatus">--</div>
            </div>
          </div>

          <div class="result-details" style="margin-top:1rem;padding:1rem;background:var(--card-bg);border-radius:6px;border:1px solid var(--border-light);">
            <h4 style="margin-top:0;">Chemical Reactions &amp; Sludge Mass Sizing</h4>
            <ul style="margin-bottom:0;line-height:1.7;">
              <li><strong>Alkalinity Consumed:</strong> <span id="resConsumedAlk">--</span></li>
              <li><strong>Supplemental Neutralization Buffer:</strong> <span id="resBufferNeed">--</span></li>
              <li><strong>Dry Coagulant Sludge Production:</strong> <span id="resSludgeTotal">--</span></li>
              <li><strong>Monthly Bulk Chemical Storage:</strong> <span id="resStorageMonth">--</span></li>
              <li><strong>Estimated Chemical Expenditure:</strong> <span id="resTotalCost" style="font-weight:700;color:var(--primary);">--</span></li>
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
            <li><a href="caustic-soda-dosing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Caustic Soda Dosing Calculator</a></li>
            <li><a href="chlorine-dioxide-dosing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Chlorine Dioxide (ClO₂) Oxidation</a></li>
            <li><a href="chlorine-dosing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Chlorine Dosing Calculator</a></li>
          </ul>
          <div style="margin-top:1.25rem;padding-top:1rem;border-top:1px solid var(--border-light);">
            <a href="chemical.html" class="sidebar-category-link">View All Chemical Calculators &rarr;</a>
          </div>
        </div>
      </aside>
    </div>

    <!-- Technical Educational Article Body (1000+ Words) -->
    <article class="article-body">
      <h2>Comparative Fundamentals of Modern Coagulant Chemistry</h2>
      <p>Coagulation is the core physicochemical process deployed in municipal surface water clarification, direct filtration, and industrial wastewater treatment. Raw waters carry natural colloidal particles—including clay silts, bacteria, viruses, silica, and natural organic matter (NOM)—possessing negative surface electrostatic charges. Mutual electrostatic repulsion keeps these sub-micron colloids in stable suspension indefinitely.</p>

      <p>Primary coagulants are multivalent metal salts that destabilize colloidal suspensions via two competing or simultaneous mechanisms: <strong>electrical double-layer compression / charge neutralization</strong> (operating at acidic to neutral pH with positively charged metal hydrolysis monomers) and <strong>sweep floc enmeshment</strong> (occurring when metal hydroxide precipitates exceed saturation limits and physically sweep suspended impurities out of the water column). Selecting between traditional aluminum-based coagulants and iron-based ferric coagulants represents a fundamental process design decision governed by raw water turbidity, water temperature, NOM color content, and natural alkalinity buffer capacity.</p>

      <h2>Hydrolysis and Chemical Speciation Across Coagulant Classes</h2>
      <p>Each commercial coagulant class exhibits distinct hydrolysis kinetics, pH operating windows, and stoichiometric impacts:</p>

      <ul>
        <li><strong>Aluminum Sulfate (Alum):</strong> $\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O}$ hydrolyzes into amorphous aluminum hydroxide ($\text{Al(OH)}_3\downarrow$). It functions within an optimum pH window of $5.8\text{ to }7.2$. In cold water ($&lt; 4^\circ\text{C}$), alum hydrolysis kinetics slow dramatically, leading to pin-point floc and dissolved aluminum carryover violating EPA drinking water secondary maximum contaminant levels ($0.05\text{ to }0.20\text{ mg/L}$).</li>
        <li><strong>Ferric Chloride ($\text{FeCl}_3$):</strong> An aggressive iron coagulant operating across an expansive pH window of $4.0\text{ to }11.0$. Because iron hydroxide ($\text{Fe(OH)}_3$) has a solubility product constant ($K_{sp} \approx 10^{-38}$) twelve orders of magnitude lower than aluminum hydroxide ($K_{sp} \approx 10^{-26}$), ferric forms heavier, denser, faster-settling flocs even in ice-cold waters. However, it is intensely corrosive, requiring PVDF, FRP, or lined titanium wetted materials.</li>
        <li><strong>Ferric Sulfate ($\text{Fe}_2(\text{SO}_4)_3$):</strong> Frequently chosen over ferric chloride to eliminate chloride ion corrosion stress in stainless steel equipment and avoid elevating the chloride-to-sulfate mass ratio (CSMR), which can trigger galvanic lead leaching in distribution networks.</li>
        <li><strong>Polyaluminum Chloride (PAC):</strong> Pre-hydrolyzed polymeric aluminum complexes containing pre-formed tridecameric Keggin polycations ($\text{Al}_{13}\text{O}_4(\text{OH})_{24}^{7+}$). Manufactured with basicities ranging from 50% to 75%, PAC requires far less bicarbonate alkalinity from raw water, functions effectively in cold water, and generates significantly lower sludge volumes.</li>
      </ul>

      <h2>Governing Mathematical Formulas for Chemical Metering</h2>
      <p>The daily pure chemical mass requirement ($W_{\text{dry}}$) is calculated using the standard waterworks relation:</p>

      <div class="formula-box">
        $$W_{\text{dry}} \, (\text{lb/day}) = Q \, (\text{MGD}) \times C_{\text{dose}} \, (\text{mg/L}) \times 8.34 \, \left(\frac{\text{lb/Mgal}}{\text{mg/L}}\right)$$
      </div>

      <p>In metric SI engineering units:</p>
      <div class="formula-box">
        $$W_{\text{dry}} \, (\text{kg/day}) = \frac{Q \, (\text{m}^3/\text{day}) \times C_{\text{dose}} \, (\text{g/m}^3)}{1,000}$$
      </div>

      <p>Because commercial chemical deliveries are billed as liquid bulk tanker loads, the solution concentration ($C_{\text{liquid}}$) is determined from specific gravity ($SG$) and dry chemical weight fraction ($w$):</p>

      <div class="formula-box">
        $$C_{\text{liquid}} = 8.34 \times SG \times w \quad (\text{lb dry chemical per gallon of solution})$$
      </div>

      <p>The total commercial liquid feed rate ($Q_{\text{liquid}}$) and pump calibration drawdown rate ($q_{\text{drawdown}}$) are:</p>

      <div class="formula-box">
        $$Q_{\text{liquid}} \, (\text{GPD}) = \frac{W_{\text{dry}} \, (\text{lb/day})}{C_{\text{liquid}} \, (\text{lb/gal})}, \quad q_{\text{drawdown}} \, (\text{mL/min per pump}) = \frac{Q_{\text{liquid}} \, (\text{GPD}) \times 2.6288}{N_{\text{duty pumps}}}$$
      </div>

      <h2>Stoichiometric Alkalinity Consumption Comparison</h2>
      <p>Metal coagulant hydrolysis releases free hydronium ions ($\text{H}^+$), reacting with natural bicarbonate alkalinity ($\text{HCO}_3^-$) to generate dissolved carbon dioxide ($\text{CO}_2$). Stoichiometric consumption varies drastically across coagulants:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Coagulant Formulation</th>
              <th>Formula Weight (g/mol)</th>
              <th>Stoichiometric Reaction</th>
              <th>Alkalinity Consumed (mg/L as CaCO₃ per mg/L dry coagulant)</th>
              <th>Effective Coagulation pH Window</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Ferric Chloride (FeCl₃)</td>
              <td>162.2</td>
              <td>$$\text{FeCl}_3 + 3\text{HCO}_3^- \to \text{Fe(OH)}_3\downarrow + 3\text{Cl}^- + 3\text{CO}_2$$</td>
              <td><strong>0.925 mg/L</strong> (Heavy acidifier)</td>
              <td>4.0 &ndash; 11.0 (Very wide)</td>
            </tr>
            <tr>
              <td>Alum [Al₂(SO₄)₃·14H₂O]</td>
              <td>594.4</td>
              <td>$$\text{Al}_2(\text{SO}_4)_3 + 6\text{HCO}_3^- \to 2\text{Al(OH)}_3\downarrow + 3\text{SO}_4^{2-} + 6\text{CO}_2$$</td>
              <td><strong>0.505 mg/L</strong></td>
              <td>5.8 &ndash; 7.2 (Narrow)</td>
            </tr>
            <tr>
              <td>Ferric Sulfate [Fe₂(SO₄)₃]</td>
              <td>399.9</td>
              <td>$$\text{Fe}_2(\text{SO}_4)_3 + 6\text{HCO}_3^- \to 2\text{Fe(OH)}_3\downarrow + 3\text{SO}_4^{2-} + 6\text{CO}_2$$</td>
              <td><strong>0.751 mg/L</strong></td>
              <td>4.5 &ndash; 10.5</td>
            </tr>
            <tr>
              <td>Polyaluminum Chloride (70% Basic PAC)</td>
              <td>Polymeric</td>
              <td>Pre-neutralized Keggin Al₁₃ structure</td>
              <td><strong>0.15 &ndash; 0.25 mg/L</strong> (Minimal drop)</td>
              <td>5.0 &ndash; 8.5 (Stable)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <p>If residual alkalinity drops below $30\text{ mg/L as CaCO}_3$, coagulation efficiency deteriorates and finished water entering distribution becomes aggressively corrosive. In such scenarios, supplemental lime ($\text{Ca(OH)}_2$) or caustic soda ($\text{NaOH}$) must be co-fed to stabilize pH.</p>

      <h2>Dry Chemical Sludge Solids Generation Modeling</h2>
      <p>Clarifier underflow sludge mass consists of precipitated metal hydroxides combined with removed suspended raw water solids:</p>

      <div class="formula-box">
        $$W_{\text{sludge}} \, (\text{lb/day dry}) = Q \, (\text{MGD}) \times \left(k_{\text{metal}} \times C_{\text{dose}} + 1.0 \times \text{TSS}_{\text{removed}}\right) \times 8.34$$
      </div>
      <p>Where $k_{\text{metal}}$ represents the stoichiometric dry precipitate multiplier: $0.263$ for commercial alum, $0.660$ for ferric chloride ($\text{MW}_{\text{Fe(OH)}_3}/\text{MW}_{\text{FeCl}_3} = 106.9/162.2$), $0.535$ for ferric sulfate, and $0.350$ for polyaluminum chloride.</p>

      <h2>Practical Worked Case Study: 15 MGD Clarification Plant Ferric Dosing</h2>
      <div class="worked-example-card">
        <h3>Engineering Design Example: High Organic Color River Water Coagulation</h3>
        <p><strong>Treatment Context:</strong> A conventional municipal water treatment plant clarifies $15.0\text{ MGD}$ of surface river water characterized by high humic color ($45\text{ Pt-Co}$) and cold seasonal temperatures ($3.5^\circ\text{C}$). Due to poor alum performance in cold water, the plant utilizes commercial $38\%\text{ liquid ferric chloride}$ ($SG = 1.42$, containing $4.49\text{ lb dry FeCl}_3/\text{gal}$). Jar testing establishes an optimum dry coagulant dose of $35.0\text{ mg/L}$. Raw water alkalinity is $58.0\text{ mg/L as CaCO}_3$, and raw turbidity is $25\text{ NTU}$ (92% removal). Two duty diaphragm metering pumps share chemical injection.</p>

        <p><strong>Step 1: Calculate Daily Pure Chemical Mass:</strong></p>
        $$W_{\text{dry}} = 15.0\text{ MGD} \times 35.0\text{ mg/L} \times 8.34 = 4,378.5\text{ lb/day dry FeCl}_3\text{ (1,986.0 kg/day)}$$

        <p><strong>Step 2: Determine Commercial Liquid Volumetric Delivery:</strong></p>
        $$Q_{\text{liquid}} = \frac{4,378.5\text{ lb/day}}{4.49\text{ lb dry/gal}} = 975.17\text{ gal/day}$$
        $$\text{Hourly Feed Rate} = \frac{975.17\text{ GPD}}{24\text{ hours}} = 40.63\text{ GPH}$$

        <p><strong>Step 3: Diaphragm Metering Pump Calibration Rate:</strong></p>
        <p>Dividing across two duty pumps ($487.58\text{ GPD per pump}$):</p>
        $$\text{Pump Drawdown Rate} = 487.58\text{ GPD} \times 2.6288 = 1,281.8\text{ mL/min per pump}$$

        <p><strong>Step 4: Stoichiometric Alkalinity Depletion Verification:</strong></p>
        $$\text{Alkalinity Consumed} = 35.0\text{ mg/L} \times 0.925 = 32.38\text{ mg/L as CaCO}_3$$
        $$\text{Residual Alkalinity} = 58.0 - 32.38 = 25.62\text{ mg/L as CaCO}_3$$
        <p>Because residual alkalinity drops below the critical $30.0\text{ mg/L}$ floor, supplemental caustic soda feed ($50\%\text{ NaOH}$) is mandated to boost finished buffer by $10\text{ mg/L}$ ($8.0\text{ mg/L 100% NaOH}$ = $1,000\text{ lb/day pure NaOH}$).</p>

        <p><strong>Step 5: Daily Coagulation Sludge Solids Generation:</strong></p>
        $$W_{\text{sludge}} = 15.0 \times \left(0.66 \times 35.0 + 25 \times 0.92\right) \times 8.34 = 15.0 \times (23.10 + 23.00) \times 8.34 = 5,767.1\text{ lb/day dry solids}$$
      </div>

      <h2>Operational Best Practices and Rapid Mixing Criteria</h2>
      <p>Successful chemical coagulation depends critically on hydrodynamics and chemical dosing sequencing:</p>
      <ul>
        <li><strong>Camp-Stein Velocity Gradient ($G$):</strong> Destabilization via charge neutralization requires flash mixing at $G &gt; 700\text{ to }1,000\text{ s}^{-1}$ within $0.5\text{ to }2.0\text{ seconds}$ of coagulant injection. In-line static mixers or high-speed mechanical turbine impellers ensure instantaneous dispersion before metal hydroxide polymers precipitate prematurely.</li>
        <li><strong>Flocculation Tapering:</strong> Slow mixing stages should be compartmentalized into three sequential basins with tapered mixing intensity ($G = 60\text{ s}^{-1} \to 40\text{ s}^{-1} \to 20\text{ s}^{-1}$) to promote floc growth without shearing fragile colloidal bridges.</li>
        <li><strong>Feed Line Scaling &amp; Flushing:</strong> Ferric chloride hydrolyzes upon contact with water, precipitating iron stains and crystalline deposits. Chemical metering skids must include an automated demineralized water flushing manifold that purges injection quill nozzles whenever the plant trips offline.</li>
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
          <p class="footer-about">High-precision water treatment, chemical dosing, and environmental engineering calculation tools conforming to AWWA and EPA standards.</p>
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
            <li><a href="https://www.awwa.org" target="_blank" rel="noopener">AWWA Coagulant Standards</a></li>
            <li><a href="https://www.epa.gov" target="_blank" rel="noopener">EPA Surface Water Treatment Rules</a></li>
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
    const COAG_PRESETS = {
      ferric_cl: { sg: 1.42, strength: 38.0, alkFactor: 0.925, sludgeFactor: 0.660, name: "Ferric Chloride (FeCl₃)" },
      alum_liquid: { sg: 1.33, strength: 48.5, alkFactor: 0.505, sludgeFactor: 0.263, name: "Liquid Alum (Al₂(SO₄)₃)" },
      ferric_so4: { sg: 1.55, strength: 50.0, alkFactor: 0.751, sludgeFactor: 0.535, name: "Ferric Sulfate (Fe₂(SO₄)₃)" },
      pac_liquid: { sg: 1.25, strength: 30.0, alkFactor: 0.200, sludgeFactor: 0.350, name: "Polyaluminum Chloride (PAC)" },
      alum_dry: { sg: 1.00, strength: 100.0, alkFactor: 0.505, sludgeFactor: 0.263, name: "Dry Granular Alum" },
      custom: { sg: 1.42, strength: 38.0, alkFactor: 0.700, sludgeFactor: 0.500, name: "Custom Coagulant" }
    };

    function updateCoagulantPreset() {
      const type = document.getElementById("coagulantType").value;
      document.getElementById("customCoagGrid").style.display = (type === "custom") ? "grid" : "none";
    }

    function toggleFlowUnitLabels() {
      const u = document.getElementById("plantFlowUnit").value;
      const lbl = document.getElementById("flowValLabel");
      if (u === "mgd") lbl.textContent = "Plant Influent Flow Rate (MGD)";
      else if (u === "gpm") lbl.textContent = "Plant Influent Flow Rate (GPM)";
      else if (u === "m3h") lbl.textContent = "Plant Influent Flow Rate (m³/hour)";
      else if (u === "m3d") lbl.textContent = "Plant Influent Flow Rate (m³/day)";
      else if (u === "lps") lbl.textContent = "Plant Influent Flow Rate (L/s)";
    }

    function calcCoagulantDosing() {
      const u = document.getElementById("plantFlowUnit").value;
      const flowIn = parseFloat(document.getElementById("plantFlowVal").value) || 0;
      const dose = parseFloat(document.getElementById("targetCoagDose").value) || 0;
      const rawAlk = parseFloat(document.getElementById("rawWaterAlkalinity").value) || 0;
      const coagKey = document.getElementById("coagulantType").value;
      const pumps = parseInt(document.getElementById("numCoagPumps").value) || 1;
      const tss = parseFloat(document.getElementById("rawTurbidityTss").value) || 0;
      const bulkCost = parseFloat(document.getElementById("bulkCoagCost").value) || 0;

      if (flowIn <= 0 || dose <= 0) {
        alert("Please enter positive values for water flow rate and coagulant dose.");
        return;
      }

      // Convert flow to MGD and m3/day
      let flowMGD = 0;
      let flowM3D = 0;
      if (u === "mgd") {
        flowMGD = flowIn;
        flowM3D = flowMGD * 3785.41;
      } else if (u === "gpm") {
        flowMGD = (flowIn * 1440) / 1000000;
        flowM3D = flowMGD * 3785.41;
      } else if (u === "m3h") {
        flowM3D = flowIn * 24;
        flowMGD = flowM3D / 3785.41;
      } else if (u === "m3d") {
        flowM3D = flowIn;
        flowMGD = flowM3D / 3785.41;
      } else if (u === "lps") {
        flowM3D = (flowIn * 86400) / 1000;
        flowMGD = flowM3D / 3785.41;
      }

      // Coagulant properties
      let p = COAG_PRESETS[coagKey];
      let sg = p.sg;
      let strength = p.strength;
      let alkFactor = p.alkFactor;
      let sludgeFactor = p.sludgeFactor;

      if (coagKey === "custom") {
        sg = parseFloat(document.getElementById("coagSG").value) || 1.42;
        strength = parseFloat(document.getElementById("coagStrength").value) || 38.0;
      }

      const isDry = coagKey === "alum_dry";
      const dryLbsDay = flowMGD * dose * 8.34;
      const dryKgDay = (flowM3D * dose) / 1000;

      const activeLbPerGal = isDry ? 1.0 : (8.34 * sg * (strength / 100));
      const liquidGPD = isDry ? 0 : dryLbsDay / activeLbPerGal;
      const liquidGPH = liquidGPD / 24;
      const liquidLPD = liquidGPD * 3.78541;

      // Pump drawdown
      const gpdPerPump = liquidGPD / pumps;
      const mlMinPerPump = gpdPerPump * 2.6288;
      const lphPerPump = (gpdPerPump * 3.78541) / 24;

      // Alkalinity
      const alkConsumed = dose * alkFactor;
      const residAlk = rawAlk - alkConsumed;

      // Sludge (lb/day)
      const drySludgeLbs = flowMGD * (sludgeFactor * dose + tss * 0.90) * 8.34;
      const drySludgeKg = drySludgeLbs * 0.453592;

      const dailyCost = isDry ? (dryLbsDay * (bulkCost / 5.38)) : (liquidGPD * bulkCost);

      // Populate UI
      document.getElementById("resDryMass").textContent = dryLbsDay.toFixed(1) + " lbs/day";
      document.getElementById("resDryMassAlt").textContent = dryKgDay.toFixed(1) + " kg/day dry pure chemical basis";

      if (isDry) {
        document.getElementById("resPumpDrawdown").textContent = (dryLbsDay / (pumps * 24)).toFixed(2) + " lbs/hr";
        document.getElementById("resPumpDrawdownAlt").textContent = "Dry chemical feeder rate per hopper";
        document.getElementById("resLiquidDay").textContent = "N/A (Dry Solid)";
        document.getElementById("resLiquidDayAlt").textContent = dryLbsDay.toFixed(1) + " lbs granular chemical / day";
      } else {
        document.getElementById("resPumpDrawdown").textContent = mlMinPerPump.toFixed(1) + " mL/min";
        document.getElementById("resPumpDrawdownAlt").textContent = lphPerPump.toFixed(2) + " L/h (" + (liquidGPH / pumps).toFixed(2) + " GPH per pump)";
        document.getElementById("resLiquidDay").textContent = liquidGPH.toFixed(2) + " GPH";
        document.getElementById("resLiquidDayAlt").textContent = liquidGPD.toFixed(1) + " GPD (" + liquidLPD.toFixed(1) + " L/day)";
      }

      document.getElementById("resResidAlk").textContent = residAlk.toFixed(1) + " mg/L";
      const alkStatus = document.getElementById("resAlkStatus");
      if (residAlk >= 30) {
        alkStatus.textContent = "Adequate buffer (Residual ≥ 30 mg/L as CaCO₃)";
        alkStatus.style.color = "var(--success, #16a34a)";
      } else if (residAlk > 0) {
        alkStatus.textContent = "Warning: Marginal buffer (< 30 mg/L). Risk of pH drop.";
        alkStatus.style.color = "#ca8a04";
      } else {
        alkStatus.textContent = "CRITICAL: Complete alkalinity depletion! Severe pH collapse.";
        alkStatus.style.color = "#dc2626";
      }

      document.getElementById("resConsumedAlk").textContent = alkConsumed.toFixed(1) + " mg/L as CaCO₃ (" + ((alkConsumed / (rawAlk || 1)) * 100).toFixed(0) + "% of raw buffer)";

      if (residAlk < 30) {
        const deficit = 30 - residAlk;
        const causticNeeded = deficit * 0.80 * flowMGD * 8.34;
        document.getElementById("resBufferNeed").textContent = "Required: " + causticNeeded.toFixed(1) + " lbs/day 100% NaOH (or " + (causticNeeded / 6.38).toFixed(1) + " GPD 50% caustic) to maintain 30 mg/L residual";
      } else {
        document.getElementById("resBufferNeed").textContent = "None required. Natural raw alkalinity buffer is sufficient.";
      }

      document.getElementById("resSludgeTotal").textContent = drySludgeLbs.toFixed(1) + " lbs/day dry solids (" + drySludgeKg.toFixed(1) + " kg/day)";
      document.getElementById("resStorageMonth").textContent = (liquidGPD * 30).toLocaleString(undefined, {maximumFractionDigits: 0}) + " gal/month bulk storage (" + ((liquidGPD * 30 * sg * 8.34) / 2000).toFixed(1) + " tons)";
      document.getElementById("resTotalCost").textContent = "$" + dailyCost.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2}) + " / day ($" + (dailyCost * 30).toLocaleString(undefined, {maximumFractionDigits: 0}) + " / month)";

      document.getElementById("coagResults").style.display = "block";
    }
  </script>
</body>
</html>
"""

TOOL_2_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Combined Gas Law Calculator | (P₁V₁)/T₁ = (P₂V₂)/T₂ Multi-State Sizer</title>
  <meta name="description" content="Calculate pressure, volume, and absolute temperature changes for gases using the Combined Gas Law (P1V1/T1 = P2V2/T2), with Boyle, Charles, and Gay-Lussac states.">
  <link rel="canonical" href="https://calchub.cloud/combined-gas-law-calculator.html">
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
        "name": "Combined Gas Law Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Solves for any unknown thermodynamic variable across pressure, volume, and temperature transitions using the Combined Gas Law (P1*V1)/T1 = (P2*V2)/T2.",
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
            "name": "What is the Combined Gas Law formula and when is it applicable?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The Combined Gas Law combines Boyle's Law, Charles's Law, and Gay-Lussac's Law into a single thermodynamic equation: (P1 * V1) / T1 = (P2 * V2) / T2. It applies to any constant-mass ideal gas process where pressure, volume, and temperature vary simultaneously."
            }
          },
          {
            "@type": "Question",
            "name": "Why must temperatures always be expressed in Kelvin or Rankine?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Gas laws describe molecular translational energy, which is zero only at Absolute Zero. Using relative scales like Celsius or Fahrenheit yields mathematically invalid negative numbers or divide-by-zero errors. Always convert temperatures to Kelvin (K = °C + 273.15) or Rankine (°R = °F + 459.67)."
            }
          },
          {
            "@type": "Question",
            "name": "How does the Combined Gas Law relate to individual gas laws?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Holding temperature constant (T1 = T2) reduces the formula to Boyle's Law: P1 * V1 = P2 * V2. Holding pressure constant (P1 = P2) yields Charles's Law: V1 / T1 = V2 / T2. Holding volume constant (V1 = V2) yields Gay-Lussac's Law: P1 / T1 = P2 / T2."
            }
          },
          {
            "@type": "Question",
            "name": "What are Standard Temperature and Pressure (STP) versus Normal Temperature and Pressure (NTP)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "IUPAC defines STP as 0°C (273.15 K) and 1 bar (100 kPa or 0.987 atm), where one mole of ideal gas occupies 22.71 L. NIST and older engineering standards use 0°C and 1.0 atm (101.325 kPa), yielding 22.414 L/mol. NTP is defined as 20°C (293.15 K) and 1.0 atm, yielding 24.04 L/mol."
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
      <span>Combined Gas Law Calculator</span>
    </nav>

    <h1 class="tool-title">Combined Gas Law Calculator (P₁V₁/T₁ = P₂V₂/T₂)</h1>
    <p class="tool-subtitle">Simultaneous Pressure, Volume &amp; Temperature State Transformation Sizer</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="solveVariable">Select Variable to Solve For</label>
            <select id="solveVariable" class="form-control" onchange="updateCombinedInputs()">
              <option value="v2" selected>Final Volume (V₂)</option>
              <option value="p2">Final Pressure (P₂)</option>
              <option value="t2">Final Temperature (T₂)</option>
              <option value="v1">Initial Volume (V₁)</option>
              <option value="p1">Initial Pressure (P₁)</option>
              <option value="t1">Initial Temperature (T₁)</option>
            </select>
          </div>

          <h4 style="margin:0.5rem 0;color:var(--text-main);border-bottom:1px solid var(--border-light);padding-bottom:0.25rem;">Initial State Parameters (State 1)</h4>

          <!-- P1 -->
          <div id="p1CmbGroup" class="grid-2-col">
            <div class="form-group">
              <label for="p1Input">Initial Absolute Pressure (P₁)</label>
              <input type="number" id="p1Input" class="form-control" value="1.01325" step="0.01" min="0.0001">
            </div>
            <div class="form-group">
              <label for="p1UnitSel">P₁ Pressure Unit</label>
              <select id="p1UnitSel" class="form-control">
                <option value="atm">Atmospheres (atm)</option>
                <option value="bar" selected>Bar (bar absolute)</option>
                <option value="kpa">Kilopascals (kPa)</option>
                <option value="psi">Pounds/sq in (psia)</option>
                <option value="pa">Pascals (Pa)</option>
              </select>
            </div>
          </div>

          <!-- V1 -->
          <div id="v1CmbGroup" class="grid-2-col">
            <div class="form-group">
              <label for="v1Input">Initial Volume (V₁)</label>
              <input type="number" id="v1Input" class="form-control" value="50.0" step="1.0" min="0.0001">
            </div>
            <div class="form-group">
              <label for="v1UnitSel">V₁ Volume Unit</label>
              <select id="v1UnitSel" class="form-control">
                <option value="l" selected>Liters (L)</option>
                <option value="m3">Cubic Meters (m³)</option>
                <option value="cm3">Cubic Centimeters (cm³ / mL)</option>
                <option value="ft3">Cubic Feet (ft³)</option>
                <option value="gal">US Gallons (gal)</option>
              </select>
            </div>
          </div>

          <!-- T1 -->
          <div id="t1CmbGroup" class="grid-2-col">
            <div class="form-group">
              <label for="t1Input">Initial Temperature (T₁)</label>
              <input type="number" id="t1Input" class="form-control" value="20.0" step="1.0">
            </div>
            <div class="form-group">
              <label for="t1UnitSel">T₁ Temperature Scale</label>
              <select id="t1UnitSel" class="form-control">
                <option value="c" selected>Celsius (°C)</option>
                <option value="k">Kelvin (K)</option>
                <option value="f">Fahrenheit (°F)</option>
                <option value="r">Rankine (°R)</option>
              </select>
            </div>
          </div>

          <h4 style="margin:1rem 0 0.5rem;color:var(--text-main);border-bottom:1px solid var(--border-light);padding-bottom:0.25rem;">Final State Parameters (State 2)</h4>

          <!-- P2 -->
          <div id="p2CmbGroup" class="grid-2-col">
            <div class="form-group">
              <label for="p2Input">Final Absolute Pressure (P₂)</label>
              <input type="number" id="p2Input" class="form-control" value="3.5" step="0.1" min="0.0001">
            </div>
            <div class="form-group">
              <label for="p2UnitSel">P₂ Pressure Unit</label>
              <select id="p2UnitSel" class="form-control">
                <option value="atm">Atmospheres (atm)</option>
                <option value="bar" selected>Bar (bar absolute)</option>
                <option value="kpa">Kilopascals (kPa)</option>
                <option value="psi">Pounds/sq in (psia)</option>
                <option value="pa">Pascals (Pa)</option>
              </select>
            </div>
          </div>

          <!-- V2 -->
          <div id="v2CmbGroup" class="grid-2-col" style="display:none;">
            <div class="form-group">
              <label for="v2Input">Final Volume (V₂)</label>
              <input type="number" id="v2Input" class="form-control" value="25.0" step="1.0" min="0.0001">
            </div>
            <div class="form-group">
              <label for="v2UnitSel">V₂ Volume Unit</label>
              <select id="v2UnitSel" class="form-control">
                <option value="l" selected>Liters (L)</option>
                <option value="m3">Cubic Meters (m³)</option>
                <option value="cm3">Cubic Centimeters (cm³ / mL)</option>
                <option value="ft3">Cubic Feet (ft³)</option>
                <option value="gal">US Gallons (gal)</option>
              </select>
            </div>
          </div>

          <!-- T2 -->
          <div id="t2CmbGroup" class="grid-2-col">
            <div class="form-group">
              <label for="t2Input">Final Temperature (T₂)</label>
              <input type="number" id="t2Input" class="form-control" value="85.0" step="1.0">
            </div>
            <div class="form-group">
              <label for="t2UnitSel">T₂ Temperature Scale</label>
              <select id="t2UnitSel" class="form-control">
                <option value="c" selected>Celsius (°C)</option>
                <option value="k">Kelvin (K)</option>
                <option value="f">Fahrenheit (°F)</option>
                <option value="r">Rankine (°R)</option>
              </select>
            </div>
          </div>

          <div class="form-group">
            <label for="gasIdCmb">Gas Molecular Identity</label>
            <select id="gasIdCmb" class="form-control">
              <option value="air" selected>Dry Atmospheric Air (MW = 28.97 g/mol)</option>
              <option value="n2">Pure Nitrogen N₂ (MW = 28.01 g/mol)</option>
              <option value="o2">Pure Oxygen O₂ (MW = 32.00 g/mol)</option>
              <option value="co2">Carbon Dioxide CO₂ (MW = 44.01 g/mol)</option>
              <option value="he">Helium He (MW = 4.003 g/mol)</option>
              <option value="ch4">Methane CH₄ (MW = 16.04 g/mol)</option>
              <option value="h2">Hydrogen H₂ (MW = 2.016 g/mol)</option>
            </select>
          </div>

          <button type="button" class="btn btn-primary" onclick="calcCombinedGasLaw()">Solve Combined Gas Law</button>
        </div>

        <div id="combinedResults" class="results-box" style="display:none;margin-top:1.5rem;">
          <h3 class="results-title">Combined Gas Law Solution &amp; Thermodynamic Diagnostics</h3>
          <div class="result-grid">
            <div class="result-card">
              <div class="result-label" id="resCmbTargetLabel">Calculated Value</div>
              <div class="result-value highlight" id="resCmbTargetVal">--</div>
              <div class="result-subtext" id="resCmbTargetAlt">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Volume Ratio (V₂ / V₁)</div>
              <div class="result-value" id="resCmbVolRatio">--</div>
              <div class="result-subtext" id="resCmbVolRatioDesc">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Pressure Ratio (P₂ / P₁)</div>
              <div class="result-value" id="resCmbPresRatio">--</div>
              <div class="result-subtext" id="resCmbPresRatioDesc">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Gas Molar Quantity</div>
              <div class="result-value highlight" id="resCmbMoles">--</div>
              <div class="result-subtext" id="resCmbMass">--</div>
            </div>
          </div>

          <div class="result-details" style="margin-top:1rem;padding:1rem;background:var(--card-bg);border-radius:6px;border:1px solid var(--border-light);">
            <h4 style="margin-top:0;">Process Verification &amp; Standard State Comparisons</h4>
            <ul style="margin-bottom:0;line-height:1.7;">
              <li><strong>Thermodynamic State Constant:</strong> <span id="resCmbConstant">--</span></li>
              <li><strong>Equivalent Volume at IUPAC STP (0°C, 1 bar):</strong> <span id="resCmbStpVol">--</span></li>
              <li><strong>Equivalent Volume at NIST Normal (20°C, 1 atm):</strong> <span id="resCmbNtpVol">--</span></li>
              <li><strong>Density Shift:</strong> <span id="resCmbDensityShift">--</span></li>
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
            <li><a href="alum-dosing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Alum Dosing Calculator</a></li>
            <li><a href="caustic-soda-dosing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Caustic Soda Dosing Calculator</a></li>
          </ul>
          <div style="margin-top:1.25rem;padding-top:1rem;border-top:1px solid var(--border-light);">
            <a href="chemical.html" class="sidebar-category-link">View All Chemical Calculators &rarr;</a>
          </div>
        </div>
      </aside>
    </div>

    <!-- Technical Educational Article Body (1000+ Words) -->
    <article class="article-body">
      <h2>Thermodynamic Derivation of the Combined Gas Law</h2>
      <p>The Combined Gas Law represents the mathematical unification of the three classical empirical gas relations discovered between the mid-seventeenth and early nineteenth centuries: <strong>Boyle's Law</strong> (Robert Boyle, 1662: $P \propto 1/V$ at constant $T$), <strong>Charles's Law</strong> (Jacques Charles, 1787: $V \propto T$ at constant $P$), and <strong>Gay-Lussac's Law</strong> (Joseph Louis Gay-Lussac, 1802: $P \propto T$ at constant $V$). While each individual empirical law restricts two thermodynamic state variables to examine the interdependence of the remaining two, real-world aerospace, internal combustion, and chemical engineering systems involve simultaneous variations across pressure, volume, and temperature.</p>

      <p>By considering a fixed mass of gas (constant moles $n$) undergoing an arbitrary transition from an initial thermodynamic equilibrium state $(P_1, V_1, T_1)$ to a final equilibrium state $(P_2, V_2, T_2)$, the process can be conceptualized as two sequential steps: an initial isothermal expansion to an intermediate pressure, followed by an isobaric heating to the final temperature. Combining these transformations yields the universal equation of state:</p>

      <div class="formula-box">
        $$\frac{P_1 V_1}{T_1} = \frac{P_2 V_2}{T_2} = n R = \text{constant}$$
      </div>

      <p>Where $R = 8.314462\text{ J/(mol}\cdot\text{K)}$ is the universal gas constant. This equation proves that the quantity $\frac{P V}{T}$ is an invariant property for any closed ideal gas system undergoing non-chemical transformation.</p>

      <h2>Analytical Solutions for the Six State Variables</h2>
      <p>Given any five known thermodynamic boundary conditions, the unknown sixth variable can be solved directly through algebraic rearrangement:</p>

      <div class="formula-box">
        $$V_2 = \frac{P_1 V_1 T_2}{P_2 T_1}, \quad P_2 = \frac{P_1 V_1 T_2}{V_2 T_1}, \quad T_2 = \frac{P_2 V_2 T_1}{P_1 V_1}$$
      </div>
      <div class="formula-box">
        $$V_1 = \frac{P_2 V_2 T_1}{P_1 T_2}, \quad P_1 = \frac{P_2 V_2 T_1}{V_1 T_2}, \quad T_1 = \frac{P_1 V_1 T_2}{P_2 V_2}$$
      </div>

      <p>It is fundamentally critical that absolute units are utilized throughout. Gauge pressures (psig, bar-g) must be converted to absolute pressure ($P_{\text{abs}} = P_{\text{gauge}} + P_{\text{atm}}$), and temperatures must be converted to the thermodynamic Kelvin or Rankine scales ($T_{\text{abs}} = T_{^\circ\text{C}} + 273.15$ or $T_{\text{abs}} = T_{^\circ\text{F}} + 459.67$).</p>

      <h2>Boundary Case Specializations</h2>
      <p>The Combined Gas Law serves as the analytical parent equation for all classic two-variable gas relationships:</p>
      <ul>
        <li><strong>Isothermal Boundary ($T_1 = T_2$):</strong> The temperature terms cancel identically, yielding <strong>Boyle's Law</strong>:
        $$P_1 V_1 = P_2 V_2$$
        Applicable to slow, highly conductive gas expansion or compression where infinite heat sink contact maintains uniform temperature.</li>
        <li><strong>Isobaric Boundary ($P_1 = P_2$):</strong> The pressure terms cancel identically, yielding <strong>Charles's Law</strong>:
        $$\frac{V_1}{T_1} = \frac{V_2}{T_2}$$
        Applicable to constant-pressure systems such as hot air balloons, weighted piston cylinders, and open-vented architectural spaces.</li>
        <li><strong>Isochoric / Isometric Boundary ($V_1 = V_2$):</strong> The volume terms cancel identically, yielding <strong>Gay-Lussac's Law</strong> (Amontons's Law):
        $$\frac{P_1}{T_1} = \frac{P_2}{T_2}$$
        Applicable to rigid, unyielding enclosures such as autoclave chambers, scuba cylinders, and fire extinguisher tanks.</li>
      </ul>

      <h2>Standard State Conventions (STP vs. NTP vs. EPA Standard)</h2>
      <p>Engineering gas volume measurements are meaningless without citing the reference pressure and temperature. Global standards organizations define differing standard states:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Standard Definition</th>
              <th>Standard Pressure</th>
              <th>Standard Temperature</th>
              <th>Molar Volume (L/mol)</th>
              <th>Primary Regulatory / Engineering Context</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>IUPAC Modern STP (Post-1982)</td>
              <td>1.000 bar (100.0 kPa)</td>
              <td>0.0°C (273.15 K)</td>
              <td>22.711 L/mol</td>
              <td>Modern Chemistry &amp; IUPAC Thermodynamic Tables</td>
            </tr>
            <tr>
              <td>IUPAC Classical STP (Pre-1982)</td>
              <td>1.000 atm (101.325 kPa)</td>
              <td>0.0°C (273.15 K)</td>
              <td>22.414 L/mol</td>
              <td>Classical Physics &amp; Legacy Textbooks</td>
            </tr>
            <tr>
              <td>NIST / ISO Normal (NTP)</td>
              <td>1.000 atm (101.325 kPa)</td>
              <td>20.0°C (293.15 K)</td>
              <td>24.042 L/mol</td>
              <td>Industrial Gas Compressors &amp; Flow Meters (Nm³/h)</td>
            </tr>
            <tr>
              <td>US EPA Standard Conditions</td>
              <td>1.000 atm (29.92 inHg)</td>
              <td>20.0°C (68.0°F / 293.15 K)</td>
              <td>24.042 L/mol</td>
              <td>Air Emissions &amp; Stack Gas Testing (SCFM)</td>
            </tr>
            <tr>
              <td>US Petroleum Standard (AGA)</td>
              <td>14.73 psia (101.56 kPa)</td>
              <td>60.0°F (15.56°C / 288.71 K)</td>
              <td>23.681 L/mol (379.48 scf/lbmol)</td>
              <td>Natural Gas Pipelines &amp; Custody Transfer (MMSCFD)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <p>To convert an operational volume ($V_{\text{actual}}$) measured at $(P_{\text{act}}, T_{\text{act}})$ to standard conditions ($V_{\text{std}}$):</p>
      <div class="formula-box">
        $$V_{\text{std}} = V_{\text{act}} \times \left(\frac{P_{\text{act}}}{P_{\text{std}}}\right) \times \left(\frac{T_{\text{std}}}{T_{\text{act}}}\right)$$
      </div>

      <h2>Practical Worked Case Study: Weather Balloon Stratospheric Ascent</h2>
      <div class="worked-example-card">
        <h3>Engineering Design Example: Radiosonde High-Altitude Balloon Expansion</h3>
        <p><strong>Scenario:</strong> A scientific latex weather sounding balloon is launched from sea level where surface barometric pressure is $P_1 = 1.013\text{ bar}$ ($101.3\text{ kPa}$), ambient temperature is $T_1 = 22.0^\circ\text{C}$ ($295.15\text{ K}$), and initial helium inflation volume is $V_1 = 5.00\text{ m}^3$ ($5,000\text{ Liters}$). The balloon ascends into the stratosphere to an altitude of $25,000\text{ meters}$, where atmospheric pressure drops precipitously to $P_2 = 0.025\text{ bar}$ ($2.5\text{ kPa}$) and ambient temperature plummets to $T_2 = -55.0^\circ\text{C}$ ($218.15\text{ K}$). Assume ideal helium gas behavior ($MW = 4.003\text{ g/mol}$).</p>

        <p><strong>Step 1: Convert Temperatures to Absolute Kelvin:</strong></p>
        $$T_1 = 22.0 + 273.15 = 295.15\text{ K}$$
        $$T_2 = -55.0 + 273.15 = 218.15\text{ K}$$

        <p><strong>Step 2: Solve for Final Stratospheric Volume (V₂) via Combined Gas Law:</strong></p>
        $$V_2 = \frac{P_1 V_1 T_2}{P_2 T_1} = \frac{1.013\text{ bar} \times 5.00\text{ m}^3 \times 218.15\text{ K}}{0.025\text{ bar} \times 295.15\text{ K}} = \frac{1,104.93}{7.37875} = 149.75\text{ m}^3$$
        <p>Volume expansion ratio:</p>
        $$r_v = \frac{V_2}{V_1} = \frac{149.75}{5.00} = 29.95 : 1\text{ (A 30-fold volumetric increase)}$$

        <p><strong>Step 3: Competing Effects Analysis:</strong></p>
        <p>The massive pressure drop ($1.013 \to 0.025\text{ bar}$) alone would drive a 40.52-fold volume expansion ($\frac{P_1}{P_2} = 40.52$). However, intense thermal cooling ($295.15 \to 218.15\text{ K}$) causes an isobaric contraction factor of $0.739$ ($\frac{T_2}{T_1} = 0.739$). The Combined Gas Law synthesizes these competing physical mechanisms into the exact resultant volume: $40.52 \times 0.739 = 29.95$.</p>

        <p><strong>Step 4: Helium Mass and Density Shift:</strong></p>
        <p>Total contained helium moles:</p>
        $$n = \frac{P_1 V_1}{R T_1} = \frac{101,300\text{ Pa} \times 5.00\text{ m}^3}{8.3145 \times 295.15\text{ K}} = 206.4\text{ moles}$$
        $$m_{\text{He}} = 206.4\text{ mol} \times 0.004003\text{ kg/mol} = 0.826\text{ kg (1.82 lbs)}$$
        <p>Initial sea level density: $\rho_1 = \frac{0.826}{5.00} = 0.165\text{ kg/m}^3$.</p>
        <p>Stratospheric burst density: $\rho_2 = \frac{0.826}{149.75} = 0.00552\text{ kg/m}^3$.</p>
      </div>

      <h2>Engineering Applications and Real-Gas Limits</h2>
      <p>Deploying the Combined Gas Law requires understanding its practical engineering boundaries:</p>
      <ul>
        <li><strong>Internal Combustion Engine Compression Stroke:</strong> In a Diesel engine, the air charge is compressed from $(P_1 = 1\text{ bar}, V_1 = 500\text{ cm}^3, T_1 = 300\text{ K})$ down to clearance volume $V_2 = 25\text{ cm}^3$ ($20:1$ compression ratio). However, because compression occurs within milliseconds, heat cannot escape through the cylinder walls; the process is <strong>isentropic/adiabatic</strong> ($P V^\gamma = \text{const}$ with $\gamma = 1.4$), raising final temperature to over $900\text{ K}$ and auto-igniting injected fuel.</li>
        <li><strong>Compressibility Factor ($Z$) at High Pressures:</strong> At extreme pressures ($P &gt; 50\text{ bar}$) or temperatures near gas liquefaction points, intermolecular attractions and finite molecular volumes violate ideal gas assumptions. Engineers modify the law by applying compressibility factors:
        $$\frac{P_1 V_1}{Z_1 T_1} = \frac{P_2 V_2}{Z_2 T_2}$$
        </li>
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
            <li><a href="https://www.iupac.org" target="_blank" rel="noopener">IUPAC Gold Book Standards</a></li>
            <li><a href="https://www.asme.org" target="_blank" rel="noopener">ASME Boiler &amp; Pressure Vessel</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    const GAS_MW_MAP = {
      air: 28.97,
      n2: 28.01,
      o2: 32.00,
      co2: 44.01,
      he: 4.003,
      ch4: 16.04,
      h2: 2.016
    };

    function updateCombinedInputs() {
      const v = document.getElementById("solveVariable").value;
      document.getElementById("p1CmbGroup").style.display = v === "p1" ? "none" : "grid";
      document.getElementById("v1CmbGroup").style.display = v === "v1" ? "none" : "grid";
      document.getElementById("t1CmbGroup").style.display = v === "t1" ? "none" : "grid";
      document.getElementById("p2CmbGroup").style.display = v === "p2" ? "none" : "grid";
      document.getElementById("v2CmbGroup").style.display = v === "v2" ? "none" : "grid";
      document.getElementById("t2CmbGroup").style.display = v === "t2" ? "none" : "grid";
    }

    function toPa(val, unit) {
      if (unit === "atm") return val * 101325;
      if (unit === "bar") return val * 100000;
      if (unit === "kpa") return val * 1000;
      if (unit === "psi") return val * 6894.757;
      return val;
    }

    function fromPa(pa, unit) {
      if (unit === "atm") return pa / 101325;
      if (unit === "bar") return pa / 100000;
      if (unit === "kpa") return pa / 1000;
      if (unit === "psi") return pa / 6894.757;
      return pa;
    }

    function toM3Cmb(val, unit) {
      if (unit === "l") return val * 0.001;
      if (unit === "cm3") return val * 0.000001;
      if (unit === "ft3") return val * 0.0283168;
      if (unit === "gal") return val * 0.00378541;
      return val;
    }

    function fromM3Cmb(m3, unit) {
      if (unit === "l") return m3 * 1000;
      if (unit === "cm3") return m3 * 1000000;
      if (unit === "ft3") return m3 / 0.0283168;
      if (unit === "gal") return m3 / 0.00378541;
      return m3;
    }

    function toKCmb(val, scale) {
      if (scale === "c") return val + 273.15;
      if (scale === "k") return val;
      if (scale === "f") return (val - 32) * (5 / 9) + 273.15;
      if (scale === "r") return val * (5 / 9);
      return val;
    }

    function fromKCmb(k, scale) {
      if (scale === "c") return k - 273.15;
      if (scale === "k") return k;
      if (scale === "f") return (k - 273.15) * (9 / 5) + 32;
      if (scale === "r") return k * (9 / 5);
      return k;
    }

    function calcCombinedGasLaw() {
      const target = document.getElementById("solveVariable").value;
      const gasKey = document.getElementById("gasIdCmb").value;
      const mw = GAS_MW_MAP[gasKey];

      let p1_pa = 0, v1_m3 = 0, t1_k = 0;
      let p2_pa = 0, v2_m3 = 0, t2_k = 0;

      if (target !== "p1") {
        p1_pa = toPa(parseFloat(document.getElementById("p1Input").value) || 0, document.getElementById("p1UnitSel").value);
      }
      if (target !== "v1") {
        v1_m3 = toM3Cmb(parseFloat(document.getElementById("v1Input").value) || 0, document.getElementById("v1UnitSel").value);
      }
      if (target !== "t1") {
        t1_k = toKCmb(parseFloat(document.getElementById("t1Input").value) || 0, document.getElementById("t1UnitSel").value);
      }
      if (target !== "p2") {
        p2_pa = toPa(parseFloat(document.getElementById("p2Input").value) || 0, document.getElementById("p2UnitSel").value);
      }
      if (target !== "v2") {
        v2_m3 = toM3Cmb(parseFloat(document.getElementById("v2Input").value) || 0, document.getElementById("v2UnitSel").value);
      }
      if (target !== "t2") {
        t2_k = toKCmb(parseFloat(document.getElementById("t2Input").value) || 0, document.getElementById("t2UnitSel").value);
      }

      let resLabel = "";
      let resVal = "";
      let resAlt = "";

      // (P1 * V1) / T1 = (P2 * V2) / T2
      if (target === "v2") {
        if (p2_pa <= 0 || t1_k <= 0) { alert("P2 and T1 must be positive non-zero values."); return; }
        v2_m3 = (p1_pa * v1_m3 * t2_k) / (p2_pa * t1_k);
        const u = document.getElementById("v1UnitSel").value;
        resLabel = "Final Volume (V₂)";
        resVal = fromM3Cmb(v2_m3, u).toFixed(4) + " " + u.toUpperCase();
        resAlt = (v2_m3 * 1000).toFixed(2) + " L (" + v2_m3.toFixed(4) + " m³)";
      } else if (target === "p2") {
        if (v2_m3 <= 0 || t1_k <= 0) { alert("V2 and T1 must be positive non-zero values."); return; }
        p2_pa = (p1_pa * v1_m3 * t2_k) / (v2_m3 * t1_k);
        const u = document.getElementById("p1UnitSel").value;
        resLabel = "Final Absolute Pressure (P₂)";
        resVal = fromPa(p2_pa, u).toFixed(4) + " " + u.toUpperCase();
        resAlt = (p2_pa / 100000).toFixed(3) + " bar (" + (p2_pa / 6894.757).toFixed(2) + " psia)";
      } else if (target === "t2") {
        if (p1_pa <= 0 || v1_m3 <= 0) { alert("P1 and V1 must be positive non-zero values."); return; }
        t2_k = (p2_pa * v2_m3 * t1_k) / (p1_pa * v1_m3);
        const s = document.getElementById("t1UnitSel").value;
        resLabel = "Final Temperature (T₂)";
        resVal = fromKCmb(t2_k, s).toFixed(2) + " °" + s.toUpperCase();
        resAlt = t2_k.toFixed(2) + " K (" + (t2_k - 273.15).toFixed(2) + " °C)";
      } else if (target === "v1") {
        if (p1_pa <= 0 || t2_k <= 0) { alert("P1 and T2 must be positive non-zero values."); return; }
        v1_m3 = (p2_pa * v2_m3 * t1_k) / (p1_pa * t2_k);
        const u = document.getElementById("v2UnitSel").value;
        resLabel = "Initial Volume (V₁)";
        resVal = fromM3Cmb(v1_m3, u).toFixed(4) + " " + u.toUpperCase();
        resAlt = (v1_m3 * 1000).toFixed(2) + " L (" + v1_m3.toFixed(4) + " m³)";
      } else if (target === "p1") {
        if (v1_m3 <= 0 || t2_k <= 0) { alert("V1 and T2 must be positive non-zero values."); return; }
        p1_pa = (p2_pa * v2_m3 * t1_k) / (v1_m3 * t2_k);
        const u = document.getElementById("p2UnitSel").value;
        resLabel = "Initial Absolute Pressure (P₁)";
        resVal = fromPa(p1_pa, u).toFixed(4) + " " + u.toUpperCase();
        resAlt = (p1_pa / 100000).toFixed(3) + " bar (" + (p1_pa / 6894.757).toFixed(2) + " psia)";
      } else if (target === "t1") {
        if (p2_pa <= 0 || v2_m3 <= 0) { alert("P2 and V2 must be positive non-zero values."); return; }
        t1_k = (p1_pa * v1_m3 * t2_k) / (p2_pa * v2_m3);
        const s = document.getElementById("t2UnitSel").value;
        resLabel = "Initial Temperature (T₁)";
        resVal = fromKCmb(t1_k, s).toFixed(2) + " °" + s.toUpperCase();
        resAlt = t1_k.toFixed(2) + " K (" + (t1_k - 273.15).toFixed(2) + " °C)";
      }

      // Calculations
      const R = 8.314462;
      const moles = (p1_pa * v1_m3) / (R * t1_k);
      const massKg = (moles * mw) / 1000;
      const massLb = massKg * 2.20462;

      const volRatio = v2_m3 / v1_m3;
      const presRatio = p2_pa / p1_pa;
      const cmbConstant = (p1_pa * v1_m3) / t1_k; // J/K

      // Equivalent STP and NTP
      // Modern STP: P_stp = 100,000 Pa, T_stp = 273.15 K
      const v_stp_m3 = (cmbConstant * 273.15) / 100000;
      // NIST NTP: P_ntp = 101,325 Pa, T_ntp = 293.15 K
      const v_ntp_m3 = (cmbConstant * 293.15) / 101325;

      const rho1 = massKg / v1_m3;
      const rho2 = massKg / v2_m3;

      document.getElementById("resCmbTargetLabel").textContent = resLabel;
      document.getElementById("resCmbTargetVal").textContent = resVal;
      document.getElementById("resCmbTargetAlt").textContent = resAlt;

      document.getElementById("resCmbVolRatio").textContent = volRatio.toFixed(3) + " : 1";
      document.getElementById("resCmbVolRatioDesc").textContent = volRatio >= 1.0 ? "Net volumetric expansion (" + (((volRatio - 1)) * 100).toFixed(1) + "% increase)" : "Net volumetric compression (" + (((1 - volRatio)) * 100).toFixed(1) + "% reduction)";

      document.getElementById("resCmbPresRatio").textContent = presRatio.toFixed(3) + " : 1";
      document.getElementById("resCmbPresRatioDesc").textContent = presRatio >= 1.0 ? "Pressure increases (" + ((presRatio - 1) * 100).toFixed(1) + "%)" : "Pressure drops (" + ((1 - presRatio) * 100).toFixed(1) + "%)";

      document.getElementById("resCmbMoles").textContent = moles.toFixed(2) + " mol";
      document.getElementById("resCmbMass").textContent = massKg.toFixed(3) + " kg (" + massLb.toFixed(2) + " lbs) of " + gasKey.toUpperCase();

      document.getElementById("resCmbConstant").textContent = (cmbConstant).toFixed(4) + " J/K (P·V/T state invariant = n·R)";
      document.getElementById("resCmbStpVol").textContent = (v_stp_m3 * 1000).toFixed(2) + " L (" + v_stp_m3.toFixed(4) + " m³ at 0°C, 1 bar)";
      document.getElementById("resCmbNtpVol").textContent = (v_ntp_m3 * 1000).toFixed(2) + " L (" + v_ntp_m3.toFixed(4) + " m³ at 20°C, 1 atm)";
      document.getElementById("resCmbDensityShift").textContent = "ρ₁ = " + rho1.toFixed(3) + " kg/m³  ➜  ρ₂ = " + rho2.toFixed(3) + " kg/m³ (" + (((rho2 - rho1) / rho1) * 100).toFixed(1) + "% change)";

      document.getElementById("combinedResults").style.display = "block";
    }
  </script>
</body>
</html>
"""

def generate():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p1 = os.path.join(root, "coagulant-dosing-calculator.html")
    p2 = os.path.join(root, "combined-gas-law-calculator.html")
    
    with open(p1, "w", encoding="utf-8") as f:
        f.write(TOOL_1_HTML.strip() + "\n")
    print(f"Generated {p1}")

    with open(p2, "w", encoding="utf-8") as f:
        f.write(TOOL_2_HTML.strip() + "\n")
    print(f"Generated {p2}")

if __name__ == "__main__":
    generate()
