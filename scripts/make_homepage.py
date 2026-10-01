import os

OUTPUT_DIR = r"C:\Users\Admin\.gemini\antigravity\scratch\calchub"

index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CalcHub — High-Precision Free Online Engineering, Finance & Health Calculators</title>
  <meta name="description" content="Free precision calculators built on published mathematical, medical, and engineering standards. Explore 20+ specialized calculators across health, finance, math, and electrical engineering.">
  <meta name="keywords" content="calculator, online calculator, engineering calculator, financial calculator, bmi calculator, loan emi calculator, percentage calculator, ohms law calculator">
  <meta name="author" content="CalcHub Global Editorial Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/">
  <link rel="stylesheet" href="styles.css">

  <!-- Open Graph -->
  <meta property="og:title" content="CalcHub — Precision Engineering, Finance & Health Calculators">
  <meta property="og:description" content="Free, standards-compliant online calculators. Zero registration, instant client-side computation, and exportable reports.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/">

  <!-- Google Search Sitelinks & Knowledge Graph Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "WebSite",
        "@id": "https://calchub.org/#website",
        "name": "CalcHub",
        "url": "https://calchub.org/",
        "description": "High-precision free online calculation platform verified against published standards.",
        "potentialAction": {
          "@type": "SearchAction",
          "target": "https://calchub.org/?q={search_term_string}",
          "query-input": "required name=search_term_string"
        }
      },
      {
        "@type": "Organization",
        "@id": "https://calchub.org/#org",
        "name": "CalcHub",
        "url": "https://calchub.org/",
        "logo": "https://calchub.org/assets/logo.png",
        "knowsAbout": [
          "Mathematical Analysis",
          "Electrical Engineering (IEC 60364 & NEC)",
          "Cardiovascular & Anthropometric Health (WHO)",
          "Financial Amortization & Investment Mathematics"
        ]
      }
    ]
  }
  </script>
