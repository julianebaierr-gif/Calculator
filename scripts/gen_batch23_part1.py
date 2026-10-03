"""
Batch 23 - Part 1: Health & Fitness Tools
1. protein-intake-calculator.html (RDA, ISSN Hypertrophy 1.6-2.2 g/kg, Leucine Trigger, TEF & Sarcopenia)
2. sleep-calculator.html (90-Minute Ultradian Sleep Cycles, NREM/REM Architecture, Sleep Inertia & Glymphatic System)
Word count target: >1,100 words in article-body each.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 1. protein-intake-calculator.html
# -------------------------------------------------------------
PROTEIN_INTAKE_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Protein Intake Calculator | Evidence-Based Daily Protein Sizer</title>
  <meta name="description" content="Calculate your optimal daily protein intake based on body weight, training goals, fat loss preservation, and clinical standards (RDA, ISSN, and Morton meta-analysis).">
  <link rel="canonical" href="https://calchub.com/protein-intake-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Clinical & Sports Nutrition Protein Intake Calculator",
    "applicationCategory": "HealthApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0.00",
      "priceCurrency": "USD"
    },
    "description": "Calculates evidence-based daily protein targets in grams, per-meal distribution boluses, and grams per kilogram body mass across athletic, fat loss, and clinical sarcopenia cohorts."
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is the difference between the RDA and optimal protein intake for athletes?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Recommended Dietary Allowance (RDA) of 0.8 grams per kilogram of body weight per day (0.36 g/lb) was established by the Food and Nutrition Board to prevent overt nitrogen deficiency in 97.5% of sedentary healthy individuals. It is a biological survival floor, not an optimal target for muscular hypertrophy, tissue repair, or athletic performance. Meta-analyses by Morton et al. demonstrate that active individuals engaged in resistance training require 1.6 to 2.2 g/kg/day (0.73 to 1.0 g/lb) to maximize muscle protein synthesis."
        }
      },
      {
        "@type": "Question",
        "name": "How much protein is needed during a caloric deficit to prevent muscle loss?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "During hypocaloric energy restriction (cutting phases), endogenous protein oxidation increases as gluconeogenesis elevates. Helms et al. and the International Society of Sports Nutrition (ISSN) recommend escalating protein intake to 2.0 to 2.4 g/kg of total body mass (or 2.3 to 3.1 g/kg of fat-free mass) to protect lean skeletal muscle tissue from catabolic breakdown."
        }
      },
      {
        "@type": "Question",
        "name": "What is the 'leucine trigger' and why does per-meal protein distribution matter?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Muscle Protein Synthesis (MPS) is activated via the intracellular mechanistic target of rapamycin complex 1 (mTORC1) pathway. Initiating maximal MPS requires reaching the 'leucine threshold'—typically 2.5 to 3.0 grams of the essential branched-chain amino acid leucine per bolus (equivalent to roughly 25 to 40 grams of high-quality intact protein). Distributing daily protein into 3 to 5 evenly spaced meals every 3 to 5 hours stimulates MPS multiple times throughout the day."
        }
      },
      {
        "@type": "Question",
        "name": "Does high protein intake cause damage to healthy kidneys or bone density?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Comprehensive systematic reviews and randomized controlled trials (including investigations by Antonio et al. examining intakes exceeding 3.3 g/kg/day) confirm that high dietary protein does not impair glomerular filtration rate (GFR), elevate serum creatinine, or compromise renal health in individuals with normal baseline kidney function. Similarly, higher protein intake enhances intestinal calcium absorption and bone mineral density rather than leaching bone minerals."
        }
      },
      {
        "@type": "Question",
        "name": "Why do older adults require more protein than young adults?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Aging induces 'anabolic resistance,' a blunted muscle protein synthetic response to hyperaminoacidemia and hyperinsulinemia. To overcome anabolic resistance, prevent sarcopenia, and maintain physical autonomy, the PROT-AGE study group and ESPEN clinical guidelines recommend that healthy older adults consume 1.2 to 1.5 g/kg/day, with individual meal boluses containing at least 35 to 40 grams of leucine-rich protein."
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
        <li class="active">Protein Intake Calculator</li>
      </ol>
    </nav>

    <div class="page-layout">
      <div class="calculator-container">
        <div class="calculator-card">
          <h1 class="calculator-title">Evidence-Based Protein Intake Calculator</h1>
          <p class="calculator-subtitle">Determine your personalized daily protein intake, per-meal leucine-trigger distribution, and grams per kilogram targets based on exercise physiology standards.</p>

          <form id="protein-form" class="calculator-form">
            <div class="form-row">
              <div class="form-group col-half">
                <label for="unit-system" class="form-label">Measurement Units</label>
                <select id="unit-system" class="form-select">
                  <option value="us" selected>US Customary (lbs, ft/in)</option>
                  <option value="metric">Metric (kg, cm)</option>
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

            <div class="form-row">
              <div class="form-group col-half">
                <label for="body-weight" class="form-label">Current Weight (<span class="weight-unit">lbs</span>)</label>
                <input type="number" id="body-weight" class="form-input" min="60" max="600" value="175" step="0.5" required>
              </div>
              <div class="form-group col-half">
                <label for="body-age" class="form-label">Age (Years)</label>
                <input type="number" id="body-age" class="form-input" min="15" max="100" value="28" required>
              </div>
            </div>

            <div class="form-group">
              <label for="fitness-goal" class="form-label">Primary Training & Health Goal</label>
              <select id="fitness-goal" class="form-select">
                <option value="hypertrophy" selected>Muscle Hypertrophy & Strength Training (ISSN / Morton 1.6–2.2 g/kg)</option>
                <option value="fat-loss">Fat Loss / Caloric Deficit Muscle Retention (Helms 2.0–2.4 g/kg)</option>
                <option value="endurance">Endurance Athletics / Marathon / Cycling (ACSM 1.2–1.6 g/kg)</option>
                <option value="sarcopenia">Healthy Aging / Sarcopenia Prevention (PROT-AGE 1.2–1.5 g/kg)</option>
                <option value="sedentary">Sedentary Maintenance (RDA Baseline 0.8 g/kg)</option>
              </select>
              <small class="form-hint">Targets align with peer-reviewed sports nutrition meta-analyses and clinical guidelines.</small>
            </div>

            <div class="form-row">
              <div class="form-group col-half">
                <label for="meals-count" class="form-label">Daily Meal Frequency</label>
                <select id="meals-count" class="form-select">
                  <option value="3">3 Meals / Day</option>
                  <option value="4" selected>4 Meals / Day (Recommended)</option>
                  <option value="5">5 Meals / Day</option>
                  <option value="6">6 Meals / Day</option>
                </select>
              </div>
              <div class="form-group col-half">
                <label for="activity-level" class="form-label">Physical Activity Tier</label>
                <select id="activity-level" class="form-select">
                  <option value="moderate" selected>Moderate (3-4 gym workouts/week)</option>
                  <option value="high">High (5-7 intense training sessions/week)</option>
                  <option value="low">Low (Light exercise or walking)</option>
                </select>
              </div>
            </div>

            <button type="submit" class="calculate-btn">Calculate Daily Protein Target</button>
          </form>

          <div id="calculator-results" class="results-container" style="display: none;">
            <h2 class="results-heading">Your Evidence-Based Protein Prescription</h2>

            <div class="results-grid">
              <div class="result-card primary-result">
                <span class="result-label">Recommended Daily Target</span>
                <span id="res-target-grams" class="result-value">--</span>
                <span id="res-target-rate" class="result-subtext">-- g/kg body weight</span>
              </div>

              <div class="result-card highlight-card">
                <span class="result-label">Per-Meal Distribution Bolus</span>
                <span id="res-meal-grams" class="result-value">--</span>
                <span class="result-subtext">Exceeds the 2.5g leucine trigger threshold</span>
              </div>

              <div class="result-card">
                <span class="result-label">Optimal Daily Range</span>
                <span id="res-range-grams" class="result-value">--</span>
                <span class="result-subtext">Clinical lower to upper target bounds</span>
              </div>

              <div class="result-card">
                <span class="result-label">Protein Caloric Equivalent</span>
                <span id="res-protein-calories" class="result-value">--</span>
                <span class="result-subtext">Based on 4.0 kcal/g Atwater physiological factor</span>
              </div>

              <div class="result-card">
                <span class="result-label">Rate per Pound (lbs)</span>
                <span id="res-rate-lb" class="result-value">--</span>
                <span class="result-subtext">Grams per lb of total body mass</span>
              </div>

              <div class="result-card">
                <span class="result-label">Sedentary RDA Baseline Comparison</span>
                <span id="res-rda-comparison" class="result-value">--</span>
                <span class="result-subtext">Basic 0.8 g/kg survival floor</span>
              </div>
            </div>

            <div class="summary-box mt-4">
              <h3 class="summary-title">Dietetic Protocol & Anabolic Window Guidance</h3>
              <p id="res-summary-text" class="summary-text">Loading personalized nutrition recommendations...</p>
            </div>
          </div>
        </div>
      </div>

      <aside class="sidebar">
        <div class="sidebar-card">
          <h3 class="sidebar-title">Macronutrient & Metabolic Tools</h3>
          <ul class="sidebar-list">
            <li><a href="macro-calculator.html">Macro Split Calculator</a></li>
            <li><a href="carbohydrate-intake-calculator.html">Carbohydrate Intake Calculator</a></li>
            <li><a href="fat-intake-calculator.html">Fat Intake Calculator</a></li>
            <li><a href="calorie-deficit-calculator.html">Calorie Deficit Calculator</a></li>
            <li><a href="tdee-calculator.html">TDEE Energy Expenditure</a></li>
          </ul>
        </div>
        <div class="sidebar-card mt-4">
          <h3 class="sidebar-title">Clinical Standards</h3>
          <p class="sidebar-text">Based on guidelines from the International Society of Sports Nutrition (ISSN), the American College of Sports Medicine (ACSM), the British Journal of Sports Medicine (Morton et al. 2018), and the PROT-AGE study group.</p>
        </div>
      </aside>
    </div>

    <article class="article-body">
      <h2>The Physiology of Dietary Protein and Muscle Protein Synthesis (MPS)</h2>
      <p>Dietary protein is not merely an energetic macronutrient yielding 4 kilocalories per gram; it is the fundamental biological substrate for cellular life. Dietary proteins are digested into free amino acids and small di- and tri-peptides, absorbed into the portal circulation, and delivered to peripheral tissues to sustain structural proteins (collagen, elastin, actin, myosin), physiological enzymes, immunoglobulins, polypeptide hormones, and transport proteins. The preservation and expansion of skeletal muscle mass are governed by the dynamic equilibrium between <strong>Muscle Protein Synthesis (MPS)</strong> and <strong>Muscle Protein Breakdown (MPB)</strong>:</p>

      $$\text{Net Muscle Protein Balance (NPB)} = \text{MPS} - \text{MPB}$$

      <p>In the post-absorptive (fasted) state, MPB exceeds MPS, resulting in a negative net protein balance. Following protein ingestion, intracellular hyperaminoacidemia stimulates MPS and suppresses MPB, transiently shifting net balance into positive territory. To achieve skeletal muscle hypertrophy or maintain muscle mass during energetic stress, cumulative MPS over 24-hour cycles must exceed cumulative MPB.</p>

      <h2>The Recommended Dietary Allowance (RDA) vs. Athletic Optimization</h2>
      <p>A central point of confusion in nutritional science is the distinction between biological sufficiency and physiological optimization. The established <strong>Recommended Dietary Allowance (RDA)</strong> for protein is <strong>0.8 grams per kilogram of body weight per day (0.36 g/lb)</strong> for healthy adults:</p>
      <ul>
        <li><strong>Epidemiological Purpose of the RDA:</strong> The RDA was calculated by the Food and Nutrition Board of the Institute of Medicine utilizing traditional nitrogen balance studies. The experimental goal was to determine the statistical intake required to prevent negative nitrogen balance (overt protein deficiency) in 97.5% of the healthy sedentary population. It represents a <em>survival floor</em> designed to prevent Kwashiorkor and systemic muscle wasting—not a recommendation for active individuals seeking optimal physical function.</li>
        <li><strong>Methodological Limitations of Nitrogen Balance:</strong> Traditional nitrogen balance measurements systematically underestimate dermal, sweat, and fecal nitrogen losses while overestimating intake, artificially suppressing estimated protein requirements. Modern methodologies utilizing the <em>Indicator Amino Acid Oxidation (IAAO)</em> technique demonstrate that even sedentary adults require approximately <strong>1.0 to 1.2 g/kg/day</strong> to reach physiological saturation.</li>
      </ul>

      <h2>The Morton et al. Meta-Analysis: The 1.62 g/kg/day Hypertrophy Ceiling</h2>
      <p>In 2018, Dr. Robert Morton and colleagues published a landmark systematic review and meta-analysis in the <em>British Journal of Sports Medicine</em> encompassing 49 randomized controlled trials and 1,863 resistance-trained participants. The authors evaluated the relationship between graded daily protein intakes and gains in fat-free mass (FFM) and one-repetition maximum (1RM) strength. Their findings established the following clinical insights:</p>

      $$P_{\text{breakpoint}} = 1.62 \text{ g/kg/day} \quad [95\% \text{ CI: } 1.03 - 2.20 \text{ g/kg/day}]$$

      <p>While the mean inflection point beyond which further protein ingestion yielded no statistically significant additional muscle mass was 1.62 g/kg/day, the upper bound of the 95% confidence interval reached <strong>2.20 g/kg/day (1.0 g/lb/day)</strong>. Consequently, the consensus recommendation endorsed by the <strong>International Society of Sports Nutrition (ISSN)</strong> for athletes engaged in resistance exercise spans <strong>1.6 to 2.2 g/kg/day (0.73 to 1.0 g/lb/day)</strong>.</p>

      <div class="table-container my-4">
        <table class="data-table">
          <thead>
            <tr>
              <th>Cohort &amp; Training Modality</th>
              <th>Target Protein (g/kg/day)</th>
              <th>Target Protein (g/lb/day)</th>
              <th>Physiological Mechanism &amp; Rationale</th>
              <th>Reference Guideline</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Sedentary Baseline</strong></td>
              <td>0.8 – 1.0 g/kg</td>
              <td>0.36 – 0.45 g/lb</td>
              <td>Prevents negative nitrogen balance and lean tissue depletion in non-exercisers.</td>
              <td>DRI / WHO Standards</td>
            </tr>
            <tr>
              <td><strong>Endurance Athletes (Runners, Cyclists)</strong></td>
              <td>1.2 – 1.6 g/kg</td>
              <td>0.55 – 0.73 g/lb</td>
              <td>Offsets amino acid oxidation during prolonged aerobic exercise; repairs mitochondrial enzymes.</td>
              <td>ACSM / ISSN Joint Stand</td>
            </tr>
            <tr>
              <td><strong>Strength / Muscle Hypertrophy</strong></td>
              <td>1.6 – 2.2 g/kg</td>
              <td>0.73 – 1.00 g/lb</td>
              <td>Maximizes myofibrillar MPS, satellite cell proliferation, and contractile tissue hypertrophy.</td>
              <td>Morton et al. (BJSM 2018)</td>
            </tr>
            <tr>
              <td><strong>Fat Loss / Caloric Restriction</strong></td>
              <td>2.0 – 2.4 g/kg</td>
              <td>0.91 – 1.10 g/lb</td>
              <td>Prevents catabolism of fat-free mass during energy deficit; enhances satiety and TEF.</td>
              <td>Helms et al. / ISSN Position</td>
            </tr>
            <tr>
              <td><strong>Older Adults (&gt;65y / Sarcopenia)</strong></td>
              <td>1.2 – 1.5 g/kg</td>
              <td>0.55 – 0.68 g/lb</td>
              <td>Overcomes age-related anabolic resistance and blunted postprandial hyperaminoacidemia.</td>
              <td>PROT-AGE Study Group</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>The Leucine Trigger and Optimal Per-Meal Bolus Distribution</h2>
      <p>Total daily protein quantity is the primary driver of body composition, but the timing and distribution of individual protein feedings significantly influence the magnitude of Muscle Protein Synthesis. Intracellular signaling governing MPS is stimulated through the <strong>mechanistic Target of Rapamycin Complex 1 (mTORC1)</strong> kinase cascade. Activation of mTORC1 requires phosphorylation of downstream target proteins, including p70S6 kinase ($p70^{S6K}$) and eukaryotic initiation factor 4E-binding protein 1 ($4E\text{-}BP1$).</p>

      <p>Crucially, mTORC1 activation is sensitive to the intracellular concentration of the branched-chain amino acid (BCAA) <strong>leucine</strong>. This phenomenon is termed the <strong>Leucine Trigger Hypothesis</strong>:</p>
      <ul>
        <li><strong>The Leucine Threshold:</strong> To maximally stimulate MPS, an individual meal bolus must provide between <strong>2.5 and 3.0 grams of leucine</strong> (or roughly 0.05 g leucine per kg of body mass per meal). Sub-threshold doses fail to fully saturate sestrin2 sensors and produce an attenuated synthetic response.</li>
        <li><strong>Equivalent Intact Protein Mass:</strong> In high-quality animal proteins (whey, milk, eggs, beef, poultry, fish), leucine comprises approximately 8% to 11% of total amino acid content. Reaching 2.5–3.0g of leucine requires consuming approximately <strong>25 to 40 grams of complete protein per feeding</strong>.</li>
        <li><strong>Meal Frequency &amp; Refractory Period:</strong> Once stimulated, MPS remains elevated for approximately 2 to 3 hours before returning to baseline, regardless of ongoing aminoacidemia (a phenomenon known as the <em>muscle full effect</em>). Consuming 3 to 5 distinct protein-rich meals spaced every 3 to 5 hours stimulates MPS multiple times throughout the day far more effectively than consuming a single massive bolus.</li>
      </ul>

      <h2>Thermic Effect of Food (TEF) and Satiety Mechanisms</h2>
      <p>Dietary protein plays a powerful metabolic role during weight management and fat loss due to its superior <strong>Thermic Effect of Food (TEF)</strong>. TEF represents the metabolic cost of digestion, peptide breakdown, hepatic deamination, and urea cycle excretion:</p>

      $$\text{TEF}_{\text{Protein}} = 20\% - 30\% \quad \text{vs.} \quad \text{TEF}_{\text{Carbohydrate}} = 5\% - 10\% \quad \text{vs.} \quad \text{TEF}_{\text{Fat}} = 0\% - 3\%$$

      <p>Consuming 100 kcal of dietary protein burns 20 to 30 kcal purely through metabolic processing, yielding a net physiological availability of only 70 to 80 kcal. Furthermore, dietary amino acids stimulate the release of potent peripheral satiety peptide hormones—including peptide YY ($PYY$), glucagon-like peptide-1 ($GLP-1$), and cholecystokinin ($CCK$)—while suppressing orexigenic ghrelin secretion from the gastric fundus.</p>

      <h2>Step-by-Step Worked Clinical Case Study</h2>
      <p>The following case study illustrates an evidence-based sports dietetic assessment for an athlete seeking concurrent muscular hypertrophy and body recomposition:</p>

      <div class="worked-example-card my-4">
        <h3 class="example-title">Dietetic Case Profile: Hypertrophy &amp; Recomposition Sizing</h3>
        <p><strong>Patient Baseline:</strong> A 26-year-old male resistance-trained athlete weighing <strong>180 lbs (81.65 kg)</strong> at 14% body fat seeks to maximize lean muscle accretion while minimizing adipose accumulation. He performs 4 heavy barbell hypertrophy sessions per week.</p>
        
        <div class="example-step">
          <div class="step-num">Step 1</div>
          <div class="step-content">
            <strong>Determine Target Daily Protein Intake per Kilogram:</strong>
            Applying the Morton meta-analytic consensus (1.6 to 2.2 g/kg/day), a dedicated hypertrophy target is established at <strong>2.0 g/kg/day</strong>.
            $$\text{Daily Protein Target} = 81.65 \text{ kg} \times 2.0 \text{ g/kg} = \mathbf{163.3 \text{ g/day}} \approx 165 \text{ g/day}$$
            In imperial units: $165 \text{ g} / 180 \text{ lbs} = \mathbf{0.92 \text{ g/lb/day}}$.
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 2</div>
          <div class="step-content">
            <strong>Calculate Per-Meal Distribution Boluses:</strong>
            The athlete follows a 4-meal daily schedule (Breakfast, Lunch, Post-Workout, Dinner).
            $$\text{Per-Meal Bolus} = \frac{165 \text{ g}}{4 \text{ meals}} = \mathbf{41.25 \text{ g/meal}}$$
            A bolus of 41.25 grams easily delivers ~3.5 to 4.0 grams of leucine, decisively exceeding the 2.5g leucine trigger threshold at every feeding.
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 3</div>
          <div class="step-content">
            <strong>Compute Caloric and TEF Energetic Contribution:</strong>
            Gross caloric energy provided by protein:
            $$\text{Gross Protein Energy} = 165 \text{ g} \times 4.0 \text{ kcal/g} = \mathbf{660 \text{ kcal/day}}$$
            Net thermic metabolic cost (assuming average 25% TEF):
            $$\text{Thermic Burn} = 660 \text{ kcal} \times 0.25 = \mathbf{165 \text{ kcal/day expended in assimilation}}$$
            Net physiological energy yield: $660 - 165 = 495 \text{ kcal/day}$.
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 4</div>
          <div class="step-content">
            <strong>Evaluate Renal &amp; Bone Biomarkers:</strong>
            Baseline serum creatinine (0.9 mg/dL) and estimated glomerular filtration rate ($eGFR > 90 \text{ mL/min/1.73m}^2$) confirm normal renal baseline. An intake of 2.0 g/kg/day falls safely below clinical concern thresholds, with adequate daily hydration (3.5 L/day) maintaining optimal urinary solute clearance.
          </div>
        </div>
      </div>

      <h2>Protein Quality Metrics: PDCAAS, DIAAS, and Plant Protein Complementation</h2>
      <p>Not all dietary protein sources possess equivalent biological bioavailability. Protein quality is determined by two factors: amino acid profile (proportions of essential amino acids relative to human tissue requirements) and ileal digestibility:</p>
      <ul>
        <li><strong>PDCAAS (Protein Digestibility-Corrected Amino Acid Score):</strong> Truncated at 1.0, PDCAAS evaluates fecal digestibility. Whey, casein, egg white, and soy isolate score 1.0.</li>
        <li><strong>DIAAS (Digestible Indispensable Amino Acid Score):</strong> The modern gold standard adopted by the FAO, measuring true ileal digestibility without score truncation. Whey isolate scores 1.15–1.30, demonstrating superior digestible amino acid density.</li>
        <li><strong>Plant-Based Protein Optimization:</strong> Many single plant sources contain a limiting amino acid (e.g., legumes are low in methionine and cysteine; cereal grains are low in lysine). Vegan athletes can match animal protein muscle-building efficacy by consuming 10% to 20% higher total protein (1.8–2.4 g/kg/day) and pairing complementary protein sources (e.g., rice and pea protein blends) to ensure leucine and essential amino acid adequacy.</li>
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
            <li><a href="protein-intake-calculator.html">Protein Intake Calculator</a></li>
            <li><a href="macro-calculator.html">Macro Split Calculator</a></li>
            <li><a href="calorie-deficit-calculator.html">Calorie Deficit Calculator</a></li>
            <li><a href="tdee-calculator.html">TDEE Calculator</a></li>
            <li><a href="lean-body-mass-calculator.html">Lean Body Mass Calculator</a></li>
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
        <p>&copy; 2026 CalcHub. Educational and clinical calculation tools. Consult a registered dietitian or physician for individualized nutrition therapy.</p>
      </div>
    </div>
  </footer>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const form = document.getElementById('protein-form');
      const unitSystem = document.getElementById('unit-system');
      const bodyWeightInput = document.getElementById('body-weight');
      const weightUnitLabels = document.querySelectorAll('.weight-unit');
      const goalSelect = document.getElementById('fitness-goal');
      const mealsSelect = document.getElementById('meals-count');
      const resultsContainer = document.getElementById('calculator-results');

      // Unit switch
      unitSystem.addEventListener('change', function() {
        const isMetric = unitSystem.value === 'metric';
        if (isMetric) {
          weightUnitLabels.forEach(el => el.textContent = 'kg');
          bodyWeightInput.value = (parseFloat(bodyWeightInput.value) * 0.453592).toFixed(1);
          bodyWeightInput.min = '30';
          bodyWeightInput.max = '280';
        } else {
          weightUnitLabels.forEach(el => el.textContent = 'lbs');
          bodyWeightInput.value = (parseFloat(bodyWeightInput.value) / 0.453592).toFixed(1);
          bodyWeightInput.min = '60';
          bodyWeightInput.max = '600';
        }
      });

      form.addEventListener('submit', function(e) {
        e.preventDefault();

        const isMetric = unitSystem.value === 'metric';
        const rawWeight = parseFloat(bodyWeightInput.value) || 0;
        const goal = goalSelect.value;
        const meals = parseInt(mealsSelect.value) || 4;

        if (rawWeight <= 0) return;

        const weightKg = isMetric ? rawWeight : rawWeight * 0.453592;
        const weightLbs = isMetric ? rawWeight / 0.453592 : rawWeight;

        // Determine target rate (g/kg) and range
        let targetRate = 2.0;
        let minRate = 1.6;
        let maxRate = 2.2;
        let protocolDescription = '';

        if (goal === 'hypertrophy') {
          targetRate = 2.0;
          minRate = 1.6;
          maxRate = 2.2;
          protocolDescription = 'Targeting 1.6 to 2.2 g/kg/day optimizes muscle protein synthesis for resistance-trained individuals (Morton et al. 2018). Focus on 25–40g complete protein per meal to trigger maximal mTORC1 activation.';
        } else if (goal === 'fat-loss') {
          targetRate = 2.2;
          minRate = 2.0;
          maxRate = 2.5;
          protocolDescription = 'Elevated protein during hypocaloric phases (2.0–2.5 g/kg/day) protects lean skeletal muscle mass from catabolism, maximizes the thermic effect of food (TEF), and maintains high satiety.';
        } else if (goal === 'endurance') {
          targetRate = 1.4;
          minRate = 1.2;
          maxRate = 1.6;
          protocolDescription = 'Endurance training increases leucine oxidation during prolonged aerobic work. An intake of 1.2–1.6 g/kg supports mitochondrial enzyme repair and glycogen recovery without excessive digestive load.';
        } else if (goal === 'sarcopenia') {
          targetRate = 1.35;
          minRate = 1.2;
          maxRate = 1.5;
          protocolDescription = 'Older adults experience anabolic resistance. Consuming 1.2–1.5 g/kg/day with leucine-rich boluses (≥35g per feeding) overcomes blunted protein synthesis and preserves bone mineral density and physical independence.';
        } else {
          // Sedentary
          targetRate = 0.85;
          minRate = 0.8;
          maxRate = 1.0;
          protocolDescription = 'The Recommended Dietary Allowance (0.8 g/kg) provides the statistical baseline to prevent negative nitrogen balance in sedentary adults. For enhanced metabolic health, 1.0–1.2 g/kg is frequently recommended.';
        }

        const totalGrams = Math.round(weightKg * targetRate);
        const minGrams = Math.round(weightKg * minRate);
        const maxGrams = Math.round(weightKg * maxRate);
        const mealBolus = (totalGrams / meals).toFixed(1);
        const proteinKcal = totalGrams * 4;
        const ratePerLb = (totalGrams / weightLbs).toFixed(2);
        const rdaBaselineGrams = Math.round(weightKg * 0.8);

        // Display results
        document.getElementById('res-target-grams').textContent = totalGrams + ' g / day';
        document.getElementById('res-target-rate').textContent = targetRate.toFixed(2) + ' g/kg body weight';
        document.getElementById('res-meal-grams').textContent = mealBolus + ' g / meal';
        document.getElementById('res-range-grams').textContent = minGrams + ' – ' + maxGrams + ' g';
        document.getElementById('res-protein-calories').textContent = proteinKcal + ' kcal / day';
        document.getElementById('res-rate-lb').textContent = ratePerLb + ' g / lb';
        document.getElementById('res-rda-comparison').textContent = rdaBaselineGrams + ' g (RDA Floor)';
        document.getElementById('res-summary-text').textContent = protocolDescription;

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
# 2. sleep-calculator.html
# -------------------------------------------------------------
SLEEP_CALCULATOR_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sleep Calculator | 90-Minute Sleep Cycle & Alarm Sizer</title>
  <meta name="description" content="Calculate optimal wake-up times and bedtimes based on 90-minute ultradian sleep cycles (NREM & REM), sleep latency, and avoiding groggy sleep inertia.">
  <link rel="canonical" href="https://calchub.com/sleep-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Clinical Sleep Cycle & Bedtime Calculator",
    "applicationCategory": "HealthApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0.00",
      "priceCurrency": "USD"
    },
    "description": "Calculates prospective bedtimes and wake times utilizing 90-minute ultradian sleep cycle architecture, sleep onset latency offsets, and circadian sleep inertia mitigation."
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "How long is a natural human sleep cycle?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A standard human ultradian sleep cycle lasts approximately 90 minutes on average (typically ranging between 80 and 110 minutes across normal adults). Each cycle transitions sequentially through non-rapid eye movement stages (NREM N1 light transition, N2 consolidated sleep, N3 slow-wave deep sleep) and concludes with Rapid Eye Movement (REM) dream sleep."
        }
      },
      {
        "@type": "Question",
        "name": "Why do I feel exhausted even after sleeping 8 hours?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Waking up feeling groggy, disoriented, and fatigued is termed 'sleep inertia.' It occurs primarily when an alarm interrupts Stage N3 slow-wave deep sleep (delta wave sleep), rather than during light N1/N2 sleep or at the natural completion of a 90-minute cycle. Sleeping 7.5 hours (exactly 5 full 90-minute cycles) frequently leaves people feeling significantly more refreshed than sleeping 8 hours (5.33 cycles, awakening midway through deep slow-wave sleep)."
        }
      },
      {
        "@type": "Question",
        "name": "What is sleep latency and how much time should be factored into bedtimes?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Sleep onset latency is the time elapsed between lying down in bed with the intention to sleep and the electroencephalographic transition to Stage N1 sleep. In healthy adults, physiological sleep latency averages 14 minutes (clinically normal: 10 to 20 minutes). If latency is under 5 minutes, severe chronic sleep deprivation is likely present; if latency exceeds 30 minutes, clinical insomnia may be present."
        }
      },
      {
        "@type": "Question",
        "name": "What is the glymphatic system and why is deep sleep essential for brain health?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Discovered by Dr. Maiken Nedergaard, the glymphatic system is a glia-mediated convective waste clearance pathway. During Stage N3 slow-wave sleep, interstitial space volume expands by 60%, allowing cerebrospinal fluid (CSF) to wash through cerebral parenchyma via astrocytic aquaporin-4 (AQP4) water channels. This process actively clears neurotoxic metabolic aggregates, including amyloid-beta and phosphorylated tau."
        }
      },
      {
        "@type": "Question",
        "name": "How many sleep cycles are recommended per night?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Healthy adults typically require 5 to 6 completed sleep cycles per night, corresponding to 7.5 to 9.0 hours of actual sleep. Four completed cycles (6.0 hours) represents the absolute minimum chronic threshold to prevent progressive neurocognitive degradation and metabolic dysfunction."
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
        <li class="active">Sleep Calculator</li>
      </ol>
    </nav>

    <div class="page-layout">
      <div class="calculator-container">
        <div class="calculator-card">
          <h1 class="calculator-title">Clinical Sleep Cycle & Bedtime Calculator</h1>
          <p class="calculator-subtitle">Calculate optimal sleep and wake times anchored to 90-minute ultradian sleep architecture, sleep latency, and circadian rhythm harmonization.</p>

          <form id="sleep-form" class="calculator-form">
            <div class="form-group">
              <label for="calc-mode" class="form-label">Calculation Mode</label>
              <select id="calc-mode" class="form-select">
                <option value="wakeup" selected>I need to wake up at a specific time (Find Bedtime)</option>
                <option value="bedtime">I am going to bed at a specific time (Find Wake-Up Time)</option>
                <option value="now">I am going to sleep right now (Find Wake-Up Time)</option>
              </select>
            </div>

            <div id="target-time-group" class="form-row">
              <div class="form-group col-half">
                <label for="target-hour" class="form-label">Hour</label>
                <select id="target-hour" class="form-select">
                  <option value="1">1</option>
                  <option value="2">2</option>
                  <option value="3">3</option>
                  <option value="4">4</option>
                  <option value="5">5</option>
                  <option value="6">6</option>
                  <option value="7" selected>7</option>
                  <option value="8">8</option>
                  <option value="9">9</option>
                  <option value="10">10</option>
                  <option value="11">11</option>
                  <option value="12">12</option>
                </select>
              </div>
              <div class="form-group col-half">
                <label for="target-minute" class="form-label">Minute &amp; AM/PM</label>
                <div style="display:flex;gap:0.5rem;">
                  <select id="target-minute" class="form-select" style="flex:1;">
                    <option value="0" selected>00</option>
                    <option value="5">05</option>
                    <option value="10">10</option>
                    <option value="15">15</option>
                    <option value="20">20</option>
                    <option value="25">25</option>
                    <option value="30">30</option>
                    <option value="35">35</option>
                    <option value="40">40</option>
                    <option value="45">45</option>
                    <option value="50">50</option>
                    <option value="55">55</option>
                  </select>
                  <select id="target-ampm" class="form-select" style="width:85px;">
                    <option value="AM" selected>AM</option>
                    <option value="PM">PM</option>
                  </select>
                </div>
              </div>
            </div>

            <div class="form-group">
              <label for="latency-mins" class="form-label">Average Time to Fall Asleep (Sleep Latency): <span id="latency-display" class="font-bold text-primary">15 minutes</span></label>
              <div class="slider-container">
                <input type="range" id="latency-mins" min="0" max="45" value="15" step="5" class="form-slider">
              </div>
              <small class="form-hint">Healthy adults average 14 minutes of sleep onset latency (range: 10–20 mins).</small>
            </div>

            <button type="submit" class="calculate-btn">Calculate Optimal Sleep Cycles</button>
          </form>

          <div id="calculator-results" class="results-container" style="display: none;">
            <h2 class="results-heading" id="results-headline">Recommended Times</h2>
            <p id="results-intro" class="calculator-subtitle">Waking up at the completion of a 90-minute sleep cycle ensures you wake during light sleep, avoiding groggy sleep inertia.</p>

            <div class="results-grid">
              <div class="result-card primary-result">
                <span class="result-label" id="res-card-label-6">6 Cycles (Optimal 9.0 Hours)</span>
                <span id="res-time-6" class="result-value">--</span>
                <span class="result-subtext">Peak cognitive & athletic restoration</span>
              </div>

              <div class="result-card highlight-card">
                <span class="result-label" id="res-card-label-5">5 Cycles (Recommended 7.5 Hours)</span>
                <span id="res-time-5" class="result-value">--</span>
                <span class="result-subtext">Standard healthy adult baseline</span>
              </div>

              <div class="result-card">
                <span class="result-label" id="res-card-label-4">4 Cycles (Minimum 6.0 Hours)</span>
                <span id="res-time-4" class="result-value">--</span>
                <span class="result-subtext">Acceptable short-term threshold</span>
              </div>

              <div class="result-card">
                <span class="result-label" id="res-card-label-3">3 Cycles (Power Sleep 4.5 Hours)</span>
                <span id="res-time-3" class="result-value">--</span>
                <span class="result-subtext">Emergency shift-work / temporary rest</span>
              </div>
            </div>

            <div class="summary-box mt-4">
              <h3 class="summary-title">Sleep Architecture Breakdown</h3>
              <p id="res-architecture-text" class="summary-text">Loading polysomnography analysis...</p>
            </div>
          </div>
        </div>
      </div>

      <aside class="sidebar">
        <div class="sidebar-card">
          <h3 class="sidebar-title">Circadian & Health Tools</h3>
          <ul class="sidebar-list">
            <li><a href="tdee-calculator.html">TDEE Energy Expenditure</a></li>
            <li><a href="calorie-calculator.html">Calorie Maintenance Calculator</a></li>
            <li><a href="water-intake-calculator.html">Daily Hydration Sizer</a></li>
            <li><a href="max-heart-rate-calculator.html">Max Heart Rate Calculator</a></li>
            <li><a href="bac-calculator.html">Blood Alcohol Concentration (BAC)</a></li>
          </ul>
        </div>
        <div class="sidebar-card mt-4">
          <h3 class="sidebar-title">Clinical Standards</h3>
          <p class="sidebar-text">Based on clinical sleep medicine parameters from the American Academy of Sleep Medicine (AASM), the Sleep Research Society (SRS), and the National Sleep Foundation.</p>
        </div>
      </aside>
    </div>

    <article class="article-body">
      <h2>Neurobiology of Human Sleep Architecture and Ultradian Rhythms</h2>
      <p>Sleep is not an inert physiological state of unconsciousness, but an active, highly organized neurobiological process essential for cerebral homeostasis, synaptic plasticity, memory consolidation, immunological competence, and systemic metabolic regulation. Electroencephalography (EEG), electrooculography (EOG), and electromyography (EMG) demonstrate that human sleep is structured into periodic, predictable <strong>ultradian cycles</strong> lasting approximately <strong>90 minutes</strong> (typically spanning 80 to 110 minutes in healthy adults). Across a typical nocturnal sleep period of 7 to 9 hours, a human adult completes four to six discrete sleep cycles.</p>

      <p>Each 90-minute sleep cycle is comprised of two distinct biological states:</p>
      <ul>
        <li><strong>Non-Rapid Eye Movement (NREM) Sleep:</strong> Subdivided into three distinct stages representing progressive deepening of sleep and slowing of cortical electrophysiological oscillations.</li>
        <li><strong>Rapid Eye Movement (REM) Sleep:</strong> Characterized by high-frequency, desynchronized cortical EEG patterns resembling wakefulness, rapid conjugate eye movements, muscle atonia, and vivid narrative dreaming.</li>
      </ul>

      <h2>The Four Stages of Human Sleep (AASM Classification)</h2>
      <p>The <em>American Academy of Sleep Medicine (AASM)</em> established the standardized scoring criteria for the stages of human sleep:</p>

      <div class="table-container my-4">
        <table class="data-table">
          <thead>
            <tr>
              <th>Sleep Stage</th>
              <th>Predominant EEG Waveforms</th>
              <th>Percentage of Total Sleep</th>
              <th>Physiological Characteristics</th>
              <th>Primary Biological Function</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Stage N1 (Light Transition)</strong></td>
              <td>Theta waves (4 – 7 Hz), alpha dropout</td>
              <td>2% – 5%</td>
              <td>Hypnagogic jerks, slow rolling eye movements, easily aroused by faint noise.</td>
              <td>Initial bridge between wakefulness and consolidated sleep.</td>
            </tr>
            <tr>
              <td><strong>Stage N2 (Consolidated Light Sleep)</strong></td>
              <td>Sleep spindles (11–16 Hz) &amp; K-complexes</td>
              <td>45% – 55%</td>
              <td>Heart rate decelerates, core body temperature drops, metabolic rate declines.</td>
              <td>Motor skill procedural memory consolidation, sensory gating via thalamic reticular nucleus.</td>
            </tr>
            <tr>
              <td><strong>Stage N3 (Slow-Wave Deep Sleep / SWS)</strong></td>
              <td>High-voltage Delta waves (0.5 – 2 Hz, &gt;75 &mu;V)</td>
              <td>15% – 25%</td>
              <td>Profound parasympathetic dominance, minimal muscle tone, highest awakening threshold.</td>
              <td>Human Growth Hormone (HGH) secretion, tissue repair, glymphatic neurotoxin clearance.</td>
            </tr>
            <tr>
              <td><strong>REM Sleep (Paradoxical Sleep)</strong></td>
              <td>Sawtooth waves, low-voltage mixed frequency</td>
              <td>20% – 25%</td>
              <td>Somatic muscle atonia (glycinergic/GABAergic motor neuron inhibition), variable HR and breathing.</td>
              <td>Emotional memory processing, affective regulation, creative synthesis, and neuroplasticity.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>The Glymphatic Waste Clearance System</h2>
      <p>A transformative discovery in contemporary neuroscience, spearheaded by Dr. Maiken Nedergaard at the University of Rochester Medical Center, identified the <strong>Glymphatic System</strong>—a brain-wide waste clearance network that operates almost exclusively during deep slow-wave sleep (Stage N3):</p>
      <ul>
        <li><strong>Mechanism of Astrocytic Clearance:</strong> During wakefulness, interstitial space within the brain is tightly compressed. During Stage N3 slow-wave sleep, glial cells (astrocytes) shrink, expanding interstitial space volume by <strong>60%</strong>. This creates a low-resistance pathway allowing arterial pulsations to drive convective influx of Cerebrospinal Fluid (CSF) along periarterial channels, filtering across astrocytic endfeet via <strong>Aquaporin-4 (AQP4) water channels</strong>.</li>
        <li><strong>Elimination of Neurotoxic Aggregates:</strong> Convective interstitial fluid flow sweeps neurotoxic protein byproducts—including <strong>amyloid-beta ($A\beta$)</strong>, <strong>phosphorylated tau</strong>, and alpha-synuclein—into perivenous spaces for lymphatic drainage into the deep cervical lymph nodes.</li>
        <li><strong>Clinical Pathology of Sleep Fragmentation:</strong> Chronic suppression or fragmentation of Stage N3 sleep severely impairs glymphatic clearance, accelerating cerebral accumulation of amyloid-beta plaques and neurofibrillary tangles, fundamentally elevating long-term risks for Alzheimer's disease and vascular dementia.</li>
      </ul>

      <h2>Sleep Inertia and the Math of Sleep Cycle Synchronization</h2>
      <p>A widespread clinical complaint is waking up feeling exhausted, disoriented, and cognitively sluggish despite having slept for 8 or 9 hours. This debilitating state is clinically diagnosed as <strong>Sleep Inertia</strong>. Sleep inertia is caused by an abrupt forced awakening during <strong>Stage N3 Slow-Wave Deep Sleep</strong>, characterized by high-amplitude delta activity. Upon forced waking from Stage N3, the prefrontal cortex exhibits transient hypoperfusion and high lingering concentrations of the neuromodulator <strong>adenosine</strong>, impairing reaction time, working memory, and executive decision-making for 30 to 90 minutes.</p>

      <p>Conversely, waking up at the conclusion of a 90-minute sleep cycle—when the brain has naturally transitioned through REM back into light Stage N1 or Stage N2 sleep—minimizes sleep inertia and allows instantaneous alertness. The mathematical model for optimal bedtimes and alarm times incorporates completed 90-minute ultradian cycles ($C$) and sleep onset latency ($L_{\text{sleep}}$):</p>

      $$\text{Total Sleep Duration} = (N_{\text{cycles}} \times 90 \text{ min}) + L_{\text{sleep}}$$

      <p>Where $N_{\text{cycles}}$ typically equals 5 (7.5 hours of sleep) or 6 (9.0 hours of sleep), and $L_{\text{sleep}}$ represents average physiological sleep onset latency (typically 14 to 15 minutes in healthy adults).</p>

      <h2>Circadian Biology: Melatonin, Cortisol, and Adenosine Pressure</h2>
      <p>Human sleep-wake timing is governed by the classic <strong>Two-Process Model of Sleep Regulation</strong> formulated by Alexander Borb&eacute;ly:</p>
      <ul>
        <li><strong>Process S (Homeostatic Sleep Pressure):</strong> Sleep pressure accumulates as an exponential function of continuous wakefulness. As cerebral neurons hydrolyze Adenosine Triphosphate ($ATP$) for metabolic energy, extracellular concentrations of free <strong>adenosine</strong> rise continuously in the basal forebrain and cortex, binding to inhibitory $A_1$ and $A_{2A}$ receptors. Caffeine functions as a competitive antagonist of adenosine receptors, masking sleep pressure without clearing adenosine. During sleep, adenosine is rapidly metabolized and re-phosphorylated, dissipating Process S.</li>
        <li><strong>Process C (Circadian Pacemaker):</strong> Driven by the master circadian pacemaker located in the <strong>Suprachiasmatic Nucleus (SCN)</strong> of the anterior hypothalamus. Synchronized by photic input from intrinsically photosensitive retinal ganglion cells (ipRGCs) via the retinohypothalamic tract, the SCN regulates the rhythmic secretion of <strong>melatonin</strong> from the pineal gland. Melatonin begins rising 2 to 3 hours before habitual bedtime (Dim Light Melatonin Onset, DLMO), peak nocturnal levels occur between 2:00 AM and 4:00 AM, and the <strong>Cortisol Awakening Response (CAR)</strong> triggers morning arousal and alertness.</li>
      </ul>

      <h2>Step-by-Step Worked Clinical Case Study</h2>
      <p>The following case study illustrates an evidence-based circadian and sleep cycle optimization protocol for a working professional:</p>

      <div class="worked-example-card my-4">
        <h3 class="example-title">Polysomnographic Case Profile: Sleep Inertia Elimination</h3>
        <p><strong>Patient Baseline:</strong> A 34-year-old financial analyst must wake up at <strong>6:30 AM</strong> every weekday for work. She currently sets an alarm for 6:30 AM and goes to bed at 10:30 PM (8.0 hours in bed), but complains of chronic morning grogginess and reliance on high-dose caffeine. Her average sleep onset latency is <strong>15 minutes</strong>.</p>
        
        <div class="example-step">
          <div class="step-num">Step 1</div>
          <div class="step-content">
            <strong>Analyze the Patient's Current Sleep Cycle Timing:</strong>
            $$\text{Time in Bed} = \text{10:30 PM to 6:30 AM} = 8.0 \text{ hours} = 480 \text{ minutes}$$
            $$\text{Actual Sleep Time} = 480 - 15 \text{ min (latency)} = 465 \text{ minutes}$$
            $$\text{Cycles Completed} = \frac{465 \text{ min}}{90 \text{ min/cycle}} = \mathbf{5.17 \text{ cycles}}$$
            Because she wakes at 5.17 cycles, her 6:30 AM alarm systematically rings 15 minutes into the deep slow-wave sleep (Stage N3) of her 6th cycle, triggering severe sleep inertia!
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 2</div>
          <div class="step-content">
            <strong>Calculate Target Bedtimes for 5 Completed Cycles (7.5 Hours of Sleep):</strong>
            $$\text{Target Sleep Duration} = 5 \times 90 \text{ min} = 450 \text{ minutes} = 7 \text{ hours } 30 \text{ minutes}$$
            $$\text{Total Time in Bed} = 450 \text{ min} + 15 \text{ min (latency)} = 465 \text{ minutes} = 7 \text{ hours } 45 \text{ minutes}$$
            Subtracting 7 hours 45 minutes from 6:30 AM wake-up:
            $$\text{Optimal Bedtime (5 Cycles)} = \mathbf{10:45 \text{ PM}}$$
            Going to sleep at 10:45 PM allows her to wake precisely at the completion of cycle 5 in light Stage N1/N2 sleep.
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 3</div>
          <div class="step-content">
            <strong>Calculate Target Bedtimes for 6 Completed Cycles (9.0 Hours of Sleep):</strong>
            $$\text{Target Sleep Duration} = 6 \times 90 \text{ min} = 540 \text{ minutes} = 9 \text{ hours } 00 \text{ minutes}$$
            $$\text{Total Time in Bed} = 540 \text{ min} + 15 \text{ min} = 555 \text{ minutes} = 9 \text{ hours } 15 \text{ minutes}$$
            Subtracting 9 hours 15 minutes from 6:30 AM wake-up:
            $$\text{Optimal Bedtime (6 Cycles)} = \mathbf{9:15 \text{ PM}}$$
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 4</div>
          <div class="step-content">
            <strong>Clinical Intervention &amp; Outcome:</strong>
            The clinician instructs the patient to shift her bedtime from 10:30 PM to <strong>10:45 PM</strong>. Despite spending 15 fewer minutes in bed, she awakens at the conclusion of her 5th cycle rather than in deep N3 slow-wave sleep. Morning sleep inertia resolves completely within three days, with sustained improvements in daytime vigilance and executive cognitive function.
          </div>
        </div>
      </div>

      <h2>Evidence-Based Sleep Hygiene and Chronobiology Principles</h2>
      <p>To maximize sleep architecture quality and consolidate deep Stage N3 and REM sleep, sleep medicine specialists recommend several environmental and behavioral adaptations:</p>
      <ul>
        <li><strong>Thermal Regulation:</strong> Sleep onset requires a drop in core body temperature of approximately $1^\circ\text{C}$ ($2^\circ\text{F}$), facilitated by cutaneous vasodilation in the distal extremities (hands and feet). Maintaining bedroom ambient temperature at <strong>65°F to 68°F (18°C to 20°C)</strong> facilitates natural heat dissipation.</li>
        <li><strong>Light Spectrum Management:</strong> Blue wavelength light (460–480 nm) strongly stimulates ipRGC melanopsin receptors, acutely suppressing pineal melatonin secretion. Cease exposure to unshaded screens and bright overhead LED lighting at least 60 to 90 minutes prior to bedtime.</li>
        <li><strong>Adenosine &amp; Pharmacological Timing:</strong> Caffeine exhibits an average elimination half-life of 5 to 7 hours and a quarter-life of 10 to 12 hours. Consuming caffeine past 12:00 PM to 2:00 PM degrades Stage N3 slow-wave amplitude and reduces total restorative sleep time. Similarly, while ethanol (alcohol) acts as a GABAergic sedative that hastens sleep onset, its hepatic metabolism into acetaldehyde induces severe second-half sleep fragmentation and obliterates REM sleep architecture.</li>
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
            <li><a href="sleep-calculator.html">Sleep Cycle Calculator</a></li>
            <li><a href="tdee-calculator.html">TDEE Calculator</a></li>
            <li><a href="calorie-deficit-calculator.html">Calorie Deficit Calculator</a></li>
            <li><a href="max-heart-rate-calculator.html">Max Heart Rate Calculator</a></li>
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
        <p>&copy; 2026 CalcHub. Educational and clinical calculation tools. Consult a board-certified sleep specialist for chronic sleep disorders.</p>
      </div>
    </div>
  </footer>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const form = document.getElementById('sleep-form');
      const modeSelect = document.getElementById('calc-mode');
      const targetTimeGroup = document.getElementById('target-time-group');
      const hourSelect = document.getElementById('target-hour');
      const minSelect = document.getElementById('target-minute');
      const ampmSelect = document.getElementById('target-ampm');
      const latencySlider = document.getElementById('latency-mins');
      const latencyDisplay = document.getElementById('latency-display');
      const resultsContainer = document.getElementById('calculator-results');

      latencySlider.addEventListener('input', function() {
        latencyDisplay.textContent = latencySlider.value + ' minutes';
      });

      modeSelect.addEventListener('change', function() {
        if (modeSelect.value === 'now') {
          targetTimeGroup.style.display = 'none';
        } else {
          targetTimeGroup.style.display = 'flex';
        }
      });

      function formatTime(totalMinutes) {
        let normalized = ((totalMinutes % 1440) + 1440) % 1440;
        let hours = Math.floor(normalized / 60);
        let mins = normalized % 60;
        let ampm = hours >= 12 ? 'PM' : 'AM';
        let displayHours = hours % 12;
        if (displayHours === 0) displayHours = 12;
        let displayMins = mins < 10 ? '0' + mins : mins;
        return displayHours + ':' + displayMins + ' ' + ampm;
      }

      form.addEventListener('submit', function(e) {
        e.preventDefault();

        const mode = modeSelect.value;
        const latency = parseInt(latencySlider.value) || 15;
        let baseMinutes = 0;

        if (mode === 'now') {
          const now = new Date();
          baseMinutes = (now.getHours() * 60) + now.getMinutes();
        } else {
          let h = parseInt(hourSelect.value);
          let m = parseInt(minSelect.value);
          let ampm = ampmSelect.value;
          if (ampm === 'PM' && h < 12) h += 12;
          if (ampm === 'AM' && h === 12) h = 0;
          baseMinutes = (h * 60) + m;
        }

        let time6 = '', time5 = '', time4 = '', time3 = '';
        let headline = '';
        let cardPrefix = '';

        if (mode === 'wakeup') {
          // Working backwards from wake time to find bedtimes
          headline = 'Optimal Bedtimes to Wake Up at ' + formatTime(baseMinutes);
          cardPrefix = 'Bedtime: ';
          time6 = formatTime(baseMinutes - (6 * 90) - latency);
          time5 = formatTime(baseMinutes - (5 * 90) - latency);
          time4 = formatTime(baseMinutes - (4 * 90) - latency);
          time3 = formatTime(baseMinutes - (3 * 90) - latency);
        } else {
          // Working forwards from bedtime to find wake times
          headline = 'Optimal Wake Times if Sleeping at ' + formatTime(baseMinutes);
          cardPrefix = 'Wake Time: ';
          time6 = formatTime(baseMinutes + latency + (6 * 90));
          time5 = formatTime(baseMinutes + latency + (5 * 90));
          time4 = formatTime(baseMinutes + latency + (4 * 90));
          time3 = formatTime(baseMinutes + latency + (3 * 90));
        }

        document.getElementById('results-headline').textContent = headline;
        document.getElementById('res-time-6').textContent = time6;
        document.getElementById('res-time-5').textContent = time5;
        document.getElementById('res-time-4').textContent = time4;
        document.getElementById('res-time-3').textContent = time3;

        document.getElementById('res-architecture-text').textContent =
          'Five completed cycles (7.5 hours) represents the optimal restorative sweet spot for most adults, maximizing both slow-wave Stage N3 deep sleep (for cellular and glymphatic brain detox) and late-cycle REM sleep (for emotional regulation and cognitive synthesis). Factor in your ' + latency + '-minute sleep onset latency to fall asleep at the ideal circadian window.';

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
    protein_path = os.path.join(BASE_DIR, "protein-intake-calculator.html")
    with open(protein_path, "w", encoding="utf-8") as f:
        f.write(PROTEIN_INTAKE_HTML.strip() + "\n")
    print(f"Generated {os.path.basename(protein_path)}")

    sleep_path = os.path.join(BASE_DIR, "sleep-calculator.html")
    with open(sleep_path, "w", encoding="utf-8") as f:
        f.write(SLEEP_CALCULATOR_HTML.strip() + "\n")
    print(f"Generated {os.path.basename(sleep_path)}")

if __name__ == "__main__":
    main()
