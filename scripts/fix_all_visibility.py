"""
Comprehensive fix for 100% visibility of all 54 tools on index.html and category hubs.
"""

import os
import re
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define all 54 tools categorized accurately
CAT_MAP = {
    "health.html": {
        "title": "Health & Fitness",
        "tools": [
            ("bmi-calculator.html", "BMI Calculator", "⚖️", "Body mass index, WHO classification & prime ratio", "BMI = kg / (m)²"),
            ("calorie-calculator.html", "Calorie Calculator (TDEE)", "🔥", "Basal metabolic rate & daily expenditure", "TDEE = BMR × Activity"),
            ("bmr-calculator.html", "BMR Calculator", "🧬", "Mifflin-St Jeor & Katch-McArdle resting calories", "BMR = 10W + 6.25H - 5A + s"),
            ("macro-calculator.html", "Macro Split Calculator", "🥗", "Daily protein, carbs & fats for IIFYM", "Atwater: 4C - 4P - 9F kcal/g"),
            ("body-fat-calculator.html", "Body Fat Calculator", "📐", "Navy tape body fat & lean mass", "US Navy Circumference Model"),
            ("ideal-weight-calculator.html", "Ideal Body Weight", "🎯", "Devine & Robinson target weight", "IBW = 50kg + 2.3kg/inch"),
            ("water-intake-calculator.html", "Daily Water Intake", "💧", "Baseline & active hydration needs", "Base (35ml/kg) + Exercise"),
            ("a1c-calculator.html", "HbA1c to eAG Glucose Sizer", "🩸", "ADAG estimated average glucose mg/dL & IFCC mmol/mol", "eAG = 28.7·A1C - 46.7 | IFCC = 10.929·(A1C - 2.15)"),
            ("bac-calculator.html", "Blood Alcohol (BAC) Clearance", "🍷", "Widmark pharmacokinetic formula & legal driving limit", "BAC = [A/(r·W)·100] - β·t | β = 0.015%/hr"),
            ("body-surface-area-calculator.html", "Body Surface Area (Mosteller)", "📐", "Mosteller, Du Bois, Haycock & Boyd multi-formula", "BSA = √((H·W)/3600) | CI = CO / BSA"),
            ("bsa-calculator.html", "Oncology BSA & Calvert Dosing", "💊", "Chemotherapy mg/m², Calvert carboplatin AUC & CrCl", "Dose = Target AUC · (GFR + 25) | CrCl Cockcroft-Gault"),
            ("calorie-deficit-calculator.html", "Calorie Deficit & Fat Loss Planner", "🔥", "Dynamic metabolic adaptation, protein & goal timeline", "Deficit = TDEE - Intake | 3500 kcal rule & Hall adaptation"),
            ("calories-burned-calculator.html", "Exercise Calories Burned (METs)", "🏃", "Ainsworth Compendium METs, gross vs net energy & EPOC", "Calories = MET · 3.5 · W(kg) / 200 · Duration"),
            ("carbohydrate-intake-calculator.html", "Carbohydrate Intake & Glycogen", "🍞", "ACSM/ISSN endurance g/kg & intra-workout fueling", "Carbs (g) = Weight (kg) · Factor (3 to 12 g/kg/day)"),
            ("cholesterol-ratio-calculator.html", "Cholesterol Ratio & Castelli Risk", "❤️", "Castelli I & II, Non-HDL & Triglyceride/HDL insulin marker", "CRI-I = TC/HDL | CRI-II = LDL/HDL | TG/HDL"),
            ("due-date-calculator.html", "Pregnancy Due Date & Gestation", "👶", "Naegele's rule, ACOG ultrasound dating & embryo transfer", "EDD = LMP + 1yr - 3mo + 7d + (Cycle - 28d)"),
            ("fat-intake-calculator.html", "Dietary Fat Intake (Grams/Day)", "🥑", "Saturated fat limit, essential omega-3/6 & keto/macro", "Fat (g) = (TDEE × %Fat) / 9 | DRI 20-35% of kcal"),
            ("heart-rate-zone-calculator.html", "Heart Rate Zone (Karvonen HRR)", "❤️", "5 cardiovascular training zones & Zone 2 FatMax", "THR = (HRR × Intensity%) + RHR | HRR = HRmax - RHR"),
            ("lean-body-mass-calculator.html", "Lean Body Mass (Boer & James)", "💪", "Boer, James & Hume equations + normalized FFMI limit", "LBM = 0.407·W + 0.267·H - 19.2 | FFMI Pope ceiling"),
            ("max-heart-rate-calculator.html", "Max Heart Rate (Tanaka & Gulati)", "🫀", "Tanaka, Gellish, Gulati female-specific & Fox HRmax", "HRmax = 208 - 0.7·Age | Gulati: 206 - 0.88·Age"),
            ("met-calculator.html", "METs & Activity Caloric Burn", "⚡", "Compendium MET-minutes, VO2 uptake & WHO guidelines", "Calories = MET · 3.5 · W(kg) / 200 · min | MET-min/wk"),
            ("ovulation-calculator.html", "Ovulation & Fertile Window", "🌸", "Ogino-Knaus rhythm method, luteal phase & LH surge", "Ovulation = Cycle - Luteal | Fertile: [Od - 5, Od]"),
            ("pregnancy-weight-gain-calculator.html", "Pregnancy Weight Gain (IOM/ACOG)", "🤰", "Pre-pregnancy BMI targets, weekly rates & twin curves", "Target GWG per IOM 2009 guidelines by BMI class"),
            ("protein-intake-calculator.html", "Protein Intake (ISSN/DRI Optimum)", "🥩", "Daily protein requirements for athletes, hypertrophy & clinical cut", "DRI: 0.8 g/kg | ISSN: 1.4-2.0 g/kg | Cut: 2.3-3.1 g/kg FFM"),
            ("sleep-calculator.html", "Sleep Cycle (90-Min REM Ultradian)", "🌙", "Sleep onset latency, 90-min REM ultradian cycles & wake times", "Sleep Time = Wake Time - (n × 90 min) - Latency (14 min)"),
            ("sodium-intake-calculator.html", "Sodium to Salt & AHA Dietary Cap", "🧂", "Dietary sodium conversion, AHA 1,500mg cap & Na/K balance", "Salt (NaCl g) = Sodium (mg) × 2.54 ÷ 1000 | AHA Ideal: 1,500 mg"),
            ("target-heart-rate-calculator.html", "Target Heart Rate (Karvonen HRR)", "❤️", "Karvonen HRR formula, ACSM cardiovascular zones & VO2max", "THR = ((HR_max - HR_rest) × Intensity%) + HR_rest"),
            ("tdee-calculator.html", "TDEE & Calorie Burn (Total Daily)", "🔥", "Total daily energy expenditure, PAL multiplier & BMR components", "TDEE = BMR × PAL = BMR + TEF + EAT + NEAT"),
            ("waist-to-height-calculator.html", "Waist-to-Height Ratio (WHtR)", "📏", "Central adiposity screening, Ashwell boundary & cardiometabolic risk", "WHtR = Waist Circumference ÷ Stature Height | Optimal < 0.50"),
            ("waist-to-height-ratio-calculator.html", "Waist-to-Height Ratio Sizer", "📐", "Bariatric WHtR visceral risk evaluation & boundary classification", "WHtR = Waist / Height | Boundary: <0.4 Take Care, 0.5 Ok, >0.6 High"),
            ("waist-to-hip-ratio-calculator.html", "Waist-to-Hip Ratio (WHR Risk)", "⚖️", "WHO visceral adiposity ratio, android vs gynoid fat distribution", "WHR = Waist (cm) ÷ Hip (cm) | WHO High Risk: M > 0.90, F > 0.85"),
        ]
    },
    "finance.html": {
        "title": "Finance & Investment",
        "tools": [
            ("loan-emi-calculator.html", "Loan EMI Calculator", "💳", "Monthly payment & interest split", "EMI = [P·r·(1+r)ⁿ] / [(1+r)ⁿ - 1]"),
            ("car-loan-calculator.html", "Car Loan Financing", "🚗", "Auto loan payments & trade-in tax", "Auto EMI & Sales Tax Credit"),
            ("mortgage-calculator.html", "Mortgage & PITI", "🏡", "Monthly payment, escrow & amortization", "PITI = P&I + Tax + Ins + PMI"),
            ("roi-calculator.html", "ROI & Annualized CAGR", "📊", "Net capital gain & geometric CAGR", "ROI = (Gain - Cost) ÷ Cost"),
            ("rule-of-72-calculator.html", "Rule of 72 Doubling Time", "📈", "Investment doubling & tripling horizon", "Doubling Years ≈ 72 ÷ Return%"),
            ("compound-interest-calculator.html", "Compound Interest", "📈", "Wealth growth with deposits", "A = P(1 + r/n)ⁿᵗ + PMT···"),
            ("simple-interest-calculator.html", "Simple Interest", "💵", "Linear interest & maturity sum", "I = P × R × T / 100"),
            ("salary-calculator.html", "Salary & Paycheck", "💼", "Hourly, monthly & annual pay", "Annual = Hourly × Hours × 52"),
            ("discount-calculator.html", "Discount & Sale", "🏷️", "Net savings, coupons & sales tax", "Price × (1 - d₁) × (1 + tax)"),
            ("tip-calculator.html", "Tip & Bill Splitter", "🍽️", "Dining gratuity & party bill split", "Tip = Subtotal × Tip%"),
            ("amortization-schedule-calculator.html", "Loan Amortization Schedule", "📅", "Monthly principal vs interest & extra payment savings", "M = P·[r(1+r)ⁿ] / [(1+r)ⁿ - 1] | Direct principal reduction"),
            ("apr-apy-calculator.html", "APR to APY Compounding Converter", "📈", "Nominal rate to effective annual percentage yield", "APY = (1 + r/n)ⁿ - 1 | Continuous APY = eʳ - 1"),
            ("break-even-calculator.html", "Break-Even Point (Units & Sales)", "⚖️", "Fixed costs, contribution margin & margin of safety", "Q_BE = FC / (P - V) | R_BE = FC / CMR"),
            ("capital-gains-calculator.html", "Capital Gains Tax (Short & Long)", "🏛️", "0%, 15%, 20% brackets, NIIT 3.8% & net take-home", "Gain = Proceeds - Cost Basis | NIIT on MAGI > $200k"),
            ("cd-calculator.html", "Certificate of Deposit (CD) Yield", "🏦", "Compound interest, APY & early withdrawal penalty", "A = P(1 + r/n)ⁿᵗ | EWP = P · r · (Penalty Mo / 12)"),
            ("credit-card-payoff-calculator.html", "Credit Card Payoff (Debt Freedom)", "💳", "Minimum payment trap vs fixed accelerated payoff", "DPR = APR/365 | Logarithmic payoff months"),
            ("debt-to-income-calculator.html", "Debt-to-Income (DTI) Ratios", "🏡", "Front-end housing & back-end total debt Fannie Mae sizer", "DTI_front = PITI/Income | DTI_back = (PITI+Debts)/Income"),
            ("down-payment-calculator.html", "Down Payment & LTV Sizer", "🏡", "Home down payment %, LTV ratio & PMI elimination", "LTV = Loan / Value | PMI eliminated at ≤ 80% LTV"),
            ("emergency-fund-calculator.html", "Emergency Fund (3-6 Months)", "🛡️", "Bare-bones survival expenses & liquid cash safety net", "Fund = Monthly Essentials × M (3 to 12 months)"),
            ("inflation-calculator.html", "Inflation & Purchasing Power", "📉", "Future equivalent cost & purchasing power erosion", "FV = PV(1+i)ⁿ | Real Return = (r - i)/(1+i)"),
            ("net-salary-calculator.html", "Net Salary & Take-Home Pay", "💼", "Gross to net paycheck, federal, FICA & state tax", "Net = Gross - (Fed + FICA 7.65% + State + PreTax)"),
            ("net-worth-calculator.html", "Personal Net Worth & Solvency", "🏛️", "Personal balance sheet, liquid net worth & debt ratio", "Net Worth = Assets - Liabilities | Liquid NW"),
            ("sales-tax-calculator.html", "Sales Tax & Reverse Pre-Tax", "🏷️", "Combined state & local rate + gross receipt extraction", "Tax = Net × Rate | Pre-Tax = Gross / (1 + Rate)"),
            ("savings-calculator.html", "Compound Savings Growth", "📈", "Initial deposit + monthly contributions compounder", "FV = P(1+r/n)ⁿᵗ + PMT·[((1+r/n)ⁿᵗ - 1)/(r/n)]"),
            ("savings-goal-calculator.html", "Savings Goal Target Sizer", "🎯", "Required monthly contribution to hit wealth target", "PMT = [FV - P(1+r/n)ⁿᵗ] / [((1+r/n)ⁿᵗ - 1)/(r/n)]"),
        ]
    },
    "math.html": {
        "title": "Mathematics & Utilities",
        "tools": [
            ("percentage-calculator.html", "Percentage Calculator", "％", "Portions, discounts & % change", "P = (Value / Total) × 100"),
            ("standard-deviation-calculator.html", "Standard Deviation & Variance", "📊", "Sample (n-1) & population stats", "s = √[ ∑(x - x̄)² ÷ (n - 1) ]"),
            ("fraction-calculator.html", "Fraction Calculator", "➗", "Add, multiply & simplify fractions", "a/b ± c/d = (ad ± bc) / bd"),
            ("ratio-calculator.html", "Ratio Simplifier", "⚖️", "Euclid's GCD ratio reduction", "X = (B × C) / A"),
            ("age-calculator.html", "Exact Age Calculator", "🎂", "Chronological age & day of week", "Gregorian Leap Calendar"),
            ("gpa-calculator.html", "College GPA Calculator", "🎓", "4.0 scale cumulative GPA", "GPA = ∑(Points × Cr) ÷ ∑Cr"),
            ("gcd-lcm-calculator.html", "GCD and LCM Calculator", "🔢", "Euclidean algorithm reduction & prime factorization", "gcd(a, b) = gcd(b, a mod b) | a·b = gcd·lcm"),
            ("quadratic-equation-calculator.html", "Quadratic Equation Calculator", "📐", "Roots x₁ & x₂, discriminant Δ & parabola vertex (h, k)", "x = (-b ± √(b² - 4ac)) / (2a) | Δ = b² - 4ac"),
            ("pythagorean-theorem-calculator.html", "Pythagorean Theorem Calculator", "🔺", "Hypotenuse, perpendicular legs & 3D space diagonal", "a² + b² = c² | d = √(x² + y² + z²)"),
            ("scientific-notation-calculator.html", "Scientific & Engineering Notation", "🔬", "Standard form m × 10ⁿ, engineering notation & SI prefixes", "m × 10ⁿ (1 ≤ |m| < 10) | Engineering n mod 3 = 0"),
            ("significant-figures-calculator.html", "Significant Figures Calculator", "📏", "Sig fig counter, round-to-even & uncertainty propagation", "Multiplication: Min SF | Addition: Min Decimals"),
            ("prime-number-calculator.html", "Prime Number & Factorization Engine", "⚛️", "Prime primality test, divisor count d(n) & prime factor tree", "Unique factorization: n = ∏ p_i^α_i | d(n) = ∏(α_i+1)"),
            ("absolute-value-calculator.html", "Absolute Value Calculator", "📏", "Real modulus |x|, complex magnitude & distance", "|x| = √(x²) | d = |x - y|"),
            ("area-calculator.html", "Geometric Area Calculator", "📐", "2D surface area across polygons, circles & Heron", "Rectangle, Triangle, Circle, Heron & Shoelace"),
            ("arithmetic-sequence-calculator.html", "Arithmetic Sequence Calculator", "🔢", "Nth term an = a1 + (n-1)d & Gauss partial sum Sn", "an = a1 + (n-1)d | Sn = (n/2)(a1 + an)"),
            ("circle-calculator.html", "Circle Calculator", "⭕", "Radius, circumference, area, sector & chord", "C = 2πr | A = πr² | s = rθ | c = 2r·sin(θ/2)"),
            ("cube-root-calculator.html", "Cube Root Calculator", "🧊", "Principal real root, complex roots & Newton-Raphson", "x³ = N | x_{n+1} = ⅓[2x_n + N/x_n²]"),
            ("decimal-to-fraction-calculator.html", "Decimal to Fraction Calculator", "➗", "Terminating & repeating decimals to rational p/q", "p/q reduced via GCD | 10^(k+p)x - 10^k x"),
            ("exponent-calculator.html", "Exponent & Powers Calculator", "⚡", "Powers bⁿ, negative reciprocals & fractional roots", "bᵐ·bⁿ = bᵐ⁺ⁿ | b⁻ⁿ = 1/bⁿ | b^(p/q) = ⁿ√(bᵖ)"),
            ("factorial-calculator.html", "Factorial & Permutation Calculator", "❗", "n!, permutations P(n, r), combinations C(n, r) & Stirling", "n! = ∏ k | P(n,r) = n!/(n-r)! | C(n,r) = n!/[r!(n-r)!]"),
            ("fraction-to-percent-calculator.html", "Fraction to Percent Calculator", "➗", "Proper, improper & mixed numbers to exact percentage", "P = (a/b) × 100% | GCD Euclidean reduction"),
            ("geometric-sequence-calculator.html", "Geometric Sequence & Series Calculator", "📈", "Nth term an = a1·rⁿ⁻¹, finite Sn & infinite S∞", "an = a1·rⁿ⁻¹ | Sn = a1(1-rⁿ)/(1-r) | S∞ = a1/(1-r)"),
            ("logarithm-calculator.html", "Logarithm Calculator (Log, Ln, Log2)", "🪵", "Arbitrary base log_b(x), ln, log10 & change of base", "log_b(x) = ln(x) / ln(b) | b^y = x"),
            ("long-division-calculator.html", "Long Division with Steps & Remainders", "➗", "Quotient Q, remainder R & repeating decimal expansion", "A = B·Q + R (0 ≤ R < B) | DMSB tableau"),
            ("mean-median-mode-calculator.html", "Mean, Median, Mode & Range Calculator", "📊", "Central tendency, multimodal frequencies & skewness", "Mean = ∑x/n | Median | Mode | Range = Max - Min"),
            ("midpoint-calculator.html", "Midpoint & Distance (2D & 3D)", "📍", "2D/3D midpoint, Euclidean distance & vector slope", "M = ((x1+x2)/2, (y1+y2)/2) | d = √(Δx² + Δy²)"),
            ("modulo-calculator.html", "Modulo & Modular Arithmetic Calculator", "🔄", "A mod M, congruence classes, Euclidean quotient & inverse", "A = M·Q + R | a ≡ b (mod m) | Extended Euclidean"),
            ("nth-root-calculator.html", "Nth Root & Radical Solver", "√", "Arbitrary radical index ⁿ√A & Newton-Raphson approximation", "x_{k+1} = (1/n)[(n-1)x_k + A/x_kⁿ⁻¹]"),
            ("square-root-calculator.html", "Square Root Calculator", "√", "Principal square root, Newton-Raphson & radical simplifier", "√x = s | x_{n+1} = ½(x_n + S/x_n)"),
            ("percent-to-fraction-calculator.html", "Percent to Fraction Calculator", "％", "Exact rational fraction, mixed number & GCD reduction", "Fraction = P / 100 = (P/GCD) / (100/GCD)"),
            ("percent-error-calculator.html", "Percent Error & Accuracy", "🎯", "Experimental vs theoretical error, precision & uncertainty", "% Error = (|Experimental - Theoretical| / |Theoretical|) × 100%"),
            ("rounding-calculator.html", "Rounding Calculator", "🔢", "Round to nearest integer, decimals, half-even & sig figs", "Round half-up, half-even (Banker's) & ceiling/floor"),
            ("factors-calculator.html", "Factors & Factor Pairs Calculator", "🔢", "Divisor pairs, prime factorization & aliquot sums", "N mod d = 0 | d(n) = ∏(α_i+1) | σ(n) = ∏(p^(a+1)-1)/(p-1)"),
            ("sum-of-integers-calculator.html", "Sum of Integers & Series Calculator", "∑", "Gauss consecutive sum, squared sums & range summation", "S = n(n+1)/2 | ∑k² = n(n+1)(2n+1)/6"),
            ("triangle-area-calculator.html", "Triangle Area Calculator", "🔺", "Heron's formula, SAS, base-height & Shoelace coordinates", "A = ½bh | A = √[s(s-a)(s-b)(s-c)] | A = ½ab·sin(γ)"),
            ("variance-calculator.html", "Variance Calculator (Sample & Population)", "📊", "Sample s² (n-1), population σ² (N) & deviation table", "s² = ∑(x - x̄)² / (n - 1) | σ² = ∑(x - μ)² / N"),
            ("distance-calculator.html", "Distance Calculator (2D & 3D)", "📍", "Euclidean, Manhattan & Chebyshev coordinate distance", "d = √[(Δx)² + (Δy)² + (Δz)²] | d_M = ∑|Δx_i|"),
            ("midrange-calculator.html", "Midrange & Center of Range", "⚖️", "Midrange (L+S)/2, range L-S & midhinge analysis", "M = (Min + Max) / 2 | Range = Max - Min"),
            ("permutation-combination-calculator.html", "Permutation & Combination (nPr, nCr)", "⚙️", "nPr, nCr, permutations & combinations with repetition", "P = n!/(n-r)! | C = n!/[r!(n-r)!] | Stars & Bars"),
            ("probability-calculator.html", "Probability Calculator (Union, Bayes)", "🎲", "Single events, compound A or B, conditional & Bayes", "P(A∪B) = P(A)+P(B)-P(AB) | P(A|B) = P(B|A)P(A)/P(B)"),
            ("proportion-calculator.html", "Proportion Calculator (Solve for X)", "∷", "Direct & inverse variation, cross-multiplication", "A/B = C/D ⇔ AD = BC | y = kx | y = k/x"),
            ("quotient-and-remainder-calculator.html", "Quotient and Remainder (Divmod)", "➗", "Euclidean integer division, mixed fractions & decimals", "A = B·Q + R (0 ≤ R < |B|) | Python divmod"),
            ("z-score-calculator.html", "Z-Score & Normal Distribution", "⎶", "Standard score, percentiles, normal CDF & p-values", "Z = (x - μ) / σ | Percentile = Φ(z) × 100%"),
            ("average-calculator.html", "Average Calculator (All Means & Weighted)", "📊", "Arithmetic, geometric, harmonic & RMS quadratic means", "HM ≤ GM ≤ AM ≤ RMS | Weighted x̄_w = ∑wx/∑w"),
        ]
    },
    "engineering.html": {
        "title": "Electrical & Power Systems",
        "tools": [
            ("ohms-law-calculator.html", "Ohm's Law Calculator", "⚡", "Voltage, current, power & ohms", "V = I·R | P = V·I = I²R"),
            ("voltage-drop-calculator.html", "Voltage Drop Calculator", "📉", "NEC 3% & 5% copper/aluminum run", "ΔV = (2 or √3) · I · L · ρ / A"),
            ("cable-sizing-calculator.html", "Cable Sizing (IEC/NEC)", "🔌", "IEC/NEC ampacity & derating", "I_tabulated ≥ I_load / (Ca × Cg)"),
            ("wire-ampacity-calculator.html", "Wire Ampacity (NEC 310.16)", "🔌", "Allowable conductor current & derating", "I_adj = I_base × K_temp × K_bundle"),
            ("conduit-fill-calculator.html", "Conduit Fill (NEC Ch. 9)", "🪢", "40% fill rule & wire jam ratio", "Fill % = ∑(A_cond) ÷ A_conduit ≤ 40%"),
            ("motor-starting-current-calculator.html", "Motor Starting Current", "⚙️", "NEMA locked rotor inrush amps", "LRA = (HP × kVA/HP × 1000) ÷ (√3 × V)"),
            ("short-circuit-calculator.html", "Short-Circuit (IEC 60909)", "💥", "Symmetrical fault kA & breaking", "Ik'' = c·Un / (√3·|Zk|)"),
            ("transformer-sizing-calculator.html", "Transformer Sizing (NEC 450)", "⚡", "kVA rating & full-load amps", "FLC = (kVA × 1000) / (√3 × V)"),
            ("power-factor-calculator.html", "Power Factor (kW to kVAR)", "⚡", "Capacitor bank rating & line current savings", "Qc = P × [tan(θ1) - tan(θ2)]"),
            ("parallel-resistor-calculator.html", "Parallel Resistor (Req)", "⚡", "Equivalent resistance & branch current divider", "1/Req = ∑(1/Ri) | Conductance G"),
            ("battery-life-calculator.html", "Battery Life & Runtime", "🔋", "Peukert's law discharge & C-rate runtime", "t = H × (C / IH)^k × DoD"),
            ("resistor-color-code-calculator.html", "Resistor Color Code", "🎨", "4 & 5-band axial resistance", "R = (Digits) × 10ⁿ ± Tol%"),
            ("555-timer-calculator.html", "555 Timer Astable & Monostable", "⏱️", "Frequency, duty cycle & pulse width", "f = 1.44 / ((R1 + 2R2) × C)"),
            ("led-resistor-calculator.html", "LED Series Resistor Calculator", "💡", "Current limiting & wattage rating", "R = (Vs - Vf) / If | P = I²R"),
            ("capacitive-reactance-calculator.html", "Capacitive Reactance (Xc)", "⚡", "AC capacitor impedance & phase shift", "Xc = 1 / (2π · f · C)"),
            ("inductive-reactance-calculator.html", "Inductive Reactance (Xl)", "⚡", "AC inductor reactance & back-EMF", "Xl = 2π · f · L"),
            ("op-amp-gain-calculator.html", "Op-Amp Gain & Inverting/Non-Inv", "📈", "Closed loop gain, bandwidth & dB", "Av = -Rf/Rin | 1 + Rf/Rin"),
            ("three-phase-power-calculator.html", "Three-Phase AC Power (kVA/kW)", "⚡", "Real, reactive & apparent 3-phase power", "P = √3 × V_LL × I_L × cos(θ)"),
            ("adc-dac-calculator.html", "ADC & DAC Converter Resolution", "🎛️", "Quantization LSB, SQNR & ENOB", "LSB = V_ref / 2^N | SQNR = 6.02N + 1.76"),
            ("antenna-length-calculator.html", "Antenna Length & Resonant Dipole", "📡", "Half-wave & quarter-wave velocity factor", "L = 142.65·k / f (MHz) | 468/f"),
            ("battery-short-circuit-current-calculator.html", "Battery Short Circuit (IEC 60896)", "🔋", "DC prospective fault current & arc flash", "I_sc = U_n / R_total | Doan Arc Flash"),
            ("bjt-transistor-calculator.html", "BJT Transistor Bias & Q-Point", "⚡", "Voltage divider bias & saturation limit", "I_B = (V_TH - V_BE) / [R_TH + (β+1)R_E]"),
            ("breaker-size-calculator.html", "Breaker Size (NEC 125% Rule)", "🛡️", "Continuous load sizing & trip curves", "I_min = 1.25·I_cont + I_noncont | NEC 240.6"),
            ("decibel-calculator.html", "Decibel Calculator (dB, dBm, SPL)", "🔊", "Power, voltage, dBm to Watts & dB SPL", "dB = 10·log(P1/P0) | 20·log(V1/V0)"),
            ("earth-pit-resistance-calculator.html", "Earth Pit Resistance (IEEE 80)", "🌍", "Grounding rod dissipation & soil resistivity", "R = (ρ/2πL)·[ln(8L/d) - 1]"),
            ("electrical-power-calculator.html", "Electrical Power & Energy Cost", "⚡", "Real, reactive, apparent & kWh cost", "P = VI·cos(θ) | P_3φ = √3·V_LL·I_L·PF"),
            ("microstrip-impedance-calculator.html", "Microstrip Impedance (IPC-2141)", "📡", "Single-ended & differential Z0", "Z0 = [87 / √(εr + 1.41)] · ln[5.98h / (0.8w + t)]"),
            ("resistor-network-calculator.html", "Resistor Network (Delta-Wye & Ladder)", "⚡", "Δ-Y Kennelly transform & R-2R ladder", "R_A = (R1·R2) / (R1+R2+R3) | V_out = V_ref·(D/2^N)"),
            ("transformer-turns-ratio-calculator.html", "Transformer Turns Ratio (a)", "⚡", "Voltage, current & impedance matching", "a = Np/Ns = Vp/Vs = Is/Ip = √(Zp/Zs)"),
            ("aluminium-cable-sizing-calculator.html", "Aluminium Cable Sizing (NEC/IEC)", "🔌", "AA-8000 ampacity, lugs & AL/CU area", "A_Al = 1.64 × A_Cu | Dual Rated AL9CU"),
            ("busbar-sizing-calculator.html", "Busbar Sizing (DIN 43671 / IEC)", "⚡", "Continuous ampacity & short-circuit force", "I = C · A^0.61 · √ΔT | F = (μ0/2π)·(i_p²/s)·L"),
            ("cable-sizing-calculator-bs-7671.html", "Cable Sizing (BS 7671 18th Ed)", "🔌", "UK wiring regulations & mV/A/m drop", "Ib ≤ In ≤ Iz | It ≥ In / (Ca·Cg·Cc·Ci)"),
            ("cable-sizing-calculator-iec-60364.html", "Cable Sizing (IEC 60364-5-52)", "🔌", "International LV dimensioning & adiabatic", "Ib ≤ In ≤ Iz | S ≥ √(Isc²·t) / k"),
            ("cable-sizing-installation-method-a.html", "Cable Sizing Method A (Insulated Wall)", "🔌", "A1 & A2 conduit in cavity derating", "Iz = I0 · Ca · Cg · Ci | High thermal penalty"),
            ("fault-current-calculator.html", "Fault Current (IEEE 141 / IEC)", "💥", "Transformer secondary & point-to-point kA", "I_sc = I_FLA / (%Z/100) | I_down = I_up / (1+f)"),
            ("filter-calculator.html", "Analog Filter (RC, RL, LC)", "🎛️", "Cutoff frequency, dB gain & phase angle", "fc = 1 / (2πRC) | fc = R / (2πL) | 1 / (2π√LC)"),
            ("generator-sizing-calculator.html", "Generator Sizing (ISO 8528)", "⚡", "Standby kVA, motor inrush & altitude derate", "kVA = kW/PF | SkVA = HP×6.0 | k_env derate"),
            ("heatsink-calculator.html", "Heatsink Sizing & Thermal", "❄️", "Thermal resistance θ_sa & junction temp", "θ_sa ≤ (Tj_max - Ta)/Pd - (θ_jc + θ_cs)"),
            ("cable-sizing-installation-method-c.html", "Cable Sizing Method C (Clipped Direct)", "🔌", "Surface clipped to masonry ampacity", "Iz = I0 · Ca · Cg | High convective cooling"),
            ("cable-sizing-installation-method-e.html", "Cable Sizing Method E (Cable Tray)", "🔌", "Perforated tray & ladder rack in free air", "Iz = I0 · Ca · Cg | 360° natural ventilation"),
            ("cable-sizing-calculator-nec.html", "Cable Sizing (NEC Table 310.16)", "🔌", "125% continuous load & conduit fill derate", "MCA = 1.25·I_cont + I_noncont | NEC 110.14(C)"),
            ("copper-cable-sizing-calculator.html", "Copper Cable Sizing (100% IACS)", "🔌", "Pure ETP Cu ampacity & I²R loss cost", "R_T = R_20·[1 + α(T-20)] | P_loss = 3·I²R"),
            ("earthing-cable-size-calculator.html", "Earthing & Grounding Cable Size", "⚡", "IEC 60364-5-54 adiabatic equation & k-factor", "S = √(I²·t) / k | BS 7671 Table 54.7"),
            ("kw-to-cable-size-calculator.html", "kW to Cable Size (1-Phase & 3-Phase)", "🔌", "Active kW to full-load current & mV/A/m", "I = kW×1000 / (√3·V·PF) | 125% continuous load"),
            ("single-phase-cable-sizing-calculator.html", "Single Phase Cable Sizing (230V/120V)", "🔌", "2-wire loop drop & radial/ring circuit", "ΔV = 2·I·L·R | 3% lighting & 5% power limit"),
            ("three-phase-cable-sizing-calculator.html", "Three Phase Cable Sizing (400V/480V)", "⚡", "Line-to-line balanced vector drop & method E", "ΔV = √3·I·L·(R·cosφ + X·sinφ) | IEC 60364-5-52"),
            ("wire-gauge-calculator.html", "Wire Gauge (AWG to mm² Metric)", "📏", "ASTM B258 logarithmic AWG scale & circular mils", "d_n = 0.005 × 92^((36-n)/39) in | kcmil conversion"),
        ]
    },
    "solar-energy.html": {
        "title": "Solar & Renewable Energy",
        "tools": [
            ("solar-panel-sizing-calculator.html", "Solar Panel & Array Sizing", "☀️", "Array watts & peak sun hours", "PV (W) = Daily Wh / (PSH × η)"),
            ("solar-battery-bank-calculator.html", "Solar Battery Bank Sizing", "🔋", "Storage Ah & kWh for autonomy", "Storage Ah = Wh ÷ (V × DoD × η)"),
            ("solar-inverter-sizing-calculator.html", "Solar Inverter Sizing", "⚡", "Continuous kVA & surge capacity", "Inverter VA = Peak Continuous Load × 1.25"),
            ("pv-string-sizing-calculator.html", "PV String Sizing (NEC 690)", "☀️", "MPPT voltage limits & module temperature", "N_max = ⌊V_max / Voc_cold⌋"),
            ("ev-charging-time-calculator.html", "EV Charging Time & Power", "🔌", "Levels 1, 2 & DC Fast charge time", "Time (hrs) = Battery (kWh) ÷ Net kW"),
            ("ev-charging-circuit-calculator.html", "EV Charging Circuit (NEC 625)", "🔌", "Continuous load 125%, breaker & AWG wire", "I_min = 1.25 × I_EVSE | NEC 625.42"),
        ]
    },
    "mechanical.html": {
        "title": "Mechanical & HVAC",
        "tools": [
            ("bolt-torque-calculator.html", "Bolt Torque & Preload", "🔩", "Tightening torque & clamp load preload", "T = K · D · Fp (VDI 2230)"),
            ("bearing-life-calculator.html", "Bearing Life (ISO 281)", "⚙️", "L10 & L10h rating life in revs & hours", "L10 = (C / P)^p × 10⁶ revs"),
            ("cooling-load-calculator.html", "Cooling Load (HVAC) Sizing", "❄️", "Sensible & latent heat in BTU/hr", "Q = 1.08 × CFM × ΔT"),
            ("pipe-sizing-calculator.html", "Pipe Sizing & Water Flow", "🚰", "Internal diameter & friction loss", "Q = A × V | Darcy-Weisbach"),
            ("pump-head-calculator.html", "Pump Head (TDH & Flow)", "🌊", "Total dynamic head & motor BHP", "TDH = Static Head + Friction Head"),
            ("gear-ratio-calculator.html", "Gear Ratio & Speed", "⚙️", "Velocity reduction & torque ratio", "Ratio = Driven Teeth ÷ Driving Teeth"),
            ("torque-calculator.html", "Torque & Shaft Power", "⚙️", "Rotational torque N·m & kW/HP", "P = (2π × N × T) ÷ 60000"),
            ("belt-length-calculator.html", "Belt Length (Open & Crossed Pulley)", "⚙️", "Pitch length, center distance & wrap angle", "L ≈ 2C + (π/2)(D+d) + (D-d)²/(4C) | ISO 5296"),
            ("conveyor-belt-speed-calculator.html", "Conveyor Belt Speed & Tonnage", "🏭", "Linear velocity, drum RPM & CEMA capacity", "v = π·Deff·N / 60 | Q = 3600·A·v·ρ (t/h)"),
            ("cutting-speed-calculator.html", "Cutting Speed & Spindle RPM", "⚙️", "Linear surface speed Vc & Taylor tool life", "Vc = π·D·N / 1000 | Vc·T^n = C (ISO 3685)"),
            ("feed-rate-calculator.html", "CNC Feed Rate & Chip Load", "⚙️", "Table feed vf, radial chip thinning & MRR", "vf = fz · z · N | MRR = ap · ae · vf / 1000"),
            ("flywheel-energy-calculator.html", "Flywheel Kinetic Energy & Stress", "🔄", "Stored energy, moment of inertia & hoop stress", "Ek = 0.5·I·ω² | σ_hoop = ρ·v² (ASME VIII)"),
            ("gear-module-calculator.html", "Gear Module & Pitch Geometry", "⚙️", "Metric module m, diametral pitch DP & tip dia", "m = d / z | da = m(z+2) | a = m(z1+z2)/2"),
            ("heat-exchanger-calculator.html", "Heat Exchanger (LMTD & NTU Area)", "🌡️", "Thermal duty, counter-flow LMTD & TEMA area", "Q = U·A·ΔTm | LMTD = (ΔT1 - ΔT2)/ln(ΔT1/ΔT2)"),
            ("hvac-calculator.html", "HVAC Sizing & Cooling Tonnage", "❄️", "Sensible, latent dehumidification & supply CFM", "Qs = 1.08·CFM·ΔT | 1 Ton = 12,000 BTU/hr"),
            ("hydraulic-cylinder-calculator.html", "Hydraulic Cylinder Sizing (ISO 6020)", "🚜", "Push/pull force, fluid velocity & Euler buckling", "F_push = p·(π/4)·D² | F_pull = p·(π/4)·(D²-d²)"),
            ("hydraulic-cylinder-force-calculator.html", "Hydraulic Cylinder Net Force (ISO 3320)", "🚜", "Net thrust, backpressure & seal friction drag", "F_net = (p1·A1 - p2·A2)·η_m - F_friction"),
            ("hydraulic-cylinder-speed-calculator.html", "Hydraulic Cylinder Speed & Flow", "🚜", "Piston velocity, cycle time & regenerative boost", "v = Q / A | v_regen = Q_pump / A_rod"),
            ("hydraulic-pump-power-calculator.html", "Hydraulic Pump Power (ISO 4409)", "⚙️", "Motor drive power, displacement & shaft torque", "P_kW = (p·Q) / (600·η_t) | T = (V_g·Δp)/(20π·η_hm)"),
            ("power-to-torque-calculator.html", "Power to Torque & Shaft Sizing", "⚙️", "Rotary torque, gear ratio & shaft shear stress", "T = (9548.8·P) / N | d = ∛(16·T / π·τ)"),
            ("psychrometric-calculator.html", "Psychrometric & Moist Air (ASHRAE)", "🌡️", "Dew point, humidity ratio W, wet bulb & enthalpy", "W = 0.62198·Pw / (Patm - Pw) | h = 1.006·T + W·(2501+1.86T)"),
            ("pulley-mechanical-advantage-calculator.html", "Pulley Mechanical Advantage (CMAA 70)", "🏗️", "Block & tackle IMA, AMA & reeving friction", "IMA = n | AMA = n·η_total | η_total = (1-η^n)/(n(1-η))"),
            ("pulley-rpm-calculator.html", "Pulley RPM & Belt Speed (ISO 5296)", "⚙️", "Rotational speed, ratio, belt velocity & slip", "N1·D1 = N2·D2 | N2 = N1·(D1/D2)·(1 - s/100)"),
            ("pump-flow-calculator.html", "Pump Flow Rate & Velocity", "🌊", "Pipe bore velocity, m³/h, GPM & VFD scaling", "Q = A·v | D = √(4Q / πv) | Q1/Q2 = N1/N2"),
            ("reynolds-number-calculator.html", "Reynolds Number (Moody & Swamee-Jain)", "🧪", "Laminar, transition & turbulent flow regime", "Re = (ρ·v·D)/μ | f = 0.25 / [log10(ε/3.7D + 5.74/Re^0.9)]²"),
            ("shaft-diameter-calculator.html", "Shaft Diameter (ASME B106.1M)", "⚙️", "Combined torsion, bending moment & keyway de-rate", "d = ∛[ (16/πτ)·√((Km·M)² + (Kt·T)²) ] | τ_kw = 0.75·τ"),
            ("spring-rate-calculator.html", "Helical Spring Rate (SMI / ASTM A228)", "🌀", "Spring constant k, Wahl stress factor & solid height", "k = (G·d⁴)/(8·D³·na) | Kw = (4C-1)/(4C-4) + 0.615/C"),
            ("thermal-expansion-calculator.html", "Thermal Expansion & Pipe Stress", "🌡️", "Linear growth ΔL, volumetric ΔV & ASME loop leg", "ΔL = L0·α·ΔT | σ = E·α·ΔT | Lleg ≈ 0.043·√(D·ΔL)"),
            ("torque-converter.html", "Torque Converter Sizing (SAE J643)", "🚗", "Stall torque ratio, speed ratio & K-factor", "TR = T_turb/T_pump | SR = N_turb/N_pump | η = TR·SR"),
            ("torque-to-hp-calculator.html", "Torque to HP & BMEP Converter", "🏎️", "Brake horsepower, kilowatts & 4-stroke BMEP", "HP = (T·RPM) / 5252 | BMEP = (4π·T)/(Vd·100)"),
            ("projectile-motion-calculator.html", "Projectile Motion Trajectory", "🚀", "Apex height, time of flight, range & impact velocity", "H = h0 + (v0·sinθ)²/(2g) | R = v0·cosθ·T"),
        ]
    },
    "civil.html": {
        "title": "Civil & Construction",
        "tools": [
            ("concrete-calculator.html", "Concrete Slab, Footing & Column", "🏗️", "Wet concrete m³ & cement bags", "Volume = L × W × H (1.54 Bulking)"),
            ("rebar-calculator.html", "Rebar Weight & Grid Spacing", "🔩", "Cut bar counts & linear mass kg/lbs", "Mass = (d² ÷ 162) × L"),
            ("brick-calculator.html", "Brick & Masonry Calculator", "🧱", "ASTM modular brick & mortar bags", "Bricks = Area × Multiplier × (1 + Waste)"),
            ("asphalt-calculator.html", "Asphalt Paving & Tonnage", "🛣️", "HMA road tonnage & base course", "Tons = Volume × Density ÷ 2,000 lbs"),
            ("beam-deflection-calculator.html", "Beam Deflection & Moments", "📐", "AISC 360 deflection & moment", "δmax = 5wL⁴ / 384EI"),
            ("retaining-wall-calculator.html", "Retaining Wall Stability", "🧱", "Rankine earth pressure & overturning", "Pa = 0.5 × γ × H² × Ka"),
            ("rainwater-downpipe-calculator.html", "Rainwater Downpipe Sizing (BS EN 12056)", "🌧️", "Roof catchment area, storm runoff L/s & leader diameter", "Ae = L·(W + H/2) | Q = (r·Ae·C)/3600 | Annular flow"),
            ("beam-calculator.html", "Beam Bending Moment & Shear (AISC 360)", "📐", "Simply supported & cantilever SFD, BMD & deflection", "M_max = wL²/8 | δ = 5wL⁴/384EI | σ = M/S"),
            ("block-calculator.html", "Block Masonry Estimator (NCMA TEK)", "🧱", "CMU block counts, Type S mortar bags & core grout", "N = Area × 12.5 blocks/m² | Mortar = N / 33.3 bags"),
            ("concrete-block-calculator.html", "Concrete Block Calculator (ASTM C90)", "🧱", "CMU counts, Type S/N mortar, sand & ASTM C476 grout", "N = Net Area × 12.5 | Grout = 0.95 m³/100 blocks"),
            ("concrete-mix-ratio-calculator.html", "Concrete Mix Ratio (ACI 211.1)", "🏗️", "Dry batch volume 1.54 factor, cement bags, sand & stone", "V_dry = V_wet × 1.54 | M10 to M25 grades | w/c ratio"),
            ("drywall-calculator.html", "Drywall Sheets, Mud & Tape (ASTM C840)", "🏠", "Gypsum board sheets 4x8 to 4x12, joint compound & screws", "Sheets = Net Area / Board Area | Level 4 & 5 finish"),
            ("excavation-calculator.html", "Excavation & Earthwork Haul (OSHA 1926)", "🚜", "Bank (BCY) vs loose (LCY) volume, swell factor & dump trucks", "V_loose = V_bank × (1 + Swell) | OSHA Type A, B, C slopes"),
            ("excavation-volume-calculator.html", "Excavation Volume (Prismoidal & End Area)", "📐", "Trapezoidal trench side slopes & prismoidal cut-and-fill", "V = (L/6)·(A1 + 4Am + A2) | Cp = (L/12)·(c1-c2)·(w1-w2)"),
            ("flooring-calculator.html", "Flooring Area & Box Estimator (NWFA)", "🪵", "Hardwood, LVP, tile carton counts, pattern waste & underlay", "Boxes = ⌈Area × (1+Waste) / Box Coverage⌉ | 1/4\" gap"),
            ("footing-size-calculator.html", "Footing Size & Soil Bearing (ACI 318)", "🏛️", "Pad width B, contact pressure & two-way punching shear", "B = √(P/qa) | φVc = 0.33λ√f'c·b0·d ≥ Vu2"),
            ("gravel-calculator.html", "Gravel & Aggregate Estimator (ASTM D448)", "🪨", "Tonnage, cubic meters/yards & 15% compaction allowance", "V_loose = V_net × (1 + Compaction) | Tons = V × ρ"),
            ("paint-calculator.html", "Paint Gallon & Coverage (MPI Standards)", "🎨", "Wall & ceiling gallons, liters, primer & fenestrations", "Gallons = (Net Area × Coats) ÷ Spread Rate | WFT/DFT"),
            ("rebar-weight-calculator.html", "Rebar Weight & Tonnage (ASTM A615)", "🔩", "Metric kg/m d²/162, US lb/ft #²/24 & BBS bundles", "m = d²/162.28 kg/m | w = #²/24 lb/ft | Lap splices"),
            ("roof-pitch-calculator.html", "Roof Pitch & Rafter Length (IRC Ch. 9)", "🏠", "Pitch X:12, slope angle, area multiplier & rafter length", "Angle = arctan(Rise/Run) | M = √(1 + (X/12)²)"),
            ("slab-concrete-calculator.html", "Slab Concrete Volume (ACI 360R)", "🏗️", "Slab-on-grade, thickened edge footings & saw-cut joints", "V = L·W·T + V_edge | Max Joint Spacing = 24·T"),
            ("slope-calculator.html", "Slope & Grade Calculator (ADAAG 405)", "📐", "Rise/run gradient, % grade, angle & ADA ramp 1:12 compliance", "m = Rise/Run | Grade % = m·100 | ADA max 8.33%"),
            ("soil-gravel-calculator.html", "Soil & Gravel Volume & Tonnage", "🪨", "Proctor density compaction, loose LCY haulage & quarry tons", "V_loose = V_compacted·(1 + C_f) | Mass = V·ρ"),
            ("tile-calculator.html", "Tile, Grout & Mortar Sizer (TCNA)", "🔲", "Floor/wall cartons, TCNA joint grout weight & thinset notch", "Grout = [(L+W)·Jw·Jd·ρ] / (L·W) · Area · 1.10"),
        ]
    },
    "chemical.html": {
        "title": "Chemical & Water Treatment",
        "tools": [
            ("chlorine-dosing-calculator.html", "Chlorine Dosing Calculator", "💧", "AWWA C651 water disinfection & bleach", "Feed (lbs) = Vol (MGal) × Dose (mg/L) × 8.34"),
            ("chemical-dosing-calculator.html", "Chemical Dosing Rate Calculator", "🧪", "Pump flow LPH & mg/L ppm feed", "Feed Rate (LPH) = (Q × D) ÷ (S × SG × 10000)"),
            ("alum-dosing-calculator.html", "Alum Dosing & Coagulation Feed", "🧪", "AWWA B403 liquid/dry alum feed, pump mL/min & alkalinity", "Feed (lb/day) = Q (MGD) · Dose (mg/L) · 8.34"),
            ("boyles-law-calculator.html", "Boyle's Gas Law (P₁V₁=P₂V₂)", "🎈", "Isothermal gas expansion, compression work & compressibility Z", "P₁V₁ = P₂V₂ | W = -P₁V₁·ln(V₂/V₁)"),
            ("calcium-hypochlorite-dosing-calculator.html", "Calcium Hypochlorite (HTH 68%)", "💧", "AWWA C651 water main shock, 65-70% tablets & CT credit", "Mass = (Vol · Dose · 8.34) / Purity | HOCl speciation"),
            ("caustic-soda-dosing-calculator.html", "Caustic Soda (NaOH) Dosing", "🧪", "50% & 25% NaOH feed, alkalinity boost & LCR corrosion", "1.0 mg/L NaOH = +1.251 mg/L Alkalinity as CaCO₃"),
            ("charles-law-calculator.html", "Charles's Law (V₁/T₁=V₂/T₂)", "🌡️", "Isobaric thermal gas expansion, Kelvin scale & boundary work", "V₁/T₁ = V₂/T₂ | W = P·ΔV = nR·ΔT"),
            ("chlorine-dioxide-dosing-calculator.html", "Chlorine Dioxide (ClO₂) Oxidation", "🔬", "Precursor NaClO₂ feed, Fe/Mn removal & EPA chlorite cap", "2 NaClO₂ + Cl₂ ➔ 2 ClO₂ + 2 NaCl | DBP cap 0.8 mg/L"),
            ("coagulant-dosing-calculator.html", "Coagulant Dosing (Jar Test Sizer)", "🧪", "Alum, FeCl₃ & ACH feed rates, dry kg/day & pump sizing", "Feed (kg/day) = (Q · Dose · 24) / 1000 | Stock LPH"),
            ("combined-gas-law-calculator.html", "Combined Gas Law (P₁V₁/T₁=P₂V₂/T₂)", "🎈", "Simultaneous pressure, volume & temperature transitions", "(P₁·V₁)/T₁ = (P₂·V₂)/T₂ | Polytropic PV^n = C"),
            ("dilution-calculator.html", "Solution Dilution (C₁V₁ = C₂V₂)", "🧪", "Serial dilution, stock aliquots, solvent volume & buffer mix", "C₁·V₁ = C₂·V₂ | V_diluent = V₂ - V₁"),
            ("gay-lussac-law-calculator.html", "Gay-Lussac's Gas Law (P₁/T₁=P₂/T₂)", "🌡️", "Isochoric rigid vessel pressure & thermal burst safety", "P₁/T₁ = P₂/T₂ | ΔP = (nR/V)·ΔT | ASME pressure relief"),
            ("half-life-calculator.html", "Radioactive Half-Life & Decay", "☢️", "Exponential nuclear kinetics, remaining mass & activity", "N(t) = N₀ · (1/2)^(t / t½) = N₀ · e^(-λt)"),
            ("henderson-hasselbalch-calculator.html", "Henderson-Hasselbalch (pH Buffer)", "🧪", "Acid-base conjugate ratio, pKa & Van Slyke buffer beta", "pH = pK_a + log([A⁻]/[HA]) | β = 2.303·C·α·(1-α)"),
            ("hydrazine-dosing-calculator.html", "Hydrazine Dosing (Boiler Deoxygenation)", "💧", "ASME / EPRI AVT(R) dissolved O₂ scavenger & pump sizing", "N₂H₄ + O₂ ➔ N₂ + 2H₂O | 1:1 mass ratio | 35% hydrate"),
            ("ideal-gas-law-calculator.html", "Ideal Gas Law (PV = nRT)", "🎈", "Universal gas state equation, density & compressibility Z", "PV = nRT = (m/M)RT | ρ = PM / RT | v_rms speed"),
            ("lime-dosing-calculator.html", "Lime Softening (Ca(OH)₂ & CaO)", "🧱", "AWWA B202 softening, CO₂ removal & sludge yield", "CaO + H₂O ➔ Ca(OH)₂ | Sludge = 2.5·CaO (kg/day)"),
            ("molar-mass-calculator.html", "Molar Mass (IUPAC Formula Sizer)", "🔬", "Molecular weight, formula mass & mass % composition", "M = Σ(n_i · A_r(i)) | %w_i = (n_i·A_r/M)·100"),
            ("molarity-calculator.html", "Molarity & Solution Preparation", "🧪", "Molar concentration, mass grams, volume & normality N", "M = n/V = m/(MW·V) | N = M·z (eq/L)"),
            ("ph-calculator.html", "pH & [H⁺]/[OH⁻] Equilibrium", "🌡️", "Strong/weak acids & bases, exact quadratic Ka & pOH", "pH = -log₁₀[H⁺] | [H⁺] = (-Ka + √(Ka² + 4KaC))/2"),
            ("ph-poh-calculator.html", "pH to pOH & Ion Converter", "🌡️", "Mutual conversion, hydronium [H⁺], hydroxide & Kw", "pH + pOH = pKw | Kw shifts 14.94 (0°C) to 12.29 (100°C)"),
            ("phosphate-dosing-calculator.html", "Phosphate Dosing (Boiler & Lead CCT)", "💧", "ASME / EPRI TSP/DSP congruent treatment & EPA LCR", "10 Ca²⁺ + 6 PO₄³⁻ + 2 OH⁻ ➔ Hydroxyapatite sludge"),
            ("polymer-dosing-calculator.html", "Polymer Dosing (Sludge Dewatering)", "🧪", "Centrifuge & belt press kg/DT, aging tank & pump LPH", "Dose = kg active / DT sludge | 45-min hydration"),
            ("ro-antiscalant-dosing-calculator.html", "RO Antiscalant (Membrane Scaling)", "🌊", "Concentration factor CF=1/(1-Y), LSI & neat pump LPH", "CF = 1/(1-Y) | Prevents CaCO₃, CaSO₄, BaSO₄ & SiO₂"),
            ("sulphuric-acid-dosing-calculator.html", "Sulfuric Acid (H₂SO₄) Dosing", "🧪", "93% & 98% H₂SO₄ feed, alkalinity reduction & cooling tower", "98.08 g H₂SO₄ per 100.09 g CaCO₃ | 0.980 mass ratio"),
            ("titration-calculator.html", "Acid-Base Titration (C₁V₁ = C₂V₂)", "🔬", "Equivalence point, analyte molarity & polyprotic curves", "C_A · V_A · n_A = C_B · V_B · n_B | Buffer inflection"),
        ]
    },
    "physics.html": {
        "title": "Physics & Applied Mechanics",
        "tools": [
            ("acceleration-calculator.html", "Acceleration (SUVAT Kinematics)", "🚀", "Uniform acceleration, velocity, travel time & g-force", "a = (v - u) / t | v² = u² + 2as | s = ut + ½at²"),
            ("angular-velocity-calculator.html", "Angular Velocity (RPM to Rad/s)", "⚙️", "Rotational speed, peripheral tangential velocity & rim g-force", "ω = 2π·RPM/60 | v = ω·r | a_c = ω²·r"),
            ("centripetal-force-calculator.html", "Centripetal Force (Circular Motion)", "🔄", "Inward force, roadway banked turn angles & loop critical velocity", "F_c = mv²/r = mω²r | tan(θ) = v²/(gr)"),
            ("doppler-effect-calculator.html", "Doppler Effect (Sound & Radar Shift)", "🔊", "Acoustic frequency shift, apparent pitch & medical ultrasound", "f' = f₀ · (c ± v_o) / (c ∓ v_s) | Mach cone"),
            ("escape-velocity-calculator.html", "Escape Velocity (Planetary Gravity)", "🪐", "Gravitational escape speed, orbital speed & Schwarzschild radius", "v_e = √(2GM/r) = √(2gr) | v_orb = v_e / √2"),
            ("free-fall-calculator.html", "Free Fall (Vacuum & Air Drag)", "🪂", "Impact velocity, fall time & terminal velocity modeling", "v = gt = √(2gh) | v_t = √((2mg)/(ρ·Cd·A))"),
            ("friction-calculator.html", "Friction (Static & Kinetic)", "🧱", "Friction force, normal force, ramp angle of repose & slide acceleration", "F_f = μ·N | θ_c = arctan(μ_s) | a = g(sinθ - μ_k·cosθ)"),
            ("gravitational-force-calculator.html", "Gravitational Force (Newton)", "🌌", "Mutual planetary attraction, orbital acceleration & potential energy", "F = G·(m₁·m₂)/r² | U = -G·(m₁·m₂)/r"),
            ("hookes-law-calculator.html", "Hooke's Law (Spring Stiffness)", "🪢", "Restoring force, elastic potential energy & harmonic frequency", "F = -k·x | U = ½·k·x² | f = (1/2π)√(k/m)"),
            ("kinetic-energy-calculator.html", "Kinetic Energy (Motion Work)", "⚡", "Translational ½mv², rotational flywheel ½Iω² & relativistic energy", "E_k = ½·m·v² | E_rot = ½·I·ω² | E = (γ-1)mc²"),
            ("photon-energy-calculator.html", "Photon Energy (Planck-Einstein)", "💡", "Quantum energy in eV & Joules, momentum & EM wavelength", "E = hf = hc/λ | E(eV) ≈ 1239.84/λ(nm) | p = h/λ"),
            ("simple-pendulum-calculator.html", "Simple Pendulum (Period & Gravity)", "🕰️", "Oscillation period T, frequency, seconds pendulum & Borda correction", "T = 2π√(L/g) | T ≈ T₀(1 + θ₀²/16)"),
            ("snells-law-calculator.html", "Snell's Law (Refraction & TIR)", "🔍", "Refraction angle, critical angle for total internal reflection & fiber", "n₁·sin(θ₁) = n₂·sin(θ₂) | θ_c = arcsin(n₂/n₁)"),
            ("specific-heat-calculator.html", "Specific Heat (Heat Transfer Q)", "🔥", "Sensible heat Q = mcΔT, calorimetry equilibrium & heating time", "Q = m·c·ΔT | T_eq = (m₁c₁T₁ + m₂c₂T₂)/(m₁c₁ + m₂c₂)"),
            ("acceleration-converter.html", "Acceleration Converter", "🚀", "m/s², g₀, ft/s², Gal & automotive 0-60 mph metrics", "a = Δv/Δt | 1 g₀ = 9.80665 m/s² = 32.174 ft/s²"),
        ]
    },
    "fire-safety.html": {
        "title": "Fire & Life Safety",
        "tools": [
            ("fire-alarm-battery-calculator.html", "Fire Alarm Battery (NFPA 72)", "🚨", "24h standby + evacuation alarm Ah sizing", "C = 1.20 × (I_sb·T_sb + I_al·T_al)"),
            ("hydrant-fire-flow-calculator.html", "Hydrant Fire Flow (NFPA 291)", "🚒", "Pitot discharge flow & rated 20 psi capacity", "Q = 29.83·cd·d²√P | Q_R at 20 psi"),
            ("smoke-detector-spacing-calculator.html", "Smoke Detector Spacing & Layout", "🚨", "NFPA 72 ceiling height derating", "S = 30ft Baseline with Derating Factor"),
            ("fire-sprinkler-calculator.html", "Fire Sprinkler Hydraulics", "💦", "NFPA 13 head flow Q=K√P & demand", "Q = K × √P (K-Factor 5.6 & 8.0)"),
            ("fire-pump-sizing-calculator.html", "Fire Pump Sizing (NFPA 20)", "🚒", "Rated flow, net head, churn & motor BHP", "BHP = (Q × H × SG) / (3960 × η)"),
            ("nac-voltage-drop-calculator.html", "NAC Voltage Drop (NFPA 72 & UL 864)", "🚨", "Point-to-point & lump-sum 16V EOL limit", "V_end = V_batt - Σ(I_seg · R_seg) ≥ 16.0V"),
            ("fire-sprinkler-hydraulic-calculator.html", "Fire Sprinkler Hydraulic (NFPA 13)", "💦", "Hazen-Williams friction & head Q=K√P", "p = 4.52·Q^1.85 / (C^1.85·d^4.87) | Q = K√P"),
            ("strobe-candela-calculator.html", "Strobe Candela (NFPA 72 Chapter 18)", "🚨", "Wall & ceiling candela sizing & UL 1971", "Iv per NFPA 72 Table 18.5.5.4.1 | 0.0375 ft-c boundary"),
        ]
    },
    "programmer.html": {
        "title": "Programmer & Networking",
        "tools": [
            ("subnet-calculator.html", "IPv4 Subnet & CIDR IP Calculator", "🌐", "Network ID, mask & usable hosts", "Usable Hosts = 2^(32 - CIDR) - 2"),
        ]
    },
    "datetime.html": {
        "title": "Date & Time Utility",
        "tools": [
            ("date-difference-calculator.html", "Date Difference & Business Days", "📅", "Exact calendar days & work weeks", "Elapsed Days & Mon-Fri Working Days"),
        ]
    },
    "converter.html": {
        "title": "Universal Unit Converters",
        "tools": [
            ("unit-converter.html", "Universal Multi-Unit Converter", "🔄", "Length, mass, temp, pressure & vol", "100% Client-Side Direct Exact Multipliers"),
            ("length-converter.html", "Length & Distance Converter", "📏", "Meters, feet, inches, kilometers, miles & nautical miles", "1 in = 0.0254 m | 1 ft = 0.3048 m | 1 mi = 1609.344 m"),
            ("weight-converter.html", "Weight & Mass Converter", "⚖️", "Kilograms, pounds, ounces, stone, carats & metric tonnes", "1 lb = 0.45359237 kg | Planck h = 6.62607015e-34"),
            ("temperature-converter.html", "Temperature Scale Converter", "🌡️", "Celsius, Fahrenheit, Kelvin, Rankine & Réaumur", "°F = (°C × 9/5) + 32 | K = °C + 273.15"),
            ("area-converter.html", "Land & Geometric Area Converter", "📐", "Square meters, feet, acres, hectares & square miles", "1 ac = 43,560 ft² = 4,046.856 m² | 1 ha = 10,000 m²"),
            ("volume-converter.html", "Volume & Capacity Converter", "🧪", "Liters, US gallons, imperial gallons, cubic meters & feet", "1 US gal = 231 in³ = 3.785 L | 1 UK gal = 4.546 L"),
            ("pressure-converter.html", "Pressure & Vacuum Converter", "💨", "Pascals, bar, PSI, atmospheres, Torr & inches of mercury", "1 atm = 101,325 Pa = 14.696 psi | 1 bar = 100 kPa"),
            ("speed-converter.html", "Speed & Velocity Converter", "🚀", "m/s, km/h, mph, knots, feet/s & Mach sound barrier", "1 m/s = 3.6 km/h | 1 mph = 1.609344 km/h | 1 kt = 1.852 km/h"),
            ("energy-converter.html", "Energy & Work Converter", "⚡", "Joules, kWh, calories, kcal, BTU, electron-volts & therms", "1 J = 1 N·m | 1 kWh = 3.6 MJ | 1 kcal = 4,184 J"),
            ("power-converter.html", "Power Converter (Watts, kW, HP)", "⚡", "Mechanical HP, metric PS, Watts, kilowatts & BTU/hr", "1 HP = 745.699872 W | 1 kW = 1,000 W | 1 PS = 735.49875 W"),
            ("force-converter.html", "Force Converter (Newtons, lbf, kN)", "💪", "Newtons, pound-force, dynes, kips & kilogram-force", "F = m·a | 1 lbf = 4.448222 N | 1 kgf = 9.80665 N"),
            ("data-storage-converter.html", "Data Storage Converter (GB, TB, GiB)", "💾", "Decimal SI bytes (KB, MB, GB, TB) & binary IEC units (KiB, MiB, GiB, TiB)", "1 TB = 10¹² bytes | 1 TiB = 2⁴⁰ bytes = 1,099.5 GB"),
            ("data-transfer-rate-converter.html", "Data Transfer Rate Converter (Mbps, Gbps)", "🌐", "Bandwidth, bits vs bytes, Gbps, MB/s & transfer download time", "1 Byte = 8 bits | T_transfer = File Size / Transfer Rate"),
            ("frequency-converter.html", "Frequency Converter (Hz, RPM, rad/s)", "📻", "Hertz, kHz, MHz, GHz, rotational RPM & angular velocity rad/s", "f = RPM / 60 | ω = 2π·f | λ = c / f"),
            ("flow-rate-converter.html", "Flow Rate Converter (GPM, L/min, m³/h)", "🌊", "Volumetric flow, US GPM, Imperial GPM, L/min, m³/h & CFS", "Q = A·v | 1 US GPM = 3.78541 L/min | 1 m³/h = 4.403 GPM"),
            ("fuel-economy-converter.html", "Fuel Economy Converter (MPG, L/100km)", "⛽", "Harmonic fuel consumption, US MPG, UK MPG, L/100km & km/L", "L/100km = 235.215 / MPG_US | MPG_UK = 1.20095·MPG_US"),
            ("angle-converter.html", "Angle Converter (Degrees, Radians, MOA)", "📐", "Sexagesimal degrees, radians, gradians, MOA & milliradians mrad", "rad = deg × π/180 | 1 MOA = 1/60° | 1 mrad = 3.438 MOA"),
            ("density-converter.html", "Density & Specific Gravity Converter", "⚖️", "kg/m³, g/cm³, lb/ft³, lb/gal & petroleum API gravity", "ρ = m/V | SG = ρ/1000 | °API = (141.5/SG) - 131.5"),
            ("illuminance-converter.html", "Illuminance & Light Level Converter", "💡", "Lux (lx), Foot-Candles (fc), Phot & Nox with IESNA standards", "1 fc = 10.7639 lx | E = (I·cosθ)/d² | OSHA 1926.56"),
            ("thermal-conductivity-converter.html", "Thermal Conductivity (k-value)", "🌡️", "W/(m·K), BTU/(hr·ft·°F), BTU·in/(hr·ft²·°F) & R-values", "q = -k·∇T | R = L/k | 1 BTU/(hr·ft·°F) = 1.731 W/(m·K)"),
            ("viscosity-converter.html", "Viscosity (Dynamic & Kinematic)", "🌊", "Centipoise (cP), Pa·s, Centistokes (cSt), Stokes & SUS", "ν = μ/ρ | 1 Pa·s = 1,000 cP | SUS ≈ 4.632·cSt | ΔP = 128μLQ/πD⁴"),
            ("cooking-converter.html", "Cooking & Baking Recipe Converter", "🍳", "Cups, tbsp, tsp, grams, oz & ingredient bulk densities", "Mass = Vol × ρ_bulk | 1 Cup AP Flour = 120g | 1 Stick Butter = 113.4g"),
            ("number-base-converter.html", "Number Base (Bin, Oct, Dec, Hex)", "💻", "Binary base 2, Octal base 8, Decimal base 10 & Hex base 16", "N = Σ(d_i · b^i) | Two's Complement: -X = ~X + 1"),
            ("roman-numeral-converter.html", "Roman Numeral Converter (1 to 3.9M)", "🏛️", "Classical subtractive notation & Vinculum overline bars", "I=1, V=5, X=10, L=50, C=100, D=500, M=1000 | V̄=5000"),
            ("time-converter.html", "Time Unit & Chronometric Converter", "⏱️", "Seconds, ms, μs, ns, hours, days, weeks & Julian years", "1 s = 9,192,631,770 Cs cycles | Julian Year = 31,557,600 s"),
            ("time-zone-converter.html", "Time Zone & World Clock Converter", "🌍", "UTC offsets, daylight saving transitions & meeting planner", "UTC ± HH:MM | IANA Zone Database"),
            ("unix-timestamp-converter.html", "Unix Timestamp & Epoch Converter", "💻", "Seconds/milliseconds to ISO 8601 UTC & local datetime", "t_epoch = Seconds since Jan 1, 1970 00:00:00 UTC"),
        ]
    }
}

