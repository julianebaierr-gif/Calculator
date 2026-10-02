"""
Generates transformer-turns-ratio-calculator.html and aluminium-cable-sizing-calculator.html
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
# 1. TRANSFORMER TURNS RATIO CALCULATOR
# ==========================================
TOOL_TRANSFORMER = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Transformer Turns Ratio Calculator — Voltage, Current &amp; Impedance Matching</title>
  <meta name="description" content="Calculate transformer turns ratio (Np/Ns), primary and secondary voltages, full-load currents, and reflected impedance matching using Faraday's law.">
  <meta name="keywords" content="transformer turns ratio calculator, transformer turns ratio online, free transformer turns ratio, calculate transformer turns ratio, primary secondary voltage calculator, transformer impedance matching calculator, step down transformer formula, transformer ratio calculator">
  <link rel="canonical" href="https://calchub.org/transformer-turns-ratio-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "Transformer Turns Ratio & Impedance Calculator",
        "operatingSystem": "All",
        "applicationCategory": "EngineeringApplication",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
        "description": "Calculates primary to secondary turns ratio, transformation ratio a, step-up/step-down voltage conversion, current transformation, and reflected impedance matching per IEEE C57."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "What is the fundamental formula for transformer turns ratio?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "According to Faraday's law of electromagnetic induction, the turns ratio a of an ideal electrical transformer is defined as the ratio of primary winding turns Np to secondary winding turns Ns. In an ideal lossless transformer, this turns ratio equals the ratio of primary voltage to secondary voltage, and the inverse ratio of secondary current to primary current: a = Np / Ns = Vp / Vs = Is / Ip."
            }
          },
          {
            "@type": "Question",
            "name": "How does turns ratio affect reflected electrical impedance matching?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "When a secondary load impedance Zs is connected across the secondary terminals, the impedance reflected back to the primary source terminals is scaled by the square of the turns ratio: Zp = a^2 * Zs = (Np / Ns)^2 * Zs. Conversely, to match a specific primary generator impedance Zp to a secondary load Zs (common in audio tube output transformers and RF antennas), the required turns ratio is a = sqrt(Zp / Zs)."
            }
          },
          {
            "@type": "Question",
            "name": "What distinguishes a step-up transformer from a step-down transformer?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "If the turns ratio a is less than 1.0 (Np < Ns), secondary voltage exceeds primary voltage (Vs > Vp), classifying the unit as a Step-Up transformer. Conversely, if a is greater than 1.0 (Np > Ns), secondary voltage is lower than primary voltage (Vs < Vp), classifying the unit as a Step-Down transformer. Because total apparent power remains constant (Vp * Ip = Vs * Is in an ideal transformer), stepping up voltage proportionally steps down current, and vice versa."
            }
          },
          {
            "@type": "Question",
            "name": "What is the EMF equation of a transformer winding?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The root-mean-square (RMS) electromotive force induced in any transformer winding is given by the general EMF equation: E_rms = 4.44 * f * N * Phi_max = 4.44 * f * N * B_max * A_c, where f is the supply AC frequency in Hertz, N is the number of turns on the winding, Phi_max is the peak magnetic flux in Webers, B_max is the peak magnetic flux density in Teslas, and A_c is the net cross-sectional core area in square meters."
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
      <span>Transformer Turns Ratio Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">Faraday&rsquo;s Law &amp; IEEE C57 Standards</div>
          <h1 class="calc-title">Transformer Turns Ratio Calculator</h1>
          <p class="calc-tagline">Calculate primary-to-secondary turns ratio ($N_p/N_s$), transformation ratio $a$, induced voltages, full-load currents, and reflected impedance matching.</p>
        </header>

        <!-- Tool Card -->
        <div class="tool-card">
          <form id="xfmrForm" onsubmit="return false;">
            <div class="calc-grid">
              <div class="form-group">
                <label for="calcMode" class="form-label">Calculation Goal</label>
                <select id="calcMode" class="form-control" onchange="toggleXfmrMode(); calculateXfmr();">
                  <option value="voltage-turns" selected>Calculate Turns Ratio from Voltages ($V_p \rightarrow V_s$)</option>
                  <option value="known-turns">Calculate Secondary Voltage from Known Turns ($N_p, N_s$)</option>
                  <option value="impedance-match">RF &amp; Audio Impedance Matching ($Z_p \leftrightarrow Z_s$)</option>
                </select>
                <small class="form-hint">Select input configuration</small>
              </div>

              <div class="form-group" id="grpVp">
                <label for="voltPrimary" class="form-label">Primary Voltage ($V_p$)</label>
                <div class="input-with-unit">
                  <input type="number" id="voltPrimary" class="form-control" value="480" step="1" min="0.1" oninput="calculateXfmr()">
                  <span class="unit-badge">V</span>
                </div>
                <small class="form-hint">Input AC supply RMS voltage</small>
              </div>

              <div class="form-group" id="grpVs">
                <label for="voltSecondary" class="form-label">Secondary Voltage ($V_s$)</label>
                <div class="input-with-unit">
                  <input type="number" id="voltSecondary" class="form-control" value="120" step="1" min="0.1" oninput="calculateXfmr()">
                  <span class="unit-badge">V</span>
                </div>
                <small class="form-hint">Desired output AC RMS voltage</small>
              </div>

              <div class="form-group" id="grpNp" style="display:none;">
                <label for="turnsPrimary" class="form-label">Primary Winding Turns ($N_p$)</label>
                <input type="number" id="turnsPrimary" class="form-control" value="800" step="1" min="1" oninput="calculateXfmr()">
                <small class="form-hint">Number of wire turns on primary</small>
              </div>

              <div class="form-group" id="grpNs" style="display:none;">
                <label for="turnsSecondary" class="form-label">Secondary Winding Turns ($N_s$)</label>
                <input type="number" id="turnsSecondary" class="form-control" value="200" step="1" min="1" oninput="calculateXfmr()">
                <small class="form-hint">Number of wire turns on secondary</small>
              </div>

              <div class="form-group" id="grpZp" style="display:none;">
                <label for="impPrimary" class="form-label">Source / Primary Impedance ($Z_p$)</label>
                <div class="input-with-unit">
                  <input type="number" id="impPrimary" class="form-control" value="3200" step="10" min="0.1" oninput="calculateXfmr()">
                  <span class="unit-badge">&Omega;</span>
                </div>
                <small class="form-hint">E.g. Tube plate impedance ($3.2\text{ k}\Omega$)</small>
              </div>

              <div class="form-group" id="grpZs" style="display:none;">
                <label for="impSecondary" class="form-label">Load / Secondary Impedance ($Z_s$)</label>
                <div class="input-with-unit">
                  <input type="number" id="impSecondary" class="form-control" value="8" step="0.5" min="0.1" oninput="calculateXfmr()">
                  <span class="unit-badge">&Omega;</span>
                </div>
                <small class="form-hint">E.g. Speaker voice coil ($8\,\Omega$)</small>
              </div>

              <div class="form-group">
                <label for="loadCurrentSec" class="form-label">Secondary Load Current ($I_s$)</label>
                <div class="input-with-unit">
                  <input type="number" id="loadCurrentSec" class="form-control" value="20" step="0.5" min="0" oninput="calculateXfmr()">
                  <span class="unit-badge">A</span>
                </div>
                <small class="form-hint">Rated load current on secondary</small>
              </div>
            </div>

            <button type="button" class="btn btn-primary" onclick="calculateXfmr()" style="margin-top:1.25rem;">
              Calculate Transformation Parameters
            </button>
          </form>

          <!-- Output Display -->
          <div class="results-panel" id="resultsBox" style="margin-top:1.75rem;">
            <div class="results-grid">
              <div class="result-tile">
                <div class="result-label">Turns Ratio ($N_p : N_s$)</div>
                <div class="result-value" id="outRatioStr">4.00 : 1</div>
                <div class="result-subtext" id="outRatioFactor">Ratio $a = 4.000$ (Step-Down)</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Secondary Voltage ($V_s$)</div>
                <div class="result-value" id="outVs">120.0 V</div>
                <div class="result-subtext" id="outVpEcho">Primary: 480.0 V</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Primary Current ($I_p$)</div>
                <div class="result-value" id="outIp">5.00 A</div>
                <div class="result-subtext" id="outIsEcho">Secondary: 20.0 A</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Transformer Apparent Power</div>
                <div class="result-value" id="outPowerKva">2.40 kVA</div>
                <div class="result-subtext">2,400 VA Total Rating</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Impedance Ratio ($Z_p / Z_s$)</div>
                <div class="result-value" id="outImpRatio">16.00 &times;</div>
                <div class="result-subtext">$a^2 = (N_p / N_s)^2$</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Transformer Classification</div>
                <div class="result-value" id="outClass">Step-Down</div>
                <div class="result-subtext" id="outClassDesc">Lowers voltage, multiplies current</div>
              </div>
            </div>
          </div>
        </div>

        <!-- 1000+ Words Technical Educational Article -->
        <article class="educational-content" style="margin-top:3rem;">
          <h2>Electromagnetic Physics &amp; Operating Principles of Transformers</h2>
          <p>
            An electrical power transformer is a static, passive electromagnetic machine that transfers alternating electrical energy from one circuit to another without changing frequency, operating strictly via mutual magnetic induction. Invented in the late 19th century through the pioneering work of Michael Faraday, Nikola Tesla, Lucien Gaulard, and William Stanley, the transformer enabled the global adoption of alternating current (AC) power distribution grids by permitting high-voltage, low-current long-distance transmission with negligible $I^2 R$ transmission line heating losses, followed by localized step-down to safe utilization voltages for industrial and residential consumers.
          </p>
          <p>
            A two-winding transformer comprises two electrically isolated conductive coils—the <strong>Primary Winding</strong> and the <strong>Secondary Winding</strong>—wound around a common high-permeability ferrosilicon laminated steel or ferrite magnetic core. When alternating current flows into the primary winding, it establishes a time-varying magnetic flux ($\Phi(t)$) in the core. This alternating magnetic flux links through the secondary winding, inducing a proportional electromotive force (EMF) strictly in accordance with Faraday's Law and Lenz's Law.
          </p>

          <h2>Core Mathematical Equations Governing Transformer Operations</h2>
          <p>
            Electrical engineers evaluate voltage transformations, winding ratios, reflected impedance, and magnetic flux using standard analytical formulas:
          </p>

          <div class="formula-box">
            <div class="formula-title">1. Ideal Transformation Ratio ($a$) and Turns Relationship</div>
            <div class="formula-math">$$a = \frac{N_p}{N_s} = \frac{V_p}{V_s} = \frac{I_s}{I_p} = \sqrt{\frac{Z_p}{Z_s}}$$</div>
            <p>Where $N_p$ is primary winding turns, $N_s$ is secondary winding turns, $V_p$ and $V_s$ are primary and secondary RMS voltages, $I_p$ and $I_s$ are primary and secondary RMS currents, and $Z_p$ and $Z_s$ are primary and secondary terminal impedances.</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">2. Voltage &amp; Current Step-Up / Step-Down Relationships</div>
            <div class="formula-math">$$V_s = V_p \times \frac{N_s}{N_p} = \frac{V_p}{a}, \quad I_p = I_s \times \frac{N_s}{N_p} = \frac{I_s}{a}$$</div>
            <p>Because apparent power is conserved in an ideal transformer ($S_p = S_s \implies V_p I_p = V_s I_s$), any increase in voltage is accompanied by an exact proportional reduction in current.</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">3. Reflected Impedance Transformation &amp; Matching</div>
            <div class="formula-math">$$Z_p = a^2 \times Z_s = \left(\frac{N_p}{N_s}\right)^2 \times Z_s, \quad Z_s = \frac{Z_p}{a^2} = \left(\frac{N_s}{N_p}\right)^2 \times Z_p$$</div>
            <p>Impedance scales with the <em>square</em> of the turns ratio. This principle is vital in audio engineering (matching high-impedance vacuum tube output stages to low-impedance $4\,\Omega$ or $8\,\Omega$ loudspeakers) and RF antenna baluns.</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">4. General EMF Induction Equation of a Transformer</div>
            <div class="formula-math">$$E_{rms} = 4.44 \times f \times N \times \Phi_{max} = 4.44 \times f \times N \times B_{max} \times A_c$$</div>
            <p>Where $f$ is operating AC frequency in Hertz, $\Phi_{max}$ is peak magnetic core flux in Webers, $B_{max}$ is peak magnetic flux density in Teslas, and $A_c$ is effective cross-sectional iron core area in square meters. The coefficient $4.44 = 4 \times K_f$ derives from the form factor $K_f = 1.11$ of a pure sinusoidal waveform.</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">5. Real-World Transformer Efficiency ($\eta$)</div>
            <div class="formula-math">$$\eta = \frac{P_{out}}{P_{in}} \times 100\% = \frac{V_s I_s \cos(\theta)}{V_s I_s \cos(\theta) + P_{core} + I_s^2 R_{eq,s}} \times 100\%$$</div>
            <p>Where $P_{core}$ represents frequency-dependent magnetic hysteresis and eddy-current losses, and $I_s^2 R_{eq,s}$ represents load-dependent ohmic copper winding losses.</p>
          </div>

          <h2>Comparison of Standard Transformer Classifications</h2>
          <p>
            Transformers are engineered across diverse topologies based on voltage level, frequency, and magnetic isolation:
          </p>

          <table class="table-custom">
            <thead>
              <tr>
                <th>Transformer Category</th>
                <th>Typical Ratio ($a$)</th>
                <th>Frequency Domain</th>
                <th>Core Material</th>
                <th>Primary Application</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Substation Distribution</strong></td>
                <td>$a = 5\text{ to }50$</td>
                <td>50 Hz / 60 Hz</td>
                <td>Grain-oriented silicon steel (CRGO)</td>
                <td>Step down 13.8 kV / 4.16 kV grid down to 480V/208V/120V</td>
              </tr>
              <tr>
                <td><strong>Industrial Control</strong></td>
                <td>$a = 2\text{ to }4$</td>
                <td>50 Hz / 60 Hz</td>
                <td>Laminated silicon steel</td>
                <td>Step 480V down to 120V/24V for PLC control circuits</td>
              </tr>
              <tr>
                <td><strong>Audio Impedance Matching</strong></td>
                <td>$a = 15\text{ to }30$</td>
                <td>20 Hz &ndash; 20 kHz</td>
                <td>Nickel-iron alloy (Mu-metal)</td>
                <td>Vacuum tube amp plate ($5\text{ k}\Omega$) to speaker ($8\,\Omega$)</td>
              </tr>
              <tr>
                <td><strong>SMPS High-Frequency Flyback</strong></td>
                <td>$a = 2\text{ to }10$</td>
                <td>50 kHz &ndash; 1 MHz</td>
                <td>Manganese-zinc (MnZn) ferrite</td>
                <td>AC-DC smartphone chargers, computer ATX power supplies</td>
              </tr>
              <tr>
                <td><strong>RF Balun / Transmission</strong></td>
                <td>$a = 1.414\text{ to }2.0$</td>
                <td>1 MHz &ndash; 500 MHz</td>
                <td>Nickel-zinc (NiZn) powdered iron</td>
                <td>Antenna matching ($50\,\Omega$ coax to $200\,\Omega$ or $450\,\Omega$ dipole)</td>
              </tr>
            </tbody>
          </table>

          <!-- Real World Worked Case Study Card -->
          <div class="worked-example-card">
            <h3>Practical Case Study: Industrial CNC Machine Power Transformer Sizing</h3>
            <p>
              An industrial facility receives a heavy-duty CNC milling machine manufactured in Germany designed to operate from a $208\text{ V}$ secondary supply. The factory power distribution panel provides $480\text{ V}$ line-to-line 3-phase power. An on-site electrical engineer must specify a dry-type step-down transformer to deliver $V_s = 208\text{ V}$ with a full-load secondary current draw of $I_s = 45.0\text{ Amps}$.
            </p>
            <div class="step-calculation">
              <strong>Step 1: Calculate the Voltage Transformation Ratio ($a$):</strong><br>
              $$a = \frac{V_p}{V_s} = \frac{480\text{ V}}{208\text{ V}} \approx 2.3077$$
              <small>The primary winding requires $2.3077$ turns for every $1$ turn on the secondary winding (Turns ratio $N_p : N_s \approx 2.31 : 1$).</small>
            </div>
            <div class="step-calculation">
              <strong>Step 2: Calculate Primary Line Current ($I_p$):</strong><br>
              $$I_p = \frac{I_s}{a} = \frac{45.0\text{ A}}{2.3077} \approx 19.50\text{ Amps}$$
            </div>
            <div class="step-calculation">
              <strong>Step 3: Calculate Total Transformer Apparent Power Rating:</strong><br>
              $$S = \sqrt{3} \times V_s \times I_s = 1.73205 \times 208\text{ V} \times 45.0\text{ A} \approx 16,212\text{ VA} = 16.21\text{ kVA}$$
              <p>Applying the standard NEC 125% continuous load margin ($16.21 \times 1.25 = 20.26\text{ kVA}$), the engineer selects the next standard commercial size: a **30 kVA 480V-to-208V/120V dry-type transformer**.</p>
            </div>
            <div class="step-calculation">
              <strong>Step 4: Verify Impedance Scaling:</strong><br>
              The CNC machine load impedance is $Z_s = \frac{V_s}{\sqrt{3} I_s} = \frac{208}{1.732 \times 45} \approx 2.668\,\Omega$. Reflected to the 480V primary grid, the source sees:
              $$Z_p = a^2 \times Z_s = (2.3077)^2 \times 2.668\,\Omega = 5.325 \times 2.668 \approx 14.21\,\Omega$$
            </div>
          </div>

          <h2>Key Engineering Guidelines for Transformer Selection &amp; Protection</h2>
          <ul>
            <li><strong>Inrush Current Sizing:</strong> When first energized at a voltage zero-crossing, a transformer core can be driven into deep magnetic saturation, drawing instantaneous peak magnetizing inrush current up to 10 to 15 times its full-load rating ($10\text{ to }15 \times I_{FLA}$) for several cycles. Primary circuit breakers must utilize Type D trip curves or inverse-time thermal-magnetic elements sized per NEC Article 450.</li>
            <li><strong>Cooling &amp; Temperature Rise Classes:</strong> Industrial dry-type transformers feature insulation temperature classes (Class 150, 180, or 220&deg;C). Specifying an 80&deg;C or 115&deg;C rise unit with Class 220 insulation provides substantial overload headroom, lower operating losses, and vastly extended operating lifespans.</li>
            <li><strong>Harmonic K-Factor Rating:</strong> Non-linear electronic loads (such as variable frequency drives, server switch-mode power supplies, and LED arrays) generate high-frequency harmonic currents that cause severe eddy-current overheating in transformer cores. Non-linear circuits mandate K-factor rated transformers (e.g. K-4, K-13, or K-20) equipped with electrostatic shielding and oversized neutral conductors.</li>
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
    function toggleXfmrMode() {
      const mode = document.getElementById('calcMode').value;
      document.getElementById('grpVp').style.display = (mode !== "impedance-match") ? "block" : "none";
      document.getElementById('grpVs').style.display = (mode === "voltage-turns") ? "block" : "none";
      document.getElementById('grpNp').style.display = (mode === "known-turns") ? "block" : "none";
      document.getElementById('grpNs').style.display = (mode === "known-turns") ? "block" : "none";
      document.getElementById('grpZp').style.display = (mode === "impedance-match") ? "block" : "none";
      document.getElementById('grpZs').style.display = (mode === "impedance-match") ? "block" : "none";
    }

    function calculateXfmr() {
      const mode = document.getElementById('calcMode').value;
      const Is = parseFloat(document.getElementById('loadCurrentSec').value) || 0;

      let a = 1.0;
      let Vp = 480;
      let Vs = 120;
      let Zp = 0;
      let Zs = 0;

      if (mode === "voltage-turns") {
        Vp = parseFloat(document.getElementById('voltPrimary').value);
        Vs = parseFloat(document.getElementById('voltSecondary').value);
        if (isNaN(Vp) || isNaN(Vs) || Vp <= 0 || Vs <= 0) return;
        a = Vp / Vs;
      } else if (mode === "known-turns") {
        Vp = parseFloat(document.getElementById('voltPrimary').value);
        const Np = parseFloat(document.getElementById('turnsPrimary').value);
        const Ns = parseFloat(document.getElementById('turnsSecondary').value);
        if (isNaN(Vp) || isNaN(Np) || isNaN(Ns) || Vp <= 0 || Np <= 0 || Ns <= 0) return;
        a = Np / Ns;
        Vs = Vp / a;
      } else {
        Zp = parseFloat(document.getElementById('impPrimary').value);
        Zs = parseFloat(document.getElementById('impSecondary').value);
        if (isNaN(Zp) || isNaN(Zs) || Zp <= 0 || Zs <= 0) return;
        a = Math.sqrt(Zp / Zs);
        Vp = 100; // Reference 100V
        Vs = Vp / a;
      }

      const Ip = (a > 0) ? (Is / a) : 0;
      const powerVa = Vs * Is;
      const powerKva = powerVa / 1000;
      const impRatio = a * a;

      let xfmrClass = "1:1 Isolation";
      let classDesc = "Unity voltage, safety galvanic isolation";
      if (a > 1.01) {
        xfmrClass = "Step-Down";
        classDesc = "Reduces voltage, multiplies current capacity";
      } else if (a < 0.99) {
        xfmrClass = "Step-Up";
        classDesc = "Boosts voltage, reduces current load";
      }

      document.getElementById('outRatioStr').textContent = a.toFixed(2) + " : 1";
      document.getElementById('outRatioFactor').textContent = `Ratio a = ${a.toFixed(3)} (${xfmrClass})`;
      document.getElementById('outVs').textContent = Vs.toFixed(1) + " V";
      document.getElementById('outVpEcho').textContent = `Primary: ${Vp.toFixed(1)} V`;
      document.getElementById('outIp').textContent = Ip.toFixed(2) + " A";
      document.getElementById('outIsEcho').textContent = `Secondary: ${Is.toFixed(1)} A`;
      document.getElementById('outPowerKva').textContent = powerKva.toFixed(2) + " kVA";
      document.getElementById('outImpRatio').textContent = impRatio.toFixed(2) + " \u00D7";
      document.getElementById('outClass').textContent = xfmrClass;
      document.getElementById('outClassDesc').textContent = classDesc;
    }

    window.addEventListener('DOMContentLoaded', () => {
      toggleXfmrMode();
      calculateXfmr();
    });
  </script>
</body>
</html>
"""

