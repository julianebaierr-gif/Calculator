# -*- coding: utf-8 -*-
"""
Generator for Batch 38 - Part 3
Tools:
5. wallpaper-calculator.html
6. wavelength-calculator.html
"""

import os

COMMON_TAIL = """    <footer class="site-footer">
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>About CalcHub</h4>
                    <p>CalcHub provides free, high-precision engineering calculators, unit converters, and analytical tools designed for practicing engineers, physicists, architects, and interior designers worldwide.</p>
                </div>
                <div class="footer-col">
                    <h4>Engineering &amp; Science Categories</h4>
                    <ul>
                        <li><a href="physics.html">Physics &amp; Electromagnetics</a></li>
                        <li><a href="civil.html">Civil &amp; Architectural Finishing</a></li>
                        <li><a href="engineering.html">Electrical &amp; RF Engineering</a></li>
                        <li><a href="converter.html">Unit Converters</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Popular Calculators</h4>
                    <ul>
                        <li><a href="wallpaper-calculator.html">Wallpaper Roll Calculator</a></li>
                        <li><a href="wavelength-calculator.html">Wavelength Calculator</a></li>
                        <li><a href="stair-calculator.html">Stair Framing</a></li>
                        <li><a href="stud-wall-calculator.html">Stud Wall Framing</a></li>
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
                    <h3>Related Tools</h3>
                    <ul class="sidebar-links">
                        <li><a href="wallpaper-calculator.html">Wallpaper Roll Calculator</a></li>
                        <li><a href="wavelength-calculator.html">Wavelength Calculator</a></li>
                        <li><a href="paint-calculator.html">Paint Gallon &amp; Coverage</a></li>
                        <li><a href="drywall-calculator.html">Drywall Sheets &amp; Compound</a></li>
                        <li><a href="flooring-calculator.html">Flooring Area &amp; Box Estimator</a></li>
                        <li><a href="tile-calculator.html">Tile, Grout &amp; Mortar</a></li>
                        <li><a href="stud-wall-calculator.html">Stud Wall Framing</a></li>
                        <li><a href="plaster-calculator.html">Plaster Material Estimator</a></li>
                        <li><a href="frequency-converter.html">Frequency Converter</a></li>
                        <li><a href="speed-converter.html">Speed &amp; Velocity Converter</a></li>
                    </ul>
                </div>
            </aside>
        </div>
    </div>
{COMMON_TAIL}"""