def update_category_pages():
    for cat_file, data in CAT_MAP.items():
        file_path = os.path.join(BASE_DIR, cat_file)
        if not os.path.exists(file_path):
            continue
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        cards_html = []
        for slug, title, icon, desc, formula in data["tools"]:
            cards_html.append(f"""        <a href="{slug}" class="silo-card">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;">
            <div class="silo-card-icon">{icon}</div>
            <span class="silo-card-badge">Certified Tool</span>
          </div>
          <div class="silo-card-title">{title}</div>
          <div class="silo-card-desc">{desc}</div>
          <div class="formula-badge-pill">{formula}</div>
          <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:var(--brand-primary);margin-top:1rem;">
            Launch Calculator &rarr;
          </span>
        </a>""")

        grid_inner = "\n\n".join(cards_html)
        num_tools = len(data["tools"])

        # Replace cards grid
        grid_pattern = re.compile(r'<div class="silo-card-grid"[^>]*>.*?</div>(?=\s*(?:<!--.*?-->\s*)*<article)', re.DOTALL)
        new_grid = f'<div class="silo-card-grid" style="margin-top:0;margin-bottom:3.5rem;">\n{grid_inner}\n    </div>'
        
        content = grid_pattern.sub(new_grid, content)

        # Update counter labels
        content = re.sub(r'<strong>\d+</strong>\s*(?:Certified Calculators|Precision Tools|Engineering Tools)', f'<strong>{num_tools}</strong> Certified Calculators', content)
        content = re.sub(r'Available (?:Tools|Health Calculators|Engineering Calculators|Finance Calculators|Mathematics Calculators)\s*\(\d+\)', f'Available Tools ({num_tools})', content)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {cat_file} with all {num_tools} cards!")

