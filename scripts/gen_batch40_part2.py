# -*- coding: utf-8 -*-
"""
Generator for Batch 40 - Part 2
Tools:
3. decimal-time-calculator.html (Payroll Decimal Hours, French Metric Time, Swatch Internet Beats)
4. leap-year-calculator.html (Astronomical Tropical Year, Gregorian 400-Year Cycle, Milanković Calendar)
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COMMON_TAIL = """    <footer class="site-footer">
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>About CalcHub</h4>
                    <p>CalcHub delivers peer-reviewed chronometric computing algorithms, astronomical date conversion systems, and calendrical engines compliant with ISO 8601, Gregorian, and Zeller algebraic formulations.</p>
                </div>
                <div class="footer-col">
                    <h4>Chronometric &amp; Time Suites</h4>
                    <ul>
                        <li><a href="datetime.html">Date &amp; Time Utilities</a></li>
                        <li><a href="math.html">Mathematics &amp; Statistics</a></li>
                        <li><a href="finance.html">Financial Planning</a></li>
                        <li><a href="converter.html">Unit &amp; Chrono Converters</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Core Calendrical Tools</h4>
                    <ul>
                        <li><a href="decimal-time-calculator.html">Decimal Time Calculator</a></li>
                        <li><a href="leap-year-calculator.html">Leap Year Calculator</a></li>
                        <li><a href="hours-calculator.html">Work Hours Calculator</a></li>
                        <li><a href="day-of-week-calculator.html">Day of Week Calculator</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="index.html">All Calculators</a></li>
                        <li><a href="converter.html">Metric Converters</a></li>
                        <li><a href="engineering.html">Engineering Tools</a></li>
                        <li><a href="health.html">Health &amp; Fitness</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 CalcHub. All rights reserved. Precision astronomical chronometry and calendar algorithms.</p>
            </div>
        </div>
    </footer>
</body>
</html>"""

def get_page_html(title, description, canonical_slug, schema_json, h1, short_desc, calc_ui, article_content, category_hub="datetime.html", category_name="Date &amp; Time Utility"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="https://calchub.com/{canonical_slug}.html">
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
    <script type="application/ld+json">
{schema_json}
    </script>
</head>
<body>
    <header class="site-header">
        <div class="header-container">
            <a href="index.html" class="logo">CalcHub</a>
            <nav class="nav-links">
                <a href="index.html">Home</a>
                <a href="datetime.html">Date &amp; Time</a>
                <a href="math.html">Math &amp; Stats</a>
                <a href="finance.html">Finance</a>
                <a href="converter.html">Converters</a>
            </nav>
        </div>
    </header>
    <div class="container">
        <div class="main-wrapper">
            <main class="content-area">
                <nav class="breadcrumb">
                    <a href="index.html">Home</a> &gt; <a href="{category_hub}">{category_name}</a> &gt; <span>{h1}</span>
                </nav>
                <div class="calculator-card">
                    <div class="calc-header">
                        <h1>{h1}</h1>
                        <p class="calc-desc">{short_desc}</p>
                    </div>
                    {calc_ui}
                </div>
                <article class="article-body">
                    {article_content}
                </article>
            </main>
            <aside class="sidebar">
                <div class="sidebar-card">
                    <h3>Related Chrono Utilities</h3>
                    <ul class="sidebar-links">
                        <li><a href="decimal-time-calculator.html">Decimal Time Calculator</a></li>
                        <li><a href="leap-year-calculator.html">Leap Year Calculator</a></li>
                        <li><a href="hours-calculator.html">Work Hours Calculator</a></li>
                        <li><a href="day-of-week-calculator.html">Day of Week Calculator</a></li>
                        <li><a href="day-of-year-calculator.html">Day of Year Calculator</a></li>
                        <li><a href="week-number-calculator.html">ISO Week Number</a></li>
                        <li><a href="date-calculator.html">Date Calculator</a></li>
                    </ul>
                </div>
            </aside>
        </div>
    </div>
{COMMON_TAIL}"""


