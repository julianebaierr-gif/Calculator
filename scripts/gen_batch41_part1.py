# -*- coding: utf-8 -*-
"""
Generator for Batch 41 - Part 1
Tools:
1. time-card-calculator.html (Weekly Timesheet, Daily/Weekly Overtime, FLSA Rounding, Gross Pay)
2. time-duration-calculator.html (Datetime Span, Sexagesimal Arithmetic, ISO 8601 Durations)
3. weeks-between-dates-calculator.html (Full Weeks, Decimal Weeks, Gestational Pregnancy, Sprint Tracking)
4. best-engineering-calculator.html (Hardware & Software Benchmark, NCEES FE/PE Compliance, Casio vs TI vs HP)
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COMMON_TAIL = """    <footer class="site-footer">
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>About CalcHub</h4>
                    <p>CalcHub delivers peer-reviewed chronometric computing algorithms, professional engineering suites, and enterprise financial calendar engines compliant with ISO 8601, NCEES, and FLSA reporting standards.</p>
                </div>
                <div class="footer-col">
                    <h4>Professional Suites</h4>
                    <ul>
                        <li><a href="datetime.html">Date &amp; Time Utilities</a></li>
                        <li><a href="engineering.html">Engineering Tools</a></li>
                        <li><a href="finance.html">Financial Planning</a></li>
                        <li><a href="math.html">Mathematics &amp; Statistics</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Core Calculators</h4>
                    <ul>
                        <li><a href="time-card-calculator.html">Time Card Calculator</a></li>
                        <li><a href="time-duration-calculator.html">Time Duration Calculator</a></li>
                        <li><a href="weeks-between-dates-calculator.html">Weeks Between Dates</a></li>
                        <li><a href="best-engineering-calculator.html">Best Engineering Calculator</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="index.html">All Calculators</a></li>
                        <li><a href="converter.html">Metric Converters</a></li>
                        <li><a href="cable-sizing-guide.html">Cable Sizing Guide</a></li>
                        <li><a href="engineering-formulas.html">Engineering Formulas</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 CalcHub. All rights reserved. Precision engineering, chronometry, and mathematical computational systems.</p>
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
                    <h3>Related Chrono &amp; Payroll Tools</h3>
                    <ul class="sidebar-links">
                        <li><a href="time-card-calculator.html">Time Card Calculator</a></li>
                        <li><a href="time-duration-calculator.html">Time Duration Calculator</a></li>
                        <li><a href="weeks-between-dates-calculator.html">Weeks Between Dates</a></li>
                        <li><a href="hours-calculator.html">Work Hours Calculator</a></li>
                        <li><a href="overtime-calculator.html">Overtime Pay Calculator</a></li>
                        <li><a href="decimal-time-calculator.html">Decimal Time Calculator</a></li>
                        <li><a href="business-days-calculator.html">Business Days Calculator</a></li>
                    </ul>
                </div>
            </aside>
        </div>
    </div>
{COMMON_TAIL}"""


# ===========================================================================
# TOOL 1: time-card-calculator.html
# ===========================================================================
def gen_time_card():
    slug = "time-card-calculator"
    title = "Time Card Calculator | Free Weekly Timesheet Hours & Gross Pay"
    desc = "Free online time card calculator. Enter clock in/out times and lunch breaks for Monday to Sunday. Computes daily hours, weekly overtime, and gross pay."
    h1 = "Time Card Calculator"
    short_desc = "Compute total weekly timesheet hours, unpaid meal break deductions, regular vs. overtime wage allocations, and gross paycheck earnings across all 7 days."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Time Card Calculator",
      "url": "https://calchub.com/time-card-calculator.html",
      "applicationCategory": "FinanceApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Calculates daily and weekly employee time card hours, lunch deductions, overtime, and gross wages."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How does a weekly time card calculator calculate total hours?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "For each workday, it subtracts clock-in time from clock-out time (accounting for shifts that cross midnight), deducts any unpaid meal or break duration in minutes, and converts the net result to decimal hours."
          }
        },
        {
          "@type": "Question",
          "name": "What is the FLSA 15-minute rounding rule for time cards?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Under 29 CFR 785.48, employers can round punches to the nearest 15 minutes using the 7/8 minute rule: punches 1 to 7 minutes past the quarter hour round down, and punches 8 to 14 minutes round up."
          }
        },
        {
          "@type": "Question",
          "name": "How is weekly overtime allocated on a time card?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Under federal FLSA rules, any hours worked beyond 40 hours in a 7-day workweek are classified as overtime and compensated at 1.5 times the standard regular hourly rate."
          }
        },
        {
          "@type": "Question",
          "name": "Do employers have to pay for lunch breaks?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Under federal law, genuine bona fide meal periods lasting 30 minutes or longer where the employee is completely relieved from all work duties are unpaid. Rest breaks lasting 5 to 20 minutes must be counted as paid work time."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-body">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.25rem; margin-bottom: 1.25rem;">
        <div>
            <label for="tcBaseRate" style="font-weight: 600; font-size: 0.875rem;">Hourly Wage Rate ($):</label>
            <input type="number" id="tcBaseRate" class="input-field" value="25.00" min="0" step="0.50">
        </div>
        <div>
            <label for="tcOtThreshold" style="font-weight: 600; font-size: 0.875rem;">Weekly Overtime Threshold:</label>
            <input type="number" id="tcOtThreshold" class="input-field" value="40" min="0" max="60" step="1">
            <span class="input-hint">Standard FLSA threshold is 40 hours/week</span>
        </div>
        <div>
            <label for="tcDailyOt" style="font-weight: 600; font-size: 0.875rem;">Daily Overtime (> 8 hrs):</label>
            <select id="tcDailyOt" class="input-field">
                <option value="no">Weekly Only (> 40 hrs @ 1.5x)</option>
                <option value="yes">Daily (> 8h @ 1.5x, > 12h @ 2.0x)</option>
            </select>
        </div>
    </div>

    <!-- 7-Day Timesheet Table -->
    <div style="overflow-x: auto; margin-bottom: 1.25rem;">
        <table style="width: 100%; border-collapse: collapse; font-size: 0.875rem; background: white; border: 1px solid #cbd5e1; border-radius: 6px;">
            <thead>
                <tr style="background: #f1f5f9; color: #334155; text-align: left;">
                    <th style="padding: 0.6rem; border-bottom: 2px solid #cbd5e1;">Day</th>
                    <th style="padding: 0.6rem; border-bottom: 2px solid #cbd5e1;">Time In</th>
                    <th style="padding: 0.6rem; border-bottom: 2px solid #cbd5e1;">Time Out</th>
                    <th style="padding: 0.6rem; border-bottom: 2px solid #cbd5e1;">Break (mins)</th>
                    <th style="padding: 0.6rem; border-bottom: 2px solid #cbd5e1; text-align: right;">Total Hours</th>
                </tr>
            </thead>
            <tbody id="timesheetBody">
                <!-- Rows injected via script -->
            </tbody>
        </table>
    </div>

    <div style="display: flex; gap: 0.75rem; margin-bottom: 1.5rem;">
        <button type="button" class="btn btn-primary" onclick="calculateTimeCard()">Calculate Paycheck</button>
        <button type="button" class="btn btn-outline" onclick="fillStandardWorkweek()">Fill 9-to-5 Mon-Fri</button>
        <button type="button" class="btn btn-outline" onclick="clearTimesheet()">Clear All</button>
    </div>

    <div class="result-box" style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem;">
        <h3 style="margin-top: 0; color: #1e293b; font-size: 1.1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">Weekly Timesheet &amp; Payroll Summary</h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Total Weekly Hours</div>
                <div id="resTotalHours" style="font-size: 1.5rem; font-weight: 700; color: #2563eb;">40.00 hrs</div>
                <div id="resTotalMins" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">2,400 net minutes</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Regular Wages</div>
                <div id="resRegWages" style="font-size: 1.4rem; font-weight: 700; color: #0f172a;">$1,000.00</div>
                <div id="resRegHours" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">40.00 hrs @ $25.00/hr</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Overtime Wages</div>
                <div id="resOtWages" style="font-size: 1.4rem; font-weight: 700; color: #d97706;">$0.00</div>
                <div id="resOtHours" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">0.00 hrs @ $37.50/hr</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Total Gross Pay</div>
                <div id="resGrossPay" style="font-size: 1.5rem; font-weight: 700; color: #16a34a;">$1,000.00</div>
                <div style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">Pre-tax gross compensation</div>
            </div>
        </div>
    </div>
</div>

<script>
const DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];

function buildTimesheetRows() {
    const tbody = document.getElementById('timesheetBody');
    tbody.innerHTML = '';
    DAYS.forEach((day, idx) => {
        const isWeekday = idx < 5;
        const inVal = isWeekday ? '08:30' : '';
        const outVal = isWeekday ? '17:00' : '';
        const breakVal = isWeekday ? '30' : '0';

        const tr = document.createElement('tr');
        tr.style.borderBottom = '1px solid #e2e8f0';
        tr.innerHTML = `
            <td style="padding: 0.5rem; font-weight: 600;">${day}</td>
            <td style="padding: 0.5rem;"><input type="time" id="in_${idx}" class="input-field" value="${inVal}" style="padding: 0.35rem; font-size: 0.85rem;" onchange="calculateTimeCard()"></td>
            <td style="padding: 0.5rem;"><input type="time" id="out_${idx}" class="input-field" value="${outVal}" style="padding: 0.35rem; font-size: 0.85rem;" onchange="calculateTimeCard()"></td>
            <td style="padding: 0.5rem;"><input type="number" id="brk_${idx}" class="input-field" value="${breakVal}" min="0" max="240" step="5" style="padding: 0.35rem; font-size: 0.85rem; width: 80px;" oninput="calculateTimeCard()"></td>
            <td id="tot_${idx}" style="padding: 0.5rem; text-align: right; font-weight: 700; color: #2563eb;">8.00 hr</td>
        `;
        tbody.appendChild(tr);
    });
}

function fillStandardWorkweek() {
    DAYS.forEach((_, idx) => {
        const isWeekday = idx < 5;
        document.getElementById(`in_${idx}`).value = isWeekday ? '09:00' : '';
        document.getElementById(`out_${idx}`).value = isWeekday ? '17:00' : '';
        document.getElementById(`brk_${idx}`).value = isWeekday ? '30' : '0';
    });
    calculateTimeCard();
}

function clearTimesheet() {
    DAYS.forEach((_, idx) => {
        document.getElementById(`in_${idx}`).value = '';
        document.getElementById(`out_${idx}`).value = '';
        document.getElementById(`brk_${idx}`).value = '0';
    });
    calculateTimeCard();
}

function calculateTimeCard() {
    const rate = parseFloat(document.getElementById('tcBaseRate').value) || 0;
    const otThresh = parseFloat(document.getElementById('tcOtThreshold').value) || 40;
    const dailyOt = document.getElementById('tcDailyOt').value === 'yes';

    let totalWeekMins = 0;
    let totalRegHours = 0;
    let totalOtHours = 0;
    let totalDtHours = 0;

    DAYS.forEach((_, idx) => {
        const inStr = document.getElementById(`in_${idx}`).value;
        const outStr = document.getElementById(`out_${idx}`).value;
        const brkMins = parseFloat(document.getElementById(`brk_${idx}`).value) || 0;

        let dayMins = 0;
        if (inStr && outStr) {
            const [inH, inM] = inStr.split(':').map(Number);
            const [outH, outM] = outStr.split(':').map(Number);
            let start = (inH * 60) + inM;
            let end = (outH * 60) + outM;

            if (end < start) {
                end += 1440; // Midnight rollover
            }
            dayMins = Math.max(0, (end - start) - brkMins);
        }

        const dayHours = dayMins / 60;
        document.getElementById(`tot_${idx}`).innerText = `${dayHours.toFixed(2)} hr`;
        totalWeekMins += dayMins;

        if (dailyOt) {
            if (dayHours <= 8) {
                totalRegHours += dayHours;
            } else if (dayHours <= 12) {
                totalRegHours += 8;
                totalOtHours += (dayHours - 8);
            } else {
                totalRegHours += 8;
                totalOtHours += 4;
                totalDtHours += (dayHours - 12);
            }
        }
    });

    const totalWeekHours = totalWeekMins / 60;

    if (!dailyOt) {
        if (totalWeekHours <= otThresh) {
            totalRegHours = totalWeekHours;
            totalOtHours = 0;
        } else {
            totalRegHours = otThresh;
            totalOtHours = totalWeekHours - otThresh;
        }
        totalDtHours = 0;
    }

    const regWages = totalRegHours * rate;
    const otWages = (totalOtHours * rate * 1.5) + (totalDtHours * rate * 2.0);
    const grossPay = regWages + otWages;

    document.getElementById('resTotalHours').innerText = `${totalWeekHours.toFixed(2)} hrs`;
    document.getElementById('resTotalMins').innerText = `${Math.round(totalWeekMins).toLocaleString()} net minutes`;
    document.getElementById('resRegWages').innerText = `$${regWages.toFixed(2)}`;
    document.getElementById('resRegHours').innerText = `${totalRegHours.toFixed(2)} hrs @ $${rate.toFixed(2)}/hr`;
    document.getElementById('resOtWages').innerText = `$${otWages.toFixed(2)}`;
    document.getElementById('resOtHours').innerText = `${(totalOtHours + totalDtHours).toFixed(2)} hrs @ 1.5x/2.0x`;
    document.getElementById('resGrossPay').innerText = `$${grossPay.toFixed(2)}`;
}

window.addEventListener('DOMContentLoaded', () => {
    buildTimesheetRows();
    document.getElementById('tcBaseRate').addEventListener('input', calculateTimeCard);
    document.getElementById('tcOtThreshold').addEventListener('input', calculateTimeCard);
    document.getElementById('tcDailyOt').addEventListener('change', calculateTimeCard);
    calculateTimeCard();
});
</script>"""

    article = """<h2>Mathematical and Statutory Structure of Timesheet Calculations</h2>
<p>Modern payroll administration relies on structured employee time recording systems, colloquially designated as <strong>time cards</strong> or <strong>timesheets</strong>. In hourly employment arrangements, gross compensation $W_{\text{gross}}$ is governed by accurate temporal summation across discrete shifts, rigorous deduction of statutory unpaid meal breaks, and algorithmic partitioning between straight-time regular hours and overtime premium hours.</p>

<p>For each diurnal shift $i \in \{1, 2, \dots, 7\}$ spanning a standard seven-day payroll workweek, total elapsed duration in net minutes $T_{\text{net}, i}$ is evaluated as:</p>

$$T_{\text{net}, i} = (t_{\text{out}, i} - t_{\text{in}, i}) - B_{\text{unpaid}, i}$$

<p>Where $t_{\text{in}, i}$ and $t_{\text{out}, i}$ represent timestamps expressed in minutes from midnight ($0 \le t \le 1440$). When a night shift crosses the midnight threshold ($t_{\text{out}, i} < t_{\text{in}, i}$), modular diurnal transformation adds $1,440 \text{ minutes}$ ($24 \text{ hours}$) to the terminal punch:</p>

$$t_{\text{out}, i} = t_{\text{out}, i} + 1440$$

<p>Total workweek duration in fractional decimal hours $H_{\text{total}}$ is then evaluated via rational division by 60:</p>

$$H_{\text{total}} = \frac{1}{60} \sum_{i=1}^{7} T_{\text{net}, i}$$

<h2>The FLSA 7/8-Minute Rounding Rule (29 CFR § 785.48)</h2>
<p>Under Title 29, Section 785.48(b) of the United States Code of Federal Regulations, employers are legally authorized to record employee starting and stopping times to the nearest quarter of an hour (15 minutes). The statute establishes the celebrated <strong>7/8-minute rounding window</strong>:</p>

<ul>
    <li><strong>Down-Rounding (Minutes 1 through 7):</strong> If an employee clocks in 1 to 7 minutes past a quarter-hour mark (e.g., 08:07), the punch rounds down to the preceding quarter hour (08:00).</li>
    <li><strong>Up-Rounding (Minutes 8 through 14):</strong> If an employee clocks in 8 to 14 minutes past a quarter-hour mark (e.g., 08:08), the punch rounds forward to the subsequent quarter hour (08:15).</li>
    <li><strong>Regulatory Neutrality Requirement:</strong> Federal courts strictly enforce that time clock rounding must operate neutrally over time. An employer cannot program an automated system to round down on clock-ins and round down on clock-outs, as this systematically deprives employees of lawfully earned compensation.</li>
</ul>

<h3>Sexagesimal to Decimal Minutes Reference Matrix</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Recorded Minutes</th>
            <th>Fractional Ratio</th>
            <th>Decimal Hours</th>
            <th>FLSA 15-Minute Rounding</th>
            <th>Tenth-Hour (6-Minute) Rounding</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>01 – 07 mins</td><td>x / 60</td><td>0.02 – 0.12 hr</td><td>0.00 hr (Round Down)</td><td>Nearest 0.10 hr</td></tr>
        <tr><td>08 – 14 mins</td><td>x / 60</td><td>0.13 – 0.23 hr</td><td>0.25 hr (Round Up)</td><td>Nearest 0.20 hr</td></tr>
        <tr><td>15 mins</td><td>15 / 60</td><td>0.250 hr</td><td>0.25 hr (Exact)</td><td>0.20 or 0.30 hr</td></tr>
        <tr><td>16 – 22 mins</td><td>x / 60</td><td>0.27 – 0.37 hr</td><td>0.25 hr (Round Down)</td><td>Nearest 0.30 hr</td></tr>
        <tr><td>23 – 29 mins</td><td>x / 60</td><td>0.38 – 0.48 hr</td><td>0.50 hr (Round Up)</td><td>Nearest 0.40 hr</td></tr>
        <tr><td>30 mins</td><td>30 / 60</td><td>0.500 hr</td><td>0.50 hr (Exact)</td><td>0.50 hr (Exact)</td></tr>
        <tr><td>38 – 44 mins</td><td>x / 60</td><td>0.63 – 0.73 hr</td><td>0.75 hr (Round Up)</td><td>Nearest 0.70 hr</td></tr>
        <tr><td>45 mins</td><td>45 / 60</td><td>0.750 hr</td><td>0.75 hr (Exact)</td><td>0.70 or 0.80 hr</td></tr>
        <tr><td>53 – 59 mins</td><td>x / 60</td><td>0.88 – 0.98 hr</td><td>1.00 hr (Round Up)</td><td>Nearest 1.00 hr</td></tr>
    </tbody>
</table>

<h2>Overtime Allocation: Federal FLSA vs. California Daily Rules</h2>
<p>Gross compensation is partitioned into regular and overtime tiers according to jurisdiction:</p>

<h3>1. Standard Federal FLSA Weekly Model</h3>
<p>Under federal guidelines, overtime applies strictly to weekly totals exceeding 40.0 hours ($H_{\text{ot\_thresh}} = 40$):</p>

$$H_{\text{reg}} = \min(H_{\text{total}}, 40)$$
$$H_{\text{ot}} = \max(0, H_{\text{total}} - 40)$$
$$W_{\text{gross}} = (H_{\text{reg}} \times R_{\text{base}}) + (H_{\text{ot}} \times 1.5 \times R_{\text{base}})$$

<h3>2. California Daily Overtime and Double-Time Model (Labor Code § 510)</h3>
<p>Under California statutory rules, hours are evaluated on each individual day:</p>
<ul>
    <li>Daily hours $\le 8.0$: Paid at straight base rate $R_{\text{base}}$.</li>
    <li>Daily hours $> 8.0$ up to $12.0$: Paid at $1.5 \times R_{\text{base}}$ (Time-and-a-half).</li>
    <li>Daily hours $> 12.0$: Paid at $2.0 \times R_{\text{base}}$ (Double time).</li>
    <li>7th Consecutive Day: First 8 hours at $1.5\times$; all hours $> 8$ at $2.0\times$.</li>
</ul>

<div class="worked-example-card">
    <h3>Worked Corporate Payroll Case Study: Warehouse Operations Shift Card</h3>
    <p><strong>Scenario:</strong> A logistics specialist works five shifts during a holiday peak week: Monday (08:00 to 17:30, 30-min break), Tuesday (08:00 to 18:30, 45-min break), Wednesday (07:30 to 16:30, 30-min break), Thursday (08:00 to 19:00, 60-min break), and Friday (08:00 to 17:00, 30-min break). Base wage is $26.00/hour. Compute: (1) daily net hours, (2) weekly total hours, (3) regular vs. overtime hours, and (4) gross earnings under federal FLSA rules.</p>
    
    <div class="step-solution">
        <h4>Step 1: Compute Daily Net Hours</h4>
        <p>Monday: $9.5\text{h gross} - 0.5\text{h break} = 9.00 \text{ hours}$.</p>
        <p>Tuesday: $10.5\text{h gross} - 0.75\text{h break} = 9.75 \text{ hours}$.</p>
        <p>Wednesday: $9.0\text{h gross} - 0.5\text{h break} = 8.50 \text{ hours}$.</p>
        <p>Thursday: $11.0\text{h gross} - 1.0\text{h break} = 10.00 \text{ hours}$.</p>
        <p>Friday: $9.0\text{h gross} - 0.5\text{h break} = 8.50 \text{ hours}$.</p>

        <h4>Step 2: Sum Total Weekly Hours</h4>
        $$H_{\text{total}} = 9.00 + 9.75 + 8.50 + 10.00 + 8.50 = 45.75 \text{ hours}$$

        <h4>Step 3: Partition Regular and Overtime Hours</h4>
        $$H_{\text{reg}} = 40.00 \text{ hours}$$
        $$H_{\text{ot}} = 45.75 - 40.00 = 5.75 \text{ overtime hours}$$

        <h4>Step 4: Compute Gross Compensation</h4>
        $$\text{Regular Pay} = 40.00 \times \$26.00 = \$1,040.00$$
        $$\text{Overtime Pay} = 5.75 \times (\$26.00 \times 1.5) = 5.75 \times \$39.00 = \$224.25$$
        $$\text{Total Gross Pay} = \$1,040.00 + \$224.25 = \$1,264.25$$
    </div>
</div>

<h2>Common Calculation Errors in Time Card Management</h2>
<ol>
    <li><strong>Failing to Deduct Unpaid Breaks:</strong> Gross clock spans must have unpaid meal periods subtracted before converting to decimal pay hours. Including lunch periods inflates labor costs unlawfully.</li>
    <li><strong>Decimal Time Truncation:</strong> Truncating minutes prematurely (e.g., treating 45 minutes as 0.45 hours instead of 0.75 hours) shorts employees by 18 minutes of wages per shift.</li>
    <li><strong>Midnight Crossing Sign Errors:</strong> When an employee works an overnight shift (e.g., 22:00 to 06:00), subtracting $6 - 22$ yields $-16$. Software engines must add 24 hours to obtain the true 8-hour shift duration.</li>
</ol>

<section class="faq-section">
    <h2>Frequently Asked Questions About Time Cards</h2>
    <div class="faq-item">
        <h3>How does a weekly time card calculator calculate total hours?</h3>
        <p>For each workday, it subtracts clock-in time from clock-out time (accounting for shifts that cross midnight), deducts any unpaid meal or break duration in minutes, and converts the net result to decimal hours.</p>
    </div>
    <div class="faq-item">
        <h3>What is the FLSA 15-minute rounding rule for time cards?</h3>
        <p>Under 29 CFR 785.48, employers can round punches to the nearest 15 minutes using the 7/8 minute rule: punches 1 to 7 minutes past the quarter hour round down, and punches 8 to 14 minutes round up.</p>
    </div>
    <div class="faq-item">
        <h3>How is weekly overtime allocated on a time card?</h3>
        <p>Under federal FLSA rules, any hours worked beyond 40 hours in a 7-day workweek are classified as overtime and compensated at 1.5 times the standard regular hourly rate.</p>
    </div>
    <div class="faq-item">
        <h3>Do employers have to pay for lunch breaks?</h3>
        <p>Under federal law, genuine bona fide meal periods lasting 30 minutes or longer where the employee is completely relieved from all work duties are unpaid. Rest breaks lasting 5 to 20 minutes must be counted as paid work time.</p>
    </div>
</section>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article, category_hub="finance.html", category_name="Finance &amp; Payroll")


# ===========================================================================
# TOOL 2: time-duration-calculator.html
# ===========================================================================
def gen_time_duration():
    slug = "time-duration-calculator"
    title = "Time Duration Calculator | Calculate Hours, Minutes & Seconds Between Times"
    desc = "Calculate the exact duration and time span between two dates and times. Computes elapsed hours, minutes, seconds, decimal hours, and ISO 8601 duration strings."
    h1 = "Time Duration Calculator"
    short_desc = "Compute the exact chronological time span between start and end date-times, with multi-unit breakdown in seconds, minutes, decimal hours, and ISO 8601 format."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Time Duration Calculator",
      "url": "https://calchub.com/time-duration-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Calculates the exact elapsed duration between two date-time timestamps in hours, minutes, seconds, and ISO 8601 notation."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How is time duration calculated across days?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The start and end date-times are converted to millisecond epoch timestamps, the difference is calculated, and then decomposed into integer days, hours, minutes, and seconds."
          }
        },
        {
          "@type": "Question",
          "name": "What is an ISO 8601 duration format?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "An ISO 8601 duration begins with P (for period), followed by date components (Y, M, W, D), then T (for time), followed by time components (H, M, S). For example, P2DT4H30M represents 2 days, 4 hours, and 30 minutes."
          }
        },
        {
          "@type": "Question",
          "name": "How does Daylight Saving Time affect duration calculations?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Standard wall-clock timestamps can gain or lose 1 hour during spring and autumn transitions. High-precision duration systems convert timestamps to UTC first to measure physical elapsed time."
          }
        },
        {
          "@type": "Question",
          "name": "What is the difference between time duration and time difference?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Time duration measures elapsed physical time between two specific chronological events, whereas time difference often refers to timezone offsets between two geographic locations."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-body">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.25rem; margin-bottom: 1.5rem;">
        <div>
            <label for="startDateTime" style="font-weight: 600; font-size: 0.875rem;">Start Date &amp; Time:</label>
            <input type="datetime-local" id="startDateTime" class="input-field" value="2026-10-01T08:00">
        </div>
        <div>
            <label for="endDateTime" style="font-weight: 600; font-size: 0.875rem;">End Date &amp; Time:</label>
            <input type="datetime-local" id="endDateTime" class="input-field" value="2026-10-05T17:30">
        </div>
    </div>

    <div style="display: flex; gap: 0.75rem; margin-bottom: 1.5rem;">
        <button type="button" class="btn btn-primary" onclick="calculateDuration()">Calculate Duration</button>
        <button type="button" class="btn btn-outline" onclick="setDurationPreset('24h')">+24 Hours</button>
        <button type="button" class="btn btn-outline" onclick="setDurationPreset('1w')">+1 Week</button>
    </div>

    <div class="result-box" style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem;">
        <h3 style="margin-top: 0; color: #1e293b; font-size: 1.1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">Chronological Elapsed Span</h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Formatted Span</div>
                <div id="resFormattedSpan" style="font-size: 1.4rem; font-weight: 700; color: #2563eb;">4d 9h 30m</div>
                <div id="resIsoDuration" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">ISO: P4DT9H30M</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Total Decimal Hours</div>
                <div id="resDecimalHours" style="font-size: 1.4rem; font-weight: 700; color: #0f172a;">105.50 hr</div>
                <div id="resTotalMinutes" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">6,330 minutes</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Total Seconds (SI)</div>
                <div id="resTotalSeconds" style="font-size: 1.4rem; font-weight: 700; color: #059669;">379,800 s</div>
                <div id="resMillis" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">379,800,000 ms</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Days &amp; Fraction</div>
                <div id="resFractionDays" style="font-size: 1.4rem; font-weight: 700; color: #7c3aed;">4.3958 Days</div>
                <div id="resFractionWeeks" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">0.628 weeks</div>
            </div>
        </div>
    </div>
</div>

<script>
function setDurationPreset(type) {
    const sEl = document.getElementById('startDateTime');
    const eEl = document.getElementById('endDateTime');
    const start = new Date(sEl.value || new Date());
    let end = new Date(start);

    if (type === '24h') {
        end.setHours(end.getHours() + 24);
    } else if (type === '1w') {
        end.setDate(end.getDate() + 7);
    }

    const pad = (n) => String(n).padStart(2, '0');
    const toLocalISO = (d) => `${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())}T${pad(d.getHours())}:${pad(d.getMinutes())}`;
    eEl.value = toLocalISO(end);
    calculateDuration();
}

function calculateDuration() {
    const sStr = document.getElementById('startDateTime').value;
    const eStr = document.getElementById('endDateTime').value;
    if (!sStr || !eStr) return;

    let d1 = new Date(sStr);
    let d2 = new Date(eStr);

    let isNeg = false;
    if (d2 < d1) {
        const tmp = d1;
        d1 = d2;
        d2 = tmp;
        isNeg = true;
    }

    const diffMs = d2 - d1;
    const totalSec = Math.floor(diffMs / 1000);
    const totalMin = Math.floor(totalSec / 60);
    const totalHours = totalSec / 3600;
    const totalDays = totalSec / 86400;

    const days = Math.floor(totalSec / 86400);
    const remSec1 = totalSec % 86400;
    const hours = Math.floor(remSec1 / 3600);
    const remSec2 = remSec1 % 3600;
    const mins = Math.floor(remSec2 / 60);
    const secs = remSec2 % 60;

    const prefix = isNeg ? "-" : "";
    document.getElementById('resFormattedSpan').innerText = `${prefix}${days}d ${hours}h ${mins}m ${secs}s`;
    document.getElementById('resIsoDuration').innerText = `ISO: ${prefix}P${days}DT${hours}H${mins}M${secs}S`;
    document.getElementById('resDecimalHours').innerText = `${prefix}${totalHours.toFixed(2)} hr`;
    document.getElementById('resTotalMinutes').innerText = `${prefix}${totalMin.toLocaleString()} minutes`;
    document.getElementById('resTotalSeconds').innerText = `${prefix}${totalSec.toLocaleString()} s`;
    document.getElementById('resMillis').innerText = `${prefix}${diffMs.toLocaleString()} ms`;
    document.getElementById('resFractionDays').innerText = `${prefix}${totalDays.toFixed(4)} Days`;
    document.getElementById('resFractionWeeks').innerText = `${prefix}${(totalDays / 7).toFixed(3)} weeks`;
}

window.addEventListener('DOMContentLoaded', () => {
    document.getElementById('startDateTime').addEventListener('change', calculateDuration);
    document.getElementById('endDateTime').addEventListener('change', calculateDuration);
    calculateDuration();
});
</script>"""

    article = """<h2>Mathematical Principles of Continuous Time Duration</h2>
<p>In physical kinematics, chronobiology, space geodesy, and computer networking, measuring the exact <strong>duration</strong> elapsed between two chronological events requires continuous interval arithmetic. While discrete dates follow discontinuous calendar partitions (varying month lengths, leap years), duration is an invariant physical scalar measured in the SI base unit of seconds ($s$).</p>

<p>Given an initial timestamp $t_{\text{start}}$ and a terminal timestamp $t_{\text{end}}$, the fundamental elapsed duration $\Delta t$ is evaluated from their UNIX epoch representations (milliseconds elapsed since January 1, 1970 00:00:00 UTC):</p>

$$\Delta t_{\text{sec}} = \frac{\tau_{\text{end}} - \tau_{\text{start}}}{1000}$$

<p>Decomposing continuous seconds $\Delta t_{\text{sec}}$ into hierarchical sexagesimal components—days $D$, hours $H$, minutes $M$, and seconds $S$—is governed by successive modulo and floor operators:</p>

$$D = \left\lfloor \frac{\Delta t_{\text{sec}}}{86400} \right\rfloor$$
$$H = \left\lfloor \frac{\Delta t_{\text{sec}} \bmod 86400}{3600} \right\rfloor$$
$$M = \left\lfloor \frac{\Delta t_{\text{sec}} \bmod 3600}{60} \right\rfloor$$
$$S = \Delta t_{\text{sec}} \bmod 60$$

<h2>The ISO 8601 Duration Standard Representation</h2>
<p>International standard <strong>ISO 8601-1:2019</strong> specifies an unambiguous syntax for exchanging duration metadata across enterprise computer software, distributed APIs, and database schemas. An ISO 8601 duration string follows the canonical format:</p>

$$\text{P}[n]\text{Y}[n]\text{M}[n]\text{D}\text{T}[n]\text{H}[n]\text{M}[n]\text{S}$$

<p>Where the structural tokens denote:</p>
<ul>
    <li><strong><code>P</code> (Period Designator):</strong> Placed at the very start of the duration representation.</li>
    <li><strong><code>Y</code>, <code>M</code>, <code>W</code>, <code>D</code>:</strong> Represent years, months, weeks, and days respectively.</li>
    <li><strong><code>T</code> (Time Separator):</strong> Must precede all time elements (hours, minutes, seconds).</li>
    <li><strong><code>H</code>, <code>M</code>, <code>S</code>:</strong> Represent hours, minutes, and seconds respectively.</li>
</ul>
<p>For example, a mission elapsed span of 4 days, 9 hours, 30 minutes, and 15 seconds is unambiguously formatted as <code>P4DT9H30M15S</code>.</p>

<h3>Chronometric Units and Conversion Factors Matrix</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Time Duration Unit</th>
            <th>SI Base Seconds ($s$)</th>
            <th>Minutes</th>
            <th>Decimal Hours</th>
            <th>Solar Days</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>1 Millisecond (ms)</td><td>$10^{-3} \text{ s}$</td><td>$1.667 \times 10^{-5}$</td><td>$2.778 \times 10^{-7}$</td><td>$1.157 \times 10^{-8}$</td></tr>
        <tr><td>1 Second (s)</td><td>$1.0 \text{ s}$</td><td>$0.01667 \text{ min}$</td><td>$0.000278 \text{ hr}$</td><td>$1.157 \times 10^{-5}$</td></tr>
        <tr><td>1 Minute (min)</td><td>$60.0 \text{ s}$</td><td>$1.0 \text{ min}$</td><td>$0.01667 \text{ hr}$</td><td>$0.000694 \text{ d}$</td></tr>
        <tr><td>1 Hour (hr)</td><td>$3,600 \text{ s}$</td><td>$60.0 \text{ min}$</td><td>$1.0 \text{ hr}$</td><td>$0.04167 \text{ d}$</td></tr>
        <tr><td>1 Mean Solar Day (d)</td><td>$86,400 \text{ s}$</td><td>$1,440 \text{ min}$</td><td>$24.0 \text{ hr}$</td><td>$1.0000 \text{ d}$</td></tr>
        <tr><td>1 Standard Week (wk)</td><td>$604,800 \text{ s}$</td><td>$10,080 \text{ min}$</td><td>$168.0 \text{ hr}$</td><td>$7.0000 \text{ d}$</td></tr>
        <tr><td>1 Julian Year ($a$)</td><td>$31,557,600 \text{ s}$</td><td>$525,960 \text{ min}$</td><td>$8,766.0 \text{ hr}$</td><td>$365.25 \text{ d}$</td></tr>
    </tbody>
</table>

<h2>Network Telemetry and Distributed Systems Clock Synchronization</h2>
<p>In cloud computing, high-frequency financial trading, and distributed database consensus (such as Google Spanner's TrueTime API), duration measurements face relativistic and network latency challenges. Network Time Protocol (NTP) and Precision Time Protocol (IEEE 1588 PTP) synchronize atomic clocks across global data centers.</p>
<p>When measuring durations across servers, engineers utilize <strong>monotonic clock timers</strong> (e.g., <code>clock_gettime(CLOCK_MONOTONIC)</code> in Linux) rather than wall-clock real time (<code>CLOCK_REALTIME</code>). Monotonic clocks never jump backward due to NTP slew adjustments or leap second insertions, guaranteeing mathematically positive duration evaluations.</p>

<div class="worked-example-card">
    <h3>Worked Engineering Case Study: Aerospace Satellite Tracking Pass Duration</h3>
    <p><strong>Scenario:</strong> A Low Earth Orbit (LEO) earth observation satellite enters ground station acquisition of signal (AOS) on <strong>October 5, 2026 at 04:12:35 UTC</strong> and loses signal (LOS) on <strong>October 5, 2026 at 04:26:50 UTC</strong>. Calculate: (1) exact pass duration in sexagesimal notation, (2) total seconds, (3) decimal hours, and (4) data transmitted if telemetry downlink operates at 850 Mbps.</p>
    
    <div class="step-solution">
        <h4>Step 1: Compute Sexagesimal Duration</h4>
        <p>Start: $04:12:35 = (4 \times 3600) + (12 \times 60) + 35 = 14,400 + 720 + 35 = 15,155 \text{ seconds}$.</p>
        <p>End: $04:26:50 = (4 \times 3600) + (26 \times 60) + 50 = 14,400 + 1560 + 50 = 16,010 \text{ seconds}$.</p>
        $$\Delta t_{\text{sec}} = 16,010 - 15,155 = 855 \text{ seconds}$$
        <p>Partitioning into minutes and seconds:</p>
        $$\text{Minutes} = \lfloor 855 / 60 \rfloor = 14 \text{ minutes}$$
        $$\text{Seconds} = 855 \bmod 60 = 15 \text{ seconds}$$
        <p><strong>Pass Span:</strong> <code>0h 14m 15s</code> (ISO: <code>PT14M15S</code>).</p>

        <h4>Step 2: Convert to Decimal Hours</h4>
        $$\Delta t_{\text{decimal}} = \frac{855}{3600} = 0.2375 \text{ hours}$$

        <h4>Step 3: Calculate Telemetry Downlink Volume</h4>
        $$\text{Total Bits} = 855 \text{ seconds} \times 850 \times 10^6 \text{ bps} = 7.2675 \times 10^{11} \text{ bits}$$
        $$\text{Total Gigabytes} = \frac{7.2675 \times 10^{11}}{8 \times 10^9} \approx 90.84 \text{ GB}$$
    </div>
</div>

<h2>Common Implementation Pitfalls with Duration Calculations</h2>
<ol>
    <li><strong>Daylight Saving Time (DST) Jumps:</strong> Calculating duration between local wall-clock times across the spring transition (e.g., 01:30 to 03:30) appears to span 2 hours, but physically only 1 hour elapsed because clocks jumped forward at 02:00. Always compute durations using UTC epoch timestamps.</li>
    <li><strong>Leap Second Distortions:</strong> While civil time occasionally inserts a 61st second (23:59:60 UTC) to match Earth's slowing rotation, POSIX standards ignore leap seconds, causing a 1-second discrepancy against International Atomic Time (TAI).</li>
    <li><strong>Floating Point Inaccuracies in Millisecond Conversions:</strong> Dividing large epoch millisecond timestamps directly in 32-bit floating point induces truncation errors. Systems must retain 64-bit double precision integers.</li>
</ol>


<h2>Specialized Applications: Athletic Chronometry and High-Precision Lap Splits</h2>
<p>In Olympic track and field, motorsport telemetry (Formula 1, NASCAR), and competitive swimming, time duration calculations require sub-second millisecond resolution governed by international governing bodies (World Athletics, FIA, World Aquatics). At velocities exceeding 300 km/h in Formula 1 racing, an interval of just 0.001 seconds (1 millisecond) represents approximately 8.33 centimeters of physical track displacement. Chronometric timing systems employ transponder loops embedded in the circuit asphalt that generate differential time splits:</p>

$$\Delta t_{	ext{split}} = t_{	ext{sector, } k} - t_{	ext{sector, } k-1}$$

<p>Accumulating lap sectors into total race duration requires high-precision sexagesimal floating-point addition that prevents IEEE 754 binary floating-point roundoff drift over multi-hour endurance events like the 24 Hours of Le Mans.</p>

<h2>Relational Databases and SQL Temporal Duration Modeling</h2>
<p>In enterprise software architecture and data warehousing (PostgreSQL, Oracle, Snowflake, MySQL), durations are stored using specialized temporal data types such as SQL standard <code>INTERVAL DAY TO SECOND</code>. Evaluating differences between timestamps utilizes statutory SQL functions:</p>
<pre><code>-- PostgreSQL exact duration extraction
SELECT AGE(end_timestamp, start_timestamp) AS calendar_span,
       EXTRACT(EPOCH FROM (end_timestamp - start_timestamp)) AS elapsed_seconds;
</code></pre>
<p>Engineers must exercise care when querying durations across Daylight Saving Time adjustments: calculating duration from naive local timestamp columns without timezone offsets (<code>TIMESTAMP WITHOUT TIME ZONE</code>) introduces a 1-hour discrepancy twice annually during clock transitions.</p>
<section class="faq-section">
    <h2>Frequently Asked Questions About Time Duration</h2>
    <div class="faq-item">
        <h3>How is time duration calculated across days?</h3>
        <p>The start and end date-times are converted to millisecond epoch timestamps, the difference is calculated, and then decomposed into integer days, hours, minutes, and seconds.</p>
    </div>
    <div class="faq-item">
        <h3>What is an ISO 8601 duration format?</h3>
        <p>An ISO 8601 duration begins with P (for period), followed by date components (Y, M, W, D), then T (for time), followed by time components (H, M, S). For example, P2DT4H30M represents 2 days, 4 hours, and 30 minutes.</p>
    </div>
    <div class="faq-item">
        <h3>How does Daylight Saving Time affect duration calculations?</h3>
        <p>Standard wall-clock timestamps can gain or lose 1 hour during spring and autumn transitions. High-precision duration systems convert timestamps to UTC first to measure physical elapsed time.</p>
    </div>
    <div class="faq-item">
        <h3>What is the difference between time duration and time difference?</h3>
        <p>Time duration measures elapsed physical time between two specific chronological events, whereas time difference often refers to timezone offsets between two geographic locations.</p>
    </div>
</section>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article)


# ===========================================================================
# TOOL 3: weeks-between-dates-calculator.html
# ===========================================================================
def gen_weeks_between_dates():
    slug = "weeks-between-dates-calculator"
    title = "Weeks Between Dates Calculator | Full Weeks, Days & Gestation Progress"
    desc = "Calculate the exact number of weeks and days between two dates. Computes full weeks, decimal weeks, percentage of year, and clinical obstetric gestation age."
    h1 = "Weeks Between Dates Calculator"
    short_desc = "Compute the exact number of calendar weeks and leftover days between two dates, including fractional decimal weeks, agile sprint intervals, and gestation tracking."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Weeks Between Dates Calculator",
      "url": "https://calchub.com/weeks-between-dates-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Calculates the number of whole weeks and residual days between any two calendar dates."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How do you calculate weeks and days between two dates?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Find the total number of days between the two dates, divide by 7 to get whole completed weeks, and the remainder gives the residual leftover days."
          }
        },
        {
          "@type": "Question",
          "name": "How many weeks are in a standard calendar year?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A common year has 365 days, which equals 52 weeks and 1 day (52.143 weeks). A leap year has 366 days, which equals 52 weeks and 2 days (52.286 weeks)."
          }
        },
        {
          "@type": "Question",
          "name": "How do obstetricians calculate pregnancy gestation weeks?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Obstetricians measure gestational age from the first day of the last menstrual period (LMP) in completed weeks and days (e.g. 24 weeks and 3 days), with full term defined at 40 weeks."
          }
        },
        {
          "@type": "Question",
          "name": "How many two-week Agile sprints fit in a calendar quarter?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A standard quarter has 13 weeks (91 days), which comfortably accommodates 6 two-week development sprints (12 weeks) plus 1 buffer/hardening week."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-body">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.25rem; margin-bottom: 1.5rem;">
        <div>
            <label for="wksStartDate" style="font-weight: 600; font-size: 0.875rem;">Start Date:</label>
            <input type="date" id="wksStartDate" class="input-field" value="2026-01-01">
        </div>
        <div>
            <label for="wksEndDate" style="font-weight: 600; font-size: 0.875rem;">End Date:</label>
            <input type="date" id="wksEndDate" class="input-field" value="2026-10-05">
        </div>
    </div>

    <div style="display: flex; gap: 0.75rem; margin-bottom: 1.5rem;">
        <button type="button" class="btn btn-primary" onclick="calculateWeeksBetween()">Calculate Weeks</button>
        <button type="button" class="btn btn-outline" onclick="setWeeksPreset('12w')">12-Week Goal</button>
        <button type="button" class="btn btn-outline" onclick="setWeeksPreset('gest')">40-Week Gestation</button>
    </div>

    <div class="result-box" style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem;">
        <h3 style="margin-top: 0; color: #1e293b; font-size: 1.1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">Elapsed Weeks Breakdown</h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Whole Weeks &amp; Days</div>
                <div id="resWholeWeeks" style="font-size: 1.4rem; font-weight: 700; color: #2563eb;">39 Wks, 4 Days</div>
                <div id="resDecimalWeeks" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">39.571 decimal weeks</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Total Calendar Days</div>
                <div id="resTotalDays" style="font-size: 1.4rem; font-weight: 700; color: #0f172a;">277 Days</div>
                <div id="resWorkDays" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">Approx 198 workdays</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Agile 2-Week Sprints</div>
                <div id="resAgileSprints" style="font-size: 1.4rem; font-weight: 700; color: #059669;">19.8 Sprints</div>
                <div style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">Standard 10-day sprints</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Annual Percentage</div>
                <div id="resYearPct" style="font-size: 1.4rem; font-weight: 700; color: #7c3aed;">75.89%</div>
                <div style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">Of 52.14-week year</div>
            </div>
        </div>
    </div>
</div>

<script>
function setWeeksPreset(type) {
    const today = new Date();
    const pad = (n) => String(n).padStart(2, '0');
    const toYMD = (d) => `${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())}`;

    document.getElementById('wksStartDate').value = toYMD(today);
    let end = new Date(today);

    if (type === '12w') {
        end.setDate(end.getDate() + (12 * 7));
    } else if (type === 'gest') {
        end.setDate(end.getDate() + (40 * 7));
    }
    document.getElementById('wksEndDate').value = toYMD(end);
    calculateWeeksBetween();
}

function calculateWeeksBetween() {
    const sStr = document.getElementById('wksStartDate').value;
    const eStr = document.getElementById('wksEndDate').value;
    if (!sStr || !eStr) return;

    let d1 = new Date(sStr + 'T00:00:00');
    let d2 = new Date(eStr + 'T00:00:00');

    let isNeg = false;
    if (d2 < d1) {
        const tmp = d1;
        d1 = d2;
        d2 = tmp;
        isNeg = true;
    }

    const diffMs = d2 - d1;
    const totalDays = Math.round(diffMs / (1000 * 60 * 60 * 24));
    const wholeWeeks = Math.floor(totalDays / 7);
    const remDays = totalDays % 7;
    const decWeeks = totalDays / 7;
    const sprints = (decWeeks / 2).toFixed(1);
    const yrPct = ((totalDays / 365) * 100).toFixed(2);
    const workDays = Math.round(totalDays * (5 / 7));

    const prefix = isNeg ? "-" : "";
    document.getElementById('resWholeWeeks').innerText = `${prefix}${wholeWeeks} Wks, ${remDays} Days`;
    document.getElementById('resDecimalWeeks').innerText = `${prefix}${decWeeks.toFixed(3)} decimal weeks`;
    document.getElementById('resTotalDays').innerText = `${prefix}${totalDays.toLocaleString()} Days`;
    document.getElementById('resWorkDays').innerText = `Approx ${prefix}${workDays} working days`;
    document.getElementById('resAgileSprints').innerText = `${prefix}${sprints} Sprints`;
    document.getElementById('resYearPct').innerText = `${yrPct}%`;
}

window.addEventListener('DOMContentLoaded', () => {
    document.getElementById('wksStartDate').addEventListener('change', calculateWeeksBetween);
    document.getElementById('wksEndDate').addEventListener('change', calculateWeeksBetween);
    calculateWeeksBetween();
});
</script>"""

    article = """<h2>Mathematical Formulation of Week Intervals</h2>
<p>In project scheduling, clinical medicine, educational semesters, and sprint planning, time is predominantly quantified in discrete units of <strong>weeks</strong> ($7 \text{ solar days}$). Unlike months, which fluctuate between 28 and 31 days, a week is an invariant seven-day continuum containing exactly:</p>

$$1 \text{ Week} = 7 \text{ days} = 168 \text{ hours} = 10,080 \text{ minutes} = 604,800 \text{ seconds}$$

<p>Given any two calendar dates $D_1$ and $D_2$, the exact number of completed whole weeks $W_{\text{whole}}$ and remaining residual days $D_{\text{residual}}$ is evaluated via integer floor division and modulo arithmetic:</p>

$$\Delta D_{\text{total}} = |D_2 - D_1|$$
$$W_{\text{whole}} = \left\lfloor \frac{\Delta D_{\text{total}}}{7} \right\rfloor$$
$$D_{\text{residual}} = \Delta D_{\text{total}} \bmod 7$$

<p>The continuous fractional decimal week value $W_{\text{decimal}}$ evaluates as:</p>

$$W_{\text{decimal}} = \frac{\Delta D_{\text{total}}}{7} = W_{\text{whole}} + \frac{D_{\text{residual}}}{7}$$

<h2>Clinical Obstetric Gestational Age (ACOG Protocol)</h2>
<p>In obstetrics and gynecology, fetal development is measured strictly in <strong>completed gestational weeks and days</strong> calculated from the first day of the patient's Last Menstrual Period (LMP). Under American College of Obstetricians and Gynecologists (ACOG) Committee Opinion No. 700:</p>

<ul>
    <li><strong>Estimated Date of Delivery (EDD):</strong> Evaluated at exactly 40 weeks and 0 days ($280 \text{ days}$) from LMP.</li>
    <li><strong>First Trimester:</strong> $0\text{w } 0\text{d}$ through $13\text{w } 6\text{d}$.</li>
    <li><strong>Second Trimester:</strong> $14\text{w } 0\text{d}$ through $27\text{w } 6\text{d}$.</li>
    <li><strong>Third Trimester:</strong> $28\text{w } 0\text{d}$ through birth.</li>
    <li><strong>Full Term Window:</strong> Spans between $39\text{w } 0\text{d}$ and $40\text{w } 6\text{d}$.</li>
</ul>

<h3>Comparative Calendar Week Division Matrix</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Time Horizon</th>
            <th>Total Days</th>
            <th>Completed Whole Weeks</th>
            <th>Decimal Weeks</th>
            <th>Agile 2-Week Sprints</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Standard 30-Day Month</td><td>30 days</td><td>4 weeks + 2 days</td><td>4.286 weeks</td><td>2.14 sprints</td></tr>
        <tr><td>Standard 31-Day Month</td><td>31 days</td><td>4 weeks + 3 days</td><td>4.429 weeks</td><td>2.21 sprints</td></tr>
        <tr><td>Calendar Quarter (Q1-Q4)</td><td>91 days</td><td>13 weeks exactly</td><td>13.000 weeks</td><td>6.50 sprints</td></tr>
        <tr><td>Common Year (365 Days)</td><td>365 days</td><td>52 weeks + 1 day</td><td>52.143 weeks</td><td>26.07 sprints</td></tr>
        <tr><td>Leap Year (366 Days)</td><td>366 days</td><td>52 weeks + 2 days</td><td>52.286 weeks</td><td>26.14 sprints</td></tr>
        <tr><td>Full Gestation Term</td><td>280 days</td><td>40 weeks exactly</td><td>40.000 weeks</td><td>20.00 sprints</td></tr>
    </tbody>
</table>

<h2>Agile Scrum Sprint Capacity and Release Cadence</h2>
<p>In modern software engineering, Scrum teams execute work in standardized time-boxed iterations designated as <strong>sprints</strong>, typically lasting two weeks ($14 \text{ calendar days}$ or $10 \text{ business days}$). Calculating the exact number of weeks between project milestones enables release managers to establish velocity targets:</p>

$$\text{Sprint Count} = \left\lfloor \frac{W_{\text{decimal}}}{2} \right\rfloor$$
$$\text{Sprint Velocity Capacity} = \text{Sprint Count} \times \bar{v}_{\text{team}}$$

<div class="worked-example-card">
    <h3>Worked Clinical &amp; Project Management Case Study: Clinical Trial Gestation Horizon</h3>
    <p><strong>Scenario:</strong> A clinical pharmaceutical research study tracks neonate developmental outcomes for mothers enrolled on <strong>January 12, 2026</strong> through study conclusion on <strong>September 28, 2026</strong>. Calculate: (1) total elapsed days, (2) whole weeks and residual days, (3) decimal weeks, and (4) how many 2-week clinical audit check-ins occur during this interval.</p>
    
    <div class="step-solution">
        <h4>Step 1: Compute Total Elapsed Days</h4>
        <p>From Jan 12 to Sept 28 in 2026 (common year):</p>
        <p>Jan: 19 days, Feb: 28 days, Mar: 31 days, Apr: 30 days, May: 31 days, Jun: 30 days, Jul: 31 days, Aug: 31 days, Sept: 28 days.</p>
        $$\Delta D = 19 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 28 = 259 \text{ days}$$

        <h4>Step 2: Partition into Whole Weeks and Residual Days</h4>
        $$W_{\text{whole}} = \lfloor 259 / 7 \rfloor = 37 \text{ weeks}$$
        $$D_{\text{residual}} = 259 \bmod 7 = 0 \text{ residual days}$$
        <p><strong>Result:</strong> Exactly 37 weeks and 0 days!</p>

        <h4>Step 3: Evaluate Decimal Weeks</h4>
        $$W_{\text{decimal}} = \frac{259}{7} = 37.000 \text{ decimal weeks}$$

        <h4>Step 4: Clinical Bi-Weekly Audit Count</h4>
        $$\text{Audits} = \lfloor 37 / 2 \rfloor = 18 \text{ complete bi-weekly audits (with 1 remaining week)}$$
    </div>
</div>

<h2>Common Implementation Pitfalls in Week Calculations</h2>
<ol>
    <li><strong>Confusing Elapsed Weeks with Calendar Week Numbers:</strong> Computing elapsed weeks ($\Delta D / 7$) measures duration. In contrast, ISO 8601 week numbers ($W01$ to $W53$) represent calendar positions anchored to January 4th.</li>
    <li><strong>Leap Year Day Shifts:</strong> A leap year introduces February 29th, shifting all post-February week offsets by exactly $+1/7 \text{ weeks}$ ($+0.143\text{ weeks}$).</li>
    <li><strong>Inclusive vs. Exclusive Date Bounds:</strong> If both start and end days are inclusive (e.g., counting both Monday and Friday as active days), add 1 to the raw day difference before dividing by 7.</li>
</ol>


<h2>Academic Semester Planning and Accreditation Credit Hour Standards</h2>
<p>Higher education institutions accredited in the United States operate under Department of Education Title IV regulations (34 CFR § 600.2) defining the statutory <strong>credit hour</strong>. A standard academic semester spans exactly 15 to 16 calendar weeks, comprising 14 weeks of formal direct instruction and 1 week of final examinations. One semester credit hour legally mandates a minimum of 1 hour (50 minutes) of classroom instruction plus 2 hours of out-of-class student work per week across the 15-week term:</p>

$$	ext{Direct Instruction Time} = 15 	ext{ weeks} 	imes 50 	ext{ minutes} = 750 	ext{ minutes} = 12.5 	ext{ hours per credit}$$

<p>University registrars and curriculum committees compute weeks between term start and graduation dates to certify that accelerated summer terms (typically 6, 8, or 10 weeks) deliver identical cumulative contact hours by proportionally increasing weekly lecture durations.</p>

<h2>Commercial Agriculture and Phenological Crop Maturation Horizons</h2>
<p>In commercial agronomy, crop production cycles from seed germination to harvest are quantified in standardized calendar week horizons. For instance, greenhouse floriculture schedules poinsettia planting precisely 14 to 16 weeks prior to the Thanksgiving holiday. In poultry farming and livestock management, broiler chicken production operates on an exact 6- to 8-week growth cycle, while bovine gestation spans an average of 40.5 weeks (283 days). Measuring elapsed weeks allows automated feeding and climate control systems to transition through calibrated nutritional growth phases.</p>
<section class="faq-section">
    <h2>Frequently Asked Questions About Weeks Between Dates</h2>
    <div class="faq-item">
        <h3>How do you calculate weeks and days between two dates?</h3>
        <p>Find the total number of days between the two dates, divide by 7 to get whole completed weeks, and the remainder gives the residual leftover days.</p>
    </div>
    <div class="faq-item">
        <h3>How many weeks are in a standard calendar year?</h3>
        <p>A common year has 365 days, which equals 52 weeks and 1 day (52.143 weeks). A leap year has 366 days, which equals 52 weeks and 2 days (52.286 weeks).</p>
    </div>
    <div class="faq-item">
        <h3>How do obstetricians calculate pregnancy gestation weeks?</h3>
        <p>Obstetricians measure gestational age from the first day of the last menstrual period (LMP) in completed weeks and days (e.g. 24 weeks and 3 days), with full term defined at 40 weeks.</p>
    </div>
    <div class="faq-item">
        <h3>How many two-week Agile sprints fit in a calendar quarter?</h3>
        <p>A standard quarter has 13 weeks (91 days), which comfortably accommodates 6 two-week development sprints (12 weeks) plus 1 buffer/hardening week.</p>
    </div>
</section>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article)


# ===========================================================================
# TOOL 4: best-engineering-calculator.html
# ===========================================================================
def gen_best_engineering():
    slug = "best-engineering-calculator"
    title = "Best Engineering Calculator Guide | Scientific & Graphing Benchmark"
    desc = "Compare the best engineering calculators for civil, mechanical, electrical, and chemical engineers. NCEES FE/PE exam approved models, Casio vs TI vs HP."
    h1 = "Best Engineering Calculator Guide"
    short_desc = "Interactive benchmark and specification comparison engine for professional engineers and STEM students, covering NCEES exam compliance, matrix solving, and CAS engines."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Best Engineering Calculator Guide",
      "url": "https://calchub.com/best-engineering-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Benchmark comparison engine for engineering scientific and graphing calculators, featuring NCEES exam approval and technical spec filters."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What calculators are permitted on the NCEES FE and PE engineering exams?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The NCEES approves specific models only: Casio fx-115 and fx-991 series, Texas Instruments TI-30X and TI-36X series, and HP 33s and HP 35s. Graphing and programmable calculators are strictly prohibited."
          }
        },
        {
          "@type": "Question",
          "name": "Which is better for engineering students: TI-36X Pro or Casio fx-991EX / fx-991CW?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Both are exceptional. The TI-36X Pro features a superior multi-tap key layout and scrolling history stack, while the Casio fx-991EX/CW excels with a faster processor, QR code graphing, and 4x4 matrix operations."
          }
        },
        {
          "@type": "Question",
          "name": "What is a Computer Algebra System (CAS) calculator?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A CAS calculator (like the TI-Nspire CX II CAS or HP Prime) can perform exact symbolic algebraic manipulations, evaluate indefinite integrals symbolically, and solve equations with variable coefficients without numerical approximation."
          }
        },
        {
          "@type": "Question",
          "name": "Why do engineers prefer Reverse Polish Notation (RPN)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "RPN (pioneered by HP) uses a stack-based operand architecture that eliminates parentheses, requires fewer keystrokes, and displays intermediate calculation states continuously."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-body">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.25rem; margin-bottom: 1.5rem;">
        <div>
            <label for="engDiscipline" style="font-weight: 600; font-size: 0.875rem;">Engineering Discipline:</label>
            <select id="engDiscipline" class="input-field" onchange="filterCalculators()">
                <option value="all">All Disciplines &amp; General STEM</option>
                <option value="fe_pe">NCEES FE / PE Exam Preparation</option>
                <option value="electrical">Electrical &amp; Electronics (Phasors &amp; Matrices)</option>
                <option value="mechanical">Mechanical &amp; Aerospace (Thermodynamics &amp; Calculus)</option>
                <option value="civil">Civil &amp; Structural (Statics &amp; Systems)</option>
            </select>
        </div>
        <div>
            <label for="calcClass" style="font-weight: 600; font-size: 0.875rem;">Calculator Category:</label>
            <select id="calcClass" class="input-field" onchange="filterCalculators()">
                <option value="all">All Models (Scientific &amp; Graphing CAS)</option>
                <option value="scientific">Scientific Non-Programmable (Exam Legal)</option>
                <option value="graphing">Graphing / CAS Flagship (Advanced R&amp;D)</option>
            </select>
        </div>
    </div>

    <!-- Interactive Comparison Cards Container -->
    <div id="calcComparisonGrid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-bottom: 1.5rem;">
        <!-- Injected via JS -->
    </div>
</div>

<script>
const CALC_MODELS = [
    {
        name: "Texas Instruments TI-36X Pro",
        type: "scientific",
        examLegal: true,
        disciplines: ["fe_pe", "electrical", "mechanical", "civil"],
        rating: "9.8 / 10 (Best Overall Exam)",
        price: "$24.99",
        specs: "Multi-tap keys, 3x3 matrices, poly/system solver, vector math, stats",
        summary: "The undisputed gold standard for the NCEES FE/PE exam. Intuitive multi-view screen and physical key layout."
    },
    {
        name: "Casio fx-991EX / fx-991CW ClassWiz",
        type: "scientific",
        examLegal: true,
        disciplines: ["fe_pe", "electrical", "mechanical", "civil"],
        rating: "9.7 / 10 (Fastest Processor)",
        price: "$22.99",
        specs: "High-res LCD, 4x4 matrices, QR code graphing, numerical calculus, 552 functions",
        summary: "Blazing fast processor with 4x4 matrix inversion. High-contrast display with natural textbook input."
    },
    {
        name: "TI-Nspire CX II CAS",
        type: "graphing",
        examLegal: false,
        disciplines: ["electrical", "mechanical", "chemical"],
        rating: "9.6 / 10 (Ultimate CAS Power)",
        price: "$165.00",
        specs: "Symbolic CAS engine, color screen, Python programming, dynamic geometry",
        summary: "Symbolic algebraic integration, differential equations, and full Python IDE. Banned on FE/PE exams."
    },
    {
        name: "HP Prime Graphing Calculator (v2)",
        type: "graphing",
        examLegal: false,
        disciplines: ["electrical", "mechanical"],
        rating: "9.5 / 10 (Touchscreen & RPN)",
        price: "$149.00",
        specs: "Capacitive color touchscreen, 528 MHz ARM, RPN stack mode, wireless connectivity",
        summary: "Unmatched computation speed with glass capacitive touch and optional Reverse Polish Notation (RPN)."
    },
    {
        name: "Texas Instruments TI-84 Plus CE",
        type: "graphing",
        examLegal: false,
        disciplines: ["mechanical", "civil"],
        rating: "9.0 / 10 (High School & College Standard)",
        price: "$139.00",
        specs: "Backlit color display, rechargeable battery, accepted on SAT/ACT/AP exams",
        summary: "Ubiquitous textbook software support and immense library of downloadable engineering programs."
    }
];

function filterCalculators() {
    const disc = document.getElementById('engDiscipline').value;
    const cat = document.getElementById('calcClass').value;
    const grid = document.getElementById('calcComparisonGrid');

    const filtered = CALC_MODELS.filter(m => {
        const matchesDisc = (disc === 'all') || (disc === 'fe_pe' ? m.examLegal : m.disciplines.includes(disc));
        const matchesCat = (cat === 'all') || (m.type === cat);
        return matchesDisc && matchesCat;
    });

    grid.innerHTML = filtered.map(m => `
        <div style="background: white; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
            <div>
                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
                    <h3 style="margin: 0; font-size: 1.1rem; color: #1e293b;">${m.name}</h3>
                    <span style="background: ${m.examLegal ? '#dcfce7' : '#fee2e2'}; color: ${m.examLegal ? '#15803d' : '#b91c1c'}; font-size: 0.75rem; font-weight: 700; padding: 0.2rem 0.5rem; border-radius: 9999px;">
                        ${m.examLegal ? 'NCEES FE/PE APPROVED' : 'NON-EXAM / CAS'}
                    </span>
                </div>
                <div style="color: #2563eb; font-weight: 700; font-size: 0.9rem; margin-bottom: 0.5rem;">${m.rating} &bull; Approx ${m.price}</div>
                <p style="font-size: 0.85rem; color: #475569; margin-bottom: 0.75rem;">${m.summary}</p>
            </div>
            <div style="background: #f8fafc; border-radius: 6px; padding: 0.5rem 0.75rem; font-size: 0.8rem; color: #334155; border: 1px solid #e2e8f0;">
                <strong>Specs:</strong> ${m.specs}
            </div>
        </div>
    `).join('');
}

window.addEventListener('DOMContentLoaded', filterCalculators);
</script>"""

    article = """<h2>Engineering Computational Requirements and Hardware Architectures</h2>
<p>Professional engineering disciplines—civil, mechanical, electrical, aerospace, chemical, and nuclear—demand computational tools capable of evaluating complex numerical problems under strict time constraints. While high-performance workstations execute Finite Element Analysis (FEA) and Computational Fluid Dynamics (CFD), the physical handheld <strong>engineering calculator</strong> remains an indispensable tool on job sites, in fabrication shops, and in high-stakes professional licensure examinations.</p>

<p>The mathematical workload of an engineer centers on four core numerical capabilities:</p>
<ol>
    <li><strong>Matrix Algebra and Linear System Solutions:</strong> Evaluating $n \times n$ systems of equations $[A]\{x\} = \{b\}$ for structural truss analysis, mesh current analysis, and state-space control.</li>
    <li><strong>Complex Number Arithmetic (Rectangular &amp; Polar Phasors):</strong> Transforming between Cartesian ($z = a + jb$) and polar ($z = r \angle \theta$) coordinates for AC circuit analysis and impedance triangles ($Z = R + jX$).</li>
    <li><strong>Numerical Calculus &amp; Root-Finding:</strong> Numerical integration $\int_a^b f(x) dx$ via Gauss-Kronrod or Simpson's rules, numerical differentiation $f'(x)$, and non-linear polynomial root-finding ($ax^3 + bx^2 + cx + d = 0$).</li>
    <li><strong>Statistical Distributions &amp; Unit Conversions:</strong> Normal cumulative distribution functions ($z$-scores), linear regression correlations ($r$), and direct physical unit conversions across imperial and SI metric systems.</li>
</ol>

<h2>The NCEES Examination Calculator Policy (FE &amp; PE Licensure)</h2>
<p>In the United States, the National Council of Examiners for Engineering and Surveying (NCEES) administers the rigorous <strong>Fundamentals of Engineering (FE)</strong> and <strong>Principles and Practice of Engineering (PE)</strong> licensure examinations. To maintain test security and prevent unauthorized external formula storage, the NCEES enforces a strict calculator policy that bans all graphing, internet-connected, or user-programmable devices.</p>

<p>Only three specific calculator series are approved for NCEES examinations:</p>
<ul>
    <li><strong>Casio:</strong> All <code>fx-115</code> and <code>fx-991</code> models (including fx-115ES PLUS, fx-991EX ClassWiz, and fx-991CW).</li>
    <li><strong>Texas Instruments:</strong> All <code>TI-30X</code> and <code>TI-36X</code> models (specifically the TI-36X Pro and TI-30X IIS).</li>
    <li><strong>Hewlett Packard:</strong> The <code>HP 33s</code> and <code>HP 35s</code> scientific models (now discontinued, but legally grandmothered).</li>
</ul>

<h3>Engineering Calculator Benchmark Comparison Matrix</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Calculator Model</th>
            <th>Type / Engine</th>
            <th>NCEES FE/PE Approved?</th>
            <th>Matrix Max Size</th>
            <th>Complex Phasor Math</th>
            <th>Symbolic CAS Engine</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>TI-36X Pro</td><td>Scientific (MultiView)</td><td>YES (Top Pick)</td><td>3 &times; 3</td><td>Full Polar &amp; Rectangular</td><td>No (Numerical Only)</td></tr>
        <tr><td>Casio fx-991EX / CW</td><td>Scientific (ClassWiz)</td><td>YES (Fastest)</td><td>4 &times; 4</td><td>Full Polar &amp; Rectangular</td><td>No (Numerical Only)</td></tr>
        <tr><td>TI-Nspire CX II CAS</td><td>Graphing CAS (ARM)</td><td>NO (Prohibited)</td><td>Unlimited</td><td>Full Complex Variables</td><td>YES (Exact Symbolic)</td></tr>
        <tr><td>HP Prime v2</td><td>Graphing Touch (ARM)</td><td>NO (Prohibited)</td><td>Unlimited</td><td>Full Complex Variables</td><td>YES (Exact Symbolic)</td></tr>
        <tr><td>TI-84 Plus CE</td><td>Graphing Non-CAS (Z80)</td><td>NO (Prohibited)</td><td>Unlimited</td><td>Rectangular &amp; Polar</td><td>No (Numerical Only)</td></tr>
    </tbody>
</table>

<h2>Symbolic Computer Algebra Systems (CAS) vs. Numerical Approximators</h2>
<p>The distinction between standard scientific calculators and advanced CAS flagships (such as the TI-Nspire CX II CAS or HP Prime) lies in symbolic manipulation. A standard numerical calculator evaluates an integral as a single floating-point decimal:</p>

$$\int_0^1 x^2 \, dx \approx 0.3333333333$$

<p>In contrast, a Computer Algebra System processes mathematical symbols as exact analytical expressions:</p>

$$\int x^2 \, dx = \frac{x^3}{3} + C, \quad \frac{d}{dx}\left( \sin(3x) \cdot e^{-2x} \right) = e^{-2x}(3\cos(3x) - 2\sin(3x))$$

<p>For advanced engineering coursework—such as fluid dynamics, controls engineering, and heat transfer—a CAS calculator saves hours of tedious algebraic derivation. However, because CAS engines solve equations symbolically, professional licensure boards strictly prohibit them in exam halls.</p>

<div class="worked-example-card">
    <h3>Worked Engineering Examination Case Study: 3-Phase AC Power Phasor Impedance</h3>
    <p><strong>Scenario:</strong> An electrical engineer taking the NCEES FE Electrical exam must evaluate the equivalent input impedance of a parallel branch consisting of a pure resistor $R = 45 \, \Omega$ in parallel with an inductive reactor $X_L = j60 \, \Omega$. Calculate: (1) equivalent impedance in rectangular format, (2) equivalent impedance in polar phasor format ($|Z| \angle \theta$), and (3) verify why a multi-view calculator is essential under exam conditions.</p>
    
    <div class="step-solution">
        <h4>Step 1: Formulate the Parallel Impedance Equation</h4>
        $$Z_{\text{eq}} = \frac{Z_1 \cdot Z_2}{Z_1 + Z_2} = \frac{45 \cdot (j60)}{45 + j60} = \frac{j2700}{45 + j60}$$

        <h4>Step 2: Complex Conjugate Reduction</h4>
        $$Z_{\text{eq}} = \frac{j2700 \cdot (45 - j60)}{(45)^2 + (60)^2} = \frac{j121,500 + 162,000}{2025 + 3600} = \frac{162,000 + j121,500}{5625}$$
        $$Z_{\text{eq}} = 28.8 + j21.6 \, \Omega$$

        <h4>Step 3: Convert to Polar Phasor Format</h4>
        $$|Z| = \sqrt{(28.8)^2 + (21.6)^2} = \sqrt{829.44 + 466.56} = \sqrt{1296} = 36.0 \, \Omega$$
        $$\theta = \arctan\left(\frac{21.6}{28.8}\right) = \arctan(0.75) \approx 36.87^\circ$$
        $$Z_{\text{eq}} = 36.0 \, \Omega \angle 36.87^\circ$$
        <p><strong>Exam Insight:</strong> On a TI-36X Pro or Casio fx-991EX, entering <code>(45 * 60i) / (45 + 60i)</code> in complex mode directly outputs $28.8 + 21.6i$ in 1.5 seconds, saving 4 minutes of manual algebraic rationalization per question!</p>
    </div>
</div>

<h2>Common Mistakes When Selecting an Engineering Calculator</h2>
<ol>
    <li><strong>Purchasing an Unapproved Calculator for Licensure Exams:</strong> Arriving at an NCEES testing center with a TI-84 Plus or TI-Nspire will result in immediate confiscation by exam proctors, leaving the candidate to complete an 8-hour engineering exam using the computer's basic digital interface.</li>
    <li><strong>Ignoring Complex Matrix Support:</strong> Electrical engineering students who choose entry-level scientific calculators often discover their model cannot invert matrices containing complex numbers ($[Z]^{-1}$), rendering them incapable of solving 3-node AC power networks.</li>
    <li><strong>Neglecting Solar Dual-Power Backup:</strong> Field engineers working on remote industrial job sites require dual-power (solar cell + LR44/CR2032 lithium backup) to prevent device shutdown during critical inspection calculations.</li>
</ol>


<h2>Power Subsystems: Rechargeable Lithium-Ion vs. Alkaline and Solar Arrays</h2>
<p>A crucial practical differentiator among engineering calculators is their internal power architecture. Models like the Casio fx-991EX and TI-36X Pro utilize hybrid <strong>Two-Way Power (Solar + Battery)</strong>, combining a high-efficiency photovoltaic cell with an LR44 or CR2032 button cell backup. These units operate reliably for 2 to 5 years without maintenance, making them ideal for field engineers, offshore rigs, and examination halls where dead batteries cause catastrophic failure.</p>

<p>Conversely, advanced graphing and CAS models (TI-Nspire CX II CAS, HP Prime v2, TI-84 Plus CE) feature backlit color LCD screens and high-frequency ARM processors that demand rechargeable 3.7V lithium-ion battery packs. While rechargeable via standard USB-C or micro-USB cables, they require periodic recharging every 1 to 2 weeks of intensive mathematical modeling.</p>

<h2>Software Emulators, Cloud Notebooks, and Examination Policies</h2>
<p>While physical hardware calculators remain mandatory in proctored examination settings, professional practicing engineers routinely augment physical devices with software simulation suites. Official PC and Mac emulator licenses (such as TI-SmartView and Casio ClassWiz Emulator) allow engineering professors and corporate trainers to project live calculator screens during technical lectures. Outside testing centers, cloud computing environments like Jupyter Notebooks running Python with NumPy, SymPy, and SciPy provide infinite mathematical power, complementing the handheld device for large-scale engineering R&D.</p>
<section class="faq-section">
    <h2>Frequently Asked Questions About Engineering Calculators</h2>
    <div class="faq-item">
        <h3>What calculators are permitted on the NCEES FE and PE engineering exams?</h3>
        <p>The NCEES approves specific models only: Casio fx-115 and fx-991 series, Texas Instruments TI-30X and TI-36X series, and HP 33s and HP 35s. Graphing and programmable calculators are strictly prohibited.</p>
    </div>
    <div class="faq-item">
        <h3>Which is better for engineering students: TI-36X Pro or Casio fx-991EX / fx-991CW?</h3>
        <p>Both are exceptional. The TI-36X Pro features a superior multi-tap key layout and scrolling history stack, while the Casio fx-991EX/CW excels with a faster processor, QR code graphing, and 4x4 matrix operations.</p>
    </div>
    <div class="faq-item">
        <h3>What is a Computer Algebra System (CAS) calculator?</h3>
        <p>A CAS calculator (like the TI-Nspire CX II CAS or HP Prime) can perform exact symbolic algebraic manipulations, evaluate indefinite integrals symbolically, and solve equations with variable coefficients without numerical approximation.</p>
    </div>
    <div class="faq-item">
        <h3>Why do engineers prefer Reverse Polish Notation (RPN)?</h3>
        <p>RPN (pioneered by HP) uses a stack-based operand architecture that eliminates parentheses, requires fewer keystrokes, and displays intermediate calculation states continuously.</p>
    </div>
</section>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article, category_hub="engineering.html", category_name="Engineering Tools")


def main():
    tc_html = gen_time_card()
    with open(os.path.join(BASE_DIR, "time-card-calculator.html"), "w", encoding="utf-8") as f:
        f.write(tc_html)
    print("Generated time-card-calculator.html successfully!")

    td_html = gen_time_duration()
    with open(os.path.join(BASE_DIR, "time-duration-calculator.html"), "w", encoding="utf-8") as f:
        f.write(td_html)
    print("Generated time-duration-calculator.html successfully!")

    wb_html = gen_weeks_between_dates()
    with open(os.path.join(BASE_DIR, "weeks-between-dates-calculator.html"), "w", encoding="utf-8") as f:
        f.write(wb_html)
    print("Generated weeks-between-dates-calculator.html successfully!")

    be_html = gen_best_engineering()
    with open(os.path.join(BASE_DIR, "best-engineering-calculator.html"), "w", encoding="utf-8") as f:
        f.write(be_html)
    print("Generated best-engineering-calculator.html successfully!")

if __name__ == "__main__":
    main()
