# -*- coding: utf-8 -*-
"""
Generator for Batch 37 - Part 3
Tools:
5. neutral-conductor-sizing-calculator.html
6. stair-calculator.html
"""

import os

COMMON_TAIL = """    <footer class="site-footer">
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>About CalcHub</h4>
                    <p>CalcHub provides free, high-precision engineering calculators, unit converters, and analytical tools designed for practicing engineers, architects, electricians, and builders worldwide.</p>
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
                        <li><a href="nec-load-calculation-calculator.html">NEC Load Calculation</a></li>
                        <li><a href="stair-calculator.html">Stair Calculator</a></li>
                        <li><a href="concrete-calculator.html">Concrete Calculator</a></li>
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
                    <h3>Related Tools</h3>
                    <ul class="sidebar-links">
                        <li><a href="neutral-conductor-sizing-calculator.html">Neutral Conductor Sizing</a></li>
                        <li><a href="stair-calculator.html">Stair Calculator</a></li>
                        <li><a href="nec-load-calculation-calculator.html">NEC Load Calculation</a></li>
                        <li><a href="motor-starter-sizing-calculator.html">Motor Starter Sizing</a></li>
                        <li><a href="3-phase-power-calculator.html">3-Phase Power Calculator</a></li>
                        <li><a href="wire-ampacity-calculator.html">Wire Ampacity</a></li>
                        <li><a href="voltage-drop-calculator.html">Voltage Drop</a></li>
                        <li><a href="conduit-fill-calculator.html">Conduit Fill</a></li>
                        <li><a href="grounding-electrode-conductor-calculator.html">Grounding Conductor</a></li>
                        <li><a href="concrete-calculator.html">Concrete Slab &amp; Footing</a></li>
                    </ul>
                </div>
            </aside>
        </div>
    </div>
{COMMON_TAIL}"""


