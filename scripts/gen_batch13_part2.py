# -*- coding: utf-8 -*-
"""
Script to generate Batch 13 Part 2 tools:
3. paint-calculator.html
4. projectile-motion-calculator.html
"""
import os

TOOL_3_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Paint Calculator | Gallons, Liters &amp; Wall Coverage Estimator</title>
  <meta name="description" content="Calculate architectural wall paint gallons, liters, primer requirements, door/window opening deductions, and multi-coat coverage per MPI standards.">
  <link rel="canonical" href="https://calchub.cloud/paint-calculator.html">
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
        "name": "Paint Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates wall and ceiling paint volume (gallons and liters), primer coats, fenestration deductions, and container purchases per MPI guidelines.",
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
            "name": "How many square feet does one gallon of paint cover?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "As an industry standard per Master Painters Institute (MPI) standards, one US gallon (3.785 liters) of quality architectural acrylic latex paint covers between 350 and 400 square feet (32.5 to 37.2 m²) on smooth, primed drywall surfaces for a single coat."
            }
          },
          {
            "@type": "Question",
            "name": "How much paint should be deducted for doors and windows?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Standard architectural practice deducts 20 to 21 square feet (approx. 1.9 m²) for each standard interior door (3 ft x 7 ft), and 15 square feet (approx. 1.4 m²) for an average residential window (3 ft x 5 ft)."
            }
          },
          {
            "@type": "Question",
            "name": "When is a dedicated primer coat necessary?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A dedicated primer coat is mandatory on unpainted porous drywall, bare wood, patched joint compound, repaired masonry, when transitioning from oil-based to latex paint, or when making dramatic color changes (e.g., dark navy to white) to equalize substrate porosity and prevent flashing."
            }
          },
          {
            "@type": "Question",
            "name": "Why are two coats of paint recommended over a single heavy coat?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Two thinner coats cure faster and more uniformly without sagging or runs, ensuring complete opacity, even sheen distribution, enhanced scrub resistance, and long-term durability. A single excessively thick coat frequently wrinkles, cracks, and takes days to achieve full hardness."
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
      <span>Paint Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calculator-main">
        <div class="calc-header">
          <h1>Paint Calculator</h1>
          <p>Estimate paint gallons, liters, primer requirements, and can purchase quantities for walls and ceilings per MPI standards.</p>
        </div>

        <div class="calculator-card">
          <form id="paintForm" onsubmit="return false;">
            <div class="form-row">
              <div class="form-group">
                <label for="roomLengthFt">Room Length (feet):</label>
                <input type="number" id="roomLengthFt" value="18.0" step="0.5" min="1" required>
                <span class="hint">Longer wall dimension</span>
              </div>
              <div class="form-group">
                <label for="roomWidthFt">Room Width (feet):</label>
                <input type="number" id="roomWidthFt" value="14.0" step="0.5" min="1" required>
                <span class="hint">Shorter wall dimension</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="wallHeightFt">Wall Height (feet):</label>
                <input type="number" id="wallHeightFt" value="9.0" step="0.5" min="5" required>
                <span class="hint">Finished floor-to-ceiling height</span>
              </div>
              <div class="form-group">
                <label for="numCoats">Number of Topcoats:</label>
                <select id="numCoats">
                  <option value="1">1 Coat (Same Color Refresh)</option>
                  <option value="2" selected>2 Coats (Standard Quality / Color Change)</option>
                  <option value="3">3 Coats (Vibrant Red/Yellow or Deep Tint)</option>
                </select>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="numDoors">Number of Standard Doors (21 sq ft):</label>
                <input type="number" id="numDoors" value="2" step="1" min="0" required>
              </div>
              <div class="form-group">
                <label for="numWindows">Number of Standard Windows (15 sq ft):</label>
                <input type="number" id="numWindows" value="2" step="1" min="0" required>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="paintCeiling">Paint the Ceiling?</label>
                <select id="paintCeiling">
                  <option value="no" selected>No (Walls Only)</option>
                  <option value="yes">Yes (Include Ceiling Area)</option>
                </select>
              </div>
              <div class="form-group">
                <label for="includePrimer">Include Dedicated Primer Coat?</label>
                <select id="includePrimer">
                  <option value="yes" selected>Yes (1 Coat Primer on Drywall)</option>
                  <option value="no">No (Pre-primed / Paint+Primer in One)</option>
                </select>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="spreadRate">Coverage Spreading Rate (sq ft / gallon):</label>
                <input type="number" id="spreadRate" value="350" step="25" min="200" max="450" required>
                <span class="hint">Standard smooth walls: 350-400 sq ft/gal</span>
              </div>
              <div class="form-group">
                <label for="wasteMargin">Roller Stipple &amp; Waste Margin (%):</label>
                <input type="number" id="wasteMargin" value="10" step="1" min="0" max="25" required>
                <span class="hint">Recommended 10% for roller nap retention &amp; touch-ups</span>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcPaintBtn">Calculate Paint Volumes</button>
              <button type="reset" class="btn btn-secondary" id="resetPaintBtn">Reset</button>
            </div>
          </form>

          <div class="results-box" id="paintResultBox" style="display:none; margin-top:25px;">
            <h3>Architectural Coatings Bill of Quantities</h3>
            <div class="result-grid">
              <div class="result-tile highlight">
                <span class="result-label">Topcoat Paint to Buy</span>
                <span class="result-value" id="resPaintGallons">0</span>
                <span class="result-unit">Gallons (~0.0 Liters)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Net Surface Area</span>
                <span class="result-value" id="resNetArea">0</span>
                <span class="result-unit">sq ft (~0 m²)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Recommended Containers</span>
                <span class="result-value" id="resContainers">0 Cans</span>
                <span class="result-unit">1-Gal &amp; 5-Gal Pails</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Primer Coat Volume</span>
                <span class="result-value" id="resPrimerVol">0</span>
                <span class="result-unit">Gallons (~0.0 Liters)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Total Liquid Coating Mass</span>
                <span class="result-value" id="resPaintMass">0</span>
                <span class="result-unit">lbs (~0 kg)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Perimeter Trim Enamel</span>
                <span class="result-value" id="resTrimEnamel">0</span>
                <span class="result-unit">Quarts (~0.0 Liters)</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Architectural Coatings &amp; Spreading Rate Physics</h2>
          <p>
            Architectural coatings serve dual engineering imperatives: providing aesthetic color and sheen while sealing building envelopes against moisture absorption, atmospheric carbonation, bacterial mold colonization, and mechanical scuff abrasion.
          </p>
          <p>
            Formulated from synthetic polymer binders (such as $100\%$ acrylic resins, polyvinyl acetates, or alkyd oils), mineral opacifying pigments (titanium dioxide, $\text{TiO}_2$), and volatile carrier solvents (water or mineral spirits), paint coverage is governed by the <strong>Theoretical Spreading Rate (TSR)</strong> and <strong>Volume Solids Content ($VS_{\%}$)</strong>:
          </p>
          <div class="formula-box">
            $$\text{Theoretical Coverage (sq ft/gal)} = \frac{1,604 \times VS_{\%}}{\text{Dry Film Thickness (DFT, mils)}}$$
          </div>
          <p>
            Where $1\text{ mil} = 0.001\text{ inch} = 25.4\text{ }\mu\text{m}$. For a standard high-quality architectural acrylic latex with $38\%$ volume solids applied at a target dry film thickness of $1.5\text{ mils}$ ($38\text{ }\mu\text{m}$), the theoretical spreading rate is precisely $\frac{1604 \times 0.38}{1.5} \approx 406\text{ sq ft/gal}$ ($10.0\text{ m}^2/\text{L}$).
          </p>

          <h2>Net Surface Area Formulation and Fenestration Deductions</h2>
          <p>
            Accurate quantification requires calculating the gross perimeter wall envelope, adding ceilings when specified, and deducting door and window openings:
          </p>
          <div class="formula-box">
            $$A_{perimeter} = 2 \times (L + W) \times H$$
            $$A_{ceiling} = L \times W \quad (\text{if ceiling is painted})$$
            $$A_{deductions} = (N_{doors} \times 21.0\text{ sq ft}) + (N_{windows} \times 15.0\text{ sq ft})$$
            $$A_{net} = A_{perimeter} + A_{ceiling} - A_{deductions}$$
          </div>
          <p>
            Where $L, W, H$ are room length, width, and height in feet. In metric units, standard doors deduct $1.95\text{ m}^2$ and windows deduct $1.40\text{ m}^2$.
          </p>

          <h2>Multi-Coat Volumetric Requirements and Application Loss</h2>
          <p>
            To compute the total liquid volume of paint ($V_{paint}$) required for $N_{coats}$ over a net surface area $A_{net}$ with spreading rate $S_R$ ($350 - 400\text{ sq ft/gal}$) and application waste allowance $W_{\%}$:
          </p>
          <div class="formula-box">
            $$V_{theoretical} = \frac{A_{net} \times N_{coats}}{S_R}$$
            $$V_{paint} = V_{theoretical} \times \left(1 + \frac{W_{\%}}{100}\right)$$
          </div>
          <p>
            The application waste factor ($W_{\%}$) accounts for:
          </p>
          <ul>
            <li><strong>Roller Nap Retention:</strong> Synthetic roller sleeves retain $100\text{ to }200\text{ mL}$ of liquid paint trapped in the fibers after cleaning.</li>
            <li><strong>Wall Texture Absorption:</strong> Orange-peel, knockdown, or heavy plaster textures increase true micro-surface area by $15\%$ to $25\%$.</li>
            <li><strong>Airless Spray Atomization:</strong> Overspray and bounce-back losses account for $20\%$ to $35\%$ of material volume compared to direct roller application.</li>
          </ul>

          <h2>Substrate Porosity, Primers &amp; Flashing Prevention</h2>
          <p>
            A primer is not merely thinned paint; it is a high-solids, low-sheen binding resin engineered to penetrate porous substrates. Unprimed fresh gypsum drywall joint compound has high capillary suction, drinking moisture out of fresh latex paint. This produces an uneven, blotchy surface finish known as <strong>flashing</strong>.
          </p>
          <p>
            Under <strong>Master Painters Institute (MPI) Standard Architectural Specifications</strong>:
          </p>
          <ul>
            <li><strong>MPI #50 (Interior Latex Primer Sealer):</strong> Applied at $350\text{ sq ft/gal}$ on new drywall to seal joint compound mud and equalize porosity before topcoats.</li>
            <li><strong>MPI #107 (High-Performance Stain-Blocking Alkyd Primer):</strong> Formulated with fast-drying solvent resins to seal water stains, smoke soot, and tannin bleed from cedar/redwood knots.</li>
            <li><strong>MPI #3 (Masonry Bonding Primer):</strong> Alkali-resistant formulation engineered to withstand high surface pH ($pH > 10$) on fresh concrete and cement stucco.</li>
          </ul>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Paint Sheen Finish</th>
                <th>Specular Gloss @ 60°</th>
                <th>Standard Spread Rate</th>
                <th>Washability / Durability</th>
                <th>Recommended Application Area</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Flat / Matte</td>
                <td>0 – 5%</td>
                <td>350 – 400 sq ft/gal</td>
                <td>Low (diffuses light imperfections)</td>
                <td>Living room ceilings, master bedrooms</td>
              </tr>
              <tr>
                <td>Eggshell / Velvet</td>
                <td>10 – 25%</td>
                <td>350 – 400 sq ft/gal</td>
                <td>Moderate (wipeable)</td>
                <td>Bedrooms, dining rooms, home offices</td>
              </tr>
              <tr>
                <td>Satin / Pearl</td>
                <td>25 – 35%</td>
                <td>350 – 400 sq ft/gal</td>
                <td>High (scrubbable, moisture resistant)</td>
                <td>Hallways, family rooms, kids' play areas</td>
              </tr>
              <tr>
                <td>Semi-Gloss</td>
                <td>35 – 70%</td>
                <td>300 – 350 sq ft/gal</td>
                <td>Very High (stain &amp; water repellant)</td>
                <td>Kitchens, bathrooms, baseboards &amp; trim</td>
              </tr>
              <tr>
                <td>High-Gloss Enamel</td>
                <td>> 70%</td>
                <td>300 – 350 sq ft/gal</td>
                <td>Maximum (heavy impact &amp; chemical resistance)</td>
                <td>Cabinets, architectural millwork, metal doors</td>
              </tr>
            </tbody>
          </table>

          <h2>Dry Film Thickness (DFT) vs Wet Film Thickness (WFT) &amp; VOC Compliance</h2>
          <p>
            In professional architectural coatings, controlling coating thickness is essential to prevent premature coating degradation. When liquid paint is applied, volatile solvents evaporate during the curing reaction, leaving behind solid resin and pigment particles.
          </p>
          <p>
            The mathematical correlation between <strong>Wet Film Thickness (WFT)</strong> and <strong>Dry Film Thickness (DFT)</strong> is governed by the formulation volume solids percentage ($VS_{\%}$):
          </p>
          <div class="formula-box">
            $$\text{DFT} = \text{WFT} \times \left(\frac{VS_{\%}}{100}\right) \iff \text{WFT} = \frac{\text{DFT}}{VS_{\%}/100}$$
          </div>
          <p>
            Inspectors use a notched stainless steel wet film comb to measure fresh WFT immediately following roller application. For instance, to achieve a specified $1.8\text{ mil}$ ($46\text{ }\mu\text{m}$) cured DFT using an acrylic paint with $40\%$ volume solids, the painter must consistently gauge application at $\text{WFT} = \frac{1.8}{0.40} = 4.5\text{ mils}$ ($114\text{ }\mu\text{m}$).
          </p>
          <p>
            <strong>Volatile Organic Compounds (VOC) Limits:</strong> Environmental regulations (such as EPA Method 24 and SCAQMD Rule 1113) restrict VOC content to under $50\text{ g/L}$ for low-VOC paints and under $5\text{ g/L}$ for zero-VOC formulations, protecting indoor air quality without sacrificing scrub resistance.
          </p>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: Multi-Room Residential Repaint Fit-Out</h3>
            <p><strong>Design Scenario:</strong> A master bedroom suite measures $L = 20.0\text{ feet}$ in length, $W = 16.0\text{ feet}$ in width, with $H = 9.5\text{ feet}$ high ceilings. The project scope calls for painting both walls and the ceiling. The walls contain two entrance doors ($21.0\text{ sq ft}$ each) and three double-hung windows ($15.0\text{ sq ft}$ each). The owner is transitioning from dark burgundy to light eggshell beige, requiring one full coat of high-hide stain-blocking primer followed by two coats of premium acrylic eggshell latex ($350\text{ sq ft/gal}$ coverage). A standard $10\%$ roller application waste allowance is budgeted. Calculate net surface area, required gallons and liters of topcoat paint, primer gallons, and container purchasing breakdown.</p>
            
            <p><strong>Step 1: Compute Perimeter Wall, Ceiling, and Fenestration Areas</strong></p>
            <div class="formula-box">
              $$A_{walls} = 2 \times (20.0\text{ ft} + 16.0\text{ ft}) \times 9.5\text{ ft} = 2 \times 36.0 \times 9.5 = 684.0\text{ sq ft}$$
              $$A_{ceiling} = 20.0\text{ ft} \times 16.0\text{ ft} = 320.0\text{ sq ft}$$
              $$A_{deduct} = (2 \times 21.0\text{ sq ft}) + (3 \times 15.0\text{ sq ft}) = 42.0 + 45.0 = 87.0\text{ sq ft}$$
              $$A_{net} = 684.0 + 320.0 - 87.0 = \mathbf{917.0\text{ sq ft}} \quad (\approx 85.19\text{ m}^2)$$
            </div>

            <p><strong>Step 2: Determine Primer Volume (1 Coat @ 350 sq ft/gal with 10% Waste)</strong></p>
            <div class="formula-box">
              $$V_{primer} = \frac{917.0\text{ sq ft} \times 1.10}{350\text{ sq ft/gal}} = \frac{1,008.7}{350} \approx 2.88\text{ Gallons} \implies \mathbf{3\text{ One-Gallon Cans of Primer}}$$
            </div>

            <p><strong>Step 3: Determine Topcoat Paint Volume (2 Coats @ 350 sq ft/gal with 10% Waste)</strong></p>
            <div class="formula-box">
              $$V_{topcoat} = \frac{917.0\text{ sq ft} \times 2\text{ coats} \times 1.10}{350\text{ sq ft/gal}} = \frac{2,017.4}{350} \approx 5.76\text{ Gallons} \quad (\approx 21.8\text{ Liters})$$
            </div>

            <p><strong>Step 4: Formulate Retail Container Purchasing Strategy</strong></p>
            <p>
              To minimize purchase expense, the contractor purchases:
            </p>
            <div class="formula-box">
              $$\text{Order: One 5-Gallon Pail } + \text{ One 1-Gallon Can } = \mathbf{6\text{ Gallons Total Topcoat Paint}}$$
            </div>
            <p>
              <strong>Procurement Summary:</strong> Order <strong>one 5-gallon pail and one 1-gallon can</strong> of eggshell topcoat (6 gal total), plus <strong>three 1-gallon cans</strong> of primer sealer. This guarantees uniform coverage with sufficient touch-up reserves.
            </p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Building &amp; Finish Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="drywall-calculator.html">Drywall Sheets &amp; Mud Estimator</a></li>
            <li><a href="flooring-calculator.html">Flooring Area &amp; Box Estimator</a></li>
            <li><a href="brick-calculator.html">Brick Masonry Calculator</a></li>
            <li><a href="concrete-block-calculator.html">Concrete Block Estimator</a></li>
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
      const calcBtn = document.getElementById('calcPaintBtn');
      const resetBtn = document.getElementById('resetPaintBtn');
      const resultBox = document.getElementById('paintResultBox');

      function calculatePaint() {
        const L = parseFloat(document.getElementById('roomLengthFt').value);
        const W = parseFloat(document.getElementById('roomWidthFt').value);
        const H = parseFloat(document.getElementById('wallHeightFt').value);
        const coats = parseInt(document.getElementById('numCoats').value);
        const doors = parseInt(document.getElementById('numDoors').value) || 0;
        const windows = parseInt(document.getElementById('numWindows').value) || 0;
        const paintCeiling = document.getElementById('paintCeiling').value === 'yes';
        const includePrimer = document.getElementById('includePrimer').value === 'yes';
        const spreadRate = parseFloat(document.getElementById('spreadRate').value);
        const wastePct = parseFloat(document.getElementById('wasteMargin').value) || 0;

        if (isNaN(L) || L <= 0 || isNaN(W) || W <= 0 || isNaN(H) || H <= 0 || isNaN(spreadRate) || spreadRate <= 0) {
          alert('Please enter valid positive dimensions and spreading rate.');
          return;
        }

        const wallArea = 2.0 * (L + W) * H;
        const ceilingArea = paintCeiling ? (L * W) : 0;
        const deductions = (doors * 21.0) + (windows * 15.0);
        const netArea = Math.max(1.0, wallArea + ceilingArea - deductions);

        const totalAreaWithWaste = netArea * (1.0 + wastePct / 100.0);
        const topcoatGallons = (totalAreaWithWaste * coats) / spreadRate;
        const primerGallons = includePrimer ? (totalAreaWithWaste / spreadRate) : 0;

        const cansToBuy = Math.ceil(topcoatGallons);
        const topcoatLiters = topcoatGallons * 3.78541;
        const primerLiters = primerGallons * 3.78541;

        let containerText = '';
        if (cansToBuy >= 5) {
          const pails5 = Math.floor(cansToBuy / 5);
          const cans1 = cansToBuy % 5;
          containerText = `${pails5} × 5-Gal` + (cans1 > 0 ? ` + ${cans1} × 1-Gal` : '');
        } else {
          containerText = `${cansToBuy} × 1-Gal Cans`;
        }

        // Perimeter baseboard trim enamel: 2*(L+W) ft -> approx 1 quart per 100-150 LF
        const trimLF = 2.0 * (L + W);
        const trimQuarts = Math.max(1, Math.ceil(trimLF / 120.0));
        const trimLiters = trimQuarts * 0.946353;

        // Weight of paint: approx 11.5 lbs per gallon (latex acrylic)
        const totalMassLbs = Math.round((topcoatGallons + primerGallons) * 11.5);
        const totalMassKg = Math.round(totalMassLbs * 0.453592);
        const netAreaM2 = (netArea * 0.092903).toFixed(1);

        document.getElementById('resPaintGallons').textContent = topcoatGallons.toFixed(1) + ` (~${topcoatLiters.toFixed(1)} L)`;
        document.getElementById('resNetArea').textContent = Math.round(netArea).toLocaleString() + ` (~${netAreaM2} m²)`;
        document.getElementById('resContainers').textContent = containerText;
        document.getElementById('resPrimerVol').textContent = primerGallons > 0 ? (primerGallons.toFixed(1) + ` (~${primerLiters.toFixed(1)} L)`) : 'None Needed';
        document.getElementById('resPaintMass').textContent = totalMassLbs.toLocaleString() + ` (~${totalMassKg} kg)`;
        document.getElementById('resTrimEnamel').textContent = trimQuarts + ` Qts (~${trimLiters.toFixed(1)} L)`;

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculatePaint);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
      });
      calculatePaint();
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
  <title>Projectile Motion Calculator | 2D Kinematics Trajectory Sizer</title>
  <meta name="description" content="Calculate projectile motion trajectories: flight time, maximum apex height, horizontal range, and impact velocity per classical Newtonian kinematics.">
  <link rel="canonical" href="https://calchub.cloud/projectile-motion-calculator.html">
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
        "name": "Projectile Motion Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates 2D projectile kinematics: apex height, time of flight, horizontal range, impact velocity, and trajectory angles.",
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
            "name": "What angle gives the maximum horizontal range in projectile motion?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Over flat ground with equal launch and landing elevations (h0 = 0), a 45-degree launch angle achieves maximum horizontal range. When launched from an elevated cliff or platform (h0 > 0), the optimal launch angle for maximum range is slightly less than 45 degrees, governed by theta_opt = arcsin(1 / sqrt(2 + 2*g*h0 / v0^2))."
            }
          },
          {
            "@type": "Question",
            "name": "What is the formula for maximum trajectory height (apex)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The maximum vertical height reached above ground is: H_max = h0 + (v0 * sin(theta))^2 / (2 * g), where v0 is launch velocity, theta is launch angle, h0 is initial release height, and g is gravitational acceleration."
            }
          },
          {
            "@type": "Question",
            "name": "How is the total time of flight calculated when launched from an elevation?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "By solving the quadratic vertical kinematic equation y(t) = h0 + v0*sin(theta)*t - 0.5*g*t^2 = 0, the positive root yields: t_flight = [v0*sin(theta) + sqrt((v0*sin(theta))^2 + 2*g*h0)] / g."
            }
          },
          {
            "@type": "Question",
            "name": "How do horizontal and vertical velocity components behave in ideal projectile motion?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In the absence of aerodynamic drag, horizontal acceleration is zero (ax = 0), meaning horizontal velocity remains constant throughout flight: vx(t) = v0*cos(theta). Vertical velocity experiences constant downward gravitational acceleration (ay = -g), varying linearly as vy(t) = v0*sin(theta) - g*t."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="mechanical">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">
        <span class="logo-icon">&pi;</span>
        <span class="logo-text">Calc<strong>Hub</strong></span>
      </a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="engineering.html">Engineering</a>
        <a href="mechanical.html" class="active">Mechanical</a>
        <a href="civil.html">Civil &amp; Roof</a>
        <a href="solar-energy.html">Solar</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo; 
      <a href="mechanical.html">Mechanical &amp; Physics</a> &rsaquo; 
      <span>Projectile Motion Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calculator-main">
        <div class="calc-header">
          <h1>Projectile Motion Calculator</h1>
          <p>Compute 2D kinematic trajectories: apex height, time of flight, horizontal range, and impact velocity.</p>
        </div>

        <div class="calculator-card">
          <form id="projectileForm" onsubmit="return false;">
            <div class="form-row">
              <div class="form-group">
                <label for="initialVelocity">Initial Launch Velocity, v₀ (m/s):</label>
                <input type="number" id="initialVelocity" value="25.0" step="0.5" min="0.1" required>
                <span class="hint">Muzzle or release speed</span>
              </div>
              <div class="form-group">
                <label for="launchAngle">Launch Angle, &theta; (degrees):</label>
                <input type="number" id="launchAngle" value="45.0" step="0.5" min="0" max="90" required>
                <span class="hint">Angle relative to horizontal plane (0° to 90°)</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="initialHeight">Initial Release Height, h₀ (meters):</label>
                <input type="number" id="initialHeight" value="2.0" step="0.1" min="0" required>
                <span class="hint">Height above landing surface (0 for ground launch)</span>
              </div>
              <div class="form-group">
                <label for="gravityAccel">Gravitational Environment, g (m/s²):</label>
                <select id="gravityAccel">
                  <option value="9.80665" selected>Earth Standard (9.81 m/s²)</option>
                  <option value="1.62">Moon Surface (1.62 m/s²)</option>
                  <option value="3.71">Mars Surface (3.71 m/s²)</option>
                  <option value="24.79">Jupiter Cloud Top (24.79 m/s²)</option>
                </select>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcProjBtn">Calculate Trajectory</button>
              <button type="reset" class="btn btn-secondary" id="resetProjBtn">Reset</button>
            </div>
          </form>

          <div class="results-box" id="projectileResultBox" style="display:none; margin-top:25px;">
            <h3>Kinematic Trajectory Flight Parameters</h3>
            <div class="result-grid">
              <div class="result-tile highlight">
                <span class="result-label">Maximum Horizontal Range (R)</span>
                <span class="result-value" id="resRange">0.00</span>
                <span class="result-unit">meters (~0 ft)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Maximum Apex Height (H_max)</span>
                <span class="result-value" id="resApexHeight">0.00</span>
                <span class="result-unit">meters above datum</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Total Time of Flight (T)</span>
                <span class="result-value" id="resFlightTime">0.00</span>
                <span class="result-unit">seconds</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Final Impact Velocity (v_f)</span>
                <span class="result-value" id="resImpactVel">0.00</span>
                <span class="result-unit">m/s (~0 km/h)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Impact Angle (&theta;_f)</span>
                <span class="result-value" id="resImpactAngle">0.0°</span>
                <span class="result-unit">below horizontal</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Time to Reach Apex (t_apex)</span>
                <span class="result-value" id="resTimeApex">0.00</span>
                <span class="result-unit">seconds</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Classical Newtonian Projectile Kinematics in Two Dimensions</h2>
          <p>
            Projectile motion is the classical physics study of the curvilinear path followed by an unpowered object launched into a uniform gravitational field. First rigorously analyzed by Galileo Galilei in his 1638 treatise <em>Dialogues Concerning Two New Sciences</em>, projectile mechanics operates upon the fundamental principle of <strong>independence of orthogonal motion vectors</strong>: horizontal motion and vertical motion proceed simultaneously without cross-axial interference.
          </p>
          <p>
            In an ideal Newtonian reference frame (neglecting atmospheric aerodynamic drag and Coriolis planetary forces), the equations of motion are decoupled into horizontal ($x$) and vertical ($y$) components:
          </p>
          <div class="formula-box">
            $$a_x(t) = 0 \implies v_x(t) = v_0 \cos \theta = \text{constant}$$
            $$a_y(t) = -g \implies v_y(t) = v_0 \sin \theta - g \cdot t$$
          </div>

          <h2>Parametric Equations of the Parabolic Trajectory</h2>
          <p>
            Integrating the velocity equations with respect to time $t$ yields the instantaneous position coordinates $(x(t), y(t))$ relative to release origin $(0, h_0)$:
          </p>
          <div class="formula-box">
            $$x(t) = (v_0 \cos \theta) \cdot t$$
            $$y(t) = h_0 + (v_0 \sin \theta) \cdot t - \frac{1}{2} g \cdot t^2$$
          </div>
          <p>
            Eliminating time $t = \frac{x}{v_0 \cos \theta}$ between these parametric relations yields the explicit Cartesian equation of the trajectory path:
          </p>
          <div class="formula-box">
            $$y(x) = h_0 + (\tan \theta) \cdot x - \left[ \frac{g}{2 v_0^2 \cos^2 \theta} \right] \cdot x^2$$
          </div>
          <p>
            Because this equation takes the quadratic polynomial form $y = A x^2 + B x + C$ with negative leading coefficient $A < 0$, the spatial trajectory of any ideal projectile is an inverted parabola.
          </p>

          <h2>Apex Height and Time to Peak ($t_{apex}$)</h2>
          <p>
            At the exact apex of the flight path, the projectile momentarily ceases vertical ascent, meaning its instantaneous vertical velocity reaches zero:
          </p>
          <div class="formula-box">
            $$v_y(t_{apex}) = v_0 \sin \theta - g \cdot t_{apex} = 0 \implies t_{apex} = \frac{v_0 \sin \theta}{g}$$
          </div>
          <p>
            Substituting $t_{apex}$ into the vertical displacement equation gives the maximum height reached above the ground datum:
          </p>
          <div class="formula-box">
            $$H_{max} = h_0 + \frac{(v_0 \sin \theta)^2}{2 g}$$
          </div>

          <h2>Total Time of Flight ($T$) and Horizontal Range ($R$)</h2>
          <p>
            The projectile impacts the ground surface when its vertical coordinate returns to zero ($y(T) = 0$):
          </p>
          <div class="formula-box">
            $$0 = h_0 + (v_0 \sin \theta) \cdot T - \frac{1}{2} g \cdot T^2$$
          </div>
          <p>
            Applying the quadratic formula and selecting the positive real root gives the exact total flight duration:
          </p>
          <div class="formula-box">
            $$T = \frac{v_0 \sin \theta + \sqrt{(v_0 \sin \theta)^2 + 2 g h_0}}{g}$$
          </div>
          <p>
            When launching from level ground ($h_0 = 0$), this simplifies to the symmetric flight duration $T = \frac{2 v_0 \sin \theta}{g}$.
          </p>
          <p>
            The total horizontal distance covered (Range $R$) is the product of constant horizontal velocity and total flight duration:
          </p>
          <div class="formula-box">
            $$R = (v_0 \cos \theta) \cdot T = \frac{v_0 \cos \theta}{g} \left[ v_0 \sin \theta + \sqrt{(v_0 \sin \theta)^2 + 2 g h_0} \right]$$
          </div>
          <p>
            For level ground launches ($h_0 = 0$), trigonometric double-angle substitution ($2 \sin\theta \cos\theta = \sin 2\theta$) yields the famous classical range equation:
          </p>
          <div class="formula-box">
            $$R_{level} = \frac{v_0^2 \sin(2\theta)}{g}$$
          </div>

          <h2>Impact Velocity Vector ($v_f$) and Terminal Angle ($\theta_f$)</h2>
          <p>
            Upon impact at time $t = T$, the velocity vector possesses orthogonal components:
          </p>
          <div class="formula-box">
            $$v_{fx} = v_0 \cos \theta$$
            $$v_{fy} = v_0 \sin \theta - g \cdot T$$
            $$v_f = \sqrt{v_{fx}^2 + v_{fy}^2} = \sqrt{v_0^2 + 2 g h_0} \quad \text{(per Conservation of Mechanical Energy)}$$
            $$\theta_f = \arctan \left( \frac{|v_{fy}|}{v_{fx}} \right)$$
          </div>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Launch Scenario</th>
                <th>Optimal Angle for Range ($\theta_{opt}$)</th>
                <th>Flight Symmetry</th>
                <th>Impact Speed vs Launch Speed</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Level Ground ($h_0 = 0$)</td>
                <td>Exactly 45.0°</td>
                <td>Perfect Parabolic Symmetry ($t_{up} = t_{down}$)</td>
                <td>$v_f = v_0$ (Identical magnitude)</td>
              </tr>
              <tr>
                <td>Elevated Platform ($h_0 > 0$)</td>
                <td>$< 45.0^\circ$ ($\approx 35^\circ - 42^\circ$)</td>
                <td>Asymmetric ($t_{down} > t_{up}$)</td>
                <td>$v_f > v_0$ (Gain from potential energy)</td>
              </tr>
              <tr>
                <td>Depressed Target ($h_0 < 0$)</td>
                <td>$> 45.0^\circ$ ($\approx 48^\circ - 55^\circ$)</td>
                <td>Truncated descent</td>
                <td>$v_f < v_0$ (Loss to elevation gain)</td>
              </tr>
              <tr>
                <td>Vertical Launch ($\theta = 90^\circ$)</td>
                <td>N/A ($R = 0$)</td>
                <td>Pure 1D vertical oscillation</td>
                <td>$v_f = \sqrt{v_0^2 + 2 g h_0}$</td>
              </tr>
            </tbody>
          </table>

          <h2>Atmospheric Aerodynamic Drag &amp; Terminal Velocity Influences</h2>
          <p>
            While elementary Newtonian kinematics presumes vacuum flight, real-world projectiles traversing Earth's atmosphere experience significant opposing aerodynamic drag forces proportional to instantaneous velocity squared ($v^2$).
          </p>
          <p>
            The nonlinear hydrodynamic drag force is formulated per Rayleigh's equation:
          </p>
          <div class="formula-box">
            $$F_D = \frac{1}{2} C_d \rho A v^2$$
          </div>
          <p>
            Where $C_d$ is the drag coefficient (typically $0.47$ for smooth spheres), $\rho \approx 1.225\text{ kg/m}^3$ is sea-level air density, $A = \pi r^2$ is frontal cross-sectional area, and $v = \sqrt{v_x^2 + v_y^2}$ is instantaneous total speed.
          </p>
          <p>
            Under quadratic air resistance, the equations of motion become coupled non-linear differential equations:
          </p>
          <div class="formula-box">
            $$m \frac{d v_x}{dt} = - \frac{1}{2} C_d \rho A v v_x \quad \text{and} \quad m \frac{d v_y}{dt} = - m g - \frac{1}{2} C_d \rho A v v_y$$
          </div>
          <p>
            Atmospheric drag breaks the ideal parabolic symmetry: the descending branch becomes markedly steeper than the launch trajectory, the peak apex shifts downrange, and falling projectiles approach a finite vertical <strong>terminal velocity</strong>:
          </p>
          <div class="formula-box">
            $$v_t = \sqrt{\frac{2 m g}{C_d \rho A}}$$
          </div>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: Water Monitor Fire Cannon Trajectory</h3>
            <p><strong>Design Scenario:</strong> A marine firefighting tugboat uses a deck-mounted high-pressure monitor nozzle mounted $h_0 = 8.0\text{ meters}$ above sea level. The monitor discharges a solid water jet stream with an initial nozzle muzzle velocity of $v_0 = 40.0\text{ m/s}$ at an elevation angle of $\theta = 35.0^\circ$ above the horizontal. Assume standard Earth gravitational acceleration ($g = 9.80665\text{ m/s}^2$) and neglect aerodynamic water droplet breakup. Calculate the peak water stream apex height ($H_{max}$), total time of flight ($T$) until the water hits the sea surface, maximum horizontal reach ($R$), and final water impact velocity ($v_f$).</p>
            
            <p><strong>Step 1: Decompose Initial Velocity into Orthogonal Components</strong></p>
            <div class="formula-box">
              $$v_{0x} = v_0 \cos(35^\circ) = 40.0 \times 0.81915 = 32.766\text{ m/s}$$
              $$v_{0y} = v_0 \sin(35^\circ) = 40.0 \times 0.57358 = 22.943\text{ m/s}$$
            </div>

            <p><strong>Step 2: Determine Peak Apex Height ($H_{max}$)</strong></p>
            <div class="formula-box">
              $$t_{apex} = \frac{v_{0y}}{g} = \frac{22.943\text{ m/s}}{9.80665\text{ m/s}^2} \approx \mathbf{2.339\text{ seconds}}$$
              $$H_{max} = h_0 + \frac{v_{0y}^2}{2 g} = 8.0\text{ m} + \frac{(22.943)^2}{2 \times 9.80665} = 8.0 + 26.838 = \mathbf{34.84\text{ meters above sea level}}$$
            </div>

            <p><strong>Step 3: Calculate Total Flight Duration ($T$) to Sea Level</strong></p>
            <div class="formula-box">
              $$T = \frac{22.943 + \sqrt{(22.943)^2 + 2 \times 9.80665 \times 8.0}}{9.80665} = \frac{22.943 + \sqrt{526.38 + 156.91}}{9.80665}$$
              $$T = \frac{22.943 + \sqrt{683.29}}{9.80665} = \frac{22.943 + 26.140}{9.80665} = \frac{49.083}{9.80665} \approx \mathbf{5.005\text{ seconds}}$$
            </div>

            <p><strong>Step 4: Compute Maximum Horizontal Stream Reach ($R$)</strong></p>
            <div class="formula-box">
              $$R = v_{0x} \times T = 32.766\text{ m/s} \times 5.005\text{ s} \approx \mathbf{164.0\text{ meters}} \quad (\approx 538.1\text{ feet})$$
            </div>

            <p><strong>Step 5: Evaluate Final Impact Velocity ($v_f$)</strong></p>
            <div class="formula-box">
              $$v_f = \sqrt{v_0^2 + 2 g h_0} = \sqrt{(40.0)^2 + 2 \times 9.80665 \times 8.0} = \sqrt{1600 + 156.91} = \sqrt{1756.91} \approx \mathbf{41.92\text{ m/s}} \quad (\approx 150.9\text{ km/h})$$
            </div>
            <p>
              <strong>Engineering Conclusion:</strong> The water monitor delivers its stream to a maximum horizontal distance of <strong>$164.0\text{ meters}$</strong>, ascending to a clearance height of <strong>$34.84\text{ meters}$</strong>, and impacting burning vessels at an energetic velocity of <strong>$41.92\text{ m/s}$</strong>.
            </p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Mechanical &amp; Physics Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="flywheel-energy-calculator.html">Flywheel Kinetic Energy</a></li>
            <li><a href="reynolds-number-calculator.html">Reynolds Number Flow</a></li>
            <li><a href="cutting-speed-calculator.html">Cutting Speed &amp; Spindle RPM</a></li>
            <li><a href="torque-calculator.html">Torque &amp; Shaft Power</a></li>
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
      const calcBtn = document.getElementById('calcProjBtn');
      const resetBtn = document.getElementById('resetProjBtn');
      const resultBox = document.getElementById('projectileResultBox');

      function calculateProjectile() {
        const v0 = parseFloat(document.getElementById('initialVelocity').value);
        const thetaDeg = parseFloat(document.getElementById('launchAngle').value);
        const h0 = parseFloat(document.getElementById('initialHeight').value);
        const g = parseFloat(document.getElementById('gravityAccel').value);

        if (isNaN(v0) || v0 <= 0 || isNaN(thetaDeg) || thetaDeg < 0 || thetaDeg > 90 || isNaN(h0) || h0 < 0 || isNaN(g) || g <= 0) {
          alert('Please enter valid positive values for velocity, angle (0-90°), and initial height.');
          return;
        }

        const thetaRad = thetaDeg * (Math.PI / 180.0);
        const v0x = v0 * Math.cos(thetaRad);
        const v0y = v0 * Math.sin(thetaRad);

        const t_apex = v0y / g;
        const H_max = h0 + (Math.pow(v0y, 2) / (2.0 * g));

        // Quadratic formula for flight time T: 0.5*g*T^2 - v0y*T - h0 = 0
        const discriminant = Math.pow(v0y, 2) + 2.0 * g * h0;
        const T = (v0y + Math.sqrt(discriminant)) / g;

        const R = v0x * T;
        const vfx = v0x;
        const vfy = v0y - g * T; // negative value
        const vf = Math.sqrt(vfx * vfx + vfy * vfy);
        const impactAngleDeg = Math.atan2(Math.abs(vfy), vfx) * (180.0 / Math.PI);

        const rangeFt = (R * 3.28084).toFixed(1);
        const vfKmh = (vf * 3.6).toFixed(1);

        document.getElementById('resRange').textContent = R.toFixed(2) + ` (~${rangeFt} ft)`;
        document.getElementById('resApexHeight').textContent = H_max.toFixed(2);
        document.getElementById('resFlightTime').textContent = T.toFixed(3);
        document.getElementById('resImpactVel').textContent = vf.toFixed(2) + ` (~${vfKmh} km/h)`;
        document.getElementById('resImpactAngle').textContent = impactAngleDeg.toFixed(1) + '°';
        document.getElementById('resTimeApex').textContent = t_apex.toFixed(3);

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculateProjectile);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
      });
      calculateProjectile();
    });
  </script>
</body>
</html>
"""

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    path_paint = os.path.join(base_dir, 'paint-calculator.html')
    with open(path_paint, 'w', encoding='utf-8') as f:
        f.write(TOOL_3_HTML.strip() + '\n')
    print("[PASS] paint-calculator.html generated successfully!")

    path_proj = os.path.join(base_dir, 'projectile-motion-calculator.html')
    with open(path_proj, 'w', encoding='utf-8') as f:
        f.write(TOOL_4_HTML.strip() + '\n')
    print("[PASS] projectile-motion-calculator.html generated successfully!")

if __name__ == '__main__':
    main()
