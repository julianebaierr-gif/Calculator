# -*- coding: utf-8 -*-
"""
Script to generate Batch 12 Part 1 tools:
1. beam-calculator.html
2. block-calculator.html
"""
import os

TOOL_1_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Beam Calculator | Shear Force, Bending Moment &amp; Deflection</title>
  <meta name="description" content="Calculate beam shear force (SFD), maximum bending moment (BMD), flexural stress, and deflection for simply supported and cantilever beams per AISC 360 &amp; Eurocode 3.">
  <link rel="canonical" href="https://calchub.cloud/beam-calculator.html">
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
        "name": "Beam Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Structural beam mechanics calculator evaluating maximum bending moment, shear force reactions, flexural stress, and elastic deflection per AISC 360.",
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
            "name": "What is the formula for maximum bending moment in a simply supported beam with UDL?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For a simply supported beam of span length L carrying a uniform distributed load (UDL) of intensity w: M_max = (w * L^2) / 8. The peak bending moment occurs exactly at the mid-span (x = L / 2) where shear force passes through zero."
            }
          },
          {
            "@type": "Question",
            "name": "How is elastic beam deflection calculated per structural design codes?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For a simply supported beam with UDL: delta_max = (5 * w * L^4) / (384 * E * I). For a central point load P: delta_max = (P * L^3) / (48 * E * I). For a cantilever beam with end load P: delta_max = (P * L^3) / (3 * E * I), where E is Young's modulus and I is second moment of area."
            }
          },
          {
            "@type": "Question",
            "name": "What is the relationship between bending moment and flexural stress?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "According to the Euler-Bernoulli flexure formula: sigma = (M * y) / I = M / S, where M is bending moment, y is extreme fiber distance from the neutral axis, I is moment of inertia, and S = I / y is the elastic section modulus."
            }
          },
          {
            "@type": "Question",
            "name": "What are standard allowable deflection limits for commercial building beams?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Per AISC 360 and IBC standards, serviceability deflection limits are typically: L/360 for floors supporting brittle plaster ceilings under live load; L/240 for roof beams with flexible ceilings; and L/180 for total load on industrial roofs and purlins."
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
      <span>Beam Calculator</span>
    </nav>

    <header class="calc-header">
      <div class="calc-badge">Structural Analysis &amp; Mechanics</div>
      <h1 class="calc-title">Beam Calculator</h1>
      <p class="calc-tagline">Calculate shear force reactions, maximum bending moment ($M_{max}$), flexural bending stress, and mid-span elastic deflection per AISC 360 and Eurocode 3.</p>
    </header>

    <div class="calc-grid">
      <div class="calc-main">
        <div class="tool-card">
          <form id="beamForm">
            <div class="form-row">
              <div class="form-group">
                <label for="beamSupport">Beam Support Configuration</label>
                <select id="beamSupport" class="form-control">
                  <option value="ss_udl" selected>Simply Supported &ndash; Uniform Distributed Load (UDL)</option>
                  <option value="ss_point">Simply Supported &ndash; Central Point Load ($P$ at $L/2$)</option>
                  <option value="cant_udl">Cantilever Beam &ndash; Uniform Distributed Load (UDL)</option>
                  <option value="cant_point">Cantilever Beam &ndash; End Point Load ($P$ at free tip)</option>
                  <option value="fixed_udl">Fixed-Fixed Beam &ndash; Uniform Distributed Load (UDL)</option>
                </select>
              </div>
              <div class="form-group">
                <label for="spanLength">Clear Span Length ($L$ in meters)</label>
                <input type="number" id="spanLength" class="form-control" value="6.0" min="0.5" step="any" required>
                <span class="hint">Effective distance between centerline of supports</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group" id="grpLoadUDL">
                <label for="loadUDL">Uniform Load Intensity ($w$ in kN/m)</label>
                <input type="number" id="loadUDL" class="form-control" value="18.0" min="0.01" step="any" required>
                <span class="hint">Includes self-weight + dead load + live load</span>
              </div>
              <div class="form-group" id="grpLoadPoint" style="display: none;">
                <label for="loadPoint">Concentrated Point Load ($P$ in kN)</label>
                <input type="number" id="loadPoint" class="form-control" value="50.0" min="0.01" step="any">
                <span class="hint">Point load magnitude applied to beam</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="elasticModulus">Young's Modulus of Elasticity ($E$ in GPa)</label>
                <select id="elasticModulus" class="form-control">
                  <option value="200" selected>Structural Steel (E = 200 GPa / 29,000 ksi)</option>
                  <option value="30">Reinforced Concrete C30/37 (E ≈ 30 GPa)</option>
                  <option value="69">Structural Aluminum 6061-T6 (E = 69 GPa)</option>
                  <option value="12">Structural Glulam Timber (E ≈ 12 GPa)</option>
                </select>
              </div>
              <div class="form-group">
                <label for="momentInertia">Moment of Inertia ($I_x$ in $10^6\text{ mm}^4$ / $\text{cm}^4 \times 100$)</label>
                <input type="number" id="momentInertia" class="form-control" value="86.9" min="0.1" step="any" required>
                <span class="hint">E.g., IPE 300 = 83.6 × 10⁶ mm⁴; W12×26 = 84.9 × 10⁶ mm⁴</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="sectionModulus">Elastic Section Modulus ($S_x$ in $10^3\text{ mm}^3$ / $\text{cm}^3$)</label>
                <input type="number" id="sectionModulus" class="form-control" value="557" min="1" step="any" required>
                <span class="hint">E.g., IPE 300 = 557 × 10³ mm³ ($S_x = I_x / c$)</span>
              </div>
              <div class="form-group">
                <label for="deflectionLimit">Deflection Serviceability Limit Ratio</label>
                <select id="deflectionLimit" class="form-control">
                  <option value="360" selected>L / 360 (Floors with Plaster Ceiling)</option>
                  <option value="240">L / 240 (Roof Beams &amp; Non-Brittle Finish)</option>
                  <option value="180">L / 180 (Industrial Roof Purlins &amp; Joists)</option>
                </select>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcBeamBtn">Calculate Beam Analysis</button>
              <button type="reset" class="btn btn-secondary" id="resetBeamBtn">Reset</button>
            </div>
          </form>

          <div id="beamResultBox" class="results-container" style="display: none; margin-top: 1.5rem;">
            <h3>Calculated Structural Beam Performance</h3>
            <div class="results-grid">
              <div class="result-tile highlight">
                <span class="result-label">Maximum Bending Moment ($M_{max}$)</span>
                <span class="result-value" id="resMaxMoment">-- kN·m</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Maximum Shear Force ($V_{max}$)</span>
                <span class="result-value" id="resMaxShear">-- kN</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Peak Flexural Stress ($\sigma_{max}$)</span>
                <span class="result-value" id="resFlexStress">-- MPa</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Maximum Elastic Deflection ($\delta_{max}$)</span>
                <span class="result-value" id="resDeflection">-- mm</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Allowable Deflection Limit ($\delta_{allow}$)</span>
                <span class="result-value" id="resAllowDefl">-- mm</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Serviceability Deflection Check</span>
                <span class="result-value" id="resDeflStatus">--</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Structural Engineering Principles of Beam Bending</h2>
          <p>
            In civil and structural engineering, a <strong>beam</strong> is a primary load-bearing structural member designed to span horizontally across openings and support transverse vertical gravity loads transferred from slabs, roofs, walls, and vehicle traffic. Under applied vertical loading, a beam develops internal <strong>shear forces ($V$)</strong> and <strong>bending moments ($M$)</strong>, causing the member to bend elastically along its neutral axis.
          </p>
          <p>
            Governed by <strong>AISC 360</strong> (<em>Specification for Structural Steel Buildings</em>) and <strong>Eurocode 3 (EN 1993-1-1)</strong>, structural beam design requires satisfying two independent criteria:
          </p>
          <ol>
            <li><strong>Ultimate Limit State (ULS):</strong> The cross-section must safely resist peak internal bending moments ($M \le M_c = F_y \cdot Z$) and shear forces without material yielding, lateral torsional buckling, or web crippling.</li>
            <li><strong>Serviceability Limit State (SLS):</strong> Maximum elastic deflections ($\delta$) must remain within acceptable deflection limits ($L/360$, $L/240$) to prevent cracking of supported masonry or plaster ceilings and eliminate noticeable floor bounce.</li>
          </ol>

          <h2>Governing Equations by Beam Support and Load Cases</h2>
          <p>
            Classical Euler-Bernoulli beam theory establishes the exact closed-form solutions for standard boundary conditions:
          </p>

          <h3>1. Simply Supported Beam with Uniform Load (UDL $w$)</h3>
          <div class="formula-box">
            $$V_{max} = R_A = R_B = \frac{w \cdot L}{2}$$
            $$M_{max} = \frac{w \cdot L^2}{8} \quad (\text{at mid-span } x = L/2)$$
            $$\delta_{max} = \frac{5 \cdot w \cdot L^4}{384 \cdot E \cdot I_x}$$
          </div>

          <h3>2. Simply Supported Beam with Central Point Load ($P$)</h3>
          <div class="formula-box">
            $$V_{max} = R_A = R_B = \frac{P}{2}$$
            $$M_{max} = \frac{P \cdot L}{4} \quad (\text{at mid-span } x = L/2)$$
            $$\delta_{max} = \frac{P \cdot L^3}{48 \cdot E \cdot I_x}$$
          </div>

          <h3>3. Cantilever Beam with Uniform Load (UDL $w$)</h3>
          <div class="formula-box">
            $$V_{max} = R_{fixed} = w \cdot L$$
            $$M_{max} = -\frac{w \cdot L^2}{2} \quad (\text{at fixed support } x = 0)$$
            $$\delta_{max} = \frac{w \cdot L^4}{8 \cdot E \cdot I_x} \quad (\text{at free tip } x = L)$$
          </div>

          <h3>4. Cantilever Beam with End Point Load ($P$)</h3>
          <div class="formula-box">
            $$V_{max} = P, \quad M_{max} = -P \cdot L \quad (\text{at fixed support})$$
            $$\delta_{max} = \frac{P \cdot L^3}{3 \cdot E \cdot I_x} \quad (\text{at free tip})$$
          </div>

          <h3>5. Fixed-Fixed Beam with Uniform Load (UDL $w$)</h3>
          <div class="formula-box">
            $$M_{support} = -\frac{w \cdot L^2}{12}, \quad M_{mid} = +\frac{w \cdot L^2}{24}$$
            $$\delta_{max} = \frac{w \cdot L^4}{384 \cdot E \cdot I_x}$$
          </div>

          <h2>Flexural Bending Stress &amp; Section Modulus ($S_x$)</h2>
          <p>
            When a beam bends, longitudinal fibers above the neutral axis undergo compression, while fibers below the neutral axis experience tension. By the Navier-Bernoulli flexure formula:
          </p>
          <div class="formula-box">
            $$\sigma = \frac{M \cdot y}{I_x} \implies \sigma_{max} = \frac{M_{max} \cdot c}{I_x} = \frac{M_{max}}{S_x} \quad [\text{MPa}]$$
          </div>
          <p>
            Where $c$ is the distance from the neutral axis to the outermost fiber, $I_x$ is the second moment of area (moment of inertia), and $S_x = I_x / c$ is the <strong>elastic section modulus</strong>. For standard structural steel sections (ASTM A992 Grade 50 with yield strength $F_y = 345\text{ MPa}$), allowable bending stress per AISC ASD is typically $\sigma_{allow} \le 0.66 F_y \approx 228\text{ MPa}$.
          </p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Standard Beam Section</th>
                <th>Depth $d$ (mm)</th>
                <th>Weight (kg/m)</th>
                <th>Moment of Inertia $I_x$ ($10^6\text{ mm}^4$)</th>
                <th>Section Modulus $S_x$ ($10^3\text{ mm}^3$)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>IPE 200 (Euro Standard)</td>
                <td>200 mm</td>
                <td>22.4 kg/m</td>
                <td>19.43 × 10⁶ mm⁴</td>
                <td>194.3 × 10³ mm³</td>
              </tr>
              <tr>
                <td>IPE 270 (Euro Standard)</td>
                <td>270 mm</td>
                <td>36.1 kg/m</td>
                <td>57.90 × 10⁶ mm⁴</td>
                <td>428.9 × 10³ mm³</td>
              </tr>
              <tr>
                <td>IPE 300 (Euro Standard)</td>
                <td>300 mm</td>
                <td>42.2 kg/m</td>
                <td>83.56 × 10⁶ mm⁴</td>
                <td>557.1 × 10³ mm³</td>
              </tr>
              <tr>
                <td>W10 × 30 (AISC Wide Flange)</td>
                <td>267 mm</td>
                <td>44.8 kg/m</td>
                <td>70.80 × 10⁶ mm⁴</td>
                <td>531.0 × 10³ mm³</td>
              </tr>
              <tr>
                <td>W12 × 26 (AISC Wide Flange)</td>
                <td>310 mm</td>
                <td>38.7 kg/m</td>
                <td>84.90 × 10⁶ mm⁴</td>
                <td>547.0 × 10³ mm³</td>
              </tr>
              <tr>
                <td>W14 × 43 (AISC Wide Flange)</td>
                <td>347 mm</td>
                <td>64.0 kg/m</td>
                <td>178.1 × 10⁶ mm⁴</td>
                <td>1,027 × 10³ mm³</td>
              </tr>
            </tbody>
          </table>

          <h2>Lateral-Torsional Buckling (LTB AISC 360 Chapter F) &amp; Web Shear Stability</h2>
          <p>
            When an I-shaped beam or structural channel is bent about its major axis, the compression flange behaves like a column subjected to compressive stress. If the compression flange is insufficiently braced against lateral displacement and twist, the member can fail catastrophically by <strong>lateral-torsional buckling (LTB)</strong> prior to reaching its full plastic moment capacity ($M_p = Z_x F_y$).
          </p>
          <p>
            Under <strong>AISC 360 Specification for Structural Steel Buildings</strong>, three unbraced length ($L_b$) regimes define the nominal flexural strength ($M_n$):
          </p>
          <div class="formula-box">
            $$L_p = 1.76 \, r_y \sqrt{\frac{E}{F_y}} \quad \text{(Limiting unbraced length for plastic behavior)}$$
            $$L_r = 1.95 \, r_{ts} \frac{E}{0.7 F_y} \sqrt{\frac{J c}{S_x h_0} + \sqrt{\left(\frac{J c}{S_x h_0}\right)^2 + 6.76 \left(\frac{0.7 F_y}{E}\right)^2}}$$
          </div>
          <p>
            1. <strong>Plastic Range ($L_b \le L_p$):</strong> The beam develops its full plastic capacity $M_n = M_p = Z_x F_y$, and LTB is completely prevented.<br>
            2. <strong>Inelastic LTB Range ($L_p < L_b \le L_r$):</strong> Bending strength degrades linearly due to partial yielding and initial geometric imperfections:
          </p>
          <div class="formula-box">
            $$M_n = C_b \left[ M_p - (M_p - 0.7 F_y S_x)\left( \frac{L_b - L_p}{L_r - L_p} \right) \right] \le M_p$$
          </div>
          <p>
            3. <strong>Elastic LTB Range ($L_b > L_r$):</strong> Buckling occurs purely elastically governed by the critical moment $M_{cr} = C_b \frac{\pi^2 E I_y}{L_b^2} \sqrt{\frac{I_w}{I_y} + \frac{L_b^2 G J}{\pi^2 E I_y}}$. Providing lateral bracings, diaphragm slab ties, or cross-frames at intervals under $L_p$ ensures that steel sections attain maximum structural economy.
          </p>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: Commercial Office Floor Primary Girder</h3>
            <p><strong>Design Scenario:</strong> An office building floor girder spans $L = 6.0\text{ meters}$ between reinforced concrete columns. The girder supports precast hollow-core concrete planks delivering a factored uniform distributed load of $w = 18.0\text{ kN/m}$ ($18\text{ N/mm}$). The selected structural shape is an <strong>IPE 300</strong> European standard I-beam ($E = 200\text{ GPa}$, $I_x = 83.56 \times 10^6\text{ mm}^4$, $S_x = 557.1 \times 10^3\text{ mm}^3$). The architectural specification requires the floor live-load deflection to satisfy the strict $L / 360$ serviceability limit. Calculate peak bending moment, maximum shear force, flexural stress, and verify deflection compliance.</p>
            
            <p><strong>Step 1: Calculate Maximum Shear Force and Reactions</strong></p>
            <div class="formula-box">
              $$V_{max} = R_A = R_B = \frac{w \cdot L}{2} = \frac{18.0\text{ kN/m} \times 6.0\text{ m}}{2} = 54.0\text{ kN}$$
            </div>

            <p><strong>Step 2: Calculate Maximum Mid-Span Bending Moment ($M_{max}$)</strong></p>
            <div class="formula-box">
              $$M_{max} = \frac{w \cdot L^2}{8} = \frac{18.0\text{ kN/m} \times (6.0\text{ m})^2}{8} = \frac{18.0 \times 36.0}{8} = 81.0\text{ kN}\cdot\text{m} = 81,000,000\text{ N}\cdot\text{mm}$$
            </div>

            <p><strong>Step 3: Evaluate Peak Flexural Bending Stress ($\sigma_{max}$)</strong></p>
            <div class="formula-box">
              $$\sigma_{max} = \frac{M_{max}}{S_x} = \frac{81,000,000\text{ N}\cdot\text{mm}}{557,100\text{ mm}^3} \approx 145.39\text{ MPa} \quad (\text{N/mm}^2)$$
            </div>
            <p>
              Comparing against standard structural steel yield strength ($S275$ with $F_y = 275\text{ MPa}$): The stress ratio is $\frac{145.39}{275} \approx 52.9\%$, providing a generous safety margin of $1.89$.
            </p>

            <p><strong>Step 4: Calculate Mid-Span Elastic Deflection ($\delta_{max}$)</strong></p>
            <div class="formula-box">
              $$\delta_{max} = \frac{5 \cdot w \cdot L^4}{384 \cdot E \cdot I_x} = \frac{5 \times 18\text{ N/mm} \times (6000\text{ mm})^4}{384 \times 200,000\text{ N/mm}^2 \times 83,560,000\text{ mm}^4}$$
              $$\delta_{max} = \frac{5 \times 18 \times 1.296 \times 10^{15}}{384 \times 2 \times 10^5 \times 8.356 \times 10^7} = \frac{1.1664 \times 10^{17}}{6.4174 \times 10^{15}} \approx 18.17\text{ mm}$$
            </div>

            <p><strong>Step 5: Check Serviceability Deflection Limit ($L / 360$)</strong></p>
            <div class="formula-box">
              $$\delta_{allow} = \frac{L}{360} = \frac{6,000\text{ mm}}{360} \approx 16.67\text{ mm}$$
            </div>
            <p>
              <strong>Engineering Conclusion:</strong> While flexural stress is completely safe ($145.4\text{ MPa} \ll 275\text{ MPa}$), actual total deflection ($\delta = 18.17\text{ mm}$) exceeds the $L/360$ threshold of $16.67\text{ mm}$ by $1.5\text{ mm}$. The structural engineer must either introduce a nominal $10\text{ mm}$ fabrication camber or upsize to an <strong>IPE 330</strong> ($I_x = 117.7 \times 10^6\text{ mm}^4 \implies \delta = 12.9\text{ mm} < 16.67\text{ mm}$) to satisfy serviceability requirements.
            </p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Civil &amp; Structural Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="beam-deflection-calculator.html">Beam Deflection Calculator</a></li>
            <li><a href="retaining-wall-calculator.html">Retaining Wall Sizing</a></li>
            <li><a href="concrete-calculator.html">Concrete Volume Calculator</a></li>
            <li><a href="rebar-calculator.html">Rebar Weight &amp; Grid Sizing</a></li>
            <li><a href="brick-calculator.html">Brick Masonry Calculator</a></li>
            <li><a href="block-calculator.html">Block Masonry Calculator</a></li>
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
      const calcBtn = document.getElementById('calcBeamBtn');
      const resetBtn = document.getElementById('resetBeamBtn');
      const resultBox = document.getElementById('beamResultBox');
      const beamSupport = document.getElementById('beamSupport');
      const grpLoadUDL = document.getElementById('grpLoadUDL');
      const grpLoadPoint = document.getElementById('grpLoadPoint');

      beamSupport.addEventListener('change', function() {
        const val = this.value;
        if (val.includes('point')) {
          grpLoadUDL.style.display = 'none';
          grpLoadPoint.style.display = 'block';
        } else {
          grpLoadUDL.style.display = 'block';
          grpLoadPoint.style.display = 'none';
        }
      });

      function calculateBeam() {
        const mode = beamSupport.value;
        const L_m = parseFloat(document.getElementById('spanLength').value);
        const E_GPa = parseFloat(document.getElementById('elasticModulus').value);
        const Ix_input = parseFloat(document.getElementById('momentInertia').value);
        const Sx_input = parseFloat(document.getElementById('sectionModulus').value);
        const deflRatio = parseFloat(document.getElementById('deflectionLimit').value);

        if (isNaN(L_m) || L_m <= 0 || isNaN(E_GPa) || E_GPa <= 0 || isNaN(Ix_input) || Ix_input <= 0 || isNaN(Sx_input) || Sx_input <= 0) {
          alert('Please enter valid positive dimensions, span, and cross-section properties.');
          return;
        }

        const L_mm = L_m * 1000.0;
        const E_N_mm2 = E_GPa * 1000.0;
        const Ix_mm4 = Ix_input * 1e6;
        const Sx_mm3 = Sx_input * 1e3;

        let M_max_kNm = 0;
        let V_max_kN = 0;
        let delta_max_mm = 0;

        if (mode === 'ss_udl') {
          const w_kNm = parseFloat(document.getElementById('loadUDL').value) || 0;
          const w_N_mm = w_kNm;
          V_max_kN = (w_kNm * L_m) / 2.0;
          M_max_kNm = (w_kNm * Math.pow(L_m, 2)) / 8.0;
          delta_max_mm = (5.0 * w_N_mm * Math.pow(L_mm, 4)) / (384.0 * E_N_mm2 * Ix_mm4);
        } else if (mode === 'ss_point') {
          const P_kN = parseFloat(document.getElementById('loadPoint').value) || 0;
          const P_N = P_kN * 1000.0;
          V_max_kN = P_kN / 2.0;
          M_max_kNm = (P_kN * L_m) / 4.0;
          delta_max_mm = (P_N * Math.pow(L_mm, 3)) / (48.0 * E_N_mm2 * Ix_mm4);
        } else if (mode === 'cant_udl') {
          const w_kNm = parseFloat(document.getElementById('loadUDL').value) || 0;
          const w_N_mm = w_kNm;
          V_max_kN = w_kNm * L_m;
          M_max_kNm = (w_kNm * Math.pow(L_m, 2)) / 2.0;
          delta_max_mm = (w_N_mm * Math.pow(L_mm, 4)) / (8.0 * E_N_mm2 * Ix_mm4);
        } else if (mode === 'cant_point') {
          const P_kN = parseFloat(document.getElementById('loadPoint').value) || 0;
          const P_N = P_kN * 1000.0;
          V_max_kN = P_kN;
          M_max_kNm = P_kN * L_m;
          delta_max_mm = (P_N * Math.pow(L_mm, 3)) / (3.0 * E_N_mm2 * Ix_mm4);
        } else if (mode === 'fixed_udl') {
          const w_kNm = parseFloat(document.getElementById('loadUDL').value) || 0;
          const w_N_mm = w_kNm;
          V_max_kN = (w_kNm * L_m) / 2.0;
          M_max_kNm = (w_kNm * Math.pow(L_m, 2)) / 12.0; // Support peak moment
          delta_max_mm = (w_N_mm * Math.pow(L_mm, 4)) / (384.0 * E_N_mm2 * Ix_mm4);
        }

        // Flexural stress sigma = M / S
        const M_max_Nmm = M_max_kNm * 1e6;
        const sigma_MPa = M_max_Nmm / Sx_mm3;

        // Allowable deflection
        const delta_allow_mm = L_mm / deflRatio;
        const isDeflCompliant = delta_max_mm <= delta_allow_mm;

        // Render outputs
        document.getElementById('resMaxMoment').textContent = M_max_kNm.toFixed(2) + ' kN·m';
        document.getElementById('resMaxShear').textContent = V_max_kN.toFixed(2) + ' kN';
        document.getElementById('resFlexStress').textContent = sigma_MPa.toFixed(1) + ' MPa (N/mm²)';
        document.getElementById('resDeflection').textContent = delta_max_mm.toFixed(2) + ' mm';
        document.getElementById('resAllowDefl').textContent = delta_allow_mm.toFixed(2) + ' mm (L/' + deflRatio + ')';
        document.getElementById('resDeflStatus').textContent = isDeflCompliant ? 'PASS: Deflection Within Permissible Service Limit' : 'FAIL: Exceeds L/' + deflRatio + ' (Upsize Section or Camber)';

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculateBeam);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
      });

      calculateBeam();
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
  <title>Block Calculator | Concrete Masonry Unit (CMU) &amp; Mortar Sizing</title>
  <meta name="description" content="Calculate concrete block (CMU) quantity, mortar bags, sand tonnage, core fill grout volume, and rebar reinforcement per ASTM C90 &amp; NCMA guidelines.">
  <link rel="canonical" href="https://calchub.cloud/block-calculator.html">
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
        "name": "Block Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Concrete masonry unit (CMU) estimator calculating block counts, mortar bags, core fill grout volume, and wastage per NCMA TEK standards.",
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
            "name": "How many standard concrete blocks (CMU) are in one square meter or square foot of wall?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A standard 8x8x16 inch CMU block measures nominal 200mm high by 400mm long with a 10mm (3/8-inch) mortar joint. Each block covers 0.08 square meters (0.8889 square feet). Therefore, exactly 12.5 blocks are required per square meter (approx. 1.125 blocks per square foot) of net wall surface area."
            }
          },
          {
            "@type": "Question",
            "name": "How much mortar is required per 100 concrete masonry blocks?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Per NCMA masonry guidelines, laying 100 standard 8-inch CMU blocks with standard 3/8-inch face-shell mortar bedding consumes approximately 3 bags (80-lb / 36-kg each) of pre-mixed Type S or Type N masonry cement, along with approximately 0.25 cubic yards (0.19 m^3) of masonry sand."
            }
          },
          {
            "@type": "Question",
            "name": "How is core-fill concrete grout volume calculated for reinforced masonry?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Standard two-core hollow 8-inch CMU blocks possess approximately 48% hollow void volume. Fully grouting every core requires approximately 0.0095 cubic meters (0.33 cubic feet) of concrete grout per block, or roughly 0.95 m^3 (1.25 cu yd) per 100 blocks."
            }
          },
          {
            "@type": "Question",
            "name": "What wastage factor should be applied to masonry block ordering?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A standard 5% to 10% wastage allowance must be added to raw theoretical block counts. Simple straight foundation walls typically require 5% waste; walls featuring numerous corner returns, window lintels, electrical box cutouts, and diagonal gables require 10% to 12% to cover cutting scrap."
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
      <span>Block Calculator</span>
    </nav>

    <header class="calc-header">
      <div class="calc-badge">Masonry &amp; Wall Sizing</div>
      <h1 class="calc-title">Block Calculator</h1>
      <p class="calc-tagline">Calculate concrete masonry unit (CMU) block counts, mortar bags, sand tonnage, and core-fill concrete grout per ASTM C90 and NCMA standards.</p>
    </header>

    <div class="calc-grid">
      <div class="calc-main">
        <div class="tool-card">
          <form id="blockForm">
            <div class="form-row">
              <div class="form-group">
                <label for="blockSizePreset">Block Size Standard (Thickness &times; Height &times; Length)</label>
                <select id="blockSizePreset" class="form-control">
                  <option value="8_8_16" selected>Standard 8&times;8&times;16 in (200&times;200&times;400 mm) &ndash; Most Common</option>
                  <option value="6_8_16">Partition 6&times;8&times;16 in (150&times;200&times;400 mm)</option>
                  <option value="4_8_16">Veneer 4&times;8&times;16 in (100&times;200&times;400 mm)</option>
                  <option value="12_8_16">Foundation 12&times;8&times;16 in (300&times;200&times;400 mm)</option>
                  <option value="metric_cmu">European Metric Block (215&times;140&times;440 mm)</option>
                </select>
              </div>
              <div class="form-group">
                <label for="unitSystem">Dimensional Units</label>
                <select id="unitSystem" class="form-control">
                  <option value="metric" selected>Metric (Meters, m²)</option>
                  <option value="imperial">Imperial (Feet, sq ft)</option>
                </select>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="wallLength">Wall Total Length</label>
                <input type="number" id="wallLength" class="form-control" value="15.0" min="0.1" step="any" required>
                <span class="hint" id="wallLenHint">Length of continuous block wall in meters</span>
              </div>
              <div class="form-group">
                <label for="wallHeight">Wall Total Height</label>
                <input type="number" id="wallHeight" class="form-control" value="2.4" min="0.1" step="any" required>
                <span class="hint" id="wallHgtHint">Height from footing top to bond beam in meters</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="openingsArea">Deductions for Doors &amp; Windows Area</label>
                <input type="number" id="openingsArea" class="form-control" value="4.5" min="0" step="any">
                <span class="hint" id="openingsHint">Total area of window/door openings in m²</span>
              </div>
              <div class="form-group">
                <label for="wasteFactor">Wastage &amp; Cutting Scrap Allowance (%)</label>
                <select id="wasteFactor" class="form-control">
                  <option value="5">5% - Straight simple continuous wall</option>
                  <option value="8" selected>8% - Standard building layout with corners</option>
                  <option value="10">10% - Complex layout with numerous openings</option>
                  <option value="12">12% - Heavy cutting (gables, diagonal steps)</option>
                </select>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="coreGrouting">Core Fill Grouting Density</label>
                <select id="coreGrouting" class="form-control">
                  <option value="none">No Core Grout (Hollow Unreinforced Masonry)</option>
                  <option value="rebar_48">Grout Rebar Cores @ 48-inch (1.2m) Spacing</option>
                  <option value="rebar_24">Grout Rebar Cores @ 24-inch (0.6m) Spacing</option>
                  <option value="full" selected>Solid Grout (100% Full Core Fill &ndash; High Shear)</option>
                </select>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcBlockBtn">Calculate Blocks &amp; Materials</button>
              <button type="reset" class="btn btn-secondary" id="resetBlockBtn">Reset</button>
            </div>
          </form>

          <div id="blockResultBox" class="results-container" style="display: none; margin-top: 1.5rem;">
            <h3>Calculated Block Masonry Bill of Materials</h3>
            <div class="results-grid">
              <div class="result-tile highlight">
                <span class="result-label">Total Blocks Required (With Waste)</span>
                <span class="result-value" id="resTotalBlocks">-- Blocks</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Net Theoretical Block Count</span>
                <span class="result-value" id="resNetBlocks">-- Blocks</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Net Masonry Wall Surface Area</span>
                <span class="result-value" id="resNetArea">-- m²</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Mortar Cement Bags (Type S/N, 36kg/80lb)</span>
                <span class="result-value" id="resMortarBags">-- Bags</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Masonry Sand Required</span>
                <span class="result-value" id="resSandTons">-- Tonnes / Tons</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Core Fill Concrete Grout Volume</span>
                <span class="result-value" id="resGroutVol">-- m³ / cu yd</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Concrete Masonry Unit (CMU) Engineering Standards</h2>
          <p>
            <strong>Concrete masonry units (CMU)</strong>, colloquially known as cinder blocks or concrete blocks, are modular precast building elements manufactured from zero-slump Portland cement, graded aggregates, water, and mineral admixtures. Standardized under <strong>ASTM C90</strong> (<em>Standard Specification for Loadbearing Concrete Masonry Units</em>) and the <strong>National Concrete Masonry Association (NCMA)</strong>, concrete blocks constitute the structural backbone of foundation stem walls, seismic shear walls, commercial perimeter envelopes, and fire-resistant stairwells.
          </p>
          <p>
            Standard CMUs are designed on a modular coordinate grid system where nominal dimensions specify the space occupied by the block <em>plus</em> the standard $3/8\text{-inch}$ ($10\text{ mm}$) mortar joint. Consequently:
          </p>
          <ul>
            <li><strong>Nominal Dimensions:</strong> $8\text{ in} \times 8\text{ in} \times 16\text{ in}$ ($200\text{ mm} \times 200\text{ mm} \times 400\text{ mm}$)</li>
            <li><strong>Actual Manufactured Dimensions:</strong> $7\frac{5}{8}\text{ in} \times 7\frac{5}{8}\text{ in} \times 15\frac{5}{8}\text{ in}$ ($194\text{ mm} \times 194\text{ mm} \times 394\text{ mm}$)</li>
          </ul>

          <h2>Block Sizing Formulation and Wall Face Area Calculation</h2>
          <p>
            Because each standard $8\times 8\times 16$ block occupies a nominal modular face elevation of $0.20\text{ m} \times 0.40\text{ m} = 0.08\text{ m}^2$ (or $8\text{ in} \times 16\text{ in} / 144 = 0.8889\text{ sq ft}$), the theoretical count of blocks ($N_{net}$) required for any wall is:
          </p>
          <div class="formula-box">
            $$A_{net} = (L_{wall} \times H_{wall}) - A_{openings}$$
            $$N_{net} = \frac{A_{net}}{A_{block,face}} = A_{net} (\text{m}^2) \times 12.50 \quad [\text{Metric}]$$
            $$N_{net} = A_{net} (\text{sq ft}) \times 1.125 \quad [\text{Imperial}]$$
          </div>
          <p>
            Accounting for cutting off-cuts around window lintels, plumbing penetration sleeves, and transport breakage, the total order quantity incorporates a waste factor ($W_{\%}$):
          </p>
          <div class="formula-box">
            $$N_{total} = \left\lceil N_{net} \cdot \left(1 + \frac{W_{\%}}{100}\right) \right\rceil$$
          </div>

          <h2>Mortar Mix Design and Sand Requirements (ASTM C270)</h2>
          <p>
            Mortar bonds adjacent masonry units together and accommodates dimensional tolerances. Per <strong>ASTM C270</strong>, structural loadbearing walls utilize <strong>Type S mortar</strong> (minimum 28-day compressive strength of $12.4\text{ MPa}$ / $1,800\text{ psi}$) or <strong>Type M mortar</strong> ($17.2\text{ MPa}$ / $2,500\text{ psi}$ for sub-grade foundation walls).
          </p>
          <p>
            Standard face-shell bedding (where mortar is applied only to the longitudinal outer shells of the block, leaving the inner cores open) consumes:
          </p>
          <div class="formula-box">
            $$\text{Mortar Cement Bags (80 lb / 36 kg)} \approx \frac{N_{total}}{33.3} \approx 3.0 \text{ bags per } 100 \text{ blocks}$$
            $$\text{Masonry Sand Volume} \approx 0.0019 \text{ m}^3 \text{ per block} \implies \approx 0.28 \text{ metric tonnes per } 100 \text{ blocks}$$
          </div>

          <h2>Core Fill Concrete Grouting Mechanics (ASTM C476)</h2>
          <p>
            To achieve high flexural and seismic shear strength, vertical steel deformed reinforcing bars (rebar) are inserted through hollow block cells, and the cores are filled with high-slump fine or coarse concrete grout per <strong>ASTM C476</strong> (slump $200 - 275\text{ mm}$ / $8 - 11\text{ inches}$). Standard two-core hollow $8\text{-inch}$ blocks have approximately $48\%$ void volume. When cores are grouted:
          </p>
          <ul>
            <li><strong>Solid Grout (100% Core Fill):</strong> Consumes $0.0095\text{ m}^3$ ($0.335\text{ cu ft}$) of concrete grout per block.</li>
            <li><strong>Grouting Every 24 inches ($600\text{ mm}$ spacing):</strong> Consumes approximately $0.0032\text{ m}^3$ ($0.112\text{ cu ft}$) per block.</li>
            <li><strong>Grouting Every 48 inches ($1,200\text{ mm}$ spacing):</strong> Consumes approximately $0.0016\text{ m}^3$ ($0.056\text{ cu ft}$) per block.</li>
          </ul>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Standard CMU Nominal Size</th>
                <th>Face Area (m² / sq ft)</th>
                <th>Blocks per 100 m² (sq ft)</th>
                <th>Full Core Grout (m³ / 100 blocks)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>4&times;8&times;16 in (100&times;200&times;400 mm)</td>
                <td>0.080 m² / 0.889 sq ft</td>
                <td>1,250 blocks (112.5)</td>
                <td>0.45 m³ (15.9 cu ft)</td>
              </tr>
              <tr>
                <td>6&times;8&times;16 in (150&times;200&times;400 mm)</td>
                <td>0.080 m² / 0.889 sq ft</td>
                <td>1,250 blocks (112.5)</td>
                <td>0.70 m³ (24.7 cu ft)</td>
              </tr>
              <tr>
                <td>8&times;8&times;16 in (200&times;200&times;400 mm)</td>
                <td>0.080 m² / 0.889 sq ft</td>
                <td>1,250 blocks (112.5)</td>
                <td>0.95 m³ (33.5 cu ft)</td>
              </tr>
              <tr>
                <td>12&times;8&times;16 in (300&times;200&times;400 mm)</td>
                <td>0.080 m² / 0.889 sq ft</td>
                <td>1,250 blocks (112.5)</td>
                <td>1.45 m³ (51.2 cu ft)</td>
              </tr>
            </tbody>
          </table>

          <h2>Horizontal Bond Beams, Control Joints &amp; Crack Control (NCMA TEK 10-2C)</h2>
          <p>
            Concrete masonry units naturally undergo irreversible drying shrinkage and reversible temperature expansion and contraction. Without adequate movement joints and horizontal bond beams, tensile stresses cause unsightly diagonal and stair-stepped wall cracking along mortar joint lines.
          </p>
          <p>
            According to <strong>NCMA TEK 10-2C (Crack Control in Concrete Masonry)</strong>, vertical control joints (CJ) must be positioned throughout uninterrupted wall runs. The maximum recommended spacing between control joints is:
          </p>
          <div class="formula-box">
            $$S_{CJ} \le 1.5 \times H_{wall} \quad \text{and} \quad S_{CJ} \le 25\text{ ft} \ (7.6\text{ m})$$
          </div>
          <p>
            Control joints must also be provided at points of geometric stress concentration, including:
          </p>
          <ul>
            <li>Immediate corners and changes in wall thickness or foundation elevations.</li>
            <li>Within $2\text{ to }4\text{ feet}$ of window and door openings.</li>
            <li>Junctions where loadbearing masonry joins non-loadbearing shear walls.</li>
          </ul>
          <p>
            <strong>Horizontal Bond Beams:</strong> Continuous horizontal bond beams formed with specialized U-shaped lintel blocks are cast at floor and roof bearing levels. Continuous longitudinal deformed steel bars (typically two #4 or #5 bars) encased in concrete grout tie adjacent masonry piers into a monolithic rigid diaphragm, distributing concentrated beam loads and wind uplift forces reliably down to footings.
          </p>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: Commercial Workshop Retaining Foundation Wall</h3>
            <p><strong>Design Scenario:</strong> A commercial light-industrial workshop requires a reinforced concrete block foundation wall measuring $L = 15.0\text{ meters}$ in length by $H = 2.4\text{ meters}$ in height. The wall incorporates two double-door equipment openings totaling $A_{openings} = 4.5\text{ m}^2$. The structural engineering drawing specifies standard $8\times 8\times 16\text{ inch}$ ($200\times 200\times 400\text{ mm}$) hollow loadbearing CMU blocks with a recommended $8\%$ cutting waste allowance. Because the wall serves as an earth-retaining basement perimeter, 100% full solid core grouting is mandatory. Calculate the net masonry area, total blocks to order, required Type S mortar bags, sand tonnage, and total concrete grout volume.</p>
            
            <p><strong>Step 1: Calculate Net Wall Surface Area ($A_{net}$)</strong></p>
            <div class="formula-box">
              $$A_{gross} = L \times H = 15.0\text{ m} \times 2.4\text{ m} = 36.0\text{ m}^2$$
              $$A_{net} = A_{gross} - A_{openings} = 36.0\text{ m}^2 - 4.5\text{ m}^2 = 31.50\text{ m}^2$$
            </div>

            <p><strong>Step 2: Determine Net and Total Block Quantities</strong></p>
            <div class="formula-box">
              $$N_{net} = 31.50\text{ m}^2 \times 12.50\text{ blocks/m}^2 = 393.75\text{ blocks}$$
              $$N_{total} = \lceil 393.75 \times (1 + 0.08) \rceil = \lceil 393.75 \times 1.08 \rceil = \lceil 425.25 \rceil = 426\text{ CMU Blocks}$$
            </div>

            <p><strong>Step 3: Estimate Mortar Cement Bags and Masonry Sand</strong></p>
            <div class="formula-box">
              $$\text{Mortar Bags (36 kg / 80 lb)} = \frac{426}{33.3} \approx 12.8 \implies \text{Order } 13\text{ Bags of Type S Mortar}$$
              $$\text{Masonry Sand} = 426 \times 0.0019\text{ m}^3 = 0.809\text{ m}^3 \times 1.60\text{ t/m}^3 \approx 1.30\text{ Tonnes of Sand}$$
            </div>

            <p><strong>Step 4: Compute Solid Core-Fill Concrete Grout Volume</strong></p>
            <div class="formula-box">
              $$V_{grout} = N_{net} \times 0.0095\text{ m}^3 = 393.75 \times 0.0095\text{ m}^3 = 3.74\text{ m}^3 \quad (\approx 4.89\text{ cu yd})$$
            </div>
            <p>
              <strong>Engineering Procurement Summary:</strong> Specifying <strong>426 blocks</strong>, <strong>13 bags of Type S mortar</strong>, <strong>1.3 tonnes of sand</strong>, and ordering <strong>$4.0\text{ m}^3$</strong> (accounting for pump truck hopper waste) of readymix masonry core grout guarantees full structural compliance with ASTM C90 and NCMA specifications.
            </p>
          </div>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Masonry &amp; Civil Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="brick-calculator.html">Brick Masonry Calculator</a></li>
            <li><a href="concrete-calculator.html">Concrete Volume Calculator</a></li>
            <li><a href="rebar-calculator.html">Rebar Weight &amp; Grid Sizing</a></li>
            <li><a href="retaining-wall-calculator.html">Retaining Wall Sizing</a></li>
            <li><a href="beam-calculator.html">Beam Bending &amp; Shear</a></li>
            <li><a href="asphalt-calculator.html">Asphalt Paving Calculator</a></li>
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
      const calcBtn = document.getElementById('calcBlockBtn');
      const resetBtn = document.getElementById('resetBlockBtn');
      const resultBox = document.getElementById('blockResultBox');
      const unitSystem = document.getElementById('unitSystem');

      const wallLenHint = document.getElementById('wallLenHint');
      const wallHgtHint = document.getElementById('wallHgtHint');
      const openingsHint = document.getElementById('openingsHint');

      const wallLength = document.getElementById('wallLength');
      const wallHeight = document.getElementById('wallHeight');
      const openingsArea = document.getElementById('openingsArea');

      unitSystem.addEventListener('change', function() {
        if (this.value === 'metric') {
          wallLenHint.textContent = 'Length of continuous block wall in meters';
          wallHgtHint.textContent = 'Height from footing top to bond beam in meters';
          openingsHint.textContent = 'Total area of window/door openings in m²';
          if (parseFloat(wallLength.value) > 20) wallLength.value = (parseFloat(wallLength.value) * 0.3048).toFixed(1);
          if (parseFloat(wallHeight.value) > 6) wallHeight.value = (parseFloat(wallHeight.value) * 0.3048).toFixed(1);
          if (parseFloat(openingsArea.value) > 20) openingsArea.value = (parseFloat(openingsArea.value) * 0.092903).toFixed(1);
        } else {
          wallLenHint.textContent = 'Length of continuous block wall in feet';
          wallHgtHint.textContent = 'Height from footing top to bond beam in feet';
          openingsHint.textContent = 'Total area of window/door openings in sq ft';
          if (parseFloat(wallLength.value) < 20) wallLength.value = (parseFloat(wallLength.value) / 0.3048).toFixed(1);
          if (parseFloat(wallHeight.value) < 6) wallHeight.value = (parseFloat(wallHeight.value) / 0.3048).toFixed(1);
          if (parseFloat(openingsArea.value) < 20) openingsArea.value = (parseFloat(openingsArea.value) / 0.092903).toFixed(1);
        }
      });

      function calculateBlock() {
        const isMetric = unitSystem.value === 'metric';
        const L = parseFloat(wallLength.value);
        const H = parseFloat(wallHeight.value);
        const A_open = parseFloat(openingsArea.value) || 0;
        const wastePct = parseFloat(document.getElementById('wasteFactor').value);
        const groutMode = document.getElementById('coreGrouting').value;
        const blockPreset = document.getElementById('blockSizePreset').value;

        if (isNaN(L) || L <= 0 || isNaN(H) || H <= 0) {
          alert('Please enter valid positive values for wall length and height.');
          return;
        }

        // Calculate net area
        const grossArea = L * H;
        const netArea = Math.max(0.1, grossArea - A_open);

        // Blocks per area unit
        let blocksPerM2 = 12.5; // Standard 8x8x16 (0.08 m2)
        let groutM3PerBlock = 0.0095; // 8x8x16 full grout

        if (blockPreset === '6_8_16') {
          blocksPerM2 = 12.5;
          groutM3PerBlock = 0.0070;
        } else if (blockPreset === '4_8_16') {
          blocksPerM2 = 12.5;
          groutM3PerBlock = 0.0045;
        } else if (blockPreset === '12_8_16') {
          blocksPerM2 = 12.5;
          groutM3PerBlock = 0.0145;
        } else if (blockPreset === 'metric_cmu') {
          blocksPerM2 = 10.0; // 215x140x440
          groutM3PerBlock = 0.0080;
        }

        // Convert area to m2 if imperial
        const netArea_m2 = isMetric ? netArea : netArea * 0.092903;

        // Net blocks
        const netBlocks = netArea_m2 * blocksPerM2;
        // Total blocks with waste
        const totalBlocks = Math.ceil(netBlocks * (1.0 + wastePct / 100.0));

        // Mortar bags (80 lb / 36 kg)
        const mortarBags = Math.ceil(totalBlocks / 33.3);
        // Sand in metric tonnes (approx 1.9 m3 sand per 1000 blocks = 0.0019 * 1.6 t)
        const sandTonnes = totalBlocks * 0.0019 * 1.60;
        const sandUS_tons = sandTonnes * 1.10231;

        // Grout volume
        let groutVol_m3 = 0;
        if (groutMode === 'full') {
          groutVol_m3 = netBlocks * groutM3PerBlock;
        } else if (groutMode === 'rebar_24') {
          groutVol_m3 = netBlocks * (groutM3PerBlock * 0.33);
        } else if (groutMode === 'rebar_48') {
          groutVol_m3 = netBlocks * (groutM3PerBlock * 0.17);
        }
        const groutVol_cuyd = groutVol_m3 * 1.30795;

        // Display results
        document.getElementById('resTotalBlocks').textContent = totalBlocks.toLocaleString('en-US') + ' Blocks';
        document.getElementById('resNetBlocks').textContent = Math.ceil(netBlocks).toLocaleString('en-US') + ' Blocks (Zero Waste)';
        document.getElementById('resNetArea').textContent = netArea.toFixed(2) + (isMetric ? ' m²' : ' sq ft') + ' (' + netArea_m2.toFixed(1) + ' m²)';
        document.getElementById('resMortarBags').textContent = mortarBags + ' Bags (Type S/N)';
        document.getElementById('resSandTons').textContent = sandTonnes.toFixed(2) + ' Tonnes (' + sandUS_tons.toFixed(2) + ' US Tons)';
        document.getElementById('resGroutVol').textContent = groutMode === 'none' ? '0 m³ (Hollow Masonry)' : (groutVol_m3.toFixed(2) + ' m³ (' + groutVol_cuyd.toFixed(2) + ' cu yd)');

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculateBlock);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
      });

      calculateBlock();
    });
  </script>
</body>
</html>
"""

def main():
    with open("beam-calculator.html", "w", encoding="utf-8") as f:
        f.write(TOOL_1_HTML.strip() + "\n")
    print("[PASS] beam-calculator.html generated successfully!")

    with open("block-calculator.html", "w", encoding="utf-8") as f:
        f.write(TOOL_2_HTML.strip() + "\n")
    print("[PASS] block-calculator.html generated successfully!")

if __name__ == "__main__":
    main()
