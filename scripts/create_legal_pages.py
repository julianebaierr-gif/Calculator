import os

COMMON_HEAD = '''  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <link rel="icon" type="image/x-icon" href="/favicon.ico">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="stylesheet" href="styles.css">'''

HEADER_HTML = '''  <!-- Sticky Header -->
  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="brand-logo">
        <span class="logo-badge">∑</span>
        <span>Calc<span class="accent">Hub</span></span>
      </a>
      <div class="header-search">
        <input type="text" id="header-search-input" placeholder="Search 380+ precision calculators... (Ctrl+K)" autocomplete="off">
        <div id="search-results-dropdown" class="search-dropdown"></div>
      </div>
      <nav class="header-nav" aria-label="Main Navigation">
        <div class="nav-row">
          <a href="index.html" class="nav-link">🏠 Home</a>
          <a href="health.html" class="nav-link">⚖️ Health</a>
          <a href="finance.html" class="nav-link">🏦 Finance</a>
          <a href="math.html" class="nav-link">🔢 Math</a>
          <a href="engineering.html" class="nav-link">⚡ Electrical</a>
          <a href="solar-energy.html" class="nav-link">☀️ Solar</a>
          <a href="mechanical.html" class="nav-link">⚙️ Mechanical</a>
        </div>
        <div class="nav-row">
          <a href="civil.html" class="nav-link">🏗️ Civil</a>
          <a href="chemical.html" class="nav-link">🧪 Chemical</a>
          <a href="fire-safety.html" class="nav-link">🚨 Fire &amp; Safety</a>
          <a href="programmer.html" class="nav-link">👨‍💻 Programmer</a>
          <a href="datetime.html" class="nav-link">📅 Date &amp; Time</a>
          <a href="converter.html" class="nav-link">🔄 Converter</a>
        </div>
      </nav>
    </div>
  </header>'''

FOOTER_HTML = '''  <!-- Site Footer -->
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
          <h4>Health &amp; Fitness</h4>
          <ul class="footer-links">
            <li><a href="bmi-calculator.html">BMI Calculator</a></li>
            <li><a href="calorie-calculator.html">Calorie Calculator (TDEE)</a></li>
            <li><a href="body-fat-calculator.html">Body Fat Calculator</a></li>
            <li><a href="ideal-weight-calculator.html">Ideal Body Weight</a></li>
            <li><a href="water-intake-calculator.html">Daily Water Intake</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Finance &amp; Money</h4>
          <ul class="footer-links">
            <li><a href="loan-emi-calculator.html">Loan EMI Calculator</a></li>
            <li><a href="compound-interest-calculator.html">Compound Interest</a></li>
            <li><a href="simple-interest-calculator.html">Simple Interest</a></li>
            <li><a href="discount-calculator.html">Discount &amp; Sale</a></li>
            <li><a href="salary-calculator.html">Salary / Paycheck</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Engineering &amp; Tech</h4>
          <ul class="footer-links">
            <li><a href="solar-energy.html">Solar &amp; Renewable Hub</a></li>
            <li><a href="mechanical.html">Mechanical &amp; HVAC Hub</a></li>
            <li><a href="civil.html">Civil &amp; Construction Hub</a></li>
            <li><a href="chemical.html">Chemical &amp; Water Hub</a></li>
            <li><a href="programmer.html">Programmer &amp; CIDR Hub</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Mathematical tools are for educational and guidance purposes.</p>
        <div class="footer-bottom-links">
          <a href="sitemap.xml">Sitemap</a>
          <a href="about.html">About Us</a>
          <a href="privacy-policy.html">Privacy Policy</a>
          <a href="terms.html">Terms of Service</a>
          <a href="disclaimer.html">Disclaimers</a>
          <a href="contact.html">Contact Us</a>
        </div>
      </div>
    </div>
  </footer>'''

