"""
Batch 21 - Part 3: Health & Fitness Tools
5. calorie-deficit-calculator.html (Dynamic Caloric Deficit, Hall Adaptive Thermogenesis & Fat Loss)
6. calories-burned-calculator.html (Compendium of Physical Activities METs & Gross vs Net Caloric Burn)
Word count target: >1,000 words in article-body each.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 5. calorie-deficit-calculator.html
# -------------------------------------------------------------
CALORIE_DEFICIT_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Calorie Deficit Calculator | Dynamic Fat Loss & Adaptive Thermogenesis</title>
  <meta name="description" content="Calculate your daily calorie deficit, weekly fat loss rate, and target date using Mifflin-St Jeor TDEE and dynamic metabolic adaptation modeling beyond the 3,500 kcal rule.">
  <link rel="canonical" href="https://calchub.com/calorie-deficit-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Dynamic Calorie Deficit & Fat Loss Calculator",
    "applicationCategory": "HealthApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0.00",
      "priceCurrency": "USD"
    },
    "description": "Calculates daily calorie deficit, target intake, protein requirements, and fat loss timeline accounting for adaptive thermogenesis and metabolic slowdown."
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is the 3,500 calorie rule and why is it flawed for long-term weight loss?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Max Wishnofsky's 1958 rule stated that a 3,500 kcal cumulative deficit produces exactly 1 pound of fat loss. While biochemically true for 1 lb of pure adipose tissue (87% lipid = 395g fat × 9 kcal/g ≈ 3,555 kcal), it assumes human metabolism is static. In reality, as body weight decreases, basal metabolic rate drops and non-exercise activity thermogenesis (NEAT) declines, meaning a static deficit produces non-linear, plateauing weight loss over time."
        }
      },
      {
        "@type": "Question",
        "name": "What is a safe and sustainable calorie deficit percentage?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "For most adults, a moderate deficit of 20% to 25% below Total Daily Energy Expenditure (TDEE) (typically 400 to 600 kcal/day) yields 0.8 to 1.5 lbs of fat loss per week while preserving lean muscle mass and thyroid function. Aggressive deficits (> 30%) trigger severe hormonal downregulation (leptin drop, cortisol surge) and muscle catabolism."
        }
      },
      {
        "@type": "Question",
        "name": "How much protein should I eat during a calorie deficit?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "To preserve lean muscle mass and maximize satiety during an energy deficit, peer-reviewed sports nutrition guidelines (ISSN / JISSN) recommend 1.6 to 2.4 grams of protein per kilogram of body weight (0.73 to 1.1 g/lb), especially when combined with progressive resistance training."
        }
      },
      {
        "@type": "Question",
        "name": "What is adaptive thermogenesis?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Adaptive thermogenesis is the disproportionate reduction in resting and non-resting energy expenditure that occurs during caloric restriction, exceeding what can be predicted by the loss of fat and fat-free mass alone. It represents the human body's evolutionary survival mechanism against starvation, regulated by circulating leptin, active triiodothyronine (T3), and sympathetic nervous system tone."
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

  <main class="main-content">
    <div class="calculator-container">
      <div class="calculator-header">
        <div class="badge-tag">Evidence-Based Nutrition</div>
        <h1 class="calculator-title">Calorie Deficit &amp; Fat Loss Calculator</h1>
        <p class="calculator-description">Calculate your daily target calories, macronutrient split, and realistic fat loss timeline using Mifflin-St Jeor TDEE and dynamic metabolic adaptation modeling.</p>
      </div>

      <div class="calculator-grid">
        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Metabolic Baseline &amp; Goal Inputs</h2>
          </div>
          <div class="calc-card-body">
            <div class="form-row" style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
              <div class="form-group">
                <label for="gender" class="form-label">Biological Sex</label>
                <select id="gender" class="form-select" onchange="calculateDeficit()">
                  <option value="male" selected>Male (+5 kcal/day offset)</option>
                  <option value="female">Female (-161 kcal/day offset)</option>
                </select>
              </div>
              <div class="form-group">
                <label for="age" class="form-label">Age (Years)</label>
                <input type="number" id="age" class="form-input" value="32" min="15" max="100" step="1" oninput="calculateDeficit()">
              </div>
            </div>

            <div class="form-row" style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
              <div class="form-group">
                <label for="current-weight" class="form-label">Current Weight (lbs)</label>
                <input type="number" id="current-weight" class="form-input" value="195" min="70" max="500" step="0.5" oninput="calculateDeficit()">
              </div>
              <div class="form-group">
                <label for="goal-weight" class="form-label">Goal Weight (lbs)</label>
                <input type="number" id="goal-weight" class="form-input" value="175" min="65" max="450" step="0.5" oninput="calculateDeficit()">
              </div>
            </div>

            <div class="form-group">
              <label for="height-inches" class="form-label">Height (Inches)</label>
              <input type="number" id="height-inches" class="form-input" value="70" min="40" max="96" step="0.5" oninput="calculateDeficit()">
              <span class="form-hint">70 inches = 5 ft 10 in</span>
            </div>

            <div class="form-group">
              <label for="activity-level" class="form-label">Physical Activity Multiplier (PAL)</label>
              <select id="activity-level" class="form-select" onchange="calculateDeficit()">
                <option value="1.2">Sedentary (Desk job, little to no exercise) - 1.20</option>
                <option value="1.375" selected>Lightly Active (Light exercise 1-3 days/week) - 1.375</option>
                <option value="1.55">Moderately Active (Moderate exercise 3-5 days/week) - 1.55</option>
                <option value="1.725">Very Active (Hard training 6-7 days/week) - 1.725</option>
                <option value="1.9">Extra Active (Laborious physical job + daily training) - 1.90</option>
              </select>
            </div>

            <div class="form-group">
              <label for="deficit-strategy" class="form-label">Deficit Strategy &amp; Aggressiveness</label>
              <select id="deficit-strategy" class="form-select" onchange="calculateDeficit()">
                <option value="0.15">Conservative (15% Deficit - High adherence, low muscle loss)</option>
                <option value="0.20" selected>Moderate (20% Deficit - Recommended balanced cut)</option>
                <option value="0.25">Aggressive (25% Deficit - Rapid fat loss, higher fatigue)</option>
                <option value="500">Fixed 500 kcal Deficit (~1.0 lb/week theoretical)</option>
              </select>
            </div>

            <button type="button" class="btn btn-primary" onclick="calculateDeficit()">Calculate Deficit &amp; Timeline</button>
          </div>
        </div>

        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Target Intake &amp; Timeline Forecast</h2>
          </div>
          <div class="calc-card-body">
            <div class="result-hero" style="background:#ecfdf5;border-color:#a7f3d0;">
              <span class="hero-label">Daily Target Calorie Intake</span>
              <div class="hero-value" id="res-target-calories" style="color:#047857;font-size:2.4rem;">1,985 kcal</div>
              <span class="form-hint">Baseline Maintenance TDEE: <span id="res-tdee">2,481 kcal/day</span> (-20.0%)</span>
            </div>

            <div class="results-grid" style="margin-top:1.5rem;">
              <div class="result-item">
                <span class="result-label">Daily Deficit</span>
                <span class="result-value" id="res-daily-deficit">496 kcal</span>
              </div>
              <div class="result-item">
                <span class="result-label">Weekly Loss Rate</span>
                <span class="result-value" id="res-weekly-loss">1.0 lbs / wk</span>
              </div>
              <div class="result-item">
                <span class="result-label">Estimated Time to Goal</span>
                <span class="result-value" id="res-weeks-to-goal">20 Weeks</span>
              </div>
              <div class="result-item">
                <span class="result-label">Optimal Daily Protein</span>
                <span class="result-value" id="res-protein-target">160 – 195 g</span>
              </div>
            </div>

            <div class="stat-box" style="margin-top:1.5rem;padding:1rem;background:#f8fafc;border-radius:8px;border:1px solid #e2e8f0;">
              <h4 style="font-weight:700;margin-bottom:0.5rem;font-size:0.95rem;">Dynamic Adaptation &amp; Plateau Warning:</h4>
              <p id="res-adaptation-note" style="font-size:0.875rem;color:#475569;margin:0;">
                At week 10-12, expected metabolic adaptation will lower resting TDEE by approximately 100-150 kcal/day. Planning a 1-week diet break at maintenance will preserve thyroid T3 and restore leptin sensitivity.
              </p>
            </div>
          </div>
        </div>
      </div>

      <article class="article-body">
        <h2>Energetic Foundations: The Laws of Thermodynamics in Human Metabolism</h2>
        <p>
          Weight loss adheres strictly to the First Law of Thermodynamics: energy can neither be created nor destroyed, only transformed from one state to another. In human bioenergetics, the fundamental energy balance equation governs changes in total body mass:
        </p>
        $$\Delta E_{\text{stored}} = E_{\text{in}} - E_{\text{out}}$$
        <p>
          Where $E_{\text{in}}$ represents metabolisable dietary intake (gross caloric intake adjusted for the coefficient of digestive absorption), and $E_{\text{out}}$ represents Total Daily Energy Expenditure ($TDEE$). To lose body fat, an individual must establish a sustained <strong>negative energy balance</strong> ($E_{\text{in}} < E_{\text{out}}$), forcing the endocrine system to mobilize stored endogenous triglycerides from subcutaneous and visceral adipocytes via hormone-sensitive lipase (HSL) lipolysis and mitochondrial $\beta$-oxidation.
        </p>

        <h2>Deconstructing Total Daily Energy Expenditure (TDEE)</h2>
        <p>
          $TDEE$ consists of four distinct, dynamically interacting metabolic components:
        </p>
        <ol>
          <li><strong>Basal Metabolic Rate (BMR, 60% – 70% of TDEE):</strong> The obligatory cellular energy expenditure required to sustain involuntary physiological processes in a post-absorptive, thermoneutral state (cellular ion pumping via $Na^+/K^+$-ATPase, cardiac muscle contraction, hepatic gluconeogenesis, protein turnover, and pulmonary ventilation). Calculated via the validated <strong>Mifflin-St Jeor equation</strong>:
            $$\text{Men: } BMR = 10 \times \text{Weight (kg)} + 6.25 \times \text{Height (cm)} - 5 \times \text{Age (yrs)} + 5$$
            $$\text{Women: } BMR = 10 \times \text{Weight (kg)} + 6.25 \times \text{Height (cm)} - 5 \times \text{Age (yrs)} - 161$$
          </li>
          <li><strong>Thermic Effect of Food (TEF, 8% – 12% of TDEE):</strong> The energetic cost of ingesting, digesting, absorbing, and metabolizing macronutrients. Protein exhibits by far the highest thermic cost ($20\% - 30\%$ of ingested energy consumed in ureagenesis and peptide processing), compared to carbohydrates ($5\% - 10\%$) and dietary fats ($0\% - 3\%$).</li>
          <li><strong>Exercise Activity Thermogenesis (EAT, 5% – 15% of TDEE):</strong> Caloric expenditure resulting from structured physical exercise (resistance training, cardiovascular endurance work, sport participation).</li>
          <li><strong>Non-Exercise Activity Thermogenesis (NEAT, 15% – 30% of TDEE):</strong> Energy expended for all spontaneous physical movement other than sleeping, eating, or sports—including walking to work, occupational movement, fidgeting, posture maintenance, and spontaneous motor pacing. NEAT is the single most variable component of human metabolism and the primary target of adaptive suppression during dieting.</li>
        </ol>

        <h2>The Fallacy of the Static 3,500 kcal Rule vs. Kevin Hall's Dynamic NIH Model</h2>
        <p>
          In 1958, Dr. Max Wishnofsky reviewed clinical calorimetry data and observed that one pound ($453.6\text{ g}$) of human adipose tissue consists of approximately 87% pure triglyceride lipid and 13% water, intracellular protein, and connective stroma:
        </p>
        $$453.6\text{ g} \times 0.87 = 394.6\text{ g lipid} \times 9.1\text{ kcal/g} \approx 3,591\text{ kcal} \implies 3,500\text{ kcal/lb}$$
        <p>
          This observation gave birth to the ubiquitous clinical heuristic: <em>"A daily deficit of 500 kcal will produce exactly 1.0 pound of fat loss per week, and 52 pounds over a year."</em>
        </p>
        <p>
          However, landmark mathematical modeling by Dr. Kevin Hall at the National Institutes of Health (NIH) demonstrated that the static 3,500 kcal rule drastically overestimates long-term weight loss because it treats human metabolism as an open linear furnace. In reality, as body mass decreases, three powerful physiological compensations occur:
        </p>
        <ul>
          <li><strong>Reduced Maintenance Cost:</strong> Moving and sustaining a lighter body requires fewer calories per minute of activity ($E_{\text{out}}$ naturally drifts downward as mass drops).</li>
          <li><strong>Adaptive Thermogenesis:</strong> Circulating adipokine <strong>leptin</strong> plummets out of proportion to adipose loss, signaling the arcuate nucleus of the hypothalamus to suppress active thyroid hormone conversion ($T_4 \to T_3$), lower sympathetic nervous tone, and dramatically downregulate spontaneous NEAT.</li>
          <li><strong>Dynamic Equilibrium:</strong> Rather than continuing to lose weight linearly indefinitely, weight loss follows an exponential decay curve that inevitably plateaus when the lower $TDEE$ converges with the reduced calorie intake. Hall's dynamic rule-of-thumb states that each 10 kcal/day change in energy intake eventually leads to roughly 1 pound of body weight change at steady state, taking over 1 to 2 years to reach complete energetic equilibrium.</li>
        </ul>

        <h2>Deficit Aggressiveness &amp; Macronutrient Partitioning Matrix</h2>
        <p>
          Structuring an evidence-based caloric deficit requires balancing the rate of adipose tissue oxidation against the preservation of skeletal muscle mass and neuroendocrine health:
        </p>

        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>Deficit Category</th>
                <th>Deficit % of TDEE</th>
                <th>Daily Caloric Cut</th>
                <th>Weekly Loss Rate</th>
                <th>Protein Target (g/kg)</th>
                <th>Clinical Indications &amp; Adherence Profile</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Conservative</strong></td>
                <td>10% – 15%</td>
                <td>250 – 350 kcal</td>
                <td>0.5 – 0.8 lbs/wk</td>
                <td>1.6 – 1.8 g/kg</td>
                <td>Athletes, lean individuals (&lt; 12% body fat men, &lt; 20% women), minimal hunger, maximum strength retention.</td>
              </tr>
              <tr>
                <td><strong>Moderate (Optimal)</strong></td>
                <td>20% – 25%</td>
                <td>400 – 600 kcal</td>
                <td>0.9 – 1.5 lbs/wk</td>
                <td>1.8 – 2.2 g/kg</td>
                <td>The gold standard for general population fat loss. Sustainable for 12–16 weeks with high satiety and manageable fatigue.</td>
              </tr>
              <tr>
                <td><strong>Aggressive</strong></td>
                <td>25% – 35%</td>
                <td>650 – 900 kcal</td>
                <td>1.5 – 2.2 lbs/wk</td>
                <td>2.2 – 2.6 g/kg</td>
                <td>Obese individuals (BMI &gt; 30) with substantial metabolic reserve; short-term "mini-cuts" (2-4 weeks) for physique athletes.</td>
              </tr>
              <tr>
                <td><strong>Very Low Calorie (VLCD)</strong></td>
                <td>&gt; 40%</td>
                <td>&gt; 1,000 kcal</td>
                <td>&gt; 2.5 lbs/wk</td>
                <td>&gt; 2.5 g/kg</td>
                <td>Medically supervised bariatric preparation only; high risk of gallstones, muscle wasting, and severe metabolic crash.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2>Worked Case Study: Designing an Evidence-Based Cutting Protocol</h2>
        <div class="worked-example-card">
          <div class="example-header">
            <span class="example-badge">Sports Dietetics Case</span>
            <h3 class="example-title">16-Week Body Recomposition &amp; Fat Loss Protocol</h3>
          </div>
          <div class="example-step">
            <div class="step-num">1</div>
            <div class="step-content">
              <strong>Client Anthropometric Profile:</strong> A 30-year-old male corporate executive and recreational weightlifter. Current Weight = 200 lbs (90.72 kg), Height = 71 inches (180.34 cm). Estimated body fat = 22% (44 lbs fat mass, 156 lbs lean body mass). Target weight = 180 lbs (approx. 13% body fat). Physical activity: 4 days/week resistance training + desk job ($PAL = 1.45$).
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">2</div>
            <div class="step-content">
              <strong>Calculate Baseline BMR and Maintenance TDEE:</strong>
              $$BMR = 10 \times 90.72 + 6.25 \times 180.34 - 5 \times 30 + 5$$
              $$BMR = 907.2 + 1127.1 - 150 + 5 = 1,889.3\text{ kcal/day}$$
              $$TDEE = BMR \times PAL = 1889.3 \times 1.45 = \mathbf{2,739.5\text{ kcal/day}}$$
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">3</div>
            <div class="step-content">
              <strong>Establish Moderate 20% Calorie Deficit:</strong>
              $$\text{Daily Deficit} = 2,739.5 \times 0.20 = 547.9\text{ kcal/day}$$
              $$\text{Target Daily Intake} = 2,739.5 - 548 = \mathbf{2,192\text{ kcal/day}}$$
              $$\text{Expected Weekly Adipose Loss} = \frac{548 \times 7}{3500} \approx \mathbf{1.10\text{ lbs/week}}$$
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">4</div>
            <div class="step-content">
              <strong>Structure Evidence-Based Macronutrient Split:</strong>
              <ul>
                <li><strong>Protein (2.0 g/kg):</strong> $90.72 \times 2.0 = 181.4\text{ g/day} \times 4\text{ kcal/g} = 726\text{ kcal}$ (33% of intake).</li>
                <li><strong>Dietary Fat (25% of energy for hormone optimization):</strong> $2,192 \times 0.25 = 548\text{ kcal} / 9\text{ kcal/g} = \mathbf{61\text{ g/day}}$.</li>
                <li><strong>Carbohydrates (Remaining calories for training performance):</strong> $2,192 - 726 - 548 = 918\text{ kcal} / 4\text{ kcal/g} = \mathbf{230\text{ g/day}}$.</li>
              </ul>
              <strong>Timeline:</strong> To lose 20 lbs at 1.1 lbs/week requires approximately 18 to 20 weeks, including two scheduled 1-week diet breaks at maintenance (2,500 kcal) at weeks 7 and 14 to attenuate adaptive thermogenesis.
            </div>
          </div>
        </div>

        <h2>The Neuroendocrine Starvation Response: Leptin, Ghrelin, and Diet Breaks</h2>
        <p>
          Prolonged energy restriction activates an evolutionary neuroendocrine cascade aimed at preventing starvation. As subcutaneous adipose reserves shrink, circulating <strong>leptin</strong> (synthesized predominantly by adipocytes) drops precipitously. Low leptin disinhibits the orexigenic neuropeptide Y (NPY) and agouti-related peptide (AgRP) neurons in the arcuate nucleus while suppressing anorexigenic pro-opiomelanocortin (POMC) neurons, triggering unrelenting biological hunger and food preoccupation.
        </p>
        <p>
          Simultaneously, stomach-derived <strong>ghrelin</strong> surges, peptide YY (PYY) and cholecystokinin (CCK) decline, and active thyroid hormone triiodothyronine ($T_3$) is converted to inactive reverse $T_3$ ($rT_3$). To mitigate this neuroendocrine crash, modern sports nutrition protocols implement structured <strong>Diet Breaks</strong>.
        </p>
        <p>
          In the landmark <em>MATADOR trial</em> (Minimizing Adaptive Thermogenesis And Deactivating Obesity Rebound), researchers compared continuous 16-week calorie restriction against intermittent restriction (2 weeks at a 33% deficit alternating with 2 weeks at maintenance energy balance). The intermittent diet break cohort achieved significantly greater fat loss ($12.3\text{ kg}$ vs $8.4\text{ kg}$), preserved resting metabolic rate, and exhibited superior weight-loss maintenance at 6 months post-diet. For long-term fat loss phases exceeding 12 weeks, scheduling a 7- to 14-day refeed at calculated maintenance calories every 6 to 8 weeks restores glycogen stores, revitalizes training intensity, and normalizes neuroendocrine homeostasis.
        </p>
      </article>
    </div>
  </main>

  <footer class="footer">
    <div class="footer-container">
      <div class="footer-brand">
        <span class="logo-icon">🧮</span>
        <span class="logo-text">CalcHub</span>
        <p class="footer-tagline">Clinical & Engineering Precision Tools for Health and Science.</p>
      </div>
      <div class="footer-links">
        <a href="index.html">All Calculators</a>
        <a href="health.html">Health Calculators</a>
        <a href="finance.html">Financial Tools</a>
        <a href="engineering.html">Engineering Tools</a>
      </div>
    </div>
  </footer>

  <script>
    function calculateDeficit() {
      const gender = document.getElementById('gender').value;
      const age = parseFloat(document.getElementById('age').value) || 0;
      const weightLbs = parseFloat(document.getElementById('current-weight').value) || 0;
      const goalLbs = parseFloat(document.getElementById('goal-weight').value) || 0;
      const heightInches = parseFloat(document.getElementById('height-inches').value) || 0;
      const pal = parseFloat(document.getElementById('activity-level').value) || 1.375;
      const strat = document.getElementById('deficit-strategy').value;

      if (age <= 0 || weightLbs <= 0 || heightInches <= 0) return;

      const weightKg = weightLbs * 0.45359237;
      const heightCm = heightInches * 2.54;

      // Mifflin-St Jeor BMR
      let bmr = (10 * weightKg) + (6.25 * heightCm) - (5 * age);
      if (gender === 'male') {
        bmr += 5;
      } else {
        bmr -= 161;
      }

      const tdee = bmr * pal;

      let deficit = 0;
      if (strat === '500') {
        deficit = 500;
      } else {
        deficit = tdee * parseFloat(strat);
      }

      const targetCalories = Math.max(Math.round(tdee - deficit), (gender === 'male' ? 1500 : 1200));
      const actualDeficit = Math.round(tdee - targetCalories);
      const weeklyLoss = (actualDeficit * 7) / 3500;

      const totalLbsToLose = Math.max(weightLbs - goalLbs, 0);
      let weeksToGoal = 0;
      if (weeklyLoss > 0 && totalLbsToLose > 0) {
        weeksToGoal = Math.ceil(totalLbsToLose / weeklyLoss);
      }

      document.getElementById('res-target-calories').innerText = targetCalories.toLocaleString() + ' kcal';
      document.getElementById('res-tdee').innerText = Math.round(tdee).toLocaleString() + ' kcal/day';
      document.getElementById('res-daily-deficit').innerText = actualDeficit.toLocaleString() + ' kcal';
      document.getElementById('res-weekly-loss').innerText = weeklyLoss.toFixed(1) + ' lbs / wk';
      document.getElementById('res-weeks-to-goal').innerText = (weeksToGoal > 0 ? weeksToGoal + ' Weeks' : 'Goal Met');

      // Protein target (1.6 - 2.2 g/kg)
      const protLow = Math.round(weightKg * 1.6);
      const protHigh = Math.round(weightKg * 2.2);
      document.getElementById('res-protein-target').innerText = `${protLow} – ${protHigh} g`;

      // Adaptation note
      const noteEl = document.getElementById('res-adaptation-note');
      if (weeklyLoss > 1.5) {
        noteEl.innerHTML = `<strong style="color:#b91c1c;">High Deficit Warning:</strong> Weekly loss exceeds 1.5 lbs/week. Expect elevated hunger signals (ghrelin surge), reduction in spontaneous NEAT, and potential loss of lean muscle mass. Prioritize resistance training and maintain protein intake above ${protHigh} g.`;
      } else {
        noteEl.innerHTML = `Sustainable fat loss trajectory. At week 8-12, expected metabolic adaptation will lower resting TDEE by approximately 75-125 kcal/day. Incorporating a 1-week diet break at maintenance will preserve thyroid T3 and restore leptin sensitivity.`;
      }
    }

    document.addEventListener('DOMContentLoaded', calculateDeficit);
  </script>
</body>
</html>
"""

