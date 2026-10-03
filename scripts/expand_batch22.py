"""
Expansion script for Batch 22 tools that need additional in-depth clinical and scientific content
to easily exceed the 1,000+ words standard in <article class="article-body">.

Target tools:
1. due-date-calculator.html (760 -> >1,100 words)
2. heart-rate-zone-calculator.html (783 -> >1,100 words)
3. lean-body-mass-calculator.html (747 -> >1,150 words)
4. max-heart-rate-calculator.html (850 -> >1,150 words)
5. met-calculator.html (696 -> >1,150 words)
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -----------------------------------------------------------------
# 1. due-date-calculator.html expansion
# -----------------------------------------------------------------
DUE_DATE_EXTRA = r"""
        <h2>ACOG / SMFM Classification of Term Pregnancy</h2>
        <p>
          Historically, any delivery occurring between 37 weeks 0 days and 41 weeks 6 days was broadly designated as a "term pregnancy." However, extensive neonatal epidemiological data published by the American College of Obstetricians and Gynecologists (ACOG) and the Society for Maternal-Fetal Medicine (SMFM) demonstrated that neonatal morbidity varies significantly within this five-week window. In response, modern obstetrics subdivides term gestations into four precise clinical categories:
        </p>
        <div class="table-responsive my-4">
          <table class="data-table">
            <thead>
              <tr>
                <th>Clinical Classification</th>
                <th>Gestational Age Window</th>
                <th>Neonatal Morbidity Profile</th>
                <th>Obstetric Management Strategy</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Early Term</strong></td>
                <td>37w 0d to 38w 6d</td>
                <td>Elevated risk of transient tachypnea of the newborn (TTN), respiratory distress syndrome (RDS), hypoglycemia, and NICU admission compared to full term.</td>
                <td>Elective induction or cesarean delivery without medical indication is strictly contraindicated prior to 39 weeks.</td>
              </tr>
              <tr>
                <td><strong>Full Term</strong></td>
                <td>39w 0d to 40w 6d</td>
                <td>Lowest incidence of neonatal adverse outcomes, lowest perinatal mortality, and optimal neurodevelopmental indices.</td>
                <td>Ideal window for planned delivery when indicated; spontaneous labor strongly encouraged in uncomplicated pregnancies.</td>
              </tr>
              <tr>
                <td><strong>Late Term</strong></td>
                <td>41w 0d to 41w 6d</td>
                <td>Progressive increase in oligohydramnios, fetal macrosomia, shoulder dystocia, meconium aspiration syndrome, and non-reassuring fetal heart tracings.</td>
                <td>Twice-weekly antenatal surveillance (non-stress test and amniotic fluid index) initiated; labor induction typically offered.</td>
              </tr>
              <tr>
                <td><strong>Post-Term</strong></td>
                <td>&ge; 42w 0d</td>
                <td>Placental senescence and vascular sclerosis cause placental insufficiency, fetal dysmaturity syndrome, umbilical cord compression, and a doubling of stillbirth risk.</td>
                <td>Active induction of labor universally indicated; expectant management past 42 weeks carries severe perinatal liability.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2>Epidemiology of Spontaneous Delivery Timing</h2>
        <p>
          While pregnant patients frequently focus on their exact 40-week Estimated Date of Delivery, large-scale population registries (such as the National Center for Health Statistics) demonstrate that only approximately <strong>4% of women give birth on their precise due date</strong>. Human gestation naturally follows a Gaussian distribution centered around the 280-day mark:
        </p>
        <ul>
          <li>Approximately <strong>60% of deliveries</strong> occur within one week (±7 days) of the calculated due date.</li>
          <li>Roughly <strong>80% of deliveries</strong> occur within two weeks (±14 days) of the estimated delivery date.</li>
          <li>Nulliparous women (first-time mothers) experience a slightly longer median gestation of <strong>282 to 288 days</strong> (40 weeks 2 days to 41 weeks 1 day) compared to multiparous women, whose median gestation spans <strong>280 to 283 days</strong>.</li>
        </ul>

        <h2>Antenatal Surveillance and Cervical Ripening in Post-Dates Gestation</h2>
        <p>
          When an uncomplicated pregnancy reaches the late-term window (41w0d), obstetricians initiate standardized biophysical testing to verify ongoing uteroplacental competence. The primary diagnostic modalities include:
        </p>
        <ul>
          <li><strong>The Non-Stress Test (NST):</strong> Electronic fetal monitoring tracks fetal heart rate accelerations (defined at &ge;32 weeks as an increase of &ge;15 bpm above baseline lasting &ge;15 seconds over a 20-minute window), confirming normal autonomic neurologic integration and absence of acidemia.</li>
          <li><strong>Amniotic Fluid Index (AFI) or Deepest Vertical Pocket (DVP):</strong> Diminished fetal renal perfusion resulting from placental insufficiency shunts blood to the fetal brain and myocardium, decreasing fetal urine production and causing <em>oligohydramnios</em> (defined as AFI &lt; 5.0 cm or DVP &lt; 2.0 cm), an absolute indication for expedited delivery.</li>
          <li><strong>The Bishop Score:</strong> Prior to initiating labor induction, the clinician evaluates cervical status across five physical parameters: cervical dilation, effacement, fetal station, cervical consistency, and cervical position. A Bishop score &ge; 8 predicts high likelihood of successful vaginal delivery equivalent to spontaneous labor onset, whereas an unfavorable score (&le; 6) mandates cervical ripening with pharmacological prostaglandins ($PGE_1$ misoprostol, $PGE_2$ dinoprostone) or mechanical methods (transcervical Foley balloon catheter dilation).</li>
        </ul>
