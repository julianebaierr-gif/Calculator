# -*- coding: utf-8 -*-
"""
Script to generate Batch 15 Part 3 tools:
5. half-life-calculator.html
6. henderson-hasselbalch-calculator.html
"""
import os

TOOL_5_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Half-Life Calculator | Radioactive Decay &amp; Isotope Kinetics Sizer</title>
  <meta name="description" content="Calculate radioactive half-life, remaining quantity N(t), initial amount N0, elapsed decay time, decay constant lambda, and mean lifetime for radioisotopes.">
  <link rel="canonical" href="https://calchub.cloud/half-life-calculator.html">
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
        "name": "Half-Life Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates exponential radioactive decay kinetics, remaining isotope mass, elapsed time, decay constant, and activity across seconds, hours, days, and years.",
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
            "name": "What is the mathematical definition of radioactive half-life?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The half-life (t1/2) is the time required for exactly one-half of the unstable atomic nuclei in a radioactive sample to undergo spontaneous nuclear decay: N(t) = N0 * (1/2)^(t / t1/2). It is a fundamental physical constant characteristic of each specific radionuclide."
            }
          },
          {
            "@type": "Question",
            "name": "How is the decay constant (lambda) related to half-life?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The radioactive decay constant (lambda) represents the instantaneous probability of decay per unit time per nucleus. It is inversely proportional to half-life: lambda = ln(2) / t1/2 ≈ 0.69315 / t1/2. The mean lifetime (tau) is tau = 1 / lambda = t1/2 / ln(2)."
            }
          },
          {
            "@type": "Question",
            "name": "How does carbon-14 dating utilize half-life mathematics?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Living organisms maintain an equilibrium ratio of carbon-14 (t1/2 = 5,730 years) to stable carbon-12 through atmospheric carbon exchange. Upon biological death, carbon uptake ceases and C-14 decays exponentially. By measuring residual C-14 activity, archaeologists calculate elapsed time: t = -ln(N / N0) / lambda."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between physical half-life and biological half-life in nuclear medicine?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Physical half-life (Tp) is the nuclear decay rate of the radioisotope (e.g., Tc-99m = 6.01 hours). Biological half-life (Tb) is the physiological clearance rate of the radiopharmaceutical from the human body. The effective half-life (Te) combines both: 1/Te = 1/Tp + 1/Tb."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="chemical">
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
        <a href="civil.html">Civil &amp; Roof</a>
        <a href="solar-energy.html">Solar</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo; 
      <a href="chemical.html">Chemical &amp; Water Treatment</a> &rsaquo; 
      <span>Half-Life Calculator</span>
    </nav>

    <h1 class="tool-title">Radioactive Half-Life &amp; Decay Calculator</h1>
    <p class="tool-subtitle">Exponential Nuclear Kinetics, Remaining Quantity N(t) &amp; Isotope Activity</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="isotopePreset">Radionuclide Standard Preset</label>
            <select id="isotopePreset" class="form-control" onchange="updateIsotopePreset()">
              <option value="c14" selected>Carbon-14 (¹⁴C, t½ = 5,730 years) - Radiocarbon Dating</option>
              <option value="i131">Iodine-131 (¹³¹I, t½ = 8.02 days) - Thyroid Radiotherapy</option>
              <option value="tc99m">Technetium-99m (⁹⁹ᵐTc, t½ = 6.01 hours) - Medical SPECT Imaging</option>
              <option value="cs137">Cesium-137 (¹³⁷Cs, t½ = 30.17 years) - Nuclear Fission Product</option>
              <option value="co60">Cobalt-60 (⁶⁰Co, t½ = 5.27 years) - Industrial Radiography</option>
              <option value="h3">Tritium (³H, t½ = 12.32 years) - Self-Powered Lighting</option>
              <option value="rn222">Radon-222 (²²²Rn, t½ = 3.823 days) - Geological Noble Gas</option>
              <option value="u238">Uranium-238 (²³⁸U, t½ = 4.468 billion years) - Primordial Decay</option>
              <option value="custom">Custom Isotope / Chemical Reaction</option>
            </select>
          </div>

          <div class="form-group">
            <label for="solveHLTarget">Variable to Solve For</label>
            <select id="solveHLTarget" class="form-control" onchange="updateHLInputs()">
              <option value="nt" selected>Remaining Quantity N(t)</option>
              <option value="n0">Initial Quantity (N₀)</option>
              <option value="t">Elapsed Decay Time (t)</option>
              <option value="thalf">Half-Life Duration (t½)</option>
            </select>
          </div>

          <!-- N0 -->
          <div id="n0Group" class="form-group">
            <label for="n0Val">Initial Quantity (N₀) (Grams, Bq, Ci, or %)</label>
            <input type="number" id="n0Val" class="form-control" value="100.0" step="1.0" min="0.000001">
          </div>

          <!-- Half-life Input -->
          <div id="thalfGroup" class="grid-2-col">
            <div class="form-group">
              <label for="thalfVal">Half-Life Value (t½)</label>
              <input type="number" id="thalfVal" class="form-control" value="5730" step="1.0" min="0.000001">
            </div>
            <div class="form-group">
              <label for="thalfUnit">Half-Life Time Units</label>
              <select id="thalfUnit" class="form-control">
                <option value="years" selected>Years</option>
                <option value="days">Days</option>
                <option value="hours">Hours</option>
                <option value="minutes">Minutes</option>
                <option value="seconds">Seconds</option>
              </select>
            </div>
          </div>

          <!-- Elapsed Time Input -->
          <div id="timeGroup" class="grid-2-col">
            <div class="form-group">
              <label for="elapsedTimeVal">Elapsed Decay Time (t)</label>
              <input type="number" id="elapsedTimeVal" class="form-control" value="11460" step="10.0" min="0">
            </div>
            <div class="form-group">
              <label for="elapsedTimeUnit">Elapsed Time Units</label>
              <select id="elapsedTimeUnit" class="form-control">
                <option value="years" selected>Years</option>
                <option value="days">Days</option>
                <option value="hours">Hours</option>
                <option value="minutes">Minutes</option>
                <option value="seconds">Seconds</option>
              </select>
            </div>
          </div>

          <!-- N(t) Input -->
          <div id="ntGroup" class="form-group" style="display:none;">
            <label for="ntVal">Remaining Quantity N(t) (Grams, Bq, Ci, or %)</label>
            <input type="number" id="ntVal" class="form-control" value="25.0" step="0.5" min="0.000001">
          </div>

          <button type="button" class="btn btn-primary" onclick="calcHalfLife()">Solve Radioactive Decay Kinetics</button>
        </div>

        <div id="hlResults" class="results-box" style="display:none;margin-top:1.5rem;">
          <h3 class="results-title">Radioactive Decay &amp; Kinetic Summary</h3>
          <div class="result-grid">
            <div class="result-card">
              <div class="result-label" id="resHLTargetLabel">Calculated Value</div>
              <div class="result-value highlight" id="resHLTargetVal">--</div>
              <div class="result-subtext" id="resHLTargetAlt">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Elapsed Half-Life Cycles</div>
              <div class="result-value" id="resHLCycles">--</div>
              <div class="result-subtext" id="resHLCyclesDesc">n = t / t½</div>
            </div>
            <div class="result-card">
              <div class="result-label">Decay Constant (λ)</div>
              <div class="result-value highlight" id="resLambda">--</div>
              <div class="result-subtext" id="resMeanLife">Mean life τ: --</div>
            </div>
            <div class="result-card">
              <div class="result-label">Fractional Remaining Activity</div>
              <div class="result-value" id="resFractionRem">--</div>
              <div class="result-subtext" id="resFractionDecayed">Decayed: --</div>
            </div>
          </div>

          <div class="result-details" style="margin-top:1rem;padding:1rem;background:var(--card-bg);border-radius:6px;border:1px solid var(--border-light);">
            <h4 style="margin-top:0;">Nuclear Kinetics &amp; Radiometric Diagnostics</h4>
            <ul style="margin-bottom:0;line-height:1.7;">
              <li><strong>Mathematical Decay Equation:</strong> <span id="resDecayEquation">--</span></li>
              <li><strong>Equivalent Scientific Half-Life:</strong> <span id="resEqHalfLife">--</span></li>
              <li><strong>Time Required for 99.9% Decay (10 Half-Lives):</strong> <span id="resTenHalfLives">--</span></li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Related Category Sidebar -->
      <aside class="post-sidebar">
        <div class="sidebar-widget">
          <div class="sidebar-widget-header">
            <span class="widget-icon">🧪</span>
            <h3 class="widget-title">Related Chemical Calculators</h3>
          </div>
          <p class="sidebar-widget-subtitle">Specialized calculation tools in this discipline:</p>
          <ul class="sidebar-links-list">
            <li><a href="dilution-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Solution Dilution (C₁V₁=C₂V₂)</a></li>
            <li><a href="boyles-law-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Boyle's Law Calculator</a></li>
            <li><a href="charles-law-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Charles's Law Calculator</a></li>
            <li><a href="combined-gas-law-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Combined Gas Law Calculator</a></li>
          </ul>
          <div style="margin-top:1.25rem;padding-top:1rem;border-top:1px solid var(--border-light);">
            <a href="chemical.html" class="sidebar-category-link">View All Chemical Calculators &rarr;</a>
          </div>
        </div>
      </aside>
    </div>

    <!-- Technical Educational Article Body (1000+ Words) -->
    <article class="article-body">
      <h2>Thermodynamics and Quantum Physics of Radioactive Decay</h2>
      <p>Radioactive decay is a stochastic quantum tunneling process governed by the weak nuclear and electromagnetic forces. In unstable radionuclides, an excess of protons, neutrons, or nuclear excitation energy renders the nucleus energetically unfavorable relative to lower-mass daughter products. Because individual quantum decay events occur completely independently with a constant probability per unit time ($\lambda$), a macroscopic population of radioactive atoms follows precise, first-order exponential decay kinetics.</p>

      <p>Formulated rigorously by Ernest Rutherford and Frederick Soddy in 1902, the law of radioactive decay represents one of the most reliable chronometers and kinetic models in modern science, underpinning geochronological age dating, radiopharmaceutical dosimetry in oncology, nuclear power fuel cycle burnup calculations, and industrial sterilization safety protocols.</p>

      <h2>Mathematical Derivation of the Exponential Decay Law</h2>
      <p>Let $N(t)$ denote the number of radioactive nuclei present at time $t$. The instantaneous rate of decay (nuclear activity $A = -dN/dt$) is directly proportional to the population size:</p>

      <div class="formula-box">
        $$-\frac{dN}{dt} = \lambda N$$
      </div>

      <p>Where $\lambda$ represents the <strong>decay constant</strong> (units of $\text{time}^{-1}$). Separating variables and integrating from $t = 0$ (where $N = N_0$) to time $t$ yields:</p>

      <div class="formula-box">
        $$\int_{N_0}^{N(t)} \frac{dN}{N} = -\lambda \int_0^t dt \quad \implies \quad \ln\left(\frac{N(t)}{N_0}\right) = -\lambda t$$
      </div>

      <p>Exponentiating both sides yields the classical exponential decay relation:</p>

      <div class="formula-box">
        $$N(t) = N_0 e^{-\lambda t}$$
      </div>

      <h2>Half-Life (t½) and Mean Lifetime (τ) Relationships</h2>
      <p>The <strong>half-life</strong> ($t_{1/2}$) is formally defined as the exact time interval required for the initial radioactive population to decrease by $50\%$ ($N(t_{1/2}) = \frac{N_0}{2}$):</p>

      <div class="formula-box">
        $$\frac{N_0}{2} = N_0 e^{-\lambda t_{1/2}} \quad \implies \quad \frac{1}{2} = e^{-\lambda t_{1/2}} \quad \implies \quad -\ln(2) = -\lambda t_{1/2}$$
      </div>
      <div class="formula-box">
        $$t_{1/2} = \frac{\ln(2)}{\lambda} = \frac{0.693147\dots}{\lambda}, \quad \lambda = \frac{\ln(2)}{t_{1/2}}$$
      </div>

      <p>Substituting $\lambda = \frac{\ln(2)}{t_{1/2}}$ into the exponential decay equation produces the base-2 formulation widely deployed in practical engineering calculations:</p>

      <div class="formula-box">
        $$N(t) = N_0 \left(e^{\ln(2)}\right)^{-\frac{t}{t_{1/2}}} = N_0 \left(\frac{1}{2}\right)^{\frac{t}{t_{1/2}}} = N_0 \cdot 2^{-n}$$
      </div>
      <p>Where $n = \frac{t}{t_{1/2}}$ represents the number of elapsed half-life cycles.</p>

      <p>The <strong>mean lifetime</strong> ($\tau$) represents the average lifespan of an individual unstable nucleus before spontaneous decay occurs:</p>
      <div class="formula-box">
        $$\tau = \frac{1}{\lambda} = \frac{t_{1/2}}{\ln(2)} \approx 1.4427 \times t_{1/2}$$
      </div>

      <h2>Analytical Inversion Formulas for Solving Missing Variables</h2>
      <p>Depending on which thermodynamic variable is unknown, the equation of state is solved algebraically:</p>
      <ul>
        <li><strong>Solving for Initial Quantity ($N_0$):</strong>
        $$N_0 = N(t) \cdot e^{\lambda t} = N(t) \cdot 2^{\frac{t}{t_{1/2}}}$$</li>
        <li><strong>Solving for Elapsed Time ($t$):</strong>
        $$t = \frac{\ln(N_0 / N(t))}{\lambda} = t_{1/2} \cdot \frac{\ln(N_0 / N(t))}{\ln(2)} = t_{1/2} \cdot \log_2\left(\frac{N_0}{N(t)}\right)$$</li>
        <li><strong>Solving for Half-Life ($t_{1/2}$):</strong>
        $$t_{1/2} = \frac{t \cdot \ln(2)}{\ln(N_0 / N(t))}$$</li>
      </ul>

      <h2>Radionuclide Benchmark Reference Table</h2>
      <p>The table below summarizes nuclear physical constants, decay modes, and technological applications across representative radioisotopes per the National Nuclear Data Center (NNDC) / IAEA database:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Radionuclide</th>
              <th>Half-Life (t½)</th>
              <th>Decay Constant λ (s⁻¹)</th>
              <th>Primary Decay Mode</th>
              <th>Specific Activity (Ci/g)</th>
              <th>Key Scientific / Industrial Application</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Carbon-14 (¹⁴C)</td>
              <td>5,730 &plusmn; 40 Years</td>
              <td>3.834 &times; 10⁻¹² s⁻¹</td>
              <td>&beta;⁻ (156 keV max)</td>
              <td>4.46 Ci/g</td>
              <td>Archaeological &amp; Geological Radiocarbon Dating</td>
            </tr>
            <tr>
              <td>Iodine-131 (¹³¹I)</td>
              <td>8.0207 Days</td>
              <td>9.991 &times; 10⁻⁷ s⁻¹</td>
              <td>&beta;⁻ (606 keV), &gamma; (364 keV)</td>
              <td>1.24 &times; 10⁵ Ci/g</td>
              <td>Thyroid Carcinoma &amp; Hyperthyroidism Ablation</td>
            </tr>
            <tr>
              <td>Technetium-99m (⁹⁹ᵐTc)</td>
              <td>6.0067 Hours</td>
              <td>3.205 &times; 10⁻⁵ s⁻¹</td>
              <td>Isomeric Transition &gamma; (140.5 keV)</td>
              <td>5.27 &times; 10⁶ Ci/g</td>
              <td>Medical Diagnostic SPECT Scintigraphy (~80% of scans)</td>
            </tr>
            <tr>
              <td>Cesium-137 (¹³⁷Cs)</td>
              <td>30.17 Years</td>
              <td>7.280 &times; 10⁻¹⁰ s⁻¹</td>
              <td>&beta;⁻ (512 keV), &gamma; (662 keV Ba-137m)</td>
              <td>87.0 Ci/g</td>
              <td>Nuclear Power Plant Fission Product, Soil Erosion Tracer</td>
            </tr>
            <tr>
              <td>Cobalt-60 (⁶⁰Co)</td>
              <td>5.2714 Years</td>
              <td>4.167 &times; 10⁻⁹ s⁻¹</td>
              <td>&beta;⁻ (318 keV), &gamma; (1.17, 1.33 MeV)</td>
              <td>1,130 Ci/g</td>
              <td>Industrial Food Irradiation &amp; Non-Destructive Testing</td>
            </tr>
            <tr>
              <td>Tritium (³H)</td>
              <td>12.32 Years</td>
              <td>1.783 &times; 10⁻⁹ s⁻¹</td>
              <td>&beta;⁻ (18.6 keV pure)</td>
              <td>9,650 Ci/g</td>
              <td>Thermonuclear Fusion Fuel, Self-Luminous Exit Signs</td>
            </tr>
            <tr>
              <td>Radon-222 (²²²Rn)</td>
              <td>3.8235 Days</td>
              <td>2.098 &times; 10⁻⁶ s⁻¹</td>
              <td>&alpha; (5.49 MeV)</td>
              <td>1.54 &times; 10⁵ Ci/g</td>
              <td>Indoor Residential Environmental Lung Carcinogen</td>
            </tr>
            <tr>
              <td>Uranium-238 (²³⁸U)</td>
              <td>4.468 &times; 10⁹ Years</td>
              <td>4.916 &times; 10⁻¹⁸ s⁻¹</td>
              <td>&alpha; (4.20 MeV)</td>
              <td>3.36 &times; 10⁻⁷ Ci/g</td>
              <td>Geological Age of the Earth Determination (U-Pb dating)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Practical Worked Case Study: Radiocarbon Dating of an Ancient Wooden Artifact</h2>
      <div class="worked-example-card">
        <h3>Archaeometric Design Example: Accelerator Mass Spectrometry (AMS) Dating</h3>
        <p><strong>Scenario:</strong> An archaeological excavation unearths an ancient carved wooden roof lintel from an underground tomb. Precision Accelerator Mass Spectrometry (AMS) measures the current specific activity of Carbon-14 in the cellulose sample at $N(t) = 3.65\text{ disintegrations per minute per gram of carbon (dpm/g)}$. Modern pre-industrial living timber displays a standardized baseline activity of $N_0 = 15.30\text{ dpm/g}$. Determine the calendar age of the timber and the calendar date the tree was harvested. Carbon-14 half-life is established at $t_{1/2} = 5,730\text{ years}$ (Libby half-life).</p>

        <p><strong>Step 1: Compute the Radioactive Decay Constant (λ):</strong></p>
        $$\lambda = \frac{\ln(2)}{5,730\text{ years}} = \frac{0.693147}{5,730} = 1.20968 \times 10^{-4}\text{ year}^{-1}$$

        <p><strong>Step 2: Calculate Elapsed Decay Time (t):</strong></p>
        <p>Using the analytical inversion formula:</p>
        $$t = \frac{\ln(N_0 / N(t))}{\lambda} = \frac{\ln(15.30 / 3.65)}{1.20968 \times 10^{-4}} = \frac{\ln(4.19178)}{1.20968 \times 10^{-4}} = \frac{1.43311}{1.20968 \times 10^{-4}} = 11,847\text{ years}$$

        <p><strong>Step 3: Number of Elapsed Half-Life Cycles:</strong></p>
        $$n = \frac{t}{t_{1/2}} = \frac{11,847}{5,730} = 2.0675\text{ half-lives}$$
        <p>After 2 full half-lives ($11,460\text{ years}$), remaining activity drops to $25\%$. The measured $3.65\text{ dpm/g}$ represents $23.86\%$ of modern activity ($3.65 / 15.30 = 0.2386$), verifying the 11,847-year age.</p>

        <p><strong>Step 4: Dendrochronological Tree-Ring Calibration:</strong></p>
        <p>Radiocarbon years before present (BP, benchmarked to 1950 AD) translate to approximately $9,897\text{ BC}$ (&plusmn;65 years), placing the architectural timber within the Pre-Pottery Neolithic A archaeological horizon.</p>
      </div>

      <h2>Ten Half-Life Safety Rule in Health Physics</h2>
      <p>A universal rule of thumb in nuclear waste containment, radiopharmaceutical disposal, and radiological emergency response is the <strong>Ten Half-Life Rule</strong>:</p>
      <ul>
        <li>After 1 half-life: $50\%$ remains ($2^{-1} = 0.50$).</li>
        <li>After 5 half-lives: $3.125\%$ remains ($2^{-5} = 0.03125$).</li>
        <li>After 7 half-lives: $0.78\%$ remains (&lt; 1% threshold).</li>
        <li>After <strong>10 half-lives</strong>: exactly $2^{-10} = \frac{1}{1024} = 0.0977\%$ remains (<strong>&gt; 99.9% decayed</strong>).</li>
      </ul>
      <p>Under US NRC (10 CFR Part 35) and international IAEA protocols, medical radioisotopes with short half-lives (e.g., Iodine-131, Technetium-99m) are stored in decay-in-storage (DIS) lead vaults for a minimum of 10 physical half-lives. Once activity falls below background radiation levels as verified by Geiger-Müller survey meters, waste can be safely incinerated or discarded as conventional medical refuse.</p>
    </article>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-grid">
        <div class="footer-col">
          <div class="footer-logo">
            <span class="logo-icon">&pi;</span>
            <span class="logo-text">Calc<strong>Hub</strong></span>
          </div>
          <p class="footer-about">High-precision nuclear kinetics, radiochemistry, and isotope calculation tools conforming to IAEA, NNDC, and NRC standards.</p>
        </div>
        <div class="footer-col">
          <h4 class="footer-title">Engineering Disciplines</h4>
          <ul class="footer-links">
            <li><a href="chemical.html">Chemical &amp; Water Treatment</a></li>
            <li><a href="mechanical.html">Mechanical &amp; HVAC</a></li>
            <li><a href="engineering.html">Electrical &amp; Electronics</a></li>
            <li><a href="civil.html">Civil &amp; Construction</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4 class="footer-title">Standard References</h4>
          <ul class="footer-links">
            <li><a href="https://www.nndc.bnl.gov" target="_blank" rel="noopener">Brookhaven National Nuclear Data</a></li>
            <li><a href="https://www.iaea.org" target="_blank" rel="noopener">International Atomic Energy Agency</a></li>
            <li><a href="https://www.nrc.gov" target="_blank" rel="noopener">US Nuclear Regulatory Commission</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    const ISOTOPE_PRESETS = {
      c14: { thalf: 5730, unit: "years" },
      i131: { thalf: 8.0207, unit: "days" },
      tc99m: { thalf: 6.0067, unit: "hours" },
      cs137: { thalf: 30.17, unit: "years" },
      co60: { thalf: 5.2714, unit: "years" },
      h3: { thalf: 12.32, unit: "years" },
      rn222: { thalf: 3.8235, unit: "days" },
      u238: { thalf: 4468000000, unit: "years" },
      custom: { thalf: 10, unit: "years" }
    };

    function updateIsotopePreset() {
      const iso = document.getElementById("isotopePreset").value;
      if (iso !== "custom") {
        const p = ISOTOPE_PRESETS[iso];
        document.getElementById("thalfVal").value = p.thalf;
        document.getElementById("thalfUnit").value = p.unit;
      }
    }

    function updateHLInputs() {
      const target = document.getElementById("solveHLTarget").value;
      document.getElementById("n0Group").style.display = target === "n0" ? "none" : "block";
      document.getElementById("thalfGroup").style.display = target === "thalf" ? "none" : "grid";
      document.getElementById("timeGroup").style.display = target === "t" ? "none" : "grid";
      document.getElementById("ntGroup").style.display = target === "nt" ? "none" : "block";
    }

    function toSeconds(val, unit) {
      if (unit === "years") return val * 365.25 * 86400;
      if (unit === "days") return val * 86400;
      if (unit === "hours") return val * 3600;
      if (unit === "minutes") return val * 60;
      return val;
    }

    function fromSeconds(s, unit) {
      if (unit === "years") return s / (365.25 * 86400);
      if (unit === "days") return s / 86400;
      if (unit === "hours") return s / 3600;
      if (unit === "minutes") return s / 60;
      return s;
    }

    function calcHalfLife() {
      const target = document.getElementById("solveHLTarget").value;

      let n0 = parseFloat(document.getElementById("n0Val").value) || 0;
      let nt = parseFloat(document.getElementById("ntVal").value) || 0;
      let thalf_s = toSeconds(parseFloat(document.getElementById("thalfVal").value) || 0, document.getElementById("thalfUnit").value);
      let t_s = toSeconds(parseFloat(document.getElementById("elapsedTimeVal").value) || 0, document.getElementById("elapsedTimeUnit").value);

      let resLabel = "";
      let resVal = "";
      let resAlt = "";

      if (target === "nt") {
        if (n0 <= 0 || thalf_s <= 0) { alert("N0 and Half-Life must be positive non-zero"); return; }
        const cycles = t_s / thalf_s;
        nt = n0 * Math.pow(0.5, cycles);
        resLabel = "Remaining Quantity N(t)";
        resVal = nt >= 0.001 ? nt.toFixed(4) : nt.toExponential(4);
        resAlt = ((nt / n0) * 100).toFixed(2) + "% of initial quantity remaining";
      } else if (target === "n0") {
        if (nt <= 0 || thalf_s <= 0) { alert("N(t) and Half-Life must be positive non-zero"); return; }
        const cycles = t_s / thalf_s;
        n0 = nt * Math.pow(2.0, cycles);
        resLabel = "Initial Quantity (N₀)";
        resVal = n0 >= 0.001 ? n0.toFixed(4) : n0.toExponential(4);
        resAlt = "Decayed to " + nt + " over " + cycles.toFixed(2) + " half-lives";
      } else if (target === "t") {
        if (n0 <= 0 || nt <= 0 || nt >= n0 || thalf_s <= 0) { alert("For decay time: N0 > N(t) > 0 and t½ > 0 required"); return; }
        t_s = thalf_s * (Math.log(n0 / nt) / Math.LN2);
        const outUnit = document.getElementById("elapsedTimeUnit").value;
        const t_disp = fromSeconds(t_s, outUnit);
        resLabel = "Elapsed Decay Time (t)";
        resVal = t_disp.toFixed(3) + " " + outUnit;
        resAlt = (t_s / 86400).toFixed(1) + " days (" + (t_s / (365.25 * 86400)).toFixed(2) + " years)";
      } else if (target === "thalf") {
        if (n0 <= 0 || nt <= 0 || nt >= n0 || t_s <= 0) { alert("For half-life: N0 > N(t) > 0 and t > 0 required"); return; }
        thalf_s = (t_s * Math.LN2) / Math.log(n0 / nt);
        const outUnit = document.getElementById("thalfUnit").value;
        const thalf_disp = fromSeconds(thalf_s, outUnit);
        resLabel = "Half-Life (t½)";
        resVal = thalf_disp.toFixed(3) + " " + outUnit;
        resAlt = (thalf_s / 86400).toFixed(1) + " days (" + (thalf_s / (365.25 * 86400)).toFixed(2) + " years)";
      }

      const cycles = t_s / thalf_s;
      const lambda_s = Math.LN2 / thalf_s;
      const meanLife_s = 1.0 / lambda_s;
      const fracRemaining = Math.pow(0.5, cycles);
      const fracDecayed = (1.0 - fracRemaining) * 100;

      document.getElementById("resHLTargetLabel").textContent = resLabel;
      document.getElementById("resHLTargetVal").textContent = resVal;
      document.getElementById("resHLTargetAlt").textContent = resAlt;

      document.getElementById("resHLCycles").textContent = cycles.toFixed(3) + " Cycles";
      document.getElementById("resHLCyclesDesc").textContent = cycles.toFixed(2) + " half-life intervals elapsed";

      document.getElementById("resLambda").textContent = lambda_s.toExponential(4) + " s⁻¹";
      document.getElementById("resMeanLife").textContent = "Mean lifetime τ: " + (meanLife_s / 86400 >= 365 ? (meanLife_s / (365.25 * 86400)).toFixed(2) + " years" : (meanLife_s / 86400).toFixed(2) + " days");

      document.getElementById("resFractionRem").textContent = (fracRemaining * 100).toFixed(3) + "%";
      document.getElementById("resFractionDecayed").textContent = "Decayed: " + fracDecayed.toFixed(3) + "% (" + (1.0 / fracRemaining).toFixed(1) + "× reduction)";

      document.getElementById("resDecayEquation").textContent = "N(t) = " + (n0 >= 0.001 ? n0.toFixed(2) : n0.toExponential(2)) + " · e^(-" + lambda_s.toExponential(3) + " · t)";
      document.getElementById("resEqHalfLife").textContent = (thalf_s / (365.25*86400) >= 1.0 ? (thalf_s / (365.25*86400)).toFixed(2) + " years" : (thalf_s / 86400).toFixed(2) + " days (" + (thalf_s / 3600).toFixed(1) + " hours)");
      document.getElementById("resTenHalfLives").textContent = (10 * thalf_s / 86400 >= 365 ? (10 * thalf_s / (365.25*86400)).toFixed(2) + " years" : (10 * thalf_s / 86400).toFixed(1) + " days (safe disposal threshold)");

      document.getElementById("hlResults").style.display = "block";
    }
  </script>
</body>
</html>
"""

TOOL_6_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Henderson-Hasselbalch Calculator | Buffer pH &amp; Capacity Sizer</title>
  <meta name="description" content="Calculate buffer solution pH, acid-conjugate base ratio, pKa, and Van Slyke buffer capacity (beta) using the Henderson-Hasselbalch equation.">
  <link rel="canonical" href="https://calchub.cloud/henderson-hasselbalch-calculator.html">
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
        "name": "Henderson-Hasselbalch Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates buffer solution pH, conjugate base to weak acid molar ratios, pKa dissociation constants, and Van Slyke buffer capacity beta.",
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
            "name": "What is the Henderson-Hasselbalch equation and what does it calculate?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The Henderson-Hasselbalch equation relates the pH of a buffer solution to the acid dissociation constant (pKa) of the weak acid and the ratio of conjugate base to weak acid: pH = pKa + log([A-] / [HA]). It allows chemists to predict buffer pH or calculate the required mass/volume ratio of components to achieve a target pH."
            }
          },
          {
            "@type": "Question",
            "name": "At what point does a buffer achieve its maximum buffer capacity?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A buffer achieves its maximum buffer capacity (beta_max) when the molar concentration of the weak acid equals the concentration of the conjugate base: [HA] = [A-]. Under this condition, log([A-]/[HA]) = log(1) = 0, so pH = pKa. The practical operating range of a buffer is generally pKa ± 1.0 pH unit."
            }
          },
          {
            "@type": "Question",
            "name": "How is Van Slyke buffer capacity (beta) mathematically defined?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Buffer capacity (beta) measures the resistance to pH change, defined as the moles of strong base or acid required to change the pH of one liter of buffer by 1.0 unit: beta = d(B) / d(pH) = 2.303 * C * [Ka * [H3O+] / (Ka + [H3O+])^2], where C is the total analytical buffer concentration C = [HA] + [A-]."
            }
          },
          {
            "@type": "Question",
            "name": "Why does temperature affect buffer pH in biological systems?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The acid dissociation constant (Ka) is a thermodynamic property governed by the standard enthalpy of ionization (Delta H°). For amine buffers like Tris (Tris(hydroxymethyl)aminomethane), the temperature coefficient (dpKa/dT) is roughly -0.028 pH units/°C, meaning a Tris buffer calibrated to pH 7.40 at 25°C climbs to pH 8.00 at 4°C."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="chemical">
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
        <a href="civil.html">Civil &amp; Roof</a>
        <a href="solar-energy.html">Solar</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo; 
      <a href="chemical.html">Chemical &amp; Water Treatment</a> &rsaquo; 
      <span>Henderson-Hasselbalch Calculator</span>
    </nav>

    <h1 class="tool-title">Henderson-Hasselbalch Buffer Calculator</h1>
    <p class="tool-subtitle">pH, pKa, Conjugate Acid-Base Ratio &amp; Van Slyke Buffer Capacity (&beta;)</p>

    <div class="calculator-layout">
      <!-- Calculator Core Interface -->
      <div class="calculator-card">
        <div class="calc-form">
          <div class="form-group">
            <label for="bufferPreset">Standard Biological &amp; Chemical Buffer System</label>
            <select id="bufferPreset" class="form-control" onchange="updateBufferPreset()">
              <option value="acetate" selected>Acetic Acid / Sodium Acetate (CH₃COOH / CH₃COO⁻, pKa = 4.76 @ 25°C)</option>
              <option value="phosphate">Phosphate Buffer (H₂PO₄⁻ / HPO₄²⁻, pKa₂ = 7.20 @ 25°C) - Physiological PBS</option>
              <option value="bicarbonate">Carbonic Acid / Bicarbonate (H₂CO₃ / HCO₃⁻, pKa₁ = 6.35 @ 25°C / 6.10 blood)</option>
              <option value="tris">Tris-HCl / Tris Base (pKa = 8.06 @ 25°C) - Molecular Biology / Gel Electrophoresis</option>
              <option value="citrate">Citric Acid / Monosodium Citrate (pKa₁ = 3.13 @ 25°C)</option>
              <option value="hepes">HEPES Buffer (pKa = 7.55 @ 25°C) - Cell Culture Medium</option>
              <option value="custom">Custom Weak Acid / Conjugate Base System</option>
            </select>
          </div>

          <div class="form-group">
            <label for="hhSolveMode">Calculation Objective</label>
            <select id="hhSolveMode" class="form-control" onchange="updateHHInputs()">
              <option value="calc_ph" selected>Calculate Resultant Buffer pH</option>
              <option value="calc_ratio">Calculate Required Base-to-Acid Ratio ([A⁻] / [HA]) for Target pH</option>
              <option value="calc_pka">Calculate Unknown Acid pKa</option>
            </select>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="pkaVal">Acid Dissociation Constant (pKₐ)</label>
              <input type="number" id="pkaVal" class="form-control" value="4.76" step="0.01" min="0" max="14">
            </div>
            <div class="form-group" id="targetPhGroup" style="display:none;">
              <label for="targetPhVal">Target Desired pH</label>
              <input type="number" id="targetPhVal" class="form-control" value="5.00" step="0.05" min="0" max="14">
            </div>
            <div class="form-group" id="measuredPhGroup" style="display:none;">
              <label for="measuredPhVal">Measured Buffer pH</label>
              <input type="number" id="measuredPhVal" class="form-control" value="4.90" step="0.05" min="0" max="14">
            </div>
          </div>

          <div id="concInputsGrid" class="grid-2-col">
            <div class="form-group">
              <label for="weakAcidConc">Weak Acid Concentration [HA] (M or mol/L)</label>
              <input type="number" id="weakAcidConc" class="form-control" value="0.10" step="0.01" min="0.0001">
            </div>
            <div class="form-group">
              <label for="conjBaseConc">Conjugate Base Concentration [A⁻] (M or mol/L)</label>
              <input type="number" id="conjBaseConc" class="form-control" value="0.15" step="0.01" min="0.0001">
            </div>
          </div>

          <div class="grid-2-col">
            <div class="form-group">
              <label for="bufferVolL">Total Buffer Preparation Volume (Liters)</label>
              <input type="number" id="bufferVolL" class="form-control" value="1.0" step="0.1" min="0.01">
            </div>
            <div class="form-group">
              <label for="tempC">Solution Temperature (°C)</label>
              <input type="number" id="tempC" class="form-control" value="25.0" step="1.0">
            </div>
          </div>

          <button type="button" class="btn btn-primary" onclick="calcHendersonHasselbalch()">Compute Buffer Equilibrium &amp; Capacity</button>
        </div>

        <div id="hhResults" class="results-box" style="display:none;margin-top:1.5rem;">
          <h3 class="results-title">Buffer Equilibrium &amp; Van Slyke Diagnostics</h3>
          <div class="result-grid">
            <div class="result-card">
              <div class="result-label" id="resHHTargetLabel">Resultant Buffer pH</div>
              <div class="result-value highlight" id="resHHTargetVal">--</div>
              <div class="result-subtext" id="resHHTargetAlt">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Base-to-Acid Ratio ([A⁻] / [HA])</div>
              <div class="result-value" id="resBaseAcidRatio">--</div>
              <div class="result-subtext" id="resFractionBase">-- % conjugate base</div>
            </div>
            <div class="result-card">
              <div class="result-label">Van Slyke Buffer Capacity (&beta;)</div>
              <div class="result-value highlight" id="resBufferBeta">--</div>
              <div class="result-subtext" id="resBetaMaxComp">--</div>
            </div>
            <div class="result-card">
              <div class="result-label">Total Buffer Strength (C_total)</div>
              <div class="result-value" id="resTotalBufferConc">--</div>
              <div class="result-subtext">[HA] + [A⁻] molarity</div>
            </div>
          </div>

          <div class="result-details" style="margin-top:1rem;padding:1rem;background:var(--card-bg);border-radius:6px;border:1px solid var(--border-light);">
            <h4 style="margin-top:0;">Chemical Speciation &amp; Practical Recipe</h4>
            <ul style="margin-bottom:0;line-height:1.7;">
              <li><strong>Acid Dissociation Constant:</strong> <span id="resKaValue">--</span></li>
              <li><strong>Buffer Working Zone (pKa &plusmn; 1.0):</strong> <span id="resBufferZone">--</span></li>
              <li><strong>Resistance to Strong Acid:</strong> Requires <strong id="resAcidResistance" style="color:var(--primary);">--</strong> of strong acid to depress pH by 1.0 unit.</li>
              <li><strong>Buffer Quality Status:</strong> <span id="resBufferQuality">--</span></li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Related Category Sidebar -->
      <aside class="post-sidebar">
        <div class="sidebar-widget">
          <div class="sidebar-widget-header">
            <span class="widget-icon">🧪</span>
            <h3 class="widget-title">Related Chemical Calculators</h3>
          </div>
          <p class="sidebar-widget-subtitle">Specialized calculation tools in this discipline:</p>
          <ul class="sidebar-links-list">
            <li><a href="dilution-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Solution Dilution (C₁V₁=C₂V₂)</a></li>
            <li><a href="coagulant-dosing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Coagulant Dosing Calculator</a></li>
            <li><a href="caustic-soda-dosing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Caustic Soda Dosing Calculator</a></li>
            <li><a href="alum-dosing-calculator.html" class="sidebar-link-item"><span class="link-bullet">›</span> Alum Dosing Calculator</a></li>
          </ul>
          <div style="margin-top:1.25rem;padding-top:1rem;border-top:1px solid var(--border-light);">
            <a href="chemical.html" class="sidebar-category-link">View All Chemical Calculators &rarr;</a>
          </div>
        </div>
      </aside>
    </div>

    <!-- Technical Educational Article Body (1000+ Words) -->
    <article class="article-body">
      <h2>Thermodynamic Derivation of the Henderson-Hasselbalch Equation</h2>
      <p>The Henderson-Hasselbalch equation is the foundational mathematical expression of acid-base equilibrium in chemistry, biochemistry, and physiological medicine. Originally formulated in 1908 by American physiologist Lawrence Joseph Henderson to describe carbonic acid buffering in blood, and later recast in logarithmic form by Danish chemist Karl Albert Hasselbalch in 1916 using Sørensen's newly introduced pH scale, the equation quantifies how weak acids and their conjugate bases regulate hydronium ion concentration ($[\text{H}_3\text{O}^+]$).</p>

      <p>Consider the reversible Brønsted-Lowry dissociation of a generic weak monoprotic acid ($\text{HA}$) in aqueous media:</p>

      <div class="formula-box">
        $$\text{HA (aq)} + \text{H}_2\text{O (l)} \rightleftharpoons \text{A}^-\text{ (aq)} + \text{H}_3\text{O}^+\text{ (aq)}$$
      </div>

      <p>The thermodynamic acid dissociation constant ($K_a$) is expressed in terms of equilibrium molar concentrations:</p>

      <div class="formula-box">
        $$K_a = \frac{[\text{H}_3\text{O}^+][\text{A}^-]}{[\text{HA}]}$$
      </div>

      <p>Rearranging explicitly for hydronium ion concentration:</p>

      <div class="formula-box">
        $$[\text{H}_3\text{O}^+] = K_a \cdot \frac{[\text{HA}]}{[\text{A}^-]}$$
      </div>

      <p>Taking the negative base-10 logarithm ($-\log_{10}$) across the entire expression, applying the definitions $\text{pH} = -\log[\text{H}_3\text{O}^+]$ and $pK_a = -\log K_a$, and inverting the fractional argument:</p>

      <div class="formula-box">
        $$-\log[\text{H}_3\text{O}^+] = -\log K_a - \log\left(\frac{[\text{HA}]}{[\text{A}^-]}\right) \quad \implies \quad \text{pH} = pK_a + \log\left(\frac{[\text{A}^-]}{[\text{HA}]}\right)$$
      </div>

      <p>Where $[\text{A}^-]$ represents the molar concentration of the conjugate base (proton acceptor) and $[\text{HA}]$ represents the molar concentration of the undissociated weak acid (proton donor).</p>

      <h2>The Chemistry of Maximum Buffer Capacity</h2>
      <p>A buffer solution resists alterations in pH when modest quantities of strong acid ($\text{HCl}$) or strong base ($\text{NaOH}$) are introduced. When equimolar quantities of conjugate base and weak acid are present ($[\text{A}^-] = [\text{HA}]$):</p>

      <div class="formula-box">
        $$\log\left(\frac{[\text{A}^-]}{[\text{HA}]}\right) = \log(1) = 0 \quad \implies \quad \text{pH} = pK_a$$
      </div>

      <p>At this specific equimolar point, the buffer achieves its <strong>maximum buffer capacity</strong>. The solution possesses equal reservoirs of conjugate base to neutralize incoming protons ($\text{A}^- + \text{H}^+ \to \text{HA}$) and weak acid to neutralize incoming hydroxyls ($\text{HA} + \text{OH}^- \to \text{A}^- + \text{H}_2\text{O}$).</p>

      <h2>Van Slyke Buffer Capacity Formulation (β)</h2>
      <p>To quantify buffer strength beyond qualitative observations, American biochemist Donald Dexter Van Slyke defined the buffer value ($\beta$) as the differential quantity of strong base ($dB$) required to produce an incremental shift in pH ($d\text{pH}$):</p>

      <div class="formula-box">
        $$\beta = \frac{dB}{d(\text{pH})} = -\frac{dA}{d(\text{pH})}$$
      </div>

      <p>For a buffer with total analytical concentration $C_{\text{total}} = [\text{HA}] + [\text{A}^-]$, the Van Slyke equation expresses $\beta$ rigorously as:</p>

      <div class="formula-box">
        $$\beta = 2.3026 \cdot C_{\text{total}} \cdot \frac{K_a [\text{H}_3\text{O}^+]}{(K_a + [\text{H}_3\text{O}^+])^2} + 2.3026 \cdot \left([\text{H}_3\text{O}^+] + [\text{OH}^-]\right)$$
      </div>

      <p>In terms of $\text{pH}$ and $pK_a$, the contribution of the weak acid-base conjugate pair is:</p>

      <div class="formula-box">
        $$\beta_{\text{buffer}} = 2.3026 \cdot C_{\text{total}} \cdot \frac{10^{\text{pH} - pK_a}}{(1 + 10^{\text{pH} - pK_a})^2}$$
      </div>

      <p>At peak buffering ($\text{pH} = pK_a$), this simplifies to:</p>
      <div class="formula-box">
        $$\beta_{\text{max}} = \frac{2.3026}{4} \cdot C_{\text{total}} \approx 0.5756 \cdot C_{\text{total}}$$
      </div>
      <p>Thus, buffer capacity scales linearly with total concentration ($C_{\text{total}}$) and reaches its mathematical peak when $\text{pH} = pK_a$. When $\text{pH}$ diverges beyond $pK_a \pm 1.0$, $\beta$ plummets to less than $33\%$ of $\beta_{\text{max}}$, rendering the buffer ineffective.</p>

      <h2>Biological and Chemical Buffer Standards Reference Table</h2>
      <p>The table below summarizes standard buffer systems, thermodynamic $pK_a$ values, temperature coefficients, and practical buffering zones:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Buffer System</th>
              <th>Conjugate Acid (HA)</th>
              <th>Conjugate Base (A⁻)</th>
              <th>pKₐ @ 25°C</th>
              <th>Temp Coeff (dpKa/dT)</th>
              <th>Effective Buffer Range</th>
              <th>Primary Application</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Acetate Buffer</td>
              <td>CH₃COOH (Acetic acid)</td>
              <td>CH₃COO⁻ (Sodium acetate)</td>
              <td>4.76</td>
              <td>+0.0002 / °C</td>
              <td>3.76 &ndash; 5.76</td>
              <td>Enzymology, DNA extraction, tanning</td>
            </tr>
            <tr>
              <td>Phosphate (PBS)</td>
              <td>H₂PO₄⁻ (Dihydrogen phosphate)</td>
              <td>HPO₄²⁻ (Monohydrogen phosphate)</td>
              <td>7.20</td>
              <td>&minus;0.0028 / °C</td>
              <td>6.20 &ndash; 8.20</td>
              <td>Cell biology, intracellular mimic, ELISA</td>
            </tr>
            <tr>
              <td>Carbonate / Blood</td>
              <td>H₂CO₃ / CO₂ (Carbonic acid)</td>
              <td>HCO₃⁻ (Bicarbonate)</td>
              <td>6.10 (blood @ 37°C)</td>
              <td>&minus;0.0055 / °C</td>
              <td>5.10 &ndash; 7.10 (Open system)</td>
              <td>Mammalian blood plasma homeostasis (pH 7.35&ndash;7.45)</td>
            </tr>
            <tr>
              <td>Tris-HCl</td>
              <td>Tris-H⁺ (Tris hydrochloride)</td>
              <td>Tris base (Free amine)</td>
              <td>8.06</td>
              <td>&minus;0.0280 / °C (High)</td>
              <td>7.06 &ndash; 9.06</td>
              <td>Molecular biology, Western blotting, PCR</td>
            </tr>
            <tr>
              <td>HEPES (Good's)</td>
              <td>HEPES zwitterion</td>
              <td>HEPES anion</td>
              <td>7.55</td>
              <td>&minus;0.0140 / °C</td>
              <td>6.55 &ndash; 8.55</td>
              <td>Live mammalian tissue culture incubation</td>
            </tr>
            <tr>
              <td>Citrate Buffer</td>
              <td>Citric acid</td>
              <td>Sodium citrate</td>
              <td>3.13 (pK₁), 4.76 (pK₂)</td>
              <td>&minus;0.0016 / °C</td>
              <td>3.00 &ndash; 6.20 (Multi-protic)</td>
              <td>Anticoagulant blood tubes, food preservation</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Practical Worked Case Study: Preparation of 0.20 M Phosphate Buffer at pH 7.40</h2>
      <div class="worked-example-card">
        <h3>Biochemical Protocol: Preparing Physiological Phosphate Buffer (PBS)</h3>
        <p><strong>Scenario:</strong> A biochemist needs to formulate $V = 1.00\text{ Liter}$ of a $0.200\text{ M}$ total phosphate buffer ($C_{\text{total}} = 0.200\text{ mol/L}$) at physiological $\text{pH } 7.40$ and $25^\circ\text{C}$. The buffer components are monobasic sodium dihydrogen phosphate ($\text{NaH}_2\text{PO}_4$, weak acid $\text{HA}$, $\text{MW} = 119.98\text{ g/mol}$) and dibasic disodium hydrogen phosphate ($\text{Na}_2\text{HPO}_4$, conjugate base $\text{A}^-$, $\text{MW} = 141.96\text{ g/mol}$). For the second dissociation of phosphoric acid ($\text{H}_2\text{PO}_4^- \rightleftharpoons \text{HPO}_4^{2-} + \text{H}^+$), $pK_a = 7.20$.</p>

        <p><strong>Step 1: Determine the Base-to-Acid Ratio via Henderson-Hasselbalch:</strong></p>
        $$\text{pH} = pK_a + \log\left(\frac{[\text{A}^-]}{[\text{HA}]}\right) \implies 7.40 = 7.20 + \log\left(\frac{[\text{A}^-]}{[\text{HA}]}\right)$$
        $$\log\left(\frac{[\text{A}^-]}{[\text{HA}]}\right) = 7.40 - 7.20 = +0.20$$
        $$\frac{[\text{A}^-]}{[\text{HA}]} = 10^{0.20} = 1.5849$$

        <p><strong>Step 2: Solve the Simultaneous Mass Conservation Equations:</strong></p>
        $$[\text{HA}] + [\text{A}^-] = 0.200\text{ M}$$
        $$[\text{A}^-] = 1.5849 \cdot [\text{HA}]$$
        $$[\text{HA}] + 1.5849 \cdot [\text{HA}] = 2.5849 \cdot [\text{HA}] = 0.200\text{ M}$$
        $$[\text{HA}] = \frac{0.200}{2.5849} = 0.07737\text{ M (NaH}_2\text{PO}_4\text{)}$$
        $$[\text{A}^-] = 0.200 - 0.07737 = 0.12263\text{ M (Na}_2\text{HPO}_4\text{)}$$

        <p><strong>Step 3: Calculate Gravimetric Mass Quantities for 1.0 Liter:</strong></p>
        $$m_{\text{NaH}_2\text{PO}_4} = 0.07737\text{ mol} \times 119.98\text{ g/mol} = 9.283\text{ grams}$$
        $$m_{\text{Na}_2\text{HPO}_4} = 0.12263\text{ mol} \times 141.96\text{ g/mol} = 17.409\text{ grams}$$

        <p><strong>Step 4: Compute the Van Slyke Buffer Capacity (β):</strong></p>
        $$\beta = 2.3026 \times 0.200 \times \frac{10^{7.40 - 7.20}}{(1 + 10^{7.40 - 7.20})^2} = 0.4605 \times \frac{1.5849}{(1 + 1.5849)^2} = 0.4605 \times \frac{1.5849}{6.6817} = 0.1092\text{ mol/(L}\cdot\text{pH)}$$
        <p>This means adding $0.1092\text{ moles of strong acid or base}$ to 1 Liter of this buffer will alter the pH by exactly $1.0\text{ unit}$.</p>
      </div>

      <h2>Analytical Limitations of the Henderson-Hasselbalch Equation</h2>
      <p>Chemists must recognize boundary scenarios where the simple equation of state fails:</p>
      <ul>
        <li><strong>Dilute Solutions ($C_{\text{total}} &lt; 10^{-3}\text{ M}$):</strong> The auto-ionization of water ($2\text{H}_2\text{O} \rightleftharpoons \text{H}_3\text{O}^+ + \text{OH}^-$ with $K_w = 1.0 \times 10^{-14}$) contributes significantly to $[\text{H}_3\text{O}^+]$, causing the equation to deviate from real pH.</li>
        <li><strong>Strong Weak Acids ($pK_a &lt; 2.5$ or $pK_a &gt; 11.5$):</strong> The assumption that initial component concentrations equal equilibrium concentrations breaks down because significant spontaneous ionization occurs without added base.</li>
        <li><strong>High Ionic Strength:</strong> At ionic strengths exceeding $I &gt; 0.1\text{ M}$, thermodynamic activities ($\gamma_i [i]$) deviate significantly from concentrations due to Debye-Hückel electrostatic screening, requiring Davies equation activity coefficient adjustments.</li>
      </ul>
    </article>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-grid">
        <div class="footer-col">
          <div class="footer-logo">
            <span class="logo-icon">&pi;</span>
            <span class="logo-text">Calc<strong>Hub</strong></span>
          </div>
          <p class="footer-about">High-precision chemical equilibrium, buffer preparation, and biochemical calculation tools conforming to IUPAC and NIST standards.</p>
        </div>
        <div class="footer-col">
          <h4 class="footer-title">Engineering Disciplines</h4>
          <ul class="footer-links">
            <li><a href="chemical.html">Chemical &amp; Water Treatment</a></li>
            <li><a href="mechanical.html">Mechanical &amp; HVAC</a></li>
            <li><a href="engineering.html">Electrical &amp; Electronics</a></li>
            <li><a href="civil.html">Civil &amp; Construction</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4 class="footer-title">Standard References</h4>
          <ul class="footer-links">
            <li><a href="https://www.iupac.org" target="_blank" rel="noopener">IUPAC Acid-Base Dissociation</a></li>
            <li><a href="https://webbook.nist.gov" target="_blank" rel="noopener">NIST Chemical Kinetics</a></li>
            <li><a href="https://www.sigmaaldrich.com" target="_blank" rel="noopener">Sigma-Aldrich Buffer Guides</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Free, open, client-side engineering tools.</p>
      </div>
    </div>
  </footer>

  <script>
    const BUFFER_PRESETS = {
      acetate: { pka: 4.76, ha: 0.10, a: 0.15 },
      phosphate: { pka: 7.20, ha: 0.08, a: 0.12 },
      bicarbonate: { pka: 6.35, ha: 0.05, a: 0.10 },
      tris: { pka: 8.06, ha: 0.05, a: 0.10 },
      citrate: { pka: 3.13, ha: 0.10, a: 0.10 },
      hepes: { pka: 7.55, ha: 0.05, a: 0.05 },
      custom: { pka: 4.76, ha: 0.10, a: 0.10 }
    };

    function updateBufferPreset() {
      const b = document.getElementById("bufferPreset").value;
      if (b !== "custom") {
        const p = BUFFER_PRESETS[b];
        document.getElementById("pkaVal").value = p.pka;
        document.getElementById("weakAcidConc").value = p.ha;
        document.getElementById("conjBaseConc").value = p.a;
      }
    }

    function updateHHInputs() {
      const mode = document.getElementById("hhSolveMode").value;
      document.getElementById("targetPhGroup").style.display = mode === "calc_ratio" ? "block" : "none";
      document.getElementById("measuredPhGroup").style.display = mode === "calc_pka" ? "block" : "none";
      document.getElementById("concInputsGrid").style.display = mode === "calc_ratio" ? "none" : "grid";
    }

    function calcHendersonHasselbalch() {
      const mode = document.getElementById("hhSolveMode").value;
      const pka = parseFloat(document.getElementById("pkaVal").value) || 4.76;
      const volL = parseFloat(document.getElementById("bufferVolL").value) || 1.0;

      let ha = parseFloat(document.getElementById("weakAcidConc").value) || 0.1;
      let a = parseFloat(document.getElementById("conjBaseConc").value) || 0.1;

      let resLabel = "";
      let resVal = "";
      let resAlt = "";
      let ratio = 1.0;
      let ph = 7.0;

      if (mode === "calc_ph") {
        if (ha <= 0 || a <= 0) { alert("[HA] and [A-] concentrations must be positive non-zero"); return; }
        ratio = a / ha;
        ph = pka + Math.log10(ratio);
        resLabel = "Resultant Buffer pH";
        resVal = ph.toFixed(2);
        resAlt = "pKa (" + pka.toFixed(2) + ") + log(" + ratio.toFixed(3) + ") = " + (Math.log10(ratio) >= 0 ? "+" : "") + Math.log10(ratio).toFixed(3);
      } else if (mode === "calc_ratio") {
        const targetPh = parseFloat(document.getElementById("targetPhVal").value) || 7.0;
        const diff = targetPh - pka;
        ratio = Math.pow(10, diff);
        ph = targetPh;
        ha = 0.1; // nominal
        a = ha * ratio;
        resLabel = "Required [A⁻] / [HA] Ratio";
        resVal = ratio.toFixed(4) + " : 1";
        resAlt = "To achieve target pH " + targetPh.toFixed(2) + " with pKa " + pka.toFixed(2);
      } else if (mode === "calc_pka") {
        if (ha <= 0 || a <= 0) { alert("[HA] and [A-] concentrations must be positive non-zero"); return; }
        const measPh = parseFloat(document.getElementById("measuredPhVal").value) || 7.0;
        ratio = a / ha;
        const calcPka = measPh - Math.log10(ratio);
        ph = measPh;
        resLabel = "Calculated pKₐ";
        resVal = calcPka.toFixed(2);
        resAlt = "Ka = " + Math.pow(10, -calcPka).toExponential(3);
      }

      // Van Slyke buffer capacity
      const c_total = ha + a;
      const ka = Math.pow(10, -pka);
      const diffPH = ph - pka;
      const expTerm = Math.pow(10, diffPH);
      const beta = 2.3026 * c_total * (expTerm / Math.pow(1 + expTerm, 2));
      const betaMax = 0.5756 * c_total;

      const fracBase = (a / (ha + a)) * 100;
      const acidResistance = (beta * volL).toFixed(3);

      document.getElementById("resHHTargetLabel").textContent = resLabel;
      document.getElementById("resHHTargetVal").textContent = resVal;
      document.getElementById("resHHTargetAlt").textContent = resAlt;

      document.getElementById("resBaseAcidRatio").textContent = ratio.toFixed(3) + " : 1";
      document.getElementById("resFractionBase").textContent = fracBase.toFixed(1) + "% conjugate base (" + (100 - fracBase).toFixed(1) + "% weak acid)";

      document.getElementById("resBufferBeta").textContent = beta.toFixed(4) + " mol/(L·pH)";
      document.getElementById("resBetaMaxComp").textContent = ((beta / betaMax) * 100).toFixed(1) + "% of peak capacity (" + betaMax.toFixed(3) + " max)";

      document.getElementById("resTotalBufferConc").textContent = c_total.toFixed(3) + " M (" + (c_total * volL).toFixed(3) + " total moles in " + volL + " L)";

      document.getElementById("resKaValue").textContent = "Ka = " + ka.toExponential(3) + " (pKa = " + pka.toFixed(2) + ")";
      document.getElementById("resBufferZone").textContent = "pH " + (pka - 1.0).toFixed(2) + " to " + (pka + 1.0).toFixed(2) + " (Buffer is currently at pH " + ph.toFixed(2) + ")";
      document.getElementById("resAcidResistance").textContent = acidResistance + " moles";

      let qual = "";
      if (Math.abs(ph - pka) <= 0.3) {
        qual = "OPTIMAL: Outstanding buffering capacity (Within ±0.3 pH of pKa).";
      } else if (Math.abs(ph - pka) <= 1.0) {
        qual = "GOOD: Functional buffering zone (Within ±1.0 pH unit of pKa).";
      } else {
        qual = "POOR: Beyond optimal buffering range (|pH - pKa| > 1.0). High risk of pH breakthrough.";
      }
      document.getElementById("resBufferQuality").textContent = qual;

      document.getElementById("hhResults").style.display = "block";
    }
  </script>
</body>
</html>
"""

def generate():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p1 = os.path.join(root, "half-life-calculator.html")
    p2 = os.path.join(root, "henderson-hasselbalch-calculator.html")
    
    with open(p1, "w", encoding="utf-8") as f:
        f.write(TOOL_5_HTML.strip() + "\n")
    print(f"Generated {p1}")

    with open(p2, "w", encoding="utf-8") as f:
        f.write(TOOL_6_HTML.strip() + "\n")
    print(f"Generated {p2}")

if __name__ == "__main__":
    generate()