# ===========================================================================
# TOOL 3: decimal-time-calculator.html
# ===========================================================================
def gen_decimal_time():
    slug = "decimal-time-calculator"
    title = "Decimal Time Calculator | Payroll Hours, Metric & Swatch Beats"
    desc = "Convert standard sexagesimal time (hours, minutes, seconds) to decimal hours for payroll, French Revolutionary metric time, centihours, and Swatch Internet Time."
    h1 = "Decimal Time Calculator"
    short_desc = "Precision chronometric conversion between standard sexagesimal time (HH:MM:SS), occupational payroll decimal hours, French Revolutionary metric time, and Swatch .beats."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Decimal Time Calculator",
      "url": "https://calchub.com/decimal-time-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Converts sexagesimal time into payroll decimal hours, centihours, French metric time, and Swatch Internet .beat units."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How do you convert minutes to decimal hours for payroll?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Divide the number of minutes by 60. For example, 45 minutes divided by 60 is 0.75 decimal hours. Total time of 8 hours and 45 minutes equals 8.75 decimal hours."
          }
        },
        {
          "@type": "Question",
          "name": "What is French Revolutionary metric time?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Introduced in 1793 during the French Revolution, metric time divides the diurnal solar day into 10 decimal hours, each hour into 100 decimal minutes, and each minute into 100 decimal seconds (100,000 decimal seconds per day)."
          }
        },
        {
          "@type": "Question",
          "name": "What is Swatch Internet Time (.beat)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Introduced by the Swatch Group in 1998, Swatch Internet Time divides a solar day into 1000 .beats, based on Biel Mean Time (UTC+1). One .beat equals exactly 86.4 seconds."
          }
        },
        {
          "@type": "Question",
          "name": "Why do aviation logbooks and payroll systems use decimal hours?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Decimal hours eliminate sexagesimal base-60 fractions, making arithmetic multiplication with hourly wage rates or aircraft fuel burn rates trivial and error-free."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-body">
    <div style="display: flex; gap: 1rem; border-bottom: 2px solid #e2e8f0; margin-bottom: 1.5rem; padding-bottom: 0.5rem;">
        <button type="button" id="tabStandard" class="btn btn-primary" style="padding: 0.5rem 1rem; font-size: 0.9rem;" onclick="switchMode('standard')">Standard to Decimal</button>
        <button type="button" id="tabDecimal" class="btn btn-outline" style="padding: 0.5rem 1rem; font-size: 0.9rem;" onclick="switchMode('decimal')">Decimal to Standard</button>
        <button type="button" id="tabMetric" class="btn btn-outline" style="padding: 0.5rem 1rem; font-size: 0.9rem;" onclick="switchMode('metric')">Metric &amp; Swatch Beats</button>
    </div>

    <!-- Mode 1: Standard to Decimal -->
    <div id="panelStandard">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 1rem; margin-bottom: 1.25rem;">
            <div>
                <label for="stdHours" style="font-weight: 600; font-size: 0.875rem;">Hours (HH):</label>
                <input type="number" id="stdHours" class="input-field" value="8" min="0" max="999" step="1">
            </div>
            <div>
                <label for="stdMinutes" style="font-weight: 600; font-size: 0.875rem;">Minutes (MM):</label>
                <input type="number" id="stdMinutes" class="input-field" value="45" min="0" max="59" step="1">
            </div>
            <div>
                <label for="stdSeconds" style="font-weight: 600; font-size: 0.875rem;">Seconds (SS):</label>
                <input type="number" id="stdSeconds" class="input-field" value="30" min="0" max="59" step="1">
            </div>
            <div>
                <label for="hourlyRate" style="font-weight: 600; font-size: 0.875rem;">Hourly Rate ($):</label>
                <input type="number" id="hourlyRate" class="input-field" value="35.00" min="0" step="0.50">
            </div>
        </div>
    </div>

    <!-- Mode 2: Decimal to Standard -->
    <div id="panelDecimal" style="display: none;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 1.25rem;">
            <div>
                <label for="decInput" style="font-weight: 600; font-size: 0.875rem;">Decimal Hours:</label>
                <input type="number" id="decInput" class="input-field" value="8.7583" min="0" step="0.0001">
            </div>
            <div>
                <label for="hourlyRate2" style="font-weight: 600; font-size: 0.875rem;">Hourly Rate ($):</label>
                <input type="number" id="hourlyRate2" class="input-field" value="35.00" min="0" step="0.50">
            </div>
        </div>
    </div>

    <!-- Mode 3: Metric Time -->
    <div id="panelMetric" style="display: none;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-bottom: 1.25rem;">
            <div>
                <label for="metricTimeInput" style="font-weight: 600; font-size: 0.875rem;">Time of Day (24-hr):</label>
                <input type="time" id="metricTimeInput" class="input-field" value="14:30" step="1">
            </div>
        </div>
    </div>

    <div style="display: flex; gap: 0.75rem; margin-bottom: 1.5rem;">
        <button type="button" class="btn btn-primary" onclick="calculateDecimalTime()">Convert Time</button>
        <button type="button" class="btn btn-outline" onclick="setCurrentTime()">Use Current Time</button>
    </div>

    <div class="result-box" style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem;">
        <h3 style="margin-top: 0; color: #1e293b; font-size: 1.1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">Converted Chronometric Results</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Decimal Hours</div>
                <div id="resDecimalHours" style="font-size: 1.4rem; font-weight: 700; color: #2563eb;">8.7583 hr</div>
                <div id="resTenthHour" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">Tenths: 8.8 hr</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Sexagesimal Time</div>
                <div id="resSexagesimal" style="font-size: 1.4rem; font-weight: 700; color: #0f172a;">08:45:30</div>
                <div id="resSexaWords" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">8h 45m 30s</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Total Duration Units</div>
                <div id="resTotalMinutes" style="font-size: 1.1rem; font-weight: 700; color: #059669;">525.5 mins</div>
                <div id="resTotalSeconds" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">31,530 seconds</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Gross Earnings</div>
                <div id="resGrossEarnings" style="font-size: 1.4rem; font-weight: 700; color: #16a34a;">$306.54</div>
                <div id="resRateEcho" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">At $35.00/hr</div>
            </div>
        </div>

        <div style="margin-top: 1.25rem; padding-top: 1rem; border-top: 1px dashed #cbd5e1; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
            <div>
                <span style="font-size: 0.85rem; font-weight: 600; color: #475569;">French Revolutionary Metric Time:</span>
                <div id="resFrenchMetric" style="font-size: 1rem; font-weight: 700; color: #7c3aed;">6h 04m 86s dec</div>
            </div>
            <div>
                <span style="font-size: 0.85rem; font-weight: 600; color: #475569;">Swatch Internet Time (.beats):</span>
                <div id="resSwatchBeats" style="font-size: 1rem; font-weight: 700; color: #d97706;">@607 .beats</div>
            </div>
            <div>
                <span style="font-size: 0.85rem; font-weight: 600; color: #475569;">Industrial Centihours:</span>
                <div id="resCentihours" style="font-size: 1rem; font-weight: 700; color: #0284c7;">875.8 c-hr</div>
            </div>
        </div>
    </div>
</div>

<script>
let currentMode = 'standard';

function switchMode(mode) {
    currentMode = mode;
    document.getElementById('panelStandard').style.display = mode === 'standard' ? 'block' : 'none';
    document.getElementById('panelDecimal').style.display = mode === 'decimal' ? 'block' : 'none';
    document.getElementById('panelMetric').style.display = mode === 'metric' ? 'block' : 'none';

    document.getElementById('tabStandard').className = mode === 'standard' ? 'btn btn-primary' : 'btn btn-outline';
    document.getElementById('tabDecimal').className = mode === 'decimal' ? 'btn btn-primary' : 'btn btn-outline';
    document.getElementById('tabMetric').className = mode === 'metric' ? 'btn btn-primary' : 'btn btn-outline';

    calculateDecimalTime();
}

function setCurrentTime() {
    const now = new Date();
    if (currentMode === 'standard') {
        document.getElementById('stdHours').value = now.getHours();
        document.getElementById('stdMinutes').value = now.getMinutes();
        document.getElementById('stdSeconds').value = now.getSeconds();
    } else if (currentMode === 'decimal') {
        const dec = now.getHours() + (now.getMinutes() / 60) + (now.getSeconds() / 3600);
        document.getElementById('decInput').value = dec.toFixed(4);
    } else {
        const h = String(now.getHours()).padStart(2, '0');
        const m = String(now.getMinutes()).padStart(2, '0');
        const s = String(now.getSeconds()).padStart(2, '0');
        document.getElementById('metricTimeInput').value = `${h}:${m}:${s}`;
    }
    calculateDecimalTime();
}

function calculateDecimalTime() {
    let totalSec = 0;
    let rate = 35.0;

    if (currentMode === 'standard') {
        const h = parseFloat(document.getElementById('stdHours').value) || 0;
        const m = parseFloat(document.getElementById('stdMinutes').value) || 0;
        const s = parseFloat(document.getElementById('stdSeconds').value) || 0;
        rate = parseFloat(document.getElementById('hourlyRate').value) || 0;
        totalSec = (h * 3600) + (m * 60) + s;
    } else if (currentMode === 'decimal') {
        const decH = parseFloat(document.getElementById('decInput').value) || 0;
        rate = parseFloat(document.getElementById('hourlyRate2').value) || 0;
        totalSec = decH * 3600;
    } else {
        const val = document.getElementById('metricTimeInput').value || '14:30:00';
        const parts = val.split(':');
        const h = parseInt(parts[0], 10) || 0;
        const m = parseInt(parts[1], 10) || 0;
        const s = parts[2] ? parseInt(parts[2], 10) : 0;
        totalSec = (h * 3600) + (m * 60) + s;
        rate = 35.0;
    }

    const decHours = totalSec / 3600;
    const totalMin = totalSec / 60;
    const grossWage = decHours * rate;

    // Sexagesimal formatting
    const outH = Math.floor(totalSec / 3600);
    const remSec = totalSec % 3600;
    const outM = Math.floor(remSec / 60);
    const outS = Math.round(remSec % 60);

    const padH = String(outH).padStart(2, '0');
    const padM = String(outM).padStart(2, '0');
    const padS = String(outS).padStart(2, '0');

    // Tenth hour (Hobbs/Aviation standard)
    const tenthHr = (Math.round(decHours * 10) / 10).toFixed(1);

    // French Revolutionary Metric Time
    // Diurnal ratio = (totalSec % 86400) / 86400
    const diurnalRatio = (totalSec % 86400) / 86400;
    const frenchSecTotal = diurnalRatio * 100000;
    const frH = Math.floor(frenchSecTotal / 10000);
    const frRem = frenchSecTotal % 10000;
    const frM = Math.floor(frRem / 100);
    const frS = Math.floor(frRem % 100);

    // Swatch Internet Time (.beats): based on UTC+1 (Biel Mean Time, 3600s offset)
    // Here we compute based on diurnal ratio: 1000 beats per day
    const beats = Math.floor(diurnalRatio * 1000);

    // Industrial centihours (1 hr = 100 centihours)
    const centihours = (decHours * 100).toFixed(1);

    document.getElementById('resDecimalHours').innerText = `${decHours.toFixed(4)} hr`;
    document.getElementById('resTenthHour').innerText = `Tenths: ${tenthHr} hr | 15-min: ${(Math.round(decHours * 4) / 4).toFixed(2)} hr`;
    document.getElementById('resSexagesimal').innerText = `${padH}:${padM}:${padS}`;
    document.getElementById('resSexaWords').innerText = `${outH}h ${outM}m ${outS}s`;
    document.getElementById('resTotalMinutes').innerText = `${totalMin.toLocaleString(undefined, {minimumFractionDigits: 1, maximumFractionDigits: 1})} mins`;
    document.getElementById('resTotalSeconds').innerText = `${Math.round(totalSec).toLocaleString()} seconds`;
    document.getElementById('resGrossEarnings').innerText = `$${grossWage.toFixed(2)}`;
    document.getElementById('resRateEcho').innerText = `At $${rate.toFixed(2)}/hr`;

    document.getElementById('resFrenchMetric').innerText = `${frH}h ${String(frM).padStart(2, '0')}m ${String(frS).padStart(2, '0')}s dec`;
    document.getElementById('resSwatchBeats').innerText = `@${String(beats).padStart(3, '0')} .beats`;
    document.getElementById('resCentihours').innerText = `${centihours} c-hr`;
}

window.addEventListener('DOMContentLoaded', () => {
    ['stdHours', 'stdMinutes', 'stdSeconds', 'hourlyRate', 'decInput', 'hourlyRate2', 'metricTimeInput'].forEach(id => {
        const el = document.getElementById(id);
        if (el) {
            el.addEventListener('input', calculateDecimalTime);
            el.addEventListener('change', calculateDecimalTime);
        }
    });
    calculateDecimalTime();
});
</script>"""

    article = """<h2>Mathematical Principles of Decimal Time Conversion</h2>
<p>In standard daily chronology, human civilization measures time using the classical sexagesimal (base-60) system inherited from ancient Babylonian astronomy. While division into 24 hours, 60 minutes, and 60 seconds is culturally entrenched, base-60 arithmetic creates friction in modern computational workflows, financial accounting, payroll processing, and aerospace logging. <strong>Decimal time</strong> resolves this friction by expressing time intervals as continuous base-10 fractions.</p>

<p>The algebraic conversion from standard sexagesimal time comprising hours $H$, minutes $M$, and seconds $S$ into continuous decimal hours $T_{\text{decimal}}$ is governed by the following exact rational formulation:</p>

$$T_{\text{decimal}} = H + \frac{M}{60} + \frac{S}{3600}$$

<p>Conversely, reversing a decimal hour value $T_{\text{decimal}}$ back into discrete sexagesimal components $(H, M, S)$ requires sequential floor integer extraction and modulo operations:</p>

$$H = \lfloor T_{\text{decimal}} \rfloor$$
$$M = \lfloor (T_{\text{decimal}} - H) \times 60 \rfloor$$
$$S = \left( (T_{\text{decimal}} - H) \times 60 - M \right) \times 60$$

<p>Where $\lfloor x \rfloor$ denotes the greatest integer function (floor operator). For instance, an elapsed duration of 8 hours, 45 minutes, and 30 seconds evaluates as:</p>

$$T_{\text{decimal}} = 8 + \frac{45}{60} + \frac{30}{3600} = 8 + 0.75 + 0.008333\dots = 8.758333\dots \text{ hours}$$

<h2>Industrial and Payroll Rounding Conventions</h2>
<p>Modern enterprise resource planning (ERP) platforms and automated punch-clock systems routinely translate raw biometric or badge timestamps into standardized decimal increments. In industrial engineering and payroll management, three primary rounding conventions predominate:</p>

<h3>1. Hundredths of an Hour (Centihours)</h3>
<p>In industrial production time-and-motion studies (such as Methods-Time Measurement or MTM) and contemporary corporate payroll, time is measured in <strong>centihours</strong> ($1 \text{ c-hr} = 0.01 \text{ hour} = 36 \text{ seconds}$). An employee clocking 37 minutes records $37/60 \approx 0.6167 \text{ hours}$, rounded to $0.62$ decimal hours (62 centihours). Multiplying directly by hourly compensation yields mathematically uniform paycheck disbursements.</p>

<h3>2. Tenths of an Hour (6-Minute Increments &amp; Aviation Hobbs)</h3>
<p>Aircraft engines and general aviation rental facilities utilize an electromechanical or digital chronometer known as a <strong>Hobbs Meter</strong>. Hobbs meters increment in tenths of an hour ($0.10 \text{ hr} = 6.0 \text{ minutes}$). Pilots log cross-country flight time, instrument flight time, and airframe maintenance cycles in tenths of an hour (e.g., $1.4$ hours rather than 1 hour and 24 minutes). Legal billing practices in law firms also traditionally track client consultation in 6-minute tenths.</p>

<h3>3. Quarter-Hour Rounding (FLSA 7/8-Minute Rule)</h3>
<p>Under Title 29, Section 785.48 of the United States Code of Federal Regulations, employers may round clock punches to the nearest quarter hour ($0.25 \text{ hr} = 15 \text{ minutes}$). The statutory standard enforces the asymmetric 7-minute rounding window: punches within 1 to 7 minutes after a quarter hour round down, whereas punches from 8 to 14 minutes round up to the next quarter hour.</p>

<h3>Sexagesimal to Decimal Conversion Reference Matrix</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Minutes ($MM$)</th>
            <th>Fractional Ratio</th>
            <th>Decimal Hours</th>
            <th>Tenth-Hour (Hobbs)</th>
            <th>Quarter-Hour (FLSA)</th>
            <th>Centihours</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>03 mins</td><td>3 / 60</td><td>0.0500 hr</td><td>0.1 hr</td><td>0.00 hr</td><td>5 c-hr</td></tr>
        <tr><td>06 mins</td><td>6 / 60</td><td>0.1000 hr</td><td>0.1 hr</td><td>0.00 hr</td><td>10 c-hr</td></tr>
        <tr><td>15 mins</td><td>15 / 60</td><td>0.2500 hr</td><td>0.3 hr</td><td>0.25 hr</td><td>25 c-hr</td></tr>
        <tr><td>20 mins</td><td>20 / 60</td><td>0.3333 hr</td><td>0.3 hr</td><td>0.25 hr</td><td>33 c-hr</td></tr>
        <tr><td>30 mins</td><td>30 / 60</td><td>0.5000 hr</td><td>0.5 hr</td><td>0.50 hr</td><td>50 c-hr</td></tr>
        <tr><td>40 mins</td><td>40 / 60</td><td>0.6667 hr</td><td>0.7 hr</td><td>0.75 hr</td><td>67 c-hr</td></tr>
        <tr><td>45 mins</td><td>45 / 60</td><td>0.7500 hr</td><td>0.8 hr</td><td>0.75 hr</td><td>75 c-hr</td></tr>
        <tr><td>50 mins</td><td>50 / 60</td><td>0.8333 hr</td><td>0.8 hr</td><td>0.75 hr</td><td>83 c-hr</td></tr>
        <tr><td>54 mins</td><td>54 / 60</td><td>0.9000 hr</td><td>0.9 hr</td><td>1.00 hr</td><td>90 c-hr</td></tr>
        <tr><td>60 mins</td><td>60 / 60</td><td>1.0000 hr</td><td>1.0 hr</td><td>1.00 hr</td><td>100 c-hr</td></tr>
    </tbody>
</table>

<h2>Alternative Metric Time Systems in History and Technology</h2>

<h3>French Revolutionary Decimal Time (1793–1795)</h3>
<p>Following the French Revolution, the National Convention decreed a total metrication of the calendar and diurnal cycle. Under the decree of 4 Frimaire Year II (November 24, 1793), each mean solar day was divided into:</p>
<ul>
    <li>$1 \text{ day} = 10 \text{ decimal hours}$</li>
    <li>$1 \text{ decimal hour} = 100 \text{ decimal minutes}$ ($1 \text{ dec-hr} = 2.4 \text{ standard hours} = 144 \text{ standard minutes}$)</li>
    <li>$1 \text{ decimal minute} = 100 \text{ decimal seconds}$ ($1 \text{ dec-min} = 1.44 \text{ standard minutes} = 86.4 \text{ standard seconds}$)</li>
    <li>$1 \text{ day} = 100,000 \text{ decimal seconds}$ (compared to $86,400$ standard SI seconds)</li>
</ul>
<p>Under French metric time, solar noon occurred at precisely 5:00:00, and midnight at 10:00:00 (or 0:00:00). Despite its mathematical elegance, the metric time system was repealed after just 17 months due to widespread public confusion and the prohibitive expense of replacing mechanical pendulum clocks throughout Europe.</p>

<h3>Swatch Internet Time (.beats)</h3>
<p>In 1998, Swiss horological manufacturer Swatch introduced <strong>Swatch Internet Time</strong> as a global, timezone-free chronometric standard for the nascent World Wide Web. The system divides the 24-hour day into 1,000 equal units designated as <strong>.beats</strong>:</p>

$$1 \text{ .beat} = \frac{86,400 \text{ seconds}}{1000} = 86.4 \text{ SI seconds} = 1 \text{ minute and } 26.4 \text{ seconds}$$

<p>Internet time references a single universal meridian: <strong>Biel Mean Time (BMT)</strong>, centered on Swatch headquarters in Biel, Switzerland (equivalent to UTC+1 or Central European Time). Midday in Biel corresponds to <code>@500 .beats</code>, and midnight to <code>@000 .beats</code>, creating an identical time display worldwide without daylight saving or regional time zone offsets.</p>

<div class="worked-example-card">
    <h3>Worked Engineering Case Study: Corporate Payroll and Commercial Aviation Flight Log</h3>
    <p><strong>Scenario:</strong> A commercial pilot and flight instructor flies a training sortie logged from 08:35 to 13:17. The instructor charges $65.00 per hour, while the aircraft wet rental rate is billed at $175.00 per Hobbs hour (tenths of an hour). Calculate: (1) exact elapsed sexagesimal duration, (2) exact payroll decimal hours, (3) rounded Hobbs flight hours, (4) total instructor compensation, and (5) aircraft rental cost.</p>
    
    <div class="step-solution">
        <h4>Step 1: Calculate Elapsed Duration</h4>
        <p>Start: $08:35 = (8 \times 60) + 35 = 515 \text{ minutes}$.</p>
        <p>End: $13:17 = (13 \times 60) + 17 = 797 \text{ minutes}$.</p>
        $$T_{\text{elapsed}} = 797 - 515 = 282 \text{ minutes} = 4 \text{ hours and } 42 \text{ minutes}$$

        <h4>Step 2: Convert to Exact Decimal Hours</h4>
        $$T_{\text{decimal}} = 4 + \frac{42}{60} = 4 + 0.70 = 4.7000 \text{ hours}$$

        <h4>Step 3: Evaluate Hobbs Tenths of an Hour</h4>
        $$\text{Hobbs Hours} = 4.7 \text{ hours (since } 42 \text{ minutes is exactly } 7 \times 6 \text{ minutes)}$$

        <h4>Step 4: Compute Instructor Fee</h4>
        $$\text{Instructor Fee} = 4.7000 \times \$65.00 = \$305.50$$

        <h4>Step 5: Compute Aircraft Wet Rental Fee</h4>
        $$\text{Aircraft Rental} = 4.7 \times \$175.00 = \$822.50$$
        <p><strong>Combined Flight Cost:</strong> $\$305.50 + \$822.50 = \$1,128.00$.</p>
    </div>
</div>

<h2>Common Calculation Errors in Decimal Time</h2>
<ol>
    <li><strong>Directly Appending Minutes as Decimals:</strong> The single most prevalent payroll error occurs when human operators mistake 45 minutes for 0.45 hours (recording 8:45 as 8.45 instead of 8.75). Because 45 minutes represents three-quarters of an hour, calculating compensation using 8.45 shorts an employee by 0.30 hours ($18 \text{ minutes}$) of wages on every shift.</li>
    <li><strong>Premature Truncation in Modulo Division:</strong> Rounding intermediate sexagesimal seconds to two decimal places before dividing minutes induces systematic floating-point drift in large-scale enterprise timesheet databases. High-precision payroll engines always retain minimum 4 to 6 decimal digits ($8.7583\dots$) prior to final dollar rounding.</li>
    <li><strong>Disregarding Unpaid Statutory Meal Breaks:</strong> Gross clock durations must have mandatory 30- or 60-minute unpaid intervals subtracted in net minutes before converting to decimal pay hours.</li>
</ol>

<section class="faq-section">
    <h2>Frequently Asked Questions About Decimal Time</h2>
    <div class="faq-item">
        <h3>How do you convert minutes to decimal hours for payroll?</h3>
        <p>Divide the number of minutes by 60. For example, 45 minutes divided by 60 is 0.75 decimal hours. Total time of 8 hours and 45 minutes equals 8.75 decimal hours.</p>
    </div>
    <div class="faq-item">
        <h3>What is French Revolutionary metric time?</h3>
        <p>Introduced in 1793 during the French Revolution, metric time divides the diurnal solar day into 10 decimal hours, each hour into 100 decimal minutes, and each minute into 100 decimal seconds (100,000 decimal seconds per day).</p>
    </div>
    <div class="faq-item">
        <h3>What is Swatch Internet Time (.beat)?</h3>
        <p>Introduced by the Swatch Group in 1998, Swatch Internet Time divides a solar day into 1000 .beats, based on Biel Mean Time (UTC+1). One .beat equals exactly 86.4 seconds.</p>
    </div>
    <div class="faq-item">
        <h3>Why do aviation logbooks and payroll systems use decimal hours?</h3>
        <p>Decimal hours eliminate sexagesimal base-60 fractions, making arithmetic multiplication with hourly wage rates or aircraft fuel burn rates trivial and error-free.</p>
    </div>
</section>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article)


