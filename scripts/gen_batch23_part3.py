"""
Batch 23 - Part 3: Health & Fitness Tools
5. tdee-calculator.html (Total Daily Energy Expenditure, BMR, NEAT, EAT, TEF, PAL Multipliers & Metabolic Adaptation)
6. waist-to-height-calculator.html (WHtR, Ashwell Shape Chart, 0.50 Threshold, Visceral Adiposity & NICE Guidelines)
Word count target: >1,100 words in article-body each.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 5. tdee-calculator.html
# -------------------------------------------------------------
TDEE_CALCULATOR_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TDEE Calculator | Total Daily Energy Expenditure & Caloric Sizer</title>
  <meta name="description" content="Calculate your true Total Daily Energy Expenditure (TDEE) and BMR using Mifflin-St Jeor and Katch-McArdle equations. Factors NEAT, EAT, and TEF components.">
  <link rel="canonical" href="https://calchub.com/tdee-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Clinical Total Daily Energy Expenditure (TDEE) Calculator",
    "applicationCategory": "HealthApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0.00",
      "priceCurrency": "USD"
    },
    "description": "Calculates complete Total Daily Energy Expenditure partitioned across Basal Metabolic Rate (BMR), NEAT, EAT, and Thermic Effect of Food (TEF) using validated physiological algorithms."
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Total Daily Energy Expenditure (TDEE) and what are its four components?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Total Daily Energy Expenditure (TDEE) is the total quantity of calories metabolized by the human body over a 24-hour period. It is composed of four distinct physiological thermogenic components: Basal Metabolic Rate (BMR, 60%–75%), Non-Exercise Activity Thermogenesis (NEAT, 15%–30%), Exercise Activity Thermogenesis (EAT, 5%–15%), and the Thermic Effect of Food (TEF, ~10%)."
        }
      },
      {
        "@type": "Question",
        "name": "Which formula is most accurate for estimating Basal Metabolic Rate (BMR)?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Systematic reviews conducted by the Academy of Nutrition and Dietetics established that the Mifflin-St Jeor equation (1990) is the most reliable predictive formula for the general adult population, with an error rate within ±10% in over 80% of subjects. When body fat percentage is accurately known via DEXA or hydrostatic weighing, the Katch-McArdle equation is preferred because it derives BMR directly from metabolically active Fat-Free Mass (FFM)."
        }
      },
      {
        "@type": "Question",
        "name": "Why is NEAT (Non-Exercise Activity Thermogenesis) so important for weight loss?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Pioneering clinical research by Dr. James Levine at the Mayo Clinic demonstrated that NEAT is the single most variable component of human energy expenditure, varying between individuals of similar stature by up to 1,000 to 2,000 kcal per day. NEAT encompasses spontaneous daily physical movement—including walking, posture maintenance, occupational physical activity, and fidgeting. Unconscious down-regulation of NEAT during caloric deficits is the primary driver of metabolic plateaus."
        }
      },
      {
        "@type": "Question",
        "name": "What is metabolic adaptation and how does it affect TDEE during dieting?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Metabolic adaptation (adaptive thermogenesis) refers to the biological reduction in 24-hour energy expenditure beyond what would be predicted purely from lost body mass. As body weight declines, circulating leptin, active thyroid hormone (triiodothyronine, T3), and sympathetic nervous system tone fall, while mitochondrial efficiency increases. Consequently, actual maintenance calories can drop by 10% to 15% below theoretical mathematical formulas."
        }
      },
      {
        "@type": "Question",
        "name": "How should caloric intake be adjusted for fat loss versus muscle gain?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "For sustainable fat loss with lean muscle preservation, clinical guidelines recommend a moderate deficit of 20% to 25% below maintenance TDEE (typically a 400 to 600 kcal/day deficit, targeting roughly 0.5% to 1.0% of body weight loss per week). For muscular hypertrophy, a modest surplus of 5% to 10% above TDEE (200 to 300 kcal/day) fuels muscle protein synthesis while minimizing adipose accumulation."
        }
      }
    ]
  }
  </script>
</head>
<body class="bg-slate-50 text-slate-900">
  <header class="header">
    <div class="header-container">
      <div class="header-logo">
        <a href="index.html" class="logo-link">
          <span class="logo-icon">🧮</span>
          <span class="logo-text">CalcHub</span>
        </a>
      </div>
      <nav class="header-nav">
        <a href="index.html" class="nav-link">Home</a>
        <a href="health.html" class="nav-link active">Health & Fitness</a>
        <a href="finance.html" class="nav-link">Finance</a>
        <a href="engineering.html" class="nav-link">Engineering</a>
      </nav>
    </div>
  </header>

  <main class="main-container">
    <nav class="breadcrumb-nav">
      <ol class="breadcrumb-list">
        <li><a href="index.html">Home</a></li>
        <li><a href="health.html">Health & Fitness</a></li>
        <li class="active">TDEE Calculator</li>
      </ol>
    </nav>

    <div class="page-layout">
      <div class="calculator-container">
        <div class="calculator-card">
          <h1 class="calculator-title">Total Daily Energy Expenditure (TDEE) Calculator</h1>
          <p class="calculator-subtitle">Calculate your precise 24-hour maintenance energy expenditure and partition calories across BMR, NEAT, EAT, and TEF components.</p>

          <form id="tdee-form" class="calculator-form">
            <div class="form-row">
              <div class="form-group col-half">
                <label for="unit-system" class="form-label">Measurement System</label>
                <select id="unit-system" class="form-select">
                  <option value="us" selected>US Customary (lbs, ft/in)</option>
                  <option value="metric">Metric (kg, cm)</option>
                </select>
              </div>
              <div class="form-group col-half">
                <label for="gender" class="form-label">Biological Sex</label>
                <select id="gender" class="form-select">
                  <option value="male" selected>Male (+5 s-factor)</option>
                  <option value="female">Female (-161 s-factor)</option>
                </select>
              </div>
            </div>

            <!-- US Height Inputs -->
            <div id="height-us-group" class="form-row">
              <div class="form-group col-half">
                <label for="height-feet" class="form-label">Height (Feet)</label>
                <input type="number" id="height-feet" class="form-input" min="4" max="7" value="5" required>
              </div>
              <div class="form-group col-half">
                <label for="height-inches" class="form-label">Height (Inches)</label>
                <input type="number" id="height-inches" class="form-input" min="0" max="11" value="10" required>
              </div>
            </div>

            <!-- Metric Height Input -->
            <div id="height-metric-group" class="form-group" style="display: none;">
              <label for="height-cm" class="form-label">Height (Centimeters)</label>
              <input type="number" id="height-cm" class="form-input" min="120" max="230" value="178" step="0.5">
            </div>

            <div class="form-row">
              <div class="form-group col-half">
                <label for="body-weight" class="form-label">Current Weight (<span class="weight-unit">lbs</span>)</label>
                <input type="number" id="body-weight" class="form-input" min="60" max="600" value="175" step="0.5" required>
              </div>
              <div class="form-group col-half">
                <label for="body-age" class="form-label">Age (Years)</label>
                <input type="number" id="body-age" class="form-input" min="15" max="100" value="30" required>
              </div>
            </div>

            <div class="form-group">
              <label for="activity-level" class="form-label">Physical Activity Level (PAL Multiplier)</label>
              <select id="activity-level" class="form-select">
                <option value="1.2">Sedentary (Desk job, minimal physical activity) [PAL 1.20]</option>
                <option value="1.375" selected>Lightly Active (Light exercise / walking 1-3 days/wk) [PAL 1.375]</option>
                <option value="1.55">Moderately Active (Moderate training / sports 3-5 days/wk) [PAL 1.55]</option>
                <option value="1.725">Very Active (Hard training / gym workouts 6-7 days/wk) [PAL 1.725]</option>
                <option value="1.9">Extremely Active (Twice daily training or manual labor job) [PAL 1.90]</option>
              </select>
            </div>

            <button type="submit" class="calculate-btn">Compute Daily Energy Expenditure</button>
          </form>

          <div id="calculator-results" class="results-container" style="display: none;">
            <h2 class="results-heading">Your 24-Hour Energy Profile</h2>

            <div class="results-grid">
              <div class="result-card primary-result">
                <span class="result-label">Maintenance TDEE</span>
                <span id="res-tdee" class="result-value">--</span>
                <span class="result-subtext">Calories to maintain current weight</span>
              </div>

              <div class="result-card highlight-card">
                <span class="result-label">Basal Metabolic Rate (BMR)</span>
                <span id="res-bmr" class="result-value">--</span>
                <span class="result-subtext">Mifflin-St Jeor resting baseline (~65% TDEE)</span>
              </div>

              <div class="result-card">
                <span class="result-label">Fat Loss Deficit (20% Cut)</span>
                <span id="res-cut" class="result-value">--</span>
                <span class="result-subtext">~1 lb fat loss per week (Moderate deficit)</span>
              </div>

              <div class="result-card">
                <span class="result-label">Lean Bulking Surplus (+10%)</span>
                <span id="res-bulk" class="result-value">--</span>
                <span class="result-subtext">Optimal hypertrophy without excess fat</span>
              </div>

              <div class="result-card">
                <span class="result-label">Aggressive Deficit (25% Cut)</span>
                <span id="res-agg-cut" class="result-value">--</span>
                <span class="result-subtext">~1.5 lbs fat loss per week (Strict cut)</span>
              </div>

              <div class="result-card">
                <span class="result-label">Thermic Effect of Food (TEF)</span>
                <span id="res-tef" class="result-value">--</span>
                <span class="result-subtext">~10% of total daily energy budget</span>
              </div>
            </div>

            <div class="summary-box mt-4">
              <h3 class="summary-title">Thermogenic Partitioning Analysis</h3>
              <p id="res-partition-text" class="summary-text">Loading energy balance breakdown...</p>
            </div>
          </div>
        </div>
      </div>

      <aside class="sidebar">
        <div class="sidebar-card">
          <h3 class="sidebar-title">Metabolism &amp; Energy Tools</h3>
          <ul class="sidebar-list">
            <li><a href="bmr-calculator.html">BMR Calculator</a></li>
            <li><a href="calorie-deficit-calculator.html">Calorie Deficit Calculator</a></li>
            <li><a href="calorie-calculator.html">Calorie Maintenance Calculator</a></li>
            <li><a href="macro-calculator.html">Macro Split Calculator</a></li>
            <li><a href="protein-intake-calculator.html">Protein Intake Calculator</a></li>
          </ul>
        </div>
        <div class="sidebar-card mt-4">
          <h3 class="sidebar-title">Clinical Standards</h3>
          <p class="sidebar-text">Based on energy expenditure modeling from the Academy of Nutrition and Dietetics, the Mifflin-St Jeor equation (1990), FAO/WHO/UNU Physical Activity Level (PAL) standards, and Mayo Clinic NEAT research.</p>
        </div>
      </aside>
    </div>

    <article class="article-body">
      <h2>The Physiology of Total Daily Energy Expenditure (TDEE)</h2>
      <p>Human energy metabolism operates under the fundamental laws of thermodynamics: energy cannot be created or destroyed, only transformed from one chemical or mechanical state into another. <strong>Total Daily Energy Expenditure (TDEE)</strong> represents the aggregate number of kilocalories metabolized by the human body across a 24-hour period to sustain cellular organ viability, digest nutrients, maintain core body temperature, perform involuntary postural shifts, and execute mechanical muscular work.</p>

      <p>TDEE is not a static monolithic number; it is a dynamic biological composite partitioned across four distinct physiological compartments:</p>

      $$TDEE = \text{BMR} + \text{NEAT} + \text{EAT} + \text{TEF}$$

      <div class="table-container my-4">
        <table class="data-table">
          <thead>
            <tr>
              <th>Thermogenic Component</th>
              <th>Proportion of Total TDEE</th>
              <th>Physiological Definition</th>
              <th>Primary Biological Determinants</th>
              <th>Inter-Individual Variability</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Basal Metabolic Rate (BMR)</strong></td>
              <td>60% – 75%</td>
              <td>Energy expended in a thermoneutral environment in post-absorptive rest to maintain vital organs (brain, liver, heart, kidneys).</td>
              <td>Fat-Free Mass (FFM), stature, biological sex, age, thyroid hormones ($T_3, T_4$).</td>
              <td>Low to Moderate (±10% across cohorts of identical lean mass).</td>
            </tr>
            <tr>
              <td><strong>Non-Exercise Activity Thermogenesis (NEAT)</strong></td>
              <td>15% – 30%</td>
              <td>Energy expended in spontaneous, non-volitional physical activity (postural shifts, occupational movement, pacing, fidgeting).</td>
              <td>Hypothalamic orexinergic signaling, occupational demands, conscious movement habits.</td>
              <td><strong>Extremely High</strong> (varies by 1,000 to 2,000 kcal/day between individuals).</td>
            </tr>
            <tr>
              <td><strong>Exercise Activity Thermogenesis (EAT)</strong></td>
              <td>5% – 15%</td>
              <td>Energy expended in structured, volitional athletic exercise (resistance training, cycling, running, sports).</td>
              <td>Exercise intensity, duration, mechanical efficiency, training frequency.</td>
              <td>Highly variable depending on weekly athletic commitment.</td>
            </tr>
            <tr>
              <td><strong>Thermic Effect of Food (TEF)</strong></td>
              <td>8% – 12% (~10%)</td>
              <td>Energy expended in the mechanical digestion, intestinal absorption, hepatic deamination, and cellular storage of nutrients.</td>
              <td>Macronutrient distribution: Protein (20–30%), Carbohydrates (5–10%), Fats (0–3%).</td>
              <td>Modest; determined strictly by diet composition and total caloric volume.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Mathematical Modeling of Basal Metabolic Rate (BMR)</h2>
      <p>Because direct calorimetry (measuring human heat dissipation within an airtight chamber) and indirect calorimetry (measuring respiratory oxygen consumption and carbon dioxide production via metabolic cart) are clinically resource-intensive, validated mathematical formulas provide accurate estimations:</p>

      <h3>1. The Mifflin-St Jeor Equation (1990) - General Population Standard</h3>
      <p>Formulated by Dr. Mark Mifflin and colleagues at the University of Nevada School of Medicine, this equation was validated by the Academy of Nutrition and Dietetics as the most dependable equation for individuals of normal, overweight, and obese classifications:</p>

      $$\text{Men: } BMR\text{ (kcal/day)} = 10 \times W\text{ (kg)} + 6.25 \times H\text{ (cm)} - 5 \times A\text{ (years)} + 5$$
      $$\text{Women: } BMR\text{ (kcal/day)} = 10 \times W\text{ (kg)} + 6.25 \times H\text{ (cm)} - 5 \times A\text{ (years)} - 161$$

      <h3>2. The Katch-McArdle Equation (1996) - Lean Body Mass Model</h3>
      <p>When body fat percentage has been determined via clinical dual-energy X-ray absorptiometry (DEXA) or hydrostatic weighing, the Katch-McArdle formula removes the confounding effect of inert adipose tissue, anchoring metabolic burn strictly to metabolically active <strong>Fat-Free Mass ($FFM$)</strong>:</p>

      $$BMR\text{ (kcal/day)} = 370 + (21.6 \times LBM\text{ in kg})$$

      <h2>Physical Activity Level (PAL) Multipliers</h2>
      <p>To scale Basal Metabolic Rate up to Total Daily Energy Expenditure, exercise physiologists utilize the standardized <strong>Physical Activity Level (PAL)</strong> factors established by the Food and Agriculture Organization (FAO), World Health Organization (WHO), and United Nations University (UNU):</p>

      $$TDEE = BMR \times PAL$$

      <ul>
        <li><strong>Sedentary ($PAL = 1.20$):</strong> Minimal movement; typical modern office worker who commutes via motor vehicle, works seated at a computer, and engages in sedentary evening relaxation.</li>
        <li><strong>Lightly Active ($PAL = 1.375$):</strong> Sustains regular recreational movement, logging 5,000 to 7,500 daily steps, or participates in light structured exercise 1 to 3 days per week.</li>
        <li><strong>Moderately Active ($PAL = 1.55$):</strong> Engages in deliberate moderate physical training (gym resistance training, running, swimming) 3 to 5 days per week, logging 8,000 to 10,000 daily steps.</li>
        <li><strong>Very Active ($PAL = 1.725$):</strong> Sustains vigorous physical conditioning 6 to 7 days per week, or maintains a physically demanding job (e.g., active nurse, agricultural worker, warehouse loader).</li>
        <li><strong>Extremely Active ($PAL = 1.90$):</strong> Professional athletes undergoing twice-daily training sessions, elite military personnel, or heavy construction laborers.</li>
      </ul>

      <h2>NEAT: The Great Metabolic Variator</h2>
      <p>Pioneering investigations by Dr. James Levine at the Mayo Clinic Endocrinology Division revolutionized modern understanding of human energy expenditure. Levine demonstrated that while BMR is largely determined by lean mass, <strong>Non-Exercise Activity Thermogenesis (NEAT)</strong> explains the massive discrepancy in weight loss success among individuals on identical diets:</p>
      <ul>
        <li><strong>The 1,000-Calorie Daily Delta:</strong> Two individuals of identical height, body weight, and age can exhibit NEAT differences exceeding <strong>1,000 to 1,500 kcal per day</strong> based purely on occupational movement and spontaneous subconscious motor activity (such as standing versus sitting, taking stairs, pacing while talking, and postural muscle tone).</li>
        <li><strong>Subconscious Down-Regulation in Energy Deficits:</strong> During hypocaloric dieting, the brain perceives an energy crisis and subconsciously dampens spontaneous movement to conserve energy. Individuals often sit more, walk slower, and fidget less without realizing it, dramatically lowering their actual TDEE and causing "unexpected" weight loss plateaus. Tracking daily step count (e.g., maintaining 8,000 to 10,000 steps/day) actively prevents this compensatory collapse in NEAT.</li>
      </ul>

      <h2>Metabolic Adaptation (Adaptive Thermogenesis)</h2>
      <p>During prolonged weight reduction, the human body exhibits <strong>Adaptive Thermogenesis</strong>—a defense mechanism engineered during evolutionary famine to preserve adipose tissue reserves. Groundbreaking research led by Dr. Kevin Hall at the National Institutes of Health (NIH) demonstrates that as adipose mass declines:</p>
      <ul>
        <li>Circulating <strong>leptin</strong> concentrations plummet by over 50%, signaling the hypothalamus to stimulate intense appetite and downregulate basal metabolic burn.</li>
        <li>Active thyroid hormone (triiodothyronine, $T_3$) declines while reverse $T_3$ ($rT_3$) rises, dampening mitochondrial uncoupling protein-1 ($UCP1$) thermogenesis.</li>
        <li>Skeletal muscle mitochondrial efficiency increases, meaning fewer calories are burned to perform the exact same mechanical physical movement.</li>
      </ul>
      <p>Consequently, actual maintenance TDEE at a reduced weight is frequently <strong>100 to 300 kcal lower</strong> than what standard mathematical formulas predict for someone of that new weight who was never obese. Clinicians account for this adaptation by prescribing periodic "diet breaks" at maintenance TDEE to transiently restore leptin, thyroid, and metabolic signaling.</p>

      <h2>Step-by-Step Worked Energy Balance Case Study</h2>
      <p>The following case study illustrates an evidence-based clinical dietetic TDEE calculation and energetic prescription for fat loss:</p>

      <div class="worked-example-card my-4">
        <h3 class="example-title">Energy Balance Case Profile: Fat Loss Deficit Sizing</h3>
        <p><strong>Patient Baseline:</strong> A 32-year-old male marketing manager presents for body composition consultation. Measurements: Height = <strong>5 feet 11 inches (71 inches / 180.34 cm)</strong>, Body Weight = <strong>190 lbs (86.18 kg)</strong>. He lifts weights at the gym 4 days per week and walks during lunch, categorizing him as <strong>Moderately Active ($PAL = 1.55$)</strong>.</p>
        
        <div class="example-step">
          <div class="step-num">Step 1</div>
          <div class="step-content">
            <strong>Calculate Basal Metabolic Rate (BMR) via Mifflin-St Jeor:</strong>
            $$\text{Height in cm} = (5 \times 12 + 11) \times 2.54 = 71 \times 2.54 = 180.34 \text{ cm}$$
            $$BMR = (10 \times 86.18) + (6.25 \times 180.34) - (5 \times 32) + 5$$
            $$BMR = 861.8 + 1127.13 - 160 + 5 = \mathbf{1,833.93 \approx 1,834 \text{ kcal/day}}$$
            His body expends 1,834 kcal every 24 hours purely to sustain coma-state organ viability.
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 2</div>
          <div class="step-content">
            <strong>Calculate Total Daily Energy Expenditure (TDEE):</strong>
            Applying the Moderately Active PAL factor ($1.55$):
            $$TDEE = BMR \times PAL = 1,834 \times 1.55 = \mathbf{2,842.7 \approx 2,843 \text{ kcal/day}}$$
            To maintain his current weight of 190 lbs, he must consume approximately 2,843 kcal daily.
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 3</div>
          <div class="step-content">
            <strong>Compute Thermogenic Partitioning Breakdown:</strong>
            $$\text{Basal Metabolic Rate (BMR)} \approx \mathbf{1,834 \text{ kcal}} \quad (64.5\%)$$
            $$\text{Thermic Effect of Food (TEF, 10\%)} \approx \mathbf{284 \text{ kcal}} \quad (10.0\%)$$
            $$\text{Activity Thermogenesis (NEAT + EAT)} = 2,843 - (1,834 + 284) = \mathbf{725 \text{ kcal}} \quad (25.5\%)$$
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 4</div>
          <div class="step-content">
            <strong>Structure an Evidence-Based Fat Loss Deficit:</strong>
            Prescribing a moderate 20% caloric restriction targets approximately 1 pound of fat loss per week while preventing lean muscle catabolism and metabolic adaptation:
            $$\text{Deficit} = 2,843 \times 0.20 = \mathbf{568.6 \approx 570 \text{ kcal/day}}$$
            $$\text{Target Intake} = 2,843 - 570 = \mathbf{2,273 \approx 2,275 \text{ kcal/day}}$$
            Consuming 2,275 kcal/day creates a weekly deficit of $570 \times 7 = 3,990\text{ kcal}$, generating approximately 1.14 lbs of fat mass reduction per week.
          </div>
        </div>
      </div>
    </article>
  </main>

  <footer class="footer">
    <div class="footer-container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="footer-logo">
            <span class="logo-icon">🧮</span>
            <span class="logo-text">CalcHub</span>
          </div>
          <p class="footer-tagline">Clinical, financial, and engineering reference calculators built with precision and peer-reviewed rigor.</p>
        </div>
        <div class="footer-links">
          <h4 class="footer-heading">Health Calculators</h4>
          <ul class="footer-nav">
            <li><a href="tdee-calculator.html">TDEE Calculator</a></li>
            <li><a href="bmr-calculator.html">BMR Calculator</a></li>
            <li><a href="calorie-deficit-calculator.html">Calorie Deficit Calculator</a></li>
            <li><a href="macro-calculator.html">Macro Split Calculator</a></li>
            <li><a href="protein-intake-calculator.html">Protein Intake Calculator</a></li>
          </ul>
        </div>
        <div class="footer-links">
          <h4 class="footer-heading">Categories</h4>
          <ul class="footer-nav">
            <li><a href="health.html">Health & Fitness</a></li>
            <li><a href="finance.html">Financial Tools</a></li>
            <li><a href="engineering.html">Engineering</a></li>
            <li><a href="index.html">Directory</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. Educational and clinical calculation tools. Consult a registered dietitian for individualized nutrition therapy.</p>
      </div>
    </div>
  </footer>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const form = document.getElementById('tdee-form');
      const unitSystem = document.getElementById('unit-system');
      const genderSelect = document.getElementById('gender');
      const heightUsGroup = document.getElementById('height-us-group');
      const heightMetricGroup = document.getElementById('height-metric-group');
      const heightFeet = document.getElementById('height-feet');
      const heightInches = document.getElementById('height-inches');
      const heightCm = document.getElementById('height-cm');
      const bodyWeightInput = document.getElementById('body-weight');
      const bodyAgeInput = document.getElementById('body-age');
      const activitySelect = document.getElementById('activity-level');
      const weightUnitLabels = document.querySelectorAll('.weight-unit');
      const resultsContainer = document.getElementById('calculator-results');

      unitSystem.addEventListener('change', function() {
        const isMetric = unitSystem.value === 'metric';
        if (isMetric) {
          heightUsGroup.style.display = 'none';
          heightMetricGroup.style.display = 'block';
          weightUnitLabels.forEach(el => el.textContent = 'kg');

          const ft = parseFloat(heightFeet.value) || 5;
          const inc = parseFloat(heightInches.value) || 10;
          const totalIn = (ft * 12) + inc;
          heightCm.value = (totalIn * 2.54).toFixed(1);

          bodyWeightInput.value = (parseFloat(bodyWeightInput.value) * 0.453592).toFixed(1);
          bodyWeightInput.min = '30';
          bodyWeightInput.max = '280';
        } else {
          heightUsGroup.style.display = 'flex';
          heightMetricGroup.style.display = 'none';
          weightUnitLabels.forEach(el => el.textContent = 'lbs');

          const cm = parseFloat(heightCm.value) || 178;
          const totalIn = cm / 2.54;
          heightFeet.value = Math.floor(totalIn / 12);
          heightInches.value = Math.round(totalIn % 12);

          bodyWeightInput.value = (parseFloat(bodyWeightInput.value) / 0.453592).toFixed(1);
          bodyWeightInput.min = '60';
          bodyWeightInput.max = '600';
        }
      });

      form.addEventListener('submit', function(e) {
        e.preventDefault();

        const isMetric = unitSystem.value === 'metric';
        const isMale = genderSelect.value === 'male';
        const age = parseFloat(bodyAgeInput.value) || 30;
        const pal = parseFloat(activitySelect.value) || 1.375;

        let weightKg = 0;
        let heightCmVal = 0;

        if (isMetric) {
          weightKg = parseFloat(bodyWeightInput.value) || 0;
          heightCmVal = parseFloat(heightCm.value) || 0;
        } else {
          const rawWeight = parseFloat(bodyWeightInput.value) || 0;
          weightKg = rawWeight * 0.453592;

          const ft = parseFloat(heightFeet.value) || 0;
          const inc = parseFloat(heightInches.value) || 0;
          heightCmVal = ((ft * 12) + inc) * 2.54;
        }

        if (weightKg <= 0 || heightCmVal <= 0) return;

        // BMR via Mifflin-St Jeor
        const s = isMale ? 5 : -161;
        const bmr = Math.round((10 * weightKg) + (6.25 * heightCmVal) - (5 * age) + s);
        const tdee = Math.round(bmr * pal);

        const moderateCut = Math.round(tdee * 0.80);
        const aggCut = Math.round(tdee * 0.75);
        const leanBulk = Math.round(tdee * 1.10);
        const tef = Math.round(tdee * 0.10);

        // Display results
        document.getElementById('res-tdee').textContent = tdee.toLocaleString() + ' kcal / day';
        document.getElementById('res-bmr').textContent = bmr.toLocaleString() + ' kcal / day';
        document.getElementById('res-cut').textContent = moderateCut.toLocaleString() + ' kcal / day';
        document.getElementById('res-bulk').textContent = leanBulk.toLocaleString() + ' kcal / day';
        document.getElementById('res-agg-cut').textContent = aggCut.toLocaleString() + ' kcal / day';
        document.getElementById('res-tef').textContent = '~' + tef.toLocaleString() + ' kcal / day';

        document.getElementById('res-partition-text').textContent =
          'Your baseline BMR accounts for ' + bmr + ' kcal (the energy required to sustain vital organ systems in complete rest). Physical activity and occupational thermogenesis add approximately ' + Math.round(tdee - bmr - tef) + ' kcal, while digestion (TEF) expends roughly ' + tef + ' kcal. A moderate 20% deficit targeting ' + moderateCut + ' kcal/day creates a safe, sustainable fat loss rate of roughly 1 lb per week.';

        resultsContainer.style.display = 'block';
        resultsContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      });

      // Initial execution
      form.dispatchEvent(new Event('submit'));
    });
  </script>
</body>
</html>
"""

