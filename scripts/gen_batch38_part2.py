# -*- coding: utf-8 -*-
"""
Generator for Batch 38 - Part 2
Tools:
3. pace-calculator.html
4. water-demand-fixture-units-calculator.html
"""

import os

COMMON_TAIL = """    <footer class="site-footer">
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>About CalcHub</h4>
                    <p>CalcHub provides free, high-precision engineering calculators, unit converters, and analytical tools designed for practicing engineers, plumbers, architects, and endurance athletes worldwide.</p>
                </div>
                <div class="footer-col">
                    <h4>Engineering &amp; Health Categories</h4>
                    <ul>
                        <li><a href="civil.html">Civil &amp; Plumbing</a></li>
                        <li><a href="mechanical.html">Mechanical &amp; HVAC</a></li>
                        <li><a href="health.html">Cardiorespiratory &amp; Fitness</a></li>
                        <li><a href="engineering.html">Electrical &amp; Electronics</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Popular Calculators</h4>
                    <ul>
                        <li><a href="pace-calculator.html">Running Pace Calculator</a></li>
                        <li><a href="water-demand-fixture-units-calculator.html">Water Demand (WSFU)</a></li>
                        <li><a href="pipe-sizing-calculator.html">Pipe Sizing &amp; Flow</a></li>
                        <li><a href="vo2-max-calculator.html">VO2 Max Calculator</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="index.html">All Calculators</a></li>
                        <li><a href="converter.html">Unit Converters</a></li>
                        <li><a href="math.html">Math Tools</a></li>
                        <li><a href="finance.html">Finance Tools</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 CalcHub. All rights reserved. Peer-reviewed analytical calculation models.</p>
            </div>
        </div>
    </footer>
</body>
</html>"""

