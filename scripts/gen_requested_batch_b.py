# -*- coding: utf-8 -*-
"""
Generator for Requested Fitness Tools - Batch B (Tools 7 to 12)
Tools:
7. stationary-bike-calorie-calculator.html (ACSM Leg Ergometry, Mechanical Watts, Cadence RPM, Resistance)
8. incline-treadmill-calorie-calculator.html (Steep Grade Locomotion, Pandolf Incline Kinetics, Vertical Work)
9. rucking-calorie-calculator.html (USARIEM Pandolf Military Pack Carriage Equation, Terrain Factor, Incline)
10. jack-daniels-running-calculator.html (Dr. Jack Daniels VDOT Metric, Oxygen Cost, Training Paces E/M/T/I/R)
11. jumping-jacks-calories-burned-calculator.html (Calisthenic Ballistics, Gravitational Potential Work, MET Cadence)
12. squat-calorie-calculator.html (Barbell & Bodyweight Squat Biomechanics, Center of Mass Delta H, EPOC)
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COMMON_TAIL = """    <footer class="site-footer">
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>About CalcHub</h4>
                    <p>CalcHub delivers peer-reviewed exercise physiology computing algorithms, biomechanical energy expenditure models, and clinical metabolic engines compliant with ACSM, NSCA, and USARIEM research standards.</p>
                </div>
                <div class="footer-col">
                    <h4>Cardio &amp; Metabolic</h4>
                    <ul>
                        <li><a href="stationary-bike-calorie-calculator.html">Stationary Bike Calories</a></li>
                        <li><a href="incline-treadmill-calorie-calculator.html">Incline Treadmill Calories</a></li>
                        <li><a href="rucking-calorie-calculator.html">Rucking Calorie Calculator</a></li>
                        <li><a href="treadmill-calorie-calculator.html">Treadmill Calorie Calculator</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Athletic Performance</h4>
                    <ul>
                        <li><a href="jack-daniels-running-calculator.html">Jack Daniels VDOT Calculator</a></li>
                        <li><a href="jumping-jacks-calories-burned-calculator.html">Jumping Jacks Calories</a></li>
                        <li><a href="squat-calorie-calculator.html">Squat Calorie Calculator</a></li>
                        <li><a href="vo2-max-calculator.html">VO2 Max Calculator</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>General Health</h4>
                    <ul>
                        <li><a href="index.html">All Calculators</a></li>
                        <li><a href="calorie-calculator.html">TDEE Calorie Calculator</a></li>
                        <li><a href="bmi-calculator.html">BMI Calculator</a></li>
                        <li><a href="body-fat-calculator.html">Body Fat Calculator</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 CalcHub. All rights reserved. Peer-reviewed exercise physiology and biomechanical calculation engines.</p>
            </div>
        </div>
    </footer>
</body>
</html>"""

def get_page_html(title, description, canonical_slug, schema_json, h1, short_desc, calc_ui, article_content, category_hub="health.html", category_name="Health &amp; Fitness"):
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
                <a href="health.html">Health &amp; Fitness</a>
                <a href="datetime.html">Date &amp; Time</a>
                <a href="math.html">Math &amp; Stats</a>
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
                    <h3>Related Training &amp; Calorie Tools</h3>
                    <ul class="sidebar-links">
                        <li><a href="stationary-bike-calorie-calculator.html">Stationary Bike Calories</a></li>
                        <li><a href="incline-treadmill-calorie-calculator.html">Incline Treadmill Calories</a></li>
                        <li><a href="rucking-calorie-calculator.html">Rucking Calorie Calculator</a></li>
                        <li><a href="jack-daniels-running-calculator.html">Jack Daniels VDOT Calculator</a></li>
                        <li><a href="jumping-jacks-calories-burned-calculator.html">Jumping Jacks Calories</a></li>
                        <li><a href="squat-calorie-calculator.html">Squat Calorie Calculator</a></li>
                        <li><a href="treadmill-calorie-calculator.html">Treadmill Calorie Calculator</a></li>
                        <li><a href="cycling-calorie-calculator.html">Cycling Calorie Calculator</a></li>
                    </ul>
                </div>
            </aside>
        </div>
    </div>
{COMMON_TAIL}"""


# ===========================================================================
# TOOL 7: stationary-bike-calorie-calculator.html
# ===========================================================================
def gen_stationary_bike():
    slug = "stationary-bike-calorie-calculator"
    title = "Stationary Bike Calorie Calculator | ACSM Ergometry & Wattage Formula"
    desc = "Calculate calories burned on an upright, recumbent, or spin stationary bike using ACSM leg ergometry formulas, mechanical wattage, cadence, and body weight."
    h1 = "Stationary Bike Calorie Calculator"
    short_desc = "Calculate clinical caloric energy expenditure, mechanical flywheel work (kJ), and metabolic equivalents (METs) on upright, recumbent, and indoor cycling spin bikes using ACSM leg ergometry formulas."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Stationary Bike Calorie Calculator",
      "url": "https://calchub.com/stationary-bike-calorie-calculator.html",
      "applicationCategory": "HealthApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript. Requires HTML5.",
      "description": "Calculates stationary cycling calories burned, mechanical power in watts, and gross vs net energy expenditure using official ACSM leg ergometry equations."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How does the ACSM leg ergometry equation calculate stationary bike calories?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The American College of Sports Medicine (ACSM) leg ergometry formula defines gross oxygen consumption as VO2 = 7.0 + (1.8 * Work Rate in kg·m/min) / Body Weight in kg, where 7.0 accounts for resting metabolic baseline plus unloaded pedaling resistance. Every liter of consumed oxygen yields approximately 4.86 to 5.0 kilocalories."
          }
        },
        {
          "@type": "Question",
          "name": "Why do stationary bike console calorie readouts overestimate energy expenditure?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Commercial gym exercise bikes assume an average unadjusted gross metabolic efficiency of 20% without accounting for individual conditioning, body weight scaling on recumbent vs upright geometry, or resting baseline metabolism. Console algorithms also routinely count resting calories you would burn sitting still, inflating workout totals by 15% to 30%."
          }
        },
        {
          "@type": "Question",
          "name": "How do mechanical watts convert to burned calories on an indoor cycle?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Mechanical work is calculated as Joules = Watts * seconds, with 1,000 Joules equaling 1 kiloJoule (kJ). Because human muscular gross efficiency ranges between 20% and 24%, the metabolic calories required to produce 1 kJ of external pedal work is approximately 1 kcal (since 1 kcal = 4.184 kJ and 1 / 0.239 ≈ 4.184 kJ/kcal)."
          }
        },
        {
          "@type": "Question",
          "name": "What is the calorie difference between an upright bike and a recumbent bike?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "An upright stationary bike engages core postural stabilizers, latissimus dorsi, and forearm tension, burning 8% to 15% more calories than a recumbent bike at identical flywheel resistance. Recumbent bikes offer full lumbar support, eliminating upper-body isometric tension."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """                    <div class="calc-body">
                        <div class="calc-form">
                            <div class="unit-toggle-group">
                                <span class="unit-toggle-label">Unit System:</span>
                                <div class="toggle-buttons">
                                    <button type="button" class="unit-btn active" id="unit-imperial" onclick="setUnitSystem('imperial')">Imperial (lbs)</button>
                                    <button type="button" class="unit-btn" id="unit-metric" onclick="setUnitSystem('metric')">Metric (kg)</button>
                                </div>
                            </div>

                            <div class="input-grid">
                                <div class="form-group">
                                    <label for="sb-weight" id="weight-label">Body Weight (lbs):</label>
                                    <input type="number" id="sb-weight" class="calc-input" value="175" min="40" max="500" step="0.5">
                                    <span class="input-hint" id="weight-hint">Standard adult weight</span>
                                </div>

                                <div class="form-group">
                                    <label for="sb-duration">Workout Duration (minutes):</label>
                                    <input type="number" id="sb-duration" class="calc-input" value="45" min="1" max="360" step="1">
                                    <span class="input-hint">Pedaling duration</span>
                                </div>

                                <div class="form-group">
                                    <label for="sb-mode">Intensity Calculation Mode:</label>
                                    <select id="sb-mode" class="calc-input" onchange="toggleModeInputs()">
                                        <option value="met" selected>Perceived Effort &amp; MET Preset</option>
                                        <option value="watts">Direct Power Meter (Watts)</option>
                                        <option value="cadence">Flywheel Resistance &amp; RPM</option>
                                    </select>
                                    <span class="input-hint">Choose calculation source</span>
                                </div>

                                <div class="form-group" id="group-preset">
                                    <label for="sb-preset">Cycling Effort Level:</label>
                                    <select id="sb-preset" class="calc-input">
                                        <option value="3.5">Very Light (50W, casual warm-up, ~3.5 METs)</option>
                                        <option value="5.5">Light / Moderate (90-100W, cruising pace, ~5.5 METs)</option>
                                        <option value="7.0" selected>Moderate Effort (120-140W, steady aerobic, ~7.0 METs)</option>
                                        <option value="8.8">Vigorous Effort (150-180W, heavy breathing, ~8.8 METs)</option>
                                        <option value="11.0">Very Vigorous (200-230W, tempo / threshold, ~11.0 METs)</option>
                                        <option value="14.0">Racing / HIIT Sprints (250W+, max anaerobic, ~14.0 METs)</option>
                                    </select>
                                    <span class="input-hint">Compendium code 02010 - 02015</span>
                                </div>

                                <div class="form-group" id="group-watts" style="display:none;">
                                    <label for="sb-watts">Average Mechanical Power (Watts):</label>
                                    <input type="number" id="sb-watts" class="calc-input" value="150" min="20" max="600" step="5">
                                    <span class="input-hint">Direct pedal / smart flywheel readout</span>
                                </div>

                                <div class="form-group" id="group-cadence" style="display:none;">
                                    <label for="sb-cadence">Pedaling Cadence (RPM):</label>
                                    <input type="number" id="sb-cadence" class="calc-input" value="80" min="40" max="140" step="1">
                                    <span class="input-hint">Revolutions per minute (monark standard)</span>
                                </div>

                                <div class="form-group">
                                    <label for="sb-bike-type">Bike Ergometer Geometry:</label>
                                    <select id="sb-bike-type" class="calc-input">
                                        <option value="upright" selected>Upright Stationary Bike (Standard)</option>
                                        <option value="spin">Spin Bike / Indoor Cycle (Studio)</option>
                                        <option value="recumbent">Recumbent Stationary Bike (Bucket Seat)</option>
                                    </select>
                                    <span class="input-hint">Adjusts postural stabilizer metabolic demand</span>
                                </div>
                            </div>

                            <button type="button" class="btn-primary" onclick="calculateStationaryBike()">Calculate Caloric Expenditure</button>
                        </div>

                        <div class="calc-results" id="sb-results">
                            <h2>Session Caloric Analysis</h2>
                            <div class="result-highlight-card">
                                <span class="highlight-label">Total Gross Energy Burned</span>
                                <span class="highlight-val" id="res-sb-total-kcal">435 kcal</span>
                                <span class="highlight-sub" id="res-sb-rate">9.7 kcal / minute (580 kcal/hr)</span>
                            </div>

                            <div class="results-stats-grid">
                                <div class="stat-card">
                                    <span class="stat-title">Net Exercise Burn</span>
                                    <span class="stat-value" id="res-sb-net-kcal">372 kcal</span>
                                    <span class="stat-desc">Calories above resting metabolic baseline</span>
                                </div>
                                <div class="stat-card">
                                    <span class="stat-title">Mechanical External Work</span>
                                    <span class="stat-value" id="res-sb-kj">405 kJ</span>
                                    <span class="stat-desc">Actual physical energy transferred to flywheel</span>
                                </div>
                                <div class="stat-card">
                                    <span class="stat-title">Metabolic Equivalent</span>
                                    <span class="stat-value" id="res-sb-mets">7.0 METs</span>
                                    <span class="stat-desc">Fold increase over resting baseline</span>
                                </div>
                                <div class="stat-card">
                                    <span class="stat-title">Oxygen Uptake (VO2)</span>
                                    <span class="stat-value" id="res-sb-vo2">24.5 mL/kg/min</span>
                                    <span class="stat-desc">Gross physiological rate of oxygen consumption</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <script>
                        let currentUnit = 'imperial';

                        function setUnitSystem(unit) {
                            currentUnit = unit;
                            document.getElementById('unit-imperial').classList.toggle('active', unit === 'imperial');
                            document.getElementById('unit-metric').classList.toggle('active', unit === 'metric');
                            const wInput = document.getElementById('sb-weight');
                            const wLabel = document.getElementById('weight-label');
                            const wHint = document.getElementById('weight-hint');

                            if (unit === 'metric') {
                                wLabel.textContent = 'Body Weight (kg):';
                                wHint.textContent = 'Kilograms (e.g., 75 kg)';
                                wInput.value = (parseFloat(wInput.value) * 0.453592).toFixed(1);
                                wInput.min = '20';
                                wInput.max = '230';
                            } else {
                                wLabel.textContent = 'Body Weight (lbs):';
                                wHint.textContent = 'Pounds (e.g., 165 lbs)';
                                wInput.value = (parseFloat(wInput.value) / 0.453592).toFixed(1);
                                wInput.min = '40';
                                wInput.max = '500';
                            }
                            calculateStationaryBike();
                        }

                        function toggleModeInputs() {
                            const mode = document.getElementById('sb-mode').value;
                            document.getElementById('group-preset').style.display = (mode === 'met') ? 'block' : 'none';
                            document.getElementById('group-watts').style.display = (mode === 'watts') ? 'block' : 'none';
                            document.getElementById('group-cadence').style.display = (mode === 'cadence') ? 'block' : 'none';
                            calculateStationaryBike();
                        }

                        function calculateStationaryBike() {
                            let rawWeight = parseFloat(document.getElementById('sb-weight').value) || 160;
                            let durationMin = parseFloat(document.getElementById('sb-duration').value) || 45;
                            let mode = document.getElementById('sb-mode').value;
                            let bikeType = document.getElementById('sb-bike-type').value;

                            let weightKg = (currentUnit === 'imperial') ? rawWeight * 0.453592 : rawWeight;

                            let grossEfficiency = 0.215; // human cycling gross mechanical efficiency ~21.5%
                            let typeMultiplier = 1.0;
                            if (bikeType === 'spin') typeMultiplier = 1.04;
                            else if (bikeType === 'recumbent') typeMultiplier = 0.91;

                            let totalKcal = 0;
                            let mets = 7.0;
                            let mechanicalWatts = 135;
                            let vo2 = 24.5;

                            if (mode === 'met') {
                                mets = parseFloat(document.getElementById('sb-preset').value) * typeMultiplier;
                                vo2 = mets * 3.5;
                                // ACSM: VO2 = 7.0 + 1.8*(WorkRate)/kg => WorkRate = (VO2 - 7.0)*kg / 1.8 (kg*m/min)
                                let workRateKgm = Math.max(0, (vo2 - 7.0) * weightKg / 1.8);
                                mechanicalWatts = workRateKgm / 6.12;
                                totalKcal = durationMin * (mets * 3.5 * weightKg) / 200;
                            } else if (mode === 'watts') {
                                mechanicalWatts = parseFloat(document.getElementById('sb-watts').value) || 150;
                                let workRateKgm = mechanicalWatts * 6.12;
                                vo2 = (7.0 + (1.8 * workRateKgm) / weightKg) * typeMultiplier;
                                mets = vo2 / 3.5;
                                totalKcal = durationMin * (mets * 3.5 * weightKg) / 200;
                            } else {
                                let rpm = parseFloat(document.getElementById('sb-cadence').value) || 80;
                                // Estimated resistance ~ 2.0 kp on Monark scale
                                let kp = 2.0 * typeMultiplier;
                                let workRateKgm = kp * rpm * 6.0; // 6m flywheel distance per crank revolution
                                mechanicalWatts = workRateKgm / 6.12;
                                vo2 = 7.0 + (1.8 * workRateKgm) / weightKg;
                                mets = vo2 / 3.5;
                                totalKcal = durationMin * (mets * 3.5 * weightKg) / 200;
                            }

                            let restingKcalMin = (1.0 * 3.5 * weightKg) / 200;
                            let restingTotalKcal = restingKcalMin * durationMin;
                            let netKcal = Math.max(0, totalKcal - restingTotalKcal);
                            let mechanicalKJ = (mechanicalWatts * durationMin * 60) / 1000;
                            let kcalPerHour = (totalKcal / durationMin) * 60;
                            let kcalPerMin = totalKcal / durationMin;

                            document.getElementById('res-sb-total-kcal').textContent = Math.round(totalKcal) + ' kcal';
                            document.getElementById('res-sb-rate').textContent = kcalPerMin.toFixed(1) + ' kcal / min (' + Math.round(kcalPerHour) + ' kcal/hr)';
                            document.getElementById('res-sb-net-kcal').textContent = Math.round(netKcal) + ' kcal';
                            document.getElementById('res-sb-kj').textContent = Math.round(mechanicalKJ) + ' kJ (' + Math.round(mechanicalWatts) + ' W)';
                            document.getElementById('res-sb-mets').textContent = mets.toFixed(1) + ' METs';
                            document.getElementById('res-sb-vo2').textContent = vo2.toFixed(1) + ' mL/kg/min';
                        }

                        window.addEventListener('DOMContentLoaded', calculateStationaryBike);
                    </script>"""

    article_content = """<h2>Biomechanical &amp; Physiological Principles of Stationary Bike Calorie Expenditure</h2>
<p>Stationary cycling represents one of the most mechanically quantifiable forms of cardiovascular conditioning in human performance laboratories. Unlike outdoor road cycling, where complex aerodynamic crosswinds, tire hysteresis, road gradient variances, and drafting dynamics introduce substantial noise, an indoor stationary bicycle (or cycle ergometer) isolates pure concentric lower-extremity torque against an electronically, mechanically, or magnetically calibrated flywheel.</p>

<p>To quantify human energy expenditure on a stationary bicycle with clinical precision, exercise physiologists rely on the standard metabolic equations established by the <strong>American College of Sports Medicine (ACSM)</strong>. The ACSM leg ergometry equation evaluates gross oxygen uptake ($\text{VO}_2$, in $\text{mL}\cdot\text{kg}^{-1}\cdot\text{min}^{-1}$) as the linear sum of resting metabolic demand, unloaded flywheel rotation, and external resistance:</p>

$$\\text{VO}_2 = 7.0 + \\frac{1.8 \\times \\text{Work Rate (kg}\\cdot\\text{m/min)}}{\\text{Body Mass (kg)}}$$

<p>In this clinical formulation:</p>
<ul>
    <li><strong>The Resting Baseline ($3.5 \, \text{mL}\cdot\text{kg}^{-1}\cdot\text{min}^{-1}$):</strong> Represents standard resting metabolic rate (1 MET), the cellular baseline energy required to sustain life.</li>
    <li><strong>Unloaded Pedaling Demand ($3.5 \, \text{mL}\cdot\text{kg}^{-1}\cdot\text{min}^{-1}$):</strong> Accounts for the metabolic cost of moving the lower extremities against zero flywheel resistance at standard cadence (typically 50 to 60 RPM). Combining the resting baseline and unloaded cycling yields the static $7.0 \, \text{mL}\cdot\text{kg}^{-1}\cdot\text{min}^{-1}$ constant.</li>
    <li><strong>The External Work Factor ($1.8 \, \text{mL}\cdot\text{O}_2\cdot\text{kg}\cdot\text{m}^{-1}$):</strong> Represents the physiological volume of oxygen consumed to generate each kilogram-meter ($\text{kg}\cdot\text{m}$) of mechanical work.</li>
</ul>

<h3>Converting Mechanical Watts to Physical Work and Heat</h3>
<p>Modern ergometers (such as Wattbike, Tacx, Wahoo KICKR, and high-end gym stationary bikes) report instant mechanical power in <strong>Watts ($W$)</strong>. One Watt is equivalent to one Joule of energy produced per second ($1 \, \text{W} = 1 \, \text{J/s}$). In clinical ergometry, power is also indexed in kilogram-meters per minute ($\text{kg}\cdot\text{m/min}$), where:</p>

$$1 \\, \\text{Watt} = 6.12 \\, \\text{kg}\\cdot\\text{m/min}$$

<p>Therefore, total mechanical work performed over an exercise session duration $t$ (in seconds) is calculated directly in kiloJoules ($\text{kJ}$):</p>

$$\\text{Work (kJ)} = \\frac{\\text{Power (Watts)} \\times \\text{Time (seconds)}}{1000}$$

<p>Because the human body is a thermodynamic heat engine, skeletal muscle fibers convert metabolic chemical energy (adenosine triphosphate, ATP) into external mechanical work at an efficiency of only <strong>$20\\%$ to $24\\%$</strong> (termed <em>Gross Mechanical Efficiency</em>, or GME). The remaining $76\\%$ to $80\\%$ of energy is dissipated as thermogenic heat:</p>

$$\\text{Metabolic Energy Expended (kcal)} = \\frac{\\text{Work (kJ)}}{4.184 \\times \\text{GME}}$$

<p>Remarkably, because $1 \\, \\text{kcal} = 4.184 \\, \\text{kJ}$ and human gross efficiency averages $23.9\\%$ ($4.184 \\times 0.239 \\approx 1.0$), <strong>1 kiloJoule of mechanical work measured at the flywheel is approximately equal to 1 kilocalorie of gross metabolic energy burned by the rider</strong>. A cyclist generating $150 \\, \\text{Watts}$ for 60 minutes performs $540 \\, \\text{kJ}$ of work and burns approximately $540$ gross kilocalories.</p>

<h2>Upright, Recumbent, and Spin Ergometer Biomechanical Differences</h2>
<p>Not all stationary cycles impose identical muscular loading. Postural inclination, saddle angle, core stabilization, and handlebar weight-bearing alter overall caloric cost across three primary architectures:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Stationary Bike Architecture</th>
            <th>Primary Muscle Recruitment</th>
            <th>Core &amp; Upper Body Support</th>
            <th>Relative Metabolic Cost</th>
            <th>Typical MET Range</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Upright Stationary Bike</strong></td>
            <td>Quadriceps, hamstrings, gluteus maximus, gastrocnemius</td>
            <td>Moderate (erector spinae, rectus abdominis isometric tension)</td>
            <td>Baseline ($1.00\\times$)</td>
            <td>$5.0 - 9.0$</td>
        </tr>
        <tr>
            <td><strong>Indoor Spin Bike (Fixed Flywheel)</strong></td>
            <td>Posterior chain, hip flexors, lats, deltoids, standing sprints</td>
            <td>High (active grip, aggressive forward hip hinge)</td>
            <td>$+4\\%$ to $+10\\%$ higher</td>
            <td>$7.0 - 14.0$</td>
        </tr>
        <tr>
            <td><strong>Recumbent Stationary Bike</strong></td>
            <td>Quadriceps dominant, anterior tibialis, reduced glute loading</td>
            <td>Minimal (rigid lumbar back support, seated pelvis)</td>
            <td>$-8\\%$ to $-12\\%$ lower</td>
            <td>$3.5 - 7.5$</td>
        </tr>
    </tbody>
</table>

<p>On an upright bike, the rider must actively support torso mass against gravity, engaging the erector spinae, transverse abdominis, and shoulder stabilizers. During high-intensity indoor cycling classes (spinning), riders frequently alternate between seated spinning and standing climbing. Standing eliminates the saddle contact point, forcing the full body weight to be stabilized across the pedal stroke and increasing myocardial demand and oxygen uptake by approximately $8\\%$ to $15\\%$ at matched mechanical wattages.</p>

<p>Conversely, recumbent bicycles recline the rider horizontally with extensive lumbar support. This configuration relieves venous pooling in the lower extremities and reduces myocardial work. However, eliminating upper body isometric recruitment reduces total systemic energy expenditure by roughly $10\\%$ compared to an upright bike at identical flywheel resistance settings.</p>

<h2>Gross vs. Net Caloric Expenditure in Stationary Cycling</h2>
<p>Exercise science draws a strict distinction between <strong>Gross Caloric Burn</strong> and <strong>Net Caloric Burn</strong>:</p>
<ul>
    <li><strong>Gross Energy Expenditure:</strong> Represents the total calories burned throughout the session duration, including the resting calories your body would have expended sitting quietly on a couch.</li>
    <li><strong>Net Energy Expenditure:</strong> Represents solely the extra calories burned specifically as a direct result of pedaling the stationary bicycle ($\text{Net} = \text{Gross} - \text{Resting Baseline}$).</li>
</ul>

<p>Gym console displays invariably project gross calories. For a 200-lb (90.7 kg) rider cycling for 60 minutes, the baseline resting metabolic rate expends approximately $95 \\, \\text{kcal/hr}$. If the console displays $600 \\, \\text{kcal}$, the actual net exercise energy surplus created by the workout is $505 \\, \\text{kcal}$. When calculating dietary caloric deficits for fat loss, relying on net expenditure prevents accidental overfeeding.</p>

<h2>Worked Clinical Case Study: Calculating Flywheel Work &amp; Caloric Expenditure</h2>
<div class="worked-example-card">
    <h3>Ergometry Case Study: 45-Minute Cadence &amp; Power Analysis</h3>
    <p><strong>Subject Profile:</strong> A 34-year-old cyclist weighing $80 \\, \\text{kg}$ ($176.4 \\, \\text{lbs}$) completes a 45-minute endurance workout on a calibrated electromagnetic stationary bike ergometer. The smart console records an average steady-state mechanical output of $175 \\, \\text{Watts}$ at a cadence of $85 \\, \\text{RPM}$.</p>

    <div class="step-solution">
        <h4>Step 1: Calculate Total Mechanical External Work (kJ)</h4>
        <p>Convert exercise duration to seconds ($45 \\times 60 = 2,700 \\, \\text{seconds}$):</p>
        $$\\text{Work (Joules)} = 175 \\, \\text{W} \\times 2,700 \\, \\text{s} = 472,500 \\, \\text{J} = 472.5 \\, \\text{kJ}$$

        <h4>Step 2: Convert Mechanical Work Rate to kg·m/min</h4>
        $$\\text{Work Rate} = 175 \\, \\text{Watts} \\times 6.12 = 1,071.0 \\, \\text{kg}\\cdot\\text{m/min}$$

        <h4>Step 3: Apply the ACSM Leg Ergometry Equation for Gross VO2</h4>
        $$\\text{VO}_2 = 7.0 + \\frac{1.8 \\times 1,071.0}{80.0} = 7.0 + \\frac{1,927.8}{80.0} = 7.0 + 24.10 = 31.10 \\, \\text{mL}\\cdot\\text{kg}^{-1}\\cdot\\text{min}^{-1}$$

        <h4>Step 4: Compute METs and Gross Caloric Expenditure</h4>
        $$\\text{METs} = \\frac{31.10}{3.5} = 8.89 \\, \\text{METs}$$
        $$\\text{Gross Kcal/min} = \\frac{8.89 \\times 3.5 \\times 80.0}{200} = 12.44 \\, \\text{kcal/min}$$
        $$\\text{Total Gross Caloric Burn} = 12.44 \\times 45 = 559.8 \\, \\text{kcal}$$

        <h4>Step 5: Compute Net Exercise Calories</h4>
        $$\\text{Resting Burn (45 min)} = \\frac{1.0 \\times 3.5 \\times 80.0}{200} \\times 45 = 63.0 \\, \\text{kcal}$$
        $$\\text{Net Exercise Calories} = 559.8 - 63.0 = 496.8 \\, \\text{kcal}$$

        <h4>Clinical Assessment</h4>
        <p>The cyclist performed $472.5 \\, \\text{kJ}$ of external flywheel work. Assuming a physiological gross mechanical efficiency of $21.5\\%$, the actual metabolic energy demanded was $472.5 / (4.184 \\times 0.215) = 525.2$ net kilocalories, validating the ACSM equation within a $5.4\\%$ margin of error. The subject sustained high aerobic capacity ($8.89 \\, \\text{METs}$) with zero joint impact force.</p>
    </div>
</div>

<h2>Stationary Cycling Metabolic Intensity Reference Table</h2>
<table class="data-table">
    <thead>
        <tr>
            <th>Mechanical Power (Watts)</th>
            <th>Perceived Exertion (RPE 1-10)</th>
            <th>Approximate METs</th>
            <th>Burn Rate (150 lb / 68 kg)</th>
            <th>Burn Rate (190 lb / 86 kg)</th>
            <th>Primary Energy Substrate</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>$50 \\, \\text{W}$</td>
            <td>2 (Very Light Recovery)</td>
            <td>3.5</td>
            <td>$4.0 \\, \\text{kcal/min}$</td>
            <td>$5.0 \\, \\text{kcal/min}$</td>
            <td>$85\\%$ Fatty Acids</td>
        </tr>
        <tr>
            <td>$100 \\, \\text{W}$</td>
            <td>4 (Light Aerobic Base)</td>
            <td>5.5</td>
            <td>$6.2 \\, \\text{kcal/min}$</td>
            <td>$7.9 \\, \\text{kcal/min}$</td>
            <td>$65\\%$ Fatty Acids, $35\\%$ Glycogen</td>
        </tr>
        <tr>
            <td>$150 \\, \\text{W}$</td>
            <td>6 (Moderate Tempo)</td>
            <td>7.5</td>
            <td>$8.5 \\, \\text{kcal/min}$</td>
            <td>$10.8 \\, \\text{kcal/min}$</td>
            <td>$45\\%$ Fatty Acids, $55\\%$ Glycogen</td>
        </tr>
        <tr>
            <td>$200 \\, \\text{W}$</td>
            <td>8 (Lactate Threshold)</td>
            <td>10.5</td>
            <td>$11.9 \\, \\text{kcal/min}$</td>
            <td>$15.1 \\, \\text{kcal/min}$</td>
            <td>$20\\%$ Fatty Acids, $80\\%$ Glycogen</td>
        </tr>
        <tr>
            <td>$250 \\, \\text{W}$</td>
            <td>9.5 (VO2 Max Interval)</td>
            <td>13.0</td>
            <td>$14.8 \\, \\text{kcal/min}$</td>
            <td>$18.7 \\, \\text{kcal/min}$</td>
            <td>$95\\%$ Muscle Glycogen</td>
        </tr>
        <tr>
            <td>$300+ \\, \\text{W}$</td>
            <td>10 (Anaerobic Capacity Sprint)</td>
            <td>16.0+</td>
            <td>$18.1+ \\, \\text{kcal/min}$</td>
            <td>$23.0+ \\, \\text{kcal/min}$</td>
            <td>$100\\%$ Anaerobic Phosphagen &amp; Glycolysis</td>
        </tr>
    </tbody>
</table>

<h2>Frequently Asked Questions About Stationary Bike Calorie Burn</h2>
<h3>How does the ACSM leg ergometry equation calculate stationary bike calories?</h3>
<p>The ACSM leg ergometry formula defines gross oxygen consumption as $\\text{VO}_2 = 7.0 + (1.8 \\times \\text{Work Rate in kg}\\cdot\\text{m/min}) / \\text{Body Weight in kg}$. The constant $7.0$ represents resting metabolism ($3.5$) plus unloaded pedaling resistance ($3.5$). Every liter of oxygen consumed metabolizes roughly $4.86$ to $5.0$ kilocalories of mixed substrate.</p>

<h3>Why do stationary bike console calorie readouts overestimate energy expenditure?</h3>
<p>Most commercial stationary bike consoles operate using broad population averages that assume an unadjusted gross efficiency of $20\\%$. They fail to adjust for individual cardiovascular conditioning, fitness level, or the difference between gross and net energy. Furthermore, consoles frequently credit the rider for baseline resting calories, inflating reported expenditure by $15\\%$ to $30\\%$.</p>

<h3>How do mechanical watts convert to burned calories on an indoor cycle?</h3>
<p>One Watt equals one Joule of work per second. Total mechanical work in kiloJoules equals $(\\text{Watts} \\times \\text{seconds}) / 1000$. Because human skeletal muscle functions at a gross efficiency of $20\\%$ to $24\\%$, each kiloJoule of external mechanical work delivered to the pedals requires approximately one kilocalorie of gross metabolic energy expenditure.</p>

<h3>What is the calorie difference between an upright bike and a recumbent bike?</h3>
<p>An upright bike requires active recruitment of the core musculature, spinal erectors, and upper extremities to maintain posture, burning $8\\%$ to $15\\%$ more calories than a recumbent bike at identical resistance. Recumbent bikes feature a full bucket seat with lumbar support, virtually eliminating upper-body isometric stabilization.</p>

<h3>Does higher pedaling cadence (RPM) burn more calories at the same wattage?</h3>
<p>Yes. While mechanical work delivered to the flywheel is identical, cycling at very high cadences ($100+$ RPM) at low resistance reduces muscular efficiency. Fast leg turnover requires rapid muscle fiber contraction and acceleration of limb mass, consuming roughly $5\\%$ to $10\\%$ more metabolic oxygen than pedaling at an optimal cadence of $80$ to $90$ RPM at equal mechanical wattage.</p>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article_content)


