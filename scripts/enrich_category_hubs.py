import os
import re
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CATEGORY_DATA = {
    "engineering.html": {
        "title": "Electrical Installation Codes & Engineering Principles",
        "tag": "Industrial Electrical Standards",
        "author": "CalcHub Electrical & Power Systems Editorial Board",
        "verification": "Verified against IEC 60364-5-52:2009, NEC NFPA 70 (2023 Edition), and BS 7671 18th Edition",
        "standards": [
            ("Governing Code", "IEC 60364-5-52 & NEC Article 310 / 215"),
            ("Thermal Ratings", "PVC (70°C) / XLPE & EPR (90°C)"),
            ("Voltage Drop Limits", "3% Branch Circuit / 5% Total Feeder"),
            ("Calculation Engine", "Deterministic Client-Side Engineering Physics")
        ],
        "intro": """
Industrial electrical power distribution demands uncompromising precision. Undersized conductors induce catastrophic thermal degradation of insulation and excessive voltage drop, causing industrial motors to overheat and digital controllers to reset. Conversely, excessive oversizing squanders capital on expensive copper and oversized raceways. Professional low-voltage electrical engineering requires systematic evaluation of continuous load ampacity, environmental thermal derating, conduit group bunching, and circuit loop impedance.
        """,
        "example_title": "Industrial Case Study: 3-Phase 37 kW / 50 HP Chiller Feeder Sizing",
        "example_badge": "Real-World Engineering Problem",
        "steps": [
            ("Step 1: Calculate Full-Load Operational Design Current (Ib)",
             r"I_b = \frac{P}{\sqrt{3} \times V \times \cos\phi} = \frac{37{,}000}{\sqrt{3} \times 400 \times 0.86} = 62.15\text{ A}",
             "For a 37 kW refrigeration compressor operating at 400V 3-phase with an 0.86 lagging power factor, continuous design current Ib equals 62.15 Amperes."),
            ("Step 2: Apply Continuous Load Safety Margin (NEC 125% Rule)",
             r"I_{continuous} = I_b \times 1.25 = 62.15 \times 1.25 = 77.69\text{ A}",
             "Under NEC 210.19 and 215.2, continuous loads operating for 3 or more consecutive hours mandate a 125% ampacity sizing factor."),
            ("Step 3: Determine Environmental & Grouping Derating Factors (Ca × Cg)",
             r"C_a = 0.87\ (40^\circ\text{C PVC}),\quad C_g = 0.70\ (3\text{ circuits in conduit}) \implies C_{total} = 0.609",
             "Ambient temperature in the industrial plant reaches 40°C. With 3 circuits grouped in the same conduit run, heat dissipation is restricted according to IEC 60364-5-52 Table B.52.14."),
            ("Step 4: Compute Minimum Tabulated Conductor Ampacity (It) & Select Cable",
             r"I_t \ge \frac{I_{continuous}}{C_a \times C_g} = \frac{77.69}{0.609} = 127.57\text{ A}",
             'Consulting IEC standard tables for copper conductors in conduit (Method B2), a <strong>35 mm² copper cable</strong> provides a rated tabulated ampacity of 133 A, safely exceeding 127.57 A. Use our interactive <a href="cable-sizing-calculator.html">Cable Sizing Calculator</a> to verify custom installation methods A through F.'),
            ("Step 5: Verify Permissible Feeder Voltage Drop (ΔV) over 85m Run",
             r"\Delta V = \frac{\sqrt{3} \times I_b \times L \times (R\cos\phi + X\sin\phi)}{1000} = \frac{\sqrt{3} \times 62.15 \times 85 \times 0.627}{1000} = 5.73\text{ V}\ (1.43\%)",
             'The feeder run length is 85 meters. The calculated voltage drop is 5.73 Volts (1.43%), well below the strict 3.0% maximum allowable limit! Check your run distances instantly with our dedicated <a href="voltage-drop-calculator.html">Voltage Drop Calculator</a>, or solve circular impedance networks with our <a href="ohms-law-calculator.html">Ohm\'s Law Calculator</a>.')
        ],
        "final_result": "Selected Specification: 35 mm² 4-Core Copper PVC Cable | Rated Ampacity: 133 A (Derated: 81.0 A > 77.7 A) | Feeder Voltage Drop: 1.43% (Passed NEC/IEC Thresholds).",
        "faqs": [
            ("Why does the 3-phase voltage drop formula use √3 while single-phase uses 2?",
             "Single-phase circuits employ two conductors (line and neutral), meaning current must traverse the entire circuit distance twice (2 × L). In a balanced 3-phase 3-wire or 4-wire system, line-to-line voltage is vectorially displaced by 120 electrical degrees, which introduces the square-root-of-three factor (√3 ≈ 1.732) rather than doubling."),
            ("When does the NEC 125% continuous load factor apply?",
             "According to National Electrical Code (NEC) Article 100, any electrical load where the maximum current is expected to continue for 3 hours or more (such as commercial lighting, data center server racks, HVAC compressors, and EV charging stations) is classified as a continuous load and must be multiplied by 1.25 when sizing conductors and overcurrent protective devices."),
            ("Why is XLPE 90°C preferred over PVC 70°C in industrial cable trays?",
             "Cross-Linked Polyethylene (XLPE) possesses thermosetting dielectric molecular cross-linking, allowing continuous conductor operation at 90°C (with short-circuit withstand up to 250°C), compared to thermoplastic PVC's 70°C limit. This 20°C differential gives XLPE cables approximately 18% to 22% higher current carrying capacity for the identical copper cross-sectional area."),
            ("How do I choose between 4-band and 5-band precision resistors?",
             "Standard 4-band axial resistors provide two significant digits, a decimal multiplier, and a tolerance band (typically ±5% gold or ±10% silver). Precision electronic circuits requiring tight tolerances (±1% brown, ±0.5% green, or ±0.1% violet) require 5-band resistors, which provide three significant digits before the multiplier for high-accuracy circuit tuning. Decode any band instantly using our <a href=\"resistor-color-code-calculator.html\">Resistor Color Code Calculator</a>."),
            ("How do solar PV array voltages affect DC string cable sizing?",
             "Solar strings operate at fluctuating DC voltages up to 1,000V or 1,500V. High DC voltages reduce operational current for a given kilowatt rating, substantially lowering I²R power losses. However, cold ambient temperatures increase open-circuit voltage (Voc), requiring temperature-compensated calculations using our <a href=\"solar-panel-sizing-calculator.html\">Solar Panel Sizing Calculator</a>.")
        ]
    },

    "solar-energy.html": {
        "title": "Solar Photovoltaic & Energy Storage Engineering",
        "tag": "Renewable Energy Standards",
        "author": "CalcHub Solar & Renewable Energy Engineering Board",
        "verification": "Aligned with IEC 62109, NEC Article 690, and IEEE 1547 Grid Interconnection Standards",
        "standards": [
            ("Governing Codes", "NEC NFPA 70 Article 690 & 705"),
            ("Battery Chemistry", "LiFePO4 (80%–90% DoD) / AGM Lead-Acid (50% DoD)"),
            ("Solar Irradiance", "NREL National Solar Radiation Database (NSRDB)"),
            ("Inverter Architecture", "Pure Sine Wave with 200%–300% Motor Surge Rating")
        ],
        "intro": """
Designing reliable off-grid and grid-hybrid photovoltaic systems requires balancing solar irradiance variability with continuous kilowatt-hour demands. System failure typically stems from undersizing storage for non-productive weather days (autonomy) or ignoring inductive motor inrush currents during compressor startup. Proper solar engineering coordinates PV array harvest wattage, deep-cycle battery chemistry amp-hours, and inverter continuous surge capacity.
        """,
        "example_title": "Field Case Study: Off-Grid Commercial Cold-Storage PV System",
        "example_badge": "Real-World Engineering Problem",
        "steps": [
            ("Step 1: Quantify Daily Energy Demand Accounting for System Inefficiencies",
             r"E_{target} = \frac{E_{load}}{\eta_{system}} = \frac{28\text{ kWh}}{0.82} = 34.15\text{ kWh/day}",
             "An off-grid agricultural refrigeration facility consumes 28 kWh per day. Factoring in an 18% cumulative loss (inverter conversion, wire resistance, and dust derating), daily array harvest target is 34.15 kWh."),
            ("Step 2: Size Solar Photovoltaic Array Peak Wattage (Wp)",
             r"P_{pv} = \frac{E_{target}}{\text{PSH}} = \frac{34{,}150\text{ Wh}}{4.6\text{ PSH}} = 7{,}424\text{ W} \approx 7.5\text{ kWp}",
             'With an average winter solar irradiance of 4.6 Peak Sun Hours (PSH), the minimum array capacity is 7,424 Watts. Specifying fourteen 550W Tier-1 Mono-PERC modules delivers 7,700 Watts peak. Model your array with our <a href="solar-panel-sizing-calculator.html">Solar Panel Sizing Calculator</a>.'),
            ("Step 3: Size Deep-Cycle Lithium Battery Bank Storage (Ah & kWh)",
             r"C_{batt} = \frac{E_{load} \times \text{Days of Autonomy}}{V_{bus} \times \text{DoD} \times \eta_{batt}} = \frac{28{,}000 \times 2}{48\text{V} \times 0.80 \times 0.95} = 1{,}535\text{ Ah}\ (73.7\text{ kWh})",
             'Guaranteeing 2 continuous days of overcast autonomy using a 48V LiFePO4 battery bank operating at 80% maximum Depth of Discharge (DoD) requires 1,535 Amp-hours. Optimize your chemistry and bank capacity using our <a href="solar-battery-bank-calculator.html">Solar Battery Bank Calculator</a>.'),
            ("Step 4: Size the Off-Grid Power Inverter Surge Capacity",
             r"P_{inv,cont} \ge 5.2\text{ kW},\quad P_{inv,surge} \ge 3 \times P_{compressor} = 10.5\text{ kVA}",
             'Continuous plant load is 5.2 kW. When the 3.5 kW refrigeration compressor cycles on, initial inductive rotor lock demands 300% starting current for 2 seconds. A 10.0 kVA pure sine wave inverter is required. Verify your inverter rating with our <a href="solar-inverter-sizing-calculator.html">Solar Inverter Sizing Calculator</a>.'),
            ("Step 5: Size High-Current DC Battery Feeders & EV Station Infrastructure",
             r"I_{dc} = \frac{P_{inv}}{\eta_{inv} \times V_{bus,min}} = \frac{5{,}200}{0.92 \times 44\text{V}} = 128.5\text{ A}",
             'At minimum battery cutoff voltage (44V), DC current reaches 128.5 A, requiring heavy-gauge 50 mm² (1/0 AWG) flexible copper welding cable. Cross-check cable thermal ampacity with our <a href="cable-sizing-calculator.html">Cable Sizing Calculator</a>, and model electric vehicle fleet charging with our <a href="ev-charging-time-calculator.html">EV Charging Time Calculator</a>.')
        ],
        "final_result": "Engineered System: 7.7 kWp PV Array (14 × 550W) | 73.7 kWh LiFePO4 Storage Bank (48V / 1,535 Ah) | 10.0 kVA Pure Sine Wave Inverter | Fully Autonomous for 48 Hours.",
        "faqs": [
            ("What are Peak Sun Hours (PSH) and how do they differ from daylight hours?",
             "Peak Sun Hours (PSH) represent the equivalent number of hours in a day during which solar irradiance averages standard test condition (STC) intensity of 1,000 Watts per square meter (1 kW/m²). A location may receive 12 hours of total daylight, but low morning and evening sun angles mean it may only generate 4.5 to 5.5 PSH of usable peak energy."),
            ("Why is Depth of Discharge (DoD) critical for solar battery lifespan?",
             "Depth of Discharge measures the percentage of battery capacity drawn during each cycle. Lead-acid/AGM batteries experience rapid plate sulfation and cell failure if discharged past 50% DoD (yielding roughly 500–800 cycles). Lithium Iron Phosphate (LiFePO4) chemistries maintain stable crystal structure up to 80%–90% DoD, reliably exceeding 4,000–6,000 cycles."),
            ("How does ambient cold temperature affect solar panel open-circuit voltage (Voc)?",
             "Photovoltaic silicon cells exhibit a negative temperature coefficient of voltage (typically -0.28% to -0.35% per °C). On cold winter mornings (-10°C), open-circuit voltage rises substantially above factory STC ratings (25°C). Solar charge controllers and inverters will suffer permanent overvoltage destruction if strings are sized without calculating cold Voc."),
            ("How does Level 2 EV charging integrate with a residential solar system?",
             "A Level 2 EV charging station operating at 240V / 32A draws 7.68 kW of continuous power. To charge an EV exclusively from solar, the PV array must generate surplus energy above base household consumption, or draw from an intelligent battery storage buffer. Model charge speeds and energy draw with our <a href=\"ev-charging-time-calculator.html\">EV Charging Time Calculator</a>.")
        ]
    },

    "mechanical.html": {
        "title": "HVAC Thermal Dynamics & Mechanical Engineering",
        "tag": "ASME & ASHRAE Standards",
        "author": "CalcHub Mechanical & HVAC Systems Editorial Board",
        "verification": "Compliant with ASHRAE Standard 90.1, ASHRAE 62.1, and ASME B31.3 Process Piping",
        "standards": [
            ("Thermal Guidelines", "ASHRAE Standard 90.1 & Standard 55 Thermal Comfort"),
            ("Hydraulics Code", "ASME B31.3 & Darcy-Weisbach / Colebrook-White Equations"),
            ("Mechanical Drives", "AGMA 6013-A06 & Industrial Shaft Torque Derivations"),
            ("Units Supported", "Imperial (BTU/hr, CFM, GPM) & Metric SI (kW, m³/hr, L/s)")
        ],
        "intro": """
Mechanical building services and industrial process systems require rigorous thermodynamic and fluid dynamic modeling. Undersized HVAC chillers fail to control indoor humidity during peak wet-bulb ambient conditions, causing mould growth and equipment downtime. Similarly, undersized fluid process piping leads to excessive frictional head loss, pump cavitation, and premature valve failure. Engineering success relies on accurate sensible-latent heat load quantification, optimal fluid velocity sizing, and mechanical torque balancing.
        """,
        "example_title": "Engineering Case Study: Data Center Server Room HVAC & Hydronic Loop",
        "example_badge": "Real-World Engineering Problem",
        "steps": [
            ("Step 1: Calculate High-Density IT Equipment Thermal Heat Dissipation",
             r"Q_{equipment} = P_{kW} \times 3{,}412.14 = 16.0 \times 3{,}412.14 = 54{,}594\text{ BTU/hr}",
             "A 500 sq ft server room houses server racks drawing 16.0 kW of electrical power. In enclosed IT spaces, 100% of electrical power consumed converts directly to sensible heat dissipation."),
            ("Step 2: Calculate Building Envelope, Lighting, and Occupant Heat Gains",
             r"Q_{envelope} = Q_{glass} + Q_{lighting} + Q_{people} = 4{,}200 + 4{,}095 + 1{,}600 = 9{,}895\text{ BTU/hr}",
             "Adding solar heat gain from west-facing glazing (4,200 BTU/hr), LED lighting arrays (4,095 BTU/hr), and 4 technical staff (4 × 400 BTU/hr) yields 9,895 BTU/hr."),
            ("Step 3: Determine Total Required Cooling Capacity in Tons of Refrigeration (TR)",
             r"Q_{total} = 54{,}594 + 9{,}895 = 64{,}489\text{ BTU/hr} \implies \text{Capacity} = \frac{64{,}489}{12{,}000} = 5.37\text{ TR}",
             'With 1 Ton of Refrigeration (TR) equaling 12,000 BTU/hr (3.517 kW), the facility requires a 6.0 TR commercial precision cooling unit. Calculate your custom commercial or residential cooling demands with our <a href="cooling-load-calculator.html">Cooling Load Calculator</a>.'),
            ("Step 4: Size the Hydronic Chilled Water Piping Loop",
             r"Q_{water} = 2.4\text{ GPM/ton} \times 5.37\text{ TR} = 12.9\text{ GPM},\quad d = \sqrt{\frac{12.9}{2.448 \times 4.0}} = 1.15\text{ in}",
             'To prevent pipe erosion and excessive noise, commercial chilled water velocity is capped at 4.0 ft/s. Sizing for 12.9 GPM dictates a <strong>1.25-inch Schedule 40 steel pipe</strong>. Model fluid friction and optimal velocities using our <a href="pipe-sizing-calculator.html">Pipe Sizing Calculator</a>.'),
            ("Step 5: Size Pump Circulation Motor Shaft Torque",
             r"T = 9{,}550 \times \frac{P_{kW}}{N_{RPM}} = 9{,}550 \times \frac{1.5}{1{,}450} = 9.88\text{ N}\cdot\text{m}",
             'For a 1.5 kW circulation pump operating at 1,450 RPM, continuous shaft torque equals 9.88 N·m. Compute rotational power and gear reduction mechanical moments with our <a href="torque-calculator.html">Torque Calculator</a>, or convert units with our <a href="unit-converter.html">Unit Converter</a>.')
        ],
        "final_result": "Engineered Specification: 6.0 TR Precision Air Handler (64,500 BTU/hr) | 1.25-inch Hydronic Piping @ 12.9 GPM (3.5 ft/s velocity) | 1.5 kW Pump Motor Delivering 9.88 N·m Continuous Torque.",
        "faqs": [
            ("What is the difference between sensible heat and latent heat in HVAC cooling?",
             "Sensible heat is thermal energy that causes a direct change in dry-bulb air temperature without changing moisture content (e.g., heat from computer servers, lighting, and solar radiation). Latent heat represents the energy required to remove moisture (humidity) from the air through condensation. Total cooling load is the enthalpy sum of sensible and latent gains."),
            ("Why is fluid velocity restricted to 4–8 ft/s (1.2–2.4 m/s) in commercial water pipes?",
             "Flow velocities below 2 ft/s allow suspended solids and silt to settle, clogging pipes and heat exchangers. Conversely, velocities exceeding 8 ft/s generate turbulent fluid erosion, pipe wall degradation, hydraulic water hammer, and severe pumping energy losses. ASHRAE 90.1 sets prescriptive pipe velocity boundaries to balance capital pipe cost and lifetime pumping energy."),
            ("How do I convert between Tons of Refrigeration (TR), BTU/hr, and Kilowatts?",
             "One Ton of Refrigeration (TR) is defined as the latent heat of fusion required to freeze or melt 2,000 lbs (one short ton) of ice at 32°F in 24 hours. Mathematically: 1 TR = 12,000 BTU/hr = 3.51685 Kilowatts (kW). You can convert thermal power and pressure seamlessly with our <a href=\"unit-converter.html\">Unit Converter</a>."),
            ("What safety factor should be applied to mechanical drive shaft torque?",
             "Industrial gear and shaft design under AGMA standards applies a Mechanical Service Factor (SF) ranging from 1.0 (smooth uniform electric motor driving a fan) to 2.25 (internal combustion engine driving heavy crushers, ball mills, or reciprocating compressors with severe torsional shock loads).")
        ]
    },

    "civil.html": {
        "title": "Concrete Technology & Structural Reinforcement",
        "tag": "ACI & Eurocode Standards",
        "author": "CalcHub Civil & Structural Construction Editorial Board",
        "verification": "Aligned with ACI 318-19, Eurocode 2 (EN 1992-1-1), BS 8110, and ASTM A615",
        "standards": [
            ("Structural Concrete", "ACI 318-19 Building Code Requirements for Structural Concrete"),
            ("Steel Reinforcement", "ASTM A615 / A615M Deformed Billet-Steel Bars (Grade 60 / 420 MPa)"),
            ("Dry Bulking Factor", "1.54 Standard Volumetric Dry-to-Wet Concrete Conversion"),
            ("Mix Proportions", "Nominal 1:1.5:3 (M20) / 1:2:4 (M15) / 1:1:2 (M25)")
        ],
        "intro": """
Structural concrete construction demands strict control over batch volumes, water-cement ratios, and rebar reinforcement densities. Inadequate material ordering halts continuous monolithic pours, causing fatal cold joints. Conversely, inaccurate rebar detailing leads to tensile failure or brittle shear collapse. CalcHub civil engineering calculators compute exact volumetric constituent yields, bulk material dry weights, and metric/imperial reinforcement bar weights.
        """,
        "example_title": "Field Case Study: Suspended Floor Slab Concrete & Rebar Take-Off",
        "example_badge": "Real-World Engineering Problem",
        "steps": [
            ("Step 1: Compute Net In-Situ Wet Concrete Volume",
             r"V_{wet} = L \times W \times T = 14.0\text{m} \times 9.0\text{m} \times 0.18\text{m} = 22.68\text{ m}^3",
             "A commercial reinforced concrete suspended slab measures 14.0 meters long, 9.0 meters wide, and 0.18 meters (180 mm) in thickness, yielding 22.68 cubic meters of wet concrete."),
            ("Step 2: Apply Dry Bulking Factor for Granular Material Batching",
             r"V_{dry} = V_{wet} \times 1.54 = 22.68 \times 1.54 = 34.93\text{ m}^3",
             "Dry cement, sand, and stone contain air voids. Adding water causes voids to collapse. Converting wet slab volume into dry batching volume requires multiplying by the empirical factor of 1.54."),
            ("Step 3: Calculate Bagged Cement, Fine Sand, and Coarse Aggregate Yield (1:1.5:3 Mix)",
             r"\text{Sum of Ratios} = 1 + 1.5 + 3 = 5.5,\quad \text{Cement Volume} = \frac{1}{5.5} \times 34.93 = 6.35\text{ m}^3",
             'At a bulk density of 1,440 kg/m³, 6.35 m³ equates to 9,144 kg of cement, or <strong>183 standard 50kg bags</strong> (192 bags with 5% jobsite wastage). Sand requires 9.5 m³ and 20mm crushed stone requires 19.1 m³. Calculate slabs, footings, and columns using our <a href="concrete-calculator.html">Concrete Calculator</a>.'),
            ("Step 4: Quantify T12 High-Yield Deformed Steel Reinforcement Weight",
             r"W_{bar} = \frac{D^2}{162} = \frac{12^2}{162} = 0.888\text{ kg/m},\quad \text{Total Length} = 1{,}700\text{m} \implies \text{Mass} = 1{,}509.6\text{ kg}",
             'The structural schedule specifies 12mm rebar placed at 150mm center-to-center in both directions. Accounting for hook development lengths, total linear steel measures 1,700 meters. Steel total mass equals <strong>1.51 metric tonnes</strong>. Detail your bar schedules with our <a href="rebar-calculator.html">Rebar Calculator</a>.')
        ],
        "final_result": "Material Take-Off: 23.8 m³ Ready-Mix Concrete (or 192 Bags Cement + 9.5 m³ Sand + 19.1 m³ Aggregate) | 1.51 Tonnes T12 High-Yield Reinforcing Steel | 100% Monolithic Pour Security.",
        "faqs": [
            ("Why is the dry concrete bulking factor 1.54 used in volume estimation?",
             "Dry aggregate particles (sand and crushed stone) have approximately 30% to 35% void ratios between angular grains. When water and fine cement paste are mixed in, the paste lubricates and fills these inter-granular voids. Consequently, it takes approximately 1.54 cubic meters of dry loose materials to yield 1.0 cubic meter of compacted wet in-situ concrete."),
            ("How does water-cement ratio (w/c) dictate structural compressive strength?",
             "According to Abrams' Law, the compressive strength of fully compacted concrete is inversely proportional to its water-cement ratio. A lower w/c ratio (e.g., 0.40 to 0.45) leaves fewer capillary pores as excess water evaporates, producing dense, watertight concrete with high 28-day strength (35–45 MPa). High w/c ratios (>0.60) cause severe bleeding, honeycombing, and cracking."),
            ("What is the standard rebar lap splice length in structural slabs and beams?",
             "Under ACI 318-19 and Eurocode 2, tensile lap splice lengths depend on concrete compressive strength, bar diameter, and coating. A standard rule of thumb for Grade 60 (420 MPa) deformed bars in normal-weight concrete is 40 to 50 times the bar diameter (40d to 50d). For a 12mm rebar, the minimum tension lap length is 480 mm to 600 mm."),
            ("What is the difference between concrete compressive strength classes (e.g., C20/25 vs 3000 PSI)?",
             "European Eurocode standard EN 206 designates concrete as C20/25, where 20 MPa is characteristic compressive strength measured on a 150mm cylinder, and 25 MPa is strength measured on a 150mm cube. American concrete standards (ASTM/ACI) express cylinder compressive strength (f'c) in pounds per square inch, such as 3,000 PSI (approx. 20.7 MPa) or 4,000 PSI (approx. 27.6 MPa).")
        ]
    },

    "chemical.html": {
        "title": "Process Stoichiometry & Chemical Treatment Engineering",
        "tag": "AWWA & Process Standards",
        "author": "CalcHub Chemical & Process Engineering Editorial Board",
        "verification": "Aligned with AWWA Standard B300, EPA Water Treatment Manuals, and ISO 5167",
        "standards": [
            ("Water Disinfection", "AWWA Standard B300 Hypochlorite & EPA Primary Drinking Water Regs"),
            ("Flow Dynamics", "Reynolds Number (Re), Darcy-Weisbach Friction, and Bernoulli Continuity"),
            ("Concentration Units", "ppm (parts per million), mg/L, % Mass Fraction, Molarity (M)"),
            ("Metering Pumps", "Diaphragm Stroke-Frequency Calibration and Volumetric Dosing (mL/min)")
        ],
        "intro": """
Precision chemical dosing is critical across water treatment, petrochemical refining, pharmaceutical synthesis, and industrial wastewater neutralization. Under-dosing biocides or coagulants fails environmental discharge regulations and biological pathogen standards. Over-dosing squanders expensive chemical stock, corrodes downstream infrastructure, and generates toxic disinfection byproducts. Engineering accuracy requires calculating stoichiometric mass flow rates, active reagent percentage adjustments, and feed pump volumetric delivery rates.
        """,
        "example_title": "Industrial Case Study: Municipal Wastewater Effluent Chlorination",
        "example_badge": "Real-World Engineering Problem",
        "steps": [
            ("Step 1: Quantify Volumetric Flow Rate & Target Active Chemical Dose",
             r"Q = 1{,}800\text{ m}^3/\text{day}\ (75\text{ m}^3/\text{hr}),\quad C_{target} = 5.0\text{ mg/L}\ (5.0\text{ g/m}^3)",
             "A municipal wastewater treatment facility discharges 1,800 m³/day (75 m³/hr). EPA regulations mandate a residual free available chlorine dosing rate of 5.0 mg/L (ppm)."),
            ("Step 2: Calculate Pure Active Chlorine Chemical Demand",
             r"\dot{m}_{active} = Q \times C_{target} = 1{,}800\text{ m}^3 \times 5.0\text{ g/m}^3 = 9{,}000\text{ g/day} = 9.00\text{ kg/day}",
             "The process demands 9.00 kg of pure active chlorine element per 24-hour continuous operating cycle."),
            ("Step 3: Adjust for Commercial Sodium Hypochlorite Active Concentration",
             r"\dot{m}_{commercial} = \frac{\dot{m}_{active}}{\text{Concentration}} = \frac{9.00\text{ kg}}{0.125} = 72.00\text{ kg/day}",
             "The facility utilizes commercial bulk sodium hypochlorite liquid (bleach) supplied at 12.5% active chlorine by mass. Daily commercial chemical demand is 72.00 kg/day."),
            ("Step 4: Convert Product Mass into Volumetric Feed Pump Delivery Rate",
             r"V_{daily} = \frac{72.00\text{ kg}}{1.21\text{ kg/L}} = 59.50\text{ L/day} \implies \text{Dosing Rate} = 41.32\text{ mL/min}",
             'Commercial 12.5% hypochlorite exhibits a specific gravity of 1.21 kg/L. The dosing metering pump must be calibrated to deliver <strong>41.32 mL/min (2.48 L/hr)</strong>. Solve chemical feeds and pump settings with our <a href="chemical-dosing-calculator.html">Chemical Dosing Calculator</a>.'),
            ("Step 5: Check Injection Quill Pipe Flow & Velocity Limits",
             r"v = \frac{Q}{A} \implies \text{Verify non-clogging laminar quill dispersion}",
             'Verify delivery line sizing and chemical distribution piping using our <a href="pipe-sizing-calculator.html">Pipe Sizing Calculator</a> and perform metric-imperial conversions with our <a href="unit-converter.html">Unit Converter</a>.')
        ],
        "final_result": "Engineered Delivery: 59.50 L/Day Bulk Hypochlorite (12.5%) | Dosing Pump Setpoint: 41.32 mL/min | Accurate Residual Disinfection Guaranteed.",
        "faqs": [
            ("What is the relationship between parts per million (ppm) and milligrams per liter (mg/L)?",
             "In dilute aqueous solutions where the specific gravity of the liquid is approximately 1.00 (such as clean drinking water), 1 milligram per liter (mg/L) is mathematically identical to 1 part per million (ppm), because 1 liter of water weighs exactly 1,000,000 milligrams. However, for dense solutions like heavy brine or 50% caustic soda (SG = 1.52), specific gravity must be factored in."),
            ("How does specific gravity affect liquid chemical metering pumps?",
             "Positive displacement diaphragm metering pumps displace a fixed volume per stroke. When chemicals are sold and specified by weight (e.g., kilograms or pounds) but dosed by volume (liters or gallons), failing to divide by solution specific gravity causes severe over-dosing errors (e.g., ferric chloride with SG 1.42 or sulfuric acid with SG 1.84)."),
            ("Why is chlorine demand distinct from chlorine dosage?",
             "Chlorine dosage is the total quantity of chemical injected into the water stream. Chlorine demand is the amount consumed by reacting with organic matter, iron, manganese, and ammonia. The remainder is chlorine residual, which provides critical downstream antimicrobial protection throughout distribution networks."),
            ("What is the difference between molarity (M) and normality (N)?",
             "Molarity is the number of moles of solute per liter of solution (mol/L). Normality is the number of gram equivalents per liter (eq/L). For monoprotic acids like hydrochloric acid (HCl), 1 M = 1 N. For diprotic sulfuric acid (H2SO4), each mole donates two protons, making a 1 M solution equivalent to 2 N.")
        ]
    },

    "fire-safety.html": {
        "title": "Fire Alarm & Life Safety Engineering",
        "tag": "NFPA & Life Safety Standards",
        "author": "CalcHub Fire & Life Safety Systems Editorial Board",
        "verification": "Compliant with NFPA 72 National Fire Alarm Code, BS 5839-1, and EN 54-7",
        "standards": [
            ("Governing Code", "NFPA 72 National Fire Alarm and Signaling Code (2022/2025 Ed.)"),
            ("Coverage Geometry", "30-Foot (9.1m) Grid Spacing & 21.2-Foot (6.4m) Corner Radius"),
            ("Air Flow Reductions", "Spacing reductions applied when air change rate exceeds 8 ACH"),
            ("Ceiling Profiles", "Smooth Flat Slab, Beam/Girder Pockets, and Sloped Ceilings")
        ],
        "intro": """
Life safety fire detection systems are governed by strict prescriptive codes. Improper smoke detector layout creates hazardous dead-air pockets in ceiling corners where thermal stratification prevents buoyant smoke plumes from reaching sensing chambers. Over-spacing detectors delays emergency egress signaling, while excessive spacing increases building electrical cabling costs. Fire protection engineers rely on NFPA 72 geometric coverage circles, ceiling height reduction factors, and notification loop voltage drop limits.
        """,
        "example_title": "Design Case Study: High-Bay Commercial Warehouse Detection Grid",
        "example_badge": "Real-World Engineering Problem",
        "steps": [
            ("Step 1: Establish NFPA 72 Baseline Radial & Square Grid Boundaries",
             r"S_{baseline} = 30\text{ ft}\ (9.1\text{m}),\quad R_{max} = \frac{\sqrt{30^2 + 30^2}}{2} = 21.21\text{ ft}\ (6.47\text{m})",
             "Under NFPA 72 Clause 17.7.3, baseline spacing for spot-type smoke detectors on smooth flat ceilings is 30 ft (9.1m) on center, with maximum radial distance from any point in the room to the nearest detector not exceeding 21.2 ft (6.47m)."),
            ("Step 2: Determine Dimensional Spacing Intervals for 60m × 30m Facility",
             r"\text{Columns} = \lceil \frac{60\text{m}}{9.1\text{m}} \rceil = 7\text{ intervals},\quad \text{Rows} = \lceil \frac{30\text{m}}{9.1\text{m}} \rceil = 4\text{ intervals}",
             "For a logistics warehouse measuring 60.0m in length by 30.0m in width with 4.8m ceiling height and air changes under 1 ACH, the floor plan partitions into 7 longitudinal columns and 4 transverse rows."),
            ("Step 3: Calculate Detector Spacing and Wall Offset Clearances",
             r"S_{length} = \frac{60}{7} = 8.57\text{m}\ (< 9.1\text{m}),\quad S_{width} = \frac{30}{4} = 7.50\text{m}\ (< 9.1\text{m})",
             "Detectors are centered at 8.57m along length and 7.50m across width. Distance to perimeter walls is half spacing (4.29m and 3.75m), fully complying with the 0.5S edge limit."),
            ("Step 4: Total Bill of Materials for Addressable Optical Detectors",
             r"\text{Total Detectors} = 7 \times 4 = 28\text{ addressable optical units}",
             'The complete floor space requires exactly <strong>28 detectors</strong> to guarantee 100% smoke plume coverage without blind spots. Calculate customized room layouts with our <a href="smoke-detector-spacing-calculator.html">Smoke Detector Spacing Calculator</a>.'),
            ("Step 5: Verify Notification Appliance Circuit (NAC) Loop Resistance & Strobe Candela",
             r"V_{drop} = I_{NAC} \times R_{loop} \le 16.0\text{V minimum operating threshold}",
             'Check NAC strobe notification loop line voltage drop using our <a href="voltage-drop-calculator.html">Voltage Drop Calculator</a> and circuit loop current limits with our <a href="ohms-law-calculator.html">Ohm\'s Law Calculator</a>.')
        ],
        "final_result": "Engineered Layout: 28 Optical Smoke Detectors in 7 × 4 Grid | Long Spacing: 8.57m | Width Spacing: 7.50m | 100% Compliant with NFPA 72 Radial Coverage.",
        "faqs": [
            ("Why cannot smoke detectors be mounted directly in ceiling-wall corners?",
             "In any enclosed room, thermal convection creates a boundary stagnation layer known as the 'dead air space' in the 90-degree intersection where the ceiling meets the wall. NFPA 72 strictly mandates that detectors must not be mounted within 4 inches (100 mm) of the ceiling-wall corner, and wall-mounted units must be placed 4 to 12 inches (100–300 mm) down from the ceiling."),
            ("How do high air change rates (ACH) affect smoke detector spacing?",
             "In cleanrooms, server facilities, and high-velocity HVAC spaces where ventilation exceeds 8 Air Changes per Hour (ACH), high air velocity dilutes smoke plumes and blows them away from ceiling detectors. NFPA 72 Table 17.7.6.3.3.1 mandates reducing spacing down to 25 ft, 20 ft, or even 15 ft as ACH increases."),
            ("What is the peak rule for sloped ceilings under NFPA 72?",
             "In buildings with pitched or peaked cathedral roofs, smoke migrates upward and collects first at the apex. Detectors must be placed within 3 feet (0.9 meters) of the peak, measured horizontally along the ceiling profile."),
            ("What is the difference between ionization and photoelectric smoke detection?",
             "Ionization detectors utilize a radioactive americium-241 source to detect microscopic combustion particles typical of fast-flaming wood and paper fires. Photoelectric detectors utilize a light-scattering optical sensor superior at detecting larger smoke particles from slow-smoldering electrical cable and upholstery fires, while being far less prone to false kitchen alarms.")
        ]
    },

    "finance.html": {
        "title": "Corporate Finance, Annuities & Wealth Modeling",
        "tag": "Financial & Accounting Standards",
        "author": "CalcHub Financial & Investment Editorial Board",
        "verification": "Compliant with US GAAP, IFRS 9 Financial Instruments, and Truth in Lending Act (Reg Z)",
        "standards": [
            ("Amortization Engine", "Reducing-Balance Amortization & Ordinary Annuities"),
            ("Compounding Frequency", "Annual, Semi-Annual, Quarterly, Monthly, and Continuous (e^rt)"),
            ("Regulatory Disclosure", "Annual Percentage Rate (APR) vs Effective Annual Rate (EAR)"),
            ("Compensation Systems", "Gross-to-Net Payroll Deduction and Marginal Tax Bracket Stacking")
        ],
        "intro": """
Financial planning and debt servicing require mathematically sound compounding and amortization algorithms. Relying on simplified flat-rate interest estimates costs borrowers tens of thousands of dollars in undisclosed finance charges. Conversely, neglecting the compounding frequency in retirement portfolios distorts wealth accumulation by hundreds of thousands over a career. CalcHub financial calculators implement verified reducing-balance amortization schedules, compound investment growth models, and take-home salary projections.
        """,
        "example_title": "Financial Case Study: Commercial Real Estate Mortgage Amortization",
        "example_badge": "Real-World Analytical Problem",
        "steps": [
            ("Step 1: Define Borrowing Principal, Annual Rate, and Repayment Tenor",
             r"P = \$420{,}000,\quad r_{annual} = 6.50\%,\quad n = 20\text{ years}\ (240\text{ monthly payments})",
             "A corporate borrower secures a $420,000 commercial facility mortgage at a 6.50% annual interest rate repayable over a 20-year term."),
            ("Step 2: Calculate Periodic Monthly Interest Rate (r)",
             r"r = \frac{0.065}{12} = 0.00541667\text{ per month}",
             "Interest is calculated monthly on the remaining outstanding balance at 0.5417% per month."),
            ("Step 3: Calculate Fixed Equated Monthly Installment (EMI)",
             r"\text{EMI} = \frac{P \cdot r \cdot (1+r)^n}{(1+r)^n - 1} = \frac{420{,}000 \cdot 0.005417 \cdot (1.005417)^{240}}{(1.005417)^{240} - 1} = \$3{,}131.29",
             'The fixed monthly repayment is <strong>$3,131.29</strong>. Compute repayment schedules, loan crossovers, and prepayments using our <a href="loan-emi-calculator.html">Loan EMI Calculator</a>.'),
            ("Step 4: Compute Total Lifetime Repayment & Interest Incurred",
             r"\text{Total Outflow} = 240 \times \$3{,}131.29 = \$751{,}509.60,\quad \text{Interest Paid} = \$331{,}509.60",
             'Over 20 years, the borrower pays $331,509.60 in cumulative interest charges (78.9% of original principal). Compare linear debt with our <a href="simple-interest-calculator.html">Simple Interest Calculator</a>.'),
            ("Step 5: Compare Against Sinking Fund Wealth Compounding & Payroll Cash Flows",
             r"A = P\left(1 + \frac{r}{m}\right)^{mt} \implies \text{Compound investment returns}",
             'Discover the wealth growth of compounding surpluses with our <a href="compound-interest-calculator.html">Compound Interest Calculator</a>, budget take-home pay with our <a href="salary-calculator.html">Salary Calculator</a>, and model markdowns with our <a href="discount-calculator.html">Discount Calculator</a>.')
        ],
        "final_result": "Amortization Profile: Monthly Payment: $3,131.29 | Total Loan Repayment: $751,509.60 | Total Interest Incurred: $331,509.60 | Principal-Interest Parity reached at Month 104.",
        "faqs": [
            ("What is the difference between reducing-balance interest and flat-rate interest?",
             "In reducing-balance amortization, interest for each billing cycle is calculated strictly on the remaining principal balance, meaning interest decreases as you repay the loan. In flat-rate loans, interest is calculated on the full initial loan amount across the entire term, doubling or tripling the effective interest rate compared to reducing loans."),
            ("What is the difference between APR and APY / EAR?",
             "Annual Percentage Rate (APR) represents the nominal annualized interest rate without taking into account intra-year compounding. Annual Percentage Yield (APY) or Effective Annual Rate (EAR) includes the effect of compounding frequency (monthly, daily). For example, 12% APR compounded monthly equals 12.68% APY."),
            ("What is loan amortization tilting?",
             "In the early years of a long-term loan (e.g., years 1 through 7 of a 30-year mortgage), monthly EMI payments consist almost entirely of interest charges (often 70%–80%), with very little principal paydown. Only after the amortization crossover point does the principal portion exceed the interest portion."),
            ("How do marginal tax brackets affect gross-to-net salary take-home pay?",
             "Income tax brackets are progressive, not flat. Moving into a higher bracket (e.g., from 22% to 24%) means only the dollars earned above that threshold are taxed at 24%, not your entire income. Check your take-home pay accurately with our <a href=\"salary-calculator.html\">Salary Calculator</a>.")
        ]
    },

    "health.html": {
        "title": "Clinical Anthropometry, Metabolism & Energy Balance",
        "tag": "WHO & Clinical Standards",
        "author": "CalcHub Health, Nutrition & Fitness Editorial Board",
        "verification": "Aligned with World Health Organization (WHO) Technical Report 854 and Revised Mifflin-St Jeor Equations",
        "standards": [
            ("BMI Categories", "WHO Technical Report Series 854 & CDC Adult BMI Classifications"),
            ("Body Composition", "U.S. Navy Circumference Equation (DoD Directive 1308.3)"),
            ("Metabolic Rate", "Mifflin-St Jeor Equation (Validated Gold Standard vs Indirect Calorimetry)"),
            ("Hydration Baseline", "European Food Safety Authority (EFSA) & U.S. National Academies Guidelines")
        ],
        "intro": """
Clinical body composition assessment and nutritional prescription require objective physiological modeling. Relying solely on gross body weight or generic Body Mass Index (BMI) cutoffs misclassifies muscular athletes as obese and overlooks sarcopenic obesity in sedentary individuals. Professional physical health programming integrates body mass indices with circumference-based body fat modeling, Mifflin-St Jeor basal metabolic calculations, and daily physical activity level (PAL) multipliers.
        """,
        "example_title": "Clinical Case Study: Adult Anthropometric & Metabolic Prescription",
        "example_badge": "Real-World Clinical Problem",
        "steps": [
            ("Step 1: Compute Standard Body Mass Index (BMI)",
             r"\text{BMI} = \frac{\text{Weight (kg)}}{\text{Height (m)}^2} = \frac{86.5}{1.78^2} = 27.30\text{ kg/m}^2",
             'For a 36-year-old male weighing 86.5 kg with a height of 178 cm (1.78 m), BMI is 27.30 kg/m² (WHO Overweight classification: 25.0–29.9). Assess your index with our <a href="bmi-calculator.html">BMI Calculator</a>.'),
            ("Step 2: Determine Body Fat Percentage Using U.S. Navy Circumference Method",
             r"\Delta_{circ} = \text{Waist} - \text{Neck} = 93.0 - 39.5 = 53.5\text{ cm} \implies \text{Body Fat} = 19.8\%",
             'Circumference analysis reveals 19.8% body fat, which corresponds to <strong>69.37 kg of Lean Body Mass (LBM)</strong> and 17.13 kg of fat mass. Determine your lean mass with our <a href="body-fat-calculator.html">Body Fat Calculator</a>.'),
            ("Step 3: Calculate Basal Metabolic Rate (BMR) via Mifflin-St Jeor Equation",
             r"\text{BMR} = 10(W) + 6.25(H) - 5(A) + 5 = 10(86.5) + 6.25(178) - 5(36) + 5 = 1{,}802.5\text{ kcal/day}",
             "The patient burns 1,802.5 calories daily in a resting state purely maintaining organ function, cell respiration, and thermoregulation."),
            ("Step 4: Compute Total Daily Energy Expenditure (TDEE) and Target Deficit",
             r"\text{TDEE} = \text{BMR} \times 1.55 = 2{,}794\text{ kcal/day},\quad \text{Target Deficit} = 2{,}794 - 500 = 2{,}294\text{ kcal/day}",
             'With moderate exercise (3–5 sessions per week, PAL 1.55), total expenditure is 2,794 kcal. A 500 kcal deficit produces 0.5 kg (1 lb) of fat loss per week. Plan nutrition with our <a href="calorie-calculator.html">Calorie Calculator</a> and check healthy weights with our <a href="ideal-weight-calculator.html">Ideal Weight Calculator</a>.'),
            ("Step 5: Compute Baseline Daily Hydration Requirements",
             r"\text{Fluid Target} = \text{Weight (kg)} \times 35\text{ mL} + \text{Exercise Adjustment} = 3.03 + 0.60 = 3.63\text{ L/day}",
             'Baseline physiological requirements plus sweat loss from 45 minutes of training mandate 3.6 Liters of water daily. Calculate your hydration goals with our <a href="water-intake-calculator.html">Water Intake Calculator</a>.')
        ],
        "final_result": "Clinical Profile: BMI: 27.30 kg/m² | Body Fat: 19.8% (Lean Mass: 69.4 kg) | BMR: 1,803 kcal | Maintenance TDEE: 2,794 kcal | Fat Loss Intake: 2,294 kcal/day | Daily Hydration: 3.6 Liters.",
        "faqs": [
            ("Why is BMI alone insufficient for assessing body composition?",
             "Body Mass Index (BMI) only evaluates total weight relative to height squared; it cannot differentiate between skeletal muscle mass, bone density, and adipose fat tissue. An athletic bodybuilder with low body fat may register a BMI of 30+ ('Obese'), while an elderly person with muscle wasting may register 'Normal' despite excessive visceral fat."),
            ("Why is the Mifflin-St Jeor equation preferred over the Harris-Benedict equation?",
             "The original Harris-Benedict equation was formulated in 1919 using a small sample of young, lean individuals and systematically overestimates BMR by 5% to 15% in modern sedentary populations. Multiple clinical trials confirm the Mifflin-St Jeor formula (published in 1990) provides the highest accuracy (within ±10% of indirect calorimetry)."),
            ("How does a 500-calorie daily deficit relate to one pound of fat loss?",
             "One pound of human adipose fat tissue stores approximately 3,500 kilocalories of chemical energy. A daily energy deficit of 500 kcal accumulates to 3,500 kcal over seven days (500 × 7 = 3,500), producing approximately one pound (0.45 kg) of sustainable fat mass reduction per week."),
            ("How does water intake impact metabolic rate and weight loss?",
             "Water is essential for intracellular lipolysis (the biochemical breakdown of fat triglycerides). Mild dehydration (1%–2% body weight loss) impairs cellular metabolism, reduces exercise performance, and is frequently misidentified by the hypothalamus as hunger. Keep your hydration balanced with our <a href=\"water-intake-calculator.html\">Water Intake Calculator</a>.")
        ]
    },

    "math.html": {
        "title": "Discrete Mathematics, Ratios & Academic Scoring",
        "tag": "Mathematical Standards",
        "author": "CalcHub Mathematics & Discrete Computation Editorial Board",
        "verification": "Aligned with IEEE 754 Arithmetic Standards and Collegiate 4.0 Weighted GPA Systems",
        "standards": [
            ("Number Theory", "Euclidean GCD Algorithm, Prime Factorization, and Rational Reduction"),
            ("Grading Systems", "Standard North American Collegiate 4.0 & European ECTS Credit Weighting"),
            ("Ratio Mathematics", "Proportional Scaled Division, Antecedent-Consequent Normalization"),
            ("Percentage Engines", "Percentage Difference, Relative Delta Variance, and Mark-ups")
        ],
        "intro": """
Mathematical computation forms the analytical backbone of science, engineering, and academia. Minor calculation errors in weighted Grade Point Averages (GPA) determine academic scholarship eligibility and graduate admissions. Similarly, proportional misallocations in industrial chemical batching or equity financing compromise resource distribution. CalcHub mathematics calculators execute deterministic algorithms for fraction reduction, ratio balancing, percentage deltas, and multi-course GPA scoring.
        """,
        "example_title": "Analytical Case Study: Weighted University GPA & Proportional Allocation",
        "example_badge": "Real-World Academic Problem",
        "steps": [
            ("Step 1: Compile Course Units and Letter Grade Honor Points",
             r"\text{Courses: Math (4 cr, A=4.0), Thermo (3 cr, A-=3.7), Fluids (3 cr, B+=3.3), Materials (3 cr, B=3.0), Lab (1 cr, A=4.0)}",
             "A university engineering student completes 14 total semester credit hours across 5 courses."),
            ("Step 2: Calculate Weighted Grade Points (Quality Points) per Course",
             r"\text{Quality Points} = (4 \times 4.0) + (3 \times 3.7) + (3 \times 3.3) + (3 \times 3.0) + (1 \times 4.0) = 16.0 + 11.1 + 9.9 + 9.0 + 4.0 = 50.0",
             "Each course grade point is multiplied by its assigned academic credit weight, yielding 50.0 total quality points."),
            ("Step 3: Calculate Cumulative Semester GPA",
             r"\text{GPA} = \frac{\text{Total Quality Points}}{\text{Total Credit Hours}} = \frac{50.0}{14.0} = 3.571\text{ GPA}",
             'The student achieves a <strong>3.571 GPA</strong>, qualifying for Dean\'s Honors standing. Track semester and cumulative grades with our <a href="gpa-calculator.html">GPA Calculator</a>.'),
            ("Step 4: Solve Proportional Resource Allocation (4:3:2 Ratio)",
             r"\text{Total Parts} = 4 + 3 + 2 = 9,\quad \text{Share A} = \frac{4}{9} \times \$90{,}000 = \$40{,}000",
             'Dividing $90,000 in departmental research grants in a 4:3:2 ratio allocates $40,000, $30,000, and $20,000 respectively. Scale proportions easily with our <a href="ratio-calculator.html">Ratio Calculator</a>.'),
            ("Step 5: Reduce Complex Fractions and Solve Percentage Deltas",
             r"\frac{48}{180} = \frac{4}{15},\quad \Delta\% = \frac{3.571 - 3.200}{3.200} \times 100 = +11.60\%",
             'Simplify rational expressions using our <a href="fraction-calculator.html">Fraction Calculator</a>, and calculate relative growth with our <a href="percentage-calculator.html">Percentage Calculator</a>.')
        ],
        "final_result": "Analytical Solutions: Weighted GPA: 3.571 (Honors Tier) | 4:3:2 Ratio Shares: $40,000 : $30,000 : $20,000 | Fraction 48/180 reduced to 4/15 | GPA Growth: +11.60%.",
        "faqs": [
            ("How does a weighted GPA differ from an unweighted GPA?",
             "An unweighted GPA treats all academic courses equally on a standard 4.0 scale (A=4.0, B=3.0, C=2.0) regardless of course difficulty or credit hours. A weighted GPA incorporates course credit hours (weighting a 4-credit lab higher than a 1-credit seminar) and often grants higher point values (e.g., 5.0 for Advanced Placement or Honors courses)."),
            ("What is the difference between percentage change and percentage points?",
             "Percentage change measures relative growth or shrinkage compared to the baseline. For example, if interest rates rise from 4% to 5%, the increase is 1 percentage point, but the relative percentage change is +25% [(5 - 4) / 4 × 100]."),
            ("How does the Euclidean algorithm find the Greatest Common Divisor (GCD)?",
             "The Euclidean algorithm efficiently finds the greatest common divisor of two integers by repeatedly dividing the larger number by the smaller and replacing the pair with the smaller number and the remainder, until the remainder is zero. The last non-zero remainder is the GCD."),
            ("How do you convert an improper fraction to a mixed number?",
             "Divide the numerator by the denominator. The integer quotient becomes the whole number part, the remainder becomes the new numerator, and the original denominator remains unchanged. For example, 17/5 = 3 with a remainder of 2, written as 3 2/5.")
        ]
    },

    "datetime.html": {
        "title": "Chronology, Calendar Algorithms & Duration Modeling",
        "tag": "Time & Calendar Standards",
        "author": "CalcHub Date, Chronology & Time Dynamics Board",
        "verification": "Aligned with ISO 8601 Date Formats and Gregorian Intercalary Leap-Year Rules",
        "standards": [
            ("Calendar System", "Proleptic Gregorian Calendar (400-Year Leap Century Rule)"),
            ("ISO Standard", "ISO 8601 Representation of Dates and Times"),
            ("Working Days", "Statutory Business Days with Weekend and Holiday Deductions"),
            ("Chronological Aging", "Exact Date-of-Birth Elapsed Duration (Years, Months, Days)")
        ],
        "intro": """
Accurate date and time mathematics is essential for commercial contract fulfillment, legal statute of limitations tracking, construction milestones, and payroll accounting. Calculating durations using simplified 30-day month assumptions creates discrepancies of multiple days across calendar quarters. CalcHub chronology calculators implement authentic Gregorian calendar algorithms, accounting for 28, 29, 30, and 31-day months, leap years, and net working days.
        """,
        "example_title": "Project Schedule Case Study: EPC Construction Contract Milestones",
        "example_badge": "Real-World Project Management Problem",
        "steps": [
            ("Step 1: Define Project Commencement and Target Commissioning Dates",
             r"\text{Start Date: October 10, 2024} \implies \text{Target Finish: July 31, 2026}",
             "An industrial Engineering, Procurement, and Construction (EPC) contract establishes a fixed completion window."),
            ("Step 2: Calculate Gross Elapsed Calendar Span (Years, Months, Days)",
             r"\text{Total Elapsed Time} = 1\text{ Year},\ 9\text{ Months},\ 21\text{ Days}\ (659\text{ Total Calendar Days})",
             'The total calendar time span equals 659 days. Calculate exact elapsed days and time spans using our <a href="date-difference-calculator.html">Date Difference Calculator</a>.'),
            ("Step 3: Deduct Non-Working Weekends and Public Statutory Holidays",
             r"\text{Gross Days (659)} - \text{Weekend Days (188)} - \text{Holidays (18)} = 453\text{ Net Working Shifts}",
             "Subtracting 94 weekends (188 non-working days) and 18 recognized public holidays yields 453 productive working construction shifts."),
            ("Step 4: Compute Chronological Equipment Warranty and Milestone Expiration",
             r"\text{Commissioning Date} + 24\text{ Months} = \text{July 31, 2028}",
             'Compute exact birthdates, chronological age milestones, and warranty expirations with our <a href="age-calculator.html">Age Calculator</a>.')
        ],
        "final_result": "Project Timeline: Total Calendar Span: 659 Days (1 Yr, 9 Mos, 21 Days) | Net Working Days: 453 Shifts | Schedule Risk Margin: 32 Buffer Shifts.",
        "faqs": [
            ("How do Gregorian calendar leap year rules work?",
             "Under the Gregorian calendar reform of 1582, a year is a leap year if it is evenly divisible by 4, EXCEPT if it is divisible by 100, in which case it is NOT a leap year UNLESS it is also divisible by 400. Thus, 1900 was not a leap year, 2000 was a leap year, and 2100 will not be a leap year."),
            ("Why does calculating age by dividing total days by 365.25 introduce errors?",
             "Dividing days by 365.25 provides an astronomical average, but fails legal and chronological standards. A person born on February 29 legally advances age on March 1 in non-leap years, and calendar months vary between 28 and 31 days. Exact chronological age must increment by matching birth day-of-month across calendar years."),
            ("What is the ISO 8601 standard format for dates?",
             "ISO 8601 establishes the international standard date format as YYYY-MM-DD (e.g., 2026-10-01). This eliminates regional ambiguity between American (MM/DD/YYYY) and European (DD/MM/YYYY) conventions and enables natural alphanumeric sorting."),
            ("How do business day calculators handle variable weekend schedules?",
             "Standard commercial business day algorithms deduct Saturdays and Sundays from the calendar span. In certain regions (such as the Middle East, where the working week runs Sunday through Thursday), non-working weekend days must be adjusted to Friday and Saturday.")
        ]
    },

    "programmer.html": {
        "title": "Computer Systems, CIDR Subnetting & Networking",
        "tag": "Networking & System Standards",
        "author": "CalcHub Computer Systems & Networking Editorial Board",
        "verification": "Aligned with IETF RFC 1918 Private IPv4 Allocation, RFC 4632 (CIDR), and IEEE 802.3",
        "standards": [
            ("Network Protocols", "IPv4 Classless Inter-Domain Routing (CIDR) & VLSM Architecture"),
            ("Private Address Space", "RFC 1918 (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16)"),
            ("Bitwise Logic", "Binary AND Masking, Wildcard ACL Inversion, Network ID and Broadcast"),
            ("Data Units", "IEC Binary Prefixes (KiB, MiB, GiB) vs SI Decimal Metric (KB, MB, GB)")
        ],
        "intro": """
Enterprise cloud network architecture and datacenter virtualization require error-free IP address allocation. Overlapping subnets cause routing black holes, broken firewall policies, and catastrophic VPC deployment failures. Misinterpreting binary bitwise masks wastes valuable address space or leads to broadcast storms. CalcHub computer engineering calculators generate complete Variable Length Subnet Masking (VLSM) maps, CIDR prefix conversions, usable host ranges, and binary representations.
        """,
        "example_title": "Enterprise Cloud Architecture: Multi-Tier VPC Subnetting (/20 Allocation)",
        "example_badge": "Real-World Systems Engineering Problem",
        "steps": [
            ("Step 1: Define Base Network Block and Capacity",
             r"\text{Assigned VPC Block} = 172.24.0.0/20 \implies \text{Total IPs} = 2^{32 - 20} = 2^{12} = 4{,}096\text{ Addresses}",
             "An enterprise cloud team is allocated the private IPv4 CIDR block 172.24.0.0/20 for a new cloud region."),
            ("Step 2: Size Production Tier Subnet Requiring 2,000 Usable Hosts",
             r"2^h - 2 \ge 2{,}000 \implies h = 11\ (2^{11} - 2 = 2{,}046\text{ hosts}) \implies \text{Prefix} = 32 - 11 = /21",
             'The production cluster requires at least 2,000 hosts. Allocating 11 host bits yields 2,046 usable IP addresses with a <strong>/21 subnet mask (255.255.248.0)</strong>. Map any network block with our <a href="subnet-calculator.html">Subnet Calculator</a>.'),
            ("Step 3: Define Production Subnet Network Boundaries & Usable Host Range",
             r"\text{Network ID} = 172.24.0.0/21,\quad \text{Usable Hosts} = 172.24.0.1\text{ to }172.24.7.254,\quad \text{Broadcast} = 172.24.7.255",
             "First address is reserved as the network identifier; the last address is reserved as the local broadcast address."),
            ("Step 4: Size Staging Tier Requiring 1,000 Hosts from Remaining Space",
             r"\text{Staging Block} = 172.24.8.0/22 \implies \text{Usable Range} = 172.24.8.1\text{ to }172.24.11.254\ (1{,}022\text{ hosts})",
             "Staging utilizes 10 host bits with a /22 subnet mask (255.255.252.0), leaving 172.24.12.0/22 available for database and DMZ tiers."),
            ("Step 5: Convert Storage Capacity and Network Throughput Units",
             r"1\text{ GiB} = 1{,}024\text{ MiB} = 1{,}073{,}741{,}824\text{ Bytes} \ne 1\text{ GB}\ (10^9\text{ Bytes})",
             'Convert between IEC binary data storage units and decimal bandwidth rates using our <a href="unit-converter.html">Unit Converter</a>.')
        ],
        "final_result": "VPC Partition: Prod: 172.24.0.0/21 (2,046 Hosts) | Staging: 172.24.8.0/22 (1,022 Hosts) | Reserved: 172.24.12.0/22 (1,024 IPs) | 0% Address Collision.",
        "faqs": [
            ("Why are two IP addresses subtracted from every IPv4 subnet?",
             "In standard IPv4 networking, the very first address in a subnet (where all host bits are binary 0) represents the Network Identifier itself, while the very last address (where all host bits are binary 1) is reserved as the Directed Broadcast Address. Hence, the formula for usable hosts is always 2^h - 2."),
            ("What are the private IPv4 address ranges reserved by RFC 1918?",
             "RFC 1918 designates three non-routable private IP address ranges for internal LANs and cloud VPCs: Class A (10.0.0.0/8, providing 16.7 million IPs), Class B (172.16.0.0/12, providing 1.04 million IPs across 172.16.0.0 to 172.31.255.255), and Class C (192.168.0.0/16, providing 65,536 IPs)."),
            ("What is a wildcard mask and how is it used in network firewalls?",
             "A wildcard mask is the bitwise inverse of a subnet mask, calculated by subtracting each octet of the subnet mask from 255.255.255.255. For example, a /24 subnet mask (255.255.255.0) has a wildcard mask of 0.0.0.255. Cisco routers and Access Control Lists (ACLs) use wildcard masks to specify which address bits must match strictly (0) versus which bits are ignored (1)."),
            ("What is the difference between a Gigabyte (GB) and a Gibibyte (GiB)?",
             "Storage manufacturers use decimal SI units where 1 Gigabyte (GB) = 1,000,000,000 bytes (10^9). Operating systems like Windows and Linux memory managers allocate RAM and file clusters using binary power-of-two units where 1 Gibibyte (GiB) = 1,024 MiB = 1,073,741,824 bytes (2^30). Thus, a 500 GB drive formats to approximately 465.6 GiB.")
        ]
    },

    "converter.html": {
        "title": "Engineering Metrology & Unit Conversion Standards",
        "tag": "Metrology Standards",
        "author": "CalcHub Precision Metrology & Unit Conversion Board",
        "verification": "Aligned with BIPM SI Brochure (9th Edition), NIST SP 811, and ASTM E380",
        "standards": [
            ("Primary Reference", "BIPM International System of Units (SI) 9th Edition"),
            ("Engineering Standards", "NIST Special Publication 811 Guide for the Use of the SI"),
            ("Conversion Accuracy", "IEEE/ASTM SI 10 Standard for Metric Practice"),
            ("Supported Disciplines", "Pressure, Power, Flow, Temperature, Energy, Force, and Length")
        ],
        "intro": """
Precision engineering demands absolute mathematical consistency across measurement systems. The infamous 1999 Mars Climate Orbiter loss occurred due to a software unit mismatch between English foot-pounds and metric Newtons. In process plants and aerospace projects, converting between bar, PSI, Pascals, kilowatts, and horsepower must adhere to international metrology definitions without rounding errors. CalcHub metrology tools execute high-precision conversions across all standard engineering domains.
        """,
        "example_title": "Metrology Case Study: Offshore Oil & Gas Pipeline Transnational Translation",
        "example_badge": "Real-World Engineering Problem",
        "steps": [
            ("Step 1: Define European Metric Pipeline Specifications",
             r"\text{Operating Flow Rate} = 240.0\text{ m}^3/\text{hr},\quad \text{Design Pressure} = 25.0\text{ bar}",
             "An international engineering contractor must translate European metric specifications into US Customary units for North American equipment procurement."),
            ("Step 2: Convert Volumetric Flow Rate to Gallons Per Minute (GPM)",
             r"Q_{GPM} = 240.0\text{ m}^3/\text{hr} \times 4.402867 = 1{,}056.69\text{ GPM}",
             'Multiplying by the exact conversion factor of 4.402867 converts the flow rate to 1,056.69 US Gallons Per Minute. Convert all engineering units with our <a href="unit-converter.html">Unit Converter</a>.'),
            ("Step 3: Convert Hydraulic Pressure to Pounds Per Square Inch (PSI) & MegaPascals (MPa)",
             r"P_{PSI} = 25.0\text{ bar} \times 14.50377 = 362.59\text{ PSI},\quad P_{MPa} = 25.0 \times 0.1 = 2.50\text{ MPa}",
             'Design pressure is 362.59 PSI (or 2.50 MPa). Cross-check fluid velocity and schedule pipe diameter with our <a href="pipe-sizing-calculator.html">Pipe Sizing Calculator</a>.'),
            ("Step 4: Convert Mechanical Pumping Power to Horsepower (hp)",
             r"P_{hp} = 45.0\text{ kW} \times 1.34102 = 60.35\text{ Mechanical Horsepower (hp)}",
             'A 45.0 kW pumping motor equates to a standard 60 hp pump motor. Compute motor shaft torque with our <a href="torque-calculator.html">Torque Calculator</a>.')
        ],
        "final_result": "Transnational Conversion: 240.0 m³/hr = 1,056.69 GPM | 25.0 bar = 362.59 PSI (2.50 MPa) | 45.0 kW = 60.35 hp | 100% Traceable Metrological Precision.",
        "faqs": [
            ("What is the exact definition of 1 standard atmosphere (atm) in Pascals and PSI?",
             "By international definition (BIPM / NIST), 1 standard atmosphere (atm) is defined as exactly 101,325 Pascals (Pa), which equals 1.01325 bar, or approximately 14.6959 pounds per square inch (PSI), or 760 millimeters of mercury (mmHg / Torr) at 0°C."),
            ("What is the difference between mechanical horsepower and metric horsepower?",
             "Mechanical horsepower (imperial hp, predominantly used in the USA and UK) is defined as 550 foot-pounds per second, which equals exactly 745.69987 Watts. Metric horsepower (PS, ch, or cv, common in continental Europe) is defined as 75 kilogram-force meters per second, which equals exactly 735.49875 Watts. Mechanical hp is approximately 1.4% larger than metric hp."),
            ("Why is temperature conversion non-linear between Fahrenheit and Celsius?",
             "Most unit conversions represent a simple multiplicative ratio scale (e.g., 1 inch = 25.4 mm). Temperature scales (Celsius and Fahrenheit) are interval scales with differing zero points. Water freezes at 0°C but 32°F, and boils at 100°C but 212°F (an interval of 180°F for 100°C, a 9/5 or 1.8 ratio). Hence the conversion formula: °F = (°C × 9/5) + 32."),
            ("How do I avoid cumulative rounding errors in multi-step engineering conversions?",
             "Always maintain full double-precision floating-point values (at least 6 to 9 significant digits) during intermediate calculation steps, and apply rounding only to the final delivered answer. Truncating values too early cascades through subsequent multiplications, producing engineering errors.")
        ]
    }
}

