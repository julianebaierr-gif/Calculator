"""
Batch 21 - Part 1: Health & Clinical Tools
1. a1c-calculator.html (Hemoglobin A1C to Estimated Average Glucose eAG & IFCC mmol/mol)
2. bac-calculator.html (Blood Alcohol Concentration & Widmark Elimination Kinetics)
Word count target: >1,000 words in article-body each.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 1. a1c-calculator.html
# -------------------------------------------------------------
A1C_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>A1C Calculator | Convert HbA1c to eAG Glucose (mg/dL & mmol/L)</title>
  <meta name="description" content="Convert your Hemoglobin HbA1c percentage to Estimated Average Glucose (eAG) in mg/dL and mmol/L, plus IFCC units (mmol/mol). ADA clinical diagnostic guidelines and glycemic targets.">
  <link rel="canonical" href="https://calchub.com/a1c-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "HbA1c to eAG Clinical Glucose Converter",
    "applicationCategory": "HealthApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0.00",
      "priceCurrency": "USD"
    },
    "description": "Clinical calculator converting Hemoglobin A1C percentage to estimated average glucose (eAG) in mg/dL, mmol/L, and IFCC mmol/mol based on the ADAG clinical trial."
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is the mathematical formula to convert A1C to Estimated Average Glucose (eAG)?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The American Diabetes Association (ADA) formula derived from the A1C-Derived Average Glucose (ADAG) study is: eAG (mg/dL) = 28.7 × A1C (%) - 46.7. To express eAG in International System units (mmol/L), the formula is: eAG (mmol/L) = 1.59 × A1C (%) - 2.59, or simply dividing mg/dL by 18.015."
        }
      },
      {
        "@type": "Question",
        "name": "How does A1C differ from daily fingerstick or Continuous Glucose Monitor (CGM) readings?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A capillary blood fingerstick or interstitial CGM reading reflects blood glucose at that exact point in time. In contrast, Hemoglobin A1c (glycated hemoglobin) measures the percentage of hemoglobin proteins coated with glucose over the 90 to 120-day lifespan of red blood cells, weighted heavily toward the preceding 30 days."
        }
      },
      {
        "@type": "Question",
        "name": "What are the clinical diagnostic thresholds for normal, prediabetes, and diabetes?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "According to American Diabetes Association (ADA) criteria: Normal is an A1C below 5.7% (eAG < 117 mg/dL); Prediabetes is an A1C between 5.7% and 6.4% (eAG 117 to 137 mg/dL); and Diabetes is diagnosed at an A1C of 6.5% or higher (eAG ≥ 140 mg/dL) on two separate laboratory tests."
        }
      },
      {
        "@type": "Question",
        "name": "What conditions can falsely elevate or lower laboratory A1C readings?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Conditions altering erythrocyte turnover skew A1C. Falsely low A1C occurs in hemolytic anemia, acute blood loss, hemodialysis, and recovery from erythropoietin therapy (younger RBCs). Falsely high A1C occurs in iron deficiency anemia, vitamin B12 deficiency, asplenia, and chronic kidney disease with reduced red cell clearance."
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
        <div class="badge-tag">Clinical Endocrinology</div>
        <h1 class="calculator-title">Hemoglobin A1C to eAG Glucose Calculator</h1>
        <p class="calculator-description">Convert laboratory HbA1c percentage to Estimated Average Glucose (eAG) in mg/dL and mmol/L, plus IFCC units (mmol/mol), adhering to the international ADAG landmark trial.</p>
      </div>

      <div class="calculator-grid">
        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Patient Glycemic Parameters</h2>
          </div>
          <div class="calc-card-body">
            <div class="form-group">
              <label for="input-mode" class="form-label">Input Measurement Unit</label>
              <select id="input-mode" class="form-select" onchange="toggleInputMode()">
                <option value="ngsp" selected>NGSP / US Standard (%)</option>
                <option value="ifcc">IFCC / International (mmol/mol)</option>
                <option value="eag_mg">eAG Glucose (mg/dL)</option>
                <option value="eag_mmol">eAG Glucose (mmol/L)</option>
              </select>
            </div>

            <div class="form-group" id="group-a1c">
              <label for="a1c-val" class="form-label" id="label-val">Hemoglobin A1c Level (%)</label>
              <input type="number" id="a1c-val" class="form-input" value="7.0" min="3.5" max="20.0" step="0.1">
              <span class="form-hint" id="hint-val">Clinical diagnostic range: 4.0% to 15.0%</span>
            </div>

            <div class="form-group">
              <label for="clinical-target" class="form-label">Patient Clinical Target Guideline</label>
              <select id="clinical-target" class="form-select">
                <option value="standard" selected>ADA Standard Adult Diabetic Target (&lt; 7.0%)</option>
                <option value="tight">AACE / Stringent Early Stage Target (&lt; 6.5%)</option>
                <option value="elderly">Frail Elderly / Hypoglycemia Prone Target (&lt; 8.0%)</option>
                <option value="normal">Non-Diabetic Healthy Baseline (&lt; 5.7%)</option>
              </select>
            </div>

            <button type="button" class="btn btn-primary" onclick="calculateA1C()">Convert & Analyze Glycemia</button>
          </div>
        </div>

        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Estimated Average Glycemia & Status</h2>
          </div>
          <div class="calc-card-body">
            <div class="result-hero" style="background:#f0fdf4;border-color:#bbf7d0;">
              <span class="hero-label" id="res-status-title">Clinical Diagnostic Status</span>
              <div class="hero-value" id="res-status" style="color:#15803d;font-size:1.6rem;">Controlled Diabetes Target</div>
              <span class="form-hint" id="res-status-desc">Meets standard American Diabetes Association adult target</span>
            </div>

            <div class="results-grid" style="margin-top:1.5rem;">
              <div class="result-item">
                <span class="result-label">Estimated Glucose (eAG)</span>
                <span class="result-value" id="res-eag-mg">154 mg/dL</span>
              </div>
              <div class="result-item">
                <span class="result-label">International eAG</span>
                <span class="result-value" id="res-eag-mmol">8.6 mmol/L</span>
              </div>
              <div class="result-item">
                <span class="result-label">IFCC Standard Unit</span>
                <span class="result-value" id="res-ifcc">53 mmol/mol</span>
              </div>
              <div class="result-item">
                <span class="result-label">NGSP HbA1c</span>
                <span class="result-value" id="res-ngsp">7.0 %</span>
              </div>
            </div>

            <div class="stat-box" style="margin-top:1.5rem;padding:1rem;background:#f8fafc;border-radius:8px;border:1px solid #e2e8f0;">
              <h4 style="font-weight:700;margin-bottom:0.5rem;font-size:0.95rem;">Glycemic Variability & Microvascular Risk:</h4>
              <p id="res-risk-analysis" style="font-size:0.875rem;color:#475569;margin:0;">
                At 7.0% A1C (154 mg/dL average), relative risk for diabetic retinopathy and nephropathy progression is reduced by approximately 50-70% compared to sustained levels above 9.0%.
              </p>
            </div>
          </div>
        </div>
      </div>

      <article class="article-body">
        <h2>Physiological Principles of Hemoglobin Glycation</h2>
        <p>
          Hemoglobin A1c (glycated hemoglobin) is the biochemical gold standard for monitoring chronic glycemic exposure in individuals with diabetes mellitus. Inside human erythrocytes (red blood cells), adult hemoglobin consists predominantly of hemoglobin A ($HbA_0$). As circulating glucose diffuses freely across the erythrocyte membrane through insulin-independent glucose transporter 1 (GLUT1) carrier proteins, it undergoes a spontaneous, non-enzymatic nucleophilic addition reaction with the N-terminal valine residue of the hemoglobin $\beta$-chain.
        </p>
        <p>
          This biochemical cascade begins with the formation of an unstable aldimine intermediate, termed a pre-A1c Schiff base. Over subsequent hours, this Schiff base undergoes an irreversible, non-enzymatic chemical rearrangement known as the <strong>Amadori rearrangement</strong>, yielding a stable, ketoamine covalent adduct: Hemoglobin A1c. Because erythrocytes have a circulating lifespan averaging 115 to 120 days, the percentage of glycated hemoglobin directly mirrors the integrated time-weighted average blood glucose concentration over the preceding 8 to 12 weeks. However, because older erythrocytes continuously undergo splenic phagocytosis while newly formed reticulocytes enter circulation, the past 30 days contribute roughly 50% to the measured A1c value, whereas days 90 to 120 contribute merely 10%.
        </p>

        <h2>Mathematical Derivation of the ADAG Translation Equations</h2>
        <p>
          Historically, patients monitoring capillary blood glucose via fingerstick meters or continuous glucose monitors (CGM) found it challenging to relate an A1c percentage (e.g., 7.8%) to day-to-day blood glucose readings expressed in milligrams per deciliter ($mg/dL$) or millimoles per liter ($mmol/L$). In 2008, the American Diabetes Association (ADA), the European Association for the Study of Diabetes (EASD), and the International Diabetes Federation (IDF) completed the landmark <em>A1C-Derived Average Glucose (ADAG) study</em>.
        </p>
        <p>
          The ADAG trial continuously monitored over 500 adult subjects across multiple multinational centers using continuous glucose monitoring sensors combined with frequent multi-point capillary fingersticks over 12 weeks. Linear regression analysis established a robust correlation ($r = 0.92$) between mean plasma glucose and laboratory high-performance liquid chromatography (HPLC) HbA1c measurements:
        </p>

        <div class="formula-box">
          <p><strong>Primary ADAG Estimated Average Glucose (eAG) Equations:</strong></p>
          $$eAG\text{ (mg/dL)} = 28.7 \times \text{HbA1c (\%)} - 46.7$$
          $$eAG\text{ (mmol/L)} = 1.59 \times \text{HbA1c (\%)} - 2.59 = \frac{eAG\text{ (mg/dL)}}{18.015}$$
        </div>

        <p>
          Conversely, when converting international clinical trial data or European laboratory reports reported in the standard International Federation of Clinical Chemistry and Laboratory Medicine (IFCC) units of millimoles of glycated hemoglobin per mole of total hemoglobin ($mmol/mol$), the exact master equation derived from the global harmonization committee is applied:
        </p>

        <div class="formula-box">
          <p><strong>IFCC to NGSP Master Harmonization Equation:</strong></p>
          $$\text{HbA1c (mmol/mol)} = 10.929 \times (\text{HbA1c [\%]} - 2.15)$$
          $$\text{HbA1c (\%)} = \frac{\text{HbA1c (mmol/mol)}}{10.929} + 2.15$$
        </div>

        <h2>Comprehensive Clinical Glycemic Reference Benchmarks</h2>
        <p>
          The diagnostic categories established by the American Diabetes Association Standards of Care establish clear diagnostic criteria and treatment benchmarks for clinical endocrinology:
        </p>

        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>Diagnostic Category</th>
                <th>HbA1c (%)</th>
                <th>IFCC (mmol/mol)</th>
                <th>eAG (mg/dL)</th>
                <th>eAG (mmol/L)</th>
                <th>Clinical Action &amp; Microvascular Risk</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Optimal Non-Diabetic</strong></td>
                <td>4.5% – 5.4%</td>
                <td>26 – 36</td>
                <td>82 – 108</td>
                <td>4.6 – 6.0</td>
                <td>Physiologically baseline; negligible macro/microvascular excess risk.</td>
              </tr>
              <tr>
                <td><strong>Pre-Diabetes (Impaired)</strong></td>
                <td>5.7% – 6.4%</td>
                <td>39 – 46</td>
                <td>117 – 137</td>
                <td>6.5 – 7.6</td>
                <td>Elevated cardiometabolic risk; lifestyle intervention and metformin.</td>
              </tr>
              <tr>
                <td><strong>Diagnostic Diabetes</strong></td>
                <td>&ge; 6.5%</td>
                <td>&ge; 48</td>
                <td>&ge; 140</td>
                <td>&ge; 7.8</td>
                <td>Formal diabetes diagnosis threshold (requires 2 concordant tests).</td>
              </tr>
              <tr>
                <td><strong>Standard ADA Target</strong></td>
                <td>&lt; 7.0%</td>
                <td>&lt; 53</td>
                <td>&lt; 154</td>
                <td>&lt; 8.6</td>
                <td>Target for non-pregnant adults; halts microvascular retinopathy/nephropathy.</td>
              </tr>
              <tr>
                <td><strong>Suboptimal Control</strong></td>
                <td>7.1% – 8.5%</td>
                <td>54 – 69</td>
                <td>157 – 197</td>
                <td>8.7 – 11.0</td>
                <td>Progressive endothelial damage; pharmacotherapy intensification indicated.</td>
              </tr>
              <tr>
                <td><strong>Severe Hyperglycemia</strong></td>
                <td>&gt; 9.0%</td>
                <td>&gt; 75</td>
                <td>&gt; 212</td>
                <td>&gt; 11.8</td>
                <td>Exponentially accelerated risk for proliferative retinopathy and ketoacidosis.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2>Step-by-Step Clinical Case Study</h2>
        <div class="worked-example-card">
          <div class="example-header">
            <span class="example-badge">Endocrinology Case Study</span>
            <h3 class="example-title">Type 2 Diabetes Mellitus Therapy Optimization</h3>
          </div>
          <div class="example-step">
            <div class="step-num">1</div>
            <div class="step-content">
              <strong>Patient Clinical Presentation:</strong> A 54-year-old male with a 6-year history of Type 2 Diabetes presents for routine quarterly review. His laboratory venipuncture report reveals an HbA1c of <strong>8.4%</strong>. The clinician needs to establish his estimated average daily glucose (eAG), convert to IFCC units, and determine therapeutic adjustment.
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">2</div>
            <div class="step-content">
              <strong>Calculate Estimated Average Glucose in mg/dL:</strong>
              $$eAG = 28.7 \times 8.4 - 46.7 = 241.08 - 46.7 = 194.38\text{ mg/dL}$$
              Rounding to the nearest whole integer yields an estimated daily blood sugar of <strong>194 mg/dL</strong>.
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">3</div>
            <div class="step-content">
              <strong>Calculate International System Metrics (mmol/L and IFCC):</strong>
              $$eAG\text{ (mmol/L)} = \frac{194.38}{18.015} = 10.79\text{ mmol/L}$$
              $$\text{IFCC} = 10.929 \times (8.4 - 2.15) = 10.929 \times 6.25 = 68.31\text{ mmol/mol}$$
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">4</div>
            <div class="step-content">
              <strong>Clinical Action Plan:</strong> At 194 mg/dL average glucose, the patient experiences substantial postprandial glycemic excursions above the renal threshold for glucose resorption (~180 mg/dL). SGLT-2 inhibitor or GLP-1 receptor agonist initiation is indicated to titrate towards the target A1c of &lt; 7.0% (154 mg/dL).
            </div>
          </div>
        </div>

        <h2>Interfering Factors and Hemoglobin Variant Confounders</h2>
        <p>
          While the A1c assay provides exceptional longitudinal clinical utility, healthcare providers and patients must recognize physiological conditions where HbA1c diverges significantly from true mean blood glucose:
        </p>
        <ul>
          <li><strong>Altered Erythrocyte Turnover:</strong> Conditions that truncate the typical 120-day red blood cell survival curve result in an underestimation of glycemia. Hemolytic anemias, acute or chronic blood loss, splenomegaly, and treatment with recombinant erythropoietin produce an erythrocyte population skewed towards younger cells with insufficient time for glycation, artificially depressing A1C.</li>
          <li><strong>Prolonged Erythrocyte Survival:</strong> Iron deficiency anemia, folate/vitamin B12 deficiency, and post-splenectomy states retard red blood cell clearance, allowing erythrocytes to circulate for extended periods. This elevates the measured A1c by 0.5% to 1.5% without a corresponding increase in true mean plasma glucose.</li>
          <li><strong>Hemoglobinopathies:</strong> Common structural hemoglobin variants (including HbS, HbC, HbE, and elevated HbF) can interfere with ion-exchange high-performance liquid chromatography (HPLC) assays, causing analytical artifacts. Enzymatic, boronate-affinity chromatography, or immunoassay methods are required for valid determination in affected individuals.</li>
          <li><strong>Chronic Kidney Disease (CKD):</strong> Patients with advanced nephropathy (eGFR &lt; 30 mL/min/1.73m²) frequently suffer from a combination of shortened red cell survival, carbamylated hemoglobin formation from uremia, and frequent transfusions, rendering serum fructosamine or continuous glucose monitoring (GMI) more clinically dependable than A1C.</li>
        </ul>

        <h2>Modern CGM Metrics: Time-in-Range (TIR) and the Glucose Management Indicator (GMI)</h2>
        <p>
          With the rapid clinical proliferation of continuous glucose monitoring (CGM) sensor technology, modern diabetology increasingly integrates interstitial sensor readings alongside venipuncture HbA1c. The international consensus on Continuous Glucose Monitoring metrics establishes <strong>Time-in-Range (TIR, 70 to 180 mg/dL or 3.9 to 10.0 mmol/L)</strong> as a primary clinical outcome target. For most non-pregnant adults with type 1 or type 2 diabetes, guidelines recommend a TIR exceeding 70%, with less than 4% of readings in hypoglycemia (&lt; 70 mg/dL) and less than 1% in severe hypoglycemia (&lt; 54 mg/dL).
        </p>
        <p>
          CGM software generates an estimated metric termed the <strong>Glucose Management Indicator (GMI)</strong>, calculated from at least 14 consecutive days of sensor data:
        </p>
        <div class="formula-box">
          <p><strong>Glucose Management Indicator (GMI) Equation:</strong></p>
          $$GMI\text{ (\%)} = 3.31 + (0.02392 \times \text{Mean Sensor Glucose in mg/dL})$$
          $$GMI\text{ (mmol/mol)} = 12.71 + (4.70587 \times \text{Mean Sensor Glucose in mmol/L})$$
        </div>
        <p>
          Clinicians frequently observe discordance between laboratory HbA1c and CGM-derived GMI. This divergence—termed the Glycation Gap or Hemoglobin Glycation Index (HGI)—reflects inter-individual differences in intracellular erythrocyte glucose transport, red cell deglycating enzymatic activity (fructosamine-3-kinase), and variations in average red blood cell lifespan. When HbA1c is clinically uninterpretable, alternative intermediate-term glycemic biomarkers such as <strong>serum fructosamine</strong> (reflecting glycated serum total protein over 2 to 3 weeks) or <strong>glycated albumin</strong> (reflecting glycemia over 14 to 21 days) offer invaluable diagnostic clarity.
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
    function toggleInputMode() {
      const mode = document.getElementById('input-mode').value;
      const label = document.getElementById('label-val');
      const hint = document.getElementById('hint-val');
      const input = document.getElementById('a1c-val');

      if (mode === 'ngsp') {
        label.innerText = 'Hemoglobin A1c Level (%)';
        hint.innerText = 'Clinical diagnostic range: 4.0% to 15.0%';
        input.value = '7.0';
        input.min = '3.5';
        input.max = '20.0';
        input.step = '0.1';
      } else if (mode === 'ifcc') {
        label.innerText = 'IFCC Standard Units (mmol/mol)';
        hint.innerText = 'Standard laboratory reporting: 20 to 140 mmol/mol';
        input.value = '53';
        input.min = '15';
        input.max = '195';
        input.step = '1';
      } else if (mode === 'eag_mg') {
        label.innerText = 'Estimated Average Glucose (mg/dL)';
        hint.innerText = 'Daily average glucose: 70 to 380 mg/dL';
        input.value = '154';
        input.min = '50';
        input.max = '500';
        input.step = '1';
      } else if (mode === 'eag_mmol') {
        label.innerText = 'Estimated Average Glucose (mmol/L)';
        hint.innerText = 'Daily average glucose: 3.9 to 21.0 mmol/L';
        input.value = '8.6';
        input.min = '2.8';
        input.max = '28.0';
        input.step = '0.1';
      }
      calculateA1C();
    }

    function calculateA1C() {
      const mode = document.getElementById('input-mode').value;
      const val = parseFloat(document.getElementById('a1c-val').value) || 0;
      let a1c_pct = 0;

      if (mode === 'ngsp') {
        a1c_pct = val;
      } else if (mode === 'ifcc') {
        a1c_pct = (val / 10.929) + 2.15;
      } else if (mode === 'eag_mg') {
        a1c_pct = (val + 46.7) / 28.7;
      } else if (mode === 'eag_mmol') {
        const mg = val * 18.015;
        a1c_pct = (mg + 46.7) / 28.7;
      }

      if (a1c_pct <= 0) return;

      const eag_mg = Math.round(28.7 * a1c_pct - 46.7);
      const eag_mmol = (eag_mg / 18.015).toFixed(1);
      const ifcc = Math.round(10.929 * (a1c_pct - 2.15));

      document.getElementById('res-ngsp').innerText = a1c_pct.toFixed(2) + ' %';
      document.getElementById('res-eag-mg').innerText = eag_mg + ' mg/dL';
      document.getElementById('res-eag-mmol').innerText = eag_mmol + ' mmol/L';
      document.getElementById('res-ifcc').innerText = ifcc + ' mmol/mol';

      const statusEl = document.getElementById('res-status');
      const descEl = document.getElementById('res-status-desc');
      const riskEl = document.getElementById('res-risk-analysis');

      if (a1c_pct < 5.7) {
        statusEl.innerText = 'Normal Healthy Glycemia';
        statusEl.style.color = '#15803d';
        descEl.innerText = 'Non-diabetic physiological range (A1C < 5.7%, eAG < 117 mg/dL)';
        riskEl.innerText = 'Physiologic normal baseline. No diabetes-associated microvascular or macrovascular risk.';
      } else if (a1c_pct < 6.5) {
        statusEl.innerText = 'Pre-Diabetes (Impaired Glucose)';
        statusEl.style.color = '#ca8a04';
        descEl.innerText = 'Elevated progression risk to Type 2 diabetes (5.7% to 6.4%)';
        riskEl.innerText = 'Increased insulin resistance and endothelial stress. Intensive lifestyle intervention (DPP trial protocol) reduces progression rate by 58%.';
      } else if (a1c_pct <= 7.0) {
        statusEl.innerText = 'Controlled Diabetic Target';
        statusEl.style.color = '#0284c7';
        descEl.innerText = 'Meets American Diabetes Association adult glycemic benchmark (≤ 7.0%)';
        riskEl.innerText = 'Optimal glycemic control halts progressive microvascular diabetic nephropathy and retinopathy. Minimal hypoglycemia risk if on metformin or GLP-1.';
      } else if (a1c_pct <= 8.5) {
        statusEl.innerText = 'Suboptimal Diabetic Control';
        statusEl.style.color = '#ea580c';
        descEl.innerText = 'Elevated mean blood glucose requiring medical evaluation (7.1% to 8.5%)';
        riskEl.innerText = 'Excess chronic microvascular risk. UKPDS showed each 1% reduction in A1C yields a 37% risk reduction in microvascular disease and 14% in myocardial infarction.';
      } else {
        statusEl.innerText = 'Severe Hyperglycemia';
        statusEl.style.color = '#dc2626';
        descEl.innerText = 'Critically high average glucose (> 8.5%, eAG > 200 mg/dL)';
        riskEl.innerText = 'Acute risk for hyperosmolar state, symptomatic polyuria, and aggressive microvascular complications. Urgent clinical pharmacotherapy titration recommended.';
      }
    }

    document.addEventListener('DOMContentLoaded', calculateA1C);
  </script>
</body>
</html>
"""