def create_about():
    content = f'''<!DOCTYPE html>
<html lang="en">
<head>
{COMMON_HEAD}
  <title>About CalcHub — Engineering, Medical & Mathematical Computation Standards</title>
  <meta name="description" content="Learn about CalcHub's mission, rigorous mathematical standards, clinical methodologies, and peer-reviewed calculation engines. Free, zero-tracking, client-side tools.">
  <link rel="canonical" href="https://calchub.org/about">
  <meta property="og:title" content="About CalcHub — Computation Standards & Mission">
  <meta property="og:description" content="Transparent, certified calculation models for health, engineering, finance, and mathematics.">
  <meta property="og:url" content="https://calchub.org/about">
  <meta property="og:type" content="website">
</head>
<body>
{HEADER_HTML}

  <main class="page-container" style="max-width: 960px; margin: 0 auto; padding: 2.5rem 1.25rem 4rem;">
    <nav class="category-breadcrumbs" style="margin-bottom: 1.5rem; font-size: 0.9rem; color: #64748B;">
      <a href="index.html" style="color: #2563EB; text-decoration: none;">Home</a> &rsaquo; <span>About CalcHub</span>
    </nav>

    <header style="margin-bottom: 2.5rem; border-bottom: 1px solid #E2E8F0; padding-bottom: 1.5rem;">
      <span class="category-tag" style="background: #EFF6FF; color: #2563EB; border-color: #BFDBFE; margin-bottom: 0.75rem; display: inline-block; padding: 4px 12px; border-radius: 999px; font-size: 0.82rem; font-weight: 600;">
        🔬 Transparent · Peer-Reviewed · Zero-Telemetry
      </span>
      <h1 style="font-size: 2.5rem; color: #0F172A; margin: 0.5rem 0 1rem; letter-spacing: -0.02em;">About CalcHub</h1>
      <p style="font-size: 1.15rem; color: #475569; line-height: 1.7; max-width: 820px; margin: 0;">
        CalcHub is an open-access, precision computational platform dedicated to providing mathematically rigorous, standards-compliant calculators across health, civil engineering, electrical design, finance, and applied physics.
      </p>
    </header>

    <article class="article-section" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 2.5rem; margin-bottom: 2rem; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
      <h2 style="font-size: 1.6rem; color: #0F172A; margin-top: 0; margin-bottom: 1rem;">Our Mission: Open-Access Precision Computing</h2>
      <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-bottom: 1.5rem;">
        The internet is crowded with simplistic calculators that conceal their underlying formulas, deliver erroneous rounding, or require users to enter private financial and health metrics into remote database servers. CalcHub was established on three non-negotiable principles:
      </p>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.25rem; margin-bottom: 2rem;">
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.25rem;">
          <h3 style="font-size: 1.1rem; color: #2563EB; margin: 0 0 0.5rem;">🔒 100% Client-Side Privacy</h3>
          <p style="font-size: 0.92rem; color: #475569; line-height: 1.6; margin: 0;">All computations occur locally in your browser. Your body measurements, salary details, and project metrics never leave your device.</p>
        </div>
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.25rem;">
          <h3 style="font-size: 1.1rem; color: #2563EB; margin: 0 0 0.5rem;">📐 Formula Transparency</h3>
          <p style="font-size: 0.92rem; color: #475569; line-height: 1.6; margin: 0;">Every calculator displays its formal LaTeX equation, variable definitions, and step-by-step worked examples with complete clinical or engineering citations.</p>
        </div>
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.25rem;">
          <h3 style="font-size: 1.1rem; color: #2563EB; margin: 0 0 0.5rem;">⚡ Instantaneous & Ad-Unobtrusive</h3>
          <p style="font-size: 0.92rem; color: #475569; line-height: 1.6; margin: 0;">No paywalls, no mandatory registration, and zero intrusive popups. Clean, keyboard-friendly interfaces built for productivity.</p>
        </div>
      </div>

      <h2 style="font-size: 1.6rem; color: #0F172A; margin-top: 2rem; margin-bottom: 1rem;">Rigorous Standards Compliance</h2>
      <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-bottom: 1.25rem;">
        CalcHub models are calibrated against globally recognized institutional specifications and peer-reviewed scientific literature:
      </p>
      <ul style="color: #334155; line-height: 1.8; font-size: 1rem; padding-left: 1.5rem; margin-bottom: 2rem;">
        <li><strong>Health &amp; Anthropometrics:</strong> World Health Organization (WHO) BMI classifications, National Academy of Medicine (NASEM) dietary reference intakes, and the Mifflin-St Jeor (1990) and Devine (1974) validated physiological equations.</li>
        <li><strong>Electrical &amp; Electronics:</strong> National Electrical Code (NEC NFPA 70), IEEE Standard 141 (Red Book), IEC 60364-5-52 conductor ampacity tables, and Kirchhoff/Ohm electrical circuit laws.</li>
        <li><strong>Civil &amp; Structural Engineering:</strong> American Concrete Institute (ACI 318), ASTM International material standards, and AASHTO highway pavement specifications.</li>
        <li><strong>Mechanical &amp; Thermodynamics:</strong> ASHRAE Fundamentals heat load guidelines, Darcy-Weisbach friction loss equations, and Bernoulli fluid dynamics principles.</li>
        <li><strong>Financial Mathematics:</strong> Chartered Financial Analyst (CFA) curriculum standards, Truth in Lending Act (TILA) annual percentage rate (APR) amortization formulations, and continuous compound interest models.</li>
      </ul>

      <h2 style="font-size: 1.6rem; color: #0F172A; margin-top: 2rem; margin-bottom: 1rem;">Editorial &amp; Engineering Review Process</h2>
      <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-bottom: 1rem;">
        Each tool hosted on CalcHub undergoes a multi-stage validation lifecycle prior to deployment:
      </p>
      <ol style="color: #334155; line-height: 1.8; font-size: 1rem; padding-left: 1.5rem; margin-bottom: 2rem;">
        <li><strong>Primary Source Sourcing:</strong> Mathematical models are extracted from authoritative peer-reviewed journals, national codes, or institutional textbooks.</li>
        <li><strong>Double-Blind Code Verification:</strong> Algorithmic implementations are written in JavaScript and cross-checked against benchmark reference datasets and NIST/IEEE test vectors.</li>
        <li><strong>Boundary &amp; Edge Case Testing:</strong> Calculators are audited for asymptotic behavior, divide-by-zero risks, imperial/metric floating-point precision, and non-linear tolerances.</li>
        <li><strong>Ongoing Community Peer Review:</strong> Practitioners, engineers, and educators continually verify calculations and submit feedback via our transparent corrections channel.</li>
      </ol>

      <h2 style="font-size: 1.6rem; color: #0F172A; margin-top: 2rem; margin-bottom: 1rem;">Contact &amp; Peer Contributions</h2>
      <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-bottom: 0;">
        We welcome contributions, formula reviews, and error reports from mathematicians, engineers, and medical professionals. To propose a tool or report a mathematical discrepancy, please visit our <a href="contact.html" style="color: #2563EB; font-weight: 600; text-decoration: underline;">Contact Page</a> or email <a href="mailto:editorial@calchub.org" style="color: #2563EB; font-weight: 600;">editorial@calchub.org</a>.
      </p>
    </article>
  </main>

{FOOTER_HTML}
  <script src="app.js"></script>
</body>
</html>'''
    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Created about.html")