# ---------------------------------------------------------------------------
# Tool 5: Neutral Conductor Sizing Calculator
# ---------------------------------------------------------------------------
def gen_neutral_sizing():
    slug = "neutral-conductor-sizing-calculator"
    title = "Neutral Conductor Sizing Calculator | Unbalanced Current, Harmonics & NEC 220.61"
    desc = "Calculate 3-phase neutral conductor ampacity, unbalanced load current, triplen harmonic distortion derating, and permissible neutral reduction per NEC 220.61 and 310.15(E)."
    h1 = "Neutral Conductor Sizing Calculator"
    short_desc = "Calculate fundamental unbalanced neutral current, triplen harmonic loading (3rd harmonic), NEC 220.61 70% derating, and conductor ampacity for 3-phase 4-wire systems."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Neutral Conductor Sizing Calculator",
      "url": "https://calchub.com/neutral-conductor-sizing-calculator.html",
      "applicationCategory": "EngineeringApplication",
      "operatingSystem": "All",
      "description": "Calculate neutral conductor sizing, 3-phase unbalance current, triplen harmonic multiplication, and NEC Section 220.61 neutral reduction factors.",
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
          "name": "Why can neutral current exceed line current in 3-phase 4-wire systems?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In systems serving non-linear electronic loads (computers, servers, variable speed drives, LED drivers), single-phase switch-mode power supplies draw pulsating current rich in triplen harmonics (specifically the 3rd harmonic, 180 Hz). Because the phase angles of triplen harmonics coincide in all three phases (3 * 120° = 360° = 0°), they do not cancel out at the neutral node. Instead, they add arithmetically in the neutral conductor, causing total neutral current to reach up to 140% to 173% of phase current."
          }
        },
        {
          "@type": "Question",
          "name": "What is the NEC Section 220.61 neutral reduction rule?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "NEC Section 220.61 permits sizing the feeder or service neutral conductor for the maximum unbalanced load. For linear loads exceeding 200 Amperes, a 70% demand factor can be applied to the portion of the unbalanced load exceeding 200 Amperes. However, this 70% reduction is strictly prohibited for portions of the load consisting of non-linear electronic equipment."
          }
        },
        {
          "@type": "Question",
          "name": "When does the neutral conductor count as a current-carrying conductor for ampacity adjustment?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Per NEC Section 310.15(E)(3), in a 3-phase 4-wire Wye circuit where the major portion of the load consists of non-linear loads, harmonic currents are present in the neutral conductor. Therefore, the neutral conductor must be counted as a current-carrying conductor when applying conduit derating adjustment factors from NEC Table 310.15(C)(1)."
          }
        },
        {
          "@type": "Question",
          "name": "What is a 200% super-neutral conductor and when is it specified?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A 200% oversized neutral (or dual neutral conductors) is engineered for data centers, broadcast facilities, and commercial office distribution panels with severe harmonic pollution. Because triplen harmonics create neutral currents exceeding phase conductor amperes, the neutral bus and conductor are rated for twice (200%) the ampacity of the phase conductors to prevent overheating and insulation breakdown."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calculator-form">
    <div class="calc-row">
        <div class="calc-field">
            <label for="nc_system">System Type:</label>
            <select id="nc_system">
                <option value="3p4w" selected>3-Phase 4-Wire Wye (208Y/120V or 480Y/277V)</option>
                <option value="1p3w">Single-Phase 3-Wire (120/240V Split-Phase)</option>
            </select>
        </div>
        <div class="calc-field">
            <label for="nc_load_nature">Nature of Electrical Load:</label>
            <select id="nc_load_nature">
                <option value="linear">Linear Loads (Motors, Heaters, Incandescent)</option>
                <option value="moderate_nl" selected>Moderate Non-Linear (Offices, Mixed PCs, Commercial)</option>
                <option value="heavy_nl">Heavy Non-Linear (Data Center, Servers, LED Drivers)</option>
            </select>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="nc_ia">Phase A Current \\(I_A\\) (Amperes):</label>
            <input type="number" id="nc_ia" value="180" step="1" min="0">
        </div>
        <div class="calc-field">
            <label for="nc_ib">Phase B Current \\(I_B\\) (Amperes):</label>
            <input type="number" id="nc_ib" value="150" step="1" min="0">
        </div>
        <div class="calc-field" id="box_nc_ic">
            <label for="nc_ic">Phase C Current \\(I_C\\) (Amperes):</label>
            <input type="number" id="nc_ic" value="120" step="1" min="0">
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="nc_thd">Estimated 3rd Harmonic Distortion (\\(\\%HD_3\\)):</label>
            <input type="number" id="nc_thd" value="30" step="5" min="0" max="100">
            <small class="field-hint">0% for linear, 20-35% commercial, 40-70% data center servers</small>
        </div>
        <div class="calc-field">
            <label for="nc_ambient">Ambient Temperature (°C):</label>
            <select id="nc_ambient">
                <option value="30" selected>30°C (86°F) - Standard</option>
                <option value="35">35°C (95°F)</option>
                <option value="40">40°C (104°F)</option>
                <option value="45">45°C (113°F)</option>
            </select>
        </div>
    </div>
    <button type="button" class="btn btn-primary" id="btn_calc_nc" style="width:100%; margin-top:1rem;">Calculate Neutral Sizing &amp; Harmonic Ampacity</button>

    <div class="calc-results" id="nc_results" style="margin-top:1.5rem;">
        <h3>Neutral Conductor Engineering Analysis</h3>
        <div class="results-grid">
            <div class="result-item">
                <span class="result-label">Fundamental Unbalance Current:</span>
                <span class="result-value" id="res_nc_fund">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Triplen Harmonic Current (180 Hz):</span>
                <span class="result-value" id="res_nc_triplen">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Total True RMS Neutral Current:</span>
                <span class="result-value" id="res_nc_trms">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">NEC 220.61 Permissible Demand:</span>
                <span class="result-value" id="res_nc_demand">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Required Neutral Wire Ampacity:</span>
                <span class="result-value" id="res_nc_req_amp">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Recommended Copper Gauge (THHN):</span>
                <span class="result-value" id="res_nc_cu_wire">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Recommended Aluminum Gauge (XHHW):</span>
                <span class="result-value" id="res_nc_al_wire">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Neutral Conductor Status:</span>
                <span class="result-value" id="res_nc_status">--</span>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const sysSelect = document.getElementById('nc_system');
    const boxIc = document.getElementById('box_nc_ic');
    const loadNature = document.getElementById('nc_load_nature');
    const thdInput = document.getElementById('nc_thd');

    sysSelect.addEventListener('change', function() {
        if (sysSelect.value === '1p3w') {
            boxIc.style.display = 'none';
        } else {
            boxIc.style.display = 'block';
        }
    });

    loadNature.addEventListener('change', function() {
        if (loadNature.value === 'linear') {
            thdInput.value = 0;
        } else if (loadNature.value === 'moderate_nl') {
            thdInput.value = 30;
        } else {
            thdInput.value = 60;
        }
    });

    function getStandardWire(amps, metal) {
        if (metal === 'cu') {
            if (amps <= 20) return '#12 AWG THHN (20A)';
            if (amps <= 30) return '#10 AWG THHN (30A)';
            if (amps <= 50) return '#8 AWG THHN (50A)';
            if (amps <= 65) return '#6 AWG THHN (65A)';
            if (amps <= 85) return '#4 AWG THHN (85A)';
            if (amps <= 100) return '#3 AWG THHN (100A)';
            if (amps <= 115) return '#2 AWG THHN (115A)';
            if (amps <= 130) return '#1 AWG THHN (130A)';
            if (amps <= 150) return '1/0 AWG THHN (150A)';
            if (amps <= 175) return '2/0 AWG THHN (175A)';
            if (amps <= 200) return '3/0 AWG THHN (200A)';
            if (amps <= 230) return '4/0 AWG THHN (230A)';
            if (amps <= 255) return '250 kcmil THHN (255A)';
            if (amps <= 285) return '300 kcmil THHN (285A)';
            if (amps <= 310) return '350 kcmil THHN (310A)';
            if (amps <= 380) return '500 kcmil THHN (380A)';
            return '2x 4/0 or 600 kcmil';
        } else {
            if (amps <= 40) return '#8 AWG Al (40A)';
            if (amps <= 50) return '#6 AWG Al (50A)';
            if (amps <= 65) return '#4 AWG Al (65A)';
            if (amps <= 75) return '#3 AWG Al (75A)';
            if (amps <= 90) return '#2 AWG Al (90A)';
            if (amps <= 100) return '#1 AWG Al (100A)';
            if (amps <= 120) return '1/0 AWG Al (120A)';
            if (amps <= 135) return '2/0 AWG Al (135A)';
            if (amps <= 155) return '3/0 AWG Al (155A)';
            if (amps <= 180) return '4/0 AWG Al (180A)';
            if (amps <= 205) return '250 kcmil Al (205A)';
            if (amps <= 230) return '300 kcmil Al (230A)';
            if (amps <= 250) return '350 kcmil Al (250A)';
            if (amps <= 310) return '500 kcmil Al (310A)';
            return '2x 300 kcmil or 600 kcmil Al';
        }
    }

    function calculateNeutral() {
        const sys = sysSelect.value;
        const ia = parseFloat(document.getElementById('nc_ia').value) || 0;
        const ib = parseFloat(document.getElementById('nc_ib').value) || 0;
        const ic = (sys === '3p4w') ? (parseFloat(document.getElementById('nc_ic').value) || 0) : 0;
        const thd3Pct = parseFloat(document.getElementById('nc_thd').value) || 0;
        const nature = loadNature.value;

        let fundUnbalance = 0;
        let triplenCurrent = 0;

        if (sys === '1p3w') {
            // Single phase 120/240V: In = |Ia - Ib|
            fundUnbalance = Math.abs(ia - ib);
            triplenCurrent = 0; // single phase cancellation does not have 3-phase additive triplen
        } else {
            // 3-phase 4-wire vector unbalance:
            // In = sqrt(Ia^2 + Ib^2 + Ic^2 - Ia*Ib - Ib*Ic - Ic*Ia)
            const term = Math.pow(ia, 2) + Math.pow(ib, 2) + Math.pow(ic, 2) - (ia * ib) - (ib * ic) - (ic * ia);
            fundUnbalance = Math.sqrt(Math.max(0, term));

            // Triplen harmonic current adds in phase: In_triplen = 3 * I_phase_avg * (HD3 / 100)
            const avgPhase = (ia + ib + ic) / 3;
            triplenCurrent = 3 * avgPhase * (thd3Pct / 100);
        }

        // True RMS neutral current:
        const totalRmsNeutral = Math.sqrt(Math.pow(fundUnbalance, 2) + Math.pow(triplenCurrent, 2));

        // Permissible NEC 220.61 reduction calculation:
        // First 200A at 100%, remainder at 70% ONLY for linear loads!
        let necReducedAmps = totalRmsNeutral;
        let reductionStatus = "No reduction allowed (Harmonic / Non-linear load)";

        if (nature === 'linear' && totalRmsNeutral > 200) {
            necReducedAmps = 200 + 0.70 * (totalRmsNeutral - 200);
            reductionStatus = "70% reduction applied to amps > 200A (NEC 220.61)";
        } else if (nature === 'linear') {
            reductionStatus = "100% evaluated (load <= 200A)";
        }

        // Conductor sizing ampacity
        const reqAmpacity = (nature === 'heavy_nl') ? Math.max(totalRmsNeutral, Math.max(ia, Math.max(ib, ic)) * 1.5) : necReducedAmps;

        let statusText = "Standard Full-Size Neutral";
        const maxPhase = Math.max(ia, Math.max(ib, ic));
        if (totalRmsNeutral > maxPhase) {
            statusText = "Oversized / Super-Neutral Required (> Phase Ampacity)";
        } else if (nature === 'heavy_nl') {
            statusText = "Harmonic Derated Conductor (NEC 310.15(E)(3))";
        }

        const cuWire = getStandardWire(reqAmpacity, 'cu');
        const alWire = getStandardWire(reqAmpacity, 'al');

        document.getElementById('res_nc_fund').textContent = fundUnbalance.toFixed(1) + ' A';
        document.getElementById('res_nc_triplen').textContent = triplenCurrent.toFixed(1) + ' A (3rd Harmonic)';
        document.getElementById('res_nc_trms').textContent = totalRmsNeutral.toFixed(1) + ' A True RMS';
        document.getElementById('res_nc_demand').textContent = necReducedAmps.toFixed(1) + ' A (' + reductionStatus + ')';
        document.getElementById('res_nc_req_amp').textContent = reqAmpacity.toFixed(1) + ' A';
        document.getElementById('res_nc_cu_wire').textContent = cuWire;
        document.getElementById('res_nc_al_wire').textContent = alWire;
        document.getElementById('res_nc_status').textContent = statusText;
    }

    document.getElementById('btn_calc_nc').addEventListener('click', calculateNeutral);
    calculateNeutral();
});
</script>"""

    article_content = """<h2>1. Physics of the Neutral Conductor in Polyphase Power Systems</h2>
