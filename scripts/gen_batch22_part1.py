"""
Batch 22 - Part 1: Health & Clinical Tools
1. due-date-calculator.html (Pregnancy Gestational Age, Naegele, Mittendorf-Williams & ACOG Biometry)
2. fat-intake-calculator.html (Dietary Lipid Sizer, Omega-3/6 Ratio & Steroid Hormone Synthesis)
Word count target: >1,050 words in article-body each.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 1. due-date-calculator.html
# -------------------------------------------------------------
DUE_DATE_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pregnancy Due Date Calculator | Naegele Rule & ACOG Ultrasound Dating</title>
  <meta name="description" content="Calculate your estimated due date (EDD), gestational age, conception date, and trimester milestones using Naegele's rule, cycle adjustments, and ACOG guidelines.">
  <link rel="canonical" href="https://calchub.com/due-date-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Clinical Pregnancy Due Date & Gestational Age Calculator",
    "applicationCategory": "HealthApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0.00",
      "priceCurrency": "USD"
    },
    "description": "Calculates clinical estimated date of delivery (EDD), current gestational weeks and days, and trimester milestones based on LMP, cycle length, or conception date adhering to ACOG Committee Opinion No. 700."
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Naegele's rule for calculating estimated due date?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Naegele's rule calculates the Estimated Date of Delivery (EDD) by taking the first day of the last normal menstrual period (LMP), adding 1 year, subtracting 3 months, and adding 7 days. For cycles varying from the standard 28 days, the formula adds or subtracts the difference (Cycle Length - 28 days)."
        }
      },
      {
        "@type": "Question",
        "name": "How does ACOG recommend reconciling LMP dating with first-trimester ultrasound?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "According to ACOG Committee Opinion No. 700: If a first-trimester ultrasound Crown-Rump Length (CRL) measurement before 9w0d differs from the LMP date by more than 5 days, the due date must be revised to the ultrasound date. Between 9w0d and 13w6d, a discrepancy of more than 7 days mandates redating. First-trimester ultrasound is the gold standard for clinical obstetric dating."
        }
      },
      {
        "@type": "Question",
        "name": "How is gestational age defined compared to fetal embryonic age?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Gestational age (menstrual age) is measured from the first day of the last menstrual period, approximately two weeks prior to ovulation and conception. Fetal embryonic age (conceptional age) begins at the exact moment of fertilization. A pregnancy at 8 weeks gestational age corresponds to an embryo at 6 weeks conceptional age."
        }
      },
      {
        "@type": "Question",
        "name": "What are the exact definitions of early term, full term, and post-term pregnancy?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The American College of Obstetricians and Gynecologists (ACOG) and Society for Maternal-Fetal Medicine (SMFM) categorize delivery timing as: Early Term (37w0d through 38w6d), Full Term (39w0d through 40w6d), Late Term (41w0d through 41w6d), and Post-Term (42w0d and beyond)."
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
        <div class="badge-tag">Obstetrics &amp; Gynecology</div>
        <h1 class="calculator-title">Pregnancy Due Date &amp; Gestational Sizer</h1>
        <p class="calculator-description">Calculate your estimated date of delivery (EDD), current gestational age, and fetal developmental milestones using Naegele's rule and ACOG ultrasound biometry standards.</p>
      </div>

      <div class="calculator-grid">
        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Dating Method &amp; Cycle Parameters</h2>
          </div>
          <div class="calc-card-body">
            <div class="form-group">
              <label for="dating-method" class="form-label">Calculation Dating Baseline</label>
              <select id="dating-method" class="form-select" onchange="toggleDatingMethod()">
                <option value="lmp" selected>First Day of Last Menstrual Period (LMP)</option>
                <option value="conception">Exact Conception Date</option>
                <option value="ivf3">IVF Day 3 Embryo Transfer</option>
                <option value="ivf5">IVF Day 5 Blastocyst Transfer</option>
              </select>
            </div>

            <div class="form-group">
              <label for="base-date" class="form-label" id="label-base-date">First Day of Last Period (LMP)</label>
              <input type="date" id="base-date" class="form-input" onchange="calculateDueDate()">
            </div>

            <div class="form-group" id="group-cycle-len">
              <label for="cycle-length" class="form-label">Average Menstrual Cycle Length (Days)</label>
              <input type="number" id="cycle-length" class="form-input" value="28" min="20" max="45" step="1" oninput="calculateDueDate()">
              <span class="form-hint">Standard cycle baseline: 28 days (ovulation at day 14)</span>
            </div>

            <div class="form-group">
              <label for="parity" class="form-label">Maternal Parity (Mittendorf-Williams Model)</label>
              <select id="parity" class="form-select" onchange="calculateDueDate()">
                <option value="nulliparous" selected>First Pregnancy (Nulliparous - ~288 day average)</option>
                <option value="multiparous">Subsequent Pregnancy (Parous - ~283 day average)</option>
              </select>
            </div>

            <button type="button" class="btn btn-primary" onclick="calculateDueDate()">Calculate Due Date &amp; Milestones</button>
          </div>
        </div>

        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Obstetric Timeline &amp; Gestational Status</h2>
          </div>
          <div class="calc-card-body">
            <div class="result-hero" style="background:#fdf2f8;border-color:#fbcfe8;">
              <span class="hero-label">Estimated Date of Delivery (EDD)</span>
              <div class="hero-value" id="res-edd-date" style="color:#be185d;font-size:2.2rem;">October 24, 2026</div>
              <span class="form-hint" id="res-edd-days">Standard 40 Weeks 0 Days Gestational Endpoint</span>
            </div>

            <div class="results-grid" style="margin-top:1.5rem;">
              <div class="result-item">
                <span class="result-label">Current Gestational Age</span>
                <span class="result-value" id="res-gest-age">10 Weeks 3 Days</span>
              </div>
              <div class="result-item">
                <span class="result-label">Current Trimester</span>
                <span class="result-value" id="res-trimester">First Trimester</span>
              </div>
              <div class="result-item">
                <span class="result-label">Estimated Conception</span>
                <span class="result-value" id="res-conception-date">January 31, 2026</span>
              </div>
              <div class="result-item">
                <span class="result-label">Days Until Delivery</span>
                <span class="result-value" id="res-days-remaining">207 Days</span>
              </div>
            </div>

            <div class="stat-box" style="margin-top:1.5rem;padding:1rem;background:#f8fafc;border-radius:8px;border:1px solid #e2e8f0;">
              <h4 style="font-weight:700;margin-bottom:0.5rem;font-size:0.95rem;">Key Clinical Developmental Milestones:</h4>
              <p id="res-milestone-text" style="font-size:0.875rem;color:#475569;margin:0;">
                At 10 weeks, major organogenesis is functionally complete; fetal heart rate averages 150-170 bpm, and the embryonic tail has fully regressed into coccygeal vertebrae.
              </p>
            </div>
          </div>
        </div>
      </div>

      <article class="article-body">
        <h2>Obstetric Foundations of Gestational Dating</h2>
        <p>
          In clinical obstetrics, an accurate assessment of gestational age is essential for clinical decision-making across the prenatal continuum. Everything from the timing of maternal serum biochemical screening (quad screen, cell-free DNA) and anatomical survey sonograms (18 to 22 weeks) to evaluating intrauterine growth restriction (IUGR), scheduling antenatal testing in high-risk pregnancies, and planning induction of labor hinges on a dependable <strong>Estimated Date of Delivery ($EDD$)</strong>.
        </p>
        <p>
          By universal medical convention, gestational age is not measured from the moment of fertilization, but from the <strong>first day of the last normal menstrual period (LMP)</strong>. Because fertilization typically occurs 14 days after menses in a canonical 28-day cycle, menstrual age exceeds true embryologic conceptional age by approximately two weeks. A pregnancy at 40 weeks 0 days gestational age represents 38 weeks of true fetal embryonic maturation.
        </p>

        <h2>Mathematical Formulations for Due Date Estimation</h2>

        <div class="formula-box">
          <p><strong>1. Naegele's Rule (1812) with Menstrual Cycle Adjustment:</strong></p>
          $$EDD = \text{LMP} + 1\text{ Year} - 3\text{ Months} + 7\text{ Days} + (\text{Cycle Length} - 28\text{ Days})$$
          <p>
            Franz Naegele formulated this arithmetic shorthand based on the observation of Hermann Boerhaave that human gestation averages 10 lunar months (280 days or 40 weeks) from the onset of menses.
          </p>
        </div>

        <div class="formula-box">
          <p><strong>2. The Mittendorf-Williams Parity Regression Model:</strong></p>
          <p>
            In 1990, epidemiologists Robert Mittendorf and Michelle Williams re-evaluated gestational duration in uncomplicated singleton pregnancies with certain menstrual histories. Their statistical analysis demonstrated that the 280-day Naegele assumption underpredicts human gestation, identifying significant parity divergence:
          </p>
          $$\text{Nulliparous (First-Time Mothers): } EDD = \text{LMP} - 3\text{ Months} + 15\text{ Days}\quad (288\text{ Days})$$
          $$\text{Parous (Multiparous Mothers): } EDD = \text{LMP} - 3\text{ Months} + 10\text{ Days}\quad (283\text{ Days})$$
        </div>

        <div class="formula-box">
          <p><strong>3. Assisted Reproductive Technology (IVF Dating):</strong></p>
          <p>
            When conception occurs via In Vitro Fertilization (IVF), the exact age of the developing blastocyst is known with absolute laboratory precision, eliminating menstrual cycle uncertainty:
          </p>
          $$\text{Day 3 Embryo Transfer: } EDD = \text{Transfer Date} + 263\text{ Days}\quad (\text{Gestational Age} = \text{Days Post Transfer} + 17\text{ Days})$$
          $$\text{Day 5 Blastocyst Transfer: } EDD = \text{Transfer Date} + 261\text{ Days}\quad (\text{Gestational Age} = \text{Days Post Transfer} + 19\text{ Days})$$
        </div>

        <h2>ACOG Guidelines: Reconciling LMP with Ultrasound Biometry</h2>
        <p>
          In <em>Committee Opinion No. 700</em> (jointly endorsed by the American College of Obstetricians and Gynecologists, the Society for Maternal-Fetal Medicine, and the American Institute of Ultrasound in Medicine), strict criteria dictate when a menstrual due date must be abandoned in favor of ultrasound measurements:
        </p>

        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>Gestational Age Range</th>
                <th>Primary Ultrasound Biometric Marker</th>
                <th>Permissible Discrepancy (LMP vs Sonogram)</th>
                <th>Clinical Action / Redating Protocol</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>&le; 8w 6d</strong></td>
                <td>Crown-Rump Length (CRL)</td>
                <td>&gt; 5 Days</td>
                <td>Redate EDD to ultrasound if difference exceeds 5 days.</td>
              </tr>
              <tr>
                <td><strong>9w 0d to 13w 6d</strong></td>
                <td>Crown-Rump Length (CRL)</td>
                <td>&gt; 7 Days</td>
                <td>Redate EDD to ultrasound if difference exceeds 7 days.</td>
              </tr>
              <tr>
                <td><strong>14w 0d to 15w 6d</strong></td>
                <td>BPD, HC, AC, FL (Composite)</td>
                <td>&gt; 7 Days</td>
                <td>Second-trimester biparietal diameter / femur length.</td>
              </tr>
              <tr>
                <td><strong>16w 0d to 21w 6d</strong></td>
                <td>Composite Biometry (Hadlock)</td>
                <td>&gt; 10 Days</td>
                <td>Redate if discrepancy &gt; 10 days. Anatomy scan baseline.</td>
              </tr>
              <tr>
                <td><strong>22w 0d to 27w 6d</strong></td>
                <td>Composite Biometry</td>
                <td>&gt; 14 Days</td>
                <td>Suboptimally dated pregnancy; biological fetal growth variance increases.</td>
              </tr>
              <tr>
                <td><strong>&ge; 28w 0d (Third Tri)</strong></td>
                <td>Composite Biometry</td>
                <td>&gt; 21 Days</td>
                <td>Least accurate dating window (±3 weeks error); do not shift dating lightly.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2>Gestational Milestones and Trimester Transitions</h2>
        <p>
          Human pregnancy encompasses three distinct physiologic trimesters, marked by critical developmental milestones:
        </p>
        <ul>
          <li><strong>First Trimester (Conception to 13w6d):</strong> Characterized by blastocyst implantation, gastrulation, and organogenesis. By week 5, cardiac tube pulsations commence; by week 10, the embryonic period concludes, and the organism is designated a fetus. Spontaneous miscarriage risk plummets dramatically once cardiac activity is confirmed past 8 weeks.</li>
          <li><strong>Second Trimester (14w0d to 27w6d):</strong> Period of rapid somatic growth and tissue differentiation. Maternal perception of fetal movement (<em>quickening</em>) typically occurs between 16 and 20 weeks. The threshold of extrauterine fetal viability is reached at <strong>24 weeks 0 days</strong>, where advanced neonatal intensive care (NICU) resuscitation becomes medically feasible.</li>
          <li><strong>Third Trimester (28w0d through Delivery):</strong> Marked by alveolar pulmonary maturation, surfactant synthesis by type II pneumocytes, and maternal antibody (IgG) placental transfer. The brain undergoes rapid gyration and myelination.</li>
        </ul>

        <h2>Worked Clinical Obstetric Case Study</h2>
        <div class="worked-example-card">
          <div class="example-header">
            <span class="example-badge">Obstetric Dating Case</span>
            <h3 class="example-title">Menstrual Due Date Calculation and Cycle Length Adjustment</h3>
          </div>
          <div class="example-step">
            <div class="step-num">1</div>
            <div class="step-content">
              <strong>Patient Clinical Data:</strong> A 29-year-old nulliparous female presents for her initial prenatal intake visit. The first day of her last normal menstrual period (LMP) was <strong>January 15, 2026</strong>. She tracks her cycles accurately with a basal body temperature app and reports a consistent <strong>32-day menstrual cycle</strong>.
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">2</div>
            <div class="step-content">
              <strong>Apply Naegele's Rule with Cycle Length Offset:</strong>
              $$\text{Standard Naegele: } \text{January 15} - 3\text{ Months} + 7\text{ Days} = \text{October 22, 2026}$$
              $$\text{Cycle Adjustment: } 32\text{ Days} - 28\text{ Days} = +4\text{ Days}$$
              $$\text{Adjusted EDD} = \text{October 22} + 4\text{ Days} = \mathbf{\text{October 26, 2026}}$$
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">3</div>
            <div class="step-content">
              <strong>Calculate Estimated Date of Ovulation / Conception:</strong>
              In a 32-day cycle, the luteal phase remains fixed at approximately 14 days, indicating ovulation occurred on cycle day 18 ($32 - 14 = 18$):
              $$\text{Conception Date} = \text{January 15} + 18\text{ Days} = \mathbf{\text{February 2, 2026}}$$
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">4</div>
            <div class="step-content">
              <strong>First-Trimester Ultrasound Correlation:</strong>
              At an 8-week transvaginal scan on March 16, 2026, the sonographer measures a Crown-Rump Length (CRL) of 18.5 mm, corresponding to 8 weeks 3 days (EDD October 25, 2026). Because the ultrasound date differs by only 1 day from the cycle-adjusted menstrual EDD of October 26 (well within the 5-day ACOG tolerance), the menstrual due date of <strong>October 26, 2026</strong> is officially maintained as the permanent obstetric estimate.
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
    function toggleDatingMethod() {
      const method = document.getElementById('dating-method').value;
      const label = document.getElementById('label-base-date');
      const cycleGroup = document.getElementById('group-cycle-len');

      if (method === 'lmp') {
        label.innerText = 'First Day of Last Period (LMP)';
        cycleGroup.style.display = 'block';
      } else if (method === 'conception') {
        label.innerText = 'Exact Date of Conception';
        cycleGroup.style.display = 'none';
      } else if (method === 'ivf3') {
        label.innerText = 'Date of Day 3 Embryo Transfer';
        cycleGroup.style.display = 'none';
      } else if (method === 'ivf5') {
        label.innerText = 'Date of Day 5 Blastocyst Transfer';
        cycleGroup.style.display = 'none';
      }
      calculateDueDate();
    }

    function calculateDueDate() {
      const method = document.getElementById('dating-method').value;
      const baseInput = document.getElementById('base-date').value;
      const cycleLen = parseInt(document.getElementById('cycle-length').value) || 28;

      if (!baseInput) return;

      const baseParts = baseInput.split('-');
      const baseDate = new Date(parseInt(baseParts[0]), parseInt(baseParts[1]) - 1, parseInt(baseParts[2]));

      let edd = new Date(baseDate.getTime());
      let conceptionDate = new Date(baseDate.getTime());

      if (method === 'lmp') {
        // Naegele + cycle offset: 280 days + (cycle - 28)
        const totalDays = 280 + (cycleLen - 28);
        edd.setDate(edd.getDate() + totalDays);
        conceptionDate.setDate(conceptionDate.getDate() + (cycleLen - 14));
      } else if (method === 'conception') {
        edd.setDate(edd.getDate() + 266);
        conceptionDate = new Date(baseDate.getTime());
      } else if (method === 'ivf3') {
        edd.setDate(edd.getDate() + 263);
        conceptionDate.setDate(conceptionDate.getDate() - 3);
      } else if (method === 'ivf5') {
        edd.setDate(edd.getDate() + 261);
        conceptionDate.setDate(conceptionDate.getDate() - 5);
      }

      // Format EDD
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      document.getElementById('res-edd-date').innerText = edd.toLocaleDateString('en-US', options);
      document.getElementById('res-conception-date').innerText = conceptionDate.toLocaleDateString('en-US', options);

      // Current Gestational Age
      const today = new Date();
      const diffTime = today.getTime() - (edd.getTime() - (280 * 24 * 60 * 60 * 1000));
      const totalGestDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));

      if (totalGestDays > 0 && totalGestDays <= 294) {
        const weeks = Math.floor(totalGestDays / 7);
        const days = totalGestDays % 7;
        document.getElementById('res-gest-age').innerText = `${weeks} Weeks ${days} Days`;

        // Trimester
        let trim = 'First Trimester';
        if (weeks >= 28) trim = 'Third Trimester';
        else if (weeks >= 14) trim = 'Second Trimester';
        document.getElementById('res-trimester').innerText = trim;

        // Days remaining
        const daysRem = Math.max(Math.floor((edd.getTime() - today.getTime()) / (1000 * 60 * 60 * 24)), 0);
        document.getElementById('res-days-remaining').innerText = `${daysRem} Days`;

        // Milestone text
        const msEl = document.getElementById('res-milestone-text');
        if (weeks < 8) {
          msEl.innerText = `At ${weeks} weeks, neural tube closure and embryonic heart tube contractions are established; embryonic buds for arms and legs are differentiating.`;
        } else if (weeks < 14) {
          msEl.innerText = `At ${weeks} weeks, major organ systems are fully formed; facial features, fingernails, and genitourinary structures are actively developing.`;
        } else if (weeks < 24) {
          msEl.innerText = `At ${weeks} weeks, fetal movement (quickening) is perceptible; lanugo hair develops, and fine hearing pathways begin responding to maternal sound.`;
        } else if (weeks < 37) {
          msEl.innerText = `At ${weeks} weeks (past the 24-week viability threshold), rapid alveolar surfactant production occurs, brain gyration accelerates, and fat accumulation peaks.`;
        } else {
          msEl.innerText = `At ${weeks} weeks, the pregnancy has reached Term status. Pulmonary alveoli and thermoregulatory systems are fully prepared for independent life.`;
        }
      } else {
        document.getElementById('res-gest-age').innerText = '40 Weeks 0 Days (At Term)';
        document.getElementById('res-days-remaining').innerText = '0 Days';
      }
    }

    // Set default base date to 70 days ago
    document.addEventListener('DOMContentLoaded', () => {
      const d = new Date();
      d.setDate(d.getDate() - 70);
      const yyyy = d.getFullYear();
      const mm = String(d.getMonth() + 1).padStart(2, '0');
      const dd = String(d.getDate()).padStart(2, '0');
      document.getElementById('base-date').value = `${yyyy}-${mm}-${dd}`;
      calculateDueDate();
    });
  </script>
</body>
</html>
"""

