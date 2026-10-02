# -*- coding: utf-8 -*-
"""
Script to generate Batch 18 Part 2 tools:
1. hookes-law-calculator.html
2. kinetic-energy-calculator.html
"""
import os

TOOL_1_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hooke's Law Calculator | Spring Constant, Force & Elastic Energy</title>
  <meta name="description" content="Calculate spring restoring force, spring constant (k), displacement elongation, elastic potential energy, and series/parallel combinations using Hooke's Law.">
  <link rel="canonical" href="https://calchub.cloud/hookes-law-calculator.html">
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
        "name": "Hooke's Law Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates linear spring restoring force, spring stiffness constant (k), elastic potential energy, harmonic oscillation period, and series/parallel spring rates.",
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
            "name": "What is Hooke's Law mathematical formula?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Hooke's Law states that the restoring force exerted by an ideal elastic spring is directly proportional to its displacement from equilibrium: F = -k × x, where 'F' is restoring force in Newtons, 'k' is the spring stiffness constant in N/m (or N/mm), and 'x' is displacement in meters. The negative sign denotes that restoring force opposes displacement."
            }
          },
          {
            "@type": "Question",
            "name": "How is elastic potential energy stored in a spring calculated?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Elastic potential energy is derived by integrating the force over displacement: U = ∫ k·x dx = ½ × k × x². Stored energy scales with the square of displacement, meaning doubling compression quadruples the stored mechanical work."
            }
          },
          {
            "@type": "Question",
            "name": "What happens when multiple springs are connected in series versus parallel?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For springs in parallel, stiffness adds directly: k_eq = k₁ + k₂. For springs in series, the reciprocal of stiffness adds: 1/k_eq = 1/k₁ + 1/k₂ (making the combined spring softer than any individual spring)."
            }
          },
          {
            "@type": "Question",
            "name": "What is the elastic limit of a spring?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The elastic limit is the maximum stress or extension a material can sustain without undergoing permanent plastic deformation. If stretched beyond its elastic limit (yield strength), Hooke's linear law fails, and the spring will not return to its original free length."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body>
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="logo">CalcHub</a>
      <nav class="nav-links">
        <a href="index.html">Home</a>
        <a href="physics.html" class="active">Physics</a>
        <a href="mechanical.html">Mechanical</a>
        <a href="engineering.html">Electrical</a>
        <a href="civil.html">Civil</a>
      </nav>
    </div>
  </header>

  <main class="page-container">
    <div class="content-wrapper">
      <div class="calculator-container">
        <h1>Hooke's Law Calculator</h1>
        <p class="lead-text">Calculate spring restoring force, stiffness constant (k), displacement elongation, stored elastic energy, and natural harmonic oscillation frequency.</p>

        <div class="calc-card">
          <div class="form-group">
            <label for="calcMode">Calculation Target</label>
            <select id="calcMode" class="form-control">
              <option value="solve_f" selected>Solve for Force (F) [Given k and x]</option>
              <option value="solve_k">Solve for Spring Constant (k) [Given F and x]</option>
              <option value="solve_x">Solve for Displacement (x) [Given F and k]</option>
              <option value="solve_network">Spring Network Combinations (Series & Parallel)</option>
            </select>
          </div>

          <div class="form-row" id="rowMain">
            <div class="form-group col-half" id="grpK">
              <label for="valK">Spring Constant / Stiffness (k)</label>
              <div class="input-with-unit">
                <input type="number" id="valK" class="form-control" value="2500" step="any" min="0">
                <select id="unitK" class="unit-select">
                  <option value="npm" selected>N/m</option>
                  <option value="npmm">N/mm</option>
                  <option value="lbpin">lbf/in</option>
                </select>
              </div>
            </div>

            <div class="form-group col-half" id="grpX">
              <label for="valX">Displacement Elongation / Compression (x)</label>
              <div class="input-with-unit">
                <input type="number" id="valX" class="form-control" value="0.08" step="any">
                <select id="unitX" class="unit-select">
                  <option value="m" selected>Meters (m)</option>
                  <option value="mm">Millimeters (mm)</option>
                  <option value="cm">Centimeters (cm)</option>
                  <option value="in">Inches (in)</option>
                </select>
              </div>
            </div>

            <div class="form-group col-half" id="grpF" style="display:none;">
              <label for="valF">Applied Restoring Force (F)</label>
              <div class="input-with-unit">
                <input type="number" id="valF" class="form-control" value="200" step="any">
                <select id="unitF" class="unit-select">
                  <option value="n" selected>Newtons (N)</option>
                  <option value="kn">kilonewtons (kN)</option>
                  <option value="lbf">Pounds force (lbf)</option>
                  <option value="kgf">kgf</option>
                </select>
              </div>
            </div>
          </div>

          <div class="form-row" id="rowNetwork" style="display:none;">
            <div class="form-group col-half">
              <label for="valK1">Spring 1 Constant (k₁)</label>
              <div class="input-with-unit">
                <input type="number" id="valK1" class="form-control" value="1000" step="any" min="0">
                <span style="font-size:12px; padding:6px 12px; background:#fff; border:1px solid #cbd5e1; border-left:none; border-radius:0 4px 4px 0; display:flex; align-items:center;">N/m</span>
              </div>
            </div>
            <div class="form-group col-half">
              <label for="valK2">Spring 2 Constant (k₂)</label>
              <div class="input-with-unit">
                <input type="number" id="valK2" class="form-control" value="2000" step="any" min="0">
                <span style="font-size:12px; padding:6px 12px; background:#fff; border:1px solid #cbd5e1; border-left:none; border-radius:0 4px 4px 0; display:flex; align-items:center;">N/m</span>
              </div>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group col-full">
              <label for="attachedMass">Attached Mass (Optional, for Oscillation Frequency)</label>
              <div class="input-with-unit">
                <input type="number" id="attachedMass" class="form-control" value="5.0" step="any" min="0">
                <span style="font-size:12px; padding:6px 12px; background:#fff; border:1px solid #cbd5e1; border-left:none; border-radius:0 4px 4px 0; display:flex; align-items:center;">kg</span>
              </div>
            </div>
          </div>

          <div class="btn-group">
            <button type="button" id="calcBtn" class="btn btn-primary">Calculate Spring Mechanics</button>
            <button type="button" id="resetBtn" class="btn btn-secondary">Reset Defaults</button>
          </div>

          <div id="resultsPanel" class="results-panel">
            <div class="result-box primary-result">
              <div class="result-label" id="resPrimaryLabel">Spring Restoring Force (F)</div>
              <div class="result-value" id="resPrimaryVal">200.0 N</div>
              <div class="result-sub" id="resPrimarySub">Equivalent to 44.96 lbf (20.39 kgf)</div>
            </div>

            <div class="result-grid">
              <div class="result-item">
                <span class="sub-label">Elastic Potential Energy (U)</span>
                <span class="sub-value" id="resEnergy">8.000 Joules</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Spring Stiffness (k)</span>
                <span class="sub-value" id="resStiffness">2,500 N/m (2.50 N/mm)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Harmonic Natural Frequency (f₀)</span>
                <span class="sub-value" id="resFreq">3.56 Hz (cycles/sec)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Oscillation Period (T)</span>
                <span class="sub-value" id="resPeriod">0.281 seconds</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. Physical Foundations of Hooke's Law of Elasticity</h2>
          <p>Hooke's Law represents the foundational empirical principle governing the elastic deformation of materials. First conceived in 1676 by English polymath Robert Hooke and published in 1678 under the famous Latin anagram <em>ut tensio, sic vis</em> ("as the extension, so the force"), the law states that the mechanical force required to compress or extend a spring by some displacement distance is strictly proportional to that distance.</p>
          <p>In vector mechanics, the restoring force \(\vec{F}\) exerted by an elastic spring on whatever is attached to it acts in the direction opposite to the displacement \(\vec{x}\) from its relaxed equilibrium position:</p>
          <div class="math-block">
            $$F = -k \cdot x$$
          </div>
          <p>Where:</p>
          <ul>
            <li>\(F\) = Spring restoring force in Newtons (\(\text{N}\))</li>
            <li>\(k\) = Spring stiffness constant in Newtons per meter (\(\text{N/m}\) or \(\text{N/mm}\))</li>
            <li>\(x\) = Elongation or compression displacement from equilibrium length (\(\text{meters, m}\))</li>
          </ul>
          <p>At the microscopic solid-state physics level, Hooke's law originates in interatomic potential wells. Solid crystalline materials (such as high-carbon spring steel or titanium alloys) consist of atoms bound in periodic lattice geometries by electromagnetic forces. When a tensile or compressive external force displaces atoms from their equilibrium lattice spacings, the interatomic potential curve closely resembles a parabolic well (\(U \propto \Delta r^2\)), producing a linear restoring force that drives atoms back toward minimum potential energy.</p>

          <h2>2. Elastic Potential Energy Formulation</h2>
          <p>Because the spring restoring force is not constant but increases linearly with displacement (\(F(x) = kx\)), the work required to stretch or compress a spring from equilibrium (\(x = 0\)) to displacement \(x\) must be determined through integral calculus:</p>
          <div class="math-block">
            $$U = \int_0^x F(x')\,dx' = \int_0^x k x'\,dx' = \frac{1}{2} k x^2$$
          </div>
          <p>This <strong>elastic potential energy</strong> (\(U\) in Joules) represents stored mechanical work ready to be converted into kinetic energy when the spring is released. The quadratic relationship (\(\propto x^2\)) carries immense engineering significance: doubling the compression displacement of an automotive suspension bump stop quadruples the absorbed impact energy (\(2^2 = 4\)), while tripling compression absorbs nine times the energy.</p>

          <h2>3. Spring Network Combinations: Series vs. Parallel Sizing</h2>
          <p>Mechanical assemblies frequently employ multi-spring configurations to tailor suspension travel, progressive damping, and package envelope constraints:</p>
          <ul>
            <li><strong>Parallel Spring Configurations:</strong> When two or more springs sit side by side sharing an applied load, every spring undergoes the exact same displacement (\(x_1 = x_2 = x\)). The total restoring force is the algebraic sum of the individual forces (\(F_{\text{total}} = F_1 + F_2 = k_1 x + k_2 x\)). Consequently, the equivalent parallel stiffness is simply additive:
              <div class="math-block">
                $$k_{\text{parallel}} = k_1 + k_2 + \dots + k_n$$
              </div>
            </li>
            <li><strong>Series Spring Configurations:</strong> When springs are linked end-to-end, each spring transmits the exact same force (\(F_1 = F_2 = F\)), but the total displacement is the sum of individual extensions (\(x_{\text{total}} = x_1 + x_2\)). Because \(x = F / k\), substituting gives \(F/k_{\text{eq}} = F/k_1 + F/k_2\), leading to the reciprocal series stiffness rule:
              <div class="math-block">
                $$\frac{1}{k_{\text{series}}} = \frac{1}{k_1} + \frac{1}{k_2} + \dots + \frac{1}{k_n} \implies k_{\text{series}} = \frac{k_1 k_2}{k_1 + k_2}$$
              </div>
              Connecting springs in series always yields an equivalent spring rate that is softer than the softest individual spring in the chain.
            </li>
          </ul>

          <h2>4. Engineering Benchmark Spring Rates Reference Table</h2>
          <p>To assist mechanical rotating equipment designers and test engineers, the reference table below outlines typical spring stiffness rates across diverse consumer and industrial engineering domains:</p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Spring Application / Mechanical Assembly</th>
                <th>Typical Spring Rate (N/mm)</th>
                <th>Spring Rate (lbf/in)</th>
                <th>Primary Engineering Function</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Ballpoint Pen Retraction Spring</td>
                <td>0.05 – 0.15 N/mm</td>
                <td>0.28 – 0.85 lbf/in</td>
                <td>Tactile button return force and latching retention</td>
              </tr>
              <tr>
                <td>Computer Keyboard Mechanical Key Switch</td>
                <td>0.10 – 0.30 N/mm</td>
                <td>0.57 – 1.71 lbf/in</td>
                <td>Ergonomic finger activation force (Cherry MX style)</td>
              </tr>
              <tr>
                <td>Pocket Innerspring Mattress Coil</td>
                <td>0.40 – 0.80 N/mm</td>
                <td>2.28 – 4.56 lbf/in</td>
                <td>Orthopedic human body contour pressure distribution</td>
              </tr>
              <tr>
                <td>Mountain Bike Rear Suspension Shock Coil</td>
                <td>60 – 110 N/mm</td>
                <td>350 – 650 lbf/in</td>
                <td>Off-road terrain bump compliance and wheel travel</td>
              </tr>
              <tr>
                <td>Passenger Sedan Front Suspension Coil Spring</td>
                <td>25 – 45 N/mm</td>
                <td>140 – 250 lbf/in</td>
                <td>Ride comfort, body roll control, and chassis isolation</td>
              </tr>
              <tr>
                <td>Formula 1 Racing Pushrod Spring</td>
                <td>150 – 350 N/mm</td>
                <td>850 – 2,000 lbf/in</td>
                <td>Aerodynamic ride height stability under downforce</td>
              </tr>
              <tr>
                <td>Internal Combustion Engine Valve Spring</td>
                <td>80 – 160 N/mm</td>
                <td>450 – 900 lbf/in</td>
                <td>Preventing valve float at high engine RPM redlines</td>
              </tr>
              <tr>
                <td>Heavy Industrial Stamping Die Spring (High-Load)</td>
                <td>250 – 800 N/mm</td>
                <td>1,400 – 4,500 lbf/in</td>
                <td>Sheet metal blanking and sheet stripper pad clamping</td>
              </tr>
            </tbody>
          </table>

          <h2>5. Worked Engineering Case Study: Vehicle Suspension Coil Jounce Design</h2>
          <div class="worked-example-card">
            <h3>Problem Statement</h3>
            <p>An automotive chassis development engineer is sizing the front suspension coil spring for an electric passenger vehicle. The corner sprung mass supported by the front left wheel assembly is \(m = 420\text{ kg}\). Under normal stationary curb load, the coil spring must compress by exactly \(x_0 = 70\text{ mm}\) (\(0.070\text{ m}\)) to achieve the target vehicle ride height. During an extreme \(2.5g\) bump impact event, the suspension jounce bumper allows an additional \(x_{\text{bump}} = 55\text{ mm}\) of compression travel.</p>
            <p><strong>Required:</strong></p>
            <ol>
              <li>Compute the required spring stiffness constant \(k\) in \(\text{N/m}\) and \(\text{N/mm}\).</li>
              <li>Determine the maximum compressive restoring force \(F_{\max}\) exerted by the spring at full jounce travel (\(x_{\text{total}} = 125\text{ mm}\)).</li>
              <li>Calculate the total elastic potential energy \(U_{\max}\) absorbed by the spring at peak compression.</li>
              <li>Determine the natural vertical bounce frequency \(f_0\) of the corner mass.</li>
            </ol>

            <h3>Step-by-Step Mathematical Solution</h3>
            <p><strong>Step 1: Calculate static corner weight force \(F_{\text{static}}\):</strong></p>
            <div class="math-block">
              $$F_{\text{static}} = m \cdot g = 420\text{ kg} \times 9.80665\text{ m/s}^2 = 4,118.8\text{ N (4.12 kN)}$$
            </div>

            <p><strong>Step 2: Calculate spring constant \(k\):</strong></p>
            <div class="math-block">
              $$k = \frac{F_{\text{static}}}{x_0} = \frac{4,118.8\text{ N}}{0.070\text{ m}} = 58,840\text{ N/m} = 58.84\text{ N/mm}$$
            </div>
            <p>Converting to US automotive units: \(58.84\text{ N/mm} \times 5.71015 \approx 336.0\text{ lbf/in}\).</p>

            <p><strong>Step 3: Calculate peak compressive force \(F_{\max}\) at full jounce:</strong></p>
            <p>Total displacement: \(x_{\text{total}} = 70\text{ mm} + 55\text{ mm} = 125\text{ mm} = 0.125\text{ m}\).</p>
            <div class="math-block">
              $$F_{\max} = k \cdot x_{\text{total}} = 58,840\text{ N/m} \times 0.125\text{ m} = 7,355.0\text{ N (7.36 kN or 1,653.5 lbf)}$$
            </div>

            <p><strong>Step 4: Compute peak absorbed elastic potential energy \(U_{\max}\):</strong></p>
            <div class="math-block">
              $$U_{\max} = \frac{1}{2} k x_{\text{total}}^2 = \frac{1}{2} \times 58,840 \times (0.125)^2 = 29,420 \times 0.015625 \approx 459.7\text{ Joules}$$
            </div>

            <p><strong>Step 5: Determine corner natural oscillation frequency \(f_0\):</strong></p>
            <div class="math-block">
              $$f_0 = \frac{1}{2\pi} \sqrt{\frac{k}{m}} = \frac{1}{2\pi} \sqrt{\frac{58,840}{420}} = \frac{1}{2\pi} \sqrt{140.1} = \frac{11.836}{6.2832} \approx 1.88\text{ Hz}$$
            </div>
            <p><strong>Chassis Dynamic Evaluation:</strong> A natural bounce frequency of \(1.88\text{ Hz}\) provides firm, sport-oriented vehicle handling while remaining within the human comfort boundary for European automotive ride quality standards (typically \(1.2\text{ to }2.0\text{ Hz}\)).</p>
          </div>

          <h2>6. Elastic Limits, Yielding, and Spring Fatigue</h2>
          <p>Real-world springs do not follow Hooke's law indefinitely. In mechanical design, materials exhibit distinct stress-strain behavioral regimes:</p>
          <ul>
            <li><strong>Elastic Limit & Yield Strength (\(\sigma_y\)):</strong> When shear stress inside the helical wire coils exceeds the material's yield strength (\(\tau > \tau_y\)), microscopic dislocations slide irreversibly through the crystal lattice. The spring undergoes permanent set (plastic deformation) and will fail to return to its original free height.</li>
            <li><strong>Mechanical Hysteresis:</strong> During rapid cyclic compression, internal atomic friction dissipates a small fraction of deformation energy as heat, causing the unloading curve on a force-deflection plot to lag below the loading curve. This hysteresis loop represents internal damping.</li>
          </ul>

          <h2>7. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-item">
            <h3>Why is the spring constant sometimes written with a negative sign?</h3>
            <p>The negative sign in \(F = -kx\) is a vector convention indicating that the force is a <em>restoring force</em>: if the spring is stretched forward (\(x > 0\)), the spring pulls backward (\(F < 0\)). When analyzing scalar magnitudes in engineering sizing, the negative sign is often dropped (\(F = kx\)).</p>
          </div>
          <div class="faq-item">
            <h3>How does temperature affect the spring constant?</h3>
            <p>Elevated operating temperatures expand interatomic lattice spacing and decrease the shear modulus (\(G\)) of the spring steel alloy. Consequently, the spring constant \(k\) softens slightly as temperature rises (typically \(1\%\text{ to }2\%\) reduction per \(50^\circ\text{C}\) rise in standard steel).</p>
          </div>
          <div class="faq-item">
            <h3>What is the relationship between Hooke's Law and Young's Modulus?</h3>
            <p>Hooke's Law for a 1D spring (\(F = kx\)) is the macroscopic integral of the microscopic continuum stress-strain relationship: \(\sigma = E \cdot \epsilon\), where \(\sigma = F/A\) is normal stress, \(\epsilon = \Delta L / L\) is engineering strain, and \(E\) is Young's Modulus of elasticity. For a uniform rod, the effective spring constant is \(k = E \cdot A / L\).</p>
          </div>
          <div class="faq-item">
            <h3>How do you calculate spring rate for a helical coil spring from geometry?</h3>
            <p>The theoretical spring rate of a round-wire helical coil spring is \(k = (G \cdot d^4) / (8 \cdot D^3 \cdot N_a)\), where \(G\) is shear modulus, \(d\) is wire diameter, \(D\) is mean coil diameter, and \(N_a\) is the number of active coils.</p>
          </div>
        </article>
      </div>

      <aside class="sidebar" id="toolSidebar">
        <!-- Injected via apply_sidebars_all.py -->
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <p>&copy; 2026 CalcHub. All rights reserved. Precision engineering, science, and technical calculation tools.</p>
    </div>
  </footer>

  <script>
    // Hooke's Law Calculation Engine
    const toNpm = (k, unit) => {
      switch(unit) {
        case 'npmm': return k * 1000;
        case 'lbpin': return k * 175.126835;
        default: return k;
      }
    };
    const fromNpm = (k, unit) => {
      switch(unit) {
        case 'npmm': return k / 1000;
        case 'lbpin': return k / 175.126835;
        default: return k;
      }
    };
    const toMeters = (x, unit) => {
      switch(unit) {
        case 'mm': return x / 1000;
        case 'cm': return x / 100;
        case 'in': return x * 0.0254;
        default: return x;
      }
    };
    const toNewtons = (f, unit) => {
      switch(unit) {
        case 'kn': return f * 1000;
        case 'lbf': return f * 4.4482216;
        case 'kgf': return f * 9.80665;
        default: return f;
      }
    };

    function updateMode() {
      const mode = document.getElementById('calcMode').value;
      document.getElementById('rowMain').style.display = mode === 'solve_network' ? 'none' : 'flex';
      document.getElementById('rowNetwork').style.display = mode === 'solve_network' ? 'flex' : 'none';

      document.getElementById('grpK').style.display = 'block';
      document.getElementById('grpX').style.display = 'block';
      document.getElementById('grpF').style.display = 'none';

      if (mode === 'solve_k') {
        document.getElementById('grpK').style.display = 'none';
        document.getElementById('grpF').style.display = 'block';
      } else if (mode === 'solve_x') {
        document.getElementById('grpX').style.display = 'none';
        document.getElementById('grpF').style.display = 'block';
      }
      calculate();
    }

    function calculate() {
      const mode = document.getElementById('calcMode').value;
      const rawMass = parseFloat(document.getElementById('attachedMass').value) || 0;

      let calc_k = 0, calc_x = 0, calc_f = 0, calc_u = 0;

      if (mode === 'solve_network') {
        const k1 = parseFloat(document.getElementById('valK1').value) || 0;
        const k2 = parseFloat(document.getElementById('valK2').value) || 0;
        const k_par = k1 + k2;
        const k_ser = (k1 > 0 && k2 > 0) ? (k1 * k2) / (k1 + k2) : 0;

        document.getElementById('resPrimaryLabel').textContent = "Parallel Network Stiffness (k_parallel)";
        document.getElementById('resPrimaryVal').textContent = k_par.toFixed(1) + " N/m (" + (k_par / 1000).toFixed(3) + " N/mm)";
        document.getElementById('resPrimarySub').textContent = 
          "Series Network Stiffness: " + k_ser.toFixed(1) + " N/m (" + (k_ser / 1000).toFixed(3) + " N/mm)";

        document.getElementById('resEnergy').textContent = "N/A (Displacement Variable)";
        document.getElementById('resStiffness').textContent = "k₁: " + k1 + " N/m | k₂: " + k2 + " N/m";

        if (rawMass > 0) {
          const f_par = (1 / (2 * Math.PI)) * Math.sqrt(k_par / rawMass);
          const f_ser = (1 / (2 * Math.PI)) * Math.sqrt(k_ser / rawMass);
          document.getElementById('resFreq').textContent = f_par.toFixed(2) + " Hz (Par) | " + f_ser.toFixed(2) + " Hz (Ser)";
          document.getElementById('resPeriod').textContent = (1/f_par).toFixed(3) + " s (Par) | " + (1/f_ser).toFixed(3) + " s (Ser)";
        }
        return;
      }

      if (mode === 'solve_f') {
        calc_k = toNpm(parseFloat(document.getElementById('valK').value) || 0, document.getElementById('unitK').value);
        calc_x = toMeters(parseFloat(document.getElementById('valX').value) || 0, document.getElementById('unitX').value);
        calc_f = calc_k * calc_x;
        calc_u = 0.5 * calc_k * calc_x * calc_x;
      } else if (mode === 'solve_k') {
        calc_f = toNewtons(parseFloat(document.getElementById('valF').value) || 0, document.getElementById('unitF').value);
        calc_x = toMeters(parseFloat(document.getElementById('valX').value) || 0.001, document.getElementById('unitX').value);
        calc_k = calc_x > 0 ? calc_f / calc_x : 0;
        calc_u = 0.5 * calc_k * calc_x * calc_x;
      } else if (mode === 'solve_x') {
        calc_f = toNewtons(parseFloat(document.getElementById('valF').value) || 0, document.getElementById('unitF').value);
        calc_k = toNpm(parseFloat(document.getElementById('valK').value) || 1, document.getElementById('unitK').value);
        calc_x = calc_k > 0 ? calc_f / calc_k : 0;
        calc_u = 0.5 * calc_k * calc_x * calc_x;
      }

      // Render Primary Box
      if (mode === 'solve_f') {
        document.getElementById('resPrimaryLabel').textContent = "Spring Restoring Force (F)";
        document.getElementById('resPrimaryVal').textContent = calc_f.toFixed(1) + " N";
        document.getElementById('resPrimarySub').textContent = 
          "Equivalent to " + (calc_f / 4.44822).toFixed(2) + " lbf (" + (calc_f / 9.80665).toFixed(2) + " kgf)";
      } else if (mode === 'solve_k') {
        document.getElementById('resPrimaryLabel').textContent = "Calculated Spring Constant (k)";
        document.getElementById('resPrimaryVal').textContent = calc_k.toFixed(1) + " N/m (" + (calc_k / 1000).toFixed(3) + " N/mm)";
        document.getElementById('resPrimarySub').textContent = "Equivalent to " + (calc_k / 175.127).toFixed(2) + " lbf/in";
      } else if (mode === 'solve_x') {
        document.getElementById('resPrimaryLabel').textContent = "Displacement Elongation / Compression (x)";
        document.getElementById('resPrimaryVal').textContent = (calc_x * 1000).toFixed(2) + " mm (" + calc_x.toFixed(4) + " m)";
        document.getElementById('resPrimarySub').textContent = "Equivalent to " + (calc_x / 0.0254).toFixed(3) + " inches";
      }

      // Render Grid Items
      if (calc_u > 1000) {
        document.getElementById('resEnergy').textContent = (calc_u / 1000).toFixed(3) + " kJ (" + calc_u.toFixed(1) + " J)";
      } else {
        document.getElementById('resEnergy').textContent = calc_u.toFixed(3) + " Joules (" + (calc_u * 0.737562).toFixed(3) + " ft-lb)";
      }

      document.getElementById('resStiffness').textContent = 
        calc_k.toLocaleString('en-US', {maximumFractionDigits: 1}) + " N/m (" + (calc_k / 1000).toFixed(3) + " N/mm)";

      if (rawMass > 0 && calc_k > 0) {
        const omega0 = Math.sqrt(calc_k / rawMass);
        const f0 = omega0 / (2 * Math.PI);
        const T0 = f0 > 0 ? 1 / f0 : 0;
        document.getElementById('resFreq').textContent = f0.toFixed(2) + " Hz (" + omega0.toFixed(2) + " rad/s)";
        document.getElementById('resPeriod').textContent = T0.toFixed(3) + " seconds";
      } else {
        document.getElementById('resFreq').textContent = "N/A (Specify mass)";
        document.getElementById('resPeriod').textContent = "N/A (Specify mass)";
      }
    }

    document.getElementById('calcMode').addEventListener('change', updateMode);
    document.querySelectorAll('input, select').forEach(el => {
      el.addEventListener('input', calculate);
      el.addEventListener('change', calculate);
    });
    document.getElementById('calcBtn').addEventListener('click', calculate);
    document.getElementById('resetBtn').addEventListener('click', () => {
      document.getElementById('calcMode').value = 'solve_f';
      document.getElementById('valK').value = '2500';
      document.getElementById('valX').value = '0.08';
      document.getElementById('valF').value = '200';
      document.getElementById('attachedMass').value = '5.0';
      updateMode();
    });

    window.addEventListener('DOMContentLoaded', updateMode);
  </script>
</body>
</html>
"""

TOOL_2_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Kinetic Energy Calculator | Translational, Rotational & Relativistic</title>
  <meta name="description" content="Calculate translational kinetic energy (½mv²), rotational kinetic energy (½Iω²), relativistic energy, momentum, and impact stopping work.">
  <link rel="canonical" href="https://calchub.cloud/kinetic-energy-calculator.html">
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
        "name": "Kinetic Energy Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates classical translational kinetic energy, flywheel rotational energy, relativistic speeds, linear momentum, and equivalent TNT impact energy.",
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
            "name": "What is the classical translational kinetic energy formula?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The classical formula for translational kinetic energy is E_k = ½ × m × v², where 'm' is mass in kilograms and 'v' is velocity in meters per second. Kinetic energy is measured in Joules (1 J = 1 kg·m²/s²)."
            }
          },
          {
            "@type": "Question",
            "name": "Why does doubling a vehicle's speed quadruple its kinetic energy?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Because kinetic energy scales with the square of velocity (E_k ∝ v²), doubling speed (2v) produces (2v)² = 4v² kinetic energy. According to the work-energy theorem (W = F × d), vehicle brakes must dissipate four times more energy, quadrupling the required physical stopping distance."
            }
          },
          {
            "@type": "Question",
            "name": "How is rotational kinetic energy formulated?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Rotational kinetic energy is formulated as E_rot = ½ × I × ω², where 'I' is the mass moment of inertia in kg·m² and 'ω' is angular velocity in radians per second (rad/s)."
            }
          },
          {
            "@type": "Question",
            "name": "When does the classical kinetic energy equation fail and require relativistic physics?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "When an object travels faster than approximately 10% the speed of light (v > 0.1c ≈ 30,000 km/s), classical mechanics introduces significant error. Einstein's special relativity must be used: E_k = (γ - 1)mc², where γ = 1 / √(1 - v²/c²)."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body>
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="logo">CalcHub</a>
      <nav class="nav-links">
        <a href="index.html">Home</a>
        <a href="physics.html" class="active">Physics</a>
        <a href="mechanical.html">Mechanical</a>
        <a href="engineering.html">Electrical</a>
        <a href="civil.html">Civil</a>
      </nav>
    </div>
  </header>

  <main class="page-container">
    <div class="content-wrapper">
      <div class="calculator-container">
        <h1>Kinetic Energy Calculator</h1>
        <p class="lead-text">Calculate translational kinetic energy (½mv²), rotational kinetic energy (½Iω²), linear momentum, relativistic speeds, and explosive TNT equivalent work.</p>

        <div class="calc-card">
          <div class="form-row">
            <div class="form-group col-half">
              <label for="keMode">Kinetic Energy Mode</label>
              <select id="keMode" class="form-control">
                <option value="trans" selected>Translational Motion (½ m v²)</option>
                <option value="rot">Rotational Flywheel Motion (½ I ω²)</option>
                <option value="both">Rolling Body (Translational + Rotational)</option>
              </select>
            </div>

            <div class="form-group col-half">
              <label for="massVal">Object Mass (m)</label>
              <div class="input-with-unit">
                <input type="number" id="massVal" class="form-control" value="1500" step="any" min="0.0001">
                <select id="massUnit" class="unit-select">
                  <option value="kg" selected>kg</option>
                  <option value="lbs">lbs</option>
                  <option value="ton">Metric Tons</option>
                  <option value="g">grams (g)</option>
                </select>
              </div>
            </div>
          </div>

          <div class="form-row" id="rowLinear">
            <div class="form-group col-full">
              <label for="velVal">Translational Linear Velocity (v)</label>
              <div class="input-with-unit">
                <input type="number" id="velVal" class="form-control" value="100" step="any" min="0">
                <select id="velUnit" class="unit-select">
                  <option value="kph" selected>km/h</option>
                  <option value="mps">m/s</option>
                  <option value="mph">mph</option>
                  <option value="fps">ft/s</option>
                </select>
              </div>
            </div>
          </div>

          <div class="form-row" id="rowRot" style="display:none;">
            <div class="form-group col-half">
              <label for="rotSpeed">Rotational Speed (RPM / ω)</label>
              <div class="input-with-unit">
                <input type="number" id="rotSpeed" class="form-control" value="3000" step="any" min="0">
                <select id="rotUnit" class="unit-select">
                  <option value="rpm" selected>RPM</option>
                  <option value="radps">rad/s</option>
                </select>
              </div>
            </div>

            <div class="form-group col-half">
              <label for="rotorShape">Rotor Shape (Moment of Inertia I)</label>
              <select id="rotorShape" class="form-control">
                <option value="disk" selected>Solid Cylinder / Disk (I = ½ m r²)</option>
                <option value="ring">Thin Cylindrical Ring / Rim (I = m r²)</option>
                <option value="sphere">Solid Sphere (I = ⅖ m r²)</option>
              </select>
            </div>

            <div class="form-group col-full">
              <label for="rotorRadius">Rotor Radius (r)</label>
              <div class="input-with-unit">
                <input type="number" id="rotorRadius" class="form-control" value="0.3" step="any" min="0.001">
                <select id="radUnit" class="unit-select">
                  <option value="m" selected>Meters (m)</option>
                  <option value="cm">Centimeters (cm)</option>
                  <option value="in">Inches (in)</option>
                </select>
              </div>
            </div>
          </div>

          <div class="btn-group">
            <button type="button" id="calcBtn" class="btn btn-primary">Calculate Kinetic Energy</button>
            <button type="button" id="resetBtn" class="btn btn-secondary">Reset to Passenger Car (100 km/h)</button>
          </div>

          <div id="resultsPanel" class="results-panel">
            <div class="result-box primary-result">
              <div class="result-label">Total Kinetic Energy (E_k)</div>
              <div class="result-value" id="resEk">578.7 kJ</div>
              <div class="result-sub" id="resEkSub">578,704 Joules • 426,832 ft-lbf • 0.161 kWh</div>
            </div>

            <div class="result-grid">
              <div class="result-item">
                <span class="sub-label">Linear Momentum (p = mv)</span>
                <span class="sub-value" id="resMom">41,667 kg·m/s (N·s)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Equivalent TNT Explosive Energy</span>
                <span class="sub-value" id="resTnt">138.3 grams TNT</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Velocity / Speed</span>
                <span class="sub-value" id="resVelOut">27.78 m/s (100.0 km/h)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Relativistic Beta Factor (v/c)</span>
                <span class="sub-value" id="resBeta">9.27 × 10⁻⁸ (Classical Regime)</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. Classical Mechanics of Kinetic Energy & The Work-Energy Theorem</h2>
          <p>Kinetic energy (\(E_k\)) represents the capacity of a physical body to perform mechanical work by virtue of being in motion. In Newtonian mechanics, accelerating a stationary mass \(m\) from rest to a translational velocity \(v\) requires applying a net force \(\vec{F}_{\text{net}}\) over a spatial displacement path \(\vec{s}\). According to the fundamental <strong>Work-Energy Theorem</strong>, the mechanical work \(W_{\text{net}}\) performed on the object precisely equals its accumulated kinetic energy:</p>
          <div class="math-block">
            $$W_{\text{net}} = \int \vec{F}_{\text{net}} \cdot d\vec{s} = \int (m \vec{a}) \cdot d\vec{s} = m \int \left(\frac{dv}{dt}\right) v\,dt = m \int_0^v v'\,dv' = \frac{1}{2} m v^2$$
          </div>
          <p>The standard SI unit of kinetic energy is the <strong>Joule</strong> (\(\text{J} = \text{kg}\cdot\text{m}^2/\text{s}^2 = \text{N}\cdot\text{m}\)). The quadratic scaling with velocity (\(E_k \propto v^2\)) is one of the most consequential truths in all of applied physics: doubling travel speed quadruples kinetic energy; tripling speed increases kinetic energy by ninefold.</p>

          <h2>2. Relationship between Kinetic Energy and Linear Momentum</h2>
          <p>While linear momentum (\(p = mv\)) measures an object's resistance to having its motion stopped over a duration of time (\(F = \Delta p / \Delta t\)), kinetic energy measures the work dissipated across spatial distance (\(W = F \cdot d\)). Combining both formulations yields the classical momentum-energy relation:</p>
          <div class="math-block">
            $$E_k = \frac{p^2}{2m} \quad \iff \quad p = \sqrt{2m E_k}$$
          </div>
          <p>This formulation explains why high-velocity, lightweight projectiles (such as a 4-gram rifle bullet traveling at \(900\text{ m/s}\)) carry moderate momentum (\(p = 3.6\text{ N}\cdot\text{s}\)) but devastating kinetic energy (\(E_k = 1,620\text{ J}\)), whereas a heavy freight train car creeping at \(0.1\text{ m/s}\) carries massive momentum but modest kinetic energy.</p>

          <h2>3. Rotational Kinetic Energy of Spinning Bodies</h2>
          <p>For a rigid rotating body—such as an automotive engine flywheel, a gas turbine rotor, or a gyroscope—every differential mass element \(dm\) moves with linear tangential velocity \(v = \omega r\). Integrating the kinetic energy across all elements yields:</p>
          <div class="math-block">
            $$E_{\text{rot}} = \int \frac{1}{2} v^2\,dm = \frac{1}{2} \omega^2 \int r^2\,dm = \frac{1}{2} I \omega^2$$
          </div>
          <p>Where \(I\) is the <strong>mass moment of inertia</strong> (\(\text{kg}\cdot\text{m}^2\)) and \(\omega\) is angular velocity in radians per second (\(\text{rad/s}\)). For a rolling wheel or ball undergoing combined translation and rotation without slipping (\(v = \omega r\)), the total kinetic energy is:</p>
          <div class="math-block">
            $$E_{\text{total}} = E_{\text{trans}} + E_{\text{rot}} = \frac{1}{2} m v^2 + \frac{1}{2} I \omega^2$$
          </div>

          <h2>4. Real-World Engineering Benchmark Reference Table</h2>
          <p>To assist automotive crash engineers, ballistics analysts, and aerospace designers, the table below documents representative kinetic energies across diverse scales of motion:</p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Physical Object / System</th>
                <th>Mass (\(m\))</th>
                <th>Velocity (\(v\))</th>
                <th>Kinetic Energy (\(E_k\))</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Thermal Electron in Semiconductor (300 K)</td>
                <td>\(9.109 \times 10^{-31}\text{ kg}\)</td>
                <td>117 km/s (Thermal)</td>
                <td>\(6.21 \times 10^{-21}\text{ J}\) (0.0388 eV)</td>
              </tr>
              <tr>
                <td>Baseball Pitch (Major League Fastball, 100 mph)</td>
                <td>145 g (0.145 kg)</td>
                <td>44.7 m/s (161 km/h)</td>
                <td>145 Joules (107 ft-lb)</td>
              </tr>
              <tr>
                <td>Olympic 100m Sprinter (Usain Bolt at Top Speed)</td>
                <td>94 kg</td>
                <td>12.4 m/s (44.7 km/h)</td>
                <td>7,227 Joules (7.23 kJ)</td>
              </tr>
              <tr>
                <td>Police Duty Handgun Round (9mm Luger 124 gr)</td>
                <td>8.03 g</td>
                <td>350 m/s (1,150 ft/s)</td>
                <td>492 Joules (363 ft-lb)</td>
              </tr>
              <tr>
                <td>Family SUV on Highway (120 km/h cruising)</td>
                <td>2,200 kg</td>
                <td>33.3 m/s (120 km/h)</td>
                <td>1.221 Megajoules (1,221 kJ)</td>
              </tr>
              <tr>
                <td>High-Speed Passenger Train (TGV at 320 km/h)</td>
                <td>400 tonnes</td>
                <td>88.9 m/s (320 km/h)</td>
                <td>1.58 Gigajoules (1,580 MJ)</td>
              </tr>
              <tr>
                <td>International Space Station in LEO Orbit</td>
                <td>420 tonnes</td>
                <td>7,660 m/s (27,580 km/h)</td>
                <td>12.3 Terajoules (12,300,000 MJ)</td>
              </tr>
            </tbody>
          </table>

          <h2>5. Worked Engineering Case Study: Vehicle Highway Crash Energy Dissipation</h2>
          <div class="worked-example-card">
            <h3>Problem Statement</h3>
            <p>A civil transportation highway agency is designing an energy-absorbing crash cushion barrier (attenuator) at a freeway bifurcation gore point. The design crash scenario stipulates a fully loaded pickup truck with total mass \(m = 2,400\text{ kg}\) impacting the barrier at a speed of \(v = 110\text{ km/h}\) (\(30.556\text{ m/s}\)). The collapsible barrier must decelerate the vehicle to a complete stop (\(v = 0\)) over a maximum allowable crushing stroke distance of \(d = 6.0\text{ meters}\).</p>
            <p><strong>Required:</strong></p>
            <ol>
              <li>Compute the initial kinetic energy \(E_k\) that must be dissipated by the barrier.</li>
              <li>Determine the average deceleration force \(F_{\text{avg}}\) that the crushable steel cartridges must exert.</li>
              <li>Calculate the uniform passenger deceleration rate in \(\text{m/s}^2\) and standardized G-forces (\(g\)).</li>
            </ol>

            <h3>Step-by-Step Mathematical Solution</h3>
            <p><strong>Step 1: Convert velocity to standard SI metric units:</strong></p>
            <div class="math-block">
              $$v = \frac{110\text{ km/h}}{3.6} = 30.556\text{ m/s}$$
            </div>

            <p><strong>Step 2: Calculate total translational kinetic energy \(E_k\):</strong></p>
            <div class="math-block">
              $$E_k = \frac{1}{2} m v^2 = \frac{1}{2} \times 2,400\text{ kg} \times (30.556\text{ m/s})^2 = 1,200 \times 933.64 \approx 1,120,370\text{ Joules (1.12 MJ)}$$
            </div>
            <p>Converting to electrical and explosive equivalents: \(1.12\text{ MJ} \approx 0.311\text{ kWh}\), or the explosive chemical energy contained in roughly \(268\text{ grams of TNT}\).</p>

            <p><strong>Step 3: Calculate average required crash barrier braking force \(F_{\text{avg}}\):</strong></p>
            <p>Applying the Work-Energy Theorem (\(W = F_{\text{avg}} \cdot d = \Delta E_k\)):</p>
            <div class="math-block">
              $$F_{\text{avg}} = \frac{E_k}{d} = \frac{1,120,370\text{ J}}{6.0\text{ m}} \approx 186,728\text{ N (186.7 kN)}$$
            </div>
            <p>Converting to gravitational force units: \(186.7\text{ kN} \div 4.44822 \approx 41,978\text{ lbf}\).</p>

            <p><strong>Step 4: Determine passenger cabin deceleration rate:</strong></p>
            <div class="math-block">
              $$a = \frac{F_{\text{avg}}}{m} = \frac{186,728\text{ N}}{2,400\text{ kg}} \approx 77.80\text{ m/s}^2$$
            </div>
            <div class="math-block">
              $$\text{G-force} = \frac{a}{9.80665} = \frac{77.80}{9.80665} \approx 7.93\text{ g}$$
            </div>
            <p><strong>Engineering Design Verdict:</strong> Under MASH (Manual for Assessing Safety Hardware) guidelines, an average vehicle deceleration of \(7.93g\) over \(6\text{ meters}\) falls safely below the human occupant severe injury threshold (\(< 12g\)), confirming that the 6-meter cartridge length is adequate.</p>
          </div>

          <h2>6. Einstein's Relativistic Kinetic Energy at High Velocities</h2>
          <p>When particle velocities approach the speed of light in a vacuum (\(c = 299,792,458\text{ m/s}\)), the classical formula \(E_k = \frac{1}{2}mv^2\) severely underestimates the work required for acceleration because relativistic mass increases without bound. Under Einstein's Special Relativity, the true kinetic energy is:</p>
          <div class="math-block">
            $$E_k = (\gamma - 1) m c^2 \quad \text{where } \gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}$$
          </div>
          <p>Expanding the Lorentz factor \(\gamma\) via binomial series (\(\gamma \approx 1 + \frac{1}{2}\frac{v^2}{c^2} + \frac{3}{8}\frac{v^4}{c^4} + \dots\)) demonstrates that at low everyday speeds (\(v \ll c\)), the higher-order terms vanish, reducing Einstein's relativistic equation exactly back to Newton's \(\frac{1}{2}mv^2\).</p>

          <h2>7. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-item">
            <h3>Can kinetic energy ever be a negative value?</h3>
            <p>No. In classical physics, mass \(m\) is always positive and velocity is squared (\(v^2 \ge 0\)), making kinetic energy strictly non-negative (\(E_k \ge 0\)). It equals zero if and only if the object is completely stationary relative to the reference frame.</p>
          </div>
          <div class="faq-item">
            <h3>Is kinetic energy dependent on the observer's frame of reference?</h3>
            <p>Yes. Because velocity is relative to the observer, kinetic energy is frame-dependent. A passenger seated inside a cruising passenger jet has zero kinetic energy relative to the aircraft cabin, but possesses hundreds of kilojoules of kinetic energy relative to an observer on the ground.</p>
          </div>
          <div class="faq-item">
            <h3>What is the difference between elastic and inelastic collisions regarding kinetic energy?</h3>
            <p>In a perfectly elastic collision (such as colliding subatomic billiard balls), total kinetic energy is conserved before and after the collision (\(\Sigma E_{k,\text{initial}} = \Sigma E_{k,\text{final}}\)). In an inelastic collision (such as a car crash), a large portion of kinetic energy is permanently dissipated into heat, sound, and plastic structural deformation.</p>
          </div>
          <div class="faq-item">
            <h3>How do flywheels store kinetic energy in hybrid vehicles?</h3>
            <p>Flywheel energy storage systems convert braking energy into rotational kinetic energy (\(E = \frac{1}{2}I\omega^2\)) by spinning a carbon-fiber rotor in a vacuum enclosure at up to 60,000 RPM. Upon acceleration, the rotor drives an electric motor-generator to feed electrical power back into the vehicle drivetrain without chemical battery wear.</p>
          </div>
        </article>
      </div>

      <aside class="sidebar" id="toolSidebar">
        <!-- Injected via apply_sidebars_all.py -->
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <p>&copy; 2026 CalcHub. All rights reserved. Precision engineering, science, and technical calculation tools.</p>
    </div>
  </footer>

  <script>
    // Kinetic Energy Calculation Engine
    const c_light = 299792458;

    const toKg = (m, unit) => {
      switch(unit) {
        case 'lbs': return m * 0.45359237;
        case 'ton': return m * 1000;
        case 'g': return m / 1000;
        default: return m;
      }
    };
    const toMps = (v, unit) => {
      switch(unit) {
        case 'kph': return v / 3.6;
        case 'mph': return v * 0.44704;
        case 'fps': return v * 0.3048;
        default: return v;
      }
    };
    const toRadPerSec = (rot, unit) => {
      return unit === 'rpm' ? rot * (Math.PI / 30) : rot;
    };
    const toMeters = (r, unit) => {
      switch(unit) {
        case 'cm': return r / 100;
        case 'in': return r * 0.0254;
        default: return r;
      }
    };

    function updateMode() {
      const m = document.getElementById('keMode').value;
      document.getElementById('rowLinear').style.display = m === 'rot' ? 'none' : 'flex';
      document.getElementById('rowRot').style.display = m === 'trans' ? 'none' : 'flex';
      calculate();
    }

    function calculate() {
      const mode = document.getElementById('keMode').value;
      const rawMass = parseFloat(document.getElementById('massVal').value) || 0;
      const m = toKg(rawMass, document.getElementById('massUnit').value);

      const rawVel = parseFloat(document.getElementById('velVal').value) || 0;
      const v = toMps(rawVel, document.getElementById('velUnit').value);

      let Ek_trans = 0;
      let Ek_rot = 0;

      if (mode !== 'rot') {
        Ek_trans = 0.5 * m * v * v;
      }

      if (mode !== 'trans') {
        const rawRot = parseFloat(document.getElementById('rotSpeed').value) || 0;
        const omega = toRadPerSec(rawRot, document.getElementById('rotUnit').value);
        const rawRadius = parseFloat(document.getElementById('rotorRadius').value) || 0.1;
        const r = toMeters(rawRadius, document.getElementById('radUnit').value);
        const shape = document.getElementById('rotorShape').value;

        let I = 0;
        if (shape === 'disk') I = 0.5 * m * r * r;
        else if (shape === 'ring') I = m * r * r;
        else if (shape === 'sphere') I = 0.4 * m * r * r;

        Ek_rot = 0.5 * I * omega * omega;
      }

      const totalEk = Ek_trans + Ek_rot;
      const momentum = m * v;
      const tntGrams = totalEk / 4184; // 1g TNT = 4,184 J
      const beta = v / c_light;

      // Render Primary Box
      if (totalEk > 1e9) {
        document.getElementById('resEk').textContent = (totalEk / 1e9).toFixed(3) + " GJ";
      } else if (totalEk > 1e6) {
        document.getElementById('resEk').textContent = (totalEk / 1e6).toFixed(3) + " MJ";
      } else if (totalEk > 1000) {
        document.getElementById('resEk').textContent = (totalEk / 1000).toFixed(2) + " kJ";
      } else {
        document.getElementById('resEk').textContent = totalEk.toFixed(2) + " Joules";
      }

      const ft_lbf = totalEk * 0.737562;
      const kWh = totalEk / 3600000;
      document.getElementById('resEkSub').textContent = 
        totalEk.toLocaleString('en-US', {maximumFractionDigits: 1}) + " Joules • " + 
        ft_lbf.toLocaleString('en-US', {maximumFractionDigits: 0}) + " ft-lbf • " + 
        kWh.toFixed(4) + " kWh";

      // Render Grid Items
      document.getElementById('resMom').textContent = 
        momentum.toLocaleString('en-US', {maximumFractionDigits: 1}) + " kg·m/s (N·s)";

      if (tntGrams > 1000000) {
        document.getElementById('resTnt').textContent = (tntGrams / 1000000).toFixed(3) + " Tons TNT";
      } else if (tntGrams > 1000) {
        document.getElementById('resTnt').textContent = (tntGrams / 1000).toFixed(2) + " kg TNT";
      } else {
        document.getElementById('resTnt').textContent = tntGrams.toFixed(2) + " grams TNT";
      }

      document.getElementById('resVelOut').textContent = 
        v.toFixed(2) + " m/s (" + (v * 3.6).toFixed(1) + " km/h | " + (v * 2.23694).toFixed(1) + " mph)";

      if (beta > 0.1) {
        document.getElementById('resBeta').textContent = beta.toFixed(4) + " (Relativistic Regime!)";
      } else {
        document.getElementById('resBeta').textContent = beta.toExponential(2) + " (Classical Regime)";
      }
    }

    document.getElementById('keMode').addEventListener('change', updateMode);
    document.querySelectorAll('input, select').forEach(el => {
      el.addEventListener('input', calculate);
      el.addEventListener('change', calculate);
    });

    document.getElementById('calcBtn').addEventListener('click', calculate);
    document.getElementById('resetBtn').addEventListener('click', () => {
      document.getElementById('keMode').value = 'trans';
      document.getElementById('massVal').value = '1500';
      document.getElementById('massUnit').value = 'kg';
      document.getElementById('velVal').value = '100';
      document.getElementById('velUnit').value = 'kph';
      updateMode();
    });

    window.addEventListener('DOMContentLoaded', updateMode);
  </script>
</body>
</html>
"""

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p1 = os.path.join(base_dir, "hookes-law-calculator.html")
    p2 = os.path.join(base_dir, "kinetic-energy-calculator.html")

    with open(p1, "w", encoding="utf-8") as f:
        f.write(TOOL_1_HTML)
    print(f"Generated {p1}")

    with open(p2, "w", encoding="utf-8") as f:
        f.write(TOOL_2_HTML)
    print(f"Generated {p2}")

if __name__ == "__main__":
    main()