<p>In a balanced three-phase four-wire alternating current system supplying purely linear resistive or inductive loads, the three phase currents are identical in magnitude and displaced from one another by \(120^\circ\) in time phase. When these currents converge at the central neutral junction (\(N\)) of a Wye-connected transformer or generator, Kirchhoff's Current Law (\(\sum \vec{I} = 0\)) dictates that the geometric vector sum of the currents is identically zero. Consequently, under perfectly balanced linear operating conditions, zero amperes return through the neutral conductor.</p>

<p>In real-world commercial and industrial electrical distribution, however, two distinct physical phenomena generate substantial current in the neutral conductor:</p>
<ol>
    <li><strong>Linear Phase Load Unbalance:</strong> Connected single-phase line-to-neutral loads (such as 120V lighting, convenience outlets, and single-phase heating elements) are rarely distributed with perfect numerical symmetry across Phases A, B, and C. The algebraic difference in phase loading forces an unbalance current to flow back to the source transformer neutral.</li>
    <li><strong>Non-Linear Loads &amp; Triplen Harmonic Accumulation:</strong> Modern electronic loads—including server racks, personal computers, variable frequency drives (VFDs), electronic ballasts, and LED power supplies—draw non-sinusoidal, discontinuous current pulses. These distorted wave shapes are heavily saturated with odd harmonics, predominantly the <strong>third harmonic (180 Hz in 60 Hz systems, 150 Hz in 50 Hz systems)</strong> and higher odd multiples of three (9th, 15th, 21st, termed <em>triplen harmonics</em>).</li>
</ol>

<h2>2. Governing Mathematical Derivations</h2>
<h3>Fundamental Vector Unbalance Current</h3>
<p>For a three-phase four-wire system with phase RMS currents \(I_A\), \(I_B\), and \(I_C\) displaced by \(120^\circ\), the fundamental neutral unbalance current \(I_{N,fund}\) is calculated via vector trigonometry:</p>

$$\vec{I}_N = \vec{I}_A + \vec{I}_B + \vec{I}_C$$

$$I_{N,fund} = \sqrt{I_A^2 + I_B^2 + I_C^2 - I_A I_B - I_B I_C - I_C I_A}$$

<p>For a single-phase 120/240V 3-wire split-phase residential service, Phase A and Phase B are displaced by \(180^\circ\), reducing the fundamental unbalance current to a simple scalar difference:</p>

$$I_{N,1\phi} = |I_A - I_B|$$

<h3>Triplen Harmonic In-Phase Arithmetic Summation</h3>
<p>While fundamental currents are displaced by \(120^\circ\) (\(2\pi/3\)), the third harmonic frequencies are displaced by \(3 \times 120^\circ = 360^\circ \equiv 0^\circ\). Because the phase displacement between the third harmonic components across all three phases is zero degrees, <strong>triplen harmonics are in-phase zero-sequence components</strong>.</p>

<p>Instead of canceling at the neutral star point, triplen currents add arithmetically. If each phase carries a third-harmonic component \(I_{h3}\), the net third-harmonic current in the neutral conductor is:</p>

$$I_{N,3rd} = 3 \times I_{h3} = 3 \times I_{phase} \times \left(\frac{\%HD_3}{100}\right)$$

<h3>Total True Root-Mean-Square Neutral Current</h3>
<p>Because the fundamental unbalance current (60 Hz) and the third harmonic current (180 Hz) are orthogonal in the frequency domain, total true RMS neutral current \(I_{N,rms}\) is determined through quadrature summation:</p>

$$I_{N,rms} = \sqrt{I_{N,fund}^2 + I_{N,3rd}^2 + I_{N,9th}^2 + \dots}$$

<p>In data centers and commercial buildings with high concentrations of switched-mode power supplies, the ratio \(I_{N,rms} / I_{phase}\) frequently reaches <strong>130% to 173%</strong>, meaning the neutral conductor carries substantially more current than any of the phase conductors.</p>

<h2>3. NEC Regulatory Code Standards: Section 220.61 and 310.15(E)</h2>
<p>The National Electrical Code contains specific mandates governing neutral conductor sizing, reduction, and thermal derating:</p>

<h3>NEC Section 220.61 Feeder Neutral Reduction (70% Rule)</h3>
<p>For commercial and industrial feeders supplying large linear loads, the service or feeder neutral conductor may be sized to carry the maximum unbalanced load. When this load exceeds 200 Amperes, a <strong>70% demand factor</strong> is permitted for that portion of the unbalanced load exceeding 200 Amperes:</p>

$$I_{neutral,demand} = 200\text{ A} + 0.70 \times \left(I_{unbalanced} - 200\text{ A}\right)$$