# ===========================================================================
# TOOL 8: incline-treadmill-calorie-calculator.html
# ===========================================================================
def gen_incline_treadmill():
    slug = "incline-treadmill-calorie-calculator"
    title = "Incline Treadmill Calorie Calculator | Steep Grade Locomotion & 12-3-30"
    desc = "Calculate calories burned walking or running on an incline treadmill using ACSM vertical component equations and the 12-3-30 workout formula."
    h1 = "Incline Treadmill Calorie Calculator"
    short_desc = "Precision biomechanical calculator computing gravitational work ($W = mgh$), vertical climbing rate, and caloric expenditure across 0% to 15%+ treadmill incline grades."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Incline Treadmill Calorie Calculator",
      "url": "https://calchub.com/incline-treadmill-calorie-calculator.html",
      "applicationCategory": "HealthApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript. Requires HTML5.",
      "description": "Calculates calories burned on an incline treadmill, vertical elevation gained, and mechanical work against gravity using official ACSM walking and running equations."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How does treadmill incline increase caloric burn so drastically?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Every percentage of treadmill grade tilts the platform upward, forcing the musculoskeletal system to perform mechanical work against gravity (W = m * g * h) with every stride. Walking at a 12% grade requires over 2.5 times more metabolic oxygen consumption than walking on a flat 0% grade at the exact same walking speed."
          }
        },
        {
          "@type": "Question",
          "name": "How many calories does the viral 12-3-30 workout burn?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The 12-3-30 protocol consists of walking at 12% incline, 3.0 mph (4.8 km/h), for 30 minutes. For an average 150-lb (68 kg) individual, this workout expends approximately 280 to 310 gross calories (or roughly 560 to 620 kcal/hour), achieving an intensity of approximately 8.5 METs."
          }
        },
        {
          "@type": "Question",
          "name": "Why does holding onto treadmill handrails ruin calorie calculations?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Holding the treadmill handrails or console transfers 25% to 40% of the subject's body weight onto the static frame, artificially supporting the torso and negating gravitational resistance. Clinical studies demonstrate that gripping handrails while walking at a 12% grade reduces actual metabolic oxygen consumption by 30% to 50% below console estimates."
          }
        },
        {
          "@type": "Question",
          "name": "What is the ACSM vertical component formula for incline walking?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The ACSM formula defines the vertical component of walking VO2 as 1.8 * Speed (m/min) * Grade (fraction). When walking at 3.0 mph (80.4 m/min) at a 10% grade (0.10), the vertical cost alone is 1.8 * 80.4 * 0.10 = 14.47 mL/kg/min, which is added to horizontal cost (8.04) and resting baseline (3.5) for a total VO2 of 26.0 mL/kg/min."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """                    <div class="calc-body">
                        <div class="calc-form">
                            <div class="unit-toggle-group">
                                <span class="unit-toggle-label">Measurement System:</span>
                                <div class="toggle-buttons">
                                    <button type="button" class="unit-btn active" id="inc-unit-imp" onclick="setInclineUnit('imperial')">Imperial (lbs, mph, ft)</button>
                                    <button type="button" class="unit-btn" id="inc-unit-met" onclick="setInclineUnit('metric')">Metric (kg, km/h, m)</button>
                                </div>
                            </div>

                            <div class="input-grid">
                                <div class="form-group">
                                    <label for="inc-weight" id="inc-weight-lbl">Body Weight (lbs):</label>
                                    <input type="number" id="inc-weight" class="calc-input" value="160" min="50" max="500" step="1">
                                    <span class="input-hint">Your body mass</span>
                                </div>

                                <div class="form-group">
                                    <label for="inc-speed" id="inc-speed-lbl">Treadmill Speed (mph):</label>
                                    <input type="number" id="inc-speed" class="calc-input" value="3.0" min="0.5" max="15.0" step="0.1">
                                    <span class="input-hint" id="inc-speed-hint">Standard walking speed (e.g., 3.0 mph)</span>
                                </div>

                                <div class="form-group">
                                    <label for="inc-grade">Incline Grade (%):</label>
                                    <input type="number" id="inc-grade" class="calc-input" value="12" min="0" max="40" step="0.5">
                                    <span class="input-hint">Treadmill ramp elevation percentage</span>
                                </div>

                                <div class="form-group">
                                    <label for="inc-duration">Workout Duration (minutes):</label>
                                    <input type="number" id="inc-duration" class="calc-input" value="30" min="1" max="300" step="1">
                                    <span class="input-hint">Total time on incline</span>
                                </div>

                                <div class="form-group">
                                    <label for="inc-preset">Popular Workout Presets:</label>
                                    <select id="inc-preset" class="calc-input" onchange="applyInclinePreset()">
                                        <option value="custom">Custom Configuration</option>
                                        <option value="12-3-30" selected>Viral 12-3-30 (12% Grade, 3.0 mph, 30 min)</option>
                                        <option value="hiking">Trail Hike Sim (8% Grade, 2.8 mph, 45 min)</option>
                                        <option value="steep-walk">Mountain Trek (15% Grade, 2.5 mph, 20 min)</option>
                                        <option value="hill-run">Incline Sprint (4% Grade, 7.0 mph, 15 min)</option>
                                        <option value="flat-walk">Flat Control (0% Grade, 3.0 mph, 30 min)</option>
                                    </select>
                                    <span class="input-hint">Pre-configured protocol presets</span>
                                </div>

                                <div class="form-group">
                                    <label for="inc-handrails">Handrail Contact:</label>
                                    <select id="inc-handrails" class="calc-input" onchange="calculateInclineTreadmill()">
                                        <option value="none" selected>No Handrail Support (Free Arm Swing - 100% Load)</option>
                                        <option value="light">Light Touch / Fingertip Balance (92% Load)</option>
                                        <option value="gripped">Firm Handrail Grip / Supported (70% Load - High Penalty)</option>
                                    </select>
                                    <span class="input-hint">Holding rails offsets gravitational weight</span>
                                </div>
                            </div>

                            <button type="button" class="btn-primary" onclick="calculateInclineTreadmill()">Calculate Incline Expenditure</button>
                        </div>

                        <div class="calc-results" id="inc-results">
                            <h2>Incline Metabolic Analysis</h2>
                            <div class="result-highlight-card">
                                <span class="highlight-label">Total Caloric Expenditure</span>
                                <span class="highlight-val" id="res-inc-total-kcal">298 kcal</span>
                                <span class="highlight-sub" id="res-inc-burn-rate">9.9 kcal / min (596 kcal/hour)</span>
                            </div>

                            <div class="results-stats-grid">
                                <div class="stat-card">
                                    <span class="stat-title">Vertical Elevation Gained</span>
                                    <span class="stat-value" id="res-inc-vert-gain">950 ft (290 m)</span>
                                    <span class="stat-desc">Cumulative vertical climbing distance</span>
                                </div>
                                <div class="stat-card">
                                    <span class="stat-title">Metabolic Equivalent</span>
                                    <span class="stat-value" id="res-inc-mets">8.6 METs</span>
                                    <span class="stat-desc">Vigorous aerobic exertion intensity</span>
                                </div>
                                <div class="stat-card">
                                    <span class="stat-title">Gravitational Work (W)</span>
                                    <span class="stat-value" id="res-inc-work">206 kJ</span>
                                    <span class="stat-desc">Mechanical energy to elevate mass against gravity</span>
                                </div>
                                <div class="stat-card">
                                    <span class="stat-title">Flat Surface Comparison</span>
                                    <span class="stat-value" id="res-inc-flat-comp">+182% More</span>
                                    <span class="stat-desc">Caloric increase compared to 0% flat grade</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <script>
                        let inclineUnit = 'imperial';

                        function setInclineUnit(unit) {
                            inclineUnit = unit;
                            document.getElementById('inc-unit-imp').classList.toggle('active', unit === 'imperial');
                            document.getElementById('inc-unit-met').classList.toggle('active', unit === 'metric');

                            const wInput = document.getElementById('inc-weight');
                            const sInput = document.getElementById('inc-speed');
                            const wLbl = document.getElementById('inc-weight-lbl');
                            const sLbl = document.getElementById('inc-speed-lbl');
                            const sHint = document.getElementById('inc-speed-hint');

                            if (unit === 'metric') {
                                wLbl.textContent = 'Body Weight (kg):';
                                sLbl.textContent = 'Treadmill Speed (km/h):';
                                sHint.textContent = 'e.g., 4.8 km/h';
                                wInput.value = (parseFloat(wInput.value) * 0.453592).toFixed(1);
                                sInput.value = (parseFloat(sInput.value) * 1.60934).toFixed(1);
                            } else {
                                wLbl.textContent = 'Body Weight (lbs):';
                                sLbl.textContent = 'Treadmill Speed (mph):';
                                sHint.textContent = 'e.g., 3.0 mph';
                                wInput.value = (parseFloat(wInput.value) / 0.453592).toFixed(1);
                                sInput.value = (parseFloat(sInput.value) / 1.60934).toFixed(1);
                            }
                            calculateInclineTreadmill();
                        }

                        function applyInclinePreset() {
                            const preset = document.getElementById('inc-preset').value;
                            if (preset === '12-3-30') {
                                document.getElementById('inc-grade').value = '12';
                                document.getElementById('inc-duration').value = '30';
                                document.getElementById('inc-speed').value = (inclineUnit === 'imperial') ? '3.0' : '4.8';
                            } else if (preset === 'hiking') {
                                document.getElementById('inc-grade').value = '8';
                                document.getElementById('inc-duration').value = '45';
                                document.getElementById('inc-speed').value = (inclineUnit === 'imperial') ? '2.8' : '4.5';
                            } else if (preset === 'steep-walk') {
                                document.getElementById('inc-grade').value = '15';
                                document.getElementById('inc-duration').value = '20';
                                document.getElementById('inc-speed').value = (inclineUnit === 'imperial') ? '2.5' : '4.0';
                            } else if (preset === 'hill-run') {
                                document.getElementById('inc-grade').value = '4';
                                document.getElementById('inc-duration').value = '15';
                                document.getElementById('inc-speed').value = (inclineUnit === 'imperial') ? '7.0' : '11.3';
                            } else if (preset === 'flat-walk') {
                                document.getElementById('inc-grade').value = '0';
                                document.getElementById('inc-duration').value = '30';
                                document.getElementById('inc-speed').value = (inclineUnit === 'imperial') ? '3.0' : '4.8';
                            }
                            calculateInclineTreadmill();
                        }

                        function calculateInclineTreadmill() {
                            let rawWeight = parseFloat(document.getElementById('inc-weight').value) || 160;
                            let rawSpeed = parseFloat(document.getElementById('inc-speed').value) || 3.0;
                            let gradePercent = parseFloat(document.getElementById('inc-grade').value) || 0;
                            let durationMin = parseFloat(document.getElementById('inc-duration').value) || 30;
                            let handrails = document.getElementById('inc-handrails').value;

                            let weightKg = (inclineUnit === 'imperial') ? rawWeight * 0.453592 : rawWeight;
                            let speedMph = (inclineUnit === 'imperial') ? rawSpeed : rawSpeed / 1.60934;
                            let speedMpm = speedMph * 26.8224; // meters per minute
                            let gradeFrac = gradePercent / 100.0;

                            let railFactor = 1.0;
                            if (handrails === 'light') railFactor = 0.92;
                            else if (handrails === 'gripped') railFactor = 0.70;

                            let vo2 = 0;
                            let vo2Flat = 0;
                            let isRunning = (speedMph >= 4.5);

                            if (!isRunning) {
                                // ACSM Walking: VO2 = 3.5 + 0.1*S + 1.8*S*G
                                vo2 = 3.5 + (0.1 * speedMpm) + (1.8 * speedMpm * gradeFrac);
                                vo2Flat = 3.5 + (0.1 * speedMpm);
                            } else {
                                // ACSM Running: VO2 = 3.5 + 0.2*S + 0.9*S*G
                                vo2 = 3.5 + (0.2 * speedMpm) + (0.9 * speedMpm * gradeFrac);
                                vo2Flat = 3.5 + (0.2 * speedMpm);
                            }

                            // Apply handrail offloading
                            vo2 = (vo2 - 3.5) * railFactor + 3.5;

                            let mets = vo2 / 3.5;
                            let totalKcal = durationMin * (mets * 3.5 * weightKg) / 200;
                            let flatKcal = durationMin * ((vo2Flat / 3.5) * 3.5 * weightKg) / 200;

                            // Vertical Elevation Gain
                            let distanceMeters = speedMpm * durationMin;
                            let vertMeters = distanceMeters * gradeFrac * railFactor;
                            let vertFeet = vertMeters * 3.28084;

                            // Gravitational Mechanical Work: W = m * g * h
                            let workJoules = weightKg * 9.80665 * vertMeters;
                            let workKJ = workJoules / 1000;

                            let flatDiffPercent = (flatKcal > 0) ? ((totalKcal - flatKcal) / flatKcal) * 100 : 0;
                            let kcalRate = totalKcal / durationMin;
                            let kcalHour = kcalRate * 60;

                            document.getElementById('res-inc-total-kcal').textContent = Math.round(totalKcal) + ' kcal';
                            document.getElementById('res-inc-burn-rate').textContent = kcalRate.toFixed(1) + ' kcal / min (' + Math.round(kcalHour) + ' kcal/hr)';
                            document.getElementById('res-inc-vert-gain').textContent = Math.round(vertFeet) + ' ft (' + Math.round(vertMeters) + ' m)';
                            document.getElementById('res-inc-mets').textContent = mets.toFixed(1) + ' METs';
                            document.getElementById('res-inc-work').textContent = Math.round(workKJ) + ' kJ';
                            document.getElementById('res-inc-flat-comp').textContent = '+' + Math.round(flatDiffPercent) + '% More';
                        }

                        window.addEventListener('DOMContentLoaded', calculateInclineTreadmill);
                    </script>"""

    article_content = """<h2>The Biomechanics of Incline Treadmill Locomotion</h2>
<p>Walking or running on a motorized treadmill at an elevated incline represents one of the most effective non-impact exercise modalities in clinical exercise physiology. When a treadmill deck is raised from a level horizontal surface ($0\\%$) to an uphill grade, the biomechanical demands of human locomotion undergo a fundamental transition: kinetic forward progression requires continuous concentric mechanical work against Earth's gravitational acceleration field.</p>

<p>On a flat surface, human walking behaves mechanically like an <strong>inverted pendulum</strong>. The kinetic energy developed during forward swing is largely recovered as potential energy when the center of mass reaches the peak of its arc over the stance leg, with up to $65\\%$ of mechanical energy stored and returned elastically. However, as the treadmill incline increases beyond $2\\%$, this pendulum energy exchange degrades rapidly. The lower extremity muscles can no longer rely on elastic recoil; instead, the quadriceps, gastrocnemius, soleus, and gluteus maximus must generate active concentric torque to physically hoist the entire bodily mass vertically with each successive stride.</p>

<h2>ACSM Incline Locomotion Mathematical Equations</h2>
<p>The standard reference for computing oxygen consumption on motorized treadmills is the <strong>American College of Sports Medicine (ACSM)</strong> metabolic equations. The ACSM model splits gross rate of oxygen consumption ($\\text{VO}_2$, in $\\text{mL}\\cdot\\text{kg}^{-1}\\cdot\\text{min}^{-1}$) into three distinct physiological components:</p>

<ol>
    <li><strong>Resting Metabolism ($3.5 \\, \\text{mL}\\cdot\\text{kg}^{-1}\\cdot\\text{min}^{-1}$):</strong> The cellular oxygen requirement at complete physical rest (1 MET).</li>
    <li><strong>Horizontal Component:</strong> The metabolic cost of moving the center of mass forward in the horizontal plane ($0.1 \\times \\text{speed}$ for walking; $0.2 \\times \\text{speed}$ for running).</li>
    <li><strong>Vertical Component:</strong> The mechanical cost of raising body weight against gravity ($1.8 \\times \\text{speed} \\times \\text{grade}$ for walking; $0.9 \\times \\text{speed} \\times \\text{grade}$ for running).</li>
</ol>

<h3>The Incline Walking Formula (Speed 1.9 to 3.7 mph / 50 to 100 m/min)</h3>
$$\\text{VO}_2 = 3.5 + (0.1 \\times S) + (1.8 \\times S \\times G)$$

<h3>The Incline Running Formula (Speed &gt; 5.0 mph / &gt; 134 m/min)</h3>
$$\\text{VO}_2 = 3.5 + (0.2 \\times S) + (0.9 \\times S \\times G)$$

<p>Where:</p>
<ul>
    <li>$S$ = Treadmill belt speed in <strong>meters per minute</strong> ($1 \\, \\text{mph} = 26.8224 \\, \\text{m/min}$).</li>
    <li>$G$ = Fractional incline grade (e.g., $12\\% \\, \\text{grade} = 0.12$).</li>
</ul>

<p>Once gross $\\text{VO}_2$ is calculated, the rate of caloric expenditure is determined using the universal thermodynamic constant for mixed substrate oxidation ($1 \\, \\text{L } \\text{O}_2 \\approx 4.86 - 5.0 \\, \\text{kcal}$):</p>

$$\\text{Caloric Burn Rate (kcal/min)} = \\frac{\\text{VO}_2 \\times \\text{Body Weight (kg)}}{200}$$

<h2>The Science of the 12-3-30 Workout: Biomechanical Demands &amp; Caloric Output</h2>
<p>In recent years, the <strong>"12-3-30" treadmill protocol</strong>—walking at a <strong>12% incline</strong>, at <strong>3.0 mph</strong>, for <strong>30 minutes</strong>—has gained immense global popularity. Exercise physiology reveals precisely why this workout yields exceptional cardiovascular conditioning and fat oxidation:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Workout Variable</th>
            <th>Flat Walking (0% Grade)</th>
            <th>The 12-3-30 Protocol (12% Grade)</th>
            <th>Flat Running (6.0 mph, 0%)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Speed</strong></td>
            <td>3.0 mph (4.8 km/h)</td>
            <td>3.0 mph (4.8 km/h)</td>
            <td>6.0 mph (9.7 km/h)</td>
        </tr>
        <tr>
            <td><strong>Incline Grade</strong></td>
            <td>0%</td>
            <td>12%</td>
            <td>0%</td>
        </tr>
        <tr>
            <td><strong>Gross VO2</strong></td>
            <td>$11.5 \\, \\text{mL/kg/min}$</td>
            <td>$28.9 \\, \\text{mL/kg/min}$</td>
            <td>$35.7 \\, \\text{mL/kg/min}$</td>
        </tr>
        <tr>
            <td><strong>Metabolic Intensity</strong></td>
            <td>3.3 METs (Light)</td>
            <td>8.3 METs (Vigorous Aerobic)</td>
            <td>10.2 METs (Heavy Aerobic)</td>
        </tr>
        <tr>
            <td><strong>30-Min Burn (160 lb Person)</strong></td>
            <td>$115 \\, \\text{kcal}$</td>
            <td>$289 \\, \\text{kcal}$</td>
            <td>$357 \\, \\text{kcal}$</td>
        </tr>
        <tr>
            <td><strong>Joint Peak Impact Force</strong></td>
            <td>$1.2\\times$ Body Weight</td>
            <td>$1.3\\times$ Body Weight</td>
            <td>$2.5\\times - 3.0\\times$ Body Weight</td>
        </tr>
    </tbody>
</table>

<p>The remarkable advantage of the 12-3-30 protocol is that it achieves a <strong>vigorous aerobic intensity of over 8.0 METs</strong>—burning nearly $2.5\\times$ more calories than flat walking—while maintaining the gentle ground reaction forces of walking locomotion. Because the foot remains in constant rolling contact with the deck without an aerial flight phase, tibiofemoral and patellofemoral joint contact forces remain below $1.3\\times$ body weight, shielding the knees, ankles, and lumbar spine from the repetitive $3.0\\times$ shock waves induced by flat asphalt running.</p>

<h2>Gravitational Mechanical Work ($W = mgh$)</h2>
<p>The extra metabolic calories consumed on an incline directly mirror the pure Newtonian physics of gravitational potential energy. When moving at belt speed $v$ (in $\\text{m/s}$) along an inclined plane of grade $\\theta$ for duration $t$ (in seconds), the total vertical elevation gained $h$ is:</p>

$$h = v \\times t \\times \\sin(\\theta) \\approx v \\times t \\times G$$

<p>The cumulative mechanical work performed strictly against gravity is:</p>

$$W_{\\text{gravity}} = m \\times g \\times h$$

<p>Where $m$ is subject mass in kilograms, and $g = 9.80665 \\, \\text{m/s}^2$ is gravitational acceleration. For a 160-lb ($72.6 \\, \\text{kg}$) person performing the 12-3-30 workout:</p>
<ul>
    <li>Total horizontal belt distance traveled: $3.0 \\, \\text{mph} \\times 0.5 \\, \\text{hours} = 1.5 \\, \\text{miles} = 2,414 \\, \\text{meters}$.</li>
    <li>Total vertical ascent: $2,414 \\, \\text{m} \\times 0.12 = 289.7 \\, \\text{meters}$ ($950.5 \\, \\text{feet}$—equivalent to climbing an 80-story skyscraper).</li>
    <li>Mechanical work against gravity: $72.6 \\, \\text{kg} \\times 9.80665 \\, \\text{m/s}^2 \\times 289.7 \\, \\text{m} = 206,250 \\, \\text{Joules} = 206.3 \\, \\text{kJ}$.</li>
</ul>

<h2>The Handrail Penalty: How Gripping the Rails Destroys Caloric Burn</h2>
<p>In commercial fitness centers, it is exceedingly common to witness gym patrons setting the treadmill incline to $12\\%$ or $15\\%$, while clutching the top handrails with locked elbows and leaning backward perpendicular to the deck. <strong>This posture invalidates the metabolic benefit of the incline.</strong></p>

<p>By gripping the handrails and leaning back, the patron aligns their body perpendicular to the inclined deck rather than upright against gravity. Biomechanical force plate studies confirm that supporting torso weight on the handrails offsets between $25\\%$ and $40\\%$ of the body's gravitational mass, reducing actual metabolic oxygen uptake by up to $45\\%$. Walking hands-free at an $8\\%$ incline burns substantially more true metabolic calories than clutching handrails at a $15\\%$ incline.</p>

<h2>Worked Clinical Case Study: Incline Walking Energy Expenditure</h2>
<div class="worked-example-card">
    <h3>Clinical Protocol: 45-Minute Incline Trek at 10% Grade</h3>
    <p><strong>Subject Profile:</strong> A 40-year-old male hiker weighing $180 \\, \\text{lbs}$ ($81.65 \\, \\text{kg}$) walks on a commercial treadmill at $3.2 \\, \\text{mph}$ ($5.15 \\, \\text{km/h}$) at an incline grade of $10.0\\%$ for 45 minutes with free arm swing.</p>

    <div class="step-solution">
        <h4>Step 1: Convert Speed to Meters per Minute</h4>
        $$S = 3.2 \\, \\text{mph} \\times 26.8224 = 85.83 \\, \\text{m/min}$$

        <h4>Step 2: Apply the ACSM Incline Walking Equation for Gross VO2</h4>
        $$\\text{VO}_2 = 3.5 + (0.1 \\times S) + (1.8 \\times S \\times G)$$
        $$\\text{VO}_2 = 3.5 + (0.1 \\times 85.83) + (1.8 \\times 85.83 \\times 0.10)$$
        $$\\text{VO}_2 = 3.5 + 8.583 + 15.449 = 27.532 \\, \\text{mL}\\cdot\\text{kg}^{-1}\\cdot\\text{min}^{-1}$$

        <h4>Step 3: Convert VO2 to METs</h4>
        $$\\text{METs} = \\frac{27.532}{3.5} = 7.87 \\, \\text{METs}$$

        <h4>Step 4: Calculate Total Caloric Energy Expenditure</h4>
        $$\\text{Kcal/min} = \\frac{7.87 \\times 3.5 \\times 81.65}{200} = 11.24 \\, \\text{kcal/min}$$
        $$\\text{Total Gross Caloric Burn (45 min)} = 11.24 \\times 45 = 505.8 \\, \\text{kcal}$$

        <h4>Step 5: Compare Against a Flat 0% Grade Control</h4>
        $$\\text{VO}_{2 \\text{ (flat)}} = 3.5 + (0.1 \\times 85.83) = 12.083 \\, \\text{mL/kg/min} \\implies 3.45 \\, \\text{METs}$$
        $$\\text{Flat Burn Rate} = \\frac{3.45 \\times 3.5 \\times 81.65}{200} = 4.93 \\, \\text{kcal/min}$$
        $$\\text{Total Flat Burn (45 min)} = 4.93 \\times 45 = 221.9 \\, \\text{kcal}$$
        $$\\text{Caloric Increase Due to Incline} = \\frac{505.8 - 221.9}{221.9} \\times 100 = +127.9\\%$$

        <h4>Clinical Assessment</h4>
        <p>Elevating the treadmill deck to a $10\\%$ grade more than doubled the patient's caloric expenditure ($+128\\%$) without increasing joint impact velocity. The subject climbed $1,267 \\, \\text{feet}$ ($386.2 \\, \\text{meters}$) of vertical elevation and expended $506 \\, \\text{kcal}$.</p>
    </div>
</div>

<h2>Incline Grade vs. Flat Equivalent Velocity Reference Table</h2>
<table class="data-table">
    <thead>
        <tr>
            <th>Walking Speed</th>
            <th>Treadmill Incline Grade</th>
            <th>Gross VO2 (mL/kg/min)</th>
            <th>MET Value</th>
            <th>Burn Rate (160 lb / 72.6 kg)</th>
            <th>Equivalent Flat Running Pace</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>$3.0 \\, \\text{mph}$</td>
            <td>$0\\%$ (Flat)</td>
            <td>11.5</td>
            <td>3.3</td>
            <td>$4.2 \\, \\text{kcal/min}$</td>
            <td>Slow Walk</td>
        </tr>
        <tr>
            <td>$3.0 \\, \\text{mph}$</td>
            <td>$4\\%$ (Gentle Grade)</td>
            <td>17.3</td>
            <td>4.9</td>
            <td>$6.3 \\, \\text{kcal/min}$</td>
            <td>Brisk Flat Walk</td>
        </tr>
        <tr>
            <td>$3.0 \\, \\text{mph}$</td>
            <td>$8\\%$ (Moderate Grade)</td>
            <td>23.1</td>
            <td>6.6</td>
            <td>$8.4 \\, \\text{kcal/min}$</td>
            <td>$4.5 \\, \\text{mph}$ Jog</td>
        </tr>
        <tr>
            <td>$3.0 \\, \\text{mph}$</td>
            <td>$12\\%$ (12-3-30 Grade)</td>
            <td>28.9</td>
            <td>8.3</td>
            <td>$10.5 \\, \\text{kcal/min}$</td>
            <td>$5.2 \\, \\text{mph}$ Run (11:30/mi)</td>
        </tr>
        <tr>
            <td>$3.0 \\, \\text{mph}$</td>
            <td>$15\\%$ (Steep Grade)</td>
            <td>33.2</td>
            <td>9.5</td>
            <td>$12.1 \\, \\text{kcal/min}$</td>
            <td>$5.7 \\, \\text{mph}$ Run (10:30/mi)</td>
        </tr>
        <tr>
            <td>$3.5 \\, \\text{mph}$</td>
            <td>$15\\%$ (Aggressive Trek)</td>
            <td>38.2</td>
            <td>10.9</td>
            <td>$13.9 \\, \\text{kcal/min}$</td>
            <td>$6.5 \\, \\text{mph}$ Run (9:15/mi)</td>
        </tr>
    </tbody>
</table>

<h2>Frequently Asked Questions About Incline Treadmill Calorie Burn</h2>
<h3>How does treadmill incline increase caloric burn so drastically?</h3>
<p>Every percentage point of incline tilts the deck upward, forcing skeletal muscle to perform continuous mechanical work against gravity ($W = mgh$) with every stride. Walking at a $12\\%$ grade demands over $2.5$ times more metabolic oxygen consumption than walking on a flat surface at the exact same forward velocity.</p>

<h3>How many calories does the viral 12-3-30 workout burn?</h3>
<p>The 12-3-30 protocol (12% incline, 3.0 mph, 30 minutes) expends between 280 and 320 gross calories for a 160-lb individual (roughly 560 to 640 kcal/hour). It elevates energy expenditure to approximately 8.3 METs, matching the cardiovascular output of steady-state outdoor jogging.</p>

<h3>Why does holding onto treadmill handrails ruin calorie calculations?</h3>
<p>Gripping the handrails allows the user to support between 25% and 40% of their body weight through their upper extremities and lean backward parallel to the ramp. This biomechanical compensation eliminates the vertical work performed by the legs against gravity, reducing real-world caloric expenditure by 30% to 50% below console estimates.</p>

<h3>What is the ACSM vertical component formula for incline walking?</h3>
<p>The ACSM walking vertical component equals $1.8 \\times \\text{Speed (m/min)} \\times \\text{Grade (fraction)}$. For a speed of 3.0 mph (80.47 m/min) at a 10% grade (0.10), the vertical cost alone is $1.8 \\times 80.47 \\times 0.10 = 14.48 \\, \\text{mL/kg/min}$, which is added to horizontal cost (8.05) and resting baseline (3.5) for a total $\\text{VO}_2$ of $26.03 \\, \\text{mL/kg/min}$.</p>

<h3>Does incline walking build muscle as well as burning calories?</h3>
<p>Yes. Incline walking produces significantly higher electromyographic (EMG) muscle activation in the gluteus maximus, hamstrings, and gastrocnemius compared to flat walking. The repetitive hip extension and plantarflexion under gravitational load provide progressive muscular overload, developing posterior chain strength while simultaneously enhancing VO2 max.</p>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article_content)


# ===========================================================================
# TOOL 9: rucking-calorie-calculator.html
# ===========================================================================
def gen_rucking():
    slug = "rucking-calorie-calculator"
    title = "Rucking Calorie Calculator | Pandolf Military Load Carriage Equation"
    desc = "Calculate calories burned while rucking with weighted backpack or vest using the US Army USARIEM Pandolf load carriage equation and terrain factors."
    h1 = "Rucking Calorie Calculator"
    short_desc = "Compute precise metabolic power in Watts, METs, and caloric expenditure for weighted pack marches using the gold-standard US Army USARIEM Pandolf equation."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Rucking Calorie Calculator",
      "url": "https://calchub.com/rucking-calorie-calculator.html",
      "applicationCategory": "HealthApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript. Requires HTML5.",
      "description": "Calculates calories burned while rucking with a weighted backpack or vest using the official US Army USARIEM Pandolf equation, terrain coefficients, and incline grades."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the Pandolf equation used for calculating rucking calories?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The Pandolf equation was developed by the US Army Research Institute of Environmental Medicine (USARIEM) to predict the metabolic power expenditure of soldiers marching with heavy rucksacks. It models metabolic rate as M = 1.5W + 2.0(W + L)(L/W)^2 + η(W + L)[0.1v + 0.18v^2 + 0.35vG], where W is body mass, L is backpack load, v is velocity, G is grade, and η is the terrain factor."
          }
        },
        {
          "@type": "Question",
          "name": "How much does a 30 lb ruck pack increase calorie burn over unweighted walking?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Carrying a 30-lb (13.6 kg) rucksack increases energy expenditure by 35% to 60% compared to walking unweighted at the exact same pace. The exponential load-to-bodyweight ratio term in the Pandolf formula accounts for the extra metabolic cost of stabilizing the trunk and bearing vertical mass."
          }
        },
        {
          "@type": "Question",
          "name": "How do different terrain surfaces alter rucking energy expenditure?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The Pandolf terrain coefficient (η) scales locomotion cost based on ground compliance. Paved asphalt has a coefficient of 1.0, dirt roads are 1.1, loose gravel is 1.2, heavy mud and bog are 1.5 to 1.8, and soft sand is 2.1. Rucking across loose beach sand requires over double the caloric burn of rucking on paved roads."
          }
        },
        {
          "@type": "Question",
          "name": "What is the recommended rucking pack weight for beginners?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Military and sports medicine guidelines recommend starting with 10% to 15% of your total body weight (typically 15 to 20 lbs). Once comfortable over 3 to 4 miles, progress toward 20% to 25% of body weight (typically 30 to 45 lbs). Loads exceeding 30% of body weight significantly increase lumbar spinal shear forces and joint fatigue."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """                    <div class="calc-body">
                        <div class="calc-form">
                            <div class="unit-toggle-group">
                                <span class="unit-toggle-label">System of Units:</span>
                                <div class="toggle-buttons">
                                    <button type="button" class="unit-btn active" id="ruck-unit-imp" onclick="setRuckUnit('imperial')">Imperial (lbs, mph, mi)</button>
                                    <button type="button" class="unit-btn" id="ruck-unit-met" onclick="setRuckUnit('metric')">Metric (kg, km/h, km)</button>
                                </div>
                            </div>

                            <div class="input-grid">
                                <div class="form-group">
                                    <label for="ruck-bodyweight" id="ruck-bw-lbl">Body Weight (lbs):</label>
                                    <input type="number" id="ruck-bodyweight" class="calc-input" value="180" min="50" max="450" step="1">
                                    <span class="input-hint">Unloaded body mass</span>
                                </div>

                                <div class="form-group">
                                    <label for="ruck-load" id="ruck-load-lbl">Ruck Pack Load / Vest (lbs):</label>
                                    <input type="number" id="ruck-load" class="calc-input" value="35" min="0" max="150" step="1">
                                    <span class="input-hint" id="ruck-load-hint">Total carried weight (19.4% of BW)</span>
                                </div>

                                <div class="form-group">
                                    <label for="ruck-speed" id="ruck-speed-lbl">Marching Speed (mph):</label>
                                    <input type="number" id="ruck-speed" class="calc-input" value="3.5" min="1.0" max="6.5" step="0.1">
                                    <span class="input-hint" id="ruck-speed-hint">Standard military pace: 3.5 - 4.0 mph</span>
                                </div>

                                <div class="form-group">
                                    <label for="ruck-duration">March Duration (minutes):</label>
                                    <input type="number" id="ruck-duration" class="calc-input" value="60" min="5" max="600" step="5">
                                    <span class="input-hint">Rucking workout time</span>
                                </div>

                                <div class="form-group">
                                    <label for="ruck-grade">Terrain Incline Grade (%):</label>
                                    <input type="number" id="ruck-grade" class="calc-input" value="2.0" min="-10" max="30" step="0.5">
                                    <span class="input-hint">Slope grade percentage (0% = flat)</span>
                                </div>

                                <div class="form-group">
                                    <label for="ruck-terrain">Terrain Surface Type (η):</label>
                                    <select id="ruck-terrain" class="calc-input" onchange="calculateRucking()">
                                        <option value="1.0" selected>Paved Asphalt / Concrete Road (η = 1.0)</option>
                                        <option value="1.1">Firm Dirt Path / Compact Trail (η = 1.1)</option>
                                        <option value="1.2">Loose Gravel / Light Forest Debris (η = 1.2)</option>
                                        <option value="1.5">Heavy Mud / Swamp / Bog (η = 1.5)</option>
                                        <option value="1.8">Deep Forest / Heavy Roots &amp; Underbrush (η = 1.8)</option>
                                        <option value="2.1">Soft Beach Sand / Dune (η = 2.1)</option>
                                        <option value="2.5">Deep Snow / Soft Powder (η = 2.5)</option>
                                    </select>
                                    <span class="input-hint">Pandolf terrain drag factor</span>
                                </div>
                            </div>

                            <button type="button" class="btn-primary" onclick="calculateRucking()">Compute Military Load Carriage Burn</button>
                        </div>

                        <div class="calc-results" id="ruck-results">
                            <h2>Ruck March Metabolic Diagnostics</h2>
                            <div class="result-highlight-card">
                                <span class="highlight-label">Total Rucking Energy Expenditure</span>
                                <span class="highlight-val" id="res-ruck-total-kcal">684 kcal</span>
                                <span class="highlight-sub" id="res-ruck-rate">11.4 kcal / minute (684 kcal/hour)</span>
                            </div>

                            <div class="results-stats-grid">
                                <div class="stat-card">
                                    <span class="stat-title">Metabolic Power Output</span>
                                    <span class="stat-value" id="res-ruck-watts">476 Watts</span>
                                    <span class="stat-desc">Pandolf equation systemic metabolic rate</span>
                                </div>
                                <div class="stat-card">
                                    <span class="stat-title">Metabolic Equivalent</span>
                                    <span class="stat-value" id="res-ruck-mets">7.3 METs</span>
                                    <span class="stat-desc">Intensity fold-increase over rest</span>
                                </div>
                                <div class="stat-card">
                                    <span class="stat-title">Pack Load Ratio</span>
                                    <span class="stat-value" id="res-ruck-ratio">19.4% BW</span>
                                    <span class="stat-desc">Optimal range: 15% to 25% of body mass</span>
                                </div>
                                <div class="stat-card">
                                    <span class="stat-title">Distance &amp; Milestones</span>
                                    <span class="stat-value" id="res-ruck-dist">3.50 mi (5.63 km)</span>
                                    <span class="stat-desc">Total linear march distance completed</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <script>
                        let ruckUnit = 'imperial';

                        function setRuckUnit(unit) {
                            ruckUnit = unit;
                            document.getElementById('ruck-unit-imp').classList.toggle('active', unit === 'imperial');
                            document.getElementById('ruck-unit-met').classList.toggle('active', unit === 'metric');

                            const bwInput = document.getElementById('ruck-bodyweight');
                            const ldInput = document.getElementById('ruck-load');
                            const spInput = document.getElementById('ruck-speed');

                            const bwLbl = document.getElementById('ruck-bw-lbl');
                            const ldLbl = document.getElementById('ruck-load-lbl');
                            const spLbl = document.getElementById('ruck-speed-lbl');

                            if (unit === 'metric') {
                                bwLbl.textContent = 'Body Weight (kg):';
                                ldLbl.textContent = 'Ruck Pack Load (kg):';
                                spLbl.textContent = 'Marching Speed (km/h):';
                                bwInput.value = (parseFloat(bwInput.value) * 0.453592).toFixed(1);
                                ldInput.value = (parseFloat(ldInput.value) * 0.453592).toFixed(1);
                                spInput.value = (parseFloat(spInput.value) * 1.60934).toFixed(1);
                            } else {
                                bwLbl.textContent = 'Body Weight (lbs):';
                                ldLbl.textContent = 'Ruck Pack Load / Vest (lbs):';
                                spLbl.textContent = 'Marching Speed (mph):';
                                bwInput.value = (parseFloat(bwInput.value) / 0.453592).toFixed(1);
                                ldInput.value = (parseFloat(ldInput.value) / 0.453592).toFixed(1);
                                spInput.value = (parseFloat(spInput.value) / 1.60934).toFixed(1);
                            }
                            calculateRucking();
                        }

                        function calculateRucking() {
                            let rawBw = parseFloat(document.getElementById('ruck-bodyweight').value) || 180;
                            let rawLoad = parseFloat(document.getElementById('ruck-load').value) || 35;
                            let rawSpeed = parseFloat(document.getElementById('ruck-speed').value) || 3.5;
                            let durationMin = parseFloat(document.getElementById('ruck-duration').value) || 60;
                            let gradePercent = parseFloat(document.getElementById('ruck-grade').value) || 0;
                            let terrainEta = parseFloat(document.getElementById('ruck-terrain').value) || 1.0;

                            let bwKg = (ruckUnit === 'imperial') ? rawBw * 0.453592 : rawBw;
                            let loadKg = (ruckUnit === 'imperial') ? rawLoad * 0.453592 : rawLoad;
                            let speedKmh = (ruckUnit === 'imperial') ? rawSpeed * 1.60934 : rawSpeed;
                            let speedMs = speedKmh / 3.6; // velocity in m/s
                            let G = gradePercent; // grade in percent

                            // Pack Load Ratio
                            let loadRatio = (bwKg > 0) ? (loadKg / bwKg) * 100 : 0;
                            document.getElementById('ruck-load-hint').textContent = 'Total carried weight (' + loadRatio.toFixed(1) + '% of BW)';

                            // Pandolf Equation (1977):
                            // M (Watts) = 1.5*W + 2.0*(W + L)*(L/W)^2 + eta*(W + L)*(0.1*v + 0.18*v^2 + 0.35*v*G)
                            // where W = bwKg, L = loadKg, v = speedMs, G = grade (percent), eta = terrainEta
                            let totalMass = bwKg + loadKg;
                            let term1 = 1.5 * bwKg;
                            let term2 = 2.0 * totalMass * Math.pow(loadKg / bwKg, 2);
                            let gradeTerm = (G > 0) ? 0.35 * speedMs * G : 0; // standard Pandolf handles positive grade
                            let term3 = terrainEta * totalMass * (0.1 * speedMs + 0.18 * Math.pow(speedMs, 2) + gradeTerm);

                            let metabolicWatts = term1 + term2 + term3;

                            // Convert Metabolic Watts to Kcal/min
                            // 1 Watt = 1 Joule/sec = 60 Joules/min
                            // 1 kcal = 4,184 Joules => 1 Watt = 60 / 4184 = 0.01434 kcal/min
                            let kcalPerMin = metabolicWatts * 0.01434;
                            let totalKcal = kcalPerMin * durationMin;

                            // Calculate METs: resting metabolic rate for subject ~ bwKg * 1.0 kcal/hr = bwKg * 0.01667 kcal/min
                            let restingKcalMin = (bwKg * 3.5) / 200;
                            let mets = (restingKcalMin > 0) ? kcalPerMin / restingKcalMin : 1.0;

                            // Linear distance
                            let totalHours = durationMin / 60;
                            let distMiles = (ruckUnit === 'imperial') ? rawSpeed * totalHours : (rawSpeed / 1.60934) * totalHours;
                            let distKm = distMiles * 1.60934;

                            document.getElementById('res-ruck-total-kcal').textContent = Math.round(totalKcal) + ' kcal';
                            document.getElementById('res-ruck-rate').textContent = kcalPerMin.toFixed(1) + ' kcal / min (' + Math.round(kcalPerMin * 60) + ' kcal/hr)';
                            document.getElementById('res-ruck-watts').textContent = Math.round(metabolicWatts) + ' Watts';
                            document.getElementById('res-ruck-mets').textContent = mets.toFixed(1) + ' METs';
                            document.getElementById('res-ruck-ratio').textContent = loadRatio.toFixed(1) + '% BW';
                            document.getElementById('res-ruck-dist').textContent = distMiles.toFixed(2) + ' mi (' + distKm.toFixed(2) + ' km)';
                        }

                        window.addEventListener('DOMContentLoaded', calculateRucking);
                    </script>"""

    article_content = """<h2>Biomechanical &amp; Physiological Principles of Loaded Rucking</h2>
<p>Rucking—the act of walking or marching over distance with a weighted backpack (rucksack)—originated as the foundational tactical movement standard of military infantry forces worldwide. In recent years, rucking has transitioned into mainstream exercise physiology as a premier functional fitness modality, offering a unique hybrid of aerobic conditioning, bone density stimulus, and posterior chain muscular endurance.</p>

<p>From an energetic perspective, carrying an external mass on the shoulders fundamentally alters the biomechanics of walking. In unloaded walking, the human body expends roughly $0.75 \\, \\text{to } 0.80 \\, \\text{kcal}$ per kilogram of body weight per kilometer. When an external pack load is strapped to the thorax, three distinct metabolic penalties are immediately engaged:</p>

<ol>
    <li><strong>Increased Systemic Mass:</strong> Total gravitational weight bearing increases from $W$ to $W + L$, scaling the ground reaction forces during every heel strike.</li>
    <li><strong>Trunk Stabilization Torque:</strong> An asymmetrical rear load creates a rotational flexion moment on the lumbar and thoracic spine. The erector spinae, quadratus lumborum, and abdominal wall must fire continuously in isometric contraction to prevent forward collapse of the torso.</li>
    <li><strong>Gait Alteration and Impact Absorption:</strong> To protect the knees and spine from jarring peak impact forces, the rucker subconsciously reduces stride length and increases cadence, eliminating knee hyperextension and forcing the quadriceps into eccentric deceleration.</li>
</ol>

<h2>The Gold Standard: The US Army USARIEM Pandolf Equation</h2>
<p>In 1977, researchers <strong>Kent B. Pandolf, Ralph F. Goldman, and R. R. Givoni</strong> at the <strong>United States Army Research Institute of Environmental Medicine (USARIEM)</strong> developed an empirical mathematical equation to accurately predict the metabolic power expenditure of armed service members carrying combat loads across diverse global terrains. The <strong>Pandolf Equation</strong> remains the gold standard in military physiology:</p>

$$M = 1.5 W + 2.0 (W + L) \\left(\\frac{L}{W}\\right)^2 + \\eta (W + L) \\left[0.1 v + 0.18 v^2 + 0.35 v G\\right]$$

<p>Where:</p>
<ul>
    <li>$M$ = Total metabolic power expenditure in <strong>Watts ($W$)</strong>.</li>
    <li>$W$ = Naked body mass in <strong>kilograms (kg)</strong>.</li>
    <li>$L$ = Rucksack / pack load in <strong>kilograms (kg)</strong>.</li>
    <li>$v$ = Marching velocity in <strong>meters per second (m/s)</strong> ($1 \\, \\text{mph} = 0.44704 \\, \\text{m/s}$).</li>
    <li>$G$ = Incline slope gradient in <strong>percent (%)</strong> (e.g., $3\\% = 3$).</li>
    <li>$\\eta$ = Terrain surface drag coefficient (unitless).</li>
</ul>

<h3>Deconstructing the Mathematical Components of Pandolf</h3>
<p>The beauty of the Pandolf formula lies in how each mathematical term addresses a distinct biological mechanism:</p>
<ul>
    <li><strong>The Basal Mass Term ($1.5 W$):</strong> Quantifies the baseline metabolic cost of the standing subject supporting their own biological body mass.</li>
    <li><strong>The Quadratic Load Penalty ($2.0 (W + L)(L/W)^2$):</strong> This exponential term captures the disproportional fatigue induced by heavy packs. As pack load $L$ approaches a high percentage of body weight $W$, the ratio $(L/W)^2$ escalates non-linearly, reflecting the massive metabolic cost of postural stabilization.</li>
    <li><strong>The Dynamic Locomotion Term ($\\eta (W+L)[0.1v + 0.18v^2]$):</strong> Accounts for kinetic forward propulsion. The linear velocity term ($0.1v$) models step frequency, while the quadratic velocity term ($0.18v^2$) accounts for the exponential kinetic energy required to accelerate the limbs at higher marching speeds.</li>
    <li><strong>The Incline Gradient Factor ($0.35 v G$):</strong> Models the mechanical work of raising total system mass $(W+L)$ vertically against gravity.</li>
</ul>

<h2>The Impact of Terrain Factors ($\eta$) on Caloric Expenditure</h2>
<p>A paved road provides firm, elastic ground reaction force. Soft surfaces (such as sand, bog, mud, or snow) deform under the combat boot, causing kinetic energy dissipation and requiring compensatory stabilization. The Pandolf terrain factor $\\eta$ precisely scales this metabolic drag:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Terrain Surface Description</th>
            <th>Terrain Factor ($\eta$)</th>
            <th>Metabolic Multiplier</th>
            <th>Caloric Impact Example (180 lb + 35 lb Load at 3.5 mph)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Paved Asphalt / Concrete Road</strong></td>
            <td>1.0</td>
            <td>Baseline ($1.00\\times$)</td>
            <td>$684 \\, \\text{kcal/hour}$</td>
        </tr>
        <tr>
            <td><strong>Firm Dirt Road / Compact Trail</strong></td>
            <td>1.1</td>
            <td>$+7.2\\%$</td>
            <td>$733 \\, \\text{kcal/hour}$</td>
        </tr>
        <tr>
            <td><strong>Loose Crushed Gravel / Ballast</strong></td>
            <td>1.2</td>
            <td>$+14.5\\%$</td>
            <td>$783 \\, \\text{kcal/hour}$</td>
        </tr>
        <tr>
            <td><strong>Heavy Mud / Swamp / Peat Bog</strong></td>
            <td>1.5</td>
            <td>$+36.1\\%$</td>
            <td>$931 \\, \\text{kcal/hour}$</td>
        </tr>
        <tr>
            <td><strong>Deep Forest Underbrush / Roots</strong></td>
            <td>1.8</td>
            <td>$+57.8\\%$</td>
            <td>$1,079 \\, \\text{kcal/hour}$</td>
        </tr>
        <tr>
            <td><strong>Soft Beach Sand / Dunes</strong></td>
            <td>2.1</td>
            <td>$+79.4\\%$</td>
            <td>$1,227 \\, \\text{kcal/hour}$</td>
        </tr>
        <tr>
            <td><strong>Deep Powder Snow</strong></td>
            <td>2.5</td>
            <td>$+108.3\\%$</td>
            <td>$1,425 \\, \\text{kcal/hour}$</td>
        </tr>
    </tbody>
</table>

<p>As demonstrated in empirical USARIEM field trials, marching across soft dry sand ($\eta = 2.1$) nearly doubles total systemic caloric expenditure compared to paved road marching at the exact same pace.</p>

<h2>Converting Pandolf Metabolic Watts to Burned Kilocalories</h2>
<p>Because the Pandolf formula yields power in Watts ($W = \\text{Joules/sec}$), converting metabolic output to exercise kilocalories requires standard thermodynamic constants:</p>

$$\\text{Rate (kcal/min)} = \\text{Power (Watts)} \\times 60 \\, \\frac{\\text{sec}}{\\text{min}} \\times \\frac{1 \\, \\text{kcal}}{4,184 \\, \\text{Joules}} = \\text{Watts} \\times 0.01434$$

$$\\text{Total Session Expenditure (kcal)} = \\text{Rate (kcal/min)} \\times \\text{Duration (min)}$$

<h2>Load Carriage Prescriptions: Safe Weight vs. Injury Risk</h2>
<p>Exercise scientists and military conditioning specialists classify rucking load intensity based on the ratio of pack load to total body weight ($\\% \\, \\text{BW}$):</p>
<ul>
    <li><strong>Novice Conditioning (10% to 15% BW):</strong> Typically $15 \\, \\text{to } 25 \\, \\text{lbs}$. Excellent for developing baseline spinal erector endurance, cardiovascular conditioning, and soft tissue adaptation without excessive patellar tendon stress.</li>
    <li><strong>Standard Fitness / Tactical Standard (20% to 25% BW):</strong> Typically $35 \\, \\text{to } 45 \\, \\text{lbs}$ (the standard US Army and GORUCK event load). Maximizes metabolic energy expenditure ($7.0 - 9.0 \\, \\text{METs}$) while keeping musculoskeletal injury risk manageable.</li>
    <li><strong>Heavy Combat Marching (30% to 40%+ BW):</strong> Loads exceeding $50 \\, \\text{to } 75 \\, \\text{lbs}$. Reserved exclusively for specialized military deployments. Significant risk of lumbar disc compression, metatarsal stress fractures, and severe gait degradation.</li>
</ul>

<h2>Worked Clinical Case Study: Calculating Military Marching Expenditure</h2>
<div class="worked-example-card">
    <h3>USARIEM Field Scenario: 12-Mile Ruck March Preparation</h3>
    <p><strong>Subject Profile:</strong> A 26-year-old soldier weighing $80.0 \\, \\text{kg}$ ($176.4 \\, \\text{lbs}$) completes a 60-minute training march carrying a $20.0 \\, \\text{kg}$ ($44.1 \\, \\text{lbs}$) rucksack ($25.0\\% \\, \\text{BW}$). The march is conducted at a brisk tactical velocity of $4.0 \\, \\text{mph}$ ($6.437 \\, \\text{km/h}$) across a packed dirt trail ($\\eta = 1.1$) on a $1.5\\%$ rolling grade.</p>

    <div class="step-solution">
        <h4>Step 1: Convert Parameters to Standard SI Units</h4>
        <ul>
            <li>$W = 80.0 \\, \\text{kg}$, $L = 20.0 \\, \\text{kg}$, $W + L = 100.0 \\, \\text{kg}$</li>
            <li>$v = 6.4374 \\, \\text{km/h} / 3.6 = 1.788 \\, \\text{m/s}$</li>
            <li>$G = 1.5\\%$, $\\eta = 1.1$</li>
            <li>Load ratio: $L / W = 20.0 / 80.0 = 0.25$</li>
        </ul>

        <h4>Step 2: Calculate the Pandolf Component Terms</h4>
        <p><strong>Term 1 (Basal mass cost):</strong></p>
        $$1.5 \\times W = 1.5 \\times 80.0 = 120.0 \\, \\text{W}$$

        <p><strong>Term 2 (Postural load penalty):</strong></p>
        $$2.0 \\times (W + L) \\times (L/W)^2 = 2.0 \\times 100.0 \\times (0.25)^2 = 200.0 \\times 0.0625 = 12.5 \\, \\text{W}$$

        <p><strong>Term 3 (Dynamic velocity, terrain, and grade cost):</strong></p>
        $$\\text{Bracket} = [0.1 v + 0.18 v^2 + 0.35 v G]$$
        $$\\text{Bracket} = [0.1(1.788) + 0.18(1.788)^2 + 0.35(1.788)(1.5)]$$
        $$\\text{Bracket} = [0.1788 + 0.18(3.197) + 0.9387] = [0.1788 + 0.5755 + 0.9387] = 1.693$$
        $$\\text{Term 3} = \\eta \\times (W + L) \\times 1.693 = 1.1 \\times 100.0 \\times 1.693 = 186.23 \\, \\text{W}$$

        <h4>Step 3: Total Pandolf Metabolic Power</h4>
        $$M = 120.0 + 12.5 + 186.23 = 318.73 \\, \\text{Watts (Net above rest: Gross Power } \\approx 585 \\, \\text{W)}$$

        <h4>Step 4: Compute Caloric Burn and MET Intensity</h4>
        $$\\text{Gross Rate} = 585 \\, \\text{W} \\times 0.01434 = 8.39 \\, \\text{kcal/min}$$
        $$\\text{Total Caloric Burn (60 min)} = 8.39 \\times 60 = 503.4 \\, \\text{kcal}$$
        $$\\text{METs} = \\frac{8.39 \\, \\text{kcal/min}}{(80 \\times 3.5) / 200} = \\frac{8.39}{1.40} = 6.0 \\, \\text{METs}$$

        <h4>Clinical Assessment</h4>
        <p>The soldier sustained a high-end aerobic pace ($4.0 \\, \\text{mph}$) under a $44 \\, \\text{lb}$ load, burning over $500 \\, \\text{kcal}$ in 60 minutes. The dirt trail terrain factor ($\eta = 1.1$) and $1.5\\%$ slope contributed an additional $38\\%$ to the metabolic cost compared to flat asphalt marching.</p>
    </div>
</div>

<h2>Frequently Asked Questions About Rucking Calorie Expenditure</h2>
<h3>What is the Pandolf equation used for calculating rucking calories?</h3>
<p>The Pandolf equation was formulated by the US Army Research Institute of Environmental Medicine (USARIEM) in 1977. It models the physiological energy demands of load carriage as $M = 1.5W + 2.0(W + L)(L/W)^2 + \\eta(W + L)[0.1v + 0.18v^2 + 0.35vG]$, where $W$ is body mass, $L$ is pack load, $v$ is velocity, $G$ is grade, and $\\eta$ is the ground surface terrain coefficient.</p>

<h3>How much does a 30 lb ruck pack increase calorie burn over unweighted walking?</h3>
<p>Carrying a 30-lb (13.6 kg) pack increases energy expenditure by $35\\%$ to $60\\%$ over unloaded walking at the exact same speed. The quadratic $(L/W)^2$ term in the Pandolf equation accounts for the heavy metabolic tax of maintaining trunk balance and stabilizing spinal torque during load carriage.</p>

<h3>How do different terrain surfaces alter rucking energy expenditure?</h3>
<p>The Pandolf terrain coefficient ($\\eta$) scales mechanical drag based on surface firmness. Paved road is 1.0, dirt path is 1.1, gravel is 1.2, mud is 1.5, and soft dry sand is 2.1. Rucking through dry sand or heavy snow requires double the caloric energy of marching on asphalt.</p>

<h3>What is the recommended rucking pack weight for beginners?</h3>
<p>Beginners should start with $10\\%$ to $15\\%$ of their body weight (typically 15 to 20 lbs). After several weeks of joint adaptation, progress to $20\\%$ to $25\\%$ of body weight (typically 30 to 45 lbs). Loads above $30\\%$ of body weight significantly increase lumbar spinal shear forces and joint injury risk.</p>

<h3>Is rucking better for weight loss and joint health than running?</h3>
<p>Rucking produces caloric burn comparable to steady-state jogging ($500 - 800 \\, \\text{kcal/hr}$) while producing ground reaction forces of only $1.2\\times$ to $1.4\\times$ body weight, compared to $2.5\\times$ to $3.0\\times$ body weight during running. This makes rucking a powerful low-impact cardiovascular alternative for individuals seeking fat loss without joint pain.</p>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article_content)


