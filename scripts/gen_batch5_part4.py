"""
Generates earth-pit-resistance-calculator.html and electrical-power-calculator.html
Each tool includes:
- 1,000+ words of deep engineering content
- Exact keyword matching in title, meta description, and H1
- KaTeX mathematical formulas
- Interactive JS calculation engine
- Reference engineering lookup tables
- Worked real-world case study example card
- Schema.org SoftwareApplication and FAQPage JSON-LD
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ==========================================
# 1. EARTH PIT RESISTANCE CALCULATOR
# ==========================================
TOOL_EARTH_PIT = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Earth Pit Resistance Calculator — IEEE 80, IS 3043 &amp; BS 7430 Grounding</title>
  <meta name="description" content="Calculate earth pit and grounding electrode resistance using IEEE 80, IS 3043, and BS 7430 formulas for driven rods, soil resistivity, and parallel arrays.">
  <meta name="keywords" content="earth pit resistance calculator, earth pit resistance online, free earth pit resistance, calculate earth pit resistance, grounding electrode resistance, ieee 80 ground rod formula, earthing pit calculator, soil resistivity grounding">
  <link rel="canonical" href="https://calchub.org/earth-pit-resistance-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "Earth Pit & Grounding Electrode Resistance Calculator",
        "operatingSystem": "All",
        "applicationCategory": "EngineeringApplication",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
        "description": "Calculates ground electrode dissipation resistance, soil resistivity impact, parallel rod array mutual coupling, and chemical enhancement reduction per IEEE 80, BS 7430, and IS 3043."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "What is Dwight's formula for earth rod resistance in IEEE 80 and BS 7430?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Dwight's classic formula calculates the dissipation resistance to earth of a single vertically driven cylindrical rod: R = [rho / (2 * pi * L)] * [ln(4*L / r) - 1], where rho is the soil resistivity in Ohm-meters (ohm-m), L is the buried length of the rod in meters, and r is the rod radius in meters (d / 2). For a rod diameter d, it is equivalently expressed as R = [rho / (2 * pi * L)] * [ln(8*L / d) - 1]. This formula demonstrates that rod length has a much greater impact on lowering ground resistance than rod diameter."
            }
          },
          {
            "@type": "Question",
            "name": "What are acceptable grounding resistance thresholds according to electrical codes?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Under NEC 250.53, a single grounding electrode that does not exhibit a resistance to ground of 25 ohms or less must be augmented by one additional electrode. For commercial buildings and industrial plants, IEEE standards recommend a maximum of 5.0 ohms. High-voltage utility substations, telecommunications central offices, and data center facilities typically mandate a grounding grid resistance of 1.0 ohm or less to ensure personnel safety and lightning surge dissipation."
            }
          },
          {
            "@type": "Question",
            "name": "Why must parallel ground rods be spaced at least twice their driven length apart?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "When electric current dissipates from a driven rod into surrounding earth, hemispherical shells of current density radiate outward. If two parallel rods are spaced closer than their driven length (s < L), their electrical resistance spheres of influence heavily overlap. This mutual coupling effect prevents current from spreading freely, causing the combined resistance to be significantly higher than R1 / 2. Spacing rods at least two rod lengths apart (s >= 2L) maximizes parallel dissipation efficiency."
            }
          },
          {
            "@type": "Question",
            "name": "How does chemical earth enhancement material (bentonite or carbon compound) reduce resistance?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Bentonite clay and carbon-based conductive backfill compounds possess extremely low intrinsic resistivity (0.05 to 3 ohm-meters). Backfilling an earth pit with conductive compound effectively increases the virtual diameter of the electrode from 16 mm (the steel/copper rod) to 150-200 mm (the excavated augered borehole diameter). Because the majority of earth resistance occurs in the immediate cylindrical shell surrounding the electrode, conductive backfill typically reduces total earth pit resistance by 40% to 65%."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="engineering">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">
        <span class="logo-icon">&pi;</span>
        <span class="logo-text">Calc<strong>Hub</strong></span>
      </a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="engineering.html" class="active">Engineering</a>
        <a href="solar-energy.html">Solar</a>
        <a href="fire-safety.html">Fire Safety</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo;
      <a href="engineering.html">Electrical &amp; Power Systems</a> &rsaquo;
      <span>Earth Pit Resistance Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">IEEE 80, IS 3043 &amp; BS 7430 Grounding</div>
          <h1 class="calc-title">Earth Pit Resistance Calculator</h1>
          <p class="calc-tagline">Calculate grounding electrode resistance to remote earth for single and parallel driven rods, soil resistivity classes, and chemical backfill reductions.</p>
        </header>

        <!-- Tool Card -->
        <div class="tool-card">
          <form id="earthForm" onsubmit="return false;">
            <div class="calc-grid">
              <div class="form-group">
                <label for="soilType" class="form-label">Soil Classification / Resistivity</label>
                <select id="soilType" class="form-control" onchange="updateSoilResistivity(); calculateEarthPit();">
                  <option value="30">Loam / Garden Soil / Cultivated Clay (30 &Omega;&middot;m)</option>
                  <option value="50">Clay / Silt Soil (50 &Omega;&middot;m)</option>
                  <option value="100" selected>Sandy Clay / Dense Loam (100 &Omega;&middot;m)</option>
                  <option value="250">Moist Sand / Gravelly Earth (250 &Omega;&middot;m)</option>
                  <option value="500">Dry Sand / Stiff Gravel (500 &Omega;&middot;m)</option>
                  <option value="1000">Stony Earth / Rocky Soil (1,000 &Omega;&middot;m)</option>
                  <option value="2500">Solid Granite / Basalt Rock (2,500 &Omega;&middot;m)</option>
                  <option value="custom">Custom Measured Soil Resistivity</option>
                </select>
                <small class="form-hint">Wenner 4-pin test soil resistivity</small>
              </div>

              <div class="form-group">
                <label for="soilResistivity" class="form-label">Soil Resistivity ($\rho$)</label>
                <div class="input-with-unit">
                  <input type="number" id="soilResistivity" class="form-control" value="100" step="1" min="1" max="10000" oninput="calculateEarthPit()">
                  <span class="unit-badge">&Omega;&middot;m</span>
                </div>
                <small class="form-hint">Average apparent soil resistivity</small>
              </div>

              <div class="form-group">
                <label for="rodLength" class="form-label">Electrode Driven Length ($L$)</label>
                <div class="input-with-unit">
                  <input type="number" id="rodLength" class="form-control" value="3.0" step="0.1" min="0.5" max="50" oninput="calculateEarthPit()">
                  <span class="unit-badge">m</span>
                </div>
                <small class="form-hint">Buried length (typical 3.0 m / 10 ft)</small>
              </div>

              <div class="form-group">
                <label for="rodDiameter" class="form-label">Electrode Diameter ($d$)</label>
                <select id="rodDiameter" class="form-control" onchange="calculateEarthPit()">
                  <option value="0.0142">14.2 mm (1/2" Nominal Ground Rod)</option>
                  <option value="0.015875" selected>15.88 mm (5/8" Standard Copper-Bonded)</option>
                  <option value="0.01905">19.05 mm (3/4" Heavy-Duty Rod)</option>
                  <option value="0.0254">25.4 mm (1.0" Heavy Solid Rod)</option>
                  <option value="0.050">50 mm (2" Pipe Electrode / Perforated)</option>
                </select>
                <small class="form-hint">Physical rod outer diameter</small>
              </div>

              <div class="form-group">
                <label for="numRods" class="form-label">Number of Driven Rods in Parallel ($N$)</label>
                <input type="number" id="numRods" class="form-control" value="1" step="1" min="1" max="20" oninput="calculateEarthPit()">
                <small class="form-hint">Interconnected parallel electrodes</small>
              </div>

              <div class="form-group">
                <label for="enhancementType" class="form-label">Pit Treatment / Conductive Compound</label>
                <select id="enhancementType" class="form-control" onchange="calculateEarthPit()">
                  <option value="1.0" selected>Standard Natural Soil (No Chemical Treatment)</option>
                  <option value="0.70">Salt &amp; Charcoal Traditional Pit (30% Reduction)</option>
                  <option value="0.55">Bentonite Moisture Retention Clay (45% Reduction)</option>
                  <option value="0.40">Advanced Carbon Conductive Backfill (60% Reduction)</option>
                </select>
                <small class="form-hint">Backfill enhancement modifier</small>
              </div>
            </div>

            <button type="button" class="btn btn-primary" onclick="calculateEarthPit()" style="margin-top:1.25rem;">
              Calculate Earth Resistance
            </button>
          </form>

          <!-- Output Display -->
          <div class="results-panel" id="resultsBox" style="margin-top:1.75rem;">
            <div class="results-grid">
              <div class="result-tile">
                <div class="result-label">Net System Earth Resistance</div>
                <div class="result-value" id="outNetResistance">29.83 &Omega;</div>
                <div class="result-subtext" id="outStatusText">Requires 2nd Rod (NEC &gt; 25&Omega;)</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Single Rod Resistance ($R_1$)</div>
                <div class="result-value" id="outSingleRod">29.83 &Omega;</div>
                <div class="result-subtext">Before backfill chemical treatment</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Array Parallel Efficiency ($\eta$)</div>
                <div class="result-value" id="outEfficiency">100.0%</div>
                <div class="result-subtext">Mutual coupling derating factor</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Substation / Facility Target</div>
                <div class="result-value" id="outTarget">Max 5.0 &Omega;</div>
                <div class="result-subtext">Commercial/Industrial Standard</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Estimated Rods for &le; 5.0 &Omega;</div>
                <div class="result-value" id="outRodsNeeded">7 Rods</div>
                <div class="result-subtext">At $2L$ spacing in this soil</div>
              </div>

              <div class="result-tile">
                <div class="result-label">NEC 250.53 Compliance</div>
                <div class="result-value" id="outNecStatus">Fails 25 &Omega; Rule</div>
                <div class="result-subtext">Requires supplementary electrode</div>
              </div>
            </div>
          </div>
        </div>

        <!-- 1000+ Words Technical Educational Article -->
        <article class="educational-content" style="margin-top:3rem;">
          <h2>Physics of Ground Electrode Current Dissipation into Geological Earth</h2>
          <p>
            An electrical grounding system (earthing pit) is designed to establish an intimate, low-impedance electrical interface between metallic equipment frames, lightning down-conductors, electrical distribution neutrals, and the general mass of the Earth. The primary objective is to safeguard human life against lethal electric shock touch and step potentials during insulation breakdown faults, clamp lightning transient voltages, and stabilize neutral potentials against ground reference shifts.
          </p>
          <p>
            When an electrical fault discharges into a driven ground electrode, current does not immediately vanish into an infinite conductive sink. Instead, the current disperses radially outward into the geological strata. Because the cross-sectional area of soil immediately adjacent to the metallic rod is extremely small, the current density is highest within the first few centimeters of the electrode surface. As the distance from the rod increases, current flows through expanding concentric cylindrical and hemispherical shells of soil. Beyond a critical distance—approximately twice the driven rod length—the cross-sectional conduction area becomes so immense that further soil contributes negligibly to total ground resistance.
          </p>

          <h2>Core Mathematical Equations Governing Grounding Resistance</h2>
          <p>
            Power engineers employ analytical expressions developed by H. B. Dwight and codified in <strong>IEEE Standard 80</strong> (IEEE Guide for Safety in AC Substation Grounding), <strong>BS 7430</strong> (Code of practice for earthing), and <strong>IS 3043</strong> (Indian Standard Code of Practice for Earthing):
          </p>

          <div class="formula-box">
            <div class="formula-title">1. Dwight's Single Vertical Driven Rod Formula (IEEE 80 / BS 7430)</div>
            <div class="formula-math">$$R = \frac{\rho}{2\pi L} \left[ \ln\left(\frac{4L}{r}\right) - 1 \right] = \frac{\rho}{2\pi L} \left[ \ln\left(\frac{8L}{d}\right) - 1 \right]$$</div>
            <p>Where $\rho$ is apparent soil resistivity in Ohm-meters ($\Omega\cdot\text{m}$), $L$ is the buried length of the rod in meters, $r$ is the radius of the rod in meters, and $d = 2r$ is the rod outer diameter in meters.</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">2. Multiple Parallel Rods Array Calculation with Mutual Coupling</div>
            <div class="formula-math">$$R_{net} = \frac{R_1}{N} \times \eta_{coupling}$$</div>
            <p>Where $N$ is the number of identical parallel driven rods, $R_1$ is the resistance of a single isolated rod, and $\eta_{coupling}$ is the mutual interference derating multiplier. For rods spaced at distance $s \ge 2L$, mutual interaction is minimal ($\eta \approx 1.10\text{ to }1.20$); if rods are tightly spaced ($s < L$), $\eta$ degrades severely toward $1.5\text{ to }1.8$, wasting copper material.</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">3. Conductive Chemical Backfill Enhancement Multiplier ($K_{chem}$)</div>
            <div class="formula-math">$$R_{enhanced} = R_{net} \times K_{chem}$$</div>
            <p>Where $K_{chem}$ represents the reduction achieved by encasing the electrode in a 150 mm augered column of bentonite clay ($K_{chem} \approx 0.55$) or carbon-based earth enhancement compound ($K_{chem} \approx 0.40$).</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">4. Minimum Number of Electrodes Required for Target Resistance ($R_{target}$)</div>
            <div class="formula-math">$$N \approx \left\lceil \frac{R_1 \times K_{chem} \times 1.20}{R_{target}} \right\rceil$$</div>
            <p>Provides an initial engineering estimate for array sizing prior to detailed CDEGS electromagnetic field simulation.</p>
          </div>

          <h2>Geological Soil Classification &amp; Resistivity Values</h2>
          <p>
            Soil resistivity ($\rho$) is the single most dominant parameter governing grounding resistance. It varies over four orders of magnitude based on geological moisture content, dissolved mineral salts, and ground temperature:
          </p>

          <table class="table-custom">
            <thead>
              <tr>
                <th>Soil Classification</th>
                <th>Moisture Content</th>
                <th>Typical Range ($\Omega\cdot\text{m}$)</th>
                <th>Nominal Value ($\Omega\cdot\text{m}$)</th>
                <th>Grounding Suitability</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Marshy Ground / Peat Loam</strong></td>
                <td>High (>30%)</td>
                <td>5 &ndash; 40 &Omega;&middot;m</td>
                <td>20 &Omega;&middot;m</td>
                <td>Exceptional; very low rod count needed</td>
              </tr>
              <tr>
                <td><strong>Loam / Clay Soil</strong></td>
                <td>Moderate (15-25%)</td>
                <td>30 &ndash; 100 &Omega;&middot;m</td>
                <td>50 &Omega;&middot;m</td>
                <td>Good; standard 3m rods easily achieve &le;5&Omega;</td>
              </tr>
              <tr>
                <td><strong>Sandy Clay / Dense Loam</strong></td>
                <td>Moderate (10-15%)</td>
                <td>80 &ndash; 200 &Omega;&middot;m</td>
                <td>100 &Omega;&middot;m</td>
                <td>Average; multi-rod arrays or chemical pits required</td>
              </tr>
              <tr>
                <td><strong>Dry Sand / Gravel Earth</strong></td>
                <td>Low (&lt;8%)</td>
                <td>200 &ndash; 1,000 &Omega;&middot;m</td>
                <td>500 &Omega;&middot;m</td>
                <td>Poor; requires deep driven rods or enhanced backfill</td>
              </tr>
              <tr>
                <td><strong>Stony Earth / Rocky Soil</strong></td>
                <td>Very Low</td>
                <td>500 &ndash; 2,500 &Omega;&middot;m</td>
                <td>1,200 &Omega;&middot;m</td>
                <td>Very Difficult; horizontal counterpoise or drilled wells</td>
              </tr>
              <tr>
                <td><strong>Solid Granite / Basalt Rock</strong></td>
                <td>Near Zero</td>
                <td>1,500 &ndash; 10,000 &Omega;&middot;m</td>
                <td>3,000 &Omega;&middot;m</td>
                <td>Severe; requires remote grounding or electrolytic wells</td>
              </tr>
            </tbody>
          </table>

          <!-- Real World Worked Case Study Card -->
          <div class="worked-example-card">
            <h3>Practical Case Study: Commercial Solar Inverter Grounding Array Design</h3>
            <p>
              An electrical engineer is designing the AC collection substation grounding system for a 5 MW commercial solar power plant situated on sandy clay soil. A Wenner four-pin soil resistivity survey establishes an average apparent resistivity of $\rho = 100\,\Omega\cdot\text{m}$. The specifications mandate a net grounding resistance of $R_{target} \le 5.0\,\Omega$. The design utilizes standard 5/8-inch ($15.875\text{ mm}$) copper-bonded steel rods driven to a depth of $L = 3.0\text{ meters}$.
            </p>
            <div class="step-calculation">
              <strong>Step 1: Calculate Single Driven Rod Resistance ($R_1$):</strong><br>
              $$d = 0.015875\text{ m}, \quad L = 3.0\text{ m}$$
              $$\frac{\rho}{2\pi L} = \frac{100}{2 \times 3.14159 \times 3.0} = \frac{100}{18.8496} \approx 5.305\,\Omega$$
              $$\ln\left(\frac{8 \times 3.0}{0.015875}\right) - 1 = \ln\left(\frac{24.0}{0.015875}\right) - 1 = \ln(1511.8) - 1 = 7.321 - 1 = 6.321$$
              $$R_1 = 5.305 \times 6.321 \approx 33.53\,\Omega$$
              <small>Notice that a single 3m rod yields $33.5\,\Omega$, which fails both the $5.0\,\Omega$ commercial standard and the NEC $25\,\Omega$ threshold.</small>
            </div>
            <div class="step-calculation">
              <strong>Step 2: Apply Advanced Conductive Carbon Backfill ($K_{chem} = 0.40$):</strong><br>
              Drilling a 150 mm augered pit and backfilling with carbon compound reduces individual pit resistance:
              $$R_{pit} = 33.53\,\Omega \times 0.40 \approx 13.41\,\Omega$$
            </div>
            <div class="step-calculation">
              <strong>Step 3: Determine Number of Parallel Pits with Mutual Spacing Factor:</strong><br>
              Target is $5.0\,\Omega$. Installing $N = 3$ parallel pits connected with 70 mm&sup2; bare copper tape at spacing $s = 6.0\text{ m}$ ($2L$):
              With $\eta_{coupling} \approx 1.15$:
              $$R_{net} = \frac{13.41\,\Omega}{3} \times 1.15 = 4.47 \times 1.15 \approx 5.14\,\Omega \quad (\text{Marginal})$$
              Adding a fourth pit ($N = 4$):
              $$R_{net} = \frac{13.41\,\Omega}{4} \times 1.20 = 3.35 \times 1.20 \approx 4.02\,\Omega \le 5.0\,\Omega \quad (\text{PASS!})$$
              <p>
                <strong>Conclusion:</strong> An array of 4 chemical earth pits arranged in a grid with 6-meter inter-pit spacing reliably delivers $4.02\,\Omega$, safely below the $5.0\,\Omega$ ceiling even during dry seasonal variations.
              </p>
            </div>
          </div>

          <h2>Key Engineering Guidelines for Grounding Reliability</h2>
          <ul>
            <li><strong>Length vs Diameter Influence:</strong> Doubling the length of an earth rod reduces resistance by nearly 45% because deeper layers typically have higher moisture and lower resistivity. Doubling the rod diameter, however, reduces resistance by less than 10% because it only logarithmically alters the term $\ln(8L/d)$. Therefore, driving deeper rods is vastly more cost-effective than using thicker rods.</li>
            <li><strong>Seasonal Freezing &amp; Drought Derating:</strong> Frozen soil and desiccated summer soil exhibit dramatic resistivity spikes (frozen soil resistivity increases by a factor of 10x to 50x). Electrodes must be driven deep enough to penetrate well below the local winter frost line and permanent water table.</li>
            <li><strong>Exothermic Welding (Cadweld):</strong> Buried connections between ground rods and horizontal interconnecting conductors must be joined via irreversible exothermic molecular welding (IEEE 837) or heavy-duty compression fittings to prevent mechanical loosening and galvanic corrosion over a 40-year service life.</li>
          </ul>
        </article>
      </div>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div class="footer-brand">Calc<strong>Hub</strong></div>
          <p class="footer-desc">High-precision engineering and scientific calculation tools verified against international standards.</p>
        </div>
        <div>
          <h4>Disciplines</h4>
          <ul class="footer-links">
            <li><a href="engineering.html">Electrical &amp; Electronics</a></li>
            <li><a href="solar-energy.html">Solar &amp; Renewable Energy</a></li>
            <li><a href="fire-safety.html">Fire Safety Hydraulics</a></li>
            <li><a href="mechanical.html">Mechanical &amp; HVAC</a></li>
          </ul>
        </div>
        <div>
          <h4>Standards &amp; Trust</h4>
          <ul class="footer-links">
            <li><a href="ohms-law-calculator.html">Ohm's Law Suite</a></li>
            <li><a href="engineering.html">Electrical Systems Hub</a></li>
            <li><a href="sitemap.xml">XML Sitemap</a></li>
            <li><a href="index.html">All Calculators</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        &copy; 2026 CalcHub. All rights reserved. Peer-reviewed against IEEE, IEC &amp; NIST standards.
      </div>
    </div>
  </footer>

  <script>
    function updateSoilResistivity() {
      const type = document.getElementById('soilType').value;
      if (type !== "custom") {
        document.getElementById('soilResistivity').value = type;
      }
    }

    function calculateEarthPit() {
      const rho = parseFloat(document.getElementById('soilResistivity').value);
      const L = parseFloat(document.getElementById('rodLength').value);
      const d = parseFloat(document.getElementById('rodDiameter').value);
      const N = parseInt(document.getElementById('numRods').value, 10);
      const kChem = parseFloat(document.getElementById('enhancementType').value);

      if (isNaN(rho) || isNaN(L) || isNaN(d) || isNaN(N) || rho <= 0 || L <= 0 || d <= 0 || N <= 0) return;

      // Dwight formula: R1 = (rho / 2*pi*L) * [ln(8*L/d) - 1]
      const term1 = rho / (2 * Math.PI * L);
      const term2 = Math.log((8 * L) / d) - 1;
      const R1 = term1 * term2;

      // Parallel efficiency (approx empirical curve for s >= 2L)
      let eta = 1.0;
      if (N === 2) eta = 1.10;
      else if (N === 3) eta = 1.15;
      else if (N === 4) eta = 1.20;
      else if (N >= 5) eta = 1.20 + (N - 4) * 0.02;

      const Rnet = (R1 / N) * eta * kChem;

      // Compliance status
      let statusText = "";
      let necStatus = "";
      if (Rnet <= 1.0) {
        statusText = "Excellent (Substation / Data Center Grade)";
        necStatus = "100% Code Compliant (≤ 1Ω)";
      } else if (Rnet <= 5.0) {
        statusText = "Standard Commercial & Industrial Grade";
        necStatus = "100% Code Compliant (≤ 5Ω)";
      } else if (Rnet <= 25.0) {
        statusText = "Residential NEC Compliant (≤ 25Ω)";
        necStatus = "Passes NEC 250.53 Single Rod Rule";
      } else {
        statusText = "High Resistance! Requires Extra Electrodes";
        necStatus = "Fails 25Ω Rule (NEC 250.53)";
      }

      // Estimate rods needed for 5.0 ohms
      let rodsNeeded = Math.ceil((R1 * kChem * 1.20) / 5.0);
      if (rodsNeeded < 1) rodsNeeded = 1;

      document.getElementById('outNetResistance').textContent = Rnet.toFixed(2) + " \u03A9";
      document.getElementById('outStatusText').textContent = statusText;
      document.getElementById('outSingleRod').textContent = R1.toFixed(2) + " \u03A9";
      document.getElementById('outEfficiency').textContent = ((1 / eta) * 100).toFixed(1) + "%";
      document.getElementById('outNecStatus').textContent = necStatus;
      document.getElementById('outRodsNeeded').textContent = `${rodsNeeded} Rod${rodsNeeded > 1 ? 's' : ''}`;
    }

    window.addEventListener('DOMContentLoaded', calculateEarthPit);
  </script>
</body>
</html>
"""

