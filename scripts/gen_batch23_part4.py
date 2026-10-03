"""
Batch 23 - Part 4: Health & Fitness Tools
7. waist-to-height-ratio-calculator.html (WHtR Clinical Diagnostic Engine, ROC AUC Meta-Analyses, NCEP ATP III & Pediatric Screening)
8. waist-to-hip-ratio-calculator.html (WHR, WHO 0.90/0.85 Cutoffs, Android vs Gynoid Obesity, INTERHEART Study & Greater Trochanter Protocol)
Word count target: >1,100 words in article-body each.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 7. waist-to-height-ratio-calculator.html
# -------------------------------------------------------------
WAIST_HEIGHT_RATIO_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Waist-to-Height Ratio Calculator | Clinical Cardiometabolic Screening</title>
  <meta name="description" content="Calculate your exact Waist-to-Height Ratio (WHtR) to assess central visceral adiposity, metabolic syndrome risk, and cardiovascular health per NICE guidelines.">
  <link rel="canonical" href="https://calchub.com/waist-to-height-ratio-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Clinical Waist-to-Height Ratio Screening Calculator",
    "applicationCategory": "HealthApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0.00",
      "priceCurrency": "USD"
    },
    "description": "Calculates prospective Waist-to-Height Ratio (WHtR), evaluates visceral fat burden, and stratifies cardiometabolic and type 2 diabetes risk according to NICE 2022 standards."
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is the Waist-to-Height Ratio (WHtR) and why is 0.50 the universal cutoff?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Waist-to-Height Ratio (WHtR) is an anthropometric measure obtained by dividing waist circumference by standing height. A value of 0.50 ('keep your waist to less than half your height') serves as the global clinical boundary for visceral adiposity. Crossing 0.50 indicates excess intra-abdominal fat surrounding vital organs, significantly elevating risks for type 2 diabetes, hypertension, and coronary artery disease."
        }
      },
      {
        "@type": "Question",
        "name": "How does the ROC Area Under the Curve (AUC) of WHtR compare to BMI?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "In a comprehensive meta-analysis of over 300,000 subjects across diverse ethnicities by Browning et al., WHtR demonstrated statistically superior Receiver Operating Characteristic (ROC) Area Under the Curve (AUC = 0.704) for discriminating cardiovascular disease, diabetes, and metabolic syndrome compared to traditional Body Mass Index (AUC = 0.671)."
        }
      },
      {
        "@type": "Question",
        "name": "Can WHtR detect the 'Normal Weight Obese' (TOFI) phenotype?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. Individuals with the TOFI ('Thin on the Outside, Fat on the Inside') or Normal-Weight Obese phenotype have a normal BMI (<25 kg/m²) but harbor dangerous amounts of deep visceral fat around the liver and mesentery. While BMI falsely misclassifies them as healthy, their WHtR exceeds 0.50, correctly identifying their atherogenic dyslipidemia and insulin resistance."
        }
      },
      {
        "@type": "Question",
        "name": "Does the WHtR 0.50 cutoff apply to children and teenagers?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. Unlike pediatric BMI which requires complex age- and sex-stratified z-score growth curves, the 0.50 WHtR cutoff accurately identifies excess central adiposity in children and adolescents aged 5 and older. Studies from the Bogalusa Heart Study confirm that children with a WHtR ≥ 0.50 have significantly higher rates of childhood hypertension and dyslipidemia."
        }
      },
      {
        "@type": "Question",
        "name": "How does WHtR relate to the Metabolic Syndrome (MetSyn) criteria?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The National Cholesterol Education Program (NCEP ATP III) and International Diabetes Federation (IDF) identify central abdominal obesity as the primary driver of Metabolic Syndrome. An elevated WHtR directly correlates with the five hallmark criteria: elevated fasting glucose, hypertriglyceridemia, reduced HDL-C, elevated blood pressure, and central adiposity."
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
        <li class="active">Waist-to-Height Ratio Calculator</li>
      </ol>
    </nav>

    <div class="page-layout">
      <div class="calculator-container">
        <div class="calculator-card">
          <h1 class="calculator-title">Clinical Waist-to-Height Ratio (WHtR) Calculator</h1>
          <p class="calculator-subtitle">Screen for central visceral adiposity, metabolic syndrome risk, and evaluate your health against the Ashwell Shape Chart and NICE 2022 guidelines.</p>

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
                  <input type="number" id="height-inches" class="form-input" min="0" max="11" value="10" required>
                </div>
              </div>
              <div class="form-group">
                <label for="waist-inches" class="form-label">Waist Circumference (Inches)</label>
                <input type="number" id="waist-inches" class="form-input" min="15" max="80" value="34" step="0.25" required>
                <small class="form-hint">Measure at the midpoint between the lower rib margin and superior iliac crest.</small>
              </div>
            </div>

            <!-- Metric Inputs -->
            <div id="metric-inputs-group" style="display: none;">
              <div class="form-group">
                <label for="height-cm" class="form-label">Height (Centimeters)</label>
                <input type="number" id="height-cm" class="form-input" min="100" max="240" value="178" step="0.5">
              </div>
              <div class="form-group">
                <label for="waist-cm" class="form-label">Waist Circumference (Centimeters)</label>
                <input type="number" id="waist-cm" class="form-input" min="40" max="200" value="86" step="0.5">
              </div>
            </div>

            <button type="submit" class="calculate-btn">Compute WHtR &amp; Health Risk</button>
          </form>

          <div id="calculator-results" class="results-container" style="display: none;">
            <h2 class="results-heading">Cardiometabolic Risk Profile</h2>

            <div class="results-grid">
              <div class="result-card primary-result">
                <span class="result-label">Waist-to-Height Ratio</span>
                <span id="res-whtr-value" class="result-value">--</span>
                <span id="res-whtr-status" class="result-subtext badge-tag">Healthy</span>
              </div>

              <div class="result-card highlight-card">
                <span class="result-label">Clinical Health Risk Tier</span>
                <span id="res-risk-tier" class="result-value">--</span>
                <span class="result-subtext">NICE 2022 clinical classification</span>
              </div>

              <div class="result-card">
                <span class="result-label">Maximum Healthy Waist Limit</span>
                <span id="res-max-waist" class="result-value">--</span>
                <span class="result-subtext">Exactly 50% of your standing height</span>
              </div>

              <div class="result-card">
                <span class="result-label">Variance from 0.50 Target</span>
                <span id="res-variance-val" class="result-value">--</span>
                <span id="res-variance-label" class="result-subtext">Margin</span>
              </div>

              <div class="result-card">
                <span class="result-label">Ashwell Shape Classification</span>
                <span id="res-shape-class" class="result-value">--</span>
                <span class="result-subtext">Body shape category</span>
              </div>

              <div class="result-card">
                <span class="result-label">Ideal Waist Range</span>
                <span id="res-ideal-band" class="result-value">--</span>
                <span class="result-subtext">WHtR between 0.40 and 0.49</span>
              </div>
            </div>

            <div class="summary-box mt-4">
              <h3 class="summary-title">Preventive Medical Evaluation</h3>
              <p id="res-clinical-summary" class="summary-text">Loading cardiometabolic analysis...</p>
            </div>
          </div>
        </div>
      </div>

      <aside class="sidebar">
        <div class="sidebar-card">
          <h3 class="sidebar-title">Body Composition Tools</h3>
          <ul class="sidebar-list">
            <li><a href="waist-to-hip-ratio-calculator.html">Waist to Hip Ratio Calculator</a></li>
            <li><a href="waist-to-height-calculator.html">Waist to Height Sizer</a></li>
            <li><a href="bmi-calculator.html">BMI Calculator</a></li>
            <li><a href="body-fat-calculator.html">Body Fat Calculator</a></li>
            <li><a href="calorie-deficit-calculator.html">Calorie Deficit Calculator</a></li>
          </ul>
        </div>
        <div class="sidebar-card mt-4">
          <h3 class="sidebar-title">Clinical Standards</h3>
          <p class="sidebar-text">Based on the UK National Institute for Health and Care Excellence (NICE 2022), systematic reviews by Browning et al., and the Ashwell Shape Chart framework.</p>
        </div>
      </aside>
    </div>

    <article class="article-body">
      <h2>The Epidemiological Superiority of Waist-to-Height Ratio (WHtR)</h2>
      <p>For more than a century, clinical medicine and public health policy relied almost exclusively on Adolphe Quetelet's 1832 Body Mass Index ($BMI = kg/m^2$) to evaluate human adiposity. However, modern endocrinology and cardiovascular pathophysiology have revealed that total body mass is an unreliable surrogate for cardiometabolic disease. <strong>Waist-to-Height Ratio (WHtR)</strong> has emerged as the premier evidence-based anthropometric indicator because it directly quantifies <strong>central intra-abdominal visceral adiposity</strong>, bypassing the inherent geometric and compositional limitations of scale weight.</p>

      <p>In a landmark systematic review and meta-analysis published in <em>Obesity Reviews</em> by Dr. Lynne Browning and colleagues evaluating over <strong>300,000 adult subjects across diverse international cohorts</strong>, the diagnostic discriminative capability of anthropometric indices was rigorously quantified using Receiver Operating Characteristic (ROC) Area Under the Curve (AUC) statistical modeling:</p>

      $$\text{ROC AUC for Type 2 Diabetes & Cardiovascular Outcomes:}$$
      $$\text{WHtR: } 0.704 \quad [95\% \text{ CI: } 0.697 - 0.711]$$
      $$\text{Waist Circumference (WC): } 0.693 \quad [95\% \text{ CI: } 0.686 - 0.700]$$
      $$\text{Body Mass Index (BMI): } 0.671 \quad [95\% \text{ CI: } 0.664 - 0.678]$$

      <p>The statistical superiority of WHtR was statistically significant ($p < 0.001$) across all evaluated cardiometabolic endpoints, confirming that dividing waist circumference by height provides superior clinical risk stratification compared to both BMI and unadjusted waist circumference.</p>

      <h2>Mathematical Formulation and the Universal 0.50 Boundary</h2>
      <p>The Waist-to-Height Ratio is a pure, dimensionless mathematical ratio:</p>

      $$WHtR = \frac{\text{Waist Circumference}}{\text{Height}}$$

      <p>The universal clinical guideline established by Dr. Margaret Ashwell and endorsed by the UK National Institute for Health and Care Excellence (NICE 2022) is structured around the 0.50 boundary:</p>

      $$\mathbf{WHtR < 0.50} \iff \text{Waist Circumference } < 0.50 \times \text{Height}$$

      <div class="table-container my-4">
        <table class="data-table">
          <thead>
            <tr>
              <th>WHtR Boundary Range</th>
              <th>NICE 2022 Health Classification</th>
              <th>Ashwell Shape Tier</th>
              <th>Visceral Adipose Burden</th>
              <th>Cardiometabolic Mortality Relative Risk</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>&lt; 0.40</strong></td>
              <td>Below Optimal (Underweight)</td>
              <td>"Take Care" / Slim</td>
              <td>Low visceral fat, potentially depleted fat-free mass and nutrient reserves.</td>
              <td>Elevated non-cardiovascular mortality risk (frailty, respiratory disease).</td>
            </tr>
            <tr>
              <td><strong>0.40 – 0.49</strong></td>
              <td><strong>Healthy Weight (Optimal)</strong></td>
              <td><strong>"No Action" / Healthy</strong></td>
              <td>Minimal deep intra-abdominal visceral adiposity; optimal insulin sensitivity.</td>
              <td><strong>Baseline (Lowest All-Cause &amp; CVD Mortality)</strong>.</td>
            </tr>
            <tr>
              <td><strong>0.50 – 0.59</strong></td>
              <td>Increased Health Risk</td>
              <td>"Consider Action"</td>
              <td>Early visceral fat accumulation; portal free fatty acid flood initiated.</td>
              <td><strong>1.5&times; to 2.0&times;</strong> elevated risk of Type 2 Diabetes &amp; Hypertension.</td>
            </tr>
            <tr>
              <td><strong>&ge; 0.60</strong></td>
              <td>Very High Health Risk</td>
              <td>"Take Action"</td>
              <td>Severe visceral obesity; extensive hepatic steatosis and systemic inflammation.</td>
              <td><strong>3.0&times; to 4.5&times;</strong> elevated risk of T2D, CAD, stroke, and premature death.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Visceral Fat Pathophysiology vs. Subcutaneous Fat</h2>
      <p>The biological explanation for WHtR's clinical predictive power lies in the unique histology and vascular anatomy of <strong>Visceral Adipose Tissue (VAT)</strong> compared to <strong>Subcutaneous Adipose Tissue (SAT)</strong>:</p>
      <ul>
        <li><strong>Portal Venous Drainage &amp; Hepatic Steatosis:</strong> Unlike subcutaneous fat in the hips and thighs (which drains into the systemic vena cava), intra-abdominal visceral adipocytes drain directly into the <strong>hepatic portal venous system</strong>. Visceral fat exhibits high basal lipolysis due to dense $\beta$-adrenergic receptor density and low sensitivity to the anti-lipolytic effects of insulin. This floods the liver with high concentrations of non-esterified free fatty acids (NEFAs), inhibiting hepatic insulin clearance, activating protein kinase C ($\text{PKC-}\epsilon$), and precipitating Non-Alcoholic Fatty Liver Disease (NAFLD).</li>
        <li><strong>Pro-Inflammatory Secretome:</strong> Visceral fat is heavily infiltrated by pro-inflammatory CD8+ T-cells and M1 polarized macrophages that form histologic "crown-like structures" around necrotic adipocytes. These cells secrete inflammatory cytokines into the portal and systemic circulation, including <strong>Tumor Necrosis Factor-alpha ($TNF\text{-}\alpha$)</strong>, <strong>Interleukin-6 ($IL\text{-}6$)</strong>, monocyte chemoattractant protein-1 ($MCP\text{-}1$), and resistin. Concurrently, visceral adiposity downregulates <strong>adiponectin</strong>, an anti-inflammatory, insulin-sensitizing hormone that protects vascular endothelium.</li>
        <li><strong>Atherogenic Dyslipidemia Phenotype:</strong> High portal free fatty acid influx drives excessive hepatic synthesis of large, triglyceride-rich Very-Low-Density Lipoproteins (VLDL). Cholesterol Ester Transfer Protein (CETP) subsequently exchanges VLDL triglycerides for cholesteryl esters in LDL and HDL particles. Hepatic lipase hydrolyzes these triglyceride-enriched particles, creating the lethal <strong>atherogenic lipid triad</strong>: hypertriglyceridemia, low HDL-C, and high concentrations of dense, easily oxidized <strong>small dense LDL (sdLDL)</strong> particles.</li>
      </ul>

      <h2>The UK NICE 2022 Clinical Guidelines Mandate</h2>
      <p>In September 2022, the UK <strong>National Institute for Health and Care Excellence (NICE Clinical Guideline CG189)</strong> issued a groundbreaking update urging healthcare practitioners to prioritize the Waist-to-Height Ratio in clinical practice:</p>
      <ul>
        <li>NICE explicitly recommends that adults with a BMI under 35 kg/m&sup2; measure their waist-to-height ratio to determine central adiposity.</li>
        <li>NICE highlights that WHtR resolves ethnic disparities, providing an accurate, culturally unbiased threshold across White, Black, Asian, and Hispanic populations without requiring shifting cutoffs.</li>
        <li>NICE emphasizes that WHtR can be accurately and safely utilized in children and young people aged 5 and older.</li>
      </ul>

      <h2>Step-by-Step Worked Clinical Epidemiology Case Study</h2>
      <p>The following case study illustrates an evidence-based medical assessment evaluating a patient who illustrates the classic "Normal Weight Obese" clinical dilemma:</p>

      <div class="worked-example-card my-4">
        <h3 class="example-title">Preventive Health Case Profile: Normal Weight Obese (TOFI) Detection</h3>
        <p><strong>Patient Baseline:</strong> A 47-year-old software engineer presents for an annual routine physical examination. Anthropometrics: Stature = <strong>5 feet 10 inches (70.0 inches / 177.8 cm)</strong>, Body Mass = <strong>168 lbs (76.2 kg)</strong>, Measured Waist Circumference = <strong>38.0 inches (96.52 cm)</strong>.</p>
        
        <div class="example-step">
          <div class="step-num">Step 1</div>
          <div class="step-content">
            <strong>Compute Traditional Body Mass Index (BMI):</strong>
            $$\text{BMI} = 703 \times \frac{168}{(70.0)^2} = 703 \times \frac{168}{4900} = \mathbf{24.10 \text{ kg/m}^2}$$
            Under standard clinical BMI criteria ($18.5 - 24.9 \text{ kg/m}^2$), the patient is categorized as <em>"Normal Weight."</em> A standard automated electronic medical record (EMR) flag would generate zero alerts!
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 2</div>
          <div class="step-content">
            <strong>Calculate Waist-to-Height Ratio (WHtR):</strong>
            $$\text{WHtR} = \frac{\text{Waist Circumference}}{\text{Height}} = \frac{38.0 \text{ in}}{70.0 \text{ in}} = \mathbf{0.543}$$
            In metric: $96.52 \text{ cm} / 177.8 \text{ cm} = \mathbf{0.543}$.
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 3</div>
          <div class="step-content">
            <strong>Evaluate Against NICE 2022 and Ashwell Clinical Thresholds:</strong>
            A WHtR of 0.543 places the patient firmly in the <strong>0.50 to 0.59 "Increased Health Risk" tier</strong>.
            $$\text{Healthy Waist Upper Boundary} = 70.0 \text{ in} \times 0.50 = \mathbf{35.0 \text{ in}}$$
            $$\text{Excess Central Visceral Circumference} = 38.0 - 35.0 = \mathbf{+3.0 \text{ in above optimal ceiling}}$$
            The patient carries 3.0 inches of hidden intra-abdominal visceral adipose accumulation despite his normal scale weight!
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 4</div>
          <div class="step-content">
            <strong>Laboratory Correlation &amp; Clinical Management:</strong>
            Triggered by the elevated WHtR, the clinician orders a comprehensive cardiometabolic panel: Fasting Plasma Glucose is 112 mg/dL (Prediabetes), Serum Triglycerides are 215 mg/dL, and HDL-C is 38 mg/dL (Triglyceride/HDL ratio = 5.66, signaling severe insulin resistance). The clinician prescribes targeted aerobic training and resistance exercise to reduce waist circumference to $\le 35.0$ inches, averting progression to overt Type 2 Diabetes.
          </div>
        </div>
      </div>

      <h2>Standardized Measurement Protocol: Avoiding Measurement Artifacts</h2>
      <p>Precise clinical anthropometry requires strict adherence to standardized measurement protocol:</p>
      <ul>
        <li><strong>Measurement Location:</strong> Position the measuring tape horizontally around the bare abdomen at the midpoint between the lower palpable margin of the lowest rib and the superior aspect of the iliac crest. For many individuals, this coincides with the level of the umbilicus, but in severe central adiposity with abdominal pendulosity (panniculus), the bony landmarks must strictly be used rather than the sagging navel.</li>
        <li><strong>Position &amp; Tension:</strong> The patient stands erect with feet together, weight evenly distributed, and arms relaxed at the sides. The tape must remain horizontal around the circumference, snug without indenting skin.</li>
        <li><strong>Breathing Phase:</strong> Record the measurement at the end of a gentle, unforced expiration. Holding the breath or abdominal valsalva maneuvers artificially falsify readings.</li>
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
            <li><a href="waist-to-hip-ratio-calculator.html">Waist to Hip Ratio Calculator</a></li>
            <li><a href="waist-to-height-calculator.html">Waist to Height Calculator</a></li>
            <li><a href="bmi-calculator.html">BMI Calculator</a></li>
            <li><a href="body-fat-calculator.html">Body Fat Calculator</a></li>
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
        <p>&copy; 2026 CalcHub. Educational and clinical calculation tools. Consult a physician for individualized cardiovascular risk assessment.</p>
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
          const inc = parseFloat(heightInches.value) || 10;
          const totalIn = (ft * 12) + inc;
          heightCm.value = (totalIn * 2.54).toFixed(1);

          const wIn = parseFloat(waistInches.value) || 34;
          waistCm.value = (wIn * 2.54).toFixed(1);
        } else {
          usGroup.style.display = 'block';
          metricGroup.style.display = 'none';

          const cm = parseFloat(heightCm.value) || 178;
          const totalIn = cm / 2.54;
          heightFeet.value = Math.floor(totalIn / 12);
          heightInches.value = Math.round(totalIn % 12);

          const wCm = parseFloat(waistCm.value) || 86;
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
        const maxHealthyWaist = (heightVal * 0.50).toFixed(1);
        const minHealthyWaist = (heightVal * 0.40).toFixed(1);
        const diff = (waistVal - (heightVal * 0.50)).toFixed(1);

        let riskTier = '';
        let statusBadge = '';
        let shapeClass = '';
        let clinicalText = '';

        if (whtr < 0.40) {
          riskTier = 'Below Optimal / Slim';
          statusBadge = '<span class="status-below">&lt; 0.40 Below Optimal</span>';
          shapeClass = '"Take Care" (Depleted Stores)';
          clinicalText = 'Your waist circumference is under 40% of your height. Cardiovascular risk is low, but screen for nutritional adequacy and sarcopenia.';
        } else if (whtr < 0.50) {
          riskTier = 'Healthy / Low Risk';
          statusBadge = '<span class="status-normal">0.40 – 0.49 Healthy</span>';
          shapeClass = '"No Action" (Optimal Shape)';
          clinicalText = 'Congratulations! Your waist circumference is less than half your height, aligning with the optimal Ashwell shape and NICE 2022 guidelines for minimal visceral adiposity.';
        } else if (whtr < 0.60) {
          riskTier = 'Increased Cardiometabolic Risk';
          statusBadge = '<span class="status-above">0.50 – 0.59 Increased Risk</span>';
          shapeClass = '"Consider Action" (Pear/Apple Border)';
          clinicalText = 'Your waist circumference is ' + Math.abs(diff) + ' ' + unitLabel + ' above the 0.50 health ceiling. This indicates early intra-abdominal visceral adipose accumulation. Moderate dietary modifications and regular physical activity are advised.';
        } else {
          riskTier = 'Very High Health Risk';
          statusBadge = '<span class="status-above">&ge; 0.60 Very High Risk</span>';
          shapeClass = '"Take Action" (Central Apple Shape)';
          clinicalText = 'Your waist circumference is ' + Math.abs(diff) + ' ' + unitLabel + ' above the 0.50 threshold. This indicates substantial visceral fat accumulation. A comprehensive cardiometabolic clinical evaluation (fasting lipids, HbA1c, blood pressure) is strongly recommended.';
        }

        // Display results
        document.getElementById('res-whtr-value').textContent = whtr.toFixed(2);
        document.getElementById('res-whtr-status').innerHTML = statusBadge;
        document.getElementById('res-risk-tier').textContent = riskTier;
        document.getElementById('res-max-waist').textContent = maxHealthyWaist + ' ' + unitLabel;
        document.getElementById('res-variance-val').textContent = (diff > 0 ? '+' : '') + diff + ' ' + unitLabel;
        document.getElementById('res-variance-label').textContent = diff > 0 ? 'Above 0.50 ceiling' : 'Safely below ceiling';
        document.getElementById('res-shape-class').textContent = shapeClass;
        document.getElementById('res-ideal-band').textContent = minHealthyWaist + ' – ' + maxHealthyWaist + ' ' + unitLabel;
        document.getElementById('res-clinical-summary').textContent = clinicalText;

        resultsContainer.style.display = 'block';
        resultsContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      });

      // Run on initial load
      form.dispatchEvent(new Event('submit'));
    });
  </script>
</body>
</html>
"""

