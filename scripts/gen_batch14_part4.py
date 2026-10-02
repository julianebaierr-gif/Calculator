# -*- coding: utf-8 -*-
"""
Script to generate Batch 14 Part 4 tools:
7. charles-law-calculator.html
8. chlorine-dioxide-dosing-calculator.html
"""
import os

TOOL_7_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Charles's Law Calculator | V₁/T₁ = V₂/T₂ Isobaric Thermal Expansion Sizer</title>
  <meta name="description" content="Calculate gas volume and absolute temperature changes at constant pressure using Charles's Law (V1/T1 = V2/T2), isobaric boundary work, and thermal expansion.">
  <link rel="canonical" href="https://calchub.cloud/charles-law-calculator.html">
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
        "name": "Charles's Law Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Computes isobaric thermal gas expansion and contraction using Charles's Law V1/T1 = V2/T2, thermodynamic boundary work P*DeltaV, and absolute temperature scales.",
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
            "name": "What is Charles's Law and what thermodynamic variable must remain constant?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Charles's Law (also known as the Law of Volumes) states that the volume of a given mass of an ideal gas is directly proportional to its absolute thermodynamic temperature, provided the system pressure and gas quantity remain constant: V1 / T1 = V2 / T2 = k."
            }
          },
          {
            "@type": "Question",
            "name": "Why MUST temperatures always be converted to Kelvin or Rankine in Charles's Law?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Celsius and Fahrenheit are relative scales with arbitrary zero points. Gas thermal kinetic energy is directly proportional to absolute thermodynamic temperature measured from Absolute Zero (0 K = -273.15°C or 0°R = -459.67°F). Calculating with Celsius or Fahrenheit yields mathematically invalid results and potential division-by-zero errors."
            }
          },
          {
            "@type": "Question",
            "name": "How is isobaric mechanical boundary work calculated during thermal gas expansion?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Because pressure P remains strictly constant during an isobaric process, the mechanical boundary work done by or on the expanding gas simplifies to: W = P * (V2 - V1) = n * R * (T2 - T1). When a gas is heated and expands (V2 > V1), it performs positive work against the surrounding atmosphere or piston face."
            }
          },
          {
            "@type": "Question",
            "name": "How did Charles's Law lead to the discovery of Absolute Zero?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "By plotting gas volume versus Celsius temperature for various gases at constant pressure, 18th-century scientists observed that every linear isobaric extrapolation intersected the zero-volume axis at exactly -273.15°C. This universal intercept established the physical existence of Absolute Zero, the thermodynamic limit where all classical molecular translation ceases."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="chemical">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">
        <span class="logo-icon">&pi;</span>
        <span class="logo-text">Calc<strong>Hub</strong></span>
      </a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="engineering.html">Engineering</a>
        <a href="mechanical.html">Mechanical</a>
        <a href="civil.html">Civil &amp; Roof</a>
        <a href="solar-energy.html">Solar</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo; 
      <a href="chemical.html">Chemical &amp; Water Treatment</a> &rsaquo; 
      <span>Charles's Law Calculator</span>
    </nav>

    <h1 class="tool-title">Charles's Law Calculator (V₁/T₁ = V₂/T₂)</h1>
    <p class="tool-subtitle">Isobaric Thermal Gas Expansion, Absolute Temperature Sizing &amp; Boundary Work</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="charlesTarget">Variable to Solve For</label>
            <select id="charlesTarget" class="form-control" onchange="updateCharlesInputs()">
              <option value="v2" selected>Final Volume (V₂)</option>
              <option value="t2">Final Temperature (T₂)</option>
              <option value="v1">Initial Volume (V₁)</option>
              <option value="t1">Initial Temperature (T₁)</option>
            </select>
          </div>

          <!-- V1 Input -->
          <div id="v1CharlesGroup" class="grid-2-col">
            <div class="form-group">
              <label for="v1Val">Initial Volume (V₁)</label>
              <input type="number" id="v1Val" class="form-control" value="50.0" step="1.0" min="0.0001">
            </div>
            <div class="form-group">
              <label for="v1Unit">V₁ Volume Unit</label>
              <select id="v1Unit" class="form-control">
                <option value="l" selected>Liters (L)</option>
                <option value="m3">Cubic Meters (m³)</option>
                <option value="cm3">Cubic Centimeters (cm³ / mL)</option>
                <option value="ft3">Cubic Feet (ft³)</option>
                <option value="gal">US Gallons (gal)</option>
              </select>
            </div>
          </div>

          <!-- T1 Input -->
          <div id="t1CharlesGroup" class="grid-2-col">
            <div class="form-group">
              <label for="t1Val">Initial Temperature (T₁)</label>
              <input type="number" id="t1Val" class="form-control" value="20.0" step="1.0">
            </div>
            <div class="form-group">
              <label for="t1Unit">T₁ Temperature Scale</label>
              <select id="t1Unit" class="form-control">
                <option value="c" selected>Celsius (°C)</option>
                <option value="k">Kelvin (K)</option>
                <option value="f">Fahrenheit (°F)</option>
                <option value="r">Rankine (°R)</option>
              </select>
            </div>
          </div>

          <!-- V2 Input -->
          <div id="v2CharlesGroup" class="grid-2-col" style="display:none;">
            <div class="form-group">
              <label for="v2Val">Final Volume (V₂)</label>
              <input type="number" id="v2Val" class="form-control" value="60.0" step="1.0" min="0.0001">
            </div>
            <div class="form-group">
              <label for="v2Unit">V₂ Volume Unit</label>
              <select id="v2Unit" class="form-control">
                <option value="l" selected>Liters (L)</option>
                <option value="m3">Cubic Meters (m³)</option>
                <option value="cm3">Cubic Centimeters (cm³ / mL)</option>
                <option value="ft3">Cubic Feet (ft³)</option>
                <option value="gal">US Gallons (gal)</option>
              </select>
            </div>
          </div>

          <!-- T2 Input -->
          <div id="t2CharlesGroup" class="grid-2-col">
            <div class="form-group">
              <label for="t2Val">Final Temperature (T₂)</label>
              <input type="number" id="t2Val" class="form-control" value="80.0" step="1.0">
            </div>
            <div class="form-group">
              <label for="t2Unit">T₂ Temperature Scale</label>
              <select id="t2Unit" class="form-control">
                <option value="c" selected>Celsius (°C)</option>
                <option value="k">Kelvin (K)</option>
                <option value="f">Fahrenheit (°F)</option>
                <option value="r">Rankine (°R)</option>
              </select>
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="sysPressure">Constant System Pressure</label>
              <input type="number" id="sysPressure" class="form-control" value="1.01325" step="0.01" min="0.001">
            </div>
            <div class="form-group">
              <label for="sysPresUnit">Pressure Unit</label>
              <select id="sysPresUnit" class="form-control">
                <option value="bar" selected>Bar (absolute)</option>
                <option value="atm">Atmospheres (atm)</option>
                <option value="kpa">Kilopascals (kPa)</option>
                <option value="psi">Pounds/sq in (psia)</option>
              </select>
            </div>
          </div>

          <div class="form-group">
            <label for="charlesGas">Gas Molecular Identity</label>
            <select id="charlesGas" class="form-control">
              <option value="air" selected>Dry Air (MW = 28.97 g/mol, Cp = 1.005 kJ/kg·K)</option>
              <option value="n2">Pure Nitrogen N₂ (MW = 28.01 g/mol, Cp = 1.040 kJ/kg·K)</option>
              <option value="o2">Pure Oxygen O₂ (MW = 32.00 g/mol, Cp = 0.918 kJ/kg·K)</option>
              <option value="co2">Carbon Dioxide CO₂ (MW = 44.01 g/mol, Cp = 0.846 kJ/kg·K)</option>
              <option value="he">Helium He (MW = 4.003 g/mol, Cp = 5.193 kJ/kg·K)</option>
              <option value="h2">Hydrogen H₂ (MW = 2.016 g/mol, Cp = 14.30 kJ/kg·K)</option>
            </select>
          </div>

          <button type="button" class="btn btn-primary" onclick="calcCharlesLaw()">Solve Charles's Law Equation</button>
        </div>

        <div id="charlesResults" class="results-box" style="display:none;margin-top:1.5rem;">
          <h3 class="results-title">Isobaric Thermal Expansion Diagnostics</h3>
          <div class="result-grid">
            <div class="result-card">
              <div class="result-label" id="resCharlesTargetLabel">Calculated Value</div>
              <div class="result-value highlight" id="resCharlesTargetVal">--</div>
              <div class="result-subtext" id="resCharlesTargetAlt">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Volumetric Thermal Expansion</div>
              <div class="result-value" id="resDeltaV">--</div>
              <div class="result-subtext" id="resDeltaVDesc">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Boundary Mechanical Work (P·ΔV)</div>
              <div class="result-value highlight" id="resWorkIsobaric">--</div>
              <div class="result-subtext" id="resWorkIsobaricDesc">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Charles Constant (k = V/T)</div>
              <div class="result-value" id="resCharlesK">--</div>
              <div class="result-subtext">Liters / Kelvin ratio</div>
            </div>
          </div>

          <div class="result-details" style="margin-top:1rem;padding:1rem;background:var(--card-bg);border-radius:6px;border:1px solid var(--border-light);">
            <h4 style="margin-top:0;">Thermodynamics &amp; Heat Transfer</h4>
            <ul style="margin-bottom:0;line-height:1.7;">
              <li><strong>Absolute Temperatures:</strong> <span id="resAbsTemps">--</span></li>
              <li><strong>Total Gas Moles &amp; Mass:</strong> <span id="resGasQuant">--</span></li>
              <li><strong>Enthalpy Thermal Transfer (ΔH = m·Cp·ΔT):</strong> <span id="resEnthalpy">--</span></li>
              <li><strong>Density Shift:</strong> <span id="resDensityShift">--</span></li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Related Category Sidebar -->
      <aside class="post-sidebar">
        <div class="sidebar-widget">
          <div class="sidebar-widget-header">
            <span class="widget-icon">🧪</span>
            <h3 class="widget-title">Related Chemical Calculators</h3>
          </div>
          <p class="sidebar-widget-subtitle">Specialized calculation tools in this discipline:</p>
          <ul class="sidebar-links-list">
            <li><a href="boyles-law-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Boyle's Law Calculator</a></li>
            <li><a href="alum-dosing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Alum Dosing Calculator</a></li>
            <li><a href="caustic-soda-dosing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Caustic Soda Dosing Calculator</a></li>
            <li><a href="thermal-expansion-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Thermal Expansion &amp; Pipe Stress</a></li>
          </ul>
          <div style="margin-top:1.25rem;padding-top:1rem;border-top:1px solid var(--border-light);">
            <a href="chemical.html" class="sidebar-category-link">View All Chemical Calculators &rarr;</a>
          </div>
        </div>
      </aside>
    </div>

    <!-- Technical Educational Article Body (1000+ Words) -->
    <article class="article-body">
      <h2>Thermodynamic Foundations of Charles's Law</h2>
      <p>Charles's Law (frequently designated as the Law of Volumes) establishes the foundational thermodynamic relationship governing isobaric (constant pressure) thermal expansion of gaseous matter. Formulated conceptually by French inventor and aeronaut Jacques Alexandre César Charles in 1787—who constructed the first hydrogen-filled gas balloon—and formalized mathematically by Joseph Louis Gay-Lussac in 1802, the law describes how gases respond volumetrically to variations in internal thermal energy.</p>

      <p>Under the kinetic molecular theory of ideal gases, macroscopic temperature represents a direct statistical measure of the average translational kinetic energy of molecular entities ($\bar{E}_k = \frac{3}{2} k_B T$). When heat is transferred into a gaseous enclosure at constant pressure, molecular velocities and collision momentum increase. To prevent internal pressure from exceeding the ambient external constraint, the physical boundaries of the container must dilate, increasing the volume and inter-molecular separation distance in exact linear proportionality to the absolute thermodynamic temperature.</p>

      <h2>Mathematical Formulation and the Absolute Temperature Scale</h2>
      <p>The mathematical postulate of Charles's Law is stated as:</p>

      <div class="formula-box">
        $$\frac{V}{T} = k \quad \implies \quad \frac{V_1}{T_1} = \frac{V_2}{T_2} \quad (P = \text{constant}, \, n = \text{constant})$$
      </div>

      <p>Where:</p>
      <ul>
        <li>$V_1, V_2$ = Initial and final gas volumes (expressed in identical units such as liters, $\text{m}^3$, or $\text{ft}^3$).</li>
        <li>$T_1, T_2$ = Initial and final temperatures expressed <strong>strictly on an absolute thermodynamic scale</strong> (Kelvin or Rankine).</li>
        <li>$k = \frac{n R}{P}$ = The isobaric Charles proportionality constant.</li>
      </ul>

      <p>Rearranging the equation yields four explicit algebraic solutions for any single unknown parameter:</p>

      <div class="formula-box">
        $$V_2 = V_1 \left(\frac{T_2}{T_1}\right), \quad T_2 = T_1 \left(\frac{V_2}{V_1}\right), \quad V_1 = V_2 \left(\frac{T_1}{T_2}\right), \quad T_1 = T_2 \left(\frac{V_1}{V_2}\right)$$
      </div>

      <p>Conversion to the absolute Kelvin scale ($K$) from Celsius ($^\circ\text{C}$) or to Rankine ($^\circ\text{R}$) from Fahrenheit ($^\circ\text{F}$) is mathematically non-negotiable:</p>
      <div class="formula-box">
        $$T_{\text{Kelvin}} = T_{^\circ\text{C}} + 273.15, \quad T_{\text{Rankine}} = T_{^\circ\text{F}} + 459.67$$
      </div>

      <h2>Isobaric Boundary Work and Enthalpy Changes</h2>
      <p>Because an isobaric system involves movable control surfaces (such as a weighted piston, an elastic bladder, or an open atmospheric ventilation column), thermal expansion forces the gas to perform mechanical boundary work against external pressure ($P$). The work done during expansion is determined by integrating $dW = P \, dV$:</p>

      <div class="formula-box">
        $$W_{\text{isobaric}} = \int_{V_1}^{V_2} P \, dV = P \cdot (V_2 - V_1) = P \cdot \Delta V$$
      </div>

      <p>By substituting the Ideal Gas Law ($P V_1 = n R T_1$ and $P V_2 = n R T_2$), boundary work can also be evaluated purely from molar thermal differential:</p>
      <div class="formula-box">
        $$W_{\text{isobaric}} = n R (T_2 - T_1) = n R \Delta T$$
      </div>

      <p>The total heat energy ($Q$) required to drive an isobaric temperature shift reflects the change in system enthalpy ($\Delta H$), encompassing both internal energy gain ($\Delta U = n C_v \Delta T$) and boundary displacement work ($W = n R \Delta T$):</p>
      <div class="formula-box">
        $$Q_p = \Delta H = m \cdot c_p \cdot \Delta T = n \cdot C_{p,\text{molar}} \cdot \Delta T$$
      </div>
      <p>Where $C_p = C_v + R$ represents the constant-pressure molar heat capacity, reflecting Mayer's thermodynamic relation for ideal gases.</p>

      <h2>Physical Properties and Heat Capacities of Common Industrial Gases</h2>
      <p>The table below summarizes molecular parameters, specific heat capacities ($c_p$), and thermal expansion characteristics across representative gases at $25^\circ\text{C}$ and $1.0\text{ atm}$:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Gas Species</th>
              <th>Molar Mass (g/mol)</th>
              <th>Specific Heat c_p (kJ/kg·K)</th>
              <th>Molar Heat C_p (J/mol·K)</th>
              <th>Isobaric Expansion Coeff β (1/K @ 20°C)</th>
              <th>Ratio of Specific Heats (γ = Cp/Cv)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Dry Atmospheric Air</td>
              <td>28.97</td>
              <td>1.005</td>
              <td>29.12</td>
              <td>0.003411 (1/293.15)</td>
              <td>1.400</td>
            </tr>
            <tr>
              <td>Nitrogen (N₂)</td>
              <td>28.01</td>
              <td>1.040</td>
              <td>29.13</td>
              <td>0.003411</td>
              <td>1.404</td>
            </tr>
            <tr>
              <td>Oxygen (O₂)</td>
              <td>32.00</td>
              <td>0.918</td>
              <td>29.38</td>
              <td>0.003411</td>
              <td>1.395</td>
            </tr>
            <tr>
              <td>Carbon Dioxide (CO₂)</td>
              <td>44.01</td>
              <td>0.846</td>
              <td>37.23</td>
              <td>0.003415</td>
              <td>1.289</td>
            </tr>
            <tr>
              <td>Helium (He, Monatomic)</td>
              <td>4.003</td>
              <td>5.193</td>
              <td>20.78</td>
              <td>0.003411</td>
              <td>1.667</td>
            </tr>
            <tr>
              <td>Hydrogen (H₂)</td>
              <td>2.016</td>
              <td>14.304</td>
              <td>28.84</td>
              <td>0.003411</td>
              <td>1.405</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Practical Worked Case Study: Atmospheric Solar Heating of an Air Dome</h2>
      <div class="worked-example-card">
        <h3>Engineering Design Example: Fabric Storage Dome Thermal Diurnal Cycle</h3>
        <p><strong>Scenario:</strong> A flexible, constant-pressure fabric pneumatic storage enclosure contains $V_1 = 2,500.0\text{ m}^3$ of atmospheric air at a cool morning ambient temperature of $T_1 = 10.0^\circ\text{C}$ ($283.15\text{ K}$). Throughout the day, intense solar radiation elevates the internal air temperature to a peak afternoon value of $T_2 = 45.0^\circ\text{C}$ ($318.15\text{ K}$). Atmospheric barometric pressure remains constant at sea level: $P = 1.01325\text{ bar}$ ($101,325\text{ Pa}$). Assume dry air behavior ($MW = 28.97\text{ g/mol}, c_p = 1.005\text{ kJ/kg}\cdot\text{K}$).</p>

        <p><strong>Step 1: Calculate Absolute Thermodynamic Temperatures:</strong></p>
        $$T_1 = 10.0 + 273.15 = 283.15\text{ K}$$
        $$T_2 = 45.0 + 273.15 = 318.15\text{ K}$$

        <p><strong>Step 2: Determine Final Expanded Volume (V₂) via Charles's Law:</strong></p>
        $$V_2 = V_1 \times \left(\frac{T_2}{T_1}\right) = 2,500.0\text{ m}^3 \times \left(\frac{318.15\text{ K}}{283.15\text{ K}}\right) = 2,500.0 \times 1.12361 = 2,809.02\text{ m}^3$$
        <p>Net volumetric expansion:</p>
        $$\Delta V = V_2 - V_1 = 2,809.02 - 2,500.0 = 309.02\text{ m}^3\text{ (+12.36% volume expansion)}$$

        <p><strong>Step 3: Compute Initial Moles and Contained Mass:</strong></p>
        $$n = \frac{P V_1}{R T_1} = \frac{101,325\text{ Pa} \times 2,500.0\text{ m}^3}{8.3145\text{ J/(mol}\cdot\text{K)} \times 283.15\text{ K}} = \frac{253,312,500}{2,354.25} = 107,598\text{ moles}$$
        $$m_{\text{air}} = 107,598\text{ mol} \times 0.02897\text{ kg/mol} = 3,117.1\text{ kg (6,872.0 lbs)}$$

        <p><strong>Step 4: Calculate Mechanical Isobaric Boundary Work (P·ΔV):</strong></p>
        $$W_{\text{isobaric}} = P \cdot \Delta V = 101,325\text{ N/m}^2 \times 309.02\text{ m}^3 = 31,311,452\text{ Joules} = 31.31\text{ MJ (8.70 kWh)}$$
        <p>The expanding gas performs $31.31\text{ MJ}$ of physical work against the surrounding atmosphere.</p>

        <p><strong>Step 5: Enthalpy Energy Transferred:</strong></p>
        $$\Delta H = m \cdot c_p \cdot \Delta T = 3,117.1\text{ kg} \times 1.005\text{ kJ/kg}\cdot\text{K} \times (45.0 - 10.0)\text{ K} = 109,644\text{ kJ} \approx 109.64\text{ MJ}$$
      </div>

      <h2>Engineering Applications and Real-World Relevance</h2>
      <p>Charles's Law dictates vital design and safety parameters across modern industrial operations:</p>
      <ul>
        <li><strong>Aerostat and Hot Air Ballooning:</strong> As air inside a balloon envelope is heated from $20^\circ\text{C}$ to $100^\circ\text{C}$, Charles's Law dictates a $27\%$ volumetric expansion. Because the envelope has an open mouth at the bottom maintaining atmospheric pressure, excess air spills out, decreasing the internal density ($\rho = \frac{P \cdot MW}{R T}$) and creating the buoyant Archimedean lift force ($F_{\text{buoyant}} = (\rho_{\text{ambient}} - \rho_{\text{hot}}) \cdot V_{\text{envelope}} \cdot g$).</li>
        <li><strong>Thermal Relief Valves in Piping Systems:</strong> When cryogenic fluids (LNG, liquid nitrogen) or liquefied gases are trapped between closed isolation valves in outdoor piping, ambient warming drives rapid thermal expansion. Without ASME Section VIII thermal pressure relief valves (TRVs), trapped fluid rapidly pressurizes beyond the yield point, causing catastrophic flange blowouts.</li>
        <li><strong>HVAC Ductwork Air Balancing:</strong> In centralized heating systems, warm air supplied at $55^\circ\text{C}$ ($131^\circ\text{F}$) occupies greater specific volume than ambient return air at $20^\circ\text{C}$ ($68^\circ\text{F}$). HVAC design engineers adjust volumetric flow rates (CFM) to account for Charles expansion and maintain balanced building pressurization.</li>
      </ul>
    </article>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-grid">
        <div class="footer-col">
          <div class="footer-logo">
            <span class="logo-icon">&pi;</span>
            <span class="logo-text">Calc<strong>Hub</strong></span>
          </div>
          <p class="footer-about">High-precision chemical, thermodynamic, and mechanical calculation tools conforming to ASME, ISO, and NIST physical standards.</p>
        </div>
        <div class="footer-col">
          <h4 class="footer-title">Engineering Disciplines</h4>
          <ul class="footer-links">
            <li><a href="chemical.html">Chemical &amp; Water Treatment</a></li>
            <li><a href="mechanical.html">Mechanical &amp; HVAC</a></li>
            <li><a href="engineering.html">Electrical &amp; Electronics</a></li>
            <li><a href="civil.html">Civil &amp; Construction</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4 class="footer-title">Standard References</h4>
          <ul class="footer-links">
            <li><a href="https://webbook.nist.gov" target="_blank" rel="noopener">NIST Chemistry WebBook</a></li>
            <li><a href="https://www.asme.org" target="_blank" rel="noopener">ASME Boiler &amp; Pressure Vessel</a></li>
            <li><a href="https://www.iupac.org" target="_blank" rel="noopener">IUPAC Physical Chemistry</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    const CHARLES_GAS_PROPS = {
      air: { mw: 28.97, cp: 1.005 },
      n2: { mw: 28.01, cp: 1.040 },
      o2: { mw: 32.00, cp: 0.918 },
      co2: { mw: 44.01, cp: 0.846 },
      he: { mw: 4.003, cp: 5.193 },
      h2: { mw: 2.016, cp: 14.304 }
    };

    function updateCharlesInputs() {
      const target = document.getElementById("charlesTarget").value;
      document.getElementById("v1CharlesGroup").style.display = target === "v1" ? "none" : "grid";
      document.getElementById("t1CharlesGroup").style.display = target === "t1" ? "none" : "grid";
      document.getElementById("v2CharlesGroup").style.display = target === "v2" ? "none" : "grid";
      document.getElementById("t2CharlesGroup").style.display = target === "t2" ? "none" : "grid";
    }

    function toKelvin(val, scale) {
      if (scale === "c") return val + 273.15;
      if (scale === "k") return val;
      if (scale === "f") return (val - 32) * (5 / 9) + 273.15;
      if (scale === "r") return val * (5 / 9);
      return val;
    }

    function fromKelvin(k, scale) {
      if (scale === "c") return k - 273.15;
      if (scale === "k") return k;
      if (scale === "f") return (k - 273.15) * (9 / 5) + 32;
      if (scale === "r") return k * (9 / 5);
      return k;
    }

    function toM3(val, unit) {
      if (unit === "l") return val * 0.001;
      if (unit === "cm3") return val * 0.000001;
      if (unit === "ft3") return val * 0.0283168;
      if (unit === "gal") return val * 0.00378541;
      return val;
    }

    function fromM3(m3, unit) {
      if (unit === "l") return m3 * 1000;
      if (unit === "cm3") return m3 * 1000000;
      if (unit === "ft3") return m3 / 0.0283168;
      if (unit === "gal") return m3 / 0.00378541;
      return m3;
    }

    function toPascalsIsobaric(val, unit) {
      if (unit === "bar") return val * 100000;
      if (unit === "atm") return val * 101325;
      if (unit === "kpa") return val * 1000;
      if (unit === "psi") return val * 6894.757;
      return val;
    }

    function calcCharlesLaw() {
      const target = document.getElementById("charlesTarget").value;
      const gasKey = document.getElementById("charlesGas").value;
      const props = CHARLES_GAS_PROPS[gasKey];
      const pVal = parseFloat(document.getElementById("sysPressure").value) || 1.01325;
      const pUnit = document.getElementById("sysPresUnit").value;
      const p_pa = toPascalsIsobaric(pVal, pUnit);

      let v1_m3 = 0, t1_k = 0, v2_m3 = 0, t2_k = 0;

      if (target !== "v1") {
        const v = parseFloat(document.getElementById("v1Val").value) || 0;
        const u = document.getElementById("v1Unit").value;
        v1_m3 = toM3(v, u);
      }
      if (target !== "t1") {
        const t = parseFloat(document.getElementById("t1Val").value) || 0;
        const s = document.getElementById("t1Unit").value;
        t1_k = toKelvin(t, s);
      }
      if (target !== "v2") {
        const v = parseFloat(document.getElementById("v2Val").value) || 0;
        const u = document.getElementById("v2Unit").value;
        v2_m3 = toM3(v, u);
      }
      if (target !== "t2") {
        const t = parseFloat(document.getElementById("t2Val").value) || 0;
        const s = document.getElementById("t2Unit").value;
        t2_k = toKelvin(t, s);
      }

      let resultText = "";
      let resultAltText = "";
      let targetLabel = "";

      if (target === "v2") {
        if (t1_k <= 0) { alert("T1 must be above Absolute Zero (> 0 K)"); return; }
        v2_m3 = v1_m3 * (t2_k / t1_k);
        const outUnit = document.getElementById("v1Unit").value;
        const v2_disp = fromM3(v2_m3, outUnit);
        targetLabel = "Final Volume (V₂)";
        resultText = v2_disp.toFixed(4) + " " + outUnit.toUpperCase();
        resultAltText = (v2_m3 * 1000).toFixed(2) + " L (" + v2_m3.toFixed(4) + " m³)";
      } else if (target === "t2") {
        if (v1_m3 <= 0) { alert("V1 must be positive"); return; }
        t2_k = t1_k * (v2_m3 / v1_m3);
        const outScale = document.getElementById("t1Unit").value;
        const t2_disp = fromKelvin(t2_k, outScale);
        targetLabel = "Final Temperature (T₂)";
        resultText = t2_disp.toFixed(2) + " °" + outScale.toUpperCase();
        resultAltText = t2_k.toFixed(2) + " K (" + (t2_k - 273.15).toFixed(2) + " °C)";
      } else if (target === "v1") {
        if (t2_k <= 0) { alert("T2 must be above Absolute Zero (> 0 K)"); return; }
        v1_m3 = v2_m3 * (t1_k / t2_k);
        const outUnit = document.getElementById("v2Unit").value;
        const v1_disp = fromM3(v1_m3, outUnit);
        targetLabel = "Initial Volume (V₁)";
        resultText = v1_disp.toFixed(4) + " " + outUnit.toUpperCase();
        resultAltText = (v1_m3 * 1000).toFixed(2) + " L (" + v1_m3.toFixed(4) + " m³)";
      } else if (target === "t1") {
        if (v2_m3 <= 0) { alert("V2 must be positive"); return; }
        t1_k = t2_k * (v1_m3 / v2_m3);
        const outScale = document.getElementById("t2Unit").value;
        const t1_disp = fromKelvin(t1_k, outScale);
        targetLabel = "Initial Temperature (T₁)";
        resultText = t1_disp.toFixed(2) + " °" + outScale.toUpperCase();
        resultAltText = t1_k.toFixed(2) + " K (" + (t1_k - 273.15).toFixed(2) + " °C)";
      }

      // Charles constant k = V / T (liters / K)
      const charlesK = (v1_m3 * 1000) / t1_k;

      // Delta V
      const deltaV_m3 = v2_m3 - v1_m3;
      const deltaV_liters = deltaV_m3 * 1000;
      const pctChange = ((v2_m3 - v1_m3) / v1_m3) * 100;

      // Isobaric Work W = P * deltaV (Joules)
      const workJoules = p_pa * deltaV_m3;
      const workKJ = workJoules / 1000;

      // Moles & Mass
      const R = 8.314462;
      const moles = (p_pa * v1_m3) / (R * t1_k);
      const massKg = (moles * props.mw) / 1000;

      // Enthalpy deltaH = m * cp * deltaT (kJ)
      const deltaT = t2_k - t1_k;
      const deltaH_kJ = massKg * props.cp * deltaT;

      // Density shift (kg/m3)
      const rho1 = massKg / v1_m3;
      const rho2 = massKg / v2_m3;

      document.getElementById("resCharlesTargetLabel").textContent = targetLabel;
      document.getElementById("resCharlesTargetVal").textContent = resultText;
      document.getElementById("resCharlesTargetAlt").textContent = resultAltText;

      document.getElementById("resDeltaV").textContent = (deltaV_liters >= 0 ? "+" : "") + deltaV_liters.toFixed(2) + " L";
      document.getElementById("resDeltaVDesc").textContent = (pctChange >= 0 ? "+" : "") + pctChange.toFixed(2) + "% volume shift (" + deltaV_m3.toFixed(4) + " m³)";

      document.getElementById("resWorkIsobaric").textContent = Math.abs(workKJ).toFixed(2) + " kJ";
      document.getElementById("resWorkIsobaricDesc").textContent = workJoules >= 0 ? "Work done BY gas expanding on atmosphere" : "Work done ON gas during cooling contraction";

      document.getElementById("resCharlesK").textContent = charlesK.toFixed(4) + " L/K";

      document.getElementById("resAbsTemps").textContent = "T₁ = " + t1_k.toFixed(2) + " K (" + (t1_k - 273.15).toFixed(1) + "°C)  ➜  T₂ = " + t2_k.toFixed(2) + " K (" + (t2_k - 273.15).toFixed(1) + "°C)";
      document.getElementById("resGasQuant").textContent = moles.toFixed(2) + " moles (" + massKg.toFixed(3) + " kg / " + (massKg * 2.20462).toFixed(2) + " lbs of " + gasKey.toUpperCase() + ")";
      document.getElementById("resEnthalpy").textContent = (deltaH_kJ >= 0 ? "+" : "") + deltaH_kJ.toFixed(2) + " kJ (" + (deltaH_kJ >= 0 ? "Heat added into gas" : "Heat rejected from gas") + ")";
      document.getElementById("resDensityShift").textContent = "ρ₁ = " + rho1.toFixed(3) + " kg/m³  ➜  ρ₂ = " + rho2.toFixed(3) + " kg/m³ (" + (((rho2 - rho1) / rho1) * 100).toFixed(1) + "% density change)";

      document.getElementById("charlesResults").style.display = "block";
    }
  </script>
</body>
</html>
"""

TOOL_8_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chlorine Dioxide Dosing Calculator | ClO₂ Pre-Oxidation &amp; Disinfection</title>
  <meta name="description" content="Calculate chlorine dioxide (ClO2) dosing rates, sodium chlorite (NaClO2) chemical precursor requirements, iron/manganese demand, and chlorite by-product limits.">
  <link rel="canonical" href="https://calchub.cloud/chlorine-dioxide-dosing-calculator.html">
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
        "name": "Chlorine Dioxide Dosing Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates chlorine dioxide (ClO2) feed rates, sodium chlorite (NaClO2) precursor demand, generator chemical yield, iron and manganese oxidation stoichiometry, and EPA chlorite by-product limits.",
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
            "name": "Why is chlorine dioxide preferred over chlorine for pre-oxidation?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Unlike chlorine (HOCl/Cl2), chlorine dioxide (ClO2) does not react with natural organic matter (NOM) via substitution reactions. Consequently, it produces virtually zero regulated trihalomethanes (THMs) or haloacetic acids (HAA5), making it the premier pre-oxidant for surface waters rich in humic and fulvic precursors."
            }
          },
          {
            "@type": "Question",
            "name": "What are the stoichiometric requirements to generate chlorine dioxide from sodium chlorite?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In the standard two-chemical process: 2 NaClO2 + Cl2 -> 2 ClO2 + 2 NaCl. Stoichiometrically, generating 1.0 lb of pure ClO2 requires 1.341 lbs of pure dry sodium chlorite (NaClO2) and 0.526 lbs of chlorine gas (Cl2). Accounting for typical generator efficiency (95%), 1.41 lbs of pure chlorite is required."
            }
          },
          {
            "@type": "Question",
            "name": "What is the EPA regulatory limit for chlorine dioxide and its chlorite by-product?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Under the EPA Stage 1 and Stage 2 Disinfection Byproducts Rules, the Maximum Residual Disinfectant Level (MRDL) for chlorine dioxide entering the distribution system is 0.8 mg/L. The Maximum Contaminant Level (MCL) for the chlorite (ClO2-) by-product ion is 1.0 mg/L. Because 50% to 70% of dosed ClO2 converts to chlorite, typical applied doses rarely exceed 1.2 to 1.4 mg/L."
            }
          },
          {
            "@type": "Question",
            "name": "What is the stoichiometric demand of chlorine dioxide for oxidizing iron and manganese?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Theoretical oxidation stoichiometry mandates: 1.0 mg/L of dissolved ferrous iron (Fe2+) consumes 1.20 mg/L of ClO2 (yielding ferric hydroxide Fe(OH)3 precipitate). 1.0 mg/L of soluble manganous manganese (Mn2+) consumes 2.45 mg/L of ClO2 (yielding manganese dioxide MnO2 precipitate)."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="chemical">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">
        <span class="logo-icon">&pi;</span>
        <span class="logo-text">Calc<strong>Hub</strong></span>
      </a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="engineering.html">Engineering</a>
        <a href="mechanical.html">Mechanical</a>
        <a href="civil.html">Civil &amp; Roof</a>
        <a href="solar-energy.html">Solar</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo; 
      <a href="chemical.html">Chemical &amp; Water Treatment</a> &rsaquo; 
      <span>Chlorine Dioxide Dosing Calculator</span>
    </nav>

    <h1 class="tool-title">Chlorine Dioxide (ClO₂) Dosing &amp; Oxidation Calculator</h1>
    <p class="tool-subtitle">Pre-Oxidation Sizing, Sodium Chlorite (NaClO₂) Precursor Demand &amp; EPA Chlorite Limits</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="clO2AppMode">Treatment Application Objective</label>
            <select id="clO2AppMode" class="form-control" onchange="updateClO2Preset()">
              <option value="iron_manganese" selected>Iron &amp; Manganese Pre-Oxidation (Well / Reservoir)</option>
              <option value="taste_odor">Taste &amp; Odor Control (Algal Geosmin / MIB Destr., 0.5&ndash;1.0 mg/L)</option>
              <option value="primary_disinf">Primary Disinfection (Cryptosporidium / Giardia Log Credit)</option>
              <option value="phenolic_destr">Industrial Phenol &amp; Cyanide Destruction</option>
              <option value="custom">Custom Applied Chlorine Dioxide Dose</option>
            </select>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="clO2FlowUnit">Raw Water Plant Flow Units</label>
              <select id="clO2FlowUnit" class="form-control" onchange="toggleClO2FlowLabels()">
                <option value="mgd" selected>MGD (Million Gallons per Day)</option>
                <option value="gpm">GPM (Gallons per Minute)</option>
                <option value="m3h">m³/hour</option>
                <option value="m3d">m³/day</option>
                <option value="lps">Liters per Second (L/s)</option>
              </select>
            </div>
            <div class="form-group">
              <label for="clO2FlowVal" id="clO2FlowLabel">Water Flow Rate (MGD)</label>
              <input type="number" id="clO2FlowVal" class="form-control" value="8.0" step="0.1" min="0.01">
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="appliedDose">Target ClO₂ Dose (mg/L or ppm)</label>
              <input type="number" id="appliedDose" class="form-control" value="1.20" step="0.05" min="0.05" max="5.0">
              <span class="field-hint">EPA MRDL cap entering distribution is 0.80 mg/L residual</span>
            </div>
            <div class="form-group">
              <label for="genYield">Generator Chemical Yield Efficiency (%)</label>
              <input type="number" id="genYield" class="form-control" value="95" step="1" min="80" max="100">
              <span class="field-hint">Standard vacuum eduction or loop generators achieve 92&ndash;98%</span>
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="chloriteGrade">Sodium Chlorite Precursor Solution</label>
              <select id="chloriteGrade" class="form-control">
                <option value="25_liquid" selected>25% Active NaClO₂ Solution (SG = 1.21, 2.52 lb active/gal)</option>
                <option value="31_liquid">31.25% Active NaClO₂ Solution (SG = 1.27, 3.31 lb active/gal)</option>
                <option value="80_dry">80% Dry Active NaClO₂ Flakes (Dry Feed System)</option>
              </select>
            </div>
            <div class="form-group">
              <label for="chlorineSource">Co-Reactant Oxidant Method</label>
              <select id="chlorineSource" class="form-control">
                <option value="gas_cl2" selected>Chlorine Gas (Cl₂) - 2-Chemical Generator (0.53 lb Cl₂/lb ClO₂)</option>
                <option value="bleach_acid">Sodium Hypochlorite (NaOCl) + Hydrochloric Acid (HCl) - 3-Chem</option>
              </select>
            </div>
          </div>

          <div id="metalStoichGrid" class="grid-2-col">
            <div class="form-group">
              <label for="rawIron">Raw Dissolved Iron Fe²⁺ (mg/L)</label>
              <input type="number" id="rawIron" class="form-control" value="0.45" step="0.05" min="0">
              <span class="field-hint">Consumes 1.20 mg/L ClO₂ per mg/L Fe</span>
            </div>
            <div class="form-group">
              <label for="rawManganese">Raw Dissolved Manganese Mn²⁺ (mg/L)</label>
              <input type="number" id="rawManganese" class="form-control" value="0.15" step="0.01" min="0">
              <span class="field-hint">Consumes 2.45 mg/L ClO₂ per mg/L Mn</span>
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="costChlorite">25% Sodium Chlorite Cost ($ / Gallon)</label>
              <input type="number" id="costChlorite" class="form-control" value="4.80" step="0.10" min="0">
            </div>
            <div class="form-group">
              <label for="dutyGenPumps">Generator Feed Tubes / Pumps</label>
              <input type="number" id="dutyGenPumps" class="form-control" value="1" step="1" min="1" max="3">
            </div>
          </div>

          <button type="button" class="btn btn-primary" onclick="calcChlorineDioxide()">Calculate Chlorine Dioxide Feed &amp; Precursors</button>
        </div>

        <div id="clO2Results" class="results-box" style="display:none;margin-top:1.5rem;">
          <h3 class="results-title">Chlorine Dioxide Generation &amp; Precursor Sizing</h3>
          <div class="result-grid">
            <div class="result-card">
              <div class="result-label">Pure ClO₂ Generation Rate</div>
              <div class="result-value highlight" id="resPureClO2">--</div>
              <div class="result-subtext" id="resPureClO2Alt">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Sodium Chlorite Feed Rate</div>
              <div class="result-value highlight" id="resChloriteFeed">--</div>
              <div class="result-subtext" id="resChloriteFeedAlt">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Co-Reactant Chlorine Demand</div>
              <div class="result-value" id="resCl2Demand">--</div>
              <div class="result-subtext" id="resCl2DemandAlt">Pure oxidant feed</div>
            </div>
            <div class="result-card">
              <div class="result-label">Predicted Chlorite By-Product</div>
              <div class="result-value" id="resChloriteIon">--</div>
              <div class="result-subtext" id="resMclStatus">--</div>
            </div>
          </div>

          <div class="result-details" style="margin-top:1rem;padding:1rem;background:var(--card-bg);border-radius:6px;border:1px solid var(--border-light);">
            <h4 style="margin-top:0;">Oxidation Stoichiometry &amp; Regulatory Diagnostics</h4>
            <ul style="margin-bottom:0;line-height:1.7;">
              <li><strong>Iron &amp; Manganese Oxidation Demand:</strong> <span id="resMetalDemand">--</span></li>
              <li><strong>Net Available Free ClO₂ for Disinfection:</strong> <span id="resNetDisinfDose">--</span></li>
              <li><strong>Liquid Precursor Storage Usage:</strong> <span id="resPrecursorMonthly">--</span></li>
              <li><strong>Estimated Precursor Chemical Cost:</strong> <span id="resClO2Cost" style="font-weight:700;color:var(--primary);">--</span></li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Related Category Sidebar -->
      <aside class="post-sidebar">
        <div class="sidebar-widget">
          <div class="sidebar-widget-header">
            <span class="widget-icon">🧪</span>
            <h3 class="widget-title">Related Chemical Calculators</h3>
          </div>
          <p class="sidebar-widget-subtitle">Specialized calculation tools in this discipline:</p>
          <ul class="sidebar-links-list">
            <li><a href="chlorine-dosing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Chlorine Dosing Calculator</a></li>
            <li><a href="calcium-hypochlorite-dosing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Calcium Hypochlorite Dosing</a></li>
            <li><a href="alum-dosing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Alum Dosing Calculator</a></li>
            <li><a href="caustic-soda-dosing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Caustic Soda Dosing Calculator</a></li>
          </ul>
          <div style="margin-top:1.25rem;padding-top:1rem;border-top:1px solid var(--border-light);">
            <a href="chemical.html" class="sidebar-category-link">View All Chemical Calculators &rarr;</a>
          </div>
        </div>
      </aside>
    </div>

    <!-- Technical Educational Article Body (1000+ Words) -->
    <article class="article-body">
      <h2>Advanced Oxidation Chemistry of Chlorine Dioxide in Water Treatment</h2>
      <p>Chlorine dioxide ($\text{ClO}_2$, molecular weight $67.45\text{ g/mol}$) is a potent synthetic free radical gas that occupies a uniquely advantageous niche in municipal water clarification, industrial odor control, and pulp bleaching. While elemental chlorine ($\text{Cl}_2$) and hypochlorite salts hydrolyze into hypochlorous acid ($\text{HOCl}$) and undergo electrophilic aromatic substitution reactions with natural organic matter (NOM)—generating carcinogenic trihalomethanes (chloroform, bromoform) and haloacetic acids—chlorine dioxide reacts predominantly via single-electron transfer oxidation pathways:</p>

      <div class="formula-box">
        $$\text{ClO}_2 + e^- \longrightarrow \text{ClO}_2^- \quad (E^\circ = 0.954 \, \text{V vs. SHE})$$
      </div>

      <p>Because $\text{ClO}_2$ does not chlorinate organic carbon, it forms virtually zero regulated THMs or HAA5s. Furthermore, unlike chlorine, whose biocidal potency drops by over 90% as pH climbs from 7.0 to 8.5 due to $\text{HOCl}$ deprotonation into the weak $\text{OCl}^-$ ion, chlorine dioxide exists as an uncharged dissolved gas across the entire drinking water pH spectrum ($\text{pH } 4.0\text{ to }10.0$). Its biocidal efficacy against encysted protozoans (<em>Cryptosporidium parvum</em> and <em>Giardia lamblia</em>) is roughly 10 to 50 times greater than free chlorine.</p>

      <h2>On-Site Generation Chemistry and Reaction Stoichiometry</h2>
      <p>Chlorine dioxide cannot be liquefied and transported in commercial cylinders because concentrated gas mixtures exceeding 10% in air ($P_{\text{partial}} &gt; 100\text{ mmHg}$) are thermally unstable and undergo explosive exothermic decomposition into chlorine and oxygen ($\text{ClO}_2 \to \frac{1}{2}\text{Cl}_2 + \text{O}_2 + \text{Heat}$). Consequently, all municipal and industrial $\text{ClO}_2$ must be synthesized on-site using vacuum-educted chemical generators.</p>

      <p>The predominant municipal method is the <strong>Two-Chemical Chlorine Gas / Sodium Chlorite Process</strong> per AWWA B303:</p>
      <div class="formula-box">
        $$2\text{NaClO}_2 + \text{Cl}_2\text{ (g)} \longrightarrow 2\text{ClO}_2\text{ (aq)} + 2\text{NaCl}$$
      </div>

      <p>Evaluating stoichiometry based on molar masses ($\text{MW}_{\text{NaClO}_2} = 90.44\text{ g/mol}$, $\text{MW}_{\text{Cl}_2} = 70.91\text{ g/mol}$, $\text{MW}_{\text{ClO}_2} = 67.45\text{ g/mol}$):</p>
      <div class="formula-box">
        $$\text{Theoretical NaClO}_2\text{ Demand} = \frac{2 \times 90.44}{2 \times 67.45} = 1.341 \, \frac{\text{lb pure NaClO}_2}{\text{lb ClO}_2}$$
        $$\text{Theoretical Cl}_2\text{ Demand} = \frac{70.91}{2 \times 67.45} = 0.526 \, \frac{\text{lb Cl}_2}{\text{lb ClO}_2}$$
      </div>

      <p>Accounting for operational generator efficiency ($\eta_{\text{gen}}$, typically $92\%\text{ to }98\%$):</p>
      <div class="formula-box">
        $$\text{Actual Pure NaClO}_2 \, (\text{lb/day}) = \frac{\text{ClO}_2 \, (\text{lb/day}) \times 1.341}{\eta_{\text{gen}} / 100}$$
      </div>

      <h2>Mathematical Sizing Formulas for Feed Streams</h2>
      <p>The pure chlorine dioxide chemical mass rate ($W_{\text{ClO}_2}$) required for plant flow ($Q$) and target applied dosage ($C_{\text{applied}}$) is:</p>

      <div class="formula-box">
        $$W_{\text{ClO}_2} \, (\text{lb/day}) = Q \, (\text{MGD}) \times C_{\text{applied}} \, (\text{mg/L}) \times 8.34 \, \left(\frac{\text{lb/Mgal}}{\text{mg/L}}\right)$$
      </div>

      <p>In metric units:</p>
      <div class="formula-box">
        $$W_{\text{ClO}_2} \, (\text{kg/day}) = \frac{Q \, (\text{m}^3/\text{day}) \times C_{\text{applied}} \, (\text{g/m}^3)}{1,000}$$
      </div>

      <p>Commercial sodium chlorite is universally supplied as an aqueous solution, most commonly <strong>$25\%\text{ active NaClO}_2$</strong> by weight ($SG = 1.21$, density $10.09\text{ lb/gal}$, containing $2.52\text{ lb pure NaClO}_2\text{ per gallon}$) or $31.25\%$ active ($SG = 1.27$, containing $3.31\text{ lb active/gal}$). The precursor volumetric pump feed rate is:</p>

      <div class="formula-box">
        $$Q_{\text{chlorite}} \, (\text{gal/day}) = \frac{\text{Actual Pure NaClO}_2 \, (\text{lb/day})}{\text{Active lb NaClO}_2 / \text{gal}}$$
        $$\text{Pump Calibration Rate} \, (\text{mL/min}) = Q_{\text{chlorite}} \, (\text{GPD}) \times 2.6288$$
      </div>

      <h2>Stoichiometry of Iron, Manganese, and Sulfide Pre-Oxidation</h2>
      <p>Chlorine dioxide reacts rapidly with reduced inorganic minerals commonly encountered in deep groundwater wells and stratified surface reservoirs:</p>
      <ul>
        <li><strong>Ferrous Iron ($\text{Fe}^{2+} \to \text{Fe}^{3+}$):</strong> Rapid oxidation occurs within seconds over $\text{pH } 5.0\text{ to }9.0$, precipitating insoluble ferric hydroxide flocs:
        $$\text{ClO}_2 + 5\text{Fe}^{2+} + 10\text{H}_2\text{O} \longrightarrow 5\text{Fe(OH)}_3\downarrow + \text{Cl}^- + 5\text{H}^+$$
        Theoretical demand: <strong>$1.20\text{ mg/L ClO}_2$ per $1.0\text{ mg/L Fe}^{2+}$</strong>.</li>
        <li><strong>Soluble Manganese ($\text{Mn}^{2+} \to \text{MnO}_2$):</strong> Chlorine dioxide oxidizes manganous ions significantly faster than chlorine or potassium permanganate, eliminating black water customer complaints:
        $$2\text{ClO}_2 + 5\text{Mn}^{2+} + 6\text{H}_2\text{O} \longrightarrow 5\text{MnO}_2\downarrow + 2\text{Cl}^- + 12\text{H}^+$$
        Theoretical demand: <strong>$2.45\text{ mg/L ClO}_2$ per $1.0\text{ mg/L Mn}^{2+}$</strong>.</li>
        <li><strong>Hydrogen Sulfide ($\text{H}_2\text{S}$ / Sulfides):</strong> Eliminates rotten egg odors without producing colloidal sulfur turbidity:
        $$\text{Demand: } 2.60\text{ mg/L ClO}_2 \text{ per } 1.0\text{ mg/L H}_2\text{S} \text{ (oxidizing sulfide completely to sulfate } \text{SO}_4^{2-}\text{)}$$
        </li>
      </ul>

      <h2>EPA Regulatory Compliance: Disinfection By-Product Caps</h2>
      <p>The primary engineering constraint on chlorine dioxide dosing is the strict federal threshold mandated under the EPA Stage 1 and Stage 2 Disinfectants and Disinfection Byproducts Rules (D/DBPR):</p>
      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Regulated Chemical Entity</th>
              <th>EPA Regulatory Standard</th>
              <th>Compliance Metric</th>
              <th>Health / Operational Concern</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Chlorine Dioxide Residual (ClO₂)</td>
              <td>MRDL = 0.80 mg/L</td>
              <td>Daily samples at entry to distribution system</td>
              <td>Methemoglobinemia (neurotoxicity in infants)</td>
            </tr>
            <tr>
              <td>Chlorite Ion By-product (ClO₂⁻)</td>
              <td>MCL = 1.00 mg/L</td>
              <td>Monthly 3-sample average in distribution network</td>
              <td>Hemolytic anemia and embryonic development</td>
            </tr>
            <tr>
              <td>Chlorate Ion By-product (ClO₃⁻)</td>
              <td>EPA Health Advisory: 0.21 mg/L</td>
              <td>Unregulated Contaminant Monitoring Rule (UCMR)</td>
              <td>Thyroid function inhibition and oxidative stress</td>
            </tr>
          </tbody>
        </table>
      </div>

      <p>When chlorine dioxide oxidizes organic matter or reduced minerals, approximately <strong>$50\%\text{ to }70\%$</strong> of the applied dose is converted into dissolved chlorite ion ($\text{ClO}_2^-$). Because chlorite is regulated at an MCL of $1.0\text{ mg/L}$, utilities without post-treatment ferrous iron or activated carbon chlorite reduction systems cannot apply initial $\text{ClO}_2$ doses exceeding $1.4\text{ to }1.5\text{ mg/L}$:</p>

      <div class="formula-box">
        $$[\text{ClO}_2^-]_{\text{predicted}} \approx C_{\text{applied}} \times 0.65 \le 1.00 \, \text{mg/L}$$
      </div>

      <h2>Practical Worked Case Study: Surface Water Plant Iron/Manganese Removal</h2>
      <div class="worked-example-card">
        <h3>Engineering Design Example: 10.0 MGD Reservoir Pre-Oxidation</h3>
        <p><strong>System Scenario:</strong> A municipal water filtration plant processes an average flow rate of $10.0\text{ MGD}$. Stratification in the source reservoir produces cold, anoxic hypolimnion water with dissolved ferrous iron $\text{Fe}^{2+} = 0.50\text{ mg/L}$ and dissolved manganese $\text{Mn}^{2+} = 0.18\text{ mg/L}$. The utility installs a two-chemical vacuum $\text{ClO}_2$ generator ($95\%$ chemical efficiency) utilizing $25\%\text{ active NaClO}_2$ solution ($SG = 1.21$, $2.52\text{ lb active/gal}$) and chlorine gas cylinders. Precursor chlorite costs $\$4.80/\text{gal}$.</p>

        <p><strong>Step 1: Calculate Minimum Stoichiometric Inorganic Demand:</strong></p>
        $$\text{Iron Demand} = 0.50\text{ mg/L Fe} \times 1.20 = 0.60\text{ mg/L ClO}_2$$
        $$\text{Manganese Demand} = 0.18\text{ mg/L Mn} \times 2.45 = 0.441\text{ mg/L ClO}_2$$
        $$\text{Total Inorganic Demand} = 0.60 + 0.441 = 1.041\text{ mg/L ClO}_2$$
        <p>Adding a safety margin of $0.25\text{ mg/L}$ for baseline primary disinfection yielding a total applied dosage of $C_{\text{applied}} = 1.29\text{ mg/L ClO}_2$.</p>

        <p><strong>Step 2: Determine Daily Pure ClO₂ Generation:</strong></p>
        $$W_{\text{ClO}_2} = 10.0\text{ MGD} \times 1.29\text{ mg/L} \times 8.34 = 107.59\text{ lb/day pure ClO}_2\text{ (48.80 kg/day)}$$

        <p><strong>Step 3: Calculate Sodium Chlorite &amp; Chlorine Precursor Requirements:</strong></p>
        <p>Pure active $\text{NaClO}_2$ at $95\%$ generator yield:</p>
        $$W_{\text{active chlorite}} = \frac{107.59\text{ lb} \times 1.341}{0.95} = \frac{144.27}{0.95} = 151.86\text{ lb/day dry active NaClO}_2$$
        <p>Liquid $25\%$ commercial chlorite solution volume ($2.52\text{ lb active/gal}$):</p>
        $$Q_{\text{chlorite}} = \frac{151.86\text{ lb/day}}{2.52\text{ lb/gal}} = 60.26\text{ gal/day (2.51 GPH)}$$
        $$\text{Metering Pump Calibration} = 60.26\text{ GPD} \times 2.6288 = 158.4\text{ mL/min}$$
        <p>Co-reactant chlorine gas demand:</p>
        $$W_{\text{Cl}_2\text{ gas}} = 107.59\text{ lb ClO}_2 \times 0.526 = 56.59\text{ lb/day chlorine gas}$$

        <p><strong>Step 4: Verify EPA Chlorite By-Product MCL Compliance:</strong></p>
        $$[\text{ClO}_2^-]_{\text{predicted}} = 1.29\text{ mg/L} \times 0.65 = 0.839\text{ mg/L}$$
        <p>Because $0.839\text{ mg/L} &lt; 1.00\text{ mg/L}$, finished water complies with the EPA Disinfection Byproduct Rule MCL without supplemental chlorite scavenging.</p>

        <p><strong>Step 5: Precursor Chemical Operating Budget:</strong></p>
        $$\text{Daily Chlorite Cost} = 60.26\text{ GPD} \times \$4.80/\text{gal} = \$289.25/\text{day (\$8,677 / month)}$$
      </div>

      <h2>Operational Safety and Generator Maintenance</h2>
      <p>Handling sodium chlorite and generating chlorine dioxide mandates strict industrial hygiene protocols:</p>
      <ul>
        <li><strong>Sodium Chlorite Explosion Hazard:</strong> Dried sodium chlorite spills become ultra-sensitive explosives upon contact with combustible organic matter (wood, rags, leather boots). Any spill of precursor solution must immediately be flooded with copious water; never use cellulose mops or paper towels.</li>
        <li><strong>Vacuum Fail-Safe Loop:</strong> Modern generators operate under continuous vacuum created by a water-driven Venturi eductor. If water flow is interrupted or motive pressure drops, mechanical vacuum check valves instantly snap shut, preventing unreacted gas from escaping into the chemical room.</li>
        <li><strong>Photolytic Degradation:</strong> Chlorine dioxide gas in clear water decomposes rapidly when exposed to sunlight ($\text{UV}$ photolysis half-life under direct noon sun is under 20 minutes). Store generator discharge solutions in dark, opaque piping or schedule injection directly into covered rapid mix chambers.</li>
      </ul>
    </article>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-grid">
        <div class="footer-col">
          <div class="footer-logo">
            <span class="logo-icon">&pi;</span>
            <span class="logo-text">Calc<strong>Hub</strong></span>
          </div>
          <p class="footer-about">High-precision chemical oxidation, disinfection by-product modeling, and water engineering calculation tools conforming to AWWA and EPA standards.</p>
        </div>
        <div class="footer-col">
          <h4 class="footer-title">Engineering Disciplines</h4>
          <ul class="footer-links">
            <li><a href="chemical.html">Chemical &amp; Water Treatment</a></li>
            <li><a href="civil.html">Civil &amp; Construction</a></li>
            <li><a href="mechanical.html">Mechanical &amp; HVAC</a></li>
            <li><a href="engineering.html">Electrical &amp; Electronics</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4 class="footer-title">Standard References</h4>
          <ul class="footer-links">
            <li><a href="https://www.awwa.org" target="_blank" rel="noopener">AWWA B303 (Sodium Chlorite)</a></li>
            <li><a href="https://www.epa.gov" target="_blank" rel="noopener">EPA Stage 2 DBPR Guidelines</a></li>
            <li><a href="https://www.waterrf.org" target="_blank" rel="noopener">Water Research Foundation</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    function updateClO2Preset() {
      const mode = document.getElementById("clO2AppMode").value;
      const target = document.getElementById("appliedDose");
      if (mode === "iron_manganese") {
        const fe = parseFloat(document.getElementById("rawIron").value) || 0;
        const mn = parseFloat(document.getElementById("rawManganese").value) || 0;
        const stoich = (fe * 1.20) + (mn * 2.45) + 0.25;
        target.value = Math.min(2.0, Math.max(0.5, stoich)).toFixed(2);
      } else if (mode === "taste_odor") {
        target.value = "0.80";
      } else if (mode === "primary_disinf") {
        target.value = "1.20";
      } else if (mode === "phenolic_destr") {
        target.value = "2.50";
      }
    }

    function toggleClO2FlowLabels() {
      const u = document.getElementById("clO2FlowUnit").value;
      const lbl = document.getElementById("clO2FlowLabel");
      if (u === "mgd") lbl.textContent = "Water Flow Rate (MGD)";
      else if (u === "gpm") lbl.textContent = "Water Flow Rate (GPM)";
      else if (u === "m3h") lbl.textContent = "Water Flow Rate (m³/hour)";
      else if (u === "m3d") lbl.textContent = "Water Flow Rate (m³/day)";
      else if (u === "lps") lbl.textContent = "Water Flow Rate (L/s)";
    }

    function calcChlorineDioxide() {
      const u = document.getElementById("clO2FlowUnit").value;
      const flowIn = parseFloat(document.getElementById("clO2FlowVal").value) || 0;
      const dose = parseFloat(document.getElementById("appliedDose").value) || 0;
      const yieldPct = parseFloat(document.getElementById("genYield").value) || 95;
      const grade = document.getElementById("chloriteGrade").value;
      const fe = parseFloat(document.getElementById("rawIron").value) || 0;
      const mn = parseFloat(document.getElementById("rawManganese").value) || 0;
      const pumps = parseInt(document.getElementById("dutyGenPumps").value) || 1;
      const costGal = parseFloat(document.getElementById("costChlorite").value) || 0;

      if (flowIn <= 0 || dose <= 0) {
        alert("Please enter positive values for plant flow and applied ClO2 dosage.");
        return;
      }

      // Convert flow to MGD and m3/day
      let flowMGD = 0;
      let flowM3D = 0;
      if (u === "mgd") {
        flowMGD = flowIn;
        flowM3D = flowMGD * 3785.41;
      } else if (u === "gpm") {
        flowMGD = (flowIn * 1440) / 1000000;
        flowM3D = flowMGD * 3785.41;
      } else if (u === "m3h") {
        flowM3D = flowIn * 24;
        flowMGD = flowM3D / 3785.41;
      } else if (u === "m3d") {
        flowM3D = flowIn;
        flowMGD = flowM3D / 3785.41;
      } else if (u === "lps") {
        flowM3D = (flowIn * 86400) / 1000;
        flowMGD = flowM3D / 3785.41;
      }

      // Pure ClO2 lb/day
      const pureClO2Lbs = flowMGD * dose * 8.34;
      const pureClO2Kg = pureClO2Lbs * 0.453592;

      // Pure NaClO2 needed
      const pureChloriteLbs = (pureClO2Lbs * 1.341) / (yieldPct / 100);
      const pureChloriteKg = pureChloriteLbs * 0.453592;

      // Cl2 demand (2-chem)
      const pureCl2Lbs = pureClO2Lbs * 0.526;
      const pureCl2Kg = pureCl2Lbs * 0.453592;

      // Solution concentration
      let activeLbPerGal = 2.52; // 25%
      let isDry = false;
      if (grade === "25_liquid") {
        activeLbPerGal = 2.52;
      } else if (grade === "31_liquid") {
        activeLbPerGal = 3.31;
      } else {
        isDry = true;
      }

      const liquidGPD = isDry ? 0 : pureChloriteLbs / activeLbPerGal;
      const liquidGPH = liquidGPD / 24;
      const mlMinPerPump = (liquidGPD / pumps) * 2.6288;
      const lphPerPump = ((liquidGPD / pumps) * 3.78541) / 24;

      // By-product chlorite estimate (~65% conversion)
      const chloriteIonEst = dose * 0.65;
      const isMclCompliant = chloriteIonEst <= 1.0;

      // Metal demand
      const metalDemand = (fe * 1.20) + (mn * 2.45);
      const netResidual = Math.max(0, dose - metalDemand);

      const dailyCost = isDry ? (pureChloriteLbs / 0.80) * 1.50 : liquidGPD * costGal;

      // UI update
      document.getElementById("resPureClO2").textContent = pureClO2Lbs.toFixed(1) + " lbs/day";
      document.getElementById("resPureClO2Alt").textContent = pureClO2Kg.toFixed(1) + " kg/day pure ClO₂ gas generated";

      if (isDry) {
        document.getElementById("resChloriteFeed").textContent = (pureChloriteLbs / 0.80).toFixed(1) + " lbs/day";
        document.getElementById("resChloriteFeedAlt").textContent = "80% active dry flakes (" + ((pureChloriteLbs / 0.80) / (pumps * 24)).toFixed(2) + " lbs/hr per feeder)";
      } else {
        document.getElementById("resChloriteFeed").textContent = mlMinPerPump.toFixed(1) + " mL/min";
        document.getElementById("resChloriteFeedAlt").textContent = lphPerPump.toFixed(2) + " L/h (" + (liquidGPH / pumps).toFixed(2) + " GPH per pump, " + liquidGPD.toFixed(1) + " GPD total)";
      }

      document.getElementById("resCl2Demand").textContent = pureCl2Lbs.toFixed(1) + " lbs/day Cl₂";
      document.getElementById("resCl2DemandAlt").textContent = pureCl2Kg.toFixed(1) + " kg/day (or " + (pureClO2Lbs * 0.88).toFixed(1) + " GPD 12.5% bleach)";

      document.getElementById("resChloriteIon").textContent = chloriteIonEst.toFixed(2) + " mg/L ClO₂⁻";
      const mclEl = document.getElementById("resMclStatus");
      if (isMclCompliant) {
        mclEl.textContent = "Compliant with EPA 1.00 mg/L MCL cap";
        mclEl.style.color = "var(--success, #16a34a)";
      } else {
        mclEl.textContent = "WARNING: Exceeds EPA 1.00 mg/L Chlorite MCL! Lower dose or add ferrous.";
        mclEl.style.color = "#dc2626";
      }

      document.getElementById("resMetalDemand").textContent = metalDemand.toFixed(2) + " mg/L (" + fe.toFixed(2) + " mg/L Fe consumes " + (fe*1.2).toFixed(2) + " + " + mn.toFixed(2) + " mg/L Mn consumes " + (mn*2.45).toFixed(2) + " ClO₂)";
      document.getElementById("resNetDisinfDose").textContent = netResidual.toFixed(2) + " mg/L available for microbial disinfection / CT credit";
      document.getElementById("resPrecursorMonthly").textContent = isDry ? ((pureChloriteLbs / 0.80) * 30).toLocaleString(undefined, {maximumFractionDigits: 0}) + " lbs dry flakes / month" : (liquidGPD * 30).toLocaleString(undefined, {maximumFractionDigits: 0}) + " gallons / month (" + ((liquidGPD * 30 * 10.1) / 2000).toFixed(1) + " tons)";
      document.getElementById("resClO2Cost").textContent = "$" + dailyCost.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2}) + " / day ($" + (dailyCost * 30).toLocaleString(undefined, {maximumFractionDigits: 0}) + " / month)";

      document.getElementById("clO2Results").style.display = "block";
    }
  </script>
</body>
</html>
"""

def generate():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p1 = os.path.join(root, "charles-law-calculator.html")
    p2 = os.path.join(root, "chlorine-dioxide-dosing-calculator.html")
    
    with open(p1, "w", encoding="utf-8") as f:
        f.write(TOOL_7_HTML.strip() + "\n")
    print(f"Generated {p1}")

    with open(p2, "w", encoding="utf-8") as f:
        f.write(TOOL_8_HTML.strip() + "\n")
    print(f"Generated {p2}")

if __name__ == "__main__":
    generate()
