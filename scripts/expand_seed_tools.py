# -*- coding: utf-8 -*-
"""
Script to expand the 32 early seed tools on CalcHub to 1,100+ words.
Adds rigorous technical sections, mathematical derivations, engineering tables,
and authoritative industry standards before FAQ sections.
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXPANSIONS = {
    "age-calculator.html": """
      <h2>Calendar Mathematics & Astronomical Time Reckoning</h2>
      <p>The calculation of exact chronological age rests on the structural mechanics of the Gregorian calendar, adopted by Pope Gregory XIII in October 1582 to correct the drift of the Julian calendar against the solar tropical year. The tropical year—the duration for Earth to complete one revolution relative to the vernal equinox—averages exactly $365.24219$ mean solar days ($365\text{ days, } 5\text{ hours, } 48\text{ minutes, and } 45\text{ seconds}$).</p>
      
      <p>Because integer calendars cannot allocate fractional days each year, the Gregorian system establishes an interlocking quadrennial and centurial intercalation rule:</p>
      <ul>
        <li>Every year evenly divisible by 4 is a leap year (adding February 29th).</li>
        <li>Except years evenly divisible by 100, which are standard 365-day years (e.g., 1800, 1900, 2100).</li>
        <li>Unless such centurial years are also evenly divisible by 400, in which case they remain leap years (e.g., 1600, 2000, 2400).</li>
      </ul>
      <p>This 400-year cycle comprises exactly $146,097$ days, yielding an average Gregorian year length of exactly $\frac{146{,}097}{400} = 365.2425\text{ days}$, producing an infinitesimal error of only one day every $3,236$ years.</p>

      <h3>Astronomical Julian Day Number (JDN) Dating Algorithm</h3>
      <p>For scientific chronology, actuarial computing, and satellite telemetry, calendar date deltas are computed without month-length ambiguity by converting calendar dates into continuous astronomical <strong>Julian Day Numbers (JDN)</strong>. For any Gregorian date with year $Y$, month $M$ (where January = 1, February = 2), and day $D$, the integer Julian Day Number at Greenwich mean noon is evaluated as:</p>
      <div class="math-block">
        $$a = \left\lfloor \frac{14 - M}{12} \right\rfloor,\quad y = Y + 4800 - a,\quad m = M + 12a - 3$$
        $$JDN = D + \left\lfloor \frac{153m + 2}{5} \right\rfloor + 365y + \left\lfloor \frac{y}{4} \right\rfloor - \left\lfloor \frac{y}{100} \right\rfloor + \left\lfloor \frac{y}{400} \right\rfloor - 32045$$
      </div>
      <p>Subtracting the birth date JDN from the reference date JDN yields the exact, invariant integer count of astronomical elapsed days lived ($N_{\text{days}} = JDN_{\text{target}} - JDN_{\text{birth}}$).</p>

      <h3>Actuarial Demography: Period Life Tables & Cohort Survival</h3>
      <p>In life insurance underwriting and social security administration, chronological age determines actuarial mortality hazard rates ($q_x$, the conditional probability that an individual aged $x$ dies before reaching age $x+1$). Under the Gompertz-Makeham law of mortality, adult human mortality risk accelerates exponentially with chronological age:</p>
      <div class="math-block">
        $$\mu(x) = A + B \cdot c^x$$
      </div>
      <p>Where $A$ denotes extrinsic age-independent baseline risk (trauma, environmental hazards), $B$ represents intrinsic biological vulnerability, and $c \approx 1.08 \text{ to } 1.10$ denotes the annual doubling rate of mortality hazard (approximately doubling every 7 to 8 years of chronological lifespan).</p>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Chronological Age Bracket</th>
            <th>Primary Biological Milestone</th>
            <th>Cognitive & Neurological Baseline</th>
            <th>Clinical Assessment Focus</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>0–24 Months (Infancy)</strong></td>
            <td>Synaptogenesis, rapid skeletal elongation</td>
            <td>Sensorimotor integration, language acquisition</td>
            <td>Pediatric WHO percentile growth curves</td>
          </tr>
          <tr>
            <td><strong>12–18 Years (Adolescence)</strong></td>
            <td>Pubertal growth spurt, epiphyseal fusion</td>
            <td>Prefrontal cortex myelination & pruning</td>
            <td>Endocrine maturation, postural spinal screening</td>
          </tr>
          <tr>
            <td><strong>25–40 Years (Early Adulthood)</strong></td>
            <td>Peak skeletal bone mineral density</td>
            <td>Stabilized executive executive function</td>
            <td>Cardiovascular lipid profiles, metabolic baseline</td>
          </tr>
          <tr>
            <td><strong>40–65 Years (Middle Adulthood)</strong></td>
            <td>Sarcopenic onset, decline in $VO_{2}\text{max}$</td>
            <td>Fluid intelligence transition to crystallized knowledge</td>
            <td>Vascular compliance, glycemic control (HbA1c)</td>
          </tr>
          <tr>
            <td><strong>65+ Years (Older Adulthood)</strong></td>
            <td>Cellular senescence, telomeric shortening</td>
            <td>Cognitive reserve mobilization</td>
            <td>Bone densitometry (DEXA), functional mobility</td>
          </tr>
        </tbody>
      </table>
""",

    "body-fat-calculator.html": """
      <h2>Mathematical Formulations of Body Composition Modeling</h2>
      <p>The quantification of human body composition divides total body mass ($BM$) into distinct physiological compartments. While simple 2-compartment (2C) models partition mass strictly into <strong>Fat Mass (FM)</strong> and <strong>Fat-Free Mass (FFM)</strong> ($BM = FM + FFM$), clinical reference standards utilize 4-compartment (4C) models that independently measure total body water ($TBW$), bone mineral content ($BMC$), total body protein, and adipose lipids:</p>
      <div class="math-block">
        $$BM = \text{Fat Mass} + \text{Total Body Water} + \text{Bone Mineral Content} + \text{Residual Protein}$$
      </div>

      <h3>Hydrostatic Weighing & Siri / Brožek Density Equations</h3>
      <p>The foundational gold standard for whole-body densitometry originates from Archimedes' principle of hydrostatic submersion. When an individual is submerged underwater following full expiration of pulmonary air, body volume ($V_b$) equals the displaced fluid volume minus residual lung volume ($RV$) and gastrointestinal gas volume ($V_{GI} \approx 0.1\text{ L}$):</p>
      <div class="math-block">
        $$D_b = \frac{M_{\text{air}}}{\frac{M_{\text{air}} - M_{\text{water}}}{\rho_{\text{water}}} - (RV + V_{GI})}$$
      </div>
      <p>From measured body density ($D_b$ in $\text{g/cm}^3$), body fat percentage ($\%BF$) is converted via either the <strong>Siri Equation</strong> or the <strong>Brožek Equation</strong>:</p>
      <div class="math-block">
        $$\%BF_{\text{Siri}} = \left( \frac{4.95}{D_b} - 4.50 \right) \times 100\%$$
        $$\%BF_{\text{Bro\v{z}ek}} = \left( \frac{4.57}{D_b} - 4.142 \right) \times 100\%$$
      </div>

      <h3>The U.S. Navy Circumference Derivation & Empirical Logarithmic Models</h3>
      <p>Because underwater weighing tanks and Dual-Energy X-ray Absorptiometry (DEXA) suites are impractical for field military testing, the Naval Health Research Center developed empirical circumference-based logarithmic models correlated against helium dilution and hydrostatic standards ($r > 0.90$):</p>
      <ul>
        <li><strong>Male Formula (Metric):</strong></li>
        $$\%BF_{\text{male}} = 495 / \left( 1.0324 - 0.19077 \log_{10}(\text{waist} - \text{neck}) + 0.15456 \log_{10}(\text{height}) \right) - 450$$
        <li><strong>Female Formula (Metric):</strong></li>
        $$\%BF_{\text{female}} = 495 / \left( 1.29579 - 0.35004 \log_{10}(\text{waist} + \text{hip} - \text{neck}) + 0.22100 \log_{10}(\text{height}) \right) - 450$$
      </ul>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Classification</th>
            <th>Men (% Body Fat)</th>
            <th>Women (% Body Fat)</th>
            <th>Health & Metabolic Implications</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Essential Fat</strong></td>
            <td>$2\% - 5\%$</td>
            <td>$10\% - 13\%$</td>
            <td>Minimum for neural myelination, organ cushioning, hormonal homeostasis</td>
          </tr>
          <tr>
            <td><strong>Athletes</strong></td>
            <td>$6\% - 13\%$</td>
            <td>$14\% - 20\%$</td>
            <td>Peak power-to-weight ratio; optimal for distance running and gymnastics</td>
          </tr>
          <tr>
            <td><strong>Fitness Standard</strong></td>
            <td>$14\% - 17\%$</td>
            <td>$21\% - 24\%$</td>
            <td>Sustained metabolic health, balanced leptin/adiponectin signalling</td>
          </tr>
          <tr>
            <td><strong>Acceptable Average</strong></td>
            <td>$18\% - 24\%$</td>
            <td>$25\% - 31\%$</td>
            <td>Standard population range; low chronic cardiometabolic risk</td>
          </tr>
          <tr>
            <td><strong>Elevated / Obese</strong></td>
            <td>$25\%+$</td>
            <td>$32\%+$</td>
            <td>Increased risk of visceral adiposity, hepatic steatosis, and insulin resistance</td>
          </tr>
        </tbody>
      </table>
""",

    "cable-sizing-calculator.html": """
      <h2>Thermodynamic & Electromagnetic Principles of Conductor Sizing</h2>
      <p>The sizing of low-voltage and medium-voltage electrical power conductors is governed by rigorous thermodynamic equilibrium equations defined in <strong>IEC 60364-5-52</strong> and <strong>NFPA 70 (National Electrical Code Article 310)</strong>. Current flowing through a conductor with internal ohmic resistance $R_{ac}$ generates Joule heat at a volumetric rate of $P = I^2 R_{ac}$. This thermal energy must dissipate through the insulation dielectric, outer jacket sheath, conduit, and surrounding ambient air or soil without exceeding the continuous thermal rating of the insulation material ($70^\circ\text{C}$ for PVC, $90^\circ\text{C}$ for XLPE/EPR).</p>

      <h3>Compound Derating Factor Formulation</h3>
      <p>Tabulated cable ampacity ($I_0$) values published in standards assume idealized laboratory installation baselines (typically $30^\circ\text{C}$ ambient air temperature and isolated single circuits). In practical engineering installations, the permissible continuous current-carrying capacity ($I_z$) must be adjusted via multiplicative environmental derating factors:</p>
      <div class="math-block">
        $$I_z = I_0 \times C_a \times C_g \times C_d \times C_i$$
      </div>
      <p>Where:</p>
      <ul>
        <li>$C_a$ = Ambient temperature correction factor ($C_a = \sqrt{\frac{T_{max} - T_{ambient}}{T_{max} - T_{base}}}$).</li>
        <li>$C_g$ = Grouping proximity factor accounting for mutual heating across bunched or touching cables on trays or conduits.</li>
        <li>$C_d$ = Thermal soil resistivity factor for direct-buried conductors ($\text{K}\cdot\text{m/W}$).</li>
        <li>$C_i$ = Thermal insulation derating factor when conductors pass through building thermal insulation batting.</li>
      </ul>

      <h3>Adiabatic Fault Withstand Capacity Equation</h3>
      <p>Under prospective short-circuit fault conditions, circuit protection breakers take finite time ($t$, typically $20\text{ to } 100\text{ ms}$) to clear. During this fault clearance interval, thermal dissipation into the environment is assumed to be zero (adiabatic thermodynamic process). The minimum conductor cross-sectional area $S$ ($\text{mm}^2$) capable of surviving fault current $I_{sc}$ without melting insulation is calculated via the IEC 60364-5-54 adiabatic equation:</p>
      <div class="math-block">
        $$S \ge \frac{\sqrt{I_{sc}^2 \cdot t}}{k}$$
      </div>
      <p>Where $k$ is the material-insulation thermal withstand constant ($k = 115\text{ A}\cdot\text{s}^{1/2}/\text{mm}^2$ for copper with PVC insulation; $k = 143\text{ A}\cdot\text{s}^{1/2}/\text{mm}^2$ for copper with XLPE insulation; $k = 94\text{ A}\cdot\text{s}^{1/2}/\text{mm}^2$ for aluminum with XLPE insulation).</p>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Conductor Size (mm²)</th>
            <th>Copper XLPE Ampacity (Method E Tray)</th>
            <th>Copper PVC Ampacity (Method E Tray)</th>
            <th>Max Fault Current 0.1s (XLPE k=143)</th>
            <th>AC Resistance at 90°C (Ω/km)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>2.5 mm²</strong></td>
            <td>33 A</td>
            <td>24 A</td>
            <td>1.13 kA</td>
            <td>8.87</td>
          </tr>
          <tr>
            <td><strong>6.0 mm²</strong></td>
            <td>54 A</td>
            <td>41 A</td>
            <td>2.71 kA</td>
            <td>3.69</td>
          </tr>
          <tr>
            <td><strong>16.0 mm²</strong></td>
            <td>110 A</td>
            <td>84 A</td>
            <td>7.23 kA</td>
            <td>1.38</td>
          </tr>
          <tr>
            <td><strong>35.0 mm²</strong></td>
            <td>182 A</td>
            <td>141 A</td>
            <td>15.82 kA</td>
            <td>0.627</td>
          </tr>
          <tr>
            <td><strong>70.0 mm²</strong></td>
            <td>298 A</td>
            <td>233 A</td>
            <td>31.65 kA</td>
            <td>0.313</td>
          </tr>
          <tr>
            <td><strong>120.0 mm²</strong></td>
            <td>415 A</td>
            <td>328 A</td>
            <td>54.26 kA</td>
            <td>0.182</td>
          </tr>
        </tbody>
      </table>
""",

    "calorie-calculator.html": """
      <h2>The Thermodynamics of Human Bioenergetics</h2>
      <p>Human energy expenditure obeys the First Law of Thermodynamics: energy cannot be created or destroyed, only transformed. When dietary caloric intake ($E_{\text{in}}$) deviates from cumulative energy expenditure ($E_{\text{out}}$), the body establishes an energy balance state governed by the thermodynamic equation of macronutrient oxidation:</p>
      <div class="math-block">
        $$\Delta \text{Body Energy Stores} = E_{\text{in}} - E_{\text{out}} = E_{\text{in}} - (\text{BMR} + \text{TEF} + \text{NEAT} + \text{EAT})$$
      </div>

      <h3>Decomposition of Total Daily Energy Expenditure (TDEE)</h3>
      <p>Total daily metabolic consumption partitions into four distinct physiological compartments:</p>
      <ul>
        <li><strong>Basal Metabolic Rate (BMR, 60%–75% of TDEE):</strong> The minimal rate of energy turnover required to sustain vegetative cellular function in a post-absorptive thermoneutral state (hepatic protein synthesis, cardiac pumping, renal filtration, sodium-potassium ATPase pump action).</li>
        <li><strong>Thermic Effect of Food (TEF, 8%–12% of TDEE):</strong> The obligatory metabolic cost of digesting, absorbing, transporting, and storing dietary macronutrients. Protein exhibits the highest thermic cost ($20\% - 30\%$ of consumed energy), carbohydrates require $5\% - 10\%$, and dietary lipids require only $0\% - 3\%$.</li>
        <li><strong>Non-Exercise Activity Thermogenesis (NEAT, 15%–30% of TDEE):</strong> Spontaneous physical movement, occupational walking, fidgeting, and postural stabilization. NEAT represents the single most variable adaptive component across human populations.</li>
        <li><strong>Exercise Activity Thermogenesis (EAT, 5%–15% of TDEE):</strong> Intentional athletic training, resistance exercise, and structured cardiovascular sessions.</li>
      </ul>

      <h3>Empirical Predictive Equations: Mifflin-St Jeor vs Katch-McArdle</h3>
      <p>In clinical dietetics, two validated predictive models dominate predictive resting metabolic rate calculations:</p>
      <div class="math-block">
        $$\text{Mifflin-St Jeor (Men): } BMR = 10 \cdot W(\text{kg}) + 6.25 \cdot H(\text{cm}) - 5 \cdot A(\text{yrs}) + 5$$
        $$\text{Mifflin-St Jeor (Women): } BMR = 10 \cdot W(\text{kg}) + 6.25 \cdot H(\text{cm}) - 5 \cdot A(\text{yrs}) - 161$$
      </div>
      <p>When body fat percentage is known, the <strong>Katch-McArdle Formula</strong> eliminates stature and age biases by evaluating lean body mass ($LBM$) directly:</p>
      <div class="math-block">
        $$BMR_{\text{Katch-McArdle}} = 370 + (21.6 \times LBM_{\text{kg}})$$
      </div>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Activity Multiplier (PAL)</th>
            <th>Daily Behavioral Profile</th>
            <th>Weekly Exercise Volume</th>
            <th>Target Caloric Range (75 kg Adult)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Sedentary ($1.20$)</strong></td>
            <td>Desk workstation, driving, minimal walking</td>
            <td>< 30 minutes light movement/wk</td>
            <td>$2{,}000 - 2{,}150\text{ kcal/day}$</td>
          </tr>
          <tr>
            <td><strong>Lightly Active ($1.375$)</strong></td>
            <td>Retail, teaching, domestic active chores</td>
            <td>1 to 3 sessions light cardio/lifting</td>
            <td>$2{,}300 - 2{,}450\text{ kcal/day}$</td>
          </tr>
          <tr>
            <td><strong>Moderately Active ($1.55$)</strong></td>
            <td>Moderate physical work, standing occupation</td>
            <td>3 to 5 structured intense training bouts</td>
            <td>$2{,}600 - 2{,}750\text{ kcal/day}$</td>
          </tr>
          <tr>
            <td><strong>Very Active ($1.725$)</strong></td>
            <td>Construction, manual labor, athletic squad</td>
            <td>6 to 7 demanding endurance/sport sessions</td>
            <td>$2{,}900 - 3{,}100\text{ kcal/day}$</td>
          </tr>
          <tr>
            <td><strong>Extremely Active ($1.90$)</strong></td>
            <td>Elite endurance athlete, military field training</td>
            <td>Twice-daily training or heavy physical labor</td>
            <td>$3{,}200 - 3{,}500+\text{ kcal/day}$</td>
          </tr>
        </tbody>
      </table>
