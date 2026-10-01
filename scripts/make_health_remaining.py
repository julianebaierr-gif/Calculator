import os

OUTPUT_DIR = r"C:\Users\Admin\.gemini\antigravity\scratch\calchub"

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

  <nav class="breadcrumbs" aria-label="Breadcrumb">
    <a href="index.html">Home</a>
    <span class="sep">›</span>
    <a href="index.html#{cat_slug}">{cat_name}</a>
    <span class="sep">›</span>
    <span class="current">{title.split('—')[0].strip()}</span>
  </nav>

  <main class="main-wrapper">
    <div class="calculator-hero">
      <span class="category-tag">📊 {cat_name}</span>
      <h1>{title.split('—')[0].strip()}</h1>
      <p class="subtitle">{hero_subtitle}</p>
    </div>

    <div class="calculator-workspace">
      {workspace_html}
    </div>

    {geo_html}
    {toc_html}

    <article class="article-section">
      {article_html}
    </article>

    <section>
      <h2>Related Health & Fitness Calculators</h2>
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
        <a href="body-fat-calculator.html" class="silo-card">
          <div class="silo-card-icon">📏</div>
          <div class="silo-card-title">Body Fat Calculator</div>
          <div class="silo-card-desc">Estimate body fat percentage and lean mass using the US Navy tape measurement method.</div>
        </a>
        <a href="water-intake-calculator.html" class="silo-card">
          <div class="silo-card-icon">💧</div>
          <div class="silo-card-title">Daily Water Intake</div>
          <div class="silo-card-desc">Determine optimal daily hydration based on body weight, climate, and exercise volume.</div>
        </a>
      </div>
    </section>
  </main>

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
</html>"""

# ==========================================
# 3. BODY FAT CALCULATOR
# ==========================================
bf_app_json = """{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Body Fat Calculator",
  "url": "https://calchub.org/body-fat-calculator.html",
  "applicationCategory": "HealthApplication",
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
}"""

bf_workspace = """
      <section class="calc-card">
        <div class="calc-card-header">
          <span class="calc-title">📏 Body Circumferences (US Navy Method)</span>
        </div>
        <form onsubmit="return false;">
          <div class="calc-form-grid">
            <div class="input-group">
              <label class="input-label" for="bf-gender">Gender</label>
              <div class="input-wrap">
                <select id="bf-gender" onchange="toggleHipField(); calcBF();">
                  <option value="male">Male</option>
                  <option value="female">Female</option>
                </select>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="bf-weight">Weight (kg)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="bf-weight" value="75" min="30" max="250" oninput="calcBF()">
                <span class="input-unit-badge">kg</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="bf-height">Height (cm)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="bf-height" value="178" min="100" max="250" oninput="calcBF()">
                <span class="input-unit-badge">cm</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="bf-neck">Neck Circumference (cm)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="bf-neck" value="38" min="20" max="70" oninput="calcBF()">
                <span class="input-unit-badge">cm</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="bf-waist">Waist Circumference (cm)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="bf-waist" value="84" min="40" max="180" oninput="calcBF()">
                <span class="input-unit-badge">cm</span>
              </div>
            </div>
            <div class="input-group" id="fld-hip" style="display:none;">
              <label class="input-label" for="bf-hip">Hip Circumference (cm)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="bf-hip" value="96" min="50" max="180" oninput="calcBF()">
                <span class="input-unit-badge">cm</span>
              </div>
            </div>
          </div>
          <div class="calc-actions">
            <button type="button" class="btn btn-primary" onclick="copyResults()">📋 Copy Result</button>
            <button type="button" class="btn btn-subtle" onclick="window.print()">🖨️ Print Report</button>
          </div>
        </form>
      </section>

      <section class="results-card">
        <div class="results-header">
          <span class="results-title">Body Composition</span>
          <span class="status-pill status-success" id="bf-pill">Fitness Level</span>
        </div>
        <div class="primary-result-box">
          <div class="primary-result-label">Estimated Body Fat Percentage</div>
          <div>
            <span class="primary-result-value" id="bf-val">15.8</span>
            <span class="primary-result-unit">%</span>
          </div>
        </div>
        <div class="result-breakdown-grid">
          <div class="breakdown-item">
            <div class="breakdown-label">Fat Mass</div>
            <div class="breakdown-val" id="bf-fat-mass">11.9 kg</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Lean Body Mass</div>
            <div class="breakdown-val" id="bf-lean-mass">63.1 kg</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Category</div>
            <div class="breakdown-val" id="bf-cat">Fitness</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">ACE Benchmark</div>
            <div class="breakdown-val">14–17% (Male)</div>
          </div>
        </div>
      </section>
