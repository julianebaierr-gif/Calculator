# -*- coding: utf-8 -*-
import glob
import re
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Full Categorized Mapping with Icons and Descriptions
CATEGORIES = {
    "health": {
        "name": "Health & Fitness",
        "icon": "⚖️",
        "hub": "health.html",
        "tools": [
            ("bmr-calculator.html", "BMR Calculator", "🧬", "Mifflin-St Jeor & Katch-McArdle resting calories"),
            ("macro-calculator.html", "Macro Split Calculator", "🥗", "Daily protein, carbs & fats for IIFYM"),
            ("calorie-calculator.html", "Calorie Calculator (TDEE)", "🔥", "BMR & daily caloric maintenance"),
            ("bmi-calculator.html", "BMI Calculator", "⚖️", "Body mass index & classification"),
            ("body-fat-calculator.html", "Body Fat Calculator", "📐", "Navy tape body fat & lean mass"),
            ("ideal-weight-calculator.html", "Ideal Body Weight", "🎯", "Devine & Robinson target weight"),
            ("water-intake-calculator.html", "Daily Water Intake", "💧", "Baseline & active hydration needs"),
            ("a1c-calculator.html", "HbA1c to eAG Glucose Sizer", "🩸", "ADAG estimated average glucose mg/dL & IFCC mmol/mol"),
            ("bac-calculator.html", "Blood Alcohol (BAC) Clearance", "🍷", "Widmark pharmacokinetic formula & legal driving limit"),
            ("body-surface-area-calculator.html", "Body Surface Area (Mosteller)", "📐", "Mosteller, Du Bois, Haycock & Boyd multi-formula"),
            ("bsa-calculator.html", "Oncology BSA & Calvert Dosing", "💊", "Chemotherapy mg/m², Calvert carboplatin AUC & CrCl"),
            ("calorie-deficit-calculator.html", "Calorie Deficit & Fat Loss Planner", "🔥", "Dynamic metabolic adaptation, protein & goal timeline"),
            ("calories-burned-calculator.html", "Exercise Calories Burned (METs)", "🏃", "Ainsworth Compendium METs, gross vs net energy & EPOC"),
            ("carbohydrate-intake-calculator.html", "Carbohydrate Intake & Glycogen", "🍞", "ACSM/ISSN endurance g/kg & intra-workout fueling"),
            ("cholesterol-ratio-calculator.html", "Cholesterol Ratio & Castelli Risk", "❤️", "Castelli I & II, Non-HDL & Triglyceride/HDL insulin marker"),
            ("due-date-calculator.html", "Pregnancy Due Date & Gestation", "👶", "Naegele's rule, ACOG ultrasound dating & embryo transfer"),
            ("fat-intake-calculator.html", "Dietary Fat Intake (Grams/Day)", "🥑", "Saturated fat limit, essential omega-3/6 & keto/macro"),
            ("heart-rate-zone-calculator.html", "Heart Rate Zone (Karvonen HRR)", "❤️", "5 cardiovascular training zones & Zone 2 FatMax"),
            ("lean-body-mass-calculator.html", "Lean Body Mass (Boer & James)", "💪", "Boer, James & Hume equations + normalized FFMI limit"),
            ("max-heart-rate-calculator.html", "Max Heart Rate (Tanaka & Gulati)", "🫀", "Tanaka, Gellish, Gulati female-specific & Fox HRmax"),
            ("met-calculator.html", "METs & Activity Caloric Burn", "⚡", "Compendium MET-minutes, VO2 uptake & WHO guidelines"),
            ("ovulation-calculator.html", "Ovulation & Fertile Window", "🌸", "Ogino-Knaus rhythm method, luteal phase & LH surge"),
            ("pregnancy-weight-gain-calculator.html", "Pregnancy Weight Gain (IOM/ACOG)", "🤰", "Pre-pregnancy BMI targets, weekly rates & twin curves"),
            ("protein-intake-calculator.html", "Protein Intake (ISSN/DRI Optimum)", "🥩", "Daily protein requirements for athletes, hypertrophy & clinical cut"),
            ("sleep-calculator.html", "Sleep Cycle (90-Min REM Ultradian)", "🌙", "Sleep onset latency, 90-min REM ultradian cycles & wake times"),
            ("sodium-intake-calculator.html", "Sodium to Salt & AHA Dietary Cap", "🧂", "Dietary sodium conversion, AHA 1,500mg cap & Na/K balance"),
            ("target-heart-rate-calculator.html", "Target Heart Rate (Karvonen HRR)", "❤️", "Karvonen HRR formula, ACSM cardiovascular zones & VO2max"),
            ("tdee-calculator.html", "TDEE & Calorie Burn (Total Daily)", "🔥", "Total daily energy expenditure, PAL multiplier & BMR components"),
            ("waist-to-height-calculator.html", "Waist-to-Height Ratio (WHtR)", "📏", "Central adiposity screening, Ashwell boundary & cardiometabolic risk"),
            ("waist-to-height-ratio-calculator.html", "Waist-to-Height Ratio Sizer", "📐", "Bariatric WHtR visceral risk evaluation & boundary classification"),
            ("waist-to-hip-ratio-calculator.html", "Waist-to-Hip Ratio (WHR Risk)", "⚖️", "WHO visceral adiposity ratio, android vs gynoid fat distribution"),
            ("one-rep-max-calculator.html", "One Rep Max (1RM)", "🏋️", "Brzycki, Epley & Lombardi 1RM strength formulas"),
            ("vo2-max-calculator.html", "VO2 Max Calculator", "🫀", "Cooper 12-min, Rockport walk & HR ratio aerobic capacity"),
            ("pace-calculator.html", "Running Pace & Race Splits", "⏱️", "min/mi, min/km, 400m track laps & Riegel race predictor"),
            ("treadmill-calorie-calculator.html", "Treadmill Calorie Calculator", "🏃", "ACSM walking & running equations with incline grade"),
            ("stairmaster-calorie-calculator.html", "StairMaster Calorie Calculator", "🪜", "Vertical mechanical work & stepping cadence"),
            ("cycling-calorie-calculator.html", "Cycling Calorie Calculator", "🚴", "Aerodynamic drag, rolling resistance & hill climbing"),
            ("pushup-calorie-calculator.html", "Pushup Calorie Calculator", "💪", "64% bodyweight mechanical stroke & tempo work"),
            ("bench-press-calories-calculator.html", "Bench Press Calories Calculator", "🏋️", "Barbell tonnage work, stroke displacement & EPOC"),
            ("swimming-calorie-calculator.html", "Swimming Calorie Calculator", "🏊", "Freestyle, breaststroke, butterfly & backstroke hydrodynamics"),
            ("stationary-bike-calorie-calculator.html", "Stationary Bike Calorie Calculator", "🚲", "ACSM leg ergometry formulas, mechanical watts & cadence"),
            ("incline-treadmill-calorie-calculator.html", "Incline Treadmill Calorie Calculator", "⛰️", "Steep grade walking, 12-3-30 workout & gravitational work"),
            ("rucking-calorie-calculator.html", "Rucking Calorie Calculator", "🎒", "US Army USARIEM Pandolf load carriage equation"),
            ("jack-daniels-running-calculator.html", "Jack Daniels Running Calculator", "⏱️", "Dr. Jack Daniels VDOT score & training paces (E, M, T, I, R)"),
            ("jumping-jacks-calories-burned-calculator.html", "Jumping Jacks Calories Burned", "⭐", "Ballistic cadence, gravitational displacement & Compendium METs"),
            ("squat-calorie-calculator.html", "Squat Calorie Calculator", "🏋️", "Barbell & bodyweight squat biomechanics, stroke & EPOC"),
            ("sit-up-calorie-calculator.html", "Sit Up Calorie Calculator", "🧘", "Trunk flexion 48% bodyweight displacement & MET standards"),
            ("leg-press-to-squat-calculator.html", "Leg Press to Squat Calculator", "🦵", "45° sled incline vector physics (W·sin 45°) & 1RM conversion"),
            ("cycling-watt-calorie-calculator.html", "Cycling Watt Calorie Calculator", "⚡", "Direct power meter kJ to kilocalories & 21.5% gross efficiency"),
            ("running-calorie-calculator.html", "Running Calorie Calculator", "🏃", "Margaria cost of transport (1.0 kcal/kg/km) & ACSM running"),
            ("rowing-machine-calorie-calculator.html", "Rowing Machine Calorie Calculator", "🚣", "Concept2 PM5 physics, 500m split pace & Watts formula"),
            ("peloton-calorie-burn-calculator.html", "Peloton Calorie Burn Calculator", "🚴", "Peloton Total Output (kJ), resistance/cadence & HR correction"),
            ("elliptical-calorie-calculator.html", "Elliptical Calorie Calculator", "🏃", "Closed-chain stride, dual-action arm poles & console correction"),
            ("ftp-calculator.html", "FTP Calculator (Cycling)", "⚡", "Functional Threshold Power, 20-min 0.95 factor & 7 Coggan zones"),
            ("elliptical-to-running-conversion-calculator.html", "Elliptical to Running Conversion", "🔄", "Cross-training cardio conversion, cadence & miles equivalence"),
            ("army-body-fat-calculator.html", "Army Body Fat Calculator", "🪖", "Official US Army AR 600-9 circumference tape test formula"),
            ("starbucks-calories-calculator.html", "Starbucks Calories Calculator", "☕", "Nutritional builder, cup sizes, milk choices & syrup pumps"),
        ]
    },
    "finance": {
        "name": "Finance & Investment",
        "icon": "🏦",
        "hub": "finance.html",
        "tools": [
            ("rule-of-72-calculator.html", "Rule of 72 Doubling Time", "📈", "Investment doubling & tripling horizon"),
            ("car-loan-calculator.html", "Car Loan Financing", "🚗", "Auto loan payments & trade-in tax"),
            ("roi-calculator.html", "ROI & Annualized CAGR", "📊", "Net capital gain & geometric CAGR"),
            ("loan-emi-calculator.html", "Loan EMI Calculator", "💳", "Monthly payment & interest split"),
            ("mortgage-calculator.html", "Mortgage & PITI", "🏡", "Monthly payment, escrow & amortization"),
            ("compound-interest-calculator.html", "Compound Interest", "📈", "Wealth growth with deposits"),
            ("simple-interest-calculator.html", "Simple Interest", "💵", "Linear interest & maturity sum"),
            ("salary-calculator.html", "Salary & Paycheck", "💼", "Hourly, monthly & annual pay"),
            ("discount-calculator.html", "Discount & Sale", "🏷️", "Net savings, coupons & sales tax"),
            ("tip-calculator.html", "Tip & Bill Splitter", "🍽️", "Dining gratuity & party bill split"),
            ("amortization-schedule-calculator.html", "Loan Amortization Schedule", "📅", "Monthly principal vs interest & extra payment savings"),
            ("apr-apy-calculator.html", "APR to APY Compounding Converter", "📈", "Nominal rate to effective annual percentage yield"),
            ("break-even-calculator.html", "Break-Even Point (Units & Sales)", "⚖️", "Fixed costs, contribution margin & margin of safety"),
            ("capital-gains-calculator.html", "Capital Gains Tax (Short & Long)", "🏛️", "0%, 15%, 20% brackets, NIIT 3.8% & net take-home"),
            ("cd-calculator.html", "Certificate of Deposit (CD) Yield", "🏦", "Compound interest, APY & early withdrawal penalty"),
            ("credit-card-payoff-calculator.html", "Credit Card Payoff (Debt Freedom)", "💳", "Minimum payment trap vs fixed accelerated payoff"),
            ("debt-to-income-calculator.html", "Debt-to-Income (DTI) Ratios", "🏡", "Front-end housing & back-end total debt Fannie Mae sizer"),
            ("down-payment-calculator.html", "Down Payment & LTV Sizer", "🏡", "Home down payment %, LTV ratio & PMI elimination"),
            ("emergency-fund-calculator.html", "Emergency Fund (3-6 Months)", "🛡️", "Bare-bones survival expenses & liquid cash safety net"),
            ("inflation-calculator.html", "Inflation & Purchasing Power", "📉", "Future equivalent cost & purchasing power erosion"),
            ("net-salary-calculator.html", "Net Salary & Take-Home Pay", "💼", "Gross to net paycheck, federal, FICA & state tax"),
            ("net-worth-calculator.html", "Personal Net Worth & Solvency", "🏛️", "Personal balance sheet, liquid net worth & debt ratio"),
            ("sales-tax-calculator.html", "Sales Tax & Reverse Pre-Tax", "🏷️", "Combined state & local rate + gross receipt extraction"),
            ("savings-calculator.html", "Compound Savings Growth", "📈", "Initial deposit + monthly contributions compounder"),
            ("savings-goal-calculator.html", "Savings Goal & Target Timeline", "🎯", "Target capital balance, monthly deposit & inflation offset"),
            ("markup-calculator.html", "Markup & Margin Calculator", "🏷️", "Cost-plus pricing markup percentage & gross profit margin"),
            ("smoking-cost-calculator.html", "Smoking Cost & Savings Compounder", "🚭", "Lifetime financial expenditure of tobacco & compound growth"),
            ("retirement-calculator.html", "Retirement Nest Egg & 4% Rule", "🏖️", "FIRE movement corpus, safe withdrawal rate & horizon"),
            ("overtime-calculator.html", "Overtime Pay (1.5x & Double Time)", "⏱️", "FLSA time-and-a-half, weighted average rate & holiday pay"),
            ("time-card-calculator.html", "Time Card & Bi-Weekly Hours", "🕒", "Punch-clock shift hours, lunch deductions & gross wages"),
        ]
    },
    "math": {
        "name": "Mathematics & Utilities",
        "icon": "🔢",
        "hub": "math.html",
        "tools": [
            ("percentage-calculator.html", "Percentage Calculator", "🔢", "Percent of, increase & decrease"),
            ("age-calculator.html", "Exact Age Calculator", "🎂", "Years, months, days & total hours"),
            ("gpa-calculator.html", "College & High School GPA", "🎓", "Cumulative 4.0 weighted GPA"),
            ("fraction-calculator.html", "Fraction Calculator", "½", "Add, subtract, multiply & divide"),
            ("ratio-calculator.html", "Ratio & Proportion Sizer", "➗", "Simplify, scale & solve missing parts"),
            ("standard-deviation-calculator.html", "Standard Deviation & Variance", "📊", "Sample (s) & population (σ) deviation"),
            ("gcd-lcm-calculator.html", "GCD & LCM Calculator", "🔢", "Greatest common divisor & least multiple"),
            ("quadratic-equation-calculator.html", "Quadratic Equation Solver", "📐", "Roots via quadratic formula & vertex"),
            ("pythagorean-theorem-calculator.html", "Pythagorean Theorem", "📐", "Right triangle hypotenuse & legs"),
            ("scientific-notation-calculator.html", "Scientific Notation Sizer", "🔬", "Standard scientific form & powers of 10"),
            ("significant-figures-calculator.html", "Significant Figures Sizer", "📐", "Sig fig precision rules & rounding"),
            ("prime-number-calculator.html", "Prime Number Validator", "🔢", "Primality testing, factor trees & cryptanalysis"),
            ("absolute-value-calculator.html", "Absolute Value Calculator", "📏", "Real & complex modulus |x|, distance from origin"),
            ("area-calculator.html", "Area Calculator (2D Geometric)", "📐", "Circles, triangles, trapezoids, polygons & ellipses"),
            ("arithmetic-sequence-calculator.html", "Arithmetic Sequence Sizer", "🔢", "Nth term, common difference (d) & partial sum"),
            ("circle-calculator.html", "Circle Calculator (Radius & Area)", "⭕", "Radius, diameter, circumference & sector area"),
            ("cube-root-calculator.html", "Cube Root Calculator (∛x)", "🧊", "Perfect cubes, real roots & fractional exponents"),
            ("decimal-to-fraction-calculator.html", "Decimal to Fraction Sizer", "½", "Terminating & repeating decimals to lowest terms"),
            ("exponent-calculator.html", "Exponent & Power Calculator", "⚡", "Base raised to power, negative & fractional indices"),
            ("factorial-calculator.html", "Factorial Calculator (n!)", "❗", "Permutations, Stirling approximation & gamma function"),
            ("fraction-to-percent-calculator.html", "Fraction to Percent Converter", "📈", "Rational fractions to exact percentages & steps"),
            ("geometric-sequence-calculator.html", "Geometric Sequence Sizer", "📐", "Common ratio (r), nth term & infinite series sum"),
            ("logarithm-calculator.html", "Logarithm (Log & Ln) Solver", "🪵", "Common log10, natural ln & change-of-base rule"),
            ("long-division-calculator.html", "Long Division with Remainders", "➗", "Step-by-step polynomial & integer long division"),
            ("mean-median-mode-calculator.html", "Mean, Median & Mode Sizer", "📊", "Measures of central tendency, range & outliers"),
            ("midpoint-calculator.html", "Midpoint Formula (2D & 3D)", "📍", "Cartesian midpoint coordinates & line length"),
            ("modulo-calculator.html", "Modulo & Remainder Calculator", "➗", "Modular arithmetic, clock math & congruences"),
            ("nth-root-calculator.html", "Nth Root Calculator (ⁿ√x)", "🌿", "General radical solver, fractional powers & principal roots"),
            ("percent-error-calculator.html", "Percent Error & Variance", "🎯", "Experimental vs theoretical accepted accuracy %"),
            ("percent-to-fraction-calculator.html", "Percent to Fraction Converter", "½", "Percentages to reduced proper/improper fractions"),
            ("percentage-change-calculator.html", "Percentage Change Sizer", "📈", "Relative percentage delta, gain & loss rate"),
            ("factors-calculator.html", "Factors & Divisors Calculator", "🔢", "All positive integer factors, prime factorization tree"),
            ("sum-of-integers-calculator.html", "Sum of Integers (Arithmetic)", "➕", "Gauss summation formula, series sum & consecutive ints"),
            ("triangle-area-calculator.html", "Triangle Area (Heron & Base)", "📐", "Base-height, Heron's formula & SAS trigonometry"),
            ("variance-calculator.html", "Variance Calculator (s² & σ²)", "📊", "Sample and population variance with sum of squares"),
            ("distance-calculator.html", "2D & 3D Distance Calculator", "📏", "Euclidean distance formula between Cartesian coordinates"),
            ("midrange-calculator.html", "Midrange Calculator", "⚖️", "Extreme score midpoint & statistical dispersion summary"),
            ("permutation-combination-calculator.html", "Permutations & Combinations", "🎲", "nPr order-dependent & nCr selection arrangements"),
            ("probability-calculator.html", "Probability Calculator", "🎲", "Single events, independent intersections & Bayes rule"),
            ("proportion-calculator.html", "Direct & Inverse Proportion", "⚖️", "Solve ratios, cross multiplication & unitary scaling"),
            ("quotient-and-remainder-calculator.html", "Quotient & Remainder Division", "➗", "Euclidean division theorem with integer remainders"),
            ("rounding-calculator.html", "Number Rounding Sizer", "🎯", "Round to nearest integer, tenth, hundredth & sig figs"),
            ("square-root-calculator.html", "Square Root Calculator (√x)", "📐", "Principal square roots, surd simplification & steps"),
            ("z-score-calculator.html", "Z-Score & Normal Probability", "📊", "Standard normal distribution, percentile & p-value"),
            ("average-calculator.html", "Average & Mean Sizer", "📊", "Arithmetic mean, weighted average & running total"),
            ("perimeter-calculator.html", "Perimeter Calculator (All Shapes)", "📏", "Boundary perimeter for rectangles, triangles & polygons"),
            ("surface-area-calculator.html", "Surface Area (3D Geometric)", "🧊", "Spheres, cylinders, cones, prisms & cuboids"),
            ("volume-calculator.html", "Volume Calculator (3D Solids)", "📦", "Cubic volume for boxes, cylinders, spheres & pyramids")
        ]
    },
    "engineering": {
        "name": "Electrical & Engineering",
        "icon": "⚡",
        "hub": "engineering.html",
        "tools": [
            ("wire-ampacity-calculator.html", "Wire Ampacity (NEC 310.16)", "⚡", "Allowable copper & aluminium conductor capacity"),
            ("conduit-fill-calculator.html", "Conduit Fill (NEC Ch. 9)", "🔌", "EMT, PVC & RMC allowable wire fill percentages"),
            ("motor-starting-current-calculator.html", "Motor Starting Current", "⚙️", "Locked rotor kVA code letters & inrush current"),
            ("short-circuit-calculator.html", "Short-Circuit (IEC 60909)", "⚡", "Symmetrical fault kA & transformer impedance"),
            ("transformer-sizing-calculator.html", "Transformer Sizing (NEC 450)", "🔌", "kVA load rating, primary & secondary full-load amps"),
            ("cable-sizing-calculator.html", "Cable Sizing (IEC/NEC)", "🔌", "Full load current, derating factors & thermal limit"),
            ("voltage-drop-calculator.html", "Voltage Drop Calculator", "📉", "Single & 3-phase conductor run voltage drop"),
            ("ohms-law-calculator.html", "Ohm's Law Calculator", "⚡", "Voltage, current, resistance & electrical power"),
            ("power-factor-calculator.html", "Power Factor (kW to kVAR)", "⚡", "Apparent kVA, true kW, reactive kVAR & correction"),
            ("parallel-resistor-calculator.html", "Parallel Resistor (Req)", "🎨", "Equivalent resistance for 2 to 6 branch circuits"),
            ("battery-life-calculator.html", "Battery Life & Runtime", "🔋", "Battery discharge duration from mAh & load current"),
            ("resistor-color-code-calculator.html", "Resistor Color Code", "🎨", "4, 5 & 6 band EIA axial resistor color decoding"),
            ("555-timer-calculator.html", "555 Timer Astable & Monostable", "⏱️", "Oscillation frequency, duty cycle & pulse width"),
            ("led-resistor-calculator.html", "LED Series Resistor Calculator", "💡", "Current limiting resistor ohms & dissipation watts"),
            ("capacitive-reactance-calculator.html", "Capacitive Reactance (Xc)", "⚡", "AC capacitance impedance ohms at given frequency"),
            ("inductive-reactance-calculator.html", "Inductive Reactance (Xl)", "⚡", "AC inductor choke impedance ohms at frequency"),
            ("op-amp-gain-calculator.html", "Op-Amp Gain & Inverting/Non-Inv", "🎛️", "Operational amplifier voltage gain ratio & dB"),
            ("three-phase-power-calculator.html", "Three-Phase AC Power (kVA/kW)", "⚡", "Star & delta line-to-line balanced AC active power"),
            ("adc-dac-calculator.html", "ADC & DAC Converter Resolution", "🎛️", "Quantization voltage step, LSB & SNR bit depth"),
            ("antenna-length-calculator.html", "Antenna Length & Resonant Dipole", "📡", "Quarter-wave whip & half-wave dipole physical length"),
            ("battery-short-circuit-current-calculator.html", "Battery Short Circuit (IEC 60896)", "🔋", "Battery bank prospective peak prospective fault current"),
            ("bjt-transistor-calculator.html", "BJT Transistor Bias & Q-Point", "⚡", "Base-emitter voltage, collector current & hFE beta"),
            ("breaker-size-calculator.html", "Breaker Size (NEC 125% Rule)", "🛡️", "Continuous load standard circuit breaker ampacity"),
            ("decibel-calculator.html", "Decibel Calculator (dB, dBm, SPL)", "🔊", "Power ratio, voltage gain dB & sound pressure"),
            ("earth-pit-resistance-calculator.html", "Earth Pit Resistance (IEEE 80)", "🌍", "Ground rod dissipation ohms in varying soil resistivity"),
            ("electrical-power-calculator.html", "Electrical Power & Energy Cost", "💡", "Kilowatt consumption, monthly kWh & utility tariffs"),
            ("microstrip-impedance-calculator.html", "Microstrip Impedance (IPC-2141)", "📡", "PCB trace characteristic impedance Z0 & dielectric"),
            ("resistor-network-calculator.html", "Resistor Network (Delta-Wye)", "⚡", "Complex bridge, ladder & star-delta transformations"),
            ("transformer-turns-ratio-calculator.html", "Transformer Turns Ratio (a)", "🔌", "Voltage transformation ratio, turns count & primary Z"),
            ("aluminium-cable-sizing-calculator.html", "Aluminium Cable Sizing", "🔌", "Aluminium feeder sizing with conductivity derating"),
            ("busbar-sizing-calculator.html", "Busbar Sizing (DIN 43671 / IEC)", "⚡", "Copper & aluminium switchgear busbar thermal capacity"),
            ("cable-sizing-calculator-bs-7671.html", "Cable Sizing (BS 7671 18th Ed)", "🔌", "UK IET Wiring Regulations thermal & voltage sizing"),
            ("cable-sizing-calculator-iec-60364.html", "Cable Sizing (IEC 60364-5-52)", "🔌", "International electrotechnical cable installation rules"),
            ("cable-sizing-installation-method-a.html", "Cable Sizing Method A (Thermal Wall)", "🔌", "Enclosed conduit in thermally insulated walls"),
            ("fault-current-calculator.html", "Fault Current (IEEE 141 / IEC)", "⚡", "Point-to-point infinite bus prospective fault kA"),
            ("filter-calculator.html", "Analog Filter (RC, RL, LC)", "🎛️", "Low-pass, high-pass cutoff frequency & roll-off slope"),
            ("generator-sizing-calculator.html", "Generator Sizing (ISO 8528)", "⚙️", "Standby alternator kVA sizing for inductive motor loads"),
            ("heatsink-calculator.html", "Heatsink Sizing & Thermal", "🌡️", "Semiconductor junction-to-ambient thermal resistance °C/W"),
            ("cable-sizing-installation-method-c.html", "Cable Sizing Method C (Direct Wall)", "🔌", "Surface-mounted direct clipped cable installation"),
            ("cable-sizing-installation-method-e.html", "Cable Sizing Method E (Cable Tray)", "🔌", "Open perforated cable tray free-air ampacity"),
            ("cable-sizing-calculator-nec.html", "Cable Sizing (NEC Table 310.16)", "🔌", "North American National Electrical Code conductor gauge"),
            ("copper-cable-sizing-calculator.html", "Copper Cable Sizing (100% IACS)", "🔌", "Pure annealed electrolytic copper conductor sizing"),
            ("earthing-cable-size-calculator.html", "Earthing Cable Size (IEC 60364)", "🌍", "Adiabatic equation minimum protective earth cross-section"),
            ("kw-to-cable-size-calculator.html", "kW to Cable Size (1 & 3-Phase)", "🔌", "Direct active power rating to required copper gauge"),
            ("single-phase-cable-sizing-calculator.html", "Single Phase Cable Sizing (230V)", "🔌", "Residential 2-wire conductor selection & voltage drop"),
            ("three-phase-cable-sizing-calculator.html", "Three Phase Cable Sizing (400V)", "🔌", "Commercial & industrial 400V/480V distribution feeders"),
            ("wire-gauge-calculator.html", "Wire Gauge (AWG to mm²)", "📏", "American Wire Gauge diameter, circular mils & metric mm²"),
            ("voltage-divider-calculator.html", "Voltage Divider Calculator", "⚡", "Dual resistor potential divider output voltage Vout"),
            ("parallel-resistance-calculator.html", "Parallel Resistance Calculator", "⚡", "Reciprocal formula branch conductor equivalent ohms"),
            ("capacitor-energy-calculator.html", "Capacitor Energy & Pulse Power", "⚡", "Stored joules E = ½CV² & instant discharge wattage"),
            ("resonant-frequency-calculator.html", "LC Resonant Frequency Tank", "📻", "Series & parallel tank circuit resonance f0 in MHz"),
            ("rc-time-constant-calculator.html", "RC Time Constant (τ = R·C)", "⏱️", "Capacitor charging time constant & 63.2% rise voltage"),
            ("rl-time-constant-calculator.html", "RL Time Constant (τ = L/R)", "⏱️", "Inductor charging transient time & decay rate"),
            ("zener-diode-calculator.html", "Zener Diode Shunt Regulator", "⚡", "Zener series ballast resistor & power dissipation watts"),
            ("lm317-calculator.html", "LM317 Adjustable Regulator", "🎛️", "Output voltage Vout from R1/R2 feedback network"),
            ("pcb-trace-width-calculator.html", "PCB Trace Width (IPC-2152)", "📐", "Internal & external copper trace width for ampacity limit"),
            ("lightning-protection-calculator.html", "Lightning Protection (IEC 62305)", "🌩️", "Rolling sphere radius, protection angle & down conductors"),
            ("lumen-lux-calculator.html", "Lumen to Lux Illuminance", "💡", "Luminous flux spread over floor area square meters"),
            ("lumen-method-calculator.html", "Lumen Method Lighting Layout", "💡", "Room cavity ratio, utilization factor & luminaire count"),
            ("motor-parameters-calculator.html", "Motor Parameters & Torque", "⚙️", "Synchronous RPM, slip percentage & mechanical shaft watts"),
            ("buck-boost-converter-calculator.html", "Buck-Boost DC Converter", "⚡", "Switching duty cycle, inductor ripple & output voltage"),
            ("3-phase-power-calculator.html", "3-Phase Power Calculator", "⚡", "Active, reactive & apparent 3-phase electrical loads"),
            ("motor-starter-sizing-calculator.html", "Motor Starter Sizing (AC-3)", "⚙️", "Contactor current rating, thermal overload relay setting"),
            ("nec-load-calculation-calculator.html", "NEC Service Load Calculation", "🏠", "Residential general lighting, small appliances & HVAC"),
            ("neutral-conductor-sizing-calculator.html", "Neutral Conductor Sizing", "🔌", "Unbalanced 3-phase neutral current & triplen harmonics"),
            ("best-engineering-calculator.html", "Best Engineering Solvers Guide", "📚", "Benchmark engineering software formulas & standards"),
            ("cable-sizing-guide.html", "Cable Sizing Standards Handbook", "📖", "IEC, NEC & BS cable selection design methodologies"),
            ("engineering-formulas.html", "Master Engineering Formulas", "📐", "Electrical, mechanical & civil structural formula sheet")
        ]
    },
    "solar": {
        "name": "Solar & Renewable Energy",
        "icon": "☀️",
        "hub": "solar-energy.html",
        "tools": [
            ("solar-panel-sizing-calculator.html", "Solar Panel Sizing & PV Array", "☀️", "Photovoltaic panel count from daily kilowatt-hours"),
            ("solar-battery-bank-calculator.html", "Solar Battery Bank Sizing", "🔋", "Storage capacity kWh & DoD autonomy days"),
            ("solar-inverter-sizing-calculator.html", "Solar Inverter Sizing (kW/kVA)", "⚡", "Continuous running wattage & surge multiplier"),
            ("ev-charging-time-calculator.html", "EV Charging Time & Power", "🔌", "Electric vehicle battery recharge hours & kW level"),
            ("pv-string-sizing-calculator.html", "PV String Sizing (Voc & Vmp)", "☀️", "Temperature-corrected open circuit voltage limits"),
            ("battery-life-calculator.html", "Battery Autonomy Runtime", "🔋", "Deep cycle battery backup duration under load"),
            ("battery-short-circuit-current-calculator.html", "Battery Short Circuit Current", "🔋", "IEC 60896 battery fault current & DC breaker capacity"),
            ("cable-sizing-calculator.html", "DC/AC Cable Sizing", "🔌", "Solar string conductor gauge & thermal ampacity"),
            ("voltage-drop-calculator.html", "Solar Circuit Voltage Drop", "📉", "Minimize DC array line losses & voltage sag"),
            ("electrical-power-calculator.html", "Solar Array Yield & kW Power", "⚡", "Instantaneous power & peak daily kilowatt-hours"),
            ("generator-sizing-calculator.html", "Hybrid Generator Backup", "⚙️", "Off-grid generator sizing & solar blending")
        ]
    },
    "mechanical": {
        "name": "Mechanical & HVAC",
        "icon": "⚙️",
        "hub": "mechanical.html",
        "tools": [
            ("cooling-load-calculator.html", "Cooling Load (HVAC) Sizing", "❄️", "Sensible, latent heat gain & tons of refrigeration"),
            ("pipe-sizing-calculator.html", "Pipe Sizing & Water Flow", "🚰", "Volumetric flow rate, velocity limit & diameter"),
            ("torque-calculator.html", "Torque & Shaft Power", "⚙️", "Rotational mechanical torque from horsepower & RPM"),
            ("pump-head-calculator.html", "Pump Total Dynamic Head (TDH)", "💧", "Static elevation, friction loss & discharge head"),
            ("gear-ratio-calculator.html", "Gear Ratio & Output Speed", "⚙️", "Velocity reduction ratio, pitch diameter & output RPM"),
            ("bolt-torque-calculator.html", "Bolt Torque & Clamp Force", "🔩", "Tightening torque T = K·F·d & proof load safety"),
            ("bearing-life-calculator.html", "Bearing Life L10 Rating (ISO)", "🔄", "Rolling element bearing fatigue hours at speed"),
            ("belt-length-calculator.html", "V-Belt & Flat Belt Length", "⚙️", "Center distance, pulley pitch diameters & contact angle"),
            ("conveyor-belt-speed-calculator.html", "Conveyor Belt Capacity (TPH)", "📦", "Material bulk density, cross-sectional bed & speed"),
            ("cutting-speed-calculator.html", "Machining Cutting Speed & Feed", "⚙️", "Surface meters per min, spindle RPM & tool feed"),
            ("feed-rate-calculator.html", "Milling Feed Rate (mm/min)", "⚙️", "Tooth chip load, cutter flute count & table feed"),
            ("flywheel-energy-calculator.html", "Flywheel Energy & Inertia", "🔄", "Stored kinetic energy, radius of gyration & mass"),
            ("gear-module-calculator.html", "Spur Gear Module & Pitch (ISO)", "⚙️", "Metric gear tooth dimensions, addendum & dedendum"),
            ("heat-exchanger-calculator.html", "Heat Exchanger LMTD & Duty", "🔥", "Log mean temperature difference & heat transfer rate"),
            ("hvac-calculator.html", "HVAC Airflow CFM & Duct Sizer", "❄️", "Room sensible heat ratio & friction rate per 100ft"),
            ("hydraulic-cylinder-calculator.html", "Hydraulic Cylinder Force & Speed", "🚜", "Push/pull piston tonnage & fluid flow requirements"),
            ("hydraulic-cylinder-force-calculator.html", "Hydraulic Cylinder Force Sizer", "🚜", "Direct fluid pressure to extension/retraction force"),
            ("hydraulic-cylinder-speed-calculator.html", "Hydraulic Cylinder Speed", "🚜", "Cycle time seconds from pump GPM & stroke length"),
            ("hydraulic-pump-power-calculator.html", "Hydraulic Pump Drive Power", "⚙️", "Required electric motor drive kW from PSI & flow"),
            ("power-to-torque-calculator.html", "Power to Torque Converter", "⚙️", "Mechanical kW/HP to Newton-meters & foot-pounds"),
            ("psychrometric-calculator.html", "Psychrometric Air Properties", "🌡️", "Dry bulb, wet bulb, relative humidity & dew point"),
            ("pulley-mechanical-advantage-calculator.html", "Pulley Mechanical Advantage", "🏗️", "Rope fall count, tension reduction & lifting effort"),
            ("pulley-rpm-calculator.html", "Pulley Ratio & Driven RPM", "⚙️", "Belt drive pulley speed relationship D1·N1 = D2·N2"),
            ("pump-flow-calculator.html", "Pump Flow Rate & Cavitation", "💧", "Discharge volume capacity & pipe velocity checks"),
            ("reynolds-number-calculator.html", "Reynolds Number (Laminar/Turb)", "🌊", "Fluid flow regime, kinematic viscosity & pipe size"),
            ("shaft-diameter-calculator.html", "Shaft Diameter (ASME Code)", "⚙️", "Torsional shear stress & bending moment combined"),
            ("spring-rate-calculator.html", "Helical Spring Rate & Stiffness", "🌀", "Hooke's constant k from wire diameter & coil count"),
            ("thermal-expansion-calculator.html", "Linear Thermal Expansion (ΔL)", "🌡️", "Expansion coefficient, temperature delta & growth"),
            ("torque-converter.html", "Torque Unit Converter", "🔄", "Nm, ft-lb, in-lb, kgf-m & dyn-cm interconversions"),
            ("torque-to-hp-calculator.html", "Torque to Horsepower Sizer", "🐎", "Engine brake horsepower from dyno torque & RPM"),
            ("projectile-motion-calculator.html", "Projectile Trajectory Motion", "🚀", "Launch angle, max apogee height & flight range"),
            ("factor-of-safety-calculator.html", "Factor of Safety (FoS Stress)", "🛡️", "Yield/ultimate strength vs working service stress"),
            ("lead-screw-calculator.html", "Lead Screw Torque & Thrust", "🔩", "Linear actuator drive torque, pitch lead & friction"),
            ("press-fit-calculator.html", "Interference Press Fit (Hole/Shaft)", "⚙️", "Contact pressure, assembly force & radial interference")
        ]
    },
    "civil": {
        "name": "Civil & Construction",
        "icon": "🏗️",
        "hub": "civil.html",
        "tools": [
            ("concrete-calculator.html", "Concrete Volume (Slab & Footing)", "🏗️", "Cubic yards, bags & premix volume"),
            ("rebar-calculator.html", "Rebar Weight & Grid Spacing", "🔩", "Total steel tonnage, lap splices & bar count"),
            ("beam-deflection-calculator.html", "Beam Deflection & Bending Moment", "🏗️", "Simply supported & cantilever deflection limits"),
            ("retaining-wall-calculator.html", "Retaining Wall (Rankine Ka)", "🧱", "Lateral earth pressure thrust & overturning moment"),
            ("brick-calculator.html", "Brick & Mortar Estimator", "🧱", "Standard modular bricks, mortar volume & wastage"),
            ("asphalt-calculator.html", "Asphalt Tonnage & Paving Area", "🛣️", "Compacted hot mix asphalt metric tonnes & depth"),
            ("rainwater-downpipe-calculator.html", "Rainwater Downpipe Sizing", "🌧️", "Roof catchment area, storm rainfall intensity & gutter"),
            ("block-calculator.html", "Concrete Block (CMU) Estimator", "🧱", "Standard 8x8x16 concrete masonry units & grout"),
            ("drywall-calculator.html", "Drywall Sheet & Mud Estimator", "📐", "Wall & ceiling board count with joint compound"),
            ("excavation-calculator.html", "Excavation & Earthwork Volume", "🚜", "Cut and fill cubic meters with soil swell factor"),
            ("flooring-calculator.html", "Flooring & Tile Coverage", "🪵", "Hardwood, laminate & vinyl plank box calculation"),
            ("footing-size-calculator.html", "Foundation Footing Concrete", "🏗️", "Continuous strip & spread isolated footing yards"),
            ("gravel-calculator.html", "Gravel & Crushed Stone Tonnage", "🪨", "Aggregates weight in tons from trench dimensions"),
            ("paint-calculator.html", "Paint Coverage & Gallons Sizer", "🎨", "Surface square footage, coats & door/window deduct"),
            ("roof-pitch-calculator.html", "Roof Pitch & Slope Rafter", "🏠", "Rise/run pitch multiplier, rafter length & roof area"),
            ("slab-concrete-calculator.html", "Concrete Slab Yardage Sizer", "🏗️", "Driveway, patio & basement in-situ concrete volume"),
            ("slope-calculator.html", "Slope Gradient & Percent Grade", "📐", "Elevation delta, pitch ratio, degrees & percentage"),
            ("soil-gravel-calculator.html", "Topsoil, Sand & Gravel Sizer", "🌱", "Landscaping material bulk cubic yards & tons"),
            ("tile-calculator.html", "Ceramic Tile & Grout Estimator", "🧱", "Floor & wall tile count with grout gap allowance"),
            ("stair-calculator.html", "Stair Riser & Tread Sizer (IBC)", "🪜", "Building code rise/run layout & stringer length"),
            ("stud-wall-calculator.html", "Wood Stud Wall Framing", "🪵", "16-in & 24-in on-center studs, top/sole plates"),
            ("plaster-calculator.html", "Plaster & Rendering Mortar", "🧱", "Cement plaster bags, fine sand volume & thickness"),
            ("water-demand-fixture-units-calculator.html", "Water Demand (Hunter Fixture Units)", "🚰", "WSFU simultaneous peak water flow GPM in buildings"),
            ("wallpaper-calculator.html", "Wallpaper Roll Estimator", "🎨", "Room wall rolls, pattern repeat waste & borders")
        ]
    },
    "chemical": {
        "name": "Chemical & Water Treatment",
        "icon": "🧪",
        "hub": "chemical.html",
        "tools": [
            ("chemical-dosing-calculator.html", "Chemical Dosing Rate (PPM)", "🧪", "Flow rate m³/hr to pure reagent kg/day"),
            ("chlorine-dosing-calculator.html", "Chlorine Dosing & Sodium Hypo", "💧", "Free chlorine residual & bleach dosing stroke"),
            ("alum-dosing-calculator.html", "Alum Coagulant Dosing", "🧪", "Alum mg/L jar test dose to bulk tanker volume"),
            ("boyles-law-calculator.html", "Boyle's Gas Law (P1·V1 = P2·V2)", "🎈", "Isothermal pressure and volume inverse variation"),
            ("calcium-hypochlorite-dosing-calculator.html", "Calcium Hypochlorite 65% Sizer", "🧪", "Granular chlorine powder batch grams & PPM target"),
            ("caustic-soda-dosing-calculator.html", "Caustic Soda (NaOH) Neutralization", "🧪", "pH adjustment alkalinity demand & 50% liquor liters"),
            ("charles-law-calculator.html", "Charles's Law (V1/T1 = V2/T2)", "🔥", "Isobaric gas volume thermal expansion with Kelvin T"),
            ("chlorine-dioxide-dosing-calculator.html", "Chlorine Dioxide (ClO2) Generator", "🧪", "Sodium chlorite precursor feed rate & active oxidant"),
            ("coagulant-dosing-calculator.html", "Water Treatment Coagulant Sizer", "💧", "Jar test optimal dosing for raw water turbidity"),
            ("combined-gas-law-calculator.html", "Combined Gas Law (PV/T)", "💨", "Simultaneous pressure, volume & temperature shifts"),
            ("dilution-calculator.html", "Solution Dilution (C1·V1 = C2·V2)", "🧪", "Stock concentrate dilution to target molarity/PPM"),
            ("gay-lussac-law-calculator.html", "Gay-Lussac's Law (P1/T1 = P2/T2)", "🌡️", "Isochoric gas pressure vs temperature relationship"),
            ("half-life-calculator.html", "Radioactive Half-Life & Decay", "☢️", "Decay constant λ, remaining activity & elapsed half-lives"),
            ("henderson-hasselbalch-calculator.html", "Henderson-Hasselbalch Buffer pH", "🧪", "Acid dissociation pKa, conjugate base/acid ratio"),
            ("hydrazine-dosing-calculator.html", "Hydrazine Boiler Oxygen Scavenger", "🔥", "Dissolved O2 chemical scavenging in steam boilers"),
            ("ideal-gas-law-calculator.html", "Ideal Gas Law (PV = nRT)", "🎈", "Molar volume, universal gas constant R & gas moles"),
            ("lime-dosing-calculator.html", "Hydrated Lime Dosing (Ca(OH)2)", "🧪", "Water softening, carbonate hardness precipitation"),
            ("molar-mass-calculator.html", "Molecular Weight & Molar Mass", "⚖️", "Periodic element atomic weight chemical sum g/mol"),
            ("molarity-calculator.html", "Molarity Calculator (M = mol/L)", "🧪", "Molar concentration from solute grams & volume"),
            ("ph-calculator.html", "pH & Hydronium Ion Sizer", "🧪", "pH = -log[H+] acid-base logarithmic scale"),
            ("ph-poh-calculator.html", "pH to pOH & Hydroxide Ions", "🧪", "Water ion product Kw = 14.0 relationship at 25°C"),
            ("phosphate-dosing-calculator.html", "Phosphate Boiler Corrosion Inhibitor", "🧪", "Congruent phosphate water treatment in drums"),
            ("polymer-dosing-calculator.html", "Flocculant Polymer Dosing", "💧", "Dry powder make-up batch % & flocculation stroke"),
            ("ro-antiscalant-dosing-calculator.html", "RO Membrane Antiscalant Dosing", "💧", "Reverse osmosis scale prevention injection rate"),
            ("sulphuric-acid-dosing-calculator.html", "Sulphuric Acid (H2SO4) Dosing", "🧪", "Alkalinity destruction & cooling tower acid feed"),
            ("titration-calculator.html", "Acid-Base Titration (Ma·Va = Mb·Vb)", "🧪", "Equivalence endpoint neutralization analysis"),
            ("mass-percent-calculator.html", "Mass Percent Concentration (w/w%)", "⚖️", "Solute mass over total solution mass percentage"),
            ("molality-calculator.html", "Molality Calculator (m = mol/kg)", "🧪", "Moles of solute per kilogram of pure solvent"),
            ("moles-calculator.html", "Chemical Moles & Avogadro Number", "⚛️", "Grams to moles via molecular weight & 6.022×10²³"),
            ("normality-calculator.html", "Normality Calculator (N = Eq/L)", "🧪", "Equivalent concentration for redox & acid-base"),
            ("percent-composition-calculator.html", "Percent Composition by Element", "🔬", "Elemental mass percentage in empirical formulas"),
            ("percent-yield-calculator.html", "Percent Chemical Reaction Yield", "🧪", "Actual recovered mass vs theoretical stoich limit"),
            ("theoretical-yield-calculator.html", "Theoretical Stoichiometric Yield", "⚗️", "Limiting reactant stoichiometry & theoretical grams"),
            ("ppm-calculator.html", "PPM to mg/L & Percent Sizer", "💧", "Parts per million, mg/kg & percentage equivalents")
        ]
    },
    "physics": {
        "name": "Physics & Applied Mechanics",
        "icon": "🔭",
        "hub": "physics.html",
        "tools": [
            ("acceleration-calculator.html", "Acceleration & Velocity Sizer", "🏎️", "Newtonian linear acceleration from speed and time"),
            ("angular-velocity-calculator.html", "Angular Velocity & RPM (ω)", "🔄", "Radians per second, rotational speed & linear v"),
            ("centripetal-force-calculator.html", "Centripetal Force (Fc = mv²/r)", "🎡", "Circular curve radial acceleration & force"),
            ("doppler-effect-calculator.html", "Doppler Effect Sound & Light", "🚨", "Observed frequency shift from source & observer speed"),
            ("escape-velocity-calculator.html", "Escape Velocity Calculator", "🚀", "Gravitational escape speed from planetary bodies"),
            ("free-fall-calculator.html", "Free Fall Velocity & Distance", "🍎", "Gravitational drop speed v = gt neglecting drag"),
            ("friction-calculator.html", "Friction Force & Normal Load", "🛷", "Static and kinetic friction force from mu (μ)"),
            ("gravitational-force-calculator.html", "Newton's Gravitational Law (F)", "🌌", "Universal gravitation attraction between masses"),
            ("hookes-law-calculator.html", "Hooke's Law Spring Force (F=kx)", "🌀", "Restoring elastic force from spring displacement"),
            ("kinetic-energy-calculator.html", "Kinetic Energy (KE = ½mv²)", "⚡", "Joules of kinetic mechanical work in moving body"),
            ("photon-energy-calculator.html", "Photon Energy (E = hf)", "💡", "Planck's constant, electromagnetic wave eV & wavelength"),
            ("simple-pendulum-calculator.html", "Simple Pendulum Period (T)", "🕰️", "Small angle oscillation period from arm length & g"),
            ("snells-law-calculator.html", "Snell's Optical Refraction Law", "🔍", "Refractive index n1/n2 & critical total internal angle"),
            ("specific-heat-calculator.html", "Specific Heat & Enthalpy (Q=mcΔT)", "🔥", "Thermal energy joules required to raise mass temp"),
            ("density-calculator.html", "Density, Mass & Volume (ρ = m/V)", "⚖️", "Specific material density kg/m³ and buoyant state"),
            ("pressure-calculator.html", "Hydrostatic Fluid Pressure (P=ρgh)", "🌊", "Column head pressure in Pascals, bar and PSI"),
            ("speed-calculator.html", "Speed, Distance & Time Sizer", "⏱️", "Kinematic velocity v = d/t in mph, km/h & m/s"),
            ("force-calculator.html", "Newton's Second Law Force (F=ma)", "🥊", "Net dynamic force in Newtons from mass & accel"),
            ("momentum-calculator.html", "Linear Momentum (p = mv)", "🎱", "Conserved momentum & kinetic energy in collisions"),
            ("impulse-calculator.html", "Impulse & Force Duration (J=FΔt)", "💥", "Change in momentum produced by impact force"),
            ("potential-energy-calculator.html", "Gravitational Potential Energy (PE)", "⛰️", "Stored positional work PE = mgh in Joules"),
            ("work-power-calculator.html", "Mechanical Work & Power (W=Fd)", "⚙️", "Force over distance work joules & power watts"),
            ("stress-strain-calculator.html", "Stress, Strain & Young's Modulus", "📏", "Engineering tensile stress σ, strain ε & elasticity"),
            ("terminal-velocity-calculator.html", "Terminal Velocity with Drag", "🪂", "Drag coefficient, frontal area & fluid density limit"),
            ("specific-gravity-calculator.html", "Specific Gravity & Relative Density", "💧", "Substance density relative to pure water reference"),
            ("wavelength-calculator.html", "Wavelength & Frequency (λ = c/f)", "📻", "Electromagnetic & acoustic wave speed equations")
        ]
    },
    "fire": {
        "name": "Fire & Life Safety",
        "icon": "🚨",
        "hub": "fire-safety.html",
        "tools": [
            ("smoke-detector-spacing-calculator.html", "Smoke Detector Spacing (NFPA 72)", "🚨", "Room dimensions to 30ft grid layout"),
            ("fire-sprinkler-calculator.html", "Fire Sprinkler Discharge (Q=K√P)", "💦", "Single head water flow in GPM"),
            ("fire-alarm-battery-calculator.html", "Fire Alarm Standby Battery", "🔋", "24-hr quiescent standby + 5-min alarm load"),
            ("hydrant-fire-flow-calculator.html", "Fire Hydrant Flow (NFPA 291)", "🚰", "Pitot tube reading to rated discharge at 20 psi"),
            ("fire-pump-sizing-calculator.html", "Fire Pump Sizing (NFPA 20)", "🚒", "Rated capacity GPM & net pressure boost"),
            ("nac-voltage-drop-calculator.html", "NAC Circuit Voltage Drop (NFPA 72)", "📉", "Notification appliance strobe/horn circuit length"),
            ("strobe-candela-calculator.html", "Strobe Candela Sizing (NFPA 72)", "💡", "Room square footage to wall/ceiling candela cd"),
            ("water-demand-fixture-units-calculator.html", "Building Water Demand", "🚰", "Hunter fixture units peak building water flow"),
            ("lightning-protection-calculator.html", "Lightning Protection Risk", "🌩️", "IEC 62305 risk assessment & rolling sphere"),
            ("pipe-sizing-calculator.html", "Fire Water Pipe Hydraulics", "🚰", "Hazen-Williams friction loss and pipe diameter")
        ]
    },
    "programmer": {
        "name": "Programmer & Networking",
        "icon": "👨‍💻",
        "hub": "programmer.html",
        "tools": [
            ("subnet-calculator.html", "IPv4 Subnet & CIDR Mask Sizer", "🌐", "Network address, usable hosts & broadcast IP"),
            ("number-base-converter.html", "Number Base Converter (Hex/Dec/Bin)", "💻", "Binary, octal, decimal & hexadecimal conversion"),
            ("data-storage-converter.html", "Data Storage Units (KB, MB, GB, TB)", "💾", "Binary GiB (1024) vs decimal GB (1000) drive capacity"),
            ("data-transfer-rate-converter.html", "Network Bandwidth & Transfer Speed", "🚀", "Mbps, Gbps, MB/s & download ETA calculator"),
            ("unix-timestamp-converter.html", "Unix Timestamp & Epoch Converter", "💻", "Seconds/milliseconds to ISO 8601 UTC & local datetime"),
            ("modulo-calculator.html", "Modulo & Remainder Sizer", "➗", "Modular arithmetic, clock math & congruences"),
            ("scientific-notation-calculator.html", "Scientific Notation Sizer", "🔬", "Standard scientific form & powers of 10"),
            ("prime-number-calculator.html", "Prime Number Validator", "🔢", "Primality testing, factor trees & cryptanalysis"),
            ("significant-figures-calculator.html", "Significant Figures Sizer", "📐", "Sig fig precision rules & rounding")
        ]
    },
    "datetime": {
        "name": "Date & Time Utility",
        "icon": "📅",
        "hub": "datetime.html",
        "tools": [
            ("date-difference-calculator.html", "Date Difference & Day Counter", "📅", "Elapsed days, weeks & calendar months between dates"),
            ("age-calculator.html", "Exact Age & Chronology Sizer", "🎂", "Years, months, days, minutes & next birthday countdown"),
            ("hours-calculator.html", "Work Hours & Shift Sizer", "🕒", "Punch time card duration, breaks & overtime"),
            ("week-number-calculator.html", "ISO Week Number Sizer", "📅", "ISO-8601 workweek index & calendar start/end dates"),
            ("add-days-to-date-calculator.html", "Add/Subtract Days to Date", "🗓️", "Future or past target milestone date generator"),
            ("add-time-calculator.html", "Time Duration Adder & Subtractor", "⏱️", "Sum clock hours, minutes & seconds with carry-over"),
            ("business-days-calculator.html", "Business Days & Working Week Sizer", "💼", "Exclude weekends and public holidays between dates"),
            ("countdown-calculator.html", "Milestone Countdown Timer", "⏳", "Live countdown in days, hours, minutes & seconds"),
            ("date-calculator.html", "Universal Calendar Date Sizer", "📅", "Comprehensive calendar math & timeline intervals"),
            ("day-of-week-calculator.html", "Day of the Week (Doomsday Rule)", "🗓️", "Determine day of the week for any historical date"),
            ("day-of-year-calculator.html", "Day of Year & Julian Ordinal", "📆", "Day index (1 to 365/366) and remaining year %"),
            ("decimal-time-calculator.html", "Decimal Time & Fraction of Day", "⏰", "Convert HH:MM:SS to decimal fractional hours"),
            ("leap-year-calculator.html", "Leap Year Checker & Gregorian Rule", "🐸", "Divisibility by 4, 100, and 400 calendar validation"),
            ("months-between-dates-calculator.html", "Months Between Dates Sizer", "📅", "Decimal and integer whole months elapsed between dates"),
            ("quarter-of-year-calculator.html", "Fiscal & Calendar Quarter Sizer", "📊", "Q1, Q2, Q3, Q4 financial boundaries & schedules"),
            ("time-calculator.html", "Time Difference & Interval Sizer", "🕒", "Difference between two clock timestamps in hours/mins"),
            ("time-duration-calculator.html", "Total Duration & Elapsed Time", "⏱️", "Chronological duration across multiple event timestamps"),
            ("weeks-between-dates-calculator.html", "Weeks Between Dates Sizer", "🗓️", "Integer weeks and residual days between dates"),
            ("time-converter.html", "Time Unit & Chronometric Converter", "⏱️", "Seconds, ms, μs, ns, hours, days & years"),
            ("time-zone-converter.html", "Time Zone & World Clock Converter", "🌍", "UTC offsets, daylight saving transitions & meeting planner")
        ]
    },
    "converter": {
        "name": "Universal Unit Converters",
        "icon": "🔄",
        "hub": "converter.html",
        "tools": [
            ("unit-converter.html", "Universal Multi-Unit Converter", "🔄", "Omni-discipline conversion across 20+ dimensions"),
            ("length-converter.html", "Length & Distance Converter", "📏", "Meters, feet, inches, miles, km, nautical & yards"),
            ("weight-converter.html", "Weight & Mass Converter", "⚖️", "Kilograms, pounds, ounces, grams, stones & tons"),
            ("temperature-converter.html", "Temperature Unit Converter", "🌡️", "Celsius, Fahrenheit, Kelvin & Rankine equations"),
            ("area-converter.html", "Area & Land Square Converter", "📐", "Square meters, acres, hectares, sq ft & sq miles"),
            ("volume-converter.html", "Volume & Capacity Converter", "🧪", "Liters, gallons, fluid oz, cubic meters & cups"),
            ("pressure-converter.html", "Pressure Unit Converter", "💨", "PSI, bar, Pascals, atmospheres & mmHg"),
            ("speed-converter.html", "Speed & Velocity Converter", "🏎️", "km/h, mph, m/s, knots & Mach number"),
            ("energy-converter.html", "Energy & Work Converter", "⚡", "Joules, calories, kilowatt-hours, BTU & ft-lbs"),
            ("power-converter.html", "Power Unit Converter", "💡", "Watts, horsepower, kW, BTU/hr & metric PS"),
            ("force-converter.html", "Force Unit Converter", "🥊", "Newtons, pound-force, dynes & kilogram-force"),
            ("data-storage-converter.html", "Data Storage Converter", "💾", "Bytes, KB, MB, GB, TB, PB & mebibytes"),
            ("data-transfer-rate-converter.html", "Data Transfer Rate Converter", "🚀", "bps, Kbps, Mbps, Gbps & byte transfer speed"),
            ("frequency-converter.html", "Frequency & Angular Converter", "📻", "Hertz, kHz, MHz, GHz, RPM & rad/sec"),
            ("flow-rate-converter.html", "Volumetric Flow Rate Converter", "🚰", "m³/hr, L/min, GPM, CFS & cubic ft/min"),
            ("fuel-economy-converter.html", "Fuel Economy & Mileage Converter", "⛽", "MPG (US & UK), L/100km & km/L equations"),
            ("angle-converter.html", "Angle & Direction Converter", "📐", "Degrees, radians, gradians, minutes & seconds"),
            ("density-converter.html", "Density Unit Converter", "⚖️", "kg/m³, g/cm³, lb/cu ft, lb/gal & specific gravity"),
            ("illuminance-converter.html", "Illuminance Lighting Converter", "💡", "Lux, foot-candles, phot & lumens per area"),
            ("thermal-conductivity-converter.html", "Thermal Conductivity Converter", "🔥", "W/m·K, BTU/hr·ft·°F & cal/s·cm·°C"),
            ("viscosity-converter.html", "Viscosity Dynamic & Kinematic", "💧", "Centipoise, Pa·s, centistokes & m²/s"),
            ("cooking-converter.html", "Culinary & Kitchen Converter", "🍳", "Teaspoons, tablespoons, cups, grams & ounces"),
            ("number-base-converter.html", "Number Base Converter", "💻", "Binary, octal, decimal & hexadecimal conversion"),
            ("roman-numeral-converter.html", "Roman Numeral Converter", "🏛️", "Standard Roman numerals (I to MMMCMXCIX) to Arabic"),
            ("time-converter.html", "Time Unit Converter", "⏱️", "Seconds, ms, hours, days, weeks & years"),
            ("time-zone-converter.html", "Time Zone Converter", "🌍", "World clock UTC offsets & regional timezone deltas"),
            ("unix-timestamp-converter.html", "Unix Timestamp Converter", "💻", "Epoch seconds/ms to human ISO 8601 UTC date")
        ]
    }
}