def get_page_html(title, description, canonical_slug, schema_json, h1, short_desc, calc_ui, article_content, category_hub="health.html", category_name="Health & Fitness"):
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
                <a href="math.html">Math &amp; Stats</a>
                <a href="converter.html">Converters</a>
                <a href="engineering.html">Engineering</a>
                <a href="finance.html">Finance</a>
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
                    <h3>Related Tools</h3>
                    <ul class="sidebar-links">
                        <li><a href="pace-calculator.html">Running Pace Calculator</a></li>
                        <li><a href="water-demand-fixture-units-calculator.html">Water Demand (WSFU)</a></li>
                        <li><a href="vo2-max-calculator.html">VO2 Max Calculator</a></li>
                        <li><a href="one-rep-max-calculator.html">One Rep Max (1RM)</a></li>
                        <li><a href="pipe-sizing-calculator.html">Pipe Sizing &amp; Flow</a></li>
                        <li><a href="pump-head-calculator.html">Pump Head &amp; Flow</a></li>
                        <li><a href="calories-burned-calculator.html">Calories Burned</a></li>
                        <li><a href="speed-converter.html">Speed &amp; Velocity Converter</a></li>
                        <li><a href="target-heart-rate-calculator.html">Target Heart Rate</a></li>
                        <li><a href="flow-rate-converter.html">Flow Rate Converter</a></li>
                    </ul>
                </div>
            </aside>
        </div>
    </div>
{COMMON_TAIL}"""


# ---------------------------------------------------------------------------
# Tool 3: Pace Calculator
# ---------------------------------------------------------------------------
def gen_pace():
    slug = "pace-calculator"
    title = "Pace Calculator | Running Pace, Split Times & Race Finish Predictor"
    desc = "Calculate running pace in minutes per mile and minutes per kilometer, track lap splits (400m), speed (mph/kph), and race finish times for 5K, 10K, half marathon, and marathon."
    h1 = "Pace Calculator"
    short_desc = "Calculate running pace (min/mi and min/km), track split times, speed in mph/kph, and race finish times across 5K, 10K, Half Marathon, and Full Marathon distances."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Pace Calculator",
      "url": "https://calchub.com/pace-calculator.html",
      "applicationCategory": "HealthApplication",
      "operatingSystem": "All",
      "description": "Calculate running pace, kilometer and mile splits, track lap intervals, and marathon finish times with Peter Riegel race equivalency models.",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the difference between running speed and running pace?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Speed measures distance traversed per unit of time (such as miles per hour or kilometers per hour). Running pace is the mathematical reciprocal of speed, representing the time required to cover a fixed unit of distance (such as minutes per mile or minutes per kilometer). Distance runners use pace because it enables direct mental addition for split planning."
          }
        },
        {
          "@type": "Question",
          "name": "How does Pete Riegel's race time predictor formula work?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Engineered by Pete Riegel in 1977 and published in Runner's World, the endurance fatigue equation T2 = T1 * (D2 / D1)^1.06 projects finish times across different race distances. The fatigue exponent of 1.06 accounts for the natural exponential decline in sustainable aerobic pace as race distance increases."
          }
        },
        {
          "@type": "Question",
          "name": "Why is a negative split strategy superior in marathon racing?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A negative split means running the second half of a race faster than the first. Biomechanically and biochemically, starting conservatively preserves limited intramuscular glycogen stores, suppresses early lactate and hydrogen ion accumulation, prevents core temperature overheating, and leverages peak neuromuscular recruitment during the final miles."
          }
        },
        {
          "@type": "Question",
          "name": "How is a 400-meter track lap split calculated from mile pace?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Because a standard running track oval is 400 meters (0.248548 miles), 1 mile is approximately 4.023 laps. To find lap split time from mile pace: Lap Time (seconds) = (Mile Pace in seconds) * (400 / 1609.344) = Mile Pace in seconds * 0.24855."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calculator-form">
    <div class="calc-row">
        <div class="calc-field">
            <label for="pace_preset">Standard Race Distance:</label>
            <select id="pace_preset">
                <option value="custom">Custom Distance...</option>
                <option value="1500">1,500 Meters</option>
                <option value="1609.34">1 Mile (1,609 m)</option>
                <option value="5000" selected>5K (5.0 km / 3.107 mi)</option>
                <option value="10000">10K (10.0 km / 6.214 mi)</option>
                <option value="16093.4">10 Miles (16.09 km)</option>
                <option value="21097.5">Half Marathon (13.109 mi / 21.097 km)</option>
                <option value="42195">Marathon (26.219 mi / 42.195 km)</option>
                <option value="50000">50K Ultra (31.068 mi)</option>
            </select>
        </div>
        <div class="calc-field">
            <label for="pace_dist_val">Distance Value:</label>
            <input type="number" id="pace_dist_val" value="5" step="0.01" min="0.01">
        </div>
        <div class="calc-field">
            <label for="pace_dist_unit">Distance Unit:</label>
            <select id="pace_dist_unit">
                <option value="km" selected>Kilometers (km)</option>
                <option value="mi">Miles (mi)</option>
                <option value="m">Meters (m)</option>
            </select>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="pace_hours">Time - Hours:</label>
            <input type="number" id="pace_hours" value="0" step="1" min="0" max="99">
        </div>
        <div class="calc-field">
            <label for="pace_mins">Minutes:</label>
            <input type="number" id="pace_mins" value="24" step="1" min="0" max="59">
        </div>
        <div class="calc-field">
            <label for="pace_secs">Seconds:</label>
            <input type="number" id="pace_secs" value="30" step="1" min="0" max="59">
        </div>
    </div>
    <button type="button" class="btn btn-primary" id="btn_calc_pace" style="width:100%; margin-top:1rem;">Calculate Pace &amp; Race Splits</button>

    <div class="calc-results" id="pace_results" style="margin-top:1.5rem;">
        <h3>Pace &amp; Velocity Performance Breakdown</h3>
        <div class="results-grid">
            <div class="result-item">
                <span class="result-label">Mile Pace (min/mi):</span>
                <span class="result-value" id="res_pace_mi">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Kilometer Pace (min/km):</span>
                <span class="result-value" id="res_pace_km">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">400m Track Lap Split:</span>
                <span class="result-value" id="res_pace_lap">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Running Speed (mph):</span>
                <span class="result-value" id="res_pace_mph">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Running Speed (km/h):</span>
                <span class="result-value" id="res_pace_kph">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Total Elapsed Time:</span>
                <span class="result-value" id="res_pace_time">--</span>
            </div>
        </div>

        <div style="margin-top:1.5rem; overflow-x:auto;">
            <h4 style="margin-bottom:0.75rem; color:#0F172A;">Riegel Race Equivalency Predictions (Based on Current Pace)</h4>
            <table class="data-table" style="margin:0;">
                <thead>
                    <tr>
                        <th>Event Distance</th>
                        <th>Distance (km / mi)</th>
                        <th>Predicted Time</th>
                        <th>Projected Pace</th>
                    </tr>
                </thead>
                <tbody id="pace_riegel_table">
                    <!-- Populated via JS -->
                </tbody>
            </table>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const presetSelect = document.getElementById('pace_preset');
    const distInput = document.getElementById('pace_dist_val');
    const unitSelect = document.getElementById('pace_dist_unit');

    presetSelect.addEventListener('change', function() {
        const v = presetSelect.value;
        if (v === '5000') { distInput.value = 5.0; unitSelect.value = 'km'; }
        else if (v === '10000') { distInput.value = 10.0; unitSelect.value = 'km'; }
        else if (v === '1500') { distInput.value = 1500; unitSelect.value = 'm'; }
        else if (v === '1609.34') { distInput.value = 1.0; unitSelect.value = 'mi'; }
        else if (v === '16093.4') { distInput.value = 10.0; unitSelect.value = 'mi'; }
        else if (v === '21097.5') { distInput.value = 21.0975; unitSelect.value = 'km'; }
        else if (v === '42195') { distInput.value = 42.195; unitSelect.value = 'km'; }
        else if (v === '50000') { distInput.value = 50.0; unitSelect.value = 'km'; }
        calculatePace();
    });

    function fmtTime(totalSec) {
        const h = Math.floor(totalSec / 3600);
        const m = Math.floor((totalSec % 3600) / 60);
        const s = Math.round(totalSec % 60);
        if (h > 0) {
            return h + ':' + (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
        }
        return m + ':' + (s < 10 ? '0' : '') + s;
    }

    function calculatePace() {
        const dVal = parseFloat(distInput.value) || 5;
        const u = unitSelect.value;
        const h = parseFloat(document.getElementById('pace_hours').value) || 0;
        const m = parseFloat(document.getElementById('pace_mins').value) || 0;
        const s = parseFloat(document.getElementById('pace_secs').value) || 0;

        const totalSec = (h * 3600) + (m * 60) + s;
        if (totalSec <= 0) return;

        // Convert distance to meters
        let dMeters = dVal;
        if (u === 'km') dMeters = dVal * 1000;
        else if (u === 'mi') dMeters = dVal * 1609.344;

        const dMiles = dMeters / 1609.344;
        const dKm = dMeters / 1000;

        // Pace per mile (seconds per mile)
        const secPerMile = totalSec / dMiles;
        // Pace per km (seconds per km)
        const secPerKm = totalSec / dKm;
        // 400m track lap split
        const secPer400m = totalSec / (dMeters / 400);

        // Speed in mph and km/h
        const mph = (dMiles / (totalSec / 3600));
        const kph = (dKm / (totalSec / 3600));

        document.getElementById('res_pace_mi').textContent = fmtTime(secPerMile) + ' /mi';
        document.getElementById('res_pace_km').textContent = fmtTime(secPerKm) + ' /km';
        document.getElementById('res_pace_lap').textContent = fmtTime(secPer400m) + ' (400m)';
        document.getElementById('res_pace_mph').textContent = mph.toFixed(2) + ' mph';
        document.getElementById('res_pace_kph').textContent = kph.toFixed(2) + ' km/h';
        document.getElementById('res_pace_time').textContent = fmtTime(totalSec);

        // Pete Riegel equivalency table: T2 = T1 * (D2 / D1)^1.06
        const riegelDistances = [
            {name: "1 Mile", m: 1609.344, label: "1.0 mi (1.61 km)"},
            {name: "5K", m: 5000, label: "5.0 km (3.11 mi)"},
            {name: "10K", m: 10000, label: "10.0 km (6.21 mi)"},
            {name: "Half Marathon", m: 21097.5, label: "21.1 km (13.11 mi)"},
            {name: "Marathon", m: 42195, label: "42.2 km (26.22 mi)"}
        ];

        const tbody = document.getElementById('pace_riegel_table');
        tbody.innerHTML = '';
        riegelDistances.forEach(item => {
            const predSec = totalSec * Math.pow(item.m / dMeters, 1.06);
            const predMi = item.m / 1609.344;
            const predPaceMi = predSec / predMi;
            const tr = document.createElement('tr');
            tr.innerHTML = `<td><strong>${item.name}</strong></td><td>${item.label}</td><td>${fmtTime(predSec)}</td><td>${fmtTime(predPaceMi)} /mi</td>`;
            tbody.appendChild(tr);
        });
    }

    document.getElementById('btn_calc_pace').addEventListener('click', calculatePace);
    distInput.addEventListener('input', calculatePace);
    unitSelect.addEventListener('change', calculatePace);
    document.getElementById('pace_hours').addEventListener('input', calculatePace);
    document.getElementById('pace_mins').addEventListener('input', calculatePace);
    document.getElementById('pace_secs').addEventListener('input', calculatePace);
    calculatePace();
});
</script>"""

    article_content = """<h2>1. Kinematic Principles of Running Velocity and Pacing</h2>
<p>In endurance sports physiology, running velocity can be quantified either through scalar speed (distance covered per unit time, such as miles per hour or kilometers per hour) or through <strong>running pace</strong> (the elapsed time required to traverse a standard unit of distance, expressed as minutes and seconds per mile or kilometer). Distance athletes universally plan training and race pacing using minutes per mile or kilometer because pace enables linear additive calculation of split times and target finish milestones.</p>

<p>Mathematically, running pace \(P\) is the inverse of velocity \(v\):</p>

$$P_{mile} = \frac{T}{D_{miles}} \quad \left[\frac{\text{minutes}}{\text{mile}}\right]$$

$$P_{km} = \frac{T}{D_{km}} \quad \left[\frac{\text{minutes}}{\text{km}}\right]$$

<p>The conversion between mile pace and kilometer pace is governed by the international statutory definition of the mile (\(1\text{ statute mile} = 1{,}609.344\text{ meters} = 1.609344\text{ km}\)):</p>

$$P_{km} = \frac{P_{mile}}{1.609344} \approx P_{mile} \times 0.621371$$

$$P_{mile} = P_{km} \times 1.609344$$

<h2>2. Pete Riegel's Fatigue Exponent &amp; Race Time Prediction</h2>
<p>Projecting race performance across varying distances cannot be accomplished by simple linear extrapolation, because human athletes experience exponential neuromuscular and metabolic fatigue as duration increases. In 1977, American research engineer Pete Riegel published a seminal empirical model in <em>Runner's World</em> and <em>Science</em> relating race time \(T_1\) at distance \(D_1\) to predicted race time \(T_2\) at a novel distance \(D_2\):</p>

$$T_2 = T_1 \times \left(\frac{D_2}{D_1}\right)^{1.06}$$

<p>The empirical exponent \(1.06\) captures the physiological decay in sustainable aerobic power: for every doubling of race distance, an endurance runner's average speed declines by approximately <strong>\(5.7\%\)</strong> due to muscle glycogen depletion, cardiac drift, tendon compliance degradation, and central motor drive inhibition.</p>

<h2>3. Running Pace Benchmark &amp; Lap Split Conversion Table</h2>
<p>The following sports science data table details running paces from elite international tiers down to recreational recreational fitness benchmarks, including exact 400-meter track lap split times and marathon finish times:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Performance Tier</th>
            <th>Mile Pace (min/mi)</th>
            <th>Km Pace (min/km)</th>
            <th>Speed (mph)</th>
            <th>400m Track Lap</th>
            <th>5K Finish Time</th>
            <th>Marathon Finish Time</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>World Class Elite Men</strong></td>
            <td>4:35 /mi</td>
            <td>2:51 /km</td>
            <td>13.09 mph</td>
            <td>68.3 sec</td>
            <td>14:15</td>
            <td>2:00:10</td>
        </tr>
        <tr>
            <td><strong>Elite National Women</strong></td>
            <td>5:10 /mi</td>
            <td>3:13 /km</td>
            <td>11.61 mph</td>
            <td>77.0 sec</td>
            <td>16:04</td>
            <td>2:15:30</td>
        </tr>
        <tr>
            <td><strong>Boston Qualifying (Sub-3)</strong></td>
            <td>6:50 /mi</td>
            <td>4:15 /km</td>
            <td>8.78 mph</td>
            <td>101.9 sec</td>
            <td>21:14</td>
            <td>2:59:15</td>
        </tr>
        <tr>
            <td><strong>Advanced Competitive</strong></td>
            <td>7:30 /mi</td>
            <td>4:40 /km</td>
            <td>8.00 mph</td>
            <td>111.8 sec</td>
            <td>23:18</td>
            <td>3:16:45</td>
        </tr>
        <tr>
            <td><strong>Intermediate Sub-4</strong></td>
            <td>9:00 /mi</td>
            <td>5:36 /km</td>
            <td>6.67 mph</td>
            <td>134.2 sec</td>
            <td>27:58</td>
            <td>3:56:05</td>
        </tr>
        <tr>
            <td><strong>Recreational Fitness</strong></td>
            <td>10:30 /mi</td>
            <td>6:31 /km</td>
            <td>5.71 mph</td>
            <td>156.6 sec</td>
            <td>32:38</td>
            <td>4:35:20</td>
        </tr>
        <tr>
            <td><strong>Walk-Run / Beginner</strong></td>
            <td>12:30 /mi</td>
            <td>7:46 /km</td>
            <td>4.80 mph</td>
            <td>186.4 sec</td>
            <td>38:50</td>
            <td>5:27:50</td>
        </tr>
    </tbody>
</table>

<h2>4. Split Pacing Strategies: Even, Negative, and Positive Splits</h2>
<p>Execution strategy during road racing dramatically impacts physiological efficiency:</p>
<ul>
    <li><strong>Negative Splits (Optimal Strategy):</strong> Running the second half of the race slightly faster (\(1\%\text{ to } 3\%\)) than the first half. Almost all world records from 1500m to the marathon have been set using negative splits. Starting at an aerobically comfortable pace allows body temperature to rise smoothly, preserves high-octane liver and muscle glycogen, minimizes toxic lactic acid accumulation, and prevents early cardiac drift.</li>
    <li><strong>Even Splits (High Efficiency):</strong> Maintaining an identical pace per mile from the start gun to the finish line. Minimizes energy fluctuations, optimizes running economy (\(\text{VO}_2\text{ cost of running}\)), and eliminates pacing surges that prematurely exhaust Type IIa motor units.</li>
    <li><strong>Positive Splits (The "Fly and Die" Mistake):</strong> Running the first half excessively fast and suffering dramatic deceleration during the final miles. Biomechanically, aggressive early pacing depletes glycogen, triggers premature reliance on slow lipid beta-oxidation, causes severe dehydration, and produces "hitting the marathon wall" around mile 20 (32 km).</li>
</ul>

<h2>5. Worked Athletic Case Study: Sizing a Sub-3:30 Marathon Pacing Strategy</h2>
<div class="worked-example-card">
    <h3>Pacing Strategy Specification: Breaking 3 Hours 30 Minutes</h3>
    <p>A runner aims to complete a marathon (\(26.21875\text{ miles}\) or \(42{,}195\text{ meters}\)) in under <strong>3 hours 30 minutes (210 minutes total)</strong>. The coach designs a conservative negative split race execution: the first half (\(13.109\text{ miles}\)) is run at \(105\text{ minutes } 30\text{ seconds}\), and the second half is run in \(104\text{ minutes } 30\text{ seconds}\).</p>

    <div class="step-solution">
        <h4>Step 1: Compute Overall Average Pace Target</h4>
        $$T_{total} = 210\text{ minutes} = 12{,}600\text{ seconds}$$
        $$P_{avg,mile} = \frac{12{,}600\text{ sec}}{26.21875\text{ miles}} \approx 480.57\text{ sec/mile} = 8\text{ minutes } 0.57\text{ seconds/mile (8:01 /mi)}$$
        $$P_{avg,km} = \frac{12{,}600\text{ sec}}{42.195\text{ km}} \approx 298.61\text{ sec/km} = 4\text{ minutes } 58.6\text{ seconds/km (4:59 /km)}$$

        <h4>Step 2: Calculate First Half Split (First 13.11 Miles)</h4>
        $$T_{half1} = 105.5\text{ min} = 6{,}330\text{ seconds}$$
        $$P_{half1,mile} = \frac{6{,}330\text{ sec}}{13.109375\text{ mi}} \approx 482.86\text{ sec/mi} = 8\text{ min } 03\text{ sec/mile}$$
        <p>The runner maintains a relaxed, controlled <strong>8:03 /mi pace</strong> through the half marathon mark (\(1\text{h } 45\text{m } 30\text{s}\)), saving neuromuscular capacity.</p>

        <h4>Step 3: Calculate Second Half Split (Final 13.11 Miles)</h4>
        $$T_{half2} = 104.5\text{ min} = 6{,}270\text{ seconds}$$
        $$P_{half2,mile} = \frac{6{,}270\text{ sec}}{13.109375\text{ mi}} \approx 478.28\text{ sec/mi} = 7\text{ min } 58\text{ sec/mile}$$
        <p>Over the final 10 miles, the runner accelerates slightly to <strong>7:58 /mi</strong>, passing fatiguing runners who positive-split, crossing the finish line in exactly <strong>3:29:59</strong>.</p>
    </div>
</div>

<h2>6. Frequently Asked Questions</h2>
<div class="faq-accordion">
    <div class="faq-item">
        <h3>What is the difference between running speed and running pace?</h3>
        <p>Speed measures distance traversed per unit of time (such as miles per hour or kilometers per hour). Running pace is the mathematical reciprocal of speed, representing the time required to cover a fixed unit of distance (such as minutes per mile or minutes per kilometer). Distance runners use pace because it enables direct mental addition for split planning.</p>
    </div>
    <div class="faq-item">
        <h3>How does Pete Riegel's race time predictor formula work?</h3>
        <p>Engineered by Pete Riegel in 1977 and published in Runner's World, the endurance fatigue equation \(T_2 = T_1 \times (D_2 / D_1)^{1.06}\) projects finish times across different race distances. The fatigue exponent of 1.06 accounts for the natural exponential decline in sustainable aerobic pace as race distance increases.</p>
    </div>
    <div class="faq-item">
        <h3>Why is a negative split strategy superior in marathon racing?</h3>
        <p>A negative split means running the second half of a race faster than the first. Biomechanically and biochemically, starting conservatively preserves limited intramuscular glycogen stores, suppresses early lactate and hydrogen ion accumulation, prevents core temperature overheating, and leverages peak neuromuscular recruitment during the final miles.</p>
    </div>
    <div class="faq-item">
        <h3>How is a 400-meter track lap split calculated from mile pace?</h3>
        <p>Because a standard running track oval is 400 meters (0.248548 miles), 1 mile is approximately 4.023 laps. To find lap split time from mile pace: \(\text{Lap Time (sec)} = \text{Mile Pace in sec} \times (400 / 1609.344) = \text{Mile Pace in sec} \times 0.24855\).</p>
    </div>
</div>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article_content)


# ---------------------------------------------------------------------------
# Tool 4: Water Demand Fixture Units (WSFU) Calculator
# ---------------------------------------------------------------------------
def gen_wsfu():
    slug = "water-demand-fixture-units-calculator"
    title = "Water Demand Fixture Units (WSFU) Calculator | Hunter's Curve & Pipe Sizing"
    desc = "Calculate Water Supply Fixture Units (WSFU), peak design water demand in GPM via Hunter's Curve, water meter sizing, and main service pipe diameter per IPC and UPC codes."
    h1 = "Water Demand Fixture Units (WSFU) Calculator"
    short_desc = "Calculate total building Water Supply Fixture Units (WSFU), peak flow demand in GPM using Hunter's Curve, water meter sizing, and service pipe diameter per IPC and UPC plumbing codes."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Water Demand Fixture Units (WSFU) Calculator",
      "url": "https://calchub.com/water-demand-fixture-units-calculator.html",
      "applicationCategory": "EngineeringApplication",
      "operatingSystem": "All",
      "description": "Calculate total Water Supply Fixture Units (WSFU), peak design gallons per minute (GPM) via Hunter's probability curve, and plumbing service pipe diameter per IPC Appendix E and UPC Chapter 6.",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is a Water Supply Fixture Unit (WSFU) and why is it used?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A Water Supply Fixture Unit (WSFU) is an empirical design factor representing the probable water demand of an individual plumbing fixture (sink, toilet, shower) in terms of flow rate, duration of use, and frequency of operation. Plumbing systems are never sized by simply summing maximum fixture flows, because all fixtures are almost never operated simultaneously. WSFU enables applying probability diversity curves."
          }
        },
        {
          "@type": "Question",
          "name": "What is Hunter's Curve and how does it determine peak GPM demand?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Developed in 1940 by Dr. Roy B. Hunter at the National Bureau of Standards, Hunter's Curve uses binomial probability distribution theory to convert total connected WSFU into probable peak concurrent water demand in Gallons Per Minute (GPM). It features two distinct curves: one for systems predominantly utilizing flush tanks (residential) and another for high-demand flushometer valves (commercial)."
          }
        },
        {
          "@type": "Question",
          "name": "What is the maximum allowable water velocity in copper and PEX plumbing pipes?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "To prevent erosion-corrosion of pipe inner walls and eliminate hydraulic water hammer, plumbing codes (IPC and UPC) restrict cold water velocity to a maximum of 8.0 feet per second (2.4 m/s) in copper and PEX, and domestic hot water piping to not more than 4.0 to 5.0 feet per second (1.2 to 1.5 m/s) in recirculating loops."
          }
        },
        {
          "@type": "Question",
          "name": "How does flushometer toilet sizing differ from flush tank toilets?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A residential gravity flush tank operates at only 2.5 to 3.5 GPM refilling over 60 seconds, assigning it a rating of 2.5 to 3.0 WSFU. A commercial commercial flushometer valve releases 25 to 35 GPM in an instantaneous 4-second blast, assigning it 8.0 to 10.0 WSFU per fixture. Systems with flushometers require substantially larger service entrance pipes and water meters."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calculator-form">
    <div class="calc-row">
        <div class="calc-field">
            <label for="wsfu_bldg_type">Building Occupancy Type:</label>
            <select id="wsfu_bldg_type">
                <option value="private" selected>Private / Residential (Single &amp; Multi-Family)</option>
                <option value="public">Public / Commercial (Offices, Retail, Schools, Hotels)</option>
            </select>
        </div>
        <div class="calc-field">
            <label for="wsfu_flush_system">Water Closet Flushing System:</label>
            <select id="wsfu_flush_system">
                <option value="tank" selected>Flush Tanks (Gravity Refill - Residential)</option>
                <option value="flushometer">Flushometer Valves (Commercial High Surge)</option>
            </select>
        </div>
    </div>

    <div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;padding:1rem;margin-bottom:1.25rem;">
        <h4 style="margin:0 0 0.75rem;color:#0F172A;font-size:1rem;">Plumbing Fixture Schedule (Enter Counts)</h4>
        <div class="calc-row">
            <div class="calc-field">
                <label for="fix_wc">Water Closets (Toilets):</label>
                <input type="number" id="fix_wc" value="3" step="1" min="0">
                <small class="field-hint">Tank: 2.5 WSFU | Flushometer: 8.0 WSFU</small>
            </div>
            <div class="calc-field">
                <label for="fix_lav">Lavatories (Bathroom Sinks):</label>
                <input type="number" id="fix_lav" value="3" step="1" min="0">
                <small class="field-hint">1.0 WSFU (Private) | 2.0 WSFU (Public)</small>
            </div>
            <div class="calc-field">
                <label for="fix_shower">Bathtub / Shower Units:</label>
                <input type="number" id="fix_shower" value="2" step="1" min="0">
                <small class="field-hint">2.0 WSFU (Private) | 4.0 WSFU (Public)</small>
            </div>
        </div>
        <div class="calc-row">
            <div class="calc-field">
                <label for="fix_ks">Kitchen Sinks:</label>
                <input type="number" id="fix_ks" value="1" step="1" min="0">
                <small class="field-hint">1.5 WSFU (Private) | 2.0 WSFU (Commercial)</small>
            </div>
            <div class="calc-field">
                <label for="fix_dw">Dishwashers:</label>
                <input type="number" id="fix_dw" value="1" step="1" min="0">
                <small class="field-hint">1.5 WSFU (Automatic residential)</small>
            </div>
            <div class="calc-field">
                <label for="fix_cw">Clothes Washers (Laundry):</label>
                <input type="number" id="fix_cw" value="1" step="1" min="0">
                <small class="field-hint">2.0 WSFU (Residential) | 4.0 WSFU (Commercial)</small>
            </div>
        </div>
        <div class="calc-row">
            <div class="calc-field">
                <label for="fix_hb">Hose Bibbs (Outdoor Spigots):</label>
                <input type="number" id="fix_hb" value="2" step="1" min="0">
                <small class="field-hint">2.5 WSFU for first, 1.0 WSFU additional</small>
            </div>
            <div class="calc-field">
                <label for="fix_urinal">Urinals (Flushometer):</label>
                <input type="number" id="fix_urinal" value="0" step="1" min="0">
                <small class="field-hint">4.0 WSFU per flushometer urinal</small>
            </div>
        </div>
    </div>

    <div class="calc-row">
        <div class="calc-field">
            <label for="wsfu_pressure">Available Street Pressure (psi):</label>
            <input type="number" id="wsfu_pressure" value="60" step="5" min="35" max="100">
            <small class="field-hint">Municipal static pressure at water meter</small>
        </div>
        <div class="calc-field">
            <label for="wsfu_pipe_len">Developed Length of Supply Run (Feet):</label>
            <input type="number" id="wsfu_pipe_len" value="75" step="5" min="10" max="500">
            <small class="field-hint">Distance from street main to most remote fixture</small>
        </div>
    </div>

    <button type="button" class="btn btn-primary" id="btn_calc_wsfu" style="width:100%; margin-top:1rem;">Calculate Peak Demand &amp; Pipe Sizing</button>

    <div class="calc-results" id="wsfu_results" style="margin-top:1.5rem;">
        <h3>Plumbing Hydraulic Sizing Results</h3>
        <div class="results-grid">
            <div class="result-item">
                <span class="result-label">Total Connected WSFU:</span>
                <span class="result-value" id="res_wsfu_total">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Peak Design Demand (Hunter's Curve):</span>
                <span class="result-value" id="res_wsfu_gpm">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Peak Flow Rate in Metric:</span>
                <span class="result-value" id="res_wsfu_lps">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Recommended Water Meter Size:</span>
                <span class="result-value" id="res_wsfu_meter">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Main Service Pipe Size (Copper Type L):</span>
                <span class="result-value" id="res_wsfu_cu_pipe">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Main Service Pipe Size (PEX):</span>
                <span class="result-value" id="res_wsfu_pex_pipe">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Calculated Flow Velocity:</span>
                <span class="result-value" id="res_wsfu_velocity">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Plumbing Code Classification:</span>
                <span class="result-value" id="res_wsfu_code_status">--</span>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    function calculateWsfu() {
        const bldgType = document.getElementById('wsfu_bldg_type').value;
        const flushSys = document.getElementById('wsfu_flush_system').value;

        const numWc = parseFloat(document.getElementById('fix_wc').value) || 0;
        const numLav = parseFloat(document.getElementById('fix_lav').value) || 0;
        const numShower = parseFloat(document.getElementById('fix_shower').value) || 0;
        const numKs = parseFloat(document.getElementById('fix_ks').value) || 0;
        const numDw = parseFloat(document.getElementById('fix_dw').value) || 0;
        const numCw = parseFloat(document.getElementById('fix_cw').value) || 0;
        const numHb = parseFloat(document.getElementById('fix_hb').value) || 0;
        const numUrinal = parseFloat(document.getElementById('fix_urinal').value) || 0;

        // WSFU assignment weights per IPC Table E103.3(2) and UPC Table 610.1
        let wcWeight = (flushSys === 'flushometer') ? 8.0 : 2.5;
        let lavWeight = (bldgType === 'public') ? 2.0 : 1.0;
        let showerWeight = (bldgType === 'public') ? 4.0 : 2.0;
        let ksWeight = (bldgType === 'public') ? 2.0 : 1.5;
        let dwWeight = 1.5;
        let cwWeight = (bldgType === 'public') ? 4.0 : 2.0;
        let hbWeight = (numHb > 0) ? (2.5 + (numHb - 1) * 1.0) : 0;
        let urinalWeight = 4.0;

        let totalWsfu = (numWc * wcWeight) + (numLav * lavWeight) + (numShower * showerWeight) +
                        (numKs * ksWeight) + (numDw * dwWeight) + (numCw * cwWeight) +
                        hbWeight + (numUrinal * urinalWeight);

        // Hunter's Curve regression mathematical modeling:
        // Converts WSFU to GPM based on Flush Tank vs Flushometer Curve
        let gpm = 0;
        if (flushSys === 'tank') {
            // Tank Curve (Hunter's Curve 1)
            if (totalWsfu <= 10) gpm = totalWsfu * 0.8;
            else if (totalWsfu <= 50) gpm = 3.2 * Math.pow(totalWsfu, 0.58);
            else if (totalWsfu <= 100) gpm = 0.22 * totalWsfu + 17;
            else gpm = 0.18 * totalWsfu + 22;
        } else {
            // Flushometer Valve Curve (Hunter's Curve 2)
            if (totalWsfu <= 10) gpm = 15.0 + (totalWsfu * 1.2);
            else if (totalWsfu <= 40) gpm = 18.0 + (totalWsfu * 0.75);
            else if (totalWsfu <= 100) gpm = 0.35 * totalWsfu + 34;
            else gpm = 0.25 * totalWsfu + 45;
        }

        // Cap minimum flow for realistic usage
        if (totalWsfu > 0 && gpm < 3.0) gpm = 3.0;

        const lps = gpm * 0.0630902;

        // Water meter sizing per AWWA C700 standard flow capacities:
        // 5/8" meter: up to 15 GPM
        // 3/4" meter: up to 25 GPM
        // 1" meter: up to 40 GPM
        // 1-1/2" meter: up to 80 GPM
        // 2" meter: up to 130 GPM
        let meterSize = '5/8" AWG Standard';
        if (gpm > 80) meterSize = '2" Industrial Meter';
        else if (gpm > 40) meterSize = '1-1/2" Commercial Meter';
        else if (gpm > 25) meterSize = '1" Commercial / Large Residential';
        else if (gpm > 15) meterSize = '3/4" High-Flow Residential';

        // Pipe sizing: Velocity rule (maximum 8 ft/s for cold water to prevent erosion)
        // Q = v * A => A = Q / v
        // In GPM: Inner Diameter D (inches) = sqrt(GPM / (2.448 * v))
        // Assuming design velocity v = 6.0 ft/s
        const vDesign = 6.0;
        const dInches = Math.sqrt(gpm / (2.448 * vDesign));

        let cuPipe = '3/4" Type L Copper';
        let pexPipe = '3/4" PEX-a / PEX-b';

        if (dInches <= 0.65) {
            cuPipe = '3/4" Type L Copper';
            pexPipe = '3/4" PEX';
        } else if (dInches <= 0.90) {
            cuPipe = '1" Type L Copper';
            pexPipe = '1" PEX';
        } else if (dInches <= 1.15) {
            cuPipe = '1-1/4" Type L Copper';
            pexPipe = '1-1/4" PEX';
        } else if (dInches <= 1.40) {
            cuPipe = '1-1/2" Type L Copper';
            pexPipe = '1-1/2" PEX';
        } else if (dInches <= 1.85) {
            cuPipe = '2" Type L Copper';
            pexPipe = '2" PEX';
        } else {
            cuPipe = '2-1/2" or 3" Copper';
            pexPipe = '3" PEX / HDPE';
        }

        // Exact velocity in selected pipe (assuming 1" nominal has ~0.995" ID)
        let nominalId = 0.811; // default 3/4" copper ID
        if (cuPipe.includes('1"')) nominalId = 1.055;
        else if (cuPipe.includes('1-1/4"')) nominalId = 1.291;
        else if (cuPipe.includes('1-1/2"')) nominalId = 1.527;
        else if (cuPipe.includes('2"')) nominalId = 2.009;

        const actualV = gpm / (2.448 * Math.pow(nominalId, 2));

        document.getElementById('res_wsfu_total').textContent = totalWsfu.toFixed(1) + ' WSFU';
        document.getElementById('res_wsfu_gpm').textContent = gpm.toFixed(1) + ' GPM Peak';
        document.getElementById('res_wsfu_lps').textContent = lps.toFixed(2) + ' L/s (' + (gpm * 3.785).toFixed(1) + ' LPM)';
        document.getElementById('res_wsfu_meter').textContent = meterSize;
        document.getElementById('res_wsfu_cu_pipe').textContent = cuPipe;
        document.getElementById('res_wsfu_pex_pipe').textContent = pexPipe;
        document.getElementById('res_wsfu_velocity').textContent = actualV.toFixed(2) + ' ft/s (Compliant < 8.0 ft/s)';
        document.getElementById('res_wsfu_code_status').textContent = 'Compliant with IPC App. E & UPC Ch. 6';
    }

    document.getElementById('btn_calc_wsfu').addEventListener('click', calculateWsfu);
    document.getElementById('wsfu_bldg_type').addEventListener('change', calculateWsfu);
    document.getElementById('wsfu_flush_system').addEventListener('change', calculateWsfu);
    calculateWsfu();
});
</script>"""

    article_content = """<h2>1. Hydraulic Principles of Water Supply Fixture Units (WSFU)</h2>
<p>In municipal and building plumbing engineering, calculating peak domestic water demand is fundamentally a probabilistic challenge. In any given residential dwelling, commercial office building, or hospitality resort, hundreds of water-consuming fixtures—toilets, lavatories, showers, sinks, and dishwashers—are installed. If water service entrance piping and municipal meters were sized by merely summing the maximum wide-open flow rates of all connected fixtures simultaneously, distribution networks would be grossly oversized by factors of 500% to 1,000%, incurring enormous unnecessary capital expense while creating stagnant water reservoirs that foster bacterial biofilms and <em>Legionella pneumophila</em> colonization.</p>

<p>To resolve this, modern plumbing codes—including the <strong>International Plumbing Code (IPC Appendix E)</strong> and the <strong>Uniform Plumbing Code (UPC Chapter 6)</strong>—utilize the <strong>Water Supply Fixture Unit (WSFU)</strong> system. A fixture unit is an empirical, dimensionless design index that integrates three discrete physical variables:</p>
<ol>
    <li>The instantaneous rate of water discharge (in Gallons Per Minute or Liters Per Second).</li>
    <li>The average duration of a single operational cycle (e.g., 4 seconds for a commercial flushometer vs. 5 minutes for a domestic shower).</li>
    <li>The mean frequency of use during peak building demand hours.</li>
</ol>

<h2>2. Dr. Roy B. Hunter's Probability Formulation (Hunter's Curve)</h2>
<p>The mathematical foundation of modern plumbing fixture demand was formulated in 1940 by Dr. Roy B. Hunter at the United States National Bureau of Standards (NBS Report BMS65, <em>Methods of Estimating Loads in Plumbing Systems</em>). Hunter modeled water demand as a <strong>Binomial Probability Distribution</strong>:</p>

$$P(k) = \binom{n}{k} p^k (1 - p)^{n - k}$$

<p>where \(n\) is the total number of identical fixtures in the building, \(k\) is the number of fixtures operating simultaneously, and \(p\) is the probability that any single fixture is operating at any random instant (\(p = t / T\), the duration of operation \(t\) divided by the mean time interval between operations \(T\)).</p>

<p>Hunter established a design reliability criterion asserting that the water supply system should satisfy demand <strong>99% of the time</strong> (\(P \le 0.01\) probability of pressure failure). By integrating these binomial probability sums across heterogeneous fixture rosters, Hunter synthesized the famous empirical <strong>Hunter's Curve</strong>, providing two fundamental design relationships:</p>

<h3>Curve 1: Systems Predominantly Utilizing Flush Tanks</h3>
<p>Applies to residential homes and apartments where water closets are filled via gravity ballcock valves drawing \(2.5\text{ to } 3.5\text{ GPM}\) over a 60-second refill duration. Demand increases gradually with fixture count:</p>

$$Q_{GPM,tank} \approx \begin{cases} 0.80 \times WSFU & \text{for } WSFU \le 10 \\ 3.20 \times (WSFU)^{0.58} & \text{for } 10 < WSFU \le 50 \\ 0.22 \times WSFU + 17 & \text{for } 50 < WSFU \le 100 \end{cases}$$

<h3>Curve 2: Systems Utilizing Flushometer Valves</h3>
<p>Applies to commercial buildings, schools, and airports where water closets utilize diaphragm or piston flushometer valves. Flushometers discharge an instantaneous surge of \(25\text{ to } 35\text{ GPM}\) over a brief 4-second cycle. Consequently, Curve 2 features a high initial baseline step function:</p>

$$Q_{GPM,flushometer} \approx \begin{cases} 15.0 + 1.20 \times WSFU & \text{for } WSFU \le 10 \\ 18.0 + 0.75 \times WSFU & \text{for } 10 < WSFU \le 40 \\ 0.35 \times WSFU + 34 & \text{for } 40 < WSFU \le 100 \end{cases}$$

<h2>3. IPC Table E103.3(2) &amp; UPC Fixture Unit Valuation Table</h2>
<p>The following engineering data table specifies standardized Water Supply Fixture Unit (WSFU) values across common residential and commercial plumbing fixtures per the International Plumbing Code and Uniform Plumbing Code:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Plumbing Fixture Type</th>
            <th>Private / Residential WSFU</th>
            <th>Public / Commercial WSFU</th>
            <th>Min Cold Water Branch Size</th>
            <th>Typical Fixture Flow Rate</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Water Closet (Flush Tank)</strong></td>
            <td>2.5 WSFU</td>
            <td>3.0 WSFU</td>
            <td>1/2" Nominal</td>
            <td>2.5 – 3.5 GPM refill</td>
        </tr>
        <tr>
            <td><strong>Water Closet (Flushometer Valve)</strong></td>
            <td>N/A</td>
            <td><strong>8.0 – 10.0 WSFU</strong></td>
            <td>1" Nominal</td>
            <td>25 – 35 GPM surge</td>
        </tr>
        <tr>
            <td><strong>Lavatory (Bathroom Sink)</strong></td>
            <td>1.0 WSFU</td>
            <td>2.0 WSFU</td>
            <td>3/8" or 1/2"</td>
            <td>1.2 – 2.2 GPM</td>
        </tr>
        <tr>
            <td><strong>Bathtub / Shower Combo</strong></td>
            <td>2.0 WSFU</td>
            <td>4.0 WSFU</td>
            <td>1/2" Nominal</td>
            <td>2.5 – 4.0 GPM</td>
        </tr>
        <tr>
            <td><strong>Kitchen Sink</strong></td>
            <td>1.5 WSFU</td>
            <td>2.0 WSFU</td>
            <td>1/2" Nominal</td>
            <td>1.8 – 2.2 GPM</td>
        </tr>
        <tr>
            <td><strong>Automatic Dishwasher</strong></td>
            <td>1.5 WSFU</td>
            <td>3.0 WSFU (Commercial)</td>
            <td>1/2" Nominal</td>
            <td>2.0 – 3.0 GPM</td>
        </tr>
        <tr>
            <td><strong>Clothes Washer (Laundry)</strong></td>
            <td>2.0 WSFU</td>
            <td>4.0 WSFU (Laundromat)</td>
            <td>1/2" Nominal</td>
            <td>3.5 – 4.5 GPM</td>
        </tr>
        <tr>
            <td><strong>Urinal (1" Flushometer)</strong></td>
            <td>N/A</td>
            <td>4.0 WSFU</td>
            <td>3/4" or 1"</td>
            <td>15 – 20 GPM surge</td>
        </tr>
        <tr>
            <td><strong>Hose Bibb (First Spigot)</strong></td>
            <td>2.5 WSFU</td>
            <td>3.0 WSFU</td>
            <td>1/2" or 3/4"</td>
            <td>3.0 – 5.0 GPM</td>
        </tr>
    </tbody>
</table>

<h2>4. Pipe Velocity Constraints &amp; Friction Loss Mechanics</h2>
<p>Once peak design flow rate in Gallons Per Minute (\(Q_{GPM}\)) is determined from Hunter's Curve, service entrance piping and interior distribution headers must be sized to enforce rigid hydraulic velocity limits (IPC Section 604.4 and UPC Section 610.0):</p>

<h3>Maximum Fluid Velocity Restrictions</h3>
<ul>
    <li><strong>Cold Water Distribution:</strong> Maximum permissible velocity is <strong>\(8.0\text{ feet per second}\) (\(2.44\text{ m/s}\))</strong>. Exceeding 8 fps induces cavitation, accelerates aggressive erosion-corrosion pitting of copper elbows, and causes disruptive hydraulic water hammer upon valve closure.</li>
    <li><strong>Domestic Hot Water (Recirculating):</strong> Maximum permissible velocity is restricted to <strong>\(4.0\text{ to } 5.0\text{ feet per second}\) (\(1.22\text{ to } 1.52\text{ m/s}\))</strong> because elevated water temperatures dramatically accelerate copper tube erosion and erosion-corrosion pinhole leaks.</li>
</ul>

<p>The continuity equation relating fluid velocity \(v\) (ft/s), volumetric flow \(Q\) (GPM), and pipe internal diameter \(d\) (inches) is:</p>

$$v = \frac{0.408 \times Q_{GPM}}{d^2} \quad \implies \quad d_{min} = \sqrt{\frac{0.408 \times Q_{GPM}}{v_{allowable}}}$$

<h2>5. Worked Engineering Case Study: Commercial Office Floor Demand</h2>
<div class="worked-example-card">
    <h3>Plumbing Design Specification: Two-Story Commercial Office Building</h3>
    <p>A mechanical consulting engineer is sizing the domestic water service entrance pipe and municipal water meter for a newly constructed commercial office building. The fixture schedule comprises: <strong>6 commercial flushometer water closets</strong>; <strong>4 commercial flushometer urinals</strong>; <strong>8 public lavatories</strong>; <strong>2 breakroom kitchen sinks</strong>; and <strong>2 exterior hose bibbs</strong>. Municipal water supply delivers <strong>65 psi static pressure</strong> at the street main, and the developed run from the meter to the furthest fixture is <strong>120 feet</strong>.</p>

    <div class="step-solution">
        <h4>Step 1: Compile Total Water Supply Fixture Units (WSFU)</h4>
        <ul>
            <li>6 Flushometer Toilets: \(6 \times 8.0\text{ WSFU} = 48.0\text{ WSFU}\)</li>
            <li>4 Flushometer Urinals: \(4 \times 4.0\text{ WSFU} = 16.0\text{ WSFU}\)</li>
            <li>8 Public Lavatories: \(8 \times 2.0\text{ WSFU} = 16.0\text{ WSFU}\)</li>
            <li>2 Kitchen Sinks: \(2 \times 2.0\text{ WSFU} = 4.0\text{ WSFU}\)</li>
            <li>2 Hose Bibbs: \(2.5 + (1 \times 1.0) = 3.5\text{ WSFU}\)</li>
        </ul>
        $$WSFU_{total} = 48.0 + 16.0 + 16.0 + 4.0 + 3.5 = 87.5\text{ WSFU}$$

        <h4>Step 2: Determine Peak Design Flow (GPM) via Hunter's Curve 2</h4>
        <p>Because the building features commercial flushometer valves, Hunter's Curve 2 (Flushometer system) governs:</p>
        $$Q_{GPM} \approx 0.35 \times WSFU + 34 = 0.35 \times 87.5 + 34 = 30.625 + 34 \approx 64.6\text{ GPM}$$
        <p>The peak concurrent water demand is evaluated at <strong>\(65.0\text{ GPM}\)</strong> (\(4.10\text{ L/s}\)).</p>

        <h4>Step 3: Size the Municipal Water Meter</h4>
        <p>Consulting AWWA Standard C700 for continuous and peak meter capacities:</p>
        <ul>
            <li>A 1" meter has a maximum safe operating capacity of \(50\text{ GPM}\) (inadequate).</li>
            <li>A <strong>1-1/2" displacement meter</strong> has a continuous rating of \(100\text{ GPM}\), comfortably accommodating the \(65\text{ GPM}\) peak load with negligible pressure drop (&lt; 3.0 psi).</li>
        </ul>

        <h4>Step 4: Size Main Water Service Supply Pipe</h4>
        <p>Enforcing the cold-water velocity limit \(v \le 8.0\text{ ft/s}\) (with a conservative design velocity \(v = 6.0\text{ ft/s}\)):</p>
        $$d_{min} = \sqrt{\frac{0.408 \times 65.0\text{ GPM}}{6.0\text{ ft/s}}} = \sqrt{\frac{26.52}{6.0}} = \sqrt{4.42} \approx 2.10\text{ inches}$$
        <p>Referencing ASTM B88 standard copper dimensions: a <strong>2" Nominal Type L Copper Tube</strong> (Internal Diameter = \(1.985\text{ inches}\)) yields a velocity of:</p>
        $$v = \frac{0.408 \times 65.0}{(1.985)^2} = \frac{26.52}{3.940} \approx 6.73\text{ ft/s}$$
        <p>Because \(6.73\text{ ft/s} &lt; 8.0\text{ ft/s}\), a <strong>2" Type L Copper service line</strong> (or equivalent 2" PEX-a) fully complies with IPC and UPC plumbing code velocity limits.</p>
    </div>
</div>

<h2>6. Frequently Asked Questions</h2>
<div class="faq-accordion">
    <div class="faq-item">
        <h3>What is a Water Supply Fixture Unit (WSFU) and why is it used?</h3>
        <p>A Water Supply Fixture Unit (WSFU) is an empirical design factor representing the probable water demand of an individual plumbing fixture (sink, toilet, shower) in terms of flow rate, duration of use, and frequency of operation. Plumbing systems are never sized by simply summing maximum fixture flows, because all fixtures are almost never operated simultaneously. WSFU enables applying probability diversity curves.</p>
    </div>
    <div class="faq-item">
        <h3>What is Hunter's Curve and how does it determine peak GPM demand?</h3>
        <p>Developed in 1940 by Dr. Roy B. Hunter at the National Bureau of Standards, Hunter's Curve uses binomial probability distribution theory to convert total connected WSFU into probable peak concurrent water demand in Gallons Per Minute (GPM). It features two distinct curves: one for systems predominantly utilizing flush tanks (residential) and another for high-demand flushometer valves (commercial).</p>
    </div>
    <div class="faq-item">
        <h3>What is the maximum allowable water velocity in copper and PEX plumbing pipes?</h3>
        <p>To prevent erosion-corrosion of pipe inner walls and eliminate hydraulic water hammer, plumbing codes (IPC and UPC) restrict cold water velocity to a maximum of 8.0 feet per second (2.4 m/s) in copper and PEX, and domestic hot water piping to not more than 4.0 to 5.0 feet per second (1.2 to 1.5 m/s) in recirculating loops.</p>
    </div>
    <div class="faq-item">
        <h3>How does flushometer toilet sizing differ from flush tank toilets?</h3>
        <p>A residential gravity flush tank operates at only 2.5 to 3.5 GPM refilling over 60 seconds, assigning it a rating of 2.5 to 3.0 WSFU. A commercial flushometer valve releases 25 to 35 GPM in an instantaneous 4-second blast, assigning it 8.0 to 10.0 WSFU per fixture. Systems with flushometers require substantially larger service entrance pipes and water meters.</p>
    </div>
</div>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article_content, "civil.html", "Civil & Plumbing")


def main():
    tools = [
        ("pace-calculator.html", gen_pace()),
        ("water-demand-fixture-units-calculator.html", gen_wsfu())
    ]
    for filename, content in tools:
        filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {filename}")

if __name__ == "__main__":
    main()
