"""
Expands the technical content in batch 3 tools so that their <article> word count exceeds 1,050+ words each.
"""

import os
import bs4

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 1. BOLT TORQUE EXPANSION
BOLT_EXTRA = """
        <h2>VDI 2230 Bolted Joint Elastic Compliance &amp; Embedding Settling Losses</h2>
        <p>In high-stress mechanical engineering joints, tightening torque does not translate directly into permanent, immutable clamping force. As analyzed in the rigorous German standard <strong>VDI 2230 Part 1 (Systematic Calculation of High Duty Bolted Joints)</strong>, all bolted connections behave as a pair of opposing springs: the bolt is stretched in tension like a slender spring, while the clamped joint members (flanges, housings, engine blocks) are compressed like stiff compressive springs. The ratio of fastener elastic resilience to clamped part resilience dictates how external operating loads (tensile separation forces or bending moments) distribute between the fastener and the joint.</p>

        <p>Furthermore, newly assembled bolted assemblies undergo an immediate phenomenon known as <strong>embedding relaxation (settling)</strong>. Microscopic surface asperities (peaks and valleys) on rough machined flanges, under washer faces, and across thread flanks plasticize and flatten under extreme clamping contact pressure. This settling loss ($\Delta f_z$, typically 2 to 5 micrometers per contact interface) shortens the effective elongation of the bolt. In short grip lengths (where the ratio of clamped thickness to bolt diameter $l_k / d &lt; 3$), even 3 micrometers of settling can dissipate up to 20% to 30% of the initial preload tension! To mitigate embedding losses, engineers specify hardened through-hardened washers (ASTM F436 / ISO 7089), maximize joint grip length, and apply a 10% to 15% tightening allowance during initial torque calibration.</p>

        <h2>Torque Wrench Calibration Standards &amp; Tightening Methods</h2>
        <p>Under international standard <strong>ISO 6789 (Assembly tools for screws and nuts — Hand torque tools)</strong>, manual click-type and digital indicating torque wrenches must maintain calibration within &plusmn;4% of indicated reading. However, because thread friction coefficients scatter unpredictably between fasteners (&plusmn;20% friction tolerance), controlling clamp force through torque alone is inherently imprecise (scatter band $\alpha_A \approx 1.4$ to $1.6$). In safety-critical aerospace and automotive engine assemblies, engineers utilize superior preload control methods:</p>
        <ul>
          <li><strong>Torque-Angle Method (Turn-of-Nut):</strong> The fastener is snugged to an initial threshold torque (typically 30% to 50% of final load) to eliminate joint gap slack, followed by rotating the wrench socket through a precise angular rotation (e.g., 90&deg; or 120&deg;). Because pitch distance traveled equals $P \times (\theta / 360^\circ)$, axial elongation and clamp force become virtually independent of thread friction.</li>
          <li><strong>Direct Tension Indicators (DTIs):</strong> Specialized hardened washers featuring raised compressible metal bumps are placed beneath the bolt head. As the fastener tightens, the bumps compress. A feeler gauge measures gap closure, directly proving that target axial preload tension has been achieved regardless of wrench torque readings.</li>
          <li><strong>Ultrasonic Bolt Elongation Measurement:</strong> An ultrasonic transducer is placed on the bolt head, transmitting acoustic sound waves down the fastener shank to the threaded tip. By measuring the time-of-flight acoustic transit time before and after tightening, technicians measure physical bolt stretch down to the nearest micron, yielding preload accuracy within &plusmn;2% to &plusmn;5%.</li>
        </ul>
"""

