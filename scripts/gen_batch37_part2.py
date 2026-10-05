# -*- coding: utf-8 -*-
"""
Generator for Batch 37 - Part 2
Tools:
3. motor-starter-sizing-calculator.html
4. nec-load-calculation-calculator.html
"""

import os

COMMON_TAIL = """    <footer class="site-footer">
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>About CalcHub</h4>
                    <p>CalcHub provides free, high-precision engineering calculators, unit converters, and analytical tools designed for practicing engineers, electricians, and contractors worldwide.</p>
                </div>
                <div class="footer-col">
                    <h4>Engineering Categories</h4>
                    <ul>
                        <li><a href="engineering.html">Electrical &amp; Electronics</a></li>
                        <li><a href="mechanical.html">Mechanical &amp; HVAC</a></li>
                        <li><a href="civil.html">Civil &amp; Structural</a></li>
                        <li><a href="chemical.html">Chemical &amp; Process</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Popular Calculators</h4>
                    <ul>
                        <li><a href="wire-ampacity-calculator.html">Wire Ampacity</a></li>
                        <li><a href="voltage-drop-calculator.html">Voltage Drop</a></li>
                        <li><a href="conduit-fill-calculator.html">Conduit Fill</a></li>
                        <li><a href="3-phase-power-calculator.html">3-Phase Power</a></li>
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

def get_page_html(title, description, canonical_slug, schema_json, h1, short_desc, calc_ui, article_content, category_hub="engineering.html", category_name="Engineering"):
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
                    <h3>Related Electrical Tools</h3>
                    <ul class="sidebar-links">
                        <li><a href="motor-starter-sizing-calculator.html">Motor Starter Sizing</a></li>
                        <li><a href="nec-load-calculation-calculator.html">NEC Load Calculation</a></li>
                        <li><a href="3-phase-power-calculator.html">3-Phase Power Calculator</a></li>
                        <li><a href="wire-ampacity-calculator.html">Wire Ampacity</a></li>
                        <li><a href="voltage-drop-calculator.html">Voltage Drop</a></li>
                        <li><a href="conduit-fill-calculator.html">Conduit Fill</a></li>
                        <li><a href="motor-parameters-calculator.html">Motor Parameters</a></li>
                        <li><a href="buck-boost-converter-calculator.html">Buck-Boost Converter</a></li>
                        <li><a href="short-circuit-current-calculator.html">Short Circuit Current</a></li>
                        <li><a href="grounding-electrode-conductor-calculator.html">Grounding Conductor</a></li>
                    </ul>
                </div>
            </aside>
        </div>
    </div>
{COMMON_TAIL}"""


