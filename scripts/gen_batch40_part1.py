# -*- coding: utf-8 -*-
"""
Generator for Batch 40 - Part 1
Tools:
1. day-of-week-calculator.html (Zeller's Congruence, Doomsday Rule, Historical Weekdays)
2. day-of-year-calculator.html (Ordinal Dates, ISO 8601 YYYY-DDD, Solar Declination)
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
                        <li><a href="day-of-week-calculator.html">Day of Week Calculator</a></li>
                        <li><a href="day-of-year-calculator.html">Day of Year Calculator</a></li>
                        <li><a href="week-number-calculator.html">ISO Week Number</a></li>
                        <li><a href="date-calculator.html">Date Calculator</a></li>
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
                        <li><a href="day-of-week-calculator.html">Day of Week Calculator</a></li>
                        <li><a href="day-of-year-calculator.html">Day of Year Calculator</a></li>
                        <li><a href="week-number-calculator.html">ISO Week Number</a></li>
                        <li><a href="date-calculator.html">Date Calculator</a></li>
                        <li><a href="add-days-to-date-calculator.html">Add Days to Date</a></li>
                        <li><a href="business-days-calculator.html">Business Days Calculator</a></li>
                        <li><a href="hours-calculator.html">Work Hours Calculator</a></li>
                    </ul>
                </div>
            </aside>
        </div>
    </div>
{COMMON_TAIL}"""


