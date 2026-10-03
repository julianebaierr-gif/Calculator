"""
Batch 22 - Part 4: Health & Fitness Tools
7. ovulation-calculator.html (Ogino-Knaus Rhythm Method, Luteal Phase, BBT, LH Surge & Fertile Window)
8. pregnancy-weight-gain-calculator.html (IOM & ACOG 2009 Gestational Weight Gain Curves, Pre-pregnancy BMI & Twin Trajectories)
Word count target: >1,050 words in article-body each.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 7. ovulation-calculator.html
# -------------------------------------------------------------
OVULATION_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ovulation Calculator | Fertile Window & Menstrual Cycle Predictor</title>
  <meta name="description" content="Calculate your estimated ovulation date, peak fertile window, implantation timeframe, and expected period using clinical rhythm and luteal phase algorithms.">
  <link rel="canonical" href="https://calchub.com/ovulation-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Clinical Ovulation and Fertile Window Calculator",
    "applicationCategory": "HealthApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0.00",
      "priceCurrency": "USD"
    },
    "description": "Calculates prospective ovulation day, six-day fertile window, peak conception dates, and implantation timeline based on menstrual cycle dynamics and luteal phase length."
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "How is the ovulation date calculated from the menstrual cycle?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Ovulation timing is governed by the length of the luteal phase, which remains remarkably stable at approximately 14 days (ranging clinically between 11 and 16 days) across most healthy individuals. In a cycle of length CL, estimated ovulation day occurs at Od = CL - Lp, where Lp is the luteal phase length. For a typical 28-day cycle with a 14-day luteal phase, ovulation occurs on cycle day 14. For a 32-day cycle, ovulation occurs around cycle day 18."
        }
      },
      {
        "@type": "Question",
        "name": "What is the fertile window and how many days does it last?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The biological fertile window spans exactly six consecutive days: the five days preceding ovulation plus the day of ovulation itself. This timeframe is dictated by physiological gamete survival: healthy human spermatozoa can survive in fertile cervical mucus for up to 120 hours (5 days), while an ovulated secondary oocyte remains viable for fertilization for only 12 to 24 hours post-follicular rupture."
        }
      },
      {
        "@type": "Question",
        "name": "Which days offer the highest probability of conception?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Extensive epidemiological studies by Wilcox et al. demonstrate that conception probability peaks two days prior to ovulation (Od - 2) and the day immediately preceding ovulation (Od - 1), yielding conception rates of approximately 25% to 30% per cycle. Having intercourse on the day of ovulation yields a conception probability of roughly 10% to 15%, while intercourse after ovulation has closed drops the probability near zero."
        }
      },
      {
        "@type": "Question",
        "name": "How do basal body temperature (BBT) and LH test strips confirm ovulation?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Urinary luteinizing hormone (LH) test strips detect the mid-cycle LH surge (typically exceeding 25 to 40 mIU/mL), which triggers oocyte release 24 to 36 hours later, functioning as a prospective predictor. Conversely, basal body temperature (BBT) shifts upward by 0.4°F to 1.0°F (0.2°C to 0.5°C) 24 to 48 hours after ovulation due to the thermogenic effect of progesterone secreted by the corpus luteum, serving as retrospective confirmation."
        }
      },
      {
        "@type": "Question",
        "name": "What happens if menstrual cycles are irregular?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "For irregular cycles, calendar algorithms use the shortest and longest recorded cycles over the prior 6 to 12 months. The first fertile day is estimated as shortest cycle minus 18 days, while the last fertile day is longest cycle minus 11 days. However, because cycle irregularity is frequently driven by variable follicular phase recruitment or conditions like PCOS, tracking cervical mucus and urinary LH surges provides substantially greater predictive reliability."
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
        <li class="active">Ovulation Calculator</li>
      </ol>
    </nav>

    <div class="page-layout">
      <div class="calculator-container">
        <div class="calculator-card">
          <h1 class="calculator-title">Clinical Ovulation & Fertile Window Calculator</h1>
          <p class="calculator-subtitle">Predict estimated ovulation day, peak conception dates, blastocyst implantation window, and next menstrual cycle onset based on endocrinological cycle parameters.</p>

          <form id="ovulation-form" class="calculator-form">
            <div class="form-group">
              <label for="lmp-date" class="form-label">First Day of Last Menstrual Period (LMP)</label>
              <input type="date" id="lmp-date" class="form-input" required>
            </div>

            <div class="form-group">
              <label for="cycle-length" class="form-label">Average Menstrual Cycle Length (Days)</label>
              <div class="slider-container">
                <input type="range" id="cycle-length" min="21" max="45" value="28" class="form-slider">
                <span id="cycle-length-val" class="slider-display">28 days</span>
              </div>
              <small class="form-hint">Normal adult cycle duration ranges from 21 to 35 days (average 28 days).</small>
            </div>

            <div class="form-group">
              <label for="luteal-length" class="form-label">Luteal Phase Duration (Days)</label>
              <div class="slider-container">
                <input type="range" id="luteal-length" min="10" max="16" value="14" class="form-slider">
                <span id="luteal-length-val" class="slider-display">14 days (Default)</span>
              </div>
              <small class="form-hint">The post-ovulatory luteal phase is typically 14 days (clinically normal: 11–16 days).</small>
            </div>

            <button type="submit" class="calculate-btn">Calculate Fertile Window & Timeline</button>
          </form>

          <div id="calculator-results" class="results-container" style="display: none;">
            <h2 class="results-heading">Fertility Profile & Cycle Milestones</h2>
            
            <div class="results-grid">
              <div class="result-card primary-result">
                <span class="result-label">Estimated Ovulation Date</span>
                <span id="res-ovulation-date" class="result-value">--</span>
                <span id="res-cycle-day" class="result-subtext">Cycle Day --</span>
              </div>

              <div class="result-card highlight-card">
                <span class="result-label">Peak Conception Window</span>
                <span id="res-peak-window" class="result-value">--</span>
                <span class="result-subtext">Highest pregnancy probability (Days -2 to 0)</span>
              </div>

              <div class="result-card">
                <span class="result-label">Full Fertile Window (6 Days)</span>
                <span id="res-fertile-window" class="result-value">--</span>
                <span class="result-subtext">5 days prior to ovulation + Ovulation day</span>
              </div>

              <div class="result-card">
                <span class="result-label">Implantation Window</span>
                <span id="res-implantation-window" class="result-value">--</span>
                <span class="result-subtext">Days 6 to 12 post-ovulation</span>
              </div>

              <div class="result-card">
                <span class="result-label">Earliest Reliable Home Pregnancy Test</span>
                <span id="res-test-date" class="result-value">--</span>
                <span class="result-subtext">Sensitive urinary hCG test (≥25 mIU/mL)</span>
              </div>

              <div class="result-card">
                <span class="result-label">Next Expected Menstrual Period</span>
                <span id="res-next-period" class="result-value">--</span>
                <span class="result-subtext">Onset of next follicular cycle</span>
              </div>
            </div>

            <div class="summary-box mt-4">
              <h3 class="summary-title">Conception Projection</h3>
              <p id="res-edd-summary" class="summary-text">If fertilization occurs during this cycle's fertile window, your estimated gestational age will reach 40 completed weeks on approximately <strong id="res-edd-date">--</strong>.</p>
            </div>
          </div>
        </div>
      </div>

      <aside class="sidebar">
        <div class="sidebar-card">
          <h3 class="sidebar-title">Women's Health & Fertility</h3>
          <ul class="sidebar-list">
            <li><a href="due-date-calculator.html">Pregnancy Due Date Calculator</a></li>
            <li><a href="pregnancy-weight-gain-calculator.html">Pregnancy Weight Gain Calculator</a></li>
            <li><a href="calorie-deficit-calculator.html">Calorie Deficit Calculator</a></li>
            <li><a href="bsa-calculator.html">Body Surface Area (BSA) Calculator</a></li>
            <li><a href="bac-calculator.html">Blood Alcohol Concentration (BAC)</a></li>
          </ul>
        </div>
        <div class="sidebar-card mt-4">
          <h3 class="sidebar-title">Clinical References</h3>
          <p class="sidebar-text">Grounded in clinical guidelines from the American College of Obstetricians and Gynecologists (ACOG), the American Society for Reproductive Medicine (ASRM), and epidemiological research by Wilcox et al. on human fertile window dynamics.</p>
        </div>
      </aside>
    </div>

    <article class="article-body">
      <h2>The Physiology of Human Ovulation and the Menstrual Cycle</h2>
      <p>Human reproduction depends on the precisely orchestrated neuroendocrine signaling cascade of the <strong>Hypothalamic-Pituitary-Ovarian (HPO) axis</strong>. Each menstrual cycle represents an integrated sequence of ovarian follicular maturation, episodic steroidogenesis, endometrial differentiation, and, in the absence of conception, programmed tissue breakdown and menstruation. Clinically, a normal menstrual cycle in healthy reproductive-age women ranges between 21 and 35 days, with an average duration of 28 days. While popular intuition frequently assumes that ovulation occurs precisely on day 14 of every woman's cycle, clinical endocrinology demonstrates that cycle variability is predominantly driven by fluctuations in the pre-ovulatory <em>follicular phase</em>, whereas the post-ovulatory <em>luteal phase</em> maintains relative temporal stability.</p>

      <p>The menstrual cycle is chronologically divided into two principal ovarian phases separated by ovulation:</p>
      <ul>
        <li><strong>Follicular Phase:</strong> Commencing with the first day of menses (Cycle Day 1), pulsatile secretion of Gonadotropin-Releasing Hormone (GnRH) from the arcuate nucleus of the hypothalamus stimulates the anterior pituitary gland to synthesize and secrete Follicle-Stimulating Hormone (FSH) and Luteinizing Hormone (LH). Circulating FSH recruits an initial cohort of antral follicles within the ovaries. As FSH levels begin to decline mid-follicular phase, the follicle exhibiting the highest density of granulosa cell FSH receptors and aromatase activity emerges as the <em>dominant Graafian follicle</em>, while subordinate cohort follicles undergo apoptotic atresia. Granulosa cells within the dominant follicle progressively secrete rising quantities of 17&beta;-estradiol ($E_2$), which induces rapid proliferation of the endometrial functionalis layer.</li>
        <li><strong>Ovulatory Phase:</strong> When circulating estradiol levels exceed an empirical threshold of approximately 200 pg/mL for at least 36 to 48 consecutive hours, estrogen exerts a positive feedback switch on the hypothalamus and anterior pituitary. This trigger unleashes a massive, synchronized surge of LH and FSH. The surge activates proteolytic enzymes (including collagenases and plasminogen activator) and prostaglandin synthesis within the follicular wall, inducing thinning and ultimate rupture of the follicular stigma. The secondary oocyte, arrested in metaphase of meiosis II and enveloped by the corona radiata and cumulus oophorus, is extruded into the peritoneal cavity and captured by the fimbriae of the fallopian tube (oviduct). Follicular rupture occurs approximately 24 to 36 hours following the initiation of the LH surge, and 10 to 12 hours after peak LH serum concentrations.</li>
        <li><strong>Luteal Phase:</strong> Following extrusion of the oocyte, the remnants of the collapsed follicle undergo profound vascularization and cellular transformation, luteinizing into the <em>corpus luteum</em>. Under tonic LH stimulation, the corpus luteum secretes substantial concentrations of progesterone and estradiol. Progesterone arrests endometrial epithelial proliferation and induces dense stromal edema, glycogen-rich glandular secretion, and spiral artery coiling, preparing the endometrial stroma for blastocyst implantation. In the absence of embryonic human chorionic gonadotropin (hCG) signaling, the corpus luteum undergoes functional and structural luteolysis around day 12 to 14 post-ovulation, precipitating progesterone withdrawal, vasoconstriction of spiral arteries, endometrial ischemia, and menstrual sloughing.</li>
      </ul>

      <h2>Mathematical Modeling of the Fertile Window & Ovulation Timing</h2>
      <p>The estimation of prospective ovulation timing rests on the biological invariance of the luteal phase duration ($L_p$). While the follicular phase can range widely from 7 to over 25 days depending on individual metabolic, psychological, and physiological variables, the lifespan of the corpus luteum is biologically constrained by programmed luteolytic pathways. Across clinical cohorts, the healthy human luteal phase averages 14 days, with a normal physiological spectrum spanning 11 to 16 days. For any menstrual cycle of known duration $C_L$ and luteal duration $L_p$, the estimated ovulation day ($O_d$) relative to the onset of the Last Menstrual Period (LMP) is expressed as:</p>

      $$O_d = C_L - L_p$$

      <p>In standard 28-day cycles with a normative 14-day luteal phase, ovulation occurs on day $28 - 14 = 14$. In a 34-day cycle, follicular recruitment requires a prolonged timeframe, placing ovulation at day $34 - 14 = 20$. Conversely, in a 24-day cycle, ovulation occurs around cycle day $24 - 14 = 10$.</p>

      <h3>The Biological Six-Day Fertile Window</h3>
      <p>Conception requires the concurrent presence of viable spermatozoa and a fertile oocyte within the ampullary portion of the fallopian tube. The temporal boundaries of the <strong>fertile window</strong> are strictly determined by the maximum functional survival spans of human male and female gametes within the female reproductive tract:</p>
      <ul>
        <li><strong>Spermatozoon Viability:</strong> In the presence of estrogen-primed, hydrated cervical mucus containing linear glycoprotein micellar channels, ejaculated human spermatozoa can maintain progressive motility, survive capacitation, and retain fertilizing capability for up to <strong>120 hours (5 days)</strong> within the crypts of the uterine cervix and fallopian tubes.</li>
        <li><strong>Oocyte Viability:</strong> Following follicular extrusion, the unfertilized secondary oocyte exhibits a highly restricted viability window. Structural deterioration of the zona pellucida and metabolic decline limit fertilizability to <strong>12 to 24 hours</strong> post-ovulation.</li>
      </ul>

      <p>Consequently, the biologically active fertile window spans exactly six consecutive days: the five days preceding ovulation plus the day of ovulation itself:</p>

      $$\text{Fertile Window} = [O_d - 5, O_d]$$

      <h3>Epidemiological Probability of Daily Conception</h3>
      <p>Seminal prospective cohort studies conducted by Dr. Allen Wilcox and colleagues (National Institute of Environmental Health Sciences, published in the <em>New England Journal of Medicine</em>) tracked daily urinary hormone metabolites and timed intercourse across hundreds of menstrual cycles. Their findings established that daily conception probabilities are not uniform across the fertile window. Intercourse occurring two days prior to ovulation or one day prior to ovulation yields the highest likelihood of successful fertilization and clinical pregnancy:</p>

      $$P(\text{Conception} \mid \text{Intercourse on Day } t) = \begin{cases} 0.04 & t = O_d - 5 \\ 0.08 & t = O_d - 4 \\ 0.15 & t = O_d - 3 \\ 0.27 & t = O_d - 2 \\ 0.31 & t = O_d - 1 \\ 0.12 & t = O_d \\ < 0.01 & t \ge O_d + 1 \end{cases}$$

      <p>This mathematical distribution demonstrates that sexual intercourse occurring 24 to 48 hours prior to ovulation maximizes reproductive efficacy because an ample pool of capacitated spermatozoa is already sequestered within the tubal ampulla at the precise instant the oocyte arrives from the infundibulum.</p>

      <div class="table-container my-4">
        <table class="data-table">
          <thead>
            <tr>
              <th>Menstrual Cycle Phase</th>
              <th>Typical Cycle Days (28-Day Cycle)</th>
              <th>Dominant Sex Hormone</th>
              <th>Endometrial State</th>
              <th>Cervical Mucus Quality</th>
              <th>Conception Probability</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Early Follicular (Menses)</strong></td>
              <td>Days 1 – 5</td>
              <td>Low Estrogen & Low Progesterone</td>
              <td>Desquamation / Menstrual sloughing</td>
              <td>Scant, thick, cellular, acidic</td>
              <td>Extremely Low (&lt;1%)</td>
            </tr>
            <tr>
              <td><strong>Mid Follicular</strong></td>
              <td>Days 6 – 9</td>
              <td>Rising 17&beta;-Estradiol ($E_2$)</td>
              <td>Proliferative (re-epithelialization)</td>
              <td>Tacky, sticky, whitish, opaque</td>
              <td>Low (1% – 5%)</td>
            </tr>
            <tr>
              <td><strong>Late Follicular (Fertile Window)</strong></td>
              <td>Days 10 – 13</td>
              <td>Peak Estradiol (&gt;200 pg/mL)</td>
              <td>Late Proliferative (thickened trilaminar)</td>
              <td>Watery, clear, stretchy egg-white ($&ge;8$ cm spinnbarkeit)</td>
              <td><strong>Peak (15% – 31%)</strong></td>
            </tr>
            <tr>
              <td><strong>Ovulation</strong></td>
              <td>Day 14</td>
              <td>LH Surge & Secondary FSH Peak</td>
              <td>Periovulatory / Transition to Secretory</td>
              <td>Abundant, slippery, alkaline ($pH \approx 7.5$)</td>
              <td>High (10% – 15%)</td>
            </tr>
            <tr>
              <td><strong>Early to Mid Luteal</strong></td>
              <td>Days 15 – 22</td>
              <td>High Progesterone & Moderate $E_2$</td>
              <td>Secretory (glycogen-rich vacuoles)</td>
              <td>Rapid thickening, cellular, tacky, hostile plug</td>
              <td>Zero (&lt;0.1%)</td>
            </tr>
            <tr>
              <td><strong>Late Luteal (Premenstrual)</strong></td>
              <td>Days 23 – 28</td>
              <td>Falling Progesterone & $E_2$</td>
              <td>Ischemic / Spiral artery constriction</td>
              <td>Dry, scant, impenetrable to sperm</td>
              <td>Zero (Inconceivable)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Primary Biological Markers and Ovulation Detection Modalities</h2>
      <p>While calendar algorithms provide an indispensable predictive baseline, multi-modal biological tracking substantially increases the accuracy of pinpointing ovulation in clinical practice. The primary validated biological markers include:</p>

      <h3>1. Urinary Luteinizing Hormone (LH) Immunochromatography</h3>
      <p>Home ovulation predictor kits (OPKs) utilize qualitative or semi-quantitative lateral flow immunoassay strips that detect urinary LH excretion. Under baseline follicular conditions, tonic LH levels range from 2 to 10 mIU/mL. The mid-cycle surge triggers a precipitous rise to 25 to 100 mIU/mL. A positive OPK test indicates that circulating LH has crossed the analytical threshold, signifying that follicular rupture will typically ensue within <strong>24 to 36 hours</strong> (and within 10 to 16 hours of the LH peak). In women with polycystic ovary syndrome (PCOS), chronically elevated baseline LH levels can generate false-positive results, necessitating specialized quantitative tracking or ultrasound correlation.</p>

      <h3>2. Cervical Mucus Analysis (Billings & Creighton Models)</h3>
      <p>Under the influence of rising mid-follicular estradiol, the cervical crypts synthesize Type E (estrogenic) mucus, which is thin, alkaline, highly hydrated (98% water), and rich in mucin macromolecules organized into parallel linear chains. This fertile mucus exhibits significant <em>spinnbarkeit</em> (elastic stretching to 8–12 cm without tearing) and displays microscopic "ferning" (crystallization into arborizing sodium chloride and potassium chloride dendrites upon drying). Cervical mucus provides a functional biological conduit that neutralizes vaginal acidity, nourishes sperm, and filters morphologically abnormal spermatozoa.</p>

      <h3>3. Basal Body Temperature (BBT) Biphasic Shift</h3>
      <p>Basal body temperature tracking requires taking oral, vaginal, or axillary temperature immediately upon awakening after at least four hours of uninterrupted sleep, prior to any physical exertion. Progesterone produced by the newly formed corpus luteum acts directly on the thermoregulatory preoptic nucleus of the anterior hypothalamus, elevating systemic basal body temperature by $0.4^\circ\text{F}\text{ to }1.0^\circ\text{F}$ ($0.2^\circ\text{C}\text{ to }0.5^\circ\text{C}$). The <em>Coverline rule</em> requires three consecutive daily temperatures that are at least $0.2^\circ\text{F}$ higher than the preceding six consecutive baseline follicular days. Crucially, BBT elevation confirms that ovulation has already occurred 24 to 48 hours prior; it is a retrospective confirmatory tool rather than a prospective planning tool.</p>

      <h3>4. Transvaginal Ultrasound (Folliculometry)</h3>
      <p>Serial transvaginal ultrasonography represents the gold-standard diagnostic reference in reproductive medicine. Serial imaging documents follicular enlargement at a rate of 1.5 to 2.0 mm per day until the dominant Graafian follicle attains a pre-ovulatory mean diameter of 18 to 24 mm. Imminent ovulation is evidenced by the appearance of the <em>cumulus oophorus</em> within the follicular antrum. Successful ovulation is confirmed by the sudden disappearance or collapse of the dominant follicle, internal echoes indicating hemorrhagic filling (corpus hemorrhagicum), and the appearance of free fluid within the pouch of Douglas (rectouterine pouch).</p>

      <h2>Step-by-Step Worked Clinical Case Study</h2>
      <p>To illustrate the practical calculation of fertile windows, ovulation timing, and subsequent gestational milestones, consider the following reproductive endocrinology scenario:</p>

      <div class="worked-example-card my-4">
        <h3 class="example-title">Clinical Case Profile: Ovulation & Conception Forecasting</h3>
        <p><strong>Patient Baseline:</strong> A 31-year-old female with regular 31-day menstrual cycles and a documented 14-day luteal phase is actively timing conception. The first day of her Last Menstrual Period (LMP) was recorded on <strong>October 1</strong>.</p>
        
        <div class="example-step">
          <div class="step-num">Step 1</div>
          <div class="step-content">
            <strong>Determine Cycle Day of Ovulation ($O_d$):</strong>
            $$\text{Cycle Length } (C_L) = 31 \text{ days}, \quad \text{Luteal Phase } (L_p) = 14 \text{ days}$$
            $$O_d = C_L - L_p = 31 - 14 = \text{Cycle Day 17}$$
            Starting from LMP on October 1 (Cycle Day 1), adding 16 elapsed days places the estimated ovulation date on <strong>October 17</strong>.
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 2</div>
          <div class="step-content">
            <strong>Calculate the Six-Day Biological Fertile Window:</strong>
            $$\text{Fertile Window} = [O_d - 5, O_d] = [\text{Cycle Day 12}, \text{Cycle Day 17}]$$
            Corresponding calendar dates: <strong>October 12 through October 17</strong>. Intercourse during this six-day window allows spermatozoa to survive and intercept the ovulated secondary oocyte.
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 3</div>
          <div class="step-content">
            <strong>Pinpoint the Peak Fertility Window:</strong>
            Peak statistical conception rates occur at $O_d - 2$, $O_d - 1$, and $O_d$ (Cycle Days 15, 16, and 17).
            $$\text{Peak Probability Window} = \mathbf{\text{October 15, 16, and 17}}$$
            Coitus scheduled every 24 to 48 hours across these peak days yields cumulative per-cycle fecundity exceeding 30%.
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 4</div>
          <div class="step-content">
            <strong>Calculate Implantation Window and Pregnancy Testing Date:</strong>
            Following successful tubal fertilization, the cleaving embryo traverses the fallopian tube as a morula and enters the uterine cavity as a blastocyst. Blastocyst apposition, adhesion, and syncytiotrophoblast invasion into the endometrial decidua occur between days 6 and 12 post-ovulation (median day 8–9).
            $$\text{Implantation Window} = [O_d + 6, O_d + 12] = [\text{Cycle Day 23}, \text{Cycle Day 29}] = \mathbf{\text{October 23 to October 29}}$$
            Syncytiotrophoblast invasion secretes hCG into the maternal circulation. Serum hCG doubles every 48 hours. Detectable urinary excretion ($\ge 25\text{ mIU/mL}$) occurs reliably 13 to 14 days post-ovulation: <strong>October 30 or October 31</strong> (coinciding with the expected date of next menses).
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 5</div>
          <div class="step-content">
            <strong>Project Estimated Due Date (EDD) if Conceived:</strong>
            Because this cycle is 31 days (3 days longer than the standard 28-day model), standard Naegele's rule must be adjusted by adding the extra 3 days:
            $$\text{Adjusted EDD} = \text{LMP} + 280 \text{ days} + (C_L - 28) = \text{Oct 1} + 280 + 3 = \mathbf{\text{July 11 of the subsequent year}}$$
            Alternatively, calculating from conception day: $O_d + 266 \text{ days} = \text{Oct 17} + 266 \text{ days} = \text{July 11}$.
          </div>
        </div>
      </div>

      <h2>Clinical Factors Influencing Ovulatory Predictability</h2>
      <p>While mathematical calculators provide an exceptional structural baseline, multiple endocrinological, pharmacological, and physiological conditions can alter or suppress normal ovulatory patterns:</p>
      <ul>
        <li><strong>Polycystic Ovary Syndrome (PCOS):</strong> Characterized by hyperandrogenism, chronic ovulatory dysfunction (oligomenorrhea or amenorrhea), and polycystic ovarian morphology on ultrasound (Rotterdam criteria). Altered LH pulse frequency and relative FSH deficiency arrest follicular development at the 5–8 mm stage, producing irregular, unannounced, or absent ovulation.</li>
        <li><strong>Functional Hypothalamic Amenorrhea (FHA):</strong> Severe energy deficit, excessive endurance training, or intense psychological distress activates the hypothalamic-pituitary-adrenal (HPA) axis. Elevated corticotropin-releasing hormone (CRH) suppresses pulsatile GnRH secretion, precipitating severe hypogonadotropic hypogonadism and anovulation.</li>
        <li><strong>Hyperprolactinemia:</strong> Elevated serum prolactin (secondary to prolactinomas, dopamine antagonist medications, or untreated primary hypothyroidism) suppresses kisspeptin neuronal signaling, dampening GnRH release and inhibiting normal follicular maturation.</li>
        <li><strong>Perimenopausal Transition:</strong> Depletion of the primordial follicle pool reduces inhibin-B feedback, resulting in compensatory hyper-elevation of serum FSH. Follicular phases shorten significantly, and erratic anovulatory cycles alternate with unexpected early ovulatory events.</li>
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
            <li><a href="due-date-calculator.html">Due Date Calculator</a></li>
            <li><a href="pregnancy-weight-gain-calculator.html">Pregnancy Weight Gain</a></li>
            <li><a href="a1c-calculator.html">A1C Blood Sugar Calculator</a></li>
            <li><a href="bac-calculator.html">Blood Alcohol Concentration</a></li>
            <li><a href="heart-rate-zone-calculator.html">Heart Rate Zone Calculator</a></li>
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
        <p>&copy; 2026 CalcHub. Educational and clinical calculation tools. Medical calculations must be verified by a board-certified physician.</p>
      </div>
    </div>
  </footer>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const form = document.getElementById('ovulation-form');
      const lmpInput = document.getElementById('lmp-date');
      const cycleSlider = document.getElementById('cycle-length');
      const cycleVal = document.getElementById('cycle-length-val');
      const lutealSlider = document.getElementById('luteal-length');
      const lutealVal = document.getElementById('luteal-length-val');
      const resultsContainer = document.getElementById('calculator-results');

      // Set default LMP to 14 days ago
      const today = new Date();
      const defaultLmp = new Date(today.getTime() - (14 * 86400000));
      lmpInput.value = defaultLmp.toISOString().split('T')[0];

      cycleSlider.addEventListener('input', function() {
        cycleVal.textContent = cycleSlider.value + ' days';
      });

      lutealSlider.addEventListener('input', function() {
        lutealVal.textContent = lutealSlider.value + ' days';
      });

      function formatDate(date) {
        return date.toLocaleDateString('en-US', {
          month: 'short',
          day: 'numeric',
          year: 'numeric'
        });
      }

      function formatShortDate(date) {
        return date.toLocaleDateString('en-US', {
          month: 'short',
          day: 'numeric'
        });
      }

      form.addEventListener('submit', function(e) {
        e.preventDefault();

        const lmpVal = lmpInput.value;
        if (!lmpVal) return;

        // Parse date carefully in local time
        const parts = lmpVal.split('-');
        const lmp = new Date(parseInt(parts[0]), parseInt(parts[1]) - 1, parseInt(parts[2]));

        const cycleLength = parseInt(cycleSlider.value);
        const lutealLength = parseInt(lutealSlider.value);

        // Ovulation day = cycleLength - lutealLength
        const ovulationCycleDay = cycleLength - lutealLength;
        const ovulationDate = new Date(lmp.getTime() + (ovulationCycleDay * 86400000));

        // Fertile window: 5 days before ovulation to day of ovulation
        const fertileStart = new Date(ovulationDate.getTime() - (5 * 86400000));
        const fertileEnd = new Date(ovulationDate.getTime());

        // Peak conception window: Od - 2 to Od
        const peakStart = new Date(ovulationDate.getTime() - (2 * 86400000));
        const peakEnd = new Date(ovulationDate.getTime());

        // Implantation window: Od + 6 to Od + 12
        const impStart = new Date(ovulationDate.getTime() + (6 * 86400000));
        const impEnd = new Date(ovulationDate.getTime() + (12 * 86400000));

        // Earliest test date: Od + 12
        const testDate = new Date(ovulationDate.getTime() + (12 * 86400000));

        // Next period date: LMP + cycleLength
        const nextPeriod = new Date(lmp.getTime() + (cycleLength * 86400000));

        // EDD: Conception date + 266 days
        const eddDate = new Date(ovulationDate.getTime() + (266 * 86400000));

        // Display results
        document.getElementById('res-ovulation-date').textContent = formatDate(ovulationDate);
        document.getElementById('res-cycle-day').textContent = 'Cycle Day ' + (ovulationCycleDay + 1);
        document.getElementById('res-peak-window').textContent = formatShortDate(peakStart) + ' – ' + formatShortDate(peakEnd);
        document.getElementById('res-fertile-window').textContent = formatShortDate(fertileStart) + ' – ' + formatShortDate(fertileEnd);
        document.getElementById('res-implantation-window').textContent = formatShortDate(impStart) + ' – ' + formatShortDate(impEnd);
        document.getElementById('res-test-date').textContent = formatDate(testDate);
        document.getElementById('res-next-period').textContent = formatDate(nextPeriod);
        document.getElementById('res-edd-date').textContent = formatDate(eddDate);

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
# 8. pregnancy-weight-gain-calculator.html
# -------------------------------------------------------------
PREGNANCY_WEIGHT_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pregnancy Weight Gain Calculator | IOM & ACOG Clinical Guidelines</title>
  <meta name="description" content="Calculate recommended gestational weight gain by trimester and week based on Institute of Medicine (IOM) and ACOG 2009 guidelines for singleton and twin pregnancies.">
  <link rel="canonical" href="https://calchub.com/pregnancy-weight-gain-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Clinical Gestational Weight Gain Calculator",
    "applicationCategory": "HealthApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0.00",
      "priceCurrency": "USD"
    },
    "description": "Calculates prospective gestational weight gain targets and weekly rates based on pre-pregnancy BMI using the Institute of Medicine (IOM) and American College of Obstetricians and Gynecologists (ACOG) guidelines."
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What are the official IOM recommendations for pregnancy weight gain?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Institute of Medicine (IOM) and ACOG 2009 clinical guidelines recommend total singleton pregnancy weight gain based strictly on pre-pregnancy Body Mass Index (BMI): Underweight (BMI < 18.5) should gain 28 to 40 lbs (12.5 to 18.0 kg); Normal weight (BMI 18.5–24.9) should gain 25 to 35 lbs (11.5 to 16.0 kg); Overweight (BMI 25.0–29.9) should gain 15 to 25 lbs (7.0 to 11.5 kg); and Obese (BMI ≥ 30.0) should gain 11 to 20 lbs (5.0 to 9.0 kg)."
        }
      },
      {
        "@type": "Question",
        "name": "How much weight should be gained in the first trimester?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "During the first trimester (Weeks 1 through 13), fetal tissue mass and fluid expansion remain minimal. Total recommended maternal weight gain across the entire first trimester is only 1.1 to 4.4 lbs (0.5 to 2.0 kg), regardless of baseline BMI, although individuals experiencing severe hyperemesis gravidarum may transiently lose weight."
        }
      },
      {
        "@type": "Question",
        "name": "What are the recommended weekly weight gain rates during the second and third trimesters?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Beginning in week 14, steady maternal blood expansion, placental enlargement, and fetal growth require consistent weekly gain: Underweight women should gain ~1.0 lb/week (0.45 kg/week, range 1.0–1.3); Normal weight women should gain ~1.0 lb/week (0.45 kg/week, range 0.8–1.0); Overweight women should gain ~0.6 lb/week (0.28 kg/week, range 0.5–0.7); and Obese women should gain ~0.5 lb/week (0.22 kg/week, range 0.4–0.6)."
        }
      },
      {
        "@type": "Question",
        "name": "What are the clinical risks of excessive gestational weight gain?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Excessive gestational weight gain significantly elevates risks for Gestational Diabetes Mellitus (GDM), gestational hypertension, preeclampsia, fetal macrosomia (birthweight > 4000g), cephalopelvic disproportion, shoulder dystocia, emergency cesarean delivery, and persistent postpartum maternal weight retention leading to long-term cardiometabolic morbidity."
        }
      },
      {
        "@type": "Question",
        "name": "How does twin pregnancy affect recommended weight gain?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Twin gestations involve dual fetal growth, two placentas (or a large shared monochorionic placenta), and significantly greater maternal blood expansion. IOM guidelines recommend: Normal weight (BMI 18.5–24.9): 37 to 54 lbs (16.8 to 24.5 kg); Overweight (BMI 25.0–29.9): 31 to 50 lbs (14.1 to 22.7 kg); and Obese (BMI ≥ 30.0): 25 to 42 lbs (11.3 to 19.1 kg)."
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
        <li class="active">Pregnancy Weight Gain Calculator</li>
      </ol>
    </nav>

    <div class="page-layout">
      <div class="calculator-container">
        <div class="calculator-card">
          <h1 class="calculator-title">Clinical Pregnancy Weight Gain Calculator</h1>
          <p class="calculator-subtitle">Track your gestational weight trajectory against Institute of Medicine (IOM) and ACOG 2009 evidence-based target ranges based on pre-pregnancy BMI.</p>

          <form id="weight-gain-form" class="calculator-form">
            <div class="form-row">
              <div class="form-group col-half">
                <label for="unit-system" class="form-label">Measurement System</label>
                <select id="unit-system" class="form-select">
                  <option value="us" selected>US Customary (lbs, ft/in)</option>
                  <option value="metric">Metric (kg, cm)</option>
                </select>
              </div>
              <div class="form-group col-half">
                <label for="gestation-type" class="form-label">Pregnancy Type</label>
                <select id="gestation-type" class="form-select">
                  <option value="singleton" selected>Singleton (One Baby)</option>
                  <option value="twins">Twin Gestation</option>
                </select>
              </div>
            </div>

            <!-- US Height Inputs -->
            <div id="height-us-group" class="form-row">
              <div class="form-group col-half">
                <label for="height-feet" class="form-label">Height (Feet)</label>
                <input type="number" id="height-feet" class="form-input" min="4" max="7" value="5" required>
              </div>
              <div class="form-group col-half">
                <label for="height-inches" class="form-label">Height (Inches)</label>
                <input type="number" id="height-inches" class="form-input" min="0" max="11" value="5" required>
              </div>
            </div>

            <!-- Metric Height Input -->
            <div id="height-metric-group" class="form-group" style="display: none;">
              <label for="height-cm" class="form-label">Height (Centimeters)</label>
              <input type="number" id="height-cm" class="form-input" min="120" max="230" value="165" step="0.5">
            </div>

            <div class="form-row">
              <div class="form-group col-half">
                <label for="pre-weight" class="form-label">Pre-Pregnancy Weight (<span class="weight-unit">lbs</span>)</label>
                <input type="number" id="pre-weight" class="form-input" min="70" max="500" value="140" step="0.5" required>
              </div>
              <div class="form-group col-half">
                <label for="curr-weight" class="form-label">Current Weight (<span class="weight-unit">lbs</span>)</label>
                <input type="number" id="curr-weight" class="form-input" min="70" max="550" value="152" step="0.5" required>
              </div>
            </div>

            <div class="form-group">
              <label for="gestational-week" class="form-label">Current Gestational Week: <span id="week-display" class="font-bold text-primary">24 weeks</span></label>
              <div class="slider-container">
                <input type="range" id="gestational-week" min="2" max="42" value="24" class="form-slider">
              </div>
              <small class="form-hint">Drag slider to select completed gestational weeks (1 to 42).</small>
            </div>

            <button type="submit" class="calculate-btn">Evaluate Gestational Weight Trajectory</button>
          </form>

          <div id="calculator-results" class="results-container" style="display: none;">
            <h2 class="results-heading">Clinical Weight Trajectory Assessment</h2>

            <div class="results-grid">
              <div class="result-card primary-result">
                <span class="result-label">Pre-Pregnancy BMI</span>
                <span id="res-bmi" class="result-value">--</span>
                <span id="res-bmi-cat" class="result-subtext">Category: Normal</span>
              </div>

              <div class="result-card highlight-card">
                <span class="result-label">Recommended Week <span id="res-current-week-label">24</span> Target</span>
                <span id="res-week-target" class="result-value">--</span>
                <span id="res-trajectory-status" class="result-subtext badge-tag">On Track</span>
              </div>

              <div class="result-card">
                <span class="result-label">Total Recommended 40-Week Gain</span>
                <span id="res-total-target" class="result-value">--</span>
                <span class="result-subtext">IOM / ACOG Clinical Range</span>
              </div>

              <div class="result-card">
                <span class="result-label">Actual Current Weight Gain</span>
                <span id="res-actual-gain" class="result-value">--</span>
                <span id="res-gain-variance" class="result-subtext">--</span>
              </div>

              <div class="result-card">
                <span class="result-label">2nd & 3rd Trimester Weekly Rate</span>
                <span id="res-weekly-rate" class="result-value">--</span>
                <span class="result-subtext">Recommended rate from week 14 onward</span>
              </div>

              <div class="result-card">
                <span class="result-label">Target Full-Term Final Weight</span>
                <span id="res-final-target" class="result-value">--</span>
                <span class="result-subtext">At 40 completed weeks</span>
              </div>
            </div>

            <div class="summary-box mt-4">
              <h3 class="summary-title">Obstetric Clinical Interpretation</h3>
              <p id="res-interpretation-text" class="summary-text">Loading clinical analysis...</p>
            </div>
          </div>
        </div>
      </div>

      <aside class="sidebar">
        <div class="sidebar-card">
          <h3 class="sidebar-title">Obstetric & Maternal Health</h3>
          <ul class="sidebar-list">
            <li><a href="due-date-calculator.html">Pregnancy Due Date Calculator</a></li>
            <li><a href="ovulation-calculator.html">Ovulation & Fertile Window</a></li>
            <li><a href="calorie-deficit-calculator.html">Calorie Deficit Calculator</a></li>
            <li><a href="carbohydrate-intake-calculator.html">Carbohydrate Intake Calculator</a></li>
            <li><a href="fat-intake-calculator.html">Fat Intake Calculator</a></li>
          </ul>
        </div>
        <div class="sidebar-card mt-4">
          <h3 class="sidebar-title">Clinical Standards</h3>
          <p class="sidebar-text">Based on the Institute of Medicine (IOM) and National Research Council Committee to Reexamine IOM Pregnancy Weight Guidelines, endorsed by the American College of Obstetricians and Gynecologists (ACOG Practice Bulletin No. 230).</p>
        </div>
      </aside>
    </div>

    <article class="article-body">
      <h2>Clinical Physiology of Gestational Weight Gain (GWG)</h2>
      <p>Gestational weight gain represents a profound maternal-fetal physiological adaptation rather than simple caloric accumulation or passive tissue deposition. Over 40 completed weeks of human gestation, the maternal organism undergoes an unprecedented neuroendocrine, cardiovascular, renal, and metabolic remodeling engineered to support embryonic differentiation, placental vasculogenesis, exponential fetal growth, and future postpartum lactation. In 2009, the <strong>Institute of Medicine (IOM)</strong> and the <strong>National Research Council (NRC)</strong> published their landmark revision of gestational weight gain guidelines, formally endorsed by the <strong>American College of Obstetricians and Gynecologists (ACOG)</strong>. Unlike historical obstetric dogmas that applied a rigid single target for all pregnant individuals, modern obstetric medicine recognizes that optimal maternal-fetal outcomes depend fundamentally on pre-pregnancy Body Mass Index (BMI).</p>

      <p>Maternal weight accumulation is non-linear and exhibits two distinct physiological velocity phases:</p>
      <ul>
        <li><strong>First Trimester (Weeks 1 to 13):</strong> During early organogenesis, embryonic mass remains microscopic (attaining only ~14 grams by week 12). Weight gain during this trimester is modest, typically totaling <strong>1.1 to 4.4 lbs (0.5 to 2.0 kg)</strong> across all pre-pregnancy BMI categories. This initial weight reflects early maternal blood plasma volume expansion and uterine hypervascularity. Many women experiencing pregnancy-related nausea and vomiting (morning sickness) or clinical hyperemesis gravidarum may experience slight weight loss or zero net gain without adversely impacting embryonic viability.</li>
        <li><strong>Second and Third Trimesters (Weeks 14 to 40):</strong> Commencing at the 14th gestational week, maternal circulating plasma volume expands by 45% to 50%, maternal cardiac output increases by 30% to 50%, the placental vascular bed expands exponentially, amniotic fluid volume accumulates to ~800 mL, and the fetus enters an exponential somatic growth trajectory. Weight gain accelerates to a continuous linear velocity of approximately <strong>0.5 to 1.3 lbs (0.2 to 0.6 kg) per week</strong> depending upon maternal pre-pregnancy BMI classification.</li>
      </ul>

      <h2>Anatomical & Physiological Distribution of Gestational Weight</h2>
      <p>A prevalent misconception is that pregnancy weight gain represents excess adipose accumulation. In reality, for a healthy woman gaining the recommended 30 pounds (13.6 kg) throughout a singleton gestation, maternal adipose tissue accounts for only approximately 25% of the total mass. The remaining 75% represents specialized feto-placental tissues and vital physiological fluid expansions:</p>

      <div class="table-container my-4">
        <table class="data-table">
          <thead>
            <tr>
              <th>Component of Weight Gain</th>
              <th>Average Mass (Pounds)</th>
              <th>Average Mass (Kilograms)</th>
              <th>Percentage of Total Gain</th>
              <th>Primary Biological Function</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Full-Term Infant (Fetus)</strong></td>
              <td>7.5 lbs</td>
              <td>3.4 kg</td>
              <td>25.0%</td>
              <td>Complete somatic and organ mass of term newborn</td>
            </tr>
            <tr>
              <td><strong>Placenta</strong></td>
              <td>1.5 lbs</td>
              <td>0.7 kg</td>
              <td>5.0%</td>
              <td>Hemochorial gas, nutrient, and endocrine exchange organ</td>
            </tr>
            <tr>
              <td><strong>Amniotic Fluid</strong></td>
              <td>2.0 lbs</td>
              <td>0.9 kg</td>
              <td>6.7%</td>
              <td>Protective mechanical cushion and pulmonary development bath</td>
            </tr>
            <tr>
              <td><strong>Uterine Hypertrophy (Myometrium)</strong></td>
              <td>2.0 lbs</td>
              <td>0.9 kg</td>
              <td>6.7%</td>
              <td>Smooth muscle cell hypertrophy from 70g pre-pregnancy to 1000g</td>
            </tr>
            <tr>
              <td><strong>Maternal Breast Tissue</strong></td>
              <td>2.0 lbs</td>
              <td>0.9 kg</td>
              <td>6.7%</td>
              <td>Prolactin-driven lobuloalveolar hyperplasia for lactation</td>
            </tr>
            <tr>
              <td><strong>Maternal Blood Plasma Volume</strong></td>
              <td>4.0 lbs</td>
              <td>1.8 kg</td>
              <td>13.3%</td>
              <td>45–50% hypervolemia to perfuse intervillous spaces</td>
            </tr>
            <tr>
              <td><strong>Extravascular Extracellular Fluid</strong></td>
              <td>4.0 lbs</td>
              <td>1.8 kg</td>
              <td>13.3%</td>
              <td>Physiological maternal interstitial edema and tissue hydration</td>
            </tr>
            <tr>
              <td><strong>Maternal Adipose / Energy Reserves</strong></td>
              <td>7.0 lbs</td>
              <td>3.2 kg</td>
              <td>23.3%</td>
              <td>Subcutaneous and visceral fat stores for third-trimester & lactation</td>
            </tr>
            <tr class="font-bold">
              <td><strong>Total Full-Term Gestational Mass</strong></td>
              <td><strong>30.0 lbs</strong></td>
              <td><strong>13.6 kg</strong></td>
              <td><strong>100.0%</strong></td>
              <td>Balanced maternal-fetal physiological adaptation</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>The IOM & ACOG 2009 Clinical Guidelines & Mathematical Formulas</h2>
      <p>Gestational weight targets are categorized strictly by pre-pregnancy Body Mass Index (BMI), computed from height ($H$) and pre-gestational weight ($W_{\text{pre}}$):</p>

      $$\text{BMI} = \frac{W_{\text{pre}}\text{ (kg)}}{[H\text{ (m)}]^2} = 703 \times \frac{W_{\text{pre}}\text{ (lbs)}}{[H\text{ (in)}]^2}$$

      <p>The Institute of Medicine establishes four discrete pre-pregnancy BMI categories, each associated with specific total gestational weight targets and second/third trimester weekly weight gain rates ($R_{\text{weekly}}$):</p>

      <div class="table-container my-4">
        <table class="data-table">
          <thead>
            <tr>
              <th>Pre-Pregnancy BMI Category</th>
              <th>Baseline BMI Range</th>
              <th>Total Singleton Gain (lbs)</th>
              <th>Total Singleton Gain (kg)</th>
              <th>2nd/3rd Tri Weekly Rate (lbs/wk)</th>
              <th>Twin Gestation Total (lbs)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Underweight</strong></td>
              <td>&lt; 18.5</td>
              <td>28 – 40 lbs</td>
              <td>12.5 – 18.0 kg</td>
              <td>1.0 (range 1.0 – 1.3)</td>
              <td>Insufficient Data (Individualized)</td>
            </tr>
            <tr>
              <td><strong>Normal Weight</strong></td>
              <td>18.5 – 24.9</td>
              <td>25 – 35 lbs</td>
              <td>11.5 – 16.0 kg</td>
              <td>1.0 (range 0.8 – 1.0)</td>
              <td>37 – 54 lbs (16.8 – 24.5 kg)</td>
            </tr>
            <tr>
              <td><strong>Overweight</strong></td>
              <td>25.0 – 29.9</td>
              <td>15 – 25 lbs</td>
              <td>7.0 – 11.5 kg</td>
              <td>0.6 (range 0.5 – 0.7)</td>
              <td>31 – 50 lbs (14.1 – 22.7 kg)</td>
            </tr>
            <tr>
              <td><strong>Obese (All Classes)</strong></td>
              <td>&ge; 30.0</td>
              <td>11 – 20 lbs</td>
              <td>5.0 – 9.0 kg</td>
              <td>0.5 (range 0.4 – 0.6)</td>
              <td>25 – 42 lbs (11.3 – 19.1 kg)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3>Mathematical Trajectory Modeling Across Gestational Age</h3>
      <p>To evaluate whether a patient's current gestational weight gain at week $W$ is clinically appropriate, obstetricians model target lower bound $G_{\min}(W)$ and upper bound $G_{\max}(W)$ using piecewise linear equations. For singleton pregnancies, first-trimester total gain is modeled as 1.1 lbs to 4.4 lbs evenly across the first 13 weeks. From week 14 through 40 ($W \ge 14$):</p>

      $$G_{\min}(W) = 1.1 + (W - 13) \times R_{\min}$$
      $$G_{\max}(W) = 4.4 + (W - 13) \times R_{\max}$$

      <p>Where $R_{\min}$ and $R_{\max}$ represent the lower and upper limits of the recommended weekly gain velocity for that BMI class. For instance, in a normal weight patient ($R_{\min} = 0.8\text{ lbs/wk}, R_{\max} = 1.0\text{ lbs/wk}$), the expected target weight gain at gestational week 24 is calculated as:</p>

      $$G_{\min}(24) = 1.1 + (24 - 13) \times 0.8 = 1.1 + 8.8 = 9.9 \text{ lbs}$$
      $$G_{\max}(24) = 4.4 + (24 - 13) \times 1.0 = 4.4 + 11.0 = 15.4 \text{ lbs}$$

      <p>Thus, at 24 weeks, a normal weight pregnant woman is expected to have gained between 9.9 and 15.4 pounds above her pre-pregnancy baseline weight.</p>

      <h2>Obstetric Risks of Gestational Weight Gain Deviations</h2>
      <p>Maintaining gestational weight gain within evidence-based IOM boundaries directly attenuates serious obstetric and neonatal morbidities. Deviations both above and below the target spectrum carry distinct clinical risks:</p>

      <h3>Risks Associated with Inadequate Gestational Weight Gain</h3>
      <ul>
        <li><strong>Small for Gestational Age (SGA) & IUGR:</strong> Sub-optimal maternal weight gain compromises placental amino acid, glucose, and fatty acid transport, increasing the odds of intrauterine growth restriction and low birthweight (&lt;2500g).</li>
        <li><strong>Spontaneous Preterm Delivery:</strong> Meta-analyses demonstrate a 30% to 50% increase in spontaneous preterm birth (&lt;37 completed weeks) among women with insufficient second- and third-trimester weight gain, predisposing neonates to respiratory distress syndrome (RDS), intraventricular hemorrhage, and neonatal intensive care unit (NICU) admission.</li>
        <li><strong>Impaired Lactogenesis:</strong> Insufficient maternal adipose deposition can diminish long-chain polyunsaturated fatty acid reserves required for successful postpartum exclusive breastfeeding.</li>
      </ul>

      <h3>Risks Associated with Excessive Gestational Weight Gain</h3>
      <ul>
        <li><strong>Gestational Diabetes Mellitus (GDM):</strong> Rapid, excessive adipose expansion exacerbates physiological pregnancy-induced insulin resistance (driven by human placental lactogen, progesterone, and cortisol), precipitating overt hyperglycemia.</li>
        <li><strong>Gestational Hypertension and Preeclampsia:</strong> Excessive volume and systemic inflammatory cytokine release from adipose tissue contribute to endothelial dysfunction, elevating the risk of de novo hypertension, proteinuria, and severe preeclampsia.</li>
        <li><strong>Fetal Macrosomia and Birth Trauma:</strong> Maternal hyperglycemia and elevated circulating amino acids stimulate fetal pancreatic beta-cell hyperplasia and excessive fetal insulin secretion, driving accelerated fetal lipogenesis. Macrosomia (birthweight &gt; 4,000 to 4,500g) dramatically increases the incidence of shoulder dystocia, brachial plexus injury, third- and fourth-degree perineal lacerations, and emergent cesarean section.</li>
        <li><strong>Postpartum Weight Retention (PPWR):</strong> Gestational gain exceeding IOM guidelines is the single strongest predictor of permanent maternal weight retention at 1 and 15 years postpartum, initiating or compounding long-term maternal obesity, metabolic syndrome, and cardiovascular disease.</li>
      </ul>

      <h2>Step-by-Step Worked Clinical Case Study</h2>
      <p>The following case study illustrates an obstetric clinical assessment of gestational weight gain using the IOM 2009 algorithm:</p>

      <div class="worked-example-card my-4">
        <h3 class="example-title">Obstetric Case Profile: Second-Trimester Weight Gain Audit</h3>
        <p><strong>Patient Presentation:</strong> A 29-year-old primigravida presents for her routine 24-week prenatal visit. Pre-pregnancy height was <strong>5 feet 5 inches (65 inches / 1.651 m)</strong> and pre-pregnancy weight was <strong>150.0 lbs (68.04 kg)</strong>. Today at 24 weeks gestation, her clinic scale records <strong>167.0 lbs (75.75 kg)</strong>. Singleton pregnancy confirmed by first-trimester dating ultrasound.</p>
        
        <div class="example-step">
          <div class="step-num">Step 1</div>
          <div class="step-content">
            <strong>Calculate Pre-Pregnancy BMI and Determine IOM Classification:</strong>
            $$\text{BMI} = 703 \times \frac{150.0}{(65)^2} = 703 \times \frac{150.0}{4225} = 703 \times 0.035503 = \mathbf{24.96 \approx 25.0 \text{ kg/m}^2}$$
            A BMI of 25.0 kg/m&sup2; places the patient at the exact threshold between Normal Weight and <strong>Overweight</strong>. Per ACOG clinical practice bulletins, a BMI of 25.0–29.9 is classified as Overweight.
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 2</div>
          <div class="step-content">
            <strong>Identify IOM Recommended Targets for Overweight Category:</strong>
            <ul>
              <li>Total 40-week Gestational Gain: <strong>15 to 25 lbs (7.0 to 11.5 kg)</strong></li>
              <li>1st Trimester Expected Gain: <strong>1.1 to 4.4 lbs</strong></li>
              <li>2nd & 3rd Trimester Weekly Velocity: <strong>0.6 lbs/week (range: 0.5 to 0.7 lbs/week)</strong></li>
            </ul>
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 3</div>
          <div class="step-content">
            <strong>Compute Expected Weight Range at Gestational Week 24:</strong>
            Weeks elapsed in the linear second trimester = $24 - 13 = 11\text{ weeks}$.
            $$G_{\min}(24) = 1.1 + (11 \times 0.5) = 1.1 + 5.5 = \mathbf{6.6 \text{ lbs}}$$
            $$G_{\max}(24) = 4.4 + (11 \times 0.7) = 4.4 + 7.7 = \mathbf{12.1 \text{ lbs}}$$
            Target Maternal Weight Range at Week 24:
            $$\text{Target Weight} = [150.0 + 6.6, 150.0 + 12.1] = \mathbf{156.6 \text{ lbs to } 162.1 \text{ lbs}}$$
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 4</div>
          <div class="step-content">
            <strong>Evaluate Actual Weight Trajectory and Clinical Variance:</strong>
            $$\text{Actual Weight Gain} = 167.0 - 150.0 = \mathbf{17.0 \text{ lbs}}$$
            Comparing actual gain of 17.0 lbs against the week-24 target of 6.6 to 12.1 lbs reveals that the patient has exceeded the upper bound of recommended weight gain by:
            $$\Delta = 17.0 - 12.1 = \mathbf{+4.9 \text{ lbs above maximum recommended trajectory}}$$
            Furthermore, having gained 17.0 lbs already at 24 weeks, she has already surpassed the lower limit of total 40-week recommended gain (15 lbs) with 16 weeks of pregnancy remaining.
          </div>
        </div>

        <div class="example-step">
          <div class="step-num">Step 5</div>
          <div class="step-content">
            <strong>Formulate Obstetric Management and Nutritional Counseling Plan:</strong>
            <ul>
              <li><strong>Dietary Audit:</strong> Evaluate daily caloric intake. The Dietary Reference Intakes (DRI) recommend an additional 340 kcal/day in the second trimester and 452 kcal/day in the third trimester above non-pregnant baseline. Women classified as overweight do not require aggressive caloric surplus; focusing on nutrient density, complex carbohydrates, lean protein, and eliminating sugar-sweetened beverages is recommended. Weight loss during pregnancy is contraindicated.</li>
              <li><strong>Physical Activity:</strong> In the absence of obstetric contraindications (such as placenta previa or cervical insufficiency), prescribe 150 minutes per week of moderate-intensity aerobic exercise (e.g., brisk walking, swimming, prenatal yoga).</li>
              <li><strong>Screening:</strong> Administer standard 50g 1-hour oral glucose challenge test (GCT) for gestational diabetes at 24 to 28 weeks, monitor blood pressure for early signs of preeclampsia, and track fundal height and ultrasound fetal biometry to assess fetal abdominal circumference and growth velocity.</li>
            </ul>
          </div>
        </div>
      </div>

      <h2>Nutritional Energy Requirements During Pregnancy</h2>
      <p>A frequent clinical pitfall is the belief that pregnancy requires "eating for two." Energetic requirements established by the Food and Nutrition Board of the National Academies demonstrate that energy demands during early gestation are virtually unchanged from baseline:</p>
      <ul>
        <li><strong>First Trimester:</strong> $0 \text{ additional kcal/day}$. Caloric needs remain identical to non-pregnant maintenance requirements. Clinical focus centers entirely on micronutrient adequacy: 400 to 800 &mu;g/day of folic acid (to prevent neural tube defects), 27 mg/day of elemental iron, 1,000 mg/day of calcium, and 600 IU/day of vitamin D.</li>
        <li><strong>Second Trimester:</strong> $+340 \text{ kcal/day}$ above non-pregnant expenditure. Equivalent to a single cup of Greek yogurt and an apple, or a small turkey sandwich.</li>
        <li><strong>Third Trimester:</strong> $+452 \text{ kcal/day}$ above non-pregnant expenditure. Sufficient to fuel rapid late-gestation fetal glycogen and lipid accumulation.</li>
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
            <li><a href="due-date-calculator.html">Due Date Calculator</a></li>
            <li><a href="ovulation-calculator.html">Ovulation Calculator</a></li>
            <li><a href="calorie-deficit-calculator.html">Calorie Deficit Calculator</a></li>
            <li><a href="carbohydrate-intake-calculator.html">Carbohydrate Intake Calculator</a></li>
            <li><a href="fat-intake-calculator.html">Fat Intake Calculator</a></li>
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
        <p>&copy; 2026 CalcHub. Educational and clinical calculation tools. Medical calculations must be verified by a board-certified physician.</p>
      </div>
    </div>
  </footer>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const form = document.getElementById('weight-gain-form');
      const unitSystem = document.getElementById('unit-system');
      const gestationType = document.getElementById('gestation-type');
      const heightUsGroup = document.getElementById('height-us-group');
      const heightMetricGroup = document.getElementById('height-metric-group');
      const heightFeet = document.getElementById('height-feet');
      const heightInches = document.getElementById('height-inches');
      const heightCm = document.getElementById('height-cm');
      const preWeight = document.getElementById('pre-weight');
      const currWeight = document.getElementById('curr-weight');
      const weekSlider = document.getElementById('gestational-week');
      const weekDisplay = document.getElementById('week-display');
      const resultsContainer = document.getElementById('calculator-results');
      const weightUnitLabels = document.querySelectorAll('.weight-unit');

      // Unit toggle
      unitSystem.addEventListener('change', function() {
        const isMetric = unitSystem.value === 'metric';
        if (isMetric) {
          heightUsGroup.style.display = 'none';
          heightMetricGroup.style.display = 'block';
          weightUnitLabels.forEach(el => el.textContent = 'kg');
          
          // Convert values if switching
          const ft = parseFloat(heightFeet.value) || 5;
          const inc = parseFloat(heightInches.value) || 5;
          const totalInches = (ft * 12) + inc;
          heightCm.value = (totalInches * 2.54).toFixed(1);

          preWeight.value = (parseFloat(preWeight.value) * 0.453592).toFixed(1);
          currWeight.value = (parseFloat(currWeight.value) * 0.453592).toFixed(1);
        } else {
          heightUsGroup.style.display = 'flex';
          heightMetricGroup.style.display = 'none';
          weightUnitLabels.forEach(el => el.textContent = 'lbs');

          const cm = parseFloat(heightCm.value) || 165;
          const totalInches = cm / 2.54;
          heightFeet.value = Math.floor(totalInches / 12);
          heightInches.value = Math.round(totalInches % 12);

          preWeight.value = (parseFloat(preWeight.value) / 0.453592).toFixed(1);
          currWeight.value = (parseFloat(currWeight.value) / 0.453592).toFixed(1);
        }
      });

      weekSlider.addEventListener('input', function() {
        weekDisplay.textContent = weekSlider.value + ' weeks';
      });

      form.addEventListener('submit', function(e) {
        e.preventDefault();

        const isMetric = unitSystem.value === 'metric';
        const isTwins = gestationType.value === 'twins';
        const week = parseInt(weekSlider.value);

        let heightMeters = 0;
        let preWeightKg = 0;
        let currWeightKg = 0;

        if (isMetric) {
          heightMeters = parseFloat(heightCm.value) / 100;
          preWeightKg = parseFloat(preWeight.value);
          currWeightKg = parseFloat(currWeight.value);
        } else {
          const ft = parseFloat(heightFeet.value) || 0;
          const inc = parseFloat(heightInches.value) || 0;
          const totalIn = (ft * 12) + inc;
          heightMeters = (totalIn * 2.54) / 100;
          preWeightKg = parseFloat(preWeight.value) * 0.453592;
          currWeightKg = parseFloat(currWeight.value) * 0.453592;
        }

        if (!heightMeters || heightMeters <= 0 || !preWeightKg || !currWeightKg) return;

        // BMI calculation
        const bmi = preWeightKg / (heightMeters * heightMeters);

        // BMI category determination
        let bmiCategory = '';
        let minTotalGainLbs = 0;
        let maxTotalGainLbs = 0;
        let weeklyRateLbs = 0;
        let weeklyRateMinLbs = 0;
        let weeklyRateMaxLbs = 0;

        if (isTwins) {
          if (bmi < 25.0) {
            bmiCategory = 'Normal Weight (Twins)';
            minTotalGainLbs = 37;
            maxTotalGainLbs = 54;
            weeklyRateLbs = 1.5;
            weeklyRateMinLbs = 1.4;
            weeklyRateMaxLbs = 1.7;
          } else if (bmi < 30.0) {
            bmiCategory = 'Overweight (Twins)';
            minTotalGainLbs = 31;
            maxTotalGainLbs = 50;
            weeklyRateLbs = 1.4;
            weeklyRateMinLbs = 1.2;
            weeklyRateMaxLbs = 1.5;
          } else {
            bmiCategory = 'Obese (Twins)';
            minTotalGainLbs = 25;
            maxTotalGainLbs = 42;
            weeklyRateLbs = 1.1;
            weeklyRateMinLbs = 1.0;
            weeklyRateMaxLbs = 1.3;
          }
        } else {
          if (bmi < 18.5) {
            bmiCategory = 'Underweight';
            minTotalGainLbs = 28;
            maxTotalGainLbs = 40;
            weeklyRateLbs = 1.0;
            weeklyRateMinLbs = 1.0;
            weeklyRateMaxLbs = 1.3;
          } else if (bmi < 25.0) {
            bmiCategory = 'Normal Weight';
            minTotalGainLbs = 25;
            maxTotalGainLbs = 35;
            weeklyRateLbs = 1.0;
            weeklyRateMinLbs = 0.8;
            weeklyRateMaxLbs = 1.0;
          } else if (bmi < 30.0) {
            bmiCategory = 'Overweight';
            minTotalGainLbs = 15;
            maxTotalGainLbs = 25;
            weeklyRateLbs = 0.6;
            weeklyRateMinLbs = 0.5;
            weeklyRateMaxLbs = 0.7;
          } else {
            bmiCategory = 'Obese';
            minTotalGainLbs = 11;
            maxTotalGainLbs = 20;
            weeklyRateLbs = 0.5;
            weeklyRateMinLbs = 0.4;
            weeklyRateMaxLbs = 0.6;
          }
        }

        // Target for current week
        let minWeekGainLbs = 0;
        let maxWeekGainLbs = 0;

        if (week <= 13) {
          // Trimester 1 linear progression
          const tri1Progress = week / 13;
          minWeekGainLbs = 1.1 * tri1Progress;
          maxWeekGainLbs = 4.4 * tri1Progress;
        } else {
          const tri2Weeks = week - 13;
          minWeekGainLbs = 1.1 + (tri2Weeks * weeklyRateMinLbs);
          maxWeekGainLbs = 4.4 + (tri2Weeks * weeklyRateMaxLbs);
        }

        const actualGainKg = currWeightKg - preWeightKg;
        const actualGainLbs = actualGainKg / 0.453592;

        let unitStr = isMetric ? 'kg' : 'lbs';
        let conv = isMetric ? 0.453592 : 1.0;

        const dispMinTotal = (minTotalGainLbs * conv).toFixed(1);
        const dispMaxTotal = (maxTotalGainLbs * conv).toFixed(1);
        const dispMinWeek = (minWeekGainLbs * conv).toFixed(1);
        const dispMaxWeek = (maxWeekGainLbs * conv).toFixed(1);
        const dispActualGain = (actualGainLbs * conv).toFixed(1);
        const dispWeeklyRate = (weeklyRateLbs * conv).toFixed(1);

        const preWeightDisp = (preWeightKg / (isMetric ? 1 : 0.453592));
        const finalMinWeight = (preWeightDisp + (minTotalGainLbs * conv)).toFixed(1);
        const finalMaxWeight = (preWeightDisp + (maxTotalGainLbs * conv)).toFixed(1);

        // Trajectory status
        let statusBadge = '';
        let interpretation = '';

        if (actualGainLbs < minWeekGainLbs) {
          const deficit = ((minWeekGainLbs - actualGainLbs) * conv).toFixed(1);
          statusBadge = '<span class="status-below">Below Target Range (' + deficit + ' ' + unitStr + ')</span>';
          interpretation = 'Your current weight gain is below the recommended IOM guideline for week ' + week + ' by approximately ' + deficit + ' ' + unitStr + '. Review your nutritional intake with your obstetrician or midwife to ensure adequate fetal growth.';
        } else if (actualGainLbs > maxWeekGainLbs) {
          const excess = ((actualGainLbs - maxWeekGainLbs) * conv).toFixed(1);
          statusBadge = '<span class="status-above">Above Target Range (+' + excess + ' ' + unitStr + ')</span>';
          interpretation = 'Your current weight gain is above the recommended IOM guideline for week ' + week + ' by approximately ' + excess + ' ' + unitStr + '. Discuss balanced caloric intake and gentle physical activity with your healthcare provider to manage risk of macrosomia and gestational diabetes.';
        } else {
          statusBadge = '<span class="status-normal">On Track (Within Recommended Range)</span>';
          interpretation = 'Congratulations! Your weight gain is currently on track within the evidence-based IOM and ACOG target range for week ' + week + ' of gestation.';
        }

        // Render to UI
        document.getElementById('res-bmi').textContent = bmi.toFixed(1);
        document.getElementById('res-bmi-cat').textContent = 'Category: ' + bmiCategory;
        document.getElementById('res-current-week-label').textContent = week;
        document.getElementById('res-week-target').textContent = dispMinWeek + ' – ' + dispMaxWeek + ' ' + unitStr;
        document.getElementById('res-trajectory-status').innerHTML = statusBadge;
        document.getElementById('res-total-target').textContent = dispMinTotal + ' – ' + dispMaxTotal + ' ' + unitStr;
        document.getElementById('res-actual-gain').textContent = (actualGainLbs >= 0 ? '+' : '') + dispActualGain + ' ' + unitStr;
        document.getElementById('res-gain-variance').textContent = (actualGainLbs >= 0 ? 'Maternal gain from baseline' : 'Net weight loss from baseline');
        document.getElementById('res-weekly-rate').textContent = '~' + dispWeeklyRate + ' ' + unitStr + '/week';
        document.getElementById('res-final-target').textContent = finalMinWeight + ' – ' + finalMaxWeight + ' ' + unitStr;
        document.getElementById('res-interpretation-text').textContent = interpretation;

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

def main():
    ovulation_path = os.path.join(BASE_DIR, "ovulation-calculator.html")
    with open(ovulation_path, "w", encoding="utf-8") as f:
        f.write(OVULATION_HTML.strip() + "\n")
    print(f"Generated {os.path.basename(ovulation_path)}")

    pregnancy_path = os.path.join(BASE_DIR, "pregnancy-weight-gain-calculator.html")
    with open(pregnancy_path, "w", encoding="utf-8") as f:
        f.write(PREGNANCY_WEIGHT_HTML.strip() + "\n")
    print(f"Generated {os.path.basename(pregnancy_path)}")

if __name__ == "__main__":
    main()
