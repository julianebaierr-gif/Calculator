# -*- coding: utf-8 -*-
"""
Generator for Batch 37 - Part 4
Tools:
7. stud-wall-calculator.html
8. plaster-calculator.html
"""

import os

COMMON_TAIL = """    <footer class="site-footer">
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>About CalcHub</h4>
                    <p>CalcHub provides free, high-precision engineering calculators, unit converters, and analytical tools designed for practicing civil engineers, architects, carpenters, and construction estimators worldwide.</p>
                </div>
                <div class="footer-col">
                    <h4>Engineering Categories</h4>
                    <ul>
                        <li><a href="civil.html">Civil &amp; Structural</a></li>
                        <li><a href="engineering.html">Electrical &amp; Electronics</a></li>
                        <li><a href="mechanical.html">Mechanical &amp; HVAC</a></li>
                        <li><a href="chemical.html">Chemical &amp; Process</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Popular Construction Calculators</h4>
                    <ul>
                        <li><a href="concrete-calculator.html">Concrete Slab &amp; Footing</a></li>
                        <li><a href="stair-calculator.html">Stair Framing</a></li>
                        <li><a href="stud-wall-calculator.html">Stud Wall Framing</a></li>
                        <li><a href="plaster-calculator.html">Plaster Material Estimator</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="index.html">All Calculators</a></li>
                        <li><a href="converter.html">Unit Converters</a></li>
                        <li><a href="math.html">Math Tools</a></li>
                        <li><a href="finance.html">Finance Tools</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 CalcHub. All rights reserved. Peer-reviewed analytical calculation models.</p>
            </div>
        </div>
    </footer>
</body>
</html>"""