<p><strong>Critical Code Restriction:</strong> NEC Section 220.61(C)(2) strictly forbids applying this 70% demand reduction to any portion of the feeder load that consists of non-linear electronic equipment, fluorescent or LED lighting, or data processing systems.</p>

<h3>NEC Section 310.15(E)(3) Current-Carrying Conductor Derating</h3>
<p>Under ordinary linear balanced conditions, the neutral conductor carries only unbalance current and does not count as a current-carrying conductor when calculating conduit ampacity derating adjustments from NEC Table 310.15(C)(1). However, per <strong>NEC Section 310.15(E)(3)</strong>:</p>
<blockquote>
<p>"In a 3-phase, 4-wire, wye-connected system where the major portion of the load consists of nonlinear loads, harmonic currents are present in the neutral conductor; the neutral conductor shall therefore be considered a current-carrying conductor."</p>
</blockquote>
<p>Counting the neutral brings the total conductor count in a 4-wire conduit from 3 to 4, mandating an immediate <strong>80% ampacity derating factor</strong> across all conductors in the raceway.</p>

<h2>4. Empirical Harmonic Spectrum Benchmark Table</h2>
<p>The following engineering data table provides standard current harmonic profiles and resultant neutral loading factors across common commercial and industrial facility types:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Facility / Load Environment</th>
            <th>Predominant Load Equipment</th>
            <th>Typical 3rd Harmonic (\% of Fund)</th>
            <th>Typical THD\(_i\) (%)</th>
            <th>Neutral Current Ratio (\(I_N / I_{phase}\))</th>
            <th>Recommended Neutral Design Sizing</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Industrial Machine Shop</strong></td>
            <td>3-Phase induction motors, resistance ovens</td>
            <td>&lt; 5%</td>
            <td>&lt; 8%</td>
            <td>10% – 30% (Unbalance only)</td>
            <td>Standard or Reduced (NEC 220.61)</td>
        </tr>
        <tr>
            <td><strong>Modern Commercial Office</strong></td>
            <td>Laptops, PCs, LED fixtures, copiers</td>
            <td>25% – 35%</td>
            <td>30% – 45%</td>
            <td>80% – 110%</td>
            <td>100% Minimum Full-Size Neutral</td>
        </tr>
        <tr>
            <td><strong>Data Center / Server Farm</strong></td>
            <td>Blade servers, high-density IT power supplies</td>
            <td>45% – 60%</td>
            <td>60% – 85%</td>
            <td>130% – 173%</td>
            <td><strong>200% Super-Neutral (Double Size)</strong></td>
        </tr>
        <tr>
            <td><strong>Broadcast &amp; Recording Studio</strong></td>
            <td>Audio amplifiers, digital video consoles</td>
            <td>30% – 45%</td>
            <td>40% – 55%</td>
            <td>100% – 135%</td>
            <td>150% – 200% Dedicated Neutral Bus</td>
        </tr>
        <tr>
            <td><strong>Healthcare / Diagnostic Labs</strong></td>
            <td>MRI machines, X-ray scanners, lab analyzers</td>
            <td>20% – 30%</td>
            <td>25% – 40%</td>
            <td>70% – 100%</td>
            <td>100% Full-Size Isolated Neutral</td>
        </tr>
    </tbody>
</table>

<h2>5. Worked Engineering Case Study: Commercial Office Floor Feeder</h2>
<div class="worked-example-card">
    <h3>Design Specification: 208Y/120V Commercial Office Subpanel Feeder</h3>
    <p>A corporate headquarters installs a 208Y/120V 3-phase 4-wire subpanel feeding workstations and solid-state LED troffers. RMS current measurements record: <strong>Phase A = 180.0 A</strong>, <strong>Phase B = 150.0 A</strong>, and <strong>Phase C = 120.0 A</strong>. Power quality loggers reveal a severe 3rd harmonic content averaging <strong>30% of fundamental phase current</strong> (\(HD_3 = 30\%\)). The consulting engineer must calculate the fundamental unbalance, the triplen harmonic current, the true RMS neutral current, and specify the copper conductor gauge.</p>

    <div class="step-solution">
        <h4>Step 1: Compute Fundamental 60 Hz Unbalance Current</h4>
        $$I_A^2 + I_B^2 + I_C^2 = 180^2 + 150^2 + 120^2 = 32{,}400 + 22{,}500 + 14{,}400 = 69{,}300$$
        $$I_A I_B + I_B I_C + I_C I_A = (180 \times 150) + (150 \times 120) + (120 \times 180) = 27{,}000 + 18{,}000 + 21{,}600 = 66{,}600$$
        $$I_{N,fund} = \sqrt{69{,}300 - 66{,}600} = \sqrt{2{,}700} \approx 51.96\text{ A}$$

        <h4>Step 2: Compute In-Phase 3rd Harmonic Neutral Current</h4>
        $$I_{phase,avg} = \frac{180 + 150 + 120}{3} = \frac{450}{3} = 150.0\text{ A}$$
        $$I_{N,3rd} = 3 \times I_{phase,avg} \times 0.30 = 3 \times 150.0 \times 0.30 = 135.0\text{ A}$$

        <h4>Step 3: Compute True RMS Total Neutral Current</h4>
        $$I_{N,rms} = \sqrt{I_{N,fund}^2 + I_{N,3rd}^2} = \sqrt{(51.96)^2 + (135.0)^2} = \sqrt{2{,}700 + 18{,}225} = \sqrt{20{,}925} \approx 144.65\text{ A}$$
        <p>Notice that the harmonic current (\(135.0\text{ A}\)) dominates the net neutral loading, resulting in a total current of nearly \(145\text{ A}\)—nearly triple the fundamental unbalance of \(52\text{ A}\).</p>

        <h4>Step 4: Conductor Ampacity &amp; NEC Derating Application</h4>
        <p>Because non-linear loads predominate, NEC Section 220.61 70% reduction is <strong>prohibited</strong>. Furthermore, per NEC 310.15(E)(3), the neutral must be counted as a current-carrying conductor, requiring an 80% raceway derating factor for 4 current-carrying wires (Phase A, B, C + Neutral). To deliver \(180\text{ A}\) phase ampacity with a \(0.80\) derating factor:</p>
        $$I_{rated} \ge \frac{180\text{ A}}{0.80} = 225.0\text{ A}$$
        <p>Referencing NEC Table 310.16 (75°C terminal rating), a <strong>4/0 AWG THHN Copper conductor</strong> (rated 230A) is selected for all three phase conductors AND the neutral conductor. Installing a full-sized 4/0 AWG copper neutral conductor prevents neutral bus overheating and guarantees thermal compliance under full harmonic loading.</p>
    </div>
</div>

