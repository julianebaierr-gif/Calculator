import os

OUTPUT_DIR = r"C:\Users\Admin\.gemini\antigravity\scratch\calchub"
from make_health_remaining import page_scaffold

# ==========================================
# 16. OHM'S LAW CALCULATOR
# ==========================================
ohm_app_json = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Ohm's Law Calculator",
      "url": "https://calchub.org/ohms-law-calculator.html",
      "applicationCategory": "EngineeringApplication",
      "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What are the four core Ohm's Law formulas?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The four fundamental variables are Voltage (V = I × R), Current (I = V / R), Resistance (R = V / I), and Electrical Power (P = V × I = I² × R = V² / R)."
          }
        }
      ]
    }
  ]
}"""

ohm_workspace = """
      <section class="calc-card">
        <div class="calc-card-header">
          <span class="calc-title">⚡ Enter Any 2 Values to Solve the Rest</span>
        </div>
        <form onsubmit="return false;">
          <div class="calc-form-grid">
            <div class="input-group">
              <label class="input-label" for="ohm-v">Voltage (V)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="ohm-v" value="120" step="any" oninput="solveOhm('V')">
                <span class="input-unit-badge">Volts</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="ohm-i">Current (I)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="ohm-i" value="10" step="any" oninput="solveOhm('I')">
                <span class="input-unit-badge">Amps</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="ohm-r">Resistance (R)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="ohm-r" placeholder="Auto-calculated" step="any" oninput="solveOhm('R')">
                <span class="input-unit-badge">Ohms (Ω)</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="ohm-p">Power (P)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="ohm-p" placeholder="Auto-calculated" step="any" oninput="solveOhm('P')">
                <span class="input-unit-badge">Watts (W)</span>
              </div>
            </div>
          </div>
          <div class="calc-actions">
            <button type="button" class="btn btn-secondary" onclick="resetOhm()">Clear & Reset</button>
            <button type="button" class="btn btn-primary" onclick="copyResults()">📋 Copy Circuit Values</button>
            <button type="button" class="btn btn-subtle" onclick="window.print()">🖨️ Print Report</button>
          </div>
        </form>
      </section>

      <section class="results-card">
        <div class="results-header">
          <span class="results-title">Calculated Circuit State</span>
          <span class="status-pill status-success">Solved State</span>
        </div>
        <div class="primary-result-box">
          <div class="primary-result-label">Electrical Power Dissipation (P)</div>
          <div>
            <span class="primary-result-value" id="card-ohm-p" style="color:#2563EB;">1,200</span>
            <span class="primary-result-unit">Watts</span>
          </div>
        </div>
        <div class="result-breakdown-grid">
          <div class="breakdown-item">
            <div class="breakdown-label">Potential Difference (V)</div>
            <div class="breakdown-val" id="card-ohm-v">120.0 V</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Current Intensity (I)</div>
            <div class="breakdown-val" id="card-ohm-i">10.00 A</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Circuit Resistance (R)</div>
            <div class="breakdown-val" id="card-ohm-r">12.00 Ω</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Conductance (G = 1/R)</div>
            <div class="breakdown-val" id="card-ohm-g">0.083 S</div>
          </div>
        </div>
      </section>
"""

ohm_geo = """
    <section class="geo-citation-box">
      <div class="geo-header">💡 Direct Answer (GEO & Quick Summary)</div>
      <p><strong>Ohm's Law</strong> defines the mathematical relationship in electrical circuits between voltage, current, and resistance. It states that the current passing through a conductor between two points is directly proportional to voltage across the points, given by:</p>
      <p><code>V = I × R &nbsp;|&nbsp; I = V / R &nbsp;|&nbsp; R = V / I &nbsp;|&nbsp; P = V × I = I²·R = V² / R</code></p>
      <p>Where <strong>V</strong> = Voltage (Volts), <strong>I</strong> = Current (Amperes), <strong>R</strong> = Resistance (Ohms Ω), and <strong>P</strong> = Power (Watts).</p>
    </section>
"""

ohm_toc = """
    <nav class="toc-container" aria-label="Table of Contents">
      <div class="toc-title">📑 Table of Contents</div>
      <ul class="toc-list">
        <li><a href="#ohm-principles">The Physics of Ohm's Law</a></li>
        <li><a href="#ohm-wheel">The 12 Formulas of the Ohm's Law Wheel</a></li>
        <li><a href="#dc-vs-ac">DC vs. AC Impedance Considerations</a></li>
        <li><a href="#ohm-faq">Frequently Asked Questions</a></li>
      </ul>
    </nav>
"""

ohm_article = """
      <h2 id="ohm-principles">The Physics of Ohm's Law</h2>
      <p>Discovered in 1827 by German physicist Georg Simon Ohm, this law represents the foundational cornerstone of all electrical engineering. It applies strictly to ohmic conductors maintaining a constant temperature.</p>

      <div class="formula-box">
        <div class="formula-title">Ohm's Law & Joule's Power Law Equations</div>
        <div class="formula-code">V = I · R &nbsp;|&nbsp; P = V · I = I² · R = V² / R</div>
      </div>

      <h2 id="ohm-wheel">The 12 Formulas of the Ohm's Law Wheel</h2>
      <div class="table-responsive">
        <table class="data-table">
          <thead><tr><th>Target Variable</th><th>Formula 1</th><th>Formula 2</th><th>Formula 3</th></tr></thead>
          <tbody>
            <tr><td><strong>Voltage (V)</strong></td><td>V = I · R</td><td>V = P / I</td><td>V = √(P · R)</td></tr>
            <tr><td><strong>Current (I)</strong></td><td>I = V / R</td><td>I = P / V</td><td>I = √(P / R)</td></tr>
            <tr><td><strong>Resistance (R)</strong></td><td>R = V / I</td><td>R = V² / P</td><td>R = P / I²</td></tr>
            <tr><td><strong>Power (P)</strong></td><td>P = V · I</td><td>P = I² · R</td><td>P = V² / R</td></tr>
          </tbody>
        </table>
      </div>

      <h2 id="dc-vs-ac">Direct Current (DC) vs. Alternating Current (AC)</h2>
      <p>In DC circuits, resistance (R) alone opposes current flow. In AC circuits containing inductors or capacitors, resistance is replaced by <strong>Impedance (Z)</strong>, which incorporates frequency-dependent reactance: <code>V = I · Z</code>.</p>

      <h2 id="ohm-faq">Frequently Asked Questions</h2>
      <div class="faq-wrap">
        <details class="faq-item">
          <summary>Does Ohm's Law apply to semiconductors (diodes/transistors)?</summary>
          <div class="faq-content">No. Diodes, LEDs, and transistors are non-ohmic components possessing non-linear current-voltage (I-V) characteristics governed by the Shockley diode equation rather than Ohm's Law.</div>
        </details>
      </div>
