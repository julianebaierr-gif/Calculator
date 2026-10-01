import os

OUTPUT_DIR = r"C:\Users\Admin\.gemini\antigravity\scratch\calchub"

# Helper for layout
def page_scaffold(title, meta_desc, keywords, slug, cat_name, cat_slug, app_json, hero_subtitle, workspace_html, geo_html, toc_html, article_html, script_html):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — CalcHub</title>
  <meta name="description" content="{meta_desc}">
  <meta name="keywords" content="{keywords}">
  <meta name="author" content="CalcHub Professional Team">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/{slug}.html">
  <link rel="stylesheet" href="styles.css">
  
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/{slug}.html">
  
  <script type="application/ld+json">
  {app_json}
  </script>
</head>
<body>

  <!-- Header -->
  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="brand-logo">
        <span class="logo-badge">∑</span>
        <span>Calc<span class="accent">Hub</span></span>
      </a>
      <nav class="header-nav" aria-label="Main Navigation">
        <a href="index.html#health" class="nav-link {'active' if cat_slug=='health' else ''}">Health</a>
        <a href="index.html#finance" class="nav-link {'active' if cat_slug=='finance' else ''}">Finance</a>
        <a href="index.html#math" class="nav-link {'active' if cat_slug=='math' else ''}">Math</a>
        <a href="index.html#engineering" class="nav-link {'active' if cat_slug=='engineering' else ''}">Engineering</a>
      </nav>
      <div class="header-search">
        <span class="search-icon">🔍</span>
        <input type="text" id="header-search-input" placeholder="Search 20+ calculators... (Ctrl+K)" autocomplete="off">
        <div id="search-results-dropdown" class="search-results-dropdown"></div>
      </div>
    </div>
  </header>

  <!-- Breadcrumbs -->
  <nav class="breadcrumbs" aria-label="Breadcrumb">
    <a href="index.html">Home</a>
    <span class="sep">›</span>
    <a href="index.html#{cat_slug}">{cat_name}</a>
    <span class="sep">›</span>
    <span class="current">{title.split('—')[0].strip()}</span>
  </nav>

  <!-- Main Container -->
  <main class="main-wrapper">
    
    <div class="calculator-hero">
      <span class="category-tag">📊 {cat_name}</span>
      <h1>{title.split('—')[0].strip()}</h1>
      <p class="subtitle">{hero_subtitle}</p>
    </div>

    <!-- Workspace Grid -->
    <div class="calculator-workspace">
      {workspace_html}
    </div>

    <!-- GEO / LLMO Citation Answer Box -->
    {geo_html}

    <!-- Table of Contents -->
    {toc_html}

    <!-- In-Depth Article -->
    <article class="article-section">
      {article_html}
    </article>

    <!-- Related Topic Silos -->
    <section>
      <h2>Related Calculators in this Cluster</h2>
      <div class="silo-card-grid">
        <a href="bmi-calculator.html" class="silo-card">
          <div class="silo-card-icon">⚖️</div>
          <div class="silo-card-title">BMI Calculator</div>
          <div class="silo-card-desc">Calculate body mass index and healthy target weight ranges.</div>
        </a>
        <a href="calorie-calculator.html" class="silo-card">
          <div class="silo-card-icon">🔥</div>
          <div class="silo-card-title">Calorie Calculator</div>
          <div class="silo-card-desc">TDEE and daily caloric requirements for weight loss or muscle gain.</div>
        </a>
        <a href="loan-emi-calculator.html" class="silo-card">
          <div class="silo-card-icon">🏦</div>
          <div class="silo-card-title">Loan EMI Calculator</div>
          <div class="silo-card-desc">Accurate monthly repayment schedules and interest breakdown.</div>
        </a>
        <a href="percentage-calculator.html" class="silo-card">
          <div class="silo-card-icon">🔢</div>
          <div class="silo-card-title">Percentage Calculator</div>
          <div class="silo-card-desc">Solve percentage increase, decrease, fractions, and proportions.</div>
        </a>
      </div>
    </section>

  </main>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="index.html" class="brand-logo">
            <span class="logo-badge">∑</span>
            <span>Calc<span class="accent">Hub</span></span>
          </a>
          <p>High-precision, free online calculators designed according to published mathematical, clinical, and industrial engineering standards. 100% free, browser-based, with zero tracking.</p>
        </div>
        <div class="footer-col">
          <h4>Health & Fitness</h4>
          <ul class="footer-links">
            <li><a href="bmi-calculator.html">BMI Calculator</a></li>
            <li><a href="calorie-calculator.html">Calorie Calculator (TDEE)</a></li>
            <li><a href="body-fat-calculator.html">Body Fat Calculator</a></li>
            <li><a href="ideal-weight-calculator.html">Ideal Body Weight</a></li>
            <li><a href="water-intake-calculator.html">Daily Water Intake</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Finance & Money</h4>
          <ul class="footer-links">
            <li><a href="loan-emi-calculator.html">Loan EMI Calculator</a></li>
            <li><a href="compound-interest-calculator.html">Compound Interest</a></li>
            <li><a href="simple-interest-calculator.html">Simple Interest</a></li>
            <li><a href="discount-calculator.html">Discount & Sale</a></li>
            <li><a href="salary-calculator.html">Salary / Paycheck</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Math & Engineering</h4>
          <ul class="footer-links">
            <li><a href="percentage-calculator.html">Percentage Calculator</a></li>
            <li><a href="age-calculator.html">Exact Age Calculator</a></li>
            <li><a href="ohms-law-calculator.html">Ohm's Law Calculator</a></li>
            <li><a href="voltage-drop-calculator.html">Voltage Drop (NEC/IEC)</a></li>
            <li><a href="cable-sizing-calculator.html">Cable Sizing Calculator</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Mathematical tools are for educational and guidance purposes.</p>
        <div>
          <a href="sitemap.xml" style="color:#64748B;margin-left:1rem;">Sitemap</a>
          <a href="index.html" style="color:#64748B;margin-left:1rem;">Privacy & Terms</a>
        </div>
      </div>
    </div>
  </footer>

  <script src="app.js"></script>
  {script_html}