# ---------------------------------------------------------------------------
# Tool 3: Motor Starter Sizing Calculator
# ---------------------------------------------------------------------------
def gen_motor_starter():
    slug = "motor-starter-sizing-calculator"
    title = "Motor Starter Sizing Calculator | NEMA, IEC, Overload & Breaker Ratings"
    desc = "Size 3-phase induction motor starters, NEMA contactor sizes, IEC AC-3 ratings, thermal overload relay settings, and branch circuit breaker/fuse protection per NEC Article 430."
    h1 = "Motor Starter Sizing Calculator"
    short_desc = "Calculate NEMA starter sizes, IEC contactor ratings, thermal overload settings, conductor ampacity, and circuit breaker sizing for 3-phase electric motors."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Motor Starter Sizing Calculator",
      "url": "https://calchub.com/motor-starter-sizing-calculator.html",
      "applicationCategory": "EngineeringApplication",
      "operatingSystem": "All",
      "description": "Calculate NEMA and IEC motor starter sizes, branch circuit conductor ampacity, thermal overload relay trip ratings, and breaker or fuse sizing per NEC Article 430.",
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
          "name": "What is the difference between NEMA and IEC motor starter sizing philosophies?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "NEMA starters are designed with heavy thermal mass and generous service margins, sized by standardized NEMA Sizes (Size 00 up to Size 9) to withstand frequent jogging, plugging, and heavy overloads across a broad horsepower spectrum. IEC contactors are application-tailored, engineered compactly based on exact motor full-load amperes (FLA), operating duty cycles, and utilization categories (AC-3 or AC-4) with little overdesign margin."
          }
        },
        {
          "@type": "Question",
          "name": "How is branch circuit conductor ampacity sized for electric motors under NEC Article 430?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Per NEC Section 430.22, conductors supplying a single continuous-duty motor must have an ampacity rating of not less than 125% of the motor full-load current (FLA) listed in NEC Tables 430.247 through 430.250, rather than the motor nameplate rating."
          }
        },
        {
          "@type": "Question",
          "name": "How do you select the thermal overload relay setting for an electric motor?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Per NEC 430.32, for motors with a marked service factor (SF) of 1.15 or greater, or marked temperature rise not over 40°C, the overload device is sized to trip at not more than 125% of nameplate full-load current. For all other motors with SF 1.0, the overload trip rating must not exceed 115% of nameplate FLA."
          }
        },
        {
          "@type": "Question",
          "name": "Why can an inverse-time circuit breaker be sized up to 250% of motor FLA?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Electric motors draw a high inrush current (locked rotor current, typically 600% of FLA) during across-the-line starting. To prevent nuisance tripping during motor acceleration while relying on the thermal overload relay to protect against running overloads, NEC Table 430.52 allows inverse-time circuit breakers to be sized up to 250% of FLA (or up to 400% if the motor fails to start without tripping)."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calculator-form">
    <div class="calc-row">
        <div class="calc-field">
            <label for="ms_hp">Motor Rated Power (HP):</label>
            <select id="ms_hp">
                <option value="1">1 HP</option>
                <option value="1.5">1.5 HP</option>
                <option value="2">2 HP</option>
                <option value="3">3 HP</option>
                <option value="5">5 HP</option>
                <option value="7.5">7.5 HP</option>
                <option value="10" selected>10 HP</option>
                <option value="15">15 HP</option>
                <option value="20">20 HP</option>
                <option value="25">25 HP</option>
                <option value="30">30 HP</option>
                <option value="40">40 HP</option>
                <option value="50">50 HP</option>
                <option value="60">60 HP</option>
                <option value="75">75 HP</option>
                <option value="100">100 HP</option>
            </select>
        </div>
        <div class="calc-field">
            <label for="ms_voltage">System Voltage (V):</label>
            <select id="ms_voltage">
                <option value="208">208 V (3-Phase)</option>
                <option value="230">230 V / 240 V (3-Phase)</option>
                <option value="460" selected>460 V / 480 V (3-Phase)</option>
                <option value="575">575 V / 600 V (3-Phase)</option>
            </select>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="ms_sf">Motor Service Factor (SF):</label>
            <select id="ms_sf">
                <option value="1.15" selected>1.15 or greater (Standard industrial)</option>
                <option value="1.0">1.00 (Standard duty / Inverter duty)</option>
            </select>
        </div>
        <div class="calc-field">
            <label for="ms_start_method">Starting Method:</label>
            <select id="ms_start_method">
                <option value="dol" selected>Across-The-Line (DOL / Direct-On-Line)</option>
                <option value="star_delta">Star-Delta (Wye-Delta Starter)</option>
                <option value="soft_start">Solid-State Soft Starter</option>
            </select>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="ms_ocpd_type">Short-Circuit Protective Device (OCPD):</label>
            <select id="ms_ocpd_type">
                <option value="it_cb" selected>Inverse-Time Circuit Breaker (250% max)</option>
                <option value="td_fuse">Dual-Element Time-Delay Fuse (175% max)</option>
                <option value="ntd_fuse">Non-Time Delay Fuse (300% max)</option>
                <option value="mcp">Instantaneous Trip / MCP (800% max)</option>
            </select>
        </div>
        <div class="calc-field">
            <label for="ms_custom_fla">Custom FLA Override (Optional):</label>
            <input type="number" id="ms_custom_fla" placeholder="Leave blank to use NEC Table 430.250" step="0.1" min="0.5">
            <small class="field-hint">Actual motor nameplate amperes if known</small>
        </div>
    </div>
    <button type="button" class="btn btn-primary" id="btn_calc_ms" style="width:100%; margin-top:1rem;">Calculate Motor Starter &amp; Protection Ratings</button>

    <div class="calc-results" id="ms_results" style="margin-top:1.5rem;">
        <h3>NEC / NEMA Motor Sizing Output</h3>
        <div class="results-grid">
            <div class="result-item">
                <span class="result-label">Motor Full Load Current (FLA):</span>
                <span class="result-value" id="res_ms_fla">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Min Conductor Ampacity (125%):</span>
                <span class="result-value" id="res_ms_conductor">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Overload Relay Max Setting:</span>
                <span class="result-value" id="res_ms_ol">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Max OCPD / Breaker Rating:</span>
                <span class="result-value" id="res_ms_ocpd">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Standard Next Standard Breaker/Fuse:</span>
                <span class="result-value" id="res_ms_std_ocpd">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Recommended NEMA Starter Size:</span>
                <span class="result-value" id="res_ms_nema">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Minimum IEC AC-3 Contactor Rating:</span>
                <span class="result-value" id="res_ms_iec">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Disconnect Switch Min Rating:</span>
                <span class="result-value" id="res_ms_disc">--</span>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    // NEC Table 430.250 Full Load Current in Amperes for 3-Phase AC Induction Motors
    const necTable430_250 = {
        '1':   {'208': 4.0,  '230': 3.6,  '460': 1.8,  '575': 1.4},
        '1.5': {'208': 5.7,  '230': 5.2,  '460': 2.6,  '575': 2.1},
        '2':   {'208': 7.5,  '230': 6.8,  '460': 3.4,  '575': 2.7},
        '3':   {'208': 10.6, '230': 9.6,  '460': 4.8,  '575': 3.9},
        '5':   {'208': 16.7, '230': 15.2, '460': 7.6,  '575': 6.1},
        '7.5': {'208': 24.2, '230': 22.0, '460': 11.0, '575': 9.0},
        '10':  {'208': 30.8, '230': 28.0, '460': 14.0, '575': 11.0},
        '15':  {'208': 46.2, '230': 42.0, '460': 21.0, '575': 17.0},
        '20':  {'208': 59.4, '230': 54.0, '460': 27.0, '575': 22.0},
        '25':  {'208': 74.8, '230': 68.0, '460': 34.0, '575': 27.0},
        '30':  {'208': 88.0, '230': 80.0, '460': 40.0, '575': 32.0},
        '40':  {'208': 114,  '230': 104,  '460': 52.0, '575': 41.0},
        '50':  {'208': 143,  '230': 130,  '460': 65.0, '575': 52.0},
        '60':  {'208': 169,  '230': 154,  '460': 77.0, '575': 62.0},
        '75':  {'208': 211,  '230': 192,  '460': 96.0, '575': 77.0},
        '100': {'208': 273,  '230': 248,  '460': 124,  '575': 99.0}
    };

    // Standard fuse / breaker sizes per NEC 240.6(A)
    const standardOcpdSizes = [15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 125, 150, 175, 200, 225, 250, 300, 350, 400, 450, 500, 600];

    function calculateMotorStarter() {
        const hpStr = document.getElementById('ms_hp').value;
        const vStr = document.getElementById('ms_voltage').value;
        const sf = parseFloat(document.getElementById('ms_sf').value) || 1.15;
        const startMethod = document.getElementById('ms_start_method').value;
        const ocpdType = document.getElementById('ms_ocpd_type').value;
        const customFla = parseFloat(document.getElementById('ms_custom_fla').value);

        let fla = (customFla && !isNaN(customFla)) ? customFla : necTable430_250[hpStr][vStr];

        // 1. Minimum conductor ampacity: 125% of FLA (NEC 430.22)
        const conductorAmp = fla * 1.25;

        // 2. Overload protection setting (NEC 430.32)
        const olMultiplier = (sf >= 1.15) ? 1.25 : 1.15;
        const olMax = fla * olMultiplier;

        // 3. Short circuit protection maximum rating (NEC Table 430.52)
        let ocpdMultiplier = 2.50; // default inverse time
        if (ocpdType === 'it_cb') ocpdMultiplier = 2.50;
        else if (ocpdType === 'td_fuse') ocpdMultiplier = 1.75;
        else if (ocpdType === 'ntd_fuse') ocpdMultiplier = 3.00;
        else if (ocpdType === 'mcp') ocpdMultiplier = 8.00;

        const maxOcpdCalc = fla * ocpdMultiplier;

        // Standard next size down or up per NEC 430.52(C)(1) Exception 1 (allows next higher standard size)
        let standardOcpd = standardOcpdSizes[0];
        for (let i = 0; i < standardOcpdSizes.length; i++) {
            if (standardOcpdSizes[i] <= maxOcpdCalc) {
                standardOcpd = standardOcpdSizes[i];
            } else {
                // Next standard size up allowed by exception
                standardOcpd = standardOcpdSizes[i];
                break;
            }
        }

        // 4. NEMA Starter Size mapping based on continuous amperes and voltage
        let nemaSize = "Size 00 (9A)";
        const hp = parseFloat(hpStr);
        const v = parseFloat(vStr);
        if (v === 460 || v === 575) {
            if (hp <= 2) nemaSize = "NEMA Size 00 (9A)";
            else if (hp <= 5) nemaSize = "NEMA Size 0 (18A)";
            else if (hp <= 10) nemaSize = "NEMA Size 1 (27A)";
            else if (hp <= 25) nemaSize = "NEMA Size 2 (45A)";
            else if (hp <= 50) nemaSize = "NEMA Size 3 (90A)";
            else if (hp <= 100) nemaSize = "NEMA Size 4 (135A)";
            else nemaSize = "NEMA Size 5 (270A)";
        } else {
            // 208V / 230V
            if (hp <= 1.5) nemaSize = "NEMA Size 00 (9A)";
            else if (hp <= 3) nemaSize = "NEMA Size 0 (18A)";
            else if (hp <= 7.5) nemaSize = "NEMA Size 1 (27A)";
            else if (hp <= 15) nemaSize = "NEMA Size 2 (45A)";
            else if (hp <= 30) nemaSize = "NEMA Size 3 (90A)";
            else if (hp <= 50) nemaSize = "NEMA Size 4 (135A)";
            else nemaSize = "NEMA Size 5 (270A)";
        }

        // 5. IEC AC-3 contactor rating
        // AC-3 category handles squirrel cage motors with starting and breaking during normal run
        let iecRating = Math.ceil(fla * 1.15) + ' A (AC-3 continuous)';

        // 6. Disconnect switch: 115% minimum of FLA (NEC 430.110)
        const discRating = (fla * 1.15).toFixed(1) + ' A (Min HP rated)';

        document.getElementById('res_ms_fla').textContent = fla.toFixed(1) + ' A';
        document.getElementById('res_ms_conductor').textContent = conductorAmp.toFixed(1) + ' A';
        document.getElementById('res_ms_ol').textContent = olMax.toFixed(1) + ' A (' + (olMultiplier * 100) + '%)';
        document.getElementById('res_ms_ocpd').textContent = maxOcpdCalc.toFixed(1) + ' A (' + (ocpdMultiplier * 100) + '%)';
        document.getElementById('res_ms_std_ocpd').textContent = standardOcpd + ' A Standard';
        document.getElementById('res_ms_nema').textContent = nemaSize;
        document.getElementById('res_ms_iec').textContent = iecRating;
        document.getElementById('res_ms_disc').textContent = discRating;
    }

    document.getElementById('btn_calc_ms').addEventListener('click', calculateMotorStarter);
    document.getElementById('ms_hp').addEventListener('change', calculateMotorStarter);
    document.getElementById('ms_voltage').addEventListener('change', calculateMotorStarter);
    calculateMotorStarter();
});
</script>"""

    article_content = """<h2>1. Industrial Electric Motor Circuit Architecture &amp; NEC Article 430</h2>