# -------------------------------------------------------------
# 8. waist-to-hip-ratio-calculator.html
# -------------------------------------------------------------
WAIST_HIP_RATIO_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Waist-to-Hip Ratio Calculator | WHO Body Shape & Health Risk</title>
  <meta name="description" content="Calculate your Waist-to-Hip Ratio (WHR) based on World Health Organization (WHO) standards. Differentiate Android vs Gynoid body fat and cardiovascular risk.">
  <link rel="canonical" href="https://calchub.com/waist-to-hip-ratio-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Clinical Waist-to-Hip Ratio (WHR) Calculator",
    "applicationCategory": "HealthApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0.00",
      "priceCurrency": "USD"
    },
    "description": "Calculates Waist-to-Hip Ratio (WHR), classifies Android versus Gynoid fat distribution, and stratifies cardiometabolic health risk according to World Health Organization (WHO) criteria."
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is the Waist-to-Hip Ratio (WHR) and what are the WHO clinical cutoffs?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Waist-to-Hip Ratio (WHR) is calculated by dividing waist circumference by hip circumference. According to the World Health Organization (WHO Technical Report Series 916), central obesity and substantially increased health risk are defined as a WHR greater than 0.90 for men and greater than 0.85 for women."
        }
      },
      {
        "@type": "Question",
        "name": "What is the difference between Android ('Apple') and Gynoid ('Pear') fat distribution?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Android obesity refers to fat concentrated intra-abdominally around the waist and portal visceral organs, producing an 'apple' shape. It is strongly linked to insulin resistance, metabolic syndrome, and coronary artery disease. Gynoid obesity refers to fat concentrated subcutaneously around the hips, buttocks, and thighs ('pear' shape). Gynoid fat acts as an inert metabolic sink that is not associated with elevated cardiovascular risk."
        }
      },
      {
        "@type": "Question",
        "name": "Where should the hip circumference be measured?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Per World Health Organization standardized anthropometric protocol, hip circumference must be measured at the widest horizontal diameter over the greater trochanters of the femurs and the maximum extension of the buttocks, keeping the measuring tape parallel to the floor."
        }
      },
      {
        "@type": "Question",
        "name": "What did the landmark INTERHEART study find regarding WHR versus BMI?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The landmark INTERHEART study (published in The Lancet, evaluating 27,098 subjects across 52 countries) proved that Waist-to-Hip Ratio is substantially more predictive of myocardial infarction than Body Mass Index (BMI). The population attributable risk (PAR) for myocardial infarction was 33.7% for elevated WHR compared to negligible predictive value for BMI."
        }
      },
      {
        "@type": "Question",
        "name": "Why do women naturally have a lower WHR cutoff than men?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Biological women have wider pelvic skeletal geometry and higher estrogen receptor-alpha (ERα) density in gluteofemoral adipose tissue, which selectively directs fat deposition to the hips and thighs. Consequently, women maintain a lower baseline WHR, and the clinical threshold for central visceral obesity is lower (0.85) than in men (0.90)."
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
        <li class="active">Waist-to-Hip Ratio Calculator</li>
      </ol>
    </nav>

    <div class="page-layout">
      <div class="calculator-container">
        <div class="calculator-card">
          <h1 class="calculator-title">Clinical Waist-to-Hip Ratio (WHR) Calculator</h1>
          <p class="calculator-subtitle">Evaluate your body fat distribution, distinguish Android vs Gynoid somatotypes, and assess cardiovascular health risk using World Health Organization (WHO) standards.</p>

          <form id="whr-form" class="calculator-form">
            <div class="form-row">
              <div class="form-group col-half">
                <label for="unit-system" class="form-label">Measurement Units</label>
                <select id="unit-system" class="form-select">
                  <option value="us" selected>US Customary (Inches)</option>
                  <option value="metric">Metric (Centimeters)</option>
                </select>
              </div>
              <div class="form-group col-half">
                <label for="gender" class="form-label">Biological Sex</label>
                <select id="gender" class="form-select">
                  <option value="male" selected>Male (WHO Cutoff: &gt;0.90)</option>
                  <option value="female">Female (WHO Cutoff: &gt;0.85)</option>
                </select>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group col-half">
                <label for="waist-circ" class="form-label">Waist Circumference (<span class="unit-label">Inches</span>)</label>
                <input type="number" id="waist-circ" class="form-input" min="15" max="80" value="34" step="0.25" required>
                <small class="form-hint">Midpoint between bottom rib and top of iliac crest.</small>
              </div>
              <div class="form-group col-half">
                <label for="hip-circ" class="form-label">Hip Circumference (<span class="unit-label">Inches</span>)</label>
                <input type="number" id="hip-circ" class="form-input" min="20" max="90" value="40" step="0.25" required>
                <small class="form-hint">Widest horizontal circumference over the buttocks.</small>
              </div>
            </div>

            <button type="submit" class="calculate-btn">Compute Waist-to-Hip Ratio</button>
          </form>

          <div id="calculator-results" class="results-container" style="display: none;">
            <h2 class="results-heading">Body Composition &amp; Risk Profile</h2>

            <div class="results-grid">
              <div class="result-card primary-result">
                <span class="result-label">Waist-to-Hip Ratio (WHR)</span>
                <span id="res-whr-value" class="result-value">--</span>
                <span id="res-whr-badge" class="result-subtext badge-tag">Low Risk</span>
              </div>

              <div class="result-card highlight-card">
                <span class="result-label">Body Fat Distribution Pattern</span>
                <span id="res-fat-pattern" class="result-value">--</span>
                <span class="result-subtext">Android vs. Gynoid Morphology</span>
              </div>

              <div class="result-card">
                <span class="result-label">WHO Cardiometabolic Risk Level</span>
                <span id="res-who-risk" class="result-value">--</span>
                <span class="result-subtext">Based on WHO Technical Report 916</span>
              </div>

              <div class="result-card">
                <span class="result-label">Clinical Risk Cutoff Threshold</span>
                <span id="res-cutoff-threshold" class="result-value">--</span>
                <span class="result-subtext">Sex-specific boundary</span>
              </div>

              <div class="result-card">
                <span class="result-label">Target Waist Circumference</span>
                <span id="res-target-waist" class="result-value">--</span>
                <span class="result-subtext">To reach low-risk WHR at current hip size</span>
              </div>

              <div class="result-card">
                <span class="result-label">Variance from Cutoff</span>
                <span id="res-variance-status" class="result-value">--</span>
                <span id="res-variance-note" class="result-subtext">Margin</span>
              </div>
            </div>

            <div class="summary-box mt-4">
              <h3 class="summary-title">Cardiometabolic Risk Interpretation</h3>
              <p id="res-clinical-text" class="summary-text">Loading anthropometric evaluation...</p>
            </div>
          </div>
        </div>
      </div>

      <aside class="sidebar">
        <div class="sidebar-card">
          <h3 class="sidebar-title">Adiposity &amp; Heart Health Tools</h3>
          <ul class="sidebar-list">
            <li><a href="waist-to-height-ratio-calculator.html">Waist to Height Ratio Calculator</a></li>
            <li><a href="waist-to-height-calculator.html">Waist to Height Calculator</a></li>
            <li><a href="bmi-calculator.html">BMI Calculator</a></li>
            <li><a href="body-fat-calculator.html">Body Fat Calculator</a></li>
            <li><a href="cholesterol-ratio-calculator.html">Cholesterol Ratio Calculator</a></li>
          </ul>
        </div>
        <div class="sidebar-card mt-4">
          <h3 class="sidebar-title">Clinical Standards</h3>
          <p class="sidebar-text">Based on World Health Organization (WHO) Technical Report Series 916, the INTERHEART global epidemiological study (Lancet 2004), and the American Heart Association (AHA).</p>
        </div>
      </aside>
    </div>

    <article class="article-body">
      <h2>The Physiology of Regional Body Fat Distribution</h2>
      <p>In clinical cardiology and metabolic medicine, body composition is defined not merely by total adipose mass, but by regional anatomical partitioning. For decades, total weight and Body Mass Index ($BMI = kg/m^2$) served as the primary clinical metrics for obesity. However, BMI fails completely to identify <em>where</em> adipose tissue is sequestered. The <strong>Waist-to-Hip Ratio (WHR)</strong> evaluates the proportionality between central abdominal fat and peripheral gluteofemoral subcutaneous fat, exposing two radically different biological somatotypes:</p>
      <ul>
        <li><strong>Android ("Apple") Adiposity:</strong> Adipose tissue is predominantly accumulated intra-abdominally within the greater omentum and mesentery surrounding visceral organs. Android obesity is driven by high density of lipolytic $\beta$-adrenergic receptors and glucocorticoid sensitivity, draining directly into the hepatic portal circulation. It represents the driving force behind the metabolic syndrome, atherogenic dyslipidemia, and systemic insulin resistance.</li>
        <li><strong>Gynoid ("Pear") Adiposity:</strong> Adipose tissue is concentrated subcutaneously over the gluteal and femoral regions (hips and thighs). Gynoid fat possesses high lipoprotein lipase ($LPL$) activity and high density of anti-lipolytic $\alpha_{2A}$-adrenergic receptors, acting as an inert, protective metabolic buffer that sequesters excess triglycerides away from the liver and skeletal muscle.</li>
      </ul>

      <h2>Mathematical Formulation: Waist-to-Hip Ratio (WHR)</h2>
      <p>The Waist-to-Hip Ratio is the dimensionless mathematical quotient of waist circumference ($W$) divided by hip circumference ($H$), measured in identical linear units:</p>

      $$WHR = \frac{\text{Waist Circumference}}{\text{Hip Circumference}}$$

      <p>Because the hip circumference in the denominator reflects gluteofemoral subcutaneous fat and pelvic skeletal width, WHR serves as a physiological contrast ratio: a high WHR indicates an expansion of visceral abdominal mass relative to protective lower-body peripheral mass.</p>

      <h2>World Health Organization (WHO) Diagnostic Criteria</h2>
      <p>The <strong>World Health Organization (WHO Technical Report Series 916)</strong> established global clinical thresholds defining substantially increased cardiometabolic disease risk:</p>

      <div class="table-container my-4">
        <table class="data-table">
          <thead>
            <tr>
              <th>Biological Sex</th>
              <th>Low Cardiometabolic Risk</th>
              <th>Moderate Health Risk</th>
              <th>Substantially Increased Risk (Central Obesity)</th>
              <th>Primary Clinical Significance</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Men</strong></td>
              <td>WHR &le; 0.90</td>
              <td>WHR 0.91 – 0.99</td>
              <td><strong>WHR &ge; 1.00</strong> (Strict threshold: &gt; 0.90)</td>
              <td>Substantial elevation in coronary heart disease, stroke, and hepatic steatosis.</td>
            </tr>
            <tr>
              <td><strong>Women</strong></td>
              <td>WHR &le; 0.80</td>
              <td>WHR 0.81 – 0.84</td>
              <td><strong>WHR &ge; 0.85</strong></td>
              <td>Significant increase in insulin resistance, gestational diabetes, and cardiovascular events.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>The Landmark INTERHEART Study: Proving WHR Superiority Over BMI</h2>
      <p>The definitive epidemiological proof of WHR's diagnostic supremacy over Body Mass Index was established by the landmark <strong>INTERHEART Study</strong>, published in <em>The Lancet</em> by Dr. Salim Yusuf and international collaborators across 262 centers in <strong>52 countries</strong> evaluating 27,098 individuals:</p>
      <ul>
        <li><strong>Predictive Power for Myocardial Infarction:</strong> The INTERHEART investigators evaluated whether BMI, waist circumference, or waist-to-hip ratio best predicted first acute myocardial infarction (heart attack). After multivariable adjustment for smoking, hypertension, diabetes, and lipid profiles, <strong>Waist-to-Hip Ratio was the single strongest anthropometric predictor of myocardial infarction across all regions and ethnic groups globally</strong>.</li>
        <li><strong>Population Attributable Risk (PAR):</strong> Elevated WHR accounted for <strong>33.7% of the Population Attributable Risk (PAR)</strong> for myocardial infarction worldwide, whereas BMI had virtually zero independent predictive power once WHR was accounted for. Individuals in the highest quintile of WHR exhibited more than double the odds of myocardial infarction compared to the lowest quintile ($\text{Odds Ratio } 2.44$).</li>
        <li><strong>The False Security of Low BMI:</strong> INTERHEART demonstrated that individuals with a low or normal BMI (<25 kg/m&sup2;) who harbored a high WHR faced greater cardiovascular risk than individuals with an elevated BMI but a favorable, low WHR.</li>
      </ul>

      <h2>Biological Sexual Dimorphism in Adipose Partitioning</h2>
      <p>The biological cutoffs for WHR differ decisively between men (0.90) and women (0.85) due to profound neuroendocrine and evolutionary differences:</p>
      <ul>
        <li><strong>Estrogen and Lipoprotein Lipase (LPL):</strong> In premenopausal women, ovarian 17&beta;-estradiol acts upon estrogen receptor-alpha ($ER\alpha$) in gluteofemoral adipocytes, selectively upregulating lipoprotein lipase activity and directing dietary fat into subcutaneous hip and thigh depots to store energy for pregnancy and lactation.</li>
        <li><strong>The Menopausal Metabolic Shift:</strong> Following menopause, estrogen levels plummet, and the androgen-to-estrogen ratio increases. Postmenopausal women experience an accelerated redistribution of body fat from gynoid subcutaneous depots into central visceral depots, resulting in a rapid increase in WHR and a steep rise in cardiovascular morbidity matching male rates.</li>
        <li><strong>Androgen Influences in Men:</strong> In men, testosterone suppresses subcutaneous femoral fat accumulation while visceral fat receptors remain highly sensitive to cortisol and sympathetic stimulation, predisposing men to android abdominal fat accumulation starting in early adulthood.</li>
      </ul>

      <h2>Step-by-Step Worked Clinical Case Study</h2>
      <p>The following case study illustrates an evidence-based clinical cardiology assessment comparing BMI and WHR in a female patient presenting for cardiovascular risk profiling:</p>

      <div class="worked-example-card my-4">
        <h3 class="example-title">Cardiovascular Prevention Case Profile: Android Obesity Screening</h3>
        <p><strong>Patient Baseline:</strong> A 50-year-old perimenopausal female presents for a routine checkup. Anthropometrics: Height = <strong>5 feet 4 inches (64 inches / 162.6 cm)</strong>, Body Weight = <strong>140 lbs (63.5 kg)</strong>. Measured Waist Circumference = <strong>32.5 inches (82.55 cm)</strong>, Measured Hip Circumference = <strong>36.0 inches (91.44 cm)</strong>.</p>
        
        <div class="example-step">
          <div class="step-num">Step 1</div>
          <div class="step-content">
            <strong>Compute Traditional Body Mass Index (BMI):</strong>
            $$\text{BMI} = 703 \times \frac{140}{(64)^2} = 703 \times \frac{140}{4096} = \mathbf{24.03 \text{ kg/m}^2}$$
            Evaluation: A BMI of 24.03 falls within the 18.5–24.9 range, classifying her as <em>"Normal Weight."</em> Under traditional clinic workflows, no metabolic concerns would be raised.
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 2</div>
          <div class="step-content">
            <strong>Calculate Waist-to-Hip Ratio (WHR):</strong>
            $$WHR = \frac{\text{Waist Circumference}}{\text{Hip Circumference}} = \frac{32.5 \text{ in}}{36.0 \text{ in}} = \mathbf{0.903}$$
            In metric equivalents: $82.55 \text{ cm} / 91.44 \text{ cm} = \mathbf{0.903}$.
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 3</div>
          <div class="step-content">
            <strong>Evaluate Against WHO Technical Report 916 Standards:</strong>
            For adult females, the WHO cutoff for substantially increased cardiometabolic risk is <strong>WHR &gt; 0.85</strong>.
            $$\Delta = 0.903 - 0.850 = \mathbf{+0.053 \text{ above clinical risk ceiling}}$$
            Her WHR of 0.903 diagnoses <strong>Android (Apple-shaped) Obesity</strong> despite a completely normal BMI!
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 4</div>
          <div class="step-content">
            <strong>Compute Target Waist for Her Current Hip Dimension:</strong>
            To reach the low-risk threshold ($\le 0.80$) at her current hip circumference of 36.0 inches:
            $$\text{Target Waist} = 36.0 \times 0.80 = \mathbf{28.8 \text{ inches}}$$
            She must reduce her waist circumference by $32.5 - 28.8 = \mathbf{3.7 \text{ inches}}$ to eliminate excess visceral fat.
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 5</div>
          <div class="step-content">
            <strong>Diagnostic Corroboration &amp; Intervention:</strong>
            Fasting laboratory testing reveals an early atherogenic lipid profile (Triglycerides 188 mg/dL, HDL-C 42 mg/dL) and borderline fasting glucose (104 mg/dL). Initiating a Mediterranean dietary pattern rich in monounsaturated fats and prescribing 150 minutes of weekly aerobic exercise successfully reverses central visceral accumulation and restores a gynoid lipid profile.
          </div>
        </div>
      </div>

      <h2>Standardized Anthropometric Measurement Technique (WHO Protocol)</h2>
      <p>Accurate calculation of WHR requires exact anatomical landmark identification to eliminate clinical measurement variability:</p>
      <ul>
        <li><strong>Waist Measurement:</strong> Standing erect with arms at sides, place the measuring tape horizontally around the torso at the midpoint between the inferior margin of the lowest palpable rib and the highest point of the iliac crest (usually level with the navel). Record at the end of a normal expiration.</li>
        <li><strong>Hip Measurement:</strong> Place the measuring tape horizontally around the maximum extension of the buttocks, corresponding anatomically to the level of the <strong>greater trochanters of the femurs</strong>. Ensure the tape is parallel to the floor from front, side, and rear views.</li>
        <li><strong>Consistency:</strong> Both measurements must be taken with the tape snug against the skin or light undergarments without compressing subcutaneous tissue. Repeat twice; if measurements differ by $>1\text{ cm}$, take a third reading and calculate the average.</li>
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
            <li><a href="waist-to-hip-ratio-calculator.html">Waist to Hip Ratio Calculator</a></li>
            <li><a href="waist-to-height-ratio-calculator.html">Waist to Height Ratio Calculator</a></li>
            <li><a href="bmi-calculator.html">BMI Calculator</a></li>
            <li><a href="body-fat-calculator.html">Body Fat Calculator</a></li>
            <li><a href="cholesterol-ratio-calculator.html">Cholesterol Ratio Calculator</a></li>
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
        <p>&copy; 2026 CalcHub. Educational and clinical calculation tools. Consult a physician for individualized cardiovascular risk assessment.</p>
      </div>
    </div>
  </footer>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const form = document.getElementById('whr-form');
      const unitSystem = document.getElementById('unit-system');
      const genderSelect = document.getElementById('gender');
      const waistInput = document.getElementById('waist-circ');
      const hipInput = document.getElementById('hip-circ');
      const unitLabels = document.querySelectorAll('.unit-label');
      const resultsContainer = document.getElementById('calculator-results');

      unitSystem.addEventListener('change', function() {
        const isMetric = unitSystem.value === 'metric';
        if (isMetric) {
          unitLabels.forEach(el => el.textContent = 'Centimeters');
          waistInput.value = (parseFloat(waistInput.value) * 2.54).toFixed(1);
          hipInput.value = (parseFloat(hipInput.value) * 2.54).toFixed(1);
          waistInput.min = '40';
          waistInput.max = '200';
          hipInput.min = '50';
          hipInput.max = '225';
        } else {
          unitLabels.forEach(el => el.textContent = 'Inches');
          waistInput.value = (parseFloat(waistInput.value) / 2.54).toFixed(1);
          hipInput.value = (parseFloat(hipInput.value) / 2.54).toFixed(1);
          waistInput.min = '15';
          waistInput.max = '80';
          hipInput.min = '20';
          hipInput.max = '90';
        }
      });

      form.addEventListener('submit', function(e) {
        e.preventDefault();

        const isMetric = unitSystem.value === 'metric';
        const isMale = genderSelect.value === 'male';
        const waist = parseFloat(waistInput.value) || 0;
        const hip = parseFloat(hipInput.value) || 0;
        const unitStr = isMetric ? 'cm' : 'in';

        if (waist <= 0 || hip <= 0) return;

        const whr = waist / hip;
        const cutoff = isMale ? 0.90 : 0.85;
        const optimalCutoff = isMale ? 0.85 : 0.80;
        const targetWaist = (hip * optimalCutoff).toFixed(1);
        const variance = (whr - cutoff).toFixed(2);

        let riskLevel = '';
        let badgeHtml = '';
        let patternStr = '';
        let clinicalText = '';

        if (whr > cutoff) {
          riskLevel = 'Substantially Increased Risk (Central Obesity)';
          badgeHtml = '<span class="status-above">High Risk (&gt; ' + cutoff + ')</span>';
          patternStr = 'Android Morphology ("Apple" Shape)';
          clinicalText = 'Your WHR exceeds the WHO clinical boundary of ' + cutoff + ' for ' + (isMale ? 'men' : 'women') + '. This indicates prominent central visceral adipose deposition around intra-abdominal portal organs. Elevated risk for type 2 diabetes, atherogenic dyslipidemia, and coronary artery disease. A waist reduction of ' + Math.abs((waist - targetWaist).toFixed(1)) + ' ' + unitStr + ' is recommended to reach the low-risk band.';
        } else if (whr > optimalCutoff) {
          riskLevel = 'Moderate Health Risk';
          badgeHtml = '<span class="status-below">Moderate Risk</span>';
          patternStr = 'Intermediate Distribution';
          clinicalText = 'Your WHR is within the intermediate range. Maintain active physical exercise and balanced nutrition to prevent progressive waist enlargement.';
        } else {
          riskLevel = 'Low Cardiometabolic Risk';
          badgeHtml = '<span class="status-normal">Low Risk (&le; ' + optimalCutoff + ')</span>';
          patternStr = 'Gynoid Morphology ("Pear" / Low Central Fat)';
          clinicalText = 'Congratulations! Your WHR is comfortably within the WHO low-risk category. Your body fat distribution reflects minimal deep visceral accumulation and optimal cardiovascular protection.';
        }

        // Render results
        document.getElementById('res-whr-value').textContent = whr.toFixed(2);
        document.getElementById('res-whr-badge').innerHTML = badgeHtml;
        document.getElementById('res-fat-pattern').textContent = patternStr;
        document.getElementById('res-who-risk').textContent = riskLevel;
        document.getElementById('res-cutoff-threshold').textContent = 'WHR > ' + cutoff + ' (' + (isMale ? 'Male' : 'Female') + ')';
        document.getElementById('res-target-waist').textContent = targetWaist + ' ' + unitStr;
        document.getElementById('res-variance-status').textContent = (variance > 0 ? '+' : '') + variance;
        document.getElementById('res-variance-note').textContent = variance > 0 ? 'Above WHO clinical cutoff' : 'Safely below WHO cutoff';
        document.getElementById('res-clinical-text').textContent = clinicalText;

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
    whtr_ratio_path = os.path.join(BASE_DIR, "waist-to-height-ratio-calculator.html")
    with open(whtr_ratio_path, "w", encoding="utf-8") as f:
        f.write(WAIST_HEIGHT_RATIO_HTML.strip() + "\n")
    print(f"Generated {os.path.basename(whtr_ratio_path)}")

    whr_path = os.path.join(BASE_DIR, "waist-to-hip-ratio-calculator.html")
    with open(whr_path, "w", encoding="utf-8") as f:
        f.write(WAIST_HIP_RATIO_HTML.strip() + "\n")
    print(f"Generated {os.path.basename(whr_path)}")

if __name__ == "__main__":
    main()