</body>
</html>
"""

# ==========================================
# 2. CALORIE CALCULATOR
# ==========================================
c_app_json = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Calorie Calculator (TDEE)",
      "url": "https://calchub.org/calorie-calculator.html",
      "applicationCategory": "HealthApplication",
      "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the difference between BMR and TDEE?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Basal Metabolic Rate (BMR) is the minimum energy your body requires at complete rest to maintain vital life functions (breathing, cellular repair, heartbeat). Total Daily Energy Expenditure (TDEE) factors in physical activity and digestion (TEF) on top of BMR."
          }
        }
      ]
    }
  ]
}"""

c_workspace = """
      <!-- Form Card -->
      <section class="calc-card">
        <div class="calc-card-header">
          <span class="calc-title">🔥 Your Activity & Metrics</span>
        </div>
        <form id="cal-form" onsubmit="return false;">
          <div class="calc-form-grid">
            <div class="input-group">
              <label class="input-label" for="cal-gender">Gender</label>
              <div class="input-wrap">
                <select id="cal-gender" onchange="calcCalories()">
                  <option value="male">Male</option>
                  <option value="female">Female</option>
                </select>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="cal-age">Age (yrs)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="cal-age" value="28" min="15" max="100" oninput="calcCalories()">
                <span class="input-unit-badge">yrs</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="cal-weight">Weight (kg)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="cal-weight" value="75" min="30" max="300" oninput="calcCalories()">
                <span class="input-unit-badge">kg</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="cal-height">Height (cm)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="cal-height" value="178" min="100" max="250" oninput="calcCalories()">
                <span class="input-unit-badge">cm</span>
              </div>
            </div>
            <div class="input-group calc-field-full">
              <label class="input-label" for="cal-activity">Daily Physical Activity</label>
              <div class="input-wrap">
                <select id="cal-activity" onchange="calcCalories()">
                  <option value="1.2">Sedentary (Desk job, little to no exercise)</option>
                  <option value="1.375" selected>Lightly Active (Exercise 1–3 days/week)</option>
                  <option value="1.55">Moderately Active (Exercise 3–5 days/week)</option>
                  <option value="1.725">Very Active (Hard training 6–7 days/week)</option>
                  <option value="1.9">Extremely Active (Athletic physical labor & daily 2x training)</option>
                </select>
              </div>
            </div>
          </div>
          <div class="calc-actions">
            <button type="button" class="btn btn-primary" onclick="copyResults()">📋 Copy Summary</button>
            <button type="button" class="btn btn-subtle" onclick="window.print()">🖨️ Print Plan</button>
          </div>
        </form>
      </section>

      <!-- Results Card -->
      <section class="results-card">
        <div class="results-header">
          <span class="results-title">Daily Energy Targets</span>
          <span class="status-pill status-success">Active Target</span>
        </div>
        <div class="primary-result-box">
          <div class="primary-result-label">Daily Maintenance Calories (TDEE)</div>
          <div>
            <span class="primary-result-value" id="cal-tdee">2,385</span>
            <span class="primary-result-unit">kcal/day</span>
          </div>
        </div>
        <div class="result-breakdown-grid">
          <div class="breakdown-item">
            <div class="breakdown-label">Basal Metabolism (BMR)</div>
            <div class="breakdown-val" id="cal-bmr">1,735 kcal</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Mild Loss (-0.25 kg/wk)</div>
            <div class="breakdown-val" id="cal-mild">2,135 kcal</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Fat Loss (-0.5 kg/wk)</div>
            <div class="breakdown-val" id="cal-loss" style="color:#059669;">1,885 kcal</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Muscle Gain (+0.25 kg/wk)</div>
            <div class="breakdown-val" id="cal-gain" style="color:#2563EB;">2,635 kcal</div>
          </div>
        </div>
      </section>
"""