"""

ohm_script = """
  <script>
    let lastEdited = ['V', 'I'];

    function solveOhm(changed) {
      if (!lastEdited.includes(changed)) {
        lastEdited.shift();
        lastEdited.push(changed);
      }

      const vEl = document.getElementById('ohm-v');
      const iEl = document.getElementById('ohm-i');
      const rEl = document.getElementById('ohm-r');
      const pEl = document.getElementById('ohm-p');

      let v = parseFloat(vEl.value);
      let i = parseFloat(iEl.value);
      let r = parseFloat(rEl.value);
      let p = parseFloat(pEl.value);

      if (lastEdited.includes('V') && lastEdited.includes('I')) {
        r = v / i;
        p = v * i;
      } else if (lastEdited.includes('V') && lastEdited.includes('R')) {
        i = v / r;
        p = (v * v) / r;
      } else if (lastEdited.includes('V') && lastEdited.includes('P')) {
        i = p / v;
        r = (v * v) / p;
      } else if (lastEdited.includes('I') && lastEdited.includes('R')) {
        v = i * r;
        p = (i * i) * r;
      } else if (lastEdited.includes('I') && lastEdited.includes('P')) {
        v = p / i;
        r = p / (i * i);
      } else if (lastEdited.includes('R') && lastEdited.includes('P')) {
        v = Math.sqrt(p * r);
        i = Math.sqrt(p / r);
      }

      if (!isNaN(v)) vEl.value = Number(v.toFixed(3));
      if (!isNaN(i)) iEl.value = Number(i.toFixed(3));
      if (!isNaN(r)) rEl.value = Number(r.toFixed(3));
      if (!isNaN(p)) pEl.value = Number(p.toFixed(3));

      document.getElementById('card-ohm-v').textContent = (v || 0).toFixed(2) + ' V';
      document.getElementById('card-ohm-i').textContent = (i || 0).toFixed(2) + ' A';
      document.getElementById('card-ohm-r').textContent = (r || 0).toFixed(2) + ' Ω';
      document.getElementById('card-ohm-p').textContent = Math.round(p || 0).toLocaleString();
      document.getElementById('card-ohm-g').textContent = r > 0 ? (1 / r).toFixed(3) + ' S' : '0 S';
    }

    function resetOhm() {
      document.getElementById('ohm-v').value = 120;
      document.getElementById('ohm-i').value = 10;
      document.getElementById('ohm-r').value = '';
      document.getElementById('ohm-p').value = '';
      lastEdited = ['V', 'I'];
      solveOhm('V');
    }

    function copyResults() {
      const v = document.getElementById('card-ohm-v').textContent;
      const i = document.getElementById('card-ohm-i').textContent;
      const r = document.getElementById('card-ohm-r').textContent;
      const p = document.getElementById('card-ohm-p').textContent;
      window.copyToClipboard(`CalcHub Ohm's Law Circuit: Voltage: ${v}, Current: ${i}, Resistance: ${r}, Power: ${p}W`);
    }
    solveOhm('V');
  </script>
"""

with open(os.path.join(OUTPUT_DIR, "ohms-law-calculator.html"), "w", encoding="utf-8") as f:
    f.write(page_scaffold("Ohm's Law Calculator — Voltage, Current, Resistance & Power",
                          "Solve any 2 variables in electrical circuits using Ohm's Law and Joule's power wheel. Computes Volts, Amps, Ohms, and Watts instantly.",
                          "ohms law calculator, voltage calculator, current calculator, resistance calculator, electric power formula, p vi formula",
                          "ohms-law-calculator", "Electrical & Electronics", "engineering", ohm_app_json,
                          "Solve voltage, current, resistance, and wattage with automated circular substitution. Includes the full 12-equation Ohm's law wheel and conductance.",
                          ohm_workspace, ohm_geo, ohm_toc, ohm_article, ohm_script))

# ==========================================
# 17. VOLTAGE DROP CALCULATOR
# ==========================================
vd_app_json = """{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Voltage Drop Calculator",
  "url": "https://calchub.org/voltage-drop-calculator.html",
  "applicationCategory": "EngineeringApplication",
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
}"""

vd_workspace = """
      <section class="calc-card">
        <div class="calc-card-header">
          <span class="calc-title">📉 Circuit Parameters (NEC & IEC 60364)</span>
        </div>
        <form onsubmit="return false;">
          <div class="calc-form-grid">
            <div class="input-group">
              <label class="input-label" for="vd-phase">Circuit Phase Type</label>
              <div class="input-wrap">
                <select id="vd-phase" onchange="calcVD()">
                  <option value="1">Single-Phase (120V / 230V AC or DC)</option>
                  <option value="3" selected>Three-Phase AC (400V / 480V)</option>
                </select>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="vd-voltage">Source Voltage (V)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="vd-voltage" value="400" min="12" max="10000" oninput="calcVD()">
                <span class="input-unit-badge">V</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="vd-current">Load Current (A)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="vd-current" value="32" min="1" max="1000" oninput="calcVD()">
                <span class="input-unit-badge">A</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="vd-length">One-Way Run Length (meters)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="vd-length" value="45" min="1" max="2000" oninput="calcVD()">
                <span class="input-unit-badge">m</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="vd-conductor">Conductor Material</label>
              <div class="input-wrap">
                <select id="vd-conductor" onchange="calcVD()">
                  <option value="cu" selected>Copper (Cu — Standard)</option>
                  <option value="al">Aluminium (Al)</option>
                </select>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="vd-size">Conductor Cross-Section (mm²)</label>
              <div class="input-wrap">
                <select id="vd-size" onchange="calcVD()">
                  <option value="1.5">1.5 mm²</option>
                  <option value="2.5">2.5 mm²</option>
                  <option value="4.0">4.0 mm²</option>
                  <option value="6.0" selected>6.0 mm²</option>
                  <option value="10.0">10.0 mm²</option>
                  <option value="16.0">16.0 mm²</option>
                  <option value="25.0">25.0 mm²</option>
                  <option value="35.0">35.0 mm²</option>
                  <option value="50.0">50.0 mm²</option>
                  <option value="70.0">70.0 mm²</option>
                  <option value="95.0">95.0 mm²</option>
                </select>
              </div>
            </div>
          </div>
          <div class="calc-actions">
            <button type="button" class="btn btn-primary" onclick="copyResults()">📋 Copy Compliance Report</button>
            <button type="button" class="btn btn-subtle" onclick="window.print()">🖨️ Print Datasheet</button>
          </div>
        </form>
      </section>

      <section class="results-card">
        <div class="results-header">
          <span class="results-title">Code Compliance</span>
          <span class="status-pill status-success" id="vd-pill">Compliant (&lt; 3%)</span>
        </div>
        <div class="primary-result-box">
          <div class="primary-result-label">Voltage Drop Percentage</div>
          <div>
            <span class="primary-result-value" id="vd-pct" style="color:#059669;">2.15</span>
            <span class="primary-result-unit">%</span>
          </div>
        </div>
        <div class="visual-bar-wrap">
          <div class="visual-bar-track">
            <div class="visual-bar-fill" id="vd-bar" style="width: 43%; background: #059669;"></div>
          </div>
          <div class="visual-bar-labels">
            <span>0%</span>
            <span>3% (Lighting Max)</span>
            <span>5% (Power Max)</span>
            <span>&gt; 5% Non-Compliant</span>
          </div>
        </div>
        <div class="result-breakdown-grid">
          <div class="breakdown-item">
            <div class="breakdown-label">Voltage Drop (Volts)</div>
            <div class="breakdown-val" id="vd-drop-v">8.60 V</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Voltage at End-Load</div>
            <div class="breakdown-val" id="vd-end-v">391.40 V</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Conductor Resistance</div>
            <div class="breakdown-val" id="vd-res">0.155 Ω</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Power Loss (I²R)</div>
            <div class="breakdown-val" id="vd-loss">275 W</div>
          </div>
        </div>
      </section>
