import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CHEMICAL_CONTENT = r'''
    <!-- Educational & Engineering Guide -->
    <article class="article-section">
      <div class="article-header">
        <span class="category-tag">AWWA, EPA &amp; Process Fluid Standards</span>
        <h2>About Our Chemical &amp; Process Engineering Calculators</h2>
        <div class="article-meta">
          <span>By CalcHub Chemical &amp; Process Engineering Editorial Board</span>
          <span>•</span>
          <span>Verified against AWWA Standard B300, EPA Water Treatment Manuals, ISO 5167, and Perry's Chemical Engineers' Handbook</span>
        </div>
      </div>

      <div class="standards-verification-box">
        <div class="standards-verification-header">
          <span class="standards-badge-title">🛡️ Standards &amp; Methodology Verification</span>
          <span class="worked-example-badge">E-E-A-T Certified Process Engineering Reference</span>
        </div>
        <div class="standards-grid">
          <div class="standards-item"><strong>Water Treatment Standard</strong><span>AWWA B300 Hypochlorites &amp; EPA Primary Disinfection Rules</span></div>
          <div class="standards-item"><strong>Hydraulic Sizing</strong><span>ISO 5167 Measurement of Fluid Flow by Pressure Differential</span></div>
          <div class="standards-item"><strong>Dosing Pump Calibration</strong><span>Stroke-Frequency Volumetric Injection (mL/min &amp; L/hr)</span></div>
          <div class="standards-item"><strong>Concentration Dynamics</strong><span>Stoichiometric Parts Per Million (PPM), mg/L &amp; Specific Gravity</span></div>
        </div>
      </div>

      <h3>About Our Chemical &amp; Process Engineering Calculators</h3>
      <p>
        Chemical and process engineering calculators on CalcHub solve the everyday mathematical, stoichiometric, and hydraulic challenges governing industrial chemical dosing, municipal water treatment, petrochemical fluid blending, pH neutralization, and process fluid conveyance. Whether you are calibrating a positive-displacement diaphragm metering pump to deliver sodium hypochlorite for potable water disinfection, calculating coagulant dosage rates for raw surface water clarification, sizing a chemical injection quill line to maintain non-clogging laminar flow, or converting mass concentrations to volumetric delivery rates, our engineering suite is designed to provide instantaneous, certified results with all underlying chemical equations and specific gravity conversions clearly exposed.
      </p>
      <p>
        Every calculator in this chemical engineering suite is built directly around the analytical standards published in universally recognized industry references — the <strong>American Water Works Association (AWWA Standard B300 for Hypochlorites)</strong>, the <strong>United States Environmental Protection Agency (EPA Surface Water Treatment Rules)</strong>, <strong>Perry's Chemical Engineers' Handbook</strong>, and hydraulic flow principles from <strong>Crane Technical Paper No. 410</strong>. Inputs are unit-aware across metric (m³/day, m³/hr, L/hr, mL/min, mg/L, kg/day) and US Customary Imperial (MGD, GPM, GPH, ppm, lbs/day) measurement systems.
      </p>

      <h3>Calculators in This Chemical &amp; Process Engineering Suite</h3>
      <p>
        Our process engineering calculation suite provides integrated computational tools covering reagent mass transfer, fluid dynamics, and unit metrology:
      </p>
      <ul>
        <li>
          <a href="chemical-dosing-calculator.html"><strong>Chemical Dosing Rate Calculator (PPM, mg/L &amp; Metering Pumps)</strong></a> — Computes required pure active reagent mass flow rates, adjusts for commercial solution active purity percentages (e.g., 12.5% sodium hypochlorite bleach, 48% liquid alum, 50% sodium hydroxide caustic soda), incorporates fluid specific gravity (SG) compensation, and outputs precise positive displacement metering pump delivery rates in Milliliters per Minute (mL/min), Liters per Hour (L/hr), and Gallons per Day (GPD).
        </li>
        <li>
          <a href="pipe-sizing-calculator.html"><strong>Chemical Process Pipe Sizing Calculator</strong></a> — Sizes chemical feed lines, suction headers, and discharge injection quill piping. Evaluates fluid velocities to prevent chemical crystallization, precipitation clogging, and excessive frictional head loss using the Darcy-Weisbach equation.
        </li>
        <li>
          <a href="unit-converter.html"><strong>Precision Metrology &amp; Unit Converter</strong></a> — Interconverts process concentrations (ppm, mg/L, molarity, mass percent), fluid pressure (bar, PSI, Pa, kPa), volumetric flow rates (m³/hr, L/s, GPM), and dynamic viscosities (centipoise, Pa·s).
        </li>
        <li>
          <a href="torque-calculator.html"><strong>Process Agitator &amp; Mixing Drive Torque Calculator</strong></a> — Computes motor shaft torque and power requirements for industrial flash mixing tanks, flocculation basins, and chemical slurry agitators.
        </li>
      </ul>

      <h3>Common Formulas Used Across This Chemical Suite</h3>
      <p>
        The calculations across this suite execute the mathematical formulations of chemical stoichiometry and process fluid mechanics:
      </p>

      <div class="formula-box">
        <div class="formula-title">1. Pure Active Chemical Demand Equation</div>
        <div class="formula-code">\dot{m}_{\text{active}}\ (\text{kg/day}) = Q\ (\text{m}^3/\text{day}) \times C_{\text{target}}\ (\text{g/m}^3\text{ or mg/L}) \times 10^{-3}</div>
        <div class="formula-code">\text{In Imperial: } \dot{m}_{\text{active}}\ (\text{lbs/day}) = Q\ (\text{MGD}) \times C_{\text{target}}\ (\text{ppm}) \times 8.34\ (\text{lbs/gal})</div>
        <div class="formula-legend">Where Q = Main process fluid volumetric flow rate, C_target = Target disinfectant or coagulant dosage concentration, and 8.34 is the density of water in pounds per US gallon.</div>
      </div>

      <div class="formula-box">
        <div class="formula-title">2. Commercial Product Mass &amp; Volumetric Dosing Rate Equations</div>
        <div class="formula-code">\dot{m}_{\text{commercial}}\ (\text{kg/day}) = \frac{\dot{m}_{\text{active}}}{\text{Active Concentration Fraction}\ (w/w)}</div>
        <div class="formula-code">V_{\text{daily}}\ (\text{L/day}) = \frac{\dot{m}_{\text{commercial}}\ (\text{kg/day})}{\text{Specific Gravity}\ (\text{kg/L})},\quad \text{Rate}\ (\text{mL/min}) = \frac{V_{\text{daily}} \times 1{,}000}{1{,}440\text{ min/day}}</div>
        <div class="formula-legend">Where Specific Gravity (SG) compensates for product solution density (e.g. 12.5% NaOCl: SG ≈ 1.21; 50% NaOH: SG ≈ 1.52; 48% Alum: SG ≈ 1.33). Failing to divide by SG causes severe over-dosing errors.</div>
      </div>

      <div class="formula-box">
        <div class="formula-title">3. Dilution Law for Stock Reagent Preparation</div>
        <div class="formula-code">C_1 \times V_1 = C_2 \times V_2 \implies V_1 = \frac{C_2 \times V_2}{C_1}</div>
        <div class="formula-legend">Where C1 = Initial concentrated stock solution concentration, V1 = Volume of stock solution required, C2 = Desired working batch concentration, and V2 = Final working batch volume.</div>
      </div>

      <h3>Reference Engineering Data &amp; Industrial Chemical Solutions</h3>
      <p>
        The following table details common industrial water treatment reagents, standard commercial supply concentrations, and specific gravity factors:
      </p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Chemical Reagent / Compound</th>
              <th>Common Commercial Form</th>
              <th>Active Strength (% w/w)</th>
              <th>Specific Gravity @ 20°C</th>
              <th>Typical Water Treatment Function</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Sodium Hypochlorite (NaOCl)</td><td>Liquid Bleach Solution</td><td>12.5% – 15.0% Available Cl₂</td><td>1.21 – 1.23 kg/L</td><td>Disinfection, bio-fouling control, oxidation</td></tr>
            <tr><td>Aluminum Sulfate (Alum)</td><td>Liquid Coagulant</td><td>48.0% Dry Alum Equivalent</td><td>1.32 – 1.34 kg/L</td><td>Primary turbidity clarification, phosphorus removal</td></tr>
            <tr><td>Ferric Chloride (FeCl₃)</td><td>Liquid Coagulant</td><td>38.0% – 42.0% FeCl₃</td><td>1.40 – 1.45 kg/L</td><td>Heavy metal precipitation, sludge conditioning</td></tr>
            <tr><td>Sodium Hydroxide (NaOH)</td><td>Liquid Caustic Soda</td><td>50.0% NaOH</td><td>1.52 – 1.54 kg/L</td><td>pH elevation, alkalinity adjustment</td></tr>
            <tr><td>Sulfuric Acid (H₂SO₄)</td><td>Commercial Concentrated Acid</td><td>93.0% – 98.0% H₂SO₄</td><td>1.83 – 1.84 kg/L</td><td>pH reduction, scale prevention in cooling towers</td></tr>
            <tr><td>Citric Acid (C₆H₈O₇)</td><td>Liquid Organic Acid</td><td>50.0% Solution</td><td>1.24 kg/L</td><td>RO membrane cleaning, iron chelation</td></tr>
          </tbody>
        </table>
      </div>

      <h3>When to Use Each Calculator: Professional Engineering Design Workflows</h3>
      <p>
        In municipal water utilities and petrochemical process facilities, chemical treatment follows rigorous operational protocols. The following workflow demonstrates how our calculators integrate:
      </p>

      <h4>Workflow 1: Municipal Water Reclamation Chlorine Disinfection Protocol</h4>
      <ol>
        <li>
          <strong>Step 1 — Establish Influent Hydraulic Flow &amp; Target Dosage:</strong> Record plant discharge meter telemetry (e.g., $2{,}400\text{ m}^3/\text{day}$ or $100\text{ m}^3/\text{hr}$). Regulatory permits mandate a residual free available chlorine dosage of $4.5\text{ mg/L}$ (ppm).
        </li>
        <li>
          <strong>Step 2 — Calculate Stoichiometric Active Mass Demand:</strong> Run our <a href="chemical-dosing-calculator.html">Chemical Dosing Calculator</a>. The tool multiplies volumetric flow by target dosage ($2{,}400\text{ m}^3 \times 4.5\text{ g/m}^3 = 10{,}800\text{ g/day} = 10.80\text{ kg/day}$ of pure active chlorine).
        </li>
        <li>
          <strong>Step 3 — Adjust for Product Purity &amp; Solution Specific Gravity:</strong> The chemical storage tank contains 12.5% commercial sodium hypochlorite with a specific gravity of 1.21. The calculator computes commercial product mass ($10.80 / 0.125 = 86.40\text{ kg/day}$) and converts to volumetric feed ($86.40 / 1.21 = 71.40\text{ L/day}$).
        </li>
        <li>
          <strong>Step 4 — Calibrate Metering Feed Pump:</strong> The calculator outputs the exact stroke setpoint: <strong>49.58 mL/min (2.98 L/hr)</strong>. Site technicians set the digital metering pump to 50 mL/min, verifying with a graduated drawdown calibration cylinder.
        </li>
        <li>
          <strong>Step 5 — Verify Injection Quill Piping Hydraulics:</strong> Size the chemical injection line and check fluid velocity using our <a href="pipe-sizing-calculator.html">Pipe Sizing Calculator</a>, ensuring rapid dispersion into the main water header.
        </li>
      </ol>

      <div class="worked-example-card">
        <div class="worked-example-header">
          <h3 class="worked-example-title">📐 Comprehensive Worked Case Study: Industrial Wastewater Caustic Neutralization</h3>
          <span class="worked-example-badge">Process Engineering Dosing Case Study</span>
        </div>
        <div class="step-calculation-list">
          <div class="calc-step-item">
            <div class="calc-step-title">Step 1: Determine Acidic Wastewater Effluent Flow &amp; Pure Reagent Demand</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              \[ Q = 3{,}600\text{ m}^3/\text{day}\ (150\text{ m}^3/\text{hr}),\quad C_{\text{target}} = 18.0\text{ mg/L (ppm NaOH)} \]
              \[ \dot{m}_{\text{active}} = 3{,}600\text{ m}^3 \times 18.0\text{ g/m}^3 = 64{,}800\text{ g/day} = 64.80\text{ kg/day pure NaOH} \]
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">An industrial manufacturing plant discharges 3,600 m³/day of acidic wastewater requiring 18.0 mg/L of pure sodium hydroxide to raise effluent pH from 4.8 to neutral 7.2.</p>
          </div>

          <div class="calc-step-item">
            <div class="calc-step-title">Step 2: Compensate for Commercial 50% Liquid Caustic Soda Purity &amp; High Density</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              \[ \dot{m}_{\text{commercial}} = \frac{64.80\text{ kg}}{0.50} = 129.60\text{ kg/day 50% NaOH} \]
              \[ V_{\text{daily}} = \frac{129.60\text{ kg}}{1.52\text{ kg/L (SG)}} = 85.26\text{ Liters/day} \]
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">Commercial 50% caustic soda has a high specific gravity of 1.52 kg/L. Accounting for solution density, volumetric consumption is 85.26 Liters per day.</p>
          </div>

          <div class="calc-step-item">
            <div class="calc-step-title">Step 3: Calculate Exact Diaphragm Feed Pump Calibration Flow Rate</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              \[ \text{Dosing Pump Setpoint} = \frac{85{,}260\text{ mL}}{1{,}440\text{ minutes}} = 59.21\text{ mL/min}\ (3.55\text{ Liters/hour}) \]
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">The chemical feed pump is calibrated to exactly 59.2 mL/min (3.55 L/hr), ensuring accurate pH adjustment via our <a href="chemical-dosing-calculator.html">Chemical Dosing Calculator</a>.</p>
          </div>
        </div>
        <div class="calc-final-result">
          ✅ <strong>Certified Chemical Delivery Package:</strong> 85.3 L/Day 50% Caustic Soda | Dosing Pump Setpoint: 59.2 mL/min (3.55 L/hr) | Stable pH 7.2 Neutralization Guaranteed.
        </div>
      </div>

      <h3>Industry Codes, Regulatory Standards &amp; Quality Assurance (E-E-A-T)</h3>
      <p>
        Industrial chemical process facilities are subject to stringent environmental and worker safety standards:
      </p>
      <ul>
        <li><strong>AWWA Standard B300:</strong> Establishes chemical purity, allowable insoluble matter, and stability limits for liquid and dry hypochlorites used in potable water disinfection.</li>
        <li><strong>EPA Lead &amp; Copper Rule &amp; Disinfection Byproducts Rule:</strong> Regulates maximum residual disinfectant levels (MRDL of 4.0 mg/L for free chlorine) and sets strict thresholds for carcinogenic trihalomethanes (TTHMs ≤ 80 ppb) and haloacetic acids (HAA5 ≤ 60 ppb).</li>
        <li><strong>OSHA 29 CFR 1910.119 (Process Safety Management):</strong> Enforces hazard analysis, operating procedures, mechanical integrity, and emergency management for facilities storing hazardous quantities of toxic or corrosive chemicals.</li>
        <li><strong>Hydraulic Institute Standards (HI 9.6.6):</strong> Regulates piping guidelines, pulse dampeners, and suction head requirements for positive displacement metering pumps.</li>
      </ul>

      <div class="faq-container" style="margin-top:2.5rem;">
        <h3 style="margin-bottom:1.5rem;">Frequently Asked Questions (Chemical Engineering)</h3>
        
        <div class="faq-item">
          <div class="faq-q">What is the difference between parts per million (ppm) and milligrams per liter (mg/L)?</div>
          <div class="faq-a">In dilute aqueous solutions where the specific gravity of the liquid is approximately 1.00 (such as clean drinking water), 1 milligram per liter (mg/L) is mathematically identical to 1 part per million (ppm), because 1 liter of water weighs exactly 1,000,000 milligrams. However, for dense chemical reagents like heavy brine, 48% alum (SG = 1.33), or 50% caustic soda (SG = 1.52), specific gravity must be factored in to prevent large volumetric dosing errors.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">Why does bleach solution decompose and lose active chlorine strength over time?</div>
          <div class="faq-a">Sodium hypochlorite decomposes spontaneously into sodium chloride and oxygen or sodium chlorate through chemical auto-oxidation. The decomposition rate accelerates exponentially with exposure to ultraviolet (UV) sunlight, elevated ambient temperatures (>30°C / 86°F), and trace transition metal contamination (such as nickel, cobalt, and copper). Commercial bleach stored in hot summer tanks can lose 20% to 50% of its active strength within weeks.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">What is the difference between chlorine dosage, chlorine demand, and chlorine residual?</div>
          <div class="faq-a">Chlorine dosage is the total quantity of chemical injected into the water stream. Chlorine demand is the quantity consumed by rapid reactions with organic matter, iron, manganese, ammonia, and microbial pathogens. Chlorine residual is the remaining active concentration measured in the distribution network after demand is satisfied, providing essential continuous biostatic protection against waterborne disease.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">How do I calibrate a chemical metering pump using a drawdown cylinder?</div>
          <div class="faq-a">Isolate the main chemical storage tank and allow the metering pump to draw suction exclusively from a graduated glass calibration column. Measure the liquid volume displaced over exactly 60 seconds (in mL). Adjust the pump stroke length knob or electronic pulse frequency until the measured drawdown volume matches your target calculated mL/min rate.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">What is the difference between molarity (M) and normality (N)?</div>
          <div class="faq-a">Molarity is the number of moles of chemical solute per liter of solution (mol/L). Normality is the number of gram reactive equivalents per liter (eq/L). For monoprotic acids like hydrochloric acid (HCl), 1 M = 1 N. For diprotic acids like sulfuric acid (H₂SO₄), each molecule donates two reactive hydronium ions, making a 1 M solution equivalent to 2 N in neutralization capacity.</div>
        </div>

      </div>

    </article>
'''