# 2. BEARING LIFE EXPANSION
BEARING_EXTRA = """
        <h2>ISO 281 Modified Reference Rating Life ($L_{10m}$) &amp; Lubrication Viscosity Ratio ($\kappa$)</h2>
        <p>While the basic $L_{10}$ calculation provides an essential baseline comparison between bearings, modern tribology recognizes that clean, properly lubricated bearings operating below their fatigue limit can run virtually indefinitely without developing subsurface rolling contact fatigue. In recognition of modern clean steel metallurgy and elastohydrodynamic lubrication (EHL) theory, <strong>ISO 281 Annex A</strong> introduced the <strong>modified rating life equation</strong>:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #2563EB;">
          $$L_{10m} = a_1 \cdot a_{\text{ISO}} \cdot L_{10}$$
        </div>
        <p>Where $a_{\text{ISO}}$ is the comprehensive life modification factor incorporating the fatigue load limit ($C_u$), the contamination parameter ($e_C$), and the critical <strong>lubrication viscosity ratio ($\kappa$)</strong>. The viscosity ratio is defined as:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #059669;">
          $$\kappa = \frac{\nu}{\nu_1}$$
        </div>
        <p>Where $\nu$ is the actual kinematic operating viscosity of the lubricant at system operating temperature ($\text{mm}^2/\text{s}$ or cSt), and $\nu_1$ is the minimum required kinematic viscosity determined from bearing pitch diameter ($d_m = \frac{d + D}{2}$) and rotational speed ($n$). When $\kappa \ge 2.0$ to $4.0$, a complete full-fluid hydrodynamic oil film separates all asperities between rolling elements and raceways, multiplying actual fatigue life by up to 5 times! Conversely, if $\kappa &lt; 0.4$ (due to excessive operating temperature or inadequate oil viscosity), metal-to-metal boundary contact occurs, slashing life by over 80% and triggering adhesive micro-wear.</p>

        <h2>Variable Operating Loads &amp; Miner's Cumulative Damage Rule</h2>
        <p>In many real-world industrial powertrains—such as mining conveyors, overhead cranes, and automotive gearboxes—rotational speeds and applied forces fluctuate across distinct operating duty cycles. In these multi-stage duty profiles, bearing life cannot be evaluated using a single static load. Instead, mechanical designers apply <strong>Palmgren-Miner's Linear Cumulative Damage Rule</strong> to determine the mean equivalent dynamic load ($P_m$):</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #7C3AED;">
          $$P_m = \left( \sum_{i=1}^k \frac{n_i \cdot q_i \cdot P_i^p}{n_m} \right)^{1/p}$$
        </div>
        <p>Where $P_i$ is the equivalent load during operating stage $i$, $q_i$ is the time fraction of stage $i$ ($\sum q_i = 1.0$), $n_i$ is the rotational speed in RPM during stage $i$, and $n_m = \sum (q_i \cdot n_i)$ is the weighted mean rotational speed. Evaluating dynamic fatigue under Miner's rule prevents severe bearing under-sizing in cyclic industrial equipment.</p>
"""

# 3. FIRE ALARM BATTERY EXPANSION
FA_EXTRA = """
        <h2>Notification Appliance Circuit (NAC) End-of-Discharge Voltage Drop Analysis</h2>
        <p>A critical engineering consideration often overlooked in secondary battery calculations is the physical behavior of <strong>Notification Appliance Circuits (NACs)</strong> as battery terminal voltage decays during continuous operation. While a nominal 24V DC fire alarm battery bank floats on utility power at approximately 27.6V DC (2.30V per cell), severing AC mains power forces the system to discharge along the electrochemical SLA discharge curve. By the end of the mandatory 24-hour standby period, the open-circuit cell voltage drops toward 21.0V to 20.4V DC (1.75V per cell—the standard low-voltage cutoff threshold).</p>

        <p>When the panel initiates full emergency evacuation notification at this depleted state, the sudden instantaneous draw of 4 to 10 Amperes of alarm current causes an immediate internal ohmic $I \cdot R_{\text{int}}$ voltage drop across aged battery lead plates, accompanied by substantial $I \cdot R_{\text{wire}}$ conductor voltage drop across long wire loops. Per <strong>UL 864 (Standard for Control Units and Accessories for Fire Alarm Systems)</strong>, all listed notification appliances (horns, strobes, speakers) are rated for regulated 24V DC operation with an allowable operating window of 16.0V to 33.0V DC. If an undersized battery drops below 19V DC at the panel terminals during alarm, downstream strobes at the end of a 500-foot loop may receive less than 16.0V DC, causing visible strobe flash failure, asynchronous pulsing, or audible horn distortion in direct violation of life safety standards.</p>

        <h2>Constant Current vs Constant Power Battery Ratings</h2>
        <p>Standard manufacturer battery datasheets provide two distinct capacity discharge tables: <strong>Constant Current (Amperes)</strong> and <strong>Constant Power (Watts per Cell)</strong>. Standard fire alarm initiating circuits and conventional horn/strobe loads exhibit resistive and semi-constant-current characteristics, making Ampere-hour (Ah) summations accurate. However, modern high-efficiency switching Emergency Voice/Alarm Communication Systems (EVACS) incorporate Class-D digital audio amplifiers. These switching power supplies behave as <em>constant power loads</em>: as battery DC bus voltage declines, the amplifier input switching regulators draw progressively <em>higher current</em> to maintain audio output wattage ($I = P / V$). For high-rise voice evacuation systems, engineers must consult manufacturer Constant Power discharge tables down to 1.75 VPC cutoff to confirm battery bank capability.</p>
"""

