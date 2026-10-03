"""
Batch 21 - Part 4: Health & Clinical Tools
7. carbohydrate-intake-calculator.html (Glycogen Resynthesis, ISSN Daily Endurance g/kg & Intra-Workout Fueling)
8. cholesterol-ratio-calculator.html (Castelli Risk Index I & II, Non-HDL & Triglyceride/HDL Insulin Resistance)
Word count target: >1,000 words in article-body each.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 7. carbohydrate-intake-calculator.html
# -------------------------------------------------------------
CARB_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Carbohydrate Intake Calculator | Athlete Glycogen & Fueling Sizer</title>
  <meta name="description" content="Calculate your daily carbohydrate requirements in grams and g/kg based on ACSM, ISSN, and IOC guidelines for endurance, team sports, keto, or bodybuilding.">
  <link rel="canonical" href="https://calchub.com/carbohydrate-intake-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Sports Carbohydrate Intake & Glycogen Calculator",
    "applicationCategory": "HealthApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0.00",
      "priceCurrency": "USD"
    },
    "description": "Calculates scientific daily carbohydrate requirements (grams and g/kg/day), intra-workout fueling rates, and glycogen loading targets based on ISSN and IOC sports nutrition consensus."
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "How many grams of carbohydrates per kilogram of body weight do athletes need daily?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "According to the American College of Sports Medicine (ACSM) and the International Olympic Committee (IOC): low-intensity skill sports require 3 to 5 g/kg/day; moderate training (1 hr/day) requires 5 to 7 g/kg/day; endurance training (1 to 3 hrs/day) requires 6 to 10 g/kg/day; and extreme endurance (> 4 hrs/day) requires 8 to 12 g/kg/day."
        }
      },
      {
        "@type": "Question",
        "name": "How much carbohydrate should endurance athletes consume during long workouts?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "For exercise lasting 1.0 to 2.5 hours, athletes should consume 30 to 60 grams of rapidly oxidizable carbohydrates per hour (glucose or maltodextrin). For ultra-endurance events exceeding 2.5 to 3 hours, up to 90 grams per hour is recommended using a 2:1 glucose-to-fructose ratio to utilize both SGLT1 and GLUT5 intestinal transporters."
        }
      },
      {
        "@type": "Question",
        "name": "How much glycogen can the human body store?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The human body stores approximately 400 to 500 grams of glycogen in skeletal muscle (providing ~1,600 to 2,000 kcal for localized muscular contraction) and approximately 80 to 100 grams in the liver (providing ~320 to 400 kcal to maintain systemic euglycemia during fasting and submaximal exercise)."
        }
      },
      {
        "@type": "Question",
        "name": "What is the carbohydrate protocol for endurance carb-loading?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Modern glycogen supercompensation protocols recommend consuming 10 to 12 grams of carbohydrate per kilogram of body weight per day for 36 to 48 hours prior to an endurance race lasting longer than 90 minutes, accompanied by a structured training taper."
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
        <div class="badge-tag">Sports Dietetics</div>
        <h1 class="calculator-title">Carbohydrate Intake &amp; Glycogen Sizer</h1>
        <p class="calculator-description">Calculate evidence-based daily carbohydrate requirements, pre-race glycogen loading protocols, and intra-workout fueling rates based on the ACSM/ISSN consensus.</p>
      </div>

      <div class="calculator-grid">
        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Athlete Profile &amp; Training Volume</h2>
          </div>
          <div class="calc-card-body">
            <div class="form-row" style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
              <div class="form-group">
                <label for="athlete-weight" class="form-label">Body Weight</label>
                <input type="number" id="athlete-weight" class="form-input" value="165" min="60" max="400" step="1" oninput="calculateCarbs()">
              </div>
              <div class="form-group">
                <label for="weight-unit" class="form-label">Unit</label>
                <select id="weight-unit" class="form-select" onchange="calculateCarbs()">
                  <option value="lbs" selected>Pounds (lbs)</option>
                  <option value="kg">Kilograms (kg)</option>
                </select>
              </div>
            </div>

            <div class="form-group">
              <label for="training-tier" class="form-label">Athletic Discipline &amp; Daily Training Load</label>
              <select id="training-tier" class="form-select" onchange="calculateCarbs()">
                <option value="sedentary">Sedentary / Weight Management (2 – 3 g/kg/day)</option>
                <option value="light">Light Training / Skill Sport (&lt; 1 hr/day: 3 – 5 g/kg/day)</option>
                <option value="moderate" selected>Moderate Training / Team Sports (~1 hr/day: 5 – 7 g/kg/day)</option>
                <option value="endurance">Endurance Training (1 – 3 hrs/day: 6 – 10 g/kg/day)</option>
                <option value="extreme">Extreme Endurance / Multi-Hour Tour (&gt; 4 hrs/day: 8 – 12 g/kg/day)</option>
                <option value="carbload">Pre-Event Glycogen Supercompensation (10 – 12 g/kg/day)</option>
                <option value="keto">Ketogenic / Very Low Carb (&lt; 50g total / &lt; 0.5 g/kg)</option>
              </select>
            </div>

            <div class="form-group">
              <label for="session-duration" class="form-label">Typical Session Duration (Minutes)</label>
              <input type="number" id="session-duration" class="form-input" value="90" min="15" max="360" step="15" oninput="calculateCarbs()">
              <span class="form-hint">Used to calculate intra-workout fueling recommendations</span>
            </div>

            <button type="button" class="btn btn-primary" onclick="calculateCarbs()">Calculate Carbohydrate Targets</button>
          </div>
        </div>

        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Daily Intake &amp; Fueling Matrix</h2>
          </div>
          <div class="calc-card-body">
            <div class="result-hero" style="background:#eff6ff;border-color:#bfdbfe;">
              <span class="hero-label">Target Daily Carbohydrate Intake</span>
              <div class="hero-value" id="res-target-carbs" style="color:#1d4ed8;font-size:2.4rem;">450 g / day</div>
              <span class="form-hint" id="res-target-calories">1,800 kcal from carbohydrates (6.0 g/kg body weight)</span>
            </div>

            <div class="results-grid" style="margin-top:1.5rem;">
              <div class="result-item">
                <span class="result-label">Recommended Range</span>
                <span class="result-value" id="res-carb-range">375 – 524 g</span>
              </div>
              <div class="result-item">
                <span class="result-label">Total Body Glycogen</span>
                <span class="result-value" id="res-glycogen-storage">~560 g (~2,240 kcal)</span>
              </div>
              <div class="result-item">
                <span class="result-label">Intra-Workout Fueling</span>
                <span class="result-value" id="res-intra-rate">30 – 60 g / hr</span>
              </div>
              <div class="result-item">
                <span class="result-label">Post-Workout Recovery</span>
                <span class="result-value" id="res-post-carb">75 – 90 g</span>
              </div>
            </div>

            <div class="stat-box" style="margin-top:1.5rem;padding:1rem;background:#f8fafc;border-radius:8px;border:1px solid #e2e8f0;">
              <h4 style="font-weight:700;margin-bottom:0.5rem;font-size:0.95rem;">Nutrient Timing &amp; Transporter Saturation:</h4>
              <p id="res-timing-note" style="font-size:0.875rem;color:#475569;margin:0;">
                For 90-minute sessions, consuming 30-60 g/hr of rapid-absorbing carbohydrates (dextrose, maltodextrin) prevents premature glycogen depletion and maintains central nervous system power output.
              </p>
            </div>
          </div>
        </div>
      </div>

      <article class="article-body">
        <h2>Biochemical Role of Carbohydrates in Athletic Performance</h2>
        <p>
          Carbohydrates are the primary, most metabolically efficient macronutrient substrate for fueling high-intensity muscular work. At exercise intensities exceeding 65% of maximal oxygen consumption ($VO_2\text{max}$), oxidative phosphorylation of free fatty acids cannot sustain the rapid turnover rate of muscular $ATP$ required by contracting myofibrils. In contrast, carbohydrate oxidation produces more energy per liter of consumed oxygen ($5.05\text{ kcal/L } O_2$) than lipid oxidation ($4.69\text{ kcal/L } O_2$), conferring an approximate <strong>7% to 11% bioenergetic efficiency advantage</strong> during demanding athletic competition.
        </p>
        <p>
          Carbohydrates are stored in the body in the form of <strong>glycogen</strong>, a branched polymer of glucose molecules organized around a central protein core called glycogenin:
        </p>
        <ul>
          <li><strong>Skeletal Muscle Glycogen (~400 to 500 grams):</strong> Muscle cells lack the enzyme glucose-6-phosphatase, trapping phosphorylated glucose within the myocyte. Muscle glycogen serves exclusively as a localized, intracellular energy supply to power muscle cross-bridge cycling.</li>
          <li><strong>Hepatic (Liver) Glycogen (~80 to 100 grams):</strong> The liver possesses active glucose-6-phosphatase, allowing it to cleave phosphate groups and liberate free glucose into systemic circulation. Hepatic glycogen maintains systemic blood glucose levels (preventing neuroglycopenic fatigue and central nervous system collapse) during overnight fasting and endurance exertion.</li>
        </ul>

        <h2>ACSM and ISSN Daily Carbohydrate Intake Guidelines</h2>
        <p>
          The joint consensus position stand from the American College of Sports Medicine (ACSM), the Academy of Nutrition and Dietetics (AND), and Dietitians of Canada establishes daily carbohydrate guidelines based on body mass ($g/kg/day$) rather than static percentages of total calories:
        </p>

        <div class="formula-box">
          <p><strong>Daily Carbohydrate Prescription Matrix:</strong></p>
          $$\text{Target Daily Carbs (grams)} = \text{Body Weight (kg)} \times \text{Prescribed Activity Factor (g/kg)}$$
          <ul>
            <li><strong>Low Intensity / Skill Sports:</strong> $3 \text{ to } 5\text{ g/kg/day}$ (Archery, golf, bowling, casual gym attendance).</li>
            <li><strong>Moderate Exercise (~1 hr/day):</strong> $5 \text{ to } 7\text{ g/kg/day}$ (Team sports, resistance training + moderate conditioning).</li>
            <li><strong>High-Volume Endurance (1 to 3 hrs/day):</strong> $6 \text{ to } 10\text{ g/kg/day}$ (Marathon, triathlon, road cycling, competitive rowing).</li>
            <li><strong>Extreme Endurance (> 4 to 5 hrs/day):</strong> $8 \text{ to } 12\text{ g/kg/day}$ (Ultra-marathons, multi-stage road races, Tour de France).</li>
            <li><strong>Carbo-Loading Supercompensation (36-48h pre-race):</strong> $10 \text{ to } 12\text{ g/kg/day}$.</li>
          </ul>
        </div>

        <h2>Intra-Workout Fueling and Intestinal Transporter Dynamics</h2>
        <p>
          During sustained exercise exceeding 60 minutes, endogenous glycogen stores progressively deplete. Ingesting exogenous carbohydrates during exercise preserves liver glycogen, attenuates the rise in catabolic cortisol, and maintains high rates of carbohydrate oxidation late into competition.
        </p>
        <p>
          The physiological ceiling for exogenous carbohydrate oxidation is dictated by the saturation kinetics of intestinal epithelial transport proteins:
        </p>
        <div class="formula-box">
          <p><strong>Intestinal Transporter Transport Saturation:</strong></p>
          <ul>
            <li><strong>Single Glucose / Maltodextrin Formulations (SGLT1 Transporter):</strong> Glucose is absorbed across the apical enterocyte membrane via sodium-glucose cotransporter 1 (SGLT1). SGLT1 saturates at approximately $1.0\text{ to }1.2\text{ grams of glucose per minute}$ ($60\text{ g/hour}$). Consuming more than 60 g/hr of pure glucose leads to unabsorbed solute pooling in the gut lumen, causing osmotic cramping and gastrointestinal distress.</li>
            <li><strong>Multiple Transportable Carbohydrates (2:1 Glucose:Fructose Ratio):</strong> Fructose is absorbed through an independent, non-sodium-dependent facilitated transporter: <strong>GLUT5</strong>. Combining glucose and fructose in a $2:1$ (or modern $1:0.8$) ratio activates both SGLT1 and GLUT5 pathways simultaneously. This elevates peak exogenous carbohydrate oxidation rates up to <strong>90 to 120 grams per hour</strong> (1.5 to 1.8 g/min), unlocking higher sustained wattage and delaying time to exhaustion.</li>
          </ul>
        </div>

        <h2>Comprehensive Sports Nutrition Reference Table</h2>
        <p>
          The reference table below displays daily intake targets, glycogen saturation metrics, and intra-workout fueling schedules across athletic disciplines:
        </p>

        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>Athletic Profile</th>
                <th>Prescribed g/kg/day</th>
                <th>Target (70 kg Athlete)</th>
                <th>Workout Duration</th>
                <th>Intra-Workout Target</th>
                <th>Primary Fuel Strategy</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Sedentary / Desk Worker</strong></td>
                <td>2.0 – 3.0 g/kg</td>
                <td>140 – 210 g</td>
                <td>&lt; 30 min</td>
                <td>None (water only)</td>
                <td>Low-glycemic complex carbohydrates, high dietary fiber.</td>
              </tr>
              <tr>
                <td><strong>Strength / Hypertrophy</strong></td>
                <td>4.0 – 6.0 g/kg</td>
                <td>280 – 420 g</td>
                <td>45 – 75 min</td>
                <td>Electrolytes or mouth rinse</td>
                <td>Pre-workout complex carbs, post-workout rapid starch + protein.</td>
              </tr>
              <tr>
                <td><strong>Team Sports (Soccer / Basketball)</strong></td>
                <td>5.0 – 7.0 g/kg</td>
                <td>350 – 490 g</td>
                <td>60 – 90 min</td>
                <td>30 – 45 g / hr</td>
                <td>Isotonic 6% carbohydrate-electrolyte sports beverage at half-time.</td>
              </tr>
              <tr>
                <td><strong>Marathon Runner (Daily)</strong></td>
                <td>7.0 – 9.0 g/kg</td>
                <td>490 – 630 g</td>
                <td>90 – 150 min</td>
                <td>30 – 60 g / hr</td>
                <td>Energy gels and chews with water every 20-30 minutes.</td>
              </tr>
              <tr>
                <td><strong>Ironman Triathlete (Daily)</strong></td>
                <td>8.0 – 10.0 g/kg</td>
                <td>560 – 700 g</td>
                <td>2 – 4 hours</td>
                <td>60 – 90 g / hr</td>
                <td>2:1 Glucose-to-fructose liquid drink mix + gels + rice bars.</td>
              </tr>
              <tr>
                <td><strong>Pre-Marathon Carbo-Load</strong></td>
                <td>10.0 – 12.0 g/kg</td>
                <td>700 – 840 g</td>
                <td>Rest / Taper</td>
                <td>N/A (Taper phase)</td>
                <td>Low-fiber, high-glycemic starches (white rice, pasta, bagels, fruit juice).</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2>Worked Sports Dietetics Case Study</h2>
        <div class="worked-example-card">
          <div class="example-header">
            <span class="example-badge">Endurance Fueling Case</span>
            <h3 class="example-title">Sub-3 Hour Marathon Fueling &amp; Carbo-Loading Strategy</h3>
          </div>
          <div class="example-step">
            <div class="step-num">1</div>
            <div class="step-content">
              <strong>Athlete Profile:</strong> A 28-year-old female marathon runner aiming for a 2:55 finish time. Body weight is 132 lbs (59.87 kg). She is currently 48 hours out from her target race. The sports nutritionist must calculate her 2-day pre-race carbo-loading targets and her race-day intra-workout fueling protocol.
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">2</div>
            <div class="step-content">
              <strong>Calculate Daily Carbo-Loading Target (10.0 g/kg/day):</strong>
              $$\text{Daily Carbs} = 59.87\text{ kg} \times 10.0\text{ g/kg} = \mathbf{598.7\text{ grams of carbohydrate/day}}$$
              $$\text{Caloric Contribution} = 598.7\text{ g} \times 4\text{ kcal/g} = \mathbf{2,395\text{ kcal from carbohydrates}}$$
              Dietary fiber is reduced to &lt; 15 g/day to avoid gastrointestinal fullness and prevent race-day bowel urgency.
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">3</div>
            <div class="step-content">
              <strong>Calculate Race Morning Pre-Event Meal (3.0 Hours Prior):</strong>
              Guidelines suggest 1 to 4 g/kg consumed 3 to 4 hours before race start:
              $$\text{Pre-Race Meal} = 59.87\text{ kg} \times 2.5\text{ g/kg} \approx \mathbf{150\text{ grams of carbohydrate}}$$
              (e.g., 2 plain white bagels with honey, 1 banana, and 12 oz isotonic sports drink).
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">4</div>
            <div class="step-content">
              <strong>Calculate Race-Day Intra-Workout Fueling (Target Finish: 175 Minutes):</strong>
              For a 2 hour 55 minute exertion, the target intake is 60 g/hr:
              $$\text{Total Exogenous Carbs} = 2.92\text{ hours} \times 60\text{ g/hr} = \mathbf{175\text{ grams total}}$$
              The athlete consumes one 25-gram dual-source maltodextrin/fructose hydrogel packet every 25 minutes with water, completely preventing the classic 20-mile "bonk" (glycogen depletion).
            </div>
          </div>
        </div>

        <h2>Post-Exercise Glycogen Resynthesis: The Biphasic Recovery Window</h2>
        <p>
          Following strenuous glycogen-depleting exercise, skeletal muscle resynthesizes glycogen through a biphasic regulatory process:
        </p>
        <ol>
          <li><strong>The Insulin-Independent Phase (First 30 to 60 Minutes):</strong> Vigorous muscular contractions stimulate calcium release and 5'-AMP-activated protein kinase (AMPK), inducing direct mechanical translocation of intracellular GLUT4 glucose transport vesicles to the sarcolemma without requiring circulating insulin. Coupled with maximal activation of the unphosphorylated form of <em>glycogen synthase</em>, glycogen storage rates reach an unprecedented 20 to 30 mmol/kg wet weight per hour if high-glycemic carbohydrates are delivered immediately.</li>
          <li><strong>The Insulin-Dependent Phase (Subsequent 2 to 24 Hours):</strong> As sarcolemmal GLUT4 abundance gradually wanes, continued glycogen replenishment becomes strictly dependent on postprandial insulin secretion. Ingesting <strong>1.0 to 1.2 grams of carbohydrate per kilogram of body weight per hour</strong> at 30-minute intervals for the first 4 hours post-workout maximizes total glycogen recovery. Combining 0.3 to 0.4 g/kg of high-leucine protein (such as whey isolate) with a slightly lower carbohydrate intake (0.8 g/kg) stimulates equivalent insulin secretion and glycogen accumulation while simultaneously initiating myofibrillar protein synthesis via mTORC1.</li>
        </ol>
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
    function calculateCarbs() {
      const weightVal = parseFloat(document.getElementById('athlete-weight').value) || 0;
      const unit = document.getElementById('weight-unit').value;
      const tier = document.getElementById('training-tier').value;
      const duration = parseFloat(document.getElementById('session-duration').value) || 0;

      if (weightVal <= 0) return;

      const weightKg = (unit === 'lbs') ? (weightVal * 0.45359237) : weightVal;

      let gpkgMid = 6.0;
      let gpkgLow = 5.0;
      let gpkgHigh = 7.0;

      if (tier === 'sedentary') {
        gpkgLow = 2.0; gpkgHigh = 3.0; gpkgMid = 2.5;
      } else if (tier === 'light') {
        gpkgLow = 3.0; gpkgHigh = 5.0; gpkgMid = 4.0;
      } else if (tier === 'moderate') {
        gpkgLow = 5.0; gpkgHigh = 7.0; gpkgMid = 6.0;
      } else if (tier === 'endurance') {
        gpkgLow = 6.0; gpkgHigh = 10.0; gpkgMid = 8.0;
      } else if (tier === 'extreme') {
        gpkgLow = 8.0; gpkgHigh = 12.0; gpkgMid = 10.0;
      } else if (tier === 'carbload') {
        gpkgLow = 10.0; gpkgHigh = 12.0; gpkgMid = 11.0;
      } else if (tier === 'keto') {
        gpkgLow = 0.3; gpkgHigh = 0.6; gpkgMid = 0.45;
      }

      let targetGrams = Math.round(weightKg * gpkgMid);
      let lowGrams = Math.round(weightKg * gpkgLow);
      let highGrams = Math.round(weightKg * gpkgHigh);

      if (tier === 'keto') {
        targetGrams = Math.min(targetGrams, 40);
        lowGrams = 20;
        highGrams = 50;
      }

      const targetCalories = targetGrams * 4;

      document.getElementById('res-target-carbs').innerText = targetGrams.toLocaleString() + ' g / day';
      document.getElementById('res-target-calories').innerText = `${targetCalories.toLocaleString()} kcal from carbohydrates (${gpkgMid.toFixed(1)} g/kg)`;
      document.getElementById('res-carb-range').innerText = `${lowGrams} – ${highGrams} g`;

      // Storage estimate: ~15g per kg total body weight capacity
      const totalStorageG = Math.round(weightKg * 7.5);
      const totalStorageKcal = totalStorageG * 4;
      document.getElementById('res-glycogen-storage').innerText = `~${totalStorageG} g (~${totalStorageKcal} kcal)`;

      // Intra workout
      let intraText = 'None (water)';
      let postCarbLow = Math.round(weightKg * 1.0);
      let postCarbHigh = Math.round(weightKg * 1.2);

      if (duration < 45) {
        intraText = 'None needed';
      } else if (duration <= 75) {
        intraText = 'Mouth rinse / 15–30 g';
      } else if (duration <= 150) {
        intraText = '30 – 60 g / hr';
      } else {
        intraText = '60 – 90 g / hr (2:1 mix)';
      }

      document.getElementById('res-intra-rate').innerText = intraText;
      document.getElementById('res-post-carb').innerText = `${postCarbLow} – ${postCarbHigh} g`;

      // Note
      const noteEl = document.getElementById('res-timing-note');
      if (tier === 'carbload') {
        noteEl.innerHTML = `<strong>Glycogen Supercompensation:</strong> Maintain 10-12 g/kg for 36-48 hours pre-race. Favor low-fiber, high-glycemic starches (white rice, pasta, bagels, sports drink) to maximize muscle glycogen by 20-40% without bowel discomfort.`;
      } else if (tier === 'keto') {
        noteEl.innerHTML = `<strong>Ketogenic Adaptation:</strong> Restricting carbohydrates below 50 g/day forces hepatic ketogenesis (beta-hydroxybutyrate synthesis). Physical output at intensities > 75% VO2max will be impaired due to diminished pyruvate dehydrogenase flux.`;
      } else if (duration > 120) {
        noteEl.innerHTML = `For sessions lasting > 2 hours, target 60-90 g/hr using a dual-source glucose:fructose formulation. This utilizes both SGLT1 and GLUT5 transporters, boosting exogenous oxidation by 50% over glucose alone.`;
      } else {
        noteEl.innerHTML = `Consume ${postCarbLow}-${postCarbHigh} g of fast-digesting carbohydrates with 25-35 g of high-leucine protein within 45 minutes post-exercise to accelerate glycogen synthase resynthesis.`;
      }
    }

    document.addEventListener('DOMContentLoaded', calculateCarbs);
  </script>
</body>
</html>
"""