"""

# -----------------------------------------------------------------
# 2. heart-rate-zone-calculator.html expansion
# -----------------------------------------------------------------
HEART_RATE_ZONE_EXTRA = r"""
        <h2>Cardiovascular Drift and Environmental Thermoregulation</h2>
        <p>
          During prolonged, steady-state aerobic exercise lasting beyond 45 to 60 minutes—particularly in warm, humid ambient environments—athletes frequently observe a steady, continuous upward creep in heart rate despite maintaining a completely constant mechanical pace or cycling power output. This physiological phenomenon is termed <strong>Cardiovascular Drift (Cardiac Drift)</strong>.
        </p>
        <p>
          Cardiovascular drift is precipitated by thermoregulatory cutaneovascular adaptations and progressive dehydration:
        </p>
        <ul>
          <li><strong>Cutaneous Vasodilation and Plasma Loss:</strong> To dissipate excessive metabolic heat generated by muscular contraction, the autonomic nervous system shunts blood to peripheral cutaneous capillary beds for evaporative cooling. Concurrently, fluid transudation through active eccrine sweat glands progressively reduces circulating blood plasma volume by 5% to 12%.</li>
          <li><strong>Compensatory Tachycardia via the Fick Principle:</strong> Reduced central blood volume attenuates venous return (preload) to the right atrium, decreasing end-diastolic ventricular filling and lowering stroke volume ($SV$) by 10% to 15%. Because systemic oxygen consumption ($VO_2$) remains fixed by the steady-state workload, cardiac output ($CO = HR \times SV$) must remain constant. To compensate for the falling stroke volume, the autonomic nervous system reflexively accelerates heart rate:
          $$\uparrow HR = \frac{CO}{\downarrow SV}$$
          </li>
        </ul>
        <p>
          Consequently, an athlete running at a steady 8:00 min/mile pace in Zone 2 (e.g., 135 BPM) may find their heart rate drifting into high Zone 3 or Zone 4 (150+ BPM) after 75 minutes. In this situation, the elevated heart rate reflects thermoregulatory and hemodynamic compensation rather than an increase in muscular glycolytic energy demand.
        </p>

        <h2>Training Intensity Distributions: Polarized (80/20) vs. Pyramidal Models</h2>
        <p>
          In contemporary sports science, pioneering observational studies by Dr. Stephen Seiler across world-class Olympic endurance competitors (cross-country skiers, rowers, marathon runners, and pursuit cyclists) have illuminated optimal weekly training intensity distributions:
        </p>
        <div class="table-responsive my-4">
          <table class="data-table">
            <thead>
              <tr>
                <th>Training Distribution Model</th>
                <th>Low-Intensity Volume (Zone 1 &amp; 2)</th>
                <th>Threshold Volume (Zone 3 &amp; 4)</th>
                <th>High-Intensity Volume (Zone 5 / Sprint)</th>
                <th>Physiological Mechanism &amp; Overtraining Risk</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Polarized Model (80/20 Paradigm)</strong></td>
                <td>75% – 85% of sessions</td>
                <td>&lt; 5% of sessions</td>
                <td>15% – 20% of sessions</td>
                <td>Maximizes mitochondrial volume without autonomic nervous system exhaustion. Avoids middle-intensity chronic fatigue while maximizing neuromuscular adaptations during hard interval sessions.</td>
              </tr>
              <tr>
                <td><strong>Pyramidal Model</strong></td>
                <td>70% – 80% of sessions</td>
                <td>15% – 20% of sessions</td>
                <td>5% – 10% of sessions</td>
                <td>Gradual tapering of volume across increasing intensities. Highly effective during race-specific mesocycles (e.g., half-marathon or marathon tempo preparation).</td>
              </tr>
              <tr>
                <td><strong>Threshold Model ("Black Hole" Training)</strong></td>
                <td>40% – 50% of sessions</td>
                <td>45% – 55% of sessions</td>
                <td>&lt; 5% of sessions</td>
                <td>Chronically stresses sympathetic nervous system; elevates resting cortisol; causes persistent glycogen depletion and autonomic staleness without inducing superior aerobic base gains.</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p>
          Dr. Seiler identified that recreational athletes frequently fall into the <em>"Threshold Trap"</em> (or "Zone 3 Black Hole"). They perform their easy recovery sessions at too intense a pace (straying into Zone 3 tempo), which induces chronic autonomic nervous system fatigue and prevents them from performing their hard Zone 5 interval sessions with adequate neuromuscular velocity and power output.
        </p>

        <h2>Autonomic Recovery and Heart Rate Variability (HRV) Biomarkers</h2>
        <p>
          Heart rate is not a static metronome; the temporal interval between successive R-waves on an electrocardiogram (the $R\text{-}R$ interval, measured in milliseconds) varies beat-by-beat under the fluctuating balance of the sympathetic and parasympathetic branches of the autonomic nervous system. This variation is quantified as <strong>Heart Rate Variability (HRV)</strong>.
        </p>
        <p>
          During high-intensity Zone 4 and Zone 5 efforts, parasympathetic vagal outflow is completely withdrawn, and sympathetic epinephrine release drives $R\text{-}R$ interval variability close to zero. Post-exercise, <strong>vagal reactivation velocity</strong> determines the rate of cardiovascular recovery. Clinicians and sports physiologists measure <em>Heart Rate Recovery at 1 minute ($HRR_1$)</em> following cessation of exercise. A decline of &gt;25 to 30 beats within the first 60 seconds indicates robust parasympathetic reactivation and low cardiovascular mortality risk, whereas an $HRR_1 &lt; 12\text{ bpm}$ indicates sympathetic hyper-reactivity, cardiac autonomic neuropathy, or severe overtraining syndrome.
        </p>
