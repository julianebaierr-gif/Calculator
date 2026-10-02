# -*- coding: utf-8 -*-
"""
Script to generate Batch 10 Part 3 tools:
5. power-to-torque-calculator.html
6. psychrometric-calculator.html
"""
import os

TOOL_5_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Power to Torque Calculator | Motor & Shaft Torsional Analysis</title>
  <meta name="description" content="Calculate shaft torque from power and rotational speed (RPM) in N·m, lb·ft, and in·lb. Includes gear reduction ratio multiplication and motor shaft shear sizing.">
  <link rel="canonical" href="https://calchub.cloud/power-to-torque-calculator.html">
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
        "name": "Power to Torque Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Mechanical driveline torque sizing engine calculating rotary torque from electric motor or engine power and shaft RPM per DIN 743 and AGMA standards.",
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
            "name": "What is the relationship between power, rotational speed, and torque?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Rotational mechanical power is the mathematical product of angular velocity and torque: P = omega * T = (2 * pi * N / 60) * T. In metric SI units: T [N*m] = (9548.8 * P [kW]) / N [RPM]. In imperial mechanical units: T [lb*ft] = (5252.11 * P [HP]) / N [RPM]."
            }
          },
          {
            "@type": "Question",
            "name": "Why is 5252 the crossover RPM between horsepower and torque?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In the imperial formula HP = (Torque [lb-ft] * RPM) / 5252.11, the constant 5252 originates from 33,000 ft-lb/min (James Watt's definition of 1 horsepower) divided by 2 * pi radians per revolution (33000 / 6.283185 = 5252.113). Consequently, whenever an engine runs at exactly 5252 RPM, its horsepower and torque in lb-ft are numerically identical."
            }
          },
          {
            "@type": "Question",
            "name": "How does a speed reducer or gearbox affect output torque?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A gearbox reduces rotational speed while multiplying torque by the reduction gear ratio (i = N_in / N_out). Taking mechanical gearmesh and bearing friction into account: T_out = T_in * i * eta_gear, where eta_gear typically ranges from 94% to 98% for multi-stage helical gearsets and 60% to 88% for worm gear drives."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between rated motor torque and breakdown torque?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Rated full-load torque is the continuous torsional moment an electric motor safely produces at rated power and speed without overheating (Class F insulation limits). Breakdown torque (pull-out torque per NEMA MG-1) is the maximum transient peak torque the motor can develop (typically 200% to 300% of rated torque) before stalling."
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
      <span>Power to Torque Calculator</span>
    </nav>

    <header class="calc-header">
      <div class="calc-badge">Driveline &amp; Motor Mechanics</div>
      <h1 class="calc-title">Power to Torque Calculator</h1>
      <p class="calc-tagline">Calculate drive shaft torque, gearbox output torque multiplication, and solid shaft minimum diameter based on power input and rotational velocity.</p>
    </header>

    <div class="calc-grid">
      <div class="calc-main">
        <div class="tool-card">
          <form id="p2tForm">
            <div class="form-row">
              <div class="form-group">
                <label for="powerUnit">Input Power Unit</label>
                <select id="powerUnit" class="form-control">
                  <option value="kw" selected>Kilowatts (kW)</option>
                  <option value="hp">Mechanical Horsepower (HP / bhp)</option>
                  <option value="w">Watts (W)</option>
                </select>
              </div>
              <div class="form-group">
                <label for="powerVal">Shaft Power Input</label>
                <input type="number" id="powerVal" class="form-control" value="15" min="0.001" step="any" required>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="rpmVal">Rotational Speed (RPM)</label>
                <input type="number" id="rpmVal" class="form-control" value="1450" min="0.1" step="any" required>
                <span class="hint">Standard 4-pole induction motor: ~1450 RPM (50Hz) or ~1750 RPM (60Hz)</span>
              </div>
              <div class="form-group">
                <label for="serviceFactor">Application Service Factor ($K_a$)</label>
                <select id="serviceFactor" class="form-control">
                  <option value="1.0">1.00 - Uniform continuous load (fans, centrifugal pumps)</option>
                  <option value="1.25" selected>1.25 - Moderate shock (conveyors, rotary compressors)</option>
                  <option value="1.5">1.50 - Heavy shock (reciprocating pumps, crushers, mills)</option>
                  <option value="2.0">2.00 - Extreme shock (presses, shears, vibratory screens)</option>
                </select>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="gearRatio">Gear Reduction Ratio ($i = N_{in} / N_{out}$)</label>
                <input type="number" id="gearRatio" class="form-control" value="1.0" min="0.01" step="any">
                <span class="hint">Set to 1.0 for direct direct-drive coupling</span>
              </div>
              <div class="form-group">
                <label for="gearEff">Gearbox Mechanical Efficiency (%)</label>
                <input type="number" id="gearEff" class="form-control" value="96" min="10" max="100" step="0.5">
                <span class="hint">Helical ~96-98%, Bevel ~94-96%, Worm ~65-85%</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="shearAllowable">Allowable Shaft Shear Stress ($\tau_{allow}$ in MPa)</label>
                <input type="number" id="shearAllowable" class="form-control" value="50" min="1" step="1">
                <span class="hint">AISI 1045 steel ~45-55 MPa; 4140 quenched &amp; tempered ~70-90 MPa</span>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcBtn">Compute Torque &amp; Driveline Parameters</button>
              <button type="reset" class="btn btn-secondary" id="resetBtn">Reset</button>
            </div>
          </form>

          <div id="p2tResultBox" class="results-container" style="display: none; margin-top: 1.5rem;">
            <h3>Calculated Torsional &amp; Driveline Sizing</h3>
            <div class="results-grid">
              <div class="result-tile highlight">
                <span class="result-label">Motor Shaft Nominal Torque</span>
                <span class="result-value" id="resTorqueNm">-- N·m</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Nominal Torque (Imperial)</span>
                <span class="result-value" id="resTorqueFtLb">-- lb·ft</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Gearbox Output Torque</span>
                <span class="result-value" id="resOutputTorque">-- N·m</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Output Speed (After Gearing)</span>
                <span class="result-value" id="resOutputRpm">-- RPM</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Design Torque ($T_{design} = T \times K_a$)</span>
                <span class="result-value" id="resDesignTorque">-- N·m</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Min. Solid Shaft Diameter ($d_{min}$)</span>
                <span class="result-value" id="resShaftDiam">-- mm</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Fundamentals of Power and Torque in Rotating Machinery</h2>
          <p>
            In mechanical drive systems, understanding the physical distinction between mechanical <strong>power</strong> and <strong>torque</strong> is the cornerstone of machine design. Rotational torque ($\tau$ or $T$) represents the static or dynamic twisting moment exerted around a rotational axis. Expressed in Newton-meters ($\text{N}\cdot\text{m}$) or pound-feet ($\text{lb}\cdot\text{ft}$), torque defines the rotational force capacity available to overcome friction, inertia, and mechanical resistance. Power ($P$), conversely, represents the time rate at which rotational work is performed, quantified in kilowatts ($\text{kW}$) or horsepower ($\text{HP}$).
          </p>
          <p>
            A high-power prime mover can produce high rotational velocity with modest torque (such as a 20,000 RPM aircraft turbine), or immense torque at low rotational velocity (such as a 12 RPM bucket-wheel excavator drum driven by the identical power input). The mathematical bridge between twisting moment and work rate is angular velocity ($\omega$ in radians per second):
          </p>
          <div class="formula-box">
            $$P = T \cdot \omega = T \cdot \left(\frac{2\pi \cdot N}{60}\right)$$
          </div>
          <p>
            Where $N$ is the shaft rotational speed in revolutions per minute ($\text{RPM}$). When rearranged to isolate torque as a function of power and operating speed, the fundamental governing relationships for both SI metric and US customary units emerge.
          </p>

          <h2>Governing Equations: Metric SI and Imperial Conversions</h2>
          <p>
            Depending on international industry practice and engineering standards (DIN, ISO, AGMA, or ANSI), driveline calculations apply specific conversion coefficients derived directly from mechanical fundamentals:
          </p>
          
          <h3>1. Metric SI Formulation</h3>
          <p>
            With power $P$ expressed in kilowatts ($\text{kW}$) and rotational speed $N$ in $\text{RPM}$, dividing the conversion factor $60 / (2\pi \times 1000)$ yields the classic metric constant $9548.8$:
          </p>
          <div class="formula-box">
            $$T (\text{N}\cdot\text{m}) = \frac{P (\text{kW}) \times 9548.8}{N (\text{RPM})} = \frac{P (\text{W})}{\omega (\text{rad/s})}$$
          </div>
          
          <h3>2. US Customary (Imperial) Horsepower Formulation</h3>
          <p>
            In US heavy industry, prime movers are rated in brake horsepower ($\text{HP}$ or $\text{bhp}$), where $1\text{ HP} = 33,000\text{ ft}\cdot\text{lbf/min} = 550\text{ ft}\cdot\text{lbf/s}$. Dividing $33,000$ by $2\pi$ produces the ubiquitous driveline constant $5252.11$:
          </p>
          <div class="formula-box">
            $$T (\text{lb}\cdot\text{ft}) = \frac{P (\text{HP}) \times 5252.11}{N (\text{RPM})}$$
          </div>
          <p>
            If torque is required in pound-inches ($\text{in}\cdot\text{lb}$), multiplying $5252.11$ by $12\text{ in/ft}$ gives $63,025$:
          </p>
          <div class="formula-box">
            $$T (\text{in}\cdot\text{lb}) = \frac{P (\text{HP}) \times 63025}{N (\text{RPM})}$$
          </div>

          <h2>Gearbox Torque Multiplication and Transmission Efficiency</h2>
          <p>
            Electric AC induction motors are economically constructed to rotate at synchronous speeds of 3000, 1500, 1000, or 750 RPM (at 50 Hz line frequency) or 3600, 1800, 1200 RPM (at 60 Hz). Most industrial end-effectors—such as conveyor head pulleys, agitator impellers, rolling mills, and hoists—require significantly lower rotational speeds ranging from 5 to 150 RPM. A mechanical speed reducer (gearbox) steps down the rotational speed while simultaneously magnifying torque:
          </p>
          <div class="formula-box">
            $$N_{out} = \frac{N_{in}}{i}, \quad T_{out} = T_{in} \cdot i \cdot \eta_{gear}$$
          </div>
          <p>
            Where $i$ is the gear reduction ratio ($i > 1.0$) and $\eta_{gear}$ is the transmission mechanical efficiency. Because of gear sliding friction, bearing churning, and lubricating oil shear losses, no speed reducer operates without parasitic loss. The table below illustrates typical efficiency bands across standard gear drive architectures:
          </p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Gear Reducer Architecture</th>
                <th>Standard Single-Stage Ratio ($i$)</th>
                <th>Mechanical Efficiency ($\eta$)</th>
                <th>Typical Industrial Applications</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Spur / Helical In-Line</td>
                <td>1.5:1 to 6.3:1</td>
                <td>97.0% &ndash; 98.5%</td>
                <td>Pumps, blowers, machine tools, general industrial drives</td>
              </tr>
              <tr>
                <td>Bevel-Helical (Right-Angle)</td>
                <td>3.15:1 to 10:1</td>
                <td>95.0% &ndash; 97.0%</td>
                <td>Heavy conveyors, bucket elevators, paper mill rollers</td>
              </tr>
              <tr>
                <td>Planetary (Epicyclic) Gearhead</td>
                <td>3:1 to 10:1 (per stage)</td>
                <td>94.0% &ndash; 97.0%</td>
                <td>Robotics, CNC servo drives, wheel drives, wind turbines</td>
              </tr>
              <tr>
                <td>Worm Gear Reducer (Single)</td>
                <td>5:1 to 70:1</td>
                <td>60.0% &ndash; 88.0%</td>
                <td>Self-locking hoists, winches, packaging machines, dampers</td>
              </tr>
              <tr>
                <td>Harmonic / Strain Wave</td>
                <td>30:1 to 160:1</td>
                <td>75.0% &ndash; 85.0%</td>
                <td>Precision robotics, aerospace gimbals, surgical manipulators</td>
              </tr>
            </tbody>
          </table>

          <h2>Application Service Factors ($K_a$) and Dynamic Peak Torques</h2>
          <p>
            Operating equipment rarely experiences steady, non-pulsating resistance. Starting shock loads, torsional vibration, product jamming, and rapid cyclical reversal impose dynamic loads far exceeding continuous nameplate ratings. International standards such as AGMA 6013 and ISO 6336 mandate applying an Application Service Factor ($K_a$) to establish the structural Design Torque ($T_{design}$):
          </p>
          <div class="formula-box">
            $$T_{design} = T_{nominal} \cdot K_a$$
          </div>
          <p>
            Selecting a service factor of $1.0$ on a positive-displacement mud pump or jaw crusher inevitably results in premature shaft fatigue failure, stripped gear teeth, or coupling shearing. For prime movers like internal combustion engines with high cyclic cylinder firing pulses, an additional engine service increment ($\Delta K_a \approx 0.25 - 0.50$) must be added.
          </p>

          <h2>Drive Shaft Torsional Shear Stress and Sizing (DIN 743 / ASME B106.1M)</h2>
          <p>
            A rotating solid circular shaft subject to pure torsional load develops maximum shear stress ($\tau_{max}$) at its outermost circumferential fibers. According to classic Saint-Venant torsional theory:
          </p>
          <div class="formula-box">
            $$\tau = \frac{T \cdot r}{J} = \frac{T \cdot (d / 2)}{\frac{\pi d^4}{32}} = \frac{16 \cdot T_{design}}{\pi \cdot d^3}$$
          </div>
          <p>
            Rearranging this equation to determine the minimum allowable solid shaft diameter ($d_{min}$) required to resist pure torsion without exceeding the allowable shear stress limit ($\tau_{allow}$):
          </p>
          <div class="formula-box">
            $$d_{min} = \sqrt[3]{\frac{16 \cdot T_{design}}{\pi \cdot \tau_{allow}}}$$
          </div>
          <p>
            For commercial medium-carbon steel shafts (such as AISI 1045 or EN8) operating with keyways (which introduce a stress concentration factor $K_t \approx 1.7$ to $2.2$), conservative engineering practice limits allowable continuous shear stress to $\tau_{allow} \approx 40 - 55\text{ MPa}$. For high-tensile alloy steels (such as AISI 4140 or 4340 Q&amp;T), allowable design shear stress may extend to $70 - 90\text{ MPa}$.
          </p>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: Overland Conveyor Drive</h3>
            <p><strong>Design Scenario:</strong> A bulk materials conveyor belt requires an electric motor drive operating continuously under moderate shock loading ($K_a = 1.35$). The selected 4-pole AC induction motor delivers $P = 45\text{ kW}$ at a nominal loaded speed of $N = 1465\text{ RPM}$. The drive uses a helical-bevel right-angle speed reducer with a gear ratio of $i = 18.5:1$ and an efficiency of $\eta_{gear} = 96\%$. Calculate motor nominal torque, gearbox output shaft torque, and the minimum diameter for an output shaft made of AISI 1045 steel ($\tau_{allow} = 45\text{ MPa}$).</p>
            
            <p><strong>Step 1: Calculate Nominal Motor Shaft Torque</strong></p>
            <div class="formula-box">
              $$T_{motor} = \frac{45\text{ kW} \times 9548.8}{1465\text{ RPM}} = 293.31\text{ N}\cdot\text{m}$$
            </div>

            <p><strong>Step 2: Calculate Output Speed and Output Shaft Torque</strong></p>
            <div class="formula-box">
              $$N_{out} = \frac{1465\text{ RPM}}{18.5} = 79.19\text{ RPM}$$
              $$T_{out} = T_{motor} \times i \times \eta_{gear} = 293.31 \times 18.5 \times 0.96 = 5,209.11\text{ N}\cdot\text{m}$$
            </div>

            <p><strong>Step 3: Determine Structural Design Torque with Service Factor</strong></p>
            <div class="formula-box">
              $$T_{design} = 5,209.11\text{ N}\cdot\text{m} \times 1.35 = 7,032.30\text{ N}\cdot\text{m} = 7,032,300\text{ N}\cdot\text{mm}$$
            </div>

            <p><strong>Step 4: Size the Solid Output Drive Shaft</strong></p>
            <div class="formula-box">
              $$d_{min} = \sqrt[3]{\frac{16 \times 7,032,300}{\pi \times 45\text{ N/mm}^2}} = \sqrt[3]{\frac{112,516,800}{141.37}} = \sqrt[3]{795,903} \approx 92.67\text{ mm}$$
            </div>
            <p>
              <strong>Engineering Conclusion:</strong> Specifying a standard commercial shaft diameter of <strong>$95\text{ mm}$</strong> or <strong>$100\text{ mm}$</strong> provides adequate torsional strength and structural rigidity, fully accounting for keyway stress concentrations and bending moments induced by the conveyor head pulley.
            </p>
          </div>

          <h2>Electric Motor Torque-Speed Characteristics &amp; VFD Considerations</h2>
          <p>
            When utilizing Variable Frequency Drives (VFDs) to govern AC induction or permanent-magnet synchronous motors (PMSM), engineers must observe two distinct operational regimes:
          </p>
          <ul>
            <li><strong>Constant Torque Region (Below Base Frequency, 0 to 50/60 Hz):</strong> As frequency and voltage scale linearly ($V/f$ ratio maintained constant), the motor core maintains saturated magnetic flux. Full rated torque ($T_{rated}$) is available continuously across the speed range, while shaft power scales linearly with speed: $P \propto N$.</li>
            <li><strong>Constant Power Region (Above Base Frequency, Field Weakening Range):</strong> To protect motor insulation against over-voltage, voltage is clamped at maximum line voltage while frequency continues to increase. Magnetic flux weakens inversely with frequency ($\Phi \propto 1/f$). As a result, available shaft torque falls rapidly: $T \propto 1/N$, while output power remains constant at nameplate capacity.</li>
          </ul>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Mechanical Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="hydraulic-pump-power-calculator.html">Hydraulic Pump Power Calculator</a></li>
            <li><a href="hydraulic-cylinder-calculator.html">Hydraulic Cylinder Sizing</a></li>
            <li><a href="pulley-rpm-calculator.html">Pulley RPM Calculator</a></li>
            <li><a href="pulley-mechanical-advantage-calculator.html">Pulley Mechanical Advantage</a></li>
            <li><a href="conveyor-belt-speed-calculator.html">Conveyor Belt Speed</a></li>
            <li><a href="flywheel-energy-calculator.html">Flywheel Energy Storage</a></li>
            <li><a href="gear-module-calculator.html">Gear Module &amp; Pitch</a></li>
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
      const calcBtn = document.getElementById('calcBtn');
      const resetBtn = document.getElementById('resetBtn');
      const resultBox = document.getElementById('p2tResultBox');

      function calculate() {
        const pUnit = document.getElementById('powerUnit').value;
        const pVal = parseFloat(document.getElementById('powerVal').value);
        const rpm = parseFloat(document.getElementById('rpmVal').value);
        const ka = parseFloat(document.getElementById('serviceFactor').value);
        const gearRatio = parseFloat(document.getElementById('gearRatio').value) || 1.0;
        const gearEffPct = parseFloat(document.getElementById('gearEff').value) || 100.0;
        const tauAllow = parseFloat(document.getElementById('shearAllowable').value) || 50.0;

        if (isNaN(pVal) || pVal <= 0 || isNaN(rpm) || rpm <= 0) {
          alert('Please enter valid positive values for power and RPM.');
          return;
        }

        // Convert power to kW and HP
        let p_kW = 0;
        let p_HP = 0;
        if (pUnit === 'kw') {
          p_kW = pVal;
          p_HP = pVal * 1.34102;
        } else if (pUnit === 'hp') {
          p_HP = pVal;
          p_kW = pVal * 0.74569987;
        } else if (pUnit === 'w') {
          p_kW = pVal / 1000;
          p_HP = p_kW * 1.34102;
        }

        // Nominal motor torque: T = (9548.8 * P_kW) / RPM
        const t_Nm = (9548.8 * p_kW) / rpm;
        const t_ftlb = (5252.11 * p_HP) / rpm;

        // Gearbox output calculations
        const eff = Math.min(1.0, Math.max(0.01, gearEffPct / 100.0));
        const outRpm = rpm / gearRatio;
        const outTorqueNm = t_Nm * gearRatio * eff;

        // Design torque considering service factor on output
        const designTorqueNm = outTorqueNm * ka;

        // Minimum solid shaft diameter: d = ( (16 * T_design_Nmm) / (pi * tau_MPa) )^(1/3)
        const t_Nmm = designTorqueNm * 1000.0;
        const d_mm = Math.cbrt((16.0 * t_Nmm) / (Math.PI * tauAllow));

        document.getElementById('resTorqueNm').textContent = t_Nm.toLocaleString('en-US', {maximumFractionDigits: 2}) + ' N·m';
        document.getElementById('resTorqueFtLb').textContent = t_ftlb.toLocaleString('en-US', {maximumFractionDigits: 2}) + ' lb·ft';
        document.getElementById('resOutputTorque').textContent = outTorqueNm.toLocaleString('en-US', {maximumFractionDigits: 2}) + ' N·m';
        document.getElementById('resOutputRpm').textContent = outRpm.toLocaleString('en-US', {maximumFractionDigits: 1}) + ' RPM';
        document.getElementById('resDesignTorque').textContent = designTorqueNm.toLocaleString('en-US', {maximumFractionDigits: 2}) + ' N·m';
        document.getElementById('resShaftDiam').textContent = d_mm.toFixed(1) + ' mm';

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculate);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
      });

      calculate();
    });
  </script>
