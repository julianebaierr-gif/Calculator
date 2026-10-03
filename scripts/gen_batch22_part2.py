"""
Batch 22 - Part 2: Health & Fitness Tools
3. heart-rate-zone-calculator.html (Karvonen Heart Rate Reserve HRR & 5-Zone Model)
4. lean-body-mass-calculator.html (Boer, James, Hume LBM & Normalized FFMI Sizer)
Word count target: >1,050 words in article-body each.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 3. heart-rate-zone-calculator.html
# -------------------------------------------------------------
HR_ZONE_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Heart Rate Zone Calculator | Karvonen HRR & 5-Zone Training Model</title>
  <meta name="description" content="Calculate your customized 5 aerobic training heart rate zones using the Karvonen formula (Heart Rate Reserve) and Tanaka/Gellish HRmax formulas. Optimize Zone 2 and lactate threshold.">
  <link rel="canonical" href="https://calchub.com/heart-rate-zone-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Karvonen 5-Zone Heart Rate Training Calculator",
    "applicationCategory": "HealthApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0.00",
      "priceCurrency": "USD"
    },
    "description": "Calculates individualized 5-zone cardiovascular training heart rates using the Karvonen Heart Rate Reserve (HRR) formula and Tanaka/Gellish maximum heart rate equations."
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is the Karvonen formula for target heart rate?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Karvonen formula calculates Target Heart Rate (THR) using Heart Rate Reserve (HRR): THR = (HRmax - HRrest) × Intensity % + HRrest. By incorporating resting heart rate (HRrest), the Karvonen method personalizes training zones to an individual's cardiovascular fitness level far more accurately than straight percentages of maximum heart rate."
        }
      },
      {
        "@type": "Question",
        "name": "Why is Zone 2 aerobic training so vital for endurance and metabolic health?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Zone 2 (60% to 70% HRR or ~65% to 75% HRmax) represents the highest training intensity where cellular ATP is produced almost exclusively through mitochondrial fat oxidation without accumulating systemic blood lactate (< 2.0 mmol/L). It stimulates mitochondrial biogenesis, enhances capillary density, and upregulates carnitine palmitoyltransferase-1 (CPT-1)."
        }
      },
      {
        "@type": "Question",
        "name": "What formula is most accurate for estimating maximum heart rate?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Tanaka formula [HRmax = 208 - (0.7 × Age)] and Gellish formula [HRmax = 207 - (0.7 × Age)] are scientifically superior to the traditional '220 - Age' formula (Fox formula), which significantly overestimates HRmax in young adults and underestimates HRmax in older individuals."
        }
      },
      {
        "@type": "Question",
        "name": "How does resting heart rate reflect cardiovascular conditioning?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Resting heart rate reflects stroke volume and autonomic parasympathetic (vagal) tone. Chronic endurance training causes eccentric ventricular hypertrophy, allowing the left ventricle to pump more blood per beat (higher stroke volume), thereby reducing the required resting heart rate to 40-55 bpm in elite athletes versus 65-80 bpm in untrained adults."
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
        <h1 class="calculator-title">Heart Rate Zone &amp; Karvonen Calculator</h1>
        <p class="calculator-description">Calculate your personalized 5 training heart rate zones using the Karvonen Heart Rate Reserve (HRR) equation and peer-reviewed Tanaka HRmax algorithms.</p>
      </div>

      <div class="calculator-grid">
        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Cardiovascular Inputs</h2>
          </div>
          <div class="calc-card-body">
            <div class="form-row" style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
              <div class="form-group">
                <label for="hr-age" class="form-label">Age (Years)</label>
                <input type="number" id="hr-age" class="form-input" value="35" min="15" max="100" step="1" oninput="calculateZones()">
              </div>
              <div class="form-group">
                <label for="hr-rest" class="form-label">Resting Heart Rate (BPM)</label>
                <input type="number" id="hr-rest" class="form-input" value="62" min="35" max="120" step="1" oninput="calculateZones()">
                <span class="form-hint">Measured upon waking in morning</span>
              </div>
            </div>

            <div class="form-group">
              <label for="hrmax-method" class="form-label">HRmax Estimation Formula</label>
              <select id="hrmax-method" class="form-select" onchange="calculateZones()">
                <option value="tanaka" selected>Tanaka Formula: 208 - (0.7 × Age) [Recommended]</option>
                <option value="gellish">Gellish Formula: 207 - (0.7 × Age)</option>
                <option value="fox">Fox Formula: 220 - Age [Classic Legacy]</option>
                <option value="custom">Custom Known Max HR (from laboratory VO2 max test)</option>
              </select>
            </div>

            <div class="form-group" id="group-custom-hr" style="display:none;">
              <label for="custom-hrmax" class="form-label">Known Laboratory Maximum HR (BPM)</label>
              <input type="number" id="custom-hrmax" class="form-input" value="185" min="120" max="230" step="1" oninput="calculateZones()">
            </div>

            <div class="form-group">
              <label for="zone-method" class="form-label">Calculation Methodology</label>
              <select id="zone-method" class="form-select" onchange="calculateZones()">
                <option value="karvonen" selected>Karvonen Heart Rate Reserve (Personalized by Resting HR)</option>
                <option value="percent_max">Standard Percentage of Max HR (% HRmax)</option>
              </select>
            </div>

            <button type="button" class="btn btn-primary" onclick="calculateZones()">Compute Training Zones</button>
          </div>
        </div>

        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Training Zones &amp; Bioenergetics</h2>
          </div>
          <div class="calc-card-body">
            <div class="result-hero" style="background:#eff6ff;border-color:#bfdbfe;">
              <span class="hero-label">Mitochondrial Zone 2 (Base Aerobic)</span>
              <div class="hero-value" id="res-zone2" style="color:#1d4ed8;font-size:2.2rem;">135 – 148 BPM</div>
              <span class="form-hint">Maximal lipid oxidation (FatMax) &amp; lactate clearance (&lt; 2.0 mmol/L)</span>
            </div>

            <div class="results-grid" style="margin-top:1.5rem;">
              <div class="result-item">
                <span class="result-label">Estimated HRmax</span>
                <span class="result-value" id="res-hrmax">184 BPM</span>
              </div>
              <div class="result-item">
                <span class="result-label">Heart Rate Reserve (HRR)</span>
                <span class="result-value" id="res-hrr">122 BPM</span>
              </div>
              <div class="result-item">
                <span class="result-label">Zone 1 (Active Recovery)</span>
                <span class="result-value" id="res-zone1">123 – 135 BPM</span>
              </div>
              <div class="result-item">
                <span class="result-label">Zone 3 (Aerobic Tempo)</span>
                <span class="result-value" id="res-zone3">148 – 160 BPM</span>
              </div>
              <div class="result-item">
                <span class="result-label">Zone 4 (Lactate Threshold)</span>
                <span class="result-value" id="res-zone4">160 – 172 BPM</span>
              </div>
              <div class="result-item">
                <span class="result-label">Zone 5 (VO2 Max Interval)</span>
                <span class="result-value" id="res-zone5">172 – 184 BPM</span>
              </div>
            </div>

            <div class="stat-box" style="margin-top:1.5rem;padding:1rem;background:#f8fafc;border-radius:8px;border:1px solid #e2e8f0;">
              <h4 style="font-weight:700;margin-bottom:0.5rem;font-size:0.95rem;">Polarized 80/20 Training Distribution:</h4>
              <p id="res-hr-note" style="font-size:0.875rem;color:#475569;margin:0;">
                Elite endurance athletes spend approximately 80% of total weekly volume in Zone 2 to build mitochondrial mass and fat oxidation, with 20% in Zones 4-5 to elevate VO2 max and anaerobic buffering capacity.
              </p>
            </div>
          </div>
        </div>
      </div>

      <article class="article-body">
        <h2>Cardiovascular Physiology and the Energetics of Heart Rate</h2>
        <p>
          During physical exertion, cardiac output ($CO$, in liters per minute) must scale linearly with systemic metabolic demand. According to the <em>Fick Principle</em>, total oxygen consumption ($VO_2$) equals cardiac output multiplied by the arteriovenous oxygen difference ($a\text{-}\bar{v}O_2\text{ diff}$):
        </p>
        $$VO_2 = CO \times (C_aO_2 - C_vO_2) = (HR \times SV) \times (C_aO_2 - C_vO_2)$$
        <p>
          In healthy adult athletes, <strong>stroke volume ($SV$)</strong>—the volume of oxygenated blood ejected by the left ventricle per beat—reaches its physiological plateau at approximately 40% to 50% of $VO_2\text{max}$. Beyond this threshold, further escalations in cardiac output and tissue oxygen delivery must be driven almost entirely by increases in <strong>Heart Rate ($HR$)</strong>, mediated by sympathetic adrenergic stimulation ($\beta_1$-receptor activation via epinephrine and norepinephrine) and parasympathetic vagal withdrawal.
        </p>
        <p>
          Because heart rate tracks systemic oxygen uptake so reliably across submaximal exercise, monitoring beats per minute (BPM) provides an exceptionally accessible proxy for internal physiological strain, lactate accumulation, and autonomic fatigue.
        </p>

        <h2>Mathematical Formulations: Fox vs. Tanaka vs. Karvonen</h2>

        <div class="formula-box">
          <p><strong>1. Maximum Heart Rate (HRmax) Estimation Models:</strong></p>
          <ul>
            <li><strong>Tanaka Equation (2001) - Validated Across 18,712 Subjects:</strong>
              $$HR_{\text{max}} = 208 - (0.7 \times \text{Age})$$
            </li>
            <li><strong>Gellish Equation (2007) - Longitudinal Stress-Testing Model:</strong>
              $$HR_{\text{max}} = 207 - (0.7 \times \text{Age})$$
            </li>
            <li><strong>Fox &amp; Haskell Formula (1971) - Legacy Formula:</strong>
              $$HR_{\text{max}} = 220 - \text{Age}$$
              <em>Clinical Note:</em> The Fox formula overestimates HRmax in young adults (under 30) and progressively underestimates true HRmax in master athletes over 50 by as much as 10 to 15 bpm.
            </li>
          </ul>
        </div>

        <div class="formula-box">
          <p><strong>2. The Karvonen Heart Rate Reserve (HRR) Equation:</strong></p>
          <p>
            In 1957, Finnish physiologist Dr. Martti Karvonen recognized that simple percentages of $HR_{\text{max}}$ ignore an individual's baseline resting fitness. Two 40-year-old individuals with identical estimated maximum heart rates (180 bpm) have radically different cardiovascular capabilities if one has a resting heart rate of 45 bpm (elite marathoner) while the other has a resting rate of 80 bpm (sedentary desk worker).
          </p>
          $$\text{Heart Rate Reserve (HRR)} = HR_{\text{max}} - HR_{\text{rest}}$$
          $$\text{Target Heart Rate (THR)} = (HRR \times \text{Target Intensity \%}) + HR_{\text{rest}}$$
        </div>

        <h2>Deconstructing the 5 Cardiovascular Training Zones</h2>
        <p>
          The standardized 5-zone cardiovascular training model structures training intensity into specific bioenergetic domains:
        </p>

        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>Training Zone</th>
                <th>Intensity Range (% HRR)</th>
                <th>Physiological Substrate</th>
                <th>Blood Lactate Level</th>
                <th>Primary Adaptations &amp; Purpose</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Zone 1: Active Recovery</strong></td>
                <td>50% – 60%</td>
                <td>90% Fatty Acids</td>
                <td>&lt; 1.2 mmol/L</td>
                <td>Post-race recovery; flushing cellular metabolic byproducts; joint mobility.</td>
              </tr>
              <tr>
                <td><strong>Zone 2: Aerobic Base (FatMax)</strong></td>
                <td>60% – 70%</td>
                <td>70%–85% Fatty Acids</td>
                <td>1.2 – 2.0 mmol/L (LT1)</td>
                <td>Mitochondrial biogenesis, capillary sprouting, CPT-1 enzyme upregulation.</td>
              </tr>
              <tr>
                <td><strong>Zone 3: Aerobic Tempo</strong></td>
                <td>70% – 80%</td>
                <td>50% Glycogen, 50% Fat</td>
                <td>2.0 – 3.5 mmol/L</td>
                <td>Marathon pace specificity; glycogen economy; cardiac stroke volume max.</td>
              </tr>
              <tr>
                <td><strong>Zone 4: Lactate Threshold</strong></td>
                <td>80% – 90%</td>
                <td>85% Glycogen</td>
                <td>3.5 – 5.0 mmol/L (LT2)</td>
                <td>Increases maximal lactate steady state (MLSS); fractional $VO_2$ utilization.</td>
              </tr>
              <tr>
                <td><strong>Zone 5: VO2 Max Interval</strong></td>
                <td>90% – 100%</td>
                <td>&gt; 95% Glycogen / PCr</td>
                <td>&gt; 6.0 mmol/L</td>
                <td>Increases absolute $VO_2\text{max}$; expands stroke volume; neuromuscular motor recruitment.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2>Zone 2 Bioenergetics: Inigo San Millan's Cellular Paradigm</h2>
        <p>
          In modern exercise science, research spearheaded by Dr. Inigo San Millan (metabolic coach to Tour de France champions) underscores that <strong>Zone 2 training</strong> is the single most powerful driver of cellular metabolic health. In Zone 2 (demarcated physiologically at the first lactate turnpoint, $LT1$, typically around $1.5\text{ to }2.0\text{ mmol/L}$ of blood lactate):
        </p>
        <ul>
          <li><strong>Slow-Twitch (Type I) Muscle Fiber Recruitment:</strong> Type I oxidative fibers are packed with high concentrations of mitochondria, myoglobin, and oxidative enzymes. Zone 2 exercise stresses these fibers continuously without activating high-threshold fast-twitch (Type IIa/IIx) fibers that produce massive surges of lactate and hydrogen ions.</li>
          <li><strong>Mitochondrial Fatty Acid Transport (CPT-1):</strong> Carnitine Palmitoyltransferase-1 ($CPT-1$) is the enzyme responsible for shuttling long-chain fatty acids into the mitochondrial matrix for $\beta$-oxidation. As exercise intensity crosses into Zone 3 and 4, rising intracellular malonyl-CoA and glycolytic flux inhibit CPT-1, turning off fat oxidation completely. Zone 2 maximizes total fatty acid oxidation ($FatMax$).</li>
          <li><strong>Lactate Clearance Kinetics:</strong> Lactate is not a waste product; it is a high-energy metabolic fuel. Slow-twitch muscle fibers clear and oxidize lactate via <strong>Monocarboxylate Transporter 1 (MCT1)</strong> and mitochondrial lactate dehydrogenase ($mLDH$). Zone 2 training upregulates MCT1 density, transforming the musculoskeletal system into a metabolic sponge that vacuums up lactate produced by fast-twitch fibers during high-intensity surges.</li>
        </ul>

        <h2>Worked Exercise Physiology Case Study</h2>
        <div class="worked-example-card">
          <div class="example-header">
            <span class="example-badge">Cardiovascular Physiology Case</span>
            <h3 class="example-title">Karvonen Zone 2 Sizing for an Ultra-Endurance Runner</h3>
          </div>
          <div class="example-step">
            <div class="step-num">1</div>
            <div class="step-content">
              <strong>Athlete Profile:</strong> A 42-year-old male trail runner preparing for a 50-mile ultramarathon. Anthropometrics and testing: Resting heart rate ($HR_{\text{rest}}$) measured at <strong>48 BPM</strong> on waking. The coach uses the Tanaka formula to estimate maximum heart rate and sets up his 5 Karvonen training zones.
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">2</div>
            <div class="step-content">
              <strong>Calculate Maximum Heart Rate and Heart Rate Reserve:</strong>
              $$HR_{\text{max}} = 208 - (0.7 \times 42) = 208 - 29.4 = \mathbf{178.6\text{ BPM}} \implies 179\text{ BPM}$$
              $$HRR = HR_{\text{max}} - HR_{\text{rest}} = 179 - 48 = \mathbf{131\text{ BPM}}$$
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">3</div>
            <div class="step-content">
              <strong>Calculate Karvonen Zone 2 Boundaries (60% to 70% HRR):</strong>
              $$\text{Zone 2 Floor (60\%)} = (131 \times 0.60) + 48 = 78.6 + 48 = \mathbf{127\text{ BPM}}$$
              $$\text{Zone 2 Ceiling (70\%)} = (131 \times 0.70) + 48 = 91.7 + 48 = \mathbf{140\text{ BPM}}$$
              Zone 2 Target: <strong>127 to 140 BPM</strong>.
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">4</div>
            <div class="step-content">
              <strong>Comparison with Standard Straight % HRmax Method:</strong>
              If calculated solely as 60%–70% of $HR_{\text{max}}$ ($179 \times 0.60 = 107\text{ BPM}$; $179 \times 0.70 = 125\text{ BPM}$), the resulting range (107–125 BPM) would severely under-target the athlete's aerobic capacity due to his elite resting heart rate. The Karvonen formula correctly anchors training zones to true functional physiology.
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
    function calculateZones() {
      const age = parseFloat(document.getElementById('hr-age').value) || 0;
      const rest = parseFloat(document.getElementById('hr-rest').value) || 0;
      const hrmaxMethod = document.getElementById('hrmax-method').value;
      const zoneMethod = document.getElementById('zone-method').value;

      const customGroup = document.getElementById('group-custom-hr');
      if (hrmaxMethod === 'custom') {
        customGroup.style.display = 'block';
      } else {
        customGroup.style.display = 'none';
      }

      if (age <= 0 || rest <= 0) return;

      let hrmax = 185;
      if (hrmaxMethod === 'tanaka') {
        hrmax = Math.round(208 - (0.7 * age));
      } else if (hrmaxMethod === 'gellish') {
        hrmax = Math.round(207 - (0.7 * age));
      } else if (hrmaxMethod === 'fox') {
        hrmax = Math.round(220 - age);
      } else if (hrmaxMethod === 'custom') {
        hrmax = parseFloat(document.getElementById('custom-hrmax').value) || 185;
      }

      const hrr = Math.max(hrmax - rest, 40);

      function getZoneBPM(lowPct, highPct) {
        if (zoneMethod === 'karvonen') {
          const low = Math.round((hrr * lowPct) + rest);
          const high = Math.round((hrr * highPct) + rest);
          return `${low} – ${high} BPM`;
        } else {
          const low = Math.round(hrmax * lowPct);
          const high = Math.round(hrmax * highPct);
          return `${low} – ${high} BPM`;
        }
      }

      const z1 = getZoneBPM(0.50, 0.60);
      const z2 = getZoneBPM(0.60, 0.70);
      const z3 = getZoneBPM(0.70, 0.80);
      const z4 = getZoneBPM(0.80, 0.90);
      const z5 = getZoneBPM(0.90, 1.00);

      document.getElementById('res-hrmax').innerText = `${hrmax} BPM`;
      document.getElementById('res-hrr').innerText = `${hrr} BPM`;
      document.getElementById('res-zone1').innerText = z1;
      document.getElementById('res-zone2').innerText = z2;
      document.getElementById('res-zone3').innerText = z3;
      document.getElementById('res-zone4').innerText = z4;
      document.getElementById('res-zone5').innerText = z5;
    }

    document.addEventListener('DOMContentLoaded', calculateZones);
  </script>
</body>
</html>
"""

