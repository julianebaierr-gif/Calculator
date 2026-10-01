"""
Script to build top-notch, SEO-rich, keyword-interlinked content for index.html.
"""

import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# The rich SEO and Engineering section to insert into index.html
RICH_CONTENT_HTML = r"""
    <!-- ================================================================= -->
    <!-- SECTION 1: WHAT IS CALCHUB? (AUTHORITATIVE PLATFORM OVERVIEW)    -->
    <!-- ================================================================= -->
    <section class="article-section home-section" id="about-calchub" style="margin-top: 1rem;">
      <div class="article-header">
        <span class="category-tag">Engineering Computational Suite</span>
        <h2>What is CalcHub? The Precision Engineering, Scientific &amp; Financial Suite</h2>
        <div class="article-meta">
          <span>By CalcHub Technical Editorial Board</span>
          <span>•</span>
          <span>Verified against IEC, NEC, ASME, ASHRAE, ACI &amp; WHO Standards</span>
          <span>•</span>
          <span>Updated October 2026</span>
        </div>
      </div>

      <div class="article-summary-box">
        <strong>CalcHub</strong> (<a href="https://calchub.org/">calchub.org</a>) is a free, browser-based mathematical and engineering computational suite built on published international standards: <strong>IEC 60364</strong> (cable sizing &amp; electrical installations), <strong>NEC NFPA 70</strong> (electrical code ampacity), <strong>ASME B31</strong> (pressure piping), <strong>ASHRAE Standard 183</strong> (HVAC peak cooling loads), <strong>ACI 318</strong> (structural concrete design), <strong>ASTM A615</strong> (reinforcing rebar), and <strong>WHO / NASEM</strong> (anthropometric metabolic health). The platform provides <strong>33 specialized precision calculators</strong> organized across <strong>12 dedicated disciplines</strong>, serving practicing engineers, contractors, software developers, researchers, and students worldwide. Every calculation executes 100% client-side with zero tracking cookies and includes one-click professional PDF report generation.
      </div>

      <p>
        Modern computational work often forces professionals to choose between heavyweight, expensive CAD/software packages or simplistic, ad-hoc web widgets that fail to declare their mathematical formulas. <strong>CalcHub bridges this divide</strong> by providing open-access, standards-grade calculation engines directly inside any desktop or mobile browser. Whether sizing three-phase copper conductors for industrial distribution boards, determining room cooling tonnage under peak solar heat gain, or structuring reducing-balance loan amortization schedules, every tool on CalcHub delivers mathematical rigor, transparent step-by-step formulas, and zero server-side latency.
      </p>

      <!-- 4 Core Trust Capabilities -->
      <div class="trust-features-grid">
        <div class="trust-feature-card">
          <div class="trust-feature-icon">📜</div>
          <h3>Published Standards Compliance</h3>
          <p>All formulas strictly adhere to published regulatory standards including IEC 60364, NEC NFPA 70, ACI 318, ASHRAE 183, AWWA, and WHO guidelines with cited reference tables.</p>
        </div>
        <div class="trust-feature-card">
          <div class="trust-feature-icon">🔒</div>
          <h3>100% Client-Side Privacy</h3>
          <p>Zero telemetry tracking, zero server databases, and no login required. Your project dimensions, chemical dosages, and sensitive financial inputs never leave your device.</p>
        </div>
        <div class="trust-feature-card">
          <div class="trust-feature-icon">⚡</div>
          <h3>Instantaneous Browser Engine</h3>
          <p>Built with optimized vanilla JavaScript without heavy third-party bundles, yielding instant sub-millisecond calculation updates and full offline readiness on field jobsites.</p>
        </div>
        <div class="trust-feature-card">
          <div class="trust-feature-icon">🖨️</div>
          <h3>Professional PDF &amp; Print Export</h3>
          <p>Generate clean, audit-ready calculation summaries formatted for engineering submittal binders, municipal permit approvals, and client documentation packages.</p>
        </div>
      </div>
    </section>

    <!-- ================================================================= -->
    <!-- SECTION 2: COMPLETE DIRECTORY & STANDARDS REFERENCE (12 HUBS)    -->
    <!-- ================================================================= -->
    <section class="home-section" id="calculator-directory">
      <div class="home-section-header">
        <h2>Complete Engineering &amp; Scientific Discipline Directory</h2>
        <p>Explore all 33 certified calculators organized across 12 specialized disciplines. Each calculator is benchmarked against recognized technical standards and includes interactive unit conversion.</p>
      </div>

      <div class="directory-grid">
        
        <!-- 1. Electrical Engineering -->
        <div class="directory-card" style="border-top: 3px solid #D97706;">
          <div class="directory-card-header">
            <h3 class="directory-card-title">
              <span>⚡</span> <a href="engineering.html">Electrical Engineering</a>
            </h3>
            <span class="directory-card-badge" style="background:#FFFBEB;color:#D97706;border:1px solid #FDE68A;">IEC &amp; NEC</span>
          </div>
          <p class="directory-card-desc">
            Industrial low-voltage and medium-voltage electrical design suite. Calculate conductor ampacity via our <a href="cable-sizing-calculator.html">Cable Sizing Calculator (IEC 60364-5-52)</a>, analyze feeder impedance with the <a href="voltage-drop-calculator.html">Voltage Drop Calculator</a>, verify DC/AC power circuits using <a href="ohms-law-calculator.html">Ohm's Law Calculator</a>, and decode 4/5/6-band resistors with the <a href="resistor-color-code-calculator.html">Resistor Color Code Decoder</a>.
          </p>
          <ul class="directory-links-list">
            <li class="directory-link-item">
              <a href="cable-sizing-calculator.html"><span>🔌 Cable Sizing &amp; Current Capacity</span><span class="tool-meta">IEC 60364 / NEC</span></a>
            </li>
            <li class="directory-link-item">
              <a href="voltage-drop-calculator.html"><span>📉 Voltage Drop &amp; Feeder Length</span><span class="tool-meta">NEC 3% / 5% Limit</span></a>
            </li>
            <li class="directory-link-item">
              <a href="ohms-law-calculator.html"><span>⚡ Ohm's Law &amp; Power Wheel</span><span class="tool-meta">V = IR &amp; P = VI</span></a>
            </li>
            <li class="directory-link-item">
              <a href="resistor-color-code-calculator.html"><span>🎨 Resistor Color Code Decoder</span><span class="tool-meta">EIA 4/5/6-Band</span></a>
            </li>
          </ul>
        </div>

        <!-- 2. Solar & Renewable Energy -->
        <div class="directory-card" style="border-top: 3px solid #EA580C;">
          <div class="directory-card-header">
            <h3 class="directory-card-title">
              <span>☀️</span> <a href="solar-energy.html">Solar &amp; Renewable Energy</a>
            </h3>
            <span class="directory-card-badge" style="background:#FFF7ED;color:#EA580C;border:1px solid #FFEDD5;">IEC 61427 &amp; NEC 690</span>
          </div>
          <p class="directory-card-desc">
            Photovoltaic array design, storage sizing, and clean mobility tools. Estimate PV array peak wattages with the <a href="solar-panel-sizing-calculator.html">Solar Panel Sizing Calculator</a>, configure off-grid Ah/kWh capacity via the <a href="solar-battery-bank-calculator.html">Solar Battery Bank Calculator</a>, determine inverter continuous and surge kVA with the <a href="solar-inverter-sizing-calculator.html">Solar Inverter Sizing Calculator</a>, and calculate Level 1/2/DC charging durations using the <a href="ev-charging-time-calculator.html">EV Charging Time Calculator</a>.
          </p>
          <ul class="directory-links-list">
            <li class="directory-link-item">
              <a href="solar-panel-sizing-calculator.html"><span>☀️ Solar Panel PV Array Sizing</span><span class="tool-meta">Daily Wh / PSH</span></a>
            </li>
            <li class="directory-link-item">
              <a href="solar-battery-bank-calculator.html"><span>🔋 Solar Battery Storage Sizing</span><span class="tool-meta">Ah &amp; kWh Capacity</span></a>
            </li>
            <li class="directory-link-item">
              <a href="solar-inverter-sizing-calculator.html"><span>⚡ Solar Inverter &amp; Surge Capacity</span><span class="tool-meta">Continuous kVA</span></a>
            </li>
            <li class="directory-link-item">
              <a href="ev-charging-time-calculator.html"><span>🔌 EV Charging Time &amp; Range</span><span class="tool-meta">SAE J1772 Levels</span></a>
            </li>
          </ul>
        </div>

        <!-- 3. Mechanical & HVAC Engineering -->
        <div class="directory-card" style="border-top: 3px solid #0891B2;">
          <div class="directory-card-header">
            <h3 class="directory-card-title">
              <span>⚙️</span> <a href="mechanical.html">Mechanical &amp; HVAC</a>
            </h3>
            <span class="directory-card-badge" style="background:#ECFEFF;color:#0891B2;border:1px solid #A5F3FC;">ASHRAE &amp; ASME</span>
          </div>
          <p class="directory-card-desc">
            Thermodynamics, hydronic piping, and rotating equipment mechanics. Compute sensible and latent heat gains in BTU/hr and Refrigeration Tons (TR) with the <a href="cooling-load-calculator.html">HVAC Cooling Load Calculator (ASHRAE 183)</a>, determine fluid velocity and friction losses using the <a href="pipe-sizing-calculator.html">Pipe Sizing &amp; Water Flow Calculator (Darcy-Weisbach)</a>, and evaluate rotational drive torque and kilowatt shaft power via the <a href="torque-calculator.html">Torque &amp; Power Calculator (ISO 80000)</a>.
          </p>
          <ul class="directory-links-list">
            <li class="directory-link-item">
              <a href="cooling-load-calculator.html"><span>❄️ HVAC Cooling Load Sizing</span><span class="tool-meta">ASHRAE 183 (TR/BTU)</span></a>
            </li>
            <li class="directory-link-item">
              <a href="pipe-sizing-calculator.html"><span>🚰 Pipe Sizing &amp; Pressure Drop</span><span class="tool-meta">Darcy-Weisbach / ASME</span></a>
            </li>
            <li class="directory-link-item">
              <a href="torque-calculator.html"><span>⚙️ Torque, RPM &amp; Shaft Power</span><span class="tool-meta">ISO 80000 (N·m/kW)</span></a>
            </li>
          </ul>
        </div>

        <!-- 4. Civil & Construction Engineering -->
        <div class="directory-card" style="border-top: 3px solid #B45309;">
          <div class="directory-card-header">
            <h3 class="directory-card-title">
              <span>🏗️</span> <a href="civil.html">Civil &amp; Construction</a>
            </h3>
            <span class="directory-card-badge" style="background:#FEFCE8;color:#B45309;border:1px solid #FEF08A;">ACI 318 &amp; ASTM</span>
          </div>
          <p class="directory-card-desc">
            Structural material estimation, batching ratios, and reinforcement takeoffs. Estimate wet concrete volume in m³ and yards³ plus cement bag counts via the <a href="concrete-calculator.html">Concrete Slab &amp; Column Calculator (ACI 318)</a>, and determine linear rebar lengths, cutting schedules, and total reinforcement weight in kg and lbs using the <a href="rebar-calculator.html">Rebar Weight &amp; Grid Spacing Calculator (ASTM A615)</a>.
          </p>
          <ul class="directory-links-list">
            <li class="directory-link-item">
              <a href="concrete-calculator.html"><span>🏗️ Concrete Volume &amp; Batching</span><span class="tool-meta">ACI 318 / Cement Bags</span></a>
            </li>
            <li class="directory-link-item">
              <a href="rebar-calculator.html"><span>🔩 Rebar Weight &amp; Grid Spacing</span><span class="tool-meta">ASTM A615 (kg/lbs)</span></a>
            </li>
          </ul>
        </div>

        <!-- 5. Chemical & Water Treatment -->
        <div class="directory-card" style="border-top: 3px solid #0D9488;">
          <div class="directory-card-header">
            <h3 class="directory-card-title">
              <span>🧪</span> <a href="chemical.html">Chemical &amp; Water</a>
            </h3>
            <span class="directory-card-badge" style="background:#F0FDFA;color:#0D9488;border:1px solid #99F6E4;">AWWA &amp; EPA</span>
          </div>
          <p class="directory-card-desc">
            Municipal and industrial water treatment mass-balance engineering. Calculate exact metering pump delivery in Liters/hr and GPH based on raw water flow rate (m³/hr, MGD), active chemical percentage, and target dosage in parts per million (ppm) or mg/L using the <a href="chemical-dosing-calculator.html">Chemical Dosing Rate Calculator</a>.
          </p>
          <ul class="directory-links-list">
            <li class="directory-link-item">
              <a href="chemical-dosing-calculator.html"><span>🧪 Chemical Dosing Pump Sizing</span><span class="tool-meta">AWWA (L/hr &amp; GPH)</span></a>
            </li>
          </ul>
        </div>

        <!-- 6. Fire & Life Safety -->
        <div class="directory-card" style="border-top: 3px solid #DC2626;">
          <div class="directory-card-header">
            <h3 class="directory-card-title">
              <span>🚨</span> <a href="fire-safety.html">Fire &amp; Life Safety</a>
            </h3>
            <span class="directory-card-badge" style="background:#FEF2F2;color:#DC2626;border:1px solid #FECACA;">NFPA 72 &amp; EN 54</span>
          </div>
          <p class="directory-card-desc">
            Certified life safety and architectural fire alarm design tools. Determine detector layout spacing, maximum square coverage grids, and ceiling height derating reduction factors adhering to the National Fire Alarm and Signaling Code using the <a href="smoke-detector-spacing-calculator.html">Smoke Detector Spacing Calculator (NFPA 72)</a>.
          </p>
          <ul class="directory-links-list">
            <li class="directory-link-item">
              <a href="smoke-detector-spacing-calculator.html"><span>🚨 Smoke Detector Layout &amp; Spacing</span><span class="tool-meta">NFPA 72 Grid (9.1m)</span></a>
            </li>
          </ul>
        </div>

        <!-- 7. Programmer & Networking -->
        <div class="directory-card" style="border-top: 3px solid #4F46E5;">
          <div class="directory-card-header">
            <h3 class="directory-card-title">
              <span>👨‍💻</span> <a href="programmer.html">Programmer &amp; Networking</a>
            </h3>
            <span class="directory-card-badge" style="background:#EEF2FF;color:#4F46E5;border:1px solid #C7D2FE;">RFC 1878 &amp; IEEE</span>
          </div>
          <p class="directory-card-desc">
            Enterprise network architecture and bitwise IP calculation. Subnet IPv4 addresses across Class A, B, and C ranges, calculate CIDR prefix masks, discover network ID, broadcast IP, and usable host address boundaries with the <a href="subnet-calculator.html">IPv4 Subnet &amp; CIDR Mask Calculator (RFC 1878)</a>.
          </p>
          <ul class="directory-links-list">
            <li class="directory-link-item">
              <a href="subnet-calculator.html"><span>🌐 IPv4 Subnet &amp; CIDR Decoder</span><span class="tool-meta">RFC 1878 Host Bounds</span></a>
            </li>
          </ul>
        </div>

        <!-- 8. Finance & Investment -->
        <div class="directory-card" style="border-top: 3px solid #2563EB;">
          <div class="directory-card-header">
            <h3 class="directory-card-title">
              <span>🏦</span> <a href="finance.html">Finance &amp; Investment</a>
            </h3>
            <span class="directory-card-badge" style="background:#EFF6FF;color:#2563EB;border:1px solid #BFDBFE;">Actuarial Math</span>
          </div>
          <p class="directory-card-desc">
            Actuarial loan mechanics, wealth compounding, and retail economics. Plan debt amortization with the <a href="loan-emi-calculator.html">Loan EMI Calculator</a>, project CAGR portfolio growth with periodic deposits via the <a href="compound-interest-calculator.html">Compound Interest Calculator</a>, compute linear promissory returns using <a href="simple-interest-calculator.html">Simple Interest</a>, optimize markdown deals with the <a href="discount-calculator.html">Discount &amp; Tax Calculator</a>, and convert hourly wages to net take-home earnings with the <a href="salary-calculator.html">Salary Paycheck Calculator</a>.
          </p>
          <ul class="directory-links-list">
            <li class="directory-link-item">
              <a href="loan-emi-calculator.html"><span>🏦 Loan EMI &amp; Amortization</span><span class="tool-meta">Monthly Reducing Balance</span></a>
            </li>
            <li class="directory-link-item">
              <a href="compound-interest-calculator.html"><span>📈 Compound Interest &amp; Wealth</span><span class="tool-meta">Periodic Contributions</span></a>
            </li>
            <li class="directory-link-item">
              <a href="salary-calculator.html"><span>💼 Salary / Paycheck Converter</span><span class="tool-meta">Hourly to Annual</span></a>
            </li>
            <li class="directory-link-item">
              <a href="discount-calculator.html"><span>🏷️ Discount &amp; Retail Sales Tax</span><span class="tool-meta">Stacked Markdown Savings</span></a>
            </li>
            <li class="directory-link-item">
              <a href="simple-interest-calculator.html"><span>💰 Simple Interest Calculator</span><span class="tool-meta">I = P × R × T / 100</span></a>
            </li>
          </ul>
        </div>

        <!-- 9. Health & Fitness -->
        <div class="directory-card" style="border-top: 3px solid #059669;">
          <div class="directory-card-header">
            <h3 class="directory-card-title">
              <span>⚖️</span> <a href="health.html">Health &amp; Fitness</a>
            </h3>
            <span class="directory-card-badge" style="background:#ECFDF5;color:#059669;border:1px solid #A7F3D0;">WHO &amp; NASEM</span>
          </div>
          <p class="directory-card-desc">
            Clinical anthropometric screening and metabolic energy balance tools. Screen body weight metrics with the <a href="bmi-calculator.html">BMI Calculator (WHO Standard)</a>, determine daily calorie targets with the <a href="calorie-calculator.html">Calorie TDEE &amp; BMR Calculator (Mifflin-St Jeor)</a>, estimate body fat via circumference with the <a href="body-fat-calculator.html">Body Fat Calculator (US Navy)</a>, analyze medical weight goals using the <a href="ideal-weight-calculator.html">Ideal Body Weight Calculator (Devine)</a>, and track fluid requirements with the <a href="water-intake-calculator.html">Daily Water Intake Calculator (NASEM)</a>.
          </p>
          <ul class="directory-links-list">
            <li class="directory-link-item">
              <a href="bmi-calculator.html"><span>⚖️ Body Mass Index (BMI)</span><span class="tool-meta">WHO Metric &amp; Imperial</span></a>
            </li>
            <li class="directory-link-item">
              <a href="calorie-calculator.html"><span>🔥 Calorie TDEE &amp; Basal BMR</span><span class="tool-meta">Mifflin-St Jeor Formula</span></a>
            </li>
            <li class="directory-link-item">
              <a href="body-fat-calculator.html"><span>📏 Body Fat Percentage</span><span class="tool-meta">US Navy Circumference</span></a>
            </li>
            <li class="directory-link-item">
              <a href="ideal-weight-calculator.html"><span>❤️ Ideal Body Weight Targets</span><span class="tool-meta">Devine / Robinson / Miller</span></a>
            </li>
            <li class="directory-link-item">
              <a href="water-intake-calculator.html"><span>💧 Daily Water Hydration Norms</span><span class="tool-meta">NASEM Fluid Norms</span></a>
            </li>
          </ul>
        </div>

        <!-- 10. Mathematics & Utilities -->
        <div class="directory-card" style="border-top: 3px solid #7C3AED;">
          <div class="directory-card-header">
            <h3 class="directory-card-title">
              <span>🔢</span> <a href="math.html">Mathematics &amp; Utilities</a>
            </h3>
            <span class="directory-card-badge" style="background:#F5F3FF;color:#7C3AED;border:1px solid #DDD6FE;">Pure Arithmetic</span>
          </div>
          <p class="directory-card-desc">
            Exact numerical problem-solving, academic evaluations, and proportional mechanics. Solve percentage increases and changes with the <a href="percentage-calculator.html">Percentage Calculator</a>, calculate chronological years, months, and days with the <a href="age-calculator.html">Exact Age Calculator</a>, evaluate cumulative weighted credits via the <a href="gpa-calculator.html">College GPA Calculator (4.0 Scale)</a>, add and simplify fractions with the <a href="fraction-calculator.html">Fraction Calculator</a>, and scale proportions using the <a href="ratio-calculator.html">Ratio Simplifier</a>.
          </p>
          <ul class="directory-links-list">
            <li class="directory-link-item">
              <a href="percentage-calculator.html"><span>🔢 Percentage Increase &amp; Difference</span><span class="tool-meta">Multi-Scenario Solver</span></a>
            </li>
            <li class="directory-link-item">
              <a href="age-calculator.html"><span>🎂 Exact Chronological Age</span><span class="tool-meta">Years, Months, Days</span></a>
            </li>
            <li class="directory-link-item">
              <a href="gpa-calculator.html"><span>🎓 College &amp; High School GPA</span><span class="tool-meta">4.0 Weighted Credits</span></a>
            </li>
            <li class="directory-link-item">
              <a href="fraction-calculator.html"><span>½ Fraction Arithmetic &amp; Reduction</span><span class="tool-meta">Proper &amp; Mixed Numbers</span></a>
            </li>
            <li class="directory-link-item">
              <a href="ratio-calculator.html"><span>➗ Ratio Simplifier &amp; Scaling</span><span class="tool-meta">A:B = C:D Resolution</span></a>
            </li>
          </ul>
        </div>

        <!-- 11. Date & Time Utilities -->
        <div class="directory-card" style="border-top: 3px solid #0284C7;">
          <div class="directory-card-header">
            <h3 class="directory-card-title">
              <span>📅</span> <a href="datetime.html">Date &amp; Time Utilities</a>
            </h3>
            <span class="directory-card-badge" style="background:#F0F9FF;color:#0284C7;border:1px solid #BAE6FD;">ISO 8601</span>
          </div>
          <p class="directory-card-desc">
            Gregorian calendar durations and project scheduling mathematics. Calculate total elapsed days, calendar weeks, and precise business working days (excluding Saturdays and Sundays) between any two dates with the <a href="date-difference-calculator.html">Date Difference &amp; Workdays Calculator (ISO 8601)</a>.
          </p>
          <ul class="directory-links-list">
            <li class="directory-link-item">
              <a href="date-difference-calculator.html"><span>📅 Date Difference &amp; Working Days</span><span class="tool-meta">ISO 8601 Calendar</span></a>
            </li>
          </ul>
        </div>

        <!-- 12. Universal Converters -->
        <div class="directory-card" style="border-top: 3px solid #9333EA;">
          <div class="directory-card-header">
            <h3 class="directory-card-title">
              <span>🔄</span> <a href="converter.html">Universal Converters</a>
            </h3>
            <span class="directory-card-badge" style="background:#FAF5FF;color:#9333EA;border:1px solid #E9D5FF;">NIST &amp; BIPM</span>
          </div>
          <p class="directory-card-desc">
            Universal bidirectional scientific and engineering unit conversion engine. Seamlessly convert between SI metric and US Customary / Imperial systems across length (m, ft, in, mm), weight &amp; mass (kg, lb, oz), temperature (°C, °F, K), pressure (bar, psi, kPa), area, and volume with the <a href="unit-converter.html">Universal Multi-Unit Converter</a>.
          </p>
          <ul class="directory-links-list">
            <li class="directory-link-item">
              <a href="unit-converter.html"><span>🔄 Universal Multi-Unit Converter</span><span class="tool-meta">Length, Mass, Temp, Press</span></a>
            </li>
          </ul>
        </div>

      </div>
    </section>

    <!-- ================================================================= -->
    <!-- SECTION 3: SPOTLIGHT ON FREQUENTLY USED ENGINEERING CALCULATORS   -->
    <!-- ================================================================= -->
    <section class="home-section" id="frequently-used-calculators">
      <div class="home-section-header">
        <h2>Frequently Used Engineering &amp; Scientific Calculators</h2>
        <p>In-depth technical overviews of our most-requested computational tools. Grounded in certified engineering formulas, ready for instant field execution.</p>
      </div>

      <div class="spotlight-grid">
        
        <!-- Spotlight 1: Cable Sizing -->
        <div class="spotlight-card">
          <div class="spotlight-card-header">
            <span class="spotlight-tag" style="background:#FFFBEB;color:#D97706;border:1px solid #FDE68A;">Electrical</span>
            <span style="font-size:0.8rem;color:#64748B;">IEC 60364-5-52</span>
          </div>
          <h3><a href="cable-sizing-calculator.html">Cable Sizing &amp; Conductor Ampacity</a></h3>
          <p>
            Determines the minimum permissible cross-sectional conductor area (mm² / AWG) for single-phase and three-phase circuits. Evaluates continuous load currents, automatic thermal correction derating factors (Ca), grouping proximity coefficients (Cg), and ensures voltage drop remains strictly below international statutory limits (3% for lighting, 5% for general motive power).
          </p>
          <div class="spotlight-formula">
            I_z = I_b / (C_a × C_g × C_d) &nbsp;·&nbsp; ΔV = √3 × I × L × (R·cosφ + X·sinφ)
          </div>
          <a href="cable-sizing-calculator.html" class="spotlight-btn">Launch Cable Sizing Calculator &rarr;</a>
        </div>

        <!-- Spotlight 2: Ohm's Law -->
        <div class="spotlight-card">
          <div class="spotlight-card-header">
            <span class="spotlight-tag" style="background:#FFFBEB;color:#D97706;border:1px solid #FDE68A;">Electronics</span>
            <span style="font-size:0.8rem;color:#64748B;">DC / AC Power Wheel</span>
          </div>
          <h3><a href="ohms-law-calculator.html">Ohm's Law &amp; Electrical Power Wheel</a></h3>
          <p>
            Solves any two unknown parameters given voltage (V), current intensity (I), resistance (R), and active power (P). Essential for circuit diagnostics, sizing protection fuses, determining resistor power ratings to prevent thermal breakdown, and verifying voltage divider networks in electronic engineering.
          </p>
          <div class="spotlight-formula">
            V = I × R &nbsp;·&nbsp; P = V × I = I²R = V² / R
          </div>
          <a href="ohms-law-calculator.html" class="spotlight-btn">Launch Ohm's Law Calculator &rarr;</a>
        </div>

        <!-- Spotlight 3: Loan EMI -->
        <div class="spotlight-card">
          <div class="spotlight-card-header">
            <span class="spotlight-tag" style="background:#EFF6FF;color:#2563EB;border:1px solid #BFDBFE;">Finance</span>
            <span style="font-size:0.8rem;color:#64748B;">Amortization Schedule</span>
          </div>
          <h3><a href="loan-emi-calculator.html">Loan EMI &amp; Debt Amortization</a></h3>
          <p>
            Calculates exact monthly repayments on reducing-balance home mortgages, auto loans, and commercial financing facilities. Dynamically visualizes the gradual mathematical shift from early heavy interest deductions toward rapid late-tenure principal reduction, enabling borrowers to compare total borrowing costs.
          </p>
          <div class="spotlight-formula">
            EMI = [P × r × (1 + r)ⁿ] / [(1 + r)ⁿ - 1]
          </div>
          <a href="loan-emi-calculator.html" class="spotlight-btn">Launch Loan EMI Calculator &rarr;</a>
        </div>

        <!-- Spotlight 4: BMI -->
        <div class="spotlight-card">
          <div class="spotlight-card-header">
            <span class="spotlight-tag" style="background:#ECFDF5;color:#059669;border:1px solid #A7F3D0;">Health</span>
            <span style="font-size:0.8rem;color:#64748B;">WHO Standards</span>
          </div>
          <h3><a href="bmi-calculator.html">Body Mass Index (BMI) &amp; Body Composition</a></h3>
          <p>
            Epidemiological body mass index evaluation adhering to World Health Organization (WHO) international classification thresholds. Computes clinical BMI in metric and imperial units, calculates BMI Prime, and projects exact kilograms or pounds required to achieve a healthy weight boundary (18.5 to 24.9 kg/m²).
          </p>
          <div class="spotlight-formula">
            BMI = weight (kg) / [height (m)]² &nbsp;·&nbsp; Imperial: (lbs × 703) / in²
          </div>
          <a href="bmi-calculator.html" class="spotlight-btn">Launch BMI Calculator &rarr;</a>
        </div>

        <!-- Spotlight 5: Cooling Load -->
        <div class="spotlight-card">
          <div class="spotlight-card-header">
            <span class="spotlight-tag" style="background:#ECFEFF;color:#0891B2;border:1px solid #A5F3FC;">Mechanical</span>
            <span style="font-size:0.8rem;color:#64748B;">ASHRAE Standard 183</span>
          </div>
          <h3><a href="cooling-load-calculator.html">HVAC Cooling Load &amp; Tonnage Sizing</a></h3>
          <p>
            Sizes air conditioning equipment capacity by calculating peak sensible heat gain through exterior building walls, roof conduction, window solar heat gain coefficients (SHGC), occupants, and electrical equipment. Converts gross thermal demand into British Thermal Units per hour (BTU/hr) and Refrigeration Tonnage (TR).
          </p>
          <div class="spotlight-formula">
            Q = U × A × ΔT &nbsp;·&nbsp; Tonnage (TR) = Total BTU/hr / 12,000
          </div>
          <a href="cooling-load-calculator.html" class="spotlight-btn">Launch Cooling Load Calculator &rarr;</a>
        </div>

        <!-- Spotlight 6: Concrete Slab -->
        <div class="spotlight-card">
          <div class="spotlight-card-header">
            <span class="spotlight-tag" style="background:#FEFCE8;color:#B45309;border:1px solid #FEF08A;">Civil</span>
            <span style="font-size:0.8rem;color:#64748B;">ACI 318 Standard</span>
          </div>
          <h3><a href="concrete-calculator.html">Concrete Slab Volume &amp; Material Batching</a></h3>
          <p>
            Estimates wet concrete volume in cubic meters (m³) and cubic yards (yd³) for residential foundations, structural slabs, and reinforced columns. Applies the industry-standard 1.54× dry volume volumetric expansion factor to compute exact 50kg cement bag counts, dry sand, and coarse gravel weights for 1:2:4 nominal mix designs.
          </p>
          <div class="spotlight-formula">
            Wet Vol = L × W × H &nbsp;·&nbsp; Dry Batch Vol = Wet Vol × 1.54
          </div>
          <a href="concrete-calculator.html" class="spotlight-btn">Launch Concrete Calculator &rarr;</a>
        </div>

      </div>
    </section>

    <!-- ================================================================= -->
    <!-- SECTION 4: STANDARDS & COMPLIANCE VERIFICATION MATRIX            -->
    <!-- ================================================================= -->
    <section class="article-section home-section" id="standards-matrix">
      <div class="article-header">
        <span class="category-tag">Regulatory Verification</span>
        <h2>Published Standards &amp; Engineering Regulatory Compliance Matrix</h2>
        <div class="article-meta">
          <span>Benchmarked against International Electrical, Mechanical, Civil &amp; Health Bodies</span>
        </div>
      </div>

      <p>
        Every calculation formula implemented on CalcHub is derived directly from published consensus engineering codes and scientific literature. The table below outlines the core standards implemented across our platform:
      </p>

      <div class="data-table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Standard Code</th>
              <th>Issuing Organization</th>
              <th>Technical Scope &amp; Methodology</th>
              <th>Implemented Calculator</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>IEC 60364-5-52</strong></td>
              <td>International Electrotechnical Commission</td>
              <td>Current-carrying capacities, conductor installation methods &amp; thermal derating factors (Ca, Cg).</td>
              <td><a href="cable-sizing-calculator.html">Cable Sizing Calculator</a></td>
            </tr>
            <tr>
              <td><strong>NEC NFPA 70</strong></td>
              <td>National Fire Protection Association (USA)</td>
              <td>National Electrical Code feeder ampacity tables, conductor impedance, and 3%/5% voltage drop thresholds.</td>
              <td><a href="voltage-drop-calculator.html">Voltage Drop Calculator</a></td>
            </tr>
            <tr>
              <td><strong>ASHRAE 183</strong></td>
              <td>American Society of Heating &amp; Air-Conditioning</td>
              <td>Peak cooling and heating load calculation principles for nonresidential and commercial buildings.</td>
              <td><a href="cooling-load-calculator.html">Cooling Load Calculator</a></td>
            </tr>
            <tr>
              <td><strong>ASME B31 / Darcy</strong></td>
              <td>American Society of Mechanical Engineers</td>
              <td>Pressure piping diameter optimization, fluid Reynolds numbers, and Darcy-Weisbach head loss friction factors.</td>
              <td><a href="pipe-sizing-calculator.html">Pipe Sizing &amp; Flow</a></td>
            </tr>
            <tr>
              <td><strong>ACI 318 / BS EN 206</strong></td>
              <td>American Concrete Institute / European Norm</td>
              <td>Structural concrete volumetric batching, aggregate proportions (1:2:4), and 50kg cement bag takeoffs.</td>
              <td><a href="concrete-calculator.html">Concrete Volume Sizing</a></td>
            </tr>
            <tr>
              <td><strong>ASTM A615 / Eurocode 2</strong></td>
              <td>ASTM International / CEN</td>
              <td>Deformed and plain carbon-steel rebar linear mass density (D²/162.2) and structural spacing.</td>
              <td><a href="rebar-calculator.html">Rebar Weight &amp; Grid</a></td>
            </tr>
            <tr>
              <td><strong>NFPA 72 &amp; EN 54-7</strong></td>
              <td>National Fire Protection Association</td>
              <td>Smoke detector radial coverage (9.1m square grid) and ceiling height reduction derating coefficients.</td>
              <td><a href="smoke-detector-spacing-calculator.html">Smoke Detector Spacing</a></td>
            </tr>
            <tr>
              <td><strong>AWWA &amp; EPA</strong></td>
              <td>American Water Works Association</td>
              <td>Water treatment coagulation and disinfection active solution metering pump delivery rates (L/hr &amp; GPH).</td>
              <td><a href="chemical-dosing-calculator.html">Chemical Dosing Rate</a></td>
            </tr>
            <tr>
              <td><strong>RFC 1878 &amp; IEEE</strong></td>
              <td>Internet Engineering Task Force</td>
              <td>Variable Length Subnet Masking (VLSM), Classless Inter-Domain Routing (CIDR), and IP host bounds.</td>
              <td><a href="subnet-calculator.html">IPv4 Subnet Calculator</a></td>
            </tr>
            <tr>
              <td><strong>WHO Standards</strong></td>
              <td>World Health Organization</td>
              <td>International epidemiological anthropometric thresholds (18.5, 25.0, 30.0 kg/m²) for adult health.</td>
              <td><a href="bmi-calculator.html">BMI Calculator</a></td>
            </tr>
            <tr>
              <td><strong>NIST &amp; BIPM</strong></td>
              <td>Bureau International des Poids et Mesures</td>
              <td>Exact physical constants and SI base units for length, mass, thermodynamics, pressure, and volume.</td>
              <td><a href="unit-converter.html">Universal Unit Converter</a></td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- ================================================================= -->
    <!-- SECTION 5: FREQUENTLY ASKED QUESTIONS (FAQ)                      -->
    <!-- ================================================================= -->
    <section class="article-section home-section" id="faq-section">
      <div class="article-header">
        <span class="category-tag">Knowledge Base</span>
        <h2>Frequently Asked Questions About CalcHub</h2>
        <div class="article-meta">
          <span>Answers on calculation accuracy, privacy, PDF reports, and offline access</span>
        </div>
      </div>

      <div class="faq-container">
        
        <details class="faq-item" open>
          <summary>How does CalcHub ensure calculations match engineering standards?</summary>
          <div class="faq-content">
            Every calculator on CalcHub is programmed using published formulas from recognized standard bodies including the International Electrotechnical Commission (IEC 60364), the National Fire Protection Association (NFPA 70 &amp; 72), the American Concrete Institute (ACI 318), ASHRAE Standard 183, and the World Health Organization (WHO). Each tool explicitly displays its underlying mathematical formulas, parameter ranges, and reference citations directly below the interactive workspace.
          </div>
        </details>

        <details class="faq-item">
          <summary>Does CalcHub store my engineering inputs or sensitive financial information?</summary>
          <div class="faq-content">
            No. CalcHub operates on a 100% client-side privacy architecture. All mathematical evaluations execute purely inside your device's web browser using vanilla JavaScript. We do not transmit, log, record, or store any of your dimensions, loan amounts, physiological data, or chemical dosages on external databases.
          </div>
        </details>

        <details class="faq-item">
          <summary>How do I export my calculation results to a formal PDF report?</summary>
          <div class="faq-content">
            Every calculator workspace includes a dedicated <strong>"🖨️ Print Report"</strong> button. Clicking this triggers your browser's native print engine with an optimized CSS print stylesheet that automatically hides navigation menus, ads, and sidebars, outputting a formal document with a clean title header, detailed inputs, calculated figures with engineering units, and a timestamp. You can select "Save as PDF" to store the file directly.
          </div>
        </details>

        <details class="faq-item">
          <summary>Are all calculators on CalcHub completely free to use?</summary>
          <div class="faq-content">
            Yes. All 33 calculators across all 12 disciplines are 100% free with unlimited usage. There are no paywalls, premium tiers, locked features, or mandatory registration barriers. Professionals, contractors, researchers, and students have unrestricted open access at all times.
          </div>
        </details>

        <details class="faq-item">
          <summary>Can CalcHub calculators be used offline on field jobsites?</summary>
          <div class="faq-content">
            Yes. Because CalcHub tools require zero server round-trips for calculation execution, once any page is loaded in your mobile or desktop web browser, the calculation logic remains fully functional even if internet connectivity drops on remote construction sites or industrial plant floors.
          </div>
        </details>

        <details class="faq-item">
          <summary>How are units handled across metric and imperial systems?</summary>
          <div class="faq-content">
            Tools that involve physical dimensions (such as our BMI Calculator, Cable Sizing, Cooling Load, and Concrete Sizing) feature built-in unit switchers allowing seamless toggling between Metric units (meters, millimeters, kilograms, kW, °C) and US Customary / Imperial units (feet, inches, pounds, BTU, °F) with dynamic real-time recalculation.
          </div>
        </details>

      </div>
    </section>
"""