<p>Electric motors represent the primary consumer of industrial electrical energy globally. Unlike static resistive heating or lighting loads, electric motors exhibit dynamic electrical properties: during initial across-the-line start-up, a stationary induction motor rotor presents almost zero back-electromotive force (back-EMF), drawing an instantaneous locked-rotor inrush current (\(LRA\)) between 600% and 800% of its rated Full-Load Amperes (\(FLA\)).</p>

<p>To safely manage these severe transient currents without causing spurious breaker trips while guaranteeing robust protection against mechanical stall, prolonged overloads, and destructive line-to-ground or phase-to-phase short circuits, the National Electrical Code (NEC Article 430) separates motor branch circuit protection into two independent functional elements:</p>
<ul>
    <li><strong>Motor Running Overload Protection (NEC Part III):</strong> Thermal or electronic overload relays calibrated to protect motor windings, bearings, and branch wiring against gradual thermal deterioration caused by mechanical overloads or low voltage.</li>
    <li><strong>Branch-Circuit Short-Circuit and Ground-Fault Protection (NEC Part IV):</strong> Fuses or magnetic/inverse-time circuit breakers sized specifically to clear catastrophic short-circuit faults instantly, while having sufficient time-delay to allow normal motor starting inrush without opening.</li>
</ul>

<h2>2. Governing Code Formulations &amp; Component Sizing Rules</h2>
<p>All calculations governing motor branch circuits begin with determining the table full-load current (\(FLA\)) from <strong>NEC Table 430.250</strong> (Three-Phase AC Motors) rather than using the motor nameplate current (NEC Section 430.6(A)(1)):</p>

<h3>Branch Circuit Conductor Ampacity</h3>
<p>Per NEC Section 430.22, conductors supplying a single continuous-duty electric motor must possess an allowable ampacity rating of not less than 125% of the motor full-load current:</p>

$$I_{conductor} \ge 1.25 \times I_{FLA}$$

<h3>Motor Overload Protection (Thermal Relay)</h3>
<p>Unlike conductor sizing which references NEC tables, the thermal overload relay heater or solid-state electronic overload trip threshold is set using the <strong>actual nameplate current</strong> marked on the motor data plate (NEC Section 430.32):</p>

$$I_{OL,max} \le \begin{cases} 1.25 \times I_{nameplate} & \text{for motors with Service Factor } (SF) \ge 1.15 \text{ or temp rise } \le 40^\circ\text{C} \\ 1.15 \times I_{nameplate} & \text{for all other motors with } SF = 1.00 \end{cases}$$

<h3>Short-Circuit &amp; Ground-Fault Protective Device (OCPD)</h3>
<p>Per NEC Section 430.52 and Table 430.52, the maximum permissible rating or setting of the branch-circuit protective device is calculated by applying the designated percentage multiplier:</p>

$$I_{OCPD,max} \le M_{device} \times I_{FLA}$$

<p>where \(M_{device}\) is established by device technology:</p>
<ul>
    <li><strong>Non-Time Delay Fuse:</strong> \(300\%\) (\(3.00 \times FLA\))</li>
    <li><strong>Dual-Element (Time-Delay) Fuse:</strong> \(175\%\) (\(1.75 \times FLA\))</li>
    <li><strong>Inverse Time Circuit Breaker:</strong> \(250\%\) (\(2.50 \times FLA\))</li>
    <li><strong>Instantaneous Trip Circuit Breaker (Motor Circuit Protector / MCP):</strong> \(800\%\) (\(8.00 \times FLA\))</li>
</ul>

<p>Per NEC 430.52(C)(1) Exception 1, if the calculated value does not correspond to a standard ampere rating listed in NEC Section 240.6(A), the next higher standard rating is permitted. Furthermore, if the motor cannot accelerate to rated speed without opening the breaker during starting, the rating of an inverse-time circuit breaker may be increased up to a statutory maximum of <strong>400% of FLA</strong> for motors rated 100A or less (NEC 430.52(C)(1) Exception 2).</p>