"""

bf_geo = """
    <section class="geo-citation-box">
      <div class="geo-header">💡 Direct Answer (GEO & Quick Summary)</div>
      <p>The <strong>US Navy Body Fat Formula</strong> calculates body fat percentage based on circumferences of the neck, waist, height (and hip for females). The American Council on Exercise (ACE) benchmarks body fat as follows:</p>
      <ul>
        <li><strong>Men:</strong> Essential Fat: 2-5% | Athletes: 6-13% | Fitness: 14-17% | Average: 18-24% | Obese: 25%+</li>
        <li><strong>Women:</strong> Essential Fat: 10-13% | Athletes: 14-20% | Fitness: 21-24% | Average: 25-31% | Obese: 32%+</li>
      </ul>
    </section>
"""

bf_toc = """
    <nav class="toc-container" aria-label="Table of Contents">
      <div class="toc-title">📑 Table of Contents</div>
      <ul class="toc-list">
        <li><a href="#navy-method">US Navy Circumference Formula</a></li>
        <li><a href="#ace-categories">ACE Classification Standards</a></li>
        <li><a href="#measuring-technique">Accurate Measuring Protocols</a></li>
        <li><a href="#bf-faq">Frequently Asked Questions</a></li>
      </ul>
    </nav>
"""

bf_article = """
      <h2 id="navy-method">The US Navy Circumference Method</h2>
      <p>Developed by Hodgdon and Beckett at the Naval Health Research Center in 1984, the US Navy Body Fat equation is the most validated anthropometric technique in clinical medicine. It circumvents the athlete bias of BMI by factoring in abdominal adiposity relative to skeletal frame.</p>

      <div class="formula-box">
        <div class="formula-title">US Navy Equations (Metric)</div>
        <div class="formula-code">Men: %Fat = 495 / (1.0324 - 0.19077·log₁₀(waist - neck) + 0.15456·log₁₀(height)) - 450<br>Women: %Fat = 495 / (1.29579 - 0.35004·log₁₀(waist + hip - neck) + 0.22100·log₁₀(height)) - 450</div>
        <div class="formula-legend">All circumferences entered in centimeters (cm)</div>
      </div>

      <h2 id="ace-categories">ACE Body Fat Classification Standards</h2>
      <div class="table-responsive">
        <table class="data-table">
          <thead><tr><th>Classification</th><th>Women (% Fat)</th><th>Men (% Fat)</th></tr></thead>
          <tbody>
            <tr><td>Essential Fat</td><td>10–13%</td><td>2–5%</td></tr>
            <tr><td>Athletes</td><td>14–20%</td><td>6–13%</td></tr>
            <tr><td>Fitness</td><td>21–24%</td><td>14–17%</td></tr>
            <tr><td>Acceptable (Average)</td><td>25–31%</td><td>18–24%</td></tr>
            <tr><td>Obese</td><td>32%+</td><td>25%+</td></tr>
          </tbody>
        </table>
      </div>

      <h2 id="measuring-technique">Accurate Measuring Protocols</h2>
      <p>Measure circumferences using an inelastic tape measure snug against skin without compressing soft tissue:</p>
      <ul>
        <li><strong>Neck:</strong> Measure just below the larynx (Adam's apple), perpendicular to the neck axis.</li>
        <li><strong>Waist:</strong> Measure horizontally at the level of the navel for men, or at the narrowest point of the torso for women.</li>
        <li><strong>Hips (Women only):</strong> Measure around the widest circumference of the buttocks.</li>
      </ul>

      <h2 id="bf-faq">Frequently Asked Questions</h2>
      <div class="faq-wrap">
        <details class="faq-item">
          <summary>How accurate is the US Navy method compared to a DEXA scan?</summary>
          <div class="faq-content">When measurements are taken properly, the US Navy method correlates with Dual-Energy X-ray Absorptiometry (DEXA) within an error margin of 3-4%. It is significantly more reliable than standard home bioelectrical impedance (BIA) bathroom scales, which vary wildly with hydration levels.</div>
        </details>
      </div>
"""

bf_script = """
  <script>
    function toggleHipField() {
      const g = document.getElementById('bf-gender').value;
      document.getElementById('fld-hip').style.display = (g === 'female') ? 'block' : 'none';
    }
    function calcBF() {
      const g = document.getElementById('bf-gender').value;
      const w = parseFloat(document.getElementById('bf-weight').value) || 75;
      const h = parseFloat(document.getElementById('bf-height').value) || 178;
      const neck = parseFloat(document.getElementById('bf-neck').value) || 38;
      const waist = parseFloat(document.getElementById('bf-waist').value) || 84;
      const hip = parseFloat(document.getElementById('bf-hip').value) || 96;

      let bf = 0;
      if (g === 'male') {
        const diff = waist - neck;
        if (diff <= 0) return;
        bf = 495 / (1.0324 - 0.19077 * Math.log10(diff) + 0.15456 * Math.log10(h)) - 450;
      } else {
        const sum = waist + hip - neck;
        if (sum <= 0) return;
        bf = 495 / (1.29579 - 0.35004 * Math.log10(sum) + 0.22100 * Math.log10(h)) - 450;
      }

      bf = Math.max(3, Math.min(60, bf));
      const fatMass = w * (bf / 100);
      const leanMass = w - fatMass;

      let cat = "Fitness";
      let pillClass = "status-success";
      if (g === 'male') {
        if (bf < 6) cat = "Essential Fat";
        else if (bf < 14) cat = "Athletes";
        else if (bf < 18) cat = "Fitness";
        else if (bf < 25) { cat = "Average"; pillClass = "status-warning"; }
        else { cat = "Obese"; pillClass = "status-danger"; }
      } else {
        if (bf < 14) cat = "Essential Fat";
        else if (bf < 21) cat = "Athletes";
        else if (bf < 25) cat = "Fitness";
        else if (bf < 32) { cat = "Average"; pillClass = "status-warning"; }
        else { cat = "Obese"; pillClass = "status-danger"; }
      }

      document.getElementById('bf-val').textContent = bf.toFixed(1);
      document.getElementById('bf-fat-mass').textContent = fatMass.toFixed(1) + ' kg';
      document.getElementById('bf-lean-mass').textContent = leanMass.toFixed(1) + ' kg';
      document.getElementById('bf-cat').textContent = cat;
      const pill = document.getElementById('bf-pill');
      pill.className = 'status-pill ' + pillClass;
      pill.textContent = cat;
    }
    function copyResults() {
      const bf = document.getElementById('bf-val').textContent;
      const cat = document.getElementById('bf-cat').textContent;
      window.copyToClipboard(`CalcHub Body Fat Report: ${bf}% (${cat})`);
    }
    calcBF();
  </script>
"""

with open(os.path.join(OUTPUT_DIR, "body-fat-calculator.html"), "w", encoding="utf-8") as f:
    f.write(page_scaffold("Body Fat Calculator — US Navy Circumference Method",
                          "Accurate body fat percentage calculator using the clinical US Navy tape measurement method. Computes fat mass, lean body mass, and fitness benchmarks.",
                          "body fat calculator, navy body fat formula, lean body mass, body fat percentage, fat mass calculator",
                          "body-fat-calculator", "Health & Fitness", "health", bf_app_json,
                          "Measure your body composition without expensive DEXA scans. Calculate your precise body fat percentage, lean tissue mass, and athletic classification.",
                          bf_workspace, bf_geo, bf_toc, bf_article, bf_script))

# ==========================================
# 4. IDEAL BODY WEIGHT CALCULATOR
# ==========================================
ibw_app_json = """{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Ideal Body Weight Calculator",
  "url": "https://calchub.org/ideal-weight-calculator.html",
  "applicationCategory": "HealthApplication",
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
}"""

ibw_workspace = """
      <section class="calc-card">
        <div class="calc-card-header">
          <span class="calc-title">❤️ Your Stature & Gender</span>
        </div>
        <form onsubmit="return false;">
          <div class="calc-form-grid">
            <div class="input-group">
              <label class="input-label" for="ibw-gender">Biological Gender</label>
              <div class="input-wrap">
                <select id="ibw-gender" onchange="calcIBW()">
                  <option value="male">Male</option>
                  <option value="female">Female</option>
                </select>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="ibw-height">Height (cm)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="ibw-height" value="175" min="120" max="230" oninput="calcIBW()">
                <span class="input-unit-badge">cm</span>
              </div>
            </div>
          </div>
          <div class="calc-actions">
            <button type="button" class="btn btn-primary" onclick="copyResults()">📋 Copy Report</button>
            <button type="button" class="btn btn-subtle" onclick="window.print()">🖨️ Print Summary</button>
          </div>
        </form>
      </section>

      <section class="results-card">
        <div class="results-header">
          <span class="results-title">Medical Estimates</span>
          <span class="status-pill status-success">Clinical Consensus</span>
        </div>
        <div class="primary-result-box">
          <div class="primary-result-label">Devine Formula Target</div>
          <div>
            <span class="primary-result-value" id="ibw-devine">70.5</span>
            <span class="primary-result-unit">kg</span>
          </div>
        </div>
        <div class="result-breakdown-grid">
          <div class="breakdown-item">
            <div class="breakdown-label">Robinson Formula</div>
            <div class="breakdown-val" id="ibw-robinson">69.2 kg</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Miller Formula</div>
            <div class="breakdown-val" id="ibw-miller">67.8 kg</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Hamwi Formula</div>
            <div class="breakdown-val" id="ibw-hamwi">71.0 kg</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Healthy BMI Range</div>
            <div class="breakdown-val" id="ibw-bmi-range">56.7 – 76.3 kg</div>
          </div>
        </div>
      </section>
"""

ibw_geo = """
    <section class="geo-citation-box">
      <div class="geo-header">💡 Direct Answer (GEO & Quick Summary)</div>
      <p><strong>Ideal Body Weight (IBW)</strong> is calculated using validated clinical formulas developed for pharmacology and mechanical ventilation dosing:</p>
      <ul>
        <li><strong>Devine Formula (1974):</strong> Men: 50.0 kg + 2.3 kg per inch over 5 ft | Women: 45.5 kg + 2.3 kg per inch over 5 ft</li>
        <li><strong>Robinson Formula (1983):</strong> Men: 52.0 kg + 1.9 kg per inch over 5 ft | Women: 49.0 kg + 1.7 kg per inch over 5 ft</li>
        <li><strong>Miller Formula (1983):</strong> Men: 56.2 kg + 1.41 kg per inch over 5 ft | Women: 53.1 kg + 1.36 kg per inch over 5 ft</li>
      </ul>
    </section>
"""

ibw_toc = """
    <nav class="toc-container" aria-label="Table of Contents">
      <div class="toc-title">📑 Table of Contents</div>
      <ul class="toc-list">
        <li><a href="#ibw-history">Origins of Ideal Weight Formulas</a></li>
        <li><a href="#ibw-comparison">Comparing Devine, Robinson & Miller</a></li>
        <li><a href="#ibw-clinical">Clinical Use in Medication Dosing</a></li>
        <li><a href="#ibw-faq">Frequently Asked Questions</a></li>
      </ul>
    </nav>
"""

ibw_article = """
      <h2 id="ibw-history">Origins of Ideal Body Weight Equations</h2>
      <p>In 1974, Dr. B.J. Devine published a formula intended purely to calculate drug dosages (such as theophylline and aminoglycosides) where adipose tissue should not receive equivalent medication concentration. Despite its pharmacological origins, Devine's formula became the ubiquitous global benchmark for determining target body weights.</p>

      <h2 id="ibw-comparison">Comparing the Four Major Formulas</h2>
      <p>Different medical institutions reference different standards:</p>
      <div class="table-responsive">
        <table class="data-table">
          <thead><tr><th>Formula</th><th>Male Equation (over 5ft)</th><th>Female Equation (over 5ft)</th><th>Primary Context</th></tr></thead>
          <tbody>
            <tr><td><strong>Devine (1974)</strong></td><td>50 kg + 2.3 kg / inch</td><td>45.5 kg + 2.3 kg / inch</td><td>Standard hospital pharmacology</td></tr>
            <tr><td><strong>Robinson (1983)</strong></td><td>52 kg + 1.9 kg / inch</td><td>49.0 kg + 1.7 kg / inch</td><td>General population update</td></tr>
            <tr><td><strong>Miller (1983)</strong></td><td>56.2 kg + 1.41 kg / inch</td><td>53.1 kg + 1.36 kg / inch</td><td>Lean mass preservation</td></tr>
            <tr><td><strong>Hamwi (1964)</strong></td><td>48 kg + 2.7 kg / inch</td><td>45.5 kg + 2.2 kg / inch</td><td>Diabetic dietary guidance</td></tr>
          </tbody>
        </table>
      </div>

      <h2 id="ibw-clinical">Clinical Importance in Healthcare</h2>
      <p>In critical care settings, mechanical ventilators deliver tidal volume based strictly on predicted Ideal Body Weight (typically 6-8 mL/kg of IBW) rather than actual weight. This prevents acute lung injury and ventilator-induced barotrauma in patients suffering from ARDS.</p>

      <h2 id="ibw-faq">Frequently Asked Questions</h2>
      <div class="faq-wrap">
        <details class="faq-item">
          <summary>Why do the formulas differ slightly?</summary>
          <div class="faq-content">Each researcher analyzed distinct cohort studies. Robinson and Miller attempted to modernize Devine's earlier 1974 model based on empirical mortality tables from the Metropolitan Life Insurance studies.</div>
        </details>
      </div>
"""

ibw_script = """
  <script>
    function calcIBW() {
      const g = document.getElementById('ibw-gender').value;
      const hCm = parseFloat(document.getElementById('ibw-height').value) || 175;
      const hInches = hCm / 2.54;
      const inchesOver5ft = Math.max(0, hInches - 60);

      let devine = (g === 'male') ? 50.0 + (2.3 * inchesOver5ft) : 45.5 + (2.3 * inchesOver5ft);
      let robinson = (g === 'male') ? 52.0 + (1.9 * inchesOver5ft) : 49.0 + (1.7 * inchesOver5ft);
      let miller = (g === 'male') ? 56.2 + (1.41 * inchesOver5ft) : 53.1 + (1.36 * inchesOver5ft);
      let hamwi = (g === 'male') ? 48.0 + (2.7 * inchesOver5ft) : 45.5 + (2.2 * inchesOver5ft);

      const hM = hCm / 100;
      const minBmiKg = 18.5 * (hM * hM);
      const maxBmiKg = 24.9 * (hM * hM);

      document.getElementById('ibw-devine').textContent = devine.toFixed(1);
      document.getElementById('ibw-robinson').textContent = robinson.toFixed(1) + ' kg';
      document.getElementById('ibw-miller').textContent = miller.toFixed(1) + ' kg';
      document.getElementById('ibw-hamwi').textContent = hamwi.toFixed(1) + ' kg';
      document.getElementById('ibw-bmi-range').textContent = `${minBmiKg.toFixed(1)} – ${maxBmiKg.toFixed(1)} kg`;
    }
    function copyResults() {
      const d = document.getElementById('ibw-devine').textContent;
      window.copyToClipboard(`CalcHub Ideal Body Weight (Devine): ${d} kg`);
    }
    calcIBW();
  </script>
"""

with open(os.path.join(OUTPUT_DIR, "ideal-weight-calculator.html"), "w", encoding="utf-8") as f:
    f.write(page_scaffold("Ideal Body Weight Calculator — Devine, Robinson & Miller",
                          "Calculate your ideal weight using clinical equations: Devine, Robinson, Miller, and Hamwi formulas. Includes healthy WHO BMI target ranges.",
                          "ideal body weight calculator, devine formula, robinson formula, ideal weight for height, healthy weight range",
                          "ideal-weight-calculator", "Health & Fitness", "health", ibw_app_json,
                          "Discover your clinical ideal body weight benchmark. Compare authoritative equations used by physicians and critical care specialists worldwide.",
                          ibw_workspace, ibw_geo, ibw_toc, ibw_article, ibw_script))

# ==========================================
# 5. WATER INTAKE CALCULATOR
# ==========================================
w_app_json = """{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Daily Water Intake Calculator",
  "url": "https://calchub.org/water-intake-calculator.html",
  "applicationCategory": "HealthApplication",
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
}"""

w_workspace = """
      <section class="calc-card">
        <div class="calc-card-header">
          <span class="calc-title">💧 Your Weight & Hydration Factors</span>
        </div>
        <form onsubmit="return false;">
          <div class="calc-form-grid">
            <div class="input-group">
              <label class="input-label" for="w-weight">Body Weight (kg)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="w-weight" value="70" min="25" max="250" oninput="calcWater()">
                <span class="input-unit-badge">kg</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="w-exercise">Daily Exercise Duration</label>
              <div class="input-wrap has-unit">
                <input type="number" id="w-exercise" value="45" min="0" max="300" step="15" oninput="calcWater()">
                <span class="input-unit-badge">min</span>
              </div>
            </div>
            <div class="input-group calc-field-full">
              <label class="input-label" for="w-climate">Local Climate / Temperature</label>
              <div class="input-wrap">
                <select id="w-climate" onchange="calcWater()">
                  <option value="1.0">Temperate / Normal Indoor (20–24°C)</option>
                  <option value="1.15" selected>Warm / Humid Climate (25–32°C)</option>
                  <option value="1.3">Hot / Arid Desert Conditions (&gt; 33°C)</option>
                </select>
              </div>
            </div>
          </div>
          <div class="calc-actions">
            <button type="button" class="btn btn-primary" onclick="copyResults()">📋 Copy Hydration Goal</button>
            <button type="button" class="btn btn-subtle" onclick="window.print()">🖨️ Print Plan</button>
          </div>
        </form>
      </section>

      <section class="results-card">
        <div class="results-header">
          <span class="results-title">Daily Hydration Target</span>
          <span class="status-pill status-success">Optimal Fluid Goal</span>
        </div>
        <div class="primary-result-box">
          <div class="primary-result-label">Recommended Water Intake</div>
          <div>
            <span class="primary-result-value" id="w-liters">2.8</span>
            <span class="primary-result-unit">Liters/day</span>
          </div>
        </div>
        <div class="result-breakdown-grid">
          <div class="breakdown-item">
            <div class="breakdown-label">Standard Glasses (8 oz)</div>
            <div class="breakdown-val" id="w-glasses">11.8 glasses</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Fluid Ounces</div>
            <div class="breakdown-val" id="w-ounces">94.7 fl oz</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Baseline Need</div>
            <div class="breakdown-val" id="w-baseline">2.3 L</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Exercise Sweat Replenishment</div>
            <div class="breakdown-val" id="w-sweat">+0.5 L</div>
          </div>
        </div>
      </section>
"""

w_geo = """
    <section class="geo-citation-box">
      <div class="geo-header">💡 Direct Answer (GEO & Quick Summary)</div>
      <p>Per the <strong>National Academies of Sciences, Engineering, and Medicine (NASEM)</strong>, adequate daily total fluid intake is:</p>
      <ul>
        <li><strong>Men:</strong> Approximately 3.7 liters (125 fl oz or ~15.5 cups) per day from all beverages and moisture-rich foods.</li>
        <li><strong>Women:</strong> Approximately 2.7 liters (91 fl oz or ~11.5 cups) per day.</li>
      </ul>
      <p>Baseline metabolic requirement is calculated as <strong>35 mL per kilogram of body weight</strong>, adding 350–500 mL for every 30 minutes of vigorous physical activity.</p>
    </section>
"""

w_toc = """
    <nav class="toc-container" aria-label="Table of Contents">
      <div class="toc-title">📑 Table of Contents</div>
      <ul class="toc-list">
        <li><a href="#water-science">Hydration Physiology & Science</a></li>
        <li><a href="#nasem-guidelines">NASEM & WHO Water Benchmarks</a></li>
        <li><a href="#electrolytes">Electrolyte Balance & Hyponatremia Risk</a></li>
        <li><a href="#w-faq">Frequently Asked Questions</a></li>
      </ul>
    </nav>
"""

w_article = """
      <h2 id="water-science">Hydration Physiology & Metabolic Demands</h2>
      <p>Water constitutes roughly 60% of an adult's total body weight and is the medium for cellular metabolism, thermoregulation through perspiration, and the removal of metabolic waste via renal filtration. Mild dehydration (loss of just 1.5–2% of total body mass in water) impairs cognitive focus, induces headaches, and reduces physical endurance.</p>

      <div class="formula-box">
        <div class="formula-title">Hydration Intake Calculation Formula</div>
        <div class="formula-code">Daily Water (mL) = [Weight (kg) × 35 mL] + [Exercise (min) × 12 mL] × Climate Factor</div>
        <div class="formula-legend">Climate factor ranges from 1.0 (temperate) to 1.3 (hot desert conditions)</div>
      </div>

      <h2 id="nasem-guidelines">Authoritative Guidelines from NASEM and WHO</h2>
      <p>Roughly 20% of your daily water intake naturally comes from food (fruits, vegetables, soups), while the remaining 80% must be consumed directly through drinking water and unsweetened beverages.</p>

      <h2 id="electrolytes">Electrolyte Balance & Avoiding Water Intoxication</h2>
      <p>Drinking excessive quantities of plain water without adequate electrolyte replenishment during endurance activities can cause <em>hyponatremia</em> (abnormally low blood sodium concentration). During heavy workouts exceeding 60 minutes in heat, supplement water with sodium, potassium, and magnesium.</p>

      <h2 id="w-faq">Frequently Asked Questions</h2>
      <div class="faq-wrap">
        <details class="faq-item">
          <summary>Does coffee or tea count toward daily hydration?</summary>
          <div class="faq-content">Yes. Extensive research from the University of Birmingham confirmed that moderate caffeine intake (up to 400 mg or roughly 4 cups of coffee daily) exhibits hydrating qualities comparable to plain water without dehydrating diuretic effects.</div>
        </details>
      </div>
"""

w_script = """
  <script>
    function calcWater() {
      const w = parseFloat(document.getElementById('w-weight').value) || 70;
      const exMin = parseFloat(document.getElementById('w-exercise').value) || 0;
      const climate = parseFloat(document.getElementById('w-climate').value) || 1.15;

      const baseMl = w * 35;
      const sweatMl = (exMin / 30) * 350;
      const totalMl = (baseMl + sweatMl) * climate;

      const totalL = totalMl / 1000;
      const totalOz = totalMl * 0.033814;
      const glasses = totalOz / 8;

      document.getElementById('w-liters').textContent = totalL.toFixed(1);
      document.getElementById('w-ounces').textContent = totalOz.toFixed(1) + ' fl oz';
      document.getElementById('w-glasses').textContent = glasses.toFixed(1) + ' glasses';
      document.getElementById('w-baseline').textContent = (baseMl / 1000).toFixed(1) + ' L';
      document.getElementById('w-sweat').textContent = '+' + (sweatMl / 1000).toFixed(1) + ' L';
    }
    function copyResults() {
      const l = document.getElementById('w-liters').textContent;
      window.copyToClipboard(`CalcHub Daily Hydration Target: ${l} Liters/day`);
    }
    calcWater();
  </script>
"""

with open(os.path.join(OUTPUT_DIR, "water-intake-calculator.html"), "w", encoding="utf-8") as f:
    f.write(page_scaffold("Daily Water Intake Calculator — Optimal Hydration Goals",
                          "Calculate your daily water intake requirements based on body weight, exercise intensity, and climate conditions using NASEM hydration standards.",
                          "water intake calculator, daily hydration calculator, how much water to drink, hydration formula, liters of water per day",
                          "water-intake-calculator", "Health & Fitness", "health", w_app_json,
                          "Maintain peak athletic performance, cellular health, and cognitive clarity. Compute your customized daily fluid target in liters, ounces, and glasses.",
                          w_workspace, w_geo, w_toc, w_article, w_script))

print("Created body-fat-calculator.html, ideal-weight-calculator.html, and water-intake-calculator.html!")