"""

# -----------------------------------------------------------------
# 3. lean-body-mass-calculator.html expansion
# -----------------------------------------------------------------
LEAN_BODY_MASS_EXTRA = r"""
        <h2>Clinical Pharmacology: Hydrophilic vs. Lipophilic Drug Dosing</h2>
        <p>
          In clinical medicine, intensive care, and surgical anesthesiology, accurate quantification of Lean Body Mass ($LBM$) is a matter of critical patient safety. Historically, pharmacological dosing algorithms based solely on Total Body Weight ($TBW$) have caused devastating adverse drug events in overweight and obese individuals.
        </p>
        <p>
          The volume of distribution ($V_d$) and clearance of therapeutic agents depend fundamentally on whether a drug is <strong>hydrophilic (water-soluble)</strong> or <strong>lipophilic (fat-soluble)</strong>:
        </p>
        <div class="table-responsive my-4">
          <table class="data-table">
            <thead>
              <tr>
                <th>Pharmacological Class</th>
                <th>Representative Medications</th>
                <th>Tissue Distribution Kinetics</th>
                <th>Standard Clinical Dosing Metric</th>
                <th>Risk of Dosing on Total Body Weight (TBW)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Hydrophilic Antibiotics</strong></td>
                <td>Gentamicin, Tobramycin, Vancomycin, Amikacin</td>
                <td>Distributes exclusively into extracellular water and vascular compartments; virtually zero distribution into adipose triglycerides.</td>
                <td><strong>Lean Body Mass (LBM)</strong> or Adjusted Body Weight (ABW)</td>
                <td>Severe acute kidney injury (nephrotoxicity), permanent ototoxicity, and neuromuscular blockade from excessive peak concentrations.</td>
              </tr>
              <tr>
                <td><strong>Intravenous Anesthetics</strong></td>
                <td>Propofol (induction bolus), Remifentanil, Cisatracurium</td>
                <td>Rapidly equilibrates with vessel-rich lean organ mass (brain, heart, liver, kidneys); adipose tissue acts as a delayed, inert reservoir.</td>
                <td><strong>Boer Lean Body Mass (LBM)</strong></td>
                <td>Catastrophic circulatory collapse, severe hypotension, delayed emergence from anesthesia, and prolonged apnea.</td>
              </tr>
              <tr>
                <td><strong>Low Molecular Weight Heparins</strong></td>
                <td>Enoxaparin (Lovenox), Dalteparin</td>
                <td>Confined predominantly to intravascular plasma volume, which expands proportionally with lean mass, not adipose mass.</td>
                <td><strong>Total Body Weight capped</strong> at Lean Mass limits</td>
                <td>Major hemorrhagic complications, intracranial hemorrhage, and retroperitoneal hematoma.</td>
              </tr>
              <tr>
                <td><strong>Chemotherapeutic Agents</strong></td>
                <td>Methotrexate, Cisplatin, Doxorubicin</td>
                <td>Metabolized and cleared by renal tubular secretion and hepatic cytochrome P450 enzymes residing in lean visceral mass.</td>
                <td><strong>Body Surface Area ($BSA$)</strong> derived from Lean Mass models</td>
                <td>Life-threatening bone marrow aplasia (neutropenic sepsis) and severe cardiotoxicity.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2>Sarcopenia, Muscle Quality, and the Aging Somatotype</h2>
        <p>
          As adults advance past the fourth decade of life, human musculoskeletal architecture undergoes involuntary, age-related changes known as <strong>sarcopenia</strong>. Sarcopenia is defined by the <em>European Working Group on Sarcopenia in Older People (EWGSOP2)</em> as a progressive generalized skeletal muscle disorder involving accelerated loss of muscle mass, architectural muscle quality, and physical functional performance.
        </p>
        <p>
          Sarcopenia represents a silent metabolic crisis:
        </p>
        <ul>
          <li><strong>Age-Related Mass Loss Velocity:</strong> Beginning at age 30, inactive adults lose approximately 3% to 8% of skeletal muscle mass per decade, accelerating to &gt;1% per year after age 60. This is accompanied by denervation of fast-twitch Type II motor units and inter-muscular adipose tissue infiltration (myosteatosis).</li>
          <li><strong>Metabolic Dysregulation:</strong> Skeletal muscle is the primary destination for insulin-stimulated glucose disposal (accounting for &gt;80% of postprandial glucose uptake via $GLUT4$ translocation). Loss of lean tissue mass precipitates systemic insulin resistance, impaired glycemic control, and metabolic syndrome—even when total body scale weight remains completely unchanged (a condition known as <em>sarcopenic obesity</em>).</li>
          <li><strong>EWGSOP2 Diagnostic Cutoffs:</strong> Clinical diagnosis utilizes dual-energy X-ray absorptiometry (DXA) to measure Appendicular Lean Mass ($ALM$, the lean mass of all four limbs). Sarcopenia is formally diagnosed when normalized appendicular mass falls below $7.0\text{ kg/m}^2$ in men or $5.5\text{ kg/m}^2$ in women, coupled with low handgrip dynamometer strength (&lt;27 kg in men, &lt;16 kg in women).</li>
        </ul>

        <h2>Basal Metabolic Rate &amp; The Katch-McArdle Lean Mass Formula</h2>
        <p>
          Most legacy metabolic formulas—including the Harris-Benedict (1919) and Mifflin-St Jeor (1990) equations—estimate daily Basal Metabolic Rate ($BMR$) using total scale weight, stature, age, and sex. However, adipose tissue is metabolically inert relative to lean tissue, consuming only ~4.5 kcal per kilogram per day, whereas lean skeletal muscle consumes ~13 kcal/kg/day and vital visceral organs (liver, brain, heart, kidneys) consume 200 to 440 kcal/kg/day.
        </p>
        <p>
          In 1996, exercise physiologists Frank Katch and William McArdle formulated the <strong>Katch-McArdle Equation</strong>, the only universally validated metabolic model that calculates basal metabolic requirements exclusively from Lean Body Mass:
        </p>
        $$BMR\text{ (kcal/day)} = 370 + (21.6 \times LBM\text{ in kg})$$
        <p>
          By anchoring caloric baseline to metabolically active lean mass, the Katch-McArdle formula eliminates the systematic overestimation of caloric expenditure common in obese populations and accurately reflects the elevated metabolic engine of muscular strength athletes.
        </p>