<h2>3. NEMA vs. IEC Starter Sizing Standard Comparison Table</h2>
<p>The following engineering data table contrasts standardized NEMA motor starter frame sizes against international IEC contactor utilization standards across standard three-phase industrial operating voltages:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>NEMA Size</th>
            <th>Continuous Current (A)</th>
            <th>Max HP @ 208V</th>
            <th>Max HP @ 230V</th>
            <th>Max HP @ 460V</th>
            <th>Max HP @ 575V</th>
            <th>Typical IEC AC-3 Equivalent</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Size 00</strong></td>
            <td>9 A</td>
            <td>1.5 HP</td>
            <td>1.5 HP</td>
            <td>2 HP</td>
            <td>2 HP</td>
            <td>9 A – 12 A (LC1D09)</td>
        </tr>
        <tr>
            <td><strong>Size 0</strong></td>
            <td>18 A</td>
            <td>3 HP</td>
            <td>3 HP</td>
            <td>5 HP</td>
            <td>5 HP</td>
            <td>18 A – 25 A (LC1D18)</td>
        </tr>
        <tr>
            <td><strong>Size 1</strong></td>
            <td>27 A</td>
            <td>7.5 HP</td>
            <td>7.5 HP</td>
            <td>10 HP</td>
            <td>10 HP</td>
            <td>25 A – 32 A (LC1D25)</td>
        </tr>
        <tr>
            <td><strong>Size 2</strong></td>
            <td>45 A</td>
            <td>10 HP</td>
            <td>15 HP</td>
            <td>25 HP</td>
            <td>25 HP</td>
            <td>40 A – 50 A (LC1D40)</td>
        </tr>
        <tr>
            <td><strong>Size 3</strong></td>
            <td>90 A</td>
            <td>25 HP</td>
            <td>30 HP</td>
            <td>50 HP</td>
            <td>50 HP</td>
            <td>65 A – 95 A (LC1D80)</td>
        </tr>
        <tr>
            <td><strong>Size 4</strong></td>
            <td>135 A</td>
            <td>40 HP</td>
            <td>50 HP</td>
            <td>100 HP</td>
            <td>100 HP</td>
            <td>115 A – 150 A (LC1D115)</td>
        </tr>
        <tr>
            <td><strong>Size 5</strong></td>
            <td>270 A</td>
            <td>75 HP</td>
            <td>100 HP</td>
            <td>200 HP</td>
            <td>200 HP</td>
            <td>225 A – 300 A (LC1F225)</td>
        </tr>
    </tbody>
</table>

<h2>4. Overload Relay Trip Class Selection (Class 10, 20, and 30)</h2>
<p>Thermal and electronic overload relays feature defined <strong>Trip Class</strong> ratings per NEMA ICS 2 and UL 508. The trip class specifies the maximum time in seconds the overload mechanism will take to trip when subjected to a locked-rotor current of exactly 600% of its rated current setting:</p>
<ul>
    <li><strong>Class 10 (Trips within 10 seconds):</strong> Mandatory for fast-heating submersible pumps, hermetic HVAC refrigeration compressors, and high-efficiency inverter-duty motors with low thermal withstand capability.</li>
    <li><strong>Class 20 (Trips within 20 seconds):</strong> The industrial workhorse standard, selected for general-purpose centrifugal fans, conveyors, compressors, and standard factory machinery.</li>
    <li><strong>Class 30 (Trips within 30 seconds):</strong> Engineered for extreme high-inertia starting loads, such as large centrifugal blowers, hammer mills, rock crushers, and ball pulverizers that require extended acceleration times exceeding 15 seconds.</li>
</ul>

<h2>5. Worked Engineering Case Study: 460V 10 HP Water Pump Motor</h2>
<div class="worked-example-card">
    <h3>Design Specification: 10 HP Chilled Water Circulation Pump</h3>
    <p>A central mechanical plant installs a 10 HP, 3-phase, 460V squirrel-cage induction motor driving a chilled water circulation pump. The motor data nameplate indicates: <strong>HP = 10</strong>, <strong>Volts = 460V</strong>, <strong>Service Factor = 1.15</strong>, <strong>Nameplate Amperes = 13.5 A</strong>. The branch circuit uses an Inverse-Time thermal-magnetic circuit breaker in an industrial motor control center (MCC).</p>

    <div class="step-solution">
        <h4>Step 1: Determine Full Load Current (FLA) from NEC Table 430.250</h4>
        <p>Consulting NEC Table 430.250 for a 10 HP, 460V 3-phase induction motor gives:</p>
        $$I_{FLA} = 14.0\text{ A}$$
        <p><em>(Note: All conductor and circuit breaker sizing must reference the 14.0A NEC table value, not the 13.5A nameplate value).</em></p>

        <h4>Step 2: Calculate Minimum Branch Conductor Ampacity</h4>
        $$I_{conductor} = 1.25 \times I_{FLA} = 1.25 \times 14.0\text{ A} = 17.5\text{ A}$$
        <p>Referencing NEC Table 310.16 (copper conductor, 75°C THHN terminal rating), a <strong>#14 AWG copper conductor</strong> is rated for 20A, but per standard commercial engineering practice and terminal compatibility, a <strong>#12 AWG THHN copper wire</strong> (rated 25A) is selected.</p>

        <h4>Step 3: Size the Thermal Overload Relay</h4>
        <p>Because the motor exhibits a Service Factor \(SF = 1.15\), the maximum allowable overload relay setting (NEC 430.32) is:</p>
        $$I_{OL,max} = 1.25 \times I_{nameplate} = 1.25 \times 13.5\text{ A} = 16.88\text{ A}$$
        <p>An electronic overload relay adjustable over 10A to 20A is dialed to 13.5A nominal and configured for Class 20 tripping.</p>

        <h4>Step 4: Size the Inverse-Time Circuit Breaker</h4>
        <p>Per NEC Table 430.52, the maximum multiplier for an inverse-time circuit breaker is 250%:</p>
        $$I_{CB,max} = 2.50 \times I_{FLA} = 2.50 \times 14.0\text{ A} = 35.0\text{ A}$$
        <p>Per NEC Section 240.6(A), 35A is a standard breaker rating. Therefore, a <strong>3-Pole 35A Inverse-Time Circuit Breaker</strong> is specified.</p>

        <h4>Step 5: Determine Starter Size and Disconnect Rating</h4>
        <p>From the NEMA Starter Rating Table, a 10 HP motor at 460V requires a <strong>NEMA Size 1 Starter</strong> (continuous rating 27A). For an IEC design, an <strong>IEC AC-3 contactor rated for 18A or 25A</strong> (such as Schneider Electric LC1D18 or LC1D25) is selected. The disconnect switch rating (NEC 430.110) must be at least \(1.15 \times 14.0\text{ A} = 16.1\text{ A}\) with a 10 HP horsepower rating.</p>
    </div>
</div>

