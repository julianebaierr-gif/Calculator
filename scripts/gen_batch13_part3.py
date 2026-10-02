# -*- coding: utf-8 -*-
"""
Script to generate Batch 13 Part 3 tools:
5. rebar-weight-calculator.html
6. roof-pitch-calculator.html
"""
import os

TOOL_5_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Rebar Weight Calculator | Steel Bar Mass per Meter &amp; Foot</title>
  <meta name="description" content="Calculate reinforcing steel rebar weight per meter (d²/162) and per foot (d²/24), total tonnage, batch bundles, and ASTM A615 / BS 4449 bar sizes.">
  <link rel="canonical" href="https://calchub.cloud/rebar-weight-calculator.html">
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
        "name": "Rebar Weight Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates reinforcing steel deformed rebar linear mass, total tonnage, and bundle counts per ASTM A615 and ISO 6935.",
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
            "name": "What is the formula to calculate rebar weight per meter in metric units?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The standard metric formula for rebar linear mass is: Unit Weight (kg/m) = d² / 162.28, where d is the nominal diameter in millimeters. For example, a 16 mm bar weighs: (16 × 16) / 162.28 = 1.578 kg/m."
            }
          },
          {
            "@type": "Question",
            "name": "What is the formula to calculate rebar weight per foot in US Imperial units?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For US customary rebar sizes (#3 through #8), where the bar number represents eighths of an inch of diameter: Unit Weight (lb/ft) = (Bar Number)² / 24. For example, a #5 bar (5/8 inch) weighs: 5² / 24 = 25 / 24 ≈ 1.042 lb/ft."
            }
          },
          {
            "@type": "Question",
            "name": "How is the d²/162 formula derived from steel density?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The volume of a 1-meter cylinder of diameter d mm is V = (π / 4) * (d / 1000)² * 1.0 m = 7.854 × 10⁻⁷ * d² m³. Multiplying by standard steel density (7,850 kg/m³) yields: Mass = 7.854 × 10⁻⁷ * d² * 7850 = 0.006165 * d² = d² / (1 / 0.006165) = d² / 162.28 kg/m."
            }
          },
          {
            "@type": "Question",
            "name": "What cutting and bending waste percentage should be added when ordering rebar?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Structural engineering practice budgets 5% to 8% scrap waste for regular straight runs, footings, and slabs, and 10% to 12% for complex shear walls, column stirrup ties, and continuous beam lap splices per ACI 318."
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
      <span>Rebar Weight Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calculator-main">
        <div class="calc-header">
          <h1>Rebar Weight Calculator</h1>
          <p>Compute reinforcing steel bar linear mass (kg/m &amp; lb/ft), total tonnage, and bundle procurement per ASTM A615 &amp; ISO 6935.</p>
        </div>

        <div class="calculator-card">
          <form id="rebarForm" onsubmit="return false;">
            <div class="form-row">
              <div class="form-group">
                <label for="barStandard">Rebar Sizing Standard:</label>
                <select id="barStandard">
                  <option value="metric" selected>Metric System (ISO 6935 / BS 4449 - mm)</option>
                  <option value="us">US Imperial (ASTM A615 - # Bar Numbers)</option>
                </select>
              </div>
              <div class="form-group" id="grpMetricSize">
                <label for="rebarDiaMm">Nominal Diameter (mm):</label>
                <select id="rebarDiaMm">
                  <option value="6">6 mm (0.222 kg/m) - Light Mesh &amp; Links</option>
                  <option value="8">8 mm (0.395 kg/m) - Slab Temp &amp; Stirrups</option>
                  <option value="10">10 mm (0.617 kg/m) - Footings &amp; Slabs</option>
                  <option value="12" selected>12 mm (0.888 kg/m) - Main Slab / Beam Rebar</option>
                  <option value="16">16 mm (1.578 kg/m) - Primary Beam &amp; Column</option>
                  <option value="20">20 mm (2.466 kg/m) - Heavy Beams &amp; Columns</option>
                  <option value="25">25 mm (3.853 kg/m) - Foundation Piles &amp; Girders</option>
                  <option value="32">32 mm (6.313 kg/m) - Heavy Infrastructure &amp; Piers</option>
                  <option value="40">40 mm (9.865 kg/m) - High-Rise Core Walls</option>
                </select>
              </div>
              <div class="form-group" id="grpUsSize" style="display:none;">
                <label for="rebarUsNo">US Bar Size (#):</label>
                <select id="rebarUsNo">
                  <option value="3">#3 (3/8" - 0.376 lb/ft)</option>
                  <option value="4" selected>#4 (1/2" - 0.668 lb/ft)</option>
                  <option value="5">#5 (5/8" - 1.043 lb/ft)</option>
                  <option value="6">#6 (3/4" - 1.502 lb/ft)</option>
                  <option value="7">#7 (7/8" - 2.044 lb/ft)</option>
                  <option value="8">#8 (1" - 2.670 lb/ft)</option>
                  <option value="9">#9 (1-1/8" - 3.400 lb/ft)</option>
                  <option value="10">#10 (1-1/4" - 4.303 lb/ft)</option>
                  <option value="11">#11 (1-3/8" - 5.313 lb/ft)</option>
                </select>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="barLength">Length per Cut Bar (meters / feet):</label>
                <input type="number" id="barLength" value="12.0" step="0.5" min="0.1" required>
                <span class="hint">Standard mill stock length is 12m (40 ft)</span>
              </div>
              <div class="form-group">
                <label for="barQuantity">Total Number of Bars:</label>
                <input type="number" id="barQuantity" value="85" step="1" min="1" required>
                <span class="hint">Piece count from bar bending schedule (BBS)</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="scrapWaste">Cutting &amp; Lap Splice Waste (%):</label>
                <input type="number" id="scrapWaste" value="8" step="1" min="0" max="25" required>
                <span class="hint">Recommended 5% to 10% for lap splices and cut off-cuts</span>
              </div>
              <div class="form-group">
                <label for="unitPrice">Steel Price per Tonne ($ / Ton):</label>
                <input type="number" id="unitPrice" value="950" step="25" min="100">
                <span class="hint">Optional market material rate</span>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcRebarBtn">Calculate Steel Mass</button>
              <button type="reset" class="btn btn-secondary" id="resetRebarBtn">Reset</button>
            </div>
          </form>

          <div class="results-box" id="rebarResultBox" style="display:none; margin-top:25px;">
            <h3>Reinforcing Steel Takeoff Quantities</h3>
            <div class="result-grid">
              <div class="result-tile highlight">
                <span class="result-label">Total Steel Tonnage</span>
                <span class="result-value" id="resTonnage">0.000</span>
                <span class="result-unit">Metric Tonnes (~0 US tons)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Total Reinforcing Mass</span>
                <span class="result-value" id="resMassKg">0</span>
                <span class="result-unit">kg (~0 lbs)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Theoretical Unit Mass</span>
                <span class="result-value" id="resUnitWeight">0.000</span>
                <span class="result-unit">kg/m (~0.000 lb/ft)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Total Linear Length</span>
                <span class="result-value" id="resTotalLength">0.0</span>
                <span class="result-unit">meters (~0 ft with waste)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Mill Stock 12m (40ft) Bars</span>
                <span class="result-value" id="resMillBars">0</span>
                <span class="result-unit">Full Length Commercial Bars</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Estimated Material Cost</span>
                <span class="result-value" id="resCost">$0</span>
                <span class="result-unit">USD (excluding freight)</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Reinforcing Steel Technology &amp; Metallurgical Specifications</h2>
          <p>
            Reinforced concrete is a composite engineering system that exploits the immense compressive strength of hardened concrete and the high tensile yield capacity of deformed steel reinforcing bars (rebar). Because unreinforced plain concrete possesses a tensile strength of only approximately $8\%$ to $12\%$ of its compressive capacity ($f_{ct} \approx 0.62 \sqrt{f'_c}\text{ MPa}$), structural elements subjected to flexure, shear, and seismic torsion require steel reinforcement strategically embedded within tensile zones.
          </p>
          <p>
            Modern construction employs thermo-mechanically treated (TMT) high-yield deformed bars governed by international manufacturing standards:
          </p>
          <ul>
            <li><strong>ASTM A615:</strong> Standard specification for deformed and plain carbon-steel bars for concrete reinforcement, predominantly specified in Grade 60 ($F_y = 420\text{ MPa} / 60,000\text{ psi}$) and Grade 75 ($F_y = 520\text{ MPa}$).</li>
            <li><strong>ASTM A706:</strong> Low-alloy weldable deformed steel with controlled carbon equivalents ($\text{CE} \le 0.55\%$), mandatory for seismic moment frames per ACI 318 Chapter 18.</li>
            <li><strong>BS 4449 / EN 10080:</strong> European and British standard specifying Grade B500B and B500C high-ductility ribbed steel with a characteristic yield strength of $500\text{ MPa}$.</li>
          </ul>

          <h2>The Mathematical Derivation of Unit Rebar Mass</h2>
          <p>
            Civil engineers and steel estimators rely on simple empirical formulas for rapid site quantification. The metric formula $m = \frac{d^2}{162}$ is derived from the fundamental physical density of carbon steel ($\rho = 7,850\text{ kg/m}^3$):
          </p>
          <p>
            Consider a solid cylindrical steel bar of nominal diameter $d$ (in millimeters) and unit length $L = 1.0\text{ meter}$:
          </p>
          <div class="formula-box">
            $$V = \frac{\pi}{4} \times \left(\frac{d}{1000}\right)^2 \times 1.0\text{ m} = \frac{\pi}{4 \times 10^6} \cdot d^2 \text{ m}^3 \approx 7.85398 \times 10^{-7} \cdot d^2 \text{ m}^3$$
            $$m = V \times \rho = 7.85398 \times 10^{-7} \cdot d^2 \times 7850\text{ kg/m}^3 \approx 0.00616538 \cdot d^2\text{ kg/m}$$
            $$m = \frac{d^2}{1 / 0.00616538} = \frac{d^2}{162.196} \approx \frac{d^2}{\mathbf{162}}\text{ kg/m}$$
          </div>
          <p>
            Similarly, in US Imperial units, where bar diameter $D$ is expressed in eighths of an inch ($d_{in} = \frac{\#}{8}$):
          </p>
          <div class="formula-box">
            $$w = \frac{\#^2}{\mathbf{24}}\text{ lb/ft}$$
          </div>

          <h2>Total Tonnage Formulation &amp; Bar Bending Schedule (BBS)</h2>
          <p>
            In a structural Bar Bending Schedule (BBS), multiple cut lengths, bend hook shapes (standard $90^\circ$ and $135^\circ$ seismic hooks per ACI 318 Section 25.3), and lap splice lengths are consolidated:
          </p>
          <div class="formula-box">
            $$L_{net} = N_{bars} \times L_{cut}$$
            $$L_{gross} = L_{net} \times \left(1 + \frac{\text{Waste}_{\%}}{100}\right)$$
            $$M_{total} = L_{gross} \times \left(\frac{d^2}{162.28}\right)\text{ kg}$$
            $$\text{Metric Tonnes} = \frac{M_{total}}{1000} \quad \text{and} \quad \text{US Short Tons} = \frac{M_{total} \times 2.20462}{2000}$$
          </div>

          <h2>Tension Lap Splices &amp; Development Length Mechanics</h2>
          <p>
            Because commercial rebar is rolled in standard mill stock lengths (typically $12.0\text{ meters}$ in metric markets, or $40\text{ and }60\text{ feet}$ in US markets), continuous structural members require bars to be lapped or mechanically coupled.
          </p>
          <p>
            Under <strong>ACI 318-19 Section 25.4</strong>, the tension development length ($l_d$) transferred through rib deformations and surrounding concrete bond stress is:
          </p>
          <div class="formula-box">
            $$l_d = \left[ \frac{3}{40} \frac{F_y}{\lambda \sqrt{f'_c}} \frac{\psi_t \psi_e \psi_s \psi_g}{\left( \frac{c_b + K_{tr}}{d_b} \right)} \right] d_b$$
          </div>
          <p>
            For standard Grade 60 bars in normal-weight $25\text{ MPa}$ ($3,500\text{ psi}$) concrete, Class B tension lap splices typically evaluate to $40\text{ to }50$ bar diameters ($l_{lap} \approx 48 d_b$). For example, a $20\text{ mm}$ deformed bar requires a minimum lap splice length of approximately $48 \times 20\text{ mm} = 960\text{ mm}$ ($\approx 1.0\text{ meter}$).
          </p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Metric Bar Size (ISO)</th>
                <th>Equivalent US Size</th>
                <th>Nominal Area (mm²)</th>
                <th>Nominal Area (sq in)</th>
                <th>Unit Weight (kg/m)</th>
                <th>Unit Weight (lb/ft)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>8 mm</td>
                <td>#2.5 (approx)</td>
                <td>50.3 mm²</td>
                <td>0.078 in²</td>
                <td>0.395 kg/m</td>
                <td>0.265 lb/ft</td>
              </tr>
              <tr>
                <td>10 mm</td>
                <td>#3 (⅜")</td>
                <td>78.5 mm²</td>
                <td>0.110 in²</td>
                <td>0.617 kg/m</td>
                <td>0.414 lb/ft</td>
              </tr>
              <tr>
                <td>12 mm</td>
                <td>#4 (½")</td>
                <td>113.1 mm²</td>
                <td>0.200 in²</td>
                <td>0.888 kg/m</td>
                <td>0.597 lb/ft</td>
              </tr>
              <tr>
                <td>16 mm</td>
                <td>#5 (⅝")</td>
                <td>201.1 mm²</td>
                <td>0.310 in²</td>
                <td>1.578 kg/m</td>
                <td>1.060 lb/ft</td>
              </tr>
              <tr>
                <td>20 mm</td>
                <td>#6 (¾")</td>
                <td>314.2 mm²</td>
                <td>0.440 in²</td>
                <td>2.466 kg/m</td>
                <td>1.657 lb/ft</td>
              </tr>
              <tr>
                <td>25 mm</td>
                <td>#8 (1")</td>
                <td>490.9 mm²</td>
                <td>0.790 in²</td>
                <td>3.853 kg/m</td>
                <td>2.589 lb/ft</td>
              </tr>
              <tr>
                <td>32 mm</td>
                <td>#10 (1¼")</td>
                <td>804.2 mm²</td>
                <td>1.270 in²</td>
                <td>6.313 kg/m</td>
                <td>4.242 lb/ft</td>
              </tr>
            </tbody>
          </table>

          <h2>Corrosion Protection, Epoxy Coating (ASTM A775) &amp; Galvanized Rebar (ASTM A767)</h2>
          <p>
            In aggressive marine environments, bridge decks exposed to winter deicing chloride salts, and wastewater treatment plants, bare carbon steel rebar is prone to severe electrochemical corrosion. Chloride ion ingress depassivates the protective alkaline oxide film, oxidizing metallic iron into hydrated iron oxide (rust) with an expansive volume increase of up to $600\%$. This causes internal tensile splitting stresses, concrete cover spalling, and sudden structural delamination.
          </p>
          <p>
            To achieve extended 75- to 100-year design service lifespans under <strong>ACI 318 Chapter 19</strong>, specialized corrosion-resistant rebar specifications are mandated:
          </p>
          <ul>
            <li><strong>Fusion-Bonded Epoxy-Coated Rebar (ASTM A775 / A934):</strong> Electrostatic application of thermosetting epoxy powder creates a $7\text{ to }12\text{ mil}$ ($175 - 300\text{ }\mu\text{m}$) protective dielectric barrier preventing electrical corrosion currents.</li>
            <li><strong>Hot-Dip Galvanized Rebar (ASTM A767):</strong> Molten zinc immersion forms metallurgical zinc-iron alloy layers providing sacrificial galvanic protection even if physical scratches occur.</li>
            <li><strong>Stainless Steel Rebar (ASTM A955):</strong> Austenitic Type 316LN or duplex Type 2205 stainless steel with critical chloride threshold values over ten times higher than conventional black carbon steel.</li>
          </ul>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: Multi-Story Building Beam Rebar Procurement</h3>
            <p><strong>Design Scenario:</strong> A structural engineering schedule for a commercial podium deck details the primary bottom flexural tensile reinforcement for 12 continuous transfer beams. Each beam requires 6 bottom continuous deformed reinforcing bars of diameter $d = 20\text{ mm}$ ($F_y = 500\text{ MPa}$ TMT steel). The overall clear span plus column embedment hook length per bar is $L_{cut} = 14.5\text{ meters}$. A standard cutting, end-hook, and lap splice waste allowance of $8\%$ is specified. Steel reinforcement is procured at a contract price of $\$950\text{ per metric tonne}$. Calculate the total net linear meters, gross procurement weight in metric tonnes and US short tons, number of standard $12\text{-meter}$ commercial stock bars required, and estimated material procurement expenditure.</p>
            
            <p><strong>Step 1: Compute Total Number of Cut Bars and Net Length</strong></p>
            <div class="formula-box">
              $$N_{total} = 12\text{ beams} \times 6\text{ bars/beam} = \mathbf{72\text{ bars}}$$
              $$L_{net} = 72 \times 14.5\text{ m} = \mathbf{1,044.0\text{ linear meters}}$$
            </div>

            <p><strong>Step 2: Determine Gross Linear Length with 8% Scrap Waste</strong></p>
            <div class="formula-box">
              $$L_{gross} = 1,044.0\text{ m} \times (1 + 0.08) = 1,044.0 \times 1.08 = \mathbf{1,127.52\text{ linear meters}}$$
            </div>

            <p><strong>Step 3: Evaluate Unit Mass and Total Steel Weight ($d = 20\text{ mm}$)</strong></p>
            <div class="formula-box">
              $$m_{unit} = \frac{d^2}{162.28} = \frac{20^2}{162.28} = \frac{400}{162.28} \approx \mathbf{2.465\text{ kg/m}}$$
              $$M_{total} = 1,127.52\text{ m} \times 2.465\text{ kg/m} = \mathbf{2,779.34\text{ kg}}$$
              $$\text{Metric Tonnes} = \frac{2,779.34\text{ kg}}{1000} \approx \mathbf{2.779\text{ Tonnes}} \quad (\approx \mathbf{3.06\text{ US Short Tons}})$$
            </div>

            <p><strong>Step 4: Determine Commercial Mill Stock 12m Bars &amp; Budget</strong></p>
            <div class="formula-box">
              $$N_{12m\_bars} = \left\lceil \frac{1,127.52\text{ m}}{12.0\text{ m/bar}} \right\rceil = \lceil 93.96 \rceil = \mathbf{94\text{ Stock Bars of } 12\text{m}}$$
              $$\text{Procurement Cost} = 2.779\text{ tonnes} \times \$950/\text{tonne} = \mathbf{\$2,640.05\text{ USD}}$$
            </div>
            <p>
              <strong>Procurement Summary:</strong> The project manager must order <strong>94 commercial $12\text{m}$ stock bars</strong> of $20\text{ mm}$ TMT rebar ($2.78\text{ metric tonnes}$) with a purchase allocation of <strong>$\$2,640$</strong>.
            </p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Civil &amp; Structural Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="rebar-calculator.html">Rebar Weight &amp; Grid Sizing</a></li>
            <li><a href="concrete-calculator.html">Concrete Volume Calculator</a></li>
            <li><a href="footing-size-calculator.html">Footing Size &amp; Soil Bearing</a></li>
            <li><a href="beam-calculator.html">Beam Bending &amp; Shear</a></li>
            <li><a href="concrete-mix-ratio-calculator.html">Concrete Mix Ratio Proportions</a></li>
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
      const calcBtn = document.getElementById('calcRebarBtn');
      const resetBtn = document.getElementById('resetRebarBtn');
      const resultBox = document.getElementById('rebarResultBox');
      const stdSelect = document.getElementById('barStandard');
      const grpMetric = document.getElementById('grpMetricSize');
      const grpUs = document.getElementById('grpUsSize');

      stdSelect.addEventListener('change', function() {
        if (this.value === 'us') {
          grpMetric.style.display = 'none';
          grpUs.style.display = 'block';
        } else {
          grpMetric.style.display = 'block';
          grpUs.style.display = 'none';
        }
      });

      function calculateRebar() {
        const isUs = (stdSelect.value === 'us');
        const cutLen = parseFloat(document.getElementById('barLength').value);
        const qty = parseInt(document.getElementById('barQuantity').value);
        const wastePct = parseFloat(document.getElementById('scrapWaste').value) || 0;
        const pricePerTon = parseFloat(document.getElementById('unitPrice').value) || 0;

        if (isNaN(cutLen) || cutLen <= 0 || isNaN(qty) || qty <= 0) {
          alert('Please enter valid positive numbers for bar length and quantity.');
          return;
        }

        let unitWeightKgM = 0;
        let unitWeightLbFt = 0;

        if (isUs) {
          const usNo = parseInt(document.getElementById('rebarUsNo').value);
          // US weight: #3: 0.376, #4: 0.668, #5: 1.043, #6: 1.502, #7: 2.044, #8: 2.670, #9: 3.400, #10: 4.303, #11: 5.313 lb/ft
          const usTable = {
            3: 0.376, 4: 0.668, 5: 1.043, 6: 1.502, 7: 2.044, 8: 2.670, 9: 3.400, 10: 4.303, 11: 5.313
          };
          unitWeightLbFt = usTable[usNo] || 0.668;
          unitWeightKgM = unitWeightLbFt * 1.48816; // 1 lb/ft = 1.48816 kg/m
        } else {
          const diaMm = parseFloat(document.getElementById('rebarDiaMm').value);
          unitWeightKgM = (diaMm * diaMm) / 162.28;
          unitWeightLbFt = unitWeightKgM * 0.671969;
        }

        const netLength = cutLen * qty;
        const grossLength = netLength * (1.0 + wastePct / 100.0);
        const totalMassKg = Math.round(grossLength * unitWeightKgM);
        const totalMassLbs = Math.round(totalMassKg * 2.20462);
        const tonnesMetric = totalMassKg / 1000.0;
        const tonsUs = totalMassLbs / 2000.0;

        const stockBarLen = isUs ? 40.0 : 12.0;
        const fullStockBars = Math.ceil(grossLength / stockBarLen);
        const estCost = Math.round(tonnesMetric * pricePerTon);

        const lenFt = (grossLength * (isUs ? 1.0 : 3.28084)).toFixed(0);

        document.getElementById('resTonnage').textContent = tonnesMetric.toFixed(3) + ` (~${tonsUs.toFixed(3)} US tons)`;
        document.getElementById('resMassKg').textContent = totalMassKg.toLocaleString() + ` (~${totalMassLbs.toLocaleString()} lbs)`;
        document.getElementById('resUnitWeight').textContent = unitWeightKgM.toFixed(3) + ` (~${unitWeightLbFt.toFixed(3)} lb/ft)`;
        document.getElementById('resTotalLength').textContent = grossLength.toFixed(1) + ` m (~${lenFt} ft)`;
        document.getElementById('resMillBars').textContent = fullStockBars.toLocaleString();
        document.getElementById('resCost').textContent = '$' + estCost.toLocaleString();

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculateRebar);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
      });
      calculateRebar();
    });
  </script>
</body>
</html>
"""

TOOL_6_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Roof Pitch Calculator | Slope Angle, Rise &amp; Run, Rafter Length</title>
  <meta name="description" content="Calculate roof pitch (X:12), slope angle in degrees, pitch multiplier factor, true rafter length, and roofing material compatibility per IBC &amp; IRC.">
  <link rel="canonical" href="https://calchub.cloud/roof-pitch-calculator.html">
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
        "name": "Roof Pitch Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates roof pitch ratio (X:12), slope angle in degrees, rafter length, and pitch multiplier per IRC Chapter 9.",
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
            "name": "What does a 6:12 roof pitch mean?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A 6:12 roof pitch means that the roof surface rises 6 inches vertically for every 12 inches (1 foot) of horizontal run. This corresponds to a slope angle of approximately 26.57 degrees and a pitch multiplier factor of 1.118."
            }
          },
          {
            "@type": "Question",
            "name": "What is the formula to convert roof pitch to degrees?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The angle in degrees is calculated using the arctangent function: Angle (degrees) = arctan(Rise / Run) * (180 / π). For example, for an 8:12 pitch: arctan(8 / 12) = arctan(0.6667) ≈ 33.69 degrees."
            }
          },
          {
            "@type": "Question",
            "name": "What is a roof pitch multiplier factor?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The roof pitch multiplier is the secant of the roof angle: Multiplier = sqrt(1 + (Rise/Run)²) = sqrt(Rise² + 12²) / 12. Multiplying the horizontal flat footprint area of a house by this factor yields the true inclined surface area of the roof."
            }
          },
          {
            "@type": "Question",
            "name": "What is the minimum roof pitch for standard asphalt shingles?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Under International Residential Code (IRC R905.2.2), asphalt shingles require a minimum slope of 2:12 (9.46°). Slopes between 2:12 and 4:12 require double layers of underlayment, while standard single underlayment is permitted on 4:12 (18.43°) and steeper."
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
      <span>Roof Pitch Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calculator-main">
        <div class="calc-header">
          <h1>Roof Pitch Calculator</h1>
          <p>Compute roof pitch ratio (X:12), slope angle in degrees, pitch multiplier factor, and true rafter lengths per IRC Chapter 9.</p>
        </div>

        <div class="calculator-card">
          <form id="pitchForm" onsubmit="return false;">
            <div class="form-row">
              <div class="form-group">
                <label for="inputMethod">Pitch Input Mode:</label>
                <select id="inputMethod">
                  <option value="riseRun" selected>Enter Vertical Rise &amp; Horizontal Run</option>
                  <option value="pitchRatio">Select Standard Pitch (X : 12)</option>
                  <option value="degrees">Enter Slope Angle (Degrees)</option>
                </select>
              </div>
              <div class="form-group" id="grpPitchSelect" style="display:none;">
                <label for="pitchSelect">Standard Pitch (X:12):</label>
                <select id="pitchSelect">
                  <option value="2">2:12 (9.46°) - Low Slope Commercial</option>
                  <option value="3">3:12 (14.04°) - Low Slope Residential</option>
                  <option value="4">4:12 (18.43°) - Standard Ranch Style</option>
                  <option value="5">5:12 (22.62°) - Conventional Residential</option>
                  <option value="6" selected>6:12 (26.57°) - Most Common Gable</option>
                  <option value="7">7:12 (30.26°) - Moderate Slope</option>
                  <option value="8">8:12 (33.69°) - Traditional Colonial</option>
                  <option value="9">9:12 (36.87°) - Cape Cod Style</option>
                  <option value="10">10:12 (39.81°) - Steep Pitch</option>
                  <option value="12">12:12 (45.00°) - 45-Degree A-Frame</option>
                </select>
              </div>
            </div>

            <div class="form-row" id="rowRiseRun">
              <div class="form-group">
                <label for="roofRise">Vertical Rise (inches or mm):</label>
                <input type="number" id="roofRise" value="6.0" step="0.25" min="0.1" required>
                <span class="hint">Vertical height gain</span>
              </div>
              <div class="form-group">
                <label for="roofRun">Horizontal Run (inches or mm):</label>
                <input type="number" id="roofRun" value="12.0" step="0.5" min="1.0" required>
                <span class="hint">Standard reference run: 12 inches</span>
              </div>
            </div>

            <div class="form-row" id="rowDegrees" style="display:none;">
              <div class="form-group">
                <label for="roofAngleDeg">Roof Angle (degrees):</label>
                <input type="number" id="roofAngleDeg" value="26.57" step="0.1" min="1" max="85">
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="buildingSpan">Building Half-Span (Run in feet):</label>
                <input type="number" id="buildingSpan" value="16.0" step="0.5" min="1" required>
                <span class="hint">Distance from exterior wall plate to ridge centerline</span>
              </div>
              <div class="form-group">
                <label for="eaveOverhang">Eave Overhang (inches):</label>
                <input type="number" id="eaveOverhang" value="18" step="1" min="0" required>
                <span class="hint">Horizontal tail overhang beyond wall</span>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcPitchBtn">Calculate Roof Pitch</button>
              <button type="reset" class="btn btn-secondary" id="resetPitchBtn">Reset</button>
            </div>
          </form>

          <div class="results-box" id="pitchResultBox" style="display:none; margin-top:25px;">
            <h3>Roof Slope Geometry &amp; Rafter Lengths</h3>
            <div class="result-grid">
              <div class="result-tile highlight">
                <span class="result-label">Pitch Ratio (X : 12)</span>
                <span class="result-value" id="resPitchRatio">6.0 : 12</span>
                <span class="result-unit">Inches of Rise per Foot</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Roof Slope Angle (&theta;)</span>
                <span class="result-value" id="resAngleDeg">26.57°</span>
                <span class="result-unit">Degrees from Horizontal</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Pitch Multiplier Factor</span>
                <span class="result-value" id="resMultiplier">1.1180</span>
                <span class="result-unit">Surface Area Multiplier</span>
              </div>
              <div class="result-tile">
                <span class="result-label">True Rafter Length</span>
                <span class="result-value" id="resRafterLen">0.0 ft</span>
                <span class="result-unit">Plate to Ridge (~0.0 m)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Rafter with Overhang</span>
                <span class="result-value" id="resTotalRafter">0.0 ft</span>
                <span class="result-unit">Total Lumber Cut Length</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Grade Percentage (%)</span>
                <span class="result-value" id="resGradePct">50.0%</span>
                <span class="result-unit">Slope Gradient (Rise/Run)</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Roof Pitch Geometry &amp; Architectural Terminology</h2>
          <p>
            Roof pitch is the numerical measure of the steepness, incline, or slope of a roof structural plane. In architectural drafting, civil carpentry, and structural engineering, pitch dictates rain runoff velocity, snow load accumulation, wind uplift pressures, attic ventilation volume, and building envelope waterproofing requirements.
          </p>
          <p>
            Across North America, roof slope is universally expressed as a ratio of <strong>inches of vertical rise per 12 inches (1 foot) of horizontal run</strong>, written as $X:12$ or $X/12$. In European and international practice, roof incline is specified either as an angle in degrees ($\theta$) or as a percentage gradient ($\%$).
          </p>

          <h2>Mathematical Formulation: Pitch, Angle &amp; Multiplier</h2>
          <p>
            Given a vertical rise ($\Delta y$) and horizontal run ($\Delta x$):
          </p>
          <div class="formula-box">
            $$\text{Pitch Ratio } X = 12 \times \left(\frac{\Delta y}{\Delta x}\right)$$
            $$\text{Slope Angle } \theta = \arctan\left(\frac{\Delta y}{\Delta x}\right) \times \left(\frac{180}{\pi}\right)$$
            $$\text{Gradient Percentage } \% = \left(\frac{\Delta y}{\Delta x}\right) \times 100$$
          </div>
          <p>
            The <strong>Roof Pitch Multiplier (Secant Factor)</strong> converts two-dimensional horizontal building footprint area into actual three-dimensional inclined roof plane area:
          </p>
          <div class="formula-box">
            $$\text{Multiplier } M = \sec \theta = \frac{1}{\cos \theta} = \sqrt{1 + \left(\frac{X}{12}\right)^2} = \frac{\sqrt{X^2 + 144}}{12}$$
            $$\text{True Incline Surface Area} = \text{Horizontal Plan Footprint Area} \times M$$
          </div>

          <h2>Rafter Length Calculations per Pythagoras</h2>
          <p>
            For a common gable rafter spanning from the exterior wall top-plate to the central ridge beam over a horizontal half-span $S$:
          </p>
          <div class="formula-box">
            $$L_{span\_rafter} = S \times M = S \times \sqrt{1 + \left(\frac{X}{12}\right)^2}$$
          </div>
          <p>
            When adding a horizontal eave overhang $O_{in}$ (in inches, $O_{ft} = O_{in} / 12$):
          </p>
          <div class="formula-box">
            $$L_{overhang\_rafter} = O_{ft} \times M$$
            $$L_{total\_rafter} = L_{span\_rafter} + L_{overhang\_rafter} = (S + O_{ft}) \times M$$
          </div>

          <h2>Roofing Material Suitability per IRC Chapter 9</h2>
          <p>
            Building codes enforce minimum pitch thresholds to prevent wind-driven rain penetration:
          </p>
          <ul>
            <li><strong>Flat / Low-Slope Roofs ($< 2:12$ / $< 9.5^\circ$):</strong> Prohibited for asphalt shingles. Requires continuous sealed membrane roofing systems: EPDM rubber, TPO, PVC, or modified bitumen torch-down per IRC R905.9.</li>
            <li><strong>Low-Pitch Shingle Roofs ($2:12 \le \text{Pitch} < 4:12$):</strong> Permitted for asphalt shingles <em>only</em> if installed over two complete layers of ASTM D226 Type I asphalt-saturated organic felt underlayment, or continuous ice-and-water peel-and-stick membrane per IRC R905.2.2.</li>
            <li><strong>Conventional Slope ($4:12 \le \text{Pitch} \le 8:12$):</strong> The universal standard for residential gables, hips, and mansards. Standard single-ply synthetic underlayment with architectural dimensional shingles.</li>
            <li><strong>Steep-Slope Roofs ($> 9:12$ / $> 37^\circ$):</strong> Rapid shedding of precipitation and heavy snow. Ideal for natural slate, cedar shakes, standing-seam copper, and clay Spanish barrel tiles. Requires specialized high-nailing patterns (6 nails per shingle) for wind resistance up to $130\text{ mph}$.</li>
          </ul>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Pitch Ratio</th>
                <th>Slope Angle (&theta;)</th>
                <th>Pitch Multiplier</th>
                <th>Grade %</th>
                <th>Primary Building Style &amp; Suitability</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>2:12</td>
                <td>9.46°</td>
                <td>1.0138</td>
                <td>16.67%</td>
                <td>Commercial flat transitions, low-slope metal seams</td>
              </tr>
              <tr>
                <td>3:12</td>
                <td>14.04°</td>
                <td>1.0308</td>
                <td>25.00%</td>
                <td>Modern ranch extensions, double-felt shingles</td>
              </tr>
              <tr>
                <td>4:12</td>
                <td>18.43°</td>
                <td>1.0541</td>
                <td>33.33%</td>
                <td>Standard ranch homes, single underlayment threshold</td>
              </tr>
              <tr>
                <td>6:12</td>
                <td>26.57°</td>
                <td>1.1180</td>
                <td>50.00%</td>
                <td>Most popular residential gable &amp; hip pitch</td>
              </tr>
              <tr>
                <td>8:12</td>
                <td>33.69°</td>
                <td>1.2019</td>
                <td>66.67%</td>
                <td>Classic Colonial, Cape Cod, enhanced attic storage</td>
              </tr>
              <tr>
                <td>10:12</td>
                <td>39.81°</td>
                <td>1.3017</td>
                <td>83.33%</td>
                <td>Tudor architectural, dramatic snow shedding</td>
              </tr>
              <tr>
                <td>12:12</td>
                <td>45.00°</td>
                <td>1.4142</td>
                <td>100.00%</td>
                <td>Symmetric A-frame, equilateral triangular gables</td>
              </tr>
            </tbody>
          </table>

          <h2>Roof Truss Engineering, Wind Uplift Pressures &amp; Snow Load Reductions (ASCE 7)</h2>
          <p>
            Roof slope fundamentally alters the environmental aerodynamic and meteorological forces acting on a structural frame. Under <strong>ASCE 7 Minimum Design Loads and Associated Criteria for Buildings and Other Structures</strong>, roof pitch directly modulates both design wind pressures ($p = q_h G C_p$) and balanced ground snow load conversion factors ($C_s$).
          </p>
          <p>
            <strong>Aerodynamic Wind Uplift Behavior:</strong>
          </p>
          <ul>
            <li><strong>Low-Pitch Roofs ($\theta < 10^\circ$ / $< 2:12$):</strong> The entire roof surface acts as an aircraft wing airfoil subjected to severe net vertical suction (negative external pressure coefficient $C_p$ reaching $-0.9$ to $-1.3$ in perimeter and corner zones), demanding engineered hurricane metal ties at every rafter-to-wall plate connection.</li>
            <li><strong>Medium-Pitch Roofs ($10^\circ \le \theta \le 30^\circ$ / $2:12\text{ to }7:12$):</strong> Windward roof planes transition between net uplift and positive downward wind pressure depending on building enclosure classification.</li>
            <li><strong>Steep-Pitch Roofs ($\theta > 30^\circ$ / $> 7:12$):</strong> The windward slope experiences direct positive stagnation pressure acting downward, increasing vertical loads while sheltering the leeward plane in turbulent wake suction.</li>
          </ul>
          <p>
            <strong>Snow Load Slope Factor ($C_s$):</strong> On heated structures with slippery standing seam metal surfaces, snow slides off spontaneously at steep angles. ASCE 7 permits reduction of roof snow load ($p_s = C_s p_f$) where the slope factor drops from $C_s = 1.0$ at $\theta = 15^\circ$ down to $C_s = 0$ (zero design snow load) at angles exceeding $70^\circ$.
          </p>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: Framing a Residential 6:12 Gable Rafter</h3>
            <p><strong>Design Scenario:</strong> A timber residential home has an exterior building clear span of $32.0\text{ feet}$ (giving a half-span run of $S = 16.0\text{ feet}$ to the central ridge board). The architectural plans specify a <strong>6:12 pitch</strong> with an exterior horizontal eave overhang of $O = 18\text{ inches}$ ($1.5\text{ feet}$). Calculate the slope angle in degrees, the roof pitch multiplier factor, the theoretical rafter line length from wall plate to ridge, the total lumber cut length including eave overhang, and total true roof area if the building is $40.0\text{ feet}$ long.</p>
            
            <p><strong>Step 1: Compute Slope Angle (&theta;) and Pitch Multiplier ($M$)</strong></p>
            <div class="formula-box">
              $$\theta = \arctan\left(\frac{6}{12}\right) = \arctan(0.50) \approx \mathbf{26.57^\circ}$$
              $$M = \sqrt{1 + (6/12)^2} = \sqrt{1 + 0.25} = \sqrt{1.25} \approx \mathbf{1.11803}$$
            </div>

            <p><strong>Step 2: Calculate Line Rafter Length (Wall Plate to Ridge)</strong></p>
            <div class="formula-box">
              $$L_{span\_rafter} = S \times M = 16.0\text{ ft} \times 1.11803 = \mathbf{17.89\text{ feet}} \quad (17\text{ ft } 10\frac{11}{16}\text{ in} \approx 5.45\text{ m})$$
            </div>

            <p><strong>Step 3: Calculate Total Rafter Length Including Eave Overhang</strong></p>
            <div class="formula-box">
              $$S_{total} = S + O_{ft} = 16.0\text{ ft} + 1.5\text{ ft} = 17.5\text{ ft}$$
              $$L_{total\_rafter} = 17.5\text{ ft} \times 1.11803 = \mathbf{19.57\text{ feet}} \quad (19\text{ ft } 6\frac{13}{16}\text{ in} \approx 5.96\text{ m})$$
            </div>
            <p>The framer will specify standard $20\text{-foot}$ $2\times 8$ or $2\times 10$ lumber for the rafters.</p>

            <p><strong>Step 4: Compute True Inclined Roofing Shingle Area</strong></p>
            <div class="formula-box">
              $$A_{horizontal} = (32.0\text{ ft} + 2 \times 1.5\text{ ft}) \times (40.0\text{ ft} + 2 \times 1.0\text{ ft rake}) = 35.0\text{ ft} \times 42.0\text{ ft} = 1,470\text{ sq ft}$$
              $$A_{true\_roof} = A_{horizontal} \times M = 1,470\text{ sq ft} \times 1.11803 = \mathbf{1,643.5\text{ sq ft}} \quad (\approx 16.44\text{ Roofing Squares})$$
            </div>
            <p>
              <strong>Carpentry Summary:</strong> Rafter stock requires ordering <strong>$20\text{-foot}$ dimensional lumber</strong> to yield the $19.57\text{ ft}$ finished cut length, and ordering <strong>$17\text{ squares}$</strong> of architectural asphalt shingles.
            </p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Civil &amp; Framing Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="beam-calculator.html">Beam Bending &amp; Shear</a></li>
            <li><a href="rainwater-downpipe-calculator.html">Rainwater Downpipe Sizing</a></li>
            <li><a href="drywall-calculator.html">Drywall Sheets &amp; Mud</a></li>
            <li><a href="concrete-calculator.html">Concrete Volume Calculator</a></li>
            <li><a href="rebar-weight-calculator.html">Rebar Weight Estimator</a></li>
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
      const calcBtn = document.getElementById('calcPitchBtn');
      const resetBtn = document.getElementById('resetPitchBtn');
      const resultBox = document.getElementById('pitchResultBox');
      const methodSelect = document.getElementById('inputMethod');
      const rowRiseRun = document.getElementById('rowRiseRun');
      const grpPitch = document.getElementById('grpPitchSelect');
      const rowDeg = document.getElementById('rowDegrees');

      methodSelect.addEventListener('change', function() {
        const val = this.value;
        rowRiseRun.style.display = (val === 'riseRun') ? 'flex' : 'none';
        grpPitch.style.display = (val === 'pitchRatio') ? 'block' : 'none';
        rowDeg.style.display = (val === 'degrees') ? 'flex' : 'none';
      });

      function calculatePitch() {
        const method = methodSelect.value;
        const halfSpanFt = parseFloat(document.getElementById('buildingSpan').value);
        const overhangIn = parseFloat(document.getElementById('eaveOverhang').value) || 0;

        if (isNaN(halfSpanFt) || halfSpanFt <= 0) {
          alert('Please enter a valid positive building span.');
          return;
        }

        let rise = 6.0;
        let run = 12.0;

        if (method === 'riseRun') {
          rise = parseFloat(document.getElementById('roofRise').value);
          run = parseFloat(document.getElementById('roofRun').value);
          if (isNaN(rise) || rise <= 0 || isNaN(run) || run <= 0) {
            alert('Please enter valid positive numbers for rise and run.');
            return;
          }
        } else if (method === 'pitchRatio') {
          rise = parseFloat(document.getElementById('pitchSelect').value);
          run = 12.0;
        } else if (method === 'degrees') {
          const deg = parseFloat(document.getElementById('roofAngleDeg').value);
          if (isNaN(deg) || deg <= 0 || deg >= 90) {
            alert('Please enter a valid angle between 1° and 89°.');
            return;
          }
          const rad = deg * (Math.PI / 180.0);
          run = 12.0;
          rise = 12.0 * Math.tan(rad);
        }

        const pitchX = (rise / run) * 12.0;
        const angleRad = Math.atan(rise / run);
        const angleDeg = angleRad * (180.0 / Math.PI);
        const multiplier = Math.sqrt(1.0 + Math.pow(rise / run, 2));
        const gradePct = (rise / run) * 100.0;

        const rafterSpanFt = halfSpanFt * multiplier;
        const overhangFt = overhangIn / 12.0;
        const rafterTotalFt = (halfSpanFt + overhangFt) * multiplier;

        const rafterSpanM = (rafterSpanFt * 0.3048).toFixed(2);
        const rafterTotalM = (rafterTotalFt * 0.3048).toFixed(2);

        document.getElementById('resPitchRatio').textContent = pitchX.toFixed(2) + ' : 12';
        document.getElementById('resAngleDeg').textContent = angleDeg.toFixed(2) + '°';
        document.getElementById('resMultiplier').textContent = multiplier.toFixed(4);
        document.getElementById('resRafterLen').textContent = rafterSpanFt.toFixed(2) + ` ft (~${rafterSpanM} m)`;
        document.getElementById('resTotalRafter').textContent = rafterTotalFt.toFixed(2) + ` ft (~${rafterTotalM} m)`;
        document.getElementById('resGradePct').textContent = gradePct.toFixed(1) + '%';

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculatePitch);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
        methodSelect.value = 'riseRun';
        rowRiseRun.style.display = 'flex';
        grpPitch.style.display = 'none';
        rowDeg.style.display = 'none';
      });
      calculatePitch();
    });
  </script>
</body>
</html>
"""

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    path_rebar = os.path.join(base_dir, 'rebar-weight-calculator.html')
    with open(path_rebar, 'w', encoding='utf-8') as f:
        f.write(TOOL_5_HTML.strip() + '\n')
    print("[PASS] rebar-weight-calculator.html generated successfully!")

    path_pitch = os.path.join(base_dir, 'roof-pitch-calculator.html')
    with open(path_pitch, 'w', encoding='utf-8') as f:
        f.write(TOOL_6_HTML.strip() + '\n')
    print("[PASS] roof-pitch-calculator.html generated successfully!")

if __name__ == '__main__':
    main()