# -------------------------------------------------------------
# 2. bac-calculator.html
# -------------------------------------------------------------
BAC_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BAC Calculator | Blood Alcohol Concentration & Widmark Clearance</title>
  <meta name="description" content="Calculate your Blood Alcohol Concentration (BAC) and estimated sobriety time using the scientific Widmark formula, body mass distribution, and liver clearance rate.">
  <link rel="canonical" href="https://calchub.com/bac-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Widmark Blood Alcohol Concentration (BAC) Calculator",
    "applicationCategory": "HealthApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0.00",
      "priceCurrency": "USD"
    },
    "description": "Forensic toxicological calculator estimating Blood Alcohol Concentration (BAC) and time to legal sobriety (0.00% and 0.08%) using the Widmark equation."
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is the Widmark formula used to calculate Blood Alcohol Concentration?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Widmark equation is: BAC = [A / (r × W) × 100] - (β × t), where A is pure alcohol consumed in grams, W is body weight in grams, r is the gender-specific volume of distribution (0.68 for biological males, 0.55 for females), β is the metabolic elimination rate (typically 0.015% per hour), and t is time elapsed in hours since drinking started."
        }
      },
      {
        "@type": "Question",
        "name": "How much pure alcohol is in one standard US drink?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "In the United States, a standard drink contains exactly 14.0 grams (0.6 fluid ounces or 17.7 mL) of pure ethanol. This corresponds to 12 fluid ounces of regular 5% ABV beer, 5 fluid ounces of 12% ABV table wine, or 1.5 fluid ounces of 40% ABV (80-proof) distilled spirits."
        }
      },
      {
        "@type": "Question",
        "name": "How fast does the human body metabolize and eliminate alcohol?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The human liver eliminates alcohol through zero-order kinetics at an average rate (β factor) of 0.015 g/dL per hour (ranging between 0.012% and 0.020%/hr). Neither black coffee, cold showers, exercise, nor sleep can accelerate this hepatic enzymatic clearance rate."
        }
      },
      {
        "@type": "Question",
        "name": "What are the physiological symptoms associated with different BAC levels?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "At 0.02-0.03%, mild euphoria and relaxation occur; at 0.05%, judgment and reaction time degrade; at 0.08% (statutory legal DUI limit in the US), gross motor coordination and peripheral vision are impaired; at 0.15%, significant balance loss and nausea occur; and at ≥ 0.30%, severe central nervous system depression, loss of consciousness, and life-threatening respiratory arrest can ensue."
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
        <div class="badge-tag">Forensic Toxicology</div>
        <h1 class="calculator-title">Blood Alcohol Concentration (BAC) Calculator</h1>
        <p class="calculator-description">Calculate your estimated Blood Alcohol Concentration (BAC) and time to legal sobriety using the peer-reviewed Widmark pharmacokinetics formula and hepatic elimination models.</p>
      </div>

      <div class="calculator-grid">
        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Consumption & Physiology Inputs</h2>
          </div>
          <div class="calc-card-body">
            <div class="form-group">
              <label for="gender" class="form-label">Biological Sex (Volume of Distribution)</label>
              <select id="gender" class="form-select" onchange="calculateBAC()">
                <option value="male" selected>Male (r = 0.68 - Higher lean muscle mass)</option>
                <option value="female">Female (r = 0.55 - Higher body water distribution ratio)</option>
              </select>
            </div>

            <div class="form-row" style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
              <div class="form-group">
                <label for="body-weight" class="form-label">Body Weight</label>
                <input type="number" id="body-weight" class="form-input" value="180" min="80" max="450" step="1" oninput="calculateBAC()">
              </div>
              <div class="form-group">
                <label for="weight-unit" class="form-label">Unit</label>
                <select id="weight-unit" class="form-select" onchange="calculateBAC()">
                  <option value="lbs" selected>Pounds (lbs)</option>
                  <option value="kg">Kilograms (kg)</option>
                </select>
              </div>
            </div>

            <div class="form-group">
              <label for="standard-drinks" class="form-label">Number of Standard Drinks Consumed</label>
              <input type="number" id="standard-drinks" class="form-input" value="3.0" min="0" max="25" step="0.5" oninput="calculateBAC()">
              <span class="form-hint">1 Standard Drink = 12 oz 5% beer = 5 oz 12% wine = 1.5 oz 40% spirits (14g alcohol)</span>
            </div>

            <div class="form-row" style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
              <div class="form-group">
                <label for="drinking-hours" class="form-label">Drinking Duration (Hours)</label>
                <input type="number" id="drinking-hours" class="form-input" value="2.0" min="0.25" max="24" step="0.25" oninput="calculateBAC()">
              </div>
              <div class="form-group">
                <label for="beta-rate" class="form-label">Metabolic Rate (β / hr)</label>
                <select id="beta-rate" class="form-select" onchange="calculateBAC()">
                  <option value="0.015" selected>Average (0.015% / hr)</option>
                  <option value="0.012">Slow Metabolism (0.012% / hr)</option>
                  <option value="0.018">Fast Metabolism (0.018% / hr)</option>
                </select>
              </div>
            </div>

            <button type="button" class="btn btn-primary" onclick="calculateBAC()">Calculate Blood Alcohol & Clearance</button>
          </div>
        </div>

        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">BAC Analysis & Sobriety Forecast</h2>
          </div>
          <div class="calc-card-body">
            <div class="result-hero" id="bac-hero" style="background:#fef2f2;border-color:#fecaca;">
              <span class="hero-label">Estimated Current Blood Alcohol</span>
              <div class="hero-value" id="res-bac" style="color:#b91c1c;font-size:2.4rem;">0.045 %</div>
              <span class="form-hint" id="res-bac-status" style="font-weight:600;">Legally Safe in US (Under 0.08% Limit), But Impaired</span>
            </div>

            <div class="results-grid" style="margin-top:1.5rem;">
              <div class="result-item">
                <span class="result-label">Peak Theoretical BAC</span>
                <span class="result-value" id="res-peak-bac">0.075 %</span>
              </div>
              <div class="result-item">
                <span class="result-label">Pure Alcohol Consumed</span>
                <span class="result-value" id="res-grams-alcohol">42.0 g</span>
              </div>
              <div class="result-item">
                <span class="result-label">Time to Legal Limit (0.08%)</span>
                <span class="result-value" id="res-time-legal">0.0 Hours</span>
              </div>
              <div class="result-item">
                <span class="result-label">Time to Full Sobriety (0.00%)</span>
                <span class="result-value" id="res-time-zero">3.0 Hours</span>
              </div>
            </div>

            <div class="stat-box" style="margin-top:1.5rem;padding:1rem;background:#f8fafc;border-radius:8px;border:1px solid #e2e8f0;">
              <h4 style="font-weight:700;margin-bottom:0.5rem;font-size:0.95rem;">Physiological & Cognitive Effects:</h4>
              <p id="res-symptoms" style="font-size:0.875rem;color:#475569;margin:0;">
                Mild impairment of divided attention, slight exaggeration of emotions, minor reduction in ocular tracking and reaction times.
              </p>
            </div>
          </div>
        </div>
      </div>

      <article class="article-body">
        <h2>Pharmacokinetics of Alcohol Absorption and Metabolism</h2>
        <p>
          Ethanol ($C_2H_5OH$) is a low-molecular-weight, water-soluble alcohol that rapidly permeates biological membranes via passive diffusion. When ingested, alcohol is not chemically digested like carbohydrates, proteins, or lipids. Approximately 20% is absorbed directly through the gastric mucosa of the stomach, while the remaining 80% is absorbed in the upper small intestine, primarily through the highly vascularized duodenal and jejunal villi.
        </p>
        <p>
          The rate of gastric emptying is the dominant factor dictating peak blood alcohol concentration. In the presence of a full meal containing dietary fats and fibrous proteins, the pyloric sphincter remains constricted to allow mechanical churning, delaying gastric emptying and flattening the systemic absorption curve. On an empty stomach, rapid transit into the duodenum produces peak systemic blood concentrations within 30 to 45 minutes of consumption.
        </p>

        <h2>The Classic Widmark Pharmacokinetic Equation</h2>
        <p>
          In 1932, Swedish physician and forensic chemist <strong>Erik M. P. Widmark</strong> formulated the fundamental mathematical model governing human alcohol pharmacokinetics. The model treats the human body as a single-compartment open system where ethanol distributes into total body water:
        </p>

        <div class="formula-box">
          <p><strong>The Widmark Equation:</strong></p>
          $$BAC\text{ (\% g/dL)} = \left[ \frac{A}{r \times W} \times 100 \right] - (\beta \times t)$$
          <p>Where:</p>
          <ul>
            <li><strong>A:</strong> Total mass of pure ethanol ingested (in grams). One US standard drink contains exactly 14.0 grams of ethanol ($A = \text{drinks} \times 14.0\text{ g}$).</li>
            <li><strong>W:</strong> Total body weight in grams ($1\text{ lb} \approx 453.592\text{ g}$; $1\text{ kg} = 1000\text{ g}$).</li>
            <li><strong>r:</strong> Widmark's rho factor (reduced body mass or volume of distribution), reflecting the fraction of body mass consisting of water. Widmark empirically established $r = 0.68 \pm 0.08$ for biological men and $r = 0.55 \pm 0.05$ for biological women.</li>
            <li><strong>&beta; (Beta):</strong> The zero-order elimination rate constant of ethanol clearance, governed by hepatic alcohol dehydrogenase saturation, typically $0.015\text{ g/dL/hr}$ ($0.015\%/\text{hr}$).</li>
            <li><strong>t:</strong> Total time elapsed in hours from the start of alcohol ingestion.</li>
          </ul>
        </div>

        <h2>Biological Sex Differences in Alcohol Distribution</h2>
        <p>
          The substantial divergence in the $r$ distribution factor between males ($0.68$) and females ($0.55$) arises from two distinct physiological phenomena:
        </p>
        <ol>
          <li><strong>Body Composition and Total Body Water (TBW):</strong> Ethanol is highly polar and water-soluble; it does not partition into lipid storage tissue (adipose). Because adult females possess on average a higher proportion of essential and subcutaneous body fat and a lower percentage of lean skeletal muscle mass than biological males, their total body water volume is roughly 10% to 15% lower per unit of body weight. Identical ethanol doses in equal-weight individuals therefore yield a substantially higher blood concentration in females.</li>
          <li><strong>First-Pass Hepatic and Gastric Metabolism:</strong> The gastric mucosa synthesizes gastric alcohol dehydrogenase (ADH) enzymes, which oxidize a modest fraction of ingested ethanol prior to portal circulation. Women have significantly lower gastric ADH activity than men, allowing a larger percentage of ingested alcohol to reach the systemic circulation untouched.</li>
        </ol>

        <h2>Zero-Order Hepatic Clearance and Elimination Kinetics</h2>
        <p>
          More than 90% of circulating ethanol is metabolized in the hepatocytes of the liver through sequential oxidation pathways:
        </p>
        $$C_2H_5OH + NAD^+ \xrightarrow{\text{Alcohol Dehydrogenase (ADH)}} CH_3CHO\text{ (Acetaldehyde)} + NADH + H^+$$
        $$CH_3CHO + NAD^+ + H_2O \xrightarrow{\text{Aldehyde Dehydrogenase (ALDH)}} CH_3COOH\text{ (Acetate)} + NADH + H^+$$
        <p>
          The primary rate-limiting enzyme, cytosolic alcohol dehydrogenase (ADH), exhibits a low Michaelis constant ($K_m \approx 0.05\text{ to }0.1\text{ g/L}$ or $0.005\text{ to }0.010\text{ g/dL}$). Consequently, even at very modest blood alcohol concentrations ($BAC > 0.02\%$), the enzyme becomes entirely saturated. The clearance reaction therefore follows <strong>zero-order kinetics</strong>: the liver oxidizes a constant absolute quantity of alcohol per unit time, regardless of whether the BAC is 0.05% or 0.25%. The universal population average clearance rate is $\beta = 0.015\%\text{ per hour}$ (approximately one standard drink metabolized every 60 to 90 minutes).
        </p>

        <h2>Clinical and Legal BAC Benchmark Reference Table</h2>
        <p>
          The following reference table outlines physiological impairment, cognitive deficits, and legal implications across the spectrum of Blood Alcohol Concentrations:
        </p>

        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>BAC Range (%)</th>
                <th>Standard Drink Equivalent (180 lb Male)</th>
                <th>Neurological &amp; Physiological Symptoms</th>
                <th>Driving Impairment Severity</th>
                <th>Legal Classification</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>0.00% – 0.03%</strong></td>
                <td>1 drink</td>
                <td>Mild pleasant relaxation, slight elevation in mood, subtle warming sensation.</td>
                <td>Minor decline in rapid visual tracking; statistically slight risk increase.</td>
                <td>Legally unimpaired (adult non-commercial drivers).</td>
              </tr>
              <tr>
                <td><strong>0.04% – 0.07%</strong></td>
                <td>2 – 3 drinks</td>
                <td>Release of inhibitions, mild motor coordination loss, lowered alertness.</td>
                <td>Significant reduction in reaction time, emergency braking distance lengthened.</td>
                <td>Commercial driver violation limit in US (0.04%); impaired driving.</td>
              </tr>
              <tr>
                <td><strong>0.08% – 0.12%</strong></td>
                <td>4 – 5 drinks</td>
                <td>Clear motor ataxia, slurred speech, impaired reasoning and short-term memory.</td>
                <td>Severe loss of peripheral vision, inability to maintain lane position.</td>
                <td><strong>Per Se Statutory DUI/DWI Violation in all 50 US States</strong>.</td>
              </tr>
              <tr>
                <td><strong>0.13% – 0.19%</strong></td>
                <td>6 – 8 drinks</td>
                <td>Gross loss of motor control, vestibular disturbance, dysphoria, nausea.</td>
                <td>Extreme danger; 25-fold to 50-fold elevated crash probability.</td>
                <td>Aggravated DUI / felony reckless endangerment jurisdiction.</td>
              </tr>
              <tr>
                <td><strong>0.20% – 0.29%</strong></td>
                <td>9 – 12 drinks</td>
                <td>Profound stupor, amnesia (blackout), severe vomiting risk, sensory blunting.</td>
                <td>Complete operational incapacity.</td>
                <td>Severe acute alcohol intoxication; medical supervision needed.</td>
              </tr>
              <tr>
                <td><strong>&ge; 0.30%</strong></td>
                <td>13+ drinks</td>
                <td>Coma, loss of protective airway reflexes, hypothermia, respiratory arrest.</td>
                <td>Fatal poisoning threshold.</td>
                <td>Potentially fatal medical emergency; intensive care required.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2>Worked Forensic Calculation Example</h2>
        <div class="worked-example-card">
          <div class="example-header">
            <span class="example-badge">Toxicology Case Study</span>
            <h3 class="example-title">Social Gathering DUI Threshold Assessment</h3>
          </div>
          <div class="example-step">
            <div class="step-num">1</div>
            <div class="step-content">
              <strong>Scenario Parameters:</strong> A 160-pound (72.57 kg) biological male consumes 4 pints of craft IPA beer (each pint 16 oz at 6.5% ABV) over a 3.0-hour dinner. The investigator must calculate his current BAC and determine when he will reach the legal driving threshold (0.08%) and full sobriety (0.00%).
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">2</div>
            <div class="step-content">
              <strong>Calculate Total Pure Alcohol Mass (A):</strong>
              $$\text{Volume} = 4 \times 16\text{ oz} = 64\text{ oz} \approx 1892.7\text{ mL}$$
              $$\text{Pure Ethanol Volume} = 1892.7\text{ mL} \times 0.065 = 123.03\text{ mL}$$
              $$\text{Pure Ethanol Mass } (A) = 123.03\text{ mL} \times 0.789\text{ g/mL} = 97.07\text{ grams of alcohol}$$
              (Equivalent to $97.07 / 14.0 = 6.93\text{ US standard drinks}$.)
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">3</div>
            <div class="step-content">
              <strong>Calculate Body Weight in Grams and Peak Theoretical BAC:</strong>
              $$W = 160\text{ lbs} \times 453.592\text{ g/lb} = 72,575\text{ grams}$$
              $$r\text{ (male)} = 0.68 \implies r \times W = 0.68 \times 72,575 = 49,351\text{ g}$$
              $$\text{Theoretical Peak BAC} = \frac{97.07}{49,351} \times 100 = 0.1967\%$$
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">4</div>
            <div class="step-content">
              <strong>Account for Metabolic Elimination Over 3 Hours:</strong>
              $$\text{Elimination} = \beta \times t = 0.015\%/\text{hr} \times 3.0\text{ hrs} = 0.0450\%$$
              $$\text{Current BAC} = 0.1967\% - 0.0450\% = \mathbf{0.1517\%}$$
              $$\text{Time to Legal 0.08\%} = \frac{0.1517 - 0.08}{0.015} = \frac{0.0717}{0.015} = \mathbf{4.78\text{ hours}}$$
              $$\text{Time to Complete Sobriety (0.00\%)} = \frac{0.1517}{0.015} = \mathbf{10.11\text{ hours}}$$
            </div>
          </div>
        </div>

        <h2>Common Myths and Clinical Realities</h2>
        <p>
          Forensic toxicology consistently refutes persistent cultural misconceptions regarding alcohol sobriety:
        </p>
        <ul>
          <li><strong>Caffeine and Cold Showers:</strong> Caffeine acts as an adenosine receptor antagonist that masks perceived drowsiness, creating an illusion of alertness termed "wide-awake drunk." However, caffeine has zero effect on hepatic alcohol dehydrogenase kinetics. BAC remains completely identical, while motor reaction speed remains dangerously impaired.</li>
          <li><strong>Breathalyzer Partition Ratio Variability:</strong> Breath alcohol analyzers (Evidential Breath Testers) measure alcohol vapor in deep alveolar breath and multiply by an assumed statutory blood-to-breath partition ratio of $2,100:1$. In the general population, true physiological ratios range from $1,800:1$ to $2,400:1$. Body temperature elevation (fever) and hematocrit variations alter Henry's Law equilibrium in alveolar air, potentially introducing a 5% to 10% variance.</li>
          <li><strong>Sleep and Metabolism:</strong> During deep sleep, gastrointestinal motility slows, and metabolic rates drop marginally. If significant alcohol remains unabsorbed in the stomach before sleep, the morning-after BAC may be surprisingly elevated as residual alcohol continues to enter circulation.</li>
        </ul>
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
    function calculateBAC() {
      const gender = document.getElementById('gender').value;
      const r = (gender === 'male') ? 0.68 : 0.55;

      let weight = parseFloat(document.getElementById('body-weight').value) || 0;
      const unit = document.getElementById('weight-unit').value;
      if (unit === 'lbs') {
        weight = weight * 453.592; // grams
      } else {
        weight = weight * 1000; // grams
      }

      const drinks = parseFloat(document.getElementById('standard-drinks').value) || 0;
      const alcoholGrams = drinks * 14.0; // 14g per US standard drink

      const hours = parseFloat(document.getElementById('drinking-hours').value) || 0;
      const beta = parseFloat(document.getElementById('beta-rate').value) || 0.015;

      if (weight <= 0) return;

      const peakBAC = (alcoholGrams / (r * weight)) * 100;
      const eliminated = beta * hours;
      let currentBAC = peakBAC - eliminated;
      if (currentBAC < 0) currentBAC = 0;

      document.getElementById('res-bac').innerText = currentBAC.toFixed(3) + ' %';
      document.getElementById('res-peak-bac').innerText = peakBAC.toFixed(3) + ' %';
      document.getElementById('res-grams-alcohol').innerText = alcoholGrams.toFixed(1) + ' g';

      // Time to 0.08%
      let timeToLegal = 0;
      if (currentBAC > 0.08) {
        timeToLegal = (currentBAC - 0.08) / beta;
      }
      document.getElementById('res-time-legal').innerText = timeToLegal.toFixed(1) + ' Hours';

      // Time to 0.00%
      let timeToZero = 0;
      if (currentBAC > 0) {
        timeToZero = currentBAC / beta;
      }
      document.getElementById('res-time-zero').innerText = timeToZero.toFixed(1) + ' Hours';

      // Hero UI updates
      const hero = document.getElementById('bac-hero');
      const valEl = document.getElementById('res-bac');
      const statusEl = document.getElementById('res-bac-status');
      const sympEl = document.getElementById('res-symptoms');

      if (currentBAC === 0) {
        hero.style.background = '#f0fdf4';
        hero.style.borderColor = '#bbf7d0';
        valEl.style.color = '#15803d';
        statusEl.innerText = 'Sober (0.00% BAC) - Completely Unimpaired';
        sympEl.innerText = 'Normal baseline cognitive and neuromuscular function. Fully legal for all motor vehicle operation.';
      } else if (currentBAC < 0.04) {
        hero.style.background = '#fefce8';
        hero.style.borderColor = '#fef08a';
        valEl.style.color = '#ca8a04';
        statusEl.innerText = 'Mild Influence - Below Legal Limit';
        sympEl.innerText = 'Subtle relaxation and warmth. Minor loss of divided attention and minor increase in risk-taking.';
      } else if (currentBAC < 0.08) {
        hero.style.background = '#fff7ed';
        hero.style.borderColor = '#fed7aa';
        valEl.style.color = '#ea580c';
        statusEl.innerText = 'Impaired - Approaching Legal DUI Threshold';
        sympEl.innerText = 'Noticeable reduction in reaction time, tracking moving targets, and steering control. Driving is unsafe.';
      } else if (currentBAC < 0.15) {
        hero.style.background = '#fef2f2';
        hero.style.borderColor = '#fecaca';
        valEl.style.color = '#b91c1c';
        statusEl.innerText = 'ILLEGAL (DUI / DWI Violation) - Major Impairment';
        sympEl.innerText = 'Statutory DUI threshold in all US states. Gross lack of muscular coordination, balance loss, substantially increased accident risk.';
      } else {
        hero.style.background = '#450a0a';
        hero.style.borderColor = '#991b1b';
        valEl.style.color = '#fca5a5';
        statusEl.innerText = 'SEVERE INTOXICATION - Acute Danger';
        statusEl.style.color = '#fecaca';
        sympEl.innerText = 'Blackout risk, loss of motor control, vomiting, risk of respiratory depression and alcohol poisoning. Medical evaluation required.';
      }
    }

    document.addEventListener('DOMContentLoaded', calculateBAC);
  </script>
</body>
</html>
"""

def generate_part1():
    with open(os.path.join(BASE_DIR, "a1c-calculator.html"), "w", encoding="utf-8") as f:
        f.write(A1C_HTML)
    print("Generated a1c-calculator.html")

    with open(os.path.join(BASE_DIR, "bac-calculator.html"), "w", encoding="utf-8") as f:
        f.write(BAC_HTML)
    print("Generated bac-calculator.html")

if __name__ == "__main__":
    generate_part1()