# -------------------------------------------------------------
# 6. waist-to-height-calculator.html
# -------------------------------------------------------------
WAIST_HEIGHT_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Waist to Height Ratio Calculator | Ashwell Shape Chart & Health Risk</title>
  <meta name="description" content="Calculate your Waist-to-Height Ratio (WHtR) using the Ashwell Shape Chart and NICE 2022 guidelines. Screen for visceral adiposity and cardiometabolic risk.">
  <link rel="canonical" href="https://calchub.com/waist-to-height-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Clinical Waist to Height Ratio (WHtR) Calculator",
    "applicationCategory": "HealthApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0.00",
      "priceCurrency": "USD"
    },
    "description": "Calculates Waist-to-Height Ratio (WHtR) and categorizes visceral adiposity and cardiovascular health risk according to NICE 2022 and Ashwell clinical shape standards."
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is the Waist-to-Height Ratio (WHtR) and what is the optimal threshold?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Waist-to-Height Ratio (WHtR) is an anthropometric index calculated by dividing waist circumference by total standing height. Grounded in extensive clinical epidemiology by Dr. Margaret Ashwell and endorsed by the UK National Institute for Health and Care Excellence (NICE 2022), the universal health guidance is: 'Keep your waist circumference to less than half your height' (WHtR < 0.50)."
        }
      },
      {
        "@type": "Question",
        "name": "Why is WHtR considered superior to Body Mass Index (BMI)?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "BMI evaluates only total body weight relative to height squared, making it blind to body composition. BMI cannot distinguish between dense skeletal muscle and harmful visceral fat, falsely labeling muscular athletes as 'overweight' while missing 'normal-weight obesity.' WHtR directly measures central visceral adiposity around the liver and pancreas, serving as a vastly superior predictor of type 2 diabetes, coronary heart disease, and premature mortality."
        }
      },
      {
        "@type": "Question",
        "name": "Where should waist circumference be measured for an accurate WHtR?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Per World Health Organization (WHO) and NIH protocols, waist circumference should be measured with a flexible tensioned tape at the midpoint between the lower palpable margin of the lowest rib and the superior border of the iliac crest (pelvic bone), typically around the level of the umbilicus, at the end of a normal expiration."
        }
      },
      {
        "@type": "Question",
        "name": "What are the clinical health risks of a WHtR greater than 0.60?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A WHtR of 0.60 or higher signifies substantial visceral fat deposition. Meta-analyses demonstrate that individuals with a WHtR ≥ 0.60 face a 3- to 5-fold higher risk of developing type 2 diabetes mellitus, severe hepatic steatosis (NAFLD), hypertension, obstructive sleep apnea, and atherogenic dyslipidemia compared to individuals with a WHtR under 0.50."
        }
      },
      {
        "@type": "Question",
        "name": "Does the 0.50 WHtR rule apply equally to children, men, and women?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. Unlike waist-to-hip ratio and absolute waist circumference cutoffs (which vary significantly between sexes and ethnic groups), the 0.50 WHtR threshold applies uniformly to men, women, children over age 5, and across all major global ethnicities (Caucasian, Asian, Hispanic, African), making it the single most universally applicable screening tool for cardiometabolic risk."
        }
      }
    ]
  }
  </script>