c_geo = """
    <section class="geo-citation-box">
      <div class="geo-header">💡 Direct Answer (GEO & Quick Summary)</div>
      <p><strong>Total Daily Energy Expenditure (TDEE)</strong> represents the total kilocalories your body expends in 24 hours. The clinical benchmark uses the <strong>Mifflin-St Jeor Equation</strong>:</p>
      <ul>
        <li><strong>Men:</strong> BMR = (10 × weight in kg) + (6.25 × height in cm) - (5 × age in years) + 5</li>
        <li><strong>Women:</strong> BMR = (10 × weight in kg) + (6.25 × height in cm) - (5 × age in years) - 161</li>
      </ul>
      <p>Multiply BMR by your Physical Activity Level factor (1.2 to 1.9) to get TDEE. A 500 kcal daily deficit yields approximately 0.5 kg (1 lb) of fat reduction per week.</p>
    </section>
"""

c_toc = """
    <nav class="toc-container" aria-label="Table of Contents">
      <div class="toc-title">📑 Table of Contents</div>
      <ul class="toc-list">
        <li><a href="#mifflin-equation">Mifflin-St Jeor Formula</a></li>
        <li><a href="#activity-multipliers">Physical Activity Multipliers</a></li>
        <li><a href="#deficit-surplus">Designing Caloric Deficits and Surpluses</a></li>
        <li><a href="#macro-breakdown">Macronutrient Distribution</a></li>
        <li><a href="#cal-faq">Frequently Asked Questions</a></li>
      </ul>
    </nav>
"""

