# -*- coding: utf-8 -*-
"""
Script to generate Batch 13 Part 1 tools:
1. footing-size-calculator.html
2. gravel-calculator.html
"""
import os

TOOL_1_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Footing Size Calculator | Spread Footing &amp; Soil Bearing Sizer</title>
  <meta name="description" content="Calculate concrete isolated spread footing dimensions, required plan area, ACI 318 two-way punching shear, and soil bearing capacity verification.">
  <link rel="canonical" href="https://calchub.cloud/footing-size-calculator.html">
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
        "name": "Footing Size Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates reinforced concrete isolated spread footing width, plan area, minimum structural depth, and two-way punching shear per ACI 318.",
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
            "name": "How is the required plan area of a spread footing calculated?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The required minimum plan area is computed by dividing total service vertical axial column load (Dead Load + Live Load + estimated self-weight of footing and soil surcharge) by allowable net soil bearing capacity: A_req = P_service / q_allow. For a square footing, the minimum width is B = sqrt(A_req)."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between gross and net soil bearing capacity?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Gross bearing capacity represents the total pressure the subsoil can support at the foundation depth. Net allowable bearing capacity subtracts the weight of the soil overburden previously resting on the founding stratum: q_net = q_gross - (gamma_soil * D_f), allowing direct design using superimposed column loads."
            }
          },
          {
            "@type": "Question",
            "name": "How does ACI 318 govern two-way punching shear in spread footings?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Punching shear is evaluated along a critical perimeter located at d/2 from the column face, where d is the effective depth of reinforcing steel. Concrete shear capacity without shear reinforcement is typically Vc = 4 * lambda * sqrt(f'c) * b0 * d (in psi) or 0.33 * lambda * sqrt(f'c) * b0 * d (in MPa)."
            }
          },
          {
            "@type": "Question",
            "name": "What is the minimum recommended footing thickness per building codes?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Per ACI 318-19 Section 13.3.1.2, footings on soil must have a minimum effective depth above bottom reinforcement of not less than 6 inches (150 mm), with an overall minimum total thickness of 10 to 12 inches (250 to 300 mm) to provide required rebar clear cover (3 inches / 75 mm against earth)."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="civil">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">
        <span class="logo-icon">&pi;</span>
        <span class="logo-text">Calc<strong>Hub</strong></span>
      </a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="engineering.html">Engineering</a>
        <a href="mechanical.html">Mechanical</a>
        <a href="civil.html" class="active">Civil &amp; Roof</a>
        <a href="solar-energy.html">Solar</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo; 
      <a href="civil.html">Civil &amp; Construction</a> &rsaquo; 
      <span>Footing Size Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calculator-main">
        <div class="calc-header">
          <h1>Footing Size Calculator</h1>
          <p>Dimension isolated spread footings, evaluate allowable soil bearing pressure, and verify ACI 318 two-way punching shear limits.</p>
        </div>

        <div class="calculator-card">
          <form id="footingForm" onsubmit="return false;">
            <div class="form-row">
              <div class="form-group">
                <label for="deadLoad">Unfactored Dead Load, D (kN):</label>
                <input type="number" id="deadLoad" value="450.0" step="10" min="0" required>
                <span class="hint">Permanent column structural self-weight</span>
              </div>
              <div class="form-group">
                <label for="liveLoad">Unfactored Live Load, L (kN):</label>
                <input type="number" id="liveLoad" value="250.0" step="10" min="0" required>
                <span class="hint">Occupancy and movable live loads</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="soilBearing">Allowable Soil Bearing Capacity, qₐ (kPa):</label>
                <input type="number" id="soilBearing" value="200.0" step="10" min="50" max="1000" required>
                <span class="hint">Net allowable bearing (e.g. 150-250 kPa for medium clay/sand)</span>
              </div>
              <div class="form-group">
                <label for="footingSelfWeight">Footing Self-Weight Allowance (%):</label>
                <input type="number" id="footingSelfWeight" value="10" step="1" min="5" max="20" required>
                <span class="hint">Typically 8% to 12% of vertical column load</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="columnWidth">Column Cross-Section (mm):</label>
                <input type="number" id="columnWidth" value="400" step="50" min="150" required>
                <span class="hint">Square column side dimension c (mm)</span>
              </div>
              <div class="form-group">
                <label for="concreteStrength">Concrete Compressive Strength, f'c (MPa):</label>
                <select id="concreteStrength">
                  <option value="20">20 MPa (C20/25 - Standard Footings)</option>
                  <option value="25" selected>25 MPa (C25/30 - Standard Structural)</option>
                  <option value="30">30 MPa (C30/37 - Heavy Foundations)</option>
                  <option value="35">35 MPa (C35/45 - Commercial Grade)</option>
                </select>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcFootingBtn">Size Spread Footing</button>
              <button type="reset" class="btn btn-secondary" id="resetFootingBtn">Reset</button>
            </div>
          </form>

          <div class="results-box" id="footingResultBox" style="display:none; margin-top:25px;">
            <h3>Structural Footing Dimensions &amp; Shear Evaluation</h3>
            <div class="result-grid">
              <div class="result-tile highlight">
                <span class="result-label">Recommended Footing Width (B)</span>
                <span class="result-value" id="resFootingWidth">0.00</span>
                <span class="result-unit">meters (Square B &times; B)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Total Footing Plan Area</span>
                <span class="result-value" id="resPlanArea">0.00</span>
                <span class="result-unit">m² (square meters)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Minimum Effective Depth (d)</span>
                <span class="result-value" id="resEffectiveDepth">0</span>
                <span class="result-unit">mm (Punching Shear Limit)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Total Footing Thickness (H)</span>
                <span class="result-value" id="resTotalDepth">0</span>
                <span class="result-unit">mm (d + 75 mm cover)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Factored Soil Pressure (q_u)</span>
                <span class="result-value" id="resFactoredPressure">0.0</span>
                <span class="result-unit">kPa (1.2D + 1.6L ultimate)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Concrete Volume per Footing</span>
                <span class="result-value" id="resConcreteVol">0.00</span>
                <span class="result-unit">m³ (~0 cement bags)</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Geotechnical Principles of Spread Footing Design</h2>
          <p>
            Shallow foundations transmit heavy superstructural loads—originating from multistory structural columns, shear walls, and bridge piers—safely into supporting soil or bedrock strata. An <strong>isolated spread footing</strong> (also termed a pad footing) is the most economical and widely deployed foundation system when competent bearing soils exist within shallow excavation depths ($1.0\text{ to }3.0\text{ meters}$).
          </p>
          <p>
            Foundation design requires a coupled geotechnical-structural methodology governed by <strong>building codes (ACI 318, Eurocode 7, and IS 456)</strong>:
          </p>
          <ul>
            <li><strong>Serviceability Limit State (Geotechnical Sizing):</strong> Footing plan dimensions ($B \times L$) are sized using unfactored service loads ($D + L$) to ensure the applied contact pressure does not exceed the allowable soil bearing capacity ($q_a$) or cause differential settlement exceeding $25\text{ mm}$ ($1.0\text{ inch}$).</li>
            <li><strong>Strength Limit State (Structural Dimensioning):</strong> Footing thickness ($H$), effective depth ($d$), and steel reinforcement ($A_s$) are designed using factored ultimate load combinations ($U = 1.2 D + 1.6 L$ under ASCE 7 / ACI 318) to prevent catastrophic two-way punching shear and one-way flexural failure.</li>
          </ul>

          <h2>Service Sizing Formulation for Plan Area</h2>
          <p>
            Let $P_D$ and $P_L$ represent the unfactored dead and live axial column loads. Because the self-weight of the concrete footing ($W_f$) and the soil backfill surcharge ($W_s$) resting above it contribute to downward pressure, civil engineers budget an allowance of $8\%$ to $12\%$ of total vertical service load:
          </p>
          <div class="formula-box">
            $$P_{service} = P_D + P_L$$
            $$P_{total} = P_{service} \times (1 + \beta_{self}) \quad (\beta_{self} \approx 0.10)$$
            $$A_{req} = \frac{P_{total}}{q_a}$$
          </div>
          <p>
            For a standard square isolated footing of width $B$:
          </p>
          <div class="formula-box">
            $$B = \sqrt{A_{req}} \implies B_{provided} = \lceil B \rceil \text{ rounded up to the nearest } 0.1\text{ meter}$$
            $$A_{actual} = B_{provided}^2$$
          </div>

          <h2>Factored Ultimate Soil Contact Pressure ($q_u$)</h2>
          <p>
            Once the physical plan area $A_{actual}$ is fixed, structural design of the concrete pad proceeds using factored ultimate column loads:
          </p>
          <div class="formula-box">
            $$P_u = 1.2 P_D + 1.6 P_L$$
            $$q_u = \frac{P_u}{A_{actual}} = \frac{1.2 P_D + 1.6 P_L}{B_{provided}^2}$$
          </div>
          <p>
            Notice that the self-weight of the footing is omitted when evaluating $q_u$ for shear and flexure, because footing mass exerts downward inertia that directly balances upward soil reaction, causing zero net bending stress in the slab.
          </p>

          <h2>ACI 318 Two-Way Punching Shear Mechanics</h2>
          <p>
            In reinforced concrete footings, <strong>two-way punching shear</strong> is universally the critical limit state dictating required slab depth. The concentrated column load attempts to punch a truncated pyramid-shaped concrete plug through the footing pad.
          </p>
          <p>
            Per <strong>ACI 318-19 Section 22.6</strong>, the critical shear perimeter ($b_0$) is located at a distance of $d/2$ from the perimeter of the column face. For a square column with side dimension $c$:
          </p>
          <div class="formula-box">
            $$b_0 = 4 \times (c + d)$$
          </div>
          <p>
            The factored punching shear force ($V_{u2}$) acting on this critical perimeter is the upward soil pressure outside the tributary punching cone:
          </p>
          <div class="formula-box">
            $$V_{u2} = q_u \times \left[ B_{provided}^2 - (c + d)^2 \right]$$
          </div>
          <p>
            The nominal concrete punching shear strength ($V_c$) without shear reinforcement is governed by the minimum of three criteria:
          </p>
          <div class="formula-box">
            $$V_c = \min \begin{cases} 
            0.33 \lambda \sqrt{f'_c} \, b_0 d \\ 
            0.17 \left(1 + \frac{2}{\beta}\right) \lambda \sqrt{f'_c} \, b_0 d \\ 
            0.083 \left(\frac{\alpha_s d}{b_0} + 2\right) \lambda \sqrt{f'_c} \, b_0 d 
            \end{cases} \quad (\text{SI units: MPa, mm, N})$$
          </div>
          <p>
            Where $\beta = 1.0$ for square columns, $\alpha_s = 40$ for interior columns, and shear reduction factor is $\phi = 0.75$. Sizing effective depth $d$ such that $\phi V_c \ge V_{u2}$ eliminates the need for expensive, labor-intensive shear stirrups.
          </p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Soil Classification</th>
                <th>Standard Penetration Test (SPT N-Value)</th>
                <th>Presumptive Bearing Capacity ($q_a$)</th>
                <th>Typical Foundation Type</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Soft Silt / Cohesive Clay</td>
                <td>N < 4</td>
                <td>50 – 75 kPa (1,000 – 1,500 psf)</td>
                <td>Deep piles or raft slab foundation</td>
              </tr>
              <tr>
                <td>Firm Sandy Silt / Medium Clay</td>
                <td>4 ≤ N ≤ 10</td>
                <td>100 – 150 kPa (2,000 – 3,000 psf)</td>
                <td>Wide spread pads or strip footings</td>
              </tr>
              <tr>
                <td>Stiff Clay / Medium Dense Sand</td>
                <td>10 ≤ N ≤ 30</td>
                <td>200 – 300 kPa (4,000 – 6,000 psf)</td>
                <td>Standard isolated spread footings</td>
              </tr>
              <tr>
                <td>Very Dense Gravelly Sand / Hard Clay</td>
                <td>30 ≤ N ≤ 50</td>
                <td>350 – 500 kPa (7,000 – 10,000 psf)</td>
                <td>Compact isolated spread pads</td>
              </tr>
              <tr>
                <td>Sound Sedimentary / Crystalline Bedrock</td>
                <td>N > 50 (Refusal)</td>
                <td>1,000 – 4,000 kPa (20,000+ psf)</td>
                <td>High-capacity rock bearing sockets</td>
              </tr>
            </tbody>
          </table>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: Sizing an Interior Column Spread Footing</h3>
            <p><strong>Design Scenario:</strong> A five-story commercial office building has an interior reinforced concrete column ($c = 450\text{ mm} \times 450\text{ mm}$) carrying an unfactored axial dead load of $P_D = 600\text{ kN}$ and an unfactored occupancy live load of $P_L = 350\text{ kN}$. Geotechnical site boreholes establish an allowable net soil bearing capacity of $q_a = 220\text{ kPa}$ at a founding depth of $D_f = 1.8\text{ meters}$. Structural concrete compressive strength is $f'_c = 25\text{ MPa}$ ($25\text{ N/mm}^2$), and steel yield strength is $F_y = 420\text{ MPa}$. Determine the required square footing width ($B$), factored soil contact pressure ($q_u$), minimum effective depth ($d$) for punching shear, total pad thickness ($H$), and concrete batch volume.</p>
            
            <p><strong>Step 1: Compute Service Loads and Required Plan Area ($A_{req}$)</strong></p>
            <div class="formula-box">
              $$P_{service} = P_D + P_L = 600\text{ kN} + 350\text{ kN} = 950\text{ kN}$$
              $$P_{total} = P_{service} \times 1.10 = 950\text{ kN} \times 1.10 = 1,045\text{ kN}$$
              $$A_{req} = \frac{P_{total}}{q_a} = \frac{1,045\text{ kN}}{220\text{ kPa}} = 4.75\text{ m}^2$$
              $$B = \sqrt{4.75} \approx 2.18\text{ m} \implies \text{Adopt } B = \mathbf{2.20\text{ meters}}$$
              $$A_{actual} = (2.20\text{ m})^2 = 4.84\text{ m}^2$$
            </div>

            <p><strong>Step 2: Calculate Factored Ultimate Soil Pressure ($q_u$)</strong></p>
            <div class="formula-box">
              $$P_u = 1.2 P_D + 1.6 P_L = 1.2(600) + 1.6(350) = 720 + 560 = 1,280\text{ kN}$$
              $$q_u = \frac{P_u}{A_{actual}} = \frac{1,280\text{ kN}}{4.84\text{ m}^2} = \mathbf{264.46\text{ kPa}} \quad (0.2645\text{ N/mm}^2)$$
            </div>

            <p><strong>Step 3: Evaluate Two-Way Punching Shear and Determine Effective Depth ($d$)</strong></p>
            <p>Assuming an effective depth of $d = 400\text{ mm}$:</p>
            <div class="formula-box">
              $$b_0 = 4 \times (c + d) = 4 \times (450 + 400) = 3,400\text{ mm}$$
              $$V_{u2} = q_u \times [B^2 - (c + d)^2] = 264.46 \times [4.84 - (0.85)^2] = 264.46 \times [4.84 - 0.7225] = \mathbf{1,088.9\text{ kN}}$$
              $$\phi V_c = 0.75 \times 0.33 \times \sqrt{25} \times 3,400 \times 400 = 0.75 \times 0.33 \times 5 \times 1.36 \times 10^6 \approx \mathbf{1,683\text{ kN}}$$
            </div>
            <p>
              Since $\phi V_c = 1,683\text{ kN} > V_{u2} = 1,088.9\text{ kN}$, $d = 400\text{ mm}$ provides ample punching shear capacity (safety margin $1.55$).
            </p>

            <p><strong>Step 4: Determine Overall Footing Thickness and Concrete Volume</strong></p>
            <div class="formula-box">
              $$H = d + \text{Clear Cover} + d_b = 400\text{ mm} + 75\text{ mm} + 20\text{ mm} \approx \mathbf{500\text{ mm}} \ (0.50\text{ m})$$
              $$V_{concrete} = B^2 \times H = 2.20\text{ m} \times 2.20\text{ m} \times 0.50\text{ m} = \mathbf{2.42\text{ m}^3}$$
            </div>
            <p>
              <strong>Engineering Conclusion:</strong> Sizing the footing pad at <strong>$2.20\text{ m} \times 2.20\text{ m} \times 0.50\text{ m}$</strong> ($2.42\text{ m}^3$ of $25\text{ MPa}$ concrete) completely satisfies both geotechnical bearing limits ($q_{max} \le 220\text{ kPa}$) and ACI 318 punching shear safety criteria.
            </p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Civil &amp; Foundation Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="concrete-calculator.html">Concrete Volume Calculator</a></li>
            <li><a href="rebar-calculator.html">Rebar Weight &amp; Grid Sizing</a></li>
            <li><a href="retaining-wall-calculator.html">Retaining Wall Stability</a></li>
            <li><a href="beam-calculator.html">Beam Bending &amp; Shear</a></li>
            <li><a href="excavation-calculator.html">Excavation Bank &amp; Haul</a></li>
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
          <li><a href="civil.html">Civil &amp; Construction</a></li>
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
      const calcBtn = document.getElementById('calcFootingBtn');
      const resetBtn = document.getElementById('resetFootingBtn');
      const resultBox = document.getElementById('footingResultBox');

      function calculateFooting() {
        const D = parseFloat(document.getElementById('deadLoad').value);
        const L = parseFloat(document.getElementById('liveLoad').value);
        const qa = parseFloat(document.getElementById('soilBearing').value);
        const selfPct = parseFloat(document.getElementById('footingSelfWeight').value) || 10;
        const c_mm = parseFloat(document.getElementById('columnWidth').value);
        const fc = parseFloat(document.getElementById('concreteStrength').value);

        if (isNaN(D) || D < 0 || isNaN(L) || L < 0 || isNaN(qa) || qa <= 0 || isNaN(c_mm) || c_mm <= 0) {
          alert('Please enter valid positive values for loads, soil bearing, and column dimensions.');
          return;
        }

        const P_service = D + L;
        const P_total = P_service * (1.0 + selfPct / 100.0);
        const A_req = P_total / qa;
        let B = Math.sqrt(A_req);
        B = Math.ceil(B * 10.0) / 10.0; // round up to nearest 0.1m
        const A_actual = B * B;

        const Pu = 1.2 * D + 1.6 * L;
        const qu = Pu / A_actual; // kPa (kN/m2)

        // Iterative punching shear depth d: phi*Vc >= Vu2
        // SI: phi*0.33*sqrt(fc)*b0*d >= qu * [B^2 - (c+d)^2]
        // where b0 = 4*(c+d)
        let d = 250.0; // start at 250mm
        const c_m = c_mm / 1000.0;
        const phi = 0.75;
        const sqrtFc = Math.sqrt(fc);

        for (let iter = 0; iter < 100; iter++) {
          const d_m = d / 1000.0;
          const b0_mm = 4.0 * (c_mm + d);
          const Vu2_kN = qu * (A_actual - Math.pow(c_m + d_m, 2));
          // phi * Vc (in kN)
          const phiVc_kN = (phi * 0.33 * sqrtFc * b0_mm * d) / 1000.0;

          if (phiVc_kN >= Vu2_kN) {
            break;
          }
          d += 10.0;
        }

        const H_mm = Math.ceil((d + 75.0 + 20.0) / 50.0) * 50.0; // round up to 50mm increment
        const H_m = H_mm / 1000.0;
        const concreteVol = B * B * H_m;

        document.getElementById('resFootingWidth').textContent = B.toFixed(2);
        document.getElementById('resPlanArea').textContent = A_actual.toFixed(2);
        document.getElementById('resEffectiveDepth').textContent = Math.round(d);
        document.getElementById('resTotalDepth').textContent = Math.round(H_mm);
        document.getElementById('resFactoredPressure').textContent = qu.toFixed(1);
        document.getElementById('resConcreteVol').textContent = concreteVol.toFixed(2);

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculateFooting);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
      });
      calculateFooting();
    });
  </script>