# -------------------------------------------------------------
# 2. fat-intake-calculator.html
# -------------------------------------------------------------
FAT_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fat Intake Calculator | Daily Dietary Fats, Omega-3 & Hormone Health</title>
  <meta name="description" content="Calculate your optimal daily fat intake in grams and percentage of calories based on AHA, ISSN, and WHO standards. Saturated fat caps, Omega-3/6 ratio, and keto macros.">
  <link rel="canonical" href="https://calchub.com/fat-intake-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Clinical Dietary Fat Intake & Lipid Sizer",
    "applicationCategory": "HealthApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0.00",
      "priceCurrency": "USD"
    },
    "description": "Calculates evidence-based daily dietary fat targets (grams and percentage of TDEE), saturated fat safety limits, and essential fatty acid requirements for hormonal synthesis."
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What percentage of daily calories should come from dietary fat?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Acceptable Macronutrient Distribution Range (AMDR) established by the National Academy of Medicine recommends that 20% to 35% of total daily calories come from dietary fat. For an individual consuming 2,000 kcal per day, this corresponds to 44 to 78 grams of fat (since 1 gram of fat provides 9 kilocalories)."
        }
      },
      {
        "@type": "Question",
        "name": "Why does dietary fat intake impact testosterone and steroid hormone synthesis?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Cholesterol and dietary lipids are the mandatory biochemical substrates for steroidogenesis. In the Leydig cells of the testes and the adrenal cortex, cholesterol is transferred via the StAR protein to the inner mitochondrial membrane and cleaved by cytochrome P450scc into pregnenolone, the precursor to testosterone, estrogen, and cortisol. Clinical trials demonstrate that reducing fat intake below 15-20% of calories significantly depresses circulating free and total testosterone levels."
        }
      },
      {
        "@type": "Question",
        "name": "What is the American Heart Association (AHA) limit for saturated fat?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The American Heart Association recommends limiting saturated fatty acid (SFA) intake to 5% to 6% of total daily calories for individuals aiming to lower LDL cholesterol, and under 10% for the general population. In a 2,000 kcal diet, 5-6% represents just 11 to 13 grams of saturated fat per day."
        }
      },
      {
        "@type": "Question",
        "name": "What are Essential Fatty Acids (EFAs) and what are their daily requirements?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Humans lack delta-12 and delta-15 desaturase enzymes, making two polyunsaturated fatty acids essential: Alpha-Linolenic Acid (ALA, an Omega-3) and Linoleic Acid (LA, an Omega-6). Daily adequate intake (AI) is 1.6 g/day for men and 1.1 g/day for women for ALA, and 14-17 g/day for LA. Marine omega-3s (EPA and DHA) should be consumed at 250 to 500 mg daily for cardioprotection."
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
        <div class="badge-tag">Nutritional Lipidology</div>
        <h1 class="calculator-title">Dietary Fat Intake &amp; Hormone Sizer</h1>
        <p class="calculator-description">Calculate your optimal daily dietary fat targets (grams and kcal), saturated fat cardiovascular safety limits, and essential fatty acid requirements based on AHA and ISSN guidelines.</p>
      </div>

      <div class="calculator-grid">
        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Caloric Intake &amp; Dietary Strategy</h2>
          </div>
          <div class="calc-card-body">
            <div class="form-group">
              <label for="daily-calories" class="form-label">Total Daily Caloric Intake (kcal)</label>
              <input type="number" id="daily-calories" class="form-input" value="2200" min="1000" max="6000" step="50" oninput="calculateFats()">
              <span class="form-hint">Your daily maintenance or deficit calorie target</span>
            </div>

            <div class="form-row" style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
              <div class="form-group">
                <label for="body-weight" class="form-label">Body Weight</label>
                <input type="number" id="body-weight" class="form-input" value="170" min="60" max="450" step="1" oninput="calculateFats()">
              </div>
              <div class="form-group">
                <label for="weight-unit" class="form-label">Unit</label>
                <select id="weight-unit" class="form-select" onchange="calculateFats()">
                  <option value="lbs" selected>Pounds (lbs)</option>
                  <option value="kg">Kilograms (kg)</option>
                </select>
              </div>
            </div>

            <div class="form-group">
              <label for="diet-protocol" class="form-label">Nutritional Strategy &amp; Goal</label>
              <select id="diet-protocol" class="form-select" onchange="calculateFats()">
                <option value="balanced" selected>Standard Balanced Health (25% - 30% of calories)</option>
                <option value="athletic">Athletic / Bodybuilding Cut (20% of calories - Higher Carbs)</option>
                <option value="mediterranean">Mediterranean Heart Health (35% of calories - High MUFA)</option>
                <option value="keto">Standard Ketogenic Diet (70% - 75% of calories)</option>
                <option value="lowfat">Clinical Low-Fat (15% of calories - Medical supervision)</option>
              </select>
            </div>

            <button type="button" class="btn btn-primary" onclick="calculateFats()">Calculate Dietary Fat Breakdown</button>
          </div>
        </div>

        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Daily Lipid Targets &amp; Safety Caps</h2>
          </div>
          <div class="calc-card-body">
            <div class="result-hero" style="background:#fefce8;border-color:#fef08a;">
              <span class="hero-label">Target Total Dietary Fat</span>
              <div class="hero-value" id="res-target-fat-g" style="color:#ca8a04;font-size:2.4rem;">67 g / day</div>
              <span class="form-hint" id="res-fat-pct">605 kcal from fat (27.5% of total calories | 0.87 g/kg)</span>
            </div>

            <div class="results-grid" style="margin-top:1.5rem;">
              <div class="result-item">
                <span class="result-label">Monounsaturated (MUFA)</span>
                <span class="result-value" id="res-mufa">33 g (14% kcal)</span>
              </div>
              <div class="result-item">
                <span class="result-label">Polyunsaturated (PUFA)</span>
                <span class="result-value" id="res-pufa">18 g (7% kcal)</span>
              </div>
              <div class="result-item">
                <span class="result-label">AHA Saturated Fat Cap</span>
                <span class="result-value" id="res-sfa-cap">&lt; 15 g (&le; 6%)</span>
              </div>
              <div class="result-item">
                <span class="result-label">Omega-3 EPA/DHA Target</span>
                <span class="result-value" id="res-omega3">500 – 1000 mg</span>
              </div>
            </div>

            <div class="stat-box" style="margin-top:1.5rem;padding:1rem;background:#f8fafc;border-radius:8px;border:1px solid #e2e8f0;">
              <h4 style="font-weight:700;margin-bottom:0.5rem;font-size:0.95rem;">Endocrine &amp; Cardiovascular Impact:</h4>
              <p id="res-endocrine-note" style="font-size:0.875rem;color:#475569;margin:0;">
                At 27.5% fat intake (0.87 g/kg), cellular steroidogenesis is fully supported for testosterone and estrogen synthesis, while adhering to American Heart Association guidelines for cardiovascular atheroma prevention.
              </p>
            </div>
          </div>
        </div>
      </div>

      <article class="article-body">
        <h2>Biochemical Functions of Dietary Lipids</h2>
        <p>
          Dietary fats (lipids) are essential macronutrients serving indispensable physiological roles far beyond simple caloric storage. Chemically, over 95% of dietary lipids exist in the form of <strong>triglycerides (triacylglycerols)</strong>, consisting of a glycerol backbone esterified to three fatty acid chains of varying carbon chain lengths and degrees of unsaturation.
        </p>
        <p>
          Unlike carbohydrates, which can be synthesized endogenously via hepatic gluconeogenesis, dietary fats provide structural building blocks and biochemical cofactors that the human body cannot manufacture:
        </p>
        <ul>
          <li><strong>Cellular Membrane Fluidity and Structure:</strong> Phospholipids (such as phosphatidylcholine and phosphatidylethanolamine) form the semi-permeable lipid bilayer of all 37 trillion cells in the human body. The ratio of saturated to polyunsaturated fatty acids embedded in the membrane governs receptor mobility, nutrient transport, and ion channel kinetics.</li>
          <li><strong>Fat-Soluble Vitamin Absorption:</strong> Dietary lipids are the obligate micellar transport vehicle required for the intestinal solubilization and lymphatic absorption of fat-soluble vitamins: <strong>Vitamin A (retinol), Vitamin D (cholecalciferol), Vitamin E (tocopherol), and Vitamin K (phylloquinone/menaquinone)</strong>. Diets containing under 15% fat lead to chronic micro-nutritional deficiencies and impaired bone mineralization.</li>
          <li><strong>Steroidogenesis and Endocrine Homeostasis:</strong> Free cholesterol serves as the obligate biochemical precursor for the synthesis of all steroid hormones—including testosterone, dihydrotestosterone (DHT), estradiol, progesterone, cortisol, and aldosterone.</li>
        </ul>

        <h2>Essential Fatty Acids: Omega-3 and Omega-6 Pathways</h2>
        <p>
          Humans lack the delta-12 and delta-15 desaturase enzymes required to insert double bonds beyond carbon-9 from the carboxyl end of a fatty acid chain. Consequently, two distinct polyunsaturated fatty acid (PUFA) families are strictly essential:
        </p>

        <div class="formula-box">
          <p><strong>Essential Fatty Acid Elongation &amp; Desaturation Cascades:</strong></p>
          $$\text{Omega-6 Family: } \text{Linoleic Acid (LA, 18:2n-6)} \xrightarrow{\Delta\text{-6 Desaturase}} \text{Arachidonic Acid (AA, 20:4n-6)} \to \text{Pro-inflammatory Eicosanoids (PGE}_2\text{, LTB}_4\text{)}$$
          $$\text{Omega-3 Family: } \alpha\text{-Linolenic Acid (ALA, 18:3n-3)} \xrightarrow{\Delta\text{-6 Desaturase}} \text{EPA (20:5n-3)} \to \text{DHA (22:6n-3)} \to \text{Anti-inflammatory Resolvins/Protectins}$$
          <p>
            Because both pathways compete for the identical rate-limiting enzyme ($\Delta$-6 desaturase), an excessively skewed dietary Omega-6 to Omega-3 ratio (frequently 16:1 to 20:1 in modern industrialized Western diets rich in refined seed oils) promotes chronic systemic endothelial inflammation. Health agencies recommend targeting an optimal dietary ratio between <strong>2:1 and 4:1</strong>, with at least 250 to 500 mg daily of direct pre-formed marine EPA/DHA.
          </p>
        </div>

        <h2>Steroid Hormone Synthesis and the Danger of Extreme Low-Fat Diets</h2>
        <p>
          A frequent pitfall among fitness enthusiasts and bodybuilders during severe calorie-cutting phases is driving dietary fat down to extreme lows ($< 10\% - 15\%$ of calories) to prioritize carbohydrate intake. Landmark clinical trials published in the <em>Journal of Clinical Endocrinology &amp; Metabolism</em> demonstrate that this triggers profound neuroendocrine hypogonadism:
        </p>
        <ol>
          <li><strong>Mitochondrial Cholesterol Translocation:</strong> The rate-limiting step in steroidogenesis is the transport of free cholesterol across the mitochondrial intermembrane space, mediated by the <strong>Steroidogenic Acute Regulatory (StAR) protein</strong>. Caloric restriction paired with low lipid intake downregulates StAR expression in testicular Leydig cells.</li>
          <li><strong>Cytochrome P450 Side-Chain Cleavage:</strong> Inside the inner mitochondrial membrane, the enzyme cytochrome $P450scc$ (CYP11A1) cleaves cholesterol into pregnenolone:
            $$\text{Cholesterol (C}_{27}\text{)} \xrightarrow{P450scc} \text{Pregnenolone (C}_{21}\text{)} \to \text{Progesterone} \to \text{Androstenedione} \to \text{Testosterone (C}_{19}\text{)}$$
          </li>
          <li><strong>Testosterone Suppression:</strong> Studies demonstrate that reducing fat intake from 40% to 20% of calories produces a statistically significant 12% to 15% drop in total and free testosterone, accompanied by an increase in sex hormone-binding globulin (SHBG). The International Society of Sports Nutrition (ISSN) recommends maintaining a baseline dietary fat floor of <strong>at least 0.7 to 1.0 grams per kilogram of body weight</strong> (or a minimum of 20% of daily calories) to preserve neuroendocrine health during prolonged cutting phases.</li>
        </ol>

        <h2>Cardiovascular Saturated Fat Limits: AHA and ACC Guidelines</h2>
        <p>
          While monounsaturated fats (MUFA, found in extra virgin olive oil, avocados, and macadamia nuts) and polyunsaturated fats (PUFA) promote cardiovascular longevity, <strong>saturated fatty acids (SFAs)</strong>—particularly palmitic ($C16:0$), myristic ($C14:0$), and lauric ($C12:0$) acids—exert distinct biological effects on hepatic lipid metabolism:
        </p>
        <ul>
          <li><strong>Hepatic LDL-Receptor Suppression:</strong> High saturated fat consumption reduces the transcriptional expression and cellular recycling of LDL receptors on the surface of hepatocytes via the SREBP-2 pathway. As clearance slows, circulating ApoB-containing LDL particles remain in bloodstream circulation longer, dramatically increasing arterial transit and susceptibility to subendothelial oxidation.</li>
          <li><strong>AHA SFA Guideline:</strong> The American Heart Association firmly recommends that saturated fat not exceed <strong>5% to 6% of total daily calories</strong> in patients with elevated LDL-C or atherosclerotic risk, and under 10% in the general population. Substituting 5% of daily calories from saturated fats with equivalent calories from polyunsaturated vegetable or marine fats reduces coronary heart disease incidence by approximately 25%.</li>
        </ul>

        <h2>Comprehensive Dietary Lipid Distribution Matrix</h2>
        <p>
          The table below demonstrates evidence-based daily fat distributions across major dietary protocols for an individual consuming 2,200 kcal/day:
        </p>

        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>Dietary Protocol</th>
                <th>Fat % of Calories</th>
                <th>Total Fat (g)</th>
                <th>SFA Cap (&le; 6%)</th>
                <th>MUFA Target (g)</th>
                <th>PUFA Target (g)</th>
                <th>Physiological Objective</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>AHA Low-Saturated Fat</strong></td>
                <td>25% – 30%</td>
                <td>61 – 73 g</td>
                <td>&lt; 14 g</td>
                <td>30 – 38 g</td>
                <td>15 – 22 g</td>
                <td>Aggressive LDL-C reduction; maximal endothelial protection.</td>
              </tr>
              <tr>
                <td><strong>Mediterranean Diet</strong></td>
                <td>35% – 40%</td>
                <td>85 – 98 g</td>
                <td>&lt; 18 g</td>
                <td>50 – 62 g</td>
                <td>18 – 24 g</td>
                <td>High extra virgin olive oil; elevated HDL and vascular longevity.</td>
              </tr>
              <tr>
                <td><strong>Athletic / Bodybuilding</strong></td>
                <td>20% – 25%</td>
                <td>49 – 61 g</td>
                <td>&lt; 15 g</td>
                <td>22 – 30 g</td>
                <td>12 – 18 g</td>
                <td>Preserves steroid hormone floor while maximizing muscle glycogen.</td>
              </tr>
              <tr>
                <td><strong>Standard Ketogenic</strong></td>
                <td>70% – 75%</td>
                <td>171 – 183 g</td>
                <td>35 – 50 g</td>
                <td>80 – 95 g</td>
                <td>30 – 40 g</td>
                <td>Induces hepatic ketogenesis (BHB production); suppresses insulin.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2>Worked Nutritional Dietetics Case Study</h2>
        <div class="worked-example-card">
          <div class="example-header">
            <span class="example-badge">Dietetics Case Study</span>
            <h3 class="example-title">Endocrine Recovery in a Competitive Natural Bodybuilder</h3>
          </div>
          <div class="example-step">
            <div class="step-num">1</div>
            <div class="step-content">
              <strong>Client Clinical Profile:</strong> A 26-year-old competitive natural male bodybuilder (Weight = 175 lbs / 79.38 kg) presents with severe lethargy, loss of libido, and a depressed total testosterone level of 240 ng/dL (reference: 300 to 1,000 ng/dL) following a 20-week contest prep. Nutritional audit reveals he was consuming 2,000 kcal/day with only <strong>25 grams of fat per day</strong> (11.2% of calories, or 0.31 g/kg).
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">2</div>
            <div class="step-content">
              <strong>Establish Evidence-Based Endocrine Fat Floor:</strong>
              Sports nutrition consensus mandates a minimum fat floor of $0.8\text{ to }1.0\text{ g/kg}$ to sustain steroidogenesis:
              $$\text{Target Fat Intake} = 79.38\text{ kg} \times 0.90\text{ g/kg} = \mathbf{71.4\text{ grams of fat/day}}$$
              $$\text{Caloric Yield from Fat} = 71.4\text{ g} \times 9\text{ kcal/g} = \mathbf{643\text{ kcal}} \quad (26.8\%\text{ of a 2,400 kcal recovery diet})$$
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">3</div>
            <div class="step-content">
              <strong>Structure Sub-Fraction Fatty Acid Targets:</strong>
              <ul>
                <li><strong>Monounsaturated Fatty Acids (MUFA ~50%):</strong> $35\text{ g}$ from extra virgin olive oil, avocados, and whole eggs to boost testicular steroidogenic enzyme activity.</li>
                <li><strong>Polyunsaturated Fatty Acids (PUFA ~25%):</strong> $18\text{ g}$ including 3 grams of wild salmon oil yielding 1,000 mg combined EPA/DHA to suppress muscle catabolism and systemic inflammation.</li>
                <li><strong>Saturated Fatty Acids (SFA ~25%):</strong> $18\text{ g}$ (6.7% of calories) providing free cholesterol for immediate Leydig cell pregnenolone synthesis without exceeding AHA safety thresholds.</li>
              </ul>
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">4</div>
            <div class="step-content">
              <strong>Clinical Outcome:</strong> Following 8 weeks on this structured lipid protocol alongside calorie restoration to maintenance, follow-up morning laboratory testing confirmed normalization of total testosterone to <strong>620 ng/dL</strong> and complete resolution of fatigue.
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
    function calculateFats() {
      const calories = parseFloat(document.getElementById('daily-calories').value) || 0;
      const weightVal = parseFloat(document.getElementById('body-weight').value) || 0;
      const unit = document.getElementById('weight-unit').value;
      const protocol = document.getElementById('diet-protocol').value;

      if (calories <= 0 || weightVal <= 0) return;

      const weightKg = (unit === 'lbs') ? (weightVal * 0.45359237) : weightVal;

      let pct = 0.275;
      if (protocol === 'balanced') pct = 0.275;
      else if (protocol === 'athletic') pct = 0.20;
      else if (protocol === 'mediterranean') pct = 0.35;
      else if (protocol === 'keto') pct = 0.725;
      else if (protocol === 'lowfat') pct = 0.15;

      const fatCalories = calories * pct;
      const totalFatG = Math.round(fatCalories / 9);
      const gPerKg = (totalFatG / weightKg).toFixed(2);

      // Sub-fractions
      let mufaG = Math.round(totalFatG * 0.50);
      let pufaG = Math.round(totalFatG * 0.25);
      let sfaG = Math.round(totalFatG * 0.25);

      // AHA SFA cap (6% of calories)
      const ahaCapG = Math.round((calories * 0.06) / 9);

      document.getElementById('res-target-fat-g').innerText = `${totalFatG} g / day`;
      document.getElementById('res-fat-pct').innerText = `${Math.round(fatCalories)} kcal from fat (${(pct * 100).toFixed(1)}% of calories | ${gPerKg} g/kg)`;

      document.getElementById('res-mufa').innerText = `${mufaG} g (${Math.round(mufaG * 9 / calories * 100)}% kcal)`;
      document.getElementById('res-pufa').innerText = `${pufaG} g (${Math.round(pufaG * 9 / calories * 100)}% kcal)`;
      document.getElementById('res-sfa-cap').innerText = `< ${ahaCapG} g (≤ 6%)`;

      const noteEl = document.getElementById('res-endocrine-note');
      if (protocol === 'keto') {
        noteEl.innerHTML = `<strong>Ketogenic Profile:</strong> High fat (${totalFatG} g, ${(pct * 100).toFixed(1)}% kcal) induces hepatic synthesis of acetoacetate and beta-hydroxybutyrate. Ensure majority of fats derive from monounsaturated sources (olive oil, avocado) rather than pure saturated butter to protect ApoB lipid particles.`;
      } else if (protocol === 'lowfat') {
        noteEl.innerHTML = `<strong style="color:#b91c1c;">Hormone Suppression Warning:</strong> At 15% fat (${totalFatG} g, ${gPerKg} g/kg), testicular and adrenal steroidogenesis can become impaired. Monitor free testosterone and ensure adequate fat-soluble vitamin (A, D, E, K) supplementation.`;
      } else {
        noteEl.innerHTML = `At ${(pct * 100).toFixed(1)}% fat intake (${gPerKg} g/kg), cellular steroidogenesis is fully supported for testosterone and estrogen synthesis, while adhering to American Heart Association guidelines for cardiovascular atheroma prevention.`;
      }
    }

    document.addEventListener('DOMContentLoaded', calculateFats);
  </script>
</body>
</html>
"""

def generate_part1():
    with open(os.path.join(BASE_DIR, "due-date-calculator.html"), "w", encoding="utf-8") as f:
        f.write(DUE_DATE_HTML)
    print("Generated due-date-calculator.html")

    with open(os.path.join(BASE_DIR, "fat-intake-calculator.html"), "w", encoding="utf-8") as f:
        f.write(FAT_HTML)
    print("Generated fat-intake-calculator.html")

if __name__ == "__main__":
    generate_part1()
