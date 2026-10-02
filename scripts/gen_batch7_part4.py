# -*- coding: utf-8 -*-
"""
Script to generate Batch 7 Part 4 tools:
7. cable-sizing-calculator-nec.html
8. copper-cable-sizing-calculator.html
"""
import os

TOOL_7_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cable Sizing Calculator NEC | National Electrical Code Wire Sizing</title>
  <meta name="description" content="Calculate electrical wire and cable sizes strictly compliant with NFPA 70 NEC Table 310.16. Accounts for continuous load 125% rule, conduit fill derating, ambient temperature adjustment, and 3% voltage drop.">
  <link rel="canonical" href="https://calchub.cloud/cable-sizing-calculator-nec.html">
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
        "name": "Cable Sizing Calculator NEC",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "National Electrical Code NFPA 70 branch circuit and feeder wire sizing engine applying NEC 310.16 ampacities, 125% continuous load rule, and conduit bundle derating.",
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
            "name": "What is the NEC 125% continuous load rule (NEC 210.19 and 215.2)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Under NEC Article 100, a continuous load is any load where the maximum current is expected to continue for 3 hours or more (such as commercial lighting, EV chargers, and office IT). NEC 210.19(A) and 215.2(A) require conductor ampacity and overcurrent protective devices to be sized for 100% of noncontinuous load plus 125% of continuous load before applying adjustment factors."
            }
          },
          {
            "@type": "Question",
            "name": "Why must 75°C ampacity be used even when installing 90°C THHN wire?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Under NEC 110.14(C), conductor termination ampacity is governed by the lowest temperature rating of any connected termination, lug, or circuit breaker. Most standard circuit breakers and panelboard lugs are rated for 75°C. Therefore, while 90°C wire (THHN/XHHW) can use the 90°C column for bundling and ambient derating, the final adjusted ampacity can never exceed the 75°C rating."
            }
          },
          {
            "@type": "Question",
            "name": "What are the conduit fill bundle adjustment factors in NEC Table 310.15(C)(1)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "When more than 3 current-carrying conductors are installed in a common raceway or cable, heat dissipation is restricted. NEC Table 310.15(C)(1) mandates derating factors: 4 to 6 conductors = 80%, 7 to 9 conductors = 70%, 10 to 20 conductors = 50%, and 21 to 30 conductors = 45%."
            }
          },
          {
            "@type": "Question",
            "name": "What are the NEC recommendations for voltage drop?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "While not strictly mandatory in the body of the NEC, Informational Notes in NEC 210.19(A) and 215.2(A)(1) recommend that total voltage drop should not exceed 3% on branch circuits or feeders, and total combined voltage drop from the service entrance to the furthest outlet should not exceed 5% for reasonable operating efficiency."
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
      <span>Cable Sizing NEC Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">NFPA 70 National Electrical Code (NEC)</div>
          <h1 class="calc-title">Cable Sizing Calculator NEC</h1>
          <p class="calc-tagline">Dimension copper and aluminum branch circuits and feeders compliant with NEC Table 310.16, 125% continuous load rule, and conduit fill.</p>
        </header>

        <!-- Tool Card -->
        <div class="tool-card">
          <form id="necForm" onsubmit="return false;">
            <div class="calc-grid">
              <div class="form-group">
                <label for="necSystemVoltage" class="form-label">System Supply Voltage</label>
                <select id="necSystemVoltage" class="form-control" onchange="calculateNec()">
                  <option value="120_1p">120V Single-Phase (2-Wire L-N)</option>
                  <option value="240_1p">240V Single-Phase (3-Wire Split Phase)</option>
                  <option value="208_3p">208V Three-Phase (4-Wire Wye)</option>
                  <option value="480_3p" selected>480V Three-Phase (4-Wire Commercial/Industrial)</option>
                  <option value="277_1p">277V Single-Phase (Commercial Lighting)</option>
                </select>
                <small class="form-hint">Nominal line-to-line or line-to-neutral voltage</small>
              </div>

              <div class="form-group">
                <label for="necConductor" class="form-label">Conductor Metal</label>
                <select id="necConductor" class="form-control" onchange="calculateNec()">
                  <option value="copper" selected>Copper Conductor (Cu)</option>
                  <option value="aluminum">Aluminum / Copper-Clad Al (Al)</option>
                </select>
                <small class="form-hint">Conductor metallurgy</small>
              </div>

              <div class="form-group">
                <label for="necInsulation" class="form-label">Insulation &amp; Temperature Rating</label>
                <select id="necInsulation" class="form-control" onchange="calculateNec()">
                  <option value="90" selected>THHN / THWN-2 / XHHW-2 (90°C Dry/Wet)</option>
                  <option value="75">THW / THWN / RHW (75°C Wet/Dry)</option>
                  <option value="60">TW / UF (60°C Residential)</option>
                </select>
                <small class="form-hint">NEC Table 310.16 insulation column</small>
              </div>

              <div class="form-group">
                <label for="necTerminalRating" class="form-label">Terminal / Lug Temperature Limit</label>
                <select id="necTerminalRating" class="form-control" onchange="calculateNec()">
                  <option value="75" selected>75°C Terminals (Standard Circuit Breakers &gt; 100A / AL9CU)</option>
                  <option value="60">60°C Terminals (Appliances &amp; Breakers &le; 100A)</option>
                </select>
                <small class="form-hint">NEC 110.14(C) termination limit</small>
              </div>

              <div class="form-group">
                <label for="necContinuousLoad" class="form-label">Continuous Load ($I_{cont}$)</label>
                <div class="input-with-unit">
                  <input type="number" id="necContinuousLoad" class="form-control" value="80" min="0" step="5" oninput="calculateNec()">
                  <span class="unit-badge">Amps</span>
                </div>
                <small class="form-hint">Operating &ge; 3 hours (Subject to 125% factor)</small>
              </div>

              <div class="form-group">
                <label for="necNonContLoad" class="form-label">Non-Continuous Load ($I_{noncont}$)</label>
                <div class="input-with-unit">
                  <input type="number" id="necNonContLoad" class="form-control" value="20" min="0" step="5" oninput="calculateNec()">
                  <span class="unit-badge">Amps</span>
                </div>
                <small class="form-hint">Intermittent / cyclical load (100% factor)</small>
              </div>

              <div class="form-group">
                <label for="necAmbientTempF" class="form-label">Ambient Temperature</label>
                <div class="input-with-unit">
                  <input type="number" id="necAmbientTempF" class="form-control" value="86" min="50" max="150" step="2" oninput="calculateNec()">
                  <span class="unit-badge">°F</span>
                </div>
                <small class="form-hint">NEC Table 310.16 baseline is 86°F (30°C)</small>
              </div>

              <div class="form-group">
                <label for="necConductorCount" class="form-label">Conductors in Raceway</label>
                <select id="necConductorCount" class="form-control" onchange="calculateNec()">
                  <option value="1.0" selected>1 to 3 Current-Carrying (100% - No Derate)</option>
                  <option value="0.80">4 to 6 Conductors (80% Derate)</option>
                  <option value="0.70">7 to 9 Conductors (70% Derate)</option>
                  <option value="0.50">10 to 20 Conductors (50% Derate)</option>
                  <option value="0.45">21 to 30 Conductors (45% Derate)</option>
                </select>
                <small class="form-hint">NEC Table 310.15(C)(1) adjustment</small>
              </div>

              <div class="form-group">
                <label for="necRouteDistance" class="form-label">One-Way Run Length ($L$)</label>
                <div class="input-with-unit">
                  <input type="number" id="necRouteDistance" class="form-control" value="150" min="1" step="10" oninput="calculateNec()">
                  <span class="unit-badge">feet</span>
                </div>
                <small class="form-hint">Length from panel to load in feet</small>
              </div>

              <div class="form-group">
                <label for="necMaxVd" class="form-label">Max Allowable Voltage Drop</label>
                <div class="input-with-unit">
                  <input type="number" id="necMaxVd" class="form-control" value="3.0" min="1.0" max="10.0" step="0.5" oninput="calculateNec()">
                  <span class="unit-badge">%</span>
                </div>
                <small class="form-hint">NEC Informational Note recommendation</small>
              </div>
            </div>

            <button type="button" id="calcNecBtn" class="btn btn-primary btn-block" onclick="calculateNec()">Size Conductor (NFPA 70 NEC)</button>
          </form>

          <div id="necResultBox" class="results-container" style="margin-top:20px;">
            <h3>NEC Conductor Sizing Summary</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label">Recommended Conductor Size</span>
                <span id="necSizeOut" class="result-value">-- AWG/kcmil</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Minimum Required Circuit Ampacity (MCA)</span>
                <span id="necMcaOut" class="result-value">-- A</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Adjusted Allowable Ampacity</span>
                <span id="necAmpacityOut" class="result-value">-- A</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Standard Overcurrent Device (OCPD)</span>
                <span id="necOcpdOut" class="result-value">-- A Breaker</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Calculated Voltage Drop ($\Delta V$)</span>
                <span id="necVdOut" class="result-value">-- V (-- %)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">NEC Code Compliance Verification</span>
                <span id="necStatusOut" class="result-value">--</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Comprehensive Guide to Wire Sizing per the National Electrical Code (NEC)</h2>
          
          <p>In the United States and jurisdictions adopting NFPA 70 standards, sizing low-voltage electrical branch circuits, feeders, and service entrance conductors is governed by the <strong>National Electrical Code (NEC)</strong>. Conductor dimensioning under the NEC is not a simple table lookup; it requires navigating a multi-layered hierarchy of statutory requirements: continuous load factors, ambient temperature adjustments, conduit bundling deratings, terminal temperature limitations, overcurrent protection sizing, and line impedance voltage drop control.</p>

          <div class="formula-box">
            <h3>The 125% Continuous Load Rule: NEC 210.19(A) &amp; NEC 215.2(A)</h3>
            <p>Under NEC Article 100, a <em>continuous load</em> is defined as an electrical load where the maximum current is sustained for 3 hours or more (e.g. store lighting, office computer servers, commercial refrigeration, electric vehicle charging). To protect circuit breakers and panelboards from thermal accumulation, the minimum circuit ampacity ($MCA$) must be sized for $125\%$ of continuous loads plus $100\%$ of noncontinuous loads:</p>
            <p>$$I_{min} \ge (1.25 \times I_{continuous}) + I_{noncontinuous}$$</p>
            <p>Furthermore, per NEC 240.4 and 240.6, the overcurrent protective device (circuit breaker or fuse) must have a standard rating not less than $I_{min}$.</p>
          </div>

          <h3>NEC Table 310.16 Ampacity Columns &amp; Terminal Limitations (NEC 110.14(C))</h3>
          <p>NEC Table 310.16 (formerly Table 310.15(B)(16)) provides allowable ampacities of insulated conductors rated up to $2000\text{ Volts}$, based on three temperature columns: $60^\circ\text{C}$, $75^\circ\text{C}$, and $90^\circ\text{C}$.</p>

          <p>A frequent error among electrical designers is assuming a conductor with $90^\circ\text{C}$ insulation (such as THHN or XHHW-2) can always be operated at its full $90^\circ\text{C}$ ampacity. <strong>NEC 110.14(C) strictly mandates that conductor ampacity is limited by the temperature rating of the connected equipment terminals:</strong></p>
          <ul>
            <li><strong>Equipment rated 100A or less (or marked for #14 through #1 AWG):</strong> Conductor sizing must be based on the $60^\circ\text{C}$ ampacity column, unless the equipment and terminals are specifically listed and labeled for $75^\circ\text{C}$.</li>
            <li><strong>Equipment rated over 100A (or marked for conductors larger than #1 AWG):</strong> Sizing is based on the $75^\circ\text{C}$ column.</li>
            <li><strong>The 90°C Derating Benefit:</strong> You CAN utilize the higher $90^\circ\text{C}$ column as the <em>starting point</em> for mathematical bundling and ambient temperature derating calculations, provided the final derated ampacity does not exceed the terminal rating ($75^\circ\text{C}$ column value).</li>
          </ul>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Conductor Size (AWG / kcmil)</th>
                <th>Copper 60°C (TW)</th>
                <th>Copper 75°C (THWN)</th>
                <th>Copper 90°C (THHN/XHHW)</th>
                <th>Aluminum 75°C (THWN)</th>
                <th>Aluminum 90°C (XHHW-2)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>#14 AWG</strong></td>
                <td>15 A</td>
                <td>20 A</td>
                <td>25 A</td>
                <td>--</td>
                <td>--</td>
              </tr>
              <tr>
                <td><strong>#12 AWG</strong></td>
                <td>20 A</td>
                <td>25 A</td>
                <td>30 A</td>
                <td>20 A</td>
                <td>25 A</td>
              </tr>
              <tr>
                <td><strong>#10 AWG</strong></td>
                <td>30 A</td>
                <td>35 A</td>
                <td>40 A</td>
                <td>30 A</td>
                <td>35 A</td>
              </tr>
              <tr>
                <td><strong>#8 AWG</strong></td>
                <td>40 A</td>
                <td>50 A</td>
                <td>55 A</td>
                <td>40 A</td>
                <td>45 A</td>
              </tr>
              <tr>
                <td><strong>#6 AWG</strong></td>
                <td>55 A</td>
                <td>65 A</td>
                <td>75 A</td>
                <td>50 A</td>
                <td>60 A</td>
              </tr>
              <tr>
                <td><strong>#4 AWG</strong></td>
                <td>70 A</td>
                <td>85 A</td>
                <td>95 A</td>
                <td>65 A</td>
                <td>75 A</td>
              </tr>
              <tr>
                <td><strong>#2 AWG</strong></td>
                <td>95 A</td>
                <td>115 A</td>
                <td>130 A</td>
                <td>90 A</td>
                <td>100 A</td>
              </tr>
              <tr>
                <td><strong>#1/0 AWG</strong></td>
                <td>125 A</td>
                <td>150 A</td>
                <td>170 A</td>
                <td>120 A</td>
                <td>135 A</td>
              </tr>
              <tr>
                <td><strong>#2/0 AWG</strong></td>
                <td>145 A</td>
                <td>175 A</td>
                <td>195 A</td>
                <td>135 A</td>
                <td>150 A</td>
              </tr>
              <tr>
                <td><strong>#4/0 AWG</strong></td>
                <td>195 A</td>
                <td>230 A</td>
                <td>260 A</td>
                <td>180 A</td>
                <td>205 A</td>
              </tr>
              <tr>
                <td><strong>250 kcmil</strong></td>
                <td>215 A</td>
                <td>255 A</td>
                <td>290 A</td>
                <td>205 A</td>
                <td>230 A</td>
              </tr>
              <tr>
                <td><strong>500 kcmil</strong></td>
                <td>320 A</td>
                <td>380 A</td>
                <td>430 A</td>
                <td>310 A</td>
                <td>350 A</td>
              </tr>
            </tbody>
          </table>

          <div class="formula-box">
            <h3>Conduit Bundle &amp; Ambient Temperature Adjustment Factors</h3>
            <p>When conductors are installed in environments where ambient temperature deviates from $86^\circ\text{F}$ ($30^\circ\text{C}$), or where more than 3 current-carrying conductors share a raceway, the allowable ampacity is derated:</p>
            <p>$$I_{adjusted} = I_{table,90^\circ\text{C}} \times K_{temp} \times K_{bundle}$$</p>
            <p>Under NEC Table 310.15(B)(1) / Table 310.16 correction factors for $90^\circ\text{C}$ rated wire:</p>
            <ul>
              <li>Ambient $96^\circ\text{F} - 104^\circ\text{F}$ ($36^\circ\text{C} - 40^\circ\text{C}$): $K_{temp} = 0.91$</li>
              <li>Ambient $105^\circ\text{F} - 113^\circ\text{F}$ ($41^\circ\text{C} - 45^\circ\text{C}$): $K_{temp} = 0.87$</li>
              <li>Ambient $114^\circ\text{F} - 122^\circ\text{F}$ ($46^\circ\text{C} - 50^\circ\text{C}$): $K_{temp} = 0.82$</li>
            </ul>
            <p>Under NEC Table 310.15(C)(1) for conductors in conduit:</p>
            <ul>
              <li>4 to 6 current-carrying conductors: $K_{bundle} = 0.80$</li>
              <li>7 to 9 current-carrying conductors: $K_{bundle} = 0.70$</li>
              <li>10 to 20 current-carrying conductors: $K_{bundle} = 0.50$</li>
            </ul>
          </div>

          <div class="worked-example-card">
            <h3>Practical Worked Engineering Example: Commercial 480V Feeder Sizing</h3>
            <p><strong>Design Scenario:</strong> Size a three-phase, 480V, 4-wire copper feeder supplying a commercial rooftop air handler. The continuous cooling load is $I_{cont} = 80\text{ A}$ and noncontinuous auxiliary heating load is $I_{noncont} = 20\text{ A}$. The feeder is routed inside EMT conduit along a rooftop where ambient temperature reaches $104^\circ\text{F}$ ($40^\circ\text{C}$). The conduit contains 4 current-carrying conductors (3 phases plus a neutral carrying harmonic imbalance). The circuit length is $150\text{ feet}$. Panelboard terminals are rated for $75^\circ\text{C}$. Maximum allowable voltage drop is $3.0\%$. Conductor specified is copper THHN ($90^\circ\text{C}$).</p>

            <p><strong>Step 1: Compute Minimum Circuit Ampacity (MCA)</strong></p>
            <p>$$MCA = (1.25 \times I_{cont}) + I_{noncont} = (1.25 \times 80\text{ A}) + 20\text{ A} = 100\text{ A} + 20\text{ A} = 120\text{ A}$$</p>
            <p>A standard $125\text{ A}$ circuit breaker is selected ($I_{ocpd} = 125\text{ A}$).</p>

            <p><strong>Step 2: Evaluate Environmental Derating Factors</strong></p>
            <p>For $90^\circ\text{C}$ THHN at $104^\circ\text{F}$, $K_{temp} = 0.91$.</p>
            <p>For 4 current-carrying conductors in conduit, $K_{bundle} = 0.80$.</p>
            <p>Combined factor = $0.91 \times 0.80 = 0.728$.</p>

            <p><strong>Step 3: Select Conductor Size to Satisfy Derating</strong></p>
            <p>The required $90^\circ\text{C}$ table ampacity before derating must be:</p>
            <p>$$I_{table,req} \ge \frac{MCA}{0.728} = \frac{120\text{ A}}{0.728} = 164.8\text{ A}$$</p>
            <p>Referring to NEC Table 310.16 ($90^\circ\text{C}$ Copper):</p>
            <ul>
              <li>#1 AWG Cu $\implies 145\text{ A}$ ($145 < 164.8 \implies$ Insufficient)</li>
              <li>#1/0 AWG Cu $\implies 170\text{ A}$ ($170 \ge 164.8 \implies$ Compliant!)</li>
            </ul>
            <p>Derated ampacity of #1/0 AWG Cu: $170\text{ A} \times 0.728 = 123.76\text{ A} \ge 120\text{ A}$.</p>
            <p>Check $75^\circ\text{C}$ terminal limit: #1/0 AWG Cu is rated $150\text{ A}$ at $75^\circ\text{C}$. Since $123.76\text{ A} \le 150\text{ A}$, the terminal rule is satisfied.</p>

            <p><strong>Step 4: Verification of Voltage Drop on #1/0 AWG Copper</strong></p>
            <p>Operating running current $I = 80 + 20 = 100\text{ A}$. From NEC Chapter 9 Table 8, DC resistance of #1/0 uncoated copper is $0.122\ \Omega/\text{kft}$:</p>
            <p>$$\Delta V_{3\phi} = \frac{\sqrt{3} \times I \times L \times R}{1000} = \frac{1.732 \times 100\text{ A} \times 150\text{ ft} \times 0.122}{1000} = 3.17\text{ Volts}$$</p>
            <p>$$\Delta V\% = \frac{3.17\text{ V}}{480\text{ V}} \times 100 = 0.66\%$$</p>
            <p>Since $0.66\% \ll 3.0\%$, #1/0 AWG Copper THHN is completely compliant with all NEC articles.</p>
          </div>

          <h2>Frequently Asked Questions (NEC Wire Sizing)</h2>
          <div class="faq-item">
            <h3>What is the "Next Higher Standard Breaker Size" rule (NEC 240.4(B))?</h3>
            <p>If the calculated ampacity of a conductor does not correspond to a standard circuit breaker rating listed in NEC 240.6, the code permits rounding up to the next higher standard rating, provided: (1) the circuit is not part of a multi-outlet branch circuit supplying receptacles, (2) the conductor ampacity is not exceeded by the next higher rating if it exceeds 800A, and (3) the rating does not exceed 800A.</p>
          </div>

          <div class="faq-item">
            <h3>How is neutral conductor count determined for conduit derating?</h3>
            <p>Under NEC 310.15(E)(1), a neutral conductor that carries only unbalanced current from other conductors of the same circuit is NOT counted as a current-carrying conductor. However, under NEC 310.15(E)(3), if the major portion of the load consists of non-linear loads (computers, LED electronic ballasts), triplen harmonic currents add in the neutral, and the neutral MUST be counted as a current-carrying conductor.</p>
          </div>

          <div class="faq-item">
            <h3>What are the small conductor rules in NEC 240.4(D)?</h3>
            <p>Unless specifically permitted for motor circuits or HVAC loads, the maximum overcurrent protection for small copper conductors is strictly limited: #14 AWG Cu is limited to 15A breaker, #12 AWG Cu is limited to 20A breaker, and #10 AWG Cu is limited to 30A breaker, regardless of higher values in the 75°C or 90°C ampacity columns.</p>
          </div>

          <div class="faq-item">
            <h3>When must aluminum wire be upsized compared to copper under the NEC?</h3>
            <p>Because electrical grade aluminum (AA-8000 series alloy) has higher electrical resistivity than copper, aluminum requires an area roughly two standard trade sizes larger to carry the equivalent ampacity. For example, a 100A circuit requires #3 AWG or #2 AWG copper, whereas aluminum requires #1 AWG or #1/0 AWG.</p>
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
    // NEC Table 310.16 Copper and Aluminum Ampacities
    const necTableData = [
      { size: "14 AWG",   cu60: 15, cu75: 20, cu90: 25, al75: 0,   al90: 0,   r_cu: 3.07,  r_al: 5.06 },
      { size: "12 AWG",   cu60: 20, cu75: 25, cu90: 30, al75: 20,  al90: 25,  r_cu: 1.93,  r_al: 3.18 },
      { size: "10 AWG",   cu60: 30, cu75: 35, cu90: 40, al75: 30,  al90: 35,  r_cu: 1.21,  r_al: 2.00 },
      { size: "8 AWG",    cu60: 40, cu75: 50, cu90: 55, al75: 40,  al90: 45,  r_cu: 0.764, r_al: 1.26 },
      { size: "6 AWG",    cu60: 55, cu75: 65, cu90: 75, al75: 50,  al90: 60,  r_cu: 0.491, r_al: 0.808 },
      { size: "4 AWG",    cu60: 70, cu75: 85, cu90: 95, al75: 65,  al90: 75,  r_cu: 0.308, r_al: 0.508 },
      { size: "3 AWG",    cu60: 85, cu75: 100, cu90: 115, al75: 75, al90: 85, r_cu: 0.245, r_al: 0.403 },
      { size: "2 AWG",    cu60: 95, cu75: 115, cu90: 130, al75: 90, al90: 100, r_cu: 0.194, r_al: 0.319 },
      { size: "1 AWG",    cu60: 110, cu75: 130, cu90: 145, al75: 100, al90: 115, r_cu: 0.154, r_al: 0.253 },
      { size: "1/0 AWG",  cu60: 125, cu75: 150, cu90: 170, al75: 120, al90: 135, r_cu: 0.122, r_al: 0.201 },
      { size: "2/0 AWG",  cu60: 145, cu75: 175, cu90: 195, al75: 135, al90: 150, r_cu: 0.0967, r_al: 0.159 },
      { size: "3/0 AWG",  cu60: 165, cu75: 200, cu90: 225, al75: 155, al90: 175, r_cu: 0.0766, r_al: 0.126 },
      { size: "4/0 AWG",  cu60: 195, cu75: 230, cu90: 260, al75: 180, al90: 205, r_cu: 0.0608, r_al: 0.100 },
      { size: "250 kcmil", cu60: 215, cu75: 255, cu90: 290, al75: 205, al90: 230, r_cu: 0.0515, r_al: 0.0847 },
      { size: "300 kcmil", cu60: 240, cu75: 285, cu90: 320, al75: 230, al90: 255, r_cu: 0.0429, r_al: 0.0707 },
      { size: "350 kcmil", cu60: 260, cu75: 310, cu90: 350, al75: 250, al90: 280, r_cu: 0.0367, r_al: 0.0605 },
      { size: "400 kcmil", cu60: 280, cu75: 335, cu90: 380, al75: 270, al90: 305, r_cu: 0.0321, r_al: 0.0529 },
      { size: "500 kcmil", cu60: 320, cu75: 380, cu90: 430, al75: 310, al90: 350, r_cu: 0.0258, r_al: 0.0424 }
    ];

    const standardBreakers = [15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 125, 150, 175, 200, 225, 250, 300, 350, 400, 450, 500, 600];

    function calculateNec() {
      const sysVolt = document.getElementById("necSystemVoltage").value;
      const conductor = document.getElementById("necConductor").value;
      const insulTemp = document.getElementById("necInsulation").value;
      const termRating = document.getElementById("necTerminalRating").value;
      const iCont = parseFloat(document.getElementById("necContinuousLoad").value) || 0;
      const iNonCont = parseFloat(document.getElementById("necNonContLoad").value) || 0;
      const tempF = parseFloat(document.getElementById("necAmbientTempF").value) || 86;
      const bundleDerate = parseFloat(document.getElementById("necConductorCount").value) || 1.0;
      const lengthFt = parseFloat(document.getElementById("necRouteDistance").value) || 1;
      const maxVdPct = parseFloat(document.getElementById("necMaxVd").value) || 3.0;

      // Minimum Circuit Ampacity (MCA)
      const mca = (iCont * 1.25) + iNonCont;
      const totalOperatingI = iCont + iNonCont;

      // Find standard breaker rating >= MCA
      let ocpd = standardBreakers[standardBreakers.length - 1];
      for (let i = 0; i < standardBreakers.length; i++) {
        if (standardBreakers[i] >= mca) {
          ocpd = standardBreakers[i];
          break;
        }
      }

      // Ambient temp correction factor (Table 310.16)
      let kTemp = 1.0;
      if (tempF > 86) {
        if (insulTemp === "90") {
          if (tempF <= 95) kTemp = 0.96;
          else if (tempF <= 104) kTemp = 0.91;
          else if (tempF <= 113) kTemp = 0.87;
          else if (tempF <= 122) kTemp = 0.82;
          else if (tempF <= 131) kTemp = 0.76;
          else kTemp = 0.71;
        } else {
          if (tempF <= 95) kTemp = 0.94;
          else if (tempF <= 104) kTemp = 0.88;
          else if (tempF <= 113) kTemp = 0.82;
          else if (tempF <= 122) kTemp = 0.75;
          else kTemp = 0.67;
        }
      }

      const totalDerating = kTemp * bundleDerate;

      // Voltage nominal and phasing
      let vNom = 480;
      let is3ph = true;
      if (sysVolt === "120_1p") { vNom = 120; is3ph = false; }
      else if (sysVolt === "240_1p") { vNom = 240; is3ph = false; }
      else if (sysVolt === "277_1p") { vNom = 277; is3ph = false; }
      else if (sysVolt === "208_3p") { vNom = 208; is3ph = true; }
      else if (sysVolt === "480_3p") { vNom = 480; is3ph = true; }

      let selected = null;

      for (let i = 0; i < necTableData.length; i++) {
        const row = necTableData[i];
        let baseRating = 0;
        let termLimitRating = 0;

        if (conductor === "copper") {
          baseRating = (insulTemp === "90") ? row.cu90 : ((insulTemp === "75") ? row.cu75 : row.cu60);
          termLimitRating = (termRating === "60") ? row.cu60 : row.cu75;
        } else {
          if (row.al75 === 0) continue; // No #14 aluminum
          baseRating = (insulTemp === "90") ? row.al90 : row.al75;
          termLimitRating = row.al75;
        }

        // Apply derating to 90C value, but cap by terminal rating
        const deratedAmpacity = baseRating * totalDerating;
        const allowableAmpacity = Math.min(deratedAmpacity, termLimitRating);

        // Check if allowable ampacity satisfies MCA
        if (allowableAmpacity < mca) continue;

        // Check small conductor rules for 15A/20A/30A
        if (conductor === "copper") {
          if (row.size === "14 AWG" && ocpd > 15) continue;
          if (row.size === "12 AWG" && ocpd > 20) continue;
          if (row.size === "10 AWG" && ocpd > 30) continue;
        }

        // Voltage drop calculation
        const resPerKft = (conductor === "copper") ? row.r_cu : row.r_al;
        let deltaV = 0;
        if (is3ph) {
          deltaV = (1.732 * totalOperatingI * lengthFt * resPerKft) / 1000;
        } else {
          deltaV = (2 * totalOperatingI * lengthFt * resPerKft) / 1000;
        }

        const vdPct = (deltaV / vNom) * 100;

        if (vdPct <= maxVdPct) {
          selected = {
            size: row.size,
            allowableAmpacity: allowableAmpacity,
            deltaV: deltaV,
            vdPct: vdPct
          };
          break;
        }
      }

      document.getElementById("necMcaOut").innerText = mca.toFixed(1) + " A";
      document.getElementById("necOcpdOut").innerText = ocpd + " A Standard Breaker";

      if (selected) {
        document.getElementById("necSizeOut").innerText = selected.size + " (" + conductor.toUpperCase() + ")";
        document.getElementById("necAmpacityOut").innerText = selected.allowableAmpacity.toFixed(1) + " A";
        document.getElementById("necVdOut").innerText = selected.deltaV.toFixed(2) + " V (" + selected.vdPct.toFixed(2) + "%)";
        document.getElementById("necStatusOut").innerText = "Fully Compliant with NEC 310.16 & 110.14(C)";
        document.getElementById("necStatusOut").style.color = "#10b981";
      } else {
        document.getElementById("necSizeOut").innerText = "> 500 kcmil (Parallel Runs Needed)";
        document.getElementById("necAmpacityOut").innerText = "--";
        document.getElementById("necVdOut").innerText = "Exceeds Drop Limit";
        document.getElementById("necStatusOut").innerText = "Non-Compliant: Parallel Feeders Required";
        document.getElementById("necStatusOut").style.color = "#ef4444";
      }
    }

    document.addEventListener("DOMContentLoaded", function() {
      calculateNec();
    });
  </script>
</body>
</html>
"""

TOOL_8_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Copper Cable Sizing Calculator | Electrical Conductor Dimensions & Voltage Drop</title>
  <meta name="description" content="Calculate pure copper electrical cable cross-section (mm² and AWG). Computes temperature-adjusted copper DC/AC resistance, continuous ampacity, voltage drop, and I²R power loss.">
  <link rel="canonical" href="https://calchub.cloud/copper-cable-sizing-calculator.html">
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
        "name": "Copper Cable Sizing Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "High-precision electrical copper cable sizing calculator computing temperature-dependent resistivity (100% IACS ETP Cu), continuous ampacity, line voltage drop, and annual kilowatt-hour joule losses.",
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
            "name": "Why is copper the global benchmark conductor in electrical engineering?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Copper establishes the International Annealed Copper Standard (100% IACS). It possesses an extremely low electrical resistivity (1.724 x 10^-8 Ohm-m at 20°C), superior tensile strength (200 to 400 MPa), exceptional thermal conductivity (390 W/m-K), high resistance to terminal creep, and forms a conductive copper oxide film that prevents thermal runaway at lug terminations."
            }
          },
          {
            "@type": "Question",
            "name": "How does operating temperature increase copper electrical resistance?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Copper has a positive temperature coefficient of resistance (alpha_20 = 0.00393 per °C). As current heats the conductor, resistance increases according to: R_T = R_20 * [1 + 0.00393 * (T - 20)]. When copper rises from 20°C to 75°C under continuous load, its electrical resistance increases by 21.6%."
            }
          },
          {
            "@type": "Question",
            "name": "What is the economic cost of undersizing copper conductors (I²R loss)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Conductors dissipate electrical energy as heat equal to P = I² * R. Sizing a cable strictly to thermal ampacity minimums results in high operating temperatures and continuous energy waste. Selecting one standard size larger copper cable reduces line resistance, frequently paying for its extra initial copper cost within 2 to 3 years through lower lifetime electricity bills."
            }
          },
          {
            "@type": "Question",
            "name": "How does copper compare directly to aluminum in cross-sectional area?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Electrical aluminum (6101-T6 alloy) has a conductivity of roughly 61% IACS compared to 100% for copper. To achieve the exact same DC line resistance and voltage drop, an aluminum conductor must have a cross-sectional area 1.64 times larger than an equivalent copper conductor (A_Al = 1.64 * A_Cu)."
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
      <span>Copper Cable Sizing Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">Electrolytic Tough Pitch (ETP Cu) 100% IACS</div>
          <h1 class="calc-title">Copper Cable Sizing Calculator</h1>
          <p class="calc-tagline">Calculate optimal copper conductor cross-section, temperature-adjusted resistance, continuous current capacity, and annual $I^2R$ power loss.</p>
        </header>

        <!-- Tool Card -->
        <div class="tool-card">
          <form id="cuForm" onsubmit="return false;">
            <div class="calc-grid">
              <div class="form-group">
                <label for="cuSystemSupply" class="form-label">System Phasing &amp; Voltage</label>
                <select id="cuSystemSupply" class="form-control" onchange="calculateCopper()">
                  <option value="400_3p" selected>Three-Phase 400V AC (50/60 Hz)</option>
                  <option value="230_1p">Single-Phase 230V AC (50/60 Hz)</option>
                  <option value="480_3p">Three-Phase 480V AC (North American Industrial)</option>
                  <option value="120_1p">Single-Phase 120V AC</option>
                </select>
                <small class="form-hint">Nominal circuit voltage</small>
              </div>

              <div class="form-group">
                <label for="cuInsulation" class="form-label">Insulation Thermal Class</label>
                <select id="cuInsulation" class="form-control" onchange="calculateCopper()">
                  <option value="xlpe" selected>XLPE / EPR Thermosetting (Max 90°C)</option>
                  <option value="pvc70">PVC Thermoplastic (Max 70°C)</option>
                  <option value="pvc75">THWN / 75°C Moisture Resistant</option>
                </select>
                <small class="form-hint">Max continuous core temperature</small>
              </div>

              <div class="form-group">
                <label for="cuDesignCurrent" class="form-label">Operating Load Current ($I$)</label>
                <div class="input-with-unit">
                  <input type="number" id="cuDesignCurrent" class="form-control" value="70" min="1" step="1" oninput="calculateCopper()">
                  <span class="unit-badge">Amps</span>
                </div>
                <small class="form-hint">Continuous operating RMS current</small>
              </div>

              <div class="form-group">
                <label for="cuAmbientTemp" class="form-label">Ambient Temperature ($T_{amb}$)</label>
                <div class="input-with-unit">
                  <input type="number" id="cuAmbientTemp" class="form-control" value="30" min="10" max="60" step="1" oninput="calculateCopper()">
                  <span class="unit-badge">°C</span>
                </div>
                <small class="form-hint">Local room or conduit temperature</small>
              </div>

              <div class="form-group">
                <label for="cuRouteLength" class="form-label">One-Way Circuit Length ($L$)</label>
                <div class="input-with-unit">
                  <input type="number" id="cuRouteLength" class="form-control" value="60" min="1" step="5" oninput="calculateCopper()">
                  <span class="unit-badge">metres</span>
                </div>
                <small class="form-hint">Route distance from source to load</small>
              </div>

              <div class="form-group">
                <label for="cuMaxVd" class="form-label">Max Allowable Voltage Drop</label>
                <div class="input-with-unit">
                  <input type="number" id="cuMaxVd" class="form-control" value="3.5" min="1.0" max="10.0" step="0.1" oninput="calculateCopper()">
                  <span class="unit-badge">%</span>
                </div>
                <small class="form-hint">Efficiency &amp; standards ceiling</small>
              </div>

              <div class="form-group">
                <label for="electricityCostKwh" class="form-label">Electricity Cost</label>
                <div class="input-with-unit">
                  <input type="number" id="electricityCostKwh" class="form-control" value="0.16" min="0.01" step="0.01" oninput="calculateCopper()">
                  <span class="unit-badge">$/kWh</span>
                </div>
                <small class="form-hint">Commercial rate for loss economics</small>
              </div>

              <div class="form-group">
                <label for="annualHours" class="form-label">Annual Operational Hours</label>
                <div class="input-with-unit">
                  <input type="number" id="annualHours" class="form-control" value="5000" min="500" max="8760" step="500" oninput="calculateCopper()">
                  <span class="unit-badge">hrs/yr</span>
                </div>
                <small class="form-hint">5000h = 16h/day industrial shift</small>
              </div>
            </div>

            <button type="button" id="calcCuBtn" class="btn btn-primary btn-block" onclick="calculateCopper()">Calculate Copper Dimensions</button>
          </form>

          <div id="cuResultBox" class="results-container" style="margin-top:20px;">
            <h3>Copper Cable Engineering Output</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label">Recommended Copper Cross-Section</span>
                <span id="cuSizeOut" class="result-value">-- mm²</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Operating Temperature Line Resistance ($R_T$)</span>
                <span id="cuResistanceOut" class="result-value">-- &Omega;</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Line-to-Line Voltage Drop ($\Delta V$)</span>
                <span id="cuVdOut" class="result-value">-- V (-- %)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Three-Phase $I^2R$ Power Loss</span>
                <span id="cuPowerLossOut" class="result-value">-- Watts</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Annual Energy Loss Cost</span>
                <span id="cuAnnualCostOut" class="result-value">-- $/year</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Equivalent Aluminum Size Required</span>
                <span id="cuAlEquivOut" class="result-value">-- mm² Al</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Engineering Metallurgical Principles of Copper Cable Sizing</h2>
          
          <p>Since the dawn of modern commercial electrification, copper has served as the universal international standard of electrical conduction. In 1913, the International Electrotechnical Commission codified the <strong>International Annealed Copper Standard (IACS)</strong>, defining $100\%$ conductivity as an annealed copper wire with a density of $8.89\text{ g/cm}^3$, a length of one meter, and a mass of one gram having an electrical resistance of exactly $0.15328\ \Omega$ at $20^\circ\text{C}$ (corresponding to a volume resistivity of $\rho_{20} = 1.7241 \times 10^{-8}\ \Omega\cdot\text{m}$).</p>

          <p>Modern electrical power cables are manufactured from <strong>Electrolytic Tough Pitch Copper (ETP Cu, UNS C11000)</strong>, refined to a minimum purity of $99.90\%$ copper with controlled residual oxygen content ($0.02\%$ to $0.04\%$). Understanding the exact thermodynamic and physical behavior of copper conductors under heavy operational currents is essential for safe sizing, voltage stability, and life-cycle energy efficiency.</p>

          <div class="formula-box">
            <h3>Temperature Dependence of Copper Electrical Resistance</h3>
            <p>Unlike superconductors, copper exhibits a positive temperature coefficient of electrical resistance ($\alpha_{20} = 0.00393\ ^\circ\text{C}^{-1}$ at $20^\circ\text{C}$). As electrical current flows through the copper core, joule heating ($I^2 R$) raises the metal lattice temperature. Increased atomic thermal vibrations scatter conducting valence electrons, increasing electrical resistivity:</p>
            <p>$$R_T = R_{20} \times [1 + \alpha_{20} (T - 20)]$$</p>
            <p>Where $R_{20}$ is the baseline DC resistance at $20^\circ\text{C}$, $T$ is the continuous operating core temperature, and $\alpha_{20} = 0.00393\ ^\circ\text{C}^{-1}$.</p>
            <ul>
              <li>At $20^\circ\text{C}$: Resistivity $\rho = 1.724 \times 10^{-8}\ \Omega\cdot\text{m}$ ($100\%$ baseline)</li>
              <li>At $70^\circ\text{C}$ (PVC limit): $R_{70} = R_{20} [1 + 0.00393(50)] = 1.1965 \times R_{20}$ (a $+19.7\%$ increase in line resistance!)</li>
              <li>At $90^\circ\text{C}$ (XLPE limit): $R_{90} = R_{20} [1 + 0.00393(70)] = 1.2751 \times R_{20}$ (a $+27.5\%$ increase in line resistance!)</li>
            </ul>
            <p><em>Engineering Rule:</em> Failing to adjust copper resistance for maximum operating temperature results in underestimating real-world line voltage drop and power loss by up to $27.5\%$!</p>
          </div>

          <h3>Copper versus Aluminum: Direct Metallurgical Comparison</h3>
          <p>Electrical engineers frequently evaluate copper versus electrical grade aluminum (AA-8000 alloy). The physical properties dictate distinct design choices:</p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Physical Property</th>
                <th>Electrolytic Copper (ETP Cu)</th>
                <th>Electrical Grade Aluminum (AA-8000)</th>
                <th>Engineering Implication</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Electrical Conductivity</strong></td>
                <td>$100\%$ IACS ($5.80 \times 10^7\text{ S/m}$)</td>
                <td>$61\%$ IACS ($3.54 \times 10^7\text{ S/m}$)</td>
                <td>Aluminum requires $1.64\times$ greater cross-sectional area to match copper DC resistance</td>
              </tr>
              <tr>
                <td><strong>Mass Density</strong></td>
                <td>$8.89\text{ g/cm}^3$</td>
                <td>$2.70\text{ g/cm}^3$</td>
                <td>Aluminum is 70% lighter per unit volume; 50% lighter for equivalent ampacity</td>
              </tr>
              <tr>
                <td><strong>Thermal Conductivity</strong></td>
                <td>$390\text{ W}/(\text{m}\cdot\text{K})$</td>
                <td>$205\text{ W}/(\text{m}\cdot\text{K})$</td>
                <td>Copper conducts heat away from terminations nearly twice as fast as aluminum</td>
              </tr>
              <tr>
                <td><strong>Tensile Strength</strong></td>
                <td>$200 - 400\text{ MPa}$</td>
                <td>$70 - 110\text{ MPa}$</td>
                <td>Copper withstands far higher mechanical pulling tension in long conduit pulls</td>
              </tr>
              <tr>
                <td><strong>Thermal Expansion ($\alpha$)</strong></td>
                <td>$16.5 \times 10^{-6}\ /\text{K}$</td>
                <td>$23.1 \times 10^{-6}\ /\text{K}$</td>
                <td>Aluminum expands 40% more under load cycles, requiring torque-limiting spring washers</td>
              </tr>
              <tr>
                <td><strong>Oxide Behavior</strong></td>
                <td>$\text{Cu}_2\text{O}$ is semi-conductive</td>
                <td>$\text{Al}_2\text{O}_3$ is an electrical insulator</td>
                <td>Aluminum requires anti-oxidant joint compound and wire brushing to prevent joint fires</td>
              </tr>
            </tbody>
          </table>

          <div class="formula-box">
            <h3>Life-Cycle Economics: The True Cost of Joule Heating Losses ($I^2R$)</h3>
            <p>Every meter of energized cable acts as a continuous low-temperature space heater. For a balanced three-phase circuit carrying continuous current $I$ through line conductors of resistance $R$, total power loss is:</p>
            <p>$$P_{loss} = 3 \times I^2 \times R \quad [\text{Watts}]$$</p>
            <p>Over an annual operating cycle of $H$ hours at commercial utility tariff $C_{kWh}$ ($/kWh):</p>
            <p>$$\text{Annual Cost } (\$) = \frac{P_{loss} \times H \times C_{kWh}}{1000}$$</p>
            <p><strong>The Economic Upsizing Opportunity:</strong> Sizing a cable strictly to thermal ampacity ratings saves initial capital expenditure on copper weight. However, stepping up one conductor cross-section (e.g. from $25\text{ mm}^2$ to $35\text{ mm}^2$, or #4 AWG to #2 AWG) slashes line resistance by roughly $30\%$. In continuous operating plants (hospitals, manufacturing, data centers), the energy savings over a 20-year building lifecycle frequently exceed the incremental cable material cost by a factor of 5 to 10!</p>
          </div>

          <div class="worked-example-card">
            <h3>Practical Worked Engineering Example: High-Efficiency Factory Feeder</h3>
            <p><strong>Design Scenario:</strong> Sizing a three-phase, 400V, 50 Hz copper feeder powering an industrial air compressor drawing a continuous running load of $I = 70\text{ A}$ at $0.85$ power factor. The one-way route length is $60\text{ meters}$. The cable is multicore copper with XLPE ($90^\circ\text{C}$) insulation installed on an open cable tray at $30^\circ\text{C}$ ambient. The plant operates 5,000 hours per year, and electricity costs $\$0.16/\text{kWh}$. Max allowable voltage drop is $3.5\%$.</p>

            <p><strong>Step 1: Preliminary Thermal Sizing</strong></p>
            <p>Referring to IEC 60364-5-52 Table B.52.4 (Method E, XLPE copper):</p>
            <ul>
              <li>$10\text{ mm}^2 \implies I_0 = 80\text{ A}$ (Marginal: $80 > 70\text{ A}$, but high heat losses)</li>
              <li>$16\text{ mm}^2 \implies I_0 = 110\text{ A}$ (Robust thermal headroom)</li>
            </ul>

            <p><strong>Step 2: Resistance &amp; Voltage Drop Comparison: $10\text{ mm}^2$ vs. $16\text{ mm}^2$</strong></p>
            <p>Operating temperature resistance $R$ for $60\text{ meters}$ at $90^\circ\text{C}$:</p>
            <ul>
              <li>For $10\text{ mm}^2$: $r_{90} \approx 2.33\ \Omega/\text{km} \implies R = 0.060\text{ km} \times 2.33 = 0.1398\ \Omega$
                $$\Delta V = \sqrt{3} \times 70\text{ A} \times 0.1398\ \Omega = 16.95\text{ V} \implies \Delta V\% = \frac{16.95}{400} \times 100 = 4.24\% \quad (\text{FAILS } > 3.5\%!)$$
              </li>
              <li>For $16\text{ mm}^2$: $r_{90} \approx 1.46\ \Omega/\text{km} \implies R = 0.060\text{ km} \times 1.46 = 0.0876\ \Omega$
                $$\Delta V = \sqrt{3} \times 70\text{ A} \times 0.0876\ \Omega = 10.62\text{ V} \implies \Delta V\% = \frac{10.62}{400} \times 100 = 2.66\% \quad (\text{PASSES } \le 3.5\%!)$$
              </li>
            </ul>

            <p><strong>Step 3: Calculating Annual Energy Loss Cost</strong></p>
            <p>For the compliant $16\text{ mm}^2$ copper cable:</p>
            <p>$$P_{loss} = 3 \times (70\text{ A})^2 \times 0.0876\ \Omega = 3 \times 4900 \times 0.0876 = 1287.7\text{ Watts} = 1.288\text{ kW}$$</p>
            <p>$$\text{Annual Energy Loss} = 1.288\text{ kW} \times 5000\text{ hrs} = 6440\text{ kWh/year}$$</p>
            <p>$$\text{Annual Cost} = 6440\text{ kWh} \times \$0.16/\text{kWh} = \$1{,}030.40/\text{year}$$</p>

            <p><strong>Step 4: The 25 mm² Economic Upsizing Analysis</strong></p>
            <p>If the engineer selects $25\text{ mm}^2$ copper ($r_{90} = 0.927\ \Omega/\text{km} \implies R = 0.0556\ \Omega$):</p>
            <p>$$P_{loss} = 3 \times 4900 \times 0.0556 = 817.3\text{ Watts} = 0.817\text{ kW}$$</p>
            <p>$$\text{Annual Cost} = 0.817\text{ kW} \times 5000 \times \$0.16 = \$653.60/\text{year}$$</p>
            <p>$$\text{Annual Savings} = \$1{,}030.40 - \$653.60 = \$376.80/\text{year}$$</p>
            <p>Over a 20-year service life, selecting $25\text{ mm}^2$ saves <strong>$\$7,536$ in wasted electricity</strong>, far exceeding the initial $\$300$ copper premium!</p>
          </div>

          <h2>Frequently Asked Questions (Copper Conductor Engineering)</h2>
          <div class="faq-item">
            <h3>What is the difference between solid, stranded, and flexible copper conductors?</h3>
            <p>Class 1 solid copper conductors consist of a single stiff wire used primarily in domestic conduit wiring up to 2.5 mm² (#10 AWG). Class 2 stranded conductors comprise multiple twisted wires (e.g. 7 or 19 strands) providing balance between flexibility and mechanical stiffness for commercial conduits. Class 5 and 6 flexible conductors utilize hundreds of fine copper strands (e.g. 0.2mm to 0.3mm wire) essential for equipment connections, elevator traveling cables, and robotic trailing leads subject to continuous bending fatigue.</p>
          </div>

          <div class="faq-item">
            <h3>What is skin effect in heavy copper cables?</h3>
            <p>At 50 Hz and 60 Hz AC power frequencies, alternating magnetic flux induces eddy currents inside the copper core, pushing current density toward the outer surface. The skin depth $\delta$ in copper is approximately $9.3\text{ mm}$ at 50 Hz. In conductors larger than $70\text{ mm}^2$ (2/0 AWG), AC resistance exceeds DC resistance by several percent. For massive busbars and utility cables larger than $300\text{ mm}^2$, segmental Milliken conductors are used to suppress skin effect.</p>
          </div>

          <div class="faq-item">
            <h3>Why must tinned copper be used in marine and sulfurous environments?</h3>
            <p>Bare copper reacts readily with sulfur, moisture, and chlorine to form non-conductive copper sulfides and green patina ($\text{CuCO}_3$). Applying a microscopic electro-plated coating of pure tin ($2\text{ to }5\ \mu\text{m}$) over individual copper strands creates a barrier against chemical corrosion, facilitates easy soldering, and prevents rubber insulation sulfur vulcanization.</p>
          </div>

          <div class="faq-item">
            <h3>How is adiabatic short-circuit withstand calculated for copper?</h3>
            <p>During a short circuit, energy dissipates adiabatically before heat can conduct into the insulation. The minimum required copper area $S$ is calculated from the IEC adiabatic equation: $S = \sqrt{I_{sc}^2 \cdot t} / k$. For copper with XLPE insulation ($90^\circ\text{C} \to 250^\circ\text{C}$ limit), the thermodynamic material constant $k = 143\text{ A}\cdot\text{s}^{1/2}/\text{mm}^2$. For copper with PVC ($70^\circ\text{C} \to 160^\circ\text{C}$ limit), $k = 115\text{ A}\cdot\text{s}^{1/2}/\text{mm}^2$.</p>
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
    // Metric Copper cable standard data (IEC 60228 Class 2 annealed copper)
    const copperMetricData = [
      { size: 1.5,  r20: 12.1,  c_pvc: 19.5, c_xlpe: 23 },
      { size: 2.5,  r20: 7.41,  c_pvc: 27.0, c_xlpe: 31 },
      { size: 4.0,  r20: 4.61,  c_pvc: 36.0, c_xlpe: 42 },
      { size: 6.0,  r20: 3.08,  c_pvc: 46.0, c_xlpe: 54 },
      { size: 10.0, r20: 1.83,  c_pvc: 63.0, c_xlpe: 75 },
      { size: 16.0, r20: 1.15,  c_pvc: 85.0, c_xlpe: 100 },
      { size: 25.0, r20: 0.727, c_pvc: 112,  c_xlpe: 127 },
      { size: 35.0, r20: 0.524, c_pvc: 138,  c_xlpe: 158 },
      { size: 50.0, r20: 0.387, c_pvc: 168,  c_xlpe: 192 },
      { size: 70.0, r20: 0.268, c_pvc: 213,  c_xlpe: 246 },
      { size: 95.0, r20: 0.193, c_pvc: 258,  c_xlpe: 298 },
      { size: 120,  r20: 0.153, c_pvc: 299,  c_xlpe: 346 },
      { size: 150,  r20: 0.124, c_pvc: 344,  c_xlpe: 399 },
      { size: 185,  r20: 0.0991, c_pvc: 392, c_xlpe: 456 },
      { size: 240,  r20: 0.0754, c_pvc: 461, c_xlpe: 538 },
      { size: 300,  r20: 0.0601, c_pvc: 530, c_xlpe: 621 }
    ];

    function calculateCopper() {
      const supply = document.getElementById("cuSystemSupply").value;
      const insulation = document.getElementById("cuInsulation").value;
      const current = parseFloat(document.getElementById("cuDesignCurrent").value) || 1;
      const ambTemp = parseFloat(document.getElementById("cuAmbientTemp").value) || 30;
      const lengthMeters = parseFloat(document.getElementById("cuRouteLength").value) || 1;
      const maxVdPct = parseFloat(document.getElementById("cuMaxVd").value) || 3.5;
      const costKwh = parseFloat(document.getElementById("electricityCostKwh").value) || 0.16;
      const hours = parseFloat(document.getElementById("annualHours").value) || 5000;

      let vNom = 400;
      let is3ph = true;
      if (supply === "230_1p") { vNom = 230; is3ph = false; }
      else if (supply === "120_1p") { vNom = 120; is3ph = false; }
      else if (supply === "480_3p") { vNom = 480; is3ph = true; }

      // Operating core temperature
      let opTemp = 90;
      if (insulation === "pvc70") opTemp = 70;
      else if (insulation === "pvc75") opTemp = 75;

      // Thermal derating Ca
      const ca = Math.sqrt(Math.max(0.1, (opTemp - ambTemp) / (opTemp - 30)));

      let selected = null;

      for (let i = 0; i < copperMetricData.length; i++) {
        const row = copperMetricData[i];
        const baseCap = (insulation === "xlpe") ? row.c_xlpe : row.c_pvc;
        const deratedCap = baseCap * ca;

        if (deratedCap < current) continue;

        // Temperature adjusted resistance
        const rT_per_km = row.r20 * (1 + 0.00393 * (opTemp - 20));
        const rT_circuit = (rT_per_km * (lengthMeters / 1000));

        let deltaV = 0;
        if (is3ph) {
          deltaV = Math.sqrt(3) * current * rT_circuit;
        } else {
          deltaV = 2 * current * rT_circuit;
        }

        const vdPct = (deltaV / vNom) * 100;

        if (vdPct <= maxVdPct) {
          // Power loss calculation
          let pLossWatts = 0;
          if (is3ph) {
            pLossWatts = 3 * current * current * rT_circuit;
          } else {
            pLossWatts = 2 * current * current * rT_circuit;
          }

          const annualCost = (pLossWatts * hours * costKwh) / 1000;
          const alArea = row.size * 1.64;

          selected = {
            size: row.size,
            rT: rT_circuit,
            deltaV: deltaV,
            vdPct: vdPct,
            pLossWatts: pLossWatts,
            annualCost: annualCost,
            alArea: alArea
          };
          break;
        }
      }

      if (selected) {
        document.getElementById("cuSizeOut").innerText = selected.size + " mm² Copper";
        document.getElementById("cuResistanceOut").innerText = selected.rT.toFixed(4) + " \u03A9";
        document.getElementById("cuVdOut").innerText = selected.deltaV.toFixed(2) + " V (" + selected.vdPct.toFixed(2) + "%)";
        document.getElementById("cuPowerLossOut").innerText = selected.pLossWatts.toFixed(1) + " W";
        document.getElementById("cuAnnualCostOut").innerText = "$" + selected.annualCost.toFixed(2) + " / yr";
        document.getElementById("cuAlEquivOut").innerText = selected.alArea.toFixed(1) + " mm² (Next: " + Math.ceil(selected.alArea) + " mm²)";
      } else {
        document.getElementById("cuSizeOut").innerText = "> 300 mm² (Parallel Conductors Needed)";
        document.getElementById("cuResistanceOut").innerText = "--";
        document.getElementById("cuVdOut").innerText = "Exceeds Drop Limit";
        document.getElementById("cuPowerLossOut").innerText = "--";
        document.getElementById("cuAnnualCostOut").innerText = "--";
        document.getElementById("cuAlEquivOut").innerText = "--";
      }
    }

    document.addEventListener("DOMContentLoaded", function() {
      calculateCopper();
    });
  </script>
</body>
</html>
"""

def main():
    root = r"C:\Users\Admin\.gemini\antigravity\scratch\calchub"
    
    p7 = os.path.join(root, "cable-sizing-calculator-nec.html")
    with open(p7, "w", encoding="utf-8") as f:
        f.write(TOOL_7_HTML.strip() + "\n")
    print("[PASS] cable-sizing-calculator-nec.html generated successfully!")

    p8 = os.path.join(root, "copper-cable-sizing-calculator.html")
    with open(p8, "w", encoding="utf-8") as f:
        f.write(TOOL_8_HTML.strip() + "\n")
    print("[PASS] copper-cable-sizing-calculator.html generated successfully!")

if __name__ == "__main__":
    main()