<h2>6. Frequently Asked Questions</h2>
<div class="faq-accordion">
    <div class="faq-item">
        <h3>What is the difference between NEMA and IEC motor starter sizing philosophies?</h3>
        <p>NEMA starters are designed with heavy thermal mass and generous service margins, sized by standardized NEMA Sizes (Size 00 up to Size 9) to withstand frequent jogging, plugging, and heavy overloads across a broad horsepower spectrum. IEC contactors are application-tailored, engineered compactly based on exact motor full-load amperes (FLA), operating duty cycles, and utilization categories (AC-3 or AC-4) with little overdesign margin.</p>
    </div>
    <div class="faq-item">
        <h3>How is branch circuit conductor ampacity sized for electric motors under NEC Article 430?</h3>
        <p>Per NEC Section 430.22, conductors supplying a single continuous-duty motor must have an ampacity rating of not less than 125% of the motor full-load current (FLA) listed in NEC Tables 430.247 through 430.250, rather than the motor nameplate rating.</p>
    </div>
    <div class="faq-item">
        <h3>How do you select the thermal overload relay setting for an electric motor?</h3>
        <p>Per NEC 430.32, for motors with a marked service factor (SF) of 1.15 or greater, or marked temperature rise not over 40°C, the overload device is sized to trip at not more than 125% of nameplate full-load current. For all other motors with SF 1.0, the overload trip rating must not exceed 115% of nameplate FLA.</p>
    </div>
    <div class="faq-item">
        <h3>Why can an inverse-time circuit breaker be sized up to 250% of motor FLA?</h3>
        <p>Electric motors draw a high inrush current (locked rotor current, typically 600% of FLA) during across-the-line starting. To prevent nuisance tripping during motor acceleration while relying on the thermal overload relay to protect against running overloads, NEC Table 430.52 allows inverse-time circuit breakers to be sized up to 250% of FLA (or up to 400% if the motor fails to start without tripping).</p>
    </div>
</div>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article_content)


