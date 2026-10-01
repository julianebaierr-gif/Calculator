"""
Master builder script to generate all new calculators and category hub pages.
"""

import os
from data_solar_mechanical import SOLAR_MECHANICAL_TOOLS
from data_civil_chemical import CIVIL_CHEMICAL_TOOLS
from data_fire_programmer_time_converter import FIRE_PROGRAMMER_TOOLS
from data_categories import NEW_CATEGORIES

ALL_NEW_TOOLS = SOLAR_MECHANICAL_TOOLS + CIVIL_CHEMICAL_TOOLS + FIRE_PROGRAMMER_TOOLS

def render_inputs(inputs):
    html = []
    for inp in inputs:
        inp_id = inp["id"]
        label = inp["label"]
        unit = f' <span class="input-unit">({inp["unit"]})</span>' if inp.get("unit") else ""
        if inp["type"] == "select":
            opts = "".join([f'<option value="{val}"{" selected" if val == inp["default"] else ""}>{txt}</option>' for val, txt in inp["options"]])
            html.append(f"""
            <div class="calc-field-group">
              <label for="{inp_id}" class="field-label">{label}{unit}</label>
              <select id="{inp_id}" class="calc-select">
                {opts}
              </select>
            </div>
            """)
        else:
            min_attr = f' min="{inp["min"]}"' if "min" in inp else ""
            max_attr = f' max="{inp["max"]}"' if "max" in inp else ""
            step_attr = f' step="{inp["step"]}"' if "step" in inp else ""
            html.append(f"""
            <div class="calc-field-group">
              <label for="{inp_id}" class="field-label">{label}{unit}</label>
              <input type="{inp["type"]}" id="{inp_id}" class="calc-input" value="{inp["default"]}"{min_attr}{max_attr}{step_attr}>
            </div>
            """)
    return "\n".join(html)

def render_metrics(metrics):
    html = []
    for m_id, label, unit in metrics:
        html.append(f"""
        <div class="breakdown-item">
          <span class="breakdown-label">{label}</span>
          <span class="breakdown-value" id="{m_id}">--</span>
        </div>
        """)
    return "\n".join(html)

def render_calculator_page(t):
    slug = t["slug"]
    title = t["title"]
    cat = t["category"]
    cat_slug = t["cat_slug"]
    icon = t["icon"]
    badge = t["badge"]
    meta_desc = t["meta_desc"]
    keywords = t["keywords"]
    art = t["article"]
    
    faq_schema = []
    faq_html = []
    for q, a in art["faqs"]:
        faq_schema.append(f"""{{
          "@type": "Question",
          "name": "{q}",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "{a}"
          }}
        }}""")
        faq_html.append(f"""
        <div class="faq-item">
          <div class="faq-q">{q}</div>
          <div class="faq-a">{a}</div>
        </div>
        """)
    faq_schema_str = ",\n".join(faq_schema)
    faq_html_str = "\n".join(faq_html)

    th_html = "".join([f"<th>{h}</th>" for h in art["table_headers"]])
    tr_html = "".join(["<tr>" + "".join([f"<td>{cell}</td>" for cell in row]) + "</tr>\n" for row in art["table_rows"]])

    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — High-Precision Free Online Tool | CalcHub</title>
  <meta name="description" content="{meta_desc}">
  <meta name="keywords" content="{keywords}">
  <meta name="author" content="CalcHub {cat} Engineering Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/{slug}">
  <link rel="stylesheet" href="styles.css">

  <!-- Open Graph -->
  <meta property="og:title" content="{title} | CalcHub">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/{slug}">

  <!-- MathJax for KaTeX math rendering -->
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <!-- Structured Data: WebApplication, MathSolver, FAQPage -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "WebApplication",
        "@id": "https://calchub.org/{slug}#app",
        "name": "{title}",
        "url": "https://calchub.org/{slug}",
        "applicationCategory": "EducationalApplication",
        "operatingSystem": "All",
        "browserRequirements": "Requires JavaScript",
        "description": "{meta_desc}"
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/" }},
          {{ "@type": "ListItem", "position": 2, "name": "{cat}", "item": "https://calchub.org/{cat_slug}" }},
          {{ "@type": "ListItem", "position": 3, "name": "{title}", "item": "https://calchub.org/{slug}" }}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {faq_schema_str}
        ]
      }}
    ]
  }}
  </script>