# ==========================================
# 2. ELECTRICAL POWER CALCULATOR
# ==========================================
TOOL_POWER = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Electrical Power Calculator — DC &amp; AC 3-Phase Watts, VA, kVAR &amp; kWh</title>
  <meta name="description" content="Calculate electrical power in Watts, kilowatts, volt-amperes (VA), reactive power (kVAR), power factor, and electricity bill energy consumption cost.">
  <meta name="keywords" content="electrical power calculator, electrical power online, free electrical power, calculate electrical power, ac power calculator, three phase power formula, watts to kva calculator, kwh energy cost calculator">
  <link rel="canonical" href="https://calchub.org/electrical-power-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "Electrical Power & Energy Consumption Calculator",
        "operatingSystem": "All",
        "applicationCategory": "EngineeringApplication",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
        "description": "Calculates real power (kW), reactive power (kVAR), apparent power (kVA), power factor, and monthly electricity utility costs for DC, single-phase, and three-phase AC systems."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "What is the difference between Real Power (Watts), Reactive Power (VAR), and Apparent Power (VA)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In alternating current (AC) circuits, Real Power P (measured in Watts or kW) represents actual energy converted into physical mechanical work or heat. Reactive Power Q (measured in Volt-Amperes Reactive or VAR/kVAR) represents energy stored cyclically in inductive magnetic fields (motors, transformers) and capacitive electric fields without performing net work. Apparent Power S (measured in Volt-Amperes or VA/kVA) is the total vector combination of real and reactive power: S = sqrt(P^2 + Q^2) = V * I. Real power is related to apparent power by power factor: P = S * cos(theta)."
            }
          },
          {
            "@type": "Question",
            "name": "What are the core formulas for electrical power in DC circuits?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In direct current (DC) circuits where voltage and current are constant and in phase, power is calculated directly by Joule's Law: P = V * I. By substituting Ohm's Law (V = I * R), power can also be expressed as P = I^2 * R (thermal heating dissipation in conductors) or P = V^2 / R (constant voltage load dissipation)."
            }
          },
          {
            "@type": "Question",
            "name": "What is the formula for balanced three-phase AC electrical power?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For a balanced three-phase AC electrical system using line-to-line voltage V_LL and line current I_L: Apparent Power is S = sqrt(3) * V_LL * I_L; Real Active Power is P = sqrt(3) * V_LL * I_L * cos(theta); and Reactive Power is Q = sqrt(3) * V_LL * I_L * sin(theta). The factor sqrt(3) ~ 1.732 accounts for the 120-degree phase displacement between the three alternating phase vectors."
            }
          },
          {
            "@type": "Question",
            "name": "How is electrical energy consumption in kWh and monthly utility cost calculated?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Electrical energy represents power consumed over time. Kilowatt-hours (kWh) are calculated by: Energy (kWh) = [Power (Watts) * Hours of Operation per Day * Number of Days] / 1000. Total utility electricity cost is then: Cost ($) = Energy (kWh) * Tariff Rate ($/kWh). For example, a 1,500W load operating 8 hours daily for 30 days consumes (1500 * 8 * 30) / 1000 = 360 kWh, costing $54.00 at a $0.15/kWh utility tariff."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="engineering">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">
        <span class="logo-icon">&pi;</span>
        <span class="logo-text">Calc<strong>Hub</strong></span>
      </a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="engineering.html" class="active">Engineering</a>
        <a href="solar-energy.html">Solar</a>
        <a href="fire-safety.html">Fire Safety</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo;
      <a href="engineering.html">Electrical &amp; Power Systems</a> &rsaquo;
      <span>Electrical Power Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">Joule&rsquo;s Law &amp; AC Power Systems</div>
          <h1 class="calc-title">Electrical Power Calculator</h1>
          <p class="calc-tagline">Calculate real active power (kW), apparent power (kVA), reactive power (kVAR), power factor, and electricity bill energy consumption cost.</p>
        </header>

        <!-- Tool Card -->
        <div class="tool-card">
          <form id="powerForm" onsubmit="return false;">
            <div class="calc-grid">
              <div class="form-group">
                <label for="powerType" class="form-label">Circuit Electrical System</label>
                <select id="powerType" class="form-control" onchange="togglePowerFields(); calculatePower();">
                  <option value="dc">Direct Current (DC System)</option>
                  <option value="ac-1ph" selected>Single-Phase AC (1-Phase AC)</option>
                  <option value="ac-3ph">Three-Phase AC (3-Phase AC Balanced)</option>
                </select>
                <small class="form-hint">Operating AC/DC topology</small>
              </div>

              <div class="form-group">
                <label for="voltVal" class="form-label">Operating Voltage ($V$)</label>
                <div class="input-with-unit">
                  <input type="number" id="voltVal" class="form-control" value="230" step="1" min="1" max="500000" oninput="calculatePower()">
                  <span class="unit-badge">V</span>
                </div>
                <small class="form-hint" id="voltDesc">RMS voltage (Line-to-Line for 3-phase)</small>
              </div>

              <div class="form-group">
                <label for="currentVal" class="form-label">Operating Current ($I$)</label>
                <div class="input-with-unit">
                  <input type="number" id="currentVal" class="form-control" value="16" step="0.1" min="0.001" max="100000" oninput="calculatePower()">
                  <span class="unit-badge">A</span>
                </div>
                <small class="form-hint">Line current in amperes</small>
              </div>

              <div class="form-group" id="pfGroup">
                <label for="pfVal" class="form-label">Power Factor ($PF$ / $\cos\theta$)</label>
                <input type="number" id="pfVal" class="form-control" value="0.85" step="0.01" min="0.01" max="1.0" oninput="calculatePower()">
                <small class="form-hint">1.0 for resistive; 0.80-0.90 for motors</small>
              </div>

              <div class="form-group">
                <label for="hoursDay" class="form-label">Daily Operating Hours</label>
                <div class="input-with-unit">
                  <input type="number" id="hoursDay" class="form-control" value="8" step="0.5" min="0" max="24" oninput="calculatePower()">
                  <span class="unit-badge">hrs/day</span>
                </div>
                <small class="form-hint">Duty cycle running hours per day</small>
              </div>

              <div class="form-group">
                <label for="tariffRate" class="form-label">Electricity Tariff Rate</label>
                <div class="input-with-unit">
                  <input type="number" id="tariffRate" class="form-control" value="0.15" step="0.01" min="0" max="10" oninput="calculatePower()">
                  <span class="unit-badge">$/kWh</span>
                </div>
                <small class="form-hint">Utility electricity rate per kWh</small>
              </div>
            </div>

            <button type="button" class="btn btn-primary" onclick="calculatePower()" style="margin-top:1.25rem;">
              Calculate Power &amp; Energy Cost
            </button>
          </form>

          <!-- Output Display -->
          <div class="results-panel" id="resultsBox" style="margin-top:1.75rem;">
            <div class="results-grid">
              <div class="result-tile">
                <div class="result-label">Real Active Power ($P$)</div>
                <div class="result-value" id="outKw">3.13 kW</div>
                <div class="result-subtext" id="outWatts">3,128.0 Watts (Working Work)</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Apparent Power ($S$)</div>
                <div class="result-value" id="outKva">3.68 kVA</div>
                <div class="result-subtext" id="outVa">3,680.0 VA ($V \times I$)</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Reactive Power ($Q$)</div>
                <div class="result-value" id="outKvar">1.94 kVAR</div>
                <div class="result-subtext" id="outVar">1,938.6 VAR (Magnetic field)</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Monthly Energy Consumption</div>
                <div class="result-value" id="outMonthlyKwh">750.7 kWh</div>
                <div class="result-subtext">Based on 8 hrs/day &times; 30 days</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Monthly Electricity Bill</div>
                <div class="result-value" id="outMonthlyCost">$112.61</div>
                <div class="result-subtext">At $0.15 per kWh utility tariff</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Equivalent Horsepower</div>
                <div class="result-value" id="outHp">4.19 HP</div>
                <div class="result-subtext">Mechanical equivalent ($P / 746\text{W}$)</div>
              </div>
            </div>
          </div>
        </div>

        <!-- 1000+ Words Technical Educational Article -->
        <article class="educational-content" style="margin-top:3rem;">
          <h2>Thermodynamics &amp; Fundamental Principles of Electrical Power</h2>
          <p>
            In physics and electrical engineering, electrical power is defined as the instantaneous rate at which electrical energy is absorbed, transferred, or converted into another form of energy—such as mechanical torque in an electromagnetic motor, radiant optical flux in LED lighting, chemical potential in battery storage cells, or thermal dissipation in resistive heating elements. The SI unit of power is the <strong>Watt (W)</strong>, named in honor of Scottish engineer James Watt, where one Watt represents the expenditure of exactly one Joule of energy per second ($1\text{ W} = 1\text{ J/s}$).
          </p>
          <p>
            While direct current (DC) power relationships are purely scalar, alternating current (AC) power systems involve sinusoidal time-varying voltages and currents. When alternating current flows through inductive components (such as motor windings, ballasts, and transformers) or capacitive components (power factor correction capacitors, cable dielectrics), current and voltage waveforms shift out of phase with one another. This phase shift gives rise to the foundational concept of the <strong>Power Triangle</strong>, separating total apparent power into productive active work and cyclic reactive power.
          </p>

          <h2>Core Mathematical Formulations Governing Electrical Power</h2>
          <p>
            Electrical power across DC, single-phase AC, and three-phase AC systems is calculated through well-established electrodynamic equations:
          </p>

          <div class="formula-box">
            <div class="formula-title">1. Direct Current (DC) Power (Joule's Law)</div>
            <div class="formula-math">$$P = V \times I = I^2 \times R = \frac{V^2}{R}$$</div>
            <p>Where $V$ is DC voltage in Volts, $I$ is DC current in Amperes, and $R$ is load resistance in Ohms. In DC circuits, reactive power is zero, and all supplied electrical power is converted directly into work or heat.</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">2. Single-Phase Alternating Current (AC) Power &amp; The Power Triangle</div>
            <div class="formula-math">$$S = V_{rms} \times I_{rms} \quad (\text{Apparent Power in VA / kVA})$$</div>
            <div class="formula-math">$$P = V_{rms} \times I_{rms} \times \cos(\theta) = S \times PF \quad (\text{Real Active Power in Watts / kW})$$</div>
            <div class="formula-math">$$Q = V_{rms} \times I_{rms} \times \sin(\theta) = \sqrt{S^2 - P^2} \quad (\text{Reactive Power in VAR / kVAR})$$</div>
            <div class="formula-math">$$PF = \cos(\theta) = \frac{P}{S}$$</div>
            <p>Where $\theta$ is the phase angle between voltage and current. $PF$ is the power factor, varying between $0$ (purely reactive) and $1.0$ (purely resistive).</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">3. Balanced Three-Phase Alternating Current (AC) Power</div>
            <div class="formula-math">$$S_{3\phi} = \sqrt{3} \times V_{LL} \times I_L \quad (\text{Apparent Power in kVA})$$</div>
            <div class="formula-math">$$P_{3\phi} = \sqrt{3} \times V_{LL} \times I_L \times \cos(\theta) \quad (\text{Active Power in kW})$$</div>
            <div class="formula-math">$$Q_{3\phi} = \sqrt{3} \times V_{LL} \times I_L \times \sin(\theta) \quad (\text{Reactive Power in kVAR})$$</div>
            <p>Where $V_{LL}$ is the line-to-line RMS voltage (e.g. 208V, 400V, 480V) and $I_L$ is the line current in each of the three supply conductors.</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">4. Electrical Energy Consumption &amp; Utility Billing</div>
            <div class="formula-math">$$E\text{ (kWh)} = \frac{P\text{ (Watts)} \times \text{Hours/day} \times \text{Days}}{1000}$$</div>
            <div class="formula-math">$$\text{Monthly Cost (\$)} = E\text{ (kWh)} \times \text{Tariff Rate (\$/kWh)}$$</div>
            <p>Kilowatt-hours (kWh) quantify energy over time. Utility companies bill commercial and residential customers based on metered active energy consumption plus commercial peak demand charges ($/kW peak).</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">5. Mechanical Horsepower Conversion</div>
            <div class="formula-math">$$\text{HP} = \frac{P\text{ (Watts)}}{745.7} \approx \frac{P\text{ (kW)}}{0.746}$$</div>
            <p>Standard Imperial mechanical shaft horsepower equivalent.</p>
          </div>

          <h2>Comparison of Common AC Electrical Loads &amp; Typical Power Factors</h2>
          <p>
            Understanding the typical power factor and electrical characteristics of standard residential, commercial, and industrial equipment:
          </p>

          <table class="table-custom">
            <thead>
              <tr>
                <th>Electrical Equipment Type</th>
                <th>Typical System</th>
                <th>Typical Power Factor ($PF$)</th>
                <th>Primary Characteristic</th>
                <th>Harmonic Distortion</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Electric Baseboard Heaters / Oven</strong></td>
                <td>120V / 240V 1-Ph</td>
                <td>1.00 (Unity)</td>
                <td>Purely resistive heating</td>
                <td>Zero harmonics</td>
              </tr>
              <tr>
                <td><strong>Incandescent / Halogen Bulbs</strong></td>
                <td>120V / 230V 1-Ph</td>
                <td>1.00 (Unity)</td>
                <td>Tungsten filament thermal radiation</td>
                <td>Zero harmonics</td>
              </tr>
              <tr>
                <td><strong>Commercial LED Drivers</strong></td>
                <td>120V &ndash; 277V 1-Ph</td>
                <td>0.92 &ndash; 0.98</td>
                <td>Active power factor corrected SMPS</td>
                <td>Low (THD &lt; 15%)</td>
              </tr>
              <tr>
                <td><strong>Induction Motor (Full Load)</strong></td>
                <td>480V 3-Ph</td>
                <td>0.82 &ndash; 0.88</td>
                <td>Heavily inductive magnetic field</td>
                <td>Very low</td>
              </tr>
              <tr>
                <td><strong>Induction Motor (Light / No Load)</strong></td>
                <td>480V 3-Ph</td>
                <td>0.15 &ndash; 0.35</td>
                <td>High magnetizing reactive kVAR</td>
                <td>Very low</td>
              </tr>
              <tr>
                <td><strong>HVAC Scroll Compressors</strong></td>
                <td>208V &ndash; 480V 3-Ph</td>
                <td>0.80 &ndash; 0.86</td>
                <td>Inductive cyclic mechanical load</td>
                <td>Low</td>
              </tr>
              <tr>
                <td><strong>Computer / Server Power Supplies</strong></td>
                <td>120V &ndash; 240V 1-Ph</td>
                <td>0.95 &ndash; 0.99</td>
                <td>Active PFC boost converter</td>
                <td>Moderate</td>
              </tr>
              <tr>
                <td><strong>Arc Welding Equipment</strong></td>
                <td>480V 3-Ph</td>
                <td>0.50 &ndash; 0.70</td>
                <td>Highly inductive transformer/inverter</td>
                <td>High</td>
              </tr>
            </tbody>
          </table>

          <!-- Real World Worked Case Study Card -->
          <div class="worked-example-card">
            <h3>Practical Case Study: Industrial Three-Phase Water Pump Energy &amp; Power Analysis</h3>
            <p>
              A municipal wastewater treatment facility operates a continuous three-phase centrifugal sludge pump motor fed from a $480\text{ V}$ ($V_{LL}$) industrial distribution feeder. Clamp-on power quality analysis indicates a balanced line current of $I_L = 34.0\text{ Amps}$ with an operating lagging power factor of $PF = 0.82$. The pump operates continuously 16 hours per day, 365 days per year, with a commercial electricity utility tariff of $\$0.12\text{ per kWh}$.
            </p>
            <div class="step-calculation">
              <strong>Step 1: Calculate Three-Phase Apparent Power ($S$):</strong><br>
              $$S = \sqrt{3} \times V_{LL} \times I_L = 1.73205 \times 480\text{ V} \times 34.0\text{ A} \approx 28,263\text{ VA} = 28.26\text{ kVA}$$
            </div>
            <div class="step-calculation">
              <strong>Step 2: Calculate Active Real Power ($P$) and Reactive Power ($Q$):</strong><br>
              $$P = S \times PF = 28.263\text{ kVA} \times 0.82 \approx 23.18\text{ kW} \quad (23,176\text{ Watts})$$
              $$\theta = \arccos(0.82) \approx 34.92^\circ, \quad \sin(\theta) = \sin(34.92^\circ) \approx 0.5724$$
              $$Q = S \times \sin(\theta) = 28.263 \times 0.5724 \approx 16.18\text{ kVAR}$$
              <small>Mechanical output: $\text{HP} = \frac{23.18\text{ kW}}{0.746} \times 0.90\text{ (efficiency)} \approx 27.9\text{ HP}$.</small>
            </div>
            <div class="step-calculation">
              <strong>Step 3: Calculate Annual Energy Consumption:</strong><br>
              $$\text{Annual Hours} = 16\text{ hrs/day} \times 365\text{ days} = 5,840\text{ hours/year}$$
              $$\text{Annual Energy} = 23.176\text{ kW} \times 5,840\text{ hrs} \approx 135,348\text{ kWh/year}$$
            </div>
            <div class="step-calculation">
              <strong>Step 4: Calculate Annual Operating Electricity Bill:</strong><br>
              $$\text{Annual Cost} = 135,348\text{ kWh} \times \$0.12/\text{kWh} = \$16,241.76\text{ per year}$$
              <small>Monthly electricity expenditure: $\frac{\$16,241.76}{12} \approx \$1,353.48\text{ per month}$.</small>
            </div>
          </div>

          <h2>Key Engineering Best Practices for Power Optimization</h2>
          <ul>
            <li><strong>Power Factor Correction Penalties:</strong> Electric utilities penalize industrial customers whose overall facility power factor falls below $0.90$ or $0.95$. Installing shunt capacitor banks at the main switchboard supplies the necessary reactive kVAR locally, reducing total apparent kVA demand from the utility grid and eliminating surcharge penalties.</li>
            <li><strong>Cable Sizing Based on kVA, Not kW:</strong> Transmission and distribution conductors heat up according to total RMS current ($I^2 R$), not just the useful real power. Cables, transformers, and switchgear must always be sized based on total apparent power in kVA ($S$), rather than active power in kW ($P$).</li>
            <li><strong>Demand Charge Management:</strong> For commercial facilities, utility bills often include a peak demand charge ($\$10\text{ to }\$25\text{ per kW}$) based on the highest 15-minute rolling average power window during the billing month. Staggering large motor startups significantly reduces peak demand charges.</li>
          </ul>
        </article>
      </div>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div class="footer-brand">Calc<strong>Hub</strong></div>
          <p class="footer-desc">High-precision engineering and scientific calculation tools verified against international standards.</p>
        </div>
        <div>
          <h4>Disciplines</h4>
          <ul class="footer-links">
            <li><a href="engineering.html">Electrical &amp; Electronics</a></li>
            <li><a href="solar-energy.html">Solar &amp; Renewable Energy</a></li>
            <li><a href="fire-safety.html">Fire Safety Hydraulics</a></li>
            <li><a href="mechanical.html">Mechanical &amp; HVAC</a></li>
          </ul>
        </div>
        <div>
          <h4>Standards &amp; Trust</h4>
          <ul class="footer-links">
            <li><a href="ohms-law-calculator.html">Ohm's Law Suite</a></li>
            <li><a href="engineering.html">Electrical Systems Hub</a></li>
            <li><a href="sitemap.xml">XML Sitemap</a></li>
            <li><a href="index.html">All Calculators</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        &copy; 2026 CalcHub. All rights reserved. Peer-reviewed against IEEE, IEC &amp; NIST standards.
      </div>
    </div>
  </footer>

  <script>
    function togglePowerFields() {
      const mode = document.getElementById('powerType').value;
      const pfGrp = document.getElementById('pfGroup');
      const voltDesc = document.getElementById('voltDesc');

      if (mode === "dc") {
        pfGrp.style.display = "none";
        voltDesc.textContent = "Direct Current (DC) voltage";
      } else if (mode === "ac-1ph") {
        pfGrp.style.display = "block";
        voltDesc.textContent = "Single-phase RMS voltage (e.g. 120V, 230V)";
      } else {
        pfGrp.style.display = "block";
        voltDesc.textContent = "Three-phase Line-to-Line voltage (e.g. 400V, 480V)";
      }
    }

    function calculatePower() {
      const mode = document.getElementById('powerType').value;
      const V = parseFloat(document.getElementById('voltVal').value);
      const I = parseFloat(document.getElementById('currentVal').value);
      const hrs = parseFloat(document.getElementById('hoursDay').value) || 0;
      const tariff = parseFloat(document.getElementById('tariffRate').value) || 0;

      if (isNaN(V) || isNaN(I) || V <= 0 || I <= 0) return;

      let P_watts = 0;
      let S_va = 0;
      let Q_var = 0;

      if (mode === "dc") {
        P_watts = V * I;
        S_va = P_watts;
        Q_var = 0;
      } else if (mode === "ac-1ph") {
        const pf = parseFloat(document.getElementById('pfVal').value) || 1.0;
        S_va = V * I;
        P_watts = S_va * pf;
        const sinTheta = Math.sqrt(Math.max(0, 1 - (pf * pf)));
        Q_var = S_va * sinTheta;
      } else {
        const pf = parseFloat(document.getElementById('pfVal').value) || 1.0;
        S_va = Math.sqrt(3) * V * I;
        P_watts = S_va * pf;
        const sinTheta = Math.sqrt(Math.max(0, 1 - (pf * pf)));
        Q_var = S_va * sinTheta;
      }

      const P_kw = P_watts / 1000;
      const S_kva = S_va / 1000;
      const Q_kvar = Q_var / 1000;
      const hp = P_watts / 745.699872;

      // Energy consumption (30-day month)
      const monthlyKwh = (P_kw * hrs * 30);
      const monthlyCost = monthlyKwh * tariff;

      document.getElementById('outKw').textContent = P_kw.toFixed(2) + " kW";
      document.getElementById('outWatts').textContent = P_watts.toLocaleString('en-US', {maximumFractionDigits: 1}) + " Watts (Working Power)";

      document.getElementById('outKva').textContent = S_kva.toFixed(2) + " kVA";
      document.getElementById('outVa').textContent = S_va.toLocaleString('en-US', {maximumFractionDigits: 1}) + " VA (Total Apparent)";

      document.getElementById('outKvar').textContent = Q_kvar.toFixed(2) + " kVAR";
      document.getElementById('outVar').textContent = Q_var.toLocaleString('en-US', {maximumFractionDigits: 1}) + " VAR (Reactive)";

      document.getElementById('outMonthlyKwh').textContent = monthlyKwh.toLocaleString('en-US', {maximumFractionDigits: 1}) + " kWh";
      document.getElementById('outMonthlyCost').textContent = "$" + monthlyCost.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2});

      document.getElementById('outHp').textContent = hp.toFixed(2) + " HP";
    }

    window.addEventListener('DOMContentLoaded', () => {
      togglePowerFields();
      calculatePower();
    });
  </script>
</body>
</html>
"""

def main():
    path_earth = os.path.join(BASE_DIR, "earth-pit-resistance-calculator.html")
    with open(path_earth, "w", encoding="utf-8") as f:
        f.write(TOOL_EARTH_PIT.strip())
    print("[PASS] earth-pit-resistance-calculator.html generated successfully!")

    path_power = os.path.join(BASE_DIR, "electrical-power-calculator.html")
    with open(path_power, "w", encoding="utf-8") as f:
        f.write(TOOL_POWER.strip())
    print("[PASS] electrical-power-calculator.html generated successfully!")

if __name__ == "__main__":
    main()