# ---------------------------------------------------------------------------
# Tool 4: NEC Load Calculation Calculator
# ---------------------------------------------------------------------------
def gen_nec_load():
    slug = "nec-load-calculation-calculator"
    title = "NEC Load Calculation Calculator | Residential Electrical Service Sizing"
    desc = "Calculate total dwelling electrical service load, service entrance conductor ampacity, and minimum panel rating per NEC Article 220 Standard and Optional Methods."
    h1 = "NEC Load Calculation Calculator"
    short_desc = "Size single-phase 120/240V residential electrical services, main breaker ampacity, and service entrance conductors using NEC Article 220 demand factor rules."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "NEC Load Calculation Calculator",
      "url": "https://calchub.com/nec-load-calculation-calculator.html",
      "applicationCategory": "EngineeringApplication",
      "operatingSystem": "All",
      "description": "Calculate residential electrical service sizing, general lighting load, appliance demand factors, and minimum service panel breaker rating per NEC Article 220.",
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
          "name": "What is the difference between NEC Article 220 Part III (Standard) and Part IV (Optional) calculation methods?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The Standard Method (Part III) applies distinct demand factor schedules to each individual load category: lighting (NEC Table 220.42), electric ranges (Table 220.55), clothes dryers (Table 220.54), and fixed appliances (75% for 4+ appliances). The Optional Method (NEC Section 220.82) simplifies this for single-family homes with 100A+ service: all non-HVAC general loads are totaled, the first 10,000 VA is taken at 100%, the remainder at 40%, and the largest HVAC load (AC vs heating) is added."
          }
        },
        {
          "@type": "Question",
          "name": "Why is general lighting calculated at 3 VA per square foot in dwelling units?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "NEC Table 220.12 mandates 3 Volt-Amperes (VA) per square foot of habitable living area. This standardized baseline accounts for all general-use illumination and general convenience receptacle outlets throughout bedrooms, living rooms, and hallways, calculated using exterior building dimensions."
          }
        },
        {
          "@type": "Question",
          "name": "How does the NEC handle coincidental Heating and Air Conditioning (HVAC) loads?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Per NEC Section 220.60 (Noncoincident Loads), where two or more dissimilar loads are unlikely to operate simultaneously—such as central air conditioning during summer and central heating during winter—only the single largest load is included in the total service calculation."
          }
        },
        {
          "@type": "Question",
          "name": "What are the standard residential electrical service sizes under modern building codes?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Modern single-family residential services are almost universally standardized at 100 Ampere (minimum code threshold per NEC 230.79), 150 Ampere, 200 Ampere (standard modern new construction), or 400 Ampere (320A continuous) for large homes with multiple electric vehicles, heat pumps, and induction ranges."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calculator-form">
    <div class="calc-row">
        <div class="calc-field">
            <label for="nec_sqft">Living Area (Square Feet):</label>
            <input type="number" id="nec_sqft" value="2400" step="50" min="200">
            <small class="field-hint">Heated/cooled area calculated from outside dimensions (3 VA/sq ft)</small>
        </div>
        <div class="calc-field">
            <label for="nec_sabc">Small Appliance &amp; Laundry Circuits:</label>
            <select id="nec_sabc">
                <option value="4500" selected>Standard: 2 Kitchen + 1 Laundry (4,500 VA)</option>
                <option value="6000">3 Kitchen + 1 Laundry (6,000 VA)</option>
                <option value="7500">4 Kitchen + 1 Laundry (7,500 VA)</option>
            </select>
            <small class="field-hint">1,500 VA per circuit per NEC 220.52</small>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="nec_range">Electric Cooking Range / Oven (VA):</label>
            <input type="number" id="nec_range" value="8000" step="500" min="0">
            <small class="field-hint">Standard residential range: 8,000 to 12,000 VA</small>
        </div>
        <div class="calc-field">
            <label for="nec_dryer">Electric Clothes Dryer (VA):</label>
            <input type="number" id="nec_dryer" value="5000" step="500" min="0">
            <small class="field-hint">Minimum 5,000 VA per NEC 220.54</small>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="nec_water_heater">Water Heater (VA):</label>
            <input type="number" id="nec_water_heater" value="4500" step="500" min="0">
            <small class="field-hint">Standard electric tank: 4,500 VA; Heat pump: 1,500 VA</small>
        </div>
        <div class="calc-field">
            <label for="nec_fixed_appliances">Other Fixed Appliances Total (VA):</label>
            <input type="number" id="nec_fixed_appliances" value="3200" step="200" min="0">
            <small class="field-hint">Dishwasher (1,200VA), Disposal (800VA), Microwave (1,200VA)</small>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="nec_ac">Air Conditioning Load (VA):</label>
            <input type="number" id="nec_ac" value="6500" step="500" min="0">
            <small class="field-hint">Central AC compressor + condenser (e.g., 3-ton = ~6,500 VA)</small>
        </div>
        <div class="calc-field">
            <label for="nec_heat">Electric Heating Load (VA):</label>
            <input type="number" id="nec_heat" value="10000" step="1000" min="0">
            <small class="field-hint">Central heat strip / resistance furnace</small>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="nec_ev">EV Charger / Dedicated Subpanel (VA):</label>
            <input type="number" id="nec_ev" value="9600" step="1000" min="0">
            <small class="field-hint">Level 2 EV Charger: 40A @ 240V = 9,600 VA (continuous @ 100%)</small>
        </div>
        <div class="calc-field">
            <label for="nec_method">NEC Calculation Standard:</label>
            <select id="nec_method">
                <option value="optional" selected>NEC 220.82 Optional Method (Recommended)</option>
                <option value="standard">NEC Part III Standard Method</option>
            </select>
        </div>
    </div>
    <button type="button" class="btn btn-primary" id="btn_calc_nec" style="width:100%; margin-top:1rem;">Calculate Electrical Service Size</button>

    <div class="calc-results" id="nec_results" style="margin-top:1.5rem;">
        <h3>Electrical Service Demand Sizing</h3>
        <div class="results-grid">
            <div class="result-item">
                <span class="result-label">General Lighting Baseline:</span>
                <span class="result-value" id="res_nec_light">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Coincidental HVAC Selected:</span>
                <span class="result-value" id="res_nec_hvac">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Total Calculated Load:</span>
                <span class="result-value" id="res_nec_total_va">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Calculated Service Current (@ 240V):</span>
                <span class="result-value" id="res_nec_amps">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Minimum Standard Panel Rating:</span>
                <span class="result-value" id="res_nec_panel">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Copper Service Conductor (THHN):</span>
                <span class="result-value" id="res_nec_cu_wire">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Aluminum Service Conductor (XHHW):</span>
                <span class="result-value" id="res_nec_al_wire">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Grounding Electrode Conductor (Cu):</span>
                <span class="result-value" id="res_nec_gec">--</span>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    function calculateNecLoad() {
        const sqft = parseFloat(document.getElementById('nec_sqft').value) || 2400;
        const sabc = parseFloat(document.getElementById('nec_sabc').value) || 4500;
        const range = parseFloat(document.getElementById('nec_range').value) || 8000;
        const dryer = parseFloat(document.getElementById('nec_dryer').value) || 5000;
        const wh = parseFloat(document.getElementById('nec_water_heater').value) || 4500;
        const fixedApp = parseFloat(document.getElementById('nec_fixed_appliances').value) || 3200;
        const ac = parseFloat(document.getElementById('nec_ac').value) || 6500;
        const heat = parseFloat(document.getElementById('nec_heat').value) || 10000;
        const ev = parseFloat(document.getElementById('nec_ev').value) || 9600;
        const method = document.getElementById('nec_method').value;

        // 1. General lighting: 3 VA per sq ft (NEC Table 220.12)
        const lightVa = sqft * 3;

        // 2. Non-coincidental HVAC load (NEC 220.60): largest of AC or Heat
        // In optional method NEC 220.82(C): AC is taken at 100%, Central electric heat at 100% (or 65% for 4+ separate units)
        let hvacVa = Math.max(ac, heat);
        let hvacDesc = (ac >= heat) ? 'AC (' + ac + ' VA)' : 'Heat (' + heat + ' VA)';

        let totalDemandVa = 0;

        if (method === 'optional') {
            // NEC Section 220.82 Optional Dwelling Method:
            // Non-HVAC general loads:
            // Lighting + SABC + Range + Dryer + Water Heater + Other fixed appliances + EV (treated as continuous/general)
            const generalVa = lightVa + sabc + range + dryer + wh + fixedApp + ev;

            // First 10,000 VA @ 100%, remainder @ 40%
            let demandGeneral = 0;
            if (generalVa <= 10000) {
                demandGeneral = generalVa;
            } else {
                demandGeneral = 10000 + 0.40 * (generalVa - 10000);
            }

            totalDemandVa = demandGeneral + hvacVa;
        } else {
            // NEC Part III Standard Method:
            // Lighting & SABC demand (NEC Table 220.42):
            const generalBase = lightVa + sabc;
            let lightDemand = 0;
            if (generalBase <= 3000) {
                lightDemand = generalBase;
            } else if (generalBase <= 120000) {
                lightDemand = 3000 + 0.35 * (generalBase - 3000);
            } else {
                lightDemand = 3000 + 0.35 * (117000) + 0.25 * (generalBase - 120000);
            }

            // Fixed appliances: 75% demand factor if 4 or more appliances (NEC 220.53)
            // (Water Heater, Disposal, Dishwasher, Microwave count as 4)
            const appDemand = (wh + fixedApp) * 0.75;

            // Dryer: Table 220.54 (100% for 1 dryer, min 5000 VA)
            const dryerDemand = Math.max(5000, dryer);

            // Range: Table 220.55 Column C (8 kW = 8,000 VA)
            const rangeDemand = Math.max(8000, range);

            // EV continuous load @ 125%
            const evDemand = ev * 1.25;

            totalDemandVa = lightDemand + appDemand + dryerDemand + rangeDemand + hvacVa + evDemand;
        }

        // Service current at 240V single-phase
        const serviceAmps = totalDemandVa / 240;

        // Minimum panel rating
        let panelRating = 100;
        let cuWire = '#4 AWG';
        let alWire = '#2 AWG';
        let gecWire = '#8 AWG';

        if (serviceAmps <= 100) {
            panelRating = 100;
            cuWire = '#4 AWG THHN';
            alWire = '#2 AWG XHHW';
            gecWire = '#8 AWG Cu';
        } else if (serviceAmps <= 125) {
            panelRating = 125;
            cuWire = '#2 AWG THHN';
            alWire = '#1/0 AWG XHHW';
            gecWire = '#6 AWG Cu';
        } else if (serviceAmps <= 150) {
            panelRating = 150;
            cuWire = '#1 AWG THHN';
            alWire = '#2/0 AWG XHHW';
            gecWire = '#6 AWG Cu';
        } else if (serviceAmps <= 200) {
            panelRating = 200;
            cuWire = '2/0 AWG THHN';
            alWire = '4/0 AWG XHHW';
            gecWire = '#4 AWG Cu';
        } else {
            panelRating = 400;
            cuWire = '2x 2/0 or 400 kcmil';
            alWire = '2x 4/0 or 600 kcmil';
            gecWire = '#1/0 AWG Cu';
        }

        document.getElementById('res_nec_light').textContent = lightVa.toLocaleString() + ' VA';
        document.getElementById('res_nec_hvac').textContent = hvacDesc;
        document.getElementById('res_nec_total_va').textContent = Math.round(totalDemandVa).toLocaleString() + ' VA';
        document.getElementById('res_nec_amps').textContent = serviceAmps.toFixed(1) + ' A';
        document.getElementById('res_nec_panel').textContent = panelRating + ' A Main Breaker';
        document.getElementById('res_nec_cu_wire').textContent = cuWire;
        document.getElementById('res_nec_al_wire').textContent = alWire;
        document.getElementById('res_nec_gec').textContent = gecWire;
    }

    document.getElementById('btn_calc_nec').addEventListener('click', calculateNecLoad);
    calculateNecLoad();
});
</script>"""

    article_content = """<h2>1. Principles of Residential Electrical Service Sizing</h2>
