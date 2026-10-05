# -*- coding: utf-8 -*-
"""
Generator for Batch 39 - Part 4
Tools:
7. countdown-calculator.html (Target Date/Time Countdown, Live Ticks, Days/Hrs/Mins/Secs)
8. date-calculator.html (Date Differences, Add/Subtract Intervals, Month Clamping)
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COMMON_TAIL = """    <footer class="site-footer">
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>About CalcHub</h4>
                    <p>CalcHub provides peer-reviewed chronometric software, astronomical date conversion models, and high-frequency countdown engines compliant with ISO 8601 and international UTC timekeeping standards.</p>
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
                        <li><a href="countdown-calculator.html">Event Countdown Timer</a></li>
                        <li><a href="date-calculator.html">Date Calculator</a></li>
                        <li><a href="business-days-calculator.html">Business Days Calculator</a></li>
                        <li><a href="hours-calculator.html">Work Hours Calculator</a></li>
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
                        <li><a href="countdown-calculator.html">Countdown Calculator</a></li>
                        <li><a href="date-calculator.html">Date Calculator</a></li>
                        <li><a href="business-days-calculator.html">Business Days Calculator</a></li>
                        <li><a href="hours-calculator.html">Work Hours Calculator</a></li>
                        <li><a href="week-number-calculator.html">ISO Week Number</a></li>
                        <li><a href="add-days-to-date-calculator.html">Add Days to Date</a></li>
                        <li><a href="add-time-calculator.html">Add Time Calculator</a></li>
                        <li><a href="date-difference-calculator.html">Date Difference</a></li>
                    </ul>
                </div>
            </aside>
        </div>
    </div>
{COMMON_TAIL}"""


# ===========================================================================
# TOOL 7: countdown-calculator.html
# ===========================================================================
def gen_countdown_calculator():
    slug = "countdown-calculator"
    title = "Countdown Calculator | Days, Hours, Minutes & Seconds to Date"
    desc = "Track the exact remaining time until any future date or event with real-time dynamic countdown ticks, timezone offsets, and total weeks, hours, minutes, and seconds breakdowns."
    h1 = "Countdown Calculator"
    short_desc = "Calculate the remaining days, hours, minutes, and seconds until any milestone event with live high-precision chronometric countdown progression."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Countdown Calculator",
      "url": "https://calchub.com/countdown-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Real-time chronometric countdown timer calculating remaining days, hours, minutes, and seconds to any target date."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How is the countdown between current time and target date calculated?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The calculation takes the target timestamp in UTC milliseconds, subtracts the current system time, and decomposes the remaining milliseconds into discrete integer units: days (86,400,000 ms), hours (3,600,000 ms), minutes (60,000 ms), and seconds (1,000 ms)."
          }
        },
        {
          "@type": "Question",
          "name": "How does the countdown handle Daylight Saving Time (DST) changes?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Because the countdown operates on absolute UTC epoch timestamps, transitions across Daylight Saving Time boundaries are naturally integrated. A 23-hour 'spring-forward' or 25-hour 'fall-back' day correctly counts down the exact physical elapsed hours."
          }
        },
        {
          "@type": "Question",
          "name": "Can you count down to a specific time of day as well as a date?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. The calculator accepts both a calendar date and a specific time of day (HH:MM), enabling second-by-second precision for product launches, exam start times, sporting events, and scheduled travel departures."
          }
        },
        {
          "@type": "Question",
          "name": "What happens when the target countdown date has passed?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "When the target timestamp occurs in the past, the engine automatically switches into 'Elapsed Since' mode, displaying the exact time that has elapsed since the milestone occurred."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-grid">
    <div class="calc-inputs">
        <div class="input-group">
            <label for="eventName">Event Title</label>
            <input type="text" id="eventName" value="New Year's Day 2027" class="input-field">
            <span class="input-hint">Name of milestone, holiday, or launch</span>
        </div>
        <div class="input-group">
            <label for="targetDateInput">Target Calendar Date</label>
            <input type="date" id="targetDateInput" class="input-field">
            <span class="input-hint">Select the future target date</span>
        </div>
        <div class="input-group">
            <label for="targetTimeInput">Target Time of Day</label>
            <input type="time" id="targetTimeInput" value="00:00" class="input-field">
            <span class="input-hint">Exact hour and minute of the event</span>
        </div>
        <div style="display:flex;gap:0.5rem;flex-wrap:wrap;margin-top:0.5rem;">
            <button type="button" class="btn-outline" onclick="setCountdownPreset('newyear')">New Year</button>
            <button type="button" class="btn-outline" onclick="setCountdownPreset(7)">+7 Days</button>
            <button type="button" class="btn-outline" onclick="setCountdownPreset(30)">+30 Days</button>
            <button type="button" class="btn-outline" onclick="setCountdownPreset(100)">+100 Days</button>
            <button type="button" class="btn-outline" onclick="setCountdownPreset('summer')">Summer Solstice</button>
        </div>
    </div>
    <div class="calc-results">
        <div class="result-card primary-result">
            <div class="result-label" id="resCountdownLabel">Time Remaining Until Event</div>
            <div class="result-value" id="resCountdownMain" style="font-size:2rem;letter-spacing:1px;font-variant-numeric:tabular-nums;">87d 07h 29m 14s</div>
            <div class="result-sub" id="resTargetFormatted">Target: Friday, Jan 01, 2027 at 00:00:00</div>
        </div>
        <div class="result-grid-mini" style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;margin-top:1rem;">
            <div class="result-card">
                <div class="result-label">Total Full Weeks</div>
                <div class="result-value-sm" id="resTotalWeeks">12.4 Weeks</div>
            </div>
            <div class="result-card">
                <div class="result-label">Total Elapsed Hours</div>
                <div class="result-value-sm" id="resTotalHours">2,095 Hours</div>
            </div>
            <div class="result-card">
                <div class="result-label">Total Minutes</div>
                <div class="result-value-sm" id="resTotalMins">125,729 Mins</div>
            </div>
            <div class="result-card">
                <div class="result-label">Total Seconds</div>
                <div class="result-value-sm" id="resTotalSecs">7,543,754 Secs</div>
            </div>
        </div>
        <div class="result-card" style="margin-top:1rem;background:var(--bg-accent, #eff6ff);border-left:4px solid var(--brand-primary, #2563eb);">
            <div class="result-label">Perspective &amp; Biological Milestone</div>
            <div class="result-value" id="resPerspective" style="color:var(--brand-primary, #2563eb);font-size:1.25rem;">Approximately 8.8 Million Human Heartbeats</div>
            <div class="result-sub" id="resSleepNights">Encompasses 87 sleep periods / nights</div>
        </div>
    </div>
</div>
<script>
let timerInterval = null;

function updateCountdown() {
    const dStr = document.getElementById('targetDateInput').value;
    const tStr = document.getElementById('targetTimeInput').value || '00:00';
    const evName = document.getElementById('eventName').value.trim() || 'Target Event';

    if (!dStr) return;

    const [y, m, d] = dStr.split('-').map(Number);
    const [th, tm] = tStr.split(':').map(Number);

    const target = new Date(y, m - 1, d, th, tm, 0);
    const now = new Date();

    const diffMs = target - now;
    const isPast = diffMs < 0;
    const absDiffSec = Math.floor(Math.abs(diffMs) / 1000);

    const days = Math.floor(absDiffSec / 86400);
    const remSec1 = absDiffSec % 86400;
    const hours = Math.floor(remSec1 / 3600);
    const remSec2 = remSec1 % 3600;
    const minutes = Math.floor(remSec2 / 60);
    const seconds = remSec2 % 60;

    const pad = (n) => String(n).padStart(2, '0');

    document.getElementById('resCountdownLabel').innerText = isPast ? `Time Elapsed Since: ${evName}` : `Time Remaining Until: ${evName}`;
    document.getElementById('resCountdownMain').innerText = `${days}d ${pad(hours)}h ${pad(minutes)}m ${pad(seconds)}s`;

    const options = { weekday: 'long', month: 'short', day: '2-digit', year: 'numeric' };
    document.getElementById('resTargetFormatted').innerText = `Target: ${target.toLocaleDateString('en-US', options)} at ${pad(th)}:${pad(tm)}:00`;

    const totWeeks = (absDiffSec / (86400 * 7)).toFixed(1);
    const totHours = Math.floor(absDiffSec / 3600);
    const totMins = Math.floor(absDiffSec / 60);

    document.getElementById('resTotalWeeks').innerText = `${totWeeks} Weeks (${days} Days)`;
    document.getElementById('resTotalHours').innerText = `${totHours.toLocaleString()} Hours`;
    document.getElementById('resTotalMins').innerText = `${totMins.toLocaleString()} Minutes`;
    document.getElementById('resTotalSecs').innerText = `${absDiffSec.toLocaleString()} Seconds`;

    const heartbeats = Math.round(totMins * 72); // baseline 72 bpm
    document.getElementById('resPerspective').innerText = `Approx. ${heartbeats.toLocaleString()} Human Heartbeats (@ 72 bpm)`;
    document.getElementById('resSleepNights').innerText = `Encompasses ${days} sleep cycles / circadian nights`;
}

function setCountdownPreset(type) {
    const today = new Date();
    let target = new Date();

    if (type === 'newyear') {
        target = new Date(today.getFullYear() + 1, 0, 1, 0, 0, 0);
        document.getElementById('eventName').value = `New Year's Day ${today.getFullYear() + 1}`;
    } else if (type === 'summer') {
        target = new Date(today.getFullYear(), 5, 21, 0, 0, 0);
        if (target < today) target = new Date(today.getFullYear() + 1, 5, 21, 0, 0, 0);
        document.getElementById('eventName').value = `Summer Solstice`;
    } else if (typeof type === 'number') {
        target.setDate(today.getDate() + type);
        document.getElementById('eventName').value = `${type}-Day Milestone`;
    }

    const y = target.getFullYear();
    const m = String(target.getMonth() + 1).padStart(2, '0');
    const d = String(target.getDate()).padStart(2, '0');
    document.getElementById('targetDateInput').value = `${y}-${m}-${d}`;
    updateCountdown();
}

window.addEventListener('DOMContentLoaded', () => {
    const today = new Date();
    const nextYear = new Date(today.getFullYear() + 1, 0, 1);
    const y = nextYear.getFullYear();
    const m = String(nextYear.getMonth() + 1).padStart(2, '0');
    const d = String(nextYear.getDate()).padStart(2, '0');
    document.getElementById('targetDateInput').value = `${y}-${m}-${d}`;

    ['targetDateInput', 'targetTimeInput', 'eventName'].forEach(id => {
        document.getElementById(id).addEventListener('input', updateCountdown);
        document.getElementById(id).addEventListener('change', updateCountdown);
    });

    updateCountdown();
    if (timerInterval) clearInterval(timerInterval);
    timerInterval = setInterval(updateCountdown, 1000);
});
</script>"""

    article = """<h2>Mathematical Formulation of Real-Time Countdown Systems</h2>
<p>In computational chronometry, a countdown timer calculates the exact vector difference between a continuous dynamic current timestamp $T_{\text{now}}$ and an invariant future target epoch $T_{\text{target}}$. Although frequently presented as a simplistic visual interface, accurate countdown engines must navigate non-trivial challenges associated with client-server clock desynchronization, Coordinated Universal Time (UTC) epoch transformations, and multi-scale dimensional unit decomposition.</p>

<p>The total physical temporal interval $\Delta t$ between $T_{\text{now}}$ and $T_{\text{target}}$ is initially quantified as an absolute scalar in milliseconds:</p>

$$\Delta t_{\text{ms}} = T_{\text{target}} - T_{\text{now}}$$

<p>When $\Delta t_{\text{ms}} > 0$, the event lies in the future. The total discrete duration in integer seconds is obtained via floor division:</p>

$$\Delta t_{\text{sec}} = \left\lfloor \frac{\Delta t_{\text{ms}}}{1000} \right\rfloor$$

<p>To map this scalar into user-readable sexagesimal positional components—days ($D$), hours ($H$), minutes ($M$), and seconds ($S$)—the algorithm applies nested modulo and floor operations:</p>

$$D = \left\lfloor \frac{\Delta t_{\text{sec}}}{86400} \right\rfloor$$

$$H = \left\lfloor \frac{\Delta t_{\text{sec}} \bmod 86400}{3600} \right\rfloor$$

$$M = \left\lfloor \frac{\Delta t_{\text{sec}} \bmod 3600}{60} \right\rfloor$$

$$S = \Delta t_{\text{sec}} \bmod 60$$

<p>Where $86400 = 24 \times 3600$ represents the total number of SI seconds in a civil solar day, and $3600$ represents the seconds in a single hour.</p>

<h2>Timezone Normalization and Epoch Alignment</h2>
<p>A frequent error in countdown implementations stems from local timezone ambiguities. If a global software release is scheduled for <code>2027-01-01 00:00:00 UTC</code>, a client browser operating in New York (Eastern Standard Time, UTC-5) must not evaluate the target as midnight local time. The countdown engine must normalize both timestamps to absolute Unix Epoch time (milliseconds elapsed since January 1, 1970 00:00:00 UTC):</p>

$$T_{\text{epoch}} = (\text{YearDays} + \text{LeapDays}) \times 86400 + (H \times 3600) + (M \times 60) + S - \text{TZ}_{\text{offset}}$$

<p>Because Unix Epoch time is intrinsically monotonic and timezone-agnostic, the resulting countdown is physically identical regardless of whether the user views the display from Tokyo, London, or San Francisco.</p>

<h3>Daylight Saving Time (DST) Invariance</h3>
<p>When a countdown spans across a Daylight Saving Time boundary—such as the March "spring-forward" transition where a civil day contains only 23 hours, or the November "fall-back" transition where a civil day contains 25 hours—naive countdown algorithms that assume every day contains 24.0 civil hours introduce a 1-hour jump in remaining time. By anchoring calculations in absolute UTC epoch milliseconds, the true physical countdown progresses without disruption.</p>

<h2>High-Frequency Precision Time: Monotonic Clocks vs. Wall-Clock Time</h2>
<p>In real-time software engineering, JavaScript web applications, and embedded digital displays, computing countdown increments using standard wall-clock interfaces (such as <code>new Date()</code>) exposes the system to non-linear clock jumps. Wall-clock time is subject to Network Time Protocol (NTP) slewing, manual operating system time adjustments, and leap second insertions. When an NTP daemon adjusts the local system clock backward by several milliseconds, wall-clock countdown timers can register frozen or backward intervals.</p>

<p>To achieve high-frequency jitter-free rendering (such as sub-frame 60 FPS / 120 FPS animations), modern web applications combine wall-clock target resolution with the <strong>Monotonic Clock</strong> provided by the W3C High Resolution Time API (<code>window.performance.now()</code>):</p>

$$\Delta t_{\text{monotonic}} = \text{TargetEpoch}_{\text{UTC}} - \big( T_{\text{origin}} + \text{performance.now()} \big)$$

<p>Because monotonic clocks never decrease and are independent of system clock modifications, countdown animations maintain sub-millisecond smoothness without displaying visual stutter.</p>

<h2>Nanosecond Synchronizations and IEEE 1588 PTP Protocols</h2>
<p>In high-frequency algorithmic financial trading (HFT), power grid phasor measurement units (PMUs), and distributed particle accelerators (such as CERN), countdown synchronization operates beyond seconds into nanosecond regimes ($10^{-9} \text{ s}$). Under standard NTP over commercial wide-area networks, timing uncertainty hovers between $1$ and $50$ milliseconds. To synchronize distributed nodes with sub-microsecond precision, enterprise engineering deploys the <strong>IEEE 1588 Precision Time Protocol (PTP)</strong>.</p>

<p>IEEE 1588 utilizes hardware packet timestamping at the physical network interface layer (PHY), measuring mean round-trip path delays ($\delta$) and clock offsets ($\theta$) via bidirectional message exchange:</p>

$$\delta = \frac{(t_2 - t_1) + (t_4 - t_3)}{2}, \quad \theta = \frac{(t_2 - t_1) - (t_4 - t_3)}{2}$$

<p>This protocol enables distributed clusters to coordinate simultaneous market orders or launch triggers with synchronization variances bounded within under $100 \text{ nanoseconds}$.</p>

<h3>Milestone Countdown Comparison Matrix</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Annual Global Milestone</th>
            <th>Canonical Date (UTC)</th>
            <th>Diurnal Characteristic</th>
            <th>Typical Advance Planning Horizon</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>New Year's Day</td><td>January 1</td><td>Global Holiday Epoch</td><td>365 Days (1 Year)</td></tr>
        <tr><td>Vernal Equinox</td><td>March 20 &ndash; 21</td><td>Equal Day &amp; Night ($\odot = 0^\circ$)</td><td>90 Days (Quarterly)</td></tr>
        <tr><td>Summer Solstice</td><td>June 20 &ndash; 21</td><td>Longest Solar Day in North</td><td>180 Days (Semi-Annual)</td></tr>
        <tr><td>Autumnal Equinox</td><td>September 22 &ndash; 23</td><td>Equal Day &amp; Night ($\odot = 180^\circ$)</td><td>90 Days (Quarterly)</td></tr>
        <tr><td>Winter Solstice</td><td>December 21 &ndash; 22</td><td>Shortest Solar Day in North</td><td>180 Days (Semi-Annual)</td></tr>
        <tr><td>Intercalary Leap Day</td><td>February 29</td><td>Quadrennial Gregorian Correction</td><td>1,461 Days (4 Years)</td></tr>
    </tbody>
</table>

<div class="worked-example-card">
    <h3>Worked Aerospace Case Study: Rocket Launch Countdown Sequencing</h3>
    <p><strong>Scenario:</strong> The European Space Agency (ESA) schedules an Ariane 6 satellite launch from the Guiana Space Centre in Kourou, French Guiana for <strong>October 15, 2026 at 14:30:00 UTC</strong>. The flight operations director monitors the mission clock on <strong>October 12, 2026 at 08:15:30 UTC</strong>. Determine: (1) exact remaining days, hours, minutes, and seconds, and (2) total cumulative remaining minutes until T-zero.</p>
    
    <div class="step-solution">
        <h4>Step 1: Calculate Elapsed Span in Days and Hours</h4>
        <p>From Oct 12, 08:15:30 to Oct 15, 08:15:30 is exactly 3 full days ($3 \times 86400 = 259,200 \text{ s}$).</p>
        <p>From 08:15:30 to 14:30:00 on Oct 15:</p>
        <ul>
            <li>08:15:30 to 08:30:00 = 14 mins 30 secs = 870 seconds.</li>
            <li>08:30:00 to 14:30:00 = 6 hours = 21,600 seconds.</li>
            <li>Subtotal = 22,470 seconds = 6 hours, 14 minutes, 30 seconds.</li>
        </ul>

        <h4>Step 2: Aggregate Total Remaining Seconds</h4>
        $$\Delta t_{\text{sec}} = 259,200 + 22,470 = 281,670 \text{ seconds}$$

        <h4>Step 3: Decompose into Standard Countdown Form</h4>
        $$D = \lfloor 281,670 / 86400 \rfloor = 3 \text{ days}$$
        $$\text{Remainder} = 281,670 \bmod 86400 = 22,470 \text{ seconds}$$
        $$H = \lfloor 22,470 / 3600 \rfloor = 6 \text{ hours}$$
        $$\text{Remainder} = 22,470 \bmod 3600 = 870 \text{ seconds}$$
        $$M = \lfloor 870 / 60 \rfloor = 14 \text{ minutes}$$
        $$S = 870 \bmod 60 = 30 \text{ seconds}$$
        <p><strong>Countdown Display:</strong> <code>L-03d 06h 14m 30s</code>.</p>

        <h4>Step 4: Compute Total Equivalent Minutes</h4>
        $$\text{Total Minutes} = \frac{281,670}{60} = 4,694.50 \text{ minutes}$$
    </div>
</div>

<h2>Common Implementation Bugs in Countdown Applications</h2>
<ol>
    <li><strong>Client System Clock Drift:</strong> Browsers evaluate <code>new Date()</code> using the local operating system clock. If the user's computer clock is manually altered or drifts by 5 minutes, client-side countdowns exhibit an identical 5-minute offset. High-reliability countdowns synchronize periodically with Network Time Protocol (NTP) servers via WebSocket or HTTP HEAD headers.</li>
    <li><strong>Timer Drift and Browser Tab Throttling:</strong> JavaScript <code>setInterval()</code> calls are heavily throttled by modern web browsers when a browser tab is placed in the background (slowing from 1,000 ms to 10,000 ms or more to conserve mobile battery). Resilient countdown engines re-query real clock time on every tick rather than simply decrementing an internal counter variable.</li>
    <li><strong>Failure to Transition to Negative (Elapsed) Time:</strong> Without proper conditional branching, timers that cross T-zero may wrap around to display nonsensical negative numbers (e.g., <code>-1d -2h</code>) instead of cleanly entering an elapsed timeline format.</li>
</ol>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article)


# ===========================================================================
# TOOL 8: date-calculator.html
# ===========================================================================
def gen_date_calculator():
    slug = "date-calculator"
    title = "Date Calculator | Days Between Dates, Add or Subtract Calendar Intervals"
    desc = "Calculate the exact duration between two dates in years, months, weeks, and days, or add and subtract calendar intervals with automatic month clamping and leap year logic."
    h1 = "Date Calculator"
    short_desc = "Compute precise chronological durations between calendar dates, or project future and past dates by adding or subtracting years, months, weeks, and days."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Date Calculator",
      "url": "https://calchub.com/date-calculator.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Multi-mode Gregorian date calculator computing elapsed time between dates and projecting future/past dates with calendar intervals."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How does the date calculator borrow days across months of different lengths?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "When the day of the end date is less than the day of the start date, the algorithm borrows days from the preceding month. The number of borrowed days exactly matches the actual length of that specific preceding month (28 or 29 for February, 30, or 31 days)."
          }
        },
        {
          "@type": "Question",
          "name": "What is the end-of-month clamping rule when adding months?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "When adding one month to January 31, the mathematical target February 31 does not exist. The algorithm applies standard clamping, adjusting the resulting date to the final valid day of the target month (February 28, or February 29 during a leap year)."
          }
        },
        {
          "@type": "Question",
          "name": "Does the calculator include both the start date and end date?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "By default, duration calculations measure the exact elapsed time between dates (excluding the start date). However, an option is provided to include both boundary dates for legal, leasing, and contractual compliance."
          }
        },
        {
          "@type": "Question",
          "name": "How are leap years factored into date difference calculations?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The calculation engine uses exact astronomical Gregorian calendrical rules. Any leap year crossed in the date span automatically accounts for the intercalary February 29th, ensuring 100% precision."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-grid">
    <div class="calc-inputs">
        <div class="input-group">
            <label for="dateCalcMode">Calculation Mode</label>
            <select id="dateCalcMode" class="input-field">
                <option value="diff" selected>Duration Between Two Dates (Date 1 &rarr; Date 2)</option>
                <option value="project">Add / Subtract Intervals (Start Date &plusmn; Y/M/W/D)</option>
            </select>
            <span class="input-hint">Select between duration analysis or forward/backward projection</span>
        </div>
        <div id="diffInputs">
            <div class="input-group">
                <label for="dDate1">Start Date (Date 1)</label>
                <input type="date" id="dDate1" class="input-field">
                <span class="input-hint">Initial baseline calendar date</span>
            </div>
            <div class="input-group">
                <label for="dDate2">End Date (Date 2)</label>
                <input type="date" id="dDate2" class="input-field">
                <span class="input-hint">Secondary target calendar date</span>
            </div>
            <div class="input-group">
                <label for="dIncludeEnd">Boundary Inclusion</label>
                <select id="dIncludeEnd" class="input-field">
                    <option value="standard" selected>Standard Elapsed Span (Exclude Start Date)</option>
                    <option value="inclusive">Inclusive Count (Include Both Boundary Dates)</option>
                </select>
                <span class="input-hint">Standard interval vs inclusive contract duration</span>
            </div>
        </div>
        <div id="projectInputs" style="display:none;">
            <div class="input-group">
                <label for="pStartDate">Anchor Date</label>
                <input type="date" id="pStartDate" class="input-field">
                <span class="input-hint">Starting calendar date</span>
            </div>
            <div class="input-group">
                <label for="pOperation">Direction</label>
                <select id="pOperation" class="input-field">
                    <option value="add" selected>+ Add (Forward in Time)</option>
                    <option value="sub">- Subtract (Backward in Time)</option>
                </select>
            </div>
            <div class="input-group">
                <label>Intervals to Offset</label>
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.5rem;margin-bottom:0.5rem;">
                    <input type="number" id="pYears" value="1" min="0" placeholder="Years" class="input-field">
                    <input type="number" id="pMonths" value="6" min="0" placeholder="Months" class="input-field">
                </div>
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.5rem;">
                    <input type="number" id="pWeeks" value="0" min="0" placeholder="Weeks" class="input-field">
                    <input type="number" id="pDays" value="15" min="0" placeholder="Days" class="input-field">
                </div>
                <span class="input-hint">Years, Months, Weeks, Days</span>
            </div>
        </div>
    </div>
    <div class="calc-results">
        <div class="result-card primary-result">
            <div class="result-label" id="resDatePrimaryLabel">Computed Calendar Duration</div>
            <div class="result-value" id="resDatePrimaryVal" style="font-size:1.75rem;">1 Year, 6 Months, 15 Days</div>
            <div class="result-sub" id="resDateTotalDays">Total: 563 Calendar Days</div>
        </div>
        <div class="result-grid-mini" style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;margin-top:1rem;">
            <div class="result-card">
                <div class="result-label">Total Full Weeks</div>
                <div class="result-value-sm" id="resDateWeeks">80.4 Weeks</div>
            </div>
            <div class="result-card">
                <div class="result-label">Total Hours</div>
                <div class="result-value-sm" id="resDateHours">13,512 Hours</div>
            </div>
            <div class="result-card">
                <div class="result-label">Total Minutes</div>
                <div class="result-value-sm" id="resDateMinutes">810,720 Mins</div>
            </div>
            <div class="result-card">
                <div class="result-label">Total Seconds</div>
                <div class="result-value-sm" id="resDateSeconds">48,643,200 Secs</div>
            </div>
        </div>
        <div class="result-card" style="margin-top:1rem;background:var(--bg-accent, #eff6ff);border-left:4px solid var(--brand-primary, #2563eb);">
            <div class="result-label">Astronomical &amp; Solar Perspective</div>
            <div class="result-value" id="resSolarPerspective" style="color:var(--brand-primary, #2563eb);font-size:1.25rem;">1.542 Solar Tropical Years</div>
            <div class="result-sub" id="resSolarPercent">15.42% of a standard decade elapsed</div>
        </div>
    </div>
</div>
<script>
function daysInMonth(y, m) {
    return new Date(y, m + 1, 0).getDate();
}

function updateDateCalculator() {
    const mode = document.getElementById('dateCalcMode').value;
    document.getElementById('diffInputs').style.display = (mode === 'diff') ? 'block' : 'none';
    document.getElementById('projectInputs').style.display = (mode === 'project') ? 'block' : 'none';

    if (mode === 'diff') {
        const d1Str = document.getElementById('dDate1').value;
        const d2Str = document.getElementById('dDate2').value;
        const incMode = document.getElementById('dIncludeEnd').value;

        if (!d1Str || !d2Str) return;

        let [y1, m1, d1] = d1Str.split('-').map(Number);
        let [y2, m2, d2] = d2Str.split('-').map(Number);

        let dt1 = new Date(y1, m1 - 1, d1);
        let dt2 = new Date(y2, m2 - 1, d2);

        if (dt2 < dt1) {
            let ty = y1, tm = m1, td = d1;
            y1 = y2; m1 = m2; d1 = d2;
            y2 = ty; m2 = tm; d2 = td;
            let tdt = dt1; dt1 = dt2; dt2 = tdt;
        }

        // Exact calendar Y-M-D decomposition
        let curY = y2 - y1;
        let curM = (m2 - 1) - (m1 - 1);
        let curD = d2 - d1;

        if (curD < 0) {
            // Borrow days from previous month
            let prevM = (m2 - 2 + 12) % 12;
            let prevY = (m2 === 1) ? y2 - 1 : y2;
            let borrowDays = daysInMonth(prevY, prevM);
            curD += borrowDays;
            curM -= 1;
        }

        if (curM < 0) {
            curM += 12;
            curY -= 1;
        }

        let totalDays = Math.round((dt2 - dt1) / 86400000);
        if (incMode === 'inclusive') {
            totalDays += 1;
            curD += 1;
        }

        const weeks = (totalDays / 7).toFixed(1);
        const hours = totalDays * 24;
        const minutes = hours * 60;
        const seconds = minutes * 60;
        const tropicalYears = (totalDays / 365.2422).toFixed(3);

        document.getElementById('resDatePrimaryLabel').innerText = 'Computed Calendar Duration';
        document.getElementById('resDatePrimaryVal').innerText = `${curY} Year${curY !== 1 ? 's' : ''}, ${curM} Month${curM !== 1 ? 's' : ''}, ${curD} Day${curD !== 1 ? 's' : ''}`;
        document.getElementById('resDateTotalDays').innerText = `Total: ${totalDays.toLocaleString()} Calendar Days`;
        document.getElementById('resDateWeeks').innerText = `${weeks} Weeks`;
        document.getElementById('resDateHours').innerText = `${hours.toLocaleString()} Hours`;
        document.getElementById('resDateMinutes').innerText = `${minutes.toLocaleString()} Mins`;
        document.getElementById('resDateSeconds').innerText = `${seconds.toLocaleString()} Secs`;
        document.getElementById('resSolarPerspective').innerText = `${tropicalYears} Solar Tropical Years`;
        document.getElementById('resSolarPercent').innerText = `${((totalDays / 3652.422) * 100).toFixed(2)}% of a standard decade elapsed`;
    } else {
        const sStr = document.getElementById('pStartDate').value;
        const op = document.getElementById('pOperation').value;
        const pY = parseInt(document.getElementById('pYears').value, 10) || 0;
        const pM = parseInt(document.getElementById('pMonths').value, 10) || 0;
        const pW = parseInt(document.getElementById('pWeeks').value, 10) || 0;
        const pD = parseInt(document.getElementById('pDays').value, 10) || 0;

        if (!sStr) return;

        let [sy, sm, sd] = sStr.split('-').map(Number);
        const sign = (op === 'add') ? 1 : -1;

        let targetY = sy + (sign * pY);
        let targetM = (sm - 1) + (sign * pM);

        targetY += Math.floor(targetM / 12);
        targetM = ((targetM % 12) + 12) % 12;

        // Month clamping rule (e.g. Jan 31 + 1 month = Feb 28)
        const maxD = daysInMonth(targetY, targetM);
        let targetD = Math.min(sd, maxD);

        let resDate = new Date(targetY, targetM, targetD);
        const addedDays = sign * ((pW * 7) + pD);
        resDate.setDate(resDate.getDate() + addedDays);

        const options = { weekday: 'long', month: 'short', day: '2-digit', year: 'numeric' };
        const iso = `${resDate.getFullYear()}-${String(resDate.getMonth() + 1).padStart(2, '0')}-${String(resDate.getDate()).padStart(2, '0')}`;

        const baseDate = new Date(sy, sm - 1, sd);
        const totalDays = Math.abs(Math.round((resDate - baseDate) / 86400000));

        document.getElementById('resDatePrimaryLabel').innerText = (op === 'add') ? 'Resulting Future Date' : 'Resulting Historical Date';
        document.getElementById('resDatePrimaryVal').innerText = resDate.toLocaleDateString('en-US', options);
        document.getElementById('resDateTotalDays').innerText = `ISO: ${iso} • Total Offset: ${totalDays.toLocaleString()} Days`;
        document.getElementById('resDateWeeks').innerText = `${(totalDays / 7).toFixed(1)} Weeks`;
        document.getElementById('resDateHours').innerText = `${(totalDays * 24).toLocaleString()} Hours`;
        document.getElementById('resDateMinutes').innerText = `${(totalDays * 1440).toLocaleString()} Mins`;
        document.getElementById('resDateSeconds').innerText = `${(totalDays * 86400).toLocaleString()} Secs`;
        document.getElementById('resSolarPerspective').innerText = `${(totalDays / 365.2422).toFixed(3)} Tropical Solar Years`;
        document.getElementById('resSolarPercent').innerText = `Offset represents ${totalDays} natural calendar diurnal rotations`;
    }
}

window.addEventListener('DOMContentLoaded', () => {
    const today = new Date();
    const sy = today.getFullYear();
    const sm = String(today.getMonth() + 1).padStart(2, '0');
    const sd = String(today.getDate()).padStart(2, '0');
    document.getElementById('dDate1').value = `${sy}-${sm}-${sd}`;
    document.getElementById('pStartDate').value = `${sy}-${sm}-${sd}`;

    const future = new Date(today);
    future.setFullYear(today.getFullYear() + 1);
    future.setMonth(today.getMonth() + 6);
    future.setDate(today.getDate() + 15);
    const fy = future.getFullYear();
    const fm = String(future.getMonth() + 1).padStart(2, '0');
    const fd = String(future.getDate()).padStart(2, '0');
    document.getElementById('dDate2').value = `${fy}-${fm}-${fd}`;

    ['dateCalcMode', 'dDate1', 'dDate2', 'dIncludeEnd', 'pStartDate', 'pOperation', 'pYears', 'pMonths', 'pWeeks', 'pDays'].forEach(id => {
        const el = document.getElementById(id);
        el.addEventListener('input', updateDateCalculator);
        el.addEventListener('change', updateDateCalculator);
    });

    updateDateCalculator();
});
</script>"""

    article = """<h2>Mathematical Foundations of Gregorian Date Calculus</h2>
<p>Calculating temporal spans between arbitrary dates or projecting calendar dates across multi-scale units (years, months, weeks, days) constitutes a core operational necessity in biomedical clinical trials, jurisprudence, actuarial life tables, and corporate debt issuance. The primary difficulty in date mathematics arises from the fact that the civil calendar is non-metric and non-uniform: solar years alternate between 365 and 366 days, while individual months vary cyclically between 28, 29, 30, and 31 days.</p>

<p>When computing the discrete decomposition $(\Delta Y, \Delta M, \Delta D)$ between two dates $D_1 = (Y_1, M_1, d_1)$ and $D_2 = (Y_2, M_2, d_2)$ where $D_2 \ge D_1$, arithmetic operates through positional borrowing:</p>

$$\Delta D = d_2 - d_1, \quad \Delta M = M_2 - M_1, \quad \Delta Y = Y_2 - Y_1$$

<h3>1. Positional Borrowing Across Months</h3>
<p>If $\Delta D < 0$, days must be borrowed from the preceding month $M_2 - 1$. Crucially, the number of borrowed days is NOT a fixed constant (such as 30), but equals the exact physical calendar length of the immediately preceding month:</p>

$$\Delta D = \Delta D + \text{DaysInMonth}(Y_2, M_2 - 1), \quad \Delta M = \Delta M - 1$$

<p>Where $\text{DaysInMonth}$ evaluates to 31 for January, 28 or 29 for February, 31 for March, 30 for April, and so forth.</p>

<h3>2. Positional Borrowing Across Years</h3>
<p>If $\Delta M < 0$, a borrow is decremented from the year term, transferring 12 months to the monthly accumulator:</p>

$$\Delta M = \Delta M + 12, \quad \Delta Y = \Delta Y - 1$$

<h2>The End-of-Month Clamping Phenomenon in Temporal Projection</h2>
<p>When adding or subtracting calendar intervals from an anchor date—for example, adding exactly one month to January 31st—algebraic computation encounters an impossibility: the date <em>February 31st</em> does not exist in any solar calendar. In software systems and legal contracts, this is resolved via the <strong>End-of-Month Clamping Convention</strong> (standardized by ANSI SQL, Java <code>java.time</code>, and Python <code>dateutil.relativedelta</code>):</p>

$$M_{\text{new}} = (M_0 + \Delta M) \bmod 12$$

$$Y_{\text{new}} = Y_0 + \left\lfloor \frac{M_0 + \Delta M}{12} \right\rfloor$$

$$d_{\text{clamped}} = \min\big(d_0, \text{DaysInMonth}(Y_{\text{new}}, M_{\text{new}})\big)$$

<p>Under this formal convention, adding one month to January 31, 2026 clamps cleanly to <strong>February 28, 2026</strong>. In a leap year (such as 2028), adding one month to January 31st clamps cleanly to <strong>February 29, 2028</strong>.</p>

<h3>Gregorian Calendar Month Length and Leap Year Matrix</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Month Index ($M$)</th>
            <th>Month Name</th>
            <th>Standard Year Days</th>
            <th>Leap Year Days</th>
            <th>Cumulative Standard Days</th>
            <th>Cumulative Leap Days</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>1</td><td>January</td><td>31 Days</td><td>31 Days</td><td>31 Days</td><td>31 Days</td></tr>
        <tr><td>2</td><td>February</td><td>28 Days</td><td>29 Days (Leap Day)</td><td>59 Days</td><td>60 Days</td></tr>
        <tr><td>3</td><td>March</td><td>31 Days</td><td>31 Days</td><td>90 Days</td><td>91 Days</td></tr>
        <tr><td>4</td><td>April</td><td>30 Days</td><td>30 Days</td><td>120 Days</td><td>121 Days</td></tr>
        <tr><td>5</td><td>May</td><td>31 Days</td><td>31 Days</td><td>151 Days</td><td>152 Days</td></tr>
        <tr><td>6</td><td>June</td><td>30 Days</td><td>30 Days</td><td>181 Days</td><td>182 Days</td></tr>
        <tr><td>7</td><td>July</td><td>31 Days</td><td>31 Days</td><td>212 Days</td><td>213 Days</td></tr>
        <tr><td>8</td><td>August</td><td>31 Days</td><td>31 Days</td><td>243 Days</td><td>244 Days</td></tr>
        <tr><td>9</td><td>September</td><td>30 Days</td><td>30 Days</td><td>273 Days</td><td>274 Days</td></tr>
        <tr><td>10</td><td>October</td><td>31 Days</td><td>31 Days</td><td>304 Days</td><td>305 Days</td></tr>
        <tr><td>11</td><td>November</td><td>30 Days</td><td>30 Days</td><td>334 Days</td><td>335 Days</td></tr>
        <tr><td>12</td><td>December</td><td>31 Days</td><td>31 Days</td><td>365 Days</td><td>366 Days</td></tr>
    </tbody>
</table>

<h2>Continuous Astronomical Time: Julian Day Numbers (JDN) and MJD</h2>
<p>To eliminate month length variations and century leap-year complexities in computational astrophysics and satellite orbit ephemerides, astronomers bypass calendar dates entirely in favor of continuous scalar numbers. The primary celestial timescale is the <strong>Julian Day Number (JDN)</strong>, defined as the continuous count of days elapsed since Greenwich mean noon on January 1, 4713 BCE (proleptic Julian calendar).</p>

<p>For modern aerospace tracking and satellite flight dynamics, NASA and the International Astronomical Union (IAU) commonly employ the <strong>Modified Julian Date (MJD)</strong>:</p>

$$\text{MJD} = \text{JDN} - 2400000.5$$

<p>The offset of $0.5$ shifts the start of the astronomical day from noon to midnight UTC, ensuring seamless synchronization with civil solar dates. The duration between any two historical or future events $(t_1, t_2)$ is obtained through exact scalar subtraction: $\Delta t = \text{MJD}_2 - \text{MJD}_1$, completely circumventing calendar irregularities.</p>

<h2>The Year 2038 Problem (Y2K38) in Computer Systems</h2>
<p>In software engineering and Unix-like operating systems (including Linux, Android, iOS, and macOS), calendar dates are traditionally stored as the number of elapsed seconds since the Unix Epoch (January 1, 1970 00:00:00 UTC). Systems utilizing legacy <strong>32-bit signed integers</strong> (<code>time_t</code>) possess a maximum positive representable value of $2^{31} - 1 = 2,147,483,647$ seconds.</p>

<p>This limitation triggers the famous <strong>Year 2038 Problem (Y2K38)</strong>:</p>

<ul>
    <li>At exactly <strong>03:14:07 UTC on Tuesday, January 19, 2038</strong>, the 32-bit integer overflows into negative values ($-2,147,483,648$).</li>
    <li>Unpatched computer systems, embedded automotive microcontrollers, and financial mortgage amortization engines will wrap backward to <strong>20:45:52 UTC on Friday, December 13, 1901</strong>.</li>
</ul>

<p>Modern date calculation libraries prevent this overflow by transitioning to <strong>64-bit signed integers</strong>, expanding the representable timeline by approximately 292 billion years.</p>

<div class="worked-example-card">
    <h3>Worked Clinical Research Case Study: Pharmaceutical Protocol Follow-up Windows</h3>
    <p><strong>Scenario:</strong> An oncology patient in an FDA Phase III clinical trial undergoes baseline surgical resection on <strong>August 31, 2026</strong>. The protocol mandates a primary efficacy evaluation visit exactly <strong>6 months</strong> post-baseline, with an allowable visit window of $\pm 7$ calendar days (per International Council for Harmonisation ICH GCP E6 guidelines). Determine: (1) the exact target protocol visit date applying end-of-month clamping, and (2) the allowable clinical visit window dates.</p>
    
    <div class="step-solution">
        <h4>Step 1: Apply 6-Month Addition with Clamping</h4>
        <p>Baseline: August 31, 2026 ($Y=2026, M=8, D=31$).</p>
        <p>Target Month: $8 + 6 = 14 \implies 14 - 12 = \text{Month 2 (February of 2027)}$.</p>
        <p>Year: $2026 + 1 = 2027$.</p>
        <p>Evaluate February 2027: 2027 is not divisible by 4, so February contains 28 days.</p>
        <p>Apply clamping: $\min(31, 28) = 28$.</p>
        <p><strong>Target Protocol Date:</strong> Sunday, February 28, 2027.</p>

        <h4>Step 2: Calculate Allowable $\pm 7$ Day Window</h4>
        <p>Earliest Visit Date: $\text{Feb 28} - 7 \text{ days} = \text{Sunday, February 21, 2027}$.</p>
        <p>Latest Visit Date: $\text{Feb 28} + 7 \text{ days} = \text{Sunday, March 7, 2027}$.</p>
        <p>Total Allowable Span: 15 inclusive calendar days (Feb 21 through Mar 7, 2027).</p>
    </div>
</div>

<h2>Common Methodological Errors in Date Calculations</h2>
<ol>
    <li><strong>Naive Thirty-Day Month Multipliers:</strong> Multiplying months by 30 (e.g., assuming 6 months = 180 days) introduces systematic discrepancies. The interval from March 1 to September 1 contains 184 days, whereas the interval from September 1 to March 1 contains only 181 days (or 182 in a leap year). True date math must traverse actual calendar months.</li>
    <li><strong>Asymmetry in Temporal Reversal:</strong> Adding a month and then subtracting a month does not necessarily return to the original date due to clamping. For example, $\text{Jan 31} + 1 \text{ month} = \text{Feb 28}$; subsequent subtraction $\text{Feb 28} - 1 \text{ month} = \text{Jan 28}$, resulting in an irreversible 3-day loss.</li>
    <li><strong>Proleptic Gregorian Calendar Distortion:</strong> Projecting dates prior to October 15, 1582 requires specifying whether calculations utilize the proleptic Gregorian calendar or the historical Julian calendar (which drifted by 10 days at the time of the Gregorian reform).</li>
</ol>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article)


def main():
    c_html = gen_countdown_calculator()
    with open(os.path.join(BASE_DIR, "countdown-calculator.html"), "w", encoding="utf-8") as f:
        f.write(c_html)
    print("Generated countdown-calculator.html successfully!")

    d_html = gen_date_calculator()
    with open(os.path.join(BASE_DIR, "date-calculator.html"), "w", encoding="utf-8") as f:
        f.write(d_html)
    print("Generated date-calculator.html successfully!")

if __name__ == "__main__":
    main()