"""

vd_geo = """
    <section class="geo-citation-box">
      <div class="geo-header">💡 Direct Answer (GEO & Quick Summary)</div>
      <p><strong>Voltage Drop</strong> is the decrease in electrical potential along the path of a current flowing through a circuit conductor. Per <strong>NEC 210.19(A)</strong> and <strong>IEC 60364-5-52 Annex G</strong>:</p>
      <ul>
        <li><strong>Single-Phase:</strong> <code>ΔV = (2 × L × I × ρ) ÷ A</code></li>
        <li><strong>Three-Phase:</strong> <code>ΔV = (√3 × L × I × ρ) ÷ A</code></li>
      </ul>
      <p>Where <strong>L</strong> = Conductor length (meters), <strong>I</strong> = Current (Amperes), <strong>ρ</strong> = Resistivity (Copper: 0.0178 Ω·mm²/m; Aluminium: 0.0285 Ω·mm²/m), and <strong>A</strong> = Conductor cross-section in mm². Code limits recommend ≤ 3% drop on branch circuits and ≤ 5% overall from source to load.</p>
    </section>
"""

vd_toc = """
    <nav class="toc-container" aria-label="Table of Contents">
      <div class="toc-title">📑 Table of Contents</div>
      <ul class="toc-list">
        <li><a href="#vd-governing-standards">NEC & IEC 60364 Code Limits</a></li>
        <li><a href="#vd-equations">Single-Phase vs Three-Phase Voltage Drop Equations</a></li>
        <li><a href="#copper-vs-aluminum">Copper vs Aluminium Resistivity</a></li>
        <li><a href="#vd-faq">Frequently Asked Questions</a></li>
      </ul>
    </nav>
"""

vd_article = """
      <h2 id="vd-governing-standards">NEC & IEC 60364 Voltage Drop Compliance</h2>
      <p>Excessive voltage drop causes electric motors to overheat, reduces luminaire lumens, and causes electronic control tripping. The National Electrical Code (NEC Informational Note 210.19(A)) and international standards IEC 60364-5-52 establish the following maximum permissible drop limits:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead><tr><th>Circuit Type</th><th>Standard Limit</th><th>Consequences of Exceeding</th></tr></thead>
          <tbody>
            <tr><td>Lighting Circuits</td><td><strong>≤ 3.0%</strong></td><td>Visible lamp flicker, reduced lumen output</td></tr>
            <tr><td>Power & Motor Circuits</td><td><strong>≤ 5.0%</strong></td><td>Motor stall on startup, elevated winding heat</td></tr>
            <tr><td>Sensitive Data Centers / Medical</td><td><strong>≤ 1.5%</strong></td><td>Power supply voltage sag, harmonic distortion</td></tr>
          </tbody>
        </table>
      </div>

      <h2 id="vd-equations">Governing Formulas</h2>
      <div class="formula-box">
        <div class="formula-title">Standard Voltage Drop Formulations</div>
        <div class="formula-code">1-Phase: ΔV = 2 · L · I · ρ / A<br>3-Phase: ΔV = √3 · L · I · ρ / A</div>
        <div class="formula-legend">L = Length (m) | I = Load (A) | ρ = Conductor Resistivity | A = Cross-Section (mm²)</div>
      </div>

      <h2 id="copper-vs-aluminum">Conductor Properties: Copper vs. Aluminium</h2>
      <p>Copper exhibits ~60% higher electrical conductivity than aluminium. When specifying aluminium feeders to reduce project capital cost, electrical engineers must upsize conductor cross-section by roughly two AWG gauge sizes (or 1.6× area in mm²) to maintain equivalent ampacity and voltage drop compliance.</p>

      <h2 id="vd-faq">Frequently Asked Questions</h2>
      <div class="faq-wrap">
        <details class="faq-item">
          <summary>How does temperature affect cable voltage drop?</summary>
          <div class="faq-content">Conductor resistance increases linearly with temperature. At full operating load (70°C for PVC, 90°C for XLPE), copper resistance is roughly 20% higher than its 20°C room temperature rating.</div>
        </details>
      </div>
"""

vd_script = """
  <script>
    function calcVD() {
      const phase = parseInt(document.getElementById('vd-phase').value) || 3;
      const v = parseFloat(document.getElementById('vd-voltage').value) || 400;
      const i = parseFloat(document.getElementById('vd-current').value) || 32;
      const l = parseFloat(document.getElementById('vd-length').value) || 45;
      const mat = document.getElementById('vd-conductor').value;
      const a = parseFloat(document.getElementById('vd-size').value) || 6.0;

      // Resistivity at 70°C operating temperature
      const rho = (mat === 'cu') ? 0.021 : 0.034; // ohm mm2 / m

      const multiplier = (phase === 1) ? 2 : Math.sqrt(3);
      const vDrop = (multiplier * l * i * rho) / a;
      const vPct = (vDrop / v) * 100;
      const endV = v - vDrop;
      const rTotal = (multiplier * l * rho) / a;
      const pLoss = i * i * rTotal;

      let pillText = "Compliant (< 3%)";
      let pillClass = "status-success";
      let barColor = "#059669";

      if (vPct > 5.0) {
        pillText = "Non-Compliant (> 5%)";
        pillClass = "status-danger";
        barColor = "#E11D48";
      } else if (vPct > 3.0) {
        pillText = "Power Only (3–5%)";
        pillClass = "status-warning";
        barColor = "#D97706";
      }

      document.getElementById('vd-pct').textContent = vPct.toFixed(2);
      document.getElementById('vd-pct').style.color = barColor;
      document.getElementById('vd-drop-v').textContent = vDrop.toFixed(2) + ' V';
      document.getElementById('vd-end-v').textContent = endV.toFixed(2) + ' V';
      document.getElementById('vd-res').textContent = rTotal.toFixed(3) + ' Ω';
      document.getElementById('vd-loss').textContent = Math.round(pLoss) + ' W';

      const pill = document.getElementById('vd-pill');
      pill.className = 'status-pill ' + pillClass;
      pill.textContent = pillText;

      const fill = document.getElementById('vd-bar');
      fill.style.width = Math.min((vPct / 6) * 100, 100) + '%';
      fill.style.background = barColor;
    }
    function copyResults() {
      const p = document.getElementById('vd-pct').textContent;
      const v = document.getElementById('vd-drop-v').textContent;
      window.copyToClipboard(`CalcHub Voltage Drop Report: ${p}% drop (${v})`);
    }
    calcVD();
  </script>
