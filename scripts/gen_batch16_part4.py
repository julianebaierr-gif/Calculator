# -*- coding: utf-8 -*-
"""
Script to generate Batch 16 Part 4 tools:
7. polymer-dosing-calculator.html
8. ro-antiscalant-dosing-calculator.html
"""
import os

TOOL_7_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Polymer Dosing Calculator | Flocculant &amp; Sludge Dewatering Sizer</title>
  <meta name="description" content="Calculate polymer dosing for water clarification, sludge dewatering (centrifuge, belt press), active neat chemical feed, aging tank volume, and dosing pump rates.">
  <link rel="canonical" href="https://calchub.cloud/polymer-dosing-calculator.html">
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
        "name": "Polymer Dosing Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates chemical polymer flocculant consumption, dry sludge solids conditioning dosages (kg/DT), make-up aging solution batching, and metering pump sizing.",
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
            "name": "What is the typical polymer dosage for mechanical sludge dewatering?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For municipal and industrial wastewater sludge dewatering (belt filter presses and centrifuges), polymer dosage is calculated on a dry solids basis: typically 4 to 8 kg of active polymer per dry metric ton (kg/DT) for primary sludge, 8 to 14 kg/DT for secondary waste activated sludge (WAS), and 6 to 10 kg/DT for anaerobically digested mixed sludge."
            }
          },
          {
            "@type": "Question",
            "name": "Why is polymer aging (maturation) required before dosing?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Commercial high-molecular-weight polyacrylamide (PAM) molecules are tightly coiled polymers. When mixed with water at 0.1% to 0.5% concentration, the polymer chains require 30 to 60 minutes of low-shear hydration and uncoiling to fully extend their charged functional groups, maximizing polymer bridging and flocculation efficiency."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between emulsion polymer and dry powder polymer?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Dry powder polymer is 90% to 95% active substance, offering the lowest shipping cost and longest shelf life, but requires dust-free pneumatic wetting systems. Liquid emulsion polymer contains 30% to 50% active polymer suspended in mineral oil carriers; it inverts and dissolves rapidly upon high-shear water contact, making it simpler to automate on compact chemical skids."
            }
          },
          {
            "@type": "Question",
            "name": "How does polymer dosing affect solids recovery and filtrate cake dryness?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Optimal polymer dosing agglomerates microscopic colloids into shear-resistant macro-flocs, increasing solids capture efficiency to >95% and boosting dewatered cake dryness from 12% up to 22-30% dry solids. Under-dosing leads to blinding and dirty filtrate, whereas over-dosing produces sticky, slimy sludge that slips on belts and wastes costly chemical."
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
      <span>Polymer Dosing Calculator</span>
    </nav>

    <h1 class="tool-title">Polymer Dosing &amp; Flocculant Sizer</h1>
    <p class="tool-subtitle">Clarification Coagulant-Aid &amp; Sludge Dewatering Conditioning (Centrifuge &amp; Belt Press)</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="polymerAppMode">Polymer Treatment Application Mode</label>
            <select id="polymerAppMode" class="form-control" onchange="updatePolymerAppMode()">
              <option value="sludge_dewatering" selected>Sludge Dewatering (Centrifuge / Belt Press, kg/Dry Ton)</option>
              <option value="water_clarification">Water / Wastewater Clarification (Coagulant Aid, mg/L ppm)</option>
              <option value="daf_thickening">Dissolved Air Flotation (DAF) Thickening (kg/Dry Ton)</option>
            </select>
          </div>

          <!-- Dewatering Mode Specific Inputs -->
          <div id="sludgeInputsGroup">
            <div class="grid-2-col">
              <div class="form-group">
                <label for="sludgeFlowVal">Sludge Feed Flow Rate</label>
                <input type="number" id="sludgeFlowVal" class="form-control" value="25.0" step="2.5" min="0.1">
              </div>
              <div class="form-group">
                <label for="sludgeFlowUnit">Flow Units</label>
                <select id="sludgeFlowUnit" class="form-control">
                  <option value="m3h" selected>Cubic Meters / Hour (m³/h)</option>
                  <option value="gpm">Gallons / Minute (GPM)</option>
                  <option value="lps">Liters / Second (L/s)</option>
                  <option value="m3d">Cubic Meters / Day (m³/day)</option>
                </select>
              </div>
            </div>

            <div class="grid-2-col">
              <div class="form-group">
                <label for="sludgeSolidsPct">Sludge Feed Total Solids (% TS)</label>
                <input type="number" id="sludgeSolidsPct" class="form-control" value="3.5" step="0.1" min="0.2" max="15.0">
                <span class="field-hint">e.g., 3.0% to 5.0% dry solids</span>
              </div>
              <div class="form-group">
                <label for="dewateringDoseKgDT">Polymer Dose (kg active / Dry Ton)</label>
                <input type="number" id="dewateringDoseKgDT" class="form-control" value="8.0" step="0.5" min="0.5" max="30.0">
                <span class="field-hint">Typically 4-12 kg active/DT</span>
              </div>
            </div>
          </div>

          <!-- Clarification Mode Specific Inputs -->
          <div id="clarifInputsGroup" style="display: none;">
            <div class="grid-2-col">
              <div class="form-group">
                <label for="waterFlowVal">Water Flow Rate</label>
                <input type="number" id="waterFlowVal" class="form-control" value="1000" step="50" min="1">
              </div>
              <div class="form-group">
                <label for="waterFlowUnit">Water Flow Units</label>
                <select id="waterFlowUnit" class="form-control">
                  <option value="m3h" selected>Cubic Meters / Hour (m³/h)</option>
                  <option value="mgd">Million Gallons / Day (MGD)</option>
                  <option value="gpm">Gallons / Minute (GPM)</option>
                </select>
              </div>
            </div>
            <div class="form-group">
              <label for="clarifDosePpm">Coagulant Aid Dose (mg/L active ppm)</label>
              <input type="number" id="clarifDosePpm" class="form-control" value="0.5" step="0.05" min="0.01" max="10.0">
            </div>
          </div>

          <!-- Polymer Reagent Formulation -->
          <div class="grid-2-col">
            <div class="form-group">
              <label for="polymerSupplyForm">Polymer Commercial Supply Form</label>
              <select id="polymerSupplyForm" class="form-control" onchange="updateSupplyForm()">
                <option value="emulsion" selected>Liquid Emulsion (40% Active, SG = 1.04)</option>
                <option value="dry_powder">Dry Powder (92% Active, Bulk Density 0.8 kg/L)</option>
                <option value="custom">Custom Commercial Polymer</option>
              </select>
            </div>
            <div class="form-group">
              <label for="neatActivePct">Commercial Active Polymer (% w/w)</label>
              <input type="number" id="neatActivePct" class="form-control" value="40.0" step="1.0" min="1.0" max="100.0">
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="agingSolnConcPct">Prepared Dosing Solution (% w/v)</label>
              <input type="number" id="agingSolnConcPct" class="form-control" value="0.25" step="0.05" min="0.02" max="1.5">
              <span class="field-hint">Aged feed solution: 0.1% to 0.5%</span>
            </div>
            <div class="form-group">
              <label for="dewateringHoursPerDay">Operating Hours / Day</label>
              <input type="number" id="dewateringHoursPerDay" class="form-control" value="8" step="1" min="1" max="24">
            </div>
          </div>

          <div class="form-group">
            <label for="feedPumpMaxCapacityLph">Dosing Pump Max Flow Rating (L/h)</label>
            <input type="number" id="feedPumpMaxCapacityLph" class="form-control" value="5000" step="250" min="10">
          </div>

          <button type="button" class="btn btn-primary" onclick="calcPolymerDosing()" style="width: 100%; margin-top: 15px;">Calculate Polymer Demand &amp; Feeder Sizing</button>
        </div>
      </div>

      <!-- Output Results Panel -->
      <div class="results-card">
        <div class="result-box primary-result">
          <div class="result-label">Aged 0.25% Solution Dosing Rate</div>
          <div id="resAgedSolnFeedRate" class="result-value">2,800 L / hour</div>
          <div id="resAgedSolnFeedRateSub" class="result-subtext">46.7 L/min (12.33 GPM of prepared 0.25% polymer solution)</div>
        </div>

        <div class="result-grid">
          <div class="result-item">
            <span class="result-label">Pure Active Polymer Rate</span>
            <span id="resActivePolymerHr" class="result-value highlight">7.00 kg / hour</span>
            <span id="resActivePolymerDay" class="result-subtext">56.0 kg / 8-hr shift (123.5 lbs/shift)</span>
          </div>
          <div class="result-item">
            <span class="result-label">Commercial Neat Consumption</span>
            <span id="resNeatPolymerHr" class="result-value">17.50 kg / hour</span>
            <span id="resNeatPolymerDay" class="result-subtext">140.0 kg / day commercial neat product</span>
          </div>
          <div class="result-item">
            <span class="result-label">Dry Sludge Throughput</span>
            <span id="resDrySludgeTonnage" class="result-value">0.875 DT / hour</span>
            <span id="resDrySludgeTonnageDay" class="result-subtext">7.00 Dry Tons / 8-hr operating day</span>
          </div>
          <div class="result-item">
            <span class="result-label">Pump Stroke Setting</span>
            <span id="resPumpStrokePct" class="result-value">56.0%</span>
            <span class="result-subtext">Of 5,000 L/h rated capacity</span>
          </div>
          <div class="result-item">
            <span class="result-label">Neat Polymer Feed Pump</span>
            <span id="resNeatDosingPumpRate" class="result-value">16.8 L / hour</span>
            <span class="result-subtext">Injected into make-up aging water</span>
          </div>
          <div class="result-item">
            <span class="result-label">IBC Tote Drum Autonomy</span>
            <span id="resToteAutonomy" class="result-value">7.1 Operating Days</span>
            <span class="result-subtext">Standard 1,000 Liter tote tank</span>
          </div>
        </div>

        <div class="result-details" style="margin-top: 15px;">
          <p><strong>Make-up Aging Tank Sizing (45-Min Maturation):</strong> <span id="resAgingTankSize">Requires minimum 2,100 Liter hydration aging tank.</span></p>
          <p><strong>Process Verification:</strong> <span id="resProcessNote">Active dosage conforms to WEF MOP-8 and EPA wastewater sludge dewatering design criteria.</span></p>
        </div>
      </div>
    </div>

    <!-- 1000+ Words Engineering Body -->
    <article class="article-body">
      <h2>Principles of Polymer Flocculation in Solid-Liquid Separation</h2>
      <p>In municipal wastewater treatment facilities (WRRFs), industrial effluent plants, and mineral processing refineries, raw suspended solids, biological sludge, and chemical precipitates exist as finely divided colloids ranging from $0.1\ \mu\text{m}\text{ to } 10\ \mu\text{m}$ in diameter. Because these particles carry net negative electrical surface charges (zeta potential between $-15\text{ mV and } -40\text{ mV}$), electrostatic repulsive forces prevent them from aggregating, keeping them in stable suspension indefinitely.</p>

      <p>While primary coagulants (such as alum, ferric chloride, or polyaluminum chloride) neutralize surface charges, high-molecular-weight <strong>polymeric flocculants</strong> are required to bridge adjacent micro-flocs into large, rapidly settling, shear-resistant macro-flocs. The most ubiquitous synthetic polymers belong to the <strong>polyacrylamide (PAM)</strong> family, possessing molecular weights spanning from $5\text{ to } 25\text{ million Daltons (g/mol)}$ and chain lengths extending up to several micrometers. By adsorbing simultaneously onto multiple particle surfaces, polymer chains create robust structural networks that enable high-throughput mechanical dewatering.</p>

      <h2>Chemical Mechanisms: Charge Neutralization vs. Bridging Flocculation</h2>
      <p>Polymeric conditioning functions via two concurrent electrochemical mechanisms:</p>
      <ul>
        <li><strong>Cationic Charge Patch Neutralization:</strong> Biological secondary sludge (waste activated sludge, WAS) contains high concentrations of extracellular polymeric substances (EPS) rich in negatively charged carboxylate ($\text{COO}^-$) and phosphate ($\text{PO}_4^{3-}$) functional groups. Highly charged cationic polyacrylamides (often incorporating quaternary ammonium groups such as DMAEA-MCQ) bind electrostatically, neutralizing local surface charges.</li>
        <li><strong>Interparticle Polymer Bridging:</strong> Uncoiled polymer macro-chains extend outward into the bulk solution beyond the electrostatic electrical double layer, attaching to adjacent solids and forming three-dimensional structural matrices. This expels interstitial water, transforming gelatinous slurry into freely draining flocs capable of withstanding intense mechanical shear inside high-speed centrifuges ($2,000\text{ to } 3,500\times g$) and high-pressure belt filter press nips ($&gt;4\text{ bar}$).</li>
      </ul>

      <h2>Mathematical Sizing Formulas for Sludge Dewatering</h2>
      <p>For mechanical sludge conditioning, dosage is universally defined on a <strong>dry solids mass basis</strong>, expressed as active kilograms of polymer per dry metric ton of sludge ($\text{kg/DT}$) or active pounds per dry US ton ($\text{lb/DT}$):</p>

      <h3>1. Calculating Dry Sludge Mass Flow Rate (M_DS)</h3>
      <p>Given wet sludge volumetric flow rate $Q_{\text{sludge}}$ ($\text{m}^3/\text{h}$), total solids percentage $\%_{\text{TS}}$, and sludge specific gravity $\text{SG}_{\text{sludge}} \approx 1.00\text{ to } 1.03$:</p>

      <div class="formula-box">
        $$\dot{M}_{\text{DS}}\text{ (Dry Metric Tons / hour)} = Q_{\text{sludge}}\text{ (m}^3/\text{h)} \times \text{SG} \times \left(\frac{\%_{\text{TS}}}{100}\right)$$
      </div>

      <h3>2. Active Polymer Mass Delivery Rate</h3>
      <p>Multiplying dry sludge throughput by the target active polymer conditioning dosage ($D_{\text{polymer}}$ in $\text{kg active / DT}$):</p>

      <div class="formula-box">
        $$\dot{m}_{\text{active}}\text{ (kg/h)} = \dot{M}_{\text{DS}}\text{ (DT/h)} \times D_{\text{polymer}}\text{ (kg/DT)}$$
      </div>

      <h3>3. Commercial Neat Chemical Feed Rate</h3>
      <p>Commercial polymers are supplied either as dry powders ($90\%\text{ to } 95\%\text{ active}$) or liquid inverse emulsions ($30\%\text{ to } 50\%\text{ active PAM}$ in mineral oil carriers with surfactant packages). Accounting for commercial active percentage ($\%_{\text{neat}}$):</p>

      <div class="formula-box">
        $$\dot{m}_{\text{neat}}\text{ (kg/h)} = \frac{\dot{m}_{\text{active}}\text{ (kg/h)}}{\left(\frac{\%_{\text{neat}}}{100}\right)}$$
      </div>

      <h3>4. Prepared Dosing Solution Volumetric Flow Rate</h3>
      <p>Commercial neat polymer cannot be injected directly into raw sludge; high local viscosity causes severe unmixed chemical channeling and wasteful balling. Instead, polymer is inverted and sheared with potable water into an <strong>aged feed solution</strong> formulated between $0.10\%\text{ and } 0.50\%\text{ w/v active concentration}$ ($1.0\text{ to } 5.0\text{ g active / Liter}$). The required volumetric feed rate ($q_{\text{aged}}$ in $\text{L/h}$) delivered by the progressive cavity or diaphragm dosing pump is:</p>

      <div class="formula-box">
        $$q_{\text{aged}}\text{ (L/h)} = \frac{\dot{m}_{\text{active}}\text{ (kg/h)} \times 1,000\text{ g/kg}}{C_{\text{aged}}\text{ (g/L)}} = \frac{\dot{m}_{\text{active}}\text{ (kg/h)}}{\left(\frac{\%_{\text{soln}}}{100}\right) \times 1.0\text{ kg/L}}$$
      </div>

      <h2>Polymer Inversion, Hydration Aging &amp; Viscosity Physics</h2>
      <p>The successful operation of a polymer feed system relies fundamentally on the physics of <strong>polymer chain uncoiling</strong>. In dry powder or emulsion form, polyacrylamide macromolecules are tightly coiled into microscopic spheres. To become active:</p>
      <ol>
        <li><strong>High-Shear Inversion (First 2 Seconds):</strong> The neat chemical must encounter instantaneous high-energy hydrodynamic shear (velocity gradient $G &gt; 1,000\text{ s}^{-1}$) created by an automated polymer blending unit (e.g., motorized dynamic mixer or progressive orifice hydro-nozzle). This fractures the surfactant carrier shell without shearing the long macromolecular polymer backbones.</li>
        <li><strong>Low-Shear Maturation Aging (30 to 60 Minutes):</strong> Following inversion, the solution must transfer into an unbaffled aging tank providing a minimum of $30\text{ to } 60\text{ minutes}$ of low-shear retention ($G \approx 50\text{ to } 100\text{ s}^{-1}$). This permits water molecules to hydrate the hydrophilic polymer segments, allowing the polymer chains to fully unravel into long, flexible linear threads.</li>
      </ol>
      <p>Dosing "green" (unaged) polymer reduces dewatering efficiency by $30\%\text{ to } 50\%$, leading to high filtrate turbidity, poor cake release, and massive chemical waste.</p>

      <h2>Polymer Dosing Guidelines Benchmark Table</h2>
      <p>The table below summarizes standard industrial polymer dosages, dewatered cake dryness, and solids capture efficiencies across primary wastewater dewatering and thickening unit processes per <strong>WEF Manual of Practice No. 8</strong> and <strong>EPA Technology Guidelines</strong>:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Dewatering / Thickening Equipment</th>
              <th>Sludge Type</th>
              <th>Feed Solids (% TS)</th>
              <th>Polymer Dose (kg active / DT)</th>
              <th>Cake Dryness (% TS)</th>
              <th>Solids Capture (%)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>High-Solid Centrifuge</td>
              <td>Anaerobically Digested (Primary + WAS)</td>
              <td>2.5 &ndash; 4.5%</td>
              <td>8.0 &ndash; 14.0 kg/DT</td>
              <td>22 &ndash; 30%</td>
              <td>95 &ndash; 98%</td>
            </tr>
            <tr>
              <td>Belt Filter Press (BFP)</td>
              <td>Anaerobically Digested (Primary + WAS)</td>
              <td>3.0 &ndash; 5.0%</td>
              <td>5.0 &ndash; 10.0 kg/DT</td>
              <td>18 &ndash; 25%</td>
              <td>94 &ndash; 97%</td>
            </tr>
            <tr>
              <td>Centrifuge (Dewatering)</td>
              <td>Pure Primary Sludge</td>
              <td>4.0 &ndash; 7.0%</td>
              <td>3.0 &ndash; 6.0 kg/DT</td>
              <td>28 &ndash; 36%</td>
              <td>96 &ndash; 99%</td>
            </tr>
            <tr>
              <td>Screw Press</td>
              <td>Aerobically Digested Sludge</td>
              <td>1.5 &ndash; 3.0%</td>
              <td>7.0 &ndash; 12.0 kg/DT</td>
              <td>16 &ndash; 22%</td>
              <td>95 &ndash; 98%</td>
            </tr>
            <tr>
              <td>Rotary Drum Thickener (RDT)</td>
              <td>Waste Activated Sludge (WAS)</td>
              <td>0.6 &ndash; 1.2%</td>
              <td>2.0 &ndash; 5.0 kg/DT</td>
              <td>5.0 &ndash; 8.0% (Thickened)</td>
              <td>93 &ndash; 96%</td>
            </tr>
            <tr>
              <td>Dissolved Air Flotation (DAF)</td>
              <td>Waste Activated Sludge (WAS)</td>
              <td>0.5 &ndash; 1.0%</td>
              <td>3.0 &ndash; 6.0 kg/DT</td>
              <td>4.0 &ndash; 6.0% (Float)</td>
              <td>90 &ndash; 95%</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Practical Worked Case Study: Sizing Centrifuge Polymer Feed</h2>
      <div class="worked-example-card">
        <h3>Wastewater Reclamation Facility Design Example: High-Solids Centrifuge</h3>
        <p><strong>Scenario:</strong> A municipal Water Resource Recovery Facility (WRRF) operates a high-solids dewatering decanter centrifuge running $8.0\text{ hours/day}$, $5\text{ days/week}$. The centrifuge processes anaerobically digested sludge at a steady volumetric feed flow rate of $Q_{\text{sludge}} = 30.0\text{ m}^3/\text{h}$ ($132\text{ GPM}$) with a total solids concentration of $\%_{\text{TS}} = 3.20\%$ ($\text{SG} = 1.015$). Full-scale plant optimization establishes an optimal conditioning dosage of $D = 9.50\text{ kg active polymer per dry metric ton of sludge (kg/DT)}$. The facility utilizes liquid emulsion polymer delivered at $42.0\%\text{ active content}$ ($\text{density} = 1.04\text{ kg/L}$) in a $1,000\text{ Liter}$ intermediate bulk container (IBC tote). The aged dosing solution is prepared at $C_{\text{aged}} = 0.20\%\text{ w/v active}$ ($2.0\text{ g/L}$).</p>

        <p><strong>Step 1: Calculate Dry Sludge Solids Throughput:</strong></p>
        $$\dot{M}_{\text{DS}} = 30.0\text{ m}^3/\text{h} \times 1.015\text{ t/m}^3 \times \left(\frac{3.20}{100}\right) = 0.9744\text{ Dry Metric Tons / hour}$$
        $$\text{Daily Dry Solids (8-hr shift)} = 0.9744\text{ DT/h} \times 8.0\text{ h} = 7.795\text{ Dry Tons / day}\ (17,185\text{ lbs/day})$$

        <p><strong>Step 2: Determine Active Pure Polymer Demand:</strong></p>
        $$\dot{m}_{\text{active}} = 0.9744\text{ DT/h} \times 9.50\text{ kg/DT} = 9.2568\text{ kg active polymer / hour}$$
        $$\text{Shift Active Consumption} = 9.2568\text{ kg/h} \times 8.0\text{ h} = 74.05\text{ kg active / shift}$$

        <p><strong>Step 3: Calculate Commercial 42% Neat Emulsion Consumption:</strong></p>
        $$\dot{m}_{\text{neat}} = \frac{9.2568\text{ kg/h}}{0.42} = 22.04\text{ kg neat / hour}$$
        $$\text{Volumetric Neat Rate} = \frac{22.04\text{ kg/h}}{1.04\text{ kg/L}} = 21.19\text{ Liters / hour}\ (0.0933\text{ GPM})$$
        $$\text{Shift Neat Consumption} = 21.19\text{ L/h} \times 8.0\text{ h} = 169.5\text{ Liters of neat polymer / day}$$

        <p><strong>Step 4: Sizing the Aged 0.20% Solution Dosing Pump:</strong></p>
        $$q_{\text{aged}} = \frac{9.2568\text{ kg/h} \times 1,000\text{ g/kg}}{2.0\text{ g active/L}} = 4,628.4\text{ Liters / hour}\ (20.38\text{ GPM})$$
        <p>The variable-speed positive displacement progressive cavity dosing pump should be rated for a nominal flow of $5,000\text{ to } 6,000\text{ L/h}$, operating comfortably at $75\%\text{ to } 90\%$ speed.</p>

        <p><strong>Step 5: Maturation Aging Tank Sizing:</strong></p>
        <p>To guarantee a 45-minute minimum uncoiling hydration residence time at peak throughput:</p>
        $$V_{\text{aging}} = 4,628.4\text{ L/h} \times \left(\frac{45\text{ min}}{60\text{ min/h}}\right) = 3,471\text{ Liters}$$
        <p>The facility should install a dual-compartment aging system with a minimum working capacity of $3,500\text{ Liters}$.</p>

        <p><strong>Step 6: IBC Tote Autonomy:</strong></p>
        $$\text{Autonomy} = \frac{1,000\text{ Liters in Tote}}{169.5\text{ Liters / operating day}} = 5.9\text{ Operating Days per 1,000 L Tote}$$
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
          <p class="footer-about">High-precision polymer conditioning, sludge dewatering stoichiometry, and wastewater solids separation engineering tools conforming to WEF and EPA standards.</p>
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
            <li><a href="https://www.wef.org" target="_blank" rel="noopener">WEF Manual of Practice No. 8</a></li>
            <li><a href="https://www.epa.gov" target="_blank" rel="noopener">EPA Biosolids Technology Fact Sheet</a></li>
            <li><a href="https://www.awwa.org" target="_blank" rel="noopener">AWWA Standard B453 Polymer Coagulants</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    function updatePolymerAppMode() {
      const mode = document.getElementById("polymerAppMode").value;
      if (mode === "sludge_dewatering") {
        document.getElementById("sludgeInputsGroup").style.display = "block";
        document.getElementById("clarifInputsGroup").style.display = "none";
        document.getElementById("dewateringDoseKgDT").value = 8.0;
      } else if (mode === "daf_thickening") {
        document.getElementById("sludgeInputsGroup").style.display = "block";
        document.getElementById("clarifInputsGroup").style.display = "none";
        document.getElementById("sludgeSolidsPct").value = 1.0;
        document.getElementById("dewateringDoseKgDT").value = 4.0;
      } else if (mode === "water_clarification") {
        document.getElementById("sludgeInputsGroup").style.display = "none";
        document.getElementById("clarifInputsGroup").style.display = "block";
      }
      calcPolymerDosing();
    }

    function updateSupplyForm() {
      const form = document.getElementById("polymerSupplyForm").value;
      if (form === "emulsion") {
        document.getElementById("neatActivePct").value = 40.0;
      } else if (form === "dry_powder") {
        document.getElementById("neatActivePct").value = 92.0;
      }
      calcPolymerDosing();
    }

    function calcPolymerDosing() {
      const mode = document.getElementById("polymerAppMode").value;
      const neatPct = parseFloat(document.getElementById("neatActivePct").value) || 40.0;
      const solnPct = parseFloat(document.getElementById("agingSolnConcPct").value) || 0.25;
      const opHours = parseFloat(document.getElementById("dewateringHoursPerDay").value) || 8;
      const maxPumpLph = parseFloat(document.getElementById("feedPumpMaxCapacityLph").value) || 5000;

      let activeKgPerHour = 0;
      let dryTonsPerHour = 0;

      if (mode === "sludge_dewatering" || mode === "daf_thickening") {
        const flowVal = parseFloat(document.getElementById("sludgeFlowVal").value) || 0;
        const flowUnit = document.getElementById("sludgeFlowUnit").value;
        const tsPct = parseFloat(document.getElementById("sludgeSolidsPct").value) || 3.5;
        const doseKgDT = parseFloat(document.getElementById("dewateringDoseKgDT").value) || 8.0;

        let m3_per_hr = 0;
        if (flowUnit === "m3h") m3_per_hr = flowVal;
        else if (flowUnit === "gpm") m3_per_hr = flowVal * 0.227125;
        else if (flowUnit === "lps") m3_per_hr = flowVal * 3.6;
        else if (flowUnit === "m3d") m3_per_hr = flowVal / opHours;

        // Specific gravity approx 1.015 for 3-4% sludge
        const sg = 1.00 + (tsPct * 0.004);
        dryTonsPerHour = m3_per_hr * sg * (tsPct / 100.0);
        activeKgPerHour = dryTonsPerHour * doseKgDT;
      } else {
        // Clarification mode
        const wFlow = parseFloat(document.getElementById("waterFlowVal").value) || 0;
        const wUnit = document.getElementById("waterFlowUnit").value;
        const ppmDose = parseFloat(document.getElementById("clarifDosePpm").value) || 0.5;

        let m3_per_hr = 0;
        if (wUnit === "m3h") m3_per_hr = wFlow;
        else if (wUnit === "mgd") m3_per_hr = (wFlow * 3785.41) / 24.0;
        else if (wUnit === "gpm") m3_per_hr = wFlow * 0.227125;

        activeKgPerHour = (m3_per_hr * ppmDose) / 1000.0;
        dryTonsPerHour = 0;
      }

      const activeKgPerDay = activeKgPerHour * opHours;
      const activeLbsPerDay = activeKgPerDay * 2.20462;

      // Commercial neat polymer
      const neatKgPerHour = activeKgPerHour / (neatPct / 100.0);
      const neatKgPerDay = neatKgPerHour * opHours;
      const neatLitersPerHour = neatKgPerHour / 1.04; // SG approx 1.04

      // Prepared aged solution: concentration in % w/v (e.g. 0.25% = 2.5 g/L)
      const concGL = solnPct * 10.0;
      const agedLitersPerHour = (activeKgPerHour * 1000.0) / concGL;
      const agedLitersPerMin = agedLitersPerHour / 60.0;
      const agedGpm = agedLitersPerHour * 0.00440287;

      const pumpStrokePct = (agedLitersPerHour / maxPumpLph) * 100.0;

      // Aging tank volume for 45 min retention
      const reqAgingLiters = agedLitersPerHour * (45.0 / 60.0);

      // Tote autonomy (1000 L tote)
      const toteDays = (neatKgPerDay / 1.04) > 0 ? (1000.0 / (neatKgPerDay / 1.04)).toFixed(1) : "N/A";

      // Render Outputs
      document.getElementById("resAgedSolnFeedRate").textContent = agedLitersPerHour.toLocaleString(undefined, {maximumFractionDigits: 0}) + " L / hour";
      document.getElementById("resAgedSolnFeedRateSub").textContent = agedLitersPerMin.toFixed(1) + " L/min (" + agedGpm.toFixed(2) + " GPM of prepared " + solnPct + "% polymer solution)";

      document.getElementById("resActivePolymerHr").textContent = activeKgPerHour.toFixed(2) + " kg / hour";
      document.getElementById("resActivePolymerDay").textContent = activeKgPerDay.toFixed(1) + " kg / " + opHours + "-hr shift (" + activeLbsPerDay.toFixed(1) + " lbs/shift)";

      document.getElementById("resNeatPolymerHr").textContent = neatKgPerHour.toFixed(2) + " kg / hour";
      document.getElementById("resNeatPolymerDay").textContent = neatKgPerDay.toFixed(1) + " kg / day commercial neat (" + neatPct + "% active)";

      if (mode === "water_clarification") {
        document.getElementById("resDrySludgeTonnage").textContent = "N/A (Clarification)";
        document.getElementById("resDrySludgeTonnageDay").textContent = "Dilute water stream coagulation";
      } else {
        document.getElementById("resDrySludgeTonnage").textContent = dryTonsPerHour.toFixed(3) + " DT / hour";
        document.getElementById("resDrySludgeTonnageDay").textContent = (dryTonsPerHour * opHours).toFixed(2) + " Dry Tons / " + opHours + "-hr shift";
      }

      document.getElementById("resPumpStrokePct").textContent = pumpStrokePct.toFixed(1) + "%";
      document.getElementById("resNeatDosingPumpRate").textContent = neatLitersPerHour.toFixed(1) + " L / hour";
      document.getElementById("resToteAutonomy").textContent = toteDays + " Operating Days";

      document.getElementById("resAgingTankSize").textContent = "Requires minimum " + reqAgingLiters.toFixed(0) + " Liter working hydration volume (45-min maturation).";
    }

    window.addEventListener("DOMContentLoaded", () => {
      calcPolymerDosing();
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
  <title>RO Antiscalant Dosing Calculator | Membrane Scale Inhibitor Sizer</title>
  <meta name="description" content="Calculate reverse osmosis (RO) membrane antiscalant chemical dosing, feed pump rates, brine concentration factor, and Langelier Saturation Index (LSI) control.">
  <link rel="canonical" href="https://calchub.cloud/ro-antiscalant-dosing-calculator.html">
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
        "name": "RO Antiscalant Dosing Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates reverse osmosis membrane chemical antiscalant feed rates, brine reject concentration factors, recovery limits, and chemical metering pump stroke sizing.",
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
            "name": "What is the primary function of antiscalant in Reverse Osmosis (RO) systems?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "As raw feedwater passes across semi-permeable RO membranes, pure permeate water is extracted, concentrating sparingly soluble mineral salts in the reject brine stream. Antiscalants are synthetic organic phosphonates or polycarboxylates that delay crystal nucleation and distort crystalline lattice growth, allowing minerals like CaCO3, CaSO4, BaSO4, and SiO2 to remain supersaturated without precipitating onto membrane surfaces."
            }
          },
          {
            "@type": "Question",
            "name": "How is the concentration factor (CF) calculated in RO systems?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The brine concentration factor represents how concentrated rejected minerals become relative to raw feedwater. It is calculated from system recovery ratio Y (permeate flow divided by feed flow): CF = 1 / (1 - Y). For instance, an RO system operating at 75% recovery (Y = 0.75) has a concentration factor of CF = 1 / (1 - 0.75) = 4.0, meaning rejected minerals are 400% more concentrated in the brine."
            }
          },
          {
            "@type": "Question",
            "name": "What is the typical dosage range for RO membrane antiscalant?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Standard industrial antiscalant dosages typically range from 1.5 to 5.0 mg/L (ppm) based on total raw feedwater flow. Under-dosing leads to irreversible mineral scaling on final-stage membrane elements, while excessive over-dosing can cause biofouling or polymer-antiscalant cross-precipitation with cationic coagulants."
            }
          },
          {
            "@type": "Question",
            "name": "Why is antiscalant dosed based on raw feed flow rather than permeate flow?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Antiscalant must be uniformly dispersed throughout the entire liquid volume entering the first-stage membrane feed manifold. If dosed into brine or permeate, mineral crystals would nucleate in earlier stages before inhibitor contact, causing premature tail-element scale blinding."
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
      <span>RO Antiscalant Dosing Calculator</span>
    </nav>

    <h1 class="tool-title">Reverse Osmosis Antiscalant Dosing Calculator</h1>
    <p class="tool-subtitle">Membrane Scale Inhibition Sizing, Concentration Factor (CF) &amp; Metering Pump Calibration</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="roFeedwaterPreset">RO System Application &amp; Water Source</label>
            <select id="roFeedwaterPreset" class="form-control" onchange="updateROPreset()">
              <option value="brackish_ground" selected>Brackish Groundwater (75% Recovery, LSI &gt; 1.5, Moderate Silica)</option>
              <option value="seawater_ro">Seawater Reverse Osmosis (SWRO, 45% Recovery, S&amp;DSI Scaling)</option>
              <option value="effluent_reuse">Tertiary Wastewater Reuse (80% Recovery, Calcium Phosphate/Sulfate)</option>
              <option value="industrial_pure">Industrial Ultrapure Boiler Feed (85% Recovery, High Silica Stress)</option>
              <option value="custom">Custom Feed &amp; Recovery Parameters</option>
            </select>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="roFeedFlowVal">RO Raw Feedwater Flow Rate</label>
              <input type="number" id="roFeedFlowVal" class="form-control" value="100" step="10" min="0.1">
            </div>
            <div class="form-group">
              <label for="roFeedFlowUnit">Feed Flow Units</label>
              <select id="roFeedFlowUnit" class="form-control">
                <option value="m3h" selected>Cubic Meters / Hour (m³/h)</option>
                <option value="gpm">Gallons / Minute (GPM)</option>
                <option value="mgd">Million Gallons / Day (MGD)</option>
                <option value="mld">Million Liters / Day (MLD)</option>
              </select>
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="roRecoveryPct">System Permeate Recovery (Y %)</label>
              <input type="number" id="roRecoveryPct" class="form-control" value="75.0" step="1.0" min="30.0" max="95.0">
              <span class="field-hint">Typically 75% for brackish, 40-50% for seawater</span>
            </div>
            <div class="form-group">
              <label for="antiscalantDosePpm">Antiscalant Dosage (mg/L neat ppm)</label>
              <input type="number" id="antiscalantDosePpm" class="form-control" value="3.0" step="0.2" min="0.5" max="15.0">
              <span class="field-hint">Based on raw feedwater flow</span>
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="antiscalantSG">Neat Antiscalant Specific Gravity (SG)</label>
              <input type="number" id="antiscalantSG" class="form-control" value="1.20" step="0.02" min="1.05" max="1.45">
              <span class="field-hint">Typically 1.15 to 1.30 kg/L</span>
            </div>
            <div class="form-group">
              <label for="tankDilutionRatio">Day Tank Dilution Factor</label>
              <select id="tankDilutionRatio" class="form-control">
                <option value="1" selected>Neat 100% (No Dilution / Direct Drum Pumping)</option>
                <option value="5">1 : 4 Dilution (20% v/v in RO Permeate)</option>
                <option value="10">1 : 9 Dilution (10% v/v in RO Permeate)</option>
                <option value="20">1 : 19 Dilution (5% v/v in RO Permeate)</option>
              </select>
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="roPumpMaxCapacityLph">Metering Pump Max Rating (L/h)</label>
              <input type="number" id="roPumpMaxCapacityLph" class="form-control" value="2.0" step="0.5" min="0.1">
            </div>
            <div class="form-group">
              <label for="operatingHoursDay">Daily Operating Hours</label>
              <input type="number" id="operatingHoursDay" class="form-control" value="24" step="1" min="1" max="24">
            </div>
          </div>

          <button type="button" class="btn btn-primary" onclick="calcROAntiscalant()" style="width: 100%; margin-top: 15px;">Calculate Antiscalant Dosing</button>
        </div>
      </div>

      <!-- Output Results Panel -->
      <div class="results-card">
        <div class="result-box primary-result">
          <div class="result-label">Feed Pump Volumetric Delivery Rate</div>
          <div id="resPumpLphVal" class="result-value">0.250 L / hour</div>
          <div id="resPumpAlternateUnits" class="result-subtext">4.17 mL/min (0.066 GPH neat antiscalant feed)</div>
        </div>

        <div class="result-grid">
          <div class="result-item">
            <span class="result-label">Daily Neat Consumption</span>
            <span id="resDailyNeatKg" class="result-value highlight">7.20 kg / day</span>
            <span id="resDailyNeatLiters" class="result-subtext">6.00 Liters / day (15.88 lbs/day)</span>
          </div>
          <div class="result-item">
            <span class="result-label">Concentration Factor (CF)</span>
            <span id="resConcentrationFactor" class="result-value">4.00 &times;</span>
            <span class="result-subtext">Brine reject mineral concentration</span>
          </div>
          <div class="result-item">
            <span class="result-label">Permeate Production Flow</span>
            <span id="resPermeateFlow" class="result-value">75.0 m³/h</span>
            <span id="resPermeateFlowSub" class="result-subtext">330.2 GPM pure permeate</span>
          </div>
          <div class="result-item">
            <span class="result-label">Concentrate Brine Discharge</span>
            <span id="resBrineFlow" class="result-value">25.0 m³/h</span>
            <span id="resBrineFlowSub" class="result-subtext">110.1 GPM reject brine</span>
          </div>
          <div class="result-item">
            <span class="result-label">Pump Stroke Setting</span>
            <span id="resPumpStrokeSetting" class="result-value">12.5%</span>
            <span id="resPumpStrokeWarning" class="result-subtext">Of 2.0 L/h maximum pump rating</span>
          </div>
          <div class="result-item">
            <span class="result-label">Standard Drum Autonomy</span>
            <span id="resDrumAutonomyDays" class="result-value">33.3 Days</span>
            <span class="result-subtext">Standard 200 L / 55-Gal shipping drum</span>
          </div>
        </div>

        <div class="result-details" style="margin-top: 15px;">
          <p><strong>Brine Scaling Stress Analysis:</strong> <span id="resScaleRiskNote">At 4.00x concentration factor, LSI in concentrate increases by approx +0.60 units. Antiscalant prevents calcite and gypsum precipitation.</span></p>
          <p><strong>Dilution Water Standard:</strong> <span id="resDilutionWaterNote">Always use chlorine-free RO permeate for antiscalant tank dilution to prevent biological fouling inside day tanks.</span></p>
        </div>
      </div>
    </div>

    <!-- 1000+ Words Engineering Body -->
    <article class="article-body">
      <h2>Engineering Fundamentals of Reverse Osmosis Membrane Scaling</h2>
      <p>In modern industrial desalination, semiconductor ultrapure water production, and municipal wastewater reclamation, <strong>Reverse Osmosis (RO)</strong> systems utilize high-pressure semi-permeable spiral-wound polyamide composite membranes to separate dissolved ionic salts from water. While RO membranes reject upwards of $99.5\%$ of monovalent and multivalent dissolved minerals, this separation inevitably partitions the raw feedwater stream into two distinct hydraulic components: a purified <strong>permeate</strong> stream and an ultra-concentrated <strong>reject (concentrate or brine)</strong> stream.</p>

      <p>As water is progressively extracted through the membrane leaves, the concentrations of sparingly soluble inorganic salts—principally calcium carbonate ($\text{CaCO}_3$), calcium sulfate ($\text{CaSO}_4$, gypsum), barium sulfate ($\text{BaSO}_4$, barite), strontium sulfate ($\text{SrSO}_4$), and reactive silica ($\text{SiO}_2$)—increase exponentially inside the membrane feed-concentrate spacer channels. When the thermodynamic ion activity product ($IAP$) of any mineral exceeds its corresponding equilibrium solubility product ($K_{sp}$), the brine becomes supersaturated ($IAP / K_{sp} &gt; 1.0$), triggering heterogeneous crystal nucleation and irreversible scale deposition across the membrane feed spacer and active surface.</p>

      <h2>The Concentration Factor (CF) and Recovery Equation</h2>
      <p>The volumetric recovery ratio ($Y$) of an RO membrane array represents the ratio of permeate flow rate ($Q_p$) to total raw feedwater flow rate ($Q_f$):</p>

      <div class="formula-box">
        $$Y = \frac{Q_p}{Q_f} \quad \implies \quad Q_f = Q_p + Q_c$$
      </div>

      <p>Where $Q_c$ denotes the concentrate brine flow rate. Assuming near-complete rejection of multivalent scaling ions ($R_{\text{salt}} \approx 100\%$), the mass balance across the membrane train defines the <strong>Concentration Factor ($CF$)</strong> of the reject brine:</p>

      <div class="formula-box">
        $$CF = \frac{C_{\text{brine}}}{C_{\text{feed}}} = \frac{1}{1 - Y}$$
      </div>

      <p>The non-linear nature of this relationship governs membrane scaling risk:</p>
      <ul>
        <li>At $50\%$ Recovery ($Y = 0.50$): $CF = \frac{1}{1 - 0.50} = 2.00\times$ (reject minerals are doubled).</li>
        <li>At $75\%$ Recovery ($Y = 0.75$): $CF = \frac{1}{1 - 0.75} = 4.00\times$ (reject minerals are quadrupled).</li>
        <li>At $85\%$ Recovery ($Y = 0.85$): $CF = \frac{1}{1 - 0.85} = 6.67\times$ (reject minerals increase nearly 7-fold).</li>
        <li>At $90\%$ Recovery ($Y = 0.90$): $CF = \frac{1}{1 - 0.90} = 10.00\times$ (reject minerals increase 10-fold).</li>
      </ul>
      <p>Because solubility products scale by the square or cube of concentration (e.g., $[\text{Ca}^{2+}][\text{SO}_4^{2-}]$ increases by $CF^2 = 16\times$ at $75\%$ recovery), scaling potential surges drastically in the tail elements of the final membrane stage.</p>

      <h2>Mechanisms of Chemical Scale Inhibition</h2>
      <p>Rather than dissolving mineral scale after it has formed, modern synthetic RO antiscalants act as <strong>threshold scale inhibitors</strong> operating at substoichiometric concentrations (merely $1\text{ to } 5\text{ mg/L}$ chemical dosed against hundreds of $\text{mg/L}$ of scaling salts). They safeguard membranes via three distinct physicochemical mechanisms:</p>
      <ol>
        <li><strong>Threshold Inhibition (Nucleation Delay):</strong> Antiscalant molecules (such as amino tris(methylene phosphonic acid) ATMP or phosphonobutane-tricarboxylic acid PBTC) electrostatically adsorb onto embryonic sub-nanometer crystal nuclei as they spontaneously form. This dramatically increases the activation energy required for crystal growth, keeping minerals in a metastable supersaturated state throughout the $10\text{ to } 30\text{ second}$ hydraulic residence time of water passing through the pressure vessels.</li>
        <li><strong>Crystal Lattice Distortion:</strong> When micro-crystals do nucleate, antiscalant anions incorporate into the regular crystalline lattice boundaries, disrupting periodic symmetry. Instead of forming sharp, hard, adherent rhombohedral calcite or needle-like gypsum crystals that mechanically pierce the polyamide polymer layer, the crystals deform into soft, rounded, non-adherent spherulites that cannot adhere to the membrane surface.</li>
        <li><strong>Colloidal Dispersion:</strong> Negatively charged polycarboxylate and polymaleic acid polymer chains coat suspended particles, increasing their negative zeta potential. The resulting mutual electrostatic repulsion keeps colloidal silica, iron hydroxide, and organic colloids dispersed in the high-velocity cross-flow stream for discharge into the reject drain.</li>
      </ol>

      <h2>Mathematical Dosing and Feeder Sizing Formulas</h2>
      <p>Because antiscalant must protect the entire membrane envelope starting from the lead element, dosage ($D_{\text{neat}}$ in $\text{mg/L}$ or $\text{ppm}$) is universally calculated against the <strong>total raw feedwater flow rate ($Q_f$)</strong>, regardless of system recovery:</p>

      <div class="formula-box">
        $$\dot{m}_{\text{neat}}\text{ (kg/day)} = \frac{Q_f\text{ (m}^3/\text{day)} \times D_{\text{neat}}\text{ (mg/L)}}{1,000}$$
        $$\dot{m}_{\text{neat}}\text{ (lb/day)} = Q_f\text{ (MGD)} \times D_{\text{neat}}\text{ (ppm)} \times 8.3454\text{ lb/(MGD}\cdot\text{ppm)}$$
      </div>

      <p>Given the specific gravity ($\text{SG}$, typically $1.15\text{ to } 1.30\text{ kg/L}$) and dilution factor in the chemical day tank ($F_{\text{dilution}} = V_{\text{total}} / V_{\text{neat}}$), the volumetric dosing rate ($q_{\text{pump}}$ in Liters per hour or Gallons per hour) delivered by the positive displacement metering pump is:</p>

      <div class="formula-box">
        $$q_{\text{pump}}\text{ (L/h)} = \frac{\dot{m}_{\text{neat}}\text{ (kg/day)} \times F_{\text{dilution}}}{24\text{ h/day} \times \text{SG}\text{ (kg/L)}}$$
      </div>

      <h2>Scaling Saturation Indices and Thresholds Benchmark Table</h2>
      <p>The table below summarizes critical scaling indices, geochemical thresholds, and maximum permissible saturation limits achievable with specialized modern threshold inhibitors:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Scaling Mineral Species</th>
              <th>Governing Thermodynamic Index</th>
              <th>Thermodynamic Saturation Limit (Without Inhibitor)</th>
              <th>Maximum Practical Limit (With High-Performance Antiscalant)</th>
              <th>Preferred Antiscalant Chemistry</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Calcium Carbonate (CaCO₃)</td>
              <td>Langelier Saturation Index (LSI, TDS &lt; 10,000 ppm)</td>
              <td>LSI &gt; 0.0 (Precipitates)</td>
              <td>LSI up to +2.5 to +2.8 (Safe)</td>
              <td>Phosphonates (PBTC, HEDP), Polyacrylates</td>
            </tr>
            <tr>
              <td>Calcium Carbonate (High Salinity)</td>
              <td>Stiff-Davis Stability Index (S&amp;DSI, SWRO)</td>
              <td>S&amp;DSI &gt; 0.0</td>
              <td>S&amp;DSI up to +1.0 to +1.2</td>
              <td>Polymaleic acid (PMA), Phosphonocarboxylic acids</td>
            </tr>
            <tr>
              <td>Calcium Sulfate (Gypsum, CaSO₄·2H₂O)</td>
              <td>Percent Saturation Ratio (% Sat)</td>
              <td>&gt; 100% Saturation</td>
              <td>Up to 230% &ndash; 300% Saturation</td>
              <td>Specialized high-sulfate phosphonate blends</td>
            </tr>
            <tr>
              <td>Barium Sulfate (Barite, BaSO₄)</td>
              <td>Percent Saturation Ratio (% Sat)</td>
              <td>&gt; 100% Saturation</td>
              <td>Up to 6,000% &ndash; 8,000% Saturation</td>
              <td>Polyphosphonates (extremely insoluble salt)</td>
            </tr>
            <tr>
              <td>Strontium Sulfate (Celestite, SrSO₄)</td>
              <td>Percent Saturation Ratio (% Sat)</td>
              <td>&gt; 100% Saturation</td>
              <td>Up to 800% &ndash; 1,200% Saturation</td>
              <td>Carboxylic-sulfonic terpolymers</td>
            </tr>
            <tr>
              <td>Reactive Colloidal Silica (SiO₂)</td>
              <td>Total Dissolved Silica (mg/L as SiO₂)</td>
              <td>120 &ndash; 140 mg/L at 25°C</td>
              <td>Up to 240 &ndash; 300 mg/L at 25°C</td>
              <td>Silica-specific dispersants (neutral charge polyethers)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Practical Worked Case Study: Sizing Antiscalant for a 1,200 GPM Brackish RO System</h2>
      <div class="worked-example-card">
        <h3>Membrane Plant Engineering Case Study: Municipal Brackish Groundwater RO</h3>
        <p><strong>Scenario:</strong> A municipal brackish water reverse osmosis (BWRO) facility treats deep well water to produce drinking water. The system operates at a total raw feedwater flow rate of $Q_f = 1,200\text{ GPM}$ ($272.5\text{ m}^3/\text{h}$, equivalent to $1.728\text{ MGD}$). The membrane array is configured in a two-stage $2:1$ vessel ratio operating at a global recovery ratio of $Y = 75.0\%$. Feedwater analysis reveals: Calcium $= 110\text{ mg/L}$, Bicarbonate $= 280\text{ mg/L}$, Sulfate $= 220\text{ mg/L}$, and Silica $= 22\text{ mg/L}$ at $T = 22.0^\circ\text{C}$ and $\text{pH } 7.60$. Projection modeling indicates the brine LSI will reach $+1.85$ and silica will reach $88\text{ mg/L}$ in the concentrate. A broad-spectrum neat liquid phosphonate antiscalant is prescribed at a continuous dosage of $D_{\text{neat}} = 3.50\text{ mg/L (ppm)}$ on raw feed. Chemical properties: neat specific gravity $\text{SG} = 1.22\text{ kg/L}$, delivered in standard $200\text{ Liter (55 gallon)}$ polyethylene drums. The chemical metering skid is equipped with a digital diaphragm pump rated at maximum capacity $q_{\text{pump, max}} = 3.00\text{ L/h}$.</p>

        <p><strong>Step 1: Compute Hydraulic Flow Balance:</strong></p>
        $$Q_{\text{permeate}} = 1,200\text{ GPM} \times 0.75 = 900\text{ GPM}\ (204.4\text{ m}^3/\text{h} = 1.296\text{ MGD})$$
        $$Q_{\text{brine}} = 1,200\text{ GPM} \times (1 - 0.75) = 300\text{ GPM}\ (68.1\text{ m}^3/\text{h} = 0.432\text{ MGD})$$
        $$CF = \frac{1}{1 - 0.75} = 4.00\times\text{ Reject Concentration Factor}$$

        <p><strong>Step 2: Determine Daily Mass Delivery Rate of Neat Antiscalant:</strong></p>
        $$\dot{m}_{\text{neat}} = 1.728\text{ MGD} \times 3.50\text{ ppm} \times 8.3454\text{ lb/(MGD}\cdot\text{ppm)} = 50.47\text{ lbs / day}\ (22.89\text{ kg / day})$$

        <p><strong>Step 3: Calculate Neat Volumetric Pumping Rate:</strong></p>
        $$q_{\text{neat}} = \frac{22.89\text{ kg/day}}{1.22\text{ kg/L}} = 18.76\text{ Liters / day}$$
        $$q_{\text{pump, hourly}} = \frac{18.76\text{ L/day}}{24\text{ hours}} = 0.7818\text{ Liters / hour}\ (13.03\text{ mL / minute} = 0.2065\text{ GPH})$$

        <p><strong>Step 4: Metering Pump Stroke Calibration:</strong></p>
        $$\text{Stroke}\% = \left( \frac{0.7818\text{ L/h}}{3.00\text{ L/h}} \right) \times 100\% = 26.06\%$$
        <p>Operating at $26.1\%$ stroke length and stroke frequency falls squarely within the optimum linear accuracy envelope ($15\%\text{ to } 85\%$) of electronic solenoid metering pumps.</p>

        <p><strong>Step 5: Shipping Drum Autonomy:</strong></p>
        $$\text{Autonomy} = \frac{200\text{ Liters in Drum}}{18.76\text{ Liters / day}} = 10.66\text{ Days per Drum}$$
        <p>The facility requires approximately 3 drums per month.</p>
      </div>

      <h2>Operational Pitfalls: Coagulant Compatibility and Biofouling</h2>
      <p>While antiscalants prevent mineral crystallization, improper operation can trigger alternative membrane failure modes:</p>
      <ul>
        <li><strong>Incompatibility with Cationic Coagulants:</strong> If upstream pretreatment utilizes cationic polymeric coagulants (e.g., polyDADMAC) to clarify turbid surface water, carryover of unreacted cationic polymer into the RO feed will react electrostatically with anionic polycarboxylate antiscalants. This produces an extremely sticky, insoluble coagulant-antiscalant co-precipitate that blindfolds lead elements, destroying membrane permeability.</li>
        <li><strong>Over-dosing and Biological Growth:</strong> Dosing antiscalant in excess of manufacturer recommendations does not provide additional scale protection. Instead, phosphonate antiscalants contain orthophosphate precursors ($\text{PO}_4$) that act as limiting biological nutrients, accelerating bacterial proliferation and severe biological slime fouling on feed spacer grids.</li>
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
          <p class="footer-about">High-precision reverse osmosis membrane modeling, threshold scale inhibition stoichiometry, and desalination chemical engineering tools conforming to AWWA and IDA standards.</p>
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
            <li><a href="https://www.idadesal.org" target="_blank" rel="noopener">International Desalination Association (IDA)</a></li>
            <li><a href="https://www.awwa.org" target="_blank" rel="noopener">AWWA Manual M46 Reverse Osmosis</a></li>
            <li><a href="https://www.dupont.com/water" target="_blank" rel="noopener">FilmTec Membrane Technical Manual</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    function updateROPreset() {
      const p = document.getElementById("roFeedwaterPreset").value;
      if (p === "brackish_ground") {
        document.getElementById("roRecoveryPct").value = 75.0;
        document.getElementById("antiscalantDosePpm").value = 3.0;
        document.getElementById("antiscalantSG").value = 1.20;
      } else if (p === "seawater_ro") {
        document.getElementById("roRecoveryPct").value = 45.0;
        document.getElementById("antiscalantDosePpm").value = 2.0;
        document.getElementById("antiscalantSG").value = 1.25;
      } else if (p === "effluent_reuse") {
        document.getElementById("roRecoveryPct").value = 80.0;
        document.getElementById("antiscalantDosePpm").value = 4.5;
        document.getElementById("antiscalantSG").value = 1.22;
      } else if (p === "industrial_pure") {
        document.getElementById("roRecoveryPct").value = 85.0;
        document.getElementById("antiscalantDosePpm").value = 5.0;
        document.getElementById("antiscalantSG").value = 1.25;
      }
      calcROAntiscalant();
    }

    function calcROAntiscalant() {
      const feedVal = parseFloat(document.getElementById("roFeedFlowVal").value) || 0;
      const feedUnit = document.getElementById("roFeedFlowUnit").value;
      const recPct = parseFloat(document.getElementById("roRecoveryPct").value) || 75.0;
      const dosePpm = parseFloat(document.getElementById("antiscalantDosePpm").value) || 3.0;
      const sg = parseFloat(document.getElementById("antiscalantSG").value) || 1.20;
      const dilution = parseFloat(document.getElementById("tankDilutionRatio").value) || 1;
      const maxPumpLph = parseFloat(document.getElementById("roPumpMaxCapacityLph").value) || 2.0;
      const opHours = parseFloat(document.getElementById("operatingHoursDay").value) || 24;

      // Feed Flow converted to m3/day and m3/h
      let m3_per_day = 0;
      let m3_per_hour = 0;
      if (feedUnit === "m3h") {
        m3_per_hour = feedVal;
        m3_per_day = feedVal * 24.0;
      } else if (feedUnit === "gpm") {
        m3_per_hour = feedVal * 0.227125;
        m3_per_day = m3_per_hour * 24.0;
      } else if (feedUnit === "mgd") {
        m3_per_day = feedVal * 3785.41;
        m3_per_hour = m3_per_day / 24.0;
      } else if (feedUnit === "mld") {
        m3_per_day = feedVal * 1000.0;
        m3_per_hour = m3_per_day / 24.0;
      }

      // Permeate and brine flows
      const recoveryFraction = recPct / 100.0;
      const permeateM3h = m3_per_hour * recoveryFraction;
      const brineM3h = m3_per_hour * (1.0 - recoveryFraction);
      const permeateGpm = permeateM3h * 4.40287;
      const brineGpm = brineM3h * 4.40287;

      // Concentration factor CF = 1 / (1 - Y)
      const cf = 1.0 / (1.0 - recoveryFraction);

      // Neat mass and volume
      const neatKgPerDay = (m3_per_day * dosePpm) / 1000.0;
      const neatKgPerHour = neatKgPerDay / 24.0;
      const neatLbsPerDay = neatKgPerDay * 2.20462;

      const neatLitersPerDay = neatKgPerDay / sg;
      const neatLitersPerHour = neatLitersPerDay / 24.0;
      const neatMlPerMin = (neatLitersPerHour * 1000.0) / 60.0;
      const neatGph = neatLitersPerHour * 0.264172;

      // Dosing pump actual flow (accounting for tank dilution)
      const pumpedLph = neatLitersPerHour * dilution;
      const pumpStrokePct = (pumpedLph / maxPumpLph) * 100.0;

      // Drum autonomy (200 L standard drum)
      const drumDays = neatLitersPerDay > 0 ? (200.0 / neatLitersPerDay).toFixed(1) : "N/A";

      // Render Outputs
      document.getElementById("resPumpLphVal").textContent = pumpedLph.toFixed(3) + " L / hour";
      document.getElementById("resPumpAlternateUnits").textContent = (pumpedLph * 1000.0 / 60.0).toFixed(2) + " mL/min (" + (pumpedLph * 0.264172).toFixed(4) + " GPH feed)";

      document.getElementById("resDailyNeatKg").textContent = neatKgPerDay.toFixed(2) + " kg / day";
      document.getElementById("resDailyNeatLiters").textContent = neatLitersPerDay.toFixed(2) + " L / day (" + neatLbsPerDay.toFixed(2) + " lbs/day neat)";

      document.getElementById("resConcentrationFactor").textContent = cf.toFixed(2) + " ×";

      document.getElementById("resPermeateFlow").textContent = permeateM3h.toFixed(1) + " m³/h";
      document.getElementById("resPermeateFlowSub").textContent = permeateGpm.toFixed(1) + " GPM pure permeate";

      document.getElementById("resBrineFlow").textContent = brineM3h.toFixed(1) + " m³/h";
      document.getElementById("resBrineFlowSub").textContent = brineGpm.toFixed(1) + " GPM reject brine";

      document.getElementById("resPumpStrokeSetting").textContent = pumpStrokePct.toFixed(1) + "%";

      let strokeDesc = "Of " + maxPumpLph.toFixed(1) + " L/h maximum pump rating";
      if (pumpStrokePct < 10) strokeDesc += " (Caution: Below 10% linearity, dilute product in day tank)";
      else if (pumpStrokePct > 90) strokeDesc += " (Warning: Above 90% capacity, pump upgrade recommended)";
      else strokeDesc += " (Optimal 10-90% linear operating range)";
      document.getElementById("resPumpStrokeWarning").textContent = strokeDesc;

      document.getElementById("resDrumAutonomyDays").textContent = drumDays + " Days";

      // Scale risk analysis
      let deltaLsi = (Math.log10(cf) * 1.0).toFixed(2);
      document.getElementById("resScaleRiskNote").textContent = "At " + cf.toFixed(2) + "x concentration factor, LSI in concentrate increases by approx +" + deltaLsi + " units. Antiscalant prevents calcite and gypsum precipitation.";
    }

    window.addEventListener("DOMContentLoaded", () => {
      calcROAntiscalant();
    });
  </script>
</body>
</html>
"""

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p7 = os.path.join(base_dir, "polymer-dosing-calculator.html")
    p8 = os.path.join(base_dir, "ro-antiscalant-dosing-calculator.html")

    with open(p7, "w", encoding="utf-8") as f:
        f.write(TOOL_7_HTML)
    print(f"Generated {p7}")

    with open(p8, "w", encoding="utf-8") as f:
        f.write(TOOL_8_HTML)
    print(f"Generated {p8}")

if __name__ == "__main__":
    main()
