# -*- coding: utf-8 -*-
"""
Generator for Batch 39 - Part 2
Tools:
3. week-number-calculator.html (ISO 8601 Week Number, Calendar Weeks, Ordinal Dates)
4. add-days-to-date-calculator.html (Add/Subtract Days, Gregorian Leap Rules, Business Days)
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COMMON_TAIL = """    <footer class="site-footer">
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>About CalcHub</h4>
                    <p>CalcHub provides peer-reviewed chronometric algorithms, ISO 8601 calendrical engines, and high-precision datetime mathematics for global enterprise logistics, legal compliance, and software engineering.</p>
                </div>
                <div class="footer-col">
                    <h4>Chronometric &amp; Time Suites</h4>
                    <ul>
                        <li><a href="datetime.html">Date &amp; Time Utilities</a></li>
                        <li><a href="math.html">Mathematics &amp; Statistics</a></li>
                        <li><a href="finance.html">Financial Planning</a></li>
                        <li><a href="converter.html">Unit &amp; Time Converters</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Popular Calendrical Tools</h4>
                    <ul>
                        <li><a href="week-number-calculator.html">ISO Week Number</a></li>
                        <li><a href="add-days-to-date-calculator.html">Add Days to Date</a></li>
                        <li><a href="hours-calculator.html">Work Hours Calculator</a></li>
                        <li><a href="date-difference-calculator.html">Date Difference</a></li>
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
                <p>&copy; 2026 CalcHub. All rights reserved. Compliant with ISO 8601, Gregorian, and Julian calendrical standards.</p>
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
                        <li><a href="week-number-calculator.html">ISO Week Number</a></li>
                        <li><a href="add-days-to-date-calculator.html">Add Days to Date</a></li>
                        <li><a href="hours-calculator.html">Work Hours Calculator</a></li>
                        <li><a href="date-difference-calculator.html">Date Difference</a></li>
                        <li><a href="time-converter.html">Time Converter</a></li>
                        <li><a href="salary-calculator.html">Salary Calculator</a></li>
                        <li><a href="ratio-simplifier-calculator.html">Ratio Simplifier</a></li>
                    </ul>
                </div>
            </aside>
        </div>
    </div>
{COMMON_TAIL}"""


# ===========================================================================
# TOOL 3: week-number-calculator.html
# ===========================================================================
def gen_week_number():
    slug = "week-number-calculator"
    title = "Week Number Calculator | ISO 8601 Calendar Week, Dates & Year"
    desc = "Determine the exact ISO 8601 week number, week start and end dates, ordinal day of year, and total weeks (52 or 53) for any Gregorian calendar date."
    h1 = "Week Number Calculator"
    short_desc = "Calculate the international standard ISO 8601 calendar week number, week starting and ending dates, day of year, and fiscal year boundaries."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Week Number Calculator",
      "url": "https://calchub.com/week-number-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Calculates ISO 8601 and traditional calendar week numbers, start and end dates of the week, and annual week counts."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the ISO 8601 week numbering standard?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Under international standard ISO 8601, weeks begin on Monday (Day 1) and end on Sunday (Day 7). Week 1 of any calendar year is defined as the week containing the first Thursday of that year, which is mathematically identical to the week containing January 4th."
          }
        },
        {
          "@type": "Question",
          "name": "Can a date in late December belong to Week 1 of the following year?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. If December 29, 30, or 31 falls on a Monday, Tuesday, or Wednesday, and the following Thursday is in January, those days belong to Week 1 of the subsequent ISO week-numbering year."
          }
        },
        {
          "@type": "Question",
          "name": "What causes a year to have 53 weeks instead of 52?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Any standard 365-day year that begins on a Thursday (or leap year that begins on a Wednesday or Thursday) contains 53 ISO weeks. This occurs because 365 days equals 52 weeks plus 1 extra day (or 2 extra days in a leap year)."
          }
        },
        {
          "@type": "Question",
          "name": "How does the US calendar week system differ from ISO 8601?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In the traditional US system, weeks begin on Sunday and end on Saturday. Furthermore, Week 1 is typically defined as the week containing January 1st, regardless of whether that week contains only one or two days of the new calendar year."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-grid">
    <div class="calc-inputs">
        <div class="input-group">
            <label for="targetDate">Select Calendar Date</label>
            <input type="date" id="targetDate" class="input-field">
            <span class="input-hint">Choose any historical, current, or future date</span>
        </div>
        <div class="input-group">
            <label for="weekStandard">Week Numbering Standard</label>
            <select id="weekStandard" class="input-field">
                <option value="iso" selected>ISO 8601 (Monday-Start, First Thu)</option>
                <option value="us">US Traditional (Sunday-Start, Jan 1)</option>
            </select>
            <span class="input-hint">Select international ISO or North American standard</span>
        </div>
        <div style="display:flex;gap:0.5rem;flex-wrap:wrap;margin-top:0.5rem;">
            <button type="button" class="btn-outline" onclick="setDatePreset(0)">Today</button>
            <button type="button" class="btn-outline" onclick="setDatePreset('jan1')">Jan 1</button>
            <button type="button" class="btn-outline" onclick="setDatePreset('mid')">Mid-Year</button>
            <button type="button" class="btn-outline" onclick="setDatePreset('dec31')">Dec 31</button>
        </div>
    </div>
    <div class="calc-results">
        <div class="result-card primary-result">
            <div class="result-label">ISO Week Number</div>
            <div class="result-value" id="resWeekNum">Week 41</div>
            <div class="result-sub" id="resWeekYear">ISO Week-Numbering Year: 2026</div>
        </div>
        <div class="result-grid-mini" style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;margin-top:1rem;">
            <div class="result-card">
                <div class="result-label">Week Starts (Monday)</div>
                <div class="result-value-sm" id="resWeekStart">Oct 05, 2026</div>
            </div>
            <div class="result-card">
                <div class="result-label">Week Ends (Sunday)</div>
                <div class="result-value-sm" id="resWeekEnd">Oct 11, 2026</div>
            </div>
            <div class="result-card">
                <div class="result-label">Day of the Year</div>
                <div class="result-value-sm" id="resDayOfYear">Day 278 of 365</div>
            </div>
            <div class="result-card">
                <div class="result-label">Total Weeks in Year</div>
                <div class="result-value-sm" id="resTotalWeeks">53 Weeks (Long Year)</div>
            </div>
        </div>
        <div class="result-card" style="margin-top:1rem;background:var(--bg-accent, #eff6ff);border-left:4px solid var(--brand-primary, #2563eb);">
            <div class="result-label">Calendar &amp; Fiscal Breakdown</div>
            <div class="result-value" id="resQuarter" style="color:var(--brand-primary, #2563eb);font-size:1.4rem;">Quarter 4 (Q4) &bull; 75.8% Year Complete</div>
            <div class="result-sub" id="resDaysLeft">87 days remaining until New Year</div>
        </div>
    </div>
</div>
<script>
function getISOWeekDetails(date) {
    const d = new Date(Date.UTC(date.getFullYear(), date.getMonth(), date.getDate()));
    // Set to nearest Thursday: current date + 4 - current day number (make Sunday 7)
    const dayNum = d.getUTCDay() || 7;
    d.setUTCDate(d.getUTCDate() + 4 - dayNum);
    const yearStart = new Date(Date.UTC(d.getUTCFullYear(), 0, 1));
    const weekNo = Math.ceil((((d - yearStart) / 86400000) + 1) / 7);
    const isoYear = d.getUTCFullYear();
    return { weekNo, isoYear };
}

function weeksInISOYear(year) {
    const d = new Date(Date.UTC(year, 11, 28));
    return getISOWeekDetails(d).weekNo;
}

function calculateWeek() {
    const dateInput = document.getElementById('targetDate').value;
    if (!dateInput) return;

    const parts = dateInput.split('-').map(Number);
    const date = new Date(parts[0], parts[1] - 1, parts[2]);

    const standard = document.getElementById('weekStandard').value;

    let weekNum, weekYear;

    if (standard === 'iso') {
        const iso = getISOWeekDetails(date);
        weekNum = iso.weekNo;
        weekYear = iso.isoYear;
    } else {
        // US Traditional: Jan 1 is in week 1, Sunday starts week
        const startOfYear = new Date(date.getFullYear(), 0, 1);
        const dayOfYear = Math.floor((date - startOfYear) / (24 * 60 * 60 * 1000));
        weekNum = Math.ceil((dayOfYear + startOfYear.getDay() + 1) / 7);
        weekYear = date.getFullYear();
    }

    // Week boundaries (Monday to Sunday for ISO)
    const dayOfWeek = date.getDay(); // 0 is Sun, 1 is Mon
    const diffToMon = (dayOfWeek === 0 ? -6 : 1) - dayOfWeek;
    const monday = new Date(date);
    monday.setDate(date.getDate() + diffToMon);

    const sunday = new Date(monday);
    sunday.setDate(monday.getDate() + 6);

    // Day of Year
    const startOfCalYear = new Date(date.getFullYear(), 0, 1);
    const isLeap = (date.getFullYear() % 4 === 0 && (date.getFullYear() % 100 !== 0 || date.getFullYear() % 400 === 0));
    const daysInYear = isLeap ? 366 : 365;
    const dayOfYear = Math.floor((date - startOfCalYear) / (24 * 60 * 60 * 1000)) + 1;
    const daysLeft = daysInYear - dayOfYear;
    const yearPct = ((dayOfYear / daysInYear) * 100).toFixed(1);

    const totalWeeksInYear = weeksInISOYear(weekYear);
    const quarter = Math.floor(date.getMonth() / 3) + 1;

    const options = { month: 'short', day: '2-digit', year: 'numeric' };
    document.getElementById('resWeekNum').innerText = `Week ${weekNum}`;
    document.getElementById('resWeekYear').innerText = `${standard === 'iso' ? 'ISO' : 'US'} Week-Numbering Year: ${weekYear}`;
    document.getElementById('resWeekStart').innerText = monday.toLocaleDateString('en-US', options);
    document.getElementById('resWeekEnd').innerText = sunday.toLocaleDateString('en-US', options);
    document.getElementById('resDayOfYear').innerText = `Day ${dayOfYear} of ${daysInYear}`;
    document.getElementById('resTotalWeeks').innerText = `${totalWeeksInYear} Weeks (${totalWeeksInYear === 53 ? 'Leap Week Year' : 'Standard 52 Wks'})`;
    document.getElementById('resQuarter').innerText = `Quarter ${quarter} (Q${quarter}) • ${yearPct}% of Year Elapsed`;
    document.getElementById('resDaysLeft').innerText = `${daysLeft} days remaining until ${date.getFullYear() + 1}`;
}

function setDatePreset(type) {
    const today = new Date();
    let target = new Date();
    if (type === 'jan1') {
        target = new Date(today.getFullYear(), 0, 1);
    } else if (type === 'mid') {
        target = new Date(today.getFullYear(), 6, 1);
    } else if (type === 'dec31') {
        target = new Date(today.getFullYear(), 11, 31);
    }
    const y = target.getFullYear();
    const m = String(target.getMonth() + 1).padStart(2, '0');
    const d = String(target.getDate()).padStart(2, '0');
    document.getElementById('targetDate').value = `${y}-${m}-${d}`;
    calculateWeek();
}

window.addEventListener('DOMContentLoaded', () => {
    const today = new Date();
    const y = today.getFullYear();
    const m = String(today.getMonth() + 1).padStart(2, '0');
    const d = String(today.getDate()).padStart(2, '0');
    document.getElementById('targetDate').value = `${y}-${m}-${d}`;
    ['targetDate', 'weekStandard'].forEach(id => {
        document.getElementById(id).addEventListener('change', calculateWeek);
    });
    calculateWeek();
});
</script>"""

    article = """<h2>Mathematical and Algorithmic Definition of ISO 8601 Weeks</h2>
<p>In global supply chain management, enterprise resource planning (ERP), financial fiscal reporting, and international governance, referencing calendar periods by discrete week numbers provides an invariant, uniform interval of exactly seven days (168 hours). The standard international authority governing this formulation is <strong>ISO 8601</strong> (<em>Data elements and interchange formats – Information interchange – Representation of dates and times</em>).</p>

<p>Under ISO 8601, the calendrical week is strictly defined by three fundamental axioms:</p>
<ol>
    <li><strong>Week Orientation:</strong> The first day of the week is invariant: Monday is Day 1 ($d = 1$), progressing sequentially to Sunday as Day 7 ($d = 7$).</li>
    <li><strong>Week 01 Anchor Rule:</strong> Week 01 of any calendar year is formally defined as the week that contains the first Thursday of that Gregorian year.</li>
    <li><strong>Equivalent Anchor Equivalencies:</strong> Axiom 2 is mathematically identical to establishing that Week 01 is:
        <ul>
            <li>The week containing January 4th.</li>
            <li>The first week of the year containing at least four days belonging to the new calendar year.</li>
            <li>The week starting with the Monday closest to January 1st (within the closed interval December 29 to January 4).</li>
        </ul>
    </li>
</ol>

<h2>The ISO Week Number Calculation Algorithm</h2>
<p>To evaluate the ISO week number $W$ and the corresponding ISO week-numbering year $Y_{\text{iso}}$ for an arbitrary Gregorian date $(Y, M, D)$, the algorithm maps the target date to its ordinal Day of the Year ($\text{DoY}$) and its Day of the Week ($\text{DoW} \in \{1=\text{Mon}, \dots, 7=\text{Sun}\}$).</p>

<p>The mathematical closed-form relation to determine the nearest Thursday's position is expressed as:</p>

$$P_{\text{Thu}} = \text{DoY} + 4 - \text{DoW}$$

<p>If $P_{\text{Thu}} < 1$, the date falls chronologically before the first Thursday of the Gregorian year, meaning the date belongs to the final week (Week 52 or Week 53) of the preceding calendar year $Y - 1$. Conversely, if $P_{\text{Thu}} > \text{DaysInYear}(Y)$, the date falls into Week 01 of the subsequent calendar year $Y + 1$.</p>

<p>When $P_{\text{Thu}}$ lies validly within year $Y$, the ISO week number is derived via integer floor division:</p>

$$W = \left\lfloor \frac{P_{\text{Thu}} - 1}{7} \right\rfloor + 1 = \left\lfloor \frac{\text{DoY} - \text{DoW} + 10}{7} \right\rfloor$$

<h2>The 53-Week Leap Week Phenomenon</h2>
<p>Because an astronomical Gregorian solar year contains either 365 days (52 weeks plus 1 day) or 366 days in a leap year (52 weeks plus 2 days), the calendar day-of-week anchors shift forward by 1 or 2 days every year. Over an average 400-year Gregorian cycle ($146,097 \text{ days} = 20,871 \text{ exact weeks}$), this fractional accumulation requires periodic <strong>leap-week years</strong> containing exactly 53 weeks.</p>

<p>A Gregorian year $Y$ contains exactly 53 ISO weeks if and only if:</p>

<ul>
    <li>January 1st of year $Y$ falls on a Thursday ($\text{DoW}(\text{Jan 1}) = 4$), OR</li>
    <li>The year $Y$ is a leap year ($\text{Leap}(Y) = \text{true}$) and January 1st falls on a Wednesday ($\text{DoW}(\text{Jan 1}) = 3$).</li>
</ul>

<h3>Multi-Year ISO 8601 Calendar Week Reference Matrix</h3>
<p>The following technical table provides the exact week configuration, starting boundary dates, and annual week count across consecutive calendar years from 2020 through 2032:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Calendar Year</th>
            <th>Jan 1 Weekday</th>
            <th>Leap Year?</th>
            <th>Total ISO Weeks</th>
            <th>Week 01 Starts (Monday)</th>
            <th>Week 52/53 Ends (Sunday)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>2020</td><td>Wednesday</td><td>Yes (366 d)</td><td>53 Weeks</td><td>Dec 30, 2019</td><td>Jan 03, 2021</td></tr>
        <tr><td>2021</td><td>Friday</td><td>No (365 d)</td><td>52 Weeks</td><td>Jan 04, 2021</td><td>Jan 02, 2022</td></tr>
        <tr><td>2022</td><td>Saturday</td><td>No (365 d)</td><td>52 Weeks</td><td>Jan 03, 2022</td><td>Jan 01, 2023</td></tr>
        <tr><td>2023</td><td>Sunday</td><td>No (365 d)</td><td>52 Weeks</td><td>Jan 02, 2023</td><td>Dec 31, 2023</td></tr>
        <tr><td>2024</td><td>Monday</td><td>Yes (366 d)</td><td>52 Weeks</td><td>Jan 01, 2024</td><td>Dec 29, 2024</td></tr>
        <tr><td>2025</td><td>Wednesday</td><td>No (365 d)</td><td>52 Weeks</td><td>Dec 30, 2024</td><td>Dec 28, 2025</td></tr>
        <tr><td>2026</td><td>Thursday</td><td>No (365 d)</td><td>53 Weeks</td><td>Dec 29, 2025</td><td>Jan 03, 2027</td></tr>
        <tr><td>2027</td><td>Friday</td><td>No (365 d)</td><td>52 Weeks</td><td>Jan 04, 2027</td><td>Jan 02, 2028</td></tr>
        <tr><td>2028</td><td>Saturday</td><td>Yes (366 d)</td><td>52 Weeks</td><td>Jan 03, 2028</td><td>Dec 31, 2028</td></tr>
        <tr><td>2029</td><td>Monday</td><td>No (365 d)</td><td>52 Weeks</td><td>Jan 01, 2029</td><td>Dec 30, 2029</td></tr>
        <tr><td>2030</td><td>Tuesday</td><td>No (365 d)</td><td>52 Weeks</td><td>Dec 31, 2029</td><td>Dec 29, 2030</td></tr>
        <tr><td>2031</td><td>Wednesday</td><td>No (365 d)</td><td>52 Weeks</td><td>Dec 30, 2030</td><td>Dec 28, 2031</td></tr>
        <tr><td>2032</td><td>Thursday</td><td>Yes (366 d)</td><td>53 Weeks</td><td>Dec 29, 2031</td><td>Jan 02, 2033</td></tr>
    </tbody>
</table>

<div class="worked-example-card">
    <h3>Worked Engineering Case Study: Automotive Supply Chain Delivery Sprint</h3>
    <p><strong>Scenario:</strong> A tier-1 automotive manufacturing subcontractor in Stuttgart, Germany receives a just-in-time logistics contract specifying delivery during <em>ISO Week 01 of 2027</em>. The procurement officer in Chicago assumes this refers to January 1, 2027. Determine: (1) the exact Gregorian start and end dates for ISO Week 01 of 2027, and (2) whether January 1, 2027 belongs to Week 01 of 2027 or Week 53 of 2026.</p>
    
    <div class="step-solution">
        <h4>Step 1: Analyze January 1, 2027</h4>
        <p>Year 2027 is a standard 365-day year. January 1, 2027 falls on a <strong>Friday</strong> ($\text{DoW} = 5$).</p>
        <p>Day of Year: $\text{DoY} = 1$.</p>

        <h4>Step 2: Evaluate the Nearest Thursday Position</h4>
        $$P_{\text{Thu}} = \text{DoY} + 4 - \text{DoW} = 1 + 4 - 5 = 0$$
        <p>Since $P_{\text{Thu}} = 0 < 1$, January 1, 2027 falls before the first Thursday of 2027. Therefore, January 1, 2027 belongs to the <strong>final week of ISO Year 2026</strong>!</p>

        <h4>Step 3: Determine the Total Weeks in 2026</h4>
        <p>From the reference matrix, January 1, 2026 was a Thursday, confirming that 2026 is an ISO 53-week leap-week year. Therefore, January 1, 2027 is part of <strong>Week 53 of 2026</strong>.</p>

        <h4>Step 4: Establish True Boundaries for Week 01 of 2027</h4>
        <p>The first Thursday of 2027 occurs on January 7, 2027.</p>
        <p>The Monday of that week is: $\text{Jan 7} - 3 = \text{January 4, 2027}$.</p>
        <p>The Sunday closing that week is: $\text{Jan 4} + 6 = \text{January 10, 2027}$.</p>
        <p><strong>Conclusion:</strong> ISO Week 01 of 2027 spans from <strong>Monday, January 4, 2027</strong> to <strong>Sunday, January 10, 2027</strong>. Delivering components on January 1st would represent delivery in Week 53 of 2026, causing a premature delivery inventory violation.</p>
    </div>
</div>

<h2>Common Enterprise Integration Pitfalls</h2>
<ol>
    <li><strong>Assuming Week 1 Always Starts in January:</strong> As illustrated in 2020 and 2026, ISO Week 01 regularly begins in late December (e.g., Dec 29 or Dec 30). Database aggregation queries grouping strictly by <code>YEAR(date)</code> and <code>WEEK(date)</code> produce catastrophic split-record errors unless using ISO-aware functions (e.g., SQL <code>%V</code> and <code>%G</code> in POSIX <code>strftime</code>).</li>
    <li><strong>Incompatible Regional Standards:</strong> North American accounting frameworks (US / Canada) commonly treat Sunday as day 1 and count any partial week containing Jan 1 as Week 1. Comparing US week numbers directly against European ISO week numbers without normalization causes multi-day reporting misalignments.</li>
    <li><strong>Fiscal 4-4-5 Retail Calendars:</strong> Corporate retail entities frequently adopt National Retail Federation (NRF) 4-4-5 or 4-5-4 week structures rather than pure ISO 8601, requiring dedicated quarterly mapping matrices.</li>
</ol>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article)


# ===========================================================================
# TOOL 4: add-days-to-date-calculator.html
# ===========================================================================
def gen_add_days_to_date():
    slug = "add-days-to-date-calculator"
    title = "Add Days to Date Calculator | Add or Subtract Calendar & Business Days"
    desc = "Add or subtract days from any date with instant Gregorian calendar calculation, leap year handling, business day exclusions (skip weekends), and full date breakdown."
    h1 = "Add Days to Date Calculator"
    short_desc = "Compute precise target calendar and business dates by adding or subtracting arbitrary day offsets across leap years and centuries."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Add Days to Date Calculator",
      "url": "https://calchub.com/add-days-to-date-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Calculates future or past calendar and business dates by adding or subtracting discrete day counts."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How does the calculator account for leap years when adding days?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The calculation engine utilizes exact Gregorian calendar rules established in 1582: a year is a leap year if divisible by 4, except for century years not divisible by 400. February 29th is automatically inserted whenever a forward or backward projection crosses an active leap day."
          }
        },
        {
          "@type": "Question",
          "name": "What is the difference between calendar days and business days?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Calendar days include every consecutive 24-hour diurnal period (all 7 days per week). Business days exclude Saturdays and Sundays, meaning adding 5 business days advances the calendar date by a full 7 calendar days."
          }
        },
        {
          "@type": "Question",
          "name": "Can you subtract days from a date as well as add them?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. By selecting the subtraction mode or entering a negative integer day value, the algorithm reverses the chronological progression to determine the exact historical calendar date."
          }
        },
        {
          "@type": "Question",
          "name": "What algorithm is used to perform arithmetic on calendar dates?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Modern calendrical algorithms map calendar dates to continuous scalar integers known as Julian Day Numbers (JDN). Adding or subtracting days is accomplished by simple integer addition or subtraction on the JDN, which is then mapped back to the Gregorian year, month, and day."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-grid">
    <div class="calc-inputs">
        <div class="input-group">
            <label for="startDate">Starting Date</label>
            <input type="date" id="startDate" class="input-field">
            <span class="input-hint">Select the initial baseline calendar date</span>
        </div>
        <div class="input-group">
            <label for="operationType">Operation</label>
            <select id="operationType" class="input-field">
                <option value="add" selected>Add Days (+ Forward in Time)</option>
                <option value="sub">Subtract Days (- Backward in Time)</option>
            </select>
            <span class="input-hint">Direction of chronological projection</span>
        </div>
        <div class="input-group">
            <label for="numDays">Number of Days to Offset</label>
            <input type="number" id="numDays" value="30" min="0" max="100000" step="1" class="input-field">
            <span class="input-hint">Integer count of days (e.g., 30, 60, 90, 180)</span>
        </div>
        <div class="input-group">
            <label for="dayType">Day Counting Mode</label>
            <select id="dayType" class="input-field">
                <option value="calendar" selected>All Calendar Days (Mon - Sun)</option>
                <option value="business">Business Working Days Only (Mon - Fri, Skip Weekends)</option>
            </select>
            <span class="input-hint">Exclude Saturdays &amp; Sundays for contract deadlines</span>
        </div>
        <div style="display:flex;gap:0.5rem;flex-wrap:wrap;margin-top:0.5rem;">
            <button type="button" class="btn-outline" onclick="setOffsetPreset(14)">+14 d</button>
            <button type="button" class="btn-outline" onclick="setOffsetPreset(30)">+30 d</button>
            <button type="button" class="btn-outline" onclick="setOffsetPreset(60)">+60 d</button>
            <button type="button" class="btn-outline" onclick="setOffsetPreset(90)">+90 d</button>
            <button type="button" class="btn-outline" onclick="setOffsetPreset(180)">+180 d</button>
            <button type="button" class="btn-outline" onclick="setOffsetPreset(365)">+1 Year</button>
        </div>
    </div>
    <div class="calc-results">
        <div class="result-card primary-result">
            <div class="result-label">Computed Target Date</div>
            <div class="result-value" id="resTargetDate" style="font-size:1.85rem;">Wednesday, Nov 04, 2026</div>
            <div class="result-sub" id="resTargetISO">ISO 8601 Format: 2026-11-04</div>
        </div>
        <div class="result-grid-mini" style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;margin-top:1rem;">
            <div class="result-card">
                <div class="result-label">Total Elapsed Span</div>
                <div class="result-value-sm" id="resSpanBreakdown">4 weeks and 2 days</div>
            </div>
            <div class="result-card">
                <div class="result-label">Target Day of Week</div>
                <div class="result-value-sm" id="resDayOfWeek">Wednesday (Day 3)</div>
            </div>
            <div class="result-card">
                <div class="result-label">Day of Year</div>
                <div class="result-value-sm" id="resTargetDoY">Day 308 of 365</div>
            </div>
            <div class="result-card">
                <div class="result-label">Weekends Crossed</div>
                <div class="result-value-sm" id="resWeekends">4 Weekends (8 Days)</div>
            </div>
        </div>
        <div class="result-card" style="margin-top:1rem;background:var(--bg-accent, #eff6ff);border-left:4px solid var(--brand-primary, #2563eb);">
            <div class="result-label">Contract &amp; Commercial Milestone Summary</div>
            <div class="result-value" id="resMilestone" style="color:var(--brand-primary, #2563eb);font-size:1.35rem;">30 Calendar Days = 22 Business Working Days</div>
            <div class="result-sub" id="resQuarterInfo">Falls in Q4 (Quarter 4) 2026</div>
        </div>
    </div>
</div>
<script>
function calculateDateOffset() {
    const startStr = document.getElementById('startDate').value;
    const op = document.getElementById('operationType').value;
    const numDays = parseInt(document.getElementById('numDays').value, 10);
    const dayType = document.getElementById('dayType').value;

    if (!startStr || isNaN(numDays) || numDays < 0) return;

    const parts = startStr.split('-').map(Number);
    const start = new Date(parts[0], parts[1] - 1, parts[2]);

    let target = new Date(start);
    let calendarDaysElapsed = 0;
    let weekendDaysCount = 0;

    if (dayType === 'calendar') {
        const delta = (op === 'add') ? numDays : -numDays;
        target.setDate(start.getDate() + delta);
        calendarDaysElapsed = numDays;

        // Count weekends crossed
        let temp = new Date(start);
        const step = (op === 'add') ? 1 : -1;
        for (let i = 0; i < numDays; i++) {
            temp.setDate(temp.getDate() + step);
            const dow = temp.getDay();
            if (dow === 0 || dow === 6) weekendDaysCount++;
        }
    } else {
        // Business days: advance/recede only on Mon-Fri
        let remaining = numDays;
        const step = (op === 'add') ? 1 : -1;
        while (remaining > 0) {
            target.setDate(target.getDate() + step);
            calendarDaysElapsed++;
            const dow = target.getDay();
            if (dow === 0 || dow === 6) {
                weekendDaysCount++;
            } else {
                remaining--;
            }
        }
    }

    const weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

    const targetDayName = weekdays[target.getDay()];
    const targetMonthName = months[target.getMonth()];
    const targetDateNum = String(target.getDate()).padStart(2, '0');
    const targetYear = target.getFullYear();

    const isoStr = `${targetYear}-${String(target.getMonth() + 1).padStart(2, '0')}-${targetDateNum}`;
    const fullDateDisplay = `${targetDayName}, ${targetMonthName} ${targetDateNum}, ${targetYear}`;

    // Day of Year
    const isLeap = (targetYear % 4 === 0 && (targetYear % 100 !== 0 || targetYear % 400 === 0));
    const totalYearDays = isLeap ? 366 : 365;
    const startOfYear = new Date(targetYear, 0, 1);
    const doy = Math.floor((target - startOfYear) / (24 * 60 * 60 * 1000)) + 1;

    const weeks = Math.floor(calendarDaysElapsed / 7);
    const remDays = calendarDaysElapsed % 7;
    const quarter = Math.floor(target.getMonth() / 3) + 1;

    document.getElementById('resTargetDate').innerText = fullDateDisplay;
    document.getElementById('resTargetISO').innerText = `ISO 8601 Format: ${isoStr}`;
    document.getElementById('resSpanBreakdown').innerText = `${weeks} weeks and ${remDays} days (${calendarDaysElapsed} total calendar days)`;
    document.getElementById('resDayOfWeek').innerText = `${targetDayName} (Day ${target.getDay() === 0 ? 7 : target.getDay()})`;
    document.getElementById('resTargetDoY').innerText = `Day ${doy} of ${totalYearDays}`;
    document.getElementById('resWeekends').innerText = `${Math.round(weekendDaysCount / 2)} Weekends (${weekendDaysCount} Weekend Days)`;

    if (dayType === 'calendar') {
        const busDays = calendarDaysElapsed - weekendDaysCount;
        document.getElementById('resMilestone').innerText = `${calendarDaysElapsed} Calendar Days = ${busDays} Business Working Days`;
    } else {
        document.getElementById('resMilestone').innerText = `${numDays} Business Days = ${calendarDaysElapsed} Calendar Days Total`;
    }
    document.getElementById('resQuarterInfo').innerText = `Falls in Q${quarter} (Quarter ${quarter}) ${targetYear}`;
}

function setOffsetPreset(d) {
    document.getElementById('numDays').value = d;
    calculateDateOffset();
}

window.addEventListener('DOMContentLoaded', () => {
    const today = new Date();
    const y = today.getFullYear();
    const m = String(today.getMonth() + 1).padStart(2, '0');
    const d = String(today.getDate()).padStart(2, '0');
    document.getElementById('startDate').value = `${y}-${m}-${d}`;

    ['startDate', 'operationType', 'numDays', 'dayType'].forEach(id => {
        const el = document.getElementById(id);
        el.addEventListener('input', calculateDateOffset);
        el.addEventListener('change', calculateDateOffset);
    });
    calculateDateOffset();
});
</script>"""

    article = """<h2>Calendrical Mechanics of Discrete Date Arithmetic</h2>
<p>Calculating chronological target dates across varying calendar intervals is deceptively complex due to non-uniform astronomical cycles, irregular monthly durations ranging from 28 to 31 days, and periodic intercalary leap day corrections. Unlike standard continuous metric units (where 100 centimeters consistently equals 1 meter), the Gregorian civil calendar is a piecewise irregular discrete system established by Papal Bull <em>Inter gravissimas</em> promulgated by Pope Gregory XIII in October 1582.</p>

<p>To accurately add or subtract an arbitrary integer number of days $N$ from an initial calendar date $D_0 = (Y_0, M_0, D_0)$, modern computational astronomy converts the calendar triple into a continuous scalar known as the <strong>Julian Day Number (JDN)</strong>. The JDN counts the integer number of civil solar days elapsed since Greenwich mean noon on January 1, 4713 BCE in the proleptic Julian calendar.</p>

<p>The conversion of any Gregorian date $(Y, M, D)$ where $M > 2$ (with January and February treated as months 13 and 14 of the preceding year $Y - 1$) is expressed via the Fliegel-Van Flandern algorithm:</p>

$$\text{JDN} = D + \left\lfloor \frac{153(M + 1)}{5} \right\rfloor + 365Y + \left\lfloor \frac{Y}{4} \right\rfloor - \left\lfloor \frac{Y}{100} \right\rfloor + \left\lfloor \frac{Y}{400} \right\rfloor - 32045$$

<p>Once transformed into continuous integer coordinates, temporal projection reduces to basic scalar arithmetic:</p>

$$\text{JDN}_{\text{target}} = \text{JDN}_{\text{start}} \pm N$$

<p>The resulting integer $\text{JDN}_{\text{target}}$ is subsequently mapped back to the Gregorian year, month, and day through an inverted division sequence that inherently and flawlessly accounts for every intervening leap year.</p>

<h2>Gregorian Leap Year Rules and Century Boundaries</h2>
<p>The fundamental leap year mechanism corrects for the astronomical tropical year (the orbital period of Earth around the Sun), which is approximately $365.24219$ mean solar days rather than exactly $365.25$ days. The complete Gregorian algorithmic rule evaluates whether a given year $Y$ contains an intercalary February 29th through three logical predicates:</p>

$$\text{IsLeap}(Y) = (Y \bmod 4 = 0) \land \big((Y \bmod 100 \neq 0) \lor (Y \bmod 400 = 0)\big)$$

<ul>
    <li><strong>Quadrennial Rule:</strong> Every year evenly divisible by 4 is a leap year (e.g., 2024, 2028, 2032).</li>
    <li><strong>Centurial Exception:</strong> Every century year evenly divisible by 100 is NOT a leap year (e.g., 1700, 1800, 1900, 2100).</li>
    <li><strong>Quadricentennial Correction:</strong> Every 400th century year IS a leap year (e.g., 1600, 2000, 2400).</li>
</ul>

<p>Neglecting this quadricentennial logic in date arithmetic produces substantial cumulative timing errors when projecting contracts, bond maturities, or legal trust milestones across century thresholds.</p>

<h2>Calendar Days vs. Business Working Days</h2>
<p>In legal contracting, real estate escrow, construction scheduling, and financial clearinghouse operations, statutory deadlines are commonly defined under two distinct counting regimes:</p>

<ol>
    <li><strong>Consecutive Calendar Days:</strong> Includes every natural diurnal cycle without exception. A 30-day notice period advances the date by exactly $30 \times 24$ hours.</li>
    <li><strong>Business (Working) Days:</strong> Strictly excludes non-working weekend days (Saturdays and Sundays where commercial banks and courts are closed). Adding $N_{\text{bus}}$ business days advances the calendar span by approximately:
    $$N_{\text{cal}} \approx N_{\text{bus}} + 2 \times \left\lfloor \frac{N_{\text{bus}} + \text{DoW}_0 - 1}{5} \right\rfloor$$
    </li>
</ol>

<p>Thus, adding 20 business days to a contract signed on a Monday advances the calendar date by 28 natural calendar days (spanning 4 full weekends).</p>

<h3>Commercial Deadline Reference Matrix</h3>
<p>The following table provides the comparative calendar vs. business day progression across standard statutory legal and commercial deadline benchmarks:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Statutory Period Name</th>
            <th>Offset Count ($N$)</th>
            <th>Calendar Duration</th>
            <th>Approximate Business Days</th>
            <th>Typical Industry Application</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Two-Week Notice</td><td>14 Days</td><td>2 Weeks (14 d)</td><td>10 Business Days</td><td>Employment resignation, tenant cure notice</td></tr>
        <tr><td>Monthly Billing Cycle</td><td>30 Days</td><td>4.3 Weeks (30 d)</td><td>21 - 22 Business Days</td><td>Net-30 commercial trade invoicing</td></tr>
        <tr><td>Standard Cure Period</td><td>45 Days</td><td>6.4 Weeks (45 d)</td><td>31 - 33 Business Days</td><td>Real estate mortgage closing contingencies</td></tr>
        <tr><td>Statutory Review Period</td><td>60 Days</td><td>8.6 Weeks (60 d)</td><td>42 - 44 Business Days</td><td>Environmental impact public comment</td></tr>
        <tr><td>Quarterly Reporting</td><td>90 Days</td><td>12.9 Weeks (90 d)</td><td>64 - 65 Business Days</td><td>SEC 10-Q corporate fiscal disclosures</td></tr>
        <tr><td>Semi-Annual Horizon</td><td>180 Days</td><td>25.7 Weeks (180 d)</td><td>128 - 130 Business Days</td><td>Treasury bill maturities, non-compete terms</td></tr>
        <tr><td>Annual Period</td><td>365 Days</td><td>52.1 Weeks (365 d)</td><td>260 - 261 Business Days</td><td>Statute of limitations, warranty expiration</td></tr>
    </tbody>
</table>

<div class="worked-example-card">
    <h3>Worked Legal Case Study: Commercial Real Estate Escrow Closing Deadline</h3>
    <p><strong>Scenario:</strong> A commercial real estate purchase agreement is formally executed on <strong>Friday, October 16, 2026</strong>. Section 14.2 of the contract stipulates that the buyer's earnest money deposit becomes non-refundable exactly <strong>45 calendar days</strong> following the execution date, while the title inspection contingency expires in <strong>30 business days</strong>. Determine the exact calendar dates for both contractual deadlines.</p>
    
    <div class="step-solution">
        <h4>Step 1: Calculate the 45 Calendar Day Milestone</h4>
        <p>Execution: October 16, 2026 ($\text{DoY} = 289$).</p>
        <p>October has 31 days. Remaining days in October: $31 - 16 = 15 \text{ days}$.</p>
        <p>Days remaining to allocate: $45 - 15 = 30 \text{ days}$.</p>
        <p>November has exactly 30 days.</p>
        <p>Therefore, 45 calendar days lands precisely on: <strong>Monday, November 30, 2026</strong>.</p>

        <h4>Step 2: Calculate the 30 Business Day Milestone</h4>
        <p>Starting Saturday, October 17, 2026:</p>
        <ul>
            <li>Week 1 (Oct 19 - Oct 23): 5 business days (Running total: 5)</li>
            <li>Week 2 (Oct 26 - Oct 30): 5 business days (Running total: 10)</li>
            <li>Week 3 (Nov 02 - Nov 06): 5 business days (Running total: 15)</li>
            <li>Week 4 (Nov 09 - Nov 13): 5 business days (Running total: 20)</li>
            <li>Week 5 (Nov 16 - Nov 20): 5 business days (Running total: 25)</li>
            <li>Week 6 (Nov 23 - Nov 27): 5 business days (Running total: 30)</li>
        </ul>
        <p>The 30th business day falls on: <strong>Friday, November 27, 2026</strong>.</p>
        <p><strong>Result:</strong> The title contingency expires first on Friday, November 27, 2026, followed 3 days later by the deposit deadline on Monday, November 30, 2026.</p>
    </div>
</div>

<h2>Common Implementation Errors in Date Arithmetic</h2>
<ol>
    <li><strong>Naive Millisecond Addition:</strong> In software code, adding milliseconds ($N \times 86,400,000 \text{ ms}$) without timezone-aware date wrappers causes dates to shift by one hour backwards or forwards when traversing Daylight Saving Time (DST) transitions (e.g., resulting in 23:00 on the previous day).</li>
    <li><strong>Month Increment Assumptions:</strong> Assuming that "adding one month" equals adding 30 days introduces errors ranging from 1 to 3 days depending on whether the intervening month is February, April, or July. Discrete day offsets must always be explicit.</li>
    <li><strong>Inclusive vs. Exclusive Boundary Counting:</strong> Under common law legal principles, the day of the triggering act (Day 0) is excluded from the calculation, while the final day of the period is included ("from and after" rule).</li>
</ol>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article)


def main():
    w_html = gen_week_number()
    with open(os.path.join(BASE_DIR, "week-number-calculator.html"), "w", encoding="utf-8") as f:
        f.write(w_html)
    print("Generated week-number-calculator.html successfully!")

    a_html = gen_add_days_to_date()
    with open(os.path.join(BASE_DIR, "add-days-to-date-calculator.html"), "w", encoding="utf-8") as f:
        f.write(a_html)
    print("Generated add-days-to-date-calculator.html successfully!")

if __name__ == "__main__":
    main()