""",

    "chemical-dosing-calculator.html": """
      <h2>Principles of Stoichiometric Chemical Feed & Dosing Engineering</h2>
      <p>In municipal water treatment, industrial effluent neutralization, and cooling tower biocidal maintenance, chemical metering pumps inject coagulants, oxidants, and pH buffers at precise volumetric delivery rates. Accurate metering prevents either treatment failure (turbidity breakthrough, pathogen survival) or hazardous over-dosing (trihalomethane disinfection byproduct formation, chemical wasting).</p>

      <h3>Continuous Active Chemical Feed Rate Formulation</h3>
      <p>The universal mass-balance equation linking target chemical dosage ($D$ in $\text{mg/L}$ or $\text{ppm}$) to continuous volumetric plant process flow ($Q$) is derived from mass conservation:</p>
      <div class="math-block">
        $$\dot{m}_{\text{pure}} = Q \times D \times 10^{-3}\text{ kg/m}^3$$
        $$\text{Feed Rate (L/hr)} = \frac{Q(\text{m}^3/\text{hr}) \times D(\text{mg/L}) \times 1000}{C_{\%}\times \rho_{\text{chem}}(\text{g/cm}^3) \times 10{,}000} = \frac{Q \times D}{C_{\%} \times \rho_{\text{chem}} \times 10}$$
      </div>
      <p>Where:</p>
      <ul>
        <li>$Q$ = Volumetric raw fluid process flow rate ($\text{m}^3/\text{hr}$ or $\text{L/min}$).</li>
        <li>$D$ = Target analytical dosage in parts per million ($\text{mg/L}$).</li>
        <li>$C_{\%}$ = Active chemical purity percentage by weight ($\%\text{ w/w}$, e.g. $12.5\%$ for commercial sodium hypochlorite bleach, $40\%$ for ferric chloride).</li>
        <li>$\rho_{\text{chem}}$ = Specific gravity or liquid density of the chemical solution ($\text{kg/L}$ or $\text{g/mL}$).</li>
      </ul>

      <h3>Coagulation Chemistry: Alum vs Ferric Metal Salts</h3>
      <p>Primary chemical coagulation neutralizes negative zeta potentials on colloidal clay, silt, and humic acid particles. When aluminum sulfate ($\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O}$) dissolves in water, it consumes natural bicarbonate alkalinity according to the stoichiometric reaction:</p>
      <div class="math-block">
        $$\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O} + 3\text{Ca}(\text{HCO}_3)_2 \longrightarrow 2\text{Al}(\text{OH})_3\downarrow + 3\text{CaSO}_4 + 6\text{CO}_2 + 14\text{H}_2\text{O}$$
      </div>
      <p>Every $1.0\text{ mg/L}$ of commercial alum added to water consumes approximately $0.50\text{ mg/L}$ of natural alkalinity expressed as $\text{CaCO}_3$. If baseline water alkalinity drops below $30\text{ mg/L}$, supplemental hydrated lime ($\text{Ca}(\text{OH})_2$) or soda ash ($\text{Na}_2\text{CO}_3$) dosing must be metered concurrently to maintain optimum coagulation pH ($6.2 - 6.8$).</p>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Chemical Reagent</th>
            <th>Primary Water Treatment Purpose</th>
            <th>Standard Solution Purity</th>
            <th>Solution Density (kg/L)</th>
            <th>Stoichiometric Alkalinity Impact</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Sodium Hypochlorite ($\text{NaOCl}$)</strong></td>
            <td>Primary disinfection, bio-oxidation</td>
            <td>$12.5\%\text{ w/w}$</td>
            <td>1.20 kg/L</td>
            <td>Slightly basic; increases alkalinity</td>
          </tr>
          <tr>
            <td><strong>Aluminum Sulfate (Alum)</strong></td>
            <td>Colloidal destabilization, coagulation</td>
            <td>$48.5\%\text{ liquid}$</td>
            <td>1.32 kg/L</td>
            <td>Consumes $0.50\text{ mg/L CaCO}_3$ per mg Alum</td>
          </tr>
          <tr>
            <td><strong>Ferric Chloride ($\text{FeCl}_3$)</strong></td>
            <td>Coagulation, phosphorus precipitation</td>
            <td>$40.0\%\text{ liquid}$</td>
            <td>1.43 kg/L</td>
            <td>Consumes $0.92\text{ mg/L CaCO}_3$ per mg $\text{FeCl}_3$</td>
          </tr>
          <tr>
            <td><strong>Sodium Hydroxide ($\text{NaOH}$)</strong></td>
            <td>pH elevation, corrosion control</td>
            <td>$50.0\%\text{ caustic}$</td>
            <td>1.52 kg/L</td>
            <td>Adds $1.25\text{ mg/L CaCO}_3$ per mg NaOH</td>
          </tr>
          <tr>
            <td><strong>Sulfuric Acid ($\text{H}_2\text{SO}_4$)</strong></td>
            <td>pH depression, scaling prevention</td>
            <td>$93.0\%\text{ commercial}$</td>
            <td>1.83 kg/L</td>
            <td>Consumes $1.02\text{ mg/L CaCO}_3$ per mg $\text{H}_2\text{SO}_4$</td>
          </tr>
        </tbody>
      </table>
""",

    "compound-interest-calculator.html": """
      <h2>Mathematical Derivations of Compound Capital Growth</h2>
      <p>Compound interest represents the process wherein accumulated financial yields earn additional returns over progressive temporal intervals. Unlike linear simple interest ($I = P \cdot r \cdot t$), compounding creates an exponential growth trajectory. For a principal sum $P$ invested at nominal annual rate $r$ compounded $n$ times per year over duration $t$ years, the terminal future balance $A(t)$ evaluates as:</p>
      <div class="math-block">
        $$A(t) = P \left( 1 + \frac{r}{n} \right)^{nt}$$
      </div>

      <h3>Continuous Compounding & Euler's Constant Limits</h3>
      <p>As compounding frequency approaches infinity ($n \to \infty$, where interest accrues continuously at every infinitesimal microsecond), the discrete binomial limit converges onto Euler's transcendental base $e \approx 2.7182818$:</p>
      <div class="math-block">
        $$\lim_{n \to \infty} P \left( 1 + \frac{r}{n} \right)^{nt} = P \cdot \lim_{n \to \infty} \left[ \left( 1 + \frac{1}{n/r} \right)^{n/r} \right]^{rt} = P \cdot e^{rt}$$
      </div>
      <p>This formulation underpins continuous discount bond pricing, Black-Scholes financial options equations, and natural demographic population kinetics.</p>

      <h3>Effective Annual Rate (EAR) vs Annual Percentage Rate (APR)</h3>
      <p>Lenders and retail banking platforms frequently advertise nominal Annual Percentage Rates (APR), which omit compounding dynamics. The true annualized economic yield or cost of capital is quantified by the <strong>Effective Annual Rate (EAR)</strong>, also termed Annual Percentage Yield (APY):</p>
      <div class="math-block">
        $$\text{EAR} = \left( 1 + \frac{r}{n} \right)^n - 1$$
      </div>
      <p>For example, a credit card facility charging a nominal $24.0\%$ APR compounded daily ($n = 365$) yields an effective annual borrowing burden of $\text{EAR} = (1 + 0.24/365)^{365} - 1 = 27.11\%$, representing an extra $311\text{ basis points}$ of real annual borrowing cost.</p>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Nominal APR ($r$)</th>
            <th>Monthly Compounding ($n=12$) EAR</th>
            <th>Daily Compounding ($n=365$) EAR</th>
            <th>Rule of 72 Doubling Time</th>
            <th>Continuous Compounding EAR</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>4.0%</strong></td>
            <td>4.074%</td>
            <td>4.081%</td>
            <td>18.0 Years</td>
            <td>4.081%</td>
          </tr>
          <tr>
            <td><strong>7.0%</strong></td>
            <td>7.229%</td>
            <td>7.250%</td>
            <td>10.3 Years</td>
            <td>7.251%</td>
          </tr>
          <tr>
            <td><strong>10.0%</strong></td>
            <td>10.471%</td>
            <td>10.516%</td>
            <td>7.2 Years</td>
            <td>10.517%</td>
          </tr>
          <tr>
            <td><strong>15.0%</strong></td>
            <td>16.075%</td>
            <td>16.180%</td>
            <td>4.8 Years</td>
            <td>16.183%</td>
          </tr>
          <tr>
            <td><strong>20.0%</strong></td>
            <td>21.939%</td>
            <td>22.134%</td>
            <td>3.6 Years</td>
            <td>22.140%</td>
          </tr>
        </tbody>
      </table>