def determine_tool_cat(filename):
    f = filename.lower()
    if any(k in f for k in ["bmi", "calorie", "body-fat", "ideal-weight", "water-intake", "bmr", "macro", "a1c", "bac", "body-surface-area", "bsa", "calorie-deficit", "calories-burned", "carbohydrate", "cholesterol", "due-date", "fat-intake", "heart-rate-zone", "lean-body-mass", "max-heart-rate", "met-calculator", "ovulation", "pregnancy-weight-gain", "protein-intake", "sleep-calculator", "sodium-intake", "target-heart-rate", "tdee", "waist-to-height", "waist-to-hip", "one-rep-max", "vo2-max", "pace", "jack-daniels", "ftp", "elliptical", "stairmaster", "rucking", "starbucks", "swimming", "pushup", "squat", "sit-up", "bench-press", "cycling", "rowing", "peloton", "leg-press", "jumping-jacks"]):
        return "health"
    if any(k in f for k in ["mortgage", "tip", "loan", "compound", "simple-interest", "discount", "salary", "roi", "rule-of-72", "amortization", "apr-apy", "break-even", "capital-gains", "cd-calculator", "credit-card", "debt-to-income", "down-payment", "emergency-fund", "inflation", "net-salary", "net-worth", "sales-tax", "savings", "markup", "smoking-cost", "retirement", "overtime", "time-card"]):
        return "finance"
    if any(k in f for k in ["short-circuit", "transformer", "ohms", "voltage-drop", "resistor", "cable-sizing", "conduit-fill", "motor-starting", "wire-ampacity", "power-factor", "parallel-resistor", "battery-life", "555-timer", "led-resistor", "capacitive-reactance", "inductive-reactance", "op-amp-gain", "three-phase-power", "adc-dac", "antenna-length", "battery-short-circuit", "bjt-transistor", "breaker-size", "decibel", "earth-pit", "electrical-power", "microstrip", "busbar", "fault-current", "filter", "generator", "heatsink", "copper-cable", "earthing", "kw-to-cable", "single-phase", "three-phase", "wire-gauge", "voltage-divider", "parallel-resistance", "capacitor-energy", "resonant-frequency", "rc-time-constant", "rl-time-constant", "zener-diode", "lm317", "pcb-trace-width", "lightning-protection", "lumen-lux", "lumen-method", "motor-parameters", "buck-boost", "3-phase-power", "motor-starter", "nec-load", "neutral-conductor", "best-engineering", "cable-sizing-guide", "engineering-formulas"]):
        return "engineering"
    if any(k in f for k in ["solar", "charging", "pv-string", "ev-charging"]):
        return "solar"
    if any(k in f for k in ["cooling", "pipe", "torque", "pump-head", "gear-ratio", "bolt-torque", "bearing-life", "belt-length", "conveyor-belt", "cutting-speed", "feed-rate", "flywheel", "gear-module", "heat-exchanger", "hvac", "hydraulic-cylinder", "hydraulic-pump", "power-to-torque", "psychrometric", "pulley", "pump-flow", "reynolds-number", "shaft-diameter", "spring-rate", "thermal-expansion", "torque-converter", "torque-to-hp", "projectile", "factor-of-safety", "lead-screw", "press-fit"]):
        return "mechanical"
    if any(k in f for k in ["beam", "retaining", "concrete", "rebar", "brick", "asphalt", "rainwater-downpipe", "block", "drywall", "excavation", "flooring", "footing", "gravel", "paint", "roof-pitch", "slab", "slope", "soil", "tile", "stair", "stud-wall", "plaster", "water-demand", "wallpaper"]):
        return "civil"
    if any(k in f for k in ["chemical", "chlorine", "alum", "boyle", "calcium-hypochlorite", "caustic", "charles", "chlorine-dioxide", "coagulant", "combined-gas", "dilution", "gay-lussac", "half-life", "henderson", "hydrazine", "ideal-gas", "lime-dosing", "molar-mass", "molarity", "ph-calculator", "ph-poh", "phosphate", "polymer", "ro-antiscalant", "sulphuric", "titration", "mass-percent", "molality", "moles-calculator", "normality", "percent-composition", "percent-yield", "theoretical-yield", "ppm-calculator"]):
        return "chemical"
    if any(k in f for k in ["acceleration", "angular-velocity", "centripetal-force", "doppler-effect", "escape-velocity", "free-fall", "friction", "gravitational-force", "hookes-law", "kinetic-energy", "photon-energy", "simple-pendulum", "snells-law", "specific-heat", "density-calculator", "pressure-calculator", "speed-calculator", "force-calculator", "momentum-calculator", "impulse-calculator", "potential-energy", "work-power", "stress-strain", "terminal-velocity", "specific-gravity", "wavelength"]):
        return "physics"
    if any(k in f for k in ["sprinkler", "smoke", "fire-alarm", "hydrant", "fire-pump", "nac", "strobe"]):
        return "fire"
    if "subnet" in f:
        return "programmer"
    if any(k in f for k in ["date-difference", "age", "hours-calculator", "week-number", "add-days-to-date", "add-time", "business-days", "countdown", "date-calculator", "day-of-week", "day-of-year", "decimal-time", "leap-year", "months-between-dates", "quarter-of-year", "time-calculator", "time-duration", "weeks-between-dates"]):
        return "datetime"
    if any(k in f for k in ["unit-converter", "length-converter", "weight-converter", "temperature-converter", "area-converter", "volume-converter", "pressure-converter", "speed-converter", "energy-converter", "power-converter", "force-converter", "data-storage-converter", "data-transfer-rate-converter", "frequency-converter", "flow-rate-converter", "fuel-economy-converter", "angle-converter", "density-converter", "illuminance-converter", "thermal-conductivity-converter", "viscosity-converter", "cooking-converter", "number-base-converter", "roman-numeral-converter", "time-converter", "time-zone", "unix-timestamp"]):
        return "converter"
    if any(k in f for k in ["percentage", "fraction", "ratio", "gpa", "standard-deviation", "gcd-lcm", "quadratic-equation", "pythagorean", "scientific-notation", "significant-figures", "prime-number", "absolute-value", "area-calculator", "arithmetic-sequence", "circle-calculator", "cube-root", "decimal-to-fraction", "exponent", "factorial", "fraction-to-percent", "geometric-sequence", "logarithm", "long-division", "mean-median-mode", "midpoint", "modulo", "nth-root", "square-root", "percent-to-fraction", "percent-error", "rounding", "factors", "sum-of-integers", "triangle-area", "variance", "distance", "midrange", "permutation", "probability", "proportion", "quotient", "z-score", "average", "perimeter", "surface-area", "volume-calculator", "percentage-change"]):
        return "math"
    return "math"

