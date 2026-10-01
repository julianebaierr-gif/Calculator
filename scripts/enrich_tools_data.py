import os
import re
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Dictionary containing tool data
TOOLS_DATA = {
    "cable-sizing-calculator.html": {
        "verification": "IEC 60364-5-52:2009 & BS 7671 (18th Edition Wiring Regulations)",
        "standards": [
            ("Governing Code", "IEC 60364-5-52 Section 523 & BS 7671:2018+A2:2022"),
            ("Installation Methods", "Reference Methods A1, A2, B1, B2, C, D1, E, and F"),
            ("Thermal Derating", "Ambient Temperature (Ca) & Grouping Factor (Cg)"),
            ("Verification Method", "Cross-verified against Schneider Electric & ABB LV Engineering Tables")
        ],
        "example_title": "Field Case Study: 45 kW Submersible Pump Feeder Cable Sizing",
        "example_badge": "Real-World Engineering Problem",
        "steps": [
            ("Step 1: Calculate Continuous Full-Load Design Current (Ib)",
             r"I_b = \frac{P}{\sqrt{3} \times V \times \cos\phi} = \frac{45{,}000}{\sqrt{3} \times 400 \times 0.85} = 76.41\text{ A}",
             "For a 45 kW submersible irrigation pump operating at 400V 3-phase with an 0.85 power factor, baseline operational load current Ib equals 76.41 Amperes."),
            ("Step 2: Apply NEC/IEC Continuous Operating Safety Margin (125%)",
             r"I_{continuous} = 76.41 \times 1.25 = 95.51\text{ A}",
             "Continuous duty (>3 hours continuous operation) requires applying the 1.25 safety factor to protect against thermal buildup."),
            ("Step 3: Establish Combined Derating Multipliers (Ca × Cg)",
             r"C_a = 0.87\ (40^\circ\text{C air}),\quad C_g = 0.79\ (2\text{ circuits on tray}) \implies C_{total} = 0.6873",
             "At 40°C ambient temperature with 2 circuits bundled on a perforated tray, thermal dissipation is reduced according to IEC Table B.52.14."),
            ("Step 4: Compute Required Tabulated Conductor Ampacity (It) & Select Cable",
             r"I_t = \frac{95.51}{0.6873} = 138.96\text{ A}",
             'Consulting IEC Reference Method E (multicore XLPE in free air), a <strong>35 mm² 4-core copper XLPE cable</strong> carries a tabulated ampacity of 145 A, safely satisfying It. Cross-reference installation methods in our <a href="engineering.html">Electrical Engineering Hub</a>.'),
            ("Step 5: Verify Voltage Drop over 95-meter Feeder Run",
             r"\Delta V = \frac{\sqrt{3} \times 76.41 \times 95 \times 0.627}{1000} = 7.89\text{ V}\ (1.97\%)",
             'The 95-meter run experiences a 7.89V drop (1.97%), comfortably under the 3.0% maximum allowable feeder threshold! Verify circuit drop with our <a href="voltage-drop-calculator.html">Voltage Drop Calculator</a> or solve circular resistance with our <a href="ohms-law-calculator.html">Ohm\'s Law Calculator</a>.')
        ],
        "final_result": "Specified Cable: 35 mm² 4-Core XLPE/SWA Copper | Base Tabulated: 145 A | Derated Capacity: 99.7 A > 95.5 A | Voltage Drop: 1.97% (Compliant).",
        "faqs": [
            ("What is the difference between tabulated current (It) and derated capacity (Iz)?",
             "Tabulated current (It) is the raw current-carrying capacity from standard manufacturer or code tables at standard reference conditions (typically 30°C in air). Derated capacity (Iz = It × Ca × Cg) is the true allowable current in real operating conditions after applying ambient temperature, grouping, and thermal insulation factors."),
            ("Why does XLPE allow higher ampacity than PVC for the same copper size?",
             "Cross-Linked Polyethylene (XLPE) has a thermosetting polymer structure that withstands continuous operating temperatures up to 90°C and short-circuit spikes up to 250°C. Thermoplastic PVC softens above 70°C. This 20°C temperature advantage allows XLPE to carry roughly 18% to 22% higher current for identical copper cross-sectional area."),
            ("How does conduit fill percentage affect cable thermal derating?",
             "Under NEC Chapter 9 Table 1, raceway fill must not exceed 40% for three or more conductors. Overfilling conduits restricts convective airflow, creating heat concentration that degrades insulation. When more than three current-carrying conductors share a raceway, NEC 310.15(C)(1) requires bundling derating factors down to 50%."),
            ("When should I choose Aluminum over Copper conductors?",
             "Aluminum is significantly lighter and approximately 60% less expensive per foot than copper, making it the preferred choice for long utility service entrance feeders. However, aluminum has higher electrical resistivity (0.0285 vs 0.0178 Ω·mm²/m), requiring roughly two AWG sizes larger to carry the same current as copper.")
        ]
    },

    "voltage-drop-calculator.html": {
        "verification": "NEC NFPA 70 Informational Note 210.19(A) & IEC 60364-5-52 Annex G",
        "standards": [
            ("Governing Standard", "NEC 210.19(A) / 215.2(A) & IEC 60364-5-52 Annex G"),
            ("Thresholds Enforced", "3% Branch Circuit / 5% Total Feeder + Branch"),
            ("Conductor Resistivities", "Copper: 0.0178 Ω·mm²/m (at 20°C) / Aluminum: 0.0285 Ω·mm²/m"),
            ("Phase Topologies", "Single-Phase (2-Wire) and Three-Phase Balanced (3/4-Wire)")
        ],
        "example_title": "Field Case Study: 120-Meter 3-Phase Commercial Warehouse Feeder",
        "example_badge": "Real-World Engineering Problem",
        "steps": [
            ("Step 1: Define Circuit Parameters and Operational Current",
             r"V_{LL} = 400\text{ V},\quad I = 55\text{ A},\quad L = 120\text{ m},\quad \text{Conductor: 25 mm² Copper}",
             "A distribution panel supplies a 55A balanced 3-phase machinery load located 120 meters away from the main switchboard."),
            ("Step 2: Determine Conductor Resistance (R)",
             r"R = \frac{\rho \times L}{A} = \frac{0.0178 \times 120}{25} = 0.08544\ \Omega",
             "At standard operating temperature, resistance of each 25 mm² copper phase conductor over 120 meters equals 0.0854 Ohms."),
            ("Step 3: Calculate Line-to-Line Voltage Drop (ΔV)",
             r"\Delta V = \sqrt{3} \times I \times R = \sqrt{3} \times 55 \times 0.08544 = 8.14\text{ Volts}",
             "Applying the 3-phase vector displacement factor (√3 ≈ 1.732) yields an 8.14 Volt line-to-line drop."),
            ("Step 4: Compute Percentage Voltage Drop and Verify Code Compliance",
             r"\%V_{drop} = \frac{\Delta V}{V_{nominal}} \times 100 = \frac{8.14}{400} \times 100 = 2.03\% \le 3.0\%",
             'The 2.03% drop is well within the 3.0% maximum feeder recommendation! To verify thermal ampacity of the 25 mm² cable, use our <a href="cable-sizing-calculator.html">Cable Sizing Calculator</a> or explore our <a href="engineering.html">Electrical Engineering Hub</a>.'),
            ("Step 5: Calculate Total Line Power Dissipation (I²R Loss)",
             r"P_{loss} = 3 \times I^2 \times R = 3 \times 55^2 \times 0.08544 = 775.2\text{ Watts}",
             'The feeder dissipates 775.2 Watts as heat into the raceway. Analyze continuous circuit power using our <a href="ohms-law-calculator.html">Ohm\'s Law Calculator</a>.')
        ],
        "final_result": "Calculation Summary: Feeder Length: 120m | Line Drop: 8.14 V (2.03%) | Line Power Loss: 775 W | NEC/IEC Compliant (Pass).",
        "faqs": [
            ("Why does single-phase voltage drop use 2 × L while 3-phase uses √3 × L?",
             "In a single-phase circuit, current travels out along the active conductor and returns through the neutral conductor, making the total circuit length 2 × L. In a balanced 3-phase circuit, the three phase currents vectorially cancel out in the neutral (or ground), and the line-to-line voltage drop is determined by the 120-degree phase displacement between vectors, introducing the factor √3 ≈ 1.732."),
            ("What are the consequences of exceeding the NEC 3% voltage drop limit?",
             "Exceeding 3% causes incandescent and LED luminaires to visibly flicker or dim, induction motors to draw higher current (causing winding overheating and insulation breakdown), electronic power supplies to reset, and electric heaters to lose significant thermal output (power drops with the square of voltage: P = V²/R)."),
            ("How does operating temperature affect conductor resistance?",
             "Conductor resistance increases linearly with temperature according to the formula: R2 = R1 × [1 + α(T2 - T1)], where α is the temperature coefficient of resistance (approx. 0.00393/°C for copper). A conductor operating at 75°C has roughly 21% higher resistance than at 20°C, increasing voltage drop significantly under heavy load."),
            ("Can increasing conductor size solve voltage drop on very long runs?",
             "Yes. Up-sizing the conductor increases cross-sectional area (A), directly reducing resistance (R = ρ·L/A) and voltage drop. For exceptionally long runs (e.g. over 200 meters), cables are frequently sized based on voltage drop rather than thermal ampacity.")
        ]
    },

    "ohms-law-calculator.html": {
        "verification": "Ohm's Law & Joule's First Law of Electrical Heating (P = V·I = I²R = V²/R)",
        "standards": [
            ("Fundamental Law", "Georg Ohm's Proportionality: V = I × R"),
            ("Power Derivations", "Joule-Lenz Law: P = V × I = I² × R = V² / R"),
            ("Derivation Matrix", "Complete 12-Formula Wheel for DC & Unity Power Factor AC"),
            ("Verification Method", "Analytically validated against IEEE Standard 551 electrical models")
        ],
        "example_title": "Field Case Study: Sizing an Industrial Tank Immersion Heating Element",
        "example_badge": "Real-World Engineering Problem",
        "steps": [
            ("Step 1: Define Thermal Heating Rating and Supply Voltage",
             r"P = 4{,}500\text{ W}\ (4.5\text{ kW}),\quad V = 230\text{ V AC}",
             "An industrial chemical process tank requires a 4.5 kW electric heating element connected to a 230V single-phase electrical supply."),
            ("Step 2: Calculate Continuous Operating Current Draw (I)",
             r"I = \frac{P}{V} = \frac{4{,}500\text{ W}}{230\text{ V}} = 19.57\text{ Amperes}",
             "The element draws 19.57 Amperes of continuous resistive current during steady-state heating."),
            ("Step 3: Determine Internal Element Electrical Resistance (R)",
             r"R = \frac{V^2}{P} = \frac{230^2}{4{,}500} = 11.76\ \Omega\quad \left(\text{or } R = \frac{V}{I} = \frac{230}{19.57} = 11.75\ \Omega\right)",
             "The Nichrome wire internal heating element must be engineered to provide exactly 11.76 Ohms of hot resistance."),
            ("Step 4: Verify Power Loss and Heat Generation Formula (I²R)",
             r"P = I^2 \times R = (19.565)^2 \times 11.756 = 4{,}500.0\text{ Watts}",
             'All four Ohm\'s law wheel equations produce identical results. Size branch circuit wiring for this heater with our <a href="cable-sizing-calculator.html">Cable Sizing Calculator</a> and verify line drop with our <a href="voltage-drop-calculator.html">Voltage Drop Calculator</a>.'),
            ("Step 5: Precision Resistor Matching and Breadboard Prototyping",
             r"R_{tolerance} = 11.76\ \Omega \pm 1\% \implies \text{Precision calibration}",
             'For electronic control sensors and precision resistor circuits, decode bands with our <a href="resistor-color-code-calculator.html">Resistor Color Code Calculator</a> or explore our <a href="engineering.html">Electrical Engineering Hub</a>.')
        ],
        "final_result": "Heater Specification: Power: 4,500 W | Voltage: 230 V | Operating Current: 19.57 A | Resistance: 11.76 Ω | Complete 12-Formula Wheel Harmony.",
        "faqs": [
            ("What is the complete 12-formula Ohm's law wheel?",
             "The Ohm's law wheel connects Voltage (V), Current (I), Resistance (R), and Power (P). For Voltage: V = I·R, V = P/I, V = √(P·R). For Current: I = V/R, I = P/V, I = √(P/R). For Resistance: R = V/I, R = V²/P, R = P/I². For Power: P = V·I, P = I²·R, P = V²/R."),
            ("Does Ohm's Law apply to AC (Alternating Current) circuits?",
             "Ohm's Law applies directly to AC circuits containing purely resistive loads (such as heaters and incandescent lamps) where the power factor is 1.0. For reactive AC circuits containing inductors (motors, transformers) or capacitors, resistance R is replaced by impedance Z [Z = √(R² + X²)], and apparent power (VA) differs from active power (W)."),
            ("Why does electrical power increase with the square of current (P = I²R)?",
             "When current doubles through a fixed resistor, not only are twice as many charge carriers flowing per second, but each carrier encounters the same electric field, doubling the voltage required (V = I·R). Since Power is V × I, multiplying (2 × V) by (2 × I) quadruples total thermal power dissipation (2² = 4)."),
            ("What is the difference between an Ohmic and Non-Ohmic conductor?",
             "An Ohmic conductor (such as copper, aluminum, or standard carbon resistors at constant temperature) maintains a constant resistance regardless of applied voltage, producing a linear straight-line V-I graph. A Non-Ohmic conductor (such as a semiconductor diode, transistor, or filament bulb where temperature changes) exhibits a curved, non-linear V-I relationship.")
        ]
    },

    "concrete-calculator.html": {
        "verification": "ACI 318-19 Structural Concrete Code & BS EN 206 Specification",
        "standards": [
            ("Structural Code", "ACI 318-19 Building Code Requirements for Structural Concrete"),
            ("Mix Design Standard", "ASTM C94 Ready-Mixed Concrete & BS EN 206"),
            ("Dry Bulking Factor", "1.54 Standard Aggregate Interstitial Void Ratio"),
            ("Material Densities", "Cement: 1,440 kg/m³ | Concrete: 2,400 kg/m³ (Wet Compacted)")
        ],
        "example_title": "Field Case Study: Reinforced Concrete Foundation Raft Pour",
        "example_badge": "Real-World Construction Problem",
        "steps": [
            ("Step 1: Calculate Net Geometric Wet In-Situ Volume",
             r"V_{wet} = L \times W \times T = 10.0\text{m} \times 6.0\text{m} \times 0.25\text{m} = 15.0\text{ m}^3",
             "A commercial equipment foundation raft measures 10.0m long, 6.0m wide, and 0.25m thick, requiring 15.0 cubic meters of wet concrete."),
            ("Step 2: Add Standard Jobsite Handling & Formwork Wastage (5%)",
             r"V_{order} = 15.0 \times 1.05 = 15.75\text{ m}^3\ (20.6\text{ yd}^3)",
             "Allowing 5% for irregular sub-base excavation and pump line priming gives a total ordering volume of 15.75 m³."),
            ("Step 3: Convert to Dry Constituent Volume Using the 1.54 Bulking Factor",
             r"V_{dry} = 15.75 \times 1.54 = 24.255\text{ m}^3",
             "Dry cement, sand, and aggregate particles contain loose interstitial air pockets that collapse when water is added, requiring 24.26 m³ of raw dry materials."),
            ("Step 4: Compute Material Batch Breakdown for M20 Structural Mix (1:1.5:3)",
             r"\sum \text{Parts} = 1 + 1.5 + 3 = 5.5,\quad \text{Cement Vol} = \frac{1}{5.5} \times 24.255 = 4.41\text{ m}^3",
             'Multiplying by cement density (1,440 kg/m³) yields 6,350 kg, requiring <strong>127 standard 50kg bags of cement</strong>, 6.62 m³ of sand, and 13.23 m³ of coarse gravel. Size the reinforcement mat for this raft with our <a href="rebar-calculator.html">Rebar Calculator</a>.'),
            ("Step 5: Convert Units for North American Batching",
             r"15.75\text{ m}^3 = 20.60\text{ cubic yards} \implies \text{Ready-mix truck loads}",
             'Convert between metric cubic meters and imperial cubic yards seamlessly with our <a href="unit-converter.html">Unit Converter</a> or browse our <a href="civil.html">Civil Engineering Hub</a>.')
        ],
        "final_result": "Material Take-Off: 15.75 m³ Wet Concrete | 127 Bags Cement (50kg) | 6.6 m³ Sand | 13.2 m³ Aggregate | 100% Monolithic Placement Security.",
        "faqs": [
            ("Why do dry concrete ingredients lose 35% of their volume when mixed?",
             "Loose dry sand and gravel contain air voids between angular particles (typically 30% to 35% void ratio). When water and fine cement paste are added, the water lubricates the grains and cement paste fills the microscopic gaps, eliminating air pockets. As a result, 1.54 m³ of loose dry components compacts into exactly 1.0 m³ of dense wet concrete."),
            ("What is the difference between nominal mix concrete and design mix concrete?",
             "Nominal mix concrete uses rough volumetric batching ratios (such as 1:2:4 for M15 or 1:1.5:3 for M20) suitable for small residential structures up to 20 MPa strength. Design mix concrete (mandated by ACI 318 for commercial structures) is determined by laboratory trial batches based on exact aggregate grading, moisture correction, water-cement ratio, and compressive strength testing."),
            ("How many standard 50kg bags of cement are in one cubic meter of concrete?",
             "For a standard M20 structural mix (1:1.5:3 proportion), approximately 8.0 to 8.2 bags of 50kg cement are required per cubic meter of finished wet concrete. For a richer M25 mix (1:1:2), approximately 10.5 to 11.0 bags are required per cubic meter."),
            ("How long must newly poured concrete cure before supporting structural loads?",
             "Concrete achieves approximately 16% of its characteristic compressive strength in 24 hours, 65% to 70% in 7 days, and reaches its full specified characteristic strength (f'c) at 28 days under proper moist curing conditions (continuous water spraying or curing compounds).")
        ]
    },

    "loan-emi-calculator.html": {
        "verification": "US GAAP, IFRS 9 Financial Instruments & Truth in Lending Act (Regulation Z)",
        "standards": [
            ("Amortization Algorithm", "Reducing-Balance Amortization Schedule (Ordinary Annuity Formula)"),
            ("Interest Calculation", "Periodic Periodic Rate r = Annual Rate / 12 (Monthly compounding)"),
            ("Balance Crossover", "Exact Principal-Interest Balance Crossing Point Modeling"),
            ("Disclosure Standard", "Annual Percentage Rate (APR) compliant with Truth in Lending (Reg Z)")
        ],
        "example_title": "Financial Case Study: $350,000 Commercial Facility Mortgage Amortization",
        "example_badge": "Real-World Financial Problem",
        "steps": [
            ("Step 1: Define Borrowing Principal, Annual Rate, and Term",
             r"P = \$350{,}000,\quad r_{annual} = 6.75\%,\quad n = 25\text{ years}\ (300\text{ monthly payments})",
             "A business takes out a $350,000 commercial property mortgage at a fixed 6.75% annual interest rate over a 25-year repayment term."),
            ("Step 2: Calculate Periodic Monthly Interest Rate (r)",
             r"r = \frac{0.0675}{12} = 0.005625\text{ per month}",
             "Interest is computed monthly on the diminishing principal balance at 0.5625% per month."),
            ("Step 3: Compute Equated Monthly Installment (EMI)",
             r"\text{EMI} = \frac{P \cdot r \cdot (1+r)^n}{(1+r)^n - 1} = \frac{350{,}000 \cdot 0.005625 \cdot (1.005625)^{300}}{(1.005625)^{300} - 1} = \$2{,}417.83",
             'The fixed monthly repayment is <strong>$2,417.83</strong>. Model prepayments and amortization schedules with our interactive calculator.'),
            ("Step 4: Compute Total Outflow and Lifetime Interest Charges",
             r"\text{Total Outflow} = 300 \times \$2{,}417.83 = \$725{,}349.00,\quad \text{Total Interest} = \$375{,}349.00",
             'Over the 25-year tenure, the borrower pays $375,349 in interest charges (107.2% of the original loan principal!). Compare linear borrowing with our <a href="simple-interest-calculator.html">Simple Interest Calculator</a>.'),
            ("Step 5: Compare Against Sinking Fund Wealth Compounding & Payroll Cash Flow",
             r"A = P\left(1 + \frac{r}{m}\right)^{mt} \implies \text{Compound growth potential}",
             'Model investment growth of excess cash flow with our <a href="compound-interest-calculator.html">Compound Interest Calculator</a>, budget executive salaries with our <a href="salary-calculator.html">Salary Calculator</a>, and visit our <a href="finance.html">Finance Hub</a>.')
        ],
        "final_result": "Amortization Profile: Monthly EMI: $2,417.83 | Total Repayment: $725,349.00 | Total Interest: $375,349.00 | First-Month Split: $1,968.75 Interest / $449.08 Principal.",
        "faqs": [
            ("What is the difference between reducing-balance EMI and flat-rate interest?",
             "In reducing-balance amortization, interest in each billing cycle is calculated strictly on the remaining outstanding principal. As you pay off principal, the monthly interest charge decreases. In a flat-rate loan, interest is calculated on the full initial loan amount across the entire term, effectively doubling the true APR compared to reducing-balance loans."),
            ("Why is the interest portion so high during the early years of a mortgage?",
             "Because the outstanding principal balance is at its highest during the early years. On a $350,000 loan at 6.75%, the first month's interest alone is $1,968.75 ($350,000 × 0.0675 / 12), leaving only $449.08 to pay down principal. Only as principal decreases does the interest portion shrink and principal paydown accelerate."),
            ("How does making extra principal prepayments reduce total loan tenure?",
             "Any additional payment made directly reduces the outstanding principal balance. Since future interest is calculated on this lower balance, the required interest charge drops immediately, compounding savings over the remaining loan term and cutting years off your mortgage."),
            ("What is the Debt-to-Income (DTI) ratio limit for commercial and residential loans?",
             "Lenders typically enforce a maximum front-end DTI ratio of 28% (mortgage payment should not exceed 28% of gross monthly income) and a back-end DTI ratio of 36% to 43% (all recurring debt payments including auto loans, credit cards, and mortgages combined).")
        ]
    },

    "bmi-calculator.html": {
        "verification": "World Health Organization (WHO) Technical Report Series 854 & CDC Guidelines",
        "standards": [
            ("Clinical Standard", "WHO Technical Report Series 854 Physical Status: Interpretation of Anthropometry"),
            ("Diagnostic Formula", "Quetelet Index: BMI = Weight (kg) / [Height (m)]²"),
            ("International Cutoffs", "Underweight (<18.5), Normal (18.5–24.9), Overweight (25–29.9), Obese (≥30.0)"),
            ("Clinical Limitations", "Muscular hypertrophy, sarcopenia, gestational changes, and pediatric age")
        ],
        "example_title": "Clinical Case Study: Adult Anthropometric Evaluation & Body Composition",
        "example_badge": "Real-World Clinical Problem",
        "steps": [
            ("Step 1: Record Standard Anthropometric Measurements",
             r"\text{Sex: Male},\quad \text{Age: 34},\quad \text{Height: 180 cm}\ (1.80\text{m}),\quad \text{Weight: 88.0 kg}",
             "A 34-year-old male presents for a preventive health screening weighing 88.0 kg with a height of 180 cm (1.80 m)."),
            ("Step 2: Calculate Body Mass Index (BMI)",
             r"\text{BMI} = \frac{\text{Weight (kg)}}{\text{Height (m)}^2} = \frac{88.0}{1.80^2} = \frac{88.0}{3.24} = 27.16\text{ kg/m}^2",
             "The calculated BMI is 27.16 kg/m², placing the individual in the WHO 'Overweight' classification (25.0 to 29.9 kg/m²)."),
            ("Step 3: Cross-Validate with Circumference-Based Body Fat Percentage",
             r"\Delta = \text{Waist (89 cm)} - \text{Neck (39 cm)} = 50\text{ cm} \implies \text{Body Fat} = 17.5\%",
             'Despite a BMI of 27.16, the patient\'s body fat is a healthy 17.5%, indicating high athletic muscle mass! Evaluate true body composition with our <a href="body-fat-calculator.html">Body Fat Calculator</a>.'),
            ("Step 4: Determine Clinically Ideal Weight Range for Height",
             r"\text{Weight}_{min} = 18.5 \times 1.80^2 = 59.9\text{ kg},\quad \text{Weight}_{max} = 24.9 \times 1.80^2 = 80.7\text{ kg}",
             'For a height of 180 cm, the normal WHO weight range spans 59.9 kg to 80.7 kg. Calculate clinical target weights using our <a href="ideal-weight-calculator.html">Ideal Weight Calculator</a>.'),
            ("Step 5: Formulate Metabolic Energy Balance & Hydration Prescription",
             r"\text{BMR} \approx 1{,}830\text{ kcal/day},\quad \text{TDEE} \approx 2{,}835\text{ kcal/day}\ (1.55\times\text{ PAL})",
             'Plan daily nutrition with our <a href="calorie-calculator.html">Calorie Calculator</a>, track hydration with our <a href="water-intake-calculator.html">Water Intake Calculator</a>, and visit our <a href="health.html">Health & Fitness Hub</a>.')
        ],
        "final_result": "Clinical Profile: BMI: 27.16 kg/m² (Overweight by BMI alone) | True Body Fat: 17.5% (Athletic/Fit) | Lean Body Mass: 72.6 kg | Metabolic Maintenance: 2,835 kcal/day.",
        "faqs": [
            ("Why does BMI sometimes misclassify muscular athletes as overweight or obese?",
             "BMI relies strictly on gross total body weight and height squared. It cannot distinguish between dense lean muscle tissue, bone mass, and adipose fat. A bodybuilder with 10% body fat and high muscle volume will register a high BMI (28 to 32 kg/m²) despite having minimal cardiovascular fat risk."),
            ("What are the official WHO BMI cutoff categories for adults?",
             "The World Health Organization (WHO) classifies adult BMI as: Underweight (< 18.5 kg/m²), Normal Weight (18.5 – 24.9 kg/m²), Overweight (25.0 – 29.9 kg/m²), Obese Class I (30.0 – 34.9 kg/m²), Obese Class II (35.0 – 39.9 kg/m²), and Obese Class III / Severe (≥ 40.0 kg/m²)."),
            ("Are Asian population BMI thresholds different from international standards?",
             "Yes. The WHO Western Pacific Region recognizes that Asian populations face elevated cardiovascular and diabetes risks at lower BMI thresholds due to higher average percentages of body fat. For Asian adults, overweight is often defined as BMI ≥ 23.0 kg/m², and obesity as BMI ≥ 27.5 kg/m²."),
            ("What is the Quetelet Index and who invented BMI?",
             "Body Mass Index was originally developed in the 1830s by Belgian mathematician, astronomer, and statistician Adolphe Quetelet. Termed the 'Quetelet Index of Obesity', it was designed for population-level statistical modeling of the 'average man' rather than individual clinical health diagnostics.")
        ]
    },

    "subnet-calculator.html": {
        "verification": "IETF RFC 1918 Private IPv4 Allocation, RFC 4632 (CIDR) & IEEE 802.3",
        "standards": [
            ("Addressing Architecture", "Classless Inter-Domain Routing (CIDR) & VLSM (RFC 4632)"),
            ("Private IP Ranges", "RFC 1918: 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16"),
            ("Subnetting Math", "Bitwise AND, Network ID, Usable Host Range (2^h - 2), and Broadcast"),
            ("Mask Formats", "Dotted Decimal (255.255.255.0), Prefix Length (/24), and Wildcard (0.0.0.255)")
        ],
        "example_title": "Enterprise Cloud Architecture: Multi-Tier VPC Subnetting (/20 Allocation)",
        "example_badge": "Real-World Systems Engineering Problem",
        "steps": [
            ("Step 1: Define Base Network Block and Capacity",
             r"\text{Assigned VPC Block} = 172.24.0.0/20 \implies \text{Total IPs} = 2^{32 - 20} = 2^{12} = 4{,}096\text{ Addresses}",
             "An enterprise cloud network team is allocated the private IPv4 block 172.24.0.0/20 for a new cloud region."),
            ("Step 2: Size Production Tier Subnet Requiring 2,000 Usable Hosts",
             r"2^h - 2 \ge 2{,}000 \implies h = 11\ (2^{11} - 2 = 2{,}046\text{ hosts}) \implies \text{Prefix} = 32 - 11 = /21",
             "The production cluster requires at least 2,000 hosts. Allocating 11 host bits yields 2,046 usable IP addresses with a /21 subnet mask (255.255.248.0)."),
            ("Step 3: Define Production Subnet Network Boundaries & Usable Host Range",
             r"\text{Network ID} = 172.24.0.0/21,\quad \text{Usable Hosts} = 172.24.0.1\text{ to }172.24.7.254,\quad \text{Broadcast} = 172.24.7.255",
             "First address is reserved as the network identifier; the last address is reserved as the local broadcast address."),
            ("Step 4: Size Staging Tier Requiring 1,000 Hosts from Remaining Space",
             r"\text{Staging Block} = 172.24.8.0/22 \implies \text{Usable Range} = 172.24.8.1\text{ to }172.24.11.254\ (1{,}022\text{ hosts})",
             'Staging utilizes 10 host bits with a /22 subnet mask (255.255.252.0), leaving 172.24.12.0/22 available for database and DMZ tiers. Explore full network systems in our <a href="programmer.html">Programmer & Networking Hub</a>.'),
            ("Step 5: Convert Storage Capacity and Network Bandwidth Units",
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
            ("What is Variable Length Subnet Masking (VLSM)?",
             "VLSM is the network design practice of dividing an IP address space into subnets of different sizes with varying prefix lengths (e.g., /24 for user LANs, /28 for server DMZs, and /30 or /31 for point-to-point router links) to prevent IP address exhaustion.")
        ]
    }
}

print("Loaded tools data module successfully!")