# -------------------------------------------------------------
# 6. calories-burned-calculator.html
# -------------------------------------------------------------
CALORIES_BURNED_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Calories Burned Calculator | Exercise MET Energy Expenditure</title>
  <meta name="description" content="Calculate gross and net calories burned for hundreds of exercises and daily activities using the updated 2024 Ainsworth Compendium of Physical Activities MET database.">
  <link rel="canonical" href="https://calchub.com/calories-burned-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "MET Exercise Calories Burned Calculator",
    "applicationCategory": "HealthApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0.00",
      "priceCurrency": "USD"
    },
    "description": "Calculates gross and net calories burned during athletic and occupational activities based on the scientific Ainsworth Compendium of Physical Activities MET values."
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is a MET (Metabolic Equivalent of Task)?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A MET is a standardized physiological metric representing the ratio of the work metabolic rate to a standard resting metabolic rate. By universal convention, 1 MET is defined as an oxygen uptake of 3.5 milliliters of O2 per kilogram of body weight per minute (3.5 mL O2/kg/min), which is roughly equivalent to 1.0 kilocalorie per kilogram of body mass per hour (1.0 kcal/kg/hr) at quiet sitting rest."
        }
      },
      {
        "@type": "Question",
        "name": "What is the mathematical formula to calculate calories burned from MET values?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The scientific equation is: Calories Burned = MET × 3.5 × Weight (kg) / 200 × Duration (minutes). Alternatively, using the hourly conversion: Calories = MET × Weight (kg) × Duration (hours)."
        }
      },
      {
        "@type": "Question",
        "name": "What is the difference between Gross Calories Burned and Net Calories Burned?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Gross calories burned represents the total energy expended during the workout, which includes your normal resting metabolic rate. Net calories burned represents only the extra energy burned above your baseline resting rate (Net = Gross Calories - Resting Calories during that duration). When logging exercise for weight loss diets, using Net Calories prevents double-counting calories already accounted for in your daily BMR."
        }
      },
      {
        "@type": "Question",
        "name": "What is EPOC (Excess Post-Exercise Oxygen Consumption)?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "EPOC, often called the 'afterburn effect,' is the measurably elevated rate of oxygen consumption following strenuous exercise. It accounts for cellular replenishment of phosphocreatine (PCr) stores, lactate clearance, glycogen resynthesis, and elevated body temperature. EPOC contributes an additional 6% to 15% of the net energy cost of high-intensity interval training (HIIT) or heavy resistance exercise."
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

  <main class="main-content">
    <div class="calculator-container">
      <div class="calculator-header">
        <div class="badge-tag">Exercise Physiology</div>
        <h1 class="calculator-title">Calories Burned by Activity Calculator</h1>
        <p class="calculator-description">Calculate gross and net energy expenditure across hundreds of exercises and sports based on the official 2024 Ainsworth Compendium of Physical Activities.</p>
      </div>

      <div class="calculator-grid">
        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Activity &amp; Body Weight Parameters</h2>
          </div>
          <div class="calc-card-body">
            <div class="form-group">
              <label for="activity-select" class="form-label">Physical Activity / Sport Discipline</label>
              <select id="activity-select" class="form-select" onchange="updateMETAndCalculate()">
                <optgroup label="Running &amp; Jogging">
                  <option value="9.8" selected>Running - 6 mph (10 min/mile pace) [9.8 METs]</option>
                  <option value="8.3">Running - 5 mph (12 min/mile pace) [8.3 METs]</option>
                  <option value="11.0">Running - 7 mph (8.5 min/mile pace) [11.0 METs]</option>
                  <option value="11.8">Running - 8 mph (7.5 min/mile pace) [11.8 METs]</option>
                  <option value="14.5">Running - 10 mph (6.0 min/mile pace) [14.5 METs]</option>
                </optgroup>
                <optgroup label="Cycling &amp; Biking">
                  <option value="6.8">Cycling - Moderate effort (12 - 13.9 mph) [6.8 METs]</option>
                  <option value="8.5">Cycling - Vigorous effort (14 - 15.9 mph) [8.5 METs]</option>
                  <option value="12.0">Cycling - Very fast / Racing (&gt; 16 mph) [12.0 METs]</option>
                  <option value="5.5">Stationary Cycling - Moderate effort (100W) [5.5 METs]</option>
                  <option value="8.8">Stationary Cycling - High intensity (150-200W) [8.8 METs]</option>
                </optgroup>
                <optgroup label="Gym, Strength &amp; Conditioning">
                  <option value="5.0">Weight Lifting - Vigorous free-weight training [5.0 METs]</option>
                  <option value="3.5">Weight Lifting - Light/moderate circuit machines [3.5 METs]</option>
                  <option value="8.0">High-Intensity Interval Training (HIIT) [8.0 METs]</option>
                  <option value="8.0">Calisthenics - Vigorous push-ups, pull-ups, burpees [8.0 METs]</option>
                  <option value="10.0">Jumping Rope - Moderate/fast pace (100-120 rpm) [10.0 METs]</option>
                  <option value="7.0">Rowing Machine - Moderate effort (100W) [7.0 METs]</option>
                </optgroup>
                <optgroup label="Walking &amp; Hiking">
                  <option value="3.5">Walking - Brisk pace (3.5 mph / 5.6 km/h) [3.5 METs]</option>
                  <option value="2.8">Walking - Casual strolling (2.5 mph) [2.8 METs]</option>
                  <option value="4.3">Walking - Very brisk (4.0 mph) [4.3 METs]</option>
                  <option value="6.0">Hiking - Cross-country with daypack [6.0 METs]</option>
                </optgroup>
                <optgroup label="Swimming &amp; Water Sports">
                  <option value="7.0">Swimming - Freestyle / front crawl (moderate) [7.0 METs]</option>
                  <option value="9.8">Swimming - Freestyle / front crawl (vigorous) [9.8 METs]</option>
                  <option value="10.3">Swimming - Breaststroke (vigorous effort) [10.3 METs]</option>
                  <option value="13.8">Swimming - Butterfly stroke [13.8 METs]</option>
                </optgroup>
              </select>
            </div>

            <div class="form-row" style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
              <div class="form-group">
                <label for="user-weight" class="form-label">Body Weight</label>
                <input type="number" id="user-weight" class="form-input" value="175" min="60" max="450" step="1" oninput="calculateBurn()">
              </div>
              <div class="form-group">
                <label for="weight-unit" class="form-label">Unit</label>
                <select id="weight-unit" class="form-select" onchange="calculateBurn()">
                  <option value="lbs" selected>Pounds (lbs)</option>
                  <option value="kg">Kilograms (kg)</option>
                </select>
              </div>
            </div>

            <div class="form-row" style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
              <div class="form-group">
                <label for="duration-mins" class="form-label">Duration (Minutes)</label>
                <input type="number" id="duration-mins" class="form-input" value="45" min="1" max="600" step="5" oninput="calculateBurn()">
              </div>
              <div class="form-group">
                <label for="custom-met" class="form-label">Activity MET Factor</label>
                <input type="number" id="custom-met" class="form-input" value="9.8" min="0.9" max="25.0" step="0.1" oninput="calculateBurn()">
              </div>
            </div>

            <button type="button" class="btn btn-primary" onclick="calculateBurn()">Calculate Energy Expenditure</button>
          </div>
        </div>

        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Energy Expenditure Results</h2>
          </div>
          <div class="calc-card-body">
            <div class="result-hero" style="background:#fff7ed;border-color:#fed7aa;">
              <span class="hero-label">Gross Calories Burned</span>
              <div class="hero-value" id="res-gross-cal" style="color:#c2410c;font-size:2.4rem;">585 kcal</div>
              <span class="form-hint">Total energy expended including resting metabolic baseline</span>
            </div>

            <div class="results-grid" style="margin-top:1.5rem;">
              <div class="result-item">
                <span class="result-label">Net Exercise Calories</span>
                <span class="result-value" id="res-net-cal">525 kcal</span>
              </div>
              <div class="result-item">
                <span class="result-label">Resting Baseline Burn</span>
                <span class="result-value" id="res-resting-cal">60 kcal</span>
              </div>
              <div class="result-item">
                <span class="result-label">Caloric Burn Rate</span>
                <span class="result-value" id="res-burn-rate">13.0 kcal / min</span>
              </div>
              <div class="result-item">
                <span class="result-label">Fat Mass Equivalent</span>
                <span class="result-value" id="res-fat-equiv">0.17 lbs fat</span>
              </div>
            </div>

            <div class="stat-box" style="margin-top:1.5rem;padding:1rem;background:#f8fafc;border-radius:8px;border:1px solid #e2e8f0;">
              <h4 style="font-weight:700;margin-bottom:0.5rem;font-size:0.95rem;">Exercise Metabolism &amp; EPOC Insights:</h4>
              <p id="res-epoc-note" style="font-size:0.875rem;color:#475569;margin:0;">
                High-intensity running (9.8 METs) generates an estimated 6% to 10% additional EPOC afterburn (~35–58 kcal) over the 12-24 hours post-workout during glycogen and phosphagen resynthesis.
              </p>
            </div>
          </div>
        </div>
      </div>

      <article class="article-body">
        <h2>The Physiology of Exercise Energy Expenditure</h2>
        <p>
          During physical exertion, skeletal muscle myocytes undergo rapid cycles of actin-myosin cross-bridge formation powered by the hydrolysis of adenosine triphosphate ($ATP$). Because intracellular muscular ATP concentrations are strictly limited (sustaining only 1 to 2 seconds of maximal contraction), the body continuously resynthesizes ATP through three integrated energetic pathways:
        </p>
        <ol>
          <li><strong>The Phosphagen (ATP-PCr) System:</strong> Rapid anaerobic rephosphorylation mediated by creatine kinase ($CP + ADP \leftrightarrow ATP + C$), dominating the first 10 seconds of maximal burst output.</li>
          <li><strong>Anaerobic Glycolysis:</strong> Fast enzymatic breakdown of muscle glycogen into pyruvate and lactate in the sarcoplasm, powering high-intensity bouts lasting 30 to 120 seconds.</li>
          <li><strong>Aerobic Oxidative Phosphorylation:</strong> Mitochondrial oxidation of pyruvate (from carbohydrates) and free fatty acids through the Krebs cycle and electron transport chain ($ETC$), supplying virtually limitless energy for prolonged submaximal aerobic exercise.</li>
        </ol>

        <h2>The MET Concept: Standardization of Human Work</h2>
        <p>
          Quantifying the energy cost of diverse physical tasks across varying body sizes requires a universal physiological currency. In 1993, Dr. Barbara Ainsworth and colleagues published the landmark <em>Compendium of Physical Activities</em> (extensively revised in 2000, 2011, and 2024), establishing the <strong>Metabolic Equivalent of Task (MET)</strong> as the international standard.
        </p>
        <div class="formula-box">
          <p><strong>Standard Definition of 1 MET:</strong></p>
          $$1\text{ MET} \equiv 3.5\text{ mL } O_2\text{ / kg / min} \approx 1.0\text{ kcal / kg / hour}$$
          <p>
            One MET represents the baseline rate of oxygen consumption of an average adult sitting quietly at rest. An activity assigned a value of 8.0 METs demands eight times the oxygen uptake and energy consumption of quiet rest.
          </p>
        </div>

        <h2>Mathematical Derivation of Caloric Burn from Oxygen Uptake</h2>
        <p>
          The conversion from oxygen consumption to kilocalories relies on indirect respiratory calorimetry. When a human metabolizes a standard mixed diet of carbohydrates and fats, each liter of oxygen consumed ($1\text{ L } O_2$) liberates approximately <strong>4.86 to 5.05 kilocalories</strong> of heat energy (conventionally approximated as $5.0\text{ kcal/L } O_2$):
        </p>
        $$\text{Rate (kcal/min)} = \text{MET} \times 3.5\frac{\text{mL } O_2}{\text{kg}\cdot\text{min}} \times \frac{1\text{ L}}{1000\text{ mL}} \times 5.0\frac{\text{kcal}}{\text{L } O_2} \times \text{Weight (kg)}$$
        $$\text{Rate (kcal/min)} = \text{MET} \times \frac{3.5 \times 5.0}{1000} \times \text{Weight (kg)} = \frac{\text{MET} \times 3.5 \times \text{Weight (kg)}}{200}$$
        <p>
          Integrating over total exercise duration ($t$ in minutes) yields the standard scientific formula:
        </p>
        <div class="formula-box">
          <p><strong>Universal Exercise Calorie Equation:</strong></p>
          $$\text{Gross Calories Burned} = \text{MET} \times \frac{3.5 \times \text{Weight (kg)}}{200} \times \text{Duration (min)}$$
          $$\text{Net Calories Burned} = (\text{MET} - 1.0) \times \frac{3.5 \times \text{Weight (kg)}}{200} \times \text{Duration (min)}$$
        </div>

        <h2>Gross vs. Net Energy Expenditure: Preventing Dietary Double-Counting</h2>
        <p>
          A critical pitfall in sports nutrition and fat loss planning is confusing <em>Gross</em> energy expenditure with <em>Net</em> energy expenditure:
        </p>
        <ul>
          <li><strong>Gross Expenditure:</strong> Measures the entire quantity of fuel burned during the workout window, including the baseline calories your body would have expended sitting on the couch doing nothing.</li>
          <li><strong>Net Expenditure:</strong> Subtracts the baseline resting metabolic rate ($1.0\text{ MET}$), isolating the exact surplus calories expended solely due to the physical movement.</li>
        </ul>
        <p>
          For example, a 180-pound male running for 60 minutes at 6 mph (9.8 METs) burns approximately <strong>800 Gross kcal</strong>. However, his baseline resting expenditure during that same hour would have been approximately <strong>82 kcal</strong>. His true net exercise energy expenditure is therefore <strong>718 Net kcal</strong>. If his daily food log adds back the full 800 gross calories while already using a baseline TDEE that accounts for 24 hours of resting metabolism, he will inadvertently overconsume food and stall fat loss.
        </p>

        <h2>Comprehensive Compendium MET Reference Table</h2>
        <p>
          The table below demonstrates validated MET ratings from the 2024 Ainsworth Compendium and expected hourly caloric expenditures for a standard 165 lb (75 kg) individual:
        </p>

        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>Physical Activity &amp; Discipline</th>
                <th>Compendium MET</th>
                <th>Intensity Classification</th>
                <th>Gross Burn (75 kg, 60 min)</th>
                <th>Net Burn (75 kg, 60 min)</th>
                <th>Primary Fuel Substrate</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Sleeping / Lying Quietly</strong></td>
                <td>0.9</td>
                <td>Resting Baseline</td>
                <td>68 kcal</td>
                <td>-8 kcal</td>
                <td>90% Fatty Acids</td>
              </tr>
              <tr>
                <td><strong>Desk Work / Computer Typing</strong></td>
                <td>1.3</td>
                <td>Sedentary</td>
                <td>98 kcal</td>
                <td>23 kcal</td>
                <td>80% Fatty Acids</td>
              </tr>
              <tr>
                <td><strong>Casual Walking (2.5 mph)</strong></td>
                <td>2.8</td>
                <td>Light Intensity</td>
                <td>210 kcal</td>
                <td>135 kcal</td>
                <td>70% Fatty Acids, 30% Glucose</td>
              </tr>
              <tr>
                <td><strong>Brisk Fitness Walk (3.5 mph)</strong></td>
                <td>3.5</td>
                <td>Moderate Intensity</td>
                <td>263 kcal</td>
                <td>188 kcal</td>
                <td>50% Fatty Acids, 50% Glucose</td>
              </tr>
              <tr>
                <td><strong>Resistance Weight Training (Vigorous)</strong></td>
                <td>5.0</td>
                <td>Moderate / Hard</td>
                <td>375 kcal</td>
                <td>300 kcal</td>
                <td>70% Glycogen, 30% Phosphagen</td>
              </tr>
              <tr>
                <td><strong>Cycling (Moderate, 12–14 mph)</strong></td>
                <td>6.8</td>
                <td>Vigorous Intensity</td>
                <td>510 kcal</td>
                <td>435 kcal</td>
                <td>60% Glucose, 40% Fatty Acids</td>
              </tr>
              <tr>
                <td><strong>Swimming Freestyle (Moderate)</strong></td>
                <td>7.0</td>
                <td>Vigorous Intensity</td>
                <td>525 kcal</td>
                <td>450 kcal</td>
                <td>65% Glucose, 35% Fatty Acids</td>
              </tr>
              <tr>
                <td><strong>HIIT / Calisthenics Circuit</strong></td>
                <td>8.0</td>
                <td>Very Vigorous</td>
                <td>600 kcal</td>
                <td>525 kcal</td>
                <td>80% Glycogen, 20% Lactate</td>
              </tr>
              <tr>
                <td><strong>Running (6 mph / 10 min pace)</strong></td>
                <td>9.8</td>
                <td>High Intensity</td>
                <td>735 kcal</td>
                <td>660 kcal</td>
                <td>75% Glucose, 25% Fatty Acids</td>
              </tr>
              <tr>
                <td><strong>Jumping Rope (Moderate, 100 rpm)</strong></td>
                <td>10.0</td>
                <td>High Intensity</td>
                <td>750 kcal</td>
                <td>675 kcal</td>
                <td>85% Glycogen, 15% Phosphagen</td>
              </tr>
              <tr>
                <td><strong>Running (8 mph / 7.5 min pace)</strong></td>
                <td>11.8</td>
                <td>Very High Intensity</td>
                <td>885 kcal</td>
                <td>810 kcal</td>
                <td>90% Glucose, 10% Fatty Acids</td>
              </tr>
              <tr>
                <td><strong>Competitive Rowing (Max Effort)</strong></td>
                <td>12.0</td>
                <td>Near Maximal</td>
                <td>900 kcal</td>
                <td>825 kcal</td>
                <td>Anaerobic Glycolysis Dominated</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2>Worked Exercise Physiology Case Study</h2>
        <div class="worked-example-card">
          <div class="example-header">
            <span class="example-badge">Training Science Case</span>
            <h3 class="example-title">Endurance Cycling vs. Resistance Training Fuel Expenditure</h3>
          </div>
          <div class="example-step">
            <div class="step-num">1</div>
            <div class="step-content">
              <strong>Athlete Profile:</strong> A 180-pound (81.65 kg) male triathlete performs two distinct training sessions: a 75-minute outdoor road cycling session at 15.0 mph ($8.5\text{ METs}$) on Tuesday, and a 60-minute vigorous free-weight hypertrophy workout ($5.0\text{ METs}$) on Wednesday. The sports nutritionist must calculate his gross and net expenditure for both sessions.
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">2</div>
            <div class="step-content">
              <strong>Calculate Tuesday Cycling Expenditure (75 min, 8.5 METs):</strong>
              $$\text{Gross Burn} = 8.5 \times \frac{3.5 \times 81.65}{200} \times 75 = 8.5 \times 1.4289 \times 75 = \mathbf{910.9\text{ Gross kcal}}$$
              $$\text{Resting Cost} = 1.0 \times 1.4289 \times 75 = 107.2\text{ kcal}$$
              $$\text{Net Burn} = 910.9 - 107.2 = \mathbf{803.7\text{ Net kcal}}$$
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">3</div>
            <div class="step-content">
              <strong>Calculate Wednesday Resistance Training (60 min, 5.0 METs):</strong>
              $$\text{Gross Burn} = 5.0 \times \frac{3.5 \times 81.65}{200} \times 60 = 5.0 \times 1.4289 \times 60 = \mathbf{428.7\text{ Gross kcal}}$$
              $$\text{Resting Cost} = 1.0 \times 1.4289 \times 60 = 85.7\text{ kcal}$$
              $$\text{Net Burn} = 428.7 - 85.7 = \mathbf{343.0\text{ Net kcal}}$$
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">4</div>
            <div class="step-content">
              <strong>EPOC Afterburn Considerations:</strong>
              While cycling burned significantly more raw calories during the session ($804\text{ net}$ vs $343\text{ net}$), heavy resistance training causes widespread micro-trauma to myofibrillar proteins, elevating muscle protein synthesis (MPS) and EPOC by an estimated 10% to 14% (~45 kcal) over the subsequent 24 to 48 hours during muscular repair and remodeling.
            </div>
          </div>
        </div>

        <h2>The Constrained Total Energy Expenditure Model: Pontzer's Evolutionary Paradigm</h2>
        <p>
          For over a century, exercise science assumed an <em>Additive Model</em> of physical activity, wherein each calorie expended during intentional workouts is simply added on top of basal metabolic rate without systemic feedback:
        </p>
        $$\text{Additive Model: } TDEE = BMR + TEF + \text{Exercise Activity}$$
        <p>
          However, revolutionary evolutionary anthropology research led by Dr. Herman Pontzer utilizing <strong>Doubly Labeled Water ($^2H_2^{18}O$)</strong>—the undisputed gold standard of human metabolic measurement—revealed that human energy expenditure is <strong>constrained</strong> within an evolved homeostatic ceiling. In cross-cultural comparisons between Western sedentary populations and the Hadza hunter-gatherers of Tanzania (who walk 5 to 10 miles daily), researchers found remarkably similar total daily energy expenditures when adjusted for lean body mass.
        </p>
        <p>
          Under the <strong>Constrained Energy Model</strong>, when physical activity levels rise dramatically over sustained periods, the body actively suppresses baseline physiological expenditures—reducing chronic systemic inflammation, lowering reproductive hormone output, and curtailing non-conscious fidgeting and spontaneous NEAT. While an intense 60-minute workout burns immediate fuel via the MET equation, the long-term net increase in daily caloric burn settles at approximately 72% of the exercise energy expended in normal-weight individuals, and as low as 50% in individuals with obesity. Consequently, exercise must be viewed primarily as a profound stimulus for cardiovascular fitness, glycemic sensitivity, and lean tissue preservation, while nutritional caloric intake remains the primary lever for sustainable adipose reduction.
        </p>
      </article>
    </div>
  </main>

  <footer class="footer">
    <div class="footer-container">
      <div class="footer-brand">
        <span class="logo-icon">🧮</span>
        <span class="logo-text">CalcHub</span>
        <p class="footer-tagline">Clinical & Engineering Precision Tools for Health and Science.</p>
      </div>
      <div class="footer-links">
        <a href="index.html">All Calculators</a>
        <a href="health.html">Health Calculators</a>
        <a href="finance.html">Financial Tools</a>
        <a href="engineering.html">Engineering Tools</a>
      </div>
    </div>
  </footer>

  <script>
    function updateMETAndCalculate() {
      const selectedMET = document.getElementById('activity-select').value;
      document.getElementById('custom-met').value = selectedMET;
      calculateBurn();
    }

    function calculateBurn() {
      const weightVal = parseFloat(document.getElementById('user-weight').value) || 0;
      const unit = document.getElementById('weight-unit').value;
      const duration = parseFloat(document.getElementById('duration-mins').value) || 0;
      const met = parseFloat(document.getElementById('custom-met').value) || 0;

      if (weightVal <= 0 || duration <= 0 || met <= 0) return;

      const weightKg = (unit === 'lbs') ? (weightVal * 0.45359237) : weightVal;

      // Gross Burn: MET * (3.5 * weightKg / 200) * duration
      const ratePerMin = met * (3.5 * weightKg / 200);
      const grossCalories = Math.round(ratePerMin * duration);

      // Resting Burn: 1.0 * (3.5 * weightKg / 200) * duration
      const restingRate = 1.0 * (3.5 * weightKg / 200);
      const restingCalories = Math.round(restingRate * duration);

      const netCalories = Math.max(grossCalories - restingCalories, 0);
      const burnRate = (grossCalories / duration).toFixed(1);
      const fatEquiv = (netCalories / 3500).toFixed(2);

      document.getElementById('res-gross-cal').innerText = grossCalories.toLocaleString() + ' kcal';
      document.getElementById('res-net-cal').innerText = netCalories.toLocaleString() + ' kcal';
      document.getElementById('res-resting-cal').innerText = restingCalories.toLocaleString() + ' kcal';
      document.getElementById('res-burn-rate').innerText = burnRate + ' kcal / min';
      document.getElementById('res-fat-equiv').innerText = fatEquiv + ' lbs fat';

      const epocEl = document.getElementById('res-epoc-note');
      if (met >= 9.0) {
        const epocLow = Math.round(netCalories * 0.08);
        const epocHigh = Math.round(netCalories * 0.15);
        epocEl.innerHTML = `High-intensity anaerobic activity (${met} METs) induces substantial EPOC afterburn (~${epocLow}–${epocHigh} kcal extra) over 12-24 hours post-workout due to PCr resynthesis, lactate clearance, and elevated core temperature.`;
      } else if (met >= 5.0) {
        const epocLow = Math.round(netCalories * 0.05);
        const epocHigh = Math.round(netCalories * 0.08);
        epocEl.innerHTML = `Moderate-to-vigorous exercise (${met} METs) produces a modest EPOC afterburn (~${epocLow}–${epocHigh} kcal extra) during cellular recovery and glycogen resynthesis.`;
      } else {
        epocEl.innerHTML = `Light aerobic/lifestyle activity (${met} METs) utilizes almost exclusively oxidative lipid pathways with negligible EPOC afterburn once the activity ceases.`;
      }
    }

    document.addEventListener('DOMContentLoaded', calculateBurn);
  </script>
</body>
</html>
"""

def generate_part3():
    with open(os.path.join(BASE_DIR, "calorie-deficit-calculator.html"), "w", encoding="utf-8") as f:
        f.write(CALORIE_DEFICIT_HTML)
    print("Generated calorie-deficit-calculator.html")

    with open(os.path.join(BASE_DIR, "calories-burned-calculator.html"), "w", encoding="utf-8") as f:
        f.write(CALORIES_BURNED_HTML)
    print("Generated calories-burned-calculator.html")

if __name__ == "__main__":
    generate_part3()