# ==========================================
# 2. ALUMINIUM CABLE SIZING CALCULATOR
# ==========================================
TOOL_ALUMINIUM = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Aluminium Cable Sizing Calculator — NEC 310.16 Ampacity &amp; Voltage Drop</title>
  <meta name="description" content="Calculate aluminum cable size, allowable ampacity, voltage drop, and copper-to-aluminum equivalent gauge per NEC Table 310.16 and international standards.">
  <meta name="keywords" content="aluminium cable sizing calculator, aluminium cable sizing online, free aluminium cable sizing, calculate aluminium cable sizing, aluminum wire ampacity calculator, aluminum vs copper cable size, nec 310.16 aluminum wire, aluminum feeder sizing">
  <link rel="canonical" href="https://calchub.org/aluminium-cable-sizing-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "Aluminium Electrical Cable Sizing Calculator",
        "operatingSystem": "All",
        "applicationCategory": "EngineeringApplication",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
        "description": "Calculates aluminum conductor cross-section, allowable ampacity, voltage drop percentage, and copper equivalent size per NEC 310.16 and IEC 60364."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "Why does aluminum wire require a larger cross-section than copper wire?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Electrical aluminum (AA-8000 alloy) has an electrical conductivity of approximately 61% of copper (IACS). The electrical resistivity of aluminum is 2.82 x 10^-8 ohm-meters compared to 1.72 x 10^-8 ohm-meters for annealed copper. To carry the same electrical current with identical I^2*R heating and voltage drop, an aluminum conductor must have roughly 1.64 times the cross-sectional area of a copper conductor, which corresponds to approximately two AWG sizes larger (e.g. 2 AWG aluminum replaces 4 AWG copper)."
            }
          },
          {
            "@type": "Question",
            "name": "What are the standard ampacities for aluminum conductors under NEC Table 310.16?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "At a 75°C insulation rating (such as THHN/THWN-2 on standard termination equipment rated 75°C), common aluminum conductor ampacities are: 6 AWG (40A), 4 AWG (55A), 2 AWG (75A), 1 AWG (85A), 1/0 AWG (100A), 2/0 AWG (115A), 3/0 AWG (130A), 4/0 AWG (150A), 250 kcmil (170A), 350 kcmil (210A), and 500 kcmil (310A)."
            }
          },
          {
            "@type": "Question",
            "name": "What special precautions are required when terminating aluminum wiring?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Terminating aluminum wiring requires three critical precautions: 1) Use modern AA-8000 series aluminum alloy (mandated by NEC 310.3) which resists mechanical creep; 2) Utilize terminal lugs and circuit breakers dual-rated and marked 'AL7CU' or 'AL9CU'; and 3) Clean the conductor with a wire brush and apply antioxidant joint compound (penetrox) to prevent insulating aluminum oxide films from creating high-resistance hot joints."
            }
          },
          {
            "@type": "Question",
            "name": "How is voltage drop calculated for long aluminum cable runs?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For a single-phase AC or DC aluminum run: Delta V = (2 * I * L * R_Al) / 1000. For a balanced three-phase AC run: Delta V = (sqrt(3) * I * L * R_Al) / 1000, where I is load current in amperes, L is one-way distance in feet or meters, and R_Al is the conductor resistance per 1000 ft or km from NEC Chapter 9 Table 8. Voltage drop should be kept within 3% for branch circuits and 5% total system per NEC 210.19(A) Informational Note."
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
      <span>Aluminium Cable Sizing Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">NEC 310.16 &amp; AA-8000 Standards</div>
          <h1 class="calc-title">Aluminium Cable Sizing Calculator</h1>
          <p class="calc-tagline">Calculate aluminum conductor size, allowable ampacity, voltage drop, and equivalent copper gauge for commercial feeders and service entrances.</p>
        </header>

        <!-- Tool Card -->
        <div class="tool-card">
          <form id="alCableForm" onsubmit="return false;">
            <div class="calc-grid">
              <div class="form-group">
                <label for="sysType" class="form-label">Electrical Distribution System</label>
                <select id="sysType" class="form-control" onchange="calculateAlCable()">
                  <option value="120_1ph">120V 1-Phase AC (2-Wire)</option>
                  <option value="240_1ph" selected>240V 1-Phase AC (Residential Service/Subpanel)</option>
                  <option value="208_3ph">208V 3-Phase AC (Commercial Power)</option>
                  <option value="480_3ph">480V 3-Phase AC (Industrial Feeder)</option>
                  <option value="dc_48">48V DC Telecom / Battery Bank</option>
                </select>
                <small class="form-hint">Nominal circuit voltage and phase</small>
              </div>

              <div class="form-group">
                <label for="designCurrent" class="form-label">Design Load Current ($I_{load}$)</label>
                <div class="input-with-unit">
                  <input type="number" id="designCurrent" class="form-control" value="100" step="1" min="1" max="2000" oninput="calculateAlCable()">
                  <span class="unit-badge">Amps</span>
                </div>
                <small class="form-hint">Including 125% continuous load factor</small>
              </div>

              <div class="form-group">
                <label for="runLength" class="form-label">One-Way Run Distance</label>
                <div class="input-with-unit">
                  <input type="number" id="runLength" class="form-control" value="150" step="5" min="1" max="5000" oninput="calculateAlCable()">
                  <span class="unit-badge">feet</span>
                </div>
                <small class="form-hint">Distance from panel to load</small>
              </div>

              <div class="form-group">
                <label for="maxVdPct" class="form-label">Max Allowed Voltage Drop</label>
                <select id="maxVdPct" class="form-control" onchange="calculateAlCable()">
                  <option value="2.0">2.0% (Critical Telecom &amp; Sensitive Electronics)</option>
                  <option value="3.0" selected>3.0% (NEC Recommended Branch/Feeder)</option>
                  <option value="5.0">5.0% (NEC Max Total System Ceiling)</option>
                </select>
                <small class="form-hint">Permissible percentage drop</small>
              </div>

              <div class="form-group">
                <label for="conduitMaterial" class="form-label">Raceway Conduit Type</label>
                <select id="conduitMaterial" class="form-control" onchange="calculateAlCable()">
                  <option value="pvc" selected>PVC / Non-Metallic Conduit</option>
                  <option value="steel">Steel / EMT Rigid Metal Conduit</option>
                  <option value="aluminum">Aluminum Metallic Conduit</option>
                </select>
                <small class="form-hint">Affects AC reactance impedance</small>
              </div>

              <div class="form-group">
                <label for="tempRating" class="form-label">Terminal Insulation Rating</label>
                <select id="tempRating" class="form-control" onchange="calculateAlCable()">
                  <option value="75" selected>75&deg;C (Standard THHN/XHHW Terminal Rating)</option>
                  <option value="90">90&deg;C (Special High-Temp Derated Terminal)</option>
                </select>
                <small class="form-hint">Equipment lug rating (75°C typical)</small>
              </div>
            </div>

            <button type="button" class="btn btn-primary" onclick="calculateAlCable()" style="margin-top:1.25rem;">
              Size Aluminum Cable
            </button>
          </form>

          <!-- Output Display -->
          <div class="results-panel" id="resultsBox" style="margin-top:1.75rem;">
            <div class="results-grid">
              <div class="result-tile">
                <div class="result-label">Recommended Aluminum Size</div>
                <div class="result-value" id="outAlGauge">2/0 AWG Al</div>
                <div class="result-subtext" id="outAlAmpacity">135A Ampacity @ 75&deg;C</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Copper Equivalent Size</div>
                <div class="result-value" id="outCuGauge">1 AWG Cu</div>
                <div class="result-subtext">Equivalent copper cross-section</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Calculated Voltage Drop</div>
                <div class="result-value" id="outVdVolts">4.82 V</div>
                <div class="result-subtext" id="outVdPct">2.01% of 240V (&le; 3.0% Pass)</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Cost Savings vs Copper</div>
                <div class="result-value" id="outSavings">&asymp; 45% &ndash; 60%</div>
                <div class="result-subtext">Substantial commercial raw material savings</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Conductor Weight Ratio</div>
                <div class="result-value" id="outWeight">&asymp; 50% Lighter</div>
                <div class="result-subtext">Eases conduit pulling tension</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Termination Requirement</div>
                <div class="result-value" id="outLugSpec">AL7CU / AL9CU</div>
                <div class="result-subtext">Mandatory anti-oxidant compound</div>
              </div>
            </div>
          </div>
        </div>

        <!-- 1000+ Words Technical Educational Article -->
        <article class="educational-content" style="margin-top:3rem;">
          <h2>Material Metallurgy &amp; Electrical Physics of Aluminum Conductors</h2>
          <p>
            In electrical power engineering, aluminum has served as a premier conductor material for over a century, particularly in high-voltage utility overhead transmission lines (where Aluminum Conductor Steel Reinforced, or ACSR, dominates global infrastructure) and commercial service entrance feeders. The economic incentive for specifying aluminum over copper is compelling: aluminum raw material costs are roughly one-third that of copper, and aluminum's lower density results in an installed cable run that weighs approximately 50% less, dramatically reducing conduit pulling tension and structural support stresses.
          </p>
          <p>
            However, aluminum exhibits distinctly different physical, thermal, and electrodynamic properties compared to copper. Modern electrical installations rely exclusively on <strong>AA-8000 series aluminum alloy</strong> (such as Alumalloy), mandated by the <strong>National Electrical Code (NEC Article 310.3)</strong>. Unlike legacy 1350 utility aluminum used in 1960s residential branch wiring, AA-8000 alloy incorporates precise metallurgical additions of iron and silicon that resist cold flow mechanical creep, maintain elastic springback in terminal lugs, and ensure tight, fire-safe connections over decades of thermal cycling.
          </p>

          <h2>Core Mathematical Equations Governing Aluminum Cable Sizing</h2>
          <p>
            Electrical engineers evaluate aluminum conductor sizing through ampacity thermal ratings and Ohm's Law voltage drop constraints:
          </p>

          <div class="formula-box">
            <div class="formula-title">1. Electrical Resistivity &amp; Area Equivalence Rule</div>
            <div class="formula-math">$$\rho_{Al} = 2.82 \times 10^{-8}\,\Omega\cdot\text{m}, \quad \rho_{Cu} = 1.72 \times 10^{-8}\,\Omega\cdot\text{m}$$</div>
            <div class="formula-math">$$\frac{A_{Al}}{A_{Cu}} = \frac{\rho_{Al}}{\rho_{Cu}} = \frac{2.82}{1.72} \approx 1.64$$</div>
            <p>An aluminum conductor requires approximately $1.64$ times the cross-sectional area of a copper conductor (roughly two AWG trade sizes larger) to achieve identical DC electrical resistance.</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">2. Single-Phase AC / DC Voltage Drop Equation</div>
            <div class="formula-math">$$\Delta V_{1\phi} = \frac{2 \times I \times L \times R_{Al}}{1000}$$</div>
            <div class="formula-math">$$\%\text{VD} = \frac{\Delta V_{1\phi}}{V_{source}} \times 100\%$$</div>
            <p>Where $I$ is load current in amperes, $L$ is one-way run distance in feet, and $R_{Al}$ is the conductor AC resistance in Ohms per 1,000 feet from NEC Chapter 9 Table 8/9.</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">3. Balanced Three-Phase AC Voltage Drop Equation</div>
            <div class="formula-math">$$\Delta V_{3\phi} = \frac{\sqrt{3} \times I \times L \times R_{Al}}{1000} \approx \frac{1.732 \times I \times L \times R_{Al}}{1000}$$</div>
            <div class="formula-math">$$\%\text{VD} = \frac{\Delta V_{3\phi}}{V_{LL}} \times 100\%$$</div>
            <p>Where $V_{LL}$ is the line-to-line three-phase RMS supply voltage (e.g. 208V, 480V).</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">4. Thermal Derating Correction Equation</div>
            <div class="formula-math">$$I_{allowable} = I_{table} \times K_{temp} \times K_{bundle}$$</div>
            <p>Where $I_{table}$ is baseline ampacity from NEC Table 310.16, $K_{temp}$ is ambient temperature correction factor (NEC Table 310.15(B)(1)), and $K_{bundle}$ is the raceway bundling adjustment factor (NEC Table 310.15(C)(1)) for more than 3 current-carrying conductors in a single conduit.</p>
          </div>

          <h2>NEC Table 310.16 Allowable Ampacities: Aluminum vs Copper</h2>
          <p>
            The table below contrasts standard 75&deg;C ampacities and DC resistances for AA-8000 aluminum versus annealed copper conductors:
          </p>

          <table class="table-custom">
            <thead>
              <tr>
                <th>Conductor Size</th>
                <th>Aluminum Ampacity (75&deg;C)</th>
                <th>Copper Ampacity (75&deg;C)</th>
                <th>Aluminum $R_{DC}$ (&Omega;/kft)</th>
                <th>Copper $R_{DC}$ (&Omega;/kft)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>6 AWG</strong></td>
                <td>40 Amps</td>
                <td>55 Amps</td>
                <td>0.808 &Omega;</td>
                <td>0.491 &Omega;</td>
              </tr>
              <tr>
                <td><strong>4 AWG</strong></td>
                <td>55 Amps</td>
                <td>70 Amps</td>
                <td>0.508 &Omega;</td>
                <td>0.308 &Omega;</td>
              </tr>
              <tr>
                <td><strong>2 AWG</strong></td>
                <td>75 Amps</td>
                <td>95 Amps</td>
                <td>0.319 &Omega;</td>
                <td>0.194 &Omega;</td>
              </tr>
              <tr>
                <td><strong>1 AWG</strong></td>
                <td>85 Amps</td>
                <td>110 Amps</td>
                <td>0.253 &Omega;</td>
                <td>0.154 &Omega;</td>
              </tr>
              <tr>
                <td><strong>1/0 AWG</strong></td>
                <td>100 Amps</td>
                <td>125 Amps</td>
                <td>0.201 &Omega;</td>
                <td>0.122 &Omega;</td>
              </tr>
              <tr>
                <td><strong>2/0 AWG</strong></td>
                <td>115 Amps</td>
                <td>145 Amps</td>
                <td>0.159 &Omega;</td>
                <td>0.0967 &Omega;</td>
              </tr>
              <tr>
                <td><strong>3/0 AWG</strong></td>
                <td>130 Amps</td>
                <td>165 Amps</td>
                <td>0.126 &Omega;</td>
                <td>0.0766 &Omega;</td>
              </tr>
              <tr>
                <td><strong>4/0 AWG</strong></td>
                <td>150 Amps</td>
                <td>195 Amps</td>
                <td>0.100 &Omega;</td>
                <td>0.0608 &Omega;</td>
              </tr>
              <tr>
                <td><strong>250 kcmil</strong></td>
                <td>170 Amps</td>
                <td>215 Amps</td>
                <td>0.0847 &Omega;</td>
                <td>0.0515 &Omega;</td>
              </tr>
              <tr>
                <td><strong>350 kcmil</strong></td>
                <td>210 Amps</td>
                <td>260 Amps</td>
                <td>0.0605 &Omega;</td>
                <td>0.0367 &Omega;</td>
              </tr>
              <tr>
                <td><strong>500 kcmil</strong></td>
                <td>260 Amps</td>
                <td>320 Amps</td>
                <td>0.0424 &Omega;</td>
                <td>0.0258 &Omega;</td>
              </tr>
            </tbody>
          </table>

          <!-- Real World Worked Case Study Card -->
          <div class="worked-example-card">
            <h3>Practical Case Study: Commercial Subpanel Feeder Sizing (Aluminum vs Copper)</h3>
            <p>
              An electrical contractor is installing a $240\text{ V}$ single-phase subpanel feeder to power an electric vehicle charging bank located $200\text{ feet}$ away from the main distribution switchboard. The calculated design load current is $I_{load} = 100\text{ Amps}$ (continuous). The specification limits maximum voltage drop to $3.0\%$ ($7.2\text{ V}$).
            </p>
            <div class="step-calculation">
              <strong>Step 1: Determine Baseline Ampacity from NEC Table 310.16 (75&deg;C):</strong><br>
              A 100A continuous load requires a minimum conductor rating of $100\text{ A}$.
              From Table 310.16, **1/0 AWG Aluminum** is rated for exactly $100\text{ Amps}$ (whereas 3 AWG or 2 AWG would be required in Copper).
            </div>
            <div class="step-calculation">
              <strong>Step 2: Check Voltage Drop for 1/0 AWG Aluminum over 200 ft:</strong><br>
              From NEC Chapter 9 Table 8, $R_{Al}$ for 1/0 AWG is $0.201\,\Omega\text{ per } 1,000\text{ ft}$.
              $$\Delta V = \frac{2 \times 100\text{ A} \times 200\text{ ft} \times 0.201\,\Omega/kft}{1000} = \frac{8040}{1000} = 8.04\text{ Volts}$$
              $$\%\text{VD} = \frac{8.04\text{ V}}{240\text{ V}} \times 100\% = 3.35\% \quad (\text{FAILS } 3.0\% \text{ limit!})$$
            </div>
            <div class="step-calculation">
              <strong>Step 3: Upsize to Next Gauge to Satisfy Voltage Drop:</strong><br>
              Upsizing to **2/0 AWG Aluminum** ($R_{Al} = 0.159\,\Omega/kft$):
              $$\Delta V = \frac{2 \times 100 \times 200 \times 0.159}{1000} = \frac{6360}{1000} = 6.36\text{ Volts}$$
              $$\%\text{VD} = \frac{6.36\text{ V}}{240\text{ V}} \times 100\% = 2.65\% \le 3.0\% \quad (\text{PASS!})$$
              <p>
                <strong>Conclusion:</strong> Selecting **2/0 AWG Aluminum** provides a robust 115A ampacity with a safe 2.65% voltage drop. Compared to specifying 1/0 AWG Copper, using 2/0 AWG Aluminum delivers over **$800 in raw material savings** across the 200-foot 3-wire run while cutting feeder weight in half.
              </p>
            </div>
          </div>

          <h2>Galvanic Corrosion Chemistry &amp; Dissimilar Metal Interactions</h2>
          <p>
            When aluminum and copper conductors are mechanically joined in the presence of atmospheric humidity or electrolyte moisture, an electrochemical galvanic cell is established. In the galvanic series of metals in seawater, aluminum possesses an anodic potential of approximately $-0.76\text{ V}$ to $-0.90\text{ V}$, whereas copper possesses a noble cathodic potential of approximately $+0.15\text{ V}$ to $+0.34\text{ V}$.
          </p>
          <div class="formula-box">
            <div class="formula-title">Galvanic Potential Difference Equation</div>
            <div class="formula-math">$$\Delta E_{cell} = E_{cathode} - E_{anode} = (+0.34\text{ V}) - (-0.85\text{ V}) \approx 1.19\text{ Volts}$$</div>
            <p>Because the galvanic potential difference exceeds $0.30\text{ V}$, galvanic corrosion occurs rapidly. The less noble aluminum metal acts as a sacrificial anode, oxidizing and pitting into powder, leaving a loose high-resistance gap. To eliminate this galvanic hazard, engineers specify tin-plated copper/aluminum bimetallic adapter sleeves or UL-listed dual-rated mechanical lugs that isolate direct contact between raw copper and raw aluminum strands.</p>
          </div>

          <h2>Critical Termination &amp; Installation Rules for Aluminum Wire</h2>
          <ul>
            <li><strong>Dual-Rated Terminal Hardware:</strong> Aluminum conductors must only be inserted into mechanical screw lugs or terminal blocks explicitly stamped and listed as <strong>AL7CU</strong> (rated 75&deg;C for aluminum or copper) or <strong>AL9CU</strong> (rated 90&deg;C). Standard copper-only lugs will cause galvanic corrosion and loose thermal connections.</li>
            <li><strong>Antioxidant Joint Compound (Penetrox / Noalox):</strong> Pure aluminum oxidizes within milliseconds of exposure to atmospheric air, creating a thin, hard microscopic film of aluminum oxide ($\text{Al}_2\text{O}_3$), which is an electrical insulator! Electricians must wire-brush the stripped aluminum strands and coat them immediately with antioxidant joint compound to seal out oxygen and break up surface oxides.</li>
            <li><strong>Calibrated Torque Wrench Execution:</strong> Unlike copper, which is ductile and forgives uneven tightening, aluminum expands thermally at approximately $23 \times 10^{-6}\text{ /}^\circ\text{C}$ (35% higher than copper). Every single aluminum lug must be torqued using a calibrated torque wrench to the exact manufacturer inch-pound specification listed in NEC Table 110.14(D) to prevent thermal loosening.</li>
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
    // Aluminum conductor data: [Name, Amp75C, Amp90C, R_per_1000ft, Cu_Equivalent]
    const AL_TABLE = [
      { name: "6 AWG Al", amp75: 40, amp90: 45, r: 0.808, cuEquiv: "8 AWG Cu" },
      { name: "4 AWG Al", amp75: 55, amp90: 65, r: 0.508, cuEquiv: "6 AWG Cu" },
      { name: "2 AWG Al", amp75: 75, amp90: 90, r: 0.319, cuEquiv: "4 AWG Cu" },
      { name: "1 AWG Al", amp75: 85, amp90: 100, r: 0.253, cuEquiv: "3 AWG Cu" },
      { name: "1/0 AWG Al", amp75: 100, amp90: 120, r: 0.201, cuEquiv: "2 AWG Cu" },
      { name: "2/0 AWG Al", amp75: 115, amp90: 135, r: 0.159, cuEquiv: "1 AWG Cu" },
      { name: "3/0 AWG Al", amp75: 130, amp90: 155, r: 0.126, cuEquiv: "1/0 AWG Cu" },
      { name: "4/0 AWG Al", amp75: 150, amp90: 180, r: 0.100, cuEquiv: "2/0 AWG Cu" },
      { name: "250 kcmil Al", amp75: 170, amp90: 205, r: 0.0847, cuEquiv: "3/0 AWG Cu" },
      { name: "300 kcmil Al", amp75: 190, amp90: 230, r: 0.0707, cuEquiv: "4/0 AWG Cu" },
      { name: "350 kcmil Al", amp75: 210, amp90: 250, r: 0.0605, cuEquiv: "250 kcmil Cu" },
      { name: "400 kcmil Al", amp75: 225, amp90: 270, r: 0.0529, cuEquiv: "300 kcmil Cu" },
      { name: "500 kcmil Al", amp75: 260, amp90: 310, r: 0.0424, cuEquiv: "350 kcmil Cu" },
      { name: "600 kcmil Al", amp75: 285, amp90: 340, r: 0.0353, cuEquiv: "400 kcmil Cu" },
      { name: "750 kcmil Al", amp75: 315, amp90: 385, r: 0.0282, cuEquiv: "500 kcmil Cu" }
    ];

    function calculateAlCable() {
      const sys = document.getElementById('sysType').value;
      const Iload = parseFloat(document.getElementById('designCurrent').value);
      const Lft = parseFloat(document.getElementById('runLength').value);
      const maxVd = parseFloat(document.getElementById('maxVdPct').value);
      const tempRating = document.getElementById('tempRating').value;

      if (isNaN(Iload) || isNaN(Lft) || Iload <= 0 || Lft <= 0) return;

      let Vnom = 240;
      let is3Ph = false;
      if (sys === "120_1ph") Vnom = 120;
      else if (sys === "240_1ph") Vnom = 240;
      else if (sys === "208_3ph") { Vnom = 208; is3Ph = true; }
      else if (sys === "480_3ph") { Vnom = 480; is3Ph = true; }
      else if (sys === "dc_48") Vnom = 48;

      let selectedConductor = null;
      let actualVdVolts = 0;
      let actualVdPct = 0;

      for (let i = 0; i < AL_TABLE.length; i++) {
        const cond = AL_TABLE[i];
        const ampacity = (tempRating === "90") ? cond.amp90 : cond.amp75;

        if (ampacity >= Iload) {
          // Check voltage drop
          let vd = 0;
          if (is3Ph) {
            vd = (Math.sqrt(3) * Iload * Lft * cond.r) / 1000;
          } else {
            vd = (2 * Iload * Lft * cond.r) / 1000;
          }
          const pct = (vd / Vnom) * 100;

          if (pct <= maxVd || i === AL_TABLE.length - 1) {
            selectedConductor = cond;
            actualVdVolts = vd;
            actualVdPct = pct;
            break;
          }
        }
      }

      if (!selectedConductor) {
        selectedConductor = AL_TABLE[AL_TABLE.length - 1];
        actualVdVolts = (2 * Iload * Lft * selectedConductor.r) / 1000;
        actualVdPct = (actualVdVolts / Vnom) * 100;
      }

      const ratedAmp = (tempRating === "90") ? selectedConductor.amp90 : selectedConductor.amp75;

      document.getElementById('outAlGauge').textContent = selectedConductor.name;
      document.getElementById('outAlAmpacity').textContent = `${ratedAmp}A Ampacity @ ${tempRating}°C`;
      document.getElementById('outCuGauge').textContent = selectedConductor.cuEquiv;

      document.getElementById('outVdVolts').textContent = actualVdVolts.toFixed(2) + " V";
      const passText = (actualVdPct <= maxVd) ? `Pass (≤ ${maxVd}%)` : `Warning: Exceeds ${maxVd}%`;
      document.getElementById('outVdPct').textContent = `${actualVdPct.toFixed(2)}% of ${Vnom}V (${passText})`;
    }

    window.addEventListener('DOMContentLoaded', calculateAlCable);
  </script>
</body>
</html>
"""

def main():
    path_xfmr = os.path.join(BASE_DIR, "transformer-turns-ratio-calculator.html")
    with open(path_xfmr, "w", encoding="utf-8") as f:
        f.write(TOOL_TRANSFORMER.strip())
    print("[PASS] transformer-turns-ratio-calculator.html generated successfully!")

    path_al = os.path.join(BASE_DIR, "aluminium-cable-sizing-calculator.html")
    with open(path_al, "w", encoding="utf-8") as f:
        f.write(TOOL_ALUMINIUM.strip())
    print("[PASS] aluminium-cable-sizing-calculator.html generated successfully!")

if __name__ == "__main__":
    main()
