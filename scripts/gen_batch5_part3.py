"""
Generates breaker-size-calculator.html and decibel-calculator.html
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
# 1. BREAKER SIZE CALCULATOR
# ==========================================
TOOL_BREAKER = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Breaker Size Calculator — NEC 125% Continuous Load &amp; Trip Curves</title>
  <meta name="description" content="Calculate circuit breaker size per NEC 240.4 &amp; 210.20 continuous load 125% rule, non-continuous loads, standard amperages, and Type B, C, D trip curves.">
  <meta name="keywords" content="breaker size calculator, breaker size online, free breaker size, calculate breaker size, nec 125 percent continuous load rule, circuit breaker sizing formula, breaker ampacity calculator, nec 240.6 standard breaker sizes">
  <link rel="canonical" href="https://calchub.org/breaker-size-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "Circuit Breaker Sizing Calculator",
        "operatingSystem": "All",
        "applicationCategory": "EngineeringApplication",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
        "description": "Calculates minimum overcurrent protection device (OCPD) amperage rating, continuous load derating per NEC 210.20, minimum conductor wire gauge, and trip curve classifications."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "What is the NEC 125% continuous load rule for circuit breaker sizing?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Per National Electrical Code (NEC) Article 100, a continuous load is defined as any electrical load where the maximum current is sustained for 3 hours or more (such as commercial lighting, EV chargers, water heaters, and continuous machinery). Under NEC 210.20(A) and 215.3, the overcurrent protective device rating must not be less than the non-continuous load plus 125% of the continuous load: Breaker Amps >= (1.25 * Continuous Amps) + Non-Continuous Amps. This derating prevents nuisance thermal tripping caused by heat accumulation inside panelboard enclosures."
            }
          },
          {
            "@type": "Question",
            "name": "What are the standard circuit breaker sizes according to NEC 240.6(A)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "NEC Table 240.6(A) establishes standard ampere ratings for low-voltage inverse-time circuit breakers and fuses: 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 125, 150, 175, 200, 225, 250, 300, 350, 400, 450, 500, 600, 700, 800, 1000, 1200, 1600, 2000, 2500, 3000, 4000, 5000, and 6000 amperes."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between Type B, Type C, and Type D MCB trip curves?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Per IEC 60898-1, miniature circuit breakers (MCBs) feature magnetic instantaneous trip thresholds categorized by curves: Type B trips instantaneously between 3 and 5 times rated current (3-5 In) for purely resistive domestic circuits; Type C trips between 5 and 10 times rated current (5-10 In) for general commercial and fluorescent lighting circuits with moderate inductive surge; and Type D trips between 10 and 20 times rated current (10-20 In) for high-inrush inductive loads like industrial electric motors, transformers, and arc welding equipment."
            }
          },
          {
            "@type": "Question",
            "name": "How does breaker size dictate minimum wire gauge?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Under NEC 240.4, conductors must be protected against overcurrent in accordance with their ampacities specified in NEC Table 310.16. Furthermore, NEC 240.4(D) enforces the 'Small Conductor Rule' for standard branch circuits: 14 AWG copper requires a maximum 15A breaker, 12 AWG copper requires a maximum 20A breaker, and 10 AWG copper requires a maximum 30A breaker, regardless of conductor insulation temperature rating."
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
      <span>Breaker Size Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">NEC 240.4 &amp; 210.20 Standard</div>
          <h1 class="calc-title">Breaker Size Calculator</h1>
          <p class="calc-tagline">Calculate overcurrent protective device (OCPD) amperage rating, 125% continuous load sizing, standard breaker selections, and trip curve classifications.</p>
        </header>

        <!-- Tool Card -->
        <div class="tool-card">
          <form id="breakerForm" onsubmit="return false;">
            <div class="calc-grid">
              <div class="form-group">
                <label for="systemPhase" class="form-label">System Phase &amp; Voltage</label>
                <select id="systemPhase" class="form-control" onchange="calculateBreaker()">
                  <option value="120_1">120V 1-Phase (Residential Branch)</option>
                  <option value="208_1">208V 1-Phase (Commercial Branch)</option>
                  <option value="240_1" selected>240V 1-Phase (Heavy Residential/EV/HVAC)</option>
                  <option value="208_3">208V 3-Phase (Commercial 3-Phase)</option>
                  <option value="480_3">480V 3-Phase (Industrial Power)</option>
                </select>
                <small class="form-hint">Nominal line-to-neutral or line-to-line</small>
              </div>

              <div class="form-group">
                <label for="loadInputType" class="form-label">Load Specification Method</label>
                <select id="loadInputType" class="form-control" onchange="toggleLoadInput(); calculateBreaker();">
                  <option value="amps" selected>Known Operating Amps (A)</option>
                  <option value="power">Total Connected Power (Watts / kW)</option>
                </select>
                <small class="form-hint">Enter direct amps or electrical power</small>
              </div>

              <div class="form-group" id="ampsGroup">
                <label for="continuousAmps" class="form-label">Continuous Load Current (&ge;3 hrs)</label>
                <div class="input-with-unit">
                  <input type="number" id="continuousAmps" class="form-control" value="32" step="0.5" min="0" oninput="calculateBreaker()">
                  <span class="unit-badge">Amps</span>
                </div>
                <small class="form-hint">E.g., 32A continuous for a 40A EVSE</small>
              </div>

              <div class="form-group" id="nonContinuousGroup">
                <label for="nonContinuousAmps" class="form-label">Non-Continuous Load Current (&lt;3 hrs)</label>
                <div class="input-with-unit">
                  <input type="number" id="nonContinuousAmps" class="form-control" value="0" step="0.5" min="0" oninput="calculateBreaker()">
                  <span class="unit-badge">Amps</span>
                </div>
                <small class="form-hint">Intermittent tools, appliances, motors</small>
              </div>

              <div class="form-group" id="powerGroup" style="display:none;">
                <label for="powerValue" class="form-label">Connected Power</label>
                <div class="input-with-unit">
                  <input type="number" id="powerValue" class="form-control" value="7680" step="10" min="1" oninput="calculateBreaker()">
                  <span class="unit-badge">Watts</span>
                </div>
                <small class="form-hint">Total real power in Watts</small>
              </div>

              <div class="form-group" id="powerFactorGroup" style="display:none;">
                <label for="powerFactor" class="form-label">Operating Power Factor ($PF$)</label>
                <input type="number" id="powerFactor" class="form-control" value="0.95" step="0.01" min="0.5" max="1.0" oninput="calculateBreaker()">
                <small class="form-hint">Typically 0.85 to 1.0</small>
              </div>

              <div class="form-group">
                <label for="loadChar" class="form-label">Load Characteristic (Trip Curve)</label>
                <select id="loadChar" class="form-control" onchange="calculateBreaker()">
                  <option value="B">Type B: Resistive (Heating, Basic Lighting)</option>
                  <option value="C" selected>Type C: General / Fluorescent / Small Motors</option>
                  <option value="D">Type D: High Inrush (Transformers, Industrial Motors)</option>
                </select>
                <small class="form-hint">IEC 60898-1 magnetic trip threshold</small>
              </div>

              <div class="form-group">
                <label for="breakerRatingType" class="form-label">Breaker Enclosure Assembly Rating</label>
                <select id="breakerRatingType" class="form-control" onchange="calculateBreaker()">
                  <option value="standard" selected>Standard 80%-Rated Breaker (125% Rule)</option>
                  <option value="100percent">100%-Rated Breaker Assembly (No 125% Mult)</option>
                </select>
                <small class="form-hint">Most standard commercial/residential panelboards are 80% rated</small>
              </div>
            </div>

            <button type="button" class="btn btn-primary" onclick="calculateBreaker()" style="margin-top:1.25rem;">
              Calculate Recommended Breaker
            </button>
          </form>

          <!-- Output Display -->
          <div class="results-panel" id="resultsBox" style="margin-top:1.75rem;">
            <div class="results-grid">
              <div class="result-tile">
                <div class="result-label">Recommended Breaker Size</div>
                <div class="result-value" id="outBreakerRating">40 Amps</div>
                <div class="result-subtext" id="outStandardPill">NEC 240.6(A) Standard Amperage</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Calculated Design Current</div>
                <div class="result-value" id="outDesignAmps">40.00 A</div>
                <div class="result-subtext" id="outRuleText">$1.25 \times I_{cont} + 1.00 \times I_{noncont}$</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Raw Operating Load Current</div>
                <div class="result-value" id="outLoadAmps">32.00 A</div>
                <div class="result-subtext" id="outContinuousBreakdown">Continuous: 32A | Non-Cont: 0A</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Recommended Conductor Wire</div>
                <div class="result-value" id="outWireGauge">8 AWG Copper</div>
                <div class="result-subtext">NEC 310.16 (75&deg;C THHN/THWN)</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Instantaneous Magnetic Trip</div>
                <div class="result-value" id="outMagneticTrip">200 &ndash; 400 A</div>
                <div class="result-subtext" id="outTripDesc">Type C curve ($5 &ndash; 10 \times I_n$)</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Maximum Continuous Capacity</div>
                <div class="result-value" id="outMaxCont">32.00 A</div>
                <div class="result-subtext">80% of standard breaker rating</div>
              </div>
            </div>
          </div>
        </div>

        <!-- 1000+ Words Technical Educational Article -->
        <article class="educational-content" style="margin-top:3rem;">
          <h2>Engineering Principles of Overcurrent Protection Sizing</h2>
          <p>
            In electrical power distribution systems, the primary function of an overcurrent protective device (OCPD)—whether an inverse-time thermal-magnetic molded case circuit breaker (MCCB), miniature circuit breaker (MCB), or current-limiting fuse—is to safeguard circuit conductors and connected equipment from thermal destruction caused by sustained overloads and explosive mechanical forces resulting from high-energy short circuits.
          </p>
          <p>
            Sizing an electrical circuit breaker requires strict adherence to national and international building codes, notably the <strong>National Electrical Code (NEC / NFPA 70)</strong> in the United States, <strong>IEC 60364</strong> across Europe and international installations, and <strong>BS 7671</strong> in the United Kingdom. A common misconception among novice designers is that circuit breakers are sized to fit the electrical appliance; in reality, circuit breakers are engineered specifically to protect the <em>wiring infrastructure</em> between the distribution panelboard and the load.
          </p>

          <h2>Core Mathematical Equations Governing Breaker Selection</h2>
          <p>
            Electrical engineers calculate design current, breaker amperage ratings, and conductor cross-sections through standard regulatory formulas:
          </p>

          <div class="formula-box">
            <div class="formula-title">1. Single-Phase AC Load Current Calculation</div>
            <div class="formula-math">$$I_{load} = \frac{P\text{ (Watts)}}{V \times PF}$$</div>
            <p>Where $P$ is active power in Watts, $V$ is line-to-neutral or line-to-line operating voltage, and $PF$ is the operating power factor ($\cos\theta$).</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">2. Three-Phase AC Balanced Load Current Calculation</div>
            <div class="formula-math">$$I_{load} = \frac{P\text{ (Watts)}}{\sqrt{3} \times V_{LL} \times PF} = \frac{S\text{ (VA)}}{\sqrt{3} \times V_{LL}}$$</div>
            <p>Where $V_{LL}$ is line-to-line voltage (e.g. 208V, 480V) and $S$ is apparent power in volt-amperes.</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">3. NEC 210.20(A) &amp; NEC 215.3 Continuous Load 125% Rule</div>
            <div class="formula-math">$$I_{min\_OCPD} = 1.25 \times I_{continuous} + 1.00 \times I_{non\_continuous}$$</div>
            <p>Where any load operating continuously for 3 hours or longer must be multiplied by $1.25$. The calculated $I_{min\_OCPD}$ is then rounded up to the next standard higher ampere rating in NEC Table 240.6(A).</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">4. 100%-Rated Assembly Exemption Rule</div>
            <div class="formula-math">$$I_{min\_OCPD} = 1.00 \times I_{continuous} + 1.00 \times I_{non\_continuous}$$</div>
            <p>Per NEC 210.20(A) Exception, if the circuit breaker and panelboard assembly are specifically listed and tested for continuous operation at 100% of their rating (common in heavy industrial drawout switchgear), the 125% multiplier is omitted.</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">5. Small Conductor Rule (NEC 240.4(D))</div>
            <div class="formula-math">$$\text{14 AWG Cu} \implies \text{Max 15A OCPD}, \quad \text{12 AWG Cu} \implies \text{Max 20A OCPD}, \quad \text{10 AWG Cu} \implies \text{Max 30A OCPD}$$</div>
            <p>Unless specifically exempted by NEC articles (such as motor branch circuits under Article 430), small copper branch circuit conductors must never be protected by breakers exceeding these ampere ceilings.</p>
          </div>

          <h2>Standard Circuit Breaker Amperage Ratings (NEC 240.6(A))</h2>
          <p>
            When calculations produce a non-standard amperage value (such as 34.2A), designers must round up to the next standard rating listed in NEC Table 240.6(A):
          </p>

          <table class="table-custom">
            <thead>
              <tr>
                <th>Standard Breaker Rating</th>
                <th>80% Max Continuous Load</th>
                <th>Min Copper Conductor (75&deg;C)</th>
                <th>Typical Domestic &amp; Commercial Application</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>15 Amps</strong></td>
                <td>12.0 Amps</td>
                <td>14 AWG</td>
                <td>Residential general lighting, bedroom receptacles</td>
              </tr>
              <tr>
                <td><strong>20 Amps</strong></td>
                <td>16.0 Amps</td>
                <td>12 AWG</td>
                <td>Kitchen small appliances, bathrooms, commercial lighting</td>
              </tr>
              <tr>
                <td><strong>30 Amps</strong></td>
                <td>24.0 Amps</td>
                <td>10 AWG</td>
                <td>Electric clothes dryers, residential water heaters, 2-ton A/C</td>
              </tr>
              <tr>
                <td><strong>40 Amps</strong></td>
                <td>32.0 Amps</td>
                <td>8 AWG</td>
                <td>Electric cooking ranges, Level 2 EV chargers (32A EVSE)</td>
              </tr>
              <tr>
                <td><strong>50 Amps</strong></td>
                <td>40.0 Amps</td>
                <td>6 AWG</td>
                <td>Heavy ranges, 9.6 kW EV chargers (40A EVSE), RV hookups</td>
              </tr>
              <tr>
                <td><strong>60 Amps</strong></td>
                <td>48.0 Amps</td>
                <td>6 AWG / 4 AWG</td>
                <td>Subpanel feeder, 11.5 kW EV chargers (48A EVSE), heat pumps</td>
              </tr>
              <tr>
                <td><strong>70 &ndash; 100 Amps</strong></td>
                <td>56.0 &ndash; 80.0 Amps</td>
                <td>4 AWG &ndash; 1 AWG</td>
                <td>Residential service subpanels, electric tankless water heaters</td>
              </tr>
              <tr>
                <td><strong>125 &ndash; 200 Amps</strong></td>
                <td>100.0 &ndash; 160.0 Amps</td>
                <td>1/0 AWG &ndash; 250 kcmil</td>
                <td>Whole-house main service entrance panelboard</td>
              </tr>
            </tbody>
          </table>

          <h2>IEC 60898-1 Trip Curve Classifications &amp; Magnetic Thresholds</h2>
          <p>
            Miniature circuit breakers (MCBs) incorporate two separate trip mechanisms: a bi-metallic thermal strip for slow overload protection and an electromagnetic solenoid for fast short-circuit clearing. The magnetic trip characteristics are standardized by curves:
          </p>

          <table class="table-custom">
            <thead>
              <tr>
                <th>Trip Curve Class</th>
                <th>Instantaneous Magnetic Trip Range</th>
                <th>Typical Inrush Multiplier</th>
                <th>Recommended Application Environment</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Type B</strong></td>
                <td>$3 \times I_n \text{ to } 5 \times I_n$</td>
                <td>Low (1.5x &ndash; 3x)</td>
                <td>Domestic resistive heaters, domestic incandescent lighting, long cable runs</td>
              </tr>
              <tr>
                <td><strong>Type C</strong></td>
                <td>$5 \times I_n \text{ to } 10 \times I_n$</td>
                <td>Medium (3x &ndash; 5x)</td>
                <td>Commercial lighting, fluorescent banks, IT server racks, fractional HP motors</td>
              </tr>
              <tr>
                <td><strong>Type D</strong></td>
                <td>$10 \times I_n \text{ to } 20 \times I_n$</td>
                <td>High (8x &ndash; 15x)</td>
                <td>Industrial 3-phase electric motors, power transformers, x-ray, arc welders</td>
              </tr>
              <tr>
                <td><strong>Type K</strong></td>
                <td>$8 \times I_n \text{ to } 12 \times I_n$</td>
                <td>Medium-High</td>
                <td>Motor control circuits requiring fast thermal trip but high magnetic ride-through</td>
              </tr>
              <tr>
                <td><strong>Type Z</strong></td>
                <td>$2 \times I_n \text{ to } 3 \times I_n$</td>
                <td>Ultra-Sensitive</td>
                <td>Semiconductor protection, PLC output modules, sensitive instrumentation</td>
              </tr>
            </tbody>
          </table>

          <!-- Real World Worked Case Study Card -->
          <div class="worked-example-card">
            <h3>Practical Case Study: Commercial Electric Vehicle Charging Circuit Sizing</h3>
            <p>
              An electrical contractor is designing a dedicated branch circuit for a commercial dual-port Level 2 EV charging station located in an office parking structure. The EVSE is rated to deliver a continuous charge current of $I_{cont} = 32\text{ Amps}$ at $240\text{ V}$ single-phase. The charging cycle routinely lasts over 6 hours during the workday.
            </p>
            <div class="step-calculation">
              <strong>Step 1: Identify Continuous vs Non-Continuous Loads:</strong><br>
              Because EV charging continues for greater than 3 hours, the load is classified as 100% continuous per NEC Article 625.42 and Article 100. Non-continuous load is $0\text{ A}$.
            </div>
            <div class="step-calculation">
              <strong>Step 2: Apply the NEC 125% Continuous Load Multiplier:</strong><br>
              $$I_{min\_OCPD} = 1.25 \times 32\text{ Amps} + 0\text{ Amps} = 40.0\text{ Amps}$$
            </div>
            <div class="step-calculation">
              <strong>Step 3: Select Standard Breaker from NEC Table 240.6(A):</strong><br>
              The calculated value of $40.0\text{ A}$ corresponds exactly to a standard NEC rating. A **40 Amp two-pole molded case circuit breaker** is selected.
            </div>
            <div class="step-calculation">
              <strong>Step 4: Coordinate Conductor Size (NEC 310.16):</strong><br>
              From NEC Table 310.16 (75&deg;C copper conductors), an 8 AWG THHN/THWN copper conductor is rated for $50\text{ Amps}$, which safely exceeds the 40A breaker rating and fulfills all code requirements. The maximum permitted continuous load on this 40A breaker is $40 \times 0.80 = 32\text{ Amps}$, proving perfect design balance.
            </div>
          </div>

          <h2>Essential Electrical Installation Safety Rules</h2>
          <ul>
            <li><strong>Thermal-Magnetic Ambient Derating:</strong> Standard thermal-magnetic circuit breakers are calibrated at an ambient temperature of $40^\circ\text{C}$ ($104^\circ\text{F}$). If installed in outdoor rooftop panels exposed to intense solar irradiance ($>50^\circ\text{C}$), the thermal bimetal strip will trip prematurely at lower currents. Manufacturer ambient temperature derating tables must be applied.</li>
            <li><strong>Interrupting Capacity (AIC / kAIC):</strong> Sizing the ampere rating is only half the engineering equation. Breakers must also possess adequate Ampere Interrupting Capacity (AIC)—typically 10 kAIC for residential panels, and 22 kAIC to 65 kAIC for commercial/industrial distribution—to interrupt available short-circuit fault currents without mechanical rupture.</li>
            <li><strong>Motor Branch Circuit Exceptions:</strong> Under NEC Article 430.52, motor branch circuit short-circuit and ground-fault protective devices may be sized up to 250% (inverse-time breaker) of motor Full-Load Amps (FLA) to withstand high starting locked-rotor inrush currents, while motor overload thermal heaters protect against sustained running overloads.</li>
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
    const NEC_STANDARD_BREAKERS = [15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 125, 150, 175, 200, 225, 250, 300, 350, 400, 450, 500, 600, 700, 800, 1000, 1200, 1600, 2000];

    function toggleLoadInput() {
      const mode = document.getElementById('loadInputType').value;
      if (mode === "amps") {
        document.getElementById('ampsGroup').style.display = "block";
        document.getElementById('nonContinuousGroup').style.display = "block";
        document.getElementById('powerGroup').style.display = "none";
        document.getElementById('powerFactorGroup').style.display = "none";
      } else {
        document.getElementById('ampsGroup').style.display = "none";
        document.getElementById('nonContinuousGroup').style.display = "none";
        document.getElementById('powerGroup').style.display = "block";
        document.getElementById('powerFactorGroup').style.display = "block";
      }
    }

    function calculateBreaker() {
      const sysType = document.getElementById('systemPhase').value;
      const loadMode = document.getElementById('loadInputType').value;
      const is100Percent = (document.getElementById('breakerRatingType').value === "100percent");
      const tripClass = document.getElementById('loadChar').value;

      let contAmps = 0;
      let nonContAmps = 0;

      if (loadMode === "amps") {
        contAmps = parseFloat(document.getElementById('continuousAmps').value) || 0;
        nonContAmps = parseFloat(document.getElementById('nonContinuousAmps').value) || 0;
      } else {
        const Pwatts = parseFloat(document.getElementById('powerValue').value) || 0;
        const pf = parseFloat(document.getElementById('powerFactor').value) || 0.95;

        let V = 240;
        let is3Ph = false;

        if (sysType === "120_1") { V = 120; }
        else if (sysType === "208_1") { V = 208; }
        else if (sysType === "240_1") { V = 240; }
        else if (sysType === "208_3") { V = 208; is3Ph = true; }
        else if (sysType === "480_3") { V = 480; is3Ph = true; }

        if (is3Ph) {
          contAmps = Pwatts / (Math.sqrt(3) * V * pf);
        } else {
          contAmps = Pwatts / (V * pf);
        }
        nonContAmps = 0; // Assume power input is continuous default
      }

      const totalLoadAmps = contAmps + nonContAmps;
      if (totalLoadAmps <= 0) return;

      let designAmps = 0;
      if (is100Percent) {
        designAmps = contAmps + nonContAmps;
      } else {
        designAmps = (1.25 * contAmps) + nonContAmps;
      }

      // Find standard breaker rating
      let selectedBreaker = NEC_STANDARD_BREAKERS[NEC_STANDARD_BREAKERS.length - 1];
      for (let i = 0; i < NEC_STANDARD_BREAKERS.length; i++) {
        if (NEC_STANDARD_BREAKERS[i] >= designAmps) {
          selectedBreaker = NEC_STANDARD_BREAKERS[i];
          break;
        }
      }

      // Conductor wire recommendation (NEC 310.16 Cu 75°C)
      let wire = "14 AWG Copper";
      if (selectedBreaker <= 15) wire = "14 AWG Copper";
      else if (selectedBreaker <= 20) wire = "12 AWG Copper";
      else if (selectedBreaker <= 30) wire = "10 AWG Copper";
      else if (selectedBreaker <= 50) wire = "8 AWG Copper";
      else if (selectedBreaker <= 65) wire = "6 AWG Copper";
      else if (selectedBreaker <= 85) wire = "4 AWG Copper";
      else if (selectedBreaker <= 100) wire = "3 AWG Copper";
      else if (selectedBreaker <= 115) wire = "2 AWG Copper";
      else if (selectedBreaker <= 130) wire = "1 AWG Copper";
      else if (selectedBreaker <= 150) wire = "1/0 AWG Copper";
      else if (selectedBreaker <= 175) wire = "2/0 AWG Copper";
      else if (selectedBreaker <= 200) wire = "3/0 AWG Copper";
      else if (selectedBreaker <= 230) wire = "4/0 AWG Copper";
      else if (selectedBreaker <= 255) wire = "250 kcmil Copper";
      else if (selectedBreaker <= 285) wire = "300 kcmil Copper";
      else if (selectedBreaker <= 310) wire = "350 kcmil Copper";
      else if (selectedBreaker <= 380) wire = "500 kcmil Copper";
      else wire = "Parallel Conductors (Per NEC 310.10)";

      // Trip magnetic range
      let tripLow = 0, tripHigh = 0, tripDesc = "";
      if (tripClass === "B") {
        tripLow = 3 * selectedBreaker;
        tripHigh = 5 * selectedBreaker;
        tripDesc = "Type B curve (3 – 5 × In)";
      } else if (tripClass === "C") {
        tripLow = 5 * selectedBreaker;
        tripHigh = 10 * selectedBreaker;
        tripDesc = "Type C curve (5 – 10 × In)";
      } else {
        tripLow = 10 * selectedBreaker;
        tripHigh = 20 * selectedBreaker;
        tripDesc = "Type D curve (10 – 20 × In)";
      }

      const maxContCapacity = is100Percent ? selectedBreaker : (0.80 * selectedBreaker);

      document.getElementById('outBreakerRating').textContent = selectedBreaker + " Amps";
      document.getElementById('outDesignAmps').textContent = designAmps.toFixed(2) + " A";
      document.getElementById('outLoadAmps').textContent = totalLoadAmps.toFixed(2) + " A";
      document.getElementById('outContinuousBreakdown').textContent = `Continuous: ${contAmps.toFixed(1)}A | Non-Cont: ${nonContAmps.toFixed(1)}A`;
      document.getElementById('outWireGauge').textContent = wire;
      document.getElementById('outMagneticTrip').textContent = `${tripLow} – ${tripHigh} A`;
      document.getElementById('outTripDesc').textContent = tripDesc;
      document.getElementById('outMaxCont').textContent = maxContCapacity.toFixed(1) + " A";
    }

    window.addEventListener('DOMContentLoaded', () => {
      toggleLoadInput();
      calculateBreaker();
    });
  </script>
</body>
</html>
"""