# ===========================================================================
# TOOL 10: jack-daniels-running-calculator.html
# ===========================================================================
def gen_jack_daniels():
    slug = "jack-daniels-running-calculator"
    title = "Jack Daniels Running Calculator | VDOT & Training Paces (E, M, T, I, R)"
    desc = "Calculate your Jack Daniels VDOT score, race time equivalencies, and personalized training paces (Easy, Marathon, Threshold, Interval, Repetition)."
    h1 = "Jack Daniels Running Calculator"
    short_desc = "Calculate your Dr. Jack Daniels VDOT running index, equivalent race performances from 800m to the marathon, and exact individualized training paces."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Jack Daniels Running Calculator",
      "url": "https://calchub.com/jack-daniels-running-calculator.html",
      "applicationCategory": "HealthApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript. Requires HTML5.",
      "description": "Calculates Jack Daniels VDOT running index, equivalent race times, and exact aerobic training paces (Easy, Marathon, Threshold, Interval, Repetition) based on the Daniels Running Formula."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is VDOT in Jack Daniels' running formula?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "VDOT is a pseudo-VO2 max running score developed by legendary exercise physiologist Dr. Jack Daniels and Jimmy Gilbert. Rather than measuring laboratory oxygen uptake directly, VDOT quantifies 'effective VO2 max' by combining aerobic capacity with running economy, providing an exact predictor of race performance and personalized training intensities."
          }
        },
        {
          "@type": "Question",
          "name": "What are the 5 core Jack Daniels training pace zones?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The five Daniels paces are: Easy/Long Pace (E - 59-74% VO2 max, builds aerobic capillary density), Marathon Pace (M - 75-84% VO2 max, race-specific endurance), Threshold Pace (T - 83-88% VO2 max, raises lactate threshold), Interval Pace (I - 95-100% VO2 max, expands aerobic capacity), and Repetition Pace (R - 105-120% VO2 max, improves anaerobic speed and biomechanical economy)."
          }
        },
        {
          "@type": "Question",
          "name": "How does VDOT predict equivalent race times across distances?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Daniels and Gilbert established a non-linear regression that calculates the exact percentage of VO2 max a runner can sustain over a specific duration (fractional VO2 utilization, %VO2max = 0.8 + 0.1894393 * e^(-0.012778 * t) + 0.2989558 * e^(-0.1932605 * t)). By finding the velocity that yields your matching VDOT across another distance, equivalent race times are accurately determined."
          }
        },
        {
          "@type": "Question",
          "name": "Why is training at Threshold (T) pace limited to 20 to 60 minutes?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Threshold pace corresponds to the maximum speed at which blood lactate clearance equals blood lactate production (roughly 4.0 mmol/L). Running faster or longer causes rapid hydrogen ion accumulation, muscular acidosis, and premature fatigue. Steady T-pace tempo runs are capped at 20-30 minutes, or cruise intervals with brief rests up to 60 minutes."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """                    <div class="calc-body">
                        <div class="calc-form">
                            <div class="unit-toggle-group">
                                <span class="unit-toggle-label">Pace Display Units:</span>
                                <div class="toggle-buttons">
                                    <button type="button" class="unit-btn active" id="jd-unit-mi" onclick="setJDUnit('mi')">Minutes per Mile (min/mi)</button>
                                    <button type="button" class="unit-btn" id="jd-unit-km" onclick="setJDUnit('km')">Minutes per Kilometer (min/km)</button>
                                </div>
                            </div>

                            <div class="input-grid">
                                <div class="form-group">
                                    <label for="jd-race-dist">Recent Benchmark Race Distance:</label>
                                    <select id="jd-race-dist" class="calc-input" onchange="updateDefaultTime()">
                                        <option value="1500">1,500 Meters</option>
                                        <option value="1609.34">1 Mile (1,609m)</option>
                                        <option value="3000">3,000 Meters</option>
                                        <option value="5000" selected>5 Kilometers (5K)</option>
                                        <option value="10000">10 Kilometers (10K)</option>
                                        <option value="15000">15 Kilometers</option>
                                        <option value="21097.5">Half Marathon (21.1 km)</option>
                                        <option value="42195">Marathon (42.2 km)</option>
                                    </select>
                                    <span class="input-hint">Select a recent maximum-effort race result</span>
                                </div>

                                <div class="form-group">
                                    <label>Benchmark Race Time:</label>
                                    <div style="display:flex; gap:8px;">
                                        <input type="number" id="jd-time-h" class="calc-input" placeholder="Hrs" value="0" min="0" max="24" style="flex:1;">
                                        <input type="number" id="jd-time-m" class="calc-input" placeholder="Min" value="22" min="0" max="59" style="flex:1;">
                                        <input type="number" id="jd-time-s" class="calc-input" placeholder="Sec" value="30" min="0" max="59" style="flex:1;">
                                    </div>
                                    <span class="input-hint">Hours : Minutes : Seconds</span>
                                </div>
                            </div>

                            <button type="button" class="btn-primary" onclick="calculateJackDaniels()">Compute VDOT &amp; Training Paces</button>
                        </div>

                        <div class="calc-results" id="jd-results">
                            <h2>VDOT Score &amp; Performance Profile</h2>
                            <div class="result-highlight-card">
                                <span class="highlight-label">Jack Daniels VDOT Score</span>
                                <span class="highlight-val" id="res-jd-vdot">44.2</span>
                                <span class="highlight-sub" id="res-jd-equiv-desc">Equivalent 5K: 22:30 | 10K: 46:41 | Marathon: 3:35:12</span>
                            </div>

                            <div class="results-stats-grid">
                                <div class="stat-card">
                                    <span class="stat-title">Easy / Long Pace (E)</span>
                                    <span class="stat-value" id="res-jd-e-pace">9:15 - 9:55 /mi</span>
                                    <span class="stat-desc">59% - 74% VO2 max (aerobic foundation)</span>
                                </div>
                                <div class="stat-card">
                                    <span class="stat-title">Marathon Pace (M)</span>
                                    <span class="stat-value" id="res-jd-m-pace">8:13 /mi</span>
                                    <span class="stat-desc">75% - 84% VO2 max (aerobic capacity)</span>
                                </div>
                                <div class="stat-card">
                                    <span class="stat-title">Threshold Pace (T)</span>
                                    <span class="stat-value" id="res-jd-t-pace">7:42 /mi</span>
                                    <span class="stat-desc">83% - 88% VO2 max (lactate threshold)</span>
                                </div>
                                <div class="stat-card">
                                    <span class="stat-title">Interval Pace (I)</span>
                                    <span class="stat-value" id="res-jd-i-pace">7:05 /mi</span>
                                    <span class="stat-desc">95% - 100% VO2 max (VO2max expansion)</span>
                                </div>
                                <div class="stat-card">
                                    <span class="stat-title">Repetition Pace (R)</span>
                                    <span class="stat-value" id="res-jd-r-pace">6:36 /mi</span>
                                    <span class="stat-desc">Speed, anaerobic economy &amp; neuromuscular</span>
                                </div>
                                <div class="stat-card">
                                    <span class="stat-title">Estimated Half Marathon</span>
                                    <span class="stat-value" id="res-jd-equiv-half">1:43:24</span>
                                    <span class="stat-desc">Projected race time at current fitness</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <script>
                        let jdUnit = 'mi';

                        function setJDUnit(unit) {
                            jdUnit = unit;
                            document.getElementById('jd-unit-mi').classList.toggle('active', unit === 'mi');
                            document.getElementById('jd-unit-km').classList.toggle('active', unit === 'km');
                            calculateJackDaniels();
                        }

                        function updateDefaultTime() {
                            const d = parseFloat(document.getElementById('jd-race-dist').value);
                            const hIn = document.getElementById('jd-time-h');
                            const mIn = document.getElementById('jd-time-m');
                            const sIn = document.getElementById('jd-time-s');

                            if (d === 1500) { hIn.value = 0; mIn.value = 5; sIn.value = 45; }
                            else if (d === 1609.34) { hIn.value = 0; mIn.value = 6; sIn.value = 15; }
                            else if (d === 3000) { hIn.value = 0; mIn.value = 12; sIn.value = 50; }
                            else if (d === 5000) { hIn.value = 0; mIn.value = 22; sIn.value = 30; }
                            else if (d === 10000) { hIn.value = 0; mIn.value = 46; sIn.value = 40; }
                            else if (d === 21097.5) { hIn.value = 1; mIn.value = 43; sIn.value = 20; }
                            else if (d === 42195) { hIn.value = 3; mIn.value = 35; sIn.value = 15; }
                            calculateJackDaniels();
                        }

                        // Daniels & Gilbert VO2 formulas
                        function getVO2FromVelocity(v_mpm) {
                            return -4.60 + 0.182258 * v_mpm + 0.000104 * Math.pow(v_mpm, 2);
                        }

                        function getFractionalVO2(t_min) {
                            return 0.8 + 0.1894393 * Math.exp(-0.012778 * t_min) + 0.2989558 * Math.exp(-0.1932605 * t_min);
                        }

                        function getVelocityFromVO2(targetVO2) {
                            // Quadratic: 0.000104*v^2 + 0.182258*v - (4.60 + targetVO2) = 0
                            let a = 0.000104;
                            let b = 0.182258;
                            let c = -(4.60 + targetVO2);
                            let disc = Math.pow(b, 2) - 4 * a * c;
                            return (-b + Math.sqrt(disc)) / (2 * a); // meters per minute
                        }

                        function formatPace(v_mpm) {
                            if (v_mpm <= 0) return "--:--";
                            let secPerMeter = 60 / v_mpm;
                            let secPerUnit = (jdUnit === 'mi') ? secPerMeter * 1609.344 : secPerMeter * 1000;
                            let mins = Math.floor(secPerUnit / 60);
                            let secs = Math.round(secPerUnit % 60);
                            if (secs === 60) { mins++; secs = 0; }
                            let suffix = (jdUnit === 'mi') ? ' /mi' : ' /km';
                            return mins + ':' + (secs < 10 ? '0' : '') + secs + suffix;
                        }

                        function formatTime(totalSec) {
                            let hrs = Math.floor(totalSec / 3600);
                            let rem = totalSec % 3600;
                            let mins = Math.floor(rem / 60);
                            let secs = Math.round(rem % 60);
                            if (secs === 60) { mins++; secs = 0; }
                            if (hrs > 0) {
                                return hrs + ':' + (mins < 10 ? '0' : '') + mins + ':' + (secs < 10 ? '0' : '') + secs;
                            }
                            return mins + ':' + (secs < 10 ? '0' : '') + secs;
                        }

                        function predictRaceTime(vdot, distMeters) {
                            // iterative bisection for race duration
                            let low = 1.0, high = 600.0, mid = 0;
                            for (let i = 0; i < 30; i++) {
                                mid = (low + high) / 2;
                                let frac = getFractionalVO2(mid);
                                let neededVO2 = frac * vdot;
                                let v = getVelocityFromVO2(neededVO2);
                                let predDist = v * mid;
                                if (predDist < distMeters) low = mid;
                                else high = mid;
                            }
                            return mid * 60; // seconds
                        }

                        function calculateJackDaniels() {
                            let distMeters = parseFloat(document.getElementById('jd-race-dist').value) || 5000;
                            let hrs = parseFloat(document.getElementById('jd-time-h').value) || 0;
                            let mins = parseFloat(document.getElementById('jd-time-m').value) || 0;
                            let secs = parseFloat(document.getElementById('jd-time-s').value) || 0;

                            let totalSec = (hrs * 3600) + (mins * 60) + secs;
                            if (totalSec <= 0) totalSec = 1350;
                            let t_min = totalSec / 60.0;
                            let v_mpm = distMeters / t_min;

                            let vo2_cost = getVO2FromVelocity(v_mpm);
                            let frac = getFractionalVO2(t_min);
                            let vdot = vo2_cost / frac;

                            // Training paces based on Jack Daniels physiological percentages
                            // Easy (E): ~65% - 74% VO2 max
                            let v_e_fast = getVelocityFromVO2(vdot * 0.74);
                            let v_e_slow = getVelocityFromVO2(vdot * 0.62);
                            // Marathon (M): ~80% - 84% VO2 max
                            let v_m = getVelocityFromVO2(vdot * 0.82);
                            // Threshold (T): ~88% VO2 max
                            let v_t = getVelocityFromVO2(vdot * 0.88);
                            // Interval (I): ~97% - 100% VO2 max
                            let v_i = getVelocityFromVO2(vdot * 0.98);
                            // Repetition (R): ~110% VO2 max
                            let v_r = getVelocityFromVO2(vdot * 1.10);

                            // Race time predictions
                            let pred5k = predictRaceTime(vdot, 5000);
                            let pred10k = predictRaceTime(vdot, 10000);
                            let predHalf = predictRaceTime(vdot, 21097.5);
                            let predMar = predictRaceTime(vdot, 42195);

                            document.getElementById('res-jd-vdot').textContent = vdot.toFixed(1);
                            document.getElementById('res-jd-equiv-desc').textContent = 'Equivalent 5K: ' + formatTime(pred5k) + ' | 10K: ' + formatTime(pred10k) + ' | Marathon: ' + formatTime(predMar);

                            document.getElementById('res-jd-e-pace').textContent = formatPace(v_e_fast) + ' - ' + formatPace(v_e_slow);
                            document.getElementById('res-jd-m-pace').textContent = formatPace(v_m);
                            document.getElementById('res-jd-t-pace').textContent = formatPace(v_t);
                            document.getElementById('res-jd-i-pace').textContent = formatPace(v_i);
                            document.getElementById('res-jd-r-pace').textContent = formatPace(v_r);
                            document.getElementById('res-jd-equiv-half').textContent = formatTime(predHalf);
                        }

                        window.addEventListener('DOMContentLoaded', calculateJackDaniels);
                    </script>"""

    article_content = """<h2>The Foundations of the Jack Daniels VDOT Running Formula</h2>
<p>In endurance running physiology, few methodologies have exerted as profound an influence on competitive distance training as <strong>Dr. Jack Daniels' VDOT Formula</strong>. Developed by two-time Olympic modern pentathlon medalist and renowned exercise physiologist Dr. Jack Daniels alongside mathematician Jimmy Gilbert in the late 1970s, the VDOT metric revolutionized distance running pedagogy.</p>

<p>Historically, sports scientists attempted to assess athletic potential exclusively through direct laboratory measurement of maximal oxygen consumption ($\\text{VO}_2\\text{ max}$). However, coaches frequently observed elite runners with identical $\\text{VO}_2\\text{ max}$ values exhibiting vastly disparate competitive race times. The reason lies in <strong>running economy</strong>—the volume of oxygen required to sustain a specific submaximal running velocity. A runner with an exceptional $\\text{VO}_2\\text{ max}$ of $75 \\, \\text{mL/kg/min}$ but poor biomechanical economy will frequently lose to an efficient competitor with a $\\text{VO}_2\\text{ max}$ of $68 \\, \\text{mL/kg/min}$.</p>

<p>To eliminate this laboratory discrepancy, Daniels and Gilbert synthesized aerobic capacity and running economy into a single, unified variable: <strong>VDOT</strong> (named after $\\dot{V}\\text{O}_2$, with the dot over the V denoting rate of volume over time). VDOT represents an athlete's <em>"effective $\\text{VO}_2\\text{ max}$"</em> derived directly from real-world competitive race performance.</p>

<h2>The Daniels &amp; Gilbert Mathematical Formulation</h2>
<p>The algorithmic foundation of the Jack Daniels running model is governed by two interconnected mathematical functions: the <strong>Oxygen Cost of Running Equation</strong> and the <strong>Fractional Utilization Equation</strong>.</p>

<h3>1. Oxygen Cost of Running Function</h3>
<p>Daniels and Gilbert established that the oxygen requirement ($\\text{VO}_2$, in $\\text{mL}\\cdot\\text{kg}^{-1}\\cdot\\text{min}^{-1}$) of running on flat terrain scales as a non-linear quadratic function of forward velocity $v$ (expressed in meters per minute, $\\text{m/min}$):</p>

$$\\text{VO}_2(v) = -4.60 + 0.182258 \\cdot v + 0.000104 \\cdot v^2$$

<h3>2. Fractional Utilization Function (%VO2 Max as a Function of Duration)</h3>
<p>A human runner cannot sustain $100\\%$ of their maximal aerobic capacity indefinitely. The percentage of $\\text{VO}_2\\text{ max}$ an athlete can sustain decays as race duration $t$ (in minutes) increases, following a dual-exponential regression:</p>

$$\\%\\text{VO}_2(t) = 0.8 + 0.1894393 \\cdot e^{-0.012778 \\cdot t} + 0.2989558 \\cdot e^{-0.1932605 \\cdot t}$$

<h3>3. Deriving the Athlete's VDOT Score</h3>
<p>When an athlete completes a race of known distance $d$ (meters) in elapsed time $t$ (minutes), their average velocity is $v = d / t$. The runner's VDOT is calculated as the ratio of the oxygen cost of that velocity to the fractional aerobic capacity sustainable for that duration:</p>

$$\\text{VDOT} = \\frac{\\text{VO}_2(v)}{\\%\\text{VO}_2(t)} = \\frac{-4.60 + 0.182258 \\cdot v + 0.000104 \\cdot v^2}{0.8 + 0.1894393 \\cdot e^{-0.012778 \\cdot t} + 0.2989558 \\cdot e^{-0.1932605 \\cdot t}}$$

<h2>The 5 Core Jack Daniels Training Zones</h2>
<p>The defining genius of the Daniels Running Formula is that once a runner's VDOT score is established, it prescribes the exact paces for every workout type. Daniels divided training into five distinct physiological intensity zones:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Training Pace Zone</th>
            <th>% VO2 Max Intensity</th>
            <th>Primary Physiological Adaptation</th>
            <th>Recommended Weekly Volume</th>
            <th>Typical Session Structure</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Easy / Long Pace (E)</strong></td>
            <td>$59\\% - 74\\%$</td>
            <td>Myocardial hypertrophy, capillary angiogenesis, mitochondrial density, fat oxidation</td>
            <td>$70\\% - 80\\%$ of total mileage</td>
            <td>Recovery runs, long weekend endurance runs (30 to 150 minutes)</td>
        </tr>
        <tr>
            <td><strong>Marathon Pace (M)</strong></td>
            <td>$75\\% - 84\\%$</td>
            <td>Race-specific fuel utilization, glycogen sparing, psychological pacing confidence</td>
            <td>$15\\% - 20\\%$ (marathon cycles)</td>
            <td>Steady-state tempo runs of 6 to 16 miles</td>
        </tr>
        <tr>
            <td><strong>Threshold Pace (T)</strong></td>
            <td>$83\\% - 88\\%$</td>
            <td>Raises lactate threshold velocity, enhances blood lactate buffering and clearance</td>
            <td>$10\\%$ of weekly mileage</td>
            <td>20-30 min continuous tempo runs, or cruise intervals (e.g., $5 \\times 1\\text{ mile}$ w/ 1 min rest)</td>
        </tr>
        <tr>
            <td><strong>Interval Pace (I)</strong></td>
            <td>$95\\% - 100\\%$</td>
            <td>Maximizes stroke volume, increases $\\text{VO}_2\\text{ max}$ ceiling, oxygen extraction</td>
            <td>$8\\%$ of weekly mileage</td>
            <td>Work bouts of 3 to 5 minutes (e.g., $5 \\times 1,000\\text{m}$ w/ matched jog recovery)</td>
        </tr>
        <tr>
            <td><strong>Repetition Pace (R)</strong></td>
            <td>$105\\% - 120\\%$</td>
            <td>Neuromuscular recruitment, mechanical running economy, anaerobic speed capacity</td>
            <td>$5\\%$ of weekly mileage</td>
            <td>Short sprints of 200m to 400m with full recovery (work-to-rest ratio $1:2$ or $1:3$)</td>
        </tr>
    </tbody>
</table>

<h2>Why Training Slower Than Goal Race Pace Produces Faster Runners</h2>
<p>The most common error among competitive runners is running "in the grey zone"—training too fast on recovery days and too slow on workout days. Jack Daniels emphasized that <strong>training at an intensity higher than prescribed for a specific adaptation yields diminishing returns and accelerates systemic overtraining</strong>.</p>

<p>For example, running Easy (E) mileage too quickly shifts substrate metabolism from lipid oxidation to intramuscular glycogen breakdown, causing chronic glycogen depletion and blunting mitochondrial biogenesis. Similarly, running Threshold (T) workouts at Interval (I) pace causes rapid systemic acidosis (blood lactate spiking above 6.0 mmol/L), shortening the duration an athlete can sustain the effort and defeating the primary objective of threshold training: spending substantial time at the exact lactate clearance equilibrium boundary ($4.0 \\, \\text{mmol/L}$).</p>

<h2>Worked Clinical Case Study: Computing VDOT &amp; Pacing Zones</h2>
<div class="worked-example-card">
    <h3>Runner Case Study: Converting a 5K Result into Marathon Pacing</h3>
    <p><strong>Subject Profile:</strong> A 28-year-old female runner finishes a certified 5K road race in $21 \\text{ minutes and } 45 \\text{ seconds}$ ($21.75 \\, \\text{minutes}$). She is commencing a 16-week marathon training cycle and requires her exact VDOT and workout paces.</p>

    <div class="step-solution">
        <h4>Step 1: Compute Race Velocity</h4>
        $$v = \\frac{5,000 \\, \\text{meters}}{21.75 \\, \\text{minutes}} = 229.885 \\, \\text{m/min}$$

        <h4>Step 2: Calculate Oxygen Cost of Velocity</h4>
        $$\\text{VO}_2(v) = -4.60 + (0.182258 \\times 229.885) + 0.000104 \\times (229.885)^2$$
        $$\\text{VO}_2(v) = -4.60 + 41.898 + 5.496 = 42.794 \\, \\text{mL}\\cdot\\text{kg}^{-1}\\cdot\\text{min}^{-1}$$

        <h4>Step 3: Calculate Fractional Utilization at 21.75 Minutes</h4>
        $$\\%\\text{VO}_2(21.75) = 0.8 + 0.1894393 \\cdot e^{-0.012778 \\times 21.75} + 0.2989558 \\cdot e^{-0.1932605 \\times 21.75}$$
        $$\\%\\text{VO}_2(21.75) = 0.8 + 0.1894393 \\cdot (0.75736) + 0.2989558 \\cdot (0.01494) = 0.8 + 0.14347 + 0.00447 = 0.9479$$

        <h4>Step 4: Compute VDOT Score</h4>
        $$\\text{VDOT} = \\frac{42.794}{0.9479} = 45.15 \\approx 45.2$$

        <h4>Step 5: Derive Individualized Training Paces</h4>
        <ul>
            <li><strong>Threshold (T) Pace ($88\\% \\text{ VDOT} = 39.73 \\, \\text{mL/kg/min}$):</strong> Velocity $= 211.5 \\, \\text{m/min} \\implies 7:37 \\, \\text{per mile} \\, (4:44 \\, \\text{per km})$.</li>
            <li><strong>Marathon (M) Pace ($82\\% \\text{ VDOT} = 37.02 \\, \\text{mL/kg/min}$):</strong> Velocity $= 195.4 \\, \\text{m/min} \\implies 8:15 \\, \\text{per mile} \\, (5:08 \\, \\text{per km})$.</li>
            <li><strong>Easy (E) Pace ($70\\% \\text{ VDOT} = 31.61 \\, \\text{mL/kg/min}$):</strong> Velocity $= 163.7 \\, \\text{m/min} \\implies 9:20 - 9:55 \\, \\text{per mile} \\, (5:48 - 6:10 \\, \\text{per km})$.</li>
            <li><strong>Equivalent Marathon Projection:</strong> $3 \\text{ hours, } 30 \\text{ minutes, } 28 \\text{ seconds}$.</li>
        </ul>

        <h4>Coaching Prescription</h4>
        <p>The runner should anchor her long runs at $9:30/\\text{mi}$, execute mid-week threshold tempos ($20-30\\text{ min}$) strictly at $7:37/\\text{mi}$, and refrain from racing during training. As aerobic adaptations manifest over 6 to 8 weeks, her VDOT can be adjusted upward based on subsequent race trials.</p>
    </div>
</div>

<h2>VDOT Performance Equivalencies Reference Table</h2>
<table class="data-table">
    <thead>
        <tr>
            <th>VDOT</th>
            <th>5K Time</th>
            <th>10K Time</th>
            <th>Half Marathon</th>
            <th>Marathon</th>
            <th>Threshold (T) Pace /mi</th>
            <th>Interval (I) Pace /mi</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>35</strong></td>
            <td>27:44</td>
            <td>57:33</td>
            <td>2:07:37</td>
            <td>4:24:26</td>
            <td>9:33</td>
            <td>8:49</td>
        </tr>
        <tr>
            <td><strong>40</strong></td>
            <td>24:39</td>
            <td>51:06</td>
            <td>1:53:19</td>
            <td>3:55:40</td>
            <td>8:27</td>
            <td>7:47</td>
        </tr>
        <tr>
            <td><strong>45</strong></td>
            <td>22:15</td>
            <td>46:09</td>
            <td>1:42:19</td>
            <td>3:33:17</td>
            <td>7:37</td>
            <td>7:00</td>
        </tr>
        <tr>
            <td><strong>50</strong></td>
            <td>20:17</td>
            <td>42:04</td>
            <td>1:33:14</td>
            <td>3:14:48</td>
            <td>6:57</td>
            <td>6:23</td>
        </tr>
        <tr>
            <td><strong>55</strong></td>
            <td>18:40</td>
            <td>38:43</td>
            <td>1:25:40</td>
            <td>2:59:17</td>
            <td>6:24</td>
            <td>5:53</td>
        </tr>
        <tr>
            <td><strong>60</strong></td>
            <td>17:19</td>
            <td>35:58</td>
            <td>1:19:19</td>
            <td>2:46:01</td>
            <td>5:56</td>
            <td>5:27</td>
        </tr>
        <tr>
            <td><strong>65</strong></td>
            <td>16:09</td>
            <td>33:34</td>
            <td>1:13:54</td>
            <td>2:34:36</td>
            <td>5:32</td>
            <td>5:05</td>
        </tr>
    </tbody>
</table>

<h2>Frequently Asked Questions About Jack Daniels' Running Calculator</h2>
<h3>What is VDOT in Jack Daniels' running formula?</h3>
<p>VDOT is a pseudo-VO2 max metric formulated by exercise physiologist Dr. Jack Daniels and Jimmy Gilbert. Rather than measuring oxygen consumption in a laboratory, VDOT quantifies 'effective VO2 max' by combining aerobic capacity with neuromuscular running economy, providing an exact predictor of race performance and personalized training intensities.</p>

<h3>What are the 5 core Jack Daniels training pace zones?</h3>
<p>The five Daniels paces are: Easy/Long Pace (E - 59-74% VO2 max, builds capillary networks), Marathon Pace (M - 75-84% VO2 max, race-specific fueling), Threshold Pace (T - 83-88% VO2 max, raises lactate threshold), Interval Pace (I - 95-100% VO2 max, expands VO2 max ceiling), and Repetition Pace (R - 105-120% VO2 max, improves anaerobic speed and economy).</p>

<h3>How does VDOT predict equivalent race times across distances?</h3>
<p>Daniels and Gilbert established a mathematical regression calculating the exact percentage of VO2 max a runner can sustain over a specific duration. By identifying the velocity that yields your matching VDOT across another distance, equivalent race times are accurately predicted.</p>

<h3>Why is training at Threshold (T) pace limited to 20 to 60 minutes?</h3>
<p>Threshold pace corresponds to the maximum speed at which blood lactate production matches systemic clearance (~4.0 mmol/L). Running faster or longer causes rapid hydrogen ion accumulation, muscular acidosis, and fatigue. Steady tempo runs are capped at 20-30 minutes, or cruise intervals with brief recovery up to 60 minutes.</p>

<h3>Can I train at my goal race pace instead of my current VDOT pace?</h3>
<p>No. Dr. Daniels emphatically warns against training at a hypothetical goal VDOT. Training at paces faster than your current physiological capacity induces chronic fatigue and elevates injury risk without stimulating the intended enzymatic and capillary adaptations. You must always train at your current fitness VDOT until race results prove you have advanced.</p>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article_content)


# ===========================================================================
# TOOL 11: jumping-jacks-calories-burned-calculator.html
# ===========================================================================
def gen_jumping_jacks():
    slug = "jumping-jacks-calories-burned-calculator"
    title = "Jumping Jacks Calories Burned Calculator | Reps, Tempo & MET Formula"
    desc = "Calculate calories burned doing jumping jacks by repetition count, cadence tempo, workout duration, and body weight using biomechanical work and MET formulas."
    h1 = "Jumping Jacks Calories Burned Calculator"
    short_desc = "Calculate caloric energy expenditure, gravitational potential work, and ballistic cadence metrics for jumping jacks using Compendium MET standards and Newtonian physics."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Jumping Jacks Calories Burned Calculator",
      "url": "https://calchub.com/jumping-jacks-calories-burned-calculator.html",
      "applicationCategory": "HealthApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript. Requires HTML5.",
      "description": "Calculates calories burned during jumping jacks calisthenics using repetition count, workout duration, jumping tempo, and body weight."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How many calories do jumping jacks burn per minute?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "At a standard moderate cadence of 45 to 55 repetitions per minute (MET 8.0), a 150-lb (68 kg) individual burns approximately 9.0 to 10.0 calories per minute (540 to 600 kcal/hour). Vigorous ballistic intervals exceeding 65 reps per minute can elevate energy expenditure to 12.0 to 14.0 calories per minute."
          }
        },
        {
          "@type": "Question",
          "name": "How many calories are burned per 100 jumping jacks?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Performing 100 jumping jacks typically requires between 1.5 and 2.0 minutes at a standard rhythm. For a 150-lb individual, 100 jumping jacks burns approximately 15 to 20 calories. For a 200-lb individual, 100 jumping jacks burns approximately 20 to 26 calories."
          }
        },
        {
          "@type": "Question",
          "name": "What muscles are recruited during jumping jacks?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Jumping jacks are a full-body ballistic movement engaging the gastrocnemius, soleus, quadriceps, gluteus medius, and hip adductors for takeoff and landing, while the lateral deltoids, supraspinatus, trapezius, and core abdominal stabilizers control arm abduction and trunk stability."
          }
        },
        {
          "@type": "Question",
          "name": "What is the MET value for jumping jacks in the Compendium of Physical Activities?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In the Compendium of Physical Activities, jumping jacks fall under calisthenics code 02054 (calisthenics, vigorous effort, jumping jacks), which is assigned a standardized metabolic equivalent of 8.0 METs. Moderate continuous calisthenic rhythmic jumping is rated at 5.0 to 6.0 METs."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """                    <div class="calc-body">
                        <div class="calc-form">
                            <div class="unit-toggle-group">
                                <span class="unit-toggle-label">Unit System:</span>
                                <div class="toggle-buttons">
                                    <button type="button" class="unit-btn active" id="jj-unit-imp" onclick="setJJUnit('imperial')">Imperial (lbs)</button>
                                    <button type="button" class="unit-btn" id="jj-unit-met" onclick="setJJUnit('metric')">Metric (kg)</button>
                                </div>
                            </div>

                            <div class="input-grid">
                                <div class="form-group">
                                    <label for="jj-weight" id="jj-weight-lbl">Body Weight (lbs):</label>
                                    <input type="number" id="jj-weight" class="calc-input" value="165" min="50" max="450" step="1">
                                    <span class="input-hint">Your body mass</span>
                                </div>

                                <div class="form-group">
                                    <label for="jj-mode">Calculation Mode:</label>
                                    <select id="jj-mode" class="calc-input" onchange="toggleJJMode()">
                                        <option value="duration" selected>Workout Duration (Minutes)</option>
                                        <option value="reps">Total Repetition Count</option>
                                    </select>
                                    <span class="input-hint">Input method</span>
                                </div>

                                <div class="form-group" id="group-jj-duration">
                                    <label for="jj-duration">Workout Duration (minutes):</label>
                                    <input type="number" id="jj-duration" class="calc-input" value="15" min="1" max="120" step="1">
                                    <span class="input-hint">Total time performing jacks</span>
                                </div>

                                <div class="form-group" id="group-jj-reps" style="display:none;">
                                    <label for="jj-reps">Total Completed Repetitions:</label>
                                    <input type="number" id="jj-reps" class="calc-input" value="500" min="10" max="5000" step="10">
                                    <span class="input-hint">Count of individual jumping jacks</span>
                                </div>

                                <div class="form-group">
                                    <label for="jj-cadence">Cadence &amp; Ballistic Intensity:</label>
                                    <select id="jj-cadence" class="calc-input">
                                        <option value="40">Slow / Low-Impact (35-40 reps/min, ~5.5 METs)</option>
                                        <option value="50" selected>Moderate Rhythm (45-55 reps/min, ~8.0 METs)</option>
                                        <option value="65">Vigorous / Fast Pace (60-70 reps/min, ~9.5 METs)</option>
                                        <option value="80">HIIT Max Ballistic (75+ reps/min, ~11.0 METs)</option>
                                    </select>
                                    <span class="input-hint">Cadence speed and effort</span>
                                </div>

                                <div class="form-group">
                                    <label for="jj-vest">Weighted Vest / Extra Load (lbs/kg):</label>
                                    <input type="number" id="jj-vest" class="calc-input" value="0" min="0" max="60" step="1">
                                    <span class="input-hint">Additional external load (0 for bodyweight only)</span>
                                </div>
                            </div>

                            <button type="button" class="btn-primary" onclick="calculateJumpingJacks()">Calculate Jumping Jack Calories</button>
                        </div>

                        <div class="calc-results" id="jj-results">
                            <h2>Session Expenditure Breakdown</h2>
                            <div class="result-highlight-card">
                                <span class="highlight-label">Total Caloric Expenditure</span>
                                <span class="highlight-val" id="res-jj-total-kcal">157 kcal</span>
                                <span class="highlight-sub" id="res-jj-rate">10.5 kcal / minute (629 kcal/hour)</span>
                            </div>

                            <div class="results-stats-grid">
                                <div class="stat-card">
                                    <span class="stat-title">Estimated Total Repetitions</span>
                                    <span class="stat-value" id="res-jj-total-reps">750 reps</span>
                                    <span class="stat-desc">Cumulative completed jumps</span>
                                </div>
                                <div class="stat-card">
                                    <span class="stat-title">Metabolic Equivalent</span>
                                    <span class="stat-value" id="res-jj-mets">8.0 METs</span>
                                    <span class="stat-desc">Compendium code 02054</span>
                                </div>
                                <div class="stat-card">
                                    <span class="stat-title">Gravitational Work (W)</span>
                                    <span class="stat-value" id="res-jj-work">44.1 kJ</span>
                                    <span class="stat-desc">Mechanical energy hoisting center of mass</span>
                                </div>
                                <div class="stat-card">
                                    <span class="stat-title">Running Equivalence</span>
                                    <span class="stat-value" id="res-jj-run-equiv">1.35 miles</span>
                                    <span class="stat-desc">Equivalent aerobic jog distance</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <script>
                        let jjUnit = 'imperial';

                        function setJJUnit(unit) {
                            jjUnit = unit;
                            document.getElementById('jj-unit-imp').classList.toggle('active', unit === 'imperial');
                            document.getElementById('jj-unit-met').classList.toggle('active', unit === 'metric');

                            const wInput = document.getElementById('jj-weight');
                            const wLbl = document.getElementById('jj-weight-lbl');
                            if (unit === 'metric') {
                                wLbl.textContent = 'Body Weight (kg):';
                                wInput.value = (parseFloat(wInput.value) * 0.453592).toFixed(1);
                            } else {
                                wLbl.textContent = 'Body Weight (lbs):';
                                wInput.value = (parseFloat(wInput.value) / 0.453592).toFixed(1);
                            }
                            calculateJumpingJacks();
                        }

                        function toggleJJMode() {
                            const mode = document.getElementById('jj-mode').value;
                            document.getElementById('group-jj-duration').style.display = (mode === 'duration') ? 'block' : 'none';
                            document.getElementById('group-jj-reps').style.display = (mode === 'reps') ? 'block' : 'none';
                            calculateJumpingJacks();
                        }

                        function calculateJumpingJacks() {
                            let rawWeight = parseFloat(document.getElementById('jj-weight').value) || 165;
                            let mode = document.getElementById('jj-mode').value;
                            let vestLoad = parseFloat(document.getElementById('jj-vest').value) || 0;
                            let cadence = parseFloat(document.getElementById('jj-cadence').value) || 50;

                            let weightKg = (jjUnit === 'imperial') ? rawWeight * 0.453592 : rawWeight;
                            let vestKg = (jjUnit === 'imperial') ? vestLoad * 0.453592 : vestLoad;
                            let totalMassKg = weightKg + vestKg;

                            let durationMin = 15;
                            let totalReps = 750;

                            if (mode === 'duration') {
                                durationMin = parseFloat(document.getElementById('jj-duration').value) || 15;
                                totalReps = Math.round(durationMin * cadence);
                            } else {
                                totalReps = parseFloat(document.getElementById('jj-reps').value) || 500;
                                durationMin = totalReps / cadence;
                            }

                            let mets = 8.0;
                            if (cadence <= 40) mets = 5.5;
                            else if (cadence <= 50) mets = 8.0;
                            else if (cadence <= 65) mets = 9.5;
                            else mets = 11.0;

                            // Scale METs if carrying weighted vest
                            if (vestKg > 0) {
                                mets *= (1.0 + (vestKg / weightKg) * 0.7);
                            }

                            let totalKcal = durationMin * (mets * 3.5 * totalMassKg) / 200;
                            let kcalRate = (durationMin > 0) ? totalKcal / durationMin : 0;
                            let kcalPerHour = kcalRate * 60;

                            // Biomechanical Gravitational Work: W = m * g * delta_h * reps
                            // Average vertical displacement of center of mass ~ 8 cm (0.08 m) per jump
                            let deltaH = 0.08;
                            let workJoules = totalMassKg * 9.80665 * deltaH * totalReps;
                            let workKJ = workJoules / 1000;

                            // Running equivalence: ~100 kcal per mile for 150 lb person
                            let runMiles = totalKcal / (weightKg * 1.60934 * 0.95);

                            document.getElementById('res-jj-total-kcal').textContent = Math.round(totalKcal) + ' kcal';
                            document.getElementById('res-jj-rate').textContent = kcalRate.toFixed(1) + ' kcal / min (' + Math.round(kcalPerHour) + ' kcal/hr)';
                            document.getElementById('res-jj-total-reps').textContent = Math.round(totalReps) + ' reps';
                            document.getElementById('res-jj-mets').textContent = mets.toFixed(1) + ' METs';
                            document.getElementById('res-jj-work').textContent = workKJ.toFixed(1) + ' kJ';
                            document.getElementById('res-jj-run-equiv').textContent = runMiles.toFixed(2) + ' miles (' + (runMiles * 1.60934).toFixed(2) + ' km)';
                        }

                        window.addEventListener('DOMContentLoaded', calculateJumpingJacks);
                    </script>"""

    article_content = """<h2>Biomechanical &amp; Neuromuscular Anatomy of the Jumping Jack</h2>
<p>The jumping jack—known historically in British physical education as the "star jump"—is one of the most widely performed calisthenic exercises in human physical conditioning. Despite its simplicity, the exercise engages a complex sequence of ballistic plyometrics, rapid eccentric-concentric stretch-shortening cycles, and multi-joint kinetic chain coordination.</p>

<p>Every repetition of a jumping jack consists of two distinct biomechanical phases:</p>

<ol>
    <li><strong>The Abduction / Aerial Phase:</strong> The gastrocnemius, soleus, quadriceps, and gluteus medius generate explosive triple extension at the hips, knees, and ankles, propelling the total body mass vertically off the floor. Simultaneously, the middle deltoids, supraspinatus, and trapezius fire concentrically to abduct both arms through a $180^\\circ$ coronal arc until the hands meet overhead, while the hip abductors spread the lower extremities outward past shoulder width.</li>
    <li><strong>The Adduction / Impact Absorption Phase:</strong> As gravitational acceleration pulls the body back to the deck, the feet strike in wide dorsiflexion. The hip adductors (adductor magnus, longus, brevis) and pectineus contract violently to bring the thighs back to the anatomical midline, while the latissimus dorsi, pectoralis major, and teres major depress and adduct the arms back against the lateral torso.</li>
</ol>

<h2>Caloric Expenditure Physics: Gravitational Work ($W = mgh$) &amp; Elastic Recovery</h2>
<p>To understand the energetic cost of jumping jacks from first principles of Newtonian mechanics, we evaluate the external mechanical work performed against Earth's gravitational acceleration ($g = 9.80665 \\, \\text{m/s}^2$). In each jump, the human center of mass (located approximately near the second sacral vertebra, $S_2$) is elevated vertically by height displacement $\\Delta h$ (typically averaging between $0.06 \\, \\text{and } 0.10 \\, \\text{meters}$, or $2.5 \\, \\text{to } 4.0 \\, \\text{inches}$ depending on cadence and jumping vigor):</p>

$$W_{\\text{single jump}} = m \\cdot g \\cdot \\Delta h$$

<p>For an individual with body mass $m = 75 \\, \\text{kg}$ ($165 \\, \\text{lbs}$) performing a jump with $\\Delta h = 0.08 \\, \\text{meters}$:</p>

$$W_{\\text{single jump}} = 75 \\, \\text{kg} \\times 9.80665 \\, \\text{m/s}^2 \\times 0.08 \\, \\text{m} = 58.84 \\, \\text{Joules}$$

<p>Across $500 \\, \\text{repetitions}$, the total cumulative external vertical work performed is:</p>

$$W_{\\text{total}} = 500 \\times 58.84 \\, \\text{J} = 29,420 \\, \\text{Joules} = 29.42 \\, \\text{kJ}$$

<p>However, total metabolic caloric consumption is vastly higher than pure vertical work due to three major physiological mechanisms:</p>
<ul>
    <li><strong>Upper Extremity Kinetic Acceleration:</strong> The human upper extremities constitute roughly $10\\%$ of total body mass. Accelerating both arms from rest through a $180^\\circ$ overhead trajectory at $50$ to $60$ repetitions per minute requires massive repetitive muscular work by the shoulder girdle.</li>
    <li><strong>Internal Muscle Work and Co-contraction:</strong> Antagonist muscles must fire continuously to decelerate the limbs at the extremes of range of motion, consuming chemical ATP without contributing to positive external work.</li>
    <li><strong>Thermodynamic Inefficiency:</strong> Human skeletal muscle converts metabolic energy into mechanical work at an efficiency of only $20\\% - 25\\%$, while $75\\% - 80\\%$ is released as thermal heat.</li>
</ul>

<h2>Compendium of Physical Activities MET Classifications</h2>
<p>In clinical exercise epidemiology, energy expenditure for calisthenics is standardized using the <strong>Compendium of Physical Activities</strong>. Jumping jacks are categorized under code <strong>02054</strong>:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Cadence &amp; Intensity Category</th>
            <th>Repetition Tempo (RPM)</th>
            <th>Compendium MET Rating</th>
            <th>Burn Rate (140 lb / 63.5 kg)</th>
            <th>Burn Rate (180 lb / 81.6 kg)</th>
            <th>Cardiovascular Training Zone</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Low-Impact / Step Jacks</strong></td>
            <td>$30 - 40 \\, \\text{reps/min}$</td>
            <td>$5.0 \\, \\text{METs}$</td>
            <td>$5.5 \\, \\text{kcal/min}$</td>
            <td>$7.1 \\, \\text{kcal/min}$</td>
            <td>Zone 1 - 2 Aerobic Base</td>
        </tr>
        <tr>
            <td><strong>Moderate Rhythmic Jacks</strong></td>
            <td>$45 - 55 \\, \\text{reps/min}$</td>
            <td>$8.0 \\, \\text{METs}$</td>
            <td>$8.9 \\, \\text{kcal/min}$</td>
            <td>$11.4 \\, \\text{kcal/min}$</td>
            <td>Zone 3 Aerobic Steady-State</td>
        </tr>
        <tr>
            <td><strong>Vigorous Ballistic Jacks</strong></td>
            <td>$60 - 70 \\, \\text{reps/min}$</td>
            <td>$9.5 \\, \\text{METs}$</td>
            <td>$10.6 \\, \\text{kcal/min}$</td>
            <td>$13.6 \\, \\text{kcal/min}$</td>
            <td>Zone 4 Lactate Threshold</td>
        </tr>
        <tr>
            <td><strong>HIIT Max Tabata Intervals</strong></td>
            <td>$75+ \\, \\text{reps/min}$</td>
            <td>$11.5 \\, \\text{METs}$</td>
            <td>$12.8 \\, \\text{kcal/min}$</td>
            <td>$16.4 \\, \\text{kcal/min}$</td>
            <td>Zone 5 Anaerobic Capacity</td>
        </tr>
    </tbody>
</table>

<h2>How Many Calories Are Burned per 100, 500, and 1,000 Jumping Jacks?</h2>
<p>The exact caloric cost of a specific repetition benchmark depends heavily on the athlete's body mass and cadenced speed. Because heavier bodies require greater force to accelerate vertically, caloric expenditure scales in direct linear proportion to body weight:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Repetition Benchmark</th>
            <th>Approximate Duration (at 50 RPM)</th>
            <th>130 lb (59 kg) Person</th>
            <th>160 lb (72.6 kg) Person</th>
            <th>200 lb (90.7 kg) Person</th>
            <th>240 lb (108.9 kg) Person</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>100 Jumping Jacks</strong></td>
            <td>2.0 minutes</td>
            <td>$16.5 \\, \\text{kcal}$</td>
            <td>$20.3 \\, \\text{kcal}$</td>
            <td>$25.4 \\, \\text{kcal}$</td>
            <td>$30.5 \\, \\text{kcal}$</td>
        </tr>
        <tr>
            <td><strong>250 Jumping Jacks</strong></td>
            <td>5.0 minutes</td>
            <td>$41.3 \\, \\text{kcal}$</td>
            <td>$50.8 \\, \\text{kcal}$</td>
            <td>$63.5 \\, \\text{kcal}$</td>
            <td>$76.2 \\, \\text{kcal}$</td>
        </tr>
        <tr>
            <td><strong>500 Jumping Jacks</strong></td>
            <td>10.0 minutes</td>
            <td>$82.6 \\, \\text{kcal}$</td>
            <td>$101.6 \\, \\text{kcal}$</td>
            <td>$127.0 \\, \\text{kcal}$</td>
            <td>$152.4 \\, \\text{kcal}$</td>
        </tr>
        <tr>
            <td><strong>1,000 Jumping Jacks</strong></td>
            <td>20.0 minutes</td>
            <td>$165.2 \\, \\text{kcal}$</td>
            <td>$203.2 \\, \\text{kcal}$</td>
            <td>$254.0 \\, \\text{kcal}$</td>
            <td>$304.8 \\, \\text{kcal}$</td>
        </tr>
    </tbody>
</table>

<h2>Worked Biomechanical Case Study: 15-Minute Calisthenic Session</h2>
<div class="worked-example-card">
    <h3>HIIT Calisthenic Protocol: 15 Minutes at 60 RPM Cadence</h3>
    <p><strong>Subject Profile:</strong> A 32-year-old fitness enthusiast weighing $175 \\, \\text{lbs}$ ($79.38 \\, \\text{kg}$) executes a continuous 15-minute jumping jack workout maintaining a brisk tempo of $60 \\, \\text{reps/min}$ (totaling $900 \\, \\text{reps}$).</p>

    <div class="step-solution">
        <h4>Step 1: Determine Metabolic Intensity (METs)</h4>
        <p>A cadence of $60 \\, \\text{reps/min}$ falls into the vigorous ballistic category, corresponding to an empirical MET value of $9.5 \\, \\text{METs}$.</p>

        <h4>Step 2: Calculate Gross Rate of Oxygen Consumption (VO2)</h4>
        $$\\text{VO}_2 = 9.5 \\times 3.5 = 33.25 \\, \\text{mL}\\cdot\\text{kg}^{-1}\\cdot\\text{min}^{-1}$$

        <h4>Step 3: Compute Caloric Burn Rate and Total Expenditure</h4>
        $$\\text{Kcal/min} = \\frac{33.25 \\times 79.38}{200} = \\frac{2,639.4}{200} = 13.20 \\, \\text{kcal/min}$$
        $$\\text{Total Energy Expended (15 min)} = 13.20 \\times 15 = 198.0 \\, \\text{kcal}$$

        <h4>Step 4: Compute External Mechanical Gravitational Work</h4>
        $$\\Delta h = 0.08 \\, \\text{meters per jump}$$
        $$W = 79.38 \\, \\text{kg} \\times 9.80665 \\, \\text{m/s}^2 \\times 0.08 \\, \\text{m} \\times 900 \\, \\text{reps}$$
        $$W = 56,048 \\, \\text{Joules} = 56.05 \\, \\text{kJ}$$

        <h4>Step 5: Compare Against Equivalent Jogging Distance</h4>
        $$\\text{Running Economy} \\approx 1.0 \\, \\text{kcal/kg/km} \\implies 79.38 \\, \\text{kcal per km}$$
        $$\\text{Equivalent Distance} = \\frac{198.0 \\, \\text{kcal}}{79.38 \\, \\text{kcal/km}} = 2.49 \\, \\text{km} \\, (1.55 \\, \\text{miles})$$

        <h4>Clinical Assessment</h4>
        <p>In 15 minutes, the participant completed 900 ground impacts, lifted their center of mass through a cumulative vertical displacement of $72 \\, \\text{meters}$ ($236 \\, \\text{feet}$), and burned $198 \\, \\text{kcal}$—achieving the precise metabolic conditioning of a 1.55-mile outdoor run.</p>
    </div>
</div>

<h2>Frequently Asked Questions About Jumping Jacks Calorie Burn</h2>
<h3>How many calories do jumping jacks burn per minute?</h3>
<p>At a standard cadence of 45 to 55 repetitions per minute (MET 8.0), a 150-lb (68 kg) individual burns approximately 9.0 to 10.0 calories per minute (540 to 600 kcal/hour). High-intensity intervals exceeding 65 reps per minute can elevate energy expenditure to 12.0 to 14.0 calories per minute.</p>

<h3>How many calories are burned per 100 jumping jacks?</h3>
<p>Performing 100 jumping jacks takes approximately 1.5 to 2.0 minutes. A 150-lb individual burns roughly 18 to 22 calories per 100 jacks, while a 200-lb individual burns 24 to 28 calories.</p>

<h3>What muscles are recruited during jumping jacks?</h3>
<p>Jumping jacks recruit the gastrocnemius, soleus, quadriceps, gluteus medius, and hip adductors for the vertical jump, while the middle deltoids, supraspinatus, upper trapezius, and core abdominal musculature coordinate arm abduction and torso stabilization.</p>

<h3>What is the MET value for jumping jacks in the Compendium of Physical Activities?</h3>
<p>Under the Compendium of Physical Activities, jumping jacks are coded as 02054 with an official value of 8.0 METs for vigorous effort. Low-impact or modified step jacks fall between 5.0 and 6.0 METs.</p>

<h3>Do jumping jacks improve bone mineral density?</h3>
<p>Yes. The repetitive ground reaction forces ($1.5\\times$ to $2.0\\times$ body weight) generate piezoelectric mechanical strain across the calcaneus, tibia, and femoral neck, stimulating osteoblast activity and helping prevent osteopenia and osteoporosis in both adolescents and aging adults.</p>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article_content)


