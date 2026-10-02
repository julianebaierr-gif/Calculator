# -*- coding: utf-8 -*-
"""
Script to generate Batch 13 Part 4 tools:
7. slab-concrete-calculator.html
8. slope-calculator.html
"""
import os

TOOL_7_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Slab Concrete Calculator | Volume, Rebar &amp; Mix Bags</title>
  <meta name="description" content="Calculate concrete slab volume in cubic meters and cubic yards, thickened edge footings, ready-mix truckloads, and control joint spacing per ACI 360R.">
  <link rel="canonical" href="https://calchub.cloud/slab-concrete-calculator.html">
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
        "name": "Slab Concrete Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates concrete slab-on-grade volume, thickened edge perimeter footings, ready-mix truck deliveries, and ACI 360R control joint spacing.",
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
            "name": "What is the recommended concrete slab thickness for residential driveways and garages?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For standard residential vehicle parking, a 4-inch (100 mm) thick slab-on-grade of 25 MPa (3,500 psi) concrete with welded wire mesh is standard. For heavy pickup trucks, RV pads, or commercial workshops, a 5 to 6-inch (125 to 150 mm) slab reinforced with #4 (12 mm) rebar grid is required."
            }
          },
          {
            "@type": "Question",
            "name": "How is the volume of a slab with thickened edges calculated?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Calculate the primary slab volume as V_slab = Length × Width × Slab Thickness. Next, calculate the perimeter thickened footing trench volume as V_edge = Perimeter × (Edge Width × Extra Trench Depth). Total volume is V_total = V_slab + V_edge, plus a 5% to 10% subgrade irregularity allowance."
            }
          },
          {
            "@type": "Question",
            "name": "What is the maximum recommended contraction joint spacing per ACI 360R?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Per ACI 360R (Guide to Design of Slabs-on-Ground), contraction saw-cut joint spacing in feet should not exceed 2 to 2.5 times the slab thickness in inches (or 24 to 30 times thickness in metric units). For example, a 4-inch slab requires joint spacing between 8 and 10 feet (2.4 to 3.0 meters)."
            }
          },
          {
            "@type": "Question",
            "name": "How many 50 kg bags of cement are needed for a concrete slab?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For a standard Grade M20 (1:1.5:3) residential slab, approximately 8 to 8.5 bags of 50-kg cement are required per cubic meter of compacted concrete, based on the 1.54 dry materials expansion factor."
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
      <span>Slab Concrete Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calculator-main">
        <div class="calc-header">
          <h1>Slab Concrete Calculator</h1>
          <p>Compute concrete volume (m³ &amp; yd³), ready-mix truckloads, thickened edge footings, and ACI 360R control joint layouts.</p>
        </div>

        <div class="calculator-card">
          <form id="slabForm" onsubmit="return false;">
            <div class="form-row">
              <div class="form-group">
                <label for="slabLength">Slab Length (meters):</label>
                <input type="number" id="slabLength" value="10.0" step="0.25" min="0.5" required>
                <span class="hint">Long dimension of formwork</span>
              </div>
              <div class="form-group">
                <label for="slabWidth">Slab Width (meters):</label>
                <input type="number" id="slabWidth" value="6.0" step="0.25" min="0.5" required>
                <span class="hint">Short dimension of formwork</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="slabThicknessMm">Slab Thickness (mm):</label>
                <input type="number" id="slabThicknessMm" value="125" step="5" min="50" max="500" required>
                <span class="hint">100 mm (4"), 125 mm (5"), 150 mm (6")</span>
              </div>
              <div class="form-group">
                <label for="concreteGrade">Target Concrete Mix / Grade:</label>
                <select id="concreteGrade">
                  <option value="8.0" selected>Grade M20 (1:1.5:3) - Residential Driveway / Slab (~8.1 bags/m³)</option>
                  <option value="11.0">Grade M25 (1:1:2) - Heavy Commercial Slab (~11.1 bags/m³)</option>
                  <option value="6.3">Grade M15 (1:2:4) - Footpaths &amp; Patio Paving (~6.3 bags/m³)</option>
                </select>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="thickenedEdge">Include Thickened Perimeter Edge?</label>
                <select id="thickenedEdge">
                  <option value="no" selected>No (Uniform Thickness Slab)</option>
                  <option value="yes">Yes (Monolithic Perimeter Footing)</option>
                </select>
              </div>
              <div class="form-group">
                <label for="wasteMargin">Subgrade &amp; Spillage Allowance (%):</label>
                <input type="number" id="wasteMargin" value="8" step="1" min="0" max="20" required>
                <span class="hint">Recommended 5% to 10% for uneven subgrade</span>
              </div>
            </div>

            <!-- Thickened Edge Dimensions (Conditional) -->
            <div class="form-row" id="edgeDimRow" style="display:none;">
              <div class="form-group">
                <label for="edgeWidthMm">Edge Footing Width (mm):</label>
                <input type="number" id="edgeWidthMm" value="300" step="25" min="150">
                <span class="hint">Standard 300 mm (12")</span>
              </div>
              <div class="form-group">
                <label for="edgeExtraDepthMm">Extra Trench Depth (mm):</label>
                <input type="number" id="edgeExtraDepthMm" value="200" step="25" min="50">
                <span class="hint">Depth below bottom of main slab</span>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcSlabBtn">Calculate Slab Materials</button>
              <button type="reset" class="btn btn-secondary" id="resetSlabBtn">Reset</button>
            </div>
          </form>

          <div class="results-box" id="slabResultBox" style="display:none; margin-top:25px;">
            <h3>Slab Concrete Takeoff &amp; Specifications</h3>
            <div class="result-grid">
              <div class="result-tile highlight">
                <span class="result-label">Total Concrete to Order</span>
                <span class="result-value" id="resTotalM3">0.00</span>
                <span class="result-unit">m³ (~0.0 cu yd)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Ready-Mix Truck Deliveries</span>
                <span class="result-value" id="resTrucks">0</span>
                <span class="result-unit">Truckloads (8 m³ trucks)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Cement Quantity (50 kg Bags)</span>
                <span class="result-value" id="resCementBags">0</span>
                <span class="result-unit">Bags (for on-site batching)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Net Surface Area</span>
                <span class="result-value" id="resSlabArea">0.0</span>
                <span class="result-unit">m² (~0 sq ft)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">ACI Max Joint Spacing</span>
                <span class="result-value" id="resJointSpacing">0.0 m</span>
                <span class="result-unit">Saw-Cut Control Grid</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Total Compacted Slab Mass</span>
                <span class="result-value" id="resTotalMass">0</span>
                <span class="result-unit">kg (~0.0 metric tons)</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Concrete Slab-on-Grade Engineering Fundamentals</h2>
          <p>
            Ground-supported concrete floor slabs—termed <strong>slabs-on-grade</strong>—represent the structural foundation interface for residential basements, attached garages, industrial manufacturing plants, and commercial retail warehouses. Unlike elevated suspended slabs that transfer floor gravity loads across intermediate structural beams to columns, slabs-on-ground transmit continuous uniform live and dead loads directly downward into the prepared sub-base and compacted soil subgrade.
          </p>
          <p>
            Under <strong>ACI 360R (Guide to Design of Slabs-on-Ground)</strong> and <strong>ACI 302.1R (Guide to Concrete Floor and Slab Construction)</strong>, structural performance depends upon subgrade uniform stiffness (characterized by the modulus of subgrade reaction $k$, in $\text{pci}$ or $\text{MPa/m}$), concrete flexural tensile strength (modulus of rupture $f_r = 0.62 \sqrt{f'_c}$), and control of concrete drying shrinkage cracking.
          </p>

          <h2>Volumetric Geometry: Flat Slabs &amp; Thickened Edge Beams</h2>
          <p>
            The net in-place volume ($V_{slab}$) of a uniform rectangular slab of length $L$, width $W$, and thickness $T$:
          </p>
          <div class="formula-box">
            $$V_{slab} = L \times W \times \left(\frac{T_{mm}}{1000}\right) \quad (L, W \text{ in meters, } T \text{ in mm})$$
          </div>
          <p>
            In monolithic residential construction, the slab perimeter is frequently cast with a <strong>thickened edge footing</strong> to support exterior timber or light-gauge steel loadbearing framing walls. For a perimeter run with footing width $b_{edge}$ and additional trench depth $d_{extra}$ below the main slab bottom:
          </p>
          <div class="formula-box">
            $$\text{Perimeter} = 2 \times (L + W)$$
            $$V_{edge} = \text{Perimeter} \times b_{edge} \times d_{extra}$$
            $$V_{gross} = (V_{slab} + V_{edge}) \times \left(1 + \frac{\text{Waste}_{\%}}{100}\right)$$
          </div>
          <p>
            Civil engineering specifications enforce a $5\%$ to $10\%$ waste factor to account for subgrade undulations, formwork lateral deflection under hydrostatic wet concrete pressure, and pump truck hopper residue.
          </p>

          <h2>Shrinkage, Curling &amp; ACI 360R Contraction Joint Spacing</h2>
          <p>
            As fresh concrete cures, hydration water is consumed and excess bleed water evaporates into ambient air, resulting in an irreversible drying shrinkage strain of approximately $0.04\%$ to $0.08\%$ ($400\text{ to }800\text{ }\mu\epsilon$). If the slab is restrained against free contraction by subgrade friction, internal tensile stresses rapidly exceed the low tensile capacity of young concrete, producing jagged, uncontrolled random surface cracking.
          </p>
          <p>
            To guide cracking into clean, concealed straight lines, <strong>contraction control joints</strong> must be saw-cut into the slab surface using an early-entry green concrete saw (within $4\text{ to }12\text{ hours}$ of finishing) to a minimum depth of:
          </p>
          <div class="formula-box">
            $$D_{joint} \ge \frac{T_{slab}}{4} \quad (\text{Minimum one-quarter of slab thickness})$$
          </div>
          <p>
            Per ACI 360R Section 6.5, maximum joint spacing ($S_{joint}$) is governed by slab thickness:
          </p>
          <div class="formula-box">
            $$S_{joint} \le 24 \times T_{slab} \quad \text{to} \quad 30 \times T_{slab}$$
            $$S_{joint\text{ (feet)}} \le (2.0 \text{ to } 2.5) \times T_{slab\text{ (inches)}}$$
          </div>
          <p>
            For a $125\text{ mm}$ ($5\text{-inch}$) slab, control joints should be spaced at intervals not exceeding $24 \times 125\text{ mm} = 3.0\text{ meters}$ ($10\text{ to }12.5\text{ feet}$). Aspect ratios of joint panels should remain as square as possible, never exceeding $1.5:1$ length-to-width.
          </p>

          <h2>Vapor Retarders &amp; Welded Wire Reinforcement (WWR)</h2>
          <p>
            Under <strong>ASTM E1745</strong>, interior conditioned slabs require a continuous high-performance polyolefin underslab vapor retarder (minimum $10\text{ to }15\text{ mil}$ thickness) placed directly on the compacted granular base to eliminate moisture vapor emissions that ruin floor adhesives and cause mold.
          </p>
          <p>
            Secondary crack-control reinforcement—such as welded wire reinforcement (WWR $6\times 6\text{ W1.4/W1.4}$ or synthetic macro-fibers at $3 - 5\text{ lb/yd}^3$)—does not prevent cracks from initiating. Rather, its sole structural function is to hold crack faces tightly together, preserving aggregate interlock across the joint.
          </p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Slab Application</th>
                <th>Typical Thickness</th>
                <th>Target 28-Day Strength ($f'_c$)</th>
                <th>Reinforcement Type</th>
                <th>Max Joint Spacing</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Pedestrian Sidewalk / Patio</td>
                <td>90 – 100 mm (3.5 – 4")</td>
                <td>20 MPa (3,000 psi)</td>
                <td>Synthetic micro-fibers</td>
                <td>2.0 – 2.5 m (6 – 8 ft)</td>
              </tr>
              <tr>
                <td>Residential Garage / Driveway</td>
                <td>100 – 125 mm (4 – 5")</td>
                <td>25 MPa (3,500 psi)</td>
                <td>WWR 6×6 W1.4/W1.4 or #3 rebar</td>
                <td>2.5 – 3.0 m (8 – 10 ft)</td>
              </tr>
              <tr>
                <td>Commercial Workshop / Retail</td>
                <td>125 – 150 mm (5 – 6")</td>
                <td>28 – 30 MPa (4,000 psi)</td>
                <td>#4 Rebar @ 18" (450 mm) oc grid</td>
                <td>3.0 – 3.7 m (10 – 12 ft)</td>
              </tr>
              <tr>
                <td>Heavy Industrial Warehouse</td>
                <td>175 – 250 mm (7 – 10")</td>
                <td>35 MPa (5,000 psi)</td>
                <td>Double mat #4 / #5 rebar grid</td>
                <td>4.0 – 4.5 m (13 – 15 ft)</td>
              </tr>
            </tbody>
          </table>

          <h2>Concrete Curing Protocols, Moisture Loss &amp; Compressive Strength Development (ACI 308R)</h2>
          <p>
            The structural durability and surface abrasion resistance of a concrete slab are largely governed by post-placement curing during the first 7 to 28 days. Under <strong>ACI 308R (Guide to External Curing of Concrete)</strong>, premature evaporation of surface moisture before Portland cement hydration is complete causes micro-cracking, plastic shrinkage crazing, and dusting of the surface paste layer.
          </p>
          <p>
            Effective curing methodologies include:
          </p>
          <ul>
            <li><strong>Liquid Membrane-Forming Curing Compounds (ASTM C309):</strong> Spray-applied acrylic resin or wax emulsions forming an impermeable film that restricts moisture loss to less than $0.55\text{ kg/m}^2$ over a $72\text{-hour}$ period.</li>
            <li><strong>Continuous Wet Burlap Curing (ASTM C171):</strong> Saturated cotton mats kept continuously damp for a minimum of 7 consecutive days, yielding maximum cement hydration and up to $30\%$ higher surface abrasion resistance.</li>
          </ul>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: Commercial Workshop Slab with Thickened Perimeter</h3>
            <p><strong>Design Scenario:</strong> An automotive repair workshop requires an engineered concrete floor slab-on-grade measuring $L = 12.0\text{ meters}$ in length by $W = 8.0\text{ meters}$ in width. To support vehicle hoists, the primary floor thickness is specified at $T = 150\text{ mm}$ ($0.15\text{ meters}$) using Grade M25 concrete ($f'_c = 25\text{ MPa}$). Around the entire perimeter, a monolithic thickened edge footing is designed: width $b = 350\text{ mm}$ ($0.35\text{ m}$) with an extra downward depth of $d_{extra} = 250\text{ mm}$ ($0.25\text{ m}$) below the slab base. A subgrade compaction waste allowance of $8\%$ is budgeted. Calculate net slab volume, edge footing volume, gross ready-mix concrete to order, ready-mix truckloads ($8.0\text{ m}^3$ capacity), and maximum ACI contraction joint cut spacing.</p>
            
            <p><strong>Step 1: Compute Primary Flat Slab Volume ($V_{slab}$)</strong></p>
            <div class="formula-box">
              $$A_{surface} = 12.0\text{ m} \times 8.0\text{ m} = 96.0\text{ m}^2 \quad (\approx 1,033.3\text{ sq ft})$$
              $$V_{slab} = 96.0\text{ m}^2 \times 0.15\text{ m} = \mathbf{14.40\text{ m}^3}$$
            </div>

            <p><strong>Step 2: Calculate Perimeter Thickened Edge Volume ($V_{edge}$)</strong></p>
            <div class="formula-box">
              $$\text{Perimeter} = 2 \times (12.0\text{ m} + 8.0\text{ m}) = 40.0\text{ linear meters}$$
              $$V_{edge} = 40.0\text{ m} \times 0.35\text{ m} \times 0.25\text{ m} = \mathbf{3.50\text{ m}^3}$$
            </div>

            <p><strong>Step 3: Determine Gross Volume with 8% Waste Allowance</strong></p>
            <div class="formula-box">
              $$V_{net} = V_{slab} + V_{edge} = 14.40\text{ m}^3 + 3.50\text{ m}^3 = 17.90\text{ m}^3$$
              $$V_{gross} = 17.90\text{ m}^3 \times (1 + 0.08) = 17.90 \times 1.08 = \mathbf{19.33\text{ m}^3} \quad (\approx 25.28\text{ cu yd})$$
            </div>

            <p><strong>Step 4: Dispatch Logistics and ACI Joint Spacing</strong></p>
            <div class="formula-box">
              $$N_{trucks} = \left\lceil \frac{19.33\text{ m}^3}{8.0\text{ m}^3/\text{truck}} \right\rceil = \lceil 2.42 \rceil = \mathbf{3\text{ Ready-Mix Truckloads}}$$
              $$S_{joint} \le 24 \times T_{slab} = 24 \times 0.15\text{ m} = \mathbf{3.60\text{ meters maximum}}$$
            </div>
            <p>
              Dividing the $12.0\text{ m} \times 8.0\text{ m}$ slab into a $4 \times 3$ panel grid yields 12 panels measuring $3.0\text{ m} \times 2.67\text{ m}$ each, perfectly satisfying the $3.6\text{ m}$ spacing limit and aspect ratio rules.
            </p>
            <p>
              <strong>Procurement Summary:</strong> Order <strong>$19.5\text{ m}^3$ of readymix concrete</strong> (delivered across 3 truckloads) and lay out control joints on a <strong>$3.0\text{ m} \times 2.67\text{ m}$ grid</strong>.
            </p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Civil &amp; Concrete Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="concrete-calculator.html">Concrete Volume Calculator</a></li>
            <li><a href="concrete-mix-ratio-calculator.html">Concrete Mix Ratio Proportions</a></li>
            <li><a href="rebar-weight-calculator.html">Rebar Weight Estimator</a></li>
            <li><a href="footing-size-calculator.html">Footing Size &amp; Soil Bearing</a></li>
            <li><a href="gravel-calculator.html">Gravel &amp; Aggregate Base</a></li>
          </ul>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container footer-content">
      <div class="footer-col">
        <h4>CalcHub</h4>
        <p>High-precision professional engineering and scientific calculation engines.</p>
      </div>
      <div class="footer-col">
        <h4>Directories</h4>
        <ul class="footer-links">
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="civil.html">Civil &amp; Construction</a></li>
          <li><a href="mechanical.html">Mechanical Engineering</a></li>
          <li><a href="engineering.html">Civil &amp; Structural</a></li>
          <li><a href="sitemap.xml">XML Sitemap</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom text-center">
      <p>&copy; 2026 CalcHub. Standard Engineering Reference Systems.</p>
    </div>
  </footer>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const calcBtn = document.getElementById('calcSlabBtn');
      const resetBtn = document.getElementById('resetSlabBtn');
      const resultBox = document.getElementById('slabResultBox');
      const edgeSelect = document.getElementById('thickenedEdge');
      const edgeRow = document.getElementById('edgeDimRow');

      edgeSelect.addEventListener('change', function() {
        edgeRow.style.display = (this.value === 'yes') ? 'flex' : 'none';
      });

      function calculateSlab() {
        const L = parseFloat(document.getElementById('slabLength').value);
        const W = parseFloat(document.getElementById('slabWidth').value);
        const thickMm = parseFloat(document.getElementById('slabThicknessMm').value);
        const bagsPerM3 = parseFloat(document.getElementById('concreteGrade').value);
        const hasEdge = (edgeSelect.value === 'yes');
        const wastePct = parseFloat(document.getElementById('wasteMargin').value) || 0;

        if (isNaN(L) || L <= 0 || isNaN(W) || W <= 0 || isNaN(thickMm) || thickMm <= 0) {
          alert('Please enter valid positive dimensions for length, width, and thickness.');
          return;
        }

        const surfaceArea = L * W;
        const thickM = thickMm / 1000.0;
        let slabVol = surfaceArea * thickM;

        let edgeVol = 0.0;
        if (hasEdge) {
          const edgeWidthM = parseFloat(document.getElementById('edgeWidthMm').value) / 1000.0;
          const edgeDepthM = parseFloat(document.getElementById('edgeExtraDepthMm').value) / 1000.0;
          const perimeter = 2.0 * (L + W);
          edgeVol = perimeter * edgeWidthM * edgeDepthM;
        }

        const netVolM3 = slabVol + edgeVol;
        const grossVolM3 = netVolM3 * (1.0 + wastePct / 100.0);
        const grossCuYd = grossVolM3 * 1.30795;
        const trucks = Math.ceil(grossVolM3 / 8.0); // 8 m3 per transit mixer truck
        const cementBags = Math.ceil(grossVolM3 * bagsPerM3);

        // ACI 360R max joint spacing: 24 to 30 * thickness
        const maxJointSpacingM = (thickM * 24.0).toFixed(1);
        const totalMassKg = Math.round(grossVolM3 * 2400.0); // standard concrete density ~2400 kg/m3
        const totalMassTonnes = (totalMassKg / 1000.0).toFixed(1);
        const surfaceSqFt = (surfaceArea * 10.7639).toFixed(0);

        document.getElementById('resTotalM3').textContent = grossVolM3.toFixed(2) + ` (~${grossCuYd.toFixed(1)} yd³)`;
        document.getElementById('resTrucks').textContent = trucks.toLocaleString();
        document.getElementById('resCementBags').textContent = cementBags.toLocaleString();
        document.getElementById('resSlabArea').textContent = surfaceArea.toFixed(1) + ` (~${surfaceSqFt} ft²)`;
        document.getElementById('resJointSpacing').textContent = maxJointSpacingM + ' meters';
        document.getElementById('resTotalMass').textContent = totalMassKg.toLocaleString() + ` (~${totalMassTonnes} tonnes)`;

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculateSlab);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
        edgeSelect.value = 'no';
        edgeRow.style.display = 'none';
      });
      calculateSlab();
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
  <title>Slope Calculator | Incline Grade, Angle, Rise &amp; Run Sizer</title>
  <meta name="description" content="Calculate terrain slope gradient (m), percentage grade (%), incline angle in degrees, 1:X ratio, and ADA ramp accessibility standards per ADAAG 405.">
  <link rel="canonical" href="https://calchub.cloud/slope-calculator.html">
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
        "name": "Slope Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates civil gradient slope, elevation percentage grade, incline angle in degrees, and ADA wheelchair ramp compliance.",
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
            "name": "What is the formula to calculate slope?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Slope (m) is the ratio of vertical change (rise) to horizontal change (run): m = Rise / Run = (y2 - y1) / (x2 - x1). Incline angle is theta = arctan(m), and percentage grade is Grade (%) = m * 100."
            }
          },
          {
            "@type": "Question",
            "name": "What is the ADA compliant slope requirement for wheelchair ramps?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Under the Americans with Disabilities Act Accessibility Guidelines (ADAAG Section 405), the maximum allowable slope for a wheelchair ramp is 1:12 (1 unit of vertical rise per 12 units of horizontal run, or 8.33% grade / 4.76 degrees)."
            }
          },
          {
            "@type": "Question",
            "name": "How do you convert percentage grade to degrees?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Divide the percentage grade by 100 to get decimal slope, then take the arctangent: Angle (degrees) = arctan(Grade / 100) * (180 / π). For example, a 10% grade equals: arctan(0.10) ≈ 5.71 degrees."
            }
          },
          {
            "@type": "Question",
            "name": "What is the minimum slope required for civil site drainage?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Under International Building Code (IBC Section 1804.4), ground immediately adjacent to building foundations must slope away at not less than 5% (1 unit vertical in 20 units horizontal) for a minimum distance of 10 feet (3.05 m) to prevent foundation water damage."
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
      <span>Slope Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calculator-main">
        <div class="calc-header">
          <h1>Slope Calculator</h1>
          <p>Compute terrain gradient, percentage grade (%), incline angle in degrees, and verify ADA accessibility compliance.</p>
        </div>

        <div class="calculator-card">
          <form id="slopeForm" onsubmit="return false;">
            <div class="form-row">
              <div class="form-group">
                <label for="slopeMode">Input Calculation Mode:</label>
                <select id="slopeMode">
                  <option value="riseRun" selected>Vertical Rise &amp; Horizontal Run</option>
                  <option value="twoPoints">Two Coordinates (x1, y1) &amp; (x2, y2)</option>
                  <option value="gradePct">Percentage Grade (%)</option>
                  <option value="angleDeg">Incline Angle (Degrees)</option>
                </select>
              </div>
            </div>

            <!-- Rise & Run Inputs -->
            <div class="form-row" id="rowRiseRun">
              <div class="form-group">
                <label for="vertRise">Vertical Elevation Change (Rise, &Delta;y):</label>
                <input type="number" id="vertRise" value="1.5" step="0.1" required>
                <span class="hint">Height gained or lost</span>
              </div>
              <div class="form-group">
                <label for="horizRun">Horizontal Distance (Run, &Delta;x):</label>
                <input type="number" id="horizRun" value="25.0" step="0.5" min="0.001" required>
                <span class="hint">Horizontal baseline distance</span>
              </div>
            </div>

            <!-- Coordinates Inputs -->
            <div class="form-row" id="rowCoords" style="display:none;">
              <div class="form-group">
                <label for="coordX1">Point 1 (x₁, y₁):</label>
                <div style="display:flex; gap:0.5rem;">
                  <input type="number" id="coordX1" value="0.0" step="0.5" placeholder="x1">
                  <input type="number" id="coordY1" value="0.0" step="0.5" placeholder="y1">
                </div>
              </div>
              <div class="form-group">
                <label for="coordX2">Point 2 (x₂, y₂):</label>
                <div style="display:flex; gap:0.5rem;">
                  <input type="number" id="coordX2" value="30.0" step="0.5" placeholder="x2">
                  <input type="number" id="coordY2" value="2.4" step="0.5" placeholder="y2">
                </div>
              </div>
            </div>

            <!-- Percentage Grade Input -->
            <div class="form-row" id="rowGrade" style="display:none;">
              <div class="form-group">
                <label for="inputGrade">Grade Percentage (%):</label>
                <input type="number" id="inputGrade" value="6.0" step="0.1">
              </div>
              <div class="form-group">
                <label for="distGrade">Horizontal Run Distance:</label>
                <input type="number" id="distGrade" value="50.0" step="1.0" min="0.1">
              </div>
            </div>

            <!-- Angle Input -->
            <div class="form-row" id="rowAngle" style="display:none;">
              <div class="form-group">
                <label for="inputAngle">Slope Angle (Degrees):</label>
                <input type="number" id="inputAngle" value="5.0" step="0.1" min="0" max="89.9">
              </div>
              <div class="form-group">
                <label for="distAngle">Horizontal Run Distance:</label>
                <input type="number" id="distAngle" value="50.0" step="1.0" min="0.1">
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcSlopeBtn">Calculate Slope Parameters</button>
              <button type="reset" class="btn btn-secondary" id="resetSlopeBtn">Reset</button>
            </div>
          </form>

          <div class="results-box" id="slopeResultBox" style="display:none; margin-top:25px;">
            <h3>Terrain &amp; Engineering Gradient Properties</h3>
            <div class="result-grid">
              <div class="result-tile highlight">
                <span class="result-label">Percentage Grade (%)</span>
                <span class="result-value" id="resGradePct">0.00%</span>
                <span class="result-unit">Vertical Rise per 100 Units</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Slope Angle (&theta;)</span>
                <span class="result-value" id="resAngleDeg">0.00°</span>
                <span class="result-unit">Degrees from Horizontal</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Gradient Ratio (1 : X)</span>
                <span class="result-value" id="resRatio">1 : 0.0</span>
                <span class="result-unit">Standard Civil Ratio</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Decimal Gradient (m)</span>
                <span class="result-value" id="resDecimalM">0.0000</span>
                <span class="result-unit">Rise / Run tangent</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Hypotenuse Slope Distance</span>
                <span class="result-value" id="resHypotenuse">0.00</span>
                <span class="result-unit">True Surface Distance</span>
              </div>
              <div class="result-tile">
                <span class="result-label">ADA Accessibility Compliance</span>
                <span class="result-value" id="resAdaStatus">Compliant</span>
                <span class="result-unit">ADAAG 405 (Max 8.33%)</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Slope Kinematics, Civil Gradients &amp; Topographic Surveying</h2>
          <p>
            Slope describes the direction and steepness of an inclined ground surface or geometric line. In civil site grading, transportation highway alignment, hydraulic stormwater channel design, and architectural accessibility engineering, precise slope evaluation governs earthwork cut-and-fill stability, gravity water drainage, and public safety.
          </p>
          <p>
            In analytical mathematics and Cartesian coordinate surveying, the gradient slope ($m$) between two spatial points $(x_1, y_1)$ and $(x_2, y_2)$ is defined as the ratio of vertical altitude displacement ($\Delta y$) to horizontal baseline station distance ($\Delta x$):
          </p>
          <div class="formula-box">
            $$m = \frac{\text{Rise}}{\text{Run}} = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}$$
          </div>

          <h2>Conversions: Percentage Grade, Degrees, Radians &amp; Ratios</h2>
          <p>
            Depending upon the engineering discipline, slope is represented in four standard mathematical formats:
          </p>
          <ul>
            <li><strong>Percentage Grade ($\%$):</strong> The standard civil highway and pipeline metric. It expresses vertical elevation gain per $100$ units of horizontal distance:
              <div class="formula-box">$$\text{Grade } (\%) = m \times 100 = \left(\frac{\text{Rise}}{\text{Run}}\right) \times 100$$</div>
            </li>
            <li><strong>Angle of Incline ($\theta$):</strong> The trigonometric angle between the ground surface plane and the horizontal datum:
              <div class="formula-box">$$\theta = \arctan(m) \times \left(\frac{180}{\pi}\right)$$</div>
            </li>
            <li><strong>Proportional Ratio ($1:X$ or $X:1$):</strong> In architectural ramp codes and geotechnical embankment slope stability, gradient is formatted as $1\text{ unit vertical to } X\text{ units horizontal}$:
              <div class="formula-box">$$\text{Ratio } 1:X \implies X = \frac{\text{Run}}{\text{Rise}} = \frac{1}{m}$$</div>
            </li>
            <li><strong>True Slope Distance (Hypotenuse):</strong> The physical walking distance along the inclined terrain:
              <div class="formula-box">$$D_{slope} = \sqrt{\Delta x^2 + \Delta y^2} = \text{Run} \times \sqrt{1 + m^2} = \frac{\text{Run}}{\cos \theta}$$</div>
            </li>
          </ul>

          <h2>ADA Wheelchair Ramp Standards (ADAAG Section 405)</h2>
          <p>
            Civil infrastructure accessible to persons with physical disabilities must comply with the <strong>Americans with Disabilities Act Accessibility Guidelines (ADAAG Section 405)</strong>. Federal standards dictate strict slope limits:
          </p>
          <ul>
            <li><strong>Maximum Ramp Slope:</strong> $1:12$ ($8.33\%$ grade or $4.76^\circ$). Every inch of vertical rise requires at least $12\text{ inches}$ ($1\text{ foot}$) of ramp run.</li>
            <li><strong>Maximum Single Run Rise:</strong> $30\text{ inches}$ ($760\text{ mm}$). Any ramp with a total rise exceeding $30\text{ inches}$ must incorporate an intermediate level resting landing (minimum $60\text{ inches} \times 60\text{ inches}$).</li>
            <li><strong>Cross-Slope Limits:</strong> The maximum allowable lateral cross-slope on any accessible walkway is $1:48$ ($2.08\%$) to prevent wheelchair drifting.</li>
          </ul>

          <h2>Hydraulic Stormwater Drainage Minimum Gradients</h2>
          <p>
            Water must drain by gravity away from building structures to prevent foundation undermining, basement flooding, and soil liquefaction. Building codes mandate minimum drainage slopes:
          </p>
          <ul>
            <li><strong>Foundation Perimeter Grading (IBC 1804.4):</strong> Unpaved ground within $10\text{ feet}$ ($3.05\text{ m}$) of a foundation wall must slope downward at minimum $5\%$ ($1:20$ or $0.5\text{ ft}$ drop per $10\text{ ft}$). Where swales or property lot lines intervene, an impervious apron with minimum $2\%$ slope is allowed.</li>
            <li><strong>Gravity Sewer &amp; Drainage Pipes (IPC Chapter 7):</strong> Underground drainage lines require minimum self-cleansing scouring velocity ($2.0\text{ ft/s}$ / $0.6\text{ m/s}$):
              <div class="formula-box">
                $$\le 2\text{-inch pipe}: \frac{1}{4}\text{ in/ft } (2.08\%) \quad \mid \quad 3\text{ to }6\text{-inch pipe}: \frac{1}{8}\text{ in/ft } (1.04\%)$$
              </div>
            </li>
            <li><strong>Paved Concrete &amp; Asphalt Surfaces:</strong> Minimum $1.0\%$ to $1.5\%$ cross-slope to eliminate standing puddles and hydroplaning hazards.</li>
          </ul>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Civil Application</th>
                <th>Slope Ratio (V : H)</th>
                <th>Percentage Grade (%)</th>
                <th>Angle in Degrees (&theta;)</th>
                <th>Code Authority / Standard</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Accessible Walkway (Normal)</td>
                <td>1 : 20</td>
                <td>5.00%</td>
                <td>2.86°</td>
                <td>ADAAG Section 403 (No handrails required)</td>
              </tr>
              <tr>
                <td>ADA Wheelchair Ramp (Max)</td>
                <td>1 : 12</td>
                <td>8.33%</td>
                <td>4.76°</td>
                <td>ADAAG Section 405 (Handrails mandatory)</td>
              </tr>
              <tr>
                <td>Residential Vehicle Driveway</td>
                <td>1 : 8 to 1 : 6.7</td>
                <td>12.0% – 15.0%</td>
                <td>6.84° – 8.53°</td>
                <td>Local Municipal Codes (Max 15-20%)</td>
              </tr>
              <tr>
                <td>Highway Maximum Grade</td>
                <td>1 : 16.7 to 1 : 14.3</td>
                <td>6.0% – 7.0%</td>
                <td>3.43° – 4.00°</td>
                <td>AASHTO Interstate Highway Criteria</td>
              </tr>
              <tr>
                <td>Cut Slope (OSHA Type B Soil)</td>
                <td>1 : 1</td>
                <td>100.0%</td>
                <td>45.00°</td>
                <td>OSHA 29 CFR 1926 Subpart P</td>
              </tr>
            </tbody>
          </table>

          <h2>Geotechnical Embankment Slope Stability, Factor of Safety &amp; Critical Slip Surfaces</h2>
          <p>
            In geotechnical slope engineering, determining the mechanical stability of natural hillsides, roadway cuts, and engineered earthen embankments prevents catastrophic landslides. The primary measure of slope equilibrium is the <strong>Factor of Safety ($FS$)</strong>, defined as the ratio of available shear strength ($\tau_f$) to mobilized driving shear stress ($\tau_m$) along the critical slip failure surface:
          </p>
          <div class="formula-box">
            $$FS = \frac{\tau_f}{\tau_m} = \frac{c' + (\sigma_n - u) \tan \phi'}{\tau_m}$$
          </div>
          <p>
            Where $c'$ is effective soil cohesion, $\sigma_n$ is normal total stress, $u$ is pore water pressure, and $\phi'$ is the internal friction angle of the soil per the Mohr-Coulomb failure criterion.
          </p>
          <p>
            <strong>Infinite Slope Analysis with Seepage:</strong> For a shallow translational slide in a granular soil slope of incline angle $\beta$ with steady-state seepage parallel to the slope:
          </p>
          <div class="formula-box">
            $$FS = \left(1 - \frac{\gamma_w \cdot h}{\gamma_{sat} \cdot z}\right) \frac{\tan \phi'}{\tan \beta}$$
          </div>
          <p>
            When pore water pressure builds to the ground surface ($h = z$), the buoyant reduction roughly halves the effective friction angle, reducing the safe slope angle to approximately half of the soil's natural internal friction angle ($\beta_{safe} \approx \frac{1}{2} \phi'$). Engineered benching, perforated horizontal drainage wicks, and retaining gabion baskets are standard stabilization countermeasures.
          </p>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: Designing an Accessible Municipal Clinic Entrance Ramp</h3>
            <p><strong>Design Scenario:</strong> A municipal community health clinic has a finished ground floor elevation set $H = 0.90\text{ meters}$ ($900\text{ mm}$ / $35.43\text{ inches}$) above the adjacent parking lot sidewalk. The architectural specification mandates a fully compliant <strong>ADA wheelchair accessible ramp</strong> designed at the maximum permissible slope ratio of $1:12$ ($8.33\%$ grade). Calculate the required total horizontal run ($\Delta x$), the slope angle in degrees ($\theta$), the physical travel length along the ramp deck (hypotenuse), verify the number of required intermediate rest landings (maximum $760\text{ mm}$ rise per run), and establish total ramp footprint dimensions.</p>
            
            <p><strong>Step 1: Compute Required Horizontal Run ($\Delta x$)</strong></p>
            <div class="formula-box">
              $$\Delta x = \Delta y \times 12 = 0.90\text{ m} \times 12 = \mathbf{10.80\text{ meters}} \quad (\approx 35.43\text{ feet})$$
            </div>

            <p><strong>Step 2: Calculate Slope Angle (&theta;) and Percentage Grade</strong></p>
            <div class="formula-box">
              $$m = \frac{1}{12} \approx 0.08333$$
              $$\text{Grade } (\%) = 0.08333 \times 100 = \mathbf{8.33\%}$$
              $$\theta = \arctan(1 / 12) = \arctan(0.08333) \approx \mathbf{4.76^\circ}$$
            </div>

            <p><strong>Step 3: Evaluate Travel Distance (Hypotenuse)</strong></p>
            <div class="formula-box">
              $$D_{slope} = \sqrt{\Delta x^2 + \Delta y^2} = \sqrt{(10.80)^2 + (0.90)^2} = \sqrt{116.64 + 0.81} = \sqrt{117.45} \approx \mathbf{10.84\text{ meters}}$$
            </div>

            <p><strong>Step 4: Check Intermediate Landing Requirement</strong></p>
            <p>
              Since the total rise of $900\text{ mm}$ exceeds the ADAAG threshold of $760\text{ mm}$ ($30\text{ inches}$), the ramp cannot be built in a single unbroken run. The civil designer splits the rise into two equal flights of $450\text{ mm}$ rise each ($5.40\text{ m}$ run per flight) separated by an intermediate level landing measuring $1.50\text{ m} \times 1.50\text{ m}$ ($5\text{ ft} \times 5\text{ ft}$).
            </p>
            <p>
              <strong>Engineering Conclusion:</strong> The ADA entrance system requires two <strong>$5.40\text{-meter}$ sloped ramp segments</strong> ($8.33\%$ grade, $4.76^\circ$) plus one <strong>$1.50\text{-meter}$ level landing</strong>, giving a total structural run of <strong>$12.30\text{ meters}$</strong>.
            </p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Civil &amp; Surveying Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="roof-pitch-calculator.html">Roof Pitch &amp; Rafter Length</a></li>
            <li><a href="excavation-volume-calculator.html">Excavation Volume Calculator</a></li>
            <li><a href="retaining-wall-calculator.html">Retaining Wall Stability</a></li>
            <li><a href="asphalt-calculator.html">Asphalt Paving &amp; Tonnage</a></li>
            <li><a href="beam-calculator.html">Beam Bending &amp; Shear</a></li>
          </ul>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container footer-content">
      <div class="footer-col">
        <h4>CalcHub</h4>
        <p>High-precision professional engineering and scientific calculation engines.</p>
      </div>
      <div class="footer-col">
        <h4>Directories</h4>
        <ul class="footer-links">
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="civil.html">Civil &amp; Construction</a></li>
          <li><a href="mechanical.html">Mechanical Engineering</a></li>
          <li><a href="engineering.html">Civil &amp; Structural</a></li>
          <li><a href="sitemap.xml">XML Sitemap</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom text-center">
      <p>&copy; 2026 CalcHub. Standard Engineering Reference Systems.</p>
    </div>
  </footer>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const calcBtn = document.getElementById('calcSlopeBtn');
      const resetBtn = document.getElementById('resetSlopeBtn');
      const resultBox = document.getElementById('slopeResultBox');
      const modeSelect = document.getElementById('slopeMode');
      const rowRiseRun = document.getElementById('rowRiseRun');
      const rowCoords = document.getElementById('rowCoords');
      const rowGrade = document.getElementById('rowGrade');
      const rowAngle = document.getElementById('rowAngle');

      modeSelect.addEventListener('change', function() {
        const val = this.value;
        rowRiseRun.style.display = (val === 'riseRun') ? 'flex' : 'none';
        rowCoords.style.display = (val === 'twoPoints') ? 'flex' : 'none';
        rowGrade.style.display = (val === 'gradePct') ? 'flex' : 'none';
        rowAngle.style.display = (val === 'angleDeg') ? 'flex' : 'none';
      });

      function calculateSlope() {
        const mode = modeSelect.value;
        let rise = 0.0;
        let run = 1.0;

        if (mode === 'riseRun') {
          rise = parseFloat(document.getElementById('vertRise').value);
          run = parseFloat(document.getElementById('horizRun').value);
          if (isNaN(rise) || isNaN(run) || run === 0) {
            alert('Please enter valid numbers. Horizontal run cannot be zero.');
            return;
          }
        } else if (mode === 'twoPoints') {
          const x1 = parseFloat(document.getElementById('coordX1').value);
          const y1 = parseFloat(document.getElementById('coordY1').value);
          const x2 = parseFloat(document.getElementById('coordX2').value);
          const y2 = parseFloat(document.getElementById('coordY2').value);
          if (isNaN(x1) || isNaN(y1) || isNaN(x2) || isNaN(y2) || (x2 - x1) === 0) {
            alert('Please enter valid coordinates with x2 ≠ x1.');
            return;
          }
          rise = y2 - y1;
          run = x2 - x1;
        } else if (mode === 'gradePct') {
          const grade = parseFloat(document.getElementById('inputGrade').value);
          run = parseFloat(document.getElementById('distGrade').value);
          if (isNaN(grade) || isNaN(run) || run === 0) {
            alert('Please enter a valid grade and distance.');
            return;
          }
          rise = (grade / 100.0) * run;
        } else if (mode === 'angleDeg') {
          const angle = parseFloat(document.getElementById('inputAngle').value);
          run = parseFloat(document.getElementById('distAngle').value);
          if (isNaN(angle) || isNaN(run) || run === 0 || angle < 0 || angle >= 90) {
            alert('Please enter a valid angle (0° to 89.9°) and distance.');
            return;
          }
          const rad = angle * (Math.PI / 180.0);
          rise = run * Math.tan(rad);
        }

        const m = rise / run;
        const gradePct = Math.abs(m) * 100.0;
        const angleRad = Math.atan(Math.abs(m));
        const angleDeg = angleRad * (180.0 / Math.PI);
        const ratioX = (Math.abs(m) > 0) ? (1.0 / Math.abs(m)) : 0;
        const hypotenuse = Math.sqrt(rise * rise + run * run);

        let adaStatus = 'Non-Compliant (>8.33%)';
        if (gradePct <= 5.0) {
          adaStatus = 'Compliant (Walkway ≤5%)';
        } else if (gradePct <= 8.333) {
          adaStatus = 'Compliant (Ramp ≤8.33%)';
        }

        document.getElementById('resGradePct').textContent = (m < 0 ? '-' : '') + gradePct.toFixed(2) + '%';
        document.getElementById('resAngleDeg').textContent = angleDeg.toFixed(2) + '°';
        document.getElementById('resRatio').textContent = (ratioX > 0) ? `1 : ${ratioX.toFixed(2)}` : 'Flat 0';
        document.getElementById('resDecimalM').textContent = m.toFixed(4);
        document.getElementById('resHypotenuse').textContent = hypotenuse.toFixed(2);
        document.getElementById('resAdaStatus').textContent = adaStatus;

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculateSlope);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
        modeSelect.value = 'riseRun';
        rowRiseRun.style.display = 'flex';
        rowCoords.style.display = 'none';
        rowGrade.style.display = 'none';
        rowAngle.style.display = 'none';
      });
      calculateSlope();
    });
  </script>
</body>
</html>
"""

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    path_slab = os.path.join(base_dir, 'slab-concrete-calculator.html')
    with open(path_slab, 'w', encoding='utf-8') as f:
        f.write(TOOL_7_HTML.strip() + '\n')
    print("[PASS] slab-concrete-calculator.html generated successfully!")

    path_slope = os.path.join(base_dir, 'slope-calculator.html')
    with open(path_slope, 'w', encoding='utf-8') as f:
        f.write(TOOL_8_HTML.strip() + '\n')
    print("[PASS] slope-calculator.html generated successfully!")

if __name__ == '__main__':
    main()