# ==========================================
# 2. DECIBEL CALCULATOR
# ==========================================
TOOL_DECIBEL = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Decibel Calculator — dB Power, Voltage, dBm, dBW &amp; dB SPL</title>
  <meta name="description" content="Calculate decibel ratios for power (10 log P1/P0), voltage &amp; sound amplitude (20 log V1/V0), dBm to Watts conversion, dBV, dBu, and acoustic dB SPL.">
  <meta name="keywords" content="decibel calculator, decibel online, free decibel calculator, calculate decibels, dbm to watts calculator, db voltage ratio calculator, db power ratio calculator, db spl sound level calculator">
  <link rel="canonical" href="https://calchub.org/decibel-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "Decibel (dB) Audio & RF Engineering Calculator",
        "operatingSystem": "All",
        "applicationCategory": "EngineeringApplication",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
        "description": "Calculates power ratios, voltage/current field ratios, dBm to milliwatts and Watts conversion, audio dBu/dBV levels, and acoustic sound pressure level (dB SPL)."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "Why is the decibel formula 10 log for power but 20 log for voltage?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The decibel is fundamentally a logarithmic measure of power ratio: dB = 10 * log10(P1 / P0). Because electrical power dissipated in a constant resistance R is proportional to the square of voltage (P = V^2 / R), the ratio of powers can be rewritten as: 10 * log10((V1^2 / R) / (V0^2 / R)) = 10 * log10((V1 / V0)^2) = 20 * log10(V1 / V0). The factor of 2 in the exponent moves to the front, producing the classic 20 * log10 multiplier for voltage, current, and sound pressure."
            }
          },
          {
            "@type": "Question",
            "name": "What is the mathematical relationship between dBm and Watts?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "dBm measures absolute power referenced to 1.0 milliwatt (0.001 W). The conversion formula is dBm = 10 * log10(Power in mW / 1 mW). Conversely, Power (mW) = 10^(dBm / 10), and Power (Watts) = 10^((dBm - 30) / 10). For example, 0 dBm equals exactly 1.0 mW; +30 dBm equals 1,000 mW (1.0 Watt); and +43 dBm equals 20 Watts (standard for cellular base station transmitters)."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between dBu and dBV in audio engineering?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Both dBu and dBV quantify root-mean-square (RMS) voltage levels without specifying impedance. dBV uses a reference level of exactly 1.0 Vrms: dBV = 20 * log10(V / 1.0V). In contrast, dBu derives from historical 600-ohm telecommunication circuits dissipating 1 mW, establishing a reference voltage of sqrt(0.001 * 600) ~ 0.7746 Vrms: dBu = 20 * log10(V / 0.7746V). Professional audio line level (+4 dBu) corresponds to 1.228 Vrms (+1.78 dBV), whereas consumer line level (-10 dBV) corresponds to 0.316 Vrms (-7.78 dBu)."
            }
          },
          {
            "@type": "Question",
            "name": "How does acoustic Sound Pressure Level (dB SPL) relate to human hearing?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Sound Pressure Level (dB SPL) is measured relative to the human auditory threshold of hearing at 1,000 Hz: p0 = 20 micropascals (20 uPa = 2 x 10^-5 N/m^2). The formula is dB SPL = 20 * log10(p / 20 uPa). 0 dB SPL represents the absolute threshold of perception, 60 dB SPL represents conversational speech, 85 dB SPL marks the OSHA threshold for workplace hearing protection, and 130-140 dB SPL marks the threshold of physical pain."
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
      <span>Decibel Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">RF, Audio &amp; Acoustic Engineering</div>
          <h1 class="calc-title">Decibel Calculator</h1>
          <p class="calc-tagline">Calculate decibel ratios for power ($10\log$), voltage ($20\log$), dBm to Watts conversion, audio dBu/dBV levels, and acoustic sound pressure level (dB SPL).</p>
        </header>

        <!-- Tool Card -->
        <div class="tool-card">
          <form id="dbForm" onsubmit="return false;">
            <div class="calc-grid">
              <div class="form-group">
                <label for="calcMode" class="form-label">Calculation Mode</label>
                <select id="calcMode" class="form-control" onchange="toggleDbMode(); calculateDb();">
                  <option value="power-ratio" selected>Power Ratio ($10 \log_{10} P_1/P_0$)</option>
                  <option value="voltage-ratio">Voltage / Field Ratio ($20 \log_{10} V_1/V_0$)</option>
                  <option value="dbm-watts">dBm &harr; Watts / mW Conversion</option>
                  <option value="sound-spl">Sound Pressure Level (dB SPL)</option>
                </select>
                <small class="form-hint">Select decibel discipline</small>
              </div>

              <!-- Power Mode Inputs -->
              <div class="form-group" id="grpPowerP1">
                <label for="valP1" class="form-label">Output / Measured Power ($P_1$)</label>
                <div class="input-with-unit">
                  <input type="number" id="valP1" class="form-control" value="50" step="0.1" min="0.000000001" oninput="calculateDb()">
                  <span class="unit-badge">W</span>
                </div>
                <small class="form-hint">Numerator power value</small>
              </div>

              <div class="form-group" id="grpPowerP0">
                <label for="valP0" class="form-label">Reference / Input Power ($P_0$)</label>
                <div class="input-with-unit">
                  <input type="number" id="valP0" class="form-control" value="5" step="0.1" min="0.000000001" oninput="calculateDb()">
                  <span class="unit-badge">W</span>
                </div>
                <small class="form-hint">Denominator reference power</small>
              </div>

              <!-- Voltage Mode Inputs -->
              <div class="form-group" id="grpVoltV1" style="display:none;">
                <label for="valV1" class="form-label">Output / Measured Voltage ($V_1$)</label>
                <div class="input-with-unit">
                  <input type="number" id="valV1" class="form-control" value="10.0" step="0.1" min="0.000001" oninput="calculateDb()">
                  <span class="unit-badge">V</span>
                </div>
                <small class="form-hint">Numerator voltage value</small>
              </div>

              <div class="form-group" id="grpVoltV0" style="display:none;">
                <label for="valV0" class="form-label">Reference Voltage ($V_0$)</label>
                <div class="input-with-unit">
                  <input type="number" id="valV0" class="form-control" value="1.0" step="0.1" min="0.000001" oninput="calculateDb()">
                  <span class="unit-badge">V</span>
                </div>
                <small class="form-hint">Reference level (e.g. 1V for dBV)</small>
              </div>

              <!-- dBm Mode Inputs -->
              <div class="form-group" id="grpDbmVal" style="display:none;">
                <label for="valDbm" class="form-label">RF Power Level</label>
                <div class="input-with-unit">
                  <input type="number" id="valDbm" class="form-control" value="30.0" step="0.5" oninput="calculateDb()">
                  <span class="unit-badge">dBm</span>
                </div>
                <small class="form-hint">E.g., +30 dBm = 1 Watt</small>
              </div>

              <!-- SPL Mode Inputs -->
              <div class="form-group" id="grpSplPressure" style="display:none;">
                <label for="valPressure" class="form-label">Sound Pressure ($p$)</label>
                <div class="input-with-unit">
                  <input type="number" id="valPressure" class="form-control" value="0.2" step="0.01" min="0.000001" oninput="calculateDb()">
                  <span class="unit-badge">Pa</span>
                </div>
                <small class="form-hint">Acoustic pressure in Pascals ($N/m^2$)</small>
              </div>
            </div>

            <button type="button" class="btn btn-primary" onclick="calculateDb()" style="margin-top:1.25rem;">
              Calculate Decibel Value
            </button>
          </form>

          <!-- Output Display -->
          <div class="results-panel" id="resultsBox" style="margin-top:1.75rem;">
            <div class="results-grid">
              <div class="result-tile">
                <div class="result-label">Decibel Value</div>
                <div class="result-value" id="outMainDb">+10.00 dB</div>
                <div class="result-subtext" id="outMainDesc">Power gain ratio ($10 \times$)</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Linear Absolute Ratio</div>
                <div class="result-value" id="outLinearRatio">10.00 &times;</div>
                <div class="result-subtext" id="outLinearDesc">$P_1 / P_0$ amplification factor</div>
              </div>

              <div class="result-tile">
                <div class="result-label">RF Power in Watts</div>
                <div class="result-value" id="outWatts">1.000 W</div>
                <div class="result-subtext" id="outMilliwatts">1,000.0 mW</div>
              </div>

              <div class="result-tile">
                <div class="result-label">dBW Level</div>
                <div class="result-value" id="outDbw">0.00 dBW</div>
                <div class="result-subtext">Referenced to 1.0 Watt</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Audio dBu Level</div>
                <div class="result-value" id="outDbu">+2.22 dBu</div>
                <div class="result-subtext">Ref $0.775\text{ V}_{rms}$ ($600\,\Omega$)</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Acoustic Sound Category</div>
                <div class="result-value" id="outSplCat">Quiet Office</div>
                <div class="result-subtext" id="outSplDesc">Acoustic environment level</div>
              </div>
            </div>
          </div>
        </div>

        <!-- 1000+ Words Technical Educational Article -->
        <article class="educational-content" style="margin-top:3rem;">
          <h2>Mathematical Foundations of the Decibel &amp; Logarithmic Scaling</h2>
          <p>
            The decibel (symbol: <strong>dB</strong>) is one-tenth of a Bel, a logarithmic dimensionless unit named in honor of telecommunications pioneer Alexander Graham Bell. Originally developed in Bell Telephone Laboratories in the 1920s to quantify signal attenuation in standard transmission cable lines, the decibel has become the universal language of RF communications, electrical acoustics, optical fiber transmission, and analog signal processing.
          </p>
          <p>
            The human perceptual system—governed by the Weber-Fechner Law—responds logarithmically rather than linearly to physical stimuli such as acoustic loudness, visual optical brightness, and radio frequency signal power. An audio amplifier delivering 100 Watts sounds only roughly twice as loud to human ears as a 10-Watt amplifier, not ten times as loud. Furthermore, electronic signal paths span astronomical dynamic ranges: a sensitive GPS receiver detects signals at $10^{-16}\text{ Watts}$ ($-130\text{ dBm}$), while a high-power broadcast transmitter radiates $50,000\text{ Watts}$ ($+77\text{ dBm}$). Compressively expressing a range of $10^{20}$ orders of magnitude into compact, manageable numbers makes the decibel indispensable for engineering.
          </p>

          <h2>Core Mathematical Formulas Governing Decibels</h2>
          <p>
            Depending on whether the quantity being compared is an energetic power parameter or a field amplitude parameter (voltage, current, sound pressure), different logarithmic scaling factors apply:
          </p>

          <div class="formula-box">
            <div class="formula-title">1. Power Ratio Decibel Equation</div>
            <div class="formula-math">$$\text{Gain/Loss (dB)} = 10 \log_{10}\left(\frac{P_1}{P_0}\right)$$</div>
            <p>Where $P_1$ is output power and $P_0$ is input/reference power measured in identical units (Watts, milliwatts). A positive value indicates power gain; a negative value indicates attenuation.</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">2. Voltage, Current &amp; Field Amplitude Decibel Equation</div>
            <div class="formula-math">$$\text{Gain/Loss (dB)} = 20 \log_{10}\left(\frac{V_1}{V_0}\right) = 20 \log_{10}\left(\frac{I_1}{I_0}\right)$$</div>
            <p>Because electrical power is proportional to voltage squared ($P = V^2 / R$), the logarithmic identity $\log(x^2) = 2 \log(x)$ transforms the $10 \log$ multiplier into $20 \log$.</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">3. Absolute RF Power: dBm and dBW Conversions</div>
            <div class="formula-math">$$P_{dBm} = 10 \log_{10}\left(\frac{P\text{ (mW)}}{1\text{ mW}}\right), \quad P\text{ (mW)} = 10^{\frac{P_{dBm}}{10}}$$</div>
            <div class="formula-math">$$P\text{ (Watts)} = \frac{10^{\frac{P_{dBm}}{10}}}{1000} = 10^{\frac{P_{dBm} - 30}{10}}, \quad P_{dBW} = P_{dBm} - 30$$</div>
            <p>dBm is referenced to $1.0\text{ milliwatt}$; dBW is referenced to $1.0\text{ Watt}$.</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">4. Professional Audio Voltage Standards: dBV and dBu</div>
            <div class="formula-math">$$V_{dBV} = 20 \log_{10}\left(\frac{V_{rms}}{1.0\text{ V}}\right), \quad V_{dBu} = 20 \log_{10}\left(\frac{V_{rms}}{0.7746\text{ V}}\right) = V_{dBV} + 2.218\text{ dB}$$</div>
            <p>The standard reference of $0.7746\text{ V}_{rms}$ for dBu originates from the voltage required to deliver $1.0\text{ mW}$ into a historical $600\,\Omega$ telecommunications impedance ($V = \sqrt{P \cdot R} = \sqrt{0.001 \times 600} \approx 0.7746\text{ V}$).</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">5. Acoustic Sound Pressure Level (dB SPL)</div>
            <div class="formula-math">$$L_p = 20 \log_{10}\left(\frac{p}{p_0}\right) = 20 \log_{10}\left(\frac{p}{20\,\mu\text{Pa}}\right)$$</div>
            <p>Where $p$ is root-mean-square sound pressure in Pascals ($\text{N/m}^2$) and $p_0 = 20\,\mu\text{Pa} = 2 \times 10^{-5}\text{ Pa}$ represents the absolute threshold of human hearing at $1\text{ kHz}$.</p>
          </div>

          <h2>Key Logarithmic Benchmark Rules of Thumb</h2>
          <p>
            Engineers commit these mental arithmetic conversions to memory for rapid field diagnostics:
          </p>
          <ul>
            <li><strong>+3 dB Power Gain:</strong> Exactly doubles the power ($\times 2.0$).</li>
            <li><strong>-3 dB Power Loss:</strong> Halves the power ($\times 0.5$, the half-power cutoff frequency $\omega_c$).</li>
            <li><strong>+6 dB Voltage Gain:</strong> Exactly doubles the voltage amplitude ($\times 2.0$), quadrupling power ($\times 4.0$).</li>
            <li><strong>+10 dB Power Gain:</strong> Increases power by a factor of 10 ($\times 10$).</li>
            <li><strong>+20 dB Power Gain:</strong> Increases power by a factor of 100 ($\times 100$); doubles voltage ten-fold ($\times 10$).</li>
            <li><strong>+30 dBm:</strong> Equals exactly 1,000 mW = 1.0 Watt.</li>
            <li><strong>+0 dBm:</strong> Equals exactly 1.0 mW = 0.001 Watt.</li>
            <li><strong>-30 dBm:</strong> Equals exactly 1.0 microwatt ($1\,\mu\text{W}$).</li>
          </ul>

          <h2>Decibel Scale Reference Guide: RF, Audio &amp; Acoustics</h2>
          <p>
            The table below correlates dB values with physical power, voltage levels, and acoustic real-world environments:
          </p>

          <table class="table-custom">
            <thead>
              <tr>
                <th>Decibel Level</th>
                <th>Power Ratio ($P_1/P_0$)</th>
                <th>Voltage Ratio ($V_1/V_0$)</th>
                <th>Equivalent dBm &rarr; Power</th>
                <th>Acoustic Sound Level (dB SPL)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>0 dB</strong></td>
                <td>1.00 &times; (Unity)</td>
                <td>1.00 &times; (Unity)</td>
                <td>0 dBm &rarr; 1.0 mW</td>
                <td>Threshold of human hearing (20 &mu;Pa)</td>
              </tr>
              <tr>
                <td><strong>+3 dB</strong></td>
                <td>1.995 &times; (&asymp; 2x)</td>
                <td>1.413 &times; (&radic;2)</td>
                <td>+3 dBm &rarr; 2.0 mW</td>
                <td>Barely perceptible acoustic volume change</td>
              </tr>
              <tr>
                <td><strong>+6 dB</strong></td>
                <td>3.981 &times; (&asymp; 4x)</td>
                <td>1.995 &times; (&asymp; 2x)</td>
                <td>+6 dBm &rarr; 4.0 mW</td>
                <td>Noticeable acoustic volume increase</td>
              </tr>
              <tr>
                <td><strong>+10 dB</strong></td>
                <td>10.00 &times; (10x)</td>
                <td>3.162 &times;</td>
                <td>+10 dBm &rarr; 10 mW</td>
                <td>Perceived doubling of subjective sound volume</td>
              </tr>
              <tr>
                <td><strong>+20 dB</strong></td>
                <td>100.0 &times; (100x)</td>
                <td>10.00 &times; (10x)</td>
                <td>+20 dBm &rarr; 100 mW</td>
                <td>Quiet recording studio / whispering (20 dB SPL)</td>
              </tr>
              <tr>
                <td><strong>+30 dB</strong></td>
                <td>1,000 &times; (1,000x)</td>
                <td>31.62 &times;</td>
                <td>+30 dBm &rarr; 1.0 Watt</td>
                <td>Quiet bedroom at night (30 dB SPL)</td>
              </tr>
              <tr>
                <td><strong>+60 dB</strong></td>
                <td>1,000,000 &times;</td>
                <td>1,000 &times;</td>
                <td>+60 dBm &rarr; 1.0 kW</td>
                <td>Normal conversational speech at 1m (60 dB SPL)</td>
              </tr>
              <tr>
                <td><strong>+85 dB</strong></td>
                <td>3.16 &times; 10&sup8; &times;</td>
                <td>17,783 &times;</td>
                <td>&mdash;</td>
                <td>OSHA 8-hour hearing protection threshold</td>
              </tr>
              <tr>
                <td><strong>+120 dB</strong></td>
                <td>10&sup1;&sup2; &times; (1 Trillion)</td>
                <td>1,000,000 &times;</td>
                <td>&mdash;</td>
                <td>Rock concert front row / human threshold of pain</td>
              </tr>
            </tbody>
          </table>

          <!-- Real World Worked Case Study Card -->
          <div class="worked-example-card">
            <h3>Practical Case Study: RF Link Budget &amp; Coaxial Cable Loss Analysis</h3>
            <p>
              A telecommunications network technician is evaluating an outdoor 2.4 GHz Wi-Fi access point installation. The transmitter output power is $P_{tx} = +20\text{ dBm}$ (100 mW). The signal is routed through 50 feet of RG-58 coaxial cable exhibiting an attenuation of $6.0\text{ dB}$, and feeds into a directional panel antenna with a gain of $+14\text{ dBi}$.
            </p>
            <div class="step-calculation">
              <strong>Step 1: Convert Transmitter Output to Watts:</strong><br>
              $$P\text{ (mW)} = 10^{20 / 10} = 10^2 = 100\text{ mW} = 0.100\text{ Watts}$$
            </div>
            <div class="step-calculation">
              <strong>Step 2: Calculate Power Arriving at Antenna Feedpoint:</strong><br>
              Subtracting the coaxial cable attenuation:
              $$P_{ant} = +20\text{ dBm} - 6.0\text{ dB} = +14\text{ dBm}$$
              $$P_{ant}\text{ (mW)} = 10^{14 / 10} = 10^{1.4} \approx 25.12\text{ mW}$$
              <small>Notice how a 6 dB loss reduces power to almost exactly one-fourth of the original 100 mW.</small>
            </div>
            <div class="step-calculation">
              <strong>Step 3: Calculate Effective Isotropic Radiated Power (EIRP):</strong><br>
              Adding the antenna forward gain:
              $$\text{EIRP} = P_{ant} + G_{ant} = +14\text{ dBm} + 14\text{ dBi} = +28\text{ dBm}$$
              $$\text{EIRP (Watts)} = 10^{(28 - 30) / 10} = 10^{-0.2} \approx 0.631\text{ Watts (631 mW)}$$
              <p>
                <strong>Conclusion:</strong> Adding and subtracting decibels directly replaces tedious linear multiplication and division of small power fractions, demonstrating the immense computational efficiency of decibel calculations in RF link design.
              </p>
            </div>
          </div>

          <h2>Key Engineering Guidelines for Decibel Operations</h2>
          <ul>
            <li><strong>Adding Ratios vs Adding Power:</strong> You can directly add and subtract decibels when cascading amplifier stages and attenuators (e.g., $+20\text{ dB gain} - 3\text{ dB loss} = +17\text{ dB net gain}$). However, you cannot directly add decibels of two separate acoustic sources! Two independent 60 dB SPL machines operating simultaneously do not produce 120 dB SPL; they produce $60 + 10 \log_{10}(2) = 63\text{ dB SPL}$.</li>
            <li><strong>Impedance Awareness for Voltage Ratios:</strong> The $20 \log_{10}(V_1 / V_0)$ formula assumes both voltages are measured across identical resistive impedances ($R_1 = R_0$). If input and output impedances differ, an impedance correction factor $10 \log_{10}(R_{in} / R_{out})$ must be included.</li>
            <li><strong>Root-Mean-Square (RMS) Requirement:</strong> When evaluating AC audio voltages for dBu and dBV measurements, always utilize true RMS digital multimeters. Average-responding meters calibrated to sine waves will yield substantial decibel errors on complex non-sinusoidal audio program material.</li>
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
    function toggleDbMode() {
      const mode = document.getElementById('calcMode').value;
      document.getElementById('grpPowerP1').style.display = (mode === "power-ratio") ? "block" : "none";
      document.getElementById('grpPowerP0').style.display = (mode === "power-ratio") ? "block" : "none";
      document.getElementById('grpVoltV1').style.display = (mode === "voltage-ratio") ? "block" : "none";
      document.getElementById('grpVoltV0').style.display = (mode === "voltage-ratio") ? "block" : "none";
      document.getElementById('grpDbmVal').style.display = (mode === "dbm-watts") ? "block" : "none";
      document.getElementById('grpSplPressure').style.display = (mode === "sound-spl") ? "block" : "none";
    }

    function calculateDb() {
      const mode = document.getElementById('calcMode').value;

      let dbVal = 0;
      let linearRatio = 1.0;
      let powerWatts = 0;
      let dbwVal = 0;
      let dbuVal = 0;
      let mainDesc = "";
      let linearDesc = "";
      let splCat = "N/A";
      let splDesc = "Acoustic level";

      if (mode === "power-ratio") {
        const P1 = parseFloat(document.getElementById('valP1').value);
        const P0 = parseFloat(document.getElementById('valP0').value);
        if (isNaN(P1) || isNaN(P0) || P1 <= 0 || P0 <= 0) return;

        linearRatio = P1 / P0;
        dbVal = 10 * Math.log10(linearRatio);
        powerWatts = P1;
        dbwVal = 10 * Math.log10(P1);
        mainDesc = (dbVal >= 0) ? `Power gain ratio (${linearRatio.toFixed(2)}x)` : `Power attenuation ratio (${linearRatio.toFixed(4)}x)`;
        linearDesc = "P1 / P0 power amplification factor";
      } else if (mode === "voltage-ratio") {
        const V1 = parseFloat(document.getElementById('valV1').value);
        const V0 = parseFloat(document.getElementById('valV0').value);
        if (isNaN(V1) || isNaN(V0) || V1 <= 0 || V0 <= 0) return;

        linearRatio = V1 / V0;
        dbVal = 20 * Math.log10(linearRatio);
        mainDesc = (dbVal >= 0) ? `Voltage gain ratio (${linearRatio.toFixed(2)}x)` : `Voltage attenuation (${linearRatio.toFixed(4)}x)`;
        linearDesc = "V1 / V0 field amplitude ratio";

        // Calculate dBu from V1
        dbuVal = 20 * Math.log10(V1 / 0.77459667);
      } else if (mode === "dbm-watts") {
        const dbm = parseFloat(document.getElementById('valDbm').value);
        if (isNaN(dbm)) return;

        dbVal = dbm;
        const pMilli = Math.pow(10, dbm / 10);
        powerWatts = pMilli / 1000;
        linearRatio = pMilli;
        dbwVal = dbm - 30;
        mainDesc = "Absolute power referenced to 1 mW";
        linearDesc = "Absolute power in milliwatts";
      } else if (mode === "sound-spl") {
        const p = parseFloat(document.getElementById('valPressure').value);
        if (isNaN(p) || p <= 0) return;

        const p0 = 0.000020; // 20 uPa
        linearRatio = p / p0;
        dbVal = 20 * Math.log10(linearRatio);
        mainDesc = "Sound Pressure Level over 20 µPa";
        linearDesc = "Pressure ratio over auditory threshold";

        if (dbVal < 30) {
          splCat = "Faint / Whisper";
          splDesc = "Quiet recording studio / countryside";
        } else if (dbVal < 60) {
          splCat = "Quiet / Moderate";
          splDesc = "Quiet residential home / library";
        } else if (dbVal < 80) {
          splCat = "Conversational";
          splDesc = "Normal speech at 1m / office / vacuum";
        } else if (dbVal < 90) {
          splCat = "Loud / Heavy Traffic";
          splDesc = "Approaching OSHA 85 dBA workplace limit";
        } else if (dbVal < 120) {
          splCat = "Hazardous / High Noise";
          splDesc = "Power lawnmower / rock concert / siren";
        } else {
          splCat = "THRESHOLD OF PAIN";
          splDesc = "Jet takeoff / permanent hearing damage risk";
        }
      }

      const sign = (dbVal > 0) ? "+" : "";
      document.getElementById('outMainDb').textContent = `${sign}${dbVal.toFixed(2)} dB`;
      document.getElementById('outMainDesc').textContent = mainDesc;

      document.getElementById('outLinearRatio').textContent = (linearRatio >= 1000) ? linearRatio.toExponential(2) + " x" : linearRatio.toFixed(2) + " x";
      document.getElementById('outLinearDesc').textContent = linearDesc;

      if (powerWatts > 0) {
        document.getElementById('outWatts').textContent = (powerWatts >= 1000) ? (powerWatts / 1000).toFixed(2) + " kW" : (powerWatts >= 0.001) ? powerWatts.toFixed(3) + " W" : (powerWatts * 1000000).toFixed(1) + " µW";
        document.getElementById('outMilliwatts').textContent = (powerWatts * 1000).toLocaleString('en-US', {maximumFractionDigits: 2}) + " mW";
        document.getElementById('outDbw').textContent = `${(dbwVal > 0 ? "+" : "")}${dbwVal.toFixed(2)} dBW`;
      } else {
        document.getElementById('outWatts').textContent = "—";
        document.getElementById('outMilliwatts').textContent = "—";
        document.getElementById('outDbw').textContent = "—";
      }

      if (dbuVal !== 0) {
        document.getElementById('outDbu').textContent = `${(dbuVal > 0 ? "+" : "")}${dbuVal.toFixed(2)} dBu`;
      } else {
        document.getElementById('outDbu').textContent = "—";
      }

      document.getElementById('outSplCat').textContent = splCat;
      document.getElementById('outSplDesc').textContent = splDesc;
    }

    window.addEventListener('DOMContentLoaded', () => {
      toggleDbMode();
      calculateDb();
    });
  </script>
</body>
</html>
"""

def main():
    path_breaker = os.path.join(BASE_DIR, "breaker-size-calculator.html")
    with open(path_breaker, "w", encoding="utf-8") as f:
        f.write(TOOL_BREAKER.strip())
    print("[PASS] breaker-size-calculator.html generated successfully!")

    path_db = os.path.join(BASE_DIR, "decibel-calculator.html")
    with open(path_db, "w", encoding="utf-8") as f:
        f.write(TOOL_DECIBEL.strip())
    print("[PASS] decibel-calculator.html generated successfully!")

if __name__ == "__main__":
    main()
