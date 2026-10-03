"""
Batch 22 - Part 3: Health & Fitness Tools
5. max-heart-rate-calculator.html (Tanaka, Gellish, Gulati, Fairbarn & Fox HRmax Algorithms)
6. met-calculator.html (Metabolic Equivalent of Task Sizer, MET-Minutes & WHO Guidelines)
Word count target: >1,050 words in article-body each.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 5. max-heart-rate-calculator.html
# -------------------------------------------------------------
MAX_HR_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Max Heart Rate Calculator | Tanaka, Gellish, Gulati & Fox Formulas</title>
  <meta name="description" content="Calculate your true maximum heart rate (HRmax) comparing Tanaka, Gellish, Gulati (female-specific), Fairbarn, and Fox formulas. Age-graded athletic dispersion.">
  <link rel="canonical" href="https://calchub.com/max-heart-rate-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Clinical Maximum Heart Rate (HRmax) Multi-Formula Calculator",
    "applicationCategory": "HealthApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0.00",
      "priceCurrency": "USD"
    },
    "description": "Calculates maximum heart rate comparing Tanaka, Gellish, Gulati (female-specific), Fairbarn, and classic Fox equations with standard error of estimate intervals."
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Why is the traditional '220 - Age' formula considered inaccurate?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The classic Fox and Haskell formula (220 - Age), created in 1971 from a compilation of eleven disparate observational studies, lacks formal regression validation. Scientific reviews by Robergs and Landwehr demonstrated that it has a standard error of estimate (SEE) of ±11 to ±12 beats per minute, systematically overestimating HRmax in young adults under 30 and severely underestimating HRmax in adults over 50 by up to 15 bpm."
        }
      },
      {
        "@type": "Question",
        "name": "What is the Tanaka formula for maximum heart rate?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Tanaka formula [HRmax = 208 - (0.7 × Age)] was derived in 2001 by Dr. Hirofumi Tanaka and colleagues through a meta-analysis of 351 laboratory studies involving 18,712 healthy human subjects. It maintains superior statistical consistency across broad adult populations."
        }
      },
      {
        "@type": "Question",
        "name": "Why do women need a gender-specific HRmax formula like the Gulati equation?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "In 2010, the St. James Women Take Heart Project led by Dr. Martha Gulati evaluated 5,437 asymptomatic women and established that female maximum heart rate declines at a faster rate with age than male heart rate. The resulting Gulati formula [HRmax = 206 - (0.88 × Age)] prevents significant over-prescription of exercise intensity in older female athletes."
        }
      },
      {
        "@type": "Question",
        "name": "Why does maximum heart rate decline as we age?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Age-related HRmax decline is driven by electrophysiological remodeling of the sinoatrial (SA) node, including a decrease in intrinsic pacemaking rate, gradual fibrosis of conductive nodal tissue, and progressive desensitization and downregulation of cardiac beta-1 adrenergic receptors to sympathetic catecholamines."
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
        <div class="badge-tag">Exercise Cardiology</div>
        <h1 class="calculator-title">Maximum Heart Rate (HRmax) Sizer</h1>
        <p class="calculator-description">Calculate and compare your maximum heart rate across the top validated physiological formulas: Tanaka, Gellish, Gulati (Women), Fairbarn, and Fox.</p>
      </div>

      <div class="calculator-grid">
        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Demographic Parameters</h2>
          </div>
          <div class="calc-card-body">
            <div class="form-row" style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
              <div class="form-group">
                <label for="hrmax-age" class="form-label">Age (Years)</label>
                <input type="number" id="hrmax-age" class="form-input" value="45" min="10" max="100" step="1" oninput="calculateHRMax()">
              </div>
              <div class="form-group">
                <label for="hrmax-gender" class="form-label">Biological Sex</label>
                <select id="hrmax-gender" class="form-select" onchange="calculateHRMax()">
                  <option value="male" selected>Male</option>
                  <option value="female">Female (Enables Gulati Model)</option>
                </select>
              </div>
            </div>

            <div class="form-group">
              <label for="hrmax-primary" class="form-label">Primary Reference Algorithm</label>
              <select id="hrmax-primary" class="form-select" onchange="calculateHRMax()">
                <option value="tanaka" selected>Tanaka et al. (2001) - 208 - (0.7 × Age) [General Standard]</option>
                <option value="gellish">Gellish et al. (2007) - 207 - (0.7 × Age) [Stress Test Standard]</option>
                <option value="gulati">Gulati et al. (2010) - 206 - (0.88 × Age) [Female Cohort]</option>
                <option value="fairbarn">Fairbarn et al. (1994) - Gender-Specific Regression</option>
                <option value="fox">Fox &amp; Haskell (1971) - 220 - Age [Legacy Comparison]</option>
              </select>
            </div>

            <button type="button" class="btn btn-primary" onclick="calculateHRMax()">Compute Maximum Heart Rate</button>
          </div>
        </div>

        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Calculated Maximum Heart Rate</h2>
          </div>
          <div class="calc-card-body">
            <div class="result-hero" style="background:#eff6ff;border-color:#bfdbfe;">
              <span class="hero-label">Primary Estimated HRmax (Tanaka)</span>
              <div class="hero-value" id="res-hrmax-primary" style="color:#1d4ed8;font-size:2.4rem;">177 BPM</div>
              <span class="form-hint" id="res-hrmax-range">95% Statistical Confidence Band: 167 – 187 BPM (±10 bpm)</span>
            </div>

            <div class="results-grid" style="margin-top:1.5rem;">
              <div class="result-item">
                <span class="result-label">Gellish Formula</span>
                <span class="result-value" id="res-hrmax-gellish">176 BPM</span>
              </div>
              <div class="result-item">
                <span class="result-label">Gulati (Women)</span>
                <span class="result-value" id="res-hrmax-gulati">166 BPM</span>
              </div>
              <div class="result-item">
                <span class="result-label">Fairbarn Formula</span>
                <span class="result-value" id="res-hrmax-fairbarn">173 BPM</span>
              </div>
              <div class="result-item">
                <span class="result-label">Legacy Fox (220-Age)</span>
                <span class="result-value" id="res-hrmax-fox">175 BPM</span>
              </div>
            </div>

            <div class="stat-box" style="margin-top:1.5rem;padding:1rem;background:#f8fafc;border-radius:8px;border:1px solid #e2e8f0;">
              <h4 style="font-weight:700;margin-bottom:0.5rem;font-size:0.95rem;">Exercise Intensity Guidelines (Tanaka Baseline):</h4>
              <p id="res-intensity-targets" style="font-size:0.875rem;color:#475569;margin:0;">
                Moderate Aerobic (64%–76%): <strong>113 – 135 BPM</strong> | Vigorous / Threshold (77%–95%): <strong>136 – 168 BPM</strong>.
              </p>
            </div>
          </div>
        </div>
      </div>

      <article class="article-body">
        <h2>Electrophysiological Basis of Maximum Heart Rate</h2>
        <p>
          Maximum heart rate ($HR_{\text{max}}$) is the highest number of contractions the myocardium can execute in one minute during an all-out, maximal graded exercise stress test to volitional exhaustion. Unlike resting heart rate, which demonstrates dramatic plasticity in response to aerobic exercise conditioning, <strong>maximum heart rate is fundamentally non-trainable</strong>. An Olympic marathon champion and a sedentary individual of identical age possess essentially identical physiological maximum heart rates.
        </p>
        <p>
          The intrinsic biological ceiling of cardiac rate is governed by the biophysics of the <strong>sinoatrial (SA) node</strong>, the primary cardiac pacemaker situated at the junction of the superior vena cava and the right atrium. Spontaneous action potentials in the SA node are initiated by hyperpolarization-activated cyclic nucleotide-gated ($HCN4$) channels generating the inward "funny" sodium current ($I_f$), followed by transient T-type ($Ca_v3.1$) and long-lasting L-type ($Ca_v1.2$) calcium channel influx.
        </p>

        <h2>Why Does Maximum Heart Rate Inevitably Decline with Age?</h2>
        <p>
          Across mammalian species, aging produces a universal, linear decrement in maximum chronotropic capacity (roughly 0.7 to 1.0 beats per minute per year in humans). Multiple electrophysiological mechanisms drive this decline:
        </p>
        <ol>
          <li><strong>Structural Remodeling of the Pacemaker:</strong> With chronological aging, the total number of functional P-cells within the sinoatrial node declines, accompanied by progressive fibrofatty infiltration of the nodal extracellular matrix.</li>
          <li><strong>$\beta_1$-Adrenergic Receptor Downregulation:</strong> Under high-intensity exercise stress, systemic catecholamines (epinephrine and norepinephrine) bind to myocardial $\beta_1$-adrenergic receptors, activating adenylyl cyclase and boosting intracellular cyclic AMP ($cAMP$). In aging myocardium, $\beta_1$-receptor density decreases by 30% to 50%, and post-receptor signal transduction is attenuated, muting the inotropic and chronotropic response to sympathetic stimulation.</li>
          <li><strong>Intrinsic Action Potential Prolongation:</strong> Repolarization velocity slows with age due to decreased density of rapidly activating delayed rectifier potassium channels ($I_{Kr}$ and $I_{Ks}$), lengthening the absolute refractory period of atrial myocytes and preventing higher frequencies.</li>
        </ol>

        <h2>Critical Evaluation of Validated HRmax Prediction Equations</h2>

        <div class="formula-box">
          <p><strong>1. The Tanaka Formula (2001) - Gold Standard Meta-Analysis:</strong></p>
          $$HR_{\text{max}} = 208 - (0.7 \times \text{Age})$$
          <p>
            Published in the <em>Journal of the American College of Cardiology</em> by Dr. Hirofumi Tanaka, Kevin Monahan, and Douglas Seals, this equation synthesized data from 351 studies encompassing 18,712 subjects. It established that the rate of HRmax decline is independent of sex and habitual physical activity status.
          </p>
        </div>

        <div class="formula-box">
          <p><strong>2. The Gellish Formula (2007) - Longitudinal Exercise Stress Protocol:</strong></p>
          $$HR_{\text{max}} = 207 - (0.7 \times \text{Age})$$
          <p>
            Derived by Ronald Gellish and colleagues at the Oakland University Beaumont Center for Human Movement, this formula resulted from a meticulous 25-year longitudinal study of 132 subjects undergoing maximal treadmill stress testing. It demonstrated the highest correlation coefficient ($r = -0.93$) and lowest standard error of any single-cohort equation.
          </p>
        </div>

        <div class="formula-box">
          <p><strong>3. The Gulati Formula (2010) - Female-Specific Landmark Trial:</strong></p>
          $$HR_{\text{max}} = 206 - (0.88 \times \text{Age})$$
          <p>
            In the <em>New England Journal of Medicine</em>, Dr. Martha Gulati published data from the St. James Women Take Heart Project evaluating 5,437 asymptomatic women. Gulati discovered that the age-related slope in women is steeper ($-0.88\text{ bpm/year}$) than the $-0.7\text{ bpm/year}$ observed in male-dominated cohorts. Using standard equations in older women overestimates their HRmax, leading to dangerously excessive exercise target prescriptions.
          </p>
        </div>

        <div class="formula-box">
          <p><strong>4. Fairbarn Equations (1994) - Gender-Stratified Cycle Ergometry:</strong></p>
          $$\text{Men: } HR_{\text{max}} = 201 - (0.63 \times \text{Age})$$
          $$\text{Women: } HR_{\text{max}} = 216 - (1.09 \times \text{Age})$$
        </div>

        <div class="formula-box">
          <p><strong>5. Fox &amp; Haskell Formula (1971) - The Historical Artifact:</strong></p>
          $$HR_{\text{max}} = 220 - \text{Age}$$
          <p>
            Despite universal presence on commercial gym equipment, this formula was never published in a peer-reviewed investigation. It arose from an arbitrary graphical line fit across an incidental collection of 11 small trials. In 2002, exercise physiologists Robert Robergs and Roberto Landwehr published a scathing review titled <em>"The Surprising History of the 'HRmax=220-age' Equation"</em>, concluding that the formula has no scientific merit and should be eradicated from clinical practice.
          </p>
        </div>

        <h2>Comparative Formula Discrepancy Matrix Across Decades</h2>
        <p>
          The table below demonstrates how the classic Fox formula diverges from modern validated equations across adult life:
        </p>

        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>Chronological Age</th>
                <th>Tanaka (2001)</th>
                <th>Gellish (2007)</th>
                <th>Gulati (Women, 2010)</th>
                <th>Fox Legacy (220-Age)</th>
                <th>Discrepancy (Fox vs Tanaka)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>20 Years Old</strong></td>
                <td>194 BPM</td>
                <td>193 BPM</td>
                <td>188 BPM</td>
                <td>200 BPM</td>
                <td>Fox overestimates by +6 BPM</td>
              </tr>
              <tr>
                <td><strong>30 Years Old</strong></td>
                <td>187 BPM</td>
                <td>186 BPM</td>
                <td>180 BPM</td>
                <td>190 BPM</td>
                <td>Fox overestimates by +3 BPM</td>
              </tr>
              <tr>
                <td><strong>40 Years Old</strong></td>
                <td>180 BPM</td>
                <td>179 BPM</td>
                <td>171 BPM</td>
                <td>180 BPM</td>
                <td>Equilibrium crossover point</td>
              </tr>
              <tr>
                <td><strong>50 Years Old</strong></td>
                <td>173 BPM</td>
                <td>172 BPM</td>
                <td>162 BPM</td>
                <td>170 BPM</td>
                <td>Fox underestimates by -3 BPM</td>
              </tr>
              <tr>
                <td><strong>60 Years Old</strong></td>
                <td>166 BPM</td>
                <td>165 BPM</td>
                <td>153 BPM</td>
                <td>160 BPM</td>
                <td>Fox underestimates by -6 BPM</td>
              </tr>
              <tr>
                <td><strong>70 Years Old</strong></td>
                <td>159 BPM</td>
                <td>158 BPM</td>
                <td>144 BPM</td>
                <td>150 BPM</td>
                <td>Fox underestimates by -9 BPM</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2>Worked Exercise Cardiology Case Study</h2>
        <div class="worked-example-card">
          <div class="example-header">
            <span class="example-badge">Exercise Cardiology Case</span>
            <h3 class="example-title">Prescribing Target HR for a Master Female Athlete</h3>
          </div>
          <div class="example-step">
            <div class="step-num">1</div>
            <div class="step-content">
              <strong>Patient Clinical Data:</strong> A 58-year-old female master triathlete is referred for cardiac risk stratification prior to Ironman competition. She relies on heart rate monitoring for high-intensity threshold workouts. The cardiologist evaluates her HRmax using both traditional and female-specific validated algorithms.
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">2</div>
            <div class="step-content">
              <strong>Calculate HRmax via Legacy Fox Formula:</strong>
              $$HR_{\text{max (Fox)}} = 220 - 58 = \mathbf{162\text{ BPM}}$$
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">3</div>
            <div class="step-content">
              <strong>Calculate HRmax via Female-Specific Gulati Formula:</strong>
              $$HR_{\text{max (Gulati)}} = 206 - (0.88 \times 58) = 206 - 51.04 = \mathbf{154.96\text{ BPM}} \implies 155\text{ BPM}$$
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">4</div>
            <div class="step-content">
              <strong>Clinical Analysis &amp; Safety Threshold:</strong>
              Using the legacy formula (162 bpm) overestimates her maximum cardiac rate by 7 full beats per minute. If prescribed a 90% VO2 max interval session based on Fox ($162 \times 0.90 = 146\text{ BPM}$), she would actually be operating at <strong>94.2% of her true physiological maximum</strong> ($146 / 155$), substantially increasing myocardial ischemia risk. Prescribing based on the Gulati formula ($155 \times 0.90 = 139.5 \approx 140\text{ BPM}$) ensures physiological accuracy and cardiac safety.
            </div>
          </div>
        </div>
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
    function calculateHRMax() {
      const age = parseFloat(document.getElementById('hrmax-age').value) || 0;
      const gender = document.getElementById('hrmax-gender').value;
      const primaryMethod = document.getElementById('hrmax-primary').value;

      if (age <= 0) return;

      const hrmax_tanaka = Math.round(208 - (0.7 * age));
      const hrmax_gellish = Math.round(207 - (0.7 * age));
      const hrmax_gulati = Math.round(206 - (0.88 * age));
      const hrmax_fox = Math.round(220 - age);

      let hrmax_fairbarn = 0;
      if (gender === 'male') {
        hrmax_fairbarn = Math.round(201 - (0.63 * age));
      } else {
        hrmax_fairbarn = Math.round(216 - (1.09 * age));
      }

      let primaryVal = hrmax_tanaka;
      if (primaryMethod === 'gellish') primaryVal = hrmax_gellish;
      else if (primaryMethod === 'gulati') primaryVal = hrmax_gulati;
      else if (primaryMethod === 'fairbarn') primaryVal = hrmax_fairbarn;
      else if (primaryMethod === 'fox') primaryVal = hrmax_fox;

      document.getElementById('res-hrmax-primary').innerText = `${primaryVal} BPM`;
      document.getElementById('res-hrmax-range').innerText = `95% Statistical Confidence Band: ${primaryVal - 10} – ${primaryVal + 10} BPM (±10 bpm)`;
      document.getElementById('res-hrmax-gellish').innerText = `${hrmax_gellish} BPM`;
      document.getElementById('res-hrmax-gulati').innerText = `${hrmax_gulati} BPM`;
      document.getElementById('res-hrmax-fairbarn').innerText = `${hrmax_fairbarn} BPM`;
      document.getElementById('res-hrmax-fox').innerText = `${hrmax_fox} BPM`;

      // Intensity bands
      const modLow = Math.round(primaryVal * 0.64);
      const modHigh = Math.round(primaryVal * 0.76);
      const vigLow = Math.round(primaryVal * 0.77);
      const vigHigh = Math.round(primaryVal * 0.95);

      document.getElementById('res-intensity-targets').innerHTML = `Moderate Aerobic (64%–76%): <strong>${modLow} – ${modHigh} BPM</strong> | Vigorous / Threshold (77%–95%): <strong>${vigLow} – ${vigHigh} BPM</strong>.`;
    }

    document.addEventListener('DOMContentLoaded', calculateHRMax);
  </script>
</body>
</html>
"""