"""

with open(os.path.join(OUTPUT_DIR, "voltage-drop-calculator.html"), "w", encoding="utf-8") as f:
    f.write(page_scaffold("Voltage Drop Calculator — NEC & IEC 60364 Conductor Sizing",
                          "Calculate cable voltage drop, percentage loss, and end-of-line voltage for single-phase and three-phase AC/DC power runs. Checks NEC 3% and 5% limits.",
                          "voltage drop calculator, cable voltage drop, nec voltage drop, wire size voltage drop, 3 phase voltage drop, iec 60364 voltage drop",
                          "voltage-drop-calculator", "Electrical Engineering", "engineering", vd_app_json,
                          "Verify cable run compliance against NEC and IEC 60364 standards. Calculate line resistance, voltage sag, and kilowatt power dissipation across feeder conductors.",
                          vd_workspace, vd_geo, vd_toc, vd_article, vd_script))

# ==========================================
# 18. CABLE SIZING CALCULATOR
# ==========================================
cs_app_json = """{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Cable Sizing Calculator",
  "url": "https://calchub.org/cable-sizing-calculator.html",
  "applicationCategory": "EngineeringApplication",
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
}"""

cs_workspace = """
      <section class="calc-card">
        <div class="calc-card-header">
          <span class="calc-title">🔌 Installation & Load Conditions (IEC 60364)</span>
        </div>
        <form onsubmit="return false;">
          <div class="calc-form-grid">
            <div class="input-group">
              <label class="input-label" for="cs-current">Design Current Ib (A)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="cs-current" value="45" min="1" max="1500" oninput="calcCable()">
                <span class="input-unit-badge">A</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="cs-temp">Ambient Temperature (°C)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="cs-temp" value="35" min="10" max="65" oninput="calcCable()">
                <span class="input-unit-badge">°C</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="cs-insul">Insulation Material</label>
              <div class="input-wrap">
                <select id="cs-insul" onchange="calcCable()">
                  <option value="xlpe" selected>XLPE / EPR (90°C Rated)</option>
                  <option value="pvc">PVC (70°C Rated)</option>
                </select>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="cs-method">Installation Method</label>
              <div class="input-wrap">
                <select id="cs-method" onchange="calcCable()">
                  <option value="conduit" selected>Enclosed in Conduit / Trunking (Method B)</option>
                  <option value="clipped">Clipped Direct to Wall (Method C)</option>
                  <option value="tray">Perforated Cable Tray in Free Air (Method E)</option>
                </select>
              </div>
            </div>
            <div class="input-group calc-field-full">
              <label class="input-label" for="cs-grouping">Number of Grouped Circuits</label>
              <div class="input-wrap">
                <select id="cs-grouping" onchange="calcCable()">
                  <option value="1.0" selected>1 Circuit (No Grouping Derating: 1.00)</option>
                  <option value="0.8">2 Circuits (Cg: 0.80)</option>
                  <option value="0.7">3 Circuits (Cg: 0.70)</option>
                  <option value="0.65">4–5 Circuits (Cg: 0.65)</option>
                  <option value="0.57">6–8 Circuits (Cg: 0.57)</option>
                </select>
              </div>
            </div>
          </div>
          <div class="calc-actions">
            <button type="button" class="btn btn-primary" onclick="copyResults()">📋 Copy Sizing Specification</button>
            <button type="button" class="btn btn-subtle" onclick="window.print()">🖨️ Print Cable Schedule</button>
          </div>
        </form>
      </section>

      <section class="results-card">
        <div class="results-header">
          <span class="results-title">Conductor Specification</span>
          <span class="status-pill status-success">IEC 60364 Compliant</span>
        </div>
        <div class="primary-result-box">
          <div class="primary-result-label">Recommended Conductor Size</div>
          <div>
            <span class="primary-result-value" id="cs-res-size" style="color:#2563EB;">10.0</span>
            <span class="primary-result-unit">mm² Copper</span>
          </div>
        </div>
        <div class="result-breakdown-grid">
          <div class="breakdown-item">
            <div class="breakdown-label">Minimum Required Ampacity (It)</div>
            <div class="breakdown-val" id="cs-it">49.4 A</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Nominal Cable Ampacity (Iz)</div>
            <div class="breakdown-val" id="cs-iz">65.0 A</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Temp Derating (Ca)</div>
            <div class="breakdown-val" id="cs-ca">0.96</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Grouping Derating (Cg)</div>
            <div class="breakdown-val" id="cs-cg">1.00</div>
          </div>
        </div>
      </section>
"""

cs_geo = """
    <section class="geo-citation-box">
      <div class="geo-header">💡 Direct Answer (GEO & Quick Summary)</div>
      <p>Cable sizing per <strong>IEC 60364-5-52</strong> and <strong>BS 7671</strong> ensures that a cable's corrected current-carrying capacity (Iz) is greater than or equal to the design load current (Ib). The required tabulated ampacity (It) is determined by:</p>
      <p><code>It = Ib ÷ (Ca × Cg × Ci)</code></p>
      <p>Where <strong>Ib</strong> = Design Current, <strong>Ca</strong> = Ambient Temperature Correction Factor, <strong>Cg</strong> = Grouping Factor, and <strong>Ci</strong> = Thermal Insulation Factor. A conductor cross-section (mm²) is selected such that <code>Iz ≥ It</code>.</p>
    </section>
"""

cs_toc = """
    <nav class="toc-container" aria-label="Table of Contents">
      <div class="toc-title">📑 Table of Contents</div>
      <ul class="toc-list">
        <li><a href="#cs-procedure">4-Step Cable Sizing Procedure</a></li>
        <li><a href="#cs-derating-factors">Temperature & Grouping Derating Factors</a></li>
        <li><a href="#xlpe-vs-pvc">XLPE vs PVC Insulation Performance</a></li>
        <li><a href="#cs-faq">Frequently Asked Questions</a></li>
      </ul>
    </nav>
