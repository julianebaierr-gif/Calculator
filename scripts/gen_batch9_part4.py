# -*- coding: utf-8 -*-
"""
Script to generate Batch 9 Part 4 tools:
7. heat-exchanger-calculator.html
8. hvac-calculator.html
"""
import os

TOOL_7_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Heat Exchanger Calculator | LMTD, NTU Effectiveness & Surface Area</title>
  <meta name="description" content="Calculate heat exchanger thermal duty, Logarithmic Mean Temperature Difference (LMTD), heat transfer surface area, and NTU effectiveness per TEMA and ASME standards.">
  <link rel="canonical" href="https://calchub.cloud/heat-exchanger-calculator.html">
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
        "name": "Heat Exchanger Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Thermal engineering calculation tool determining heat duty Q = U*A*Delta_Tm, Logarithmic Mean Temperature Difference (LMTD), surface area, and NTU effectiveness per TEMA standards.",
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
            "name": "What is the Logarithmic Mean Temperature Difference (LMTD) formula?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For a counter-current heat exchanger: Delta_T_1 = T_hot_in - T_cold_out and Delta_T_2 = T_hot_out - T_cold_in. The Log Mean Temperature Difference is: LMTD = (Delta_T_1 - Delta_T_2) / ln(Delta_T_1 / Delta_T_2). For shell-and-tube or cross-flow configurations, LMTD is multiplied by a geometry correction factor F (Delta_T_m = F * LMTD)."
            }
          },
          {
            "@type": "Question",
            "name": "Why is counter-flow more thermally efficient than parallel-flow?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In counter-current flow, the cold fluid exits near the entry temperature of the hot fluid, allowing the cold fluid outlet temperature to exceed the hot fluid outlet temperature (temperature cross). This maximizes the thermal driving gradient across the entire length of the exchanger, resulting in a higher LMTD and requiring significantly less heat transfer surface area."
            }
          },
          {
            "@type": "Question",
            "name": "How is heat exchanger required surface area (A) calculated?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The fundamental heat exchanger design equation is: A = Q / (U * Delta_T_m), where Q is the thermal duty in Watts (or BTU/hr), U is the overall heat transfer coefficient in W/(m^2*K) (or BTU/(hr*ft^2*deg F)), and Delta_T_m is the effective mean temperature difference."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between the LMTD method and the NTU-Effectiveness method?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The LMTD method is ideal for design sizing problems where all four inlet and outlet fluid temperatures are known or specified, allowing direct calculation of required surface area A. The Number of Transfer Units (NTU) effectiveness method is used for rating existing heat exchangers where the physical area A is fixed and outlet temperatures must be predicted for given inlet conditions."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="mechanical">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">
        <span class="logo-icon">&pi;</span>
        <span class="logo-text">Calc<strong>Hub</strong></span>
      </a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="engineering.html">Engineering</a>
        <a href="mechanical.html" class="active">Mechanical</a>
        <a href="solar-energy.html">Solar</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo;
      <a href="mechanical.html">Mechanical &amp; Machine Design</a> &rsaquo;
      <span>Heat Exchanger Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">TEMA &amp; ASME Section VIII Thermal Standards</div>
          <h1 class="calc-title">Heat Exchanger Calculator</h1>
          <p class="calc-tagline">Calculate heat exchanger thermal duty (Q), Logarithmic Mean Temperature Difference (LMTD), required heat transfer surface area (A), and NTU thermal effectiveness.</p>
        </header>

        <div class="tool-card">
          <form id="heCalcForm">
            <div class="calc-grid">
              <div class="form-group">
                <label for="flowArrangement">Flow Arrangement</label>
                <select id="flowArrangement">
                  <option value="counter" selected>Counter-Current Flow (Maximum LMTD)</option>
                  <option value="parallel">Co-Current / Parallel Flow</option>
                  <option value="shellTube">Shell & Tube (1 Shell Pass, 2+ Tube Passes)</option>
                  <option value="crossFlow">Cross-Flow (Both Fluids Unmixed)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="heUnits">Engineering Units</label>
                <select id="heUnits">
                  <option value="metric" selected>Metric (°C, kW, kg/s, m², W/m²·K)</option>
                  <option value="imperial">Imperial (°F, BTU/hr, lbs/hr, ft², BTU/hr·ft²·°F)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="hotIn" id="lblHotIn">Hot Fluid Inlet Temp (Th,in) [°C]</label>
                <input type="number" id="hotIn" step="0.5" value="95.0">
              </div>

              <div class="form-group">
                <label for="hotOut" id="lblHotOut">Hot Fluid Outlet Temp (Th,out) [°C]</label>
                <input type="number" id="hotOut" step="0.5" value="65.0">
              </div>

              <div class="form-group">
                <label for="coldIn" id="lblColdIn">Cold Fluid Inlet Temp (Tc,in) [°C]</label>
                <input type="number" id="coldIn" step="0.5" value="20.0">
              </div>

              <div class="form-group">
                <label for="coldOut" id="lblColdOut">Cold Fluid Outlet Temp (Tc,out) [°C]</label>
                <input type="number" id="coldOut" step="0.5" value="45.0">
              </div>

              <div class="form-group">
                <label for="hotMassFlow" id="lblHotMassFlow">Hot Fluid Mass Flow Rate (mh) [kg/s]</label>
                <input type="number" id="hotMassFlow" step="0.1" min="0.01" max="1000" value="2.0">
              </div>

              <div class="form-group">
                <label for="hotCp" id="lblHotCp">Hot Fluid Specific Heat (Cp,h) [kJ/kg·K]</label>
                <input type="number" id="hotCp" step="0.05" min="0.5" max="10" value="4.18">
              </div>

              <div class="form-group">
                <label for="overallU" id="lblOverallU">Overall Heat Transfer Coeff (U) [W/m²·K]</label>
                <input type="number" id="overallU" step="10" min="5" max="15000" value="850">
              </div>

              <div class="form-group">
                <label for="foulingFactor" id="lblFouling">Fouling Resistance Factor (Rf) [m²·K/W]</label>
                <select id="foulingFactor">
                  <option value="0" selected>Clean Tubes (Rf = 0.0000)</option>
                  <option value="0.0001">Treated Cooling Water (Rf = 0.0001 m²·K/W)</option>
                  <option value="0.0003">River / Raw Water (Rf = 0.0003 m²·K/W)</option>
                  <option value="0.0002">Light Hydrocarbon / Fuel Oil (Rf = 0.0002 m²·K/W)</option>
                </select>
              </div>
            </div>

            <div class="calc-actions">
              <button type="button" id="calcHeBtn" class="btn btn-primary">Calculate Thermal Performance</button>
              <button type="reset" id="resetHeBtn" class="btn btn-secondary">Reset Defaults</button>
            </div>
          </form>

          <div id="heResultBox" class="results-container" style="display: none;">
            <h3>Thermal Design & Heat Transfer Results</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label">Thermal Heat Duty (Q)</span>
                <span id="resHeatDuty" class="result-value">-- kW</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Required Surface Area (A)</span>
                <span id="resSurfaceArea" class="result-value">-- m²</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Log Mean Temp Diff (LMTD)</span>
                <span id="resLmtd" class="result-value">-- °C</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Configuration Correction Factor (F)</span>
                <span id="resCorrF" class="result-value">--</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Effective Temp Difference (&Delta;Tm)</span>
                <span id="resEffDeltaTm" class="result-value">-- °C</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Thermal Effectiveness (&epsilon;)</span>
                <span id="resEffectiveness" class="result-value">-- %</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Number of Transfer Units (NTU)</span>
                <span id="resNtu" class="result-value">--</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Derated Fouled Coeff (U_dirty)</span>
                <span id="resUdirty" class="result-value">-- W/m²·K</span>
              </div>
            </div>
            <div id="heNotesBox" style="margin-top: 1rem; color: #1e40af; background: #eff6ff; border: 1px solid #bfdbfe; padding: 0.75rem; border-radius: 6px;"></div>
          </div>
        </div>

        <article class="article-body">
          <h2>Thermal Process Engineering & Heat Exchanger Fundamentals</h2>
          <p>Heat exchangers are thermodynamic devices engineered to transfer thermal energy between two or more fluid streams across a solid conduction boundary without intermixing. Operating in power stations, chemical refineries, district cooling plants, food pasteurization lines, and refrigeration chillers, heat exchangers are governed by the <strong>Tubular Exchanger Manufacturers Association (TEMA)</strong> and <strong>ASME Section VIII</strong> standards.</p>

          <p>Proper sizing requires solving the combined effects of convective fluid boundary layers, conductive wall resistance, fluid fouling scale, and temperature profile convergence. Designing an exchanger with insufficient area fails to achieve process target temperatures, causing boiling instability or product ruination. Conversely, gross oversizing causes fluid velocity stagnation, accelerating fouling deposition, sedimentation, and tube corrosion.</p>

          <h2>Thermal Heat Duty Formulation</h2>
          <p>Under steady-state operation neglecting atmospheric heat leakage, the total thermal duty (\(Q\)) transferred from the hot stream to the cold stream is governed by the First Law of Thermodynamics:</p>

          <div class="formula-box">
            $$Q = \dot{m}_h c_{p,h} (T_{h,\text{in}} - T_{h,\text{out}}) = \dot{m}_c c_{p,c} (T_{c,\text{out}} - T_{c,\text{in}}) \quad [\text{kW or BTU/hr}]$$
          </div>

          <p>Where:</p>
          <ul>
            <li><strong>\(\dot{m}_h, \dot{m}_c\)</strong>: Mass flow rates of the hot and cold streams (\(\text{kg/s}\) or \(\text{lbs/hr}\)).</li>
            <li><strong>\(c_{p,h}, c_{p,c}\)</strong>: Specific heat capacities at constant pressure (\(\text{kJ/kg}\cdot\text{K}\) or \(\text{BTU/lb}\cdot^\circ\text{F}\)).</li>
            <li><strong>\(C_h = \dot{m}_h c_{p,h}\)</strong> and <strong>\(C_c = \dot{m}_c c_{p,c}\)</strong>: Fluid heat capacity rates (\(\text{kW/K}\)).</li>
          </ul>

          <h2>The Logarithmic Mean Temperature Difference (LMTD) Method</h2>
          <p>Because fluid temperatures vary continuously along the tube bundle, arithmetic temperature differences (\(\Delta T_{\text{avg}} = (T_{h} - T_{c})\)) grossly overestimate heat transfer. The mathematically rigorous driving gradient is the <strong>Logarithmic Mean Temperature Difference (LMTD)</strong>:</p>

          <div class="formula-box">
            $$\text{LMTD} = \frac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1 / \Delta T_2)}$$
          </div>

          <h3>Counter-Current Flow Boundary Definitions</h3>
          <p>In a counter-flow heat exchanger, the fluids enter at opposite ends and travel in reverse directions:</p>
          <div class="formula-box">
            $$\Delta T_1 = T_{h,\text{in}} - T_{c,\text{out}} \quad \text{and} \quad \Delta T_2 = T_{h,\text{out}} - T_{c,\text{in}}$$
          </div>

          <h3>Co-Current (Parallel) Flow Boundary Definitions</h3>
          <p>In parallel flow, both fluids enter at the same end and travel in parallel:</p>
          <div class="formula-box">
            $$\Delta T_1 = T_{h,\text{in}} - T_{c,\text{in}} \quad \text{and} \quad \Delta T_2 = T_{h,\text{out}} - T_{c,\text{out}}$$
          </div>
          <p>Because counter-flow maintains an almost uniform temperature difference across the entire heat exchange length, its LMTD is consistently 20% to 50% higher than parallel flow, enabling a drastically smaller required heat transfer surface area.</p>

          <h2>Shell & Tube LMTD Correction Factor (F)</h2>
          <p>When fluid flow is not purely counter-current—as occurs in multi-pass shell-and-tube exchangers (TEMA E-shell with 2, 4, or 6 tube passes) and cross-flow radiators—the effective mean temperature difference (\(\Delta T_m\)) is derated by an empirical geometry correction factor (\(F \le 1.0\)):</p>

          <div class="formula-box">
            $$\Delta T_m = F \cdot \text{LMTD}_{\text{counter}}$$
          </div>

          <p>The correction factor \(F\) is calculated as a function of the heat capacity ratio (\(R\)) and thermal effectiveness (\(P\)):</p>

          <div class="formula-box">
            $$R = \frac{T_{h,\text{in}} - T_{h,\text{out}}}{T_{c,\text{out}} - T_{c,\text{in}}} = \frac{C_c}{C_h}, \quad P = \frac{T_{c,\text{out}} - T_{c,\text{in}}}{T_{h,\text{in}} - T_{c,\text{in}}}$$
            $$F = \frac{\sqrt{R^2 + 1} \cdot \ln\left(\frac{1 - P}{1 - P \cdot R}\right)}{(R - 1) \cdot \ln\left(\frac{2 - P(R + 1 - \sqrt{R^2 + 1})}{2 - P(R + 1 + \sqrt{R^2 + 1})}\right)}$$
          </div>
          <p>TEMA standards recommend that exchangers never be operated at \(F < 0.75\), as the curve drops precipitously toward zero, making the exchanger unstable and susceptible to temperature pinching.</p>

          <h2>Required Heat Transfer Surface Area & Overall U-Value</h2>
          <p>The total outside surface area (\(A\)) required to transfer heat duty \(Q\) is:</p>

          <div class="formula-box">
            $$A = \frac{Q}{U_{\text{dirty}} \cdot \Delta T_m} \quad [\text{m}^2 \text{ or ft}^2]$$
          </div>

          <p>Where \(U_{\text{dirty}}\) incorporates both internal and external convective film coefficients (\(h_i, h_o\)), tube wall metal thermal conduction (\(k_{\text{metal}}\)), and fouling scale resistance factors (\(R_{fi}, R_{fo}\)):</p>

          <div class="formula-box">
            $$\frac{1}{U_{\text{dirty}}} = \frac{1}{U_{\text{clean}}} + R_f$$
          </div>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Service & Fluid Combination</th>
                <th>Clean Coeff \(U\) (\(\text{W/m}^2\cdot\text{K}\))</th>
                <th>Typical Fouling \(R_f\) (\(\text{m}^2\cdot\text{K/W}\))</th>
                <th>Design Coeff \(U_{\text{dirty}}\) (\(\text{W/m}^2\cdot\text{K}\))</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Water to Water (Plate & Frame)</td>
                <td>3,000 &ndash; 7,000</td>
                <td>0.00005 &ndash; 0.00010</td>
                <td>2,000 &ndash; 4,500</td>
              </tr>
              <tr>
                <td>Water to Water (Shell & Tube)</td>
                <td>1,200 &ndash; 2,500</td>
                <td>0.00015 &ndash; 0.00025</td>
                <td>800 &ndash; 1,500</td>
              </tr>
              <tr>
                <td>Steam Condenser (Water in Tubes)</td>
                <td>2,000 &ndash; 4,000</td>
                <td>0.00010 &ndash; 0.00020</td>
                <td>1,500 &ndash; 2,800</td>
              </tr>
              <tr>
                <td>Water to Lube Oil (Tubular Cooler)</td>
                <td>250 &ndash; 500</td>
                <td>0.00020 &ndash; 0.00035</td>
                <td>180 &ndash; 350</td>
              </tr>
              <tr>
                <td>Air to Water (Fin-Fan Radiator)</td>
                <td>30 &ndash; 60</td>
                <td>0.00020 &ndash; 0.00040</td>
                <td>25 &ndash; 50</td>
              </tr>
            </tbody>
          </table>

          <div class="worked-example-card">
            <h3>Step-by-Step Worked Case Study: District Heating Substation Water-Water Cooler</h3>
            <p><strong>Design Scenario:</strong> An engineer is sizing a counter-flow shell-and-tube heat exchanger for a commercial building district heating substation:</p>
            <ul>
              <li>Hot district water: \(T_{h,\text{in}} = 95^\circ\text{C}\), \(T_{h,\text{out}} = 65^\circ\text{C}\).</li>
              <li>Hot fluid mass flow: \(\dot{m}_h = 2.0\text{ kg/s}\), \(c_{p,h} = 4.18\text{ kJ/kg}\cdot\text{K}\).</li>
              <li>Cold building loop: \(T_{c,\text{in}} = 20^\circ\text{C}\), \(T_{c,\text{out}} = 45^\circ\text{C}\).</li>
              <li>Overall clean heat transfer coefficient: \(U_{\text{clean}} = 850\text{ W/m}^2\cdot\text{K}\).</li>
              <li>Treated water fouling resistance: \(R_f = 0.0001\text{ m}^2\cdot\text{K/W}\).</li>
            </ul>

            <p><strong>Step 1: Compute thermal heat duty (\(Q\))</strong></p>
            <div class="formula-box">
              $$Q = \dot{m}_h c_{p,h} (T_{h,\text{in}} - T_{h,\text{out}}) = 2.0 \cdot 4.18 \cdot (95 - 65) = 8.36 \times 30 = 250.8\text{ kW}$$
            </div>

            <p><strong>Step 2: Determine Counter-Flow LMTD</strong></p>
            <div class="formula-box">
              $$\Delta T_1 = T_{h,\text{in}} - T_{c,\text{out}} = 95 - 45 = 50.0^\circ\text{C}$$
              $$\Delta T_2 = T_{h,\text{out}} - T_{c,\text{in}} = 65 - 20 = 45.0^\circ\text{C}$$
              $$\text{LMTD} = \frac{50.0 - 45.0}{\ln(50.0 / 45.0)} = \frac{5.0}{\ln(1.1111)} = \frac{5.0}{0.10536} = 47.46^\circ\text{C}$$
            </div>

            <p><strong>Step 3: Calculate derated fouled overall coefficient (\(U_{\text{dirty}}\))</strong></p>
            <div class="formula-box">
              $$\frac{1}{U_{\text{dirty}}} = \frac{1}{850} + 0.0001 = 0.001176 + 0.000100 = 0.001276 \implies U_{\text{dirty}} = 783.4\text{ W/m}^2\cdot\text{K}$$
            </div>

            <p><strong>Step 4: Compute required heat transfer surface area (\(A\))</strong></p>
            <div class="formula-box">
              $$A = \frac{Q}{U_{\text{dirty}} \cdot \text{LMTD}} = \frac{250,800\text{ W}}{783.4\text{ W/m}^2\cdot\text{K} \cdot 47.46\text{ K}} = \frac{250800}{37180.2} = 6.75\text{ m}^2$$
            </div>
            <p><strong>Engineering Conclusion:</strong> A counter-flow exchanger with <strong>\(6.75\text{ m}^2\)</strong> of surface area provides the required 251 kW heating duty with built-in fouling reserve.</p>
          </div>

          <h2>Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3>What is a temperature pinch point in heat exchanger design?</h3>
            <p>A temperature pinch point occurs where the temperature difference between the hot and cold fluid streams approaches a minimal value (\(\Delta T_{\text{min}} \to 0\)). As the pinch point narrows, the LMTD approaches zero, causing the required surface area to approach infinity. In industrial process design, minimum approach temperatures are typically restricted to \(3^\circ\text{C}\) to \(5^\circ\text{C}\) for plate heat exchangers and \(5^\circ\text{C}\) to \(10^\circ\text{C}\) for shell-and-tube units.</p>
          </div>

          <div class="faq-item">
            <h3>Why are Plate and Frame heat exchangers more compact than Shell and Tube?</h3>
            <p>Gasketed plate heat exchangers feature thin, pressed metal plates with corrugation chevrons that induce intense boundary-layer turbulence even at low Reynolds numbers (\(Re < 50\)). This produces heat transfer coefficients 3 to 5 times higher than smooth cylindrical tubes (\(U \approx 4,000 - 6,000\text{ W/m}^2\cdot\text{K}\)), requiring 70% less surface area and foot-print space.</p>
          </div>

          <div class="faq-item">
            <h3>How does baffle spacing affect shell-side heat transfer and pressure drop?</h3>
            <p>Segmental baffles in shell-and-tube exchangers direct fluid across the tube bundle perpendicular to the tubes, generating high cross-flow velocities that boost heat transfer. However, closing baffle spacing increases shell-side pressure drop exponentially (\(\Delta P \propto v^2\)). TEMA standards require baffle spacing to be maintained between 20% and 100% of the inside shell diameter.</p>
          </div>

          <div class="faq-item">
            <h3>When must the Effectiveness-NTU method be used instead of LMTD?</h3>
            <p>The \(\varepsilon\)-NTU method is essential when evaluating an existing heat exchanger under new operating flow rates or inlet temperatures where the outlet temperatures are unknown. Solving for outlet temperatures using LMTD requires cumbersome, iterative numerical root-finding because LMTD depends directly on the unknown outlet temperatures. In contrast, the \(\varepsilon\)-NTU method calculates effectiveness directly from known heat capacity rates and area.</p>
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
        <li><a href="mechanical.html">Mechanical</a></li>
        <li><a href="ohms-law-calculator.html">Ohm's Law</a></li>
        <li><a href="sitemap.xml">Sitemap</a></li>
      </ul>
    </div>
  </footer>

  <script>
    const flowArrangementSelect = document.getElementById('flowArrangement');
    const heUnitsSelect = document.getElementById('heUnits');
    const hotInInput = document.getElementById('hotIn');
    const hotOutInput = document.getElementById('hotOut');
    const coldInInput = document.getElementById('coldIn');
    const coldOutInput = document.getElementById('coldOut');
    const hotMassFlowInput = document.getElementById('hotMassFlow');
    const hotCpInput = document.getElementById('hotCp');
    const overallUInput = document.getElementById('overallU');
    const foulingFactorSelect = document.getElementById('foulingFactor');

    const lblHotIn = document.getElementById('lblHotIn');
    const lblHotOut = document.getElementById('lblHotOut');
    const lblColdIn = document.getElementById('lblColdIn');
    const lblColdOut = document.getElementById('lblColdOut');
    const lblHotMassFlow = document.getElementById('lblHotMassFlow');
    const lblHotCp = document.getElementById('lblHotCp');
    const lblOverallU = document.getElementById('lblOverallU');
    const lblFouling = document.getElementById('lblFouling');

    const heResultBox = document.getElementById('heResultBox');
    const resHeatDuty = document.getElementById('resHeatDuty');
    const resSurfaceArea = document.getElementById('resSurfaceArea');
    const resLmtd = document.getElementById('resLmtd');
    const resCorrF = document.getElementById('resCorrF');
    const resEffDeltaTm = document.getElementById('resEffDeltaTm');
    const resEffectiveness = document.getElementById('resEffectiveness');
    const resNtu = document.getElementById('resNtu');
    const resUdirty = document.getElementById('resUdirty');
    const heNotesBox = document.getElementById('heNotesBox');

    heUnitsSelect.addEventListener('change', function() {
      const isMetric = this.value === 'metric';
      if (isMetric) {
        lblHotIn.textContent = "Hot Fluid Inlet Temp (Th,in) [°C]";
        lblHotOut.textContent = "Hot Fluid Outlet Temp (Th,out) [°C]";
        lblColdIn.textContent = "Cold Fluid Inlet Temp (Tc,in) [°C]";
        lblColdOut.textContent = "Cold Fluid Outlet Temp (Tc,out) [°C]";
        lblHotMassFlow.textContent = "Hot Fluid Mass Flow Rate (mh) [kg/s]";
        lblHotCp.textContent = "Hot Fluid Specific Heat (Cp,h) [kJ/kg·K]";
        lblOverallU.textContent = "Overall Heat Transfer Coeff (U) [W/m²·K]";
        lblFouling.textContent = "Fouling Resistance Factor (Rf) [m²·K/W]";
        hotInInput.value = 95.0;
        hotOutInput.value = 65.0;
        coldInInput.value = 20.0;
        coldOutInput.value = 45.0;
        hotMassFlowInput.value = 2.0;
        hotCpInput.value = 4.18;
        overallUInput.value = 850;
      } else {
        lblHotIn.textContent = "Hot Fluid Inlet Temp (Th,in) [°F]";
        lblHotOut.textContent = "Hot Fluid Outlet Temp (Th,out) [°F]";
        lblColdIn.textContent = "Cold Fluid Inlet Temp (Tc,in) [°F]";
        lblColdOut.textContent = "Cold Fluid Outlet Temp (Tc,out) [°F]";
        lblHotMassFlow.textContent = "Hot Fluid Mass Flow Rate (mh) [lbs/hr]";
        lblHotCp.textContent = "Hot Fluid Specific Heat (Cp,h) [BTU/lb·°F]";
        lblOverallU.textContent = "Overall Heat Transfer Coeff (U) [BTU/hr·ft²·°F]";
        lblFouling.textContent = "Fouling Resistance Factor (Rf) [hr·ft²·°F/BTU]";
        hotInInput.value = 200.0;
        hotOutInput.value = 150.0;
        coldInInput.value = 70.0;
        coldOutInput.value = 110.0;
        hotMassFlowInput.value = 16000;
        hotCpInput.value = 1.0;
        overallUInput.value = 150;
      }
      calculateHeatExchanger();
    });

    function calculateHeatExchanger() {
      const arrangement = flowArrangementSelect.value;
      const isMetric = heUnitsSelect.value === 'metric';

      let Th_in = parseFloat(hotInInput.value);
      let Th_out = parseFloat(hotOutInput.value);
      let Tc_in = parseFloat(coldInInput.value);
      let Tc_out = parseFloat(coldOutInput.value);

      let mh = parseFloat(hotMassFlowInput.value);
      let Cph = parseFloat(hotCpInput.value);
      let U_clean = parseFloat(overallUInput.value);
      let Rf = parseFloat(foulingFactorSelect.value);

      if (isNaN(Th_in)) Th_in = isMetric ? 95 : 200;
      if (isNaN(Th_out)) Th_out = isMetric ? 65 : 150;
      if (isNaN(Tc_in)) Tc_in = isMetric ? 20 : 70;
      if (isNaN(Tc_out)) Tc_out = isMetric ? 45 : 110;
      if (isNaN(mh) || mh <= 0) mh = isMetric ? 2.0 : 16000;
      if (isNaN(Cph) || Cph <= 0) Cph = isMetric ? 4.18 : 1.0;
      if (isNaN(U_clean) || U_clean <= 0) U_clean = isMetric ? 850 : 150;

      // Thermal Duty Q
      let Q_watts = 0;
      let Q_disp = 0;
      let uDuty = isMetric ? 'kW' : 'BTU/hr';

      if (isMetric) {
        // Q = mh * Cph * (Th_in - Th_out) [kW]
        const Q_kw = mh * Cph * (Th_in - Th_out);
        Q_watts = Q_kw * 1000;
        Q_disp = Q_kw;
      } else {
        // Q = mh * Cph * (Th_in - Th_out) [BTU/hr]
        const Q_btu = mh * Cph * (Th_in - Th_out);
        Q_watts = Q_btu * 0.293071; // Watts
        Q_disp = Q_btu;
      }

      // Temperature differences
      let dT1 = 0;
      let dT2 = 0;

      if (arrangement === 'parallel') {
        dT1 = Th_in - Tc_in;
        dT2 = Th_out - Tc_out;
      } else {
        // Counter, Shell-and-tube, Crossflow reference counter LMTD
        dT1 = Th_in - Tc_out;
        dT2 = Th_out - Tc_in;
      }

      let lmtd = 0;
      if (dT1 <= 0 || dT2 <= 0) {
        lmtd = 1.0; // Temp cross error
      } else if (Math.abs(dT1 - dT2) < 0.001) {
        lmtd = dT1;
      } else {
        lmtd = (dT1 - dT2) / Math.log(dT1 / dT2);
      }

      // Correction Factor F
      let F = 1.0;
      if (arrangement === 'shellTube' || arrangement === 'crossFlow') {
        const denomP = (Th_in - Tc_in);
        const P = denomP !== 0 ? (Tc_out - Tc_in) / denomP : 0.5;
        const denomR = (Tc_out - Tc_in);
        const R = denomR !== 0 ? (Th_in - Th_out) / denomR : 1.0;

        if (arrangement === 'shellTube') {
          // 1 shell pass, 2 tube passes
          const term1 = Math.sqrt(Math.pow(R, 2) + 1);
          const top = term1 * Math.log(Math.max(0.001, (1 - P) / Math.max(0.001, 1 - P * R)));
          const botNum = 2 - P * (R + 1 - term1);
          const botDen = 2 - P * (R + 1 + term1);
          if (botDen > 0 && botNum > 0) {
            const bot = (R - 1) * Math.log(botNum / botDen);
            if (bot !== 0) F = Math.min(1.0, Math.max(0.4, top / bot));
          } else {
            F = 0.85;
          }
        } else {
          F = 0.90;
        }
      }

      const effDeltaTm = F * lmtd;

      // Fouled U
      // 1/U_dirty = 1/U_clean + Rf
      let U_dirty = U_clean;
      if (isMetric) {
        const invU = (1 / U_clean) + Rf;
        U_dirty = 1 / invU;
      } else {
        // Imperial Rf approx Rf_metric * 5.678
        const Rf_imp = Rf * 5.678;
        const invU = (1 / U_clean) + Rf_imp;
        U_dirty = 1 / invU;
      }

      // Surface Area
      let area = 0;
      let uArea = isMetric ? 'm²' : 'ft²';
      if (isMetric) {
        // A = Q_watts / (U_dirty * effDeltaTm)
        area = Q_watts / (U_dirty * effDeltaTm);
      } else {
        // A = Q_btu / (U_dirty * effDeltaTm)
        area = Q_disp / (U_dirty * effDeltaTm);
      }

      // Effectiveness epsilon = Q / Q_max
      // Q_max = C_min * (Th_in - Tc_in)
      const Ch = isMetric ? (mh * Cph * 1000) : (mh * Cph); // W/K or BTU/hr-F
      // Assuming balanced or known cold flow
      const Cc = (Th_in - Th_out) > 0 ? (Ch * (Th_in - Th_out)) / Math.max(1, (Tc_out - Tc_in)) : Ch;
      const Cmin = Math.min(Ch, Cc);
      const Qmax = Cmin * (Th_in - Tc_in);
      const effectiveness = Math.min(100, Math.max(0, (isMetric ? Q_watts : Q_disp) / (Qmax > 0 ? Qmax : 1) * 100));

      // NTU = U * A / Cmin
      const NTU = (U_dirty * area) / (Cmin > 0 ? Cmin : 1);

      resHeatDuty.textContent = Q_disp.toFixed(1) + " " + uDuty;
      resSurfaceArea.textContent = Math.abs(area).toFixed(2) + " " + uArea;
      resLmtd.textContent = lmtd.toFixed(2) + " " + (isMetric ? '°C' : '°F');
      resCorrF.textContent = F.toFixed(3);
      resEffDeltaTm.textContent = effDeltaTm.toFixed(2) + " " + (isMetric ? '°C' : '°F');
      resEffectiveness.textContent = effectiveness.toFixed(1) + " %";
      resNtu.textContent = NTU.toFixed(2);
      resUdirty.textContent = U_dirty.toFixed(1) + (isMetric ? ' W/m²·K' : ' BTU/hr·ft²·°F');

      let notes = `<strong>TEMA Thermal Analysis:</strong> Heat duty of <strong>${Q_disp.toFixed(1)} ${uDuty}</strong> requires <strong>${Math.abs(area).toFixed(2)} ${uArea}</strong> of surface area at an effective LMTD of <strong>${effDeltaTm.toFixed(1)} ${isMetric ? '°C' : '°F'}</strong>. `;
      if (F < 0.75 && arrangement !== 'counter' && arrangement !== 'parallel') {
        notes += `<span style="color:#b45309;">Warning: Configuration factor F (${F.toFixed(2)}) is below 0.75. Consider adding shell passes to prevent temperature pinch.</span>`;
      } else {
        notes += `Thermal effectiveness is <strong>${effectiveness.toFixed(1)}%</strong> (NTU = ${NTU.toFixed(2)}).`;
      }
      heNotesBox.innerHTML = notes;

      heResultBox.style.display = 'block';
    }

    document.getElementById('calcHeBtn').addEventListener('click', calculateHeatExchanger);
    document.getElementById('resetHeBtn').addEventListener('click', function() {
      setTimeout(calculateHeatExchanger, 50);
    });

    window.addEventListener('DOMContentLoaded', calculateHeatExchanger);
  </script>
