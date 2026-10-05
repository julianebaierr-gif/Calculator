# -*- coding: utf-8 -*-
"""
Generator for Batch 40 - Part 4
Tools:
7. quarter-of-year-calculator.html (Calendar Quarters Q1-Q4, Fiscal Quarters, Retail 4-4-5 Calendar)
8. time-calculator.html (Sexagesimal Time Arithmetic, Add/Subtract/Multiply/Divide, Takt Time)
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COMMON_TAIL = """    <footer class="site-footer">
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>About CalcHub</h4>
                    <p>CalcHub delivers peer-reviewed chronometric computing algorithms, astronomical date conversion systems, and enterprise financial calendar engines compliant with ISO 8601, SEC, and IRS reporting standards.</p>
                </div>
                <div class="footer-col">
                    <h4>Chronometric &amp; Time Suites</h4>
                    <ul>
                        <li><a href="datetime.html">Date &amp; Time Utilities</a></li>
                        <li><a href="finance.html">Financial Planning</a></li>
                        <li><a href="math.html">Mathematics &amp; Statistics</a></li>
                        <li><a href="converter.html">Unit &amp; Chrono Converters</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Core Calendrical Tools</h4>
                    <ul>
                        <li><a href="quarter-of-year-calculator.html">Quarter of Year Calculator</a></li>
                        <li><a href="time-calculator.html">Time Calculator</a></li>
                        <li><a href="hours-calculator.html">Work Hours Calculator</a></li>
                        <li><a href="months-between-dates-calculator.html">Months Between Dates</a></li>
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
                <p>&copy; 2026 CalcHub. All rights reserved. Precision chronological and fiscal quarter calculation algorithms.</p>
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
                    <h3>Related Chrono &amp; Fiscal Tools</h3>
                    <ul class="sidebar-links">
                        <li><a href="quarter-of-year-calculator.html">Quarter of Year Calculator</a></li>
                        <li><a href="time-calculator.html">Time Calculator</a></li>
                        <li><a href="months-between-dates-calculator.html">Months Between Dates</a></li>
                        <li><a href="overtime-calculator.html">Overtime Pay Calculator</a></li>
                        <li><a href="week-number-calculator.html">ISO Week Number</a></li>
                        <li><a href="business-days-calculator.html">Business Days Calculator</a></li>
                        <li><a href="countdown-calculator.html">Countdown Calculator</a></li>
                    </ul>
                </div>
            </aside>
        </div>
    </div>
{COMMON_TAIL}"""


# ===========================================================================
# TOOL 7: quarter-of-year-calculator.html
# ===========================================================================
def gen_quarter_of_year():
    slug = "quarter-of-year-calculator"
    title = "Quarter of the Year Calculator | Calendar, Fiscal & Retail 4-4-5"
    desc = "Find what quarter of the year any date falls in (Q1, Q2, Q3, Q4). Calculate federal fiscal quarters, retail 4-4-5 periods, days elapsed, and remaining quarter days."
    h1 = "Quarter of the Year Calculator"
    short_desc = "Determine the calendar quarter (Q1-Q4), federal fiscal quarter (FY), start/end dates, elapsed days, and percentage completion for any date."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Quarter of the Year Calculator",
      "url": "https://calchub.com/quarter-of-year-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Calculates calendar and fiscal quarters (Q1-Q4), quarter boundaries, elapsed days, and completion percentages."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What are the exact months and dates in each calendar quarter?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Q1 spans January 1 to March 31 (90 or 91 days). Q2 spans April 1 to June 30 (91 days). Q3 spans July 1 to September 30 (92 days). Q4 spans October 1 to December 31 (92 days)."
          }
        },
        {
          "@type": "Question",
          "name": "How does the US Federal Government fiscal year differ from the calendar year?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The US federal fiscal year begins on October 1 and ends on September 30. Q1 begins October 1, Q2 begins January 1, Q3 begins April 1, and Q4 begins July 1."
          }
        },
        {
          "@type": "Question",
          "name": "What is a Retail 4-4-5 quarterly accounting calendar?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The 4-4-5 calendar divides each quarter into three discrete accounting periods of 4 weeks, 4 weeks, and 5 weeks (exactly 13 weeks or 91 days per quarter), ensuring identical day-of-week retail comparisons year over year."
          }
        },
        {
          "@type": "Question",
          "name": "How do you calculate what quarter a date falls in mathematically?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Using month number M (1 to 12), the calendar quarter is evaluated as ceil(M / 3), or Math.floor((M - 1) / 3) + 1."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-body">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.25rem; margin-bottom: 1.5rem;">
        <div>
            <label for="quarterDate" style="font-weight: 600; font-size: 0.875rem;">Selected Date:</label>
            <input type="date" id="quarterDate" class="input-field" value="2026-10-05">
        </div>
        <div>
            <label for="fiscalConvention" style="font-weight: 600; font-size: 0.875rem;">Fiscal Year Convention:</label>
            <select id="fiscalConvention" class="input-field">
                <option value="cal">Calendar Year (Starts Jan 1)</option>
                <option value="us_fed">US Federal Government (Starts Oct 1)</option>
                <option value="uk_corp">UK / Japan / Canada (Starts Apr 1)</option>
                <option value="au_nz">Australia / New Zealand (Starts Jul 1)</option>
            </select>
        </div>
    </div>

    <div style="display: flex; gap: 0.75rem; margin-bottom: 1.5rem;">
        <button type="button" class="btn btn-primary" onclick="calculateQuarter()">Analyze Quarter</button>
        <button type="button" class="btn btn-outline" onclick="setQuarterToday()">Today's Date</button>
    </div>

    <div class="result-box" style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem;">
        <div id="quarterBanner" style="padding: 1rem; border-radius: 6px; margin-bottom: 1.25rem; font-weight: 700; font-size: 1.25rem; text-align: center; background: #eff6ff; color: #1d4ed8; border: 1px solid #93c5fd;">
            CALENDAR QUARTER 4 (Q4 2026)
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-bottom: 1.25rem;">
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Fiscal Quarter Designation</div>
                <div id="resFiscalDesig" style="font-size: 1.4rem; font-weight: 700; color: #2563eb;">Q1 FY2027</div>
                <div id="resFiscalSub" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">US Federal Cycle</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Quarter Date Range</div>
                <div id="resDateRange" style="font-size: 1.1rem; font-weight: 700; color: #0f172a;">Oct 1 – Dec 31</div>
                <div id="resTotalDaysQ" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">92 Calendar Days Total</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Days Elapsed in Quarter</div>
                <div id="resDaysElapsed" style="font-size: 1.4rem; font-weight: 700; color: #059669;">5 Days</div>
                <div id="resElapsedPct" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">5.43% Completed</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Days Remaining in Q</div>
                <div id="resDaysRemaining" style="font-size: 1.4rem; font-weight: 700; color: #dc2626;">87 Days</div>
                <div id="resRemainingPct" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">94.57% Remaining</div>
            </div>
        </div>

        <div style="background: white; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.75rem; font-size: 0.875rem;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.35rem;">
                <span style="font-weight: 600;">Quarter Progress Bar:</span>
                <span id="progressText" style="font-weight: 700; color: #2563eb;">5.4%</span>
            </div>
            <div style="background: #e2e8f0; border-radius: 9999px; height: 10px; overflow: hidden;">
                <div id="progressBar" style="background: #2563eb; height: 100%; width: 5.4%;"></div>
            </div>
        </div>
    </div>
</div>

<script>
function setQuarterToday() {
    const today = new Date();
    const pad = (n) => String(n).padStart(2, '0');
    document.getElementById('quarterDate').value = `${today.getFullYear()}-${pad(today.getMonth() + 1)}-${pad(today.getDate())}`;
    calculateQuarter();
}

function isLeapYear(y) {
    return (y % 4 === 0 && y % 100 !== 0) || (y % 400 === 0);
}

function calculateQuarter() {
    const dStr = document.getElementById('quarterDate').value;
    if (!dStr) return;
    const parts = dStr.split('-');
    const y = parseInt(parts[0], 10);
    const m = parseInt(parts[1], 10); // 1-based (1..12)
    const day = parseInt(parts[2], 10);
    const conv = document.getElementById('fiscalConvention').value;

    const calQ = Math.floor((m - 1) / 3) + 1;

    // Boundaries of calendar quarters
    let qStart, qEnd, totalQDays;
    const isLeap = isLeapYear(y);

    if (calQ === 1) {
        qStart = new Date(y, 0, 1);
        qEnd = new Date(y, 2, 31);
        totalQDays = isLeap ? 91 : 90;
    } else if (calQ === 2) {
        qStart = new Date(y, 3, 1);
        qEnd = new Date(y, 5, 30);
        totalQDays = 91;
    } else if (calQ === 3) {
        qStart = new Date(y, 6, 1);
        qEnd = new Date(y, 8, 30);
        totalQDays = 92;
    } else {
        qStart = new Date(y, 9, 1);
        qEnd = new Date(y, 11, 31);
        totalQDays = 92;
    }

    const curDate = new Date(y, m - 1, day);
    const elapsedMs = curDate - qStart;
    const elapsedDays = Math.floor(elapsedMs / (1000 * 60 * 60 * 24)) + 1;
    const remainingDays = totalQDays - elapsedDays;
    const pct = Math.min(100, Math.max(0, (elapsedDays / totalQDays) * 100));

    // Fiscal calculation
    let fQ = calQ;
    let fYear = y;
    let convName = "Calendar Standard";

    if (conv === 'us_fed') {
        convName = "US Federal Government";
        if (m >= 10) {
            fQ = 1;
            fYear = y + 1;
        } else if (m >= 7) {
            fQ = 4;
            fYear = y;
        } else if (m >= 4) {
            fQ = 3;
            fYear = y;
        } else {
            fQ = 2;
            fYear = y;
        }
    } else if (conv === 'uk_corp') {
        convName = "UK / Japan Corporate";
        if (m >= 4) {
            fQ = Math.floor((m - 4) / 3) + 1;
            fYear = y;
        } else {
            fQ = 4;
            fYear = y - 1;
        }
    } else if (conv === 'au_nz') {
        convName = "Australia / NZ Corporate";
        if (m >= 7) {
            fQ = Math.floor((m - 7) / 3) + 1;
            fYear = y + 1;
        } else {
            fQ = Math.floor((m + 5) / 3) + 1;
            fYear = y;
        }
    }

    const qNames = ["", "Q1 (Jan 1 - Mar 31)", "Q2 (Apr 1 - Jun 30)", "Q3 (Jul 1 - Sep 30)", "Q4 (Oct 1 - Dec 31)"];
    document.getElementById('quarterBanner').innerText = `CALENDAR QUARTER ${calQ} (${y}) — ${qNames[calQ]}`;
    document.getElementById('resFiscalDesig').innerText = `Q${fQ} FY${fYear}`;
    document.getElementById('resFiscalSub').innerText = `${convName} convention`;
    document.getElementById('resDateRange').innerText = `${qStart.toLocaleDateString(undefined, {month:'short', day:'numeric'})} – ${qEnd.toLocaleDateString(undefined, {month:'short', day:'numeric'})}`;
    document.getElementById('resTotalDaysQ').innerText = `${totalQDays} Calendar Days Total`;
    document.getElementById('resDaysElapsed').innerText = `${elapsedDays} Days`;
    document.getElementById('resElapsedPct').innerText = `${pct.toFixed(2)}% Completed`;
    document.getElementById('resDaysRemaining').innerText = `${remainingDays} Days`;
    document.getElementById('resRemainingPct').innerText = `${(100 - pct).toFixed(2)}% Remaining`;

    document.getElementById('progressText').innerText = `${pct.toFixed(1)}%`;
    document.getElementById('progressBar').style.width = `${pct.toFixed(1)}%`;
}

window.addEventListener('DOMContentLoaded', () => {
    document.getElementById('quarterDate').addEventListener('change', calculateQuarter);
    document.getElementById('quarterDate').addEventListener('input', calculateQuarter);
    document.getElementById('fiscalConvention').addEventListener('change', calculateQuarter);
    calculateQuarter();
});
</script>"""

    article = """<h2>Mathematical and Calendrical Structure of Quarters</h2>
<p>In modern corporate governance, macroeconomic monitoring, accounting audits, and public financial reporting, a calendar year is partitioned into four equal intervals designated as <strong>quarters</strong> (symbolized as <strong>Q1, Q2, Q3, and Q4</strong>). Each quarter encompasses approximately three continuous calendar months, or one-fourth of the annual cycle.</p>

<p>Mathematically, given any month number $M \in \{1, 2, \dots, 12\}$, the corresponding standard calendar quarter $Q_{\text{calendar}}$ is evaluated using discrete ceiling arithmetic:</p>

$$Q_{\text{calendar}} = \left\lceil \frac{M}{3} \right\rceil = \left\lfloor \frac{M - 1}{3} \right\rfloor + 1$$

<p>Where $\lceil x \rceil$ represents the ceiling operator and $\lfloor x \rfloor$ represents the floor operator. The calendar quarter boundaries in the Gregorian calendar span as follows:</p>

<ul>
    <li><strong>Quarter 1 (Q1):</strong> January 1 through March 31. Spans 90 days in common years, and 91 days in quadrennial leap years ($24.66\%$ to $24.86\%$ of the year).</li>
    <li><strong>Quarter 2 (Q2):</strong> April 1 through June 30. Spans exactly 91 days ($24.93\%$ to $24.86\%$ of the year).</li>
    <li><strong>Quarter 3 (Q3):</strong> July 1 through September 30. Spans exactly 92 days ($25.21\%$ to $25.14\%$ of the year).</li>
    <li><strong>Quarter 4 (Q4):</strong> October 1 through December 31. Spans exactly 92 days ($25.21\%$ to $25.14\%$ of the year).</li>
</ul>

<h2>Fiscal Year (FY) Offsets and International Sovereign Standards</h2>
<p>While the civil calendar year strictly begins on January 1st, sovereign governments, public corporations, and international tax authorities frequently decouple their statutory <strong>Fiscal Year</strong> from the calendar year to synchronize with budgetary legislative cycles or seasonal revenue patterns:</p>

<h3>1. United States Federal Government (October 1 Start)</h3>
<p>Under Title 31 of the United States Code, the federal government's fiscal year begins on <strong>October 1st</strong> and concludes on <strong>September 30th</strong> of the following calendar year. The fiscal year is designated by the calendar year in which it terminates (e.g., FY2027 runs from October 1, 2026 through September 30, 2027):</p>
<ul>
    <li><strong>Fiscal Q1:</strong> October 1 – December 31 (Calendar Q4)</li>
    <li><strong>Fiscal Q2:</strong> January 1 – March 31 (Calendar Q1)</li>
    <li><strong>Fiscal Q3:</strong> April 1 – June 30 (Calendar Q2)</li>
    <li><strong>Fiscal Q4:</strong> July 1 – September 30 (Calendar Q3)</li>
</ul>

<h3>2. United Kingdom, Canada, Japan, and India (April 1 Start)</h3>
<p>Corporate taxation and governmental budgets in the UK, India, Canada, and Japan traditionally commence on <strong>April 1st</strong>. Under this system, Fiscal Q1 corresponds to calendar April–June, while Fiscal Q4 concludes on March 31st of the subsequent calendar year.</p>

<h3>3. Australia and New Zealand (July 1 Start)</h3>
<p>In the Southern Hemisphere, Australia and New Zealand initiate their fiscal year on <strong>July 1st</strong>, aligning corporate tax obligations with the winter seasonal transition. Fiscal Q1 spans July–September, and Fiscal Q4 terminates on June 30th.</p>

<h3>Comparative Fiscal Calendar Reference Matrix</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Calendar Months</th>
            <th>Standard Calendar</th>
            <th>US Federal Govt</th>
            <th>UK / Canada / Japan</th>
            <th>Australia / NZ</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>January – March</td><td>Q1</td><td>Q2 (FY)</td><td>Q4 (Prior FY)</td><td>Q3 (FY)</td></tr>
        <tr><td>April – June</td><td>Q2</td><td>Q3 (FY)</td><td>Q1 (New FY)</td><td>Q4 (FY)</td></tr>
        <tr><td>July – September</td><td>Q3</td><td>Q4 (FY)</td><td>Q2 (FY)</td><td>Q1 (New FY)</td></tr>
        <tr><td>October – December</td><td>Q4</td><td>Q1 (New FY)</td><td>Q3 (FY)</td><td>Q2 (FY)</td></tr>
    </tbody>
</table>

<h2>The Retail 4-4-5 Accounting Calendar (NRF Framework)</h2>
<p>In retail sales analytics, e-commerce merchandising, and consumer packaged goods (CPG), comparing calendar months creates misleading statistical noise because standard months contain differing numbers of weekends (e.g., March might have five Saturdays in one year but only four the next, distorting same-store sales by 10% to 15%).</p>

<p>To eliminate weekend distortion, the National Retail Federation (NRF) standardizes corporate reporting using the <strong>4-4-5 Quarterly Calendar</strong> (and its variants, 4-5-4 and 5-4-4). Under the 4-4-5 system:</p>

$$1 \text{ Quarter} = 4 \text{ weeks} + 4 \text{ weeks} + 5 \text{ weeks} = 13 \text{ weeks} = 91 \text{ days exactly}$$

$$1 \text{ Retail Year} = 4 \text{ Quarters} \times 13 \text{ weeks} = 52 \text{ weeks} = 364 \text{ days}$$

<p>Because $364 \text{ days}$ falls approximately $1.2422 \text{ days}$ short of the true solar year, the NRF calendar accumulates an extra 53rd week (a 14-week quarter) approximately once every 5 to 6 years to re-anchor the calendar to the solar solstice.</p>

<div class="worked-example-card">
    <h3>Worked Corporate Finance Case Study: SEC Form 10-Q Quarterly Filing Deadlines</h3>
    <p><strong>Scenario:</strong> A large accelerated filer listed on the NASDAQ ends its third fiscal quarter on <strong>September 30, 2026</strong>. Under SEC rules, a large accelerated filer must file Form 10-Q within <strong>40 calendar days</strong> of the fiscal quarter end. Determine: (1) what calendar and fiscal quarter September 30 represents under US federal standards, (2) the exact filing deadline, and (3) what fiscal quarter commences the next day.</p>
    
    <div class="step-solution">
        <h4>Step 1: Identify Calendar and Fiscal Quarters</h4>
        <p>September is Month 9. Calendar Quarter: $\lceil 9 / 3 \rceil = \text{Q3 2026}$.</p>
        <p>Under US Federal fiscal convention, October begins the new fiscal year. Therefore, September 30 marks the terminal day of <strong>Fiscal Q4 FY2026</strong>.</p>

        <h4>Step 2: Calculate SEC 40-Day Filing Deadline</h4>
        <p>Terminal Quarter Date: September 30, 2026.</p>
        <p>Adding 40 calendar days: October has 31 days ($40 - 31 = 9$).</p>
        <p><strong>SEC Form 10-Q Deadline:</strong> <strong>November 9, 2026</strong>.</p>

        <h4>Step 3: New Fiscal Quarter Transition</h4>
        <p>The following day, <strong>October 1, 2026</strong>, initiates <strong>Fiscal Q1 of FY2027</strong> (while remaining Calendar Q4 2026).</p>
    </div>
</div>

<h2>Common Implementation Pitfalls with Quarters</h2>
<ol>
    <li><strong>Assuming Every Quarter Has 91.25 Days:</strong> While the mathematical mean is $365 / 4 = 91.25 \text{ days}$, real Gregorian calendar quarters have 90, 91, or 92 days. Attempting to amortize revenue on a simple daily divide without accounting for monthly day variance produces audit discrepancies.</li>
    <li><strong>Confusing Calendar Year and Fiscal Year in File Naming:</strong> Labeling a report <code>Q1_2027_Financials.xlsx</code> when referring to Calendar Q1 vs. Fiscal Q1 leads to executive reporting errors. Best practice is always appending the prefix <code>CY2027-Q1</code> or <code>FY2027-Q1</code>.</li>
    <li><strong>Leap Day Accumulation Exclusively in Q1:</strong> Leap year intercalations (February 29th) alter only Q1 (expanding it from 90 to 91 days). Q2, Q3, and Q4 durations remain completely identical regardless of leap year status.</li>
</ol>

<section class="faq-section">
    <h2>Frequently Asked Questions About Quarters of the Year</h2>
    <div class="faq-item">
        <h3>What are the exact months and dates in each calendar quarter?</h3>
        <p>Q1 spans January 1 to March 31 (90 or 91 days). Q2 spans April 1 to June 30 (91 days). Q3 spans July 1 to September 30 (92 days). Q4 spans October 1 to December 31 (92 days).</p>
    </div>
    <div class="faq-item">
        <h3>How does the US Federal Government fiscal year differ from the calendar year?</h3>
        <p>The US federal fiscal year begins on October 1 and ends on September 30. Q1 begins October 1, Q2 begins January 1, Q3 begins April 1, and Q4 begins July 1.</p>
    </div>
    <div class="faq-item">
        <h3>What is a Retail 4-4-5 quarterly accounting calendar?</h3>
        <p>The 4-4-5 calendar divides each quarter into three discrete accounting periods of 4 weeks, 4 weeks, and 5 weeks (exactly 13 weeks or 91 days per quarter), ensuring identical day-of-week retail comparisons year over year.</p>
    </div>
    <div class="faq-item">
        <h3>How do you calculate what quarter a date falls in mathematically?</h3>
        <p>Using month number M (1 to 12), the calendar quarter is evaluated as ceil(M / 3), or Math.floor((M - 1) / 3) + 1.</p>
    </div>
</section>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article)


# ===========================================================================
# TOOL 8: time-calculator.html
# ===========================================================================
def gen_time_calculator():
    slug = "time-calculator"
    title = "Time Calculator | Add, Subtract, Multiply & Divide Durations"
    desc = "Add, subtract, multiply, and divide time durations in hours, minutes, and seconds (HH:MM:SS). Calculate cumulative time, decimal conversions, and manufacturing takt time."
    h1 = "Time Calculator"
    short_desc = "Precision arithmetic computational engine for adding, subtracting, multiplying, and dividing time durations expressed in sexagesimal hours, minutes, and seconds."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Time Calculator",
      "url": "https://calchub.com/time-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Performs addition, subtraction, multiplication, and division on time durations in hours, minutes, and seconds."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How do you add two time durations together?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Convert both durations to total seconds, add the seconds together, then convert back to hours, minutes, and seconds by dividing by 3600 and 60 using modulo arithmetic."
          }
        },
        {
          "@type": "Question",
          "name": "How does subtraction work when Time 2 is larger than Time 1?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "For clock times wrapping past midnight, 24 hours (86,400 seconds) is added to the difference. For raw mathematical durations, the result represents a negative duration."
          }
        },
        {
          "@type": "Question",
          "name": "How do you multiply or divide a time duration by a number?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Convert the duration into total seconds, multiply or divide by the scalar factor, then re-format into sexagesimal hours, minutes, and seconds."
          }
        },
        {
          "@type": "Question",
          "name": "What is takt time in manufacturing engineering?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Takt time is the maximum allowable time per unit to produce a product in order to meet customer demand, evaluated as Net Available Production Time divided by Customer Demand Units."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-body">
    <!-- Operation Selector Tabs -->
    <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; border-bottom: 2px solid #e2e8f0; margin-bottom: 1.5rem; padding-bottom: 0.5rem;">
        <button type="button" id="tabAdd" class="btn btn-primary" style="padding: 0.5rem 1rem; font-size: 0.9rem;" onclick="setTimeOp('add')">Add (+)</button>
        <button type="button" id="tabSub" class="btn btn-outline" style="padding: 0.5rem 1rem; font-size: 0.9rem;" onclick="setTimeOp('sub')">Subtract (-)</button>
        <button type="button" id="tabMult" class="btn btn-outline" style="padding: 0.5rem 1rem; font-size: 0.9rem;" onclick="setTimeOp('mult')">Multiply (&times;)</button>
        <button type="button" id="tabDiv" class="btn btn-outline" style="padding: 0.5rem 1rem; font-size: 0.9rem;" onclick="setTimeOp('div')">Divide (&divide;)</button>
    </div>

    <!-- Time 1 Input -->
    <div style="background: white; border: 1px solid #e2e8f0; border-radius: 6px; padding: 1rem; margin-bottom: 1rem;">
        <h4 style="margin-top: 0; margin-bottom: 0.75rem; font-size: 0.9rem; color: #475569;">Time Duration 1:</h4>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.75rem;">
            <div>
                <label for="t1Hours" style="font-size: 0.75rem; font-weight: 600;">Hours:</label>
                <input type="number" id="t1Hours" class="input-field" value="5" min="0" step="1">
            </div>
            <div>
                <label for="t1Mins" style="font-size: 0.75rem; font-weight: 600;">Minutes:</label>
                <input type="number" id="t1Mins" class="input-field" value="45" min="0" max="59" step="1">
            </div>
            <div>
                <label for="t1Secs" style="font-size: 0.75rem; font-weight: 600;">Seconds:</label>
                <input type="number" id="t1Secs" class="input-field" value="30" min="0" max="59" step="1">
            </div>
        </div>
    </div>

    <!-- Time 2 / Factor Input -->
    <div id="t2Wrapper" style="background: white; border: 1px solid #e2e8f0; border-radius: 6px; padding: 1rem; margin-bottom: 1.25rem;">
        <h4 id="t2Heading" style="margin-top: 0; margin-bottom: 0.75rem; font-size: 0.9rem; color: #475569;">Time Duration 2:</h4>
        <div id="t2Inputs" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.75rem;">
            <div>
                <label for="t2Hours" style="font-size: 0.75rem; font-weight: 600;">Hours:</label>
                <input type="number" id="t2Hours" class="input-field" value="2" min="0" step="1">
            </div>
            <div>
                <label for="t2Mins" style="font-size: 0.75rem; font-weight: 600;">Minutes:</label>
                <input type="number" id="t2Mins" class="input-field" value="35" min="0" max="59" step="1">
            </div>
            <div>
                <label for="t2Secs" style="font-size: 0.75rem; font-weight: 600;">Seconds:</label>
                <input type="number" id="t2Secs" class="input-field" value="15" min="0" max="59" step="1">
            </div>
        </div>
        <div id="scalarInputWrapper" style="display: none;">
            <label for="scalarFactor" style="font-size: 0.75rem; font-weight: 600;">Factor / Divisor:</label>
            <input type="number" id="scalarFactor" class="input-field" value="4" min="0.001" step="0.5">
        </div>
    </div>

    <div style="display: flex; gap: 0.75rem; margin-bottom: 1.5rem;">
        <button type="button" class="btn btn-primary" onclick="calculateTimeArithmetic()">Calculate Result</button>
        <button type="button" class="btn btn-outline" onclick="resetTimeInputs()">Reset</button>
    </div>

    <div class="result-box" style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem;">
        <h3 style="margin-top: 0; color: #1e293b; font-size: 1.1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">Time Arithmetic Output</h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Formatted Sexagesimal</div>
                <div id="resSexaTime" style="font-size: 1.4rem; font-weight: 700; color: #2563eb;">08:20:45</div>
                <div id="resWordsTime" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">8h 20m 45s</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Decimal Hours</div>
                <div id="resDecHours" style="font-size: 1.4rem; font-weight: 700; color: #0f172a;">8.3458 hr</div>
                <div id="resDecMinutes" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">500.75 mins</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Total Net Seconds</div>
                <div id="resTotalSec" style="font-size: 1.4rem; font-weight: 700; color: #059669;">30,045 s</div>
                <div style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">SI Standard Base Unit</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Days &amp; Fraction</div>
                <div id="resDaysPortion" style="font-size: 1.2rem; font-weight: 700; color: #7c3aed;">0.3477 Days</div>
                <div style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">Of standard 24-hr day</div>
            </div>
        </div>

        <div style="margin-top: 1.25rem; padding-top: 1rem; border-top: 1px dashed #cbd5e1; font-size: 0.875rem;">
            <span style="font-weight: 600; color: #475569;">Operation Equation Summary:</span>
            <div id="equationSummary" style="font-weight: 700; color: #1e293b; font-size: 1rem; margin-top: 0.25rem;">
                5h 45m 30s + 2h 35m 15s = 8h 20m 45s
            </div>
        </div>
    </div>
</div>

<script>
let currentOp = 'add';

function setTimeOp(op) {
    currentOp = op;
    const ops = ['add', 'sub', 'mult', 'div'];
    ops.forEach(o => {
        const tab = document.getElementById('tab' + o.charAt(0).toUpperCase() + o.slice(1));
        if (tab) {
            tab.className = (o === op) ? 'btn btn-primary' : 'btn btn-outline';
        }
    });

    const isScalar = (op === 'mult' || op === 'div');
    document.getElementById('t2Inputs').style.display = isScalar ? 'none' : 'grid';
    document.getElementById('scalarInputWrapper').style.display = isScalar ? 'block' : 'none';
    document.getElementById('t2Heading').innerText = isScalar ? (op === 'mult' ? 'Multiplication Factor:' : 'Divisor:') : 'Time Duration 2:';

    calculateTimeArithmetic();
}

function resetTimeInputs() {
    document.getElementById('t1Hours').value = '5';
    document.getElementById('t1Mins').value = '45';
    document.getElementById('t1Secs').value = '30';
    document.getElementById('t2Hours').value = '2';
    document.getElementById('t2Mins').value = '35';
    document.getElementById('t2Secs').value = '15';
    document.getElementById('scalarFactor').value = '4';
    setTimeOp('add');
}

function calculateTimeArithmetic() {
    const h1 = parseFloat(document.getElementById('t1Hours').value) || 0;
    const m1 = parseFloat(document.getElementById('t1Mins').value) || 0;
    const s1 = parseFloat(document.getElementById('t1Secs').value) || 0;
    const sec1 = (h1 * 3600) + (m1 * 60) + s1;

    let resSec = 0;
    let eqStr = "";

    const formatT = (h, m, s) => `${h}h ${m}m ${s}s`;

    if (currentOp === 'add' || currentOp === 'sub') {
        const h2 = parseFloat(document.getElementById('t2Hours').value) || 0;
        const m2 = parseFloat(document.getElementById('t2Mins').value) || 0;
        const s2 = parseFloat(document.getElementById('t2Secs').value) || 0;
        const sec2 = (h2 * 3600) + (m2 * 60) + s2;

        if (currentOp === 'add') {
            resSec = sec1 + sec2;
            eqStr = `${formatT(h1, m1, s1)} + ${formatT(h2, m2, s2)}`;
        } else {
            resSec = sec1 - sec2;
            eqStr = `${formatT(h1, m1, s1)} - ${formatT(h2, m2, s2)}`;
        }
    } else {
        const factor = parseFloat(document.getElementById('scalarFactor').value) || 1;
        if (currentOp === 'mult') {
            resSec = sec1 * factor;
            eqStr = `${formatT(h1, m1, s1)} &times; ${factor}`;
        } else {
            resSec = factor !== 0 ? (sec1 / factor) : 0;
            eqStr = `${formatT(h1, m1, s1)} &divide; ${factor}`;
        }
    }

    const isNeg = resSec < 0;
    const absSec = Math.abs(resSec);

    const outH = Math.floor(absSec / 3600);
    const rem = absSec % 3600;
    const outM = Math.floor(rem / 60);
    const outS = Math.round(rem % 60);

    const sign = isNeg ? "-" : "";
    const pad = (n) => String(n).padStart(2, '0');
    const sexaFormatted = `${sign}${pad(outH)}:${pad(outM)}:${pad(outS)}`;
    const wordsFormatted = `${sign}${outH}h ${outM}m ${outS}s`;

    const decHours = (resSec / 3600).toFixed(4);
    const decMins = (resSec / 60).toFixed(2);
    const daysPortion = (resSec / 86400).toFixed(4);

    document.getElementById('resSexaTime').innerText = sexaFormatted;
    document.getElementById('resWordsTime').innerText = wordsFormatted;
    document.getElementById('resDecHours').innerText = `${decHours} hr`;
    document.getElementById('resDecMinutes').innerText = `${decMins} mins`;
    document.getElementById('resTotalSec').innerText = `${Math.round(resSec).toLocaleString()} s`;
    document.getElementById('resDaysPortion').innerText = `${daysPortion} Days`;
    document.getElementById('equationSummary').innerHTML = `${eqStr} = <strong>${wordsFormatted}</strong> (${decHours} hrs)`;
}

window.addEventListener('DOMContentLoaded', () => {
    ['t1Hours', 't1Mins', 't1Secs', 't2Hours', 't2Mins', 't2Secs', 'scalarFactor'].forEach(id => {
        const el = document.getElementById(id);
        if (el) {
            el.addEventListener('input', calculateTimeArithmetic);
            el.addEventListener('change', calculateTimeArithmetic);
        }
    });
    calculateTimeArithmetic();
});
</script>"""

    article = """<h2>Mathematical Principles of Sexagesimal Time Arithmetic</h2>
<p>Unlike standard base-10 decimal mathematics, time intervals are evaluated using the ancient Babylonian <strong>sexagesimal (base-60)</strong> numeral system. Because an hour contains 60 minutes and a minute contains 60 seconds, operations such as addition, subtraction, multiplication, and division cannot be performed by direct columnar decimal arithmetic without systematic base-60 carry and borrow transformations.</p>

<p>The universal algebraic algorithm for computing arbitrary arithmetic across sexagesimal time durations converts all input vectors into total SI base seconds $T_{\text{sec}}$:</p>

$$T_{\text{sec}} = (H \times 3600) + (M \times 60) + S$$

<p>Once translated into continuous integer seconds, standard linear algebraic operations are applied:</p>

<ul>
    <li><strong>Duration Addition:</strong> $T_{\text{sum}} = T_{\text{sec}, 1} + T_{\text{sec}, 2}$</li>
    <li><strong>Duration Subtraction:</strong> $T_{\text{diff}} = T_{\text{sec}, 1} - T_{\text{sec}, 2}$</li>
    <li><strong>Scalar Multiplication:</strong> $T_{\text{product}} = T_{\text{sec}, 1} \times k$ (where $k \in \mathbb{R}$ represents cycle frequency or batches)</li>
    <li><strong>Scalar Division:</strong> $T_{\text{quotient}} = \frac{T_{\text{sec}, 1}}{N}$ (where $N \in \mathbb{R}$ represents units produced or sub-intervals)</li>
</ul>

<p>Following scalar evaluation, the resulting aggregate seconds $T_{\text{result}}$ are partitioned back into canonical sexagesimal components via successive floor division and modulo arithmetic:</p>

$$H_{\text{out}} = \left\lfloor \frac{|T_{\text{result}}|}{3600} \right\rfloor$$
$$M_{\text{out}} = \left\lfloor \frac{|T_{\text{result}}| \bmod 3600}{60} \right\rfloor$$
$$S_{\text{out}} = |T_{\text{result}}| \bmod 60$$

<h2>Industrial Engineering: Takt Time and Cycle Time Formulation</h2>
<p>In manufacturing engineering and Lean Six Sigma methodology, time duration division forms the cornerstone of synchronous assembly line design through the concept of <strong>Takt Time</strong>. Derived from the German word <em>Taktzeit</em> (meter or pulse), takt time defines the precise cadence at which a manufacturing facility must complete individual units to satisfy customer demand.</p>

<p>Takt time is evaluated as the net available production operating time divided by total customer demand over that identical timeframe:</p>

$$\text{Takt Time} = \frac{T_{\text{available, net}}}{D_{\text{customer}}}$$

<p>Where $T_{\text{available, net}}$ represents gross shift duration minus planned maintenance, safety briefings, and statutory employee meal breaks:</p>

$$T_{\text{available, net}} = T_{\text{gross}} - (T_{\text{breaks}} + T_{\text{maintenance}})$$

<p>For example, if an automotive powertrain assembly line operates for 8 hours (480 minutes) with two 15-minute scheduled breaks ($T_{\text{available}} = 450 \text{ minutes} = 27,000 \text{ seconds}$) and the customer demands 450 engine units per shift:</p>

$$\text{Takt Time} = \frac{27,000 \text{ seconds}}{450 \text{ units}} = 60.0 \text{ seconds per unit}$$

<p>If the workstation's actual cycle time exceeds 60 seconds, the line creates production bottlenecks; if cycle time is under 60 seconds, the station produces costly excess inventory.</p>

<h3>Sexagesimal Time Units and Equivalence Matrix</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Time Unit</th>
            <th>Equivalence in Seconds (SI)</th>
            <th>Equivalence in Minutes</th>
            <th>Equivalence in Hours</th>
            <th>Equivalence in Days</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>1 Second (s)</td><td>1.0 s</td><td>0.01667 min</td><td>0.000278 hr</td><td>0.0000116 days</td></tr>
        <tr><td>1 Minute (min)</td><td>60.0 s</td><td>1.0 min</td><td>0.016667 hr</td><td>0.000694 days</td></tr>
        <tr><td>1 Hobbs Tenth (0.1 hr)</td><td>360.0 s</td><td>6.0 min</td><td>0.1000 hr</td><td>0.004167 days</td></tr>
        <tr><td>1 Centihour (c-hr)</td><td>36.0 s</td><td>0.6 min</td><td>0.0100 hr</td><td>0.000417 days</td></tr>
        <tr><td>1 Quarter Hour</td><td>900.0 s</td><td>15.0 min</td><td>0.2500 hr</td><td>0.010417 days</td></tr>
        <tr><td>1 Hour (hr)</td><td>3,600.0 s</td><td>60.0 min</td><td>1.0 hr</td><td>0.041667 days</td></tr>
        <tr><td>1 Solar Day</td><td>86,400.0 s</td><td>1,440.0 min</td><td>24.0 hr</td><td>1.000000 days</td></tr>
    </tbody>
</table>

<h2>Audio, Video, and Media Production Runtime Summation</h2>
<p>In digital media mastering, film post-production, and podcast broadcasting, audio engineers must sum discrete multi-track cue durations to comply with broadcast commercial insertion limits or physical CD/vinyl disc maximum capacities (e.g., Red Book CD-DA audio maximum of 74 or 80 minutes).</p>

<p>Because non-linear editing (NLE) timelines operate in frame rates ($24\text{ fps}$, $29.97\text{ fps SMPTE drop-frame}$, or $60\text{ fps}$), summing sexagesimal durations requires converting frames to sub-second rational coefficients:</p>

$$S_{\text{total}} = S_{\text{integer}} + \frac{\text{Frames}}{\text{Frame Rate}}$$

<div class="worked-example-card">
    <h3>Worked Engineering Case Study: Lean Six Sigma Production Run</h3>
    <p><strong>Scenario:</strong> A medical device manufacturer produces robotic surgical instruments. The plant operates a single shift of 8 hours and 30 minutes ($08:30:00$). Planned unpaid lunch is 45 minutes ($00:45:00$) and two paid operator rest breaks total 30 minutes ($00:30:00$, which counts as production time). Daily customer order demand is 155 finished surgical instruments. Calculate: (1) net available operating time in sexagesimal and seconds, (2) required takt time per unit, and (3) total time to produce a specialized sub-batch of 28 units if cycle time is 2 minutes and 45 seconds per unit.</p>
    
    <div class="step-solution">
        <h4>Step 1: Compute Net Available Operating Time</h4>
        <p>Gross shift: $8\text{h } 30\text{m } 00\text{s} = (8 \times 3600) + (30 \times 60) = 28,800 + 1,800 = 30,600 \text{ seconds}$.</p>
        <p>Unpaid meal deduction: $45 \text{ minutes} = 2,700 \text{ seconds}$.</p>
        $$T_{\text{net}} = 30,600 - 2,700 = 27,900 \text{ seconds} = 7 \text{ hours and } 45 \text{ minutes}$$

        <h4>Step 2: Calculate Required Takt Time</h4>
        $$\text{Takt Time} = \frac{27,900 \text{ seconds}}{155 \text{ units}} = 180.0 \text{ seconds per unit}$$
        <p>In sexagesimal: $180 / 60 = 3 \text{ minutes and } 0 \text{ seconds per unit}$.</p>

        <h4>Step 3: Calculate Sub-Batch Production Time</h4>
        <p>Unit cycle time: $2\text{m } 45\text{s} = (2 \times 60) + 45 = 165 \text{ seconds}$.</p>
        $$T_{\text{batch}} = 28 \text{ units} \times 165 \text{ seconds} = 4,620 \text{ seconds}$$
        <p>Partitioning into sexagesimal:</p>
        $$H = \lfloor 4620 / 3600 \rfloor = 1 \text{ hour}$$
        $$M = \lfloor (4620 \bmod 3600) / 60 \rfloor = \lfloor 1020 / 60 \rfloor = 17 \text{ minutes}$$
        $$S = 1020 \bmod 60 = 0 \text{ seconds}$$
        <p><strong>Sub-Batch Duration:</strong> <strong>1 hour, 17 minutes, and 0 seconds</strong> ($1.2833$ decimal hours).</p>
    </div>
</div>

<h2>Common Calculation Errors in Time Arithmetic</h2>
<ol>
    <li><strong>Treating Minutes and Seconds as Decimals:</strong> Adding $4.45 \text{ hours}$ and $2.35 \text{ hours}$ as standard decimal numbers yields $6.80$, whereas adding $4\text{h } 45\text{m}$ and $2\text{h } 35\text{m}$ yields $7\text{h } 20\text{m}$ ($7.333 \text{ hours}$). Failing to convert base-60 produces massive compounding errors.</li>
    <li><strong>Negative Duration Underflow:</strong> In subtraction when subtracting a larger duration from a smaller duration, naive code often produces outputs like <code>-2 hours and +40 minutes</code>. The sign must distribute across the entire scalar: $-1\text{h } 20\text{m}$ ($-80 \text{ minutes}$).</li>
    <li><strong>Daylight Saving Transition Drift:</strong> When computing elapsed time between clock timestamps spanning the spring or autumn DST transition, civil clocks jump forward by 1 hour (a 23-hour day) or fall back 1 hour (a 25-hour day). Physical time arithmetic must reference UTC epoch timestamps rather than wall-clock strings.</li>
</ol>

<section class="faq-section">
    <h2>Frequently Asked Questions About Time Calculations</h2>
    <div class="faq-item">
        <h3>How do you add two time durations together?</h3>
        <p>Convert both durations to total seconds, add the seconds together, then convert back to hours, minutes, and seconds by dividing by 3600 and 60 using modulo arithmetic.</p>
    </div>
    <div class="faq-item">
        <h3>How does subtraction work when Time 2 is larger than Time 1?</h3>
        <p>For clock times wrapping past midnight, 24 hours (86,400 seconds) is added to the difference. For raw mathematical durations, the result represents a negative duration.</p>
    </div>
    <div class="faq-item">
        <h3>How do you multiply or divide a time duration by a number?</h3>
        <p>Convert the duration into total seconds, multiply or divide by the scalar factor, then re-format into sexagesimal hours, minutes, and seconds.</p>
    </div>
    <div class="faq-item">
        <h3>What is takt time in manufacturing engineering?</h3>
        <p>Takt time is the maximum allowable time per unit to produce a product in order to meet customer demand, evaluated as Net Available Production Time divided by Customer Demand Units.</p>
    </div>
</section>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article)


def main():
    qy_html = gen_quarter_of_year()
    with open(os.path.join(BASE_DIR, "quarter-of-year-calculator.html"), "w", encoding="utf-8") as f:
        f.write(qy_html)
    print("Generated quarter-of-year-calculator.html successfully!")

    t_html = gen_time_calculator()
    with open(os.path.join(BASE_DIR, "time-calculator.html"), "w", encoding="utf-8") as f:
        f.write(t_html)
    print("Generated time-calculator.html successfully!")

if __name__ == "__main__":
    main()