</head>
<body>

  <!-- Header -->
  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="brand-logo">
        <span class="logo-badge">∑</span>
        <span>Calc<span class="accent">Hub</span></span>
      </a>
      <nav class="header-nav" aria-label="Main Navigation">
        <a href="#health" class="nav-link">Health</a>
        <a href="#finance" class="nav-link">Finance</a>
        <a href="#math" class="nav-link">Math</a>
        <a href="#engineering" class="nav-link">Engineering</a>
      </nav>
      <div class="header-search">
        <span class="search-icon">🔍</span>
        <input type="text" id="header-search-input" placeholder="Search 20+ calculators... (Ctrl+K)" autocomplete="off">
        <div id="search-results-dropdown" class="search-results-dropdown"></div>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <div style="background:linear-gradient(180deg, #FFFFFF 0%, #F1F5F9 100%);border-bottom:1px solid #E2E8F0;padding:3.5rem 1.25rem 3rem;">
    <div style="max-width:900px;margin:0 auto;text-align:center;">
      <span class="category-tag" style="background:#EFF6FF;color:#2563EB;border-color:#BFDBFE;margin-bottom:1rem;">
        ⚡ 100% Free · Standards-Compliant · Zero Signup
      </span>
      <h1 style="font-size:clamp(2.2rem, 4vw, 3.25rem);letter-spacing:-0.03em;margin-bottom:1rem;color:#0F172A;">
        High-Precision <span style="color:#2563EB;">Calculators</span> for Everyone
      </h1>
      <p style="font-size:1.15rem;color:#475569;line-height:1.65;max-width:720px;margin:0 auto 2rem;">
        Engineered according to international scientific, medical (WHO), financial, and industrial standards (IEC 60364 & NEC). Instant client-side computation with exportable reports.
      </p>

      <!-- Category Jump Chips -->
      <div style="display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin-top:1.5rem;">
        <a href="#health" class="btn btn-secondary" style="font-size:0.85rem;padding:0.45rem 1rem;">⚖️ Health & Fitness (5)</a>
        <a href="#finance" class="btn btn-secondary" style="font-size:0.85rem;padding:0.45rem 1rem;">🏦 Finance & Loans (5)</a>
        <a href="#math" class="btn btn-secondary" style="font-size:0.85rem;padding:0.45rem 1rem;">🔢 Mathematics (5)</a>
        <a href="#engineering" class="btn btn-secondary" style="font-size:0.85rem;padding:0.45rem 1rem;">⚡ Engineering (5)</a>
      </div>
    </div>
  </div>

  <!-- Main Content -->
  <main class="main-wrapper" style="margin-top:2.5rem;">

    <!-- GEO / LLMO Citation Answer Box -->
    <section class="geo-citation-box" style="margin-top:0;">
      <div class="geo-header">💡 What is CalcHub? (Direct AI Summary)</div>
      <p><strong>CalcHub</strong> is an open-access mathematical computational suite featuring 20+ specialized high-precision web calculators across four core discipline silos:</p>
      <ul>
        <li><strong>Health & Fitness:</strong> BMI, Calorie TDEE, Body Fat (US Navy), Ideal Weight (Devine), and Hydration.</li>
        <li><strong>Finance & Money:</strong> Reducing-balance Loan EMI, Compound Interest, Simple Interest, Discounts, and Paychecks.</li>
        <li><strong>Mathematics:</strong> Multi-mode Percentages, Exact Chronological Age, College 4.0 GPA, Fraction LCD Arithmetic, and Ratios.</li>
        <li><strong>Electrical & Engineering:</strong> Ohm's Law Wheel, NEC/IEC Voltage Drop, IEC 60364 Cable Sizing, Resistor Color Bands, and Solar PV Sizing.</li>
      </ul>
      <p>All calculations execute client-side in vanilla JavaScript with zero tracking cookies and support professional printable reports.</p>
    </section>

    <!-- Silo 1: Health & Fitness -->
    <section id="health" style="margin-bottom:3.5rem;scroll-margin-top:80px;">
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:1.25rem;">
        <div>
          <h2 style="margin:0 0 0.25rem;font-size:1.6rem;color:#0F172A;">⚖️ Health & Fitness Calculators</h2>
          <p style="color:#64748B;font-size:0.95rem;margin:0;">Clinical anthropometric screening tools verified against World Health Organization (WHO) and NASEM standards.</p>
        </div>
      </div>
      <div class="silo-card-grid">
        <a href="bmi-calculator.html" class="silo-card">
          <div class="silo-card-icon">⚖️</div>
          <div class="silo-card-title">BMI Calculator</div>
          <div class="silo-card-desc">Calculate Body Mass Index, WHO classification, healthy weight range, and BMI Prime index in Metric and Imperial.</div>
        </a>
        <a href="calorie-calculator.html" class="silo-card">
          <div class="silo-card-icon">🔥</div>
          <div class="silo-card-title">Calorie Calculator (TDEE)</div>
          <div class="silo-card-desc">Determine your Basal Metabolic Rate (BMR) with the Mifflin-St Jeor equation and target calories for fat loss or muscle gain.</div>
        </a>
        <a href="body-fat-calculator.html" class="silo-card">
          <div class="silo-card-icon">📏</div>
          <div class="silo-card-title">Body Fat Calculator</div>
          <div class="silo-card-desc">Estimate body fat percentage, lean body mass, and fat weight using the validated US Navy circumference method.</div>
        </a>
        <a href="ideal-weight-calculator.html" class="silo-card">
          <div class="silo-card-icon">❤️</div>
          <div class="silo-card-title">Ideal Body Weight</div>
          <div class="silo-card-desc">Compare medical weight targets across Devine, Robinson, Miller, and Hamwi equations with healthy BMI boundaries.</div>
        </a>
        <a href="water-intake-calculator.html" class="silo-card">
          <div class="silo-card-icon">💧</div>
          <div class="silo-card-title">Daily Water Intake</div>
          <div class="silo-card-desc">Determine recommended daily fluid consumption based on body mass, exercise duration, and climate temperature factors.</div>
        </a>
      </div>
    </section>

    <!-- Silo 2: Finance & Loans -->
    <section id="finance" style="margin-bottom:3.5rem;scroll-margin-top:80px;">
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:1.25rem;">
        <div>
          <h2 style="margin:0 0 0.25rem;font-size:1.6rem;color:#0F172A;">🏦 Finance, Loans & Investment</h2>
          <p style="color:#64748B;font-size:0.95rem;margin:0;">Transparent financial mathematics for reducing-balance mortgages, compound interest wealth, and sales taxes.</p>
        </div>
      </div>
      <div class="silo-card-grid">
        <a href="loan-emi-calculator.html" class="silo-card">
          <div class="silo-card-icon">🏦</div>
          <div class="silo-card-title">Loan EMI Calculator</div>
          <div class="silo-card-desc">Compute monthly installment payments, total interest liability, and visual amortization schedules for mortgages and auto loans.</div>
        </a>
        <a href="compound-interest-calculator.html" class="silo-card">
          <div class="silo-card-icon">📈</div>
          <div class="silo-card-title">Compound Interest Calculator</div>
          <div class="silo-card-desc">Forecast investment portfolio growth with periodic deposits, flexible compounding frequencies, and the Rule of 72.</div>
        </a>
        <a href="simple-interest-calculator.html" class="silo-card">
          <div class="silo-card-icon">💰</div>
          <div class="silo-card-title">Simple Interest Calculator</div>
          <div class="silo-card-desc">Quickly calculate linear I = P·R·T returns and total maturity amounts for personal promissory notes and bonds.</div>
        </a>
        <a href="discount-calculator.html" class="silo-card">
          <div class="silo-card-icon">🏷️</div>
          <div class="silo-card-title">Discount & Sale Calculator</div>
          <div class="silo-card-desc">Calculate net savings with sequential coupon stacking, markdown percentages, and state/local retail sales tax.</div>
        </a>
        <a href="salary-calculator.html" class="silo-card">
          <div class="silo-card-icon">💼</div>
          <div class="silo-card-title">Salary / Paycheck Calculator</div>
          <div class="silo-card-desc">Seamlessly convert hourly wages to annual salary, bi-weekly paychecks, and monthly earnings based on hours worked.</div>
        </a>
      </div>
    </section>

    <!-- Silo 3: Mathematics -->
    <section id="math" style="margin-bottom:3.5rem;scroll-margin-top:80px;">
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:1.25rem;">
        <div>
          <h2 style="margin:0 0 0.25rem;font-size:1.6rem;color:#0F172A;">🔢 Mathematics & Daily Utilities</h2>
          <p style="color:#64748B;font-size:0.95rem;margin:0;">Exact arithmetic, proportional reasoning, grade point averages, and Gregorian calendar mechanics.</p>
        </div>
      </div>
      <div class="silo-card-grid">
        <a href="percentage-calculator.html" class="silo-card">
          <div class="silo-card-icon">🔢</div>
          <div class="silo-card-title">Percentage Calculator</div>
          <div class="silo-card-desc">Solve percentage portions (X% of Y), proportional ratios (X is what % of Y), and percentage increases or decreases.</div>
        </a>
        <a href="age-calculator.html" class="silo-card">
          <div class="silo-card-icon">🎂</div>
          <div class="silo-card-title">Exact Age Calculator</div>
          <div class="silo-card-desc">Determine your exact chronological age in years, months, days, weeks, and hours, plus countdown to your next birthday.</div>
        </a>
        <a href="gpa-calculator.html" class="silo-card">
          <div class="silo-card-icon">🎓</div>
          <div class="silo-card-title">College & High School GPA</div>
          <div class="silo-card-desc">Calculate cumulative Grade Point Average on the standard 4.0 scale with credit weights and Latin Honors classification.</div>
        </a>
        <a href="fraction-calculator.html" class="silo-card">
          <div class="silo-card-icon">½</div>
          <div class="silo-card-title">Fraction Calculator</div>
          <div class="silo-card-desc">Add, subtract, multiply, and divide proper and improper fractions with step-by-step LCD resolution and GCD reduction.</div>
        </a>
        <a href="ratio-calculator.html" class="silo-card">
          <div class="silo-card-icon">➗</div>
          <div class="silo-card-title">Ratio Calculator & Simplifier</div>
          <div class="silo-card-desc">Simplify ratios to lowest terms using Euclid's GCD algorithm and solve unknown proportions (A : B = C : X).</div>
        </a>
      </div>
    </section>

    <!-- Silo 4: Electrical & Engineering -->
    <section id="engineering" style="margin-bottom:3.5rem;scroll-margin-top:80px;">
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:1.25rem;">
        <div>
          <h2 style="margin:0 0 0.25rem;font-size:1.6rem;color:#0F172A;">⚡ Electrical & Energy Engineering</h2>
          <p style="color:#64748B;font-size:0.95rem;margin:0;">Verified electrical engineering calculators compliant with IEC 60364-5-52, NEC NFPA 70, and EIA standards.</p>
        </div>
      </div>
      <div class="silo-card-grid">
        <a href="ohms-law-calculator.html" class="silo-card">
          <div class="silo-card-icon">⚡</div>
          <div class="silo-card-title">Ohm's Law Calculator</div>
          <div class="silo-card-desc">Solve voltage, current, resistance, and wattage simultaneously using the full 12-formula circular Ohm's law wheel.</div>
        </a>
        <a href="voltage-drop-calculator.html" class="silo-card">
          <div class="silo-card-icon">📉</div>
          <div class="silo-card-title">Voltage Drop Calculator</div>
          <div class="silo-card-desc">Check NEC 3% and 5% compliance across single-phase and three-phase copper/aluminum cable runs.</div>
        </a>
        <a href="cable-sizing-calculator.html" class="silo-card">
          <div class="silo-card-icon">🔌</div>
          <div class="silo-card-title">Cable Sizing (IEC 60364)</div>
          <div class="silo-card-desc">Size low-voltage conductors with ambient temperature derating (Ca), grouping factors (Cg), and XLPE/PVC ampacity.</div>
        </a>
        <a href="resistor-color-code-calculator.html" class="silo-card">
          <div class="silo-card-icon">🎨</div>
          <div class="silo-card-title">Resistor Color Code</div>
          <div class="silo-card-desc">Decode 4-band and 5-band axial resistors with an interactive graphical SVG resistor and guaranteed tolerance ranges.</div>
        </a>
        <a href="solar-panel-sizing-calculator.html" class="silo-card">
          <div class="silo-card-icon">☀️</div>
          <div class="silo-card-title">Solar & Battery Sizing</div>
          <div class="silo-card-desc">Calculate photovoltaic array wattage, module counts, and battery bank storage (Ah/kWh) based on peak sun hours.</div>
        </a>
      </div>
    </section>

  </main>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="index.html" class="brand-logo">
            <span class="logo-badge">∑</span>
            <span>Calc<span class="accent">Hub</span></span>
          </a>
          <p>High-precision, free online calculators designed according to published mathematical, clinical, and industrial engineering standards. 100% free, browser-based, with zero tracking.</p>
        </div>
        <div class="footer-col">
          <h4>Health & Fitness</h4>
          <ul class="footer-links">
            <li><a href="bmi-calculator.html">BMI Calculator</a></li>
            <li><a href="calorie-calculator.html">Calorie Calculator (TDEE)</a></li>
            <li><a href="body-fat-calculator.html">Body Fat Calculator</a></li>
            <li><a href="ideal-weight-calculator.html">Ideal Body Weight</a></li>
            <li><a href="water-intake-calculator.html">Daily Water Intake</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Finance & Money</h4>
          <ul class="footer-links">
            <li><a href="loan-emi-calculator.html">Loan EMI Calculator</a></li>
            <li><a href="compound-interest-calculator.html">Compound Interest</a></li>
            <li><a href="simple-interest-calculator.html">Simple Interest</a></li>
            <li><a href="discount-calculator.html">Discount & Sale</a></li>
            <li><a href="salary-calculator.html">Salary / Paycheck</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Math & Engineering</h4>
          <ul class="footer-links">
            <li><a href="percentage-calculator.html">Percentage Calculator</a></li>
            <li><a href="age-calculator.html">Exact Age Calculator</a></li>
            <li><a href="ohms-law-calculator.html">Ohm's Law Calculator</a></li>
            <li><a href="voltage-drop-calculator.html">Voltage Drop (NEC/IEC)</a></li>
            <li><a href="cable-sizing-calculator.html">Cable Sizing Calculator</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Mathematical tools are for educational and guidance purposes.</p>
        <div>
          <a href="sitemap.xml" style="color:#64748B;margin-left:1rem;">Sitemap</a>
          <a href="index.html" style="color:#64748B;margin-left:1rem;">Privacy & Terms</a>
        </div>
      </div>
    </div>
  </footer>

  <script src="app.js"></script>
</body>
</html>
"""

with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

print("Created index.html successfully!")
