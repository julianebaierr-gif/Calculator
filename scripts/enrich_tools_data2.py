import os
import re
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load data from enrich_tools_data.py if present
from enrich_tools_data import TOOLS_DATA

# Additional tools definitions
ADDITIONAL_DATA = {
    "resistor-color-code-calculator.html": {
        "verification": "EIA-RS-279 / IEC 60062 Resistor Marking Standards",
        "standards": [
            ("Standard Code", "EIA-RS-279 & IEC 60062 Color Coding Standards"),
            ("Band Configurations", "4-Band (General) and 5-Band (Precision ±1%, ±0.5%)"),
            ("Multiplier Range", "10⁻² (Silver) up to 10⁹ (White)"),
            ("Verification Method", "Cross-checked against Vishay & Bourns standard resistor charts")
        ],
        "example_title": "Electronics Prototyping: 5-Band Precision Bias Resistor Decoding",
        "example_badge": "Real-World Engineering Problem",
        "steps": [
            ("Step 1: Identify Band Sequence for 5-Band Resistor",
             r"\text{Bands: Brown (1), Green (5), Black (0), Orange (10³), Brown (±1%)}",
             "A high-precision analog operational amplifier circuit requires decoding a 5-band metal film axial resistor."),
            ("Step 2: Read Significant Digits and Multiplier",
             r"\text{Digits: 1, 5, 0} \implies 150 \times 10^3\ \Omega = 150{,}000\ \Omega\ (150\text{ k}\Omega)",
             "Combining significant digits yields 150. Multiplying by 10³ gives 150,000 Ohms (150 kΩ)."),
            ("Step 3: Calculate Tolerance Range Boundaries (±1%)",
             r"R_{min} = 150\text{ k}\Omega - 1\% = 148.5\text{ k}\Omega,\quad R_{max} = 150\text{ k}\Omega + 1\% = 151.5\text{ k}\Omega",
             "The manufactured resistor is certified to measure strictly between 148.5 kΩ and 151.5 kΩ."),
            ("Step 4: Check Operational Power Rating and Thermal Dissipation",
             r"P = \frac{V^2}{R} = \frac{15^2}{150{,}000} = 0.0015\text{ W}\ (1.5\text{ mW}) \ll 0.25\text{ W}",
             'With 15V across the resistor, heat dissipation is 1.5 mW, well below a standard 1/4-Watt resistor limit. Compute circuit voltages and currents with our <a href="ohms-law-calculator.html">Ohm\'s Law Calculator</a> or visit our <a href="engineering.html">Electrical Engineering Hub</a>.')
        ],
        "final_result": "Decoded Value: 150 kΩ ±1% | Certified Range: 148.5 kΩ to 151.5 kΩ | Safe for 1/4W Operation.",
        "faqs": [
            ("How do I tell which end of a resistor to read first?",
             "Look for a wider gap: the tolerance band (gold, silver, or brown) is separated by a noticeably larger spacing from the other bands. Additionally, gold and silver bands rarely appear as first significant digits, indicating they mark the tail end."),
            ("What is the difference between 4-band and 5-band resistors?",
             "A 4-band resistor has two significant digits, a multiplier, and a tolerance band (typically ±5% or ±10%). A 5-band resistor provides three significant digits, a multiplier, and a tighter tolerance band (±1% or ±0.5%), offering superior accuracy for precision electronics."),
            ("What does the 6th band represent on a 6-band resistor?",
             "The sixth band designates the Temperature Coefficient of Resistance (TCR), expressed in parts per million per Kelvin (ppm/K). It indicates how much the resistance drifts as operating temperature changes (e.g., brown = 100 ppm/K, red = 50 ppm/K)."),
            ("Why are resistor values standardized into E-series (E12, E24, E96)?",
             "Standard resistors follow logarithmic E-series (IEC 60063). In the E12 series (±10% tolerance), there are 12 values per decade (10, 12, 15, 18, 22...) engineered such that each value's tolerance band overlaps with the next, eliminating manufacturing value gaps.")
        ]
    },

    "solar-panel-sizing-calculator.html": {
        "verification": "IEC 61215 Terrestrial PV Modules & NEC NFPA 70 Article 690",
        "standards": [
            ("PV Module Standard", "IEC 61215 & IEC 61730 Photovoltaic Safety Qualification"),
            ("System Losses", "15%–20% Balance of System (BoS) Losses (Inverter, Wiring, Soiling)"),
            ("Irradiance Source", "NREL PVWatts & NASA Surface Meteorology Solar Insolation Data"),
            ("DC Array Design", "NEC 690.8 Circuit Sizing and Maximum System Voltage Limits")
        ],
        "example_title": "Field Case Study: 30 kWh/Day Residential Off-Grid Solar Array Sizing",
        "example_badge": "Real-World Renewable Energy Problem",
        "steps": [
            ("Step 1: Quantify Daily Energy Target with System Inefficiency Compensation",
             r"E_{target} = \frac{E_{load}}{\eta_{sys}} = \frac{30\text{ kWh}}{0.80} = 37.5\text{ kWh/day}",
             "To reliably supply 30 kWh of daily household consumption with 20% system losses, the PV array must generate 37.5 kWh daily."),
            ("Step 2: Size Solar Array Peak Wattage (Wp) Based on Peak Sun Hours (PSH)",
             r"P_{pv} = \frac{E_{target}}{\text{PSH}} = \frac{37{,}500\text{ Wh}}{4.8\text{ PSH}} = 7{,}812.5\text{ W} \approx 8.0\text{ kWp}",
             "With 4.8 Peak Sun Hours of winter solar insolation, the required solar peak capacity is approximately 8.0 kWp."),
            ("Step 3: Determine Module Count for 550W Tier-1 Panels",
             r"\text{Modules} = \lceil \frac{7{,}812.5\text{ W}}{550\text{ W}} \rceil = 15\text{ Panels} \implies 8{,}250\text{ W total}",
             'Fifteen 550W mono-PERC modules deliver 8,250 Watts peak (8.25 kWp). Size your battery storage with our <a href="solar-battery-bank-calculator.html">Solar Battery Bank Calculator</a>.'),
            ("Step 4: Size Matching Off-Grid Inverter and DC Cabling",
             r"P_{inv} \ge 8.0\text{ kW},\quad I_{dc} = \frac{8{,}250\text{ W}}{48\text{ V}} = 171.9\text{ A}",
             'Select a matching inverter with our <a href="solar-inverter-sizing-calculator.html">Solar Inverter Sizing Calculator</a> and verify DC battery cable ampacity using our <a href="cable-sizing-calculator.html">Cable Sizing Calculator</a> or browse our <a href="solar-energy.html">Solar Energy Hub</a>.')
        ],
        "final_result": "Engineered System: 8.25 kWp Solar PV Array (15 × 550W Panels) | Daily Generation: 39.6 kWh | Fully Offsets 30 kWh Daily Load.",
        "faqs": [
            ("What are Peak Sun Hours (PSH) and how are they measured?",
             "Peak Sun Hours (PSH) represent the equivalent number of hours in a day during which solar irradiance equals 1,000 W/m² (Standard Test Conditions). A location with 12 hours of sunlight might receive only 4.5 to 5.5 PSH due to low morning and evening sun angles."),
            ("How do hot summer temperatures impact solar panel power output?",
             "Solar panels lose efficiency as cell temperature rises above 25°C. Silicon panels have a temperature coefficient of Pmax of approximately -0.35% to -0.40% per °C. On a 40°C day with cell temperatures reaching 65°C, output drops by roughly 14% to 16%."),
            ("What is the difference between Monocrystalline and Polycrystalline panels?",
             "Monocrystalline panels are sliced from single-crystal silicon ingots, delivering higher efficiency (20%–22%), superior low-light performance, and sleek black aesthetics. Polycrystalline panels are made from melted silicon fragments, with lower efficiency (15%–17%) and a speckled blue appearance."),
            ("What tilt angle is optimal for fixed solar panels?",
             "A common rule of thumb for fixed year-round solar panels is to set the tilt angle equal to the local latitude, facing true South (Northern Hemisphere) or true North (Southern Hemisphere). For winter-optimized off-grid systems, tilt is increased by 10° to 15° to capture low winter sun.")
        ]
    },

    "solar-battery-bank-calculator.html": {
        "verification": "IEEE Standard 1013 & IEEE 485 Battery Sizing Standards",
        "standards": [
            ("Sizing Guideline", "IEEE 1013 Recommended Practice for Sizing Lead-Acid/Lithium Batteries"),
            ("Chemistry Parameters", "LiFePO4 (80%–90% DoD, 95% eff) / AGM Lead-Acid (50% DoD, 80% eff)"),
            ("Autonomy Standard", "1 to 3 Days Reserve Autonomy for Meteorological Variability"),
            ("System Voltages", "12V, 24V, and 48V DC Low-Voltage Battery Busses")
        ],
        "example_title": "Field Case Study: Off-Grid Cabin 48V LiFePO4 Battery Bank Design",
        "example_badge": "Real-World Energy Storage Problem",
        "steps": [
            ("Step 1: Quantify Daily Energy Consumption",
             r"E_{daily} = 12\text{ kWh/day}\ (12{,}000\text{ Wh/day})",
             "An off-grid remote cabin requires 12 kWh of electricity daily for lighting, refrigeration, water pumping, and communications."),
            ("Step 2: Factor Days of Autonomy for Overcast Reserves (2 Days)",
             r"E_{reserve} = 12{,}000\text{ Wh} \times 2\text{ days} = 24{,}000\text{ Wh}",
             "To ensure uninterrupted power through two consecutive sunless overcast days, reserve capacity must store 24 kWh."),
            ("Step 3: Apply Usable Depth of Discharge (DoD) & Battery Coulombic Efficiency",
             r"E_{nominal} = \frac{24{,}000\text{ Wh}}{0.80\text{ DoD} \times 0.95\ \eta} = 31{,}578.9\text{ Wh}\ (31.58\text{ kWh})",
             "Lithium Iron Phosphate (LiFePO4) supports 80% safe Depth of Discharge with 95% round-trip efficiency, requiring 31.58 kWh nominal storage."),
            ("Step 4: Compute Battery Bank Capacity in Amp-Hours (Ah) at 48V DC",
             r"C_{Ah} = \frac{31{,}579\text{ Wh}}{48\text{ V}} = 657.9\text{ Ah} \implies 700\text{ Ah bank}",
             'At 48V DC bus voltage, the bank requires <strong>658 Ah (approx. seven 48V 100Ah server rack modules)</strong>. Size your PV generation with our <a href="solar-panel-sizing-calculator.html">Solar Panel Sizing Calculator</a> and verify your inverter with our <a href="solar-inverter-sizing-calculator.html">Solar Inverter Sizing Calculator</a>.')
        ],
        "final_result": "Storage Specification: 48V DC LiFePO4 Bank | 658 Ah (31.6 kWh Nominal Storage) | 2 Full Days Autonomy | 6,000+ Cycle Lifespan.",
        "faqs": [
            ("Why is 48V DC preferred over 12V or 24V for solar battery banks?",
             "Higher system voltage dramatically reduces current (I = P/V). A 4,800W load at 12V draws 400 Amperes, requiring massive busbars and causing severe I²R voltage drop losses. At 48V, the same load draws only 100 Amperes, allowing much smaller cables and improving efficiency."),
            ("How does Depth of Discharge (DoD) dictate battery longevity?",
             "Discharging lead-acid batteries past 50% DoD degrades lead plates through severe sulfation, shortening life to 300–500 cycles. LiFePO4 cells tolerate 80%–90% DoD for 4,000 to 6,000 cycles, providing over 10 years of daily off-grid cycling."),
            ("What is battery bank autonomy?",
             "Autonomy is the number of days a battery bank can supply full facility electrical loads without any charging input from solar panels, wind turbines, or backup generators."),
            ("Can you mix old and new batteries in the same bank?",
             "Never mix old and new batteries, nor different chemistries, capacities, or brands in the same bank. Older batteries have higher internal resistance, causing them to draw down new batteries and triggering premature bank failure.")
        ]
    },

    "solar-inverter-sizing-calculator.html": {
        "verification": "UL 1741 & IEEE 1547 Grid Interconnection & Off-Grid Standards",
        "standards": [
            ("Safety Standards", "UL 1741 Standard for Inverters and Interconnection System Equipment"),
            ("Waveform Type", "Pure Sine Wave (<3% Total Harmonic Distortion - THD)"),
            ("Surge Capacity", "200% to 300% Inrush Factor for Inductive Compressor & Pump Motors"),
            ("DC Input Windows", "MPPT Tracking Voltage Range and Maximum Open-Circuit Voltage")
        ],
        "example_title": "Field Case Study: Sizing a Commercial Off-Grid Workshop Inverter",
        "example_badge": "Real-World Engineering Problem",
        "steps": [
            ("Step 1: Calculate Total Simultaneous Continuous Running Load",
             r"P_{cont} = 1{,}200\text{W (lighting)} + 1{,}500\text{W (tools)} + 2{,}200\text{W (HVAC)} = 4{,}900\text{ Watts}",
             "A commercial workshop operates simultaneous lighting, power tools, and air conditioning totaling 4.9 kW continuous draw."),
            ("Step 2: Apply Continuous Operational Safety Margin (25%)",
             r"P_{design} = 4{,}900 \times 1.25 = 6{,}125\text{ Watts}\ (6.13\text{ kW})",
             "Applying a 25% continuous duty headroom margin mandates an inverter continuous rating of at least 6.13 kW."),
            ("Step 3: Calculate Motor Startup Inductive Surge Inrush",
             r"P_{surge} = 2{,}200\text{W (HVAC compressor)} \times 3.0 = 6{,}600\text{W Surge} \implies \text{Total Surge} = 9{,}300\text{ W}",
             "Compressor startup inrush demands 300% starting current for 3 seconds, requiring a 9.3 kW instantaneous surge capacity."),
            ("Step 4: Select Matching Inverter Rating",
             r"\text{Selected Inverter} = 8.0\text{ kW Continuous} / 16.0\text{ kW Surge Pure Sine Wave Inverter}",
             'An 8.0 kW pure sine wave inverter easily handles 6.13 kW continuous and provides up to 16 kW peak surge. Pair with our <a href="solar-battery-bank-calculator.html">Solar Battery Bank Calculator</a> and <a href="solar-panel-sizing-calculator.html">Solar Panel Sizing Calculator</a>.')
        ],
        "final_result": "Inverter Sizing: 8.0 kW Continuous Output | 16.0 kW Peak Motor Surge | Pure Sine Wave (<3% THD) | 100% Reliable Inductive Starts.",
        "faqs": [
            ("What is the difference between Pure Sine Wave and Modified Sine Wave inverters?",
             "Pure Sine Wave inverters produce smooth, clean alternating current identical to utility grid power, essential for motors, compressors, medical gear, and sensitive electronics. Modified Sine Wave inverters produce blocky, stepped square waves that cause motor hum, excessive heat, and can destroy digital electronics."),
            ("Why must inverters be oversized for motor and compressor loads?",
             "Inductive motors (air conditioners, refrigerators, well pumps, power tools) require 2 to 4 times their rated running wattage for 2–3 seconds to break static rotor lock. If an inverter lacks sufficient surge capacity, its overcurrent protection will trip instantly upon motor startup."),
            ("What is inverter conversion efficiency?",
             "Modern high-frequency inverters operate at 93% to 97% peak conversion efficiency. The remaining 3% to 7% is lost as thermal heat dissipation, requiring adequate ventilation in the equipment room."),
            ("How do I size an MPPT charge controller for an inverter system?",
             "The MPPT controller must handle the total PV array wattage divided by battery voltage (e.g., 4,000W / 48V = 83.3A, requiring a 100A MPPT). Additionally, the maximum array open-circuit voltage (Voc) at the coldest expected winter temperature must not exceed the controller's DC input voltage ceiling.")
        ]
    },

    "ev-charging-time-calculator.html": {
        "verification": "SAE J1772 & IEC 62196 Electric Vehicle Conductive Charging Standards",
        "standards": [
            ("Charging Levels", "Level 1 (120V AC, 1.4–1.9 kW) | Level 2 (240V AC, 7.2–19.2 kW) | DC Fast (50–350 kW)"),
            ("Battery Chemistry", "Lithium-Ion / LFP Packs with BMS Thermal Tapering above 80% SoC"),
            ("Charging Efficiency", "85%–90% AC-to-DC Onboard Inverter Conversion Efficiency"),
            ("Applicable Standard", "SAE J1772 / CCS Combo / NACS (Tesla) / IEC 61851")
        ],
        "example_title": "Field Case Study: Sizing Home Level 2 Charging for 77 kWh EV",
        "example_badge": "Real-World Automotive Engineering Problem",
        "steps": [
            ("Step 1: Determine Usable Battery Energy to Replenish (20% to 80% SoC)",
             r"\Delta E = 77\text{ kWh} \times (0.80 - 0.20) = 46.2\text{ kWh}",
             "A driver charges an electric vehicle with a 77 kWh usable battery pack from 20% to 80% State of Charge (SoC)."),
            ("Step 2: Factor AC-to-DC Onboard Charger Thermal Efficiency (88%)",
             r"E_{required} = \frac{46.2\text{ kWh}}{0.88} = 52.5\text{ kWh}",
             "Onboard charging electronics, coolant pumps, and battery thermal management incur a 12% energy loss, requiring 52.5 kWh from the wall."),
            ("Step 3: Calculate Home Level 2 Charger Continuous Power Output",
             r"P_{chg} = 240\text{ V} \times 40\text{ A} \times 0.80\text{ (continuous)} = 7.68\text{ kW}",
             "A 50A breaker supplies a 40A continuous charging station (80% continuous load rule), delivering 7.68 kW."),
            ("Step 4: Compute Total Charging Duration",
             r"t = \frac{E_{required}}{P_{chg}} = \frac{52.5\text{ kWh}}{7.68\text{ kW}} = 6.84\text{ Hours}\ (6\text{h } 50\text{m})",
             'Charging from 20% to 80% takes 6 hours and 50 minutes overnight. Size branch circuit wiring for this charger with our <a href="cable-sizing-calculator.html">Cable Sizing Calculator</a> and explore our <a href="solar-energy.html">Solar Energy Hub</a>.')
        ],
        "final_result": "Charging Profile: 46.2 kWh Delivered | 7.68 kW Delivery Rate | Charge Time: 6 Hours 50 Minutes | Ready by Morning Commute.",
        "faqs": [
            ("Why does DC Fast Charging slow down dramatically above 80% State of Charge?",
             "Lithium-ion batteries cannot absorb massive current at high states of charge without causing lithium plating on the anode, which destroys battery health and poses fire risks. To protect cell life, the vehicle's Battery Management System (BMS) tapers charging speed from 150+ kW down to 20–30 kW once the battery reaches 80%."),
            ("What is the continuous load rule for EV chargers under NEC 625?",
             "Under National Electrical Code (NEC) Article 625, EV charging is defined as a continuous load. Circuit breakers and conductors must be sized at 125% of the charger's rated output. For a 48A charger, you must install a 60A breaker (48 × 1.25 = 60)."),
            ("How much energy is lost during EV charging?",
             "AC charging experiences roughly 10% to 15% energy loss due to AC-to-DC rectification in the vehicle's onboard charger, battery cooling fans, and cell resistance. DC Fast charging experiences roughly 5% to 10% loss."),
            ("Can you charge an EV from a home solar system?",
             "Yes. An average EV traveling 30 miles daily consumes about 10 kWh. A typical 3 kW to 5 kW home solar array generates enough surplus electricity during daytime hours to cover standard daily commuting needs.")
        ]
    },

    "cooling-load-calculator.html": {
        "verification": "ASHRAE Standard 183 & Standard 90.1 Energy Efficient HVAC Design",
        "standards": [
            ("Thermodynamic Code", "ASHRAE Standard 183 Peak Cooling & Heating Load Calculations"),
            ("Thermal Envelope", "ASHRAE 90.1 Maximum U-Factors & Solar Heat Gain Coefficients (SHGC)"),
            ("Metabolic Heat", "ASHRAE Fundamentals Table 1 Sensible & Latent Occupant Gains"),
            ("Units Enforced", "Tons of Refrigeration (TR), BTU/hr, and Kilowatts (kW)")
        ],
        "example_title": "Field Case Study: Commercial Conference Room HVAC Thermal Load",
        "example_badge": "Real-World Mechanical Engineering Problem",
        "steps": [
            ("Step 1: Calculate Floor Area Conduction Base Load",
             r"q_{envelope} = 50\text{ m}^2 \times 300\text{ BTU/hr/m}^2 = 15{,}000\text{ BTU/hr}",
             "A 50 m² executive conference room with exterior insulated walls requires 15,000 BTU/hr baseline sensible envelope cooling."),
            ("Step 2: Add Occupant Sensible & Latent Metabolic Heat (15 People)",
             r"q_{people} = 15 \times 400\text{ BTU/hr/person} = 6{,}000\text{ BTU/hr}",
             "Fifteen meeting participants release 6,000 BTU/hr of combined sensible body heat and latent moisture respiration."),
            ("Step 3: Add Window Solar Radiation & AV Electronics Heat Release",
             r"q_{internal} = 8\text{ m}^2 \times 800\text{ BTU/hr} + 1{,}200\text{W} \times 3.412 = 6{,}400 + 4{,}094 = 10{,}494\text{ BTU/hr}",
             "West-facing glass and audiovisual conference displays release an additional 10,494 BTU/hr."),
            ("Step 4: Compute Total Required Cooling Capacity in Tons of Refrigeration (TR)",
             r"q_{total} = 15{,}000 + 6{,}000 + 10{,}494 = 31{,}494\text{ BTU/hr} \implies \text{TR} = \frac{31{,}494}{12{,}000} = 2.62\text{ TR}",
             'Total heat gain is 31,494 BTU/hr (2.62 TR). A <strong>3.0 Ton commercial inverter ducted unit</strong> provides optimal comfort and dehumidification. Size chilled water piping for this system with our <a href="pipe-sizing-calculator.html">Pipe Sizing Calculator</a> and explore our <a href="mechanical.html">Mechanical Engineering Hub</a>.')
        ],
        "final_result": "Engineered HVAC Load: 31,500 BTU/hr (9.23 kW) | Recommended Unit: 3.0 Tons of Refrigeration (TR) | Balanced Sensible-Latent Control.",
        "faqs": [
            ("What does 1 Ton of Refrigeration (TR) mean?",
             "One Ton of Refrigeration (1 TR) is the rate of heat extraction required to freeze 2,000 lbs (one short ton) of pure water at 0°C into ice in 24 hours. In modern engineering units, 1 TR = 12,000 BTU/hr = 3.51685 Kilowatts (kW)."),
            ("What happens if an air conditioning system is oversized?",
             "An oversized AC cools the room air temperature too rapidly, causing the thermostat to shut off before the evaporator coil has had time to condense and extract airborne humidity. The result is a cold, clammy, humid indoor environment prone to mold growth, alongside frequent compressor short-cycling that inflates electric bills."),
            ("How do I convert between BTU/hr, TR, and Kilowatts?",
             "To convert BTU/hr to Tons of Refrigeration, divide by 12,000. To convert Kilowatts to Tons, divide by 3.517. To convert BTU/hr to Watts, multiply by 0.293. You can convert units instantly with our <a href=\"unit-converter.html\">Unit Converter</a>."),
            ("Why must kitchen and server room cooling loads be calculated separately?",
             "Commercial kitchens and server rooms have exceptionally high internal heat generation that far exceeds standard floor-area estimates. Server rooms produce nearly 100% sensible heat (3,412 BTU/hr per kW of IT gear) with zero latent load, while commercial kitchens produce massive latent steam moisture alongside high cooking sensible gains.")
        ]
    },

    "pipe-sizing-calculator.html": {
        "verification": "ASME B31.3 Process Piping & Darcy-Weisbach Fluid Mechanics",
        "standards": [
            ("Piping Standard", "ASME B31.3 Process Piping & ASHRAE 90.1 Hydronic Velocity Limits"),
            ("Governing Equation", "Continuity Equation (Q = A × v) & Darcy-Weisbach Friction Head Loss"),
            ("Velocity Bounds", "Suction: 2–4 ft/s | Discharge: 4–8 ft/s | Municipal Water: 1.5–2.5 m/s"),
            ("Units Supported", "GPM & Inches (US Customary) | m³/hr, L/s & mm (Metric SI)")
        ],
        "example_title": "Field Case Study: Industrial Cooling Tower Water Circulation Sizing",
        "example_badge": "Real-World Hydraulics Problem",
        "steps": [
            ("Step 1: Define Process Volumetric Flow Rate",
             r"Q = 120\text{ m}^3/\text{hr} = 0.0333\text{ m}^3/\text{s}\ (528.3\text{ GPM})",
             "A central industrial cooling tower circulation loop requires 120 m³/hr of continuous water circulation."),
            ("Step 2: Establish Optimal Fluid Velocity Boundary (v = 2.0 m/s)",
             r"v = 2.0\text{ m/s}\ (6.56\text{ ft/s})",
             "Under ASHRAE hydronic guidelines, discharge piping velocity is targeted at 2.0 m/s to prevent pipe erosion and limit pumping frictional head loss."),
            ("Step 3: Calculate Required Pipe Cross-Sectional Area and Internal Diameter (d)",
             r"A = \frac{Q}{v} = \frac{0.0333}{2.0} = 0.01667\text{ m}^2,\quad d = \sqrt{\frac{4 \times A}{\pi}} = 0.1456\text{ m} = 145.6\text{ mm}",
             'Calculated internal diameter is 145.6 mm. Specifying a standard <strong>DN150 (6-inch Schedule 40) steel pipe</strong> (inner diameter 154 mm) results in an optimal velocity of 1.79 m/s. Size the drive motor with our <a href="torque-calculator.html">Torque Calculator</a> and chemical biocides with our <a href="chemical-dosing-calculator.html">Chemical Dosing Calculator</a>.')
        ],
        "final_result": "Hydraulic Specification: DN150 (6-Inch) Schedule 40 Pipe | Velocity: 1.79 m/s (Within Optimal 1.5–2.2 m/s Band) | Non-Erosive Flow.",
        "faqs": [
            ("Why is fluid velocity capped in water distribution pipes?",
             "Velocities above 8 ft/s (2.4 m/s) generate excessive turbulence that erodes pipe inner walls, creates severe hydraulic water hammer during valve closure, and causes pumping head loss that wastes electric power. Velocities below 2 ft/s (0.6 m/s) allow sediment to settle and foul heat exchangers."),
            ("What is the difference between Nominal Pipe Size (NPS) and Internal Diameter (ID)?",
             "NPS is a standardized North American sizing designation. For pipe sizes from 1/8\" up to 12\", the NPS does not match either the exact inside diameter or outside diameter. The actual inside diameter varies depending on wall thickness (Schedule 40 vs Schedule 80). Only at 14\" and above does the outer diameter match the nominal size."),
            ("How does pipe roughness affect frictional head loss?",
             "According to the Darcy-Weisbach equation, friction factor (f) depends on pipe interior roughness (ε). Smooth copper and PVC pipes have very low roughness (0.0015 mm), causing minimal pressure drop. Old cast iron or corroded steel pipes have high roughness (0.15–0.5 mm), increasing pumping resistance by 50% or more."),
            ("What is Reynolds Number (Re) in pipe flow?",
             "Reynolds Number is a dimensionless ratio of inertial forces to viscous forces. Values below 2,000 indicate smooth laminar flow; values between 2,000 and 4,000 indicate unstable transition flow; and values exceeding 4,000 indicate turbulent flow typical of industrial piping systems.")
        ]
    },

    "rebar-calculator.html": {
        "verification": "ASTM A615 / A615M & BS 4449 Reinforcing Steel Standards",
        "standards": [
            ("Material Standard", "ASTM A615 / A615M Deformed Billet-Steel Bars (Grade 60 / 420 MPa)"),
            ("Weight Formula", "Unit Weight: W = D² / 162 (kg/m) | W = D² / 24 (lbs/ft for imperial # sizes)"),
            ("Splice Development", "40d to 50d Tension Lap Splice per ACI 318-19 Section 25.5"),
            ("Steel Density", "Standard Structural Steel Density: 7,850 kg/m³ (490 lbs/ft³)")
        ],
        "example_title": "Field Case Study: Foundation Slab Bottom Mat Reinforcement Take-Off",
        "example_badge": "Real-World Structural Problem",
        "steps": [
            ("Step 1: Define Slab Geometry and Bar Spacing Schedule",
             r"L = 12.0\text{ m},\quad W = 8.0\text{ m},\quad \text{Bar: T12 (12mm) @ 150mm c/c both directions}",
             "A structural foundation slab measuring 12.0m by 8.0m requires a bottom reinforcement mesh of 12mm high-yield deformed bars spaced at 150mm on center."),
            ("Step 2: Calculate Number of Longitudinal and Transverse Bars",
             r"\text{Bars}_{long} = \lceil \frac{8.0}{0.15} \rceil + 1 = 55\text{ bars},\quad \text{Bars}_{trans} = \lceil \frac{12.0}{0.15} \rceil + 1 = 81\text{ bars}",
             "Longitudinal direction requires 55 bars of 12m length. Transverse direction requires 81 bars of 8m length."),
            ("Step 3: Compute Total Linear Steel Length with End Hooks & Lap Splices",
             r"\text{Total Length} = (55 \times 12.0\text{m}) + (81 \times 8.0\text{m}) + \text{Hooks (8%)} = 660 + 648 + 105 = 1{,}413\text{ meters}",
             "Adding 8% for end hook bends and overlap splices yields 1,413 linear meters of 12mm rebar."),
            ("Step 4: Compute Total Reinforcement Mass Using the D²/162 Formula",
             r"W_{unit} = \frac{12^2}{162} = 0.888\text{ kg/m},\quad M_{total} = 1{,}413\text{ m} \times 0.888\text{ kg/m} = 1{,}255.4\text{ kg}",
             'Total steel reinforcement mass is <strong>1.26 metric tonnes (2,768 lbs)</strong>. Estimate the concrete pour volume for this slab with our <a href="concrete-calculator.html">Concrete Calculator</a> and visit our <a href="civil.html">Civil Engineering Hub</a>.')
        ],
        "final_result": "Reinforcement Take-Off: 1,413 Linear Meters T12 Rebar | Unit Mass: 0.889 kg/m | Total Steel Weight: 1.26 Tonnes (2,768 lbs).",
        "faqs": [
            ("How does the rebar weight formula D² / 162 work?",
             "The formula derives from multiplying the cross-sectional area of a circular bar [π·(D/2)²] by steel's density (7,850 kg/m³). Converting millimeters to meters: Mass per meter = (π/4) × (D/1000)² × 7,850 = D² / 162.28 kg/m. Rounding to 162 provides a standard civil engineering field shortcut."),
            ("How are US Imperial rebar sizes (#3, #4, #5, #8) numbered?",
             "Imperial bar numbers represent diameter in eighths of an inch. A #3 bar is 3/8\" (9.5 mm); a #4 bar is 4/8\" or 1/2\" (12.7 mm); a #5 bar is 5/8\" (15.9 mm); and a #8 bar is 8/8\" or exactly 1.0 inch (25.4 mm)."),
            ("What is the minimum concrete cover required for rebar?",
             "Under ACI 318-19, concrete cover protects steel from moisture and fire. Minimum cover is 75 mm (3 inches) for concrete cast permanently against soil; 40 to 50 mm (1.5–2 inches) for exterior beams and columns; and 20 mm (0.75 inch) for interior slabs not exposed to weather."),
            ("What is the difference between Grade 40 and Grade 60 rebar?",
             "Grade 40 steel has a minimum yield strength of 40,000 PSI (approx. 280 MPa). Grade 60 steel has a minimum yield strength of 60,000 PSI (approx. 420 MPa). Grade 60 is the standard structural steel specified for modern commercial and residential seismic designs.")
        ]
    },

    "chemical-dosing-calculator.html": {
        "verification": "AWWA Standard B300 & EPA Water Treatment Standards",
        "standards": [
            ("Disinfection Standard", "AWWA B300 Standard for Hypochlorites & EPA Surface Water Treatment Rules"),
            ("Mass Flow Formula", "Reagent Mass Rate: m = Q × C / (% Active × Specific Gravity)"),
            ("Metering Calibration", "Volumetric Dosing Pump Stroke Calibration (mL/min and L/hr)"),
            ("Units Supported", "PPM, mg/L, % Concentration, GPM, and m³/hr")
        ],
        "example_title": "Field Case Study: Industrial Wastewater Sodium Hypochlorite Dosing",
        "example_badge": "Real-World Chemical Engineering Problem",
        "steps": [
            ("Step 1: Define Wastewater Discharge Flow Rate and Target Chlorine Dose",
             r"Q = 1{,}500\text{ m}^3/\text{day}\ (62.5\text{ m}^3/\text{hr}),\quad C_{target} = 4.0\text{ mg/L}\ (4.0\text{ g/m}^3)",
             "An industrial wastewater facility discharges 1,500 m³/day requiring a continuous active chlorine disinfectant dose of 4.0 mg/L (ppm)."),
            ("Step 2: Calculate Pure Active Chemical Demand",
             r"\dot{m}_{active} = 1{,}500\text{ m}^3 \times 4.0\text{ g/m}^3 = 6{,}000\text{ g/day} = 6.00\text{ kg/day}",
             "The stream requires 6.00 kg of pure active chlorine element daily."),
            ("Step 3: Compensate for Commercial Solution Active Concentration (12.5%)",
             r"\dot{m}_{commercial} = \frac{6.00\text{ kg}}{0.125} = 48.00\text{ kg/day}",
             "The site uses bulk commercial liquid sodium hypochlorite supplied at 12.5% active chlorine by mass."),
            ("Step 4: Compute Volumetric Metering Pump Delivery Rate (mL/min)",
             r"V = \frac{48.00\text{ kg}}{1.21\text{ kg/L}} = 39.67\text{ L/day} \implies \text{Rate} = \frac{39{,}670\text{ mL}}{1{,}440\text{ min}} = 27.55\text{ mL/min}",
             'At solution specific gravity of 1.21 kg/L, calibrate the positive-displacement metering pump to <strong>27.55 mL/min (1.65 L/hr)</strong>. Size delivery piping with our <a href="pipe-sizing-calculator.html">Pipe Sizing Calculator</a> and explore our <a href="chemical.html">Chemical Engineering Hub</a>.')
        ],
        "final_result": "Feed Rate: 39.67 L/Day Commercial Bleach (12.5%) | Dosing Pump Setpoint: 27.55 mL/min | Verified EPA Residual Compliance.",
        "faqs": [
            ("What is the difference between mg/L and parts per million (ppm)?",
             "For dilute aqueous solutions with a specific gravity close to 1.0 (such as drinking water), 1 milligram per liter (mg/L) is identical to 1 part per million (ppm), because 1 liter of water weighs 1,000,000 milligrams. For dense chemicals (e.g. 50% caustic soda with SG 1.52), specific gravity must be factored in."),
            ("Why does hypochlorite bleach lose strength over time?",
             "Sodium hypochlorite decomposes spontaneously into sodium chloride and oxygen or chlorate. Rate of decomposition accelerates dramatically with exposure to sunlight (UV rays), elevated temperatures (>30°C), and contact with transition metals like copper and nickel."),
            ("What is the difference between chemical dosage and chemical demand?",
             "Dosage is the amount of chemical added to the water. Demand is the portion consumed by reacting with organic matter, iron, manganese, and bacteria. The leftover active chemical is residual, which provides critical downstream antimicrobial protection."),
            ("How do I calibrate a chemical metering pump using a drawdown cylinder?",
             "Isolate the chemical supply tank and run the metering pump drawing exclusively from a graduated glass cylinder. Measure the volume drawn down over exactly 60 seconds (in mL). Adjust pump stroke length or pulse frequency until measured drawdown matches calculated target mL/min.")
        ]
    },

    "smoke-detector-spacing-calculator.html": {
        "verification": "NFPA 72 National Fire Alarm and Signaling Code (2022/2025 Edition)",
        "standards": [
            ("Governing Code", "NFPA 72 National Fire Alarm and Signaling Code Clause 17.7.3"),
            ("Baseline Grid", "30-Foot (9.1m) Square Grid Spacing on Smooth Flat Ceilings"),
            ("Coverage Radius", "21.2-Foot (6.4m) Maximum Radial Reach to All Enclosure Corners"),
            ("Wall Clearances", "Minimum 4\" (100mm) Offset from Ceiling Corners to Prevent Dead Air Pocketing")
        ],
        "example_title": "Field Case Study: Commercial Office Floor Smoke Detection Layout",
        "example_badge": "Real-World Fire Safety Problem",
        "steps": [
            ("Step 1: Define Room Dimensions and Ceiling Architecture",
             r"L = 36.0\text{ m},\quad W = 18.0\text{ m},\quad \text{Ceiling: 3.5m Smooth Concrete Slab}",
             "A commercial open-plan office space measures 36.0 meters long by 18.0 meters wide with a flat slab ceiling."),
            ("Step 2: Determine Grid Column & Row Intervals Under NFPA 72 Spacing (S = 9.1m)",
             r"\text{Columns} = \lceil \frac{36.0}{9.1} \rceil = 4\text{ intervals},\quad \text{Rows} = \lceil \frac{18.0}{9.1} \rceil = 2\text{ intervals}",
             "The space partitions into 4 columns along the length and 2 rows across the width."),
            ("Step 3: Verify Spacing and Perimeter Wall Offset Clearances",
             r"S_{length} = \frac{36}{4} = 9.00\text{m}\ (< 9.1\text{m}),\quad S_{width} = \frac{18}{2} = 9.00\text{m}\ (< 9.1\text{m})",
             "Spacing is 9.00m center-to-center. Distance to boundary walls is half spacing (4.50m), satisfying the 0.5S edge limit."),
            ("Step 4: Compute Total Detector Count and Check Radial Coverage",
             r"\text{Total Detectors} = 4 \times 2 = 8\text{ Optical Smoke Detectors},\quad R = \sqrt{4.5^2 + 4.5^2} = 6.36\text{m} \le 6.47\text{m}",
             'Eight detectors provide 100% compliant coverage with zero dead-air corners! Verify Notification Appliance Circuit (NAC) wiring with our <a href="voltage-drop-calculator.html">Voltage Drop Calculator</a> and explore our <a href="fire-safety.html">Fire Safety Hub</a>.')
        ],
        "final_result": "Engineered Layout: 8 Optical Smoke Detectors | 4 × 2 Grid @ 9.0m c/c | Corner Radius: 6.36m (Passed NFPA 72 limit of 6.47m).",
        "faqs": [
            ("Why is there a 4-inch dead air exclusion zone near ceiling corners?",
             "In an enclosed room, thermal convection creates a boundary stagnation layer in the 90-degree corner where ceiling meets wall. Rising buoyant smoke curls away from the corner without entering it. NFPA 72 strictly prohibits mounting detectors within 4 inches (100 mm) of any corner."),
            ("How does ceiling height above 10 feet affect smoke detector spacing?",
             "As ceiling height increases, rising smoke plumes cool and entrain ambient air, diffusing before reaching the ceiling. For ceiling heights between 10 ft and 30 ft, NFPA 72 Table 17.7.3.1.2 mandates reducing detector spacing down to 0.7S, 0.5S, or 0.4S to guarantee early detection."),
            ("How does HVAC airflow velocity affect smoke detection?",
             "High ventilation airflows (above 8 Air Changes per Hour) dilute smoke and blow it away from detectors. Spacing must be reduced from 900 sq ft down to 500, 250, or 125 sq ft per detector in cleanrooms, computer server rooms, and telecommunication facilities."),
            ("When should optical beam smoke detectors be used instead of spot detectors?",
             "Optical projected beam smoke detectors are ideal for high-ceiling open spaces (atriums, warehouses, aircraft hangars, sports arenas) where spot detector installation and ongoing maintenance access are impractical. A single beam covers optical path lengths up to 100 meters (330 feet).")
        ]
    },

    "compound-interest-calculator.html": {
        "verification": "US GAAP & IFRS Compound Annual Growth Rate (CAGR) Standards",
        "standards": [
            ("Compounding Law", "Future Value: A = P × (1 + r/n)^(n×t) & Continuous: A = P × e^(rt)"),
            ("Yield Standard", "Annual Percentage Yield (APY) vs Nominal APR Disclosures"),
            ("Frequencies", "Daily (365), Monthly (12), Quarterly (4), Semi-Annual (2), and Annual (1)"),
            ("Accounting Compliance", "IFRS 9 Financial Instruments Time Value of Money")
        ],
        "example_title": "Financial Case Study: Corporate Sinking Fund Investment Growth",
        "example_badge": "Real-World Wealth Problem",
        "steps": [
            ("Step 1: Define Initial Principal, Growth Rate, and Investment Horizon",
             r"P = \$50{,}000,\quad r = 8.00\%\ (0.08),\quad t = 15\text{ years},\quad n = 12\text{ (Monthly Compounding)}",
             "A corporate treasury invests $50,000 into an index-linked commercial growth fund earning 8.0% annual interest compounded monthly."),
            ("Step 2: Calculate Effective Annual Yield (APY)",
             r"\text{APY} = \left(1 + \frac{0.08}{12}\right)^{12} - 1 = (1.006667)^{12} - 1 = 8.30\%",
             "Monthly compounding increases the effective annual yield from 8.0% to 8.30% APY."),
            ("Step 3: Compute Future Investment Value (A)",
             r"A = 50{,}000 \times \left(1 + \frac{0.08}{12}\right)^{12 \times 15} = 50{,}000 \times (1.006667)^{180} = \$165{,}347.16",
             "The original $50,000 investment grows to $165,347.16 over 15 years."),
            ("Step 4: Compute Total Compound Interest Earned",
             r"\text{Interest} = A - P = \$165{,}347.16 - \$50{,}000 = \$115{,}347.16",
             'The investment generates $115,347.16 in pure compounding interest (over 230% capital gain!). Compare against amortized loans with our <a href="loan-emi-calculator.html">Loan EMI Calculator</a> and explore our <a href="finance.html">Finance Hub</a>.')
        ],
        "final_result": "Investment Growth: Initial $50,000 grows to $165,347.16 | Total Interest: $115,347.16 | Capital Multiplier: 3.31× Initial Investment.",
        "faqs": [
            ("What is the difference between simple interest and compound interest?",
             "Simple interest calculates returns strictly on the original principal balance throughout the entire term. Compound interest calculates returns on both the original principal and accumulated interest from previous periods, creating exponential 'interest on interest' wealth acceleration."),
            ("What is the Rule of 72 in compound interest?",
             "The Rule of 72 is a mental shortcut to estimate how many years it takes for an investment to double at a fixed annual interest rate. Divide 72 by the annual interest rate: at 8% interest, capital doubles in approximately 9 years (72 / 8 = 9)."),
            ("What is the difference between APR and APY?",
             "Annual Percentage Rate (APR) is the simple annualized nominal interest rate without accounting for compounding within the year. Annual Percentage Yield (APY) takes compounding frequency into account, revealing the true annual return. At 10% APR compounded daily, the effective APY is 10.52%."),
            ("How does continuous compounding work?",
             "Continuous compounding assumes interest is compounded an infinite number of times per second. It is calculated using Euler's constant (e ≈ 2.71828) via the formula A = P·e^(rt). It represents the theoretical maximum growth limit for any given interest rate.")
        ]
    }
}

print(f"Loaded {len(ADDITIONAL_DATA)} additional tools definitions.")