<p>Determining the electrical service entrance capacity for a single-family dwelling unit requires synthesizing architectural floor plans, appliance specifications, and mechanical HVAC requirements under the regulatory framework of <strong>NEC Article 220</strong> (Branch-Circuit, Feeder, and Service Load Calculations). An undersized service panel causes severe breaker nuisance tripping, fire risks from overheated main conductors, and code inspection failures during renovations or electric vehicle (EV) charger installations.</p>

<p>The National Electrical Code provides two distinct methodologies for sizing dwelling unit services:</p>
<ul>
    <li><strong>The Standard Calculation Method (NEC Article 220, Part III):</strong> The classical prescriptive calculation that groups electrical loads into specific subcategories and applies individual demand reduction tables (NEC Table 220.42 for lighting, Table 220.54 for clothes dryers, Table 220.55 for cooking appliances, and Section 220.53 for 4+ fastened-in-place appliances).</li>
    <li><strong>The Optional Calculation Method (NEC Article 220, Section 220.82):</strong> An engineering-simplified calculation permissible for existing or new single-family dwelling units served by a 120/240-volt, 3-wire service with an anticipated ampacity of 100 amperes or greater. Under this method, all non-HVAC general loads are aggregated together, the first 10,000 VA is evaluated at 100%, the balance at 40%, and the larger of air conditioning or electric heating is added.</li>
</ul>

<h2>2. NEC Article 220 Mathematical Formulas &amp; Demand Factors</h2>
<p>Under the NEC Section 220.82 Optional Method, total service demand in Volt-Amperes (\(VA_{total}\)) is evaluated through two distinct load groupings:</p>

<h3>General Non-HVAC Load Formulation</h3>
<p>First, all continuous and intermittent non-heating/cooling loads are compiled:</p>

$$VA_{general} = VA_{lighting} + VA_{SABC} + VA_{dryer} + VA_{range} + VA_{water\_heater} + VA_{fixed\_appliances} + VA_{EV}$$

<p>where:</p>
<ul>
    <li>\(VA_{lighting} = \text{Area (sq ft)} \times 3\text{ VA/sq ft}\) (NEC Table 220.12).</li>
    <li>\(VA_{SABC} \ge 4{,}500\text{ VA}\) (At least two 20A small-appliance branch circuits for kitchen countertops plus one 20A laundry circuit @ 1,500 VA each per NEC 220.52).</li>
    <li>\(VA_{dryer} \ge 5{,}000\text{ VA}\) or nameplate rating (NEC 220.54).</li>
    <li>\(VA_{range}\) is the nameplate rating or NEC Table 220.55 equivalent.</li>
</ul>

<p>Next, the dwelling demand factor is applied to this non-HVAC sum:</p>

$$VA_{demand,gen} = \begin{cases} VA_{general} & \text{if } VA_{general} \le 10{,}000\text{ VA} \\ 10{,}000 + 0.40 \times (VA_{general} - 10{,}000) & \text{if } VA_{general} > 10{,}000\text{ VA} \end{cases}$$

<h3>Non-Coincidental HVAC Load Evaluation</h3>
<p>Per NEC Section 220.60, electric space heating and central air conditioning are non-coincidental loads because they do not operate simultaneously at maximum capacity during the same season. The design engineer evaluates both:</p>

$$VA_{HVAC} = \max\left(VA_{AC} \times 1.00, \; VA_{Heat} \times 1.00\right)$$

<h3>Total Service Amperes and Panel Selection</h3>
<p>The total dwelling demand is the sum of general demand and HVAC demand:</p>

$$VA_{service} = VA_{demand,gen} + VA_{HVAC}$$

<p>The calculated service current \(I_{service}\) at standard single-phase residential supply voltage (\(240\text{ V}\)) is:</p>

$$I_{service} = \frac{VA_{service}}{240\text{ V}}$$

<p>The main service disconnect and panel bus must have an ampere rating equal to or exceeding \(I_{service}\), rounded up to the nearest standard electrical distribution panel rating: 100A, 125A, 150A, 200A, or 400A (NEC Section 240.6).</p>

<h2>3. NEC Table 310.12 Residential Service Conductor Sizing Table</h2>
<p>The following engineering data table specifies allowable minimum conductor gauges for 120/240-volt single-phase dwelling service entrance and main feeder runs per NEC Section 310.12 (formerly Table 310.15(B)(7)):</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Service Rating (Amperes)</th>
            <th>Copper Conductor (75°C THHN/THWN-2)</th>
            <th>Aluminum / Copper-Clad Al (XHHW/USE-2)</th>
            <th>Min Grounding Electrode Conductor (Cu)</th>
            <th>Typical Dwelling Size Scope</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>100 A</strong></td>
            <td>#4 AWG Cu</td>
            <td>#2 AWG Al</td>
            <td>#8 AWG Cu</td>
            <td>Small condos, gas-heated homes (&lt;1,400 sq ft)</td>
        </tr>
        <tr>
            <td><strong>125 A</strong></td>
            <td>#2 AWG Cu</td>
            <td>#1/0 AWG Al</td>
            <td>#6 AWG Cu</td>
            <td>Modest suburban homes with gas heating</td>
        </tr>
        <tr>
            <td><strong>150 A</strong></td>
            <td>#1 AWG Cu</td>
            <td>#2/0 AWG Al</td>
            <td>#6 AWG Cu</td>
            <td>Mid-sized homes (1,600 – 2,400 sq ft), gas furnace</td>
        </tr>
        <tr>
            <td><strong>200 A</strong></td>
            <td>2/0 AWG Cu</td>
            <td>4/0 AWG Al</td>
            <td>#4 AWG Cu</td>
            <td>Modern standard (2,000 – 3,500 sq ft), all-electric or EV</td>
        </tr>
        <tr>
            <td><strong>400 A (320A Continuous)</strong></td>
            <td>2 parallel runs of 2/0 AWG Cu or 400 kcmil</td>
            <td>2 parallel runs of 4/0 AWG Al or 600 kcmil</td>
            <td>#1/0 AWG Cu</td>
            <td>Large executive homes (&gt;3,500 sq ft), dual heat pumps, 2x EVs, pool</td>
        </tr>
    </tbody>
</table>

<h2>4. Fastened-In-Place Appliance Rules &amp; Continuous Loads</h2>
<p>When applying the standard calculation method (Part III), NEC Section 220.53 grants a <strong>75% demand factor</strong> if four or more fastened-in-place appliances (excluding electric ranges, clothes dryers, and HVAC equipment) are served by the same feeder or service entrance. Qualifying appliances include electric water heaters, under-cabinet dishwashers, in-sink food waste disposers, built-in microwave ovens, and attic attic ventilation fans.</p>

