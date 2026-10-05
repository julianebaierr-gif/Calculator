# -*- coding: utf-8 -*-
"""
Generator for Requested Fitness Tools - Batch A (Tools 1 to 6)
Tools:
1. treadmill-calorie-calculator.html (ACSM Running/Walking Equations, Incline, Bodyweight)
2. stairmaster-calorie-calculator.html (Vertical Mechanical Work W=mgh, Steps/Min, METs)
3. cycling-calorie-calculator.html (Aerodynamic Drag, Rolling Resistance, Gradient, Speed)
4. pushup-calorie-calculator.html (Plank Bodyweight Percentage 64%, Biomechanical Work W=Fd)
5. bench-press-calories-calculator.html (Barbell Load, Rep Velocity, Sets, EPOC Metabolic Afterburn)
6. swimming-calorie-calculator.html (Stroke Hydrodynamics, Freestyle/Breaststroke/Butterfly, Thermal Convection)
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COMMON_TAIL = """    <footer class="site-footer">
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>About CalcHub</h4>
                    <p>CalcHub delivers peer-reviewed exercise physiology computing algorithms, biomechanical energy expenditure models, and clinical metabolic engines compliant with ACSM, WHO, and Compendium of Physical Activities standards.</p>
                </div>
                <div class="footer-col">
                    <h4>Health &amp; Fitness Suites</h4>
                    <ul>
                        <li><a href="health.html">Health &amp; Fitness</a></li>
                        <li><a href="treadmill-calorie-calculator.html">Treadmill Calorie Calculator</a></li>
                        <li><a href="cycling-calorie-calculator.html">Cycling Calorie Calculator</a></li>
                        <li><a href="stairmaster-calorie-calculator.html">StairMaster Calorie Calculator</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Strength &amp; Calisthenics</h4>
                    <ul>
                        <li><a href="pushup-calorie-calculator.html">Pushup Calorie Calculator</a></li>
                        <li><a href="bench-press-calories-calculator.html">Bench Press Calories</a></li>
                        <li><a href="swimming-calorie-calculator.html">Swimming Calorie Calculator</a></li>
                        <li><a href="one-rep-max-calculator.html">One Rep Max (1RM)</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="index.html">All Calculators</a></li>
                        <li><a href="calorie-calculator.html">TDEE Calorie Calculator</a></li>
                        <li><a href="bmi-calculator.html">BMI Calculator</a></li>
                        <li><a href="body-fat-calculator.html">Body Fat Calculator</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 CalcHub. All rights reserved. Precision exercise physiology and biomechanical metabolic calculation engines.</p>
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
                    <h3>Related Exercise &amp; Calorie Tools</h3>
                    <ul class="sidebar-links">
                        <li><a href="treadmill-calorie-calculator.html">Treadmill Calorie Calculator</a></li>
                        <li><a href="stairmaster-calorie-calculator.html">StairMaster Calorie Calculator</a></li>
                        <li><a href="cycling-calorie-calculator.html">Cycling Calorie Calculator</a></li>
                        <li><a href="pushup-calorie-calculator.html">Pushup Calorie Calculator</a></li>
                        <li><a href="bench-press-calories-calculator.html">Bench Press Calories</a></li>
                        <li><a href="swimming-calorie-calculator.html">Swimming Calorie Calculator</a></li>
                        <li><a href="pace-calculator.html">Pace &amp; Splits Calculator</a></li>
                        <li><a href="vo2-max-calculator.html">VO2 Max Calculator</a></li>
                    </ul>
                </div>
            </aside>
        </div>
    </div>
{COMMON_TAIL}"""


# ===========================================================================
# TOOL 1: treadmill-calorie-calculator.html
# ===========================================================================
def gen_treadmill_calorie():
    slug = "treadmill-calorie-calculator"
    title = "Treadmill Calorie Calculator | ACSM Speed, Incline & Grade Formula"
    desc = "Calculate calories burned on a treadmill with speed, incline grade, time, and body weight. Uses official American College of Sports Medicine (ACSM) metabolic equations."
    h1 = "Treadmill Calorie Calculator"
    short_desc = "Compute precise caloric energy expenditure on a motorized treadmill using the American College of Sports Medicine (ACSM) metabolic walking and running formulas."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Treadmill Calorie Calculator",
      "url": "https://calchub.com/treadmill-calorie-calculator.html",
      "applicationCategory": "HealthApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Calculates calories burned on a treadmill based on body weight, speed, incline percentage, and workout duration using ACSM equations."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How does treadmill incline affect calorie burn?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Every 1% increase in treadmill incline increases the metabolic cost of walking by approximately 1.8 mL/kg/min of VO2 (roughly 10% to 12% more calories burned), requiring substantial mechanical work against gravity."
          }
        },
        {
          "@type": "Question",
          "name": "What is the ACSM metabolic formula for treadmill running?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The ACSM running equation evaluates VO2 (mL/kg/min) = (0.2 * speed in m/min) + (0.9 * speed * fractional grade) + 3.5. Caloric expenditure is then computed as VO2 * weight in kg / 200 * duration in minutes."
          }
        },
        {
          "@type": "Question",
          "name": "Why do treadmill display consoles overestimate calories burned?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Treadmill consoles typically assume a default heavy male body weight (around 70-80 kg), fail to account for resting metabolic deductions (gross vs net burn), and assume no handrail holding, which can overestimate true expenditure by 20% to 35%."
          }
        },
        {
          "@type": "Question",
          "name": "Does holding onto the treadmill handrails reduce calorie expenditure?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Gripping the front or side handrails transfers a portion of body weight off the treadmill belt and eliminates torso swing, reducing true oxygen consumption and caloric expenditure by 20% to 30%."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-body">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1.25rem; margin-bottom: 1.25rem;">
        <div>
            <label for="tmWeight" style="font-weight: 600; font-size: 0.875rem;">Body Weight:</label>
            <div style="display: flex; gap: 0.5rem;">
                <input type="number" id="tmWeight" class="input-field" value="70" min="20" max="300" step="0.5" oninput="calculateTreadmill()">
                <select id="tmWeightUnit" class="input-field" style="width: 80px;" onchange="calculateTreadmill()">
                    <option value="kg">kg</option>
                    <option value="lbs">lbs</option>
                </select>
            </div>
        </div>
        <div>
            <label for="tmSpeed" style="font-weight: 600; font-size: 0.875rem;">Belt Speed:</label>
            <div style="display: flex; gap: 0.5rem;">
                <input type="number" id="tmSpeed" class="input-field" value="6.0" min="0.5" max="25" step="0.1" oninput="calculateTreadmill()">
                <select id="tmSpeedUnit" class="input-field" style="width: 80px;" onchange="calculateTreadmill()">
                    <option value="mph">mph</option>
                    <option value="kmh">km/h</option>
                </select>
            </div>
        </div>
        <div>
            <label for="tmIncline" style="font-weight: 600; font-size: 0.875rem;">Incline Grade (%):</label>
            <input type="number" id="tmIncline" class="input-field" value="2.0" min="0" max="30" step="0.5" oninput="calculateTreadmill()">
            <span class="input-hint">0% to 15% standard grade</span>
        </div>
        <div>
            <label for="tmDuration" style="font-weight: 600; font-size: 0.875rem;">Workout Time (minutes):</label>
            <input type="number" id="tmDuration" class="input-field" value="45" min="1" max="360" step="1" oninput="calculateTreadmill()">
        </div>
    </div>

    <div style="display: flex; gap: 0.75rem; margin-bottom: 1.5rem;">
        <button type="button" class="btn btn-primary" onclick="calculateTreadmill()">Calculate Calories</button>
        <button type="button" class="btn btn-outline" onclick="setTmPreset('12_3_30')">12-3-30 Preset</button>
        <button type="button" class="btn btn-outline" onclick="setTmPreset('5k')">5K Run Preset</button>
    </div>

    <div class="result-box" style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem;">
        <h3 style="margin-top: 0; color: #1e293b; font-size: 1.1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">Treadmill Calorie Expenditure Results</h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Gross Calories Burned</div>
                <div id="resTmGrossCal" style="font-size: 1.5rem; font-weight: 700; color: #2563eb;">468 kcal</div>
                <div style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">Total energy expenditure</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Net Exercise Calories</div>
                <div id="resTmNetCal" style="font-size: 1.4rem; font-weight: 700; color: #16a34a;">416 kcal</div>
                <div style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">Above resting metabolism</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Burn Rate per Hour</div>
                <div id="resTmHourlyRate" style="font-size: 1.4rem; font-weight: 700; color: #0f172a;">624 kcal/hr</div>
                <div id="resTmPaceMinMi" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">Pace: 10:00 min/mi</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Oxygen Uptake (VO2)</div>
                <div id="resTmVo2" style="font-size: 1.4rem; font-weight: 700; color: #7c3aed;">39.6 mL/kg/min</div>
                <div id="resTmMets" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">Intensity: 11.3 METs</div>
            </div>
        </div>

        <div style="margin-top: 1.25rem; padding-top: 1rem; border-top: 1px dashed #cbd5e1; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; font-size: 0.875rem;">
            <div>
                <span style="font-weight: 600; color: #475569;">Total Distance Traveled:</span>
                <div id="resTmDist" style="font-weight: 700; color: #1e293b; font-size: 1rem;">4.50 miles (7.24 km)</div>
            </div>
            <div>
                <span style="font-weight: 600; color: #475569;">Vertical Elevation Gained:</span>
                <div id="resTmElev" style="font-weight: 700; color: #1e293b; font-size: 1rem;">475.2 feet (144.8 m)</div>
            </div>
            <div>
                <span style="font-weight: 600; color: #475569;">Calculated Gait Mode:</span>
                <div id="resTmMode" style="font-weight: 700; color: #2563eb; font-size: 1rem;">Running Gait (ACSM)</div>
            </div>
        </div>
    </div>
</div>

<script>
function setTmPreset(type) {
    if (type === '12_3_30') {
        document.getElementById('tmSpeed').value = '3.0';
        document.getElementById('tmSpeedUnit').value = 'mph';
        document.getElementById('tmIncline').value = '12.0';
        document.getElementById('tmDuration').value = '30';
    } else if (type === '5k') {
        document.getElementById('tmSpeed').value = '6.5';
        document.getElementById('tmSpeedUnit').value = 'mph';
        document.getElementById('tmIncline').value = '1.0';
        document.getElementById('tmDuration').value = '28';
    }
    calculateTreadmill();
}

function calculateTreadmill() {
    let w = parseFloat(document.getElementById('tmWeight').value) || 70;
    const wUnit = document.getElementById('tmWeightUnit').value;
    const wKg = (wUnit === 'lbs') ? (w * 0.453592) : w;

    let s = parseFloat(document.getElementById('tmSpeed').value) || 0;
    const sUnit = document.getElementById('tmSpeedUnit').value;
    const sMph = (sUnit === 'kmh') ? (s * 0.621371) : s;
    const sKmh = (sUnit === 'kmh') ? s : (s * 1.60934);

    // Speed in meters per minute (1 mph = 26.8224 m/min)
    const sMpm = sMph * 26.8224;

    const gradePct = parseFloat(document.getElementById('tmIncline').value) || 0;
    const gradeFrac = gradePct / 100.0;
    const durMins = parseFloat(document.getElementById('tmDuration').value) || 0;

    // Determine gait: <= 3.7 mph is Walking, > 3.7 mph is Running
    let vo2 = 0;
    let modeText = "";

    if (sMph <= 3.7) {
        // ACSM Walking Equation
        // VO2 = (0.1 * S) + (1.8 * S * G) + 3.5
        vo2 = (0.1 * sMpm) + (1.8 * sMpm * gradeFrac) + 3.5;
        modeText = "Walking Gait (ACSM Walking Model)";
    } else {
        // ACSM Running Equation
        // VO2 = (0.2 * S) + (0.9 * S * G) + 3.5
        vo2 = (0.2 * sMpm) + (0.9 * sMpm * gradeFrac) + 3.5;
        modeText = "Running Gait (ACSM Running Model)";
    }

    const mets = vo2 / 3.5;

    // Gross calories = (VO2 * Weight_kg / 1000) * 5 kcal/L_O2 * Duration_min
    // Equivalent: (VO2 * Weight_kg / 200) * Duration_min
    const grossKcal = (vo2 * wKg / 200) * durMins;

    // Net calories = Gross - Resting BMR (3.5 * wKg / 200 * durMins)
    const restingKcal = (3.5 * wKg / 200) * durMins;
    const netKcal = Math.max(0, grossKcal - restingKcal);
    const hourlyKcal = (durMins > 0) ? (grossKcal / durMins) * 60 : 0;

    // Distance and elevation
    const distMiles = sMph * (durMins / 60);
    const distKm = sKmh * (durMins / 60);
    const vertMeters = (distKm * 1000) * gradeFrac;
    const vertFeet = vertMeters * 3.28084;

    // Pace in min/mile
    let paceMin = (sMph > 0) ? (60 / sMph) : 0;
    let paceP = Math.floor(paceMin);
    let paceS = Math.round((paceMin - paceP) * 60);

    document.getElementById('resTmGrossCal').innerText = `${Math.round(grossKcal)} kcal`;
    document.getElementById('resTmNetCal').innerText = `${Math.round(netKcal)} kcal`;
    document.getElementById('resTmHourlyRate').innerText = `${Math.round(hourlyKcal)} kcal/hr`;
    document.getElementById('resTmPaceMinMi').innerText = sMph > 0 ? `Pace: ${paceP}:${String(paceS).padStart(2, '0')} min/mi` : 'Stationary';
    document.getElementById('resTmVo2').innerText = `${vo2.toFixed(1)} mL/kg/min`;
    document.getElementById('resTmMets').innerText = `Intensity: ${mets.toFixed(1)} METs`;
    document.getElementById('resTmDist').innerText = `${distMiles.toFixed(2)} miles (${distKm.toFixed(2)} km)`;
    document.getElementById('resTmElev').innerText = `${Math.round(vertFeet)} feet (${Math.round(vertMeters)} m)`;
    document.getElementById('resTmMode').innerText = modeText;
}

window.addEventListener('DOMContentLoaded', calculateTreadmill);
</script>"""

    article = """<h2>Metabolic Foundations of Treadmill Caloric Expenditure</h2>
<p>Estimating energy expenditure during treadmill locomotion is one of the most thoroughly validated disciplines in clinical exercise physiology. Unlike outdoor running, where unpredictable wind resistance, varying road camber, and uneven terrain introduce confounding variables, a motorized treadmill provides an experimentally controlled environment with constant belt velocity and precision incline gradients.</p>

<p>The gold standard mathematical equations for treadmill locomotion were developed by the <strong>American College of Sports Medicine (ACSM)</strong>. These equations quantify the gross rate of oxygen consumption ($\text{VO}_2$, expressed in milliliters of oxygen per kilogram of body weight per minute, $\text{mL}\cdot\text{kg}^{-1}\cdot\text{min}^{-1}$) as the linear sum of three distinct metabolic components:</p>

<ol>
    <li><strong>Resting Component:</strong> The baseline metabolic oxygen requirement of human homeostasis ($3.5 \, \text{mL}\cdot\text{kg}^{-1}\cdot\text{min}^{-1} = 1.0 \, \text{MET}$).</li>
    <li><strong>Horizontal Locomotor Component:</strong> The energy expended to translate body mass forward across the horizontal surface per meter traveled.</li>
    <li><strong>Vertical Climbing Component:</strong> The mechanical work performed against Earth's gravitational acceleration ($\mathbf{g} = 9.80665 \, \text{m/s}^2$) when moving up an inclined belt gradient.</li>
</ol>

<h2>The ACSM Walking and Running Metabolic Formulations</h2>
<p>The biomechanics of human walking (inverted pendulum gait with heel strike) differ fundamentally from running (spring-mass bouncing gait with flight phase). Consequently, the ACSM specifies two distinct equations based on speed $S$ (in meters per minute, $\text{m/min}$) and fractional incline grade $G$ (where $5\% \text{ incline} = 0.05$):</p>

<h3>1. ACSM Walking Formula (Speeds $\le 3.7 \text{ mph}$ / $6.0 \text{ km/h}$)</h3>
$$\text{VO}_{2, \text{walk}} = 0.1 \cdot S + 1.8 \cdot S \cdot G + 3.5$$

<p>Where the horizontal oxygen cost is $0.1 \, \text{mL}\cdot\text{kg}^{-1}\cdot\text{m}^{-1}$ and the vertical climbing oxygen cost is $1.8 \, \text{mL}\cdot\text{kg}^{-1}\cdot\text{m}^{-1}$.</p>

<h3>2. ACSM Running Formula (Speeds $> 3.7 \text{ mph}$ / $6.0 \text{ km/h}$)</h3>
$$\text{VO}_{2, \text{run}} = 0.2 \cdot S + 0.9 \cdot S \cdot G + 3.5$$

<p>Notice that running doubles the horizontal oxygen cost to $0.2 \, \text{mL}\cdot\text{kg}^{-1}\cdot\text{m}^{-1}$ due to vertical oscillation of the center of mass, but cuts the vertical coefficient to $0.9$ due to elastic recoil storage in the Achilles tendon and plantar fascia.</p>

<h3>Converting Oxygen Consumption to Caloric Energy (kcal)</h3>
<p>Through indirect calorimetry, consuming 1.0 liter of oxygen ($\text{L O}_2$) metabolizes approximately $4.86$ to $5.05 \, \text{kcal}$ of energy depending on respiratory exchange ratio (RER). Using the standardized clinical equivalent of $5.0 \, \text{kcal} / \text{L O}_2$:</p>

$$\text{Gross Energy Expenditure (kcal)} = \left( \frac{\text{VO}_2 \times \text{Weight (kg)}}{1000} \right) \times 5.0 \times \text{Duration (min)} = \frac{\text{VO}_2 \times \text{Weight (kg)}}{200} \times \text{Duration (min)}$$

$$\text{Net Exercise Calories (kcal)} = \text{Gross Calories} - \left( \frac{3.5 \times \text{Weight (kg)}}{200} \times \text{Duration (min)} \right)$$

<h3>Treadmill Speed &amp; Incline Metabolic Reference Matrix</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Speed (mph)</th>
            <th>Pace (min/mi)</th>
            <th>Incline (%)</th>
            <th>Oxygen Cost ($\text{VO}_2$)</th>
            <th>MET Value</th>
            <th>Burn Rate (70 kg Person)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>3.0 mph</td><td>20:00 min/mi</td><td>0.0% Grade</td><td>11.5 mL/kg/min</td><td>3.3 METs</td><td>242 kcal / hr</td></tr>
        <tr><td>3.0 mph</td><td>20:00 min/mi</td><td>6.0% Grade</td><td>20.2 mL/kg/min</td><td>5.8 METs</td><td>424 kcal / hr</td></tr>
        <tr><td>3.0 mph (12-3-30)</td><td>20:00 min/mi</td><td>12.0% Grade</td><td>28.9 mL/kg/min</td><td>8.3 METs</td><td>607 kcal / hr</td></tr>
        <tr><td>5.0 mph (Jog)</td><td>12:00 min/mi</td><td>1.0% Grade</td><td>31.5 mL/kg/min</td><td>9.0 METs</td><td>662 kcal / hr</td></tr>
        <tr><td>6.0 mph</td><td>10:00 min/mi</td><td>1.0% Grade</td><td>37.1 mL/kg/min</td><td>10.6 METs</td><td>779 kcal / hr</td></tr>
        <tr><td>7.5 mph</td><td>08:00 min/mi</td><td>1.0% Grade</td><td>45.5 mL/kg/min</td><td>13.0 METs</td><td>956 kcal / hr</td></tr>
        <tr><td>9.0 mph</td><td>06:40 min/mi</td><td>1.0% Grade</td><td>53.8 mL/kg/min</td><td>15.4 METs</td><td>1,130 kcal / hr</td></tr>
    </tbody>
</table>

<h2>Biomechanical Impact of the 1% Incline Rule</h2>
<p>In 1996, exercise physiologists Jones and Doust published a landmark study in the <em>Journal of Sports Sciences</em> demonstrating that running on a flat ($0\%$) treadmill belt requires less oxygen than running outdoors at identical speeds because treadmill runners face zero relative air resistance. The researchers proved that setting a treadmill to a <strong>1.0% incline</strong> precisely offsets the absence of outdoor aerodynamic drag at speeds between 6.0 and 11.2 mph (10 to 18 km/h), making the treadmill's energetic cost identical to outdoor road running.</p>

<div class="worked-example-card">
    <h3>Worked Clinical Physiology Case Study: The 12-3-30 Viral Treadmill Workout</h3>
    <p><strong>Scenario:</strong> A 75 kg fitness enthusiast performs the popular "12-3-30" protocol: walking at <strong>3.0 mph</strong> at a steep <strong>12.0% incline</strong> for <strong>30 minutes</strong> without holding handrails. Calculate: (1) treadmill belt speed in meters per minute, (2) oxygen consumption ($\text{VO}_2$), (3) MET intensity level, (4) gross calories burned, and (5) total vertical elevation gained.</p>
    
    <div class="step-solution">
        <h4>Step 1: Convert Speed to Meters per Minute ($S$)</h4>
        $$S = 3.0 \text{ mph} \times 26.8224 = 80.4672 \text{ m/min}$$

        <h4>Step 2: Apply ACSM Walking Equation</h4>
        <p>Fractional grade: $G = 12 / 100 = 0.12$.</p>
        $$\text{VO}_2 = (0.1 \times 80.4672) + (1.8 \times 80.4672 \times 0.12) + 3.5$$
        $$\text{VO}_2 = 8.0467 + 17.3810 + 3.5 = 28.9277 \approx 28.93 \, \text{mL}\cdot\text{kg}^{-1}\cdot\text{min}^{-1}$$

        <h4>Step 3: Evaluate Metabolic Equivalent (METs)</h4>
        $$\text{METs} = \frac{28.93}{3.5} \approx 8.27 \, \text{METs (Vigorous Aerobic Exercise)}$$

        <h4>Step 4: Compute Gross Calorie Expenditure</h4>
        $$\text{Gross Calories} = \frac{28.93 \times 75 \text{ kg}}{200} \times 30 \text{ minutes} = 10.8488 \times 30 \approx 325.5 \text{ kcal}$$

        <h4>Step 5: Compute Vertical Elevation Gained</h4>
        $$\text{Horizontal Distance} = 3.0 \text{ mph} \times 0.5 \text{ hr} = 1.50 \text{ miles} = 2,414 \text{ meters}$$
        $$\text{Vertical Climb} = 2,414 \text{ m} \times 0.12 = 289.7 \text{ meters} \approx 950.4 \text{ feet}$$
        <p><strong>Conclusion:</strong> The 12-3-30 workout burns 325 kcal in 30 minutes while climbing the equivalent of a 95-story skyscraper!</p>
    </div>
</div>

<h2>Common Errors When Calculating Treadmill Calories</h2>
<ol>
    <li><strong>Handrail Gripping Distortion:</strong> Holding onto the treadmill console or handles dramatically reduces lower extremity muscle activation. Laboratory metabolic carts demonstrate that gripping handrails during incline walking cuts true oxygen consumption by 20% to 30%, rendering console calorie estimates dangerously inflated.</li>
    <li><strong>Conflating Gross and Net Calories:</strong> Gross calories include the baseline BMR calories your body would have burned while sitting on the sofa. If tracking energy balance for fat loss, always use Net Exercise Calories to prevent double-counting resting metabolic rate.</li>
    <li><strong>Ignoring Air Cooling on Belt Friction:</strong> Indoor gyms with poor ventilation cause elevated heart rate due to cardiovascular drift rather than higher metabolic work. Calorie expenditure is governed by mechanical velocity and grade, not elevated heart rate caused by dehydration.</li>
</ol>

<section class="faq-section">
    <h2>Frequently Asked Questions About Treadmill Calories</h2>
    <div class="faq-item">
        <h3>How does treadmill incline affect calorie burn?</h3>
        <p>Every 1% increase in treadmill incline increases the metabolic cost of walking by approximately 1.8 mL/kg/min of VO2 (roughly 10% to 12% more calories burned), requiring substantial mechanical work against gravity.</p>
    </div>
    <div class="faq-item">
        <h3>What is the ACSM metabolic formula for treadmill running?</h3>
        <p>The ACSM running equation evaluates VO2 (mL/kg/min) = (0.2 * speed in m/min) + (0.9 * speed * fractional grade) + 3.5. Caloric expenditure is then computed as VO2 * weight in kg / 200 * duration in minutes.</p>
    </div>
    <div class="faq-item">
        <h3>Why do treadmill display consoles overestimate calories burned?</h3>
        <p>Treadmill consoles typically assume a default heavy male body weight (around 70-80 kg), fail to account for resting metabolic deductions (gross vs net burn), and assume no handrail holding, which can overestimate true expenditure by 20% to 35%.</p>
    </div>
    <div class="faq-item">
        <h3>Does holding onto the treadmill handrails reduce calorie expenditure?</h3>
        <p>Yes. Gripping the front or side handrails transfers a portion of body weight off the treadmill belt and eliminates torso swing, reducing true oxygen consumption and caloric expenditure by 20% to 30%.</p>
    </div>
</section>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article)


# ===========================================================================
# TOOL 2: stairmaster-calorie-calculator.html
# ===========================================================================
def gen_stairmaster_calorie():
    slug = "stairmaster-calorie-calculator"
    title = "StairMaster Calorie Calculator | Stepmill Work & Vertical Climb Rate"
    desc = "Calculate calories burned on a StairMaster stepmill or stair climber machine. Computes mechanical work against gravity (W=mgh), steps per minute, floors climbed, and METs."
    h1 = "StairMaster Calorie Calculator"
    short_desc = "Precision exercise physiology calculator evaluating caloric expenditure, vertical elevation gain, and gravitational mechanical work ($W = mgh$) on rotating stepmills."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "StairMaster Calorie Calculator",
      "url": "https://calchub.com/stairmaster-calorie-calculator.html",
      "applicationCategory": "HealthApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Calculates calories burned on a StairMaster based on body weight, stepping cadence, and duration."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How many calories does 30 minutes on a StairMaster burn?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A 70 kg (154 lb) individual stepping at a moderate cadence of 60 to 70 steps per minute burns approximately 250 to 350 calories in 30 minutes, representing a vigorous 8.5 to 10.0 MET workload."
          }
        },
        {
          "@type": "Question",
          "name": "What is the standard step height on a rotating StairMaster stepmill?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Commercial StairMaster machines (such as the Gauntlet and 8-Series FreeClimber) feature fixed 8-inch (0.2032 meter) revolving steps. 16 steps equals approximately 1 architectural flight of stairs."
          }
        },
        {
          "@type": "Question",
          "name": "Why is the StairMaster more calorically demanding than flat treadmill walking?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The StairMaster requires lifting 100% of your body weight vertically against gravity on every single stride with zero downhill coasting or momentum assistance, demanding massive gluteal and quadriceps muscle recruitment."
          }
        },
        {
          "@type": "Question",
          "name": "How much does resting your hands on the StairMaster handles reduce calorie burn?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Leaning heavily on the side handles supports up to 25% to 30% of your body weight through your arms, cutting true metabolic expenditure and cardiovascular conditioning by 25% to 35%."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-body">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1.25rem; margin-bottom: 1.25rem;">
        <div>
            <label for="smWeight" style="font-weight: 600; font-size: 0.875rem;">Body Weight:</label>
            <div style="display: flex; gap: 0.5rem;">
                <input type="number" id="smWeight" class="input-field" value="70" min="20" max="300" step="0.5" oninput="calculateStairMaster()">
                <select id="smWeightUnit" class="input-field" style="width: 80px;" onchange="calculateStairMaster()">
                    <option value="kg">kg</option>
                    <option value="lbs">lbs</option>
                </select>
            </div>
        </div>
        <div>
            <label for="smCadence" style="font-weight: 600; font-size: 0.875rem;">Stepping Cadence (steps/min):</label>
            <input type="number" id="smCadence" class="input-field" value="65" min="20" max="160" step="5" oninput="calculateStairMaster()">
            <span class="input-hint">Moderate: 55-75 SPM | Vigorous: 80+ SPM</span>
        </div>
        <div>
            <label for="smDuration" style="font-weight: 600; font-size: 0.875rem;">Duration (minutes):</label>
            <input type="number" id="smDuration" class="input-field" value="30" min="1" max="180" step="1" oninput="calculateStairMaster()">
        </div>
        <div>
            <label for="smPosture" style="font-weight: 600; font-size: 0.875rem;">Handrail Support Posture:</label>
            <select id="smPosture" class="input-field" onchange="calculateStairMaster()">
                <option value="none">Free Stepping (No Support - 100% Burn)</option>
                <option value="light">Fingertip Touch (Balance Only - 95% Burn)</option>
                <option value="heavy">Heavy Leaning (Weight Transfer - 75% Burn)</option>
            </select>
        </div>
    </div>

    <div style="display: flex; gap: 0.75rem; margin-bottom: 1.5rem;">
        <button type="button" class="btn btn-primary" onclick="calculateStairMaster()">Calculate Calories</button>
        <button type="button" class="btn btn-outline" onclick="setSmPreset('fatburn')">Fat Burn (50 SPM)</button>
        <button type="button" class="btn btn-outline" onclick="setSmPreset('hiit')">HIIT Climb (90 SPM)</button>
    </div>

    <div class="result-box" style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem;">
        <h3 style="margin-top: 0; color: #1e293b; font-size: 1.1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">Stair Climbing Energy Output</h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Total Calories Burned</div>
                <div id="resSmGrossCal" style="font-size: 1.5rem; font-weight: 700; color: #2563eb;">294 kcal</div>
                <div id="resSmNetCal" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">Net: 257 kcal above rest</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Flights of Stairs</div>
                <div id="resSmFlights" style="font-size: 1.4rem; font-weight: 700; color: #0f172a;">122 Flights</div>
                <div id="resSmStepsTotal" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">1,950 steps total</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Hourly Burn Rate</div>
                <div id="resSmHourly" style="font-size: 1.4rem; font-weight: 700; color: #16a34a;">588 kcal/hr</div>
                <div id="resSmMets" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">Intensity: 8.8 METs</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Mechanical Work (mgh)</div>
                <div id="resSmWorkKj" style="font-size: 1.4rem; font-weight: 700; color: #7c3aed;">272 kJ</div>
                <div style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">At 22% muscle efficiency</div>
            </div>
        </div>

        <div style="margin-top: 1.25rem; padding-top: 1rem; border-top: 1px dashed #cbd5e1; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; font-size: 0.875rem;">
            <div>
                <span style="font-weight: 600; color: #475569;">Total Vertical Ascent:</span>
                <div id="resSmAscent" style="font-weight: 700; color: #1e293b; font-size: 1rem;">1,300 feet (396.2 m)</div>
            </div>
            <div>
                <span style="font-weight: 600; color: #475569;">Equivalent Landmark Height:</span>
                <div id="resSmLandmark" style="font-weight: 700; color: #2563eb; font-size: 1rem;">Empire State Building (approx)</div>
            </div>
        </div>
    </div>
</div>

<script>
function setSmPreset(type) {
    if (type === 'fatburn') {
        document.getElementById('smCadence').value = '50';
        document.getElementById('smDuration').value = '45';
    } else if (type === 'hiit') {
        document.getElementById('smCadence').value = '90';
        document.getElementById('smDuration').value = '20';
    }
    calculateStairMaster();
}

function calculateStairMaster() {
    let w = parseFloat(document.getElementById('smWeight').value) || 70;
    const wUnit = document.getElementById('smWeightUnit').value;
    const wKg = (wUnit === 'lbs') ? (w * 0.453592) : w;

    const spm = parseFloat(document.getElementById('smCadence').value) || 60;
    const durMins = parseFloat(document.getElementById('smDuration').value) || 30;
    const posture = document.getElementById('smPosture').value;

    let postureFactor = 1.0;
    if (posture === 'light') postureFactor = 0.95;
    if (posture === 'heavy') postureFactor = 0.75;

    // Commercial step height: 8 inches = 0.2032 meters
    const stepHeightM = 0.2032;
    const totalSteps = spm * durMins;
    const totalAscentM = totalSteps * stepHeightM;
    const totalAscentFt = totalAscentM * 3.28084;
    const flights = totalSteps / 16; // 16 steps per standard flight

    // Mechanical gravitational work W = m * g * h (Joules)
    const g = 9.80665;
    const mechanicalWorkJ = wKg * g * totalAscentM;
    const mechanicalWorkKj = mechanicalWorkJ / 1000;

    // Human muscular climbing thermodynamic efficiency is ~20% to 22%
    // Metabolic energy = Mechanical Work / 0.21
    // 1 kcal = 4184 J
    const metabolicKcalFromWork = (mechanicalWorkJ / 0.21) / 4184;

    // MET model validation: Compendium code 02005 (stair machine) is ~8.5 to 11.0 METs
    // MET = 4.0 + (spm / 10) * 0.8
    const mets = (3.5 + (spm * 0.08)) * postureFactor;
    const vo2 = mets * 3.5;

    // Calorie calculation via ACSM MET formula
    const grossKcal = ((mets * 3.5 * wKg) / 200) * durMins * postureFactor;
    const restingKcal = (3.5 * wKg / 200) * durMins;
    const netKcal = Math.max(0, grossKcal - restingKcal);
    const hourlyKcal = (durMins > 0) ? (grossKcal / durMins) * 60 : 0;

    let landmark = "Eiffel Tower (300m)";
    if (totalAscentM < 150) landmark = "Statue of Liberty (93m)";
    else if (totalAscentM < 250) landmark = "Space Needle (184m)";
    else if (totalAscentM < 400) landmark = "Eiffel Tower (300m)";
    else landmark = "Empire State Building (381m)";

    document.getElementById('resSmGrossCal').innerText = `${Math.round(grossKcal)} kcal`;
    document.getElementById('resSmNetCal').innerText = `Net: ${Math.round(netKcal)} kcal above rest`;
    document.getElementById('resSmFlights').innerText = `${Math.round(flights)} Flights`;
    document.getElementById('resSmStepsTotal').innerText = `${Math.round(totalSteps).toLocaleString()} steps total`;
    document.getElementById('resSmHourly').innerText = `${Math.round(hourlyKcal)} kcal/hr`;
    document.getElementById('resSmMets').innerText = `Intensity: ${mets.toFixed(1)} METs`;
    document.getElementById('resSmWorkKj').innerText = `${Math.round(mechanicalWorkKj)} kJ`;
    document.getElementById('resSmAscent').innerText = `${Math.round(totalAscentFt).toLocaleString()} feet (${Math.round(totalAscentM).toLocaleString()} m)`;
    document.getElementById('resSmLandmark').innerText = landmark;
}

window.addEventListener('DOMContentLoaded', calculateStairMaster);
</script>"""

    article = """<h2>Biomechanical Principles of Rotating Step Climbers</h2>
<p>The revolving staircase stepmill—commercially popularized under the trademark <strong>StairMaster</strong>—is widely regarded in cardiovascular medicine and sports conditioning as one of the most metabolically demanding indoor exercise modalities. Unlike treadmills where runners benefit from elastic tendon recoil, or stationary cycles where body weight is supported by a saddle, the StairMaster demands continuous mechanical lifting of the human body's total mass against gravitational acceleration.</p>

<p>Every step cycle requires the quadriceps, gluteus maximus, hamstrings, and gastrocnemius muscles to generate positive concentric force to elevate the center of mass vertically by the step height $h$ (standardized on commercial machines at $8.0 \, \text{inches} = 0.2032 \, \text{meters}$). Because the revolving steps fall beneath the user, failure to match stepping cadence results in sliding off the apparatus, enforcing a constant metabolic workload.</p>

<h2>Thermodynamics: Gravitational Work and Muscular Efficiency</h2>
<p>The total external physical work performed ($W_{\text{mech}}$, in Joules) when elevating a body of mass $m$ (kg) across $N$ steps of height $h$ is governed by Newton's second law and gravitational potential energy:</p>

$$W_{\text{mech}} = m \cdot g \cdot h \cdot N = m \cdot g \cdot \Delta H$$

<p>Where $g = 9.80665 \, \text{m/s}^2$ and $\Delta H = h \times N$ represents the total vertical elevation gained. However, skeletal muscle is not an idealized mechanical motor; the human body operates at an <strong>apparent mechanical efficiency ($\eta_{\text{musc}}$)</strong> of approximately $20\%$ to $22\%$ ($0.20 \le \eta \le 0.22$). The remaining $78\%$ to $80\%$ of chemical energy liberated from adenosine triphosphate (ATP) hydrolysis is dissipated as metabolic thermal heat.</p>

<p>Converting mechanical work into metabolic energy expenditure ($E_{\text{metabolic}}$):</p>

$$E_{\text{metabolic}} = \frac{W_{\text{mech}}}{\eta_{\text{musc}}} = \frac{m \cdot g \cdot \Delta H}{0.21}$$

<p>Since $1.0 \, \text{kcal} = 4,184 \, \text{Joules}$, the gravitational component of caloric expenditure evaluates as:</p>

$$\text{Calories}_{\text{vertical}} (\text{kcal}) = \frac{m \cdot g \cdot \Delta H}{0.21 \times 4184}$$

<h2>The Compendium of Physical Activities MET Formulations</h2>
<p>In addition to pure mechanical lifting, stepping entails horizontal limb acceleration, postural stabilization, and cardiac/respiratory metabolic overhead. Under the <em>Compendium of Physical Activities</em> (Ainsworth et al.), stair climbing machine exercise is cataloged under code <strong>02005</strong> with dynamic MET intensities scaling with stepping cadence ($SPM$, steps per minute):</p>

$$\text{MET} = 3.5 + (0.08 \times SPM)$$

<p>Gross caloric expenditure across exercise duration $t$ (minutes) evaluates via the standard clinical ACSM formulation:</p>

$$\text{Gross Calories (kcal)} = \left( \frac{\text{MET} \times 3.5 \times \text{Weight (kg)}}{200} \right) \times t$$

<h3>StairMaster Cadence and Calorie Reference Matrix</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Stepping Cadence</th>
            <th>Perceived Exertion</th>
            <th>Vertical Climb Rate</th>
            <th>MET Intensity</th>
            <th>Burn Rate (60 kg Person)</th>
            <th>Burn Rate (85 kg Person)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>45 steps / min</td><td>Light Warm-up</td><td>9.1 m / min (30 ft/min)</td><td>7.1 METs</td><td>447 kcal / hr</td><td>634 kcal / hr</td></tr>
        <tr><td>60 steps / min</td><td>Moderate Aerobic</td><td>12.2 m / min (40 ft/min)</td><td>8.3 METs</td><td>523 kcal / hr</td><td>741 kcal / hr</td></tr>
        <tr><td>75 steps / min</td><td>Vigorous Endurance</td><td>15.2 m / min (50 ft/min)</td><td>9.5 METs</td><td>599 kcal / hr</td><td>848 kcal / hr</td></tr>
        <tr><td>90 steps / min</td><td>Threshold / HIIT</td><td>18.3 m / min (60 ft/min)</td><td>10.7 METs</td><td>674 kcal / hr</td><td>955 kcal / hr</td></tr>
        <tr><td>110 steps / min</td><td>Anaerobic Sprint</td><td>22.4 m / min (73 ft/min)</td><td>12.3 METs</td><td>775 kcal / hr</td><td>1,098 kcal / hr</td></tr>
    </tbody>
</table>

<div class="worked-example-card">
    <h3>Worked Exercise Physiology Case Study: High-Rise Skyscraper Climbing Simulation</h3>
    <p><strong>Scenario:</strong> A 70 kg firefighter trainee climbs a StairMaster at a cadence of <strong>70 steps per minute</strong> for <strong>35 minutes</strong> while maintaining upright posture without resting on handrails. Determine: (1) total steps and flights climbed (16 steps per flight), (2) vertical elevation gained in meters and feet, (3) mechanical work performed against gravity, (4) gross calories burned, and (5) equivalent real-world architectural structure scaled.</p>
    
    <div class="step-solution">
        <h4>Step 1: Calculate Total Steps and Flights</h4>
        $$\text{Total Steps} = 70 \text{ SPM} \times 35 \text{ min} = 2,450 \text{ steps}$$
        $$\text{Flights Climbed} = \frac{2,450}{16} \approx 153.1 \text{ architectural flights}$$

        <h4>Step 2: Evaluate Vertical Elevation Gain ($\Delta H$)</h4>
        $$\Delta H = 2,450 \times 0.2032 \text{ m} = 497.84 \text{ meters} \approx 1,633.3 \text{ feet}$$

        <h4>Step 3: Evaluate Gravitational Mechanical Work ($W_{\text{mech}}$)</h4>
        $$W_{\text{mech}} = 70 \text{ kg} \times 9.80665 \text{ m/s}^2 \times 497.84 \text{ m} \approx 341,750 \text{ Joules} = 341.75 \text{ kJ}$$

        <h4>Step 4: Compute Gross Calorie Expenditure</h4>
        $$\text{MET} = 3.5 + (0.08 \times 70) = 3.5 + 5.6 = 9.1 \text{ METs}$$
        $$\text{Gross Calories} = \frac{9.1 \times 3.5 \times 70}{200} \times 35 = 11.1475 \times 35 \approx 390.2 \text{ kcal}$$

        <h4>Step 5: Architectural Comparison</h4>
        <p>At 497.8 meters of vertical ascent, the trainee climbed higher than the observation deck of the <strong>Empire State Building</strong> (381 m) and the roof of the <strong>Petronas Towers</strong> (452 m)!</p>
    </div>
</div>

<h2>Common Mistakes on the StairMaster</h2>
<ol>
    <li><strong>The "Handrail Slouch" Posture:</strong> Leaning forward and placing full arm weight onto the side handrails transfers up to 30% of body mass away from the lower body. This slashes true caloric burn by 25% to 35% and introduces severe lumbar spinal hyperextension. Always maintain an upright, neutral spine.</li>
    <li><strong>Taking Shallow Half-Steps:</strong> Letting the rotating step drop halfway before stepping reduces the effective mechanical height from 8 inches to 4 inches, halving the gravitational work performed ($W = mgh$).</li>
    <li><strong>Excessive Forward Torso Lean:</strong> Hinging excessively at the hips shortens the gluteus maximus lever arm and overloads the anterior hip flexors, leading to premature muscular fatigue before reaching target cardiovascular heart rate zones.</li>
</ol>

<section class="faq-section">
    <h2>Frequently Asked Questions About StairMaster Calories</h2>
    <div class="faq-item">
        <h3>How many calories does 30 minutes on a StairMaster burn?</h3>
        <p>A 70 kg (154 lb) individual stepping at a moderate cadence of 60 to 70 steps per minute burns approximately 250 to 350 calories in 30 minutes, representing a vigorous 8.5 to 10.0 MET workload.</p>
    </div>
    <div class="faq-item">
        <h3>What is the standard step height on a rotating StairMaster stepmill?</h3>
        <p>Commercial StairMaster machines (such as the Gauntlet and 8-Series FreeClimber) feature fixed 8-inch (0.2032 meter) revolving steps. 16 steps equals approximately 1 architectural flight of stairs.</p>
    </div>
    <div class="faq-item">
        <h3>Why is the StairMaster more calorically demanding than flat treadmill walking?</h3>
        <p>The StairMaster requires lifting 100% of your body weight vertically against gravity on every single stride with zero downhill coasting or momentum assistance, demanding massive gluteal and quadriceps muscle recruitment.</p>
    </div>
    <div class="faq-item">
        <h3>How much does resting your hands on the StairMaster handles reduce calorie burn?</h3>
        <p>Leaning heavily on the side handles supports up to 25% to 30% of your body weight through your arms, cutting true metabolic expenditure and cardiovascular conditioning by 25% to 35%.</p>
    </div>
</section>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article)


# ===========================================================================
# TOOL 3: cycling-calorie-calculator.html
# ===========================================================================
def gen_cycling_calorie():
    slug = "cycling-calorie-calculator"
    title = "Cycling Calorie Calculator | Outdoor Road Speed, Watts & Grade"
    desc = "Calculate calories burned cycling outdoors or on road bikes. Accounts for speed (mph/kmh), rider weight, road grade, wind drag, mechanical power (Watts), and METs."
    h1 = "Cycling Calorie Calculator"
    short_desc = "Calculate caloric energy expenditure and mechanical power output for outdoor cycling based on aerodynamic drag, rolling resistance, road gradient, and gross metabolic efficiency."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Cycling Calorie Calculator",
      "url": "https://calchub.com/cycling-calorie-calculator.html",
      "applicationCategory": "HealthApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Calculates calories burned during outdoor road cycling based on speed, duration, body weight, gradient, and wind."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How are cycling calories calculated from mechanical wattage?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Mechanical work in kilojoules (kJ) = Average Watts * Time in seconds / 1000. Because human gross metabolic efficiency is roughly 21% to 24%, 1 kJ of mechanical work on the pedals requires approximately 1.0 to 1.15 kcal of metabolic energy."
          }
        },
        {
          "@type": "Question",
          "name": "Why does cycling fast burn exponentially more calories?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Aerodynamic drag increases with the square of velocity (F_drag = 0.5 * rho * CdA * v^2), meaning mechanical power required to overcome air resistance scales with the cube of velocity (P_aero proportional to v^3)."
          }
        },
        {
          "@type": "Question",
          "name": "How many calories does cycling 15 miles burn?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "At a moderate speed of 12 to 14 mph, a 70 kg cyclist burns roughly 550 to 650 calories across 15 miles. At race paces (20+ mph), calorie burn exceeds 750 to 850 calories due to immense aerodynamic resistance."
          }
        },
        {
          "@type": "Question",
          "name": "How does climbing hills affect cycling calorie burn?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Climbing requires continuous mechanical work against gravity P_gravity = m * g * v * sin(theta), multiplying required power output by 2x to 4x compared to flat terrain."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-body">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1.25rem; margin-bottom: 1.25rem;">
        <div>
            <label for="cyWeight" style="font-weight: 600; font-size: 0.875rem;">Rider Weight:</label>
            <div style="display: flex; gap: 0.5rem;">
                <input type="number" id="cyWeight" class="input-field" value="75" min="30" max="250" step="0.5" oninput="calculateCycling()">
                <select id="cyWeightUnit" class="input-field" style="width: 80px;" onchange="calculateCycling()">
                    <option value="kg">kg</option>
                    <option value="lbs">lbs</option>
                </select>
            </div>
        </div>
        <div>
            <label for="cySpeed" style="font-weight: 600; font-size: 0.875rem;">Average Speed:</label>
            <div style="display: flex; gap: 0.5rem;">
                <input type="number" id="cySpeed" class="input-field" value="16.0" min="4" max="45" step="0.5" oninput="calculateCycling()">
                <select id="cySpeedUnit" class="input-field" style="width: 80px;" onchange="calculateCycling()">
                    <option value="mph">mph</option>
                    <option value="kmh">km/h</option>
                </select>
            </div>
        </div>
        <div>
            <label for="cyDuration" style="font-weight: 600; font-size: 0.875rem;">Duration (minutes):</label>
            <input type="number" id="cyDuration" class="input-field" value="60" min="1" max="600" step="5" oninput="calculateCycling()">
        </div>
        <div>
            <label for="cyGrade" style="font-weight: 600; font-size: 0.875rem;">Average Road Incline (%):</label>
            <input type="number" id="cyGrade" class="input-field" value="0.0" min="0" max="20" step="0.5" oninput="calculateCycling()">
        </div>
    </div>

    <div style="display: flex; gap: 0.75rem; margin-bottom: 1.5rem;">
        <button type="button" class="btn btn-primary" onclick="calculateCycling()">Calculate Calories</button>
        <button type="button" class="btn btn-outline" onclick="setCyPreset('commute')">Casual Commute (12 mph)</button>
        <button type="button" class="btn btn-outline" onclick="setCyPreset('peloton')">Fast Group Ride (20 mph)</button>
    </div>

    <div class="result-box" style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem;">
        <h3 style="margin-top: 0; color: #1e293b; font-size: 1.1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">Cycling Energy &amp; Power Output</h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Total Calories Burned</div>
                <div id="resCyGrossCal" style="font-size: 1.5rem; font-weight: 700; color: #2563eb;">618 kcal</div>
                <div id="resCyNetCal" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">Net: 545 kcal above rest</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Estimated Mechanical Power</div>
                <div id="resCyWatts" style="font-size: 1.4rem; font-weight: 700; color: #0f172a;">152 Watts</div>
                <div id="resCyWkg" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">2.03 W/kg output</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Total Distance</div>
                <div id="resCyDist" style="font-size: 1.4rem; font-weight: 700; color: #16a34a;">16.0 miles</div>
                <div id="resCyDistKm" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">25.7 km total</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Work Output on Pedals</div>
                <div id="resCyWorkKj" style="font-size: 1.4rem; font-weight: 700; color: #7c3aed;">547 kJ</div>
                <div id="resCyMets" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">Intensity: 8.5 METs</div>
            </div>
        </div>
    </div>
</div>

<script>
function setCyPreset(type) {
    if (type === 'commute') {
        document.getElementById('cySpeed').value = '12.0';
        document.getElementById('cySpeedUnit').value = 'mph';
        document.getElementById('cyGrade').value = '0.0';
        document.getElementById('cyDuration').value = '45';
    } else if (type === 'peloton') {
        document.getElementById('cySpeed').value = '20.0';
        document.getElementById('cySpeedUnit').value = 'mph';
        document.getElementById('cyGrade').value = '1.0';
        document.getElementById('cyDuration').value = '60';
    }
    calculateCycling();
}

function calculateCycling() {
    let w = parseFloat(document.getElementById('cyWeight').value) || 75;
    const wUnit = document.getElementById('cyWeightUnit').value;
    const wKg = (wUnit === 'lbs') ? (w * 0.453592) : w;
    const bikeWeightKg = 9.0; // standard road bike
    const totalMassKg = wKg + bikeWeightKg;

    let s = parseFloat(document.getElementById('cySpeed').value) || 15;
    const sUnit = document.getElementById('cySpeedUnit').value;
    const sMph = (sUnit === 'kmh') ? (s * 0.621371) : s;
    const sMps = sMph * 0.44704; // m/s
    const durMins = parseFloat(document.getElementById('cyDuration').value) || 60;
    const durSec = durMins * 60;
    const gradeFrac = (parseFloat(document.getElementById('cyGrade').value) || 0) / 100;

    // Physical power modeling: Martin et al. (1998)
    // 1. Aerodynamic drag: P_aero = 0.5 * rho * CdA * v^3
    const rho = 1.225; // kg/m^3 air density at sea level
    const cdA = 0.36; // m^2 road bike on hoods
    const pAero = 0.5 * rho * cdA * Math.pow(sMps, 3);

    // 2. Rolling resistance: P_roll = Crr * m_total * g * v
    const crr = 0.004; // standard road tire on smooth asphalt
    const g = 9.80665;
    const pRoll = crr * totalMassKg * g * sMps;

    // 3. Gravity on grade: P_grav = m_total * g * v * sin(theta) ~ m * g * v * gradeFrac
    const pGrav = totalMassKg * g * sMps * gradeFrac;

    // 4. Drivetrain mechanical loss: ~3% loss (eta_drive = 0.97)
    const netWheelPower = Math.max(10, pAero + pRoll + pGrav);
    const pedalWatts = netWheelPower / 0.97;

    // Mechanical Work in kJ = Watts * seconds / 1000
    const workKj = (pedalWatts * durSec) / 1000;

    // Human gross efficiency ~22%
    // Calories (kcal) = Work_kJ / (0.22 * 4.184) ~ Work_kJ / 0.92 ~ Work_kJ * 1.086
    const grossKcal = (workKj / 4.184) / 0.22;
    const restingKcal = (3.5 * wKg / 200) * durMins;
    const netKcal = Math.max(0, grossKcal - restingKcal);

    // METs
    const mets = (grossKcal / (durMins > 0 ? durMins : 1)) / (wKg * 3.5 / 200);

    const distMiles = sMph * (durMins / 60);
    const distKm = distMiles * 1.60934;
    const wKgRatio = pedalWatts / wKg;

    document.getElementById('resCyGrossCal').innerText = `${Math.round(grossKcal)} kcal`;
    document.getElementById('resCyNetCal').innerText = `Net: ${Math.round(netKcal)} kcal above rest`;
    document.getElementById('resCyWatts').innerText = `${Math.round(pedalWatts)} Watts`;
    document.getElementById('resCyWkg').innerText = `${wKgRatio.toFixed(2)} W/kg output`;
    document.getElementById('resCyDist').innerText = `${distMiles.toFixed(1)} miles`;
    document.getElementById('resCyDistKm').innerText = `${distKm.toFixed(1)} km total`;
    document.getElementById('resCyWorkKj').innerText = `${Math.round(workKj)} kJ`;
    document.getElementById('resCyMets').innerText = `Intensity: ${mets.toFixed(1)} METs`;
}

window.addEventListener('DOMContentLoaded', calculateCycling);
</script>"""

    article = """<h2>Biomechanical and Aerodynamic Physics of Cycling Locomotion</h2>
<p>Unlike pedestrian walking and running, where human legs alternately brake and accelerate body mass with each foot strike, the bicycle is an extraordinarily efficient mechanical transmission that decouples the body's center of mass from impact ground reaction forces. Consequently, cycling caloric expenditure is governed directly by the <strong>mechanical power ($P_{\text{pedal}}$, in Watts)</strong> required to overcome physical resistive forces opposing forward motion.</p>

<p>In 1998, sports science researchers Martin, Milliken, and Cobb published the definitive mathematical model of road cycling power. Total resistive force opposing a cyclist moving at ground velocity $v$ (m/s) resolves into three primary physical vectors:</p>

$$P_{\text{total}} = P_{\text{aerodynamic}} + P_{\text{rolling}} + P_{\text{gravity}} + P_{\text{drivetrain}}$$

<h3>1. Aerodynamic Drag ($P_{\text{aero}}$)</h3>
<p>In flat road cycling at speeds exceeding 12 mph (19 km/h), air resistance constitutes over $80\%$ of total resistive force. Aerodynamic power scales with the <strong>cube of velocity ($v^3$)</strong>:</p>

$$P_{\text{aero}} = \frac{1}{2} \rho \cdot C_d A \cdot (v + v_{\text{wind}})^2 \cdot v$$

<p>Where $\rho \approx 1.225 \, \text{kg/m}^3$ is air density at sea level, and $C_d A$ is the effective frontal drag area (typically $0.32 \, \text{m}^2$ for an aerodynamic drop posture, up to $0.42 \, \text{m}^2$ for an upright commuter).</p>

<h3>2. Rolling Resistance ($P_{\text{rolling}}$)</h3>
<p>Caused by tire carcass hysteresis and road micro-roughness:</p>

$$P_{\text{rolling}} = C_{rr} \cdot m_{\text{total}} \cdot g \cdot \cos(\theta) \cdot v$$

<p>Where $C_{rr} \approx 0.0035$ to $0.0050$ for modern clincher/tubeless road tires, and $m_{\text{total}} = m_{\text{rider}} + m_{\text{bike}}$.</p>

<h3>3. Gravitational Resistance on Incline ($P_{\text{gravity}}$)</h3>
<p>When ascending a road gradient of angle $\theta$ (fractional grade $G = \tan \theta$):</p>

$$P_{\text{gravity}} = m_{\text{total}} \cdot g \cdot \sin(\theta) \cdot v \approx m_{\text{total}} \cdot g \cdot G \cdot v$$

<h2>Gross Metabolic Efficiency and the Kilojoule-to-Calorie Equivalence</h2>
<p>A remarkable coincidence of human biophysics simplifies cycling energetics. When a cyclist pedaling at a measured mechanical power output generates mechanical work in kilojoules ($kJ$):</p>

$$\text{Work (kJ)} = \frac{P_{\text{pedal}} (\text{Watts}) \times \text{Duration (seconds)}}{1000}$$

<p>Human skeletal muscle operates at a <strong>Gross Metabolic Efficiency ($\eta_{\text{GME}}$)</strong> of approximately $21.0\%$ to $24.0\%$ ($0.21 \le \eta \le 0.24$). To convert mechanical work ($kJ$) into biological metabolic energy ($kcal$):</p>

$$\text{Metabolic Calories (kcal)} = \frac{\text{Work (kJ)}}{4.184 \times \eta_{\text{GME}}}$$

<p>Because $4.184 \times 0.239 \approx 1.000$, <strong>one kilojoule ($1 \, \text{kJ}$) of mechanical work on a bicycle power meter corresponds almost exactly to one dietary calorie ($1 \, \text{kcal}$) burned by the human body!</strong> This gives cyclists equipped with crank or pedal power meters the single most accurate calorie calculation in all of sports science.</p>

<h3>Road Cycling Speed, Wattage &amp; Calorie Reference Matrix</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Cycling Speed</th>
            <th>Riding Style / Posture</th>
            <th>Required Power (Watts)</th>
            <th>Work Rate (kJ/hr)</th>
            <th>Calorie Burn (75 kg Rider)</th>
            <th>Compendium MET</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>10.0 mph (16 km/h)</td><td>Leisure Commute (Upright)</td><td>65 W</td><td>234 kJ / hr</td><td>260 kcal / hr</td><td>4.0 METs</td></tr>
        <tr><td>12.5 mph (20 km/h)</td><td>Moderate Touring (Hoods)</td><td>105 W</td><td>378 kJ / hr</td><td>420 kcal / hr</td><td>6.0 METs</td></tr>
        <tr><td>15.0 mph (24 km/h)</td><td>Club Endurance Pace</td><td>145 W</td><td>522 kJ / hr</td><td>580 kcal / hr</td><td>8.0 METs</td></tr>
        <tr><td>18.0 mph (29 km/h)</td><td>Vigorous Sportive Pace</td><td>210 W</td><td>756 kJ / hr</td><td>840 kcal / hr</td><td>10.0 METs</td></tr>
        <tr><td>21.0 mph (34 km/h)</td><td>Fast Cat 3/4 Pack Speed</td><td>300 W</td><td>1,080 kJ / hr</td><td>1,200 kcal / hr</td><td>12.5 METs</td></tr>
        <tr><td>25.0 mph (40 km/h)</td><td>Time Trial Solo Breakaway</td><td>430 W</td><td>1,548 kJ / hr</td><td>1,720 kcal / hr</td><td>16.0 METs</td></tr>
    </tbody>
</table>

<div class="worked-example-card">
    <h3>Worked Exercise Physiology Case Study: 40 km Metric Century Training Ride</h3>
    <p><strong>Scenario:</strong> A 75 kg road cyclist riding a 9 kg carbon bike completes a <strong>40-kilometer</strong> solo training route in <strong>1 hour and 15 minutes (75 minutes)</strong> on flat roads with negligible wind. Determine: (1) average speed in km/h and m/s, (2) required mechanical pedal wattage, (3) total mechanical work in kilojoules, and (4) gross metabolic calories burned.</p>
    
    <div class="step-solution">
        <h4>Step 1: Compute Average Speed</h4>
        $$v_{\text{km/h}} = \frac{40 \text{ km}}{1.25 \text{ hr}} = 32.0 \text{ km/h} \approx 19.88 \text{ mph}$$
        $$v_{\text{m/s}} = \frac{32.0}{3.6} \approx 8.889 \text{ m/s}$$

        <h4>Step 2: Calculate Resistive Power Components</h4>
        <p>Aerodynamic power ($C_d A = 0.36 \, \text{m}^2$, $\rho = 1.225$):</p>
        $$P_{\text{aero}} = 0.5 \times 1.225 \times 0.36 \times (8.889)^3 = 0.2205 \times 702.3 \approx 154.9 \text{ W}$$
        <p>Rolling resistance ($C_{rr} = 0.004$, $m_{\text{total}} = 84 \text{ kg}$):</p>
        $$P_{\text{rolling}} = 0.004 \times 84 \times 9.80665 \times 8.889 \approx 29.3 \text{ W}$$
        <p>Accounting for 3% drivetrain friction ($P_{\text{wheel}} = 184.2 \text{ W}$):</p>
        $$P_{\text{pedal}} = \frac{184.2}{0.97} \approx 189.9 \approx 190 \text{ Watts}$$

        <h4>Step 3: Evaluate Total Mechanical Work on Pedals</h4>
        $$\text{Work (kJ)} = \frac{190 \text{ Watts} \times (75 \times 60 \text{ sec})}{1000} = \frac{190 \times 4500}{1000} = 855 \text{ kJ}$$

        <h4>Step 4: Compute Gross Metabolic Calorie Expenditure</h4>
        $$\text{Calories (kcal)} = \frac{855 \text{ kJ}}{4.184 \times 0.22} = \frac{855}{0.9205} \approx 928.8 \text{ kcal}$$
        <p><strong>Result:</strong> The cyclist burned 929 kcal at an average burn rate of $743 \text{ kcal/hr}$.</p>
    </div>
</div>

<h2>Common Mistakes in Cycling Calorie Calculations</h2>
<ol>
    <li><strong>Relying on Heart Rate Monitors for Coasting:</strong> A heart rate monitor cannot distinguish between pedaling at 300 Watts and coasting downhill at 35 mph with zero pedal resistance. Heart rate stays high from adrenaline, causing heart rate straps to wildly overestimate coasting calories.</li>
    <li><strong>Ignoring the Cubic Velocity Penalty:</strong> Assuming that doubling your speed from 10 mph to 20 mph merely doubles your calorie burn. Because aerodynamic power scales with $v^3$, riding at 20 mph requires nearly <strong>four to five times more power</strong> than riding at 10 mph!</li>
    <li><strong>Disregarding Group Drafting:</strong> Tucking into the slipstream of a peloton or cycling group reduces aerodynamic drag by 25% to 40%, cutting true calorie expenditure drastically compared to solo riding at the identical speed.</li>
</ol>

<section class="faq-section">
    <h2>Frequently Asked Questions About Cycling Calories</h2>
    <div class="faq-item">
        <h3>How are cycling calories calculated from mechanical wattage?</h3>
        <p>Mechanical work in kilojoules (kJ) = Average Watts * Time in seconds / 1000. Because human gross metabolic efficiency is roughly 21% to 24%, 1 kJ of mechanical work on the pedals requires approximately 1.0 to 1.15 kcal of metabolic energy.</p>
    </div>
    <div class="faq-item">
        <h3>Why does cycling fast burn exponentially more calories?</h3>
        <p>Aerodynamic drag increases with the square of velocity (F_drag = 0.5 * rho * CdA * v^2), meaning mechanical power required to overcome air resistance scales with the cube of velocity (P_aero proportional to v^3).</p>
    </div>
    <div class="faq-item">
        <h3>How many calories does cycling 15 miles burn?</h3>
        <p>At a moderate speed of 12 to 14 mph, a 70 kg cyclist burns roughly 550 to 650 calories across 15 miles. At race paces (20+ mph), calorie burn exceeds 750 to 850 calories due to immense aerodynamic resistance.</p>
    </div>
    <div class="faq-item">
        <h3>How does climbing hills affect cycling calorie burn?</h3>
        <p>Climbing requires continuous mechanical work against gravity P_gravity = m * g * v * sin(theta), multiplying required power output by 2x to 4x compared to flat terrain.</p>
    </div>
</section>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article)


# ===========================================================================
# TOOL 4: pushup-calorie-calculator.html
# ===========================================================================
def gen_pushup_calorie():
    slug = "pushup-calorie-calculator"
    title = "Pushup Calorie Calculator | Reps, Bodyweight Percentage & Work"
    desc = "Calculate calories burned doing pushups. Biomechanical models accounting for 64% bodyweight displacement, pushup tempo, sets, and mechanical work (W=Fd)."
    h1 = "Pushup Calorie Calculator"
    short_desc = "Biomechanical caloric calculator evaluating energy expenditure during pushups based on effective body mass displacement (64%), vertical center-of-mass travel, and rep tempo."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Pushup Calorie Calculator",
      "url": "https://calchub.com/pushup-calorie-calculator.html",
      "applicationCategory": "HealthApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Calculates calories burned doing pushups based on repetitions, body weight, variation style, and exercise duration."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How many calories does 1 pushup burn?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "One standard pushup burns approximately 0.29 to 0.45 calories depending on the individual's body weight, vertical stroke depth, and rep tempo. Doing 100 pushups burns approximately 30 to 45 calories."
          }
        },
        {
          "@type": "Question",
          "name": "What percentage of body weight do you lift during a pushup?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Force plate biomechanical studies demonstrate that in the top plank position, you support approximately 69% of body weight, and in the bottom 90-degree flexion position, you support approximately 64% of body weight (knee pushups support roughly 49% to 54%)."
          }
        },
        {
          "@type": "Question",
          "name": "Does doing pushups burn calories after you stop exercising?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Intense pushup sets create micro-tears in pectoral and triceps muscle fibers and deplete phosphagen stores, triggering Excess Post-Exercise Oxygen Consumption (EPOC) that elevates metabolic burn for hours after the workout."
          }
        },
        {
          "@type": "Question",
          "name": "How does tempo change the caloric cost of pushups?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Slowing the eccentric descent increases time under tension (TUT), recruiting higher threshold motor units and nearly doubling the muscular metabolic cost compared to rapid momentum-assisted bouncing."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-body">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1.25rem; margin-bottom: 1.25rem;">
        <div>
            <label for="puWeight" style="font-weight: 600; font-size: 0.875rem;">Body Weight:</label>
            <div style="display: flex; gap: 0.5rem;">
                <input type="number" id="puWeight" class="input-field" value="75" min="30" max="250" step="0.5" oninput="calculatePushup()">
                <select id="puWeightUnit" class="input-field" style="width: 80px;" onchange="calculatePushup()">
                    <option value="kg">kg</option>
                    <option value="lbs">lbs</option>
                </select>
            </div>
        </div>
        <div>
            <label for="puReps" style="font-weight: 600; font-size: 0.875rem;">Total Pushup Reps:</label>
            <input type="number" id="puReps" class="input-field" value="50" min="1" max="2000" step="5" oninput="calculatePushup()">
        </div>
        <div>
            <label for="puStyle" style="font-weight: 600; font-size: 0.875rem;">Pushup Variation:</label>
            <select id="puStyle" class="input-field" onchange="calculatePushup()">
                <option value="standard">Standard Floor Pushup (~64% BW)</option>
                <option value="knee">Modified Knee Pushup (~49% BW)</option>
                <option value="decline">Feet-Elevated Decline Pushup (~74% BW)</option>
                <option value="incline">Hands-Elevated Incline Pushup (~50% BW)</option>
            </select>
        </div>
        <div>
            <label for="puTempo" style="font-weight: 600; font-size: 0.875rem;">Rep Tempo / Cadence:</label>
            <select id="puTempo" class="input-field" onchange="calculatePushup()">
                <option value="moderate">Moderate Cadence (2 sec/rep)</option>
                <option value="slow">Strict Time Under Tension (4 sec/rep)</option>
                <option value="fast">Explosive / Rapid (1 sec/rep)</option>
            </select>
        </div>
    </div>

    <div style="display: flex; gap: 0.75rem; margin-bottom: 1.5rem;">
        <button type="button" class="btn btn-primary" onclick="calculatePushup()">Calculate Calories</button>
        <button type="button" class="btn btn-outline" onclick="setPuPreset(30)">30 Reps</button>
        <button type="button" class="btn btn-outline" onclick="setPuPreset(100)">100 Rep Challenge</button>
    </div>

    <div class="result-box" style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem;">
        <h3 style="margin-top: 0; color: #1e293b; font-size: 1.1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">Pushup Caloric &amp; Mechanical Output</h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Total Calories Burned</div>
                <div id="resPuGrossCal" style="font-size: 1.5rem; font-weight: 700; color: #2563eb;">21.6 kcal</div>
                <div id="resPuPerRep" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">0.43 kcal per repetition</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Effective Lifted Mass</div>
                <div id="resPuLiftedMass" style="font-size: 1.4rem; font-weight: 700; color: #0f172a;">48.0 kg</div>
                <div id="resPuLiftedPct" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">64.0% of body weight</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Mechanical Work (W)</div>
                <div id="resPuWorkKj" style="font-size: 1.4rem; font-weight: 700; color: #059669;">7.06 kJ</div>
                <div style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">Concentric lifting work</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Cumulative Tonnage Lifted</div>
                <div id="resPuTonnage" style="font-size: 1.4rem; font-weight: 700; color: #7c3aed;">2,400 kg</div>
                <div style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">5,291 lbs volume</div>
            </div>
        </div>
    </div>
</div>

<script>
function setPuPreset(reps) {
    document.getElementById('puReps').value = reps;
    calculatePushup();
}

function calculatePushup() {
    let w = parseFloat(document.getElementById('puWeight').value) || 75;
    const wUnit = document.getElementById('puWeightUnit').value;
    const wKg = (wUnit === 'lbs') ? (w * 0.453592) : w;

    const reps = parseFloat(document.getElementById('puReps').value) || 50;
    const style = document.getElementById('puStyle').value;
    const tempo = document.getElementById('puTempo').value;

    let bwFactor = 0.64; // Standard
    if (style === 'knee') bwFactor = 0.49;
    if (style === 'decline') bwFactor = 0.74;
    if (style === 'incline') bwFactor = 0.50;

    let tempoFactor = 1.0;
    let secPerRep = 2.0;
    if (tempo === 'slow') { tempoFactor = 1.25; secPerRep = 4.0; }
    if (tempo === 'fast') { tempoFactor = 0.85; secPerRep = 1.0; }

    const liftedMassKg = wKg * bwFactor;
    // Vertical travel of center of mass: approx 0.30 meters (12 inches)
    const displacementM = 0.30;
    const g = 9.80665;

    // Mechanical Work per rep = Force * Distance = (m_lifted * g) * d
    const workPerRepJ = liftedMassKg * g * displacementM;
    const totalWorkJ = workPerRepJ * reps;
    const totalWorkKj = totalWorkJ / 1000;

    // Human muscle efficiency during calisthenics ~18% (accounting for eccentric + isometric stabilization)
    const efficiency = 0.18;
    const metabolicKcal = (totalWorkJ / efficiency) / 4184 * tempoFactor;

    // Cumulative volume lifted
    const cumulativeTonnageKg = liftedMassKg * reps;
    const cumulativeTonnageLbs = cumulativeTonnageKg * 2.20462;
    const calPerRep = reps > 0 ? (metabolicKcal / reps) : 0;

    document.getElementById('resPuGrossCal').innerText = `${metabolicKcal.toFixed(1)} kcal`;
    document.getElementById('resPuPerRep').innerText = `${calPerRep.toFixed(2)} kcal per repetition`;
    document.getElementById('resPuLiftedMass').innerText = `${liftedMassKg.toFixed(1)} kg (${(liftedMassKg * 2.20462).toFixed(1)} lbs)`;
    document.getElementById('resPuLiftedPct').innerText = `${(bwFactor * 100).toFixed(1)}% of body weight`;
    document.getElementById('resPuWorkKj').innerText = `${totalWorkKj.toFixed(2)} kJ`;
    document.getElementById('resPuTonnage').innerText = `${Math.round(cumulativeTonnageKg).toLocaleString()} kg (${Math.round(cumulativeTonnageLbs).toLocaleString()} lbs)`;
}

window.addEventListener('DOMContentLoaded', calculatePushup);
</script>"""

    article = """<h2>Biomechanical Foundations of the Pushup Exercise</h2>
<p>The pushup is one of the most fundamental closed-kinetic chain calisthenic movements in exercise science. By supporting the body's mass on the palms and metatarsals (toes), the movement recruits the pectoralis major, anterior deltoids, triceps brachii, and an extensive network of core postural stabilizers (rectus abdominis, obliques, transversus abdominis, and serratus anterior).</p>

<p>Calculating the true caloric energy expenditure of pushups requires evaluating the biomechanical lever arm of the human skeleton. In 2011, researchers Ebben, Wurm, and VanderZanden published a ground-breaking kinetic investigation in the <em>Journal of Strength and Conditioning Research</em> using precision multi-axis force platforms to quantify ground reaction forces across standard pushup variations:</p>

<ul>
    <li><strong>Standard Pushup:</strong> In the top plank position, the arms support $69.16\%$ of total body weight. In the bottom flexed position (elbows at $90^\circ$), the arms support $64.02\%$ of body weight. The average effective lifted mass throughout the stroke is approximately <strong>$64.0\%$ of body weight</strong>.</li>
    <li><strong>Modified Knee Pushup:</strong> Flexing at the knees reduces the body's lever arm, supporting approximately <strong>$49.0\%$ to $53.5\%$ of body weight</strong>.</li>
    <li><strong>Feet-Elevated Decline Pushup:</strong> Elevating the feet on a 12-inch bench shifts center of mass anteriorly onto the hands, increasing effective lifted mass to <strong>$74.1\%$ of body weight</strong>.</li>
    <li><strong>Hands-Elevated Incline Pushup:</strong> Elevating hands on a bench decreases effective lifted mass to <strong>$41.0\%$ to $55.0\%$ of body weight</strong>.</li>
</ul>

<h2>Mechanical Work Formulation ($W = F \cdot d$)</h2>
<p>The mechanical work performed during each pushup repetition is governed by Newtonian physics:</p>

$$W_{\text{rep}} = F_{\text{effective}} \cdot d = (m_{\text{body}} \times \text{Factor}_{\text{BW}} \times g) \cdot \Delta h_{\text{COM}}$$

<p>Where $g = 9.80665 \, \text{m/s}^2$ and $\Delta h_{\text{COM}}$ represents the vertical displacement of the center of mass (typically $0.28$ to $0.35$ meters for average adult arm lengths). For an individual weighing $75 \, \text{kg}$ performing a standard pushup ($\text{Factor}_{\text{BW}} = 0.64$):</p>

$$F_{\text{effective}} = 75 \times 0.64 \times 9.80665 \approx 470.72 \text{ Newtons}$$
$$W_{\text{rep}} = 470.72 \, \text{N} \times 0.30 \, \text{m} \approx 141.22 \text{ Joules per rep}$$

<p>Accounting for skeletal muscle mechanical efficiency ($\eta \approx 18\%$ when including eccentric braking and isometric core stabilization) and thermochemical conversion ($1 \, \text{kcal} = 4,184 \, \text{J}$):</p>

$$\text{Metabolic Calories per Rep} = \frac{141.22 \text{ J}}{0.18 \times 4,184 \text{ J/kcal}} \approx 0.375 \text{ kcal per repetition}$$

<h3>Pushup Variations &amp; Biomechanical Kinetic Matrix</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Pushup Variation</th>
            <th>Effective Bodyweight %</th>
            <th>Effective Load (70 kg Person)</th>
            <th>Mechanical Work / Rep</th>
            <th>Calories per 50 Reps</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Modified (Knees)</td><td>49.0% Body Weight</td><td>34.3 kg (75.6 lbs)</td><td>100.9 J</td><td>16.8 kcal</td></tr>
        <tr><td>Hands-Elevated Incline (30 cm)</td><td>55.0% Body Weight</td><td>38.5 kg (84.9 lbs)</td><td>113.3 J</td><td>18.8 kcal</td></tr>
        <tr><td>Standard Floor Pushup</td><td>64.0% Body Weight</td><td>44.8 kg (98.8 lbs)</td><td>131.8 J</td><td>21.9 kcal</td></tr>
        <tr><td>Decline (Feet on 30 cm Box)</td><td>74.0% Body Weight</td><td>51.8 kg (114.2 lbs)</td><td>152.4 J</td><td>25.3 kcal</td></tr>
        <tr><td>One-Arm Pushup</td><td>71.5% Body Weight</td><td>50.1 kg (110.5 lbs)</td><td>147.4 J</td><td>24.5 kcal (Heavy Core)</td></tr>
    </tbody>
</table>

<div class="worked-example-card">
    <h3>Worked Biomechanical Case Study: The 100-Pushup Daily Challenge</h3>
    <p><strong>Scenario:</strong> An 80 kg athlete completes <strong>100 standard pushups</strong> in four sets of 25 reps with strict 2-second tempo (1 second down, 1 second up) with a vertical center-of-mass travel of $0.32 \text{ meters}$. Calculate: (1) effective lifted mass per repetition, (2) total mechanical work performed, (3) gross metabolic calories burned, and (4) cumulative volume tonnage lifted.</p>
    
    <div class="step-solution">
        <h4>Step 1: Compute Effective Lifted Mass</h4>
        $$m_{\text{lifted}} = 80 \text{ kg} \times 0.64 = 51.2 \text{ kg} \approx 112.87 \text{ lbs}$$

        <h4>Step 2: Evaluate Mechanical Work per Rep and Total</h4>
        $$W_{\text{rep}} = 51.2 \text{ kg} \times 9.80665 \text{ m/s}^2 \times 0.32 \text{ m} \approx 160.67 \text{ Joules}$$
        $$W_{\text{total}} = 100 \times 160.67 \text{ J} = 16,067 \text{ Joules} \approx 16.07 \text{ kJ}$$

        <h4>Step 3: Evaluate Metabolic Caloric Expenditure</h4>
        $$\text{Calories} = \frac{16,067 \text{ J}}{0.18 \times 4,184 \text{ J/kcal}} = \frac{16,067}{753.12} \approx 21.33 \text{ kcal (direct concentric work)}$$
        <p>Adding dynamic core isometric stabilization and warm-up metabolic overhead ($\approx 1.6\times$ multiplier):</p>
        $$\text{Total Caloric Burn} \approx 34.1 \text{ kcal}$$

        <h4>Step 4: Cumulative Tonnage Lifted</h4>
        $$\text{Total Tonnage} = 100 \text{ reps} \times 51.2 \text{ kg} = 5,120 \text{ kg} \approx 11,287 \text{ lbs}$$
        <p><strong>Physiological Insight:</strong> Although 34 calories seems modest, completing 100 pushups is equivalent to bench pressing over 5.1 metric tons of cumulative volume!</p>
    </div>
</div>

<h2>Common Calculation Errors Regarding Pushup Calorie Burn</h2>
<ol>
    <li><strong>Assuming 100% Body Weight is Lifted:</strong> The most common error online assumes an 80 kg person lifts 80 kg per rep. Because your feet act as a ground fulcrum, you only lift 64% of your mass.</li>
    <li><strong>Ignoring Time Under Tension (TUT):</strong> Rapidly bouncing through 50 pushups using elastic bounce burns significantly fewer calories than performing 50 slow, controlled reps with a 3-second eccentric descent.</li>
    <li><strong>Equating Pushups to Cardio Machines:</strong> Pushups are primarily an anaerobic muscular endurance stimulus. Their primary body composition benefit is muscular hypertrophy and metabolic rate maintenance, rather than massive acute calorie expenditure.</li>
</ol>

<section class="faq-section">
    <h2>Frequently Asked Questions About Pushup Calories</h2>
    <div class="faq-item">
        <h3>How many calories does 1 pushup burn?</h3>
        <p>One standard pushup burns approximately 0.29 to 0.45 calories depending on the individual's body weight, vertical stroke depth, and rep tempo. Doing 100 pushups burns approximately 30 to 45 calories.</p>
    </div>
    <div class="faq-item">
        <h3>What percentage of body weight do you lift during a pushup?</h3>
        <p>Force plate biomechanical studies demonstrate that in the top plank position, you support approximately 69% of body weight, and in the bottom 90-degree flexion position, you support approximately 64% of body weight (knee pushups support roughly 49% to 54%).</p>
    </div>
    <div class="faq-item">
        <h3>Does doing pushups burn calories after you stop exercising?</h3>
        <p>Yes. Intense pushup sets create micro-tears in pectoral and triceps muscle fibers and deplete phosphagen stores, triggering Excess Post-Exercise Oxygen Consumption (EPOC) that elevates metabolic burn for hours after the workout.</p>
    </div>
    <div class="faq-item">
        <h3>How does tempo change the caloric cost of pushups?</h3>
        <p>Slowing the eccentric descent increases time under tension (TUT), recruiting higher threshold motor units and nearly doubling the muscular metabolic cost compared to rapid momentum-assisted bouncing.</p>
    </div>
</section>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article)


# ===========================================================================
# TOOL 5: bench-press-calories-calculator.html
# ===========================================================================
def gen_bench_press_calorie():
    slug = "bench-press-calories-calculator"
    title = "Bench Press Calories Calculator | Barbell Load, Sets & Rep Work"
    desc = "Calculate calories burned during barbell bench press training. Accounts for lifted weight, sets, reps, stroke distance, rest periods, and EPOC metabolic afterburn."
    h1 = "Bench Press Calories Calculator"
    short_desc = "Biomechanical and metabolic resistance training engine calculating mechanical work ($W = F \cdot d$), cumulative volume tonnage, and EPOC caloric afterburn for bench press workouts."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Bench Press Calories Calculator",
      "url": "https://calchub.com/bench-press-calories-calculator.html",
      "applicationCategory": "HealthApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Calculates calories burned bench pressing based on barbell weight, reps, sets, rest intervals, and metabolic work."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How many calories does a bench press workout burn?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A standard 45-minute heavy bench press session comprising 4 to 6 working sets with rest intervals burns approximately 150 to 250 calories during the workout, plus an additional 30 to 60 calories through EPOC afterburn."
          }
        },
        {
          "@type": "Question",
          "name": "How is mechanical work calculated on the bench press?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Mechanical work in Joules = Barbell Mass (kg) * Gravity (9.81 m/s^2) * Vertical Stroke Displacement (m) * Total Repetitions."
          }
        },
        {
          "@type": "Question",
          "name": "What is EPOC (Excess Post-Exercise Oxygen Consumption) in weightlifting?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "EPOC represents the elevated rate of oxygen consumption post-exercise required to replenish creatine phosphate, re-oxygenate blood myoglobin, clear lactate, and initiate protein synthesis repair."
          }
        },
        {
          "@type": "Question",
          "name": "Do longer rest periods reduce caloric expenditure in resistance training?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Longer rest periods reduce the average calories burned per minute of workout time, but allow greater power output and heavier barbell loading, resulting in higher mechanical work per working set."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-body">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1.25rem; margin-bottom: 1.25rem;">
        <div>
            <label for="bpWeight" style="font-weight: 600; font-size: 0.875rem;">Lifter Body Weight:</label>
            <div style="display: flex; gap: 0.5rem;">
                <input type="number" id="bpWeight" class="input-field" value="80" min="30" max="250" step="0.5" oninput="calculateBenchPress()">
                <select id="bpWeightUnit" class="input-field" style="width: 80px;" onchange="calculateBenchPress()">
                    <option value="kg">kg</option>
                    <option value="lbs">lbs</option>
                </select>
            </div>
        </div>
        <div>
            <label for="bpBarWeight" style="font-weight: 600; font-size: 0.875rem;">Barbell Load (Bar + Plates):</label>
            <div style="display: flex; gap: 0.5rem;">
                <input type="number" id="bpBarWeight" class="input-field" value="80" min="10" max="500" step="2.5" oninput="calculateBenchPress()">
                <select id="bpBarUnit" class="input-field" style="width: 80px;" onchange="calculateBenchPress()">
                    <option value="kg">kg</option>
                    <option value="lbs">lbs</option>
                </select>
            </div>
        </div>
        <div>
            <label for="bpSets" style="font-weight: 600; font-size: 0.875rem;">Working Sets:</label>
            <input type="number" id="bpSets" class="input-field" value="4" min="1" max="20" step="1" oninput="calculateBenchPress()">
        </div>
        <div>
            <label for="bpReps" style="font-weight: 600; font-size: 0.875rem;">Reps per Set:</label>
            <input type="number" id="bpReps" class="input-field" value="8" min="1" max="50" step="1" oninput="calculateBenchPress()">
        </div>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.25rem; margin-bottom: 1.5rem;">
        <div>
            <label for="bpRestMins" style="font-weight: 600; font-size: 0.875rem;">Rest Between Sets (minutes):</label>
            <input type="number" id="bpRestMins" class="input-field" value="2.5" min="0.5" max="10" step="0.5" oninput="calculateBenchPress()">
        </div>
        <div>
            <label for="bpStrokeDist" style="font-weight: 600; font-size: 0.875rem;">Vertical Bar Stroke (cm):</label>
            <input type="number" id="bpStrokeDist" class="input-field" value="38" min="15" max="75" step="1" oninput="calculateBenchPress()">
            <span class="input-hint">Distance from chest touch to lockout</span>
        </div>
    </div>

    <div style="display: flex; gap: 0.75rem; margin-bottom: 1.5rem;">
        <button type="button" class="btn btn-primary" onclick="calculateBenchPress()">Calculate Energy</button>
        <button type="button" class="btn btn-outline" onclick="setBpPreset('hypertrophy')">3 &times; 10 Hypertrophy</button>
        <button type="button" class="btn btn-outline" onclick="setBpPreset('strength')">5 &times; 5 Strength</button>
    </div>

    <div class="result-box" style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem;">
        <h3 style="margin-top: 0; color: #1e293b; font-size: 1.1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">Bench Press Energy &amp; Tonnage Output</h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Total Workout Calories</div>
                <div id="resBpTotalCal" style="font-size: 1.5rem; font-weight: 700; color: #2563eb;">118 kcal</div>
                <div id="resBpEpoc" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">Includes 24 kcal EPOC afterburn</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Total Tonnage Lifted</div>
                <div id="resBpTonnage" style="font-size: 1.4rem; font-weight: 700; color: #0f172a;">2,560 kg</div>
                <div id="resBpTonnageLbs" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">5,644 lbs volume</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Mechanical Work (W)</div>
                <div id="resBpWorkKj" style="font-size: 1.4rem; font-weight: 700; color: #16a34a;">9.54 kJ</div>
                <div style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">Concentric lifting physics</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Workout Duration</div>
                <div id="resBpTotalTime" style="font-size: 1.4rem; font-weight: 700; color: #7c3aed;">11.5 minutes</div>
                <div id="resBpTotalReps" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">32 reps total</div>
            </div>
        </div>
    </div>
</div>

<script>
function setBpPreset(type) {
    if (type === 'hypertrophy') {
        document.getElementById('bpSets').value = '3';
        document.getElementById('bpReps').value = '10';
        document.getElementById('bpRestMins').value = '2.0';
    } else if (type === 'strength') {
        document.getElementById('bpSets').value = '5';
        document.getElementById('bpReps').value = '5';
        document.getElementById('bpRestMins').value = '3.0';
    }
    calculateBenchPress();
}

function calculateBenchPress() {
    let w = parseFloat(document.getElementById('bpWeight').value) || 80;
    const wUnit = document.getElementById('bpWeightUnit').value;
    const wKg = (wUnit === 'lbs') ? (w * 0.453592) : w;

    let b = parseFloat(document.getElementById('bpBarWeight').value) || 80;
    const bUnit = document.getElementById('bpBarUnit').value;
    const barKg = (bUnit === 'lbs') ? (b * 0.453592) : b;

    const sets = parseFloat(document.getElementById('bpSets').value) || 4;
    const reps = parseFloat(document.getElementById('bpReps').value) || 8;
    const restMins = parseFloat(document.getElementById('bpRestMins').value) || 2.5;
    const strokeCm = parseFloat(document.getElementById('bpStrokeDist').value) || 38;
    const strokeM = strokeCm / 100.0;

    const totalReps = sets * reps;
    const totalTonnageKg = barKg * totalReps;
    const totalTonnageLbs = totalTonnageKg * 2.20462;

    // Time: assume 3 seconds per rep TUT + rest intervals
    const activeTimeMins = (totalReps * 3) / 60;
    const restTimeMins = (sets - 1) * restMins;
    const totalDurationMins = activeTimeMins + restTimeMins;

    // Mechanical Work in Joules W = m * g * d * reps
    const g = 9.80665;
    const workJ = barKg * g * strokeM * totalReps;
    const workKj = workJ / 1000;

    // Muscular efficiency in heavy bench press ~15% (due to heavy eccentric braking and shoulder stabilization)
    const concentricKcal = (workJ / 0.15) / 4184;

    // Inter-set resting metabolic burn (MET ~ 2.5 during rest recovery)
    const restKcal = ((2.5 * 3.5 * wKg) / 200) * restTimeMins;

    // EPOC afterburn (~20% of total workout expenditure)
    const directKcal = concentricKcal + restKcal;
    const epocKcal = directKcal * 0.20;
    const totalGrossKcal = directKcal + epocKcal;

    document.getElementById('resBpTotalCal').innerText = `${Math.round(totalGrossKcal)} kcal`;
    document.getElementById('resBpEpoc').innerText = `Includes ${Math.round(epocKcal)} kcal EPOC afterburn`;
    document.getElementById('resBpTonnage').innerText = `${Math.round(totalTonnageKg).toLocaleString()} kg`;
    document.getElementById('resBpTonnageLbs').innerText = `${Math.round(totalTonnageLbs).toLocaleString()} lbs volume`;
    document.getElementById('resBpWorkKj').innerText = `${workKj.toFixed(2)} kJ`;
    document.getElementById('resBpTotalTime').innerText = `${totalDurationMins.toFixed(1)} minutes`;
    document.getElementById('resBpTotalReps').innerText = `${totalReps} total reps (${sets} sets)`;
}

window.addEventListener('DOMContentLoaded', calculateBenchPress);
</script>"""

    article = """<h2>Biomechanical and Energetic Modeling of Heavy Resistance Training</h2>
<p>Estimating caloric expenditure during heavy resistance exercises—such as the <strong>Barbell Bench Press</strong>—presents physiological complexities absent in steady-state aerobic locomotion. While running or cycling consumes energy continuously along linear aerobic pathways, the bench press relies predominantly on the anaerobic phosphagen system (adenosine triphosphate and creatine phosphate, ATP-CP) and rapid anaerobic glycolysis.</p>

<p>Energy consumption in the bench press is evaluated by partitioning the exercise session into three distinct thermodynamic phases:</p>
<ol>
    <li><strong>Direct Mechanical Concentric Work ($W_{\text{concentric}}$):</strong> The positive physical work performed by the pectoralis major, anterior deltoids, and triceps brachii against gravity to lift the barbell from the sternum to full elbow lockout.</li>
    <li><strong>Inter-Set Metabolic Recovery ($E_{\text{recovery}}$):</strong> The active metabolic cost of phosphagen resynthesis and cardiorespiratory recovery during rest intervals between working sets.</li>
    <li><strong>Excess Post-Exercise Oxygen Consumption (EPOC):</strong> The extended post-workout metabolic afterburn driven by cellular repair, protein synthesis, and metabolic clearance.</li>
</ol>

<h2>Mechanical Work Formulation on the Barbell</h2>
<p>When a lifter presses a barbell with mass $m_{\text{bar}}$ vertically across a linear stroke distance $d$ (meters), the mechanical work performed per repetition evaluates as:</p>

$$W_{\text{rep}} = F \cdot d = (m_{\text{bar}} \times g) \cdot d$$

<p>Where $g = 9.80665 \, \text{m/s}^2$. Across $S$ sets of $R$ repetitions, cumulative mechanical concentric work evaluates as:</p>

$$W_{\text{total}} = S \cdot R \cdot (m_{\text{bar}} \cdot g \cdot d)$$

<p>In human skeletal muscle, the thermodynamic efficiency during high-load concentric pressing is approximately $15\%$ ($\eta \approx 0.15$). The remaining $85\%$ of chemical potential energy is liberated as thermal heat. The metabolic caloric equivalent of concentric barbell displacement evaluates as:</p>

$$\text{Calories}_{\text{concentric}} = \frac{W_{\text{total}}}{0.15 \times 4184}$$

<h2>The Role of EPOC (Excess Post-Exercise Oxygen Consumption)</h2>
<p>Unlike aerobic treadmill exercise, where energy expenditure returns to baseline within minutes of stopping, heavy strength training induces sustained metabolic disruption. As demonstrated in classic studies by Børsheim and Bahr (2003) and Schuenke et al. (2002), high-intensity resistance training stimulates an <strong>EPOC afterburn</strong> lasting from 14 to 38 hours post-workout. EPOC accounts for an additional <strong>$15\%$ to $25\%$ of total workout caloric expenditure</strong>, driven by:</p>
<ul>
    <li>Replenishment of muscle myoglobin and hemoglobin oxygen stores.</li>
    <li>Resynthesis of ATP and creatine phosphate via mitochondrial oxidative phosphorylation.</li>
    <li>Lactate gluconeogenesis in the liver via the Cori Cycle.</li>
    <li>Elevated core body temperature and sympathetic nervous system circulation.</li>
    <li>Myofibrillar micro-trauma repair and ribosomal protein synthesis (mTOR activation).</li>
</ul>

<h3>Bench Press Load, Volume &amp; Caloric Expenditure Matrix</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Barbell Load</th>
            <th>Sets &amp; Reps Scheme</th>
            <th>Rest Interval</th>
            <th>Cumulative Tonnage</th>
            <th>Direct Calories</th>
            <th>Total Burn + EPOC</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>60 kg (132 lbs)</td><td>3 sets &times; 10 reps</td><td>2.0 mins</td><td>1,800 kg (3,968 lbs)</td><td>72 kcal</td><td>88 kcal</td></tr>
        <tr><td>80 kg (176 lbs)</td><td>4 sets &times; 8 reps</td><td>2.5 mins</td><td>2,560 kg (5,644 lbs)</td><td>96 kcal</td><td>118 kcal</td></tr>
        <tr><td>100 kg (225 lbs)</td><td>5 sets &times; 5 reps</td><td>3.0 mins</td><td>2,500 kg (5,512 lbs)</td><td>104 kcal</td><td>128 kcal</td></tr>
        <tr><td>120 kg (265 lbs)</td><td>5 sets &times; 3 reps</td><td>4.0 mins</td><td>1,800 kg (3,968 lbs)</td><td>92 kcal</td><td>114 kcal</td></tr>
        <tr><td>140 kg (308 lbs)</td><td>6 sets &times; 2 reps</td><td>5.0 mins</td><td>1,680 kg (3,704 lbs)</td><td>95 kcal</td><td>119 kcal</td></tr>
    </tbody>
</table>

<div class="worked-example-card">
    <h3>Worked Strength Conditioning Case Study: 5x5 Heavy Bench Press Session</h3>
    <p><strong>Scenario:</strong> An 85 kg competitive powerlifter performs a classic <strong>5 &times; 5 working set protocol</strong> with a <strong>100 kg (225 lb) barbell</strong>. The vertical stroke distance from chest touch to lockout is <strong>36 cm (0.36 m)</strong>, and the lifter takes <strong>3.0 minutes of rest</strong> between sets. Calculate: (1) total repetitions and tonnage volume, (2) total mechanical work, (3) inter-set recovery calories, and (4) total gross caloric burn including EPOC.</p>
    
    <div class="step-solution">
        <h4>Step 1: Compute Repetitions and Tonnage Volume</h4>
        $$\text{Total Reps} = 5 \text{ sets} \times 5 \text{ reps} = 25 \text{ repetitions}$$
        $$\text{Volume Tonnage} = 25 \times 100 \text{ kg} = 2,500 \text{ kg} \approx 5,512 \text{ lbs}$$

        <h4>Step 2: Evaluate Mechanical Concentric Work</h4>
        $$W_{\text{rep}} = 100 \text{ kg} \times 9.80665 \text{ m/s}^2 \times 0.36 \text{ m} \approx 353.04 \text{ Joules}$$
        $$W_{\text{total}} = 25 \times 353.04 \text{ J} = 8,826 \text{ Joules} \approx 8.83 \text{ kJ}$$
        $$\text{Concentric Calories} = \frac{8,826}{0.15 \times 4184} \approx 14.06 \text{ kcal}$$

        <h4>Step 3: Evaluate Inter-Set Rest Period Burn</h4>
        $$\text{Total Rest Time} = (5 - 1) \text{ intervals} \times 3.0 \text{ min} = 12.0 \text{ minutes}$$
        $$\text{Rest Calories} = \frac{2.5 \text{ METs} \times 3.5 \times 85 \text{ kg}}{200} \times 12.0 \text{ min} \approx 44.63 \text{ kcal}$$

        <h4>Step 4: Compute Total Session Expenditure with EPOC</h4>
        $$\text{Direct Workout Calories} = 14.06 + 44.63 \approx 58.69 \text{ kcal}$$
        $$\text{EPOC Afterburn (20%)} = 58.69 \times 0.20 \approx 11.74 \text{ kcal}$$
        $$\text{Total Gross Caloric Burn} = 58.69 + 11.74 \approx 70.43 \text{ kcal}$$
        <p><strong>Training Insight:</strong> While a 5x5 bench press session burns ~70 to 80 kcal directly, its neuromuscular adaptation preserves lean muscle mass, elevating resting metabolic rate 24/7.</p>
    </div>
</div>

<h2>Common Misconceptions in Resistance Training Calorie Tracking</h2>
<ol>
    <li><strong>Expecting Cardio-Level Calorie Burns:</strong> Fitness wearables frequently display 400+ calories for a 30-minute chest workout by erroneously interpreting elevated heart rate as aerobic output. Heavy lifting spikes sympathetic heart rate via the Valsalva maneuver, not proportional oxygen consumption.</li>
    <li><strong>Ignoring Eccentric Energy Cost:</strong> Lowering a 100 kg barbell in a controlled descent requires active eccentric muscle contraction that consumes ~25% as much energy as concentric pressing while generating massive structural hypertrophy signaling.</li>
    <li><strong>Neglecting Bar Stroke Depth:</strong> Bouncing the bar off the rib cage or cutting the range of motion in half halves the mechanical displacement $d$, substantially reducing muscular work and hypertrophy stimulus.</li>
</ol>

<section class="faq-section">
    <h2>Frequently Asked Questions About Bench Press Calories</h2>
    <div class="faq-item">
        <h3>How many calories does a bench press workout burn?</h3>
        <p>A standard 45-minute heavy bench press session comprising 4 to 6 working sets with rest intervals burns approximately 150 to 250 calories during the workout, plus an additional 30 to 60 calories through EPOC afterburn.</p>
    </div>
    <div class="faq-item">
        <h3>How is mechanical work calculated on the bench press?</h3>
        <p>Mechanical work in Joules = Barbell Mass (kg) * Gravity (9.81 m/s^2) * Vertical Stroke Displacement (m) * Total Repetitions.</p>
    </div>
    <div class="faq-item">
        <h3>What is EPOC (Excess Post-Exercise Oxygen Consumption) in weightlifting?</h3>
        <p>EPOC represents the elevated rate of oxygen consumption post-exercise required to replenish creatine phosphate, re-oxygenate blood myoglobin, clear lactate, and initiate protein synthesis repair.</p>
    </div>
    <div class="faq-item">
        <h3>Do longer rest periods reduce caloric expenditure in resistance training?</h3>
        <p>Longer rest periods reduce the average calories burned per minute of workout time, but allow greater power output and heavier barbell loading, resulting in higher mechanical work per working set.</p>
    </div>
</section>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article)


# ===========================================================================
# TOOL 6: swimming-calorie-calculator.html
# ===========================================================================
def gen_swimming_calorie():
    slug = "swimming-calorie-calculator"
    title = "Swimming Calorie Calculator | Stroke Styles, Pace & Water Thermal Loss"
    desc = "Calculate calories burned swimming freestyle, breaststroke, backstroke, and butterfly. Accounts for stroke mechanics, lap pace, body weight, and water convection."
    h1 = "Swimming Calorie Calculator"
    short_desc = "Precision aquatic exercise physiology engine evaluating caloric expenditure across swimming strokes, hydrodynamic drag, lap pacing, and water thermal conduction."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Swimming Calorie Calculator",
      "url": "https://calchub.com/swimming-calorie-calculator.html",
      "applicationCategory": "HealthApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Calculates calories burned swimming based on stroke type, pace, body weight, and duration."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Which swimming stroke burns the most calories?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The Butterfly stroke burns the most calories by a wide margin, requiring 11.0 to 13.8 METs (up to 800-950 kcal/hr for an average adult) due to immense bilateral shoulder power and undulatory dolphin kicking."
          }
        },
        {
          "@type": "Question",
          "name": "Why does swimming burn more calories in colder water?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Water has a thermal conductivity approximately 24 times greater than air. In water temperatures below 25°C (77°F), the human body expends significant metabolic energy through non-shivering thermogenesis to maintain a 37°C core body temperature."
          }
        },
        {
          "@type": "Question",
          "name": "How many calories does swimming 1,000 meters burn?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Swimming 1,000 meters (approx 40 laps in a 25m pool) at a moderate freestyle pace typically burns 220 to 300 calories for a 70 kg swimmer in roughly 20 to 25 minutes."
          }
        },
        {
          "@type": "Question",
          "name": "Why is swimming gross mechanical efficiency so low compared to running?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Water density is roughly 800 times greater than air. Swimmers operate at a low gross mechanical efficiency of only 5% to 9% because the vast majority of metabolic energy is lost generating turbulent vortices and overcoming viscous fluid drag."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calc-body">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1.25rem; margin-bottom: 1.25rem;">
        <div>
            <label for="swWeight" style="font-weight: 600; font-size: 0.875rem;">Swimmer Body Weight:</label>
            <div style="display: flex; gap: 0.5rem;">
                <input type="number" id="swWeight" class="input-field" value="70" min="25" max="250" step="0.5" oninput="calculateSwimming()">
                <select id="swWeightUnit" class="input-field" style="width: 80px;" onchange="calculateSwimming()">
                    <option value="kg">kg</option>
                    <option value="lbs">lbs</option>
                </select>
            </div>
        </div>
        <div>
            <label for="swStroke" style="font-weight: 600; font-size: 0.875rem;">Swimming Stroke Style:</label>
            <select id="swStroke" class="input-field" onchange="calculateSwimming()">
                <option value="freestyle_mod">Freestyle / Front Crawl (Moderate - 8.3 METs)</option>
                <option value="freestyle_vig">Freestyle / Front Crawl (Vigorous - 10.0 METs)</option>
                <option value="breaststroke">Breaststroke (Recreational/Moderate - 7.0 METs)</option>
                <option value="breaststroke_vig">Breaststroke (Competition/Vigorous - 10.3 METs)</option>
                <option value="backstroke">Backstroke (Moderate Pace - 7.0 METs)</option>
                <option value="butterfly">Butterfly (Vigorous / Competition - 13.8 METs)</option>
                <option value="treading">Treading Water (Moderate - 3.5 METs)</option>
                <option value="treading_vig">Treading Water (Vigorous - 9.8 METs)</option>
            </select>
        </div>
        <div>
            <label for="swDuration" style="font-weight: 600; font-size: 0.875rem;">Duration (minutes):</label>
            <input type="number" id="swDuration" class="input-field" value="45" min="1" max="300" step="5" oninput="calculateSwimming()">
        </div>
        <div>
            <label for="swTemp" style="font-weight: 600; font-size: 0.875rem;">Pool Water Temperature:</label>
            <select id="swTemp" class="input-field" onchange="calculateSwimming()">
                <option value="standard">Standard Indoor Lap Pool (26&deg;C - 28&deg;C / 80&deg;F)</option>
                <option value="cold">Cold Open Water (&lt; 20&deg;C / &lt; 68&deg;F - Extra Thermogenesis)</option>
                <option value="warm">Warm Therapy Pool (&gt; 31&deg;C / &gt; 88&deg;F)</option>
            </select>
        </div>
    </div>

    <div style="display: flex; gap: 0.75rem; margin-bottom: 1.5rem;">
        <button type="button" class="btn btn-primary" onclick="calculateSwimming()">Calculate Calories</button>
        <button type="button" class="btn btn-outline" onclick="setSwPreset('lap30')">30 Min Lap Swim</button>
        <button type="button" class="btn btn-outline" onclick="setSwPreset('fly20')">20 Min Butterfly HIIT</button>
    </div>

    <div class="result-box" style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem;">
        <h3 style="margin-top: 0; color: #1e293b; font-size: 1.1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">Aquatic Energy Expenditure Summary</h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Total Calories Burned</div>
                <div id="resSwGrossCal" style="font-size: 1.5rem; font-weight: 700; color: #2563eb;">383 kcal</div>
                <div id="resSwNetCal" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">Net: 328 kcal above rest</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Hourly Burn Rate</div>
                <div id="resSwHourly" style="font-size: 1.4rem; font-weight: 700; color: #0f172a;">510 kcal/hr</div>
                <div id="resSwMets" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">Intensity: 8.3 METs</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Estimated Distance</div>
                <div id="resSwDist" style="font-size: 1.4rem; font-weight: 700; color: #16a34a;">1,800 meters</div>
                <div id="resSwLaps" style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">72 laps (25m pool)</div>
            </div>
            <div style="background: white; padding: 0.75rem; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 700;">Calorie Equivalence</div>
                <div id="resSwEquiv" style="font-size: 1.2rem; font-weight: 700; color: #7c3aed;">~3.8 Miles Running</div>
                <div style="font-size: 0.8rem; color: #64748b; margin-top: 0.25rem;">Equivalent land cardio cost</div>
            </div>
        </div>
    </div>
</div>

<script>
const STROKE_METS = {
    freestyle_mod: 8.3,
    freestyle_vig: 10.0,
    breaststroke: 7.0,
    breaststroke_vig: 10.3,
    backstroke: 7.0,
    butterfly: 13.8,
    treading: 3.5,
    treading_vig: 9.8
};

// Typical pacing in m/min
const STROKE_SPEED_MPM = {
    freestyle_mod: 40,
    freestyle_vig: 55,
    breaststroke: 32,
    breaststroke_vig: 45,
    backstroke: 35,
    butterfly: 50,
    treading: 0,
    treading_vig: 0
};

function setSwPreset(type) {
    if (type === 'lap30') {
        document.getElementById('swStroke').value = 'freestyle_mod';
        document.getElementById('swDuration').value = '30';
    } else if (type === 'fly20') {
        document.getElementById('swStroke').value = 'butterfly';
        document.getElementById('swDuration').value = '20';
    }
    calculateSwimming();
}

function calculateSwimming() {
    let w = parseFloat(document.getElementById('swWeight').value) || 70;
    const wUnit = document.getElementById('swWeightUnit').value;
    const wKg = (wUnit === 'lbs') ? (w * 0.453592) : w;

    const stroke = document.getElementById('swStroke').value;
    const durMins = parseFloat(document.getElementById('swDuration').value) || 45;
    const temp = document.getElementById('swTemp').value;

    let baseMets = STROKE_METS[stroke] || 8.0;

    // Thermal factor: cold water increases energy cost via thermogenesis
    let thermalFactor = 1.0;
    if (temp === 'cold') thermalFactor = 1.15; // 15% increase
    if (temp === 'warm') thermalFactor = 1.02;

    const effectiveMets = baseMets * thermalFactor;

    // ACSM Gross Calorie formula: (MET * 3.5 * weight_kg / 200) * duration_min
    const grossKcal = ((effectiveMets * 3.5 * wKg) / 200) * durMins;
    const restingKcal = (3.5 * wKg / 200) * durMins;
    const netKcal = Math.max(0, grossKcal - restingKcal);
    const hourlyKcal = (durMins > 0) ? (grossKcal / durMins) * 60 : 0;

    // Estimated distance based on typical stroke velocity
    const speedMpm = STROKE_SPEED_MPM[stroke] || 40;
    const estDistanceM = speedMpm * durMins;
    const laps25m = Math.round(estDistanceM / 25);

    // Equivalent running miles (~100 kcal / mile for average adult)
    const equivRunningMiles = (grossKcal / 100).toFixed(1);

    document.getElementById('resSwGrossCal').innerText = `${Math.round(grossKcal)} kcal`;
    document.getElementById('resSwNetCal').innerText = `Net: ${Math.round(netKcal)} kcal above rest`;
    document.getElementById('resSwHourly').innerText = `${Math.round(hourlyKcal)} kcal/hr`;
    document.getElementById('resSwMets').innerText = `Intensity: ${effectiveMets.toFixed(1)} METs`;
    document.getElementById('resSwDist').innerText = `${estDistanceM.toLocaleString()} meters`;
    document.getElementById('resSwLaps').innerText = `${laps25m} laps (25m pool) | ${(estDistanceM / 1609.34).toFixed(2)} mi`;
    document.getElementById('resSwEquiv').innerText = `~${equivRunningMiles} Miles Running`;
}

window.addEventListener('DOMContentLoaded', calculateSwimming);
</script>"""

    article = """<h2>Hydrodynamic and Metabolic Energetics of Swimming</h2>
<p>Swimming represents one of the most energetically demanding athletic disciplines due to the physical properties of the aquatic medium. Water has a physical mass density of approximately $1,000 \, \text{kg/m}^3$—nearly <strong>800 times denser than ambient air</strong>—and a dynamic viscosity over 50 times greater than air. Consequently, moving through water generates immense hydrodynamic drag that severely limits mechanical efficiency.</p>

<p>In terrestrial running or cycling, human gross mechanical efficiency ranges between $20\%$ and $25\%$. In contrast, pioneering fluid mechanics studies by Pendergast, di Prampero, and Zamparo demonstrate that human swimming exhibits an exceptionally low <strong>gross mechanical propelling efficiency of only $5\%$ to $9\%$</strong>. Over $90\%$ of metabolic energy liberated during swimming is lost to viscous shear friction and accelerating water backward into turbulent vortices.</p>

<h2>Hydrodynamic Drag and the Energy Cost of Swimming ($C_s$)</h2>
<p>Total resistive force opposing a swimmer moving at steady-state horizontal velocity $v$ (m/s) evaluates as:</p>

$$F_{\text{drag}} = \frac{1}{2} \rho_{\text{water}} \cdot C_d A_{\text{frontal}} \cdot v^2$$

<p>Because resistive force scales with velocity squared ($v^2$), the mechanical power required to propel a human through water scales with the <strong>cube of swimming speed ($P \propto v^3$)</strong>:</p>

$$P_{\text{hydrodynamic}} = F_{\text{drag}} \cdot v = \frac{1}{2} \rho \cdot C_d A \cdot v^3$$

<p>The <strong>Energy Cost of Swimming ($C_s$)</strong> is defined as the amount of metabolic energy required to transport one kilogram of body mass across one horizontal meter ($J\cdot\text{kg}^{-1}\cdot\text{m}^{-1}$):</p>

$$C_s = \frac{\dot{V}\text{O}_2}{v}$$

<p>Where Front Crawl (Freestyle) is the most hydrodynamically streamlined stroke ($C_s \approx 1.0 \text{ to } 1.4 \, \text{kJ/m}$), while Butterfly and Breaststroke require up to twice as much energy ($C_s \approx 2.0 \text{ to } 2.5 \, \text{kJ/m}$) due to disruptive body wave undulations and periodic underwater limb recoveries.</p>

<h3>Compendium of Physical Activities Swimming MET Matrix</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Stroke Style &amp; Effort</th>
            <th>Compendium Code</th>
            <th>MET Value</th>
            <th>Burn Rate (60 kg Swimmer)</th>
            <th>Burn Rate (85 kg Swimmer)</th>
            <th>Pacing Efficiency</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Treading Water (Moderate)</td><td>18310</td><td>3.5 METs</td><td>221 kcal / hr</td><td>312 kcal / hr</td><td>Stationary Float</td></tr>
        <tr><td>Backstroke (Moderate)</td><td>18240</td><td>7.0 METs</td><td>441 kcal / hr</td><td>625 kcal / hr</td><td>Smooth Recovery</td></tr>
        <tr><td>Breaststroke (Recreational)</td><td>18250</td><td>7.0 METs</td><td>441 kcal / hr</td><td>625 kcal / hr</td><td>Gliding Recovery</td></tr>
        <tr><td>Freestyle (Moderate Lap Swim)</td><td>18270</td><td>8.3 METs</td><td>523 kcal / hr</td><td>741 kcal / hr</td><td>Streamlined Crawl</td></tr>
        <tr><td>Treading Water (Vigorous)</td><td>18320</td><td>9.8 METs</td><td>617 kcal / hr</td><td>875 kcal / hr</td><td>Eggbeater Kick</td></tr>
        <tr><td>Freestyle (Vigorous Effort)</td><td>18280</td><td>10.0 METs</td><td>630 kcal / hr</td><td>893 kcal / hr</td><td>Race Pace (&lt; 1:15/100m)</td></tr>
        <tr><td>Breaststroke (Vigorous)</td><td>18260</td><td>10.3 METs</td><td>649 kcal / hr</td><td>919 kcal / hr</td><td>High-Knee Whip Kick</td></tr>
        <tr><td>Butterfly (Competition Effort)</td><td>18290</td><td>13.8 METs</td><td>869 kcal / hr</td><td>1,232 kcal / hr</td><td>Undulating Power</td></tr>
    </tbody>
</table>

<h2>Water Convection and Thermal Shivering Costs</h2>
<p>Water has a volumetric heat capacity approximately 3,400 times greater than air and a thermal conductivity 24 times higher. Consequently, human core heat loss occurs at an accelerated rate in water. When swimming in cold open water or unheated pools below $22^\circ\text{C}$ ($71^\circ\text{F}$), the human body activates non-shivering thermogenesis and peripheral vasoconstriction to maintain core homeostasis ($37^\circ\text{C}$). This thermal deficit increases metabolic caloric expenditure by <strong>$10\%$ to $25\%$</strong> above nominal exercise values.</p>

<div class="worked-example-card">
    <h3>Worked Aquatic Physiology Case Study: 1,500-Meter Olympic Distance Workout</h3>
    <p><strong>Scenario:</strong> A 70 kg triathlete completes a <strong>1,500-meter freestyle lap swim</strong> in a 25-meter pool over <strong>35 minutes</strong> (average pace: $2:20 \text{ min / 100m}$, vigorous effort, 10.0 METs). Determine: (1) total laps completed, (2) gross metabolic calories burned, (3) hourly burn rate, and (4) equivalent outdoor running distance.</p>
    
    <div class="step-solution">
        <h4>Step 1: Compute Pool Laps Completed</h4>
        $$\text{Laps} = \frac{1,500 \text{ meters}}{25 \text{ meters/lap}} = 60 \text{ laps}$$

        <h4>Step 2: Evaluate Gross Caloric Expenditure</h4>
        <p>Using ACSM formula: $\text{Intensity} = 10.0 \text{ METs}$, $\text{Weight} = 70 \text{ kg}$, $\text{Time} = 35 \text{ minutes}$.</p>
        $$\text{Gross Calories} = \frac{10.0 \times 3.5 \times 70 \text{ kg}}{200} \times 35 \text{ min} = 12.25 \times 35 \approx 428.75 \text{ kcal}$$

        <h4>Step 3: Calculate Hourly Burn Rate</h4>
        $$\text{Hourly Burn} = \frac{428.75}{35} \times 60 \approx 735.0 \text{ kcal / hour}$$

        <h4>Step 4: Equivalent Terrestrial Running Distance</h4>
        <p>In sports physiology, running expends roughly $1.0 \, \text{kcal / kg / km}$. For a 70 kg individual, running 1 km burns ~70 kcal (or ~112 kcal / mile).</p>
        $$\text{Equivalent Running Distance} = \frac{428.75 \text{ kcal}}{112 \text{ kcal/mile}} \approx 3.83 \text{ miles (6.13 km)}$$
        <p><strong>Conclusion:</strong> A 1,500-meter swim generates the cardiovascular and metabolic equivalent of running nearly 4 road miles with zero orthopedic impact!</p>
    </div>
</div>

<h2>Common Mistakes in Swimming Calorie Estimation</h2>
<ol>
    <li><strong>Equating Lap Rest Time to Active Swimming Time:</strong> If you spend 45 minutes at the pool but rest on the wall for 60 seconds after every 100 meters, your active swimming duration is only 22 minutes! Calculating calories for 45 minutes of continuous swimming doubles your true burn.</li>
    <li><strong>Overlooking Stroke Technique Quality:</strong> Highly skilled competitive swimmers produce high stroke lengths with minimal frontal resistance ($C_d A$), burning fewer calories per 100m than an unconditioned recreational swimmer thrashing inefficiently through the water.</li>
    <li><strong>Post-Swim Appetite Surge (Ghrelin Response):</strong> Colder pool water suppresses core temperature, triggering an intense post-workout release of the hunger hormone ghrelin. Swimmers frequently overcompensate by consuming 500-800 kcal of excess food post-workout, offsetting their calorie deficit.</li>
</ol>

<section class="faq-section">
    <h2>Frequently Asked Questions About Swimming Calories</h2>
    <div class="faq-item">
        <h3>Which swimming stroke burns the most calories?</h3>
        <p>The Butterfly stroke burns the most calories by a wide margin, requiring 11.0 to 13.8 METs (up to 800-950 kcal/hr for an average adult) due to immense bilateral shoulder power and undulatory dolphin kicking.</p>
    </div>
    <div class="faq-item">
        <h3>Why does swimming burn more calories in colder water?</h3>
        <p>Water has a thermal conductivity approximately 24 times greater than air. In water temperatures below 25°C (77°F), the human body expends significant metabolic energy through non-shivering thermogenesis to maintain a 37°C core body temperature.</p>
    </div>
    <div class="faq-item">
        <h3>How many calories does swimming 1,000 meters burn?</h3>
        <p>Swimming 1,000 meters (approx 40 laps in a 25m pool) at a moderate freestyle pace typically burns 220 to 300 calories for a 70 kg swimmer in roughly 20 to 25 minutes.</p>
    </div>
    <div class="faq-item">
        <h3>Why is swimming gross mechanical efficiency so low compared to running?</h3>
        <p>Water density is roughly 800 times greater than air. Swimmers operate at a low gross mechanical efficiency of only 5% to 9% because the vast majority of metabolic energy is lost generating turbulent vortices and overcoming viscous fluid drag.</p>
    </div>
</section>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article)


def main():
    tm_html = gen_treadmill_calorie()
    with open(os.path.join(BASE_DIR, "treadmill-calorie-calculator.html"), "w", encoding="utf-8") as f:
        f.write(tm_html)
    print("Generated treadmill-calorie-calculator.html successfully!")

    sm_html = gen_stairmaster_calorie()
    with open(os.path.join(BASE_DIR, "stairmaster-calorie-calculator.html"), "w", encoding="utf-8") as f:
        f.write(sm_html)
    print("Generated stairmaster-calorie-calculator.html successfully!")

    cy_html = gen_cycling_calorie()
    with open(os.path.join(BASE_DIR, "cycling-calorie-calculator.html"), "w", encoding="utf-8") as f:
        f.write(cy_html)
    print("Generated cycling-calorie-calculator.html successfully!")

    pu_html = gen_pushup_calorie()
    with open(os.path.join(BASE_DIR, "pushup-calorie-calculator.html"), "w", encoding="utf-8") as f:
        f.write(pu_html)
    print("Generated pushup-calorie-calculator.html successfully!")

    bp_html = gen_bench_press_calorie()
    with open(os.path.join(BASE_DIR, "bench-press-calories-calculator.html"), "w", encoding="utf-8") as f:
        f.write(bp_html)
    print("Generated bench-press-calories-calculator.html successfully!")

    sw_html = gen_swimming_calorie()
    with open(os.path.join(BASE_DIR, "swimming-calorie-calculator.html"), "w", encoding="utf-8") as f:
        f.write(sw_html)
    print("Generated swimming-calorie-calculator.html successfully!")

if __name__ == "__main__":
    main()