# 4. HYDRANT FIRE FLOW EXPANSION
HYDRANT_EXTRA = """
        <h2>Hazen-Williams Hydraulic Friction &amp; Water Distribution C-Factors</h2>
        <p>The mathematical foundation of the NFPA 291 fire flow rating equation ($Q_R \propto \Delta P^{0.54}$) is directly rooted in the classical <strong>Hazen-Williams hydraulic formula</strong> for pressurized water flow in closed municipal pipelines. In fluid dynamics, friction head loss ($h_f$) in a municipal distribution water main is modeled as:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #2563EB;">
          $$h_f = \frac{10.67 \cdot L \cdot Q^{1.852}}{C^{1.852} \cdot D^{4.87}}$$
        </div>
        <p>Where $L$ is pipeline length in feet, $D$ is pipe inside diameter in feet, $Q$ is volumetric flow rate in cubic feet per second, and $C$ is the Hazen-Williams roughness coefficient. Inverting the friction relationship reveals that flow is proportional to pressure drop raised to the exponent $\frac{1}{1.852} \approx 0.54$.</p>

        <p>The roughness coefficient $C$ dramatically affects available fire flow in aged municipal grids. Unlined cast iron water mains installed in older metropolitan centers in the early 20th century suffer severe internal tuberculation, dropping their hydraulic $C$-factor from an initial 130 down to 80 or lower. This tuberculation increases pipeline friction resistance by over 300%, severely restricting water delivery during large commercial fires. Conversely, modern cement-mortar lined ductile iron pipe (CMLDI) and molecularly oriented PVC pipe (AWWA C900) maintain a pristine $C$-factor between 140 and 150 over decades of service, ensuring maximum available GPM at minimal pressure drop.</p>

        <h2>Multi-Hydrant Simultaneous Group Testing Protocols</h2>
        <p>In large industrial parks, airports, and commercial warehousing districts, structural fire protection design requires available fire flows exceeding 2,500 to 5,000 GPM. A single 2.5-inch hydrant butt flowing at standard municipal pressure cannot deliver this volume without exceeding hazardous outlet velocities. Under NFPA 291 Chapter 4, test engineers conduct <strong>Group Hydrant Flow Tests</strong>:</p>
        <ul>
          <li><strong>Gauge Hydrant (Residual Hydrant):</strong> Placed centrally between the water main supply source and the discharging hydrants. Static pressure ($P_S$) and residual pressure ($P_R$) are continuously monitored here.</li>
          <li><strong>Flow Hydrants 1, 2, and 3:</strong> Multiple surrounding hydrants are opened sequentially. Stream velocity pressure is measured at each active outlet butt using calibrated Pitot tubes.</li>
          <li><strong>Flow Summation:</strong> The total test flow is calculated by summing all individual discharges: $Q_F = \sum Q_i = Q_1 + Q_2 + Q_3$. The aggregated group flow is then extrapolated to 20 PSI residual using the standard NFPA 291 formula, verifying whether the water distribution grid can support large fire attack apparatus and multiple building riser connections simultaneously.</li>
        </ul>
"""