</head>
<body>

  <!-- Sticky Header -->
  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="brand-logo">
        <span class="logo-badge">∑</span>
        <span>Calc<span class="accent">Hub</span></span>
      </a>
      <nav class="header-nav" aria-label="Main Navigation">
        <a href="health.html" class="nav-link">⚖️ Health</a>
        <a href="finance.html" class="nav-link">🏦 Finance</a>
        <a href="math.html" class="nav-link">🔢 Math</a>
        <a href="engineering.html" class="nav-link">⚡ Engineering</a>
        <a href="solar-energy.html" class="nav-link">☀️ Solar</a>
        <a href="mechanical.html" class="nav-link">⚙️ Mechanical</a>
      </nav>
      <div class="header-search">
        <span class="search-icon">🔍</span>
        <input type="text" id="header-search-input" placeholder="Search 30+ calculators... (Ctrl+K)" autocomplete="off">
        <div id="search-results-dropdown" class="search-results-dropdown"></div>
      </div>
    </div>
  </header>

  <!-- Breadcrumbs -->
  <nav class="breadcrumbs" aria-label="Breadcrumb">
    <a href="index.html">Home</a>
    <span class="sep">›</span>
    <a href="{cat_slug}">{cat}</a>
    <span class="sep">›</span>
    <span class="current">{title}</span>
  </nav>

  <!-- Main Container -->
  <main class="main-wrapper">
    
    <div class="calculator-hero">
      <span class="category-tag">{icon} {cat} · {badge}</span>
      <h1>{title}</h1>
      <p class="subtitle">{meta_desc}</p>
    </div>

    <!-- Workspace Grid -->
    <div class="calculator-workspace">
      
      <!-- Input Card -->
      <div class="calc-card">
        <div class="card-header">
          <h2>Input Parameters</h2>
          <span style="font-size:0.85rem;color:var(--text-muted);">Real-time reactive calculation</span>
        </div>

        <div class="calc-form-grid">
          {render_inputs(t["inputs"])}
        </div>

        <div class="calc-actions">
          <button type="button" class="btn btn-primary" id="btn-calc">Calculate Result</button>
          <button type="button" class="btn btn-secondary" id="btn-reset">Reset Defaults</button>
        </div>
      </div>

      <!-- Results Card -->
      <div class="results-card">
        <div class="results-header">
          <h3>Calculated Results</h3>
          <span class="results-badge">{badge}</span>
        </div>

        <div class="primary-result-box">
          <div class="primary-result-label">Computed Result</div>
          <div class="primary-result-value" id="prim-val">--</div>
          <div class="primary-result-desc" id="prim-unit">--</div>
        </div>

        <div class="result-breakdown-grid">
          {render_metrics(t["metrics"])}
        </div>

        <div class="results-footer-actions">
          <button type="button" class="btn btn-secondary" onclick="copyToClipboard(document.getElementById('prim-val').textContent, 'Calculated result copied!')">
            📋 Copy Result
          </button>
          <button type="button" class="btn btn-secondary" onclick="printCalculatorReport()">
            🖨️ Print Report
          </button>
        </div>
      </div>

    </div>

    <!-- Educational Long-Form Article -->
    <article class="article-section">
      <div class="article-header">
        <span class="category-tag">Verified Engineering Reference</span>
        <h2>Scientific & Mathematical Fundamentals</h2>
        <div class="article-meta">
          <span>By CalcHub {cat} Editorial Board</span>
          <span>•</span>
          <span>Verified against {badge}</span>
        </div>
      </div>

      <div class="article-summary-box">
        <strong>Executive Summary:</strong> {art["summary"]}
      </div>

      <h3>1. Engineering Principles & Definitions</h3>
      {art["principles"]}

      <h3>2. Mathematical Formulas & Governing Equations</h3>
      {art["formulas"]}

      <h3>3. Reference Standards & Data Table</h3>
      <div class="data-table-container">
        <table class="data-table">
          <thead>
            <tr>{th_html}</tr>
          </thead>
          <tbody>
            {tr_html}
          </tbody>
        </table>
      </div>

      <h3>4. Worked Real-World Engineering Example</h3>
      <p>{art["example"]}</p>

      <div class="faq-container" style="margin-top:2.5rem;">
        <h3 style="margin-bottom:1.5rem;">Frequently Asked Questions</h3>
        {faq_html_str}
      </div>

    </article>

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
          <h4>Engineering & Solar</h4>
          <ul class="footer-links">
            <li><a href="solar-battery-bank-calculator.html">Solar Battery Bank</a></li>
            <li><a href="solar-inverter-sizing-calculator.html">Solar Inverter Sizing</a></li>
            <li><a href="cooling-load-calculator.html">Cooling Load (HVAC)</a></li>
            <li><a href="concrete-calculator.html">Concrete Volume Sizing</a></li>
            <li><a href="chemical-dosing-calculator.html">Chemical Dosing Rate</a></li>
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
  <script>
    function calculate() {{
      {t["calc_js"]}
    }}

    document.addEventListener('DOMContentLoaded', () => {{
      const inputs = document.querySelectorAll('.calc-input, .calc-select');
      inputs.forEach(i => {{
        i.addEventListener('input', calculate);
        i.addEventListener('change', calculate);
      }});

      const btnCalc = document.getElementById('btn-calc');
      if (btnCalc) btnCalc.addEventListener('click', calculate);

      const btnReset = document.getElementById('btn-reset');
      if (btnReset) btnReset.addEventListener('click', () => {{
        inputs.forEach(i => {{
          const def = i.getAttribute('value');
          if (def !== null) i.value = def;
        }});
        calculate();
      }});

      calculate();
    }});
  </script>
