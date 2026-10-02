# -*- coding: utf-8 -*-
"""
Script to generate Batch 8 Part 2 tools:
3. nac-voltage-drop-calculator.html
4. single-phase-cable-sizing-calculator.html
"""
import os

TOOL_3_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NAC Voltage Drop Calculator | NFPA 72 Fire Alarm Notification Circuit Sizing</title>
  <meta name="description" content="Calculate fire alarm Notification Appliance Circuit (NAC) voltage drop compliant with NFPA 72 and UL 864. Computes end-of-line EOL voltage, strobe/horn current, wire gauge, and distance.">
  <link rel="canonical" href="https://calchub.cloud/nac-voltage-drop-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "NAC Voltage Drop Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Life-safety fire alarm Notification Appliance Circuit (NAC) voltage drop and end-of-line voltage calculation tool per NFPA 72 and UL 864 standards.",
        "offers": {
          "@type": "Offer",
          "price": "0.00",
          "priceCurrency": "USD"
        }
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "What is the minimum operating voltage for a 24VDC NAC device under NFPA 72?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Under NFPA 72 and UL 864, notification appliances (strobes, horns, chimes) listed for regulated 24VDC must operate reliably between 16.0 VDC and 33.0 VDC. Therefore, the calculated voltage at the last device on the NAC circuit (End-of-Line, EOL) must never drop below 16.0 VDC under worst-case standby battery depletion (20.4 VDC panel battery cutoff)."
            }
          },
          {
            "@type": "Question",
            "name": "Why must 20.4 VDC be used as the starting voltage instead of 24.0 VDC?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "NFPA 72 requires secondary emergency battery standby (typically 24 hours of supervision followed by 5 minutes or 15 minutes of full alarm). At the end of discharge, lead-acid batteries drop from 27.4V float voltage down to 20.4 VDC (1.70 volts per cell). Engineers must verify that appliances fire reliably at this depleted threshold."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between Point-to-Point and Lump-Sum calculation methods?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The Point-to-Point method calculates the cumulative voltage drop along each individual wire segment between appliances, providing exact terminal voltages. The Lump-Sum method assumes all appliance currents are lumped together at the furthest end of the circuit (or at the electrical midpoint), producing a conservative worst-case safety margin."
            }
          },
          {
            "@type": "Question",
            "name": "Why is solid FPLR/FPLP copper cable standard for fire alarm NAC circuits?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Solid copper conductors (#12, #14, #16, or #18 AWG) eliminate loose strand terminal faults under screw terminals. Fire Power Limited Riser (FPLR) and Plenum (FPLP) cables have heat-resistant insulation rated up to 105°C, ensuring integrity during evacuation alarms."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="engineering">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">
        <span class="logo-icon">&pi;</span>
        <span class="logo-text">Calc<strong>Hub</strong></span>
      </a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="engineering.html" class="active">Engineering</a>
        <a href="solar-energy.html">Solar</a>
        <a href="fire-safety.html">Fire Safety</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo;
      <a href="fire-safety.html">Fire &amp; Life Safety</a> &rsaquo;
      <span>NAC Voltage Drop Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">NFPA 72 &amp; UL 864 Standards</div>
          <h1 class="calc-title">NAC Voltage Drop Calculator</h1>
          <p class="calc-tagline">Calculate fire alarm Notification Appliance Circuit (NAC) voltage drop, End-of-Line (EOL) terminal voltage, and max loop distance.</p>
        </header>

        <!-- Tool Card -->
        <div class="tool-card">
          <form id="nacForm" onsubmit="return false;">
            <div class="calc-grid">
              <div class="form-group">
                <label for="nacSourceVoltage" class="form-label">FACP / Booster Source Voltage</label>
                <select id="nacSourceVoltage" class="form-control" onchange="calculateNac()">
                  <option value="20.4" selected>20.4 VDC (NFPA 72 Worst-Case Battery Cutoff)</option>
                  <option value="24.0">24.0 VDC (Nominal Regulated Power Supply)</option>
                  <option value="27.4">27.4 VDC (AC Mains Float Charge Condition)</option>
                </select>
                <small class="form-hint">Supply voltage at panel terminals</small>
              </div>

              <div class="form-group">
                <label for="nacWireGauge" class="form-label">Fire Alarm Cable Gauge (Solid Copper)</label>
                <select id="nacWireGauge" class="form-control" onchange="calculateNac()">
                  <option value="14" selected>14 AWG Solid Copper ($R \approx 3.07\ \Omega/\text{kft}$)</option>
                  <option value="12">12 AWG Solid Copper ($R \approx 1.93\ \Omega/\text{kft}$)</option>
                  <option value="16">16 AWG Solid Copper ($R \approx 4.99\ \Omega/\text{kft}$)</option>
                  <option value="18">18 AWG Solid Copper ($R \approx 7.77\ \Omega/\text{kft}$)</option>
                </select>
                <small class="form-hint">FPLR / FPLP solid conductor resistance</small>
              </div>

              <div class="form-group">
                <label for="nacTotalCurrent" class="form-label">Total Connected Alarm Current</label>
                <div class="input-with-unit">
                  <input type="number" id="nacTotalCurrent" class="form-control" value="1.85" min="0.05" max="6.0" step="0.05" oninput="calculateNac()">
                  <span class="unit-badge">Amps</span>
                </div>
                <small class="form-hint">Sum of all strobes, horns &amp; speakers (e.g. 1.85A)</small>
              </div>

              <div class="form-group">
                <label for="nacCircuitLength" class="form-label">One-Way Run Length to Furthest Device</label>
                <div class="input-with-unit">
                  <input type="number" id="nacCircuitLength" class="form-control" value="320" min="10" max="2500" step="10" oninput="calculateNac()">
                  <span class="unit-badge">feet</span>
                </div>
                <small class="form-hint">Distance from panel to last appliance</small>
              </div>

              <div class="form-group">
                <label for="nacCalcMethod" class="form-label">Load Distribution Topology</label>
                <select id="nacCalcMethod" class="form-control" onchange="calculateNac()">
                  <option value="lump_end" selected>End-of-Line Lump Sum (Conservative Worst-Case)</option>
                  <option value="lump_center">Center of Load / Uniform Distribution (~50% Drop)</option>
                </select>
                <small class="form-hint">Spatial appliance layout along circuit</small>
              </div>

              <div class="form-group">
                <label for="nacWireTemp" class="form-label">Conductor Temperature Rating</label>
                <select id="nacWireTemp" class="form-control" onchange="calculateNac()">
                  <option value="75" selected>75°C Elevated Fire Alarm Operating Temp</option>
                  <option value="60">60°C Standard Ambient</option>
                </select>
                <small class="form-hint">Resistance increases with temperature</small>
              </div>
            </div>

            <button type="button" id="calcNacBtn" class="btn btn-primary btn-block" onclick="calculateNac()">Calculate NAC Voltage Drop</button>
          </form>

          <div id="nacResultBox" class="results-container" style="margin-top:20px;">
            <h3>NAC Voltage Drop Analysis Summary</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label">End-of-Line (EOL) Voltage</span>
                <span id="nacEolVoltageOut" class="result-value">-- VDC</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Total Circuit Voltage Drop ($\Delta V$)</span>
                <span id="nacDropOut" class="result-value">-- VDC</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Loop Resistance ($2 \times R_{wire}$)</span>
                <span id="nacLoopResOut" class="result-value">-- &Omega;</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Percentage Voltage Drop</span>
                <span id="nacPctOut" class="result-value">-- %</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Maximum Compliant Distance ($16\text{V}$ EOL)</span>
                <span id="nacMaxDistOut" class="result-value">-- feet</span>
              </div>
              <div class="result-tile">
                <span class="result-label">NFPA 72 &amp; UL 864 Compliance</span>
                <span id="nacStatusOut" class="result-value">--</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Engineering Analysis: Fire Alarm Notification Appliance Circuits (NAC)</h2>
          
          <p>Fire alarm Notification Appliance Circuits (NAC) supply regulated direct current ($24\text{ VDC}$) to life-safety emergency signaling devices, including high-candela synchronized strobes, audible notification horns, electronic sounders, and voice evacuation loudspeakers. If electrical line voltage drop along a NAC is excessive, the voltage reaching distant appliances will fall below their certified operational threshold. When this occurs, xenon or LED strobes fail to flash, synchronization modules lose coordination timing, and audible horns fail to produce the legally mandated decibel sound pressure levels ($75\text{ dBA}$ at 10 feet per NFPA 72).</p>

          <p>Designing fire alarm notification circuits requires strict adherence to <strong>NFPA 72 (National Fire Alarm and Signaling Code Chapter 18 &amp; 24)</strong>, <strong>UL 864 (Standard for Control Units and Accessories for Fire Alarm Systems)</strong>, and <strong>UL 1971 (Signaling Devices for the Hearing Impaired)</strong>.</p>

          <div class="formula-box">
            <h3>The 16.0 VDC UL Operating Threshold &amp; 20.4 VDC Battery Rule</h3>
            <p>Every UL-listed 24VDC notification appliance is certified to operate reliably over an input voltage window of <strong>$16.0\text{ VDC}$ to $33.0\text{ VDC}$</strong>. Under NFPA 72 Section 10.6.7, secondary emergency power must supply the system under full alarm load for at least 5 minutes (or 15 minutes for emergency voice communications) following 24 hours of primary power failure.</p>
            <p>At the end of secondary battery discharge, a nominal $24\text{V}$ sealed lead-acid (SLA) battery bank degrades to $1.70\text{ Volts per cell}$, yielding a terminal cutoff voltage of exactly:</p>
            <p>$$V_{source,min} = 12 \text{ cells} \times 1.70\text{ V/cell} = 20.4\text{ VDC}$$</p>
            <p>Therefore, the maximum allowable total loop voltage drop across the entire circuit length is strictly limited to:</p>
            <p>$$\Delta V_{max,allowable} = V_{source,min} - V_{appliance,min} = 20.4\text{ VDC} - 16.0\text{ VDC} = 4.4\text{ VDC}$$</p>
          </div>

          <h3>Calculation Methodologies: Lump-Sum vs. Point-to-Point</h3>
          <p>Electrical engineers and fire alarm designers utilize two standardized calculation methodologies to determine NAC compliance:</p>

          <h4>1. The End-of-Line (EOL) Lump-Sum Method (Worst-Case)</h4>
          <p>The Lump-Sum method assumes that the entire connected appliance current load ($I_{total}$) is concentrated at the very end of the circuit ($L$ feet away). Because current travels out along the positive conductor and returns along the negative conductor, the total round-trip loop resistance is $R_{loop} = 2 \times L \times R_{wire}$:</p>
          <p>$$\Delta V = 2 \times L \times I_{total} \times \left(\frac{R_{1000\text{ft}}}{1000}\right)$$</p>
          <p>$$V_{EOL} = V_{source} - \Delta V$$</p>
          <p>This is the most conservative design technique, providing an inherent safety factor that ensures code compliance even if appliances are added or relocated during building tenant improvements.</p>

          <h4>2. The Center-of-Load / Point-to-Point Method</h4>
          <p>When notification appliances are spaced uniformly along a hallway or multi-story stairwell, current drops off after each successive appliance tap. In the Center-of-Load approximation, the total current is assumed to act at the geographic midpoint ($L/2$):</p>
          <p>$$\Delta V_{center} \approx \frac{1}{2} \cdot \Delta V_{lump-sum}$$</p>
          <p>In exact Point-to-Point calculations, each segment resistance between device $k$ and device $k+1$ is evaluated individually with its specific downstream current sum:</p>
          <p>$$\Delta V_{P2P} = \sum_{k=1}^{N} \left[ 2 \cdot L_k \cdot R_{wire} \cdot \sum_{i=k}^{N} I_i \right]$$</p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Conductor Size (AWG)</th>
                <th>Conductor Type</th>
                <th>DC Resistance at 20°C (Ω/kft)</th>
                <th>DC Resistance at 75°C (Ω/kft)</th>
                <th>Max Loop Distance (1A Load, 4.4V Drop)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>#18 AWG</strong></td>
                <td>Solid Annealed Copper</td>
                <td>$6.38\ \Omega/\text{kft}$</td>
                <td>$7.77\ \Omega/\text{kft}$</td>
                <td>$283\text{ feet}$</td>
              </tr>
              <tr>
                <td><strong>#16 AWG</strong></td>
                <td>Solid Annealed Copper</td>
                <td>$4.02\ \Omega/\text{kft}$</td>
                <td>$4.99\ \Omega/\text{kft}$</td>
                <td>$441\text{ feet}$</td>
              </tr>
              <tr>
                <td><strong>#14 AWG</strong></td>
                <td>Solid Annealed Copper</td>
                <td>$2.52\ \Omega/\text{kft}$</td>
                <td>$3.07\ \Omega/\text{kft}$</td>
                <td>$716\text{ feet}$</td>
              </tr>
              <tr>
                <td><strong>#12 AWG</strong></td>
                <td>Solid Annealed Copper</td>
                <td>$1.59\ \Omega/\text{kft}$</td>
                <td>$1.93\ \Omega/\text{kft}$</td>
                <td>$1{,}140\text{ feet}$</td>
              </tr>
            </tbody>
          </table>

          <div class="worked-example-card">
            <h3>Practical Worked Engineering Example: Office Building Strobe NAC Run</h3>
            <p><strong>Design Scenario:</strong> Dimensioning a Class B notification appliance circuit powering 10 wall-mounted horn-strobes in an office corridor. Total connected alarm current is $I_{total} = 1.85\text{ Amperes}$. The circuit route length from the Fire Alarm Control Panel (FACP) to the furthest device is $320\text{ feet}$. Solid 14 AWG FPLR copper cable is specified ($R_{75} = 3.07\ \Omega/\text{kft}$). Sizing must be evaluated under worst-case battery depletion ($V_{source} = 20.4\text{ VDC}$) using the EOL Lump-Sum method. Maximum allowable voltage drop is to ensure $V_{EOL} \ge 16.0\text{ VDC}$.</p>

            <p><strong>Step 1: Calculate Total Loop Resistance ($R_{loop}$)</strong></p>
            <p>One-way length is $320\text{ feet}$; round-trip conductor length is $2 \times 320 = 640\text{ feet}$.</p>
            <p>$$R_{loop} = \frac{640\text{ ft} \times 3.07\ \Omega}{1000\text{ ft}} = 1.9648\ \Omega$$</p>

            <p><strong>Step 2: Calculate Circuit Voltage Drop ($\Delta V$)</strong></p>
            <p>$$\Delta V = I_{total} \times R_{loop} = 1.85\text{ A} \times 1.9648\ \Omega = 3.635\text{ Volts}$$</p>

            <p><strong>Step 3: Determine End-of-Line Terminal Voltage ($V_{EOL}$)</strong></p>
            <p>$$V_{EOL} = V_{source} - \Delta V = 20.4\text{ VDC} - 3.635\text{ VDC} = 16.765\text{ VDC}$$</p>
            <p>Since $16.765\text{ VDC} \ge 16.0\text{ VDC}$, the circuit satisfies NFPA 72 and UL 864 requirements with a healthy $0.765\text{ V}$ safety margin.</p>

            <p><strong>Step 4: Compute Maximum Allowable Circuit Distance</strong></p>
            <p>The maximum permissible distance before $V_{EOL}$ reaches the $16.0\text{ V}$ threshold ($\Delta V_{max} = 4.4\text{ V}$):</p>
            <p>$$L_{max} = \frac{\Delta V_{max} \times 1000}{2 \times I_{total} \times R_{wire}} = \frac{4.4 \times 1000}{2 \times 1.85 \times 3.07} = \frac{4400}{11.359} = 387.35\text{ feet}$$</p>
            <p>The proposed $320\text{ ft}$ run is well within the $387\text{ ft}$ maximum ceiling.</p>
          </div>

          <h2>Frequently Asked Questions (NAC Voltage Drop)</h2>
          <div class="faq-item">
            <h3>What is the difference between Class A and Class B NAC circuits?</h3>
            <p>A Class B circuit is a radial circuit terminating in an End-of-Line resistor (EOLR); a single open-circuit fault prevents downstream devices from operating. A Class A circuit loops back from the last device to the FACP; during a single open fault, the panel drives signals from both ends, ensuring all notification appliances continue operating.</p>
          </div>

          <div class="faq-item">
            <h3>Why do modern LED strobes draw significantly less current than xenon strobes?</h3>
            <p>Traditional xenon flash tubes require high-voltage capacitor discharges that consume substantial peak current (e.g. $150\text{ mA}$ to $250\text{ mA}$ per 75-candela strobe). Modern solid-state LED strobes utilize high-efficiency optical lenses and pulse-width drivers, drawing as little as $25\text{ mA}$ to $40\text{ mA}$ for identical light output, permitting up to $4\times$ longer NAC wire runs without excessive voltage drop.</p>
          </div>

          <div class="faq-item">
            <h3>How do NAC Power Boosters (Remote Power Supplies) solve voltage drop issues?</h3>
            <p>When an existing building expansion requires additional notification appliances or long wire runs exceeding $500\text{ feet}$, installing an auxiliary NAC Power Extender (booster panel) closer to the load centers provides fresh $24\text{V}$ power directly from an internal power supply and battery set, eliminating long voltage drop runs back to the main FACP.</p>
          </div>

          <div class="faq-item">
            <h3>Does wire temperature affect fire alarm voltage drop calculations?</h3>
            <p>Yes. Copper electrical resistance increases by approximately $0.393\%$ per $^\circ\text{C}$. During an active building fire, ambient temperatures inside ceiling plenums and risers rise rapidly. Evaluating wire resistance at $75^\circ\text{C}$ (rather than $20^\circ\text{C}$ laboratory ambient) is standard engineering best practice mandated by fire protection authorities.</p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar" id="toolSidebar">
        <!-- Dynamically rendered sidebar -->
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; 2026 CalcHub. All rights reserved. Engineering and mathematical tools grounded in international standards.</p>
      <ul class="footer-links">
        <li><a href="index.html">Home</a></li>
        <li><a href="engineering.html">Engineering</a></li>
        <li><a href="ohms-law-calculator.html">Ohm's Law</a></li>
        <li><a href="sitemap.xml">Sitemap</a></li>
      </ul>
    </div>
  </footer>

  <script>
    // Solid copper resistance per 1000 ft
    const nacWireRes = {
      "12": { "60": 1.78, "75": 1.93 },
      "14": { "60": 2.82, "75": 3.07 },
      "16": { "60": 4.58, "75": 4.99 },
      "18": { "60": 7.14, "75": 7.77 }
    };

    function calculateNac() {
      const vSource = parseFloat(document.getElementById("nacSourceVoltage").value) || 20.4;
      const awg = document.getElementById("nacWireGauge").value;
      const current = parseFloat(document.getElementById("nacTotalCurrent").value) || 0.1;
      const lengthFt = parseFloat(document.getElementById("nacCircuitLength").value) || 10;
      const method = document.getElementById("nacCalcMethod").value;
      const temp = document.getElementById("nacWireTemp").value;

      const rPerKft = nacWireRes[awg][temp] || 3.07;
      const loopFactor = (method === "lump_center") ? 0.5 : 1.0;

      // Round trip resistance = 2 * length * r_per_ft
      const rLoopActual = (2 * lengthFt * rPerKft) / 1000;
      const rEffective = rLoopActual * loopFactor;

      const deltaV = current * rEffective;
      const vEol = vSource - deltaV;
      const pctDrop = (deltaV / vSource) * 100;

      // Max distance before reaching 16.0V
      const allowableDrop = vSource - 16.0;
      let maxDistFt = 0;
      if (allowableDrop > 0 && current > 0) {
        maxDistFt = (allowableDrop * 1000) / (2 * current * rPerKft * loopFactor);
      }

      document.getElementById("nacEolVoltageOut").innerText = vEol.toFixed(2) + " VDC";
      document.getElementById("nacDropOut").innerText = deltaV.toFixed(2) + " VDC";
      document.getElementById("nacLoopResOut").innerText = rLoopActual.toFixed(3) + " \u03A9";
      document.getElementById("nacPctOut").innerText = pctDrop.toFixed(1) + "%";
      document.getElementById("nacMaxDistOut").innerText = Math.floor(maxDistFt) + " feet";

      const statusEl = document.getElementById("nacStatusOut");
      if (vEol >= 16.0) {
        statusEl.innerText = "PASS: Compliant with NFPA 72 & UL 864 (>= 16.0 VDC)";
        statusEl.style.color = "#10b981";
      } else {
        statusEl.innerText = "FAIL: EOL Voltage Below 16.0V UL Cutoff! Upsize wire or add booster.";
        statusEl.style.color = "#ef4444";
      }
    }

    document.addEventListener("DOMContentLoaded", function() {
      calculateNac();
    });
  </script>
</body>
</html>
"""

TOOL_4_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Single Phase Cable Sizing Calculator | 230V & 120V Electrical Wire Sizing</title>
  <meta name="description" content="Calculate single-phase low-voltage electrical cable size (mm² & AWG) for 230V, 120V, and 240V circuits. Computes continuous current, 2-wire loop voltage drop, and installation deratings per IEC 60364 and NEC.">
  <link rel="canonical" href="https://calchub.cloud/single-phase-cable-sizing-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "Single Phase Cable Sizing Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Single-phase electrical cable dimensioning engine calculating live-neutral 2-wire loop voltage drop, continuous thermal ampacity, and breaker coordination.",
        "offers": {
          "@type": "Offer",
          "price": "0.00",
          "priceCurrency": "USD"
        }
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "Why is voltage drop doubled in a single-phase circuit?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In a single-phase 2-wire AC circuit, current travels out to the load along the active phase conductor and returns through the neutral conductor. Because both conductors have identical resistance R, the total loop resistance is 2 * R. In contrast, balanced three-phase circuits share a common neutral carrying zero fundamental current, resulting in a voltage drop multiplier of sqrt(3) approx 1.732 instead of 2.0."
            }
          },
          {
            "@type": "Question",
            "name": "How does power factor affect single-phase cable sizing?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For a given real power P (in watts), current is inversely proportional to power factor: I = P / (V * cos(theta)). An inductive load operating at a poor power factor of 0.70 draws 42.8% more current than a unity power factor load (1.0), requiring significantly larger conductors to prevent thermal overload."
            }
          },
          {
            "@type": "Question",
            "name": "What are standard single-phase residential cable sizes?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In international metric practice (BS 7671/IEC): 1.5 mm² is standard for lighting (6A–10A), 2.5 mm² for standard socket ring/radial circuits (16A–20A), 4.0 mm² and 6.0 mm² for heavy appliances (32A cookers/showers), and 10 mm² to 16 mm² for sub-mains (40A–63A). In North America: #14 AWG (15A), #12 AWG (20A), #10 AWG (30A), and #8 AWG (40A–50A)."
            }
          },
          {
            "@type": "Question",
            "name": "What are maximum allowable single-phase voltage drop limits?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Under IEC 60364-5-52 and BS 7671: maximum 3% (6.9V on 230V) for lighting circuits, and maximum 5% (11.5V on 230V) for general power circuits. Under NEC recommendations: maximum 3% on branch circuits, and 5% total from service panel to the furthest outlet."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="engineering">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">
        <span class="logo-icon">&pi;</span>
        <span class="logo-text">Calc<strong>Hub</strong></span>
      </a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="engineering.html" class="active">Engineering</a>
        <a href="solar-energy.html">Solar</a>
        <a href="fire-safety.html">Fire Safety</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo;
      <a href="engineering.html">Electrical &amp; Power Systems</a> &rsaquo;
      <span>Single Phase Cable Sizing Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">IEC 60364 &amp; NEC Single-Phase Dimensioning</div>
          <h1 class="calc-title">Single Phase Cable Sizing Calculator</h1>
          <p class="calc-tagline">Calculate copper and aluminum wire sizes for 230V, 120V, and 240V single-phase electrical branch circuits and sub-mains.</p>
        </header>

        <!-- Tool Card -->
        <div class="tool-card">
          <form id="singlePhaseForm" onsubmit="return false;">
            <div class="calc-grid">
              <div class="form-group">
                <label for="spVoltage" class="form-label">Single-Phase Voltage</label>
                <select id="spVoltage" class="form-control" onchange="calculateSinglePhase()">
                  <option value="230" selected>230V AC (UK / Europe / International Standard)</option>
                  <option value="120">120V AC (North American Standard Wall Socket)</option>
                  <option value="240">240V AC (North American Split-Phase Dryer/EV)</option>
                  <option value="277">277V AC (North American Commercial Lighting)</option>
                </select>
                <small class="form-hint">Nominal line-to-neutral or line-to-line</small>
              </div>

              <div class="form-group">
                <label for="spLoadCurrent" class="form-label">Load Operating Current ($I_b$)</label>
                <div class="input-with-unit">
                  <input type="number" id="spLoadCurrent" class="form-control" value="25" min="0.5" max="500" step="1" oninput="calculateSinglePhase()">
                  <span class="unit-badge">Amps</span>
                </div>
                <small class="form-hint">Design operating current</small>
              </div>

              <div class="form-group">
                <label for="spBreakerIn" class="form-label">Protective Device Rating ($I_n$)</label>
                <div class="input-with-unit">
                  <input type="number" id="spBreakerIn" class="form-control" value="32" min="6" max="630" step="1" oninput="calculateSinglePhase()">
                  <span class="unit-badge">Amps</span>
                </div>
                <small class="form-hint">Circuit breaker / fuse rating (Ib &le; In &le; Iz)</small>
              </div>

              <div class="form-group">
                <label for="spConductor" class="form-label">Conductor Metallurgy</label>
                <select id="spConductor" class="form-control" onchange="calculateSinglePhase()">
                  <option value="copper" selected>Annealed Copper (Cu)</option>
                  <option value="aluminum">Electrical Aluminum (Al)</option>
                </select>
                <small class="form-hint">Core conductor material</small>
              </div>

              <div class="form-group">
                <label for="spInsulation" class="form-label">Insulation Thermal Class</label>
                <select id="spInsulation" class="form-control" onchange="calculateSinglePhase()">
                  <option value="pvc" selected>PVC / 70°C Thermoplastic</option>
                  <option value="xlpe">XLPE / 90°C Thermosetting</option>
                </select>
                <small class="form-hint">Continuous operating limit</small>
              </div>

              <div class="form-group">
                <label for="spInstallMethod" class="form-label">Installation Reference Method</label>
                <select id="spInstallMethod" class="form-control" onchange="calculateSinglePhase()">
                  <option value="C" selected>Method C: Clipped direct to masonry surface</option>
                  <option value="A">Method A: In conduit in thermally insulated wall</option>
                  <option value="B">Method B: In conduit on wooden/masonry wall</option>
                  <option value="E">Method E: In free air on perforated cable tray</option>
                </select>
                <small class="form-hint">Governs thermal dissipation</small>
              </div>

              <div class="form-group">
                <label for="spRouteLength" class="form-label">One-Way Circuit Length ($L$)</label>
                <div class="input-with-unit">
                  <input type="number" id="spRouteLength" class="form-control" value="30" min="1" step="2" oninput="calculateSinglePhase()">
                  <span class="unit-badge">metres</span>
                </div>
                <small class="form-hint">Distance from panelboard to load</small>
              </div>

              <div class="form-group">
                <label for="spAmbientTemp" class="form-label">Ambient Temperature</label>
                <div class="input-with-unit">
                  <input type="number" id="spAmbientTemp" class="form-control" value="30" min="10" max="65" step="1" oninput="calculateSinglePhase()">
                  <span class="unit-badge">°C</span>
                </div>
                <small class="form-hint">Surrounding air temperature</small>
              </div>

              <div class="form-group">
                <label for="spMaxVd" class="form-label">Max Allowable Voltage Drop</label>
                <div class="input-with-unit">
                  <input type="number" id="spMaxVd" class="form-control" value="4.0" min="1.0" max="10.0" step="0.5" oninput="calculateSinglePhase()">
                  <span class="unit-badge">%</span>
                </div>
                <small class="form-hint">Standard threshold (3% lighting, 5% power)</small>
              </div>
            </div>

            <button type="button" id="calcSpBtn" class="btn btn-primary btn-block" onclick="calculateSinglePhase()">Calculate Single-Phase Cable</button>
          </form>

          <div id="spResultBox" class="results-container" style="margin-top:20px;">
            <h3>Single-Phase Sizing Results</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label">Recommended Conductor Area</span>
                <span id="spCableSizeOut" class="result-value">-- mm²</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Derated Current Capacity ($I_z$)</span>
                <span id="spIzOut" class="result-value">-- A</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Two-Wire Loop Voltage Drop ($\Delta V$)</span>
                <span id="spVdOut" class="result-value">-- V (-- %)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Circuit Loop Resistance ($R_{loop}$)</span>
                <span id="spLoopResOut" class="result-value">-- &Omega;</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Power Lost in Cable ($I^2 R$)</span>
                <span id="spPowerLossOut" class="result-value">-- Watts</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Overcurrent Protection Verification</span>
                <span id="spStatusOut" class="result-value">--</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Engineering Principles of Single-Phase Low-Voltage Cable Sizing</h2>
          
          <p>Single-phase alternating current (AC) power distribution is the most widespread electrical infrastructure in the modern world, powering homes, commercial offices, municipal facilities, and retail centers. While conceptually straightforward compared to three-phase networks, single-phase circuits present unique thermodynamic and electrical impedance challenges. Because the entire return current must flow through the neutral conductor, single-phase circuits suffer from <strong>double the loop resistance</strong> per unit distance compared to equivalent balanced polyphase configurations.</p>

          <p>Sizing single-phase cables accurately requires adhering to statutory requirements codified in <strong>IEC 60364-5-52</strong>, the UK <strong>BS 7671 (IET Wiring Regulations)</strong>, and <strong>NFPA 70 National Electrical Code (NEC Article 310 &amp; 210)</strong>.</p>

          <div class="formula-box">
            <h3>The Fundamental Overcurrent Coordination Rule</h3>
            <p>Every single-phase branch circuit or sub-feeder must satisfy the core overcurrent protective coordination inequality:</p>
            <p>$$I_b \le I_n \le I_z$$</p>
            <p>Where:</p>
            <ul>
              <li>$I_b$ = Operating design load current in Amperes.</li>
              <li>$I_n$ = Nominal trip rating of the protective circuit breaker or fuse (e.g. 16A, 20A, 32A, 40A, 50A, 63A).</li>
              <li>$I_z$ = Effective continuous current-carrying capacity of the derated installed cable ($I_z = I_0 \times C_a \times C_g$).</li>
            </ul>
          </div>

          <h3>Single-Phase Two-Wire Loop Voltage Drop Formulation</h3>
          <p>In a single-phase two-wire circuit (Active and Neutral), current $I$ leaves the distribution board via the phase conductor, travels distance $L$, passes through the load, and returns across the exact same distance $L$ via the neutral conductor. The total circuit conductor length is therefore $2 \times L$.</p>
          
          <p>The voltage drop across the circuit is governed by the vector projection of complex line impedance ($Z = R + jX$):</p>
          
          <p>$$\Delta V_{1\phi} = 2 \times I \times L \times (R \cos\varphi + X \sin\varphi)$$</p>
          <p>$$\Delta V\% = \frac{\Delta V_{1\phi}}{V_{nominal}} \times 100$$</p>
          
          <p>Where $R$ is the AC resistance of the conductor at operating temperature ($\Omega/\text{m}$), $X$ is line reactance ($\Omega/\text{m}$), and $\cos\varphi$ is the load power factor. In cables with cross-sections under $16\text{ mm}^2$, inductive reactance is negligible ($X \approx 0$), simplifying the equation to Ohm's Law: $\Delta V = 2 \cdot I \cdot L \cdot R$.</p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Conductor Cross-Section (mm²)</th>
                <th>Method C (Clipped Direct) PVC 70°C</th>
                <th>Method A2 (Insulated Cavity) PVC 70°C</th>
                <th>Voltage Drop Factor (mV/A/m)</th>
                <th>Typical Domestic &amp; Commercial Use</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>1.5 mm²</strong></td>
                <td>19.5 A</td>
                <td>14.5 A</td>
                <td>$29.0\text{ mV/A/m}$</td>
                <td>Lighting circuits, smoke detectors, 6A–10A MCB</td>
              </tr>
              <tr>
                <td><strong>2.5 mm²</strong></td>
                <td>27.0 A</td>
                <td>18.5 A</td>
                <td>$18.0\text{ mV/A/m}$</td>
                <td>Ring main &amp; radial socket outlets, 16A–20A MCB</td>
              </tr>
              <tr>
                <td><strong>4.0 mm²</strong></td>
                <td>36.0 A</td>
                <td>25.0 A</td>
                <td>$11.0\text{ mV/A/m}$</td>
                <td>Radial power, water heaters, 25A–32A MCB</td>
              </tr>
              <tr>
                <td><strong>6.0 mm²</strong></td>
                <td>46.0 A</td>
                <td>32.0 A</td>
                <td>$7.3\text{ mV/A/m}$</td>
                <td>Electric cookers, electric showers, 32A–40A MCB</td>
              </tr>
              <tr>
                <td><strong>10.0 mm²</strong></td>
                <td>63.0 A</td>
                <td>43.0 A</td>
                <td>$4.4\text{ mV/A/m}$</td>
                <td>Heavy domestic shower, sub-distribution, 50A MCB</td>
              </tr>
              <tr>
                <td><strong>16.0 mm²</strong></td>
                <td>85.0 A</td>
                <td>57.0 A</td>
                <td>$2.8\text{ mV/A/m}$</td>
                <td>Main residential supply tail, 63A–80A breaker</td>
              </tr>
              <tr>
                <td><strong>25.0 mm²</strong></td>
                <td>112.0 A</td>
                <td>75.0 A</td>
                <td>$1.75\text{ mV/A/m}$</td>
                <td>Heavy 100A residential service entrance sub-main</td>
              </tr>
            </tbody>
          </table>

          <div class="worked-example-card">
            <h3>Practical Worked Engineering Example: Residential EV Charger Radial</h3>
            <p><strong>Design Scenario:</strong> Size a dedicated single-phase 230V radial circuit powering a $7.4\text{ kW}$ residential electric vehicle (EV) charger. The continuous load current is $I_b = 32\text{ Amperes}$ ($\cos\varphi = 1.0$). The circuit is protected by a $32\text{ A}$ Type B RCBO ($I_n = 32\text{ A}$). The cable route is $30\text{ meters}$ long, clipped directly to an interior garage masonry wall (Method C) where ambient summer temperature peaks at $35^\circ\text{C}$. Multi-core copper cable with $70^\circ\text{C}$ PVC insulation is specified. Maximum allowable voltage drop is $4.0\%$.</p>

            <p><strong>Step 1: Determine Environmental Correction Factor ($C_a$)</strong></p>
            <p>For PVC ($70^\circ\text{C}$) at $35^\circ\text{C}$ ambient, $C_a = \sqrt{\frac{70 - 35}{70 - 30}} = \sqrt{\frac{35}{40}} = 0.935$.</p>
            <p>No grouping derating ($C_g = 1.0$).</p>
            <p>Required base tabulated rating:</p>
            <p>$$I_0 \ge \frac{I_n}{C_a} = \frac{32\text{ A}}{0.935} = 34.22\text{ A}$$</p>

            <p><strong>Step 2: Thermal Selection from Table 4D2A (Method C PVC)</strong></p>
            <ul>
              <li>$4.0\text{ mm}^2 \implies I_0 = 36\text{ A}$ ($36 \ge 34.22\text{ A} \implies$ Thermal PASS)</li>
            </ul>
            <p>Derated capacity of $4.0\text{ mm}^2$: $I_z = 36 \times 0.935 = 33.66\text{ A} \ge 32\text{ A}$.</p>

            <p><strong>Step 3: Check Voltage Drop on $4.0\text{ mm}^2$</strong></p>
            <p>For $4.0\text{ mm}^2$ copper, $(mV/A/m) = 11.0\text{ mV/A/m}$:</p>
            <p>$$\Delta V = \frac{11.0 \times 32\text{ A} \times 30\text{ m}}{1000} = \frac{10{,}560}{1000} = 10.56\text{ Volts}$$</p>
            <p>$$\Delta V\% = \frac{10.56\text{ V}}{230\text{ V}} \times 100 = 4.59\%$$</p>
            <p><em>Critical Engineering Finding:</em> While $4.0\text{ mm}^2$ passes thermal ampacity, it <strong>FAILS voltage drop</strong> ($4.59\% > 4.0\%$)! Under heavy charging, EV on-board chargers throttle power when voltage sags excessively.</p>

            <p><strong>Step 4: Upsizing to $6.0\text{ mm}^2$ Conductor</strong></p>
            <p>For $6.0\text{ mm}^2$ copper, $(mV/A/m) = 7.3\text{ mV/A/m}$:</p>
            <p>$$\Delta V = \frac{7.3 \times 32\text{ A} \times 30\text{ m}}{1000} = 7.01\text{ Volts}$$</p>
            <p>$$\Delta V\% = \frac{7.01\text{ V}}{230\text{ V}} \times 100 = 3.05\% \le 4.0\% \quad (\text{PASS!})$$</p>
            <p>The engineer correctly specifies <strong>$6.0\text{ mm}^2$ Copper PVC</strong> to satisfy both thermal and voltage drop standards.</p>
          </div>

          <h2>Frequently Asked Questions (Single-Phase Cable Sizing)</h2>
          <div class="faq-item">
            <h3>Why does an EV charger require a dedicated radial rather than tapping an existing ring circuit?</h3>
            <p>Electric vehicle charging draws maximum rated current continuously for 4 to 8 hours. Standard domestic ring final circuits (wired in 2.5 mm² protected by a 32A breaker) are designed for intermittent diversity loads. Subjecting a ring circuit to continuous 32A charging creates thermal hotspots at socket terminals, risking joint melting and fire.</p>
          </div>

          <div class="faq-item">
            <h3>What is the minimum cable size for an electric instantaneous shower?</h3>
            <p>Modern electric showers range from $8.5\text{ kW}$ ($37\text{ A}$ at 230V) to $10.5\text{ kW}$ ($45.6\text{ A}$ at 230V). Due to thermal deratings in loft insulation and voltage drop, an $8.5\text{ kW}$ shower typically requires $6.0\text{ mm}^2$ or $10.0\text{ mm}^2$ cable, while a $9.5\text{ kW}$ or $10.5\text{ kW}$ shower strictly requires $10.0\text{ mm}^2$ copper protected by a 45A or 50A MCB/RCBO.</p>
          </div>

          <div class="faq-item">
            <h3>Can I use a 2-core cable without an earth wire for single-phase circuits?</h3>
            <p>No. Under modern international regulations (BS 7671, IEC 60364, and NEC), all low-voltage AC wiring must incorporate a dedicated Circuit Protective Conductor (CPC / earth wire). Even if appliances are double-insulated (Class II), the protective earth must be present at all outlet boxes and accessory points for future safety.</p>
          </div>

          <div class="faq-item">
            <h3>How do harmonics in modern electronic power supplies affect the single-phase neutral?</h3>
            <p>In single-phase circuits, harmonic distortion does not create neutral overloading (unlike three-phase systems where triplen harmonics sum in the neutral). The neutral carries exactly the same RMS current as the phase conductor. Both phase and neutral conductors must always be sized with identical cross-sectional areas.</p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar" id="toolSidebar">
        <!-- Dynamically rendered sidebar -->
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; 2026 CalcHub. All rights reserved. Engineering and mathematical tools grounded in international standards.</p>
      <ul class="footer-links">
        <li><a href="index.html">Home</a></li>
        <li><a href="engineering.html">Engineering</a></li>
        <li><a href="ohms-law-calculator.html">Ohm's Law</a></li>
        <li><a href="sitemap.xml">Sitemap</a></li>
      </ul>
    </div>
  </footer>

  <script>
    // Standard IEC Single-Phase Ratings Table (Copper base values)
    const spRatings = [
      { size: 1.5,  c_pvc: 19.5, c_xlpe: 26,  mv: 29.0, r_cu: 12.1 },
      { size: 2.5,  c_pvc: 27.0, c_xlpe: 36,  mv: 18.0, r_cu: 7.41 },
      { size: 4.0,  c_pvc: 36.0, c_xlpe: 49,  mv: 11.0, r_cu: 4.61 },
      { size: 6.0,  c_pvc: 46.0, c_xlpe: 62,  mv: 7.3,  r_cu: 3.08 },
      { size: 10.0, c_pvc: 63.0, c_xlpe: 85,  mv: 4.4,  r_cu: 1.83 },
      { size: 16.0, c_pvc: 85.0, c_xlpe: 110, mv: 2.8,  r_cu: 1.15 },
      { size: 25.0, c_pvc: 112,  c_xlpe: 146, mv: 1.75, r_cu: 0.727 },
      { size: 35.0, c_pvc: 138,  c_xlpe: 180, mv: 1.25, r_cu: 0.524 },
      { size: 50.0, c_pvc: 168,  c_xlpe: 219, mv: 0.93, r_cu: 0.387 }
    ];

    const spMethodMultipliers = {
      "C": 1.00,
      "A": 0.72,
      "B": 0.85,
      "E": 1.10
    };

    function calculateSinglePhase() {
      const vNom = parseFloat(document.getElementById("spVoltage").value) || 230;
      const ib = parseFloat(document.getElementById("spLoadCurrent").value) || 1;
      const inVal = parseFloat(document.getElementById("spBreakerIn").value) || 16;
      const conductor = document.getElementById("spConductor").value;
      const insulation = document.getElementById("spInsulation").value;
      const method = document.getElementById("spInstallMethod").value;
      const length = parseFloat(document.getElementById("spRouteLength").value) || 1;
      const ambTemp = parseFloat(document.getElementById("spAmbientTemp").value) || 30;
      const maxVd = parseFloat(document.getElementById("spMaxVd").value) || 4.0;

      // Ca
      let ca = 1.0;
      if (insulation === "xlpe") {
        ca = Math.sqrt(Math.max(0.1, (90 - ambTemp) / (90 - 30)));
      } else {
        ca = Math.sqrt(Math.max(0.1, (70 - ambTemp) / (70 - 30)));
      }

      const methodMult = spMethodMultipliers[method] || 1.0;
      const condMult = (conductor === "aluminum") ? 0.78 : 1.0;

      let selected = null;

      for (let i = 0; i < spRatings.length; i++) {
        const row = spRatings[i];
        const baseRating = (insulation === "xlpe") ? row.c_xlpe : row.c_pvc;
        const deratedIz = baseRating * methodMult * condMult * ca;

        if (deratedIz < inVal) continue;

        let mvVal = row.mv;
        if (conductor === "aluminum") mvVal *= 1.64;

        const deltaV = (mvVal * ib * length) / 1000;
        const vdPct = (deltaV / vNom) * 100;

        if (vdPct <= maxVd) {
          // Loop resistance = 2 * length * r
          const rPerM = (row.r_cu * ((conductor === "aluminum") ? 1.64 : 1.0)) / 1000;
          const rLoop = 2 * length * rPerM;
          const powerLoss = ib * ib * rLoop;

          selected = {
            size: row.size,
            iz: deratedIz,
            deltaV: deltaV,
            vdPct: vdPct,
            rLoop: rLoop,
            powerLoss: powerLoss
          };
          break;
        }
      }

      if (selected) {
        document.getElementById("spCableSizeOut").innerText = selected.size + " mm² (" + conductor.toUpperCase() + ")";
        document.getElementById("spIzOut").innerText = selected.iz.toFixed(1) + " A";
        document.getElementById("spVdOut").innerText = selected.deltaV.toFixed(2) + " V (" + selected.vdPct.toFixed(2) + "%)";
        document.getElementById("spLoopResOut").innerText = selected.rLoop.toFixed(3) + " \u03A9";
        document.getElementById("spPowerLossOut").innerText = selected.powerLoss.toFixed(1) + " W";
        document.getElementById("spStatusOut").innerText = "Fully Compliant (Ib <= In <= Iz)";
        document.getElementById("spStatusOut").style.color = "#10b981";
      } else {
        document.getElementById("spCableSizeOut").innerText = "> 50 mm²";
        document.getElementById("spIzOut").innerText = "--";
        document.getElementById("spVdOut").innerText = "Exceeds Drop Limit";
        document.getElementById("spLoopResOut").innerText = "--";
        document.getElementById("spPowerLossOut").innerText = "--";
        document.getElementById("spStatusOut").innerText = "Non-Compliant: Upsize or Parallel Feeder Required";
        document.getElementById("spStatusOut").style.color = "#ef4444";
      }
    }

    document.addEventListener("DOMContentLoaded", function() {
      calculateSinglePhase();
    });
  </script>
</body>
</html>
"""

def main():
    root = r"C:\Users\Admin\.gemini\antigravity\scratch\calchub"
    
    p3 = os.path.join(root, "nac-voltage-drop-calculator.html")
    with open(p3, "w", encoding="utf-8") as f:
        f.write(TOOL_3_HTML.strip() + "\n")
    print("[PASS] nac-voltage-drop-calculator.html generated successfully!")

    p4 = os.path.join(root, "single-phase-cable-sizing-calculator.html")
    with open(p4, "w", encoding="utf-8") as f:
        f.write(TOOL_4_HTML.strip() + "\n")
    print("[PASS] single-phase-cable-sizing-calculator.html generated successfully!")

if __name__ == "__main__":
    main()