<h2>6. Frequently Asked Questions</h2>
<div class="faq-accordion">
    <div class="faq-item">
        <h3>Why can neutral current exceed line current in 3-phase 4-wire systems?</h3>
        <p>In systems serving non-linear electronic loads (computers, servers, variable speed drives, LED drivers), single-phase switch-mode power supplies draw pulsating current rich in triplen harmonics (specifically the 3rd harmonic, 180 Hz). Because the phase angles of triplen harmonics coincide in all three phases (\(3 \times 120^\circ = 360^\circ \equiv 0^\circ\)), they do not cancel out at the neutral node. Instead, they add arithmetically in the neutral conductor, causing total neutral current to reach up to 140% to 173% of phase current.</p>
    </div>
    <div class="faq-item">
        <h3>What is the NEC Section 220.61 neutral reduction rule?</h3>
        <p>NEC Section 220.61 permits sizing the feeder or service neutral conductor for the maximum unbalanced load. For linear loads exceeding 200 Amperes, a 70% demand factor can be applied to the portion of the unbalanced load exceeding 200 Amperes. However, this 70% reduction is strictly prohibited for portions of the load consisting of non-linear electronic equipment.</p>
    </div>
    <div class="faq-item">
        <h3>When does the neutral conductor count as a current-carrying conductor for ampacity adjustment?</h3>
        <p>Per NEC Section 310.15(E)(3), in a 3-phase 4-wire Wye circuit where the major portion of the load consists of non-linear loads, harmonic currents are present in the neutral conductor. Therefore, the neutral conductor must be counted as a current-carrying conductor when applying conduit derating adjustment factors from NEC Table 310.15(C)(1).</p>
    </div>
    <div class="faq-item">
        <h3>What is a 200% super-neutral conductor and when is it specified?</h3>
        <p>A 200% oversized neutral (or dual neutral conductors) is engineered for data centers, broadcast facilities, and commercial office distribution panels with severe harmonic pollution. Because triplen harmonics create neutral currents exceeding phase conductor amperes, the neutral bus and conductor are rated for twice (200%) the ampacity of the phase conductors to prevent overheating and insulation breakdown.</p>
    </div>
</div>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article_content)