# ---------------------------------------------------------------------------
# Tool 5: Wallpaper Calculator
# ---------------------------------------------------------------------------
def gen_wallpaper():
    slug = "wallpaper-calculator"
    title = "Wallpaper Calculator | Roll Estimator, Pattern Repeat & Drop Match"
    desc = "Calculate how many wallpaper rolls you need: accounts for room perimeter, wall height, pattern repeats (straight & drop match), window/door deductions, and adhesive paste."
    h1 = "Wallpaper Calculator"
    short_desc = "Estimate required wallpaper rolls (single and double rolls), pattern repeat waste, drop match allowances, strip counts, and adhesive paste requirements."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Wallpaper Calculator",
      "url": "https://calchub.com/wallpaper-calculator.html",
      "applicationCategory": "DesignApplication",
      "operatingSystem": "All",
      "description": "Calculate wallpaper roll requirements, pattern repeat waste, strip count, and adhesive coverage for interior residential and commercial decorating.",
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
          "name": "What is the difference between a straight match, drop match, and random match in wallpaper?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A random match has no repeating design across strips (solids, grasscloth, vertical stripes), creating zero pattern waste. A straight match aligns pattern elements horizontally at identical heights across adjacent strips. A drop match (or half-drop match) shifts the repeating motif vertically by half the repeat length on each alternating strip to create diagonal visual flow, increasing scrap waste by 15% to 25%."
          }
        },
        {
          "@type": "Question",
          "name": "What are the standard dimensions of American Double Rolls vs. European Metric Rolls?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "An American Double Roll typically measures 20.5 inches wide by 33 feet long (covering 56.4 sq ft) or 27 inches wide by 27 feet long (covering 60.75 sq ft). A European Metric Single Roll measures 53 cm (20.8 inches) wide by 10.05 meters (32.9 feet) long, covering approximately 5.33 square meters (57.3 square feet)."
          }
        },
        {
          "@type": "Question",
          "name": "Why should you NOT deduct small windows and doors from wallpaper orders?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Professional paperhangers advise against subtracting windows and doors under 20 square feet because wallpaper strips must be hung continuously around openings. The cutouts above and below windows frequently cannot be reused on full-height walls if a pattern repeat is present, meaning subtracting them risks stranding the installer without enough matching roll length."
          }
        },
        {
          "@type": "Question",
          "name": "How is the number of usable strips per roll calculated?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The cut length of each strip equals Wall Height + Pattern Repeat + 4 inches (trimming allowance at ceiling and baseboard). The number of strips per roll is: Floor(Roll Length / Cut Length). For example, a 33-foot roll hung on an 8-foot wall with a 12-inch repeat gives Cut Length = 8' + 1' + 4\" = 9'4\" (9.33 ft). 33 / 9.33 = 3 usable strips per roll."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calculator-form">
    <div class="calc-row">
        <div class="calc-field">
            <label for="wp_room_len">Room Length (Feet):</label>
            <input type="number" id="wp_room_len" value="14" step="0.5" min="1">
        </div>
        <div class="calc-field">
            <label for="wp_room_wid">Room Width (Feet):</label>
            <input type="number" id="wp_room_wid" value="12" step="0.5" min="1">
            <small class="field-hint">Room perimeter = 2 × (L + W)</small>
        </div>
        <div class="calc-field">
            <label for="wp_wall_hgt">Wall Height (Feet):</label>
            <input type="number" id="wp_wall_hgt" value="8.5" step="0.25" min="6" max="25">
            <small class="field-hint">Floor to ceiling finished height</small>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="wp_roll_type">Roll Standard Size:</label>
            <select id="wp_roll_type">
                <option value="us_205" selected>American Double Roll (20.5" × 33 ft / 56.4 sq ft)</option>
                <option value="us_27">American Commercial (27" × 27 ft / 60.75 sq ft)</option>
                <option value="euro_53">European Metric Roll (53 cm × 10.05 m / 57.3 sq ft)</option>
            </select>
        </div>
        <div class="calc-field">
            <label for="wp_repeat">Pattern Repeat (Inches):</label>
            <select id="wp_repeat">
                <option value="0">0" (Solid / Texture / Random Match - 0% waste)</option>
                <option value="6">6" Repeat (Small Floral / Geometric)</option>
                <option value="12" selected>12" Repeat (Medium Pattern)</option>
                <option value="18">18" Repeat (Large Motif / Damask)</option>
                <option value="24">24" Repeat (Oversized Mural Repeat)</option>
            </select>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="wp_match_type">Match Configuration:</label>
            <select id="wp_match_type">
                <option value="random">Random Match (Free Match - 0% loss)</option>
                <option value="straight" selected>Straight Match (Standard Horizontal Alignment)</option>
                <option value="drop">Drop Match / Half-Drop Match (Diagonal Pattern)</option>
            </select>
        </div>
        <div class="calc-field">
            <label for="wp_openings">Windows &amp; Large Doors to Deduct:</label>
            <select id="wp_openings">
                <option value="none">Do Not Deduct (Recommended for Safety)</option>
                <option value="mod" selected>Moderate (Deduct 1 Standard Door + 2 Windows ~50 sq ft)</option>
                <option value="large">Substantial (Large French Doors + Picture Window ~100 sq ft)</option>
            </select>
        </div>
    </div>
    <button type="button" class="btn btn-primary" id="btn_calc_wp" style="width:100%; margin-top:1rem;">Calculate Wallpaper Rolls &amp; Materials</button>

    <div class="calc-results" id="wp_results" style="margin-top:1.5rem;">
        <h3>Wallpaper Material Estimation Summary</h3>
        <div class="results-grid">
            <div class="result-item">
                <span class="result-label">Gross Wall Area:</span>
                <span class="result-value" id="res_wp_gross_area">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Net Surface to Cover:</span>
                <span class="result-value" id="res_wp_net_area">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Total Vertical Strips Required:</span>
                <span class="result-value" id="res_wp_strips_req">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Usable Strips per Roll:</span>
                <span class="result-value" id="res_wp_strips_per_roll">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Calculated Rolls (Strict):</span>
                <span class="result-value" id="res_wp_rolls_raw">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Recommended Rolls to Order (w/ 10% Margin):</span>
                <span class="result-value" id="res_wp_rolls_order">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Cut Scrap &amp; Waste Factor:</span>
                <span class="result-value" id="res_wp_waste_pct">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Wallpaper Paste Required:</span>
                <span class="result-value" id="res_wp_paste">--</span>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    function calculateWallpaper() {
        const len = parseFloat(document.getElementById('wp_room_len').value) || 14;
        const wid = parseFloat(document.getElementById('wp_room_wid').value) || 12;
        const hgt = parseFloat(document.getElementById('wp_wall_hgt').value) || 8.5;
        const rollType = document.getElementById('wp_roll_type').value;
        const repeatIn = parseFloat(document.getElementById('wp_repeat').value) || 0;
        const matchType = document.getElementById('wp_match_type').value;
        const openings = document.getElementById('wp_openings').value;

        // Perimeter = 2 * (L + W)
        const perimeterFt = 2 * (len + wid);
        const grossArea = perimeterFt * hgt;

        // Deductions
        let deduction = 0;
        if (openings === 'mod') deduction = 50;
        else if (openings === 'large') deduction = 100;
        const netArea = Math.max(0, grossArea - deduction);

        // Roll dimensions
        let rollWidthIn = 20.5;
        let rollLenFt = 33.0;
        let rollArea = 56.4;

        if (rollType === 'us_27') {
            rollWidthIn = 27.0;
            rollLenFt = 27.0;
            rollArea = 60.75;
        } else if (rollType === 'euro_53') {
            rollWidthIn = 20.86; // 53 cm
            rollLenFt = 32.97;   // 10.05 m
            rollArea = 57.3;
        }

        const rollWidthFt = rollWidthIn / 12;

        // Total vertical strips needed to cover perimeter
        const totalStripsReq = Math.ceil(perimeterFt / rollWidthFt);

        // Cut length of each strip:
        // Height + trim allowance (4 inches = 0.33 ft) + repeat allowance
        let repeatAllowanceFt = 0;
        if (matchType === 'straight') {
            repeatAllowanceFt = repeatIn / 12;
        } else if (matchType === 'drop') {
            repeatAllowanceFt = (repeatIn * 1.5) / 12;
        }
        const cutLengthFt = hgt + 0.33 + repeatAllowanceFt;

        // Number of usable strips per roll
        let stripsPerRoll = Math.floor(rollLenFt / cutLengthFt);
        if (stripsPerRoll < 1) stripsPerRoll = 1;

        // Rolls required via strip method
        const rollsNeeded = Math.ceil(totalStripsReq / stripsPerRoll);
        // Order with +1 safety roll or 10%
        const rollsToOrder = Math.max(rollsNeeded + 1, Math.ceil(rollsNeeded * 1.10));

        // Theoretical waste
        const theoreticalRollAreaUsed = rollsToOrder * rollArea;
        const wastePct = Math.round(((theoreticalRollAreaUsed - netArea) / theoreticalRollAreaUsed) * 100);

        // Adhesive paste estimation (1 gallon covers ~350-400 sq ft)
        const pasteGallons = Math.ceil(netArea / 350 * 10) / 10;
        const pasteKg = Math.ceil(netArea * 0.015 * 10) / 10;

        document.getElementById('res_wp_gross_area').textContent = Math.round(grossArea) + ' sq ft (' + (grossArea * 0.0929).toFixed(1) + ' m²)';
        document.getElementById('res_wp_net_area').textContent = Math.round(netArea) + ' sq ft (' + (netArea * 0.0929).toFixed(1) + ' m²)';
        document.getElementById('res_wp_strips_req').textContent = totalStripsReq + ' vertical drops';
        document.getElementById('res_wp_strips_per_roll').textContent = stripsPerRoll + ' drops/roll (' + cutLengthFt.toFixed(1) + ' ft/drop)';
        document.getElementById('res_wp_rolls_raw').textContent = rollsNeeded + ' rolls';
        document.getElementById('res_wp_rolls_order').textContent = rollsToOrder + ' rolls (+1 safety spare)';
        document.getElementById('res_wp_waste_pct').textContent = Math.max(5, wastePct) + '% (Match loss & cutoffs)';
        document.getElementById('res_wp_paste').textContent = pasteGallons + ' gal / ' + pasteKg + ' kg adhesive';
    }

    document.getElementById('btn_calc_wp').addEventListener('click', calculateWallpaper);
    document.getElementById('wp_room_len').addEventListener('input', calculateWallpaper);
    document.getElementById('wp_room_wid').addEventListener('input', calculateWallpaper);
    document.getElementById('wp_wall_hgt').addEventListener('input', calculateWallpaper);
    document.getElementById('wp_roll_type').addEventListener('change', calculateWallpaper);
    document.getElementById('wp_repeat').addEventListener('change', calculateWallpaper);
    document.getElementById('wp_match_type').addEventListener('change', calculateWallpaper);
    document.getElementById('wp_openings').addEventListener('change', calculateWallpaper);
    calculateWallpaper();
});
</script>"""

    article_content = """<h2>1. Architectural Principles of Wallcovering Installation</h2>
<p>In residential and commercial architectural interior design, wallpaper installation represents a precision finish trade combining surface geometry, material yield optimization, and pattern matching mechanics. Unlike uniform liquid wall paint—which is applied continuously with rollers and where coverage is a simple linear function of square footage—wallpaper consists of discrete pre-printed rolls of defined width and length. Estimating wallpaper orders solely by dividing total wall area by roll square footage results in acute material shortages because it ignores vertical repeat loss and strip truncation.</p>

<p>Every professional wallpaper material takeoff begins by establishing the primary spatial parameters:</p>
<ul>
    <li><strong>Room Perimeter:</strong> The total linear distance around the room walls: \(P = 2 \times (\text{Length} + \text{Width})\).</li>
    <li><strong>Finished Wall Height:</strong> The vertical distance from the top of the baseboard trim to the bottom of the crown molding or ceiling line.</li>
    <li><strong>Strip Width:</strong> The physical width of the paper roll, establishing how many vertical hanging drops are required to enclose the room perimeter.</li>
    <li><strong>Pattern Repeat &amp; Match Discipline:</strong> The vertical spatial interval between recurring motifs printed on the substrate.</li>
</ul>

<h2>2. Pattern Match Classifications &amp; Scrap Waste Mechanics</h2>
<p>The single greatest driver of wallpaper scrap waste is the <strong>Pattern Match Type</strong>:</p>

<h3>1. Random Match (Free Match)</h3>
<p>Wallcoverings with solid colors, vertical stripes, linen textures, or non-directional grasscloth fibers require no horizontal alignment between adjacent strips. Each succeeding strip is hung directly from where the prior strip ended on the roll, incurring <strong>0% pattern waste</strong>. Installers only account for a standard \(4\text{-inch}\) (\(10\text{ cm}\)) top-and-bottom trimming margin.</p>

<h3>2. Straight Match</h3>
<p>In a straight match design, pattern elements align horizontally across the wall at identical heights. The design motifs match straight across from strip to strip. When cutting each successive strip from the roll, the installer must align the motif with the prior strip, discarding an average scrap piece equal to the pattern repeat (\(6\text{ to } 18\text{ inches}\)):</p>

$$\text{Cut Length} = \text{Wall Height} + \text{Pattern Repeat} + \text{Trimming Margin (4'')}$$

<h3>3. Drop Match / Half-Drop Match</h3>
<p>In a drop match (most commonly a half-drop match), the pattern elements shift vertically by half the repeat distance on each alternating strip. This creates diagonal visual flow across the room. Because odd-numbered strips match with odd-numbered strips and even-numbered strips match with even-numbered strips, scrap losses increase to <strong>15% to 25%</strong> of the total roll area.</p>

<h2>3. Mathematical Strip Method Takeoff Formulations</h2>
<p>Professional paperhangers rely on the <strong>Vertical Strip Method</strong> rather than the crude square footage method:</p>

<h3>Step 1: Calculate Total Vertical Strips Required</h3>
$$N_{strips} = \text{ceil}\left(\frac{\text{Room Perimeter}}{\text{Roll Width}}\right)$$

<h3>Step 2: Calculate Usable Strips per Roll</h3>
$$\text{Strips per Roll} = \left\lfloor \frac{\text{Roll Length}}{\text{Cut Length}} \right\rfloor = \left\lfloor \frac{\text{Roll Length}}{\text{Wall Height} + \text{Repeat Allowance} + 0.33\text{ ft}} \right\rfloor$$

<h3>Step 3: Calculate Total Rolls to Order</h3>
$$N_{rolls,raw} = \text{ceil}\left(\frac{N_{strips}}{\text{Strips per Roll}}\right)$$

$$N_{order} = N_{rolls,raw} + 1\text{ (Spare Roll for Pattern Matching &amp; Damage)}$$

<p>A spare roll from the <strong>same manufacturing run dye lot</strong> is mandatory. Wallpaper rolls from different dye lots exhibit subtle ink pigmentation variances that appear visually jarring when hung side by side under natural daylight.</p>

<h2>4. Standard Roll Dimensions &amp; Specifications Table</h2>
<p>The following design data table outlines standard commercial and residential wallpaper roll formats, surface coverages, and typical applications:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Roll Standard</th>
            <th>Width</th>
            <th>Length</th>
            <th>Nominal Surface Area</th>
            <th>Usable Area (w/ repeat)</th>
            <th>Primary Application</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>American Double Roll (Standard)</strong></td>
            <td>20.5 inches (52 cm)</td>
            <td>33.0 feet (10.0 m)</td>
            <td>56.38 sq ft (5.24 m²)</td>
            <td>46 – 50 sq ft</td>
            <td>Residential living rooms, bedrooms, nurseries</td>
        </tr>
        <tr>
            <td><strong>American Commercial 27"</strong></td>
            <td>27.0 inches (68.6 cm)</td>
            <td>27.0 feet (8.23 m)</td>
            <td>60.75 sq ft (5.64 m²)</td>
            <td>50 – 54 sq ft</td>
            <td>Commercial hospitality, luxury residential</td>
        </tr>
        <tr>
            <td><strong>European Metric Single Roll</strong></td>
            <td>20.86 inches (53 cm)</td>
            <td>32.97 feet (10.05 m)</td>
            <td>57.30 sq ft (5.33 m²)</td>
            <td>47 – 51 sq ft</td>
            <td>British &amp; European imported designer papers</td>
        </tr>
        <tr>
            <td><strong>Type II Commercial Vinyl 54"</strong></td>
            <td>54.0 inches (137 cm)</td>
            <td>90.0 feet (30 yards)</td>
            <td>405.0 sq ft (37.6 m²)</td>
            <td>360 – 380 sq ft</td>
            <td>Hotels, hospital corridors, high-abuse corporate</td>
        </tr>
        <tr>
            <td><strong>Grasscloth / Natural Fiber</strong></td>
            <td>36.0 inches (91.4 cm)</td>
            <td>24.0 feet (8 yards)</td>
            <td>72.0 sq ft (6.69 m²)</td>
            <td>65 – 68 sq ft</td>
            <td>Textured feature walls, study rooms, dining</td>
        </tr>
    </tbody>
</table>

<h2>5. Worked Architectural Case Study: 14' x 12' Master Bedroom Feature Walls</h2>
<div class="worked-example-card">
    <h3>Wallpaper Takeoff Specification: Master Bedroom Suite</h3>
    <p>An interior designer is papering the four walls of a master bedroom measuring <strong>14.0 feet in length</strong> by <strong>12.0 feet in width</strong>, with a finished ceiling height of <strong>8.5 feet (102 inches)</strong>. The selected designer wallcovering is an <strong>American Double Roll (20.5 inches wide by 33.0 feet long)</strong> featuring an intricate floral damask with a <strong>12-inch straight pattern repeat</strong>. The room features one entry door (21 sq ft) and two windows (15 sq ft each). The designer calculates the exact roll requirement using the Vertical Strip Method.</p>

    <div class="step-solution">
        <h4>Step 1: Calculate Room Perimeter and Total Required Strips</h4>
        $$P = 2 \times (14.0\text{ ft} + 12.0\text{ ft}) = 2 \times 26.0 = 52.0\text{ Linear Feet}$$
        <p>Roll width in feet: \(20.5\text{ inches} / 12 = 1.7083\text{ feet}\).</p>
        $$N_{strips} = \text{ceil}\left(\frac{52.0\text{ ft}}{1.7083\text{ ft}}\right) = \text{ceil}(30.44) = 31\text{ vertical strips (drops)}$$

        <h4>Step 2: Calculate Cut Length per Strip with Repeat Allowance</h4>
        <p>Wall height = \(8.5\text{ ft}\) (\(102\text{ in}\)). Trimming margin at top and bottom = \(4\text{ in}\) (\(0.33\text{ ft}\)). Pattern repeat = \(12\text{ in}\) (\(1.0\text{ ft}\)).</p>
        $$\text{Cut Length} = 8.5\text{ ft} + 1.0\text{ ft} + 0.33\text{ ft} = 9.83\text{ feet (118 inches)}$$

        <h4>Step 3: Calculate Usable Strips per Roll</h4>
        $$\text{Strips per Roll} = \left\lfloor \frac{33.0\text{ ft}}{9.83\text{ ft}} \right\rfloor = \lfloor 3.35 \rfloor = 3\text{ usable strips per roll}$$
        <p><em>(Notice: The remaining \(33.0 - (3 \times 9.83) = 3.51\text{ feet}\) of roll end scrap cannot span the 8.5-foot wall height and is discarded or saved for above-door header cuts).</em></p>

        <h4>Step 4: Calculate Total Rolls to Order</h4>
        $$N_{rolls,raw} = \text{ceil}\left(\frac{31\text{ strips}}{3\text{ strips/roll}}\right) = \text{ceil}(10.33) = 11\text{ rolls}$$
        <p>Adding 1 safety spare roll for future damage or repair patching from the identical dye lot:</p>
        $$N_{order} = 11 + 1 = 12\text{ American Double Rolls}$$

        <h4>Step 5: Adhesive Paste Specification</h4>
        <p>Net surface area: \((52\text{ ft} \times 8.5\text{ ft}) - 51\text{ sq ft} = 442 - 51 = 391\text{ sq ft}\).</p>
        <p>At a standard commercial paste spread rate of 350 sq ft per gallon, the contractor specifies <strong>1.5 Gallons of heavy-duty pre-mixed clear vinyl adhesive paste</strong>.</p>
    </div>
</div>

<h2>6. Frequently Asked Questions</h2>
<div class="faq-accordion">
    <div class="faq-item">
        <h3>What is the difference between a straight match, drop match, and random match in wallpaper?</h3>
        <p>A random match has no repeating design across strips (solids, grasscloth, vertical stripes), creating zero pattern waste. A straight match aligns pattern elements horizontally at identical heights across adjacent strips. A drop match (or half-drop match) shifts the repeating motif vertically by half the repeat length on each alternating strip to create diagonal visual flow, increasing scrap waste by 15% to 25%.</p>
    </div>
    <div class="faq-item">
        <h3>What are the standard dimensions of American Double Rolls vs. European Metric Rolls?</h3>
        <p>An American Double Roll typically measures 20.5 inches wide by 33 feet long (covering 56.4 sq ft) or 27 inches wide by 27 feet long (covering 60.75 sq ft). A European Metric Single Roll measures 53 cm (20.8 inches) wide by 10.05 meters (32.9 feet) long, covering approximately 5.33 square meters (57.3 square feet).</p>
    </div>
    <div class="faq-item">
        <h3>Why should you NOT deduct small windows and doors from wallpaper orders?</h3>
        <p>Professional paperhangers advise against subtracting windows and doors under 20 square feet because wallpaper strips must be hung continuously around openings. The cutouts above and below windows frequently cannot be reused on full-height walls if a pattern repeat is present, meaning subtracting them risks stranding the installer without enough matching roll length.</p>
    </div>
    <div class="faq-item">
        <h3>How is the number of usable strips per roll calculated?</h3>
        <p>The cut length of each strip equals Wall Height + Pattern Repeat + 4 inches (trimming allowance at ceiling and baseboard). The number of strips per roll is: Floor(Roll Length / Cut Length). For example, a 33-foot roll hung on an 8-foot wall with a 12-inch repeat gives Cut Length = 8' + 1' + 4" = 9'4" (9.33 ft). 33 / 9.33 = 3 usable strips per roll.</p>
    </div>
</div>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article_content, "civil.html", "Civil & Finishing")


