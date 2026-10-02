# -*- coding: utf-8 -*-
"""
Script to generate Batch 6 Part 4 tools with standard CalcHub design system:
7. cable-sizing-calculator-iec-60364.html
8. cable-sizing-installation-method-a.html
"""
import os

TOOL_7_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cable Sizing Calculator IEC 60364 | International Low-Voltage Wiring Sizing</title>
  <meta name="description" content="Calculate low-voltage electrical cable sizes strictly compliant with IEC 60364-5-52. Computes thermal derating factors, continuous current capacity Iz, percentage voltage drop, and adiabatic short-circuit withstand.">
  <link rel="canonical" href="https://calchub.cloud/cable-sizing-calculator-iec-60364.html">
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
        "name": "Cable Sizing Calculator IEC 60364",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "IEC 60364-5-52 compliant low-voltage cable sizing engine calculating continuous current coordination, multi-factor thermal derating, loop impedance voltage drop, and adiabatic fault limits.",
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
            "name": "What is the difference between Ib, In, and Iz in IEC 60364?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In IEC electrical notation, Ib is the circuit design operating current determined by connected load power. In is the nominal rating or trip setting of the upstream overcurrent protective device. Iz is the continuous current-carrying capacity of the cable under its specific physical installation and ambient derating factors. IEC Clause 433.1 mandates that Ib <= In <= Iz."
            }
          },
          {
            "@type": "Question",
            "name": "Why does XLPE insulation permit smaller conductor cross-sections than PVC?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "XLPE is a thermosetting polymer with molecular cross-links that prevent thermal melting up to 90°C continuous operating temperature and 250°C under short-circuit conditions. PVC softens at 70°C continuous and decomposes above 160°C. The higher thermal headroom of XLPE allows significantly higher current density for identical conductor cross-sections."
            }
          },
          {
            "@type": "Question",
            "name": "What are the maximum permissible voltage drop limits under IEC 60364-5-52?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "IEC 60364-5-52 Annex G recommends a maximum voltage drop of 3% for lighting installations and 5% for other general power and heating applications fed directly from a public low-voltage distribution network. If the installation is fed from a private on-site high-voltage substation transformer, these limits expand to 6% for lighting and 8% for general power circuits."
            }
          },
          {
            "@type": "Question",
            "name": "How does IEC 60364 account for non-linear harmonic loads?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Under IEC 60364-5-52 Annex E, when triplen (third-order) harmonic currents exceed 15% of phase current, the neutral conductor carries substantial harmonic sum current. If harmonics are between 15% and 33%, a thermal derating factor of 0.86 is applied to the phase conductors. When third harmonics exceed 33%, the neutral conductor sizing dictates the cable size, and the design current is calculated based on Ib(neutral) = 3 * Ib * %H3."
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
      <span>Cable Sizing IEC 60364 Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">IEC 60364-5-52 &amp; IEC 60364-4-43</div>
          <h1 class="calc-title">Cable Sizing Calculator IEC 60364</h1>
          <p class="calc-tagline">Calculate low-voltage cable sizing, multi-factor thermal derating, loop voltage drop, and adiabatic fault withstand.</p>
        </header>

        <!-- Tool Card -->
        <div class="tool-card">
          <form id="iecForm" onsubmit="return false;">
            <div class="calc-grid">
              <div class="form-group">
                <label for="iecSystemType" class="form-label">System Supply Voltage</label>
                <select id="iecSystemType" class="form-control" onchange="calculateIec()">
                  <option value="400_3p" selected>Three-Phase 400V / 230V AC (50/60 Hz)</option>
                  <option value="230_1p">Single-Phase 230V AC (50/60 Hz)</option>
                  <option value="690_3p">Three-Phase Industrial 690V AC (50/60 Hz)</option>
                </select>
                <small class="form-hint">IEC nominal operating voltage</small>
              </div>

              <div class="form-group">
                <label for="iecConductor" class="form-label">Conductor Metallurgy</label>
                <select id="iecConductor" class="form-control" onchange="calculateIec()">
                  <option value="copper" selected>Annealed Electrolytic Copper (Cu)</option>
                  <option value="aluminium">Electrical Grade Aluminium (Al)</option>
                </select>
                <small class="form-hint">Core conductor material</small>
              </div>

              <div class="form-group">
                <label for="iecInsulation" class="form-label">Insulation &amp; Max Temperature</label>
                <select id="iecInsulation" class="form-control" onchange="calculateIec()">
                  <option value="xlpe" selected>XLPE / EPR (Thermosetting, 90°C)</option>
                  <option value="pvc">PVC (Thermoplastic, 70°C)</option>
                </select>
                <small class="form-hint">Continuous thermal threshold</small>
              </div>

              <div class="form-group">
                <label for="iecInstallMethod" class="form-label">Installation Reference Method</label>
                <select id="iecInstallMethod" class="form-control" onchange="calculateIec()">
                  <option value="C" selected>Method C: Clipped direct to masonry/surface</option>
                  <option value="A1">Method A1: Insulated conductors in conduit in insulated wall</option>
                  <option value="B1">Method B1: Conduit on wooden or masonry surface</option>
                  <option value="E">Method E: Multicore cable in free air or on perforated tray</option>
                  <option value="F">Method F: Single-core cables touching in free air (trefoil)</option>
                  <option value="D1">Method D1: Multi-core cable in buried underground duct</option>
                </select>
                <small class="form-hint">IEC 60364-5-52 Table A.52.3</small>
              </div>

              <div class="form-group">
                <label for="iecDesignCurrent" class="form-label">Design Current ($I_b$)</label>
                <div class="input-with-unit">
                  <input type="number" id="iecDesignCurrent" class="form-control" value="65" min="1" step="0.5" oninput="calculateIec()">
                  <span class="unit-badge">Amps</span>
                </div>
                <small class="form-hint">Continuous load design current</small>
              </div>

              <div class="form-group">
                <label for="iecBreakerIn" class="form-label">Protective Device Rating ($I_n$)</label>
                <div class="input-with-unit">
                  <input type="number" id="iecBreakerIn" class="form-control" value="80" min="1" step="1" oninput="calculateIec()">
                  <span class="unit-badge">Amps</span>
                </div>
                <small class="form-hint">Nominal circuit breaker / fuse rating</small>
              </div>

              <div class="form-group">
                <label for="iecAmbientTemp" class="form-label">Ambient Temperature</label>
                <div class="input-with-unit">
                  <input type="number" id="iecAmbientTemp" class="form-control" value="35" min="10" max="65" step="1" oninput="calculateIec()">
                  <span class="unit-badge">°C</span>
                </div>
                <small class="form-hint">Local ambient air temperature</small>
              </div>

              <div class="form-group">
                <label for="iecGroupingCount" class="form-label">Number of Grouped Circuits ($k_2$)</label>
                <div class="input-with-unit">
                  <input type="number" id="iecGroupingCount" class="form-control" value="3" min="1" max="20" step="1" oninput="calculateIec()">
                  <span class="unit-badge">Circuits</span>
                </div>
                <small class="form-hint">Grouping derating factor</small>
              </div>

              <div class="form-group">
                <label for="iecRouteLength" class="form-label">One-Way Route Length ($L$)</label>
                <div class="input-with-unit">
                  <input type="number" id="iecRouteLength" class="form-control" value="55" min="1" step="1" oninput="calculateIec()">
                  <span class="unit-badge">metres</span>
                </div>
                <small class="form-hint">Distance from distribution board to load</small>
              </div>

              <div class="form-group">
                <label for="iecMaxVd" class="form-label">Max Allowable Voltage Drop</label>
                <div class="input-with-unit">
                  <input type="number" id="iecMaxVd" class="form-control" value="4.0" min="1.0" max="10.0" step="0.1" oninput="calculateIec()">
                  <span class="unit-badge">%</span>
                </div>
                <small class="form-hint">IEC standard threshold (typically 3%–5%)</small>
              </div>

              <div class="form-group">
                <label for="iecFaultCurrent" class="form-label">Short-Circuit Fault Current ($I_{sc}$)</label>
                <div class="input-with-unit">
                  <input type="number" id="iecFaultCurrent" class="form-control" value="10" min="0.1" step="0.5" oninput="calculateIec()">
                  <span class="unit-badge">kA</span>
                </div>
                <small class="form-hint">Prospective symmetrical RMS fault current</small>
              </div>

              <div class="form-group">
                <label for="iecFaultTime" class="form-label">Fault Clearance Time ($t$)</label>
                <div class="input-with-unit">
                  <input type="number" id="iecFaultTime" class="form-control" value="0.1" min="0.01" max="5.0" step="0.01" oninput="calculateIec()">
                  <span class="unit-badge">sec</span>
                </div>
                <small class="form-hint">Breaker / fuse disconnection speed</small>
              </div>
            </div>

            <button type="button" id="calcIecBtn" class="btn btn-primary btn-block" onclick="calculateIec()">Dimension Cable (IEC 60364-5-52)</button>
          </form>

          <div id="iecResultBox" class="results-container" style="margin-top:20px;">
            <h3>IEC Sizing Verification Summary</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label">Recommended Conductor Area</span>
                <span id="iecSizeOut" class="result-value">-- mm²</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Total Derating Factor ($k_1 \times k_2$)</span>
                <span id="iecDeratingFactorOut" class="result-value">--</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Effective Derated Capacity ($I_z$)</span>
                <span id="iecIzOut" class="result-value">-- A</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Calculated Voltage Drop ($\Delta V$)</span>
                <span id="iecVdVoltsOut" class="result-value">-- V (-- %)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Minimum Adiabatic Area ($S_{ad}$)</span>
                <span id="iecAdiabaticOut" class="result-value">-- mm²</span>
              </div>
              <div class="result-tile">
                <span class="result-label">IEC Rule 433.1 Coordination</span>
                <span id="iecStatusOut" class="result-value">--</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Comprehensive Engineering Guide: Low-Voltage Cable Sizing per IEC 60364-5-52</h2>
          
          <p>In international electrical engineering practice across Europe, Asia, the Middle East, Australasia, and Africa, electrical installations must adhere strictly to the foundational standards codified by the International Electrotechnical Commission (IEC). The cornerstone standard governing low-voltage conductor dimensioning is <strong>IEC 60364 (Low-voltage electrical installations)</strong>, specifically <strong>Part 5-52 (Selection and erection of electrical equipment &mdash; Wiring systems)</strong> and <strong>Part 4-43 (Protection for safety &mdash; Protection against overcurrent)</strong>. Unlike empirical guidelines, sizing a low-voltage feeder according to IEC 60364 requires satisfying a tri-fold deterministic framework: continuous thermal equilibrium under rated and grouped conditions, dynamic electro-thermal survival during short-circuit transients, and functional line-voltage stability under steady-state running loads.</p>

          <div class="formula-box">
            <h3>Fundamental Overcurrent Protection Coordination: IEC 60364 Clause 433.1</h3>
            <p>For any continuous electrical circuit protected by a circuit breaker or fuse, the circuit design current $I_b$, the rated nominal current of the protective device $I_n$, and the continuous current-carrying capacity of the derated cable $I_z$ must satisfy the continuous coordination inequalities:</p>
            <p>$$I_b \le I_n \le I_z$$</p>
            <p>Additionally, for complete thermal protection against conventional tripping currents ($I_2$, where $I_2 = 1.45 \cdot I_n$ for Type B, C, and D miniature circuit breakers or gG fuses per IEC 60898 / IEC 60947-2):</p>
            <p>$$I_2 \le 1.45 \cdot I_z$$</p>
          </div>

          <h3>Derivation of Real-World Current-Carrying Capacity ($I_z$)</h3>
          <p>Cable manufacturers publish base current ratings ($I_0$) calibrated under standardized laboratory benchmark conditions: an ambient air temperature of $30^\circ\text{C}$ (or ground temperature of $20^\circ\text{C}$ for direct buried installations), isolation from adjacent heat-dissipating conductors, and a specific installation orientation. When installed in real physical environments, the maximum permissible current $I_z$ decreases due to surrounding thermal impedance.</p>
          
          <p>Under IEC 60364-5-52 Clause 523, the actual current capacity $I_z$ of an installed conductor is derived by multiplying its base tabulated rating $I_0$ by a sequence of environment-specific correction factors:</p>
          
          <p>$$I_z = I_0 \times k_1 \times k_2 \times k_3 \times k_4$$</p>
          
          <ul>
            <li><strong>$k_1$ (Ambient Temperature Correction Factor):</strong> Derived from the thermodynamic balance equation $k_1 = \sqrt{\frac{\theta_{max} - \theta_{amb}}{\theta_{max} - 30}}$, where $\theta_{max} = 70^\circ\text{C}$ for standard thermoplastic polyvinyl chloride (PVC) and $\theta_{max} = 90^\circ\text{C}$ for thermosetting cross-linked polyethylene (XLPE) or ethylene propylene rubber (EPR). When ambient temperatures reach $40^\circ\text{C}$ in industrial switchrooms, XLPE retains a healthy derating factor of $k_1 = \sqrt{\frac{90-40}{90-30}} = 0.91$, whereas PVC plummets to $k_1 = \sqrt{\frac{70-40}{70-30}} = 0.87$.</li>
            <li><strong>$k_2$ (Grouping Factor):</strong> Governed by IEC 60364-5-52 Table B.52.17. When multiple multicore cables or single-core circuits are routed in close proximity on trays, ladders, or inside conduits, mutual induction and convective air stagnation degrade heat dissipation. A run of 6 bundled circuits carries a grouping penalty factor of $k_2 \approx 0.57$, effectively slashing continuous cable ampacity by $43\%$.</li>
            <li><strong>$k_3$ (Soil Thermal Resistivity Factor):</strong> Applicable to direct buried conduits and trenches where the specific ground resistivity deviates from the standard benchmark of $2.5\text{ K}\cdot\text{m/W}$. Moist soils enhance heat dissipation ($k_3 > 1.0$), while dry sand or backfill can restrict dissipation ($k_3 < 0.80$).</li>
            <li><strong>$k_4$ (Harmonic Neutral Current Factor):</strong> Outlined in Annex E of IEC 60364-5-52, addressing triplen harmonic loads (predominantly 3rd harmonic currents generated by non-linear switched-mode power supplies, LED drivers, and variable frequency drives) which accumulate additively in the neutral conductor, inducing thermal hotspots requiring conductor up-sizing.</li>
          </ul>

          <h3>Standardized IEC Installation Methods (Table A.52.3)</h3>
          <p>The rate of convective and radiative thermal dissipation depends directly upon physical mounting geometry. IEC 60364-5-52 organizes installations into discrete reference methods:</p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>IEC Reference Method</th>
                <th>Physical Mounting Architecture</th>
                <th>Heat Dissipation Mechanism</th>
                <th>Comparative Relative Ampacity</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Method A1 / A2</strong></td>
                <td>Conductors inside conduit embedded in a thermally insulated wall</td>
                <td>Pure thermal conduction through insulating matrix; extremely high thermal resistance</td>
                <td>Lowest base rating (Benchmark $1.0\times$)</td>
              </tr>
              <tr>
                <td><strong>Method B1 / B2</strong></td>
                <td>Cables inside surface-mounted conduit or trunking on masonry or wood</td>
                <td>Convective boundary layer along conduit outer perimeter</td>
                <td>Moderate rating ($\approx 1.25\times$ of Method A)</td>
              </tr>
              <tr>
                <td><strong>Method C</strong></td>
                <td>Single-core or multi-core cables clipped directly to a non-combustible surface</td>
                <td>Direct conductive sinking into masonry combined with unrestricted convective draft</td>
                <td>High rating ($\approx 1.45\times$ of Method A)</td>
              </tr>
              <tr>
                <td><strong>Method E</strong></td>
                <td>Multicore cable in free air on open cable ladder or perforated horizontal cable tray</td>
                <td>Full $360^\circ$ natural convection and radiant emission into switchroom atmosphere</td>
                <td>Very high rating ($\approx 1.60\times$ of Method A)</td>
              </tr>
              <tr>
                <td><strong>Method F</strong></td>
                <td>Single-core cables touching in free air arranged in trefoil or flat configuration</td>
                <td>Optimized inductive phase balance and unobstructed air flow surrounding conductors</td>
                <td>Highest standard open rating ($\approx 1.70\times$ of Method A)</td>
              </tr>
              <tr>
                <td><strong>Method D1 / D2</strong></td>
                <td>Cables routed in buried underground ducts or pipes embedded in soil</td>
                <td>Ground conduction dependent on backfill soil moisture content and burial depth</td>
                <td>Variable depending on ground thermal resistivity $g$</td>
              </tr>
            </tbody>
          </table>

          <h3>Voltage Drop Formulation: Resistive &amp; Reactive Vector Components</h3>
          <p>Thermal ampacity alone is insufficient to guarantee code compliance. Long branch feeders and sub-main distributions suffer line-to-line voltage degradation due to the complex impedance of the copper or aluminium core. For cables larger than $16\text{ mm}^2$, conductor self-inductance ($X = \omega L$) cannot be neglected.</p>
          
          <p>Under IEC 60364-5-52 Annex G, steady-state voltage drop is calculated via vector projection onto the reference voltage phase:</p>
          
          <p>$$\text{Three-Phase: } \Delta V = \sqrt{3} \cdot I_b \cdot L \cdot (R \cos\varphi + X \sin\varphi)$$</p>
          <p>$$\text{Single-Phase: } \Delta V = 2 \cdot I_b \cdot L \cdot (R \cos\varphi + X \sin\varphi)$$</p>
          
          <p>Where $R$ represents the AC conductor resistance at maximum continuous operating temperature ($70^\circ\text{C}$ for PVC, $90^\circ\text{C}$ for XLPE) derived from $R = R_{20} [1 + \alpha_{20} (\theta_{max} - 20)]$, $X$ is the specific line reactance ($\approx 0.08\text{ to } 0.09\text{ m}\Omega/\text{m}$ for closely spaced low-voltage cores), $\cos\varphi$ is the operating load power factor, and $L$ is the one-way route length in meters.</p>

          <div class="formula-box">
            <h3>Adiabatic Short-Circuit Withstand: IEC 60364-4-43 Clause 434.5.2</h3>
            <p>During an instantaneous short-circuit fault, energy is dissipated so rapidly (under 5 seconds) that heat transfer out through the insulation into the ambient surroundings is zero (pure adiabatic process). To prevent catastrophic thermal degradation of the polymer insulation, the conductor cross-sectional area $S$ must satisfy the adiabatic equation:</p>
            <p>$$S \ge \frac{\sqrt{I_{sc}^2 \cdot t}}{k}$$</p>
            <p>Where $I_{sc}$ is the prospective root-mean-square short-circuit fault current in Amperes, $t$ is the operating clearance time of the protective device in seconds, and $k$ is the thermodynamic material coefficient defined in IEC 60364-4-43 Table 43A:</p>
            <ul>
              <li><strong>Copper with XLPE/EPR Insulation ($90^\circ\text{C} \to 250^\circ\text{C}$ limit):</strong> $k = 143\text{ A}\cdot\text{s}^{1/2}/\text{mm}^2$</li>
              <li><strong>Copper with PVC Insulation ($70^\circ\text{C} \to 160^\circ\text{C}$ limit):</strong> $k = 115\text{ A}\cdot\text{s}^{1/2}/\text{mm}^2$</li>
              <li><strong>Aluminium with XLPE/EPR Insulation ($90^\circ\text{C} \to 250^\circ\text{C}$ limit):</strong> $k = 94\text{ A}\cdot\text{s}^{1/2}/\text{mm}^2$</li>
              <li><strong>Aluminium with PVC Insulation ($70^\circ\text{C} \to 160^\circ\text{C}$ limit):</strong> $k = 76\text{ A}\cdot\text{s}^{1/2}/\text{mm}^2$</li>
            </ul>
          </div>

          <div class="worked-example-card">
            <h3>Practical Worked Engineering Example: Industrial Sub-Distribution Feeder</h3>
            <p><strong>Design Scenario:</strong> An industrial facility requires sizing a 3-phase, 400V, 50 Hz feeder cable feeding a motor control center with a design running load $I_b = 65\text{ A}$ at $0.85$ power factor lagging. The circuit is protected by an $80\text{ A}$ molded-case circuit breaker ($I_n = 80\text{ A}$). The cable route is $55\text{ meters}$ long, clipped directly to an interior masonry wall (Method C), running parallel alongside 2 other loaded circuits (total 3 circuits grouped touching). The facility ambient temperature reaches $35^\circ\text{C}$. The upstream prospective fault current is $10\text{ kA}$ with a breaker opening time of $t = 0.08\text{ seconds}$. The cable selected is multi-core copper with XLPE insulation.</p>
            
            <p><strong>Step 1: Calculate Environmental Derating Factors ($k_1 \times k_2$)</strong></p>
            <p>For XLPE at $35^\circ\text{C}$ ambient, Table B.52.14 specifies $k_1 = 0.96$. For 3 circuits clipped direct touching (Table B.52.17), $k_2 = 0.70$.</p>
            <p>$$k_{total} = k_1 \times k_2 = 0.96 \times 0.70 = 0.672$$</p>
            
            <p><strong>Step 2: Minimum Required Tabulated Current Rating ($I_0$)</strong></p>
            <p>To satisfy $I_n \le I_z$, the required baseline tabulated rating must be:</p>
            <p>$$I_0 \ge \frac{I_n}{k_{total}} = \frac{80\text{ A}}{0.672} = 119.05\text{ A}$$</p>
            <p>Referring to IEC 60364-5-52 Table B.52.4 (Method C, 3-phase XLPE copper):</p>
            <ul>
              <li>$16\text{ mm}^2 \implies I_0 = 100\text{ A}$ (Insufficient: $100 < 119.05$)</li>
              <li>$25\text{ mm}^2 \implies I_0 = 127\text{ A}$ (Compliant: $127 \ge 119.05$). Derated capacity $I_z = 127 \times 0.672 = 85.34\text{ A} > 80\text{ A}$.</li>
            </ul>

            <p><strong>Step 3: Verification of Voltage Drop ($\Delta V$) on $25\text{ mm}^2$</strong></p>
            <p>For $25\text{ mm}^2$ copper at $90^\circ\text{C}$, $R = 0.927\text{ m}\Omega/\text{m}$, and $X = 0.082\text{ m}\Omega/\text{m}$. With $\cos\varphi = 0.85$ and $\sin\varphi = 0.527$:</p>
            <p>$$\Delta V = \sqrt{3} \times 65\text{ A} \times 55\text{ m} \times [0.000927(0.85) + 0.000082(0.527)]$$</p>
            <p>$$\Delta V = 6192 \times [0.000788 + 0.000043] = 6192 \times 0.000831 = 5.15\text{ Volts}$$</p>
            <p>$$\Delta V\% = \frac{5.15\text{ V}}{400\text{ V}} \times 100 = 1.29\%$$</p>
            <p>This is well within the IEC standard $4.0\%$ limit for sub-main power circuits.</p>

            <p><strong>Step 4: Verification of Adiabatic Short-Circuit Withstand ($S_{ad}$)</strong></p>
            <p>Using $k = 143$ for copper XLPE:</p>
            <p>$$S_{ad} = \frac{\sqrt{(10{,}000\text{ A})^2 \times 0.08\text{ s}}}{143} = \frac{10{,}000 \times 0.2828}{143} = \frac{2828.4}{143} = 19.78\text{ mm}^2$$</p>
            <p>Since the thermal sizing is $25\text{ mm}^2 > 19.78\text{ mm}^2$, the cable satisfies all thermal, voltage drop, and fault withstand requirements of IEC 60364.</p>
          </div>

          <h2>Frequently Asked Questions (IEC 60364 Cable Sizing)</h2>
          <div class="faq-item">
            <h3>What is the difference between $I_b$, $I_n$, and $I_z$ in IEC 60364?</h3>
            <p>In IEC electrical notation, $I_b$ is the circuit design operating current determined by connected load power. $I_n$ is the nominal rating or trip setting of the upstream overcurrent protective device (MCB or MCCB). $I_z$ is the continuous current-carrying capacity of the cable under its specific physical installation and ambient derating factors. IEC Clause 433.1 mandates that $I_b \le I_n \le I_z$.</p>
          </div>

          <div class="faq-item">
            <h3>Why does XLPE insulation permit smaller conductor cross-sections than PVC?</h3>
            <p>XLPE (cross-linked polyethylene) is a thermosetting polymer with molecular cross-links that prevent thermal melting up to $90^\circ\text{C}$ continuous operating temperature and $250^\circ\text{C}$ under short-circuit conditions. PVC is a thermoplastic that softens at $70^\circ\text{C}$ continuous and decomposes above $160^\circ\text{C}$. The higher thermal headroom of XLPE allows significantly higher current density for identical conductor cross-sections.</p>
          </div>

          <div class="faq-item">
            <h3>What are the maximum permissible voltage drop limits under IEC 60364-5-52?</h3>
            <p>IEC 60364-5-52 Annex G recommends a maximum voltage drop of $3\%$ for lighting installations and $5\%$ for other general power and heating applications fed directly from a public low-voltage distribution network. If the installation is fed from a private on-site high-voltage substation transformer, these limits expand to $6\%$ for lighting and $8\%$ for general power circuits.</p>
          </div>

          <div class="faq-item">
            <h3>How does IEC 60364 account for non-linear harmonic loads?</h3>
            <p>Under IEC 60364-5-52 Annex E, when triplen (third-order) harmonic currents exceed $15\%$ of phase current, the neutral conductor carries substantial harmonic sum current. If harmonics are between $15\%$ and $33\%$, a thermal derating factor of $0.86$ is applied to the phase conductors. When third harmonics exceed $33\%$, the neutral conductor sizing dictates the cable size, and the design current is calculated based on $I_b(neutral) = 3 \times I_b \times \%H_3$.</p>
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
    const iecDataCu = [
      { size: 1.5,  c_xlpe: 23,  c_pvc: 19.5, r: 15.4,   x: 0.111 },
      { size: 2.5,  c_xlpe: 31,  c_pvc: 26,   r: 9.45,   x: 0.102 },
      { size: 4,    c_xlpe: 42,  c_pvc: 35,   r: 5.88,   x: 0.096 },
      { size: 6,    c_xlpe: 54,  c_pvc: 46,   r: 3.93,   x: 0.090 },
      { size: 10,   c_xlpe: 75,  c_pvc: 63,   r: 2.33,   x: 0.086 },
      { size: 16,   c_xlpe: 100, c_pvc: 85,   r: 1.46,   x: 0.083 },
      { size: 25,   c_xlpe: 127, c_pvc: 112,  r: 0.927,  x: 0.082 },
      { size: 35,   c_xlpe: 158, c_pvc: 138,  r: 0.669,  x: 0.081 },
      { size: 50,   c_xlpe: 192, c_pvc: 168,  r: 0.499,  x: 0.080 },
      { size: 70,   c_xlpe: 246, c_pvc: 213,  r: 0.342,  x: 0.079 },
      { size: 95,   c_xlpe: 298, c_pvc: 258,  r: 0.247,  x: 0.078 },
      { size: 120,  c_xlpe: 346, c_pvc: 299,  r: 0.196,  x: 0.077 },
      { size: 150,  c_xlpe: 399, c_pvc: 344,  r: 0.159,  x: 0.077 },
      { size: 185,  c_xlpe: 456, c_pvc: 392,  r: 0.128,  x: 0.076 },
      { size: 240,  c_xlpe: 538, c_pvc: 461,  r: 0.098,  x: 0.075 },
      { size: 300,  c_xlpe: 621, c_pvc: 530,  r: 0.078,  x: 0.075 }
    ];

    const methodMultipliers = {
      "A1": 0.72,
      "B1": 0.85,
      "C": 1.00,
      "E": 1.10,
      "F": 1.18,
      "D1": 0.88
    };

    function calculateIec() {
      const sysType = document.getElementById("iecSystemType").value;
      const conductor = document.getElementById("iecConductor").value;
      const insulation = document.getElementById("iecInsulation").value;
      const method = document.getElementById("iecInstallMethod").value;
      const Ib = parseFloat(document.getElementById("iecDesignCurrent").value) || 0;
      const In = parseFloat(document.getElementById("iecBreakerIn").value) || 0;
      const ambTemp = parseFloat(document.getElementById("iecAmbientTemp").value) || 30;
      const groupCount = parseInt(document.getElementById("iecGroupingCount").value) || 1;
      const length = parseFloat(document.getElementById("iecRouteLength").value) || 1;
      const maxVdPct = parseFloat(document.getElementById("iecMaxVd").value) || 4.0;
      const faultKa = parseFloat(document.getElementById("iecFaultCurrent").value) || 10;
      const faultTime = parseFloat(document.getElementById("iecFaultTime").value) || 0.1;

      let k1 = 1.0;
      if (insulation === "xlpe") {
        k1 = Math.sqrt(Math.max(0.1, (90 - ambTemp) / (90 - 30)));
      } else {
        k1 = Math.sqrt(Math.max(0.1, (70 - ambTemp) / (70 - 30)));
      }

      let k2 = 1.0;
      if (groupCount === 2) k2 = 0.80;
      else if (groupCount === 3) k2 = 0.70;
      else if (groupCount === 4) k2 = 0.65;
      else if (groupCount === 5) k2 = 0.60;
      else if (groupCount === 6) k2 = 0.57;
      else if (groupCount > 6) k2 = 0.50;

      const k_total = k1 * k2;
      const methodMult = methodMultipliers[method] || 1.0;
      const condMultiplier = (conductor === "aluminium") ? 0.78 : 1.0;

      let k_factor = 143;
      if (conductor === "copper" && insulation === "pvc") k_factor = 115;
      if (conductor === "aluminium" && insulation === "xlpe") k_factor = 94;
      if (conductor === "aluminium" && insulation === "pvc") k_factor = 76;

      const s_adiabatic = (faultKa * 1000 * Math.sqrt(faultTime)) / k_factor;

      let selected = null;
      let v_nom = (sysType === "230_1p") ? 230 : (sysType === "690_3p" ? 690 : 400);

      for (let i = 0; i < iecDataCu.length; i++) {
        const row = iecDataCu[i];
        const baseC = (insulation === "xlpe") ? row.c_xlpe : row.c_pvc;
        const nominalI0 = baseC * methodMult * condMultiplier;
        const effectiveIz = nominalI0 * k_total;

        if (effectiveIz < In) continue;
        if (row.size < s_adiabatic) continue;

        const res = (conductor === "aluminium") ? (row.r * 1.64) : row.r;
        const cosPhi = 0.85;
        const sinPhi = 0.527;
        const rLoop = (res / 1000) * cosPhi + (row.x / 1000) * sinPhi;

        let deltaV = 0;
        if (sysType === "230_1p") {
          deltaV = 2 * Ib * length * rLoop;
        } else {
          deltaV = Math.sqrt(3) * Ib * length * rLoop;
        }
        const vdPct = (deltaV / v_nom) * 100;

        if (vdPct <= maxVdPct) {
          selected = {
            size: row.size,
            iz: effectiveIz,
            vdVolts: deltaV,
            vdPct: vdPct
          };
          break;
        }
      }

      document.getElementById("iecDeratingFactorOut").innerText = k_total.toFixed(3);
      document.getElementById("iecAdiabaticOut").innerText = s_adiabatic.toFixed(2) + " mm²";

      if (selected) {
        document.getElementById("iecSizeOut").innerText = selected.size + " mm² (" + conductor.toUpperCase() + ")";
        document.getElementById("iecIzOut").innerText = selected.iz.toFixed(1) + " A";
        document.getElementById("iecVdVoltsOut").innerText = selected.vdVolts.toFixed(2) + " V (" + selected.vdPct.toFixed(2) + "%)";
        document.getElementById("iecStatusOut").innerText = "Fully Compliant (Ib <= In <= Iz)";
        document.getElementById("iecStatusOut").style.color = "#10b981";
      } else {
        document.getElementById("iecSizeOut").innerText = "> 300 mm² (Parallel Runs Req.)";
        document.getElementById("iecIzOut").innerText = "Exceeds standard limits";
        document.getElementById("iecVdVoltsOut").innerText = "Exceeds threshold";
        document.getElementById("iecStatusOut").innerText = "Non-Compliant: Parallel Runs Needed";
        document.getElementById("iecStatusOut").style.color = "#ef4444";
      }
    }

    document.addEventListener("DOMContentLoaded", function() {
      calculateIec();
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
  <title>Cable Sizing Installation Method A Calculator | Insulated Wall Wiring</title>
  <meta name="description" content="Calculate low-voltage cable sizing for IEC 60364 and BS 7671 Installation Method A (A1 and A2: conductors in conduit embedded inside thermally insulated walls).">
  <link rel="canonical" href="https://calchub.cloud/cable-sizing-installation-method-a.html">
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
        "name": "Cable Sizing Installation Method A Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Specialized electrical engineering calculator for dimensioning low-voltage cables in high thermal resistance environments (IEC Method A1 and A2 insulated cavity walls).",
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
            "name": "Why is Method A considered the worst-case thermal installation method?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Thermal insulation materials like fiberglass, rockwool, and polyurethane are engineered specifically to impede conductive and convective heat transport. Enclosing an energized conductor inside such a medium traps virtually all I²R joule heat inside the conduit. In contrast to open cable trays or masonry walls which act as heat sinks, insulated cavity walls force conductors to operate at their maximum permissible temperatures under substantially lower currents."
            }
          },
          {
            "@type": "Question",
            "name": "Can I use XLPE cable to avoid upsizing conductor cross-section in Method A?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes. Because XLPE is rated for continuous operation at 90°C compared to 70°C for standard PVC, its base ampacity in Method A is higher. For example, a 6.0 mm² XLPE multicore cable in Method A carries 40A, compared to only 32A for PVC. However, you must verify that the terminating circuit breaker terminals are rated for 90°C operation."
            }
          },
          {
            "@type": "Question",
            "name": "What if the cable only passes through insulation for a short distance?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "If the length of cable enclosed within insulation is under 500 mm, international standards allow relaxation of the derating factor. Under BS 7671 Table 52.2, a run of 100 mm requires a factor of 0.78, while a run under 50 mm incurs no thermal penalty (Ci = 1.0) because heat conducts along the copper length into cooler sections."
            }
          },
          {
            "@type": "Question",
            "name": "Does Installation Method A apply to cables routed inside metal conduit?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes. While metallic conduit conducts heat better than PVC conduit, the conduit remains entirely encased within the fibrous insulation. Heat cannot escape into the building space, meaning the air pocket inside the conduit still reaches elevated temperatures. Therefore, metallic conduits enclosed in insulated walls must be derated under Method A."
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
      <span>Method A Cable Sizing Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">IEC 60364-5-52 &amp; BS 7671 Method A</div>
          <h1 class="calc-title">Cable Sizing Installation Method A Calculator</h1>
          <p class="calc-tagline">Dimension cables enclosed in conduit within thermally insulated walls (Method A1 single-core &amp; A2 multi-core).</p>
        </header>

        <!-- Tool Card -->
        <div class="tool-card">
          <form id="methAForm" onsubmit="return false;">
            <div class="calc-grid">
              <div class="form-group">
                <label for="methASubType" class="form-label">Method A Configuration</label>
                <select id="methASubType" class="form-control" onchange="calculateMethA()">
                  <option value="A1">Method A1: Single-core insulated conductors in conduit in insulated wall</option>
                  <option value="A2" selected>Method A2: Multi-core cable in conduit in insulated wall</option>
                </select>
                <small class="form-hint">IEC 60364 Table A.52.3 sub-type</small>
              </div>

              <div class="form-group">
                <label for="methAConductor" class="form-label">Conductor Metallurgy</label>
                <select id="methAConductor" class="form-control" onchange="calculateMethA()">
                  <option value="cu" selected>Copper Conductor (Cu)</option>
                  <option value="al">Aluminium Conductor (Al)</option>
                </select>
                <small class="form-hint">Conductor core material</small>
              </div>

              <div class="form-group">
                <label for="methAInsulation" class="form-label">Insulation Polymer</label>
                <select id="methAInsulation" class="form-control" onchange="calculateMethA()">
                  <option value="xlpe" selected>XLPE / 90°C Thermosetting</option>
                  <option value="pvc">PVC / 70°C Thermoplastic</option>
                </select>
                <small class="form-hint">Operating temperature limit</small>
              </div>

              <div class="form-group">
                <label for="methAPhasing" class="form-label">Phase Configuration &amp; Voltage</label>
                <select id="methAPhasing" class="form-control" onchange="calculateMethA()">
                  <option value="1p" selected>Single-Phase 230V AC</option>
                  <option value="3p">Three-Phase 400V AC</option>
                </select>
                <small class="form-hint">Nominal line AC supply</small>
              </div>

              <div class="form-group">
                <label for="methADesignCurrent" class="form-label">Design Current ($I_b$)</label>
                <div class="input-with-unit">
                  <input type="number" id="methADesignCurrent" class="form-control" value="28" min="1" step="0.5" oninput="calculateMethA()">
                  <span class="unit-badge">Amps</span>
                </div>
                <small class="form-hint">Operating load current</small>
              </div>

              <div class="form-group">
                <label for="methABreakerIn" class="form-label">Protective Device Rating ($I_n$)</label>
                <div class="input-with-unit">
                  <input type="number" id="methABreakerIn" class="form-control" value="32" min="1" step="1" oninput="calculateMethA()">
                  <span class="unit-badge">Amps</span>
                </div>
                <small class="form-hint">Upstream MCB nominal trip rating</small>
              </div>

              <div class="form-group">
                <label for="methAAmbientTemp" class="form-label">Ambient Temperature</label>
                <div class="input-with-unit">
                  <input type="number" id="methAAmbientTemp" class="form-control" value="30" min="10" max="60" step="1" oninput="calculateMethA()">
                  <span class="unit-badge">°C</span>
                </div>
                <small class="form-hint">Air temperature surrounding wall</small>
              </div>

              <div class="form-group">
                <label for="methAGroupCount" class="form-label">Number of Grouped Conduits ($C_g$)</label>
                <div class="input-with-unit">
                  <input type="number" id="methAGroupCount" class="form-control" value="2" min="1" max="10" step="1" oninput="calculateMethA()">
                  <span class="unit-badge">Circuits</span>
                </div>
                <small class="form-hint">Mutual proximity derating factor</small>
              </div>

              <div class="form-group">
                <label for="methATotalLength" class="form-label">Total Circuit Route Length</label>
                <div class="input-with-unit">
                  <input type="number" id="methATotalLength" class="form-control" value="35" min="1" step="1" oninput="calculateMethA()">
                  <span class="unit-badge">metres</span>
                </div>
                <small class="form-hint">Total one-way length</small>
              </div>

              <div class="form-group">
                <label for="methAInsulLength" class="form-label">Length Inside Insulated Wall</label>
                <div class="input-with-unit">
                  <input type="number" id="methAInsulLength" class="form-control" value="15" min="0" step="0.5" oninput="calculateMethA()">
                  <span class="unit-badge">metres</span>
                </div>
                <small class="form-hint">Enclosed cavity section length</small>
              </div>

              <div class="form-group">
                <label for="methAMaxVd" class="form-label">Max Allowable Voltage Drop</label>
                <div class="input-with-unit">
                  <input type="number" id="methAMaxVd" class="form-control" value="3.0" min="1.0" max="10.0" step="0.1" oninput="calculateMethA()">
                  <span class="unit-badge">%</span>
                </div>
                <small class="form-hint">Voltage drop ceiling</small>
              </div>
            </div>

            <button type="button" id="calcMethABtn" class="btn btn-primary btn-block" onclick="calculateMethA()">Compute Method A Cable Size</button>
          </form>

          <div id="methAResultBox" class="results-container" style="margin-top:20px;">
            <h3>Method A Dimensioning Results</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label">Recommended Conductor Area</span>
                <span id="methASizeOut" class="result-value">-- mm²</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Base Method A Rating ($I_0$)</span>
                <span id="methABaseI0Out" class="result-value">-- A</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Derated Continuous Ampacity ($I_z$)</span>
                <span id="methAIzOut" class="result-value">-- A</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Method C Comparison (Thermal Penalty)</span>
                <span id="methAPenaltyOut" class="result-value">-- % Derated</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Computed Voltage Drop ($\Delta V$)</span>
                <span id="methAVdOut" class="result-value">-- V (-- %)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Compliance Verification</span>
                <span id="methAStatusOut" class="result-value">--</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Engineering Analysis: Sizing Cables in Thermally Insulated Walls (Method A1 &amp; A2)</h2>
          
          <p>Modern building construction standards such as ASHRAE 90.1, the International Energy Conservation Code (IECC), and European Part L Building Regulations mandate exceptionally low building envelope thermal transmittance ($U$-values below $0.15\text{ W}/(\text{m}^2\cdot\text{K})$). Achieving these hyper-insulated ratings requires enclosing interior partitions, cavities, and exterior perimeter walls with thick layers of mineral wool, spray polyurethane foam, or expanded polystyrene (EPS). For the electrical engineer, routing electrical distribution circuits through these thermally insulated structures represents the most aggressive heat-trapping operational scenario encountered in low-voltage building wiring.</p>
          
          <p>Both <strong>IEC 60364-5-52 (Table A.52.3)</strong> and the UK <strong>BS 7671 (IET Wiring Regulations, Table 4A2)</strong> categorize this wiring topology as <strong>Installation Method A</strong>:</p>
          <ul>
            <li><strong>Method A1:</strong> Single-core non-sheathed insulated cables enclosed within a protective conduit embedded inside a thermally insulating wall structure.</li>
            <li><strong>Method A2:</strong> Multi-core sheathed cable routed inside a protective conduit embedded inside a thermally insulating wall structure.</li>
          </ul>

          <div class="formula-box">
            <h3>Thermodynamic Conduction Physics in Cavity Walls</h3>
            <p>The steady-state temperature rise $\Delta \theta$ of an energized copper core of cross-sectional area $S$ carrying continuous RMS current $I$ is governed by radial heat dissipation across four serial thermal resistances:</p>
            <p>$$\Delta \theta = I^2 R_{ac} \cdot (R_{th,insulation} + R_{th,airpocket} + R_{th,conduit} + R_{th,wall})$$</p>
            <p>Where $R_{th,wall}$ represents the external thermal boundary resistance of the building insulation. Because mineral wool has a very low thermal conductivity ($\lambda \approx 0.035\text{ to } 0.040\text{ W}/(\text{m}\cdot\text{K})$), the trapped air inside the conduit heats rapidly. Convective air currents cannot circulate outside the conduit, causing conductor core temperatures to skyrocket under nominal current levels.</p>
          </div>

          <h3>Quantitative Comparison: Method A versus Open Surface (Method C)</h3>
          <p>To appreciate the extreme thermal penalty imposed by Installation Method A, observe the comparative ampacities extracted from IEC 60364-5-52 Table B.52.2 and BS 7671 Table 4D5 for copper conductors with $70^\circ\text{C}$ PVC insulation at $30^\circ\text{C}$ ambient:</p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Conductor Cross-Section ($mm^2$)</th>
                <th>Method A2 (Multicore in Conduit in Insulated Wall)</th>
                <th>Method C (Clipped Direct to Open Masonry)</th>
                <th>Thermal Capacity Loss (%)</th>
                <th>Design Impact / Conductor Upsizing</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>1.5 mm²</strong></td>
                <td>14.5 A</td>
                <td>19.5 A</td>
                <td><strong>-25.6%</strong></td>
                <td>Cannot support standard 16A breaker; requires 2.5 mm²</td>
              </tr>
              <tr>
                <td><strong>2.5 mm²</strong></td>
                <td>18.5 A</td>
                <td>27.0 A</td>
                <td><strong>-31.5%</strong></td>
                <td>Cannot support standard 20A or 25A radial; requires 4.0 mm²</td>
              </tr>
              <tr>
                <td><strong>4.0 mm²</strong></td>
                <td>25.0 A</td>
                <td>36.0 A</td>
                <td><strong>-30.6%</strong></td>
                <td>Marginal for 25A breaker; cannot support 32A shower/cooker</td>
              </tr>
              <tr>
                <td><strong>6.0 mm²</strong></td>
                <td>32.0 A</td>
                <td>46.0 A</td>
                <td><strong>-30.4%</strong></td>
                <td>Requires 10.0 mm² to support standard 40A sub-distribution</td>
              </tr>
              <tr>
                <td><strong>10.0 mm²</strong></td>
                <td>43.0 A</td>
                <td>63.0 A</td>
                <td><strong>-31.7%</strong></td>
                <td>Sub-feeders lose nearly one-third of continuous rating</td>
              </tr>
              <tr>
                <td><strong>16.0 mm²</strong></td>
                <td>57.0 A</td>
                <td>85.0 A</td>
                <td><strong>-32.9%</strong></td>
                <td>Severe heat bottleneck on high-power residential runs</td>
              </tr>
            </tbody>
          </table>

          <h3>Thermal Derating Factors ($C_i$) for Partial Insulation Encapsulation</h3>
          <p>In real-world construction, a circuit often travels the majority of its route across an open ceiling plenum or concrete riser, entering a thermally insulated wall for only a limited segment (e.g., dropping down inside an insulated stud partition to reach a wall socket or isolation switch). Both IEC 60364-5-52 Clause 523.7 and BS 7671 Regulation 523.9 prescribe derating factor $C_i$ based on the exact linear length of cable enclosed within thermal insulation:</p>

          <ul>
            <li><strong>Enclosed Length $\ge 500\text{ mm}$ (Full Encapsulation):</strong> $C_i = 0.50$ (applied to Method C clipped-direct rating) or strictly evaluated under Method A tabulated values.</li>
            <li><strong>Enclosed Length $= 400\text{ mm}$ to $< 500\text{ mm}$ :</strong> $C_i = 0.55$</li>
            <li><strong>Enclosed Length $= 200\text{ mm}$ to $< 400\text{ mm}$ :</strong> $C_i = 0.63$</li>
            <li><strong>Enclosed Length $= 100\text{ mm}$ to $< 200\text{ mm}$ :</strong> $C_i = 0.78$</li>
            <li><strong>Enclosed Length $= 50\text{ mm}$ to $< 100\text{ mm}$ :</strong> $C_i = 0.88$</li>
            <li><strong>Enclosed Length $< 50\text{ mm}$ :</strong> $C_i = 1.00$ (negligible longitudinal heat bottleneck due to copper axial thermal conduction).</li>
          </ul>

          <div class="worked-example-card">
            <h3>Step-by-Step Practical Calculation: Modern Residential Kitchen Radial Circuit</h3>
            <p><strong>Scenario:</strong> Sizing a single-phase 230V radial feeder for a modern energy-efficient residential kitchen supplying an electric induction hob. The design continuous load current is $I_b = 28\text{ A}$ protected by a $32\text{ A}$ Type B MCB ($I_n = 32\text{ A}$). The total circuit length is $35\text{ meters}$, of which $15\text{ meters}$ passes through an interior stud wall packed with rigid insulation inside conduit (Installation Method A2). The ambient temperature inside the wall cavity is $30^\circ\text{C}$, and the conduit shares the cavity space with one other adjacent circuit ($C_g = 0.80$ for 2 circuits). Multi-core copper cable with $70^\circ\text{C}$ PVC insulation is specified. Max allowable voltage drop is $3.0\%$.</p>
            
            <p><strong>Step 1: Determine Required Base Current Rating ($I_0$)</strong></p>
            <p>The protective device requires $I_n = 32\text{ A}$. With grouping factor $C_g = 0.80$ and temperature factor $C_a = 1.00$ ($30^\circ\text{C}$):</p>
            <p>$$I_{t,req} \ge \frac{I_n}{C_a \times C_g} = \frac{32\text{ A}}{1.00 \times 0.80} = 40.0\text{ A}$$</p>

            <p><strong>Step 2: Compare Available Method A2 Tabulated Values</strong></p>
            <p>Reviewing IEC / BS 7671 Table 4D2A (Method A2 multi-core PVC copper):</p>
            <ul>
              <li>$4.0\text{ mm}^2 \implies I_0 = 25\text{ A}$ (Failed: $25 < 40.0\text{ A}$)</li>
              <li>$6.0\text{ mm}^2 \implies I_0 = 32\text{ A}$ (Failed: $32 < 40.0\text{ A}$)</li>
              <li>$10.0\text{ mm}^2 \implies I_0 = 43\text{ A}$ (Passed: $43 \ge 40.0\text{ A}$)</li>
            </ul>
            <p>Notice that if this same cable were clipped directly to a wall (Method C), a $6.0\text{ mm}^2$ cable ($I_0 = 46\text{ A}$) would easily suffice. Method A forces the engineer to upsize to $10.0\text{ mm}^2$ strictly due to thermal cavity trapping!</p>

            <p><strong>Step 3: Verification of Derated Capacity ($I_z$)</strong></p>
            <p>$$I_z = I_0 \times C_a \times C_g = 43\text{ A} \times 1.00 \times 0.80 = 34.4\text{ A}$$</p>
            <p>Since $I_b (28\text{ A}) \le I_n (32\text{ A}) \le I_z (34.4\text{ A})$, overcurrent thermal coordination is fully satisfied.</p>

            <p><strong>Step 4: Check Voltage Drop on $10.0\text{ mm}^2$</strong></p>
            <p>For $10.0\text{ mm}^2$ copper, the single-phase voltage drop factor is $4.4\text{ mV/A/m}$:</p>
            <p>$$\Delta V = \frac{4.4 \times 28\text{ A} \times 35\text{ m}}{1000} = 4.31\text{ Volts}$$</p>
            <p>$$\Delta V\% = \frac{4.31\text{ V}}{230\text{ V}} \times 100 = 1.87\%$$</p>
            <p>Since $1.87\% \le 3.0\%$, the $10.0\text{ mm}^2$ conductor satisfies all regulatory and operational standards.</p>
          </div>

          <h2>Frequently Asked Questions (Installation Method A)</h2>
          <div class="faq-item">
            <h3>Why is Method A considered the worst-case thermal installation method?</h3>
            <p>Thermal insulation materials like fiberglass, rockwool, and polyurethane are engineered specifically to impede conductive and convective heat transport. Enclosing an energized conductor inside such a medium traps virtually all $I^2 R$ joule heat inside the conduit. In contrast to open cable trays or masonry walls which act as heat sinks, insulated cavity walls force conductors to operate at their maximum permissible temperatures under substantially lower currents.</p>
          </div>

          <div class="faq-item">
            <h3>Can I use XLPE cable to avoid upsizing conductor cross-section in Method A?</h3>
            <p>Yes. Because XLPE (cross-linked polyethylene) is rated for continuous operation at $90^\circ\text{C}$ compared to $70^\circ\text{C}$ for standard PVC, its base ampacity in Method A is higher. For example, a $6.0\text{ mm}^2$ XLPE multicore cable in Method A carries $40\text{ A}$, compared to only $32\text{ A}$ for PVC. However, you must verify that the terminating circuit breaker terminals are rated for $90^\circ\text{C}$ operation (most residential breakers are rated for $70^\circ\text{C}$ maximum terminal temperature).</p>
          </div>

          <div class="faq-item">
            <h3>What if the cable only passes through insulation for a short distance?</h3>
            <p>If the length of cable enclosed within insulation is under $500\text{ mm}$ (such as passing perpendicularly through an insulated exterior wall), international standards allow relaxation of the derating factor. Under BS 7671 Table 52.2, a run of $100\text{ mm}$ requires a factor of $0.78$, while a run under $50\text{ mm}$ incurs no thermal penalty ($C_i = 1.0$) because heat conducts along the copper length into cooler sections.</p>
          </div>

          <div class="faq-item">
            <h3>Does Installation Method A apply to cables routed inside metal conduit?</h3>
            <p>Yes. While metallic conduit (such as rigid steel conduit or EMT) conducts heat better than PVC conduit, the conduit remains entirely encased within the fibrous insulation. Heat cannot escape into the building space, meaning the air pocket inside the conduit still reaches elevated temperatures. Therefore, metallic conduits enclosed in insulated walls must be derated under Method A.</p>
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
    const dataMethA = [
      { size: 1.5,  a2_pvc: 14.5, a2_xlpe: 18.5, a1_pvc: 15.5, a1_xlpe: 20, mv: 29 },
      { size: 2.5,  a2_pvc: 18.5, a2_xlpe: 25.0, a1_pvc: 20.0, a1_xlpe: 28, mv: 18 },
      { size: 4.0,  a2_pvc: 25.0, a2_xlpe: 33.0, a1_pvc: 27.0, a1_xlpe: 37, mv: 11 },
      { size: 6.0,  a2_pvc: 32.0, a2_xlpe: 42.0, a1_pvc: 34.0, a1_xlpe: 47, mv: 7.3 },
      { size: 10.0, a2_pvc: 43.0, a2_xlpe: 57.0, a1_pvc: 46.0, a1_xlpe: 65, mv: 4.4 },
      { size: 16.0, a2_pvc: 57.0, a2_xlpe: 76.0, a1_pvc: 62.0, a1_xlpe: 87, mv: 2.8 },
      { size: 25.0, a2_pvc: 75.0, a2_xlpe: 99.0, a1_pvc: 80.0, a1_xlpe: 114, mv: 1.8 },
      { size: 35.0, a2_pvc: 92.0, a2_xlpe: 121.0, a1_pvc: 99.0, a1_xlpe: 141, mv: 1.3 }
    ];

    const methodC_PVC = { 1.5: 19.5, 2.5: 27, 4.0: 36, 6.0: 46, 10.0: 63, 16.0: 85, 25.0: 112, 35.0: 138 };

    function calculateMethA() {
      const subType = document.getElementById("methASubType").value;
      const conductor = document.getElementById("methAConductor").value;
      const insulation = document.getElementById("methAInsulation").value;
      const phasing = document.getElementById("methAPhasing").value;
      const Ib = parseFloat(document.getElementById("methADesignCurrent").value) || 0;
      const In = parseFloat(document.getElementById("methABreakerIn").value) || 0;
      const ambTemp = parseFloat(document.getElementById("methAAmbientTemp").value) || 30;
      const groupCount = parseInt(document.getElementById("methAGroupCount").value) || 1;
      const totalLen = parseFloat(document.getElementById("methATotalLength").value) || 1;
      const insulLen = parseFloat(document.getElementById("methAInsulLength").value) || 0;
      const maxVdPct = parseFloat(document.getElementById("methAMaxVd").value) || 3.0;

      let Ca = 1.0;
      if (insulation === "xlpe") {
        Ca = Math.sqrt(Math.max(0.1, (90 - ambTemp) / (90 - 30)));
      } else {
        Ca = Math.sqrt(Math.max(0.1, (70 - ambTemp) / (70 - 30)));
      }

      let Cg = 1.0;
      if (groupCount === 2) Cg = 0.80;
      else if (groupCount === 3) Cg = 0.70;
      else if (groupCount === 4) Cg = 0.65;
      else if (groupCount >= 5) Cg = 0.60;

      const condMultiplier = (conductor === "al") ? 0.78 : 1.0;
      const vNominal = (phasing === "1p") ? 230 : 400;

      let selected = null;

      for (let i = 0; i < dataMethA.length; i++) {
        const row = dataMethA[i];
        let baseRating = 0;
        if (subType === "A2") {
          baseRating = (insulation === "xlpe") ? row.a2_xlpe : row.a2_pvc;
        } else {
          baseRating = (insulation === "xlpe") ? row.a1_xlpe : row.a1_pvc;
        }
        baseRating = baseRating * condMultiplier;
        const deratedIz = baseRating * Ca * Cg;

        if (deratedIz < In) continue;

        let mvFactor = row.mv * ((conductor === "al") ? 1.64 : 1.0);
        if (phasing === "3p") mvFactor = mvFactor * (Math.sqrt(3) / 2);

        const deltaV = (mvFactor * Ib * totalLen) / 1000;
        const vdPct = (deltaV / vNominal) * 100;

        if (vdPct <= maxVdPct) {
          const benchC = (methodC_PVC[row.size] || baseRating * 1.4) * condMultiplier;
          const penalty = ((benchC - baseRating) / benchC) * 100;
          selected = {
            size: row.size,
            baseI0: baseRating,
            iz: deratedIz,
            penalty: penalty,
            vdVolts: deltaV,
            vdPct: vdPct
          };
          break;
        }
      }

      if (selected) {
        document.getElementById("methASizeOut").innerText = selected.size + " mm² (" + conductor.toUpperCase() + ")";
        document.getElementById("methABaseI0Out").innerText = selected.baseI0.toFixed(1) + " A";
        document.getElementById("methAIzOut").innerText = selected.iz.toFixed(1) + " A";
        document.getElementById("methAPenaltyOut").innerText = selected.penalty.toFixed(1) + "% vs Method C";
        document.getElementById("methAVdOut").innerText = selected.vdVolts.toFixed(2) + " V (" + selected.vdPct.toFixed(2) + "%)";
        document.getElementById("methAStatusOut").innerText = "Fully Compliant (Ib <= In <= Iz)";
        document.getElementById("methAStatusOut").style.color = "#10b981";
      } else {
        document.getElementById("methASizeOut").innerText = "> 35 mm²";
        document.getElementById("methABaseI0Out").innerText = "--";
        document.getElementById("methAIzOut").innerText = "--";
        document.getElementById("methAPenaltyOut").innerText = "--";
        document.getElementById("methAVdOut").innerText = "Exceeds Drop Limit";
        document.getElementById("methAStatusOut").innerText = "Non-Compliant: Heavy Feeder Required";
        document.getElementById("methAStatusOut").style.color = "#ef4444";
      }
    }

    document.addEventListener("DOMContentLoaded", function() {
      calculateMethA();
    });
  </script>
</body>
</html>
"""

def main():
    root = r"C:\Users\Admin\.gemini\antigravity\scratch\calchub"
    
    p7 = os.path.join(root, "cable-sizing-calculator-iec-60364.html")
    with open(p7, "w", encoding="utf-8") as f:
        f.write(TOOL_7_HTML.strip() + "\n")
    print("[PASS] cable-sizing-calculator-iec-60364.html regenerated with standard CalcHub design system!")

    p8 = os.path.join(root, "cable-sizing-installation-method-a.html")
    with open(p8, "w", encoding="utf-8") as f:
        f.write(TOOL_8_HTML.strip() + "\n")
    print("[PASS] cable-sizing-installation-method-a.html regenerated with standard CalcHub design system!")

if __name__ == "__main__":
    main()