# ---------------------------------------------------------------------------
# Tool 6: Stair Calculator
# ---------------------------------------------------------------------------
def gen_stair_calculator():
    slug = "stair-calculator"
    title = "Stair Calculator | Riser Height, Tread Run, Stringer & Headroom (IBC & IRC)"
    desc = "Calculate stair dimensions, riser height, tread depth, stringer length, headroom clearance, and Blondel's comfort formula conforming to International Building Code (IBC) and IRC."
    h1 = "Stair Calculator"
    short_desc = "Compute precise stair riser count, tread run, stringer framing dimensions, pitch angle, and headroom clearance compliant with IRC and IBC architectural building codes."

    schema = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Stair Calculator",
      "url": "https://calchub.com/stair-calculator.html",
      "applicationCategory": "EngineeringApplication",
      "operatingSystem": "All",
      "description": "Calculate stair dimensions, stringer length, riser height, tread depth, incline angle, and code compliance per IRC and IBC standards.",
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
          "name": "What are the maximum riser height and minimum tread run limits under IRC and IBC?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Under the International Residential Code (IRC Section R311.7), maximum riser height is 7.75 inches (197 mm) and minimum tread depth is 10.0 inches (254 mm). Under the International Building Code (IBC Section 1011 for commercial buildings), standards are stricter: maximum riser height is 7.0 inches (178 mm) and minimum tread depth is 11.0 inches (279 mm)."
          }
        },
        {
          "@type": "Question",
          "name": "What is Blondel's formula for stair comfort?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Blondel's formula states that two risers plus one tread depth should equal the average human walking stride: 2 * Riser + Tread = 24 to 25 inches (61 to 64 cm). Staircases adhering to this ergonomic ratio provide natural gait cadence and significantly reduce trip-and-fall hazards."
          }
        },
        {
          "@type": "Question",
          "name": "What is the minimum required headroom clearance for a stairway?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Both the IRC (R311.7.2) and IBC (1011.3) mandate a minimum vertical headroom clearance of not less than 6 feet 8 inches (80 inches or 2032 mm). This distance is measured vertically from the sloped plane tangent to the tread nosings upward to the ceiling or floor structure above."
          }
        },
        {
          "@type": "Question",
          "name": "What is the minimum throat depth required on a wooden stair stringer?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "When notching a 2x12 lumber board for a cut stair stringer, building codes require maintaining a minimum uncut 'throat' depth (the perpendicular distance from the inside corner of the notch to the back edge of the board) of at least 3.5 to 5.0 inches (typically 5 inches minimum for 2x12 lumber) to preserve structural shear and bending resistance."
          }
        }
      ]
    }
  ]
}"""

    calc_ui = """<div class="calculator-form">
    <div class="calc-row">
        <div class="calc-field">
            <label for="st_total_rise">Total Vertical Rise (Inches):</label>
            <input type="number" id="st_total_rise" value="108" step="0.125" min="10">
            <small class="field-hint">Finished lower floor to finished upper floor (e.g., 9 ft = 108")</small>
        </div>
        <div class="calc-field">
            <label for="st_target_riser">Target Riser Height (Inches):</label>
            <input type="number" id="st_target_riser" value="7.25" step="0.125" min="5" max="8.5">
            <small class="field-hint">Ideal ergonomic riser height (~7.0" to 7.5")</small>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="st_tread_depth">Tread Run / Depth (Inches):</label>
            <input type="number" id="st_tread_depth" value="11.0" step="0.125" min="9" max="14">
            <small class="field-hint">Horizontal tread run without nosing (min 10" IRC, 11" IBC)</small>
        </div>
        <div class="calc-field">
            <label for="st_code_std">Building Code Profile:</label>
            <select id="st_code_std">
                <option value="irc" selected>IRC Residential (Max Rise 7.75", Min Run 10")</option>
                <option value="ibc">IBC Commercial (Max Rise 7.00", Min Run 11")</option>
            </select>
        </div>
    </div>
    <div class="calc-row">
        <div class="calc-field">
            <label for="st_headroom_open">Stairwell Opening Length (Inches):</label>
            <input type="number" id="st_headroom_open" value="120" step="1" min="36">
            <small class="field-hint">Length of ceiling opening above lower run for headroom check</small>
        </div>
        <div class="calc-field">
            <label for="st_floor_thickness">Upper Floor Floor Thickness (Inches):</label>
            <input type="number" id="st_floor_thickness" value="11.5" step="0.5" min="6">
            <small class="field-hint">Upper floor joist depth + subfloor + finish flooring</small>
        </div>
    </div>
    <button type="button" class="btn btn-primary" id="btn_calc_stair" style="width:100%; margin-top:1rem;">Calculate Stair Framing Dimensions</button>

    <div class="calc-results" id="st_results" style="margin-top:1.5rem;">
        <h3>Stair Engineering &amp; Framing Blueprint</h3>
        <div class="results-grid">
            <div class="result-item">
                <span class="result-label">Number of Risers:</span>
                <span class="result-value" id="res_st_num_risers">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Exact Riser Height:</span>
                <span class="result-value" id="res_st_rise_exact">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Number of Treads:</span>
                <span class="result-value" id="res_st_num_treads">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Total Horizontal Run:</span>
                <span class="result-value" id="res_st_total_run">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Stringer Length (Hypotenuse):</span>
                <span class="result-value" id="res_st_stringer">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Stair Incline / Pitch Angle:</span>
                <span class="result-value" id="res_st_angle">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Blondel's Comfort Index (2R + T):</span>
                <span class="result-value" id="res_st_blondel">--</span>
            </div>
            <div class="result-item">
                <span class="result-label">Calculated Headroom Clearance:</span>
                <span class="result-value" id="res_st_headroom">--</span>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    function calculateStairs() {
        const totalRise = parseFloat(document.getElementById('st_total_rise').value) || 108;
        const targetRiser = parseFloat(document.getElementById('st_target_riser').value) || 7.25;
        const treadDepth = parseFloat(document.getElementById('st_tread_depth').value) || 11.0;
        const codeStd = document.getElementById('st_code_std').value;
        const openingLen = parseFloat(document.getElementById('st_headroom_open').value) || 120;
        const floorThick = parseFloat(document.getElementById('st_floor_thickness').value) || 11.5;

        // Number of risers must be integer: round(totalRise / targetRiser)
        let numRisers = Math.round(totalRise / targetRiser);
        if (numRisers < 1) numRisers = 1;

        let exactRiser = totalRise / numRisers;

        // Number of treads is (numRisers - 1)
        const numTreads = numRisers - 1;

        // Total horizontal run
        const totalRun = numTreads * treadDepth;

        // Stringer diagonal length
        const stringerLen = Math.sqrt(Math.pow(totalRun, 2) + Math.pow(totalRise, 2));

        // Pitch angle: arctan(exactRiser / treadDepth)
        const pitchAngleRad = Math.atan(exactRiser / treadDepth);
        const pitchAngleDeg = (pitchAngleRad * 180 / Math.PI);

        // Blondel index: 2 * R + T (ideal: 24" - 25")
        const blondelVal = (2 * exactRiser) + treadDepth;
        let blondelStatus = "Optimal";
        if (blondelVal < 23.5) blondelStatus = "Too Steep / Short";
        else if (blondelVal > 25.5) blondelStatus = "Too Flat / Long";

        // Headroom calculation:
        // Lower run begins at x = 0. Upper floor header is located at x = (totalRun - openingLen).
        // Vertical height of stair at header: y_stair = (totalRun - openingLen) * (totalRise / totalRun)
        // Ceiling height at that point: totalRise - floorThick
        // Headroom = (totalRise - floorThick) - y_stair
        let headroom = 0;
        if (openingLen < totalRun) {
            const xHeader = totalRun - openingLen;
            const yAtHeader = xHeader * (totalRise / totalRun);
            headroom = (totalRise - floorThick) - yAtHeader;
        } else {
            headroom = totalRise + 30; // completely open stairwell
        }

        // Code check
        let maxRiseLimit = (codeStd === 'irc') ? 7.75 : 7.00;
        let minRunLimit = (codeStd === 'irc') ? 10.0 : 11.0;
        let codeCompliant = (exactRiser <= maxRiseLimit) && (treadDepth >= minRunLimit) && (headroom >= 80);

        const riseFraction = exactRiser.toFixed(3) + '" (' + Math.round(exactRiser * 16) / 16 + '")';
        const totalRunFt = Math.floor(totalRun / 12) + "'-" + (totalRun % 12).toFixed(1) + '"';
        const stringerFt = Math.floor(stringerLen / 12) + "'-" + (stringerLen % 12).toFixed(1) + '" (' + stringerLen.toFixed(1) + '")';
        const headroomFt = Math.floor(headroom / 12) + "'-" + (headroom % 12).toFixed(1) + '"';

        document.getElementById('res_st_num_risers').textContent = numRisers + " risers";
        document.getElementById('res_st_rise_exact').textContent = riseFraction + (exactRiser <= maxRiseLimit ? " [PASS]" : " [EXCEEDS CODE]");
        document.getElementById('res_st_num_treads').textContent = numTreads + " treads";
        document.getElementById('res_st_total_run').textContent = totalRunFt + " (" + totalRun.toFixed(1) + '")';
        document.getElementById('res_st_stringer').textContent = stringerFt;
        document.getElementById('res_st_angle').textContent = pitchAngleDeg.toFixed(1) + "°";
        document.getElementById('res_st_blondel').textContent = blondelVal.toFixed(2) + '" (' + blondelStatus + ')';
        document.getElementById('res_st_headroom').textContent = headroomFt + (headroom >= 80 ? " [PASS ≥ 80\"]" : " [FAIL < 80\"]");
    }

    document.getElementById('btn_calc_stair').addEventListener('click', calculateStairs);
    calculateStairs();
});
</script>"""

    article_content = """<h2>1. Architectural Stair Anatomy &amp; Geometric Principles</h2>
<p>In architectural and structural engineering, staircase design requires resolving vertical circulation within rigid three-dimensional boundaries while rigorously observing life-safety codes. A poorly proportioned stairway creates immediate fall hazards, causes physiological fatigue, and violates building regulations.</p>

<p>Every standard straight-run staircase consists of essential structural elements:</p>
<ul>
    <li><strong>Total Rise:</strong> The exact finished vertical dimension measured from the surface of the finished lower floor to the surface of the finished upper floor landing.</li>
    <li><strong>Riser Height (\(R\)):</strong> The vertical face between two consecutive stair treads. Under modern building codes, all risers within a flight must be identical to within \(3/8\text{ inch}\) (\(9.5\text{ mm}\)) tolerance to prevent tripping.</li>
    <li><strong>Tread Depth / Run (\(T\)):</strong> The horizontal distance measured between the leading edge of consecutive step nosings.</li>
    <li><strong>Total Run:</strong> The overall horizontal floor space occupied by the flight of stairs from the bottom riser face to the top landing face. Because the upper finished floor acts as the final step, the number of treads is always exactly one fewer than the number of risers (\(N_{treads} = N_{risers} - 1\)).</li>
    <li><strong>Stringers (Carriages):</strong> The sloped structural timber, steel, or concrete beams (typically cut from \(2\times 12\) lumber) that support the treads and risers.</li>
