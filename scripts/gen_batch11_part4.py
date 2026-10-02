# -*- coding: utf-8 -*-
"""
Script to generate Batch 11 Part 4 tools:
7. torque-converter.html
8. torque-to-hp-calculator.html
"""
import os

TOOL_7_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Torque Converter Calculator | Stall Speed, Torque Ratio &amp; K-Factor</title>
  <meta name="description" content="Calculate torque converter stall speed, torque multiplication ratio (TR), speed ratio (SR), K-factor, hydraulic transmission efficiency, and heat rejection.">
  <link rel="canonical" href="https://calchub.cloud/torque-converter.html">
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
        "name": "Torque Converter Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Hydrodynamic fluid coupling and torque converter analysis calculator evaluating stall torque ratio, speed ratio, K-factor capacity, and thermal heat generation per SAE J643.",
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
            "name": "How does a hydrodynamic torque converter multiply engine torque?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A torque converter consists of an impeller (pump), turbine, and stator. When the turbine is stationary or rotating slowly (high slip), fluid discharged by the turbine strikes the stator vanes. The stationary stator redirects fluid momentum into the rotation direction of the impeller, creating hydrodynamic torque multiplication typically between 1.8:1 and 2.5:1 at stall."
            }
          },
          {
            "@type": "Question",
            "name": "What is the Coupling Point of a torque converter?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The coupling point occurs when the turbine accelerates to approximately 85% to 90% of impeller speed (Speed Ratio SR approx 0.85-0.90). At this threshold, fluid leaves the turbine at an angle that no longer hits the front of the stator vanes; the stator one-way sprag clutch unlocks and freewheels, causing torque multiplication to drop to 1.0:1 where the unit acts as a simple fluid coupling."
            }
          },
          {
            "@type": "Question",
            "name": "What is the Torque Converter K-Factor?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The K-factor represents the hydrodynamic capacity of a torque converter, defined as K = RPM / sqrt(Torque). A higher K-factor indicates a 'looser' converter that stalls at higher RPM for a given engine torque; a lower K-factor indicates a 'tighter' converter suited for heavy towing and diesel applications."
            }
          },
          {
            "@type": "Question",
            "name": "Why does a torque converter generate so much heat at low vehicle speeds?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Converter efficiency is the product of torque ratio and speed ratio: eta = TR * SR. At zero vehicle speed (stall condition), SR = 0, so mechanical efficiency is 0%. Exactly 100% of engine power input is converted directly into thermal heat inside the automatic transmission fluid (ATF), necessitating dedicated external oil coolers."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="mechanical">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">
        <span class="logo-icon">&pi;</span>
        <span class="logo-text">Calc<strong>Hub</strong></span>
      </a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="engineering.html">Engineering</a>
        <a href="mechanical.html" class="active">Mechanical</a>
        <a href="solar-energy.html">Solar</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo; 
      <a href="engineering.html">Engineering</a> &rsaquo; 
      <a href="mechanical.html">Mechanical</a> &rsaquo; 
      <span>Torque Converter Calculator</span>
    </nav>

    <header class="calc-header">
      <div class="calc-badge">Hydrodynamics &amp; Transmissions</div>
      <h1 class="calc-title">Torque Converter Calculator</h1>
      <p class="calc-tagline">Evaluate hydrodynamic torque multiplication ($TR$), turbine output torque, converter efficiency, capacity K-factor, and transmission heat dissipation per SAE J643.</p>
    </header>

    <div class="calc-grid">
      <div class="calc-main">
        <div class="tool-card">
          <form id="tcForm">
            <div class="form-row">
              <div class="form-group">
                <label for="engineTorque">Engine Input Torque ($T_{pump}$ in N&middot;m)</label>
                <input type="number" id="engineTorque" class="form-control" value="450" min="1" step="any" required>
                <span class="hint">Flywheel gross torque delivered to converter impeller</span>
              </div>
              <div class="form-group">
                <label for="engineRpm">Engine Input Speed ($N_{pump}$ in RPM)</label>
                <input type="number" id="engineRpm" class="form-control" value="2800" min="100" step="any" required>
                <span class="hint">Crankshaft / impeller rotational velocity</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="turbineRpm">Transmission Turbine Speed ($N_{turbine}$ in RPM)</label>
                <input type="number" id="turbineRpm" class="form-control" value="1400" min="0" step="any" required>
                <span class="hint">Output shaft speed (set 0 for complete stall condition)</span>
              </div>
              <div class="form-group">
                <label for="stallRatioPreset">Stall Torque Multiplication Ratio ($TR_{stall}$)</label>
                <select id="stallRatioPreset" class="form-control">
                  <option value="1.8">1.80 : 1 - Low Stall / Heavy Commercial Diesel</option>
                  <option value="2.0">2.00 : 1 - Standard Passenger Car / SUV</option>
                  <option value="2.2" selected>2.20 : 1 - Performance Street / Light Truck</option>
                  <option value="2.5">2.50 : 1 - High-Stall Drag Racing / High-RPM Cam</option>
                </select>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="lockupActive">Lockup TCC (Torque Converter Clutch) Status</label>
                <select id="lockupActive" class="form-control">
                  <option value="no" selected>Disengaged (Pure Hydrodynamic Fluid Drive)</option>
                  <option value="yes">Engaged (100% Mechanical Lockup &ndash; Zero Slip)</option>
                </select>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcTcBtn">Calculate Converter Hydrodynamics</button>
              <button type="reset" class="btn btn-secondary" id="resetTcBtn">Reset</button>
            </div>
          </form>

          <div id="tcResultBox" class="results-container" style="display: none; margin-top: 1.5rem;">
            <h3>Calculated Hydrodynamic Transmission Metrics</h3>
            <div class="results-grid">
              <div class="result-tile highlight">
                <span class="result-label">Turbine Output Shaft Torque ($T_{turbine}$)</span>
                <span class="result-value" id="resTurbineTorque">-- N·m</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Effective Torque Ratio ($TR$)</span>
                <span class="result-value" id="resTorqueRatio">-- : 1</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Speed Ratio ($SR = N_t / N_p$)</span>
                <span class="result-value" id="resSpeedRatio">--</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Converter Hydrodynamic Efficiency ($\eta$)</span>
                <span class="result-value" id="resEfficiency">-- %</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Converter Capacity K-Factor</span>
                <span class="result-value" id="resKFactor">--</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Fluid Heat Dissipation Rate ($P_{heat}$)</span>
                <span class="result-value" id="resHeatPower">-- kW</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Operating Regime Assessment</span>
                <span class="result-value" id="resRegimeStatus">--</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Hydrodynamic Principles of Torque Converters (SAE J643)</h2>
          <p>
            In automatic transmission drivetrains, heavy construction equipment (bulldozers, wheel loaders), and railway diesel-hydraulic locomotives, the <strong>torque converter</strong> functions as an automatic fluid clutch and continuously variable hydraulic torque amplifier. Unlike a simple two-element fluid coupling (which can only transfer torque at a 1:1 ratio with inherent slip losses), a hydrodynamic torque converter incorporates three distinct bladed elements operating inside a sealed, oil-filled toroidal casing:
          </p>
          <ol>
            <li><strong>Impeller (Pump):</strong> Bolted directly to the engine flexplate/flywheel, the pump rotates at crankshaft speed and accelerates automatic transmission fluid (ATF) radially outward via centrifugal force.</li>
            <li><strong>Turbine:</strong> Splined directly to the transmission input shaft, the turbine receives the high-velocity fluid discharged from the impeller, absorbing kinetic momentum to generate driving torque.</li>
            <li><strong>Stator:</strong> Mounted between the turbine outlet and impeller inlet on a stationary reaction shaft via a one-way overrunning sprag clutch, the stator redirects returning fluid momentum into the rotation direction of the impeller.</li>
          </ol>

          <h2>Torque Multiplication Mechanics and the Coupling Point</h2>
          <p>
            When a vehicle is stationary with the brakes applied and throttle opened, the condition is termed <strong>Stall</strong> ($N_{turbine} = 0$, Speed Ratio $SR = 0$). In this regime, fluid exits the turbine blades with high reverse velocity. The stationary stator vanes intercept this counter-rotating flow and deflect it forward into the suction eye of the impeller. This redirected momentum aids engine rotation rather than opposing it, producing physical <strong>Torque Multiplication ($TR$)</strong>:
          </p>
          <div class="formula-box">
            $$TR = \frac{T_{turbine}}{T_{pump}} \approx 1.8 \text{ to } 2.5 \quad (\text{At Stall})$$
          </div>
          <p>
            As vehicle acceleration commences, turbine speed rises toward pump speed. The dimensionless <strong>Speed Ratio ($SR$)</strong> increases:
          </p>
          <div class="formula-box">
            $$SR = \frac{N_{turbine}}{N_{pump}}$$
          </div>
          <p>
            As $SR$ increases, the angle at which fluid exits the turbine continuously changes. When $SR$ reaches approximately $0.85 \text{ to } 0.90$, fluid strikes the back faces of the stator blades. The one-way sprag clutch releases, allowing the stator to freewheel effortlessly in the oil stream. This transition is the <strong>Coupling Point</strong>. Beyond the coupling point, torque multiplication ceases ($TR = 1.0$), and the converter functions as a classic fluid coupling.
          </p>

          <h2>Hydrodynamic Efficiency ($\eta$) and Heat Generation</h2>
          <p>
            Mechanical transmission efficiency is defined as the ratio of turbine output power to impeller input power:
          </p>
          <div class="formula-box">
            $$\eta = \frac{P_{turbine}}{P_{pump}} = \frac{T_{turbine} \cdot \omega_{turbine}}{T_{pump} \cdot \omega_{pump}} = \left(\frac{T_{turbine}}{T_{pump}}\right) \cdot \left(\frac{N_{turbine}}{N_{pump}}\right) = TR \cdot SR$$
          </div>
          <p>
            At stall ($SR = 0$), efficiency is precisely zero: $\eta = TR \times 0 = 0\%$. Exactly 100% of engine power input is converted into turbulent viscous shear and fluid friction inside the automatic transmission fluid (ATF). The rate of thermal heat generation ($P_{heat}$) rejected into the transmission oil is:
          </p>
          <div class="formula-box">
            $$P_{in} (\text{kW}) = \frac{T_{pump} (\text{N}\cdot\text{m}) \times N_{pump} (\text{RPM})}{9548.8}$$
            $$P_{heat} (\text{kW}) = P_{in} \cdot (1 - \eta)$$
          </div>
          <p>
            This thermal spike explains why prolonged stall testing (power braking) will boil transmission fluid and destroy internal rubber seals within 15 to 30 seconds unless a lockup clutch or neutral idle disengagement is activated.
          </p>

          <h2>The Converter Capacity K-Factor</h2>
          <p>
            In torque converter performance modeling (SAE J643), the <strong>K-factor</strong> characterizes the hydrodynamic capacity and flow resistance of the toroidal blading:
          </p>
          <div class="formula-box">
            $$K = \frac{N}{\sqrt{T}} \quad \left[\frac{\text{RPM}}{\sqrt{\text{N}\cdot\text{m}}} \text{ or } \frac{\text{RPM}}{\sqrt{\text{lb}\cdot\text{ft}}}\right]$$
          </div>
          <p>
            A torque converter with a higher K-factor exhibits less hydrodynamic resistance to flow, allowing the engine to flash to a higher stall RPM before pump torque balances engine torque output. Race vehicles utilize high-K converters (stall speeds of 3,500 to 5,500 RPM) to launch engines directly within their peak torque and horsepower powerbands.
          </p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Speed Ratio ($SR$)</th>
                <th>Torque Ratio ($TR$)</th>
                <th>Efficiency ($\eta$)</th>
                <th>Converter Operating Mode</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>$SR = 0.00$ (Full Stall)</td>
                <td>2.0 &ndash; 2.5 : 1</td>
                <td>0.0%</td>
                <td>Maximum torque multiplication; 100% heat dissipation</td>
              </tr>
              <tr>
                <td>$SR = 0.40$ (Low Speed)</td>
                <td>1.6 &ndash; 1.8 : 1</td>
                <td>64.0% &ndash; 72.0%</td>
                <td>High acceleration thrust; active stator redirection</td>
              </tr>
              <tr>
                <td>$SR = 0.70$ (Mid Acceleration)</td>
                <td>1.2 &ndash; 1.3 : 1</td>
                <td>84.0% &ndash; 91.0%</td>
                <td>Diminishing torque boost; stator approaching freewheel</td>
              </tr>
              <tr>
                <td>$SR = 0.88$ (Coupling Point)</td>
                <td>1.00 : 1</td>
                <td>88.0%</td>
                <td>Stator sprag clutch unlocks; begins freewheeling</td>
              </tr>
              <tr>
                <td>$SR = 0.95$ (Fluid Coupling)</td>
                <td>1.00 : 1</td>
                <td>95.0%</td>
                <td>Cruising speed; 5% fluid slip loss</td>
              </tr>
              <tr>
                <td>$SR = 1.00$ (TCC Locked)</td>
                <td>1.00 : 1</td>
                <td>100.0%</td>
                <td>Mechanical lockup clutch engaged; zero slip, zero heat</td>
              </tr>
            </tbody>
          </table>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: Heavy Off-Highway Dump Truck Launch Analysis</h3>
            <p><strong>Design Scenario:</strong> An off-highway mining dump truck is powered by a heavy-duty diesel engine delivering $T_{pump} = 1,850\text{ N}\cdot\text{m}$ of gross flywheel torque at $N_{pump} = 1,900\text{ RPM}$ during grade launch. The transmission uses a heavy-duty hydrodynamic torque converter with a stall torque ratio of $TR_{stall} = 2.20:1$. The truck is moving slowly up an incline, with the transmission turbine rotating at $N_{turbine} = 760\text{ RPM}$. Determine the speed ratio, interpolated torque multiplication ratio, turbine output torque delivered to the gearbox, transmission efficiency, and the rate of thermal heat rejection to the transmission fluid cooler.</p>
            
            <p><strong>Step 1: Calculate the Speed Ratio ($SR$)</strong></p>
            <div class="formula-box">
              $$SR = \frac{N_{turbine}}{N_{pump}} = \frac{760\text{ RPM}}{1,900\text{ RPM}} = 0.40$$
            </div>

            <p><strong>Step 2: Interpolate Torque Ratio ($TR$) at $SR = 0.40$</strong></p>
            <p>Assuming standard linear decay between stall ($TR = 2.20$ at $SR = 0$) and the coupling point ($TR = 1.00$ at $SR = 0.88$):</p>
            <div class="formula-box">
              $$TR(SR) = TR_{stall} - \left(\frac{TR_{stall} - 1.00}{0.88}\right) \times SR = 2.20 - \left(\frac{1.20}{0.88}\right) \times 0.40 = 2.20 - 0.5455 \approx 1.655:1$$
            </div>

            <p><strong>Step 3: Calculate Turbine Output Shaft Torque ($T_{turbine}$)</strong></p>
            <div class="formula-box">
              $$T_{turbine} = T_{pump} \times TR = 1,850\text{ N}\cdot\text{m} \times 1.655 \approx 3,061.75\text{ N}\cdot\text{m}$$
            </div>
            <p>
              The torque converter amplifies the engine's $1,850\text{ N}\cdot\text{m}$ into over $3,061\text{ N}\cdot\text{m}$ entering the planetary gear set.
            </p>

            <p><strong>Step 4: Compute Converter Hydrodynamic Efficiency ($\eta$)</strong></p>
            <div class="formula-box">
              $$\eta = TR \times SR = 1.655 \times 0.40 = 0.662 \quad (66.2\%)$$
            </div>

            <p><strong>Step 5: Determine Heat Rejection Rate to ATF Oil Cooler</strong></p>
            <div class="formula-box">
              $$P_{in} = \frac{1,850\text{ N}\cdot\text{m} \times 1,900\text{ RPM}}{9548.8} = \frac{3,515,000}{9548.8} \approx 368.11\text{ kW} \quad (\approx 493.6\text{ HP})$$
              $$P_{heat} = P_{in} \times (1 - \eta) = 368.11\text{ kW} \times (1 - 0.662) = 368.11 \times 0.338 \approx 124.42\text{ kW}$$
            </div>
            <p>
              <strong>Engineering Sizing Insight:</strong> The vehicle transmission oil cooler must reject $124.4\text{ kW}$ (approx. $424,500\text{ BTU/hr}$) of continuous waste heat to prevent oil oxidation, thermal breakdown of ATF friction modifiers, and converter seal degradation during heavy grade ascent.
            </p>
          </div>

          <h2>Torque Converter Clutch (TCC) Lockup and Electronic Slip Modulation</h2>
          <p>
            To eliminate the continuous $5\% \text{ to } 12\%$ hydrodynamic slip and parasitic fuel consumption associated with fluid couplings during highway cruising, modern automatic transmissions incorporate an electronically modulated <strong>Torque Converter Clutch (TCC)</strong>. Positioned between the turbine hub and the front converter cover, this annular wet friction clutch disc locks the turbine directly to the engine cover:
          </p>
          <ul>
            <li><strong>Full Lockup Mode:</strong> Hydraulic line pressure locks the friction disc against the converter cover ($SR = 1.0, TR = 1.0$), establishing a direct 1:1 mechanical drive line. Hydraulic fluid shear ceases entirely, yielding 100% transmission efficiency and zero fluid heat dissipation.</li>
            <li><strong>Continuous Slip Regulation (ECCC):</strong> In modern 8-, 9-, and 10-speed transmissions, transmission control modules (TCM) utilize pulse-width modulated (PWM) hydraulic solenoids to maintain a controlled micro-slip of $20 \text{ to } 50\text{ RPM}$ during low-speed acceleration. This slight slip isolates low-frequency firing torsional vibrations produced by downsized 3- and 4-cylinder engines while recovering more than $90\%$ of open-converter efficiency losses.</li>
          </ul>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Driveline Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="torque-to-hp-calculator.html">Torque to Horsepower</a></li>
            <li><a href="power-to-torque-calculator.html">Power to Torque Calculator</a></li>
            <li><a href="gear-ratio-calculator.html">Gear Ratio &amp; Speed</a></li>
            <li><a href="torque-calculator.html">Torque &amp; Shaft Power</a></li>
            <li><a href="flywheel-energy-calculator.html">Flywheel Energy Storage</a></li>
            <li><a href="shaft-diameter-calculator.html">Shaft Diameter Sizing</a></li>
          </ul>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container footer-content">
      <div class="footer-col">
        <h4>CalcHub</h4>
        <p>High-precision professional engineering and scientific calculation engines.</p>
      </div>
      <div class="footer-col">
        <h4>Directories</h4>
        <ul class="footer-links">
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="mechanical.html">Mechanical Engineering</a></li>
          <li><a href="engineering.html">Civil &amp; Structural</a></li>
          <li><a href="sitemap.xml">XML Sitemap</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom text-center">
      <p>&copy; 2026 CalcHub. Standard Engineering Reference Systems.</p>
    </div>
  </footer>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const calcBtn = document.getElementById('calcTcBtn');
      const resetBtn = document.getElementById('resetTcBtn');
      const resultBox = document.getElementById('tcResultBox');

      function calculateTC() {
        const t_pump = parseFloat(document.getElementById('engineTorque').value);
        const n_pump = parseFloat(document.getElementById('engineRpm').value);
        let n_turb = parseFloat(document.getElementById('turbineRpm').value);
        const tr_stall = parseFloat(document.getElementById('stallRatioPreset').value);
        const isLocked = document.getElementById('lockupActive').value === 'yes';

        if (isNaN(t_pump) || t_pump <= 0 || isNaN(n_pump) || n_pump <= 0 || isNaN(n_turb) || n_turb < 0) {
          alert('Please enter valid positive values for torque and rotational speeds.');
          return;
        }

        if (isLocked) {
          n_turb = n_pump;
          document.getElementById('turbineRpm').value = n_pump;
        }

        // Speed ratio SR = Nt / Np
        let sr = Math.min(1.0, n_turb / n_pump);

        // Torque ratio calculation
        let tr = 1.0;
        let eff = 0;
        let status = '';

        if (isLocked) {
          tr = 1.0;
          sr = 1.0;
          eff = 1.0;
          status = 'Mechanical Lockup Clutch Engaged (100% Efficiency, Zero Slip)';
        } else if (sr === 0) {
          tr = tr_stall;
          eff = 0.0;
          status = 'Full Stall Condition (Max Multiplication, 100% Heat Generation)';
        } else if (sr < 0.88) {
          // In torque multiplication zone
          tr = tr_stall - ((tr_stall - 1.0) / 0.88) * sr;
          eff = tr * sr;
          status = 'Torque Multiplication Zone (Active Stator Fluid Redirection)';
        } else {
          // Coupling zone
          tr = 1.0;
          eff = sr;
          status = 'Fluid Coupling Mode (Stator Freewheeling on Sprag Clutch)';
        }

        // Output turbine torque
        const t_turb = t_pump * tr;

        // Capacity K-Factor: K = N / sqrt(T)
        const kFactor = n_pump / Math.sqrt(t_pump);

        // Input power & Heat dissipation
        const p_in_kW = (t_pump * n_pump) / 9548.8;
        const p_heat_kW = p_in_kW * (1.0 - eff);

        // Display results
        document.getElementById('resTurbineTorque').textContent = t_turb.toFixed(1) + ' N·m (' + (t_turb * 0.737562).toFixed(1) + ' lb·ft)';
        document.getElementById('resTorqueRatio').textContent = tr.toFixed(2) + ' : 1';
        document.getElementById('resSpeedRatio').textContent = sr.toFixed(3);
        document.getElementById('resEfficiency').textContent = (eff * 100.0).toFixed(1) + ' %';
        document.getElementById('resKFactor').textContent = kFactor.toFixed(1) + ' (RPM/√N·m)';
        document.getElementById('resHeatPower').textContent = p_heat_kW.toFixed(2) + ' kW (' + (p_heat_kW * 1.34102).toFixed(1) + ' HP)';
        document.getElementById('resRegimeStatus').textContent = status;

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculateTC);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
      });

      calculateTC();
    });
  </script>