</body>
</html>"""
    return content

def render_category_page(cat):
    slug = cat["slug"]
    title = cat["title"]
    icon = cat["icon"]
    badge = cat["badge"]
    meta_desc = cat["meta_desc"]
    overview = cat["overview"]
    tools = cat["tools"]

    cards_html = []
    accent = cat.get("accent_color", "#2563EB")
    for t_slug, t_title, t_icon, t_badge, t_desc in tools:
        cards_html.append(f"""
        <a href="{t_slug}" class="silo-card" style="border-top:3px solid {accent};">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;">
            <div class="silo-card-icon">{t_icon}</div>
            <span class="silo-card-badge">{t_badge}</span>
          </div>
          <div class="silo-card-title">{t_title}</div>
          <div class="silo-card-desc">{t_desc}</div>
          <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:{accent};margin-top:1rem;">
            Launch Calculator &rarr;
          </span>
        </a>
        """)
    cards_str = "\n".join(cards_html)

    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — High-Precision Free Online Tools | CalcHub</title>
  <meta name="description" content="{meta_desc}">
  <meta name="author" content="CalcHub {title} Editorial Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/{slug}">
  <link rel="stylesheet" href="styles.css">

  <!-- Open Graph -->
  <meta property="og:title" content="{title} | CalcHub">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/{slug}">

  <!-- Structured Data: CollectionPage -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "CollectionPage",
        "@id": "https://calchub.org/{slug}#webpage",
        "url": "https://calchub.org/{slug}",
        "name": "{title}",
        "description": "{meta_desc}",
        "breadcrumb": {{
          "@type": "BreadcrumbList",
          "itemListElement": [
            {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/" }},
            {{ "@type": "ListItem", "position": 2, "name": "{title}", "item": "https://calchub.org/{slug}" }}
          ]
        }}
      }}
    ]
  }}
  </script>
</head>
<body>

  <!-- Sticky Header -->
  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="brand-logo">
        <span class="logo-badge">∑</span>
        <span>Calc<span class="accent">Hub</span></span>
      </a>
      <nav class="header-nav" aria-label="Main Navigation">
        <a href="health.html" class="nav-link">⚖️ Health</a>
        <a href="finance.html" class="nav-link">🏦 Finance</a>
        <a href="math.html" class="nav-link">🔢 Math</a>
        <a href="engineering.html" class="nav-link">⚡ Engineering</a>
        <a href="solar-energy.html" class="nav-link">☀️ Solar</a>
        <a href="mechanical.html" class="nav-link">⚙️ Mechanical</a>
      </nav>
      <div class="header-search">
        <span class="search-icon">🔍</span>
        <input type="text" id="header-search-input" placeholder="Search 30+ calculators... (Ctrl+K)" autocomplete="off">
        <div id="search-results-dropdown" class="search-results-dropdown"></div>
      </div>
    </div>
  </header>

  <!-- Category Hub Hero -->
  <div class="cat-hub-hero">
    <div class="cat-hub-hero-inner">
      <div class="category-breadcrumbs">
        <a href="index.html">Home</a> &rsaquo; <span>{title}</span>
      </div>
      <span class="category-tag" style="background:#F8FAFC;color:{accent};border-color:#E2E8F0;margin-bottom:1rem;">
        {icon} Verified {badge} Compliant
      </span>
      <h1 style="font-size:clamp(2.2rem, 4vw, 3rem);letter-spacing:-0.03em;margin-bottom:0.75rem;color:#0F172A;">
        {title}
      </h1>
      <p style="font-size:1.1rem;color:#475569;line-height:1.65;margin-bottom:1.5rem;">
        {meta_desc}
      </p>
      <div style="display:flex;gap:1.5rem;flex-wrap:wrap;">
        <span style="font-size:0.88rem;color:#64748B;"><strong>{len(tools)}</strong> Certified Calculators</span>
        <span style="font-size:0.88rem;color:#64748B;">• <strong>100%</strong> Free & Client-Side</span>
        <span style="font-size:0.88rem;color:#64748B;">• <strong>Print-Ready</strong> Reports</span>
      </div>
    </div>
  </div>

  <!-- Main Tools Grid -->
  <main class="main-wrapper" style="margin-top:2.5rem;">

    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:1.5rem;">
      <h2 style="margin:0;font-size:1.5rem;color:#0F172A;">Available Tools ({len(tools)})</h2>
      <a href="index.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">&larr; All Categories</a>
    </div>

    <div class="silo-card-grid" style="margin-top:0;margin-bottom:3.5rem;">
      {cards_str}
    </div>

    <!-- Educational Guide -->
    <article class="article-section">
      <div class="article-header">
        <span class="category-tag">Field Manual</span>
        <h2>Discipline Engineering & Theoretical Standards</h2>
        <div class="article-meta">
          <span>By CalcHub {title} Editorial Board</span>
          <span>•</span>
          <span>Verified against {badge}</span>
        </div>
      </div>

      <p>{overview}</p>
      <p>All calculators in this section execute purely in your web browser with instantaneous numerical evaluations, zero telemetry tracking, and exportable print-ready reports.</p>
    </article>

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
          <h4>All Categories</h4>
          <ul class="footer-links">
            <li><a href="solar-energy.html">Solar & Renewable</a></li>
            <li><a href="mechanical.html">Mechanical & HVAC</a></li>
            <li><a href="civil.html">Civil & Construction</a></li>
            <li><a href="chemical.html">Chemical & Water</a></li>
            <li><a href="fire-safety.html">Fire & Life Safety</a></li>
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
</html>"""
    return content

def main():
    print(f"Building {len(ALL_NEW_TOOLS)} new calculators...")
    for t in ALL_NEW_TOOLS:
        html = render_calculator_page(t)
        filepath = t["slug"]
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"[OK] Created {filepath}")

    print(f"\nBuilding {len(NEW_CATEGORIES)} new category hub pages...")
    for cat in NEW_CATEGORIES:
        html = render_category_page(cat)
        filepath = cat["slug"]
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"[OK] Created Category Page: {filepath}")

    print("\nAll new calculators and category pages generated successfully!")

if __name__ == "__main__":
    main()
