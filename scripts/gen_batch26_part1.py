import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 1. DENSITY CONVERTER
# -------------------------------------------------------------
density_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Density Converter — kg/m³, g/cm³, lb/ft³, lb/gal, API Gravity | CalcHub</title>
  <meta name="description" content="Convert volumetric density and specific gravity across kg/m³, g/cm³, lb/ft³, lb/gal (US/UK), g/mL, and petroleum API Gravity with exact physical constants.">
  <meta name="keywords" content="density converter, kg/m3 to g/cm3, lb/ft3 to kg/m3, density of water, api gravity to specific gravity, lb/gal to kg/m3, hydrometer converter, specific gravity calculator">
  <meta name="author" content="CalcHub Fluid Mechanics & Petrochemical Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/density-converter.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="Density Converter — kg/m³, g/cm³, lb/ft³, lb/gal, API Gravity | CalcHub">
  <meta property="og:description" content="Convert volumetric density and specific gravity across kg/m³, g/cm³, lb/ft³, lb/gal (US/UK), g/mL, and petroleum API Gravity with exact physical constants.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/density-converter.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/density-converter.html#app",
      "name": "Precision Volumetric Density & Specific Gravity Converter",
      "url": "https://calchub.org/density-converter.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Metrological density conversion engine translating between SI metric (kg/m³, g/cm³, g/mL), imperial engineering (lb/ft³, lb/in³, lb/gal), and petroleum API gravity."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Universal Unit Converters", "item": "https://calchub.org/converter.html"},
        {"@type": "ListItem", "position": 3, "name": "Density Converter", "item": "https://calchub.org/density-converter.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the relationship between mass density and specific gravity (relative density)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Mass density (ρ) is the mass of a substance per unit volume (e.g., kg/m³ or lb/ft³). Specific gravity (SG), also termed relative density, is a dimensionless ratio comparing the density of a substance to the density of pure deaerated water at its maximum density temperature of 3.98°C (1,000 kg/m³ or 62.428 lb/ft³): SG = ρ_substance / ρ_water. Because SG is dimensionless, an oil with an SG of 0.85 has a density of 850 kg/m³ or 0.85 g/cm³."
          }
        },
        {
          "@type": "Question",
          "name": "How is American Petroleum Institute (API) Gravity calculated from Specific Gravity?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The American Petroleum Institute defines API Gravity by the inverse formula: API = (141.5 / SG @ 60°F) - 131.5. Rearranging for specific gravity yields SG @ 60°F = 141.5 / (API + 131.5). Water has an SG of 1.0, corresponding to an API gravity of 10°. Crude oils lighter than water have API gravities greater than 10° (e.g., West Texas Intermediate crude is ~39.6° API, corresponding to an SG of ~0.827)."
          }
        },
        {
          "@type": "Question",
          "name": "Why does temperature alter the volumetric density of liquids and gases?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Thermal expansion causes molecules to vibrate more energetically and increase their intermolecular spacing as temperature increases, causing volume to expand while mass remains constant. By ρ = m / V, density decreases with rising temperature according to the volumetric thermal expansion coefficient β: ρ(T) ≈ ρ_0 / (1 + βΔT). For gases, density also varies linearly with absolute pressure via the Ideal Gas Law: ρ = (P · M) / (R · T)."
          }
        },
        {
          "@type": "Question",
          "name": "How does 1 gram per cubic centimeter (g/cm³) relate to kilograms per cubic meter (kg/m³)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "One gram is 10⁻³ kg and one cubic centimeter is (10⁻² m)³ = 10⁻⁶ m³. Therefore, 1 g/cm³ = 10⁻³ kg / 10⁻⁶ m³ = 1,000 kg/m³. Water at 4°C has a density of exactly 1.000 g/cm³, 1.000 g/mL, or 1,000 kg/m³."
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
            <span>Density Converter</span>
          </div>
          <span class="badge">Fluid Dynamics, Materials &amp; Petrochemical</span>
          <h1>Precision Density Converter</h1>
          <p class="tagline">Convert between mass density units (kg/m³, g/cm³, lb/ft³, lb/gal) and specific gravity with exact international physical constants.</p>
        </div>

        <div class="calculator-container card-surface">
          <div class="converter-box">
            <div class="converter-inputs-grid">
              <div class="input-col">
                <label for="densityFromVal" class="input-label">From Value</label>
                <input type="number" id="densityFromVal" class="converter-num-input" value="1000" step="any" placeholder="Enter density">
                <label for="densityFromUnit" class="input-label sub-label">From Unit</label>
                <select id="densityFromUnit" class="converter-select">
                  <option value="kg_m3" selected>Kilograms / m³ (kg/m³)</option>
                  <option value="g_cm3">Grams / cm³ (g/cm³)</option>
                  <option value="g_ml">Grams / mL (g/mL)</option>
                  <option value="lb_ft3">Pounds / ft³ (lb/ft³)</option>
                  <option value="lb_in3">Pounds / in³ (lb/in³)</option>
                  <option value="lb_gal_us">Pounds / Gallon (US lb/gal)</option>
                  <option value="lb_gal_uk">Pounds / Gallon (UK lb/gal)</option>
                  <option value="sg">Specific Gravity (SG vs water)</option>
                  <option value="api">API Gravity (°API)</option>
                </select>
              </div>

              <div class="swap-col">
                <button type="button" id="densitySwapBtn" class="swap-button" title="Swap input and output units" aria-label="Swap units">
                  &#8644;
                </button>
              </div>

              <div class="input-col">
                <label for="densityToVal" class="input-label">Converted Value</label>
                <input type="text" id="densityToVal" class="converter-num-input output-val" readonly value="62.428">
                <label for="densityToUnit" class="input-label sub-label">To Unit</label>
                <select id="densityToUnit" class="converter-select">
                  <option value="kg_m3">Kilograms / m³ (kg/m³)</option>
                  <option value="g_cm3">Grams / cm³ (g/cm³)</option>
                  <option value="g_ml">Grams / mL (g/mL)</option>
                  <option value="lb_ft3" selected>Pounds / ft³ (lb/ft³)</option>
                  <option value="lb_in3">Pounds / in³ (lb/in³)</option>
                  <option value="lb_gal_us">Pounds / Gallon (US lb/gal)</option>
                  <option value="lb_gal_uk">Pounds / Gallon (UK lb/gal)</option>
                  <option value="sg">Specific Gravity (SG vs water)</option>
                  <option value="api">API Gravity (°API)</option>
                </select>
              </div>
            </div>

            <div class="converter-quick-presets">
              <span class="preset-label">Standard Material Reference Benchmarks:</span>
              <button type="button" class="preset-chip" data-val="1000" data-from="kg_m3" data-to="lb_ft3">Pure Water (1000 kg/m³ = 62.43 lb/ft³)</button>
              <button type="button" class="preset-chip" data-val="7850" data-from="kg_m3" data-to="lb_in3">Structural Steel (7850 kg/m³ = 0.284 lb/in³)</button>
              <button type="button" class="preset-chip" data-val="39.6" data-from="api" data-to="kg_m3">WTI Crude Oil (39.6° API = 827 kg/m³)</button>
              <button type="button" class="preset-chip" data-val="1.225" data-from="kg_m3" data-to="lb_ft3">Sea Level Air (1.225 kg/m³ = 0.0765 lb/ft³)</button>
            </div>

            <div class="conversion-summary-panel" id="densitySummaryCard">
              <div class="summary-line">
                <span class="summary-label">Direct Relation:</span>
                <span class="summary-formula" id="densityEquation">1,000 kg/m³ = 62.428 lb/ft³</span>
              </div>
              <div class="summary-submetrics">
                <div class="submetric-item">
                  <span class="submetric-name">Specific Gravity (SG):</span>
                  <span class="submetric-val" id="densitySgVal">1.000</span>
                </div>
                <div class="submetric-item">
                  <span class="submetric-name">Equivalent API Gravity:</span>
                  <span class="submetric-val" id="densityApiVal">10.0° API</span>
                </div>
                <div class="submetric-item">
                  <span class="submetric-name">Mass of 1 US Gallon:</span>
                  <span class="submetric-val" id="densityGalWeight">8.345 lbs (3.785 kg)</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <section>
            <h2>Physical Foundations of Mass Density &amp; Specific Gravity</h2>
            <p>
              Density is a fundamental intensive property of matter defined as the mass of a substance contained within a unit volume:
            </p>
            <p>
              $$\rho = \frac{m}{V}$$
            </p>
            <p>
              Where \(\rho\) (rho) represents density, \(m\) is mass, and \(V\) is volume. In the International System of Units (SI), the derived unit of density is the <strong>kilogram per cubic meter (\(\text{kg/m}^3\))</strong>. Because solid and liquid materials often have high concentrations of mass in compact volumes, laboratory chemistry routinely utilizes the decimal sub-multiple <strong>gram per cubic centimeter (\(\text{g/cm}^3\))</strong> or <strong>gram per milliliter (\(\text{g/mL}\))</strong>, which are numerically identical:
            </p>
            <p>
              $$1\text{ g/cm}^3 = 1\text{ g/mL} = 1,000\text{ kg/m}^3$$
            </p>
            <p>
              In US Customary and British Imperial engineering, structural engineers, hydrologists, and naval architects quantify density using <strong>pounds per cubic foot (\(\text{lb/ft}^3\))</strong>, <strong>pounds per cubic inch (\(\text{lb/in}^3\))</strong>, and <strong>pounds per gallon (\(\text{lb/gal}\))</strong>. Precise translation between these systems is essential in geotechnical soil mechanics, aerospace structural sizing, pipeline hydraulics, and petroleum refining.
            </p>
          </section>

          <section>
            <h2>Exact Mathematical Conversion Multipliers &amp; Governing Equations</h2>
            <p>
              Density conversions depend on the standardized mass definitions established by the BIPM (Bureau International des Poids et Mesures) and NIST SP 811:
            </p>
            <ul>
              <li>\(1\text{ Pound (avoirdupois)} \equiv 0.45359237\text{ Kilograms}\)</li>
              <li>\(1\text{ Foot} \equiv 0.3048\text{ Meters} \implies 1\text{ ft}^3 \equiv 0.028316846592\text{ m}^3\)</li>
              <li>\(1\text{ Inch} \equiv 0.0254\text{ Meters} \implies 1\text{ in}^3 \equiv 0.000016387064\text{ m}^3\)</li>
              <li>\(1\text{ US Liquid Gallon} \equiv 231\text{ in}^3 \equiv 0.003785411784\text{ m}^3\)</li>
              <li>\(1\text{ UK Imperial Gallon} \equiv 4.54609\text{ Liters} = 0.00454609\text{ m}^3\)</li>
            </ul>

            <div class="formula-card">
              <h3>Analytical Density Formulas</h3>
              <p>$$\text{Base SI Metric: } 1\text{ kg/m}^3 = 0.001\text{ g/cm}^3 = 0.06242796\text{ lb/ft}^3$$</p>
              <p>$$\text{Pounds per Cubic Foot to kg/m³: } 1\text{ lb/ft}^3 = \frac{0.45359237}{0.028316846592}\text{ kg/m}^3 \approx 16.018463\text{ kg/m}^3$$</p>
              <p>$$\text{Pounds per Cubic Inch: } 1\text{ lb/in}^3 = 1,728\text{ lb/ft}^3 \approx 27,679.9047\text{ kg/m}^3$$</p>
              <p>$$\text{US Pounds per Gallon: } 1\text{ lb/gal}_{\text{US}} = \frac{0.45359237}{0.003785411784}\text{ kg/m}^3 \approx 119.826427\text{ kg/m}^3$$</p>
              <p>$$\text{UK Pounds per Gallon: } 1\text{ lb/gal}_{\text{UK}} = \frac{0.45359237}{0.00454609}\text{ kg/m}^3 \approx 99.776372\text{ kg/m}^3$$</p>
              <p>$$\text{Specific Gravity: } \text{SG} = \frac{\rho_{\text{sample}}}{\rho_{\text{water @ 4°C}}} = \frac{\rho_{\text{sample}}}{1,000\text{ kg/m}^3} = \frac{\rho_{\text{sample}}}{62.42796\text{ lb/ft}^3}$$</p>
              <p>$$\text{API Gravity Formula: } ^\circ\text{API} = \frac{141.5}{\text{SG @ 60°F}} - 131.5 \iff \text{SG} = \frac{141.5}{^\circ\text{API} + 131.5}$$</p>
            </div>
          </section>

          <section>
            <h2>Petroleum Hydrometry &amp; The API Gravity Standard</h2>
            <p>
              In the international crude oil and gas trading markets, liquid petroleum is evaluated based on <strong>API Gravity</strong>, an inverse hydrometer scale developed jointly by the American Petroleum Institute and the National Bureau of Standards.
            </p>
            <p>
              Because oil is less dense than water, lighter oils have higher API gravities. The scale is calibrated such that pure water at 60°F (15.56°C) has an API gravity of exactly 10.0°:
            </p>
            <ul>
              <li><strong>Light Crude Oil (API &gt; 31.1°):</strong> Examples include Brent Crude (~38.3° API) and West Texas Intermediate (WTI, ~39.6° API). Highly prized by refineries because it yields large fractions of high-value gasoline and aviation jet fuel with low refining energy.</li>
              <li><strong>Medium Crude Oil (22.3° &le; API &le; 31.1°):</strong> Moderate viscosity crude oils typical of Persian Gulf and Russian Urals grades.</li>
              <li><strong>Heavy Crude Oil (10.0° &le; API &le; 22.3°):</strong> Dense crude oils that require heated transport and cracking units to produce lighter fractions.</li>
              <li><strong>Extra Heavy Crude / Bitumen (API &lt; 10.0°):</strong> Denser than water (\(\text{SG} > 1.0\)), sinking rather than floating if spilled. Found in the Canadian Athabasca oil sands and Venezuelan Orinoco belt, requiring dilution with natural gas condensate for pipeline pumping.</li>
            </ul>
          </section>

          <section>
            <h2>Comparative Material Density Benchmark Matrix</h2>
            <p>
              The multi-column engineering matrix below compares representative solids, liquids, and gases across metric, imperial, and specific gravity units at standard reference temperature (20°C / 68°F and 1 atm unless otherwise noted):
            </p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>Material / Substance</th>
                  <th>Density (\(\text{kg/m}^3\))</th>
                  <th>Density (\(\text{g/cm}^3\))</th>
                  <th>Imperial (\(\text{lb/ft}^3\))</th>
                  <th>Imperial (\(\text{lb/in}^3\))</th>
                  <th>Specific Gravity (SG)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Air (Dry at Sea Level, 15°C)</strong></td>
                  <td>1.225</td>
                  <td>0.001225</td>
                  <td>0.07647</td>
                  <td>0.000044</td>
                  <td>0.00123</td>
                </tr>
                <tr>
                  <td><strong>Gasoline (Octane, typical)</strong></td>
                  <td>740</td>
                  <td>0.740</td>
                  <td>46.20</td>
                  <td>0.0267</td>
                  <td>0.740 (59.7° API)</td>
                </tr>
                <tr>
                  <td><strong>Pure Water (at 3.98°C max)</strong></td>
                  <td>1,000</td>
                  <td>1.000</td>
                  <td>62.43</td>
                  <td>0.0361</td>
                  <td>1.000 (10.0° API)</td>
                </tr>
                <tr>
                  <td><strong>Seawater (35 ppt salinity)</strong></td>
                  <td>1,025</td>
                  <td>1.025</td>
                  <td>63.99</td>
                  <td>0.0370</td>
                  <td>1.025</td>
                </tr>
                <tr>
                  <td><strong>Portland Concrete (Reinforced)</strong></td>
                  <td>2,400</td>
                  <td>2.400</td>
                  <td>149.83</td>
                  <td>0.0867</td>
                  <td>2.400</td>
                </tr>
                <tr>
                  <td><strong>Structural Aluminum (6061-T6)</strong></td>
                  <td>2,700</td>
                  <td>2.700</td>
                  <td>168.56</td>
                  <td>0.0975</td>
                  <td>2.700</td>
                </tr>
                <tr>
                  <td><strong>Titanium (Grade 5 Ti-6Al-4V)</strong></td>
                  <td>4,430</td>
                  <td>4.430</td>
                  <td>276.55</td>
                  <td>0.1600</td>
                  <td>4.430</td>
                </tr>
                <tr>
                  <td><strong>Structural Carbon Steel (A36)</strong></td>
                  <td>7,850</td>
                  <td>7.850</td>
                  <td>490.06</td>
                  <td>0.2836</td>
                  <td>7.850</td>
                </tr>
                <tr>
                  <td><strong>Pure Copper (C11000 ETP)</strong></td>
                  <td>8,940</td>
                  <td>8.940</td>
                  <td>558.10</td>
                  <td>0.3230</td>
                  <td>8.940</td>
                </tr>
                <tr>
                  <td><strong>Liquid Mercury (at 20°C)</strong></td>
                  <td>13,546</td>
                  <td>13.546</td>
                  <td>845.65</td>
                  <td>0.4894</td>
                  <td>13.546</td>
                </tr>
                <tr>
                  <td><strong>Pure Gold (24 Karat)</strong></td>
                  <td>19,320</td>
                  <td>19.320</td>
                  <td>1,206.11</td>
                  <td>0.6980</td>
                  <td>19.320</td>
                </tr>
              </tbody>
            </table>
          </section>

          <section>
            <h2>Worked Engineering Case Study: Offshore Oil Storage Tank Tonnage Audit</h2>
            <div class="worked-example-card">
              <h3>Engineering Scenario: Crude Oil Volume-to-Mass Cargo Verification</h3>
              <p>
                An offshore production platform is pumping crude oil into a Floating Production Storage and Offloading (FPSO) vessel cargo tank. The petroleum laboratory measures the oil quality at <strong>34.0° API</strong> at the standard reference temperature of 60°F. The custody transfer ultrasonic meter records a delivered gross volume of <strong>250,000 Barrels (bbl)</strong>.
              </p>
              <p>The cargo surveyor must calculate:</p>
              <ol>
                <li>The specific gravity (SG) of the crude oil at 60°F.</li>
                <li>The oil density in kilograms per cubic meter (\(\text{kg/m}^3\)) and pounds per US gallon (\(\text{lb/gal}\)).</li>
                <li>The total metric tonnes of crude loaded into the vessel (1 barrel = 42 US gallons = 0.1589873 m³).</li>
                <li>The displacement draft impact in long tons (2,240 lbs).</li>
              </ol>

              <h4>Step-by-Step Calculation:</h4>
              <p><strong>1. Specific Gravity from API Gravity:</strong></p>
              <p>$$\text{SG} = \frac{141.5}{^\circ\text{API} + 131.5} = \frac{141.5}{34.0 + 131.5} = \frac{141.5}{165.5} \approx \mathbf{0.854985}$$</p>

              <p><strong>2. Density in kg/m³ and lb/gal:</strong></p>
              <p>$$\rho_{\text{kg/m}^3} = \text{SG} \times 1,000\text{ kg/m}^3 = 0.854985 \times 1,000 = \mathbf{854.985\text{ kg/m}^3}$$</p>
              <p>$$\rho_{\text{lb/gal}} = \text{SG} \times 8.345404\text{ lb/gal} = 0.854985 \times 8.345404 \approx \mathbf{7.135\text{ lb/gal}}$$</p>

              <p><strong>3. Total Metric Tonnes Loaded:</strong></p>
              <p>$$\text{Total Volume in m}^3 = 250,000\text{ bbl} \times 0.158987295\text{ m}^3\text{/bbl} = 39,746.82\text{ m}^3$$</p>
              <p>$$\text{Total Mass} = 39,746.82\text{ m}^3 \times 854.985\text{ kg/m}^3 = 33,982,936\text{ kg} = \mathbf{33,982.94\text{ metric tonnes}}$$</p>

              <p><strong>4. Vessel Displacement in Long Tons:</strong></p>
              <p>$$\text{Mass in Pounds} = 33,982,936\text{ kg} \times 2.20462262\text{ lb/kg} = 74,919,550\text{ lbs}$$</p>
              <p>$$\text{Long Tons} = \frac{74,919,550}{2,240} \approx \mathbf{33,446.23\text{ long tons}}$$</p>

              <p>
                <strong>Surveyor Verification:</strong> The 250,000 bbl cargo parcel adds 33,982.9 metric tonnes of deadweight displacement, ensuring accurate stability ballast adjustment and bills of lading.
              </p>
            </div>
          </section>

          <section class="faq-section">
            <h2>Frequently Asked Questions Regarding Volumetric Density</h2>
            <div class="faq-item">
              <h3>What is the difference between bulk density and particle (true) density?</h3>
              <p><strong>True (particle) density</strong> is the mass of the solid particles divided by the volume of the particles themselves, excluding all voids and pore spaces between them. <strong>Bulk density</strong> is the mass of many particles divided by the total volume they occupy, including the internal pore volume and inter-particle void spaces. For example, solid silica quartz has a particle density of 2,650 kg/m³, but loose dry sand has a bulk density of only 1,500 to 1,650 kg/m³ due to air voids.</p>
            </div>
            <div class="faq-item">
              <h3>Why does water expand and become less dense when freezing into ice?</h3>
              <p>Unlike almost all other liquids which become denser upon freezing, water exhibits an anomalous density peak at 3.98°C (1,000 kg/m³). Below 4°C, hydrogen bonding between polar H₂O molecules forces them into an open hexagonal crystalline lattice structure. This lattice holds molecules farther apart than the disordered liquid state, causing ice at 0°C to have a density of only 917 kg/m³. Because ice is ~8.3% less dense than water, ice floats on lakes and protects aquatic ecosystems from freezing solid.</p>
            </div>
            <div class="faq-item">
              <h3>How does a digital Coriolis mass flow meter measure fluid density?</h3>
              <p>A Coriolis flow meter vibrates measuring tubes at their natural resonant frequency. When fluid flows through the vibrating tube, the resonant frequency of oscillation shifts inversely with the mass of the vibrating assembly: \(f = \frac{1}{2\pi}\sqrt{\frac{k}{m_{\text{tube}} + \rho_{\text{fluid}} V}}\). By continuously detecting the resonant frequency shift, the electronics compute fluid density in real time with accuracy up to 0.0005 g/cm³.</p>
            </div>
            <div class="faq-item">
              <h3>What is the Baumé scale and how does it compare to Specific Gravity?</h3>
              <p>The Baumé scale (°Bé) is an older hydrometer scale used in brewing, winemaking, battery acid testing, and industrial chemical manufacturing. For liquids heavier than water: \(^\circ\text{Bé} = 145 - (145 / \text{SG})\). For liquids lighter than water: \(^\circ\text{Bé} = (140 / \text{SG}) - 130\). Pure water is 0° Bé on the heavy scale and 10° Bé on the light scale.</p>
            </div>
          </section>
        </article>
      </div>

      <aside class="converter-sidebar">
        <div class="sidebar-card">
          <h3>Related Fluid &amp; Mass Converters</h3>
          <ul class="sidebar-links">
            <li><a href="weight-converter.html">Weight & Mass Converter (kg, lbs, tons)</a></li>
            <li><a href="volume-converter.html">Volume Converter (liters, gallons, m³)</a></li>
            <li><a href="flow-rate-converter.html">Flow Rate Converter (GPM, L/min, m³/h)</a></li>
            <li><a href="pressure-converter.html">Pressure Converter (psi, bar, kPa)</a></li>
            <li><a href="temperature-converter.html">Temperature Converter (°C, °F, K)</a></li>
            <li><a href="viscosity-converter.html">Viscosity Converter (cP, cSt, Pa·s)</a></li>
            <li><a href="force-converter.html">Force Converter (N, lbf, kN)</a></li>
            <li><a href="energy-converter.html">Energy Converter (Joules, kWh)</a></li>
          </ul>
        </div>
        <div class="sidebar-card">
          <h3>Rule of Thumb: Water Density</h3>
          <p class="sidebar-tip">
            Remember the classic practical water density constants:<br><br>
            &bull; <strong>1.000 g/cm³</strong> (or 1.000 g/mL)<br>
            &bull; <strong>1,000 kg/m³</strong><br>
            &bull; <strong>62.43 lb/ft³</strong><br>
            &bull; <strong>8.345 lb/gal (US)</strong><br>
            &bull; <strong>10.00 lb/gal (UK)</strong>
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
      // Base unit: kg/m^3
      var factors = {
        kg_m3: 1.0,
        g_cm3: 1000.0,
        g_ml: 1000.0,
        lb_ft3: 16.01846337,
        lb_in3: 27679.90471,
        lb_gal_us: 119.8264273,
        lb_gal_uk: 99.77637266,
        sg: 1000.0
      };

      var unitLabels = {
        kg_m3: 'kg/m³',
        g_cm3: 'g/cm³',
        g_ml: 'g/mL',
        lb_ft3: 'lb/ft³',
        lb_in3: 'lb/in³',
        lb_gal_us: 'US lb/gal',
        lb_gal_uk: 'UK lb/gal',
        sg: 'SG',
        api: '°API'
      };

      function toBaseKgM3(val, unit) {
        if (unit === 'api') {
          // API = 141.5 / SG - 131.5 -> SG = 141.5 / (API + 131.5)
          if (val <= -131.5) return 0;
          var sg = 141.5 / (val + 131.5);
          return sg * 1000.0;
        }
        return val * factors[unit];
      }

      function fromBaseKgM3(kgM3, unit) {
        if (unit === 'api') {
          var sg = kgM3 / 1000.0;
          if (sg <= 0) return 0;
          return (141.5 / sg) - 131.5;
        }
        return kgM3 / factors[unit];
      }

      var fromInput = document.getElementById('densityFromVal');
      var fromSelect = document.getElementById('densityFromUnit');
      var toInput = document.getElementById('densityToVal');
      var toSelect = document.getElementById('densityToUnit');
      var swapBtn = document.getElementById('densitySwapBtn');

      var equationEl = document.getElementById('densityEquation');
      var sgEl = document.getElementById('densitySgVal');
      var apiEl = document.getElementById('densityApiVal');
      var galWeightEl = document.getElementById('densityGalWeight');

      function calculate() {
        var val = parseFloat(fromInput.value);
        if (isNaN(val)) {
          toInput.value = '';
          return;
        }

        var fromUnit = fromSelect.value;
        var toUnit = toSelect.value;

        var baseKgM3 = toBaseKgM3(val, fromUnit);
        var result = fromBaseKgM3(baseKgM3, toUnit);

        if (Math.abs(result) >= 1e7 || (Math.abs(result) < 1e-4 && result !== 0)) {
          toInput.value = result.toExponential(5);
        } else {
          toInput.value = parseFloat(result.toPrecision(6)).toString();
        }

        if (equationEl) {
          equationEl.textContent = val + " " + unitLabels[fromUnit] + " = " + toInput.value + " " + unitLabels[toUnit];
        }

        if (sgEl) {
          var sgVal = baseKgM3 / 1000.0;
          sgEl.textContent = sgVal.toFixed(4);
        }

        if (apiEl) {
          var sgVal = baseKgM3 / 1000.0;
          if (sgVal > 0) {
            var apiVal = (141.5 / sgVal) - 131.5;
            apiEl.textContent = apiVal.toFixed(1) + "° API";
          } else {
            apiEl.textContent = "N/A";
          }
        }

        if (galWeightEl) {
          var lbPerGal = baseKgM3 / 119.8264273;
          var kgPerGal = lbPerGal * 0.45359237;
          galWeightEl.textContent = lbPerGal.toFixed(3) + " lbs (" + kgPerGal.toFixed(3) + " kg)";
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
# 2. ILLUMINANCE CONVERTER
# -------------------------------------------------------------
illuminance_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Illuminance Converter — Lux, Foot-Candles, Phot, Nox | CalcHub</title>
  <meta name="description" content="Convert light illuminance and luminous flux density between Lux (lx), Foot-Candles (fc), Phot (ph), and Nox with OSHA and IESNA lighting design standards.">
  <meta name="keywords" content="illuminance converter, lux to foot-candles, fc to lux, phot to lux, light level converter, lumen per square meter, inverse square law light, osha lighting requirements, iesna illuminance">
  <meta name="author" content="CalcHub Optical Physics & Architectural Lighting Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/illuminance-converter.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="Illuminance Converter — Lux, Foot-Candles, Phot, Nox | CalcHub">
  <meta property="og:description" content="Convert light illuminance and luminous flux density between Lux (lx), Foot-Candles (fc), Phot (ph), and Nox with OSHA and IESNA lighting design standards.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/illuminance-converter.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/illuminance-converter.html#app",
      "name": "Precision Optical Illuminance Converter",
      "url": "https://calchub.org/illuminance-converter.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Professional photometric illuminance converter translating between Lux, Foot-Candles, Phot, and Nox adhering to CIE and IESNA optical standards."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Universal Unit Converters", "item": "https://calchub.org/converter.html"},
        {"@type": "ListItem", "position": 3, "name": "Illuminance Converter", "item": "https://calchub.org/illuminance-converter.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the exact conversion between Lux (lx) and Foot-Candles (fc)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "One Lux is defined as one lumen per square meter (1 lm/m²), whereas one Foot-Candle is defined as one lumen per square foot (1 lm/ft²). Because 1 international foot equals 0.3048 meters, 1 square foot equals (0.3048)² = 0.09290304 square meters. Therefore, 1 Foot-Candle = 1 / 0.09290304 ≈ 10.76391 Lux. Conversely, 1 Lux ≈ 0.092903 Foot-Candles. For rapid mental approximation in architectural design, engineers frequently multiply foot-candles by 10 to obtain lux."
          }
        },
        {
          "@type": "Question",
          "name": "What is the difference between Illuminance (Lux) and Luminance (cd/m²)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Illuminance (measured in Lux or Foot-Candles) quantifies the total luminous flux incident upon a given surface area from external light sources—it measures the light falling onto an object. Luminance (measured in candelas per square meter, cd/m² or nits) quantifies the luminous intensity emitted or reflected by a surface in a given direction toward an observer's eyes—it measures surface brightness as perceived by human vision."
          }
        },
        {
          "@type": "Question",
          "name": "How does the Inverse Square Law govern light illuminance over distance?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "From a point light source of luminous intensity I (measured in candelas), illuminance E on a perpendicular surface at distance d follows E = I / d². Because the surface area of a sphere scales with the square of radius (4πr²), doubling the distance from a light source reduces surface illuminance to one-fourth (25%) of its original value. Tripling the distance reduces illuminance to one-ninth (~11.1%)."
          }
        },
        {
          "@type": "Question",
          "name": "What are the recommended OSHA and IESNA illuminance levels for commercial work spaces?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "OSHA Standard 1926.56 mandates minimum safety illumination: 5 foot-candles (54 lux) for general construction and warehouse corridors; 10 foot-candles (108 lux) for manufacturing shops and mechanical rooms; and 30 foot-candles (323 lux) for field offices. The Illuminating Engineering Society (IESNA) recommends 300 to 500 lux (30 to 50 fc) for commercial office desk work and 1,000 to 2,000 lux (100 to 200 fc) for high-precision electronics assembly and medical operating suites."
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
            <span>Illuminance Converter</span>
          </div>
          <span class="badge">Photometry, Architecture &amp; Optics</span>
          <h1>Precision Illuminance Converter</h1>
          <p class="tagline">Convert between light level units (Lux, Foot-Candles, Phot, Nox) adhering to CIE photometric observer curves and IESNA standards.</p>
        </div>

        <div class="calculator-container card-surface">
          <div class="converter-box">
            <div class="converter-inputs-grid">
              <div class="input-col">
                <label for="illumFromVal" class="input-label">From Value</label>
                <input type="number" id="illumFromVal" class="converter-num-input" value="500" step="any" placeholder="Enter illuminance">
                <label for="illumFromUnit" class="input-label sub-label">From Unit</label>
                <select id="illumFromUnit" class="converter-select">
                  <option value="lux" selected>Lux (lx = lm/m²)</option>
                  <option value="fc">Foot-Candles (fc = lm/ft²)</option>
                  <option value="phot">Phot (ph = lm/cm²)</option>
                  <option value="nox">Nox (nx = 10⁻³ lx)</option>
                  <option value="flx">Flame / Foot-Candle</option>
                </select>
              </div>

              <div class="swap-col">
                <button type="button" id="illumSwapBtn" class="swap-button" title="Swap input and output units" aria-label="Swap units">
                  &#8644;
                </button>
              </div>

              <div class="input-col">
                <label for="illumToVal" class="input-label">Converted Value</label>
                <input type="text" id="illumToVal" class="converter-num-input output-val" readonly value="46.45">
                <label for="illumToUnit" class="input-label sub-label">To Unit</label>
                <select id="illumToUnit" class="converter-select">
                  <option value="lux">Lux (lx = lm/m²)</option>
                  <option value="fc" selected>Foot-Candles (fc = lm/ft²)</option>
                  <option value="phot">Phot (ph = lm/cm²)</option>
                  <option value="nox">Nox (nx = 10⁻³ lx)</option>
                  <option value="flx">Flame / Foot-Candle</option>
                </select>
              </div>
            </div>

            <div class="converter-quick-presets">
              <span class="preset-label">Standard Architectural Lighting Benchmarks:</span>
              <button type="button" class="preset-chip" data-val="50" data-from="fc" data-to="lux">Office Desk (50 fc = 538 lux)</button>
              <button type="button" class="preset-chip" data-val="1000" data-from="lux" data-to="fc">Surgery Suite (1,000 lux = 92.9 fc)</button>
              <button type="button" class="preset-chip" data-val="10000" data-from="lux" data-to="fc">Overcast Daylight (10,000 lux = 929 fc)</button>
              <button type="button" class="preset-chip" data-val="0.25" data-from="lux" data-to="nox">Full Moon (0.25 lux = 250 nox)</button>
            </div>

            <div class="conversion-summary-panel" id="illumSummaryCard">
              <div class="summary-line">
                <span class="summary-label">Direct Relation:</span>
                <span class="summary-formula" id="illumEquation">500 lx = 46.45 fc</span>
              </div>
              <div class="summary-submetrics">
                <div class="submetric-item">
                  <span class="submetric-name">Lumens on 10 m² Room:</span>
                  <span class="submetric-val" id="illumRoomLm">5,000 Lumens</span>
                </div>
                <div class="submetric-item">
                  <span class="submetric-name">Approx. LED Watts (100 lm/W):</span>
                  <span class="submetric-val" id="illumLedWatts">50.0 Watts</span>
                </div>
                <div class="submetric-item">
                  <span class="submetric-name">Lighting Application Class:</span>
                  <span class="submetric-val" id="illumAppClass">Commercial Office / Classrooms</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <section>
            <h2>Photometric Principles of Light Illuminance &amp; Luminous Flux Density</h2>
            <p>
              Illuminance measures the total amount of visible light emitted from surrounding fixtures or the sun that falls upon a given unit surface area. It is defined mathematically as the areal density of luminous flux:
            </p>
            <p>
              $$E = \frac{d\Phi_v}{dA}$$
            </p>
            <p>
              Where \(E\) is illuminance, \(\Phi_v\) is luminous flux measured in <strong>lumens (\(\text{lm}\))</strong>, and \(A\) is surface area. Luminous flux is distinguished from radiant flux (measured in raw electromagnetic watts) because it is weighted according to the spectral sensitivity of the human eye, standardized by the Commission Internationale de l'Éclairage (CIE) photopic luminosity function \(V(\lambda)\) which peaks at a yellowish-green wavelength of 555 nanometers.
            </p>
            <p>
              Across international architectural and optical engineering, two primary units dominate:
            </p>
            <ul>
              <li><strong>Lux (\(\text{lx}\)):</strong> The coherent SI unit of illuminance, defined as one lumen incident uniformly across one square meter (\(1\text{ lx} = 1\text{ lm/m}^2\)). Used across all metric territories, ISO standards, and European building codes (EN 12464).</li>
              <li><strong>Foot-Candle (\(\text{fc}\)):</strong> The foundational imperial unit utilized across North America and ANSI/IESNA standards, defined as one lumen incident uniformly across one square foot (\(1\text{ fc} = 1\text{ lm/ft}^2\)).</li>
            </ul>
          </section>

          <section>
            <h2>Exact Mathematical Conversion Multipliers &amp; The Inverse Square Law</h2>
            <p>
              Because the foot is legally defined as exactly 0.3048 meters, the conversion ratio between Lux and Foot-Candles is derived directly from the square of this spatial conversion:
            </p>
            <p>
              $$1\text{ ft} = 0.3048\text{ m} \implies 1\text{ ft}^2 = (0.3048)^2\text{ m}^2 = 0.09290304\text{ m}^2$$
            </p>

            <div class="formula-card">
              <h3>Core Photometric Illuminance Formulas</h3>
              <p>$$\text{Foot-Candle to Lux: } 1\text{ fc} = \frac{1\text{ lm}}{1\text{ ft}^2} = \frac{1\text{ lm}}{0.09290304\text{ m}^2} \approx 10.7639104\text{ lx}$$</p>
              <p>$$\text{Lux to Foot-Candle: } 1\text{ lx} = 0.09290304\text{ fc} \approx \frac{1}{10.76391}\text{ fc}$$</p>
              <p>$$\text{Phot (CGS Unit): } 1\text{ ph} \equiv 1\text{ lm/cm}^2 = 10,000\text{ lx} \approx 929.0304\text{ fc}$$</p>
              <p>$$\text{Nox (Low-Light Scotopic): } 1\text{ nx} \equiv 10^{-3}\text{ lx} = 0.001\text{ lx} \approx 0.0000929\text{ fc}$$</p>
              <p>$$\text{Point-Source Inverse Square Law: } E = \frac{I \cdot \cos(\theta)}{d^2}$$</p>
              <p>$$\text{Total Lumens Required: } \Phi_{\text{total}} = \frac{E \cdot A}{\text{CU} \cdot \text{LLF}}$$</p>
            </div>

            <p>
              In the Inverse Square Law formula, \(I\) is luminous intensity in candelas (\(\text{cd}\)), \(d\) is distance from the luminaire to the work surface, and \(\theta\) is the angle of incidence between the incident light ray and the surface normal vector (Lambert's Cosine Law). If light strikes a table at an angle of 30° from perpendicular, illuminance drops by a factor of \(\cos(30^\circ) \approx 0.866\).
            </p>
          </section>

          <section>
            <h2>Architectural Lighting Guidelines: IESNA &amp; OSHA Compliance</h2>
            <p>
              In workplace hygiene and commercial building design, adequate illumination prevents eyestrain, reduces industrial machine accidents, and maximizes worker productivity. The engineering table below outlines mandatory OSHA minimums and recommended IESNA (Illuminating Engineering Society of North America) design targets:
            </p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>Environment / Visual Task</th>
                  <th>Standard Foot-Candles (fc)</th>
                  <th>Equivalent Lux (lx)</th>
                  <th>Visual Demands &amp; Recommended Lighting Quality</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Emergency Egress &amp; Stairwells</strong></td>
                  <td>1 &ndash; 5 fc</td>
                  <td>10 &ndash; 50 lx</td>
                  <td>Minimum life safety lighting (NFPA 101), emergency backup paths</td>
                </tr>
                <tr>
                  <td><strong>Warehouses &amp; Loading Docks</strong></td>
                  <td>10 &ndash; 20 fc</td>
                  <td>100 &ndash; 200 lx</td>
                  <td>Large item storage, forklift navigation, rough material handling</td>
                </tr>
                <tr>
                  <td><strong>Heavy Industrial Workshops</strong></td>
                  <td>20 &ndash; 30 fc</td>
                  <td>200 &ndash; 300 lx</td>
                  <td>Machine operation, fabrication shops, carpentry, packaging</td>
                </tr>
                <tr>
                  <td><strong>Commercial Offices &amp; Classrooms</strong></td>
                  <td>30 &ndash; 50 fc</td>
                  <td>300 &ndash; 500 lx</td>
                  <td>Computer VDT screens, reading printed text, lecture halls</td>
                </tr>
                <tr>
                  <td><strong>Drafting &amp; Technical Laboratories</strong></td>
                  <td>50 &ndash; 100 fc</td>
                  <td>500 &ndash; 1,000 lx</td>
                  <td>Detailed CAD drafting, scientific inspection, quality control</td>
                </tr>
                <tr>
                  <td><strong>Electronics Micro-Soldering</strong></td>
                  <td>100 &ndash; 200 fc</td>
                  <td>1,000 &ndash; 2,000 lx</td>
                  <td>SMD PCB assembly, watchmaking, high-contrast fine inspection</td>
                </tr>
                <tr>
                  <td><strong>Hospital Operating Surgical Field</strong></td>
                  <td>1,000 &ndash; 2,000 fc</td>
                  <td>10,000 &ndash; 20,000 lx</td>
                  <td>Surgical cavity illumination with shadowless adjustable luminaires</td>
                </tr>
                <tr>
                  <td><strong>Direct Summer Noon Sunlight</strong></td>
                  <td>3,000 &ndash; 10,000 fc</td>
                  <td>32,000 &ndash; 100,000 lx</td>
                  <td>Natural solar illumination, outdoor daytime reference</td>
                </tr>
              </tbody>
            </table>
          </section>

          <section>
            <h2>Worked Engineering Case Study: Commercial Office Floor Lighting Layout</h2>
            <div class="worked-example-card">
              <h3>Engineering Scenario: Lumen Method Illuminance &amp; Luminaire Sizing</h3>
              <p>
                An electrical lighting designer is calculating the fixture layout for an open-plan engineering office measuring <strong>20 meters long by 15 meters wide</strong> (floor area \(A = 300\text{ m}^2 = 3,229.17\text{ ft}^2\)). The client specification requires an average maintained desk illuminance of <strong>50 Foot-Candles</strong> using modern 2x4 LED troffers delivering <strong>4,800 Lumens</strong> each.
              </p>
              <p>
                Engineering assumptions: Coefficient of Utilization (\(\text{CU}\)) = 0.65; Light Loss Factor (\(\text{LLF}\)) = 0.85 (accounting for lamp dirt depreciation and room surface degradation).
              </p>
              <p>The lighting designer must determine:</p>
              <ol>
                <li>The required illuminance target in metric Lux (\(\text{lx}\)).</li>
                <li>The total maintained raw luminous flux (\(\Phi_{\text{net}}\)) required on the desk task planes.</li>
                <li>The total lamp lumens (\(\Phi_{\text{gross}}\)) that must be emitted by the luminaires.</li>
                <li>The total number of 4,800-lumen LED troffer fixtures to install.</li>
              </ol>

              <h4>Step-by-Step Calculation:</h4>
              <p><strong>1. Convert Foot-Candles to Lux:</strong></p>
              <p>$$E = 50\text{ fc} \times 10.76391\text{ lx/fc} = 538.20\text{ Lux (lm/m}^2\text{)}$$</p>

              <p><strong>2. Net Luminous Flux Incident on Workplane:</strong></p>
              <p>$$\Phi_{\text{net}} = E \times A = 538.20\text{ lx} \times 300\text{ m}^2 = 161,460\text{ lumens}$$</p>

              <p><strong>3. Gross Fixture Lumens with Loss Factors:</strong></p>
              <p>$$\Phi_{\text{gross}} = \frac{\Phi_{\text{net}}}{\text{CU} \times \text{LLF}} = \frac{161,460}{0.65 \times 0.85} = \frac{161,460}{0.5525} \approx \mathbf{292,235\text{ lumens}}$$</p>

              <p><strong>4. Total Required LED Fixtures:</strong></p>
              <p>$$N = \frac{\Phi_{\text{gross}}}{\text{Lumens per Fixture}} = \frac{292,235}{4,800} = 60.88\text{ fixtures}$$</p>
              <p>Rounding up to establish a symmetric 7 &times; 9 grid yields <strong>63 luminaires</strong>.</p>

              <p>
                <strong>Design Verification:</strong> Installing 63 fixtures produces \(63 \times 4,800 \times 0.5525 / 300 = \mathbf{556.9\text{ Lux}} = \mathbf{51.7\text{ fc}}\), satisfying the 50 fc client design criteria while guaranteeing uniform luminance distribution.
              </p>
            </div>
          </section>

          <section class="faq-section">
            <h2>Frequently Asked Questions Regarding Light Units &amp; Photometry</h2>
            <div class="faq-item">
              <h3>Can illuminance meters (lux meters) measure LED lighting accurately?</h3>
              <p>Standard analog lux meters were historically calibrated for 2856K incandescent tungsten filament lamps. Because modern white LEDs produce distinct narrow spectral spikes (especially phosphor-converted blue pumps around 450 nm), inexpensive photodiode sensors without accurate cosine diffusion diffusers and precise \(V(\lambda)\) optical filters can produce errors between 8% and 20%. Architectural audits should utilize <strong>Class A or Class B photometric lux meters</strong> adhering to DIN 5032-7 standards.</p>
            </div>
            <div class="faq-item">
              <h3>What is the difference between photopic, scotopic, and mesopic illuminance?</h3>
              <p><strong>Photopic vision</strong> occurs under bright daylight or indoor lighting (&gt;3 lx), mediated by retinal cone photoreceptors with peak sensitivity at 555 nm. <strong>Scotopic vision</strong> occurs in darkness (&lt;0.01 lx), mediated by retinal rod cells with peak sensitivity shifted to 507 nm (Purkinje effect). <strong>Mesopic vision</strong> spans the intermediate dusk and nighttime streetlighting regime (0.01 to 3 lx), where both rods and cones contribute simultaneously to visual detection.</p>
            </div>
            <div class="faq-item">
              <h3>Why is the foot-candle still widely used in the United States?</h3>
              <p>The US lighting design, architectural, and electrical contracting sectors operate under ANSI/IESNA standards that have historically utilized imperial units (square feet, ceiling heights in feet, foot-candles). Because foot-candles produce convenient double-digit numbers for common tasks (e.g., 30 fc for circulation, 50 fc for offices, 100 fc for drafting), the scale remains deeply embedded in commercial blueprints and building specifications.</p>
            </div>
            <div class="faq-item">
              <h3>How does Color Rendering Index (CRI) affect perceived illuminance?</h3>
              <p>Color Rendering Index (CRI or \(R_a\)) measures how faithfully a light source reveals the true colors of objects compared to a natural blackbody reference. While CRI does not alter the physical illuminance value measured in lux, human observers perceive spaces illuminated by high-CRI light sources (&gt;90 CRI) as brighter, clearer, and more visually comfortable than lower-CRI sources of identical lux output due to enhanced chromatic contrast.</p>
            </div>
          </section>
        </article>
      </div>

      <aside class="converter-sidebar">
        <div class="sidebar-card">
          <h3>Related Optics &amp; Energy Tools</h3>
          <ul class="sidebar-links">
            <li><a href="energy-converter.html">Energy Converter (Joules, kWh)</a></li>
            <li><a href="power-converter.html">Power Converter (Watts, kW, HP)</a></li>
            <li><a href="frequency-converter.html">Frequency Converter (Hz, THz, rad/s)</a></li>
            <li><a href="area-converter.html">Area Converter (m², ft², acres)</a></li>
            <li><a href="length-converter.html">Length Converter (meters, feet, inches)</a></li>
            <li><a href="density-converter.html">Density Converter (kg/m³, lb/ft³)</a></li>
            <li><a href="temperature-converter.html">Temperature Converter (°C, °F, K)</a></li>
            <li><a href="speed-converter.html">Speed Converter (m/s, km/h)</a></li>
          </ul>
        </div>
        <div class="sidebar-card">
          <h3>Quick Lighting Rule of Thumb</h3>
          <p class="sidebar-tip">
            Need a rapid mental estimate between US and Metric lighting? Remember:
            <br><br>
            <strong>1 Foot-Candle &approx; 10 Lux</strong>
            <br><br>
            (Exactly: \(1\text{ fc} = 10.764\text{ lx}\)).
            <br>
            A 50 fc office desk equals approximately 500 lux!
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
      // Base unit: Lux (lx = lm/m^2)
      var factors = {
        lux: 1.0,
        fc: 10.7639104167,
        phot: 10000.0,
        nox: 0.001,
        flx: 10.7639104167
      };

      var unitLabels = {
        lux: 'lx',
        fc: 'fc',
        phot: 'ph',
        nox: 'nx',
        flx: 'flame'
      };

      var fromInput = document.getElementById('illumFromVal');
      var fromSelect = document.getElementById('illumFromUnit');
      var toInput = document.getElementById('illumToVal');
      var toSelect = document.getElementById('illumToUnit');
      var swapBtn = document.getElementById('illumSwapBtn');

      var equationEl = document.getElementById('illumEquation');
      var roomLmEl = document.getElementById('illumRoomLm');
      var ledWattsEl = document.getElementById('illumLedWatts');
      var appClassEl = document.getElementById('illumAppClass');

      function calculate() {
        var val = parseFloat(fromInput.value);
        if (isNaN(val)) {
          toInput.value = '';
          return;
        }

        var fromUnit = fromSelect.value;
        var toUnit = toSelect.value;

        // Base lux
        var baseLux = val * factors[fromUnit];
        var result = baseLux / factors[toUnit];

        if (Math.abs(result) >= 1e7 || (Math.abs(result) < 1e-4 && result !== 0)) {
          toInput.value = result.toExponential(5);
        } else {
          toInput.value = parseFloat(result.toPrecision(6)).toString();
        }

        if (equationEl) {
          equationEl.textContent = val + " " + unitLabels[fromUnit] + " = " + toInput.value + " " + unitLabels[toUnit];
        }

        // Submetrics: 10 m^2 room lumens = baseLux * 10
        if (roomLmEl) {
          var lm10 = baseLux * 10.0;
          roomLmEl.textContent = Math.round(lm10).toLocaleString() + " Lumens";
        }

        // Approx LED watts @ 100 lm/W for a 10 m^2 room
        if (ledWattsEl) {
          var watts = (baseLux * 10.0) / 100.0;
          ledWattsEl.textContent = watts.toFixed(1) + " Watts";
        }

        // App class description
        if (appClassEl) {
          if (baseLux < 50) {
            appClassEl.textContent = "Night Egress / Hallways (<50 lx)";
          } else if (baseLux < 200) {
            appClassEl.textContent = "Storage & Loading Docks (100-200 lx)";
          } else if (baseLux < 750) {
            appClassEl.textContent = "Offices & Classrooms (300-500 lx)";
          } else if (baseLux < 1500) {
            appClassEl.textContent = "Detailed Drafting & Labs (500-1,000 lx)";
          } else if (baseLux < 5000) {
            appClassEl.textContent = "High-Precision Soldering (1,000-2,000 lx)";
          } else {
            appClassEl.textContent = "Surgical / Direct Sunlight (>5,000 lx)";
          }
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
with open(os.path.join(BASE_DIR, 'density-converter.html'), 'w', encoding='utf-8') as f:
    f.write(density_html.strip() + '\n')
print("Generated density-converter.html successfully!")

with open(os.path.join(BASE_DIR, 'illuminance-converter.html'), 'w', encoding='utf-8') as f:
    f.write(illuminance_html.strip() + '\n')
print("Generated illuminance-converter.html successfully!")