def update_homepage():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # Expand the FAQPage schema in index.html to include all 6 questions
    faq_schema = '''      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "How does CalcHub ensure calculations match engineering standards?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Every calculator on CalcHub is programmed using published formulas from recognized standard bodies including IEC 60364, NFPA 70 & 72, ACI 318, ASHRAE Standard 183, and WHO. Each tool displays its underlying mathematical formulas, parameter ranges, and reference citations."
            }
          },
          {
            "@type": "Question",
            "name": "Does CalcHub store my engineering inputs or sensitive financial information?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "No. CalcHub operates on a 100% client-side privacy architecture. All mathematical evaluations execute purely inside your device's web browser using vanilla JavaScript. No dimensions or financial inputs are transmitted to external servers."
            }
          },
          {
            "@type": "Question",
            "name": "How do I export my calculation results to a formal PDF report?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Every calculator includes a dedicated Print Report button that triggers an optimized CSS print stylesheet to output a formal document with clean title headers, detailed inputs, calculated figures with engineering units, and a timestamp."
            }
          },
          {
            "@type": "Question",
            "name": "Are all calculators on CalcHub completely free to use?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes. All 33 calculators across all 12 disciplines are 100% free with unlimited usage, with zero paywalls, locked features, or mandatory registration barriers."
            }
          },
          {
            "@type": "Question",
            "name": "Can CalcHub calculators be used offline on field jobsites?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes. Because CalcHub tools require zero server round-trips for calculation execution, once loaded in your browser, the calculation logic remains fully functional without an active internet connection."
            }
          },
          {
            "@type": "Question",
            "name": "How are units handled across metric and imperial systems?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Tools that involve physical dimensions feature built-in unit switchers allowing seamless toggling between Metric units (meters, millimeters, kilograms, kW, °C) and US Customary / Imperial units (feet, inches, pounds, BTU, °F)."
            }
          }
        ]
      }'''

    schema_pattern = re.compile(r'\{\s*"@type":\s*"FAQPage".*?\}\s*\]\s*\}', re.DOTALL)
    if schema_pattern.search(html):
        html = schema_pattern.sub(lambda m: faq_schema + '\n    ]\n  }', html)
        print("Updated JSON-LD FAQPage schema successfully.")

    # In index.html, replace the incomplete filter & block sections and small geo box with the new master content
    replace_pattern = re.compile(r'<!--\s*Category Filter Bar\s*-->.*?</main>', re.DOTALL)
    
    if replace_pattern.search(html):
        new_main_content = RICH_CONTENT_HTML.strip() + "\n\n  </main>"
        html = replace_pattern.sub(lambda m: new_main_content, html)
        print("Replaced main content with new SEO & Engineering architecture.")
    else:
        print("Warning: replace pattern for main content not found!")
        return

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("index.html updated successfully!")

if __name__ == "__main__":
    update_homepage()
