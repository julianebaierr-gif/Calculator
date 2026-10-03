import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 5. COOKING CONVERTER
# -------------------------------------------------------------
cooking_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cooking Converter — Cups, Grams, Tablespoons, Ounces, mL | CalcHub</title>
  <meta name="description" content="Convert culinary recipe measurements between cups, tablespoons, teaspoons, milliliters, grams, and ounces with ingredient-specific density factors and baker's percentages.">
  <meta name="keywords" content="cooking converter, cups to grams, grams to cups flour, tablespoons to cups, ml to fl oz, baking recipe converter, butter stick to cups, culinary weight to volume, bakers percentage">
  <meta name="author" content="CalcHub Food Science & Culinary Metrology Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/cooking-converter.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="Cooking Converter — Cups, Grams, Tablespoons, Ounces, mL | CalcHub">
  <meta property="og:description" content="Convert culinary recipe measurements between cups, tablespoons, teaspoons, milliliters, grams, and ounces with ingredient-specific density factors and baker's percentages.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/cooking-converter.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/cooking-converter.html#app",
      "name": "Precision Culinary & Baking Recipe Converter",
      "url": "https://calchub.org/cooking-converter.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Professional culinary converter translating volumetric recipe measurements into grams and milliliters using ingredient-specific packing density metrology."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Universal Unit Converters", "item": "https://calchub.org/converter.html"},
        {"@type": "ListItem", "position": 3, "name": "Cooking Converter", "item": "https://calchub.org/cooking-converter.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Why does 1 cup of all-purpose flour weigh differently depending on how it is scooped?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Flour is a compressible particulate solid. Scooping directly from a bag with a measuring cup packs the flour tightly, yielding between 140 and 160 grams per cup. Sifting or fluffing with a fork before spooning into a cup ('spoon and level' method) yields approximately 120 to 125 grams per cup. This 30% volumetric variation is the primary cause of dry, dense cakes and bread failures in baking, which is why professional pastry chefs measure ingredients strictly by mass in grams."
          }
        },
        {
          "@type": "Question",
          "name": "What is the difference between a US Legal Cup, a US Customary Cup, and a Metric Cup?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The US Legal Cup (mandated by the FDA for nutrition facts labeling) equals exactly 240 milliliters. The US Customary Cup (used in traditional American cookbooks) equals 1/2 liquid pint, or 236.588 milliliters. In Australia, New Zealand, Canada, and parts of the Commonwealth, a Metric Cup equals exactly 250 milliliters. In the United Kingdom, traditional recipes occasionally reference the Imperial Cup, which equals 1/2 Imperial pint, or 284.13 milliliters."
          }
        },
        {
          "@type": "Question",
          "name": "How much does one standard American stick of butter weigh and measure?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "One standard American stick of butter equals 1/4 pound (4 ounces, or exactly 113.398 grams). In volumetric culinary measurements, one stick equals 1/2 US cup, or 8 tablespoons, or 24 teaspoons. Two full sticks equal 1 cup (226.8 grams)."
          }
        },
        {
          "@type": "Question",
          "name": "What are Baker's Percentages and why are they used in commercial bakeries?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In baker's percentages, the total weight of flour is always established as the 100% mathematical baseline, and all other ingredients (water, yeast, salt, fat, sugar) are calculated as a percentage relative to the flour weight. For example, a sourdough bread formula with 1,000 g flour, 700 g water, and 20 g salt has 70% hydration and 2% salt. This allows recipes to scale seamlessly from a single 500g loaf to a 500kg industrial production batch without recalculating individual ratios."
          }
        }
      ]
    }
  ]
}
  </script>
