# -*- coding: utf-8 -*-
"""
Script to generate Batch 8 Part 3 tools:
5. three-phase-cable-sizing-calculator.html
6. wire-gauge-calculator.html
"""
import os

TOOL_5_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Three Phase Cable Sizing Calculator | 400V & 480V Industrial Wire Sizing</title>
  <meta name="description" content="Calculate three-phase electrical cable sizes (mm² and kcmil) for 400V, 480V, and 690V industrial power systems. Computes full-load current, balanced line voltage drop, and thermal derating per IEC 60364 and NEC.">
  <link rel="canonical" href="https://calchub.cloud/three-phase-cable-sizing-calculator.html">
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
        "name": "Three Phase Cable Sizing Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Industrial three-phase low-voltage cable dimensioning tool calculating symmetrical line currents, vector impedance voltage drop, and installation derating per IEC 60364-5-52.",
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
            "name": "How is balanced three-phase line current calculated from active power (kW)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For a balanced three-phase AC circuit: I = (P_kW * 1000) / (sqrt(3) * V_LL * cos(theta)), where V_LL is line-to-line RMS voltage and cos(theta) is the operating power factor. For apparent power in kVA: I = (S_kVA * 1000) / (sqrt(3) * V_LL)."
            }
          },
          {
            "@type": "Question",
            "name": "Why is the three-phase voltage drop formula multiplied by sqrt(3) instead of 2?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In a balanced three-phase system, the return currents in the three phase conductors are 120 degrees out of phase and sum vectorially to zero at the neutral star point. Line-to-line voltage drop between any two phase conductors is derived from the geometric phase displacement: Delta_V_LL = sqrt(3) * I * L * (R * cos(theta) + X * sin(theta)), resulting in sqrt(3) approx 1.732 rather than 2.0."
            }
          },
          {
            "@type": "Question",
            "name": "When does cable inductive reactance (X) become significant in three-phase sizing?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For conductor cross-sections up to 16 mm², cable resistance R is large and reactance X is negligible. However, for heavy feeders of 25 mm² and larger, conductor self-inductance and mutual phase inductance (typically 0.08 to 0.09 mOhm/m) contribute significantly to impedance. At 0.80 power factor, reactive drop X * sin(theta) can account for 20% to 35% of total voltage drop."
            }
          },
          {
            "@type": "Question",
            "name": "What is the standard permissible voltage drop for three-phase commercial installations?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Under IEC 60364-5-52 Annex G, the recommended maximum voltage drop is 3% for lighting circuits and 5% for other general power and motor circuits supplied directly from the low-voltage public grid. For installations fed from an on-site private transformer substation, limits expand to 6% for lighting and 8% for power."
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
      <span>Three Phase Cable Sizing Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">IEC 60364-5-52 &amp; NEC 310 Industrial Standards</div>
          <h1 class="calc-title">Three Phase Cable Sizing Calculator</h1>
          <p class="calc-tagline">Calculate three-phase feeder cable sizing, balanced line-to-line voltage drop, thermal derating, and breaker coordination.</p>
        </header>

        <!-- Tool Card -->
        <div class="tool-card">
          <form id="threePhaseForm" onsubmit="return false;">
            <div class="calc-grid">
              <div class="form-group">
                <label for="tpSystemVoltage" class="form-label">Line-to-Line Voltage ($V_{LL}$)</label>
                <select id="tpSystemVoltage" class="form-control" onchange="calculateThreePhase()">
                  <option value="400" selected>400V Three-Phase AC (50/60 Hz Standard)</option>
                  <option value="480">480V Three-Phase AC (North American Industrial)</option>
                  <option value="208">208V Three-Phase AC (Commercial Light Power)</option>
                  <option value="690">690V Three-Phase AC (Heavy Industrial / Mining / Marine)</option>
                </select>
                <small class="form-hint">Nominal phase-to-phase system voltage</small>
              </div>

              <div class="form-group">
                <label for="tpInputMode" class="form-label">Load Specification Mode</label>
                <select id="tpInputMode" class="form-control" onchange="calculateThreePhase()">
                  <option value="current" selected>Direct Full-Load Current (Amperes)</option>
                  <option value="power_kw">Active Power Rating (Kilowatts kW)</option>
                  <option value="apparent_kva">Apparent Power Rating (kVA)</option>
                </select>
                <small class="form-hint">Select input parameter type</small>
              </div>

              <div class="form-group">
                <label for="tpLoadValue" class="form-label">Load Value</label>
                <div class="input-with-unit">
                  <input type="number" id="tpLoadValue" class="form-control" value="85" min="1" max="2500" step="1" oninput="calculateThreePhase()">
                  <span id="tpUnitBadge" class="unit-badge">Amps</span>
                </div>
                <small class="form-hint">Operating load magnitude</small>
              </div>

              <div class="form-group">
                <label for="tpPowerFactor" class="form-label">Power Factor ($\cos\varphi$)</label>
                <div class="input-with-unit">
                  <input type="number" id="tpPowerFactor" class="form-control" value="0.85" min="0.5" max="1.0" step="0.05" oninput="calculateThreePhase()">
                  <span class="unit-badge">$\cos\varphi$</span>
                </div>
                <small class="form-hint">Standard industrial motor is 0.80 to 0.88</small>
              </div>

              <div class="form-group">
                <label for="tpConductorMetal" class="form-label">Conductor Metallurgy</label>
                <select id="tpConductorMetal" class="form-control" onchange="calculateThreePhase()">
                  <option value="copper" selected>Annealed Electrolytic Copper (Cu)</option>
                  <option value="aluminum">Electrical Grade Aluminum (Al)</option>
                </select>
                <small class="form-hint">Conductor core metal</small>
              </div>

              <div class="form-group">
                <label for="tpInsulation" class="form-label">Insulation Thermal Class</label>
                <select id="tpInsulation" class="form-control" onchange="calculateThreePhase()">
                  <option value="xlpe" selected>XLPE / EPR Thermosetting (Max 90°C)</option>
                  <option value="pvc">PVC Thermoplastic (Max 70°C)</option>
                </select>
                <small class="form-hint">Operating temperature limit</small>
              </div>

              <div class="form-group">
                <label for="tpInstallMethod" class="form-label">Installation Reference Method</label>
                <select id="tpInstallMethod" class="form-control" onchange="calculateThreePhase()">
                  <option value="E" selected>Method E: In free air on perforated cable tray</option>
                  <option value="C">Method C: Clipped direct to masonry surface</option>
                  <option value="B1">Method B1: Conduit on wooden/masonry surface</option>
                  <option value="D1">Method D1: Multi-core in underground buried duct</option>
                </select>
                <small class="form-hint">IEC 60364-5-52 mounting reference</small>
              </div>

              <div class="form-group">
                <label for="tpRouteLength" class="form-label">One-Way Feeder Route Length ($L$)</label>
                <div class="input-with-unit">
                  <input type="number" id="tpRouteLength" class="form-control" value="75" min="1" step="5" oninput="calculateThreePhase()">
                  <span class="unit-badge">metres</span>
                </div>
                <small class="form-hint">Distance from switchboard to subpanel</small>
              </div>

              <div class="form-group">
                <label for="tpAmbientTemp" class="form-label">Ambient Temperature</label>
                <div class="input-with-unit">
                  <input type="number" id="tpAmbientTemp" class="form-control" value="35" min="10" max="65" step="1" oninput="calculateThreePhase()">
                  <span class="unit-badge">°C</span>
                </div>
                <small class="form-hint">Ambient switchroom or plant temperature</small>
              </div>

              <div class="form-group">
                <label for="tpMaxVd" class="form-label">Maximum Allowable Voltage Drop</label>
                <div class="input-with-unit">
                  <input type="number" id="tpMaxVd" class="form-control" value="4.0" min="1.0" max="10.0" step="0.5" oninput="calculateThreePhase()">
                  <span class="unit-badge">%</span>
                </div>
                <small class="form-hint">Standard threshold (typically 4.0% for sub-mains)</small>
              </div>
            </div>

            <button type="button" id="calcTpBtn" class="btn btn-primary btn-block" onclick="calculateThreePhase()">Calculate Three-Phase Cable Size</button>
          </form>

          <div id="tpResultBox" class="results-container" style="margin-top:20px;">
            <h3>Three-Phase Sizing Results</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label">Recommended Conductor Area</span>
                <span id="tpCableSizeOut" class="result-value">-- mm²</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Calculated Line Current ($I_b$)</span>
                <span id="tpCurrentOut" class="result-value">-- A</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Derated Current Capacity ($I_z$)</span>
                <span id="tpIzOut" class="result-value">-- A</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Three-Phase Voltage Drop ($\Delta V$)</span>
                <span id="tpVdOut" class="result-value">-- V (-- %)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Three-Phase $I^2 R$ Power Loss</span>
                <span id="tpPowerLossOut" class="result-value">-- Watts</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Overcurrent Protection Rating ($I_n$)</span>
                <span id="tpBreakerOut" class="result-value">-- A Standard</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Engineering Principles of Three-Phase Low-Voltage Cable Sizing</h2>
          
          <p>Polyphase alternating current systems, formulated by Nikola Tesla and standardized across global utility grids, represent the most thermodynamically efficient method of transmitting and utilizing electrical power. A three-phase power circuit consists of three alternating sinusoidal currents of identical frequency and peak amplitude, separated in time by a phase displacement angle of exactly $120^\circ$ ($2\pi/3\text{ radians}$). This unique symmetry produces a constant total electrical power transfer and creates a rotating magnetic field in the stators of AC induction motors without requiring starting capacitors.</p>

          <p>Dimensioning three-phase feeders and branch circuits requires adhering strictly to international electrical engineering codes, including <strong>IEC 60364-5-52</strong>, <strong>BS 7671 (IET Wiring Regulations)</strong>, and <strong>NFPA 70 National Electrical Code (NEC Article 310)</strong>.</p>

          <div class="formula-box">
            <h3>Three-Phase Power and Current Formulation</h3>
            <p>For any balanced three-phase system, total real power ($P$ in Watts), apparent power ($S$ in Volt-Amperes), and line current ($I$ in Amperes) are related by:</p>
            <p>$$P = \sqrt{3} \times V_{LL} \times I \times \cos\varphi$$</p>
            <p>$$S = \sqrt{3} \times V_{LL} \times I$$</p>
            <p>Where $V_{LL}$ represents the line-to-line root-mean-square voltage (e.g. $400\text{V}$ or $480\text{V}$), and $\cos\varphi$ represents the operating power factor. Solving for continuous operating current ($I_b$):</p>
            <p>$$I_b = \frac{P}{\sqrt{3} \times V_{LL} \times \cos\varphi} = \frac{S}{\sqrt{3} \times V_{LL}}$$</p>
          </div>

          <h3>Symmetrical Three-Phase Voltage Drop Mechanics</h3>
          <p>Unlike single-phase circuits where current travels out through the active wire and must return through the neutral wire ($2 \times L$ loop length), balanced three-phase systems share return paths among the three phases. The instantaneous sum of the three phase currents at any instant is zero:</p>
          <p>$$i_A(t) + i_B(t) + i_C(t) = 0$$</p>
          <p>Consequently, the neutral conductor carries zero fundamental current under balanced loads. The line-to-line voltage degradation between phase conductors is derived from the vector difference between phase potentials:</p>
          
          <p>$$\Delta V_{3\phi} = \sqrt{3} \times I_b \times L \times (R \cos\varphi + X \sin\varphi)$$</p>
          <p>$$\Delta V\% = \frac{\Delta V_{3\phi}}{V_{LL}} \times 100$$</p>

          <p>Where $R$ is the AC conductor resistance at maximum operating temperature ($70^\circ\text{C}$ for PVC, $90^\circ\text{C}$ for XLPE) in $\Omega/\text{m}$, $X$ is the conductor reactance ($\approx 0.08\text{ m}\Omega/\text{m}$ for low-voltage multicore cables) in $\Omega/\text{m}$, and $L$ is the one-way circuit route distance in meters.</p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Conductor Area (mm²)</th>
                <th>Method E (Tray) XLPE 90°C</th>
                <th>Method C (Clipped) XLPE 90°C</th>
                <th>AC Resistance at 90°C (Ω/km)</th>
                <th>Reactance X at 50 Hz (Ω/km)</th>
                <th>3-Phase (mV/A/m) Factor</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>16 mm²</strong></td>
                <td>110 A</td>
                <td>98 A</td>
                <td>$1.46\ \Omega/\text{km}$</td>
                <td>$0.083\ \Omega/\text{km}$</td>
                <td>$2.40\text{ mV/A/m}$</td>
              </tr>
              <tr>
                <td><strong>25 mm²</strong></td>
                <td>146 A</td>
                <td>127 A</td>
                <td>$0.927\ \Omega/\text{km}$</td>
                <td>$0.082\ \Omega/\text{km}$</td>
                <td>$1.50\text{ mV/A/m}$</td>
              </tr>
              <tr>
                <td><strong>35 mm²</strong></td>
                <td>180 A</td>
                <td>158 A</td>
                <td>$0.669\ \Omega/\text{km}$</td>
                <td>$0.081\ \Omega/\text{km}$</td>
                <td>$1.10\text{ mV/A/m}$</td>
              </tr>
              <tr>
                <td><strong>50 mm²</strong></td>
                <td>219 A</td>
                <td>192 A</td>
                <td>$0.499\ \Omega/\text{km}$</td>
                <td>$0.080\ \Omega/\text{km}$</td>
                <td>$0.80\text{ mV/A/m}$</td>
              </tr>
              <tr>
                <td><strong>70 mm²</strong></td>
                <td>279 A</td>
                <td>246 A</td>
                <td>$0.342\ \Omega/\text{km}$</td>
                <td>$0.079\ \Omega/\text{km}$</td>
                <td>$0.55\text{ mV/A/m}$</td>
              </tr>
              <tr>
                <td><strong>95 mm²</strong></td>
                <td>338 A</td>
                <td>298 A</td>
                <td>$0.247\ \Omega/\text{km}$</td>
                <td>$0.078\ \Omega/\text{km}$</td>
                <td>$0.40\text{ mV/A/m}$</td>
              </tr>
              <tr>
                <td><strong>120 mm²</strong></td>
                <td>392 A</td>
                <td>346 A</td>
                <td>$0.196\ \Omega/\text{km}$</td>
                <td>$0.077\ \Omega/\text{km}$</td>
                <td>$0.31\text{ mV/A/m}$</td>
              </tr>
              <tr>
                <td><strong>150 mm²</strong></td>
                <td>451 A</td>
                <td>399 A</td>
                <td>$0.159\ \Omega/\text{km}$</td>
                <td>$0.077\ \Omega/\text{km}$</td>
                <td>$0.25\text{ mV/A/m}$</td>
              </tr>
              <tr>
                <td><strong>185 mm²</strong></td>
                <td>515 A</td>
                <td>456 A</td>
                <td>$0.128\ \Omega/\text{km}$</td>
                <td>$0.076\ \Omega/\text{km}$</td>
                <td>$0.20\text{ mV/A/m}$</td>
              </tr>
              <tr>
                <td><strong>240 mm²</strong></td>
                <td>607 A</td>
                <td>538 A</td>
                <td>$0.098\ \Omega/\text{km}$</td>
                <td>$0.075\ \Omega/\text{km}$</td>
                <td>$0.155\text{ mV/A/m}$</td>
              </tr>
            </tbody>
          </table>

          <div class="worked-example-card">
            <h3>Practical Worked Engineering Example: 50 kW Industrial Sub-Main Sizing</h3>
            <p><strong>Design Scenario:</strong> Size a three-phase, 400V, 50 Hz sub-main feeder supplying an industrial process heating panel. Total active load is $P = 50\text{ kW}$ operating at $\cos\varphi = 0.85$ lagging. The feeder is routed $75\text{ meters}$ along a perforated cable tray (Method E) inside a manufacturing plant where ambient summer temperature reaches $35^\circ\text{C}$. Multi-core copper cable with XLPE ($90^\circ\text{C}$) insulation is specified. Maximum allowable line voltage drop is $4.0\%$.</p>

            <p><strong>Step 1: Compute Full-Load Operating Current ($I_b$)</strong></p>
            <p>$$I_b = \frac{50 \times 1000}{\sqrt{3} \times 400 \times 0.85} = \frac{50{,}000}{1.732 \times 340} = \frac{50{,}000}{588.88} = 84.91\text{ Amperes}$$</p>

            <p><strong>Step 2: Select Overcurrent Protective Device ($I_n$)</strong></p>
            <p>The standard nominal circuit breaker rating immediately above $84.91\text{ A}$ is $I_n = 100\text{ A}$.</p>

            <p><strong>Step 3: Thermal Ampacity Sizing with Ambient Derating</strong></p>
            <p>At $35^\circ\text{C}$ ambient, XLPE derating factor $C_a = \sqrt{\frac{90 - 35}{90 - 30}} = 0.957$.</p>
            <p>Required base tabulated ampacity:</p>
            <p>$$I_0 \ge \frac{I_n}{C_a} = \frac{100\text{ A}}{0.957} = 104.49\text{ A}$$</p>
            <p>Referring to Table 4E2A (Method E XLPE Copper):</p>
            <ul>
              <li>$16\text{ mm}^2 \implies I_0 = 110\text{ A}$ ($110 \ge 104.49\text{ A} \implies$ Thermal PASS)</li>
            </ul>
            <p>Derated capacity of $16\text{ mm}^2$: $I_z = 110 \times 0.957 = 105.27\text{ A} \ge 100\text{ A}$.</p>

            <p><strong>Step 4: Check Voltage Drop on $16\text{ mm}^2$</strong></p>
            <p>For $16\text{ mm}^2$ copper XLPE, $(mV/A/m) = 2.40\text{ mV/A/m}$:</p>
            <p>$$\Delta V = \frac{2.40 \times 84.91\text{ A} \times 75\text{ m}}{1000} = \frac{15{,}283.8}{1000} = 15.28\text{ Volts}$$</p>
            <p>$$\Delta V\% = \frac{15.28\text{ V}}{400\text{ V}} \times 100 = 3.82\%$$</p>
            <p>Since $3.82\% \le 4.0\%$, the $16\text{ mm}^2$ XLPE copper cable satisfies all thermal, regulatory, and voltage drop requirements.</p>
          </div>

          <h2>Frequently Asked Questions (Three-Phase Cable Sizing)</h2>
          <div class="faq-item">
            <h3>When must parallel conductors be used for large three-phase feeders?</h3>
            <p>When continuous load currents exceed $400\text{ A}$ to $500\text{ A}$, single massive cables (such as $300\text{ mm}^2$ or $400\text{ mm}^2$) become difficult to pull and suffer from skin effect and thermal heat entrapment. Paralleling two or more smaller conductors per phase (e.g. two runs of $150\text{ mm}^2$ instead of one $300\text{ mm}^2$) reduces overall cable weight, eases bending radius constraints, and provides superior surface-area-to-volume thermal dissipation.</p>
          </div>

          <div class="faq-item">
            <h3>Why must all phase conductors of a three-phase circuit be routed in the same metallic conduit?</h3>
            <p>Under NEC 300.3(B) and IEC 60364-5-52, all three phase conductors (and the neutral) must pass through the same metal raceway or armor opening. If individual phases are routed through separate steel conduits, alternating magnetic flux induces massive eddy currents and hysteresis heating in the enclosing steel pipe, creating an induction furnace effect that melts cable insulation.</p>
          </div>

          <div class="faq-item">
            <h3>What causes neutral conductor overheating in balanced three-phase systems?</h3>
            <p>While fundamental 50/60 Hz balanced currents cancel in the neutral, non-linear electronic loads (switched-mode computer supplies, LED drivers, VFDs) generate third-order triplen harmonics (150 Hz, 450 Hz). Triplen harmonics are in-phase with each other and add arithmetically in the neutral, frequently causing neutral currents to reach $130\%$ to $170\%$ of phase currents. In such systems, 200% oversized neutrals or active harmonic filters are mandatory.</p>
          </div>

          <div class="faq-item">
            <h3>What is the difference between three-core and four-core cables?</h3>
            <p>A 3-core cable contains three insulated phase conductors (L1, L2, L3) and is used for pure three-phase balanced loads that require no neutral (such as 3-phase electric motors, delta-connected heaters, and pumps). A 4-core cable includes a full-sized neutral conductor (L1, L2, L3, N) required to supply single-phase line-to-neutral sub-circuits from a four-wire wye distribution board.</p>
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
    // Standard IEC Three-Phase Ratings Table (Copper base values)
    const tpRatingsTable = [
      { size: 1.5,  c_xlpe: 25,  c_pvc: 19.5, mv: 25.0, r90: 15.4,   x: 0.111 },
      { size: 2.5,  c_xlpe: 33,  c_pvc: 26.5, mv: 15.0, r90: 9.45,   x: 0.102 },
      { size: 4.0,  c_xlpe: 45,  c_pvc: 36.0, mv: 9.5,  r90: 5.88,   x: 0.096 },
      { size: 6.0,  c_xlpe: 58,  c_pvc: 46.0, mv: 6.4,  r90: 3.93,   x: 0.090 },
      { size: 10.0, c_xlpe: 80,  c_pvc: 63.0, mv: 3.8,  r90: 2.33,   x: 0.086 },
      { size: 16.0, c_xlpe: 110, c_pvc: 85.0, mv: 2.4,  r90: 1.46,   x: 0.083 },
      { size: 25.0, c_xlpe: 146, c_pvc: 110,  mv: 1.50, r90: 0.927,  x: 0.082 },
      { size: 35.0, c_xlpe: 180, c_pvc: 137,  mv: 1.10, r90: 0.669,  x: 0.081 },
      { size: 50.0, c_xlpe: 219, c_pvc: 167,  mv: 0.80, r90: 0.499,  x: 0.080 },
      { size: 70.0, c_xlpe: 279, c_pvc: 216,  mv: 0.55, r90: 0.342,  x: 0.079 },
      { size: 95.0, c_xlpe: 338, c_pvc: 264,  mv: 0.40, r90: 0.247,  x: 0.078 },
      { size: 120,  c_xlpe: 392, c_pvc: 308,  mv: 0.31, r90: 0.196,  x: 0.077 },
      { size: 150,  c_xlpe: 451, c_pvc: 356,  mv: 0.25, r90: 0.159,  x: 0.077 },
      { size: 185,  c_xlpe: 515, c_pvc: 409,  mv: 0.20, r90: 0.128,  x: 0.076 },
      { size: 240,  c_xlpe: 607, c_pvc: 485,  mv: 0.155, r90: 0.098, x: 0.075 },
      { size: 300,  c_xlpe: 701, c_pvc: 561,  mv: 0.125, r90: 0.078, x: 0.075 }
    ];

    const standardBreakers3Ph = [16, 20, 25, 32, 40, 50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800];

    const tpMethodMult = {
      "E": 1.00,
      "C": 0.90,
      "B1": 0.80,
      "D1": 0.85
    };

    function calculateThreePhase() {
      const vLL = parseFloat(document.getElementById("tpSystemVoltage").value) || 400;
      const mode = document.getElementById("tpInputMode").value;
      const loadVal = parseFloat(document.getElementById("tpLoadValue").value) || 1;
      const pf = parseFloat(document.getElementById("tpPowerFactor").value) || 0.85;
      const metal = document.getElementById("tpConductorMetal").value;
      const insulation = document.getElementById("tpInsulation").value;
      const method = document.getElementById("tpInstallMethod").value;
      const length = parseFloat(document.getElementById("tpRouteLength").value) || 1;
      const ambTemp = parseFloat(document.getElementById("tpAmbientTemp").value) || 30;
      const maxVd = parseFloat(document.getElementById("tpMaxVd").value) || 4.0;

      // Update unit badge
      const unitBadge = document.getElementById("tpUnitBadge");
      if (mode === "current") unitBadge.innerText = "Amps";
      else if (mode === "power_kw") unitBadge.innerText = "kW";
      else if (mode === "apparent_kva") unitBadge.innerText = "kVA";

      let ib = 0;
      if (mode === "current") {
        ib = loadVal;
      } else if (mode === "power_kw") {
        ib = (loadVal * 1000) / (Math.sqrt(3) * vLL * pf);
      } else if (mode === "apparent_kva") {
        ib = (loadVal * 1000) / (Math.sqrt(3) * vLL);
      }

      // Next standard breaker >= ib
      let inBreaker = standardBreakers3Ph[standardBreakers3Ph.length - 1];
      for (let i = 0; i < standardBreakers3Ph.length; i++) {
        if (standardBreakers3Ph[i] >= ib) {
          inBreaker = standardBreakers3Ph[i];
          break;
        }
      }

      // Ca
      let ca = 1.0;
      if (insulation === "xlpe") {
        ca = Math.sqrt(Math.max(0.1, (90 - ambTemp) / (90 - 30)));
      } else {
        ca = Math.sqrt(Math.max(0.1, (70 - ambTemp) / (70 - 30)));
      }

      const methodFactor = tpMethodMult[method] || 1.0;
      const condMult = (metal === "aluminum") ? 0.78 : 1.0;

      let selected = null;

      for (let i = 0; i < tpRatingsTable.length; i++) {
        const row = tpRatingsTable[i];
        let baseRating = (insulation === "xlpe") ? row.c_xlpe : row.c_pvc;
        const deratedIz = baseRating * methodFactor * condMult * ca;

        if (deratedIz < inBreaker) continue;

        let mvVal = row.mv;
        if (metal === "aluminum") mvVal *= 1.64;

        const deltaV = (mvVal * ib * length) / 1000;
        const vdPct = (deltaV / vLL) * 100;

        if (vdPct <= maxVd) {
          // Three phase power loss = 3 * I^2 * R
          const rPerM = (row.r90 * ((metal === "aluminum") ? 1.64 : 1.0)) / 1000;
          const rLine = length * rPerM;
          const pLoss = 3 * ib * ib * rLine;

          selected = {
            size: row.size,
            iz: deratedIz,
            deltaV: deltaV,
            vdPct: vdPct,
            pLoss: pLoss
          };
          break;
        }
      }

      document.getElementById("tpCurrentOut").innerText = ib.toFixed(1) + " A";
      document.getElementById("tpBreakerOut").innerText = inBreaker + " A Standard Breaker";

      if (selected) {
        document.getElementById("tpCableSizeOut").innerText = selected.size + " mm² (" + metal.toUpperCase() + ")";
        document.getElementById("tpIzOut").innerText = selected.iz.toFixed(1) + " A";
        document.getElementById("tpVdOut").innerText = selected.deltaV.toFixed(2) + " V (" + selected.vdPct.toFixed(2) + "%)";
        document.getElementById("tpPowerLossOut").innerText = selected.pLoss.toFixed(1) + " W";
      } else {
        document.getElementById("tpCableSizeOut").innerText = "> 300 mm² (Parallel Conductors Req.)";
        document.getElementById("tpIzOut").innerText = "--";
        document.getElementById("tpVdOut").innerText = "Exceeds Drop Limit";
        document.getElementById("tpPowerLossOut").innerText = "--";
      }
    }

    document.addEventListener("DOMContentLoaded", function() {
      calculateThreePhase();
    });
  </script>
</body>
</html>
"""

TOOL_6_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Wire Gauge Calculator | AWG to mm² Conversion, Resistance & Ampacity</title>
  <meta name="description" content="Calculate American Wire Gauge (AWG) wire diameter, cross-sectional area (mm² and circular mils), electrical resistance (Ohms/kft and Ohms/km), and voltage drop.">
  <link rel="canonical" href="https://calchub.cloud/wire-gauge-calculator.html">
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
        "name": "Wire Gauge Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Comprehensive American Wire Gauge (AWG) and metric wire cross-section calculator computing exact geometric diameter, circular mils, resistance, and maximum ampacity.",
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
            "name": "How is American Wire Gauge (AWG) mathematically defined?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The American Wire Gauge (AWG / Brown & Sharpe) system is a logarithmic progression standardized in 1857. It defines #36 AWG as exactly 0.0050 inches (0.127 mm) diameter and #0000 (4/0) AWG as exactly 0.4600 inches (11.684 mm) diameter. The ratio between consecutive gauge diameters is constant: 92^(1/39) approx 1.122932."
            }
          },
          {
            "@type": "Question",
            "name": "What are circular mils and how do they relate to square millimeters?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A circular mil (cmil) is the area of a circle with a diameter of 1 mil (0.001 inch). One circular mil equals (pi / 4) * 10^-6 square inches, or approximately 0.0005067 mm². Circular mils simplify wire sizing because the area of any round conductor equals its diameter in mils squared: Area_cmil = (d_mils)^2."
            }
          },
          {
            "@type": "Question",
            "name": "What are the handy mental rules of thumb for the AWG wire scale?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Three fundamental AWG geometric rules: (1) An increase of 3 gauge numbers doubles wire resistance and halves cross-sectional area (e.g. #10 AWG has double the resistance of #7 AWG). (2) An increase of 6 gauge numbers halves wire diameter. (3) An increase of 10 gauge numbers multiplies resistance tenfold and divides area by 10."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between chassis wiring ampacity and power transmission ampacity?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Chassis wiring ratings apply to short, single unbundled conductors exposed in open equipment enclosures where convective cooling is excellent. Power transmission ampacity (such as NEC Table 310.16) applies to long continuous runs inside conduits or multiconductor cables where heat accumulation is restricted, requiring significantly lower current limits."
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
      <span>Wire Gauge Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">ASTM B258 &amp; IEC 60228 Standard Metrology</div>
          <h1 class="calc-title">Wire Gauge Calculator</h1>
          <p class="calc-tagline">Calculate American Wire Gauge (AWG) dimensions, circular mils, metric $mm^2$, DC line resistance, and allowable ampacity.</p>
        </header>

        <!-- Tool Card -->
        <div class="tool-card">
          <form id="gaugeForm" onsubmit="return false;">
            <div class="calc-grid">
              <div class="form-group">
                <label for="gaugeSelect" class="form-label">American Wire Gauge (AWG)</label>
                <select id="gaugeSelect" class="form-control" onchange="calculateGauge()">
                  <option value="-3">4/0 AWG (0000 AWG - Heavy Feeder)</option>
                  <option value="-2">3/0 AWG (000 AWG - 200A Service)</option>
                  <option value="-1">2/0 AWG (00 AWG - 175A Service)</option>
                  <option value="0">1/0 AWG (0 AWG - 150A Service)</option>
                  <option value="1">1 AWG (130A Sub-main)</option>
                  <option value="2">2 AWG (115A Sub-main)</option>
                  <option value="3">3 AWG (100A Service)</option>
                  <option value="4">4 AWG (85A Sub-panel)</option>
                  <option value="6">6 AWG (65A Range / EV / Hot Tub)</option>
                  <option value="8">8 AWG (50A Cooker / Central AC)</option>
                  <option value="10">10 AWG (30A Dryer / Water Heater)</option>
                  <option value="12" selected>12 AWG (20A Standard Receptacle)</option>
                  <option value="14">14 AWG (15A Standard Residential Lighting)</option>
                  <option value="16">16 AWG (10A Extension Cord / Alarm)</option>
                  <option value="18">18 AWG (7A Low Voltage / Thermostat)</option>
                  <option value="20">20 AWG (5A Electronic Interconnect)</option>
                  <option value="22">22 AWG (Hookup Wire / Telecommunications)</option>
                  <option value="24">24 AWG (Ethernet Cat5/6 / Data Cable)</option>
                  <option value="26">26 AWG (Patch Cords / Ribbon Cable)</option>
                  <option value="28">28 AWG (USB Data Lines)</option>
                  <option value="30">30 AWG (Wire Wrap / Micro-electronics)</option>
                </select>
                <small class="form-hint">Standard ASTM B258 wire size</small>
              </div>

              <div class="form-group">
                <label for="gaugeConductorMetal" class="form-label">Conductor Metallurgy</label>
                <select id="gaugeConductorMetal" class="form-control" onchange="calculateGauge()">
                  <option value="copper" selected>Electrolytic Copper (100% IACS)</option>
                  <option value="aluminum">Aluminum Alloy (61% IACS)</option>
                </select>
                <small class="form-hint">Conductor material resistivity</small>
              </div>

              <div class="form-group">
                <label for="wireLengthFt" class="form-label">Circuit Wire Length</label>
                <div class="input-with-unit">
                  <input type="number" id="wireLengthFt" class="form-control" value="100" min="1" step="10" oninput="calculateGauge()">
                  <span class="unit-badge">feet</span>
                </div>
                <small class="form-hint">One-way distance</small>
              </div>

              <div class="form-group">
                <label for="gaugeTestCurrent" class="form-label">Operating Load Current</label>
                <div class="input-with-unit">
                  <input type="number" id="gaugeTestCurrent" class="form-control" value="16" min="0.1" step="1" oninput="calculateGauge()">
                  <span class="unit-badge">Amps</span>
                </div>
                <small class="form-hint">For voltage drop calculation</small>
              </div>
            </div>

            <button type="button" id="calcGaugeBtn" class="btn btn-primary btn-block" onclick="calculateGauge()">Evaluate Wire Dimensions</button>
          </form>

          <div id="gaugeResultBox" class="results-container" style="margin-top:20px;">
            <h3>AWG Metrology &amp; Physical Properties</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label">Diameter (Inches &amp; mm)</span>
                <span id="gaugeDiameterOut" class="result-value">-- in (-- mm)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Cross-Sectional Area</span>
                <span id="gaugeAreaOut" class="result-value">-- mm² (-- cmil)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">DC Resistance per 1000 ft</span>
                <span id="gaugeResKftOut" class="result-value">-- &Omega;/kft</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Total Wire Resistance (for length)</span>
                <span id="gaugeTotalResOut" class="result-value">-- &Omega;</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Voltage Drop at Load Current</span>
                <span id="gaugeVdOut" class="result-value">-- Volts (2-wire)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">NEC 75°C Conduit Ampacity</span>
                <span id="gaugeAmpacityOut" class="result-value">-- A</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Engineering Principles: American Wire Gauge (AWG) Metrology</h2>
          
          <p>The <strong>American Wire Gauge (AWG)</strong> system, also historically known as the <em>Brown &amp; Sharpe (B&amp;S) wire gauge</em>, is the standardized logarithmic wire dimensioning scale utilized throughout North America and global electronics manufacturing. Standardized in 1857 by J.R. Brown, the AWG system provides a mathematically rigorous geometric progression defining the physical diameter, cross-sectional area, electrical resistance, and mass of solid non-ferrous round conductors.</p>

          <div class="formula-box">
            <h3>Mathematical Formulation of the AWG Scale (ASTM B258)</h3>
            <p>The AWG scale is anchored at two reference benchmark points:</p>
            <ul>
              <li><strong>#36 AWG:</strong> Defined exactly as $0.0050\text{ inches}$ ($5.0\text{ mils}$ or $0.127\text{ mm}$) in diameter.</li>
              <li><strong>#0000 (4/0) AWG:</strong> Defined exactly as $0.4600\text{ inches}$ ($460.0\text{ mils}$ or $11.684\text{ mm}$) in diameter.</li>
            </ul>
            <p>The gauge range spans exactly 39 intervening diameter steps between gauge #36 and gauge 4/0 (where 0 = 0, 2/0 = -1, 3/0 = -2, 4/0 = -3). The ratio between any two consecutive gauge diameters is constant:</p>
            <p>$$\text{Ratio } r = \sqrt[39]{\frac{0.4600}{0.0050}} = \sqrt[39]{92} \approx 1.1229322$$</p>
            <p>For any gauge number $n$, the conductor diameter in inches and millimeters is calculated from:</p>
            <p>$$d_n = 0.005 \times 92^{\frac{36 - n}{39}} \quad [\text{inches}]$$</p>
            <p>$$d_n = 0.127 \times 92^{\frac{36 - n}{39}} \quad [\text{millimeters}]$$</p>
          </div>

          <h3>Circular Mils and Cross-Sectional Area</h3>
          <p>In electrical engineering, wire area is expressed in both metric square millimeters ($\text{mm}^2$) and North American <strong>circular mils (cmil)</strong>. A circular mil represents the area of a circle having a diameter of one mil ($0.001\text{ inch}$):</p>
          <p>$$A_{cmil} = (d_{mils})^2 = (d_{inches} \times 1000)^2$$</p>
          <p>$$A_{mm^2} = \frac{\pi}{4} \cdot d_{mm}^2 = A_{cmil} \times 0.000506707$$</p>
          <p>For large conductors exceeding 4/0 AWG ($211{,}600\text{ cmil}$), gauge numbers are abandoned in favor of thousand circular mils (<strong>kcmil</strong> or <strong>MCM</strong>), such as 250 kcmil, 350 kcmil, and 500 kcmil.</p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>AWG Size</th>
                <th>Diameter (inches)</th>
                <th>Diameter (mm)</th>
                <th>Area (Circular Mils)</th>
                <th>Area (mm²)</th>
                <th>Copper DC Resistance at 20°C (Ω/kft)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>4/0 AWG</strong></td>
                <td>0.4600 in</td>
                <td>11.684 mm</td>
                <td>211,600 cmil</td>
                <td>107.2 mm²</td>
                <td>$0.0490\ \Omega/\text{kft}$</td>
              </tr>
              <tr>
                <td><strong>2/0 AWG</strong></td>
                <td>0.3648 in</td>
                <td>9.266 mm</td>
                <td>133,100 cmil</td>
                <td>67.43 mm²</td>
                <td>$0.0779\ \Omega/\text{kft}$</td>
              </tr>
              <tr>
                <td><strong>1/0 AWG</strong></td>
                <td>0.3249 in</td>
                <td>8.251 mm</td>
                <td>105,600 cmil</td>
                <td>53.49 mm²</td>
                <td>$0.0983\ \Omega/\text{kft}$</td>
              </tr>
              <tr>
                <td><strong>2 AWG</strong></td>
                <td>0.2576 in</td>
                <td>6.544 mm</td>
                <td>66,360 cmil</td>
                <td>33.62 mm²</td>
                <td>$0.1563\ \Omega/\text{kft}$</td>
              </tr>
              <tr>
                <td><strong>4 AWG</strong></td>
                <td>0.2043 in</td>
                <td>5.189 mm</td>
                <td>41,740 cmil</td>
                <td>21.15 mm²</td>
                <td>$0.2485\ \Omega/\text{kft}$</td>
              </tr>
              <tr>
                <td><strong>6 AWG</strong></td>
                <td>0.1620 in</td>
                <td>4.115 mm</td>
                <td>26,240 cmil</td>
                <td>13.30 mm²</td>
                <td>$0.3951\ \Omega/\text{kft}$</td>
              </tr>
              <tr>
                <td><strong>8 AWG</strong></td>
                <td>0.1285 in</td>
                <td>3.264 mm</td>
                <td>16,510 cmil</td>
                <td>8.367 mm²</td>
                <td>$0.6282\ \Omega/\text{kft}$</td>
              </tr>
              <tr>
                <td><strong>10 AWG</strong></td>
                <td>0.1019 in</td>
                <td>2.588 mm</td>
                <td>10,380 cmil</td>
                <td>5.261 mm²</td>
                <td>$0.9989\ \Omega/\text{kft}$</td>
              </tr>
              <tr>
                <td><strong>12 AWG</strong></td>
                <td>0.0808 in</td>
                <td>2.053 mm</td>
                <td>6,530 cmil</td>
                <td>3.309 mm²</td>
                <td>$1.588\ \Omega/\text{kft}$</td>
              </tr>
              <tr>
                <td><strong>14 AWG</strong></td>
                <td>0.0641 in</td>
                <td>1.628 mm</td>
                <td>4,110 cmil</td>
                <td>2.081 mm²</td>
                <td>$2.525\ \Omega/\text{kft}$</td>
              </tr>
            </tbody>
          </table>

          <div class="formula-box">
            <h3>Three Golden Rules of AWG Mental Arithmetic</h3>
            <p>Because the ratio $r \approx 1.1229322$, its mathematical powers yield practical mental approximations utilized by electrical engineers in the field:</p>
            <ul>
              <li><strong>The Rule of 3 (Halving Area / Doubling Resistance):</strong> Since $(1.12293)^3 \approx 1.414 \approx \sqrt{2}$, stepping up 3 gauge numbers (e.g. from #10 to #13 AWG) halves the cross-sectional area and <strong>doubles electrical resistance</strong> ($R_{n+3} \approx 2 \cdot R_n$). Conversely, dropping 3 gauge numbers doubles the copper volume.</li>
              <li><strong>The Rule of 6 (Doubling Diameter):</strong> Since $(1.12293)^6 \approx 2.005 \approx 2.0$, a change of 6 gauge numbers doubles or halves the wire diameter ($d_{n+6} \approx \frac{1}{2} d_n$).</li>
              <li><strong>The Rule of 10 (Decade Scaling):</strong> Since $(1.12293)^{10} \approx 3.162 \approx \sqrt{10}$, stepping up 10 gauge numbers divides the cross-sectional area by exactly 10 and <strong>multiplies line resistance by 10</strong>. For example, #20 AWG has approximately 10 times the resistance of #10 AWG ($10.15\ \Omega/\text{kft}$ vs $1.00\ \Omega/\text{kft}$).</li>
            </ul>
          </div>

          <div class="worked-example-card">
            <h3>Practical Worked Engineering Example: #12 AWG Branch Circuit Resistance &amp; Voltage Drop</h3>
            <p><strong>Design Scenario:</strong> An electrician installs a $120\text{V}$ single-phase residential 20A branch circuit utilizing #12 AWG solid copper wire ($n = 12$). The one-way run length to a kitchen microwave outlet is $100\text{ feet}$. Operating load current is $16\text{ Amperes}$ continuous. Determine the exact conductor cross-sectional area, round-trip resistance at $20^\circ\text{C}$, and line voltage drop.</p>

            <p><strong>Step 1: Calculate Geometric Diameter</strong></p>
            <p>$$d_{12} = 0.005 \times 92^{\frac{36 - 12}{39}} = 0.005 \times 92^{\frac{24}{39}} = 0.005 \times 92^{0.61538} = 0.005 \times 16.1618 = 0.0808\text{ inches}$$</p>
            <p>In millimeters: $0.0808 \times 25.4 = 2.053\text{ mm}$.</p>

            <p><strong>Step 2: Calculate Area in Circular Mils and mm²</strong></p>
            <p>$$A_{cmil} = (80.809\text{ mils})^2 = 6{,}530\text{ Circular Mils}$$</p>
            <p>$$A_{mm^2} = \frac{\pi}{4} \times (2.053\text{ mm})^2 = 3.309\text{ mm}^2$$</p>

            <p><strong>Step 3: Calculate Circuit Resistance for 100 ft (Two-Wire Loop)</strong></p>
            <p>Standard #12 AWG copper resistance per $1000\text{ ft}$ is $R_{kft} \approx 1.588\ \Omega/\text{kft}$.</p>
            <p>Total round-trip loop distance is $2 \times 100\text{ ft} = 200\text{ ft}$.</p>
            <p>$$R_{loop} = \frac{200\text{ ft}}{1000\text{ ft}} \times 1.588\ \Omega = 0.3176\ \Omega$$</p>

            <p><strong>Step 4: Calculate Voltage Drop</strong></p>
            <p>$$\Delta V = I \times R_{loop} = 16\text{ A} \times 0.3176\ \Omega = 5.08\text{ Volts}$$</p>
            <p>$$\Delta V\% = \frac{5.08\text{ V}}{120\text{ V}} \times 100 = 4.23\%$$</p>
            <p>Because $4.23\% > 3.0\%$ NEC recommended branch circuit drop, the engineer upsizes the run to <strong>#10 AWG</strong> ($R_{kft} = 0.999\ \Omega/\text{kft} \implies \Delta V = 3.20\text{V} = 2.66\%$).</p>
          </div>

          <h2>Frequently Asked Questions (Wire Gauge Metrology)</h2>
          <div class="faq-item">
            <h3>Why does gauge number decrease as wire diameter increases?</h3>
            <p>The AWG scale originated from historical wire drawing manufacturing processes. A metal wire was drawn through a series of successively smaller conical dies. A #1 AWG wire passed through a single drawing die; a #14 AWG wire was drawn through 14 progressive dies; a #36 AWG wire required 36 successive passes to draw it down to a thin strand. Thus, higher gauge numbers represent more drawing steps and thinner wires.</p>
          </div>

          <div class="faq-item">
            <h3>How does stranded wire differ from solid wire of the same AWG?</h3>
            <p>A stranded conductor of a given AWG (e.g. 7-strand or 19-strand #12 AWG) contains the exact same total metallic cross-sectional copper area as a solid #12 AWG wire. However, because round strands do not pack with 100% density (leaving microscopic air gaps between strands), the overall outer diameter of stranded wire is approximately $5\%$ to $10\%$ larger than solid wire.</p>
          </div>

          <div class="faq-item">
            <h3>What is the difference between AWG and the SWG (Standard Wire Gauge)?</h3>
            <p>AWG (American Wire Gauge) is defined mathematically by a continuous logarithmic equation ($r = \sqrt[39]{92}$). The British Standard Wire Gauge (SWG / Imperial Standard Wire Gauge), established in 1883, is a discrete empirical scale based on Birmingham wire tables. SWG diameters differ by several mils from AWG for identical gauge numbers (e.g. #14 SWG is 0.080 in / 2.03 mm, whereas #14 AWG is 0.064 in / 1.63 mm).</p>
          </div>

          <div class="faq-item">
            <h3>How does skin effect alter resistance in high-frequency wire applications?</h3>
            <p>At radio frequencies, alternating magnetic flux forces current to flow only along the conductor surface (skin depth $\delta = \sqrt{\rho / (\pi f \mu)}$). At 1 MHz in copper, the skin depth is only $0.066\text{ mm}$ ($2.6\text{ mils}$). Thick solid wire becomes highly inefficient because the center core carries zero current. High-frequency RF circuits therefore employ stranded <em>Litz wire</em> composed of individually insulated thin strands twisted in woven patterns.</p>
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
    // Standard NEC 75C Ampacities for AWG
    const awgAmpacities75 = {
      "-3": 260, "-2": 225, "-1": 195, "0": 170,
      "1": 145, "2": 130, "3": 115, "4": 95,
      "6": 75, "8": 55, "10": 40, "12": 30,
      "14": 25, "16": 18, "18": 14, "20": 11,
      "22": 7, "24": 3.5, "26": 2.2, "28": 1.4, "30": 0.86
    };

    function calculateGauge() {
      const n = parseInt(document.getElementById("gaugeSelect").value);
      const metal = document.getElementById("gaugeConductorMetal").value;
      const lengthFt = parseFloat(document.getElementById("wireLengthFt").value) || 100;
      const current = parseFloat(document.getElementById("gaugeTestCurrent").value) || 10;

      // ASTM B258 diameter equation
      // d = 0.005 * 92^((36 - n) / 39) inches
      const dInches = 0.005 * Math.pow(92, (36 - n) / 39);
      const dMm = dInches * 25.4;
      const dMils = dInches * 1000;

      // Area
      const areaCmil = dMils * dMils;
      const areaMm2 = (Math.PI / 4) * dMm * dMm;

      // DC Resistance per 1000 ft at 20C
      // Copper: rho = 10.371 Ohms * cmil / ft
      // Aluminum: rho = 17.0 Ohms * cmil / ft
      const rhoCmilFt = (metal === "aluminum") ? 17.0 : 10.371;
      const rPerKft = (rhoCmilFt * 1000) / areaCmil;

      // Total loop resistance for lengthFt (2-wire circuit)
      const rSingleWire = (rPerKft * lengthFt) / 1000;
      const rLoop = 2 * rSingleWire;
      const deltaV = current * rLoop;

      // Ampacity
      const ampacity = awgAmpacities75[n.toString()] || 15;
      const alAmpacity = (metal === "aluminum") ? (ampacity * 0.78) : ampacity;

      document.getElementById("gaugeDiameterOut").innerText = dInches.toFixed(4) + " in (" + dMm.toFixed(3) + " mm)";
      document.getElementById("gaugeAreaOut").innerText = areaMm2.toFixed(3) + " mm² (" + Math.round(areaCmil).toLocaleString() + " cmil)";
      document.getElementById("gaugeResKftOut").innerText = rPerKft.toFixed(4) + " \u03A9/kft";
      document.getElementById("gaugeTotalResOut").innerText = rSingleWire.toFixed(4) + " \u03A9 (Single) / " + rLoop.toFixed(4) + " \u03A9 (Loop)";
      document.getElementById("gaugeVdOut").innerText = deltaV.toFixed(2) + " V (2-wire drop)";
      document.getElementById("gaugeAmpacityOut").innerText = Math.round(alAmpacity) + " A (75°C Conductor Rating)";
    }

    document.addEventListener("DOMContentLoaded", function() {
      calculateGauge();
    });
  </script>
</body>
</html>
"""

def main():
    root = r"C:\Users\Admin\.gemini\antigravity\scratch\calchub"
    
    p5 = os.path.join(root, "three-phase-cable-sizing-calculator.html")
    with open(p5, "w", encoding="utf-8") as f:
        f.write(TOOL_5_HTML.strip() + "\n")
    print("[PASS] three-phase-cable-sizing-calculator.html generated successfully!")

    p6 = os.path.join(root, "wire-gauge-calculator.html")
    with open(p6, "w", encoding="utf-8") as f:
        f.write(TOOL_6_HTML.strip() + "\n")
    print("[PASS] wire-gauge-calculator.html generated successfully!")

if __name__ == "__main__":
    main()