# ---------------------------------------------------------------------------
# Tool 6: Wavelength Calculator
# ---------------------------------------------------------------------------
def gen_wavelength():
    slug = "wavelength-calculator"
    title = "Wavelength Calculator | Frequency to Wavelength (λ = v/f) & RF Antennas"
    desc = "Calculate electromagnetic and acoustic wavelength (λ = v/f), quarter-wave antenna length, phase constant (β), velocity factor, and photon energy across radio, microwave and audio frequencies."
    h1 = "Wavelength Calculator"
    short_desc = "Compute wavelength (λ), half-wave and quarter-wave resonant antenna dimensions, wave number, phase constant, and photon energy across electromagnetic and acoustic spectrums."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Wavelength Calculator",
      "url": "https://calchub.com/wavelength-calculator.html",
      "applicationCategory": "EngineeringApplication",
      "operatingSystem": "All",
      "description": "Calculate electromagnetic and sound wavelength from frequency, propagation medium velocity factor, antenna resonant lengths, and phase constant.",
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
          "name": "What is the universal wave equation relating wavelength, frequency, and wave speed?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The universal wave equation is: λ = v / f, where λ (lambda) is wavelength in meters, v is the propagation velocity of the wave in the transmission medium in meters per second (m/s), and f is the oscillation frequency in Hertz (Hz). For electromagnetic waves in vacuum, v equals the speed of light: c = 299,792,458 m/s."
          }
        },
        {
          "@type": "Question",
          "name": "What is the Velocity Factor (VF) of a transmission line and why does it shorten wavelength?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Velocity factor (VF) is the ratio of wave propagation speed inside a dielectric medium to the speed of light in vacuum: VF = v / c = 1 / sqrt(ε_r), where ε_r is the relative dielectric permittivity. In coaxial cables with solid polyethylene (ε_r ≈ 2.25, VF ≈ 0.66), electromagnetic waves travel 34% slower than in air, shortening physical wavelength by exactly the same factor."
          }
        },
        {
          "@type": "Question",
          "name": "Why are quarter-wavelength (λ/4) and half-wavelength (λ/2) dimensions critical in antenna design?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "At integer fractions of a wavelength (specifically λ/4 for monopoles and λ/2 for center-fed dipoles), constructive interference between incident and reflected standing waves creates pure electrical resonance. At resonance, reactive inductive and capacitive impedances cancel out, leaving purely resistive radiation resistance and maximizing radiated electromagnetic power."
          }
        },
        {
          "@type": "Question",
          "name": "How does temperature affect acoustic wavelength in air?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The speed of sound in air is proportional to the square root of absolute thermodynamic temperature: v_sound ≈ 331.3 * sqrt(1 + T_c / 273.15) m/s (or approximately 331.3 + 0.606 * T_c). As air warms, sound speed increases, which lengthens acoustic wavelength for a constant audio frequency."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calculator-form">
    <div class="calc-row">
        <div class="calc-field">
            <label for="wl_type">Wave Physical Domain:</label>
            <select id="wl_type">
                <option value="em" selected>Electromagnetic (Radio, Microwave, Light, Laser)</option>
                <option value="sound">Acoustic / Sound (Air, Water, Solids)</option>
            </select>
        </div>
        <div class="calc-field">
            <label for="wl_medium">Propagation Medium / Transmission Line:</label>
            <select id="wl_medium">
                <option value="vacuum" selected>Vacuum / Free Air Space (c = 299,792,458 m/s)</option>
                <option value="coax_pe">Coaxial Cable - Solid PE (VF = 0.66)</option>
                <option value="coax_foam">Coaxial Cable - Foam PE (VF = 0.82)</option>
                <option value="coax_ptfe">Coaxial Cable - PTFE / Teflon (VF = 0.70)</option>
                <option value="pcb_fr4">PCB Microstrip - FR4 Substrate (VF ≈ 0.50)</option>
                <option value="custom_vf">Custom Dielectric Velocity Factor</option>
            </select>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="wl_freq_val">Frequency Value:</label>
            <input type="number" id="wl_freq_val" value="2.4" step="0.001" min="0.0001">
        </div>
        <div class="calc-field">
            <label for="wl_freq_unit">Frequency Unit:</label>
            <select id="wl_freq_unit">
                <option value="1">Hertz (Hz)</option>
                <option value="1e3">Kilohertz (kHz)</option>
                <option value="1e6">Megahertz (MHz)</option>
                <option value="1e9" selected>Gigahertz (GHz - e.g., 2.4 GHz WiFi)</option>
                <option value="1e12">Terahertz (THz)</option>
            </select>
        </div>
    </div>
    <div class="calc-row" id="box_wl_custom_vf" style="display:none;">
        <div class="calc-field">
            <label for="wl_custom_vf_val">Custom Velocity Factor (0.1 to 1.0):</label>
            <input type="number" id="wl_custom_vf_val" value="0.75" step="0.01" min="0.05" max="1.0">
            <small class="field-hint">VF = 1 / sqrt(dielectric constant ε_r)</small>
        </div>
    </div>
    <div class="calc-row" id="box_wl_sound_temp" style="display:none;">
        <div class="calc-field">
            <label for="wl_temp_c">Air Temperature (°C):</label>
            <input type="number" id="wl_temp_c" value="20" step="1" min="-40" max="60">
            <small class="field-hint">20°C standard room temperature (v = 343.4 m/s)</small>
        </div>
        <div class="calc-field">
            <label for="wl_sound_mat">Acoustic Medium:</label>
            <select id="wl_sound_mat">
                <option value="air" selected>Air (Gas)</option>
                <option value="water_fresh">Fresh Water (v = 1,482 m/s)</option>
                <option value="water_sea">Seawater (v = 1,522 m/s)</option>
                <option value="steel">Structural Steel (v = 5,960 m/s)</option>
            </select>
        </div>
    </div>
    <button type="button" class="btn btn-primary" id="btn_calc_wl" style="width:100%; margin-top:1rem;">Calculate Wavelength &amp; Resonance</button>

    <div class="calc-results" id="wl_results" style="margin-top:1.5rem;">
        <h3>Wave Mechanics &amp; Antenna Geometry</h3>
        <div class="results-grid">
            <div class="result-item">
                <span class="result-label">Full Wavelength (\\(\\lambda\\)):</span>
                <span class="result-value" id="res_wl_lambda_m">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Wavelength in Imperial:</span>
                <span class="result-value" id="res_wl_lambda_imp">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Half-Wave (\\(\\lambda/2\\) Dipole):</span>
                <span class="result-value" id="res_wl_half">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Quarter-Wave (\\(\\lambda/4\\) Monopole):</span>
                <span class="result-value" id="res_wl_quarter">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Phase Constant / Wave Number (\\(\\beta\\)):</span>
                <span class="result-value" id="res_wl_beta">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Wave Period (\\(T\\)):</span>
                <span class="result-value" id="res_wl_period">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Propagation Velocity (\\(v\\)):</span>
                <span class="result-value" id="res_wl_velocity">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Photon Energy (\\(E = hf\\)):</span>
                <span class="result-value" id="res_wl_photon">--</span>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const typeSelect = document.getElementById('wl_type');
    const medSelect = document.getElementById('wl_medium');
    const boxVf = document.getElementById('box_wl_custom_vf');
    const boxSound = document.getElementById('box_wl_sound_temp');

    typeSelect.addEventListener('change', function() {
        if (typeSelect.value === 'sound') {
            medSelect.parentElement.style.display = 'none';
            boxVf.style.display = 'none';
            boxSound.style.display = 'flex';
        } else {
            medSelect.parentElement.style.display = 'flex';
            boxSound.style.display = 'none';
            if (medSelect.value === 'custom_vf') boxVf.style.display = 'flex';
        }
    });

    medSelect.addEventListener('change', function() {
        if (medSelect.value === 'custom_vf') {
            boxVf.style.display = 'flex';
        } else {
            boxVf.style.display = 'none';
        }
    });

    function calculateWavelength() {
        const isSound = (typeSelect.value === 'sound');
        const freqVal = parseFloat(document.getElementById('wl_freq_val').value) || 1;
        const multiplier = parseFloat(document.getElementById('wl_freq_unit').value) || 1;
        const freqHz = freqVal * multiplier;
        if (freqHz <= 0) return;

        let velocity = 299792458; // c in m/s

        if (!isSound) {
            const med = medSelect.value;
            let vf = 1.0;
            if (med === 'coax_pe') vf = 0.66;
            else if (med === 'coax_foam') vf = 0.82;
            else if (med === 'coax_ptfe') vf = 0.70;
            else if (med === 'pcb_fr4') vf = 0.50;
            else if (med === 'custom_vf') {
                vf = parseFloat(document.getElementById('wl_custom_vf_val').value) || 0.75;
            }
            velocity = 299792458 * vf;
        } else {
            const mat = document.getElementById('wl_sound_mat').value;
            if (mat === 'air') {
                const tempC = parseFloat(document.getElementById('wl_temp_c').value) || 20;
                velocity = 331.3 * Math.sqrt(1 + (tempC / 273.15));
            } else if (mat === 'water_fresh') {
                velocity = 1482;
            } else if (mat === 'water_sea') {
                velocity = 1522;
            } else if (mat === 'steel') {
                velocity = 5960;
            }
        }

        // Wavelength lambda = v / f
        const lambdaM = velocity / freqHz;
        const lambdaMm = lambdaM * 1000;
        const lambdaCm = lambdaM * 100;
        const lambdaIn = lambdaM * 39.3701;
        const lambdaFt = lambdaM * 3.28084;

        // Formatted metric lambda
        let lambdaMetricStr = '';
        if (lambdaM >= 1000) lambdaMetricStr = (lambdaM / 1000).toFixed(3) + ' km';
        else if (lambdaM >= 1) lambdaMetricStr = lambdaM.toFixed(4) + ' m';
        else if (lambdaM >= 0.01) lambdaMetricStr = lambdaCm.toFixed(2) + ' cm (' + lambdaMm.toFixed(1) + ' mm)';
        else if (lambdaM >= 1e-6) lambdaMetricStr = (lambdaM * 1e6).toFixed(2) + ' µm (' + lambdaMm.toFixed(3) + ' mm)';
        else lambdaMetricStr = (lambdaM * 1e9).toFixed(1) + ' nm';

        // Formatted imperial lambda
        let lambdaImpStr = '';
        if (lambdaFt >= 1) lambdaImpStr = lambdaFt.toFixed(2) + ' ft (' + lambdaIn.toFixed(1) + ' in)';
        else lambdaImpStr = lambdaIn.toFixed(3) + ' inches';

        // Half-wave & quarter-wave
        const halfM = lambdaM / 2;
        const quarterM = lambdaM / 4;
        const halfIn = lambdaIn / 2;
        const quarterIn = lambdaIn / 4;

        const halfStr = (halfM >= 1 ? halfM.toFixed(3) + ' m' : (halfM * 100).toFixed(2) + ' cm') + ' (' + halfIn.toFixed(2) + '")';
        const quarterStr = (quarterM >= 1 ? quarterM.toFixed(3) + ' m' : (quarterM * 100).toFixed(2) + ' cm') + ' (' + quarterIn.toFixed(2) + '")';

        // Phase constant beta = 2 * pi / lambda
        const beta = (2 * Math.PI) / lambdaM;
        const periodSec = 1 / freqHz;

        let periodStr = '';
        if (periodSec >= 1e-3) periodStr = (periodSec * 1000).toFixed(2) + ' ms';
        else if (periodSec >= 1e-6) periodStr = (periodSec * 1e6).toFixed(2) + ' µs';
        else if (periodSec >= 1e-9) periodStr = (periodSec * 1e9).toFixed(3) + ' ns';
        else periodStr = (periodSec * 1e12).toFixed(3) + ' ps';

        // Photon energy E = h * f (h = 6.62607015e-34 J*s, 1 eV = 1.602176634e-19 J)
        const hPlanck = 6.62607015e-34;
        const eJoules = hPlanck * freqHz;
        const eEv = eJoules / 1.602176634e-19;

        let photonStr = '';
        if (isSound) {
            photonStr = 'N/A (Mechanical Wave)';
        } else {
            if (eEv >= 1e6) photonStr = (eEv / 1e6).toFixed(2) + ' MeV';
            else if (eEv >= 1e3) photonStr = (eEv / 1e3).toFixed(2) + ' keV';
            else if (eEv >= 1) photonStr = eEv.toFixed(3) + ' eV';
            else if (eEv >= 1e-6) photonStr = (eEv * 1e6).toFixed(2) + ' µeV';
            else photonStr = (eEv * 1e9).toFixed(2) + ' neV';
        }

        document.getElementById('res_wl_lambda_m').textContent = lambdaMetricStr;
        document.getElementById('res_wl_lambda_imp').textContent = lambdaImpStr;
        document.getElementById('res_wl_half').textContent = halfStr;
        document.getElementById('res_wl_quarter').textContent = quarterStr;
        document.getElementById('res_wl_beta').textContent = beta.toFixed(3) + ' rad/m';
        document.getElementById('res_wl_period').textContent = periodStr;
        document.getElementById('res_wl_velocity').textContent = Math.round(velocity).toLocaleString() + ' m/s';
        document.getElementById('res_wl_photon').textContent = photonStr;
    }

    document.getElementById('btn_calc_wl').addEventListener('click', calculateWavelength);
    document.getElementById('wl_freq_val').addEventListener('input', calculateWavelength);
    document.getElementById('wl_freq_unit').addEventListener('change', calculateWavelength);
    medSelect.addEventListener('change', calculateWavelength);
    calculateWavelength();
});
</script>"""

    article_content = """<h2>1. Fundamental Physics of Wave Mechanics and Wavelength</h2>