def build_sidebar_html(current_file, cat_key):
    cat_data = CATEGORIES[cat_key]
    available = [t for t in cat_data["tools"] if t[0] != current_file]
    if not available:
        available = cat_data["tools"]

    initial_5 = available[:5]
    items_html = []
    for slug, title, icon, desc in initial_5:
        items_html.append(f'''            <li>
              <a href="{slug}" class="sidebar-tool-item">
                <span class="st-icon">{icon}</span>
                <div class="st-info">
                  <span class="st-title">{title}</span>
                  <span class="st-desc">{desc}</span>
                </div>
                <span class="st-arrow">›</span>
              </a>
            </li>''')

    tools_list = "\n".join(items_html)
    pool_data = [
        {"slug": slug, "title": title, "icon": icon, "desc": desc}
        for slug, title, icon, desc in available
    ]
    json_pool = json.dumps(pool_data, ensure_ascii=False)

    return f'''      <!-- Related Category Sidebar -->
      <aside class="post-sidebar" aria-label="Related Calculators Sidebar">
        <div class="sidebar-widget">
          <div class="sidebar-widget-header">
            <div class="widget-header-title-wrap">
              <span class="widget-icon">{cat_data["icon"]}</span>
              <h3 class="widget-title">Related {cat_data["name"]}</h3>
            </div>
          </div>
          <p class="sidebar-widget-subtitle">Top 5 precision tools in this discipline:</p>
          <ul class="sidebar-tools-list" id="sidebarToolsList">
{tools_list}
          </ul>
          <div class="sidebar-widget-footer">
            <a href="{cat_data["hub"]}" class="sidebar-category-link">View All {cat_data["name"]} ({len(cat_data["tools"])}+) &rarr;</a>
          </div>
          <script type="application/json" class="sidebar-pool-data">
{json_pool}
          </script>
        </div>
      </aside>
      <script>
        if (!window.rotateSidebarTools) {{
          window.rotateSidebarTools = function() {{
            const widget = document.querySelector('.sidebar-widget');
            if (!widget) return;
            const poolScript = widget.querySelector('.sidebar-pool-data');
            const list = widget.querySelector('.sidebar-tools-list');
            if (!poolScript || !list) return;
            try {{
              const pool = JSON.parse(poolScript.textContent);
              const currentPath = window.location.pathname.split('/').pop() || '';
              const available = pool.filter(item => item.slug !== currentPath);
              if (!available.length) return;
              for (let i = available.length - 1; i > 0; i--) {{
                const j = Math.floor(Math.random() * (i + 1));
                [available[i], available[j]] = [available[j], available[i]];
              }}
              const selected = available.slice(0, 5);
              list.innerHTML = selected.map(item => `
                <li>
                  <a href="${{item.slug}}" class="sidebar-tool-item">
                    <span class="st-icon">${{item.icon}}</span>
                    <div class="st-info">
                      <span class="st-title">${{item.title}}</span>
                      <span class="st-desc">${{item.desc}}</span>
                    </div>
                    <span class="st-arrow">›</span>
                  </a>
                </li>
              `).join('');
            }} catch (err) {{
              console.error('Sidebar rotation error:', err);
            }}
          }};
          document.addEventListener('DOMContentLoaded', () => {{
            window.rotateSidebarTools();
          }});
        }}
      </script>'''