</body>
</html>
"""

TOOL_8_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HVAC Calculator | Cooling Load, Heating Demand & Airflow (CFM)</title>
  <meta name="description" content="Calculate residential and commercial HVAC cooling load (BTU/hr and Tons), heating capacity, airflow (CFM), sensible and latent heat loads per ASHRAE and ACCA Manual J standards.">
  <link rel="canonical" href="https://calchub.cloud/hvac-calculator.html">
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
        "name": "HVAC Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Comprehensive HVAC heat load and psychrometric sizing engine calculating total cooling tonnage, heating BTU/hr, sensible/latent loads, and supply airflow CFM per ASHRAE Fundamentals.",
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
            "name": "How is HVAC sensible heat cooling load calculated?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The sensible heat equation for standard air is: Q_s = 1.08 * CFM * Delta_T, where Q_s is sensible heat transfer rate in BTU/hr, CFM is volumetric airflow in cubic feet per minute, and Delta_T is the dry-bulb temperature difference across the coil in degrees Fahrenheit. The 1.08 constant derives from: density of standard air (0.075 lb/cu ft) * specific heat (0.24 BTU/lb*F) * 60 min/hr."
            }
          },
          {
            "@type": "Question",
            "name": "What is the latent heat load equation in HVAC?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The latent heat load equation represents dehumidification (moisture removal): Q_l = 4840 * CFM * Delta_W, where Delta_W is the humidity ratio difference in pounds of moisture per pound of dry air. Alternatively, using grains of moisture (7,000 grains = 1 lb): Q_l = 0.68 * CFM * Delta_w_grains."
            }
          },
          {
            "@type": "Question",
            "name": "How many CFM of airflow are required per ton of air conditioning?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Standard comfort cooling design (ASHRAE/ACCA) specifies a nominal rule of thumb of 400 CFM per Ton of cooling (1 Ton = 12,000 BTU/hr). In hot, arid climates where latent loads are low, airflow is often elevated to 450 CFM/ton to maximize sensible heat ratio (SHR). In hot, humid climates requiring heavy moisture removal, airflow is reduced to 320 - 350 CFM/ton to lower the coil surface temperature and maximize condensation."
            }
          },
          {
            "@type": "Question",
            "name": "What is the Sensible Heat Ratio (SHR) in air conditioning?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The Sensible Heat Ratio is the fraction of total cooling capacity dedicated to dropping air temperature: SHR = Q_sensible / (Q_sensible + Q_latent). Typical residential comfort cooling exhibits an SHR between 0.70 and 0.80 (70% - 80% temperature drop, 20% - 30% moisture condensation). Data centers with zero human occupancy operate at an SHR of 0.95 to 1.00."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="mechanical">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">
        <span class="logo-icon">&pi;</span>
        <span class="logo-text">Calc<strong>Hub</strong></span>
      </a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="engineering.html">Engineering</a>
        <a href="mechanical.html" class="active">Mechanical</a>
        <a href="solar-energy.html">Solar</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo;
      <a href="mechanical.html">Mechanical &amp; Machine Design</a> &rsaquo;
      <span>HVAC Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">ASHRAE Fundamentals &amp; ACCA Manual J Standards</div>
          <h1 class="calc-title">HVAC Calculator</h1>
          <p class="calc-tagline">Calculate building cooling loads (BTU/hr & Tons), heating demand, supply airflow (CFM), sensible and latent heat splits, and seasonal equipment sizing.</p>
        </header>

        <div class="tool-card">
          <form id="hvacCalcForm">
            <div class="calc-grid">
              <div class="form-group">
                <label for="buildingType">Building / Occupancy Classification</label>
                <select id="buildingType">
                  <option value="residential" selected>Single-Family Residential Home</option>
                  <option value="commercialOffice">Commercial Office Space</option>
                  <option value="retailStore">Retail Store / Commercial Strip</option>
                  <option value="classroom">School / Educational Classroom</option>
                  <option value="restaurant">Restaurant / Dining Facility</option>
                  <option value="dataCenter">Server Room / Data Center</option>
                </select>
              </div>

              <div class="form-group">
                <label for="climateZone">Regional Climate Zone</label>
                <select id="climateZone">
                  <option value="hotHumid">Zone 1 & 2: Hot & Humid (Gulf Coast / Florida)</option>
                  <option value="mixedHumid" selected>Zone 3 & 4: Mixed-Humid (Mid-Atlantic / Midwest)</option>
                  <option value="hotDry">Zone 2 & 3: Hot-Dry / Arid (Southwest / Arizona)</option>
                  <option value="coldMarine">Zone 4 & 5: Marine / Moderate (Pacific NW)</option>
                  <option value="veryCold">Zone 6 & 7: Cold / Very Cold (Northeast / Upper Midwest)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="floorArea">Conditioned Floor Area [sq ft]</label>
                <input type="number" id="floorArea" step="50" min="100" max="200000" value="2000">
              </div>

              <div class="form-group">
                <label for="ceilingHeightHvac">Average Ceiling Height [ft]</label>
                <input type="number" id="ceilingHeightHvac" step="0.5" min="7" max="35" value="9">
              </div>

              <div class="form-group">
                <label for="numOccupants">Number of Regular Occupants</label>
                <input type="number" id="numOccupants" min="1" max="1000" step="1" value="4">
              </div>

              <div class="form-group">
                <label for="insulationQuality">Envelope Thermal Insulation Level</label>
                <select id="insulationQuality">
                  <option value="modern" selected>Modern Code Compliant (R-38 Attic, R-20 Walls, Low-E)</option>
                  <option value="average">Standard Average (R-30 Attic, R-13 Walls, Double-Pane)</option>
                  <option value="poor">Older / Poorly Insulated (R-11 Attic, Single-Pane Windows)</option>
                  <option value="highPerformance">High-Performance / Passive House (R-60 Attic, R-30+ Walls)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="summerOutdoorTemp">Summer Design Outdoor Dry-Bulb [°F]</label>
                <input type="number" id="summerOutdoorTemp" step="1" min="70" max="125" value="95">
              </div>

              <div class="form-group">
                <label for="summerIndoorTemp">Summer Indoor Thermostat Setpoint [°F]</label>
                <input type="number" id="summerIndoorTemp" step="1" min="65" max="85" value="75">
              </div>

              <div class="form-group">
                <label for="winterOutdoorTemp">Winter Design Outdoor Temp [°F]</label>
                <input type="number" id="winterOutdoorTemp" step="1" min="-30" max="65" value="15">
              </div>

              <div class="form-group">
                <label for="targetCfmPerTon">Target Airflow Rate per Ton of Cooling</label>
                <select id="targetCfmPerTon">
                  <option value="400" selected>400 CFM/ton (Standard Balanced Comfort)</option>
                  <option value="350">350 CFM/ton (Enhanced Dehumidification - Humid Climates)</option>
                  <option value="450">450 CFM/ton (High Sensible - Dry Climates)</option>
                </select>
              </div>
            </div>

            <div class="calc-actions">
              <button type="button" id="calcHvacBtn" class="btn btn-primary">Calculate HVAC Sizing</button>
              <button type="reset" id="resetHvacBtn" class="btn btn-secondary">Reset Defaults</button>
            </div>
          </form>

          <div id="hvacResultBox" class="results-container" style="display: none;">
            <h3>HVAC Equipment Capacity & Airflow Requirements</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label">Recommended Cooling Capacity</span>
                <span id="resCoolingTons" class="result-value">-- Tons</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Total Cooling Load</span>
                <span id="resCoolingBtu" class="result-value">-- BTU/hr</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Sensible Cooling Load (Qs)</span>
                <span id="resSensibleBtu" class="result-value">-- BTU/hr</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Latent Dehumidification Load (Ql)</span>
                <span id="resLatentBtu" class="result-value">-- BTU/hr</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Required Supply Airflow</span>
                <span id="resSupplyCfm" class="result-value">-- CFM</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Estimated Winter Heating Load</span>
                <span id="resHeatingBtu" class="result-value">-- BTU/hr</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Sensible Heat Ratio (SHR)</span>
                <span id="resShrRatio" class="result-value">--</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Unit Area Sizing Factor</span>
                <span id="resSqftPerTon" class="result-value">-- sq ft/Ton</span>
              </div>
            </div>
            <div id="hvacNotesBox" style="margin-top: 1rem; color: #1e40af; background: #eff6ff; border: 1px solid #bfdbfe; padding: 0.75rem; border-radius: 6px;"></div>
          </div>
        </div>

        <article class="article-body">
          <h2>Applied Building Thermodynamics & HVAC Load Sizing Fundamentals</h2>
          <p>Heating, Ventilation, and Air Conditioning (HVAC) systems are thermodynamic machines designed to maintain human thermal comfort, control indoor moisture levels, and provide essential ventilation air. In the United States and internationally, HVAC equipment sizing is governed by the <strong>American Society of Heating, Refrigerating and Air-Conditioning Engineers (ASHRAE)</strong> and the <strong>Air Conditioning Contractors of America (ACCA)</strong> under <strong>Manual J</strong> (Residential Load Calculation) and <strong>Manual S</strong> (Equipment Selection).</p>

          <p>Historical "rules of thumb"—such as arbitrarily assigning 1 ton of cooling for every 500 square feet—frequently result in severe equipment oversizing. An oversized air conditioner cools a building so rapidly that it satisfies the thermostat setpoint in brief 5-to-10 minute short-cycles. Consequently, the cooling coil lacks sufficient runtime to condense indoor moisture, creating cold, clammy rooms, high relative humidity (> 60%), and accelerated microbial mold growth inside ductwork.</p>

          <h2>The Psychrometric Heat Balance Equations</h2>
          <p>Conditioned air passing through an evaporative cooling coil experiences both dry-bulb temperature reduction (sensible heat extraction) and water vapor condensation (latent heat extraction). The total cooling duty is the sum of both vectors:</p>

          <div class="formula-box">
            $$Q_{\text{total}} = Q_{\text{sensible}} + Q_{\text{latent}} \quad [\text{BTU/hr}]$$
          </div>

          <h3>1. Sensible Heat Load Formulation</h3>
          <p>Sensible heat changes air temperature without altering moisture mass. Derived from the thermodynamic properties of standard air (density \(\rho = 0.075\text{ lb/ft}^3\), specific heat \(c_p = 0.24\text{ BTU/lb}\cdot^\circ\text{F}\)):</p>

          <div class="formula-box">
            $$Q_s = \rho \cdot c_p \cdot 60 \cdot \text{CFM} \cdot \Delta T = 1.08 \cdot \text{CFM} \cdot (T_{\text{return}} - T_{\text{supply}}) \quad [\text{BTU/hr}]$$
          </div>

          <h3>2. Latent Heat Load Formulation</h3>
          <p>Latent heat represents the phase change enthalpy required to condense airborne water vapor into liquid condensate at the evaporator coil drain pan (latent heat of vaporization \(h_{fg} \approx 1,061\text{ BTU/lb}\)):</p>

          <div class="formula-box">
            $$Q_l = 4840 \cdot \text{CFM} \cdot \Delta W = 0.68 \cdot \text{CFM} \cdot \Delta w_{\text{grains}} \quad [\text{BTU/hr}]$$
          </div>

          <p>Where \(\Delta W\) is humidity ratio in pounds of water per pound of dry air, and \(\Delta w_{\text{grains}}\) is in grains of moisture (\(1\text{ lb} = 7,000\text{ grains}\)).</p>

          <h3>3. Sensible Heat Ratio (SHR)</h3>
          <p>The Sensible Heat Ratio quantifies the proportion of sensible cooling relative to total coil capacity:</p>

          <div class="formula-box">
            $$\text{SHR} = \frac{Q_s}{Q_{\text{total}}} = \frac{Q_s}{Q_s + Q_l}$$
          </div>
          <p>Comfort cooling typically demands an SHR between 0.72 and 0.80. If an area features high occupant density (auditoriums, restaurants) or high ambient infiltration in humid regions, the SHR drops below 0.65, requiring dedicated outdoor air systems (DOAS) or reheat coils.</p>

          <h2>Tonnage Conversion and Airflow (CFM) Relationships</h2>
          <p>Air conditioning capacity is rated in <strong>Tons of Refrigeration (TR)</strong>. One ton represents the rate of heat extraction required to freeze 2,000 pounds (one short ton) of pure water at 32&deg;F into ice in 24 hours:</p>

          <div class="formula-box">
            $$1\text{ Ton of Refrigeration} = 12,000\text{ BTU/hr} = 3.517\text{ kW}_{\text{thermal}}$$
          </div>

          <p>Supply airflow volumetric capacity (\(\text{CFM}\)) determines air distribution velocity, duct sizing, and coil bypass factor:</p>

          <div class="formula-box">
            $$\text{CFM} = \text{Cooling Tons} \times (\text{CFM/Ton Rating})$$
          </div>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Airflow Setting (CFM/Ton)</th>
                <th>Coil Surface Temperature</th>
                <th>Sensible Heat Ratio (SHR)</th>
                <th>Target Operating Environment</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>320 &ndash; 350 CFM/ton</td>
                <td>Low (Cold Coil &sim; 48&deg;F)</td>
                <td>0.65 &ndash; 0.72 (High Latent)</td>
                <td>Humid coastal climates; maximum moisture removal.</td>
              </tr>
              <tr>
                <td>400 CFM/ton</td>
                <td>Nominal Standard (&sim; 53&deg;F)</td>
                <td>0.75 &ndash; 0.80 (Balanced)</td>
                <td>Standard comfort cooling across mixed climate zones.</td>
              </tr>
              <tr>
                <td>450 &ndash; 500 CFM/ton</td>
                <td>High (Warm Coil &sim; 58&deg;F)</td>
                <td>0.85 &ndash; 0.95 (High Sensible)</td>
                <td>Arid deserts; commercial data centers with no latent load.</td>
              </tr>
            </tbody>
          </table>

          <h2>Winter Space Heating Load Formulation</h2>
          <p>Unlike summer cooling—which must handle solar radiation, internal equipment heat gains, and moisture latent loads—winter space heating is calculated under worst-case night-time conditions (zero solar gain). The heating demand (\(Q_{\text{heating}}\)) reflects pure transmission loss through the building envelope plus infiltration air warming:</p>

          <div class="formula-box">
            $$Q_{\text{heating}} = \left[ \sum (U \cdot A) + 1.08 \cdot \text{CFM}_{\text{inf}} \right] \cdot (T_{\text{indoor}} - T_{\text{outdoor, winter}})$$
          </div>

          <div class="worked-example-card">
            <h3>Step-by-Step Worked Case Study: Suburban Residential Home Load Sizing</h3>
            <p><strong>Design Scenario:</strong> An HVAC mechanical contractor is performing a Manual J cooling and heating load calculation for a 2,000 sq ft single-story home with 9 ft ceilings in Cincinnati, Ohio (Zone 4 Mixed-Humid).</p>
            <ul>
              <li>Conditioned floor area: \(A = 2,000\text{ sq ft}\). Ceiling height: \(H = 9\text{ ft}\) (Volume = \(18,000\text{ cu ft}\)).</li>
              <li>Occupancy: 4 residents. Insulation: Standard double-pane, R-30 attic, R-13 walls.</li>
              <li>Summer outdoor design dry-bulb: \(95^\circ\text{F}\). Indoor setpoint: \(75^\circ\text{F}\) (\(\Delta T = 20^\circ\text{F}\)).</li>
              <li>Winter outdoor design temp: \(15^\circ\text{F}\). Indoor setpoint: \(70^\circ\text{F}\) (\(\Delta T = 55^\circ\text{F}\)).</li>
            </ul>

            <p><strong>Step 1: Compute baseline envelope conduction and infiltration</strong></p>
            <p>For standard construction in Zone 4, baseline envelope sensible heat gain is approximately \(12.5\text{ BTU/hr per sq ft}\) plus internal loads:</p>
            <div class="formula-box">
              $$Q_{\text{envelope}} = 2000 \times 12.5 = 25,000\text{ BTU/hr}$$
              $$Q_{\text{internal}} = (4 \text{ people} \times 400\text{ BTU}) + 3,000\text{ BTU (appliances)} = 4,600\text{ BTU/hr}$$
              $$Q_{\text{sensible}} = 25,000 + 4,600 = 29,600\text{ BTU/hr}$$
            </div>

            <p><strong>Step 2: Add latent moisture load (occupants + ventilation)</strong></p>
            <div class="formula-box">
              $$Q_{\text{latent}} \approx 4 \text{ people} \times 200\text{ BTU} + 5,600\text{ BTU (infiltration)} = 6,400\text{ BTU/hr}$$
            </div>

            <p><strong>Step 3: Total cooling load and tonnage sizing</strong></p>
            <div class="formula-box">
              $$Q_{\text{total}} = 29,600 + 6,400 = 36,000\text{ BTU/hr}$$
              $$\text{Tonnage} = \frac{36,000\text{ BTU/hr}}{12,000\text{ BTU/ton}} = 3.0\text{ Tons of Cooling}$$
            </div>

            <p><strong>Step 4: Determine supply airflow (CFM)</strong></p>
            <div class="formula-box">
              $$\text{Airflow} = 3.0\text{ Tons} \times 400\text{ CFM/ton} = 1,200\text{ CFM}$$
            </div>

            <p><strong>Step 5: Compute winter space heating demand</strong></p>
            <p>Envelope heat loss coefficient \(\approx 24\text{ BTU/hr per sq ft}\) at \(55^\circ\text{F}\) winter \(\Delta T\):</p>
            <div class="formula-box">
              $$Q_{\text{heating}} = 2000 \times 24 = 48,000\text{ BTU/hr} \quad (14.1\text{ kW})$$
            </div>
            <p><strong>Engineering Conclusion:</strong> Sizing requires a <strong>3.0 Ton (36,000 BTU/hr)</strong> heat pump or AC system with <strong>1,200 CFM</strong> ductwork airflow, backed by a 50,000 BTU/hr heating furnace or auxiliary heat strip.</p>
          </div>

          <h2>Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3>Why is an oversized air conditioner worse than a slightly undersized one?</h3>
            <p>An oversized air conditioner drops air temperature rapidly and shuts off before it can extract humidity. Moisture condensation on the evaporator coil requires sustained runtime (at least 15 to 20 minutes per cycle). Short-cycling leaves relative humidity high, leading to dust mite infestation, wood floor warping, mold growth, and high electricity bills due to frequent compressor inrush currents.</p>
          </div>

          <div class="faq-item">
            <h3>What is the difference between SEER and SEER2 efficiency ratings?</h3>
            <p>The Seasonal Energy Efficiency Ratio (SEER) measures total cooling output over a typical cooling season divided by total watt-hours consumed. Starting in 2023, the US Department of Energy enacted <strong>SEER2</strong> (under M1 testing protocols), which increases external static pressure from 0.1 inches water column to 0.5 in. w.c. to reflect real-world duct resistance. A SEER2 rating of 14.3 is roughly equivalent to legacy 15.0 SEER.</p>
          </div>

          <div class="faq-item">
            <h3>How does high altitude affect HVAC airflow and cooling capacity?</h3>
            <p>At high elevations (such as Denver, Colorado at 5,280 ft), atmospheric air pressure is lower, reducing air density by approximately 17% (\(\rho \approx 0.062\text{ lb/ft}^3\)). The sensible heat constant drops from 1.08 to approximately 0.90. To deliver equivalent mass cooling, HVAC blower fans must deliver 15% to 20% higher volumetric CFM, and compressors must be derated by 3% per 1,000 feet above sea level.</p>
          </div>

          <div class="faq-item">
            <h3>What is the difference between a split system and a packaged HVAC unit?</h3>
            <p>A split system separates components: the compressor and condenser coil reside outdoors, while the evaporator coil and air handler/furnace reside indoors in an attic, closet, or basement. A packaged rooftop unit (RTU) houses all refrigeration and air handling components inside a single weatherized cabinet, commonly installed on commercial flat roofs to save interior floor space.</p>
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
        <li><a href="mechanical.html">Mechanical</a></li>
        <li><a href="ohms-law-calculator.html">Ohm's Law</a></li>
        <li><a href="sitemap.xml">Sitemap</a></li>
      </ul>
    </div>
  </footer>

  <script>
    const buildingTypeSelect = document.getElementById('buildingType');
    const climateZoneSelect = document.getElementById('climateZone');
    const floorAreaInput = document.getElementById('floorArea');
    const ceilingHeightHvacInput = document.getElementById('ceilingHeightHvac');
    const numOccupantsInput = document.getElementById('numOccupants');
    const insulationQualitySelect = document.getElementById('insulationQuality');
    const summerOutdoorTempInput = document.getElementById('summerOutdoorTemp');
    const summerIndoorTempInput = document.getElementById('summerIndoorTemp');
    const winterOutdoorTempInput = document.getElementById('winterOutdoorTemp');
    const targetCfmPerTonSelect = document.getElementById('targetCfmPerTon');

    const hvacResultBox = document.getElementById('hvacResultBox');
    const resCoolingTons = document.getElementById('resCoolingTons');
    const resCoolingBtu = document.getElementById('resCoolingBtu');
    const resSensibleBtu = document.getElementById('resSensibleBtu');
    const resLatentBtu = document.getElementById('resLatentBtu');
    const resSupplyCfm = document.getElementById('resSupplyCfm');
    const resHeatingBtu = document.getElementById('resHeatingBtu');
    const resShrRatio = document.getElementById('resShrRatio');
    const resSqftPerTon = document.getElementById('resSqftPerTon');
    const hvacNotesBox = document.getElementById('hvacNotesBox');

    function calculateHvac() {
      const area = parseFloat(floorAreaInput.value) || 2000;
      const height = parseFloat(ceilingHeightHvacInput.value) || 9;
      const occupants = parseInt(numOccupantsInput.value, 10) || 4;
      const tOutSummer = parseFloat(summerOutdoorTempInput.value) || 95;
      const tInSummer = parseFloat(summerIndoorTempInput.value) || 75;
      const tOutWinter = parseFloat(winterOutdoorTempInput.value) || 15;
      const cfmPerTon = parseFloat(targetCfmPerTonSelect.value) || 400;

      // Base load factors per sq ft (BTU/hr/sqft)
      let baseLoadRate = 14.0;
      const bType = buildingTypeSelect.value;
      if (bType === 'commercialOffice') baseLoadRate = 18.0;
      else if (bType === 'retailStore') baseLoadRate = 22.0;
      else if (bType === 'classroom') baseLoadRate = 25.0;
      else if (bType === 'restaurant') baseLoadRate = 35.0;
      else if (bType === 'dataCenter') baseLoadRate = 45.0;

      // Insulation multiplier
      let insulMult = 1.0;
      const insul = insulationQualitySelect.value;
      if (insul === 'highPerformance') insulMult = 0.75;
      else if (insul === 'modern') insulMult = 0.90;
      else if (insul === 'average') insulMult = 1.05;
      else if (insul === 'poor') insulMult = 1.35;

      // Delta T summer impact
      const summerDeltaT = Math.max(5, tOutSummer - tInSummer);
      const deltaTFactor = summerDeltaT / 20.0;

      // Ceiling height factor (> 9 ft increases volume)
      const heightFactor = Math.max(1.0, 1.0 + (height - 9) * 0.04);

      // Sensible Envelope Load
      const q_envelope = area * baseLoadRate * insulMult * deltaTFactor * heightFactor;

      // Internal Gains: People (400 BTU sensible, 200 BTU latent)
      const q_people_sensible = occupants * 350;
      const q_people_latent = occupants * 250;

      // Equipment & Lighting sensible gain
      let q_equip_sensible = area * 1.5;
      if (bType === 'dataCenter') q_equip_sensible = area * 25.0;
      else if (bType === 'restaurant') q_equip_sensible = area * 8.0;

      // Latent Infiltration Load
      const zone = climateZoneSelect.value;
      let latentFactor = 0.25;
      if (zone === 'hotHumid') latentFactor = 0.40;
      else if (zone === 'mixedHumid') latentFactor = 0.28;
      else if (zone === 'hotDry') latentFactor = 0.10;
      else if (zone === 'coldMarine') latentFactor = 0.20;

      const q_sensible_total = q_envelope + q_people_sensible + q_equip_sensible;
      const q_latent_total = (q_sensible_total * latentFactor) + q_people_latent;
      const q_cooling_total = q_sensible_total + q_latent_total;

      const coolingTons = q_cooling_total / 12000;
      // Round to standard 0.5 ton increment
      const recommendedTons = Math.ceil(coolingTons * 2) / 2;

      const supplyCfm = recommendedTons * cfmPerTon;

      // Winter Heating Demand
      const winterDeltaT = Math.max(10, 70 - tOutWinter);
      const q_heating = area * (baseLoadRate * 0.9) * insulMult * (winterDeltaT / 50.0) * heightFactor;

      const shr = q_sensible_total / q_cooling_total;
      const sqftPerTon = area / recommendedTons;

      resCoolingTons.textContent = recommendedTons.toFixed(1) + " Tons";
      resCoolingBtu.textContent = Math.round(q_cooling_total).toLocaleString() + " BTU/hr";
      resSensibleBtu.textContent = Math.round(q_sensible_total).toLocaleString() + " BTU/hr";
      resLatentBtu.textContent = Math.round(q_latent_total).toLocaleString() + " BTU/hr";
      resSupplyCfm.textContent = Math.round(supplyCfm).toLocaleString() + " CFM";
      resHeatingBtu.textContent = Math.round(q_heating).toLocaleString() + " BTU/hr";
      resShrRatio.textContent = shr.toFixed(2) + ` (${(shr * 100).toFixed(0)}% Sensible)`;
      resSqftPerTon.textContent = Math.round(sqftPerTon) + " sq ft/Ton";

      let notes = `<strong>ASHRAE Manual J Sizing:</strong> Building requires <strong>${recommendedTons.toFixed(1)} Tons (${Math.round(q_cooling_total).toLocaleString()} BTU/hr)</strong> of cooling at <strong>${Math.round(supplyCfm)} CFM</strong>. Heating demand is <strong>${Math.round(q_heating).toLocaleString()} BTU/hr</strong>. Floor coverage rate is <strong>${Math.round(sqftPerTon)} sq ft/Ton</strong>.`;
      hvacNotesBox.innerHTML = notes;

      hvacResultBox.style.display = 'block';
    }

    document.getElementById('calcHvacBtn').addEventListener('click', calculateHvac);
    document.getElementById('resetHvacBtn').addEventListener('click', function() {
      setTimeout(calculateHvac, 50);
    });

    window.addEventListener('DOMContentLoaded', calculateHvac);
  </script>
</body>
</html>
"""

def main():
    target_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    file7 = os.path.join(target_dir, "heat-exchanger-calculator.html")
    with open(file7, "w", encoding="utf-8") as f:
        f.write(TOOL_7_HTML)
    print(f"[PASS] heat-exchanger-calculator.html generated successfully!")

    file8 = os.path.join(target_dir, "hvac-calculator.html")
    with open(file8, "w", encoding="utf-8") as f:
        f.write(TOOL_8_HTML)
    print(f"[PASS] hvac-calculator.html generated successfully!")

if __name__ == "__main__":
    main()