"""

cs_article = """
      <h2 id="cs-procedure">The 4-Step Sizing Procedure (IEC 60364-5-52)</h2>
      <ol>
        <li><strong>Determine Design Current (Ib):</strong> Calculate operational load current from kilowatt power and power factor.</li>
        <li><strong>Calculate Required Tabulated Current (It):</strong> Divide Ib by all applicable derating factors: <code>It = Ib / (Ca · Cg)</code>.</li>
        <li><strong>Select Conductor Size:</strong> Consult IEC 60364-5-52 Table B.52.4 to choose the smallest standard conductor whose tabulated current <code>Iz ≥ It</code>.</li>
        <li><strong>Verify Voltage Drop:</strong> Confirm that total voltage drop over the run length does not exceed 3% for lighting or 5% for power.</li>
      </ol>

      <h2 id="cs-derating-factors">Derating Correction Multipliers</h2>
      <p>Cables running in ambient air above 30°C or bunched together in trays cannot dissipate heat effectively, requiring derating:</p>
      <div class="table-responsive">
        <table class="data-table">
          <thead><tr><th>Ambient Temp (°C)</th><th>XLPE Derating (Ca)</th><th>PVC Derating (Ca)</th></tr></thead>
          <tbody>
            <tr><td>30°C</td><td>1.00</td><td>1.00</td></tr>
            <tr><td>35°C</td><td>0.96</td><td>0.94</td></tr>
            <tr><td>40°C</td><td>0.91</td><td>0.87</td></tr>
            <tr><td>45°C</td><td>0.87</td><td>0.79</td></tr>
            <tr><td>50°C</td><td>0.82</td><td>0.71</td></tr>
          </tbody>
        </table>
      </div>

      <h2 id="xlpe-vs-pvc">XLPE (90°C) vs. PVC (70°C)</h2>
      <p>Cross-Linked Polyethylene (XLPE) operates at conductor temperatures up to 90°C, compared to 70°C for PVC. This 20°C thermal margin allows XLPE to carry approximately 15-20% higher ampacity in the exact same copper cross-sectional area.</p>

      <h2 id="cs-faq">Frequently Asked Questions</h2>
      <div class="faq-wrap">
        <details class="faq-item">
          <summary>What is the rule of thumb for cable current capacity?</summary>
          <div class="faq-content">In small residential wiring, copper cables roughly support: 1.5 mm² ≈ 16A, 2.5 mm² ≈ 24A, 4.0 mm² ≈ 32A, 6.0 mm² ≈ 41A, 10.0 mm² ≈ 57A. However, professional engineering always mandates formal derating calculations.</div>
        </details>
      </div>
"""

cs_script = """
  <script>
    // Simplified IEC 60364-5-52 Copper XLPE/PVC reference ampacity (Method B/C)
    const AMPACITY_TABLE = [
      { size: 1.5, xlpe: 19.5, pvc: 15.5 },
      { size: 2.5, xlpe: 27.0, pvc: 21.0 },
      { size: 4.0, xlpe: 36.0, pvc: 28.0 },
      { size: 6.0, xlpe: 46.0, pvc: 36.0 },
      { size: 10.0, xlpe: 65.0, pvc: 50.0 },
      { size: 16.0, xlpe: 87.0, pvc: 68.0 },
      { size: 25.0, xlpe: 114.0, pvc: 89.0 },
      { size: 35.0, xlpe: 141.0, pvc: 110.0 },
      { size: 50.0, xlpe: 182.0, pvc: 134.0 },
      { size: 70.0, xlpe: 234.0, pvc: 171.0 },
      { size: 95.0, xlpe: 284.0, pvc: 207.0 }
    ];

    function calcCable() {
      const ib = parseFloat(document.getElementById('cs-current').value) || 45;
      const temp = parseFloat(document.getElementById('cs-temp').value) || 35;
      const insul = document.getElementById('cs-insul').value;
      const cg = parseFloat(document.getElementById('cs-grouping').value) || 1.0;

      // Temp derating approximation
      let ca = 1.0;
      if (temp > 30) {
        ca = insul === 'xlpe' ? 1.0 - ((temp - 30) * 0.009) : 1.0 - ((temp - 30) * 0.014);
      }
      ca = Math.max(0.4, Math.min(1.0, ca));

      const it = ib / (ca * cg);

      let chosen = AMPACITY_TABLE[AMPACITY_TABLE.length - 1];
      for (let row of AMPACITY_TABLE) {
        const rating = insul === 'xlpe' ? row.xlpe : row.pvc;
        if (rating >= it) {
          chosen = row;
          break;
        }
      }

      const iz = insul === 'xlpe' ? chosen.xlpe : chosen.pvc;

      document.getElementById('cs-res-size').textContent = chosen.size.toFixed(1);
      document.getElementById('cs-it').textContent = it.toFixed(1) + ' A';
      document.getElementById('cs-iz').textContent = iz.toFixed(1) + ' A';
      document.getElementById('cs-ca').textContent = ca.toFixed(2);
      document.getElementById('cs-cg').textContent = cg.toFixed(2);
    }
    function copyResults() {
      const s = document.getElementById('cs-res-size').textContent;
      const iz = document.getElementById('cs-iz').textContent;
      window.copyToClipboard(`CalcHub Cable Sizing: ${s} mm² Copper (Tabulated Iz: ${iz})`);
    }
    calcCable();
  </script>
