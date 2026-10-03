import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 3. THERMAL CONDUCTIVITY CONVERTER
# -------------------------------------------------------------
thermal_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Thermal Conductivity Converter — W/(m·K), BTU/(hr·ft·°F), k-value | CalcHub</title>
  <meta name="description" content="Convert thermal conductivity (k-value, lambda λ) across W/(m·K), BTU/(hr·ft·°F), BTU·in/(hr·ft²·°F), cal/(s·cm·°C), and kcal/(hr·m·°C) with heat transfer precision.">
  <meta name="keywords" content="thermal conductivity converter, w/mk to btu/hr-ft-f, k value to r value, thermal transmittance u-value, btu in/hr ft2 f to w/mk, fourier heat conduction, insulation conductivity">
  <meta name="author" content="CalcHub Thermodynamics & Heat Transfer Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/thermal-conductivity-converter.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="Thermal Conductivity Converter — W/(m·K), BTU/(hr·ft·°F), k-value | CalcHub">
  <meta property="og:description" content="Convert thermal conductivity (k-value, lambda λ) across W/(m·K), BTU/(hr·ft·°F), BTU·in/(hr·ft²·°F), cal/(s·cm·°C), and kcal/(hr·m·°C) with heat transfer precision.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/thermal-conductivity-converter.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/thermal-conductivity-converter.html#app",
      "name": "Precision Thermal Conductivity & Heat Transfer Converter",
      "url": "https://calchub.org/thermal-conductivity-converter.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Engineering thermal conductivity converter translating between SI metric W/(m·K), imperial BTU engineering units, and architectural R-value heat transfer parameters."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Universal Unit Converters", "item": "https://calchub.org/converter.html"},
        {"@type": "ListItem", "position": 3, "name": "Thermal Conductivity Converter", "item": "https://calchub.org/thermal-conductivity-converter.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the physical definition of thermal conductivity (k or λ)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Thermal conductivity (denoted k or λ) is an intrinsic material transport property quantifying the rate of heat energy transferred through a unit thickness of material per unit area per unit temperature gradient under steady-state conditions: k = q · L / (A · ΔT). In SI units, it is measured in Watts per meter-Kelvin [W/(m·K)]. Materials with high thermal conductivity (such as copper at ~400 W/m·K) are thermal conductors; materials with low conductivity (such as silica aerogel at ~0.015 W/m·K) are effective thermal insulators."
          }
        },
        {
          "@type": "Question",
          "name": "How does thermal conductivity relate to architectural R-value and U-value?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Thermal conductivity (k) is an intensive property independent of geometry, whereas R-value is an extensive thermal resistance property that depends directly on insulation thickness L: R = L / k. In metric units, RSI = L(meters) / k[W/(m·K)]. In US imperial units, R-value = L(inches) / (k[BTU·in/(hr·ft²·°F)]). The overall heat transfer coefficient (U-value or thermal transmittance) is simply the mathematical reciprocal of total thermal resistance: U = 1 / R_total."
          }
        },
        {
          "@type": "Question",
          "name": "What is the exact conversion factor between W/(m·K) and BTU/(hr·ft·°F)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "1 BTU/(hr·ft·°F) equals approximately 1.730735 W/(m·K). Conversely, 1 W/(m·K) = 0.577789 BTU/(hr·ft·°F). In the building trades, conductivity is often specified as BTU-inch per hour-square foot-degree Fahrenheit [BTU·in/(hr·ft²·°F)], where 1 W/(m·K) = 6.93347 BTU·in/(hr·ft²·°F)."
          }
        },
        {
          "@type": "Question",
          "name": "Why is diamond an exceptional thermal conductor despite being an electrical insulator?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In metals like copper and aluminum, heat is conducted primarily by free valence electrons. In diamond, heat conduction is mediated by quantized lattice vibrations called phonons. Diamond's rigid tetrahedral covalent sp³ crystal lattice of light carbon atoms creates extremely strong interatomic bonds and a very high Debye temperature (~2,220 K). This suppresses phonon-phonon scattering, enabling an extraordinary room-temperature thermal conductivity exceeding 2,000 W/(m·K)—five times higher than pure copper."
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
            <span>Thermal Conductivity Converter</span>
          </div>
          <span class="badge">Heat Transfer &amp; Materials Physics</span>
          <h1>Precision Thermal Conductivity Converter</h1>
          <p class="tagline">Convert thermal conductivity k-values between W/(m·K), BTU/(hr·ft·°F), BTU·in/(hr·ft²·°F), and cal/(s·cm·°C) with heat transfer precision.</p>
        </div>

        <div class="calculator-container card-surface">
          <div class="converter-box">
            <div class="converter-inputs-grid">
              <div class="input-col">
                <label for="tcFromVal" class="input-label">From Value</label>
                <input type="number" id="tcFromVal" class="converter-num-input" value="1" step="any" placeholder="Enter conductivity">
                <label for="tcFromUnit" class="input-label sub-label">From Unit</label>
                <select id="tcFromUnit" class="converter-select">
                  <option value="w_mk" selected>Watts / (m·K) [W/(m·K)]</option>
                  <option value="btu_hrftf">BTU / (hr·ft·°F)</option>
                  <option value="btu_in">BTU·in / (hr·ft²·°F)</option>
                  <option value="cal_scmc">cal / (s·cm·°C)</option>
                  <option value="kcal_hrmc">kcal / (hr·m·°C)</option>
                  <option value="w_cmk">Watts / (cm·K)</option>
                </select>
              </div>

              <div class="swap-col">
                <button type="button" id="tcSwapBtn" class="swap-button" title="Swap input and output units" aria-label="Swap units">
                  &#8644;
                </button>
              </div>

              <div class="input-col">
                <label for="tcToVal" class="input-label">Converted Value</label>
                <input type="text" id="tcToVal" class="converter-num-input output-val" readonly value="0.5778">
                <label for="tcToUnit" class="input-label sub-label">To Unit</label>
                <select id="tcToUnit" class="converter-select">
                  <option value="w_mk">Watts / (m·K) [W/(m·K)]</option>
                  <option value="btu_hrftf" selected>BTU / (hr·ft·°F)</option>
                  <option value="btu_in">BTU·in / (hr·ft²·°F)</option>
                  <option value="cal_scmc">cal / (s·cm·°C)</option>
                  <option value="kcal_hrmc">kcal / (hr·m·°C)</option>
                  <option value="w_cmk">Watts / (cm·K)</option>
                </select>
              </div>
            </div>

            <div class="converter-quick-presets">
              <span class="preset-label">Standard Material Benchmarks:</span>
              <button type="button" class="preset-chip" data-val="0.035" data-from="w_mk" data-to="btu_in">Fiberglass Batt (0.035 W/m·K = 0.243 BTU·in)</button>
              <button type="button" class="preset-chip" data-val="401" data-from="w_mk" data-to="btu_hrftf">Pure Copper (401 W/m·K = 231.7 BTU)</button>
              <button type="button" class="preset-chip" data-val="0.606" data-from="w_mk" data-to="btu_hrftf">Liquid Water @ 20°C (0.606 W/m·K)</button>
              <button type="button" class="preset-chip" data-val="2200" data-from="w_mk" data-to="btu_hrftf">CVD Diamond (2,200 W/m·K)</button>
            </div>

            <div class="conversion-summary-panel" id="tcSummaryCard">
              <div class="summary-line">
                <span class="summary-label">Direct Relation:</span>
                <span class="summary-formula" id="tcEquation">1 W/(m·K) = 0.5778 BTU/(hr·ft·°F)</span>
              </div>
              <div class="summary-submetrics">
                <div class="submetric-item">
                  <span class="submetric-name">R-Value per Inch Thickness:</span>
                  <span class="submetric-val" id="tcRPerInch">R-0.144 / inch</span>
                </div>
                <div class="submetric-item">
                  <span class="submetric-name">Metric RSI per 100mm:</span>
                  <span class="submetric-val" id="tcRsi100mm">RSI 0.100 m²·K/W</span>
                </div>
                <div class="submetric-item">
                  <span class="submetric-name">Thermal Regime:</span>
                  <span class="submetric-val" id="tcRegimeVal">Moderate Insulator / Building Material</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <section>
            <h2>Foundations of Thermal Conduction &amp; Fourier's Law</h2>
            <p>
              Thermal conductivity is an intrinsic physical transport property that quantifies a substance's capability to conduct thermal energy via molecular collision and microscopic electron/phonon propagation. Under Fourier's Law of One-Dimensional Heat Conduction, the conductive heat flux vector \(\vec{q}\) is directly proportional to the negative spatial temperature gradient:
            </p>
            <p>
              $$q = -k \cdot \frac{dT}{dx} \quad \implies \quad \dot{Q} = \frac{k \cdot A \cdot (T_{\text{hot}} - T_{\text{cold}})}{L}$$
            </p>
            <p>
              Where \(\dot{Q}\) is the total heat transfer rate in Watts (\(\text{W}\) or Joules/sec), \(k\) is thermal conductivity, \(A\) is the cross-sectional heat transfer area, and \(L\) is the material thickness.
            </p>
            <p>
              In the International System of Units (SI), thermal conductivity is measured in <strong>Watts per meter-Kelvin [\(\text{W/(m}\cdot\text{K)}\)]</strong>. Because temperature increments in Celsius and Kelvin are identical (\(\Delta 1^\circ\text{C} \equiv \Delta 1\text{ K}\)), the unit is numerically identical to \(\text{W/(m}\cdot^\circ\text{C)}\). In North American building engineering and refrigeration, heat transfer is traditionally quantified in British Thermal Units per hour-foot-degree Fahrenheit [\(\text{BTU/(hr}\cdot\text{ft}\cdot^\circ\text{F)}\)] or architectural inch-units [\(\text{BTU}\cdot\text{in/(hr}\cdot\text{ft}^2\cdot^\circ\text{F)}\)].
            </p>
          </section>

          <section>
            <h2>Exact Mathematical Conversion Multipliers &amp; Governing Equivalences</h2>
            <p>
              Translating between SI and Imperial conductivity units requires applying the fundamental physical definitions of energy, length, and thermodynamic temperature:
            </p>
            <ul>
              <li>\(1\text{ International Table BTU} \equiv 1,055.05585262\text{ Joules}\)</li>
              <li>\(1\text{ Hour} \equiv 3,600\text{ Seconds}\)</li>
              <li>\(1\text{ Foot} \equiv 0.3048\text{ Meters}\)</li>
              <li>\(\Delta 1^\circ\text{F} \equiv \frac{5}{9}\text{ K} \approx 0.5555556\text{ K}\)</li>
            </ul>

            <div class="formula-card">
              <h3>Analytical Thermal Conductivity Relationships</h3>
              <p>$$\text{BTU/(hr·ft·°F) to W/(m·K): } 1\text{ BTU/(hr}\cdot\text{ft}\cdot^\circ\text{F)} = \frac{1,055.05585}{3,600 \times 0.3048 \times (5/9)}\text{ W/(m}\cdot\text{K)} \approx 1.730735\text{ W/(m}\cdot\text{K)}$$</p>
              <p>$$\text{W/(m·K) to BTU/(hr·ft·°F): } 1\text{ W/(m}\cdot\text{K)} \approx 0.577789\text{ BTU/(hr}\cdot\text{ft}\cdot^\circ\text{F)}$$</p>
              <p>$$\text{Building Board BTU·in/(hr·ft²·°F): } 1\text{ BTU}\cdot\text{in/(hr}\cdot\text{ft}^2\cdot^\circ\text{F)} = \frac{1.730735}{12} \approx 0.144228\text{ W/(m}\cdot\text{K)}$$</p>
              <p>$$\text{CGS Metric: } 1\text{ cal/(s}\cdot\text{cm}\cdot^\circ\text{C)} = \frac{4.1868}{0.01}\text{ W/(m}\cdot\text{K)} = 418.68\text{ W/(m}\cdot\text{K)}$$</p>
              <p>$$\text{Metric Engineering: } 1\text{ kcal/(hr}\cdot\text{m}\cdot^\circ\text{C)} = \frac{4,186.8}{3,600}\text{ W/(m}\cdot\text{K)} = 1.163\text{ W/(m}\cdot\text{K)}$$</p>
              <p>$$\text{Architectural Imperial R-Value: } R = \frac{L_{\text{inches}}}{k_{\text{BTU}\cdot\text{in/(hr}\cdot\text{ft}^2\cdot^\circ\text{F)}} = \frac{L_{\text{meters}}}{k_{\text{W/(m}\cdot\text{K)}}} \times 5.678263$$</p>
            </div>
          </section>

          <section>
            <h2>Thermal Conductivity Spectrum of Engineering Materials</h2>
            <p>
              The thermal conductivity of matter spans over five orders of magnitude—ranging from evacuated aerogel foams with conductivities near \(0.015\text{ W/(m}\cdot\text{K)}\) up to synthetic CVD diamond and graphene exceeding \(2,000\text{ W/(m}\cdot\text{K)}\). The benchmark table below categorizes critical engineering materials:
            </p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>Material / Substance</th>
                  <th>SI \(\text{W/(m}\cdot\text{K)}\)</th>
                  <th>Imperial \(\text{BTU/(hr}\cdot\text{ft}\cdot^\circ\text{F)}\)</th>
                  <th>Trade \(\text{BTU}\cdot\text{in/(hr}\cdot\text{ft}^2\cdot^\circ\text{F)}\)</th>
                  <th>Thermal Role in Engineering</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Silica Aerogel Blanket</strong></td>
                  <td>0.015</td>
                  <td>0.0087</td>
                  <td>0.104</td>
                  <td>Cryogenic &amp; aerospace superinsulation</td>
                </tr>
                <tr>
                  <td><strong>Polyurethane Rigid Foam (PIR)</strong></td>
                  <td>0.022</td>
                  <td>0.0127</td>
                  <td>0.153</td>
                  <td>Refrigeration &amp; high-performance building envelope</td>
                </tr>
                <tr>
                  <td><strong>Still Air (Sea Level, 20°C)</strong></td>
                  <td>0.026</td>
                  <td>0.0150</td>
                  <td>0.180</td>
                  <td>Gaseous thermal insulation benchmark</td>
                </tr>
                <tr>
                  <td><strong>Expanded Polystyrene (EPS)</strong></td>
                  <td>0.036</td>
                  <td>0.0208</td>
                  <td>0.250</td>
                  <td>Architectural exterior wall foam board</td>
                </tr>
                <tr>
                  <td><strong>Fiberglass Batt Insulation</strong></td>
                  <td>0.040</td>
                  <td>0.0231</td>
                  <td>0.277</td>
                  <td>Residential stud-wall thermal dampening</td>
                </tr>
                <tr>
                  <td><strong>Hardwood Timber (Oak / Pine)</strong></td>
                  <td>0.15 &ndash; 0.17</td>
                  <td>0.087 &ndash; 0.098</td>
                  <td>1.04 &ndash; 1.18</td>
                  <td>Structural framing (thermal bridging material)</td>
                </tr>
                <tr>
                  <td><strong>Structural Concrete (Normal)</strong></td>
                  <td>1.40 &ndash; 1.70</td>
                  <td>0.81 &ndash; 0.98</td>
                  <td>9.71 &ndash; 11.78</td>
                  <td>High thermal mass building foundations</td>
                </tr>
                <tr>
                  <td><strong>Austenitic Stainless Steel (304)</strong></td>
                  <td>16.2</td>
                  <td>9.36</td>
                  <td>112.3</td>
                  <td>Corrosion-resistant thermal isolation structures</td>
                </tr>
                <tr>
                  <td><strong>Structural Carbon Steel (A36)</strong></td>
                  <td>50.2</td>
                  <td>29.0</td>
                  <td>348.0</td>
                  <td>Structural beam &amp; pressure vessel shells</td>
                </tr>
                <tr>
                  <td><strong>Die-Cast Aluminum (A380)</strong></td>
                  <td>109</td>
                  <td>63.0</td>
                  <td>755.7</td>
                  <td>Automotive engine heads &amp; transmission housings</td>
                </tr>
                <tr>
                  <td><strong>Extruded Aluminum (6063)</strong></td>
                  <td>201</td>
                  <td>116.1</td>
                  <td>1,393.6</td>
                  <td>Electronics heat sinks &amp; LED thermal dissipators</td>
                </tr>
                <tr>
                  <td><strong>Pure Copper (C11000 ETP)</strong></td>
                  <td>398 &ndash; 401</td>
                  <td>230.0 &ndash; 231.7</td>
                  <td>2,760 &ndash; 2,780</td>
                  <td>High-power CPU cold plates &amp; heat exchangers</td>
                </tr>
                <tr>
                  <td><strong>Chemical Vapor Diamond (CVD)</strong></td>
                  <td>1,800 &ndash; 2,200</td>
                  <td>1,040 &ndash; 1,271</td>
                  <td>12,480 &ndash; 15,250</td>
                  <td>Laser diode submounts &amp; GaN RF power amplifiers</td>
                </tr>
              </tbody>
            </table>
          </section>

          <section>
            <h2>Worked Engineering Case Study: Cryogenic LNG Pipe Insulation Analysis</h2>
            <div class="worked-example-card">
              <h3>Engineering Scenario: Cryogenic Pipeline Boil-Off Heat Gain Verification</h3>
              <p>
                An energy terminal engineer is specifying the insulation thickness for an <strong>8-inch Liquefied Natural Gas (LNG) transmission pipeline</strong> conveying liquid methane at <strong>-162°C (111.15 K)</strong> through an ambient outdoor environment at <strong>+38°C (311.15 K)</strong>. The total pipeline length is <strong>500 meters</strong>.
              </p>
              <p>
                The insulation material selected is rigid closed-cell <strong>cellular glass (foam glass)</strong> with a certified thermal conductivity of <strong>\(k = 0.040\text{ W/(m}\cdot\text{K)}\)</strong>. The insulation jacket has an installed thickness of <strong>\(150\text{ mm} = 0.15\text{ m}\)</strong>.
              </p>
              <p>The engineer must determine:</p>
              <ol>
                <li>The thermal conductivity in Imperial trade units [\(\text{BTU}\cdot\text{in/(hr}\cdot\text{ft}^2\cdot^\circ\text{F)}\)].</li>
                <li>The imperial R-value of the 150 mm (5.91 inch) insulation layer.</li>
                <li>The radial steady-state conductive heat ingress (\(\dot{Q}\)) in kilowatts and BTU/hr across the 500m line.</li>
              </ol>

              <h4>Step-by-Step Calculation:</h4>
              <p><strong>1. Convert Conductivity to Imperial Units:</strong></p>
              <p>$$k_{\text{BTU}\cdot\text{in}} = 0.040\text{ W/(m}\cdot\text{K)} \times 6.93347 \approx \mathbf{0.2773\text{ BTU}\cdot\text{in/(hr}\cdot\text{ft}^2\cdot^\circ\text{F)}}$$</p>

              <p><strong>2. Compute Imperial R-Value:</strong></p>
              <p>Insulation thickness \(L = 0.15\text{ m} \times 39.3701 = 5.9055\text{ inches}\).</p>
              <p>$$R_{\text{imperial}} = \frac{L_{\text{inches}}}{k_{\text{BTU}\cdot\text{in}}} = \frac{5.9055}{0.2773} \approx \mathbf{R\text{-}21.3}$$</p>

              <p><strong>3. Radial Heat Transfer Rate (Cylindrical Conduction):</strong></p>
              <p>Pipe outer radius \(r_1 = \frac{8.625\text{ in}}{2} = 4.3125\text{ in} = 0.1095\text{ m}\).</p>
              <p>Insulation outer radius \(r_2 = r_1 + 0.15\text{ m} = 0.2595\text{ m}\).</p>
              <p>$$\Delta T = T_{\text{ambient}} - T_{\text{pipe}} = 38 - (-162) = 200\text{ K} \quad (360^\circ\text{F})$$</p>
              <p>$$\dot{Q} = \frac{2\pi \cdot k \cdot L_{\text{length}} \cdot \Delta T}{\ln(r_2 / r_1)} = \frac{2 \times 3.14159 \times 0.040 \times 500 \times 200}{\ln(0.2595 / 0.1095)}$$</p>
              <p>$$\ln(2.36986) \approx 0.86283$$</p>
              <p>$$\dot{Q} = \frac{25,132.7}{0.86283} = 29,128\text{ Watts} = \mathbf{29.13\text{ kW}}$$</p>
              <p>$$\dot{Q}_{\text{BTU/hr}} = 29,128\text{ W} \times 3.412142\text{ BTU/(hr}\cdot\text{W)} = \mathbf{99,388\text{ BTU/hr}}$$</p>

              <p>
                <strong>Audit Conclusion:</strong> The 150 mm cellular glass insulation limits total cryogenic boil-off heat gain to 29.13 kW across the 500-meter line, well within the 35 kW re-liquefaction compressor capacity.
              </p>
            </div>
          </section>

          <section class="faq-section">
            <h2>Frequently Asked Questions Regarding Thermal Conductivity</h2>
            <div class="faq-item">
              <h3>What is the difference between thermal conductivity and thermal diffusivity?</h3>
              <p><strong>Thermal conductivity (\(k\))</strong> measures a material's capability to transfer heat under steady-state conditions, measured in \(\text{W/(m}\cdot\text{K)}\). <strong>Thermal diffusivity (\(\alpha\))</strong> measures the rate at which temperature changes propagate through a material under transient, time-varying conditions, defined as \(\alpha = \frac{k}{\rho \cdot c_p}\), where \(\rho\) is density and \(c_p\) is specific heat capacity. Measured in \(\text{m}^2\text{/s}\), high diffusivity indicates that a material rapidly responds to thermal shock and reaches thermal equilibrium quickly.</p>
            </div>
            <div class="faq-item">
              <h3>How does temperature affect the thermal conductivity of gases vs. liquids?</h3>
              <p>In gases, thermal conduction occurs through molecular collisions. As temperature rises, mean molecular velocity increases, causing the thermal conductivity of gases to <em>increase</em> with temperature (e.g., air increases from 0.024 W/m·K at 0°C to 0.030 W/m·K at 80°C). In most non-metallic liquids, intermolecular bonding weakens with thermal expansion, causing thermal conductivity to <em>decrease</em> with rising temperature (with the notable exception of water, which peaks around 130°C).</p>
            </div>
            <div class="faq-item">
              <h3>What is thermal contact resistance and how do thermal pastes help?</h3>
              <p>Even finely polished metal surfaces touch only at microscopic asperities, leaving microscopic air pockets across over 90% of the contact area. Because air has a very low conductivity (\(0.026\text{ W/m}\cdot\text{K}\)), these voids create a severe thermal barrier known as thermal contact resistance (\(R_c\)). Thermal interface materials (TIMs, such as zinc oxide or silver thermal grease, \(k \approx 4 \text{ to } 12\text{ W/m}\cdot\text{K}\)) displace the air, slashing interface resistance by over 80%.</p>
            </div>
            <div class="faq-item">
              <h3>How do moisture and humidity degrade insulation thermal conductivity?</h3>
              <p>Water has a thermal conductivity of approximately \(0.60\text{ W/(m}\cdot\text{K)}\)—over fifteen times higher than dry fiberglass or foam insulation (\(0.035\text{ to } 0.040\text{ W/m}\cdot\text{K)}\). When water vapor condenses inside porous insulation, it displaces dead air within the pores. A moisture accumulation of merely 1% to 2% by volume can degrade the effective insulation performance by up to 30% to 50%, requiring vapor retarders on building envelopes.</p>
            </div>
          </section>
        </article>
      </div>

      <aside class="converter-sidebar">
        <div class="sidebar-card">
          <h3>Related Thermal &amp; Physics Tools</h3>
          <ul class="sidebar-links">
            <li><a href="temperature-converter.html">Temperature Converter (°C, °F, K)</a></li>
            <li><a href="energy-converter.html">Energy Converter (Joules, BTU, kWh)</a></li>
            <li><a href="power-converter.html">Power Converter (Watts, kW, HP)</a></li>
            <li><a href="density-converter.html">Density Converter (kg/m³, lb/ft³)</a></li>
            <li><a href="viscosity-converter.html">Viscosity Converter (cP, cSt, Pa·s)</a></li>
            <li><a href="area-converter.html">Area Converter (m², ft², acres)</a></li>
            <li><a href="length-converter.html">Length Converter (m, ft, in)</a></li>
            <li><a href="pressure-converter.html">Pressure Converter (Pa, bar, psi)</a></li>
          </ul>
        </div>
        <div class="sidebar-card">
          <h3>R-Value Rule of Thumb</h3>
          <p class="sidebar-tip">
            To quickly calculate imperial R-value per inch of insulation thickness:
            <br><br>
            $$R/\text{inch} \approx \frac{0.1442}{k_{\text{W/(m}\cdot\text{K)}}}$$
            <br>
            For a foam with \(k = 0.024\text{ W/m}\cdot\text{K}\), \(R/\text{inch} = 0.1442 / 0.024 \approx \mathbf{R\text{-}6.0/\text{inch}}\).
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
      // Base unit: W/(m·K)
      var factors = {
        w_mk: 1.0,
        btu_hrftf: 1.730734666,
        btu_in: 0.144227889,
        cal_scmc: 418.68,
        kcal_hrmc: 1.163,
        w_cmk: 100.0
      };

      var unitLabels = {
        w_mk: 'W/(m·K)',
        btu_hrftf: 'BTU/(hr·ft·°F)',
        btu_in: 'BTU·in/(hr·ft²·°F)',
        cal_scmc: 'cal/(s·cm·°C)',
        kcal_hrmc: 'kcal/(hr·m·°C)',
        w_cmk: 'W/(cm·K)'
      };

      var fromInput = document.getElementById('tcFromVal');
      var fromSelect = document.getElementById('tcFromUnit');
      var toInput = document.getElementById('tcToVal');
      var toSelect = document.getElementById('tcToUnit');
      var swapBtn = document.getElementById('tcSwapBtn');

      var equationEl = document.getElementById('tcEquation');
      var rPerInchEl = document.getElementById('tcRPerInch');
      var rsi100mmEl = document.getElementById('tcRsi100mm');
      var regimeEl = document.getElementById('tcRegimeVal');

      function calculate() {
        var val = parseFloat(fromInput.value);
        if (isNaN(val)) {
          toInput.value = '';
          return;
        }

        var fromUnit = fromSelect.value;
        var toUnit = toSelect.value;

        // Base W/(m·K)
        var baseWmk = val * factors[fromUnit];
        var result = baseWmk / factors[toUnit];

        if (Math.abs(result) >= 1e7 || (Math.abs(result) < 1e-4 && result !== 0)) {
          toInput.value = result.toExponential(5);
        } else {
          toInput.value = parseFloat(result.toPrecision(6)).toString();
        }

        if (equationEl) {
          equationEl.textContent = val + " " + unitLabels[fromUnit] + " = " + toInput.value + " " + unitLabels[toUnit];
        }

        // Submetrics
        if (baseWmk > 0) {
          // Imperial R-value per inch = 0.144228 / baseWmk
          var rPerIn = 0.144227889 / baseWmk;
          rPerInchEl.textContent = "R-" + rPerIn.toFixed(2) + " / inch";

          // Metric RSI per 100mm (0.1 m) = 0.1 / baseWmk
          var rsi = 0.1 / baseWmk;
          rsi100mmEl.textContent = "RSI " + rsi.toFixed(3) + " m²·K/W";

          // Thermal regime
          if (baseWmk < 0.05) {
            regimeEl.textContent = "High-Performance Thermal Insulator";
          } else if (baseWmk < 0.25) {
            regimeEl.textContent = "Moderate Insulator / Wood / Plastic";
          } else if (baseWmk < 5.0) {
            regimeEl.textContent = "Masonry / Concrete / Glass / Rock";
          } else if (baseWmk < 100.0) {
            regimeEl.textContent = "Alloy Steel / Moderate Conductor";
          } else {
            regimeEl.textContent = "High Thermal Conductor (Cu, Al, Ag, Diamond)";
          }
        } else {
          rPerInchEl.textContent = "N/A";
          rsi100mmEl.textContent = "N/A";
          regimeEl.textContent = "N/A";
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
# 4. VISCOSITY CONVERTER
# -------------------------------------------------------------
viscosity_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Viscosity Converter — Centipoise, Pa·s, cSt, Stokes, SUS | CalcHub</title>
  <meta name="description" content="Convert dynamic and kinematic fluid viscosity across Centipoise (cP), Pascal-seconds (Pa·s), Centistokes (cSt), Stokes, Saybolt Universal Seconds (SUS), and Poise.">
  <meta name="keywords" content="viscosity converter, centipoise to pa s, cp to cst, dynamic to kinematic viscosity, saybolt universal seconds to centistokes, sus to cst, reynolds number viscosity, fluid friction converter">
  <meta name="author" content="CalcHub Fluid Dynamics & Tribology Engineering Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/viscosity-converter.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="Viscosity Converter — Centipoise, Pa·s, cSt, Stokes, SUS | CalcHub">
  <meta property="og:description" content="Convert dynamic and kinematic fluid viscosity across Centipoise (cP), Pascal-seconds (Pa·s), Centistokes (cSt), Stokes, Saybolt Universal Seconds (SUS), and Poise.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/viscosity-converter.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/viscosity-converter.html#app",
      "name": "Precision Dynamic & Kinematic Viscosity Converter",
      "url": "https://calchub.org/viscosity-converter.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Scientific fluid viscosity conversion engine translating between dynamic viscosity (Pa·s, cP, Poise) and kinematic viscosity (cSt, Stokes, SUS, m²/s)."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Universal Unit Converters", "item": "https://calchub.org/converter.html"},
        {"@type": "ListItem", "position": 3, "name": "Viscosity Converter", "item": "https://calchub.org/viscosity-converter.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the physical distinction between Dynamic Viscosity and Kinematic Viscosity?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Dynamic viscosity (μ or η, also termed absolute viscosity) measures a fluid's internal tangential resistance to shear flow under applied shear stress: τ = μ · (du/dy). It is measured in Pascal-seconds (Pa·s) or Centipoise (cP). Kinematic viscosity (ν) is the ratio of dynamic viscosity to fluid density: ν = μ / ρ. Measured in Centistokes (cSt) or m²/s, kinematic viscosity represents a fluid's resistive flow behavior driven purely by gravitational body forces, such as draining through an efflux capillary viscometer."
          }
        },
        {
          "@type": "Question",
          "name": "What is the exact mathematical relationship between Centipoise (cP) and Pascal-seconds (Pa·s)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "One Pascal-second (1 Pa·s) equals exactly 1,000 millipascal-seconds (mPa·s) or 1,000 Centipoise (cP), and 10 Poise (P). Pure liquid water at 20°C (68°F) has a dynamic viscosity of 1.002 cP (0.001002 Pa·s). Therefore, Centipoise conveniently expresses viscosity relative to water, where a fluid with a viscosity of 50 cP is 50 times more viscous than room-temperature water."
          }
        },
        {
          "@type": "Question",
          "name": "How are Saybolt Universal Seconds (SUS) converted to Centistokes (cSt)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Per ASTM D2161 standards, Saybolt Universal Seconds (SUS or SSU) measure the time in seconds required for 60 mL of petroleum oil to flow through a calibrated Saybolt Universal orifice at a controlled temperature (typically 100°F or 210°F). For kinematic viscosities greater than 100 cSt, the conversion is approximately: cSt ≈ 0.216 × SUS. For lower viscosities, empirical ASTM polynomial tables or non-linear formulas must be utilized."
          }
        },
        {
          "@type": "Question",
          "name": "Why does liquid viscosity drop dramatically as temperature increases?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In liquids, viscosity arises predominantly from cohesive intermolecular attractive forces. As thermal energy increases, molecular thermal agitation expands intermolecular distances and weakens intermolecular bonding, allowing liquid layers to slide past one another much more readily. This temperature dependence is modeled mathematically by the Andrade equation or the Vogel-Fulcher-Tammann (VFT) empirical relationship."
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
            <span>Viscosity Converter</span>
          </div>
          <span class="badge">Tribology, Rheology &amp; Fluid Mechanics</span>
          <h1>Precision Viscosity Converter</h1>
          <p class="tagline">Convert dynamic and kinematic viscosity units across cP, Pa·s, cSt, Stokes, and SUS with density interconversions.</p>
        </div>

        <div class="calculator-container card-surface">
          <div class="converter-box">
            <div class="converter-inputs-grid">
              <div class="input-col">
                <label for="viscFromVal" class="input-label">From Value</label>
                <input type="number" id="viscFromVal" class="converter-num-input" value="100" step="any" placeholder="Enter viscosity">
                <label for="viscFromUnit" class="input-label sub-label">From Unit</label>
                <select id="viscFromUnit" class="converter-select">
                  <optgroup label="Dynamic Viscosity (Absolute)">
                    <option value="cp" selected>Centipoise (cP = mPa·s)</option>
                    <option value="pa_s">Pascal-Second (Pa·s)</option>
                    <option value="poise">Poise (P = 0.1 Pa·s)</option>
                    <option value="lbf_s_ft2">lbf·s/ft² (slug/ft·s)</option>
                    <option value="lb_ft_s">lb/(ft·s)</option>
                  </optgroup>
                  <optgroup label="Kinematic Viscosity (Gravity-Driven)">
                    <option value="cst">Centistokes (cSt = mm²/s)</option>
                    <option value="stokes">Stokes (St = cm²/s)</option>
                    <option value="m2_s">Square Meters / Sec (m²/s)</option>
                    <option value="ft2_s">Square Feet / Sec (ft²/s)</option>
                    <option value="sus">Saybolt Universal Sec (SUS)</option>
                  </optgroup>
                </select>
              </div>

              <div class="swap-col">
                <button type="button" id="viscSwapBtn" class="swap-button" title="Swap input and output units" aria-label="Swap units">
                  &#8644;
                </button>
              </div>

              <div class="input-col">
                <label for="viscToVal" class="input-label">Converted Value</label>
                <input type="text" id="viscToVal" class="converter-num-input output-val" readonly value="0.100">
                <label for="viscToUnit" class="input-label sub-label">To Unit</label>
                <select id="viscToUnit" class="converter-select">
                  <optgroup label="Dynamic Viscosity (Absolute)">
                    <option value="cp">Centipoise (cP = mPa·s)</option>
                    <option value="pa_s" selected>Pascal-Second (Pa·s)</option>
                    <option value="poise">Poise (P = 0.1 Pa·s)</option>
                    <option value="lbf_s_ft2">lbf·s/ft² (slug/ft·s)</option>
                    <option value="lb_ft_s">lb/(ft·s)</option>
                  </optgroup>
                  <optgroup label="Kinematic Viscosity (Gravity-Driven)">
                    <option value="cst">Centistokes (cSt = mm²/s)</option>
                    <option value="stokes">Stokes (St = cm²/s)</option>
                    <option value="m2_s">Square Meters / Sec (m²/s)</option>
                    <option value="ft2_s">Square Feet / Sec (ft²/s)</option>
                    <option value="sus">Saybolt Universal Sec (SUS)</option>
                  </optgroup>
                </select>
              </div>
            </div>

            <div style="margin-top:0.75rem;padding:0.75rem 1rem;background:#F8FAFC;border-radius:8px;border:1px solid var(--border-light);display:flex;align-items:center;gap:1rem;flex-wrap:wrap;">
              <label for="viscDensity" style="font-size:0.875rem;font-weight:600;color:var(--text-main);">Assumed Fluid Density (for Dynamic &harr; Kinematic bridge):</label>
              <input type="number" id="viscDensity" value="1000" step="any" style="width:110px;padding:0.4rem 0.6rem;border:1px solid #CBD5E1;border-radius:6px;font-size:0.9rem;" placeholder="kg/m³">
              <span style="font-size:0.825rem;color:var(--text-muted);">(Default: 1,000 kg/m³ for water; ~880 kg/m³ for ISO motor oils)</span>
            </div>

            <div class="converter-quick-presets">
              <span class="preset-label">Standard Fluid Benchmarks:</span>
              <button type="button" class="preset-chip" data-val="1.002" data-from="cp" data-to="pa_s">Water @ 20°C (1.002 cP = 1.002 mPa·s)</button>
              <button type="button" class="preset-chip" data-val="100" data-from="cst" data-to="sus">ISO VG 100 Oil (100 cSt ≈ 463 SUS)</button>
              <button type="button" class="preset-chip" data-val="1412" data-from="cp" data-to="pa_s">Glycerin @ 20°C (1,412 cP = 1.412 Pa·s)</button>
              <button type="button" class="preset-chip" data-val="50000" data-from="cp" data-to="poise">Honey / Molasses (50,000 cP = 500 P)</button>
            </div>

            <div class="conversion-summary-panel" id="viscSummaryCard">
              <div class="summary-line">
                <span class="summary-label">Direct Relation:</span>
                <span class="summary-formula" id="viscEquation">100 cP = 0.100 Pa·s</span>
              </div>
              <div class="summary-submetrics">
                <div class="submetric-item">
                  <span class="submetric-name">Kinematic @ 1000 kg/m³:</span>
                  <span class="submetric-val" id="viscKinVal">100.0 cSt (mm²/s)</span>
                </div>
                <div class="submetric-item">
                  <span class="submetric-name">Saybolt Universal Time:</span>
                  <span class="submetric-val" id="viscSusVal">463.2 SUS</span>
                </div>
                <div class="submetric-item">
                  <span class="submetric-name">Flow Analogy:</span>
                  <span class="submetric-val" id="viscAnalogyVal">Light Motor Oil (SAE 30 / ISO VG 100)</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <section>
            <h2>Rheological Fundamentals: Dynamic vs. Kinematic Viscosity</h2>
            <p>
              Viscosity is the quantitative physical measure of a fluid's internal friction—its resistance to progressive shear deformation or flow when subjected to an external mechanical force. Conceived mathematically by Sir Isaac Newton, fluid layers in laminar motion experience a shear stress (\(\tau\)) directly proportional to the transverse velocity gradient:
            </p>
            <p>
              $$\tau = \mu \cdot \frac{du}{dy}$$
            </p>
            <p>
              Where \(\tau\) is shear stress (\(\text{N/m}^2\) or \(\text{Pa}\)), \(du/dy\) is the shear rate (\(\text{s}^{-1}\)), and \(\mu\) is the coefficient of <strong>Dynamic Viscosity</strong> (also termed absolute viscosity).
            </p>
            <p>
              Engineers classify viscosity into two complementary domains:
            </p>
            <ol>
              <li><strong>Dynamic Viscosity (\(\mu\) or \(\eta\)):</strong> Measures the force required to overcome internal fluid friction under mechanical shearing. The SI unit is the <strong>Pascal-second (\(\text{Pa}\cdot\text{s} = \text{N}\cdot\text{s/m}^2 = \text{kg/(m}\cdot\text{s)})\)</strong>. In chemistry and tribology, the CGS unit <strong>Poise (P)</strong> and <strong>Centipoise (cP)</strong> dominate.</li>
              <li><strong>Kinematic Viscosity (\(\nu\)):</strong> Measures fluid resistive flow under the influence of Earth's gravity, calculated by dividing dynamic viscosity by mass density (\(\rho\)):
                $$\nu = \frac{\mu}{\rho}$$
                The SI unit is \(\text{m}^2/\text{s}\), but the petroleum, lubricants, and hydraulic industries universally utilize the <strong>Centistokes (\(\text{cSt} = \text{mm}^2/\text{s}\))</strong> or legacy <strong>Saybolt Universal Seconds (SUS)</strong>.
              </li>
            </ol>
          </section>

          <section>
            <h2>Exact Mathematical Conversion Multipliers &amp; Analytical Equations</h2>
            <p>
              The mathematical relationships connecting dynamic viscosity, kinematic viscosity, CGS units, and imperial units are governed by standard metrology constants:
            </p>

            <div class="formula-card">
              <h3>Core Viscosity Conversion Formulations</h3>
              <p>$$\text{SI Dynamic to Centipoise: } 1\text{ Pa}\cdot\text{s} \equiv 1,000\text{ mPa}\cdot\text{s} = 1,000\text{ cP} = 10\text{ Poise (P)}$$</p>
              <p>$$\text{CGS Poise Definition: } 1\text{ Poise} \equiv 1\text{ dyn}\cdot\text{s/cm}^2 = 0.1\text{ Pa}\cdot\text{s} = 100\text{ cP}$$</p>
              <p>$$\text{Kinematic SI to Centistokes: } 1\text{ m}^2/\text{s} = 10,000\text{ Stokes (St)} = 1,000,000\text{ cSt}$$</p>
              <p>$$\text{Centistokes to SI: } 1\text{ cSt} \equiv 1\text{ mm}^2/\text{s} = 10^{-6}\text{ m}^2/\text{s} = 0.01\text{ St}$$</p>
              <p>$$\text{Dynamic to Kinematic: } \nu_{\text{cSt}} = \frac{\mu_{\text{cP}}}{\text{Specific Gravity (SG)}} = \frac{\mu_{\text{cP}}}{\rho_{\text{kg/m}^3} / 1,000}$$</p>
              <p>$$\text{Imperial Dynamic Units: } 1\text{ lbf}\cdot\text{s/ft}^2 = 1\text{ slug/(ft}\cdot\text{s)} \approx 47.88026\text{ Pa}\cdot\text{s} = 47,880.26\text{ cP}$$</p>
              <p>$$\text{Saybolt Seconds Conversion (cSt > 100): } \text{SUS} \approx 4.632 \times \nu_{\text{cSt}} \iff \nu_{\text{cSt}} \approx 0.2158 \times \text{SUS}$$</p>
            </div>
          </section>

          <section>
            <h2>Comparative Viscosity Benchmark Spectrum Across Common Fluids</h2>
            <p>
              Understanding the magnitude of fluid resistance is vital for selecting industrial centrifugal pumps, positive displacement gear pumps, motor lubricants, and pipeline diameters. The comparative spectrum below illustrates representative fluids at standard ambient conditions (20°C / 68°F unless otherwise specified):
            </p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>Fluid Substance &amp; Temperature</th>
                  <th>Dynamic Viscosity (\(\text{cP}\))</th>
                  <th>Dynamic Viscosity (\(\text{Pa}\cdot\text{s}\))</th>
                  <th>Kinematic Viscosity (\(\text{cSt}\))</th>
                  <th>Saybolt Seconds (SUS)</th>
                  <th>Rheological Flow Classification</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Dry Air (20°C, 1 atm)</strong></td>
                  <td>0.0182</td>
                  <td>0.0000182</td>
                  <td>15.1</td>
                  <td>&lt;32 SUS</td>
                  <td>Newtonian Gas</td>
                </tr>
                <tr>
                  <td><strong>Gasoline (Automotive Fuel)</strong></td>
                  <td>0.60</td>
                  <td>0.00060</td>
                  <td>0.81</td>
                  <td>&lt;32 SUS</td>
                  <td>Newtonian Fluid (Low Drag)</td>
                </tr>
                <tr>
                  <td><strong>Pure Water (at 20°C)</strong></td>
                  <td>1.002</td>
                  <td>0.001002</td>
                  <td>1.004</td>
                  <td>31 SUS</td>
                  <td>Global Viscosity Calibration Standard</td>
                </tr>
                <tr>
                  <td><strong>Whole Milk (Fresh Cow Milk)</strong></td>
                  <td>2.0 &ndash; 3.0</td>
                  <td>0.002 &ndash; 0.003</td>
                  <td>1.9 &ndash; 2.9</td>
                  <td>~34 SUS</td>
                  <td>Near-Newtonian Emulsion</td>
                </tr>
                <tr>
                  <td><strong>Light Machine Oil (ISO VG 32)</strong></td>
                  <td>27.5</td>
                  <td>0.0275</td>
                  <td>32.0</td>
                  <td>150 SUS</td>
                  <td>Newtonian Lubricating Oil</td>
                </tr>
                <tr>
                  <td><strong>Heavy Engine Oil (SAE 50 @ 20°C)</strong></td>
                  <td>450 &ndash; 500</td>
                  <td>0.45 &ndash; 0.50</td>
                  <td>500 &ndash; 560</td>
                  <td>~2,500 SUS</td>
                  <td>High-viscosity crankcase lubricant</td>
                </tr>
                <tr>
                  <td><strong>Castor Oil (Pure Organic)</strong></td>
                  <td>985</td>
                  <td>0.985</td>
                  <td>1,025</td>
                  <td>~4,750 SUS</td>
                  <td>Natural viscous trigylceride</td>
                </tr>
                <tr>
                  <td><strong>Honey (Clover Table Grade)</strong></td>
                  <td>2,000 &ndash; 10,000</td>
                  <td>2.0 &ndash; 10.0</td>
                  <td>1,400 &ndash; 7,000</td>
                  <td>~9,000 &ndash; 46,000 SUS</td>
                  <td>Newtonian to Pseudoplastic Liquid</td>
                </tr>
                <tr>
                  <td><strong>Peanut Butter / Toothpaste</strong></td>
                  <td>100,000 &ndash; 250,000</td>
                  <td>100 &ndash; 250</td>
                  <td>N/A (Bingham Plastic)</td>
                  <td>N/A (Semi-solid)</td>
                  <td>Non-Newtonian Yield Stress Solid</td>
                </tr>
              </tbody>
            </table>
          </section>

          <section>
            <h2>Pipe Friction &amp; The Hagen-Poiseuille Pressure Drop Equation</h2>
            <p>
              In laminar pipe flow (Reynolds Number \(Re < 2,300\)), dynamic viscosity directly governs the total pressure drop required to drive fluid through a circular conduit, modeled exactly by the <strong>Hagen-Poiseuille Law</strong>:
            </p>
            <p>
              $$\Delta P = \frac{8 \cdot \mu \cdot L \cdot Q}{\pi \cdot R^4} = \frac{128 \cdot \mu \cdot L \cdot Q}{\pi \cdot D^4}$$
            </p>
            <p>
              Where \(\Delta P\) is pressure drop in Pascals, \(\mu\) is dynamic viscosity in \(\text{Pa}\cdot\text{s}\), \(L\) is pipe length, \(Q\) is volumetric flow rate in \(\text{m}^3/\text{s}\), and \(D\) is pipe internal diameter.
            </p>
            <p>
              Because pressure drop is directly proportional to dynamic viscosity (\(\Delta P \propto \mu\)), pumping heavy crude oil or syrup with a viscosity of \(1,000\text{ cP}\) requires precisely <strong>1,000 times more pumping pressure</strong> than pumping water at the identical flow rate through the same line. Furthermore, because pressure loss scales inversely with the fourth power of pipe diameter (\(D^4\)), even modest pipe erosion or diameter reduction severely multiplies pump head pressure requirements.
            </p>
          </section>

          <section>
            <h2>Worked Engineering Case Study: Hydraulic Oil Lube System Viscosity Audit</h2>
            <div class="worked-example-card">
              <h3>Engineering Scenario: Industrial Gearbox Lubrication Grade Conversion</h3>
              <p>
                A manufacturing plant operates a heavy ball mill driven by a multi-stage helical gearbox. The German machine manufacturer specifies an operating lubricant viscosity of <strong>\(220\text{ cSt}\) at 40°C</strong> (ISO VG 220). The maintenance depot in the United States stocks hydraulic oil labeled in <strong>Saybolt Universal Seconds (SUS)</strong> and dynamic viscosity in <strong>Centipoise (cP)</strong>. The lubricant oil has a measured mass density of <strong>\(885\text{ kg/m}^3\) (Specific Gravity = 0.885)</strong> at 40°C.
              </p>
              <p>The plant tribology engineer must compute:</p>
              <ol>
                <li>The absolute dynamic viscosity in Centipoise (\(\text{cP}\)) and Pascal-seconds (\(\text{Pa}\cdot\text{s}\)).</li>
                <li>The equivalent Saybolt Universal Seconds (\(\text{SUS}\)) rating at 100°F (approx. 37.8°C).</li>
                <li>The Reynolds number (\(Re\)) if oil flows through a 2-inch (0.0508m) lube supply line at \(1.2\text{ m/s}\).</li>
                <li>Confirm whether the flow regime is laminar (\(Re < 2,000\)).</li>
              </ol>

              <h4>Step-by-Step Calculation:</h4>
              <p><strong>1. Convert Kinematic Viscosity to Dynamic Viscosity:</strong></p>
              <p>$$\mu_{\text{cP}} = \nu_{\text{cSt}} \times \text{Specific Gravity} = 220\text{ cSt} \times 0.885 = \mathbf{194.7\text{ cP}}$$</p>
              <p>$$\mu_{\text{Pa}\cdot\text{s}} = \frac{194.7\text{ cP}}{1,000} = \mathbf{0.1947\text{ Pa}\cdot\text{s}}$$</p>

              <p><strong>2. Convert Centistokes to Saybolt Universal Seconds (SUS):</strong></p>
              <p>Because \(\nu > 100\text{ cSt}\), we apply the standard ASTM D2161 multiplier (\(\text{SUS} \approx 4.632 \times \nu_{\text{cSt}}\)):</p>
              <p>$$\text{SUS} = 4.632 \times 220 \approx \mathbf{1,019\text{ SUS}}$$</p>

              <p><strong>3. Calculate Pipe Flow Reynolds Number (\(Re\)):</strong></p>
              <p>$$\nu_{\text{m}^2/\text{s}} = 220\text{ cSt} \times 10^{-6} = 0.000220\text{ m}^2/\text{s}$$</p>
              <p>$$Re = \frac{v \cdot D}{\nu} = \frac{1.2\text{ m/s} \times 0.0508\text{ m}}{0.000220\text{ m}^2/\text{s}} = \frac{0.06096}{0.000220} \approx \mathbf{277.1}$$</p>

              <p>
                <strong>Tribology Verification:</strong> The Reynolds number of 277.1 is well below the 2,300 laminar critical threshold. Flow in the lubrication circuit is smoothly laminar without turbulence, preventing foaming and ensuring steady oil film delivery to the gearbox bearings.
              </p>
            </div>
          </section>

          <section class="faq-section">
            <h2>Frequently Asked Questions Regarding Fluid Viscosity Units</h2>
            <div class="faq-item">
              <h3>What is the difference between Newtonian and non-Newtonian fluids?</h3>
              <p>A <strong>Newtonian fluid</strong> (such as water, mineral oil, or alcohol) possesses a constant viscosity that remains invariant regardless of the shear rate applied. In contrast, <strong>non-Newtonian fluids</strong> change their apparent viscosity under shear: <em>shear-thinning (pseudoplastic)</em> fluids like paint, blood, and ketchup become thinner as they are stirred or pumped; <em>shear-thickening (dilatant)</em> fluids like cornstarch-water suspensions become more solid under rapid impact; and <em>thixotropic</em> fluids become less viscous over time under sustained mixing.</p>
            </div>
            <div class="faq-item">
              <h3>What does Viscosity Index (VI) mean on motor oil bottles?</h3>
              <p>The Viscosity Index (VI) is an empirical, unitless number measuring how much a lubricant's kinematic viscosity changes across temperature (historically benchmarked between 40°C and 100°C per ASTM D2270). A higher VI indicates that the oil's viscosity changes less dramatically across thermal swings. Modern multigrade synthetic motor oils (such as 0W-40) feature VI values above 160 to 180, flowing easily during sub-zero winter cold starts while retaining adequate lubricating film thickness under high-temperature highway cruising.</p>
            </div>
            <div class="faq-item">
              <h3>How does a capillary U-tube viscometer measure kinematic viscosity?</h3>
              <p>A capillary viscometer (such as an Ubbelohde or Cannon-Fenske tube) measures the efflux time (\(t\)) required for a fixed volume of liquid to drain through a calibrated precision glass capillary under gravity. Kinematic viscosity is calculated via \(\nu = C \cdot t\), where \(C\) is the manufacturer's certified viscometer calibration constant (in \(\text{cSt/s}\)).</p>
            </div>
            <div class="faq-item">
              <h3>Can pressure increase fluid viscosity?</h3>
              <p>Yes. Under extreme pressures encountered in elastohydrodynamic lubrication of gears and rolling element bearings (&gt;1,000 bar or &gt;100 MPa), fluid molecules are compressed tightly together. By the Barus equation (\(\mu_P = \mu_0 e^{\alpha P}\)), mineral oil viscosity can increase by several orders of magnitude under peak contact stress, momentarily transforming from liquid oil into a glass-like solid that prevents metal-to-metal contact.</p>
            </div>
          </section>
        </article>
      </div>

      <aside class="converter-sidebar">
        <div class="sidebar-card">
          <h3>Related Fluid &amp; Pressure Tools</h3>
          <ul class="sidebar-links">
            <li><a href="density-converter.html">Density Converter (kg/m³, lb/ft³, API)</a></li>
            <li><a href="flow-rate-converter.html">Flow Rate Converter (GPM, L/min, m³/h)</a></li>
            <li><a href="pressure-converter.html">Pressure Converter (psi, bar, kPa)</a></li>
            <li><a href="temperature-converter.html">Temperature Converter (°C, °F, K)</a></li>
            <li><a href="speed-converter.html">Speed Converter (m/s, km/h)</a></li>
            <li><a href="thermal-conductivity-converter.html">Thermal Conductivity (W/m·K)</a></li>
            <li><a href="energy-converter.html">Energy Converter (Joules, BTU)</a></li>
            <li><a href="force-converter.html">Force Converter (N, lbf)</a></li>
          </ul>
        </div>
        <div class="sidebar-card">
          <h3>The Golden Metric Rule</h3>
          <p class="sidebar-tip">
            Remember water's baseline:
            <br><br>
            <strong>Water @ 20°C:</strong><br>
            &bull; Dynamic = <strong>1.002 cP</strong> (0.001 Pa·s)<br>
            &bull; Kinematic = <strong>1.004 cSt</strong> (1.004 mm²/s)<br>
            <br>
            Any fluid with \(X\text{ cP}\) is roughly \(X\) times more viscous than water!
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
      // Internal standard representation: Dynamic viscosity in Pa·s
      var DYN_FACTORS = {
        pa_s: 1.0,
        cp: 0.001,
        poise: 0.1,
        lbf_s_ft2: 47.88025898,
        lb_ft_s: 1.48816394
      };

      var KIN_FACTORS = {
        m2_s: 1.0,
        cst: 1e-6,
        stokes: 1e-4,
        ft2_s: 0.09290304
      };

      var unitLabels = {
        pa_s: 'Pa·s',
        cp: 'cP',
        poise: 'P',
        lbf_s_ft2: 'lbf·s/ft²',
        lb_ft_s: 'lb/(ft·s)',
        m2_s: 'm²/s',
        cst: 'cSt',
        stokes: 'St',
        ft2_s: 'ft²/s',
        sus: 'SUS'
      };

      var isDyn = {
        pa_s: true, cp: true, poise: true, lbf_s_ft2: true, lb_ft_s: true
      };

      function toDynamicPaS(val, unit, density) {
        if (isDyn[unit]) {
          return val * DYN_FACTORS[unit];
        }
        // Kinematic to Dynamic: mu = nu * rho
        var nuM2s = 0;
        if (unit === 'sus') {
          // SUS to cSt
          var cst = (val > 100) ? 0.2158 * val : (0.226 * val - 195.0 / val);
          if (cst < 0) cst = 0;
          nuM2s = cst * 1e-6;
        } else {
          nuM2s = val * KIN_FACTORS[unit];
        }
        return nuM2s * density;
      }

      function fromDynamicPaS(paS, unit, density) {
        if (isDyn[unit]) {
          return paS / DYN_FACTORS[unit];
        }
        // Dynamic to Kinematic: nu = mu / rho
        var nuM2s = (density > 0) ? (paS / density) : 0;
        if (unit === 'sus') {
          var cst = nuM2s * 1e6;
          // cSt to SUS
          if (cst <= 0) return 0;
          if (cst > 100) {
            return cst / 0.2158;
          } else {
            // approx inversion
            return 4.632 * cst;
          }
        }
        return nuM2s / KIN_FACTORS[unit];
      }

      var fromInput = document.getElementById('viscFromVal');
      var fromSelect = document.getElementById('viscFromUnit');
      var toInput = document.getElementById('viscToVal');
      var toSelect = document.getElementById('viscToUnit');
      var densityInput = document.getElementById('viscDensity');
      var swapBtn = document.getElementById('viscSwapBtn');

      var equationEl = document.getElementById('viscEquation');
      var kinValEl = document.getElementById('viscKinVal');
      var susValEl = document.getElementById('viscSusVal');
      var analogyEl = document.getElementById('viscAnalogyVal');

      function calculate() {
        var val = parseFloat(fromInput.value);
        var density = parseFloat(densityInput.value);
        if (isNaN(density) || density <= 0) density = 1000.0;

        if (isNaN(val)) {
          toInput.value = '';
          return;
        }

        var fromUnit = fromSelect.value;
        var toUnit = toSelect.value;

        var basePaS = toDynamicPaS(val, fromUnit, density);
        var result = fromDynamicPaS(basePaS, toUnit, density);

        if (Math.abs(result) >= 1e7 || (Math.abs(result) < 1e-4 && result !== 0)) {
          toInput.value = result.toExponential(5);
        } else {
          toInput.value = parseFloat(result.toPrecision(6)).toString();
        }

        if (equationEl) {
          equationEl.textContent = val + " " + unitLabels[fromUnit] + " = " + toInput.value + " " + unitLabels[toUnit];
        }

        // Submetrics
        var cst = (basePaS / density) * 1e6;
        if (kinValEl) {
          kinValEl.textContent = (cst >= 1e5 ? cst.toExponential(3) : cst.toFixed(2)) + " cSt (mm²/s)";
        }

        if (susValEl) {
          var sus = (cst > 100) ? (cst * 4.632) : (cst * 4.632);
          susValEl.textContent = (sus >= 1e5 ? sus.toExponential(3) : sus.toFixed(1)) + " SUS";
        }

        if (analogyEl) {
          var cp = basePaS * 1000.0;
          if (cp < 0.1) {
            analogyEl.textContent = "Gas / Vapor (Air ~0.018 cP)";
          } else if (cp < 5.0) {
            analogyEl.textContent = "Thin Liquid (Water ~1.0 cP, Gas ~0.6 cP)";
          } else if (cp < 50.0) {
            analogyEl.textContent = "Light Oil (Kerosene, SAE 10W)";
          } else if (cp < 500.0) {
            analogyEl.textContent = "Motor / Gear Oil (SAE 30-50, Olive Oil)";
          } else if (cp < 5000.0) {
            analogyEl.textContent = "Thick Viscous (Glycerin ~1,400 cP, Syrup)";
          } else if (cp < 50000.0) {
            analogyEl.textContent = "Heavy Slurry (Honey ~10,000 cP, Molasses)";
          } else {
            analogyEl.textContent = "Semi-Solid / Paste (Grease, Peanut Butter)";
          }
        }
      }

      fromInput.addEventListener('input', calculate);
      fromSelect.addEventListener('change', calculate);
      toSelect.addEventListener('change', calculate);
      densityInput.addEventListener('input', calculate);

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
with open(os.path.join(BASE_DIR, 'thermal-conductivity-converter.html'), 'w', encoding='utf-8') as f:
    f.write(thermal_html.strip() + '\n')
print("Generated thermal-conductivity-converter.html successfully!")

with open(os.path.join(BASE_DIR, 'viscosity-converter.html'), 'w', encoding='utf-8') as f:
    f.write(viscosity_html.strip() + '\n')
print("Generated viscosity-converter.html successfully!")
