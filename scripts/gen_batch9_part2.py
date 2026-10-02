# -*- coding: utf-8 -*-
"""
Script to generate Batch 9 Part 2 tools:
3. cutting-speed-calculator.html
4. feed-rate-calculator.html
"""
import os

TOOL_3_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cutting Speed Calculator | CNC Machining RPM & Surface Speed</title>
  <meta name="description" content="Calculate CNC cutting speed (Vc in m/min and SFM), spindle rotational speed (RPM), and Taylor tool life for turning, milling, and drilling per ISO 3685 and ASME machining standards.">
  <link rel="canonical" href="https://calchub.cloud/cutting-speed-calculator.html">
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
        "name": "Cutting Speed Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "CNC machining speeds and feeds calculation engine computing linear surface cutting speed (Vc/SFM), spindle RPM, and material removal rates per ISO 3685.",
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
            "name": "What is the formula for cutting speed (Vc) in machining?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In metric units: Vc = (pi * D * N) / 1000 [m/min], where D is workpiece or cutter diameter in millimeters, and N is spindle speed in RPM. In imperial units: Vc = (pi * D * N) / 12 [SFM - Surface Feet per Minute], where D is in inches."
            }
          },
          {
            "@type": "Question",
            "name": "How do you calculate CNC spindle speed (RPM) from surface speed?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Solving for RPM yields: Metric N = (1000 * Vc) / (pi * D). Imperial N = (12 * Vc) / (pi * D) approx (3.82 * Vc) / D, where Vc is recommended surface feet per minute (SFM) and D is tool or part diameter in inches."
            }
          },
          {
            "@type": "Question",
            "name": "What is Taylor's Tool Life Equation and how is it used?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Taylor's Tool Life law states: Vc * T^n = C, where Vc is cutting speed, T is tool endurance life in minutes, n is the Taylor exponent (0.10 to 0.15 for HSS, 0.20 to 0.35 for cemented carbide, 0.40 to 0.60 for ceramic/cBN), and C is the reference cutting speed for a 1-minute tool life. Increasing Vc decreases tool life exponentially."
            }
          },
          {
            "@type": "Question",
            "name": "Why does cutting speed differ between workpiece materials?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Material machinability depends on hardness, thermal conductivity, abrasive inclusions, and shear yield strength. Free-machining aluminum 6061 can run at high surface speeds (300 - 1000 m/min / 1000 - 3300 SFM), whereas nickel superalloys (Inconel 718) and titanium alloys have low thermal conductivity, concentrating extreme heat at the cutting edge and requiring low speeds (25 - 60 m/min / 80 - 200 SFM) to prevent catastrophic edge deformation."
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
      <span>Cutting Speed Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">ISO 3685 &amp; ASME B94 Machining Standards</div>
          <h1 class="calc-title">Cutting Speed Calculator</h1>
          <p class="calc-tagline">Calculate CNC surface speed (Vc/SFM), spindle rotational speed (RPM), material removal rates, and Taylor tool life across milling, turning, and drilling operations.</p>
        </header>

        <div class="tool-card">
          <form id="cuttingCalcForm">
            <div class="calc-grid">
              <div class="form-group">
                <label for="machiningOperation">Machining Operation</label>
                <select id="machiningOperation">
                  <option value="milling" selected>CNC Milling (Rotating Cutter, Fixed Part)</option>
                  <option value="turning">CNC Turning / Lathe (Rotating Part, Fixed Tool)</option>
                  <option value="drilling">Drilling (Rotating Drill Bit)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="speedMode">Calculation Objective</label>
                <select id="speedMode">
                  <option value="findRpm" selected>Calculate Spindle RPM from Target Surface Speed</option>
                  <option value="findSpeed">Calculate Surface Speed from Given Spindle RPM</option>
                </select>
              </div>

              <div class="form-group">
                <label for="speedUnits">Engineering Units</label>
                <select id="speedUnits">
                  <option value="metric" selected>Metric (m/min, mm, cm³/min)</option>
                  <option value="imperial">Imperial (SFM, inches, in³/min)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="workMaterial">Workpiece Material Preset</label>
                <select id="workMaterial">
                  <option value="custom">Custom Surface Speed...</option>
                  <option value="al6061" selected>Aluminum Alloys (6061-T6, 7075)</option>
                  <option value="steel1018">Low-Carbon Mild Steel (AISI 1018/1020)</option>
                  <option value="steel4140">Alloy Steel Prehardened (AISI 4140/4340)</option>
                  <option value="ss304">Austenitic Stainless Steel (304 / 316)</option>
                  <option value="castIron">Gray Cast Iron (Class 30/40)</option>
                  <option value="titanium">Titanium Alloy (Ti-6Al-4V Grade 5)</option>
                  <option value="inconel">Nickel Superalloy (Inconel 718)</option>
                  <option value="brass">Free-Cutting Brass (C36000)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="toolMaterial">Cutting Tool Material</label>
                <select id="toolMaterial">
                  <option value="carbide" selected>Coated Solid Carbide (TiAlN / AlCrN)</option>
                  <option value="carbideUncoated">Uncoated Micrograin Carbide</option>
                  <option value="hss">High-Speed Steel (HSS / HSS-Co M42)</option>
                  <option value="ceramic">Ceramic / cBN (Hard Machining)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="toolDiam" id="lblToolDiam">Tool / Part Diameter D [mm]</label>
                <input type="number" id="toolDiam" step="0.5" min="0.5" max="2000" value="12.0">
              </div>

              <div class="form-group" id="grpTargetSpeed">
                <label for="targetVc" id="lblTargetVc">Target Surface Cutting Speed Vc [m/min]</label>
                <input type="number" id="targetVc" step="5" min="5" max="3000" value="250">
              </div>

              <div class="form-group" id="grpInputRpm" style="display: none;">
                <label for="inputRpm">Spindle Speed N [RPM]</label>
                <input type="number" id="inputRpm" step="50" min="10" max="60000" value="6630">
              </div>

              <div class="form-group">
                <label for="axialDoc" id="lblAxialDoc">Axial Depth of Cut (ap) [mm]</label>
                <input type="number" id="axialDoc" step="0.5" min="0.1" max="100" value="3.0">
              </div>

              <div class="form-group">
                <label for="radialDoc" id="lblRadialDoc">Radial Width of Cut (ae) [mm]</label>
                <input type="number" id="radialDoc" step="0.5" min="0.1" max="500" value="6.0">
              </div>
            </div>

            <div class="calc-actions">
              <button type="button" id="calcSpeedBtn" class="btn btn-primary">Calculate Machining Speed</button>
              <button type="reset" id="resetSpeedBtn" class="btn btn-secondary">Reset Defaults</button>
            </div>
          </form>

          <div id="speedResultBox" class="results-container" style="display: none;">
            <h3>Machining Speeds & Cutting Performance Results</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label" id="resPrimarySpeedLabel">Calculated Spindle Speed</span>
                <span id="resSpindleRpm" class="result-value">-- RPM</span>
              </div>
              <div class="result-tile">
                <span class="result-label" id="resSecondarySpeedLabel">Surface Cutting Speed (Vc)</span>
                <span id="resSurfaceSpeed" class="result-value">-- m/min</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Equivalent Imperial Speed</span>
                <span id="resAltSpeed" class="result-value">-- SFM</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Angular Velocity (&omega;)</span>
                <span id="resAngularVel" class="result-value">-- rad/s</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Radial Engagement Ratio</span>
                <span id="resRadialEngagement" class="result-value">-- %</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Taylor 15-min Tool Life Speed</span>
                <span id="resTaylorSpeed" class="result-value">-- m/min</span>
              </div>
            </div>
            <div id="speedNotesBox" style="margin-top: 1rem; color: #1e40af; background: #eff6ff; border: 1px solid #bfdbfe; padding: 0.75rem; border-radius: 6px;"></div>
          </div>
        </div>

        <article class="article-body">
          <h2>Machining Mechanics & Surface Cutting Velocity Fundamentals</h2>
          <p>In subtractive manufacturing and computer numerical control (CNC) machining, <strong>cutting speed</strong> (\(V_c\)) defines the instantaneous linear relative velocity between the cutting edge of a tool and the workpiece surface passing beneath it. Whether executing precision turning on a multi-axis lathe, high-speed end milling in aerospace aluminum, or deep hole drilling in titanium forgings, cutting speed dictates tool life, thermal generation, surface finish roughness (\(Ra\)), and machine tool spindle longevity.</p>

          <p>Operating outside optimal surface speed bands causes rapid tool degradation. Insufficient cutting velocity produces <strong>built-up edge (BUE)</strong>—a phenomenon where workpiece material pressure-welds onto the cutting edge, dulling the tool and tearing the machined surface. Conversely, excessive velocity elevates cutting temperatures beyond 900&deg;C (1,650&deg;F), triggering rapid thermal softening, crater wear on the tool rake face, chemical diffusion wear, and catastrophic thermal shock chipping.</p>

          <h2>Mathematical Formulations for Cutting Speed and Spindle RPM</h2>
          <p>Cutting speed represents the circumference traversed by the tool or workpiece per unit time. Because rotating spindle speeds are governed in revolutions per minute (RPM) while cutting speed is standardized in linear units, conversion factors must reconcile geometry and time.</p>

          <h3>Metric System Formulations (m/min and mm)</h3>
          <p>When tool diameter (\(D\)) is specified in millimeters, the circumference in meters is \((\pi \cdot D) / 1000\). The linear surface speed (\(V_c\)) in meters per minute is:</p>

          <div class="formula-box">
            $$V_c = \frac{\pi \cdot D \cdot N}{1000} \quad [\text{m/min}]$$
          </div>

          <p>Solving for spindle rotational frequency (\(N\)) in revolutions per minute:</p>

          <div class="formula-box">
            $$N = \frac{1000 \cdot V_c}{\pi \cdot D} \approx \frac{318.3 \cdot V_c}{D} \quad [\text{RPM}]$$
          </div>

          <h3>Imperial System Formulations (SFM and inches)</h3>
          <p>In North American machine shops, surface cutting speed is measured in <strong>Surface Feet per Minute (SFM)</strong> and diameters are measured in inches. Because 1 foot contains 12 inches:</p>

          <div class="formula-box">
            $$V_c = \frac{\pi \cdot D \cdot N}{12} \quad [\text{SFM}]$$
          </div>

          <p>Solving for spindle RPM:</p>

          <div class="formula-box">
            $$N = \frac{12 \cdot V_c}{\pi \cdot D} \approx \frac{3.82 \cdot V_c}{D} \quad [\text{RPM}]$$
          </div>

          <h2>Taylor's Tool Life Equation & Thermal Wear Mechanics</h2>
          <p>The mathematical relationship governing cutting speed and tool wear was formulated by Frederick Winslow Taylor and standardized under <strong>ISO 3685</strong>. The empirical equation relates linear cutting speed (\(V_c\)) to tool endurance life (\(T\)) in minutes:</p>

          <div class="formula-box">
            $$V_c \cdot T^n = C \quad \Longleftrightarrow \quad T = \left( \frac{C}{V_c} \right)^{1/n}$$
          </div>

          <p>Where:</p>
          <ul>
            <li><strong>\(T\)</strong>: Tool life in minutes until flank wear land reaches the critical threshold (\(VB = 0.3\text{ mm}\)).</li>
            <li><strong>\(n\)</strong>: Taylor tool material exponent, reflecting thermal sensitivity:
              <ul>
                <li>High-Speed Steel (HSS): \(n \approx 0.10 - 0.15\) (High thermal sensitivity; 10% speed increase cuts tool life in half).</li>
                <li>Cemented Tungsten Carbide: \(n \approx 0.20 - 0.35\) (Moderate thermal resilience).</li>
                <li>Silicon Nitride / Whisker Ceramics: \(n \approx 0.40 - 0.55\).</li>
                <li>Polycrystalline Cubic Boron Nitride (cBN): \(n \approx 0.50 - 0.70\).</li>
              </ul>
            </li>
            <li><strong>\(C\)</strong>: Machining constant, representing the theoretical cutting speed that would yield exactly 1 minute of tool life.</li>
          </ul>

          <h2>Reference Cutting Speeds Across Engineering Materials</h2>
          <p>Recommended starting surface speeds vary dramatically across ISO material groups (P, M, K, N, S, H) depending on cutting tool substrate and multi-layer PVD/CVD coatings:</p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>ISO Material Group</th>
                <th>Workpiece Material</th>
                <th>HSS Tooling (m/min | SFM)</th>
                <th>Coated Carbide (m/min | SFM)</th>
                <th>cBN / Ceramic (m/min | SFM)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>ISO N (Non-Ferrous)</strong></td>
                <td>Aluminum 6061-T6 / 7075</td>
                <td>80 &ndash; 150 | 250 &ndash; 500</td>
                <td>300 &ndash; 1000 | 1000 &ndash; 3300</td>
                <td>1200+ | 4000+ (PCD)</td>
              </tr>
              <tr>
                <td><strong>ISO P (Carbon Steels)</strong></td>
                <td>AISI 1018 / 1045 Mild Steel</td>
                <td>25 &ndash; 40 | 80 &ndash; 130</td>
                <td>180 &ndash; 320 | 600 &ndash; 1050</td>
                <td>350 &ndash; 600 | 1150 &ndash; 2000</td>
              </tr>
              <tr>
                <td><strong>ISO P (Alloy Steels)</strong></td>
                <td>AISI 4140 / 4340 (30 HRC)</td>
                <td>18 &ndash; 28 | 60 &ndash; 90</td>
                <td>120 &ndash; 220 | 400 &ndash; 720</td>
                <td>250 &ndash; 450 | 800 &ndash; 1500</td>
              </tr>
              <tr>
                <td><strong>ISO M (Stainless)</strong></td>
                <td>Austenitic 304 / 316 Stainless</td>
                <td>12 &ndash; 20 | 40 &ndash; 65</td>
                <td>100 &ndash; 180 | 330 &ndash; 600</td>
                <td>150 &ndash; 250 | 500 &ndash; 820</td>
              </tr>
              <tr>
                <td><strong>ISO K (Cast Irons)</strong></td>
                <td>Class 35 Gray Cast Iron</td>
                <td>20 &ndash; 35 | 65 &ndash; 115</td>
                <td>150 &ndash; 280 | 500 &ndash; 920</td>
                <td>400 &ndash; 800 | 1300 &ndash; 2600</td>
              </tr>
              <tr>
                <td><strong>ISO S (Superalloys)</strong></td>
                <td>Titanium Ti-6Al-4V Grade 5</td>
                <td>8 &ndash; 15 | 25 &ndash; 50</td>
                <td>45 &ndash; 80 | 150 &ndash; 260</td>
                <td>N/A (PCD / Ceramic unstable)</td>
              </tr>
              <tr>
                <td><strong>ISO S (Heat Resistant)</strong></td>
                <td>Inconel 718 / Waspaloy</td>
                <td>5 &ndash; 10 | 15 &ndash; 35</td>
                <td>25 &ndash; 50 | 80 &ndash; 165</td>
                <td>150 &ndash; 250 | 500 &ndash; 820 (Whiskered)</td>
              </tr>
              <tr>
                <td><strong>ISO H (Hardened)</strong></td>
                <td>Tool Steel D2 (58&ndash;62 HRC)</td>
                <td>N/A (Ineffective)</td>
                <td>40 &ndash; 80 | 130 &ndash; 260</td>
                <td>100 &ndash; 200 | 330 &ndash; 650 (cBN)</td>
              </tr>
            </tbody>
          </table>

          <h2>Kinematic Differences: Milling vs. Turning vs. Drilling</h2>
          <p>While the mathematical formula \(V_c = \pi D N / 1000\) remains universally identical across all operations, the physical definition of the diameter parameter \(D\) shifts dynamically:</p>
          <ul>
            <li><strong>CNC Milling:</strong> The cutting tool rotates while the workpiece traverses beneath it. Here, \(D\) is the outside diameter of the end mill, face mill, or shell mill. The cutting speed is fixed across all flutes for a given RPM regardless of workpiece dimensions.</li>
            <li><strong>CNC Lathe / Turning:</strong> The workpiece rotates in a chuck while a stationary single-point insert cuts radially. Consequently, \(D\) changes continuously as the part diameter reduces during facing and turning passes. Modern CNC lathes utilize <strong>Constant Surface Speed (CSS / G96)</strong>, dynamically accelerating spindle RPM as the tool approaches centerline to maintain a constant \(V_c\).</li>
            <li><strong>Drilling:</strong> The drill rotates into solid material. While \(V_c\) is calculated at the outer drill margins, the cutting speed drops to strictly <strong>zero at the drill chisel point</strong> (web center). Material extrusion, rather than shearing, occurs at the drill center, requiring heavy axial thrust loads.</li>
          </ul>

          <div class="worked-example-card">
            <h3>Step-by-Step Worked Case Study: CNC Milling 4140 Alloy Steel</h3>
            <p><strong>Design Scenario:</strong> A CNC machinist is rough milling an aerospace bracket forged from AISI 4140 pre-hardened alloy steel (28 HRC) using a 12.0 mm 4-flute TiAlN-coated solid carbide end mill.</p>
            <ul>
              <li>Tool diameter: \(D = 12.0\text{ mm}\).</li>
              <li>Recommended surface cutting speed: \(V_c = 160\text{ m/min}\).</li>
              <li>Axial depth of cut: \(a_p = 6.0\text{ mm}\).</li>
              <li>Radial width of cut: \(a_e = 4.0\text{ mm}\) (33.3% radial stepover).</li>
            </ul>

            <p><strong>Step 1: Calculate required spindle rotational speed (\(N\))</strong></p>
            <div class="formula-box">
              $$N = \frac{1000 \cdot V_c}{\pi \cdot D} = \frac{1000 \cdot 160}{\pi \cdot 12.0} = \frac{160000}{37.699} = 4,244.1\text{ RPM}$$
            </div>
            <p>The machinist programs the CNC spindle to <strong>4,245 RPM</strong>.</p>

            <p><strong>Step 2: Calculate equivalent imperial surface speed in SFM</strong></p>
            <div class="formula-box">
              $$V_{c, \text{SFM}} = V_c \times 3.28084 = 160 \times 3.28084 = 524.9\text{ SFM}$$
              $$D_{\text{inches}} = \frac{12.0}{25.4} = 0.4724\text{ inches}$$
              $$N = \frac{12 \cdot 524.9}{\pi \cdot 0.4724} = \frac{6298.8}{1.484} = 4,244.5\text{ RPM}$$
            </div>

            <p><strong>Step 3: Verify radial engagement ratio and thermal duty cycle</strong></p>
            <div class="formula-box">
              $$\text{Engagement \%} = \frac{a_e}{D} \times 100 = \frac{4.0}{12.0} \times 100 = 33.3\%$$
            </div>
            <p>Because the radial engagement is 33.3% (&lt; 50%), each flute is in cut for only 120&deg; of the 360&deg; rotation, allowing 240&deg; of rotation in air for compressed air or coolant cooling. This intermittent cut extends tool life significantly compared to full-slotting (100% engagement).</p>
          </div>

          <h2>Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3>What is Constant Surface Speed (CSS) on a CNC lathe and why is it important?</h3>
            <p>Constant Surface Speed (programmed via G96 on Fanuc, Haas, and Siemens controls) continuously adjusts spindle RPM as the tool moves across varying diameters. As the lathe tool faces off a bar toward the center, diameter \(D \to 0\), so the CNC automatically accelerates the spindle to maintain the target \(V_c\). This prevents the tool from slowing down to a crawl at the center, ensuring consistent surface finish and maximizing tool life across facing and contoured profiling.</p>
          </div>

          <div class="faq-item">
            <h3>How do PVD and CVD tool coatings allow higher cutting speeds?</h3>
            <p>Physical Vapor Deposition (PVD) and Chemical Vapor Deposition (CVD) coatings apply micro-thin ceramic layers (Titanium Aluminum Nitride TiAlN, Aluminum Titanium Nitride AlTiN, Diamond) possessing extreme nano-hardness and thermal stability up to 1,100&deg;C. Under intense cutting heat, TiAlN forms an amorphous aluminum oxide (\(\text{Al}_2\text{O}_3\)) surface glaze that acts as a thermal barrier, deflecting heat into outgoing chips and protecting the underlying carbide substrate from thermal deformation.</p>
          </div>

          <div class="faq-item">
            <h3>Why must cutting speed be reduced in deep slotting compared to profile milling?</h3>
            <p>In full-slotting (\(a_e = D\)), the radial engagement is 100%, and each flute spends 180&deg; of each rotation engaged in violent cutting. Chips cannot easily escape the narrow slot, causing chip re-cutting, rapid heat accumulation, and tool deflection. In contrast, peripheral shoulder milling (\(a_e \le 0.25 D\)) provides substantial cooling time in air and promotes efficient chip evacuation, allowing 20% to 50% higher surface speeds.</p>
          </div>

          <div class="faq-item">
            <h3>How does cutting fluid (flood coolant vs MQL) affect allowable cutting speed?</h3>
            <p>Flood coolant drastically reduces localized friction and thermal buildup, allowing higher speeds in drilling, reaming, and stainless steel turning. However, in interrupted milling with carbide inserts, cyclical flooding can cause thermal fatigue cracking (comb cracks) due to rapid heating during cut entry and violent cooling upon exit. For carbide milling in high-strength steels, dry machining with high-pressure air blast or Minimum Quantity Lubrication (MQL) often yields longer tool life than flood coolant.</p>
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
    // Presets for Vc based on Material & Carbide Tooling [m/min]
    const MATERIAL_PRESETS = {
      al6061: 350,
      steel1018: 220,
      steel4140: 160,
      ss304: 130,
      castIron: 180,
      titanium: 60,
      inconel: 35,
      brass: 300
    };

    const TOOL_MULTIPLIERS = {
      carbide: 1.0,
      carbideUncoated: 0.75,
      hss: 0.20,
      ceramic: 2.2
    };

    const machiningOperationSelect = document.getElementById('machiningOperation');
    const speedModeSelect = document.getElementById('speedMode');
    const speedUnitsSelect = document.getElementById('speedUnits');
    const workMaterialSelect = document.getElementById('workMaterial');
    const toolMaterialSelect = document.getElementById('toolMaterial');
    const toolDiamInput = document.getElementById('toolDiam');
    const targetVcInput = document.getElementById('targetVc');
    const inputRpmInput = document.getElementById('inputRpm');
    const axialDocInput = document.getElementById('axialDoc');
    const radialDocInput = document.getElementById('radialDoc');

    const lblToolDiam = document.getElementById('lblToolDiam');
    const lblTargetVc = document.getElementById('lblTargetVc');
    const lblAxialDoc = document.getElementById('lblAxialDoc');
    const lblRadialDoc = document.getElementById('lblRadialDoc');
    const grpTargetSpeed = document.getElementById('grpTargetSpeed');
    const grpInputRpm = document.getElementById('grpInputRpm');

    const speedResultBox = document.getElementById('speedResultBox');
    const resPrimarySpeedLabel = document.getElementById('resPrimarySpeedLabel');
    const resSecondarySpeedLabel = document.getElementById('resSecondarySpeedLabel');
    const resSpindleRpm = document.getElementById('resSpindleRpm');
    const resSurfaceSpeed = document.getElementById('resSurfaceSpeed');
    const resAltSpeed = document.getElementById('resAltSpeed');
    const resAngularVel = document.getElementById('resAngularVel');
    const resRadialEngagement = document.getElementById('resRadialEngagement');
    const resTaylorSpeed = document.getElementById('resTaylorSpeed');
    const speedNotesBox = document.getElementById('speedNotesBox');

    workMaterialSelect.addEventListener('change', function() {
      const mat = this.value;
      if (mat !== 'custom') {
        const baseVc = MATERIAL_PRESETS[mat] || 150;
        const toolMult = TOOL_MULTIPLIERS[toolMaterialSelect.value] || 1.0;
        const isMetric = speedUnitsSelect.value === 'metric';
        const finalVc = baseVc * toolMult;
        targetVcInput.value = isMetric ? Math.round(finalVc) : Math.round(finalVc * 3.28084);
      }
      calculateCuttingSpeed();
    });

    toolMaterialSelect.addEventListener('change', function() {
      if (workMaterialSelect.value !== 'custom') {
        const baseVc = MATERIAL_PRESETS[workMaterialSelect.value] || 150;
        const toolMult = TOOL_MULTIPLIERS[this.value] || 1.0;
        const isMetric = speedUnitsSelect.value === 'metric';
        const finalVc = baseVc * toolMult;
        targetVcInput.value = isMetric ? Math.round(finalVc) : Math.round(finalVc * 3.28084);
      }
      calculateCuttingSpeed();
    });

    speedModeSelect.addEventListener('change', function() {
      if (this.value === 'findRpm') {
        grpTargetSpeed.style.display = 'block';
        grpInputRpm.style.display = 'none';
        resPrimarySpeedLabel.textContent = "Calculated Spindle Speed";
        resSecondarySpeedLabel.textContent = "Surface Cutting Speed (Vc)";
      } else {
        grpTargetSpeed.style.display = 'none';
        grpInputRpm.style.display = 'block';
        resPrimarySpeedLabel.textContent = "Calculated Surface Speed";
        resSecondarySpeedLabel.textContent = "Input Spindle Speed (RPM)";
      }
      calculateCuttingSpeed();
    });

    speedUnitsSelect.addEventListener('change', function() {
      const isMetric = this.value === 'metric';
      if (isMetric) {
        lblToolDiam.textContent = "Tool / Part Diameter D [mm]";
        lblTargetVc.textContent = "Target Surface Cutting Speed Vc [m/min]";
        lblAxialDoc.textContent = "Axial Depth of Cut (ap) [mm]";
        lblRadialDoc.textContent = "Radial Width of Cut (ae) [mm]";
        toolDiamInput.value = 12.0;
        targetVcInput.value = 250;
        axialDocInput.value = 3.0;
        radialDocInput.value = 6.0;
      } else {
        lblToolDiam.textContent = "Tool / Part Diameter D [in]";
        lblTargetVc.textContent = "Target Surface Cutting Speed Vc [SFM]";
        lblAxialDoc.textContent = "Axial Depth of Cut (ap) [in]";
        lblRadialDoc.textContent = "Radial Width of Cut (ae) [in]";
        toolDiamInput.value = 0.50;
        targetVcInput.value = 800;
        axialDocInput.value = 0.125;
        radialDocInput.value = 0.250;
      }
      calculateCuttingSpeed();
    });

    function calculateCuttingSpeed() {
      const mode = speedModeSelect.value;
      const isMetric = speedUnitsSelect.value === 'metric';
      const uDiam = isMetric ? 'mm' : 'in';
      const uSpeed = isMetric ? 'm/min' : 'SFM';
      const uAltSpeed = isMetric ? 'SFM' : 'm/min';

      let D = parseFloat(toolDiamInput.value);
      if (isNaN(D) || D <= 0) D = isMetric ? 12.0 : 0.5;

      let N = 0;
      let Vc = 0;

      if (mode === 'findRpm') {
        Vc = parseFloat(targetVcInput.value);
        if (isNaN(Vc) || Vc <= 0) Vc = isMetric ? 200 : 650;

        if (isMetric) {
          N = (1000 * Vc) / (Math.PI * D);
        } else {
          N = (12 * Vc) / (Math.PI * D);
        }
        resSpindleRpm.textContent = Math.round(N) + " RPM";
        resSurfaceSpeed.textContent = Vc.toFixed(1) + " " + uSpeed;
      } else {
        N = parseFloat(inputRpmInput.value);
        if (isNaN(N) || N <= 0) N = 2000;

        if (isMetric) {
          Vc = (Math.PI * D * N) / 1000;
        } else {
          Vc = (Math.PI * D * N) / 12;
        }
        resSpindleRpm.textContent = Vc.toFixed(1) + " " + uSpeed;
        resSurfaceSpeed.textContent = Math.round(N) + " RPM";
      }

      // Alternate Speed Conversion
      let altVc = isMetric ? (Vc * 3.28084) : (Vc / 3.28084);
      resAltSpeed.textContent = altVc.toFixed(1) + " " + uAltSpeed;

      // Angular Velocity omega = 2*pi*N / 60 (rad/s)
      const omega = (2 * Math.PI * N) / 60;
      resAngularVel.textContent = omega.toFixed(1) + " rad/s";

      // Radial Engagement %
      let ae = parseFloat(radialDocInput.value);
      if (isNaN(ae) || ae < 0) ae = D / 2;
      const engagementPct = Math.min(100, (ae / D) * 100);
      resRadialEngagement.textContent = engagementPct.toFixed(1) + " %";

      // Taylor Tool Life estimate (assuming target Vc gives 15-min life)
      // Vc_15 = Vc * (15/15)^n = Vc
      resTaylorSpeed.textContent = Vc.toFixed(1) + " " + uSpeed;

      let notes = `<strong>Speed Kinematics:</strong> For a <strong>${D.toFixed(2)} ${uDiam}</strong> cutter at <strong>${Math.round(N)} RPM</strong>, linear rim cutting speed is <strong>${Vc.toFixed(1)} ${uSpeed}</strong> (${altVc.toFixed(1)} ${uAltSpeed}). `;
      if (N > 15000) {
        notes += `<span style="color:#b45309;">High-speed machining (HSM) zone: Ensure dual-contact spindle (BBT/HSK) and dynamically balanced toolholder (G2.5 @ 20k RPM).</span>`;
      } else {
        notes += `Radial stepover of <strong>${ae.toFixed(2)} ${uDiam}</strong> provides <strong>${engagementPct.toFixed(1)}%</strong> tool engagement.`;
      }
      speedNotesBox.innerHTML = notes;

      speedResultBox.style.display = 'block';
    }

    document.getElementById('calcSpeedBtn').addEventListener('click', calculateCuttingSpeed);
    document.getElementById('resetSpeedBtn').addEventListener('click', function() {
      setTimeout(calculateCuttingSpeed, 50);
    });

    window.addEventListener('DOMContentLoaded', calculateCuttingSpeed);
  </script>
</body>
</html>
"""

TOOL_4_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Feed Rate Calculator | CNC Table Feed, Chip Load & Material Removal Rate</title>
  <meta name="description" content="Calculate CNC feed rate (vf in mm/min and IPM), chip load per tooth (fz), radial chip thinning factors (RCTF), and material removal rates per ISO 13399 and ASME machining standards.">
  <link rel="canonical" href="https://calchub.cloud/feed-rate-calculator.html">
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
        "name": "Feed Rate Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "CNC machining feeds and material removal rate calculation tool solving table linear feed rate vf = fz * z * N, radial chip thinning compensation, and cycle machining time per ISO 13399.",
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
            "name": "What is the formula for CNC milling table feed rate (vf)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "CNC milling table feed rate is: vf = fz * z * N, where vf is table linear feed speed in mm/min (or inches/min), fz is feed per tooth / chip load (mm/tooth or IPT), z is the number of flutes/teeth on the cutter, and N is spindle speed in RPM."
            }
          },
          {
            "@type": "Question",
            "name": "What is Radial Chip Thinning (RCT) and when does it apply?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "When radial width of cut (ae) is less than 50% of cutter diameter (ae < D/2), the maximum chip thickness produced at the tooth entry/exit is significantly smaller than the programmed linear feed per tooth (fz). To maintain the manufacturer recommended chip thickness and avoid tool rubbing/burnishing, the programmed feed must be multiplied by a chip thinning factor: fz_comp = fz_actual / (2 * sqrt((ae/D) - (ae/D)^2))."
            }
          },
          {
            "@type": "Question",
            "name": "How is Material Removal Rate (MRR) calculated for milling?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For CNC milling: MRR = (ap * ae * vf) / 1000 [cm^3/min], where ap is axial depth of cut in mm, ae is radial width of cut in mm, and vf is table feed rate in mm/min. In imperial units: MRR = ap * ae * vf [in^3/min], with ap and ae in inches and vf in inches per minute (IPM)."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between feed per tooth (fz) and feed per revolution (fn)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Feed per tooth (fz, also termed chip load) represents the advance of a single cutting edge as it traverses through the workpiece. Feed per revolution (fn) is the total distance the tool advances during one full 360-degree spindle rotation: fn = fz * z. Lathe turning tools have a single active cutting point (z=1), so fn equals fz."
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
      <span>Feed Rate Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">ISO 13399 &amp; ASME B5 CNC Machining Standards</div>
          <h1 class="calc-title">Feed Rate Calculator</h1>
          <p class="calc-tagline">Calculate CNC milling table feed rates (mm/min and IPM), chip load per tooth, radial chip thinning compensation factors, and volumetric material removal rates.</p>
        </header>

        <div class="tool-card">
          <form id="feedCalcForm">
            <div class="calc-grid">
              <div class="form-group">
                <label for="feedUnits">Engineering Units</label>
                <select id="feedUnits">
                  <option value="metric" selected>Metric (mm, mm/min, cm³/min)</option>
                  <option value="imperial">Imperial (in, IPM, in³/min)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="feedMode">Calculation Mode</label>
                <select id="feedMode">
                  <option value="fromChipLoad" selected>Calculate Table Feed (vf) from Chip Load (fz)</option>
                  <option value="fromTableFeed">Calculate Chip Load (fz) from Programmed Feed (vf)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="spindleRpm">Spindle Rotational Speed (N) [RPM]</label>
                <input type="number" id="spindleRpm" step="50" min="10" max="60000" value="4500">
              </div>

              <div class="form-group">
                <label for="numFlutes">Number of Cutter Flutes / Teeth (z)</label>
                <input type="number" id="numFlutes" min="1" max="30" step="1" value="4">
              </div>

              <div class="form-group" id="grpChipLoad">
                <label for="chipLoad" id="lblChipLoad">Feed per Tooth / Chip Load (fz) [mm/tooth]</label>
                <input type="number" id="chipLoad" step="0.01" min="0.001" max="2.0" value="0.06">
              </div>

              <div class="form-group" id="grpTableFeed" style="display: none;">
                <label for="tableFeed" id="lblTableFeed">Programmed Table Feed (vf) [mm/min]</label>
                <input type="number" id="tableFeed" step="10" min="1" max="50000" value="1080">
              </div>

              <div class="form-group">
                <label for="cutterDiam" id="lblCutterDiam">Cutter Diameter (D) [mm]</label>
                <input type="number" id="cutterDiam" step="0.5" min="0.5" max="500" value="12.0">
              </div>

              <div class="form-group">
                <label for="radDoc" id="lblRadDoc">Radial Width of Cut (ae) [mm]</label>
                <input type="number" id="radDoc" step="0.5" min="0.1" max="500" value="3.0">
              </div>

              <div class="form-group">
                <label for="axDoc" id="lblAxDoc">Axial Depth of Cut (ap) [mm]</label>
                <input type="number" id="axDoc" step="0.5" min="0.1" max="500" value="6.0">
              </div>

              <div class="form-group">
                <label for="applyRct">Radial Chip Thinning (RCT) Compensation</label>
                <select id="applyRct">
                  <option value="yes" selected>Enable RCT Feed Compensation</option>
                  <option value="no">Disable (Standard Linear Feed)</option>
                </select>
              </div>
            </div>

            <div class="calc-actions">
              <button type="button" id="calcFeedBtn" class="btn btn-primary">Calculate CNC Feed Dynamics</button>
              <button type="reset" id="resetFeedBtn" class="btn btn-secondary">Reset Defaults</button>
            </div>
          </form>

          <div id="feedResultBox" class="results-container" style="display: none;">
            <h3>CNC Feed Rate & Material Removal Results</h3>
            <div class="results-grid">
              <div class="result-tile">
                <span class="result-label" id="resPrimaryFeedLabel">Effective Table Feed Rate (vf)</span>
                <span id="resTableFeedVal" class="result-value">-- mm/min</span>
              </div>
              <div class="result-tile">
                <span class="result-label" id="resSecondaryFeedLabel">Feed per Tooth (Chip Load fz)</span>
                <span id="resChipLoadVal" class="result-value">-- mm/tooth</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Feed per Revolution (fn)</span>
                <span id="resFeedRevVal" class="result-value">-- mm/rev</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Material Removal Rate (MRR)</span>
                <span id="resMrrVal" class="result-value">-- cm³/min</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Chip Thinning Factor (RCTF)</span>
                <span id="resRctfVal" class="result-value">--</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Actual Max Chip Thickness (hex)</span>
                <span id="resHexVal" class="result-value">-- mm</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Radial Engagement</span>
                <span id="resRadEngageVal" class="result-value">-- %</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Estimated Spindle Power Demand</span>
                <span id="resPowerVal" class="result-value">-- kW</span>
              </div>
            </div>
            <div id="feedNotesBox" style="margin-top: 1rem; color: #1e40af; background: #eff6ff; border: 1px solid #bfdbfe; padding: 0.75rem; border-radius: 6px;"></div>
          </div>
        </div>

        <article class="article-body">
          <h2>CNC Machining Feed Dynamics & Chip Formation Physics</h2>
          <p>In metal cutting and CNC machining, <strong>feed rate</strong> determines the advance velocity of the cutting tool relative to the workpiece. While cutting speed (\(V_c\)) governs the thermal threshold and rotational surface shearing velocity, the feed rate directly dictates <strong>undeformed chip thickness</strong>, mechanical cutting forces, tool deflection bending moments, surface scallop crest height, and spindle power consumption.</p>

          <p>Programming an incorrect feed rate causes catastrophic machining failures. If the feed rate is programmed too low, chip thickness drops below the micro-honed cutting edge radius (\(r_\beta \approx 5 - 20\ \mu\text{m}\)), causing the tool to rub and burnish rather than shear. This rubbing generates extreme friction, severe work hardening in austenitic steels and nickel alloys, rapid flank wear, and premature chatter vibration. Conversely, an excessive feed rate overloads tool flutes with chips, packing flutes until the solid carbide shank snaps under extreme torsional shear.</p>

          <h2>Core Mathematical Equations for Milling Feed Rates</h2>
          <p>Milling cutters feature multiple discrete teeth or flutes (\(z\)) distributed symmetrically around the tool circumference. The relationship between individual tooth advance and total table axis velocity is formulated per <strong>ISO 13399</strong>:</p>

          <div class="formula-box">
            $$v_f = f_z \cdot z \cdot N \quad [\text{mm/min or IPM}]$$
          </div>

          <p>Where:</p>
          <ul>
            <li><strong>\(v_f\)</strong>: Linear table feed speed, in millimeters per minute (\(\text{mm/min}\)) or inches per minute (\(\text{IPM}\)).</li>
            <li><strong>\(f_z\)</strong>: Feed per tooth (chip load), in millimeters per tooth (\(\text{mm/tooth}\)) or inches per tooth (\(\text{IPT}\)).</li>
            <li><strong>\(z\)</strong>: Total active flute or tooth count on the cutting tool.</li>
            <li><strong>\(N\)</strong>: Spindle rotational frequency, in revolutions per minute (\(\text{RPM}\)).</li>
          </ul>

          <p>The total feed distance traversed per one single 360-degree rotation of the spindle is the <strong>feed per revolution</strong> (\(f_n\)):</p>

          <div class="formula-box">
            $$f_n = \frac{v_f}{N} = f_z \cdot z \quad [\text{mm/rev or IPR}]$$
          </div>

          <h2>Radial Chip Thinning (RCT) & High-Efficiency Milling (HEM)</h2>
          <p>One of the most vital principles in modern CNC toolpath programming is <strong>Radial Chip Thinning</strong>. Classical feed rate formulas assume that maximum chip thickness equals the programmed feed per tooth (\(h_{\text{max}} = f_z\)). However, this assumption is true only when the radial width of cut (\(a_e\)) equals or exceeds 50% of the cutter diameter (\(a_e \ge D/2\)).</p>

          <p>When executing light radial stepovers typical of High-Efficiency Milling (HEM), trochoidal milling, and dynamic toolpaths (\(a_e < 0.25 D\)), the tooth enters and exits the workpiece across a narrow circular arc, producing a thin sliver of a chip. The true maximum chip thickness (\(h_{\text{ex}}\)) is geometrically defined as:</p>

          <div class="formula-box">
            $$h_{\text{ex}} = 2 \cdot f_z \cdot \sqrt{\frac{a_e}{D} - \left(\frac{a_e}{D}\right)^2}$$
          </div>

          <p>If an engineer runs a 12 mm end mill at a 1.2 mm radial stepover (\(a_e/D = 0.10\)) with a standard catalog chip load of \(f_z = 0.05\text{ mm}\), the actual chip thickness produced is only \(0.03\text{ mm}\)—causing tool rubbing and thermal glaze. To achieve the targeted chip thickness (\(h_{\text{target}}\)), the programmed feed per tooth must be escalated by the <strong>Radial Chip Thinning Factor (RCTF)</strong>:</p>

          <div class="formula-box">
            $$\text{RCTF} = \frac{1}{2 \cdot \sqrt{\frac{a_e}{D} - \left(\frac{a_e}{D}\right)^2}} \quad \Longleftrightarrow \quad f_{z, \text{programmed}} = f_{z, \text{target}} \cdot \text{RCTF}$$
          </div>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Radial Engagement Ratio (\(a_e / D\))</th>
                <th>Radial Chip Thinning Factor (RCTF)</th>
                <th>Programmed Feed Multiplier</th>
                <th>Effective Machining Benefit</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>50% (Full Slotting or Heavy Shoulder)</td>
                <td>1.00</td>
                <td>1.00 &times; (No compensation)</td>
                <td>Standard chip thickness geometry.</td>
              </tr>
              <tr>
                <td>30% (Standard Semi-Finishing)</td>
                <td>1.09</td>
                <td>1.09 &times; Catalog Feed</td>
                <td>Mild thinning compensation.</td>
              </tr>
              <tr>
                <td>20% (Typical Roughing Shoulder)</td>
                <td>1.25</td>
                <td>1.25 &times; Catalog Feed</td>
                <td>25% cycle time reduction.</td>
              </tr>
              <tr>
                <td>10% (High-Efficiency Dynamic Milling)</td>
                <td>1.67</td>
                <td>1.67 &times; Catalog Feed</td>
                <td>67% feed boost with low cutting forces.</td>
              </tr>
              <tr>
                <td>5% (High-Speed Trochoidal Peel)</td>
                <td>2.29</td>
                <td>2.29 &times; Catalog Feed</td>
                <td>129% feed increase without overloading tool.</td>
              </tr>
              <tr>
                <td>2% (Finishing Wall Profiling)</td>
                <td>3.57</td>
                <td>3.57 &times; Catalog Feed</td>
                <td>Prevents microscopic rubbing on finishing walls.</td>
              </tr>
            </tbody>
          </table>

          <h2>Volumetric Material Removal Rate (MRR)</h2>
          <p>Material Removal Rate (\(\text{MRR}\)) quantifies the volume of metal sheared away per unit of machining time. It serves as the primary benchmark for machining efficiency, spindle power sizing, and tooling comparison:</p>

          <div class="formula-box">
            $$\text{MRR} = \frac{a_p \cdot a_e \cdot v_f}{1000} \quad [\text{cm}^3/\text{min}] \quad \Longleftrightarrow \quad \text{MRR} = a_p \cdot a_e \cdot v_f \quad [\text{in}^3/\text{min}]$$
          </div>

          <p>Where \(a_p\) is axial depth of cut (mm or in), \(a_e\) is radial width of cut (mm or in), and \(v_f\) is table feed speed (mm/min or IPM). Spindle net cutting power (\(P_c\)) is directly proportional to MRR and the specific cutting energy of the workpiece material (\(k_c\)):</p>

          <div class="formula-box">
            $$P_c = \frac{\text{MRR} \cdot k_c}{60 \times 10^3} \quad [\text{kW}]$$
          </div>

          <p>Where specific cutting force (\(k_c\)) ranges from 700 \(\text{N/mm}^2\) for aluminum up to 2,200 \(\text{N/mm}^2\) for alloy steel and 3,200 \(\text{N/mm}^2\) for nickel superalloys.</p>

          <div class="worked-example-card">
            <h3>Step-by-Step Worked Case Study: Dynamic Trochoidal Milling in 304 Stainless</h3>
            <p><strong>Design Scenario:</strong> A programmer is setting up a dynamic HEM roughing toolpath on a 5-axis machining center to pocket 304 austenitic stainless steel using a 10 mm 5-flute carbide end mill.</p>
            <ul>
              <li>Cutter diameter: \(D = 10.0\text{ mm}\), Flutes: \(z = 5\).</li>
              <li>Spindle speed: \(N = 4,200\text{ RPM}\) (\(V_c = 132\text{ m/min}\)).</li>
              <li>Target chip thickness (catalog recommended): \(f_{z, \text{target}} = 0.045\text{ mm/tooth}\).</li>
              <li>Axial depth of cut: \(a_p = 15.0\text{ mm}\) (1.5 &times; \(D\)).</li>
              <li>Radial width of cut: \(a_e = 1.0\text{ mm}\) (10% stepover).</li>
            </ul>

            <p><strong>Step 1: Compute Radial Engagement Ratio (\(a_e / D\))</strong></p>
            <div class="formula-box">
              $$\frac{a_e}{D} = \frac{1.0}{10.0} = 0.10 \quad (10\%)$$
            </div>

            <p><strong>Step 2: Calculate Radial Chip Thinning Factor (RCTF)</strong></p>
            <div class="formula-box">
              $$\text{RCTF} = \frac{1}{2 \cdot \sqrt{0.10 - (0.10)^2}} = \frac{1}{2 \cdot \sqrt{0.10 - 0.01}} = \frac{1}{2 \cdot \sqrt{0.09}} = \frac{1}{2 \cdot 0.30} = 1.667$$
            </div>

            <p><strong>Step 3: Calculate compensated feed per tooth and linear table feed rate</strong></p>
            <div class="formula-box">
              $$f_{z, \text{comp}} = 0.045 \times 1.667 = 0.075\text{ mm/tooth}$$
              $$v_f = f_{z, \text{comp}} \cdot z \cdot N = 0.075 \cdot 5 \cdot 4200 = 1,575\text{ mm/min} \quad (62.0\text{ IPM})$$
            </div>
            <p>Without chip thinning compensation, the feed rate would be only \(0.045 \times 5 \times 4200 = 945\text{ mm/min}\). Enabling RCT increases feed speed by <strong>66.7%</strong> while keeping true chip thickness at the safe \(0.045\text{ mm}\) specification.</p>

            <p><strong>Step 4: Compute Volumetric Material Removal Rate (MRR)</strong></p>
            <div class="formula-box">
              $$\text{MRR} = \frac{15.0 \cdot 1.0 \cdot 1575}{1000} = \frac{23625}{1000} = 23.63\text{ cm}^3/\text{min} \quad (1.44\text{ in}^3/\text{min})$$
            </div>
          </div>

          <h2>Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3>What happens if I enable Radial Chip Thinning on a 50% or full-slot cut?</h3>
            <p>At 50% radial engagement (\(a_e / D = 0.50\)), the chip thinning factor mathematically equals 1.00, meaning zero compensation is applied. If engagement exceeds 50% (such as full slotting at 100%), chip thinning does not occur; instead, the chip thickness at entry/exit is already maximized. You should never apply chip thinning multipliers above 50% engagement, as doing so would overload flutes and snap the tool.</p>
          </div>

          <div class="faq-item">
            <h3>Why do 5-flute and 7-flute end mills allow higher feed rates than 3-flute or 4-flute cutters?</h3>
            <p>Because linear feed rate is directly proportional to flute count (\(v_f = f_z \cdot z \cdot N\)), a 5-flute end mill delivers a 25% higher table feed than a 4-flute tool at the exact same spindle RPM and chip load. For peripheral dynamic roughing in steel, 5-flute, 6-flute, and 7-flute end mills provide massive productivity gains because the small radial engagement leaves ample open flute space for chip ejection.</p>
          </div>

          <div class="faq-item">
            <h3>How does tool stickout (overhang) constrain allowable feed rates?</h3>
            <p>Tool deflection is governed by cantilever beam mechanics: deflection \(\delta \propto L^3 / D^4\), meaning doubling tool overhang increases deflection by a factor of 8. Excessive deflection causes chatter, poor dimensional tolerances, and chipped cutting corners. When tool overhang exceeds 3 &times; diameter (e.g., sticking out 50 mm on a 10 mm tool), feed per tooth and axial depth of cut must be reduced by 20% to 50% to prevent chatter resonance.</p>
          </div>

          <div class="faq-item">
            <h3>How do I calculate feed rate for CNC circular interpolation (internal bore milling)?</h3>
            <p>When an end mill travels along a circular internal bore arc, the tool center line travels along a tighter radius than the outer tool edge touching the wall. The feed rate programmed at the tool center point must be derated by the arc ratio: \(v_{f, \text{center}} = v_{f, \text{linear}} \cdot \left(\frac{D_{\text{bore}} - D_{\text{tool}}}{D_{\text{bore}}}\right)\). Conversely, when contouring around an outside boss, the center feed can be increased.</p>
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
    const feedUnitsSelect = document.getElementById('feedUnits');
    const feedModeSelect = document.getElementById('feedMode');
    const spindleRpmInput = document.getElementById('spindleRpm');
    const numFlutesInput = document.getElementById('numFlutes');
    const chipLoadInput = document.getElementById('chipLoad');
    const tableFeedInput = document.getElementById('tableFeed');
    const cutterDiamInput = document.getElementById('cutterDiam');
    const radDocInput = document.getElementById('radDoc');
    const axDocInput = document.getElementById('axDoc');
    const applyRctSelect = document.getElementById('applyRct');

    const lblChipLoad = document.getElementById('lblChipLoad');
    const lblTableFeed = document.getElementById('lblTableFeed');
    const lblCutterDiam = document.getElementById('lblCutterDiam');
    const lblRadDoc = document.getElementById('lblRadDoc');
    const lblAxDoc = document.getElementById('lblAxDoc');
    const grpChipLoad = document.getElementById('grpChipLoad');
    const grpTableFeed = document.getElementById('grpTableFeed');

    const feedResultBox = document.getElementById('feedResultBox');
    const resPrimaryFeedLabel = document.getElementById('resPrimaryFeedLabel');
    const resSecondaryFeedLabel = document.getElementById('resSecondaryFeedLabel');
    const resTableFeedVal = document.getElementById('resTableFeedVal');
    const resChipLoadVal = document.getElementById('resChipLoadVal');
    const resFeedRevVal = document.getElementById('resFeedRevVal');
    const resMrrVal = document.getElementById('resMrrVal');
    const resRctfVal = document.getElementById('resRctfVal');
    const resHexVal = document.getElementById('resHexVal');
    const resRadEngageVal = document.getElementById('resRadEngageVal');
    const resPowerVal = document.getElementById('resPowerVal');
    const feedNotesBox = document.getElementById('feedNotesBox');

    feedModeSelect.addEventListener('change', function() {
      if (this.value === 'fromChipLoad') {
        grpChipLoad.style.display = 'block';
        grpTableFeed.style.display = 'none';
        resPrimaryFeedLabel.textContent = "Effective Table Feed Rate (vf)";
        resSecondaryFeedLabel.textContent = "Feed per Tooth (Chip Load fz)";
      } else {
        grpChipLoad.style.display = 'none';
        grpTableFeed.style.display = 'block';
        resPrimaryFeedLabel.textContent = "Calculated Chip Load (fz)";
        resSecondaryFeedLabel.textContent = "Input Programmed Feed (vf)";
      }
      calculateFeeds();
    });

    feedUnitsSelect.addEventListener('change', function() {
      const isMetric = this.value === 'metric';
      if (isMetric) {
        lblChipLoad.textContent = "Feed per Tooth / Chip Load (fz) [mm/tooth]";
        lblTableFeed.textContent = "Programmed Table Feed (vf) [mm/min]";
        lblCutterDiam.textContent = "Cutter Diameter (D) [mm]";
        lblRadDoc.textContent = "Radial Width of Cut (ae) [mm]";
        lblAxDoc.textContent = "Axial Depth of Cut (ap) [mm]";
        chipLoadInput.value = 0.06;
        tableFeedInput.value = 1080;
        cutterDiamInput.value = 12.0;
        radDocInput.value = 3.0;
        axDocInput.value = 6.0;
      } else {
        lblChipLoad.textContent = "Feed per Tooth / Chip Load (fz) [IPT]";
        lblTableFeed.textContent = "Programmed Table Feed (vf) [IPM]";
        lblCutterDiam.textContent = "Cutter Diameter (D) [in]";
        lblRadDoc.textContent = "Radial Width of Cut (ae) [in]";
        lblAxDoc.textContent = "Axial Depth of Cut (ap) [in]";
        chipLoadInput.value = 0.0025;
        tableFeedInput.value = 45.0;
        cutterDiamInput.value = 0.50;
        radDocInput.value = 0.125;
        axDocInput.value = 0.250;
      }
      calculateFeeds();
    });

    function calculateFeeds() {
      const mode = feedModeSelect.value;
      const isMetric = feedUnitsSelect.value === 'metric';
      const uFeed = isMetric ? 'mm/min' : 'IPM';
      const uChip = isMetric ? 'mm/tooth' : 'IPT';
      const uRev = isMetric ? 'mm/rev' : 'IPR';
      const uMrr = isMetric ? 'cm³/min' : 'in³/min';

      let N = parseFloat(spindleRpmInput.value);
      let z = parseInt(numFlutesInput.value, 10);
      let D = parseFloat(cutterDiamInput.value);
      let ae = parseFloat(radDocInput.value);
      let ap = parseFloat(axDocInput.value);

      if (isNaN(N) || N <= 0) N = 4000;
      if (isNaN(z) || z <= 0) z = 4;
      if (isNaN(D) || D <= 0) D = isMetric ? 12.0 : 0.5;
      if (isNaN(ae) || ae <= 0) ae = D / 4;
      if (isNaN(ap) || ap <= 0) ap = D / 2;

      // Radial engagement ratio
      const ratio_ae_D = Math.min(1.0, ae / D);
      const radEngagePct = ratio_ae_D * 100;

      // Radial Chip Thinning Factor (RCTF)
      let rctf = 1.0;
      if (ratio_ae_D < 0.5) {
        const radFactor = 2 * Math.sqrt(ratio_ae_D - Math.pow(ratio_ae_D, 2));
        if (radFactor > 0) {
          rctf = 1.0 / radFactor;
        }
      }

      const applyRct = (applyRctSelect.value === 'yes');
      const effRctf = applyRct ? rctf : 1.0;

      let vf = 0; // table feed
      let fz = 0; // chip load

      if (mode === 'fromChipLoad') {
        const inputFz = parseFloat(chipLoadInput.value);
        fz = isNaN(inputFz) || inputFz <= 0 ? (isMetric ? 0.05 : 0.002) : inputFz;
        // Programmed fz compensated by RCT
        const programmedFz = fz * effRctf;
        vf = programmedFz * z * N;

        resTableFeedVal.textContent = vf.toFixed(1) + " " + uFeed;
        resChipLoadVal.textContent = (applyRct ? `${programmedFz.toFixed(4)} (Base: ${fz.toFixed(4)})` : fz.toFixed(4)) + " " + uChip;
      } else {
        const inputVf = parseFloat(tableFeedInput.value);
        vf = isNaN(inputVf) || inputVf <= 0 ? (isMetric ? 1000 : 40) : inputVf;
        const totalFz = vf / (z * N);
        fz = totalFz / effRctf;

        resTableFeedVal.textContent = fz.toFixed(4) + " " + uChip;
        resChipLoadVal.textContent = vf.toFixed(1) + " " + uFeed;
      }

      // Feed per revolution
      const fn = vf / N;
      resFeedRevVal.textContent = fn.toFixed(4) + " " + uRev;

      // Material Removal Rate (MRR)
      let mrr = 0;
      if (isMetric) {
        // ap [mm], ae [mm], vf [mm/min] -> mm^3/min / 1000 = cm^3/min
        mrr = (ap * ae * vf) / 1000;
      } else {
        // ap [in], ae [in], vf [IPM] -> in^3/min
        mrr = ap * ae * vf;
      }
      resMrrVal.textContent = mrr.toFixed(2) + " " + uMrr;

      // Estimated Power Demand
      // kc approx 1800 N/mm^2 for medium steel -> 1 cm^3/min approx 0.03 kW
      const mrr_cm3 = isMetric ? mrr : (mrr * 16.3871);
      const estKw = Math.max(0.5, (mrr_cm3 * 1800) / 60000);
      const uPwr = isMetric ? 'kW' : 'HP';
      const dispPwr = isMetric ? estKw : (estKw * 1.341);
      resPowerVal.textContent = dispPwr.toFixed(2) + " " + uPwr;

      resRctfVal.textContent = rctf.toFixed(2) + "× (" + (rctf > 1.05 ? "Thinning Active" : "No Thinning") + ")";
      const hex = fz; // true max chip thickness achieved
      resHexVal.textContent = hex.toFixed(4) + " " + (isMetric ? 'mm' : 'in');
      resRadEngageVal.textContent = radEngagePct.toFixed(1) + " %";

      let notes = `<strong>Machining Feed Dynamics:</strong> Table feed rate of <strong>${vf.toFixed(1)} ${uFeed}</strong> delivers <strong>${mrr.toFixed(1)} ${uMrr}</strong> material removal rate. `;
      if (applyRct && rctf > 1.05) {
        notes += `Radial chip thinning compensation is <strong>ACTIVE (${rctf.toFixed(2)}&times;)</strong>, maintaining true chip thickness of ${hex.toFixed(4)} ${isMetric ? 'mm' : 'in'} during light ${radEngagePct.toFixed(1)}% stepover.`;
      } else {
        notes += `Feed per revolution is <strong>${fn.toFixed(4)} ${uRev}</strong> across ${z} flutes.`;
      }
      feedNotesBox.innerHTML = notes;

      feedResultBox.style.display = 'block';
    }

    document.getElementById('calcFeedBtn').addEventListener('click', calculateFeeds);
    document.getElementById('resetFeedBtn').addEventListener('click', function() {
      setTimeout(calculateFeeds, 50);
    });

    window.addEventListener('DOMContentLoaded', calculateFeeds);
  </script>
</body>
</html>
"""

def main():
    target_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    file3 = os.path.join(target_dir, "cutting-speed-calculator.html")
    with open(file3, "w", encoding="utf-8") as f:
        f.write(TOOL_3_HTML)
    print(f"[PASS] cutting-speed-calculator.html generated successfully!")

    file4 = os.path.join(target_dir, "feed-rate-calculator.html")
    with open(file4, "w", encoding="utf-8") as f:
        f.write(TOOL_4_HTML)
    print(f"[PASS] feed-rate-calculator.html generated successfully!")

if __name__ == "__main__":
    main()