</body>
</html>
"""

TOOL_2_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gravel Calculator | Crushed Stone, Aggregate Tons &amp; Volume</title>
  <meta name="description" content="Calculate crushed gravel, stone aggregate tonnage, cubic yards, cubic meters, compaction factors, and density per ASTM D448 for driveways and bases.">
  <link rel="canonical" href="https://calchub.cloud/gravel-calculator.html">
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
        "name": "Gravel Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates crushed stone aggregate tonnage, cubic yards, loose vs compacted volumes, and bulk densities per ASTM D448.",
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
            "name": "How much does a cubic yard of gravel weigh?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A standard cubic yard of crushed stone or gravel weighs between 2,500 and 2,900 lbs (1.25 to 1.45 US tons / 1.13 to 1.32 metric tonnes), depending on moisture and mineral composition (limestone, granite, or river gravel)."
            }
          },
          {
            "@type": "Question",
            "name": "What is the compaction factor for crushed stone aggregate bases?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "When crushed stone (such as Crusher Run, DGA, or ABC stone) is mechanically compacted with a vibratory roller, its volume decreases by 15% to 20%. Therefore, civil specifications mandate multiplying in-place plan volume by 1.15 to 1.20 when ordering material."
            }
          },
          {
            "@type": "Question",
            "name": "How deep should gravel be installed for residential driveways and patios?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For residential vehicle driveways, civil guidelines specify a 4 to 6-inch (100 to 150 mm) compacted crushed stone base (#57 or Crusher Run) topped by a 2-inch (50 mm) wearing layer. For pedestrian walkways and patios, a 3 to 4-inch base is standard."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between #57 crushed stone and Crusher Run (Dense Graded Aggregate)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "ASTM #57 stone consists of clean, washed angular gravel (1/2 to 1 inch) without fine sand particles, providing excellent drainage. Crusher Run (DGA) contains graded crushed stone blended with stone dust fines, compacting into an impermeable, highly rigid sub-base."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="civil">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">
        <span class="logo-icon">&pi;</span>
        <span class="logo-text">Calc<strong>Hub</strong></span>
      </a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="engineering.html">Engineering</a>
        <a href="mechanical.html">Mechanical</a>
        <a href="civil.html" class="active">Civil &amp; Roof</a>
        <a href="solar-energy.html">Solar</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo; 
      <a href="civil.html">Civil &amp; Construction</a> &rsaquo; 
      <span>Gravel Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calculator-main">
        <div class="calc-header">
          <h1>Gravel Calculator</h1>
          <p>Estimate crushed stone volume, metric tonnes, US tons, and compaction allowances per ASTM D448 aggregate gradations.</p>
        </div>

        <div class="calculator-card">
          <form id="gravelForm" onsubmit="return false;">
            <div class="form-row">
              <div class="form-group">
                <label for="gravelLength">Area Length (meters):</label>
                <input type="number" id="gravelLength" value="25.0" step="0.5" min="0.1" required>
                <span class="hint">Driveway, path or foundation run</span>
              </div>
              <div class="form-group">
                <label for="gravelWidth">Area Width (meters):</label>
                <input type="number" id="gravelWidth" value="4.0" step="0.1" min="0.1" required>
                <span class="hint">Cross-sectional width</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="gravelDepth">Finished Compacted Depth (mm):</label>
                <input type="number" id="gravelDepth" value="150" step="10" min="20" required>
                <span class="hint">Standard base: 100-150 mm (4-6 inches)</span>
              </div>
              <div class="form-group">
                <label for="aggregateType">Gravel / Aggregate Type (ASTM D448):</label>
                <select id="aggregateType">
                  <option value="1600" selected>Crushed Limestone / Granite (1,600 kg/m³ / 2,700 lb/yd³)</option>
                  <option value="1750">Dense Graded Aggregate (DGA / Crusher Run - 1,750 kg/m³)</option>
                  <option value="1500">Clean Washed River Gravel (1,500 kg/m³ / 2,525 lb/yd³)</option>
                  <option value="1400">Pea Gravel / Decorative Round (1,400 kg/m³ / 2,360 lb/yd³)</option>
                  <option value="1300">Volcanic Scoria / Lightweight Aggregate (1,300 kg/m³)</option>
                </select>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="compactionWaste">Compaction &amp; Spillage Factor (%):</label>
                <input type="number" id="compactionWaste" value="15" step="1" min="0" max="30" required>
                <span class="hint">Recommended 15% for compacted road base, 5% for loose decorative</span>
              </div>
              <div class="form-group">
                <label for="truckPayload">Dump Truck Payload (Metric Tonnes):</label>
                <input type="number" id="truckPayload" value="15.0" step="1.0" min="1.0" required>
                <span class="hint">Standard tandem dump truck: 12-16 tonnes</span>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcGravelBtn">Calculate Aggregate Quantities</button>
              <button type="reset" class="btn btn-secondary" id="resetGravelBtn">Reset</button>
            </div>
          </form>

          <div class="results-box" id="gravelResultBox" style="display:none; margin-top:25px;">
            <h3>Aggregates Material Bill of Quantities</h3>
            <div class="result-grid">
              <div class="result-tile highlight">
                <span class="result-label">Total Aggregate Weight</span>
                <span class="result-value" id="resGravelTonnes">0.00</span>
                <span class="result-unit">Metric Tonnes (~0 US tons)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Net In-Place Volume</span>
                <span class="result-value" id="resNetVol">0.00</span>
                <span class="result-unit">m³ (~0 cu yd)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Loose Volume to Purchase</span>
                <span class="result-value" id="resLooseVol">0.00</span>
                <span class="result-unit">m³ (incl. compaction &amp; waste)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Dump Truck Loads</span>
                <span class="result-value" id="resGravelTrucks">0</span>
                <span class="result-unit">Trips (based on payload)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Total Surface Coverage</span>
                <span class="result-value" id="resSurfaceArea">0.0</span>
                <span class="result-unit">m² (~0 sq ft)</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Bulk Density Used</span>
                <span class="result-value" id="resDensity">0</span>
                <span class="result-unit">kg/m³ compacted bulk</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Gravel and Mineral Aggregate Engineering Fundamentals</h2>
          <p>
            Mineral aggregates—encompassing crushed stone, uncrushed alluvial gravel, crushed slag, and manufactured sands—constitute the structural foundation of modern civil infrastructure. Whether deployed as sub-base support under flexible asphalt highways, ballast beneath railway sleepers, drainage filter media behind retaining walls, or wearing surfaces on unpaved access roads, gravel performs vital load-distribution and moisture-management functions.
          </p>
          <p>
            Under <strong>ASTM D448 (Standard Classification for Sizes of Aggregate for Road and Bridge Construction)</strong> and <strong>AASHTO M43</strong>, coarse aggregates are classified by nominal sieve sizes ranging from #1 ($3\frac{1}{2}\text{ to }1\frac{1}{2}\text{ inches}$) down to #89 ($\frac{3}{8}\text{ inch}$ down to #16 mesh). Particle shape (angularity versus sphericity) directly governs mechanical shear interlock and bearing capacity.
          </p>

          <h2>Geometric Formulation for In-Place Volume</h2>
          <p>
            To compute the in-place compacted volume ($V_{net}$) of an aggregate layer over a rectangular footprint of length $L$, width $W$, and uniform compacted depth $T$:
          </p>
          <div class="formula-box">
            $$A_{surface} = L \times W$$
            $$V_{net} = A_{surface} \times \left(\frac{T}{1000}\right) \quad (L, W \text{ in meters, } T \text{ in mm})$$
          </div>
          <p>
            In Imperial units, with length and width in feet and thickness in inches:
          </p>
          <div class="formula-box">
            $$V_{cu\_yd} = \frac{L_{ft} \times W_{ft} \times (T_{in} / 12)}{27}$$
          </div>

          <h2>Aggregate Compaction Factors &amp; Subgrade Surcharge</h2>
          <p>
            When crushed stone is delivered loose in a dump truck, it has a loose bulk density. When spread on subgrade and compacted using heavy vibratory smooth-drum rollers or plate compactors, the mechanical vibrations force fine stone particles into voids between larger angular rocks.
          </p>
          <p>
            This volumetric densification results in a <strong>compaction reduction of $12\%$ to $20\%$</strong>. Furthermore, on soft clay or silty subgrades, an additional $3\%$ to $5\%$ of aggregate is pressed into the natural ground (subgrade intrusion) unless a separation geotextile fabric (non-woven needle-punched Class 1 geotextile) is installed.
          </p>
          <p>
            To avoid severe material shortages on site, the purchased loose volume ($V_{loose}$) and total mass ($M$) must incorporate this compaction factor ($C_f$):
          </p>
          <div class="formula-box">
            $$V_{loose} = V_{net} \times \left(1 + \frac{C_f}{100}\right)$$
            $$M_{tonnes} = V_{loose} \times \left(\frac{\rho_{bulk}}{1000}\right) \quad (\rho_{bulk} \text{ in kg/m}^3)$$
            $$M_{US\_tons} = M_{tonnes} \times 1.10231$$
          </div>

          <h2>Types of Construction Aggregate &amp; Sieve Gradings</h2>
          <p>
            Selecting the appropriate aggregate type is essential for structural performance:
          </p>
          <ul>
            <li><strong>Dense Graded Aggregate (DGA / Crusher Run / ABC Stone):</strong> A graded blend of angular crushed stone (from $1\text{-inch}$ down to micro-fine stone dust). When compacted, the dust particles completely fill interstitial voids, creating a dense, rock-hard impervious layer ideal for vehicular sub-bases.</li>
            <li><strong>#57 Crushed Stone ($1/2\text{ to }1\text{ inch}$):</strong> Clean washed, uniformly sized angular crushed limestone or granite without fines. Possesses high hydraulic conductivity, making it the premier choice for French drains, perimeter foundation footing drains, and driveway top dressing.</li>
            <li><strong>Pea Gravel ($3/8\text{ inch}$):</strong> Smooth, rounded river gravel. Highly decorative and comfortable underfoot, used extensively in garden walkways, exposed aggregate concrete patios, and children's playground safety surfacing.</li>
            <li><strong>Rip-Rap (Class 1 to Class 3, $4\text{ to }12\text{ inches}$):</strong> Heavy, angular blasted rock dumped along riverbanks, stormwater culvert outlets, and steep embankments for severe scour and soil erosion protection.</li>
          </ul>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Aggregate Designation</th>
                <th>Nominal Size</th>
                <th>Bulk Density (kg/m³ / lb/yd³)</th>
                <th>Compaction Loss</th>
                <th>Primary Civil Function</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Dense Graded (DGA / ABC)</td>
                <td>0 to 25 mm (0 to 1")</td>
                <td>1,750 kg/m³ (2,950 lb/yd³)</td>
                <td>15% – 20%</td>
                <td>Driveway sub-base, asphalt base course</td>
              </tr>
              <tr>
                <td>ASTM #57 Crushed Stone</td>
                <td>12.5 to 25 mm (½ to 1")</td>
                <td>1,600 kg/m³ (2,700 lb/yd³)</td>
                <td>10% – 12%</td>
                <td>Sub-surface drainage, concrete aggregate</td>
              </tr>
              <tr>
                <td>ASTM #4 Crushed Rock</td>
                <td>20 to 50 mm (¾ to 2")</td>
                <td>1,550 kg/m³ (2,600 lb/yd³)</td>
                <td>8% – 10%</td>
                <td>Construction entrance tracking pads</td>
              </tr>
              <tr>
                <td>Washed Pea Gravel</td>
                <td>6 to 10 mm (¼ to ⅜")</td>
                <td>1,400 kg/m³ (2,360 lb/yd³)</td>
                <td>5% – 8%</td>
                <td>Decorative paths, pipe bedding envelope</td>
              </tr>
              <tr>
                <td>Crushed Recycled Concrete</td>
                <td>0 to 40 mm (0 to 1½")</td>
                <td>1,500 kg/m³ (2,525 lb/yd³)</td>
                <td>12% – 15%</td>
                <td>Sustainable road sub-base, parking lots</td>
              </tr>
            </tbody>
          </table>

          <h2>California Bearing Ratio (CBR) &amp; Flexible Pavement Base Structural Design</h2>
          <p>
            In highway and parking facility engineering, crushed aggregate gravel functions as the structural unbound base layer directly beneath hot-mix asphalt (HMA) or concrete pavements. The primary engineering performance metric is the <strong>California Bearing Ratio (CBR)</strong> per <strong>ASTM D1883</strong>, which evaluates the mechanical shear resistance of compacted aggregate relative to standard crushed California limestone (defined as $100\%$ CBR).
          </p>
          <p>
            Under the <strong>AASHTO Guide for Design of Pavement Structures</strong>, the overall Pavement Structural Number ($SN$) is computed as:
          </p>
          <div class="formula-box">
            $$SN = a_1 D_1 + a_2 D_2 m_2 + a_3 D_3 m_3$$
          </div>
          <p>
            Where:
          </p>
          <ul>
            <li>$a_2$: Structural layer coefficient of the crushed stone base (typically $a_2 = 0.14$ for high-quality crushed stone with $\text{CBR} \ge 80\%$, corresponding to a resilient modulus $M_R \approx 30,000\text{ psi} / 207\text{ MPa}$).</li>
            <li>$D_2$: Compacted base thickness in inches.</li>
            <li>$m_2$: Drainage coefficient (typically $1.0$ for well-drained stone bases).</li>
          </ul>
          <p>
            <strong>Subgrade Geotextile Separation:</strong> On soft clay or silty subgrades with low in-situ strength ($\text{CBR} < 3\%$), dynamic heavy vehicular wheel pulses pump wet clay fines upward into the aggregate voids while forcing crushed stones downward. Installing a needle-punched non-woven geotextile separation fabric prevents subgrade migration, maintaining aggregate structural interlock and extending pavement fatigue life by up to $300\%$.
          </p>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: Commercial Truck Loading Dock Access Road</h3>
            <p><strong>Design Scenario:</strong> A logistics distribution center requires a heavy-duty crushed stone base course for a semi-trailer loading dock apron. The road measures $L = 60.0\text{ meters}$ in length and $W = 6.0\text{ meters}$ in width. The geotechnical pavement design mandates a compacted base thickness of $T = 200\text{ mm}$ ($0.20\text{ meters}$) of <strong>Dense Graded Aggregate (DGA / Crusher Run)</strong> with a compacted bulk density of $\rho = 1,750\text{ kg/m}^3$. A compaction densification and subgrade intrusion allowance of $18\%$ is specified. Delivery will be executed via tri-axle highway dump trucks with a certified legal payload capacity of $16.0\text{ metric tonnes}$. Calculate net in-place volume, gross loose volume to order, total mass in metric tonnes and US tons, and dump truck deliveries required.</p>
            
            <p><strong>Step 1: Compute Surface Area and Compacted Net Volume ($V_{net}$)</strong></p>
            <div class="formula-box">
              $$A_{surface} = 60.0\text{ m} \times 6.0\text{ m} = 360.0\text{ m}^2 \quad (\approx 3,875\text{ sq ft})$$
              $$V_{net} = 360.0\text{ m}^2 \times 0.20\text{ m} = \mathbf{72.0\text{ m}^3} \quad (\approx 94.17\text{ cu yd})$$
            </div>

            <p><strong>Step 2: Determine Loose Volume to Purchase with 18% Compaction Allowance</strong></p>
            <div class="formula-box">
              $$V_{loose} = V_{net} \times (1 + 0.18) = 72.0\text{ m}^3 \times 1.18 = \mathbf{84.96\text{ m}^3} \quad (\approx 111.12\text{ cu yd})$$
            </div>

            <p><strong>Step 3: Evaluate Total Aggregate Mass</strong></p>
            <div class="formula-box">
              $$M_{tonnes} = 84.96\text{ m}^3 \times 1.75\text{ t/m}^3 = \mathbf{148.68\text{ Metric Tonnes}}$$
              $$M_{US\_tons} = 148.68\text{ t} \times 1.10231 = \mathbf{163.89\text{ US Short Tons}}$$
            </div>

            <p><strong>Step 4: Determine Number of Dump Truck Deliveries</strong></p>
            <div class="formula-box">
              $$N_{trucks} = \left\lceil \frac{148.68\text{ tonnes}}{16.0\text{ tonnes/truck}} \right\rceil = \lceil 9.29 \rceil = \mathbf{10\text{ Dump Truck Loads}}$$
            </div>
            <p>
              <strong>Procurement Summary:</strong> Order <strong>150 metric tonnes</strong> (or approximately <strong>112 cubic yards</strong>) of Dense Graded Aggregate across <strong>10 dump truck deliveries</strong> to guarantee a uniform, compliant $200\text{ mm}$ finished compacted road base.
            </p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Civil &amp; Road Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="asphalt-calculator.html">Asphalt Paving &amp; Tonnage</a></li>
            <li><a href="concrete-calculator.html">Concrete Volume Calculator</a></li>
            <li><a href="excavation-calculator.html">Excavation Bank &amp; Haul</a></li>
            <li><a href="excavation-volume-calculator.html">Excavation Volume Calculator</a></li>
            <li><a href="retaining-wall-calculator.html">Retaining Wall Stability</a></li>
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
          <li><a href="civil.html">Civil &amp; Construction</a></li>
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
      const calcBtn = document.getElementById('calcGravelBtn');
      const resetBtn = document.getElementById('resetGravelBtn');
      const resultBox = document.getElementById('gravelResultBox');

      function calculateGravel() {
        const L = parseFloat(document.getElementById('gravelLength').value);
        const W = parseFloat(document.getElementById('gravelWidth').value);
        const depthMm = parseFloat(document.getElementById('gravelDepth').value);
        const density = parseFloat(document.getElementById('aggregateType').value);
        const compWastePct = parseFloat(document.getElementById('compactionWaste').value) || 0;
        const truckPay = parseFloat(document.getElementById('truckPayload').value);

        if (isNaN(L) || L <= 0 || isNaN(W) || W <= 0 || isNaN(depthMm) || depthMm <= 0 || isNaN(truckPay) || truckPay <= 0) {
          alert('Please enter valid positive dimensions, thickness, and truck payload.');
          return;
        }

        const surfaceAreaM2 = L * W;
        const depthM = depthMm / 1000.0;
        const netVolM3 = surfaceAreaM2 * depthM;
        const looseVolM3 = netVolM3 * (1.0 + compWastePct / 100.0);

        const totalKg = looseVolM3 * density;
        const totalTonnes = totalKg / 1000.0;
        const totalUsTons = totalTonnes * 1.10231;

        const netCuYd = netVolM3 * 1.30795;
        const looseCuYd = looseVolM3 * 1.30795;
        const surfaceSqFt = surfaceAreaM2 * 10.7639;

        const truckLoads = Math.ceil(totalTonnes / truckPay);

        document.getElementById('resGravelTonnes').textContent = totalTonnes.toFixed(2) + ` (~${totalUsTons.toFixed(1)} tons)`;
        document.getElementById('resNetVol').textContent = netVolM3.toFixed(2) + ` (~${netCuYd.toFixed(1)} yd³)`;
        document.getElementById('resLooseVol').textContent = looseVolM3.toFixed(2) + ` (~${looseCuYd.toFixed(1)} yd³)`;
        document.getElementById('resGravelTrucks').textContent = truckLoads.toLocaleString();
        document.getElementById('resSurfaceArea').textContent = surfaceAreaM2.toFixed(1) + ` (~${Math.round(surfaceSqFt).toLocaleString()} ft²)`;
        document.getElementById('resDensity').textContent = density.toLocaleString();

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculateGravel);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
      });
      calculateGravel();
    });
  </script>
</body>
</html>
"""

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    path_footing = os.path.join(base_dir, 'footing-size-calculator.html')
    with open(path_footing, 'w', encoding='utf-8') as f:
        f.write(TOOL_1_HTML.strip() + '\n')
    print("[PASS] footing-size-calculator.html generated successfully!")

    path_gravel = os.path.join(base_dir, 'gravel-calculator.html')
    with open(path_gravel, 'w', encoding='utf-8') as f:
        f.write(TOOL_2_HTML.strip() + '\n')
    print("[PASS] gravel-calculator.html generated successfully!")

if __name__ == '__main__':
    main()
