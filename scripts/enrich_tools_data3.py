import os

THIRD_BATCH_DATA = {
    "simple-interest-calculator.html": {
        "verification": "Standard Financial Accounting Linear Interest Model (I = P·r·t)",
        "standards": [
            ("Core Formula", "Linear Interest: I = P × r × t & Total Accrual: A = P × (1 + r × t)"),
            ("Use Cases", "Promissory notes, short-term commercial paper, bridge loans, bonds"),
            ("Time Conventions", "Exact/365, Ordinary/360 (Banker's Rule), and Monthly allocations"),
            ("Accounting Standards", "IFRS 9 Financial Assets & Liabilities at Amortized Cost")
        ],
        "example_title": "Field Case Study: Short-Term Commercial Equipment Bridge Loan",
        "example_badge": "Real-World Financial Problem",
        "steps": [
            ("Step 1: Define Loan Principal, Annual Interest Rate, and Term",
             r"P = \$25{,}000,\quad r = 7.50\%\ (0.075),\quad t = 1.5\text{ years}\ (18\text{ months})",
             "A manufacturing business borrows $25,000 as a simple-interest working capital bridge loan."),
            ("Step 2: Calculate Total Simple Interest Incurred (I)",
             r"I = P \times r \times t = 25{,}000 \times 0.075 \times 1.5 = \$2{,}812.50",
             "Over the 18-month term, interest accrues linearly to $2,812.50."),
            ("Step 3: Calculate Total Payoff Amount at Maturity (A)",
             r"A = P + I = \$25{,}000 + \$2{,}812.50 = \$27{,}812.50",
             'The total payoff amount at maturity is $27,812.50. Compare against exponential wealth growth with our <a href="compound-interest-calculator.html">Compound Interest Calculator</a>, model amortized mortgages with our <a href="loan-emi-calculator.html">Loan EMI Calculator</a>, and visit our <a href="finance.html">Finance Hub</a>.')
        ],
        "final_result": "Loan Payoff: Principal: $25,000 | Total Accrued Interest: $2,812.50 | Final Lump-Sum Repayment: $27,812.50.",
        "faqs": [
            ("When is simple interest used instead of compound interest?",
             "Simple interest is predominantly used for short-term financing (less than one year), such as commercial promissory notes, automobile installment contracts without compounding, pawn loans, Treasury bills, and intercompany bridge financing."),
            ("What is the Banker's Rule in simple interest calculations?",
             "The Banker's Rule (Ordinary Interest) assumes each calendar year contains exactly 360 days (twelve 30-day months) while calculating interest over the exact number of calendar days elapsed. This produces a slightly higher interest payout to lenders than using 365 days."),
            ("Can you convert simple interest to an equivalent compound annual rate?",
             "Yes. Over terms exceeding one year, simple interest yields lower returns than compounding. To find the equivalent compound rate, solve: (1 + r_compound)^t = (1 + r_simple × t)."),
            ("How does paying off a simple interest loan early save money?",
             "Because simple interest accrues daily (I = P × r × days / 365), paying off the principal ahead of schedule stops future interest accumulation immediately, with zero compounding penalties.")
        ]
    },

    "salary-calculator.html": {
        "verification": "Progressive Income Tax Withholding & FICA / National Insurance Standards",
        "standards": [
            ("Tax Architecture", "Marginal Progressive Tax Brackets (US IRS / UK HMRC / State Taxes)"),
            ("Mandatory Deductions", "Social Security (6.2%), Medicare (1.45%), State Disability / SUI"),
            ("Pay Frequencies", "Annual, Monthly, Bi-Weekly (26 pay periods), Weekly (52 pay periods)"),
            ("Compensation Units", "Gross Annual Salary, Hourly Wage, Overtime 1.5×, and Net Take-Home")
        ],
        "example_title": "Payroll Case Study: Corporate Salary Gross-to-Net Breakdown",
        "example_badge": "Real-World Compensation Problem",
        "steps": [
            ("Step 1: Define Base Annual Salary and Pay Period Frequency",
             r"\text{Gross Salary} = \$85{,}000/\text{year},\quad \text{Pay Frequency: Bi-Weekly (26 Paychecks/Year)}",
             "A professional receives an $85,000 annual gross salary paid bi-weekly ($3,269.23 per paycheck)."),
            ("Step 2: Calculate Mandatory FICA Social Security & Medicare Withholdings",
             r"\text{Social Security (6.2%)} = \$5{,}270.00,\quad \text{Medicare (1.45%)} = \$1{,}232.50",
             "Mandatory federal payroll taxes total $6,502.50 annually ($250.10 per bi-weekly paycheck)."),
            ("Step 3: Compute Progressive Federal & State Income Tax Withholding",
             r"\text{Federal Income Tax (Effective 11.2%)} = \$9{,}520.00,\quad \text{State Tax (4.5%)} = \$3{,}825.00",
             "Income taxes total $13,345.00 annually."),
            ("Step 4: Compute Net Take-Home Pay per Paycheck",
             r"\text{Net Annual} = \$85{,}000 - \$6{,}502.50 - \$13{,}345.00 = \$65{,}152.50 \implies \$2{,}505.87/\text{paycheck}",
             'Net take-home pay is <strong>$2,505.87 bi-weekly ($5,429.38/month)</strong>. Model debt affordability with our <a href="loan-emi-calculator.html">Loan EMI Calculator</a> and budget savings with our <a href="discount-calculator.html">Discount Calculator</a>.')
        ],
        "final_result": "Compensation Summary: Gross: $85,000/yr | Taxes & Deductions: $19,847.50 (23.35%) | Net Take-Home Pay: $65,152.50 ($2,505.87 Bi-Weekly).",
        "faqs": [
            ("How do progressive marginal tax brackets work?",
             "Marginal tax brackets tax dollars earned within specific income tiers, not your total income. Entering a higher tax bracket (e.g., from 12% to 22%) means only the dollars earned above that threshold are taxed at 22%. Your earlier income remains taxed at the lower 10% and 12% rates."),
            ("What is the difference between effective tax rate and marginal tax rate?",
             "Your marginal tax rate is the tax rate paid on your next additional dollar of income. Your effective tax rate is your actual total tax paid divided by your total gross income. Effective tax rates are always significantly lower than top marginal rates."),
            ("How many paychecks are in a bi-weekly versus semi-monthly schedule?",
             "Bi-weekly employees are paid every two weeks, resulting in 26 paychecks per year (meaning two months per year have three paychecks). Semi-monthly employees are paid twice per month (typically on the 15th and last day), resulting in exactly 24 paychecks per year."),
            ("What is the difference between pre-tax and post-tax payroll deductions?",
             "Pre-tax deductions (traditional 401k, health insurance premiums, HSA contributions) reduce your gross taxable income before taxes are calculated, lowering your total tax burden. Post-tax deductions (Roth 401k, wage garnishments) are deducted after taxes have already been calculated.")
        ]
    },

    "discount-calculator.html": {
        "verification": "Commercial Pricing & Markdown Mathematical Standards",
        "standards": [
            ("Markdown Formula", "Discount Amount: D = P_original × (d / 100) & Final Price: P_final = P_original - D"),
            ("Multiple Discounts", "Cascading discounts: P_final = P_original × (1 - d1) × (1 - d2)"),
            ("Sales Tax Integration", "Total Outflow: P_total = P_final × (1 + Tax / 100)"),
            ("Commercial Accuracy", "Cents rounding to nearest 0.01 currency unit")
        ],
        "example_title": "Commercial Retail Case Study: Cascading Sale & Tax Markdown",
        "example_badge": "Real-World Commercial Problem",
        "steps": [
            ("Step 1: Define Original Price, Primary Markdown, and Loyalty Coupon",
             r"P_{orig} = \$240.00,\quad \text{Store Sale: 30% Off},\quad \text{Member Coupon: Extra 15% Off},\quad \text{Tax: 8.5%}",
             "A retail customer purchases equipment priced at $240.00 with a 30% store discount, an additional 15% loyalty coupon, and 8.5% sales tax."),
            ("Step 2: Apply Primary 30% Store Markdown",
             r"P_{sale} = \$240.00 \times (1 - 0.30) = \$168.00\quad (\text{Savings: } \$72.00)",
             "The primary 30% discount drops the price to $168.00."),
            ("Step 3: Apply Secondary 15% Cascading Loyalty Coupon",
             r"P_{coupon} = \$168.00 \times (1 - 0.15) = \$142.80\quad (\text{Additional Savings: } \$25.20)",
             "Cascading discounts do not add to 45%; the secondary 15% applies to the reduced $168.00 balance, giving $142.80."),
            ("Step 4: Compute Sales Tax and Total Out-of-Pocket Payment",
             r"\text{Tax} = \$142.80 \times 0.085 = \$12.14,\quad P_{final} = \$142.80 + \$12.14 = \$154.94",
             'The final total payment is <strong>$154.94</strong> (Total savings: $97.20 or 40.5% effective discount). Calculate general percentage deltas with our <a href="percentage-calculator.html">Percentage Calculator</a> and visit our <a href="finance.html">Finance Hub</a>.')
        ],
        "final_result": "Pricing Breakdown: Original: $240.00 | Total Discounts: -$97.20 (40.5% Off) | Sales Tax (8.5%): +$12.14 | Final Price: $154.94.",
        "faqs": [
            ("Why does '30% off + 15% off' not equal 45% off?",
             "Discounts are applied consecutively, not additively. The first 30% discount reduces the price to 70% of original. The second 15% discount is calculated on that reduced 70% price (0.70 × 0.85 = 0.595, or 59.5% of original price). The true combined discount is 40.5%, not 45%."),
            ("What is the difference between markup and profit margin?",
             "Markup is the percentage added to cost to determine selling price: Markup = (Price - Cost) / Cost. Margin is the percentage of selling price that represents profit: Margin = (Price - Cost) / Price. A 50% markup equals a 33.3% profit margin."),
            ("How do you calculate the original price if you only know the sale price?",
             "Divide the sale price by (1 - discount percentage in decimal). If an item on 20% sale costs $80, the original price was $80 / (1 - 0.20) = $80 / 0.80 = $100."),
            ("Is sales tax applied before or after store discounts?",
             "In almost all jurisdictions, sales tax is legally applied to the post-discounted final purchase price, ensuring you only pay tax on the actual money you spend.")
        ]
    },

    "calorie-calculator.html": {
        "verification": "Mifflin-St Jeor & Revised Harris-Benedict Metabolic Equations",
        "standards": [
            ("Metabolic Equation", "Mifflin-St Jeor Equation (Validated ±10% vs Indirect Calorimetry)"),
            ("Activity Multipliers", "Physical Activity Level (PAL): Sedentary (1.2) to Very Active (1.9)"),
            ("Macronutrient Values", "Protein: 4 kcal/g | Carbohydrates: 4 kcal/g | Dietary Fat: 9 kcal/g"),
            ("Clinical Deficit", "500 kcal/day deficit corresponds to ~1 lb (0.45 kg) fat loss per week")
        ],
        "example_title": "Clinical Case Study: Adult Energy Expenditure & Deficit Prescription",
        "example_badge": "Real-World Clinical Problem",
        "steps": [
            ("Step 1: Record Baseline Biometrics and Activity Level",
             r"\text{Male, 32 Years},\quad W = 84.0\text{ kg},\quad H = 180\text{ cm},\quad \text{Exercise: 4 days/week (Moderate, PAL 1.55)}",
             "A 32-year-old male weighing 84 kg with a height of 180 cm exercises moderately 4 days per week."),
            ("Step 2: Calculate Basal Metabolic Rate (BMR) via Mifflin-St Jeor",
             r"\text{BMR} = 10(W) + 6.25(H) - 5(A) + 5 = 10(84) + 6.25(180) - 5(32) + 5 = 1{,}810\text{ kcal/day}",
             "The patient burns 1,810 calories daily at absolute physiological rest purely maintaining organ cellular activity."),
            ("Step 3: Calculate Maintenance Total Daily Energy Expenditure (TDEE)",
             r"\text{TDEE} = \text{BMR} \times 1.55 = 1{,}810 \times 1.55 = 2{,}805.5\text{ kcal/day}",
             "Accounting for daily physical movement and exercise thermogenesis, maintenance calorie expenditure is 2,806 kcal/day."),
            ("Step 4: Prescribe Sustainable Caloric Deficit for Fat Loss",
             r"\text{Target Intake} = 2{,}806 - 500 = 2{,}306\text{ kcal/day}\ (\text{Target Loss: 0.5 kg / 1 lb fat per week})",
             'Consuming 2,306 calories daily establishes a 3,500 kcal weekly deficit (yielding 1 lb fat loss/week). Check healthy body weight ranges with our <a href="ideal-weight-calculator.html">Ideal Weight Calculator</a>, calculate hydration with our <a href="water-intake-calculator.html">Water Intake Calculator</a>, and visit our <a href="health.html">Health Hub</a>.')
        ],
        "final_result": "Metabolic Prescription: BMR: 1,810 kcal | Maintenance TDEE: 2,806 kcal | Fat Loss Intake: 2,306 kcal/day | Protein Target: 168g/day (2.0g/kg).",
        "faqs": [
            ("What is the difference between BMR and TDEE?",
             "Basal Metabolic Rate (BMR) is the minimum energy required to keep vital organs functioning in a comatose resting state. Total Daily Energy Expenditure (TDEE) includes BMR plus the thermic effect of food (TEF) and all physical activity (exercise, walking, working)."),
            ("Why is the Mifflin-St Jeor equation considered more accurate than Harris-Benedict?",
             "The Harris-Benedict equation was established in 1919 using a lean, young sample population and systematically overestimates caloric expenditure by 5% to 15% in modern sedentary populations. Mifflin-St Jeor (1990) was validated across diverse body compositions and is recognized as the clinical gold standard."),
            ("Why does weight loss plateau after several weeks in a caloric deficit?",
             "As body weight drops, BMR decreases (a lighter body burns fewer calories). Additionally, the body initiates adaptive thermogenesis—reducing non-exercise activity thermogenesis (NEAT) and thyroid output. Adjusting calorie targets downward every 5–10 lbs lost breaks through plateaus."),
            ("What is the recommended macronutrient distribution for fat loss?",
             "Evidence-based sports nutrition recommends high protein (1.6 to 2.2 grams per kg of body weight) to preserve lean muscle tissue during a deficit, 20% to 30% of daily calories from healthy fats for hormonal health, and the remainder from complex carbohydrates for training glycogen.")
        ]
    },

    "body-fat-calculator.html": {
        "verification": "U.S. Navy Circumference Method (DoD Instruction 1308.3)",
        "standards": [
            ("Clinical Standard", "Department of Defense Directive 1308.3 & Hodgdon-Beckett Equations"),
            ("Accuracy Correlation", "Correlates within ±3.0% of Dual-Energy X-Ray Absorptiometry (DEXA)"),
            ("Measurements", "Neck, Waist (at navel), Hips (women only), and Height in cm/inches"),
            ("Essential Fat Limits", "Men: 2%–5% | Women: 10%–13% minimum essential biological adipose")
        ],
        "example_title": "Clinical Case Study: Adult Anthropometric Body Fat & Lean Mass Assessment",
        "example_badge": "Real-World Body Composition Problem",
        "steps": [
            ("Step 1: Record Circumference Tape Measurements",
             r"\text{Male, Height: 178 cm},\quad \text{Neck: 39.0 cm},\quad \text{Waist (Abdominal): 91.0 cm},\quad \text{Weight: 85.0 kg}",
             "A 30-year-old male records standard circumference measurements using a non-elastic anthropometric measuring tape."),
            ("Step 2: Calculate U.S. Navy Body Fat Percentage",
             r"\%BF = 495 / \left[1.0324 - 0.19077 \log_{10}(\text{Waist} - \text{Neck}) + 0.15456 \log_{10}(\text{Height})\right] - 450 = 18.8\%",
             "Applying the logarithmic U.S. Navy formula yields 18.8% body fat."),
            ("Step 3: Calculate Total Fat Mass and Fat-Free Lean Body Mass (LBM)",
             r"\text{Fat Mass} = 85.0 \times 0.188 = 15.98\text{ kg},\quad \text{Lean Body Mass} = 85.0 - 15.98 = 69.02\text{ kg}",
             'The individual carries <strong>69.02 kg of Lean Body Mass</strong> and 15.98 kg of adipose tissue. Cross-check your overall body mass index with our <a href="bmi-calculator.html">BMI Calculator</a> and plan nutrition with our <a href="calorie-calculator.html">Calorie Calculator</a>.')
        ],
        "final_result": "Body Composition: Body Fat: 18.8% (Healthy Fitness Tier) | Lean Body Mass: 69.0 kg | Fat Mass: 16.0 kg | DEXA Validated.",
        "faqs": [
            ("How accurate is the U.S. Navy circumference method compared to DEXA?",
             "Multiple clinical validation studies demonstrate the U.S. Navy equation correlates within ±3.0% to 3.5% of laboratory DEXA and hydrostatic underwater weighing scans, provided tape measurements are taken with tension-calibrated measuring tapes."),
            ("What is considered a healthy body fat percentage for men and women?",
             "For men: Essential fat (2%–5%), Athletes (6%–13%), Fitness (14%–17%), Acceptable (18%–24%), Obese (≥25%). For women: Essential fat (10%–13%), Athletes (14%–20%), Fitness (21%–24%), Acceptable (25%–31%), Obese (≥32%). Women require higher essential fat for reproductive endocrine health."),
            ("Where should the waist measurement be taken for the Navy calculation?",
             "For men, measure horizontally around the abdomen across the navel (belly button) at the end of normal expiration. For women, measure at the narrowest point of the natural waistline between the rib cage and hips, and measure hips around the widest circumference of the buttocks."),
            ("Can you lose body fat in specific areas through targeted exercises (spot reduction)?",
             "No. Anatomical physiology demonstrates spot reduction is impossible. Fat is mobilized systemically from triglycerides stored throughout the body into free fatty acids via lipolysis, regulated by genetics and hormones rather than which muscles are exercised.")
        ]
    },

    "ideal-weight-calculator.html": {
        "verification": "Devine, Robinson, Miller, and Hamwi Clinical Formulas",
        "standards": [
            ("Clinical Formulas", "Devine (1974), Robinson (1983), Miller (1983), and Hamwi (1964) Equations"),
            ("Pharmacological Standard", "Devine Ideal Body Weight (IBW) used for clinical drug clearance (creatinine)"),
            ("BMI Correlation", "Correlated with WHO Normal Weight Range (BMI 18.5 – 24.9 kg/m²)"),
            ("Clinical Adjustments", "Frame size adjustments (small, medium, large frame via wrist circumference)")
        ],
        "example_title": "Clinical Case Study: Adult Medical Ideal Body Weight Quantification",
        "example_badge": "Real-World Clinical Problem",
        "steps": [
            ("Step 1: Record Biological Sex and Stature",
             r"\text{Male},\quad \text{Height: 5 ft 10 in}\ (70\text{ inches} = 177.8\text{ cm})",
             "A male patient measuring 5 feet 10 inches requires ideal body weight calculation for medication dosing."),
            ("Step 2: Calculate Devine Clinical Ideal Body Weight (IBW)",
             r"\text{IBW}_{Devine} = 50.0\text{ kg} + 2.3\text{ kg} \times (\text{Height in inches} - 60) = 50.0 + 2.3 \times 10 = 73.0\text{ kg}\ (160.9\text{ lbs})",
             "The Devine formula yields an ideal body weight of 73.0 kg (160.9 lbs)."),
            ("Step 3: Compare Across Robinson and Miller Medical Formulas",
             r"\text{Robinson} = 72.6\text{ kg}\ (160.1\text{ lbs}),\quad \text{Miller} = 71.2\text{ kg}\ (157.0\text{ lbs}),\quad \text{Hamwi} = 75.3\text{ kg}\ (166.0\text{ lbs})",
             "The consensus medical ideal weight range across all four peer-reviewed formulas is 71.2 kg to 75.3 kg (157 to 166 lbs)."),
            ("Step 4: Verify WHO Normal Healthy BMI Range (18.5 to 24.9 kg/m²)",
             r"\text{WHO Range} = 18.5 \times (1.778)^2\text{ to } 24.9 \times (1.778)^2 = 58.5\text{ kg to } 78.7\text{ kg}\ (129\text{ to } 173.5\text{ lbs})",
             'All clinical formulas sit securely in the upper tier of the WHO normal weight range. Assess your current index with our <a href="bmi-calculator.html">BMI Calculator</a> and evaluate body fat with our <a href="body-fat-calculator.html">Body Fat Calculator</a>.')
        ],
        "final_result": "Consensus Clinical IBW: 73.0 kg (161 lbs) | Multi-Formula Band: 71.2 – 75.3 kg | WHO Healthy Range: 58.5 – 78.7 kg.",
        "faqs": [
            ("Why did Dr. B.J. Devine create the Ideal Body Weight formula?",
             "Dr. Devine originally published the formula in 1974 to standardize dosages of hydrophilic medications (such as aminoglycoside antibiotics and theophylline) and calculate renal clearance. Hydrophilic drugs distribute predominantly into lean body mass rather than adipose tissue."),
            ("Why do clinical formulas give different results for men and women?",
             "Men have higher average bone mineral density, greater skeletal frame mass, and higher natural lean muscle mass compared to women of the identical height. Consequently, ideal weight equations assign a lower baseline and smaller height multiplier for females."),
            ("How does body frame size influence ideal body weight?",
             "Body frame size (determined by measuring wrist circumference relative to height) shifts ideal body weight by approximately ±10%. An individual with a large bone structure can comfortably carry 10% more mass while maintaining optimal cardiovascular biomarkers."),
            ("Is being slightly above your ideal body weight unhealthy?",
             "Not necessarily. If excess weight is comprised of skeletal muscle mass and cardiovascular fitness is high, carrying weight slightly above IBW poses minimal metabolic risk. Visceral abdominal fat (measured via waist circumference) is a far stronger predictor of disease than total weight.")
        ]
    },

    "water-intake-calculator.html": {
        "verification": "National Academies of Sciences & EFSA Hydration Standards",
        "standards": [
            ("Clinical Baseline", "30–35 mL of water per kilogram of body weight daily"),
            ("Activity Adjustment", "Add 350–500 mL per 30 minutes of moderate-to-vigorous exercise"),
            ("Climate Compensation", "Add 250–500 mL for hot/humid environments or high-altitude respiration"),
            ("Hydration Guideline", "European Food Safety Authority (EFSA) Adequate Daily Intake Standards")
        ],
        "example_title": "Physiological Case Study: Daily Hydration for Active Adult in Warm Climate",
        "example_badge": "Real-World Health Problem",
        "steps": [
            ("Step 1: Determine Baseline Physiological Hydration from Body Weight",
             r"\text{Weight: 80.0 kg} \implies V_{base} = 80 \times 35\text{ mL} = 2{,}800\text{ mL}\ (2.80\text{ Liters})",
             "An 80 kg individual requires 2.80 Liters of water daily purely for cellular metabolism, renal filtration, and basal respiration."),
            ("Step 2: Add Exercise Perspiration Replenishment (45 Minutes Training)",
             r"V_{exercise} = \frac{45\text{ min}}{30\text{ min}} \times 400\text{ mL} = 600\text{ mL}\ (0.60\text{ Liters})",
             "Replacing fluid lost through active sweat during 45 minutes of training requires an additional 600 mL."),
            ("Step 3: Add Ambient Climate Compensation (Warm/Humid)",
             r"V_{climate} = +350\text{ mL}\ (0.35\text{ Liters})",
             "Warm weather elevates perspiration and evaporative skin cooling, adding 350 mL."),
            ("Step 4: Compute Total Recommended Daily Hydration Target",
             r"V_{total} = 2{,}800 + 600 + 350 = 3{,}750\text{ mL}\ (3.75\text{ Liters / 127 oz})",
             'Total recommended intake is <strong>3.75 Liters (approx. 15-16 standard glasses)</strong> daily. Balance metabolic nutrition with our <a href="calorie-calculator.html">Calorie Calculator</a> and visit our <a href="health.html">Health Hub</a>.')
        ],
        "final_result": "Hydration Prescription: Baseline: 2.80 L | Exercise: +0.60 L | Climate: +0.35 L | Total Target: 3.75 Liters/Day (127 fl oz).",
        "faqs": [
            ("Does the '8 glasses of water a day' rule have scientific backing?",
             "The popular '8×8 rule' (eight 8-ounce glasses = 64 oz / 1.9 L) is a simple public health guideline, but it ignores individual body weight, gender, ambient climate, and physical activity. An 85 kg athlete exercising in summer requires more than double the water of a 55 kg sedentary individual in winter."),
            ("Do tea, coffee, and food count toward daily fluid intake?",
             "Yes. Approximately 20% of daily hydration comes from water contained in solid foods (fruits, vegetables, soups). Caffeinated beverages like coffee and tea count toward daily hydration; contrary to popular myth, their mild diuretic effect does not offset the volume of fluid consumed."),
            ("What are the primary clinical indicators of dehydration?",
             "The simplest clinical check is urine color: pale straw or light yellow indicates optimal hydration; dark amber indicates dehydration. Other symptoms include dry mouth, fatigue, headache, decreased skin turgor, and reduced cognitive focus."),
            ("Can you drink too much water (Hyponatremia)?",
             "Yes. Excessive water intake (e.g., several liters within an hour) without electrolyte replenishment can dilute blood sodium levels below 135 mmol/L, causing exercise-associated hyponatremia (water intoxication), leading to cerebral edema and requiring emergency medical care.")
        ]
    },

    "percentage-calculator.html": {
        "verification": "Standard Mathematical Proportions & Relative Delta Standards",
        "standards": [
            ("Core Equations", "Percentage Of: P = (V / Total) × 100 | Percentage Change: Δ% = [(V2 - V1) / V1] × 100"),
            ("Difference Formula", "Percentage Difference: %Diff = [|V1 - V2| / ((V1 + V2) / 2)] × 100"),
            ("Commercial Uses", "Sales growth, inflation rate, discount markdowns, scientific error margins"),
            ("Numerical Precision", "High-precision floating point arithmetic")
        ],
        "example_title": "Analytical Case Study: Quarterly Corporate Revenue Growth Analysis",
        "example_badge": "Real-World Analytical Problem",
        "steps": [
            ("Step 1: Record Baseline and Comparison Revenue Figures",
             r"Q1\text{ Revenue} = \$125{,}000,\quad Q2\text{ Revenue} = \$165{,}000",
             "A company's quarterly revenue expands from $125,000 in Q1 to $165,000 in Q2."),
            ("Step 2: Calculate Absolute Dollar Increase",
             r"\Delta = \$165{,}000 - \$125{,}000 = +\$40{,}000",
             "Gross revenue grew by $40,000."),
            ("Step 3: Calculate Relative Percentage Growth (Percentage Change)",
             r"\%\text{ Growth} = \frac{\$40{,}000}{\$125{,}000} \times 100 = +32.00\%",
             "Revenue grew by exactly +32.00% relative to Q1."),
            ("Step 4: Calculate Q2 as a Percentage of Q1",
             r"\text{Ratio\%} = \frac{\$165{,}000}{\$125{,}000} \times 100 = 132.00\%",
             'Q2 represents 132.00% of Q1 performance. Simplify proportional shares with our <a href="fraction-calculator.html">Fraction Calculator</a>, scale funding with our <a href="ratio-calculator.html">Ratio Calculator</a>, and visit our <a href="math.html">Math Hub</a>.')
        ],
        "final_result": "Statistical Analysis: Absolute Growth: +$40,000 | Relative Growth: +32.00% | Proportional Ratio: 132.00% of Baseline.",
        "faqs": [
            ("What is the difference between percentage change and percentage difference?",
             "Percentage change has a clear direction from an older baseline to a newer value [ (New - Old) / Old × 100 ]. Percentage difference compares two values where neither is a baseline, dividing absolute difference by their average [ |A - B| / ((A + B) / 2) × 100 ]."),
            ("What is the difference between percentage and percentile?",
             "A percentage is a mathematical proportion out of 100 (e.g., scoring 85% on an exam means answering 85 out of 100 questions correctly). A percentile indicates rank relative to a population (e.g., scoring in the 85th percentile means scoring higher than 85% of all test takers)."),
            ("How do you calculate percentage increase or decrease backwards?",
             "To find the original price before a 25% increase that resulted in $125: divide by (1 + 0.25), giving $125 / 1.25 = $100. To find the original price before a 20% discount that resulted in $80: divide by (1 - 0.20), giving $80 / 0.80 = $100."),
            ("What is a basis point (bps)?",
             "A basis point is one hundredth of a percentage point (0.01% or 0.0001 in decimal). Commonly used in finance and interest rates: an increase of 50 basis points on a 4.50% interest rate raises it to 5.00%.")
        ]
    },

    "fraction-calculator.html": {
        "verification": "Euclidean Algorithm & Rational Arithmetic Standards",
        "standards": [
            ("Core Operations", "Addition, Subtraction, Multiplication, Division of Rational Numbers"),
            ("Simplification Engine", "Euclidean Greatest Common Divisor (GCD) Lowest Common Denominator (LCD)"),
            ("Conversions", "Proper Fractions, Improper Fractions, and Mixed Numbers"),
            ("Decimal Representation", "Terminating and Recurring Decimal Representation")
        ],
        "example_title": "Mathematical Case Study: Multi-Term Rational Fraction Arithmetic",
        "example_badge": "Real-World Mathematical Problem",
        "steps": [
            ("Step 1: Set Up Addition of Unequal Denominator Fractions",
             r"\frac{5}{12} + \frac{7}{18}",
             "Add two fractions with differing denominators: 5/12 and 7/18."),
            ("Step 2: Find the Least Common Denominator (LCD) via LCM",
             r"\text{LCM}(12, 18) = 36,\quad \frac{5 \times 3}{12 \times 3} = \frac{15}{36},\quad \frac{7 \times 2}{18 \times 2} = \frac{14}{36}",
             "The least common multiple of 12 and 18 is 36. Converting both fractions yields 15/36 and 14/36."),
            ("Step 3: Add Numerators and Simplify via GCD",
             r"\frac{15 + 14}{36} = \frac{29}{36}",
             "Adding numerators yields 29/36. Since 29 is prime, 29/36 is in irreducible lowest terms."),
            ("Step 4: Convert to Decimal and Percentage Equivalence",
             r"\frac{29}{36} \approx 0.80555\dots = 80.56\%",
             'The fraction equals approximately 0.8056 (80.56%). Model proportional ratios with our <a href="ratio-calculator.html">Ratio Calculator</a> and analyze percentages with our <a href="percentage-calculator.html">Percentage Calculator</a>.')
        ],
        "final_result": "Calculation Result: 5/12 + 7/18 = 29/36 | Irreducible Form: 29/36 | Decimal: 0.80556 | Percentage: 80.56%.",
        "faqs": [
            ("How do you divide two fractions?",
             "To divide fractions, multiply the first fraction by the reciprocal (the inverted form) of the second fraction: (a/b) ÷ (c/d) = (a/b) × (d/c) = (a × d) / (b × c). For example: (3/4) ÷ (2/5) = (3/4) × (5/2) = 15/8 = 1 7/8."),
            ("How do you convert an improper fraction to a mixed number?",
             "Divide the numerator by the denominator. The whole integer quotient becomes the whole number, the remainder becomes the new numerator, and the original denominator stays the same. For example: 25/7 = 3 with remainder 4, written as 3 4/7."),
            ("Why must denominators match when adding or subtracting fractions?",
             "The denominator represents the size or number of equal parts that make up a whole unit. You cannot directly combine parts of different sizes (e.g. thirds and fifths) without first converting them into equal-sized common fractional units."),
            ("What is an irreducible fraction in lowest terms?",
             "A fraction a/b is in lowest terms (irreducible) when the numerator and denominator share no common factors other than 1, meaning their Greatest Common Divisor is 1 [GCD(a, b) = 1].")
        ]
    },

    "ratio-calculator.html": {
        "verification": "Euclidean Proportional Scaling & Ratio Division Standards",
        "standards": [
            ("Core Mathematics", "Direct & Inverse Proportion: a : b = c : d ⟹ a × d = b × c"),
            ("Proportional Sharing", "Part Allocation: Share = (Part / Total Parts) × Total Quantity"),
            ("Reduction Engine", "Euclidean GCD Integer Simplification"),
            ("Scaling Dimensions", "Scale factor enlargement, reduction, aspect ratio preservation")
        ],
        "example_title": "Engineering Case Study: Industrial Concrete Mix Proportional Scaling",
        "example_badge": "Real-World Engineering Problem",
        "steps": [
            ("Step 1: Define Target Material Ratio (Cement : Sand : Aggregate)",
             r"\text{Ratio: 1 : 2 : 4 (Total Parts = 1 + 2 + 4 = 7)}",
             "An on-site concrete batching plant must mix 2,800 kg of dry materials in a strict 1:2:4 ratio."),
            ("Step 2: Calculate One Unit Share Value",
             r"\text{One Share} = \frac{2{,}800\text{ kg}}{7\text{ parts}} = 400.0\text{ kg/part}",
             "Each part represents exactly 400 kg of material."),
            ("Step 3: Allocate Proportional Constituent Masses",
             r"\text{Cement (1 part)} = 400\text{ kg},\quad \text{Sand (2 parts)} = 800\text{ kg},\quad \text{Aggregate (4 parts)} = 1{,}600\text{ kg}",
             "The mix requires 400 kg of cement, 800 kg of sand, and 1,600 kg of coarse stone gravel."),
            ("Step 4: Cross-Check Scale Reduction and Equality",
             r"400 : 800 : 1{,}600 \implies \text{Divide by GCD (400)} = 1 : 2 : 4",
             'The proportion reduces to 1:2:4. Calculate finished concrete yields with our <a href="concrete-calculator.html">Concrete Calculator</a> and visit our <a href="math.html">Math Hub</a>.')
        ],
        "final_result": "Proportional Allocation: Total: 2,800 kg | Cement: 400 kg | Sand: 800 kg | Aggregate: 1,600 kg | Preserves 1:2:4 Ratio.",
        "faqs": [
            ("How do you solve for an unknown in a ratio proportion (a : b = c : x)?",
             "Use cross-multiplication: multiply the outer terms (extremes) and set them equal to the product of the inner terms (means): a × x = b × c, so x = (b × c) / a. For example, if 3 : 5 = 12 : x, then x = (5 × 12) / 3 = 60 / 3 = 20."),
            ("What is the difference between a ratio and a proportion?",
             "A ratio is a mathematical comparison of two or more quantities showing relative sizes (e.g., 3:2). A proportion is a mathematical statement asserting that two ratios are equal (e.g., 3/2 = 6/4)."),
            ("How do you simplify a ratio containing fractions or decimals?",
             "Multiply all terms in the ratio by the least common denominator of the fractions (or by 10, 100 to eliminate decimals), then divide all terms by their Greatest Common Divisor (GCD) until all terms are irreducible integers."),
            ("What is aspect ratio in video and photography displays?",
             "Aspect ratio is the proportional relationship between the width and height of an image or screen. Common standard ratios include 16:9 (widescreen high-definition video), 4:3 (traditional television), and 1:1 (square social media formats).")
        ]
    },

    "gpa-calculator.html": {
        "verification": "North American Collegiate 4.0 & ECTS Credit Weighted Grade Standards",
        "standards": [
            ("Grading Scale", "Standard 4.0 Scale: A=4.0, A-=3.7, B+=3.3, B=3.0, B-=2.7, C+=2.3, C=2.0, D=1.0, F=0.0"),
            ("Weighting Formula", "GPA = Sum(Grade Points × Course Credit Hours) / Sum(Credit Hours)"),
            ("Academic Standing", "Dean's List / Cum Laude (≥3.50), Good Standing (≥2.00), Academic Probation (<2.00)"),
            ("Honors Weighting", "Weighted AP / Honors / Graduate courses receive +0.5 to +1.0 grade point bump")
        ],
        "example_title": "Academic Case Study: Engineering Undergraduate Semester GPA Scoring",
        "example_badge": "Real-World Academic Problem",
        "steps": [
            ("Step 1: Compile Course Enrolment, Credit Hours, and Letter Grades",
             r"\text{Calculus IV (4 cr, A=4.0), Heat Transfer (3 cr, A-=3.7), Circuit Analysis (3 cr, B+=3.3), Lab (1 cr, A=4.0)}",
             "A student completes 11 semester credit hours across 4 engineering courses."),
            ("Step 2: Calculate Weighted Quality Points per Course",
             r"\text{Calculus: } 4 \times 4.0 = 16.0,\quad \text{Heat Transfer: } 3 \times 3.7 = 11.1,\quad \text{Circuits: } 3 \times 3.3 = 9.9,\quad \text{Lab: } 1 \times 4.0 = 4.0",
             "Multiplying each course grade point value by its credit hour weight produces individual course quality points."),
            ("Step 3: Sum Total Quality Points and Compute Semester GPA",
             r"\text{Total Points} = 16.0 + 11.1 + 9.9 + 4.0 = 41.0,\quad \text{GPA} = \frac{41.0}{11.0} = 3.727",
             'The student achieves a <strong>3.727 Semester GPA</strong>, qualifying for the Dean\'s Honors List! Explore academic ratios with our <a href="ratio-calculator.html">Ratio Calculator</a> and visit our <a href="math.html">Math Hub</a>.')
        ],
        "final_result": "Academic Standing: Total Credits: 11 | Quality Points: 41.0 | Semester GPA: 3.727 (Dean's List / Magna Cum Laude Tier).",
        "faqs": [
            ("How does a weighted GPA differ from an unweighted GPA?",
             "An unweighted GPA treats every course identically on a 4.0 scale regardless of course rigor. A weighted GPA accounts for both credit hours and course difficulty, awarding extra quality points (e.g., 5.0 for AP/IB/Honors courses) to reflect higher academic challenge."),
            ("How do I calculate cumulative GPA across multiple semesters?",
             "Sum all quality points earned across all completed semesters and divide by the total cumulative credit hours attempted across those semesters. Never simply average semester GPA numbers together unless all semesters had identical credit totals."),
            ("Do Pass/Fail or Withdrawn (W) courses impact GPA?",
             "Standard letter grades of Pass (P), Satisfactory (S), or Withdrawn (W) award credit hours toward degree completion but carry zero grade points and are excluded from GPA calculation formulas."),
            ("What GPA is required for Latin Honors at graduation?",
             "Collegiate thresholds vary, but standard benchmarks are: Cum Laude (with praise, typically top 20% or 3.50–3.69 GPA), Magna Cum Laude (with high praise, top 10% or 3.70–3.89 GPA), and Summa Cum Laude (with highest praise, top 5% or 3.90–4.00 GPA).")
        ]
    },

    "date-difference-calculator.html": {
        "verification": "ISO 8601 Calendar Standards & Gregorian Intercalary Leap-Year Rules",
        "standards": [
            ("Calendar Engine", "Proleptic Gregorian Calendar (28–31 Day Months & 400-Year Leap Rules)"),
            ("Time Formats", "ISO 8601 YYYY-MM-DD Representation"),
            ("Business Days", "Statutory Working Days (Excluding Weekends & Public Holidays)"),
            ("Output Formats", "Years/Months/Days, Total Elapsed Days, Total Hours, Minutes, and Seconds")
        ],
        "example_title": "Project Management Case Study: Turnaround Project Duration Tracking",
        "example_badge": "Real-World Chronology Problem",
        "steps": [
            ("Step 1: Set Project Start Date and Contractual Handover Date",
             r"\text{Start Date: February 15, 2024},\quad \text{Handover Date: November 20, 2025}",
             "A plant maintenance overhaul contract spans from February 15, 2024 through November 20, 2025."),
            ("Step 2: Factor Gregorian Leap Year (2024 has 29 Days in February)",
             r"\text{Elapsed Time: 1 Year, 9 Months, 5 Days}\ (644\text{ Total Calendar Days})",
             "Accounting for the extra intercalary day in leap year 2024 gives exactly 644 calendar days."),
            ("Step 3: Deduct Non-Working Weekends and Statutory Public Holidays",
             r"644\text{ Calendar Days} - 184\text{ Weekend Days} - 16\text{ Holidays} = 444\text{ Working Shifts}",
             'Deducting 92 weekends and 16 holidays leaves 444 productive working shifts. Track milestones and chronological age with our <a href="age-calculator.html">Age Calculator</a> and visit our <a href="datetime.html">Date & Time Hub</a>.')
        ],
        "final_result": "Chronological Span: 1 Year, 9 Months, 5 Days (644 Calendar Days) | Productive Work Shifts: 444 Days | Total Hours: 15,456.",
        "faqs": [
            ("How does leap year affect day count calculations?",
             "Years evenly divisible by 4 are leap years, except for century years not divisible by 400 (e.g., 1900 was not a leap year, 2000 was a leap year, 2100 will not be). A leap year introduces February 29 (366 days total), shifting day counts and weekday alignment."),
            ("Why does dividing days by 30 or 365 produce inaccuracies?",
             "Calendar months vary from 28 to 31 days. Dividing total days by an average like 30 or 365.25 generates discrepancies of several days across specific calendar spans. Exact chronological calculations must count actual calendar days in each individual month."),
            ("What is Julian Day Number (JDN)?",
             "Julian Day Number is a continuous count of days elapsed since the beginning of the Julian period (January 1, 4713 BC). Astronomers and computer scientists use JDN to compute elapsed time between historical events without dealing with calendar month anomalies."),
            ("How do business day calculations handle regional weekend conventions?",
             "In Western countries, weekends comprise Saturday and Sunday (5-day working week). In several Middle Eastern jurisdictions, the weekend runs Friday and Saturday (or Friday and half of Saturday). Professional tools allow custom selection of non-working days.")
        ]
    },

    "age-calculator.html": {
        "verification": "Civil Registration & Chronological Age Determination Standards",
        "standards": [
            ("Legal Age Standard", "Civil Law Age Attainment on Anniversary of Date of Birth"),
            ("Leap Year Rule", "February 29 Birthdays legally advance on March 1 in Non-Leap Years"),
            ("Granular Units", "Years, Months, Days, Total Weeks, Total Hours, Minutes, and Seconds"),
            ("Countdown Engine", "Next Birthday Day-of-Week & Milestone Countdown Timer")
        ],
        "example_title": "Legal Chronology Case Study: Exact Chronological Age Quantification",
        "example_badge": "Real-World Chronology Problem",
        "steps": [
            ("Step 1: Record Date of Birth and Current Target Reference Date",
             r"\text{Date of Birth: August 24, 1996},\quad \text{Reference Date: October 1, 2026}",
             "Calculate the exact chronological age of an individual born on August 24, 1996 on October 1, 2026."),
            ("Step 2: Calculate Elapsed Calendar Years, Months, and Days",
             r"\text{Age} = 30\text{ Years},\ 1\text{ Month},\ 7\text{ Days}",
             "From August 24, 1996 to August 24, 2026 is exactly 30 years. From August 24 to September 24 is 1 month. From September 24 to October 1 is 7 days."),
            ("Step 3: Convert into Total Elapsed Days, Hours, and Minutes",
             r"\text{Total Days} = 10{,}995\text{ Days},\quad \text{Total Hours} = 263{,}880\text{ Hours}",
             'Total lifespan elapsed equals 10,995 days. Calculate milestone durations with our <a href="date-difference-calculator.html">Date Difference Calculator</a> and visit our <a href="datetime.html">Date & Time Hub</a>.')
        ],
        "final_result": "Chronological Status: 30 Years, 1 Month, 7 Days | Total Days: 10,995 | Next Birthday: Tuesday, August 24, 2027.",
        "faqs": [
            ("When does someone born on February 29 legally turn a year older in non-leap years?",
             "Under English Common Law and most United States jurisdictions, a person born on February 29 legally advances age on March 1 in non-leap years. In Taiwan and certain European legal systems, age legally advances on February 28."),
            ("Why is calculating age by dividing total days by 365.25 inaccurate?",
             "Dividing total elapsed days by 365.25 provides an approximate statistical age, but frequently misstates your true birthday age by a day or two depending on whether leap years occurred recently. Exact chronological age must match birth dates across calendar years."),
            ("What is chronological age versus biological age?",
             "Chronological age is the exact elapsed time since your birth. Biological age reflects cellular and physiological health (cardiovascular function, telomere length, DNA methylation biomarkers), which can be younger or older than chronological age based on lifestyle."),
            ("How does traditional East Asian age reckoning differ from Western age?",
             "In traditional Korean and Chinese systems, an infant was considered 1 year old at birth, and everyone gained another year simultaneously on the Lunar New Year or January 1st. South Korea officially adopted the international Western age system for all legal and official matters in 2023.")
        ]
    },

    "torque-calculator.html": {
        "verification": "AGMA 6013 & ISO Mechanical Power-Torque-Speed Equations",
        "standards": [
            ("Core Equations", "Rotational Power: P = T × ω = T × (2π × N / 60) ⟹ T = 9,550 × P(kW) / N(RPM)"),
            ("Imperial Formula", "Horsepower Torque: T(lb-ft) = 5,252 × HP / N(RPM)"),
            ("Gear Reduction", "T_output = T_input × Gear Ratio × Transmission Efficiency (η)"),
            ("Standard Units", "Newton-meters (N·m), Pound-feet (lb-ft), Kilowatts (kW), and RPM")
        ],
        "example_title": "Mechanical Engineering Case Study: Industrial Conveyor Drive Sizing",
        "example_badge": "Real-World Mechanical Engineering Problem",
        "steps": [
            ("Step 1: Define Electric Drive Motor Power and Synchronous Shaft Speed",
             r"P = 15.0\text{ kW},\quad N_{motor} = 1{,}450\text{ RPM}",
             "A 15 kW 4-pole industrial electric motor operates at 1,450 RPM full-load speed."),
            ("Step 2: Calculate Motor Continuous Shaft Torque via the 9,550 Constant",
             r"T_{motor} = 9{,}550 \times \frac{P_{kW}}{N_{RPM}} = 9{,}550 \times \frac{15.0}{1{,}450} = 98.79\text{ N}\cdot\text{m}\ (72.86\text{ lb-ft})",
             "The motor shaft delivers 98.79 Newton-meters of continuous rotational torque."),
            ("Step 3: Calculate Output Torque After 10:1 Helical Gearbox Reduction (96% Efficiency)",
             r"T_{output} = T_{motor} \times \text{Ratio} \times \eta = 98.79 \times 10 \times 0.96 = 948.4\text{ N}\cdot\text{m}",
             'After gear reduction, output torque multiplies tenfold to 948.4 N·m at 145 RPM. Size pump and piping systems with our <a href="pipe-sizing-calculator.html">Pipe Sizing Calculator</a> and explore our <a href="mechanical.html">Mechanical Engineering Hub</a>.')
        ],
        "final_result": "Drive Sizing: Motor Torque: 98.79 N·m (72.9 lb-ft) | Gearbox Output: 948.4 N·m @ 145 RPM | AGMA Heavy Industrial Duty.",
        "faqs": [
            ("Where does the 9,550 constant come from in the torque formula?",
             "Mechanical power is Power (Watts) = Torque (N·m) × Angular Velocity (rad/s). Since ω = 2π·N / 60, Power (kW) = [Torque × 2π × N] / (60 × 1,000). Inverting the constant: 60,000 / (2π) = 9,549.3 ≈ 9,550. Thus, Torque (N·m) = 9,550 × Power(kW) / RPM."),
            ("Where does the 5,252 constant come from in horsepower torque?",
             "One horsepower is defined as 550 foot-pounds per second (33,000 ft-lb/min). Dividing 33,000 by 2π yields 5,252.1. Consequently, horsepower and torque curves on an engine dynamometer always cross at exactly 5,252 RPM."),
            ("What is the difference between torque and work?",
             "Both torque and work share identical dimensional units (Newton-meters). However, work is a scalar dot product where force causes linear displacement in the direction of motion (measured in Joules). Torque is a vector cross product representing rotational force about an axis, where no movement needs to occur for static torque to exist."),
            ("How does gear reduction affect motor torque and rotational speed?",
             "A speed-reducing gearbox (e.g. 5:1 ratio) reduces output rotational speed by a factor of 5 while multiplying output torque by a factor of 5 (minus frictional gear mesh losses), allowing small motors to move heavy industrial loads.")
        ]
    },

    "unit-converter.html": {
        "verification": "BIPM International System of Units (SI) 9th Edition & NIST SP 811",
        "standards": [
            ("Metrology Standard", "BIPM SI Brochure (9th Edition) & NIST Special Publication 811 Guide for SI"),
            ("Conversion Practice", "IEEE/ASTM SI 10 American National Standard for Metric Practice"),
            ("Supported Dimensions", "Length, Area, Volume, Mass/Weight, Temperature, Pressure, Energy, Power"),
            ("Precision Engine", "Double-precision 64-bit IEEE 754 floating-point conversion factors")
        ],
        "example_title": "Field Metrology Case Study: Multi-Parameter Transnational Engineering Conversion",
        "example_badge": "Real-World Metrology Problem",
        "steps": [
            ("Step 1: Convert Industrial Fluid Pressure (Bar to PSI and Pascals)",
             r"P = 18.5\text{ bar} \implies P_{PSI} = 18.5 \times 14.50377 = 268.32\text{ PSI},\quad P_{Pa} = 1.85\text{ MPa}",
             "An offshore process valve rated at 18.5 bar translates to 268.32 PSI or 1,850,000 Pascals."),
            ("Step 2: Convert Mechanical Drive Power (Kilowatts to Horsepower)",
             r"P_{motor} = 55.0\text{ kW} \implies P_{hp} = 55.0 \times 1.34102 = 73.76\text{ Mechanical Horsepower (hp)}",
             "A 55.0 kW electric motor corresponds to a standard 75 hp American drive motor."),
            ("Step 3: Convert Volumetric Flow Rate (Cubic Meters/Hour to GPM)",
             r"Q = 150.0\text{ m}^3/\text{hr} \implies Q_{GPM} = 150.0 \times 4.402867 = 660.43\text{ US Gallons/Minute (GPM)}",
             'Translating flow specifications yields 660.43 GPM. Size process pipe diameters with our <a href="pipe-sizing-calculator.html">Pipe Sizing Calculator</a> and explore our <a href="converter.html">Unit Converter Hub</a>.')
        ],
        "final_result": "Metrological Conversions: 18.5 bar = 268.32 PSI (1.85 MPa) | 55.0 kW = 73.76 hp | 150.0 m³/hr = 660.43 GPM | 100% Traceable Metrological Precision.",
        "faqs": [
            ("Why is temperature conversion non-linear between Celsius and Fahrenheit?",
             "Unlike units of length or mass which are ratio scales with a shared zero point, Celsius and Fahrenheit are interval scales with different origins. Water freezes at 0°C but 32°F, and boils at 100°C but 212°F (180°F span for 100°C = 9/5 ratio). Hence: °F = (°C × 9/5) + 32."),
            ("What is the exact definition of 1 standard atmosphere (atm)?",
             "By international treaty (BIPM/NIST), 1 standard atmosphere (atm) is defined as exactly 101,325 Pascals (Pa), which equals 1.01325 bar, or approx. 14.6959 PSI, or 760 mmHg at 0°C."),
            ("What is the difference between mass (kg) and weight (Newtons)?",
             "Mass is an intrinsic property measuring the quantity of matter in an object, constant anywhere in the universe. Weight is the gravitational force exerted on that mass (W = m·g). On Earth, 1 kg experiences roughly 9.80665 Newtons (2.20462 lbs) of force."),
            ("How do I avoid cumulative rounding errors during multi-step unit conversions?",
             "Always maintain full 64-bit double-precision floating-point values during intermediate conversion steps, applying rounding only to the final delivered engineering output. Rounding prematurely at each intermediate step compounds error significantly.")
        ]
    }
}

print(f"Loaded {len(THIRD_BATCH_DATA)} third-batch tool definitions.")
