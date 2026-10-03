import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 7. FUEL ECONOMY CONVERTER
# -------------------------------------------------------------
fuel_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fuel Economy Converter — MPG, L/100km, km/L, gal/100mi | CalcHub</title>
  <meta name="description" content="Convert automotive fuel economy and consumption between US MPG, Imperial (UK) MPG, L/100km, and km/L. Master the MPG illusion, EPA ratings, and WLTP benchmarks.">
  <meta name="keywords" content="fuel economy converter, mpg to l/100km, l/100km to mpg, mpg us to imperial, km/l to mpg, fuel consumption calculator, mpg illusion, wltp to epa conversion, gas mileage converter">
  <meta name="author" content="CalcHub Automotive & Mechanical Powertrain Engineering Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/fuel-economy-converter.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="Fuel Economy Converter — MPG, L/100km, km/L, gal/100mi | CalcHub">
  <meta property="og:description" content="Convert automotive fuel economy and consumption between US MPG, Imperial (UK) MPG, L/100km, and km/L. Master the MPG illusion, EPA ratings, and WLTP benchmarks.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/fuel-economy-converter.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/fuel-economy-converter.html#app",
      "name": "Automotive Fuel Economy & Consumption Converter",
      "url": "https://calchub.org/fuel-economy-converter.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Scientific vehicle fuel economy and consumption conversion engine adhering to EPA, WLTP, and ISO 7860 harmonic conversion mathematics."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Universal Unit Converters", "item": "https://calchub.org/converter.html"},
        {"@type": "ListItem", "position": 3, "name": "Fuel Economy Converter", "item": "https://calchub.org/fuel-economy-converter.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Why is the conversion between Miles per Gallon (MPG) and Liters per 100 Kilometers (L/100km) non-linear?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "MPG measures fuel efficiency as distance traveled per unit volume of fuel (distance / volume), whereas L/100km measures fuel consumption as volume consumed per fixed distance (volume / distance). Because they are mathematically inverse reciprocals, their conversion is harmonic: L/100km = 235.215 / MPG_US. As MPG increases, the marginal reduction in liters consumed diminishes exponentially."
          }
        },
        {
          "@type": "Question",
          "name": "What is the cognitive cognitive bias known as the 'MPG Illusion'?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Discovered by behavioral researchers Larrick and Soll (2008), the MPG Illusion refers to consumers incorrectly assuming that a linear increase in MPG equates to a linear fuel savings. For example, upgrading an SUV from 14 MPG to 18 MPG saves 1.59 gallons every 100 miles, whereas upgrading a fuel-efficient sedan from 35 MPG to 50 MPG saves only 0.86 gallons every 100 miles. Measuring consumption in L/100km or gallons/100mi eliminates this bias."
          }
        },
        {
          "@type": "Question",
          "name": "Why does a vehicle with a 40 MPG rating in the UK not achieve 40 MPG in the United States?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The British Imperial gallon is defined as exactly 4.54609 liters, which is approximately 20.095% larger than the US liquid gallon (3.78541 liters). Therefore, 40 UK MPG equals only 33.31 US MPG. Additionally, the European WLTP testing cycle generally reports higher laboratory numbers than the United States EPA 5-cycle laboratory procedure."
          }
        },
        {
          "@type": "Question",
          "name": "How does the EPA determine MPGe (Miles per Gallon equivalent) for electric vehicles?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The US EPA defines 1 gallon of conventional unleaded gasoline as containing a standardized thermal energy content of 115,000 BTU, which corresponds precisely to 33.705 kilowatt-hours (kWh) of electrical energy. An electric vehicle that consumes 30 kWh per 100 miles achieves an MPGe rating of (33.705 / 30) × 100 ≈ 112.35 MPGe."
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
    <div class="header-container">
      <a href="index.html" class="logo">CalcHub</a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="converter.html" class="active">Converters</a>
        <a href="financial.html">Finance</a>
        <a href="fitness.html">Fitness</a>
        <a href="health.html">Health</a>
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
            <span>Fuel Economy Converter</span>
          </div>
          <span class="badge">Automotive &amp; Powertrain Dynamics</span>
          <h1>Precision Fuel Economy Converter</h1>
          <p class="tagline">Convert between fuel efficiency (US MPG, UK MPG, km/L) and consumption (L/100km, gal/100mi) using rigorous harmonic thermodynamics.</p>
        </div>

        <div class="calculator-container card-surface">
          <div class="converter-box">
            <div class="converter-inputs-grid">
              <div class="input-col">
                <label for="fuelFromVal" class="input-label">From Value</label>
                <input type="number" id="fuelFromVal" class="converter-num-input" value="30" step="any" min="0.1" placeholder="Enter fuel value">
                <label for="fuelFromUnit" class="input-label sub-label">From Unit</label>
                <select id="fuelFromUnit" class="converter-select">
                  <option value="mpg_us" selected>Miles per Gallon (US MPG)</option>
                  <option value="l_100km">Liters / 100 km (L/100km)</option>
                  <option value="mpg_uk">Miles per Gallon (UK MPG)</option>
                  <option value="km_l">Kilometers per Liter (km/L)</option>
                  <option value="gal_100mi">Gallons / 100 Miles (US gal/100mi)</option>
                </select>
              </div>

              <div class="swap-col">
                <button type="button" id="fuelSwapBtn" class="swap-button" title="Swap input and output units" aria-label="Swap units">
                  &#8644;
                </button>
              </div>

              <div class="input-col">
                <label for="fuelToVal" class="input-label">Converted Value</label>
                <input type="text" id="fuelToVal" class="converter-num-input output-val" readonly value="7.84">
                <label for="fuelToUnit" class="input-label sub-label">To Unit</label>
                <select id="fuelToUnit" class="converter-select">
                  <option value="mpg_us">Miles per Gallon (US MPG)</option>
                  <option value="l_100km" selected>Liters / 100 km (L/100km)</option>
                  <option value="mpg_uk">Miles per Gallon (UK MPG)</option>
                  <option value="km_l">Kilometers per Liter (km/L)</option>
                  <option value="gal_100mi">Gallons / 100 Miles (US gal/100mi)</option>
                </select>
              </div>
            </div>

            <div class="converter-quick-presets">
              <span class="preset-label">Standard Automobile Benchmarks:</span>
              <button type="button" class="preset-chip" data-val="15" data-from="mpg_us" data-to="l_100km">15 US MPG (Heavy Truck - 15.7 L/100km)</button>
              <button type="button" class="preset-chip" data-val="30" data-from="mpg_us" data-to="l_100km">30 US MPG (Family Sedan - 7.8 L/100km)</button>
              <button type="button" class="preset-chip" data-val="50" data-from="mpg_us" data-to="l_100km">50 US MPG (Hybrid - 4.7 L/100km)</button>
              <button type="button" class="preset-chip" data-val="6.0" data-from="l_100km" data-to="mpg_us">6.0 L/100km (Euro Diesel - 39.2 US MPG)</button>
            </div>

            <div class="conversion-summary-panel" id="fuelSummaryCard">
              <div class="summary-line">
                <span class="summary-label">Harmonic Relation:</span>
                <span class="summary-formula" id="fuelEquation">30.0 US MPG = 7.84 L/100km</span>
              </div>
              <div class="summary-submetrics">
                <div class="submetric-item">
                  <span class="submetric-name">Fuel for 15,000 km:</span>
                  <span class="submetric-val" id="fuelAnnualLiters">1,176 Liters</span>
                </div>
                <div class="submetric-item">
                  <span class="submetric-name">Fuel for 10,000 miles:</span>
                  <span class="submetric-val" id="fuelAnnualGallons">333.3 US Gallons</span>
                </div>
                <div class="submetric-item">
                  <span class="submetric-name">Est. CO₂ Emitted / Year:</span>
                  <span class="submetric-val" id="fuelCo2Val">2,963 kg CO₂</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <section>
            <h2>Vehicle Efficiency vs. Fuel Consumption: The Physics &amp; Mathematics</h2>
            <p>
              Automotive energy reporting utilizes two diametrically opposed methodologies across global markets. In North America and Great Britain, vehicle capability is characterized by <strong>Fuel Efficiency</strong> (how much distance can be achieved per volume of fuel consumed, such as Miles per Gallon). In continental Europe, Australasia, and most SI-metric territories, vehicle performance is characterized by <strong>Fuel Consumption</strong> (the absolute volume of fuel required to traverse a normalized distance, universally reported as Liters per 100 Kilometers).
            </p>
            <p>
              This philosophical difference creates an essential mathematical reality: efficiency and consumption are <strong>inverse reciprocal quantities</strong>. As a result, calculating conversions between them cannot be performed with a simple constant multiplier; it requires a harmonic inversion:
            </p>
            <p>
              $$\text{Efficiency} \propto \frac{\text{Distance}}{\text{Volume}} \quad \longleftrightarrow \quad \text{Consumption} \propto \frac{\text{Volume}}{\text{Distance}}$$
            </p>
          </section>

          <section>
            <h2>Exact Mathematical Conversion Constants &amp; Reciprocal Formulas</h2>
            <p>
              To derive the exact conversion constants between US MPG, Imperial (UK) MPG, and Liters per 100 Kilometers, we apply the legal metrological definitions established by the International Organization for Standardization (ISO) and the US National Institute of Standards and Technology (NIST):
            </p>
            <ul>
              <li>\(1\text{ International Mile} \equiv 1.609344\text{ Kilometers}\)</li>
              <li>\(1\text{ US Liquid Gallon} \equiv 3.785411784\text{ Liters}\)</li>
              <li>\(1\text{ Imperial (UK) Gallon} \equiv 4.54609\text{ Liters}\)</li>
            </ul>

            <div class="formula-card">
              <h3>Harmonic Conversion Formulas</h3>
              <p>$$\text{L/100km from US MPG: } L/100\text{km} = \frac{100 \times 3.785411784}{1.609344 \times \text{MPG}_{\text{US}}} = \frac{235.214583}{\text{MPG}_{\text{US}}}$$</p>
              <p>$$\text{US MPG from L/100km: } \text{MPG}_{\text{US}} = \frac{235.214583}{L/100\text{km}}$$</p>
              <p>$$\text{L/100km from UK MPG: } L/100\text{km} = \frac{100 \times 4.54609}{1.609344 \times \text{MPG}_{\text{UK}}} = \frac{282.480936}{\text{MPG}_{\text{UK}}}$$</p>
              <p>$$\text{UK MPG to US MPG: } \text{MPG}_{\text{UK}} = \text{MPG}_{\text{US}} \times \frac{4.54609}{3.785411784} \approx 1.20095 \times \text{MPG}_{\text{US}}$$</p>
              <p>$$\text{Kilometers per Liter (km/L): } \text{km/L} = \frac{100}{L/100\text{km}} = 0.425144 \times \text{MPG}_{\text{US}}$$</p>
              <p>$$\text{Gallons per 100 Miles: } \text{gal/100mi} = \frac{100}{\text{MPG}_{\text{US}}} = \frac{L/100\text{km}}{2.352146}$$</p>
            </div>
          </section>

          <section>
            <h2>The 'MPG Illusion' &amp; Why Non-Linear Thinking Deceives Car Buyers</h2>
            <p>
              In 2008, behavioral scientists Richard Larrick and Jack Soll published groundbreaking research in <em>Science</em> demonstrating that consumers systematically misjudge gasoline savings because fuel efficiency in MPG scales as a hyperbola rather than a straight line.
            </p>
            <p>
              Consider a fleet manager who must choose between two distinct vehicle replacement initiatives across a 10,000-mile operating cycle:
            </p>
            <ol>
              <li><strong>Scenario A:</strong> Upgrading a fleet of large cargo vans from <strong>10 MPG to 15 MPG</strong> (a +5 MPG improvement).</li>
              <li><strong>Scenario B:</strong> Upgrading an administrative pool of compact passenger sedans from <strong>35 MPG to 50 MPG</strong> (a +15 MPG improvement).</li>
            </ol>
            <p>
              Intuition leads most people to believe that Scenario B saves three times as much fuel as Scenario A. However, examining actual volumetric consumption reveals the dramatic truth:
            </p>
            <ul>
              <li><strong>Scenario A (10 to 15 MPG):</strong>
                $$\text{Gallons consumed at 10 MPG} = \frac{10,000}{10} = 1,000\text{ gal}$$
                $$\text{Gallons consumed at 15 MPG} = \frac{10,000}{15} = 666.67\text{ gal}$$
                $$\mathbf{\text{Net Fuel Saved}} = 1,000 - 666.67 = \mathbf{333.33\text{ gallons}}$$
              </li>
              <li><strong>Scenario B (35 to 50 MPG):</strong>
                $$\text{Gallons consumed at 35 MPG} = \frac{10,000}{35} = 285.71\text{ gal}$$
                $$\text{Gallons consumed at 50 MPG} = \frac{10,000}{50} = 200.00\text{ gal}$$
                $$\mathbf{\text{Net Fuel Saved}} = 285.71 - 200.00 = \mathbf{85.71\text{ gallons}}$$
              </li>
            </ul>
            <p>
              Replacing the 10 MPG truck saves nearly <strong>four times more fuel</strong> than replacing the 35 MPG car, despite gaining only 5 MPG versus 15 MPG. Because of this psychological distortion, the US EPA now mandates that all new vehicle window stickers ("Monroney labels") prominently display <strong>Gallons per 100 Miles</strong> alongside classic MPG figures.
            </p>
          </section>

          <section>
            <h2>Comparative Fuel Economy &amp; Carbon Footprint Benchmark Table</h2>
            <p>
              The technical table below cross-references automotive vehicle classes against their nominal consumption in both metric and imperial units, accompanied by annual fuel usage and typical greenhouse gas emissions based on combustion of E10 unleaded gasoline (yielding \(2.31\text{ kg CO}_2\text{/L}\) or \(8.89\text{ kg CO}_2\text{/gal}\)):
            </p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>Vehicle Class &amp; Powertrain</th>
                  <th>US MPG</th>
                  <th>UK MPG</th>
                  <th>L/100km</th>
                  <th>km/L</th>
                  <th>Gal / 100 mi</th>
                  <th>Annual CO₂ (15k km / ~9.3k mi)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Heavy Commercial Pickup / V8 SUV</strong></td>
                  <td>14.0</td>
                  <td>16.8</td>
                  <td>16.80</td>
                  <td>5.95</td>
                  <td>7.14</td>
                  <td>5,821 kg CO₂</td>
                </tr>
                <tr>
                  <td><strong>Full-Size Crossover / Minivan</strong></td>
                  <td>22.0</td>
                  <td>26.4</td>
                  <td>10.69</td>
                  <td>9.35</td>
                  <td>4.55</td>
                  <td>3,704 kg CO₂</td>
                </tr>
                <tr>
                  <td><strong>Mid-Size Turbocharged Sedan</strong></td>
                  <td>30.0</td>
                  <td>36.0</td>
                  <td>7.84</td>
                  <td>12.75</td>
                  <td>3.33</td>
                  <td>2,717 kg CO₂</td>
                </tr>
                <tr>
                  <td><strong>Compact Subcompact Hatchback</strong></td>
                  <td>38.0</td>
                  <td>45.6</td>
                  <td>6.19</td>
                  <td>16.16</td>
                  <td>2.63</td>
                  <td>2,145 kg CO₂</td>
                </tr>
                <tr>
                  <td><strong>Full Hybrid-Electric Vehicle (HEV)</strong></td>
                  <td>52.0</td>
                  <td>62.4</td>
                  <td>4.52</td>
                  <td>22.11</td>
                  <td>1.92</td>
                  <td>1,566 kg CO₂</td>
                </tr>
                <tr>
                  <td><strong>Plug-In Hybrid (PHEV Charge Sustaining)</strong></td>
                  <td>46.0</td>
                  <td>55.2</td>
                  <td>5.11</td>
                  <td>19.56</td>
                  <td>2.17</td>
                  <td>1,771 kg CO₂</td>
                </tr>
                <tr>
                  <td><strong>Battery Electric Vehicle (EV @ 120 MPGe)</strong></td>
                  <td>120.0*</td>
                  <td>144.1*</td>
                  <td>1.96*</td>
                  <td>51.02*</td>
                  <td>0.83*</td>
                  <td>0 kg direct (tailpipe)</td>
                </tr>
              </tbody>
            </table>
            <p class="table-footnote"><em>*EV values represented in gasoline gallon equivalent (MPGe) based on 33.705 kWh = 1 US gallon.</em></p>
          </section>

          <section>
            <h2>Worked Engineering Case Study: Commercial Fleet Decarbonization Audit</h2>
            <div class="worked-example-card">
              <h3>Engineering Scenario: Delivery Fleet Fuel Analysis</h3>
              <p>
                A logistics company operates a regional delivery fleet of <strong>50 commercial step vans</strong>. Each vehicle logs an average of <strong>24,000 miles (38,624 km) per year</strong>. The fleet currently averages <strong>11.5 US MPG</strong> on diesel fuel. The company is evaluating a fleet refresh with new aerodynamic clean-diesel vans rated at <strong>17.0 US MPG</strong>.
              </p>
              <p>The sustainability engineer must compute:</p>
              <ol>
                <li>The baseline and new fuel consumption in Liters per 100 Kilometers (\(\text{L/100km}\)).</li>
                <li>The annual fuel saved per individual van in US Gallons and Liters.</li>
                <li>The total annual monetary fuel savings for all 50 vans at diesel pricing of \$3.90/gallon.</li>
                <li>The annual fleet-wide carbon footprint reduction in metric tons of \(\text{CO}_2\) (diesel produces \(10.18\text{ kg CO}_2\text{/gal}\)).</li>
              </ol>

              <h4>Step-by-Step Calculation:</h4>
              <p><strong>1. Convert Fuel Economy to L/100km:</strong></p>
              <p>$$\text{Baseline Consumption} = \frac{235.215}{11.5} = 20.45\text{ L/100km}$$</p>
              <p>$$\text{New Van Consumption} = \frac{235.215}{17.0} = 13.84\text{ L/100km}$$</p>

              <p><strong>2. Annual Fuel Consumption per Van (24,000 miles):</strong></p>
              <p>$$\text{Baseline Gallons/van} = \frac{24,000}{11.5} = 2,086.96\text{ gal} \quad (7,899.9\text{ Liters})$$</p>
              <p>$$\text{New Gallons/van} = \frac{24,000}{17.0} = 1,411.76\text{ gal} \quad (5,344.1\text{ Liters})$$</p>
              <p>$$\text{Net Savings per Van} = 2,086.96 - 1,411.76 = 675.20\text{ gal} \quad (2,555.8\text{ Liters})$$</p>

              <p><strong>3. Fleet-Wide Monetary Savings (50 Vans):</strong></p>
              <p>$$\text{Total Fleet Fuel Saved} = 50 \times 675.20\text{ gal} = 33,760\text{ gallons/year}$$</p>
              <p>$$\text{Financial Savings} = 33,760\text{ gal} \times \$3.90\text{/gal} = \mathbf{\$131,664\text{ / year}}$$</p>

              <p><strong>4. Fleet-Wide Greenhouse Gas Reduction:</strong></p>
              <p>$$\text{Carbon Reduced} = 33,760\text{ gal} \times 10.18\text{ kg CO}_2\text{/gal} = 343,677\text{ kg CO}_2 = \mathbf{343.68\text{ metric tons CO}_2}$$</p>

              <p>
                <strong>Audit Conclusion:</strong> By increasing fleet efficiency from 11.5 to 17.0 MPG, the logistics provider trims fuel expenditure by \$131,664 annually and eliminates over 343 metric tons of greenhouse gas emissions, confirming the disproportionate impact of improving heavy vehicles at the lower end of the MPG spectrum.
              </p>
            </div>
          </section>

          <section class="faq-section">
            <h2>Frequently Asked Questions Regarding Automotive Fuel Units</h2>
            <div class="faq-item">
              <h3>Why do WLTP ratings in Europe report better fuel economy than US EPA ratings?</h3>
              <p>The European WLTP (Worldwide Harmonized Light Vehicles Test Procedure) test cycle features gentler acceleration phases, fewer cold starts, and tests vehicles under warmer laboratory ambient conditions compared to the US EPA's multi-cycle methodology. The EPA tests five distinct cycles: FTP-75 (city), HWFET (highway), US06 (aggressive high-speed), SC03 (air conditioning load at 95°F), and Cold FTP (20°F cold start). Consequently, EPA ratings are typically 15% to 22% lower (stricter) than European WLTP ratings for the identical automobile.</p>
            </div>
            <div class="faq-item">
              <h3>How does ethanol blended fuel (E10 or E85) impact fuel economy?</h3>
              <p>Ethanol has approximately 33% lower volumetric energy density than pure gasoline (\(23.5\text{ MJ/L}\) vs \(34.2\text{ MJ/L}\)). Standard commercial E10 gasoline (10% ethanol blend) decreases vehicle fuel economy by approximately 3% to 4% compared to 100% petroleum gasoline. High-ethanol E85 (85% ethanol) reduces fuel economy by roughly 25% to 30%, meaning a vehicle getting 30 MPG on regular fuel will achieve only 21 to 22 MPG on E85.</p>
            </div>
            <div class="faq-item">
              <h3>Can I convert fuel economy for marine vessels or aviation aircraft?</h3>
              <p>In aviation and commercial marine shipping, fuel consumption is measured in mass units per time, such as <strong>Pounds per Hour (lb/hr)</strong> or <strong>Specific Fuel Consumption (SFC in g/kWh)</strong>, rather than miles per gallon. Because aircraft flight speeds vary widely with headwinds and altitude, and aircraft mass drops significantly as fuel is consumed during flight, volumetric distance metrics are inadequate for aeronautical flight planning.</p>
            </div>
            <div class="faq-item">
              <h3>What is the relationship between tire pressure and fuel consumption?</h3>
              <p>Under-inflated tires increase rolling resistance because the tire sidewall flexes more dramatically as the wheel rotates. According to the US Department of Energy, for every 1.0 psi drop in pressure across all four tires, fuel economy drops by approximately 0.2%. A vehicle underinflated by 5 psi experiences a 1% decline in fuel efficiency, equivalent to consuming roughly 0.1 additional liters of fuel per 100 kilometers.</p>
            </div>
          </section>
        </article>
      </div>

      <aside class="converter-sidebar">
        <div class="sidebar-card">
          <h3>Related Energy &amp; Motion Tools</h3>
          <ul class="sidebar-links">
            <li><a href="speed-converter.html">Speed Converter (mph, km/h, m/s)</a></li>
            <li><a href="energy-converter.html">Energy Converter (kWh, Joules, BTU)</a></li>
            <li><a href="power-converter.html">Power Converter (HP, kW, Watts)</a></li>
            <li><a href="volume-converter.html">Volume Converter (gallons, liters)</a></li>
            <li><a href="length-converter.html">Length Converter (miles, kilometers)</a></li>
            <li><a href="flow-rate-converter.html">Flow Rate Converter (GPM, L/min)</a></li>
            <li><a href="pressure-converter.html">Pressure Converter (psi, bar, kPa)</a></li>
            <li><a href="weight-converter.html">Weight Converter (lbs, kg)</a></li>
          </ul>
        </div>
        <div class="sidebar-card">
          <h3>The Golden Formula</h3>
          <p class="sidebar-tip">
            Need a quick mental conversion between US MPG and L/100km? Memorize the number <strong>235</strong>:
            <br><br>
            $$\text{L/100km} \approx \frac{235}{\text{MPG}}$$
            $$\text{MPG} \approx \frac{235}{\text{L/100km}}$$
          </p>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="footer-logo">CalcHub</div>
          <p>The open-access platform for professional scientific, engineering, financial, and physiological calculations and unit conversions.</p>
        </div>
        <div class="footer-links">
          <h4>Converter Hubs</h4>
          <ul>
            <li><a href="converter.html">All Unit Converters</a></li>
            <li><a href="length-converter.html">Length Converter</a></li>
            <li><a href="weight-converter.html">Weight Converter</a></li>
            <li><a href="speed-converter.html">Speed Converter</a></li>
          </ul>
        </div>
        <div class="footer-links">
          <h4>Transportation &amp; Energy</h4>
          <ul>
            <li><a href="fuel-economy-converter.html">Fuel Economy Converter</a></li>
            <li><a href="energy-converter.html">Energy Converter</a></li>
            <li><a href="power-converter.html">Power Converter</a></li>
            <li><a href="pressure-converter.html">Pressure Converter</a></li>
          </ul>
        </div>
        <div class="footer-links">
          <h4>Company &amp; Legal</h4>
          <ul>
            <li><a href="about.html">About CalcHub</a></li>
            <li><a href="contact.html">Contact Us</a></li>
            <li><a href="privacy.html">Privacy Policy</a></li>
            <li><a href="terms.html">Terms of Service</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. Standard-grade metrology verified against NIST Special Publication 811 and ISO 80000 standards.</p>
      </div>
    </div>
  </footer>

  <script>
    (function() {
      // Internal standard representation: L/100km (fuel consumption)
      var C_US = 235.214583;
      var C_UK = 282.480936;

      function toL100km(val, unit) {
        if (val <= 0) return 0;
        if (unit === 'l_100km') return val;
        if (unit === 'mpg_us') return C_US / val;
        if (unit === 'mpg_uk') return C_UK / val;
        if (unit === 'km_l') return 100.0 / val;
        if (unit === 'gal_100mi') return val * 2.35214583;
        return val;
      }

      function fromL100km(l100km, unit) {
        if (l100km <= 0) return 0;
        if (unit === 'l_100km') return l100km;
        if (unit === 'mpg_us') return C_US / l100km;
        if (unit === 'mpg_uk') return C_UK / l100km;
        if (unit === 'km_l') return 100.0 / l100km;
        if (unit === 'gal_100mi') return l100km / 2.35214583;
        return l100km;
      }

      var unitLabels = {
        mpg_us: 'US MPG',
        l_100km: 'L/100km',
        mpg_uk: 'UK MPG',
        km_l: 'km/L',
        gal_100mi: 'gal/100mi'
      };

      var fromInput = document.getElementById('fuelFromVal');
      var fromSelect = document.getElementById('fuelFromUnit');
      var toInput = document.getElementById('fuelToVal');
      var toSelect = document.getElementById('fuelToUnit');
      var swapBtn = document.getElementById('fuelSwapBtn');

      var equationEl = document.getElementById('fuelEquation');
      var annualLitersEl = document.getElementById('fuelAnnualLiters');
      var annualGallonsEl = document.getElementById('fuelAnnualGallons');
      var co2ValEl = document.getElementById('fuelCo2Val');

      function calculate() {
        var val = parseFloat(fromInput.value);
        if (isNaN(val) || val <= 0) {
          toInput.value = '';
          return;
        }

        var fromUnit = fromSelect.value;
        var toUnit = toSelect.value;

        var l100km = toL100km(val, fromUnit);
        var result = fromL100km(l100km, toUnit);

        toInput.value = (Math.round(result * 100) / 100).toFixed(2);

        if (equationEl) {
          equationEl.textContent = val + " " + unitLabels[fromUnit] + " = " + toInput.value + " " + unitLabels[toUnit];
        }

        if (annualLitersEl && annualGallonsEl && co2ValEl) {
          // Annual 15,000 km
          var annualL = (15000.0 / 100.0) * l100km;
          annualLitersEl.textContent = Math.round(annualL).toLocaleString() + " Liters";

          // Annual 10,000 miles in gallons
          // gal/100mi = l100km / 2.35214583
          var galPer100mi = l100km / 2.35214583;
          var annualG = galPer100mi * 100.0;
          annualGallonsEl.textContent = (Math.round(annualG * 10) / 10).toFixed(1) + " US Gallons";

          // CO2 estimate: ~2.31 kg CO2 per liter gasoline for 15,000 km
          var co2Kg = annualL * 2.31;
          co2ValEl.textContent = Math.round(co2Kg).toLocaleString() + " kg CO₂";
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

# -------------------------------------------------------------
# 8. ANGLE CONVERTER
# -------------------------------------------------------------
angle_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Angle Converter — Degrees, Radians, Gradians, MOA, mrad | CalcHub</title>
  <meta name="description" content="Convert geometric and ballistics angles between degrees (°), radians (rad), gradians (gon), minutes of arc (MOA), seconds of arc, milliradians (mrad), and full circles.">
  <meta name="keywords" content="angle converter, degrees to radians, radians to degrees, moa to mrad, arcseconds to degrees, gradians to degrees, mil dot calculator, ballistic reticle converter, circular trigonometry">
  <meta name="author" content="CalcHub Geodesy & Ballistic Trigonometry Engineering Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/angle-converter.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="Angle Converter — Degrees, Radians, Gradians, MOA, mrad | CalcHub">
  <meta property="og:description" content="Convert geometric and ballistics angles between degrees (°), radians (rad), gradians (gon), minutes of arc (MOA), seconds of arc, milliradians (mrad), and full circles.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/angle-converter.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/angle-converter.html#app",
      "name": "Precision Geometric & Ballistic Angle Converter",
      "url": "https://calchub.org/angle-converter.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "High-precision plane angle conversion engine translating between SI radians, sexagesimal degrees, minutes of arc (MOA), NATO mils, and astronomical arcseconds."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Universal Unit Converters", "item": "https://calchub.org/converter.html"},
        {"@type": "ListItem", "position": 3, "name": "Angle Converter", "item": "https://calchub.org/angle-converter.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the physical definition of a radian (rad) in the International System of Units?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The radian (rad) is the coherent SI unit of plane angle, defined as the angle subtended at the center of a circle by an arc whose length is equal to the radius of the circle (s = r). Because the circumference of a circle equals 2πr, one full revolution contains exactly 2π radians (approx. 6.2831853 rad). Consequently, 1 radian = 180 / π ≈ 57.2957795 degrees."
          }
        },
        {
          "@type": "Question",
          "name": "What is the relationship between Minutes of Angle (MOA) and Milliradians (mrad / mils) in ballistics?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "One Minute of Angle (1 MOA) is 1/60th of a degree. One milliradian (1 mrad) is 0.001 radian, which equals (0.001 × 180 / π) × 60 ≈ 3.43775 MOA. At 100 yards distance, 1 MOA subtends 1.047 inches (frequently approximated as 1.0 inch), whereas 1 mrad subtends exactly 10 cm at 100 meters (or 3.6 inches at 100 yards). Scope turrets with 0.1 mrad clicks adjust impact by 1 cm per 100 m."
          }
        },
        {
          "@type": "Question",
          "name": "What is a Gradian (gon) and where is it used today?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A gradian (also known as a gon or grade) is a decimalized angular measurement where a right angle is divided into exactly 100 gradians, making a full circle 400 gradians. Conceived during the French Revolution to align angles with the decimal metric system, gradians remain standard in European civil land surveying, geodetic total stations, and tunnel construction."
          }
        },
        {
          "@type": "Question",
          "name": "How does an astronomical Arcsecond define the astrophysical distance unit known as a Parsec?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "An arcsecond (\") is 1/3600th of a degree. A parsec (parallax second) is defined as the astronomical distance at which the mean radius of Earth's orbit (1 Astronomical Unit, or 1 AU ≈ 149,597,871 km) subtends an angle of exactly 1 arcsecond. Through the small-angle tangent formula, 1 parsec = 1 AU / tan(1\") ≈ 3.08567758 × 10^16 meters (approx. 3.26 light-years)."
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
    <div class="header-container">
      <a href="index.html" class="logo">CalcHub</a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="converter.html" class="active">Converters</a>
        <a href="financial.html">Finance</a>
        <a href="fitness.html">Fitness</a>
        <a href="health.html">Health</a>
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
            <span>Angle Converter</span>
          </div>
          <span class="badge">Trigonometry, Geodesy &amp; Ballistics</span>
          <h1>Precision Angle Converter</h1>
          <p class="tagline">Convert between geometric and optical angles: degrees, radians, gradians, MOA, arcseconds, and milliradians with mathematical rigor.</p>
        </div>

        <div class="calculator-container card-surface">
          <div class="converter-box">
            <div class="converter-inputs-grid">
              <div class="input-col">
                <label for="angleFromVal" class="input-label">From Value</label>
                <input type="number" id="angleFromVal" class="converter-num-input" value="45" step="any" placeholder="Enter angle">
                <label for="angleFromUnit" class="input-label sub-label">From Unit</label>
                <select id="angleFromUnit" class="converter-select">
                  <option value="deg" selected>Degrees (°)</option>
                  <option value="rad">Radians (rad)</option>
                  <option value="grad">Gradians / Gon (gon)</option>
                  <option value="moa">Minutes of Arc (MOA)</option>
                  <option value="arcsec">Seconds of Arc (arcsec / ")</option>
                  <option value="mrad">Milliradians (mrad / mil)</option>
                  <option value="turn">Full Circles / Revolutions</option>
                </select>
              </div>

              <div class="swap-col">
                <button type="button" id="angleSwapBtn" class="swap-button" title="Swap input and output units" aria-label="Swap units">
                  &#8644;
                </button>
              </div>

              <div class="input-col">
                <label for="angleToVal" class="input-label">Converted Value</label>
                <input type="text" id="angleToVal" class="converter-num-input output-val" readonly value="0.785398">
                <label for="angleToUnit" class="input-label sub-label">To Unit</label>
                <select id="angleToUnit" class="converter-select">
                  <option value="deg">Degrees (°)</option>
                  <option value="rad" selected>Radians (rad)</option>
                  <option value="grad">Gradians / Gon (gon)</option>
                  <option value="moa">Minutes of Arc (MOA)</option>
                  <option value="arcsec">Seconds of Arc (arcsec / ")</option>
                  <option value="mrad">Milliradians (mrad / mil)</option>
                  <option value="turn">Full Circles / Revolutions</option>
                </select>
              </div>
            </div>

            <div class="converter-quick-presets">
              <span class="preset-label">Standard Trigonometric &amp; Ballistic Benchmarks:</span>
              <button type="button" class="preset-chip" data-val="90" data-from="deg" data-to="rad">90° Right Angle (π/2 rad)</button>
              <button type="button" class="preset-chip" data-val="180" data-from="deg" data-to="rad">180° Straight (π rad)</button>
              <button type="button" class="preset-chip" data-val="1" data-from="moa" data-to="mrad">1 MOA (0.291 mrad)</button>
              <button type="button" class="preset-chip" data-val="1" data-from="mrad" data-to="moa">1 mrad (3.438 MOA)</button>
            </div>

            <div class="conversion-summary-panel" id="angleSummaryCard">
              <div class="summary-line">
                <span class="summary-label">Direct Relation:</span>
                <span class="summary-formula" id="angleEquation">45° = 0.785398 rad</span>
              </div>
              <div class="summary-submetrics">
                <div class="submetric-item">
                  <span class="submetric-name">Arc Length (r = 1m):</span>
                  <span class="submetric-val" id="angleArcVal">0.7854 m</span>
                </div>
                <div class="submetric-item">
                  <span class="submetric-name">Dispersion @ 100m:</span>
                  <span class="submetric-val" id="angleDisp100m">78.54 m</span>
                </div>
                <div class="submetric-item">
                  <span class="submetric-name">Sin / Cos / Tan:</span>
                  <span class="submetric-val" id="angleTrigVal">sin: 0.707 | cos: 0.707</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <section>
            <h2>Geometrical Metrology of Plane Angles</h2>
            <p>
              A plane angle represents the geometric divergence between two intersecting rays originating from a shared vertex, or the rotational aperture through which a line sweeps around a fixed pivot point. In classical mathematics, geodesy, navigation, computer graphics, and precision ballistics, angles form the trigonometric infrastructure that bridges linear spatial distances and directional coordinates.
            </p>
            <p>
              In the International System of Units (SI), the coherent derived unit for plane angles is the <strong>radian (rad)</strong>. Unlike traditional base units such as the meter or kilogram, the radian is a dimensionless ratio of two lengths (arc length divided by radius, \(s/r\)), defined such that one complete circular revolution contains exactly \(2\pi\) radians:
            </p>
            <p>
              $$\theta = \frac{s}{r} \quad [\text{meters / meters} = \text{dimensionless rad}]$$
            </p>
            <p>
              Despite the pure mathematical elegance of the radian in calculus and differential equations, multiple angular measurement conventions remain dominant in distinct engineering disciplines:
            </p>
            <ul>
              <li><strong>Sexagesimal Degrees (°, &prime;, &Prime;):</strong> Inherited from ancient Babylonian astronomy (dividing a circle into 360 equal parts, each degree into 60 minutes of arc, and each minute into 60 seconds of arc). This remains the global benchmark for cartography, aeronautical navigation, and mechanical drafting.</li>
              <li><strong>Minutes of Angle (MOA):</strong> Exactly \(\frac{1}{60}\) of a degree. Widely utilized in firearm marksmanship and precision optical rifle scopes because 1 MOA closely corresponds to 1 inch at 100 yards.</li>
              <li><strong>Milliradians (mrad / mils):</strong> Defined as \(\frac{1}{1000}\) of a radian. The metric standard in modern precision riflescopes and military artillery because 1 mrad corresponds exactly to 10 centimeters of lateral shift at 100 meters range (or 1 meter at 1,000 meters).</li>
              <li><strong>Gradians / Gon (gon):</strong> The metric decimalization of angles, where a right angle equals exactly 100 gradians and a complete circle comprises 400 gradians. Standard in European geodetic engineering and civil tunnel construction.</li>
            </ul>
          </section>

          <section>
            <h2>Exact Mathematical Conversion Constants &amp; Analytical Formulas</h2>
            <p>
              Converting between radians, degrees, gradians, and angular sub-divisions involves exact analytical relationships tied to the fundamental circle constant \(\pi \approx 3.141592653589793\):
            </p>

            <div class="formula-card">
              <h3>Analytical Angle Formulas</h3>
              <p>$$\text{Full Revolution: } 1\text{ turn} \equiv 360^\circ \equiv 2\pi\text{ rad} \equiv 400\text{ gon} \equiv 21,600\text{ MOA} \equiv 1,296,000''$$</p>
              <p>$$\text{Degrees to Radians: } \theta_{\text{rad}} = \theta_{\text{deg}} \times \frac{\pi}{180} \approx \theta_{\text{deg}} \times 0.0174532925$$</p>
              <p>$$\text{Radians to Degrees: } \theta_{\text{deg}} = \theta_{\text{rad}} \times \frac{180}{\pi} \approx \theta_{\text{rad}} \times 57.29577951$$</p>
              <p>$$\text{Degrees to Gradians: } \theta_{\text{gon}} = \theta_{\text{deg}} \times \frac{400}{360} = \theta_{\text{deg}} \times \frac{10}{9}$$</p>
              <p>$$\text{MOA to Milliradians (mrad): } 1\text{ MOA} = \frac{\pi}{180 \times 60} \times 1000\text{ mrad} \approx 0.2908882\text{ mrad}$$</p>
              <p>$$\text{Milliradians to MOA: } 1\text{ mrad} = \frac{1}{0.2908882} \approx 3.43774677\text{ MOA}$$</p>
              <p>$$\text{Circular Arc Length: } s = r \cdot \theta_{\text{rad}}$$</p>
              <p>$$\text{Sector Surface Area: } A = \frac{1}{2} r^2 \theta_{\text{rad}}$$</p>
            </div>
          </section>

          <section>
            <h2>Ballistic Reticle Dynamics: MOA vs. Milliradians (MILs)</h2>
            <p>
              In long-range optical marksmanship, riflescopes feature adjustment turrets and illuminated reticles calibrated in either <strong>MOA</strong> or <strong>Milliradians (MILs)</strong>. Misinterpreting these units causes major trajectory misses at extended distances:
            </p>
            <ul>
              <li><strong>True MOA (TMOA):</strong> One true MOA is \(\frac{1}{60}^\circ\). Subtended linear height at distance \(D\) is:
                $$h = D \times \tan\left(\frac{1^\circ}{60}\right)$$
                At exactly 100 yards (3,600 inches), \(h = 3,600 \times \tan(0.016667^\circ) = \mathbf{1.04719755\text{ inches}}\). At 1,000 yards, 1 TMOA subtends \(10.47\text{ inches}\).</li>
              <li><strong>Shooter's MOA (SMOA):</strong> Often used in American scopes, rounded to exactly 1.000 inch at 100 yards. Over 1,000 yards, the difference between TMOA and SMOA accumulates into a \(4.7\text{ inch}\) elevation error.</li>
              <li><strong>Milliradian (mrad / MIL):</strong> Subtends \(1\text{ unit}\) at \(1,000\text{ units}\) of distance:
                $$\text{At } 100\text{ meters}: 1\text{ mrad} = 100\text{ m} \times 0.001 = 0.100\text{ m} = \mathbf{10.0\text{ cm}}$$
                $$\text{At } 100\text{ yards}: 1\text{ mrad} = 3,600\text{ inches} \times 0.001 = \mathbf{3.60\text{ inches}}$$
                Standard MIL turrets feature \(0.1\text{ mrad}\) clicks, translating to exactly \(1\text{ cm}\) of point-of-impact shift per click at 100 meters, or \(10\text{ cm}\) per click at 1,000 meters.</li>
            </ul>
          </section>

          <section>
            <h2>Comparative Angular Reference Benchmark Matrix</h2>
            <p>
              The multi-column engineering matrix below compares critical geometric angles across degrees, radians, gradians, minutes of arc, and milliradians:
            </p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>Angular Angle Description</th>
                  <th>Degrees (°)</th>
                  <th>Radians (rad)</th>
                  <th>Gradians (gon)</th>
                  <th>Arcminutes (MOA)</th>
                  <th>Milliradians (mrad)</th>
                  <th>Dispersion @ 100m Range</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Telescope Resolution Limit</strong></td>
                  <td>0.000278° (1")</td>
                  <td>4.848 × 10⁻⁶ rad</td>
                  <td>0.000309 gon</td>
                  <td>0.0167 MOA</td>
                  <td>0.0048 mrad</td>
                  <td>0.48 mm</td>
                </tr>
                <tr>
                  <td><strong>1 Minute of Angle (1 MOA)</strong></td>
                  <td>0.016667°</td>
                  <td>0.000291 rad</td>
                  <td>0.018519 gon</td>
                  <td>1.0000 MOA</td>
                  <td>0.2909 mrad</td>
                  <td>2.91 cm (1.14")</td>
                </tr>
                <tr>
                  <td><strong>1 Milliradian (1 mrad)</strong></td>
                  <td>0.057296°</td>
                  <td>0.001000 rad</td>
                  <td>0.063662 gon</td>
                  <td>3.4377 MOA</td>
                  <td>1.0000 mrad</td>
                  <td>10.00 cm (3.94")</td>
                </tr>
                <tr>
                  <td><strong>1 Degree (1°)</strong></td>
                  <td>1.0000°</td>
                  <td>0.017453 rad</td>
                  <td>1.1111 gon</td>
                  <td>60.00 MOA</td>
                  <td>17.453 mrad</td>
                  <td>1.745 m</td>
                </tr>
                <tr>
                  <td><strong>30° Angle (Equilateral Tri / 6)</strong></td>
                  <td>30.00°</td>
                  <td>0.523599 rad (\(\pi/6\))</td>
                  <td>33.33 gon</td>
                  <td>1,800 MOA</td>
                  <td>523.6 mrad</td>
                  <td>52.36 m</td>
                </tr>
                <tr>
                  <td><strong>45° Angle (Right Isosceles)</strong></td>
                  <td>45.00°</td>
                  <td>0.785398 rad (\(\pi/4\))</td>
                  <td>50.00 gon</td>
                  <td>2,700 MOA</td>
                  <td>785.4 mrad</td>
                  <td>78.54 m</td>
                </tr>
                <tr>
                  <td><strong>90° Angle (Perpendicular Right)</strong></td>
                  <td>90.00°</td>
                  <td>1.570796 rad (\(\pi/2\))</td>
                  <td>100.00 gon</td>
                  <td>5,400 MOA</td>
                  <td>1,570.8 mrad</td>
                  <td>100.0 m (Subtended ray)</td>
                </tr>
                <tr>
                  <td><strong>180° Angle (Straight Line)</strong></td>
                  <td>180.00°</td>
                  <td>3.141593 rad (\(\pi\))</td>
                  <td>200.00 gon</td>
                  <td>10,800 MOA</td>
                  <td>3,141.6 mrad</td>
                  <td>N/A (Opposite direction)</td>
                </tr>
                <tr>
                  <td><strong>360° Angle (Full Circle / 1 Turn)</strong></td>
                  <td>360.00°</td>
                  <td>6.283185 rad (\(2\pi\))</td>
                  <td>400.00 gon</td>
                  <td>21,600 MOA</td>
                  <td>6,283.2 mrad</td>
                  <td>0 m (Coincident ray)</td>
                </tr>
              </tbody>
            </table>
          </section>

          <section>
            <h2>Worked Engineering Case Study: Long-Range Rifle Scope Reticle Zeroing</h2>
            <div class="worked-example-card">
              <h3>Engineering Scenario: Long-Distance Crosswind Deflection Correction</h3>
              <p>
                A competitive precision rifle marksman is engaging a steel target at a confirmed range of <strong>800 meters (874.89 yards)</strong>. The ballistic computer predicts a 10 mph 90-degree crosswind will blow the 6.5mm Creedmoor bullet <strong>1.92 meters (192 cm)</strong> to the right by the time it reaches the 800m target.
              </p>
              <p>The marksman's scope is equipped with a <strong>MIL reticle (0.1 mrad click turrets)</strong>. The marksman needs to determine:</p>
              <ol>
                <li>The required windage correction in Milliradians (\(\text{mrad}\)).</li>
                <li>The exact number of clicks to dial on the scope turret (at \(0.1\text{ mrad/click}\)).</li>
                <li>The equivalent angular offset in Minutes of Angle (\(\text{MOA}\)) if using a backup rifle with an MOA optic.</li>
              </ol>

              <h4>Step-by-Step Calculation:</h4>
              <p><strong>1. Calculate Required Offset in Milliradians:</strong></p>
              <p>At 800 meters, 1 mrad subtends \(800\text{ m} \times 0.001 = 0.80\text{ meters} = 80\text{ cm}\).</p>
              <p>$$\text{Angle in mrad} = \frac{\text{Lateral Deflection (cm)}}{\text{Subtension per mrad @ 800m}} = \frac{192\text{ cm}}{80\text{ cm/mrad}} = \mathbf{2.40\text{ mrad}}$$</p>

              <p><strong>2. Determine Scope Turret Click Adjustment:</strong></p>
              <p>Each turret click provides \(0.1\text{ mrad}\) of angular movement:</p>
              <p>$$\text{Turret Clicks} = \frac{2.40\text{ mrad}}{0.10\text{ mrad/click}} = \mathbf{24\text{ clicks left}}$$</p>

              <p><strong>3. Convert Correction to Minutes of Angle (MOA):</strong></p>
              <p>Using the exact conversion factor (\(1\text{ mrad} = 3.43774677\text{ MOA}\)):</p>
              <p>$$\text{Angle in MOA} = 2.40\text{ mrad} \times 3.43774677\text{ MOA/mrad} = \mathbf{8.25\text{ MOA}}$$</p>
              <p>If utilizing a \(1/4\text{ MOA}\) click scope, the shooter dials \(8.25 \times 4 = \mathbf{33\text{ clicks left}}\).</p>

              <p>
                <strong>Marksman Conclusion:</strong> Dialing 2.4 mrad (24 clicks left) shifts the rifle barrel axis to exactly compensate for the 1.92-meter lateral wind deflection, delivering a center-mass impact at 800 meters.
              </p>
            </div>
          </section>

          <section class="faq-section">
            <h2>Frequently Asked Questions Regarding Angular Measurements</h2>
            <div class="faq-item">
              <h3>Why does a full circle contain 360 degrees instead of 100 or 400?</h3>
              <p>The 360-degree division was instituted by ancient Sumerian and Babylonian astronomers around 2400 BC. They used a sexagesimal (base-60) numbering system and observed that the solar year was roughly 360 days. Crucially, the number 360 is highly composite, having 24 divisors (1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120, 180, 360), allowing a circle to be divided into halves, thirds, quarters, fifths, and sixths without encountering fractional remainder values.</p>
            </div>
            <div class="faq-item">
              <h3>What is the difference between true mathematical mils and NATO mils?</h3>
              <p>A true mathematical milliradian divides a full circle into \(2\pi \times 1,000 \approx 6,283.185\) parts. Because this fractional number is inconvenient for rapid compass and artillery calculations in the field, military organizations rounded it: <strong>NATO forces standard 6,400 mils</strong> per circle (making right angles 1,600 mils), the former <strong>Soviet Union standard 6,000 mils</strong>, and the <strong>Swedish military standard 6,300 mils</strong>. Riflescopes use true mathematical mils (6,283), whereas military compasses use NATO 6,400 mils.</p>
            </div>
            <div class="faq-item">
              <h3>Why do mathematical functions in programming languages (C, Python, Java) require radians?</h3>
              <p>In calculus, trigonometric derivatives and Taylor series expansions are valid only when angles are expressed in radians. For example, \(\frac{d}{dx}\sin(x) = \cos(x)\) is true <em>only</em> if \(x\) is in radians. If \(x\) were in degrees, the derivative would require an unwieldy scaling factor: \(\frac{d}{dx}\sin(x) = \frac{\pi}{180}\cos(x)\). To ensure performance and numerical stability, all language standard libraries (e.g., Python's <code>math.sin()</code>) enforce radian input.</p>
            </div>
            <div class="faq-item">
              <h3>What is the small-angle approximation and when is it valid?</h3>
              <p>For sufficiently small angles expressed in radians (\(\theta \ll 1\)), the trigonometric functions can be approximated by: \(\sin(\theta) \approx \theta\), \(\tan(\theta) \approx \theta\), and \(\cos(\theta) \approx 1 - \frac{\theta^2}{2}\). For angles under 0.1 radian (approx. 5.7 degrees), the error in assuming \(\sin(\theta) = \theta\) is less than 0.17%, making it invaluable in optics, pendulum mechanics, and structural deflection formulas.</p>
            </div>
          </section>
        </article>
      </div>

      <aside class="converter-sidebar">
        <div class="sidebar-card">
          <h3>Related Trigonometry &amp; Physics Tools</h3>
          <ul class="sidebar-links">
            <li><a href="length-converter.html">Length Converter (meters, yards, inches)</a></li>
            <li><a href="frequency-converter.html">Frequency Converter (Hz, RPM, rad/s)</a></li>
            <li><a href="speed-converter.html">Speed Converter (m/s, km/h, mph)</a></li>
            <li><a href="force-converter.html">Force Converter (N, lbf)</a></li>
            <li><a href="power-converter.html">Power Converter (kW, HP)</a></li>
            <li><a href="energy-converter.html">Energy Converter (Joules, BTU)</a></li>
            <li><a href="pressure-converter.html">Pressure Converter (psi, bar)</a></li>
            <li><a href="temperature-converter.html">Temperature Converter (°C, °F, K)</a></li>
          </ul>
        </div>
        <div class="sidebar-card">
          <h3>Ballistics Quick Reference</h3>
          <p class="sidebar-tip">
            Remember the scope turret rule of thumb:
            <br><br>
            <strong>1 MOA</strong> &approx; 1 inch at 100 yards.<br>
            <strong>1 mrad</strong> &approx; 10 cm at 100 meters (or 3.6 inches at 100 yards).
          </p>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="footer-logo">CalcHub</div>
          <p>The open-access platform for professional scientific, engineering, financial, and physiological calculations and unit conversions.</p>
        </div>
        <div class="footer-links">
          <h4>Converter Hubs</h4>
          <ul>
            <li><a href="converter.html">All Unit Converters</a></li>
            <li><a href="length-converter.html">Length Converter</a></li>
            <li><a href="weight-converter.html">Weight Converter</a></li>
            <li><a href="temperature-converter.html">Temperature Converter</a></li>
          </ul>
        </div>
        <div class="footer-links">
          <h4>Engineering Tools</h4>
          <ul>
            <li><a href="angle-converter.html">Angle Converter</a></li>
            <li><a href="frequency-converter.html">Frequency Converter</a></li>
            <li><a href="power-converter.html">Power Converter</a></li>
            <li><a href="force-converter.html">Force Converter</a></li>
          </ul>
        </div>
        <div class="footer-links">
          <h4>Company &amp; Legal</h4>
          <ul>
            <li><a href="about.html">About CalcHub</a></li>
            <li><a href="contact.html">Contact Us</a></li>
            <li><a href="privacy.html">Privacy Policy</a></li>
            <li><a href="terms.html">Terms of Service</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. Standard-grade metrology verified against NIST Special Publication 811 and ISO 80000 standards.</p>
      </div>
    </div>
  </footer>

  <script>
    (function() {
      // Base unit: Radians (rad)
      var factors = {
        rad: 1.0,
        deg: Math.PI / 180.0,
        grad: Math.PI / 200.0,
        moa: Math.PI / (180.0 * 60.0),
        arcsec: Math.PI / (180.0 * 3600.0),
        mrad: 0.001,
        turn: 2.0 * Math.PI
      };

      var unitLabels = {
        rad: 'rad',
        deg: '°',
        grad: 'gon',
        moa: 'MOA',
        arcsec: 'arcsec',
        mrad: 'mrad',
        turn: 'revolutions'
      };

      var fromInput = document.getElementById('angleFromVal');
      var fromSelect = document.getElementById('angleFromUnit');
      var toInput = document.getElementById('angleToVal');
      var toSelect = document.getElementById('angleToUnit');
      var swapBtn = document.getElementById('angleSwapBtn');

      var equationEl = document.getElementById('angleEquation');
      var arcValEl = document.getElementById('angleArcVal');
      var disp100mEl = document.getElementById('angleDisp100m');
      var trigValEl = document.getElementById('angleTrigVal');

      function calculate() {
        var val = parseFloat(fromInput.value);
        if (isNaN(val)) {
          toInput.value = '';
          return;
        }

        var fromUnit = fromSelect.value;
        var toUnit = toSelect.value;

        // Base radians
        var baseRad = val * factors[fromUnit];
        var result = baseRad / factors[toUnit];

        if (Math.abs(result) >= 1e7 || (Math.abs(result) < 1e-4 && result !== 0)) {
          toInput.value = result.toExponential(6);
        } else {
          toInput.value = parseFloat(result.toPrecision(7)).toString();
        }

        if (equationEl) {
          equationEl.textContent = val + unitLabels[fromUnit] + " = " + toInput.value + " " + unitLabels[toUnit];
        }

        // Submetrics
        // Arc length for r = 1m -> s = r * theta (in rad)
        if (arcValEl) {
          var s = 1.0 * Math.abs(baseRad);
          if (s >= 1000) {
            arcValEl.textContent = (s / 1000).toFixed(3) + " km";
          } else if (s >= 1) {
            arcValEl.textContent = s.toFixed(4) + " m";
          } else {
            arcValEl.textContent = (s * 100).toFixed(2) + " cm";
          }
        }

        // Lateral dispersion at 100 meters: 100 * tan(theta)
        if (disp100mEl) {
          // If theta is very small, 100 * baseRad
          var dispM = 100.0 * Math.abs(Math.tan(baseRad));
          if (dispM > 100000) {
            disp100mEl.textContent = "Inf / Undefined";
          } else if (dispM >= 1000) {
            disp100mEl.textContent = (dispM / 1000).toFixed(2) + " km";
          } else if (dispM >= 1) {
            disp100mEl.textContent = dispM.toFixed(3) + " m";
          } else {
            disp100mEl.textContent = (dispM * 100).toFixed(2) + " cm (" + (dispM * 39.3701).toFixed(2) + " in)";
          }
        }

        // Trig values
        if (trigValEl) {
          var sVal = Math.sin(baseRad);
          var cVal = Math.cos(baseRad);
          trigValEl.textContent = "sin: " + sVal.toFixed(3) + " | cos: " + cVal.toFixed(3);
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
with open(os.path.join(BASE_DIR, 'fuel-economy-converter.html'), 'w', encoding='utf-8') as f:
    f.write(fuel_html.strip() + '\n')
print("Generated fuel-economy-converter.html successfully!")

with open(os.path.join(BASE_DIR, 'angle-converter.html'), 'w', encoding='utf-8') as f:
    f.write(angle_html.strip() + '\n')
print("Generated angle-converter.html successfully!")