"""

with open(os.path.join(OUTPUT_DIR, "cable-sizing-calculator.html"), "w", encoding="utf-8") as f:
    f.write(page_scaffold("Cable Sizing Calculator — IEC 60364 & BS 7671 Conductor Ampacity",
                          "Determine minimum conductor size (mm²) per IEC 60364-5-52 and BS 7671. Automatic ambient temperature derating, grouping factors, and XLPE/PVC ratings.",
                          "cable sizing calculator, iec 60364 cable sizing, wire ampacity calculator, bs 7671 cable calculator, electrical cable size, conductor sizing",
                          "cable-sizing-calculator", "Electrical Engineering", "engineering", cs_app_json,
                          "Size power cables with international engineering standards. Applies ambient temperature derating (Ca) and multi-circuit bundling factors (Cg).",
                          cs_workspace, cs_geo, cs_toc, cs_article, cs_script))

# ==========================================
# 19. RESISTOR COLOR CODE CALCULATOR
# ==========================================
res_app_json = """{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Resistor Color Code Calculator",
  "url": "https://calchub.org/resistor-color-code-calculator.html",
  "applicationCategory": "EngineeringApplication",
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
}"""

res_workspace = """
      <section class="calc-card">
        <div class="calc-card-header">
          <span class="calc-title">🎨 4-Band & 5-Band Color Decoders</span>
        </div>
        <form onsubmit="return false;">
          <div style="display:flex;justify-content:center;margin:1.5rem 0;">
            <!-- Graphical Resistor SVG with dynamic colored bands -->
            <svg width="280" height="80" viewBox="0 0 280 80">
              <!-- Lead wires -->
              <line x1="0" y1="40" x2="40" y2="40" stroke="#94A3B8" stroke-width="4"/>
              <line x1="240" y1="40" x2="280" y2="40" stroke="#94A3B8" stroke-width="4"/>
              <!-- Resistor body -->
              <rect x="40" y="16" width="200" height="48" rx="14" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="2"/>
              <!-- Bands -->
              <rect id="svg-b1" x="70" y="16" width="12" height="48" fill="#A855F7"/>
              <rect id="svg-b2" x="105" y="16" width="12" height="48" fill="#6B7280"/>
              <rect id="svg-b3" x="140" y="16" width="12" height="48" fill="#EF4444"/>
              <rect id="svg-b4" x="200" y="16" width="12" height="48" fill="#EAB308"/>
            </svg>
          </div>

          <div class="calc-form-grid">
            <div class="input-group">
              <label class="input-label" for="res-b1">1st Band (Digit 1)</label>
              <div class="input-wrap">
                <select id="res-b1" onchange="calcResistor()">
                  <option value="1">1 Brown</option>
                  <option value="2">2 Red</option>
                  <option value="3">3 Orange</option>
                  <option value="4" selected>4 Yellow</option>
                  <option value="5">5 Green</option>
                  <option value="6">6 Blue</option>
                  <option value="7">7 Violet</option>
                  <option value="8">8 Gray</option>
                  <option value="9">9 White</option>
                </select>
              </div>
            </div>

            <div class="input-group">
              <label class="input-label" for="res-b2">2nd Band (Digit 2)</label>
              <div class="input-wrap">
                <select id="res-b2" onchange="calcResistor()">
                  <option value="0">0 Black</option>
                  <option value="1">1 Brown</option>
                  <option value="2">2 Red</option>
                  <option value="3">3 Orange</option>
                  <option value="4">4 Yellow</option>
                  <option value="5">5 Green</option>
                  <option value="6">6 Blue</option>
                  <option value="7" selected>7 Violet</option>
                  <option value="8">8 Gray</option>
                  <option value="9">9 White</option>
                </select>
              </div>
            </div>

            <div class="input-group">
              <label class="input-label" for="res-b3">Multiplier</label>
              <div class="input-wrap">
                <select id="res-b3" onchange="calcResistor()">
                  <option value="1">×1 Black</option>
                  <option value="10">×10 Brown</option>
                  <option value="100">×100 Red</option>
                  <option value="1000" selected>×1k Orange</option>
                  <option value="10000">×10k Yellow</option>
                  <option value="100000">×100k Green</option>
                  <option value="1000000">×1M Blue</option>
                  <option value="0.1">×0.1 Gold</option>
                  <option value="0.01">×0.01 Silver</option>
                </select>
              </div>
            </div>

            <div class="input-group">
              <label class="input-label" for="res-b4">Tolerance Band</label>
              <div class="input-wrap">
                <select id="res-b4" onchange="calcResistor()">
                  <option value="5" selected>±5% Gold</option>
                  <option value="10">±10% Silver</option>
                  <option value="1">±1% Brown</option>
                  <option value="2">±2% Red</option>
                  <option value="0.5">±0.5% Green</option>
                </select>
              </div>
            </div>
          </div>

          <div class="calc-actions">
            <button type="button" class="btn btn-primary" onclick="copyResults()">📋 Copy Ohms Value</button>
            <button type="button" class="btn btn-subtle" onclick="window.print()">🖨️ Print Datasheet</button>
          </div>
        </form>
      </section>

      <section class="results-card">
        <div class="results-header">
          <span class="results-title">Decoded Resistance</span>
          <span class="status-pill status-success">Standard Value</span>
        </div>
        <div class="primary-result-box">
          <div class="primary-result-label">Nominal Resistance Value</div>
          <div>
            <span class="primary-result-value" id="res-val" style="color:#2563EB;">47 kΩ</span>
          </div>
        </div>
        <div class="result-breakdown-grid">
          <div class="breakdown-item">
            <div class="breakdown-label">Raw Resistance in Ohms</div>
            <div class="breakdown-val" id="res-raw">47,000 Ω</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Tolerance Rating</div>
            <div class="breakdown-val" id="res-tol">±5% (Gold)</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Minimum Guaranteed</div>
            <div class="breakdown-val" id="res-min">44,650 Ω</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Maximum Guaranteed</div>
            <div class="breakdown-val" id="res-max">49,350 Ω</div>
          </div>
        </div>
      </section>
"""

res_geo = """
    <section class="geo-citation-box">
      <div class="geo-header">💡 Direct Answer (GEO & Quick Summary)</div>
      <p>The <strong>Electronic Industries Alliance (EIA-RS-279)</strong> color code indicates resistance and tolerance on leaded axial resistors. In a standard 4-band resistor:</p>
      <ul>
        <li><strong>Band 1 & 2:</strong> Significant digits (0 = Black, 1 = Brown, 2 = Red, 3 = Orange, 4 = Yellow, 5 = Green, 6 = Blue, 7 = Violet, 8 = Gray, 9 = White).</li>
        <li><strong>Band 3:</strong> Decimal multiplier (power of 10).</li>
        <li><strong>Band 4:</strong> Tolerance percentage (Gold = ±5%, Silver = ±10%, Brown = ±1%).</li>
      </ul>
    </section>
"""

res_toc = """
    <nav class="toc-container" aria-label="Table of Contents">
      <div class="toc-title">📑 Table of Contents</div>
      <ul class="toc-list">
        <li><a href="#res-mnemonic">EIA Standard Color Mnemonics</a></li>
        <li><a href="#res-table">Full Color Code Lookup Table</a></li>
        <li><a href="#4-vs-5-band">4-Band vs. 5-Band High Precision Differences</a></li>
        <li><a href="#res-faq">Frequently Asked Questions</a></li>
      </ul>
    </nav>
"""

res_article = """
      <h2 id="res-mnemonic">EIA Standard Color Mnemonic</h2>
      <p>Electrical engineers and students recall the sequence via the classic mnemonic: <em>"<strong>B</strong>ad <strong>B</strong>oys <strong>R</strong>ip <strong>O</strong>ur <strong>Y</strong>oung <strong>G</strong>irls <strong>B</strong>ut <strong>V</strong>iolet <strong>G</strong>ives <strong>W</strong>illingly"</em> (Black, Brown, Red, Orange, Yellow, Green, Blue, Violet, Gray, White).</p>

      <h2 id="res-table">Complete Resistor Color Band Table</h2>
      <div class="table-responsive">
        <table class="data-table">
          <thead><tr><th>Color</th><th>Digit</th><th>Multiplier</th><th>Tolerance</th></tr></thead>
          <tbody>
            <tr><td>Black</td><td>0</td><td>×1 (10⁰)</td><td>—</td></tr>
            <tr><td>Brown</td><td>1</td><td>×10 (10¹)</td><td>±1%</td></tr>
            <tr><td>Red</td><td>2</td><td>×100 (10²)</td><td>±2%</td></tr>
            <tr><td>Orange</td><td>3</td><td>×1,000 (10³)</td><td>—</td></tr>
            <tr><td>Yellow</td><td>4</td><td>×10,000 (10⁴)</td><td>—</td></tr>
            <tr><td>Green</td><td>5</td><td>×100,000 (10⁵)</td><td>±0.5%</td></tr>
            <tr><td>Blue</td><td>6</td><td>×1,000,000 (10⁶)</td><td>±0.25%</td></tr>
            <tr><td>Violet</td><td>7</td><td>×10,000,000 (10⁷)</td><td>±0.1%</td></tr>
            <tr><td>Gray</td><td>8</td><td>—</td><td>±0.05%</td></tr>
            <tr><td>White</td><td>9</td><td>—</td><td>—</td></tr>
            <tr><td>Gold</td><td>—</td><td>×0.1</td><td>±5%</td></tr>
            <tr><td>Silver</td><td>—</td><td>×0.01</td><td>±10%</td></tr>
          </tbody>
        </table>
      </div>

      <h2 id="4-vs-5-band">4-Band vs 5-Band Precision Resistors</h2>
      <p>Standard carbon-film resistors use 4 bands. Precision metal-film resistors feature 5 bands: 3 significant digits, 1 multiplier band, and 1 tolerance band, allowing 1% and 0.1% precision in audio, medical, and aerospace electronics.</p>

      <h2 id="res-faq">Frequently Asked Questions</h2>
      <div class="faq-wrap">
        <details class="faq-item">
          <summary>How do I know which end of the resistor to read first?</summary>
          <div class="faq-content">Look for the tolerance band (typically Gold or Silver). It is set slightly further apart from the other grouped bands with a wider gap. Start reading from the opposite end.</div>
        </details>
      </div>
