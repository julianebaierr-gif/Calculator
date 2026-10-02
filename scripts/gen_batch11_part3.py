# -*- coding: utf-8 -*-
"""
Script to generate Batch 11 Part 3 tools:
5. spring-rate-calculator.html
6. thermal-expansion-calculator.html
"""
import os

TOOL_5_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Spring Rate Calculator | Helical Compression Spring Design</title>
  <meta name="description" content="Calculate helical compression spring rate (k in N/mm &amp; lbf/in), Wahl stress factor, solid height, and maximum shear stress per ASTM A228 and SMI standards.">
  <link rel="canonical" href="https://calchub.cloud/spring-rate-calculator.html">
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
        "name": "Spring Rate Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Helical compression spring design calculator evaluating spring rate k = (G * d^4) / (8 * D^3 * na), spring index C, Wahl curvature stress factor, and solid height per SMI standards.",
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
            "name": "What is the formula for helical compression spring rate (k)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The classic round-wire helical compression spring rate formula is: k = (G * d^4) / (8 * D^3 * na), where G is torsional shear modulus of the wire material, d is wire diameter, D is mean coil diameter (Outer Diameter minus wire diameter), and na is the count of active working coils."
            }
          },
          {
            "@type": "Question",
            "name": "What is the Spring Index (C) and why does it matter?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The spring index is the dimensionless ratio of mean coil diameter to wire diameter: C = D / d. Recommended industrial design practice maintains C between 4 and 12. Values below 4 cause severe localized curvature stress and tooling breakage during coiling; values above 12 result in tangled, flimsy coils prone to buckling."
            }
          },
          {
            "@type": "Question",
            "name": "What is the Wahl curvature factor in spring stress calculations?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Because spring wire is curved into a helix and subjected to direct transverse shear, shear stress on the inner surface of the coil is magnified. The Wahl factor Kw = (4C - 1) / (4C - 4) + 0.615 / C corrects for this stress peak. True maximum shear stress is: tau_max = Kw * (8 * F * D) / (pi * d^3)."
            }
          },
          {
            "@type": "Question",
            "name": "How does end coil type determine the number of active coils (na)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For squared and ground ends (the industrial standard for stable seating), the two end coils do not deflect: na = nt - 2, where nt is total coils. For squared-only (unground) ends, na = nt - 2. For plain unground ends, all coils deflect: na = nt."
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
      <span>Spring Rate Calculator</span>
    </nav>

    <header class="calc-header">
      <div class="calc-badge">Spring Mechanics &amp; Machine Design</div>
      <h1 class="calc-title">Spring Rate Calculator</h1>
      <p class="calc-tagline">Calculate helical compression spring constant ($k$), spring index ($C$), Wahl stress factor, solid deflection height, and peak torsional shear stress.</p>
    </header>

    <div class="calc-grid">
      <div class="calc-main">
        <div class="tool-card">
          <form id="springForm">
            <div class="form-row">
              <div class="form-group">
                <label for="wireMaterial">Spring Material Specification ($G$ Modulus)</label>
                <select id="wireMaterial" class="form-control">
                  <option value="79300" selected>Music Wire ASTM A228 (High Carbon Steel, G = 79.3 GPa)</option>
                  <option value="78600">Oil-Tempered Wire ASTM A229 (G = 78.6 GPa)</option>
                  <option value="79300_cr">Chrome Silicon ASTM A401 (High Fatigue, G = 79.3 GPa)</option>
                  <option value="69000">Stainless Steel 302/304 ASTM A313 (Corrosion, G = 69.0 GPa)</option>
                  <option value="71000">Stainless Steel 17-7 PH (Precipitation Hardened, G = 71.0 GPa)</option>
                  <option value="41400">Phosphor Bronze ASTM B159 (Non-Magnetic, G = 41.4 GPa)</option>
                  <option value="custom">Custom Shear Modulus ($G$)</option>
                </select>
              </div>
              <div class="form-group">
                <label for="gModulus">Torsional Shear Modulus ($G$ in MPa)</label>
                <input type="number" id="gModulus" class="form-control" value="79300" min="1000" step="100" required>
                <span class="hint">1 GPa = 1,000 MPa = 1,000 N/mm²</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="wireDia">Wire Diameter ($d$ in mm)</label>
                <input type="number" id="wireDia" class="form-control" value="3.5" min="0.1" step="any" required>
                <span class="hint">Gauge / cross-sectional diameter of the wire</span>
              </div>
              <div class="form-group">
                <label for="outerDia">Outer Coil Diameter ($D_{outer}$ in mm)</label>
                <input type="number" id="outerDia" class="form-control" value="28.0" min="0.5" step="any" required>
                <span class="hint">Mean diameter $D = D_{outer} - d$</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="totalCoils">Total Number of Coils ($n_t$)</label>
                <input type="number" id="totalCoils" class="form-control" value="9.5" min="1" step="0.25" required>
                <span class="hint">Total coils counted tip-to-tip</span>
              </div>
              <div class="form-group">
                <label for="endType">Spring End Coil Geometry</label>
                <select id="endType" class="form-control">
                  <option value="sq_ground" selected>Squared &amp; Ground Ends ($n_a = n_t - 2$)</option>
                  <option value="squared">Squared / Closed Unground ($n_a = n_t - 2$)</option>
                  <option value="plain_ground">Plain &amp; Ground Ends ($n_a = n_t - 1$)</option>
                  <option value="plain">Plain Open Ends ($n_a = n_t$)</option>
                </select>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="freeLength">Free Length ($L_{free}$ in mm)</label>
                <input type="number" id="freeLength" class="form-control" value="65.0" min="1" step="any" required>
                <span class="hint">Unloaded overall spring length</span>
              </div>
              <div class="form-group">
                <label for="appliedLoad">Design Working Load ($F$ in Newtons)</label>
                <input type="number" id="appliedLoad" class="form-control" value="350" min="0" step="any">
                <span class="hint">Applied compressive operating force</span>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcSpringBtn">Calculate Spring Mechanics</button>
              <button type="reset" class="btn btn-secondary" id="resetSpringBtn">Reset</button>
            </div>
          </form>

          <div id="springResultBox" class="results-container" style="display: none; margin-top: 1.5rem;">
            <h3>Calculated Helical Spring Characteristics</h3>
            <div class="results-grid">
              <div class="result-tile highlight">
                <span class="result-label">Spring Constant / Rate ($k$)</span>
                <span class="result-value" id="resSpringRate">-- N/mm</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Spring Rate in Imperial</span>
                <span class="result-value" id="resRateImperial">-- lbf/in</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Spring Index ($C = D / d$)</span>
                <span class="result-value" id="resSpringIndex">--</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Wahl Stress Factor ($K_w$)</span>
                <span class="result-value" id="resWahlFactor">--</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Solid Height ($H_s$)</span>
                <span class="result-value" id="resSolidHeight">-- mm</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Max Deflection to Solid ($\delta_s$)</span>
                <span class="result-value" id="resMaxDeflection">-- mm</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Operating Deflection under Load</span>
                <span class="result-value" id="resWorkDeflection">-- mm</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Wahl Corrected Shear Stress ($\tau_{max}$)</span>
                <span class="result-value" id="resShearStress">-- MPa</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Engineering Mechanics of Helical Compression Springs</h2>
          <p>
            <strong>Helical compression springs</strong> are ubiquitous machine elements designed to absorb mechanical shock, store elastic potential energy, maintain tension between mating assemblies, and exert controlled clamping forces in automotive suspensions, aerospace valves, electrical switches, and industrial machinery. Despite their apparent axial motion, the primary mode of internal stress in a helical spring is pure <strong>torsion (twisting)</strong> of the coiled circular wire.
          </p>
          <p>
            When an external compressive axial force ($F$) is applied, it exerts a twisting torque ($T = F \times \frac{D}{2}$) throughout the continuous active length of the coiled helix. According to energy principles and Castigliano's theorem, the relationship between axial compressive deflection ($\delta$) and applied force establishes the fundamental spring constant or <strong>spring rate ($k$)</strong>:
          </p>
          <div class="formula-box">
            $$k = \frac{F}{\delta} = \frac{G \cdot d^4}{8 \cdot D^3 \cdot n_a} \quad [\text{N/mm or lbf/in}]$$
          </div>
          <p>
            Where:
          </p>
          <ul>
            <li>$G$ is the torsional shear modulus of elasticity of the spring wire material ($\text{N/mm}^2$ or $\text{MPa}$).</li>
            <li>$d$ is the wire cross-sectional diameter ($\text{mm}$).</li>
            <li>$D$ is the mean coil diameter ($D = D_{outer} - d = D_{inner} + d$) in millimeters.</li>
            <li>$n_a$ is the number of active deflection coils.</li>
          </ul>

          <h2>Spring Index ($C$) and the Wahl Curvature Correction Factor ($K_w$)</h2>
          <p>
            The geometric proportion of a helical spring is governed by its <strong>Spring Index ($C$)</strong>:
          </p>
          <div class="formula-box">
            $$C = \frac{D}{d}$$
          </div>
          <p>
            Per the Spring Manufacturers Institute (SMI) design manual, optimal manufacturing and fatigue performance occurs when $4.0 \le C \le 12.0$. If $C < 4$, the wire is coiled so tightly that extreme plastic residual stresses develop on the inner surface during manufacturing, and coiling pins experience severe wear. If $C > 12$, the coils lack structural lateral rigidity, making them prone to tangling during bulk transport and susceptible to lateral buckling during axial deflection.
          </p>
          <p>
            Because the wire is curved rather than straight, the stress distribution across the wire cross-section is non-linear. The inner radius of the coil experiences higher fiber strain than the outer radius. Dr. A. M. Wahl (Westinghouse Electric) developed the theoretical curvature correction factor ($K_w$) combining direct transverse shear with toroidal curvature concentration:
          </p>
          <div class="formula-box">
            $$K_w = \frac{4C - 1}{4C - 4} + \frac{0.615}{C}$$
          </div>
          <p>
            The true peak torsional shear stress ($\tau_{max}$) occurring at the innermost fiber of the wire under applied load $F$ is:
          </p>
          <div class="formula-box">
            $$\tau_{max} = K_w \cdot \left(\frac{8 \cdot F \cdot D}{\pi \cdot d^3}\right) \quad [\text{MPa}]$$
          </div>

          <h2>Active vs. Inactive Coils by End Architecture</h2>
          <p>
            The physical manner in which spring ends are formed dictates how many coils participate in elastic energy storage:
          </p>
          <table class="reference-table">
            <thead>
              <tr>
                <th>End Formation Style</th>
                <th>Active Coils ($n_a$)</th>
                <th>Solid Height ($H_s$) Formula</th>
                <th>Squareness / Seating Characteristic</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Squared &amp; Ground (Closed &amp; Ground)</td>
                <td>$n_a = n_t - 2.0$</td>
                <td>$H_s = n_t \cdot d$</td>
                <td>Best seating stability; perpendicularity &le; 1.5&deg;; industry standard</td>
              </tr>
              <tr>
                <td>Squared / Closed Unground</td>
                <td>$n_a = n_t - 2.0$</td>
                <td>$H_s = (n_t + 1) \cdot d$</td>
                <td>Economical closed end; slight seating tilt; wire end remains full diameter</td>
              </tr>
              <tr>
                <td>Plain Open Ends (Unground)</td>
                <td>$n_a = n_t$</td>
                <td>$H_s = (n_t + 1) \cdot d$</td>
                <td>All coils active; poor seating stability; requires guide rod or recess</td>
              </tr>
              <tr>
                <td>Plain Ground Ends</td>
                <td>$n_a = n_t - 1.0$</td>
                <td>$H_s = n_t \cdot d$</td>
                <td>Improved flat seating while maintaining open pitch at extremities</td>
              </tr>
            </tbody>
          </table>

          <h2>Solid Height ($H_s$) and Maximum Available Travel ($\delta_s$)</h2>
          <p>
            The <strong>solid height ($H_s$)</strong> represents the axial length of the spring when it is compressed completely flat until all adjacent coils press against one another. Compressing a spring beyond solid height causes permanent mechanical jam and catastrophic destruction of the wire surface. The maximum permissible travel from the unloaded free length ($L_{free}$) to solid closure is:
          </p>
          <div class="formula-box">
            $$\delta_s = L_{free} - H_s$$
          </div>
          <p>
            To prevent coil binding and noise during continuous cyclic operation, good engineering practice limits maximum operating deflection to no more than $80\% - 85\%$ of the available travel to solid ($\delta_{work} \le 0.85 \cdot \delta_s$).
          </p>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: High-Pressure Relief Valve Spring Design</h3>
            <p><strong>Design Scenario:</strong> An industrial safety relief valve requires a spring that cracks open at an axial preload force of $F = 350\text{ N}$ with an intended cracking deflection of $\delta = 14.0\text{ mm}$ (demanding a target spring rate of $k = 350 / 14 = 25.0\text{ N/mm}$). The design uses cold-drawn music wire ASTM A228 ($G = 79,300\text{ MPa}$, minimum tensile strength $S_{ut} = 1,750\text{ MPa}$). The housing limits the outer coil diameter to $D_{outer} \le 28.0\text{ mm}$. A wire diameter of $d = 3.5\text{ mm}$ with $n_t = 9.5$ total coils (squared and ground ends) is proposed, with an overall free length of $L_{free} = 65.0\text{ mm}$. Evaluate the actual spring rate, spring index, solid height, and check that shear stress under full load remains within the allowable torsional yield limit ($\tau_{allow} \approx 0.45 S_{ut} \approx 787\text{ MPa}$).</p>
            
            <p><strong>Step 1: Determine Mean Coil Diameter and Active Coils</strong></p>
            <div class="formula-box">
              $$D = D_{outer} - d = 28.0\text{ mm} - 3.5\text{ mm} = 24.5\text{ mm}$$
              $$n_a = n_t - 2.0 = 9.5 - 2.0 = 7.5\text{ active coils}$$
            </div>

            <p><strong>Step 2: Calculate the Spring Constant / Rate ($k$)</strong></p>
            <div class="formula-box">
              $$d^4 = (3.5)^4 = 150.0625\text{ mm}^4$$
              $$D^3 = (24.5)^3 = 14,706.125\text{ mm}^3$$
              $$k = \frac{79,300 \times 150.0625}{8 \times 14,706.125 \times 7.5} = \frac{11,899,956}{882,367.5} \approx 13.486\text{ N/mm}$$
            </div>

            <p><strong>Step 3: Calculate Spring Index ($C$) and Wahl Factor ($K_w$)</strong></p>
            <div class="formula-box">
              $$C = \frac{D}{d} = \frac{24.5}{3.5} = 7.00 \quad (\text{Optimal range: } 4 \le C \le 12)$$
              $$K_w = \frac{4(7) - 1}{4(7) - 4} + \frac{0.615}{7} = \frac{27}{24} + 0.08786 = 1.125 + 0.0879 = 1.2129$$
            </div>

            <p><strong>Step 4: Evaluate Solid Height and Deflection Capacity</strong></p>
            <div class="formula-box">
              $$H_s = n_t \times d = 9.5 \times 3.5\text{ mm} = 33.25\text{ mm}$$
              $$\delta_s = L_{free} - H_s = 65.0 - 33.25 = 31.75\text{ mm}$$
            </div>

            <p><strong>Step 5: Verify Wahl Corrected Shear Stress at $F = 350\text{ N}$</strong></p>
            <div class="formula-box">
              $$\tau_{max} = 1.2129 \times \frac{8 \times 350\text{ N} \times 24.5\text{ mm}}{\pi \times (3.5\text{ mm})^3} = 1.2129 \times \frac{68,600}{134.696} = 1.2129 \times 509.30 \approx 617.7\text{ MPa}$$
            </div>
            <p>
              <strong>Engineering Conclusion:</strong> The maximum operating shear stress of $617.7\text{ MPa}$ is safely below the allowable static limit of $787\text{ MPa}$ ($78.5\%$ of allowable), ensuring long fatigue life and zero permanent plastic set under continuous valve operation.
            </p>
          </div>

          <h2>Spring Buckling Stability and Slenderness Ratio ($L_{free} / D$)</h2>
          <p>
            When a slender compression spring is compressed, it behaves analogously to an Euler column subjected to axial compression. If the free length of the spring is large relative to its mean coil diameter, the spring becomes unstable and will buckle laterally under axial load:
          </p>
          <div class="formula-box">
            $$\text{Slenderness Ratio} = \frac{L_{free}}{D}$$
          </div>
          <p>
            Per SMI and DIN 2089 recommendations:
          </p>
          <ul>
            <li><strong>Stable Region ($L_{free} / D \le 4.0$):</strong> Helical springs with squared and ground ends remain laterally stable throughout their entire deflection travel up to solid height without external guidance.</li>
            <li><strong>Buckling Prone Region ($L_{free} / D > 4.0$):</strong> The spring is prone to lateral snaking or buckling when compressed beyond critical deflection ($\delta_{cr}$). For such slender springs, mechanical designers must specify an internal guide mandrel rod or an external guide sleeve (clearance $\approx 0.1 \cdot d$) to maintain axial alignment and prevent coil clashing.</li>
          </ul>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Machine Design Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="shaft-diameter-calculator.html">Shaft Diameter Sizing</a></li>
            <li><a href="bolt-torque-calculator.html">Bolt Torque &amp; Preload</a></li>
            <li><a href="flywheel-energy-calculator.html">Flywheel Energy Storage</a></li>
            <li><a href="power-to-torque-calculator.html">Power to Torque Calculator</a></li>
            <li><a href="bearing-life-calculator.html">Bearing Life (ISO 281)</a></li>
            <li><a href="thermal-expansion-calculator.html">Thermal Expansion Calculator</a></li>
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
      const calcBtn = document.getElementById('calcSpringBtn');
      const resetBtn = document.getElementById('resetSpringBtn');
      const resultBox = document.getElementById('springResultBox');

      const wireMaterial = document.getElementById('wireMaterial');
      const gModulus = document.getElementById('gModulus');
      const wireDia = document.getElementById('wireDia');
      const outerDia = document.getElementById('outerDia');
      const totalCoils = document.getElementById('totalCoils');
      const endType = document.getElementById('endType');
      const freeLength = document.getElementById('freeLength');
      const appliedLoad = document.getElementById('appliedLoad');

      wireMaterial.addEventListener('change', function() {
        if (this.value !== 'custom') {
          const val = this.value.split('_')[0];
          gModulus.value = val;
        }
      });

      function calculateSpring() {
        const G = parseFloat(gModulus.value);
        const d = parseFloat(wireDia.value);
        const D_out = parseFloat(outerDia.value);
        const nt = parseFloat(totalCoils.value);
        const ends = endType.value;
        const L_free = parseFloat(freeLength.value);
        const F = parseFloat(appliedLoad.value) || 0;

        if (isNaN(G) || G <= 0 || isNaN(d) || d <= 0 || isNaN(D_out) || D_out <= d || isNaN(nt) || nt <= 0) {
          alert('Please enter valid positive spring dimensions (D_out must be greater than wire diameter d).');
          return;
        }

        // Mean diameter D
        const D = D_out - d;
        // Spring index C
        const C = D / d;

        // Active coils na
        let na = nt;
        let Hs = nt * d;
        if (ends === 'sq_ground') {
          na = Math.max(0.5, nt - 2.0);
          Hs = nt * d;
        } else if (ends === 'squared') {
          na = Math.max(0.5, nt - 2.0);
          Hs = (nt + 1.0) * d;
        } else if (ends === 'plain_ground') {
          na = Math.max(0.5, nt - 1.0);
          Hs = nt * d;
        } else if (ends === 'plain') {
          na = nt;
          Hs = (nt + 1.0) * d;
        }

        // Spring rate k = (G * d^4) / (8 * D^3 * na) [N/mm]
        const d4 = Math.pow(d, 4);
        const D3 = Math.pow(D, 3);
        const k_N_mm = (G * d4) / (8.0 * D3 * na);
        // Convert to lbf/in: 1 N/mm = 5.710147 lbf/in
        const k_lbf_in = k_N_mm * 5.710147;

        // Wahl factor Kw = (4C - 1) / (4C - 4) + 0.615 / C
        const Kw = ((4.0 * C - 1.0) / (4.0 * C - 4.0)) + (0.615 / C);

        // Solid deflection delta_s
        const delta_s = Math.max(0, L_free - Hs);

        // Operating deflection under load F
        const workDeflection = F > 0 ? (F / k_N_mm) : 0;

        // Shear stress tau = Kw * (8 * F * D) / (pi * d^3)
        let tau_MPa = 0;
        if (F > 0) {
          tau_MPa = Kw * ((8.0 * F * D) / (Math.PI * Math.pow(d, 3)));
        }

        // Render outputs
        document.getElementById('resSpringRate').textContent = k_N_mm.toFixed(3) + ' N/mm';
        document.getElementById('resRateImperial').textContent = k_lbf_in.toFixed(2) + ' lbf/in';
        document.getElementById('resSpringIndex').textContent = C.toFixed(2) + (C < 4 ? ' (Too tight, high stress)' : (C > 12 ? ' (Prone to tangle/buckle)' : ' (Optimal 4–12 range)'));
        document.getElementById('resWahlFactor').textContent = Kw.toFixed(3);
        document.getElementById('resSolidHeight').textContent = Hs.toFixed(2) + ' mm';
        document.getElementById('resMaxDeflection').textContent = delta_s.toFixed(2) + ' mm';
        document.getElementById('resWorkDeflection').textContent = workDeflection > 0 ? (workDeflection.toFixed(2) + ' mm (' + ((workDeflection / delta_s) * 100).toFixed(1) + '% to solid)') : '0 mm (Unloaded)';
        document.getElementById('resShearStress').textContent = tau_MPa > 0 ? (tau_MPa.toFixed(1) + ' MPa') : '0 MPa';

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculateSpring);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
      });

      calculateSpring();
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
  <title>Thermal Expansion Calculator | Linear, Volumetric &amp; Pipe Stress</title>
  <meta name="description" content="Calculate linear (&Delta;L), volumetric (&Delta;V), and thermal expansion stress for metals, piping, concrete, and plastics per ASME B31.3 &amp; ASTM E228.">
  <link rel="canonical" href="https://calchub.cloud/thermal-expansion-calculator.html">
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
        "name": "Thermal Expansion Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Thermo-mechanical expansion engine computing linear Delta L = alpha * L * Delta T, volumetric Delta V, constrained compressive stress, and expansion loop sizing per ASME B31.3.",
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
            "name": "What is the formula for linear thermal expansion?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The change in length (Delta L) due to temperature change is calculated as: Delta L = L_0 * alpha * Delta T, where L_0 is initial length, alpha is the material coefficient of linear thermal expansion (typically expressed in 10^-6 / deg C or 10^-6 / deg F), and Delta T = T_final - T_initial."
            }
          },
          {
            "@type": "Question",
            "name": "What is the relationship between linear (alpha) and volumetric (beta) thermal expansion?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For isotropic solid materials expanding uniformly in all three spatial dimensions, the volumetric expansion coefficient beta is approximately three times the linear coefficient: beta approx 3 * alpha. Area expansion is approximately two times the linear coefficient: gamma approx 2 * alpha."
            }
          },
          {
            "@type": "Question",
            "name": "How is thermal stress calculated when thermal expansion is completely restrained?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "When a structural member or piping run is clamped rigidly between immovable anchors, thermal strain (epsilon_th = alpha * Delta T) cannot expand physically. By Hooke's Law, this generates immense internal compressive stress: sigma_th = E * alpha * Delta T, where E is Young's modulus of elasticity."
            }
          },
          {
            "@type": "Question",
            "name": "How does ASME B31.3 recommend absorbing thermal growth in process piping?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Rather than allowing rigid thermal stress to buckle pipe supports or tear nozzle flanges from pumps and boilers, piping engineers install flexible expansion loops (U-bends), directional Z-bends, or bellows expansion joints that flex elastically to absorb the computed Delta L growth."
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
      <span>Thermal Expansion Calculator</span>
    </nav>

    <header class="calc-header">
      <div class="calc-badge">Thermal Mechanics &amp; Piping</div>
      <h1 class="calc-title">Thermal Expansion Calculator</h1>
      <p class="calc-tagline">Calculate linear and volumetric thermal expansion, constrained compressive stress, and piping expansion loop sizing per ASME B31.3 and ASTM E228.</p>
    </header>

    <div class="calc-grid">
      <div class="calc-main">
        <div class="tool-card">
          <form id="thermalForm">
            <div class="form-row">
              <div class="form-group">
                <label for="materialPreset">Material Selection (Thermal Coefficient $\alpha$)</label>
                <select id="materialPreset" class="form-control">
                  <option value="12.0" selected>Structural Carbon Steel (α = 12.0 × 10⁻⁶ /°C, E = 200 GPa)</option>
                  <option value="17.3">Stainless Steel 304 / 316 (α = 17.3 × 10⁻⁶ /°C, E = 193 GPa)</option>
                  <option value="23.1">Aluminum 6061-T6 (α = 23.1 × 10⁻⁶ /°C, E = 69 GPa)</option>
                  <option value="16.5">Copper C11000 (α = 16.5 × 10⁻⁶ /°C, E = 117 GPa)</option>
                  <option value="18.7">Brass C36000 (α = 18.7 × 10⁻⁶ /°C, E = 100 GPa)</option>
                  <option value="10.8">Cast Iron Gray (α = 10.8 × 10⁻⁶ /°C, E = 110 GPa)</option>
                  <option value="10.0">Structural Concrete (α = 10.0 × 10⁻⁶ /°C, E = 30 GPa)</option>
                  <option value="54.0">PVC Pipe (Rigid) (α = 54.0 × 10⁻⁶ /°C, E = 3 GPa)</option>
                  <option value="1.2">Invar 36 (Low Expansion Alloy) (α = 1.2 × 10⁻⁶ /°C, E = 148 GPa)</option>
                  <option value="custom">Custom Thermal Expansion Coefficient</option>
                </select>
              </div>
              <div class="form-group">
                <label for="alphaCoeff">Expansion Coefficient ($\alpha$ in $10^{-6}\text{ /}^\circ\text{C}$)</label>
                <input type="number" id="alphaCoeff" class="form-control" value="12.0" min="0.01" step="any" required>
                <span class="hint">Linear thermal expansion per unit temperature change</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="initLength">Initial Length ($L_0$ in meters)</label>
                <input type="number" id="initLength" class="form-control" value="25.0" min="0.01" step="any" required>
                <span class="hint">Total length of pipeline, structural beam, or rail track</span>
              </div>
              <div class="form-group">
                <label for="elasticModulus">Young's Modulus of Elasticity ($E$ in GPa)</label>
                <input type="number" id="elasticModulus" class="form-control" value="200" min="1" step="1" required>
                <span class="hint">Used to evaluate constrained thermal stress ($\sigma = E \cdot \alpha \cdot \Delta T$)</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="tempInitial">Initial Installation Temperature ($T_{initial}$)</label>
                <input type="number" id="tempInitial" class="form-control" value="20" step="any" required>
                <span class="hint">Ambient construction temperature (e.g. 20&deg;C)</span>
              </div>
              <div class="form-group">
                <label for="tempFinal">Maximum Operating Temperature ($T_{final}$)</label>
                <input type="number" id="tempFinal" class="form-control" value="120" step="any" required>
                <span class="hint">Peak fluid or environmental temperature (e.g. steam line = 120&deg;C)</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="crossSection">Conduit / Beam Cross-Section Area ($A_{cross}$ in mm²)</label>
                <input type="number" id="crossSection" class="form-control" value="2165" min="1" step="any">
                <span class="hint">E.g., 4-inch Sch 40 pipe wall area ≈ 2,165 mm² (optional for force)</span>
              </div>
              <div class="form-group">
                <label for="pipeOuterDia">Pipe Outer Diameter for Loop Sizing ($D_{outer}$ in mm)</label>
                <input type="number" id="pipeOuterDia" class="form-control" value="114.3" min="1" step="any">
                <span class="hint">E.g., 4-inch pipe OD = 114.3 mm</span>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" class="btn btn-primary" id="calcThermalBtn">Calculate Thermal Growth &amp; Stress</button>
              <button type="reset" class="btn btn-secondary" id="resetThermalBtn">Reset</button>
            </div>
          </form>

          <div id="thermalResultBox" class="results-container" style="display: none; margin-top: 1.5rem;">
            <h3>Thermal Expansion &amp; Stress Sizing</h3>
            <div class="results-grid">
              <div class="result-tile highlight">
                <span class="result-label">Linear Thermal Elongation ($\Delta L$)</span>
                <span class="result-value" id="resDeltaL">-- mm</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Total Expanded Length ($L_{final}$)</span>
                <span class="result-value" id="resFinalLength">-- m</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Temperature Differential ($\Delta T$)</span>
                <span class="result-value" id="resDeltaT">-- &deg;C</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Fully Constrained Thermal Stress ($\sigma_{th}$)</span>
                <span class="result-value" id="resThermalStress">-- MPa</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Restraining Anchor Force ($F_{anchor}$)</span>
                <span class="result-value" id="resAnchorForce">-- kN</span>
              </div>
              <div class="result-tile">
                <span class="result-label">Recommended Expansion U-Loop Leg ($L_{leg}$)</span>
                <span class="result-value" id="resLoopLength">-- m</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>Thermodynamic Fundamentals of Thermal Expansion</h2>
          <p>
            All matter expands when subjected to elevated temperatures and contracts when cooled. At the atomic lattice scale, increasing thermal kinetic energy intensifies the vibrational amplitude of constituent atoms within their intermolecular potential energy wells. Because atomic bonding potential energy curves (such as the Lennard-Jones potential) are inherently asymmetric (anharmonic), atoms vibrate with larger separation distances at higher thermal energy states, manifesting macroscopically as <strong>thermal expansion</strong>.
          </p>
          <p>
            In mechanical piping networks (ASME B31.1 / ASME B31.3), civil structural engineering (continuous welded rail track, concrete bridge spans), and machine tool design, failure to accommodate thermal expansion can generate millions of Newtons of destructive anchor forces, leading to pipeline buckling, flange joint leakage, structural shear, and fatigue rupture.
          </p>

          <h2>Linear Thermal Expansion Formulation ($\Delta L$)</h2>
          <p>
            For moderate temperature differentials where the material coefficient remains essentially constant, linear thermal expansion is directly proportional to initial length ($L_0$) and temperature increase ($\Delta T$):
          </p>
          <div class="formula-box">
            $$\Delta L = L_0 \cdot \alpha \cdot \Delta T = L_0 \cdot \alpha \cdot (T_{final} - T_{initial})$$
          </div>
          <p>
            Where:
          </p>
          <ul>
            <li>$\Delta L$ is the axial dimensional elongation in meters or millimeters.</li>
            <li>$L_0$ is the initial original length of the structural member.</li>
            <li>$\alpha$ is the Coefficient of Linear Thermal Expansion ($\text{CLTE}$), conventionally expressed in units of $10^{-6}\text{ /}^\circ\text{C}$ or $\mu\text{m/(m}\cdot\text{K)}$.</li>
            <li>$\Delta T$ is the positive or negative temperature swing ($^\circ\text{C}$ or $\text{K}$).</li>
          </ul>

          <h2>Volumetric ($\beta$) and Superficial ($\gamma$) Expansion</h2>
          <p>
            In three-dimensional solid bodies and liquid reservoirs, thermal growth occurs across all spatial coordinates. For isotropic materials:
          </p>
          <div class="formula-box">
            $$\text{Area Expansion: } \Delta A \approx 2 \cdot \alpha \cdot A_0 \cdot \Delta T$$
            $$\text{Volumetric Expansion: } \Delta V = V_0 \cdot \beta \cdot \Delta T \approx 3 \cdot \alpha \cdot V_0 \cdot \Delta T$$
          </div>
          <p>
            Where $\beta \approx 3\alpha$ is the coefficient of volumetric thermal expansion. In closed liquid systems (such as domestic hydronic heating loops or transformer oil tanks), liquid volumetric expansion far exceeds the volumetric expansion of the enclosing steel vessel ($\beta_{water} \approx 207 \times 10^{-6} \gg \beta_{steel} \approx 36 \times 10^{-6}$), necessitating pre-charged diaphragm expansion vessels to prevent hydrostatic over-pressurization.
          </p>

          <h2>Constrained Thermal Stress ($\sigma_{th}$) and Restraining Anchor Force</h2>
          <p>
            When a thermal pipe run or continuous welded railway track is completely restrained against axial growth by rigid end anchors or tie clamps, thermal strain ($\epsilon_{th} = \alpha \cdot \Delta T$) is entirely transformed into internal mechanical elastic compressive strain. By Hooke's Law:
          </p>
          <div class="formula-box">
            $$\sigma_{th} = E \cdot \epsilon_{th} = E \cdot \alpha \cdot \Delta T \quad [\text{MPa}]$$
          </div>
          <p>
            Where $E$ is Young's modulus of elasticity in $\text{MPa}$ ($1\text{ GPa} = 1,000\text{ MPa}$). Remarkably, <strong>thermal stress is entirely independent of length</strong>! A $1\text{ meter}$ pipe and a $1,000\text{ meter}$ pipe subjected to the same temperature increase generate identical internal stress if both are rigidly restrained.
          </p>
          <p>
            The total axial thrust force ($F_{anchor}$) exerted by the expanding member against restraining end anchors is:
          </p>
          <div class="formula-box">
            $$F_{anchor} = \sigma_{th} \cdot A_{cross} = E \cdot \alpha \cdot \Delta T \cdot A_{cross} \quad [\text{N}]$$
          </div>

          <h2>ASME B31.3 Piping Expansion Loop Sizing (The Kellogg Formula)</h2>
          <p>
            To avoid massive anchor thrust forces and dangerous thermal stresses, piping systems incorporate flexible structural expansion U-loops. The required minimum leg length of an expansion U-loop ($L_{leg}$) is evaluated per the classic Kellogg formulation:
          </p>
          <div class="formula-box">
            $$L_{leg} = \sqrt{\frac{3 \cdot E \cdot D_{outer} \cdot \Delta L}{S_A}} \approx 0.043 \cdot \sqrt{D_{outer} (\text{mm}) \cdot \Delta L (\text{mm})} \quad [\text{m}]$$
          </div>
          <p>
            Where $D_{outer}$ is the outside pipe diameter and $S_A$ is the allowable displacement stress range per ASME B31.3.
          </p>

          <table class="reference-table">
            <thead>
              <tr>
                <th>Engineering Material</th>
                <th>CLTE $\alpha$ ($10^{-6}$ / &deg;C)</th>
                <th>Elastic Modulus $E$ (GPa)</th>
                <th>Thermal Stress per 50&deg;C Rise ($\sigma_{th}$)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Invar 36 (Ni-Fe Alloy)</td>
                <td>1.2</td>
                <td>148</td>
                <td>8.88 MPa (Ultra-low expansion)</td>
              </tr>
              <tr>
                <td>Structural Concrete</td>
                <td>10.0</td>
                <td>30</td>
                <td>15.0 MPa (Matches rebar steel closely)</td>
              </tr>
              <tr>
                <td>Carbon Steel (ASTM A106 / A36)</td>
                <td>12.0</td>
                <td>200</td>
                <td>120.0 MPa (High compressive stress)</td>
              </tr>
              <tr>
                <td>Copper (ASTM B88 Tube)</td>
                <td>16.5</td>
                <td>117</td>
                <td>96.5 MPa</td>
              </tr>
              <tr>
                <td>Stainless Steel (AISI 304 / 316)</td>
                <td>17.3</td>
                <td>193</td>
                <td>166.9 MPa (Very high thermal growth)</td>
              </tr>
              <tr>
                <td>Aluminum (6061-T6 Alloy)</td>
                <td>23.1</td>
                <td>69</td>
                <td>79.7 MPa (Nearly double steel growth)</td>
              </tr>
              <tr>
                <td>Polyvinyl Chloride (PVC)</td>
                <td>54.0</td>
                <td>3.0</td>
                <td>8.1 MPa (Large growth, low stiffness)</td>
              </tr>
            </tbody>
          </table>

          <div class="worked-example-card">
            <h3>Worked Engineering Case Study: Industrial High-Pressure Steam Piping Run</h3>
            <p><strong>Design Scenario:</strong> An industrial chemical plant installs an outdoor carbon steel steam pipeline (ASTM A106 Grade B, $\alpha = 12.0 \times 10^{-6}\text{ /}^\circ\text{C}$, $E = 200\text{ GPa}$). The nominal pipe size is NPS 4-inch Schedule 40 ($D_{outer} = 114.3\text{ mm}$, pipe wall cross-sectional area $A_{cross} = 2,165\text{ mm}^2$). The straight run between fixed building anchors spans $L_0 = 40.0\text{ m}$. The pipe is installed at Winter ambient conditions ($T_{initial} = 5.0^\circ\text{C}$) and carries saturated steam at $T_{final} = 175.0^\circ\text{C}$ ($\Delta T = 170.0^\circ\text{C}$). Calculate the unrestrained thermal expansion ($\Delta L$), evaluate the theoretical anchor force if rigidly locked, and size a flexible expansion U-loop.</p>
            
            <p><strong>Step 1: Calculate Unrestrained Thermal Elongation ($\Delta L$)</strong></p>
            <div class="formula-box">
              $$\Delta L = L_0 \times \alpha \times \Delta T = 40.0\text{ m} \times (12.0 \times 10^{-6}\text{ /}^\circ\text{C}) \times 170.0^\circ\text{C}$$
              $$\Delta L = 40.0 \times 0.00204 = 0.0816\text{ m} = 81.60\text{ mm}$$
            </div>
            <p>
              The $40\text{ meter}$ pipe run expands by over $81.6\text{ mm}$ (approx. $3.21\text{ inches}$).
            </p>

            <p><strong>Step 2: Calculate Constrained Thermal Stress and Anchor Thrust Force</strong></p>
            <div class="formula-box">
              $$\sigma_{th} = E \times \alpha \times \Delta T = 200,000\text{ MPa} \times (12.0 \times 10^{-6}) \times 170 = 408.0\text{ MPa}$$
              $$F_{anchor} = \sigma_{th} \times A_{cross} = 408.0\text{ N/mm}^2 \times 2,165\text{ mm}^2 = 883,320\text{ N} \approx 883.3\text{ kN} \quad (\approx 90.0\text{ metric tons!})$$
            </div>
            <p>
              An unyielding anchor would experience an immense $883\text{ kN}$ thrust, far exceeding the yield strength of the steel ($S_y = 240\text{ MPa}$) and crushing the pipe wall.
            </p>

            <p><strong>Step 3: Size the Flexible ASME B31.3 Expansion U-Loop Leg</strong></p>
            <div class="formula-box">
              $$L_{leg} \approx 0.043 \times \sqrt{D_{outer} (\text{mm}) \times \Delta L (\text{mm})} = 0.043 \times \sqrt{114.3 \times 81.60}$$
              $$L_{leg} = 0.043 \times \sqrt{9,326.88} = 0.043 \times 96.57 \approx 4.15\text{ meters}$$
            </div>
            <p>
              <strong>Engineering Conclusion:</strong> Installing a symmetrical expansion U-loop with perpendicular legs of $L_{leg} = 4.2\text{ meters}$ absorbs the entire $81.6\text{ mm}$ thermal growth via elastic cantilever bending, reducing anchor loads to benign levels ($< 5\text{ kN}$) and ensuring full compliance with ASME B31.3.
            </p>
          </div>

          <h2>Continuous Welded Rail (CWR) and Civil Thermal Neutral Temperature ($T_N$)</h2>
          <p>
            Modern civil high-speed railway networks eliminate bolted fishplate rail expansion gaps to provide a smooth, low-maintenance ride. Instead, rails are flash-butt welded into continuous strings spanning multiple kilometers (Continuous Welded Rail, CWR). Because the steel rails cannot expand or contract longitudinally, severe thermal stresses develop:
          </p>
          <div class="formula-box">
            $$F_{rail} = A_{rail} \cdot E \cdot \alpha \cdot (T_{rail} - T_N) \quad [\text{N}]$$
          </div>
          <p>
            To manage seasonal extremes, railway track engineers prestress and anchor the rail at a carefully calibrated <strong>Rail Neutral Temperature ($T_N$)</strong>, typically chosen between $27^\circ\text{C}$ and $35^\circ\text{C}$ ($80^\circ\text{F} - 95^\circ\text{F}$). When direct summer solar radiation drives steel rail head temperatures to $60^\circ\text{C}$ ($140^\circ\text{F}$, $\Delta T = +28^\circ\text{C}$), a heavy UIC 60 rail ($A = 7,670\text{ mm}^2$) develops over $515\text{ kN}$ of longitudinal compressive force. If ballast shoulder resistance is inadequate, this force precipitates sudden lateral "sun kink" track buckling, causing derailments. Conversely, extreme winter cold creates massive tensile forces that can snap rails in brittle fracture.
          </p>
        </article>
      </div>

      <aside class="calc-sidebar">
        <div class="sidebar-card">
          <h4>Related Thermal &amp; Piping Calculators</h4>
          <ul class="sidebar-links">
            <li><a href="heat-exchanger-calculator.html">Heat Exchanger LMTD</a></li>
            <li><a href="pipe-sizing-calculator.html">Pipe Sizing &amp; Velocity</a></li>
            <li><a href="pump-flow-calculator.html">Pump Flow &amp; Pipe Velocity</a></li>
            <li><a href="shaft-diameter-calculator.html">Shaft Diameter Sizing</a></li>
            <li><a href="spring-rate-calculator.html">Spring Rate Calculator</a></li>
            <li><a href="cooling-load-calculator.html">Cooling Load Calculator</a></li>
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
      const calcBtn = document.getElementById('calcThermalBtn');
      const resetBtn = document.getElementById('resetThermalBtn');
      const resultBox = document.getElementById('thermalResultBox');

      const materialPreset = document.getElementById('materialPreset');
      const alphaCoeff = document.getElementById('alphaCoeff');
      const elasticModulus = document.getElementById('elasticModulus');

      const matData = {
        '12.0': { alpha: 12.0, e: 200 },
        '17.3': { alpha: 17.3, e: 193 },
        '23.1': { alpha: 23.1, e: 69 },
        '16.5': { alpha: 16.5, e: 117 },
        '18.7': { alpha: 18.7, e: 100 },
        '10.8': { alpha: 10.8, e: 110 },
        '10.0': { alpha: 10.0, e: 30 },
        '54.0': { alpha: 54.0, e: 3 },
        '1.2': { alpha: 1.2, e: 148 }
      };

      materialPreset.addEventListener('change', function() {
        if (this.value !== 'custom' && matData[this.value]) {
          alphaCoeff.value = matData[this.value].alpha;
          elasticModulus.value = matData[this.value].e;
        }
      });

      function calculateThermal() {
        const alpha_val = parseFloat(alphaCoeff.value);
        const L0 = parseFloat(document.getElementById('initLength').value);
        const E_GPa = parseFloat(elasticModulus.value);
        const T_init = parseFloat(document.getElementById('tempInitial').value);
        const T_final = parseFloat(document.getElementById('tempFinal').value);
        const A_cross = parseFloat(document.getElementById('crossSection').value) || 0;
        const D_out = parseFloat(document.getElementById('pipeOuterDia').value) || 0;

        if (isNaN(alpha_val) || alpha_val <= 0 || isNaN(L0) || L0 <= 0 || isNaN(E_GPa) || E_GPa <= 0) {
          alert('Please enter valid positive values for material coefficient, length, and modulus.');
          return;
        }

        const deltaT = T_final - T_init;
        const alpha_scientific = alpha_val * 1e-6;

        // Linear elongation Delta L = L0 * alpha * Delta T [meters]
        const deltaL_m = L0 * alpha_scientific * deltaT;
        const deltaL_mm = deltaL_m * 1000.0;
        const finalLength_m = L0 + deltaL_m;

        // Fully constrained thermal stress sigma = E * alpha * Delta T [MPa]
        const E_MPa = E_GPa * 1000.0;
        const sigma_th = E_MPa * alpha_scientific * Math.abs(deltaT);

        // Restraining anchor force [kN]
        const f_anchor_kN = (sigma_th * A_cross) / 1000.0;

        // Expansion loop sizing (Kellogg formula)
        let loopLeg_m = 0;
        if (D_out > 0 && Math.abs(deltaL_mm) > 0) {
          loopLeg_m = 0.043 * Math.sqrt(D_out * Math.abs(deltaL_mm));
        }

        // Render outputs
        document.getElementById('resDeltaL').textContent = deltaL_mm.toFixed(2) + ' mm (' + (deltaL_mm / 25.4).toFixed(3) + ' in)';
        document.getElementById('resFinalLength').textContent = finalLength_m.toFixed(4) + ' m';
        document.getElementById('resDeltaT').textContent = (deltaT >= 0 ? '+' : '') + deltaT.toFixed(1) + ' °C (' + (deltaT * 1.8).toFixed(1) + ' °F)';
        document.getElementById('resThermalStress').textContent = sigma_th.toFixed(1) + ' MPa (' + (sigma_th * 145.038).toFixed(0) + ' psi)';
        document.getElementById('resAnchorForce').textContent = A_cross > 0 ? (f_anchor_kN.toFixed(1) + ' kN (' + (f_anchor_kN * 0.10197).toFixed(1) + ' tonnes-force)') : 'N/A (Specify Area)';
        document.getElementById('resLoopLength').textContent = loopLeg_m > 0 ? (loopLeg_m.toFixed(2) + ' m leg per ASME B31.3') : 'N/A';

        resultBox.style.display = 'block';
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      calcBtn.addEventListener('click', calculateThermal);
      resetBtn.addEventListener('click', function() {
        resultBox.style.display = 'none';
      });

      calculateThermal();
    });
  </script>
</body>
</html>
"""

def main():
    with open("spring-rate-calculator.html", "w", encoding="utf-8") as f:
        f.write(TOOL_5_HTML.strip() + "\n")
    print("[PASS] spring-rate-calculator.html generated successfully!")

    with open("thermal-expansion-calculator.html", "w", encoding="utf-8") as f:
        f.write(TOOL_6_HTML.strip() + "\n")
    print("[PASS] thermal-expansion-calculator.html generated successfully!")

if __name__ == "__main__":
    main()