</head>
<body class="bg-slate-50 text-slate-900">
  <header class="header">
    <div class="header-container">
      <div class="header-logo">
        <a href="index.html" class="logo-link">
          <span class="logo-icon">🧮</span>
          <span class="logo-text">CalcHub</span>
        </a>
      </div>
      <nav class="header-nav">
        <a href="index.html" class="nav-link">Home</a>
        <a href="health.html" class="nav-link active">Health & Fitness</a>
        <a href="finance.html" class="nav-link">Finance</a>
        <a href="engineering.html" class="nav-link">Engineering</a>
      </nav>
    </div>
  </header>

  <main class="main-container">
    <nav class="breadcrumb-nav">
      <ol class="breadcrumb-list">
        <li><a href="index.html">Home</a></li>
        <li><a href="health.html">Health & Fitness</a></li>
        <li class="active">Waist to Height Calculator</li>
      </ol>
    </nav>

    <div class="page-layout">
      <div class="calculator-container">
        <div class="calculator-card">
          <h1 class="calculator-title">Waist to Height Ratio (WHtR) Calculator</h1>
          <p class="calculator-subtitle">Screen for central visceral adiposity, cardiometabolic risk, and evaluate your health against the Ashwell Shape Chart and NICE 2022 guidelines.</p>

          <form id="whtr-form" class="calculator-form">
            <div class="form-row">
              <div class="form-group col-half">
                <label for="unit-system" class="form-label">Measurement System</label>
                <select id="unit-system" class="form-select">
                  <option value="us" selected>US Customary (Inches)</option>
                  <option value="metric">Metric (Centimeters)</option>
                </select>
              </div>
              <div class="form-group col-half">
                <label for="gender" class="form-label">Biological Sex</label>
                <select id="gender" class="form-select">
                  <option value="male" selected>Male</option>
                  <option value="female">Female</option>
                </select>
              </div>
            </div>

            <!-- US Inputs -->
            <div id="us-inputs-group">
              <div class="form-row">
                <div class="form-group col-half">
                  <label for="height-feet" class="form-label">Height (Feet)</label>
                  <input type="number" id="height-feet" class="form-input" min="4" max="7" value="5" required>
                </div>
                <div class="form-group col-half">
                  <label for="height-inches" class="form-label">Height (Inches)</label>
                  <input type="number" id="height-inches" class="form-input" min="0" max="11" value="9" required>
                </div>
              </div>
              <div class="form-group">
                <label for="waist-inches" class="form-label">Waist Circumference (Inches)</label>
                <input type="number" id="waist-inches" class="form-input" min="15" max="80" value="33" step="0.25" required>
                <small class="form-hint">Measure at the midpoint between the lowest rib and top of iliac crest.</small>
              </div>
            </div>

            <!-- Metric Inputs -->
            <div id="metric-inputs-group" style="display: none;">
              <div class="form-group">
                <label for="height-cm" class="form-label">Height (Centimeters)</label>
                <input type="number" id="height-cm" class="form-input" min="100" max="240" value="175" step="0.5">
              </div>
              <div class="form-group">
                <label for="waist-cm" class="form-label">Waist Circumference (Centimeters)</label>
                <input type="number" id="waist-cm" class="form-input" min="40" max="200" value="84" step="0.5">
              </div>
            </div>

            <button type="submit" class="calculate-btn">Evaluate Waist-to-Height Ratio</button>
          </form>

          <div id="calculator-results" class="results-container" style="display: none;">
            <h2 class="results-heading">Cardiometabolic Risk Assessment</h2>

            <div class="results-grid">
              <div class="result-card primary-result">
                <span class="result-label">Waist-to-Height Ratio (WHtR)</span>
                <span id="res-whtr-value" class="result-value">--</span>
                <span id="res-whtr-status" class="result-subtext badge-tag">Healthy</span>
              </div>

              <div class="result-card highlight-card">
                <span class="result-label">Ashwell Shape Classification</span>
                <span id="res-ashwell-shape" class="result-value">--</span>
                <span class="result-subtext">Clinical anthropometric tier</span>
              </div>

              <div class="result-card">
                <span class="result-label">Maximum Ideal Waist Limit</span>
                <span id="res-max-ideal-waist" class="result-value">--</span>
                <span class="result-subtext">Exactly 50% of your standing height</span>
              </div>

              <div class="result-card">
                <span class="result-label">Variance from 0.50 Threshold</span>
                <span id="res-waist-variance" class="result-value">--</span>
                <span id="res-variance-note" class="result-subtext">Margin</span>
              </div>

              <div class="result-card">
                <span class="result-label">Cardiovascular Risk Level</span>
                <span id="res-cvd-risk" class="result-value">--</span>
                <span class="result-subtext">NICE 2022 clinical risk category</span>
              </div>

              <div class="result-card">
                <span class="result-label">Ideal Waist Circumference Band</span>
                <span id="res-ideal-waist-range" class="result-value">--</span>
                <span class="result-subtext">WHtR between 0.40 and 0.49</span>
              </div>
            </div>

            <div class="summary-box mt-4">
              <h3 class="summary-title">Clinical Medical Interpretation</h3>
              <p id="res-whtr-clinical" class="summary-text">Loading anthropometric analysis...</p>
            </div>
          </div>
        </div>
      </div>

      <aside class="sidebar">
        <div class="sidebar-card">
          <h3 class="sidebar-title">Body Composition Tools</h3>
          <ul class="sidebar-list">
            <li><a href="bmi-calculator.html">BMI Calculator</a></li>
            <li><a href="body-fat-calculator.html">Body Fat Calculator</a></li>
            <li><a href="ideal-weight-calculator.html">Ideal Body Weight</a></li>
            <li><a href="lean-body-mass-calculator.html">Lean Body Mass Calculator</a></li>
            <li><a href="calorie-deficit-calculator.html">Calorie Deficit Calculator</a></li>
          </ul>
        </div>
        <div class="sidebar-card mt-4">
          <h3 class="sidebar-title">Clinical Standards</h3>
          <p class="sidebar-text">Based on the UK National Institute for Health and Care Excellence (NICE Clinical Guideline CG189 / 2022 Update), Dr. Margaret Ashwell's shape chart, and epidemiological consensus on central visceral adiposity.</p>
        </div>
      </aside>
    </div>

    <article class="article-body">
      <h2>The Clinical Significance of Central Visceral Adiposity</h2>
      <p>In preventive medicine, clinical cardiology, and metabolic endocrinology, <em>where</em> body fat is anatomically distributed is vastly more critical to morbidity and mortality than the absolute volume of adipose tissue on a scale. Human adipose tissue is divided into two physiologically distinct biological depots:</p>
      <ul>
        <li><strong>Subcutaneous Adipose Tissue (SAT):</strong> Stored beneath the skin throughout the extremities and buttocks. SAT serves as a safe metabolic buffer for excess caloric storage with minimal direct atherogenic liability.</li>
        <li><strong>Visceral Adipose Tissue (VAT):</strong> Stored deep within the peritoneal cavity surrounding intra-abdominal organs, including the liver, pancreas, intestines, and kidneys. Visceral adiposity exhibits high lipolytic turnover, draining directly into the <strong>hepatic portal venous system</strong>. Visceral adipocytes flood the liver with free fatty acids ($FFAs$) and secrete pro-inflammatory cytokines—including Tumor Necrosis Factor-alpha ($TNF\text{-}\alpha$), Interleukin-6 ($IL\text{-}6$), and resistin—while suppressing cardioprotective <strong>adiponectin</strong>.</li>
      </ul>
      <p>This portal flux triggers hepatic steatosis (Non-Alcoholic Fatty Liver Disease, NAFLD), systemic insulin resistance, endothelial dysfunction, elevated small dense LDL particles, hypertriglyceridemia, and hypertension. Waist circumference provides a direct physical surrogate for visceral adipose accumulation.</p>

      <h2>Mathematical Formulation: The Waist-to-Height Ratio (WHtR)</h2>
      <p>The <strong>Waist-to-Height Ratio (WHtR)</strong> is the dimensionless mathematical proportion of waist circumference ($W$) to standing vertical height ($H$), measured in identical units:</p>

      $$WHtR = \frac{\text{Waist Circumference}}{\text{Height}}$$

      <p>In 1996, nutritional scientist Dr. Margaret Ashwell proposed the universal public health aphorism:</p>

      $$\mathbf{\text{“Keep your waist circumference to less than half your height.”}} \implies WHtR < 0.50$$

      <p>While Body Mass Index ($BMI = kg/m^2$) compares weight to height squared, WHtR compares a one-dimensional linear circumference to a one-dimensional linear height. This direct scaling allows WHtR to adjust naturally for body stature without the non-linear dimensional distortions inherent in BMI.</p>

      <div class="table-container my-4">
        <table class="data-table">
          <thead>
            <tr>
              <th>WHtR Boundary Range</th>
              <th>Ashwell Shape Classification</th>
              <th>Clinical Visceral Adiposity Profile</th>
              <th>Cardiometabolic Disease Risk Tier</th>
              <th>Recommended Clinical Action</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>&lt; 0.40</strong></td>
              <td>"Take Care" / Extremely Slim</td>
              <td>Deficient visceral and subcutaneous energy stores.</td>
              <td>Low cardiovascular risk, but elevated risk of nutritional deficiency, osteopenia, and frailty.</td>
              <td>Nutritional evaluation; ensure caloric and micronutrient adequacy.</td>
            </tr>
            <tr>
              <td><strong>0.40 – 0.49</strong></td>
              <td><strong>"No Action" / Healthy Shape</strong></td>
              <td>Optimal balance; minimal deep intra-abdominal visceral fat.</td>
              <td><strong>Lowest Cardiometabolic Risk</strong>; optimal blood pressure, insulin sensitivity, and lipid profile.</td>
              <td>Maintain current balanced nutrition and physical activity habits.</td>
            </tr>
            <tr>
              <td><strong>0.50 – 0.59</strong></td>
              <td>"Consider Action" / Increased Risk</td>
              <td>Moderate visceral adipose accumulation around portal organs.</td>
              <td><strong>Elevated Risk</strong> of prediabetes, endothelial dysfunction, hypertension, and dyslipidemia.</td>
              <td>Lifestyle intervention: caloric moderation, aerobic exercise, and waist reduction.</td>
            </tr>
            <tr>
              <td><strong>&ge; 0.60</strong></td>
              <td>"Take Action" / Very High Risk</td>
              <td>Severe visceral obesity and hepatic lipid infiltration.</td>
              <td><strong>Very High Risk</strong>; strong correlation with Type 2 Diabetes, obstructive sleep apnea, stroke, and CAD.</td>
              <td>Medical evaluation: comprehensive metabolic panel, HbA1c, fasting lipids, blood pressure audit.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Why WHtR Outperforms Body Mass Index (BMI)</h2>
      <p>Extensive systematic reviews and meta-analyses published in the <em>International Journal of Obesity</em> and <em>Obesity Reviews</em> demonstrate that Waist-to-Height Ratio is a superior predictor of cardiometabolic morbidity and all-cause mortality compared to traditional BMI. The primary flaws of BMI resolved by WHtR include:</p>
      <ul>
        <li><strong>Resolution of the Athletic Muscle Paradox:</strong> Muscular athletes, bodybuilders, and powerlifters possess high skeletal muscle mass and bone mineral density. BMI frequently classifies these healthy individuals as "overweight" or "obese" ($BMI > 25\text{ to }30$). However, because their waist remains tight and narrow, their WHtR remains strictly beneath 0.50, correctly identifying their excellent cardiovascular health.</li>
        <li><strong>Detection of "Normal Weight Obesity" (TOFI: Thin Outside, Fat Inside):</strong> Individuals with sedentary lifestyles and poor diets frequently exhibit a completely normal BMI (<25.0) alongside low skeletal muscle mass and excessive visceral fat deposition around the liver and mesentery. BMI gives these individuals a false bill of health, whereas WHtR detects their elevated ratio ($WHtR \ge 0.53$), capturing high cardiovascular risk that would otherwise remain untreated.</li>
        <li><strong>Universal Demographics (The Single Cutoff Rule):</strong> BMI and absolute waist circumference cutoffs differ significantly between men and women and across ethnic groups (e.g., WHO guidelines establish lower BMI cutoffs for South Asian cohorts). Remarkably, meta-analyses demonstrate that the <strong>0.50 WHtR threshold applies uniformly to men, women, and children over age 5 across all major global ethnicities</strong>.</li>
      </ul>

      <h2>The UK NICE 2022 Guidelines Endorsement</h2>
      <p>In 2022, the UK <strong>National Institute for Health and Care Excellence (NICE Guideline CG189)</strong> officially updated its clinical recommendations for assessing obesity and health risk, formally advising healthcare practitioners to adopt the Waist-to-Height Ratio:</p>
      <blockquote>
        "Healthcare professionals should encourage people to measure their waist-to-height ratio to assess central adiposity. A waist-to-height ratio of 0.5 or more indicates increased health risks. Waist-to-height ratio can be used for men, women, and children aged 5 and over across all ethnic groups."
      </blockquote>

      <h2>Step-by-Step Worked Clinical Case Study</h2>
      <p>The following case study illustrates an evidence-based clinical screening comparing BMI and WHtR in a patient presenting for preventive cardiovascular risk stratification:</p>

      <div class="worked-example-card my-4">
        <h3 class="example-title">Preventive Cardiology Case Profile: Central Adiposity Screening</h3>
        <p><strong>Patient Baseline:</strong> A 44-year-old corporate accountant presents for a health audit. Anthropometrics: Height = <strong>5 feet 8 inches (68 inches / 172.7 cm)</strong>, Body Weight = <strong>162 lbs (73.48 kg)</strong>, Measured Waist Circumference = <strong>37.5 inches (95.25 cm)</strong>.</p>
        
        <div class="example-step">
          <div class="step-num">Step 1</div>
          <div class="step-content">
            <strong>Calculate Traditional Body Mass Index (BMI):</strong>
            $$\text{BMI} = 703 \times \frac{162}{(68)^2} = 703 \times \frac{162}{4624} = \mathbf{24.63 \text{ kg/m}^2}$$
            Traditional evaluation: A BMI of 24.63 falls within the 18.5–24.9 range, classifying the patient as <em>"Normal Weight."</em> Under standard BMI protocols, the patient would be told he is in optimal health!
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 2</div>
          <div class="step-content">
            <strong>Calculate Waist-to-Height Ratio (WHtR):</strong>
            $$\text{WHtR} = \frac{\text{Waist Circumference}}{\text{Height}} = \frac{37.5 \text{ inches}}{68.0 \text{ inches}} = \mathbf{0.551}$$
            In metric equivalents: $95.25 \text{ cm} / 172.7 \text{ cm} = \mathbf{0.551}$.
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 3</div>
          <div class="step-content">
            <strong>Apply the Ashwell Shape Chart and NICE Guidelines:</strong>
            A WHtR of 0.551 falls within the <strong>0.50 to 0.59 "Consider Action" tier</strong>.
            $$\text{Maximum Recommended Waist} = 68.0 \text{ inches} \times 0.50 = \mathbf{34.0 \text{ inches}}$$
            $$\text{Excess Waist Circumference} = 37.5 - 34.0 = \mathbf{+3.5 \text{ inches above optimal threshold}}$$
            Despite having a "normal" BMI, the patient carries 3.5 inches of excess visceral adiposity!
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 4</div>
          <div class="step-content">
            <strong>Clinical Diagnostics and Intervention:</strong>
            Because WHtR identified central adiposity, the physician orders a fasting blood lipid panel and HbA1c. Lab results confirm early insulin resistance (fasting glucose 108 mg/dL, Triglyceride-to-HDL ratio 3.8). A targeted lifestyle protocol focused on reducing waist circumference by 3.5 inches reverses the hidden metabolic syndrome before overt cardiovascular events occur.
          </div>
        </div>
      </div>

      <h2>Standardized Anthropometric Measurement Technique</h2>
      <p>To ensure high reproducibility and clinical accuracy when measuring waist circumference:</p>
      <ul>
        <li><strong>Anatomical Landmark:</strong> Stand erect with feet shoulder-width apart. Locate the lower palpable edge of the 12th rib and the top of the iliac crest (pelvic bone). Position the measuring tape horizontally around the abdomen precisely midway between these two points (typically level with or slightly above the navel).</li>
        <li><strong>Tape Tension:</strong> Use a non-stretchable vinyl or fiberglass tape. Ensure the tape is parallel to the floor all the way around the torso, snug against the bare skin without compressing the underlying soft tissues.</li>
        <li><strong>Respiratory Phase:</strong> Take the measurement at the end of a normal, unforced expiration. Avoid sucking in the stomach or holding the breath, which can artificially distort the measurement by up to 2 inches.</li>
      </ul>
    </article>
  </main>

  <footer class="footer">
    <div class="footer-container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="footer-logo">
            <span class="logo-icon">🧮</span>
            <span class="logo-text">CalcHub</span>
          </div>
          <p class="footer-tagline">Clinical, financial, and engineering reference calculators built with precision and peer-reviewed rigor.</p>
        </div>
        <div class="footer-links">
          <h4 class="footer-heading">Health Calculators</h4>
          <ul class="footer-nav">
            <li><a href="waist-to-height-calculator.html">Waist to Height Calculator</a></li>
            <li><a href="bmi-calculator.html">BMI Calculator</a></li>
            <li><a href="body-fat-calculator.html">Body Fat Calculator</a></li>
            <li><a href="ideal-weight-calculator.html">Ideal Body Weight</a></li>
            <li><a href="calorie-deficit-calculator.html">Calorie Deficit Calculator</a></li>
          </ul>
        </div>
        <div class="footer-links">
          <h4 class="footer-heading">Categories</h4>
          <ul class="footer-nav">
            <li><a href="health.html">Health & Fitness</a></li>
            <li><a href="finance.html">Financial Tools</a></li>
            <li><a href="engineering.html">Engineering</a></li>
            <li><a href="index.html">Directory</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. Educational and clinical calculation tools. Consult a physician for cardiovascular risk evaluation.</p>
      </div>
    </div>
  </footer>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const form = document.getElementById('whtr-form');
      const unitSystem = document.getElementById('unit-system');
      const usGroup = document.getElementById('us-inputs-group');
      const metricGroup = document.getElementById('metric-inputs-group');
      const heightFeet = document.getElementById('height-feet');
      const heightInches = document.getElementById('height-inches');
      const waistInches = document.getElementById('waist-inches');
      const heightCm = document.getElementById('height-cm');
      const waistCm = document.getElementById('waist-cm');
      const resultsContainer = document.getElementById('calculator-results');

      unitSystem.addEventListener('change', function() {
        const isMetric = unitSystem.value === 'metric';
        if (isMetric) {
          usGroup.style.display = 'none';
          metricGroup.style.display = 'block';

          const ft = parseFloat(heightFeet.value) || 5;
          const inc = parseFloat(heightInches.value) || 9;
          const totalIn = (ft * 12) + inc;
          heightCm.value = (totalIn * 2.54).toFixed(1);

          const wIn = parseFloat(waistInches.value) || 33;
          waistCm.value = (wIn * 2.54).toFixed(1);
        } else {
          usGroup.style.display = 'block';
          metricGroup.style.display = 'none';

          const cm = parseFloat(heightCm.value) || 175;
          const totalIn = cm / 2.54;
          heightFeet.value = Math.floor(totalIn / 12);
          heightInches.value = Math.round(totalIn % 12);

          const wCm = parseFloat(waistCm.value) || 84;
          waistInches.value = (wCm / 2.54).toFixed(1);
        }
      });

      form.addEventListener('submit', function(e) {
        e.preventDefault();

        const isMetric = unitSystem.value === 'metric';
        let heightVal = 0;
        let waistVal = 0;
        let unitLabel = isMetric ? 'cm' : 'in';

        if (isMetric) {
          heightVal = parseFloat(heightCm.value) || 0;
          waistVal = parseFloat(waistCm.value) || 0;
        } else {
          const ft = parseFloat(heightFeet.value) || 0;
          const inc = parseFloat(heightInches.value) || 0;
          heightVal = (ft * 12) + inc;
          waistVal = parseFloat(waistInches.value) || 0;
        }

        if (heightVal <= 0 || waistVal <= 0) return;

        const whtr = waistVal / heightVal;
        const maxIdealWaist = (heightVal * 0.50).toFixed(1);
        const minIdealWaist = (heightVal * 0.40).toFixed(1);
        const waistDiff = (waistVal - (heightVal * 0.50)).toFixed(1);

        let shapeCategory = '';
        let statusBadge = '';
        let cvdRisk = '';
        let clinicalText = '';

        if (whtr < 0.40) {
          shapeCategory = 'Take Care (Slim / Underweight)';
          statusBadge = '<span class="status-below">Below Optimal (&lt; 0.40)</span>';
          cvdRisk = 'Low CVD Risk (Elevated Frailty Risk)';
          clinicalText = 'Your waist circumference is under 40% of your standing height. While cardiovascular risk is low, verify nutritional adequacy to guard against osteopenia and sarcopenia.';
        } else if (whtr < 0.50) {
          shapeCategory = 'Healthy Shape (No Action Needed)';
          statusBadge = '<span class="status-normal">Healthy (0.40 – 0.49)</span>';
          cvdRisk = 'Lowest Cardiovascular Risk';
          clinicalText = 'Congratulations! Your waist circumference is less than half your height, aligning with the optimal Ashwell shape and NICE 2022 guidelines for minimal visceral adiposity.';
        } else if (whtr < 0.60) {
          shapeCategory = 'Consider Action (Increased Risk)';
          statusBadge = '<span class="status-above">Elevated (0.50 – 0.59)</span>';
          cvdRisk = 'Increased Cardiometabolic Risk';
          clinicalText = 'Your waist circumference exceeds 50% of your height by ' + Math.abs(waistDiff) + ' ' + unitLabel + '. This signifies early visceral fat accumulation around intra-abdominal organs. Modest dietary adjustments and aerobic exercise are recommended to bring your waist below ' + maxIdealWaist + ' ' + unitLabel + '.';
        } else {
          shapeCategory = 'Take Action (Very High Risk)';
          statusBadge = '<span class="status-above">Very High Risk (&ge; 0.60)</span>';
          cvdRisk = 'High Risk of T2D & Heart Disease';
          clinicalText = 'Your waist circumference is ' + Math.abs(waistDiff) + ' ' + unitLabel + ' above the 0.50 threshold, categorizing you in the very high risk tier. Comprehensive clinical evaluation (HbA1c, fasting lipids, and blood pressure audit) is strongly advised.';
        }

        // Display results
        document.getElementById('res-whtr-value').textContent = whtr.toFixed(2);
        document.getElementById('res-whtr-status').innerHTML = statusBadge;
        document.getElementById('res-ashwell-shape').textContent = shapeCategory;
        document.getElementById('res-max-ideal-waist').textContent = maxIdealWaist + ' ' + unitLabel;
        document.getElementById('res-waist-variance').textContent = (waistDiff > 0 ? '+' : '') + waistDiff + ' ' + unitLabel;
        document.getElementById('res-variance-note').textContent = waistDiff > 0 ? 'Above 0.50 health ceiling' : 'Safely below health ceiling';
        document.getElementById('res-cvd-risk').textContent = cvdRisk;
        document.getElementById('res-ideal-waist-range').textContent = minIdealWaist + ' – ' + maxIdealWaist + ' ' + unitLabel;
        document.getElementById('res-whtr-clinical').textContent = clinicalText;

        resultsContainer.style.display = 'block';
        resultsContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      });

      // Initial execution
      form.dispatchEvent(new Event('submit'));
    });
  </script>
</body>
</html>
"""

def main():
    tdee_path = os.path.join(BASE_DIR, "tdee-calculator.html")
    with open(tdee_path, "w", encoding="utf-8") as f:
        f.write(TDEE_CALCULATOR_HTML.strip() + "\n")
    print(f"Generated {os.path.basename(tdee_path)}")

    whtr_path = os.path.join(BASE_DIR, "waist-to-height-calculator.html")
    with open(whtr_path, "w", encoding="utf-8") as f:
        f.write(WAIST_HEIGHT_HTML.strip() + "\n")
    print(f"Generated {os.path.basename(whtr_path)}")

if __name__ == "__main__":
    main()