"""

# -----------------------------------------------------------------
# 4. max-heart-rate-calculator.html expansion
# -----------------------------------------------------------------
MAX_HEART_RATE_EXTRA = r"""
        <h2>Standard Error of Estimate (SEE) and Individual Dispersion</h2>
        <p>
          A vital clinical reality emphasized by exercise physiologists—and routinely overlooked in commercial fitness applications—is that all population regression equations represent <em>statistical averages</em>, not immutable biological laws. Every maximum heart rate formula carries a significant <strong>Standard Error of Estimate (SEE)</strong>:
        </p>
        <div class="formula-box my-4">
          <p><strong>Statistical Dispersion in Population HRmax Equations:</strong></p>
          $$\text{Tanaka Formula SEE} = \pm 7.2\text{ to } 10.0\text{ BPM}$$
          $$\text{Gellish Formula SEE} = \pm 7.0\text{ to } 8.5\text{ BPM}$$
          $$\text{Fox Legacy Formula SEE} = \pm 11.0\text{ to } 12.5\text{ BPM}$$
        </div>
        <p>
          Applying standard Gaussian probability to a 40-year-old individual whose Tanaka-predicted HRmax is 180 BPM:
        </p>
        <ul>
          <li><strong>68% of Individuals (1 Standard Deviation):</strong> True physiological maximum heart rate falls between <strong>172 and 188 BPM</strong> (within ±8 BPM).</li>
          <li><strong>95% of Individuals (2 Standard Deviations):</strong> True HRmax falls between <strong>164 and 196 BPM</strong> (within ±16 BPM).</li>
          <li><strong>5% Extreme Outliers:</strong> Approximately 1 in 20 healthy adults exhibits a true physiological maximum heart rate that diverges by more than <strong>16 to 20 BPM</strong> from any mathematical formula!</li>
        </ul>
        <p>
          <strong>Training Prescription Hazard:</strong> If an athlete whose true maximum heart rate is 198 BPM relies on an unadjusted formula predicting 180 BPM, their calculated Zone 4 threshold (85% = 153 BPM) will actually correspond to a leisurely 77% of their true capacity. Conversely, an athlete with an innate maximum of 165 BPM prescribed 153 BPM will unknowingly be pushed into intense, fatiguing anaerobic distress.
        </p>

        <h2>Gold-Standard Laboratory Testing: Cardiopulmonary Exercise Testing (CPET)</h2>
        <p>
          To establish true maximum heart rate without mathematical approximation, exercise physiologists conduct a <strong>Cardiopulmonary Exercise Test (CPET)</strong> utilizing breath-by-breath metabolic gas analysis cart and continuous 12-lead electrocardiography. Protocols include the standardized Bruce treadmill protocol or incremental ramp cycle ergometry.
        </p>
        <p>
          True physiological maximal exertion ($HR_{\text{max}}$ and $VO_2\text{max}$) is objectively confirmed only when at least three of the following five clinical criteria are fulfilled:
        </p>
        <ol>
          <li><strong>Oxygen Uptake Plateau:</strong> Failure of $VO_2$ to increase by &gt;150 mL/min (or &lt;2.1 mL/kg/min) despite a prescribed increase in treadmill speed or elevation.</li>
          <li><strong>Respiratory Exchange Ratio ($RER$):</strong> Carbon dioxide production divided by oxygen uptake ($VCO_2 / VO_2$) exceeding <strong>1.10 to 1.15</strong>, confirming massive bicarbonate buffering of lactic acidosis.</li>
          <li><strong>Post-Exercise Blood Lactate:</strong> Capillary blood lactate concentration exceeding <strong>8.0 mmol/L</strong> drawn 2 to 5 minutes post-exhaustion.</li>
          <li><strong>Rating of Perceived Exertion (RPE):</strong> A score of <strong>19 or 20</strong> on the 15-point Borg Scale, or a 10 on the Category-Ratio 10 (CR10) scale.</li>
          <li><strong>Heart Rate Plateau:</strong> Heart rate failing to rise further despite increasing mechanical workload, or achieving within ±5 bpm of age-predicted maximum.</li>
        </ol>

        <h2>Impact of Cardiovascular Pharmacotherapy on Chronotropic Dynamics</h2>
        <p>
          Prescription cardiovascular medications fundamentally alter sinoatrial nodal pacemaking and blunting maximum chronotropic capacity:
        </p>
        <ul>
          <li><strong>$\beta$-Adrenergic Receptor Antagonists (Beta-Blockers):</strong> Agents such as metoprolol succinate, atenolol, bisoprolol, and carvedilol competitively inhibit $\beta_1$-adrenergic receptors in nodal tissue. They attenuate maximum exercise heart rate by <strong>20% to 35%</strong> (typically capping peak exercise rate at 120 to 140 BPM regardless of age). <em>Clinical Rule:</em> Mathematical HRmax equations must never be utilized for patients on beta-blocker therapy; exercise prescription must be guided by Borg RPE or physician-supervised stress testing.</li>
          <li><strong>Non-Dihydropyridine Calcium Channel Blockers:</strong> Diltiazem and verapamil inhibit slow inward calcium currents ($I_{Ca-L}$) in SA and AV nodal cells, dampening peak exercise heart rate by 10 to 15 bpm.</li>
          <li><strong>Sympathomimetic Agents:</strong> Central nervous system stimulants (such as amphetamines, methylphenidate, high-dose caffeine, and pseudoephedrine) accelerate resting and submaximal heart rates without meaningfully expanding the intrinsic physiological HRmax ceiling.</li>
        </ul>
