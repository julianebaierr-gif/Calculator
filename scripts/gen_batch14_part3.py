# -*- coding: utf-8 -*-
"""
Script to generate Batch 14 Part 3 tools:
5. calcium-hypochlorite-dosing-calculator.html
6. caustic-soda-dosing-calculator.html
"""
import os

TOOL_5_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Calcium Hypochlorite Dosing Calculator | HTH Granular &amp; Tablet Sizer</title>
  <meta name="description" content="Calculate calcium hypochlorite (HTH 65-70%) chemical mass, tablet counts, batch slug and shock chlorination dosages per AWWA C651, C652, and EPA standards.">
  <link rel="canonical" href="https://calchub.cloud/calcium-hypochlorite-dosing-calculator.html">
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
        "name": "Calcium Hypochlorite Dosing Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates dry calcium hypochlorite granular and tablet quantities for continuous water disinfection, pipeline shock chlorination, and storage tank sanitization per AWWA guidelines.",
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
            "name": "What percentage of available chlorine is contained in commercial calcium hypochlorite?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Commercial high-test hypochlorite (HTH) granular or tablet products typically contain between 65% and 70% available chlorine by weight (nominally 68%). Standard calcium hypochlorite has the chemical formula Ca(OCl)2 with a molecular weight of 142.98 g/mol."
            }
          },
          {
            "@type": "Question",
            "name": "How is calcium hypochlorite mass calculated for a water volume and target dosage?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The required dry chemical mass is determined by dividing the pure chlorine demand by the available chlorine fraction: Mass (lbs) = [Volume (Million Gallons) * Target Dose (mg/L) * 8.34 lb/gal] / (% Available Chlorine / 100). In metric units: Mass (kg) = [Volume (m3) * Target Dose (g/m3)] / [1,000 * (% Available Chlorine / 100)]."
            }
          },
          {
            "@type": "Question",
            "name": "What are the standard AWWA C651 disinfection dosage options for new water mains?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "AWWA C651 recognizes three methods: 1) Continuous Feed Method: 25 mg/L free chlorine maintained for 24 hours with minimum 10 mg/L residual remaining. 2) Slug Method: 100 mg/L free chlorine moved slowly through the pipe with minimum 3-hour contact time. 3) Tablet/Granular Method: Granules or 5g tablets pre-placed in pipe joints during construction, filled to yield >= 25 mg/L after 24 hours."
            }
          },
          {
            "@type": "Question",
            "name": "How does water pH affect the biocidal efficacy of hypochlorite solutions?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "When calcium hypochlorite dissolves, it forms hypochlorous acid (HOCl) and hypochlorite ions (OCl-). HOCl is 80 to 100 times more potent as a disinfectant than OCl-. At pH 6.5, roughly 90% exists as HOCl; at pH 7.5, it is 50% HOCl; and at pH 8.5, only 10% remains as HOCl, requiring higher contact times (CT) to achieve equivalent pathogen inactivation."
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
      <span>Calcium Hypochlorite Dosing Calculator</span>
    </nav>

    <h1 class="tool-title">Calcium Hypochlorite (HTH) Dosing Calculator</h1>
    <p class="tool-subtitle">Dry Granular &amp; Tablet Sizing, AWWA C651 Pipeline Shock &amp; Storage Tank Disinfection</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="appMode">Disinfection Application Type</label>
            <select id="appMode" class="form-control" onchange="updateDosePreset()">
              <option value="water_main_cont" selected>AWWA C651 Water Main Continuous Feed (25 mg/L, 24-hr hold)</option>
              <option value="water_main_slug">AWWA C651 Water Main Slug Method (100 mg/L, 3-hr contact)</option>
              <option value="tank_spray">AWWA C652 Water Storage Tank Spray Method (200 mg/L)</option>
              <option value="tank_fill">AWWA C652 Storage Tank Full Fill Method (10 mg/L, 24-hr)</option>
              <option value="well_shock">Emergency Well Casing Shock Chlorination (50&ndash;200 mg/L)</option>
              <option value="potable_cont">Continuous Potable Water Supply Chlorination (1.5&ndash;3.0 mg/L)</option>
              <option value="custom">Custom Target Free Chlorine Dose</option>
            </select>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="calcMode">Volume Basis</label>
              <select id="calcMode" class="form-control" onchange="toggleVolInputs()">
                <option value="direct_gal" selected>Direct Water Volume (Gallons)</option>
                <option value="direct_m3">Direct Water Volume (Cubic Meters / Liters)</option>
                <option value="pipe_dims">Pipeline Dimensions (Diameter &amp; Length)</option>
                <option value="flow_mgd">Continuous Flow Stream (MGD / GPM)</option>
              </select>
            </div>
            <div class="form-group">
              <label for="hthPurity">Commercial HTH Available Chlorine (%)</label>
              <select id="hthPurity" class="form-control">
                <option value="65">65% Available Chlorine (Standard Granular)</option>
                <option value="68" selected>68% Available Chlorine (Commercial Premium HTH)</option>
                <option value="70">70% Available Chlorine (High-Grade Briquettes/Tablets)</option>
                <option value="60">60% Available Chlorine (Commercial Blend)</option>
              </select>
            </div>
          </div>

          <!-- Direct Volume Inputs -->
          <div id="directGalGroup" class="form-group">
            <label for="volGallons">Total Water Volume to Disinfect (Gallons)</label>
            <input type="number" id="volGallons" class="form-control" value="50000" step="1000" min="1">
          </div>

          <div id="directM3Group" class="form-group" style="display:none;">
            <label for="volM3">Total Water Volume to Disinfect (m³)</label>
            <input type="number" id="volM3" class="form-control" value="190" step="5" min="0.1">
          </div>

          <!-- Pipeline Inputs -->
          <div id="pipeGroup" class="grid-2-col" style="display:none;">
            <div class="form-group">
              <label for="pipeDia">Internal Pipe Diameter (Inches)</label>
              <input type="number" id="pipeDia" class="form-control" value="12" step="1" min="1">
            </div>
            <div class="form-group">
              <label for="pipeLen">Total Pipeline Length (Feet)</label>
              <input type="number" id="pipeLen" class="form-control" value="2000" step="50" min="1">
            </div>
          </div>

          <!-- Flow Inputs -->
          <div id="flowGroup" class="grid-2-col" style="display:none;">
            <div class="form-group">
              <label for="contFlowVal">Continuous Water Flow Rate</label>
              <input type="number" id="contFlowVal" class="form-control" value="1.0" step="0.1" min="0.01">
            </div>
            <div class="form-group">
              <label for="contFlowUnit">Flow Rate Units</label>
              <select id="contFlowUnit" class="form-control">
                <option value="mgd" selected>MGD (Million Gallons / Day)</option>
                <option value="gpm">GPM (Gallons / Minute)</option>
                <option value="m3h">m³/hour</option>
              </select>
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="targetPpm">Target Free Available Chlorine (mg/L or ppm)</label>
              <input type="number" id="targetPpm" class="form-control" value="25.0" step="0.5" min="0.1">
            </div>
            <div class="form-group">
              <label for="waterPh">Estimated Water pH</label>
              <input type="number" id="waterPh" class="form-control" value="7.4" step="0.1" min="4.0" max="11.0">
              <span class="field-hint">Governs HOCl vs OCl⁻ biocidal speciation</span>
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="tabletWeight">Tablet Size Option (grams per tablet)</label>
              <select id="tabletWeight" class="form-control">
                <option value="5" selected>5 gram Tablets (Standard AWWA C651 pre-placement)</option>
                <option value="20">20 gram Briquettes / Tablets</option>
                <option value="200">200 gram (7 oz) Slow-Dissolve Puck / Stick</option>
              </select>
            </div>
            <div class="form-group">
              <label for="hthCostPerLb">Granular HTH Price ($ / lb)</label>
              <input type="number" id="hthCostPerLb" class="form-control" value="3.25" step="0.10" min="0">
            </div>
          </div>

          <button type="button" class="btn btn-primary" onclick="calcCalciumHypo()">Calculate Hypochlorite Chemical Quantities</button>
        </div>

        <div id="hypoResults" class="results-box" style="display:none;margin-top:1.5rem;">
          <h3 class="results-title">Calcium Hypochlorite Dosage Breakdown</h3>
          <div class="result-grid">
            <div class="result-card">
              <div class="result-label">Pure Chlorine Equivalent Demand</div>
              <div class="result-value" id="resPureCl2">--</div>
              <div class="result-subtext" id="resPureCl2Alt">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Required Dry HTH Mass</div>
              <div class="result-value highlight" id="resDryHth">--</div>
              <div class="result-subtext" id="resDryHthAlt">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Tablet Equivalent Count</div>
              <div class="result-value highlight" id="resTabletCount">--</div>
              <div class="result-subtext" id="resTabletDesc">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Active HOCl Fraction</div>
              <div class="result-value" id="resHoclFrac">--</div>
              <div class="result-subtext" id="resHoclDesc">Potent biocidal speciation</div>
            </div>
          </div>

          <div class="result-details" style="margin-top:1rem;padding:1rem;background:var(--card-bg);border-radius:6px;border:1px solid var(--border-light);">
            <h4 style="margin-top:0;">Volume &amp; Disinfection Analytics</h4>
            <ul style="margin-bottom:0;line-height:1.7;">
              <li><strong>Total Water Volume:</strong> <span id="resTotalVol">--</span></li>
              <li><strong>Standard Packaging Requirement:</strong> <span id="resPackaging">--</span></li>
              <li><strong>Estimated Chemical Cost:</strong> <span id="resTotalCost" style="font-weight:700;color:var(--primary);">--</span></li>
              <li><strong>EPA CT Inactivation Metric:</strong> <span id="resCtMetric">--</span></li>
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
            <li><a href="alum-dosing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Alum Dosing Calculator</a></li>
            <li><a href="pipe-sizing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Pipe Sizing &amp; Water Flow</a></li>
          </ul>
          <div style="margin-top:1.25rem;padding-top:1rem;border-top:1px solid var(--border-light);">
            <a href="chemical.html" class="sidebar-category-link">View All Chemical Calculators &rarr;</a>
          </div>
        </div>
      </aside>
    </div>

    <!-- Technical Educational Article Body (1000+ Words) -->
    <article class="article-body">
      <h2>Physical Chemistry and Industrial Specifications of Calcium Hypochlorite</h2>
      <p>Calcium hypochlorite—commercially recognized in municipal water engineering as <strong>high-test hypochlorite (HTH)</strong>—is a dry, white crystalline solid with the chemical formula $\text{Ca(OCl)}_2$ and a formula weight of $142.98\text{ g/mol}$. Unlike liquid sodium hypochlorite ($\text{NaOCl}$, commercial bleach), which decomposes rapidly under warm ambient temperatures (losing up to 50% of its active chlorine strength within 60 to 90 days), solid calcium hypochlorite remains exceptionally stable in moisture-tight containers, retaining roughly 65% to 70% available chlorine content over multi-year storage periods.</p>

      <p>Because of its dense chlorine potency ($1.0\text{ lb}$ of $68\%\text{ HTH}$ provides equivalent oxidizing power to $0.68\text{ lb}$ of compressed liquefied elemental chlorine gas $\text{Cl}_2$ or roughly $5.5\text{ lbs}$ of standard $12.5\%\text{ NaOCl}$ liquid), calcium hypochlorite serves as the universal standard chemical for remote wellhead disinfection, emergency disaster relief sanitization, municipal water storage reservoir rehabilitation, and AWWA C651 disinfection of newly constructed water distribution mains.</p>

      <h2>Aqueous Dissociation Chemistry and pH-Dependent Speciation</h2>
      <p>When dry calcium hypochlorite granules or compressed briquettes dissolve in aqueous solution, complete dissociation occurs:</p>

      <div class="formula-box">
        $$\text{Ca(OCl)}_2\text{ (s)} + 2\text{H}_2\text{O} \longrightarrow \text{Ca}^{2+} + 2\text{HOCl} + 2\text{OH}^-$$
      </div>

      <p>The resulting hypochlorous acid ($\text{HOCl}$) establishes an immediate thermodynamic proton exchange equilibrium with the hypochlorite anion ($\text{OCl}^-$):</p>

      <div class="formula-box">
        $$\text{HOCl} \rightleftharpoons \text{H}^+ + \text{OCl}^- \quad (pK_a = 7.54 \text{ at } 25^\circ\text{C})$$
      </div>

      <p>This equilibrium is critical for disinfection efficacy because uncharged hypochlorous acid ($\text{HOCl}$) penetrates neutral bacterial cell membranes and viral capsids approximately <strong>80 to 100 times faster</strong> than the negatively charged hypochlorite ion ($\text{OCl}^-$), which suffers electrostatic repulsion by the negatively charged bacterial peptidoglycan wall. The fractional distribution of active $\text{HOCl}$ is governed rigorously by aqueous pH:</p>

      <div class="formula-box">
        $$\alpha_{\text{HOCl}} = \frac{[\text{HOCl}]}{[\text{HOCl}] + [\text{OCl}^-]} = \frac{1}{1 + 10^{\text{pH} - pK_a}} = \frac{1}{1 + 10^{\text{pH} - 7.54}}$$
      </div>

      <p>At $\text{pH } 6.5$, over $91\%$ of free available chlorine exists in the potent $\text{HOCl}$ state. At neutral $\text{pH } 7.54$, the solution is evenly split ($50\% \text{ HOCl} : 50\% \text{ OCl}^-$). By $\text{pH } 8.5$, only $9.9\%$ remains as $\text{HOCl}$, requiring significantly elevated disinfectant contact times ($CT$) to achieve regulatory compliance under the EPA Surface Water Treatment Rule.</p>

      <h2>Mathematical Formulas for Hypochlorite Dosage and Mass Sizing</h2>
      <p>The standard dosage equation relates volumetric water demand ($V$), target free chlorine concentration ($C_{\text{FAC}}$, in mg/L or ppm), and commercial chemical purity ($P_{\text{HTH}}$, expressed as a decimal fraction):</p>

      <p>In US Customary units for a batch volume of water:</p>
      <div class="formula-box">
        $$W_{\text{pure Cl}_2} \, (\text{lb}) = \frac{V \, (\text{gallons})}{1,000,000} \times C_{\text{FAC}} \, (\text{mg/L}) \times 8.34 \, \left(\frac{\text{lb/Mgal}}{\text{mg/L}}\right)$$
        $$W_{\text{HTH}} \, (\text{lb}) = \frac{W_{\text{pure Cl}_2}}{P_{\text{HTH}}}$$
      </div>

      <p>In metric SI units:</p>
      <div class="formula-box">
        $$W_{\text{HTH}} \, (\text{kg}) = \frac{V \, (\text{m}^3) \times C_{\text{FAC}} \, (\text{g/m}^3)}{1,000 \times P_{\text{HTH}}}$$
      </div>

      <p>For pipeline disinfection where water volume must be calculated from internal pipe geometry:</p>
      <div class="formula-box">
        $$V_{\text{pipe}} \, (\text{gallons}) = \frac{\pi \times (D_{\text{in}} / 12)^2}{4} \times L_{\text{ft}} \times 7.48052 \approx 0.0408 \times D_{\text{in}}^2 \times L_{\text{ft}}$$
      </div>

      <p>When pre-placing tablets in pipeline joints during construction per AWWA C651 Section 4.4.2, the number of 5-gram tablets ($N_{\text{tabs}}$) required per pipe section (typically $18\text{ or }20\text{ ft}$ lengths) is:</p>
      <div class="formula-box">
        $$N_{\text{tabs}} = \left\lceil \frac{W_{\text{HTH}} \, (\text{grams})}{5.0 \, \text{g/tab}} \right\rceil = \left\lceil \frac{W_{\text{HTH}} \, (\text{lb}) \times 453.592}{5.0} \right\rceil$$
      </div>

      <h2>AWWA Disinfection Standards Comparison Table</h2>
      <p>The American Water Works Association (AWWA) establishes mandatory minimum disinfection dosages, holding durations, and residual testing criteria across distribution infrastructure:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Standard Specification</th>
              <th>Infrastructure Type</th>
              <th>Disinfection Method</th>
              <th>Initial Target Chlorine (mg/L)</th>
              <th>Minimum Contact Time</th>
              <th>Minimum Final Residual (mg/L)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>AWWA C651 Sec 4.4.3</td>
              <td>New Water Mains</td>
              <td>Continuous Feed</td>
              <td>25.0 &ndash; 50.0</td>
              <td>24 Hours</td>
              <td>&ge; 10.0 mg/L</td>
            </tr>
            <tr>
              <td>AWWA C651 Sec 4.4.4</td>
              <td>New Water Mains</td>
              <td>Slug Method</td>
              <td>100.0</td>
              <td>3 Hours</td>
              <td>&ge; 50.0 mg/L</td>
            </tr>
            <tr>
              <td>AWWA C651 Sec 4.4.2</td>
              <td>Small Pipes (&le; 24")</td>
              <td>Tablet Pre-placement</td>
              <td>&ge; 25.0</td>
              <td>24 Hours</td>
              <td>&ge; 10.0 mg/L</td>
            </tr>
            <tr>
              <td>AWWA C652 Method 1</td>
              <td>Finished Water Reservoirs</td>
              <td>Complete Fill</td>
              <td>10.0</td>
              <td>24 Hours (or 6h @ 50 mg/L)</td>
              <td>&ge; 2.0 mg/L</td>
            </tr>
            <tr>
              <td>AWWA C652 Method 2</td>
              <td>Finished Water Reservoirs</td>
              <td>Surface Spray / Wash</td>
              <td>200.0</td>
              <td>30 Minutes Contact</td>
              <td>Periodic Rinse Verification</td>
            </tr>
            <tr>
              <td>AWWA C654 Sec 4.2</td>
              <td>Deep Drinking Wells</td>
              <td>Casing Shock Slug</td>
              <td>50.0 &ndash; 100.0</td>
              <td>12 &ndash; 24 Hours</td>
              <td>&ge; 10.0 mg/L before pump to waste</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Practical Worked Case Study: Disinfection of 2,400 Feet of 16-Inch Water Main</h2>
      <div class="worked-example-card">
        <h3>Engineering Design Example: AWWA C651 Pipeline Commissioning</h3>
        <p><strong>Project Scope:</strong> A newly installed transmission main consisting of $2,400\text{ linear feet}$ of $16\text{-inch}$ nominal ductile iron pipe (internal diameter $D = 16.0\text{ inches}$) must be disinfected using the AWWA C651 Continuous Feed Method. Specifications dictate a minimum initial free chlorine concentration of $30.0\text{ mg/L}$ held for 24 hours. The contractor utilizes commercial $68\%\text{ available chlorine HTH}$ granular material dissolved into a concentrated stock solution pumped via a portable chemical injection pump. Stock hypochlorite is packaged in $50\text{-lb}$ plastic pails at $\$165.00$ per pail.</p>

        <p><strong>Step 1: Compute Internal Pipeline Water Volume:</strong></p>
        $$V_{\text{pipe}} = 0.0408 \times (16.0)^2 \times 2,400\text{ ft} = 0.0408 \times 256 \times 2,400 = 25,067.5\text{ gallons}$$
        <p>In million gallons: $V = 0.02507\text{ Mgal}$ (or $94.89\text{ m}^3$).</p>

        <p><strong>Step 2: Determine Pure Elemental Chlorine Equivalent Demand:</strong></p>
        $$W_{\text{Cl}_2} = 0.025068\text{ Mgal} \times 30.0\text{ mg/L} \times 8.34 = 6.272\text{ lbs pure }\text{Cl}_2\text{ equivalent (2.845 kg)}$$

        <p><strong>Step 3: Calculate Required Mass of 68% Calcium Hypochlorite:</strong></p>
        $$W_{\text{HTH}} = \frac{6.272\text{ lbs}}{0.68} = 9.224\text{ lbs of 68% HTH (4.184 kg)}$$

        <p><strong>Step 4: Alternative Joint Tablet Pre-Placement Check:</strong></p>
        <p>If pre-placing 5-gram tablets inside pipe joints during installation ($2,400\text{ ft} / 20\text{ ft joints} = 120\text{ pipe joints}$):</p>
        $$N_{\text{total tablets}} = \left\lceil \frac{9.224\text{ lbs} \times 453.592\text{ g/lb}}{5.0\text{ g/tab}} \right\rceil = \lceil 836.7 \rceil = 837\text{ tablets}$$
        $$\text{Tablets per 20-ft Pipe Joint} = \frac{837}{120} \approx 7\text{ tablets per joint glued with food-grade adhesive}$$

        <p><strong>Step 5: Chemical Procurement &amp; Cost Estimation:</strong></p>
        <p>Required dry weight is $9.22\text{ lbs}$. One standard $50\text{-lb}$ pail provides sufficient material for over 5 complete line fills or subsequent hydrostatic re-testing, incurring $\$165.00$ in chemical cost ($\$30.43$ prorated chemical usage).</p>
      </div>

      <h2>Safe Handling, Storage, and Neutralization Precautions</h2>
      <p>Calcium hypochlorite is classified under OSHA and NFPA 400 as a <strong>Class 3 Oxidizer</strong>. Safe operational protocols include:</p>
      <ul>
        <li><strong>Thermal Decomposition and Fire Hazard:</strong> Unlike table salt or lime, calcium hypochlorite undergoes violent exothermic self-sustained thermal decomposition if exposed to heat ($&gt; 55^\circ\text{C} / 130^\circ\text{F}$), sparks, or small amounts of moisture in an unvented drum. It releases toxic, asphyxiating chlorine gas ($\text{Cl}_2$) and oxygen, which accelerates nearby fires. Store only in cool, well-ventilated dedicated chemical magazines.</li>
        <li><strong>Organic Incompatibility:</strong> Contact between calcium hypochlorite and trace hydrocarbons (grease, engine oil, diesel, brake fluid, glycol antifreeze) triggers spontaneous combustion and violent deflagration. Never use dirty scoops or petroleum-greased tools when dispensing HTH.</li>
        <li><strong>Dechlorination Before Environmental Discharge:</strong> Water containing high chlorine residuals ($&gt; 0.2\text{ mg/L}$) cannot be discharged into storm sewers, ditches, or receiving streams per Clean Water Act NPDES permits due to extreme toxicity to aquatic life. Neutralize all chlorinated wash water using chemical dechlorination agents:
        $$\text{Sodium Thiosulfate: } 1.0\text{ lb } \text{Cl}_2 \text{ requires } 1.1\text{ to } 1.4\text{ lbs } \text{Na}_2\text{S}_2\text{O}_3$$
        $$\text{Sodium Bisulfite: } 1.0\text{ lb } \text{Cl}_2 \text{ requires } 1.46\text{ lbs } \text{NaHSO}_3$$
        $$\text{Ascorbic Acid (Vitamin C): } 1.0\text{ lb } \text{Cl}_2 \text{ requires } 2.48\text{ lbs } \text{C}_6\text{H}_8\text{O}_6$$
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
          <p class="footer-about">High-precision chemical dosing, water treatment, and pipeline sanitization tools conforming to AWWA, EPA, and Ten State Standards.</p>
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
            <li><a href="https://www.awwa.org" target="_blank" rel="noopener">AWWA C651 (Water Mains)</a></li>
            <li><a href="https://www.awwa.org" target="_blank" rel="noopener">AWWA C652 (Storage Tanks)</a></li>
            <li><a href="https://www.epa.gov" target="_blank" rel="noopener">EPA Drinking Water Standards</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    function updateDosePreset() {
      const mode = document.getElementById("appMode").value;
      const target = document.getElementById("targetPpm");
      if (mode === "water_main_cont") target.value = 25.0;
      else if (mode === "water_main_slug") target.value = 100.0;
      else if (mode === "tank_spray") target.value = 200.0;
      else if (mode === "tank_fill") target.value = 10.0;
      else if (mode === "well_shock") target.value = 100.0;
      else if (mode === "potable_cont") target.value = 2.0;
    }

    function toggleVolInputs() {
      const mode = document.getElementById("calcMode").value;
      document.getElementById("directGalGroup").style.display = mode === "direct_gal" ? "block" : "none";
      document.getElementById("directM3Group").style.display = mode === "direct_m3" ? "block" : "none";
      document.getElementById("pipeGroup").style.display = mode === "pipe_dims" ? "grid" : "none";
      document.getElementById("flowGroup").style.display = mode === "flow_mgd" ? "grid" : "none";
    }

    function calcCalciumHypo() {
      const mode = document.getElementById("calcMode").value;
      const targetPpm = parseFloat(document.getElementById("targetPpm").value) || 0;
      const purityPct = parseFloat(document.getElementById("hthPurity").value) || 68;
      const purityFrac = purityPct / 100;
      const ph = parseFloat(document.getElementById("waterPh").value) || 7.4;
      const tabWtGrams = parseFloat(document.getElementById("tabletWeight").value) || 5;
      const costPerLb = parseFloat(document.getElementById("hthCostPerLb").value) || 3.25;

      if (targetPpm <= 0) {
        alert("Please enter a positive target chlorine dosage.");
        return;
      }

      let totalGal = 0;
      let totalM3 = 0;

      if (mode === "direct_gal") {
        totalGal = parseFloat(document.getElementById("volGallons").value) || 0;
        totalM3 = totalGal * 0.00378541;
      } else if (mode === "direct_m3") {
        totalM3 = parseFloat(document.getElementById("volM3").value) || 0;
        totalGal = totalM3 * 264.172;
      } else if (mode === "pipe_dims") {
        const dia = parseFloat(document.getElementById("pipeDia").value) || 0;
        const len = parseFloat(document.getElementById("pipeLen").value) || 0;
        totalGal = 0.0408 * Math.pow(dia, 2) * len;
        totalM3 = totalGal * 0.00378541;
      } else if (mode === "flow_mgd") {
        const flowVal = parseFloat(document.getElementById("contFlowVal").value) || 0;
        const flowU = document.getElementById("contFlowUnit").value;
        if (flowU === "mgd") totalGal = flowVal * 1000000;
        else if (flowU === "gpm") totalGal = flowVal * 1440;
        else if (flowU === "m3h") totalGal = flowVal * 24 * 264.172;
        totalM3 = totalGal * 0.00378541;
      }

      if (totalGal <= 0) {
        alert("Water volume or flow rate must be greater than zero.");
        return;
      }

      // Calculations
      const pureCl2Lbs = (totalGal / 1000000) * targetPpm * 8.34;
      const pureCl2Kg = pureCl2Lbs * 0.453592;

      const dryHthLbs = pureCl2Lbs / purityFrac;
      const dryHthKg = dryHthLbs * 0.453592;

      const dryHthGrams = dryHthKg * 1000;
      const totalTablets = Math.ceil(dryHthGrams / tabWtGrams);

      // Speciation HOCl vs OCl- at 25C (pKa = 7.54)
      const hoclFraction = 1.0 / (1.0 + Math.pow(10, ph - 7.54));
      const hoclPct = hoclFraction * 100;

      const totalCost = dryHthLbs * costPerLb;
      const standardPails = (dryHthLbs / 50).toFixed(1);

      // UI update
      document.getElementById("resPureCl2").textContent = pureCl2Lbs.toFixed(2) + " lbs";
      document.getElementById("resPureCl2Alt").textContent = pureCl2Kg.toFixed(2) + " kg active Cl₂ equivalent";

      document.getElementById("resDryHth").textContent = dryHthLbs.toFixed(2) + " lbs";
      document.getElementById("resDryHthAlt").textContent = dryHthKg.toFixed(2) + " kg of " + purityPct + "% HTH";

      document.getElementById("resTabletCount").textContent = totalTablets.toLocaleString() + " tablets";
      document.getElementById("resTabletDesc").textContent = "@ " + tabWtGrams + "g each (" + (dryHthGrams / 1000).toFixed(2) + " kg total)";

      document.getElementById("resHoclFrac").textContent = hoclPct.toFixed(1) + "% HOCl";
      document.getElementById("resHoclDesc").textContent = (100 - hoclPct).toFixed(1) + "% OCl⁻ at pH " + ph.toFixed(1);

      document.getElementById("resTotalVol").textContent = totalGal.toLocaleString(undefined, {maximumFractionDigits: 0}) + " Gallons (" + totalM3.toLocaleString(undefined, {maximumFractionDigits: 1}) + " m³)";
      document.getElementById("resPackaging").textContent = dryHthLbs > 50 ? standardPails + " x 50-lb drums/pails" : (dryHthLbs > 5 ? (dryHthLbs / 5).toFixed(1) + " x 5-lb bottles" : dryHthLbs.toFixed(2) + " lbs bulk loose powder");
      document.getElementById("resTotalCost").textContent = "$" + totalCost.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});

      let ctVal = 0;
      let ctContext = "";
      if (document.getElementById("appMode").value === "water_main_cont") {
        ctVal = targetPpm * 24 * 60; // mg/L * min
        ctContext = "AWWA 24h continuous: " + ctVal.toLocaleString() + " mg·min/L (Massive safety margin)";
      } else if (document.getElementById("appMode").value === "water_main_slug") {
        ctVal = targetPpm * 3 * 60;
        ctContext = "AWWA 3h slug: " + ctVal.toLocaleString() + " mg·min/L";
      } else {
        ctContext = targetPpm.toFixed(1) + " mg/L free chlorine available residual";
      }
      document.getElementById("resCtMetric").textContent = ctContext;

      document.getElementById("hypoResults").style.display = "block";
    }
  </script>