# ===========================================================================
# TOOL 4: leap-year-calculator.html
# ===========================================================================
def gen_leap_year():
    slug = "leap-year-calculator"
    title = "Leap Year Calculator | Gregorian Algorithm & Astronomical Drift"
    desc = "Check if any year is a leap year using the Gregorian 400-year algorithmic rules. Discover upcoming leap years, tropical solar year physics, and calendar history."
    h1 = "Leap Year Calculator"
    short_desc = "Verify whether any year in the past, present, or future is an intercalary leap year using the Gregorian quadrennial, centurial, and quadricenturial algorithmic rules."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Leap Year Calculator",
      "url": "https://calchub.com/leap-year-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Calculates whether a year is a leap year, explains the 400-year Gregorian cycle, and lists upcoming leap years."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the exact 3-step Gregorian rule for leap years?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A year is a leap year if: (1) it is evenly divisible by 4, EXCEPT (2) if it is divisible by 100, it is NOT a leap year, UNLESS (3) it is also divisible by 400, in which case it IS a leap year."
          }
        },
        {
          "@type": "Question",
          "name": "Why was the year 2000 a leap year but 1900 was not?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Both 1900 and 2000 are century years divisible by 100. However, 1900 is not divisible by 400 (1900 / 400 = 4.75), making it a common year. Year 2000 is evenly divisible by 400 (2000 / 400 = 5), making it a rare quadricenturial leap year."
          }
        },
        {
          "@type": "Question",
          "name": "What is the next leap year after 2024?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The next leap year after 2024 is 2028, followed by 2032, 2036, and 2040."
          }
        },
        {
          "@type": "Question",
          "name": "Why do leap years exist in astronomy?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The astronomical tropical year (the time it takes Earth to orbit the Sun from equinox to equinox) is approximately 365.2422 solar days. Without intercalary leap days, the calendar would drift approximately 1 day every 4 years, causing seasons to shift completely over centuries."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-body">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.25rem; margin-bottom: 1.5rem;">
        <div>
            <label for="yearInput" style="font-weight: 600; font-size: 0.875rem;">Year to Check (YYYY):</label>
            <input type="number" id="yearInput" class="input-field" value="2024" min="1" max="9999" step="1">
            <span class="input-hint">Enter any CE / AD calendar year (e.g. 1900, 2000, 2024, 2028)</span>
        </div>
        <div style="display: flex; align-items: flex-end; gap: 0.5rem;">
            <button type="button" class="btn btn-primary" onclick="checkLeapYear()">Check Year</button>
            <button type="button" class="btn btn-outline" onclick="setCurrentYear()">Current Year</button>
        </div>
    </div>

    <div class="result-box" style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem;">
        <div id="statusBanner" style="padding: 1rem; border-radius: 6px; margin-bottom: 1.25rem; font-weight: 700; font-size: 1.2rem; text-align: center; background: #dcfce7; color: #15803d; border: 1px solid #86efac;">
            2024 IS A LEAP YEAR! (366 Days)
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-bottom: 1.25rem;">
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Total Days in Year</div>
                <div id="resTotalDays" style="font-size: 1.4rem; font-weight: 700; color: #2563eb;">366 Days</div>
                <div id="resTotalHours" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">8,784 Hours</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Days in February</div>
                <div id="resFebDays" style="font-size: 1.4rem; font-weight: 700; color: #0f172a;">29 Days</div>
                <div style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">February 29 Present</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Previous Leap Year</div>
                <div id="resPrevLeap" style="font-size: 1.2rem; font-weight: 700; color: #475569;">2020</div>
                <div style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">4 years prior</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Next Leap Year</div>
                <div id="resNextLeap" style="font-size: 1.2rem; font-weight: 700; color: #16a34a;">2028</div>
                <div style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">4 years ahead</div>
            </div>
        </div>

        <h4 style="margin: 1rem 0 0.5rem 0; font-size: 0.95rem; color: #334155;">Gregorian 3-Step Algorithmic Verification:</h4>
        <div style="background: white; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.75rem; font-size: 0.875rem;">
            <div id="ruleStep1" style="margin-bottom: 0.35rem; color: #16a34a;">&#x2714; Divisible by 4? 2024 / 4 = 506 (Remainder 0) &rarr; YES</div>
            <div id="ruleStep2" style="margin-bottom: 0.35rem; color: #2563eb;">&#x2714; Divisible by 100? 2024 / 100 = 20.24 (Remainder 24) &rarr; NOT A CENTURY YEAR</div>
            <div id="ruleStep3" style="color: #64748b;">&bull; Divisible by 400? N/A (Standard quadrennial leap year)</div>
        </div>

        <h4 style="margin: 1.25rem 0 0.5rem 0; font-size: 0.95rem; color: #334155;">Surrounding Leap Years Sequence:</h4>
        <div id="surroundingYears" style="display: flex; flex-wrap: wrap; gap: 0.5rem; font-size: 0.85rem;">
            <!-- Generated dynamically -->
        </div>
    </div>
</div>

<script>
function isLeap(y) {
    return (y % 4 === 0 && y % 100 !== 0) || (y % 400 === 0);
}

function setCurrentYear() {
    document.getElementById('yearInput').value = new Date().getFullYear();
    checkLeapYear();
}

function checkLeapYear() {
    const y = parseInt(document.getElementById('yearInput').value, 10);
    if (isNaN(y) || y < 1) return;

    const div4 = (y % 4 === 0);
    const div100 = (y % 100 === 0);
    const div400 = (y % 400 === 0);
    const leap = isLeap(y);

    const banner = document.getElementById('statusBanner');
    if (leap) {
        banner.style.background = '#dcfce7';
        banner.style.color = '#15803d';
        banner.style.border = '1px solid #86efac';
        banner.innerHTML = `${y} IS A LEAP YEAR! (366 Days)`;
    } else {
        banner.style.background = '#fef2f2';
        banner.style.color = '#b91c1c';
        banner.style.border = '1px solid #fca5a5';
        banner.innerHTML = `${y} IS A COMMON YEAR (365 Days)`;
    }

    document.getElementById('resTotalDays').innerText = leap ? '366 Days' : '365 Days';
    document.getElementById('resTotalHours').innerText = leap ? '8,784 Hours' : '8,760 Hours';
    document.getElementById('resFebDays').innerText = leap ? '29 Days' : '28 Days';

    // Rule explanation
    const s1 = document.getElementById('ruleStep1');
    const s2 = document.getElementById('ruleStep2');
    const s3 = document.getElementById('ruleStep3');

    if (div4) {
        s1.style.color = '#16a34a';
        s1.innerHTML = `&#x2714; Divisible by 4? ${y} &divide; 4 = ${y / 4} (Remainder 0) &rarr; YES`;
    } else {
        s1.style.color = '#dc2626';
        s1.innerHTML = `&#x2718; Divisible by 4? ${y} &divide; 4 = ${(y / 4).toFixed(2)} (Remainder ${y % 4}) &rarr; NO (Immediately Common Year)`;
    }

    if (div100) {
        s2.style.color = '#ea580c';
        s2.innerHTML = `&#x26A0; Divisible by 100? ${y} &divide; 100 = ${y / 100} &rarr; CENTURY YEAR (Requires 400-year check)`;
        if (div400) {
            s3.style.color = '#16a34a';
            s3.innerHTML = `&#x2714; Divisible by 400? ${y} &divide; 400 = ${y / 400} (Remainder 0) &rarr; QUADRICENTURIAL LEAP YEAR!`;
        } else {
            s3.style.color = '#dc2626';
            s3.innerHTML = `&#x2718; Divisible by 400? ${y} &divide; 400 = ${(y / 400).toFixed(2)} &rarr; NOT divisible by 400 &rarr; COMMON CENTURY YEAR`;
        }
    } else {
        s2.style.color = '#2563eb';
        s2.innerHTML = `&#x2714; Divisible by 100? ${y} &divide; 100 = ${(y / 100).toFixed(2)} &rarr; NOT A CENTURY YEAR (Rule 1 holds)`;
        s3.style.color = '#64748b';
        s3.innerHTML = `&bull; Divisible by 400? Skipped (Century rule does not apply)`;
    }

    // Previous and next leap years
    let prev = y - 1;
    while (prev > 0 && !isLeap(prev)) prev--;
    let next = y + 1;
    while (!isLeap(next)) next++;

    document.getElementById('resPrevLeap').innerText = prev > 0 ? prev : 'N/A';
    document.getElementById('resNextLeap').innerText = next;

    // Surrounding 5 leap years
    const surrounding = [];
    let cur = y - 12;
    while (surrounding.length < 7 && cur < y + 25) {
        if (cur > 0 && isLeap(cur)) {
            surrounding.push(cur);
        }
        cur++;
    }

    const pillsHtml = surrounding.map(yr => {
        const isCurrent = (yr === y);
        const bg = isCurrent ? '#2563eb' : '#e2e8f0';
        const color = isCurrent ? '#ffffff' : '#1e293b';
        return `<span style="background: ${bg}; color: ${color}; padding: 0.25rem 0.6rem; border-radius: 9999px; font-weight: 600;">${yr}</span>`;
    }).join(' ');

    document.getElementById('surroundingYears').innerHTML = pillsHtml;
}

window.addEventListener('DOMContentLoaded', () => {
    document.getElementById('yearInput').addEventListener('input', checkLeapYear);
    document.getElementById('yearInput').addEventListener('change', checkLeapYear);
    checkLeapYear();
});
</script>"""

    article = """<h2>Astronomical Foundations of the Tropical Year</h2>
<p>A calendar year is fundamentally an attempt to synchronize civil human society with the orbital mechanics of our solar system. An astronomical <strong>Tropical Year</strong> (also known as the solar year) is defined as the precise duration required for the Earth to complete one full revolution around the Sun relative to the vernal equinox ($0^\circ$ ecliptic longitude). In modern ephemeris astronomy (J2000.0 epoch), the mean tropical year evaluates to:</p>

$$T_{\text{tropical}} \approx 365.242189 \text{ ephemeris solar days} \approx 365 \text{ days, } 5 \text{ hours, } 48 \text{ minutes, and } 45.19 \text{ seconds}$$

<p>Because an integer civil year consists of exactly 365 calendar days ($8,760 \text{ hours}$), an unadjusted calendar accumulates a deficit of approximately $0.242189 \text{ days}$ (nearly six hours) each year. Without systematic intercalation (adding extra days), seasonal events—such as the summer solstice, autumn harvest, and winter freezes—would slowly drift through the calendar at a rate of roughly 24 days per century, completely inverting the agricultural calendar across several hundred years.</p>

<h2>The Gregorian 400-Year Cycle Algorithm</h2>
<p>To eliminate calendar drift, Julius Caesar instituted the Julian calendar in 45 BCE, introducing an intercalary day every four years ($365.25 \text{ days}$ average). However, because $365.25 > 365.2422$, the Julian calendar overcorrected by approximately 11 minutes and 14 seconds annually. By 1582 CE, the calendar had drifted out of synchronization with the vernal equinox by 10 full days.</p>

<p>To rectify this error, Pope Gregory XIII promulgated the papal bull <em>Inter gravissimas</em> in October 1582, introducing the <strong>Gregorian Calendar Algorithm</strong>. The modern algorithm enforces three sequential mathematical tests:</p>

$$\text{IsLeapYear}(Y) = \begin{cases} 
\text{True} & \text{if } (Y \bmod 4 = 0 \land Y \bmod 100 \neq 0) \lor (Y \bmod 400 = 0) \\ 
\text{False} & \text{otherwise} 
\end{cases}$$

<p>This formulation establishes three strict hierarchical rules:</p>
<ol>
    <li><strong>The Quadrennial Rule:</strong> Every year evenly divisible by 4 is a leap year (e.g., 2024, 2028, 2032).</li>
    <li><strong>The Centurial Exception:</strong> If a year is evenly divisible by 100, it is <strong>not</strong> a leap year (e.g., 1700, 1800, 1900, 2100).</li>
    <li><strong>The Quadricenturial Exception:</strong> If a year is evenly divisible by 400, it <strong>is</strong> a leap year despite ending in double zeroes (e.g., 1600, 2000, 2400).</li>
</ol>

<h3>Mathematical Analysis of the 400-Year Cycle</h3>
<p>Across a complete 400-year Gregorian cycle, the distribution of common and leap years is evaluated as follows:</p>

$$\text{Total Years} = 400$$
$$\text{Quadrennial Candidates} = \frac{400}{4} = 100$$
$$\text{Centurial Exclusions} = \frac{400}{100} = 4$$
$$\text{Quadricenturial Inclusions} = \frac{400}{400} = 1$$
$$\text{Net Leap Years} = 100 - 4 + 1 = 97 \text{ leap years}$$

<p>The average length of a Gregorian calendar year over the 400-year cycle evaluates to:</p>

$$\bar{T}_{\text{Gregorian}} = \frac{(303 \times 365) + (97 \times 366)}{400} = \frac{110,595 + 35,502}{400} = \frac{146,097}{400} = 365.2425 \text{ days}$$

<p>Comparing the Gregorian average ($365.242500$) with the astronomical tropical year ($365.242189$) reveals an annual discrepancy of just $+0.000311 \text{ days}$ (approximately 26.8 seconds per year). The Gregorian calendar requires approximately <strong>3,215 years</strong> to accumulate a single day of error!</p>

<h3>Comparative Planetary &amp; Calendrical Intercalation Matrix</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Calendar System</th>
            <th>Cycle Length</th>
            <th>Leap Years in Cycle</th>
            <th>Mean Year Length</th>
            <th>Annual Drift vs. Tropical Year</th>
            <th>Time to Accumulate 1 Day Error</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Egyptian Civil</td><td>1 Year</td><td>0</td><td>365.0000 days</td><td>-0.242189 days</td><td>~4.1 years</td></tr>
        <tr><td>Julian (45 BCE)</td><td>4 Years</td><td>1</td><td>365.2500 days</td><td>+0.007811 days</td><td>~128 years</td></tr>
        <tr><td>Gregorian (1582)</td><td>400 Years</td><td>97</td><td>365.2425 days</td><td>+0.000311 days</td><td>~3,215 years</td></tr>
        <tr><td>Revised Julian (Milanković)</td><td>900 Years</td><td>218</td><td>365.242222 days</td><td>+0.000033 days</td><td>~30,300 years</td></tr>
        <tr><td>Persian Jalali (Solar Hijri)</td><td>2,820 Years</td><td>683</td><td>365.242198 days</td><td>+0.000009 days</td><td>~110,000 years</td></tr>
    </tbody>
</table>

<h2>Financial and Algorithmic Implications of Leap Years</h2>

<h3>1. Bond Accrual and Day-Count Conventions</h3>
<p>In fixed-income financial engineering, interest accrual between payment dates depends strictly on legal day-count conventions. Under the <strong>Actual/Actual ICMA</strong> standard, the annual coupon is divided by 366 during a leap year and 365 in common years. Under <strong>Actual/360</strong> (prevalent in US money markets and commercial loans), the extra day in February adds a 366th day of accrued interest, yielding an annualized excess cost of $1/360 \approx 0.278\%$ on outstanding principal.</p>

<h3>2. The Infamous Zune Leap Year Bug (December 31, 2008)</h3>
<p>On December 31, 2008 (a leap year), millions of Microsoft Zune 30GB media players froze simultaneously across the globe. The root cause was an infinite loop in the driver clock routine <code>SetTimes()</code>. The algorithm repeatedly decremented elapsed days by 366 for leap years and 365 for common years. On day 366, the loop checked <code>days > 365</code>, saw <code>days = 366</code> in a leap year, but failed to exit because the condition deducted 366 only if <code>days > 366</code>, locking the device into an infinite loop until the battery drained or midnight struck.</p>

<div class="worked-example-card">
    <h3>Worked Mathematical Case Study: Century Boundary Verification (1900 vs 2000 vs 2100)</h3>
    <p><strong>Scenario:</strong> An enterprise database architect is auditing legacy chronological stored procedures to verify date handling across century boundaries. Evaluate the leap year status of years <strong>1900</strong>, <strong>2000</strong>, and <strong>2100</strong> using the Gregorian algorithm.</p>
    
    <div class="step-solution">
        <h4>Audit 1: Year 1900</h4>
        <p>Step 1: $1900 \bmod 4 = 0$ (Passes quadrennial check).</p>
        <p>Step 2: $1900 \bmod 100 = 0$ (Century year exception triggered).</p>
        <p>Step 3: $1900 \bmod 400 = 300 \neq 0$ ($1900 / 400 = 4.75$).</p>
        <p><strong>Result:</strong> <strong>Common Year (365 Days)</strong>. February 1900 had only 28 days.</p>

        <h4>Audit 2: Year 2000</h4>
        <p>Step 1: $2000 \bmod 4 = 0$ (Passes quadrennial check).</p>
        <p>Step 2: $2000 \bmod 100 = 0$ (Century year exception triggered).</p>
        <p>Step 3: $2000 \bmod 400 = 0$ ($2000 / 400 = 5.0$).</p>
        <p><strong>Result:</strong> <strong>Leap Year (366 Days)</strong>! Year 2000 was a rare quadricenturial leap year with February 29 present.</p>

        <h4>Audit 3: Year 2100</h4>
        <p>Step 1: $2100 \bmod 4 = 0$ (Passes quadrennial check).</p>
        <p>Step 2: $2100 \bmod 100 = 0$ (Century year exception triggered).</p>
        <p>Step 3: $2100 \bmod 400 = 100 \neq 0$ ($2100 / 400 = 5.25$).</p>
        <p><strong>Result:</strong> <strong>Common Year (365 Days)</strong>. February 2100 will have only 28 days.</p>
    </div>
</div>

<h2>Common Implementation Pitfalls in Software Development</h2>
<ol>
    <li><strong>Assuming Divisible by 4 is Sufficient:</strong> The most frequent bug in junior developer code is writing <code>if (year % 4 == 0) return true;</code> without checking the century and 400-year exceptions. This incorrectly marks 1900, 2100, 2200, and 2300 as leap years.</li>
    <li><strong>Leap Seconds vs. Leap Years:</strong> Leap years adjust for the Earth's orbital period around the Sun ($~365.2422 \text{ days}$). In contrast, <strong>Leap Seconds</strong> adjust UTC atomic clocks for variations in Earth's axial rotation speed (tidal friction slowing the day by milliseconds). Leap years occur predictably in February; leap seconds are announced by the International Earth Rotation and Reference Systems Service (IERS) in June or December.</li>
    <li><strong>Historical Retroactivity (Proleptic Calendar):</strong> Applying the Gregorian algorithm to dates prior to October 15, 1582 creates a "Proleptic Gregorian Calendar," which does not match real historical records of the Roman, Byzantine, or medieval European eras.</li>
</ol>

<section class="faq-section">
    <h2>Frequently Asked Questions About Leap Years</h2>
    <div class="faq-item">
        <h3>What is the exact 3-step Gregorian rule for leap years?</h3>
        <p>A year is a leap year if: (1) it is evenly divisible by 4, EXCEPT (2) if it is divisible by 100, it is NOT a leap year, UNLESS (3) it is also divisible by 400, in which case it IS a leap year.</p>
    </div>
    <div class="faq-item">
        <h3>Why was the year 2000 a leap year but 1900 was not?</h3>
        <p>Both 1900 and 2000 are century years divisible by 100. However, 1900 is not divisible by 400 (1900 / 400 = 4.75), making it a common year. Year 2000 is evenly divisible by 400 (2000 / 400 = 5), making it a rare quadricenturial leap year.</p>
    </div>
    <div class="faq-item">
        <h3>What is the next leap year after 2024?</h3>
        <p>The next leap year after 2024 is 2028, followed by 2032, 2036, and 2040.</p>
    </div>
    <div class="faq-item">
        <h3>Why do leap years exist in astronomy?</h3>
        <p>The astronomical tropical year (the time it takes Earth to orbit the Sun from equinox to equinox) is approximately 365.2422 solar days. Without intercalary leap days, the calendar would drift approximately 1 day every 4 years, causing seasons to shift completely over centuries.</p>
    </div>
</section>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article)


def main():
    dec_html = gen_decimal_time()
    with open(os.path.join(BASE_DIR, "decimal-time-calculator.html"), "w", encoding="utf-8") as f:
        f.write(dec_html)
    print("Generated decimal-time-calculator.html successfully!")

    leap_html = gen_leap_year()
    with open(os.path.join(BASE_DIR, "leap-year-calculator.html"), "w", encoding="utf-8") as f:
        f.write(leap_html)
    print("Generated leap-year-calculator.html successfully!")

if __name__ == "__main__":
    main()