</head>
<body class="converter-page">
  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="logo">
        <span class="logo-badge">∑</span>
        <span>Calc<span class="accent">Hub</span></span>
      </a>
      <nav class="header-nav" aria-label="Main Navigation">
        <div class="nav-row">
          <a href="index.html" class="nav-link">🏠 Home</a>
          <a href="health.html" class="nav-link">⚖️ Health</a>
          <a href="finance.html" class="nav-link">🏦 Finance</a>
          <a href="math.html" class="nav-link">🔢 Math</a>
          <a href="engineering.html" class="nav-link">⚡ Electrical</a>
          <a href="solar-energy.html" class="nav-link">☀️ Solar</a>
          <a href="mechanical.html" class="nav-link">⚙️ Mechanical</a>
        </div>
        <div class="nav-row">
          <a href="civil.html" class="nav-link">🏗️ Civil</a>
          <a href="chemical.html" class="nav-link">🧪 Chemical</a>
          <a href="fire-safety.html" class="nav-link">🚨 Fire &amp; Safety</a>
          <a href="programmer.html" class="nav-link">👨‍💻 Programmer</a>
          <a href="datetime.html" class="nav-link">📅 Date &amp; Time</a>
          <a href="converter.html" class="nav-link active">🔄 Converter</a>
        </div>
      </nav>
    </div>
  </header>

  <main class="page-wrapper">
    <div class="converter-layout">
      <div class="converter-main">
        <div class="calculator-header">
          <div class="breadcrumbs">
            <a href="index.html">Home</a> &rsaquo;
            <a href="converter.html">Unit Converters</a> &rsaquo;
            <span>Cooking Converter</span>
          </div>
          <span class="badge">Culinary Metrology &amp; Food Science</span>
          <h1>Precision Cooking &amp; Baking Converter</h1>
          <p class="tagline">Convert volumetric recipe measurements (cups, tbsp, tsp, mL) to mass in grams using ingredient-specific packing densities.</p>
        </div>

        <div class="calculator-container card-surface">
          <div class="converter-box">
            <div style="margin-bottom:1rem;">
              <label for="cookIngredient" class="input-label">Select Ingredient (for Volume &harr; Weight Conversion):</label>
              <select id="cookIngredient" class="converter-select" style="font-weight:600;color:var(--primary);">
                <option value="water" selected>Water / Milk (1.00 g/mL &bull; 240g / cup)</option>
                <option value="flour_ap">All-Purpose Flour, Spooned (0.50 g/mL &bull; 120g / cup)</option>
                <option value="flour_packed">All-Purpose Flour, Scooped/Packed (0.60 g/mL &bull; 145g / cup)</option>
                <option value="sugar_white">Granulated White Sugar (0.83 g/mL &bull; 200g / cup)</option>
                <option value="sugar_brown">Brown Sugar, Packed (0.92 g/mL &bull; 220g / cup)</option>
                <option value="sugar_powdered">Powdered / Confectioners Sugar (0.50 g/mL &bull; 120g / cup)</option>
                <option value="butter">Butter / Margarine (0.95 g/mL &bull; 227g / cup &bull; 113g / stick)</option>
                <option value="honey">Honey / Maple Syrup / Molasses (1.42 g/mL &bull; 340g / cup)</option>
                <option value="oil_veg">Vegetable / Olive Oil (0.92 g/mL &bull; 220g / cup)</option>
                <option value="oats_rolled">Rolled Oats / Oatmeal (0.38 g/mL &bull; 90g / cup)</option>
                <option value="cocoa">Cocoa Powder, Unsweetened (0.42 g/mL &bull; 100g / cup)</option>
              </select>
            </div>

            <div class="converter-inputs-grid">
              <div class="input-col">
                <label for="cookFromVal" class="input-label">From Value</label>
                <input type="number" id="cookFromVal" class="converter-num-input" value="1" step="any" placeholder="Enter amount">
                <label for="cookFromUnit" class="input-label sub-label">From Unit</label>
                <select id="cookFromUnit" class="converter-select">
                  <optgroup label="Volume Units">
                    <option value="cup_us" selected>US Cups (240 mL)</option>
                    <option value="tbsp_us">US Tablespoons (14.79 mL)</option>
                    <option value="tsp_us">US Teaspoons (4.93 mL)</option>
                    <option value="fl_oz_us">US Fluid Ounces (29.57 mL)</option>
                    <option value="ml">Milliliters (mL)</option>
                    <option value="liter">Liters (L)</option>
                    <option value="cup_metric">Metric Cups (250 mL)</option>
                    <option value="pint_us">US Liquid Pints (473 mL)</option>
                    <option value="stick_butter">Butter Sticks (1/2 cup)</option>
                  </optgroup>
                  <optgroup label="Mass / Weight Units">
                    <option value="grams">Grams (g)</option>
                    <option value="kg">Kilograms (kg)</option>
                    <option value="oz_wt">Ounces (oz weight)</option>
                    <option value="lb_wt">Pounds (lbs weight)</option>
                  </optgroup>
                </select>
              </div>

              <div class="swap-col">
                <button type="button" id="cookSwapBtn" class="swap-button" title="Swap input and output units" aria-label="Swap units">
                  &#8644;
                </button>
              </div>

              <div class="input-col">
                <label for="cookToVal" class="input-label">Converted Value</label>
                <input type="text" id="cookToVal" class="converter-num-input output-val" readonly value="240.0">
                <label for="cookToUnit" class="input-label sub-label">To Unit</label>
                <select id="cookToUnit" class="converter-select">
                  <optgroup label="Volume Units">
                    <option value="cup_us">US Cups (240 mL)</option>
                    <option value="tbsp_us">US Tablespoons (14.79 mL)</option>
                    <option value="tsp_us">US Teaspoons (4.93 mL)</option>
                    <option value="fl_oz_us">US Fluid Ounces (29.57 mL)</option>
                    <option value="ml">Milliliters (mL)</option>
                    <option value="liter">Liters (L)</option>
                    <option value="cup_metric">Metric Cups (250 mL)</option>
                    <option value="pint_us">US Liquid Pints (473 mL)</option>
                    <option value="stick_butter">Butter Sticks (1/2 cup)</option>
                  </optgroup>
                  <optgroup label="Mass / Weight Units">
                    <option value="grams" selected>Grams (g)</option>
                    <option value="kg">Kilograms (kg)</option>
                    <option value="oz_wt">Ounces (oz weight)</option>
                    <option value="lb_wt">Pounds (lbs weight)</option>
                  </optgroup>
                </select>
              </div>
            </div>

            <div class="converter-quick-presets">
              <span class="preset-label">Standard Culinary Equivalents:</span>
              <button type="button" class="preset-chip" data-ing="flour_ap" data-val="1" data-from="cup_us" data-to="grams">1 Cup AP Flour (120g)</button>
              <button type="button" class="preset-chip" data-ing="sugar_white" data-val="1" data-from="cup_us" data-to="grams">1 Cup Sugar (200g)</button>
              <button type="button" class="preset-chip" data-ing="butter" data-val="1" data-from="stick_butter" data-to="grams">1 Stick Butter (113.4g)</button>
              <button type="button" class="preset-chip" data-ing="water" data-val="1" data-from="cup_us" data-to="tbsp_us">1 Cup = 16 Tablespoons</button>
            </div>

            <div class="conversion-summary-panel" id="cookSummaryCard">
              <div class="summary-line">
                <span class="summary-label">Recipe Formula:</span>
                <span class="summary-formula" id="cookEquation">1 US Cup = 240.0 Grams (Water)</span>
              </div>
              <div class="summary-submetrics">
                <div class="submetric-item">
                  <span class="submetric-name">Volume in mL:</span>
                  <span class="submetric-val" id="cookMlVal">240.0 mL</span>
                </div>
                <div class="submetric-item">
                  <span class="submetric-name">Weight in Ounces:</span>
                  <span class="submetric-val" id="cookOzVal">8.47 oz wt</span>
                </div>
                <div class="submetric-item">
                  <span class="submetric-name">Kitchen Spoon Breakdown:</span>
                  <span class="submetric-val" id="cookSpoonsVal">16 Tbsp | 48 Tsp</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <section>
            <h2>The Science of Culinary Metrology: Volume vs. Weight in the Kitchen</h2>
            <p>
              In gastronomy and professional pastry baking, ingredient measurement methods represent the divide between culinary success and recipe failure. In domestic American kitchens, recipes traditionally instruct cooks to measure ingredients by <strong>volume</strong> using sets of nested cups, tablespoons, and teaspoons. In contrast, European, Asian, and professional commercial kitchens around the globe measure ingredients strictly by <strong>mass</strong> in grams using digital kitchen scales.
            </p>
            <p>
              The fundamental flaw of volumetric measurement for dry particulate ingredients (such as flours, starches, cocoa, and sugars) is that dry powders do not behave as incompressible liquids. Particulate solids exhibit variable <strong>packing density</strong> depending on how they are transferred into the cup:
            </p>
            <ul>
              <li><strong>Aerated / Sifted:</strong> Fluffing flour introduces air voids between flour grains, yielding a low bulk density of approximately \(0.45\text{ to } 0.50\text{ g/mL}\) (~110 to 120 grams per US cup).</li>
              <li><strong>Scooped Directly:</strong> Dipping a measuring cup directly into a dense bag of flour compacts the starch granules, forcing air out and increasing bulk density to \(0.60\text{ to } 0.65\text{ g/mL}\) (~145 to 155 grams per US cup).</li>
            </ul>
            <p>
              A single baker who scoops flour directly from the bag accidentally adds up to <strong>30% more dry flour</strong> than a recipe developer who gently spooned and leveled the ingredient. This unintended 30% flour excess ruins bread gluten hydration, creates dry and rubbery cakes, and turns tender cookies into hard biscuits. Converting recipes to precise grams eliminates packing variables entirely.
            </p>
          </section>

          <section>
            <h2>Ingredient Density Matrix &amp; Exact Grams-per-Cup Equivalents</h2>
            <p>
              Converting volume to weight requires multiplying the measured liquid volume by the specific bulk packing density (\(\rho_{\text{bulk}}\)) of the chosen food ingredient:
            </p>
            <p>
              $$\text{Mass (grams)} = \text{Volume (mL)} \times \rho_{\text{bulk}}\text{ (g/mL)}$$
            </p>
            <p>
              The reference table below outlines the certified weight-to-volume relationships for core pantry staples standardized by the American Institute of Baking (AIB) and King Arthur Baking Company:
            </p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>Culinary Ingredient</th>
                  <th>Bulk Density (\(\text{g/mL}\))</th>
                  <th>1 US Cup (240 mL)</th>
                  <th>1 Metric Cup (250 mL)</th>
                  <th>1 US Tablespoon (15 mL)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Pure Water / Milk / Broth</strong></td>
                  <td>1.00 g/mL</td>
                  <td>240.0 g</td>
                  <td>250.0 g</td>
                  <td>15.0 g</td>
                </tr>
                <tr>
                  <td><strong>All-Purpose Flour (Spooned &amp; Leveled)</strong></td>
                  <td>0.50 g/mL</td>
                  <td>120.0 g</td>
                  <td>125.0 g</td>
                  <td>7.5 g</td>
                </tr>
                <tr>
                  <td><strong>Bread Flour (High Protein)</strong></td>
                  <td>0.53 g/mL</td>
                  <td>127.0 g</td>
                  <td>132.5 g</td>
                  <td>7.9 g</td>
                </tr>
                <tr>
                  <td><strong>Granulated White Cane Sugar</strong></td>
                  <td>0.83 g/mL</td>
                  <td>200.0 g</td>
                  <td>208.0 g</td>
                  <td>12.5 g</td>
                </tr>
                <tr>
                  <td><strong>Brown Sugar (Firmly Packed)</strong></td>
                  <td>0.92 g/mL</td>
                  <td>220.0 g</td>
                  <td>230.0 g</td>
                  <td>13.8 g</td>
                </tr>
                <tr>
                  <td><strong>Confectioners / Powdered Sugar</strong></td>
                  <td>0.50 g/mL</td>
                  <td>120.0 g</td>
                  <td>125.0 g</td>
                  <td>7.5 g</td>
                </tr>
                <tr>
                  <td><strong>Unsalted Butter (Solid Block)</strong></td>
                  <td>0.95 g/mL</td>
                  <td>226.8 g (2 sticks)</td>
                  <td>237.5 g</td>
                  <td>14.2 g</td>
                </tr>
                <tr>
                  <td><strong>Vegetable / Canola / Olive Oil</strong></td>
                  <td>0.92 g/mL</td>
                  <td>220.0 g</td>
                  <td>230.0 g</td>
                  <td>13.8 g</td>
                </tr>
                <tr>
                  <td><strong>Honey / Molasses / Corn Syrup</strong></td>
                  <td>1.42 g/mL</td>
                  <td>340.0 g</td>
                  <td>355.0 g</td>
                  <td>21.3 g</td>
                </tr>
                <tr>
                  <td><strong>Unsweetened Dutch Cocoa Powder</strong></td>
                  <td>0.42 g/mL</td>
                  <td>100.0 g</td>
                  <td>105.0 g</td>
                  <td>6.3 g</td>
                </tr>
                <tr>
                  <td><strong>Rolled Oats (Old Fashioned)</strong></td>
                  <td>0.38 g/mL</td>
                  <td>90.0 g</td>
                  <td>95.0 g</td>
                  <td>5.6 g</td>
                </tr>
                <tr>
                  <td><strong>Fine Table Salt (NaCl)</strong></td>
                  <td>1.20 g/mL</td>
                  <td>288.0 g</td>
                  <td>300.0 g</td>
                  <td>18.0 g (6.0 g/tsp)</td>
                </tr>
              </tbody>
            </table>
          </section>

          <section>
            <h2>Volumetric Measurement Hierarchies Across Global Territories</h2>
            <p>
              A major hazard when following international culinary recipes online is the regional variation in what constitutes a "cup" or a "tablespoon":
            </p>
            <ul>
              <li><strong>US Customary vs. US Legal Cup:</strong> In standard recipe books, a US customary cup is defined as \(1/16\text{ US gallon} = 8\text{ fl oz} \approx 236.59\text{ mL}\). However, the United States Food and Drug Administration (FDA) legally defines the cup as exactly \(240\text{ mL}\) for all commercial nutrition facts labeling. Modern measuring cups sold in North America are almost universally calibrated to \(240\text{ mL}\).</li>
              <li><strong>The Australian 20 mL Tablespoon:</strong> While the United States (14.79 mL), Canada (15.0 mL), the United Kingdom (15.0 mL), and New Zealand (15.0 mL) define a tablespoon as approximately 15 milliliters containing 3 teaspoons, <strong>Australia legally defines the tablespoon as 20 milliliters containing 4 teaspoons</strong>. Using an Australian measuring spoon set on an American baking recipe introduces a 33% excess of leavening agents such as baking powder or salt.</li>
              <li><strong>The British Imperial Fluid Ounce:</strong> One British Imperial fluid ounce equals \(28.413\text{ mL}\), whereas one US fluid ounce equals \(29.574\text{ mL}\). Conversely, an Imperial pint contains 20 fluid ounces (\(568.26\text{ mL}\)), whereas a US pint contains only 16 fluid ounces (\(473.18\text{ mL}\))—a difference of nearly 20%.</li>
            </ul>
          </section>

          <section>
            <h2>Baker's Percentages &amp; Sourdough Hydration Mathematics</h2>
            <p>
              In professional artisanal bakeries and commercial patisseries, recipes are written as <strong>Baker's Percentages</strong>. In this system, the total weight of flour is always indexed as 100%, and the weight of every other ingredient is calculated as a fraction of the flour mass:
            </p>
            <p>
              $$\text{Baker's } \% = \frac{\text{Weight of Ingredient}}{\text{Total Flour Weight}} \times 100\%$$
            </p>
            <p>
              This allows instant calculation of <strong>Dough Hydration</strong>:
            </p>
            <p>
              $$\text{Hydration } \% = \frac{\text{Total Water Weight}}{\text{Total Flour Weight}} \times 100\%$$
            </p>
            <p>
              Standard commercial white sandwich breads typically utilize 60% to 64% hydration (stiff, easy to shape by industrial machines), whereas rustic open-crumb artisanal sourdoughs range from 75% to 85% hydration (soft, wet dough requiring gentle stretch-and-fold fermentation techniques).
            </p>
          </section>

          <section>
            <h2>Worked Engineering Case Study: Commercial French Baguette Scaling</h2>
            <div class="worked-example-card">
              <h3>Culinary Scenario: Converting Home Volumetric Sourdough to Commercial Grams</h3>
              <p>
                An artisan baker is scaling an American domestic home recipe for French baguettes to produce <strong>50 loaves (each weighing 350 grams before baking, total dough mass = 17,500 grams)</strong>. The original home recipe is written in US volumetric cups:
              </p>
              <ul>
                <li>3 cups All-Purpose Bread Flour</li>
                <li>1 cup Water</li>
                <li>1.5 teaspoons Fine Salt</li>
                <li>1 teaspoon Instant Yeast</li>
              </ul>
              <p>The head baker needs to:</p>
              <ol>
                <li>Convert the single-batch home recipe into exact weights in grams.</li>
                <li>Calculate the exact Baker's Percentages (flour, hydration, salt, yeast).</li>
                <li>Scale the formula to yield precisely 17,500 grams of total mixed dough for the 50 commercial baguettes.</li>
              </ol>

              <h4>Step-by-Step Calculation:</h4>
              <p><strong>1. Single Batch Mass Conversion:</strong></p>
              <p>Bread Flour: \(3\text{ cups} \times 127\text{ g/cup} = \mathbf{381.0\text{ grams}}\)</p>
              <p>Water: \(1\text{ cup} \times 240\text{ g/cup} = \mathbf{240.0\text{ grams}}\)</p>
              <p>Salt: \(1.5\text{ tsp} \times 6.0\text{ g/tsp} = \mathbf{9.0\text{ grams}}\)</p>
              <p>Instant Yeast: \(1.0\text{ tsp} \times 3.1\text{ g/tsp} = \mathbf{3.1\text{ grams}}\)</p>
              <p>Single Batch Total Weight: \(381 + 240 + 9 + 3.1 = 633.1\text{ grams}\)</p>

              <p><strong>2. Compute Baker's Percentages (Flour = 100%):</strong></p>
              <p>Flour: \(381 / 381 \times 100\% = \mathbf{100.0\%}\)</p>
              <p>Water (Hydration): \(240 / 381 \times 100\% = \mathbf{63.0\%}\)</p>
              <p>Salt: \(9 / 381 \times 100\% = \mathbf{2.36\%}\)</p>
              <p>Yeast: \(3.1 / 381 \times 100\% = \mathbf{0.81\%}\)</p>
              <p>Total Formula Percentage: \(100 + 63.0 + 2.36 + 0.81 = \mathbf{166.17\%}\)</p>

              <p><strong>3. Scale to 17,500 Grams Total Dough:</strong></p>
              <p>$$\text{Total Flour Needed} = \frac{\text{Target Dough Mass}}{\text{Total Formula Decimal}} = \frac{17,500\text{ g}}{1.6617} \approx \mathbf{10,531.4\text{ g (10.53 kg)}}$$</p>
              <p>$$\text{Water Needed (63%)} = 10,531.4 \times 0.630 = \mathbf{6,634.8\text{ g (6.63 Liters)}}$$</p>
              <p>$$\text{Salt Needed (2.36%)} = 10,531.4 \times 0.0236 = \mathbf{248.5\text{ g}}$$</p>
              <p>$$\text{Yeast Needed (0.81%)} = 10,531.4 \times 0.0081 = \mathbf{85.3\text{ g}}$$</p>

              <p>
                <strong>Baker's Verification:</strong> Total mixed mass equals \(10,531.4 + 6,634.8 + 248.5 + 85.3 = \mathbf{17,500.0\text{ grams}}\). Measuring with a commercial digital scale ensures that every single baguette has identical hydration, crumb structure, and crust blister development.
              </p>
            </div>
          </section>

          <section class="faq-section">
            <h2>Frequently Asked Questions Regarding Cooking Measurements</h2>
            <div class="faq-item">
              <h3>What is the difference between a fluid ounce and a dry ounce?</h3>
              <p>A <strong>Fluid Ounce (fl oz)</strong> is a measure of volumetric space, equal to approximately 29.57 milliliters in the US. A <strong>Dry Ounce (oz)</strong> is a measure of physical mass or weight, equal to 28.3495 grams (1/16th of an avoirdupois pound). They are identical only for water at room temperature (1 fl oz of water weighs approximately 1.04 dry ounces). For a light ingredient like cornstarch or flour, 1 fluid ounce of volume weighs only about 0.5 to 0.6 dry ounces.</p>
            </div>
            <div class="faq-item">
              <h3>How can I substitute active dry yeast for instant yeast?</h3>
              <p>Instant (rapid-rise) yeast has smaller granules and a higher percentage of live yeast cells than active dry yeast. To substitute active dry yeast for instant yeast, multiply the required instant yeast amount by 1.25 (e.g., 4 grams instant yeast = 5 grams active dry yeast) and proof it in warm water (105°F to 115°F) for 5 to 10 minutes before adding to dry flour.</p>
            </div>
            <div class="faq-item">
              <h3>Why does salt measurement vary so widely between Table Salt and Kosher Salt?</h3>
              <p>Fine table salt has tiny, compact cubic crystals with a high bulk density (~1.20 g/mL or ~6 grams per teaspoon). Morton Kosher salt has coarse, dense flakes (~0.85 g/mL or ~4.8 grams per teaspoon). Diamond Crystal Kosher salt has hollow pyramid-shaped flakes with an extremely low bulk density (~0.50 g/mL or ~2.8 grams per teaspoon). A recipe calling for "1 tablespoon salt" measured with table salt adds more than twice as much sodium as one measured with Diamond Crystal Kosher salt.</p>
            </div>
            <div class="faq-item">
              <h3>How many tablespoons are in a cup, pint, and quart?</h3>
              <p>The standard kitchen hierarchy is: 1 US Cup = 16 Tablespoons = 48 Teaspoons; 1 US Pint = 2 Cups = 32 Tablespoons; 1 US Quart = 2 Pints = 4 Cups = 64 Tablespoons; 1 US Gallon = 4 Quarts = 16 Cups = 256 Tablespoons.</p>
            </div>
          </section>
        </article>
      </div>

      <aside class="converter-sidebar">
        <div class="sidebar-card">
          <h3>Related Everyday &amp; Mass Tools</h3>
          <ul class="sidebar-links">
            <li><a href="volume-converter.html">Volume Converter (liters, gallons, cups)</a></li>
            <li><a href="weight-converter.html">Weight Converter (grams, ounces, lbs)</a></li>
            <li><a href="density-converter.html">Density Converter (g/cm³, lb/gal)</a></li>
            <li><a href="temperature-converter.html">Temperature Converter (°C, °F)</a></li>
            <li><a href="energy-converter.html">Energy Converter (calories, Joules)</a></li>
            <li><a href="length-converter.html">Length Converter (inches, cm)</a></li>
            <li><a href="area-converter.html">Area Converter (sq inches, sq cm)</a></li>
            <li><a href="pressure-converter.html">Pressure Converter (bar, psi)</a></li>
          </ul>
        </div>
        <div class="sidebar-card">
          <h3>The Golden Baker's Rule</h3>
          <p class="sidebar-tip">
            Always weigh dry ingredients for consistent pastry results:
            <br><br>
            &bull; <strong>1 Cup Flour</strong> &approx; <strong>120 grams</strong><br>
            &bull; <strong>1 Cup Sugar</strong> &approx; <strong>200 grams</strong><br>
            &bull; <strong>1 Stick Butter</strong> &approx; <strong>113.4 grams</strong><br>
            &bull; <strong>1 Cup Water</strong> &approx; <strong>240 grams</strong>
          </p>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-col">
        <div class="footer-brand">
          <span class="logo-badge">∑</span>
          <span>Calc<span class="accent">Hub</span></span>
        </div>
        <p class="footer-summary">Authoritative engineering, financial, athletic, and physical calculation tools adhering to international ISO, BIPM, NIST, and IEEE computational standards.</p>
      </div>
      <div class="footer-col">
        <h4 class="footer-heading">Hub Categories</h4>
        <ul class="footer-links">
          <li><a href="converter.html">Universal Converters</a></li>
          <li><a href="engineering.html">Electrical &amp; Electronics</a></li>
          <li><a href="mechanical.html">Mechanical &amp; HVAC</a></li>
          <li><a href="health.html">Health &amp; Medical</a></li>
          <li><a href="finance.html">Finance &amp; Taxes</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4 class="footer-heading">Standard Guidelines</h4>
        <ul class="footer-links">
          <li><a href="converter.html">NIST SP 811 Standards</a></li>
          <li><a href="converter.html">BIPM SI Brochure 9th Ed</a></li>
          <li><a href="converter.html">IEEE Floating Point Specs</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="footer-bottom-inner">
        <p>&copy; 2026 CalcHub. All rights reserved. Peer-reviewed computational algorithms.</p>
      </div>
    </div>
  </footer>

  <script>
    (function() {
      // Density table in g/mL
      var INGREDIENT_DENSITIES = {
        water: 1.0,
        flour_ap: 0.50,
        flour_packed: 0.604,
        sugar_white: 0.833,
        sugar_brown: 0.917,
        sugar_powdered: 0.50,
        butter: 0.945,
        honey: 1.417,
        oil_veg: 0.917,
        oats_rolled: 0.375,
        cocoa: 0.417
      };

      // Base volume: mL
      var VOL_FACTORS = {
        cup_us: 240.0,
        tbsp_us: 14.78676,
        tsp_us: 4.92892,
        fl_oz_us: 29.57353,
        ml: 1.0,
        liter: 1000.0,
        cup_metric: 250.0,
        pint_us: 473.176,
        stick_butter: 120.0
      };

      // Base weight: grams
      var WT_FACTORS = {
        grams: 1.0,
        kg: 1000.0,
        oz_wt: 28.34952,
        lb_wt: 453.59237
      };

      var isVol = {
        cup_us: true, tbsp_us: true, tsp_us: true, fl_oz_us: true,
        ml: true, liter: true, cup_metric: true, pint_us: true, stick_butter: true
      };

      var unitLabels = {
        cup_us: 'US Cups',
        tbsp_us: 'US Tbsp',
        tsp_us: 'US Tsp',
        fl_oz_us: 'fl oz',
        ml: 'mL',
        liter: 'L',
        cup_metric: 'Metric Cups',
        pint_us: 'US Pints',
        stick_butter: 'sticks',
        grams: 'g',
        kg: 'kg',
        oz_wt: 'oz wt',
        lb_wt: 'lbs'
      };

      var ingSelect = document.getElementById('cookIngredient');
      var fromInput = document.getElementById('cookFromVal');
      var fromSelect = document.getElementById('cookFromUnit');
      var toInput = document.getElementById('cookToVal');
      var toSelect = document.getElementById('cookToUnit');
      var swapBtn = document.getElementById('cookSwapBtn');

      var equationEl = document.getElementById('cookEquation');
      var mlValEl = document.getElementById('cookMlVal');
      var ozValEl = document.getElementById('cookOzVal');
      var spoonsValEl = document.getElementById('cookSpoonsVal');

      function calculate() {
        var val = parseFloat(fromInput.value);
        if (isNaN(val)) {
          toInput.value = '';
          return;
        }

        var ingKey = ingSelect.value;
        var density = INGREDIENT_DENSITIES[ingKey] || 1.0;

        var fromU = fromSelect.value;
        var toU = toSelect.value;

        // Convert input to internal baseline: volume in mL AND weight in grams
        var baseMl = 0;
        var baseGrams = 0;

        if (isVol[fromU]) {
          baseMl = val * VOL_FACTORS[fromU];
          baseGrams = baseMl * density;
        } else {
          baseGrams = val * WT_FACTORS[fromU];
          baseMl = (density > 0) ? (baseGrams / density) : 0;
        }

        // Convert baseline to target unit
        var result = 0;
        if (isVol[toU]) {
          result = baseMl / VOL_FACTORS[toU];
        } else {
          result = baseGrams / WT_FACTORS[toU];
        }

        if (Math.abs(result) >= 1e6 || (Math.abs(result) < 1e-3 && result !== 0)) {
          toInput.value = result.toExponential(4);
        } else {
          toInput.value = (Math.round(result * 100) / 100).toString();
        }

        if (equationEl) {
          equationEl.textContent = val + " " + unitLabels[fromU] + " = " + toInput.value + " " + unitLabels[toU];
        }

        if (mlValEl) {
          mlValEl.textContent = baseMl.toFixed(1) + " mL";
        }

        if (ozValEl) {
          var oz = baseGrams / 28.34952;
          ozValEl.textContent = oz.toFixed(2) + " oz wt (" + baseGrams.toFixed(1) + " g)";
        }

        if (spoonsValEl) {
          var tbsp = baseMl / 14.78676;
          var tsp = baseMl / 4.92892;
          spoonsValEl.textContent = tbsp.toFixed(1) + " Tbsp | " + tsp.toFixed(1) + " Tsp";
        }
      }

      fromInput.addEventListener('input', calculate);
      fromSelect.addEventListener('change', calculate);
      toSelect.addEventListener('change', calculate);
      ingSelect.addEventListener('change', calculate);

      swapBtn.addEventListener('click', function() {
        var temp = fromSelect.value;
        fromSelect.value = toSelect.value;
        toSelect.value = temp;
        calculate();
      });

      var presets = document.querySelectorAll('.preset-chip');
      presets.forEach(function(chip) {
        chip.addEventListener('click', function() {
          if (this.dataset.ing) ingSelect.value = this.dataset.ing;
          fromInput.value = this.dataset.val;
          fromSelect.value = this.dataset.from;
          toSelect.value = this.dataset.to;
          calculate();
        });
      });

      calculate();
    })();
  </script>
</body>
</html>
"""

# -------------------------------------------------------------
# 6. NUMBER BASE CONVERTER
# -------------------------------------------------------------
num_base_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Number Base Converter — Binary, Decimal, Hex, Octal | CalcHub</title>
  <meta name="description" content="Convert numbers across Binary (base 2), Octal (base 8), Decimal (base 10), and Hexadecimal (base 16) with Two's Complement signed representation and bitwise analysis.">
  <meta name="keywords" content="number base converter, binary to hex, hex to decimal, binary to decimal, octal to binary, radix converter, two's complement calculator, bitwise base converter, ieee 754 binary">
  <meta name="author" content="CalcHub Computer Science & Digital Logic Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/number-base-converter.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="Number Base Converter — Binary, Decimal, Hex, Octal | CalcHub">
  <meta property="og:description" content="Convert numbers across Binary (base 2), Octal (base 8), Decimal (base 10), and Hexadecimal (base 16) with Two's Complement signed representation and bitwise analysis.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/number-base-converter.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/number-base-converter.html#app",
      "name": "Precision Radix & Number Base Converter",
      "url": "https://calchub.org/number-base-converter.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Digital computer systems radix converter supporting Binary, Octal, Decimal, Hexadecimal, and arbitrary bases up to Base 36 with Two's complement integer support."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Universal Unit Converters", "item": "https://calchub.org/converter.html"},
        {"@type": "ListItem", "position": 3, "name": "Number Base Converter", "item": "https://calchub.org/number-base-converter.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Why do digital computers utilize Binary (Base 2) and Hexadecimal (Base 16)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Physical digital semiconductors represent data using two discrete voltage states: high voltage (logic 1) and low/ground voltage (logic 0). This makes base-2 binary the natural hardware representation. Hexadecimal (base 16) is utilized by programmers as a human-readable shorthand for binary, because exactly 4 binary bits (one nibble) map directly into one single hexadecimal digit (e.g., 1111_2 = F_16, and 11111111_2 = FF_16 = 255_10)."
          }
        },
        {
          "@type": "Question",
          "name": "How does Two's Complement represent negative numbers in binary?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Two's complement is the universal binary encoding for signed integers. To negate a binary number, invert all bits (logical NOT, one's complement) and add 1 to the least significant bit: -X = (~X) + 1. For an 8-bit integer, +5 is 00000101. Inverting yields 11111010; adding 1 yields 11111011 (-5 in decimal). Two's complement eliminates the problem of dual positive and negative zeros (+0 and -0) and allows standard addition hardware to perform subtraction directly."
          }
        },
        {
          "@type": "Question",
          "name": "What is the positional expansion formula for converting any base to decimal?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In any positional numeral system with radix b, the decimal value N equals the sum of each digit d_i multiplied by base b raised to its positional power i: N = Σ [d_i × b^i]. For example, the hexadecimal number 2AF_16 in decimal is: (2 × 16²) + (10 × 16¹) + (15 × 16⁰) = (2 × 256) + (10 × 16) + (15 × 1) = 512 + 160 + 15 = 687_10."
          }
        },
        {
          "@type": "Question",
          "name": "Why was Octal (Base 8) widely used in early computing systems?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Early mainframe computers (such as the DEC PDP-8, PDP-11, and IBM 7090) used word architectures based on multiples of 3 bits, such as 12-bit, 18-bit, or 36-bit words. Because 2³ = 8, one octal digit maps cleanly into exactly 3 binary bits. Octal is still preserved in modern Unix/Linux file permissions (e.g., chmod 755 represents rwxr-xr-x)."
          }
        }
      ]
    }
  ]
}
  </script>
</head>
<body class="converter-page">
  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="logo">
        <span class="logo-badge">∑</span>
        <span>Calc<span class="accent">Hub</span></span>
      </a>
      <nav class="header-nav" aria-label="Main Navigation">
        <div class="nav-row">
          <a href="index.html" class="nav-link">🏠 Home</a>
          <a href="health.html" class="nav-link">⚖️ Health</a>
          <a href="finance.html" class="nav-link">🏦 Finance</a>
          <a href="math.html" class="nav-link">🔢 Math</a>
          <a href="engineering.html" class="nav-link">⚡ Electrical</a>
          <a href="solar-energy.html" class="nav-link">☀️ Solar</a>
          <a href="mechanical.html" class="nav-link">⚙️ Mechanical</a>
        </div>
        <div class="nav-row">
          <a href="civil.html" class="nav-link">🏗️ Civil</a>
          <a href="chemical.html" class="nav-link">🧪 Chemical</a>
          <a href="fire-safety.html" class="nav-link">🚨 Fire &amp; Safety</a>
          <a href="programmer.html" class="nav-link">👨‍💻 Programmer</a>
          <a href="datetime.html" class="nav-link">📅 Date &amp; Time</a>
          <a href="converter.html" class="nav-link active">🔄 Converter</a>
        </div>
      </nav>
    </div>
  </header>

  <main class="page-wrapper">
    <div class="converter-layout">
      <div class="converter-main">
        <div class="calculator-header">
          <div class="breadcrumbs">
            <a href="index.html">Home</a> &rsaquo;
            <a href="converter.html">Unit Converters</a> &rsaquo;
            <span>Number Base Converter</span>
          </div>
          <span class="badge">Computer Architecture &amp; Discrete Math</span>
          <h1>Precision Number Base Converter</h1>
          <p class="tagline">Convert across Binary (base 2), Octal (base 8), Decimal (base 10), and Hexadecimal (base 16) with Two's complement integer analysis.</p>
        </div>

        <div class="calculator-container card-surface">
          <div class="converter-box">
            <div class="converter-inputs-grid">
              <div class="input-col">
                <label for="baseFromVal" class="input-label">From Value</label>
                <input type="text" id="baseFromVal" class="converter-num-input" value="255" placeholder="Enter number" style="text-transform:uppercase;">
                <label for="baseFromUnit" class="input-label sub-label">From Radix Base</label>
                <select id="baseFromUnit" class="converter-select">
                  <option value="10" selected>Decimal (Base 10)</option>
                  <option value="2">Binary (Base 2)</option>
                  <option value="16">Hexadecimal (Base 16)</option>
                  <option value="8">Octal (Base 8)</option>
                  <option value="36">Base 36 (0-9, A-Z)</option>
                </select>
              </div>

              <div class="swap-col">
                <button type="button" id="baseSwapBtn" class="swap-button" title="Swap input and output units" aria-label="Swap units">
                  &#8644;
                </button>
              </div>

              <div class="input-col">
                <label for="baseToVal" class="input-label">Converted Value</label>
                <input type="text" id="baseToVal" class="converter-num-input output-val" readonly value="FF" style="text-transform:uppercase;">
                <label for="baseToUnit" class="input-label sub-label">To Radix Base</label>
                <select id="baseToUnit" class="converter-select">
                  <option value="10">Decimal (Base 10)</option>
                  <option value="2">Binary (Base 2)</option>
                  <option value="16" selected>Hexadecimal (Base 16)</option>
                  <option value="8">Octal (Base 8)</option>
                  <option value="36">Base 36 (0-9, A-Z)</option>
                </select>
              </div>
            </div>

            <div class="converter-quick-presets">
              <span class="preset-label">Standard Computer Science Radix Benchmarks:</span>
              <button type="button" class="preset-chip" data-val="255" data-from="10" data-to="16">255 Decimal = 0xFF</button>
              <button type="button" class="preset-chip" data-val="11111111" data-from="2" data-to="10">8-Bit 11111111 = 255</button>
              <button type="button" class="preset-chip" data-val="755" data-from="8" data-to="2">Unix chmod 755 (Octal)</button>
              <button type="button" class="preset-chip" data-val="65535" data-from="10" data-to="16">16-Bit Max (0xFFFF)</button>
            </div>

            <div class="conversion-summary-panel" id="baseSummaryCard">
              <div class="summary-line">
                <span class="summary-label">Radix Relation:</span>
                <span class="summary-formula" id="baseEquation">255 (Base 10) = FF (Base 16)</span>
              </div>
              <div class="summary-submetrics">
                <div class="submetric-item">
                  <span class="submetric-name">Full 8-Bit Binary:</span>
                  <span class="submetric-val" id="baseBin8">1111 1111</span>
                </div>
                <div class="submetric-item">
                  <span class="submetric-name">Octal (Base 8):</span>
                  <span class="submetric-val" id="baseOctVal">377</span>
                </div>
                <div class="submetric-item">
                  <span class="submetric-name">Signed 8-Bit Two's Comp:</span>
                  <span class="submetric-val" id="baseSigned8">-1 (if 8-bit signed)</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <section>
            <h2>Theoretical Foundations of Positional Numeral Systems &amp; Radix</h2>
            <p>
              In discrete mathematics and computer engineering, a <strong>positional numeral system</strong> represents any real integer using an ordered sequence of numeric glyphs whose values depend upon their position relative to the radix point. The fundamental parameter defining any positional system is its <strong>base (or radix, \(b\))</strong>, an integer greater than 1 indicating the count of unique symbol digits available:
            </p>
            <p>
              $$N = \sum_{i=0}^{n-1} d_i \cdot b^i = d_{n-1} b^{n-1} + d_{n-2} b^{n-2} + \dots + d_1 b^1 + d_0 b^0$$
            </p>
            <p>
              Where \(d_i \in \{0, 1, \dots, b-1\}\) represents the digit at position \(i\).
            </p>
            <p>
              Four primary bases form the operational architecture of digital electronics and software engineering:
            </p>
            <ol>
              <li><strong>Decimal (Base 10):</strong> The human standard numbering system utilizing digits \(\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}\), likely derived from counting on ten human fingers.</li>
              <li><strong>Binary (Base 2):</strong> The fundamental machine language of all silicon microprocessors, using only two states \(\{0, 1\}\) representing physical transistor conduction (cutoff vs saturation) or memory capacitor charge.</li>
              <li><strong>Hexadecimal (Base 16):</strong> A compact human-readable representation using digits \(\{0\text{--}9\}\) and letters \(\{\text{A}, \text{B}, \text{C}, \text{D}, \text{E}, \text{F}\}\) (representing 10 through 15). Because \(16 = 2^4\), every single hexadecimal character corresponds exactly to a 4-bit binary nibble.</li>
              <li><strong>Octal (Base 8):</strong> Using digits \(\{0, 1, 2, 3, 4, 5, 6, 7\}\). Because \(8 = 2^3\), each octal digit corresponds exactly to 3 binary bits, universally preserved in Linux file permission modes (e.g., <code>chmod 777</code>).</li>
            </ol>
          </section>

          <section>
            <h2>Exact Mathematical Conversion Algorithms</h2>
            <p>
              Transforming numbers between arbitrary bases requires two systematic analytical algorithms: positional expansion to evaluate arbitrary bases into decimal, and successive integer division with remainder extraction to convert decimal into any destination radix.
            </p>

            <div class="formula-card">
              <h3>Core Radix Algorithms</h3>
              <p><strong>1. Arbitrary Base to Decimal (Base 10 Evaluation):</strong></p>
              <p>$$N_{10} = d_{k-1} b^{k-1} + d_{k-2} b^{k-2} + \dots + d_1 b^1 + d_0 b^0$$</p>
              <p>$$\text{Example: } \text{3E8}_{16} = (3 \times 16^2) + (14 \times 16^1) + (8 \times 16^0) = 768 + 224 + 8 = 1,000_{10}$$</p>

              <p><strong>2. Decimal to Destination Base (Successive Division Algorithm):</strong></p>
              <p>Divide the decimal integer repeatedly by target base \(b\); the remainders read in reverse chronological order formulate the destination representation.</p>
              <p>$$\text{Example converting } 29_{10} \text{ to binary:}$$</p>
              <p>$$29 \div 2 = 14 \text{ R } 1 \quad (\text{LSB})$$</p>
              <p>$$14 \div 2 = 7 \text{ R } 0$$</p>
              <p>$$7 \div 2 = 3 \text{ R } 1$$</p>
              <p>$$3 \div 2 = 1 \text{ R } 1$$</p>
              <p>$$1 \div 2 = 0 \text{ R } 1 \quad (\text{MSB}) \implies \mathbf{11101_2}$$</p>
            </div>
          </section>

          <section>
            <h2>Hexadecimal-Binary Grouping &amp; Two's Complement Encoding</h2>
            <p>
              A major advantage of power-of-two number bases is that conversion between binary, octal, and hexadecimal does not require arithmetic division; it is performed by simple bit-grouping inspection:
            </p>
            <ul>
              <li><strong>Binary to Hexadecimal:</strong> Group binary bits into clusters of 4 starting from the right (least significant bit):
                $$\text{Binary: } \underbrace{1101}_{\text{D}} \quad \underbrace{1011}_{\text{B}} \quad \underbrace{0000}_{0} \quad \underbrace{1111}_{\text{F}} \implies \mathbf{\text{0xDB0F}}$$
              </li>
              <li><strong>Binary to Octal:</strong> Group bits into clusters of 3 starting from the right:
                $$\text{Binary: } \underbrace{001}_{1} \quad \underbrace{101}_{5} \quad \underbrace{011}_{3} \implies \mathbf{153_8}$$
              </li>
            </ul>
            <p>
              For signed integer representation, digital microprocessors utilize <strong>Two's Complement Arithmetic</strong>. In an \(n\)-bit two's complement system:
            </p>
            <p>
              $$\text{Range: } -2^{n-1} \le X \le 2^{n-1} - 1$$
            </p>
            <p>
              For standard 8-bit bytes, the range spans \(-128\) to \(+127\). The most significant bit (MSB) acts as the sign flag: if the MSB is 0, the number is positive; if the MSB is 1, the number is negative. To compute the magnitude of a negative number:
            </p>
            <p>
              $$-X = \sim X + 1$$
            </p>
            <p>
              For example, \(11111111_2\) represents \(255\) in an unsigned 8-bit integer, but in signed two's complement it represents \(-1\).
            </p>
          </section>

          <section>
            <h2>Comprehensive 4-Bit Radix Truth Table (0 to 15)</h2>
            <p>
              The reference table below illustrates the exact equivalence across decimal, 4-bit binary, octal, hexadecimal, and standard ASCII control values:
            </p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>Decimal (Base 10)</th>
                  <th>Binary (Base 2)</th>
                  <th>Octal (Base 8)</th>
                  <th>Hexadecimal (Base 16)</th>
                  <th>Signed 4-Bit Two's Comp</th>
                  <th>Bitwise Meaning / Logic</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>0</strong></td>
                  <td>0000</td>
                  <td>00</td>
                  <td>0x0</td>
                  <td>0</td>
                  <td>All bits cleared (NULL / Zero)</td>
                </tr>
                <tr>
                  <td><strong>1</strong></td>
                  <td>0001</td>
                  <td>01</td>
                  <td>0x1</td>
                  <td>+1</td>
                  <td>Least Significant Bit (LSB) set</td>
                </tr>
                <tr>
                  <td><strong>2</strong></td>
                  <td>0010</td>
                  <td>02</td>
                  <td>0x2</td>
                  <td>+2</td>
                  <td>Bit 1 set (2¹)</td>
                </tr>
                <tr>
                  <td><strong>3</strong></td>
                  <td>0011</td>
                  <td>03</td>
                  <td>0x3</td>
                  <td>+3</td>
                  <td>Bits 0 and 1 set</td>
                </tr>
                <tr>
                  <td><strong>4</strong></td>
                  <td>0100</td>
                  <td>04</td>
                  <td>0x4</td>
                  <td>+4</td>
                  <td>Bit 2 set (2²)</td>
                </tr>
                <tr>
                  <td><strong>5</strong></td>
                  <td>0101</td>
                  <td>05</td>
                  <td>0x5</td>
                  <td>+5</td>
                  <td>Bits 0 and 2 set</td>
                </tr>
                <tr>
                  <td><strong>6</strong></td>
                  <td>0110</td>
                  <td>06</td>
                  <td>0x6</td>
                  <td>+6</td>
                  <td>Bits 1 and 2 set</td>
                </tr>
                <tr>
                  <td><strong>7</strong></td>
                  <td>0111</td>
                  <td>07</td>
                  <td>0x7</td>
                  <td>+7 (Max signed 4-bit)</td>
                  <td>Lower 3 bits set</td>
                </tr>
                <tr>
                  <td><strong>8</strong></td>
                  <td>1000</td>
                  <td>10</td>
                  <td>0x8</td>
                  <td>-8 (Min signed 4-bit)</td>
                  <td>Bit 3 set (Sign bit in 4-bit)</td>
                </tr>
                <tr>
                  <td><strong>9</strong></td>
                  <td>1001</td>
                  <td>11</td>
                  <td>0x9</td>
                  <td>-7</td>
                  <td>Decimal 9 representation</td>
                </tr>
                <tr>
                  <td><strong>10</strong></td>
                  <td>1010</td>
                  <td>12</td>
                  <td>0xA</td>
                  <td>-6</td>
                  <td>Alternating bit pattern (Nibble)</td>
                </tr>
                <tr>
                  <td><strong>11</strong></td>
                  <td>1011</td>
                  <td>13</td>
                  <td>0xB</td>
                  <td>-5</td>
                  <td>Hexadecimal 'B'</td>
                </tr>
                <tr>
                  <td><strong>12</strong></td>
                  <td>1100</td>
                  <td>14</td>
                  <td>0xC</td>
                  <td>-4</td>
                  <td>Upper 2 bits of nibble set</td>
                </tr>
                <tr>
                  <td><strong>13</strong></td>
                  <td>1101</td>
                  <td>15</td>
                  <td>0xD</td>
                  <td>-3</td>
                  <td>Hexadecimal 'D'</td>
                </tr>
                <tr>
                  <td><strong>14</strong></td>
                  <td>1110</td>
                  <td>16</td>
                  <td>0xE</td>
                  <td>-2</td>
                  <td>Hexadecimal 'E'</td>
                </tr>
                <tr>
                  <td><strong>15</strong></td>
                  <td>1111</td>
                  <td>17</td>
                  <td>0xF</td>
                  <td>-1</td>
                  <td>Full nibble saturation (All 1s)</td>
                </tr>
              </tbody>
            </table>
          </section>

          <section>
            <h2>Worked Computer Science Case Study: Memory Dump Register Decoding</h2>
            <div class="worked-example-card">
              <h3>Systems Engineering Scenario: Debugging a Hexadecimal Machine Crash Dump</h3>
              <p>
                An embedded firmware developer is inspecting an ARM Cortex-M4 microcontroller hard fault dump. The crash log indicates that processor register <code>R0</code> contained the 32-bit hexadecimal word <strong><code>0xFFFFA4C2</code></strong>.
              </p>
              <p>The systems engineer must determine:</p>
              <ol>
                <li>The exact raw binary representation in 32 bits (grouped into nibbles).</li>
                <li>The unsigned 32-bit decimal integer value.</li>
                <li>The signed 32-bit two's complement decimal value.</li>
                <li>The equivalent Octal representation for cross-checking with a Unix core dump log.</li>
              </ol>

              <h4>Step-by-Step Calculation:</h4>
              <p><strong>1. Hexadecimal to Binary Translation (Direct Nibble Substitution):</strong></p>
              <p>F = 1111 | F = 1111 | F = 1111 | F = 1111 | A = 1010 | 4 = 0100 | C = 1100 | 2 = 0010</p>
              <p>$$\mathbf{\text{Binary: } 1111\ 1111\ 1111\ 1111\ 1010\ 0100\ 1100\ 0010_2}$$</p>

              <p><strong>2. Unsigned 32-Bit Decimal Value:</strong></p>
              <p>$$N_{\text{unsigned}} = (\text{0xFFFFA4C2})_{16} = 4,294,943,938_{10}$$</p>

              <p><strong>3. Signed 32-Bit Two's Complement Value:</strong></p>
              <p>Because the MSB is 1 (the first hex digit is F = 1111), the number is negative.</p>
              <p>$$\text{Invert bits: } \sim(1111\ 1111\ 1111\ 1111\ 1010\ 0100\ 1100\ 0010) = 0000\ 0000\ 0000\ 0000\ 0101\ 1011\ 0011\ 1101$$</p>
              <p>In hexadecimal, \(\sim \text{0xFFFFA4C2} = \text{0x00005B3D}\).</p>
              <p>$$\text{Add 1: } \text{0x00005B3D} + 1 = \text{0x00005B3E}$$</p>
              <p>Evaluate magnitude in decimal:</p>
              <p>$$(5 \times 16^3) + (11 \times 16^2) + (3 \times 16^1) + (14 \times 16^0) = (5 \times 4096) + (11 \times 256) + 48 + 14 = 20,480 + 2,816 + 62 = 23,358$$</p>
              <p>$$\mathbf{\text{Signed Decimal Value: } -23,358_{10}}$$</p>

              <p><strong>4. Convert to Octal (Group by 3 bits from right):</strong></p>
              <p>$$\text{Bits: } 011\ 111\ 111\ 111\ 111\ 111\ 101\ 001\ 001\ 100\ 001\ 0$$</p>
              <p>$$\mathbf{\text{Octal: } 37777722302_8}$$</p>

              <p>
                <strong>Debug Conclusion:</strong> Register R0 was holding a signed temperature sensor offset of <strong>-23,358</strong> counts, which underflowed an unsigned buffer pointer and caused the processor hard fault exception.
              </p>
            </div>
          </section>

          <section class="faq-section">
            <h2>Frequently Asked Questions Regarding Number Bases</h2>
            <div class="faq-item">
              <h3>What are Endianness and Byte Order (Big-Endian vs. Little-Endian)?</h3>
              <p>Endianness defines the sequential memory address order in which multi-byte words are stored in RAM. In <strong>Big-Endian</strong> architectures (network TCP/IP protocol, Motorola 68k), the most significant byte (MSB) is stored at the lowest memory address. In <strong>Little-Endian</strong> architectures (x86, x86-64, modern ARM), the least significant byte (LSB) is stored first at the lowest address. For example, 32-bit hex word <code>0x12345678</code> is stored in Little-Endian memory as <code>78 56 34 12</code>.</p>
            </div>
            <div class="faq-item">
              <h3>What is Base 64 encoding and why is it used in web development?</h3>
              <p>Base 64 uses 64 printable ASCII characters (A-Z, a-z, 0-9, +, /) to represent arbitrary binary data. Because early email systems (SMTP) and HTTP transmission channels were designed strictly for 7-bit ASCII text, sending raw binary files (images, PDF attachments, cryptographic keys) caused corrupted byte transmission. Base 64 splits binary bytes into 6-bit chunks (\(2^6 = 64\)) and maps each to safe printable ASCII characters, expanding file size by approximately 33%.</p>
            </div>
            <div class="faq-item">
              <h3>How does floating-point decimal conversion work in IEEE 754?</h3>
              <p>Computers store decimal fractions (such as 0.1) using the IEEE 754 floating-point standard: \(V = (-1)^s \times (1 + \text{mantissa}) \times 2^{\text{exponent} - \text{bias}}\). Because fractions like \(0.1_{10}\) result in an infinitely repeating binary fraction (\(0.0001100110011\dots_2\)), binary computers cannot store 0.1 exactly, leading to small roundoff anomalies like <code>0.1 + 0.2 === 0.30000000000000004</code> in languages like JavaScript and Python.</p>
            </div>
            <div class="faq-item">
              <h3>Can a number base be higher than 36?</h3>
              <p>Yes. Base 36 uses the ten numeric digits (0-9) and twenty-six Latin letters (A-Z). Systems with higher bases, like Base 58 (used in Bitcoin addresses to eliminate easily confused characters like 0, O, I, and l) and Base 64, use custom symbol tables that include both uppercase and lowercase distinctions and punctuation symbols.</p>
            </div>
          </section>
        </article>
      </div>

      <aside class="converter-sidebar">
        <div class="sidebar-card">
          <h3>Related Digital &amp; CS Tools</h3>
          <ul class="sidebar-links">
            <li><a href="data-storage-converter.html">Data Storage Converter (GB, TB, GiB)</a></li>
            <li><a href="data-transfer-rate-converter.html">Data Transfer Rate Converter (Mbps, Gbps)</a></li>
            <li><a href="subnet-calculator.html">Subnet Calculator (CIDR, IP Masks)</a></li>
            <li><a href="frequency-converter.html">Frequency Converter (Hz, MHz, GHz)</a></li>
            <li><a href="time-converter.html">Time Converter (ms, μs, ns)</a></li>
            <li><a href="power-converter.html">Power Converter (Watts, kW)</a></li>
            <li><a href="angle-converter.html">Angle Converter (Degrees, Radians)</a></li>
            <li><a href="energy-converter.html">Energy Converter (Joules, kWh)</a></li>
          </ul>
        </div>
        <div class="sidebar-card">
          <h3>Hexadecimal Quick Cheat Sheet</h3>
          <p class="sidebar-tip">
            Remember the core binary nibble values:
            <br><br>
            &bull; <code>0xA</code> = 10 (1010)<br>
            &bull; <code>0xB</code> = 11 (1011)<br>
            &bull; <code>0xC</code> = 12 (1100)<br>
            &bull; <code>0xD</code> = 13 (1101)<br>
            &bull; <code>0xE</code> = 14 (1110)<br>
            &bull; <code>0xF</code> = 15 (1111)
          </p>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-col">
        <div class="footer-brand">
          <span class="logo-badge">∑</span>
          <span>Calc<span class="accent">Hub</span></span>
        </div>
        <p class="footer-summary">Authoritative engineering, financial, athletic, and physical calculation tools adhering to international ISO, BIPM, NIST, and IEEE computational standards.</p>
      </div>
      <div class="footer-col">
        <h4 class="footer-heading">Hub Categories</h4>
        <ul class="footer-links">
          <li><a href="converter.html">Universal Converters</a></li>
          <li><a href="engineering.html">Electrical &amp; Electronics</a></li>
          <li><a href="mechanical.html">Mechanical &amp; HVAC</a></li>
          <li><a href="health.html">Health &amp; Medical</a></li>
          <li><a href="finance.html">Finance &amp; Taxes</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4 class="footer-heading">Standard Guidelines</h4>
        <ul class="footer-links">
          <li><a href="converter.html">NIST SP 811 Standards</a></li>
          <li><a href="converter.html">BIPM SI Brochure 9th Ed</a></li>
          <li><a href="converter.html">IEEE Floating Point Specs</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="footer-bottom-inner">
        <p>&copy; 2026 CalcHub. All rights reserved. Peer-reviewed computational algorithms.</p>
      </div>
    </div>
  </footer>

  <script>
    (function() {
      var fromInput = document.getElementById('baseFromVal');
      var fromSelect = document.getElementById('baseFromUnit');
      var toInput = document.getElementById('baseToVal');
      var toSelect = document.getElementById('baseToUnit');
      var swapBtn = document.getElementById('baseSwapBtn');

      var equationEl = document.getElementById('baseEquation');
      var bin8El = document.getElementById('baseBin8');
      var octValEl = document.getElementById('baseOctVal');
      var signed8El = document.getElementById('baseSigned8');

      function calculate() {
        var str = fromInput.value.trim();
        if (!str) {
          toInput.value = '';
          return;
        }

        var fromBase = parseInt(fromSelect.value, 10);
        var toBase = parseInt(toSelect.value, 10);

        try {
          // Parse string into BigInt or integer
          var decVal;
          if (str.startsWith('-')) {
            decVal = -parseInt(str.substring(1), fromBase);
          } else {
            decVal = parseInt(str, fromBase);
          }

          if (isNaN(decVal)) {
            toInput.value = 'Invalid Input';
            return;
          }

          // Convert to target base
          var resStr;
          if (decVal < 0) {
            resStr = '-' + Math.abs(decVal).toString(toBase).toUpperCase();
          } else {
            resStr = decVal.toString(toBase).toUpperCase();
          }

          toInput.value = resStr;

          if (equationEl) {
            equationEl.textContent = str.toUpperCase() + " (Base " + fromBase + ") = " + resStr + " (Base " + toBase + ")";
          }

          // Binary representation formatted in nibbles
          if (bin8El) {
            var unsignedDec = decVal >>> 0; // 32-bit unsigned
            var binStr = unsignedDec.toString(2);
            // Pad to multiple of 4
            while (binStr.length % 4 !== 0) {
              binStr = '0' + binStr;
            }
            // Insert spaces every 4 bits
            var chunks = [];
            for (var i = 0; i < binStr.length; i += 4) {
              chunks.push(binStr.substr(i, 4));
            }
            bin8El.textContent = chunks.join(' ');
          }

          if (octValEl) {
            octValEl.textContent = (decVal >>> 0).toString(8);
          }

          if (signed8El) {
            // Check 8-bit two's complement interpretation of lower 8 bits
            var byteVal = decVal & 0xFF;
            var signedVal = (byteVal & 0x80) ? (byteVal - 0x100) : byteVal;
            signed8El.textContent = signedVal.toString() + " (signed 8-bit)";
          }
        } catch(e) {
          toInput.value = 'Error';
        }
      }

      fromInput.addEventListener('input', calculate);
      fromSelect.addEventListener('change', calculate);
      toSelect.addEventListener('change', calculate);

      swapBtn.addEventListener('click', function() {
        var temp = fromSelect.value;
        fromSelect.value = toSelect.value;
        toSelect.value = temp;
        calculate();
      });

      var presets = document.querySelectorAll('.preset-chip');
      presets.forEach(function(chip) {
        chip.addEventListener('click', function() {
          fromInput.value = this.dataset.val;
          fromSelect.value = this.dataset.from;
          toSelect.value = this.dataset.to;
          calculate();
        });
      });

      calculate();
    })();
  </script>
</body>
</html>
"""

# Write files
with open(os.path.join(BASE_DIR, 'cooking-converter.html'), 'w', encoding='utf-8') as f:
    f.write(cooking_html.strip() + '\n')
print("Generated cooking-converter.html successfully!")

with open(os.path.join(BASE_DIR, 'number-base-converter.html'), 'w', encoding='utf-8') as f:
    f.write(num_base_html.strip() + '\n')
print("Generated number-base-converter.html successfully!")
