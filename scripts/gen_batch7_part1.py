# -*- coding: utf-8 -*-
"""
Script to generate Batch 7 Part 1 tools:
1. fault-current-calculator.html
2. filter-calculator.html
"""
import os

TOOL_1_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fault Current Calculator | Point-to-Point Electrical Short Circuit Analysis</title>
  <meta name="description" content="Calculate electrical fault currents, symmetrical short-circuit kA, transformer secondary prospective fault levels, and downstream line impedance per IEEE 141 and IEC 60909.">
  <link rel="canonical" href="https://calchub.cloud/fault-current-calculator.html">
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
        "name": "Fault Current Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Professional electrical short-circuit and prospective fault current calculator based on IEEE 141 Red Book point-to-point and IEC 60909 impedance methodology.",
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
            "name": "What is the difference between prospective fault current and load current?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Load current is the normal continuous current drawn by connected electrical equipment under operational conditions. Prospective fault current (or short-circuit current) is the massive theoretical current that rushes through the circuit when a zero-impedance short-circuit occurs between live conductors or between phase and ground, limited solely by upstream system impedance."
            }
          },
          {
            "@type": "Question",
            "name": "How does transformer percent impedance (%Z) limit secondary fault current?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Percent impedance (%Z) defines the percentage of rated primary voltage required to circulate rated full-load current through a short-circuited secondary. The available symmetrical fault current directly at the secondary terminals of an infinite-bus transformer is: I_sc = I_FLA / (%Z / 100). A transformer with 5% impedance limits maximum bolted fault current to exactly 20 times its full-load rating."
            }
          },
          {
            "@type": "Question",
            "name": "Why do running electric motors contribute to short-circuit fault current?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "When a terminal short-circuit occurs, system voltage drops toward zero. Operating induction and synchronous motors do not stop instantly; their rotating mechanical inertia drives the rotor magnetic field through the stator windings, momentarily transforming them into induction generators that feed reverse fault current into the short-circuit for several cycles."
            }
          },
          {
            "@type": "Question",
            "name": "What is the Point-to-Point method for calculating downstream fault currents?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The Point-to-Point method (codified in IEEE 141 Red Book) computes downstream short-circuit current at a subpanel or motor disconnect by calculating a multiplier f = (1.732 * L * I_sc_upstream) / (C * n * V_LL), where L is cable length, C is conductor impedance factor, and n is number of conductors per phase. Downstream available fault current is then: I_sc_downstream = I_sc_upstream / (1 + f)."
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
      <span>Fault Current Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">IEEE 141 &amp; IEC 60909 Methodologies</div>
          <h1 class="calc-title">Fault Current Calculator</h1>
          <p class="calc-tagline">Calculate prospective 3-phase symmetrical short-circuit kA at transformer terminals and downstream distribution panels.</p>
        </header>

        <!-- Tool Card -->
        <div class="tool-card">
          <form id="faultForm" onsubmit="return false;">
            <div class="calc-grid">
              <div class="form-group">
                <label for="xfmrRatingKva" class="form-label">Transformer Rating ($S_n$)</label>
                <div class="input-with-unit">
                  <input type="number" id="xfmrRatingKva" class="form-control" value="1000" min="10" step="50" oninput="calculateFaultCurrent()">
                  <span class="unit-badge">kVA</span>
                </div>
                <small class="form-hint">Nominal 3-phase power rating</small>
              </div>

              <div class="form-group">
                <label for="secVoltage" class="form-label">Secondary Line-to-Line Voltage ($V_{LL}$)</label>
                <div class="input-with-unit">
                  <input type="number" id="secVoltage" class="form-control" value="400" min="100" max="1000" step="10" oninput="calculateFaultCurrent()">
                  <span class="unit-badge">Volts</span>
                </div>
                <small class="form-hint">Secondary operating voltage (e.g. 400V or 480V)</small>
              </div>

              <div class="form-group">
                <label for="xfmrZPercent" class="form-label">Transformer Impedance ($\%Z$)</label>
                <div class="input-with-unit">
                  <input type="number" id="xfmrZPercent" class="form-control" value="5.75" min="1.0" max="15.0" step="0.25" oninput="calculateFaultCurrent()">
                  <span class="unit-badge">%</span>
                </div>
                <small class="form-hint">Nameplate impedance (typically 4.0% – 6.0%)</small>
              </div>

              <div class="form-group">
                <label for="motorContribution" class="form-label">Motor Load Contribution</label>
                <select id="motorContribution" class="form-control" onchange="calculateFaultCurrent()">
                  <option value="none">No Motor Contribution (Pure Static / Resistive)</option>
                  <option value="standard" selected>Standard Industrial Mix (100% Motor kVA, +4x FLA)</option>
                  <option value="heavy">Heavy Industrial Plant (100% Induction, +5x FLA)</option>
                </select>
                <small class="form-hint">Rotary inertia transient fault feed</small>
              </div>

              <div class="form-group">
                <label for="cableRunLength" class="form-label">Downstream Feeder Length ($L$)</label>
                <div class="input-with-unit">
                  <input type="number" id="cableRunLength" class="form-control" value="40" min="0" max="1000" step="5" oninput="calculateFaultCurrent()">
                  <span class="unit-badge">metres</span>
                </div>
                <small class="form-hint">0m for transformer secondary terminals</small>
              </div>

              <div class="form-group">
                <label for="cableSizeMm2" class="form-label">Feeder Conductor Cross-Section</label>
                <select id="cableSizeMm2" class="form-control" onchange="calculateFaultCurrent()">
                  <option value="25">25 mm² Copper ($C \approx 14,000$)</option>
                  <option value="35">35 mm² Copper ($C \approx 18,000$)</option>
                  <option value="50">50 mm² Copper ($C \approx 22,500$)</option>
                  <option value="70">70 mm² Copper ($C \approx 28,000$)</option>
                  <option value="95">95 mm² Copper ($C \approx 33,500$)</option>
                  <option value="120">120 mm² Copper ($C \approx 37,500$)</option>
                  <option value="150">150 mm² Copper ($C \approx 41,000$)</option>
                  <option value="185">185 mm² Copper ($C \approx 44,500$)</option>
                  <option value="240" selected>240 mm² Copper ($C \approx 48,000$)</option>
                  <option value="300">300 mm² Copper ($C \approx 50,500$)</option>
                </select>
                <small class="form-hint">Cable line impedance limiter</small>
              </div>

              <div class="form-group">
                <label for="parallelRuns" class="form-label">Conductors per Phase ($n$)</label>
                <div class="input-with-unit">
                  <input type="number" id="parallelRuns" class="form-control" value="1" min="1" max="8" step="1" oninput="calculateFaultCurrent()">
                  <span class="unit-badge">runs</span>
                </div>
                <small class="form-hint">Parallel sets of cables</small>
              </div>

              <div class="form-group">
                <label for="sourceMva" class="form-label">Upstream Primary Utility Short-Circuit</label>
                <select id="sourceMva" class="form-control" onchange="calculateFaultCurrent()">
                  <option value="infinite" selected>Infinite Utility Bus (Conservative Sizing)</option>
                  <option value="500">500 MVA Available Utility Fault</option>
                  <option value="250">250 MVA Available Utility Fault</option>
                  <option value="100">100 MVA Weak Rural Grid</option>
                </select>
                <small class="form-hint">Upstream grid source stiffness</small>
              </div>
            </div>

            <button type="button" id="calcFaultBtn" class="btn btn-primary btn-block" onclick="calculateFaultCurrent()">Calculate Available Fault Current</button>
          </form>

          <div id="faultResultBox" class="results-container" style="margin-top:20px;">
            <h3>Short-Circuit Analysis Results</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label">Transformer Full-Load Amps ($I_{FLA}$)</span>
                <span id="xfmrFlaOut" class="result-value">-- A</span>
              </div>
              <div class="result-tile">
                <span class="result-label">XFMR Secondary Bolted Fault ($I_{sc,base}$)</span>
                <span id="xfmrScOut" class="result-value">-- kA</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Motor Inrush Contribution ($I_{sc,motor}$)</span>
                <span id="motorScOut" class="result-value">-- kA</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Total Bus Fault Current (Switchboard)</span>
                <span id="totalBusScOut" class="result-value">-- kA</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Point-to-Point Feeder Multiplier ($f$)</span>
                <span id="ptpFactorOut" class="result-value">--</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Downstream Subpanel Fault Current</span>
                <span id="downstreamScOut" class="result-value">-- kA</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Engineering Principles of Short-Circuit Fault Current Analysis</h2>
          
          <p>Every commercial, industrial, and utility power distribution system must be engineered to withstand and safely isolate catastrophic short circuits. An electrical short-circuit or fault occurs when an unintended low-impedance electrical path forms between energized phase conductors, or between a phase conductor and neutral or earth. The resulting massive surge of electrical current generates destructive electromagnetic forces and intense localized thermal energy (joule heating) governed by the relationship $E = I^2 t$. If switchboards, circuit breakers, fuses, and busbar supports lack adequate Short-Circuit Current Ratings (SCCR) and interrupting capacity ($I_{cu} / I_{cs}$), physical structural explosion, catastrophic arc flash discharge, and uncontained electrical fires occur.</p>

          <p>Calculating available prospective fault current is the fundamental prerequisite mandated by international regulatory codes, including <strong>NFPA 70 (National Electrical Code NEC Article 110.9 &amp; 110.10)</strong>, <strong>IEEE 141 (Red Book: Recommended Practice for Electric Power Distribution for Industrial Plants)</strong>, and <strong>IEC 60909 (Short-circuit currents in three-phase a.c. systems)</strong>.</p>

          <div class="formula-box">
            <h3>Transformer Secondary Bolted Fault Current Formulation</h3>
            <p>For a three-phase distribution transformer supplying a low-voltage switchboard, the rated secondary full-load current ($I_{FLA}$) is derived from apparent power $S_n$ (in kVA) and secondary line-to-line voltage $V_{LL}$ (in Volts):</p>
            <p>$$I_{FLA} = \frac{S_n \times 1000}{\sqrt{3} \times V_{LL}}$$</p>
            <p>When assuming an infinite utility primary bus (where grid impedance is considered negligible), the maximum three-phase symmetrical bolted fault current ($I_{sc,xfmr}$) available at the transformer secondary terminals is inversely proportional to its internal percent impedance ($\%Z$):</p>
            <p>$$I_{sc,xfmr} = \frac{I_{FLA}}{\frac{\%Z}{100}} = I_{FLA} \times \frac{100}{\%Z}$$</p>
            <p>Where $\%Z$ represents the vector combination of transformer winding resistance and leakage reactance ($\%Z = \sqrt{\%R^2 + \%X^2}$).</p>
          </div>

          <h3>Accounting for Upstream Utility Grid Source Impedance</h3>
          <p>While the infinite bus assumption provides a conservative, worst-case upper bound suitable for preliminary equipment selection, real-world utility interconnections possess finite fault capacity. The primary utility network is characterized by its available short-circuit power ($MVA_{sc,grid}$) at the medium-voltage point of common coupling (PCC). To compute exact secondary fault levels under finite grid stiffness, source impedances are converted to a common system base:</p>

          <p>$$Z_{grid,sec} = \frac{V_{LL}^2}{MVA_{sc,grid} \times 10^6} \quad [\Omega]$$</p>
          <p>$$Z_{xfmr,sec} = \frac{\%Z}{100} \times \frac{V_{LL}^2}{S_n \times 1000} \quad [\Omega]$$</p>
          <p>$$Z_{total} = Z_{grid,sec} + Z_{xfmr,sec}$$</p>
          <p>$$I_{sc,actual} = \frac{V_{LL}}{\sqrt{3} \times Z_{total}}$$</p>

          <h3>Rotary Induction Motor Contribution to Short Circuits</h3>
          <p>A frequently overlooked danger in industrial electrical plants is the transient feedback from rotating induction motors. Under normal operation, induction motors consume power from the grid to sustain their rotor magnetic flux. At the instant a three-phase bolted short-circuit occurs, line voltage drops precipitously toward zero volts.</p>

          <p>Due to mechanical inertia, the motor rotor continues spinning at high speed. The trapped flux within the rotor cage induces a back-electromotive force (back-EMF) across the stator terminals. As a consequence, <strong>every operating motor momentarily functions as an independent induction generator</strong>, back-feeding intense fault current into the short-circuit for the first 1 to 4 electrical cycles.</p>

          <p>IEEE 141 (Clause 4.3.4) and ANSI C37.010 provide standard engineering approximations for motor contribution based on connected equipment:</p>
          <ul>
            <li><strong>Low-Voltage Induction Motors ($\le 600\text{V}$):</strong> Momentary symmetrical fault contribution is typically $4.0\times$ to $5.0\times$ the motor full-load running current ($I_{FLA,motor}$).</li>
            <li><strong>Standard Commercial / Industrial Mix:</strong> In typical commercial buildings with lighting, HVAC, and mixed plug loads, motor contribution is modeled as roughly $2.0\times$ to $4.0\times$ the transformer rated secondary FLA.</li>
            <li><strong>Heavy Process Manufacturing:</strong> Where motor loads dominate (pumps, compressors, conveyors, fans), motor contribution frequently adds $100\%$ of the transformer base rating at $4.0\times$ FLA, substantially increasing required switchboard breaker interrupting ratings (e.g. pushing a 35 kA board requirement to 50 kA or 65 kA).</li>
          </ul>

          <div class="formula-box">
            <h3>Downstream Point-to-Point Cable Impedance Method (IEEE 141)</h3>
            <p>As electrical current travels through feeder cables from the main switchboard to distribution subpanels, motor control centers (MCC), and terminal disconnects, the physical resistance and inductance of the copper or aluminum conductors add impedance, dramatically damping available short-circuit currents.</p>
            <p>The IEEE Point-to-Point method calculates the dimensionless feeder impedance factor $f$:</p>
            <p>$$f = \frac{1.732 \times L \times I_{sc,upstream}}{C \times n \times V_{LL}}$$</p>
            <p>Where:</p>
            <ul>
              <li>$L$ = One-way circuit length in meters (or feet with appropriate $C$ factor).</li>
              <li>$I_{sc,upstream}$ = Available symmetrical short-circuit current at the supply switchboard (Amperes).</li>
              <li>$V_{LL}$ = Line-to-line system voltage (Volts).</li>
              <li>$n$ = Number of parallel conductors per phase.</li>
              <li>$C$ = Conductor material and conduit impedance constant (derived from IEEE 141 Table 4-1 / Bussmann SPD).</li>
            </ul>
            <p>Once factor $f$ is evaluated, the available symmetrical fault current at the downstream load terminal ($I_{sc,downstream}$) is calculated directly by:</p>
            <p>$$I_{sc,downstream} = \frac{I_{sc,upstream}}{1 + f}$$</p>
          </div>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Conductor Size (mm²)</th>
                <th>Equivalent AWG/kcmil</th>
                <th>Copper in Steel Conduit ($C$)</th>
                <th>Copper in PVC Conduit ($C$)</th>
                <th>Aluminum in Steel Conduit ($C$)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>16 mm²</strong></td>
                <td>#6 AWG</td>
                <td>8,900</td>
                <td>9,100</td>
                <td>5,400</td>
              </tr>
              <tr>
                <td><strong>25 mm²</strong></td>
                <td>#4 AWG</td>
                <td>13,800</td>
                <td>14,200</td>
                <td>8,400</td>
              </tr>
              <tr>
                <td><strong>35 mm²</strong></td>
                <td>#2 AWG</td>
                <td>18,200</td>
                <td>18,900</td>
                <td>11,100</td>
              </tr>
              <tr>
                <td><strong>50 mm²</strong></td>
                <td>1/0 AWG</td>
                <td>22,600</td>
                <td>23,700</td>
                <td>13,800</td>
              </tr>
              <tr>
                <td><strong>70 mm²</strong></td>
                <td>2/0 AWG</td>
                <td>27,800</td>
                <td>29,400</td>
                <td>17,000</td>
              </tr>
              <tr>
                <td><strong>95 mm²</strong></td>
                <td>3/0 AWG</td>
                <td>33,200</td>
                <td>35,600</td>
                <td>20,400</td>
              </tr>
              <tr>
                <td><strong>120 mm²</strong></td>
                <td>4/0 AWG</td>
                <td>37,600</td>
                <td>40,800</td>
                <td>23,200</td>
              </tr>
              <tr>
                <td><strong>185 mm²</strong></td>
                <td>350 kcmil</td>
                <td>44,200</td>
                <td>49,100</td>
                <td>27,800</td>
              </tr>
              <tr>
                <td><strong>240 mm²</strong></td>
                <td>500 kcmil</td>
                <td>47,800</td>
                <td>54,200</td>
                <td>30,500</td>
              </tr>
            </tbody>
          </table>

          <div class="worked-example-card">
            <h3>Practical Worked Engineering Example: Industrial Manufacturing Facility</h3>
            <p><strong>Scenario:</strong> Sizing switchgear interrupting ratings for an industrial facility served by a 1,000 kVA, 400V, 50 Hz substation transformer with a nameplate impedance of $\%Z = 5.75\%$. The utility medium-voltage grid is modeled as an infinite bus. Operating equipment includes a standard industrial motor mix (contributing $4.0\times$ motor FLA, where motor load equals $100\%$ of transformer kVA). Sizing is also required for a downstream distribution subpanel located $40\text{ meters}$ away, fed by a single run ($n = 1$) of $240\text{ mm}^2$ copper cable in steel conduit ($C = 47{,}800$).</p>

            <p><strong>Step 1: Calculate Transformer Full-Load Amps ($I_{FLA}$)</strong></p>
            <p>$$I_{FLA} = \frac{1000 \times 1000}{\sqrt{3} \times 400} = \frac{1{,}000{,}000}{692.82} = 1443.38\text{ A}$$</p>

            <p><strong>Step 2: Calculate Base Secondary Bolted Fault Current ($I_{sc,xfmr}$)</strong></p>
            <p>$$I_{sc,xfmr} = \frac{I_{FLA}}{\%Z / 100} = \frac{1443.38}{0.0575} = 25{,}102\text{ A} = 25.10\text{ kA}$$</p>

            <p><strong>Step 3: Calculate Motor Inrush Fault Contribution ($I_{sc,motor}$)</strong></p>
            <p>Assuming 100% connected motor load at $4.0\times$ running FLA:</p>
            <p>$$I_{sc,motor} = 4.0 \times 1443.38\text{ A} = 5773.5\text{ A} = 5.77\text{ kA}$$</p>
            <p>Total prospective fault current available at the main switchboard busbar:</p>
            <p>$$I_{sc,total} = I_{sc,xfmr} + I_{sc,motor} = 25.10\text{ kA} + 5.77\text{ kA} = 30.87\text{ kA}$$</p>
            <p><em>Conclusion for Main Switchgear:</em> The main circuit breaker must possess an interrupting rating of at least $35\text{ kA}$ or $50\text{ kA}$ (standard industrial rating).</p>

            <p><strong>Step 4: Compute Downstream Fault Current at Subpanel (Point-to-Point)</strong></p>
            <p>Applying the IEEE 141 feeder attenuation factor $f$ for $L = 40\text{ m}$, $C = 47{,}800$, $n = 1$, and $V_{LL} = 400\text{ V}$:</p>
            <p>$$f = \frac{1.732 \times 40 \times 30{,}870}{47{,}800 \times 1 \times 400} = \frac{2{,}138{,}674}{19{,}120{,}000} = 0.1118$$</p>
            <p>The available symmetrical short-circuit current at the downstream subpanel is:</p>
            <p>$$I_{sc,subpanel} = \frac{I_{sc,upstream}}{1 + f} = \frac{30{,}870\text{ A}}{1 + 0.1118} = \frac{30{,}870}{1.1118} = 27{,}766\text{ A} = 27.77\text{ kA}$$</p>
            <p>The 40-meter run of $240\text{ mm}^2$ cable absorbs sufficient energy to reduce the prospective fault current from $30.87\text{ kA}$ down to $27.77\text{ kA}$. Branch circuit breakers in the subpanel must be rated for at least $30\text{ kA}$ or $35\text{ kA}$.</p>
          </div>

          <h2>Frequently Asked Questions (Fault Current Analysis)</h2>
          <div class="faq-item">
            <h3>What is the difference between symmetrical and asymmetrical fault current?</h3>
            <p>Symmetrical short-circuit current represents the purely alternating steady-state AC sine wave component where positive and negative peak amplitudes are identical. Asymmetrical fault current occurs during the first few cycles immediately following fault initiation, where a transient DC offset component is superimposed onto the AC waveform, shifting the zero-crossing axis and producing a much higher initial peak current ($i_{peak}$). Circuit breakers must possess both adequate symmetrical RMS interrupting capacity and asymmetrical peak withstand capability.</p>
          </div>

          <div class="faq-item">
            <h3>Why must protective devices have an interrupting rating higher than available fault current?</h3>
            <p>Under NEC 110.9 and IEC 60947-2, protective devices (fuses, MCBs, MCCBs, ACBs) must be capable of interrupting the maximum prospective short-circuit current available at their line terminals. If a circuit breaker with a 10 kA rating is installed where 25 kA of fault current is available, the breaker's internal arc chutes will be overwhelmed, resulting in catastrophic failure, sustained plasma arcing, and explosion.</p>
          </div>

          <div class="faq-item">
            <h3>How do parallel feeder conductors affect short-circuit current?</h3>
            <p>Routing parallel conductors per phase reduces the total circuit impedance proportionally to the number of parallel runs $n$. Because electrical impedance is halved when doubling parallel conductors ($Z_{eq} = Z / 2$), downstream fault currents attenuate far less over distance compared to a single smaller conductor run.</p>
          </div>

          <div class="faq-item">
            <h3>Does power factor influence short-circuit current magnitude?</h3>
            <p>During a short circuit, fault impedance is heavily inductive ($X/R$ ratio typically exceeds 3 to 10 near transformers and generators). A higher $X/R$ ratio produces a much larger and longer-lasting DC offset transient, creating higher mechanical peak stresses ($i_{peak} = \kappa \sqrt{2} I_{sc}''$) on busbars and disconnect switches.</p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar" id="toolSidebar">
        <!-- Dynamically rendered sidebar -->
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; 2026 CalcHub. All rights reserved. Engineering and mathematical tools grounded in international standards.</p>
      <ul class="footer-links">
        <li><a href="index.html">Home</a></li>
        <li><a href="engineering.html">Engineering</a></li>
        <li><a href="ohms-law-calculator.html">Ohm's Law</a></li>
        <li><a href="sitemap.xml">Sitemap</a></li>
      </ul>
    </div>
  </footer>

  <script>
    const cFactors = {
      "25": 13800,
      "35": 18200,
      "50": 22600,
      "70": 27800,
      "95": 33200,
      "120": 37600,
      "150": 41000,
      "185": 44200,
      "240": 47800,
      "300": 50500
    };

    function calculateFaultCurrent() {
      const kva = parseFloat(document.getElementById("xfmrRatingKva").value) || 1000;
      const vLL = parseFloat(document.getElementById("secVoltage").value) || 400;
      const zPct = parseFloat(document.getElementById("xfmrZPercent").value) || 5.75;
      const motorMode = document.getElementById("motorContribution").value;
      const length = parseFloat(document.getElementById("cableRunLength").value) || 0;
      const cableSize = document.getElementById("cableSizeMm2").value;
      const runs = parseInt(document.getElementById("parallelRuns").value) || 1;
      const gridMva = document.getElementById("sourceMva").value;

      // Full load amps
      const iFla = (kva * 1000) / (Math.sqrt(3) * vLL);

      // Base XFMR fault
      let zTotalEquivalent = zPct / 100;
      if (gridMva !== "infinite") {
        const mvaVal = parseFloat(gridMva);
        // Grid equivalent impedance on transformer base
        const zGridPerUnit = kva / (mvaVal * 1000);
        zTotalEquivalent += zGridPerUnit;
      }

      const iScXfmr = iFla / zTotalEquivalent;

      // Motor contribution
      let iScMotor = 0;
      if (motorMode === "standard") {
        iScMotor = iFla * 4.0;
      } else if (motorMode === "heavy") {
        iScMotor = iFla * 5.0;
      }

      const iScTotalBus = iScXfmr + iScMotor;

      // Downstream point-to-point calculation
      let fFactor = 0;
      let iScDownstream = iScTotalBus;

      if (length > 0) {
        const cVal = cFactors[cableSize] || 47800;
        fFactor = (1.732 * length * iScTotalBus) / (cVal * runs * vLL);
        iScDownstream = iScTotalBus / (1 + fFactor);
      }

      document.getElementById("xfmrFlaOut").innerText = iFla.toFixed(1) + " A";
      document.getElementById("xfmrScOut").innerText = (iScXfmr / 1000).toFixed(2) + " kA";
      document.getElementById("motorScOut").innerText = (iScMotor / 1000).toFixed(2) + " kA";
      document.getElementById("totalBusScOut").innerText = (iScTotalBus / 1000).toFixed(2) + " kA";
      document.getElementById("ptpFactorOut").innerText = fFactor.toFixed(4);
      document.getElementById("downstreamScOut").innerText = (iScDownstream / 1000).toFixed(2) + " kA";
    }

    document.addEventListener("DOMContentLoaded", function() {
      calculateFaultCurrent();
    });
  </script>
</body>
</html>
"""

TOOL_2_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Filter Calculator | RC, RL, LC Low-Pass & High-Pass Frequency Response</title>
  <meta name="description" content="Calculate analog active and passive electrical filters. Computes cutoff frequency fc, component values, damping factor Q, attenuation dB, and phase shift for RC, RL, and LC circuits.">
  <link rel="canonical" href="https://calchub.cloud/filter-calculator.html">
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
        "name": "Filter Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Comprehensive analog electronic filter calculator for RC, RL, and LC circuits calculating 3dB cutoff frequency, transfer function attenuation, and phase angle.",
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
            "name": "What is the 3dB cutoff frequency (fc) of an analog filter?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The cutoff frequency fc (also known as the corner, break, or half-power frequency) is the specific frequency at which the filter's output signal power drops to 50% of the maximum passband power. In terms of voltage amplitude, the output drops by a factor of 1/sqrt(2) approx 0.7071 of the input voltage, representing an attenuation of exactly -3.01 dB."
            }
          },
          {
            "@type": "Question",
            "name": "What is the roll-off rate of a first-order vs second-order filter?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A first-order passive filter (single resistor and capacitor RC, or RL) attenuates out-of-band signals at a slope of -20 dB per decade (-6 dB per octave). A second-order filter (such as an LC resonant tank or active Sallen-Key topology) produces a roll-off slope twice as steep at -40 dB per decade (-12 dB per octave)."
            }
          },
          {
            "@type": "Question",
            "name": "How is the resonant frequency of an LC filter calculated?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The natural undamped resonant frequency f0 of an LC filter occurs where inductive reactance equals capacitive reactance (X_L = X_C). It is calculated using Thomson's resonance equation: f0 = 1 / (2 * pi * sqrt(L * C))."
            }
          },
          {
            "@type": "Question",
            "name": "Why is filter quality factor (Q) critical in LC and active circuits?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Quality factor Q measures the damping of the circuit. A high Q (Q > 0.707) produces a sharp frequency transition but causes peaking and ringing in the time domain. A Butterworth response (Q = 0.707) provides maximal passband flatness without ripple, while a Bessel response (Q = 0.577) prioritizes linear phase response and minimal group delay."
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
      <span>Filter Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">Analog Signal Processing &amp; RF Engineering</div>
          <h1 class="calc-title">Filter Calculator</h1>
          <p class="calc-tagline">Calculate cutoff frequency, transfer function gain, phase response, and component values for RC, RL, and LC analog filters.</p>
        </header>

        <!-- Tool Card -->
        <div class="tool-card">
          <form id="filterForm" onsubmit="return false;">
            <div class="calc-grid">
              <div class="form-group">
                <label for="filterTopology" class="form-label">Filter Topology</label>
                <select id="filterTopology" class="form-control" onchange="calculateFilter()">
                  <option value="rc_lp" selected>RC Low-Pass Filter (1st Order Passive)</option>
                  <option value="rc_hp">RC High-Pass Filter (1st Order Passive)</option>
                  <option value="rl_lp">RL Low-Pass Filter (1st Order Passive)</option>
                  <option value="rl_hp">RL High-Pass Filter (1st Order Passive)</option>
                  <option value="lc_lp">LC Low-Pass Filter (2nd Order Resonant)</option>
                  <option value="lc_hp">LC High-Pass Filter (2nd Order Resonant)</option>
                </select>
                <small class="form-hint">Circuit architecture &amp; order</small>
              </div>

              <div class="form-group">
                <label for="filterResistor" class="form-label">Resistance ($R$)</label>
                <div class="input-with-unit">
                  <input type="number" id="filterResistor" class="form-control" value="10" min="0.001" step="0.5" oninput="calculateFilter()">
                  <span class="unit-badge">k&Omega;</span>
                </div>
                <small class="form-hint">Series or load resistance</small>
              </div>

              <div class="form-group">
                <label for="filterCapacitor" class="form-label">Capacitance ($C$)</label>
                <div class="input-with-unit">
                  <input type="number" id="filterCapacitor" class="form-control" value="100" min="0.001" step="10" oninput="calculateFilter()">
                  <span class="unit-badge">nF</span>
                </div>
                <small class="form-hint">Shunt or series capacitor</small>
              </div>

              <div class="form-group">
                <label for="filterInductor" class="form-label">Inductance ($L$)</label>
                <div class="input-with-unit">
                  <input type="number" id="filterInductor" class="form-control" value="10" min="0.001" step="1" oninput="calculateFilter()">
                  <span class="unit-badge">mH</span>
                </div>
                <small class="form-hint">For RL and LC filter circuits</small>
              </div>

              <div class="form-group">
                <label for="evalFrequency" class="form-label">Evaluation Test Frequency ($f$)</label>
                <div class="input-with-unit">
                  <input type="number" id="evalFrequency" class="form-control" value="1000" min="0.1" step="50" oninput="calculateFilter()">
                  <span class="unit-badge">Hz</span>
                </div>
                <small class="form-hint">Operating signal frequency to test</small>
              </div>

              <div class="form-group">
                <label for="inputVoltage" class="form-label">Input Signal Amplitude ($V_{in}$)</label>
                <div class="input-with-unit">
                  <input type="number" id="inputVoltage" class="form-control" value="5.0" min="0.1" step="0.5" oninput="calculateFilter()">
                  <span class="unit-badge">Volts</span>
                </div>
                <small class="form-hint">Peak or RMS excitation voltage</small>
              </div>
            </div>

            <button type="button" id="calcFilterBtn" class="btn btn-primary btn-block" onclick="calculateFilter()">Compute Frequency Response</button>
          </form>

          <div id="filterResultBox" class="results-container" style="margin-top:20px;">
            <h3>Filter Transfer Function Summary</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label">Cutoff Corner Frequency ($f_c$)</span>
                <span id="fcOut" class="result-value">-- Hz</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Voltage Gain ($V_{out} / V_{in}$)</span>
                <span id="gainOut" class="result-value">--</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Attenuation at Test Frequency</span>
                <span id="attenDbOut" class="result-value">-- dB</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Output Voltage ($V_{out}$)</span>
                <span id="voutOut" class="result-value">-- V</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Phase Shift ($\theta$)</span>
                <span id="phaseOut" class="result-value">-- °</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Asymptotic Stopband Roll-off</span>
                <span id="rolloffOut" class="result-value">-- dB/decade</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Engineering Theory of Electrical and Electronic Filters</h2>
          
          <p>An electrical filter is a frequency-selective two-port network designed to pass signals within a specified frequency band (the <em>passband</em>) while attenuating or suppressing unwanted frequencies, electromagnetic noise, harmonics, and radio-frequency interference outside that band (the <em>stopband</em>). Filters form the backbone of modern electronics, audio engineering, power conversion, biomedical instrumentation, radio-frequency communication, and sensor interfacing. Whether extracting microvolt ECG biomedical pulses, removing 100 kHz PWM switching ripple from buck converters, or anti-aliasing an analog-to-digital converter (ADC), filter design governs signal fidelity.</p>

          <p>Filters are categorized into <strong>passive</strong> topologies constructed exclusively from linear passive components (resistors $R$, inductors $L$, capacitors $C$) which require no external power supply, and <strong>active</strong> topologies incorporating operational amplifiers (op-amps) or transistors to eliminate bulky inductors, provide voltage gain, and isolate high load impedances.</p>

          <div class="formula-box">
            <h3>First-Order Passive RC Filters</h3>
            <p>A first-order passive RC filter consists of a single resistor and a single capacitor arranged as a voltage divider. The cutoff corner frequency $f_c$ occurs where the capacitive reactance $X_C = \frac{1}{2\pi f C}$ equals the resistance $R$:</p>
            <p>$$f_c = \frac{1}{2\pi R C} \quad [\text{Hz}]$$</p>
            <p>The complex transfer function $H(j\omega)$ and corresponding amplitude response $|H(j\omega)|$ for a <strong>Low-Pass RC Filter</strong> (output taken across the capacitor):</p>
            <p>$$H_{LP}(j\omega) = \frac{1}{1 + j\omega RC} \implies |H_{LP}(f)| = \frac{1}{\sqrt{1 + \left(\frac{f}{f_c}\right)^2}}$$</p>
            <p>$$\text{Phase Shift: } \theta_{LP}(f) = -\arctan\left(\frac{f}{f_c}\right)$$</p>
            <p>For an <strong>RC High-Pass Filter</strong> (output taken across the resistor):</p>
            <p>$$H_{HP}(j\omega) = \frac{j\omega RC}{1 + j\omega RC} \implies |H_{HP}(f)| = \frac{\frac{f}{f_c}}{\sqrt{1 + \left(\frac{f}{f_c}\right)^2}}$$</p>
            <p>$$\text{Phase Shift: } \theta_{HP}(f) = +90^\circ - \arctan\left(\frac{f}{f_c}\right) = \arctan\left(\frac{f_c}{f}\right)$$</p>
          </div>

          <h3>First-Order RL Filters: Inductive Duals</h3>
          <p>In high-frequency RF networks and power electronics where inductors are readily available, an RL filter utilizes the frequency-dependent inductive reactance $X_L = 2\pi f L$. The cutoff frequency for an RL circuit is governed by the $L/R$ time constant $\tau = \frac{L}{R}$:</p>

          <p>$$f_c = \frac{R}{2\pi L} \quad [\text{Hz}]$$</p>
          
          <p>In an <strong>RL Low-Pass Filter</strong>, the output is taken across the resistor while the inductor acts as a high-frequency blocking choke. Conversely, in an <strong>RL High-Pass Filter</strong>, the output is tapped across the inductor, which blocks DC and low frequencies while conducting high-frequency transient signals.</p>

          <div class="formula-box">
            <h3>Second-Order LC Resonant Filters</h3>
            <p>Combining both inductive and capacitive energy storage elements creates a second-order filter capable of a steep $-40\text{ dB/decade}$ ($-12\text{ dB/octave}$) stopband roll-off. The undamped resonant frequency $f_0$ occurs when inductive reactance exactly cancels capacitive reactance ($X_L = X_C$):</p>
            <p>$$f_0 = \frac{1}{2\pi \sqrt{L C}} \quad [\text{Hz}]$$</p>
            <p>The damping factor $\zeta$ and Quality factor $Q$ are dictated by circuit load resistance $R$:</p>
            <p>$$Q = R \sqrt{\frac{C}{L}} \quad \text{(for parallel damped LC)}, \quad Q = \frac{1}{R} \sqrt{\frac{L}{C}} \quad \text{(for series damped LC)}$$</p>
            <p>The second-order low-pass transfer function magnitude is given by:</p>
            <p>$$|H_{LC}(f)| = \frac{1}{\sqrt{\left[1 - \left(\frac{f}{f_0}\right)^2\right]^2 + \left[\frac{f}{Q \cdot f_0}\right]^2}}$$</p>
          </div>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Filter Topology</th>
                <th>Order ($n$)</th>
                <th>Cutoff Equation ($f_c$)</th>
                <th>Phase at $f = f_c$</th>
                <th>Stopband Roll-off Rate</th>
                <th>Typical Engineering Application</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>RC Low-Pass</strong></td>
                <td>1st</td>
                <td>$f_c = \frac{1}{2\pi RC}$</td>
                <td>$-45^\circ$</td>
                <td>$-20\text{ dB/decade}$</td>
                <td>ADC anti-aliasing, DAC reconstruction, sensor debouncing</td>
              </tr>
              <tr>
                <td><strong>RC High-Pass</strong></td>
                <td>1st</td>
                <td>$f_c = \frac{1}{2\pi RC}$</td>
                <td>$+45^\circ$</td>
                <td>$-20\text{ dB/decade}$</td>
                <td>AC coupling, DC blocking in audio preamplifiers</td>
              </tr>
              <tr>
                <td><strong>RL Low-Pass</strong></td>
                <td>1st</td>
                <td>$f_c = \frac{R}{2\pi L}$</td>
                <td>$-45^\circ$</td>
                <td>$-20\text{ dB/decade}$</td>
                <td>Switchmode supply EMI chokes, RF power decoupling</td>
              </tr>
              <tr>
                <td><strong>RL High-Pass</strong></td>
                <td>1st</td>
                <td>$f_c = \frac{R}{2\pi L}$</td>
                <td>$+45^\circ$</td>
                <td>$-20\text{ dB/decade}$</td>
                <td>High-frequency pulse triggering, RF carrier bias tees</td>
              </tr>
              <tr>
                <td><strong>LC Low-Pass</strong></td>
                <td>2nd</td>
                <td>$f_0 = \frac{1}{2\pi \sqrt{LC}}$</td>
                <td>$-90^\circ$</td>
                <td>$-40\text{ dB/decade}$</td>
                <td>Class-D audio amplifier demodulation, SMPS output smoothing</td>
              </tr>
              <tr>
                <td><strong>LC High-Pass</strong></td>
                <td>2nd</td>
                <td>$f_0 = \frac{1}{2\pi \sqrt{LC}}$</td>
                <td>$+90^\circ$</td>
                <td>$-40\text{ dB/decade}$</td>
                <td>Sub-woofer crossover, RF receiver front-end isolation</td>
              </tr>
            </tbody>
          </table>

          <div class="worked-example-card">
            <h3>Practical Worked Engineering Example: Audio ADC Anti-Aliasing Filter</h3>
            <p><strong>Design Scenario:</strong> An audio engineer is designing a precision analog front-end for a 24-bit, 48 kHz ADC sampling system. To satisfy the Nyquist-Shannon sampling theorem, all input signal content above the Nyquist frequency ($f_{Nyquist} = 24\text{ kHz}$) must be suppressed to avoid alias distortion. A first-order passive RC low-pass filter is implemented using a $10\text{ k}\Omega$ precision metal film resistor ($R = 10{,}000\ \Omega$) and a $680\text{ pF}$ polypropylene film capacitor ($C = 680 \times 10^{-12}\text{ F}$). The excitation signal is a $5.0\text{ V}$ peak sine wave.</p>

            <p><strong>Step 1: Calculate the 3dB Cutoff Frequency ($f_c$)</strong></p>
            <p>$$f_c = \frac{1}{2\pi \times 10{,}000\ \Omega \times (680 \times 10^{-12}\ \text{F})} = \frac{1}{2\pi \times 6.8 \times 10^{-6}} = \frac{1}{4.2726 \times 10^{-5}} = 23{,}405\text{ Hz} \approx 23.4\text{ kHz}$$</p>

            <p><strong>Step 2: Calculate Output Voltage &amp; Phase at $1\text{ kHz}$ (Audio Passband)</strong></p>
            <p>At $f = 1{,}000\text{ Hz}$:</p>
            <p>$$|H(1\text{kHz})| = \frac{1}{\sqrt{1 + \left(\frac{1000}{23405}\right)^2}} = \frac{1}{\sqrt{1 + (0.0427)^2}} = \frac{1}{\sqrt{1.0018}} = 0.9991$$</p>
            <p>$$\text{Attenuation: } 20 \log_{10}(0.9991) = -0.0078\text{ dB} \quad (\approx 0\text{ dB})$$</p>
            <p>$$V_{out} = 5.0\text{ V} \times 0.9991 = 4.995\text{ V}$$</p>
            <p>$$\theta = -\arctan\left(\frac{1000}{23405}\right) = -2.45^\circ$$</p>

            <p><strong>Step 3: Calculate Attenuation at Nyquist Frequency ($24\text{ kHz}$)</strong></p>
            <p>At $f = 24{,}000\text{ Hz} \approx f_c$:</p>
            <p>$$|H(24\text{kHz})| = \frac{1}{\sqrt{1 + \left(\frac{24000}{23405}\right)^2}} = \frac{1}{\sqrt{1 + 1.0515}} = \frac{1}{1.4323} = 0.6982$$</p>
            <p>$$\text{Attenuation: } 20 \log_{10}(0.6982) = -3.12\text{ dB}$$</p>
            <p>$$V_{out} = 5.0\text{ V} \times 0.6982 = 3.491\text{ V}$$</p>
            <p>$$\theta = -\arctan(1.0254) = -45.72^\circ$$</p>

            <p><strong>Step 4: Calculate Attenuation in the Deep Stopband ($100\text{ kHz}$)</strong></p>
            <p>At $f = 100{,}000\text{ Hz}$ (e.g. ambient SMPS noise):</p>
            <p>$$|H(100\text{kHz})| = \frac{1}{\sqrt{1 + \left(\frac{100000}{23405}\right)^2}} = \frac{1}{\sqrt{1 + 18.254}} = \frac{1}{4.388} = 0.2279$$</p>
            <p>$$\text{Attenuation: } 20 \log_{10}(0.2279) = -12.84\text{ dB}$$</p>
            <p>$$V_{out} = 5.0\text{ V} \times 0.2279 = 1.139\text{ V}, \quad \theta = -\arctan(4.2726) = -76.8^\circ$$</p>
          </div>

          <h2>Frequently Asked Questions (Analog Filter Design)</h2>
          <div class="faq-item">
            <h3>What is the physical meaning of the decibel (dB) attenuation scale in filters?</h3>
            <p>The decibel is a logarithmic ratio representing power or voltage scaling. Voltage gain in dB is defined as $A_{dB} = 20 \log_{10}(V_{out} / V_{in})$. A $-3\text{ dB}$ attenuation indicates the output voltage has dropped to $70.7\%$ of input voltage (and output power to $50\%$). A $-20\text{ dB}$ reduction means the voltage is reduced tenfold ($10\%$), while $-40\text{ dB}$ represents a hundredfold reduction ($1\%$).</p>
          </div>

          <div class="faq-item">
            <h3>Why do passive RC filters cause loading errors when connected to low-impedance circuits?</h3>
            <p>A passive RC filter has a finite output impedance ($Z_{out} \approx R \parallel X_C$). If the downstream circuit has an input impedance comparable to $R$, it draws significant current from the filter divider, altering both the passband gain and shifting the cutoff frequency. Active filters utilizing op-amp voltage followers solve this by presenting near-infinite input impedance and near-zero output impedance.</p>
          </div>

          <div class="faq-item">
            <h3>When should I choose an LC filter instead of an RC filter?</h3>
            <p>LC filters are essential in high-power applications (such as DC-DC switching power supplies and audio power amplifiers) because inductors dissipate negligible DC resistive heat compared to power resistors ($I^2 R$). Furthermore, LC filters achieve a sharp $-40\text{ dB/decade}$ roll-off without requiring active transistors or operational amplifiers.</p>
          </div>

          <div class="faq-item">
            <h3>What is the difference between Butterworth, Chebyshev, and Bessel filters?</h3>
            <p>These classical filter approximations optimize different engineering trade-offs. <strong>Butterworth filters</strong> provide a mathematically maximally flat passband with zero ripple at the expense of moderate roll-off steepness. <strong>Chebyshev filters</strong> deliver an extremely steep roll-off transition into the stopband by permitting controlled ripple in the passband. <strong>Bessel filters</strong> prioritize linear phase response and constant group delay, preserving complex audio and digital pulse waveforms without transient overshoot or ringing.</p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar" id="toolSidebar">
        <!-- Dynamically rendered sidebar -->
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; 2026 CalcHub. All rights reserved. Engineering and mathematical tools grounded in international standards.</p>
      <ul class="footer-links">
        <li><a href="index.html">Home</a></li>
        <li><a href="engineering.html">Engineering</a></li>
        <li><a href="ohms-law-calculator.html">Ohm's Law</a></li>
        <li><a href="sitemap.xml">Sitemap</a></li>
      </ul>
    </div>
  </footer>

  <script>
    function calculateFilter() {
      const topology = document.getElementById("filterTopology").value;
      const rKOhm = parseFloat(document.getElementById("filterResistor").value) || 10;
      const cNf = parseFloat(document.getElementById("filterCapacitor").value) || 100;
      const lMh = parseFloat(document.getElementById("filterInductor").value) || 10;
      const testFreq = parseFloat(document.getElementById("evalFrequency").value) || 1000;
      const vin = parseFloat(document.getElementById("inputVoltage").value) || 5.0;

      const r = rKOhm * 1000; // Ohms
      const c = cNf * 1e-9;   // Farads
      const l = lMh * 1e-3;   // Henrys

      let fc = 0;
      let gain = 1.0;
      let phaseDeg = 0;
      let rolloff = "-20";

      if (topology === "rc_lp") {
        fc = 1 / (2 * Math.PI * r * c);
        const ratio = testFreq / fc;
        gain = 1 / Math.sqrt(1 + ratio * ratio);
        phaseDeg = -Math.atan(ratio) * (180 / Math.PI);
        rolloff = "-20";
      } else if (topology === "rc_hp") {
        fc = 1 / (2 * Math.PI * r * c);
        const ratio = testFreq / fc;
        gain = ratio / Math.sqrt(1 + ratio * ratio);
        phaseDeg = (Math.PI / 2 - Math.atan(ratio)) * (180 / Math.PI);
        rolloff = "+20 (Passband high)";
      } else if (topology === "rl_lp") {
        fc = r / (2 * Math.PI * l);
        const ratio = testFreq / fc;
        gain = 1 / Math.sqrt(1 + ratio * ratio);
        phaseDeg = -Math.atan(ratio) * (180 / Math.PI);
        rolloff = "-20";
      } else if (topology === "rl_hp") {
        fc = r / (2 * Math.PI * l);
        const ratio = testFreq / fc;
        gain = ratio / Math.sqrt(1 + ratio * ratio);
        phaseDeg = (Math.PI / 2 - Math.atan(ratio)) * (180 / Math.PI);
        rolloff = "+20";
      } else if (topology === "lc_lp") {
        fc = 1 / (2 * Math.PI * Math.sqrt(l * c));
        const q = (1 / r) * Math.sqrt(l / c) || 1.0;
        const ratio = testFreq / fc;
        const denom = Math.sqrt(Math.pow(1 - ratio * ratio, 2) + Math.pow(ratio / q, 2));
        gain = 1 / Math.max(0.00001, denom);
        phaseDeg = -Math.atan2(ratio / q, 1 - ratio * ratio) * (180 / Math.PI);
        rolloff = "-40";
      } else if (topology === "lc_hp") {
        fc = 1 / (2 * Math.PI * Math.sqrt(l * c));
        const q = (1 / r) * Math.sqrt(l / c) || 1.0;
        const ratio = testFreq / fc;
        const num = ratio * ratio;
        const denom = Math.sqrt(Math.pow(1 - ratio * ratio, 2) + Math.pow(ratio / q, 2));
        gain = num / Math.max(0.00001, denom);
        phaseDeg = (Math.PI - Math.atan2(ratio / q, 1 - ratio * ratio)) * (180 / Math.PI);
        rolloff = "+40";
      }

      const vout = vin * gain;
      const attenDb = 20 * Math.log10(Math.max(1e-6, gain));

      let fcDisplay = fc.toFixed(1) + " Hz";
      if (fc >= 1e6) {
        fcDisplay = (fc / 1e6).toFixed(3) + " MHz";
      } else if (fc >= 1e3) {
        fcDisplay = (fc / 1e3).toFixed(2) + " kHz";
      }

      document.getElementById("fcOut").innerText = fcDisplay;
      document.getElementById("gainOut").innerText = gain.toFixed(4);
      document.getElementById("attenDbOut").innerText = attenDb.toFixed(2) + " dB";
      document.getElementById("voutOut").innerText = vout.toFixed(3) + " V";
      document.getElementById("phaseOut").innerText = phaseDeg.toFixed(1) + "°";
      document.getElementById("rolloffOut").innerText = rolloff + " dB/dec";
    }

    document.addEventListener("DOMContentLoaded", function() {
      calculateFilter();
    });
  </script>
</body>
</html>
"""

def main():
    root = r"C:\Users\Admin\.gemini\antigravity\scratch\calchub"
    
    p1 = os.path.join(root, "fault-current-calculator.html")
    with open(p1, "w", encoding="utf-8") as f:
        f.write(TOOL_1_HTML.strip() + "\n")
    print("[PASS] fault-current-calculator.html generated successfully!")

    p2 = os.path.join(root, "filter-calculator.html")
    with open(p2, "w", encoding="utf-8") as f:
        f.write(TOOL_2_HTML.strip() + "\n")
    print("[PASS] filter-calculator.html generated successfully!")

if __name__ == "__main__":
    main()