# -------------------------------------------------------------
# 8. cholesterol-ratio-calculator.html
# -------------------------------------------------------------
CHOLESTEROL_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cholesterol Ratio Calculator | Castelli Risk Index & Atherogenic Ratios</title>
  <meta name="description" content="Calculate your Castelli Risk Index I (TC/HDL), Castelli Risk Index II (LDL/HDL), Triglyceride/HDL ratio, and Non-HDL cholesterol to assess cardiovascular risk.">
  <link rel="canonical" href="https://calchub.com/cholesterol-ratio-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Clinical Cholesterol Ratio & Castelli Risk Calculator",
    "applicationCategory": "HealthApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0.00",
      "priceCurrency": "USD"
    },
    "description": "Calculates clinical atherogenic cholesterol ratios including Castelli Risk Index I & II, Non-HDL Cholesterol, and Triglyceride-to-HDL ratio for insulin resistance."
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is the Castelli Risk Index I and why is it important?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Castelli Risk Index I (CRI-I) is the ratio of Total Cholesterol to HDL Cholesterol (TC / HDL). Derived from the landmark Framingham Heart Study by Dr. William Castelli, it reflects the balance between all circulating cholesterol particles and protective reverse-cholesterol-transport HDL particles. An ideal ratio is below 3.5 for men and below 4.4 for women, with ratios exceeding 5.0 indicating substantially elevated coronary heart disease risk."
        }
      },
      {
        "@type": "Question",
        "name": "Why is the Triglyceride-to-HDL ratio considered a marker for insulin resistance?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Triglyceride-to-HDL ratio (TG / HDL) is a validated surrogate marker for insulin resistance, metabolic syndrome, and the presence of small, dense LDL particles (Phenotype B). A ratio below 2.0 (in mg/dL units) indicates normal insulin sensitivity and buoyant, less atherogenic LDL, whereas a ratio above 3.0 or 3.5 strongly correlates with hyperinsulinemia, hepatic steatosis, and cardiovascular disease."
        }
      },
      {
        "@type": "Question",
        "name": "What is Non-HDL cholesterol and why is it superior to LDL alone?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Non-HDL Cholesterol is calculated simply as Total Cholesterol minus HDL (Non-HDL = TC - HDL). It accounts for all circulating atherogenic, Apolipoprotein B (ApoB)-containing lipoproteins—including LDL, VLDL, IDL, and Lipoprotein(a). Clinical guidelines (AHA/ACC and NLA) emphasize Non-HDL as a secondary target of therapy because it accurately predicts cardiovascular risk even in individuals with hypertriglyceridemia."
        }
      },
      {
        "@type": "Question",
        "name": "How does the Friedewald formula estimate LDL cholesterol?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The standard Friedewald formula is: LDL = Total Cholesterol - HDL - (Triglycerides / 5) in mg/dL (or TG / 2.2 in mmol/L). The term (TG / 5) estimates very-low-density lipoprotein (VLDL) cholesterol. It is valid only when fasting triglycerides are below 400 mg/dL (4.52 mmol/L)."
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
        <div class="badge-tag">Cardiovascular Lipidology</div>
        <h1 class="calculator-title">Cholesterol Ratio &amp; Atherogenic Risk Calculator</h1>
        <p class="calculator-description">Calculate your Castelli Risk Index I (TC/HDL), Castelli Risk Index II (LDL/HDL), Triglyceride/HDL ratio, and Non-HDL cholesterol based on the Framingham Heart Study.</p>
      </div>

      <div class="calculator-grid">
        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Standard Fasting Lipid Panel</h2>
          </div>
          <div class="calc-card-body">
            <div class="form-group">
              <label for="lipid-unit" class="form-label">Laboratory Reporting Unit</label>
              <select id="lipid-unit" class="form-select" onchange="toggleLipidUnits()">
                <option value="mgdl" selected>US Standard (mg/dL)</option>
                <option value="mmoll">International SI (mmol/L)</option>
              </select>
            </div>

            <div class="form-row" style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
              <div class="form-group">
                <label for="tc-val" class="form-label">Total Cholesterol (TC)</label>
                <input type="number" id="tc-val" class="form-input" value="210" min="50" max="600" step="1" oninput="calculateLipids()">
              </div>
              <div class="form-group">
                <label for="hdl-val" class="form-label">HDL "Good" Cholesterol</label>
                <input type="number" id="hdl-val" class="form-input" value="50" min="10" max="150" step="1" oninput="calculateLipids()">
              </div>
            </div>

            <div class="form-row" style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
              <div class="form-group">
                <label for="ldl-val" class="form-label">LDL "Bad" Cholesterol</label>
                <input type="number" id="ldl-val" class="form-input" value="130" min="20" max="400" step="1" oninput="calculateLipids()">
              </div>
              <div class="form-group">
                <label for="tg-val" class="form-label">Triglycerides (TG)</label>
                <input type="number" id="tg-val" class="form-input" value="150" min="20" max="1500" step="1" oninput="calculateLipids()">
              </div>
            </div>

            <button type="button" class="btn btn-primary" onclick="calculateLipids()">Analyze Atherogenic Risk</button>
          </div>
        </div>

        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Atherogenic Ratios &amp; Risk Profiling</h2>
          </div>
          <div class="calc-card-body">
            <div class="result-hero" id="ratio-hero" style="background:#fefce8;border-color:#fef08a;">
              <span class="hero-label">Castelli Risk Index I (TC / HDL)</span>
              <div class="hero-value" id="res-castelli-1" style="color:#ca8a04;font-size:2.4rem;">4.20</div>
              <span class="form-hint" id="res-castelli-1-status" style="font-weight:600;">Average Coronary Risk (Ideal &lt; 3.5 Men, &lt; 4.4 Women)</span>
            </div>

            <div class="results-grid" style="margin-top:1.5rem;">
              <div class="result-item">
                <span class="result-label">Castelli Index II (LDL/HDL)</span>
                <span class="result-value" id="res-castelli-2">2.60</span>
              </div>
              <div class="result-item">
                <span class="result-label">TG / HDL Ratio</span>
                <span class="result-value" id="res-tg-hdl">3.00</span>
              </div>
              <div class="result-item">
                <span class="result-label">Non-HDL Cholesterol</span>
                <span class="result-value" id="res-non-hdl">160 mg/dL</span>
              </div>
              <div class="result-item">
                <span class="result-label">Friedewald Est. LDL</span>
                <span class="result-value" id="res-friedewald">130 mg/dL</span>
              </div>
            </div>

            <div class="stat-box" style="margin-top:1.5rem;padding:1rem;background:#f8fafc;border-radius:8px;border:1px solid #e2e8f0;">
              <h4 style="font-weight:700;margin-bottom:0.5rem;font-size:0.95rem;">Metabolic Health &amp; Atherogenicity Summary:</h4>
              <p id="res-lipid-summary" style="font-size:0.875rem;color:#475569;margin:0;">
                TG/HDL ratio of 3.0 borders the threshold for insulin resistance and elevated small, dense LDL particle distribution. Non-HDL is above the recommended optimal threshold (130 mg/dL).
              </p>
            </div>
          </div>
        </div>
      </div>

      <article class="article-body">
        <h2>Lipidology Beyond Total Cholesterol: The Power of Ratios</h2>
        <p>
          For over four decades, clinical cardiology relied almost exclusively on Total Cholesterol ($TC$) as the primary screening biomarker for atherosclerotic cardiovascular disease ($ASCVD$). However, multiple clinical investigations—including the seminal <strong>Framingham Heart Study</strong>—revealed a profound paradox: more than 50% of individuals suffering acute myocardial infarctions possessed "normal" total cholesterol levels (&lt; 200 mg/dL).
        </p>
        <p>
          Total cholesterol reflects the sum total of sterol content across all circulating lipoproteins. However, different lipoprotein classes perform fundamentally opposing physiological functions:
        </p>
        <ul>
          <li><strong>Atherogenic Particles (ApoB family):</strong> Low-Density Lipoproteins ($LDL$), Very-Low-Density Lipoproteins ($VLDL$), and Intermediate-Density Lipoproteins ($IDL$) carry cholesterol into arterial walls. When trapped in the subendothelial space of coronary arteries, they undergo oxidative modification, triggering macrophage phagocytosis, foam cell formation, and progressive atheromatous plaque accumulation.</li>
          <li><strong>Anti-Atherogenic Particles (ApoA-I family):</strong> High-Density Lipoproteins ($HDL$) mediate <em>reverse cholesterol transport</em>, extracting excess cholesterol from peripheral arterial tissues and transporting it back to the liver for biliary excretion. Furthermore, HDL particles exert potent anti-inflammatory, anti-thrombotic, and antioxidant effects on the vascular endothelium.</li>
        </ul>
        <p>
          Consequently, the <strong>ratio</strong> between atherogenic particles and protective HDL provides far superior prognostic power for predicting ischemic coronary events than total cholesterol alone.
        </p>

        <h2>Mathematical Definitions of the Core Lipid Ratios</h2>

        <div class="formula-box">
          <p><strong>1. Castelli Risk Index I (TC / HDL Ratio):</strong></p>
          $$CRI\text{-}I = \frac{\text{Total Cholesterol}}{\text{HDL Cholesterol}}$$
          <p>
            Formulated by Dr. William P. Castelli (former director of the Framingham Study), this ratio measures the overall balance between cholesterol entering tissues versus cholesterol being cleared.
          </p>
          <ul>
            <li><strong>Optimal / Low Risk:</strong> &lt; 3.5 in men; &lt; 3.0 in women.</li>
            <li><strong>Average Risk:</strong> 3.5 to 5.0.</li>
            <li><strong>High Atherogenic Risk:</strong> &gt; 5.0 (associated with a doubling of 10-year myocardial infarction risk).</li>
          </ul>
        </div>

        <div class="formula-box">
          <p><strong>2. Castelli Risk Index II (LDL / HDL Ratio):</strong></p>
          $$CRI\text{-}II = \frac{\text{LDL Cholesterol}}{\text{HDL Cholesterol}}$$
          <p>
            Focuses strictly on the direct ratio of primary atherogenic carriers to protective reverse transport carriers:
          </p>
          <ul>
            <li><strong>Ideal Risk:</strong> &lt; 2.0.</li>
            <li><strong>Normal Risk:</strong> 2.0 to 3.2.</li>
            <li><strong>Elevated Risk:</strong> &gt; 3.5.</li>
          </ul>
        </div>

        <div class="formula-box">
          <p><strong>3. Triglyceride to HDL Ratio (TG / HDL) - The Insulin Resistance Marker:</strong></p>
          $$\text{Ratio (mg/dL)} = \frac{\text{Triglycerides}}{\text{HDL}}\quad \Bigg|\quad \text{Ratio (mmol/L)} = \frac{\text{Triglycerides (mmol/L)}}{\text{HDL (mmol/L)}} \times 0.437$$
          <p>
            The TG/HDL ratio is a validated surrogate biomarker for <strong>Atherogenic Dyslipidemia</strong>, hepatic insulin resistance, and the presence of <em>small, dense LDL particles (sdLDL / Phenotype B)</em>. Small dense LDL particles are particularly dangerous because they easily penetrate damaged arterial endothelium, resist hepatic LDL-receptor binding, and are highly prone to oxidation.
          </p>
          <ul>
            <li><strong>Ideal / High Insulin Sensitivity:</strong> &lt; 1.5 (&lt; 0.65 in mmol/L).</li>
            <li><strong>Normal:</strong> 1.5 to 2.5 (0.65 to 1.10 in mmol/L).</li>
            <li><strong>High / Insulin Resistance &amp; Small Dense LDL:</strong> &gt; 3.0 (&gt; 1.30 in mmol/L).</li>
          </ul>
        </div>

        <div class="formula-box">
          <p><strong>4. Non-HDL Cholesterol:</strong></p>
          $$\text{Non-HDL} = \text{Total Cholesterol} - \text{HDL Cholesterol}$$
          <p>
            Non-HDL encapsulates the full atherogenic burden ($LDL + VLDL + IDL + Lp(a)$). The American Heart Association (AHA) and National Lipid Association (NLA) designate Non-HDL as a secondary target of therapy:
          </p>
          <ul>
            <li><strong>Optimal:</strong> &lt; 100 mg/dL (&lt; 2.6 mmol/L).</li>
            <li><strong>Desirable:</strong> &lt; 130 mg/dL (&lt; 3.4 mmol/L).</li>
            <li><strong>High Risk:</strong> &ge; 160 mg/dL (&ge; 4.1 mmol/L).</li>
          </ul>
        </div>

        <h2>Comprehensive Cardiovascular Risk Stratification Table</h2>
        <p>
          The table below demonstrates risk categories across all primary ratios in both US standard (mg/dL) and International System (mmol/L) units:
        </p>

        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>Risk Category</th>
                <th>Castelli I (TC/HDL)</th>
                <th>Castelli II (LDL/HDL)</th>
                <th>TG / HDL Ratio (mg/dL)</th>
                <th>Non-HDL (mg/dL)</th>
                <th>Non-HDL (mmol/L)</th>
                <th>Clinical Interpretation</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Optimal / Low Risk</strong></td>
                <td>&lt; 3.5 (Men)<br>&lt; 3.0 (Women)</td>
                <td>&lt; 2.0</td>
                <td>&lt; 1.5</td>
                <td>&lt; 100</td>
                <td>&lt; 2.6</td>
                <td>Minimal atherogenic plaque progression; high insulin sensitivity; large buoyant LDL.</td>
              </tr>
              <tr>
                <td><strong>Moderate / Desirable</strong></td>
                <td>3.5 – 4.5</td>
                <td>2.0 – 3.0</td>
                <td>1.5 – 2.5</td>
                <td>100 – 129</td>
                <td>2.6 – 3.3</td>
                <td>Average population risk; balanced reverse cholesterol transport.</td>
              </tr>
              <tr>
                <td><strong>Borderline High</strong></td>
                <td>4.6 – 5.0</td>
                <td>3.1 – 3.5</td>
                <td>2.6 – 3.2</td>
                <td>130 – 159</td>
                <td>3.4 – 4.1</td>
                <td>Early endothelial dysfunction; lifestyle intervention (dietary fiber, aerobic training) indicated.</td>
              </tr>
              <tr>
                <td><strong>High Risk</strong></td>
                <td>5.1 – 6.0</td>
                <td>3.6 – 4.5</td>
                <td>3.3 – 4.0</td>
                <td>160 – 189</td>
                <td>4.1 – 4.9</td>
                <td>Substantial excess cardiovascular risk; small dense LDL phenotype; consider statin therapy.</td>
              </tr>
              <tr>
                <td><strong>Very High Risk</strong></td>
                <td>&gt; 6.0</td>
                <td>&gt; 4.5</td>
                <td>&gt; 4.0</td>
                <td>&ge; 190</td>
                <td>&ge; 4.9</td>
                <td>Accelerated coronary atherogenesis; metabolic syndrome; aggressive lipid-lowering required.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2>Worked Clinical Cardiology Case Study</h2>
        <div class="worked-example-card">
          <div class="example-header">
            <span class="example-badge">Preventive Cardiology Case</span>
            <h3 class="example-title">Unmasking Hidden Atherogenic Risk in "Normal" Cholesterol</h3>
          </div>
          <div class="example-step">
            <div class="step-num">1</div>
            <div class="step-content">
              <strong>Patient Clinical Data:</strong> A 49-year-old male presents for an executive annual physical. Routine fasting lipid panel reports: Total Cholesterol = 195 mg/dL (frequently mischaracterized as "normal" because it is &lt; 200 mg/dL), HDL = 32 mg/dL, LDL = 125 mg/dL, and Triglycerides = 190 mg/dL. The physician calculates full atherogenic ratios.
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">2</div>
            <div class="step-content">
              <strong>Calculate Castelli Risk Index I (TC / HDL):</strong>
              $$CRI\text{-}I = \frac{195\text{ mg/dL}}{32\text{ mg/dL}} = \mathbf{6.09}$$
              <strong>Clinical Finding:</strong> Despite a "normal" total cholesterol of 195, his Castelli I index of 6.09 is severely elevated (High Risk &gt; 5.0), placing him in the highest quintile of coronary risk.
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">3</div>
            <div class="step-content">
              <strong>Calculate TG / HDL Ratio and Castelli Index II:</strong>
              $$\text{TG / HDL} = \frac{190\text{ mg/dL}}{32\text{ mg/dL}} = \mathbf{5.94}$$
              $$CRI\text{-}II = \frac{125\text{ mg/dL}}{32\text{ mg/dL}} = \mathbf{3.91}$$
              <strong>Clinical Finding:</strong> A TG/HDL ratio of 5.94 strongly confirms atherogenic dyslipidemia, profound hepatic insulin resistance, and a predominance of small dense LDL particles.
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">4</div>
            <div class="step-content">
              <strong>Calculate Non-HDL Cholesterol and Therapy Plan:</strong>
              $$\text{Non-HDL} = 195 - 32 = \mathbf{163\text{ mg/dL}}$$
              Non-HDL is significantly elevated (&ge; 160 mg/dL). Clinical management focuses on aggressive carbohydrate reduction (cutting refined starches and added sugars to lower triglycerides and raise HDL), daily cardiovascular exercise, and moderate-intensity statin therapy to lower ApoB particle count.
            </div>
          </div>
        </div>

        <h2>Advanced Lipidology: Apolipoprotein B and Particle Discordance</h2>
        <p>
          While standard lipid panels report the <em>mass</em> of cholesterol carried within lipoproteins (e.g., mg of LDL cholesterol per deciliter of plasma), atherosclerotic plaque initiation is governed by the <strong>absolute number of circulating atherogenic particles</strong>. Each atherogenic particle—whether an LDL, VLDL, IDL, or Lipoprotein(a)—carries exactly one molecule of <strong>Apolipoprotein B (ApoB-100)</strong> on its outer phospholipid shell.
        </p>
        <p>
          In patients with metabolic syndrome, visceral obesity, or type 2 diabetes, a dangerous clinical phenomenon termed <strong>LDL Particle Discordance</strong> frequently occurs:
        </p>
        <ul>
          <li><strong>Concordant Profile:</strong> Normal LDL-C accompanied by normal ApoB particle number (low cardiovascular risk).</li>
          <li><strong>Discordant High-Risk Profile:</strong> "Normal" LDL-C (e.g., 95 mg/dL) paired with a severely elevated ApoB particle count (> 110 mg/dL). This occurs because high circulating triglycerides stimulate cholesterol ester transfer protein (CETP) to exchange triglycerides into LDL in return for cholesterol esters. Hepatic lipase then hydrolyzes these triglyceride-enriched particles, creating millions of small, cholesterol-depleted, dense LDL particles. Even though each particle carries less total cholesterol mass, the total particle count is massive, and cardiovascular risk tracks strictly with particle number (ApoB), not cholesterol mass.</li>
        </ul>
        <p>
          When advanced NMR lipoprofile or ApoB immunoassay testing is unavailable, the combination of an elevated <strong>Castelli Risk Index I (> 4.5)</strong> and a high <strong>TG/HDL ratio (> 3.0)</strong> serves as a virtually cost-free, highly sensitive clinical surrogate identifying patients with discordant, highly atherogenic small dense LDL profiles requiring aggressive lifestyle and pharmacologic intervention.
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
    function toggleLipidUnits() {
      const unit = document.getElementById('lipid-unit').value;
      const tc = document.getElementById('tc-val');
      const hdl = document.getElementById('hdl-val');
      const ldl = document.getElementById('ldl-val');
      const tg = document.getElementById('tg-val');

      if (unit === 'mgdl') {
        tc.value = '210';
        hdl.value = '50';
        ldl.value = '130';
        tg.value = '150';
        tc.step = '1';
        hdl.step = '1';
        ldl.step = '1';
        tg.step = '1';
      } else {
        tc.value = '5.43';
        hdl.value = '1.29';
        ldl.value = '3.36';
        tg.value = '1.70';
        tc.step = '0.01';
        hdl.step = '0.01';
        ldl.step = '0.01';
        tg.step = '0.01';
      }
      calculateLipids();
    }

    function calculateLipids() {
      const unit = document.getElementById('lipid-unit').value;
      let tc = parseFloat(document.getElementById('tc-val').value) || 0;
      let hdl = parseFloat(document.getElementById('hdl-val').value) || 0;
      let ldl = parseFloat(document.getElementById('ldl-val').value) || 0;
      let tg = parseFloat(document.getElementById('tg-val').value) || 0;

      if (tc <= 0 || hdl <= 0) return;

      // In mmol/L: convert to mg/dL for standardized ratio calculations
      let tc_mg = (unit === 'mgdl') ? tc : tc * 38.67;
      let hdl_mg = (unit === 'mgdl') ? hdl : hdl * 38.67;
      let ldl_mg = (unit === 'mgdl') ? ldl : ldl * 38.67;
      let tg_mg = (unit === 'mgdl') ? tg : tg * 88.57;

      const cri1 = tc_mg / hdl_mg;
      const cri2 = (ldl_mg > 0) ? (ldl_mg / hdl_mg) : (tc_mg - hdl_mg - (tg_mg / 5)) / hdl_mg;
      const tg_hdl = tg_mg / hdl_mg;
      const non_hdl_mg = tc_mg - hdl_mg;
      const non_hdl_val = (unit === 'mgdl') ? Math.round(non_hdl_mg) : (tc - hdl).toFixed(2);
      const unitSuffix = (unit === 'mgdl') ? ' mg/dL' : ' mmol/L';

      // Friedewald estimated LDL
      let friedewald = (unit === 'mgdl') ? (tc - hdl - (tg / 5)) : (tc - hdl - (tg / 2.2));

      document.getElementById('res-castelli-1').innerText = cri1.toFixed(2);
      document.getElementById('res-castelli-2').innerText = cri2.toFixed(2);
      document.getElementById('res-tg-hdl').innerText = tg_hdl.toFixed(2);
      document.getElementById('res-non-hdl').innerText = non_hdl_val + unitSuffix;
      document.getElementById('res-friedewald').innerText = ((friedewald > 0 && tg_mg < 400) ? ((unit === 'mgdl' ? Math.round(friedewald) : friedewald.toFixed(2)) + unitSuffix) : 'N/A (TG > 400)');

      // Hero styling
      const hero = document.getElementById('ratio-hero');
      const valEl = document.getElementById('res-castelli-1');
      const statusEl = document.getElementById('res-castelli-1-status');
      const summaryEl = document.getElementById('res-lipid-summary');

      if (cri1 < 3.5) {
        hero.style.background = '#f0fdf4';
        hero.style.borderColor = '#bbf7d0';
        valEl.style.color = '#15803d';
        statusEl.innerText = 'Optimal / Low Coronary Risk (< 3.5)';
        summaryEl.innerText = 'Excellent cholesterol balance. Strong protective reverse cholesterol transport and minimal systemic atherogenic lipoprotein burden.';
      } else if (cri1 <= 5.0) {
        hero.style.background = '#fefce8';
        hero.style.borderColor = '#fef08a';
        valEl.style.color = '#ca8a04';
        statusEl.innerText = 'Average Cardiovascular Risk (3.5 – 5.0)';
        summaryEl.innerText = `Castelli index of ${cri1.toFixed(2)} represents standard adult risk. TG/HDL ratio is ${tg_hdl.toFixed(2)} (${tg_hdl > 3.0 ? 'Elevated insulin resistance signal' : 'Normal metabolic profile'}).`;
      } else {
        hero.style.background = '#fef2f2';
        hero.style.borderColor = '#fecaca';
        valEl.style.color = '#b91c1c';
        statusEl.innerText = 'High Atherogenic Risk (> 5.0)';
        summaryEl.innerText = `Elevated Castelli index (${cri1.toFixed(2)}) indicates substantial excess coronary risk. Non-HDL burden is elevated. Clinical evaluation and lifestyle/statin optimization recommended.`;
      }
    }

    document.addEventListener('DOMContentLoaded', calculateLipids);
  </script>
</body>
</html>
"""

def generate_part4():
    with open(os.path.join(BASE_DIR, "carbohydrate-intake-calculator.html"), "w", encoding="utf-8") as f:
        f.write(CARB_HTML)
    print("Generated carbohydrate-intake-calculator.html")

    with open(os.path.join(BASE_DIR, "cholesterol-ratio-calculator.html"), "w", encoding="utf-8") as f:
        f.write(CHOLESTEROL_HTML)
    print("Generated cholesterol-ratio-calculator.html")

if __name__ == "__main__":
    generate_part4()