def create_privacy():
    content = f'''<!DOCTYPE html>
<html lang="en">
<head>
{COMMON_HEAD}
  <title>Privacy Policy — CalcHub Mathematical Computation Engine</title>
  <meta name="description" content="CalcHub's comprehensive privacy policy. 100% client-side computations, zero telemetry on mathematical inputs, GDPR & CCPA compliant.">
  <link rel="canonical" href="https://calchub.org/privacy-policy">
  <meta property="og:title" content="Privacy Policy — CalcHub">
  <meta property="og:description" content="Discover how CalcHub protects your data with client-side computation and zero tracking.">
  <meta property="og:url" content="https://calchub.org/privacy-policy">
  <meta property="og:type" content="website">
</head>
<body>
{HEADER_HTML}

  <main class="page-container" style="max-width: 960px; margin: 0 auto; padding: 2.5rem 1.25rem 4rem;">
    <nav class="category-breadcrumbs" style="margin-bottom: 1.5rem; font-size: 0.9rem; color: #64748B;">
      <a href="index.html" style="color: #2563EB; text-decoration: none;">Home</a> &rsaquo; <span>Privacy Policy</span>
    </nav>

    <header style="margin-bottom: 2.5rem; border-bottom: 1px solid #E2E8F0; padding-bottom: 1.5rem;">
      <span class="category-tag" style="background: #EFF6FF; color: #2563EB; border-color: #BFDBFE; margin-bottom: 0.75rem; display: inline-block; padding: 4px 12px; border-radius: 999px; font-size: 0.82rem; font-weight: 600;">
        🛡️ GDPR · CCPA · Zero-Tracking Architecture
      </span>
      <h1 style="font-size: 2.5rem; color: #0F172A; margin: 0.5rem 0 1rem; letter-spacing: -0.02em;">Privacy Policy</h1>
      <p style="font-size: 1.1rem; color: #475569; line-height: 1.7; margin: 0;">
        Last Updated: January 1, 2026. CalcHub is committed to total user privacy through client-side computational architecture.
      </p>
    </header>

    <article class="article-section" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 2.5rem; margin-bottom: 2rem; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
      <h2 style="font-size: 1.5rem; color: #0F172A; margin-top: 0; margin-bottom: 1rem;">1. Core Architecture: 100% Client-Side Computation</h2>
      <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-bottom: 1.25rem;">
        Unlike traditional web utilities that post form data to remote servers for processing, <strong>CalcHub runs all calculations entirely inside your browser's local JavaScript runtime</strong>.
      </p>
      <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-bottom: 1.5rem;">
        Whether you are evaluating sensitive health metrics (such as BMI, body fat percentage, or caloric targets), private financial records (such as salary, mortgage principal, or loan interest), or proprietary engineering dimensions, <strong>no numerical inputs or outputs are ever transmitted to our web servers, stored in cloud databases, or viewed by third parties</strong>.
      </p>

      <h2 style="font-size: 1.5rem; color: #0F172A; margin-top: 2rem; margin-bottom: 1rem;">2. Information We Automatically Collect</h2>
      <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-bottom: 1rem;">
        When you visit CalcHub, our hosting infrastructure and content delivery network (CDN) collect standard non-identifiable web traffic telemetry:
      </p>
      <ul style="color: #334155; line-height: 1.8; font-size: 1rem; padding-left: 1.5rem; margin-bottom: 1.5rem;">
        <li>Browser user-agent, operating system, and screen resolution.</li>
        <li>Referring URL and requested page paths.</li>
        <li>Anonymized IP addresses used exclusively for DDoS mitigation and server load balancing.</li>
      </ul>

      <h2 style="font-size: 1.5rem; color: #0F172A; margin-top: 2rem; margin-bottom: 1rem;">3. Cookies and Local Storage</h2>
      <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-bottom: 1rem;">
        We use minimal browser storage strictly to improve your user experience:
      </p>
      <ul style="color: #334155; line-height: 1.8; font-size: 1rem; padding-left: 1.5rem; margin-bottom: 1.5rem;">
        <li><strong>Functional LocalStorage:</strong> Used to persist your preferred measurement unit system (Metric vs. Imperial) and theme preferences across sessions. No personal identifiable information (PII) is stored.</li>
        <li><strong>Third-Party Vendor Cookies:</strong> Third-party partners, including Google AdSense, may place cookies to serve relevant contextual advertising based on prior visits to this or other websites. Users may opt out of personalized advertising by visiting <a href="https://adssettings.google.com" target="_blank" rel="noopener noreferrer" style="color: #2563EB;">Google Ads Settings</a> or <a href="https://www.aboutads.info/choices/" target="_blank" rel="noopener noreferrer" style="color: #2563EB;">AboutAds.info</a>.</li>
      </ul>

      <h2 style="font-size: 1.5rem; color: #0F172A; margin-top: 2rem; margin-bottom: 1rem;">4. GDPR and CCPA Compliance</h2>
      <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-bottom: 1rem;">
        Under the General Data Protection Regulation (GDPR) and California Consumer Privacy Act (CCPA):
      </p>
      <ul style="color: #334155; line-height: 1.8; font-size: 1rem; padding-left: 1.5rem; margin-bottom: 1.5rem;">
        <li>We do not sell, rent, or trade your personal data to any third party.</li>
        <li>Because we do not store personal account databases or computational input logs, we hold zero user-identifiable records.</li>
        <li>If you contact our editorial team via email, your email address is used solely to respond to your specific inquiry.</li>
      </ul>

      <h2 style="font-size: 1.5rem; color: #0F172A; margin-top: 2rem; margin-bottom: 1rem;">5. Contact Data Protection Officer</h2>
      <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-bottom: 0;">
        For privacy queries, data protection concerns, or legal notices, contact our data compliance coordinator at <a href="mailto:privacy@calchub.org" style="color: #2563EB; font-weight: 600;">privacy@calchub.org</a>.
      </p>
    </article>
  </main>

{FOOTER_HTML}
  <script src="app.js"></script>
</body>
</html>'''
    with open('privacy-policy.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Created privacy-policy.html")

def create_terms():
    content = f'''<!DOCTYPE html>
<html lang="en">
<head>
{COMMON_HEAD}
  <title>Terms of Service — CalcHub User Agreement & Computational Terms</title>
  <meta name="description" content="CalcHub Terms of Service. Review permitted usage, intellectual property rights, mathematical warranties, and limitation of liability.">
  <link rel="canonical" href="https://calchub.org/terms">
  <meta property="og:title" content="Terms of Service — CalcHub">
  <meta property="og:description" content="Terms of service and legal agreement for using CalcHub precision calculators.">
  <meta property="og:url" content="https://calchub.org/terms">
  <meta property="og:type" content="website">
</head>
<body>
{HEADER_HTML}

  <main class="page-container" style="max-width: 960px; margin: 0 auto; padding: 2.5rem 1.25rem 4rem;">
    <nav class="category-breadcrumbs" style="margin-bottom: 1.5rem; font-size: 0.9rem; color: #64748B;">
      <a href="index.html" style="color: #2563EB; text-decoration: none;">Home</a> &rsaquo; <span>Terms of Service</span>
    </nav>

    <header style="margin-bottom: 2.5rem; border-bottom: 1px solid #E2E8F0; padding-bottom: 1.5rem;">
      <span class="category-tag" style="background: #EFF6FF; color: #2563EB; border-color: #BFDBFE; margin-bottom: 0.75rem; display: inline-block; padding: 4px 12px; border-radius: 999px; font-size: 0.82rem; font-weight: 600;">
        ⚖️ Legal Agreement · User Terms
      </span>
      <h1 style="font-size: 2.5rem; color: #0F172A; margin: 0.5rem 0 1rem; letter-spacing: -0.02em;">Terms of Service</h1>
      <p style="font-size: 1.1rem; color: #475569; line-height: 1.7; margin: 0;">
        Last Updated: January 1, 2026. By accessing CalcHub, you accept and agree to be bound by these Terms of Service.
      </p>
    </header>

    <article class="article-section" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 2.5rem; margin-bottom: 2rem; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
      <h2 style="font-size: 1.5rem; color: #0F172A; margin-top: 0; margin-bottom: 1rem;">1. Acceptance of Agreement</h2>
      <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-bottom: 1.25rem;">
        These Terms of Service constitute a legally binding agreement between you and CalcHub ("we", "us", or "our"). If you do not agree with all of these terms, you are expressly prohibited from using the platform and must discontinue use immediately.
      </p>

      <h2 style="font-size: 1.5rem; color: #0F172A; margin-top: 2rem; margin-bottom: 1rem;">2. Permitted Use and License</h2>
      <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-bottom: 1rem;">
        CalcHub grants you a revocable, non-exclusive, non-transferable, limited license to access and utilize our online mathematical models, calculators, and educational content for personal, academic, research, and non-commercial professional reference purposes.
      </p>
      <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-bottom: 1.5rem;">
        You agree not to scrape, reverse engineer, systematically extract, or mirror CalcHub content or computational logic into third-party commercial applications without prior written authorization.
      </p>

      <h2 style="font-size: 1.5rem; color: #0F172A; margin-top: 2rem; margin-bottom: 1rem;">3. Intellectual Property Rights</h2>
      <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-bottom: 1.5rem;">
        Unless otherwise indicated, the platform, source code, algorithms, user interfaces, branding ("CalcHub", "∑ CalcHub"), and written reference documentation are proprietary intellectual property owned or licensed by CalcHub and are protected by applicable copyright, trademark, and unfair competition laws.
      </p>

      <h2 style="font-size: 1.5rem; color: #0F172A; margin-top: 2rem; margin-bottom: 1rem;">4. "As-Is" Computational Warranty Disclaimer</h2>
      <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-bottom: 1.5rem;">
        CalcHub provides all calculations, tables, formulas, and guidance on an <strong>"AS IS" and "AS AVAILABLE"</strong> basis. While we strive for uncompromising accuracy and cite official governing standards, we make no warranties or representations of any kind, express or implied, regarding the mathematical absolute certainty, applicability, or reliability of any tool for a specific real-world deployment.
      </p>

      <h2 style="font-size: 1.5rem; color: #0F172A; margin-top: 2rem; margin-bottom: 1rem;">5. Limitation of Liability</h2>
      <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-bottom: 1.5rem;">
        In no event shall CalcHub, its contributors, or licensors be liable to you or any third party for any direct, indirect, consequential, exemplary, incidental, special, or punitive damages—including lost profits, lost savings, structural construction failures, medical harm, or financial losses—arising from your use of or reliance upon any calculator or data on this site.
      </p>

      <h2 style="font-size: 1.5rem; color: #0F172A; margin-top: 2rem; margin-bottom: 1rem;">6. Modifications &amp; Governing Law</h2>
      <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-bottom: 0;">
        We reserve the right to modify these terms at any time without notice. Continued use of CalcHub following any revision constitutes your acceptance of the updated terms. These terms are governed by standard international internet regulations and applicable local laws.
      </p>
    </article>
  </main>

{FOOTER_HTML}
  <script src="app.js"></script>
</body>
</html>'''
    with open('terms.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Created terms.html")

def create_disclaimer():
    content = f'''<!DOCTYPE html>
<html lang="en">
<head>
{COMMON_HEAD}
  <title>Disclaimers — Medical, Financial & Engineering Standards | CalcHub</title>
  <meta name="description" content="Crucial multi-disciplinary disclaimers for CalcHub. Essential medical, financial, and life safety notices regarding precision calculator usage.">
  <link rel="canonical" href="https://calchub.org/disclaimer">
  <meta property="og:title" content="Disclaimers — Medical, Financial & Engineering | CalcHub">
  <meta property="og:description" content="Important regulatory and safety disclaimers for health, finance, and engineering tools.">
  <meta property="og:url" content="https://calchub.org/disclaimer">
  <meta property="og:type" content="website">
</head>
<body>
{HEADER_HTML}

  <main class="page-container" style="max-width: 960px; margin: 0 auto; padding: 2.5rem 1.25rem 4rem;">
    <nav class="category-breadcrumbs" style="margin-bottom: 1.5rem; font-size: 0.9rem; color: #64748B;">
      <a href="index.html" style="color: #2563EB; text-decoration: none;">Home</a> &rsaquo; <span>Disclaimers</span>
    </nav>

    <header style="margin-bottom: 2.5rem; border-bottom: 1px solid #E2E8F0; padding-bottom: 1.5rem;">
      <span class="category-tag" style="background: #FEF2F2; color: #DC2626; border-color: #FECACA; margin-bottom: 0.75rem; display: inline-block; padding: 4px 12px; border-radius: 999px; font-size: 0.82rem; font-weight: 600;">
        ⚠️ YMYL Regulatory Disclaimers & Professional Advice Boundaries
      </span>
      <h1 style="font-size: 2.5rem; color: #0F172A; margin: 0.5rem 0 1rem; letter-spacing: -0.02em;">Disclaimers</h1>
      <p style="font-size: 1.1rem; color: #475569; line-height: 1.7; margin: 0;">
        Important legal, clinical, financial, and industrial life-safety disclaimers regarding the use of CalcHub computational models.
      </p>
    </header>

    <article class="article-section" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 2.5rem; margin-bottom: 2rem; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
      
      <!-- Medical Disclaimer -->
      <div style="border-left: 4px solid #EF4444; padding-left: 1.5rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; color: #991B1B; margin-top: 0; margin-bottom: 0.75rem;">🩺 Medical &amp; Clinical Health Disclaimer</h2>
        <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-bottom: 1rem;">
          <strong>CalcHub is not a medical practice, clinical diagnostic service, or healthcare provider.</strong> All anthropometric, physiological, and metabolic calculators (including BMI, Calorie TDEE, Body Fat Percentage, Ideal Body Weight, Body Surface Area, Water Intake, and HbA1c calculators) are formulated strictly for informational, educational, and preliminary screening purposes.
        </p>
        <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-bottom: 0;">
          These calculators do not establish a patient-physician relationship and should never be used to diagnose, prescribe, or treat any disease, clinical condition, or eating disorder. Anthropometric formulas (such as BMI) carry inherent physiological limitations in athletes, pregnant women, the elderly, and diverse ethnic cohorts. Always consult a board-certified physician, registered dietitian, or qualified healthcare professional before beginning any diet, exercise, or medical regimen.
        </p>
      </div>

      <!-- Financial Disclaimer -->
      <div style="border-left: 4px solid #F59E0B; padding-left: 1.5rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; color: #92400E; margin-top: 0; margin-bottom: 0.75rem;">💰 Financial, Tax &amp; Investment Disclaimer</h2>
        <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-bottom: 1rem;">
          <strong>CalcHub is not a registered investment advisor, broker-dealer, certified financial planner (CFP), or tax advisory firm.</strong> The financial tools provided (including Mortgage, Loan EMI, Compound Interest, Salary/Paycheck, ROI, and Simple Interest calculators) simulate mathematical outcomes based on idealized conditions and user-entered assumptions.
        </p>
        <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-bottom: 0;">
          Real-world financial instruments entail loan origination fees, compounding frequencies, variable interest adjustments, local municipal tax codes, inflation risk, and market volatility. Calculations do not constitute financial advice or lending commitments. Always consult a licensed Certified Public Accountant (CPA) or fiduciary financial advisor prior to executing financial agreements or investments.
        </p>
      </div>

      <!-- Engineering & Life Safety Disclaimer -->
      <div style="border-left: 4px solid #2563EB; padding-left: 1.5rem; margin-bottom: 2rem;">
        <h2 style="font-size: 1.5rem; color: #1E40AF; margin-top: 0; margin-bottom: 0.75rem;">⚙️ Engineering, Structural &amp; Life Safety Disclaimer</h2>
        <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-bottom: 1rem;">
          <strong>CalcHub calculators are educational modeling tools and do not substitute for certified professional engineering review.</strong> Calculations across electrical conductor sizing (NEC NFPA 70), structural concrete volumes (ACI 318), smoke detector coverage (NFPA 72), HVAC cooling loads (ASHRAE), and chemical dosing are intended for preliminary sizing and academic evaluation only.
        </p>
        <p style="color: #334155; line-height: 1.75; font-size: 1rem; margin-bottom: 0;">
          All physical structural installations, high-voltage wiring, life safety alarm deployments, and industrial fluid pipelines must be formally designed, reviewed, and stamped by a licensed Professional Engineer (PE) and comply with local municipal building and electrical codes. CalcHub assumes no liability for construction defects, electrical fires, structural failures, or personal injury resulting from reliance upon these models.
        </p>
      </div>

    </article>
  </main>

{FOOTER_HTML}
  <script src="app.js"></script>
</body>
</html>'''
    with open('disclaimer.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Created disclaimer.html")

def create_contact():
    content = f'''<!DOCTYPE html>
<html lang="en">
<head>
{COMMON_HEAD}
  <title>Contact Us — CalcHub Editorial & Technical Inquiries</title>
  <meta name="description" content="Get in touch with the CalcHub editorial and engineering board. Submit formula reviews, error reports, and feature proposals.">
  <link rel="canonical" href="https://calchub.org/contact">
  <meta property="og:title" content="Contact CalcHub — Editorial & Technical Support">
  <meta property="og:description" content="Reach the CalcHub team for corrections, inquiries, and mathematical feedback.">
  <meta property="og:url" content="https://calchub.org/contact">
  <meta property="og:type" content="website">
</head>
<body>
{HEADER_HTML}

  <main class="page-container" style="max-width: 960px; margin: 0 auto; padding: 2.5rem 1.25rem 4rem;">
    <nav class="category-breadcrumbs" style="margin-bottom: 1.5rem; font-size: 0.9rem; color: #64748B;">
      <a href="index.html" style="color: #2563EB; text-decoration: none;">Home</a> &rsaquo; <span>Contact Us</span>
    </nav>

    <header style="margin-bottom: 2.5rem; border-bottom: 1px solid #E2E8F0; padding-bottom: 1.5rem;">
      <span class="category-tag" style="background: #EFF6FF; color: #2563EB; border-color: #BFDBFE; margin-bottom: 0.75rem; display: inline-block; padding: 4px 12px; border-radius: 999px; font-size: 0.82rem; font-weight: 600;">
        📫 Dedicated Support & Mathematical Corrections
      </span>
      <h1 style="font-size: 2.5rem; color: #0F172A; margin: 0.5rem 0 1rem; letter-spacing: -0.02em;">Contact Us</h1>
      <p style="font-size: 1.1rem; color: #475569; line-height: 1.7; margin: 0;">
        Have a question about a calculation, a mathematical discrepancy to report, or an idea for a new precision tool? We welcome community feedback.
      </p>
    </header>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-bottom: 2.5rem;">
      <article class="article-section" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 2rem; box-shadow: 0 1px 3px rgba(0,0,0,0.05); margin: 0;">
        <h2 style="font-size: 1.35rem; color: #0F172A; margin-top: 0; margin-bottom: 1rem;">Direct Communications</h2>
        <div style="margin-bottom: 1.5rem;">
          <h3 style="font-size: 0.95rem; text-transform: uppercase; letter-spacing: 0.05em; color: #64748B; margin: 0 0 0.25rem;">Editorial &amp; Peer Review</h3>
          <p style="margin: 0; font-size: 1.05rem;"><a href="mailto:editorial@calchub.org" style="color: #2563EB; font-weight: 600; text-decoration: none;">editorial@calchub.org</a></p>
          <p style="font-size: 0.85rem; color: #64748B; margin: 0.25rem 0 0;">For formula citations, clinical literature, and engineering standards review.</p>
        </div>
        <div style="margin-bottom: 1.5rem;">
          <h3 style="font-size: 0.95rem; text-transform: uppercase; letter-spacing: 0.05em; color: #64748B; margin: 0 0 0.25rem;">Discrepancy &amp; Bug Reports</h3>
          <p style="margin: 0; font-size: 1.05rem;"><a href="mailto:corrections@calchub.org" style="color: #2563EB; font-weight: 600; text-decoration: none;">corrections@calchub.org</a></p>
          <p style="font-size: 0.85rem; color: #64748B; margin: 0.25rem 0 0;">Please include input parameters, expected vs. observed result, and reference standard.</p>
        </div>
        <div>
          <h3 style="font-size: 0.95rem; text-transform: uppercase; letter-spacing: 0.05em; color: #64748B; margin: 0 0 0.25rem;">General &amp; Legal Inquiries</h3>
          <p style="margin: 0; font-size: 1.05rem;"><a href="mailto:contact@calchub.org" style="color: #2563EB; font-weight: 600; text-decoration: none;">contact@calchub.org</a></p>
          <p style="font-size: 0.85rem; color: #64748B; margin: 0.25rem 0 0;">Licensing, terms of service, and general platform inquiries.</p>
        </div>
      </article>

      <article class="article-section" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 2rem; box-shadow: 0 1px 3px rgba(0,0,0,0.05); margin: 0;">
        <h2 style="font-size: 1.35rem; color: #0F172A; margin-top: 0; margin-bottom: 1rem;">Send a Message</h2>
        <form id="contact-form" onsubmit="event.preventDefault(); document.getElementById('contact-status').style.display='block'; this.reset();" style="display: flex; flex-direction: column; gap: 1rem;">
          <div>
            <label for="contact-name" style="display: block; font-size: 0.88rem; font-weight: 600; color: #334155; margin-bottom: 0.35rem;">Full Name</label>
            <input type="text" id="contact-name" required placeholder="Dr. Jane Doe / John Smith, PE" style="width: 100%; padding: 0.65rem 0.85rem; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 0.95rem; box-sizing: border-box;">
          </div>
          <div>
            <label for="contact-email" style="display: block; font-size: 0.88rem; font-weight: 600; color: #334155; margin-bottom: 0.35rem;">Email Address</label>
            <input type="email" id="contact-email" required placeholder="name@institution.org" style="width: 100%; padding: 0.65rem 0.85rem; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 0.95rem; box-sizing: border-box;">
          </div>
          <div>
            <label for="contact-category" style="display: block; font-size: 0.88rem; font-weight: 600; color: #334155; margin-bottom: 0.35rem;">Inquiry Topic</label>
            <select id="contact-category" style="width: 100%; padding: 0.65rem 0.85rem; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 0.95rem; box-sizing: border-box; background: #FFF;">
              <option value="correction">Calculation Correction / Discrepancy</option>
              <option value="feature">New Calculator Proposal</option>
              <option value="citation">Standard / Reference Citation Update</option>
              <option value="general">General Feedback</option>
            </select>
          </div>
          <div>
            <label for="contact-message" style="display: block; font-size: 0.88rem; font-weight: 600; color: #334155; margin-bottom: 0.35rem;">Message</label>
            <textarea id="contact-message" rows="4" required placeholder="Describe your inquiry or calculation discrepancy with exact numbers..." style="width: 100%; padding: 0.65rem 0.85rem; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 0.95rem; box-sizing: border-box; resize: vertical;"></textarea>
          </div>
          <button type="submit" style="background: #2563EB; color: #FFFFFF; font-weight: 600; padding: 0.75rem 1.5rem; border: none; border-radius: 6px; cursor: pointer; font-size: 0.95rem; transition: background 0.2s;">
            Submit Inquiry
          </button>
          <div id="contact-status" style="display: none; padding: 0.75rem 1rem; background: #ECFDF5; border: 1px solid #A7F3D0; color: #065F46; border-radius: 6px; font-size: 0.9rem;">
            ✓ Thank you! Your message has been received by our editorial team. Response time is typically within 24-48 business hours.
          </div>
        </form>
      </article>
    </div>
  </main>

{FOOTER_HTML}
  <script src="app.js"></script>
</body>
</html>'''
    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Created contact.html")

if __name__ == '__main__':
    create_about()
    create_privacy()
    create_terms()
    create_disclaimer()
    create_contact()