<p>Conversely, <strong>Electric Vehicle Supply Equipment (EVSE)</strong> represents a continuous load per NEC Article 625. A standard Level 2 EV charging circuit operating at 40A, 240V draws \(9{,}600\text{ VA}\) continuously for 4 to 8 hours. When sized under the standard calculation method, continuous loads must be evaluated at <strong>125% of their rated ampacity</strong> (\(9{,}600 \times 1.25 = 12{,}000\text{ VA}\)), whereas under the Section 220.82 Optional Method, the nameplate \(9{,}600\text{ VA}\) is combined into the general load bundle prior to the 40% reduction.</p>

<h2>5. Worked Engineering Case Study: 2,400 Sq Ft Dwelling with Heat Pump &amp; EV</h2>
<div class="worked-example-card">
    <h3>Design Specification: New Suburban All-Electric Residence</h3>
    <p>A new single-family residence features a finished conditioned living space of \(2{,}400\text{ sq ft}\). The electrical equipment roster includes: standard kitchen countertop small-appliance circuits (2 circuits) and laundry (1 circuit) total \(4{,}500\text{ VA}\); an electric cooking range rated at \(8{,}000\text{ VA}\); an electric clothes dryer rated at \(5{,}000\text{ VA}\); an electric hybrid heat pump water heater rated at \(4{,}500\text{ VA}\); other fixed appliances (dishwasher, disposal, microwave) totaling \(3{,}200\text{ VA}\); a 40A Level 2 EV charger (\(9{,}600\text{ VA}\)); a central 3-ton air conditioning compressor (\(6{,}500\text{ VA}\)); and an auxiliary electric heating strip (\(10{,}000\text{ VA}\)). The master electrician sizes the electrical service under <strong>NEC Section 220.82 (Optional Method)</strong>.</p>

    <div class="step-solution">
        <h4>Step 1: Compute General Lighting Baseline</h4>
        $$VA_{lighting} = 2{,}400\text{ sq ft} \times 3\text{ VA/sq ft} = 7{,}200\text{ VA}$$

        <h4>Step 2: Aggregate All Non-HVAC General Connected Loads</h4>
        $$VA_{gen} = 7{,}200\text{ (light)} + 4{,}500\text{ (SABC/laundry)} + 8{,}000\text{ (range)} + 5{,}000\text{ (dryer)} + 4{,}500\text{ (WH)} + 3{,}200\text{ (fixed)} + 9{,}600\text{ (EV)}$$
        $$VA_{gen} = 42{,}000\text{ VA}$$

        <h4>Step 3: Apply NEC 220.82 Demand Factors</h4>
        <p>First 10,000 VA evaluated at 100%:</p>
        $$10{,}000\text{ VA} \times 1.00 = 10{,}000\text{ VA}$$
        <p>Remaining balance of \((42{,}000 - 10{,}000) = 32{,}000\text{ VA}\) evaluated at 40%:</p>
        $$32{,}000\text{ VA} \times 0.40 = 12{,}800\text{ VA}$$
        $$VA_{demand,gen} = 10{,}000 + 12{,}800 = 22{,}800\text{ VA}$$

        <h4>Step 4: Non-Coincidental HVAC Load Evaluation</h4>
        $$VA_{HVAC} = \max(6{,}500\text{ VA [AC]}, \; 10{,}000\text{ VA [Heat]}) = 10{,}000\text{ VA}$$

        <h4>Step 5: Compute Total Service Demand and Minimum Service Rating</h4>
        $$VA_{service} = VA_{demand,gen} + VA_{HVAC} = 22{,}800\text{ VA} + 10{,}000\text{ VA} = 32{,}800\text{ VA}$$
        $$I_{service} = \frac{32{,}800\text{ VA}}{240\text{ V}} = 136.67\text{ A}$$
        <p>Because the calculated demand of \(136.7\text{ A}\) exceeds 125A, code mandates selecting the next standard higher service size: a <strong>200 Ampere Service Entrance Panel</strong>.</p>

        <h4>Step 6: Conductor and Grounding Specification</h4>
        <p>Consulting NEC Table 310.12 for a 200A residential service:</p>
        <ul>
            <li><strong>Copper Option:</strong> <strong>2/0 AWG THHN Copper</strong> ungrounded conductors.</li>
            <li><strong>Aluminum Option:</strong> <strong>4/0 AWG Aluminum (SE Cable / XHHW)</strong> ungrounded conductors.</li>
            <li><strong>Grounding Electrode Conductor (NEC Table 250.66):</strong> <strong>#4 AWG Bare Copper</strong> connected to concrete-encased Ufer ground and two driven ground rods spaced &ge; 6 feet apart.</li>
        </ul>
    </div>
</div>

<h2>6. Frequently Asked Questions</h2>
<div class="faq-accordion">
    <div class="faq-item">
        <h3>What is the difference between NEC Article 220 Part III (Standard) and Part IV (Optional) calculation methods?</h3>
        <p>The Standard Method (Part III) applies distinct demand factor schedules to each individual load category: lighting (NEC Table 220.42), electric ranges (Table 220.55), clothes dryers (Table 220.54), and fixed appliances (75% for 4+ appliances). The Optional Method (NEC Section 220.82) simplifies this for single-family homes with 100A+ service: all non-HVAC general loads are totaled, the first 10,000 VA is taken at 100%, the remainder at 40%, and the largest HVAC load (AC vs heating) is added.</p>
    </div>
    <div class="faq-item">
        <h3>Why is general lighting calculated at 3 VA per square foot in dwelling units?</h3>
        <p>NEC Table 220.12 mandates 3 Volt-Amperes (VA) per square foot of habitable living area. This standardized baseline accounts for all general-use illumination and general convenience receptacle outlets throughout bedrooms, living rooms, and hallways, calculated using exterior building dimensions.</p>
    </div>
    <div class="faq-item">
        <h3>How does the NEC handle coincidental Heating and Air Conditioning (HVAC) loads?</h3>
        <p>Per NEC Section 220.60 (Noncoincident Loads), where two or more dissimilar loads are unlikely to operate simultaneously—such as central air conditioning during summer and central heating during winter—only the single largest load is included in the total service calculation.</p>
    </div>
    <div class="faq-item">
        <h3>What are the standard residential electrical service sizes under modern building codes?</h3>
        <p>Modern single-family residential services are almost universally standardized at 100 Ampere (minimum code threshold per NEC 230.79), 150 Ampere, 200 Ampere (standard modern new construction), or 400 Ampere (320A continuous) for large homes with multiple electric vehicles, heat pumps, and induction ranges.</p>
    </div>
</div>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article_content)


def main():
    tools = [
        ("motor-starter-sizing-calculator.html", gen_motor_starter()),
        ("nec-load-calculation-calculator.html", gen_nec_load())
    ]
    for filename, content in tools:
        filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {filename}")

if __name__ == "__main__":
    main()