# 5. BATTERY LIFE EXPANSION
BATTERY_EXTRA = """
        <h2>Electrochemical Cell Polarization &amp; Dynamic Internal Resistance</h2>
        <p>When an electrical load draws current from a battery cell, the closed-circuit operating terminal voltage ($V_{\text{terminal}}$) immediately drops below its open-circuit potential ($V_{\text{oc}}$). This voltage loss—termed <strong>overpotential</strong> or <strong>polarization</strong>—stems from three distinct electrochemical mechanisms occurring inside the battery:</p>
        <ul>
          <li><strong>Ohmic (IR) Polarization:</strong> Instantaneous resistive losses across the metallic current collectors, tabs, active electrode coatings, and the ionic resistance of the liquid or gel electrolyte. Governed strictly by Ohm's Law ($\Delta V_{\text{ohmic}} = I \cdot R_{\text{int}}$).</li>
          <li><strong>Activation (Charge-Transfer) Polarization:</strong> The energy barrier required to drive chemical redox reactions at the interface between electrode materials and the electrolyte. Governed by the Butler-Volmer equation.</li>
          <li><strong>Concentration (Mass-Transport) Polarization:</strong> The slowest dynamic component, caused by finite diffusion rates of lithium ions or sulfate ions migrating through the electrolyte and electrode pores. Under heavy continuous discharge, ion depletion occurs at the reaction sites, causing terminal voltage to sag prematurely even though chemical energy remains inside the bulk material.</li>
        </ul>

        <h2>State of Charge (SoC) Tracking &amp; Battery Management System (BMS) Logic</h2>
        <p>In modern lithium-ion and LiFePO4 battery banks, calculating remaining runtime and operational health is handled by an intelligent digital <strong>Battery Management System (BMS)</strong>. Because lithium iron phosphate has an extraordinarily flat discharge voltage curve—maintaining approximately 3.20V to 3.25V per cell across 20% to 80% State of Charge (SoC)—measuring voltage alone provides an inaccurate estimation of remaining capacity. Instead, professional BMS units utilize dual-mode state estimation:</p>
        <ol>
          <li><strong>Coulomb Counting (Current Integration):</strong> A precision shunt resistor or Hall-effect sensor measures instantaneous current ($I(t)$) in milliamperes at high sampling frequencies (100 Hz to 1 kHz). The BMS numerically integrates current over time:
            $$\text{SoC}(t) = \text{SoC}_0 - \frac{1}{C_{\text{rated}}} \int_0^t I(t) \, dt$$
          </li>
          <li><strong>Extended Kalman Filtering (EKF):</strong> Over long discharge cycles, Coulomb counting accumulates minor sensor drift errors. To eliminate drift, the BMS runs an adaptive Kalman filter algorithm that blends current integration with dynamic electrochemical equivalent-circuit models (ECM) and temperature-compensated open-circuit voltage lookups during rest intervals, maintaining state-of-charge tracking precision within &plusmn;1% accuracy.</li>
        </ol>
"""

updates = [
    ("bolt-torque-calculator.html", BOLT_EXTRA),
    ("bearing-life-calculator.html", BEARING_EXTRA),
    ("fire-alarm-battery-calculator.html", FA_EXTRA),
    ("hydrant-fire-flow-calculator.html", HYDRANT_EXTRA),
    ("battery-life-calculator.html", BATTERY_EXTRA),
]

for fname, extra_html in updates:
    fpath = os.path.join(BASE_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Insert extra technical section before <h2>Frequently Asked Technical Questions</h2>
    target = '<h2>Frequently Asked Technical Questions</h2>'
    if target in content and extra_html not in content:
        content = content.replace(target, extra_html + "\n\n        " + target)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[PASS] Expanded article in {fname}")
    else:
        print(f"[SKIP] Target not found or already expanded in {fname}")

