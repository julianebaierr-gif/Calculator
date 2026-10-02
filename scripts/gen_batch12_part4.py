# -*- coding: utf-8 -*-
"""
Script to generate Batch 12 Part 4 tools:
7. excavation-volume-calculator.html
8. flooring-calculator.html
"""
import os

TOOL_7_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Excavation Volume Calculator | Prismoidal &amp; End-Area Earthwork</title>
  <meta name="description" content="Calculate earthwork excavation volumes using the Average End Area method, Prismoidal formula, trench trapezoidal side slopes, and soil swell factor expansions.">
  <link rel="canonical" href="https://calchub.cloud/excavation-volume-calculator.html">
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
        "name": "Excavation Volume Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Earthwork volume calculator applying the Average End Area and Prismoidal formulas to sloped trenches, basement cuts, and trapezoidal cross-sections.",
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
            "name": "What is the difference between the Average End Area method and the Prismoidal formula?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The Average End Area method computes volume as V = (L / 2) * (A1 + A2). While simple, it almost always overestimates true volume when cross-sectional areas differ significantly. The Prismoidal formula, V = (L / 6) * (A1 + 4*Am + A2), where Am is the midsection area, accounts for three-dimensional taper and yields the exact mathematical earthwork volume."
            }
          },
          {
            "@type": "Question",
            "name": "How is the volume of a sloped trapezoidal trench calculated?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For a trench of length L, base width b, depth d, and horizontal-to-vertical side slope z:1 (H:V): The cross-sectional area is A = d * (b + z * d). Total volume is V = L * d * (b + z * d), where top width is W_top = b + 2 * z * d."
            }
          },
          {
            "@type": "Question",
            "name": "What is the prismoidal correction (Cp) formula?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The prismoidal correction formula for three-level highway sections is: C_p = (L / 12) * (c1 - c2) * (w1 - w2), where c1, c2 are center cut heights and w1, w2 are total top widths at stations 1 and 2. True volume is V_true = V_end_area - C_p."
            }
          },
          {
            "@type": "Question",
            "name": "Why must swell factors be applied to excavation volume estimates?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In-situ undisturbed ground (Bank volume) expands when mechanically dislodged due to particle separation and air entrapment. Swell factors range from 15% for granular sand to 40% for cohesive clays, and up to 60% for blasted rock, governing dump truck haul fleet requirements."
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
      <span>Excavation Volume Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calculator-main">
        <div class="calc-header">
          <h1>Excavation Volume Calculator</h1>
          <p>Compute accurate earthwork cut volumes using the Prismoidal formula, trapezoidal side slopes, and soil swell factors.</p>
        </div>

        <div class="calculator-card">
          <form id="volumeCalcForm" onsubmit="return false;">
            <div class="form-row">
              <div class="form-group">
                <label for="calcMethod">Geometry Configuration:</label>
                <select id="calcMethod">
                  <option value="trapezoid" selected>Trapezoidal Trench (Sloped Side Embankments)</option>
                  <option value="slopedPit">Rectangular Foundation Pit (4 Sloped Sides)</option>
                  <option value="endArea">Two Cross-Sections (Average End Area)</option>
                </select>
              </div>
              <div class="form-group">
                <label for="excavLength">Length of Cut (meters):</label>
                <input type="number" id="excavLength" value="50.0" step="1.0" min="0.1" required>
                <span class="hint">Longitudinal station distance</span>
              </div>
            </div>

            <!-- Trapezoidal Trench Inputs -->
            <div class="form-row" id="rowTrapezoid">
              <div class="form-group">
                <label for="bottomWidth">Bottom Base Width (meters):</label>
                <input type="number" id="bottomWidth" value="1.5" step="0.1" min="0.1">
                <span class="hint">Trench invert width for pipe bedding</span>
              </div>
              <div class="form-group">
                <label for="trenchDepth">Excavation Depth (meters):</label>
                <input type="number" id="trenchDepth" value="2.4" step="0.1" min="0.1">
                <span class="hint">Vertical cut from grade to invert</span>
              </div>
              <div class="form-group">
                <label for="sideSlopeZ">Side Slope Ratio (H : 1V):</label>
                <select id="sideSlopeZ">
                  <option value="0">Vertical 0:1 (Shored / Trench Box)</option>
                  <option value="0.75">0.75:1 (53° - OSHA Type A Clay)</option>
                  <option value="1.0" selected>1.0:1 (45° - OSHA Type B Silt/Loam)</option>
                  <option value="1.5">1.5:1 (34° - OSHA Type C Sand/Gravel)</option>
                  <option value="2.0">2.0:1 (26.6° - Stable Drainage Ditch)</option>
                </select>
              </div>
            </div>

            <!-- Sloped Pit Inputs -->
            <div class="form-row" id="rowPit" style="display:none;">
              <div class="form-group">
                <label for="pitBottomL">Bottom Length (meters):</label>
                <input type="number" id="pitBottomL" value="18.0" step="0.5" min="0.1">
              </div>
              <div class="form-group">
                <label for="pitBottomW">Bottom Width (meters):</label>
                <input type="number" id="pitBottomW" value="12.0" step="0.5" min="0.1">
              </div>
              <div class="form-group">
                <label for="pitDepth">Pit Depth (meters):</label>
                <input type="number" id="pitDepth" value="3.0" step="0.1" min="0.1">
              </div>
            </div>

            <!-- End Area Inputs -->
            <div class="form-row" id="rowEndArea" style="display:none;">
              <div class="form-group">
                <label for="areaStation1">Area at Station 1 (m²):</label>
                <input type="number" id="areaStation1" value="24.5" step="0.1" min="0.1">
              </div>
              <div class="form-group">
                <label for="areaStation2">Area at Station 2 (m²):</label>
                <input type="number" id="areaStation2" value="38.2" step="0.1" min="0.1">
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="soilSwell">Soil Swell Factor (%):</label>
                <input type="number" id="soilSwell" value="25" step="1" min="0" max="80" required>
                <span class="hint">Standard common earth ~25%, clay ~40%</span>
              </div>
              <div class="form-group">
                <label for="dumpTruckCap">Dump Truck Box Capacity (m³):</label>
                <input type="number" id="dumpTruckCap" value="10.0" step="0.5" min="1.0" required>
                <span class="hint">Standard 10-wheeler ~10 m³</span>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcVolBtn">Compute Earthwork Volumes</button>
              <button type="reset" class="btn btn-secondary" id="resetVolBtn">Reset</button>
            </div>
          </form>

          <div class="results-box" id="volResultBox" style="display:none; margin-top:25px;">
            <h3>Exact Earthwork Volumetric Quantities</h3>
            <div class="result-grid">
              <div class="result-tile highlight">
                <span class="result-label">True Bank Volume (In-Situ)</span>
                <span class="result-value" id="resTrueBank">0.00</span>
                <span class="result-unit">m³ (~0 cu yd)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Expanded Loose Volume</span>
                <span class="result-value" id="resLooseVol">0.00</span>
                <span class="result-unit">m³ (~0 cu yd)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Truck Haul Trips</span>
                <span class="result-value" id="resTruckLoads">0</span>
                <span class="result-unit">Haul Loads</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Top Trench / Pit Width</span>
                <span class="result-value" id="resTopWidth">0.00</span>
                <span class="result-unit">meters (Surface Daylight)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Cross-Sectional Area (Avg)</span>
                <span class="result-value" id="resAvgArea">0.00</span>
                <span class="result-unit">m² (square meters)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Total Excavated Mass</span>
                <span class="result-value" id="resSoilMass">0</span>
                <span class="result-unit">Metric Tonnes (~0 US tons)</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Earthwork Volumetric Calculation Methodologies</h2>
          <p>
            In heavy highway engineering, civil site preparation, and pipeline installation, calculating precise cut-and-fill volumes directly governs project contracting costs, mass haul logistics, and equipment fleet selection. Ground topography rarely forms uniform geometric prisms, necessitating mathematical integration methods to evaluate three-dimensional excavation solids.
          </p>
          <p>
            Two primary analytical procedures are standardized across civil engineering practice:
          </p>
          <ul>
            <li><strong>Average End Area Method:</strong> A widely used surveying approximation that calculates volume between two cross-sections by averaging their end areas and multiplying by station distance.</li>
            <li><strong>Prismoidal Formula:</strong> The mathematically exact volume integral for any solid bounded by planar surfaces or surfaces generated by straight lines moving over parallel end planes.</li>
          </ul>

          <h2>Mathematical Derivation: Average End Area vs. Prismoidal Formula</h2>
          <p>
            Given two parallel cross-sectional cut areas $A_1$ and $A_2$ separated by a longitudinal centerline distance $L$, the <strong>Average End Area volume ($V_e$)</strong> is formulated as:
          </p>
          <div class="formula-box">
            $$V_e = \frac{L}{2} (A_1 + A_2) = L \times \left(\frac{A_1 + A_2}{2}\right)$$
          </div>
          <p>
            While straightforward, the average end area method introduces a systematic mathematical error whenever $A_1 \ne A_2$. Because it assumes a linear variation in area along $L$ rather than a quadratic variation in linear dimensions, the end area method <strong>consistently overestimates</strong> true earthwork volume.
          </p>
          <p>
            To achieve exact volumetric precision, the <strong>Prismoidal Formula</strong> samples the mid-depth cross-sectional area $A_m$:
          </p>
          <div class="formula-box">
            $$V_p = \frac{L}{6} (A_1 + 4 A_m + A_2)$$
          </div>
          <p>
            <strong>Crucial Rule:</strong> The mid-area $A_m$ is <em>not</em> the arithmetic average of $A_1$ and $A_2$. Rather, $A_m$ must be calculated by first averaging the linear dimensions (widths and heights) of the two end sections and then evaluating the resulting area.
          </p>
          <p>
            For three-level highway cross-sections, the difference between the average end area approximation and the exact prismoidal volume is called the <strong>Prismoidal Correction ($C_p$)</strong>:
          </p>
          <div class="formula-box">
            $$C_p = V_e - V_p = \frac{L}{12} (c_1 - c_2)(w_1 - w_2)$$
            $$V_{true} = V_e - C_p$$
          </div>
          <p>
            Where $c_1, c_2$ are center cut depths and $w_1, w_2$ are total slope-stake daylight widths at stations 1 and 2.
          </p>

          <h2>Trapezoidal Trench Hydraulics and Pipeline Earthwork</h2>
          <p>
            When excavating continuous utility trenches for water transmission mains, gravity sewers, or stormwater culverts in unstable soils, vertical sidewalls will collapse unless shored. Under <strong>OSHA 29 CFR 1926 Subpart P</strong>, unbraced trenches must be sloped back to safe repose angles.
          </p>
          <p>
            Let a trench have base invert width $b$, depth $d$, length $L$, and horizontal-to-vertical side slope ratio $z : 1$ (where $z = \cot \theta$). The geometric dimensions are:
          </p>
          <div class="formula-box">
            $$W_{top} = b + 2 \cdot z \cdot d$$
            $$A = d \cdot \left(\frac{b + W_{top}}{2}\right) = d \cdot (b + z \cdot d)$$
            $$V_{bank} = L \cdot d \cdot (b + z \cdot d)$$
          </div>
          <p>
            For a four-sided sloped excavation pit (such as an open commercial building foundation basement) with bottom dimensions $L_b \times W_b$, depth $d$, and side slopes $z:1$:
          </p>
          <div class="formula-box">
            $$L_{top} = L_b + 2 \cdot z \cdot d \quad \text{and} \quad W_{top} = W_b + 2 \cdot z \cdot d$$
            $$A_1 = L_{top} \cdot W_{top}, \quad A_2 = L_b \cdot W_b, \quad A_m = \left(\frac{L_b + L_{top}}{2}\right) \cdot \left(\frac{W_b + W_{top}}{2}\right)$$
            $$V_{pit} = \frac{d}{6} (A_1 + 4 A_m + A_2) = d \cdot \left( L_b W_b + z d (L_b + W_b) + \frac{4}{3} z^2 d^2 \right)$$
          </div>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Soil / Rock Material</th>
                <th>In-Situ Unit Weight</th>
                <th>Swell Factor ($S_w$)</th>
                <th>OSHA Slope Ratio ($H:V$)</th>
                <th>Bank-to-Loose Factor</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Dense Glacial Till / Clay</td>
                <td>2,050 kg/m³ (3,450 lb/yd³)</td>
                <td>35% – 45%</td>
                <td>0.75:1 (53°, Type A)</td>
                <td>1.40</td>
              </tr>
              <tr>
                <td>Common Sandy Loam / Silt</td>
                <td>1,680 kg/m³ (2,830 lb/yd³)</td>
                <td>20% – 28%</td>
                <td>1.0:1 (45°, Type B)</td>
                <td>1.25</td>
              </tr>
              <tr>
                <td>Clean Gravel &amp; Coarse Sand</td>
                <td>1,850 kg/m³ (3,120 lb/yd³)</td>
                <td>12% – 18%</td>
                <td>1.5:1 (34°, Type C)</td>
                <td>1.15</td>
              </tr>
              <tr>
                <td>Rip-Rap / Blasted Basalt</td>
                <td>2,700 kg/m³ (4,550 lb/yd³)</td>
                <td>50% – 65%</td>
                <td>Stable Vertical (90°)</td>
                <td>1.60</td>
              </tr>
            </tbody>
          </table>

          <h2>Mass-Haul Curve Construction &amp; Economic Limit of Haul (LEH)</h2>
          <p>
            When managing large-scale civil site grading or highway corridor alignments, calculating cross-sectional volumes is only the initial step; the civil engineer must determine the most cost-effective disposition of cut material into fill embankments using a <strong>Mass-Haul Diagram</strong>.
          </p>
          <p>
            The algebraic accumulation of cut (positive volume) and fill (negative volume corrected for shrinkage $S_h$) yields a continuous profile curve. Where the mass curve rises, excavation exceeds embankment; where it drops, fill exceeds excavation. A horizontal balance line intersects the curve at equal cut and fill stations. The <strong>Economic Limit of Haul (LEH)</strong> establishes the exact haul distance beyond which it is cheaper to waste excavated soil locally and purchase borrow material from an off-site pit:
          </p>
          <div class="formula-box">
            $$\text{LEH} = \text{Free-Haul Distance} + \frac{C_{borrow}}{C_{overhaul}}$$
          </div>
          <p>
            Where $C_{borrow}$ is the cost to purchase, excavate, and place borrow material per cubic meter, and $C_{overhaul}$ is the contractor's transportation cost per cubic meter per station ($100\text{ m}$ / $100\text{ ft}$). Incorporating accurate prismoidal volume corrections directly prevents severe cash-flow disputes between grading contractors and project owners.
          </p>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: Municipal Stormwater Trunk Culvert Trench</h3>
            <p><strong>Design Scenario:</strong> A civil contractor is excavating a $L = 120.0\text{ meter}$ trench for a $1,200\text{ mm}$ precast concrete stormwater trunk line. The trench design requires a firm bedding bottom width of $b = 2.0\text{ meters}$ and a uniform cut depth of $d = 2.5\text{ meters}$. Geotechnical tests classify the soil as <strong>OSHA Type B Silt-Loam</strong>, requiring a side slope of $1:1$ ($z = 1.0$, $45^\circ$ angle). Laboratory tests indicate a swell factor of $S_w = 25\%$ and in-situ bank density of $1,700\text{ kg/m}^3$. Material is loaded into highway dump trucks with a struck capacity of $12.0\text{ m}^3$. Calculate top trench width, in-situ bank volume, loose haul volume, total excavated mass, and dump truck trips.</p>
            
            <p><strong>Step 1: Compute Top Trench Width and Cross-Sectional Area</strong></p>
            <div class="formula-box">
              $$W_{top} = b + 2 \cdot z \cdot d = 2.0\text{ m} + 2 \times 1.0 \times 2.5\text{ m} = 2.0 + 5.0 = \mathbf{7.0\text{ meters}}$$
              $$A = d \times (b + z \cdot d) = 2.5\text{ m} \times (2.0\text{ m} + 1.0 \times 2.5\text{ m}) = 2.5 \times 4.5 = \mathbf{11.25\text{ m}^2}$$
            </div>

            <p><strong>Step 2: Determine In-Situ Bank Volume ($V_{bank}$)</strong></p>
            <div class="formula-box">
              $$V_{bank} = L \times A = 120.0\text{ m} \times 11.25\text{ m}^2 = \mathbf{1,350.0\text{ m}^3} \quad (\approx 1,765.7\text{ cu yd})$$
            </div>

            <p><strong>Step 3: Calculate Loose Hauled Volume ($V_{loose}$) with Swell</strong></p>
            <div class="formula-box">
              $$V_{loose} = V_{bank} \times (1 + S_w / 100) = 1,350.0\text{ m}^3 \times 1.25 = \mathbf{1,687.5\text{ m}^3} \quad (\approx 2,207.2\text{ cu yd})$$
            </div>

            <p><strong>Step 4: Evaluate Excavated Soil Mass &amp; Dump Truck Trips</strong></p>
            <div class="formula-box">
              $$M_{total} = V_{bank} \times 1.70\text{ t/m}^3 = 1,350.0 \times 1.70 = \mathbf{2,295.0\text{ Metric Tonnes}}$$
              $$N_{trips} = \left\lceil \frac{1,687.5\text{ m}^3}{12.0\text{ m}^3/\text{load}} \right\rceil = \lceil 140.6 \rceil = \mathbf{141\text{ Dump Truck Loads}}$$
            </div>
            <p>
              <strong>Engineering Operational Takeaway:</strong> The top width of the trench will daylight at $7.0\text{ meters}$, requiring a site working corridor of at least $12\text{ meters}$ for excavator swing radius and haul truck turnaround. The haulage schedule must accommodate <strong>141 truck trips</strong> moving $1,687.5\text{ m}^3$ of loose earth.
            </p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Civil &amp; Earthwork Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="excavation-calculator.html">Excavation Bank &amp; Haul Estimator</a></li>
            <li><a href="retaining-wall-calculator.html">Retaining Wall Sizing</a></li>
            <li><a href="concrete-calculator.html">Concrete Volume Calculator</a></li>
            <li><a href="gravel-calculator.html">Gravel &amp; Aggregate Estimator</a></li>
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
      const calcBtn = document.getElementById('calcVolBtn');
      const resetBtn = document.getElementById('resetVolBtn');
      const resultBox = document.getElementById('volResultBox');
      const methodSelect = document.getElementById('calcMethod');
      const rowTrap = document.getElementById('rowTrapezoid');
      const rowPit = document.getElementById('rowPit');
      const rowEnd = document.getElementById('rowEndArea');

      methodSelect.addEventListener('change', function() {
        const val = this.value;
        rowTrap.style.display = (val === 'trapezoid') ? 'flex' : 'none';
        rowPit.style.display = (val === 'slopedPit') ? 'flex' : 'none';
        rowEnd.style.display = (val === 'endArea') ? 'flex' : 'none';
      });

      function calculateVolume() {
        const method = methodSelect.value;
        const L = parseFloat(document.getElementById('excavLength').value);
        const swellPct = parseFloat(document.getElementById('soilSwell').value) || 0;
        const truckCap = parseFloat(document.getElementById('dumpTruckCap').value);

        if (isNaN(L) || L <= 0 || isNaN(truckCap) || truckCap <= 0) {
          alert('Please enter valid positive dimensions for length and truck capacity.');
          return;
        }

        let V_bank = 0;
        let topWidth = 0;
        let avgArea = 0;

        if (method === 'trapezoid') {
          const b = parseFloat(document.getElementById('bottomWidth').value);
          const d = parseFloat(document.getElementById('trenchDepth').value);
          const z = parseFloat(document.getElementById('sideSlopeZ').value);
          if (isNaN(b) || b <= 0 || isNaN(d) || d <= 0) {
            alert('Please enter valid trench bottom width and depth.');
            return;
          }
          topWidth = b + 2 * z * d;
          avgArea = d * (b + z * d);
          V_bank = L * avgArea;
        } else if (method === 'slopedPit') {
          const Lb = parseFloat(document.getElementById('pitBottomL').value);
          const Wb = parseFloat(document.getElementById('pitBottomW').value);
          const d = parseFloat(document.getElementById('pitDepth').value);
          const z = 1.0; // standard 1:1 slope for pits
          if (isNaN(Lb) || Lb <= 0 || isNaN(Wb) || Wb <= 0 || isNaN(d) || d <= 0) {
            alert('Please enter valid pit bottom dimensions and depth.');
            return;
          }
          const Lt = Lb + 2 * z * d;
          const Wt = Wb + 2 * z * d;
          topWidth = Wt;
          const A1 = Lt * Wt;
          const A2 = Lb * Wb;
          const Am = ((Lt + Lb) / 2.0) * ((Wt + Wb) / 2.0);
          V_bank = (d / 6.0) * (A1 + 4.0 * Am + A2);
          avgArea = V_bank / d;
        } else if (method === 'endArea') {
          const A1 = parseFloat(document.getElementById('areaStation1').value);
          const A2 = parseFloat(document.getElementById('areaStation2').value);
          if (isNaN(A1) || A1 <= 0 || isNaN(A2) || A2 <= 0) {
            alert('Please enter valid positive cross-sectional areas.');
            return;
          }
          avgArea = (A1 + A2) / 2.0;
          V_bank = L * avgArea;
          topWidth = Math.sqrt(avgArea); // approximate equivalent
        }

        const V_loose = V_bank * (1 + swellPct / 100.0);
        const truckLoads = Math.ceil(V_loose / truckCap);
        const massTonnes = Math.round(V_bank * 1.70); // avg 1.7 t/m3
        const massUsTons = Math.round(massTonnes * 1.10231);

        const bankYd = (V_bank * 1.30795).toFixed(1);
        const looseYd = (V_loose * 1.30795).toFixed(1);

        document.getElementById('resTrueBank').textContent = V_bank.toFixed(1) + ` (~${bankYd} yd³)`;
        document.getElementById('resLooseVol').textContent = V_loose.toFixed(1) + ` (~${looseYd} yd³)`;
        document.getElementById('resTruckLoads').textContent = truckLoads.toLocaleString();
        document.getElementById('resTopWidth').textContent = topWidth.toFixed(2);
        document.getElementById('resAvgArea').textContent = avgArea.toFixed(2);
        document.getElementById('resSoilMass').textContent = massTonnes.toLocaleString() + ` (~${massUsTons} US tons)`;

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculateVolume);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
        methodSelect.value = 'trapezoid';
        rowTrap.style.display = 'flex';
        rowPit.style.display = 'none';
        rowEnd.style.display = 'none';
      });
      calculateVolume();
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
  <title>Flooring Calculator | Square Footage, Boxes &amp; Waste Estimator</title>
  <meta name="description" content="Calculate flooring square footage, cartons/boxes to purchase, pattern waste allowances (hardwood, LVP, tile), and underlayment rolls per NWFA standards.">
  <link rel="canonical" href="https://calchub.cloud/flooring-calculator.html">
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
        "name": "Flooring Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates flooring square footage, carton packaging counts, installation waste factors, and underlayment rolls per NWFA and TCNA standards.",
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
            "name": "What percentage of waste should be added when ordering flooring?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For standard straight plank installations (hardwood, laminate, LVP) in rectangular rooms, add 5% to 7% waste. For diagonal or brick patterns, add 10% to 12%. For complex herringbone, chevron, or tile patterns with multiple doorways and angled corners, add 15% to 20% waste."
            }
          },
          {
            "@type": "Question",
            "name": "How do you calculate the number of boxes of flooring to buy?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "First, compute net room square footage (Length x Width) and multiply by (1 + Waste Percentage / 100). Next, divide this gross area by the square footage coverage per box (found on the carton label, typically 18 to 24 sq ft for wood/LVP, or 10 to 15 sq ft for tile) and round UP to the nearest whole carton."
            }
          },
          {
            "@type": "Question",
            "name": "Why is an expansion gap necessary when installing hardwood or laminate flooring?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Per NWFA guidelines, organic wood fibers and click-lock laminate cores expand and contract with seasonal relative humidity changes. A continuous 1/4-inch to 1/2-inch (6 to 12 mm) expansion gap must be preserved around all perimeter walls and vertical obstructions, later concealed by baseboards or quarter-round molding."
            }
          },
          {
            "@type": "Question",
            "name": "How many rolls of underlayment are needed for a flooring installation?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Divide the total floor area by the square footage of the underlayment roll (standard rolls cover 100 sq ft). Include a 5% allowance for overlapping seam edges and perimeter wall trimming."
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
      <span>Flooring Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calculator-main">
        <div class="calc-header">
          <h1>Flooring Calculator</h1>
          <p>Estimate floor square footage, required carton boxes, pattern cutting waste, and underlayment rolls per NWFA and TCNA standards.</p>
        </div>

        <div class="calculator-card">
          <form id="flooringForm" onsubmit="return false;">
            <div class="form-row">
              <div class="form-group">
                <label for="roomL">Room Length (feet):</label>
                <input type="number" id="roomL" value="22.0" step="0.5" min="1" required>
                <span class="hint">Long wall dimension</span>
              </div>
              <div class="form-group">
                <label for="roomW">Room Width (feet):</label>
                <input type="number" id="roomW" value="16.0" step="0.5" min="1" required>
                <span class="hint">Short wall dimension</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="closetArea">Additional Closets / Alcoves (sq ft):</label>
                <input type="number" id="closetArea" value="24.0" step="1" min="0" required>
                <span class="hint">Add entryway nooks or walk-in closets</span>
              </div>
              <div class="form-group">
                <label for="islandDeduct">Obstruction Deductions (sq ft):</label>
                <input type="number" id="islandDeduct" value="0.0" step="1" min="0" required>
                <span class="hint">Kitchen islands, fire hearths, built-ins</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="flooringType">Flooring Material &amp; Format:</label>
                <select id="flooringType">
                  <option value="wood" selected>Solid / Engineered Hardwood Plank</option>
                  <option value="lvp">Luxury Vinyl Plank (LVP / SPC Rigid Core)</option>
                  <option value="laminate">Laminate Click-Lock Flooring</option>
                  <option value="tile">Porcelain / Ceramic Floor Tile</option>
                </select>
              </div>
              <div class="form-group">
                <label for="boxCoverage">Coverage Per Box / Carton (sq ft):</label>
                <input type="number" id="boxCoverage" value="20.5" step="0.1" min="1.0" required>
                <span class="hint">Check carton specification label</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="layoutPattern">Installation Layout &amp; Waste Factor:</label>
                <select id="layoutPattern">
                  <option value="7" selected>Standard Straight Planks (7% Waste)</option>
                  <option value="10">Offset Staggered / Running Bond (10% Waste)</option>
                  <option value="12">Diagonal / 45-Degree Angle (12% Waste)</option>
                  <option value="15">Herringbone / Parquet Pattern (15% Waste)</option>
                  <option value="custom">Custom Waste Percentage</option>
                </select>
              </div>
              <div class="form-group" id="customWasteGroup" style="display:none;">
                <label for="customWastePct">Custom Waste (%):</label>
                <input type="number" id="customWastePct" value="10" step="1" min="0" max="30">
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcFloorBtn">Calculate Flooring Materials</button>
              <button type="reset" class="btn btn-secondary" id="resetFloorBtn">Reset</button>
            </div>
          </form>

          <div class="results-box" id="floorResultBox" style="display:none; margin-top:25px;">
            <h3>Flooring Material Bill of Quantities</h3>
            <div class="result-grid">
              <div class="result-tile highlight">
                <span class="result-label">Full Cartons / Boxes to Buy</span>
                <span class="result-value" id="resBoxes">0</span>
                <span class="result-unit">Cartons (covers waste)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Net Floor Surface Area</span>
                <span class="result-value" id="resNetArea">0</span>
                <span class="result-unit">sq ft (~0 m²)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Purchased Total Coverage</span>
                <span class="result-value" id="resPurchasedSqFt">0.0</span>
                <span class="result-unit">sq ft (Total in boxes)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Underlayment Rolls (100 sq ft)</span>
                <span class="result-value" id="resUnderlayRolls">0</span>
                <span class="result-unit">Rolls (Acoustic / Vapor)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Perimeter Molding / Baseboard</span>
                <span class="result-value" id="resBaseboardLF">0</span>
                <span class="result-unit">Linear Feet (10% waste)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Total Material Weight</span>
                <span class="result-value" id="resFloorWeight">0</span>
                <span class="result-unit">lbs (~0 kg)</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Flooring Surface Area Estimation &amp; Industry Standards</h2>
          <p>
            Whether specifying prefinished solid oak, rigid core stone-polymer composite (SPC) luxury vinyl plank, or large-format rectified porcelain tile, accurate dimensional quantification is critical. Under-ordering results in project work stoppages and color-dye-lot mismatch risks, while excessive over-ordering wastes budget capital.
          </p>
          <p>
            Professional trade organizations—including the <strong>National Wood Flooring Association (NWFA)</strong> and the <strong>Tile Council of North America (TCNA)</strong>—mandate rigorous formulas accounting for net floor geometry, cutting waste allowances, packaging unit minimums, and expansion gap perimeters.
          </p>

          <h2>Net Surface Area Formulation</h2>
          <p>
            The net required surface area ($A_{net}$) accounts for the primary room footprint, adjacent alcoves or closets, and deductions for unfloored fixtures (such as built-in kitchen cabinetry islands, brick masonry fireplaces, or bathtub bases):
          </p>
          <div class="formula-box">
            $$A_{room} = L_{room} \times W_{room}$$
            $$A_{net} = A_{room} + A_{closets} - A_{deductions}$$
          </div>
          <p>
            To determine the gross area that must be purchased ($A_{gross}$), an empirical pattern cutting waste factor ($W_{\%}$) is applied:
          </p>
          <div class="formula-box">
            $$A_{gross} = A_{net} \times \left(1 + \frac{W_{\%}}{100}\right)$$
          </div>

          <h2>Carton Packaging Logic and Over-Order Rounding</h2>
          <p>
            Hardwood, LVP, laminate, and ceramic tiles are sold exclusively in factory-sealed cartons containing a fixed nominal area ($C_{box}$). Retailers do not break cartons. Therefore, the required purchase quantity must always be rounded up to the nearest whole integer:
          </p>
          <div class="formula-box">
            $$N_{boxes} = \left\lceil \frac{A_{gross}}{C_{box}} \right\rceil$$
            $$A_{purchased} = N_{boxes} \times C_{box}$$
            $$\text{Reserve Attic Stock} = A_{purchased} - A_{net}$$
          </div>
          <p>
            The reserve attic stock provides homeowners and facility managers with matching dye-lot replacement planks or tiles to repair future water damage, heavy scratches, or plumbing access cuts over the building lifespan.
          </p>

          <h2>Pattern Waste Guidelines per TCNA and NWFA</h2>
          <p>
            Different aesthetic laying patterns generate varying amounts of off-cut scrap:
          </p>
          <ul>
            <li><strong>Straight Plank (Parallel to Longest Wall):</strong> $5\% - 7\%$ waste. Standard layout with lowest scrap rate. Planks cut at the end of one run start the next course.</li>
            <li><strong>Offset / Staggered Running Bond (1/2 or 1/3 lap):</strong> $8\% - 10\%$ waste. Mandatory for large-format tiles ($12 \times 24\text{ in}$ or larger) per ANSI A108.02 to avoid lippage.</li>
            <li><strong>Diagonal Layout (45° Orientation):</strong> $12\% - 15\%$ waste. Every perimeter wall contact requires two triangular angled cuts, eliminating reuse of short scrap.</li>
            <li><strong>Herringbone and Chevron Parquet:</strong> $15\% - 20\%$ waste. Demands dedicated left-and-right milled tongue-and-groove planks with extensive boundary miter trimmings.</li>
          </ul>

          <h2>Perimeter Expansion Gaps and Transition Moldings</h2>
          <p>
            Natural wood is hygroscopic, expanding when absorbing ambient air humidity and contracting during winter heating cycles. Floating click-lock LVP and laminate floors similarly experience thermal expansion.
          </p>
          <div class="formula-box">
            $$\text{Perimeter Expansion Gap} = \frac{1}{4}\text{ to }\frac{1}{2}\text{ inch } (6.35 - 12.7\text{ mm})$$
          </div>
          <p>
            This expansion perimeter must remain completely unhindered around all drywall walls, structural columns, and door casings. The gap is subsequently concealed by installing baseboards and shoe molding (quarter-round).
          </p>
          <p>
            The required linear footage of baseboard molding ($LF_{molding}$) is:
          </p>
          <div class="formula-box">
            $$\text{Perimeter} = 2 \times (L_{room} + W_{room})$$
            $$LF_{molding} = \lceil \text{Perimeter} \times 1.10 \rceil \quad (10\% \text{ allowance for 45° corner miters})$$
          </div>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Flooring Type</th>
                <th>Typical Box Area</th>
                <th>Carton Weight</th>
                <th>Typical Waste %</th>
                <th>Subfloor Requirements</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Solid Hardwood (3/4" Oak)</td>
                <td>18.0 – 24.0 sq ft</td>
                <td>55 – 70 lbs (25 – 32 kg)</td>
                <td>7% – 10%</td>
                <td>3/4" Plywood, nailed/cleated</td>
              </tr>
              <tr>
                <td>Rigid Core SPC LVP (5–7 mm)</td>
                <td>20.0 – 26.0 sq ft</td>
                <td>38 – 48 lbs (17 – 22 kg)</td>
                <td>7% – 12%</td>
                <td>Flat within 3/16" over 10 ft</td>
              </tr>
              <tr>
                <td>Laminate Plank (8–12 mm)</td>
                <td>17.0 – 22.0 sq ft</td>
                <td>32 – 42 lbs (15 – 19 kg)</td>
                <td>7% – 10%</td>
                <td>Vapor barrier underlayment</td>
              </tr>
              <tr>
                <td>Porcelain Tile (12x24 / 24x24)</td>
                <td>12.0 – 16.0 sq ft</td>
                <td>50 – 65 lbs (23 – 30 kg)</td>
                <td>10% – 15%</td>
                <td>Cement backer board / uncoupling</td>
              </tr>
            </tbody>
          </table>

          <h2>Subfloor Preparation, Moisture Testing (ASTM F1869 &amp; F2170) &amp; Acoustic Underlayment</h2>
          <p>
            A high-performance flooring installation is only as durable as the subfloor substrate beneath it. According to the <strong>National Wood Flooring Association (NWFA)</strong> and ASTM specifications, subfloor deflection must not exceed $L / 360$ under total design load, and subfloor flatness must satisfy strict tolerances: maximum $\frac{3}{16}\text{ inch}$ variation over a $10\text{-foot}$ radius ($4.8\text{ mm}$ over $3\text{ m}$) for floating click-lock systems, or $\frac{1}{8}\text{ inch}$ over $6\text{ feet}$ for glue-down hardwoods.
          </p>
          <p>
            <strong>Subfloor Moisture Vapor Emissions:</strong> Concrete slab subfloors must undergo quantitative moisture vapor emission testing prior to installation:
          </p>
          <ul>
            <li><strong>ASTM F1869 (Calcium Chloride Test):</strong> Measures moisture vapor emission rate (MVER). Most flooring adhesives require MVER below $3.0\text{ lbs} / 1,000\text{ sq ft} / 24\text{ hours}$.</li>
            <li><strong>ASTM F2170 (In-Situ Relative Humidity Probes):</strong> Internal concrete relative humidity must typically remain under $75\% - 85\%$ RH unless an epoxy moisture mitigation membrane is applied.</li>
          </ul>
          <p>
            <strong>Acoustic Isolation (IIC and STC Ratings):</strong> In multi-family condominiums and high-rise developments, building codes mandate minimum <strong>Impact Insulation Class (IIC)</strong> and <strong>Sound Transmission Class (STC)</strong> ratings of 50 or higher (ASTM E492 / E90). Specialized closed-cell cross-linked polyethylene (XLPE) or natural cork underlayment rolls dampen footfall impact resonance, ensuring compliant acoustic isolation.
          </p>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: Commercial Executive Office Suite Fit-Out</h3>
            <p><strong>Design Scenario:</strong> An architect specifies luxury SPC rigid-core vinyl plank flooring for a corporate executive suite. The main room measures $L = 26.0\text{ feet}$ by $W = 18.0\text{ feet}$, plus an adjoining coffee pantry alcove measuring $6.0\text{ ft} \times 8.0\text{ ft}$ ($48.0\text{ sq ft}$). A permanent conference buffet island deducts $16.0\text{ sq ft}$ of floor space. The selected architectural plank is packaged at $21.5\text{ sq ft}$ per carton, weighing $42\text{ lbs}$ per box. The floor will be laid in a staggered straight plank pattern with a recommended $8\%$ waste factor. Calculate net floor square footage, total gross area to order, full cartons to purchase, underlayment rolls ($100\text{ sq ft}$ each), and perimeter baseboard linear footage.</p>
            
            <p><strong>Step 1: Calculate Net Floor Surface Area ($A_{net}$)</strong></p>
            <div class="formula-box">
              $$A_{main} = 26.0\text{ ft} \times 18.0\text{ ft} = 468.0\text{ sq ft}$$
              $$A_{net} = 468.0\text{ sq ft} + 48.0\text{ sq ft} - 16.0\text{ sq ft} = \mathbf{500.0\text{ sq ft}} \quad (\approx 46.45\text{ m}^2)$$
            </div>

            <p><strong>Step 2: Apply 8% Installation Waste Allowance</strong></p>
            <div class="formula-box">
              $$A_{gross} = 500.0\text{ sq ft} \times (1 + 0.08) = 500.0 \times 1.08 = \mathbf{540.0\text{ sq ft}}$$
            </div>

            <p><strong>Step 3: Determine Required Carton Boxes to Purchase</strong></p>
            <div class="formula-box">
              $$N_{boxes} = \left\lceil \frac{540.0\text{ sq ft}}{21.5\text{ sq ft/box}} \right\rceil = \lceil 25.116 \rceil = \mathbf{26\text{ Cartons of LVP}}$$
              $$A_{purchased} = 26 \times 21.5\text{ sq ft} = 559.0\text{ sq ft} \implies (59.0\text{ sq ft reserve spare})$$
            </div>

            <p><strong>Step 4: Compute Underlayment Rolls and Perimeter Baseboards</strong></p>
            <div class="formula-box">
              $$\text{Underlayment Rolls} = \left\lceil \frac{500.0\text{ sq ft} \times 1.05}{100\text{ sq ft/roll}} \right\rceil = \left\lceil \frac{525.0}{100} \right\rceil = \mathbf{6\text{ Rolls of 100 sq ft Underlayment}}$$
              $$\text{Perimeter Baseboard} = \lceil (2 \times (26 + 18) + (2 \times 6)) \times 1.10 \rceil = \lceil 100 \times 1.10 \rceil = \mathbf{110\text{ Linear Feet}}$$
            </div>
            <p>
              <strong>Procurement Summary:</strong> Order <strong>26 boxes</strong> of LVP ($1,092\text{ lbs}$ shipping mass), <strong>6 rolls</strong> of acoustic underlayment, and <strong>110 linear feet</strong> of primed baseboard molding.
            </p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Building &amp; Finish Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="drywall-calculator.html">Drywall Sheets &amp; Mud Estimator</a></li>
            <li><a href="paint-calculator.html">Paint Gallon &amp; Primer Calculator</a></li>
            <li><a href="concrete-calculator.html">Concrete Volume Calculator</a></li>
            <li><a href="beam-calculator.html">Beam Bending &amp; Shear</a></li>
            <li><a href="block-calculator.html">Block Masonry Estimator</a></li>
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
      const calcBtn = document.getElementById('calcFloorBtn');
      const resetBtn = document.getElementById('resetFloorBtn');
      const resultBox = document.getElementById('floorResultBox');
      const patternSelect = document.getElementById('layoutPattern');
      const customWasteGroup = document.getElementById('customWasteGroup');
      const floorTypeSelect = document.getElementById('flooringType');
      const boxCoverageInput = document.getElementById('boxCoverage');

      patternSelect.addEventListener('change', function() {
        if (this.value === 'custom') {
          customWasteGroup.style.display = 'block';
        } else {
          customWasteGroup.style.display = 'none';
        }
      });

      floorTypeSelect.addEventListener('change', function() {
        const val = this.value;
        if (val === 'wood') boxCoverageInput.value = '20.5';
        else if (val === 'lvp') boxCoverageInput.value = '23.8';
        else if (val === 'laminate') boxCoverageInput.value = '19.2';
        else if (val === 'tile') boxCoverageInput.value = '14.4';
      });

      function calculateFlooring() {
        const L = parseFloat(document.getElementById('roomL').value);
        const W = parseFloat(document.getElementById('roomW').value);
        const closetSqFt = parseFloat(document.getElementById('closetArea').value) || 0;
        const deductSqFt = parseFloat(document.getElementById('islandDeduct').value) || 0;
        const boxCov = parseFloat(boxCoverageInput.value);

        if (isNaN(L) || L <= 0 || isNaN(W) || W <= 0 || isNaN(boxCov) || boxCov <= 0) {
          alert('Please enter valid positive dimensions and box coverage.');
          return;
        }

        let wastePct = 7.0;
        if (patternSelect.value === 'custom') {
          wastePct = parseFloat(document.getElementById('customWastePct').value) || 10.0;
        } else {
          wastePct = parseFloat(patternSelect.value);
        }

        const roomArea = L * W;
        const netArea = Math.max(1.0, roomArea + closetSqFt - deductSqFt);
        const grossArea = netArea * (1 + wastePct / 100.0);
        const boxesNeeded = Math.ceil(grossArea / boxCov);
        const purchasedSqFt = boxesNeeded * boxCov;

        // Underlayment: 100 sq ft per roll with 5% lap waste
        const underlayRolls = Math.max(1, Math.ceil((netArea * 1.05) / 100.0));

        // Perimeter molding: 2*(L+W) + 10% waste
        const perimeter = 2 * (L + W);
        const moldingLF = Math.ceil(perimeter * 1.10);

        // Approximate weight per sq ft based on material
        const mType = floorTypeSelect.value;
        let weightPerSqFt = 2.0; // LVP approx 2 lb/sqft
        if (mType === 'wood') weightPerSqFt = 2.8;
        else if (mType === 'laminate') weightPerSqFt = 1.8;
        else if (mType === 'tile') weightPerSqFt = 4.2;

        const totalWeightLbs = Math.round(purchasedSqFt * weightPerSqFt);
        const totalWeightKg = Math.round(totalWeightLbs * 0.453592);
        const netAreaM2 = (netArea * 0.092903).toFixed(1);

        document.getElementById('resBoxes').textContent = boxesNeeded.toLocaleString();
        document.getElementById('resNetArea').textContent = Math.round(netArea).toLocaleString() + ` (~${netAreaM2} m²)`;
        document.getElementById('resPurchasedSqFt').textContent = purchasedSqFt.toFixed(1);
        document.getElementById('resUnderlayRolls').textContent = underlayRolls.toLocaleString();
        document.getElementById('resBaseboardLF').textContent = moldingLF.toLocaleString();
        document.getElementById('resFloorWeight').textContent = totalWeightLbs.toLocaleString() + ` (~${totalWeightKg} kg)`;

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculateFlooring);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
        customWasteGroup.style.display = 'none';
      });
      calculateFlooring();
    });
  </script>
</body>
</html>
"""

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    path_vol = os.path.join(base_dir, 'excavation-volume-calculator.html')
    with open(path_vol, 'w', encoding='utf-8') as f:
        f.write(TOOL_7_HTML.strip() + '\n')
    print("[PASS] excavation-volume-calculator.html generated successfully!")

    path_floor = os.path.join(base_dir, 'flooring-calculator.html')
    with open(path_floor, 'w', encoding='utf-8') as f:
        f.write(TOOL_8_HTML.strip() + '\n')
    print("[PASS] flooring-calculator.html generated successfully!")

if __name__ == '__main__':
    main()
