# -*- coding: utf-8 -*-
"""
Script to generate Batch 9 Part 1 tools:
1. belt-length-calculator.html
2. conveyor-belt-speed-calculator.html
"""
import os

TOOL_1_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Belt Length Calculator | Open & Crossed Two-Pulley V-Belt Length</title>
  <meta name="description" content="Calculate two-pulley belt pitch lengths, center distances, and wrap angles for open and crossed belt drives per ISO 5296 and RMA IP-20 mechanical power transmission standards.">
  <link rel="canonical" href="https://calchub.cloud/belt-length-calculator.html">
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
        "name": "Belt Length Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Mechanical power transmission tool calculating pitch length, center distance, arc of contact, and speed ratio for open and crossed two-pulley V-belt and synchronous timing belt drives.",
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
            "name": "What is the formula for calculating open belt length for two pulleys?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The exact geometric formula for an open two-pulley belt drive is: L = 2*C*cos(phi) + (pi/2)*(D + d) + phi*(D - d), where phi = arcsin((D - d) / (2*C)). In standard mechanical design practice, the highly accurate standard approximation is: L approx 2*C + (pi/2)*(D + d) + (D - d)^2 / (4*C), where C is center distance, D is large pulley diameter, and d is small pulley diameter."
            }
          },
          {
            "@type": "Question",
            "name": "How does belt length calculation differ for a crossed belt drive?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In a crossed belt drive (where the driven pulley rotates in the reverse direction), the belt crosses over itself. The standard formula becomes: L approx 2*C + (pi/2)*(D + d) + (D + d)^2 / (4*C). The arc of contact is identical on both pulleys: theta = 180 deg + 2*arcsin((D + d) / (2*C))."
            }
          },
          {
            "@type": "Question",
            "name": "Why is the arc of contact (wrap angle) critical for V-belt drive capacity?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Frictional grip between the belt and pulley grooves obeys the belt friction equation (Euler-Eytelwein formula): T1/T2 = e^(mu*theta/sin(alpha/2)). When the wrap angle theta drops below 180 degrees (common when large pulley ratio differences exist at tight center distances), frictional traction decreases exponentially, requiring an arc-of-contact correction factor (C_theta) to derate allowable belt power."
            }
          },
          {
            "@type": "Question",
            "name": "What is the recommended center distance between two pulleys?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Per standard mechanical power transmission guidelines (RMA/ISO), the minimum center distance should satisfy: C_min = 0.55*(D + d) + T_belt, and ideally C >= D. The maximum center distance should typically not exceed: C_max = 2*(D + d), to prevent excessive belt vibration, catenary sag, and flapping."
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
      <a href="mechanical.html">Mechanical &amp; Machine Design</a> &rsaquo;
      <span>Belt Length Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">ISO 5296 &amp; RMA IP-20 Machine Design Standards</div>
          <h1 class="calc-title">Belt Length Calculator</h1>
          <p class="calc-tagline">Calculate theoretical pitch length, required center distance, arc of contact, and speed ratios for open and crossed two-pulley mechanical belt drives.</p>
        </header>

        <div class="tool-card">
          <form id="beltCalcForm">
            <div class="calc-grid">
              <div class="form-group">
                <label for="calcMode">Calculation Mode</label>
                <select id="calcMode">
                  <option value="findLength" selected>Calculate Belt Length from Center Distance</option>
                  <option value="findCenter">Calculate Center Distance from Standard Belt Length</option>
                </select>
              </div>

              <div class="form-group">
                <label for="driveType">Drive Configuration</label>
                <select id="driveType">
                  <option value="open" selected>Open Belt Drive (Same Direction)</option>
                  <option value="crossed">Crossed Belt Drive (Reversed Rotation)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="units">Engineering Units</label>
                <select id="units">
                  <option value="metric" selected>Metric (mm, meters)</option>
                  <option value="imperial">Imperial (inches, feet)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="diamLarge" id="lblDiamLarge">Large Pulley Diameter D [mm]</label>
                <input type="number" id="diamLarge" step="0.5" min="10" max="5000" value="250">
              </div>

              <div class="form-group">
                <label for="diamSmall" id="lblDiamSmall">Small Pulley Diameter d [mm]</label>
                <input type="number" id="diamSmall" step="0.5" min="5" max="5000" value="125">
              </div>

              <div class="form-group" id="grpCenterDist">
                <label for="centerDist" id="lblCenterDist">Center Distance C [mm]</label>
                <input type="number" id="centerDist" step="1" min="10" max="10000" value="500">
              </div>

              <div class="form-group" id="grpBeltLength" style="display: none;">
                <label for="givenBeltLength" id="lblGivenBeltLength">Nominal Belt Length L [mm]</label>
                <input type="number" id="givenBeltLength" step="1" min="50" max="20000" value="1600">
              </div>

              <div class="form-group">
                <label for="motorRpm">Drive Pulley Rotational Speed [RPM]</label>
                <input type="number" id="motorRpm" step="10" min="1" max="20000" value="1750">
              </div>
            </div>

            <div class="calc-actions">
              <button type="button" id="calcBeltBtn" class="btn btn-primary">Calculate Belt Drive Parameters</button>
              <button type="reset" id="resetBeltBtn" class="btn btn-secondary">Reset Defaults</button>
            </div>
          </form>

          <div id="beltResultBox" class="results-container" style="display: none;">
            <h3>Mechanical Belt Drive Engineering Results</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label" id="resPrimaryLabel">Calculated Belt Pitch Length</span>
                <span id="resPrimaryVal" class="result-value">-- mm</span>
              </div>
              <div class="result-tile">
                <span class="result-label" id="resSecondaryLabel">Shaft Center Distance</span>
                <span id="resSecondaryVal" class="result-value">-- mm</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Speed Transmission Ratio (i)</span>
                <span id="resRatio" class="result-value">--</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Driven Pulley Speed</span>
                <span id="resDrivenRpm" class="result-value">-- RPM</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Small Pulley Wrap Angle (&theta;)</span>
                <span id="resWrapSmall" class="result-value">-- &deg;</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Large Pulley Wrap Angle (&theta;)</span>
                <span id="resWrapLarge" class="result-value">-- &deg;</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Linear Belt Speed (v)</span>
                <span id="resBeltSpeed" class="result-value">-- m/s</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Arc of Contact Factor (C_&theta;)</span>
                <span id="resWrapFactor" class="result-value">--</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Center Distance Validation</span>
                <span id="resDistStatus" class="result-value">--</span>
              </div>
            </div>
            <div id="beltNotesBox" style="margin-top: 1rem; color: #1e40af; background: #eff6ff; border: 1px solid #bfdbfe; padding: 0.75rem; border-radius: 6px;"></div>
          </div>
        </div>

        <article class="article-body">
          <h2>Mechanical Principles of Two-Pulley Belt Transmission Systems</h2>
          <p>Flexible belt drives represent one of the most widely utilized mechanical power transmission elements in industrial machinery, automotive engines, agricultural harvesters, and HVAC air handling equipment. By utilizing friction (in flat and V-belts) or positive tooth engagement (in synchronous timing belts), a belt drive smoothly transmits rotational torque between parallel shafts while providing critical vibration isolation, shock-load damping, and overload protection.</p>

          <p>Proper belt dimensioning requires solving exact geometric tangency equations between two pitch circles. If a belt is sized too short, bearings endure severe static radial overloads, causing premature fatigue spalling and shaft deflection. If sized too long, the belt experiences excessive slack-side catenary flutter, pulley slippage, rapid tooth jumping (ratcheting), and localized thermal degradation.</p>

          <h2>Open Belt Drive Mathematical Formulations</h2>
          <p>In an open belt drive configuration, the belt encircles both pulleys without crossing, ensuring that both the driving and driven shafts rotate in identical directions. The belt consists of two tangent spans and two circular arcs contacting the pulley circumferences.</p>

          <p>The exact trigonometric formulation for the total pitch length (\(L\)) of an open belt drive is:</p>

          <div class="formula-box">
            $$L = 2C \cos\phi + \frac{\pi}{2}(D + d) + \phi(D - d)$$
          </div>

          <p>Where the angle of inclination (\(\phi\)) between the centerline and the tangent line is given by:</p>

          <div class="formula-box">
            $$\phi = \arcsin\left(\frac{D - d}{2C}\right) \quad [\text{radians}]$$
          </div>

          <p>For standard mechanical design calculations, engineering standards (ISO 5296 and RMA IP-20) universally accept the classic truncated series expansion approximation:</p>

          <div class="formula-box">
            $$L \approx 2C + \frac{\pi}{2}(D + d) + \frac{(D - d)^2}{4C}$$
          </div>

          <p>Where the geometric parameters represent:</p>
          <ul>
            <li><strong>\(L\)</strong>: Total belt pitch length (mm or inches).</li>
            <li><strong>\(C\)</strong>: Center-to-center shaft distance (mm or inches).</li>
            <li><strong>\(D\)</strong>: Pitch diameter of the larger pulley (mm or inches).</li>
            <li><strong>\(d\)</strong>: Pitch diameter of the smaller pulley (mm or inches).</li>
          </ul>

          <h2>Crossed Belt Drive Mathematical Formulations</h2>
          <p>In a crossed belt drive, the belt crosses over midway between shafts, causing the driven pulley to rotate in the opposite direction from the driver. Because the tangent lines cross the shaft center axis, both pulleys share an identical, expanded arc of contact:</p>

          <div class="formula-box">
            $$L_{\text{crossed}} \approx 2C + \frac{\pi}{2}(D + d) + \frac{(D + d)^2}{4C}$$
          </div>

          <p>The angle of contact for crossed drives is symmetrical on both pulleys:</p>

          <div class="formula-box">
            $$\theta_{\text{crossed}} = 180^\circ + 2\arcsin\left(\frac{D + d}{2C}\right)$$
          </div>

          <p>While crossed drives provide a generous arc of contact (\(>180^\circ\)), internal friction and rubbing occur at the crossover point unless guide rollers or special quarter-turn configurations are implemented. Consequently, crossed drives are strictly restricted to low-speed flat belt systems and are never recommended for standard V-belts or timing belts.</p>

          <h2>Center Distance Computation from Known Belt Length</h2>
          <p>In equipment retrofits and production machine design, engineers often select a standardized, off-the-shelf belt catalog length (\(L\)) and must compute the precise nominal center distance (\(C\)) to position motor slide rails. Solving the open-belt quadratic equation yields:</p>

          <div class="formula-box">
            $$C = \frac{B + \sqrt{B^2 - 2(D - d)^2}}{4}$$
          </div>

          <p>Where the intermediate geometric constant \(B\) is defined as:</p>

          <div class="formula-box">
            $$B = L - \frac{\pi}{2}(D + d)$$
          </div>

          <h2>Arc of Contact (Wrap Angle) and Frictional Grip</h2>
          <p>Frictional traction between a flexible belt and a smooth pulley groove is dictated by the fundamental <strong>Euler-Eytelwein equation</strong> (also known as the capstan formula):</p>

          <div class="formula-box">
            $$\frac{T_1}{T_2} = e^{\mu \cdot \theta / \sin(\alpha / 2)}$$
          </div>

          <p>Where \(T_1\) and \(T_2\) are the tight-side and slack-side tensions, \(\mu\) is the coefficient of friction, \(\theta\) is the wrap angle in radians, and \(\alpha\) is the included V-groove angle (typically 34&deg; to 38&deg;). For an open belt drive, the small pulley wrap angle (\(\theta_{\text{small}}\)) is always less than 180&deg;:</p>

          <div class="formula-box">
            $$\theta_{\text{small}} = 180^\circ - 2\arcsin\left(\frac{D - d}{2C}\right) \approx 180^\circ - 57.3^\circ \left(\frac{D - d}{C}\right)$$
            $$\theta_{\text{large}} = 180^\circ + 2\arcsin\left(\frac{D - d}{2C}\right) \approx 180^\circ + 57.3^\circ \left(\frac{D - d}{C}\right)$$
          </div>

          <p>Whenever \(\theta_{\text{small}} < 180^\circ\), the drive cannot transmit full catalog horsepower. Power capacity must be derated by the arc of contact correction factor (\(C_\theta\)):</p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Small Pulley Wrap Angle (\(\theta_{\text{small}}\))</th>
                <th>Arc Factor (\(C_\theta\)) (V-Belts)</th>
                <th>Arc Factor (\(C_\theta\)) (Flat Belts)</th>
                <th>Required Horsepower Multiplier</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>180&deg;</td>
                <td>1.00</td>
                <td>1.00</td>
                <td>1.00 &times; (No derate)</td>
              </tr>
              <tr>
                <td>170&deg;</td>
                <td>0.98</td>
                <td>0.96</td>
                <td>1.02 &times; Design HP</td>
              </tr>
              <tr>
                <td>160&deg;</td>
                <td>0.95</td>
                <td>0.91</td>
                <td>1.05 &times; Design HP</td>
              </tr>
              <tr>
                <td>150&deg;</td>
                <td>0.92</td>
                <td>0.86</td>
                <td>1.09 &times; Design HP</td>
              </tr>
              <tr>
                <td>140&deg;</td>
                <td>0.89</td>
                <td>0.81</td>
                <td>1.12 &times; Design HP</td>
              </tr>
              <tr>
                <td>130&deg;</td>
                <td>0.86</td>
                <td>0.75</td>
                <td>1.16 &times; Design HP</td>
              </tr>
              <tr>
                <td>120&deg;</td>
                <td>0.82</td>
                <td>0.69</td>
                <td>1.22 &times; Design HP</td>
              </tr>
            </tbody>
          </table>

          <h2>Linear Belt Speed & Centrifugal Force Limits</h2>
          <p>Linear surface velocity (\(v\)) determines dynamic stress, cooling efficiency, and centrifugal tension throwing the belt outward from the pulley face:</p>

          <div class="formula-box">
            $$v = \frac{\pi \cdot d \cdot N}{60 \times 1000} \quad [\text{m/s}] \quad \Longleftrightarrow \quad v = \frac{\pi \cdot d \cdot N}{12} \quad [\text{ft/min}]$$
          </div>

          <p>Standard classical industrial V-belts (A, B, C sections) operate optimally between <strong>10 m/s and 25 m/s (2,000 to 5,000 ft/min)</strong>. At speeds exceeding 30 m/s (6,000 ft/min), centrifugal tension (\(T_c = m \cdot v^2\)) diminishes effective wedging grip so drastically that dynamic re-tensioning, precision dynamic balancing, and ductile iron or steel sheaves become mandatory.</p>

          <div class="worked-example-card">
            <h3>Step-by-Step Worked Case Study: Industrial Exhaust Blower Drive</h3>
            <p><strong>Design Scenario:</strong> An engineer is designing a V-belt drive connecting a 4-pole electric motor (1,750 RPM) to an industrial ventilation centrifugal blower running at 875 RPM.</p>
            <ul>
              <li>Motor drive pulley diameter: \(d = 125\text{ mm}\).</li>
              <li>Blower driven pulley diameter: \(D = 250\text{ mm}\).</li>
              <li>Shaft center distance constraint: \(C = 500\text{ mm}\).</li>
              <li>Drive type: Open belt drive.</li>
            </ul>

            <p><strong>Step 1: Calculate speed ratio and driven speed</strong></p>
            <div class="formula-box">
              $$i = \frac{D}{d} = \frac{250}{125} = 2.00$$
              $$N_{\text{driven}} = \frac{N_{\text{motor}}}{i} = \frac{1750}{2.00} = 875\text{ RPM}$$
            </div>

            <p><strong>Step 2: Calculate approximate belt pitch length (\(L\))</strong></p>
            <div class="formula-box">
              $$L \approx 2(500) + \frac{\pi}{2}(250 + 125) + \frac{(250 - 125)^2}{4(500)}$$
              $$L \approx 1000 + 1.5708 \times 375 + \frac{15625}{2000} = 1000 + 589.05 + 7.81 = 1596.86\text{ mm}$$
            </div>
            <p>The engineer selects the nearest standard ISO V-belt length: <strong>1,600 mm</strong> (or standard B61 / SPB1600).</p>

            <p><strong>Step 3: Calculate small pulley arc of contact (\(\theta_{\text{small}}\))</strong></p>
            <div class="formula-box">
              $$\phi = \arcsin\left(\frac{250 - 125}{2 \times 500}\right) = \arcsin\left(\frac{125}{1000}\right) = \arcsin(0.125) = 7.18^\circ$$
              $$\theta_{\text{small}} = 180^\circ - 2(7.18^\circ) = 165.64^\circ$$
            </div>

            <p><strong>Step 4: Determine linear belt speed (\(v\))</strong></p>
            <div class="formula-box">
              $$v = \frac{\pi \cdot 125 \cdot 1750}{60000} = \frac{687223}{60000} = 11.45\text{ m/s} \quad (2254\text{ ft/min})$$
            </div>
            <p><strong>Engineering Conclusion:</strong> Operating at 11.45 m/s, the belt operates within the optimal aerodynamic efficiency band. The wrap angle of 165.6&deg; yields an arc factor \(C_\theta \approx 0.965\), requiring a slight 3.6% design power margin.</p>
          </div>

          <h2>Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3>What is the difference between belt pitch length, inside length, and outside length?</h3>
            <p>Pitch length (Lp or Lw) is the circumference measured along the neutral bending axis of the belt's internal tensile cords (aramid or polyester), where neither tension nor compression occurs during flexing. Inside length (Li) is measured along the inner bottom surface of the belt, while outside length (La) is measured along the outer top back. For classical V-belts: \(L_a \approx L_i + 50\text{ mm}\), and \(L_p \approx L_i + 30\text{ mm}\).</p>
          </div>

          <div class="faq-item">
            <h3>How do I select the proper center distance for a new belt drive?</h3>
            <p>As a rule of thumb, center distance should satisfy \(0.55(D + d) + t_{\text{belt}} \le C \le 2(D + d)\). A center distance that is too tight reduces the small pulley arc of contact below 120&deg;, severely limiting power capacity and inducing extreme flex fatigue. An overly long center distance causes belt whipping and necessitates heavy idler pulleys.</p>
          </div>

          <div class="faq-item">
            <h3>When should an idler pulley be used on a belt drive?</h3>
            <p>Idler pulleys are required when center distance is fixed without motor adjustment rails, when center distances are unusually long, or when an extreme pulley ratio causes the wrap angle on the small pulley to fall below 120&deg;. Idlers should always be positioned on the slack (loose) side of the drive. If an inside grooved idler is used, it should be placed near the large pulley; if an outside flat back-idler is used, it should be located near the small pulley to maximize wrap angle.</p>
          </div>

          <div class="faq-item">
            <h3>How does temperature affect industrial belt length and tension?</h3>
            <p>Standard rubber polychloroprene and EPDM belts have negative thermal expansion characteristics when under tension (the Gough-Joule effect), meaning they contract and tighten slightly as operating temperature rises. However, ambient heat above 85&deg;C (185&deg;F) accelerates elastomer hardening, ozone cracking, and cord degradation, reducing fatigue life by approximately 50% for every 10&deg;C rise above rated limits.</p>
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
        <li><a href="mechanical.html">Mechanical</a></li>
        <li><a href="ohms-law-calculator.html">Ohm's Law</a></li>
        <li><a href="sitemap.xml">Sitemap</a></li>
      </ul>
    </div>
  </footer>

  <script>
    const calcModeSelect = document.getElementById('calcMode');
    const driveTypeSelect = document.getElementById('driveType');
    const unitsSelect = document.getElementById('units');
    const diamLargeInput = document.getElementById('diamLarge');
    const diamSmallInput = document.getElementById('diamSmall');
    const centerDistInput = document.getElementById('centerDist');
    const givenBeltLengthInput = document.getElementById('givenBeltLength');
    const motorRpmInput = document.getElementById('motorRpm');

    const lblDiamLarge = document.getElementById('lblDiamLarge');
    const lblDiamSmall = document.getElementById('lblDiamSmall');
    const lblCenterDist = document.getElementById('lblCenterDist');
    const lblGivenBeltLength = document.getElementById('lblGivenBeltLength');
    const grpCenterDist = document.getElementById('grpCenterDist');
    const grpBeltLength = document.getElementById('grpBeltLength');

    const beltResultBox = document.getElementById('beltResultBox');
    const resPrimaryLabel = document.getElementById('resPrimaryLabel');
    const resPrimaryVal = document.getElementById('resPrimaryVal');
    const resSecondaryLabel = document.getElementById('resSecondaryLabel');
    const resSecondaryVal = document.getElementById('resSecondaryVal');
    const resRatio = document.getElementById('resRatio');
    const resDrivenRpm = document.getElementById('resDrivenRpm');
    const resWrapSmall = document.getElementById('resWrapSmall');
    const resWrapLarge = document.getElementById('resWrapLarge');
    const resBeltSpeed = document.getElementById('resBeltSpeed');
    const resWrapFactor = document.getElementById('resWrapFactor');
    const resDistStatus = document.getElementById('resDistStatus');
    const beltNotesBox = document.getElementById('beltNotesBox');

    calcModeSelect.addEventListener('change', function() {
      if (this.value === 'findLength') {
        grpCenterDist.style.display = 'block';
        grpBeltLength.style.display = 'none';
        resPrimaryLabel.textContent = "Calculated Belt Pitch Length";
        resSecondaryLabel.textContent = "Shaft Center Distance";
      } else {
        grpCenterDist.style.display = 'none';
        grpBeltLength.style.display = 'block';
        resPrimaryLabel.textContent = "Required Shaft Center Distance";
        resSecondaryLabel.textContent = "Catalog Belt Pitch Length";
      }
      calculateBeltDrive();
    });

    unitsSelect.addEventListener('change', function() {
      const isMetric = this.value === 'metric';
      const u = isMetric ? 'mm' : 'in';
      lblDiamLarge.textContent = `Large Pulley Diameter D [${u}]`;
      lblDiamSmall.textContent = `Small Pulley Diameter d [${u}]`;
      lblCenterDist.textContent = `Center Distance C [${u}]`;
      lblGivenBeltLength.textContent = `Nominal Belt Length L [${u}]`;

      if (isMetric) {
        diamLargeInput.value = 250;
        diamSmallInput.value = 125;
        centerDistInput.value = 500;
        givenBeltLengthInput.value = 1600;
      } else {
        diamLargeInput.value = 10.0;
        diamSmallInput.value = 5.0;
        centerDistInput.value = 20.0;
        givenBeltLengthInput.value = 64.0;
      }
      calculateBeltDrive();
    });

    function calculateBeltDrive() {
      const mode = calcModeSelect.value;
      const driveType = driveTypeSelect.value;
      const isMetric = unitsSelect.value === 'metric';
      const u = isMetric ? 'mm' : 'in';
      const spdUnit = isMetric ? 'm/s' : 'ft/min';

      let D = parseFloat(diamLargeInput.value);
      let d = parseFloat(diamSmallInput.value);
      let rpm = parseFloat(motorRpmInput.value);

      if (isNaN(D) || D <= 0) D = isMetric ? 250 : 10;
      if (isNaN(d) || d <= 0) d = isMetric ? 125 : 5;
      if (d > D) {
        // Swap so D is always larger
        const temp = D;
        D = d;
        d = temp;
      }
      if (isNaN(rpm) || rpm <= 0) rpm = 1750;

      const ratio = D / d;
      const drivenRpm = rpm / ratio;

      let C = 0;
      let L = 0;
      let phi = 0;
      let wrapSmall = 180;
      let wrapLarge = 180;

      if (mode === 'findLength') {
        C = parseFloat(centerDistInput.value);
        if (isNaN(C) || C <= 0) C = isMetric ? 500 : 20;

        if (driveType === 'open') {
          // Check geometric possibility
          if (2 * C < (D - d)) C = (D - d) / 2 + 1;
          phi = Math.asin((D - d) / (2 * C));
          L = 2 * C + (Math.PI / 2) * (D + d) + Math.pow(D - d, 2) / (4 * C);
          wrapSmall = 180 - (2 * phi * 180 / Math.PI);
          wrapLarge = 180 + (2 * phi * 180 / Math.PI);
        } else {
          // Crossed drive
          if (2 * C < (D + d)) C = (D + d) / 2 + 1;
          phi = Math.asin((D + d) / (2 * C));
          L = 2 * C + (Math.PI / 2) * (D + d) + Math.pow(D + d, 2) / (4 * C);
          wrapSmall = 180 + (2 * phi * 180 / Math.PI);
          wrapLarge = wrapSmall;
        }

        resPrimaryVal.textContent = L.toFixed(2) + " " + u;
        resSecondaryVal.textContent = C.toFixed(2) + " " + u;
      } else {
        // Find Center Distance from known Length
        L = parseFloat(givenBeltLengthInput.value);
        if (isNaN(L) || L <= 0) L = isMetric ? 1600 : 64;

        if (driveType === 'open') {
          const B = L - (Math.PI / 2) * (D + d);
          const discriminant = Math.pow(B, 2) - 2 * Math.pow(D - d, 2);
          if (discriminant >= 0) {
            C = (B + Math.sqrt(discriminant)) / 4;
            phi = Math.asin((D - d) / (2 * C));
            wrapSmall = 180 - (2 * phi * 180 / Math.PI);
            wrapLarge = 180 + (2 * phi * 180 / Math.PI);
          } else {
            C = 0.55 * (D + d);
            wrapSmall = 140;
            wrapLarge = 220;
          }
        } else {
          const B = L - (Math.PI / 2) * (D + d);
          const discriminant = Math.pow(B, 2) - 2 * Math.pow(D + d, 2);
          if (discriminant >= 0) {
            C = (B + Math.sqrt(discriminant)) / 4;
            phi = Math.asin((D + d) / (2 * C));
            wrapSmall = 180 + (2 * phi * 180 / Math.PI);
            wrapLarge = wrapSmall;
          } else {
            C = 0.55 * (D + d);
            wrapSmall = 200;
            wrapLarge = 200;
          }
        }

        resPrimaryVal.textContent = C.toFixed(2) + " " + u;
        resSecondaryVal.textContent = L.toFixed(2) + " " + u;
      }

      // Linear speed (m/s or ft/min)
      // d is pitch diameter of small pulley, rpm is motor speed on small pulley
      let linearSpeed = 0;
      if (isMetric) {
        linearSpeed = (Math.PI * (d / 1000) * rpm) / 60; // m/s
      } else {
        linearSpeed = (Math.PI * (d / 12) * rpm); // ft/min
      }

      // Arc of contact factor (C_theta) approximation for V-belts
      let arcFactor = 1.0;
      if (wrapSmall < 180) {
        arcFactor = 1.0 - (180 - wrapSmall) * 0.003;
      }

      // Center distance rule of thumb: 0.55*(D+d) <= C <= 2*(D+d)
      const cMin = 0.55 * (D + d);
      const cMax = 2.0 * (D + d);
      let distStatus = "Optimal Engineering Range";
      let statusColor = "#166534";

      if (C < cMin) {
        distStatus = "Too Tight (C < 0.55(D+d))";
        statusColor = "#b45309";
      } else if (C > cMax) {
        distStatus = "Too Long (C > 2(D+d))";
        statusColor = "#b45309";
      }

      resRatio.textContent = ratio.toFixed(2) + ":1";
      resDrivenRpm.textContent = drivenRpm.toFixed(1) + " RPM";
      resWrapSmall.textContent = wrapSmall.toFixed(1) + "°";
      resWrapLarge.textContent = wrapLarge.toFixed(1) + "°";
      resBeltSpeed.textContent = linearSpeed.toFixed(2) + " " + spdUnit;
      resWrapFactor.textContent = arcFactor.toFixed(3);
      resDistStatus.textContent = distStatus;
      resDistStatus.style.color = statusColor;

      let notes = `<strong>Design Analysis:</strong> Center distance of <strong>${C.toFixed(1)} ${u}</strong> provides a small pulley wrap angle of <strong>${wrapSmall.toFixed(1)}&deg;</strong>. `;
      if (wrapSmall < 140) {
        notes += `<span style="color:#b45309;">Warning: Wrap angle is below 140&deg;. Consider increasing center distance or adding an idler pulley to prevent belt slippage.</span>`;
      } else {
        notes += `Arc of contact factor is <strong>${arcFactor.toFixed(3)}</strong>, ensuring efficient frictional power transfer.`;
      }
      beltNotesBox.innerHTML = notes;

      beltResultBox.style.display = 'block';
    }

    document.getElementById('calcBeltBtn').addEventListener('click', calculateBeltDrive);
    document.getElementById('resetBeltBtn').addEventListener('click', function() {
      setTimeout(calculateBeltDrive, 50);
    });

    window.addEventListener('DOMContentLoaded', calculateBeltDrive);
  </script>
</body>
</html>
"""

TOOL_2_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Conveyor Belt Speed Calculator | CEMA & ISO 5048 Material Flow Rate</title>
  <meta name="description" content="Calculate industrial conveyor belt speed, drive pulley RPM, bulk material throughput (tons/hr), and required motor drive power per CEMA and ISO 5048 standards.">
  <link rel="canonical" href="https://calchub.cloud/conveyor-belt-speed-calculator.html">
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
        "name": "Conveyor Belt Speed Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Bulk materials handling calculation tool computing conveyor belt linear velocity, drive drum rotational RPM, mass throughput capacity, and required drive power per CEMA standards.",
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
            "name": "How is conveyor belt linear speed calculated from drive pulley RPM?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Belt linear speed is derived from drive pulley circumference: v = (pi * D_eff * N) / 60 in metric (m/s), or v = (pi * D_eff * N) / 12 in imperial (ft/min), where D_eff is the effective drive drum diameter including pulley lagging and belt carcass thickness, and N is rotational speed in revolutions per minute (RPM)."
            }
          },
          {
            "@type": "Question",
            "name": "What is the relationship between conveyor belt speed and material throughput capacity?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Conveyor volumetric capacity is directly proportional to speed: Q_vol = A * v * 3600 (m^3/hr), where A is the cross-sectional surcharge load area determined by belt width, idler troughing angle (20, 35, or 45 degrees), and material angle of repose. Mass throughput is Q_mass = Q_vol * rho_bulk (metric tons per hour)."
            }
          },
          {
            "@type": "Question",
            "name": "What are maximum recommended belt speeds for various bulk materials?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Per CEMA standards: Fragile or dusty materials (grain, fine coal, sand) are typically limited to 1.5 - 2.5 m/s (300 - 500 ft/min) to prevent degradation and dust creation. Coarse ore, crushed rock, and gravel operate at 2.5 - 4.0 m/s (500 - 800 ft/min). Overland long-distance transport conveyors running iron ore or coal frequently operate at high speeds up to 6.0 - 8.5 m/s (1,200 - 1,700 ft/min)."
            }
          },
          {
            "@type": "Question",
            "name": "How does drive pulley lagging affect effective conveyor speed?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Rubber or ceramic pulley lagging increases the outer drum diameter by 10 mm to 25 mm (3/8 to 1 inch). Because linear speed is governed by the center line of the tensioned belt carcass: D_eff = D_shell + 2*t_lagging + t_belt. Neglecting lagging thickness underestimates actual belt velocity by 3% to 7%."
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
      <a href="mechanical.html">Mechanical &amp; Machine Design</a> &rsaquo;
      <span>Conveyor Belt Speed Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">CEMA 7th Edition &amp; ISO 5048 Bulk Material Standards</div>
          <h1 class="calc-title">Conveyor Belt Speed Calculator</h1>
          <p class="calc-tagline">Calculate industrial conveyor belt linear speed, drive drum rotational RPM, volumetric and mass throughput capacities, and required motor power.</p>
        </header>

        <div class="tool-card">
          <form id="conveyorCalcForm">
            <div class="calc-grid">
              <div class="form-group">
                <label for="speedCalcMode">Calculation Mode</label>
                <select id="speedCalcMode">
                  <option value="rpmToSpeed" selected>Calculate Belt Speed from Drive Pulley RPM</option>
                  <option value="speedToRpm">Calculate Required Drive RPM from Target Belt Speed</option>
                </select>
              </div>

              <div class="form-group">
                <label for="conveyorUnits">Engineering Units</label>
                <select id="conveyorUnits">
                  <option value="metric" selected>Metric (m/s, mm, t/h, kW)</option>
                  <option value="imperial">Imperial (ft/min, in, STPH, HP)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="pulleyDiam" id="lblPulleyDiam">Drive Pulley Shell Diameter [mm]</label>
                <input type="number" id="pulleyDiam" step="5" min="50" max="3000" value="500">
              </div>

              <div class="form-group">
                <label for="laggingThick" id="lblLaggingThick">Pulley Lagging Thickness [mm]</label>
                <input type="number" id="laggingThick" step="1" min="0" max="100" value="12">
              </div>

              <div class="form-group">
                <label for="beltThick" id="lblBeltThick">Conveyor Belt Thickness [mm]</label>
                <input type="number" id="beltThick" step="0.5" min="2" max="60" value="10">
              </div>

              <div class="form-group" id="grpPulleyRpm">
                <label for="pulleyRpm">Drive Pulley Rotational Speed [RPM]</label>
                <input type="number" id="pulleyRpm" step="1" min="1" max="1000" value="75">
              </div>

              <div class="form-group" id="grpTargetSpeed" style="display: none;">
                <label for="targetSpeed" id="lblTargetSpeed">Target Linear Belt Speed [m/s]</label>
                <input type="number" id="targetSpeed" step="0.1" min="0.1" max="15.0" value="2.0">
              </div>

              <div class="form-group">
                <label for="beltWidth" id="lblBeltWidth">Belt Width [mm]</label>
                <select id="beltWidth">
                  <option value="500">500 mm (20 in)</option>
                  <option value="650">650 mm (24 in)</option>
                  <option value="800">800 mm (30 in)</option>
                  <option value="1000" selected>1000 mm (36 in)</option>
                  <option value="1200">1200 mm (42 in)</option>
                  <option value="1400">1400 mm (48 in)</option>
                  <option value="1600">1600 mm (54 in)</option>
                  <option value="1800">1800 mm (60 in)</option>
                  <option value="2000">2000 mm (72 in)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="troughAngle">Idler Troughing Angle</label>
                <select id="troughAngle">
                  <option value="20">20&deg; Standard Trough (Flat or Light Material)</option>
                  <option value="35" selected>35&deg; Deep Trough (General Mining / Ore)</option>
                  <option value="45">45&deg; High Capacity Deep Trough (Gravel / Grain)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="bulkDensity" id="lblBulkDensity">Bulk Material Density [t/m³]</label>
                <input type="number" id="bulkDensity" step="0.05" min="0.2" max="5.0" value="1.6">
              </div>
            </div>

            <div class="calc-actions">
              <button type="button" id="calcConveyorBtn" class="btn btn-primary">Calculate Conveyor Dynamics</button>
              <button type="reset" id="resetConveyorBtn" class="btn btn-secondary">Reset Defaults</button>
            </div>
          </form>

          <div id="conveyorResultBox" class="results-container" style="display: none;">
            <h3>Conveyor Velocity & Throughput Results</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label" id="resSpeedPrimaryLabel">Linear Belt Speed</span>
                <span id="resBeltSpeedVal" class="result-value">-- m/s</span>
              </div>
              <div class="result-tile">
                <span class="result-label" id="resRpmSecondaryLabel">Drive Pulley Rotational Speed</span>
                <span id="resDriveRpmVal" class="result-value">-- RPM</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Effective Drum Diameter (D_eff)</span>
                <span id="resEffDiam" class="result-value">-- mm</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Volumetric Capacity</span>
                <span id="resVolCapacity" class="result-value">-- m³/h</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Mass Throughput Rate</span>
                <span id="resMassThroughput" class="result-value">-- t/h</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Surcharge Cross-Section Area</span>
                <span id="resLoadArea" class="result-value">-- m²</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Material Category Speed Limit</span>
                <span id="resSpeedRating" class="result-value">--</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Drive Motor Output Power Est.</span>
                <span id="resEstPower" class="result-value">-- kW</span>
              </div>
            </div>
            <div id="conveyorNotesBox" style="margin-top: 1rem; color: #1e40af; background: #eff6ff; border: 1px solid #bfdbfe; padding: 0.75rem; border-radius: 6px;"></div>
          </div>
        </div>

        <article class="article-body">
          <h2>Industrial Conveyor Belt Kinematics & Bulk Material Transport</h2>
          <p>Continuous belt conveyors represent the backbone of bulk materials handling, moving millions of tons of coal, copper ore, aggregates, cement clinker, agricultural grains, and port cargo worldwide every hour. Governed by the <strong>Conveyor Equipment Manufacturers Association (CEMA)</strong> and the International Organization for Standardization under <strong>ISO 5048</strong>, sizing a conveyor requires harmonizing linear belt velocity, pulley mechanical geometry, material trajectory kinetics, and drive powertrain torque.</p>

          <p>Operating a conveyor at improper belt speeds creates severe operational challenges. Excessive velocity causes severe particle degradation, fugitive dust clouds at transfer chutes, destructive material spillage, and rapid idler bearing failure. Conversely, running a belt too slowly necessitates wider, heavier belts and massive structural trusses to achieve the required tonnage, exponentially multiplying capital expenditure.</p>

          <h2>Drive Pulley Rotational Speed to Linear Velocity Formulations</h2>
          <p>The tangential linear velocity (\(v\)) of a conveyor belt is directly governed by the rotational frequency of the drive pulley drum and its effective pitch radius:</p>

          <div class="formula-box">
            $$v = \frac{\pi \cdot D_{\text{eff}} \cdot N}{60 \times 1000} \quad [\text{m/s}] \quad \Longleftrightarrow \quad v = \frac{\pi \cdot D_{\text{eff}} \cdot N}{12} \quad [\text{ft/min}]$$
          </div>

          <p>Where:</p>
          <ul>
            <li><strong>\(v\)</strong>: Linear belt travel speed, expressed in meters per second (\(\text{m/s}\)) or feet per minute (\(\text{ft/min}\)).</li>
            <li><strong>\(N\)</strong>: Rotational speed of the drive pulley shaft, in revolutions per minute (\(\text{RPM}\)).</li>
            <li><strong>\(D_{\text{eff}}\)</strong>: Effective diameter of the drive drum (mm or inches), measured to the neutral bending center line of the belt carcass.</li>
          </ul>

          <p>In precision engineering design, the bare steel pulley shell diameter (\(D_{\text{shell}}\)) must be modified to account for bonded rubber/ceramic lagging (\(t_{\text{lag}}\)) and the belt carcass thickness (\(t_{\text{belt}}\)):</p>

          <div class="formula-box">
            $$D_{\text{eff}} = D_{\text{shell}} + 2 \cdot t_{\text{lag}} + t_{\text{belt}}$$
          </div>

          <p>Overlooking lagging thickness (typically 12 mm to 20 mm) and heavy multi-ply textile or steel-cord belt thickness (10 mm to 25 mm) introduces an error of up to 8% in belt speed, gear reducer output calculations, and scale calibration.</p>

          <h2>Volumetric Load Capacity & Surcharge Cross-Section Area</h2>
          <p>Under continuous steady-state loading, the volumetric discharge capacity (\(Q_{\text{vol}}\)) traversing the conveyor is the product of the cross-sectional area of the material load (\(A\)) and linear belt velocity (\(v\)):</p>

          <div class="formula-box">
            $$Q_{\text{vol}} = 3600 \cdot A \cdot v \quad [\text{m}^3/\text{hr}] \quad \Longleftrightarrow \quad Q_{\text{vol}} = 60 \cdot A \cdot v \quad [\text{ft}^3/\text{hr}]$$
          </div>

          <p>The cross-sectional area (\(A\)) on a standard 3-roll troughed belt consists of two geometric zones per CEMA Chapter 4:</p>
          <ol>
            <li><strong>Trapezoidal Trough Area (\(A_{\text{trough}}\)):</strong> The material contained within the lower channel formed by the inclined side idlers (troughing angles \(\beta = 20^\circ, 35^\circ,\) or \(45^\circ\)).</li>
            <li><strong>Circular Surcharge Area (\(A_{\text{surch}}\)):</strong> The heaped parabolic crown resting above the trapezoid, bounded by the material's dynamic angle of surcharge (\(\alpha\), typically 5&deg; to 15&deg; shallower than the static angle of repose due to conveyor vibration).</li>
          </ol>

          <div class="formula-box">
            $$A_{\text{total}} = A_{\text{trough}} + A_{\text{surch}} \approx k_{\text{trough}} \cdot \left(0.9 \cdot W - 0.05\right)^2$$
          </div>

          <p>Where \(W\) is belt width in meters, and \(k_{\text{trough}}\) is an empirical shape coefficient (typically 0.11 for 20&deg; idlers, 0.135 for 35&deg; idlers, and 0.155 for 45&deg; idlers with a 20&deg; surcharge angle).</p>

          <h2>Mass Throughput Capacity Calculations</h2>
          <p>Multiplying volumetric flow by the material's bulk density (\(\rho_{\text{bulk}}\)) yields the commercial mass throughput rate (\(Q_{\text{mass}}\)):</p>

          <div class="formula-box">
            $$Q_{\text{mass}} = Q_{\text{vol}} \cdot \rho_{\text{bulk}} \quad [\text{metric tons/hour}] \quad \Longleftrightarrow \quad Q_{\text{STPH}} = \frac{Q_{\text{vol}} \cdot \rho_{\text{bulk}}}{2000} \quad [\text{short tons/hour}]$$
          </div>

          <h2>CEMA Recommended Maximum Conveyor Belt Speeds</h2>
          <p>Allowable belt speeds depend on material abrasiveness, lump sizing, friability, windage, and belt width. As standardized in CEMA Table 4-1:</p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Bulk Material Characteristics</th>
                <th>Typical Materials</th>
                <th>Belt Width &lt; 800 mm</th>
                <th>Belt Width 800 &ndash; 1400 mm</th>
                <th>Belt Width &gt; 1400 mm</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Dusty, light, or fine grains</td>
                <td>Flour, cement, grain, fly ash</td>
                <td>1.5 &ndash; 2.0 m/s (300 fpm)</td>
                <td>2.0 &ndash; 2.5 m/s (400 fpm)</td>
                <td>2.5 &ndash; 3.0 m/s (500 fpm)</td>
              </tr>
              <tr>
                <td>Moderately abrasive, mixed lumps</td>
                <td>Bituminous coal, crushed limestone</td>
                <td>2.0 &ndash; 2.5 m/s (450 fpm)</td>
                <td>2.5 &ndash; 3.5 m/s (600 fpm)</td>
                <td>3.5 &ndash; 4.5 m/s (800 fpm)</td>
              </tr>
              <tr>
                <td>Heavy, sharp, abrasive crushed ore</td>
                <td>Iron ore, granite, trap rock</td>
                <td>1.8 &ndash; 2.2 m/s (400 fpm)</td>
                <td>2.2 &ndash; 3.0 m/s (550 fpm)</td>
                <td>3.0 &ndash; 4.0 m/s (750 fpm)</td>
              </tr>
              <tr>
                <td>Overland long-distance transport</td>
                <td>Run-of-mine coal, bauxite</td>
                <td>N/A</td>
                <td>4.0 &ndash; 6.0 m/s (1000 fpm)</td>
                <td>6.0 &ndash; 8.5 m/s (1500 fpm)</td>
              </tr>
            </tbody>
          </table>

          <h2>Drive Motor Power Estimation per ISO 5048</h2>
          <p>Total mechanical power required at the drive pulley shaft (\(P_{\text{shaft}}\)) overcomes primary friction resistance (\(F_H\)), secondary resistance (\(F_N\)), and lift resistance (\(F_{St}\)):</p>

          <div class="formula-box">
            $$P_{\text{shaft}} = \frac{T_e \cdot v}{1000} \quad [\text{kW}] \quad \Longleftrightarrow \quad P_{\text{motor}} = \frac{P_{\text{shaft}}}{\eta_{\text{drive}}}$$
          </div>

          <p>Where \(T_e\) represents effective belt tension (Newtons), \(v\) is belt speed (m/s), and \(\eta_{\text{drive}}\) is overall powertrain efficiency (typically 0.88 to 0.94 for helical bevel reducers and flexible couplings).</p>

          <div class="worked-example-card">
            <h3>Step-by-Step Worked Case Study: Crushed Copper Ore Feed Conveyor</h3>
            <p><strong>Design Scenario:</strong> An engineer is sizing the drive pulley RPM and checking throughput capacity for a copper concentrator plant feed conveyor:</p>
            <ul>
              <li>Belt width: \(W = 1000\text{ mm}\) (36 inches).</li>
              <li>Drive drum bare shell diameter: \(D_{\text{shell}} = 500\text{ mm}\).</li>
              <li>Ceramic diamond lagging thickness: \(t_{\text{lag}} = 12\text{ mm}\).</li>
              <li>Steel-cord belt thickness: \(t_{\text{belt}} = 14\text{ mm}\).</li>
              <li>Drive shaft speed: \(N = 75\text{ RPM}\).</li>
              <li>Idler troughing: 35&deg; 3-roll idlers (\(k_{\text{trough}} = 0.135\)).</li>
              <li>Crushed copper ore bulk density: \(\rho = 1.65\text{ t/m}^3\).</li>
            </ul>

            <p><strong>Step 1: Compute effective pulley diameter (\(D_{\text{eff}}\))</strong></p>
            <div class="formula-box">
              $$D_{\text{eff}} = 500 + 2(12) + 14 = 500 + 24 + 14 = 538\text{ mm} = 0.538\text{ m}$$
            </div>

            <p><strong>Step 2: Calculate linear belt velocity (\(v\))</strong></p>
            <div class="formula-box">
              $$v = \frac{\pi \cdot 0.538 \cdot 75}{60} = \frac{126.76}{60} = 2.11\text{ m/s} \quad (415\text{ ft/min})$$
            </div>

            <p><strong>Step 3: Calculate surcharge load cross-sectional area (\(A\))</strong></p>
            <div class="formula-box">
              $$A \approx 0.135 \cdot (0.9 \cdot 1.0 - 0.05)^2 = 0.135 \cdot (0.85)^2 = 0.135 \cdot 0.7225 = 0.0975\text{ m}^2$$
            </div>

            <p><strong>Step 4: Determine volumetric capacity (\(Q_{\text{vol}}\))</strong></p>
            <div class="formula-box">
              $$Q_{\text{vol}} = 3600 \cdot 0.0975 \cdot 2.11 = 740.6\text{ m}^3/\text{hr}$$
            </div>

            <p><strong>Step 5: Determine mass throughput capacity (\(Q_{\text{mass}}\))</strong></p>
            <div class="formula-box">
              $$Q_{\text{mass}} = 740.6 \times 1.65\text{ t/m}^3 = 1222.0\text{ metric tons/hr}$$
            </div>
            <p><strong>Engineering Conclusion:</strong> Operating at 2.11 m/s, the conveyor easily delivers the targeted <strong>1,222 metric tons/hour</strong> while remaining well within the CEMA recommended maximum of 2.8 m/s for crushed abrasive ore on a 1000 mm belt.</p>
          </div>

          <h2>Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3>How do idler troughing angles affect conveyor load capacity?</h3>
            <p>Deepening the idler troughing angle increases cross-sectional capacity without requiring a wider belt. Upgrading from standard 20&deg; idlers to 35&deg; idlers increases cross-sectional surcharge area by approximately 25% to 30%. Deep 45&deg; idlers provide up to 45% more capacity compared to 20&deg; idlers, but require highly flexible transverse belt constructions (such as high-transverse-flex nylon fabrics) to ensure proper trough contact and belt tracking when running empty.</p>
          </div>

          <div class="faq-item">
            <h3>Why does conveyor belt speed affect transfer chute wear?</h3>
            <p>The kinetic energy of falling bulk material entering a transfer chute is proportional to the square of its discharge velocity (\(KE = \frac{1}{2}m v^2\)). High belt velocities impart high initial horizontal momentum to discharged rocks, causing severe impact against wear liners and violent turbulence in the loading skirtboard. Transfer chute geometry must be engineered using rock boxes, curved curved hoods, and curved spoon deflectors to match material exit velocity to the receiving belt speed.</p>
          </div>

          <div class="faq-item">
            <h3>What causes belt slip on the drive pulley and how can it be resolved?</h3>
            <p>Belt slip occurs when the tension ratio (\(T_1 / T_2\)) exceeds the frictional traction limit \(e^{\mu \theta}\). Common causes include inadequate gravity take-up counterweight, worn-down smooth steel pulley surfaces, water/slurry ingress, or seized idler rolls. Slippage can be mitigated by installing high-friction ceramic lagging (\(\mu \approx 0.40\)), increasing pulley wrap angle using a snub pulley, or increasing counterweight take-up tension.</p>
          </div>

          <div class="faq-item">
            <h3>When should variable frequency drives (VFDs) be used on conveyor systems?</h3>
            <p>VFDs provide controlled acceleration ramps (S-curves) over 30 to 90 seconds, preventing destructive dynamic tension waves (stress shockwaves) from snapping belt splices during starting. VFDs also enable closed-loop belt speed modulation to match incoming surge hopper levels, maintaining a constant full cross-sectional bed profile at reduced speeds to dramatically minimize transfer point dust and reduce power consumption during low-production shifts.</p>
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
        <li><a href="mechanical.html">Mechanical</a></li>
        <li><a href="ohms-law-calculator.html">Ohm's Law</a></li>
        <li><a href="sitemap.xml">Sitemap</a></li>
      </ul>
    </div>
  </footer>

  <script>
    const speedCalcModeSelect = document.getElementById('speedCalcMode');
    const conveyorUnitsSelect = document.getElementById('conveyorUnits');
    const pulleyDiamInput = document.getElementById('pulleyDiam');
    const laggingThickInput = document.getElementById('laggingThick');
    const beltThickInput = document.getElementById('beltThick');
    const pulleyRpmInput = document.getElementById('pulleyRpm');
    const targetSpeedInput = document.getElementById('targetSpeed');
    const beltWidthSelect = document.getElementById('beltWidth');
    const troughAngleSelect = document.getElementById('troughAngle');
    const bulkDensityInput = document.getElementById('bulkDensity');

    const lblPulleyDiam = document.getElementById('lblPulleyDiam');
    const lblLaggingThick = document.getElementById('lblLaggingThick');
    const lblBeltThick = document.getElementById('lblBeltThick');
    const lblTargetSpeed = document.getElementById('lblTargetSpeed');
    const lblBeltWidth = document.getElementById('lblBeltWidth');
    const lblBulkDensity = document.getElementById('lblBulkDensity');

    const grpPulleyRpm = document.getElementById('grpPulleyRpm');
    const grpTargetSpeed = document.getElementById('grpTargetSpeed');

    const conveyorResultBox = document.getElementById('conveyorResultBox');
    const resSpeedPrimaryLabel = document.getElementById('resSpeedPrimaryLabel');
    const resRpmSecondaryLabel = document.getElementById('resRpmSecondaryLabel');
    const resBeltSpeedVal = document.getElementById('resBeltSpeedVal');
    const resDriveRpmVal = document.getElementById('resDriveRpmVal');
    const resEffDiam = document.getElementById('resEffDiam');
    const resVolCapacity = document.getElementById('resVolCapacity');
    const resMassThroughput = document.getElementById('resMassThroughput');
    const resLoadArea = document.getElementById('resLoadArea');
    const resSpeedRating = document.getElementById('resSpeedRating');
    const resEstPower = document.getElementById('resEstPower');
    const conveyorNotesBox = document.getElementById('conveyorNotesBox');

    speedCalcModeSelect.addEventListener('change', function() {
      if (this.value === 'rpmToSpeed') {
        grpPulleyRpm.style.display = 'block';
        grpTargetSpeed.style.display = 'none';
        resSpeedPrimaryLabel.textContent = "Linear Belt Speed";
        resRpmSecondaryLabel.textContent = "Drive Pulley Rotational Speed";
      } else {
        grpPulleyRpm.style.display = 'none';
        grpTargetSpeed.style.display = 'block';
        resSpeedPrimaryLabel.textContent = "Required Drive Pulley RPM";
        resRpmSecondaryLabel.textContent = "Specified Target Belt Speed";
      }
      calculateConveyor();
    });

    conveyorUnitsSelect.addEventListener('change', function() {
      const isMetric = this.value === 'metric';
      if (isMetric) {
        lblPulleyDiam.textContent = "Drive Pulley Shell Diameter [mm]";
        lblLaggingThick.textContent = "Pulley Lagging Thickness [mm]";
        lblBeltThick.textContent = "Conveyor Belt Thickness [mm]";
        lblTargetSpeed.textContent = "Target Linear Belt Speed [m/s]";
        lblBulkDensity.textContent = "Bulk Material Density [t/m³]";
        pulleyDiamInput.value = 500;
        laggingThickInput.value = 12;
        beltThickInput.value = 10;
        targetSpeedInput.value = 2.0;
        bulkDensityInput.value = 1.6;
      } else {
        lblPulleyDiam.textContent = "Drive Pulley Shell Diameter [in]";
        lblLaggingThick.textContent = "Pulley Lagging Thickness [in]";
        lblBeltThick.textContent = "Conveyor Belt Thickness [in]";
        lblTargetSpeed.textContent = "Target Linear Belt Speed [ft/min]";
        lblBulkDensity.textContent = "Bulk Material Density [lbs/ft³]";
        pulleyDiamInput.value = 20.0;
        laggingThickInput.value = 0.5;
        beltThickInput.value = 0.4;
        targetSpeedInput.value = 400;
        bulkDensityInput.value = 100;
      }
      calculateConveyor();
    });

    function calculateConveyor() {
      const mode = speedCalcModeSelect.value;
      const isMetric = conveyorUnitsSelect.value === 'metric';
      const uDim = isMetric ? 'mm' : 'in';
      const uSpd = isMetric ? 'm/s' : 'ft/min';
      const uCapVol = isMetric ? 'm³/h' : 'ft³/h';
      const uCapMass = isMetric ? 't/h' : 'STPH';
      const uArea = isMetric ? 'm²' : 'ft²';
      const uPwr = isMetric ? 'kW' : 'HP';

      let D_shell = parseFloat(pulleyDiamInput.value);
      let t_lag = parseFloat(laggingThickInput.value);
      let t_belt = parseFloat(beltThickInput.value);
      if (isNaN(D_shell) || D_shell <= 0) D_shell = isMetric ? 500 : 20;
      if (isNaN(t_lag) || t_lag < 0) t_lag = 0;
      if (isNaN(t_belt) || t_belt < 0) t_belt = 0;

      const D_eff = D_shell + 2 * t_lag + t_belt;

      let v = 0; // m/s (metric) or ft/min (imperial)
      let rpm = 0;

      if (mode === 'rpmToSpeed') {
        rpm = parseFloat(pulleyRpmInput.value);
        if (isNaN(rpm) || rpm <= 0) rpm = 75;

        if (isMetric) {
          v = (Math.PI * (D_eff / 1000) * rpm) / 60; // m/s
        } else {
          v = (Math.PI * (D_eff / 12) * rpm); // ft/min
        }
        resBeltSpeedVal.textContent = v.toFixed(2) + " " + uSpd;
        resDriveRpmVal.textContent = rpm.toFixed(1) + " RPM";
      } else {
        v = parseFloat(targetSpeedInput.value);
        if (isNaN(v) || v <= 0) v = isMetric ? 2.0 : 400;

        if (isMetric) {
          rpm = (v * 60) / (Math.PI * (D_eff / 1000));
        } else {
          rpm = (v * 12) / (Math.PI * D_eff);
        }
        resBeltSpeedVal.textContent = rpm.toFixed(1) + " RPM";
        resDriveRpmVal.textContent = v.toFixed(2) + " " + uSpd;
      }

      // Convert v to m/s for standardized area calculations
      const v_mps = isMetric ? v : (v * 0.00508);

      // Belt width in meters
      const widthValMm = parseFloat(beltWidthSelect.value);
      const widthMeters = widthValMm / 1000;

      // Trough coefficient based on trough angle
      const troughDeg = parseInt(troughAngleSelect.value, 10);
      let k_trough = 0.135;
      if (troughDeg === 20) k_trough = 0.110;
      else if (troughDeg === 45) k_trough = 0.155;

      // Effective load cross sectional area A (m^2)
      const A_m2 = k_trough * Math.pow(Math.max(0.2, 0.9 * widthMeters - 0.05), 2);
      const A_disp = isMetric ? A_m2 : (A_m2 * 10.7639);

      // Volumetric capacity Q_vol
      const Q_vol_m3h = 3600 * A_m2 * v_mps;
      const Q_vol_disp = isMetric ? Q_vol_m3h : (Q_vol_m3h * 35.3147);

      // Mass throughput Q_mass
      let density = parseFloat(bulkDensityInput.value);
      if (isNaN(density) || density <= 0) density = isMetric ? 1.6 : 100;

      let Q_mass_th = 0;
      if (isMetric) {
        Q_mass_th = Q_vol_m3h * density; // t/h
      } else {
        // density in lbs/ft^3, Q_vol in ft^3/h -> lbs/h / 2000 = STPH
        Q_mass_th = (Q_vol_disp * density) / 2000;
      }

      // Estimated drive power (rough CEMA approximation: ~0.025 kW per t/h per 100m horizontal)
      // Assuming 100m conveyor baseline
      const estKw = Math.max(2.2, Q_mass_th * 0.035 * (v_mps / 2.0));
      const estPwrDisp = isMetric ? estKw : (estKw * 1.34102);

      // Material speed rating check per CEMA
      let speedStatus = "Normal Operating Speed";
      let statusColor = "#166534";
      if (v_mps > 4.5) {
        speedStatus = "High Speed (Overland / Non-Dusty Material)";
        statusColor = "#b45309";
      } else if (v_mps < 1.0) {
        speedStatus = "Low Speed (Feeder / Delicate Material)";
      }

      resEffDiam.textContent = D_eff.toFixed(1) + " " + uDim;
      resVolCapacity.textContent = Q_vol_disp.toFixed(1) + " " + uCapVol;
      resMassThroughput.textContent = Q_mass_th.toFixed(1) + " " + uCapMass;
      resLoadArea.textContent = A_disp.toFixed(4) + " " + uArea;
      resSpeedRating.textContent = speedStatus;
      resSpeedRating.style.color = statusColor;
      resEstPower.textContent = estPwrDisp.toFixed(1) + " " + uPwr;

      conveyorNotesBox.innerHTML = `<strong>CEMA Capacity Analysis:</strong> At <strong>${v_mps.toFixed(2)} m/s</strong> on a ${widthValMm} mm belt with ${troughDeg}&deg; idlers, the conveyor achieves <strong>${Q_mass_th.toFixed(1)} ${uCapMass}</strong> throughput. Drive drum effective pitch diameter is <strong>${D_eff.toFixed(1)} ${uDim}</strong>.`;

      conveyorResultBox.style.display = 'block';
    }

    document.getElementById('calcConveyorBtn').addEventListener('click', calculateConveyor);
    document.getElementById('resetConveyorBtn').addEventListener('click', function() {
      setTimeout(calculateConveyor, 50);
    });

    window.addEventListener('DOMContentLoaded', calculateConveyor);
  </script>
</body>
</html>
"""

def main():
    target_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    file1 = os.path.join(target_dir, "belt-length-calculator.html")
    with open(file1, "w", encoding="utf-8") as f:
        f.write(TOOL_1_HTML)
    print(f"[PASS] belt-length-calculator.html generated successfully!")

    file2 = os.path.join(target_dir, "conveyor-belt-speed-calculator.html")
    with open(file2, "w", encoding="utf-8") as f:
        f.write(TOOL_2_HTML)
    print(f"[PASS] conveyor-belt-speed-calculator.html generated successfully!")

if __name__ == "__main__":
    main()