# -------------------------------------------------------------
# 4. lean-body-mass-calculator.html
# -------------------------------------------------------------
LBM_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lean Body Mass Calculator | Boer, James, Hume Formulas & FFMI Sizer</title>
  <meta name="description" content="Calculate your Lean Body Mass (LBM in kg/lbs) using Boer, James, and Hume formulas, plus Fat-Free Mass Index (FFMI) and natural muscular potential ceilings.">
  <link rel="canonical" href="https://calchub.com/lean-body-mass-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Clinical Lean Body Mass & Normalized FFMI Calculator",
    "applicationCategory": "HealthApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0.00",
      "priceCurrency": "USD"
    },
    "description": "Calculates Lean Body Mass (LBM) across Boer, James, and Hume clinical formulas, and determines height-normalized Fat-Free Mass Index (FFMI) for muscular potential evaluation."
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is the difference between Lean Body Mass (LBM) and Fat-Free Mass (FFM)?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "In strict multi-compartment body composition models: Fat-Free Mass (FFM) contains strictly zero lipid content (consisting entirely of water, protein, and bone mineral). Lean Body Mass (LBM) includes essential structural lipids found in cellular membranes, bone marrow, and the central nervous system (~3% in men, ~9-12% in women). In clinical medicine and sports science, the terms are frequently used interchangeably."
        }
      },
      {
        "@type": "Question",
        "name": "Which formula is considered the modern clinical standard for Lean Body Mass?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Boer formula (1984) is widely recognized as the clinical standard in pharmacokinetics, anesthesiology, and nephrology. Unlike the older James formula (which can paradoxically calculate declining LBM in severe obesity), the Boer equation maintains consistent linearity across wide ranges of body mass index."
        }
      },
      {
        "@type": "Question",
        "name": "What is Normalized Fat-Free Mass Index (FFMI) and what does a score of 25 mean?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Normalized FFMI adjusts raw fat-free mass index [FFM (kg) / Height (m)²] to a standardized reference height of 1.80 meters (approx. 5'11\"). In landmark research by Dr. Harrison Pope examining pre-steroid era bodybuilders and natural athletes, a normalized FFMI of 25.0 was identified as the theoretical upper ceiling of natural human muscular development without anabolic-androgenic steroid use."
        }
      },
      {
        "@type": "Question",
        "name": "Why is Lean Body Mass critical for clinical anesthetic and antibiotic dosing?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Hydrophilic medications—including polar aminoglycoside antibiotics, neuromuscular blocking agents (rocuronium, vecuronium), and intravenous induction anesthetics (propofol)—distribute almost exclusively into extracellular fluid and lean vascular tissues, with negligible uptake into adipose tissue. Dosing strictly by total body weight causes severe toxicity in obese patients, making LBM the required dosing denominator."
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
        <div class="badge-tag">Body Composition &amp; Kinanthropometry</div>
        <h1 class="calculator-title">Lean Body Mass &amp; FFMI Calculator</h1>
        <p class="calculator-description">Calculate your Lean Body Mass (LBM) using the validated Boer, James, and Hume clinical formulas, and determine your height-normalized Fat-Free Mass Index (FFMI).</p>
      </div>

      <div class="calculator-grid">
        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Anthropometric Inputs</h2>
          </div>
          <div class="calc-card-body">
            <div class="form-row" style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
              <div class="form-group">
                <label for="lbm-gender" class="form-label">Biological Sex</label>
                <select id="lbm-gender" class="form-select" onchange="calculateLBM()">
                  <option value="male" selected>Male</option>
                  <option value="female">Female</option>
                </select>
              </div>
              <div class="form-group">
                <label for="lbm-unit" class="form-label">Unit System</label>
                <select id="lbm-unit" class="form-select" onchange="toggleLBMUnits()">
                  <option value="metric" selected>Metric (cm, kg)</option>
                  <option value="us">US Customary (in, lbs)</option>
                </select>
              </div>
            </div>

            <div class="form-row" style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
              <div class="form-group">
                <label for="lbm-height" class="form-label" id="label-lbm-height">Height (cm)</label>
                <input type="number" id="lbm-height" class="form-input" value="178" min="50" max="250" step="0.5" oninput="calculateLBM()">
              </div>
              <div class="form-group">
                <label for="lbm-weight" class="form-label" id="label-lbm-weight">Weight (kg)</label>
                <input type="number" id="lbm-weight" class="form-input" value="80" min="20" max="350" step="0.5" oninput="calculateLBM()">
              </div>
            </div>

            <div class="form-group">
              <label for="lbm-bf" class="form-label">Known Body Fat Percentage (% - Optional for FFMI)</label>
              <input type="number" id="lbm-bf" class="form-input" value="15.0" min="3" max="65" step="0.5" oninput="calculateLBM()">
              <span class="form-hint">From DEXA, hydrostatic weighing, or skinfold caliper</span>
            </div>

            <button type="button" class="btn btn-primary" onclick="calculateLBM()">Calculate Lean Mass &amp; FFMI</button>
          </div>
        </div>

        <div class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title">Lean Mass &amp; Muscular Index Results</h2>
          </div>
          <div class="calc-card-body">
            <div class="result-hero" style="background:#f0fdf4;border-color:#bbf7d0;">
              <span class="hero-label">Primary Lean Body Mass (Boer Formula)</span>
              <div class="hero-value" id="res-lbm-boer" style="color:#15803d;font-size:2.4rem;">60.9 kg (134.3 lbs)</div>
              <span class="form-hint" id="res-lbm-pct">76.1% of Total Body Mass</span>
            </div>

            <div class="results-grid" style="margin-top:1.5rem;">
              <div class="result-item">
                <span class="result-label">James Formula (1976)</span>
                <span class="result-value" id="res-lbm-james">62.2 kg</span>
              </div>
              <div class="result-item">
                <span class="result-label">Hume Formula (1966)</span>
                <span class="result-value" id="res-lbm-hume">57.1 kg</span>
              </div>
              <div class="result-item">
                <span class="result-label">Raw FFMI</span>
                <span class="result-value" id="res-ffmi-raw">21.5 kg/m²</span>
              </div>
              <div class="result-item">
                <span class="result-label">Normalized FFMI (1.8m)</span>
                <span class="result-value" id="res-ffmi-norm">21.6 kg/m²</span>
              </div>
            </div>

            <div class="stat-box" style="margin-top:1.5rem;padding:1rem;background:#f8fafc;border-radius:8px;border:1px solid #e2e8f0;">
              <h4 style="font-weight:700;margin-bottom:0.5rem;font-size:0.95rem;">Kinanthropometric &amp; Muscular Classification:</h4>
              <p id="res-ffmi-status" style="font-size:0.875rem;color:#475569;margin:0;">
                Normalized FFMI of 21.6 places you in the "Above Average Muscularity" category. Theoretical natural drug-free ceiling is ~25.0 kg/m².
              </p>
            </div>
          </div>
        </div>
      </div>

      <article class="article-body">
        <h2>The Multi-Compartment Model of Human Body Composition</h2>
        <p>
          In human anatomy and sports medicine, total body mass is traditionally divided using the classic <strong>Two-Compartment (2C) Model</strong> proposed by Behnke and Siri:
        </p>
        $$\text{Total Body Weight (TBW)} = \text{Fat Mass (FM)} + \text{Fat-Free Mass (FFM)}$$
        <p>
          While frequently utilized synonymously, a precise histological distinction exists between <em>Fat-Free Mass (FFM)</em> and <em>Lean Body Mass (LBM)</em>:
        </p>
        <ul>
          <li><strong>Fat-Free Mass (FFM):</strong> Represents the complete absence of all lipid molecules. It comprises skeletal muscle mass, internal organ viscera (liver, heart, kidneys, spleen), bone mineral mass, and intracellular/extracellular water.</li>
          <li><strong>Lean Body Mass (LBM):</strong> Encompasses Fat-Free Mass plus <strong>essential lipids</strong>. Essential lipids reside in the phospholipids of cellular membranes, myelin sheaths of peripheral and central nervous system axolemma, and bone marrow stroma. Essential fat accounts for approximately 3% of body weight in biological men and 9% to 12% in biological women (essential for reproductive and endocrine viability).</li>
        </ul>

        <h2>Mathematical Derivations of Validated Clinical LBM Formulas</h2>
        <p>
          When direct 4-compartment DEXA, magnetic resonance imaging (MRI), or hydrostatic underwater weighing is unavailable, clinical pharmacology relies on validated anthropometric equations based on stature ($H$ in cm) and body mass ($W$ in kg):
        </p>

        <div class="formula-box">
          <p><strong>1. The Boer Formula (1984) - Modern Pharmacokinetic Standard:</strong></p>
          $$\text{Men: } LBM\text{ (kg)} = 0.407 \times W + 0.267 \times H - 19.2$$
          $$\text{Women: } LBM\text{ (kg)} = 0.252 \times W + 0.473 \times H - 48.3$$
          <p>
            Derived by Dr. P. Boer to estimate extracellular and intravascular fluid compartments, the Boer equation is favored in clinical pharmacology because it maintains stable linear scaling across severe obesity without paradoxically predicting negative or declining lean mass.
          </p>
        </div>

        <div class="formula-box">
          <p><strong>2. The James Formula (1976) - Classical Physiological Model:</strong></p>
          $$\text{Men: } LBM\text{ (kg)} = 1.1 \times W - 128 \times \left(\frac{W}{H}\right)^2$$
          $$\text{Women: } LBM\text{ (kg)} = 1.07 \times W - 148 \times \left(\frac{W}{H}\right)^2$$
          <p>
            While accurate in normal-weight individuals, the quadratic ratio $(W/H)^2$ causes the James formula to curve downward in severe morbid obesity ($BMI > 42\text{ kg/m}^2$), occasionally yielding erroneous, physiologically impossible drop-offs in lean mass.
          </p>
        </div>

        <div class="formula-box">
          <p><strong>3. The Hume Formula (1966) - Hospitalized Patient Baseline:</strong></p>
          $$\text{Men: } LBM\text{ (kg)} = 0.32810 \times W + 0.33929 \times H - 29.5336$$
          $$\text{Women: } LBM\text{ (kg)} = 0.29569 \times W + 0.41813 \times H - 43.2933$$
        </div>

        <h2>Fat-Free Mass Index (FFMI) and the Natural Muscular Ceiling</h2>
        <p>
          Body Mass Index ($BMI = kg/m^2$) is notoriously incapable of distinguishing between dense skeletal muscle and adiposity. An elite natural bodybuilder standing 5 ft 10 in and weighing 210 lbs at 8% body fat has a BMI of 30.1, misclassifying him as clinically "obese."
        </p>
        <p>
          In 1995, Dr. Harrison Pope and colleagues at Harvard Medical School developed the <strong>Fat-Free Mass Index (FFMI)</strong> to quantify muscularity normalized to height:
        </p>
        $$\text{Fat-Free Mass (FFM in kg)} = \text{Total Weight (kg)} \times \left(1 - \frac{\text{Body Fat \%}}{100}\right)$$
        $$\text{Raw FFMI} = \frac{\text{FFM (kg)}}{\text{Height (m)}^2}$$
        <p>
          Because taller individuals naturally carry slightly more absolute muscular mass per unit of height squared due to broad bone frame geometry, Dr. Pope formulated the <strong>Height-Normalized FFMI</strong> adjusted to a standardized stature of 1.80 meters (approx. 5'11"):
        </p>
        $$\text{Normalized FFMI} = \text{Raw FFMI} + 6.3 \times (1.80\text{ m} - \text{Height in meters})$$

        <h2>The Natural Genetic Limit: The Landmark Pope Study Findings</h2>
        <p>
          In Pope's seminal study evaluating 157 male athletes—including 83 anabolic steroid users and 74 non-users, alongside 20 historical Mr. America champions from the pre-steroid era (1939 to 1959, prior to the synthetic commercialization of Dianabol and testosterone esters):
        </p>
        <ul>
          <li>Non-steroid-using athletes achieved a mean normalized FFMI of <strong>21.8 ± 1.8</strong>. Not a single natural subject surpassed a normalized FFMI of 25.0.</li>
          <li>Pre-steroid era champions (including John Grimek and Steve Reeves) averaged a normalized FFMI of <strong>25.4</strong>, with a hard upper bound around 27.3 achieved by rare genetic outliers.</li>
          <li>In contrast, anabolic-androgenic steroid users regularly exceeded <strong>27.0 to 32.0+ kg/m²</strong>.</li>
        </ul>

        <h2>Comprehensive FFMI Classification Matrix</h2>
        <p>
          The table below demonstrates normalized FFMI tiers for adult males and equivalent clinical thresholds for females:
        </p>

        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>Male Normalized FFMI</th>
                <th>Female Normalized FFMI</th>
                <th>Muscularity Classification</th>
                <th>Visual &amp; Athletic Characteristic</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>&lt; 18.0</strong></td>
                <td>&lt; 14.5</td>
                <td>Slightly Below Average</td>
                <td>Sedentary or slender build; minimal structured resistance training.</td>
              </tr>
              <tr>
                <td><strong>18.0 – 19.9</strong></td>
                <td>14.5 – 16.5</td>
                <td>Average Population Baseline</td>
                <td>Typical non-athletic adult male; normal muscle-to-fat ratio.</td>
              </tr>
              <tr>
                <td><strong>20.0 – 21.9</strong></td>
                <td>16.6 – 18.5</td>
                <td>Above Average Muscularity</td>
                <td>Recreational gym-goer; visible athletic muscular definition.</td>
              </tr>
              <tr>
                <td><strong>22.0 – 23.5</strong></td>
                <td>18.6 – 20.0</td>
                <td>Excellent / Highly Muscular</td>
                <td>Dedicated natural strength athlete (3-5+ years progressive training).</td>
              </tr>
              <tr>
                <td><strong>23.6 – 25.0</strong></td>
                <td>20.1 – 21.5</td>
                <td>Near Natural Genetic Limit</td>
                <td>Elite natural bodybuilder/powerlifter; maximal muscle thickness.</td>
              </tr>
              <tr>
                <td><strong>&gt; 25.0</strong></td>
                <td>&gt; 21.5</td>
                <td>Super-Physiological / Outlier</td>
                <td>Rare genetic elite or likely pharmaceutical androgen assistance.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2>Worked Kinanthropometric Case Study</h2>
        <div class="worked-example-card">
          <div class="example-header">
            <span class="example-badge">Sports Kinanthropometry Case</span>
            <h3 class="example-title">Physique Athlete Muscular Potential Assessment</h3>
          </div>
          <div class="example-step">
            <div class="step-num">1</div>
            <div class="step-content">
              <strong>Athlete Profile:</strong> A 25-year-old male natural physique competitor standing 6 ft 1 in (185.42 cm = 1.854 m) weighs 205 lbs (92.99 kg). DEXA body composition scan confirms exactly <strong>11.5% body fat</strong>. The sports scientist calculates his Boer LBM, James LBM, and Height-Normalized FFMI.
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">2</div>
            <div class="step-content">
              <strong>Calculate DEXA Fat-Free Mass (FFM):</strong>
              $$\text{FFM} = 92.99\text{ kg} \times (1 - 0.115) = 92.99 \times 0.885 = \mathbf{82.30\text{ kg of lean mass}}$$
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">3</div>
            <div class="step-content">
              <strong>Calculate Raw and Normalized FFMI:</strong>
              $$\text{Raw FFMI} = \frac{82.30}{(1.854)^2} = \frac{82.30}{3.4373} = \mathbf{23.94\text{ kg/m}^2}$$
              $$\text{Normalized FFMI} = 23.94 + 6.3 \times (1.80 - 1.854) = 23.94 + 6.3 \times (-0.054) = 23.94 - 0.34 = \mathbf{23.60\text{ kg/m}^2}$$
            </div>
          </div>
          <div class="example-step">
            <div class="step-num">4</div>
            <div class="step-content">
              <strong>Calculate Boer and James Formula Concordance:</strong>
              $$\text{Boer LBM} = 0.407 \times 92.99 + 0.267 \times 185.42 - 19.2 = 37.85 + 49.51 - 19.2 = \mathbf{68.16\text{ kg}}$$
              <strong>Insight:</strong> The general population Boer formula underpredicts his lean mass (68.2 kg vs true 82.3 kg) by 14 kg because empirical population formulas assume average body fat (~20-25%), whereas DEXA-derived FFMI accurately captures his advanced muscular hypertrophy. His Normalized FFMI of 23.6 confirms he is approaching his natural genetic muscular ceiling.
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
    function toggleLBMUnits() {
      const unit = document.getElementById('lbm-unit').value;
      const hLabel = document.getElementById('label-lbm-height');
      const wLabel = document.getElementById('label-lbm-weight');
      const hInput = document.getElementById('lbm-height');
      const wInput = document.getElementById('lbm-weight');

      if (unit === 'metric') {
        hLabel.innerText = 'Height (cm)';
        hInput.value = '178';
        hInput.min = '50';
        hInput.max = '250';
        hInput.step = '0.5';

        wLabel.innerText = 'Weight (kg)';
        wInput.value = '80';
        wInput.min = '20';
        wInput.max = '350';
        wInput.step = '0.5';
      } else {
        hLabel.innerText = 'Height (inches)';
        hInput.value = '70';
        hInput.min = '20';
        hInput.max = '98';
        hInput.step = '0.5';

        wLabel.innerText = 'Weight (lbs)';
        wInput.value = '176';
        wInput.min = '45';
        wInput.max = '770';
        wInput.step = '1';
      }
      calculateLBM();
    }

    function calculateLBM() {
      const gender = document.getElementById('lbm-gender').value;
      const unit = document.getElementById('lbm-unit').value;
      let h = parseFloat(document.getElementById('lbm-height').value) || 0;
      let w = parseFloat(document.getElementById('lbm-weight').value) || 0;
      const bf = parseFloat(document.getElementById('lbm-bf').value) || 0;

      if (h <= 0 || w <= 0) return;

      const h_cm = (unit === 'metric') ? h : h * 2.54;
      const w_kg = (unit === 'metric') ? w : w * 0.45359237;

      // 1. Boer (1984)
      let lbm_boer = 0;
      if (gender === 'male') {
        lbm_boer = 0.407 * w_kg + 0.267 * h_cm - 19.2;
      } else {
        lbm_boer = 0.252 * w_kg + 0.473 * h_cm - 48.3;
      }

      // 2. James (1976)
      let lbm_james = 0;
      const ratio = w_kg / h_cm;
      if (gender === 'male') {
        lbm_james = 1.1 * w_kg - 128 * Math.pow(ratio, 2);
      } else {
        lbm_james = 1.07 * w_kg - 148 * Math.pow(ratio, 2);
      }

      // 3. Hume (1966)
      let lbm_hume = 0;
      if (gender === 'male') {
        lbm_hume = 0.32810 * w_kg + 0.33929 * h_cm - 29.5336;
      } else {
        lbm_hume = 0.29569 * w_kg + 0.41813 * h_cm - 43.2933;
      }

      // FFMI Calculation
      let ffm_kg = w_kg * (1 - (bf / 100));
      if (bf <= 0) ffm_kg = lbm_boer;

      const h_m = h_cm / 100;
      const raw_ffmi = ffm_kg / (h_m * h_m);
      const norm_ffmi = raw_ffmi + 6.3 * (1.80 - h_m);

      const lbm_boer_lbs = lbm_boer * 2.20462;
      const lbm_pct = (lbm_boer / w_kg * 100).toFixed(1);

      document.getElementById('res-lbm-boer').innerText = `${lbm_boer.toFixed(1)} kg (${lbm_boer_lbs.toFixed(1)} lbs)`;
      document.getElementById('res-lbm-pct').innerText = `${lbm_pct}% of Total Body Mass`;
      document.getElementById('res-lbm-james').innerText = `${lbm_james.toFixed(1)} kg`;
      document.getElementById('res-lbm-hume').innerText = `${lbm_hume.toFixed(1)} kg`;
      document.getElementById('res-ffmi-raw').innerText = `${raw_ffmi.toFixed(1)} kg/m²`;
      document.getElementById('res-ffmi-norm').innerText = `${norm_ffmi.toFixed(1)} kg/m²`;

      const statusEl = document.getElementById('res-ffmi-status');
      if (norm_ffmi < 18.0) {
        statusEl.innerText = `Normalized FFMI of ${norm_ffmi.toFixed(1)}: Below average muscularity. Progressive overload resistance training and adequate dietary protein (1.6 g/kg) will yield rapid muscular development.`;
      } else if (norm_ffmi <= 20.0) {
        statusEl.innerText = `Normalized FFMI of ${norm_ffmi.toFixed(1)}: Average adult muscularity baseline. Healthy physical conditioning with room for hypertrophy.`;
      } else if (norm_ffmi <= 22.0) {
        statusEl.innerText = `Normalized FFMI of ${norm_ffmi.toFixed(1)}: Above average muscularity. Characteristic of consistent recreational weightlifting.`;
      } else if (norm_ffmi <= 23.5) {
        statusEl.innerText = `Normalized FFMI of ${norm_ffmi.toFixed(1)}: Excellent muscular development. Reflects 3-5+ years of dedicated natural hypertrophy training.`;
      } else if (norm_ffmi <= 25.0) {
        statusEl.innerText = `Normalized FFMI of ${norm_ffmi.toFixed(1)}: Near natural genetic ceiling. Highly elite physique development.`;
      } else {
        statusEl.innerText = `Normalized FFMI of ${norm_ffmi.toFixed(1)}: Exceptional muscularity exceeding 25.0. Exceeds historical natural limits documented by Dr. Harrison Pope.`;
      }
    }

    document.addEventListener('DOMContentLoaded', calculateLBM);
  </script>
</body>
</html>
"""

def generate_part2():
    with open(os.path.join(BASE_DIR, "heart-rate-zone-calculator.html"), "w", encoding="utf-8") as f:
        f.write(HR_ZONE_HTML)
    print("Generated heart-rate-zone-calculator.html")

    with open(os.path.join(BASE_DIR, "lean-body-mass-calculator.html"), "w", encoding="utf-8") as f:
        f.write(LBM_HTML)
    print("Generated lean-body-mass-calculator.html")

if __name__ == "__main__":
    generate_part2()
