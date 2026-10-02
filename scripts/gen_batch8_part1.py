# -*- coding: utf-8 -*-
"""
Script to generate Batch 8 Part 1 tools:
1. earthing-cable-size-calculator.html
2. kw-to-cable-size-calculator.html
"""
import os

TOOL_1_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Earthing Cable Size Calculator | Grounding Conductor Adiabatic Sizing</title>
  <meta name="description" content="Calculate electrical earthing cable sizes (circuit protective conductor CPC and grounding electrode conductor GEC) compliant with IEC 60364-5-54, BS 7671, and NEC Table 250.66/250.122.">
  <link rel="canonical" href="https://calchub.cloud/earthing-cable-size-calculator.html">
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
        "name": "Earthing Cable Size Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Professional grounding and earthing cable sizing engine calculating minimum adiabatic cross-sectional area per IEC 60364-5-54 and code minimums per BS 7671 and NEC.",
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
            "name": "What is the adiabatic equation for sizing earthing conductors?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The adiabatic equation S = sqrt(I^2 * t) / k (codified in IEC 60364-5-54 and BS 7671 Regulation 543.1.3) calculates the minimum cross-sectional area S (mm²) of a protective conductor required to survive short-circuit ground fault currents without exceeding thermal limits of its insulation. I is prospective RMS fault current, t is fault clearance time in seconds, and k is the thermodynamic material constant."
            }
          },
          {
            "@type": "Question",
            "name": "What are the standard k-factors for copper, aluminum, and steel earthing conductors?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Per IEC 60364-5-54: Copper with 70°C PVC insulation has k = 115 (or k = 143 for 90°C XLPE; k = 176 for bare copper in free air). Aluminum with PVC insulation has k = 76 (or k = 94 for XLPE; k = 116 for bare aluminum). Galvanized steel conductors have k = 46 to 58 depending on insulation type."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between a CPC and a Grounding Electrode Conductor (GEC)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A Circuit Protective Conductor (CPC, or Equipment Grounding Conductor EGC) runs alongside circuit phase and neutral conductors to bond exposed metal frames back to the distribution board to trip protective devices during ground faults. A Grounding Electrode Conductor (GEC) connects the main earthing terminal (MET) or service panel neutral bus directly to earth ground electrodes (earth rods, foundation rebar, buried grounding mesh)."
            }
          },
          {
            "@type": "Question",
            "name": "When can table selection (BS 7671 Table 54.7) be used instead of the adiabatic equation?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Table 54.7 provides conservative prescriptive sizing based on phase conductor size: if phase S <= 16 mm², earthing conductor S_e = S; if 16 mm² < S <= 35 mm², S_e = 16 mm²; if S > 35 mm², S_e = S / 2. While simple, the adiabatic equation often permits significantly smaller, fully compliant earthing conductors when protective devices operate rapidly (under 0.4 seconds)."
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
      <span>Earthing Cable Size Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">IEC 60364-5-54 &amp; BS 7671 Regulation 543</div>
          <h1 class="calc-title">Earthing Cable Size Calculator</h1>
          <p class="calc-tagline">Calculate protective earthing conductor cross-section (CPC, GEC, and bonding conductors) using the adiabatic equation and international code tables.</p>
        </header>

        <!-- Tool Card -->
        <div class="tool-card">
          <form id="earthForm" onsubmit="return false;">
            <div class="calc-grid">
              <div class="form-group">
                <label for="earthConductorMetal" class="form-label">Earthing Conductor Metal</label>
                <select id="earthConductorMetal" class="form-control" onchange="calculateEarthCable()">
                  <option value="copper" selected>Electrolytic Copper (Cu)</option>
                  <option value="aluminum">Electrical Grade Aluminum (Al)</option>
                  <option value="steel">Galvanized Structural Steel (Fe)</option>
                </select>
                <small class="form-hint">Metallurgy of protective conductor</small>
              </div>

              <div class="form-group">
                <label for="earthInsulation" class="form-label">Conductor Enclosure &amp; Insulation</label>
                <select id="earthInsulation" class="form-control" onchange="calculateEarthCable()">
                  <option value="pvc" selected>PVC Insulated (70°C Continuous / 160°C Fault)</option>
                  <option value="xlpe">XLPE / EPR Insulated (90°C Continuous / 250°C Fault)</option>
                  <option value="bare_cable">Bare Conductor Bundled in Multicore Cable</option>
                  <option value="bare_free">Bare Conductor in Free Air / Ground</option>
                </select>
                <small class="form-hint">Governs thermodynamic factor k</small>
              </div>

              <div class="form-group">
                <label for="faultCurrentKa" class="form-label">Prospective Earth Fault Current ($I_f$)</label>
                <div class="input-with-unit">
                  <input type="number" id="faultCurrentKa" class="form-control" value="6.5" min="0.1" max="100" step="0.5" oninput="calculateEarthCable()">
                  <span class="unit-badge">kA</span>
                </div>
                <small class="form-hint">Symmetrical phase-to-earth fault current</small>
              </div>

              <div class="form-group">
                <label for="disconnectionTime" class="form-label">Disconnection Time ($t$)</label>
                <div class="input-with-unit">
                  <input type="number" id="disconnectionTime" class="form-control" value="0.1" min="0.01" max="5.0" step="0.02" oninput="calculateEarthCable()">
                  <span class="unit-badge">sec</span>
                </div>
                <small class="form-hint">Breaker / fuse clearance speed (e.g. 0.1s for MCB)</small>
              </div>

              <div class="form-group">
                <label for="phaseConductorSize" class="form-label">Associated Phase Conductor Size</label>
                <select id="phaseConductorSize" class="form-control" onchange="calculateEarthCable()">
                  <option value="1.5">1.5 mm²</option>
                  <option value="2.5">2.5 mm²</option>
                  <option value="4.0">4.0 mm²</option>
                  <option value="6.0">6.0 mm²</option>
                  <option value="10.0">10 mm²</option>
                  <option value="16.0">16 mm²</option>
                  <option value="25.0">25 mm²</option>
                  <option value="35.0" selected>35 mm²</option>
                  <option value="50.0">50 mm²</option>
                  <option value="70.0">70 mm²</option>
                  <option value="95.0">95 mm²</option>
                  <option value="120.0">120 mm²</option>
                  <option value="150.0">150 mm²</option>
                  <option value="185.0">185 mm²</option>
                  <option value="240.0">240 mm²</option>
                </select>
                <small class="form-hint">For BS 7671 Table 54.7 comparison</small>
              </div>

              <div class="form-group">
                <label for="circuitBreakerRating" class="form-label">Upstream Protective Device ($I_n$)</label>
                <div class="input-with-unit">
                  <input type="number" id="circuitBreakerRating" class="form-control" value="100" min="6" max="2500" step="10" oninput="calculateEarthCable()">
                  <span class="unit-badge">Amps</span>
                </div>
                <small class="form-hint">For NEC Table 250.122 cross-check</small>
              </div>
            </div>

            <button type="button" id="calcEarthBtn" class="btn btn-primary btn-block" onclick="calculateEarthCable()">Dimension Earthing Conductor</button>
          </form>

          <div id="earthResultBox" class="results-container" style="margin-top:20px;">
            <h3>Earthing Conductor Dimensioning Output</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label">Recommended Earthing Cable Size</span>
                <span id="earthSizeOut" class="result-value">-- mm²</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Minimum Adiabatic Cross-Section ($S_{ad}$)</span>
                <span id="adiabaticOut" class="result-value">-- mm²</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Thermodynamic Material Factor ($k$)</span>
                <span id="kFactorOut" class="result-value">--</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Table 54.7 Prescriptive Size ($S_e$)</span>
                <span id="tableSizeOut" class="result-value">-- mm²</span>
              </div>
              <div class="result-tile">
                <span class="result-label">NEC Table 250.122 Minimum (EGC)</span>
                <span id="necSizeOut" class="result-value">-- AWG</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Thermal Short-Circuit Feasibility</span>
                <span id="earthStatusOut" class="result-value">--</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Engineering Analysis: Earthing &amp; Grounding Conductor Sizing</h2>
          
          <p>The electrical earthing (or grounding) system is the most critical life-safety element of any electrical installation. In low-voltage power networks, earthing conductors fulfill two non-negotiable functions: (1) ensuring rapid automatic disconnection of supply (ADS) by providing a low-impedance return path for phase-to-earth fault currents, and (2) clamping touch and step voltages ($U_t$) on exposed metallic enclosures to safe levels ($< 50\text{V AC}$ per IEC 60364-4-41) to prevent fatal electrocution.</p>

          <p>Dimensioning earthing conductors&mdash;whether circuit protective conductors (CPC), main equipotential bonding conductors, or grounding electrode conductors (GEC)&mdash;is governed by international codes including <strong>IEC 60364-5-54 (Selection and erection of electrical equipment &mdash; Earthing arrangements and protective conductors)</strong>, the UK <strong>BS 7671 (IET Wiring Regulations Regulation 543)</strong>, and the US <strong>NFPA 70 National Electrical Code (NEC Article 250)</strong>.</p>

          <div class="formula-box">
            <h3>The Fundamental Adiabatic Thermal Equation: IEC 60364-5-54</h3>
            <p>During an earth fault, the short-circuit current ($I_f$) dissipates immense joule heat into the protective conductor. Because protective overcurrent devices (circuit breakers, MCCBs, and fuses) clear faults rapidly (typically between $0.02\text{ to } 0.4\text{ seconds}$, and strictly under $5\text{ seconds}$), zero heat escapes into the surrounding ambient air or conduit walls. The process is strictly <strong>adiabatic</strong>.</p>
            <p>Under IEC 60364-5-54 Clause 543.1.2 and BS 7671 Regulation 543.1.3, the minimum cross-sectional area $S$ of a protective conductor is calculated from:</p>
            <p>$$S = \frac{\sqrt{I_f^2 \cdot t}}{k} = \frac{I_f \sqrt{t}}{k}$$</p>
            <p>Where:</p>
            <ul>
              <li>$S$ = Minimum cross-sectional area of the earthing conductor in square millimeters ($\text{mm}^2$).</li>
              <li>$I_f$ = Prospective root-mean-square (RMS) phase-to-earth fault current passing through the protective device in Amperes ($\text{A}$).</li>
              <li>$t$ = Operating disconnect time of the protective device in seconds ($\text{s}$).</li>
              <li>$k$ = Thermodynamic material constant taking into account electrical resistivity, temperature coefficient of resistance, volumetric heat capacity, and permissible initial and final temperatures of the conductor material and its insulation.</li>
            </ul>
          </div>

          <h3>Thermodynamic $k$-Factor Values for Common Conductors</h3>
          <p>The material constant $k$ is derived from the thermodynamic physical properties of the conductor metal and the thermal boundary limits of its insulation matrix:</p>
          <p>$$k = \sqrt{\frac{Q_c \cdot (\beta + 20)}{\rho_{20}} \ln\left(\frac{\beta + \theta_f}{\beta + \theta_i}\right)}$$</p>
          <p>Where $Q_c$ is volumetric heat capacity, $\beta$ is reciprocal of temperature coefficient at $0^\circ\text{C}$ ($234.5$ for copper, $228$ for aluminum, $202$ for steel), $\rho_{20}$ is electrical resistivity at $20^\circ\text{C}$, $\theta_i$ is initial operating temperature, and $\theta_f$ is maximum permissible short-circuit final temperature.</p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Conductor Material</th>
                <th>Insulation Type</th>
                <th>Initial Temp ($\theta_i$)</th>
                <th>Final Fault Temp ($\theta_f$)</th>
                <th>$k$-Factor (IEC 60364-5-54)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Copper (Cu)</strong></td>
                <td>70°C PVC Insulated</td>
                <td>$70^\circ\text{C}$</td>
                <td>$160^\circ\text{C}$</td>
                <td><strong>$k = 115$</strong></td>
              </tr>
              <tr>
                <td><strong>Copper (Cu)</strong></td>
                <td>90°C XLPE / EPR Insulated</td>
                <td>$90^\circ\text{C}$</td>
                <td>$250^\circ\text{C}$</td>
                <td><strong>$k = 143$</strong></td>
              </tr>
              <tr>
                <td><strong>Copper (Cu)</strong></td>
                <td>Bare (Bundled in Cable)</td>
                <td>$70^\circ\text{C}$</td>
                <td>$160^\circ\text{C}$</td>
                <td><strong>$k = 143$</strong></td>
              </tr>
              <tr>
                <td><strong>Copper (Cu)</strong></td>
                <td>Bare in Free Air / Trench</td>
                <td>$30^\circ\text{C}$</td>
                <td>$200^\circ\text{C}$</td>
                <td><strong>$k = 176$</strong></td>
              </tr>
              <tr>
                <td><strong>Aluminum (Al)</strong></td>
                <td>70°C PVC Insulated</td>
                <td>$70^\circ\text{C}$</td>
                <td>$160^\circ\text{C}$</td>
                <td><strong>$k = 76$</strong></td>
              </tr>
              <tr>
                <td><strong>Aluminum (Al)</strong></td>
                <td>90°C XLPE / EPR Insulated</td>
                <td>$90^\circ\text{C}$</td>
                <td>$250^\circ\text{C}$</td>
                <td><strong>$k = 94$</strong></td>
              </tr>
              <tr>
                <td><strong>Aluminum (Al)</strong></td>
                <td>Bare in Free Air</td>
                <td>$30^\circ\text{C}$</td>
                <td>$200^\circ\text{C}$</td>
                <td><strong>$k = 116$</strong></td>
              </tr>
              <tr>
                <td><strong>Galvanized Steel</strong></td>
                <td>Steel Wire Armour (SWA)</td>
                <td>$60^\circ\text{C}$</td>
                <td>$160^\circ\text{C}$</td>
                <td><strong>$k = 51$</strong></td>
              </tr>
              <tr>
                <td><strong>Galvanized Steel</strong></td>
                <td>Bare Earth Tape / Rod</td>
                <td>$30^\circ\text{C}$</td>
                <td>$200^\circ\text{C}$</td>
                <td><strong>$k = 58$</strong></td>
              </tr>
            </tbody>
          </table>

          <div class="formula-box">
            <h3>Prescriptive Sizing: BS 7671 Table 54.7 &amp; NEC Table 250.122</h3>
            <p>If prospective fault current and clearance times are not calculated mathematically, national codes permit prescriptive rule-of-thumb sizing based on associated phase conductors:</p>
            <p><strong>BS 7671 Table 54.7 Method (When phase and earth metals are identical):</strong></p>
            <ul>
              <li>If $S_{phase} \le 16\text{ mm}^2 \implies S_{earth} = S_{phase}$</li>
              <li>If $16\text{ mm}^2 < S_{phase} \le 35\text{ mm}^2 \implies S_{earth} = 16\text{ mm}^2$</li>
              <li>If $S_{phase} > 35\text{ mm}^2 \implies S_{earth} = \frac{S_{phase}}{2}$</li>
            </ul>
            <p><strong>NEC Table 250.122 (Equipment Grounding Conductor based on Breaker Rating):</strong></p>
            <ul>
              <li>15A Breaker $\implies$ #14 AWG Copper ($2.08\text{ mm}^2$)</li>
              <li>20A Breaker $\implies$ #12 AWG Copper ($3.31\text{ mm}^2$)</li>
              <li>30A Breaker $\implies$ #10 AWG Copper ($5.26\text{ mm}^2$)</li>
              <li>60A Breaker $\implies$ #10 AWG Copper ($5.26\text{ mm}^2$)</li>
              <li>100A Breaker $\implies$ #8 AWG Copper ($8.37\text{ mm}^2$)</li>
              <li>200A Breaker $\implies$ #6 AWG Copper ($13.3\text{ mm}^2$)</li>
              <li>400A Breaker $\implies$ #3 AWG Copper ($26.7\text{ mm}^2$)</li>
              <li>600A Breaker $\implies$ #1 AWG Copper ($42.4\text{ mm}^2$)</li>
            </ul>
          </div>

          <div class="worked-example-card">
            <h3>Practical Worked Engineering Example: Industrial Sub-Distribution Feeder Earthing</h3>
            <p><strong>Design Scenario:</strong> Size the Circuit Protective Conductor (CPC) for a three-phase distribution subpanel fed from a main switchboard. Phase conductors are $35\text{ mm}^2$ copper. The circuit is protected by a $100\text{ A}$ Type C MCB. Symmetrical earth fault calculation indicates a prospective earth fault current $I_f = 6{,}500\text{ A}$ ($6.5\text{ kA}$). The MCB's instantaneous electromagnetic magnetic trip clears the fault within $t = 0.08\text{ seconds}$. The earthing conductor selected is a single-core copper cable with $70^\circ\text{C}$ PVC insulation ($k = 115$).</p>

            <p><strong>Step 1: Calculate Minimum Cross-Section via Adiabatic Equation</strong></p>
            <p>$$S = \frac{I_f \sqrt{t}}{k} = \frac{6500 \times \sqrt{0.08}}{115} = \frac{6500 \times 0.2828}{115} = \frac{1838.48}{115} = 15.99\text{ mm}^2$$</p>
            <p>The calculated adiabatic minimum is $15.99\text{ mm}^2$. The next standard commercial cable size is <strong>$16\text{ mm}^2$</strong>.</p>

            <p><strong>Step 2: Compare with BS 7671 Table 54.7 Prescriptive Sizing</strong></p>
            <p>For $S_{phase} = 35\text{ mm}^2$, Table 54.7 specifies:</p>
            <p>$$S_{earth} = 16\text{ mm}^2$$</p>
            <p>The adiabatic calculation and Table 54.7 converge on the exact same size ($16\text{ mm}^2$).</p>

            <p><strong>Step 3: Verification of Thermal Feasibility &amp; Let-Through Energy ($I^2 t$)</strong></p>
            <p>Fault energy let-through: $I^2 t = (6500)^2 \times 0.08 = 3{,}380{,}000\text{ A}^2\text{s}$.</p>
            <p>Maximum thermal withstand of $16\text{ mm}^2$ copper PVC:</p>
            <p>$$k^2 S^2 = (115)^2 \times (16)^2 = 13{,}225 \times 256 = 3{,}385{,}600\text{ A}^2\text{s}$$</p>
            <p>Since $k^2 S^2 (3{,}385{,}600) \ge I^2 t (3{,}380{,}000)$, the $16\text{ mm}^2$ copper conductor will safely absorb the fault energy without exceeding $160^\circ\text{C}$.</p>
          </div>

          <h2>Frequently Asked Questions (Earthing Cable Sizing)</h2>
          <div class="faq-item">
            <h3>Can the steel wire armour (SWA) of a cable be used as the sole earthing conductor?</h3>
            <p>Yes, provided the cross-sectional area of the steel wire armour satisfies the adiabatic equation $S \ge \frac{\sqrt{I^2 t}}{k}$ with $k = 51$ for steel armour. Because steel has higher electrical resistivity than copper, SWA must have roughly twice the cross-sectional area of a copper CPC to provide equivalent fault-handling capacity. Most modern 3-core and 4-core XLPE SWA cables up to $95\text{ mm}^2$ easily qualify.</p>
          </div>

          <div class="faq-item">
            <h3>What is the minimum size for a main equipotential bonding conductor?</h3>
            <p>Under BS 7671 Regulation 544.1.1, main bonding conductors connecting incoming metal gas, water, and structural steel services to the Main Earthing Terminal (MET) must not be less than half the required cross-sectional area of the earthing conductor of the installation, with a minimum of $6\text{ mm}^2$ and need not exceed $25\text{ mm}^2$ for copper.</p>
          </div>

          <div class="faq-item">
            <h3>Why does aluminum have lower k-factor than copper?</h3>
            <p>Electrical grade aluminum has a lower volumetric heat capacity ($Q_c \approx 2.42 \times 10^6\text{ J}/(\text{m}^3\cdot\text{K})$ vs $3.42 \times 10^6$ for copper) and higher electrical resistivity ($\rho \approx 2.82 \times 10^{-8}\ \Omega\cdot\text{m}$ vs $1.72 \times 10^{-8}$ for copper). Consequently, aluminum heats up significantly faster during short-circuit faults, yielding lower $k$-factors ($76$ vs $115$ for PVC) and requiring larger cross-sections.</p>
          </div>

          <div class="faq-item">
            <h3>Does the adiabatic equation apply to long-duration earth faults (> 5 seconds)?</h3>
            <p>No. If the protective device takes longer than 5 seconds to clear an earth fault (such as on high-impedance TT systems without RCD protection), heat begins conducting out through the insulation into the surrounding medium. In such cases, non-adiabatic continuous thermal equilibrium equations or standard table selections must be employed.</p>
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
    const standardMetricEarthSizes = [1.5, 2.5, 4.0, 6.0, 10.0, 16.0, 25.0, 35.0, 50.0, 70.0, 95.0, 120.0, 150.0, 185.0, 240.0];

    // k-factor matrix per IEC 60364-5-54
    const kMatrix = {
      "copper": { "pvc": 115, "xlpe": 143, "bare_cable": 143, "bare_free": 176 },
      "aluminum": { "pvc": 76, "xlpe": 94, "bare_cable": 94, "bare_free": 116 },
      "steel": { "pvc": 46, "xlpe": 54, "bare_cable": 51, "bare_free": 58 }
    };

    function calculateEarthCable() {
      const metal = document.getElementById("earthConductorMetal").value;
      const insulation = document.getElementById("earthInsulation").value;
      const faultKa = parseFloat(document.getElementById("faultCurrentKa").value) || 1;
      const faultTime = parseFloat(document.getElementById("disconnectionTime").value) || 0.1;
      const phaseSize = parseFloat(document.getElementById("phaseConductorSize").value) || 16;
      const breakerRating = parseFloat(document.getElementById("circuitBreakerRating").value) || 100;

      const faultAmps = faultKa * 1000;
      const k = kMatrix[metal][insulation] || 115;

      // Adiabatic calculation S = (I * sqrt(t)) / k
      const sAdiabatic = (faultAmps * Math.sqrt(faultTime)) / k;

      // Table 54.7 Prescriptive Sizing
      let sTable = 16.0;
      if (phaseSize <= 16.0) {
        sTable = phaseSize;
      } else if (phaseSize <= 35.0) {
        sTable = 16.0;
      } else {
        sTable = phaseSize / 2;
      }

      // NEC 250.122 Minimum estimation
      let necAwg = "#14 AWG";
      if (breakerRating > 15 && breakerRating <= 20) necAwg = "#12 AWG (3.3 mm²)";
      else if (breakerRating > 20 && breakerRating <= 60) necAwg = "#10 AWG (5.3 mm²)";
      else if (breakerRating > 60 && breakerRating <= 100) necAwg = "#8 AWG (8.4 mm²)";
      else if (breakerRating > 100 && breakerRating <= 200) necAwg = "#6 AWG (13.3 mm²)";
      else if (breakerRating > 200 && breakerRating <= 300) necAwg = "#4 AWG (21.2 mm²)";
      else if (breakerRating > 300 && breakerRating <= 400) necAwg = "#3 AWG (26.7 mm²)";
      else if (breakerRating > 400 && breakerRating <= 500) necAwg = "#2 AWG (33.6 mm²)";
      else if (breakerRating > 500 && breakerRating <= 600) necAwg = "#1 AWG (42.4 mm²)";
      else if (breakerRating > 600) necAwg = "#1/0 to #4/0 AWG";

      // Select standard size >= sAdiabatic
      let recommendedSize = null;
      for (let i = 0; i < standardMetricEarthSizes.length; i++) {
        if (standardMetricEarthSizes[i] >= sAdiabatic) {
          recommendedSize = standardMetricEarthSizes[i];
          break;
        }
      }

      document.getElementById("adiabaticOut").innerText = sAdiabatic.toFixed(2) + " mm²";
      document.getElementById("kFactorOut").innerText = k + " A·s^(1/2)/mm²";
      document.getElementById("tableSizeOut").innerText = sTable + " mm²";
      document.getElementById("necSizeOut").innerText = necAwg;

      const statusEl = document.getElementById("earthStatusOut");

      if (recommendedSize) {
        document.getElementById("earthSizeOut").innerText = recommendedSize + " mm² " + metal.toUpperCase();
        statusEl.innerText = "Feasible: Conductor Withstands Fault Energy Let-Through (I²t)";
        statusEl.style.color = "#10b981";
      } else {
        document.getElementById("earthSizeOut").innerText = "> 240 mm² (Parallel Conductors Req.)";
        statusEl.innerText = "Exceeds standard single conductor thermal limit; check protective clearance speed";
        statusEl.style.color = "#ef4444";
      }
    }

    document.addEventListener("DOMContentLoaded", function() {
      calculateEarthCable();
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
  <title>kW to Cable Size Calculator | Kilowatt Load to Electrical Wire Sizing</title>
  <meta name="description" content="Convert electrical kilowatts (kW) into exact low-voltage cable sizes. Computes full-load amps, 3-phase and 1-phase voltage drop, power factor, and thermal derating.">
  <link rel="canonical" href="https://calchub.cloud/kw-to-cable-size-calculator.html">
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
        "name": "kW to Cable Size Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Convert kilowatt (kW) connected load to exact electrical cable size and copper cross-section for single-phase and three-phase systems.",
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
            "name": "How is electrical load current calculated from kilowatts (kW)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For a three-phase system: I = (P_kW * 1000) / (sqrt(3) * V_LL * cos(theta) * eta), where V_LL is line-to-line voltage, cos(theta) is power factor, and eta is motor efficiency. For a single-phase system: I = (P_kW * 1000) / (V_LN * cos(theta) * eta)."
            }
          },
          {
            "@type": "Question",
            "name": "Why must motor efficiency and power factor be included when sizing cable from kW?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Motor nameplates specify mechanical shaft power in kW, not electrical input power. Because motors have internal electrical and magnetic losses (efficiency eta approx 85% to 95%) and draw reactive magnetizing current (power factor cos(theta) approx 0.80 to 0.88), the actual electrical line current is significantly higher than a pure resistive kW calculation would indicate."
            }
          },
          {
            "@type": "Question",
            "name": "What is the continuous load safety factor for kW cable sizing?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Under NEC 210.19 and IEC 60364-5-52, continuous loads (operating for 3 hours or more) require protective devices and conductors to be sized for 125% of the calculated full-load current (I_design = 1.25 * I_FLA)."
            }
          },
          {
            "@type": "Question",
            "name": "How does cable length impact kW-to-cable sizing?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Even if a conductor meets thermal current capacity for a given kW rating, long distances introduce electrical resistance that causes voltage drop. International standards recommend limiting voltage drop to 3% for lighting and 4% to 5% for general motor/power loads, which frequently requires upsizing the conductor beyond its thermal rating."
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
      <span>kW to Cable Size Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">IEC 60364 &amp; NEC Standard Conversion</div>
          <h1 class="calc-title">kW to Cable Size Calculator</h1>
          <p class="calc-tagline">Convert electrical kilowatt (kW) ratings into exact conductor cross-sections ($mm^2$ &amp; AWG) with voltage drop and thermal derating.</p>
        </header>

        <!-- Tool Card -->
        <div class="tool-card">
          <form id="kwForm" onsubmit="return false;">
            <div class="calc-grid">
              <div class="form-group">
                <label for="powerKw" class="form-label">Connected Active Power ($P$)</label>
                <div class="input-with-unit">
                  <input type="number" id="powerKw" class="form-control" value="30" min="0.1" step="1" oninput="calculateKwCable()">
                  <span class="unit-badge">kW</span>
                </div>
                <small class="form-hint">Load rating in kilowatts</small>
              </div>

              <div class="form-group">
                <label for="kwSupplySystem" class="form-label">Supply Voltage &amp; Phase</label>
                <select id="kwSupplySystem" class="form-control" onchange="calculateKwCable()">
                  <option value="400_3p" selected>Three-Phase 400V AC (50/60 Hz)</option>
                  <option value="230_1p">Single-Phase 230V AC (50/60 Hz)</option>
                  <option value="480_3p">Three-Phase 480V AC (North American)</option>
                  <option value="208_3p">Three-Phase 208V AC</option>
                  <option value="120_1p">Single-Phase 120V AC</option>
                </select>
                <small class="form-hint">Operating system voltage</small>
              </div>

              <div class="form-group">
                <label for="kwPowerFactor" class="form-label">Power Factor ($\cos\varphi$)</label>
                <div class="input-with-unit">
                  <input type="number" id="kwPowerFactor" class="form-control" value="0.85" min="0.5" max="1.0" step="0.05" oninput="calculateKwCable()">
                  <span class="unit-badge">$\cos\varphi$</span>
                </div>
                <small class="form-hint">1.0 for resistive; 0.8–0.88 for induction motors</small>
              </div>

              <div class="form-group">
                <label for="kwEfficiency" class="form-label">Equipment Efficiency ($\eta$)</label>
                <div class="input-with-unit">
                  <input type="number" id="kwEfficiency" class="form-control" value="90" min="50" max="100" step="1" oninput="calculateKwCable()">
                  <span class="unit-badge">%</span>
                </div>
                <small class="form-hint">100% for heaters; 88%–94% for industrial motors</small>
              </div>

              <div class="form-group">
                <label for="kwConductorMetal" class="form-label">Conductor Metal</label>
                <select id="kwConductorMetal" class="form-control" onchange="calculateKwCable()">
                  <option value="copper" selected>Annealed Copper (Cu)</option>
                  <option value="aluminum">Electrical Aluminum (Al)</option>
                </select>
                <small class="form-hint">Cable core material</small>
              </div>

              <div class="form-group">
                <label for="kwInsulation" class="form-label">Cable Insulation</label>
                <select id="kwInsulation" class="form-control" onchange="calculateKwCable()">
                  <option value="xlpe" selected>XLPE / 90°C Thermosetting</option>
                  <option value="pvc">PVC / 70°C Thermoplastic</option>
                </select>
                <small class="form-hint">Maximum conductor core temperature</small>
              </div>

              <div class="form-group">
                <label for="kwRouteLength" class="form-label">One-Way Run Length ($L$)</label>
                <div class="input-with-unit">
                  <input type="number" id="kwRouteLength" class="form-control" value="50" min="1" step="5" oninput="calculateKwCable()">
                  <span class="unit-badge">metres</span>
                </div>
                <small class="form-hint">Distance from switchboard to load</small>
              </div>

              <div class="form-group">
                <label for="kwAmbientTemp" class="form-label">Ambient Temperature</label>
                <div class="input-with-unit">
                  <input type="number" id="kwAmbientTemp" class="form-control" value="35" min="10" max="65" step="1" oninput="calculateKwCable()">
                  <span class="unit-badge">°C</span>
                </div>
                <small class="form-hint">Baseline is 30°C in air</small>
              </div>

              <div class="form-group">
                <label for="kwMaxVd" class="form-label">Max Allowable Voltage Drop</label>
                <div class="input-with-unit">
                  <input type="number" id="kwMaxVd" class="form-control" value="4.0" min="1.0" max="10.0" step="0.5" oninput="calculateKwCable()">
                  <span class="unit-badge">%</span>
                </div>
                <small class="form-hint">Standard threshold (typically 3%–5%)</small>
              </div>
            </div>

            <button type="button" id="calcKwBtn" class="btn btn-primary btn-block" onclick="calculateKwCable()">Size Cable from kW</button>
          </form>

          <div id="kwResultBox" class="results-container" style="margin-top:20px;">
            <h3>kW Cable Conversion Results</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label">Recommended Cable Cross-Section</span>
                <span id="kwCableSizeOut" class="result-value">-- mm²</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Calculated Full-Load Current ($I_{FLA}$)</span>
                <span id="kwCurrentOut" class="result-value">-- A</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Continuous Design Current ($1.25 \times I$)</span>
                <span id="kwDesignCurrentOut" class="result-value">-- A</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Derated Cable Ampacity ($I_z$)</span>
                <span id="kwIzOut" class="result-value">-- A</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Line Voltage Drop ($\Delta V$)</span>
                <span id="kwVdOut" class="result-value">-- V (-- %)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Standard Circuit Breaker Size</span>
                <span id="kwBreakerOut" class="result-value">-- A</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Engineering Guide: Converting Kilowatts (kW) to Cable Cross-Section</h2>
          
          <p>Converting electrical active power in kilowatts ($kW$) into an accurately sized electrical cable is one of the most frequent tasks performed by electrical consulting engineers, contractors, and industrial technicians. Whether dimensioning a feeder for a $45\text{ kW}$ induction motor, a $150\text{ kW}$ commercial HVAC chiller, or a $22\text{ kW}$ electric vehicle fast charger, sizing cannot be completed by simple kW-to-area lookup tables. Doing so ignores the thermodynamic physics of line impedance, thermal dissipation, power factor, and voltage degradation.</p>

          <div class="formula-box">
            <h3>Derivation of Full-Load Running Current from Active Power</h3>
            <p>Kilowatts ($kW$) measure real electrical power performing mechanical or thermal work. To size conductors, this power must first be converted into root-mean-square (RMS) line current in Amperes ($A$):</p>
            <p><strong>For Three-Phase Balanced Circuits:</strong></p>
            <p>$$I = \frac{P_{kW} \times 1000}{\sqrt{3} \times V_{LL} \times \cos\varphi \times \eta}$$</p>
            <p><strong>For Single-Phase Circuits:</strong></p>
            <p>$$I = \frac{P_{kW} \times 1000}{V_{LN} \times \cos\varphi \times \eta}$$</p>
            <p>Where:</p>
            <ul>
              <li>$P_{kW}$ = Nameplate electrical or shaft power in kilowatts ($kW$).</li>
              <li>$V_{LL}$ = Line-to-line RMS voltage (e.g. $400\text{V}$ or $480\text{V}$).</li>
              <li>$V_{LN}$ = Line-to-neutral RMS voltage (e.g. $230\text{V}$ or $120\text{V}$).</li>
              <li>$\cos\varphi$ = Operating electrical load power factor ($\cos\theta$). Pure resistive heating has $\cos\varphi = 1.0$; induction motors typically operate between $0.80$ and $0.88$ lagging.</li>
              <li>$\eta$ = Fractional mechanical efficiency ($0.50$ to $1.0$). For motors, nameplate kW represents output shaft power, meaning electrical input is $P_{in} = P_{shaft} / \eta$.</li>
            </ul>
          </div>

          <h3>The Continuous Load Safety Factor: 125% Rule</h3>
          <p>Under both <strong>NEC Article 215.2 / 210.19</strong> and <strong>IEC 60364-5-52</strong>, when an electrical load is continuous (operating for 3 hours or more without interruption), the design current ($I_b$) is scaled up by a factor of $1.25$:</p>
          <p>$$I_{design} = 1.25 \times I_{FLA}$$</p>
          <p>This $25\%$ safety buffer prevents nuisance thermal tripping of circuit breakers and ensures conductors operate within safe long-term temperature boundaries.</p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Motor / Load Rating (kW)</th>
                <th>Three-Phase 400V FLA (0.85 PF, 90% Eff)</th>
                <th>Design Current ($1.25\times$)</th>
                <th>Recommended Copper Size (XLPE)</th>
                <th>Standard Breaker Rating</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>3.0 kW</strong></td>
                <td>5.66 A</td>
                <td>7.08 A</td>
                <td><strong>1.5 mm²</strong></td>
                <td>10 A Breaker</td>
              </tr>
              <tr>
                <td><strong>5.5 kW</strong></td>
                <td>10.38 A</td>
                <td>12.98 A</td>
                <td><strong>2.5 mm²</strong></td>
                <td>16 A Breaker</td>
              </tr>
              <tr>
                <td><strong>7.5 kW</strong></td>
                <td>14.16 A</td>
                <td>17.70 A</td>
                <td><strong>4.0 mm²</strong></td>
                <td>20 A Breaker</td>
              </tr>
              <tr>
                <td><strong>11.0 kW</strong></td>
                <td>20.76 A</td>
                <td>25.95 A</td>
                <td><strong>6.0 mm²</strong></td>
                <td>32 A Breaker</td>
              </tr>
              <tr>
                <td><strong>15.0 kW</strong></td>
                <td>28.31 A</td>
                <td>35.39 A</td>
                <td><strong>10.0 mm²</strong></td>
                <td>40 A Breaker</td>
              </tr>
              <tr>
                <td><strong>22.0 kW</strong></td>
                <td>41.52 A</td>
                <td>51.90 A</td>
                <td><strong>16.0 mm²</strong></td>
                <td>63 A Breaker</td>
              </tr>
              <tr>
                <td><strong>30.0 kW</strong></td>
                <td>56.63 A</td>
                <td>70.78 A</td>
                <td><strong>25.0 mm²</strong></td>
                <td>80 A Breaker</td>
              </tr>
              <tr>
                <td><strong>45.0 kW</strong></td>
                <td>84.94 A</td>
                <td>106.18 A</td>
                <td><strong>35.0 mm²</strong></td>
                <td>125 A Breaker</td>
              </tr>
              <tr>
                <td><strong>75.0 kW</strong></td>
                <td>141.57 A</td>
                <td>176.96 A</td>
                <td><strong>70.0 mm²</strong></td>
                <td>200 A Breaker</td>
              </tr>
              <tr>
                <td><strong>110.0 kW</strong></td>
                <td>207.63 A</td>
                <td>259.54 A</td>
                <td><strong>120.0 mm²</strong></td>
                <td>300 A Breaker</td>
              </tr>
            </tbody>
          </table>

          <div class="formula-box">
            <h3>Voltage Drop Limitation on Sizing</h3>
            <p>Even when a cable satisfies continuous thermal ampacity, conductor resistance $R$ over long route distances $L$ induces line voltage drop:</p>
            <p>$$\text{Three-Phase: } \Delta V = \sqrt{3} \times I \times L \times (R \cos\varphi + X \sin\varphi)$$</p>
            <p>$$\Delta V\% = \frac{\Delta V}{V_{nominal}} \times 100\%$$</p>
            <p>If $\Delta V\%$ exceeds statutory limits ($3\%$ for lighting, $4\%$ to $5\%$ for general industrial power per IEC 60364-5-52 Annex G), the conductor cross-section must be stepped up to the next standard gauge, regardless of thermal capacity.</p>
          </div>

          <div class="worked-example-card">
            <h3>Practical Worked Engineering Example: 30 kW Industrial Compressor Feeder</h3>
            <p><strong>Design Scenario:</strong> Size a three-phase, 400V, 50 Hz feeder cable powering a $30\text{ kW}$ rotary screw air compressor. The compressor motor operates with a power factor of $\cos\varphi = 0.85$ and a full-load mechanical efficiency of $\eta = 90\%$. The feeder is routed $50\text{ meters}$ along a cable ladder in a factory where ambient temperature peaks at $35^\circ\text{C}$. Multi-core copper cable with XLPE ($90^\circ\text{C}$) insulation is specified. Maximum permissible voltage drop is $4.0\%$.</p>

            <p><strong>Step 1: Calculate Full-Load Operating Current ($I_{FLA}$)</strong></p>
            <p>$$I_{FLA} = \frac{30 \times 1000}{\sqrt{3} \times 400 \times 0.85 \times 0.90} = \frac{30{,}000}{1.732 \times 400 \times 0.765} = \frac{30{,}000}{529.99} = 56.60\text{ Amperes}$$</p>

            <p><strong>Step 2: Apply Continuous Load Factor ($1.25\times$)</strong></p>
            <p>$$I_{design} = 1.25 \times 56.60\text{ A} = 70.75\text{ Amperes}$$</p>
            <p>A standard $80\text{ A}$ circuit breaker is selected ($I_n = 80\text{ A}$).</p>

            <p><strong>Step 3: Thermal Ampacity Sizing with Ambient Derating</strong></p>
            <p>At $35^\circ\text{C}$ ambient, XLPE derating factor $C_a = \sqrt{\frac{90 - 35}{90 - 30}} = 0.957$.</p>
            <p>Required tabulated rating:</p>
            <p>$$I_0 \ge \frac{I_n}{C_a} = \frac{80\text{ A}}{0.957} = 83.59\text{ A}$$</p>
            <p>From IEC 60364-5-52 Table B.52.4 (Method E, XLPE Copper):</p>
            <ul>
              <li>$10\text{ mm}^2 \implies I_0 = 80\text{ A}$ (Insufficient: $80 < 83.59$)</li>
              <li>$16\text{ mm}^2 \implies I_0 = 110\text{ A}$ (Compliant: $110 \ge 83.59\text{ A}$)</li>
            </ul>

            <p><strong>Step 4: Verification of Voltage Drop ($\Delta V$) on $16\text{ mm}^2$</strong></p>
            <p>For $16\text{ mm}^2$ copper XLPE, $(mV/A/m) \approx 2.4\text{ mV/A/m}$:</p>
            <p>$$\Delta V = \frac{2.4 \times 56.60\text{ A} \times 50\text{ m}}{1000} = 6.79\text{ Volts}$$</p>
            <p>$$\Delta V\% = \frac{6.79\text{ V}}{400\text{ V}} \times 100 = 1.70\%$$</p>
            <p>Since $1.70\% \le 4.0\%$, the $16\text{ mm}^2$ XLPE copper cable satisfies all thermal, mechanical, and voltage drop requirements.</p>
          </div>

          <h2>Frequently Asked Questions (kW to Cable Sizing)</h2>
          <div class="faq-item">
            <h3>Why does single-phase require much larger cable than three-phase for the same kW?</h3>
            <p>In a single-phase 230V system, all power travels through a single line and neutral pair ($P = V \cdot I$). In a 400V three-phase system, power divides across three separate phase conductors at a higher line-to-line voltage ($P = \sqrt{3} \cdot V_{LL} \cdot I$). A $10\text{ kW}$ load draws $43.5\text{ A}$ on single-phase 230V, requiring $10\text{ mm}^2$ cable, but only $14.4\text{ A}$ on 400V three-phase, requiring only $2.5\text{ mm}^2$ cable!</p>
          </div>

          <div class="faq-item">
            <h3>How do VFDs (Variable Frequency Drives) affect kW cable sizing?</h3>
            <p>Variable frequency drives generate high-frequency pulse-width modulated (PWM) voltage spikes ($dV/dt$) and high-frequency harmonic ground currents. While the continuous fundamental current corresponds to motor kW, shielded symmetrical VFD cables with XLPE insulation and foil/braid shields must be specified to prevent reflected wave insulation breakdown and EMI interference.</p>
          </div>

          <div class="faq-item">
            <h3>Can I use aluminum cable instead of copper for motor feeders?</h3>
            <p>Yes, but aluminum requires approximately $1.64\times$ greater cross-sectional area to achieve identical electrical resistance. For example, a $45\text{ kW}$ load that utilizes $35\text{ mm}^2$ copper typically requires $70\text{ mm}^2$ aluminum cable, and terminations must utilize dual-rated AL7CU or AL9CU mechanical compression lugs.</p>
          </div>

          <div class="faq-item">
            <h3>What is the difference between kVA and kW in cable sizing?</h3>
            <p>Kilowatts ($kW$) represent real active power doing work, while kilovolt-amperes ($kVA$) represent apparent total power ($kVA = kW / \cos\varphi$). Cables must carry the total vector sum of active and reactive current; therefore, cables are always dimensioned based on the total apparent power ($kVA$) or calculated line amperes ($I$), rather than active kilowatts alone.</p>
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
    // Standard IEC Copper Ratings (Method C/E approx values)
    const kwCableTable = [
      { size: 1.5,  c_xlpe: 23,  c_pvc: 19.5, mv_3p: 25.0, mv_1p: 29.0 },
      { size: 2.5,  c_xlpe: 31,  c_pvc: 26.0, mv_3p: 15.0, mv_1p: 18.0 },
      { size: 4.0,  c_xlpe: 42,  c_pvc: 35.0, mv_3p: 9.5,  mv_1p: 11.0 },
      { size: 6.0,  c_xlpe: 54,  c_pvc: 46.0, mv_3p: 6.4,  mv_1p: 7.3 },
      { size: 10.0, c_xlpe: 75,  c_pvc: 63.0, mv_3p: 3.8,  mv_1p: 4.4 },
      { size: 16.0, c_xlpe: 100, c_pvc: 85.0, mv_3p: 2.4,  mv_1p: 2.8 },
      { size: 25.0, c_xlpe: 127, c_pvc: 112,  mv_3p: 1.50, mv_1p: 1.75 },
      { size: 35.0, c_xlpe: 158, c_pvc: 138,  mv_3p: 1.10, mv_1p: 1.25 },
      { size: 50.0, c_xlpe: 192, c_pvc: 168,  mv_3p: 0.80, mv_1p: 0.93 },
      { size: 70.0, c_xlpe: 246, c_pvc: 213,  mv_3p: 0.55, mv_1p: 0.63 },
      { size: 95.0, c_xlpe: 298, c_pvc: 258,  mv_3p: 0.40, mv_1p: 0.46 },
      { size: 120,  c_xlpe: 346, c_pvc: 299,  mv_3p: 0.31, mv_1p: 0.36 },
      { size: 150,  c_xlpe: 399, c_pvc: 344,  mv_3p: 0.25, mv_1p: 0.29 },
      { size: 185,  c_xlpe: 456, c_pvc: 392,  mv_3p: 0.20, mv_1p: 0.23 },
      { size: 240,  c_xlpe: 538, c_pvc: 461,  mv_3p: 0.155, mv_1p: 0.18 }
    ];

    const standardBreakersList = [6, 10, 16, 20, 25, 32, 40, 50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630];

    function calculateKwCable() {
      const pKw = parseFloat(document.getElementById("powerKw").value) || 1;
      const supply = document.getElementById("kwSupplySystem").value;
      const pf = parseFloat(document.getElementById("kwPowerFactor").value) || 0.85;
      const effPct = parseFloat(document.getElementById("kwEfficiency").value) || 90;
      const metal = document.getElementById("kwConductorMetal").value;
      const insulation = document.getElementById("kwInsulation").value;
      const length = parseFloat(document.getElementById("kwRouteLength").value) || 1;
      const ambTemp = parseFloat(document.getElementById("kwAmbientTemp").value) || 30;
      const maxVd = parseFloat(document.getElementById("kwMaxVd").value) || 4.0;

      const eff = effPct / 100;
      let vNom = 400;
      let is3ph = true;

      if (supply === "400_3p") { vNom = 400; is3ph = true; }
      else if (supply === "230_1p") { vNom = 230; is3ph = false; }
      else if (supply === "480_3p") { vNom = 480; is3ph = true; }
      else if (supply === "208_3p") { vNom = 208; is3ph = true; }
      else if (supply === "120_1p") { vNom = 120; is3ph = false; }

      // Full Load Current
      let ifla = 0;
      if (is3ph) {
        ifla = (pKw * 1000) / (Math.sqrt(3) * vNom * pf * eff);
      } else {
        ifla = (pKw * 1000) / (vNom * pf * eff);
      }

      const idesign = ifla * 1.25;

      // Select standard breaker >= idesign
      let ocpd = standardBreakersList[standardBreakersList.length - 1];
      for (let i = 0; i < standardBreakersList.length; i++) {
        if (standardBreakersList[i] >= idesign) {
          ocpd = standardBreakersList[i];
          break;
        }
      }

      // Temperature correction factor
      let ca = 1.0;
      if (insulation === "xlpe") {
        ca = Math.sqrt(Math.max(0.1, (90 - ambTemp) / (90 - 30)));
      } else {
        ca = Math.sqrt(Math.max(0.1, (70 - ambTemp) / (70 - 30)));
      }

      const condMult = (metal === "aluminum") ? 0.78 : 1.0;

      let selected = null;

      for (let i = 0; i < kwCableTable.length; i++) {
        const row = kwCableTable[i];
        let baseRating = (insulation === "xlpe") ? row.c_xlpe : row.c_pvc;
        baseRating *= condMult;
        const iz = baseRating * ca;

        if (iz < ocpd) continue;

        let mv = is3ph ? row.mv_3p : row.mv_1p;
        if (metal === "aluminum") mv *= 1.64;

        const deltaV = (mv * ifla * length) / 1000;
        const vdPct = (deltaV / vNom) * 100;

        if (vdPct <= maxVd) {
          selected = {
            size: row.size,
            iz: iz,
            deltaV: deltaV,
            vdPct: vdPct
          };
          break;
        }
      }

      document.getElementById("kwCurrentOut").innerText = ifla.toFixed(1) + " A";
      document.getElementById("kwDesignCurrentOut").innerText = idesign.toFixed(1) + " A (1.25× Continuous)";
      document.getElementById("kwBreakerOut").innerText = ocpd + " A Standard Breaker";

      if (selected) {
        document.getElementById("kwCableSizeOut").innerText = selected.size + " mm² (" + metal.toUpperCase() + ")";
        document.getElementById("kwIzOut").innerText = selected.iz.toFixed(1) + " A";
        document.getElementById("kwVdOut").innerText = selected.deltaV.toFixed(2) + " V (" + selected.vdPct.toFixed(2) + "%)";
      } else {
        document.getElementById("kwCableSizeOut").innerText = "> 240 mm² (Parallel Conductors Req.)";
        document.getElementById("kwIzOut").innerText = "--";
        document.getElementById("kwVdOut").innerText = "Exceeds Drop Limit";
      }
    }

    document.addEventListener("DOMContentLoaded", function() {
      calculateKwCable();
    });
  </script>
</body>
</html>
"""

def main():
    root = r"C:\Users\Admin\.gemini\antigravity\scratch\calchub"
    
    p1 = os.path.join(root, "earthing-cable-size-calculator.html")
    with open(p1, "w", encoding="utf-8") as f:
        f.write(TOOL_1_HTML.strip() + "\n")
    print("[PASS] earthing-cable-size-calculator.html generated successfully!")

    p2 = os.path.join(root, "kw-to-cable-size-calculator.html")
    with open(p2, "w", encoding="utf-8") as f:
        f.write(TOOL_2_HTML.strip() + "\n")
    print("[PASS] kw-to-cable-size-calculator.html generated successfully!")

if __name__ == "__main__":
    main()