</ul>

<h2>2. International Building Codes: IRC vs. IBC Dimensional Mandates</h2>
<p>Modern building jurisdictions enforce staircase parameters defined by either the <strong>International Residential Code (IRC)</strong> for one- and two-family dwellings, or the <strong>International Building Code (IBC)</strong> for commercial, institutional, and multi-family occupancies:</p>

<h3>IRC Section R311.7 (Residential Standards)</h3>
<ul>
    <li><strong>Maximum Riser Height:</strong> \(7\frac{3}{4}\text{ inches}\) (\(197\text{ mm}\)).</li>
    <li><strong>Minimum Tread Depth:</strong> \(10\text{ inches}\) (\(254\text{ mm}\)).</li>
    <li><strong>Minimum Stair Width:</strong> \(36\text{ inches}\) (\(914\text{ mm}\)) clear above the handrail.</li>
    <li><strong>Minimum Headroom:</strong> \(6\text{ feet } 8\text{ inches}\) (\(80\text{ inches}\) or \(2{,}032\text{ mm}\)) measured vertically from the sloped plane tangent to tread nosings.</li>
    <li><strong>Maximum Dimension Variation:</strong> The greatest riser height or tread depth within any flight must not exceed the smallest by more than \(3/8\text{ inch}\) (\(9.5\text{ mm}\)).</li>
</ul>

<h3>IBC Section 1011 (Commercial Standards)</h3>
<ul>
    <li><strong>Maximum Riser Height:</strong> \(7.0\text{ inches}\) (\(178\text{ mm}\)) (with a minimum of \(4.0\text{ inches}\)).</li>
    <li><strong>Minimum Tread Depth:</strong> \(11.0\text{ inches}\) (\(279\text{ mm}\)).</li>
    <li><strong>Minimum Stair Width:</strong> \(44\text{ inches}\) (\(1{,}118\text{ mm}\)) for occupant load &ge; 50; \(36\text{ inches}\) for &lt; 50.</li>
    <li><strong>Minimum Headroom:</strong> \(80\text{ inches}\) (\(2{,}032\text{ mm}\)) continuous throughout the flight and landings.</li>
</ul>

<h2>3. Mathematical Formulations &amp; Ergonomic Walking Rules</h2>
<p>To establish perfect layout dimensions, the total vertical rise is divided into integer riser increments, from which remaining geometry is derived:</p>

<h3>Riser Count and Exact Riser Height</h3>
$$N_{risers} = \text{round}\left(\frac{\text{Total Rise}}{R_{target}}\right)$$

$$R_{exact} = \frac{\text{Total Rise}}{N_{risers}}$$

<h3>Total Horizontal Run and Stringer Diagonal</h3>
$$N_{treads} = N_{risers} - 1$$

$$\text{Total Run} = N_{treads} \times T$$

$$\text{Stringer Length} = \sqrt{(\text{Total Run})^2 + (\text{Total Rise})^2}$$

<h3>Stair Incline Pitch Angle (\(\theta\))</h3>
$$\theta = \arctan\left(\frac{R_{exact}}{T}\right) \times \left(\frac{180}{\pi}\right)$$

<p>Optimal architectural stair slope ranges strictly between <strong>\(30^\circ\) and \(37^\circ\)</strong>. Slopes steeper than \(40^\circ\) induce severe forward-pitch discomfort during descent, while angles below \(25^\circ\) waste floor space and disrupt natural pedestrian stride.</p>

<h3>Blondel's Ergonomic Walking Stride Formula</h3>
<p>Formulated in 1675 by French architect Nicolas-François Blondel in his treatise <em>Cours d'architecture</em>, the universal rule of stair comfort asserts that the effort expended in climbing vertically equals approximately twice the effort of walking horizontally:</p>

$$2R + T = 24\text{ to } 25\text{ inches } (610\text{ to } 635\text{ mm})$$

<p>Other traditional architectural rules of thumb include:</p>
<ul>
    <li><strong>Riser + Tread Rule:</strong> \(R + T \approx 17\text{ to } 18\text{ inches}\)</li>
    <li><strong>Product Rule:</strong> \(R \times T \approx 72\text{ to } 75\)</li>
</ul>