# ===========================================================================
# TOOL 1: day-of-week-calculator.html
# ===========================================================================
def gen_day_of_week():
    slug = "day-of-week-calculator"
    title = "Day of the Week Calculator | Zeller's Congruence & Doomsday Algorithm"
    desc = "Find the exact day of the week for any past, present, or future date using Zeller's Congruence. Discover what day of the week you were born and historical weekdays."
    h1 = "Day of the Week Calculator"
    short_desc = "Determine the exact weekday for any Gregorian calendar date using Christian Zeller's congruence algorithm and John Conway's Doomsday rule."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Day of the Week Calculator",
      "url": "https://calchub.com/day-of-week-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Calculates the exact day of the week for any calendar date using Zeller's congruence algorithm."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is Zeller's Congruence algorithm?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Zeller's Congruence is an algebraic formula devised by German mathematician Christian Zeller in 1882 to calculate the day of the week for any Gregorian or Julian calendar date based on day, month, century, and year components."
          }
        },
        {
          "@type": "Question",
          "name": "Why are January and February treated as months 13 and 14?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In Zeller's Congruence, the astronomical year is defined as starting in March. Treating January and February as months 13 and 14 of the preceding year places the intercalary leap day (February 29th) at the very end of the year, preventing leap day shifts from disrupting the formula for the remaining ten months."
          }
        },
        {
          "@type": "Question",
          "name": "What is John Conway's Doomsday rule?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The Doomsday rule is a mental arithmetic algorithm invented by mathematician John Horton Conway. It relies on the fact that certain memorable calendar dates (such as 4/4, 6/6, 8/8, 10/10, and 12/12) always fall on the exact same day of the week (the 'Doomsday') in any given year."
          }
        },
        {
          "@type": "Question",
          "name": "What was the day of the week on July 4, 1776?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Applying Zeller's Congruence, July 4, 1776 (the day the United States Declaration of Independence was adopted) fell on a Thursday."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-grid">
    <div class="calc-inputs">
        <div class="input-group">
            <label for="dowDate">Select Calendar Date</label>
            <input type="date" id="dowDate" class="input-field">
            <span class="input-hint">Select any date (e.g., your birthdate or historical event)</span>
        </div>
        <div style="display:flex;gap:0.5rem;flex-wrap:wrap;margin-top:0.5rem;">
            <button type="button" class="btn-outline" onclick="setDowPreset('today')">Today</button>
            <button type="button" class="btn-outline" onclick="setDowPreset('1776-07-04')">US Indep (1776)</button>
            <button type="button" class="btn-outline" onclick="setDowPreset('1969-07-20')">Apollo 11 (1969)</button>
            <button type="button" class="btn-outline" onclick="setDowPreset('2000-01-01')">Y2K (2000)</button>
        </div>
    </div>
    <div class="calc-results">
        <div class="result-card primary-result">
            <div class="result-label">Computed Day of the Week</div>
            <div class="result-value" id="resDayName" style="font-size:2.25rem;color:var(--brand-primary, #2563eb);">Sunday</div>
            <div class="result-sub" id="resIsoDay">ISO-8601 Day 7 • Weekend Day</div>
        </div>
        <div class="result-grid-mini" style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;margin-top:1rem;">
            <div class="result-card">
                <div class="result-label">Zeller Remainder ($h$)</div>
                <div class="result-value-sm" id="resZellerH">h = 1 (Sunday)</div>
            </div>
            <div class="result-card">
                <div class="result-label">Conway Doomsday</div>
                <div class="result-value-sm" id="resDoomsday">Sunday for 2026</div>
            </div>
            <div class="result-card">
                <div class="result-label">Day of Year</div>
                <div class="result-value-sm" id="resDoyVal">Day 278 of 365</div>
            </div>
            <div class="result-card">
                <div class="result-label">Leap Year Status</div>
                <div class="result-value-sm" id="resLeapStatus">Common Year (365 d)</div>
            </div>
        </div>
        <div class="result-card" style="margin-top:1rem;background:var(--bg-accent, #eff6ff);border-left:4px solid var(--brand-primary, #2563eb);">
            <div class="result-label">Cultural &amp; Astrological Context</div>
            <div class="result-value" id="resPlanetary" style="color:var(--brand-primary, #2563eb);font-size:1.25rem;">Sun's Day (Dominica / Sol)</div>
            <div class="result-sub" id="resRomanName">Classical Latin: Dies Solis • Traditional rest day</div>
        </div>
    </div>
</div>
<script>
function zellerDayOfWeek(y, m, q) {
    if (m <= 2) {
        m += 12;
        y -= 1;
    }
    const K = y % 100;
    const J = Math.floor(y / 100);
    // Zeller Gregorian: h = (q + floor(13(m+1)/5) + K + floor(K/4) + floor(J/4) - 2J) mod 7
    // h: 0=Sat, 1=Sun, 2=Mon, 3=Tue, 4=Wed, 5=Thu, 6=Fri
    let h = (q + Math.floor((13 * (m + 1)) / 5) + K + Math.floor(K / 4) + Math.floor(J / 4) - (2 * J)) % 7;
    if (h < 0) h += 7;
    return h;
}

function calculateDayOfWeek() {
    const dateStr = document.getElementById('dowDate').value;
    if (!dateStr) return;

    const [y, m, q] = dateStr.split('-').map(Number);
    const h = zellerDayOfWeek(y, m, q);

    const zellerDays = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];
    const dayName = zellerDays[h];

    // ISO day: Mon=1 ... Sun=7
    const isoDays = { 'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7 };
    const isoNum = isoDays[dayName];
    const isWeekend = (dayName === 'Saturday' || dayName === 'Sunday');

    // Doomsday anchor for year
    // Anchor for century: 1800=Fri(5), 1900=Wed(3), 2000=Tue(2), 2100=Sun(0)
    const c = Math.floor(y / 100);
    const anchorMap = { 0: 2, 1: 0, 2: 5, 3: 3 }; // mod 4 from 2000
    const anchor = anchorMap[((c % 4) + 4) % 4];
    const yPart = y % 100;
    const doomsdayVal = (anchor + yPart + Math.floor(yPart / 4)) % 7;
    const conwayDays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    const doomsdayName = conwayDays[doomsdayVal];

    // Day of Year
    const startOfYear = new Date(y, 0, 1);
    const curDate = new Date(y, m - 1, q);
    const isLeap = (y % 4 === 0 && (y % 100 !== 0 || y % 400 === 0));
    const totalDays = isLeap ? 366 : 365;
    const doy = Math.floor((curDate - startOfYear) / 86400000) + 1;

    // Planetary / Etymological details
    const planetaryInfo = {
        'Monday': { name: "Moon's Day (Dies Lunae)", sub: "Associated with silver, tides, and maternal renewal" },
        'Tuesday': { name: "Tiw's / Mars' Day (Dies Martis)", sub: "Associated with iron, vigor, and courageous action" },
        'Wednesday': { name: "Woden's / Mercury's Day (Dies Mercurii)", sub: "Associated with communication, commerce, and intellect" },
        'Thursday': { name: "Thor's / Jupiter's Day (Dies Iovis)", sub: "Associated with tin, expansion, and benevolent wisdom" },
        'Friday': { name: "Frigg's / Venus' Day (Dies Veneris)", sub: "Associated with copper, harmony, beauty, and social warmth" },
        'Saturday': { name: "Saturn's Day (Dies Saturni)", sub: "Associated with lead, discipline, boundaries, and endurance" },
        'Sunday': { name: "Sun's Day (Dies Solis)", sub: "Associated with gold, vitality, solar radiance, and enlightenment" }
    };

    document.getElementById('resDayName').innerText = dayName;
    document.getElementById('resIsoDay').innerText = `ISO-8601 Day ${isoNum} • ${isWeekend ? 'Weekend Day' : 'Standard Working Weekday'}`;
    document.getElementById('resZellerH').innerText = `h = ${h} (${dayName})`;
    document.getElementById('resDoomsday').innerText = `${doomsdayName} for Year ${y}`;
    document.getElementById('resDoyVal').innerText = `Day ${doy} of ${totalDays}`;
    document.getElementById('resLeapStatus').innerText = isLeap ? 'Leap Year (366 days)' : 'Common Year (365 days)';
    document.getElementById('resPlanetary').innerText = planetaryInfo[dayName].name;
    document.getElementById('resRomanName').innerText = planetaryInfo[dayName].sub;
}

function setDowPreset(val) {
    if (val === 'today') {
        const today = new Date();
        const y = today.getFullYear();
        const m = String(today.getMonth() + 1).padStart(2, '0');
        const d = String(today.getDate()).padStart(2, '0');
        document.getElementById('dowDate').value = `${y}-${m}-${d}`;
    } else {
        document.getElementById('dowDate').value = val;
    }
    calculateDayOfWeek();
}

window.addEventListener('DOMContentLoaded', () => {
    const today = new Date();
    const y = today.getFullYear();
    const m = String(today.getMonth() + 1).padStart(2, '0');
    const d = String(today.getDate()).padStart(2, '0');
    document.getElementById('dowDate').value = `${y}-${m}-${d}`;

    document.getElementById('dowDate').addEventListener('change', calculateDayOfWeek);
    document.getElementById('dowDate').addEventListener('input', calculateDayOfWeek);
    calculateDayOfWeek();
});
</script>"""

    article = """<h2>Mathematical Formulation of Zeller's Congruence</h2>
<p>Determining the day of the week corresponding to any arbitrary historical, contemporary, or future calendar date is one of the classic problems in discrete calendrical mathematics. While naive human computation requires counting elapsed days across varying monthly lengths and leap years, analytical number theory provides exact closed-form algebraic solutions. The most famous and mathematically rigorous formulation is <strong>Zeller's Congruence</strong>, published in 1882 by the German mathematician and theologian Christian Zeller.</p>

<p>For the Gregorian calendar, Zeller's Congruence evaluates an integer index $h$ corresponding to the day of the week according to the following equation:</p>

$$h = \left( q + \left\lfloor \frac{13(m + 1)}{5} \right\rfloor + K + \left\lfloor \frac{K}{4} \right\rfloor + \left\lfloor \frac{J}{4} \right\rfloor - 2J \right) \bmod 7$$

<p>Where the algebraic variables are strictly defined as follows:</p>
<ul>
    <li>$q$: The day of the month ($1 \le q \le 31$).</li>
    <li>$m$: The month of the year, transformed so that the year begins in March:
        <ul>
            <li>March = 3, April = 4, May = 5, ..., December = 12.</li>
            <li><strong>January = 13 and February = 14 of the preceding year ($Y - 1$).</strong></li>
        </ul>
    </li>
    <li>$K$: The year of the century ($K = Y \bmod 100$).</li>
    <li>$J$: The zero-based century index ($J = \lfloor Y / 100 \rfloor$).</li>
</ul>

<p>The resulting integer $h$ maps directly to the classical days of the week: $h = 0 \implies \text{Saturday}$, $h = 1 \implies \text{Sunday}$, $h = 2 \implies \text{Monday}$, $h = 3 \implies \text{Tuesday}$, $h = 4 \implies \text{Wednesday}$, $h = 5 \implies \text{Thursday}$, and $h = 6 \implies \text{Friday}$.</p>

<h3>The March Month Re-Indexing Principle</h3>
<p>The brilliant innovation of Zeller's formulation lies in treating January and February as months 13 and 14 of the previous year. In the astronomical Gregorian calendar, leap day intercalations occur exclusively on February 29th. By placing the leap day at the very end of the mathematical year (as the terminal day of Month 14), leap years exert zero disruptive offset on the progression of the subsequent ten months (March through December), preserving a perfectly uniform linear term $\lfloor 13(m+1)/5 \rfloor$.</p>

<h2>John Conway's Doomsday Mental Calculation Rule</h2>
<p>In 1973, Princeton mathematician John Horton Conway formulated the <strong>Doomsday Rule</strong>, a mental arithmetic algorithm designed to enable humans to calculate the day of the week for any date in seconds without writing code or equations.</p>

<p>The Doomsday rule is founded on the mathematical invariance that in any given year, a specific set of memorable calendar dates always fall on the exact same day of the week, known as the year's <strong>Doomsday</strong>:</p>

<ul>
    <li><strong>Even Months:</strong> $4/4$ (April 4), $6/6$ (June 6), $8/8$ (August 8), $10/10$ (October 10), and $12/12$ (December 12).</li>
    <li><strong>Odd Months (Mnemonic "Work 9 to 5 at 7-11"):</strong> $5/9$ (May 9), $9/5$ (September 5), $7/11$ (July 11), and $11/7$ (November 7).</li>
    <li><strong>Terminal February Day:</strong> The last day of February (February 28 in common years, February 29 in leap years).</li>
    <li><strong>Independence Day:</strong> July 4th.</li>
    <li><strong>Halloween:</strong> October 31st.</li>
</ul>

<p>To determine the Doomsday for a year $Y$, calculate the Century Anchor $C$ (where $1800\text{s} = \text{Friday}$, $1900\text{s} = \text{Wednesday}$, $2000\text{s} = \text{Tuesday}$, $2100\text{s} = \text{Sunday}$) and evaluate the year's two-digit offset $y = Y \bmod 100$:</p>

$$\text{Doomsday} = \left( C + \left\lfloor \frac{y}{12} \right\rfloor + (y \bmod 12) + \left\lfloor \frac{y \bmod 12}{4} \right\rfloor \right) \bmod 7$$

<h3>Seven-Day Planetary and Etymological Reference Matrix</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Day Name</th>
            <th>ISO-8601 Index</th>
            <th>Zeller Remainder ($h$)</th>
            <th>Classical Latin Name</th>
            <th>Celestial Archetype</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Monday</td><td>Day 1</td><td>$h = 2$</td><td>Dies Lunae</td><td>Moon (Silver, Tides)</td></tr>
        <tr><td>Tuesday</td><td>Day 2</td><td>$h = 3$</td><td>Dies Martis</td><td>Mars (Iron, Strength)</td></tr>
        <tr><td>Wednesday</td><td>Day 3</td><td>$h = 4$</td><td>Dies Mercurii</td><td>Mercury (Quicksilver, Intellect)</td></tr>
        <tr><td>Thursday</td><td>Day 4</td><td>$h = 5$</td><td>Dies Iovis</td><td>Jupiter (Tin, Expansion)</td></tr>
        <tr><td>Friday</td><td>Day 5</td><td>$h = 6$</td><td>Dies Veneris</td><td>Venus (Copper, Harmony)</td></tr>
        <tr><td>Saturday</td><td>Day 6</td><td>$h = 0$</td><td>Dies Saturni</td><td>Saturn (Lead, Structure)</td></tr>
        <tr><td>Sunday</td><td>Day 7</td><td>$h = 1$</td><td>Dies Solis</td><td>Sun (Gold, Vitality)</td></tr>
    </tbody>
</table>

<div class="worked-example-card">
    <h3>Worked Historical Case Study: The Apollo 11 Lunar Landing</h3>
    <p><strong>Scenario:</strong> On <strong>July 20, 1969</strong>, Apollo 11 astronaut Neil Armstrong stepped onto the lunar surface at 02:56 UTC. Calculate the exact day of the week for July 20, 1969 using Zeller's Congruence.</p>
    
    <div class="step-solution">
        <h4>Step 1: Extract and Normalize Zeller Variables</h4>
        <p>Day: $q = 20$.</p>
        <p>Month: July is Month 7 ($m = 7$). Since $m > 2$, year remains 1969.</p>
        <p>Century Index: $J = \lfloor 1969 / 100 \rfloor = 19$.</p>
        <p>Century Year: $K = 1969 \bmod 100 = 69$.</p>

        <h4>Step 2: Evaluate the Algebraic Terms</h4>
        $$\left\lfloor \frac{13(m + 1)}{5} \right\rfloor = \left\lfloor \frac{13(8)}{5} \right\rfloor = \left\lfloor \frac{104}{5} \right\rfloor = 20$$
        $$\left\lfloor \frac{K}{4} \right\rfloor = \left\lfloor \frac{69}{4} \right\rfloor = 17$$
        $$\left\lfloor \frac{J}{4} \right\rfloor = \left\lfloor \frac{19}{4} \right\rfloor = 4$$
        $$-2J = -2(19) = -38$$

        <h4>Step 3: Sum the Terms</h4>
        $$\text{Sum} = q + 20 + K + 17 + 4 - 38 = 20 + 20 + 69 + 17 + 4 - 38 = 92$$

        <h4>Step 4: Compute the Modulo 7 Remainder</h4>
        $$h = 92 \bmod 7$$
        <p>Since $92 = (13 \times 7) + 1$, the remainder is $h = 1$.</p>
        <p><strong>Conclusion:</strong> In Zeller's table, $h = 1$ corresponds precisely to <strong>Sunday</strong>! The Apollo 11 moon landing occurred on a Sunday evening in US timezones.</p>
    </div>
</div>

<h2>Common Calculation Errors and Historical Anomalies</h2>
<ol>
    <li><strong>The Gregorian Calendar Reform Shift (October 1582):</strong> Applying the Gregorian formula to dates prior to October 15, 1582 produces invalid results because European nations utilized the Julian calendar. During the reform, Pope Gregory XIII excised 10 full days: Thursday, October 4, 1582 was immediately followed by Friday, October 15, 1582.</li>
    <li><strong>British and American Adoption (September 1752):</strong> Great Britain and its American colonies did not adopt the Gregorian calendar until September 1752, when 11 days were dropped (Wednesday, September 2, 1752 was followed by Thursday, September 14, 1752). Historical American dates before 1752 require Julian Zeller math.</li>
    <li><strong>Negative Modulo Operations in Software:</strong> In languages such as C, C++, and JavaScript, the remainder operator <code>%</code> can return negative values for negative dividends (e.g., <code>-3 % 7 = -3</code> instead of $+4$). Software implementations must add 7 to negative remainders to guarantee non-negative mathematical congruence.</li>
</ol>
<h2>Perpetual Calendar Cycles and the 400-Year Gregorian Periodicity</h2>
<p>Because the Gregorian calendar introduces 97 leap days across every 400-year cycle, the total number of days in 400 Gregorian years is exactly:
$$400 \times 365 + 97 = 146,097 \text{ days}$$
Dividing 146,097 by 7 yields:
$$\frac{146,097}{7} = 20,871 \text{ weeks exactly with 0 remainder!}$$
This remarkable mathematical identity means that the Gregorian calendar repeats in an exact, unbroken cycle every 400 years. October 5, 2026 will fall on the exact same weekday as October 5, 2426, and fell on the same day in 1626. Furthermore, within any single century, days of the week shift forward by 1 day in standard years ($365 \bmod 7 = 1$) and by 2 days in leap years ($366 \bmod 7 = 2$). This simple modular shift governs all perpetual calendar mechanical wheels and digital perpetual clock algorithms.</p>

<section class="faq-section">
    <h2>Frequently Asked Questions About Day of the Week Calculations</h2>
    <div class="faq-item">
        <h3>How does Zeller's Congruence handle leap years?</h3>
        <p>Zeller's congruence handles leap years by re-indexing January and February as months 13 and 14 of the preceding year. Because February is treated as the final month of the year, leap day adjustments (February 29th) are naturally captured by the term $\lfloor K/4 \rfloor$ and $\lfloor J/4 \rfloor$ without perturbing March through December calculations.</p>
    </div>
    <div class="faq-item">
        <h3>Why did October 1582 lose 10 days?</h3>
        <p>In October 1582, Pope Gregory XIII implemented the Gregorian calendar reform to correct the 10-day drift accumulated by the Julian calendar's assumption that an astronomical solar year was exactly 365.25 days (rather than approximately 365.2422 days). To re-align the vernal equinox with March 21 for Easter computations, October 4, 1582 was immediately followed by October 15, 1582.</p>
    </div>
    <div class="faq-item">
        <h3>What is the Doomsday rule mnemonic for months?</h3>
        <p>John Conway's Doomsday rule uses memorable calendar anchors that always share the identical day of the week within any given year: 4/4, 6/6, 8/8, 10/10, 12/12 for even months, and the mnemonic "I work 9-to-5 at 7-11" for odd months (9/5, 5/9, 7/11, 11/7).</p>
    </div>
    <div class="faq-item">
        <h3>Can Zeller's Congruence be used for dates BC / BCE?</h3>
        <p>Standard Zeller's congruence requires astronomical year numbering where 1 BC is Year 0, 2 BC is Year -1, etc. In software, negative modulo operations must also be carefully normalized to prevent incorrect weekday mappings.</p>
    </div>
</section>
"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article)


# ===========================================================================
# TOOL 2: day-of-year-calculator.html
# ===========================================================================
def gen_day_of_year():
    slug = "day-of-year-calculator"
    title = "Day of the Year Calculator | Ordinal Date (ISO 8601 YYYY-DDD)"
    desc = "Find the exact day of the year (1 to 366), ordinal date, days remaining, percentage of year complete, and solar declination angle for any calendar date."
    h1 = "Day of the Year Calculator"
    short_desc = "Compute the continuous ordinal day of the year (Day 1 to 366), percentage of the annual solar cycle elapsed, and astronomical solar declination angles."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Day of the Year Calculator",
      "url": "https://calchub.com/day-of-year-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Calculates the continuous day of the year, ISO 8601 ordinal date, days remaining, and annual percentage elapsed."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is an ordinal date under ISO 8601?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "An ordinal date is an international standard date format defined by ISO 8601 as YYYY-DDD, where YYYY is the four-digit calendar year and DDD is the three-digit day of the year ranging from 001 to 365 (or 001 to 366 in a leap year)."
          }
        },
        {
          "@type": "Question",
          "name": "How is the day of the year calculated algebraically?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The day of the year is calculated by summing the fixed lengths of all months preceding the target month, adding the current day of the month, and adding an additional day if the year is a leap year and the target date falls after February 29th."
          }
        },
        {
          "@type": "Question",
          "name": "How does the day of the year affect solar photovoltaic calculations?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Solar engineers use the day of the year (N) to calculate Earth's orbital solar declination angle (delta) and solar irradiance, which govern solar panel tilt optimization, solar azimuth, and atmospheric air mass."
          }
        },
        {
          "@type": "Question",
          "name": "What day of the year is July 1st in common and leap years?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In a standard 365-day year, July 1st is Day 182. In a leap year (366 days), July 1st is Day 183. In common years, July 2nd marks the exact midpoint of the year."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-grid">
    <div class="calc-inputs">
        <div class="input-group">
            <label for="doyTargetDate">Select Calendar Date</label>
            <input type="date" id="doyTargetDate" class="input-field">
            <span class="input-hint">Select any date to evaluate annual ordinal position</span>
        </div>
        <div style="display:flex;gap:0.5rem;flex-wrap:wrap;margin-top:0.5rem;">
            <button type="button" class="btn-outline" onclick="setDoyPreset('today')">Today</button>
            <button type="button" class="btn-outline" onclick="setDoyPreset('mid')">Mid-Year (Jul 2)</button>
            <button type="button" class="btn-outline" onclick="setDoyPreset('equinox')">Autumn Equinox</button>
            <button type="button" class="btn-outline" onclick="setDoyPreset('dec31')">Dec 31</button>
        </div>
    </div>
    <div class="calc-results">
        <div class="result-card primary-result">
            <div class="result-label">Ordinal Day of the Year</div>
            <div class="result-value" id="resDoyMain" style="font-size:2.5rem;color:var(--brand-primary, #2563eb);">Day 278</div>
            <div class="result-sub" id="resIsoOrdinal">ISO 8601 Ordinal Format: 2026-278</div>
        </div>
        <div class="result-grid-mini" style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;margin-top:1rem;">
            <div class="result-card">
                <div class="result-label">Days Remaining</div>
                <div class="result-value-sm" id="resDaysRemaining">87 Days Left</div>
            </div>
            <div class="result-card">
                <div class="result-label">Percentage Complete</div>
                <div class="result-value-sm" id="resPctComplete">76.16% Complete</div>
            </div>
            <div class="result-card">
                <div class="result-label">Solar Declination (&delta;)</div>
                <div class="result-value-sm" id="resSolarDeclination">-4.82&deg; South</div>
            </div>
            <div class="result-card">
                <div class="result-label">Total Days in Year</div>
                <div class="result-value-sm" id="resYearType">365 Days (Common)</div>
            </div>
        </div>
        <div class="result-card" style="margin-top:1rem;background:var(--bg-accent, #eff6ff);border-left:4px solid var(--brand-primary, #2563eb);">
            <div class="result-label">Astronomical &amp; Seasonal Alignment</div>
            <div class="result-value" id="resSeasonInfo" style="color:var(--brand-primary, #2563eb);font-size:1.25rem;">Autumn / Fall (Northern Hemisphere)</div>
            <div class="result-sub" id="resWeekNumInfo">Falls in ISO Week 41 • Q4 Quarter</div>
        </div>
    </div>
</div>
<script>
function calculateDayOfYear() {
    const dStr = document.getElementById('doyTargetDate').value;
    if (!dStr) return;

    const [y, m, d] = dStr.split('-').map(Number);
    const date = new Date(y, m - 1, d);
    const startOfYear = new Date(y, 0, 1);

    const isLeap = (y % 4 === 0 && (y % 100 !== 0 || y % 400 === 0));
    const totalDays = isLeap ? 366 : 365;

    const doy = Math.floor((date - startOfYear) / 86400000) + 1;
    const daysLeft = totalDays - doy;
    const pct = ((doy / totalDays) * 100).toFixed(2);

    // Solar Declination angle: delta = 23.45 * sin(360/365 * (doy + 284) deg)
    const angleRad = ((360 / 365) * (doy + 284)) * (Math.PI / 180);
    const deltaDeg = (23.45 * Math.sin(angleRad)).toFixed(2);
    const declText = deltaDeg >= 0 ? `+${deltaDeg}° North` : `${deltaDeg}° South`;

    // ISO ordinal string: YYYY-DDD
    const isoOrdinal = `${y}-${String(doy).padStart(3, '0')}`;

    // Season estimation (Northern Hemisphere meteorological)
    let season = 'Winter';
    if (doy >= 60 && doy < 152) season = 'Spring (Vernal)';
    else if (doy >= 152 && doy < 244) season = 'Summer (Estival)';
    else if (doy >= 244 && doy < 335) season = 'Autumn / Fall (Autumnal)';

    // ISO week number
    const tempDate = new Date(Date.UTC(y, m - 1, d));
    const dayNum = tempDate.getUTCDay() || 7;
    tempDate.setUTCDate(tempDate.getUTCDate() + 4 - dayNum);
    const yearStart = new Date(Date.UTC(tempDate.getUTCFullYear(), 0, 1));
    const weekNo = Math.ceil((((tempDate - yearStart) / 86400000) + 1) / 7);
    const quarter = Math.floor((m - 1) / 3) + 1;

    document.getElementById('resDoyMain').innerText = `Day ${doy}`;
    document.getElementById('resIsoOrdinal').innerText = `ISO 8601 Ordinal Format: ${isoOrdinal}`;
    document.getElementById('resDaysRemaining').innerText = `${daysLeft} Day${daysLeft !== 1 ? 's' : ''} Left`;
    document.getElementById('resPctComplete').innerText = `${pct}% Complete`;
    document.getElementById('resSolarDeclination').innerHTML = declText;
    document.getElementById('resYearType').innerText = `${totalDays} Days (${isLeap ? 'Leap Year' : 'Common Year'})`;
    document.getElementById('resSeasonInfo').innerText = `${season} (Northern Hemisphere)`;
    document.getElementById('resWeekNumInfo').innerText = `Falls in ISO Week ${weekNo} • Quarter ${quarter} (Q${quarter})`;
}

function setDoyPreset(type) {
    const today = new Date();
    const y = today.getFullYear();
    let target = new Date();

    if (type === 'today') {
        target = today;
    } else if (type === 'mid') {
        target = new Date(y, 6, 2);
    } else if (type === 'equinox') {
        target = new Date(y, 8, 22);
    } else if (type === 'dec31') {
        target = new Date(y, 11, 31);
    }

    const ty = target.getFullYear();
    const tm = String(target.getMonth() + 1).padStart(2, '0');
    const td = String(target.getDate()).padStart(2, '0');
    document.getElementById('doyTargetDate').value = `${ty}-${tm}-${td}`;
    calculateDayOfYear();
}

window.addEventListener('DOMContentLoaded', () => {
    const today = new Date();
    const y = today.getFullYear();
    const m = String(today.getMonth() + 1).padStart(2, '0');
    const d = String(today.getDate()).padStart(2, '0');
    document.getElementById('doyTargetDate').value = `${y}-${m}-${d}`;

    document.getElementById('doyTargetDate').addEventListener('change', calculateDayOfYear);
    document.getElementById('doyTargetDate').addEventListener('input', calculateDayOfYear);
    calculateDayOfYear();
});
</script>"""

    article = """<h2>Mathematical Mechanics of the Ordinal Day of the Year</h2>
<p>In astronomical modeling, geospatial data processing, solar radiation forecasting, and aerospace orbital mechanics, civil calendar representations based on variable month names and days are inherently unwieldy. Instead, engineering systems represent chronological progression as a continuous one-dimensional scalar known as the <strong>Day of the Year (DoY)</strong>, or <strong>ordinal date</strong>. Under international standard <strong>ISO 8601</strong>, an ordinal date is formally encoded as <code>YYYY-DDD</code>, where <code>DDD</code> spans monotonically from <code>001</code> to <code>365</code> (or <code>366</code> in an astronomical leap year).</p>

<p>For any Gregorian calendar date consisting of year $Y$, month $M \in \{1,\dots,12\}$, and day $D \in \{1,\dots,31\}$, the closed-form algebraic equation for the ordinal day of the year is given by:</p>

$$\text{DoY} = \left\lfloor \frac{275 \cdot M}{9} \right\rfloor - \left\lfloor \frac{M + 9}{12} \right\rfloor \cdot \big(1 + \mathbb{I}_{\text{leap}}(Y)\big) + D - 30$$

<p>Where $\mathbb{I}_{\text{leap}}(Y)$ is the binary indicator function returning 1 if $Y$ is a leap year and 0 otherwise. This integer formula eliminates table lookups by exploiting the linear slope approximation of monthly accumulations ($275/9 \approx 30.555$), with the step term $\lfloor (M+9)/12 \rfloor$ acting as an activation switch that suppresses February's anomaly for January and February ($M \le 2$), while subtracting 1 or 2 days for all subsequent months ($M \ge 3$).</p>

<h2>Solar Declination Angle and Radiation Modeling</h2>
<p>The primary scientific application of the Day of the Year ($N = \text{DoY}$) occurs in solar photovoltaic engineering and atmospheric meteorology. Because the Earth's rotational axis is tilted by an obliquity of approximately $23.45^\circ$ relative to the ecliptic plane, the apparent latitude where the Sun is directly overhead at solar noon (the <strong>Solar Declination Angle</strong> $\delta$) oscillates continuously throughout the annual cycle.</p>

<p>Cooper's fundamental astronomical approximation models solar declination $\delta$ as a sinusoidal function of the day of the year $N$:</p>

$$\delta = 23.45^\circ \times \sin\left( \frac{360^\circ}{365} \times (N + 284) \right)$$

<p>Where the phase shift of $+284$ days aligns the sinusoidal zero-crossing with the vernal equinox ($N \approx 80$, March 21st, where $\delta = 0^\circ$). The extreme boundaries occur at the solstices:</p>
<ul>
    <li><strong>Summer Solstice ($N \approx 172$, June 21):</strong> $\delta = +23.45^\circ$ (Sun zenith at Tropic of Cancer).</li>
    <li><strong>Winter Solstice ($N \approx 355$, December 21):</strong> $\delta = -23.45^\circ$ (Sun zenith at Tropic of Capricorn).</li>
</ul>

<p>Solar photovoltaic engineers directly feed $\delta$ into equations calculating the local solar zenith angle $\theta_z$, optimal photovoltaic array tilt angles ($\beta \approx \phi - \delta$), and atmospheric optical air mass ($AM$).</p>

<h3>Ordinal Day Reference Matrix for Month Start Boundaries</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Month ($M$)</th>
            <th>Common Year Start (DoY)</th>
            <th>Leap Year Start (DoY)</th>
            <th>Cumulative Annual Percentage</th>
            <th>Approximate Solar Declination ($\delta$)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>January 1</td><td>Day 001</td><td>Day 001</td><td>0.27%</td><td>-23.01&deg; South</td></tr>
        <tr><td>February 1</td><td>Day 032</td><td>Day 032</td><td>8.77%</td><td>-17.28&deg; South</td></tr>
        <tr><td>March 1</td><td>Day 060</td><td>Day 061</td><td>16.44%</td><td>-7.69&deg; South</td></tr>
        <tr><td>April 1</td><td>Day 091</td><td>Day 092</td><td>24.93%</td><td>+4.42&deg; North</td></tr>
        <tr><td>May 1</td><td>Day 121</td><td>Day 122</td><td>33.15%</td><td>+14.90&deg; North</td></tr>
        <tr><td>June 1</td><td>Day 152</td><td>Day 153</td><td>41.64%</td><td>+21.90&deg; North</td></tr>
        <tr><td>July 1</td><td>Day 182</td><td>Day 183</td><td>49.86%</td><td>+23.12&deg; North</td></tr>
        <tr><td>August 1</td><td>Day 213</td><td>Day 214</td><td>58.36%</td><td>+18.08&deg; North</td></tr>
        <tr><td>September 1</td><td>Day 244</td><td>Day 245</td><td>66.85%</td><td>+8.57&deg; North</td></tr>
        <tr><td>October 1</td><td>Day 274</td><td>Day 275</td><td>75.07%</td><td>-2.99&deg; South</td></tr>
        <tr><td>November 1</td><td>Day 305</td><td>Day 306</td><td>83.56%</td><td>-14.28&deg; South</td></tr>
        <tr><td>December 1</td><td>Day 335</td><td>Day 336</td><td>91.78%</td><td>-21.68&deg; South</td></tr>
    </tbody>
</table>

<div class="worked-example-card">
    <h3>Worked Solar Engineering Case Study: Photovoltaic Peak Solar Declination</h3>
    <p><strong>Scenario:</strong> A solar farm installation in Phoenix, Arizona ($\text{Latitude } \phi = 33.45^\circ \text{ N}$) is optimizing fixed-tilt single-axis tracking algorithms for <strong>October 5, 2026</strong>. Determine: (1) the ordinal day of the year ($N$), (2) the percentage of the calendar year elapsed, and (3) the exact solar declination angle ($\delta$).</p>
    
    <div class="step-solution">
        <h4>Step 1: Verify Leap Year Status</h4>
        <p>Year 2026: $2026 \bmod 4 = 2 \neq 0$. Common year (365 days).</p>

        <h4>Step 2: Calculate Ordinal Day ($N$)</h4>
        <p>From the reference matrix, October 1st in a common year is Day 274.</p>
        $$N = \text{Day}(\text{Oct 1}) + (5 - 1) = 274 + 4 = 278$$
        <p><strong>Ordinal Date:</strong> <code>2026-278</code>.</p>

        <h4>Step 3: Calculate Annual Percentage Elapsed</h4>
        $$\text{Percentage} = \frac{278}{365} \times 100\% \approx 76.1644\%$$

        <h4>Step 4: Compute Solar Declination Angle ($\delta$)</h4>
        $$\theta_{\text{arg}} = \frac{360^\circ}{365} \times (278 + 284) = \frac{360^\circ}{365} \times 562 = 554.3014^\circ$$
        $$\theta_{\text{normalized}} = 554.3014^\circ - 360^\circ = 194.3014^\circ$$
        $$\sin(194.3014^\circ) \approx -0.2470$$
        $$\delta = 23.45^\circ \times (-0.2470) \approx -5.79^\circ$$
        <p><strong>Result:</strong> The Sun's subsolar point lies at approximately $5.79^\circ$ South latitude, indicating the Northern Hemisphere autumn solar descent.</p>
    </div>
</div>

<h2>Common Implementation Pitfalls with Day of the Year</h2>
<ol>
    <li><strong>Confusing Ordinal Day with Julian Day Number (JDN):</strong> In computer science documentation and legacy codebases, the ordinal Day of the Year (1 to 365) is frequently mislabeled as a "Julian date" (e.g., calling <code>2026-278</code> a Julian date). In strict astronomy, Julian Date represents the continuous count of days since 4713 BCE (e.g., $\text{JD } 2,461,319.5$). Conflating the two creates catastrophic database synchronization errors.</li>
    <li><strong>Zero-Based vs. One-Based Indexing Discrepancies:</strong> In C <code>struct tm</code> (POSIX), the member <code>tm_yday</code> is zero-based ($0 \le \text{tm\_yday} \le 365$, where January 1 is Day 0). In ISO 8601, ordinal dates are strictly one-based ($001 \le \text{DDD} \le 366$). Converting between POSIX systems and ISO displays requires careful $+1$ offset handling.</li>
    <li><strong>The Leap Day Boundary Shift:</strong> Omitting the quadrennial check shifts all dates after February 28th backward by exactly one day in leap years, throwing off agricultural growing degree day (GDD) calculations and satellite ground-track predictions.</li>
</ol>
<h2>Agricultural Growing Degree Days and Phenological Modeling</h2>
<p>Agronomists, horticulturists, and climate scientists rely on continuous day-of-the-year numbering to track Growing Degree Days (GDD) and biological life cycle milestones (phenology). Standard calendar months introduce uneven day intervals (28 to 31 days) that distort thermal accumulation integrals. By utilizing continuous ordinal days $N$, daily mean temperatures $T_{\text{mean}}$ above a base physiological threshold $T_{\text{base}}$ are integrated seamlessly:
$$\text{GDD}_{\text{cumulative}} = \sum_{N = N_{\text{bio}}}^{N_{\text{harvest}}} \max\left(0, \frac{T_{\text{max}}(N) + T_{\text{min}}(N)}{2} - T_{\text{base}}\right)$$
This enables predictive harvesting models for commercial corn, wheat, viticulture, and orchard pest emergence regardless of leap year discrepancies.</p>

<h2>Satellite Orbital Telemetry and TLE Epoch Formats</h2>
<p>In aerospace geodesy and space situational awareness, North American Aerospace Defense Command (NORAD) and NASA publish Two-Line Element sets (TLE) using fractional day-of-the-year notation. For example, epoch <code>26278.41666667</code> denotes the year 2026, day 278, at precisely 10:00:00 UTC. Using ordinal days avoids sexagesimal time conversions and eliminates ambiguity across planetary coordinate reference frames.</p>

<section class="faq-section">
    <h2>Frequently Asked Questions About Day of the Year</h2>
    <div class="faq-item">
        <h3>What is an ISO 8601 Ordinal Date?</h3>
        <p>An ISO 8601 ordinal date consists of a 4-digit calendar year followed by a 3-digit continuous day count, formatted as <code>YYYY-DDD</code> (e.g., <code>2026-001</code> for January 1st, or <code>2026-365</code> for December 31st). It eliminates monthly boundaries for logistics, packaging expiry tracking, and manufacturing lot codes.</p>
    </div>
    <div class="faq-item">
        <h3>How does a leap year change the day of the year?</h3>
        <p>In a leap year, February has 29 days instead of 28. Consequently, all calendar dates from March 1st onward have an ordinal day that is 1 higher than in a common year (e.g., March 1st is Day 60 in a common year, but Day 61 in a leap year).</p>
    </div>
    <div class="faq-item">
        <h3>Why is Day of the Year preferred in solar engineering?</h3>
        <p>Day of the year provides a smooth, monotonically increasing index $N \in [1, 365]$ that feeds directly into trigonometric equations for solar declination, equation of time, solar zenith angles, and atmospheric air mass without complex date-parsing overhead.</p>
    </div>
    <div class="faq-item">
        <h3>What is the difference between Day of the Year and Julian Day?</h3>
        <p>Day of the year (ordinal day) counts days from 1 to 365 (or 366) within a single calendar year. Julian Day Number (JDN) is a continuous astronomical count of elapsed solar days since January 1, 4713 BCE (over 2.46 million days). Though often confused in legacy business programming, they are completely distinct concepts.</p>
    </div>
</section>
"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article)


def main():
    dow_html = gen_day_of_week()
    with open(os.path.join(BASE_DIR, "day-of-week-calculator.html"), "w", encoding="utf-8") as f:
        f.write(dow_html)
    print("Generated day-of-week-calculator.html successfully!")

    doy_html = gen_day_of_year()
    with open(os.path.join(BASE_DIR, "day-of-year-calculator.html"), "w", encoding="utf-8") as f:
        f.write(doy_html)
    print("Generated day-of-year-calculator.html successfully!")

if __name__ == "__main__":
    main()