<p>In classical electrodynamics, quantum mechanics, and physical acoustics, a <strong>wave</strong> represents the propagation of a dynamic disturbance or oscillatory energy perturbation through spacetime or physical matter without transporting net bulk mass. The <strong>wavelength (\(\lambda\))</strong> is the spatial period of the wave—the physical Euclidean distance measured between two consecutive spatial points that occupy identical vibrational phase (such as two successive crests, troughs, or zero-crossings):</p>

<p>Every wave phenomenon is governed by the universal kinematic relation linking spatial wavelength \(\lambda\), temporal oscillation frequency \(f\), and phase propagation velocity \(v\):</p>

$$\lambda = \frac{v}{f}$$

<p>where:</p>
<ul>
    <li>\(\lambda\) (lambda) is wavelength measured in meters (\(\text{m}\)).</li>
    <li>\(v\) is the phase velocity of the wave in the transmission medium in meters per second (\(\text{m/s}\)).</li>
    <li>\(f\) is the temporal frequency measured in Hertz (\(\text{Hz} = \text{s}^{-1}\)).</li>
</ul>

<p>In vacuum, electromagnetic radiation (radio waves, microwaves, infrared, visible light, ultraviolet, X-rays, and gamma rays) propagates at the universal invariant physical constant—the <strong>speed of light (\(c\))</strong>, defined by the International Bureau of Weights and Measures (BIPM) as exactly:</p>