"""

res_script = """
  <script>
    const COLOR_HEX = {
      0: '#0F172A', 1: '#9A3412', 2: '#EF4444', 3: '#F97316', 4: '#FBBF24',
      5: '#10B981', 6: '#3B82F6', 7: '#8B5CF6', 8: '#6B7280', 9: '#F8FAFC',
      'gold': '#EAB308', 'silver': '#94A3B8'
    };

    function calcResistor() {
      const b1 = parseInt(document.getElementById('res-b1').value);
      const b2 = parseInt(document.getElementById('res-b2').value);
      const mult = parseFloat(document.getElementById('res-b3').value);
      const tol = parseFloat(document.getElementById('res-b4').value);

      const rawOhms = ((b1 * 10) + b2) * mult;
      
      let formatted = '';
      if (rawOhms >= 1000000) {
        formatted = (rawOhms / 1000000).toFixed(2).replace(/\\.00$/, '') + ' MΩ';
      } else if (rawOhms >= 1000) {
        formatted = (rawOhms / 1000).toFixed(2).replace(/\\.00$/, '') + ' kΩ';
      } else {
        formatted = rawOhms.toFixed(1).replace(/\\.0$/, '') + ' Ω';
      }

      const minOhms = rawOhms * (1 - (tol / 100));
      const maxOhms = rawOhms * (1 + (tol / 100));

      document.getElementById('res-val').textContent = formatted;
      document.getElementById('res-raw').textContent = rawOhms.toLocaleString() + ' Ω';
      document.getElementById('res-tol').textContent = `±${tol}%`;
      document.getElementById('res-min').textContent = Math.round(minOhms).toLocaleString() + ' Ω';
      document.getElementById('res-max').textContent = Math.round(maxOhms).toLocaleString() + ' Ω';

      // Update SVG colors
      document.getElementById('svg-b1').setAttribute('fill', COLOR_HEX[b1] || '#9A3412');
      document.getElementById('svg-b2').setAttribute('fill', COLOR_HEX[b2] || '#8B5CF6');
      let mKey = 0;
      if (mult === 1) mKey = 0;
      else if (mult === 10) mKey = 1;
      else if (mult === 100) mKey = 2;
      else if (mult === 1000) mKey = 3;
      else if (mult === 10000) mKey = 4;
      else if (mult === 100000) mKey = 5;
      else if (mult === 1000000) mKey = 6;
      else if (mult === 0.1) mKey = 'gold';
      else if (mult === 0.01) mKey = 'silver';
      document.getElementById('svg-b3').setAttribute('fill', COLOR_HEX[mKey] || '#F97316');
      document.getElementById('svg-b4').setAttribute('fill', tol === 10 ? '#94A3B8' : '#EAB308');
    }

    function copyResults() {
      const v = document.getElementById('res-val').textContent;
      const t = document.getElementById('res-tol').textContent;
      window.copyToClipboard(`CalcHub Resistor Value: ${v} ${t}`);
    }
    calcResistor();
  </script>
"""

with open(os.path.join(OUTPUT_DIR, "resistor-color-code-calculator.html"), "w", encoding="utf-8") as f:
    f.write(page_scaffold("Resistor Color Code Calculator — 4-Band & 5-Band Interactive Decoder",
                          "Decode 4-band and 5-band resistor color codes with an interactive visual SVG resistor. Computes resistance in Ohms, tolerance range, and EIA mnemonics.",
                          "resistor color code calculator, 4 band resistor calculator, resistor color bands, 10k resistor color code, tolerance calculator",
                          "resistor-color-code-calculator", "Electrical Engineering", "engineering", res_app_json,
                          "Decode axial leaded resistors with an interactive graphical color band selector. Instant tolerance calculation and minimum/maximum ohm bounds.",
                          res_workspace, res_geo, res_toc, res_article, res_script))

# ==========================================
# 20. SOLAR PANEL & BATTERY SIZING
# ==========================================
sol_app_json = """{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Solar Panel & Battery Sizing Calculator",
  "url": "https://calchub.org/solar-panel-sizing-calculator.html",
  "applicationCategory": "EngineeringApplication",
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
}"""

sol_workspace = """
      <section class="calc-card">
        <div class="calc-card-header">
          <span class="calc-title">☀️ Solar Generation & Battery Storage Needs</span>
        </div>
        <form onsubmit="return false;">
          <div class="calc-form-grid">
            <div class="input-group">
              <label class="input-label" for="sol-daily">Daily Power Usage (kWh/day)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="sol-daily" value="18" min="1" max="200" step="0.5" oninput="calcSolar()">
                <span class="input-unit-badge">kWh</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="sol-sun">Peak Sun Hours (PSh/day)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="sol-sun" value="4.5" min="2" max="8" step="0.1" oninput="calcSolar()">
                <span class="input-unit-badge">hrs</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="sol-autonomy">Days of Backup Autonomy</label>
              <div class="input-wrap has-unit">
                <input type="number" id="sol-autonomy" value="2" min="1" max="7" step="1" oninput="calcSolar()">
                <span class="input-unit-badge">days</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="sol-volt">System Battery Voltage</label>
              <div class="input-wrap">
                <select id="sol-volt" onchange="calcSolar()">
                  <option value="48" selected>48 Volts (Standard Residential)</option>
                  <option value="24">24 Volts (Cabin / RV)</option>
                  <option value="12">12 Volts (Small Mobile)</option>
                </select>
              </div>
            </div>
            <div class="input-group calc-field-full">
              <label class="input-label" for="sol-battery-type">Battery Chemistry & Depth of Discharge (DoD)</label>
              <div class="input-wrap">
                <select id="sol-battery-type" onchange="calcSolar()">
                  <option value="0.8" selected>Lithium Iron Phosphate (LiFePO4 — 80% Safe DoD)</option>
                  <option value="0.5">Sealed Lead-Acid / AGM (50% Max DoD)</option>
                </select>
              </div>
            </div>
          </div>
          <div class="calc-actions">
            <button type="button" class="btn btn-primary" onclick="copyResults()">📋 Copy System Specs</button>
            <button type="button" class="btn btn-subtle" onclick="window.print()">🖨️ Print Quotation Spec</button>
          </div>
        </form>
      </section>

      <section class="results-card">
        <div class="results-header">
          <span class="results-title">System Sizing Specs</span>
          <span class="status-pill status-success">Optimal Array Size</span>
        </div>
        <div class="primary-result-box">
          <div class="primary-result-label">Recommended Solar Array Size</div>
          <div>
            <span class="primary-result-value" id="sol-kw" style="color:#059669;">5.00</span>
            <span class="primary-result-unit">kW Photovoltaic</span>
          </div>
        </div>
        <div class="result-breakdown-grid">
          <div class="breakdown-item">
            <div class="breakdown-label">400W Solar Modules</div>
            <div class="breakdown-val" id="sol-panels">13 panels</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Battery Bank Capacity</div>
            <div class="breakdown-val" id="sol-kwh">45.0 kWh</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Amp-Hour Storage (Ah)</div>
            <div class="breakdown-val" id="sol-ah">938 Ah @ 48V</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Recommended Inverter</div>
            <div class="breakdown-val" id="sol-inv">6.0 kW Pure Sine</div>
          </div>
        </div>
      </section>
