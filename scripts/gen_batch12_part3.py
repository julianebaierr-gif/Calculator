# -*- coding: utf-8 -*-
"""
Script to generate Batch 12 Part 3 tools:
5. drywall-calculator.html
6. excavation-calculator.html
"""
import os

TOOL_5_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Drywall Calculator | Sheets, Joint Compound Mud &amp; Tape Estimator</title>
  <meta name="description" content="Calculate gypsum drywall sheets (4x8, 4x12), joint compound mud buckets, paper tape linear feet, and drywall screws per ASTM C840 finish specifications.">
  <link rel="canonical" href="https://calchub.cloud/drywall-calculator.html">
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
        "name": "Drywall Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates drywall panel sheets (4x8, 4x10, 4x12), ready-mix joint compound gallons, joint tape rolls, and screw counts per ASTM C840.",
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
            "name": "How many drywall sheets are required for a room?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Calculate the perimeter walls area (2 * (Length + Width) * Height) plus ceiling area (Length * Width). Subtract window and door openings. Divide the net surface area by the sheet area (32 sq ft for 4x8, 40 sq ft for 4x10, 48 sq ft for 4x12) and multiply by a 10% to 15% cutting waste factor."
            }
          },
          {
            "@type": "Question",
            "name": "How much joint compound (mud) and tape is needed per sheet of drywall?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "As an industry standard per ASTM C840, 100 sq ft of drywall requires approximately 0.053 gallons (or 5.3 gallons per 1,000 sq ft) of joint compound for a Level 4 finish (embed, fill, finish coats), along with 37 linear feet of paper joint tape per 100 sq ft."
            }
          },
          {
            "@type": "Question",
            "name": "How many drywall screws are needed per 4x8 sheet?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For 16-inch on-center framing spacing, building codes require drywall screws spaced 12 inches apart on ceilings and 16 inches apart on walls, requiring approximately 32 to 36 screws per 4x8 sheet, or roughly one 5-lb box (approx. 1,000 screws) for every 28 to 30 sheets."
            }
          },
          {
            "@type": "Question",
            "name": "When should 5/8-inch Type X drywall be used instead of standard 1/2-inch boards?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "5/8-inch Type X gypsum board contains special non-combustible glass fibers in its core that provide a 1-hour fire-resistance rating per ASTM E119. Building codes mandate Type X for garage-to-house separation walls, furnace rooms, multi-family party walls, and commercial corridor assemblies."
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
      <span>Drywall Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calculator-main">
        <div class="calc-header">
          <h1>Drywall Calculator</h1>
          <p>Estimate gypsum drywall sheets, joint compound mud buckets, paper tape rolls, and screw counts per ASTM C840 finish standards.</p>
        </div>

        <div class="calculator-card">
          <form id="drywallForm" onsubmit="return false;">
            <div class="form-row">
              <div class="form-group">
                <label for="roomLength">Room Length (feet):</label>
                <input type="number" id="roomLength" value="20.0" step="0.5" min="1" required>
                <span class="hint">Longer room dimension</span>
              </div>
              <div class="form-group">
                <label for="roomWidth">Room Width (feet):</label>
                <input type="number" id="roomWidth" value="14.0" step="0.5" min="1" required>
                <span class="hint">Shorter room dimension</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="ceilingHeight">Ceiling Height (feet):</label>
                <input type="number" id="ceilingHeight" value="9.0" step="0.5" min="5" required>
                <span class="hint">Floor to joist/truss height (e.g. 8, 9, 10 ft)</span>
              </div>
              <div class="form-group">
                <label for="sheetSize">Drywall Panel Sheet Size:</label>
                <select id="sheetSize">
                  <option value="32" selected>4' &times; 8' (32 sq ft) - Standard DIY &amp; Remodel</option>
                  <option value="40">4' &times; 10' (40 sq ft) - 10-ft Walls</option>
                  <option value="48">4' &times; 12' (48 sq ft) - Professional Commercial</option>
                  <option value="54">4.5' &times; 12' (54 sq ft) - 9-ft Ceiling Stretch Board</option>
                </select>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="openingDeduction">Deduction for Doors &amp; Windows (sq ft):</label>
                <input type="number" id="openingDeduction" value="65.0" step="5" min="0" required>
                <span class="hint">Average interior door ~21 sq ft, window ~15 sq ft</span>
              </div>
              <div class="form-group">
                <label for="includeCeiling">Include Ceiling Drywall?</label>
                <select id="includeCeiling">
                  <option value="yes" selected>Yes (Walls + Ceiling)</option>
                  <option value="no">No (Walls Only)</option>
                </select>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="wasteFactor">Cutting &amp; Corner Waste (%):</label>
                <input type="number" id="wasteFactor" value="10" step="1" min="0" max="25" required>
                <span class="hint">Recommended 10% for simple rooms, 15% for complex layouts</span>
              </div>
              <div class="form-group">
                <label for="finishLevel">ASTM C840 Finish Level:</label>
                <select id="finishLevel">
                  <option value="3">Level 3 (Heavy Texture / Heavy Wallcovering)</option>
                  <option value="4" selected>Level 4 (Standard Flat / Satin Paint)</option>
                  <option value="5">Level 5 (Premium Skim Coat / Gloss Paint)</option>
                </select>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcDrywallBtn">Calculate Drywall Bill</button>
              <button type="reset" class="btn btn-secondary" id="resetDrywallBtn">Reset</button>
            </div>
          </form>

          <div class="results-box" id="drywallResultBox" style="display:none; margin-top:25px;">
            <h3>Drywall Material Bill of Quantities</h3>
            <div class="result-grid">
              <div class="result-tile highlight">
                <span class="result-label">Drywall Panels to Order</span>
                <span class="result-value" id="resSheets">0</span>
                <span class="result-unit">Sheets (incl. waste)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Net Surface Area</span>
                <span class="result-value" id="resNetArea">0</span>
                <span class="result-unit">sq ft (~0 m²)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Joint Compound Mud (4.5 Gal Pails)</span>
                <span class="result-value" id="resMudBuckets">0</span>
                <span class="result-unit">Pails (~0 gal total)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Joint Tape (500 ft Rolls)</span>
                <span class="result-value" id="resTapeRolls">0</span>
                <span class="result-unit">Rolls (~0 linear ft)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Type W/S Drywall Screws</span>
                <span class="result-value" id="resScrews">0</span>
                <span class="result-unit">Screws (~0 5-lb boxes)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Total Gypsum Dry Mass</span>
                <span class="result-value" id="resDrywallMass">0</span>
                <span class="result-unit">lbs (~0 kg)</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Gypsum Wallboard Technology &amp; ASTM Specifications</h2>
          <p>
            Gypsum board, commonly referred to as drywall, plasterboard, or sheetrock, is the ubiquitous interior lining material in commercial and residential construction. Consisting of a non-combustible core of calcium sulfate dihydrate ($\text{CaSO}_4 \cdot 2\text{H}_2\text{O}$) encased in $100\%$ recycled fibrous paper liners, gypsum board provides structural shear diaphragm strength, thermal insulation, acoustic isolation, and essential fire resistance.
          </p>
          <p>
            Under <strong>ASTM C1396 (Standard Specification for Gypsum Board)</strong> and <strong>ASTM C840 (Standard Specification for Application and Finishing of Gypsum Board)</strong>, sheet thickness and core formulations are engineered for specific performance parameters:
          </p>
          <ul>
            <li><strong>1/2-Inch Regular ($12.7\text{ mm}$):</strong> Standard for residential interior walls and partition framing spaced at $16\text{ inches}$ on-center ($406\text{ mm}$). Weighs approximately $1.6\text{ lbs/sq ft}$ ($7.8\text{ kg/m}^2$).</li>
            <li><strong>1/2-Inch Sag-Resistant Ceiling Board:</strong> Enhanced chemically modified core formulation engineered to prevent sagging when supporting overhead attic batt insulation under high ambient humidity.</li>
            <li><strong>5/8-Inch Type X ($15.9\text{ mm}$):</strong> Special glass-fiber-reinforced core providing a certified 1-hour fire resistance rating per <strong>ASTM E119</strong>. Weighs approximately $2.2\text{ lbs/sq ft}$ ($10.7\text{ kg/m}^2$).</li>
            <li><strong>5/8-Inch Type C:</strong> Proprietary formulation with expanded vermiculite, offering enhanced core integrity under prolonged fire exposure for 2-hour and 3-hour rated elevator shaft enclosures and firewall assemblies.</li>
          </ul>

          <h2>Geometric Formulae for Drywall Surface Area</h2>
          <p>
            Accurate estimation begins with calculating gross surface area and deducting door and window fenestrations:
          </p>
          <div class="formula-box">
            $$A_{walls} = 2 \times (L + W) \times H$$
            $$A_{ceiling} = L \times W \quad (\text{if ceiling is included})$$
            $$A_{net} = A_{walls} + A_{ceiling} - A_{openings}$$
          </div>
          <p>
            To compute the total sheets required with cutting, trimming, and layout waste factor $W_{\%}$:
          </p>
          <div class="formula-box">
            $$N_{sheets} = \left\lceil \frac{A_{net} \times (1 + W_{\%} / 100)}{A_{panel}} \right\rceil$$
          </div>
          <p>
            Where $A_{panel}$ is the nominal surface area of the chosen sheet ($32\text{ sq ft}$ for $4\times 8$, $40\text{ sq ft}$ for $4\times 10$, $48\text{ sq ft}$ for $4\times 12$, and $54\text{ sq ft}$ for $4.5\times 12$ stretch boards).
          </p>

          <h2>Fastener Engineering: Drywall Screws &amp; Stud Spacing</h2>
          <p>
            Correct fastening prevents fastener popping and structural sagging. Screws are specified based on framing substrate:
          </p>
          <ul>
            <li><strong>Type W Screws:</strong> Coarse-thread bugle-head fasteners for attaching gypsum panels to wood framing (minimum penetration $\frac{5}{8}\text{ inch}$ / $16\text{ mm}$).</li>
            <li><strong>Type S Screws:</strong> Fine-thread, self-drilling point screws for light-gauge structural steel studs (minimum penetration $\frac{3}{8}\text{ inch}$ / $9.5\text{ mm}$).</li>
          </ul>
          <p>
            Fastener spacing guidelines per ASTM C840 dictate:
          </p>
          <div class="formula-box">
            $$\text{Wall Stud Spacing: Maximum } 16\text{ inches on-center}$$
            $$\text{Ceiling Joist Spacing: Maximum } 12\text{ inches on-center}$$
            $$\text{Fastener Rate} \approx 32\text{ to }36\text{ screws per } 4\times 8\text{ sheet } (\approx 1.0\text{ to }1.1\text{ screws per sq ft})$$
          </div>

          <h2>ASTM C840 Joint Compound (Mud) &amp; Finishing Levels</h2>
          <p>
            Finishing drywall joints requires embedding paper joint tape or fiberglass mesh in joint compound, followed by progressive feathering coats. The Gypsum Association (GA-214) and ASTM C840 categorize finishing into five distinct levels:
          </p>
          <ul>
            <li><strong>Level 1 (Fire-Taping):</strong> Tape embedded in compound over all joints and interior angles. Tool marks and ridges acceptable. Used in plenum areas, attics, and service corridors.</li>
            <li><strong>Level 2:</strong> Tape embedded, followed by a thin wipe coat of joint compound over tape and screw heads. Used in garages and mechanical rooms behind tile substrates.</li>
            <li><strong>Level 3:</strong> Tape embedded with two separate coats of compound over joints and fastener heads. Specified where heavy-texture spray or medium-to-heavy wall coverings are applied.</li>
            <li><strong>Level 4 (Standard Architectural Finish):</strong> Tape embedded plus three coats of compound over joints and fastener heads. The universal specification for standard flat, eggshell, and satin residential interior paints.</li>
            <li><strong>Level 5 (Premium Critical Lighting Finish):</strong> Level 4 finish supplemented by a continuous, uniform thin skim coat applied over the entire board surface to equalize porosity and eliminate photographing under harsh grazing light.</li>
          </ul>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Panel Size</th>
                <th>Square Feet / Board</th>
                <th>Joint Tape / Sheet</th>
                <th>Ready-Mix Mud / 100 Sheets</th>
                <th>Weight (1/2" Regular)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>4' &times; 8' (1.22 &times; 2.44 m)</td>
                <td>32 sq ft</td>
                <td>~12 linear ft</td>
                <td>~12 pails (4.5 gal)</td>
                <td>51.2 lbs (23.2 kg)</td>
              </tr>
              <tr>
                <td>4' &times; 10' (1.22 &times; 3.05 m)</td>
                <td>40 sq ft</td>
                <td>~14 linear ft</td>
                <td>~15 pails (4.5 gal)</td>
                <td>64.0 lbs (29.0 kg)</td>
              </tr>
              <tr>
                <td>4' &times; 12' (1.22 &times; 3.66 m)</td>
                <td>48 sq ft</td>
                <td>~16 linear ft</td>
                <td>~18 pails (4.5 gal)</td>
                <td>76.8 lbs (34.8 kg)</td>
              </tr>
              <tr>
                <td>4.5' &times; 12' (1.37 &times; 3.66 m)</td>
                <td>54 sq ft</td>
                <td>~17 linear ft</td>
                <td>~20 pails (4.5 gal)</td>
                <td>86.4 lbs (39.2 kg)</td>
              </tr>
            </tbody>
          </table>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: Commercial Conference Room Fit-Out</h3>
            <p><strong>Design Scenario:</strong> An office conference room measures $L = 24.0\text{ feet}$ in length, $W = 16.0\text{ feet}$ in width, with a finished suspended deck height of $H = 9.0\text{ feet}$. Both walls and the drywall ceiling are to be sheeted with $4\times 12\text{ foot}$ ($48\text{ sq ft}$) panels to minimize butt joints. Total door and window opening deductions equal $A_{openings} = 85.0\text{ sq ft}$. A standard $10\%$ cutting waste allowance is budgeted for a Level 4 paint-ready finish. Calculate net surface area, total panels, joint compound buckets ($4.5\text{ gallon}$ pails), paper tape rolls ($500\text{ ft}$ rolls), and drywall screws.</p>
            
            <p><strong>Step 1: Calculate Gross and Net Surface Areas</strong></p>
            <div class="formula-box">
              $$A_{walls} = 2 \times (24.0\text{ ft} + 16.0\text{ ft}) \times 9.0\text{ ft} = 2 \times 40.0 \times 9.0 = 720.0\text{ sq ft}$$
              $$A_{ceiling} = 24.0\text{ ft} \times 16.0\text{ ft} = 384.0\text{ sq ft}$$
              $$A_{gross} = 720.0 + 384.0 = 1,104.0\text{ sq ft}$$
              $$A_{net} = 1,104.0\text{ sq ft} - 85.0\text{ sq ft} = 1,019.0\text{ sq ft}$$
            </div>

            <p><strong>Step 2: Determine Drywall Panel Quantities ($4\times 12$ Sheets)</strong></p>
            <div class="formula-box">
              $$A_{budgeted} = 1,019.0\text{ sq ft} \times 1.10 = 1,120.9\text{ sq ft}$$
              $$N_{sheets} = \left\lceil \frac{1,120.9\text{ sq ft}}{48.0\text{ sq ft/sheet}} \right\rceil = \lceil 23.35 \rceil = \mathbf{24\text{ Panels of } 4\times 12}$$
            </div>

            <p><strong>Step 3: Estimate Joint Compound Mud Requirements (Level 4 Finish)</strong></p>
            <div class="formula-box">
              $$\text{Total Mud Volume} = 1,019\text{ sq ft} \times 0.053\text{ gal/sq ft} \approx 54.0\text{ Gallons}$$
              $$\text{Number of 4.5-Gallon Pails} = \left\lceil \frac{54.0}{4.5} \right\rceil = \mathbf{12\text{ Pails of All-Purpose Compound}}$$
            </div>

            <p><strong>Step 4: Compute Joint Tape and Drywall Screws</strong></p>
            <div class="formula-box">
              $$\text{Linear Feet of Tape} = 1,019\text{ sq ft} \times 0.37\text{ ft/sq ft} = 377.0\text{ ft} \implies \mathbf{1\text{ Roll of } 500\text{ ft Tape}}$$
              $$\text{Drywall Screws} = 24\text{ sheets} \times 48\text{ screws/sheet} = 1,152\text{ screws} \implies \mathbf{2\text{ Boxes of 5-lb Type S Screws}}$$
            </div>
            <p>
              <strong>Procurement Summary:</strong> Order <strong>24 sheets</strong> of $4\times 12$ drywall, <strong>12 pails</strong> ($4.5\text{-gal}$) of joint compound, <strong>1 roll</strong> of $500\text{-ft}$ paper joint tape, and <strong>two 5-lb boxes</strong> of self-drilling screws.
            </p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Building &amp; Finish Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="flooring-calculator.html">Flooring Area &amp; Box Estimator</a></li>
            <li><a href="paint-calculator.html">Paint Gallon &amp; Primer Calculator</a></li>
            <li><a href="concrete-block-calculator.html">Concrete Block Estimator</a></li>
            <li><a href="brick-calculator.html">Brick Masonry Calculator</a></li>
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
      const calcBtn = document.getElementById('calcDrywallBtn');
      const resetBtn = document.getElementById('resetDrywallBtn');
      const resultBox = document.getElementById('drywallResultBox');

      function calculateDrywall() {
        const L = parseFloat(document.getElementById('roomLength').value);
        const W = parseFloat(document.getElementById('roomWidth').value);
        const H = parseFloat(document.getElementById('ceilingHeight').value);
        const panelArea = parseFloat(document.getElementById('sheetSize').value);
        const openingSqFt = parseFloat(document.getElementById('openingDeduction').value) || 0;
        const inclCeiling = document.getElementById('includeCeiling').value === 'yes';
        const wastePct = parseFloat(document.getElementById('wasteFactor').value) || 0;
        const finishLvl = parseInt(document.getElementById('finishLevel').value);

        if (isNaN(L) || L <= 0 || isNaN(W) || W <= 0 || isNaN(H) || H <= 0) {
          alert('Please enter valid positive dimensions for room length, width, and height.');
          return;
        }

        const wallArea = 2.0 * (L + W) * H;
        const ceilingArea = inclCeiling ? (L * W) : 0;
        const grossArea = wallArea + ceilingArea;
        const netArea = Math.max(1.0, grossArea - openingSqFt);

        const totalAreaWithWaste = netArea * (1.0 + wastePct / 100.0);
        const totalSheets = Math.ceil(totalAreaWithWaste / panelArea);

        // Mud factor based on finish level
        let mudGallonsPer1000 = 53.0; // Level 4 standard
        if (finishLvl === 3) mudGallonsPer1000 = 42.0;
        else if (finishLvl === 5) mudGallonsPer1000 = 75.0; // includes full skim coat

        const totalMudGallons = (netArea / 1000.0) * mudGallonsPer1000;
        const mudBuckets = Math.ceil(totalMudGallons / 4.5);

        // Tape: ~37 linear feet per 100 sq ft
        const tapeFeet = Math.round((netArea / 100.0) * 37.0);
        const tapeRolls = Math.max(1, Math.ceil(tapeFeet / 500.0));

        // Screws: ~34 screws per 32 sq ft sheet -> ~1.06 screws per sq ft
        const screwsPerSheet = panelArea >= 48 ? 48 : 34;
        const totalScrews = totalSheets * screwsPerSheet;
        const screwBoxes5lb = Math.ceil(totalScrews / 1000.0);

        // 1/2" regular sheet weighs ~1.6 lb per sq ft
        const totalMassLbs = Math.round(totalSheets * panelArea * 1.6);
        const totalMassKg = Math.round(totalMassLbs * 0.453592);
        const netAreaM2 = (netArea * 0.092903).toFixed(1);

        document.getElementById('resSheets').textContent = totalSheets.toLocaleString();
        document.getElementById('resNetArea').textContent = Math.round(netArea).toLocaleString() + ` (~${netAreaM2} m²)`;
        document.getElementById('resMudBuckets').textContent = mudBuckets.toLocaleString() + ` (~${totalMudGallons.toFixed(1)} gal)`;
        document.getElementById('resTapeRolls').textContent = tapeRolls.toLocaleString() + ` (~${tapeFeet} ft)`;
        document.getElementById('resScrews').textContent = totalScrews.toLocaleString() + ` (~${screwBoxes5lb} boxes)`;
        document.getElementById('resDrywallMass').textContent = totalMassLbs.toLocaleString() + ` (~${totalMassKg} kg)`;

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculateDrywall);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
      });
      calculateDrywall();
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
  <title>Excavation Calculator | Earthwork Volume &amp; Truck Haul Estimator</title>
  <meta name="description" content="Calculate earthwork excavation volumes (Bank, Loose, Compacted Cubic Yards), soil swell factors, trench slope benching per OSHA, and dump truck trips.">
  <link rel="canonical" href="https://calchub.cloud/excavation-calculator.html">
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
        "name": "Excavation Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates earthwork excavation bank cubic yards (BCY), loose cubic yards (LCY) with soil swell factors, and dump truck haul cycles per OSHA 1926.",
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
            "name": "What is the difference between Bank Cubic Yards (BCY) and Loose Cubic Yards (LCY)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Bank Cubic Yards (BCY) measures soil in its natural, undisturbed in-situ state before excavation. When dug up, soil particles separate and create air voids, expanding by 15% to 40% into Loose Cubic Yards (LCY). LCY is the actual volume that must be hauled away by dump trucks."
            }
          },
          {
            "@type": "Question",
            "name": "What is the soil swell factor formula?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Loose volume is calculated as: V_loose = V_bank * (1 + S_w / 100), where S_w is the swell percentage. Conversely, the Load Factor (L_f) is defined as L_f = V_bank / V_loose = 1 / (1 + S_w / 100)."
            }
          },
          {
            "@type": "Question",
            "name": "How many dump truck loads are required for an excavation project?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Divide the total Loose Cubic Yards (LCY) or loose cubic meters by the rated hauling capacity of the dump truck (typically 10 to 12 cubic yards for standard tri-axle dump trucks, or 14 to 18 cubic yards for end-dump trailers), rounding up to the next whole number."
            }
          },
          {
            "@type": "Question",
            "name": "What are OSHA trench sloping and benching requirements?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Per OSHA 29 CFR 1926 Subpart P, excavations deeper than 5 feet (1.5 m) require protective systems. Allowable maximum side slopes are: Type A Soil (dense clay): 3/4:1 (53°); Type B Soil (silt, loam, sandy clay): 1:1 (45°); and Type C Soil (sand, gravel, submerged): 1.5:1 (34°)."
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
      <span>Excavation Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calculator-main">
        <div class="calc-header">
          <h1>Excavation Calculator</h1>
          <p>Compute earthwork bank volume (BCY), loose haul volume (LCY), soil swell expansion, and dump truck trips per OSHA standards.</p>
        </div>

        <div class="calculator-card">
          <form id="excavationForm" onsubmit="return false;">
            <div class="form-row">
              <div class="form-group">
                <label for="excavationShape">Excavation Geometry:</label>
                <select id="excavationShape">
                  <option value="rect" selected>Rectangular Trench or Basement Pit</option>
                  <option value="cylinder">Circular Pier / Caisson Shaft</option>
                </select>
              </div>
              <div class="form-group">
                <label for="excavationDepth">Excavation Depth (meters):</label>
                <input type="number" id="excavationDepth" value="2.5" step="0.1" min="0.1" required>
                <span class="hint">Vertical cut depth</span>
              </div>
            </div>

            <div class="form-row" id="rectDimRow">
              <div class="form-group">
                <label for="excavLength">Length at Surface (meters):</label>
                <input type="number" id="excavLength" value="15.0" step="0.5" min="0.1" required>
              </div>
              <div class="form-group">
                <label for="excavWidth">Width at Surface (meters):</label>
                <input type="number" id="excavWidth" value="8.0" step="0.5" min="0.1" required>
              </div>
            </div>

            <div class="form-row" id="cylDimRow" style="display:none;">
              <div class="form-group">
                <label for="excavDiameter">Shaft Diameter (meters):</label>
                <input type="number" id="excavDiameter" value="3.0" step="0.1" min="0.1">
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="soilType">Soil Classification &amp; Swell:</label>
                <select id="soilType">
                  <option value="15">Sand &amp; Gravel (15% Swell, Type C Soil)</option>
                  <option value="25" selected>Common Earth / Loam (25% Swell, Type B Soil)</option>
                  <option value="40">Dense Heavy Clay (40% Swell, Type A Soil)</option>
                  <option value="60">Blasted Solid Rock (60% Swell)</option>
                </select>
              </div>
              <div class="form-group">
                <label for="truckCapacity">Dump Truck Capacity (m³):</label>
                <input type="number" id="truckCapacity" value="10.0" step="0.5" min="1.0" required>
                <span class="hint">Standard 10-wheeler ~8-10 m³ (10-13 cu yd)</span>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcExcavBtn">Calculate Earthwork Volume</button>
              <button type="reset" class="btn btn-secondary" id="resetExcavBtn">Reset</button>
            </div>
          </form>

          <div class="results-box" id="excavResultBox" style="display:none; margin-top:25px;">
            <h3>Earthwork Mass Haul &amp; Volume Estimates</h3>
            <div class="result-grid">
              <div class="result-tile highlight">
                <span class="result-label">Loose Haul Volume (LCY)</span>
                <span class="result-value" id="resLooseVol">0.00</span>
                <span class="result-unit">m³ (~0 cu yd)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Bank In-Situ Volume (BCY)</span>
                <span class="result-value" id="resBankVol">0.00</span>
                <span class="result-unit">m³ (~0 cu yd)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Dump Truck Loads Needed</span>
                <span class="result-value" id="resTruckLoads">0</span>
                <span class="result-unit">Haul Trips</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Volumetric Soil Swell</span>
                <span class="result-value" id="resSwellVol">+0.00</span>
                <span class="result-unit">m³ Expansion Air Voids</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Total Excavated Mass</span>
                <span class="result-value" id="resSoilMass">0</span>
                <span class="result-unit">Metric Tonnes (~0 US tons)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">OSHA Trench Slope Guidance</span>
                <span class="result-value" id="resOshaSlope">Type B</span>
                <span class="result-unit">1:1 (45° angle)</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Earthwork Principles: Bank, Loose, and Compacted Volumes</h2>
          <p>
            Civil earthwork engineering involves excavating, hauling, grading, and compacting soil and rock materials. A fundamental tenet of geotechnical engineering is that soil volume changes dramatically throughout the excavation and embankment construction lifecycle. Civil engineers classify earth materials into three distinct volumetric states:
          </p>
          <ul>
            <li><strong>Bank Cubic Yards (BCY / In-Situ $m^3$):</strong> The volume of soil or rock in its natural, undisturbed ground state prior to excavation. All contractual earthwork pay quantities are typically measured in bank volume.</li>
            <li><strong>Loose Cubic Yards (LCY / Haul $m^3$):</strong> The expanded volume of material after mechanical excavation and loading into dump trucks. Mechanical shearing breaks internal soil cohesion, causing particles to rearrange with increased pore voids.</li>
            <li><strong>Compacted Cubic Yards (CCY / Fill $m^3$):</strong> The volume of soil after placement in embankments and mechanical densification using vibratory rollers or sheep's foot compactors to eliminate air voids.</li>
          </ul>

          <h2>Soil Swell and Load Factor Equations</h2>
          <p>
            The expansion of soil from undisturbed bank state to loose state is governed by the <strong>Swell Percentage ($S_w$)</strong>:
          </p>
          <div class="formula-box">
            $$V_{loose} = V_{bank} \times \left(1 + \frac{S_w}{100}\right)$$
          </div>
          <p>
            Conversely, the <strong>Load Factor ($L_f$)</strong> defines the proportion of bank volume contained within a unit loose volume:
          </p>
          <div class="formula-box">
            $$L_f = \frac{V_{bank}}{V_{loose}} = \frac{1}{1 + \frac{S_w}{100}} = \frac{\rho_{loose}}{\rho_{bank}}$$
          </div>
          <p>
            When soil is subsequently placed in structural engineered fills, it experiences <strong>Shrinkage Factor ($S_h$)</strong> relative to the bank state:
          </p>
          <div class="formula-box">
            $$V_{compacted} = V_{bank} \times (1 - S_h)$$
          </div>

          <h2>Excavation Geometry &amp; Prismoidal Formulas</h2>
          <p>
            For a vertical-walled rectangular pit or foundation basement of length $L$, width $W$, and depth $D$:
          </p>
          <div class="formula-box">
            $$V_{bank} = L \times W \times D$$
          </div>
          <p>
            For circular deep foundation caissons, bored piles, or cylindrical shaft excavations with diameter $d$:
          </p>
          <div class="formula-box">
            $$V_{bank} = \pi \times \left(\frac{d}{2}\right)^2 \times D$$
          </div>
          <p>
            For deep foundation cuts with sloped side embankments conforming to angle of repose, the <strong>Prismoidal Formula</strong> provides exact volumetric evaluation between top surface area $A_1$, bottom area $A_2$, and mid-depth area $A_m$:
          </p>
          <div class="formula-box">
            $$V_{bank} = \frac{D}{6} (A_1 + 4 A_m + A_2)$$
          </div>

          <h2>OSHA Excavation Safety Standards (29 CFR 1926 Subpart P)</h2>
          <p>
            Trench collapses represent one of the deadliest hazards in heavy construction. Under federal standard <strong>OSHA 29 CFR 1926 Subpart P</strong>, any trench deeper than $5\text{ feet}$ ($1.52\text{ meters}$) requires an engineered protective system: sloping, benching, shoring, or trench shield boxes.
          </p>
          <p>
            Soil classification dictates maximum allowable side slopes ($H:V$):
          </p>
          <ul>
            <li><strong>Type A Soil ($q_u \ge 144\text{ kPa} / 1.5\text{ tsf}$):</strong> Stiff, cohesive clays, cemented sands (caliche). Maximum allowable slope: $\frac{3}{4}:1$ ($53^\circ$ angle).</li>
            <li><strong>Type B Soil ($48\text{ kPa} \le q_u < 144\text{ kPa}$):</strong> Cohesive silt, loam, silt clay, sandy loam. Maximum allowable slope: $1:1$ ($45^\circ$ angle).</li>
            <li><strong>Type C Soil ($q_u < 48\text{ kPa} / 0.5\text{ tsf}$):</strong> Granular soils including gravel, sand, submerged soil with seeping water. Maximum allowable slope: $1.5:1$ ($34^\circ$ angle).</li>
          </ul>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Soil Type</th>
                <th>Bank Density (kg/m³ / lb/cu yd)</th>
                <th>Swell Factor ($S_w$)</th>
                <th>Load Factor ($L_f$)</th>
                <th>OSHA Maximum Slope</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Clean Sand &amp; Fine Gravel</td>
                <td>1,780 kg/m³ (3,000 lb/yd³)</td>
                <td>12% – 18%</td>
                <td>0.86</td>
                <td>1.5:1 (34°, Type C)</td>
              </tr>
              <tr>
                <td>Common Earth / Loam</td>
                <td>1,600 kg/m³ (2,700 lb/yd³)</td>
                <td>20% – 28%</td>
                <td>0.80</td>
                <td>1:1 (45°, Type B)</td>
              </tr>
              <tr>
                <td>Dense Heavy Clay</td>
                <td>1,900 kg/m³ (3,200 lb/yd³)</td>
                <td>35% – 45%</td>
                <td>0.70</td>
                <td>0.75:1 (53°, Type A)</td>
              </tr>
              <tr>
                <td>Blasted Solid Rock / Granite</td>
                <td>2,600 kg/m³ (4,400 lb/yd³)</td>
                <td>50% – 70%</td>
                <td>0.60</td>
                <td>Vertical (Stable Rock)</td>
              </tr>
            </tbody>
          </table>

          <h2>Mass-Haul Diagrams, Cut-and-Fill Balancing &amp; Trench Shoring Systems</h2>
          <p>
            On highway, pipeline, and large-scale industrial site grading developments, minimizing earth haul expenses is the paramount engineering challenge. The cumulative volume of cut (excavation) and fill (embankment placement) along a project alignment is analyzed using a <strong>Mass-Haul Diagram</strong>.
          </p>
          <p>
            The mass-haul curve plots station along the horizontal axis versus cumulative net earthwork volume on the vertical axis (with cut represented as rising positive slopes and fill as falling negative slopes). The balance points occur where the profile curve intersects the baseline. The economic <strong>Limit of Economic Haul (LEH)</strong> is formulated by equating haul cost against the alternative expense of borrowing off-site material:
          </p>
          <div class="formula-box">
            $$\text{LEH} = \text{Free-Haul Distance} + \frac{\text{Unit Cost of Borrow Soil}}{\text{Unit Overhaul Cost per Station}}$$
          </div>
          <p>
            <strong>Excavation Support Systems:</strong> When property line constraints, adjacent foundations, or underground utilities prevent OSHA open sloping, temporary retaining shoring must be engineered:
          </p>
          <ul>
            <li><strong>Soldier Piles and Lagging:</strong> Vertical wide-flange steel H-beams driven or grouted into pre-drilled holes at $6\text{ to }10\text{ foot}$ spacing, with heavy horizontal timber lagging planks slotted between flanges.</li>
            <li><strong>Interlocking Steel Sheet Piling:</strong> Hot-rolled Z-profile or U-profile steel sheets vibrated into the ground to provide a continuous impervious barrier against unstable running sand and high groundwater tables.</li>
            <li><strong>Trench Boxes (Shields):</strong> Heavy dual-wall steel or aluminum protective shields dragged along pipeline trenches to safeguard pipelayers from catastrophic sidewall cave-ins.</li>
          </ul>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: Commercial Basement Earthwork Mass Haul</h3>
            <p><strong>Design Scenario:</strong> An earthwork contractor is excavating a foundation basement for a commercial medical clinic. The excavation pit is rectangular with vertical shored perimeter walls measuring $L = 20.0\text{ meters}$ in length, $W = 12.0\text{ meters}$ in width, and $D = 3.0\text{ meters}$ in finished cut depth. The geotechnical bore report classifies the subsoil as <strong>Common Earth / Silty Clay</strong> with an in-situ bank density of $\rho_{bank} = 1,750\text{ kg/m}^3$ and an established soil swell factor of $S_w = 25\%$. Material will be hauled off-site using tri-axle dump trucks with a legal highway volumetric box capacity of $10.0\text{ m}^3$ ($13.1\text{ cu yd}$). Calculate Bank Volume (BCY), Loose Hauled Volume (LCY), total earth mass, and number of truck haul cycles.</p>
            
            <p><strong>Step 1: Compute Undisturbed In-Situ Bank Volume ($V_{bank}$)</strong></p>
            <div class="formula-box">
              $$V_{bank} = L \times W \times D = 20.0\text{ m} \times 12.0\text{ m} \times 3.0\text{ m} = \mathbf{720.0\text{ m}^3} \quad (\approx 941.7\text{ cu yd})$$
            </div>

            <p><strong>Step 2: Determine Loose Hauled Volume ($V_{loose}$) with Swell Factor</strong></p>
            <div class="formula-box">
              $$V_{loose} = V_{bank} \times \left(1 + \frac{S_w}{100}\right) = 720.0\text{ m}^3 \times 1.25 = \mathbf{900.0\text{ m}^3} \quad (\approx 1,177.2\text{ cu yd})$$
              $$\Delta V_{swell} = 900.0\text{ m}^3 - 720.0\text{ m}^3 = 180.0\text{ m}^3 \text{ of added void volume}$$
            </div>

            <p><strong>Step 3: Evaluate Total In-Situ Mass</strong></p>
            <div class="formula-box">
              $$M_{total} = V_{bank} \times \rho_{bank} = 720.0\text{ m}^3 \times 1,750\text{ kg/m}^3 = 1,260,000\text{ kg} = \mathbf{1,260\text{ Metric Tonnes}}$$
            </div>

            <p><strong>Step 4: Determine Number of Dump Truck Haul Trips</strong></p>
            <div class="formula-box">
              $$N_{trips} = \left\lceil \frac{V_{loose}}{\text{Truck Capacity}} \right\rceil = \left\lceil \frac{900.0\text{ m}^3}{10.0\text{ m}^3/\text{load}} \right\rceil = \mathbf{90\text{ Dump Truck Loads}}$$
            </div>
            <p>
              <strong>Earthwork Operational Summary:</strong> Contracting requires booking <strong>90 truck trips</strong> to haul $900.0\text{ m}^3$ of loose earth. At an average fleet cycle time of 45 minutes per truck across a 5-truck convoy, the excavation job will require approximately 13.5 operating hours of earthmoving.
            </p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Civil &amp; Earthwork Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="excavation-volume-calculator.html">Excavation Volume Calculator</a></li>
            <li><a href="retaining-wall-calculator.html">Retaining Wall Sizing</a></li>
            <li><a href="concrete-calculator.html">Concrete Volume Calculator</a></li>
            <li><a href="gravel-calculator.html">Gravel &amp; Crushed Stone Estimator</a></li>
            <li><a href="asphalt-calculator.html">Asphalt Paving Calculator</a></li>
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
      const calcBtn = document.getElementById('calcExcavBtn');
      const resetBtn = document.getElementById('resetExcavBtn');
      const resultBox = document.getElementById('excavResultBox');
      const shapeSelect = document.getElementById('excavationShape');
      const rectRow = document.getElementById('rectDimRow');
      const cylRow = document.getElementById('cylDimRow');

      shapeSelect.addEventListener('change', function() {
        if (this.value === 'cylinder') {
          rectRow.style.display = 'none';
          cylRow.style.display = 'flex';
        } else {
          rectRow.style.display = 'flex';
          cylRow.style.display = 'none';
        }
      });

      function calculateExcavation() {
        const shape = shapeSelect.value;
        const depth = parseFloat(document.getElementById('excavationDepth').value);
        const swellPct = parseFloat(document.getElementById('soilType').value);
        const truckCap = parseFloat(document.getElementById('truckCapacity').value);

        if (isNaN(depth) || depth <= 0 || isNaN(truckCap) || truckCap <= 0) {
          alert('Please enter valid positive dimensions for depth and truck capacity.');
          return;
        }

        let V_bank = 0;
        if (shape === 'cylinder') {
          const dia = parseFloat(document.getElementById('excavDiameter').value);
          if (isNaN(dia) || dia <= 0) {
            alert('Please enter a valid diameter.');
            return;
          }
          const radius = dia / 2.0;
          V_bank = Math.PI * radius * radius * depth;
        } else {
          const L = parseFloat(document.getElementById('excavLength').value);
          const W = parseFloat(document.getElementById('excavWidth').value);
          if (isNaN(L) || L <= 0 || isNaN(W) || W <= 0) {
            alert('Please enter valid length and width dimensions.');
            return;
          }
          V_bank = L * W * depth;
        }

        const V_loose = V_bank * (1.0 + swellPct / 100.0);
        const V_swell = V_loose - V_bank;
        const truckLoads = Math.ceil(V_loose / truckCap);

        // Standard density ~1750 kg/m3 bank
        const massTonnes = Math.round(V_bank * 1.75);
        const massUsTons = Math.round(massTonnes * 1.10231);

        const bankYards = (V_bank * 1.30795).toFixed(1);
        const looseYards = (V_loose * 1.30795).toFixed(1);

        let oshaSlope = 'Type B: 1:1 (45°)';
        if (swellPct === 15) oshaSlope = 'Type C: 1.5:1 (34°)';
        else if (swellPct === 40) oshaSlope = 'Type A: 0.75:1 (53°)';
        else if (swellPct === 60) oshaSlope = 'Stable Rock: Vertical (90°)';

        document.getElementById('resLooseVol').textContent = V_loose.toFixed(1) + ` (~${looseYards} yd³)`;
        document.getElementById('resBankVol').textContent = V_bank.toFixed(1) + ` (~${bankYards} yd³)`;
        document.getElementById('resTruckLoads').textContent = truckLoads.toLocaleString();
        document.getElementById('resSwellVol').textContent = '+' + V_swell.toFixed(1);
        document.getElementById('resSoilMass').textContent = massTonnes.toLocaleString() + ` (~${massUsTons} US tons)`;
        document.getElementById('resOshaSlope').textContent = oshaSlope;

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculateExcavation);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
        shapeSelect.value = 'rect';
        rectRow.style.display = 'flex';
        cylRow.style.display = 'none';
      });
      calculateExcavation();
    });
  </script>
</body>
</html>
"""

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    path_drywall = os.path.join(base_dir, 'drywall-calculator.html')
    with open(path_drywall, 'w', encoding='utf-8') as f:
        f.write(TOOL_5_HTML.strip() + '\n')
    print("[PASS] drywall-calculator.html generated successfully!")

    path_excav = os.path.join(base_dir, 'excavation-calculator.html')
    with open(path_excav, 'w', encoding='utf-8') as f:
        f.write(TOOL_6_HTML.strip() + '\n')
    print("[PASS] excavation-calculator.html generated successfully!")

if __name__ == '__main__':
    main()