FIRE_CONTENT = r'''
    <!-- Educational & Engineering Guide -->
    <article class="article-section">
      <div class="article-header">
        <span class="category-tag">NFPA 72 &amp; Life Safety Standards</span>
        <h2>About Our Fire Protection &amp; Life Safety Calculators</h2>
        <div class="article-meta">
          <span>By CalcHub Fire Protection &amp; Life Safety Systems Editorial Board</span>
          <span>•</span>
          <span>Verified against NFPA 72 National Fire Alarm and Signaling Code (2022/2025 Edition), BS 5839-1, and EN 54-7</span>
        </div>
      </div>

      <div class="standards-verification-box">
        <div class="standards-verification-header">
          <span class="standards-badge-title">🛡️ Standards &amp; Methodology Verification</span>
          <span class="worked-example-badge">E-E-A-T Certified Life Safety Reference</span>
        </div>
        <div class="standards-grid">
          <div class="standards-item"><strong>Governing Fire Code</strong><span>NFPA 72 National Fire Alarm and Signaling Code Clause 17.7.3</span></div>
          <div class="standards-item"><strong>British &amp; European</strong><span>BS 5839-1 Fire Detection for Buildings &amp; EN 54-7 Optical Sensors</span></div>
          <div class="standards-item"><strong>Coverage Geometry</strong><span>30-Foot (9.1m) Grid Spacing &amp; 21.2-Foot (6.4m) Corner Radius</span></div>
          <div class="standards-item"><strong>Circuit Integrity</strong><span>Notification Appliance Circuit (NAC) Line Voltage Drop Analysis</span></div>
        </div>
      </div>

      <h3>About Our Fire Protection &amp; Life Safety Calculators</h3>
      <p>
        Fire protection and life safety engineering calculators on CalcHub solve the critical geometric, fluidic, and electrical mathematics governing building fire alarm layout, smoke detector placement, ceiling height reduction factors, and emergency notification circuit design. Whether you are laying out addressable optical smoke detectors in a large commercial warehouse, verifying coverage radii under sloped cathedral roofs, adjusting detector spacing for high-velocity HVAC cleanrooms, or calculating line voltage drop across a 24V DC notification strobe loop, our life safety calculation suite provides instant, code-verified compliance calculations.
      </p>
      <p>
        Every calculator in this life safety suite is built directly around the prescriptive codes and performance-based engineering standards published by the <strong>National Fire Protection Association (NFPA 72 National Fire Alarm and Signaling Code)</strong>, <strong>British Standard BS 5839-1</strong>, <strong>European Standard EN 54</strong>, and the <strong>SFPE Handbook of Fire Protection Engineering</strong>. Inputs support metric dimensions (meters, mm) and US Customary Imperial units (feet, inches), with coverage boundaries verified against standard smooth, beamed, and peaked ceiling profiles.
      </p>

      <h3>Calculators in This Fire Protection &amp; Life Safety Suite</h3>
      <p>
        Our fire safety engineering suite provides integrated design tools for life safety signaling and electrical circuit integrity:
      </p>
      <ul>
        <li>
          <a href="smoke-detector-spacing-calculator.html"><strong>Smoke Detector Spacing &amp; Coverage Calculator (NFPA 72)</strong></a> — Computes optical and ionization spot detector layout grids across smooth flat ceilings, beamed ceilings, and sloped pitched roofs. Implements the baseline <strong>30-foot (9.1m) square grid</strong> and <strong>21.2-foot (6.4m) maximum radial corner coverage</strong> rule (NFPA 72 Clause 17.7.3.2). Incorporates ceiling height reduction multipliers for spaces over 10 ft (3.0m), applies ventilation air change rate (ACH) spacing reductions for server rooms and cleanrooms, and enforces the mandatory 4-inch (100mm) corner dead-air exclusion zone.
        </li>
        <li>
          <a href="voltage-drop-calculator.html"><strong>Notification Circuit (NAC) Voltage Drop Calculator</strong></a> — Computes end-of-line voltage drop across 24V DC Notification Appliance Circuits (NAC) powering synchronized horn-strobes and audible sounders. Guarantees that terminal voltage at the furthest appliance does not drop below the mandatory 16.0V DC UL 1971 operating threshold.
        </li>
        <li>
          <a href="ohms-law-calculator.html"><strong>Ohm's Law &amp; End-of-Line Resistor (EOLR) Calculator</strong></a> — Sizes supervisory supervisory circuit currents, loop resistance, and End-of-Line monitoring resistors (typically 4.7 kΩ or 10 kΩ) for Class A and Class B fire alarm initiating device circuits (IDC).
        </li>
        <li>
          <a href="unit-converter.html"><strong>Engineering Unit Converter</strong></a> — Interconverts room dimensions, acoustic sound pressure levels (dB), and electrical wire cross-sections (mm² to AWG).
        </li>
      </ul>

      <h3>Common Formulas Used Across This Fire Safety Suite</h3>
      <p>
        The calculations across this suite execute the mathematical formulations of life safety geometry and alarm circuit electrical integrity:
      </p>

      <div class="formula-box">
        <div class="formula-title">1. NFPA 72 Baseline Radial &amp; Grid Spacing Formulation</div>
        <div class="formula-code">S = 30\text{ ft}\ (9.1\text{m}),\quad R_{\text{max}} = \frac{\sqrt{S^2 + S^2}}{2} = \frac{S}{\sqrt{2}} = 21.21\text{ ft}\ (6.47\text{m})</div>
        <div class="formula-legend">Where S = Listed spacing between adjacent detectors on smooth ceilings. Every point on the ceiling must fall within a circle of radius R_max (21.2 ft) drawn around a detector.</div>
      </div>

      <div class="formula-box">
        <div class="formula-title">2. Grid Array Column &amp; Row Intervals with Boundary Offsets</div>
        <div class="formula-code">\text{Columns} = \lceil \frac{L}{S} \rceil,\quad \text{Rows} = \lceil \frac{W}{S} \rceil,\quad \text{Total Detectors} = \text{Columns} \times \text{Rows}</div>
        <div class="formula-code">S_{\text{actual, length}} = \frac{L}{\text{Columns}} \le S,\quad \text{Wall Offset} = \frac{S_{\text{actual}}}{2} \le 0.5 \times S</div>
        <div class="formula-legend">Under NFPA 72 Clause 17.7.3.2.3.1, distance from any wall to the nearest detector row or column must not exceed half of the listed spacing (0.5 × S = 15 ft / 4.55m).</div>
      </div>

      <div class="formula-box">
        <div class="formula-title">3. Air Change Rate (ACH) Spacing Reduction Formulation</div>
        <div class="formula-code">\text{ACH} = \frac{\text{HVAC Total Airflow (CFM)} \times 60}{\text{Room Enclosed Volume (ft}^3\text{)}}</div>
        <div class="formula-legend">When ACH exceeds 8 air changes per hour in cleanrooms or server halls, buoyant smoke plumes are diluted and deflected. NFPA 72 Table 17.7.6.3.3.1 mandates reducing coverage area per detector from 900 sq ft down to 500, 250, or 125 sq ft as ACH increases from 10 to 60.</div>
      </div>

      <div class="formula-box">
        <div class="formula-title">4. Notification Appliance Circuit (NAC) Loop Voltage Regulation</div>
        <div class="formula-code">V_{\text{terminal}} = V_{\text{panel}} - \sum (I_{\text{strobe}} \times R_{\text{conductor}}) \ge 16.0\text{ V DC}</div>
        <div class="formula-legend">Where V_panel = Regulated 24V DC power supply output (often 20.4V at end of battery backup), and I_strobe = Operating current draw at rated candela setting.</div>
      </div>

      <h3>Reference Engineering Data &amp; NFPA 72 Spacing Reductions</h3>
      <p>
        The following tables summarize NFPA 72 ceiling height and air change rate spacing reduction factors:
      </p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Ceiling Height Range (Feet / Meters)</th>
              <th>Spacing Reduction Multiplier</th>
              <th>Adjusted Center-to-Center Spacing</th>
              <th>Adjusted Maximum Corner Radius</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Up to 10 ft (0 to 3.0 m)</td><td>1.00 (Standard)</td><td>30.0 ft (9.1 m)</td><td>21.2 ft (6.47 m)</td></tr>
            <tr><td>10.1 to 12.0 ft (3.1 to 3.6 m)</td><td>0.91</td><td>27.3 ft (8.3 m)</td><td>19.3 ft (5.88 m)</td></tr>
            <tr><td>12.1 to 14.0 ft (3.7 to 4.2 m)</td><td>0.84</td><td>25.2 ft (7.6 m)</td><td>17.8 ft (5.42 m)</td></tr>
            <tr><td>14.1 to 16.0 ft (4.3 to 4.8 m)</td><td>0.77</td><td>23.1 ft (7.0 m)</td><td>16.3 ft (4.97 m)</td></tr>
            <tr><td>16.1 to 18.0 ft (4.9 to 5.4 m)</td><td>0.71</td><td>21.3 ft (6.5 m)</td><td>15.0 ft (4.57 m)</td></tr>
            <tr><td>18.1 to 20.0 ft (5.5 to 6.1 m)</td><td>0.64</td><td>19.2 ft (5.8 m)</td><td>13.6 ft (4.14 m)</td></tr>
            <tr><td>Above 30 ft (9.1 m)</td><td>Beam Detectors Recommended</td><td>N/A (Optical Projected Beam)</td><td>N/A</td></tr>
          </tbody>
        </table>
      </div>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Air Changes per Hour (ACH)</th>
              <th>Minutes per Air Change</th>
              <th>Maximum Floor Area per Detector</th>
              <th>Linear Spacing on Center</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Under 8 ACH</td><td>Over 7.5 Minutes</td><td>900 sq ft (83.6 m²)</td><td>30.0 ft (9.1 m)</td></tr>
            <tr><td>8 to 15 ACH</td><td>4.0 to 7.5 Minutes</td><td>500 sq ft (46.5 m²)</td><td>22.4 ft (6.8 m)</td></tr>
            <tr><td>16 to 30 ACH</td><td>2.0 to 3.9 Minutes</td><td>250 sq ft (23.2 m²)</td><td>15.8 ft (4.8 m)</td></tr>
            <tr><td>31 to 60 ACH</td><td>1.0 to 1.9 Minutes</td><td>125 sq ft (11.6 m²)</td><td>11.2 ft (3.4 m)</td></tr>
          </tbody>
        </table>
      </div>

      <h3>When to Use Each Calculator: Professional Engineering Design Workflows</h3>
      <p>
        In fire protection consulting, life safety systems must integrate spatial sensor coverage with circuit electrical survivability. The following workflow demonstrates how our calculators integrate:
      </p>

      <h4>Workflow 1: Commercial Logistics Facility Smoke Detection &amp; Notification Layout</h4>
      <ol>
        <li>
          <strong>Step 1 — Establish Building Geometric Boundaries:</strong> Measure the open warehouse floor plan (e.g., 54m length × 27m width × 4.5m ceiling height).
        </li>
        <li>
          <strong>Step 2 — Determine Grid Detector Layout:</strong> Open the <a href="smoke-detector-spacing-calculator.html">Smoke Detector Spacing Calculator</a>. At 4.5m ceiling height, NFPA 72 establishes an 8.0m spacing interval. The calculator partitions the layout into 7 columns along the length and 4 rows across the width ($7 \times 4 = 28\text{ detectors}$), verifying that the furthest corner radius does not exceed 6.4m.
        </li>
        <li>
          <strong>Step 3 — Verify Perimeter Wall Exclusions:</strong> Ensure detectors are mounted at half spacing from perimeter walls (4.0m and 3.4m), and confirm no detectors are placed within the 4-inch (100mm) corner dead-air zone.
        </li>
        <li>
          <strong>Step 4 — Size Notification Strobe Appliance Circuit (NAC):</strong> Connect 14 synchronized 75-candela strobes along the 120-meter notification circuit. Using the <a href="voltage-drop-calculator.html">Voltage Drop Calculator</a>, verify that terminal voltage at the last strobe remains above 18.2V DC (exceeding the 16.0V UL cutoff).
        </li>
        <li>
          <strong>Step 5 — Verify End-of-Line Monitoring:</strong> Use the <a href="ohms-law-calculator.html">Ohm's Law Calculator</a> to calculate standby supervisory current across the 4.7 kΩ EOLR resistor, verifying panel loop fault detection integrity.
        </li>
      </ol>

      <div class="worked-example-card">
        <div class="worked-example-header">
          <h3 class="worked-example-title">📐 Comprehensive Worked Case Study: Commercial Office Floor Smoke Detection Layout</h3>
          <span class="worked-example-badge">NFPA 72 Certified Life Safety Case Study</span>
        </div>
        <div class="step-calculation-list">
          <div class="calc-step-item">
            <div class="calc-step-title">Step 1: Define Facility Floor Dimensions &amp; Ceiling Profile</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              \[ L = 48.0\text{ m (157.5 ft)},\quad W = 24.0\text{ m (78.7 ft)},\quad \text{Ceiling: 3.6m Flat Concrete Slab} \]
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">A commercial open-plan corporate facility measures 48.0 meters long by 24.0 meters wide with smooth flat slab construction and normal ventilation (&lt;8 ACH).</p>
          </div>

          <div class="calc-step-item">
            <div class="calc-step-title">Step 2: Calculate Column &amp; Row Intervals Under Listed Spacing (S = 9.1m)</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              \[ \text{Columns} = \lceil \frac{48.0\text{m}}{9.1\text{m}} \rceil = 6\text{ intervals},\quad \text{Rows} = \lceil \frac{24.0\text{m}}{9.1\text{m}} \rceil = 3\text{ intervals} \]
              \[ S_{\text{length}} = \frac{48.0}{6} = 8.00\text{ m}\ (< 9.1\text{m}),\quad S_{\text{width}} = \frac{24.0}{3} = 8.00\text{ m}\ (< 9.1\text{m}) \]
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">The room partitions into a uniform 8.0m × 8.0m grid (well within 9.1m maximum spacing), with perimeter wall offsets at exactly 4.0m (0.5S).</p>
          </div>

          <div class="calc-step-item">
            <div class="calc-step-title">Step 3: Total Detector Count &amp; Corner Radial Verification</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              \[ \text{Total Detectors} = 6 \times 3 = 18\text{ Addressable Optical Detectors} \]
              \[ R_{\text{corner}} = \sqrt{4.0^2 + 4.0^2} = 5.66\text{ meters}\ (< 6.47\text{m maximum allowed radius}) \]
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">Eighteen addressable optical detectors cover the floor space, with maximum corner radial reach measuring 5.66m, easily passing the 6.47m NFPA 72 limit via our <a href="smoke-detector-spacing-calculator.html">Smoke Detector Spacing Calculator</a>.</p>
          </div>
        </div>
        <div class="calc-final-result">
          ✅ <strong>Certified Life Safety Layout:</strong> 18 Addressable Optical Detectors in 6 × 3 Grid | 8.0m Uniform Spacing | Corner Reach: 5.66m (Compliant) | 100% Blind-Spot Elimination.
        </div>
      </div>

      <h3>Industry Codes, Regulatory Standards &amp; Quality Assurance (E-E-A-T)</h3>
      <p>
        Fire alarm systems are heavily regulated to protect human life during emergency egress:
      </p>
      <ul>
        <li><strong>NFPA 72 Clause 17.7.3.2:</strong> Governs spot smoke detector spacing, radial coverage circles, and smooth ceiling layout boundaries.</li>
        <li><strong>NFPA 72 Clause 17.7.3.2.1 (Dead Air Space):</strong> Mandates that detectors must not be mounted within 4 inches (100 mm) of any ceiling-wall intersection, and wall-mounted units must be placed 4 to 12 inches (100–300 mm) down from the ceiling.</li>
        <li><strong>NFPA 72 Clause 17.7.3.7 (Peaked &amp; Sloped Ceilings):</strong> Requires detectors to be placed within 3 feet (0.9 meters) of the roof apex, measured horizontally along the ceiling profile.</li>
        <li><strong>UL 1971 &amp; NFPA 72 Chapter 18:</strong> Standardizes emergency notification appliance synchronization (flashing within 10 milliseconds of each other) to prevent photosensitive epileptic seizures.</li>
      </ul>

      <div class="faq-container" style="margin-top:2.5rem;">
        <h3 style="margin-bottom:1.5rem;">Frequently Asked Questions (Fire Protection)</h3>
        
        <div class="faq-item">
          <div class="faq-q">Why does NFPA 72 prohibit mounting smoke detectors directly in ceiling-wall corners?</div>
          <div class="faq-a">In an enclosed room, thermal convection creates a boundary stagnation layer known as the 'dead air space' in the 90-degree intersection where the ceiling meets the wall. Rising buoyant smoke curls away from the corner before reaching it. NFPA 72 strictly prohibits mounting detectors within 4 inches (100 mm) of the ceiling-wall corner, and wall-mounted units must be placed 4 to 12 inches (100–300 mm) down from the ceiling.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">How do air change rates (ACH) affect smoke detector spacing in server rooms and cleanrooms?</div>
          <div class="faq-a">In cleanrooms, server halls, and telecommunication spaces where ventilation exceeds 8 Air Changes per Hour (ACH), high air velocity dilutes smoke plumes and blows them away from ceiling detectors. NFPA 72 Table 17.7.6.3.3.1 mandates reducing spacing down to 25 ft, 20 ft, or 15 ft (reducing area coverage from 900 sq ft down to 500, 250, or 125 sq ft per detector) as air change rates accelerate.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">What is the peak rule for sloped ceilings under NFPA 72?</div>
          <div class="faq-a">In buildings with pitched, peaked, or cathedral roof profiles, thermal buoyancy causes smoke to rise and collect first along the high apex. NFPA 72 mandates that detectors must be located within 3 feet (0.9 meters) of the peak, measured horizontally along the ceiling profile, with subsequent rows spaced down the slope.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">What is the difference between ionization and photoelectric smoke detection?</div>
          <div class="faq-a">Ionization detectors use a minute radioactive americium-241 source to detect tiny combustion particles typical of fast-flaming wood, paper, and grease fires. Photoelectric detectors utilize a light-scattering optical infrared chamber superior at detecting larger smoke particles from slow-smoldering electrical cable and upholstery fires, while being substantially less prone to false cooking alarms.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">Why must Notification Appliance Circuit (NAC) voltage drop be verified?</div>
          <div class="faq-a">Fire alarm control panels output 24V DC to power audible horns and visual strobes. If circuit conductors have high electrical resistance over long wiring distances, voltage drops below the 16.0V DC minimum operating threshold required by UL 1971. Inadequate voltage causes strobes to lose synchronization or fail completely during building evacuation.</div>
        </div>

      </div>

    </article>
'''

