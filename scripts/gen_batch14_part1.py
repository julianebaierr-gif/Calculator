# -*- coding: utf-8 -*-
"""
Script to generate Batch 14 Part 1 tools:
1. soil-gravel-calculator.html
2. tile-calculator.html
"""
import os

TOOL_1_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Soil &amp; Gravel Calculator | Earthwork Volume &amp; Tonnage Estimator</title>
  <meta name="description" content="Calculate soil, gravel, crushed stone, and road base volume, compaction shrinkage, in-place tonnage, cubic yards, cubic meters, and dump truck loads.">
  <link rel="canonical" href="https://calchub.cloud/soil-gravel-calculator.html">
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
        "name": "Soil & Gravel Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Computes volume, tonnage, compaction shrink allowances, loose haulage requirements, and truck delivery trips for aggregate gravel, topsoil, and engineered backfill.",
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
            "name": "How is soil and gravel compaction shrinkage factored into material orders?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "When soil or crushed aggregate is spread and compacted on site using pneumatic rollers or vibratory plates, air voids are expelled. The compacted volume (CCY) is smaller than the loose delivered volume (LCY). Contractors must order loose material equal to V_loose = V_compacted * (1 + Compaction Factor), where compaction factors typically range from 12% to 25% depending on gradation."
            }
          },
          {
            "@type": "Question",
            "name": "What is the typical bulk density of crushed aggregate gravel versus topsoil?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Dry crushed limestone gravel (#57 stone) has a loose bulk density of approximately 1.4 to 1.55 tons per cubic yard (95 to 105 lb/cu ft or 1,450 to 1,600 kg/m3), reaching 1.8 to 2.1 t/yd3 when densely compacted with fines. Screened dry topsoil averages 1.0 to 1.2 tons per cubic yard (75 to 85 lb/cu ft), while moist clay loam can exceed 1.35 t/yd3."
            }
          },
          {
            "@type": "Question",
            "name": "How many cubic yards or tons fit into a standard tandem dump truck?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A standard tandem-axle dump truck generally carries 10 to 14 cubic yards of bulk material with a highway gross payload limit of roughly 12 to 16 US tons. Tri-axle and quad-axle dump trucks carry 15 to 22 cubic yards (18 to 24 tons), depending on state bridge gross weight formulas."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between Bank Cubic Yards (BCY), Loose Cubic Yards (LCY), and Compacted Cubic Yards (CCY)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "BCY is earth in its undisturbed natural state. LCY is earth that has been excavated, which swells in volume due to introduced voids (typically 15% to 35% swell). CCY is earth placed in embankments or subbase and mechanically rolled, resulting in higher density and lower volume than its loose state."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="civil">
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
        <a href="civil.html" class="active">Civil &amp; Roof</a>
        <a href="solar-energy.html">Solar</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo; 
      <a href="civil.html">Civil &amp; Construction</a> &rsaquo; 
      <span>Soil &amp; Gravel Calculator</span>
    </nav>

    <h1 class="tool-title">Soil &amp; Gravel Volume &amp; Tonnage Calculator</h1>
    <p class="tool-subtitle">Geotechnical Earthwork, Compaction Shrinkage, Haulage &amp; Quarry Material Sizing</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="materialType">Material Selection &amp; Gradation</label>
            <select id="materialType" class="form-control" onchange="updateDensityPreset()">
              <option value="crushed_stone" selected>Crushed Stone / Dense Graded Base (#57 / 21A) (105 lb/cu ft / 1.42 t/yd³)</option>
              <option value="pea_gravel">Pea Gravel / River Rock (100 lb/cu ft / 1.35 t/yd³)</option>
              <option value="bank_gravel">Bank Run Gravel (Sandy Gravel) (115 lb/cu ft / 1.55 t/yd³)</option>
              <option value="topsoil">Screened Topsoil / Loam (80 lb/cu ft / 1.08 t/yd³)</option>
              <option value="clay_fill">Compacted Clay / Common Fill (110 lb/cu ft / 1.48 t/yd³)</option>
              <option value="sand">Coarse Concrete Sand (95 lb/cu ft / 1.28 t/yd³)</option>
              <option value="crushed_concrete">Recycled Crushed Concrete (RCA) (92 lb/cu ft / 1.24 t/yd³)</option>
              <option value="custom">Custom Bulk Density</option>
            </select>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="unitSystem">Measurement System</label>
              <select id="unitSystem" class="form-control" onchange="toggleUnitLabels()">
                <option value="imperial" selected>Imperial (Feet, Inches, US Tons)</option>
                <option value="metric">Metric (Meters, Centimeters, Tonnes)</option>
              </select>
            </div>
            <div class="form-group">
              <label for="densityInput" id="densityLabel">Loose Bulk Density (tons / yd³)</label>
              <input type="number" id="densityInput" class="form-control" value="1.42" step="0.01" min="0.5">
            </div>
          </div>

          <div class="form-group">
            <label>Plan Geometry Style</label>
            <div class="radio-group" style="display:flex;gap:1.5rem;margin-bottom:0.5rem;">
              <label><input type="radio" name="geomStyle" value="rect" checked onchange="toggleGeom()"> Rectangular Area</label>
              <label><input type="radio" name="geomStyle" value="circle" onchange="toggleGeom()"> Circular Area</label>
              <label><input type="radio" name="geomStyle" value="direct" onchange="toggleGeom()"> Direct Area Input</label>
            </div>
          </div>

          <div id="rectInputs" class="grid-2-col">
            <div class="form-group">
              <label for="lengthInput" id="lengthLabel">Length (ft)</label>
              <input type="number" id="lengthInput" class="form-control" value="60" step="0.5" min="0.1">
            </div>
            <div class="form-group">
              <label for="widthInput" id="widthLabel">Width (ft)</label>
              <input type="number" id="widthInput" class="form-control" value="20" step="0.5" min="0.1">
            </div>
          </div>

          <div id="circleInputs" class="form-group" style="display:none;">
            <label for="diameterInput" id="diameterLabel">Diameter (ft)</label>
            <input type="number" id="diameterInput" class="form-control" value="30" step="0.5" min="0.1">
          </div>

          <div id="directInputs" class="form-group" style="display:none;">
            <label for="areaInput" id="areaLabel">Total Surface Area (sq ft)</label>
            <input type="number" id="areaInput" class="form-control" value="1200" step="1" min="1">
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="depthInput" id="depthLabel">Layer Thickness / Depth (inches)</label>
              <input type="number" id="depthInput" class="form-control" value="4" step="0.25" min="0.1">
            </div>
            <div class="form-group">
              <label for="compactionPct">Compaction Shrinkage Allowance (%)</label>
              <input type="number" id="compactionPct" class="form-control" value="15" step="1" min="0" max="60">
              <span class="field-hint">Extra material ordered to achieve compacted in-place thickness (typically 10&ndash;25%)</span>
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="truckCapacity" id="truckLabel">Dump Truck Capacity (US Tons)</label>
              <input type="number" id="truckCapacity" class="form-control" value="14" step="1" min="1">
            </div>
            <div class="form-group">
              <label for="pricePerTon">Estimated Material Price ($ / ton or tonne)</label>
              <input type="number" id="pricePerTon" class="form-control" value="38" step="0.50" min="0">
            </div>
          </div>

          <button type="button" class="btn btn-primary" onclick="calcSoilGravel()">Calculate Earthwork &amp; Tonnage</button>
        </div>

        <div id="calcResults" class="results-box" style="display:none;margin-top:1.5rem;">
          <h3 class="results-title">Earthwork Sizing &amp; Haulage Summary</h3>
          <div class="result-grid">
            <div class="result-card">
              <div class="result-label">Net In-Place Compacted Volume</div>
              <div class="result-value" id="resCompactedVol">--</div>
              <div class="result-subtext" id="resCompactedVolAlt">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Gross Order Volume (Loose LCY / m³)</div>
              <div class="result-value highlight" id="resOrderVol">--</div>
              <div class="result-subtext" id="resOrderVolAlt">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Total Mass to Order</div>
              <div class="result-value highlight" id="resTotalWeight">--</div>
              <div class="result-subtext" id="resTotalWeightAlt">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Estimated Delivery Loads</div>
              <div class="result-value" id="resTruckLoads">--</div>
              <div class="result-subtext" id="resTruckLoadsSub">Full payload dump trips</div>
            </div>
          </div>

          <div class="result-details" style="margin-top:1rem;padding:1rem;background:var(--card-bg);border-radius:6px;border:1px solid var(--border-light);">
            <h4 style="margin-top:0;">Cost &amp; Material Breakdown</h4>
            <ul style="margin-bottom:0;line-height:1.7;">
              <li><strong>Surface Area:</strong> <span id="resArea">--</span></li>
              <li><strong>Compaction Adjustment:</strong> <span id="resCompactionFactor">--</span></li>
              <li><strong>Estimated Material Cost:</strong> <span id="resTotalCost" style="font-weight:700;color:var(--primary);">--</span></li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Related Category Sidebar -->
      <aside class="post-sidebar">
        <div class="sidebar-widget">
          <div class="sidebar-widget-header">
            <span class="widget-icon">🏗️</span>
            <h3 class="widget-title">Related Civil Calculators</h3>
          </div>
          <p class="sidebar-widget-subtitle">Specialized calculation tools in this discipline:</p>
          <ul class="sidebar-links-list">
            <li><a href="gravel-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Gravel &amp; Aggregate Estimator</a></li>
            <li><a href="excavation-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Excavation &amp; Earthwork Haul</a></li>
            <li><a href="excavation-volume-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Excavation Volume Calculator</a></li>
            <li><a href="asphalt-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Asphalt Paving &amp; Tonnage</a></li>
            <li><a href="concrete-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Concrete Slab, Footing &amp; Column</a></li>
            <li><a href="footing-size-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Footing Size &amp; Soil Bearing</a></li>
          </ul>
          <div style="margin-top:1.25rem;padding-top:1rem;border-top:1px solid var(--border-light);">
            <a href="civil.html" class="sidebar-category-link">View All Civil Calculators &rarr;</a>
          </div>
        </div>
      </aside>
    </div>

    <!-- Technical Educational Article Body (1000+ Words) -->
    <article class="article-body">
      <h2>Engineering Fundamentals of Soil and Aggregate Gravel Earthworks</h2>
      <p>Earthwork estimating, subgrade preparation, and granular base placement represent the primary structural foundation of civil infrastructure projects ranging from residential driveways and commercial building pads to interstate highways and airfield runways. Soil and crushed aggregate materials behave distinctly from manufactured structural materials like steel or cured concrete because their volumetric and gravimetric parameters shift dynamically through the three standard geotechnical phases: bank state, loose excavated state, and mechanically compacted state.</p>

      <p>When civil engineers and earthwork contractors calculate material quantities for purchasing and site placement, failure to account for moisture content, void ratios, and mechanical compaction shrinkage invariably results in either significant material shortages or expensive over-ordering. This comprehensive soil and gravel calculation framework integrates ASTM geotechnical testing standards (ASTM D698, ASTM D1557, ASTM C29) and AASHTO transportation specifications to translate target geometric design boundaries into rigorous quarry order tonnages, loose haulage volumes, and dump truck cycle logistics.</p>

      <h2>The Three Volumetric States: Bank, Loose, and Compacted</h2>
      <p>Geotechnical earthmoving revolves around three distinct volumetric classifications defined by relative bulk density and soil mechanics:</p>
      <ul>
        <li><strong>Bank Cubic Yards (BCY) / Bank Cubic Meters (BCM):</strong> Earth and rock in its natural, undisturbed geological stratum prior to ripping, grading, or bucket excavation. It possesses natural pre-consolidation density governed by overburden pressure and geologic history.</li>
        <li><strong>Loose Cubic Yards (LCY) / Loose Cubic Meters (LCM):</strong> Material that has been excavated, blasted, crushed, or loaded into haul units. The excavation and crushing processes break intergranular bonds and introduce substantial void spaces filled with ambient air, causing the material to swell. The swell factor $S_w$ increases volume by 10% to 40% above the bank volume.</li>
        <li><strong>Compacted Cubic Yards (CCY) / Compacted Cubic Meters (CCM):</strong> Material placed in uniform lifts (typically 6 to 12 inches thick) and systematically densified using heavy compaction plant (smooth drum vibratory rollers, padfoot rollers, or pneumatic-tired compactors). Compaction forces out entrapped air, aligns soil grains, and achieves target relative compaction (typically 95% to 98% of Standard or Modified Proctor maximum dry density).</li>
      </ul>

      <h2>Governing Mathematical Formulas for Earthwork Sizing</h2>
      <p>The calculation sequence begins with geometric volume determination for the specified design layer thickness:</p>

      <div class="formula-box">
        $$V_{\text{geom, imperial}} = \frac{A_{\text{surface}} \, (\text{sq ft}) \times t \, (\text{inches})}{12 \times 27} = \frac{A_{\text{surface}} \times t}{324} \quad (\text{cu yd})$$
      </div>

      <p>In metric units, the design compacted volume is simply the product of plan area and layer depth:</p>

      <div class="formula-box">
        $$V_{\text{geom, metric}} = A_{\text{surface}} \, (\text{m}^2) \times \frac{t \, (\text{cm})}{100} = A_{\text{surface}} \times t_{\text{meters}} \quad (\text{m}^3)$$
      </div>

      <p>To compensate for mechanical shrinkage during roller passes, the gross loose order volume ($V_{\text{order}}$) is scaled by the compaction factor ($C_f$):</p>

      <div class="formula-box">
        $$V_{\text{order}} = V_{\text{compacted}} \times \left(1 + \frac{C_{\%}}{100}\right)$$
      </div>

      <p>Where $C_{\%}$ is the anticipated compaction shrinkage percentage (commonly 12% to 20% for dense-graded crushed stone base course and 15% to 25% for uncompacted topsoil and backfill loam).</p>

      <p>The total weight required for purchase from aggregate quarries or soil suppliers is calculated using the bulk density ($\rho_{\text{loose}}$):</p>

      <div class="formula-box">
        $$W_{\text{tons}} = V_{\text{order}} \, (\text{cu yd}) \times \rho_{\text{bulk}} \, \left(\frac{\text{US tons}}{\text{yd}^3}\right)$$
      </div>

      <p>Haulage fleet logistics require rounding up to the nearest integer delivery truckload based on road-legal vehicular payload ratings ($P_{\text{truck}}$):</p>

      <div class="formula-box">
        $$N_{\text{loads}} = \left\lceil \frac{W_{\text{tons}}}{P_{\text{truck}}} \right\rceil$$
      </div>

      <h2>Geotechnical Soil &amp; Aggregate Material Reference Table</h2>
      <p>The table below provides engineering benchmark densities, compaction shrinkage factors, and swell ratios across common earthwork materials per ASTM C29, AASHTO T 99, and NAVFAC DM 7.02:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Material Classification</th>
              <th>AASHTO / ASTM Code</th>
              <th>Loose Density (lb/cu ft)</th>
              <th>Loose Density (tons/yd³)</th>
              <th>Compacted Density (t/yd³)</th>
              <th>Compaction Shrinkage</th>
              <th>Excavation Swell</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Dense Graded Base (Crushed Limestone / 21A)</td>
              <td>AASHTO M 147 / ASTM D2940</td>
              <td>100 &ndash; 110</td>
              <td>1.35 &ndash; 1.48</td>
              <td>1.65 &ndash; 1.85</td>
              <td>15% &ndash; 22%</td>
              <td>20% &ndash; 25%</td>
            </tr>
            <tr>
              <td>Washed #57 Open-Graded Crushed Stone</td>
              <td>ASTM C33 Size 57</td>
              <td>95 &ndash; 105</td>
              <td>1.28 &ndash; 1.42</td>
              <td>1.45 &ndash; 1.55</td>
              <td>8% &ndash; 12%</td>
              <td>25% &ndash; 30%</td>
            </tr>
            <tr>
              <td>Pea Gravel / Uncrushed River Rock</td>
              <td>ASTM C33 Coarse</td>
              <td>95 &ndash; 102</td>
              <td>1.28 &ndash; 1.38</td>
              <td>1.40 &ndash; 1.50</td>
              <td>6% &ndash; 10%</td>
              <td>15% &ndash; 20%</td>
            </tr>
            <tr>
              <td>Sandy Gravel (Bank Run / Subbase)</td>
              <td>USCS: GW-SW</td>
              <td>110 &ndash; 120</td>
              <td>1.48 &ndash; 1.62</td>
              <td>1.75 &ndash; 1.95</td>
              <td>14% &ndash; 20%</td>
              <td>15% &ndash; 18%</td>
            </tr>
            <tr>
              <td>Coarse Sand (Concrete Sand)</td>
              <td>ASTM C33 Fine Aggregate</td>
              <td>90 &ndash; 100</td>
              <td>1.22 &ndash; 1.35</td>
              <td>1.45 &ndash; 1.60</td>
              <td>10% &ndash; 15%</td>
              <td>12% &ndash; 15%</td>
            </tr>
            <tr>
              <td>Common Fill Clay Loam</td>
              <td>USCS: CL / ML</td>
              <td>100 &ndash; 115</td>
              <td>1.35 &ndash; 1.55</td>
              <td>1.60 &ndash; 1.80</td>
              <td>18% &ndash; 25%</td>
              <td>25% &ndash; 35%</td>
            </tr>
            <tr>
              <td>Screened Loam / Planting Topsoil</td>
              <td>Landscape Grade A</td>
              <td>75 &ndash; 85</td>
              <td>1.01 &ndash; 1.15</td>
              <td>1.20 &ndash; 1.30</td>
              <td>20% &ndash; 28%</td>
              <td>30% &ndash; 40%</td>
            </tr>
            <tr>
              <td>Recycled Concrete Aggregate (RCA)</td>
              <td>AASHTO M 319</td>
              <td>88 &ndash; 96</td>
              <td>1.19 &ndash; 1.30</td>
              <td>1.40 &ndash; 1.55</td>
              <td>12% &ndash; 16%</td>
              <td>20% &ndash; 25%</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Practical Worked Case Study: Commercial Parking Bay Subbase</h2>
      <div class="worked-example-card">
        <h3>Design Example: Engineered Driveway &amp; Parking Apron</h3>
        <p><strong>Project Scenario:</strong> A civil site plan requires placing a 6-inch (0.50 ft) compacted subbase course of dense-graded crushed limestone aggregate (#21A / Crusher Run) over an engineered subgrade measuring 120 feet in length by 30 feet in width. The project specification dictates compaction to 98% Modified Proctor density with a design compaction shrinkage allowance of 18%. The quarry supplies crushed stone at a loose bulk density of 105 lb/cu ft (1.42 tons per cubic yard), delivered via 15-ton tri-axle dump trucks at $42.00 per ton delivered.</p>

        <p><strong>Step 1: Compute the Net In-Place Compacted Volume:</strong></p>
        <p>Surface Plan Area:</p>
        $$A_{\text{surface}} = 120\text{ ft} \times 30\text{ ft} = 3,600\text{ sq ft}$$
        <p>In-place Compacted Cubic Yards:</p>
        $$V_{\text{compacted}} = \frac{3,600\text{ sq ft} \times 6\text{ inches}}{324} = \frac{21,600}{324} = 66.67\text{ cu yd}$$

        <p><strong>Step 2: Apply the Compaction Shrinkage Factor:</strong></p>
        <p>To ensure 66.67 cu yd remains after heavy vibratory rolling, loose quarry material must be ordered:</p>
        $$V_{\text{order}} = 66.67\text{ cu yd} \times (1 + 0.18) = 66.67 \times 1.18 = 78.67\text{ cu yd (LCY)}$$

        <p><strong>Step 3: Determine Quarry Order Tonnage:</strong></p>
        <p>At a loose bulk density of 1.42 tons/yd³:</p>
        $$W_{\text{tons}} = 78.67\text{ yd}^3 \times 1.42\text{ tons/yd}^3 = 111.71\text{ US tons}$$

        <p><strong>Step 4: Haulage Fleet Dispatch &amp; Cost Estimation:</strong></p>
        $$N_{\text{truckloads}} = \left\lceil \frac{111.71}{15} \right\rceil = \lceil 7.45 \rceil = 8\text{ truck trips}$$
        <p>Total Material Procurement Cost:</p>
        $$\text{Total Cost} = 111.71\text{ tons} \times \$42.00/\text{ton} = \$4,691.82$$
      </div>

      <h2>Construction Best Practices and Quality Control</h2>
      <p>Achieving structural stability in aggregate base layers and engineered fills requires strict adherence to soil mechanics fundamentals:</p>
      <ul>
        <li><strong>Optimum Moisture Content (OMC):</strong> Compacting gravel or soil that is either too dry or saturated prevents target density. Soil moisture should be maintained within $\pm 2\%$ of the Proctor optimum using water truck spray bars before running compaction equipment.</li>
        <li><strong>Lift Thickness Limitations:</strong> Never place aggregate base in loose lifts exceeding 8 inches (200 mm). Heavy vibratory rollers cannot transfer sufficient dynamic compaction energy below an 8-inch depth, resulting in soft, uncompacted sub-layers prone to settlement and potholing.</li>
        <li><strong>Geotextile Separation:</strong> On soft subgrades with a California Bearing Ratio (CBR) under 3, install a woven or non-woven geotextile separation fabric between the native soil and the gravel subbase. This prevents crushed rock from punching down into the subgrade mud while stopping fine silts from pumping up into the drainage aggregate.</li>
        <li><strong>Nuclear Density Gauge Testing:</strong> Verify in-place dry density and moisture content per ASTM D6938 prior to placing asphalt or concrete surface courses. Proof-roll the finished subbase with a fully loaded 20-ton tandem dump truck to identify deflection or rutting.</li>
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
          <p class="footer-about">High-precision engineering and construction calculation tools conforming to ASTM, ACI, and AASHTO specifications.</p>
        </div>
        <div class="footer-col">
          <h4 class="footer-title">Engineering Disciplines</h4>
          <ul class="footer-links">
            <li><a href="civil.html">Civil &amp; Construction</a></li>
            <li><a href="mechanical.html">Mechanical &amp; HVAC</a></li>
            <li><a href="engineering.html">Electrical &amp; Electronics</a></li>
            <li><a href="chemical.html">Chemical &amp; Water Treatment</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4 class="footer-title">Standard References</h4>
          <ul class="footer-links">
            <li><a href="https://www.astm.org" target="_blank" rel="noopener">ASTM International</a></li>
            <li><a href="https://www.transportation.org" target="_blank" rel="noopener">AASHTO Standards</a></li>
            <li><a href="https://www.fhwa.dot.gov" target="_blank" rel="noopener">FHWA Earthwork Specs</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    const DENSITY_PRESETS = {
      crushed_stone: { imperial: 1.42, metric: 1.68, comp: 18 },
      pea_gravel: { imperial: 1.35, metric: 1.60, comp: 10 },
      bank_gravel: { imperial: 1.55, metric: 1.84, comp: 16 },
      topsoil: { imperial: 1.08, metric: 1.28, comp: 22 },
      clay_fill: { imperial: 1.48, metric: 1.75, comp: 20 },
      sand: { imperial: 1.28, metric: 1.52, comp: 12 },
      crushed_concrete: { imperial: 1.24, metric: 1.47, comp: 14 },
      custom: { imperial: 1.40, metric: 1.65, comp: 15 }
    };

    function updateDensityPreset() {
      const type = document.getElementById("materialType").value;
      const isMetric = document.getElementById("unitSystem").value === "metric";
      if (type !== "custom") {
        const val = isMetric ? DENSITY_PRESETS[type].metric : DENSITY_PRESETS[type].imperial;
        document.getElementById("densityInput").value = val;
        document.getElementById("compactionPct").value = DENSITY_PRESETS[type].comp;
      }
    }

    function toggleUnitLabels() {
      const isMetric = document.getElementById("unitSystem").value === "metric";
      document.getElementById("densityLabel").textContent = isMetric ? "Loose Bulk Density (tonnes / m³)" : "Loose Bulk Density (US tons / yd³)";
      document.getElementById("lengthLabel").textContent = isMetric ? "Length (m)" : "Length (ft)";
      document.getElementById("widthLabel").textContent = isMetric ? "Width (m)" : "Width (ft)";
      document.getElementById("diameterLabel").textContent = isMetric ? "Diameter (m)" : "Diameter (ft)";
      document.getElementById("areaLabel").textContent = isMetric ? "Total Surface Area (sq m)" : "Total Surface Area (sq ft)";
      document.getElementById("depthLabel").textContent = isMetric ? "Layer Thickness (cm)" : "Layer Thickness (inches)";
      document.getElementById("truckLabel").textContent = isMetric ? "Dump Truck Capacity (Tonnes)" : "Dump Truck Capacity (US Tons)";
      updateDensityPreset();
    }

    function toggleGeom() {
      const style = document.querySelector('input[name="geomStyle"]:checked').value;
      document.getElementById("rectInputs").style.display = style === "rect" ? "grid" : "none";
      document.getElementById("circleInputs").style.display = style === "circle" ? "block" : "none";
      document.getElementById("directInputs").style.display = style === "direct" ? "block" : "none";
    }

    function calcSoilGravel() {
      const isMetric = document.getElementById("unitSystem").value === "metric";
      const style = document.querySelector('input[name="geomStyle"]:checked').value;
      const depth = parseFloat(document.getElementById("depthInput").value) || 0;
      const compPct = parseFloat(document.getElementById("compactionPct").value) || 0;
      const density = parseFloat(document.getElementById("densityInput").value) || 1.4;
      const truckCap = parseFloat(document.getElementById("truckCapacity").value) || 14;
      const pricePerTon = parseFloat(document.getElementById("pricePerTon").value) || 0;

      let area = 0;
      if (style === "rect") {
        const l = parseFloat(document.getElementById("lengthInput").value) || 0;
        const w = parseFloat(document.getElementById("widthInput").value) || 0;
        area = l * w;
      } else if (style === "circle") {
        const d = parseFloat(document.getElementById("diameterInput").value) || 0;
        area = Math.PI * Math.pow(d / 2, 2);
      } else {
        area = parseFloat(document.getElementById("areaInput").value) || 0;
      }

      if (area <= 0 || depth <= 0) {
        alert("Please enter valid positive dimensions.");
        return;
      }

      let netVol = 0; // cu yd or m3
      let netVolAlt = 0; // m3 or cu yd
      let orderVol = 0;
      let orderVolAlt = 0;

      if (!isMetric) {
        // Area sq ft, depth inches -> cu yd
        netVol = (area * depth) / 324; // cu yd
        netVolAlt = netVol * 0.764555; // m3
        orderVol = netVol * (1 + compPct / 100);
        orderVolAlt = orderVol * 0.764555;
      } else {
        // Area sq m, depth cm -> m3
        netVol = area * (depth / 100); // m3
        netVolAlt = netVol * 1.30795; // cu yd
        orderVol = netVol * (1 + compPct / 100);
        orderVolAlt = orderVol * 1.30795;
      }

      const totalWeight = orderVol * density;
      const totalWeightAlt = isMetric ? totalWeight * 1.10231 : totalWeight * 0.907185;
      const truckLoads = Math.ceil(totalWeight / truckCap);
      const totalCost = totalWeight * pricePerTon;

      document.getElementById("resCompactedVol").textContent = netVol.toFixed(2) + (isMetric ? " m³" : " cu yd");
      document.getElementById("resCompactedVolAlt").textContent = netVolAlt.toFixed(2) + (isMetric ? " cu yd (equiv)" : " m³ (equiv)");
      document.getElementById("resOrderVol").textContent = orderVol.toFixed(2) + (isMetric ? " m³ (loose)" : " cu yd (loose)");
      document.getElementById("resOrderVolAlt").textContent = orderVolAlt.toFixed(2) + (isMetric ? " cu yd (loose)" : " m³ (loose)");
      document.getElementById("resTotalWeight").textContent = totalWeight.toFixed(2) + (isMetric ? " Tonnes" : " US Tons");
      document.getElementById("resTotalWeightAlt").textContent = totalWeightAlt.toFixed(2) + (isMetric ? " US Tons" : " Metric Tonnes");
      document.getElementById("resTruckLoads").textContent = truckLoads + " loads";
      document.getElementById("resTruckLoadsSub").textContent = "@ " + truckCap + (isMetric ? " tonnes/truck" : " tons/truck");

      document.getElementById("resArea").textContent = area.toFixed(1) + (isMetric ? " sq meters" : " sq feet");
      document.getElementById("resCompactionFactor").textContent = compPct.toFixed(1) + "% (" + (1 + compPct/100).toFixed(2) + "x order multiplier)";
      document.getElementById("resTotalCost").textContent = "$" + totalCost.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});

      document.getElementById("calcResults").style.display = "block";
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
  <title>Tile Calculator | Floor &amp; Wall Tile, Grout &amp; Mortar Sizer</title>
  <meta name="description" content="Calculate floor and wall tile counts, carton boxes, layout wastage, grout bag requirements, and thinset mortar coverage per TCNA ANSI standards.">
  <link rel="canonical" href="https://calchub.cloud/tile-calculator.html">
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
        "name": "Tile Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates ceramic, porcelain, and stone tile piece counts, carton boxes, layout wastage margins, grout weight, and thinset mortar bed requirements.",
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
            "name": "How much tile waste percentage should be added to an installation?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For standard grid or stacked patterns on simple rectangular floors, a 10% wastage allowance is recommended. For diagonal, herringbone, chevron, or rooms with numerous niches and irregular angles, specify 15% to 20% waste to accommodate perimeter angle cuts and breakages."
            }
          },
          {
            "@type": "Question",
            "name": "How is grout consumption calculated for floor and wall tiles?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Grout consumption is governed by the joint geometry formula: Grout Weight = [(Tile Length + Tile Width) * Joint Width * Tile Thickness * Grout Density] / (Tile Length * Tile Width) * Surface Area. Narrow joints (1/16 to 1/8 inch) consume significantly less grout than wide 1/4 to 3/8 inch rustic joints."
            }
          },
          {
            "@type": "Question",
            "name": "What size trowel notch is required for thinset mortar coverage?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Per TCNA guidelines, tiles up to 8x8 inches use a 1/4x1/4 inch square-notch trowel (covering approx 80-90 sq ft per 50 lb bag). Large format tiles (12x24 inches or greater) require a 1/2x1/2 inch trowel with back-buttering (covering approx 40-50 sq ft per 50 lb bag) to achieve minimum 80% interior and 95% wet-area contact coverage."
            }
          },
          {
            "@type": "Question",
            "name": "Should deductions for doors, vanities, and tubs be excluded from the tile order?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Large un-tiled obstacles like built-in bathtubs, kitchen islands, and prefabricated shower pans should be deducted from gross room square footage. However, freestanding vanities or appliances placed on top of finished floors should have tiles installed underneath and must remain included in the order."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="civil">
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
        <a href="civil.html" class="active">Civil &amp; Roof</a>
        <a href="solar-energy.html">Solar</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo; 
      <a href="civil.html">Civil &amp; Construction</a> &rsaquo; 
      <span>Tile Calculator</span>
    </nav>

    <h1 class="tool-title">Tile, Grout &amp; Mortar Calculator</h1>
    <p class="tool-subtitle">Floor &amp; Wall Tile Piece Counts, Cartons, TCNA Thinset &amp; Joint Grout Sizing</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="tilePreset">Tile Size Standard Preset</label>
            <select id="tilePreset" class="form-control" onchange="updateTilePreset()">
              <option value="12x24" selected>12" &times; 24" Large Format Porcelain (300 &times; 600 mm)</option>
              <option value="12x12">12" &times; 12" Standard Ceramic / Stone (300 &times; 300 mm)</option>
              <option value="24x24">24" &times; 24" Extra Large Porcelain (600 &times; 600 mm)</option>
              <option value="6x24">6" &times; 24" Wood Plank Tile (150 &times; 600 mm)</option>
              <option value="3x6">3" &times; 6" Subway Tile (75 &times; 150 mm)</option>
              <option value="4x4">4" &times; 4" Square Wall Tile (100 &times; 100 mm)</option>
              <option value="hex_2">2" Mosaic Hexagon Sheet (300 &times; 300 mm sheet)</option>
              <option value="custom">Custom Dimensions</option>
            </select>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="tileUnit">Measurement Units</label>
              <select id="tileUnit" class="form-control" onchange="toggleTileUnits()">
                <option value="imperial" selected>Imperial (Inches, Feet, Lbs)</option>
                <option value="metric">Metric (Millimeters, Meters, Kg)</option>
              </select>
            </div>
            <div class="form-group">
              <label for="tileThickness" id="thicknessLabel">Tile Thickness (inches)</label>
              <input type="number" id="tileThickness" class="form-control" value="0.375" step="0.025" min="0.1">
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="tileLength" id="tileLengthLabel">Tile Length (inches)</label>
              <input type="number" id="tileLength" class="form-control" value="24" step="0.25" min="0.5">
            </div>
            <div class="form-group">
              <label for="tileWidth" id="tileWidthLabel">Tile Width (inches)</label>
              <input type="number" id="tileWidth" class="form-control" value="12" step="0.25" min="0.5">
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="roomLength" id="roomLengthLabel">Room / Wall Length (ft)</label>
              <input type="number" id="roomLength" class="form-control" value="18" step="0.5" min="1">
            </div>
            <div class="form-group">
              <label for="roomWidth" id="roomWidthLabel">Room / Wall Width or Height (ft)</label>
              <input type="number" id="roomWidth" class="form-control" value="12" step="0.5" min="1">
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="deductArea" id="deductAreaLabel">Area Deductions (Doors, Tubs) (sq ft)</label>
              <input type="number" id="deductArea" class="form-control" value="15" step="1" min="0">
            </div>
            <div class="form-group">
              <label for="layoutPattern">Installation Pattern (Waste Allowance)</label>
              <select id="layoutPattern" class="form-control">
                <option value="10" selected>Straight / Grid (10% Waste)</option>
                <option value="12">Running Bond / 1/3 Offset (12% Waste)</option>
                <option value="15">Diagonal / 45-Degree (15% Waste)</option>
                <option value="18">Herringbone / Chevron (18% Waste)</option>
                <option value="20">Complex / Small Irregular Cuts (20% Waste)</option>
              </select>
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="groutJoint" id="groutJointLabel">Grout Joint Width (inches)</label>
              <select id="groutJoint" class="form-control">
                <option value="0.0625">1/16" (1.6 mm) - Rectified Precision Tiles</option>
                <option value="0.125" selected>1/8" (3.2 mm) - Standard Floor Joints</option>
                <option value="0.1875">3/16" (4.8 mm) - Semi-Polished / Wide</option>
                <option value="0.25">1/4" (6.4 mm) - Quarry / Rustic Tile</option>
                <option value="0.375">3/8" (9.5 mm) - Paver / Mexican Saltillo</option>
              </select>
            </div>
            <div class="form-group">
              <label for="boxCoverage" id="boxCoverageLabel">Square Feet per Carton Box</label>
              <input type="number" id="boxCoverage" class="form-control" value="16" step="0.5" min="1">
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="pricePerSqFt">Tile Price ($ / sq ft or sq m)</label>
              <input type="number" id="pricePerSqFt" class="form-control" value="4.50" step="0.25" min="0">
            </div>
            <div class="form-group">
              <label for="thinsetBags">Thinset Bag Size (lb or kg)</label>
              <select id="thinsetBags" class="form-control">
                <option value="50" selected>50 lb Standard Dry Mortar Bag (~50 sq ft coverage)</option>
                <option value="25">25 lb Half-Size Mortar Bag (~25 sq ft coverage)</option>
                <option value="20">20 kg Metric Mortar Bag (~4.5 m² coverage)</option>
              </select>
            </div>
          </div>

          <button type="button" class="btn btn-primary" onclick="calcTileProject()">Calculate Tile, Grout &amp; Mortar</button>
        </div>

        <div id="tileResults" class="results-box" style="display:none;margin-top:1.5rem;">
          <h3 class="results-title">Tile &amp; Installation Material Breakdown</h3>
          <div class="result-grid">
            <div class="result-card">
              <div class="result-label">Net Surface Area</div>
              <div class="result-value" id="resNetArea">--</div>
              <div class="result-subtext" id="resGrossAreaSub">Gross: --</div>
            </div>
            <div class="result-card">
              <div class="result-label">Total Tile Area to Purchase</div>
              <div class="result-value highlight" id="resOrderArea">--</div>
              <div class="result-subtext" id="resWastageSub">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Total Tile Boxes (Cartons)</div>
              <div class="result-value highlight" id="resTotalBoxes">--</div>
              <div class="result-subtext" id="resTotalPieces">-- pieces</div>
            </div>
            <div class="result-card">
              <div class="result-label">Grout Requirement</div>
              <div class="result-value" id="resGroutWeight">--</div>
              <div class="result-subtext" id="resGroutBags">-- bags</div>
            </div>
          </div>

          <div class="result-details" style="margin-top:1rem;padding:1rem;background:var(--card-bg);border-radius:6px;border:1px solid var(--border-light);">
            <h4 style="margin-top:0;">Installation Material &amp; Cost Estimation</h4>
            <ul style="margin-bottom:0;line-height:1.7;">
              <li><strong>Thinset Mortar:</strong> <span id="resThinsetBags">--</span></li>
              <li><strong>Single Tile Surface Area:</strong> <span id="resSingleTileArea">--</span></li>
              <li><strong>Estimated Tile Material Cost:</strong> <span id="resTotalTileCost" style="font-weight:700;color:var(--primary);">--</span></li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Related Category Sidebar -->
      <aside class="post-sidebar">
        <div class="sidebar-widget">
          <div class="sidebar-widget-header">
            <span class="widget-icon">🏗️</span>
            <h3 class="widget-title">Related Civil Calculators</h3>
          </div>
          <p class="sidebar-widget-subtitle">Specialized calculation tools in this discipline:</p>
          <ul class="sidebar-links-list">
            <li><a href="flooring-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Flooring Area &amp; Box Estimator</a></li>
            <li><a href="drywall-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Drywall Sheets, Mud &amp; Tape</a></li>
            <li><a href="concrete-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Concrete Slab, Footing &amp; Column</a></li>
            <li><a href="paint-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Paint Gallon &amp; Coverage</a></li>
            <li><a href="brick-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Brick &amp; Masonry Calculator</a></li>
          </ul>
          <div style="margin-top:1.25rem;padding-top:1rem;border-top:1px solid var(--border-light);">
            <a href="civil.html" class="sidebar-category-link">View All Civil Calculators &rarr;</a>
          </div>
        </div>
      </aside>
    </div>

    <!-- Technical Educational Article Body (1000+ Words) -->
    <article class="article-body">
      <h2>Engineering Standards in Architectural Ceramic, Porcelain, and Stone Tiling</h2>
      <p>Precision tile installation requires rigorous planning that encompasses surface geometric modeling, structural substrate deflection criteria, thinset mortar bed transfer rates, and joint grout volume physics. The Tile Council of North America (TCNA Handbook for Ceramic, Glass, and Stone Tile Installation) and the American National Standards Institute (ANSI A108/A118/A136) specify exact technical thresholds to prevent debonding, tenting, grout joint cracking, and uneven lippage.</p>

      <p>Whether installing 3" &times; 6" subway tiles in a commercial food prep washroom or 24" &times; 48" rectified porcelain slabs across an expansive hotel atrium, accurate material procurement hinges on three intertwined calculations: net area minus structural fenestrations, pattern cut waste multipliers, and adhesive bed coverage governed by notch morphology.</p>

      <h2>Mathematical Formulation of Tile Piece and Carton Quantities</h2>
      <p>The foundational step determines the net substrate installation area ($A_{\text{net}}$):</p>

      <div class="formula-box">
        $$A_{\text{net}} = (L_{\text{room}} \times W_{\text{room}}) - \sum A_{\text{deductions}}$$
      </div>

      <p>Where $\sum A_{\text{deductions}}$ represents non-tiled areas such as prefabricated alcove shower receptors, floor-mounted cabinetry footprints, or doorway thresholds. To account for perimeter trimming, edge squaring, and unavoidable breakage during wet-saw cutting, an engineered waste factor ($W_{\%}$) is applied:</p>

      <div class="formula-box">
        $$A_{\text{gross}} = A_{\text{net}} \times \left(1 + \frac{W_{\%}}{100}\right)$$
      </div>

      <p>The area of an individual tile unit ($a_{\text{tile}}$) expressed in square feet is:</p>

      <div class="formula-box">
        $$a_{\text{tile}} = \frac{L_{\text{tile}} \, (\text{in}) \times W_{\text{tile}} \, (\text{in})}{144} \quad (\text{or } a_{\text{tile}} = \frac{L \, (\text{mm}) \times W \, (\text{mm})}{1,000,000} \text{ in metric m}^2)$$
      </div>

      <p>The raw tile count ($N_{\text{pieces}}$) and required commercial cartons ($N_{\text{boxes}}$) are calculated by rounding up to ensure full carton lots:</p>

      <div class="formula-box">
        $$N_{\text{pieces}} = \left\lceil \frac{A_{\text{gross}}}{a_{\text{tile}}} \right\rceil, \quad N_{\text{boxes}} = \left\lceil \frac{A_{\text{gross}}}{\text{Box Coverage (sq ft)}} \right\rceil$$
      </div>

      <h2>TCNA Grout Joint Volume Formula</h2>
      <p>Unlike simplistic surface approximations, the volume of cementitious or epoxy grout consumed across a tiled assembly depends directly on joint width ($J_w$), joint depth ($J_d$, equivalent to tile thickness), tile length ($L$), and tile width ($W$). The standardized TCNA gravimetric joint formula is expressed as:</p>

      <div class="formula-box">
        $$\text{Grout Weight (lbs)} = \frac{(L + W) \times J_w \times J_d \times \rho_{\text{grout}}}{L \times W} \times A_{\text{net}} \times 1.10$$
      </div>

      <p>Where $L, W, J_w,$ and $J_d$ are expressed in inches, $A_{\text{net}}$ is in square feet, and $\rho_{\text{grout}}$ represents the cured dry density of Portland cement grout ($\approx 105\text{ to }115\text{ lb/cu ft}$, or approximately $0.065\text{ lb/cu in}$). The $1.10$ multiplier incorporates a 10% safety allowance for float residue and wash bucket sponge loss.</p>

      <h2>Thinset Mortar Coverage and Trowel Notch Morphology</h2>
      <p>Polymer-modified dry-set mortar (ANSI A118.4 / A118.15) provides the mechanical bond between tile backing and concrete backer units or poured slabs. ANSI A108.5 mandates a minimum mortar contact coverage of 80% for dry interior spaces and 95% for exterior or wet shower enclosures. Achieving this coverage depends critically on trowel notch size:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Tile Dimension Category</th>
              <th>Recommended Trowel Notch</th>
              <th>Mortar Bed Thickness</th>
              <th>Average Coverage (50 lb Bag)</th>
              <th>ANSI A108 Coverage Requirement</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Mosaics (&le; 2" &times; 2")</td>
              <td>3/16" &times; 5/32" V-Notch</td>
              <td>3/32" (2.4 mm)</td>
              <td>90 &ndash; 105 sq ft</td>
              <td>80% Interior / 95% Wet</td>
            </tr>
            <tr>
              <td>Small Tiles (4" &times; 4" to 8" &times; 8")</td>
              <td>1/4" &times; 1/4" Square Notch</td>
              <td>1/8" (3.2 mm)</td>
              <td>80 &ndash; 90 sq ft</td>
              <td>80% Interior / 95% Wet</td>
            </tr>
            <tr>
              <td>Medium Format (8" &times; 8" to 12" &times; 12")</td>
              <td>1/4" &times; 3/8" Square Notch</td>
              <td>5/32" (4.0 mm)</td>
              <td>60 &ndash; 70 sq ft</td>
              <td>80% Interior / 95% Wet</td>
            </tr>
            <tr>
              <td>Large Format Tile (LFT &ge; 15" edge)</td>
              <td>1/2" &times; 1/2" Square Notch</td>
              <td>1/4" (6.4 mm)</td>
              <td>40 &ndash; 50 sq ft</td>
              <td>80% Interior / 95% Wet + Back-butter</td>
            </tr>
            <tr>
              <td>Heavy Gauged Porcelain / Paver Slabs</td>
              <td>3/4" Round Notch / Euro U-Notch</td>
              <td>5/16" (8.0 mm)</td>
              <td>30 &ndash; 40 sq ft</td>
              <td>95% Full Coverage + Back-butter</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Pattern Layout Waste Multipliers</h2>
      <p>The cutting waste percentage is directly correlated with tile aspect ratio and installation pattern geometry:</p>
      <ul>
        <li><strong>Standard Stacked or Grid Layout:</strong> Minimal cuts occurring primarily at room boundary perimeters. Waste factor: <strong>8% to 10%</strong>.</li>
        <li><strong>Running Bond / 1/3 Offset:</strong> Used universally for wood-look planks and 12" &times; 24" rectangular formats. Note: TCNA restricts 50% brick-joint offsets on large format tiles due to inherent center crown warpage (firing camber); a 33% maximum offset is required. Waste factor: <strong>12% to 14%</strong>.</li>
        <li><strong>Diagonal (45&deg; Angle):</strong> Every boundary edge requires a precision miter cut, generating triangular off-cuts that cannot always be reused. Waste factor: <strong>15% to 18%</strong>.</li>
        <li><strong>Herringbone &amp; Chevron:</strong> Complex multi-directional orientation with heavy diagonal cuts against perimeter borders. Waste factor: <strong>18% to 22%</strong>.</li>
      </ul>

      <h2>Practical Worked Case Study: Master Ensuite Wet Room</h2>
      <div class="worked-example-card">
        <h3>Design Example: 12" &times; 24" Porcelain Tile Bathroom Floor</h3>
        <p><strong>Project Parameters:</strong> A residential master bathroom floor measures 16 feet in length by 12 feet in width. A built-in soaking tub (6 ft &times; 3 ft) and a shower curb footprint occupy 22 square feet of deducted floor space. The owner selects 12" &times; 24" rectified porcelain tiles installed in a 1/3 offset pattern with 1/8" grout joints. Tiles are packaged in cartons containing 16.0 square feet (8 tiles per box) at $5.20/sq ft. ANSI A118.4 polymer-modified thinset is supplied in 50 lb bags, and sanded grout is packaged in 25 lb bags.</p>

        <p><strong>Step 1: Calculate Net and Gross Tiled Surface Area:</strong></p>
        $$A_{\text{gross floor}} = 16\text{ ft} \times 12\text{ ft} = 192\text{ sq ft}$$
        $$A_{\text{net}} = 192\text{ sq ft} - 22\text{ sq ft} = 170\text{ sq ft}$$
        <p>Applying a 12% pattern waste allowance for the 1/3 offset running bond:</p>
        $$A_{\text{order}} = 170\text{ sq ft} \times 1.12 = 190.4\text{ sq ft}$$

        <p><strong>Step 2: Determine Tile Pieces and Carton Boxes:</strong></p>
        <p>Area per tile: $a_{\text{tile}} = \frac{12 \times 24}{144} = 2.0\text{ sq ft}$.</p>
        $$N_{\text{pieces}} = \left\lceil \frac{190.4}{2.0} \right\rceil = \lceil 95.2 \rceil = 96\text{ tiles}$$
        <p>Total Cartons Required:</p>
        $$N_{\text{boxes}} = \left\lceil \frac{190.4\text{ sq ft}}{16.0\text{ sq ft/box}} \right\rceil = \lceil 11.9 \rceil = 12\text{ boxes (providing 192.0 sq ft)}$$

        <p><strong>Step 3: Calculate TCNA Joint Grout Requirement:</strong></p>
        <p>Parameters: $L = 24", W = 12", J_w = 0.125", J_d = 0.375"$, grout density factor $\approx 0.065\text{ lb/cu in}$, $A_{\text{net}} = 170\text{ sq ft}$:</p>
        $$\text{Grout Weight} = \frac{(24 + 12) \times 0.125 \times 0.375 \times 0.065}{24 \times 12} \times 170 \times 1.10$$
        $$\text{Grout Weight} = \frac{36 \times 0.003047}{288} \times 170 \times 1.10 = \frac{0.1097}{288} \times 187 = 0.000381 \times 187 \approx 13.8\text{ lbs}$$
        <p>Order: <strong>One 25 lb bag of grout</strong> (provides ample material for float packing and future tile maintenance).</p>

        <p><strong>Step 4: Compute Thinset Adhesive Bags:</strong></p>
        <p>Large format 12" &times; 24" tiles require a 1/2" &times; 1/2" square-notch trowel with back-buttering, yielding roughly 45 sq ft of coverage per 50 lb mortar bag:</p>
        $$N_{\text{thinset}} = \left\lceil \frac{170\text{ sq ft}}{45\text{ sq ft/bag}} \right\rceil = \lceil 3.78 \rceil = 4\text{ bags (50 lb each)}$$

        <p><strong>Step 5: Total Estimated Material Expenditure:</strong></p>
        $$\text{Tile Cost} = 12\text{ boxes} \times 16\text{ sq ft/box} \times \$5.20/\text{sq ft} = 192\text{ sq ft} \times \$5.20 = \$998.40$$
      </div>

      <h2>Deflection and Expansion Joint Engineering</h2>
      <p>Before installing ceramic or stone tile, the underlying structural floor assembly must be verified for deflection compliance:</p>
      <ul>
        <li><strong>L/360 Deflection Standard (Ceramic &amp; Porcelain):</strong> Under total design service load (dead load plus live load), the maximum allowable subfloor deflection cannot exceed $L/360$, where $L$ is the clear span of the floor joists. For a 15-foot joist span, maximum deflection is $180\text{ in} / 360 = 0.50\text{ inches}$.</li>
        <li><strong>L/720 Deflection Standard (Natural Stone):</strong> Dimension stone tiles (granite, marble, travertine, limestone) are brittle and have zero flexural ductility. Substrates must achieve twice the rigidity ($L/720$), requiring thicker double-layer plywood subflooring or uncoupling membranes.</li>
        <li><strong>Perimeter Movement Joints (EJ171):</strong> Per TCNA Method EJ171, tile installations must never abut rigid walls, columns, or curbed perimeters tightly. Leave an open 1/4-inch perimeter expansion gap covered by baseboards or filled with 100% silicone movement sealant to accommodate seasonal thermal expansion and framing creep.</li>
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
          <p class="footer-about">High-precision engineering and construction calculation tools conforming to TCNA, ANSI, and ASTM specifications.</p>
        </div>
        <div class="footer-col">
          <h4 class="footer-title">Engineering Disciplines</h4>
          <ul class="footer-links">
            <li><a href="civil.html">Civil &amp; Construction</a></li>
            <li><a href="mechanical.html">Mechanical &amp; HVAC</a></li>
            <li><a href="engineering.html">Electrical &amp; Electronics</a></li>
            <li><a href="chemical.html">Chemical &amp; Water Treatment</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4 class="footer-title">Standard References</h4>
          <ul class="footer-links">
            <li><a href="https://www.tcnatile.com" target="_blank" rel="noopener">Tile Council of North America (TCNA)</a></li>
            <li><a href="https://www.ansi.org" target="_blank" rel="noopener">ANSI A108 / A118 Standards</a></li>
            <li><a href="https://www.ntca.org" target="_blank" rel="noopener">National Tile Contractors Assoc.</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    const TILE_PRESETS = {
      "12x24": { l_in: 24, w_in: 12, th_in: 0.375, l_mm: 600, w_mm: 300, th_mm: 9.5, box_imp: 16, box_met: 1.44 },
      "12x12": { l_in: 12, w_in: 12, th_in: 0.3125, l_mm: 300, w_mm: 300, th_mm: 8.0, box_imp: 15, box_met: 1.39 },
      "24x24": { l_in: 24, w_in: 24, th_in: 0.375, l_mm: 600, w_mm: 600, th_mm: 9.5, box_imp: 16, box_met: 1.44 },
      "6x24": { l_in: 24, w_in: 6, th_in: 0.375, l_mm: 600, w_mm: 150, th_mm: 9.5, box_imp: 12, box_met: 1.11 },
      "3x6": { l_in: 6, w_in: 3, th_in: 0.25, l_mm: 150, w_mm: 75, th_mm: 6.35, box_imp: 10, box_met: 0.93 },
      "4x4": { l_in: 4, w_in: 4, th_in: 0.25, l_mm: 100, w_mm: 100, th_mm: 6.35, box_imp: 10, box_met: 0.93 },
      "hex_2": { l_in: 12, w_in: 12, th_in: 0.25, l_mm: 300, w_mm: 300, th_mm: 6.35, box_imp: 10, box_met: 0.93 },
      "custom": { l_in: 24, w_in: 12, th_in: 0.375, l_mm: 600, w_mm: 300, th_mm: 9.5, box_imp: 16, box_met: 1.44 }
    };

    function updateTilePreset() {
      const val = document.getElementById("tilePreset").value;
      const isMetric = document.getElementById("tileUnit").value === "metric";
      if (val !== "custom") {
        const p = TILE_PRESETS[val];
        if (!isMetric) {
          document.getElementById("tileLength").value = p.l_in;
          document.getElementById("tileWidth").value = p.w_in;
          document.getElementById("tileThickness").value = p.th_in;
          document.getElementById("boxCoverage").value = p.box_imp;
        } else {
          document.getElementById("tileLength").value = p.l_mm;
          document.getElementById("tileWidth").value = p.w_mm;
          document.getElementById("tileThickness").value = p.th_mm;
          document.getElementById("boxCoverage").value = p.box_met;
        }
      }
    }

    function toggleTileUnits() {
      const isMetric = document.getElementById("tileUnit").value === "metric";
      document.getElementById("tileLengthLabel").textContent = isMetric ? "Tile Length (mm)" : "Tile Length (inches)";
      document.getElementById("tileWidthLabel").textContent = isMetric ? "Tile Width (mm)" : "Tile Width (inches)";
      document.getElementById("thicknessLabel").textContent = isMetric ? "Tile Thickness (mm)" : "Tile Thickness (inches)";
      document.getElementById("roomLengthLabel").textContent = isMetric ? "Room / Wall Length (m)" : "Room / Wall Length (ft)";
      document.getElementById("roomWidthLabel").textContent = isMetric ? "Room / Wall Width or Height (m)" : "Room / Wall Width or Height (ft)";
      document.getElementById("deductAreaLabel").textContent = isMetric ? "Area Deductions (Doors, Tubs) (sq m)" : "Area Deductions (Doors, Tubs) (sq ft)";
      document.getElementById("boxCoverageLabel").textContent = isMetric ? "Square Meters per Carton Box" : "Square Feet per Carton Box";
      updateTilePreset();
    }

    function calcTileProject() {
      const isMetric = document.getElementById("tileUnit").value === "metric";
      const roomL = parseFloat(document.getElementById("roomLength").value) || 0;
      const roomW = parseFloat(document.getElementById("roomWidth").value) || 0;
      const deduct = parseFloat(document.getElementById("deductArea").value) || 0;
      const wastePct = parseFloat(document.getElementById("layoutPattern").value) || 10;
      const boxCov = parseFloat(document.getElementById("boxCoverage").value) || 16;
      const pricePerSq = parseFloat(document.getElementById("pricePerSqFt").value) || 0;

      let tileL = parseFloat(document.getElementById("tileLength").value) || 12;
      let tileW = parseFloat(document.getElementById("tileWidth").value) || 12;
      let tileTh = parseFloat(document.getElementById("tileThickness").value) || 0.375;
      let jointW = parseFloat(document.getElementById("groutJoint").value) || 0.125;

      if (roomL <= 0 || roomW <= 0 || tileL <= 0 || tileW <= 0) {
        alert("Please enter positive dimensions for room and tile.");
        return;
      }

      const grossRoomArea = roomL * roomW;
      const netArea = Math.max(0, grossRoomArea - deduct);
      const grossOrderArea = netArea * (1 + wastePct / 100);

      // Single tile area
      let singleTileArea = 0; // sq ft or sq m
      let singleTileAreaAlt = "";
      if (!isMetric) {
        singleTileArea = (tileL * tileW) / 144;
        singleTileAreaAlt = (singleTileArea * 0.092903).toFixed(3) + " m²";
      } else {
        singleTileArea = (tileL * tileW) / 1000000;
        singleTileAreaAlt = (singleTileArea * 10.7639).toFixed(3) + " sq ft";
      }

      const totalPieces = Math.ceil(grossOrderArea / singleTileArea);
      const totalBoxes = Math.ceil(grossOrderArea / boxCov);
      const totalTileCost = totalBoxes * boxCov * pricePerSq;

      // TCNA Grout Calculation
      // (L + W) * Jw * Th * 0.065 / (L * W) * Area * 1.10
      let groutL_in = isMetric ? tileL / 25.4 : tileL;
      let groutW_in = isMetric ? tileW / 25.4 : tileW;
      let groutTh_in = isMetric ? tileTh / 25.4 : tileTh;
      let groutArea_sqft = isMetric ? netArea * 10.7639 : netArea;

      let groutWeightLbs = ((groutL_in + groutW_in) * jointW * groutTh_in * 0.065) / (groutL_in * groutW_in) * groutArea_sqft * 1.10;
      let groutWeightKg = groutWeightLbs * 0.453592;

      // Thinset: Large format >= 15" needs 1/2" notch (45 sqft/50lb bag), else 1/4" notch (75 sqft/50lb bag)
      const maxDimInches = isMetric ? Math.max(tileL, tileW) / 25.4 : Math.max(tileL, tileW);
      const coveragePerBag = maxDimInches >= 14 ? 45 : 75; // sq ft
      const areaForThinsetSqFt = isMetric ? netArea * 10.7639 : netArea;
      const thinsetBagsCount = Math.ceil(areaForThinsetSqFt / coveragePerBag);

      // Populate results
      document.getElementById("resNetArea").textContent = netArea.toFixed(1) + (isMetric ? " m²" : " sq ft");
      document.getElementById("resGrossAreaSub").textContent = "Gross room: " + grossRoomArea.toFixed(1) + (isMetric ? " m²" : " sq ft");
      document.getElementById("resOrderArea").textContent = grossOrderArea.toFixed(1) + (isMetric ? " m²" : " sq ft");
      document.getElementById("resWastageSub").textContent = "Includes +" + wastePct + "% cut & layout waste";

      document.getElementById("resTotalBoxes").textContent = totalBoxes + " Boxes";
      document.getElementById("resTotalPieces").textContent = totalPieces + " total tiles";

      if (!isMetric) {
        document.getElementById("resGroutWeight").textContent = groutWeightLbs.toFixed(1) + " lbs";
        document.getElementById("resGroutBags").textContent = Math.ceil(groutWeightLbs / 25) + " x 25-lb bags (or " + Math.ceil(groutWeightLbs / 10) + " x 10-lb)";
      } else {
        document.getElementById("resGroutWeight").textContent = groutWeightKg.toFixed(1) + " kg";
        document.getElementById("resGroutBags").textContent = Math.ceil(groutWeightKg / 10) + " x 10-kg bags (or " + Math.ceil(groutWeightKg / 5) + " x 5-kg)";
      }

      document.getElementById("resThinsetBags").textContent = thinsetBagsCount + " bags (50-lb / 22.7 kg) (" + (maxDimInches >= 14 ? "1/2\" LFT notch" : "1/4\" notch") + ")";
      document.getElementById("resSingleTileArea").textContent = singleTileArea.toFixed(3) + (isMetric ? " m² (" : " sq ft (") + singleTileAreaAlt + ")";
      document.getElementById("resTotalTileCost").textContent = "$" + totalTileCost.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});

      document.getElementById("tileResults").style.display = "block";
    }
  </script>
</body>
</html>
"""

def generate():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p1 = os.path.join(root, "soil-gravel-calculator.html")
    p2 = os.path.join(root, "tile-calculator.html")
    
    with open(p1, "w", encoding="utf-8") as f:
        f.write(TOOL_1_HTML.strip() + "\n")
    print(f"Generated {p1}")

    with open(p2, "w", encoding="utf-8") as f:
        f.write(TOOL_2_HTML.strip() + "\n")
    print(f"Generated {p2}")

if __name__ == "__main__":
    generate()