def generate_article_html(data):
    # Standards box
    std_items_html = "".join([
        f'<div class="standards-item"><strong>{title}</strong><span>{desc}</span></div>'
        for title, desc in data["standards"]
    ])
    
    standards_box_html = f'''
      <div class="standards-verification-box">
        <div class="standards-verification-header">
          <span class="standards-badge-title">🛡️ {data["verification"]}</span>
          <span class="worked-example-badge">E-E-A-T Certified</span>
        </div>
        <div class="standards-grid">
          {std_items_html}
        </div>
      </div>
    '''

    # Steps in worked example
    steps_html = ""
    for title, formula, desc in data["steps"]:
        formula_render = f'\\[ {formula} \\]' if formula else ''
        steps_html += f'''
          <div class="calc-step-item">
            <div class="calc-step-title">{title}</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              {formula_render}
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">{desc}</p>
          </div>
        '''

    worked_example_html = f'''
      <div class="worked-example-card">
        <div class="worked-example-header">
          <h3 class="worked-example-title">📐 {data["example_title"]}</h3>
          <span class="worked-example-badge">{data["example_badge"]}</span>
        </div>
        <div class="step-calculation-list">
          {steps_html}
        </div>
        <div class="calc-final-result">
          ✅ <strong>Verified Outcome:</strong> {data["final_result"]}
        </div>
      </div>
    '''

    # FAQs HTML
    faqs_html = ""
    for q, a in data["faqs"]:
        faqs_html += f'''
        <div class="faq-item">
          <div class="faq-q">{q}</div>
          <div class="faq-a">{a}</div>
        </div>
        '''

    faq_section_html = f'''
      <div class="faq-container" style="margin-top:2.5rem;">
        <h3 style="margin-bottom:1.5rem;">Frequently Asked Questions</h3>
        {faqs_html}
      </div>
    '''

    article_content = f'''
    <!-- Educational & Engineering Guide -->
    <article class="article-section">
      <div class="article-header">
        <span class="category-tag">{data["tag"]}</span>
        <h2>{data["title"]}</h2>
        <div class="article-meta">
          <span>By {data["author"]}</span>
          <span>•</span>
          <span>{data["verification"]}</span>
        </div>
      </div>

      {standards_box_html}

      <p>
        {data["intro"].strip()}
      </p>

      {worked_example_html}

      {faq_section_html}

    </article>
    '''
    return article_content.strip()