$$c = 299{,}792{,}458\text{ m/s} \approx 3.00 \times 10^8\text{ m/s}$$

<h2>2. Dielectric Permittivity &amp; Velocity Factor (VF) in RF Media</h2>
<p>When an electromagnetic wave transitions from free space into a physical dielectric transmission line (such as a coaxial cable, twisted pair, or printed circuit board stripline), its electric and magnetic fields polarize the bound orbital electrons of the insulating atoms. This dielectric polarization impedes wave propagation, slowing phase velocity below the vacuum speed of light:</p>

$$v = \frac{c}{\sqrt{\mu_r \cdot \epsilon_r}}$$

<p>where \(\epsilon_r\) is relative dielectric permittivity and \(\mu_r\) is relative magnetic permeability (for non-magnetic plastics, \(\mu_r \approx 1.0\)). The dimensionless ratio \(v / c\) is termed the <strong>Velocity Factor (\(VF\))</strong>:</p>

$$VF = \frac{v}{c} = \frac{1}{\sqrt{\epsilon_r}} \quad \implies \quad \lambda_{dielectric} = \lambda_0 \times VF$$

<p>Consequently, an RF signal traveling inside a coaxial cable with solid polyethylene insulation (\(\epsilon_r = 2.25, VF = 0.66\)) travels <strong>34% slower</strong> than in air, shortening its physical wavelength by 34%. Sizing antenna matching stubs or resonant PCB traces without factoring in the velocity factor causes catastrophic center-frequency mistuning.</p>

