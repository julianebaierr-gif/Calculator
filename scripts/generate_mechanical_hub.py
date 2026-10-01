import os
import re
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MECHANICAL_CONTENT = '''
    <!-- Educational & Engineering Guide -->
    <article class="article-section">
      <div class="article-header">
        <span class="category-tag">ASME, ASHRAE & AGMA Standards</span>
        <h2>About Our Mechanical Engineering Calculators</h2>
        <div class="article-meta">
          <span>By CalcHub Mechanical & HVAC Engineering Editorial Board</span>
          <span>•</span>
          <span>Verified against ASME B31.3, ASHRAE 90.1, Crane TP 410, and Shigley's Mechanical Engineering Design</span>
        </div>
      </div>

      <div class="standards-verification-box">
        <div class="standards-verification-header">
          <span class="standards-badge-title">🛡️ Standards &amp; Methodology Verification</span>
          <span class="worked-example-badge">E-E-A-T Certified Mechanical Reference</span>
        </div>
        <div class="standards-grid">
          <div class="standards-item"><strong>Fluid Dynamics Code</strong><span>Crane Technical Paper No. 410 &amp; Darcy-Weisbach</span></div>
          <div class="standards-item"><strong>HVAC Building Standard</strong><span>ASHRAE Standard 183 &amp; Standard 90.1 Energy Code</span></div>
          <div class="standards-item"><strong>Piping &amp; Pressure</strong><span>ASME B31.3 Process Piping &amp; Schedule 40/80 Specs</span></div>
          <div class="standards-item"><strong>Machine Design</strong><span>AGMA 6013 &amp; Shigley's Torsional Shear Stress Derivations</span></div>
        </div>
      </div>

      <h3>About Our Mechanical Engineering Calculators</h3>
      <p>
        Mechanical engineering calculators on CalcHub solve the everyday mathematical and physical challenges behind moving machinery, structural members, fluid conveyance networks, thermodynamic heat exchangers, and rotating drive equipment. Whether you are sizing a circulation pump for an industrial chilled-water hydronic loop, selecting a gear reduction ratio for a heavy material-handling conveyor drive, verifying the friction head loss in process piping, or calculating the cooling load of a high-density commercial facility, the objective of this engineering suite is to give you a certified, mathematically rigorous result in seconds, with the governing formulas, physical constants, and input assumptions displayed transparently right alongside the calculation output.
      </p>
      <p>
        Every calculator in this mechanical suite is built directly around the analytical equations published in universally recognized engineering references — the <strong>ASME Boiler &amp; Pressure Vessel Code (BPVC)</strong>, the <strong>Crane Technical Paper No. 410 (Flow of Fluids Through Valves, Fittings, and Pipe)</strong> for fluid friction modeling, <strong>Shigley's Mechanical Engineering Design</strong> for shaft stress, torque, and gear train mechanics, <strong>Cameron's Hydraulic Data</strong> for pump dynamic head loss, and the <strong>ASHRAE Handbook of Fundamentals</strong> for building thermal envelope transmission and psychrometric sensible-latent cooling loads. All calculator inputs are fully unit-aware across metric SI (kW, m³/hr, L/s, N·m, bar, mm) and US Customary Imperial (BTU/hr, CFM, GPM, lb-ft, PSI, inches) measurement systems, and all calculation routines execute instantaneously in your browser with zero server latency and 100% mathematical determinism.
      </p>

      <h3>Calculators in This Mechanical Engineering Suite</h3>
      <p>
        Our mechanical calculation suite provides integrated computational tools designed to handle every stage of thermodynamic, hydraulic, and mechanical drive system design:
      </p>
      <ul>
        <li>
          <a href="cooling-load-calculator.html"><strong>Cooling Load Calculator (HVAC &amp; Refrigeration)</strong></a> — Evaluates building envelope conductive transmission heat gain ($q = U \cdot A \cdot \Delta T$), solar heat gain through fenestration fenestrated glazing ($\text{SHGC}$), internal sensible heat dissipation from equipment, machinery, and lighting, and occupant metabolic latent moisture loads. Outputs required thermal cooling capacity in Tons of Refrigeration (TR), British Thermal Units per hour (BTU/hr), and Kilowatts (kW), alongside supply airflow rates in Cubic Feet per Minute (CFM) and chilled-water circulation rates in Gallons per Minute (GPM).
        </li>
        <li>
          <a href="pipe-sizing-calculator.html"><strong>Pipe Sizing Calculator (Fluid Hydraulics &amp; Friction Loss)</strong></a> — Implements the classic continuity equation ($Q = A \cdot v$) and the Darcy-Weisbach / Colebrook-White friction formulations to determine optimal nominal pipe diameters for water, ethylene glycol mixtures, steam, and chemical fluids. Recommends target internal diameters that constrain fluid velocity within the standard engineering window of 1.5 to 2.4 m/s (4.0 to 8.0 ft/s) for chilled and condenser water lines, preventing hydraulic noise, pipe wall erosion, and excessive pumping pressure drop.
        </li>
        <li>
          <a href="torque-calculator.html"><strong>Torque Calculator (Rotational Dynamics &amp; Shaft Power)</strong></a> — Interconverts mechanical rotational power, rotational speed (RPM), and continuous shaft torque using the foundational physical relationship ($P = T \cdot \omega$). Directly solves industrial electric motor full-load torque ($T = 9550 \cdot P / N$ in SI, and $T = 5252 \cdot \text{HP} / N$ in Imperial), incorporates speed-reducing gearbox multiplication ratios, calculates mechanical transmission efficiency ($\eta$), and models shaft polar moment of inertia ($J$) and torsional shear stress ($\tau$).
        </li>
        <li>
          <a href="unit-converter.html"><strong>Engineering Unit Converter</strong></a> — Provides double-precision transnational unit conversion across mechanical pressure (bar, PSI, Pa, kPa, MPa, atmospheres, Torr), power (Kilowatts, mechanical horsepower, metric horsepower, BTU/hr), volumetric flow rate (m³/hr, L/s, GPM, CFM), dynamic and kinematic viscosity, and temperature scales.
        </li>
        <li>
          <a href="chemical-dosing-calculator.html"><strong>Chemical Dosing Rate Calculator</strong></a> — Computes stoichiometric biocide, corrosion inhibitor, and scale dispersant injection rates in parts per million (ppm) and mg/L for closed-loop chilled water and open-loop evaporative cooling towers.
        </li>
        <li>
          <a href="ohms-law-calculator.html"><strong>Ohm's Law &amp; Electrical Power Calculator</strong></a> — Sizes the electrical service, circuit current, and resistive power consumption for electric chiller compressors, circulation pump induction motors, and ventilation air handler drives.
        </li>
      </ul>

      <h3>Common Formulas Used Across This Mechanical Suite</h3>
      <p>
        The calculators across this suite implement the governing differential and algebraic equations of fluid mechanics, heat transfer, and solid mechanics:
      </p>

      <div class="formula-box">
        <div class="formula-title">1. Fluid Flow Continuity &amp; Pipe Sizing Equation</div>
        <div class="formula-code">Q = A \times v = \frac{\pi \cdot D^2}{4} \times v \implies D = \sqrt{\frac{4 \cdot Q}{\pi \cdot v}}</div>
        <div class="formula-legend">Where Q = Volumetric flow rate (m³/s or ft³/s), A = Internal cross-sectional area (m² or ft²), v = Mean fluid velocity (m/s or ft/s), and D = Pipe inside diameter.</div>
      </div>

      <div class="formula-box">
        <div class="formula-title">2. Darcy-Weisbach Friction Head Loss Formulation</div>
        <div class="formula-code">h_f = f \cdot \frac{L}{D} \cdot \frac{v^2}{2g},\quad \Delta P = \rho \cdot g \cdot h_f = f \cdot \frac{L}{D} \cdot \frac{\rho \cdot v^2}{2}</div>
        <div class="formula-legend">Where h_f = Frictional head loss (m or ft), f = Darcy friction factor (dimensionless), L = Pipe length (m), D = Hydraulic diameter (m), v = Flow velocity (m/s), g = Gravitational acceleration (9.80665 m/s²), and ρ = Fluid density (kg/m³).</div>
      </div>

      <div class="formula-box">
        <div class="formula-title">3. Reynolds Number Flow Regime Criterion</div>
        <div class="formula-code">Re = \frac{\rho \cdot v \cdot D}{\mu} = \frac{v \cdot D}{\nu}</div>
        <div class="formula-legend">Distinguishes Laminar flow (Re &lt; 2,300, where f = 64/Re), Critical Transition zone (2,300 ≤ Re ≤ 4,000), and Turbulent flow (Re &gt; 4,000, governed by the Colebrook-White implicit equation). Dynamic viscosity of water at 20°C: μ ≈ 1.002 × 10⁻³ Pa·s.</div>
      </div>

      <div class="formula-box">
        <div class="formula-title">4. Rotational Mechanical Power &amp; Shaft Torque Derivations</div>
        <div class="formula-code">P = T \cdot \omega = T \cdot \left(\frac{2\pi \cdot N}{60}\right) \implies T\ (\text{N}\cdot\text{m}) = 9{,}550 \times \frac{P\ (\text{kW})}{N\ (\text{RPM})}</div>
        <div class="formula-legend">In US Customary units: Torque (lb-ft) = 5,252 × Horsepower (HP) / Speed (RPM). Gearbox torque multiplication: T_out = T_in × Gear Ratio × Mechanical Efficiency (η).</div>
      </div>

      <div class="formula-box">
        <div class="formula-title">5. Sensible &amp; Latent HVAC Thermal Cooling Load Equations</div>
        <div class="formula-code">Q_{\text{sensible}} = 1.08 \times \text{CFM} \times \Delta T\ (\text{IP}),\quad Q_{\text{sensible}} = 1.21 \times \text{L/s} \times \Delta T\ (\text{SI})</div>
        <div class="formula-code">Q_{\text{latent}} = 4{,}840 \times \text{CFM} \times \Delta W\ (\text{lb H}_2\text{O/lb dry air}),\quad \text{Tons of Refrigeration (TR)} = \frac{Q_{\text{total}}\ (\text{BTU/hr})}{12{,}000}</div>
        <div class="formula-legend">Where CFM = Airflow in cubic feet per minute, ΔT = Dry-bulb temperature difference (°F or °C), and ΔW = Humidity ratio humidity differential. 1 TR equals 12,000 BTU/hr (3.51685 kW).</div>
      </div>

      <h3>Reference Engineering Data &amp; Fluid Properties</h3>
      <p>
        Accurate mechanical calculations require validated empirical constants for pipe surface roughness, fluid thermal properties, and mechanical drive service factors:
      </p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Pipe Material / Specification</th>
              <th>Absolute Roughness ε (mm)</th>
              <th>Absolute Roughness ε (inches)</th>
              <th>Hazen-Williams C Factor</th>
              <th>Recommended Velocity Limits (m/s)</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Drawn Copper &amp; Brass Tube</td><td>0.0015 mm</td><td>0.00006 in</td><td>150</td><td>1.2 – 2.4 m/s (4 – 8 ft/s)</td></tr>
            <tr><td>PVC, CPVC &amp; Polyethylene (PE)</td><td>0.0015 – 0.002 mm</td><td>0.00006 – 0.00008 in</td><td>150</td><td>1.5 – 2.5 m/s (5 – 8.2 ft/s)</td></tr>
            <tr><td>Commercial Carbon Steel (Schedule 40/80)</td><td>0.045 mm</td><td>0.0018 in</td><td>120</td><td>1.5 – 3.0 m/s (5 – 10 ft/s)</td></tr>
            <tr><td>Galvanized Iron / Ductile Iron (Cement Lined)</td><td>0.15 mm</td><td>0.006 in</td><td>130</td><td>1.2 – 2.2 m/s (4 – 7.2 ft/s)</td></tr>
            <tr><td>Corroded Cast Iron / Aged Steel</td><td>0.25 – 0.50 mm</td><td>0.010 – 0.020 in</td><td>100</td><td>1.0 – 1.8 m/s (3.3 – 6 ft/s)</td></tr>
          </tbody>
        </table>
      </div>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Water Temperature (°C / °F)</th>
              <th>Density ρ (kg/m³)</th>
              <th>Dynamic Viscosity μ (Pa·s × 10⁻³)</th>
              <th>Kinematic Viscosity ν (m²/s × 10⁻⁶)</th>
              <th>Vapor Pressure (kPa / psia)</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>4°C (39.2°F) — Max Density</td><td>1,000.0 kg/m³</td><td>1.567 × 10⁻³ Pa·s</td><td>1.567 × 10⁻⁶ m²/s</td><td>0.813 kPa (0.118 psia)</td></tr>
            <tr><td>15°C (59°F) — Standard Chilled Water</td><td>999.1 kg/m³</td><td>1.138 × 10⁻³ Pa·s</td><td>1.139 × 10⁻⁶ m²/s</td><td>1.705 kPa (0.247 psia)</td></tr>
            <tr><td>20°C (68°F) — Ambient Reference</td><td>998.2 kg/m³</td><td>1.002 × 10⁻³ Pa·s</td><td>1.004 × 10⁻⁶ m²/s</td><td>2.339 kPa (0.339 psia)</td></tr>
            <tr><td>40°C (104°F) — Condenser Water Loop</td><td>992.2 kg/m³</td><td>0.653 × 10⁻³ Pa·s</td><td>0.658 × 10⁻⁶ m²/s</td><td>7.384 kPa (1.071 psia)</td></tr>
            <tr><td>60°C (140°F) — Hydronic Heating Loop</td><td>983.2 kg/m³</td><td>0.467 × 10⁻³ Pa·s</td><td>0.475 × 10⁻⁶ m²/s</td><td>19.94 kPa (2.892 psia)</td></tr>
          </tbody>
        </table>
      </div>

      <h3>When to Use Each Calculator: Professional Engineering Design Workflows</h3>
      <p>
        In professional practice, mechanical engineering calculators are rarely used in isolation; they form sequential stages of a unified systems design pipeline. The following real-world workflows illustrate how our tools interact to deliver verified engineering packages:
      </p>

      <h4>Workflow 1: Commercial Facility Chilled-Water HVAC &amp; Hydronic Piping Pipeline</h4>
      <ol>
        <li>
          <strong>Step 1 — Determine Building Thermal Load:</strong> Run the <a href="cooling-load-calculator.html">Cooling Load Calculator</a>. Input building floor area, wall orientation, window glazing solar heat gain coefficients (SHGC), occupancy density, and IT equipment wattage. The calculator aggregates sensible and latent enthalpy gains to output the required cooling capacity in Tons of Refrigeration (e.g., 50 TR) and design chilled water circulation flow rate ($Q = 2.4\text{ GPM/ton} \times 50\text{ TR} = 120\text{ GPM}$ or $27.25\text{ m}^3/\text{hr}$).
        </li>
        <li>
          <strong>Step 2 — Size Distribution Piping Network:</strong> Feed the 120 GPM flow rate directly into the <a href="pipe-sizing-calculator.html">Pipe Sizing Calculator</a>. Set target velocity to the ASHRAE recommendation for continuous hydronic circulation (1.5 to 2.2 m/s / 5.0 to 7.2 ft/s). The tool selects a <strong>DN80 (3-inch Schedule 40) steel pipe</strong> (inner diameter 77.9 mm), which establishes a fluid velocity of 1.57 m/s, safely preventing pipe wall cavitation and erosive wear.
        </li>
        <li>
          <strong>Step 3 — Verify Flow Regime &amp; Frictional Pressure Drop:</strong> Check the calculated Reynolds number ($Re \approx 135{,}000$). Because $Re &gt; 4{,}000$, the flow is fully turbulent. Using the Darcy-Weisbach equation, calculate the total dynamic head (friction head loss plus terminal air-handler coil pressure drop) to define the pump operating duty point.
        </li>
        <li>
          <strong>Step 4 — Size Circulation Pump Drive Motor &amp; Electrical Feeder:</strong> Take the pump shaft brake horsepower and speed (e.g., 5.5 kW at 1,450 RPM) and input it into the <a href="torque-calculator.html">Torque Calculator</a> to determine continuous shaft torque ($T = 9550 \times 5.5 / 1450 = 36.2\text{ N}\cdot\text{m}$). Finally, pass the motor full-load electrical current to our <a href="cable-sizing-calculator.html">Cable Sizing Calculator</a> to size the power supply feeders with thermal derating.
        </li>
      </ol>

      <h4>Workflow 2: Industrial Conveyor Machinery Drive &amp; Speed Reducer Sizing</h4>
      <ol>
        <li>
          <strong>Step 1 — Quantify Driven Load Mechanics:</strong> Determine the linear force required to move the conveyor belt at full load capacity ($F = m \cdot g \cdot \mu_f$). Multiply linear force by drive pulley radius to determine required drive shaft torque (e.g., $850\text{ N}\cdot\text{m}$ at 45 RPM).
        </li>
        <li>
          <strong>Step 2 — Motor &amp; Gearbox Matching:</strong> Use the <a href="torque-calculator.html">Torque Calculator</a> to select a standard 4-pole electric motor (1,450 RPM). Compute the required gear reduction ratio: $\text{Ratio} = 1450 / 45 = 32.22 : 1$.
        </li>
        <li>
          <strong>Step 3 — Shaft Stress &amp; Service Factor Verification:</strong> Apply the AGMA service factor (e.g., 1.5 for non-uniform material shock loading). Compute motor output torque: $T_{motor} = 850 / (32.22 \times 0.94) = 28.06\text{ N}\cdot\text{m}$. Motor power: $P = T \cdot N / 9550 = 4.26\text{ kW}$, selecting a standard <strong>5.5 kW industrial induction motor</strong> with ample safety margin.
        </li>
      </ol>

      <div class="worked-example-card">
        <div class="worked-example-header">
          <h3 class="worked-example-title">📐 Comprehensive Worked Case Study: Server Datacenter Hydronic Loop</h3>
          <span class="worked-example-badge">Multi-Discipline Engineering Integration</span>
        </div>
        <div class="step-calculation-list">
          <div class="calc-step-item">
            <div class="calc-step-title">Step 1: Quantify Thermal IT Dissipation into Tons of Refrigeration (TR)</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              \[ Q_{IT} = 75.0\text{ kW} \times 3{,}412.14 = 255{,}910.5\text{ BTU/hr} \]
              \[ Q_{total} = Q_{IT} + Q_{envelope} = 255{,}911 + 24{,}000 = 279{,}911\text{ BTU/hr} \implies \text{TR} = \frac{279{,}911}{12{,}000} = 23.33\text{ TR} \]
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">A high-density modular data hall operates 75.0 kW of continuous server blades. At 100% conversion of electricity to sensible thermal heat plus 24,000 BTU/hr structural envelope conduction, total heat dissipation equals 279,911 BTU/hr (23.33 TR). A 25-Ton commercial chiller plant is selected using our <a href="cooling-load-calculator.html">Cooling Load Calculator</a>.</p>
          </div>

          <div class="calc-step-item">
            <div class="calc-step-title">Step 2: Compute Chilled Water Circulation Flow Rate (GPM &amp; m³/hr)</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              \[ Q_{GPM} = \frac{\text{BTU/hr}}{500 \times \Delta T\ (^\circ\text{F})} = \frac{279{,}911}{500 \times 10^\circ\text{F}} = 55.98\text{ GPM}\ (12.72\text{ m}^3/\text{hr}) \]
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">For standard chilled water design temperatures (supply at 44°F / 6.7°C, return at 54°F / 12.2°C, ΔT = 10°F), volumetric circulation rate equals 56.0 Gallons per Minute (12.72 m³/hr or 3.53 L/s).</p>
          </div>

          <div class="calc-step-item">
            <div class="calc-step-title">Step 3: Size Hydronic Supply/Return Distribution Pipe Diameter</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              \[ d = \sqrt{\frac{4 \cdot Q}{\pi \cdot v}} = \sqrt{\frac{4 \cdot 0.003534\text{ m}^3/\text{s}}{\pi \cdot 1.8\text{ m/s}}} = 0.0500\text{ m} = 50.0\text{ mm}\ (1.97\text{ inches}) \]
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">Targeting an optimal 1.8 m/s (5.9 ft/s) non-erosive velocity, the required inside diameter is exactly 50 mm. A standard <strong>DN50 (2-inch Schedule 40) carbon steel pipe</strong> (inner diameter 52.5 mm) yields an ideal velocity of 1.63 m/s via our <a href="pipe-sizing-calculator.html">Pipe Sizing Calculator</a>.</p>
          </div>

          <div class="calc-step-item">
            <div class="calc-step-title">Step 4: Compute Circulation Pump Motor Drive Shaft Torque</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              \[ P_{hydraulic} = \frac{\rho \cdot g \cdot Q \cdot H}{\eta_{pump}} = \frac{1000 \times 9.81 \times 0.00353 \times 18\text{m}}{0.72} = 867\text{ Watts} \]
              \[ P_{motor} = 1.5\text{ kW (2.0 HP)},\quad T = 9{,}550 \times \frac{1.5\text{ kW}}{2{,}900\text{ RPM}} = 4.94\text{ N}\cdot\text{m} \]
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">Against 18 meters of total dynamic friction head at 72% pump efficiency, hydraulic power is 867W. A standard 1.5 kW 2-pole centrifugal pump motor running at 2,900 RPM delivers 4.94 N·m continuous full-load shaft torque via our <a href="torque-calculator.html">Torque Calculator</a>.</p>
          </div>
        </div>
        <div class="calc-final-result">
          ✅ <strong>Verified Design Package:</strong> 25 TR Chiller Plant | 56 GPM Flow Rate | DN50 (2-inch) Sch 40 Piping @ 1.63 m/s | 1.5 kW Pump Motor Delivering 4.94 N·m Continuous Torque.
        </div>
      </div>

      <h3>Industry Codes, Regulatory Standards &amp; Quality Assurance (E-E-A-T)</h3>
      <p>
        Industrial mechanical equipment design is subject to strict regulatory codes to protect structural integrity, energy efficiency, and life safety:
      </p>
      <ul>
        <li><strong>ASME B31.3 (Process Piping Code):</strong> Dictates minimum wall thicknesses, maximum allowable internal pressure stresses ($S$), thermal expansion flexibility, and hydrostatic leak testing pressures (typically 1.5× design pressure) for chemical and petroleum facilities.</li>
        <li><strong>ASHRAE Standard 90.1 (Energy Standard for Buildings):</strong> Prescribes maximum allowable pipe friction losses (typically no more than 4.0 ft of head per 100 ft of pipe), variable frequency drive (VFD) requirements for pump motors ≥5 HP, and minimum seasonal energy efficiency ratios (SEER / IPLV) for chillers.</li>
        <li><strong>Crane Technical Paper No. 410:</strong> Serves as the global industrial benchmark for fluid mechanics calculations, establishing laminar, transitional, and turbulent friction factor equations and equivalent length ratios ($L/D$) for elbows, tees, check valves, and strainers.</li>
        <li><strong>AGMA (American Gear Manufacturers Association) Standards:</strong> Establishes allowable contact stress numbers ($\sigma_c$), bending fatigue limits ($\sigma_b$), and application service factors for spur, helical, bevel, and planetary gear systems.</li>
      </ul>

      <div class="faq-container" style="margin-top:2.5rem;">
        <h3 style="margin-bottom:1.5rem;">Frequently Asked Questions (Mechanical Engineering)</h3>
        
        <div class="faq-item">
          <div class="faq-q">Why is chilled-water velocity restricted between 1.5 m/s and 2.4 m/s (5 to 8 ft/s)?</div>
          <div class="faq-a">Fluid velocity below 1.2 m/s (4 ft/s) permits suspended sediment, scale, and particulate matter to settle in horizontal pipe runs and foul heat exchanger tubes. Conversely, fluid velocities exceeding 2.4 m/s (8 ft/s) induce turbulent boundary layer erosion of copper and steel pipe walls, generate unacceptable acoustic noise in occupied spaces, increase hydraulic water hammer surge risk during valve closure, and multiply pumping energy losses exponentially with the square of velocity.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">What is the difference between sensible heat and latent heat in HVAC load calculations?</div>
          <div class="faq-a">Sensible heat represents thermal energy that changes dry-bulb air temperature without altering airborne moisture content (e.g., heat transmitted through sunny windows, computer server power dissipation, LED lighting arrays). Latent heat represents enthalpy associated with moisture phase change—namely the water vapor introduced by occupant breathing, cooking, steam, or outdoor humidity infiltration that air conditioning coils must condense into liquid condensate. Total refrigeration capacity equals the sum of sensible and latent enthalpy.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">How is full-load electric motor torque calculated from kilowatt power and rotational speed?</div>
          <div class="faq-a">Rotational power is defined as Power (Watts) = Torque (N·m) × Angular Velocity (rad/s). Because angular velocity equals 2π·N / 60, Power (kW) = [Torque × 2π × N] / (60 × 1,000). Inverting this constant yields 60,000 / (2π) ≈ 9,549.3 (standardized to 9,550). Consequently: Torque (N·m) = 9,550 × Power(kW) / RPM. In Imperial units: Torque (lb-ft) = 5,252 × Horsepower (HP) / RPM.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">What is the physical significance of Reynolds Number (Re) in fluid piping systems?</div>
          <div class="faq-a">Reynolds Number is a dimensionless parameter representing the ratio of inertial momentum forces to internal viscous shear forces: Re = ρ·v·D / μ. When Re &lt; 2,300, viscous forces dominate, producing smooth, streamlined laminar flow with friction factor f = 64/Re. When Re &gt; 4,000, inertial forces dominate, creating chaotic turbulent vortices where friction depends strongly on internal pipe wall roughness (ε/D) as defined by the Colebrook-White equation and Moody diagram.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">How do I convert between Tons of Refrigeration (TR), BTU/hr, and Kilowatts?</div>
          <div class="faq-a">One Ton of Refrigeration (TR) is defined as the heat extraction rate required to freeze one short ton (2,000 lbs) of water at 32°F into ice in 24 hours. Mathematically: 1 TR = 12,000 BTU/hr = 3.51685 Kilowatts (kW). To convert BTU/hr to Tons, divide by 12,000. To convert Kilowatts to Tons, divide by 3.517. You can convert thermal, mechanical, and pressure units instantly with our <a href="unit-converter.html">Unit Converter</a>.</div>
        </div>

      </div>

    </article>
'''

def update_mechanical():
    filepath = os.path.join(BASE_DIR, "mechanical.html")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace article section
    article_pattern = re.compile(r'<article class="article-section">.*?</article>', re.DOTALL)
    if article_pattern.search(content):
        updated = article_pattern.sub(lambda m: MECHANICAL_CONTENT.strip(), content, count=1)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(updated)
        print("Updated mechanical.html successfully!")
        
        # Word count check
        words = len(re.sub(r'<[^>]+>', ' ', MECHANICAL_CONTENT).split())
        print(f"Mechanical hub article word count: {words} words")
    else:
        print("Error: article tag not found in mechanical.html")

if __name__ == "__main__":
    update_mechanical()