</body>
</html>
"""

TOOL_8_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Torque to HP Calculator | Horsepower, Kilowatts &amp; BMEP</title>
  <meta name="description" content="Convert torque (N·m, lb·ft, in·lb) and RPM to horsepower (HP / bhp) and kilowatts (kW). Includes brake mean effective pressure (BMEP) engine sizing.">
  <link rel="canonical" href="https://calchub.cloud/torque-to-hp-calculator.html">
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
        "name": "Torque to HP Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Rotational mechanical power converter calculating Horsepower HP = (Torque * RPM) / 5252, Kilowatts P = (T * RPM) / 9548.8, and 4-stroke engine BMEP.",
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
            "name": "What is the formula to calculate horsepower from torque and RPM?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In US imperial units: HP = (Torque [lb-ft] * RPM) / 5252.113. If torque is given in pound-inches: HP = (Torque [in-lb] * RPM) / 63,025. In metric SI units: Power [kW] = (Torque [N-m] * RPM) / 9548.8, which converts to mechanical HP as HP = kW * 1.34102."
            }
          },
          {
            "@type": "Question",
            "name": "Why do horsepower and torque curves always cross at 5252 RPM?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "One mechanical horsepower is defined as 33,000 foot-pounds of work per minute. Dividing 33,000 by 2 * pi radians per revolution yields exactly 5,252.113. When an engine rotates at 5,252 RPM, RPM and the 5252 constant cancel out completely, making horsepower and torque (in lb-ft) numerically equal on any dyno graph."
            }
          },
          {
            "@type": "Question",
            "name": "What is Brake Mean Effective Pressure (BMEP)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "BMEP is the theoretical average cylinder pressure exerted on pistons during the power stroke that produces the measured brake torque: BMEP [bar] = (4 * pi * Torque [N-m]) / (Displacement [Liters] * 100). BMEP serves as an engine-independent benchmark of volumetric efficiency and combustion design."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between mechanical HP, metric HP (PS), and electrical kW?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "1 mechanical horsepower (Imperial HP / bhp) = 745.69987 Watts. 1 metric horsepower (PS / cv / pk) is based on 75 kg-m/s = 735.49875 Watts (approximately 0.9863 Imperial HP). 1 Kilowatt (kW) = 1,000 Watts = 1.34102 Imperial HP = 1.35962 Metric PS."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="mechanical">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">
        <span class="logo-icon">&pi;</span>
        <span class="logo-text">Calc<strong>Hub</strong></span>
      </a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="engineering.html">Engineering</a>
        <a href="mechanical.html" class="active">Mechanical</a>
        <a href="solar-energy.html">Solar</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo; 
      <a href="engineering.html">Engineering</a> &rsaquo; 
      <a href="mechanical.html">Mechanical</a> &rsaquo; 
      <span>Torque to HP Calculator</span>
    </nav>

    <header class="calc-header">
      <div class="calc-badge">Engine Dynamics &amp; Dyno Sizing</div>
      <h1 class="calc-title">Torque to HP Calculator</h1>
      <p class="calc-tagline">Convert rotational torque and RPM to brake horsepower (HP / bhp), metric PS, kilowatts (kW), and evaluate engine brake mean effective pressure (BMEP).</p>
    </header>

    <div class="calc-grid">
      <div class="calc-main">
        <div class="tool-card">
          <form id="t2hpForm">
            <div class="form-row">
              <div class="form-group">
                <label for="torqueUnit">Torque Input Unit</label>
                <select id="torqueUnit" class="form-control">
                  <option value="ftlb" selected>Foot-Pounds (lb&middot;ft / ft&middot;lbf)</option>
                  <option value="nm">Newton-Meters (N&middot;m)</option>
                  <option value="inlb">Inch-Pounds (in&middot;lb)</option>
                  <option value="kgm">Kilogram-Meters (kg&middot;m)</option>
                </select>
              </div>
              <div class="form-group">
                <label for="torqueValue">Torque Magnitude ($T$)</label>
                <input type="number" id="torqueValue" class="form-control" value="380" min="0.01" step="any" required>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="engineSpeed">Rotational Speed ($N$ in RPM)</label>
                <input type="number" id="engineSpeed" class="form-control" value="5500" min="1" step="any" required>
                <span class="hint">Crossover speed where HP = Torque (lb-ft) is exactly 5,252 RPM</span>
              </div>
              <div class="form-group">
                <label for="engineDisplacement">Engine Displacement (Optional for BMEP)</label>
                <div style="display: flex; gap: 0.5rem;">
                  <input type="number" id="engineDisplacement" class="form-control" value="3.0" min="0" step="any">
                  <select id="dispUnit" class="form-control" style="width: 100px;">
                    <option value="l" selected>Liters</option>
                    <option value="ci">CID (in³)</option>
                    <option value="cc">cc (cm³)</option>
                  </select>
                </div>
                <span class="hint">4-stroke engine displacement for BMEP analysis</span>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcHpBtn">Convert Torque to Horsepower</button>
              <button type="reset" class="btn btn-secondary" id="resetHpBtn">Reset</button>
            </div>
          </form>

          <div id="t2hpResultBox" class="results-container" style="display: none; margin-top: 1.5rem;">
            <h3>Calculated Power &amp; Performance Output</h3>
            <div class="results-grid">
              <div class="result-tile highlight">
                <span class="result-label">Brake Horsepower (HP / bhp)</span>
                <span class="result-value" id="resHP">-- HP</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Metric Horsepower (PS / cv)</span>
                <span class="result-value" id="resPS">-- PS</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Mechanical Power in Kilowatts</span>
                <span class="result-value" id="resKW">-- kW</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Standard Torque in Newton-Meters</span>
                <span class="result-value" id="resNm">-- N·m</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Standard Torque in Foot-Pounds</span>
                <span class="result-value" id="resFtLb">-- lb·ft</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Brake Mean Effective Pressure (BMEP)</span>
                <span class="result-value" id="resBMEP">-- bar / psi</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Specific Power Density</span>
                <span class="result-value" id="resPowerDensity">-- HP/L</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Physics of Rotary Power: Torque vs. Horsepower</h2>
          <p>
            In internal combustion engine dynamometry, electric motor testing, and vehicular performance analysis, the relationship between <strong>torque</strong> and <strong>horsepower</strong> is frequently misunderstood. Automotive enthusiasts often quote the aphorism: <em>"Torque is how hard you hit the wall; horsepower is how fast you hit the wall."</em> While evocative, the physical truth is grounded in classical Newtonian mechanics:
          </p>
          <ul>
            <li><strong>Torque ($T$):</strong> A static or dynamic twisting moment (rotational force vector cross-product $\vec{\tau} = \vec{r} \times \vec{F}$), measured in foot-pounds ($\text{lb}\cdot\text{ft}$) or Newton-meters ($\text{N}\cdot\text{m}$). Torque describes the engine's instantaneous capacity to perform work.</li>
            <li><strong>Horsepower ($HP$ or $P$):</strong> The time rate of doing rotational work ($P = \frac{dW}{dt} = T \cdot \omega$). Power depends simultaneously on torque and how many times per second that twisting moment is repeated (rotational velocity).</li>
          </ul>
          <p>
            On a chassis or engine dynamometer, power is never measured directly. The dyno absorption brake measures instantaneous reaction torque and shaft RPM; horsepower is strictly a <strong>calculated mathematical derivative</strong> of those two measured physical quantities.
          </p>

          <h2>The Derivation of the 5252 Imperial Constant</h2>
          <p>
            In the 18th century, Scottish engineer James Watt sought to market his new condensing steam engines to Cornish coal mine operators who used draught pit ponies to haul water buckets from mine shafts. To establish an equivalence, Watt conducted experiments with brewery dray horses turning an $8\text{-foot}$ radius capstan. Watt observed that an average draft horse could exert a steady pulling force of $180\text{ pounds}$ while walking a $24\text{-foot}$ circumference track $2.4\text{ times per minute}$.
          </p>
          <p>
            Calculating the mechanical work performed:
          </p>
          <div class="formula-box">
            $$\text{Work per minute} = 180\text{ lbf} \times (2.4 \times 2\pi \times 12\text{ ft}) \approx 32,572\text{ ft}\cdot\text{lbf/min}$$
          </div>
          <p>
            Watt rounded this figure upward by approximately 1.3% to establish the legendary engineering benchmark:
          </p>
          <div class="formula-box">
            $$1\text{ Horsepower} = 33,000\text{ foot-pounds of work per minute} = 550\text{ ft}\cdot\text{lbf/second}$$
          </div>
          <p>
            When rotational speed is expressed in revolutions per minute ($N$ in $\text{RPM}$), each revolution sweeps through an angular displacement of $2\pi$ radians. The linear work distance traveled per minute at radius $r$ is $2\pi \cdot r \cdot N$. Substituting this into the horsepower definition:
          </p>
          <div class="formula-box">
            $$HP = \frac{\text{Force} \times \text{Distance per minute}}{33,000} = \frac{F \times (2\pi \cdot r \cdot N)}{33,000} = \frac{(F \cdot r) \times 2\pi \cdot N}{33,000}$$
          </div>
          <p>
            Recognizing that $F \cdot r = \text{Torque } (T \text{ in lb}\cdot\text{ft})$:
          </p>
          <div class="formula-box">
            $$HP = \frac{T \times 2\pi \times N}{33,000} = \frac{T \times N}{\frac{33,000}{2\pi}} = \frac{T (\text{lb}\cdot\text{ft}) \times N (\text{RPM})}{5252.113}$$
          </div>
          <p>
            <strong>The 5252 Crossover Phenomenon:</strong> Whenever an engine operates at exactly $5252.113\text{ RPM}$, the speed term in the numerator cancels the denominator constant perfectly ($5252 / 5252 = 1.0$), making numerical horsepower exactly equal to torque in pound-feet ($HP = T$). Below $5252\text{ RPM}$, torque in lb-ft is always numerically greater than horsepower; above $5252\text{ RPM}$, horsepower is always numerically greater than torque.
          </p>

          <h2>Metric SI Formulation (Kilowatts &amp; Newton-Meters)</h2>
          <p>
            In the International System of Units (SI), mechanical power is quantified in Watts ($\text{W}$) or Kilowatts ($\text{kW}$), where $1\text{ Watt} = 1\text{ Joule/second} = 1\text{ N}\cdot\text{m/s}$. Given torque $T$ in $\text{N}\cdot\text{m}$ and speed $N$ in $\text{RPM}$:
          </p>
          <div class="formula-box">
            $$P (\text{kW}) = \frac{T (\text{N}\cdot\text{m}) \times \omega (\text{rad/s})}{1000} = \frac{T \times \left(\frac{2\pi \cdot N}{60}\right)}{1000} = \frac{T (\text{N}\cdot\text{m}) \times N (\text{RPM})}{9548.8}$$
          </div>
          <p>
            To convert between metric Kilowatts and mechanical Imperial Horsepower:
          </p>
          <div class="formula-box">
            $$HP = P (\text{kW}) \times 1.341022, \quad P (\text{kW}) = HP \times 0.74569987$$
            $$1\text{ Metric PS (Pferdest&auml;rke)} = P (\text{kW}) \times 1.35962 = 0.98632\text{ Imperial HP}$$
          </div>

          <h2>Brake Mean Effective Pressure (BMEP) as an Engine Benchmark</h2>
          <p>
            Comparing raw horsepower or torque between an $8.0\text{-liter}$ heavy truck V8 and a $2.0\text{-liter}$ turbocharged inline-4 gives little insight into combustion efficiency. Automotive engine developers utilize <strong>Brake Mean Effective Pressure (BMEP)</strong>&mdash;a theoretical constant pressure that, if applied uniformly to each piston throughout the power expansion stroke, would produce the measured brake torque output:
          </p>
          <div class="formula-box">
            $$\text{BMEP (bar)} = \frac{4\pi \cdot T (\text{N}\cdot\text{m})}{V_d (\text{Liters}) \times 100} \approx \frac{0.12566 \cdot T (\text{N}\cdot\text{m})}{V_d (\text{Liters})}$$
          </div>
          <p>
            Where $V_d$ is total engine displacement in liters. Representative BMEP ranges across internal combustion architectures include:
          </p>
          <ul>
            <li>Naturally Aspirated 4-Stroke Gasoline: $9.0\text{ to } 12.0\text{ bar}$ ($130\text{ to } 175\text{ psi}$)</li>
            <li>High-Performance Naturally Aspirated (BMW M, Porsche GT3): $13.0\text{ to } 15.0\text{ bar}$ ($190\text{ to } 218\text{ psi}$)</li>
            <li>Production Turbocharged Gasoline: $16.0\text{ to } 24.0\text{ bar}$ ($230\text{ to } 350\text{ psi}$)</li>
            <li>Heavy-Duty Commercial Turbo Diesel: $18.0\text{ to } 26.0\text{ bar}$ ($260\text{ to } 375\text{ psi}$)</li>
            <li>Formula 1 Hybrid Turbo V6: $> 30.0\text{ bar}$ ($> 435\text{ psi}$)</li>
          </ul>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: High-Performance Turbocharged Sports Sedan Dyno Run</h3>
            <p><strong>Design Scenario:</strong> A $3.0\text{-liter}$ turbocharged inline-6 performance engine is evaluated on an all-wheel-drive hub chassis dynamometer. At peak power engine speed of $N = 6,200\text{ RPM}$, the dynamometer measures a wheel torque output of $T = 425\text{ lb}\cdot\text{ft}$ ($576.22\text{ N}\cdot\text{m}$). Calculate the brake horsepower, metric horsepower (PS), mechanical kilowatts, and evaluate the Brake Mean Effective Pressure (BMEP) to verify combustion efficiency.</p>
            
            <p><strong>Step 1: Calculate Brake Horsepower (HP)</strong></p>
            <div class="formula-box">
              $$HP = \frac{425\text{ lb}\cdot\text{ft} \times 6,200\text{ RPM}}{5252.113} = \frac{2,635,000}{5252.113} \approx 501.70\text{ HP}$$
            </div>
            <p>
              Because operating speed ($6,200\text{ RPM}$) is above the $5252$ crossover point, horsepower ($501.7\text{ HP}$) is numerically higher than torque ($425\text{ lb}\cdot\text{ft}$).
            </p>

            <p><strong>Step 2: Convert to Kilowatts and Metric PS</strong></p>
            <div class="formula-box">
              $$P (\text{kW}) = \frac{501.70\text{ HP}}{1.341022} = 374.12\text{ kW}$$
              $$\text{Metric PS} = 374.12\text{ kW} \times 1.35962 \approx 508.66\text{ PS}$$
            </div>

            <p><strong>Step 3: Calculate Brake Mean Effective Pressure (BMEP)</strong></p>
            <div class="formula-box">
              $$\text{BMEP} = \frac{4\pi \times 576.22\text{ N}\cdot\text{m}}{3.0\text{ Liters} \times 100} = \frac{7,241.0}{300} = 24.14\text{ bar} \quad (\approx 350.1\text{ psi})$$
            </div>

            <p><strong>Step 4: Determine Specific Power Output per Liter</strong></p>
            <div class="formula-box">
              $$\text{Specific Output} = \frac{501.70\text{ HP}}{3.0\text{ L}} = 167.23\text{ HP/Liter}$$
            </div>
            <p>
              <strong>Engineering Conclusion:</strong> Operating at $24.14\text{ bar}$ BMEP and $167.2\text{ HP/Liter}$ confirms that the engine's forced-induction turbochargers and variable valve timing are delivering exceptional volumetric efficiency and combustion chamber peak cylinder pressures without encountering pre-ignition knock.
            </p>
          </div>

          <h2>Electric Motor vs. Internal Combustion Torque-Power Envelopes</h2>
          <p>
            When transitioning between internal combustion engines (ICE) and electric vehicle (EV) powertrains, engineers must account for fundamentally divergent torque-speed characteristics:
          </p>
          <ul>
            <li><strong>Internal Combustion Engines:</strong> Produce zero torque at 0 RPM, requiring a friction clutch or slipping torque converter to launch. Torque rises to a mid-RPM peak before breathing limitations cause it to fall, while horsepower continues rising toward redline. Multi-speed gearboxes (6 to 10 ratios) are mandatory to keep the engine operating near its narrow power peak.</li>
            <li><strong>Electric Traction Motors (PMSM / AC Induction):</strong> Develop maximum rated torque instantly at 0 RPM. From 0 RPM up to <strong>Base Speed</strong>, the motor operates in the <em>Constant Torque Region</em> where power scales linearly ($P \propto N$). Above base speed, the inverter clamps voltage and enters the <em>Field Weakening (Constant Power) Region</em> where available torque falls inversely with speed ($T \propto 1/N$) while nameplate horsepower remains constant. This wide constant-power bandwidth enables single-speed reduction transmissions with extreme launch acceleration and smooth high-speed cruising.</li>
          </ul>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Driveline &amp; Motor Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="power-to-torque-calculator.html">Power to Torque Calculator</a></li>
            <li><a href="torque-converter.html">Torque Converter Calculator</a></li>
            <li><a href="torque-calculator.html">Torque &amp; Shaft Power</a></li>
            <li><a href="gear-ratio-calculator.html">Gear Ratio &amp; Speed</a></li>
            <li><a href="flywheel-energy-calculator.html">Flywheel Energy Storage</a></li>
            <li><a href="shaft-diameter-calculator.html">Shaft Diameter Sizing</a></li>
          </ul>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container footer-content">
      <div class="footer-col">
        <h4>CalcHub</h4>
        <p>High-precision professional engineering and scientific calculation engines.</p>
      </div>
      <div class="footer-col">
        <h4>Directories</h4>
        <ul class="footer-links">
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="mechanical.html">Mechanical Engineering</a></li>
          <li><a href="engineering.html">Civil &amp; Structural</a></li>
          <li><a href="sitemap.xml">XML Sitemap</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom text-center">
      <p>&copy; 2026 CalcHub. Standard Engineering Reference Systems.</p>
    </div>
  </footer>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const calcBtn = document.getElementById('calcHpBtn');
      const resetBtn = document.getElementById('resetHpBtn');
      const resultBox = document.getElementById('t2hpResultBox');

      function calculateHP() {
        const tUnit = document.getElementById('torqueUnit').value;
        const tVal = parseFloat(document.getElementById('torqueValue').value);
        const rpm = parseFloat(document.getElementById('engineSpeed').value);
        const dispVal = parseFloat(document.getElementById('engineDisplacement').value) || 0;
        const dispU = document.getElementById('dispUnit').value;

        if (isNaN(tVal) || tVal <= 0 || isNaN(rpm) || rpm <= 0) {
          alert('Please enter valid positive values for torque and RPM.');
          return;
        }

        // Convert torque to lb-ft and N-m
        let t_ftlb = 0;
        let t_nm = 0;

        if (tUnit === 'ftlb') {
          t_ftlb = tVal;
          t_nm = tVal * 1.3558179483314;
        } else if (tUnit === 'nm') {
          t_nm = tVal;
          t_ftlb = tVal / 1.3558179483314;
        } else if (tUnit === 'inlb') {
          t_ftlb = tVal / 12.0;
          t_nm = t_ftlb * 1.3558179483314;
        } else if (tUnit === 'kgm') {
          t_nm = tVal * 9.80665;
          t_ftlb = t_nm / 1.3558179483314;
        }

        // Horsepower HP = (Torque_ftlb * RPM) / 5252.113
        const hp = (t_ftlb * rpm) / 5252.113;
        // Kilowatts kW = (Torque_nm * RPM) / 9548.8
        const kw = (t_nm * rpm) / 9548.8;
        // Metric PS
        const ps = kw * 1.35962;

        // BMEP calculation
        let bmep_bar = 0;
        let bmep_psi = 0;
        let powerDensity = 0;

        if (dispVal > 0) {
          let dispLiters = dispVal;
          if (dispU === 'ci') dispLiters = dispVal * 0.0163871;
          else if (dispU === 'cc') dispLiters = dispVal / 1000.0;

          if (dispLiters > 0) {
            bmep_bar = (4.0 * Math.PI * t_nm) / (dispLiters * 100.0);
            bmep_psi = bmep_bar * 14.5038;
            powerDensity = hp / dispLiters;
          }
        }

        // Render outputs
        document.getElementById('resHP').textContent = hp.toFixed(1) + ' HP (' + hp.toLocaleString('en-US', {maximumFractionDigits: 1}) + ' bhp)';
        document.getElementById('resPS').textContent = ps.toFixed(1) + ' PS (cv)';
        document.getElementById('resKW').textContent = kw.toFixed(1) + ' kW';
        document.getElementById('resNm').textContent = t_nm.toFixed(1) + ' N·m';
        document.getElementById('resFtLb').textContent = t_ftlb.toFixed(1) + ' lb·ft';
        document.getElementById('resBMEP').textContent = bmep_bar > 0 ? (bmep_bar.toFixed(2) + ' bar (' + bmep_psi.toFixed(1) + ' psi)') : 'N/A (Specify Displacement)';
        document.getElementById('resPowerDensity').textContent = powerDensity > 0 ? (powerDensity.toFixed(1) + ' HP/L') : 'N/A';

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculateHP);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
      });

      calculateHP();
    });
  </script>
</body>
</html>
"""

def main():
    with open("torque-converter.html", "w", encoding="utf-8") as f:
        f.write(TOOL_7_HTML.strip() + "\n")
    print("[PASS] torque-converter.html generated successfully!")

    with open("torque-to-hp-calculator.html", "w", encoding="utf-8") as f:
        f.write(TOOL_8_HTML.strip() + "\n")
    print("[PASS] torque-to-hp-calculator.html generated successfully!")

if __name__ == "__main__":
    main()
