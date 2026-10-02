# -*- coding: utf-8 -*-
"""
Script to generate Batch 12 Part 2 tools:
3. concrete-block-calculator.html
4. concrete-mix-ratio-calculator.html
"""
import os

TOOL_3_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Concrete Block Calculator | ASTM C90 CMU &amp; Mortar Estimator</title>
  <meta name="description" content="Calculate concrete masonry blocks (CMU), ASTM C270 mortar bags, masonry sand, and ASTM C476 core grout volume with opening deductions and waste allowances.">
  <link rel="canonical" href="https://calchub.cloud/concrete-block-calculator.html">
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
        "name": "Concrete Block Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates concrete masonry unit (CMU) counts, Type S/N mortar batches, masonry sand tonnage, and core-fill grout volumes per ASTM C90 and TMS 402.",
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
            "name": "How many standard concrete blocks (CMU) are required per square foot and square meter of wall?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A standard nominal 8x8x16 inch CMU block (actual 7-5/8 x 7-5/8 x 15-5/8 inches plus 3/8-inch mortar joint) has a nominal face area of 128 sq in (0.8889 sq ft or 0.08 m²). Therefore, exactly 1.125 blocks are needed per square foot (112.5 blocks per 100 sq ft) or 12.5 blocks per square meter."
            }
          },
          {
            "@type": "Question",
            "name": "How much mortar and sand is needed for 100 concrete blocks?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For standard face-shell bedding of 8-inch CMU blocks, approximately 3 bags (80-lb / 36-kg) of ASTM C270 Type S or Type N masonry cement and 0.28 to 0.32 metric tons (7.5 to 8.5 cu ft) of masonry sand are required per 100 blocks."
            }
          },
          {
            "@type": "Question",
            "name": "How much concrete grout is needed to fill cores in concrete block walls?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For standard 8-inch hollow CMU blocks, 100% solid core grouting requires approximately 0.95 m³ (33.5 cu ft) of grout per 100 blocks. Grouting every 24 inches on-center consumes ~0.32 m³ per 100 blocks, and grouting every 48 inches consumes ~0.16 m³ per 100 blocks."
            }
          },
          {
            "@type": "Question",
            "name": "What is the compressive strength requirement for ASTM C90 loadbearing CMU?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "ASTM C90 mandates a minimum average net-area compressive strength of 2,000 psi (13.79 MPa) for individual units, and 1,900 psi (13.1 MPa) minimum for any single unit, ensuring sufficient capacity for multistory loadbearing masonry structures."
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
      <span>Concrete Block Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calculator-main">
        <div class="calc-header">
          <h1>Concrete Block Calculator</h1>
          <p>Estimate CMU concrete block counts, mortar cement bags, masonry sand, and core grout volume per ASTM C90 and TMS 402 specifications.</p>
        </div>

        <div class="calculator-card">
          <form id="cmuCalcForm" onsubmit="return false;">
            <div class="form-row">
              <div class="form-group">
                <label for="wallLength">Wall Length (meters):</label>
                <input type="number" id="wallLength" value="12.0" step="0.1" min="0.1" required>
                <span class="hint">Total horizontal run of masonry wall</span>
              </div>
              <div class="form-group">
                <label for="wallHeight">Wall Height (meters):</label>
                <input type="number" id="wallHeight" value="2.8" step="0.05" min="0.1" required>
                <span class="hint">Total finished height from top of footing</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="openingArea">Deductions for Openings (m²):</label>
                <input type="number" id="openingArea" value="3.6" step="0.1" min="0" required>
                <span class="hint">Total area of doors, windows, and louvers</span>
              </div>
              <div class="form-group">
                <label for="blockSize">Block Nominal Size:</label>
                <select id="blockSize">
                  <option value="4">4" CMU (100 × 200 × 400 mm) - Partition</option>
                  <option value="6">6" CMU (150 × 200 × 400 mm) - Light Load</option>
                  <option value="8" selected>8" CMU (200 × 200 × 400 mm) - Standard Loadbearing</option>
                  <option value="10">10" CMU (250 × 200 × 400 mm) - Heavy Foundation</option>
                  <option value="12">12" CMU (300 × 200 × 400 mm) - Retaining &amp; Basements</option>
                </select>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="groutSpacing">Core Grouting Specification:</label>
                <select id="groutSpacing">
                  <option value="0">No Core Grout (Hollow Non-Structural)</option>
                  <option value="48">Grout Every 48" (1200 mm oc)</option>
                  <option value="32">Grout Every 32" (800 mm oc)</option>
                  <option value="24">Grout Every 24" (600 mm oc)</option>
                  <option value="16">Grout Every 16" (400 mm oc - Every Cell)</option>
                  <option value="100" selected>100% Solid Grout (Retaining / Shear Wall)</option>
                </select>
                <span class="hint">Frequency of vertical rebar core cells filled</span>
              </div>
              <div class="form-group">
                <label for="wasteMargin">Waste &amp; Cutting Allowance (%):</label>
                <input type="number" id="wasteMargin" value="8" step="1" min="0" max="25" required>
                <span class="hint">Recommended 5% to 10% for cuts &amp; breakage</span>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcCmuBtn">Calculate Materials</button>
              <button type="reset" class="btn btn-secondary" id="resetCmuBtn">Reset</button>
            </div>
          </form>

          <div class="results-box" id="cmuResultBox" style="display:none; margin-top:25px;">
            <h3>Concrete Masonry Material Bill of Quantities</h3>
            <div class="result-grid">
              <div class="result-tile highlight">
                <span class="result-label">Total CMU Blocks to Order</span>
                <span class="result-value" id="resTotalBlocks">0</span>
                <span class="result-unit">Units (including waste)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Net Masonry Wall Area</span>
                <span class="result-value" id="resNetArea">0.00</span>
                <span class="result-unit">m² (sq meters)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Type S/N Mortar Cement</span>
                <span class="result-value" id="resMortarBags">0</span>
                <span class="result-unit">Bags (80 lb / 36.3 kg)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Masonry Sand Volume</span>
                <span class="result-value" id="resSandTonnes">0.00</span>
                <span class="result-unit">Metric Tonnes (~0.0 m³)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Concrete Core Grout Volume</span>
                <span class="result-value" id="resGroutVol">0.00</span>
                <span class="result-unit">m³ (Cubic Meters)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Total Assembled Wall Mass</span>
                <span class="result-value" id="resWallMass">0</span>
                <span class="result-unit">kg (~0.0 metric tons)</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Concrete Masonry Unit (CMU) Engineering &amp; Sizing Principles</h2>
          <p>
            Concrete masonry construction relies on precast hollow or solid block units manufactured from Portland cement, graded mineral aggregates, and water under high compaction and steam curing. In modern commercial, institutional, and residential structures, <strong>Concrete Masonry Units (CMU)</strong> serve as loadbearing exterior walls, interior acoustic partitions, fire separation barriers, and retaining wall assemblies.
          </p>
          <p>
            Under <strong>ASTM C90 (Standard Specification for Loadbearing Concrete Masonry Units)</strong>, manufactured blocks must satisfy strict physical criteria regarding compressive strength, water absorption, dimensional tolerances, and moisture shrinkage. Standard modular blocks are designed around a $4\text{-inch}$ ($100\text{ mm}$) modular grid system. The nominal dimensions of a standard block are $8 \times 8 \times 16\text{ inches}$ ($200 \times 200 \times 400\text{ mm}$), while its actual physical dimensions are $7\frac{5}{8} \times 7\frac{5}{8} \times 15\frac{5}{8}\text{ inches}$ ($194 \times 194 \times 397\text{ mm}$). The planned $\frac{3}{8}\text{-inch}$ ($9.5\text{ mm}$) mortar joint brings the installed dimensions precisely to modular grid lines.
          </p>

          <h2>Mathematical Geometry of CMU Wall Layout</h2>
          <p>
            The face area of an individual installed modular unit, including its surrounding $\frac{3}{8}\text{-inch}$ ($9.5\text{ mm}$) bed and head mortar joints, is:
          </p>
          <div class="formula-box">
            $$A_{unit} = H_{nom} \times L_{nom} = 0.20\text{ m} \times 0.40\text{ m} = 0.080\text{ m}^2 \quad (0.8889\text{ sq ft})$$
          </div>
          <p>
            To compute the total block requirement for a wall with surface length $L$, height $H$, and total window/door opening deductions $A_{openings}$:
          </p>
          <div class="formula-box">
            $$A_{gross} = L \times H$$
            $$A_{net} = A_{gross} - A_{openings}$$
            $$N_{net} = \frac{A_{net}}{A_{unit}} = A_{net} \times 12.50\text{ blocks/m}^2 \quad \left(A_{net} \text{ in ft}^2 \times 1.125\text{ blocks/ft}^2\right)$$
            $$N_{total} = \lceil N_{net} \times (1 + \text{Waste Factor}) \rceil$$
          </div>

          <h2>ASTM C270 Mortar Proportioning &amp; Sand Quantities</h2>
          <p>
            Masonry mortar bonds units into an integrated monolithic structural diaphragm while sealing joints against moisture penetration and air infiltration. Mortar selection is governed by <strong>ASTM C270 (Standard Specification for Mortar for Unit Masonry)</strong>:
          </p>
          <ul>
            <li><strong>Type M Mortar ($17.2\text{ MPa} / 2,500\text{ psi}$):</strong> High-strength compressive mix used for below-grade foundations, heavy retaining walls, and earth-contact structures subject to severe frost action.</li>
            <li><strong>Type S Mortar ($12.4\text{ MPa} / 1,800\text{ psi}$):</strong> High flexural bond strength mix mandatory for exterior loadbearing masonry walls, seismic shear walls, and below-grade foundation basements.</li>
            <li><strong>Type N Mortar ($5.2\text{ MPa} / 750\text{ psi}$):</strong> Medium-strength, highly workable mix optimized for exterior above-grade veneers and interior architectural partitions.</li>
          </ul>
          <p>
            For standard face-shell bedding of $8\text{-inch}$ ($200\text{ mm}$) blocks, mortar consumption adheres to empirical site-tested ratios:
          </p>
          <div class="formula-box">
            $$\text{Mortar Cement Bags (80 lb / 36.3 kg)} \approx \frac{N_{total}}{33.0}$$
            $$\text{Masonry Sand (Metric Tonnes)} \approx N_{total} \times 0.0030 \text{ tonnes}$$
          </div>

          <h2>Core Grouting Mechanics &amp; Reinforcement (ASTM C476 &amp; TMS 402)</h2>
          <p>
            Hollow CMUs have an internal void volume of approximately $48\%$ to $52\%$ divided into two large hollow cores. In structural reinforced masonry designed per <strong>TMS 402/602 (Building Code Requirements and Specification for Masonry Structures)</strong>, vertical reinforcing rebar (typically #4, #5, or #6 deformed bars) is positioned within these hollow cells. High-slump concrete grout (compressive strength $f'_g \ge 13.8\text{ MPa} / 2,000\text{ psi}$, slump $200 - 275\text{ mm}$ per <strong>ASTM C476</strong>) is then poured or pumped to encapsulate the steel.
          </p>
          <p>
            The required grout volume varies directly with cell grouting frequency:
          </p>
          <ul>
            <li><strong>100% Solid Grout:</strong> Every core cell is grouted solid ($0.0095\text{ m}^3 / 0.335\text{ cu ft}$ per $8\text{-inch}$ block). Mandatory for basement retaining walls, storm shelters, and foundation walls.</li>
            <li><strong>Grout @ 16" oc ($400\text{ mm}$):</strong> Every vertical cell aligned with rebar is filled ($0.0095\text{ m}^3$ per block).</li>
            <li><strong>Grout @ 24" oc ($600\text{ mm}$):</strong> Two out of every three units contain filled cells ($0.0063\text{ m}^3$ per block).</li>
            <li><strong>Grout @ 32" oc ($800\text{ mm}$):</strong> Every other block has one cell filled ($0.00475\text{ m}^3$ per block).</li>
            <li><strong>Grout @ 48" oc ($1200\text{ mm}$):</strong> One cell out of every three blocks is filled ($0.00317\text{ m}^3$ per block).</li>
          </ul>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Nominal CMU Size (W &times; H &times; L)</th>
                <th>Actual Dimensions</th>
                <th>Unit Weight (Medium Wt)</th>
                <th>100% Solid Grout Vol / 100 Blocks</th>
                <th>Typical Structural Application</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>4 &times; 8 &times; 16 in (100 mm)</td>
                <td>3⅝ &times; 7⅝ &times; 15⅝ in</td>
                <td>10.5 kg (23 lb)</td>
                <td>0.45 m³ (15.9 cu ft)</td>
                <td>Interior non-bearing firewalls, pipe chases</td>
              </tr>
              <tr>
                <td>6 &times; 8 &times; 16 in (150 mm)</td>
                <td>5⅝ &times; 7⅝ &times; 15⅝ in</td>
                <td>13.8 kg (30 lb)</td>
                <td>0.70 m³ (24.7 cu ft)</td>
                <td>Light commercial perimeter, residential 1-story</td>
              </tr>
              <tr>
                <td>8 &times; 8 &times; 16 in (200 mm)</td>
                <td>7⅝ &times; 7⅝ &times; 15⅝ in</td>
                <td>16.3 kg (36 lb)</td>
                <td>0.95 m³ (33.5 cu ft)</td>
                <td>Standard multistory loadbearing, shear walls</td>
              </tr>
              <tr>
                <td>10 &times; 8 &times; 16 in (250 mm)</td>
                <td>9⅝ &times; 7⅝ &times; 15⅝ in</td>
                <td>19.5 kg (43 lb)</td>
                <td>1.20 m³ (42.4 cu ft)</td>
                <td>Industrial blast walls, deep earth retaining</td>
              </tr>
              <tr>
                <td>12 &times; 8 &times; 16 in (300 mm)</td>
                <td>11⅝ &times; 7⅝ &times; 15⅝ in</td>
                <td>23.1 kg (51 lb)</td>
                <td>1.45 m³ (51.2 cu ft)</td>
                <td>Heavy basement retaining walls, bridge abutments</td>
              </tr>
            </tbody>
          </table>

          <h2>Control Joint Spacing &amp; Thermal Movement Details</h2>
          <p>
            Because concrete masonry units undergo hydration shrinkage and thermal cycling, horizontal expansion and contraction must be accommodated. Continuous unreinforced block runs must incorporate vertical control joints (CJ) sealed with backer rod and elastomeric sealant at maximum intervals governed by <strong>NCMA TEK 10-2C</strong>:
          </p>
          <div class="formula-box">
            $$\text{Maximum Joint Spacing } S_{CJ} \le 1.5 \times H_{wall} \quad \text{and} \quad S_{CJ} \le 7.62\text{ m } (25\text{ ft})$$
          </div>
          <p>
            Furthermore, continuous prefabricated joint reinforcement (ladder-type or truss-type 9-gauge galvanized wire) should be embedded into horizontal bed joints every $16\text{ inches}$ ($400\text{ mm}$, every second course) to resist tensile shear stresses and prevent unsightly stair-step cracking.
          </p>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: Commercial Cold Storage Exterior Perimeter Wall</h3>
            <p><strong>Design Scenario:</strong> A commercial logistics warehouse requires a reinforced concrete masonry perimeter fire wall. The wall dimensions are $L = 18.0\text{ meters}$ in length and $H = 3.6\text{ meters}$ in clear height. The wall incorporates two overhead dock doors ($2.4\text{ m} \times 2.8\text{ m}$ each, totaling $A_{openings} = 13.44\text{ m}^2$). Structural plans mandate standard $8\times 8\times 16\text{ inch}$ ($200\text{ mm}$) loadbearing CMU blocks. Because of lateral hurricane wind loads, vertical cores must be grouted at $24\text{ inches}$ on-center ($600\text{ mm}$). With an $8\%$ cutting waste factor, calculate total blocks to purchase, Type S mortar bags, masonry sand, and core grout volume.</p>
            
            <p><strong>Step 1: Compute Gross, Deducted, and Net Wall Area</strong></p>
            <div class="formula-box">
              $$A_{gross} = 18.0\text{ m} \times 3.6\text{ m} = 64.80\text{ m}^2$$
              $$A_{net} = A_{gross} - A_{openings} = 64.80\text{ m}^2 - 13.44\text{ m}^2 = 51.36\text{ m}^2$$
            </div>

            <p><strong>Step 2: Determine Net and Gross Block Quantities</strong></p>
            <div class="formula-box">
              $$N_{net} = 51.36\text{ m}^2 \times 12.50\text{ blocks/m}^2 = 642\text{ blocks}$$
              $$N_{total} = \lceil 642 \times (1 + 0.08) \rceil = \lceil 642 \times 1.08 \rceil = \lceil 693.36 \rceil = 694\text{ Blocks}$$
            </div>

            <p><strong>Step 3: Estimate Mortar Cement and Masonry Sand</strong></p>
            <div class="formula-box">
              $$\text{Mortar Bags (80 lb / 36.3 kg)} = \frac{694}{33.0} \approx 21.03 \implies 21\text{ Bags of Type S Mortar}$$
              $$\text{Masonry Sand} = 694 \times 0.0030\text{ tonnes} = 2.08\text{ Metric Tonnes of Sand}$$
            </div>

            <p><strong>Step 4: Compute Concrete Core Grout Volume (@ 24" oc)</strong></p>
            <div class="formula-box">
              $$V_{grout} = 642 \text{ (net blocks)} \times 0.0063\text{ m}^3/\text{block} \approx 4.04\text{ m}^3 \quad (\approx 5.28\text{ cu yd})$$
            </div>
            <p>
              <strong>Procurement Recommendation:</strong> Order <strong>694 units</strong> of 8-inch CMU, <strong>21 bags</strong> of Type S cement, <strong>2.1 tonnes</strong> of masonry sand, and schedule <strong>$4.25\text{ m}^3$</strong> (including 5% pump line waste) of fine aggregate core-fill concrete grout.
            </p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Masonry &amp; Civil Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="block-calculator.html">Block Masonry Estimator</a></li>
            <li><a href="concrete-calculator.html">Concrete Volume Calculator</a></li>
            <li><a href="brick-calculator.html">Brick Masonry Calculator</a></li>
            <li><a href="rebar-calculator.html">Rebar Weight &amp; Grid Sizing</a></li>
            <li><a href="retaining-wall-calculator.html">Retaining Wall Sizing</a></li>
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
      const calcBtn = document.getElementById('calcCmuBtn');
      const resetBtn = document.getElementById('resetCmuBtn');
      const resultBox = document.getElementById('cmuResultBox');

      function calculateCMU() {
        const L = parseFloat(document.getElementById('wallLength').value);
        const H = parseFloat(document.getElementById('wallHeight').value);
        const A_openings = parseFloat(document.getElementById('openingArea').value) || 0;
        const blockW = parseInt(document.getElementById('blockSize').value);
        const groutMode = document.getElementById('groutSpacing').value;
        const wastePct = parseFloat(document.getElementById('wasteMargin').value) || 0;

        if (isNaN(L) || L <= 0 || isNaN(H) || H <= 0) {
          alert('Please enter valid positive dimensions for wall length and height.');
          return;
        }

        const A_gross = L * H;
        const A_net = Math.max(0.1, A_gross - A_openings);

        const BLOCKS_PER_M2 = 12.5; // Standard 8x8x16 modular block with 3/8" joint
        const netBlocks = A_net * BLOCKS_PER_M2;
        const totalBlocks = Math.ceil(netBlocks * (1 + wastePct / 100.0));

        // Mortar: approx 1 bag (80 lb) per 33 blocks
        const mortarBags = Math.ceil(totalBlocks / 33.0);
        const sandTonnes = totalBlocks * 0.0030;

        // Core grout volume per block based on width and spacing
        // Standard 8" solid is 0.0095 m3/block
        let unitGroutSolid = 0.0095;
        let blockWeightKg = 16.3;

        if (blockW === 4) { unitGroutSolid = 0.0045; blockWeightKg = 10.5; }
        else if (blockW === 6) { unitGroutSolid = 0.0070; blockWeightKg = 13.8; }
        else if (blockW === 8) { unitGroutSolid = 0.0095; blockWeightKg = 16.3; }
        else if (blockW === 10) { unitGroutSolid = 0.0120; blockWeightKg = 19.5; }
        else if (blockW === 12) { unitGroutSolid = 0.0145; blockWeightKg = 23.1; }

        let groutRatio = 0.0;
        if (groutMode === '100') groutRatio = 1.0;
        else if (groutMode === '16') groutRatio = 1.0;
        else if (groutMode === '24') groutRatio = 0.667;
        else if (groutMode === '32') groutRatio = 0.50;
        else if (groutMode === '48') groutRatio = 0.333;
        else groutRatio = 0.0;

        const totalGroutM3 = netBlocks * unitGroutSolid * groutRatio;
        const groutMassKg = totalGroutM3 * 2300.0; // standard grout density ~2300 kg/m3
        const mortarMassKg = mortarBags * 36.3 + sandTonnes * 1000.0;
        const totalWallMassKg = Math.round(netBlocks * blockWeightKg + mortarMassKg + groutMassKg);

        document.getElementById('resTotalBlocks').textContent = totalBlocks.toLocaleString();
        document.getElementById('resNetArea').textContent = A_net.toFixed(2);
        document.getElementById('resMortarBags').textContent = mortarBags.toLocaleString();
        document.getElementById('resSandTonnes').textContent = sandTonnes.toFixed(2);
        document.getElementById('resGroutVol').textContent = totalGroutM3.toFixed(2);
        document.getElementById('resWallMass').textContent = totalWallMassKg.toLocaleString();

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculateCMU);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
      });
      calculateCMU();
    });
  </script>