def get_page_html(title, description, canonical_slug, schema_json, h1, short_desc, calc_ui, article_content, category_hub="civil.html", category_name="Civil Engineering"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="https://calchub.com/{canonical_slug}.html">
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
    <script type="application/ld+json">
{schema_json}
    </script>
</head>
<body>
    <header class="site-header">
        <div class="header-container">
            <a href="index.html" class="logo">CalcHub</a>
            <nav class="nav-links">
                <a href="index.html">Home</a>
                <a href="math.html">Math &amp; Stats</a>
                <a href="converter.html">Converters</a>
                <a href="engineering.html">Engineering</a>
                <a href="finance.html">Finance</a>
            </nav>
        </div>
    </header>
    <div class="container">
        <div class="main-wrapper">
            <main class="content-area">
                <nav class="breadcrumb">
                    <a href="index.html">Home</a> &gt; <a href="{category_hub}">{category_name}</a> &gt; <span>{h1}</span>
                </nav>
                <div class="calculator-card">
                    <div class="calc-header">
                        <h1>{h1}</h1>
                        <p class="calc-desc">{short_desc}</p>
                    </div>
                    {calc_ui}
                </div>
                <article class="article-body">
                    {article_content}
                </article>
            </main>
            <aside class="sidebar">
                <div class="sidebar-card">
                    <h3>Related Construction Tools</h3>
                    <ul class="sidebar-links">
                        <li><a href="stud-wall-calculator.html">Stud Wall Framing</a></li>
                        <li><a href="plaster-calculator.html">Plaster Material Estimator</a></li>
                        <li><a href="stair-calculator.html">Stair Calculator</a></li>
                        <li><a href="concrete-calculator.html">Concrete Slab &amp; Footing</a></li>
                        <li><a href="rebar-calculator.html">Rebar Weight &amp; Spacing</a></li>
                        <li><a href="retaining-wall-calculator.html">Retaining Wall Sizing</a></li>
                        <li><a href="brick-calculator.html">Brick &amp; Mortar Calculator</a></li>
                        <li><a href="roofing-calculator.html">Roof Pitch &amp; Shingle</a></li>
                        <li><a href="beam-deflection-calculator.html">Beam Deflection Calculator</a></li>
                        <li><a href="soil-compaction-calculator.html">Soil Compaction</a></li>
                    </ul>
                </div>
            </aside>
        </div>
    </div>
{COMMON_TAIL}"""


# ---------------------------------------------------------------------------
# Tool 7: Stud Wall Calculator
# ---------------------------------------------------------------------------
def gen_stud_wall():
    slug = "stud-wall-calculator"
    title = "Stud Wall Calculator | Wood & Steel Framing Lumber Estimator"
    desc = "Calculate timber and steel stud wall framing: count common studs, top and bottom plates, corner posts, window/door headers, drywall sheets, and waste factors."
    h1 = "Stud Wall Calculator"
    short_desc = "Estimate lumber requirements for wood and light-gauge steel stud walls including common studs, top/sole plates, corner assemblies, door/window framing, and drywall."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Stud Wall Calculator",
      "url": "https://calchub.com/stud-wall-calculator.html",
      "applicationCategory": "EngineeringApplication",
      "operatingSystem": "All",
      "description": "Calculate wall framing lumber, common studs (16-inch or 24-inch OC), top and bottom plates, headers, king and trimmer studs, and drywall sheathing.",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the difference between 16-inch and 24-inch on-center (OC) stud spacing?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "16-inch on-center (OC) framing is the traditional structural standard for load-bearing exterior and interior walls, providing superior lateral stiffness, high vertical compressive capacity, and continuous backing for 1/2-inch drywall. 24-inch OC framing (Advanced Framing or Optimum Value Engineering) uses ~30% less lumber, enhances wall thermal performance by expanding insulation cavity area, but requires 5/8-inch drywall or structural sheathing to prevent surface sagging."
          }
        },
        {
          "@type": "Question",
          "name": "Why do standard walls require a double top plate?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A double top plate ties adjacent wall segments together at corner intersections and splices, providing structural continuity against wind shear and seismic forces. Furthermore, it distributes concentrated point loads from roof trusses and floor joists that do not align directly over vertical wall studs."
          }
        },
        {
          "@type": "Question",
          "name": "How many extra studs are needed for corners, wall intersections, and rough openings?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Each 90-degree corner typically requires 2 to 3 extra studs (for 3-stud or California corner nailer assemblies). Each interior T-junction wall intersection requires 2 extra studs for drywall backing. Each door or window rough opening requires 2 king studs, 2 jack (trimmer) studs, a structural header (2x6 to 2x12), and upper/lower cripple studs."
          }
        },
        {
          "@type": "Question",
          "name": "What waste factor should be added when ordering framing lumber?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Professional framing contractors typically add a 10% to 15% waste allowance to stud and plate orders to account for warped boards, excessive knots, crown culling, trimming scrap, and short blocking/firestop lumber requirements."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calculator-form">
    <div class="calc-row">
        <div class="calc-field">
            <label for="sw_length">Wall Length (Feet):</label>
            <input type="number" id="sw_length" value="24" step="0.5" min="1">
            <small class="field-hint">Total continuous wall run</small>
        </div>
        <div class="calc-field">
            <label for="sw_height">Wall Height (Feet):</label>
            <select id="sw_height">
                <option value="8" selected>8 Feet (92-5/8" precut stud)</option>
                <option value="9">9 Feet (104-5/8" precut stud)</option>
                <option value="10">10 Feet (116-5/8" precut stud)</option>
                <option value="12">12 Feet (140-5/8" precut stud)</option>
            </select>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="sw_spacing">Stud Spacing On-Center (OC):</label>
            <select id="sw_spacing">
                <option value="16" selected>16 Inches On-Center (Standard Structural)</option>
                <option value="24">24 Inches On-Center (Advanced Framing / Non-Bearing)</option>
                <option value="12">12 Inches On-Center (Heavy Tile / Commercial)</option>
            </select>
        </div>
        <div class="calc-field">
            <label for="sw_plates">Plate Configuration:</label>
            <select id="sw_plates">
                <option value="3" selected>Standard: 1 Sole Plate + 2 Top Plates (3 Total)</option>
                <option value="2">Single Top Plate: 1 Sole + 1 Top (2 Total - Advanced Framing)</option>
            </select>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="sw_corners">90° Corner Assemblies:</label>
            <input type="number" id="sw_corners" value="2" step="1" min="0">
            <small class="field-hint">Adds 2 extra studs per corner for backing</small>
        </div>
        <div class="calc-field">
            <label for="sw_intersections">T-Wall Intersections (Nailers):</label>
            <input type="number" id="sw_intersections" value="1" step="1" min="0">
            <small class="field-hint">Adds 2 studs per T-junction for drywall backing</small>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="sw_doors">Door Openings:</label>
            <input type="number" id="sw_doors" value="1" step="1" min="0">
            <small class="field-hint">Adds 2 Kings, 2 Trimmers + cripple allowances</small>
        </div>
        <div class="calc-field">
            <label for="sw_windows">Window Openings:</label>
            <input type="number" id="sw_windows" value="2" step="1" min="0">
            <small class="field-hint">Adds 2 Kings, 2 Trimmers + sill &amp; cripples</small>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="sw_waste">Waste &amp; Culling Allowance (%):</label>
            <input type="number" id="sw_waste" value="15" step="1" min="5" max="30">
            <small class="field-hint">Standard contractor allowance: 10% - 15%</small>
        </div>
        <div class="calc-field">
            <label for="sw_sheathing">Drywall / Sheathing Sheet Size:</label>
            <select id="sw_sheathing">
                <option value="32" selected>4' x 8' Sheet (32 sq ft)</option>
                <option value="40">4' x 10' Sheet (40 sq ft)</option>
                <option value="48">4' x 12' Sheet (48 sq ft)</option>
            </select>
        </div>
    </div>
    <button type="button" class="btn btn-primary" id="btn_calc_sw" style="width:100%; margin-top:1rem;">Calculate Wall Framing Materials</button>

    <div class="calc-results" id="sw_results" style="margin-top:1.5rem;">
        <h3>Framing Material Takeoff Bill</h3>
        <div class="results-grid">
            <div class="result-item">
                <span class="result-label">Base Common Studs:</span>
                <span class="result-value" id="res_sw_common">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Corner &amp; T-Wall Backing Studs:</span>
                <span class="result-value" id="res_sw_backing">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Opening Studs (Kings &amp; Jacks):</span>
                <span class="result-value" id="res_sw_openings">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Total Studs (Including Waste):</span>
                <span class="result-value" id="res_sw_total_studs">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Horizontal Plates Total Length:</span>
                <span class="result-value" id="res_sw_plate_lf">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Plates Lumber (16-Ft Boards):</span>
                <span class="result-value" id="res_sw_plate_boards">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Drywall / OSB Sheets (One Side):</span>
                <span class="result-value" id="res_sw_sheets_1s">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Drywall Sheets (Both Sides):</span>
                <span class="result-value" id="res_sw_sheets_2s">--</span>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    function calculateStudWall() {
        const lengthFt = parseFloat(document.getElementById('sw_length').value) || 24;
        const heightFt = parseFloat(document.getElementById('sw_height').value) || 8;
        const ocSpacingIn = parseFloat(document.getElementById('sw_spacing').value) || 16;
        const numPlates = parseInt(document.getElementById('sw_plates').value) || 3;
        const numCorners = parseInt(document.getElementById('sw_corners').value) || 0;
        const numIntersections = parseInt(document.getElementById('sw_intersections').value) || 0;
        const numDoors = parseInt(document.getElementById('sw_doors').value) || 0;
        const numWindows = parseInt(document.getElementById('sw_windows').value) || 0;
        const wastePct = (parseFloat(document.getElementById('sw_waste').value) || 15) / 100;
        const sheetSizeSqFt = parseFloat(document.getElementById('sw_sheathing').value) || 32;

        // 1. Common studs: ceil((length * 12) / spacing) + 1
        const commonStuds = Math.ceil((lengthFt * 12) / ocSpacingIn) + 1;

        // 2. Corner assemblies: each 90-deg corner needs 2 additional studs for nailer/post
        // T-Intersections: each intersection needs 2 additional studs for drywall backing
        const cornerStuds = numCorners * 2;
        const interStuds = numIntersections * 2;
        const backingStuds = cornerStuds + interStuds;

        // 3. Openings: each door/window requires:
        // 2 King studs + 2 Jack/Trimmer studs = 4 studs per opening
        // plus cripple studs: estimated ~2 cripples per door, ~3 cripples per window
        const totalOpenings = numDoors + numWindows;
        const openingKingsJacks = totalOpenings * 4;
        const crippleStuds = (numDoors * 2) + (numWindows * 3);
        const totalOpeningFramingStuds = openingKingsJacks + crippleStuds;

        // Subtotal raw studs before waste
        const rawStuds = commonStuds + backingStuds + totalOpeningFramingStuds;

        // Total studs with waste allowance
        const totalStudsWithWaste = Math.ceil(rawStuds * (1 + wastePct));

        // 4. Horizontal plates:
        // Total Linear Feet = lengthFt * numPlates
        const rawPlateLf = lengthFt * numPlates;
        const plateLfWithWaste = Math.ceil(rawPlateLf * (1 + wastePct));
        // Order in standard 16-ft framing boards
        const plateBoards16Ft = Math.ceil(plateLfWithWaste / 16);

        // 5. Drywall / Plywood sheathing sheets:
        const wallGrossArea = lengthFt * heightFt;
        // Approximate opening deduction: door ~20 sq ft, window ~15 sq ft
        const openingArea = (numDoors * 20) + (numWindows * 15);
        const netWallArea = Math.max(0, wallGrossArea - openingArea);

        // One side sheathing (with 10% cut waste)
        const sheetsOneSide = Math.ceil((netWallArea * 1.10) / sheetSizeSqFt);
        // Both sides (interior partition drywall)
        const sheetsBothSides = sheetsOneSide * 2;

        document.getElementById('res_sw_common').textContent = commonStuds + ' studs';
        document.getElementById('res_sw_backing').textContent = backingStuds + ' studs (' + cornerStuds + ' crn, ' + interStuds + ' int)';
        document.getElementById('res_sw_openings').textContent = totalOpeningFramingStuds + ' studs (' + openingKingsJacks + ' k/j, ' + crippleStuds + ' crp)';
        document.getElementById('res_sw_total_studs').textContent = totalStudsWithWaste + ' studs (' + Math.round(wastePct * 100) + '% waste)';
        document.getElementById('res_sw_plate_lf').textContent = plateLfWithWaste + ' LF (' + numPlates + ' plates)';
        document.getElementById('res_sw_plate_boards').textContent = plateBoards16Ft + ' boards (2x4 or 2x6 x 16\')';
        document.getElementById('res_sw_sheets_1s').textContent = sheetsOneSide + ' sheets';
        document.getElementById('res_sw_sheets_2s').textContent = sheetsBothSides + ' sheets';
    }

    document.getElementById('btn_calc_sw').addEventListener('click', calculateStudWall);
    calculateStudWall();
});
</script>"""

    article_content = """<h2>1. Architectural Framing Systems &amp; Stud Wall Mechanics</h2>
<p>Light-frame timber and cold-formed steel stud construction represent the dominant building methodology for low-rise residential, institutional, and commercial structures across North America, Australasia, and Europe. Engineered for high strength-to-weight performance, a platform-framed stud wall serves as a structural diaphragm: vertical studs resist axial gravity loads from roofs, snow, and upper floor joists, while providing lateral flexural resistance against perpendicular wind loads.</p>

<p>Every standard framed wall comprises horizontal and vertical structural components configured to form rigid planar assemblies:</p>
<ul>
    <li><strong>Sole / Bottom Plate:</strong> A horizontal dimensional lumber member anchored directly to the concrete foundation slab (using pressure-treated wood and anchor bolts per IRC Section R403.1.6) or fastened into subfloor wood joists.</li>
    <li><strong>Common Vertical Studs:</strong> Evenly spaced vertical members running between the bottom plate and top plate, precision-cut to accommodate standard ceiling heights (precut \(92\frac{5}{8}\text{ in}\) for 8-ft ceilings, \(104\frac{5}{8}\text{ in}\) for 9-ft ceilings).</li>
    <li><strong>Double Top Plates:</strong> Two stacked horizontal boards. The lower top plate ties the vertical studs together; the upper top plate overlaps adjacent walls at corners and wall splices, mechanically locking intersecting wall assemblies together to transfer lateral diaphragm shears.</li>
    <li><strong>Header Assemblies:</strong> Horizontal beam spans placed over doors and windows to divert roof and floor loads around the opening into adjacent supporting studs.</li>
</ul>

<h2>2. 16-Inch vs. 24-Inch On-Center Framing Disciplines</h2>
<p>The spacing of vertical studs is governed by building code structural span tables (IRC Section R602.3 and IBC Section 2308):</p>

<h3>16-Inch On-Center (OC) Conventional Framing</h3>
<p>The traditional construction standard specifies studs placed exactly \(16\text{ inches}\) center-to-center. This configuration aligns with standard \(48\text{ inch}\) sheet goods (\(16 \times 3 = 48\)), guaranteeing that every third stud provides a rigid joint for drywall and plywood seams. It provides superior axial load capacity, accommodates high-deflection exterior siding, and permits using standard \(1/2\text{ inch}\) gypsum wallboard without risking ceiling or wall sagging.</p>

<h3>24-Inch On-Center (OC) Advanced Framing (OVE)</h3>
<p>Developed under the principles of <strong>Optimum Value Engineering (OVE)</strong>, \(24\text{ inch}\) OC framing aligns roof trusses, wall studs, and floor joists in a direct vertical load path ("in-line framing"). This discipline delivers measurable advantages:</p>
<ul>
    <li>Reduces total framing lumber consumption by <strong>25% to 30%</strong>.</li>
    <li>Replaces solid timber with insulation cavity volume, eliminating thermal bridging and raising exterior wall effective R-values by 15% to 20%.</li>
    <li>Requires \(5/8\text{ inch}\) drywall or specialized sag-resistant gypsum panels to span the wider \(24\text{''}\) spacing without surface bowing.</li>
</ul>

<h2>3. Mathematical Takeoff Formulations</h2>
<p>Accurate lumber material estimation requires accounting for linear spacing, plate multiplication, framing junctions, and rough opening assemblies:</p>

<h3>Common Stud Calculation</h3>
<p>To span a wall length \(L\) (in feet) at an on-center spacing \(OC\) (in inches), the baseline number of common studs is calculated as:</p>

$$N_{common} = \text{ceil}\left(\frac{L \times 12}{OC}\right) + 1$$

<p>The addition of \(+1\) accounts for the closing end stud.</p>

<h3>Corner Assemblies and Drywall Backing</h3>
<p>Standard framing requires substantial backing lumber to provide continuous nailing surfaces for interior drywall sheets:</p>
<ul>
    <li><strong>Three-Stud Corner / California Corner:</strong> Adds \(2\) additional studs per \(90^\circ\) corner.</li>
    <li><strong>Partition Intersection (T-Junction):</strong> Adding an intersecting interior wall requires a 3-stud backing channel or ladder blocking, contributing \(2\) additional studs per junction.</li>
</ul>

$$N_{backing} = (2 \times N_{corners}) + (2 \times N_{intersections})$$

<h3>Door and Window Opening Assemblies</h3>
<p>Each rough wall opening requires specialized framing members:</p>
<ul>
    <li><strong>King Studs:</strong> Full-length vertical studs running continuously from bottom plate to top plate on each side of the opening (\(2\) per opening).</li>
    <li><strong>Jack / Trimmer Studs:</strong> Shortened vertical studs nailed to the inside face of the king studs that physically bear the concentrated weight of the overhead structural header (\(2\) per opening).</li>
    <li><strong>Cripple Studs:</strong> Short framing pieces placed above the header or below window rough sills, maintaining regular \(16\text{''}\) or \(24\text{''}\) modular layout.</li>
</ul>

$$N_{openings} = (4 \times N_{openings}) + N_{cripples}$$

<h3>Total Studs with Contractor Waste Allowance</h3>
$$N_{total} = \text{ceil}\left(\left(N_{common} + N_{backing} + N_{openings}\right) \times (1 + w_{waste})\right)$$

<p>where \(w_{waste}\) typically equals \(0.10\) to \(0.15\) (10% to 15%) to account for warped boards, knots, fire-blocking cuts, and job-site culling.</p>

<h2>4. IRC Header Span Capacity Reference Table</h2>
<p>The following engineering data table specifies allowable header lumber sizes and maximum opening clear spans for exterior bearing walls supporting a roof and ceiling per <strong>IRC Table R602.7(1)</strong> (assuming #2 Douglas Fir / Southern Pine lumber stock):</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Header Member Size</th>
            <th>Building Width: 20 Feet</th>
            <th>Building Width: 28 Feet</th>
            <th>Building Width: 36 Feet</th>
            <th>Min Number of Jack/Trimmer Studs</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>(2) 2 x 4 Lumber</strong></td>
            <td>3 ft – 6 in</td>
            <td>3 ft – 1 in</td>
            <td>2 ft – 8 in</td>
            <td>1 Jack each side</td>
        </tr>
        <tr>
            <td><strong>(2) 2 x 6 Lumber</strong></td>
            <td>5 ft – 5 in</td>
            <td>4 ft – 8 in</td>
            <td>4 ft – 2 in</td>
            <td>1 Jack each side</td>
        </tr>
        <tr>
            <td><strong>(2) 2 x 8 Lumber</strong></td>
            <td>6 ft – 10 in</td>
            <td>5 ft – 11 in</td>
            <td>5 ft – 4 in</td>
            <td>1 Jack each side</td>
        </tr>
        <tr>
            <td><strong>(2) 2 x 10 Lumber</strong></td>
            <td>8 ft – 5 in</td>
            <td>7 ft – 3 in</td>
            <td>6 ft – 6 in</td>
            <td>2 Jacks each side (&gt;6 ft span)</td>
        </tr>
        <tr>
            <td><strong>(2) 2 x 12 Lumber</strong></td>
            <td>9 ft – 9 in</td>
            <td>8 ft – 5 in</td>
            <td>7 ft – 7 in</td>
            <td>2 Jacks each side (&gt;6 ft span)</td>
        </tr>
        <tr>
            <td><strong>(2) 1.75" LVL (Engineered)</strong></td>
            <td>14 ft – 2 in</td>
            <td>12 ft – 4 in</td>
            <td>11 ft – 0 in</td>
            <td>2 to 3 Jacks each side</td>
        </tr>
    </tbody>
</table>

<h2>5. Worked Construction Case Study: 24-Foot Exterior Load-Bearing Wall</h2>
<div class="worked-example-card">
    <h3>Framing Takeoff Specification: 24-Foot x 8-Foot Exterior Wall</h3>
    <p>A residential contractor is framing an exterior load-bearing wall measuring <strong>24.0 feet in length</strong> and <strong>8.0 feet in height</strong>. Construction details specify: <strong>16-inch OC stud spacing</strong>; standard triple plate configuration (1 bottom sole plate + 2 top plates); <strong>two 90-degree corner assemblies</strong>; <strong>one interior partition T-wall intersection</strong>; <strong>one 3-foot entry door</strong>; and <strong>two 3-foot x 4-foot windows</strong>. The contractor applies a standard <strong>15% lumber waste allowance</strong> and orders 16-foot dimensional lumber boards for the horizontal plates.</p>

    <div class="step-solution">
        <h4>Step 1: Calculate Base Common Studs</h4>
        $$N_{common} = \text{ceil}\left(\frac{24\text{ ft} \times 12}{16\text{ in}}\right) + 1 = \text{ceil}\left(\frac{288}{16}\right) + 1 = 18 + 1 = 19\text{ studs}$$

        <h4>Step 2: Calculate Corner and Intersection Backing Studs</h4>
        <p>Two corners requiring 2 extra studs each for California drywall backing:</p>
        $$N_{corners} = 2 \times 2 = 4\text{ studs}$$
        <p>One T-intersection requiring 2 extra studs for drywall nailer channel:</p>
        $$N_{intersections} = 1 \times 2 = 2\text{ studs}$$
        $$N_{backing} = 4 + 2 = 6\text{ studs}$$

        <h4>Step 3: Calculate Rough Opening Framing Members</h4>
        <p>Total openings = 1 door + 2 windows = 3 openings.</p>
        <p>Kings &amp; Jacks: 3 openings \(\times\) 4 studs (2 kings + 2 trimmers) = 12 studs.</p>
        <p>Cripple studs: door (2 cripples above header) + 2 windows (3 upper/lower cripples each = 6) = 8 cripple studs.</p>
        $$N_{openings,raw} = 12 + 8 = 20\text{ studs}$$

        <h4>Step 4: Total Stud Takeoff with 15% Waste Allowance</h4>
        $$N_{raw,total} = 19\text{ (common)} + 6\text{ (backing)} + 20\text{ (openings)} = 45\text{ studs}$$
        $$N_{order} = \text{ceil}(45 \times 1.15) = \text{ceil}(51.75) = 52\text{ precut } 92\frac{5}{8}\text{'' studs}$$

        <h4>Step 5: Horizontal Plates Lumber Takeoff</h4>
        <p>Three continuous plates \(\times 24\text{ linear feet} = 72\text{ Linear Feet (LF)}\).</p>
        <p>Adding 15% cutting and splice waste: \(72 \times 1.15 = 82.8\text{ LF}\).</p>
        <p>Specifying standard 16-foot dimensional lumber boards:</p>
        $$N_{plate\_boards} = \text{ceil}\left(\frac{82.8}{16}\right) = 6\text{ boards of } 2\times 4 \times 16\text{ ft}$$

        <h4>Step 6: Drywall / Sheathing Estimate</h4>
        <p>Gross wall area: \(24\text{ ft} \times 8\text{ ft} = 192\text{ sq ft}\).</p>
        <p>Deducting rough openings: 1 door (\(21\text{ sq ft}\)) + 2 windows (\(15\text{ sq ft each} = 30\text{ sq ft}\)) = \(51\text{ sq ft}\).</p>
        <p>Net wall area: \(192 - 51 = 141\text{ sq ft}\).</p>
        <p>Sheathing sheets (\(4\times 8\text{ ft} = 32\text{ sq ft}\)) with 10% cut waste:</p>
        $$N_{sheets} = \text{ceil}\left(\frac{141 \times 1.10}{32}\right) = 5\text{ sheets (exterior sheathing)}, \quad 10\text{ sheets (both interior/exterior faces)}$$
    </div>
</div>

<h2>6. Frequently Asked Questions</h2>
<div class="faq-accordion">
    <div class="faq-item">
        <h3>What is the difference between 16-inch and 24-inch on-center (OC) stud spacing?</h3>
        <p>16-inch on-center (OC) framing is the traditional structural standard for load-bearing exterior and interior walls, providing superior lateral stiffness, high vertical compressive capacity, and continuous backing for 1/2-inch drywall. 24-inch OC framing (Advanced Framing or Optimum Value Engineering) uses ~30% less lumber, enhances wall thermal performance by expanding insulation cavity area, but requires 5/8-inch drywall or structural sheathing to prevent surface sagging.</p>
    </div>
    <div class="faq-item">
        <h3>Why do standard walls require a double top plate?</h3>
        <p>A double top plate ties adjacent wall segments together at corner intersections and splices, providing structural continuity against wind shear and seismic forces. Furthermore, it distributes concentrated point loads from roof trusses and floor joists that do not align directly over vertical wall studs.</p>
    </div>
    <div class="faq-item">
        <h3>How many extra studs are needed for corners, wall intersections, and rough openings?</h3>
        <p>Each 90-degree corner typically requires 2 to 3 extra studs (for 3-stud or California corner nailer assemblies). Each interior T-junction wall intersection requires 2 extra studs for drywall backing. Each door or window rough opening requires 2 king studs, 2 jack (trimmer) studs, a structural header (2x6 to 2x12), and upper/lower cripple studs.</p>
    </div>
    <div class="faq-item">
        <h3>What waste factor should be added when ordering framing lumber?</h3>
        <p>Professional framing contractors typically add a 10% to 15% waste allowance to stud and plate orders to account for warped boards, excessive knots, crown culling, trimming scrap, and short blocking/firestop lumber requirements.</p>
    </div>
</div>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article_content)


# ---------------------------------------------------------------------------
# Tool 8: Plaster Calculator
# ---------------------------------------------------------------------------
def gen_plaster_calculator():
    slug = "plaster-calculator"
    title = "Plaster Calculator | Cement & Sand Quantity Material Estimator"
    desc = "Calculate plaster mortar materials: cement bags, sand volume in cubic meters and cubic feet, water requirements, dry bulking volume, and joint waste factors."
    h1 = "Plaster Calculator"
    short_desc = "Calculate cement bags (50kg), sand volume, dry bulking factor (1.33), joint waste, and water requirements for interior and exterior wall plastering."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Plaster Calculator",
      "url": "https://calchub.com/plaster-calculator.html",
      "applicationCategory": "EngineeringApplication",
      "operatingSystem": "All",
      "description": "Calculate cement bags, fine sand volume, dry mortar bulking allowance, and mixing water for interior and exterior wall plastering.",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Why is a dry volume multiplier of 1.30 to 1.35 (typically 1.33) used in plaster calculations?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "When dry sand and cement powders are mixed with water, the fine cement particles dissolve and fill the microscopic interstitial voids between the larger sand grains. Consequently, dry unmixed mortar contracts by approximately 30% to 35% when transitioning into dense, plastic wet mortar. To produce 1.0 cubic meter of finished wet plaster, estimators must prepare 1.30 to 1.35 cubic meters (standardly 1.33 m³) of dry constituent materials."
          }
        },
        {
          "@type": "Question",
          "name": "What are the recommended cement-to-sand plaster mix ratios for different surfaces?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Common civil engineering mix ratios include: 1:3 for RCC ceiling plaster and damp-proof/waterproofing coats; 1:4 for exterior exposed brick/block masonry walls subject to heavy rainfall; 1:5 or 1:6 for interior smooth wall plastering; and 1:6 for general second-coat finishing over rough masonry."
          }
        },
        {
          "@type": "Question",
          "name": "What is the standard recommended thickness for wall and ceiling plaster?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Standard plaster thicknesses are: 6 mm to 8 mm (1/4 inch) for smooth RCC concrete ceiling slabs; 12 mm (1/2 inch) for internal masonry wall surfaces; 15 mm (5/8 inch) for rough or uneven internal brickwork; and 18 mm to 20 mm (3/4 inch) applied in two coats (12 mm base scratch coat + 8 mm finish coat) for weather-resistant exterior walls."
          }
        },
        {
          "@type": "Question",
          "name": "How much extra plaster is allowed for joint filling and surface unevenness?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Civil estimators add a 15% to 20% waste allowance to the calculated net wet volume. This accounts for mortar filling deep masonry joints (raked mortar grooves), irregular brick alignment, rebound drop loss during troweling, and edge trimming."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calculator-form">
    <div class="calc-row">
        <div class="calc-field">
            <label for="pl_area_unit">Area Measurement Unit:</label>
            <select id="pl_area_unit">
                <option value="sqm" selected>Square Meters (m²)</option>
                <option value="sqft">Square Feet (sq ft)</option>
            </select>
        </div>
        <div class="calc-field">
            <label for="pl_area">Plastering Surface Area:</label>
            <input type="number" id="pl_area" value="100" step="1" min="1">
            <small class="field-hint">Net wall/ceiling area after window/door deductions</small>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="pl_thickness">Plaster Thickness:</label>
            <select id="pl_thickness">
                <option value="6">6 mm (~1/4") - RCC Concrete Ceiling</option>
                <option value="12" selected>12 mm (~1/2") - Standard Internal Wall</option>
                <option value="15">15 mm (~5/8") - Rough Brick / Uneven Masonry</option>
                <option value="20">20 mm (~3/4") - Exterior Two-Coat Waterproof</option>
            </select>
        </div>
        <div class="calc-field">
            <label for="pl_ratio">Cement : Sand Mortar Mix Ratio:</label>
            <select id="pl_ratio">
                <option value="3">1 : 3 (Ceiling / High Strength / Waterproof)</option>
                <option value="4" selected>1 : 4 (Standard Exterior Walls)</option>
                <option value="5">1 : 5 (Internal Brick Masonry)</option>
                <option value="6">1 : 6 (Internal AAC Block / Smooth Finish)</option>
            </select>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="pl_waste">Joint Filling &amp; Rebound Waste Factor (%):</label>
            <input type="number" id="pl_waste" value="20" step="1" min="5" max="35">
            <small class="field-hint">Recommended: 15% - 20% for brickwork joints &amp; trowel rebound</small>
        </div>
        <div class="calc-field">
            <label for="pl_bag_weight">Cement Bag Unit Weight:</label>
            <select id="pl_bag_weight">
                <option value="50" selected>50 kg Bag (Standard International / IS / BS)</option>
                <option value="42.6">94 lb Bag (1 US Bag / ~42.6 kg)</option>
            </select>
        </div>
    </div>
    <button type="button" class="btn btn-primary" id="btn_calc_pl" style="width:100%; margin-top:1rem;">Calculate Plaster Materials</button>

    <div class="calc-results" id="pl_results" style="margin-top:1.5rem;">
        <h3>Plaster Material Estimation Takeoff</h3>
        <div class="results-grid">
            <div class="result-item">
                <span class="result-label">Net Wet Mortar Volume:</span>
                <span class="result-value" id="res_pl_wet_vol">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Total Dry Volume (Factor 1.33 + Waste):</span>
                <span class="result-value" id="res_pl_dry_vol">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Cement Required (Bags):</span>
                <span class="result-value" id="res_pl_cement_bags">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Cement Weight (kg / lbs):</span>
                <span class="result-value" id="res_pl_cement_wt">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Sand Volume (Cubic Meters):</span>
                <span class="result-value" id="res_pl_sand_m3">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Sand Volume (Cubic Feet / cft):</span>
                <span class="result-value" id="res_pl_sand_cft">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Sand Weight (Metric Tons):</span>
                <span class="result-value" id="res_pl_sand_tons">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Mixing Water Requirement:</span>
                <span class="result-value" id="res_pl_water">--</span>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    function calculatePlaster() {
        const unit = document.getElementById('pl_area_unit').value;
        let areaVal = parseFloat(document.getElementById('pl_area').value) || 100;
        const thicknessMm = parseFloat(document.getElementById('pl_thickness').value) || 12;
        const sandPart = parseFloat(document.getElementById('pl_ratio').value) || 4;
        const wastePct = (parseFloat(document.getElementById('pl_waste').value) || 20) / 100;
        const bagWeightKg = parseFloat(document.getElementById('pl_bag_weight').value) || 50;

        // Convert area to square meters if input is sq ft
        let areaSqm = (unit === 'sqft') ? (areaVal * 0.092903) : areaVal;
        const thicknessM = thicknessMm / 1000;

        // 1. Wet Mortar Volume = Area * Thickness
        const wetVolM3 = areaSqm * thicknessM;

        // 2. Add waste & joint filling allowance:
        // wet_with_waste = wetVolM3 * (1 + wastePct)
        // 3. Convert to dry volume using bulking / void factor 1.33:
        // Dry Volume = wet_with_waste * 1.33
        const dryVolM3 = wetVolM3 * (1 + wastePct) * 1.33;

        // 4. Cement volume in m3:
        // Total parts = 1 (cement) + sandPart
        const totalParts = 1 + sandPart;
        const cementVolM3 = dryVolM3 * (1 / totalParts);

        // Density of dry loose cement = 1440 kg/m3
        const cementWeightKg = cementVolM3 * 1440;
        const cementBags = cementWeightKg / bagWeightKg;

        // 5. Sand volume in m3:
        const sandVolM3 = dryVolM3 * (sandPart / totalParts);
        // Sand in cubic feet (1 m3 = 35.3147 cft)
        const sandCft = sandVolM3 * 35.3147;
        // Density of dry river sand = 1600 kg/m3 => Tons = (m3 * 1600) / 1000
        const sandMetricTons = (sandVolM3 * 1600) / 1000;

        // 6. Water requirement: Water-cement ratio ~0.50
        const waterLiters = cementWeightKg * 0.50;

        const wetVolCft = wetVolM3 * 35.3147;
        const dryVolCft = dryVolM3 * 35.3147;

        document.getElementById('res_pl_wet_vol').textContent = wetVolM3.toFixed(3) + ' m³ (' + wetVolCft.toFixed(1) + ' cft)';
        document.getElementById('res_pl_dry_vol').textContent = dryVolM3.toFixed(3) + ' m³ (' + dryVolCft.toFixed(1) + ' cft)';
        document.getElementById('res_pl_cement_bags').textContent = Math.ceil(cementBags * 10) / 10 + ' Bags (' + Math.ceil(cementBags) + ' to order)';
        document.getElementById('res_pl_cement_wt').textContent = Math.round(cementWeightKg).toLocaleString() + ' kg (' + Math.round(cementWeightKg * 2.20462).toLocaleString() + ' lbs)';
        document.getElementById('res_pl_sand_m3').textContent = sandVolM3.toFixed(3) + ' m³';
        document.getElementById('res_pl_sand_cft').textContent = sandCft.toFixed(1) + ' cft';
        document.getElementById('res_pl_sand_tons').textContent = sandMetricTons.toFixed(2) + ' Metric Tons';
        document.getElementById('res_pl_water').textContent = Math.round(waterLiters) + ' Liters (W/C = 0.50)';
    }

    document.getElementById('btn_calc_pl').addEventListener('click', calculatePlaster);
    document.getElementById('pl_area_unit').addEventListener('change', calculatePlaster);
    document.getElementById('pl_thickness').addEventListener('change', calculatePlaster);
    document.getElementById('pl_ratio').addEventListener('change', calculatePlaster);
    calculatePlaster();
});
</script>"""

    article_content = """<h2>1. Civil Engineering Principles of Wall and Ceiling Plastering</h2>
<p>Plastering represents one of the most critical finishing operations in civil building construction, providing both aesthetic uniformity and vital structural envelope protection. In reinforced concrete (RCC) frame and masonry load-bearing structures, raw brickwork, concrete blocks, and exposed concrete surfaces present irregular joint lines, micro-fissures, and high water absorption porosity. Applying a dense, well-graded cement-sand plaster mortar fulfills three essential functions:</p>
<ul>
    <li><strong>Weatherproofing &amp; Moisture Barrier:</strong> Shields porous masonry bricks and clay blocks against torrential rain intrusion, efflorescence crystallization, and freeze-thaw spalling.</li>
    <li><strong>Fire Resistance &amp; Acoustic Attenuation:</strong> Delivers non-combustible mineral mass that substantially enhances fire rating duration (providing 1 to 2 hours of additional thermal barrier protection) while dampening airborne sound transmission.</li>
    <li><strong>Geometric Rectification:</strong> Levels plumb deviations, corrects out-of-square wall intersections, and creates a smooth, durable substrate for paint, tiles, or decorative wall cladding.</li>
</ul>

<h2>2. The Physics of Dry Bulking and Wet Shrinkage</h2>
<p>In construction estimating, the single most widespread error is directly multiplying wall surface area by plaster thickness to estimate material orders. When dry hydraulic Portland cement powder and granular sand particles are combined with mixing water, the fine cement particles (specific surface area \(\approx 300\text{ to } 350\text{ m}^2/\text{kg}\)) dissolve into a colloidal paste that flows directly into the microscopic interstitial void spaces between adjacent sand grains.</p>

<p>Because these voids are occupied by hydrating paste rather than contributing to bulk volume, dry mortar experiences a volumetric contraction of <strong>30% to 35%</strong> upon wetting and consolidation. Conversely, to produce \(1.0\text{ m}^3\) of compacted, dense wet mortar, civil engineering standards mandate multiplying wet volume by a <strong>Dry Volume Factor of 1.30 to 1.35 (standardly 1.33)</strong>:</p>

$$V_{dry} = V_{wet} \times 1.33$$

<h3>Joint Filling and Trowel Rebound Losses</h3>
<p>In addition to dry shrinkage, mortar applied to brick or concrete block masonry is pressed deeply into raked mortar joints (\(10\text{ mm}\) deep) and compensates for surface undulations. Furthermore, when masons apply mortar with a hand trowel, a fraction drops to the floor (rebound loss). Construction estimators account for this by incorporating a <strong>15% to 20% waste factor</strong>:</p>

$$V_{adjusted,dry} = V_{wet} \times (1 + w_{waste}) \times 1.33$$

<h2>3. Governing Mix Formulations &amp; Material Densities</h2>
<p>For a specified cement-to-sand volumetric ratio of \(1 : n\) (where \(1\) represents Portland cement and \(n\) represents fine aggregate sand), total dry mortar volume is divided into proportional components:</p>

<h3>Cement Volume and Bag Quantity</h3>
$$\text{Cement Volume } (V_c) = V_{adjusted,dry} \times \left(\frac{1}{1 + n}\right) \quad [\text{m}^3]$$

<p>The standard nominal dry loose density of Ordinary Portland Cement (OPC) is universally calibrated at <strong>\(1{,}440\text{ kg/m}^3\)</strong>. The mass of cement in kilograms is:</p>

$$M_{cement} = V_c \times 1{,}440\text{ kg/m}^3$$

<p>A standard international commercial cement bag contains \(50\text{ kg}\) (occupying approximately \(0.03472\text{ m}^3\) or \(1.226\text{ ft}^3\)). The number of bags required is:</p>

$$N_{bags} = \frac{M_{cement}}{50\text{ kg}} = \frac{V_c}{0.03472\text{ m}^3}$$

<h3>Fine Sand Volume and Weight</h3>
$$\text{Sand Volume } (V_s) = V_{adjusted,dry} \times \left(\frac{n}{1 + n}\right) \quad [\text{m}^3]$$

<p>Converting sand volume from cubic meters (\(\text{m}^3\)) to cubic feet (\(\text{cft}\)) using the imperial conversion factor \(1\text{ m}^3 = 35.3147\text{ cft}\):</p>

$$V_{s,cft} = V_s \times 35.3147$$

<p>Assuming clean river sand with a typical bulk density of \(1{,}600\text{ kg/m}^3\), sand weight in metric tons is:</p>

$$M_{sand} = \frac{V_s \times 1{,}600\text{ kg/m}^3}{1{,}000} \quad [\text{Metric Tons}]$$

<h3>Water-Cement Ratio (\(W/C\))</h3>
<p>To ensure full hydration of calcium silicates without inducing excessive drying shrinkage cracks or plastic bleeding, the water-cement ratio is maintained between <strong>0.45 and 0.55</strong>:</p>

$$\text{Water Volume (Liters)} = M_{cement} \times (W/C)$$

<h2>4. Empirical Plaster Mix Ratios &amp; Thickness Standards Table</h2>
<p>The following engineering data table specifies recommended plaster mix designs, layer thicknesses, and curing standards across structural building assemblies:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Application Substrate</th>
            <th>Recommended Mix Ratio (Cement:Sand)</th>
            <th>Standard Thickness</th>
            <th>Number of Coats</th>
            <th>Minimum Moist Curing Period</th>
            <th>Primary Engineering Objective</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>RCC Concrete Ceiling</strong></td>
            <td>1 : 3</td>
            <td>6 mm – 8 mm</td>
            <td>Single coat</td>
            <td>7 Days</td>
            <td>High bond strength, overhead anti-delamination</td>
        </tr>
        <tr>
            <td><strong>Interior Brick Masonry</strong></td>
            <td>1 : 5 or 1 : 6</td>
            <td>12 mm</td>
            <td>Single coat</td>
            <td>7 Days</td>
            <td>Smooth finish, low shrinkage, paint substrate</td>
        </tr>
        <tr>
            <td><strong>Rough / Uneven Masonry</strong></td>
            <td>1 : 4 or 1 : 5</td>
            <td>15 mm</td>
            <td>Single coat</td>
            <td>10 Days</td>
            <td>Corrects wall plumb alignment up to 1/2"</td>
        </tr>
        <tr>
            <td><strong>Exterior Weather Wall</strong></td>
            <td>1 : 4</td>
            <td>18 mm – 20 mm</td>
            <td>Two coats (12mm base + 8mm finish)</td>
            <td>14 Days</td>
            <td>Waterproof barrier against driving rain</td>
        </tr>
        <tr>
            <td><strong>DPC / Basement Waterproofing</strong></td>
            <td>1 : 3 + Integral compound</td>
            <td>20 mm</td>
            <td>Two coats</td>
            <td>14 Days</td>
            <td>Hydrostatic head resistance, damp proofing</td>
        </tr>
    </tbody>
</table>

<h2>5. Worked Engineering Case Study: 100 Square Meter External Wall Plastering</h2>
<div class="worked-example-card">
    <h3>Material Takeoff Specification: 100 m² Exterior Brick Wall Plaster</h3>
    <p>A civil contractor is preparing a material purchase order for plastering <strong>100 square meters (\(100\text{ m}^2\))</strong> of exterior clay brick masonry. Project specifications mandate: a finished plaster thickness of <strong>12 mm</strong>; a <strong>1 : 4 cement-to-sand mortar mix ratio</strong>; a <strong>20% waste allowance</strong> for masonry raked joints and rebound loss; a <strong>dry volume conversion factor of 1.33</strong>; and standard <strong>50 kg Ordinary Portland Cement bags</strong>.</p>

    <div class="step-solution">
        <h4>Step 1: Compute Net Wet Mortar Volume</h4>
        $$t = 12\text{ mm} = 0.012\text{ m}$$
        $$V_{wet} = 100\text{ m}^2 \times 0.012\text{ m} = 1.20\text{ m}^3$$

        <h4>Step 2: Add 20% Joint Filling &amp; Rebound Allowance</h4>
        $$V_{wet,adjusted} = 1.20\text{ m}^3 \times (1 + 0.20) = 1.44\text{ m}^3$$

        <h4>Step 3: Convert to Dry Volume Using 1.33 Bulking Factor</h4>
        $$V_{dry} = 1.44\text{ m}^3 \times 1.33 = 1.9152\text{ m}^3$$

        <h4>Step 4: Calculate Cement Volume, Weight, and Bag Count</h4>
        <p>Proportion of cement in 1 : 4 mix: \(\frac{1}{1 + 4} = \frac{1}{5} = 0.20\)</p>
        $$V_{cement} = 1.9152\text{ m}^3 \times 0.20 = 0.38304\text{ m}^3$$
        <p>Using cement density of \(1{,}440\text{ kg/m}^3\):</p>
        $$M_{cement} = 0.38304\text{ m}^3 \times 1{,}440\text{ kg/m}^3 = 551.58\text{ kg}$$
        <p>Converting to 50 kg bags:</p>
        $$N_{bags} = \frac{551.58\text{ kg}}{50\text{ kg}} = 11.03\text{ bags}$$
        <p>The contractor specifies <strong>12 bags of 50 kg OPC cement</strong>.</p>

        <h4>Step 5: Calculate Fine Sand Volume and Weight</h4>
        <p>Proportion of sand in 1 : 4 mix: \(\frac{4}{1 + 4} = \frac{4}{5} = 0.80\)</p>
        $$V_{sand} = 1.9152\text{ m}^3 \times 0.80 = 1.53216\text{ m}^3$$
        <p>Converting to cubic feet (\(\text{cft}\)):</p>
        $$V_{sand,cft} = 1.53216\text{ m}^3 \times 35.3147 = 54.11\text{ cft}$$
        <p>Calculating sand mass using density of \(1{,}600\text{ kg/m}^3\):</p>
        $$M_{sand} = \frac{1.53216 \times 1{,}600}{1{,}000} \approx 2.45\text{ Metric Tons}$$

        <h4>Step 6: Compute Water Requirement</h4>
        <p>Assuming an optimal water-cement ratio \(W/C = 0.50\):</p>
        $$\text{Water} = 551.58\text{ kg} \times 0.50 \approx 276\text{ Liters}$$
        <p>Summary of site delivery order: <strong>12 Bags Cement (50kg)</strong>, <strong>55 cft (2.5 Tons) Washed River Sand</strong>, and clean potable mixing water.</p>
    </div>
</div>

<h2>6. Frequently Asked Questions</h2>
<div class="faq-accordion">
    <div class="faq-item">
        <h3>Why is a dry volume multiplier of 1.30 to 1.35 (typically 1.33) used in plaster calculations?</h3>
        <p>When dry sand and cement powders are mixed with water, the fine cement particles dissolve and fill the microscopic interstitial voids between the larger sand grains. Consequently, dry unmixed mortar contracts by approximately 30% to 35% when transitioning into dense, plastic wet mortar. To produce 1.0 cubic meter of finished wet plaster, estimators must prepare 1.30 to 1.35 cubic meters (standardly 1.33 m³) of dry constituent materials.</p>
    </div>
    <div class="faq-item">
        <h3>What are the recommended cement-to-sand plaster mix ratios for different surfaces?</h3>
        <p>Common civil engineering mix ratios include: 1:3 for RCC ceiling plaster and damp-proof/waterproofing coats; 1:4 for exterior exposed brick/block masonry walls subject to heavy rainfall; 1:5 or 1:6 for interior smooth wall plastering; and 1:6 for general second-coat finishing over rough masonry.</p>
    </div>
    <div class="faq-item">
        <h3>What is the standard recommended thickness for wall and ceiling plaster?</h3>
        <p>Standard plaster thicknesses are: 6 mm to 8 mm (1/4 inch) for smooth RCC concrete ceiling slabs; 12 mm (1/2 inch) for internal masonry wall surfaces; 15 mm (5/8 inch) for rough or uneven internal brickwork; and 18 mm to 20 mm (3/4 inch) applied in two coats (12 mm base scratch coat + 8 mm finish coat) for weather-resistant exterior walls.</p>
    </div>
    <div class="faq-item">
        <h3>How much extra plaster is allowed for joint filling and surface unevenness?</h3>
        <p>Civil estimators add a 15% to 20% waste allowance to the calculated net wet volume. This accounts for mortar filling deep masonry joints (raked mortar grooves), irregular brick alignment, rebound drop loss during troweling, and edge trimming.</p>
    </div>
</div>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article_content)


def main():
    tools = [
        ("stud-wall-calculator.html", gen_stud_wall()),
        ("plaster-calculator.html", gen_plaster_calculator())
    ]
    for filename, content in tools:
        filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {filename}")

if __name__ == "__main__":
    main()
