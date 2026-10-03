"""
Batch 21 - Part 2: Health & Clinical Tools
3. body-surface-area-calculator.html (Body Surface Area Multi-Formula & Hemodynamic Indexation)
4. bsa-calculator.html (BSA Chemotherapy Dosing, Calvert Carboplatin AUC & Renal Sizing)
Word count target: >1,000 words in article-body each.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 3. body-surface-area-calculator.html
# -------------------------------------------------------------
BSA_MULTI_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Body Surface Area (BSA) Calculator | Mosteller, Du Bois & Haycock</title>
  <meta name="description" content="Calculate Body Surface Area (BSA in m²) using Mosteller, Du Bois, Haycock, Gehan-George, and Boyd formulas. Clinical indexing for cardiac output, GFR, and burn fluid resuscitation.">
  <link rel="canonical" href="https://calchub.com/body-surface-area-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Clinical Body Surface Area (BSA) Multi-Formula Calculator",
    "applicationCategory": "HealthApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0.00",
      "priceCurrency": "USD"
    },
    "description": "Calculates clinical Body Surface Area (BSA in m²) comparing Mosteller, Du Bois, Haycock, Gehan-George, and Boyd formulas, including cardiac index and burn resuscitation."
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is the Mosteller formula for Body Surface Area?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Mosteller formula is BSA (m²) = √[ (Height in cm × Weight in kg) / 3600 ]. In US customary units, it is BSA (m²) = √[ (Height in inches × Weight in lbs) / 3131 ]. It is the most widely adopted formula in modern clinical oncology and nephrology due to its mathematical simplicity and high concordance with 3D photonic body scans."
        }
      },
      {
        "@type": "Question",
        "name": "Why is Body Surface Area preferred over simple weight for drug dosing and physiological metrics?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Body Surface Area scales allometrically with metabolic rate, basal energy expenditure, circulating blood volume, cardiac output, and glomerular filtration rate (GFR). Adipose tissue has significantly lower blood flow and metabolic activity than lean visceral mass, so dosing highly toxic medications (such as chemotherapy) solely by total body weight leads to severe overdosing in obese patients and underdosing in slender patients."
        }
      },
      {
        "@type": "Question",
        "name": "Which BSA formula is considered most accurate for pediatric patients?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Haycock formula [BSA = 0.024265 × Weight(kg)^0.5378 × Height(cm)^0.3964] is widely recognized in pediatric intensive care and nephrology because it was specifically derived from neonates, infants, children, and young adults, providing superior accuracy across low birth weight and pediatric body surface-to-mass ratios."
        }
      },
      {
        "@type": "Question",
        "name": "What is the normal average Body Surface Area for adult men and women?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The historical standard reference human BSA is 1.73 m² (used to normalize GFR measurements). In contemporary populations, the average adult male BSA is approximately 1.90 m² to 2.00 m², while the average adult female BSA is approximately 1.60 m² to 1.70 m²."
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
        <div class="badge-tag">Clinical Physiology</div>
        <h1 class="calculator-title">Body Surface Area (BSA) Calculator</h1>
        <p class="calculator-description">Calculate Body Surface Area ($m^2$) across all major validated clinical formulas: Mosteller, Du Bois &amp; Du Bois, Haycock (Pediatric), Gehan &amp; George, and Boyd.</p>
      </div>

      <div class="calculator-grid">
        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Patient Anthropometrics</h2>
          </div>
          <div class="calc-card-body">
            <div class="form-group">
              <label for="unit-system" class="form-label">Measurement Unit System</label>
              <select id="unit-system" class="form-select" onchange="toggleUnits()">
                <option value="metric" selected>Metric Units (cm, kg)</option>
                <option value="us">US Customary Units (inches, lbs)</option>
              </select>
            </div>

            <div class="form-group">
              <label for="height-val" class="form-label" id="label-height">Height (cm)</label>
              <input type="number" id="height-val" class="form-input" value="175" min="30" max="250" step="0.5" oninput="calculateBSA()">
              <span class="form-hint" id="hint-height">Adult average: 160 – 185 cm</span>
            </div>

            <div class="form-group">
              <label for="weight-val" class="form-label" id="label-weight">Weight (kg)</label>
              <input type="number" id="weight-val" class="form-input" value="70" min="1" max="350" step="0.5" oninput="calculateBSA()">
              <span class="form-hint" id="hint-weight">Patient total body mass</span>
            </div>

            <div class="form-group">
              <label for="primary-formula" class="form-label">Primary Clinical Reference Formula</label>
              <select id="primary-formula" class="form-select" onchange="calculateBSA()">
                <option value="mosteller" selected>Mosteller (Modern Clinical Standard)</option>
                <option value="dubois">Du Bois &amp; Du Bois (Historical Landmark)</option>
                <option value="haycock">Haycock (Pediatric &amp; Low Weight)</option>
                <option value="gehan">Gehan &amp; George (Large Empirical Cohort)</option>
                <option value="boyd">Boyd (Obesity Derivation)</option>
              </select>
            </div>

            <button type="button" class="btn btn-primary" onclick="calculateBSA()">Calculate Body Surface Area</button>
          </div>
        </div>

        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Calculated Surface Area & Indexes</h2>
          </div>
          <div class="calc-card-body">
            <div class="result-hero" style="background:#eff6ff;border-color:#bfdbfe;">
              <span class="hero-label">Primary Body Surface Area (Mosteller)</span>
              <div class="hero-value" id="res-bsa-primary" style="color:#1d4ed8;font-size:2.4rem;">1.84 m²</div>
              <span class="form-hint" id="res-bsa-diff">Standard Reference Adult Baseline: 1.73 m² (+6.4%)</span>
            </div>

            <div class="results-grid" style="margin-top:1.5rem;">
              <div class="result-item">
                <span class="result-label">Du Bois &amp; Du Bois</span>
                <span class="result-value" id="res-bsa-dubois">1.85 m²</span>
              </div>
              <div class="result-item">
                <span class="result-label">Haycock (Pediatric)</span>
                <span class="result-value" id="res-bsa-haycock">1.84 m²</span>
              </div>
              <div class="result-item">
                <span class="result-label">Gehan &amp; George</span>
                <span class="result-value" id="res-bsa-gehan">1.84 m²</span>
              </div>
              <div class="result-item">
                <span class="result-label">Boyd Formula</span>
                <span class="result-value" id="res-bsa-boyd">1.86 m²</span>
              </div>
            </div>

            <div class="stat-box" style="margin-top:1.5rem;padding:1rem;background:#f8fafc;border-radius:8px;border:1px solid #e2e8f0;">
              <h4 style="font-weight:700;margin-bottom:0.5rem;font-size:0.95rem;">Hemodynamic & Physiological Normalization:</h4>
              <p id="res-hemo" style="font-size:0.875rem;color:#475569;margin:0;">
                Resting Cardiac Output norm (5.0 L/min) corresponds to a Cardiac Index of <strong>2.72 L/min/m²</strong> (Normal range: 2.5 to 4.0 L/min/m²). Standard GFR indexing factor: <strong>1.06×</strong> reference.
              </p>
            </div>
          </div>
        </div>
      </div>

      <article class="article-body">
        <h2>Physiological Rationale for Body Surface Area Indexing</h2>
        <p>
          In human medicine, pharmacokinetics, and clinical hemodynamics, simple total body mass (weight in kilograms or pounds) provides a notoriously flawed denominator for scaling metabolic processes. Adipose tissue is poorly vascularized and metabolically quiescent compared to high-perfusion visceral organs such as the liver, kidneys, heart, and brain. Consequently, metabolic clearance rates, basal energy expenditure (BEE), and renal ultrafiltration correlate far more tightly with <strong>Body Surface Area ($BSA$)</strong> than with body weight alone.
        </p>
        <p>
          This biological phenomenon follows the classical <em>allometric surface area-to-volume scaling law</em> (Rubner's Surface Rule). As an organism increases in mass, heat dissipation to the surrounding environment occurs across the two-dimensional cutaneous surface, while basal heat generation occurs across three-dimensional cellular volume. In humans, physiological parameters—including glomerular filtration rate ($mL/min/1.73m^2$), cardiac index ($L/min/m^2$), pulmonary vital capacity, and narrow-therapeutic-index chemotherapeutic drugs—are universally normalized to body surface area.
        </p>

        <h2>Mathematical Comparison of Validated BSA Formulas</h2>
        <p>
          Direct physical measurement of human surface area requires intricate coating techniques or three-dimensional stereophotogrammetry. Over the past century, clinical researchers developed multiple empirical equations relating readily accessible height and weight measurements to true cutaneous surface area:
        </p>

        <div class="formula-box">
          <p><strong>1. Mosteller Formula (1987) - The Modern Universal Standard:</strong></p>
          $$BSA\text{ (m}^2\text{)} = \sqrt{\frac{\text{Height (cm)} \times \text{Weight (kg)}}{3600}} = \sqrt{\frac{\text{Height (in)} \times \text{Weight (lbs)}}{3131}}$$
          <p>
            Published in the <em>New England Journal of Medicine</em>, Mosteller's formula simplified complex logarithmic exponents into a single square-root function that can be calculated on a standard pocket calculator while maintaining less than 1% variance from Du Bois.
          </p>
        </div>

        <div class="formula-box">
          <p><strong>2. Du Bois &amp; Du Bois Formula (1916) - Historical Landmark:</strong></p>
          $$BSA\text{ (m}^2\text{)} = 0.007184 \times \text{Weight (kg)}^{0.425} \times \text{Height (cm)}^{0.725}$$
          <p>
            Derived by Delafield and Eugene Du Bois via precise paper-mold measurements of 9 human subjects (including a bilateral amputee and an emaciated child), this formula served as the foundational clinical benchmark for over 70 years.
          </p>
        </div>

        <div class="formula-box">
          <p><strong>3. Haycock Formula (1978) - Pediatric and Neonatal Standard:</strong></p>
          $$BSA\text{ (m}^2\text{)} = 0.024265 \times \text{Weight (kg)}^{0.5378} \times \text{Height (cm)}^{0.3964}$$
          <p>
            Specifically validated across 81 subjects ranging from premature infants weighing under 1 kg to fully developed adults. It eliminates the systematic underestimation seen with Du Bois in neonates.
          </p>
        </div>

        <div class="formula-box">
          <p><strong>4. Gehan &amp; George Formula (1970) - Empirical Autopsy Cohort:</strong></p>
          $$BSA\text{ (m}^2\text{)} = 0.0235 \times \text{Weight (kg)}^{0.51456} \times \text{Height (cm)}^{0.42246}$$
          <p>
            Derived from 401 direct surface area measurements conducted by the National Cancer Institute (NCI).
          </p>
        </div>

        <div class="formula-box">
          <p><strong>5. Boyd Formula (1935) - Dynamic Weight-Dependent Exponent:</strong></p>
          $$BSA\text{ (m}^2\text{)} = 0.0003207 \times \text{Height (cm)}^{0.3} \times \text{Weight (grams)}^{0.7285 - (0.0188 \times \log_{10}[\text{Weight in grams}])}$$
          <p>
            Introduced a non-linear exponent that adjusts for progressive adiposity and extreme body mass indexes.
          </p>
        </div>

        <h2>Clinical Applications Across Medical Disciplines</h2>
        <p>
          Standardized body surface area calculations form the bedrock of several critical medical specialties:
        </p>
        <ul>
          <li><strong>Clinical Oncology:</strong> High-toxicity cytotoxic agents—including doxorubicin, paclitaxel, 5-fluorouracil, and cisplatin—are dosed strictly in milligrams per square meter ($mg/m^2$). In patients with extreme obesity ($BMI > 35\text{ kg/m}^2$), clinical oncologists debate whether to cap BSA at $2.0\text{ m}^2$ or use full actual BSA to prevent undertreating curative malignancies.</li>
          <li><strong>Nephrology and Renal Medicine:</strong> Glomerular filtration rate (GFR) is universally reported normalized to a standard body surface area of $1.73\text{ m}^2$. For drug dosing (such as aminoglycosides or vancomycin), un-indexing GFR to the patient's individual BSA is necessary to avoid toxic accumulation.</li>
          <li><strong>Cardiovascular Hemodynamics:</strong> Cardiac output ($CO$, normal 4 to 8 L/min) varies dramatically with physical stature. The <em>Cardiac Index ($CI$)</em> normalizes flow to surface area:
            $$CI = \frac{CO}{BSA}\quad (\text{Normal reference: } 2.5 \text{ to } 4.0\text{ L/min/m}^2)$$
            A cardiac index below $2.2\text{ L/min/m}^2$ signifies cardiogenic shock or decompensated heart failure requiring inotropic support.
          </li>
          <li><strong>Severe Burn Resuscitation (Parkland Formula):</strong> Emergency fluid resuscitation in massive thermal injuries utilizes Total Body Surface Area percentages ($TBSA\%$) mapped via the Lund-Browder or Wallace Rule of Nines chart:
            $$\text{Resuscitation Volume (first 24h)} = 4\text{ mL} \times \text{Body Weight (kg)} \times \%TBSA\text{ second/third degree}$$
          </li>
        </ul>

        <h2>Comprehensive Clinical Reference Data Table</h2>
        <p>
          The table below demonstrates formula concordance and variance across the full spectrum of pediatric and adult anthropometrics:
        </p>

        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>Demographic Category</th>
                <th>Height (cm / in)</th>
                <th>Weight (kg / lbs)</th>
                <th>Mosteller (m²)</th>
                <th>Du Bois (m²)</th>
                <th>Haycock (m²)</th>
                <th>Boyd (m²)</th>
                <th>Cardiac Output Nomogram</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Neonate (1 Month)</strong></td>
                <td>54 cm (21.3 in)</td>
                <td>4.0 kg (8.8 lbs)</td>
                <td>0.245</td>
                <td>0.246</td>
                <td>0.248</td>
                <td>0.247</td>
                <td>CO ≈ 0.8 L/min (CI: 3.2 L/min/m²)</td>
              </tr>
              <tr>
                <td><strong>Child (6 Years)</strong></td>
                <td>115 cm (45.3 in)</td>
                <td>20 kg (44.1 lbs)</td>
                <td>0.800</td>
                <td>0.793</td>
                <td>0.795</td>
                <td>0.805</td>
                <td>CO ≈ 2.5 L/min (CI: 3.1 L/min/m²)</td>
              </tr>
              <tr>
                <td><strong>Slender Adult Female</strong></td>
                <td>162 cm (63.8 in)</td>
                <td>52 kg (114.6 lbs)</td>
                <td>1.530</td>
                <td>1.536</td>
                <td>1.535</td>
                <td>1.538</td>
                <td>CO ≈ 4.3 L/min (CI: 2.8 L/min/m²)</td>
              </tr>
              <tr>
                <td><strong>Standard Reference Adult</strong></td>
                <td>173 cm (68.1 in)</td>
                <td>70 kg (154.3 lbs)</td>
                <td>1.834</td>
                <td>1.832</td>
                <td>1.833</td>
                <td>1.848</td>
                <td>CO ≈ 5.0 L/min (CI: 2.7 L/min/m²)</td>
              </tr>
              <tr>
                <td><strong>Tall Athletic Male</strong></td>
                <td>188 cm (74.0 in)</td>
                <td>88 kg (194.0 lbs)</td>
                <td>2.144</td>
                <td>2.146</td>
                <td>2.152</td>
                <td>2.176</td>
                <td>CO ≈ 6.2 L/min (CI: 2.9 L/min/m²)</td>
              </tr>
              <tr>
                <td><strong>Severe Obesity (Class III)</strong></td>
                <td>175 cm (68.9 in)</td>
                <td>135 kg (297.6 lbs)</td>
                <td>2.563</td>
                <td>2.488</td>
                <td>2.527</td>
                <td>2.624</td>
                <td>CO ≈ 7.0 L/min (CI: 2.7 L/min/m²)</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2>Worked Clinical Calculation Example</h2>
        <div class="worked-example-card">
          <div class="example-header">
            <span class="example-badge">Clinical Case Study</span>
            <h3 class="example-title">Intensive Care Hemodynamic Indexation</h3>
          </div>
          <div class="example-step">
            <div class="step-num">1</div>
            <div class="step-content">
              <strong>Patient Data:</strong> A 68-year-old female is admitted to the surgical ICU following coronary artery bypass graft (CABG) surgery. Height is 165 cm, Weight is 64 kg. Pulmonary artery catheterization demonstrates a thermodilution Cardiac Output ($CO$) of 3.8 L/min. The intensivist must determine her exact BSA and Cardiac Index ($CI$) to evaluate for low-output syndrome.
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">2</div>
            <div class="step-content">
              <strong>Calculate Mosteller Body Surface Area:</strong>
              $$BSA = \sqrt{\frac{165 \times 64}{3600}} = \sqrt{\frac{10560}{3600}} = \sqrt{2.9333} = \mathbf{1.7127\text{ m}^2}$$
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">3</div>
            <div class="step-content">
              <strong>Cross-Validate with Du Bois Formula:</strong>
              $$BSA = 0.007184 \times (64)^{0.425} \times (165)^{0.725} = 0.007184 \times 5.867 \times 40.548 = \mathbf{1.7088\text{ m}^2}$$
              The difference between Mosteller and Du Bois is less than 0.23%, confirming excellent clinical precision.
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">4</div>
            <div class="step-content">
              <strong>Calculate Cardiac Index and Clinical Interpretation:</strong>
              $$CI = \frac{CO}{BSA} = \frac{3.8\text{ L/min}}{1.713\text{ m}^2} = \mathbf{2.218\text{ L/min/m}^2}$$
              <strong>Interpretation:</strong> A cardiac index of 2.22 L/min/m² borders the diagnostic threshold for cardiogenic hypoperfusion ($CI < 2.2$). Low-dose inotropic support (dobutamine or milrinone) and afterload optimization are indicated.
            </div>
          </div>
        </div>

        <h2>Modern Validation: 3D Whole-Body Photonic Scanning and Extreme Anthropometrics</h2>
        <p>
          In recent decades, biomedical engineers and clinical pharmacologists validated historical BSA equations against modern high-precision three-dimensional photonic body surface scanners. These optical systems capture over 300,000 discrete surface coordinates across the human epidermis, generating an indisputable ground-truth measurement of cutaneous area.
        </p>
        <p>
          Validation studies published in the <em>European Journal of Clinical Pharmacology</em> demonstrated that in individuals with a normal body mass index ($18.5 \le BMI \le 24.9\text{ kg/m}^2$), the Mosteller, Du Bois, and Haycock formulas all correlate remarkably well with 3D photonic scans (mean error &lt; 2.5%). However, significant divergence emerges in extreme body habitus:
        </p>
        <ul>
          <li><strong>Severe Obesity ($BMI \ge 40\text{ kg/m}^2$):</strong> The Du Bois and Gehan-George formulas tend to systematically underestimate true cutaneous surface area by 4% to 8% in morbid obesity, because their derivation cohorts underrepresented modern extreme body compositions. The Livingston-Lee and Boyd formulas maintain superior linearity in severe adiposity.</li>
          <li><strong>Pediatric and Neonatal Intensive Care:</strong> In infants weighing under 10 kg, the head constitutes up to 20% of total surface area (compared to roughly 7% to 9% in adults), while the lower extremities represent a dramatically smaller percentage. Standard adult formulas (like Mosteller and Du Bois) lose precision below 0.5 m², whereas the <strong>Haycock formula</strong> explicitly corrects for this pediatric cephalic-to-limb proportion shift.</li>
        </ul>

        <h2>Critical Care Fluid Balances and Evaporative Heat Loss</h2>
        <p>
          Beyond pharmacotherapy, Body Surface Area dictates basal insensate water evaporation across the stratum corneum and respiratory tract (typically 300 to 500 mL/m²/day under thermoneutral resting conditions). In febrile, septic, or mechanically ventilated intensive care patients, insensate evaporative losses escalate by approximately 10% to 13% for each 1°C elevation in core body temperature above 37°C. Critical care physicians calculate maintenance fluid requirements and electrolyte replacement rates directly normalized to the patient's Mosteller BSA to preserve hemodynamic stability and prevent hypernatremic dehydration.
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
    function toggleUnits() {
      const system = document.getElementById('unit-system').value;
      const hLabel = document.getElementById('label-height');
      const wLabel = document.getElementById('label-weight');
      const hHint = document.getElementById('hint-height');
      const wHint = document.getElementById('hint-weight');
      const hInput = document.getElementById('height-val');
      const wInput = document.getElementById('weight-val');

      if (system === 'metric') {
        hLabel.innerText = 'Height (cm)';
        hHint.innerText = 'Adult average: 160 – 185 cm';
        hInput.value = '175';
        hInput.min = '30';
        hInput.max = '250';
        hInput.step = '0.5';

        wLabel.innerText = 'Weight (kg)';
        wHint.innerText = 'Patient total body mass';
        wInput.value = '70';
        wInput.min = '1';
        wInput.max = '350';
        wInput.step = '0.5';
      } else {
        hLabel.innerText = 'Height (inches)';
        hHint.innerText = 'Adult average: 63 – 73 inches';
        hInput.value = '69';
        hInput.min = '12';
        hInput.max = '98';
        hInput.step = '0.5';

        wLabel.innerText = 'Weight (lbs)';
        wHint.innerText = 'Patient total body mass';
        wInput.value = '154';
        wInput.min = '3';
        wInput.max = '770';
        wInput.step = '1';
      }
      calculateBSA();
    }

    function calculateBSA() {
      const system = document.getElementById('unit-system').value;
      let h = parseFloat(document.getElementById('height-val').value) || 0;
      let w = parseFloat(document.getElementById('weight-val').value) || 0;

      if (h <= 0 || w <= 0) return;

      let h_cm = (system === 'metric') ? h : h * 2.54;
      let w_kg = (system === 'metric') ? w : w * 0.45359237;

      // Formulas
      // 1. Mosteller
      const bsa_mosteller = Math.sqrt((h_cm * w_kg) / 3600);
      // 2. Du Bois
      const bsa_dubois = 0.007184 * Math.pow(w_kg, 0.425) * Math.pow(h_cm, 0.725);
      // 3. Haycock
      const bsa_haycock = 0.024265 * Math.pow(w_kg, 0.5378) * Math.pow(h_cm, 0.3964);
      // 4. Gehan-George
      const bsa_gehan = 0.0235 * Math.pow(w_kg, 0.51456) * Math.pow(h_cm, 0.42246);
      // 5. Boyd (w in grams)
      const w_g = w_kg * 1000;
      const boyd_exp = 0.7285 - (0.0188 * Math.log10(w_g));
      const bsa_boyd = 0.0003207 * Math.pow(h_cm, 0.3) * Math.pow(w_g, boyd_exp);

      const prefFormula = document.getElementById('primary-formula').value;
      let primaryVal = bsa_mosteller;
      if (prefFormula === 'dubois') primaryVal = bsa_dubois;
      else if (prefFormula === 'haycock') primaryVal = bsa_haycock;
      else if (prefFormula === 'gehan') primaryVal = bsa_gehan;
      else if (prefFormula === 'boyd') primaryVal = bsa_boyd;

      document.getElementById('res-bsa-primary').innerText = primaryVal.toFixed(2) + ' m²';
      document.getElementById('res-bsa-dubois').innerText = bsa_dubois.toFixed(2) + ' m²';
      document.getElementById('res-bsa-haycock').innerText = bsa_haycock.toFixed(2) + ' m²';
      document.getElementById('res-bsa-gehan').innerText = bsa_gehan.toFixed(2) + ' m²';
      document.getElementById('res-bsa-boyd').innerText = bsa_boyd.toFixed(2) + ' m²';

      const diffPct = ((primaryVal - 1.73) / 1.73 * 100).toFixed(1);
      const sign = (diffPct >= 0) ? '+' : '';
      document.getElementById('res-bsa-diff').innerText = `Standard Reference Adult Baseline: 1.73 m² (${sign}${diffPct}%)`;

      // Hemodynamics
      const ci_norm = (5.0 / primaryVal).toFixed(2);
      const gfr_factor = (primaryVal / 1.73).toFixed(2);
      document.getElementById('res-hemo').innerHTML = `Resting Cardiac Output norm (5.0 L/min) corresponds to a Cardiac Index of <strong>${ci_norm} L/min/m²</strong> (Normal range: 2.5 to 4.0 L/min/m²). Standard GFR indexing factor: <strong>${gfr_factor}×</strong> reference.`;
    }

    document.addEventListener('DOMContentLoaded', calculateBSA);
  </script>
</body>
</html>
"""