<h2>3. Acoustic Waves and Temperature Dependence in Compressible Fluid Media</h2>
<p>Unlike electromagnetic waves which oscillate without a physical medium, acoustic sound waves are mechanical longitudinal pressure waves requiring molecular collisions in compressible matter. In dry atmospheric air, the speed of sound is governed by thermodynamic gas kinetics and absolute Kelvin temperature (\(T\)):</p>

$$v_{sound} = \sqrt{\gamma \cdot R_{specific} \cdot T} = \sqrt{1.40 \times 287.05 \times (T_c + 273.15)}$$

<p>For ambient terrestrial temperatures between \(-20^\circ\text{C}\) and \(+40^\circ\text{C}\), this simplifies to the standard acoustic linear approximation:</p>

$$v_{sound} \approx 331.3 + 0.606 \times T_c \quad [\text{m/s}]$$

<p>At standard room temperature (\(20^\circ\text{C}\) / \(68^\circ\text{F}\)), sound travels at \(343.4\text{ m/s}\) (\(1{,}126\text{ ft/s}\)). A low-frequency \(40\text{ Hz}\) deep bass note from a concert subwoofer has a physical acoustic wavelength of \(8.58\text{ meters}\) (\(28.2\text{ feet}\)), necessitating large physical acoustic quarter-wave bass reflex port dimensions.</p>