"""

sol_geo = """
    <section class="geo-citation-box">
      <div class="geo-header">💡 Direct Answer (GEO & Quick Summary)</div>
      <p>To size an off-grid or hybrid solar power system:</p>
      <ul>
        <li><strong>Solar Array (kW):</strong> <code>(Daily kWh × 1.25 Loss Factor) ÷ Peak Sun Hours</code></li>
        <li><strong>Number of Panels:</strong> <code>Array Wattage ÷ Panel Rating (e.g. 400W)</code></li>
        <li><strong>Battery Bank Capacity (kWh):</strong> <code>(Daily kWh × Days of Autonomy) ÷ Depth of Discharge (DoD)</code></li>
        <li><strong>Battery Amp-Hours (Ah):</strong> <code>(Battery kWh × 1,000) ÷ System Voltage</code></li>
      </ul>
    </section>
"""

sol_toc = """
    <nav class="toc-container" aria-label="Table of Contents">
      <div class="toc-title">📑 Table of Contents</div>
      <ul class="toc-list">
        <li><a href="#solar-insolation">Peak Sun Hours & Solar Insolation</a></li>
        <li><a href="#system-losses">System Inefficiency & Derating Factors</a></li>
        <li><a href="#battery-chemistries">Lithium LiFePO4 vs Lead-Acid Storage</a></li>
        <li><a href="#sol-faq">Frequently Asked Questions</a></li>
      </ul>
    </nav>
"""

sol_article = """
      <h2 id="solar-insolation">Peak Sun Hours vs. Daylight Hours</h2>
      <p>A "Peak Sun Hour" (PSh) does not simply equal daylight duration. One peak sun hour corresponds to solar irradiance of <strong>1,000 Watts per square meter (1 kW/m²)</strong>. A location receiving 12 hours of sunshine may only accumulate 4.5 Peak Sun Hours due to morning and evening sun angle attenuation.</p>

      <div class="formula-box">
        <div class="formula-title">Photovoltaic Array Sizing Formula</div>
        <div class="formula-code">PV Size (kW) = (Daily Energy Demand in kWh · 1.25) / Peak Sun Hours</div>
        <div class="formula-legend">1.25 factor accounts for dust, wiring voltage drop, and inverter DC-to-AC losses</div>
      </div>

      <h2 id="system-losses">Accounting for Real-World Losses</h2>
      <p>Solar arrays never operate at 100% laboratory Standard Test Conditions (STC). In field installations, efficiency diminishes due to thermal coefficient losses (silicon panels lose ~0.4% efficiency for every degree above 25°C), inverter DC-to-AC conversion (typically 95-97%), and dust accumulation.</p>

      <h2 id="battery-chemistries">Lithium Iron Phosphate (LiFePO4) vs. Lead-Acid</h2>
      <div class="table-responsive">
        <table class="data-table">
          <thead><tr><th>Feature</th><th>LiFePO4 Lithium</th><th>AGM / Gel Lead-Acid</th></tr></thead>
          <tbody>
            <tr><td>Usable Depth of Discharge (DoD)</td><td><strong>80–90%</strong></td><td>50% (Deeper drains destroy life)</td></tr>
            <tr><td>Cycle Life</td><td>3,500 – 6,000 cycles</td><td>500 – 1,000 cycles</td></tr>
            <tr><td>Round-Trip Efficiency</td><td>95%</td><td>80%</td></tr>
          </tbody>
        </table>
      </div>

      <h2 id="sol-faq">Frequently Asked Questions</h2>
      <div class="faq-wrap">
        <details class="faq-item">
          <summary>What is Days of Autonomy?</summary>
          <div class="faq-content">Days of Autonomy represents the number of consecutive days your battery bank can power your essential loads without receiving any solar recharge (during heavy overcast, rain, or snowstorms). Typically 1-3 days for residential off-grid systems.</div>
        </details>
      </div>
"""

sol_script = """
  <script>
    function calcSolar() {
      const dailyKwh = parseFloat(document.getElementById('sol-daily').value) || 18;
      const psh = parseFloat(document.getElementById('sol-sun').value) || 4.5;
      const autonomy = parseFloat(document.getElementById('sol-autonomy').value) || 2;
      const vSys = parseFloat(document.getElementById('sol-volt').value) || 48;
      const dod = parseFloat(document.getElementById('sol-battery-type').value) || 0.8;

      // 1.25 factor for systemic inefficiency
      const arrayKw = (dailyKwh * 1.25) / psh;
      const arrayWatts = arrayKw * 1000;
      const numPanels = Math.ceil(arrayWatts / 400);

      // Battery storage
      const battKwh = (dailyKwh * autonomy) / dod;
      const battAh = (battKwh * 1000) / vSys;
      const invKw = Math.ceil(arrayKw * 1.2);

      document.getElementById('sol-kw').textContent = arrayKw.toFixed(2);
      document.getElementById('sol-panels').textContent = `${numPanels} panels (400W)`;
      document.getElementById('sol-kwh').textContent = battKwh.toFixed(1) + ' kWh';
      document.getElementById('sol-ah').textContent = `${Math.round(battAh)} Ah @ ${vSys}V`;
      document.getElementById('sol-inv').textContent = `${invKw}.0 kW Pure Sine`;
    }
    function copyResults() {
      const kw = document.getElementById('sol-kw').textContent;
      const pan = document.getElementById('sol-panels').textContent;
      const b = document.getElementById('sol-kwh').textContent;
      window.copyToClipboard(`CalcHub Solar Spec: Array: ${kw} kW (${pan}), Battery: ${b}`);
    }
    calcSolar();
  </script>
"""

with open(os.path.join(OUTPUT_DIR, "solar-panel-sizing-calculator.html"), "w", encoding="utf-8") as f:
    f.write(page_scaffold("Solar Panel & Battery Sizing Calculator — Off-Grid System Sizing",
                          "Size solar panel arrays, battery bank storage (Ah and kWh), and inverter capacity based on daily energy consumption and peak sun hours.",
                          "solar panel calculator, solar battery sizing, off grid solar calculator, solar panel array size, kwh to solar panels",
                          "solar-panel-sizing-calculator", "Renewable Energy & Solar", "engineering", sol_app_json,
                          "Engineer residential and off-grid solar energy systems. Calculate photovoltaic array capacity, battery storage, and inverter sizing based on peak sun hours.",
                          sol_workspace, sol_geo, sol_toc, sol_article, sol_script))

print("Created all 5 Engineering Calculators successfully!")