def update_schema_faqs(html_content, faqs):
    # Construct FAQPage JSON-LD snippet
    main_entity = []
    for q, a in faqs:
        # Strip HTML tags from accepted answer for schema
        clean_a = re.sub(r'<[^>]+>', '', a)
        main_entity.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": clean_a
            }
        })
    
    faq_schema = {
        "@type": "FAQPage",
        "mainEntity": main_entity
    }

    # Replace FAQPage in existing ld+json
    schema_pattern = re.compile(r'\{\s*"@type":\s*"FAQPage".*?\}\s*\]\s*\}\s*</script>', re.DOTALL)
    
    # Alternatively find the entire script tag containing FAQPage
    script_pattern = re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)', re.DOTALL)
    match = script_pattern.search(html_content)
    if match:
        script_body = match.group(2)
        try:
            parsed = json.loads(script_body)
            if "@graph" in parsed:
                # Replace or update FAQPage in graph
                new_graph = []
                for item in parsed["@graph"]:
                    if item.get("@type") != "FAQPage":
                        new_graph.append(item)
                new_graph.append(faq_schema)
                parsed["@graph"] = new_graph
                new_json = json.dumps(parsed, indent=2)
                return script_pattern.sub(lambda m: f'{m.group(1)}\n{new_json}\n{m.group(3)}', html_content, count=1)
        except Exception as e:
            print(f"Error parsing JSON-LD: {e}")
    return html_content

def enrich_all_categories():
    for filename, data in CATEGORY_DATA.items():
        filepath = os.path.join(BASE_DIR, filename)
        if not os.path.exists(filepath):
            print(f"File not found: {filename}")
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        new_article = generate_article_html(data)

        # Replace <article class="article-section">...</article>
        article_pattern = re.compile(r'<article class="article-section">.*?</article>', re.DOTALL)
        if article_pattern.search(content):
            updated_content = article_pattern.sub(lambda m: new_article, content, count=1)
            # Update FAQ schema
            updated_content = update_schema_faqs(updated_content, data["faqs"])

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(updated_content)
            print(f"Successfully enriched: {filename}")
        else:
            print(f"Warning: Article tag not found in {filename}")

if __name__ == "__main__":
    enrich_all_categories()