def update_index_page():
    index_path = os.path.join(BASE_DIR, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Category Overview Cards with ALL tools
    cat_cards_html = []
    total_tools_count = 0

    for cat_file, data in CAT_MAP.items():
        num_tools = len(data["tools"])
        total_tools_count += num_tools
        tool_links = []
        for slug, title, icon, desc, formula in data["tools"]:
            tool_links.append(f"""          <a href="{slug}" class="cat-tool-item"><span>{icon} {title}</span><span class="arr">&rarr;</span></a>""")
        
        links_block = "\n".join(tool_links)
        cat_cards_html.append(f"""      <!-- {data["title"]} -->
      <div class="category-overview-card">
        <div class="cat-card-header">
          <div class="cat-icon-box">{data["tools"][0][2]}</div>
          <span class="cat-count-badge">{num_tools} Tools</span>
        </div>
        <div class="cat-card-title">{data["title"]}</div>
        <div class="cat-card-desc">Certified industrial & academic calculations verified against international standards.</div>
        <div class="cat-tool-preview-list">
{links_block}
        </div>
        <a href="{cat_file}" class="cat-explore-btn">Explore {data["title"]} Hub &rarr;</a>
      </div>""")

    new_cat_grid = '<div class="category-overview-grid">\n' + "\n\n".join(cat_cards_html) + '\n    </div>'

    # Replace category grid on index.html
    cat_grid_pattern = re.compile(r'<div class="category-overview-grid">.*?</div>\s*(?=<!-- Comprehensive Platform Authority|<!-- Full Interactive Tool Directory|\s*<section)', re.DOTALL)
    if cat_grid_pattern.search(content):
        content = cat_grid_pattern.sub(new_cat_grid + '\n\n    ', content)
    else:
        # Fallback search
        cat_grid_pattern2 = re.compile(r'<div class="category-overview-grid">.*?</div>', re.DOTALL)
        content = cat_grid_pattern2.sub(new_cat_grid, content, count=1)

    # 2. Add Complete Interactive 54-Tool Directory Section if not present
    all_tools_items = []
    for cat_file, data in CAT_MAP.items():
        for slug, title, icon, desc, formula in data["tools"]:
            all_tools_items.append(f"""        <div class="directory-tool-card" data-cat="{data['title'].lower()}" data-search="{title.lower()} {slug.lower()} {desc.lower()}" style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:1rem;display:flex;flex-direction:column;justify-content:space-between;transition:transform 0.2s,box-shadow 0.2s;">
          <div>
            <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
              <span style="font-size:1.5rem;">{icon}</span>
              <span style="font-size:0.72rem;background:#F1F5F9;color:#475569;padding:2px 8px;border-radius:12px;font-weight:600;">{data['title']}</span>
            </div>
            <h3 style="margin:0 0 0.35rem;font-size:1rem;color:#0F172A;"><a href="{slug}" style="color:#0F172A;text-decoration:none;">{title}</a></h3>
            <p style="margin:0 0 0.75rem;font-size:0.82rem;color:#64748B;line-height:1.4;">{desc}</p>
          </div>
          <div style="display:flex;align-items:center;justify-content:space-between;border-top:1px solid #F1F5F9;padding-top:0.65rem;margin-top:0.5rem;">
            <code style="font-size:0.75rem;color:#2563EB;background:#EFF6FF;padding:2px 6px;border-radius:4px;">{formula[:28]}</code>
            <a href="{slug}" style="font-size:0.82rem;font-weight:700;color:#2563EB;text-decoration:none;">Launch &rarr;</a>
          </div>
        </div>""")

    directory_block = f"""    <!-- Full Interactive Tool Directory (All {total_tools_count} Calculators Live) -->
    <section id="all-calculators-directory" style="margin-top:4rem;padding-top:2.5rem;border-top:1px solid #E2E8F0;">
      <div style="text-align:center;margin-bottom:2rem;">
        <span class="category-tag" style="background:#F0FDF4;color:#166534;border-color:#BBF7D0;margin-bottom:0.75rem;">
          ⚡ Complete Live Directory · {total_tools_count} High-Precision Tools Live
        </span>
        <h2 style="font-size:2rem;color:#0F172A;margin:0 0 0.5rem;">All {total_tools_count} Online Calculators</h2>
        <p style="color:#64748B;font-size:1rem;max-width:700px;margin:0 auto 1.5rem;">
          Instant access to all verified tools across Health, Finance, Engineering, Civil, Mechanical, Math, Chemical, and Solar energy.
        </p>

        <!-- Live Instant Search Bar -->
        <div style="max-width:600px;margin:0 auto;position:relative;">
          <input type="text" id="directory-search-input" placeholder="🔍 Search any calculator (e.g., bmr, wire, brick, roi, pump, asphalt)..." 
                 oninput="filterDirectoryTools()"
                 style="width:100%;padding:0.85rem 1.25rem;border-radius:12px;border:2px solid #CBD5E1;font-size:1rem;outline:none;transition:border-color 0.2s;"
                 onfocus="this.style.borderColor='#2563EB'" onblur="this.style.borderColor='#CBD5E1'">
        </div>
      </div>

      <div id="directory-tools-grid" style="display:grid;grid-template-columns:repeat(auto-fill, minmax(260px, 1fr));gap:1rem;">
{chr(10).join(all_tools_items)}
      </div>
      <div id="no-search-results" style="display:none;text-align:center;padding:3rem;color:#64748B;">
        <p style="font-size:1.1rem;margin-bottom:0.5rem;">No calculators match your search.</p>
        <button type="button" class="btn btn-secondary" onclick="document.getElementById('directory-search-input').value='';filterDirectoryTools();">Clear Search</button>
      </div>

      <script>
        function filterDirectoryTools() {{
          const q = document.getElementById('directory-search-input').value.toLowerCase().trim();
          const cards = document.querySelectorAll('.directory-tool-card');
          let visibleCount = 0;
          cards.forEach(card => {{
            const searchData = card.getAttribute('data-search') || '';
            const match = !q || searchData.includes(q);
            card.style.display = match ? 'flex' : 'none';
            if (match) visibleCount++;
          }});
          document.getElementById('no-search-results').style.display = visibleCount === 0 ? 'block' : 'none';
        }}
      </script>
    </section>"""

    # Check if section already exists, replace or insert before closing </main>
    if '<section id="all-calculators-directory"' in content:
        content = re.sub(r'<section id="all-calculators-directory".*?</section>', directory_block, content, flags=re.DOTALL)
    else:
        content = content.replace('</main>', directory_block + '\n  </main>')

    # Update hero quick category chips
    chips_html = f"""      <div style="display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin-bottom:1.5rem;">
        <a href="health.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">⚖️ Health ({len(CAT_MAP['health.html']['tools'])})</a>
        <a href="finance.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">🏦 Finance ({len(CAT_MAP['finance.html']['tools'])})</a>
        <a href="math.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">🔢 Math ({len(CAT_MAP['math.html']['tools'])})</a>
        <a href="engineering.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">⚡ Electrical ({len(CAT_MAP['engineering.html']['tools'])})</a>
        <a href="solar-energy.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">☀️ Solar ({len(CAT_MAP['solar-energy.html']['tools'])})</a>
        <a href="mechanical.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">⚙️ Mechanical ({len(CAT_MAP['mechanical.html']['tools'])})</a>
        <a href="civil.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">🏗️ Civil ({len(CAT_MAP['civil.html']['tools'])})</a>
        <a href="chemical.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">🧪 Chemical ({len(CAT_MAP['chemical.html']['tools'])})</a>
        <a href="physics.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">🔬 Physics ({len(CAT_MAP['physics.html']['tools'])})</a>
        <a href="fire-safety.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">🚨 Fire ({len(CAT_MAP['fire-safety.html']['tools'])})</a>
        <a href="programmer.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">👨‍💻 Tech ({len(CAT_MAP['programmer.html']['tools'])})</a>
        <a href="datetime.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">📅 Date ({len(CAT_MAP['datetime.html']['tools'])})</a>
        <a href="converter.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">🔄 Converter ({len(CAT_MAP['converter.html']['tools'])})</a>
      </div>"""

    content = re.sub(r'<!-- Quick Category Jump Chips -->\s*<div[^>]*>.*?</div>', f'<!-- Quick Category Jump Chips -->\n{chips_html}', content, flags=re.DOTALL)

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"index.html updated! All {total_tools_count} calculators are now listed in category previews AND directory!")

if __name__ == "__main__":
    update_category_pages()
    update_index_page()