</body>
</html>
"""

TOOL_4_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Concrete Mix Ratio Calculator | ACI 211.1 Batch Proportioning</title>
  <meta name="description" content="Calculate concrete mix proportions (cement bags, sand, gravel &amp; water) for standard grades (M10, M15, M20, M25, M30) per ACI 211.1 &amp; IS 456.">
  <link rel="canonical" href="https://calchub.cloud/concrete-mix-ratio-calculator.html">
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
        "name": "Concrete Mix Ratio Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates volumetric and gravimetric concrete batch proportions (cement, sand, coarse aggregate, water) using dry volume expansion factors per ACI 211.1.",
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
            "name": "Why is a dry volume factor of 1.54 to 1.57 used when calculating concrete mix proportions?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "When dry ingredients (cement, sand, and coarse aggregates) are mixed with water, the fine particles fill the interstitial voids between larger stones. Consequently, the dry volume contracts by approximately 54% to 57%. Therefore, to produce 1.0 m³ of compacted wet concrete, approximately 1.54 m³ of dry materials must be batched."
            }
          },
          {
            "@type": "Question",
            "name": "What are the standard volumetric mix ratios for nominal concrete grades?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Standard nominal volumetric ratios (Cement : Sand : Aggregate) are: M10 (1:3:6) for lean sub-base blinding; M15 (1:2:4) for plain mass concrete and paths; M20 (1:1.5:3) for standard residential reinforced slabs and beams; and M25 (1:1:2) for heavy-duty columns and water-retaining structures."
            }
          },
          {
            "@type": "Question",
            "name": "How does the water-cement (w/c) ratio govern concrete compressive strength?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Per Abrams' Law, concrete compressive strength is inversely proportional to the water-cement ratio by weight. Lower w/c ratios (e.g., 0.40 to 0.45) produce high compressive strength and low capillary permeability, whereas higher w/c ratios (0.55 to 0.65) increase workability at the expense of strength and durability."
            }
          },
          {
            "@type": "Question",
            "name": "How many 50 kg bags of cement are required for 1 cubic meter of M20 (1:1.5:3) concrete?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For 1.0 m³ of M20 concrete (1:1.5:3, total parts = 5.5): Dry volume = 1.54 m³. Cement volume = 1.54 / 5.5 = 0.28 m³. Multiplying by cement bulk density (1440 kg/m³) gives 403.2 kg of cement, which equals approximately 8.06 standard 50-kg bags (or ~8.5 bags including 5% site wastage)."
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
      <span>Concrete Mix Ratio Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calculator-main">
        <div class="calc-header">
          <h1>Concrete Mix Ratio Calculator</h1>
          <p>Compute precise batch quantities of cement bags, fine sand, coarse gravel, and mixing water based on ACI 211.1 volumetric proportions.</p>
        </div>

        <div class="calculator-card">
          <form id="mixCalcForm" onsubmit="return false;">
            <div class="form-row">
              <div class="form-group">
                <label for="wetVolume">Wet Concrete Volume Required (m³):</label>
                <input type="number" id="wetVolume" value="5.0" step="0.1" min="0.1" required>
                <span class="hint">In-place compacted concrete volume</span>
              </div>
              <div class="form-group">
                <label for="concreteGrade">Concrete Grade / Nominal Ratio:</label>
                <select id="concreteGrade">
                  <option value="1:3:6">M10 (1 : 3 : 6) - Lean Concrete / Blinding Bed</option>
                  <option value="1:2:4">M15 (1 : 2 : 4) - Mass Concrete, Footpaths, Floors</option>
                  <option value="1:1.5:3" selected>M20 (1 : 1.5 : 3) - Standard Reinforced Concrete (RCC)</option>
                  <option value="1:1:2">M25 (1 : 1 : 2) - Heavy Beams, Columns, Retaining Walls</option>
                  <option value="custom">Custom Ratio (C : S : A)</option>
                </select>
              </div>
            </div>

            <div class="form-row" id="customRatioRow" style="display:none;">
              <div class="form-group">
                <label for="custCement">Cement Part:</label>
                <input type="number" id="custCement" value="1.0" step="0.1" min="0.1">
              </div>
              <div class="form-group">
                <label for="custSand">Sand (Fine Aggregate) Part:</label>
                <input type="number" id="custSand" value="2.0" step="0.1" min="0.1">
              </div>
              <div class="form-group">
                <label for="custAggregate">Coarse Stone Aggregate Part:</label>
                <input type="number" id="custAggregate" value="4.0" step="0.1" min="0.1">
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="waterCementRatio">Water-Cement (w/c) Ratio:</label>
                <input type="number" id="waterCementRatio" value="0.50" step="0.01" min="0.30" max="0.75" required>
                <span class="hint">Standard RCC range: 0.45 to 0.55 by weight</span>
              </div>
              <div class="form-group">
                <label for="mixWaste">Wastage &amp; Compaction Allowance (%):</label>
                <input type="number" id="mixWaste" value="5" step="1" min="0" max="20" required>
                <span class="hint">Accounts for transit spillage, formwork bulking</span>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcMixBtn">Calculate Concrete Batch</button>
              <button type="reset" class="btn btn-secondary" id="resetMixBtn">Reset</button>
            </div>
          </form>

          <div class="results-box" id="mixResultBox" style="display:none; margin-top:25px;">
            <h3>Batch Proportioning &amp; Material Quantities</h3>
            <div class="result-grid">
              <div class="result-tile highlight">
                <span class="result-label">Cement Quantity (50 kg Bags)</span>
                <span class="result-value" id="resCementBags">0</span>
                <span class="result-unit">Bags (~0 kg total)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Fine Aggregate (Sand)</span>
                <span class="result-value" id="resSandMass">0.00</span>
                <span class="result-unit">Metric Tonnes (~0.00 m³)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Coarse Gravel Aggregate</span>
                <span class="result-value" id="resStoneMass">0.00</span>
                <span class="result-unit">Metric Tonnes (~0.00 m³)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Mixing Water Required</span>
                <span class="result-value" id="resWaterLiters">0</span>
                <span class="result-unit">Liters (kg)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Calculated Dry Batch Volume</span>
                <span class="result-value" id="resDryVol">0.00</span>
                <span class="result-unit">m³ (Expansion Factor: 1.54)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Estimated Wet Batch Weight</span>
                <span class="result-value" id="resTotalWeight">0</span>
                <span class="result-unit">kg (~0.00 metric tons)</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Concrete Proportioning Fundamentals (ACI 211.1 &amp; IS 456)</h2>
          <p>
            Concrete is an artificial composite building material composed of a hydraulic binder (ordinary Portland cement), water, fine aggregate (clean masonry sand), and coarse aggregates (crushed gravel or granite rock). The fundamental objective of concrete mix design per <strong>ACI 211.1 (Standard Practice for Selecting Proportions for Normal, Heavyweight, and Mass Concrete)</strong> is to select the most economical proportions of materials that produce fresh concrete with the necessary workability and finishability, followed by hardened concrete satisfying specified compressive strength, durability, and low permeability.
          </p>
          <p>
            Standard nominal mixes rely on fixed volumetric batch proportions denoted as $(1 : X : Y)$, representing the ratio of <strong>Cement : Fine Aggregate (Sand) : Coarse Aggregate (Gravel)</strong>. For critical structural elements, mix design is determined through laboratory trial batches to optimize particle packing, aggregate gradation curves, and slump behavior.
          </p>

          <h2>The Dry Volume Expansion Factor (1.54 to 1.57 Multiplier)</h2>
          <p>
            A common source of under-ordering and structural site deficits is failure to account for aggregate void structure. Dry coarse stones and sand contain loose air voids ranging between $30\%$ and $40\%$ of their bulk volume. When water and micro-fine cement particles are introduced and the mixture is thoroughly mechanically agitated, the cement paste lubricates and fills these interstitial interstitial voids.
          </p>
          <p>
            As a direct physical consequence, the volume of fresh wet, fully compacted concrete is significantly smaller than the cumulative loose dry volumes of its individual constituents. Rigorous empirical civil engineering standards employ a <strong>dry volume conversion factor of 1.54 to 1.57</strong>:
          </p>
          <div class="formula-box">
            $$V_{dry} = V_{wet} \times 1.54 \quad \text{(or up to } 1.57 \text{ for angular crushed granite)}$$
          </div>
          <p>
            This means to cast exactly $1.0\text{ m}^3$ of in-place dense concrete slab or column, the batch plant must meter out $1.54\text{ m}^3$ of unmixed dry raw ingredients.
          </p>

          <h2>Mathematical Formulation for Component Volumes and Masses</h2>
          <p>
            Let a nominal concrete mix have proportions $c : s : a$ corresponding to cement, fine aggregate, and coarse aggregate respectively. Let the total ratio sum be $S_r = c + s + a$. For a specified wet volume $V_{wet}$ and site wastage allowance $W_{\%}$:
          </p>
          <div class="formula-box">
            $$V_{gross} = V_{wet} \times \left(1 + \frac{W_{\%}}{100}\right)$$
            $$V_{dry} = V_{gross} \times 1.54$$
          </div>
          <p>
            The volume and mass of each individual constituent are computed as:
          </p>
          <div class="formula-box">
            $$V_{cement} = \frac{c}{S_r} \times V_{dry} \implies M_{cement} = V_{cement} \times \rho_{cement} \quad (\rho_{cement} \approx 1440\text{ kg/m}^3)$$
            $$\text{Number of 50-kg Bags} = \frac{M_{cement}}{50\text{ kg}}$$
            $$V_{sand} = \frac{s}{S_r} \times V_{dry} \implies M_{sand} = V_{sand} \times \rho_{sand} \quad (\rho_{sand} \approx 1600\text{ kg/m}^3)$$
            $$V_{stone} = \frac{a}{S_r} \times V_{dry} \implies M_{stone} = V_{stone} \times \rho_{stone} \quad (\rho_{stone} \approx 1550\text{ kg/m}^3)$$
          </div>

          <h2>Water-Cement Ratio ($w/c$) &amp; Abrams' Compressive Strength Law</h2>
          <p>
            Formulated by Duff Abrams in 1918, <strong>Abrams' Law</strong> dictates that for given materials and curing conditions, the compressive strength of fully compacted concrete is strictly governed by the water-to-cement ratio by mass:
          </p>
          <div class="formula-box">
            $$f'_c = \frac{A}{B^{1.5 (w/c)}}$$
          </div>
          <p>
            Here, $A$ and $B$ are empirical empirical constants. While chemical hydration of Portland cement only requires approximately $0.23$ to $0.25$ parts of water by weight (with an additional $0.15$ bound in gel pores), such dry mixtures have zero workability without superplasticizers. Practical water-cement ratios range from:
          </p>
          <ul>
            <li><strong>Low w/c ($0.38 - 0.42$):</strong> High-strength concrete ($f'_c \ge 40\text{ MPa}$), prestressed bridge girders, marine structures exposed to chlorides.</li>
            <li><strong>Standard w/c ($0.45 - 0.50$):</strong> Commercial multi-story frames, foundation slabs, waterproof basements.</li>
            <li><strong>Medium w/c ($0.52 - 0.60$):</strong> Plain mass footings, non-structural blinding, residential pavements.</li>
          </ul>
          <p>
            The required volume of batch mixing water is calculated directly from total cement mass:
          </p>
          <div class="formula-box">
            $$W_{liters} = M_{cement}\text{ (kg)} \times (w/c)$$
          </div>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Concrete Grade</th>
                <th>Volumetric Ratio (C : S : A)</th>
                <th>28-Day Strength ($f_{ck}$)</th>
                <th>Typical w/c</th>
                <th>Cement Bags / m³</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>M10</td>
                <td>1 : 3 : 6</td>
                <td>10 MPa (1,450 psi)</td>
                <td>0.55 – 0.60</td>
                <td>~4.4 bags</td>
              </tr>
              <tr>
                <td>M15</td>
                <td>1 : 2 : 4</td>
                <td>15 MPa (2,175 psi)</td>
                <td>0.50 – 0.55</td>
                <td>~6.3 bags</td>
              </tr>
              <tr>
                <td>M20</td>
                <td>1 : 1.5 : 3</td>
                <td>20 MPa (2,900 psi)</td>
                <td>0.45 – 0.50</td>
                <td>~8.1 bags</td>
              </tr>
              <tr>
                <td>M25</td>
                <td>1 : 1 : 2</td>
                <td>25 MPa (3,625 psi)</td>
                <td>0.40 – 0.45</td>
                <td>~11.1 bags</td>
              </tr>
              <tr>
                <td>M30 / M35</td>
                <td>Designed Mix (ACI 211)</td>
                <td>30 – 35 MPa</td>
                <td>0.38 – 0.42</td>
                <td>~12.5 bags</td>
              </tr>
            </tbody>
          </table>

          <h2>Field Aggregate Bulking &amp; Moisture Corrections</h2>
          <p>
            When batching concrete on construction job sites by volume rather than mass, fine sand exhibits a critical physical phenomenon known as <strong>sand bulking</strong>. Surface tension in moisture films surrounding fine sand particles pushes them apart, causing a volumetric expansion of up to $20\%$ to $30\%$ at moisture contents of $4\%$ to $6\%$.
          </p>
          <p>
            If uncorrected, bulking causes severely lean, under-sanded, harsh concrete batches susceptible to honeycombing. Civil engineers must perform a simple field displacement test in a graduated cylinder to measure bulking percentage and proportionally increase the loose sand volume batched into the concrete mixer.
          </p>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: Casting a Ground Floor Reinforced Concrete Slab</h3>
            <p><strong>Design Scenario:</strong> An engineer is casting a continuous reinforced concrete slab for a multi-family residential building. The slab dimensions are $10.0\text{ m}$ in length, $8.0\text{ m}$ in width, and $0.15\text{ m}$ ($150\text{ mm}$) in uniform thickness. The structural drawings specify <strong>Grade M20</strong> concrete with nominal volumetric proportions $(1 : 1.5 : 3)$. The target water-cement ratio is specified as $w/c = 0.50$ by weight, and a standard site wastage and over-excavation allowance of $5\%$ is budgeted. Calculate the required quantities of 50-kg cement bags, sand tonnage, crushed stone tonnage, and mixing water.</p>
            
            <p><strong>Step 1: Compute Wet Compacted Concrete Volume ($V_{wet}$)</strong></p>
            <div class="formula-box">
              $$V_{net} = 10.0\text{ m} \times 8.0\text{ m} \times 0.15\text{ m} = 12.0\text{ m}^3$$
              $$V_{gross} = 12.0\text{ m}^3 \times (1 + 0.05) = 12.60\text{ m}^3$$
            </div>

            <p><strong>Step 2: Determine Required Total Dry Batch Volume ($V_{dry}$)</strong></p>
            <div class="formula-box">
              $$V_{dry} = V_{gross} \times 1.54 = 12.60\text{ m}^3 \times 1.54 = 19.404\text{ m}^3$$
            </div>

            <p><strong>Step 3: Proportion Cement, Sand, and Coarse Aggregate</strong></p>
            <p>For Grade M20 $(1 : 1.5 : 3)$, the sum of parts is $S_r = 1 + 1.5 + 3 = 5.5$.</p>
            <div class="formula-box">
              $$V_{cement} = \frac{1.0}{5.5} \times 19.404\text{ m}^3 = 3.528\text{ m}^3$$
              $$M_{cement} = 3.528\text{ m}^3 \times 1440\text{ kg/m}^3 = 5,080.32\text{ kg}$$
              $$\text{Number of 50-kg Cement Bags} = \frac{5,080.32}{50} \approx 101.6 \implies \mathbf{102\text{ Bags of Cement}}$$
            </div>

            <p><strong>Step 4: Compute Sand and Stone Quantities</strong></p>
            <div class="formula-box">
              $$V_{sand} = \frac{1.5}{5.5} \times 19.404\text{ m}^3 = 5.292\text{ m}^3 \implies M_{sand} = 5.292 \times 1600\text{ kg/m}^3 = 8,467\text{ kg} \ (\mathbf{8.47\text{ Tonnes}})$$
              $$V_{stone} = \frac{3.0}{5.5} \times 19.404\text{ m}^3 = 10.584\text{ m}^3 \implies M_{stone} = 10.584 \times 1550\text{ kg/m}^3 = 16,405\text{ kg} \ (\mathbf{16.41\text{ Tonnes}})$$
            </div>

            <p><strong>Step 5: Determine Required Mixing Water</strong></p>
            <div class="formula-box">
              $$W_{water} = M_{cement} \times (w/c) = 5,080.32\text{ kg} \times 0.50 = \mathbf{2,540\text{ Liters of Water}}$$
            </div>
            <p>
              <strong>Site Batch Summary:</strong> To cast the $12.0\text{ m}^3$ slab with zero shortage, the site manager must procure <strong>102 bags of cement</strong>, <strong>8.5 tonnes of sand</strong>, <strong>16.5 tonnes of crushed aggregate</strong>, and verify supply of <strong>2,540 liters of clean mixing water</strong>.
            </p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Civil &amp; Concrete Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="concrete-calculator.html">Concrete Volume Calculator</a></li>
            <li><a href="concrete-block-calculator.html">Concrete Block Estimator</a></li>
            <li><a href="rebar-calculator.html">Rebar Weight &amp; Grid Sizing</a></li>
            <li><a href="brick-calculator.html">Brick Masonry Calculator</a></li>
            <li><a href="block-calculator.html">Block Masonry Estimator</a></li>
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
      const calcBtn = document.getElementById('calcMixBtn');
      const resetBtn = document.getElementById('resetMixBtn');
      const resultBox = document.getElementById('mixResultBox');
      const gradeSelect = document.getElementById('concreteGrade');
      const customRow = document.getElementById('customRatioRow');

      gradeSelect.addEventListener('change', function() {
        if (this.value === 'custom') {
          customRow.style.display = 'flex';
        } else {
          customRow.style.display = 'none';
        }
      });

      function calculateMix() {
        const V_wet = parseFloat(document.getElementById('wetVolume').value);
        const gradeVal = gradeSelect.value;
        const wc = parseFloat(document.getElementById('waterCementRatio').value);
        const wastePct = parseFloat(document.getElementById('mixWaste').value) || 0;

        if (isNaN(V_wet) || V_wet <= 0 || isNaN(wc) || wc <= 0) {
          alert('Please enter valid positive numbers for concrete volume and water-cement ratio.');
          return;
        }

        let c = 1.0, s = 2.0, a = 4.0;
        if (gradeVal === '1:3:6') { c = 1.0; s = 3.0; a = 6.0; }
        else if (gradeVal === '1:2:4') { c = 1.0; s = 2.0; a = 4.0; }
        else if (gradeVal === '1:1.5:3') { c = 1.0; s = 1.5; a = 3.0; }
        else if (gradeVal === '1:1:2') { c = 1.0; s = 1.0; a = 2.0; }
        else if (gradeVal === 'custom') {
          c = parseFloat(document.getElementById('custCement').value) || 1.0;
          s = parseFloat(document.getElementById('custSand').value) || 2.0;
          a = parseFloat(document.getElementById('custAggregate').value) || 4.0;
        }

        const sumParts = c + s + a;
        const V_gross = V_wet * (1 + wastePct / 100.0);
        const DRY_FACTOR = 1.54;
        const V_dry = V_gross * DRY_FACTOR;

        const V_c = (c / sumParts) * V_dry;
        const V_s = (s / sumParts) * V_dry;
        const V_a = (a / sumParts) * V_dry;

        const DENSITY_CEMENT = 1440.0; // kg/m3
        const DENSITY_SAND = 1600.0;   // kg/m3
        const DENSITY_STONE = 1550.0;  // kg/m3

        const M_c = V_c * DENSITY_CEMENT;
        const M_s = V_s * DENSITY_SAND;
        const M_a = V_a * DENSITY_STONE;

        const cementBags = Math.ceil(M_c / 50.0);
        const sandTonnes = M_s / 1000.0;
        const stoneTonnes = M_a / 1000.0;
        const waterLiters = Math.round(M_c * wc);

        const totalBatchKg = Math.round(M_c + M_s + M_a + waterLiters);

        document.getElementById('resCementBags').textContent = cementBags.toLocaleString();
        document.getElementById('resSandMass').textContent = sandTonnes.toFixed(2);
        document.getElementById('resStoneMass').textContent = stoneTonnes.toFixed(2);
        document.getElementById('resWaterLiters').textContent = waterLiters.toLocaleString();
        document.getElementById('resDryVol').textContent = V_dry.toFixed(2);
        document.getElementById('resTotalWeight').textContent = totalBatchKg.toLocaleString();

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculateMix);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
        customRow.style.display = 'none';
      });
      calculateMix();
    });
  </script>
</body>
</html>
"""

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    path_cmu = os.path.join(base_dir, 'concrete-block-calculator.html')
    with open(path_cmu, 'w', encoding='utf-8') as f:
        f.write(TOOL_3_HTML.strip() + '\n')
    print("[PASS] concrete-block-calculator.html generated successfully!")

    path_mix = os.path.join(base_dir, 'concrete-mix-ratio-calculator.html')
    with open(path_mix, 'w', encoding='utf-8') as f:
        f.write(TOOL_4_HTML.strip() + '\n')
    print("[PASS] concrete-mix-ratio-calculator.html generated successfully!")

if __name__ == '__main__':
    main()
