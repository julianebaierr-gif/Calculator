# -*- coding: utf-8 -*-
"""
Generator for Batch 40 - Part 3
Tools:
5. months-between-dates-calculator.html (Calendar Month Difference, Fractional Days, Day-Count Conventions)
6. overtime-calculator.html (FLSA Regular Rate, Time-and-a-Half, California Daily Double Time)
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COMMON_TAIL = """    <footer class="site-footer">
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>About CalcHub</h4>
                    <p>CalcHub delivers peer-reviewed chronometric computing algorithms, astronomical date conversion systems, and payroll engines compliant with FLSA, ISO 8601, and statutory accounting standards.</p>
                </div>
                <div class="footer-col">
                    <h4>Chronometric &amp; Payroll Suites</h4>
                    <ul>
                        <li><a href="datetime.html">Date &amp; Time Utilities</a></li>
                        <li><a href="finance.html">Payroll &amp; Compensation</a></li>
                        <li><a href="math.html">Mathematics &amp; Statistics</a></li>
                        <li><a href="converter.html">Unit &amp; Chrono Converters</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Core Calculators</h4>
                    <ul>
                        <li><a href="months-between-dates-calculator.html">Months Between Dates</a></li>
                        <li><a href="overtime-calculator.html">Overtime Pay Calculator</a></li>
                        <li><a href="hours-calculator.html">Work Hours Calculator</a></li>
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
                <p>&copy; 2026 CalcHub. All rights reserved. Precision chronological and statutory compensation calculation algorithms.</p>
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
                        <li><a href="months-between-dates-calculator.html">Months Between Dates</a></li>
                        <li><a href="overtime-calculator.html">Overtime Pay Calculator</a></li>
                        <li><a href="hours-calculator.html">Work Hours Calculator</a></li>
                        <li><a href="decimal-time-calculator.html">Decimal Time Calculator</a></li>
                        <li><a href="date-calculator.html">Date Calculator</a></li>
                        <li><a href="business-days-calculator.html">Business Days Calculator</a></li>
                        <li><a href="countdown-calculator.html">Countdown Calculator</a></li>
                    </ul>
                </div>
            </aside>
        </div>
    </div>
{COMMON_TAIL}"""


# ===========================================================================
# TOOL 5: months-between-dates-calculator.html
# ===========================================================================
def gen_months_between_dates():
    slug = "months-between-dates-calculator"
    title = "Months Between Dates Calculator | Exact, Decimal & Day Counts"
    desc = "Calculate the exact number of calendar months and days between two dates. Compute decimal months, financial 30/360 day counts, and pediatric ages."
    h1 = "Months Between Dates Calculator"
    short_desc = "Compute the exact calendar month duration between two dates, including fractional decimal months, remaining residual days, and financial amortization convention breakdowns."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Months Between Dates Calculator",
      "url": "https://calchub.com/months-between-dates-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Calculates the exact number of months and residual days between any two calendar dates, with fractional month and financial convention analysis."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How do you calculate months between two dates with differing day numbers?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Count the full whole calendar months elapsed between the start day of the month and the end day of the month. If the end day is less than the start day, deduct one month and calculate the remaining residual days using the days in the previous month."
          }
        },
        {
          "@type": "Question",
          "name": "What is the average number of days in a month?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Across a standard Gregorian calendar year, the average month length is 365 / 12 = 30.4167 days. Accounting for the 400-year Gregorian cycle with leap years, the mean astronomical month is 365.2425 / 12 = 30.4369 days."
          }
        },
        {
          "@type": "Question",
          "name": "What is the 30/360 day-count convention for calculating months?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In commercial real estate and bond accounting, the 30/360 convention treats every month as having exactly 30 days and each year as 360 days. Months between dates is computed directly as ((Y2 - Y1)*360 + (M2 - M1)*30 + (D2 - D1)) / 30."
          }
        },
        {
          "@type": "Question",
          "name": "How is pediatric age in months calculated clinically?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Pediatricians track developmental milestones up to 24 or 36 months using exact calendar month anniversaries (e.g., born March 15 becomes exactly 6 months old on September 15)."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-body">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.25rem; margin-bottom: 1.5rem;">
        <div>
            <label for="startDate" style="font-weight: 600; font-size: 0.875rem;">Start Date:</label>
            <input type="date" id="startDate" class="input-field" value="2024-01-15">
        </div>
        <div>
            <label for="endDate" style="font-weight: 600; font-size: 0.875rem;">End Date:</label>
            <input type="date" id="endDate" class="input-field" value="2026-10-05">
        </div>
    </div>

    <div style="display: flex; gap: 0.75rem; margin-bottom: 1.5rem;">
        <button type="button" class="btn btn-primary" onclick="calculateMonthsBetween()">Calculate Months</button>
        <button type="button" class="btn btn-outline" onclick="setPresetDates('ytd')">This Year to Date</button>
        <button type="button" class="btn btn-outline" onclick="setPresetDates('1year')">1 Year from Today</button>
    </div>

    <div class="result-box" style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem;">
        <h3 style="margin-top: 0; color: #1e293b; font-size: 1.1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">Span &amp; Month Breakdown</h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Full Calendar Months</div>
                <div id="resFullMonths" style="font-size: 1.4rem; font-weight: 700; color: #2563eb;">32 Months</div>
                <div id="resResidualDays" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">+ 20 residual days</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Exact Decimal Months</div>
                <div id="resDecimalMonths" style="font-size: 1.4rem; font-weight: 700; color: #0f172a;">32.6452 mo</div>
                <div style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">Based on exact month lengths</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Years &amp; Months</div>
                <div id="resYearsMonths" style="font-size: 1.2rem; font-weight: 700; color: #059669;">2 yrs, 8 mos, 20 days</div>
                <div id="resTotalWeeks" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">142.1 weeks</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Total Elapsed Days</div>
                <div id="resTotalDays" style="font-size: 1.4rem; font-weight: 700; color: #7c3aed;">994 Days</div>
                <div id="resBond30360" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">30/360 Days: 980 days</div>
            </div>
        </div>

        <div style="margin-top: 1.25rem; padding-top: 1rem; border-top: 1px dashed #cbd5e1; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; font-size: 0.875rem;">
            <div>
                <span style="font-weight: 600; color: #475569;">Average 30.4375-Day Months:</span>
                <div id="resAvgMonths" style="font-weight: 700; color: #1e293b; font-size: 1rem;">32.657 mo</div>
            </div>
            <div>
                <span style="font-weight: 600; color: #475569;">Financial 30/360 Months:</span>
                <div id="resFinMonths" style="font-weight: 700; color: #1e293b; font-size: 1rem;">32.667 mo</div>
            </div>
            <div>
                <span style="font-weight: 600; color: #475569;">Pediatric Developmental Index:</span>
                <div id="resPediatric" style="font-weight: 700; color: #1e293b; font-size: 1rem;">32 completed months</div>
            </div>
        </div>
    </div>
</div>

<script>
function setPresetDates(type) {
    const today = new Date();
    const pad = (n) => String(n).padStart(2, '0');
    const toYMD = (d) => `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;

    if (type === 'ytd') {
        document.getElementById('startDate').value = `${today.getFullYear()}-01-01`;
        document.getElementById('endDate').value = toYMD(today);
    } else if (type === '1year') {
        document.getElementById('startDate').value = toYMD(today);
        const nextYr = new Date(today.getFullYear() + 1, today.getMonth(), today.getDate());
        document.getElementById('endDate').value = toYMD(nextYr);
    }
    calculateMonthsBetween();
}

function daysInMonth(year, month) {
    // month is 1-based (1..12)
    return new Date(year, month, 0).getDate();
}

function calculateMonthsBetween() {
    const sStr = document.getElementById('startDate').value;
    const eStr = document.getElementById('endDate').value;
    if (!sStr || !eStr) return;

    let d1 = new Date(sStr + 'T00:00:00');
    let d2 = new Date(eStr + 'T00:00:00');

    let inverted = false;
    if (d1 > d2) {
        const tmp = d1;
        d1 = d2;
        d2 = tmp;
        inverted = true;
    }

    const y1 = d1.getFullYear();
    const m1 = d1.getMonth(); // 0-based
    const day1 = d1.getDate();

    const y2 = d2.getFullYear();
    const m2 = d2.getMonth();
    const day2 = d2.getDate();

    // Calendar month calculation
    let fullYears = y2 - y1;
    let fullMonths = m2 - m1;
    let residualDays = day2 - day1;

    if (residualDays < 0) {
        fullMonths -= 1;
        // Previous month days relative to d2
        let prevM = m2 - 1;
        let prevY = y2;
        if (prevM < 0) {
            prevM = 11;
            prevY -= 1;
        }
        const dimPrev = daysInMonth(prevY, prevM + 1);
        residualDays += dimPrev;
    }

    if (fullMonths < 0) {
        fullYears -= 1;
        fullMonths += 12;
    }

    const totalFullMonths = (fullYears * 12) + fullMonths;

    // Fractional month based on days in the residual month
    const dimEnd = daysInMonth(y2, m2 + 1);
    const frac = residualDays / dimEnd;
    const decimalMonths = totalFullMonths + frac;

    // Total days elapsed
    const diffMs = Math.abs(d2 - d1);
    const totalDays = Math.round(diffMs / (1000 * 60 * 60 * 24));
    const totalWeeks = (totalDays / 7).toFixed(1);

    // Average 30.4375-day months
    const avgMonths = (totalDays / 30.4375).toFixed(3);

    // 30/360 bond convention
    const bondDays = ((y2 - y1) * 360) + ((m2 - m1) * 30) + (day2 - day1);
    const finMonths = (bondDays / 30).toFixed(3);

    const prefix = inverted ? " (Inverted Range)" : "";
    document.getElementById('resFullMonths').innerText = `${totalFullMonths} Months${prefix}`;
    document.getElementById('resResidualDays').innerText = `+ ${residualDays} residual days`;
    document.getElementById('resDecimalMonths').innerText = `${decimalMonths.toFixed(4)} mo`;
    document.getElementById('resYearsMonths').innerText = `${fullYears} yrs, ${fullMonths} mos, ${residualDays} days`;
    document.getElementById('resTotalWeeks').innerText = `${totalWeeks} weeks`;
    document.getElementById('resTotalDays').innerText = `${totalDays.toLocaleString()} Days`;
    document.getElementById('resBond30360').innerText = `30/360 Days: ${bondDays.toLocaleString()} days`;

    document.getElementById('resAvgMonths').innerText = `${avgMonths} mo`;
    document.getElementById('resFinMonths').innerText = `${finMonths} mo`;
    document.getElementById('resPediatric').innerText = `${totalFullMonths} completed months (${decimalMonths.toFixed(1)} mo adjusted)`;
}

window.addEventListener('DOMContentLoaded', () => {
    document.getElementById('startDate').addEventListener('change', calculateMonthsBetween);
    document.getElementById('endDate').addEventListener('change', calculateMonthsBetween);
    calculateMonthsBetween();
});
</script>"""

    article = """<h2>Calendrical Theory of Measuring Month Durations</h2>
<p>Calculating the precise duration between two calendar dates in units of <strong>months</strong> presents unique mathematical challenges not found in metric SI measurements. While physical units such as seconds, meters, and kilograms are invariant constants, the Gregorian calendar month is an irregular piecewise continuum varying from 28 to 31 days. Consequently, there is no single universal definition of a "month difference"; rather, computing elapsed months requires selecting between exact astronomical, calendar anniversary, or statutory financial conventions.</p>

<p>The standard chronometric algorithm for computing integer whole calendar months and residual days between start date $(Y_1, M_1, D_1)$ and end date $(Y_2, M_2, D_2)$ is formulated as follows:</p>

$$\Delta M_{\text{raw}} = (Y_2 - Y_1) \times 12 + (M_2 - M_1)$$

<p>If the terminal day of the month has not yet reached the starting anniversary ($D_2 < D_1$), the full month count must be decremented by 1, and the residual day count borrows the total days from the preceding month:</p>

$$\Delta M_{\text{full}} = \begin{cases} 
\Delta M_{\text{raw}} & \text{if } D_2 \ge D_1 \\ 
\Delta M_{\text{raw}} - 1 & \text{if } D_2 < D_1 
\end{cases}$$

$$\Delta D_{\text{residual}} = \begin{cases} 
D_2 - D_1 & \text{if } D_2 \ge D_1 \\ 
D_2 - D_1 + \text{DaysInMonth}(Y_{\text{prev}}, M_{\text{prev}}) & \text{if } D_2 < D_1 
\end{cases}$$

<p>Where $\text{DaysInMonth}(Y, M) \in \{28, 29, 30, 31\}$. The fractional decimal month duration is then evaluated by dividing the residual days by the denominator of the bounding month:</p>

$$\Delta M_{\text{decimal}} = \Delta M_{\text{full}} + \frac{\Delta D_{\text{residual}}}{\text{DaysInMonth}(Y_2, M_2)}$$

<h2>Financial and Regulatory Day-Count Conventions</h2>
<p>In structured debt securities, corporate commercial paper, mortgage amortizations, and municipal bonds, legal indenture contracts mandate specific day-count conventions to eliminate month-length anomalies. Three standard financial frameworks dictate how months are quantified:</p>

<h3>1. The 30/360 US Bond Basis (NASD Convention)</h3>
<p>Under the 30/360 convention, every calendar year is artificially standardized to 360 days, and every month is treated as containing exactly 30 days. Day differences evaluate according to the linear formula:</p>

$$\text{Days}_{30/360} = (Y_2 - Y_1) \times 360 + (M_2 - M_1) \times 30 + (D_2 - D_1)$$
$$\text{Months}_{30/360} = \frac{\text{Days}_{30/360}}{30}$$

<p>If $D_1$ is 31, it is changed to 30. If $D_2$ is 31 and $D_1 \ge 30$, $D_2$ is changed to 30. This ensures perfectly uniform monthly interest coupons on 30-year fixed mortgages regardless of whether February has 28 or 29 days.</p>

<h3>2. Actual/Actual ICMA Standard</h3>
<p>Prevalent in US Treasury bonds and European sovereign debt, Actual/Actual measures the exact number of calendar days between coupon payments divided by the exact number of days in the payment period multiplied by the annual frequency. In a leap year, a semi-annual period spanning February contains 182 days, whereas in a common year it contains 181 days.</p>

<h3>3. Average Astronomical Month (Mean Solar Month)</h3>
<p>In epidemiological research and demographic modeling, elapsed days $\Delta D_{\text{actual}}$ are divided by the mean Gregorian month length across the 400-year cycle:</p>

$$\bar{M}_{\text{Gregorian}} = \frac{365.2425}{12} \approx 30.436875 \text{ days}$$
$$\Delta M_{\text{astronomical}} = \frac{\Delta D_{\text{actual}}}{30.436875}$$

<h3>Comparative Month Duration Conventions Matrix</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Convention Name</th>
            <th>Primary Application</th>
            <th>Assumed Month Length</th>
            <th>Year Divisor</th>
            <th>Leap Year Impact</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Calendar Anniversary</td><td>Pediatrics, Birthdays, Age Tracking</td><td>Variable (28–31 days)</td><td>365 / 366 days</td><td>Captured on Feb 29</td></tr>
        <tr><td>30/360 US (NASD)</td><td>Corporate Bonds, Mortgages</td><td>Fixed 30.00 days</td><td>360 days</td><td>Ignored (Treated as 30)</td></tr>
        <tr><td>Actual/360</td><td>Commercial Loans, Money Markets</td><td>Actual elapsed days</td><td>360 days</td><td>Adds 1 interest day in Feb</td></tr>
        <tr><td>Actual/365 Fixed</td><td>Consumer Credit Lines, UK Gilts</td><td>Actual elapsed days</td><td>365 days</td><td>Adds 1 interest day in Feb</td></tr>
        <tr><td>Mean Gregorian</td><td>Demographics, Scientific Studies</td><td>Fixed 30.4369 days</td><td>365.2425 days</td><td>Uniform smoothed average</td></tr>
    </tbody>
</table>

<h2>Clinical and Developmental Applications in Pediatrics</h2>
<p>The World Health Organization (WHO) and American Academy of Pediatrics (AAP) track infant growth velocity, head circumference percentiles, and developmental milestones (gross motor, fine motor, expressive language) strictly in completed chronological months up to age 24 months, and subsequent 6-month intervals up to age 5.</p>
<p>For premature neonates born prior to 37 gestational weeks, clinicians compute <strong>Adjusted Age in Months</strong>:</p>

$$\text{Age}_{\text{adjusted}} = \text{Chronological Age (months)} - \left( \frac{40 - \text{Gestational Weeks at Birth}}{4.348} \right)$$

<p>This prevents false diagnosis of cognitive or physical development delays by measuring developmental progress against post-conceptual maturity rather than the civil birth date.</p>

<div class="worked-example-card">
    <h3>Worked Financial Case Study: Commercial Real Estate Lease Duration</h3>
    <p><strong>Scenario:</strong> A technology corporation executes a commercial headquarters office lease commencing on <strong>January 15, 2024</strong> and terminating on <strong>October 5, 2026</strong>. Determine: (1) full calendar months and residual days, (2) exact decimal months, (3) 30/360 bond months for rent amortizations, and (4) total elapsed days spanning the 2024 leap year.</p>
    
    <div class="step-solution">
        <h4>Step 1: Calculate Calendar Month Offset</h4>
        <p>Year offset: $2026 - 2024 = 2 \text{ years} = 24 \text{ months}$.</p>
        <p>Month offset: October (Month 10) minus January (Month 1) $= 9 \text{ months}$.</p>
        <p>Raw months: $24 + 9 = 33 \text{ months}$.</p>

        <h4>Step 2: Adjust for Day Difference</h4>
        <p>Start day: 15. End day: 5. Because $5 < 15$, deduct 1 month: $33 - 1 = 32 \text{ full months}$.</p>
        <p>Residual days: September has 30 days. Borrowing from September: $(5 - 15) + 30 = 20 \text{ residual days}$.</p>
        <p><strong>Calendar Span:</strong> 32 whole months and 20 days (or 2 years, 8 months, 20 days).</p>

        <h4>Step 3: Evaluate Exact Decimal Months</h4>
        <p>Terminal month (October) contains 31 days. Fractional component: $20 / 31 \approx 0.6452$.</p>
        $$\Delta M_{\text{decimal}} = 32 + 0.6452 = 32.6452 \text{ months}$$

        <h4>Step 4: Compute 30/360 Financial Basis</h4>
        $$\text{Days}_{30/360} = (2 \times 360) + (9 \times 30) + (5 - 15) = 720 + 270 - 10 = 980 \text{ days}$$
        $$\text{Months}_{30/360} = \frac{980}{30} \approx 32.6667 \text{ months}$$

        <h4>Step 5: Compute Actual Elapsed Days</h4>
        <p>2024 is a leap year (366 days). Total calendar days elapsed $= 994 \text{ actual days}$.</p>
    </div>
</div>

<h2>Common Calculation Errors and Implementation Pitfalls</h2>
<ol>
    <li><strong>Assuming All Months Have 30 Days:</strong> Dividing total elapsed days by 30 produces substantial distortion over long spans. Over a 5-year duration (1,826 days), dividing by 30 yields 60.87 months, whereas dividing by 30.4375 yields exactly 59.99 months.</li>
    <li><strong>End-of-Month (EOM) Boundary Paradox:</strong> What is the interval between January 31st and February 28th? In legal contracts, February 28th is considered exactly 1 full calendar month from January 31st because both represent the terminal day of their respective months. Naive day subtraction yields $28 - 31 = -3 \text{ days}$, introducing an artificial month deficit.</li>
    <li><strong>Timezone Normalization Errors:</strong> Comparing timestamps generated in UTC against local Daylight Saving Time can alter the apparent start or end day, causing integer month calculations to drift by a full month.</li>
</ol>

<section class="faq-section">
    <h2>Frequently Asked Questions About Months Between Dates</h2>
    <div class="faq-item">
        <h3>How do you calculate months between two dates with differing day numbers?</h3>
        <p>Count the full whole calendar months elapsed between the start day of the month and the end day of the month. If the end day is less than the start day, deduct one month and calculate the remaining residual days using the days in the previous month.</p>
    </div>
    <div class="faq-item">
        <h3>What is the average number of days in a month?</h3>
        <p>Across a standard Gregorian calendar year, the average month length is 365 / 12 = 30.4167 days. Accounting for the 400-year Gregorian cycle with leap years, the mean astronomical month is 365.2425 / 12 = 30.4369 days.</p>
    </div>
    <div class="faq-item">
        <h3>What is the 30/360 day-count convention for calculating months?</h3>
        <p>In commercial real estate and bond accounting, the 30/360 convention treats every month as having exactly 30 days and each year as 360 days. Months between dates is computed directly as ((Y2 - Y1)*360 + (M2 - M1)*30 + (D2 - D1)) / 30.</p>
    </div>
    <div class="faq-item">
        <h3>How is pediatric age in months calculated clinically?</h3>
        <p>Pediatricians track developmental milestones up to 24 or 36 months using exact calendar month anniversaries (e.g., born March 15 becomes exactly 6 months old on September 15).</p>
    </div>
</section>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article)


# ===========================================================================
# TOOL 6: overtime-calculator.html
# ===========================================================================
def gen_overtime():
    slug = "overtime-calculator"
    title = "Overtime Pay Calculator | FLSA Regular Rate, Time-and-a-Half & Double Time"
    desc = "Calculate overtime pay under FLSA rules, including time-and-a-half (1.5x), California daily double time (2.0x), non-discretionary bonuses, and blended hourly rates."
    h1 = "Overtime Pay Calculator"
    short_desc = "Precision payroll computation for overtime wages under US FLSA statutory guidelines, California daily double-time labor codes, and weighted regular rates of pay."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Overtime Pay Calculator",
      "url": "https://calchub.com/overtime-calculator.html",
      "applicationCategory": "FinanceApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Calculates overtime pay, regular rate of pay, time-and-a-half, California double time, and blended bonus earnings."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How is time-and-a-half overtime calculated under the FLSA?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Under the federal Fair Labor Standards Act (FLSA), overtime is paid at 1.5 times the employee's regular rate of pay for all hours worked exceeding 40 in a single standard 7-day workweek."
          }
        },
        {
          "@type": "Question",
          "name": "What is the Regular Rate of Pay when bonuses or commissions are included?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The regular rate of pay is calculated by dividing total remuneration (base wages plus non-discretionary bonuses, commissions, and shift differentials) by total hours worked in the workweek. Overtime is then paid on this higher blended rate."
          }
        },
        {
          "@type": "Question",
          "name": "How does California daily overtime and double time work?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Under California Labor Code 510, non-exempt employees earn 1.5x pay for hours worked over 8 up to 12 in a single day, and 2.0x (double time) for all hours worked beyond 12 in a single workday."
          }
        },
        {
          "@type": "Question",
          "name": "Can an employer waive overtime pay by paying a flat salary?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. An employee is only exempt from overtime if they satisfy both the statutory salary threshold and specific administrative, professional, or executive duties tests mandated by the Department of Labor."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-body">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.25rem; margin-bottom: 1.5rem;">
        <div>
            <label for="baseHourlyRate" style="font-weight: 600; font-size: 0.875rem;">Base Hourly Rate ($):</label>
            <input type="number" id="baseHourlyRate" class="input-field" value="28.50" min="0" step="0.50">
            <span class="input-hint">Contractual base straight-time rate</span>
        </div>
        <div>
            <label for="totalHoursWorked" style="font-weight: 600; font-size: 0.875rem;">Total Workweek Hours:</label>
            <input type="number" id="totalHoursWorked" class="input-field" value="48.5" min="0" max="168" step="0.25">
            <span class="input-hint">Total clock hours in the 7-day workweek</span>
        </div>
        <div>
            <label for="nondiscBonus" style="font-weight: 600; font-size: 0.875rem;">Weekly Bonus / Commission ($):</label>
            <input type="number" id="nondiscBonus" class="input-field" value="150.00" min="0" step="10.00">
            <span class="input-hint">Non-discretionary bonus or incentive pay</span>
        </div>
        <div>
            <label for="calcMode" style="font-weight: 600; font-size: 0.875rem;">Overtime Jurisdiction Standard:</label>
            <select id="calcMode" class="input-field">
                <option value="flsa">Federal FLSA Standard (> 40 hrs/wk @ 1.5x)</option>
                <option value="ca_daily">California Daily (> 8h @ 1.5x, > 12h @ 2.0x)</option>
                <option value="custom_double">Custom Overtime + Double Time</option>
            </select>
        </div>
    </div>

    <!-- Specific Daily Inputs for California Mode -->
    <div id="caDailyWrapper" style="display: none; background: white; border: 1px solid #e2e8f0; border-radius: 6px; padding: 1rem; margin-bottom: 1.5rem;">
        <h4 style="margin-top: 0; font-size: 0.95rem; color: #1e293b;">Daily Hours Distribution (Past 7 Days):</h4>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 0.5rem;">
            <div><label style="font-size: 0.75rem;">Mon</label><input type="number" id="dMon" class="input-field" value="10" min="0" max="24" step="0.5"></div>
            <div><label style="font-size: 0.75rem;">Tue</label><input type="number" id="dTue" class="input-field" value="13" min="0" max="24" step="0.5"></div>
            <div><label style="font-size: 0.75rem;">Wed</label><input type="number" id="dWed" class="input-field" value="9" min="0" max="24" step="0.5"></div>
            <div><label style="font-size: 0.75rem;">Thu</label><input type="number" id="dThu" class="input-field" value="8.5" min="0" max="24" step="0.5"></div>
            <div><label style="font-size: 0.75rem;">Fri</label><input type="number" id="dFri" class="input-field" value="8" min="0" max="24" step="0.5"></div>
            <div><label style="font-size: 0.75rem;">Sat</label><input type="number" id="dSat" class="input-field" value="0" min="0" max="24" step="0.5"></div>
            <div><label style="font-size: 0.75rem;">Sun</label><input type="number" id="dSun" class="input-field" value="0" min="0" max="24" step="0.5"></div>
        </div>
    </div>

    <div style="display: flex; gap: 0.75rem; margin-bottom: 1.5rem;">
        <button type="button" class="btn btn-primary" onclick="calculateOvertime()">Calculate Overtime</button>
        <button type="button" class="btn btn-outline" onclick="setOvertimePreset(45)">45 Hours Shift</button>
        <button type="button" class="btn btn-outline" onclick="setOvertimePreset(55)">55 Hours Shift</button>
    </div>

    <div class="result-box" style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem;">
        <h3 style="margin-top: 0; color: #1e293b; font-size: 1.1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">Gross Wage &amp; Overtime Breakdown</h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Total Gross Pay</div>
                <div id="resTotalGross" style="font-size: 1.5rem; font-weight: 700; color: #16a34a;">$1,678.96</div>
                <div id="resBlendedRate" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">Blended Regular Rate: $31.59/hr</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Regular Wages</div>
                <div id="resRegWages" style="font-size: 1.4rem; font-weight: 700; color: #0f172a;">$1,140.00</div>
                <div id="resRegHours" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">40.0 hrs @ $28.50/hr</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Overtime Wages (1.5x)</div>
                <div id="resOtWages" style="font-size: 1.4rem; font-weight: 700; color: #2563eb;">$388.96</div>
                <div id="resOtHours" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">8.5 hrs @ $45.76/hr</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Double Time Wages (2.0x)</div>
                <div id="resDtWages" style="font-size: 1.4rem; font-weight: 700; color: #7c3aed;">$0.00</div>
                <div id="resDtHours" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">0.0 hrs @ $0.00/hr</div>
            </div>
        </div>

        <div style="margin-top: 1.25rem; padding-top: 1rem; border-top: 1px dashed #cbd5e1; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; font-size: 0.875rem;">
            <div>
                <span style="font-weight: 600; color: #475569;">Incentive / Bonus Pay Included:</span>
                <div id="resBonusEcho" style="font-weight: 700; color: #1e293b; font-size: 1rem;">$150.00</div>
            </div>
            <div>
                <span style="font-weight: 600; color: #475569;">Effective Average Pay Rate:</span>
                <div id="resEffectiveAvg" style="font-weight: 700; color: #1e293b; font-size: 1rem;">$34.62 / hour worked</div>
            </div>
            <div>
                <span style="font-weight: 600; color: #475569;">Overtime Premium Lift:</span>
                <div id="resPremiumLift" style="font-weight: 700; color: #1e293b; font-size: 1rem;">+$134.28 above straight time</div>
            </div>
        </div>
    </div>
</div>

<script>
function setOvertimePreset(hrs) {
    document.getElementById('totalHoursWorked').value = hrs;
    calculateOvertime();
}

function calculateOvertime() {
    const baseRate = parseFloat(document.getElementById('baseHourlyRate').value) || 0;
    const bonus = parseFloat(document.getElementById('nondiscBonus').value) || 0;
    const mode = document.getElementById('calcMode').value;

    const caWrapper = document.getElementById('caDailyWrapper');
    caWrapper.style.display = (mode === 'ca_daily') ? 'block' : 'none';

    let totalHrs = 0;
    let regHrs = 0;
    let otHrs = 0;
    let dtHrs = 0;

    if (mode === 'ca_daily') {
        const days = ['dMon', 'dTue', 'dWed', 'dThu', 'dFri', 'dSat', 'dSun'];
        days.forEach(id => {
            const h = parseFloat(document.getElementById(id).value) || 0;
            totalHrs += h;
            if (h <= 8) {
                regHrs += h;
            } else if (h <= 12) {
                regHrs += 8;
                otHrs += (h - 8);
            } else {
                regHrs += 8;
                otHrs += 4;
                dtHrs += (h - 12);
            }
        });
        document.getElementById('totalHoursWorked').value = totalHrs.toFixed(1);
    } else {
        totalHrs = parseFloat(document.getElementById('totalHoursWorked').value) || 0;
        if (totalHrs <= 40) {
            regHrs = totalHrs;
            otHrs = 0;
            dtHrs = 0;
        } else {
            regHrs = 40;
            otHrs = totalHrs - 40;
            dtHrs = 0;
        }
    }

    if (totalHrs <= 0) {
        document.getElementById('resTotalGross').innerText = '$0.00';
        return;
    }

    // FLSA Regular Rate of Pay formulation
    // Straight time total earnings = (Total Hours * Base Rate) + Bonus
    const straightTimeEarnings = (totalHrs * baseRate) + bonus;
    const regularRateOfPay = straightTimeEarnings / totalHrs;

    // Overtime premiums (0.5x regular rate for OT, 1.0x for DT because straight time is already counted)
    const otPremiumRate = regularRateOfPay * 1.5;
    const dtPremiumRate = regularRateOfPay * 2.0;

    const regPay = regHrs * baseRate;
    const otPay = otHrs * (baseRate * 1.5) + (otHrs * (bonus / totalHrs) * 0.5);
    const dtPay = dtHrs * (baseRate * 2.0) + (dtHrs * (bonus / totalHrs) * 1.0);

    const totalGross = (regHrs * baseRate) + (otHrs * baseRate * 1.5) + (dtHrs * baseRate * 2.0) + bonus + ((otHrs * 0.5 + dtHrs * 1.0) * (bonus / totalHrs));
    const effectiveAvg = totalGross / totalHrs;
    const straightNoBonus = totalHrs * baseRate;
    const premiumLift = totalGross - straightNoBonus - bonus;

    document.getElementById('resTotalGross').innerText = `$${totalGross.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}`;
    document.getElementById('resBlendedRate').innerText = `Blended Regular Rate: $${regularRateOfPay.toFixed(2)}/hr`;
    document.getElementById('resRegWages').innerText = `$${regPay.toFixed(2)}`;
    document.getElementById('resRegHours').innerText = `${regHrs.toFixed(1)} hrs @ $${baseRate.toFixed(2)}/hr`;
    document.getElementById('resOtWages').innerText = `$${otPay.toFixed(2)}`;
    document.getElementById('resOtHours').innerText = `${otHrs.toFixed(1)} hrs @ $${(baseRate * 1.5 + (bonus/totalHrs)*0.5).toFixed(2)}/hr`;
    document.getElementById('resDtWages').innerText = `$${dtPay.toFixed(2)}`;
    document.getElementById('resDtHours').innerText = `${dtHrs.toFixed(1)} hrs @ $${(baseRate * 2.0 + (bonus/totalHrs)*1.0).toFixed(2)}/hr`;

    document.getElementById('resBonusEcho').innerText = `$${bonus.toFixed(2)}`;
    document.getElementById('resEffectiveAvg').innerText = `$${effectiveAvg.toFixed(2)} / hr worked`;
    document.getElementById('resPremiumLift').innerText = `+$${premiumLift.toFixed(2)} premium above straight`;
}

window.addEventListener('DOMContentLoaded', () => {
    ['baseHourlyRate', 'totalHoursWorked', 'nondiscBonus', 'calcMode', 'dMon', 'dTue', 'dWed', 'dThu', 'dFri', 'dSat', 'dSun'].forEach(id => {
        const el = document.getElementById(id);
        if (el) {
            el.addEventListener('input', calculateOvertime);
            el.addEventListener('change', calculateOvertime);
        }
    });
    calculateOvertime();
});
</script>"""

    article = """<h2>Statutory Foundations of Overtime Compensation Under the FLSA</h2>
<p>The legal framework governing employee overtime compensation in the United States was established by Congress under the <strong>Fair Labor Standards Act (FLSA)</strong> of 1938 (29 U.S.C. § 207). Under federal law, non-exempt employees must receive overtime compensation for all hours worked in excess of 40 hours during a designated seven-day workweek at a rate not less than <strong>one and one-half times ($1.5\times$)</strong> their regular rate of pay.</p>

<p>The primary statutory objective of the FLSA was twofold: to discourage employers from imposing excessively burdensome hours on individual workers, and to financially incentivize the hiring of additional labor across the national workforce.</p>

<h2>The Regular Rate of Pay Formulation (29 U.S.C. § 207(e))</h2>
<p>The single most contentious and legally litigated area of payroll compliance involves determining the true <strong>Regular Rate of Pay ($R_{\text{reg}}$)</strong>. Many employers mistakenly compute overtime simply by multiplying the contractual base hourly wage $R_{\text{base}}$ by 1.5. However, under Section 207(e) of the FLSA and 29 CFR Part 778, the regular rate must encompass <em>all remuneration for employment paid to, or on behalf of, the employee</em>.</p>

<p>When an employee earns non-discretionary bonuses (e.g., attendance bonuses, safety awards, production quotas), commission payments, or shift differentials ($B_{\text{nondisc}}$), the regular rate must be recalculated as a weighted blended rate across all hours worked during that workweek ($H_{\text{total}}$):</p>

$$R_{\text{reg}} = \frac{(H_{\text{total}} \times R_{\text{base}}) + B_{\text{nondisc}}}{H_{\text{total}}} = R_{\text{base}} + \frac{B_{\text{nondisc}}}{H_{\text{total}}}$$

<p>Because the straight-time portion of the employee's compensation is already captured in the initial wage and bonus summation, the employer must pay an additional <strong>overtime premium</strong> of half-time ($0.5 \times R_{\text{reg}}$) for each overtime hour $H_{\text{ot}}$:</p>

$$W_{\text{ot\_premium}} = H_{\text{ot}} \times 0.5 \times R_{\text{reg}}$$

$$\text{Gross Pay} = (H_{\text{total}} \times R_{\text{base}}) + B_{\text{nondisc}} + \left( H_{\text{ot}} \times 0.5 \times R_{\text{reg}} \right)$$

<h2>State-Specific Daily Overtime and Double-Time Statutes</h2>
<p>While federal FLSA regulations impose overtime exclusively on weekly aggregates exceeding 40 hours, several state jurisdictions enforce strict daily overtime thresholds:</p>

<h3>1. California Labor Code § 510</h3>
<p>California maintains the most rigorous statutory overtime scheme in the United States. Under California Labor Code Section 510:</p>
<ul>
    <li><strong>Daily Overtime (1.5x):</strong> Any work beyond 8 hours up to and including 12 hours in any single workday, and the first 8 hours worked on the seventh consecutive day of work in a workweek.</li>
    <li><strong>Daily Double Time (2.0x):</strong> Any work beyond 12 hours in any single workday, and all hours worked beyond 8 hours on the seventh consecutive day of work in a workweek.</li>
    <li><strong>Weekly Overtime (1.5x):</strong> Any work beyond 40 hours in a workweek.</li>
</ul>

<h3>2. Alaska, Colorado, and Nevada Daily Thresholds</h3>
<p>Alaska requires overtime ($1.5\times$) for work exceeding 8 hours per day for employers with four or more employees. Colorado enforces overtime after 12 hours per workday or 12 consecutive hours regardless of the start of the workday. Nevada mandates daily overtime after 8 hours (or 10 hours for 4-day compressed workweeks) for employees whose base wage is less than 1.5 times the state minimum wage.</p>

<h3>State-by-State Overtime Statutory Comparison Matrix</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Jurisdiction</th>
            <th>Weekly OT Threshold</th>
            <th>Daily OT Threshold (1.5x)</th>
            <th>Daily Double Time (2.0x)</th>
            <th>7th Consecutive Day Rule</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Federal (FLSA)</td><td>40 Hours</td><td>None</td><td>None</td><td>None</td></tr>
        <tr><td>California</td><td>40 Hours</td><td>&gt; 8 to 12 Hours</td><td>&gt; 12 Hours</td><td>First 8h @ 1.5x; &gt; 8h @ 2.0x</td></tr>
        <tr><td>Alaska</td><td>40 Hours</td><td>&gt; 8 Hours</td><td>None</td><td>None</td></tr>
        <tr><td>Colorado</td><td>40 Hours</td><td>&gt; 12 Hours</td><td>None</td><td>None</td></tr>
        <tr><td>Nevada</td><td>40 Hours</td><td>&gt; 8 Hours (if &lt; 1.5x Min Wage)</td><td>None</td><td>None</td></tr>
        <tr><td>New York</td><td>40 Hours</td><td>None</td><td>None</td><td>None</td></tr>
    </tbody>
</table>

<h2>Exempt vs. Non-Exempt Classification Rules</h2>
<p>Employees are not automatically exempt from overtime simply by receiving a fixed salary or possessing a managerial title. To be classified as exempt from overtime under the FLSA, an employee must satisfy both the <strong>Salary Basis Test</strong> and the specific <strong>Duties Test</strong> defined by Department of Labor (DOL) regulations:</p>
<ul>
    <li><strong>Salary Level Test:</strong> The employee must receive a guaranteed, pre-determined salary meeting the federal statutory minimum threshold (annually adjusted under DOL regulations).</li>
    <li><strong>Executive Exemption:</strong> Primary duty must be management of the enterprise or a recognized subdivision, regularly directing the work of two or more full-time employees, with authority to hire or fire.</li>
    <li><strong>Administrative Exemption:</strong> Primary duty must be performance of office or non-manual work directly related to the management or general business operations, requiring the exercise of discretion and independent judgment.</li>
    <li><strong>Professional Exemption:</strong> Primary duty requires advanced knowledge in a field of science or learning acquired by a prolonged course of specialized intellectual instruction (e.g., engineers, physicians, certified accountants).</li>
</ul>

<div class="worked-example-card">
    <h3>Worked Corporate Payroll Case Study: Industrial Technician with Nondiscretionary Production Bonus</h3>
    <p><strong>Scenario:</strong> A precision turbine technician in Texas earns a base hourly wage of $28.50. During an emergency plant turnaround, the technician works <strong>48.5 hours</strong> in a single workweek and earns an additional <strong>$150.00</strong> non-discretionary safety and turnaround completion bonus. Calculate: (1) straight-time earnings, (2) regular rate of pay ($R_{\text{reg}}$), (3) overtime premium due, and (4) total gross compensation.</p>
    
    <div class="step-solution">
        <h4>Step 1: Compute Total Straight-Time Earnings</h4>
        $$\text{Hourly Straight Pay} = 48.5 \times \$28.50 = \$1,382.25$$
        $$\text{Total Straight Earnings} = \$1,382.25 + \$150.00 = \$1,532.25$$

        <h4>Step 2: Calculate Regular Rate of Pay ($R_{\text{reg}}$)</h4>
        $$R_{\text{reg}} = \frac{\$1,532.25}{48.5 \text{ hours}} \approx \$31.5928 \text{ per hour}$$

        <h4>Step 3: Evaluate Overtime Hours and Premium</h4>
        $$H_{\text{ot}} = 48.5 - 40.0 = 8.5 \text{ overtime hours}$$
        $$\text{Half-Time Overtime Premium Rate} = 0.5 \times \$31.5928 \approx \$15.7964 \text{ per hour}$$
        $$\text{Overtime Premium Amount} = 8.5 \times \$15.7964 \approx \$134.27$$

        <h4>Step 4: Compute Total Gross Pay</h4>
        $$\text{Total Gross Pay} = \text{Total Straight Earnings} + \text{Overtime Premium}$$
        $$\text{Total Gross Pay} = \$1,532.25 + \$134.27 = \$1,666.52$$
        <p><strong>Compliance Insight:</strong> If the employer had unlawfully excluded the $150 bonus from the regular rate, the technician would have received only $8.5 \times (0.5 \times 28.50) = \$121.13$ in overtime premium, resulting in a statutory wage violation and liability for back-wages plus liquidated damages.</p>
    </div>
</div>

<h2>Common Payroll Compliance Pitfalls in Overtime Computation</h2>
<ol>
    <li><strong>Excluding Non-Discretionary Incentive Bonuses from Regular Rate:</strong> By far the most frequent source of multi-million dollar class-action wage lawsuits. Discretionary bonuses (such as unexpected holiday gifts not tied to contracts or hours) can be excluded, but any bonus tied to production, attendance, safety, or quality must be folded into the regular rate.</li>
    <li><strong>Compensatory ("Comp") Time Off in Private Sector:</strong> Private employers cannot offer compensatory time off in lieu of paying cash overtime wages. Comp time agreements are legal exclusively for public sector government agencies under strict FLSA limitations.</li>
    <li><strong>Averaging Hours Across Multi-Week Pay Periods:</strong> Employers on biweekly pay periods cannot average hours across the two-week cycle (e.g., working 50 hours in Week 1 and 30 hours in Week 2 is NOT 80 regular hours; the employee is legally owed 10 hours of overtime pay for Week 1).</li>
</ol>

<section class="faq-section">
    <h2>Frequently Asked Questions About Overtime Pay</h2>
    <div class="faq-item">
        <h3>How is time-and-a-half overtime calculated under the FLSA?</h3>
        <p>Under the federal Fair Labor Standards Act (FLSA), overtime is paid at 1.5 times the employee's regular rate of pay for all hours worked exceeding 40 in a single standard 7-day workweek.</p>
    </div>
    <div class="faq-item">
        <h3>What is the Regular Rate of Pay when bonuses or commissions are included?</h3>
        <p>The regular rate of pay is calculated by dividing total remuneration (base wages plus non-discretionary bonuses, commissions, and shift differentials) by total hours worked in the workweek. Overtime is then paid on this higher blended rate.</p>
    </div>
    <div class="faq-item">
        <h3>How does California daily overtime and double time work?</h3>
        <p>Under California Labor Code 510, non-exempt employees earn 1.5x pay for hours worked over 8 up to 12 in a single day, and 2.0x (double time) for all hours worked beyond 12 in a single workday.</p>
    </div>
    <div class="faq-item">
        <h3>Can an employer waive overtime pay by paying a flat salary?</h3>
        <p>No. An employee is only exempt from overtime if they satisfy both the statutory salary threshold and specific administrative, professional, or executive duties tests mandated by the Department of Labor.</p>
    </div>
</section>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article, category_hub="finance.html", category_name="Finance &amp; Payroll")


def main():
    mb_html = gen_months_between_dates()
    with open(os.path.join(BASE_DIR, "months-between-dates-calculator.html"), "w", encoding="utf-8") as f:
        f.write(mb_html)
    print("Generated months-between-dates-calculator.html successfully!")

    ot_html = gen_overtime()
    with open(os.path.join(BASE_DIR, "overtime-calculator.html"), "w", encoding="utf-8") as f:
        f.write(ot_html)
    print("Generated overtime-calculator.html successfully!")

if __name__ == "__main__":
    main()