# -------------------------------------------------------------
# 4. bsa-calculator.html
# -------------------------------------------------------------
BSA_CHEMO_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BSA Calculator | Oncology Chemotherapy & Calvert Carboplatin AUC Sizer</title>
  <meta name="description" content="Calculate Body Surface Area (BSA in m²) for oncology chemotherapy dosing (mg/m²) and Carboplatin AUC using the Calvert and Cockcroft-Gault CrCl equations.">
  <link rel="canonical" href="https://calchub.com/bsa-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Oncology BSA & Calvert Carboplatin Dosing Calculator",
    "applicationCategory": "HealthApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0.00",
      "priceCurrency": "USD"
    },
    "description": "Clinical oncology calculator determining patient Body Surface Area (BSA), target chemotherapy dose (mg/m²), and Carboplatin AUC dosing via the Calvert formula."
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "How does the Calvert formula calculate Carboplatin dosage?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Calvert equation is: Total Carboplatin Dose (mg) = Target AUC × (GFR + 25). Because carboplatin is cleared almost exclusively by glomerular filtration, dosing by renal clearance (GFR or estimated CrCl via Cockcroft-Gault) achieves the targeted therapeutic plasma exposure (Area Under the Curve) while preventing lethal thrombocytopenia."
        }
      },
      {
        "@type": "Question",
        "name": "Should chemotherapy doses be capped at 2.0 m² for obese cancer patients?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "According to the American Society of Clinical Oncology (ASCO) clinical practice guidelines, full actual weight-based Body Surface Area (BSA) should be used without empirical dose capping, unless clinical toxicity warrants reduction. Historical practice of arbitrarily capping BSA at 2.0 m² led to documented underdosing and worse cancer survival outcomes."
        }
      },
      {
        "@type": "Question",
        "name": "What is the maximum allowed GFR cap in the Calvert Carboplatin formula?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Both the FDA and ASCO recommend capping estimated GFR (or CrCl) at 125 mL/min in the Calvert formula. For instance, for an AUC of 6, the maximum carboplatin dose is 6 × (125 + 25) = 900 mg, preventing severe hematologic toxicity in hyperfiltering patients."
        }
      },
      {
        "@type": "Question",
        "name": "How is Creatinine Clearance (CrCl) calculated for oncology Calvert dosing?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The standard Cockcroft-Gault equation is: CrCl (mL/min) = [(140 - Age) × Weight (kg)] / (72 × Serum Creatinine mg/dL), multiplied by 0.85 for female patients. Actual body weight is generally recommended unless morbidly obese."
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
        <div class="badge-tag">Clinical Oncology</div>
        <h1 class="calculator-title">Oncology BSA &amp; Chemotherapy Dosing Calculator</h1>
        <p class="calculator-description">Calculate patient Body Surface Area ($m^2$), weight-based chemotherapy doses ($\text{mg/m}^2$), and target Carboplatin AUC using the Calvert and Cockcroft-Gault equations.</p>
      </div>

      <div class="calculator-grid">
        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Patient Anthropometrics &amp; Drug Protocol</h2>
          </div>
          <div class="calc-card-body">
            <div class="form-row" style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
              <div class="form-group">
                <label for="chemo-height" class="form-label">Height (cm)</label>
                <input type="number" id="chemo-height" class="form-input" value="172" min="50" max="240" step="0.5" oninput="calculateChemo()">
              </div>
              <div class="form-group">
                <label for="chemo-weight" class="form-label">Weight (kg)</label>
                <input type="number" id="chemo-weight" class="form-input" value="72" min="5" max="300" step="0.5" oninput="calculateChemo()">
              </div>
            </div>

            <div class="form-row" style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
              <div class="form-group">
                <label for="chemo-age" class="form-label">Patient Age (Years)</label>
                <input type="number" id="chemo-age" class="form-input" value="62" min="18" max="110" step="1" oninput="calculateChemo()">
              </div>
              <div class="form-group">
                <label for="chemo-gender" class="form-label">Biological Sex</label>
                <select id="chemo-gender" class="form-select" onchange="calculateChemo()">
                  <option value="female" selected>Female (0.85 CrCl factor)</option>
                  <option value="male">Male (1.00 CrCl factor)</option>
                </select>
              </div>
            </div>

            <div class="form-group">
              <label for="chemo-scr" class="form-label">Serum Creatinine (mg/dL)</label>
              <input type="number" id="chemo-scr" class="form-input" value="0.9" min="0.2" max="10.0" step="0.05" oninput="calculateChemo()">
              <span class="form-hint">Normal laboratory baseline: 0.6 – 1.2 mg/dL</span>
            </div>

            <div class="form-row" style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
              <div class="form-group">
                <label for="chemo-prescribed" class="form-label">Chemo Dose (mg/m²)</label>
                <input type="number" id="chemo-prescribed" class="form-input" value="75" min="1" max="2500" step="5" oninput="calculateChemo()">
              </div>
              <div class="form-group">
                <label for="chemo-auc" class="form-label">Target Carboplatin AUC</label>
                <select id="chemo-auc" class="form-select" onchange="calculateChemo()">
                  <option value="5" selected>AUC 5 (Standard solid tumor)</option>
                  <option value="6">AUC 6 (Ovarian / Lung first line)</option>
                  <option value="4">AUC 4 (Previously irradiated / elderly)</option>
                  <option value="2">AUC 2 (Weekly radiosensitizing)</option>
                </select>
              </div>
            </div>

            <button type="button" class="btn btn-primary" onclick="calculateChemo()">Compute Oncology Dosages</button>
          </div>
        </div>

        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Dosage Recommendations</h2>
          </div>
          <div class="calc-card-body">
            <div class="result-hero" style="background:#fdf2f8;border-color:#fbcfe8;">
              <span class="hero-label">Calculated BSA (Mosteller)</span>
              <div class="hero-value" id="res-chemo-bsa" style="color:#be185d;font-size:2.4rem;">1.85 m²</div>
              <span class="form-hint">Du Bois: <span id="res-chemo-dubois">1.84 m²</span> | ASCO Uncapped Protocol</span>
            </div>

            <div class="results-grid" style="margin-top:1.5rem;">
              <div class="result-item">
                <span class="result-label">Standard Chemotherapy Dose</span>
                <span class="result-value" id="res-chemo-total-dose">138.8 mg</span>
              </div>
              <div class="result-item">
                <span class="result-label">Cockcroft-Gault CrCl</span>
                <span class="result-value" id="res-chemo-crcl">73.5 mL/min</span>
              </div>
              <div class="result-item">
                <span class="result-label">Calvert Carboplatin Dose</span>
                <span class="result-value" id="res-carboplatin-dose">492 mg</span>
              </div>
              <div class="result-item">
                <span class="result-label">Max FDA Cap for AUC</span>
                <span class="result-value" id="res-carboplatin-cap">750 mg</span>
              </div>
            </div>

            <div class="stat-box" style="margin-top:1.5rem;padding:1rem;background:#f8fafc;border-radius:8px;border:1px solid #e2e8f0;">
              <h4 style="font-weight:700;margin-bottom:0.5rem;font-size:0.95rem;">Oncology Safety &amp; Organ Clearance Note:</h4>
              <p id="res-chemo-note" style="font-size:0.875rem;color:#475569;margin:0;">
                Patient renal function is adequate for full AUC 5 dosing without GFR ceiling truncation. Dose rounding to nearest vial or 5 mg recommended by institutional pharmacy guidelines.
              </p>
            </div>
          </div>
        </div>
      </div>

      <article class="article-body">
        <h2>Principles of Chemotherapy Dosing and Pharmacokinetics</h2>
        <p>
          Unlike therapeutic agents with broad safety margins (such as penicillins or antihypertensives), antineoplastic cytotoxic medications possess an exceptionally steep dose-response curve paired with a narrow therapeutic window. The concentration required to eradicate malignant clones is frequently indistinguishable from the threshold causing life-threatening myelosuppression, cardiotoxicity, or gastrointestinal mucositis.
        </p>
        <p>
          In the 1950s, laboratory animal studies by Pinkel established that cross-species toxicities of antimetabolite drugs (including methotrexate and 6-mercaptopurine) matched far more accurately when normalized to Body Surface Area ($m^2$) rather than weight ($mg/kg$). Because drug clearance mechanisms—including hepatic blood perfusion, cytochrome P450 enzyme abundance, and glomerular filtration—scale with surface area, the oncology community universally adopted $mg/m^2$ as the standard dosing nomenclature for cytotoxic protocols.
        </p>

        <h2>The ASCO Obesity Dosing Guidelines</h2>
        <p>
          For decades, widespread clinical anxiety over drug-induced toxicity led oncologists to arbitrarily "cap" the body surface area of obese patients at $2.0\text{ m}^2$ or calculate doses using an idealized or adjusted body weight ($ABW$). In 2012 (and updated in 2021), the <strong>American Society of Clinical Oncology (ASCO)</strong> published a definitive practice guideline systematically disproving this dogma:
        </p>
        <ul>
          <li><strong>Actual Weight Preservation:</strong> Retrospective and prospective studies in breast, colon, ovarian, and lung cancers demonstrated that capping BSA at $2.0\text{ m}^2$ resulted in significant underdosing in up to 40% of obese patients, leading to statistically higher cancer recurrence rates and reduced overall survival.</li>
          <li><strong>Toxicity Parity:</strong> Full, actual weight-based BSA dosing does not result in disproportionate increases in Grade 3 or 4 hematologic toxicities in obese individuals compared to normal-weight peers. ASCO firmly recommends using actual body weight for BSA calculations across all standard curative-intent regimens.</li>
        </ul>

        <h2>The Calvert Equation for Carboplatin AUC Dosing</h2>
        <p>
          While most antineoplastics are dosed in $mg/m^2$, the platinum coordination complex <strong>carboplatin</strong> is a notable exception. Carboplatin is cleared almost exclusively (greater than 85%) through simple renal glomerular filtration, without significant tubular secretion or reabsorption. Dosing carboplatin by surface area produced erratic systemic exposure and unpredictable nadir thrombocytopenia.
        </p>
        <p>
          In 1989, Hilary Calvert and colleagues published a pharmacokinetic formula establishing that carboplatin's systemic exposure—measured as the Area Under the Plasma Concentration-Time Curve ($AUC$ in $mg/mL \cdot min$)—is directly coupled to renal clearance:
        </p>

        <div class="formula-box">
          <p><strong>The Calvert Formula:</strong></p>
          $$\text{Total Carboplatin Dose (mg)} = \text{Target AUC} \times (\text{GFR} + 25)$$
          <p>Where:</p>
          <ul>
            <li><strong>Target AUC:</strong> Chosen clinical exposure target (typically 4 to 6 $mg/mL \cdot min$ for single-agent or combination solid tumor regimens).</li>
            <li><strong>GFR (mL/min):</strong> Glomerular filtration rate, universally estimated via the Cockcroft-Gault creatinine clearance formula.</li>
            <li><strong>25:</strong> Empirical non-renal clearance constant ($mL/min$).</li>
          </ul>
        </div>

        <h2>Cockcroft-Gault Creatinine Clearance Estimation</h2>
        <p>
          In routine oncology clinical practice, serum creatinine is substituted into the Cockcroft-Gault equation to estimate renal capacity for Calvert dosing:
        </p>

        <div class="formula-box">
          <p><strong>Cockcroft-Gault Equation:</strong></p>
          $$CrCl\text{ (mL/min)} = \frac{(140 - \text{Age}) \times \text{Weight (kg)}}{72 \times \text{Serum Creatinine (mg/dL)}} \times (0.85\text{ if female})$$
          <p>
            <em>FDA Safety Cap:</em> In 2010, the US FDA and ASCO instituted a maximum GFR cap of <strong>125 mL/min</strong> in the Calvert equation. Patients with supranormal renal clearance (such as young patients with $CrCl > 150\text{ mL/min}$) must have GFR capped at 125 to avoid lethal carboplatin overdosing:
          </p>
          $$\text{Max Allowed Carboplatin Dose (mg)} = \text{Target AUC} \times (125 + 25) = \text{Target AUC} \times 150$$
        </div>

        <h2>Oncology Dosing Reference Table</h2>
        <p>
          The table below demonstrates representative cytotoxic regimens, BSA dosing, and Calvert AUC calculations:
        </p>

        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>Regimen / Protocol</th>
                <th>Standard Agent</th>
                <th>Prescribed Metric</th>
                <th>Standard BSA Dose (1.80 m²)</th>
                <th>Capped Max Dose / Safety Limit</th>
                <th>Primary Dose-Limiting Toxicity</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>AC Regimen (Breast)</strong></td>
                <td>Doxorubicin</td>
                <td>60 mg/m²</td>
                <td>108 mg</td>
                <td>Lifetime cumulative cap 450–550 mg/m²</td>
                <td>Irreversible cardiomyopathy, myelosuppression.</td>
              </tr>
              <tr>
                <td><strong>FOLFOX (Colorectal)</strong></td>
                <td>Oxaliplatin</td>
                <td>85 mg/m²</td>
                <td>153 mg</td>
                <td>Dose reduce for peripheral neuropathy</td>
                <td>Cold-induced dysesthesia, sensory neuropathy.</td>
              </tr>
              <tr>
                <td><strong>TC Protocol (Gynecologic)</strong></td>
                <td>Paclitaxel</td>
                <td>175 mg/m²</td>
                <td>315 mg</td>
                <td>Premedicate with dexamethasone/H1/H2</td>
                <td>Severe hypersensitivity, peripheral neuropathy.</td>
              </tr>
              <tr>
                <td><strong>TC Protocol (Gynecologic)</strong></td>
                <td>Carboplatin</td>
                <td>AUC 5 – 6</td>
                <td>450 – 550 mg (GFR dep.)</td>
                <td>Max cap: 750 mg (AUC 5) / 900 mg (AUC 6)</td>
                <td>Dose-limiting thrombocytopenia, neutropenia.</td>
              </tr>
              <tr>
                <td><strong>Cisplatin Combination</strong></td>
                <td>Cisplatin</td>
                <td>75 – 100 mg/m²</td>
                <td>135 – 180 mg</td>
                <td>Aggressive pre/post hydration mandatory</td>
                <td>Nephrotoxicity, ototoxicity, emetogenicity.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2>Worked Clinical Oncology Case Study</h2>
        <div class="worked-example-card">
          <div class="example-header">
            <span class="example-badge">Oncology Protocol Case</span>
            <h3 class="example-title">Ovarian Carcinoma Paclitaxel / Carboplatin Sizing</h3>
          </div>
          <div class="example-step">
            <div class="step-num">1</div>
            <div class="step-content">
              <strong>Patient Clinical Profile:</strong> A 64-year-old female diagnosed with stage III high-grade serous ovarian carcinoma is scheduled for Cycle 1 of Carboplatin (AUC 6) + Paclitaxel (175 mg/m²). Anthropometrics: Height = 168 cm, Weight = 75 kg. Laboratory values: Serum Creatinine = 0.85 mg/dL.
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">2</div>
            <div class="step-content">
              <strong>Calculate Body Surface Area (Mosteller):</strong>
              $$BSA = \sqrt{\frac{168 \times 75}{3600}} = \sqrt{\frac{12600}{3600}} = \sqrt{3.5} = \mathbf{1.871\text{ m}^2}$$
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">3</div>
            <div class="step-content">
              <strong>Calculate Prescribed Paclitaxel Dose:</strong>
              $$\text{Paclitaxel Dose} = 175\text{ mg/m}^2 \times 1.871\text{ m}^2 = 327.4\text{ mg}$$
              (Standard oncology pharmacy rounds to <strong>325 mg</strong> or 330 mg per institutional policy.)
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">4</div>
            <div class="step-content">
              <strong>Calculate Cockcroft-Gault Creatinine Clearance and Calvert Dose:</strong>
              $$CrCl = \frac{(140 - 64) \times 75}{72 \times 0.85} \times 0.85 = \frac{76 \times 75}{72} = \frac{5700}{72} = \mathbf{79.17\text{ mL/min}}$$
              Since 79.17 mL/min is below the 125 mL/min FDA cap, uncapped GFR is utilized:
              $$\text{Carboplatin Dose} = \text{Target AUC} \times (GFR + 25) = 6 \times (79.17 + 25) = 6 \times 104.17 = \mathbf{625\text{ mg}}$$
              The patient receives Paclitaxel 325 mg IV over 3 hours followed by Carboplatin 625 mg IV over 60 minutes.
            </div>
          </div>
        </div>

        <h2>Pharmacogenomic Stratification and Non-Renal Clearance Pathways</h2>
        <p>
          While Body Surface Area ($m^2$) standardizes the geometric denominator for drug distribution volume, systemic clearance remains heavily governed by inter-individual genetic polymorphism in phase I and phase II metabolic enzymes. Modern oncology protocols increasingly mandate pharmacogenomic profiling prior to administering full BSA-calculated dosages:
        </p>
        <ul>
          <li><strong>Dihydropyrimidine Dehydrogenase (DPD / DPYD gene):</strong> DPD is the primary catabolic enzyme responsible for clearing greater than 80% of administered fluoropyrimidines (5-Fluorouracil and capecitabine). Approximately 3% to 5% of patients carry partial DPD deficiency variants ($*2A, *13, \text{c.2846A>T}$), and 0.2% possess complete deficiency. In these individuals, administering a standard BSA-calculated dose results in life-threatening mucositis, neutropenic sepsis, and death. Clinical guidelines (CPIC) mandate a 50% initial dose reduction for intermediate metabolizers and total avoidance in poor metabolizers.</li>
          <li><strong>UDP-Glucuronosyltransferase 1A1 (UGT1A1):</strong> Irinotecan (used in FOLFIRINOX and FOLFIRI for pancreatic and colorectal cancers) is converted to its active metabolite SN-38, which requires hepatic glucuronidation by UGT1A1 for inactivation. Patients homozygous for the $UGT1A1*28$ allele (Gilbert syndrome genotype) suffer severe clearance impairment, predisposing them to Grade 4 diarrhea and profound neutropenia unless upfront BSA doses are adjusted.</li>
          <li><strong>Cockcroft-Gault vs. CKD-EPI in Calvert Sizing:</strong> While nephrology guidelines favor the CKD-EPI (2021 race-free) equation for diagnosing chronic kidney disease, oncology protocols universally retain Cockcroft-Gault for carboplatin dosing. CKD-EPI reports GFR in $mL/min/1.73m^2$; substituting this directly into the Calvert equation without de-indexing for individual BSA introduces systematic errors of 15% to 25% in very large or very small patients. When CKD-EPI is used, it must be multiplied by $(\text{Patient BSA} / 1.73)$ before entry into Calvert.</li>
        </ul>

        <h2>Hemodialysis and Special Organ Dysfunction Adjustments</h2>
        <p>
          In end-stage renal disease (ESRD) patients maintained on thrice-weekly intermittent hemodialysis, carboplatin Calvert dosing requires strict timing. Carboplatin is cleared by high-flux dialyzers with an extraction ratio of 40% to 50%. Standard clinical oncology protocol administers carboplatin immediately following a hemodialysis session, allowing a prolonged interdialytic period (typically 44 to 48 hours) for antineoplastic tissue exposure, using an empirical GFR estimate of 0 to 10 mL/min (resulting in a total dose of $AUC \times [0 + 25] = AUC \times 25\text{ mg}$).
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
    function calculateChemo() {
      const h = parseFloat(document.getElementById('chemo-height').value) || 0;
      const w = parseFloat(document.getElementById('chemo-weight').value) || 0;
      const age = parseFloat(document.getElementById('chemo-age').value) || 0;
      const gender = document.getElementById('chemo-gender').value;
      const scr = parseFloat(document.getElementById('chemo-scr').value) || 0.9;
      const prescribed = parseFloat(document.getElementById('chemo-prescribed').value) || 0;
      const targetAUC = parseFloat(document.getElementById('chemo-auc').value) || 5;

      if (h <= 0 || w <= 0 || age <= 0 || scr <= 0) return;

      // Mosteller BSA
      const bsa = Math.sqrt((h * w) / 3600);
      const bsa_dubois = 0.007184 * Math.pow(w, 0.425) * Math.pow(h, 0.725);

      document.getElementById('res-chemo-bsa').innerText = bsa.toFixed(2) + ' m²';
      document.getElementById('res-chemo-dubois').innerText = bsa_dubois.toFixed(2) + ' m²';

      // Standard Chemo Total Dose
      const totalChemo = prescribed * bsa;
      document.getElementById('res-chemo-total-dose').innerText = totalChemo.toFixed(1) + ' mg';

      // Cockcroft-Gault CrCl
      let crcl = ((140 - age) * w) / (72 * scr);
      if (gender === 'female') {
        crcl = crcl * 0.85;
      }
      document.getElementById('res-chemo-crcl').innerText = crcl.toFixed(1) + ' mL/min';

      // Calvert Formula with 125 cap
      const cappedGFR = Math.min(crcl, 125);
      const carboplatinDose = Math.round(targetAUC * (cappedGFR + 25));
      const maxCap = Math.round(targetAUC * (125 + 25));

      document.getElementById('res-carboplatin-dose').innerText = carboplatinDose + ' mg';
      document.getElementById('res-carboplatin-cap').innerText = maxCap + ' mg';

      const noteEl = document.getElementById('res-chemo-note');
      if (crcl > 125) {
        noteEl.innerHTML = `<strong style="color:#b91c1c;">FDA Safety Cap Applied:</strong> Patient CrCl (${crcl.toFixed(1)} mL/min) exceeds 125 mL/min. GFR capped at 125 mL/min to prevent severe myelotoxicity (max dose ${maxCap} mg).`;
      } else if (crcl < 50) {
        noteEl.innerHTML = `<strong style="color:#ca8a04;">Renal Impairment Warning:</strong> Patient CrCl is ${crcl.toFixed(1)} mL/min (< 50 mL/min). Close monitoring of platelet nadir at days 14-21 indicated; verify renal status before subsequent cycles.`;
      } else {
        noteEl.innerHTML = `Patient renal function is adequate for full AUC ${targetAUC} dosing without GFR ceiling truncation. Dose rounding to nearest vial or 5 mg recommended by institutional pharmacy guidelines.`;
      }
    }

    document.addEventListener('DOMContentLoaded', calculateChemo);
  </script>
</body>
</html>
"""

def generate_part2():
    with open(os.path.join(BASE_DIR, "body-surface-area-calculator.html"), "w", encoding="utf-8") as f:
        f.write(BSA_MULTI_HTML)
    print("Generated body-surface-area-calculator.html")

    with open(os.path.join(BASE_DIR, "bsa-calculator.html"), "w", encoding="utf-8") as f:
        f.write(BSA_CHEMO_HTML)
    print("Generated bsa-calculator.html")

if __name__ == "__main__":
    generate_part2()