<h2>4. Structural Stringer Lumber Sizing &amp; Throat Depth Table</h2>
<p>The following engineering data table provides structural recommendations for cutting wooden stringers from dimensional lumber, specifying minimum uncut throat depth and allowable maximum stringer spans:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Lumber Stock</th>
            <th>Actual Dimensions</th>
            <th>Min Uncut Throat Depth</th>
            <th>Max Stringer Clear Span (Residential)</th>
            <th>Max Clear Span with Center Support</th>
            <th>Recommended Material Grade</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>2 x 10 Lumber</strong></td>
            <td>1.5" x 9.25"</td>
            <td>3.5" (Marginal)</td>
            <td>6 ft – 0 in</td>
            <td>12 ft – 0 in</td>
            <td>#2 Douglas Fir / Southern Pine</td>
        </tr>
        <tr>
            <td><strong>2 x 12 Lumber (Standard)</strong></td>
            <td>1.5" x 11.25"</td>
            <td><strong>5.0" (Code Recommended)</strong></td>
            <td>10 ft – 6 in</td>
            <td>18 ft – 0 in</td>
            <td>Select Structural / #1 Southern Pine</td>
        </tr>
        <tr>
            <td><strong>1.75" x 11.875" LVL</strong></td>
            <td>Laminated Veneer Lumber</td>
            <td>5.5"</td>
            <td>14 ft – 0 in</td>
            <td>24 ft – 0 in</td>
            <td>2.0E / 2900Fb Engineered Wood</td>
        </tr>
        <tr>
            <td><strong>Steel C-Channel (C10x15.3)</strong></td>
            <td>Structural Steel Channel</td>
            <td>Full Web (10")</td>
            <td>20 ft – 0 in</td>
            <td>35 ft – 0 in</td>
            <td>ASTM A36 Structural Steel</td>
        </tr>
    </tbody>
</table>

<h2>5. Headroom Geometry and Floor Opening Calculation</h2>
<p>Inadequate headroom represents the single most expensive error in residential carpentry, frequently requiring structural ceiling framing alterations after drywall installation. Headroom clearance \(H\) is calculated directly from the stairwell opening length \(L_{open}\) and upper floor assembly thickness \(t_{floor}\) (joist height + subfloor + flooring):</p>

$$H = (\text{Total Rise} - t_{floor}) - \left[(\text{Total Run} - L_{open}) \times \left(\frac{\text{Total Rise}}{\text{Total Run}}\right)\right]$$

<p>If \(H &lt; 80\text{ inches}\) (\(2{,}032\text{ mm}\)), the stairwell ceiling opening must be lengthened or the stair incline altered to ensure full head clearance.</p>

<h2>6. Worked Framing Case Study: 9-Foot Finished Ceiling Residential Stair</h2>
<div class="worked-example-card">
    <h3>Design Specification: Two-Story Residential Foyer Stairway</h3>
    <p>A builder is framing an interior straight-run stairway between the ground floor and second floor. Measurements establish a <strong>Total Vertical Rise = 108.0 inches</strong> (9 ft 0 in finished floor to finished floor). The ceiling opening length in the second-floor framing is \(L_{open} = 120\text{ inches}\), and the upper floor framing thickness is \(t_{floor} = 11.5\text{ inches}\) (10" I-joists + 3/4" subfloor + 3/4" hardwood). Target riser height is \(7.25\text{ inches}\), and desired tread run is \(11.0\text{ inches}\). Sized under the <strong>IRC Residential Building Code</strong>.</p>

    <div class="step-solution">
        <h4>Step 1: Calculate Number of Risers and Exact Riser Height</h4>
        $$N_{risers} = \text{round}\left(\frac{108.0}{7.25}\right) = \text{round}(14.896) = 15\text{ risers}$$
        $$R_{exact} = \frac{108.0\text{ inches}}{15} = 7.20\text{ inches} \approx 7\frac{3}{16}\text{ inches}$$
        <p>Verification against IRC: \(7.20\text{ in} \le 7.75\text{ in}\) max permissible riser. <strong>[PASS]</strong></p>

        <h4>Step 2: Calculate Number of Treads and Total Horizontal Run</h4>
        $$N_{treads} = 15 - 1 = 14\text{ treads}$$
        $$\text{Total Run} = 14 \times 11.0\text{ inches} = 154.0\text{ inches} = 12\text{ ft } 10\text{ in}$$
        <p>Verification against IRC: \(11.0\text{ in} \ge 10.0\text{ in}\) minimum tread run. <strong>[PASS]</strong></p>

        <h4>Step 3: Evaluate Blondel's Comfort Formula</h4>
        $$2R + T = (2 \times 7.20) + 11.0 = 14.40 + 11.0 = 25.40\text{ inches}$$
        <p>This falls squarely within the ergonomic ideal walking stride range of \(24.0\) to \(25.5\text{ inches}\), delivering an easy, fatigue-free ascent.</p>

        <h4>Step 4: Compute Stringer Length and Pitch Angle</h4>
        $$\text{Stringer Length} = \sqrt{(154.0)^2 + (108.0)^2} = \sqrt{23{,}716 + 11{,}664} = \sqrt{35{,}380} \approx 188.10\text{ inches} \approx 15\text{ ft } 8\frac{1}{8}\text{ in}$$
        $$\theta = \arctan\left(\frac{7.20}{11.0}\right) = \arctan(0.6545) \approx 33.2^\circ$$
        <p>A pitch angle of \(33.2^\circ\) represents the optimal architectural envelope for residential stairways.</p>

        <h4>Step 5: Verify Minimum Headroom Clearance</h4>
        <p>Distance from lower start to upper ceiling opening header: \(\text{Total Run} - L_{open} = 154.0 - 120.0 = 34.0\text{ inches}\).</p>
        <p>Height of stair surface directly below header:</p>
        $$y_{header} = 34.0 \times \left(\frac{108.0}{154.0}\right) = 34.0 \times 0.7013 = 23.84\text{ inches}$$
        <p>Ceiling height at header: \(\text{Total Rise} - t_{floor} = 108.0 - 11.5 = 96.5\text{ inches}\).</p>
        <p>Clear headroom vertically above tread nosing:</p>
        $$H = 96.5\text{ in} - 23.84\text{ in} = 72.66\text{ inches}$$
        <p><strong>Code Warning:</strong> \(72.66\text{ inches} &lt; 80.0\text{ inches}\) IRC minimum required headroom! To achieve compliant \(80\text{''}\) clearance, the ceiling opening length \(L_{open}\) must be extended from \(120\text{''}\) to at least \(130.5\text{ inches}\).</p>
    </div>
</div>

<h2>7. Frequently Asked Questions</h2>
<div class="faq-accordion">
    <div class="faq-item">
        <h3>What are the maximum riser height and minimum tread run limits under IRC and IBC?</h3>
        <p>Under the International Residential Code (IRC Section R311.7), maximum riser height is 7.75 inches (197 mm) and minimum tread depth is 10.0 inches (254 mm). Under the International Building Code (IBC Section 1011 for commercial buildings), standards are stricter: maximum riser height is 7.0 inches (178 mm) and minimum tread depth is 11.0 inches (279 mm).</p>
    </div>
    <div class="faq-item">
        <h3>What is Blondel's formula for stair comfort?</h3>
        <p>Blondel's formula states that two risers plus one tread depth should equal the average human walking stride: \(2R + T = 24\text{ to } 25\text{ inches}\) (\(61\text{ to } 64\text{ cm}\)). Staircases adhering to this ergonomic ratio provide natural gait cadence and significantly reduce trip-and-fall hazards.</p>
    </div>
    <div class="faq-item">
        <h3>What is the minimum required headroom clearance for a stairway?</h3>
        <p>Both the IRC (R311.7.2) and IBC (1011.3) mandate a minimum vertical headroom clearance of not less than 6 feet 8 inches (80 inches or 2,032 mm). This distance is measured vertically from the sloped plane tangent to the tread nosings upward to the ceiling or floor structure above.</p>
    </div>
    <div class="faq-item">
        <h3>What is the minimum throat depth required on a wooden stair stringer?</h3>
        <p>When notching a 2x12 lumber board for a cut stair stringer, building codes require maintaining a minimum uncut "throat" depth (the perpendicular distance from the inside corner of the notch to the back edge of the board) of at least 3.5 to 5.0 inches (typically 5 inches minimum for 2x12 lumber) to preserve structural shear and bending resistance.</p>
    </div>
</div>"""

    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article_content, "civil.html", "Civil Engineering")


def main():
    tools = [
        ("neutral-conductor-sizing-calculator.html", gen_neutral_sizing()),
        ("stair-calculator.html", gen_stair_calculator())
    ]
    for filename, content in tools:
        filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {filename}")

if __name__ == "__main__":
    main()