""",

    "concrete-calculator.html": """
      <h2>Constituent Materials & Volumetric Proportioning in Concrete Engineering</h2>
      <p>Hydraulic cement concrete is an artificial composite rock produced by the exothermic hydration reaction between Portland cement, supplemental cementitious materials (slag, fly ash, silica fume), potable water, and graded aggregates. Under the <strong>American Concrete Institute (ACI 211.1) Standard Practice for Selecting Proportions for Normal, Heavyweight, and Mass Concrete</strong>, structural concrete mix designs are formulated on absolute solid volume conservation:</p>
      <div class="math-block">
        $$V_{\text{concrete}} = V_{\text{water}} + V_{\text{cement}} + V_{\text{fine agg}} + V_{\text{coarse agg}} + V_{\text{entrapped air}} = 1.0\text{ m}^3\text{ (or } 27\text{ ft}^3\text{)}$$
      </div>

      <h3>Abrams' Law: The Water-Cementitious Ratio ($w/cm$)</h3>
      <p>In 1918, Duff Abrams discovered that the 28-day compressive strength ($f'_c$) of fully compacted concrete depends principally on the ratio of water to cementitious mass by weight ($w/cm$), independent of aggregate quantities:</p>
      <div class="math-block">
        $$f'_c = \frac{A}{B^{1.5 \cdot (w/cm)}}$$
      </div>
      <p>Lowering the water-cement ratio from $0.65$ to $0.40$ reduces capillary pore porosity in the hydrated calcium-silicate-hydrate ($\text{C-S-H}$) gel matrix, boosting compressive resistance from $20\text{ MPa}$ ($3{,}000\text{ psi}$) to over $45\text{ MPa}$ ($6{,}500\text{ psi}$), while substantially inhibiting chloride ion penetration and freeze-thaw spalling.</p>

      <h3>Field Waste Factors & Subgrade Excavation Bulking</h3>
      <p>When pouring concrete slabs, footings, and grade beams, ordering the theoretical mathematical geometric volume ($L \times W \times H$) leads to short-loads due to subgrade undulations, formwork deflection, and pumping wastage. Standard civil engineering practice applies contingency factors:</p>
      <ul>
        <li><strong>Formed Walls & Columns:</strong> Add $5\%$ over theoretical geometry.</li>
        <li><strong>Suspended Decks & Elevated Beams:</strong> Add $5\% - 7\%$ for deflection allowances.</li>
        <li><strong>Slabs-on-Grade (Over Compacted Gravel):</strong> Add $8\% - 10\%$ for subgrade grade variations.</li>
        <li><strong>Continuous Trench Footings (Poured against Earth):</strong> Add $10\% - 15\%$ for irregular earthen trench walls.</li>
      </ul>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Target Compressive Strength ($f'_c$)</th>
            <th>Max Water-Cement Ratio ($w/cm$)</th>
            <th>Standard Volumetric Mix (Cement:Sand:Stone)</th>
            <th>Typical Civil Application</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>15 MPa (2,200 psi)</strong></td>
            <td>0.65</td>
            <td>1 : 3 : 5</td>
            <td>Mass concrete mud-slabs, fence post footings, unreinforced bedding</td>
          </tr>
          <tr>
            <td><strong>20 MPa (3,000 psi)</strong></td>
            <td>0.55</td>
            <td>1 : 2 : 4</td>
            <td>Residential footings, garage slabs, sidewalks, driveways</td>
          </tr>
          <tr>
            <td><strong>25 MPa (3,600 psi)</strong></td>
            <td>0.50</td>
            <td>1 : 1.5 : 3</td>
            <td>Commercial grade slabs-on-grade, foundation retaining walls</td>
          </tr>
          <tr>
            <td><strong>30 MPa (4,350 psi)</strong></td>
            <td>0.45</td>
            <td>1 : 1.25 : 2.5</td>
            <td>Structural columns, elevated suspended decks, precast lintels</td>
          </tr>
          <tr>
            <td><strong>35+ MPa (5,000+ psi)</strong></td>
            <td>0.40</td>
            <td>Engineered Mix Design</td>
            <td>Pre-stressed bridge girders, marine structures, seismic moment frames</td>
          </tr>
        </tbody>
      </table>
""",

    "cooling-load-calculator.html": """
      <h2>Thermodynamic Fundamentals of HVAC Space Heat Balance</h2>
      <p>HVAC space cooling load calculations govern the mechanical capacity sizing of chillers, direct-expansion (DX) coils, and air handling fans. Unlike instantaneous heat gain, a building's cooling load represents the rate at which heat must be extracted from the indoor atmosphere to maintain a stable dry-bulb temperature and relative humidity. Heat transfer occurs across exterior building envelopes via conduction, solar radiation, infiltration, and internal equipment dissipation, governed by <strong>ASHRAE Fundamentals Heat Balance (HB)</strong> and <strong>Radiant Time Series (RTS)</strong> methodologies.</p>

      <h3>Sensible vs Latent Heat Extraction Components</h3>
      <p>Total mechanical cooling demand partitions into sensible and latent thermal vectors:</p>
      <div class="math-block">
        $$\dot{Q}_{\text{total}} = \dot{Q}_{\text{sensible}} + \dot{Q}_{\text{latent}}$$
        $$\dot{Q}_{\text{sensible}} = 1.08 \times CFM \times (T_{\text{return}} - T_{\text{supply}})$$
        $$\dot{Q}_{\text{latent}} = 4840 \times CFM \times (W_{\text{return}} - W_{\text{supply}})$$
      </div>
      <p>Where $CFM$ represents airflow in cubic feet per minute, $T$ denotes dry-bulb temperature in $^\circ\text{F}$, and $W$ denotes humidity ratio in pounds of moisture per pound of dry air ($lb_{\text{water}}/lb_{\text{dry air}}$). The Sensible Heat Ratio ($\text{SHR} = \dot{Q}_s / \dot{Q}_t$) typically ranges from $0.70\text{ to } 0.85$ in commercial buildings.</p>

      <h3>Envelope Fenestration & Conduction Formulations</h3>
      <p>Heat conduction across opaque wall assemblies and roof assemblies is calculated via overall thermal transmittance ($U$-factor) and Cooling Load Temperature Differences (CLTD) accounting for thermal lag and diurnal solar absorption:</p>
      <div class="math-block">
        $$q_{\text{envelope}} = U \times A \times \text{CLTD}_{\text{corrected}}$$
        $$q_{\text{solar}} = A_{\text{glass}} \times \text{SHGC} \times \text{SC} \times I_{\text{solar}}$$
      </div>
      <p>Where $\text{SHGC}$ is the fenestration Solar Heat Gain Coefficient, $\text{SC}$ is internal shading coefficient, and $I_{\text{solar}}$ is directional peak solar irradiance ($\text{Btu/hr}\cdot\text{ft}^2$).</p>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Space Occupancy Category</th>
            <th>Sensible Heat per Person (Btu/hr)</th>
            <th>Latent Moisture Heat (Btu/hr)</th>
            <th>Ventilation Rate (CFM/person)</th>
            <th>Equipment Lighting Allowance (W/ft²)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Private Office / Executive</strong></td>
            <td>245 Btu/hr</td>
            <td>155 Btu/hr</td>
            <td>15 - 20 CFM</td>
            <td>0.65 - 0.85 W/ft²</td>
          </tr>
          <tr>
            <td><strong>Open-Plan Call Center</strong></td>
            <td>250 Btu/hr</td>
            <td>200 Btu/hr</td>
            <td>20 CFM</td>
            <td>1.00 - 1.20 W/ft²</td>
          </tr>
          <tr>
            <td><strong>Restaurant Dining Area</strong></td>
            <td>275 Btu/hr</td>
            <td>275 Btu/hr</td>
            <td>20 - 25 CFM</td>
            <td>1.20 - 1.50 W/ft²</td>
          </tr>
          <tr>
            <td><strong>Gymnasium / Fitness Studio</strong></td>
            <td>580 Btu/hr</td>
            <td>870 Btu/hr</td>
            <td>30 - 40 CFM</td>
            <td>0.80 - 1.00 W/ft²</td>
          </tr>
          <tr>
            <td><strong>Data Center / Server Room</strong></td>
            <td>N/A (Unoccupied)</td>
            <td>0 Btu/hr (No Latent)</td>
            <td>5 CFM (Positive Pressure)</td>
            <td>25.0 - 100.0+ W/ft²</td>
          </tr>
        </tbody>
      </table>
""",

    "date-difference-calculator.html": """
      <h2>Financial Day-Count Conventions & Industrial Project Schedules</h2>
      <p>Quantifying the duration between two dates is fundamental to contract law, commercial paper interest settlement, and Critical Path Method (CPM) project construction management. While calendars appear simple, global finance and engineering apply distinct statutory day-count conventions that alter elapsed durations by up to several business days over annual accounting cycles.</p>

      <h3>Global Fixed-Income Day-Count Methodologies</h3>
      <p>In municipal bond issuance, commercial lending, and Treasury debt settlements, interest accrual uses specific day-count conventions ($\text{Day Count Fraction} = \frac{\text{Days}(D_1, D_2)}{\text{Days in Year}}$):</p>
      <ul>
        <li><strong>Actual/Actual (ICMA / US Treasury):</strong> Counts the exact calendar days between $D_1$ and $D_2$, divided by the exact number of days in the current calendar year (365 or 366 in a leap year).</li>
        <li><strong>30/360 (Bond Basis / US Corporate):</strong> Assumes each complete month possesses exactly 30 days and the calendar year contains exactly 360 days ($\text{Days} = 360(Y_2 - Y_1) + 30(M_2 - M_1) + (D_2 - D_1)$).</li>
        <li><strong>Actual/360 (Money Market / Commercial Paper):</strong> Counts exact days elapsed between start and end dates, but annualizes across a fixed 360-day commercial denominator, slightly boosting real annualized interest yields to lenders.</li>
        <li><strong>Actual/365 Fixed:</strong> Counts exact calendar days divided by a fixed 365-day denominator regardless of leap years (standard in the UK and commonwealth financial systems).</li>
      </ul>

      <h3>ISO 8601 Calendar Week & Workday Scheduling Algorithms</h3>
      <p>Under international standard <strong>ISO 8601</strong>, calendar weeks commence on Monday (Day 1) and conclude on Sunday (Day 7). Week 1 of any Gregorian calendar year is defined as the week containing the first Thursday of that year (equivalent to the week containing January 4th). For industrial project scheduling, Net Working Days ($NWD$) exclude weekend days and statutory gazetted holidays:</p>
      <div class="math-block">
        $$NWD = \text{Total Elapsed Days} - 2 \times \lfloor \text{Weeks} \rfloor - \text{Weekend Boundary Adjustments} - \text{Observed Statutory Holidays}$$
      </div>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Day-Count Convention</th>
            <th>Primary Market Application</th>
            <th>Leap Year Handling</th>
            <th>30-Day Month Assumption</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Actual/Actual</strong></td>
            <td>US Treasury Bonds, Sovereign Gilts, Eurobonds</td>
            <td>Exact 366-day leap year denominator</td>
            <td>No (exact calendar month lengths)</td>
          </tr>
          <tr>
            <td><strong>30/360 Bond Basis</strong></td>
            <td>US Corporate Bonds, Municipal Revenue Bonds</td>
            <td>Ignored (standard 360-day denominator)</td>
            <td>Yes (all months normalized to 30 days)</td>
          </tr>
          <tr>
            <td><strong>Actual/360</strong></td>
            <td>Commercial bank lending, SOFR loans, T-Bills</td>
            <td>Exact numerator, fixed 360 denominator</td>
            <td>No (exact calendar days counted)</td>
          </tr>
          <tr>
            <td><strong>Actual/365 Fixed</strong></td>
            <td>Sterling loans, Australian & Canadian paper</td>
            <td>Fixed 365 denominator even in leap years</td>
            <td>No (exact calendar days counted)</td>
          </tr>
          <tr>
            <td><strong>Business Days (NWD)</strong></td>
            <td>CPM Construction milestones, legal notice periods</td>
            <td>Leap days counted if falling on Mon–Fri</td>
            <td>Excludes non-working weekends and public holidays</td>
          </tr>
        </tbody>
      </table>
""",

    "discount-calculator.html": """
      <h2>Microeconomics of Pricing Mechanics: Margins, Markups, and Elasticity</h2>
      <p>Price promotional discounts represent one of the most critical microeconomic levers in commercial retail and wholesale supply chains. While discounts stimulate sales volume, miscalculating promotional margins rapidly erodes gross operating profitability. A thorough understanding of pricing mathematics requires separating percentage discounts from gross margin and markup percentages.</p>

      <h3>The Fundamental Markup vs Margin Mathematical Duality</h3>
      <p>Commercial merchants and procurement teams frequently conflate markup and gross margin, leading to catastrophic pricing discrepancies:</p>
      <div class="math-block">
        $$\text{Markup \%} = \frac{\text{Selling Price} - \text{Wholesale Cost}}{\text{Wholesale Cost}} \times 100\% = \frac{\text{Gross Profit}}{\text{Cost}} \times 100\%$$
        $$\text{Gross Margin \%} = \frac{\text{Selling Price} - \text{Wholesale Cost}}{\text{Selling Price}} \times 100\% = \frac{\text{Gross Profit}}{\text{Revenue}} \times 100\%$$
      </div>
      <p>For an article acquired at wholesale cost of $\$50$ and retailed at $\$100$, the markup is $\frac{50}{50} = 100\%$, but the gross margin is only $\frac{50}{100} = 50\%$. If a merchant applies an unbudgeted $30\%$ promotional discount to retail price, the discounted price is $\$70$, slashing gross margin from $50\%$ to $\frac{20}{70} = 28.57\%$.</p>

      <h3>Multi-Tier Compounding Trade Discounts</h3>
      <p>In wholesale supply channels (e.g., electrical or plumbing equipment supply), list prices are discounted through multi-stage trade chains known as series discounts (e.g., $30\% / 10\% / 5\%$). These are multiplicative, not additive:</p>
      <div class="math-block">
        $$P_{\text{net}} = P_{\text{list}} \times (1 - d_1) \times (1 - d_2) \times (1 - d_3)$$
      </div>
      <p>A $\$1{,}000$ equipment list price with a $30/10/5$ chain discount does not equal $45\%$ ($d_{total} \ne 45\%$). Instead, $P_{\text{net}} = 1000 \times 0.70 \times 0.90 \times 0.95 = \$598.50$, representing an actual net discount of $40.15\%$.</p>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Initial Gross Margin %</th>
            <th>Promotional Discount %</th>
            <th>Resulting Post-Discount Margin %</th>
            <th>Required Sales Volume Increase to Break Even</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>40.0%</strong></td>
            <td>10.0%</td>
            <td>33.3%</td>
            <td>+33.3% unit sales required</td>
          </tr>
          <tr>
            <td><strong>40.0%</strong></td>
            <td>20.0%</td>
            <td>25.0%</td>
            <td>+100.0% unit sales required</td>
          </tr>
          <tr>
            <td><strong>50.0%</strong></td>
            <td>15.0%</td>
            <td>41.2%</td>
            <td>+42.9% unit sales required</td>
          </tr>
          <tr>
            <td><strong>50.0%</strong></td>
            <td>25.0%</td>
            <td>33.3%</td>
            <td>+100.0% unit sales required</td>
          </tr>
          <tr>
            <td><strong>30.0%</strong></td>
            <td>15.0%</td>
            <td>17.6%</td>
            <td>+100.0% unit sales required</td>
          </tr>
        </tbody>
      </table>
""",

    "ev-charging-time-calculator.html": """
      <h2>Electrochemical & Power Electronics Dynamics of EV Charging</h2>
      <p>Electric vehicle (EV) charging duration is governed by lithium-ion cell electrochemical kinetics and onboard power conversion electronics. Charging time is not a simple linear division of battery pack capacity ($kWh$) by charger power ($kW$). Instead, the charging process follows a Constant-Current / Constant-Voltage (CC/CV) profile managed by the vehicle's Battery Management System (BMS) to avoid thermal runaway and lithium dendrite plating.</p>

      <h3>AC Level 1/2 vs DC Fast Charging (DCFC) Power Architecture</h3>
      <p>Charging infrastructure partitions across two distinct electrical paradigms:</p>
      <ul>
        <li><strong>AC Level 1 & Level 2 Charging:</strong> The vehicle receives alternating current from the electrical grid ($120\text{V}$ single-phase for Level 1, $208\text{V} - 240\text{V}$ split-phase for Level 2). The vehicle's internal <strong>Onboard Charger (OBC)</strong> rectifies AC into DC to charge the traction battery. OBC thermal capacity restricts maximum AC charging rates to between $7.2\text{ kW}$ and $19.2\text{ kW}$ ($32\text{A to } 80\text{A}$).</li>
        <li><strong>DC Fast Charging (DCFC / Level 3):</strong> High-voltage three-phase AC ($480\text{V}$) is rectified externally inside the stationary commercial charging station into high-voltage direct current ($400\text{V} \text{ or } 800\text{V}$). DC power bypasses the vehicle OBC, feeding directly into the battery pack contactors at power outputs from $50\text{ kW}$ to $350+\text{ kW}$.</li>
      </ul>

      <h3>The CC/CV Charging Curve & High State-of-Charge (SoC) Throttling</h3>
      <p>During DC fast charging from $10\%$ to $80\%$ State of Charge (SoC), the BMS operates in <strong>Constant Current (CC)</strong> mode, drawing peak charger power. Once cell potentials reach their upper cutoff threshold (typically $\approx 4.20\text{V}$ per cell, around $80\%$ SoC), the BMS switches into <strong>Constant Voltage (CV)</strong> mode. In CV mode, charging current tapers down exponentially to prevent cell degradation:</p>
      <div class="math-block">
        $$I(t) = I_0 \cdot e^{-t / \tau}$$
      </div>
      <p>Consequently, replenishing an EV battery pack from $80\%$ to $100\%$ SoC often requires as much time as charging from $10\%$ to $80\%$!</p>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Charging Level & Standard</th>
            <th>Supply Voltage & Current</th>
            <th>Peak Power Delivery</th>
            <th>Efficiency Factor ($\eta$)</th>
            <th>Charge Time (60 kWh Pack, 10-80%)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>AC Level 1 (NEMA 5-15)</strong></td>
            <td>120V 1-Phase @ 12A</td>
            <td>1.44 kW</td>
            <td>82% - 85%</td>
            <td>~34.0 Hours</td>
          </tr>
          <tr>
            <td><strong>AC Level 2 (32A Dedicated)</strong></td>
            <td>240V Split-Phase @ 32A</td>
            <td>7.68 kW</td>
            <td>88% - 90%</td>
            <td>~6.1 Hours</td>
          </tr>
          <tr>
            <td><strong>AC Level 2 (48A Hardwired)</strong></td>
            <td>240V Split-Phase @ 48A</td>
            <td>11.52 kW</td>
            <td>90% - 92%</td>
            <td>~4.0 Hours</td>
          </tr>
          <tr>
            <td><strong>DC Fast (50 kW Urban)</strong></td>
            <td>400V DC Direct Bus</td>
            <td>50.0 kW</td>
            <td>92% - 94%</td>
            <td>~52 Minutes</td>
          </tr>
          <tr>
            <td><strong>DC Ultra-Fast (150 kW)</strong></td>
            <td>400V / 800V DC Bus</td>
            <td>150.0 kW</td>
            <td>94% - 96%</td>
            <td>~22 Minutes</td>
          </tr>
          <tr>
            <td><strong>DC Hyper-Charging (350 kW)</strong></td>
            <td>800V Architecture</td>
            <td>350.0 kW</td>
            <td>95% - 97%</td>
            <td>~14 Minutes</td>
          </tr>
        </tbody>
      </table>
""",

    "fraction-calculator.html": """
      <h2>Algebraic Theory of Rational Numbers & Number Fields</h2>
      <p>In modern abstract algebra, a rational number is an element of the field of fractions $\mathbb{Q}$ formed over the integral domain of integers $\mathbb{Z}$. Every rational number is represented as an equivalence class of ordered pairs $(a, b)$ with $a, b \in \mathbb{Z}$ and $b \ne 0$, denoted as $\frac{a}{b}$. Two fractions $\frac{a}{b}$ and $\frac{c}{d}$ represent the identical rational element if and only if they satisfy the cross-multiplication equivalence relation:</p>
      <div class="math-block">
        $$\frac{a}{b} = \frac{c}{d} \iff a \cdot d = b \cdot c$$
      </div>

      <h3>Euclidean Algorithm & Irreducible Canonical Form</h3>
      <p>To reduce any rational fraction $\frac{a}{b}$ to its irreducible canonical representation ($\gcd(a', b') = 1$), the numerator and denominator are divided by their <strong>Greatest Common Divisor (GCD)</strong>, determined via the Euclidean division algorithm:</p>
      <div class="math-block">
        $$a = q_1 b + r_1,\quad b = q_2 r_1 + r_2,\quad \dots,\quad r_{k-1} = q_{k+1} r_k + 0 \implies \gcd(a, b) = r_k$$
        $$\frac{a}{b} = \frac{a / \gcd(a,b)}{b / \gcd(a,b)}$$
      </div>
      <p>The <strong>Least Common Multiple (LCM)</strong> of two denominators, vital for fraction addition and subtraction, is derived via the fundamental identity:</p>
      <div class="math-block">
        $$\text{lcm}(b, d) = \frac{|b \cdot d|}{\gcd(b, d)}$$
      </div>

      <h3>Continued Fraction Approximations of Real Numbers</h3>
      <p>Beyond rational arithmetic, continued fractions provide optimal rational approximations for irrational constants ($\pi, e, \sqrt{2}$). Any real number $x$ can be decomposed into an infinite continued fraction $[a_0; a_1, a_2, \dots]$:</p>
      <div class="math-block">
        $$x = a_0 + \frac{1}{a_1 + \frac{1}{a_2 + \frac{1}{a_3 + \dots}}}$$
      </div>
      <p>For Archimedes' circle constant $\pi \approx 3.14159265$, the first successive continued fraction convergents yield $\frac{3}{1}, \frac{22}{7} \approx 3.142857$, and the famous Chinese Tsu Ch'ung-chih rational approximation $\frac{355}{113} \approx 3.14159292$, accurate to six decimal places!</p>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Operation</th>
            <th>Formal Algebraic Definition</th>
            <th>Computational Example</th>
            <th>Irreducible Canonical Result</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Addition ($+$)</strong></td>
            <td>$\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}$</td>
            <td>$\frac{3}{8} + \frac{5}{12} = \frac{36 + 40}{96} = \frac{76}{96}$</td>
            <td>$\frac{19}{24}$</td>
          </tr>
          <tr>
            <td><strong>Subtraction ($-$)</strong></td>
            <td>$\frac{a}{b} - \frac{c}{d} = \frac{ad - bc}{bd}$</td>
            <td>$\frac{7}{10} - \frac{4}{15} = \frac{105 - 40}{150} = \frac{65}{150}$</td>
            <td>$\frac{13}{30}$</td>
          </tr>
          <tr>
            <td><strong>Multiplication ($\times$)</strong></td>
            <td>$\frac{a}{b} \times \frac{c}{d} = \frac{a \cdot c}{b \cdot d}$</td>
            <td>$\frac{4}{9} \times \frac{15}{16} = \frac{60}{144}$</td>
            <td>$\frac{5}{12}$</td>
          </tr>
          <tr>
            <td><strong>Division ($\div$)</strong></td>
            <td>$\frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \times \frac{d}{c} = \frac{ad}{bc}$</td>
            <td>$\frac{5}{6} \div \frac{10}{21} = \frac{5 \times 21}{6 \times 10} = \frac{105}{60}$</td>
            <td>$\frac{7}{4} = 1\frac{3}{4}$</td>
          </tr>
        </tbody>
      </table>
""",

    "gpa-calculator.html": """
      <h2>Statistical Mechanics of Academic Grade Point Averaging</h2>
      <p>Grade Point Average (GPA) represents a credit-weighted quantitative summary of an individual's academic scholarship across secondary and tertiary educational institutions. Rather than taking a simple arithmetic mean of letter grades, collegiate accreditation standards mandate computing a credit-hour weighted average that reflects the curricular rigor and instructional duration of each course module.</p>

      <h3>Credit-Hour Weighted Arithmetic Mean Formulation</h3>
      <p>For an academic transcript consisting of $k$ distinct courses, where course $i$ carries credit weight $C_i$ and numerical grade honor points $GP_i$, Cumulative GPA is calculated as:</p>
      <div class="math-block">
        $$\text{GPA} = \frac{\sum_{i=1}^{k} (C_i \times GP_i)}{\sum_{i=1}^{k} C_i} = \frac{\text{Total Honor Points Earned}}{\text{Total Credit Hours Attempted}}$$
      </div>
      <p>Courses graded on a Pass/Fail (P/F), Satisfactory/Unsatisfactory (S/U), or Audit (AU) basis earn credit toward degree completion but are strictly excluded from both the numerator and denominator of the GPA equation.</p>

      <h3>Unweighted 4.0 Scale vs Weighted 5.0 AP / IB Honors Scales</h3>
      <p>In North American secondary education, two distinct GPA reporting scales coexist:</p>
      <ul>
        <li><strong>Standard Unweighted 4.0 Scale:</strong> Every course is evaluated on a uniform scale where an 'A' grade earns $4.00$ grade points, regardless of whether the course is introductory or college-level.</li>
        <li><strong>Weighted 5.0 / 6.0 Honors Scale:</strong> Recognizes academic challenge by adding premium weight points:
          <ul>
            <li>Honors / Dual-Enrollment Courses: $+0.50$ bump (Grade 'A' = $4.50$).</li>
            <li>Advanced Placement (AP) / International Baccalaureate (IB) Higher Level: $+1.00$ bump (Grade 'A' = $5.00$).</li>
          </ul>
        </li>
      </ul>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Letter Grade</th>
            <th>Standard Percentage Range</th>
            <th>Unweighted 4.0 Scale</th>
            <th>Weighted AP / IB Scale</th>
            <th>Latin Honors & Academic Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>A+ / A</strong></td>
            <td>93% – 100%</td>
            <td>4.00</td>
            <td>5.00</td>
            <td>Summa Cum Laude eligible (Top 5% of class)</td>
          </tr>
          <tr>
            <td><strong>A-</strong></td>
            <td>90% – 92%</td>
            <td>3.70</td>
            <td>4.70</td>
            <td>Magna Cum Laude tier; Dean's High Honors</td>
          </tr>
          <tr>
            <td><strong>B+</strong></td>
            <td>87% – 89%</td>
            <td>3.30</td>
            <td>4.30</td>
            <td>Cum Laude range; graduate school competitive</td>
          </tr>
          <tr>
            <td><strong>B</strong></td>
            <td>83% – 86%</td>
            <td>3.00</td>
            <td>4.00</td>
            <td>Solid academic standing; graduate admissions threshold</td>
          </tr>
          <tr>
            <td><strong>B-</strong></td>
            <td>80% – 82%</td>
            <td>2.70</td>
            <td>3.70</td>
            <td>Standard satisfactory performance baseline</td>
          </tr>
          <tr>
            <td><strong>C+ / C</strong></td>
            <td>73% – 79%</td>
            <td>2.00 – 2.30</td>
            <td>3.00 – 3.30</td>
            <td>Minimum grade to satisfy core major prerequisite requirements</td>
          </tr>
          <tr>
            <td><strong>D</strong></td>
            <td>60% – 69%</td>
            <td>1.00</td>
            <td>2.00</td>
            <td>Marginal credit; triggers academic probation if cumulative < 2.0</td>
          </tr>
          <tr>
            <td><strong>F</strong></td>
            <td>< 60%</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>Course failure; zero honor points, full credit burden retained</td>
          </tr>
        </tbody>
      </table>
""",

    "ideal-weight-calculator.html": """
      <h2>Comparative Analysis of Clinical Ideal Body Weight (IBW) Formulations</h2>
      <p>In pharmacokinetics, clinical nutrition, and mechanical ventilation medicine, calculating Ideal Body Weight (IBW) is critical for determining appropriate therapeutic drug dosages (aminoglycosides, chemotherapy, anesthetics) and tidal volume ventilator settings ($6 - 8\text{ mL/kg IBW}$). Dosing hydrophobic drugs based on actual total body weight in individuals with obesity results in lethal overdoses, whereas using lean body mass or IBW ensures therapeutic plasma concentrations.</p>

      <h3>The Classic Anthropometric Formulas: Devine, Robinson, Miller, Hamwi</h3>
      <p>Over the past 60 years, clinical researchers developed multiple empirical regressions linking adult height ($H$ in inches over 5 feet / 60 inches) to target medical body mass ($W$ in kilograms):</p>
      <ul>
        <li><strong>Devine Formula (1974 - Clinical Standard):</strong></li>
        $$\text{Men: } IBW_{\text{Devine}} = 50.0\text{ kg} + 2.3 \times (H - 60)$$
        $$\text{Women: } IBW_{\text{Devine}} = 45.5\text{ kg} + 2.3 \times (H - 60)$$
        <li><strong>Robinson Formula (1983 Modification):</strong></li>
        $$\text{Men: } IBW_{\text{Robinson}} = 52.0\text{ kg} + 1.9 \times (H - 60)$$
        $$\text{Women: } IBW_{\text{Robinson}} = 49.0\text{ kg} + 1.7 \times (H - 60)$$
        <li><strong>Miller Formula (1983):</strong></li>
        $$\text{Men: } IBW_{\text{Miller}} = 56.2\text{ kg} + 1.41 \times (H - 60)$$
        $$\text{Women: } IBW_{\text{Miller}} = 53.1\text{ kg} + 1.36 \times (H - 60)$$
        <li><strong>Hamwi Formula (1964 Diabetic Guideline):</strong></li>
        $$\text{Men: } IBW_{\text{Hamwi}} = 48.0\text{ kg} + 2.7 \times (H - 60)$$
        $$\text{Women: } IBW_{\text{Hamwi}} = 45.5\text{ kg} + 2.2 \times (H - 60)$$
      </ul>

      <h3>Adjusted Body Weight (AdjBW) for Clinical Pharmacokinetics</h3>
      <p>When actual total body weight ($TBW$) exceeds $120\%$ of calculated IBW, adipose tissue contributes partially to drug distribution. Clinical pharmacists employ the <strong>Adjusted Body Weight (AdjBW)</strong> formula with an empiric correction factor ($\alpha = 0.40$ for aminoglycosides):</p>
      <div class="math-block">
        $$\text{AdjBW} = IBW + 0.40 \times (TBW - IBW)$$
      </div>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Stature (Height)</th>
            <th>Devine IBW (Men)</th>
            <th>Devine IBW (Women)</th>
            <th>WHO Normal BMI Range (18.5–24.9)</th>
            <th>Mechanical Vent Tidal Volume (6 mL/kg)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>5' 4" (163 cm)</strong></td>
            <td>59.2 kg (130.5 lb)</td>
            <td>54.7 kg (120.6 lb)</td>
            <td>49.2 – 66.2 kg</td>
            <td>355 mL</td>
          </tr>
          <tr>
            <td><strong>5' 7" (170 cm)</strong></td>
            <td>66.1 kg (145.7 lb)</td>
            <td>61.6 kg (135.8 lb)</td>
            <td>53.5 – 72.0 kg</td>
            <td>396 mL</td>
          </tr>
          <tr>
            <td><strong>5' 10" (178 cm)</strong></td>
            <td>73.0 kg (160.9 lb)</td>
            <td>68.5 kg (151.0 lb)</td>
            <td>58.6 – 78.9 kg</td>
            <td>438 mL</td>
          </tr>
          <tr>
            <td><strong>6' 0" (183 cm)</strong></td>
            <td>77.6 kg (171.1 lb)</td>
            <td>73.1 kg (161.2 lb)</td>
            <td>62.0 – 83.4 kg</td>
            <td>466 mL</td>
          </tr>
          <tr>
            <td><strong>6' 3" (190 cm)</strong></td>
            <td>84.5 kg (186.3 lb)</td>
            <td>80.0 kg (176.4 lb)</td>
            <td>66.8 – 89.9 kg</td>
            <td>507 mL</td>
          </tr>
        </tbody>
      </table>
""",

    "loan-emi-calculator.html": """
      <h2>Actuarial Mathematics of Amortized Loan Repayments</h2>
      <p>An Equated Monthly Installment (EMI) is a fixed cash outflow paid by a borrower to a financial lender at specified calendar intervals over an agreed amortization tenure. Each installment decomposes mathematically into two concurrent streams: an interest charge on the outstanding principal balance and a capital repayment component that progressively extinguishes the debt obligation.</p>

      <h3>Derivation of the Ordinary Annuity Present Value Equation</h3>
      <p>The mathematical proof of the EMI formula stems from the present value of an ordinary annuity. The initial borrowed principal $P$ must equal the sum of all future monthly cash installments $E$, discounted back to present value at the per-period periodic interest rate $r = \frac{R}{12 \times 100}$ over $N$ total repayment months:</p>
      <div class="math-block">
        $$P = \sum_{t=1}^{N} \frac{E}{(1 + r)^t} = E \left[ \frac{1 - (1 + r)^{-N}}{r} \right]$$
      </div>
      <p>Solving algebraically for the monthly installment payment $E$ yields the universal loan amortization equation:</p>
      <div class="math-block">
        $$E = P \cdot r \cdot \frac{(1 + r)^N}{(1 + r)^N - 1}$$
      </div>

      <h3>Amortization Dynamics & The Interest-Principal Inflection Point</h3>
      <p>During the opening stages of a long-term loan (e.g., a 30-year home mortgage), the outstanding principal balance is near its peak, causing monthly interest charges to consume up to $70\% - 85\%$ of each installment payment. As the principal is gradually amortized down, the interest charge shrinks monotonically, allowing an increasing fraction of the payment to pay down principal:</p>
      <div class="math-block">
        $$\text{Interest Component in Month } t: I_t = P_{t-1} \times r$$
        $$\text{Principal Component in Month } t: \Delta P_t = E - I_t$$
      </div>
      <p>The <strong>Inflection Crossover Point</strong>—the exact month where principal repayment surpasses the interest charge—typically does not occur until year 12 to 16 of a standard 30-year amortization schedule!</p>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Loan Term (Years)</th>
            <th>Nominal Interest Rate</th>
            <th>Monthly EMI per $100,000 Borrowed</th>
            <th>Total Interest Paid over Life of Loan</th>
            <th>Total Repayment Ratio (Total / Principal)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>15 Years</strong></td>
            <td>5.50%</td>
            <td>$817.08</td>
            <td>$47,075</td>
            <td>1.47×</td>
          </tr>
          <tr>
            <td><strong>15 Years</strong></td>
            <td>7.00%</td>
            <td>$898.83</td>
            <td>$61,789</td>
            <td>1.62×</td>
          </tr>
          <tr>
            <td><strong>20 Years</strong></td>
            <td>6.50%</td>
            <td>$745.57</td>
            <td>$78,938</td>
            <td>1.79×</td>
          </tr>
          <tr>
            <td><strong>30 Years</strong></td>
            <td>5.50%</td>
            <td>$567.79</td>
            <td>$104,404</td>
            <td>2.04×</td>
          </tr>
          <tr>
            <td><strong>30 Years</strong></td>
            <td>7.00%</td>
            <td>$665.30</td>
            <td>$139,510</td>
            <td>2.40×</td>
          </tr>
          <tr>
            <td><strong>30 Years</strong></td>
            <td>8.50%</td>
            <td>$768.91</td>
            <td>$176,809</td>
            <td>2.77×</td>
          </tr>
        </tbody>
      </table>
""",

    "ohms-law-calculator.html": """
      <h2>Electromagnetic Theory: Microscopic to Macroscopic Ohm's Law</h2>
      <p>Ohm's Law represents one of the foundational empirical laws of classical electromagnetism. Formulated by Georg Simon Ohm in 1827, it establishes that electric current passing through an isotropic conducting material is directly proportional to the applied potential difference across its terminals and inversely proportional to electrical resistance, provided temperature remains constant.</p>

      <h3>Microscopic Vector Formulation: Drude Electron Transport Model</h3>
      <p>At the sub-atomic quantum level, macroscopic Ohm's Law ($V = IR$) emerges from microscopic electron drift kinematics governed by the <strong>Drude Transport Model</strong>. In a conducting metal with electron charge density $n$, electronic charge $e$, electron effective mass $m_e$, and mean electron scattering relaxation time $\tau$, applied electric field vector $\mathbf{E}$ induces a current density vector $\mathbf{J}$:</p>
      <div class="math-block">
        $$\mathbf{J} = \sigma \mathbf{E} = \frac{n e^2 \tau}{m_e} \mathbf{E}$$
      </div>
      <p>Where electrical conductivity $\sigma$ is the reciprocal of electrical resistivity ($\sigma = 1/\rho$). Integrating current density across conductor cross-sectional area $A$ and electric field over length $L$ recovers macroscopic Ohm's Law:</p>
      <div class="math-block">
        $$V = \int_0^L \mathbf{E} \cdot d\mathbf{l} = E \cdot L,\quad I = \iint_A \mathbf{J} \cdot d\mathbf{A} = J \cdot A$$
        $$R = \rho \frac{L}{A} \implies V = I \cdot R$$
      </div>

      <h3>Joule Heating Thermodynamics & Power Formulations</h3>
      <p>Ohmic dissipation converts electrical potential energy into thermal kinetic energy through inelastic electron-phonon collisions in the crystal lattice. Electrical power dissipation $P$ evaluates across four interconnected formulations:</p>
      <div class="math-block">
        $$P = V \cdot I = I^2 R = \frac{V^2}{R} = \frac{E^2 L \cdot A}{\rho}$$
      </div>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Target Variable</th>
            <th>Given Voltage & Current ($V, I$)</th>
            <th>Given Voltage & Resistance ($V, R$)</th>
            <th>Given Current & Resistance ($I, R$)</th>
            <th>Given Power & Resistance ($P, R$)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Voltage ($V$)</strong></td>
            <td>$V = \frac{P}{I}$</td>
            <td>$V = \text{Specified}$</td>
            <td>$V = I \cdot R$</td>
            <td>$V = \sqrt{P \cdot R}$</td>
          </tr>
          <tr>
            <td><strong>Current ($I$)</strong></td>
            <td>$I = \text{Specified}$</td>
            <td>$I = \frac{V}{R}$</td>
            <td>$I = \text{Specified}$</td>
            <td>$I = \sqrt{\frac{P}{R}}$</td>
          </tr>
          <tr>
            <td><strong>Resistance ($R$)</strong></td>
            <td>$R = \frac{V}{I}$</td>
            <td>$R = \text{Specified}$</td>
            <td>$R = \text{Specified}$</td>
            <td>$R = \frac{P}{I^2}$</td>
          </tr>
          <tr>
            <td><strong>Power ($P$)</strong></td>
            <td>$P = V \cdot I$</td>
            <td>$P = \frac{V^2}{R}$</td>
            <td>$P = I^2 \cdot R$</td>
            <td>$P = \text{Specified}$</td>
          </tr>
        </tbody>
      </table>
""",

    "percentage-calculator.html": """
      <h2>Mathematical Logic of Ratios, Base Scaling, and Percentage Deltas</h2>
      <p>Percentages represent dimensionless scaling ratios normalized over a denominator of 100 ($\text{per centum}$). While mathematically elementary, percentage operations generate pervasive cognitive and analytical fallacies in finance, data science, and public policy due to base asymmetry and compounding scale shifts.</p>

      <h3>The Mathematical Asymmetry of Percentage Increases vs Decreases</h3>
      <p>A fundamental theorem of percentage arithmetic is that a percentage decrease followed by an identical percentage increase does not restore the original baseline value. If an asset priced at $X_0$ suffers a loss of $p\%$, its depreciated value is $X_1 = X_0(1 - p)$. A subsequent recovery of $p\%$ yields:</p>
      <div class="math-block">
        $$X_2 = X_1 (1 + p) = X_0 (1 - p)(1 + p) = X_0 (1 - p^2) < X_0$$
      </div>
      <p>For example, if an investment portfolio falls by $50\%$, it requires not a $50\%$ gain to recover, but an exact $100\%$ gain ($\frac{1}{1 - 0.50} - 1 = 1.00$) simply to break even!</p>

      <h3>Percentage Points vs Relative Percentage Change</h3>
      <p>Conflating percentage points with relative percentage change produces massive analytical distortions:</p>
      <ul>
        <li><strong>Percentage Point Difference ($\Delta_{\text{pts}}$):</strong> Absolute arithmetic subtraction between two rates ($\Delta = R_2 - R_1$). If central bank interest rates rise from $4.0\%$ to $5.0\%$, the increase is exactly $1.0\text{ percentage point}$ (or $100\text{ basis points}$).</li>
        <li><strong>Relative Percentage Change ($\% \Delta$):</strong> The fractional shift normalized against the initial baseline ($\% \Delta = \frac{R_2 - R_1}{R_1} \times 100\%$). Moving from $4.0\%$ to $5.0\%$ represents a relative increase of $\frac{5.0 - 4.0}{4.0} \times 100\% = +25.0\%$!</li>
      </ul>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Downside Percentage Loss</th>
            <th>Required Recovery Gain to Break Even</th>
            <th>Mathematical Recovery Multiplier</th>
            <th>Break-Even Formula</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>-10.0%</strong></td>
            <td>+11.11%</td>
            <td>1.111×</td>
            <td>$\frac{1}{0.90} - 1$</td>
          </tr>
          <tr>
            <td><strong>-20.0%</strong></td>
            <td>+25.00%</td>
            <td>1.250×</td>
            <td>$\frac{1}{0.80} - 1$</td>
          </tr>
          <tr>
            <td><strong>-33.3%</strong></td>
            <td>+50.00%</td>
            <td>1.500×</td>
            <td>$\frac{1}{0.667} - 1$</td>
          </tr>
          <tr>
            <td><strong>-50.0%</strong></td>
            <td>+100.00%</td>
            <td>2.000×</td>
            <td>$\frac{1}{0.50} - 1$</td>
          </tr>
          <tr>
            <td><strong>-75.0%</strong></td>
            <td>+300.00%</td>
            <td>4.000×</td>
            <td>$\frac{1}{0.25} - 1$</td>
          </tr>
          <tr>
            <td><strong>-90.0%</strong></td>
            <td>+900.00%</td>
            <td>10.000×</td>
            <td>$\frac{1}{0.10} - 1$</td>
          </tr>
        </tbody>
      </table>
""",

    "pipe-sizing-calculator.html": """
      <h2>Fluid Mechanics & Friction Head Loss in Hydraulic Piping Design</h2>
      <p>Hydraulic pipe dimensioning balances capital piping expenditures against lifetime pumping energy costs while preventing fluid erosion, excessive acoustic noise, and catastrophic water hammer pressure transients. Sizing is governed by the <strong>Continuity Equation</strong> and internal viscous friction laws defined by Darcy-Weisbach and Colebrook-White formulations.</p>

      <h3>Reynolds Number & Viscous Flow Regimes</h3>
      <p>Internal pipe flow behavior is determined by the dimensionless <strong>Reynolds Number ($Re$)</strong>, quantifying the ratio of inertial forces to viscous forces:</p>
      <div class="math-block">
        $$Re = \frac{\rho \cdot v \cdot D}{\mu} = \frac{v \cdot D}{\nu}$$
      </div>
      <p>Where $v$ is fluid velocity ($\text{m/s}$), $D$ is internal pipe diameter ($\text{m}$), and $\nu$ is kinematic viscosity ($\text{m}^2/\text{s}$). Fluid mechanics establishes three distinct flow regimes:</p>
      <ul>
        <li><strong>Laminar Flow ($Re < 2300$):</strong> Streamlined fluid layers with friction factor $f = \frac{64}{Re}$.</li>
        <li><strong>Transitional Flow ($2300 \le Re \le 4000$):</strong> Unstable, intermittent boundary-layer turbulence.</li>
        <li><strong>Turbulent Flow ($Re > 4000$):</strong> Chaotic vortex shedding governed by the implicit Colebrook-White equation:</li>
      </ul>
      <div class="math-block">
        $$\frac{1}{\sqrt{f}} = -2.0 \log_{10} \left( \frac{\varepsilon / D}{3.7} + \frac{2.51}{Re \sqrt{f}} \right)$$
      </div>

      <h3>Permissible Design Velocities & The Joukowsky Water Hammer Surge</h3>
      <p>To avoid internal pipe wall cavitation, erosion-corrosion, and structural vibration, industrial piping specifications restrict maximum flow velocities:</p>
      <ul>
        <li><strong>Pump Suction Lines:</strong> $0.6 - 1.5\text{ m/s}$ ($2 - 5\text{ ft/s}$) to ensure Net Positive Suction Head Available ($\text{NPSHa} > \text{NPSHr}$).</li>
        <li><strong>Pump Discharge / Distribution Headers:</strong> $1.5 - 2.4\text{ m/s}$ ($5 - 8\text{ ft/s}$).</li>
        <li><strong>Boiler Feedwater / High-Pressure Steam:</strong> $2.5 - 4.0\text{ m/s}$.</li>
      </ul>
      <p>Rapid valve closure induces a destructive kinetic pressure shock wave governed by the <strong>Joukowsky Equation</strong> ($\Delta P = \rho \cdot a \cdot \Delta v$, where $a \approx 1{,}200\text{ m/s}$ is acoustic wave velocity in water-filled steel pipe), generating instantaneous pressure surges exceeding $15 - 25\text{ bar}$!</p>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Nominal Pipe Size (NPS / DN)</th>
            <th>Internal Diameter (Sched 40 Steel)</th>
            <th>Recommended Flow at 1.5 m/s (m³/h)</th>
            <th>Recommended Flow at 2.4 m/s (m³/h)</th>
            <th>Friction Head Loss (m / 100m at 2.0 m/s)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>DN 25 (1")</strong></td>
            <td>26.6 mm</td>
            <td>3.00 m³/h</td>
            <td>4.80 m³/h</td>
            <td>17.5 m / 100m</td>
          </tr>
          <tr>
            <td><strong>DN 50 (2")</strong></td>
            <td>52.5 mm</td>
            <td>11.7 m³/h</td>
            <td>18.7 m³/h</td>
            <td>7.2 m / 100m</td>
          </tr>
          <tr>
            <td><strong>DN 80 (3")</strong></td>
            <td>77.9 mm</td>
            <td>25.7 m³/h</td>
            <td>41.2 m³/h</td>
            <td>4.3 m / 100m</td>
          </tr>
          <tr>
            <td><strong>DN 100 (4")</strong></td>
            <td>102.3 mm</td>
            <td>44.4 m³/h</td>
            <td>71.0 m³/h</td>
            <td>3.0 m / 100m</td>
          </tr>
          <tr>
            <td><strong>DN 150 (6")</strong></td>
            <td>154.1 mm</td>
            <td>100.7 m³/h</td>
            <td>161.1 m³/h</td>
            <td>1.8 m / 100m</td>
          </tr>
          <tr>
            <td><strong>DN 200 (8")</strong></td>
            <td>202.7 mm</td>
            <td>174.3 m³/h</td>
            <td>278.8 m³/h</td>
            <td>1.3 m / 100m</td>
          </tr>
        </tbody>
      </table>
""",

    "ratio-calculator.html": """
      <h2>Mathematical Theory of Proportions, Incommensurability, and Scaling Laws</h2>
      <p>A ratio represents an ordered mathematical relationship expressing the relative magnitude of two or more quantities ($a : b$). When two ratios are equated ($a : b = c : d$), they establish a <strong>Proportion</strong> governed by the fundamental property of proportionality: the product of the extremes equals the product of the means ($a \cdot d = b \cdot c$).</p>

      <h3>The Golden Ratio ($\phi$) and Incommensurable Geometry</h3>
      <p>A unique geometric proportion discovered by ancient Euclidean mathematicians is the <strong>Golden Ratio ($\phi$)</strong>, defined when the ratio of the whole segment ($a+b$) to the larger portion ($a$) equals the ratio of the larger portion to the smaller portion ($b$):</p>
      <div class="math-block">
        $$\frac{a + b}{a} = \frac{a}{b} = \phi \implies 1 + \frac{1}{\phi} = \phi \implies \phi^2 - \phi - 1 = 0$$
        $$\phi = \frac{1 + \sqrt{5}}{2} \approx 1.6180339887\dots$$
      </div>
      <p>The golden ratio represents the most irrational number in mathematics because its continued fraction expansion $[1; 1, 1, 1, \dots]$ possesses the slowest possible convergence rate, underlying optimal phyllotaxis spiral packing in plant morphology and logarithmic spirals in galactic kinematics.</p>

      <h3>Geometric Scaling: The Square-Cube Law</h3>
      <p>In biomechanics and structural engineering, ratios govern physical scaling via the <strong>Galileo Square-Cube Law</strong>. If an engineering structure or organism scales up proportionally by a linear dimension ratio of $k$ ($L_2 = k \cdot L_1$):</p>
      <ul>
        <li>Surface area scales quadratically ($A_2 = k^2 \cdot A_1$).</li>
        <li>Enclosed volume and gravitational mass scale cubically ($V_2 = k^3 \cdot V_1$).</li>
      </ul>
      <p>Because structural load-bearing capacity depends on cross-sectional area ($\propto k^2$) while mechanical gravitational weight scales with volume ($\propto k^3$), doubling an animal's size ($k=2$) increases its weight by $8\times$ while its bone cross-sectional strength increases only $4\times$, explaining why elephants require disproportionately massive columnar limbs compared to gazelles.</p>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Application Discipline</th>
            <th>Standard Aspect / Scale Ratio</th>
            <th>Decimal Value</th>
            <th>Primary Engineering / Artistic Application</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>High-Definition Video (16:9)</strong></td>
            <td>$16 : 9$</td>
            <td>1.778 : 1</td>
            <td>Global broadcast standard for television, monitors, streaming media</td>
          </tr>
          <tr>
            <td><strong>Cinemascope Widescreen (21:9)</strong></td>
            <td>$64 : 27$</td>
            <td>2.370 : 1</td>
            <td>Anamorphic theatrical motion picture format</td>
          </tr>
          <tr>
            <td><strong>Classic Photography (3:2)</strong></td>
            <td>$3 : 2$</td>
            <td>1.500 : 1</td>
            <td>35mm film sensor format; golden standard for DSLR cameras</td>
          </tr>
          <tr>
            <td><strong>Standard Paper (ISO A4 1:√2)</strong></td>
            <td>$1 : \sqrt{2}$</td>
            <td>1 : 1.414</td>
            <td>ISO 216 paper sizing; halving sheet retains exact identical aspect ratio</td>
          </tr>
          <tr>
            <td><strong>Mechanical Gear Reducer</strong></td>
            <td>$N_1 : N_2$</td>
            <td>Variable</td>
            <td>Torque multiplier ($\tau_2 = \tau_1 \times (N_2 / N_1)$), speed reduction</td>
          </tr>
        </tbody>
      </table>
""",

    "rebar-calculator.html": """
      <h2>Structural Concrete Reinforcement Mechanics & ACI 318-19 Formulations</h2>
      <p>Plain unreinforced concrete possesses tremendous compressive strength ($20 - 50\text{ MPa}$) but brittle, weak tensile strength (typically only $8\% - 12\%$ of compressive resistance). Deformed steel rebar ($f_y = 420\text{ MPa} / 60\text{ ksi}$) embedded along tension zones carries all tensile and flexural stresses, governed by <strong>ACI 318-19: Building Code Requirements for Structural Concrete</strong>.</p>

      <h3>Flexural Beam Mechanics & The Balanced Reinforcement Ratio</h3>
      <p>In reinforced concrete flexural design, the internal stress distribution of a cracked beam section transforms into a Whitney equivalent rectangular compressive stress block of depth $a = \beta_1 c$. Tensile yield equilibrium dictates:</p>
      <div class="math-block">
        $$T = C \implies A_s f_y = 0.85 f'_c b a \implies a = \frac{A_s f_y}{0.85 f'_c b}$$
        $$M_n = A_s f_y \left( d - \frac{a}{2} \right)$$
      </div>
      <p>To ensure ductile failure (where rebar yields with visible cracking before explosive concrete crushing occurs), ACI 318-19 requires tension steel strain $\varepsilon_t \ge 0.005$ and enforces minimum reinforcement bounds:</p>
      <div class="math-block">
        $$\rho_{\min} = \frac{A_s}{b \cdot d} \ge \max\left( \frac{0.25 \sqrt{f'_c}}{f_y},\ \frac{1.4}{f_y} \right)$$
      </div>

      <h3>Development Length ($l_d$) & Lap Splice Requirements</h3>
      <p>Steel rebar transfers stress into surrounding concrete via interfacial bond shear and rib mechanical interlock. The tension development length $l_d$ required to prevent pullout bond failure is given by:</p>
      <div class="math-block">
        $$l_d = \left( \frac{f_y}{1.1 \lambda \sqrt{f'_c}} \cdot \frac{\psi_t \psi_e \psi_s}{\left( \frac{c_b + K_{tr}}{d_b} \right)} \right) d_b$$
      </div>
      <p>Standard Class B lap splices in structural beams and foundation footings typically require lap lengths equal to $1.3 \times l_d$ (commonly $40\text{ to } 50\times$ the nominal bar diameter $d_b$).</p>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>US Bar Size</th>
            <th>Metric Designation</th>
            <th>Nominal Diameter ($d_b$)</th>
            <th>Cross-Sectional Area ($A_b$)</th>
            <th>Unit Weight (kg/m / lb/ft)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>#3 Rebar</strong></td>
            <td>10M</td>
            <td>9.53 mm (0.375")</td>
            <td>71 mm² (0.11 in²)</td>
            <td>0.560 kg/m (0.376 lb/ft)</td>
          </tr>
          <tr>
            <td><strong>#4 Rebar</strong></td>
            <td>13M</td>
            <td>12.70 mm (0.500")</td>
            <td>129 mm² (0.20 in²)</td>
            <td>0.994 kg/m (0.668 lb/ft)</td>
          </tr>
          <tr>
            <td><strong>#5 Rebar</strong></td>
            <td>16M</td>
            <td>15.88 mm (0.625")</td>
            <td>199 mm² (0.31 in²)</td>
            <td>1.552 kg/m (1.043 lb/ft)</td>
          </tr>
          <tr>
            <td><strong>#6 Rebar</strong></td>
            <td>19M</td>
            <td>19.05 mm (0.750")</td>
            <td>284 mm² (0.44 in²)</td>
            <td>2.235 kg/m (1.502 lb/ft)</td>
          </tr>
          <tr>
            <td><strong>#8 Rebar</strong></td>
            <td>25M</td>
            <td>25.40 mm (1.000")</td>
            <td>510 mm² (0.79 in²)</td>
            <td>3.973 kg/m (2.670 lb/ft)</td>
          </tr>
          <tr>
            <td><strong>#10 Rebar</strong></td>
            <td>32M</td>
            <td>32.26 mm (1.270")</td>
            <td>819 mm² (1.27 in²)</td>
            <td>6.404 kg/m (4.303 lb/ft)</td>
          </tr>
        </tbody>
      </table>
""",

    "resistor-color-code-calculator.html": """
      <h2>Standard Color-Code Band Decoding & Standard EIA Decade Values</h2>
      <p>The electronic resistor color-coding system, standardized under <strong>IEC 60062</strong> and <strong>EIA-RS-279</strong>, provides an unambiguous optical marking scheme to identify the nominal resistance value, manufacturing tolerance, and temperature coefficient of leaded axial passive components without requiring micro-text printing.</p>

      <h3>Decoding 4-Band, 5-Band, and 6-Band Color Resistors</h3>
      <p>Axial through-hole resistors employ three standardized band formats:</p>
      <ul>
        <li><strong>4-Band Resistors (Standard Tolerance $\pm 5\% - 10\%$):</strong>
          <ul>
            <li>Band 1: First significant digit (0–9).</li>
            <li>Band 2: Second significant digit (0–9).</li>
            <li>Band 3: Multiplier ($10^n$, including Gold = $0.1$ and Silver = $0.01$).</li>
            <li>Band 4: Tolerance ($\pm\%$, Gold = $5\%$, Silver = $10\%$).</li>
          </ul>
        </li>
        <li><strong>5-Band Resistors (Precision Tolerance $\pm 0.5\% - 2\%$):</strong> Three significant digits, followed by multiplier and tolerance bands, yielding higher numerical precision.</li>
        <li><strong>6-Band Resistors (High-Stability & Military):</strong> Five standard precision bands plus a 6th band indicating the <strong>Temperature Coefficient of Resistance (TCR)</strong> expressed in parts per million per Kelvin ($ppm/\text{K}$).</li>
      </ul>

      <h3>Standard EIA Decade Series (E12, E24, E96, E192)</h3>
      <p>Resistor values are not manufactured at random intervals. Instead, standard component values conform to geometrically spaced logarithmic decades defined by the <strong>Renard Series</strong> ($R_n = 10^{k/N}$), ensuring that adjacent values within their tolerance envelopes cover the entire spectrum without wasteful overlap:</p>
      <div class="math-block">
        $$\text{Value Step Multiplier} = \sqrt[N]{10}$$
      </div>
      <p>For the $E12$ series ($10\%$ tolerance), $N = 12$, producing the twelve canonical base values: $10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82$. The $E96$ series ($1\%$ precision) features $96$ logarithmically spaced base values across each decade.</p>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Color Band</th>
            <th>Significant Digit</th>
            <th>Multiplier ($10^n$)</th>
            <th>Tolerance Band</th>
            <th>6th Band TCR (ppm/K)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Black</strong></td>
            <td>0</td>
            <td>$10^0 = 1\ \Omega$</td>
            <td>--</td>
            <td>$250\text{ ppm/K}$</td>
          </tr>
          <tr>
            <td><strong>Brown</strong></td>
            <td>1</td>
            <td>$10^1 = 10\ \Omega$</td>
            <td>$\pm 1\%$ (F)</td>
            <td>$100\text{ ppm/K}$</td>
          </tr>
          <tr>
            <td><strong>Red</strong></td>
            <td>2</td>
            <td>$10^2 = 100\ \Omega$</td>
            <td>$\pm 2\%$ (G)</td>
            <td>$50\text{ ppm/K}$</td>
          </tr>
          <tr>
            <td><strong>Orange</strong></td>
            <td>3</td>
            <td>$10^3 = 1\text{ k}\Omega$</td>
            <td>$\pm 0.05\%$</td>
            <td>$15\text{ ppm/K}$</td>
          </tr>
          <tr>
            <td><strong>Yellow</strong></td>
            <td>4</td>
            <td>$10^4 = 10\text{ k}\Omega$</td>
            <td>--</td>
            <td>$25\text{ ppm/K}$</td>
          </tr>
          <tr>
            <td><strong>Green</strong></td>
            <td>5</td>
            <td>$10^5 = 100\text{ k}\Omega$</td>
            <td>$\pm 0.5\%$ (D)</td>
            <td>$20\text{ ppm/K}$</td>
          </tr>
          <tr>
            <td><strong>Blue</strong></td>
            <td>6</td>
            <td>$10^6 = 1\text{ M}\Omega$</td>
            <td>$\pm 0.25\%$ (C)</td>
            <td>$10\text{ ppm/K}$</td>
          </tr>
          <tr>
            <td><strong>Violet</strong></td>
            <td>7</td>
            <td>$10^7 = 10\text{ M}\Omega$</td>
            <td>$\pm 0.1\%$ (B)</td>
            <td>$5\text{ ppm/K}$</td>
          </tr>
          <tr>
            <td><strong>Gold</strong></td>
            <td>--</td>
            <td>$10^{-1} = 0.1\ \Omega$</td>
            <td>$\pm 5\%$ (J)</td>
            <td>--</td>
          </tr>
          <tr>
            <td><strong>Silver</strong></td>
            <td>--</td>
            <td>$10^{-2} = 0.01\ \Omega$</td>
            <td>$\pm 10\%$ (K)</td>
            <td>--</td>
          </tr>
        </tbody>
      </table>
""",

    "salary-calculator.html": """
      <h2>Macroeconomic Decomposition of Gross Compensation & Payroll Economics</h2>
      <p>The conversion of contracted annual salary into net disposable take-home pay is governed by sovereign progressive income taxation, mandatory social security contributions, and pre-tax fringe benefit elections. Gross compensation is neither equivalent to an employee's liquid income nor is it the full economic cost borne by an employer.</p>

      <h3>Progressive Marginal Tax Brackets vs Effective Average Tax Rate</h3>
      <p>Modern fiscal systems utilize progressive tax brackets wherein higher income tiers face higher marginal rates. An employee's gross income is not taxed at a single rate; instead, progressive slicing applies:</p>
      <div class="math-block">
        $$\text{Total Federal Tax} = \sum_{j=1}^{m} \tau_j \cdot \max\left( 0,\ \min(Y_{\text{taxable}},\ K_j) - K_{j-1} \right)$$
        $$\text{Effective Average Tax Rate} = \frac{\text{Total Taxes Paid}}{Y_{\text{gross}}} \times 100\%$$
      </div>
      <p>Where $\tau_j$ represents the marginal tax rate of tier $j$, and $K_j$ represents the tier ceiling boundary. Because statutory deductions (standard deduction, personal exemptions) shield the lowest earning dollars, the effective tax rate is substantially lower than the employee's top marginal tax bracket.</p>

      <h3>Total Cost of Employment (TCOE) Employer Burden</h3>
      <p>From an enterprise accounting perspective, an employee's contracted gross salary ($Y_{\text{gross}}$) represents only $70\% - 80\%$ of their <strong>Total Cost of Employment (TCOE)</strong>. Employers incur statutory and contractual overheads:</p>
      <div class="math-block">
        $$\text{TCOE} = Y_{\text{gross}} + \text{FICA Match (7.65\%)} + \text{FUTA/SUTA Unemployment} + \text{Workers' Comp} + \text{Health Benefits} + \text{401(k) Match}$$
      </div>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Gross Annual Salary</th>
            <th>Monthly Gross</th>
            <th>Bi-Weekly Paycheck (26/yr)</th>
            <th>Est. Net Take-Home (Single Filer)</th>
            <th>Effective Overall Tax Burden</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>$45,000 / yr</strong></td>
            <td>$3,750</td>
            <td>$1,731</td>
            <td>$1,385 / check</td>
            <td>~20.0%</td>
          </tr>
          <tr>
            <td><strong>$65,000 / yr</strong></td>
            <td>$5,417</td>
            <td>$2,500</td>
            <td>$1,940 / check</td>
            <td>~22.4%</td>
          </tr>
          <tr>
            <td><strong>$95,000 / yr</strong></td>
            <td>$7,917</td>
            <td>$3,654</td>
            <td>$2,631 / check</td>
            <td>~28.0%</td>
          </tr>
          <tr>
            <td><strong>$130,000 / yr</strong></td>
            <td>$10,833</td>
            <td>$5,000</td>
            <td>$3,485 / check</td>
            <td>~30.3%</td>
          </tr>
          <tr>
            <td><strong>$180,000 / yr</strong></td>
            <td>$15,000</td>
            <td>$6,923</td>
            <td>$4,650 / check</td>
            <td>~32.8%</td>
          </tr>
        </tbody>
      </table>
""",

    "simple-interest-calculator.html": """
      <h2>Mathematical Theory of Simple Interest & Commercial Discounting</h2>
      <p>Simple interest represents the most straightforward financial model of debt service, where capital growth occurs at a constant, linear velocity over time. Unlike compound interest, interest accrued during preceding periods does not capitalize into the principal balance; only the original principal sum generates returns over the elapsed investment tenure.</p>

      <h3>The Linear Simple Interest Formulation</h3>
      <p>For a principal investment $P$ accruing simple interest at an annual percentage rate $r$ (expressed as a decimal) over elapsed duration $t$ years, total interest earned $I$ and cumulative maturity balance $A(t)$ evaluate as:</p>
      <div class="math-block">
        $$I = P \cdot r \cdot t$$
        $$A(t) = P + I = P (1 + r \cdot t)$$
      </div>

      <h3>Exact vs Ordinary Simple Interest (Banker's Rule)</h3>
      <p>When calculating simple interest over discrete calendar days ($d$), historical banking traditions established two distinct conventions:</p>
      <ul>
        <li><strong>Exact Simple Interest (Actual/365):</strong> Evaluates time as $t = \frac{d}{365}$ (or $366$ in leap years). Standard in government debt securities and treasury bill accounting.</li>
        <li><strong>Ordinary Simple Interest / Banker's Rule (Actual/360):</strong> Evaluates time as $t = \frac{d}{360}$. Because the 360-day denominator is smaller than the true 365-day solar year, the Banker's Rule yields $\frac{365}{360} \approx 1.0139\times$ ($1.39\%$ more interest) on identical capital!</li>
      </ul>

      <h3>Commercial Paper & Treasury Bill Bank Discount Yields</h3>
      <p>Short-term commercial paper and government Treasury bills do not pay periodic coupons; instead, they are sold at a discount to their face maturity value ($F$). The discount yield ($d$) is calculated based on face value rather than purchase price ($P = F(1 - d \cdot t)$). To convert bank discount yield $d$ into equivalent simple investment yield ($Y$):</p>
      <div class="math-block">
        $$Y = \frac{365 \cdot d}{360 - d \cdot t_{\text{days}}}$$
      </div>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Principal Sum ($P$)</th>
            <th>Annual Rate ($r$)</th>
            <th>Duration ($t$)</th>
            <th>Simple Interest Earned ($I$)</th>
            <th>Compounded Monthly Balance ($A$)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>$5,000</strong></td>
            <td>4.0%</td>
            <td>3 Years</td>
            <td>$600.00</td>
            <td>$5,636.36 (+$36.36)</td>
          </tr>
          <tr>
            <td><strong>$10,000</strong></td>
            <td>6.0%</td>
            <td>5 Years</td>
            <td>$3,000.00</td>
            <td>$13,488.50 (+$488.50)</td>
          </tr>
          <tr>
            <td><strong>$25,000</strong></td>
            <td>8.0%</td>
            <td>7 Years</td>
            <td>$14,000.00</td>
            <td>$43,685.95 (+$4,685.95)</td>
          </tr>
          <tr>
            <td><strong>$50,000</strong></td>
            <td>10.0%</td>
            <td>10 Years</td>
            <td>$50,000.00</td>
            <td>$135,352.07 (+$35,352.07)</td>
          </tr>
        </tbody>
      </table>
""",

    "smoke-detector-spacing-calculator.html": """
      <h2>Fire Dynamics & NFPA 72 Engineering Design Guidelines</h2>
      <p>Automatic fire smoke detection engineering is governed by <strong>NFPA 72: National Fire Alarm and Signaling Code</strong>. Smoke detectors rely on buoyant convective thermal plumes generated by combustion to carry suspended particulate aerosols into the detector sensing chamber. Sizing detector placement requires accounting for ceiling geometry, stratification boundaries, beam pockets, and HVAC ventilation air dilution.</p>

      <h3>Smooth Ceiling Coverage Geometry & Point-to-Point Radial Distance</h3>
      <p>Under NFPA 72 Section 17.7.3.2.3.1, point-type smoke detectors mounted on smooth ceilings carry a nominal rated spacing of $S = 30\text{ feet}$ ($9.1\text{ meters}$). This spacing is derived from inscribing square detector zones inside a circle of radius $R = \frac{S}{\sqrt{2}} = 21.2\text{ feet}$ ($6.46\text{ meters}$):</p>
      <div class="math-block">
        $$R = 0.707 \times S = 21.21\text{ ft (6.46 m)}$$
      </div>
      <p>Every point on the ceiling must fall within radius $R$ of at least one detector. Detectors must be located at least $4\text{ inches}$ ($100\text{ mm}$) from side walls and no closer than $36\text{ inches}$ ($914\text{ mm}$) from forced-air HVAC supply diffusers to avoid clean air wash.</p>

      <h3>Thermal Stratification & Ceiling Height Reduction Multipliers</h3>
      <p>In high-ceiling spaces (atriums, aircraft hangars, warehouses), buoyant smoke cools as it entrains surrounding ambient air. In heated buildings with solar roof exposure, a hot ceiling air boundary layer forms, causing the rising smoke plume to lose buoyancy and <strong>stratify</strong> several feet below the physical ceiling. In such environments, projected optical beam detectors or aspirating smoke detection (ASD) systems must be engineered.</p>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Ceiling Height (ft / m)</th>
            <th>NFPA Heat Detector Reduction Factor</th>
            <th>Equivalent Linear Spacing ($S$)</th>
            <th>Coverage Area per Unit (ft²)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Up to 10 ft (3.05 m)</strong></td>
            <td>1.00</td>
            <td>30.0 ft</td>
            <td>900 ft²</td>
          </tr>
          <tr>
            <td><strong>10 to 12 ft (3.66 m)</strong></td>
            <td>0.91</td>
            <td>27.3 ft</td>
            <td>745 ft²</td>
          </tr>
          <tr>
            <td><strong>12 to 14 ft (4.27 m)</strong></td>
            <td>0.84</td>
            <td>25.2 ft</td>
            <td>635 ft²</td>
          </tr>
          <tr>
            <td><strong>14 to 16 ft (4.88 m)</strong></td>
            <td>0.77</td>
            <td>23.1 ft</td>
            <td>534 ft²</td>
          </tr>
          <tr>
            <td><strong>16 to 18 ft (5.49 m)</strong></td>
            <td>0.71</td>
            <td>21.3 ft</td>
            <td>454 ft²</td>
          </tr>
          <tr>
            <td><strong>20 to 22 ft (6.71 m)</strong></td>
            <td>0.58</td>
            <td>17.4 ft</td>
            <td>303 ft²</td>
          </tr>
          <tr>
            <td><strong>28 to 30 ft (9.14 m)</strong></td>
            <td>0.34</td>
            <td>10.2 ft</td>
            <td>104 ft²</td>
          </tr>
        </tbody>
      </table>
""",

    "solar-battery-bank-calculator.html": """
      <h2>Electrochemical Storage Mechanics & Sizing Equations for Off-Grid Solar</h2>
      <p>Solar energy storage systems decouple photovoltaic daytime generation from diurnal household load profiles. Sizing battery capacity requires engineering around electrochemical storage limits: Peukert's capacity loss, maximum Depth of Discharge (DoD), round-trip Coulombic efficiency, and multi-day meteorological solar drought autonomy.</p>

      <h3>Off-Grid Battery Bank Sizing Formulation</h3>
      <p>The total nominal battery bank storage capacity ($C_{\text{bank}}$ in kilowatt-hours) required to supply daily energy consumption $E_{\text{daily}}$ over $N_{\text{days}}$ of autonomy is given by:</p>
      <div class="math-block">
        $$C_{\text{bank}}(\text{kWh}) = \frac{E_{\text{daily}}(\text{kWh}) \times N_{\text{autonomy}}}{\text{DoD}_{\max} \times \eta_{\text{inv}} \times \eta_{\text{temp}}}$$
        $$\text{Ampere-Hour Capacity (Ah)} = \frac{C_{\text{bank}}(\text{kWh}) \times 1000}{V_{\text{system}}(\text{V})}$$
      </div>
      <p>Where $\text{DoD}_{\max}$ is maximum allowable depth of discharge ($80\% - 90\%$ for Lithium Iron Phosphate $\text{LiFePO}_4$; $50\%$ for flooded lead-acid), $\eta_{\text{inv}}$ is DC-to-AC inverter conversion efficiency ($\approx 92\% - 96\%$), and $\eta_{\text{temp}}$ is temperature derating at winter minimums.</p>

      <h3>LiFePO4 vs Lead-Acid Peukert Capacity Degradation</h3>
      <p>Under <strong>Peukert's Law</strong> ($C_p = I^k \cdot t$), lead-acid battery banks suffer severe usable capacity reductions under heavy continuous discharge rates ($k \approx 1.25 - 1.40$). A lead-acid battery rated at $100\text{ Ah}$ at a slow $20\text{-hour}$ discharge rate ($C_{20}$) delivers only $65\text{ Ah}$ if discharged over $2\text{ hours}$ ($C_2$). In contrast, modern lithium iron phosphate ($\text{LiFePO}_4$) cells exhibit a near-ideal Peukert exponent ($k \approx 1.02 - 1.05$), delivering full rated capacity even under $1C$ heavy continuous inverter loads.</p>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Battery Chemistry</th>
            <th>Usable Depth of Discharge (DoD)</th>
            <th>Expected Cycle Life</th>
            <th>Round-Trip Coulombic Efficiency</th>
            <th>Energy Density (Wh/kg)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Flooded Lead-Acid (FLA)</strong></td>
            <td>50%</td>
            <td>500 - 1,200 cycles</td>
            <td>75% - 82%</td>
            <td>30 - 40 Wh/kg</td>
          </tr>
          <tr>
            <td><strong>Absorbent Glass Mat (AGM)</strong></td>
            <td>50%</td>
            <td>600 - 1,500 cycles</td>
            <td>80% - 85%</td>
            <td>35 - 45 Wh/kg</td>
          </tr>
          <tr>
            <td><strong>Lithium Iron Phosphate (LiFePO4)</strong></td>
            <td>80% - 90%</td>
            <td>4,000 - 8,000 cycles</td>
            <td>95% - 98%</td>
            <td>90 - 130 Wh/kg</td>
          </tr>
          <tr>
            <td><strong>Lithium NMC (Ternary)</strong></td>
            <td>80% - 90%</td>
            <td>1,500 - 3,000 cycles</td>
            <td>92% - 95%</td>
            <td>150 - 220 Wh/kg</td>
          </tr>
        </tbody>
      </table>
""",

    "solar-inverter-sizing-calculator.html": """
      <h2>Power Electronics & MPPT String Inverter Sizing Engineering</h2>
      <p>Solar photovoltaic inverters convert variable direct-current (DC) power from solar arrays into synchronized utility-grade alternating current (AC). Dimensioning solar inverters requires optimizing the <strong>Inverter Loading Ratio (ILR)</strong>, matching Maximum Power Point Tracking (MPPT) voltage operating windows, and verifying open-circuit cold-temperature safety voltages against <strong>NEC Article 690.7</strong>.</p>

      <h3>Inverter Loading Ratio (ILR / DC-to-AC Ratio) Economics</h3>
      <p>Modern commercial and residential solar systems are engineered with a DC-to-AC ratio exceeding unity ($\text{ILR} = 1.15 \text{ to } 1.35$):</p>
      <div class="math-block">
        $$\text{ILR} = \frac{\text{Total DC Array Nameplate Rating (kWp)}}{\text{Inverter Continuous AC Output Capacity (kW)}}$$
      </div>
      <p>Because solar panels operate at nameplate STC rating ($1{,}000\text{ W/m}^2$, $25^\circ\text{C}$ cell temperature) for fewer than $5\%$ of daylight hours due to thermal degradation and oblique sun angles, sizing the inverter equal to peak DC capacity leaves power electronics severely underutilized. An oversizing ratio of $1.25$ increases total annual energy harvest by $10\% - 18\%$ while incurring negligible mid-day clipping losses ($< 1.5\%$).</p>

      <h3>Cold Temperature Open-Circuit Voltage ($V_{oc}$) Safety Calculation</h3>
      <p>Photovoltaic semiconductors possess a negative temperature coefficient ($\gamma_{Voc} \approx -0.28\% / ^\circ\text{C}$). In winter cold snaps, string open-circuit voltage rises substantially. To prevent catastrophic inverter semiconductor gate breakdown, maximum string open-circuit voltage at record low ambient temperature ($T_{\min}$) must not exceed the inverter's maximum input DC voltage rating ($600\text{V}$ residential, $1000\text{V} - 1500\text{V}$ commercial):</p>
      <div class="math-block">
        $$V_{oc,\max} = N_{\text{modules}} \times V_{oc,STC} \times \left[ 1 + \left( \frac{\gamma_{Voc}}{100} \right) \times (T_{\min} - 25) \right] \le V_{\text{inv,max}}$$
      </div>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Inverter Topology</th>
            <th>Typical System Size</th>
            <th>MPPT Voltage Window</th>
            <th>Peak Conversion Efficiency</th>
            <th>Shading & Mismatch Tolerance</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Microinverters (Enphase)</strong></td>
            <td>Residential (3 kW - 15 kW)</td>
            <td>25V - 60V per panel</td>
            <td>97.0% - 97.5%</td>
            <td>Maximum; panel-level independent optimization</td>
          </tr>
          <tr>
            <td><strong>DC Optimizers + Inverter (SolarEdge)</strong></td>
            <td>Residential / Commercial</td>
            <td>8V - 80V buck/boost</td>
            <td>98.0% - 99.0%</td>
            <td>High; panel-level MPPT with central inverter</td>
          </tr>
          <tr>
            <td><strong>String Inverter (SMA / Fronius)</strong></td>
            <td>Commercial (10 kW - 100 kW)</td>
            <td>200V - 850V DC</td>
            <td>98.2% - 98.6%</td>
            <td>Moderate; string performance limited by weakest cell</td>
          </tr>
          <tr>
            <td><strong>Central Utility Inverter</strong></td>
            <td>Utility Scale (1 MW - 5 MW)</td>
            <td>800V - 1500V DC</td>
            <td>98.8% - 99.2%</td>
            <td>Requires unshaded uniform utility solar fields</td>
          </tr>
        </tbody>
      </table>
""",

    "solar-panel-sizing-calculator.html": """
      <h2>Solar Photovoltaic Resource Geometry & Array Sizing Formulations</h2>
      <p>Dimensioning a solar photovoltaic array involves balancing building electrical load demand against geographical solar irradiance. Array sizing calculations combine solar astronomical geometry, local Peak Sun Hours (PSH), array tilt transposition, and system loss derating factors defined in <strong>NREL PVWatts</strong> methodologies.</p>

      <h3>Peak Sun Hours (PSH) & Global Horizontal Irradiance Integration</h3>
      <p>Solar irradiance measures instantaneous solar radiant power flux per unit area ($\text{W/m}^2$). Solar irradiation, or insolation, represents cumulative energy integrated over time ($\text{kWh/m}^2/\text{day}$). One <strong>Peak Sun Hour (PSH)</strong> is defined as the equivalent duration that solar irradiance would need to shine at standardized STC intensity ($1{,}000\text{ W/m}^2$) to deliver identical total daily insolation:</p>
      <div class="math-block">
        $$1\text{ PSH} \equiv 1.0\text{ kWh/m}^2/\text{day} = 3.6\text{ MJ/m}^2/\text{day}$$
      </div>

      <h3>Total Array Capacity Sizing Formulation</h3>
      <p>The total DC nameplate array capacity ($P_{\text{array}}$ in kilowatts-peak, $\text{kWp}$) required to offset average daily energy consumption ($E_{\text{daily}}$ in $\text{kWh/day}$) is calculated as:</p>
      <div class="math-block">
        $$P_{\text{array}}(\text{kWp}) = \frac{E_{\text{daily}}(\text{kWh/day})}{\text{PSH} \times \eta_{\text{system}}}$$
        $$N_{\text{panels}} = \left\lceil \frac{P_{\text{array}} \times 1000}{P_{\text{module,STC}}} \right\rceil$$
      </div>
      <p>Where $\eta_{\text{system}}$ represents the compound system derating factor ($\approx 75\% - 82\%$), combining soiling ($2\% - 5\%$), thermal cell heat derating ($8\% - 14\%$), wiring ohmic drop ($2\%$), inverter conversion losses ($2\% - 4\%$), and module nameplate tolerance mismatch ($1\%$).</p>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Geographical Region</th>
            <th>Annual Average Peak Sun Hours (PSH)</th>
            <th>Recommended Array Tilt</th>
            <th>Required Array Size for 30 kWh/day (80% System Eff)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Southwest US / Desert Sunbelt</strong></td>
            <td>5.5 - 6.5 PSH / day</td>
            <td>Latitude - 5° (~25°–30°)</td>
            <td>6.0 kWp - 6.8 kWp (15–17 Panels)</td>
          </tr>
          <tr>
            <td><strong>Southern US / Mediterranean</strong></td>
            <td>4.5 - 5.5 PSH / day</td>
            <td>Latitude (~30°–35°)</td>
            <td>6.8 kWp - 8.3 kWp (17–21 Panels)</td>
          </tr>
          <tr>
            <td><strong>Mid-Atlantic / Central Europe</strong></td>
            <td>3.5 - 4.5 PSH / day</td>
            <td>Latitude (~35°–45°)</td>
            <td>8.3 kWp - 10.7 kWp (21–27 Panels)</td>
          </tr>
          <tr>
            <td><strong>Northern US / UK / Scandinavia</strong></td>
            <td>2.5 - 3.5 PSH / day</td>
            <td>Latitude (~45°–55°)</td>
            <td>10.7 kWp - 15.0 kWp (27–38 Panels)</td>
          </tr>
        </tbody>
      </table>
""",

    "subnet-calculator.html": """
      <h2>Binary Boolean Masking & VLSM Subnetting Architecture</h2>
      <p>In Internet Protocol version 4 (IPv4) networking, defined under <strong>RFC 791</strong> and <strong>RFC 4632</strong>, a 32-bit address is partitioned into a network prefix and a host identifier. Subnetting enables network administrators to divide physical and virtual networks into segmented broadcast domains, optimizing IP address utilization and enforcing routing firewall boundaries.</p>

      <h3>Bitwise Boolean Masking & Host Population Equations</h3>
      <p>Every IPv4 address and subnet mask consists of 32 binary bits divided into four 8-bit octets. When a routing device evaluates a destination packet, it performs a bitwise logical AND operation ($\&$) between the 32-bit destination IP address and the configured Subnet Mask:</p>
      <div class="math-block">
        $$\text{Network Address} = \text{Destination IP Address} \ \& \ \text{Subnet Mask}$$
        $$\text{Broadcast Address} = \text{Network Address} \ | \ (\sim \text{Subnet Mask})$$
      </div>
      <p>For any Classless Inter-Domain Routing (CIDR) prefix length $/n$ (where $n$ represents the count of leading 1-bits in the mask), the host bit count is $h = 32 - n$. The total address block size and usable host population evaluate as:</p>
      <div class="math-block">
        $$\text{Total Addresses} = 2^{32 - n} = 2^h$$
        $$\text{Usable Host Addresses} = 2^h - 2\quad (\text{for } n \le 30)$$
      </div>
      <p>Two addresses in every subnet are reserved by protocol: the all-zeros host address (identifying the Network Wire) and the all-ones host address (identifying the Subnet Directed Broadcast).</p>

      <h3>Point-to-Point Links: /30 vs RFC 3021 /31 Subnets</h3>
      <p>In legacy routing, point-to-point router serial links utilized $/30$ subnets, allocating $4$ addresses ($2^2$) to provide $2$ usable host interfaces, resulting in a $50\%$ address wastage rate. <strong>RFC 3021: Using 31-Bit Prefixes on IPv4 Point-to-Point Links</strong> eliminated this inefficiency by permitting $/31$ subnets on point-to-point Ethernet links, treating the host bits $0$ and $1$ as valid endpoints without network or broadcast reservations.</p>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>CIDR Prefix</th>
            <th>Dotted Decimal Subnet Mask</th>
            <th>Wildcard Mask</th>
            <th>Total Addresses</th>
            <th>Usable Host Interfaces</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>/24</strong></td>
            <td>255.255.255.0</td>
            <td>0.0.0.255</td>
            <td>256</td>
            <td>254 hosts (Standard LAN)</td>
          </tr>
          <tr>
            <td><strong>/25</strong></td>
            <td>255.255.255.128</td>
            <td>0.0.0.127</td>
            <td>128</td>
            <td>126 hosts</td>
          </tr>
          <tr>
            <td><strong>/26</strong></td>
            <td>255.255.255.192</td>
            <td>0.0.0.63</td>
            <td>64</td>
            <td>62 hosts</td>
          </tr>
          <tr>
            <td><strong>/27</strong></td>
            <td>255.255.255.224</td>
            <td>0.0.0.31</td>
            <td>32</td>
            <td>30 hosts</td>
          </tr>
          <tr>
            <td><strong>/28</strong></td>
            <td>255.255.255.240</td>
            <td>0.0.0.15</td>
            <td>16</td>
            <td>14 hosts</td>
          </tr>
          <tr>
            <td><strong>/29</strong></td>
            <td>255.255.255.248</td>
            <td>0.0.0.7</td>
            <td>8</td>
            <td>6 hosts (Small DMZ)</td>
          </tr>
          <tr>
            <td><strong>/30</strong></td>
            <td>255.255.255.252</td>
            <td>0.0.0.3</td>
            <td>4</td>
            <td>2 hosts (Point-to-point)</td>
          </tr>
          <tr>
            <td><strong>/31</strong></td>
            <td>255.255.255.254</td>
            <td>0.0.0.1</td>
            <td>2</td>
            <td>2 hosts (RFC 3021 P2P)</td>
          </tr>
          <tr>
            <td><strong>/32</strong></td>
            <td>255.255.255.255</td>
            <td>0.0.0.0</td>
            <td>1</td>
            <td>1 host (Loopback interface)</td>
          </tr>
        </tbody>
      </table>
""",

    "torque-calculator.html": """
      <h2>Rotational Dynamics: Torque, Angular Kinematics, and Fastener Preload</h2>
      <p>Torque ($\tau$), also termed moment of force, represents the rotational analog of linear force. When a physical force $\mathbf{F}$ is applied at a displacement vector $\mathbf{r}$ relative to a fulcrum rotation axis, the resulting vector cross product creates rotational acceleration governed by <strong>Euler's Second Law of Motion</strong>:</p>
      <div class="math-block">
        $$\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F} \implies \tau = r \cdot F \cdot \sin(\theta)$$
      </div>
      <p>Where $\theta$ is the angle between the lever arm and the applied force vector. In the International System of Units (SI), torque is measured in Newton-meters ($\text{N}\cdot\text{m}$), whereas imperial engineering utilizes foot-pounds ($\text{ft}\cdot\text{lb}$) or inch-pounds ($\text{in}\cdot\text{lb}$).</p>

      <h3>Rotational Mechanical Power Formulations</h3>
      <p>The rate of mechanical work delivered by a rotating drive shaft or electric motor shaft equals torque multiplied by angular velocity ($\omega$ in radians per second):</p>
      <div class="math-block">
        $$P(\text{Watts}) = \tau(\text{N}\cdot\text{m}) \times \omega(\text{rad/s}) = \tau \times \left( \frac{2\pi \cdot N_{\text{RPM}}}{60} \right)$$
        $$\text{Imperial Horsepower: } HP = \frac{\tau(\text{ft}\cdot\text{lb}) \times N_{\text{RPM}}}{5252}$$
      </div>
      <p>At exactly $5{,}252\text{ RPM}$, engine horsepower and torque are numerically identical ($HP = \tau$) across all dynamometer testing charts!</p>

      <h3>Bolted Joint Clamping: The Torque-Tension Short Equation</h3>
      <p>In mechanical assembly, tightening a bolt applies rotational torque to stretch the bolt shank, inducing tensile clamping preload ($F_p$) that clamps joint flanges together. The torque-tension relationship is governed by the <strong>Short-Form Fastener Equation</strong>:</p>
      <div class="math-block">
        $$T = K \cdot F_p \cdot d$$
      </div>
      <p>Where $d$ is nominal bolt diameter, and $K$ is the dimensionless nut friction factor ($K \approx 0.20$ for dry steel-on-steel; $K \approx 0.15$ for cadmium plated or lightly oiled fasteners; $K \approx 0.10$ for anti-seize lubricated threads). Lubricating a dry bolt without adjusting the torque wrench setting increases bolt clamping tension by up to $100\%$, risking shank tensile yield failure!</p>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Fastener Grade & Size</th>
            <th>Nominal Tensile Strength</th>
            <th>Proof Load Clamping Tension</th>
            <th>Dry Tightening Torque (K=0.20)</th>
            <th>Lubricated Torque (K=0.15)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>M8 Metric Grade 8.8</strong></td>
            <td>800 MPa</td>
            <td>14.6 kN (3,280 lb)</td>
            <td>23.4 N·m (17.3 ft·lb)</td>
            <td>17.5 N·m (12.9 ft·lb)</td>
          </tr>
          <tr>
            <td><strong>M10 Metric Grade 8.8</strong></td>
            <td>800 MPa</td>
            <td>23.2 kN (5,215 lb)</td>
            <td>46.4 N·m (34.2 ft·lb)</td>
            <td>34.8 N·m (25.7 ft·lb)</td>
          </tr>
          <tr>
            <td><strong>M12 Metric Grade 8.8</strong></td>
            <td>800 MPa</td>
            <td>33.7 kN (7,575 lb)</td>
            <td>80.9 N·m (59.7 ft·lb)</td>
            <td>60.7 N·m (44.8 ft·lb)</td>
          </tr>
          <tr>
            <td><strong>M16 Metric Grade 10.9</strong></td>
            <td>1040 MPa</td>
            <td>88.8 kN (19,960 lb)</td>
            <td>284 N·m (209 ft·lb)</td>
            <td>213 N·m (157 ft·lb)</td>
          </tr>
          <tr>
            <td><strong>1/2"-13 SAE Grade 5</strong></td>
            <td>120 ksi</td>
            <td>12.05 kip (53.6 kN)</td>
            <td>75 ft·lb (102 N·m)</td>
            <td>56 ft·lb (76 N·m)</td>
          </tr>
        </tbody>
      </table>
""",

    "unit-converter.html": """
      <h2>Metrology, BIPM Fundamental Base Units, and Conversion Dimensionality</h2>
      <p>Scientific unit conversion is governed by the principles of metrology established by the <strong>International Bureau of Weights and Measures (BIPM)</strong> under the International System of Units (SI). In 2019, the BIPM completed a historic redefinition of all seven SI base units ($m, kg, s, A, K, mol, cd$), anchoring them permanently to invariant physical constants of nature (the speed of light $c$, Planck's constant $h$, elementary charge $e$, and the hyperfine transition frequency of Cesium-133).</p>

      <h3>Dimensional Homogeneity & Fourier Dimensional Analysis</h3>
      <p>Any physical quantity $Q$ can be expressed as a product of a numerical value $\{Q\}$ and a unit $[Q]$ ($Q = \{Q\} [Q]$). In 1822, Joseph Fourier established the principle of dimensional homogeneity: physical equations can only relate quantities possessing identical dimensional exponents across the seven base dimensions ($[M^a L^b T^c I^d \Theta^e N^f J^g]$):</p>
      <div class="math-block">
        $$\text{Pressure: } [P] = [M L^{-1} T^{-2}],\quad \text{Energy: } [E] = [M L^2 T^{-2}],\quad \text{Power: } [P] = [M L^2 T^{-3}]$$
      </div>
      <p>Converting between unit systems requires multiplying by an exact dimensional identity ratio ($1 \equiv \frac{[Q]_{\text{target}}}{[Q]_{\text{source}}}$). For example, by international treaty since 1959, the imperial inch is legally defined as exactly $1\text{ in} \equiv 0.0254\text{ meters}$, and the imperial pound-mass is defined as exactly $1\text{ lb} \equiv 0.45359237\text{ kilograms}$.</p>

      <h3>Temperature Scales: Affine vs Linear Transformations</h3>
      <p>While mass, length, and energy conversions are purely multiplicative ratio transformations ($y = m \cdot x$), thermodynamic temperature scales feature non-zero origin offsets, requiring affine linear transformations ($y = m \cdot x + b$):</p>
      <div class="math-block">
        $$T(^\circ\text{C}) = \frac{5}{9} \times (T(^\circ\text{F}) - 32),\quad T(^\circ\text{F}) = \frac{9}{5} \times T(^\circ\text{C}) + 32$$
        $$T(\text{K}) = T(^\circ\text{C}) + 273.15,\quad T(^\circ\text{R}) = T(^\circ\text{F}) + 459.67$$
      </div>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Physical Dimension</th>
            <th>SI Base Unit</th>
            <th>Standard Imperial Unit</th>
            <th>Exact Multiplicative Conversion Factor</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Length ($L$)</strong></td>
            <td>Meter ($\text{m}$)</td>
            <td>Foot ($\text{ft}$)</td>
            <td>$1\text{ ft} \equiv 0.3048\text{ m}$</td>
          </tr>
          <tr>
            <td><strong>Mass ($M$)</strong></td>
            <td>Kilogram ($\text{kg}$)</td>
            <td>Pound-mass ($\text{lb}$)</td>
            <td>$1\text{ lb} \equiv 0.45359237\text{ kg}$</td>
          </tr>
          <tr>
            <td><strong>Force ($F$)</strong></td>
            <td>Newton ($\text{N}$)</td>
            <td>Pound-force ($\text{lbf}$)</td>
            <td>$1\text{ lbf} \approx 4.4482216\text{ N}$</td>
          </tr>
          <tr>
            <td><strong>Pressure ($P$)</strong></td>
            <td>Pascal ($\text{Pa} = \text{N/m}^2$)</td>
            <td>Pounds per sq inch ($\text{psi}$)</td>
            <td>$1\text{ psi} \approx 6{,}894.757\text{ Pa}$</td>
          </tr>
          <tr>
            <td><strong>Energy ($E$)</strong></td>
            <td>Joule ($\text{J} = \text{N}\cdot\text{m}$)</td>
            <td>British Thermal Unit ($\text{Btu}$)</td>
            <td>$1\text{ Btu}_{\text{IT}} \equiv 1{,}055.056\text{ J}$</td>
          </tr>
          <tr>
            <td><strong>Power ($P$)</strong></td>
            <td>Watt ($\text{W} = \text{J/s}$)</td>
            <td>Mechanical Horsepower ($\text{HP}$)</td>
            <td>$1\text{ HP} \approx 745.6999\text{ W}$</td>
          </tr>
        </tbody>
      </table>
""",

    "voltage-drop-calculator.html": """
      <h2>Electromagnetic Theory of Line Impedance & AC Voltage Drop Formulations</h2>
      <p>Voltage drop represents the loss of electrical potential along a transmission feeder or branch circuit conductor resulting from the conductor's internal complex impedance $\mathbf{Z} = R + jX$. Under <strong>NEC Article 210.19(A) Informational Note 4</strong> and <strong>IEC 60364-5-52 Annex G</strong>, branch circuit voltage drop must not exceed $3.0\%$, and cumulative voltage drop from service equipment to the furthest outlet must remain within $5.0\%$ under full continuous load.</p>

      <h3>Vector AC Voltage Drop Equation & Power Factor Coupling</h3>
      <p>In alternating-current (AC) circuits, voltage drop is not merely a scalar product of current and resistance ($IR$). AC line inductance introduces inductive reactance $X_L = 2\pi f L$, creating a phase angle shift $\varphi$. The exact vector line-to-neutral voltage drop $\Delta V$ evaluates as:</p>
      <div class="math-block">
        $$\text{Single-Phase (2-Wire): } \Delta V = 2 \cdot I \cdot L \cdot (R \cos\varphi + X \sin\varphi)$$
        $$\text{Three-Phase (Balanced): } \Delta V = \sqrt{3} \cdot I \cdot L \cdot (R \cos\varphi + X \sin\varphi)$$
        $$\Delta V\% = \frac{\Delta V}{V_{\text{nominal}}} \times 100\%$$
      </div>
      <p>Where:</p>
      <ul>
        <li>$I$ = Circuit load current in Amperes ($A$).</li>
        <li>$L$ = One-way circuit route length in meters or feet.</li>
        <li>$R$ = Conductor AC resistance at operating temperature ($75^\circ\text{C}$ or $90^\circ\text{C}$) in $\Omega/\text{km}$ or $\Omega/1000\text{ft}$.</li>
        <li>$X$ = Conductor inductive reactance in $\Omega/\text{km}$, caused by electromagnetic spacing inside metallic conduit.</li>
        <li>$\cos\varphi$ = Operating load power factor ($\sin\varphi = \sqrt{1 - \cos^2\varphi}$).</li>
      </ul>

      <h3>Conductor Temperature Correction & Resistance Escalation</h3>
      <p>Electrical resistivity of copper and aluminum increases with conductor operating temperature. If a cable operating at elevated temperature $T_2$ is sized using cold resistance values ($T_1 = 20^\circ\text{C}$), voltage drop will be significantly underestimated:</p>
      <div class="math-block">
        $$R_{T2} = R_{T1} \left[ 1 + \alpha_{20} (T_2 - 20) \right]$$
      </div>
      <p>Where $\alpha_{20} = 0.00393 / ^\circ\text{C}$ for electrical copper. At $75^\circ\text{C}$ full load, conductor resistance is $21.6\%$ higher than at $20^\circ\text{C}$ room temperature!</p>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Conductor Size (AWG / mm²)</th>
            <th>Copper AC Resistance @ 75°C (Steel Conduit)</th>
            <th>Reactance X (Steel Conduit)</th>
            <th>Three-Phase 100A, 50m Drop (0.85 PF)</th>
            <th>Drop % on 400V 3-Phase</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>#4 AWG (21.2 mm²)</strong></td>
            <td>$1.08\ \Omega/\text{km}$</td>
            <td>$0.19\ \Omega/\text{km}$</td>
            <td>$8.83\text{ Volts}$</td>
            <td>2.21% (Compliant)</td>
          </tr>
          <tr>
            <td><strong>#2 AWG (33.6 mm²)</strong></td>
            <td>$0.69\ \Omega/\text{km}$</td>
            <td>$0.18\ \Omega/\text{km}$</td>
            <td>$5.90\text{ Volts}$</td>
            <td>1.48% (Compliant)</td>
          </tr>
          <tr>
            <td><strong>1/0 AWG (53.5 mm²)</strong></td>
            <td>$0.43\ \Omega/\text{km}$</td>
            <td>$0.17\ \Omega/\text{km}$</td>
            <td>$3.94\text{ Volts}$</td>
            <td>0.99% (Compliant)</td>
          </tr>
          <tr>
            <td><strong>4/0 AWG (107 mm²)</strong></td>
            <td>$0.22\ \Omega/\text{km}$</td>
            <td>$0.15\ \Omega/\text{km}$</td>
            <td>$2.30\text{ Volts}$</td>
            <td>0.58% (Compliant)</td>
          </tr>
        </tbody>
      </table>
""",

    "water-intake-calculator.html": """
      <h2>Renal Physiology, Osmoregulation, and Fluid Balance Dynamics</h2>
      <p>Human fluid homeostasis is regulated by the hypothalamic-pituitary-adrenal axis and renal counter-current multiplication. Total Body Water ($TBW$) accounts for approximately $60\%$ of adult male body mass and $50\% - 55\%$ of female body mass, partitioned between the intracellular fluid compartment (ICF, $67\%$) and extracellular fluid compartment (ECF, $33\%$).</p>

      <h3>Neuroendocrine Osmoregulation: Arginine Vasopressin (AVP / ADH)</h3>
      <p>Plasma osmolality is maintained within a strict physiological homeostatic setpoint of $280\text{ to } 295\text{ mOsm/kg}\cdot\text{H}_2\text{O}$. When water deficits concentrate extracellular fluids by as little as $1\% - 2\%$, hypothalamic osmoreceptors trigger two coordinated responses:</p>
      <ul>
        <li><strong>Arginine Vasopressin (ADH) Secretion:</strong> Posterior pituitary releases antidiuretic hormone, stimulating aquaporin-2 water channel insertion into renal collecting ducts, concentrating urine up to $1{,}200\text{ mOsm/kg}$.</li>
        <li><strong>Conscious Thirst Activation:</strong> Stimulates voluntary fluid ingestion to restore intravascular volume.</li>
      </ul>

      <h3>Renal Solute Load & Obligatory Urine Volume</h3>
      <p>The human kidney must excrete daily metabolic waste solutes (urea from protein catabolism, sodium, potassium, chloride) totaling approximately $600\text{ to } 900\text{ mOsm/day}$. The minimum physiological <strong>Obligatory Urine Volume</strong> required to clear this waste load without uremic toxicity is:</p>
      <div class="math-block">
        $$V_{\text{obligatory}} = \frac{\text{Daily Solute Load (mOsm)}}{\text{Max Urine Concentration (1200 mOsm/L)}} \approx \frac{600}{1200} = 0.50\text{ Liters/day}$$
      </div>
      <p>Adding insensible cutaneous evaporation ($450\text{ mL}$), respiratory expiration ($350\text{ mL}$), and fecal losses ($150\text{ mL}$) establishes an absolute baseline daily water loss of approximately $1.45\text{ Liters/day}$ under sedentary, thermoneutral resting conditions.</p>

      <table class="reference-table" style="margin: 1.5rem 0;">
        <thead>
          <tr>
            <th>Physiological Parameter / State</th>
            <th>Baseline Sedentary Adult</th>
            <th>Moderate Exercise (1 Hr)</th>
            <th>High Heat Stress / Extreme Labor</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Urine Output</strong></td>
            <td>1,200 – 1,800 mL / day</td>
            <td>1,000 – 1,400 mL / day</td>
            <td>500 – 800 mL / day (Max concentrated)</td>
          </tr>
          <tr>
            <td><strong>Sweat Secretion</strong></td>
            <td>100 – 200 mL / day</td>
            <td>800 – 1,500 mL / hr</td>
            <td>1,500 – 2,500+ mL / hr</td>
          </tr>
          <tr>
            <td><strong>Insensible (Skin & Lungs)</strong></td>
            <td>700 – 900 mL / day</td>
            <td>900 – 1,200 mL / day</td>
            <td>1,200 – 1,800 mL / day</td>
          </tr>
          <tr>
            <td><strong>Metabolic Oxidation Yield</strong></td>
            <td>~300 mL / day ($C_6H_{12}O_6 \to H_2O$)</td>
            <td>~400 mL / day</td>
            <td>~500 mL / day</td>
          </tr>
          <tr>
            <td><strong>Target Total Fluid Intake</strong></td>
            <td><strong>2.7 L (Women) / 3.7 L (Men)</strong></td>
            <td><strong>3.5 L – 4.5 L / day</strong></td>
            <td><strong>5.0 L – 8.0+ L / day (With Electrolytes)</strong></td>
          </tr>
        </tbody>
      </table>
"""
}

def expand_seed_tools():
    print(f"Expanding {len(EXPANSIONS)} seed tools to 1,100+ words...")
    success_count = 0
    for filename, new_content in EXPANSIONS.items():
        filepath = os.path.join(BASE_DIR, filename)
        if not os.path.exists(filepath):
            print(f"WARNING: {filepath} not found!")
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Check if already expanded
        if "Standards & Methodology Verification" in new_content and "Standards & Methodology Verification" in content:
            # check if title matches
            h2_match = re.search(r'<h2>(.*?)</h2>', new_content)
            if h2_match and h2_match.group(1) in content:
                print(f"Already expanded: {filename}")
                continue

        # Strategy: Insert right before the FAQ section or right before </article>
        # Look for FAQ container
        faq_match = re.search(r'(<div class="faq-(container|accordion)"|<div class="faq-item"|<h2[^>]*>Frequently Asked Questions)', content)
        if faq_match:
            insert_pos = faq_match.start()
            updated_content = content[:insert_pos] + new_content + "\n\n      " + content[insert_pos:]
        else:
            # Insert before </article>
            art_close = content.find("</article>")
            if art_close != -1:
                updated_content = content[:art_close] + new_content + "\n    " + content[art_close:]
            else:
                print(f"Error: Could not locate insertion point in {filename}")
                continue

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(updated_content)

        success_count += 1
        print(f"Successfully expanded {filename}")

    print(f"Done! {success_count} files expanded.")

if __name__ == "__main__":
    expand_seed_tools()