# -------------------------------------------------------------
# 6. met-calculator.html
# -------------------------------------------------------------
MET_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MET Calculator | Metabolic Equivalent of Task & MET-Minutes</title>
  <meta name="description" content="Calculate exercise intensity, calories burned, and weekly MET-minutes using the 2024 Ainsworth Compendium of Physical Activities and WHO health guidelines.">
  <link rel="canonical" href="https://calchub.com/met-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Clinical MET & Weekly MET-Minutes Calculator",
    "applicationCategory": "HealthApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0.00",
      "priceCurrency": "USD"
    },
    "description": "Calculates Metabolic Equivalent of Task (MET), oxygen uptake, energy expenditure in kcal, and weekly cumulative MET-minutes adhering to WHO physical activity recommendations."
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is the exact scientific definition of 1 MET?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "One Metabolic Equivalent of Task (1 MET) is standardized as the resting metabolic rate of an average seated adult, defined as an oxygen uptake (VO2) of 3.5 milliliters of oxygen per kilogram of body weight per minute (3.5 mL O2/kg/min), approximately equivalent to 1.0 kcal per kilogram per hour (1.0 kcal/kg/hr) or 4.184 kJ/kg/hr."
        }
      },
      {
        "@type": "Question",
        "name": "What are the WHO weekly MET-minute physical activity guidelines?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The World Health Organization (WHO) and CDC recommend achieving at least 500 to 1,000 MET-minutes per week of moderate-to-vigorous physical activity. This is equivalent to 150 to 300 minutes of moderate-intensity activity (3 to 6 METs) or 75 to 150 minutes of vigorous activity (> 6 METs) per week to significantly lower risks of cardiovascular mortality, stroke, and metabolic syndrome."
        }
      },
      {
        "@type": "Question",
        "name": "What are the intensity cutoffs for light, moderate, and vigorous METs?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Physical activity is clinically categorized into three distinct MET intensity tiers: Light-Intensity Activity is < 3.0 METs (slow walking, typing, standing); Moderate-Intensity Activity is 3.0 to 5.9 METs (brisk walking at 3.5 mph, leisurely cycling, active gardening); and Vigorous-Intensity Activity is ≥ 6.0 METs (jogging, competitive swimming, circuit training)."
        }
      },
      {
        "@type": "Question",
        "name": "What is the Byrne correction for MET calculations in overweight individuals?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "In 2005, Dr. Nuala Byrne and colleagues demonstrated that the standard 1 MET baseline (3.5 mL O2/kg/min) significantly overestimates true resting metabolic rate in overweight and obese individuals, whose resting oxygen consumption averages closer to 2.6 to 2.8 mL O2/kg/min due to the lower metabolic activity of adipose tissue per unit mass."
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
        <div class="badge-tag">Exercise Epidemiology</div>
        <h1 class="calculator-title">Metabolic Equivalent of Task (MET) Calculator</h1>
        <p class="calculator-description">Calculate physical work intensity, oxygen uptake ($VO_2$), caloric expenditure, and cumulative weekly MET-minutes based on the 2024 Ainsworth Compendium.</p>
      </div>

      <div class="calculator-grid">
        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Activity &amp; Frequency Parameters</h2>
          </div>
          <div class="calc-card-body">
            <div class="form-group">
              <label for="met-activity" class="form-label">Activity from 2024 Ainsworth Compendium</label>
              <select id="met-activity" class="form-select" onchange="syncMETInput()">
                <optgroup label="Light Activity (&lt; 3.0 METs)">
                  <option value="1.3">Desk work / Computer typing [1.3 METs]</option>
                  <option value="2.0">Slow stroll / Window shopping (2.0 mph) [2.0 METs]</option>
                  <option value="2.5">Stretching / Hatha yoga [2.5 METs]</option>
                </optgroup>
                <optgroup label="Moderate Intensity (3.0 – 5.9 METs)">
                  <option value="3.5" selected>Brisk fitness walking (3.5 mph / 5.6 km/h) [3.5 METs]</option>
                  <option value="4.0">Water aerobics / Calisthenics (moderate) [4.0 METs]</option>
                  <option value="5.0">Weight lifting / Free-weight resistance training [5.0 METs]</option>
                  <option value="5.5">Casual recreational cycling (10-12 mph) [5.5 METs]</option>
                </optgroup>
                <optgroup label="Vigorous Intensity (&ge; 6.0 METs)">
                  <option value="6.0">Cross-country hiking with daypack [6.0 METs]</option>
                  <option value="7.0">Swimming freestyle (moderate effort) [7.0 METs]</option>
                  <option value="8.0">High-Intensity Interval Training (HIIT) [8.0 METs]</option>
                  <option value="9.8">Running (6 mph / 10 min/mile pace) [9.8 METs]</option>
                  <option value="11.8">Running (8 mph / 7.5 min/mile pace) [11.8 METs]</option>
                  <option value="12.3">Jumping rope (fast pace, 120-140 rpm) [12.3 METs]</option>
                </optgroup>
              </select>
            </div>

            <div class="form-row" style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
              <div class="form-group">
                <label for="met-value" class="form-label">MET Value</label>
                <input type="number" id="met-value" class="form-input" value="3.5" min="0.8" max="25" step="0.1" oninput="calculateMETMetrics()">
              </div>
              <div class="form-group">
                <label for="met-duration" class="form-label">Duration (Mins / Session)</label>
                <input type="number" id="met-duration" class="form-input" value="45" min="1" max="600" step="5" oninput="calculateMETMetrics()">
              </div>
            </div>

            <div class="form-row" style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
              <div class="form-group">
                <label for="met-weight" class="form-label">Body Weight</label>
                <input type="number" id="met-weight" class="form-input" value="160" min="50" max="450" step="1" oninput="calculateMETMetrics()">
              </div>
              <div class="form-group">
                <label for="met-unit" class="form-label">Weight Unit</label>
                <select id="met-unit" class="form-select" onchange="calculateMETMetrics()">
                  <option value="lbs" selected>Pounds (lbs)</option>
                  <option value="kg">Kilograms (kg)</option>
                </select>
              </div>
            </div>

            <div class="form-group">
              <label for="met-frequency" class="form-label">Weekly Frequency (Sessions per Week)</label>
              <input type="number" id="met-frequency" class="form-input" value="4" min="1" max="14" step="1" oninput="calculateMETMetrics()">
              <span class="form-hint">Used to calculate weekly MET-minutes for WHO guidelines</span>
            </div>

            <button type="button" class="btn btn-primary" onclick="calculateMETMetrics()">Calculate MET Energy &amp; Volume</button>
          </div>
        </div>

        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Bioenergetics &amp; Weekly Volume</h2>
          </div>
          <div class="calc-card-body">
            <div class="result-hero" style="background:#f0fdf4;border-color:#bbf7d0;">
              <span class="hero-label">Weekly Exercise Volume</span>
              <div class="hero-value" id="res-weekly-met-min" style="color:#15803d;font-size:2.4rem;">630 MET-min</div>
              <span class="form-hint" id="res-who-status" style="font-weight:600;">Meets WHO Recommended Health Target (500 – 1000 MET-min/wk)</span>
            </div>

            <div class="results-grid" style="margin-top:1.5rem;">
              <div class="result-item">
                <span class="result-label">Single Session Energy</span>
                <span class="result-value" id="res-session-kcal">200 kcal</span>
              </div>
              <div class="result-item">
                <span class="result-label">Weekly Caloric Burn</span>
                <span class="result-value" id="res-weekly-kcal">800 kcal / wk</span>
              </div>
              <div class="result-item">
                <span class="result-label">Oxygen Uptake (VO2)</span>
                <span class="result-value" id="res-vo2">12.3 mL/kg/min</span>
              </div>
              <div class="result-item">
                <span class="result-label">Intensity Tier</span>
                <span class="result-value" id="res-intensity-tier">Moderate (3.5 METs)</span>
              </div>
            </div>

            <div class="stat-box" style="margin-top:1.5rem;padding:1rem;background:#f8fafc;border-radius:8px;border:1px solid #e2e8f0;">
              <h4 style="font-weight:700;margin-bottom:0.5rem;font-size:0.95rem;">Epidemiological Health &amp; Mortality Risk:</h4>
              <p id="res-epidemiology-note" style="font-size:0.875rem;color:#475569;margin:0;">
                Achieving 630 MET-minutes weekly is associated with a 20% to 25% reduction in all-cause mortality, lower incidence of coronary artery disease, and enhanced glycemic control.
              </p>
            </div>
          </div>
        </div>
      </div>

      <article class="article-body">
        <h2>The Concept of the Metabolic Equivalent of Task (MET)</h2>
        <p>
          In exercise epidemiology and preventive cardiology, quantifying the physical exertion of daily living and athletic sports across diverse populations requires an objective, mass-independent metric. In 1993, Dr. Barbara Ainsworth and an international committee of kinesiologists developed the <strong>Compendium of Physical Activities</strong>, establishing the <strong>Metabolic Equivalent of Task (MET)</strong> as the international standard.
        </p>
        <p>
          One MET represents the baseline resting energy expenditure of an average human adult:
        </p>

        <div class="formula-box">
          <p><strong>Universal Physiological Standardization of 1 MET:</strong></p>
          $$1\text{ MET} \equiv 3.5\text{ mL } O_2\text{ / kg body mass / minute} \approx 1.0\text{ kcal / kg / hour} \approx 4.184\text{ kJ / kg / hour}$$
          <p>
            An activity cataloged at 7.0 METs (such as moderate freestyle swimming) requires seven times the rate of oxygen uptake and cellular energy consumption as sitting quietly in an armchair.
          </p>
        </div>

        <h2>Mathematical Formulations: From Oxygen Uptake to Caloric Burn</h2>
        <p>
          The conversion from METs to mechanical oxygen consumption and gross caloric expenditure is derived through fundamental respiratory calorimetry:
        </p>
        $$\text{Gross } VO_2\text{ (mL/kg/min)} = \text{MET} \times 3.5$$
        $$\text{Energy Rate (kcal/min)} = \text{MET} \times \frac{3.5 \times \text{Weight (kg)}}{200}$$
        $$\text{Total Session Energy (kcal)} = \text{Energy Rate (kcal/min)} \times \text{Duration (min)}$$
        <p>
          To quantify physical activity dose over time, epidemiologists calculate <strong>MET-minutes</strong> or <strong>MET-hours</strong>:
        </p>
        $$\text{MET-Minutes} = \text{MET Value} \times \text{Duration in Minutes}$$
        $$\text{Weekly Physical Activity Dose} = \sum (\text{MET-Minutes per Session} \times \text{Weekly Sessions})$$

        <h2>WHO and CDC Physical Activity Guidelines</h2>
        <p>
          The <em>World Health Organization (WHO) Guidelines on Physical Activity and Sedentary Behaviour</em> and the US Department of Health and Human Services (HHS) define exercise volume targets using cumulative weekly MET-minutes:
        </p>
        <ul>
          <li><strong>Insufficient / Inactive (&lt; 500 MET-min/week):</strong> Sedentary lifestyle associated with elevated cardiovascular risk, insulin resistance, sarcopenia, and premature all-cause mortality.</li>
          <li><strong>Target Baseline (500 to 1,000 MET-min/week):</strong> The standard clinical recommendation. Achieved via 150 to 300 minutes of moderate-intensity activity (e.g., five 30-minute brisk walks at 3.5 METs $= 525\text{ MET-min}$) or 75 to 150 minutes of vigorous activity (e.g., three 25-minute runs at 10 METs $= 750\text{ MET-min}$).</li>
          <li><strong>Optimal Longevity Band (1,000 to 1,500 MET-min/week):</strong> Associated with maximal cardiovascular protection, optimal mitochondrial density, and a 31% to 37% reduction in premature mortality risk.</li>
          <li><strong>Diminishing Returns Ceiling (&gt; 3,000 MET-min/week):</strong> Characteristic of competitive endurance athletes. Provides high functional fitness with negligible incremental reduction in all-cause mortality.</li>
        </ul>

        <h2>The Byrne Correction in Obesity and Special Populations</h2>
        <p>
          While the classical value of $1\text{ MET} = 3.5\text{ mL } O_2/\text{kg/min}$ provides exceptional accuracy in young, normal-weight adults ($BMI < 25\text{ kg/m}^2$), clinical research by Dr. Nuala Byrne published in the <em>Journal of Applied Physiology</em> demonstrated significant divergence in overweight and obese populations:
        </p>
        <p>
          Adipose tissue is metabolically quiescent, consuming far less oxygen per gram of tissue than skeletal muscle, the liver, or kidneys. In individuals with significant adiposity ($BMI > 30\text{ kg/m}^2$), true resting metabolic rate averages <strong>2.6 to 2.8 mL O2/kg/min</strong> rather than 3.5. Utilizing the uncorrected 3.5 constant overestimates resting oxygen consumption by up to 25% to 35% in obese patients. Exercise physiologists applying METs to bariatric or metabolic syndrome cohorts frequently utilize adjusted resting denominators ($2.8\text{ mL/kg/min}$) to avoid inflating calculated caloric expenditure.
        </p>

        <h2>Comprehensive MET Intensity Taxonomy Table</h2>
        <p>
          The table below demonstrates representative activities across the three recognized physical activity intensity tiers:
        </p>

        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>Intensity Classification</th>
                <th>MET Range</th>
                <th>Compendium Activity Examples</th>
                <th>VO2 Demand (mL/kg/min)</th>
                <th>Physiological Substrate</th>
                <th>Talking Test Characteristic</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Light Intensity</strong></td>
                <td>1.0 – 2.9</td>
                <td>Desk typing (1.3), cooking (2.0), strolling (2.5)</td>
                <td>3.5 – 10.2</td>
                <td>&gt; 80% Fatty Acids</td>
                <td>Can sing or speak in continuous sentences with zero breathlessness.</td>
              </tr>
              <tr>
                <td><strong>Moderate Intensity</strong></td>
                <td>3.0 – 5.9</td>
                <td>Brisk walking 3.5 mph (3.5), circuit training (5.0), cycling 11 mph (5.5)</td>
                <td>10.5 – 20.7</td>
                <td>50% Fat, 50% Carbohydrates</td>
                <td>Can converse in comfortable sentences, but cannot sing without pausing for breath.</td>
              </tr>
              <tr>
                <td><strong>Vigorous Intensity</strong></td>
                <td>6.0 – 8.9</td>
                <td>Hiking daypack (6.0), swimming freestyle (7.0), HIIT (8.0)</td>
                <td>21.0 – 31.2</td>
                <td>70%–85% Carbohydrates</td>
                <td>Cannot speak more than a few words without stopping to catch breath.</td>
              </tr>
              <tr>
                <td><strong>Near-Maximal / Sprint</strong></td>
                <td>&ge; 9.0</td>
                <td>Running 6 mph (9.8), running 8 mph (11.8), jumping rope (12.3)</td>
                <td>&gt; 31.5</td>
                <td>&gt; 90% Glycogen &amp; PCr</td>
                <td>Gasping; speech impossible; sustained only for minutes.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2>Worked Exercise Epidemiology Case Study</h2>
        <div class="worked-example-card">
          <div class="example-header">
            <span class="example-badge">Public Health Case</span>
            <h3 class="example-title">Prescribing Physical Activity for Metabolic Syndrome</h3>
          </div>
          <div class="example-step">
            <div class="step-num">1</div>
            <div class="step-content">
              <strong>Patient Clinical Profile:</strong> A 52-year-old male with pre-diabetes and mild hypertension weighs 185 lbs (83.91 kg). His physician prescribes an exercise regimen to achieve the WHO target of <strong>750 MET-minutes per week</strong>. The patient chooses a combination of brisk walking (3.5 METs) on weekdays and recreational cycling (6.0 METs) on weekends.
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">2</div>
            <div class="step-content">
              <strong>Calculate Weekday Walking Volume (3 Days × 40 Minutes at 3.5 METs):</strong>
              $$\text{Session Volume} = 3.5\text{ METs} \times 40\text{ min} = \mathbf{140\text{ MET-minutes}}$$
              $$\text{3 Weekday Sessions} = 140 \times 3 = \mathbf{420\text{ MET-minutes}}$$
              $$\text{Weekday Caloric Burn} = 3 \times \left(3.5 \times \frac{3.5 \times 83.91}{200} \times 40\right) = 3 \times 205.6 = \mathbf{616.7\text{ kcal}}$$
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">3</div>
            <div class="step-content">
              <strong>Calculate Weekend Cycling Volume to Reach Target (Target Remaining = 330 MET-min):</strong>
              $$\text{Required Cycling Duration} = \frac{330\text{ MET-minutes}}{6.0\text{ METs}} = \mathbf{55\text{ minutes of cycling}}$$
              $$\text{Weekend Caloric Burn} = 6.0 \times \frac{3.5 \times 83.91}{200} \times 55 = 6.0 \times 1.4684 \times 55 = \mathbf{484.6\text{ kcal}}$$
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">4</div>
            <div class="step-content">
              <strong>Total Weekly Prescription &amp; Clinical Impact:</strong>
              $$\text{Total Weekly Volume} = 420 + 330 = \mathbf{750\text{ MET-minutes/week}}$$
              $$\text{Total Exercise Energy} = 616.7 + 484.6 = \mathbf{1,101.3\text{ kcal/week}}$$
              Meeting 750 MET-min/week upregulates skeletal muscle GLUT4 transporter expression, lowers fasting glucose, and satisfies the physical activity benchmark proven to halt progression to frank Type 2 Diabetes.
            </div>
          </div>
        </div>
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
    function syncMETInput() {
      const selectedMET = document.getElementById('met-activity').value;
      document.getElementById('met-value').value = selectedMET;
      calculateMETMetrics();
    }

    function calculateMETMetrics() {
      const met = parseFloat(document.getElementById('met-value').value) || 0;
      const duration = parseFloat(document.getElementById('met-duration').value) || 0;
      const weightVal = parseFloat(document.getElementById('met-weight').value) || 0;
      const unit = document.getElementById('met-unit').value;
      const freq = parseFloat(document.getElementById('met-frequency').value) || 0;

      if (met <= 0 || duration <= 0 || weightVal <= 0) return;

      const weightKg = (unit === 'lbs') ? (weightVal * 0.45359237) : weightVal;

      // Energy per min: MET * (3.5 * weightKg / 200)
      const kcalPerMin = met * (3.5 * weightKg / 200);
      const sessionKcal = Math.round(kcalPerMin * duration);
      const weeklyKcal = Math.round(sessionKcal * freq);

      // Volume: MET-min
      const sessionMETMin = Math.round(met * duration);
      const weeklyMETMin = Math.round(sessionMETMin * freq);

      // VO2
      const vo2 = (met * 3.5).toFixed(1);

      document.getElementById('res-weekly-met-min').innerText = `${weeklyMETMin.toLocaleString()} MET-min`;
      document.getElementById('res-session-kcal').innerText = `${sessionKcal.toLocaleString()} kcal`;
      document.getElementById('res-weekly-kcal').innerText = `${weeklyKcal.toLocaleString()} kcal / wk`;
      document.getElementById('res-vo2').innerText = `${vo2} mL/kg/min`;

      // Intensity tier
      let tier = 'Moderate';
      if (met < 3.0) tier = 'Light Intensity';
      else if (met >= 6.0) tier = 'Vigorous Intensity';
      document.getElementById('res-intensity-tier').innerText = `${tier} (${met} METs)`;

      // WHO Status
      const whoEl = document.getElementById('res-who-status');
      const epiEl = document.getElementById('res-epidemiology-note');

      if (weeklyMETMin < 500) {
        whoEl.innerText = 'Below WHO Recommended Target (< 500 MET-min/wk)';
        whoEl.style.color = '#ca8a04';
        epiEl.innerText = `Currently achieving ${weeklyMETMin} MET-minutes. Increasing frequency or duration to reach 500-1,000 MET-min/wk significantly reduces risks of stroke, cardiovascular disease, and metabolic syndrome.`;
      } else if (weeklyMETMin <= 1000) {
        whoEl.innerText = 'Meets WHO Recommended Health Target (500 – 1000 MET-min/wk)';
        whoEl.style.color = '#15803d';
        epiEl.innerText = `Achieving ${weeklyMETMin} MET-minutes weekly is associated with a 20% to 25% reduction in all-cause mortality, optimal blood pressure regulation, and enhanced glycemic control.`;
      } else {
        whoEl.innerText = 'Optimal Longevity & High Cardiorespiratory Volume (> 1000 MET-min/wk)';
        whoEl.style.color = '#1d4ed8';
        epiEl.innerText = `High activity volume (${weeklyMETMin} MET-minutes) confers near-maximal cardiovascular longevity, peak mitochondrial density, and strong protection against cardiometabolic disorders.`;
      }
    }

    document.addEventListener('DOMContentLoaded', calculateMETMetrics);
  </script>
</body>
</html>
"""

def generate_part3():
    with open(os.path.join(BASE_DIR, "max-heart-rate-calculator.html"), "w", encoding="utf-8") as f:
        f.write(MAX_HR_HTML)
    print("Generated max-heart-rate-calculator.html")

    with open(os.path.join(BASE_DIR, "met-calculator.html"), "w", encoding="utf-8") as f:
        f.write(MET_HTML)
    print("Generated met-calculator.html")

if __name__ == "__main__":
    generate_part3()
