# -*- coding: utf-8 -*-
"""
Generator for Batch 39 - Part 1
Tools:
1. hours-calculator.html (Work Hours, Timesheet, Decimal Hours & Pay)
2. ratio-simplifier-calculator.html (Ratio Reduction, Euclid GCD, Aspect Ratios)
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COMMON_TAIL = """    <footer class="site-footer">
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>About CalcHub</h4>
                    <p>CalcHub delivers professional-grade, peer-reviewed computational engines, timesheet mathematics, and algebraic reduction utilities adhering to international ISO, FLSA, and IEEE scientific calculation standards.</p>
                </div>
                <div class="footer-col">
                    <h4>Chronometric &amp; Math Suites</h4>
                    <ul>
                        <li><a href="datetime.html">Date &amp; Time Utilities</a></li>
                        <li><a href="math.html">Mathematics &amp; Statistics</a></li>
                        <li><a href="finance.html">Payroll &amp; Financial Analysis</a></li>
                        <li><a href="converter.html">Unit &amp; Chrono Converters</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Core Productivity Tools</h4>
                    <ul>
                        <li><a href="hours-calculator.html">Work Hours Calculator</a></li>
                        <li><a href="ratio-simplifier-calculator.html">Ratio Simplifier</a></li>
                        <li><a href="salary-calculator.html">Salary &amp; Paycheck</a></li>
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
                <p>&copy; 2026 CalcHub. All rights reserved. Precision chronological and algebraic computational systems.</p>
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
                    <h3>Related Chrono &amp; Math Tools</h3>
                    <ul class="sidebar-links">
                        <li><a href="hours-calculator.html">Work Hours Calculator</a></li>
                        <li><a href="ratio-simplifier-calculator.html">Ratio Simplifier</a></li>
                        <li><a href="salary-calculator.html">Salary &amp; Paycheck</a></li>
                        <li><a href="date-difference-calculator.html">Date Difference</a></li>
                        <li><a href="time-converter.html">Time Converter</a></li>
                        <li><a href="percentage-calculator.html">Percentage Calculator</a></li>
                        <li><a href="fraction-calculator.html">Fraction Calculator</a></li>
                        <li><a href="overtime-calculator.html">Overtime Calculator</a></li>
                        <li><a href="time-card-calculator.html">Time Card Calculator</a></li>
                    </ul>
                </div>
            </aside>
        </div>
    </div>
{COMMON_TAIL}"""


# ===========================================================================
# TOOL 1: hours-calculator.html
# ===========================================================================
def gen_hours_calculator():
    slug = "hours-calculator"
    title = "Hours Calculator | Work Time, Decimal Hours, Breaks & Gross Pay"
    desc = "Calculate total work hours, minutes, and decimal hours between start and end times with unpaid break deductions, FLSA 7-minute rounding rules, and gross payroll earnings."
    h1 = "Hours Calculator"
    short_desc = "Compute precise worked elapsed time, sexagesimal to decimal conversions, unpaid lunch break subtractions, and gross payroll amounts across overnight shifts."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Hours Calculator",
      "url": "https://calchub.com/hours-calculator.html",
      "applicationCategory": "BusinessApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Professional work hours, decimal conversion, lunch break subtraction, and payroll computation tool."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How are minutes converted into decimal hours for payroll?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Minutes are divided by 60 to produce a decimal fraction. For instance, 15 minutes equals 15/60 = 0.25 hours, 30 minutes equals 0.50 hours, and 45 minutes equals 0.75 hours. Decimal hours are required by automated payroll accounting software to multiply by hourly wage rates."
          }
        },
        {
          "@type": "Question",
          "name": "What is the FLSA 7-minute rounding rule (29 CFR § 785.48)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Under the US Fair Labor Standards Act (FLSA), employers may round employee punch times to the nearest 15-minute interval (quarter of an hour). Punches between 1 and 7 minutes past the quarter-hour round down, whereas punches between 8 and 14 minutes past the quarter-hour round up to the next quarter-hour."
          }
        },
        {
          "@type": "Question",
          "name": "How does the calculator handle overnight shifts crossing midnight?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "When the recorded end time is numerically earlier than the start time (e.g., start at 22:00 and end at 06:30), the algorithm applies a modulo-24 adjustment by adding 24 hours (1,440 minutes) to the end timestamp before subtracting the start time and deducting unpaid meal breaks."
          }
        },
        {
          "@type": "Question",
          "name": "What is the difference between total elapsed hours and net billable hours?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Total elapsed hours represent the total wall-clock duration between clock-in and clock-out. Net billable or payable hours subtract all bona fide unpaid meal intervals (typically 30 to 60 minutes where the employee is entirely relieved from duty per labor standards)."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-grid">
    <div class="calc-inputs">
        <div class="input-group">
            <label for="startTime">Start Time (Clock-In)</label>
            <input type="time" id="startTime" value="09:00" class="input-field">
            <span class="input-hint">24-hour or AM/PM shift starting timestamp</span>
        </div>
        <div class="input-group">
            <label for="endTime">End Time (Clock-Out)</label>
            <input type="time" id="endTime" value="17:30" class="input-field">
            <span class="input-hint">Shift end timestamp (handles overnight shifts)</span>
        </div>
        <div class="input-group">
            <label for="breakMins">Unpaid Break Duration (Minutes)</label>
            <input type="number" id="breakMins" value="30" min="0" max="720" step="1" class="input-field">
            <span class="input-hint">Deducted lunch or meal recess (e.g., 30 or 60 min)</span>
        </div>
        <div class="input-group">
            <label for="hourlyRate">Hourly Pay Rate ($ / hour)</label>
            <input type="number" id="hourlyRate" value="28.50" min="0" step="0.25" class="input-field">
            <span class="input-hint">Base contract or standard hourly wage</span>
        </div>
        <div class="input-group">
            <label for="roundingMode">FLSA Punch Rounding Mode</label>
            <select id="roundingMode" class="input-field">
                <option value="exact" selected>Exact Minutes (No Rounding)</option>
                <option value="15min">15-Minute Rule (7/8 Minute FLSA Window)</option>
                <option value="6min">6-Minute Tenth-Hour Rule (0.10 hr)</option>
            </select>
            <span class="input-hint">Select employer timesheet rounding standard</span>
        </div>
        <div class="input-group">
            <label for="overtimeThreshold">Daily Overtime Threshold (Hours)</label>
            <input type="number" id="overtimeThreshold" value="8.0" min="0" max="24" step="0.5" class="input-field">
            <span class="input-hint">Standard daily hours before 1.5x overtime multiplier (default 8)</span>
        </div>
    </div>
    <div class="calc-results">
        <div class="result-card primary-result">
            <div class="result-label">Net Payable Work Duration</div>
            <div class="result-value" id="resDuration">7 hrs 00 mins</div>
            <div class="result-sub" id="resDecimal">7.000 Decimal Hours</div>
        </div>
        <div class="result-grid-mini" style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;margin-top:1rem;">
            <div class="result-card">
                <div class="result-label">Total Elapsed Span</div>
                <div class="result-value-sm" id="resElapsed">8 hrs 30 mins</div>
            </div>
            <div class="result-card">
                <div class="result-label">Break Deducted</div>
                <div class="result-value-sm" id="resBreakDeducted">30 mins (0.50 hrs)</div>
            </div>
            <div class="result-card">
                <div class="result-label">Regular Hours</div>
                <div class="result-value-sm" id="resRegularHrs">7.00 hrs</div>
            </div>
            <div class="result-card">
                <div class="result-label">Overtime Hours</div>
                <div class="result-value-sm" id="resOvertimeHrs">0.00 hrs</div>
            </div>
        </div>
        <div class="result-card" style="margin-top:1rem;background:var(--bg-accent, #eff6ff);border-left:4px solid var(--brand-primary, #2563eb);">
            <div class="result-label">Estimated Gross Shift Earnings</div>
            <div class="result-value" id="resGrossPay" style="color:var(--brand-primary, #2563eb);font-size:1.75rem;">$199.50</div>
            <div class="result-sub" id="resPayBreakdown">7.00 hrs @ $28.50/hr + 0.00 OT hrs @ $42.75/hr</div>
        </div>
    </div>
</div>
<script>
function calculateHours() {
    const startStr = document.getElementById('startTime').value;
    const endStr = document.getElementById('endTime').value;
    const breakMins = Math.max(0, parseFloat(document.getElementById('breakMins').value) || 0);
    const hourlyRate = Math.max(0, parseFloat(document.getElementById('hourlyRate').value) || 0);
    const roundingMode = document.getElementById('roundingMode').value;
    const otThreshold = Math.max(0, parseFloat(document.getElementById('overtimeThreshold').value) || 8);

    if (!startStr || !endStr) return;

    const [sh, sm] = startStr.split(':').map(Number);
    const [eh, em] = endStr.split(':').map(Number);

    let startTotalMins = sh * 60 + sm;
    let endTotalMins = eh * 60 + em;

    // Apply punch rounding to start and end if requested
    function applyPunchRounding(mins, mode) {
        if (mode === '15min') {
            const remainder = mins % 15;
            if (remainder >= 8) {
                return mins + (15 - remainder);
            } else {
                return mins - remainder;
            }
        } else if (mode === '6min') {
            const remainder = mins % 6;
            if (remainder >= 3) {
                return mins + (6 - remainder);
            } else {
                return mins - remainder;
            }
        }
        return mins;
    }

    const roundedStartMins = applyPunchRounding(startTotalMins, roundingMode);
    let roundedEndMins = applyPunchRounding(endTotalMins, roundingMode);

    // Midnight rollover logic
    if (roundedEndMins < roundedStartMins) {
        roundedEndMins += 24 * 60;
    }

    let rawElapsedMins = roundedEndMins - roundedStartMins;
    let netMins = Math.max(0, rawElapsedMins - breakMins);

    const netHours = Math.floor(netMins / 60);
    const netRemainderMins = netMins % 60;
    const decimalHours = netMins / 60;

    const elapsedHours = Math.floor(rawElapsedMins / 60);
    const elapsedRemainderMins = rawElapsedMins % 60;

    let regularHours = Math.min(decimalHours, otThreshold);
    let overtimeHours = Math.max(0, decimalHours - otThreshold);

    const otRate = hourlyRate * 1.5;
    const regularPay = regularHours * hourlyRate;
    const overtimePay = overtimeHours * otRate;
    const totalGross = regularPay + overtimePay;

    document.getElementById('resDuration').innerText = `${netHours} hrs ${netRemainderMins.toString().padStart(2, '0')} mins`;
    document.getElementById('resDecimal').innerText = `${decimalHours.toFixed(3)} Decimal Hours (${decimalHours.toFixed(2)} for payroll)`;
    document.getElementById('resElapsed').innerText = `${elapsedHours} hrs ${elapsedRemainderMins.toString().padStart(2, '0')} mins`;
    document.getElementById('resBreakDeducted').innerText = `${breakMins} mins (${(breakMins / 60).toFixed(2)} hrs)`;
    document.getElementById('resRegularHrs').innerText = `${regularHours.toFixed(2)} hrs`;
    document.getElementById('resOvertimeHrs').innerText = `${overtimeHours.toFixed(2)} hrs`;
    document.getElementById('resGrossPay').innerText = `$${totalGross.toFixed(2)}`;
    document.getElementById('resPayBreakdown').innerText = `${regularHours.toFixed(2)} reg hrs @ $${hourlyRate.toFixed(2)} + ${overtimeHours.toFixed(2)} OT hrs @ $${otRate.toFixed(2)}`;
}

['startTime', 'endTime', 'breakMins', 'hourlyRate', 'roundingMode', 'overtimeThreshold'].forEach(id => {
    const el = document.getElementById(id);
    if (el) {
        el.addEventListener('input', calculateHours);
        el.addEventListener('change', calculateHours);
    }
});
window.addEventListener('DOMContentLoaded', calculateHours);
</script>"""

    article = """<h2>Mathematical Formulation of Work Time and Decimal Conversion</h2>
<p>Tracking occupational attendance, professional billable hours, and industrial shift work requires continuous transformation between sexagesimal chronometric units (hours, minutes, and seconds based on base-60) and decimal arithmetic (base-10). Automated payroll software, enterprise resource planning (ERP) systems, and job-costing databases cannot directly execute algebraic multiplication on strings representing hours and minutes ($HH:MM$). Instead, worked intervals must be mapped to continuous real numbers known as decimal hours.</p>

<p>The total raw elapsed duration $T_{\text{raw}}$ between an arbitrary clock-in timestamp $t_{\text{start}}$ and clock-out timestamp $t_{\text{end}}$ on a 24-hour diurnal cycle is expressed in total minutes as follows:</p>

$$T_{\text{raw}} = (t_{\text{end}} - t_{\text{start}}) \pmod{1440}$$

<p>Where $1440$ represents the total number of minutes in a standard civil solar day ($24 \times 60$). When an employee works an overnight nocturnal shift—for example, clocking in at 21:45 in the evening and clocking out at 06:15 the following morning—the condition $t_{\text{end}} < t_{\text{start}}$ triggers the modulo operator, automatically shifting the terminal timestamp forward by adding 1,440 minutes.</p>

<p>Net payable work time $T_{\text{net}}$ accounts for bona fide unpaid meal or personal rest intervals $T_{\text{break}}$ where the worker is fully relieved of all duties:</p>

$$T_{\text{net}} = \max(0, T_{\text{raw}} - T_{\text{break}})$$

<p>Conversion from net discrete minutes $T_{\text{net}}$ to fractional decimal hours $H_{\text{decimal}}$ is governed by exact rational division:</p>

$$H_{\text{decimal}} = \frac{T_{\text{net}}}{60} = H_{\text{integer}} + \frac{M_{\text{remainder}}}{60}$$

<p>Where $H_{\text{integer}} = \lfloor T_{\text{net}} / 60 \rfloor$ and $M_{\text{remainder}} = T_{\text{net}} \bmod 60$. For instance, a shift duration of 7 hours and 42 minutes yields:</p>

$$H_{\text{decimal}} = 7 + \frac{42}{60} = 7 + 0.70 = 7.700 \text{ hours}$$

<h2>The FLSA 7-Minute Rounding Framework (29 CFR § 785.48)</h2>
<p>In accordance with United States federal statutory regulations established by the Fair Labor Standards Act (FLSA) under Title 29 of the Code of Federal Regulations, Section 785.48(b), employers are legally permitted to record employee starting and stopping times to the nearest five minutes, six minutes (one-tenth of an hour), or quarter of an hour (15 minutes). For the common 15-minute rounding paradigm, the statute establishes an asymmetric 7/8 minute rule:</p>

<ul>
    <li><strong>Down-Rounding (1 to 7 Minutes):</strong> If an employee punches in between 1 and 7 minutes after a 15-minute boundary, the time is rounded back down to the preceding quarter-hour mark.</li>
    <li><strong>Up-Rounding (8 to 14 Minutes):</strong> If an employee punches in between 8 and 14 minutes past a 15-minute boundary, the time is rounded forward to the next quarter-hour mark.</li>
    <li><strong>Symmetry Principle:</strong> The employer cannot enforce rounding that exclusively operates in favor of the business. It must work symmetrically on clock-ins and clock-outs, ensuring that over an extended auditing period, employee compensation accurately reflects all hours worked.</li>
</ul>

<h3>Sexagesimal to Decimal Conversion Reference Table</h3>
<p>The following benchmark reference matrix establishes the exact fractional and decimal equivalencies across the complete 60-minute cycle in 5-minute increments, alongside standard payroll rounding benchmarks:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Minutes ($MM$)</th>
            <th>Fractional Hour</th>
            <th>Decimal Equivalent</th>
            <th>Tenth-Hour (6-Min)</th>
            <th>Quarter-Hour (15-Min)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>05 mins</td><td>5 / 60</td><td>0.0833 hr</td><td>0.10 hr</td><td>0.00 hr (Round Down)</td></tr>
        <tr><td>10 mins</td><td>10 / 60</td><td>0.1667 hr</td><td>0.20 hr</td><td>0.25 hr (Round Up)</td></tr>
        <tr><td>15 mins</td><td>15 / 60</td><td>0.2500 hr</td><td>0.30 hr</td><td>0.25 hr (Exact)</td></tr>
        <tr><td>20 mins</td><td>20 / 60</td><td>0.3333 hr</td><td>0.30 hr</td><td>0.25 hr (Round Down)</td></tr>
        <tr><td>25 mins</td><td>25 / 60</td><td>0.4167 hr</td><td>0.40 hr</td><td>0.50 hr (Round Up)</td></tr>
        <tr><td>30 mins</td><td>30 / 60</td><td>0.5000 hr</td><td>0.50 hr</td><td>0.50 hr (Exact)</td></tr>
        <tr><td>35 mins</td><td>35 / 60</td><td>0.5833 hr</td><td>0.60 hr</td><td>0.50 hr (Round Down)</td></tr>
        <tr><td>40 mins</td><td>40 / 60</td><td>0.6667 hr</td><td>0.70 hr</td><td>0.75 hr (Round Up)</td></tr>
        <tr><td>45 mins</td><td>45 / 60</td><td>0.7500 hr</td><td>0.80 hr</td><td>0.75 hr (Exact)</td></tr>
        <tr><td>50 mins</td><td>50 / 60</td><td>0.8333 hr</td><td>0.80 hr</td><td>0.75 hr (Round Down)</td></tr>
        <tr><td>55 mins</td><td>55 / 60</td><td>0.9167 hr</td><td>0.90 hr</td><td>1.00 hr (Round Up)</td></tr>
        <tr><td>60 mins</td><td>60 / 60</td><td>1.0000 hr</td><td>1.00 hr</td><td>1.00 hr (Exact)</td></tr>
    </tbody>
</table>

<h2>Overtime Allocation and Gross Wage Formulation</h2>
<p>Gross compensation $W_{\text{gross}}$ is governed by statutory overtime thresholds, commonly defined under federal standards as 40 hours per workweek, or under daily overtime jurisdictions (such as California Labor Code § 510) as all hours exceeding 8.0 in a single diurnal work period. For a daily overtime model with threshold $H_{\text{ot\_thresh}}$:</p>

$$H_{\text{reg}} = \min(H_{\text{decimal}}, H_{\text{ot\_thresh}})$$

$$H_{\text{ot}} = \max(0, H_{\text{decimal}} - H_{\text{ot\_thresh}})$$

<p>Gross compensation combines standard remuneration at the base contract rate $R_{\text{base}}$ with premium compensation calculated at the statutory time-and-a-half rate ($1.5 \times R_{\text{base}}$):</p>

$$W_{\text{gross}} = (H_{\text{reg}} \times R_{\text{base}}) + (H_{\text{ot}} \times 1.5 \times R_{\text{base}})$$

<div class="worked-example-card">
    <h3>Worked Engineering Case Study: Overnight Manufacturing Shift</h3>
    <p><strong>Scenario:</strong> A CNC precision machinist clocks into an aerospace manufacturing plant at 20:47 in the evening and clocks out at 06:22 the following morning. The employee takes an unpaid 45-minute lunch break at 01:30. The machinist's contractual base pay is $34.00 per hour, and the facility enforces daily overtime compensation for all hours worked in excess of 8.00 hours. Punch rounding is set to exact minutes.</p>
    
    <div class="step-solution">
        <h4>Step 1: Convert Start and End Timestamps to Diurnal Minutes</h4>
        <p>Start: $20:47 = (20 \times 60) + 47 = 1200 + 47 = 1247 \text{ minutes}$.</p>
        <p>End: $06:22 = (6 \times 60) + 22 = 360 + 22 = 382 \text{ minutes}$.</p>

        <h4>Step 2: Calculate Raw Elapsed Span Across Midnight</h4>
        <p>Since $t_{\text{end}} (382) < t_{\text{start}} (1247)$, add 1,440 minutes:</p>
        $$T_{\text{raw}} = (382 + 1440) - 1247 = 1822 - 1247 = 575 \text{ minutes}$$
        <p>In sexagesimal hours: $\lfloor 575 / 60 \rfloor = 9 \text{ hours and } 35 \text{ minutes}$.</p>

        <h4>Step 3: Deduct Unpaid Meal Interval</h4>
        $$T_{\text{net}} = 575 - 45 = 530 \text{ minutes}$$
        $$\text{Net Duration} = 8 \text{ hours and } 50 \text{ minutes}$$

        <h4>Step 4: Convert to Decimal Hours</h4>
        $$H_{\text{decimal}} = \frac{530}{60} \approx 8.8333 \text{ hours}$$

        <h4>Step 5: Partition Regular vs. Overtime Hours and Compute Wages</h4>
        <p>Regular Hours $H_{\text{reg}} = 8.000 \text{ hours}$.</p>
        <p>Overtime Hours $H_{\text{ot}} = 8.8333 - 8.000 = 0.8333 \text{ hours}$.</p>
        <p>Regular Pay: $8.000 \times \$34.00 = \$272.00$.</p>
        <p>Overtime Rate: $\$34.00 \times 1.5 = \$51.00 / \text{hour}$.</p>
        <p>Overtime Pay: $0.8333 \times \$51.00 = \$42.50$.</p>
        <p><strong>Total Gross Shift Earnings:</strong> $\$272.00 + \$42.50 = \$314.50$.</p>
    </div>
</div>

<h2>Common Audit Traps and Timesheet Discrepancies</h2>
<ol>
    <li><strong>Minute-to-Decimal Truncation Errors:</strong> Calculating payroll by rounding decimal hours to a single decimal place (e.g., recording 8 hours 20 minutes as 8.3 instead of 8.333) results in compounding payroll shortfalls of 2 minutes per shift, accumulating into significant annual wage underpayments.</li>
    <li><strong>Asymmetric Rounding Practices:</strong> Implementing a punch clock configured to round employee arrivals forward to the next quarter hour while rounding clock-outs backward constitutes an unlawful FLSA wage violation subject to federal Department of Labor back-pay penalties.</li>
    <li><strong>Unrecorded Short Breaks:</strong> Under 29 CFR § 785.18, short rest pauses lasting 5 to 20 minutes are legally defined as compensable working hours that cannot be deducted from employee timesheet totals.</li>
</ol>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article)


# ===========================================================================
# TOOL 2: ratio-simplifier-calculator.html
# ===========================================================================
def gen_ratio_simplifier():
    slug = "ratio-simplifier-calculator"
    title = "Ratio Simplifier Calculator | Reduce Ratios to Simplest Form (A:B)"
    desc = "Simplify ratios into lowest integer terms using Euclid's GCD algorithm. Supports multi-term ratios (A:B:C), fractional and decimal inputs, aspect ratios, and scaling factors."
    h1 = "Ratio Simplifier Calculator"
    short_desc = "Reduce any two-term or multi-term ratio to its simplest primitive integer form, solve missing proportion values, and compute exact geometric scale factors."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Ratio Simplifier Calculator",
      "url": "https://calchub.com/ratio-simplifier-calculator.html",
      "applicationCategory": "EducationalApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Mathematical ratio reduction tool utilizing the Euclidean algorithm to simplify two-term and three-term ratios to lowest terms."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How do you simplify a ratio to lowest terms?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "To simplify an integer ratio A:B, find the Greatest Common Divisor (GCD) of both terms using the Euclidean algorithm, then divide both A and B by that GCD. The resulting integers have a GCD of 1, representing the ratio in its simplest primitive form."
          }
        },
        {
          "@type": "Question",
          "name": "How are decimal and fractional ratios simplified?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "For decimal ratios, multiply all terms by a power of 10 sufficient to convert every term into an integer (e.g., 2.5:1.25 multiplied by 100 becomes 250:125, which reduces to 2:1). For fractional ratios, multiply each term by the Least Common Multiple (LCM) of all denominators."
          }
        },
        {
          "@type": "Question",
          "name": "Can three-part ratios (A:B:C) be simplified?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. A three-part ratio A:B:C is simplified by computing the greatest common divisor across all three terms: GCD(A, B, C) = GCD(GCD(A, B), C). Each term is then divided by this joint divisor."
          }
        },
        {
          "@type": "Question",
          "name": "What is the difference between a ratio and a proportion?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A ratio expresses the relative magnitude or comparative relationship between two quantities (A:B). A proportion is a mathematical equation stating that two distinct ratios are equal (A/B = C/D)."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-grid">
    <div class="calc-inputs">
        <div class="input-group">
            <label for="ratioA">Ratio Term A</label>
            <input type="number" id="ratioA" value="1920" step="any" class="input-field">
            <span class="input-hint">First quantity, integer or decimal (e.g., 1920 or 2.5)</span>
        </div>
        <div class="input-group">
            <label for="ratioB">Ratio Term B</label>
            <input type="number" id="ratioB" value="1080" step="any" class="input-field">
            <span class="input-hint">Second quantity, integer or decimal (e.g., 1080 or 1.25)</span>
        </div>
        <div class="input-group">
            <label for="ratioC">Optional Term C (Multi-part A:B:C)</label>
            <input type="number" id="ratioC" value="" placeholder="Optional 3rd term" step="any" class="input-field">
            <span class="input-hint">Leave blank for standard 2-term ratio (e.g., for concrete 1:2:4)</span>
        </div>
        <div class="input-group">
            <label for="scaleTarget">Solve Proportion: Target Term A</label>
            <input type="number" id="scaleTarget" value="" placeholder="e.g., Scale to new width" step="any" class="input-field">
            <span class="input-hint">Enter target value for A to calculate scaled B (Proportion solver)</span>
        </div>
    </div>
    <div class="calc-results">
        <div class="result-card primary-result">
            <div class="result-label">Simplest Integer Ratio</div>
            <div class="result-value" id="resSimplified">16 : 9</div>
            <div class="result-sub" id="resGCD">Greatest Common Divisor (GCD) = 120</div>
        </div>
        <div class="result-grid-mini" style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;margin-top:1rem;">
            <div class="result-card">
                <div class="result-label">Unit Ratio (1 : n)</div>
                <div class="result-value-sm" id="resUnitB">1 : 0.5625</div>
            </div>
            <div class="result-card">
                <div class="result-label">Unit Ratio (n : 1)</div>
                <div class="result-value-sm" id="resUnitA">1.7778 : 1</div>
            </div>
            <div class="result-card">
                <div class="result-label">Decimal Value (A / B)</div>
                <div class="result-value-sm" id="resDecimalVal">1.777778</div>
            </div>
            <div class="result-card">
                <div class="result-label">Percentage (A / (A+B))</div>
                <div class="result-value-sm" id="resPercent">64.00% : 36.00%</div>
            </div>
        </div>
        <div class="result-card" id="resProportionBox" style="margin-top:1rem;background:var(--bg-accent, #eff6ff);border-left:4px solid var(--brand-primary, #2563eb);display:none;">
            <div class="result-label">Scaled Equivalent Proportion</div>
            <div class="result-value" id="resScaled" style="color:var(--brand-primary, #2563eb);font-size:1.5rem;">A = 0 &rarr; B = 0</div>
            <div class="result-sub" id="resScaleFormula">Scale multiplier k = 1.0</div>
        </div>
    </div>
</div>
<script>
function gcd2(a, b) {
    a = Math.abs(a);
    b = Math.abs(b);
    while (b) {
        let t = b;
        b = a % b;
        a = t;
    }
    return a;
}

function calculateRatio() {
    let a = parseFloat(document.getElementById('ratioA').value);
    let b = parseFloat(document.getElementById('ratioB').value);
    let cStr = document.getElementById('ratioC').value.trim();
    let hasC = cStr !== '' && !isNaN(parseFloat(cStr));
    let c = hasC ? parseFloat(cStr) : null;
    let targetA = parseFloat(document.getElementById('scaleTarget').value);

    if (isNaN(a) || isNaN(b) || a <= 0 || b <= 0) return;
    if (hasC && c <= 0) return;

    // Convert potential decimals to integers by finding common multiplier
    function getDecimalPlaces(num) {
        const s = num.toString();
        const idx = s.indexOf('.');
        return idx >= 0 ? s.length - idx - 1 : 0;
    }

    let dPlaces = Math.max(getDecimalPlaces(a), getDecimalPlaces(b));
    if (hasC) dPlaces = Math.max(dPlaces, getDecimalPlaces(c));

    let multiplier = Math.pow(10, Math.min(dPlaces, 6));
    let intA = Math.round(a * multiplier);
    let intB = Math.round(b * multiplier);
    let intC = hasC ? Math.round(c * multiplier) : null;

    let commonDiv = gcd2(intA, intB);
    if (hasC) commonDiv = gcd2(commonDiv, intC);

    let simpA = intA / commonDiv;
    let simpB = intB / commonDiv;
    let simpC = hasC ? intC / commonDiv : null;

    if (hasC) {
        document.getElementById('resSimplified').innerText = `${simpA} : ${simpB} : ${simpC}`;
        document.getElementById('resGCD').innerText = `Multiplied by ${multiplier}, Common GCD = ${commonDiv}`;
        document.getElementById('resUnitB').innerText = `1 : ${(b/a).toFixed(4)} : ${(c/a).toFixed(4)}`;
        document.getElementById('resUnitA').innerText = `${(a/c).toFixed(4)} : ${(b/c).toFixed(4)} : 1`;
        document.getElementById('resDecimalVal').innerText = `N/A (Multi-term)`;
        const tot = a + b + c;
        document.getElementById('resPercent').innerText = `${((a/tot)*100).toFixed(1)}% : ${((b/tot)*100).toFixed(1)}% : ${((c/tot)*100).toFixed(1)}%`;
    } else {
        document.getElementById('resSimplified').innerText = `${simpA} : ${simpB}`;
        document.getElementById('resGCD').innerText = `Common Divisor (GCD) = ${commonDiv / (multiplier > 1 ? multiplier : 1)}`;
        document.getElementById('resUnitB').innerText = `1 : ${(b / a).toFixed(4)}`;
        document.getElementById('resUnitA').innerText = `${(a / b).toFixed(4)} : 1`;
        document.getElementById('resDecimalVal').innerText = (a / b).toFixed(6);
        const tot = a + b;
        document.getElementById('resPercent').innerText = `${((a/tot)*100).toFixed(2)}% : ${((b/tot)*100).toFixed(2)}%`;
    }

    // Proportion scaling
    const propBox = document.getElementById('resProportionBox');
    if (!isNaN(targetA) && targetA > 0) {
        propBox.style.display = 'block';
        const scaleFactor = targetA / a;
        const scaledB = b * scaleFactor;
        if (hasC) {
            const scaledC = c * scaleFactor;
            document.getElementById('resScaled').innerText = `${targetA} : ${scaledB.toFixed(2)} : ${scaledC.toFixed(2)}`;
        } else {
            document.getElementById('resScaled').innerText = `${targetA} : ${scaledB.toFixed(2)}`;
        }
        document.getElementById('resScaleFormula').innerText = `Scale Factor k = ${scaleFactor.toFixed(4)} (based on A = ${targetA})`;
    } else {
        propBox.style.display = 'none';
    }
}

['ratioA', 'ratioB', 'ratioC', 'scaleTarget'].forEach(id => {
    const el = document.getElementById(id);
    if (el) {
        el.addEventListener('input', calculateRatio);
        el.addEventListener('change', calculateRatio);
    }
});
window.addEventListener('DOMContentLoaded', calculateRatio);
</script>"""

    article = """<h2>Theoretical Principles of Ratio Simplification</h2>
<p>In classical number theory and applied mathematics, a ratio represents a quantitative quotient that expresses the proportional relationship between two or more commensurate magnitudes. For any two non-zero real numbers $A$ and $B$, the expression $A : B$ denotes that the first quantity contains $A / B$ times as many units as the second quantity.</p>

<p>A ratio is said to be in its <strong>simplest form</strong> (or primitive irreducible form) when all of its components are mutually coprime positive integers—meaning that their Greatest Common Divisor (GCD) is exactly 1:</p>

$$\gcd\left(\frac{A}{\gcd(A, B)}, \frac{B}{\gcd(A, B)}\right) = 1$$

<p>The reduction of an integer ratio $A : B$ directly utilizes the Euclidean Algorithm, an ancient iterative procedure founded on the principle that the greatest common divisor of two integers $a$ and $b$ (where $a > b$) also divides their algebraic remainder $a \bmod b$:</p>

$$\gcd(a, b) = \gcd(b, a \bmod b) \quad \text{iterated until } a \bmod b = 0$$

<p>Once $\gcd(A, B)$ is determined, the simplified terms $A'$ and $B'$ are evaluated via exact division:</p>

$$A' = \frac{A}{\gcd(A, B)}, \quad B' = \frac{B}{\gcd(A, B)}$$

<h2>Handling Non-Integer and Multi-Part Terms</h2>
<p>Practical scientific, engineering, and chemical applications frequently introduce quantities that are not integers, including rational fractions, empirical decimals, or multi-term compound mixtures.</p>

<h3>1. Decimal Ratios</h3>
<p>When terms contain fractional decimal digits (e.g., $3.75 : 1.25$), each term is magnified by an integer power of ten $10^k$, where $k$ matches the maximum number of decimal places present across all terms:</p>

$$k = \max(\text{decimals}(A), \text{decimals}(B))$$

$$A_{\text{int}} = A \times 10^k, \quad B_{\text{int}} = B \times 10^k$$

<p>The Euclidean reduction is subsequently performed on the resulting integers $A_{\text{int}}$ and $B_{\text{int}}$.</p>

<h3>2. Fractional Ratios</h3>
<p>For ratios expressed as fractions $p_1/q_1 : p_2/q_2$, the terms are unified by computing the Least Common Multiple (LCM) of the denominators:</p>

$$\text{LCM}(q_1, q_2) = \frac{q_1 \times q_2}{\gcd(q_1, q_2)}$$

<p>Multiplying each fraction by the joint denominator clears the fractional expressions:</p>

$$\left(\frac{p_1}{q_1} \times \text{LCM}\right) : \left(\frac{p_2}{q_2} \times \text{LCM}\right)$$

<h3>3. Multi-Term Ratios (A : B : C)</h3>
<p>For three-term or higher mixtures—such as standard concrete proportioning (cement : sand : aggregate) or mortar recipes—the overall GCD is derived associatively:</p>

$$\gcd(A, B, C) = \gcd(\gcd(A, B), C)$$

<p>Dividing every term by this global divisor yields the primitive three-term ratio.</p>

<h2>Standard Display Aspect Ratios and Comparative Matrix</h2>
<p>The most pervasive digital implementation of ratio simplification occurs in digital imaging, cinematography, and display engineering, where pixel dimensions are reduced to aspect ratios. The following table illustrates standard industry display standards and their mathematical reductions:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Format Name</th>
            <th>Native Resolution ($W \times H$)</th>
            <th>Greatest Common Divisor</th>
            <th>Simplified Aspect Ratio</th>
            <th>Decimal Aspect Ratio</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>VGA Standard</td><td>640 &times; 480</td><td>160</td><td>4 : 3</td><td>1.3333 : 1</td></tr>
        <tr><td>High Definition (720p)</td><td>1280 &times; 720</td><td>80</td><td>16 : 9</td><td>1.7778 : 1</td></tr>
        <tr><td>Full HD (1080p)</td><td>1920 &times; 1080</td><td>120</td><td>16 : 9</td><td>1.7778 : 1</td></tr>
        <tr><td>WUXGA Display</td><td>1920 &times; 1200</td><td>240</td><td>16 : 10 (8 : 5)</td><td>1.6000 : 1</td></tr>
        <tr><td>Ultra HD 4K</td><td>3840 &times; 2160</td><td>240</td><td>16 : 9</td><td>1.7778 : 1</td></tr>
        <tr><td>Cinema 4K (DCI)</td><td>4096 &times; 2160</td><td>256</td><td>256 : 135</td><td>1.8963 : 1</td></tr>
        <tr><td>Ultra-Wide Monitor</td><td>3440 &times; 1440</td><td>80</td><td>43 : 18 (&approx; 21:9)</td><td>2.3889 : 1</td></tr>
        <tr><td>Classic 35mm Film</td><td>36mm &times; 24mm</td><td>12</td><td>3 : 2</td><td>1.5000 : 1</td></tr>
    </tbody>
</table>

<h2>Continued Fractions and Rational Approximation of Real Ratios</h2>
<p>When physical measurements, irrational constants, or continuous engineering parameters yield non-integer ratios (such as $\pi : 1 \approx 3.14159265 : 1$ or the Golden Ratio $\phi : 1 \approx 1.61803399 : 1$), exact integer simplification is impossible because the true terms share no common measure (incommensurability). Under such conditions, applied mathematics utilizes <strong>Simple Continued Fractions</strong> to construct the best possible rational approximations.</p>

<p>Any real quotient $x = A / B$ can be expressed uniquely as a continued fraction expansion:</p>

$$x = a_0 + \frac{1}{a_1 + \frac{1}{a_2 + \frac{1}{a_3 + \dots}}}$$

<p>The partial convergents $p_k / q_k$ generated by truncating this infinite or long expansion at index $k$ provide the mathematically optimal integer ratios:</p>

$$p_k = a_k p_{k-1} + p_{k-2}, \quad q_k = a_k q_{k-1} + q_{k-2}$$

<p>By Dirichlet's Approximation Theorem, each convergent $p_k / q_k$ satisfies the inequality:</p>

$$\left| \frac{A}{B} - \frac{p_k}{q_k} \right| < \frac{1}{q_k^2}$$

<p>This formulation allows mechanical engineers designing gearbox tooth counts, astronomical clock gear trains, and architectural proportions to identify the most accurate integer gear ratios (e.g., approximating $\pi \approx 355 : 113$ with an error of less than $3 \times 10^{-7}$).</p>

<h2>Proportions and Scaling Multipliers</h2>
<p>A proportion equates two equivalent ratios: $A / B = C / D$. When one term is modified, all complementary terms must scale by the exact same linear factor $k$ to preserve dimensional symmetry:</p>

$$k = \frac{A_{\text{new}}}{A_{\text{original}}}$$

$$B_{\text{new}} = B_{\text{original}} \times k$$

<div class="worked-example-card">
    <h3>Worked Engineering Case Study: Concrete Mix Volumetric Scaling</h3>
    <p><strong>Scenario:</strong> A structural engineer is preparing a high-strength concrete mix batch for foundation footings. The design specification specifies a volumetric proportion of 350 kg cement, 700 kg sand, and 1,050 kg coarse crushed stone aggregate. The on-site mixer requires scaling down so that exactly 120 kg of cement is utilized per drum batch. Determine: (1) the simplest integer ratio of the mix, and (2) the exact quantities of sand and aggregate required for the 120 kg cement batch.</p>
    
    <div class="step-solution">
        <h4>Step 1: Formulate the Three-Part Integer Ratio</h4>
        <p>Raw mix: $350 : 700 : 1050$.</p>

        <h4>Step 2: Calculate the Greatest Common Divisor (GCD)</h4>
        <p>Using the Euclidean algorithm:</p>
        $$\gcd(350, 700) = 350 \quad (\text{since } 700 = 2 \times 350 + 0)$$
        $$\gcd(350, 1050) = 350 \quad (\text{since } 1050 = 3 \times 350 + 0)$$
        <p>Therefore, the global joint divisor is $\gcd(350, 700, 1050) = 350$.</p>

        <h4>Step 3: Reduce to Simplest Terms</h4>
        $$A' = \frac{350}{350} = 1, \quad B' = \frac{700}{350} = 2, \quad C' = \frac{1050}{350} = 3$$
        <p><strong>Simplified Ratio:</strong> $1 : 2 : 3$ (Standard M15 structural concrete specification).</p>

        <h4>Step 4: Scale the Proportion to 120 kg Cement Batch</h4>
        <p>Linear scale factor: $k = 120 / 1 = 120$.</p>
        <p>Required Sand: $B_{\text{scaled}} = 2 \times 120 = 240 \text{ kg}$.</p>
        <p>Required Aggregate: $C_{\text{scaled}} = 3 \times 120 = 360 \text{ kg}$.</p>
        <p><strong>Total Batch Mass:</strong> $120 + 240 + 360 = 720 \text{ kg}$.</p>
    </div>
</div>

<h2>Common Analytical Pitfalls with Ratios</h2>
<ol>
    <li><strong>Confusing Part-to-Part with Part-to-Whole Ratios:</strong> In a ratio of $1 : 4$, the first part does not represent $1/4$ ($25\%$) of the whole; it represents $1 / (1 + 4) = 1/5$ ($20\%$). The total number of constituent parts is $A + B$.</li>
    <li><strong>Unit Mismatch:</strong> Ratios are inherently dimensionless scalars, meaning that the input terms must share identical physical units prior to reduction. Comparing 500 millimeters to 2 meters requires converting 2 meters to 2,000 millimeters first ($500 : 2000 \implies 1 : 4$).</li>
    <li><strong>Floating Point Rounding Artifacts:</strong> Performing division before simplification in numerical code can introduce IEEE 754 precision noise (e.g., $1/3 \approx 0.3333333333333333$). The Euclidean algorithm must always operate directly on integer numerators and denominators to guarantee exact algebraic purity.</li>
</ol>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article, category_hub="math.html", category_name="Mathematics &amp; Utilities")


def main():
    h_html = gen_hours_calculator()
    with open(os.path.join(BASE_DIR, "hours-calculator.html"), "w", encoding="utf-8") as f:
        f.write(h_html)
    print("Generated hours-calculator.html successfully!")

    r_html = gen_ratio_simplifier()
    with open(os.path.join(BASE_DIR, "ratio-simplifier-calculator.html"), "w", encoding="utf-8") as f:
        f.write(r_html)
    print("Generated ratio-simplifier-calculator.html successfully!")

if __name__ == "__main__":
    main()