def update_all_sidebars():
    category_pages = set([
        "index.html", "404.html", "health.html", "finance.html", "math.html",
        "engineering.html", "solar-energy.html", "mechanical.html", "civil.html",
        "chemical.html", "physics.html", "fire-safety.html", "programmer.html",
        "datetime.html", "converter.html"
    ])

    all_html_files = glob.glob(os.path.join(BASE_DIR, "*.html"))
    tool_files = [f for f in all_html_files if os.path.basename(f) not in category_pages]

    print(f"Applying updated Top 5 Dynamic Sidebars across {len(tool_files)} tool pages...")
    updated_count = 0

    # Pattern for existing sidebar + optional following script
    sidebar_regex = re.compile(
        r'(?:<!--\s*(?:Related Category Sidebar|Post Sidebar)\s*-->\s*)?<aside class="(?:post-sidebar|sidebar-column|converter-sidebar|sidebar)"[^>]*>[\s\S]*?</aside>(?:\s*<script>[\s\S]*?rotateSidebarTools[\s\S]*?</script>)?',
        re.IGNORECASE
    )

    for file_path in tool_files:
        filename = os.path.basename(file_path)
        cat_key = determine_tool_cat(filename)
        new_sidebar = build_sidebar_html(filename, cat_key)

        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        if sidebar_regex.search(content):
            content = sidebar_regex.sub(lambda m: new_sidebar, content)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            updated_count += 1

    print(f"Successfully updated sidebars across {updated_count} tool pages!")

if __name__ == "__main__":
    update_all_sidebars()