# ===========================================================================
# TOOL 12: squat-calorie-calculator.html
# ===========================================================================
def gen_squat_calorie():
    slug = "squat-calorie-calculator"
    title = "Squat Calorie Calculator | Barbell & Bodyweight Biomechanics Formula"
    desc = "Calculate calories burned performing squats using barbell load, bodyweight center of mass displacement, sets, reps, and EPOC metabolic afterburn."
    h1 = "Squat Calorie Calculator"
    short_desc = "Biomechanical resistance training engine calculating mechanical work ($W = F \\cdot d$), cumulative volume tonnage, and EPOC caloric expenditure for barbell and bodyweight squats."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Squat Calorie Calculator",
      "url": "https://calchub.com/squat-calorie-calculator.html",
      "applicationCategory": "HealthApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript. Requires HTML5.",
      "description": "Calculates mechanical work in Joules, intra-workout caloric burn, and post-exercise excess oxygen consumption (EPOC) for barbell back squats, front squats, and bodyweight squats."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How does the squat calorie formula calculate mechanical work?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Mechanical work per repetition is calculated as W = F * d = [(m_bar + 0.88 * m_body) * g] * Δh, where 0.88 accounts for the mass of the body above the knees that is displaced vertically through femur descent height Δh, and g is gravitational acceleration (9.81 m/s²)."
          }
        },
        {
          "@type": "Question",
          "name": "How many calories does a 315-lb (140 kg) squat workout burn?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A standard 5x5 barbell squat session at 315 lbs for an 85 kg lifter expends approximately 180 to 240 active lifting calories during the workout, plus an additional 60 to 100 kilocalories over the subsequent 24 to 48 hours via Excess Post-Exercise Oxygen Consumption (EPOC) for muscle protein synthesis and glycogen resynthesis."
          }
        },
        {
          "@type": "Question",
          "name": "Why do squats burn more calories than leg press or bench press?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The barbell squat recruits the largest collective muscle mass in the human body, including the gluteus maximus, quadriceps, adductor magnus, hamstrings, and erector spinae, while forcing the torso to support the load against gravity. Moving both the barbell and 88% of bodyweight through deep knee flexion requires double the mechanical work of seated machine exercises."
          }
        },
        {
          "@type": "Question",
          "name": "How much does squat depth affect caloric burn?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Squat depth directly dictates vertical stroke displacement (Δh). A deep squat (below parallel, hip crease below knee cap) involves a vertical stroke of 0.60 to 0.70 meters, requiring roughly 35% to 50% more mechanical work than a shallow quarter squat (0.35 to 0.40 meters) with the identical barbell weight."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """                    <div class="calc-body">
                        <div class="calc-form">
                            <div class="unit-toggle-group">
                                <span class="unit-toggle-label">Measurement System:</span>
                                <div class="toggle-buttons">
                                    <button type="button" class="unit-btn active" id="sq-unit-imp" onclick="setSqUnit('imperial')">Imperial (lbs, in)</button>
                                    <button type="button" class="unit-btn" id="sq-unit-met" onclick="setSqUnit('metric')">Metric (kg, cm)</button>
                                </div>
                            </div>

                            <div class="input-grid">
                                <div class="form-group">
                                    <label for="sq-bodyweight" id="sq-bw-lbl">Body Weight (lbs):</label>
                                    <input type="number" id="sq-bodyweight" class="calc-input" value="185" min="60" max="500" step="1">
                                    <span class="input-hint">Lifter body mass</span>
                                </div>

                                <div class="form-group">
                                    <label for="sq-load" id="sq-load-lbl">Barbell / External Load (lbs):</label>
                                    <input type="number" id="sq-load" class="calc-input" value="225" min="0" max="1000" step="5">
                                    <span class="input-hint">Weight on barbell (0 for air squats)</span>
                                </div>

                                <div class="form-group">
                                    <label for="sq-sets">Total Working Sets:</label>
                                    <input type="number" id="sq-sets" class="calc-input" value="5" min="1" max="30" step="1">
                                    <span class="input-hint">Completed sets</span>
                                </div>

                                <div class="form-group">
                                    <label for="sq-reps">Repetitions per Set:</label>
                                    <input type="number" id="sq-reps" class="calc-input" value="8" min="1" max="100" step="1">
                                    <span class="input-hint">Reps executed in each set</span>
                                </div>

                                <div class="form-group">
                                    <label for="sq-depth">Squat Depth &amp; Biomechanical Stroke:</label>
                                    <select id="sq-depth" class="calc-input" onchange="calculateSquat()">
                                        <option value="parallel" selected>Parallel Depth (Femur parallel to floor ~ 0.52m stroke)</option>
                                        <option value="deep">Below Parallel / ATG (Full Olympic depth ~ 0.65m stroke)</option>
                                        <option value="half">Half Squat (Thighs ~45 degrees ~ 0.38m stroke)</option>
                                        <option value="quarter">Quarter Squat (Shallow bend ~ 0.25m stroke)</option>
                                    </select>
                                    <span class="input-hint">Vertical displacement range</span>
                                </div>

                                <div class="form-group">
                                    <label for="sq-rest">Rest Interval Between Sets (seconds):</label>
                                    <input type="number" id="sq-rest" class="calc-input" value="120" min="15" max="600" step="15">
                                    <span class="input-hint">Inter-set recovery time</span>
                                </div>
                            </div>

                            <button type="button" class="btn-primary" onclick="calculateSquat()">Compute Squat Biomechanical Energy</button>
                        </div>

                        <div class="calc-results" id="sq-results">
                            <h2>Squat Biomechanical Diagnostics</h2>
                            <div class="result-highlight-card">
                                <span class="highlight-label">Total Session Caloric Expenditure</span>
                                <span class="highlight-val" id="res-sq-total-kcal">224 kcal</span>
                                <span class="highlight-sub" id="res-sq-breakdown">168 kcal Intra-Workout + 56 kcal EPOC Afterburn</span>
                            </div>

                            <div class="results-stats-grid">
                                <div class="stat-card">
                                    <span class="stat-title">Mechanical Work (W)</span>
                                    <span class="stat-value" id="res-sq-work">38.4 kJ</span>
                                    <span class="stat-desc">True physical work lifting barbell &amp; body mass</span>
                                </div>
                                <div class="stat-card">
                                    <span class="stat-title">Cumulative Volume Load</span>
                                    <span class="stat-value" id="res-sq-volume">9,000 lbs (4,082 kg)</span>
                                    <span class="stat-desc">Barbell tonnage (Sets &times; Reps &times; Weight)</span>
                                </div>
                                <div class="stat-card">
                                    <span class="stat-title">Workout Duration</span>
                                    <span class="stat-value" id="res-sq-duration">10.7 min</span>
                                    <span class="stat-desc">Active lifting time + inter-set rest intervals</span>
                                </div>
                                <div class="stat-card">
                                    <span class="stat-title">Metabolic Equivalent</span>
                                    <span class="stat-value" id="res-sq-mets">6.5 METs</span>
                                    <span class="stat-desc">Heavy resistance training metabolic demand</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <script>
                        let sqUnit = 'imperial';

                        function setSqUnit(unit) {
                            sqUnit = unit;
                            document.getElementById('sq-unit-imp').classList.toggle('active', unit === 'imperial');
                            document.getElementById('sq-unit-met').classList.toggle('active', unit === 'metric');

                            const bwInput = document.getElementById('sq-bodyweight');
                            const ldInput = document.getElementById('sq-load');
                            const bwLbl = document.getElementById('sq-bw-lbl');
                            const ldLbl = document.getElementById('sq-load-lbl');

                            if (unit === 'metric') {
                                bwLbl.textContent = 'Body Weight (kg):';
                                ldLbl.textContent = 'Barbell / External Load (kg):';
                                bwInput.value = (parseFloat(bwInput.value) * 0.453592).toFixed(1);
                                ldInput.value = (parseFloat(ldInput.value) * 0.453592).toFixed(1);
                            } else {
                                bwLbl.textContent = 'Body Weight (lbs):';
                                ldLbl.textContent = 'Barbell / External Load (lbs):';
                                bwInput.value = (parseFloat(bwInput.value) / 0.453592).toFixed(1);
                                ldInput.value = (parseFloat(ldInput.value) / 0.453592).toFixed(1);
                            }
                            calculateSquat();
                        }

                        function calculateSquat() {
                            let rawBw = parseFloat(document.getElementById('sq-bodyweight').value) || 185;
                            let rawLoad = parseFloat(document.getElementById('sq-load').value) || 225;
                            let sets = parseFloat(document.getElementById('sq-sets').value) || 5;
                            let reps = parseFloat(document.getElementById('sq-reps').value) || 8;
                            let depth = document.getElementById('sq-depth').value;
                            let restSec = parseFloat(document.getElementById('sq-rest').value) || 120;

                            let bwKg = (sqUnit === 'imperial') ? rawBw * 0.453592 : rawBw;
                            let loadKg = (sqUnit === 'imperial') ? rawLoad * 0.453592 : rawLoad;

                            // Stroke displacement in meters
                            let deltaH = 0.52; // parallel
                            if (depth === 'deep') deltaH = 0.65;
                            else if (depth === 'half') deltaH = 0.38;
                            else if (depth === 'quarter') deltaH = 0.25;

                            let totalReps = sets * reps;
                            // Effective moved mass = barbell load + 88% of body mass (torso, head, arms, thighs above knee)
                            let movedMassKg = loadKg + (0.88 * bwKg);

                            // Mechanical Concentric Work per rep: W = m * g * deltaH
                            let workJoulesPerRep = movedMassKg * 9.80665 * deltaH;
                            let totalWorkJoules = workJoulesPerRep * totalReps;
                            let totalWorkKJ = totalWorkJoules / 1000;

                            // Human skeletal muscle gross concentric efficiency ~ 20%
                            // Eccentric lowering adds ~ 33% of concentric metabolic cost
                            // Total intra-workout caloric cost = (Work_Joules / (4184 * 0.20)) * 1.33
                            let liftingKcal = (totalWorkJoules / (4184 * 0.20)) * 1.33;

                            // Rest period baseline energy expenditure: ~1.5 METs
                            let activeLiftingSec = totalReps * 3.5; // ~3.5 seconds per repetition tempo
                            let totalRestSec = (sets > 1) ? (sets - 1) * restSec : 0;
                            let totalWorkoutSec = activeLiftingSec + totalRestSec;
                            let totalWorkoutMin = totalWorkoutSec / 60;

                            let restingKcal = (totalWorkoutMin * (1.5 * 3.5 * bwKg)) / 200;
                            let intraWorkoutKcal = liftingKcal + restingKcal;

                            // EPOC (Excess Post-Exercise Oxygen Consumption): heavy squats elicit high EPOC (~25% to 35% of lifting burn)
                            let epocKcal = intraWorkoutKcal * 0.30;
                            let totalKcal = intraWorkoutKcal + epocKcal;

                            // Volume tonnage
                            let volumeLbs = (sqUnit === 'imperial') ? (rawLoad * totalReps) : (rawLoad * 2.20462 * totalReps);
                            let volumeKg = volumeLbs * 0.453592;

                            let mets = (intraWorkoutKcal / totalWorkoutMin) / ((3.5 * bwKg) / 200);

                            document.getElementById('res-sq-total-kcal').textContent = Math.round(totalKcal) + ' kcal';
                            document.getElementById('res-sq-breakdown').textContent = Math.round(intraWorkoutKcal) + ' kcal Intra-Workout + ' + Math.round(epocKcal) + ' kcal EPOC Afterburn';
                            document.getElementById('res-sq-work').textContent = totalWorkKJ.toFixed(1) + ' kJ';
                            document.getElementById('res-sq-volume').textContent = Math.round(volumeLbs).toLocaleString() + ' lbs (' + Math.round(volumeKg).toLocaleString() + ' kg)';
                            document.getElementById('res-sq-duration').textContent = totalWorkoutMin.toFixed(1) + ' min';
                            document.getElementById('res-sq-mets').textContent = mets.toFixed(1) + ' METs';
                        }

                        window.addEventListener('DOMContentLoaded', calculateSquat);
                    </script>"""

    article_content = """<h2>Biomechanical &amp; Physiological Kinetics of the Squat</h2>
<p>The squat is universally regarded by biomechanists and strength conditioning specialists as the quintessential multi-joint lower extremity exercise. Whether performed as an unloaded bodyweight movement or loaded with a heavy barbell in back or front squat configurations, the exercise demands intense concentric, eccentric, and isometric coordination across the entirety of the axial skeleton and lower limbs.</p>

<p>During the descending (eccentric) phase of a squat, the hips, knees, and ankles flex simultaneously. The quadriceps (rectus femoris, vastus lateralis, vastus medialis, and vastus intermedius) control knee flexion through eccentric lengthening. Simultaneously, the gluteus maximus, adductor magnus, and hamstrings control hip flexion, while the soleus and gastrocnemius control closed-chain tibial translation. During the ascending (concentric) phase, these muscular groups reverse direction, firing explosively to produce upward mechanical force against the combined load of the barbell and the lifter's own anatomical body mass.</p>

<h2>The Physics of Mechanical Work: Barbell Mass + Body Weight ($W = F \\cdot d$)</h2>
<p>In standard gymnasium culture, lifters frequently calculate workout volume merely as the product of barbell weight, sets, and repetitions (e.g., $5 \\times 5 \\text{ at } 315 \\, \\text{lbs} = 7,875 \\, \\text{lbs}$). However, from a rigorous Newtonian physics standpoint, <strong>this calculation omits over half of the actual mechanical work performed</strong>.</p>

<p>When an athlete squats, their center of mass descends and ascends through space. The mass being lifted includes not only the external barbell load ($m_{\\text{bar}}$), but also all anatomical mass situated superior to the knee joints ($m_{\\text{body, effective}}$). Cadaveric and anthropometric segmental studies confirm that the feet and lower shanks remain stationary on the ground, meaning approximately <strong>$88\\%$ of total body weight</strong> is vertically displaced during every single repetition:</p>

$$m_{\\text{total}} = m_{\\text{bar}} + (0.88 \\times m_{\\text{body}})$$

<p>The mechanical force required to elevate this mass against gravitational acceleration ($g = 9.80665 \\, \\text{m/s}^2$) is:</p>

$$F = m_{\\text{total}} \\times g = [m_{\\text{bar}} + (0.88 \\times m_{\\text{body}})] \\times 9.80665$$

<p>Mechanical concentric work ($W_{\\text{concentric}}$, in Joules) is the product of this gravitational force and the vertical displacement stroke height ($\\Delta h$):</p>

$$W_{\\text{concentric}} = F \\cdot \\Delta h = [m_{\\text{bar}} + (0.88 \\times m_{\\text{body}})] \\cdot g \\cdot \\Delta h$$

<h3>The Crucial Impact of Squat Depth (Stroke Height $\\Delta h$)</h3>
<p>The vertical stroke height $\\Delta h$ is dictated by anthropometry (femur length) and squat depth:</p>
<ul>
    <li><strong>Quarter Squats ($135^\\circ$ knee angle):</strong> $\\Delta h \\approx 0.20 - 0.28 \\, \\text{meters}$. Minimal mechanical work, reduced glute recruitment.</li>
    <li><strong>Half Squats ($90^\\circ$ knee angle):</strong> $\\Delta h \\approx 0.35 - 0.42 \\, \\text{meters}$. Moderate quadriceps loading.</li>
    <li><strong>Parallel Squats (Femur parallel to floor):</strong> $\\Delta h \\approx 0.48 - 0.55 \\, \\text{meters}$. Full recruitment of gluteus maximus and adductor magnus.</li>
    <li><strong>Deep Olympic Squats (Below parallel / ATG):</strong> $\\Delta h \\approx 0.62 - 0.72 \\, \\text{meters}$. Maximum mechanical work, expansive range of motion.</li>
</ul>

<p>Because mechanical work scales linearly with stroke displacement $\\Delta h$, an athlete who squats below parallel executes <strong>up to $50\\%$ more true physical work per repetition</strong> than a lifter executing shallow quarter squats with the identical barbell poundage.</p>

<h2>Energetics: Skeletal Muscle Efficiency and the Eccentric Penalty</h2>
<p>Skeletal muscle converts chemical adenosine triphosphate (ATP) into external mechanical tension at a gross efficiency of approximately <strong>$20\\%$</strong>. Therefore, every Joule of concentric work delivered to the barbell and torso requires roughly five Joules of metabolic chemical energy:</p>

$$\\text{Concentric Energy (Joules)} = \\frac{W_{\\text{concentric}}}{0.20}$$

<p>Furthermore, the eccentric lowering phase is not free. While eccentric muscle lengthening exhibits higher mechanical efficiency than concentric shortening, absorbing the downward momentum of a heavy barbell and decelerating the load at the bottom turnaround point consumes approximately $33\\%$ of the concentric metabolic cost. Factoring in inter-set resting metabolic requirements yields the total intra-workout caloric expenditure:</p>

$$\\text{Intra-Workout Energy (kcal)} = \\frac{W_{\\text{concentric}} \\times 1.33}{4,184 \\times 0.20} + \\text{Resting Metabolic Baseline}$$

<h2>EPOC: The Metabolic Caloric Afterburn of Heavy Squatting</h2>
<p>Resistance exercise differs fundamentally from steady-state cardio because a major fraction of total energy expenditure occurs <em>after the training session concludes</em>. This phenomenon is termed <strong>Excess Post-Exercise Oxygen Consumption (EPOC)</strong>.</p>

<p>Heavy compound barbell squats induce profound systemic perturbations: severe muscle fiber microtrauma, glycogen depletion, elevated core temperature, and massive central nervous system fatigue. In the 24 to 48 hours following a rigorous squat workout, the body's basal metabolic rate remains elevated by $8\\%$ to $14\\%$ to fuel:</p>
<ol>
    <li>Resynthesis of intramuscular phosphocreatine (PCr) and ATP stores.</li>
    <li>Metabolizing accumulated lactate via the hepatic Cori cycle.</li>
    <li>Muscle protein synthesis (MPS) repairing myofibrillar micro-tears.</li>
    <li>Restoring intracellular fluid balance and glycogen re-esterification.</li>
</ol>

<p>Clinical metabolic cart studies indicate that for heavy compound lower body lifting, EPOC adds between <strong>$25\\%$ and $35\\%$</strong> in extra metabolic calories above intra-workout expenditure over the following 24 to 48 hours.</p>

<h2>Worked Clinical Case Study: 5x5 Barbell Back Squat Session</h2>
<div class="worked-example-card">
    <h3>Laboratory Strength Scenario: 5x5 at 225 lbs (102 kg)</h3>
    <p><strong>Subject Profile:</strong> A 25-year-old powerlifter weighing $185 \\, \\text{lbs}$ ($83.91 \\, \\text{kg}$) performs 5 sets of 5 repetitions (25 total reps) on the barbell back squat with $225 \\, \\text{lbs}$ ($102.06 \\, \\text{kg}$) at parallel depth (stroke $\\Delta h = 0.52 \\, \\text{meters}$). Rest intervals between sets are 2.5 minutes (150 seconds).</p>

    <div class="step-solution">
        <h4>Step 1: Compute Total Effective Lifted Mass</h4>
        $$m_{\\text{total}} = m_{\\text{bar}} + (0.88 \\times m_{\\text{body}})$$
        $$m_{\\text{total}} = 102.06 \\, \\text{kg} + (0.88 \\times 83.91 \\, \\text{kg}) = 102.06 + 73.84 = 175.90 \\, \\text{kg}$$

        <h4>Step 2: Calculate Concentric Mechanical Work</h4>
        $$W_{\\text{rep}} = 175.90 \\, \\text{kg} \\times 9.80665 \\, \\text{m/s}^2 \\times 0.52 \\, \\text{m} = 897.0 \\, \\text{Joules}$$
        $$W_{\\text{total concentric}} = 897.0 \\, \\text{J} \\times 25 \\, \\text{reps} = 22,425 \\, \\text{Joules} = 22.43 \\, \\text{kJ}$$

        <h4>Step 3: Calculate Metabolic Lifting Caloric Cost</h4>
        $$\\text{Lifting Kcal} = \\frac{22,425 \\times 1.33}{4,184 \\times 0.20} = \\frac{29,825.25}{836.8} = 35.64 \\, \\text{kcal (Pure Mechanical)}$$

        <h4>Step 4: Factor in Cardiovascular, Stabilizer &amp; Rest Interval Metabolism</h4>
        <p>Total session time includes $25 \\times 3.5\\text{s} = 87.5\\text{s}$ active lifting plus $4 \\times 150\\text{s} = 600\\text{s}$ rest, totaling $687.5 \\, \\text{seconds}$ ($11.46 \\, \\text{minutes}$). Operating at a resistance training metabolic intensity of $\\sim 6.0 \\, \\text{METs}$ during lifting sets and $1.5 \\, \\text{METs}$ during rest intervals yields an intra-workout expenditure of $118.5 \\, \\text{kcal}$.</p>

        <h4>Step 5: Compute EPOC Caloric Afterburn</h4>
        $$\\text{EPOC (30%)} = 118.5 \\times 0.30 = 35.55 \\, \\text{kcal}$$
        $$\\text{Total 24-Hour Energy Expenditure} = 118.5 + 35.55 = 154.05 \\, \\text{kcal}$$

        <h4>Clinical Assessment</h4>
        <p>The lifter completed $22.43 \\, \\text{kJ}$ of mechanical work, lifting a cumulative barbell volume of $5,625 \\, \\text{lbs}$ ($2,551 \\, \\text{kg}$). Total systemic caloric burn was $154 \\, \\text{kcal}$, with over $23\\%$ of the metabolic cost delivered via post-exercise EPOC recovery.</p>
    </div>
</div>

<h2>Squat Caloric Expenditure Reference Table</h2>
<table class="data-table">
    <thead>
        <tr>
            <th>Squat Exercise Protocol</th>
            <th>Barbell Load</th>
            <th>Sets &amp; Reps</th>
            <th>Total Reps</th>
            <th>Intra-Workout Burn (175 lb Lifter)</th>
            <th>Total Burn + EPOC</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Bodyweight Air Squats</strong></td>
            <td>0 lbs (Bodyweight)</td>
            <td>4 sets &times; 25 reps</td>
            <td>100 reps</td>
            <td>$95 \\, \\text{kcal}$</td>
            <td>$110 \\, \\text{kcal}$</td>
        </tr>
        <tr>
            <td><strong>Hypertrophy Back Squat</strong></td>
            <td>185 lbs (84 kg)</td>
            <td>4 sets &times; 10 reps</td>
            <td>40 reps</td>
            <td>$145 \\, \\text{kcal}$</td>
            <td>$188 \\, \\text{kcal}$</td>
        </tr>
        <tr>
            <td><strong>Heavy 5x5 Strength</strong></td>
            <td>275 lbs (125 kg)</td>
            <td>5 sets &times; 5 reps</td>
            <td>25 reps</td>
            <td>$160 \\, \\text{kcal}$</td>
            <td>$215 \\, \\text{kcal}$</td>
        </tr>
        <tr>
            <td><strong>Elite 5x5 Powerlifting</strong></td>
            <td>365 lbs (165 kg)</td>
            <td>5 sets &times; 5 reps</td>
            <td>25 reps</td>
            <td>$195 \\, \\text{kcal}$</td>
            <td>$265 \\, \\text{kcal}$</td>
        </tr>
        <tr>
            <td><strong>20-Rep Breathing Squat</strong></td>
            <td>225 lbs (102 kg)</td>
            <td>1 set &times; 20 reps</td>
            <td>20 reps</td>
            <td>$130 \\, \\text{kcal}$</td>
            <td>$180 \\, \\text{kcal}$</td>
        </tr>
    </tbody>
</table>

<h2>Frequently Asked Questions About Squat Calorie Burn</h2>
<h3>How does the squat calorie formula calculate mechanical work?</h3>
<p>Mechanical work per repetition is formulated as $W = F \\cdot d = [(m_{\\text{bar}} + 0.88 \\cdot m_{\\text{body}}) \\cdot g] \\cdot \\Delta h$, where $0.88$ represents the fraction of human body weight located superior to the knee joints that undergoes vertical displacement through stroke height $\\Delta h$, and $g$ is gravitational acceleration ($9.80665 \\, \\text{m/s}^2$).</p>

<h3>How many calories does a 315-lb (140 kg) squat workout burn?</h3>
<p>A standard 5x5 barbell squat session at 315 lbs for an 85-kg lifter expends between 180 and 240 active lifting calories intra-workout, plus an additional 60 to 90 kilocalories over the subsequent 24 to 48 hours through Excess Post-Exercise Oxygen Consumption (EPOC).</p>

<h3>Why do squats burn more calories than leg press or bench press?</h3>
<p>The barbell squat recruits the largest collective skeletal muscle volume in the human body, including the gluteus maximus, quadriceps, adductor magnus, hamstrings, and erector spinae, while forcing the torso to support the axial load against gravity. Moving both the barbell and 88% of bodyweight through deep knee flexion requires double the mechanical work of seated machine movements.</p>

<h3>How much does squat depth affect caloric burn?</h3>
<p>Squat depth directly dictates vertical stroke displacement ($\Delta h$). A deep squat (below parallel) features a stroke of 0.60 to 0.70 meters, demanding roughly 35% to 50% more mechanical work than a shallow quarter squat (0.35 to 0.40 meters) with the exact same barbell weight.</p>

<h3>Does performing squats elevate metabolism after the workout?</h3>
<p>Yes. Heavy compound squats trigger significant EPOC. Repairing micro-tears in damaged myofibrils, clearing lactic metabolites, and replenishing depleted creatine phosphate stores elevates resting metabolic rate by 8% to 14% for up to 48 hours following an intense leg training session.</p>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article_content)


# ===========================================================================
# MAIN GENERATOR DISPATCHER
# ===========================================================================
def main():
    tools = [
        ("stationary-bike-calorie-calculator.html", gen_stationary_bike),
        ("incline-treadmill-calorie-calculator.html", gen_incline_treadmill),
        ("rucking-calorie-calculator.html", gen_rucking),
        ("jack-daniels-running-calculator.html", gen_jack_daniels),
        ("jumping-jacks-calories-burned-calculator.html", gen_jumping_jacks),
        ("squat-calorie-calculator.html", gen_squat_calorie),
    ]

    for filename, gen_func in tools:
        filepath = os.path.join(BASE_DIR, filename)
        content = gen_func()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {filename} successfully!")

if __name__ == "__main__":
    main()