<h2>4. Comprehensive Electromagnetic Spectrum &amp; Wavelength Benchmark Table</h2>
<p>The following physics reference table outlines the electromagnetic spectrum, frequency bands, physical wavelengths, photon energies (\(E = hf\)), and dominant technologies:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Spectral Band</th>
            <th>Frequency Range</th>
            <th>Wavelength in Vacuum (\(\lambda_0\))</th>
            <th>Photon Energy (\(E\))</th>
            <th>Primary Scientific &amp; Industrial Utilization</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>ELF / VLF Radio</strong></td>
            <td>3 Hz – 30 kHz</td>
            <td>100,000 km – 10 km</td>
            <td>12 feV – 124 peV</td>
            <td>Submarine naval communication through deep ocean</td>
        </tr>
        <tr>
            <td><strong>HF (High Frequency)</strong></td>
            <td>3 MHz – 30 MHz</td>
            <td>100 m – 10 m</td>
            <td>12.4 neV – 124 neV</td>
            <td>Amateur shortwave radio, skywave ionospheric bounce</td>
        </tr>
        <tr>
            <td><strong>VHF Radio</strong></td>
            <td>30 MHz – 300 MHz</td>
            <td>10 m – 1.0 m</td>
            <td>124 neV – 1.24 µeV</td>
            <td>FM broadcast radio, aviation VHF airband, marine radio</td>
        </tr>
        <tr>
            <td><strong>UHF Radio</strong></td>
            <td>300 MHz – 3 GHz</td>
            <td>1.0 m – 10 cm</td>
            <td>1.24 µeV – 12.4 µeV</td>
            <td>Cellular 4G/5G, Wi-Fi 2.4 GHz, GPS L1 (1575.42 MHz)</td>
        </tr>
        <tr>
            <td><strong>SHF Microwave</strong></td>
            <td>3 GHz – 30 GHz</td>
            <td>10 cm – 1.0 cm</td>
            <td>12.4 µeV – 124 µeV</td>
            <td>Wi-Fi 5/6 (5 GHz), satellite TV, radar, satellite uplink</td>
        </tr>
        <tr>
            <td><strong>EHF Millimeter Wave</strong></td>
            <td>30 GHz – 300 GHz</td>
            <td>10 mm – 1.0 mm</td>
            <td>124 µeV – 1.24 meV</td>
            <td>5G mmWave cellular, automotive anti-collision radar</td>
        </tr>
        <tr>
            <td><strong>Infrared (IR)</strong></td>
            <td>300 GHz – 430 THz</td>
            <td>1.0 mm – 700 nm</td>
            <td>1.24 meV – 1.77 eV</td>
            <td>Fiber optic telecom (1310/1550 nm), thermal imaging</td>
        </tr>
        <tr>
            <td><strong>Visible Light</strong></td>
            <td>430 THz – 750 THz</td>
            <td>700 nm – 400 nm</td>
            <td>1.77 eV – 3.10 eV</td>
            <td>Human vision, optical microscopy, photonics</td>
        </tr>
        <tr>
            <td><strong>Ultraviolet (UV)</strong></td>
            <td>750 THz – 30 PHz</td>
            <td>400 nm – 10 nm</td>
            <td>3.1 eV – 124 eV</td>
            <td>Semiconductor photolithography, germicidal sterilization</td>
        </tr>
        <tr>
            <td><strong>X-Rays &amp; Gamma</strong></td>
            <td>&gt; 30 PHz</td>
            <td>&lt; 10 nm (&lt; 0.01 nm)</td>
            <td>&gt; 124 eV (&gt; 100 keV)</td>
            <td>Medical diagnostic radiography, oncology radiotherapy</td>
        </tr>
    </tbody>
</table>

<h2>5. Antenna Resonance: Half-Wave Dipoles &amp; Quarter-Wave Monopoles</h2>
<p>Antenna geometry is dictated strictly by wavelength fractions. When an alternating RF current drives an antenna element whose physical length matches an odd harmonic fraction of the signal's electrical wavelength, <strong>standing wave resonance</strong> occurs:</p>