</body>
</html>
"""

TOOL_6_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Psychrometric Calculator | Moist Air Properties &amp; HVAC Sizing</title>
  <meta name="description" content="Calculate moist air psychrometric properties per ASHRAE Fundamentals: dew point, relative humidity, humidity ratio (W), wet bulb, enthalpy (h), and specific volume.">
  <link rel="canonical" href="https://calchub.cloud/psychrometric-calculator.html">
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
        "name": "Psychrometric Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Thermodynamic moist air psychrometric calculator solving ASHRAE Fundamentals Chapter 1 formulations for humidity ratio, dew point, wet-bulb, enthalpy, and moist air density.",
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
            "name": "What is the difference between dry-bulb, wet-bulb, and dew point temperatures?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Dry-bulb temperature is the true ambient air temperature measured by a standard thermometer shielded from radiation and moisture. Wet-bulb temperature reflects the lowest temperature achievable via evaporative water cooling into ambient air at adiabatic saturation. Dew point temperature is the exact threshold to which moist air must be cooled at constant barometric pressure and moisture content for water vapor to condense into liquid."
            }
          },
          {
            "@type": "Question",
            "name": "How is the humidity ratio (specific humidity) calculated?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The humidity ratio (W) is the ratio of water vapor mass to dry air mass: W = 0.62198 * (P_w / (P_atm - P_w)), where P_w is the partial pressure of water vapor and P_atm is total barometric atmospheric pressure. The constant 0.62198 represents the molecular weight ratio of water vapor (18.015 g/mol) to dry air (28.966 g/mol)."
            }
          },
          {
            "@type": "Question",
            "name": "Why does psychrometric enthalpy matter for HVAC cooling and heating coil sizing?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Specific enthalpy (h) measures the total thermal energy (sensible heat plus latent moisture heat) contained per kilogram of dry air: h = 1.006 * T_db + W * (2501 + 1.86 * T_db) kJ/kg. The total cooling or heating coil capacity required to condition an airstream is computed directly from mass airflow times enthalpy difference: Q_total = m_air * Delta_h."
            }
          },
          {
            "@type": "Question",
            "name": "How does elevation or barometric pressure alter psychrometric properties?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "As elevation increases, atmospheric barometric pressure drops. According to Dalton's Law of partial pressures, lower barometric pressure forces water to evaporate faster, significantly elevating the saturation humidity ratio W for any given temperature. Consequently, HVAC equipment installed in high-altitude environments requires greater volumetric airflow (CFM or m^3/s) to achieve equivalent sensible cooling capacity."
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
      <span>Psychrometric Calculator</span>
    </nav>

    <header class="calc-header">
      <div class="calc-badge">Thermodynamics &amp; HVAC Sizing</div>
      <h1 class="calc-title">Psychrometric Calculator</h1>
      <p class="calc-tagline">Evaluate complete moist air state points: humidity ratio, dew point, wet-bulb temperature, enthalpy, specific volume, and air density per ASHRAE Fundamentals.</p>
    </header>

    <div class="calc-grid">
      <div class="calc-main">
        <div class="tool-card">
          <form id="psychForm">
            <div class="form-row">
              <div class="form-group">
                <label for="tempDb">Dry-Bulb Temperature ($T_{db}$)</label>
                <div style="display: flex; gap: 0.5rem;">
                  <input type="number" id="tempDb" class="form-control" value="24" step="0.1" required>
                  <select id="tempUnit" class="form-control" style="width: 100px;">
                    <option value="c" selected>&deg;C</option>
                    <option value="f">&deg;F</option>
                  </select>
                </div>
                <span class="hint">Comfort range typically 20&deg;C &ndash; 26&deg;C (68&deg;F &ndash; 78&deg;F)</span>
              </div>
              <div class="form-group">
                <label for="rhVal">Relative Humidity ($RH$ in %)</label>
                <input type="number" id="rhVal" class="form-control" value="50" min="0" max="100" step="0.5" required>
                <span class="hint">Standard indoor design target ~40% &ndash; 60%</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="pressureVal">Barometric Atmospheric Pressure ($P_{atm}$)</label>
                <div style="display: flex; gap: 0.5rem;">
                  <input type="number" id="pressureVal" class="form-control" value="101.325" step="any" required>
                  <select id="pressureUnit" class="form-control" style="width: 110px;">
                    <option value="kpa" selected>kPa</option>
                    <option value="bar">bar</option>
                    <option value="psi">psi</option>
                    <option value="inhg">inHg</option>
                  </select>
                </div>
                <span class="hint">Standard sea level pressure = 101.325 kPa (14.696 psi)</span>
              </div>
              <div class="form-group">
                <label for="elevPreset">Elevation Preset (Barometric Estimate)</label>
                <select id="elevPreset" class="form-control">
                  <option value="101.325" selected>Sea Level (0 m / 0 ft &rarr; 101.325 kPa)</option>
                  <option value="95.46">500 m / 1,640 ft &rarr; 95.46 kPa</option>
                  <option value="89.87">1,000 m / 3,280 ft &rarr; 89.87 kPa</option>
                  <option value="84.56">1,500 m / 4,920 ft &rarr; 84.56 kPa</option>
                  <option value="79.50">2,000 m / 6,560 ft &rarr; 79.50 kPa</option>
                </select>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcPsychBtn">Compute Psychrometric Properties</button>
              <button type="reset" class="btn btn-secondary" id="resetPsychBtn">Reset</button>
            </div>
          </form>

          <div id="psychResultBox" class="results-container" style="display: none; margin-top: 1.5rem;">
            <h3>Calculated Moist Air Psychrometric State Point</h3>
            <div class="results-grid">
              <div class="result-tile highlight">
                <span class="result-label">Dew Point Temperature ($T_{dp}$)</span>
                <span class="result-value" id="resDewPoint">-- &deg;C</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Wet-Bulb Temperature ($T_{wb}$)</span>
                <span class="result-value" id="resWetBulb">-- &deg;C</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Humidity Ratio ($W$)</span>
                <span class="result-value" id="resHumRatio">-- g/kg</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Specific Enthalpy ($h$)</span>
                <span class="result-value" id="resEnthalpy">-- kJ/kg</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Specific Volume ($v$)</span>
                <span class="result-value" id="resSpecVol">-- m³/kg</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Moist Air Density ($\rho$)</span>
                <span class="result-value" id="resDensity">-- kg/m³</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Vapor Pressure ($P_w$)</span>
                <span class="result-value" id="resVaporPress">-- kPa</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Saturation Vapor Pressure ($P_{ws}$)</span>
                <span class="result-value" id="resSatPress">-- kPa</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Psychrometrics and Moist Air Thermodynamics</h2>
          <p>
            <strong>Psychrometrics</strong> is the branch of applied thermodynamics that investigates the physical, thermal, and psychrometric properties of atmospheric gas mixtures comprising dry air and water vapor. In heating, ventilation, air conditioning (HVAC), industrial drying, cleanroom environmental control, and meteorology, precise evaluation of moist air thermodynamic properties is essential to size air handling units, cooling towers, dehumidifiers, and thermal comfort systems per standards such as <strong>ASHRAE 55</strong> and <strong>ASHRAE 62.1</strong>.
          </p>
          <p>
            Atmospheric air is not a single uniform chemical species; rather, it behaves as a binary mixture of dry air (predominantly nitrogen, oxygen, argon, and carbon dioxide with an average molar mass $M_{da} = 28.966\text{ g/mol}$) and gaseous water vapor ($M_w = 18.01528\text{ g/mol}$). According to Dalton's Law of Partial Pressures, the total barometric atmospheric pressure ($P_{atm}$) is the sum of dry air partial pressure ($P_a$) and water vapor partial pressure ($P_w$):
          </p>
          <div class="formula-box">
            $$P_{atm} = P_a + P_w$$
          </div>

          <h2>Key Psychrometric State Parameters &amp; Governing Equations</h2>
          <p>
            Under the formulation outlined in the <em>ASHRAE Handbook &ndash; Fundamentals (Chapter 1)</em>, the state of moist air at any given barometric pressure is uniquely determined by any two independent thermodynamic properties (most commonly dry-bulb temperature and relative humidity).
          </p>

          <h3>1. Saturation Vapor Pressure ($P_{ws}$)</h3>
          <p>
            Saturation vapor pressure represents the maximum partial pressure exerted by water vapor in equilibrium with pure liquid water at temperature $T$ (°C). Using the highly accurate Magnus-Tetens empirical formulation (valid between $-40^\circ\text{C}$ and $+50^\circ\text{C}$):
          </p>
          <div class="formula-box">
            $$P_{ws}(T) = 0.61078 \times \exp\left(\frac{17.27 \cdot T}{T + 237.3}\right) \quad [\text{kPa}]$$
          </div>

          <h3>2. Actual Vapor Pressure ($P_w$) and Relative Humidity ($RH$)</h3>
          <p>
            Relative humidity ($RH$) is defined as the ratio of actual water vapor partial pressure to saturation vapor pressure at the identical dry-bulb temperature:
          </p>
          <div class="formula-box">
            $$RH = \frac{P_w}{P_{ws}(T_{db})} \times 100\% \implies P_w = \left(\frac{RH}{100}\right) \cdot P_{ws}(T_{db})$$
          </div>

          <h3>3. Humidity Ratio ($W$, Specific Humidity)</h3>
          <p>
            The humidity ratio ($W$), also referred to as absolute or specific humidity, expresses the mass of water vapor associated with each unit mass of bone-dry air. Derived from the ideal gas law:
          </p>
          <div class="formula-box">
            $$W = \frac{m_w}{m_{da}} = \frac{M_w \cdot P_w}{M_{da} \cdot P_a} = \frac{18.01528}{28.966} \cdot \left(\frac{P_w}{P_{atm} - P_w}\right) \approx 0.62198 \cdot \frac{P_w}{P_{atm} - P_w} \quad [\text{kg}_w/\text{kg}_{da}]$$
          </div>

          <h3>4. Dew Point Temperature ($T_{dp}$)</h3>
          <p>
            The dew point is the temperature at which water vapor in moist air begins to condense into liquid droplets at constant total atmospheric pressure. Inverting the Magnus-Tetens relationship with respect to actual vapor pressure $P_w$:
          </p>
          <div class="formula-box">
            $$\alpha(T_{db}, RH) = \ln\left(\frac{P_w}{0.61078}\right), \quad T_{dp} = \frac{237.3 \cdot \alpha}{17.27 - \alpha} \quad [^\circ\text{C}]$$
          </div>

          <h3>5. Wet-Bulb Temperature ($T_{wb}$)</h3>
          <p>
            The wet-bulb temperature corresponds to the temperature indicated by a thermometer enveloped in a wetted wick exposed to rapid air currents. It denotes the thermodynamic limit of evaporative cooling. A widely utilized and continuous numerical approximation developed by Stull (2011) evaluates $T_{wb}$ directly from dry-bulb temperature and relative humidity:
          </p>
          <div class="formula-box">
            $$\begin{aligned}
            T_{wb} &= T_{db} \cdot \text{atan}(0.151977 \sqrt{RH + 8.313659}) + \text{atan}(T_{db} + RH) \\
            &\quad - \text{atan}(RH - 1.676331) + 0.00391838 \cdot (RH)^{1.5} \cdot \text{atan}(0.023101 \cdot RH) - 4.686035
            \end{aligned}$$
          </div>

          <h3>6. Specific Enthalpy of Moist Air ($h$)</h3>
          <p>
            Specific enthalpy ($h$) quantifies the total thermal energy content per kilogram of dry air, incorporating sensible thermal energy of dry air plus the latent and sensible heat of the associated water vapor (reference datum at $0^\circ\text{C}$ dry air and liquid water):
          </p>
          <div class="formula-box">
            $$h = c_{pa} \cdot T_{db} + W \cdot (h_{we} + c_{pw} \cdot T_{db}) = 1.006 \cdot T_{db} + W \cdot (2501 + 1.86 \cdot T_{db}) \quad [\text{kJ/kg}_{da}]$$
          </div>
          <p>
            Where $c_{pa} = 1.006\text{ kJ/(kg}\cdot\text{K)}$ is the specific heat capacity of dry air, $h_{we} = 2501\text{ kJ/kg}$ is the latent heat of vaporization of water at $0^\circ\text{C}$, and $c_{pw} = 1.86\text{ kJ/(kg}\cdot\text{K)}$ is the specific heat of water vapor.
          </p>

          <h3>7. Specific Volume ($v$) and Moist Air Density ($\rho$)</h3>
          <p>
            Specific volume represents the cubic meters of moist air mixture space occupied per kilogram of dry air:
          </p>
          <div class="formula-box">
            $$v = \frac{R_a \cdot (T_{db} + 273.15) \cdot (1 + 1.6078 \cdot W)}{P_{atm}} \quad [\text{m}^3/\text{kg}_{da}]$$
          </div>
          <p>
            Where $R_a = 0.287042\text{ kJ/(kg}\cdot\text{K)}$ is the specific gas constant of dry air, and $P_{atm}$ is in $\text{kPa}$. Moist air mixture mass density ($\rho$) is subsequently computed as:
          </p>
          <div class="formula-box">
            $$\rho = \frac{1 + W}{v} \quad [\text{kg/m}^3]$$
          </div>

          <h2>Psychrometric Process Reference Matrix</h2>
          <p>
            Every HVAC conditioning process traces a distinct directional path across the psychrometric diagram:
          </p>
          <table class="reference-table">
            <thead>
              <tr>
                <th>Psychrometric Process</th>
                <th>Sensible Heat ($T_{db}$)</th>
                <th>Humidity Ratio ($W$)</th>
                <th>Relative Humidity ($RH$)</th>
                <th>Enthalpy ($h$)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Sensible Heating (Electric Duct Heater)</td>
                <td>Increases (&uarr;)</td>
                <td>Constant (&rarr;)</td>
                <td>Decreases (&darr;)</td>
                <td>Increases (&uarr;)</td>
              </tr>
              <tr>
                <td>Sensible Cooling (Dry Coil above $T_{dp}$)</td>
                <td>Decreases (&darr;)</td>
                <td>Constant (&rarr;)</td>
                <td>Increases (&uarr;)</td>
                <td>Decreases (&darr;)</td>
              </tr>
              <tr>
                <td>Cooling &amp; Dehumidification (Chilled Water Coil)</td>
                <td>Decreases (&darr;)</td>
                <td>Decreases (&darr;)</td>
                <td>Increases (&uarr;)</td>
                <td>Decreases (&darr;)</td>
              </tr>
              <tr>
                <td>Adiabatic Humidification (Evaporative Cooler)</td>
                <td>Decreases (&darr;)</td>
                <td>Increases (&uarr;)</td>
                <td>Increases (&uarr;)</td>
                <td>Constant (&rarr;)</td>
              </tr>
              <tr>
                <td>Steam Humidification (Isothermal)</td>
                <td>Constant (&rarr;)</td>
                <td>Increases (&uarr;)</td>
                <td>Increases (&uarr;)</td>
                <td>Increases (&uarr;)</td>
              </tr>
              <tr>
                <td>Chemical Dehumidification (Desiccant Wheel)</td>
                <td>Increases (&uarr;)</td>
                <td>Decreases (&darr;)</td>
                <td>Decreases (&darr;)</td>
                <td>Constant / Slight &uarr;</td>
              </tr>
            </tbody>
          </table>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: Cleanroom Air Conditioning Sizing</h3>
            <p><strong>Design Scenario:</strong> An ISO Class 7 pharmaceutical cleanroom supply air system draws outdoor air at Summer design conditions: $T_{db} = 35.0^\circ\text{C}$, $RH = 60.0\%$, at standard atmospheric pressure $P_{atm} = 101.325\text{ kPa}$. The air handling unit conditions this air to a space supply state of $T_{supply} = 16.0^\circ\text{C}$ and $W_{supply} = 0.0085\text{ kg}_w/\text{kg}_{da}$. Calculate the outdoor air state point (dew point, humidity ratio, and enthalpy) and determine the total enthalpy extraction ($\Delta h$) required per kilogram of dry air.</p>
            
            <p><strong>Step 1: Calculate Outdoor Air Saturation and Actual Vapor Pressures</strong></p>
            <div class="formula-box">
              $$P_{ws}(35) = 0.61078 \times \exp\left(\frac{17.27 \times 35}{35 + 237.3}\right) = 0.61078 \times \exp(2.2198) = 5.623\text{ kPa}$$
              $$P_w = 0.60 \times 5.623\text{ kPa} = 3.374\text{ kPa}$$
            </div>

            <p><strong>Step 2: Determine Outdoor Humidity Ratio ($W_{out}$)</strong></p>
            <div class="formula-box">
              $$W_{out} = 0.62198 \times \frac{3.374}{101.325 - 3.374} = 0.62198 \times \frac{3.374}{97.951} = 0.02142\text{ kg}_w/\text{kg}_{da} = 21.42\text{ g/kg}$$
            </div>

            <p><strong>Step 3: Calculate Outdoor Dew Point Temperature ($T_{dp}$)</strong></p>
            <div class="formula-box">
              $$\alpha = \ln\left(\frac{3.374}{0.61078}\right) = \ln(5.524) = 1.7091$$
              $$T_{dp} = \frac{237.3 \times 1.7091}{17.27 - 1.7091} = \frac{405.57}{15.5609} \approx 26.06^\circ\text{C}$$
            </div>

            <p><strong>Step 4: Calculate Specific Enthalpies of Outdoor and Supply Air</strong></p>
            <div class="formula-box">
              $$h_{out} = 1.006 \times 35 + 0.02142 \times (2501 + 1.86 \times 35) = 35.21 + 0.02142 \times 2566.1 = 35.21 + 54.97 = 90.18\text{ kJ/kg}_{da}$$
              $$h_{supply} = 1.006 \times 16 + 0.0085 \times (2501 + 1.86 \times 16) = 16.10 + 0.0085 \times 2530.76 = 16.10 + 21.51 = 37.61\text{ kJ/kg}_{da}$$
            </div>

            <p><strong>Step 5: Enthalpy Extraction Rate ($\Delta h$)</strong></p>
            <div class="formula-box">
              $$\Delta h = h_{out} - h_{supply} = 90.18 - 37.61 = 52.57\text{ kJ/kg}_{da}$$
            </div>
            <p>
              <strong>Engineering Sizing Insight:</strong> Latent moisture removal accounts for $\frac{54.97 - 21.51}{52.57} = \frac{33.46}{52.57} \approx 63.6\%$ of the total cooling coil load. The coil must operate well below the $26.06^\circ\text{C}$ dew point to condense out $12.92\text{ g}$ of moisture per kilogram of processed dry air.
            </p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related HVAC &amp; Fluid Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="hvac-calculator.html">HVAC Duct Sizing &amp; CFM</a></li>
            <li><a href="heat-exchanger-calculator.html">Heat Exchanger LMTD</a></li>
            <li><a href="hydraulic-pump-power-calculator.html">Hydraulic Pump Power</a></li>
            <li><a href="power-to-torque-calculator.html">Power to Torque Calculator</a></li>
            <li><a href="cooling-load-calculator.html">Cooling Load Calculator</a></li>
            <li><a href="pipe-sizing-calculator.html">Pipe Sizing Calculator</a></li>
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
      const calcBtn = document.getElementById('calcPsychBtn');
      const resetBtn = document.getElementById('resetPsychBtn');
      const resultBox = document.getElementById('psychResultBox');
      const elevPreset = document.getElementById('elevPreset');
      const pressureVal = document.getElementById('pressureVal');
      const pressureUnit = document.getElementById('pressureUnit');

      elevPreset.addEventListener('change', function() {
        if (pressureUnit.value === 'kpa') {
          pressureVal.value = this.value;
        } else if (pressureUnit.value === 'psi') {
          pressureVal.value = (parseFloat(this.value) * 0.145038).toFixed(3);
        } else if (pressureUnit.value === 'bar') {
          pressureVal.value = (parseFloat(this.value) * 0.01).toFixed(4);
        } else if (pressureUnit.value === 'inhg') {
          pressureVal.value = (parseFloat(this.value) * 0.2953).toFixed(2);
        }
      });

      function calculatePsych() {
        const tUnit = document.getElementById('tempUnit').value;
        let tInput = parseFloat(document.getElementById('tempDb').value);
        let rh = parseFloat(document.getElementById('rhVal').value);
        let pInput = parseFloat(pressureVal.value);
        let pU = pressureUnit.value;

        if (isNaN(tInput) || isNaN(rh) || isNaN(pInput) || pInput <= 0) {
          alert('Please enter valid numerical parameters.');
          return;
        }

        // Convert dry-bulb to Celsius
        let tDb_C = (tUnit === 'f') ? (tInput - 32) * (5 / 9) : tInput;
        // Clamp RH between 0.01 and 100
        rh = Math.max(0.01, Math.min(100.0, rh));

        // Convert atmospheric pressure to kPa
        let pAtm_kPa = 101.325;
        if (pU === 'kpa') pAtm_kPa = pInput;
        else if (pU === 'bar') pAtm_kPa = pInput * 100.0;
        else if (pU === 'psi') pAtm_kPa = pInput / 0.1450377;
        else if (pU === 'inhg') pAtm_kPa = pInput / 0.2952998;

        // 1. Saturation vapor pressure (kPa) via Magnus-Tetens
        const pSat_kPa = 0.61078 * Math.exp((17.27 * tDb_C) / (tDb_C + 237.3));

        // 2. Actual vapor pressure (kPa)
        const pVapor_kPa = (rh / 100.0) * pSat_kPa;

        // Ensure vapor pressure does not exceed atmospheric pressure
        const effectiveVapor_kPa = Math.min(pVapor_kPa, pAtm_kPa * 0.99);

        // 3. Humidity ratio W [kg_w / kg_da]
        const humRatio = 0.62198 * (effectiveVapor_kPa / (pAtm_kPa - effectiveVapor_kPa));
        const humRatio_g_kg = humRatio * 1000.0;

        // 4. Dew point temperature [C]
        const alpha = Math.log(effectiveVapor_kPa / 0.61078);
        const tDp_C = (237.3 * alpha) / (17.27 - alpha);

        // 5. Wet-bulb temperature [C] via Stull's equation
        const atan = Math.atan;
        const sqrt = Math.sqrt;
        const tWb_C = tDb_C * atan(0.151977 * sqrt(rh + 8.313659)) +
                      atan(tDb_C + rh) -
                      atan(rh - 1.676331) +
                      0.00391838 * Math.pow(rh, 1.5) * atan(0.023101 * rh) -
                      4.686035;

        // 6. Specific enthalpy [kJ / kg_da]
        const enthalpy = 1.006 * tDb_C + humRatio * (2501.0 + 1.86 * tDb_C);

        // 7. Specific volume [m^3 / kg_da]
        // R_da = 0.287042 kPa * m^3 / (kg * K)
        const specVol = (0.287042 * (tDb_C + 273.15) * (1.0 + 1.6078 * humRatio)) / pAtm_kPa;

        // 8. Density [kg_moist_air / m^3]
        const density = (1.0 + humRatio) / specVol;

        // Render outputs
        const unitSuffix = (tUnit === 'f') ? ' °F' : ' °C';
        const displayDp = (tUnit === 'f') ? (tDp_C * (9/5) + 32) : tDp_C;
        const displayWb = (tUnit === 'f') ? (tWb_C * (9/5) + 32) : tWb_C;

        document.getElementById('resDewPoint').textContent = displayDp.toFixed(2) + unitSuffix;
        document.getElementById('resWetBulb').textContent = displayWb.toFixed(2) + unitSuffix;
        document.getElementById('resHumRatio').textContent = humRatio_g_kg.toFixed(3) + ' g/kg';
        document.getElementById('resEnthalpy').textContent = enthalpy.toFixed(2) + ' kJ/kg';
        document.getElementById('resSpecVol').textContent = specVol.toFixed(4) + ' m³/kg';
        document.getElementById('resDensity').textContent = density.toFixed(3) + ' kg/m³';
        document.getElementById('resVaporPress').textContent = effectiveVapor_kPa.toFixed(3) + ' kPa';
        document.getElementById('resSatPress').textContent = pSat_kPa.toFixed(3) + ' kPa';

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculatePsych);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
      });

      calculatePsych();
    });
  </script>
</body>
</html>
"""

def main():
    with open("power-to-torque-calculator.html", "w", encoding="utf-8") as f:
        f.write(TOOL_5_HTML.strip() + "\n")
    print("[PASS] power-to-torque-calculator.html generated successfully!")

    with open("psychrometric-calculator.html", "w", encoding="utf-8") as f:
        f.write(TOOL_6_HTML.strip() + "\n")
    print("[PASS] psychrometric-calculator.html generated successfully!")

if __name__ == "__main__":
    main()