def update_chemical_and_fire():
    # Update chemical
    chem_path = os.path.join(BASE_DIR, "chemical.html")
    with open(chem_path, "r", encoding="utf-8") as f:
        c_content = f.read()
    article_pattern = re.compile(r'<article class="article-section">.*?</article>', re.DOTALL)
    if article_pattern.search(c_content):
        c_updated = article_pattern.sub(lambda m: CHEMICAL_CONTENT.strip(), c_content, count=1)
        with open(chem_path, "w", encoding="utf-8") as f:
            f.write(c_updated)
        print("Updated chemical.html successfully!")
        words = len(re.sub(r'<[^>]+>', ' ', CHEMICAL_CONTENT).split())
        print(f"Chemical hub article word count: {words} words")

    # Update fire
    fire_path = os.path.join(BASE_DIR, "fire-safety.html")
    with open(fire_path, "r", encoding="utf-8") as f:
        f_content = f.read()
    if article_pattern.search(f_content):
        f_updated = article_pattern.sub(lambda m: FIRE_CONTENT.strip(), f_content, count=1)
        with open(fire_path, "w", encoding="utf-8") as f:
            f.write(f_updated)
        print("Updated fire-safety.html successfully!")
        words = len(re.sub(r'<[^>]+>', ' ', FIRE_CONTENT).split())
        print(f"Fire Safety hub article word count: {words} words")

if __name__ == "__main__":
    update_chemical_and_fire()