<h3>Half-Wave (\(\lambda/2\)) Center-Fed Dipole</h3>
<p>The fundamental dipole antenna comprises two symmetrical wire legs each measuring a quarter-wavelength (\(\lambda/4\)), totaling one half-wavelength end-to-end. At resonance, the terminal feedpoint impedance exhibits zero reactance and a pure radiation resistance of approximately <strong>\(73.13\text{ }\Omega\)</strong>, presenting a near-ideal match to standard \(75\text{ }\Omega\) or \(50\text{ }\Omega\) coaxial feedlines:</p>

$$L_{dipole} = \frac{\lambda_0}{2} \times k_{end}$$

<p>where \(k_{end} \approx 0.95\) is the antenna wire end-effect capacitive fringing velocity correction factor.</p>

<h3>Quarter-Wave (\(\lambda/4\)) Monopole Ground-Plane Antenna</h3>
<p>Mounted perpendicularly over an infinite conducting ground plane (or a vehicle roof), a quarter-wave vertical radiator mirrors itself in the ground plane to replicate half-wave dipole behavior. Its radiation resistance is exactly half that of a dipole: \(R_{rad} \approx 36.5\text{ }\Omega\):</p>

$$L_{monopole} = \frac{\lambda_0}{4} \times 0.95$$

<h2>6. Worked Engineering Case Study: Designing a 2.45 GHz Wi-Fi Monopole</h2>
<div class="worked-example-card">
    <h3>RF Engineering Specification: 2.45 GHz IoT Antenna Design</h3>
    <p>An embedded electronics engineer is designing a quarter-wave (\(\lambda/4\)) PCB trace antenna for a 2.45 GHz (\(2{,}450\text{ MHz}\)) Wi-Fi / Bluetooth IoT microcontroller. The engineer must calculate the free-space wavelength, determine the physical quarter-wave antenna trace length with an end-effect velocity factor \(k = 0.95\), and evaluate the phase constant \(\beta\).</p>

    <div class="step-solution">
        <h4>Step 1: Compute Vacuum Wavelength (\(\lambda_0\))</h4>
        $$f = 2.45\text{ GHz} = 2.45 \times 10^9\text{ Hz}$$
        $$\lambda_0 = \frac{c}{f} = \frac{299{,}792{,}458\text{ m/s}}{2.45 \times 10^9\text{ s}^{-1}} \approx 0.12236\text{ meters} \approx 12.24\text{ cm} \approx 122.4\text{ mm}$$

        <h4>Step 2: Calculate Quarter-Wave Radiator Length</h4>
        $$\frac{\lambda_0}{4} = \frac{122.36\text{ mm}}{4} = 30.59\text{ mm}$$
        <p>Applying the standard antenna end-effect velocity correction factor \(k = 0.95\):</p>
        $$L_{trace} = 30.59\text{ mm} \times 0.95 = 29.06\text{ mm} \approx 1.144\text{ inches}$$
        <p>A straight or meandered PCB trace measuring <strong>\(29.1\text{ mm}\)</strong> routed over a ground plane will resonate at \(2.45\text{ GHz}\).</p>

        <h4>Step 3: Compute Phase Constant (\(\beta\)) and Wave Period</h4>
        $$\beta = \frac{2\pi}{\lambda_0} = \frac{2\pi}{0.12236\text{ m}} \approx 51.35\text{ radians/meter}$$
        $$T = \frac{1}{f} = \frac{1}{2.45 \times 10^9\text{ Hz}} \approx 0.408 \times 10^{-9}\text{ seconds} = 408\text{ picoseconds}$$

        <h4>Step 4: Quantum Photon Energy</h4>
        $$E = h \cdot f = (6.626 \times 10^{-34}\text{ J}\cdot\text{s}) \times (2.45 \times 10^9\text{ s}^{-1}) = 1.623 \times 10^{-24}\text{ Joules}$$
        $$E(eV) = \frac{1.623 \times 10^{-24}\text{ J}}{1.602 \times 10^{-19}\text{ J/eV}} \approx 10.13\text{ }\mu\text{eV}$$
        <p>Because \(10.13\text{ }\mu\text{eV}\) is vastly lower than the \(12.4\text{ eV}\) ionizing threshold of chemical molecular bonds, 2.45 GHz RF radiation is strictly non-ionizing.</p>
    </div>
</div>

<h2>7. Frequently Asked Questions</h2>
<div class="faq-accordion">
    <div class="faq-item">
        <h3>What is the universal wave equation relating wavelength, frequency, and wave speed?</h3>
        <p>The universal wave equation is: \(\lambda = v / f\), where \(\lambda\) (lambda) is wavelength in meters, \(v\) is the propagation velocity of the wave in the transmission medium in meters per second (m/s), and \(f\) is the oscillation frequency in Hertz (Hz). For electromagnetic waves in vacuum, \(v\) equals the speed of light: \(c = 299{,}792{,}458\text{ m/s}\).</p>
    </div>
    <div class="faq-item">
        <h3>What is the Velocity Factor (VF) of a transmission line and why does it shorten wavelength?</h3>
        <p>Velocity factor (VF) is the ratio of wave propagation speed inside a dielectric medium to the speed of light in vacuum: \(VF = v / c = 1 / \sqrt{\epsilon_r}\), where \(\epsilon_r\) is relative dielectric permittivity. In coaxial cables with solid polyethylene (\(\epsilon_r \approx 2.25, VF \approx 0.66\)), electromagnetic waves travel 34% slower than in air, shortening physical wavelength by exactly the same factor.</p>
    </div>
    <div class="faq-item">
        <h3>Why are quarter-wavelength (λ/4) and half-wavelength (λ/2) dimensions critical in antenna design?</h3>
        <p>At integer fractions of a wavelength (specifically \(\lambda/4\) for monopoles and \(\lambda/2\) for center-fed dipoles), constructive interference between incident and reflected standing waves creates pure electrical resonance. At resonance, reactive inductive and capacitive impedances cancel out, leaving purely resistive radiation resistance and maximizing radiated electromagnetic power.</p>
    </div>
    <div class="faq-item">
        <h3>How does temperature affect acoustic wavelength in air?</h3>
        <p>The speed of sound in air is proportional to the square root of absolute thermodynamic temperature: \(v_{sound} \approx 331.3 \times \sqrt{1 + T_c / 273.15}\text{ m/s}\) (or approximately \(331.3 + 0.606 \times T_c\)). As air warms, sound speed increases, which lengthens acoustic wavelength for a constant audio frequency.</p>
    </div>
</div>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article_content, "physics.html", "Physics & RF")


def main():
    tools = [
        ("wallpaper-calculator.html", gen_wallpaper()),
        ("wavelength-calculator.html", gen_wavelength())
    ]
    for filename, content in tools:
        filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {filename}")

if __name__ == "__main__":
    main()