"""

# -----------------------------------------------------------------
# 5. met-calculator.html expansion
# -----------------------------------------------------------------
MET_CALCULATOR_EXTRA = r"""
        <h2>METs in Clinical Cardiology &amp; Diagnostic Exercise Stress Testing</h2>
        <p>
          In clinical cardiology, functional capacity expressed in METs represents the single most powerful prognostic indicator of both cardiac and all-cause mortality. During diagnostic treadmill stress testing (such as the standard <strong>Bruce Protocol</strong>, where speed and incline increase every 3 minutes):
        </p>
        <div class="table-responsive my-4">
          <table class="data-table">
            <thead>
              <tr>
                <th>Bruce Protocol Stage</th>
                <th>Treadmill Speed &amp; Incline</th>
                <th>Equivalent MET Demand</th>
                <th>Oxygen Uptake ($VO_2$)</th>
                <th>Clinical Diagnostic &amp; Prognostic Significance</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Stage 1 (Minutes 1–3)</strong></td>
                <td>1.7 mph @ 10% Grade</td>
                <td>4.6 METs</td>
                <td>16.1 mL/kg/min</td>
                <td>Inability to complete Stage 1 indicates severe physical impairment, advanced heart failure, or severe peripheral artery disease.</td>
              </tr>
              <tr>
                <td><strong>Stage 2 (Minutes 4–6)</strong></td>
                <td>2.5 mph @ 12% Grade</td>
                <td>7.0 METs</td>
                <td>24.5 mL/kg/min</td>
                <td>Minimum functional capacity required to perform strenuous activities of daily living without angina or excessive dyspnea.</td>
              </tr>
              <tr>
                <td><strong>Stage 3 (Minutes 7–9)</strong></td>
                <td>3.4 mph @ 14% Grade</td>
                <td>10.1 METs</td>
                <td>35.4 mL/kg/min</td>
                <td><strong>The 10-MET Survival Milestone:</strong> Achieving Stage 3 conveys exceptional long-term cardiac prognosis, regardless of baseline coronary artery calcium (CAC).</td>
              </tr>
              <tr>
                <td><strong>Stage 4 (Minutes 10–12)</strong></td>
                <td>4.2 mph @ 16% Grade</td>
                <td>13.5 METs</td>
                <td>47.3 mL/kg/min</td>
                <td>High aerobic endurance capacity; characteristic of competitive athletic populations and master endurance runners.</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p>
          <strong>The Myers Landmark Veterans Affairs Trial:</strong> In a landmark investigation published in the <em>New England Journal of Medicine</em> by Dr. Jonathan Myers and colleagues evaluating 6,213 men undergoing treadmill exercise testing, peak exercise capacity in METs was stronger than any other clinical variable (including smoking, hypertension, diabetes, and left ventricular ejection fraction) in predicting mortality:
        </p>
        <ul>
          <li><strong>The 12% Survival Dividend:</strong> Every 1 MET increase in peak aerobic exercise capacity was associated with a <strong>12% improvement in overall survival</strong>.</li>
          <li>Patients capable of exercising beyond <strong>10 METs</strong> had an annual mortality rate of less than 1%, whereas those achieving less than 5 METs experienced an annual mortality rate exceeding 5% to 8%.</li>
          <li><strong>Pre-Operative Surgical Clearance:</strong> The American College of Cardiology and American Heart Association (ACC/AHA) pre-operative guidelines utilize the 4-MET milestone (the ability to climb two flights of stairs or walk briskly up a hill without stopping) as the threshold for proceeding with major elective non-cardiac surgery without invasive cardiac catheterization.</li>
        </ul>

        <h2>Gross Energy Expenditure vs. Net Energy Expenditure</h2>
        <p>
          A frequent mathematical and nutritional error in sports nutrition is failing to distinguish between <strong>Gross Caloric Expenditure</strong> and <strong>Net Caloric Expenditure</strong>:
        </p>
        <ul>
          <li><strong>Gross Energy Expenditure:</strong> Represents the entire caloric burn measured during an exercise session. It includes both the energy required for mechanical movement AND the baseline resting metabolic rate that the individual would have burned anyway simply by staying alive.
          $$\text{Gross Energy Rate} = \text{MET} \times \frac{3.5 \times \text{Weight (kg)}}{200} \text{ kcal/min}$$
          </li>
          <li><strong>Net Energy Expenditure:</strong> Isolates the true <em>additional</em> caloric cost of the physical activity above resting baseline. Because 1 MET is by definition resting metabolic rate, Net METs is calculated by subtracting 1.0:
          $$\text{Net METs} = \text{Gross METs} - 1.0$$
          $$\text{Net Caloric Burn} = (\text{MET} - 1.0) \times \frac{3.5 \times \text{Weight (kg)}}{200} \times \text{Duration (min)}$$
          </li>
        </ul>
        <p>
          <strong>Nutritional Case Example:</strong> If an 80 kg individual cycles at 6.0 METs for 60 minutes:
        </p>
        $$\text{Gross Burn} = 6.0 \times \frac{3.5 \times 80}{200} \times 60 = 6.0 \times 1.4 \times 60 = \mathbf{504\text{ kcal}}$$
        $$\text{Net Burn} = (6.0 - 1.0) \times \frac{3.5 \times 80}{200} \times 60 = 5.0 \times 1.4 \times 60 = \mathbf{420\text{ kcal}}$$
        <p>
          The difference of 84 kcal represents resting basal expenditure. If a person adds the full 504 gross kcal to their total daily energy intake while also calculating their BMR for the full 24 hours, they are <em>double-counting</em> those 84 calories, gradually compromising fat loss over consecutive training weeks.
        </p>
"""

def expand_tool(filename, extra_html):
    filepath = os.path.join(BASE_DIR, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filename}")
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Insert extra_html immediately before </article>
    if "</article>" not in content:
        print(f"No </article> in {filename}")
        return False

    # Check if already expanded
    if "Classification of Term Pregnancy" in content or "Cardiovascular Drift" in content or "Pharmacological Class" in content or "Statistical Dispersion in Population" in content or "The Myers Landmark Veterans Affairs" in content:
        print(f"Already expanded: {filename}")
        return True

    updated = content.replace("</article>", extra_html.strip() + "\n    </article>")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(updated)

    print(f"Successfully expanded: {filename}")
    return True

def main():
    expand_tool("due-date-calculator.html", DUE_DATE_EXTRA)
    expand_tool("heart-rate-zone-calculator.html", HEART_RATE_ZONE_EXTRA)
    expand_tool("lean-body-mass-calculator.html", LEAN_BODY_MASS_EXTRA)
    expand_tool("max-heart-rate-calculator.html", MAX_HEART_RATE_EXTRA)
    expand_tool("met-calculator.html", MET_CALCULATOR_EXTRA)

if __name__ == "__main__":
    main()