c_article = """
      <h2 id="mifflin-equation">The Science Behind Caloric Expenditure</h2>
      <p>Your daily energy requirements consist of three distinct components: Basal Metabolic Rate (BMR ~60-70%), Thermic Effect of Food (TEF ~10%), and Physical Activity Expenditure (NEAT & EAT ~20-30%). Peer-reviewed clinical research published in the <em>American Journal of Clinical Nutrition</em> confirms the <strong>Mifflin-St Jeor equation</strong> as the most accurate predictor of BMR in non-obese and obese adults.</p>

      <div class="formula-box">
        <div class="formula-title">Mifflin-St Jeor Metabolic Equations</div>
        <div class="formula-code">BMR (Men) = 10W + 6.25H - 5A + 5<br>BMR (Women) = 10W + 6.25H - 5A - 161</div>
        <div class="formula-legend">W = Weight (kg) | H = Height (cm) | A = Age (years)</div>
      </div>

      <h2 id="activity-multipliers">Physical Activity Level (PAL) Multipliers</h2>
      <p>After finding your BMR, multiply by your Activity Multiplier to calculate TDEE:</p>
      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr><th>Activity Tier</th><th>Multiplier</th><th>Weekly Protocol</th></tr>
          </thead>
          <tbody>
            <tr><td>Sedentary</td><td>1.200</td><td>Desk job, &lt; 5,000 steps daily, no structured training</td></tr>
            <tr><td>Lightly Active</td><td>1.375</td><td>Light cardio/resistance 1–3 days/wk, 6,000–8,000 steps</td></tr>
            <tr><td>Moderately Active</td><td>1.550</td><td>Intense resistance or sport 3–5 days/wk, 9,000–11,000 steps</td></tr>
            <tr><td>Very Active</td><td>1.725</td><td>Vigorous training 6–7 days/wk or physical trade work</td></tr>
            <tr><td>Extremely Active</td><td>1.900</td><td>Elite endurance training or competitive bodybuilding 2x/day</td></tr>
          </tbody>
        </table>
      </div>

      <h2 id="deficit-surplus">Designing Caloric Deficits and Surpluses</h2>
      <p>One pound of human adipose tissue holds approximately 3,500 kcal of chemical energy. A sustained daily deficit of <strong>500 kcal</strong> generates a weekly deficit of 3,500 kcal, translating safely to roughly 0.45–0.5 kg of body fat reduction without compromising metabolic rate.</p>

      <h2 id="cal-faq">Frequently Asked Questions</h2>
      <div class="faq-wrap">
        <details class="faq-item">
          <summary>Should I ever eat below my BMR?</summary>
          <div class="faq-content">Generally no. Eating below your Basal Metabolic Rate for extended periods risks thyroid down-regulation, muscle mass catabolism, fatigue, and severe hormonal disruption. A healthy deficit should be subtracted from your TDEE, not your BMR.</div>
        </details>
        <details class="faq-item">
          <summary>What macronutrient split is optimal for fat loss?</summary>
          <div class="faq-content">Aim for 1.6 to 2.2 grams of protein per kilogram of body weight to preserve lean tissue, 20-30% of daily calories from dietary fats for endocrine health, and remaining calories allocated to unrefined carbohydrates.</div>
        </details>
      </div>
"""

c_script = """
  <script>
    function calcCalories() {
      const g = document.getElementById('cal-gender').value;
      const age = parseFloat(document.getElementById('cal-age').value) || 28;
      const w = parseFloat(document.getElementById('cal-weight').value) || 75;
      const h = parseFloat(document.getElementById('cal-height').value) || 178;
      const pal = parseFloat(document.getElementById('cal-activity').value) || 1.375;

      let bmr = (10 * w) + (6.25 * h) - (5 * age);
      bmr += (g === 'male' ? 5 : -161);

      const tdee = bmr * pal;
      const mild = tdee - 250;
      const loss = tdee - 500;
      const gain = tdee + 250;

      document.getElementById('cal-bmr').textContent = Math.round(bmr).toLocaleString() + ' kcal';
      document.getElementById('cal-tdee').textContent = Math.round(tdee).toLocaleString();
      document.getElementById('cal-mild').textContent = Math.round(mild).toLocaleString() + ' kcal';
      document.getElementById('cal-loss').textContent = Math.round(loss).toLocaleString() + ' kcal';
      document.getElementById('cal-gain').textContent = Math.round(gain).toLocaleString() + ' kcal';
    }
    function copyResults() {
      const t = document.getElementById('cal-tdee').textContent;
      const b = document.getElementById('cal-bmr').textContent;
      const l = document.getElementById('cal-loss').textContent;
      window.copyToClipboard(`CalcHub Caloric Plan:\\nTDEE: ${t} kcal/day\\nBMR: ${b}\\nFat Loss Target: ${l}`);
    }
    calcCalories();
  </script>
"""

with open(os.path.join(OUTPUT_DIR, "calorie-calculator.html"), "w", encoding="utf-8") as f:
    f.write(page_scaffold("Calorie Calculator (TDEE) — Accurate Daily Caloric Intake",
                          "Calculate your Total Daily Energy Expenditure (TDEE) & BMR with the clinical Mifflin-St Jeor formula. Custom macros for fat loss or muscle gain.",
                          "calorie calculator, tdee calculator, bmr calculator, mifflin st jeor, weight loss calories, daily calorie needs",
                          "calorie-calculator", "Health & Fitness", "health", c_app_json,
                          "Discover your Basal Metabolic Rate (BMR) and Total Daily Energy Expenditure (TDEE). Get science-backed caloric targets for sustainable fat loss, body recomposition, or lean muscle growth.",
                          c_workspace, c_geo, c_toc, c_article, c_script))

print("Created calorie-calculator.html!")