</body>
</html>
"""

TOOL_6_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Caustic Soda Dosing Calculator | NaOH Neutralization &amp; Feed Rate</title>
  <meta name="description" content="Calculate sodium hydroxide (caustic soda 50% and 25%) dosing rates, chemical metering pump feed in GPH and mL/min, alkalinity boost, and pH adjustment.">
  <link rel="canonical" href="https://calchub.cloud/caustic-soda-dosing-calculator.html">
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
        "name": "Caustic Soda Dosing Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates commercial liquid sodium hydroxide (NaOH 50% and 25%) volumetric feed rates, chemical metering pump calibration, alkalinity supplementation, and acid neutralization.",
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
            "name": "What are the physical density and active chemical properties of 50% caustic soda?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Commercial 50% membrane grade sodium hydroxide (NaOH) has a specific gravity of approximately 1.53 at 20°C (density of 12.76 lb/gal or 1,530 kg/m3). Each gallon of 50% caustic solution contains exactly 6.38 lbs of pure dry 100% active NaOH."
            }
          },
          {
            "@type": "Question",
            "name": "Why does 50% caustic soda require heated chemical storage tanks?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Fifty percent caustic soda has a remarkably high freezing/crystallization point of 12°C to 14°C (53.6°F to 57°F). In cold or unheated pump rooms, 50% NaOH solidifies into dense crystals, plugging suction piping and damaging diaphragm metering heads. Facilities frequently dilute 50% NaOH down to 25% (freezing point -17°C / 1°F) to avoid tank heat tracing."
            }
          },
          {
            "@type": "Question",
            "name": "How much total alkalinity does caustic soda addition add to drinking water?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Stoichiometrically, adding 1.0 mg/L of 100% dry active NaOH increases total water alkalinity by 1.251 mg/L as calcium carbonate (CaCO3). Because commercial 50% caustic contains 0.50 lb active NaOH per pound of solution, 1.0 mg/L of 50% liquid product adds 0.625 mg/L alkalinity as CaCO3."
            }
          },
          {
            "@type": "Question",
            "name": "How do you calibrate a metering pump stroke for liquid caustic soda feed?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "First determine liquid gallons per day: GPD = (Daily dry active NaOH in lbs) / (6.38 lb dry/gal for 50% solution). Convert GPD to milliliters per minute using the hydraulic multiplier 2.6288: Rate (mL/min) = GPD * 2.6288. Measure drawdown using a graduated cylinder over 60 seconds."
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
      <span>Caustic Soda Dosing Calculator</span>
    </nav>

    <h1 class="tool-title">Caustic Soda (NaOH) Dosing &amp; Feed Calculator</h1>
    <p class="tool-subtitle">Liquid Sodium Hydroxide 50% / 25%, Metering Pump Calibration &amp; Alkalinity Stoichiometry</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="causticGrade">Caustic Soda Commercial Grade</label>
            <select id="causticGrade" class="form-control" onchange="updateGradeProps()">
              <option value="50_liquid" selected>50% Commercial Liquid NaOH (SG = 1.53, 6.38 lb active/gal, Freeze Pt 12°C)</option>
              <option value="25_liquid">25% Diluted Liquid NaOH (SG = 1.28, 2.67 lb active/gal, Freeze Pt -17°C)</option>
              <option value="20_liquid">20% Industrial Solution (SG = 1.22, 2.03 lb active/gal, Freeze Pt -26°C)</option>
              <option value="100_dry">100% Pure Dry Caustic Flakes / Beads (Alkaline Neutralization)</option>
              <option value="custom">Custom Specific Gravity &amp; Concentration</option>
            </select>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="causticFlowUnit">Water Plant Flow Units</label>
              <select id="causticFlowUnit" class="form-control" onchange="toggleCausticFlowLabels()">
                <option value="mgd" selected>MGD (Million Gallons per Day)</option>
                <option value="gpm">GPM (Gallons per Minute)</option>
                <option value="m3h">m³/hour</option>
                <option value="m3d">m³/day</option>
                <option value="lps">Liters per Second (L/s)</option>
              </select>
            </div>
            <div class="form-group">
              <label for="causticFlowVal" id="causticFlowLabel">Water Flow Rate (MGD)</label>
              <input type="number" id="causticFlowVal" class="form-control" value="4.0" step="0.1" min="0.01">
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="doseActive">Target Active NaOH Dose (mg/L or ppm pure)</label>
              <input type="number" id="doseActive" class="form-control" value="12.0" step="0.5" min="0.1">
              <span class="field-hint">Pure 100% NaOH chemical basis</span>
            </div>
            <div class="form-group">
              <label for="rawWaterAlk">Current Raw Alkalinity (mg/L as CaCO₃)</label>
              <input type="number" id="rawWaterAlk" class="form-control" value="35" step="1" min="0">
              <span class="field-hint">Initial alkalinity prior to caustic addition</span>
            </div>
          </div>

          <div id="customCausticGrid" class="grid-2-col" style="display:none;">
            <div class="form-group">
              <label for="custSG">Solution Specific Gravity (SG)</label>
              <input type="number" id="custSG" class="form-control" value="1.53" step="0.01" min="1.0">
            </div>
            <div class="form-group">
              <label for="custStrength">Active Chemical Concentration (% by weight)</label>
              <input type="number" id="custStrength" class="form-control" value="50.0" step="0.5" min="1" max="100">
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="causticPumps">Operating Duty Metering Pumps</label>
              <input type="number" id="causticPumps" class="form-control" value="1" step="1" min="1" max="4">
            </div>
            <div class="form-group">
              <label for="causticCostPerGal">Commercial Chemical Cost ($ / Gallon)</label>
              <input type="number" id="causticCostPerGal" class="form-control" value="2.40" step="0.10" min="0">
            </div>
          </div>

          <button type="button" class="btn btn-primary" onclick="calcCausticDosing()">Calculate Caustic Soda Feed &amp; Stoichiometry</button>
        </div>

        <div id="causticResults" class="results-box" style="display:none;margin-top:1.5rem;">
          <h3 class="results-title">Caustic Soda Feed Rate &amp; Alkalinity Diagnostics</h3>
          <div class="result-grid">
            <div class="result-card">
              <div class="result-label">Pure 100% NaOH Mass Demand</div>
              <div class="result-value highlight" id="resPureMass">--</div>
              <div class="result-subtext" id="resPureMassAlt">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Liquid Feed Rate (Per Pump)</div>
              <div class="result-value highlight" id="resPumpFlow">--</div>
              <div class="result-subtext" id="resPumpFlowAlt">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Daily Liquid Consumption</div>
              <div class="result-value" id="resLiquidDay">--</div>
              <div class="result-subtext" id="resLiquidDayAlt">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Total Alkalinity Increase</div>
              <div class="result-value" id="resAlkBoost">--</div>
              <div class="result-subtext" id="resFinishedAlk">--</div>
            </div>
          </div>

          <div class="result-details" style="margin-top:1rem;padding:1rem;background:var(--card-bg);border-radius:6px;border:1px solid var(--border-light);">
            <h4 style="margin-top:0;">Chemical Engineering &amp; Operational Insights</h4>
            <ul style="margin-bottom:0;line-height:1.7;">
              <li><strong>Active Chemical per Gallon:</strong> <span id="resActivePerGal">--</span></li>
              <li><strong>Freezing &amp; Crystallization Caution:</strong> <span id="resFreezeRisk">--</span></li>
              <li><strong>Estimated Chemical Expenditure:</strong> <span id="resCausticCost" style="font-weight:700;color:var(--primary);">--</span></li>
              <li><strong>Corrosion Control &amp; LSI Benefit:</strong> <span id="resCorrosionNote">--</span></li>
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
            <li><a href="pipe-sizing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Pipe Sizing &amp; Water Flow</a></li>
          </ul>
          <div style="margin-top:1.25rem;padding-top:1rem;border-top:1px solid var(--border-light);">
            <a href="chemical.html" class="sidebar-category-link">View All Chemical Calculators &rarr;</a>
          </div>
        </div>
      </aside>
    </div>

    <!-- Technical Educational Article Body (1000+ Words) -->
    <article class="article-body">
      <h2>Role of Sodium Hydroxide in Municipal and Industrial Water Treatment</h2>
      <p>Sodium hydroxide ($\text{NaOH}$, commonly termed caustic soda or lye) is the preeminent strong inorganic base deployed throughout water supply networks, industrial effluent treatment, and chemical processing facilities. Unlike hydrated lime ($\text{Ca(OH)}_2$), which produces significant insoluble calcium solids that scale feed lines, or soda ash ($\text{Na}_2\text{CO}_3$), which dissolves slowly and presents dust handling hazards, caustic soda is delivered as a clear, high-density liquid solution that can be metered directly with positive-displacement diaphragm or peristaltic pumps.</p>

      <p>In municipal drinking water operations, caustic soda serves three critical objectives: primary pH adjustment to achieve optimum coagulation windows, supplemental alkalinity restoration following acidic coagulant addition (such as alum or ferric chloride), and finished water corrosion control under the EPA Lead and Copper Rule (LCR). By maintaining distributed water within a passivating pH regime (typically $7.4\text{ to }8.5$), caustic soda stabilizes protective carbonate and phosphate films on plumbing lead and copper surfaces, preventing toxic metal leaching.</p>

      <h2>Physical and Thermodynamic Properties of Commercial Caustic Soda Grades</h2>
      <p>Commercial caustic soda is manufactured primarily via chlor-alkali electrolysis of sodium chloride brine and is transported in membrane or diaphragm cell grades. Understanding solution thermodynamics is vital because high-strength caustic exhibits severe non-linear physical behavior:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Commercial Grade</th>
              <th>Specific Gravity @ 20°C</th>
              <th>Solution Density (lb/gal)</th>
              <th>Active NaOH Content (lb/gal)</th>
              <th>Freezing / Crystallization Pt</th>
              <th>Viscosity @ 20°C (cP)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>50% Membrane Caustic Soda</td>
              <td>1.525 &ndash; 1.530</td>
              <td>12.72 &ndash; 12.76</td>
              <td>6.36 &ndash; 6.38</td>
              <td>12.0°C &ndash; 14.4°C (53.6°F &ndash; 58.0°F)</td>
              <td>78.0 cP (Highly viscous)</td>
            </tr>
            <tr>
              <td>25% Diluted Caustic Soda</td>
              <td>1.275 &ndash; 1.280</td>
              <td>10.63 &ndash; 10.68</td>
              <td>2.66 &ndash; 2.67</td>
              <td>&minus;17.2°C (1.0°F)</td>
              <td>5.5 cP</td>
            </tr>
            <tr>
              <td>20% Diluted Solution</td>
              <td>1.218 &ndash; 1.222</td>
              <td>10.15 &ndash; 10.20</td>
              <td>2.03 &ndash; 2.04</td>
              <td>&minus;26.0°C (&minus;14.8°F)</td>
              <td>3.5 cP</td>
            </tr>
            <tr>
              <td>10% Low-Strength Feed</td>
              <td>1.108 &ndash; 1.111</td>
              <td>9.24 &ndash; 9.27</td>
              <td>0.92 &ndash; 0.93</td>
              <td>&minus;10.0°C (14.0°F)</td>
              <td>1.8 cP</td>
            </tr>
          </tbody>
        </table>
      </div>

      <p>The remarkable freezing characteristic of 50% caustic soda represents one of the most frequent operational failure modes in cold climates. Because 50% NaOH crystallizes at $12^\circ\text{C}$ ($54^\circ\text{F}$)—well above the freezing point of pure water—outdoor bulk storage tanks, uninsulated fill lines, and exterior pump rooms must be equipped with immersion heaters, heat tracing cables, and thermal insulation jackets maintained above $18^\circ\text{C}$ ($65^\circ\text{F}$). Facilities unable to maintain heated storage universally specify pre-diluted 25% caustic soda, which remains liquid down to $-17^\circ\text{C}$ ($1^\circ\text{F}$).</p>

      <h2>Mathematical Formulation of Caustic Soda Metering</h2>
      <p>The engineering calculation sequence converts plant hydraulic flow rate ($Q$) and target active chemical concentration ($C_{\text{active}}$, in mg/L or ppm of pure $100\%\text{ NaOH}$) into physical liquid feed volumes and pump calibration rates:</p>

      <p>The pure active chemical mass demand ($W_{\text{active}}$) in US Customary waterworks units is:</p>
      <div class="formula-box">
        $$W_{\text{active}} \, (\text{lb/day pure NaOH}) = Q \, (\text{MGD}) \times C_{\text{active}} \, (\text{mg/L}) \times 8.34 \, \left(\frac{\text{lb/Mgal}}{\text{mg/L}}\right)$$
      </div>

      <p>In metric SI engineering units:</p>
      <div class="formula-box">
        $$W_{\text{active}} \, (\text{kg/day pure NaOH}) = \frac{Q \, (\text{m}^3/\text{day}) \times C_{\text{active}} \, (\text{g/m}^3)}{1,000}$$
      </div>

      <p>The active chemical weight concentration per gallon of commercial liquid product ($C_{\text{liquid}}$) is:</p>
      <div class="formula-box">
        $$C_{\text{liquid}} = 8.34 \times SG \times w \quad (\text{lb active NaOH per gallon})$$
      </div>
      <p>Where $SG$ is the solution specific gravity and $w$ is the decimal weight fraction of $\text{NaOH}$ (e.g., $w = 0.50$ for 50% solution). For standard 50% grade ($SG = 1.53$):</p>
      <div class="formula-box">
        $$C_{\text{liquid, 50%}} = 8.34 \times 1.53 \times 0.50 \approx 6.38 \, \text{lb active NaOH / gal}$$
      </div>

      <p>The total commercial liquid feed rate is therefore:</p>
      <div class="formula-box">
        $$Q_{\text{liquid}} \, (\text{gal/day}) = \frac{W_{\text{active}} \, (\text{lb/day})}{C_{\text{liquid}} \, (\text{lb/gal})}, \quad Q_{\text{liquid}} \, (\text{GPH}) = \frac{Q_{\text{liquid}} \, (\text{GPD})}{24}$$
      </div>

      <p>For instantaneous pump stroke calibration via draw-down cylinder testing (milliliters over 60 seconds):</p>
      <div class="formula-box">
        $$\text{Pump Drawdown Rate} \, (\text{mL/min}) = \frac{Q_{\text{liquid}} \, (\text{gal/day}) \times 3,785.41 \, \text{mL/gal}}{1,440 \, \text{min/day}} = Q_{\text{liquid}} \, (\text{GPD}) \times 2.6288$$
      </div>

      <h2>Stoichiometric Alkalinity Generation and Acid Neutralization</h2>
      <p>When caustic soda neutralizes carbon dioxide or strong mineral acids, it transforms dissolved carbonic acid ($\text{H}_2\text{CO}_3$) into bicarbonate alkalinity ($\text{HCO}_3^-$):</p>
      <div class="formula-box">
        $$\text{NaOH} + \text{H}_2\text{CO}_3 \longrightarrow \text{NaHCO}_3 + \text{H}_2\text{O}$$
      </div>
      <p>Evaluating molecular weights ($\text{MW}_{\text{NaOH}} = 40.00\text{ g/mol}$; equivalent weight of $\text{CaCO}_3 = 50.045\text{ g/eq}$):</p>
      <div class="formula-box">
        $$\Delta \text{Alkalinity} = C_{\text{active}} \times \frac{50.045}{40.00} = C_{\text{active}} \times 1.251 \, \frac{\text{mg/L alkalinity as CaCO}_3}{\text{mg/L 100% active NaOH}}$$
      </div>
      <p>Thus, every $1.0\text{ mg/L}$ of pure dry active $\text{NaOH}$ dosed increases total water alkalinity by $1.251\text{ mg/L as CaCO}_3$. Conversely, when neutralizing industrial acidic wastewater streams, caustic soda reacts according to the following stoichiometric mass ratios:</p>
      <ul>
        <li><strong>Sulfuric Acid ($\text{H}_2\text{SO}_4$, 98.08 g/mol):</strong> $1.0\text{ lb } \text{H}_2\text{SO}_4$ requires $0.816\text{ lbs pure NaOH}$ ($1.63\text{ lbs of 50% caustic}$).</li>
        <li><strong>Hydrochloric Acid ($\text{HCl}$, 36.46 g/mol):</strong> $1.0\text{ lb } \text{HCl}$ requires $1.097\text{ lbs pure NaOH}$ ($2.19\text{ lbs of 50% caustic}$).</li>
        <li><strong>Nitric Acid ($\text{HNO}_3$, 63.01 g/mol):</strong> $1.0\text{ lb } \text{HNO}_3$ requires $0.635\text{ lbs pure NaOH}$ ($1.27\text{ lbs of 50% caustic}$).</li>
        <li><strong>Alum Consumption Offsetting:</strong> Because $1.0\text{ mg/L}$ commercial alum consumes $0.505\text{ mg/L}$ alkalinity, precisely $0.404\text{ mg/L pure active NaOH}$ ($0.808\text{ mg/L of 50% caustic}$) restores exact chemical equilibrium.</li>
      </ul>

      <h2>Practical Worked Case Study: 6.0 MGD Finished Water Corrosion Passivation</h2>
      <div class="worked-example-card">
        <h3>Engineering Design Example: Lead &amp; Copper Rule Distribution Buffering</h3>
        <p><strong>Treatment Context:</strong> A conventional municipal surface water treatment plant clarifies $6.0\text{ MGD}$ of reservoir water. Coagulation with aluminum sulfate has depressed raw water alkalinity to $28.0\text{ mg/L as CaCO}_3$ and dropped finished water pH to $6.75$. To comply with the Lead and Copper Rule, the utility mandates dosing caustic soda to elevate finished water pH to $7.85$ and boost total alkalinity by $15.0\text{ mg/L as CaCO}_3$. Commercial $50\%\text{ liquid NaOH}$ ($SG = 1.53$, $6.38\text{ lb active/gal}$) is fed from a bulk storage tank through two diaphragm metering pumps operating in parallel. Commercial chemical price is $\$2.60$ per delivered gallon.</p>

        <p><strong>Step 1: Compute Target Active NaOH Concentration:</strong></p>
        <p>To produce an alkalinity increase of $\Delta \text{Alk} = 15.0\text{ mg/L as CaCO}_3$:</p>
        $$C_{\text{active}} = \frac{15.0\text{ mg/L as CaCO}_3}{1.251} = 11.99\text{ mg/L of 100% pure NaOH}$$

        <p><strong>Step 2: Determine Daily Pure Active Mass Demand:</strong></p>
        $$W_{\text{active}} = 6.0\text{ MGD} \times 11.99\text{ mg/L} \times 8.34 = 600.0\text{ lb/day pure NaOH (272.15 kg/day)}$$

        <p><strong>Step 3: Calculate Commercial 50% Liquid Volumetric Delivery:</strong></p>
        $$Q_{\text{liquid}} = \frac{600.0\text{ lb/day}}{6.38\text{ lb active/gal}} = 94.04\text{ gal/day of 50% NaOH}$$
        $$\text{Hourly Facility Feed Rate} = \frac{94.04\text{ GPD}}{24\text{ hours}} = 3.92\text{ GPH (14.83 L/h)}$$

        <p><strong>Step 4: Metering Pump Stroke Draw-down Calibration:</strong></p>
        <p>Splitting load across two duty metering pumps ($47.02\text{ GPD per pump}$):</p>
        $$\text{Rate per Pump} = 47.02\text{ GPD} \times 2.6288 = 123.6\text{ mL/min per pump}$$

        <p><strong>Step 5: Verify Finished Water Chemistry &amp; Annual Budget:</strong></p>
        $$\text{Finished Alkalinity} = 28.0 + 15.0 = 43.0\text{ mg/L as CaCO}_3$$
        $$\text{Daily Chemical Expenditure} = 94.04\text{ GPD} \times \$2.60/\text{gal} = \$244.50/\text{day (\$89,244 / year)}$$
      </div>

      <h2>Material Selection and Exothermic Dilution Safety</h2>
      <p>Caustic soda presents severe chemical burn hazards and requires rigorous process piping engineering:</p>
      <ul>
        <li><strong>Extreme Heat of Dilution:</strong> Diluting 50% caustic soda with water releases immense thermodynamic heat of solution ($\approx 10.7\text{ kcal/mol}$ of $\text{NaOH}$). Never add water into concentrated caustic; boiling steam explosions will occur. Always slowly add caustic to large volumes of cool water under continuous mechanical agitation.</li>
        <li><strong>Caustic Embrittlement:</strong> Carbon steel piping and vessels exposed to caustic concentrations above 20% at temperatures exceeding $49^\circ\text{C}$ ($120^\circ\text{F}$) suffer intergranular stress-corrosion cracking (caustic embrittlement). Piping systems should utilize Schedule 80 CPVC, PVDF, PTFE-lined steel, or Nickel alloys (Monel / Alloy 20). Aluminum, bronze, brass, and zinc/galvanized fittings must be strictly excluded, as caustic aggressively attacks amphoteric metals to generate explosive hydrogen gas ($\text{H}_2$).</li>
        <li><strong>Pump Viscosity Sizing:</strong> Due to 50% caustic's high kinematic viscosity ($78\text{ cP at }20^\circ\text{C}$), suction piping must be sized generously (minimum 1.0 to 1.5-inch diameter) with flooded suction heads to prevent cavitation in positive-displacement diaphragm pumps.</li>
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
          <p class="footer-about">High-precision chemical engineering, neutralization, and corrosion control calculation tools conforming to AWWA, EPA, and Ten State Standards.</p>
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
            <li><a href="https://www.awwa.org" target="_blank" rel="noopener">AWWA B501 (Caustic Soda)</a></li>
            <li><a href="https://www.epa.gov" target="_blank" rel="noopener">EPA Lead &amp; Copper Rule</a></li>
            <li><a href="https://www.chlorineinstitute.org" target="_blank" rel="noopener">The Chlorine Institute (Pamphlet 94)</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    const CAUSTIC_PRESETS = {
      "50_liquid": { sg: 1.53, strength: 50.0, freeze: "12°C to 14°C (54°F to 58°F). Requires heated/insulated storage!" },
      "25_liquid": { sg: 1.28, strength: 25.0, freeze: "-17°C (1°F). Safe in unheated indoor spaces." },
      "20_liquid": { sg: 1.22, strength: 20.0, freeze: "-26°C (-15°F). Excellent cold-weather stability." },
      "100_dry": { sg: 2.13, strength: 100.0, freeze: "N/A (Dry solid flake/bead). Keep moisture-sealed." },
      "custom": { sg: 1.53, strength: 50.0, freeze: "Custom solution dependent on concentration." }
    };

    function updateGradeProps() {
      const g = document.getElementById("causticGrade").value;
      document.getElementById("customCausticGrid").style.display = (g === "custom") ? "grid" : "none";
    }

    function toggleCausticFlowLabels() {
      const u = document.getElementById("causticFlowUnit").value;
      const lbl = document.getElementById("causticFlowLabel");
      if (u === "mgd") lbl.textContent = "Water Flow Rate (MGD)";
      else if (u === "gpm") lbl.textContent = "Water Flow Rate (GPM)";
      else if (u === "m3h") lbl.textContent = "Water Flow Rate (m³/hour)";
      else if (u === "m3d") lbl.textContent = "Water Flow Rate (m³/day)";
      else if (u === "lps") lbl.textContent = "Water Flow Rate (L/s)";
    }

    function calcCausticDosing() {
      const u = document.getElementById("causticFlowUnit").value;
      const flowIn = parseFloat(document.getElementById("causticFlowVal").value) || 0;
      const doseActive = parseFloat(document.getElementById("doseActive").value) || 0;
      const rawAlk = parseFloat(document.getElementById("rawWaterAlk").value) || 0;
      const gradeKey = document.getElementById("causticGrade").value;
      const pumps = parseInt(document.getElementById("causticPumps").value) || 1;
      const costPerGal = parseFloat(document.getElementById("causticCostPerGal").value) || 0;

      if (flowIn <= 0 || doseActive <= 0) {
        alert("Please enter valid positive values for flow and target dosage.");
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

      // Dry active NaOH lbs/day
      const pureLbsDay = flowMGD * doseActive * 8.34;
      const pureKgDay = pureLbsDay * 0.453592;

      let sg = 1.53;
      let concPct = 50.0;
      let freezeNote = CAUSTIC_PRESETS[gradeKey].freeze;

      if (gradeKey === "custom") {
        sg = parseFloat(document.getElementById("custSG").value) || 1.53;
        concPct = parseFloat(document.getElementById("custStrength").value) || 50.0;
      } else {
        sg = CAUSTIC_PRESETS[gradeKey].sg;
        concPct = CAUSTIC_PRESETS[gradeKey].strength;
      }

      const activeLbPerGal = 8.34 * sg * (concPct / 100);
      const isDry = gradeKey === "100_dry";

      const liquidGPD = isDry ? 0 : pureLbsDay / activeLbPerGal;
      const liquidGPH = liquidGPD / 24;
      const liquidLPD = liquidGPD * 3.78541;

      // Pump calibration mL/min
      const gpdPerPump = liquidGPD / pumps;
      const mlMinPerPump = gpdPerPump * 2.6288;
      const lphPerPump = (gpdPerPump * 3.78541) / 24;

      // Alkalinity boost: 1.0 mg/L active NaOH adds 1.251 mg/L CaCO3
      const alkIncrease = doseActive * 1.251;
      const finishedAlk = rawAlk + alkIncrease;

      const dailyCost = isDry ? (pureLbsDay * (costPerGal / 6.38)) : (liquidGPD * costPerGal);

      // UI Population
      document.getElementById("resPureMass").textContent = pureLbsDay.toFixed(1) + " lbs/day";
      document.getElementById("resPureMassAlt").textContent = pureKgDay.toFixed(1) + " kg/day pure 100% active NaOH";

      if (isDry) {
        document.getElementById("resPumpFlow").textContent = (pureLbsDay / (pumps * 24)).toFixed(2) + " lbs/hr";
        document.getElementById("resPumpFlowAlt").textContent = "Dry chemical feeder rate per hopper";
        document.getElementById("resLiquidDay").textContent = "N/A (Dry Solid)";
        document.getElementById("resLiquidDayAlt").textContent = pureLbsDay.toFixed(1) + " lbs solid flake/beads per day";
      } else {
        document.getElementById("resPumpFlow").textContent = mlMinPerPump.toFixed(1) + " mL/min";
        document.getElementById("resPumpFlowAlt").textContent = lphPerPump.toFixed(2) + " L/h (" + (liquidGPH / pumps).toFixed(2) + " GPH per pump)";
        document.getElementById("resLiquidDay").textContent = liquidGPH.toFixed(2) + " GPH";
        document.getElementById("resLiquidDayAlt").textContent = liquidGPD.toFixed(1) + " GPD (" + liquidLPD.toFixed(1) + " L/day)";
      }

      document.getElementById("resAlkBoost").textContent = "+" + alkIncrease.toFixed(1) + " mg/L as CaCO₃";
      document.getElementById("resFinishedAlk").textContent = "Finished alkalinity: " + finishedAlk.toFixed(1) + " mg/L (" + rawAlk.toFixed(1) + " raw + " + alkIncrease.toFixed(1) + " added)";

      document.getElementById("resActivePerGal").textContent = isDry ? "100% dry solid chemical" : activeLbPerGal.toFixed(2) + " lbs active NaOH / gallon (" + (concPct).toFixed(1) + "% by wt, SG = " + sg.toFixed(2) + ")";
      document.getElementById("resFreezeRisk").textContent = freezeNote;
      document.getElementById("resCausticCost").textContent = "$" + dailyCost.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2}) + " / day ($" + (dailyCost * 30).toLocaleString(undefined, {maximumFractionDigits: 0}) + " / month)";

      let corrosionNote = "";
      if (finishedAlk < 30) {
        corrosionNote = "Marginal buffer (< 30 mg/L). Low pH buffering stability.";
      } else if (finishedAlk <= 80) {
        corrosionNote = "Optimized municipal drinking water distribution range (Lead & Copper passivation).";
      } else {
        corrosionNote = "Robust alkalinity buffer (> 80 mg/L). Excellent buffering capacity.";
      }
      document.getElementById("resCorrosionNote").textContent = corrosionNote;

      document.getElementById("causticResults").style.display = "block";
    }
  </script>
</body>
</html>
"""

def generate():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p1 = os.path.join(root, "calcium-hypochlorite-dosing-calculator.html")
    p2 = os.path.join(root, "caustic-soda-dosing-calculator.html")
    
    with open(p1, "w", encoding="utf-8") as f:
        f.write(TOOL_5_HTML.strip() + "\n")
    print(f"Generated {p1}")

    with open(p2, "w", encoding="utf-8") as f:
        f.write(TOOL_6_HTML.strip() + "\n")
    print(f"Generated {p2}")

if __name__ == "__main__":
    generate()
